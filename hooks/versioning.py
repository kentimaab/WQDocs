"""
Per-product versioning: archive a version of MOD, BMS or WWT with mike.

Archiving freezes one product, in both languages, at /docs/<product>/<version>/ and
/docs/sv/<product>/<version>/. The archives live on the `versions` branch, which the deploy
workflow lays over the built site. Each product keeps its own versions.json next to its
archives.

docs/current-versions.json says what each product's current version is (update it when a
release goes live):
  {"live": "MOD 2027.1.0"} the live pages are current, shown under that name
  {"pinned": "2026.1.1"}   the live pages aren't released: the archived version is current,
                           and the deploy's `pin` step turns the product's live pages into
                           redirects to it, out of the search and the sitemap
The version menu (assets/javascripts/version-select.js) reads both files on a product's
pages. Archived pages load the menu's script and stylesheet from the live site, so menu
changes reach them.

Each language is staged under .versions-build/<lang>/<product>/:
  src/      the language's docs tree without Images/, preprocessed like CI does
            (script_deps.py, English only). The MOD snippets are included from here.
  docs/     the product's pages and the assets they need. Links that leave the product
            are rewritten to the live pages, since the archive holds only this product.
            Screenshots are linked as /docs/Images/... already, so archives share them.
  zensical.toml   the language's config, cut down to the product.
The staged site is built strictly first, then mike builds it again and commits it.

A version whose docs have since moved on is archived from the commit where they were
final, with --ref: the pages, MOD snippets and the product's nav come from that commit,
while the theme, stylesheets, scripts and the other tabs are today's.

Usage:
    python hooks/versioning.py build bms 2026.1.1       # build only, kept for preview --local
    python hooks/versioning.py preview --local          # live site/ + what build made, no mike
    python hooks/versioning.py archive bms 2026.1.1     # commit to the versions branch
    python hooks/versioning.py archive bms 2026.1.1 --push
    python hooks/versioning.py archive bms 2026.1.0 --ref 9667d82 --title "BMS 2026.1.0"
    python hooks/versioning.py pin site                 # deploy step, after the archives
    python hooks/versioning.py preview                  # live site/ + archives, locally

Archiving needs the Zensical fork of mike (not on PyPI):
    pip install "mike @ git+https://github.com/squidfunk/mike.git"
"""
import argparse
import http.server
import io
import json
import os
import posixpath
import re
import shutil
import subprocess
import sys
import tarfile
import tomllib
import zipfile
from urllib.parse import quote, unquote

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STAGE = os.path.join(REPO, '.versions-build')
CURRENT = os.path.join(REPO, 'docs', 'current-versions.json')
LOCAL = os.path.join(STAGE, 'local')
BRANCH = 'versions'
SITE_URL = 'https://www.widequick.com/docs/'
PRODUCTS = {'mod': 'MOD', 'bms': 'BMS', 'wwt': 'WWT'}

# (name, config, docs dir, URL prefix below /docs/, preprocessed with script_deps.py in CI)
LANGUAGES = [
    ('en', 'zensical.toml', 'docs', '', True),
    ('sv', 'zensical-sv.toml', 'docs-sv', 'sv/', False),
]

# Assets every archive needs besides the ones its pages link to.
BASE_ASSETS = ['assets/stylesheets', 'assets/javascripts']

# Loaded from the live site by every archive, so a change to the version menu reaches them all
LIVE_ASSETS = ['assets/javascripts/version-select.js', 'assets/stylesheets/version-select.css']

LINK_RE = re.compile(r'(\]\()(<[^>]+>|[^)\s]+)')
ATTR_RE = re.compile(r'\b(href|src)="([^"]+)"')
FENCE_RE = re.compile(r'^\s*(```|~~~)')


def fwd(path):
    return path.replace(os.sep, '/')


def page_url(path):
    """URL path of a docs file: 'mod/x/index.md' -> 'mod/x/', 'mod/x.md' -> 'mod/x/'."""
    if path == 'index.md':
        return ''
    if path.endswith('/index.md'):
        return path[:-len('index.md')]
    if path.endswith('.md'):
        return path[:-3] + '/'
    return path


def rewrite_url(url, page_dir, product, prefix, assets):
    """Point a link that leaves the product at the live site; keep the rest.

    page_dir is the page's folder below the language docs root, e.g. 'bms/modules/x'.
    Links to docs/assets/ stay relative and the asset is copied into the archive.
    """
    if not url or url.startswith(('http:', 'https:', 'mailto:', '#', 'data:', '//', '/docs/')):
        return url
    if url.startswith('/'):
        # Root-relative links are written from the docs root, e.g. /mod/modules/
        return '/docs/' + prefix + url.lstrip('/')
    path, hashmark, anchor = url.partition('#')
    target = posixpath.normpath(posixpath.join(page_dir, unquote(path)))
    staged_dir = posixpath.relpath(page_dir, product)
    if target == product or target.startswith(product + '/'):
        # In the archive the product folder is the root, so a link that climbs out of
        # it and back in (../../bms/x.md) has to take the short way.
        if not posixpath.normpath(posixpath.join(staged_dir, unquote(path))).startswith('..'):
            return url
        short = quote(posixpath.relpath(target, page_dir), safe='/') + ('/' if path.endswith('/') else '')
        return short + hashmark + anchor
    if target.startswith('assets/'):
        assets.add(target)
        return posixpath.relpath(target, staged_dir) + hashmark + anchor
    return '/docs/' + prefix + quote(page_url(target), safe='/') + hashmark + anchor


def rewrite_page(text, page_dir, product, prefix, assets):
    out, fenced = [], False
    for line in text.split('\n'):
        if FENCE_RE.match(line):
            fenced = not fenced
        elif not fenced:
            def md(m):
                url = m.group(2)
                if url.startswith('<') and url.endswith('>'):
                    return m.group(1) + '<' + rewrite_url(url[1:-1], page_dir, product, prefix, assets) + '>'
                return m.group(1) + rewrite_url(url, page_dir, product, prefix, assets)
            line = LINK_RE.sub(md, line)
            line = ATTR_RE.sub(lambda m: '%s="%s"' % (m.group(1), rewrite_url(m.group(2), page_dir, product, prefix, assets)), line)
        out.append(line)
    return '\n'.join(out)


def md_paths(node):
    if isinstance(node, str):
        yield node
    elif isinstance(node, list):
        for x in node:
            yield from md_paths(x)
    elif isinstance(node, dict):
        for x in node.values():
            yield from md_paths(x)


def strip_prefix(node, product):
    if isinstance(node, str):
        return node[len(product) + 1:] if node.startswith(product + '/') else node
    if isinstance(node, list):
        return [strip_prefix(x, product) for x in node]
    return {k: strip_prefix(v, product) for k, v in node.items()}


def toml_value(v):
    if isinstance(v, str):
        return '"' + v.replace('\\', '\\\\').replace('"', '\\"') + '"'
    if isinstance(v, bool):
        return 'true' if v else 'false'
    if isinstance(v, list):
        return '[' + ', '.join(toml_value(x) for x in v) + ']'
    if isinstance(v, dict):
        return '{ ' + ', '.join('%s = %s' % (toml_value(k), toml_value(x)) for k, x in v.items()) + ' }'
    return str(v)


def product_section(nav, product):
    """The top-level nav entry holding the product's pages, as (index, title, value)."""
    found = [(i, title, value) for i, item in enumerate(nav) for title, value in item.items()
             if isinstance(value, list) and all(p.startswith(product + '/') for p in md_paths(value))]
    if len(found) != 1:
        sys.exit('expected one top-level nav section for %s, found %d' % (product, len(found)))
    return found[0]


def product_config(config_text, product, prefix, src, ref_config_text=None):
    """The language's config, cut down to one product.

    The top level of the nav stays whole, so an archive shows the same tabs as the live site:
    the product's own section holds the archived pages, and every other entry links to the
    live site. The logo links to the live home page too.

    Archiving an earlier commit takes the product's pages from that commit's config
    (ref_config_text) and everything else, theme and tabs included, from today's.
    """
    cfg = tomllib.loads(config_text)['project']
    own, own_title, own_value = product_section(cfg['nav'], product)
    if ref_config_text:
        own_value = product_section(tomllib.loads(ref_config_text)['project']['nav'], product)[2]
    nav = []
    for i, item in enumerate(cfg['nav']):
        (title, value), = item.items()
        if i == own:
            nav.append({own_title: strip_prefix(own_value, product)})
        else:
            # The live page the tab opens: a section's first page, as the theme does
            nav.append({title: '/docs/' + prefix + quote(page_url(next(md_paths(value))), safe='/')})

    def replace(pattern, value, text, required=True):
        new, n = re.subn(pattern, lambda m: value, text, count=1, flags=re.M | re.S)
        if required and not n:
            sys.exit('config pattern not found: ' + pattern)
        return new

    text = config_text
    text = replace(r'^nav = \[.*?^\]\n', 'nav = ' + toml_value(nav) + '\n', text)
    text = replace(r'^site_url = .*?$', 'site_url = ' + toml_value(SITE_URL + prefix + product + '/'), text)
    text = replace(r'^docs_dir = .*?\n', '', text, required=False)
    text = replace(r'^site_dir = .*?\n', '', text, required=False)
    text = replace(r'^\[project\]\n', '[project]\ndocs_dir = "docs"\nsite_dir = "site"\n', text)
    text = replace(r'^custom_dir = .*?$', 'custom_dir = ' + toml_value(fwd(os.path.join(REPO, 'overrides'))), text)
    text = replace(r'^base_path = .*?$', 'base_path = [' + toml_value(fwd(src)) + ']', text)
    text = replace(r'^exclude_docs = """.*?"""\n', 'exclude_docs = """\narchive/\n"""\n', text, required=False)
    text = replace(r'^\[project\.extra\]\n', '[project.extra]\nhomepage = %s\n' % toml_value('/docs/' + prefix), text)
    for a in LIVE_ASSETS:
        text = text.replace(toml_value(a), toml_value('/docs/' + a))
    text = text.rstrip('\n') + '\n\n[project.plugins.mike]\ndeploy_prefix = %s\nversion_selector = false\n' % toml_value(prefix + product)
    return text, cfg


def git_show(ref, path):
    """A file as it was at `ref`, or None when it didn't exist then."""
    r = subprocess.run(['git', 'show', '%s:%s' % (ref, path)], cwd=REPO, capture_output=True)
    return r.stdout.decode('utf-8') if r.returncode == 0 else None


def checkout_docs(ref, docs, dest):
    """The docs tree as it was at `ref`, without Images/, into dest."""
    tar = subprocess.run(['git', 'archive', '--format=tar', ref, '--', docs, ':(exclude)%s/Images' % docs],
                         cwd=REPO, capture_output=True, check=True).stdout
    with tarfile.open(fileobj=io.BytesIO(tar)) as t:
        for m in t.getmembers():
            if m.isfile() and m.name.startswith(docs + '/'):
                target = os.path.join(dest, *m.name[len(docs) + 1:].split('/'))
                os.makedirs(os.path.dirname(target), exist_ok=True)
                with t.extractfile(m) as f, open(target, 'wb') as out:
                    shutil.copyfileobj(f, out)


def stage(product, lang, ref=None):
    name, config, docs, prefix, preprocess = lang
    root = os.path.join(STAGE, name, product)
    src = os.path.join(root, 'src')
    out = os.path.join(root, 'docs')
    shutil.rmtree(root, ignore_errors=True)
    if ref:
        # Pages, MOD snippets and the preprocessor as they were at that commit
        checkout_docs(ref, docs, src)
        deps = git_show(ref, 'hooks/script_deps.py')
        if deps is not None:
            deps_path = os.path.join(root, 'script_deps.py')
            open(deps_path, 'w', encoding='utf-8').write(deps)
        else:
            deps_path = None
    else:
        shutil.copytree(os.path.join(REPO, docs), src,
                        ignore=lambda d, names: ['Images'] if os.path.samefile(d, os.path.join(REPO, docs)) else [])
        deps_path = os.path.join(REPO, 'hooks', 'script_deps.py')
    if preprocess and deps_path:
        subprocess.run([sys.executable, deps_path, src], check=True)

    shutil.copytree(os.path.join(src, product), out, ignore=shutil.ignore_patterns('archive'))
    assets = set()
    for dp, dn, fn in os.walk(out):
        for f in fn:
            if not f.endswith('.md'):
                continue
            p = os.path.join(dp, f)
            page_dir = posixpath.normpath(product + '/' + fwd(os.path.relpath(dp, out)))
            text = open(p, encoding='utf-8').read()
            new = rewrite_page(text, page_dir, product, prefix, assets)
            if new != text:
                open(p, 'w', encoding='utf-8', newline='').write(new)

    ref_config = git_show(ref, config) if ref else None
    if ref and ref_config is None:
        sys.exit('%s has no %s' % (ref, config))
    text, cfg = product_config(open(os.path.join(REPO, config), encoding='utf-8').read(), product, prefix, src, ref_config)
    theme = cfg.get('theme', {})
    # Stylesheets and scripts are always today's, so every archive has the version menu and
    # looks like the live site; the images its pages link to come with the pages.
    wanted = [(a, os.path.join(REPO, docs)) for a in BASE_ASSETS]
    wanted += [(a, src) for a in sorted(assets | {theme[k] for k in ('logo', 'favicon') if k in theme})]
    for a, base in wanted:
        s, d = os.path.join(base, a), os.path.join(out, a)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        elif os.path.isfile(s):
            os.makedirs(os.path.dirname(d), exist_ok=True)
            shutil.copy2(s, d)
        else:
            print('warning: %s links to missing %s' % (product, a))
    for a in LIVE_ASSETS:
        if os.path.isfile(os.path.join(out, a)):
            os.remove(os.path.join(out, a))
    open(os.path.join(root, 'zensical.toml'), 'w', encoding='utf-8').write(text)
    return root, prefix + product


def zensical_build(root, version):
    env = dict(os.environ, MIKE_DOCS_VERSION=version)
    subprocess.run(['zensical', 'build', '--clean', '--strict', '--config-file', 'zensical.toml'],
                   cwd=root, env=env, check=True)


def version_key(version):
    return [(0, int(x)) if x.isdigit() else (1, x) for x in re.split(r'[.\-]', version)]


def keep_local(root, deploy_prefix, version, title):
    """Lay a build out the way mike does on the versions branch, for `preview --local`."""
    base = os.path.join(LOCAL, *deploy_prefix.split('/'))
    dest = os.path.join(base, version)
    shutil.rmtree(dest, ignore_errors=True)
    shutil.copytree(os.path.join(root, 'site'), dest)
    listing = os.path.join(base, 'versions.json')
    versions = json.load(open(listing, encoding='utf-8')) if os.path.isfile(listing) else []
    versions = [v for v in versions if v['version'] != version]
    versions.append({'version': version, 'title': title, 'aliases': []})
    versions.sort(key=lambda v: version_key(v['version']), reverse=True)
    json.dump(versions, open(listing, 'w', encoding='utf-8'), indent=2)


def cmd_build(args):
    title = args.title or '%s %s' % (PRODUCTS[args.product], args.version)
    for lang in LANGUAGES:
        root, deploy_prefix = stage(args.product, lang, args.ref)
        zensical_build(root, args.version)
        keep_local(root, deploy_prefix, args.version, title)
        print('built %s/%s/, for `preview --local`' % (deploy_prefix, args.version))


def cmd_archive(args):
    if not shutil.which('mike'):
        sys.exit('mike not found. Install the Zensical fork: pip install "mike @ git+https://github.com/squidfunk/mike.git"')
    title = args.title or '%s %s' % (PRODUCTS[args.product], args.version)
    source = ' from %s' % args.ref if args.ref else ''
    for lang in LANGUAGES:
        root, deploy_prefix = stage(args.product, lang, args.ref)
        zensical_build(root, args.version)
        cmd = ['mike', 'deploy', '--config-file', 'zensical.toml', '--branch', args.branch,
               '--deploy-prefix', deploy_prefix, '--title', title,
               '--message', 'Archive %s (%s)%s' % (title, lang[0], source)]
        if args.push:
            cmd.append('--push')
        subprocess.run(cmd + [args.version], cwd=root, check=True)
        print('archived %s/%s/ on %s' % (deploy_prefix, args.version, args.branch))


def pinned_versions():
    """{product: version} for the products whose current version is an archive."""
    return {p: e['pinned'] for p, e in json.load(open(CURRENT, encoding='utf-8')).items() if e.get('pinned')}


def redirect_page(url):
    return ('<!doctype html>\n<html>\n<head>\n<meta charset="utf-8">\n<title>Redirecting</title>\n'
            '<link rel="canonical" href="{0}">\n<meta name="robots" content="noindex">\n'
            '<script>location.replace("{0}" + location.hash)</script>\n'
            '<meta http-equiv="refresh" content="0; url={0}">\n</head>\n'
            '<body><a href="{0}">{0}</a></body>\n</html>\n').format(url)


def pin_product(site, prefix, product, version):
    """Point a product's live pages at its pinned archive, page by page."""
    root = os.path.join(site, *(prefix + product).split('/'))
    pinned = os.path.join(root, version)
    if not os.path.isfile(os.path.join(pinned, 'index.html')):
        sys.exit('%s%s is pinned to %s, which is not archived on the %s branch' % (prefix, product, version, BRANCH))
    archived = {v['version'] for v in json.load(open(os.path.join(root, 'versions.json'), encoding='utf-8'))}
    base = '/docs/' + prefix + product + '/'
    pages = 0
    for dp, dn, fn in os.walk(root):
        if os.path.samefile(dp, root):
            dn[:] = [d for d in dn if d not in archived]
        for f in fn:
            if not f.endswith('.html'):
                continue
            rel = fwd(os.path.relpath(os.path.join(dp, f), root))
            page = rel[:-len('index.html')] if rel.endswith('index.html') else rel
            same = os.path.isfile(os.path.join(pinned, *rel.split('/')))
            url = base + version + '/' + (quote(page, safe='/') if same else '')
            open(os.path.join(dp, f), 'w', encoding='utf-8', newline='\n').write(redirect_page(url))
            pages += 1

    lang_root = os.path.join(site, *prefix.split('/')) if prefix else site
    search_path = os.path.join(lang_root, 'search.json')
    search, removed = unpinned_search(open(search_path, encoding='utf-8').read(), [product])
    open(search_path, 'w', encoding='utf-8').write(search)
    sitemap_path = os.path.join(lang_root, 'sitemap.xml')
    sitemap, dropped = unpinned_sitemap(open(sitemap_path, encoding='utf-8').read(), prefix, [product])
    open(sitemap_path, 'w', encoding='utf-8').write(sitemap)
    print('pinned %s%s to %s: %d pages redirect, %d search entries and %d sitemap entries removed'
          % (prefix, product, version, pages, removed, dropped))


# A pinned product's live pages leave the live site's search, and its sitemap: instant
# navigation only takes over links that are in the sitemap, so these load as whole pages and
# the redirect runs. Otherwise the theme would fetch them in the background, follow the
# redirect unseen and show the archive under the live address.
def unpinned_search(text, products):
    search = json.loads(text)
    before = len(search['items'])
    search['items'] = [i for i in search['items']
                       if not any(i['location'].startswith(p + '/') for p in products)]
    return json.dumps(search, ensure_ascii=False, separators=(',', ':')), before - len(search['items'])


def unpinned_sitemap(text, prefix, products):
    dropped = 0
    for p in products:
        text, n = re.subn(r'\s*<url>\s*<loc>[^<]*/docs/%s%s/[^<]*</loc>.*?</url>' % (re.escape(prefix), re.escape(p)),
                          '', text, flags=re.S)
        dropped += n
    return text, dropped


def cmd_pin(args):
    pins = pinned_versions()
    for product, version in sorted(pins.items()):
        for lang in LANGUAGES:
            pin_product(os.path.abspath(args.site), lang[3], product, version)
    if not pins:
        print('no pinned products')


def cmd_preview(args):
    site = os.path.join(REPO, 'site')
    if not os.path.isdir(site):
        sys.exit('build the live site first: zensical build -f zensical.toml and -f zensical-sv.toml')
    if args.local:
        # What `build` has laid out, no branch or mike involved
        archives = LOCAL
        if not os.path.isdir(archives):
            print('nothing built yet: run `build` for the versions to preview first')
    else:
        archives = os.path.join(STAGE, 'preview')
        shutil.rmtree(archives, ignore_errors=True)
        os.makedirs(archives)
        zipped = subprocess.run(['git', 'archive', '--format=zip', args.branch], cwd=REPO,
                                capture_output=True)
        if zipped.returncode:
            print('no %s branch yet, previewing the live site only' % args.branch)
        else:
            zipfile.ZipFile(io.BytesIO(zipped.stdout)).extractall(archives)
    pins = pinned_versions()

    def pinned_target(path):
        """Where the deployed site sends a pinned product's live page, as the pin step does."""
        for product, version in pins.items():
            for prefix in [lang[3] for lang in LANGUAGES]:
                base = '/docs/' + prefix + product + '/'
                if not path.startswith(base):
                    continue
                rest = path[len(base):]
                listing = os.path.join(archives, *(prefix + product).split('/'), 'versions.json')
                archived = {v['version'] for v in json.load(open(listing, encoding='utf-8'))} if os.path.isfile(listing) else set()
                if rest.split('/')[0] in archived or rest == 'versions.json':
                    return None
                page = os.path.join(archives, *(prefix + product).split('/'), version, *rest.split('/'))
                same = os.path.isfile(os.path.join(page, 'index.html')) or os.path.isfile(page)
                return base + version + '/' + (quote(rest, safe='/') if same else '')
        return None

    class Handler(http.server.SimpleHTTPRequestHandler):
        # /docs/... is served from the archives first, then from site/, as on the server.
        def translate_path(self, path):
            path = unquote(path.split('?', 1)[0].split('#', 1)[0])
            if not path.startswith('/docs/'):
                return os.path.join(site, '__missing__')
            rel = path[len('/docs/'):]
            for base in (archives, site):
                full = os.path.join(base, *rel.split('/'))
                if os.path.isdir(full) and os.path.isfile(os.path.join(full, 'index.html')) or os.path.isfile(full):
                    return full
            return os.path.join(site, *rel.split('/'))

        def redirected(self):
            path = unquote(self.path.split('?', 1)[0].split('#', 1)[0])
            target = '/docs/' if path in ('/', '') else pinned_target(path)
            if target:
                self.send_response(302)
                self.send_header('Location', target)
                self.end_headers()
            return bool(target)

        def unpinned(self):
            """The sitemap and search index as the pin step leaves them on the server."""
            path = unquote(self.path.split('?', 1)[0])
            for prefix in [lang[3] for lang in LANGUAGES]:
                if pins and path in ('/docs/%ssitemap.xml' % prefix, '/docs/%ssearch.json' % prefix):
                    text = open(self.translate_path(path), encoding='utf-8').read()
                    if path.endswith('.xml'):
                        body, kind = unpinned_sitemap(text, prefix, list(pins))[0], 'application/xml'
                    else:
                        body, kind = unpinned_search(text, list(pins))[0], 'application/json'
                    body = body.encode('utf-8')
                    self.send_response(200)
                    self.send_header('Content-Type', kind)
                    self.send_header('Content-Length', str(len(body)))
                    self.end_headers()
                    return body
            return None

        def do_GET(self):
            if self.redirected():
                return
            body = self.unpinned()
            if body is not None:
                self.wfile.write(body)
                return
            super().do_GET()

        def do_HEAD(self):
            if not self.redirected():
                super().do_HEAD()

    print('serving http://localhost:%d/docs/ (Ctrl+C to stop)' % args.port)
    http.server.ThreadingHTTPServer(('localhost', args.port), Handler).serve_forever()


def main():
    # mike runs `zensical build` by name, so the zensical next to this Python must be found
    # even when its environment isn't activated.
    os.environ['PATH'] = os.path.dirname(sys.executable) + os.pathsep + os.environ.get('PATH', '')
    parser = argparse.ArgumentParser(description=__doc__.split('\n\n')[1],
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='command', required=True)
    for name, fn, help_text in (('build', cmd_build, 'stage and build a version, without committing'),
                                ('archive', cmd_archive, 'archive a version on the versions branch')):
        p = sub.add_parser(name, help=help_text)
        p.add_argument('product', choices=sorted(PRODUCTS))
        p.add_argument('version', help='e.g. 2026.1.1')
        p.add_argument('--ref', help='take the pages from this commit instead of the working tree')
        p.add_argument('--title', help='name in the version menu (default: "BMS 2026.1.1" and so on)')
        p.set_defaults(fn=fn)
        if name == 'archive':
            p.add_argument('--push', action='store_true', help='push the versions branch to origin')
            p.add_argument('--branch', default=BRANCH,
                           help='branch to commit to, e.g. a throwaway one to preview with (default: %(default)s)')
    p = sub.add_parser('pin', help='deploy step: point pinned products at their archived version')
    p.add_argument('site', help='the built site, with the archives already in it')
    p.set_defaults(fn=cmd_pin)
    p = sub.add_parser('preview', help='serve the live site with the archived versions on top')
    p.add_argument('--port', type=int, default=8000)
    p.add_argument('--branch', default=BRANCH)
    p.add_argument('--local', action='store_true', help='serve the versions `build` made, instead of a branch')
    p.set_defaults(fn=cmd_preview)
    args = parser.parse_args()
    args.fn(args)


if __name__ == '__main__':
    main()
