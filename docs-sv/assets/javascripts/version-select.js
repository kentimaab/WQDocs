// Version menu for the product sections (MOD, BMS, WWT).
//
// Older versions of a product are archived with mike at /docs/<product>/<version>/ (and
// /docs/sv/<product>/<version>/), each product with its own versions.json beside them
// (hooks/versioning.py). /docs/current-versions.json says what each product's current
// version is: its live pages under a name ({"live": "MOD 2027.1.0"}), or one of its archives
// when the live pages aren't released yet ({"pinned": "2026.1.1"}; the deploy then sends the
// live pages there). On a product's pages this puts a version menu at the top of the left
// sidebar and keeps the reader on the same page when the chosen version has it. Products with
// neither a live name nor an archive get no menu.
//
// Archived pages load this script and its stylesheet from the live site, so a change here
// reaches every archive. Archived pages other than the current version get a banner pointing
// to it, and all archived pages get the "Home" item their breadcrumbs lack: in an archive the
// product's overview is the build's own home page.
(function () {
    var TEXT = {
        en: {
            label: 'Version',
            latest: 'Latest',
            home: 'Home',
            banner: 'You are viewing the documentation for {version}.',
            link: 'Go to {current}'
        },
        sv: {
            label: 'Version',
            latest: 'Senaste',
            home: 'Hem',
            banner: 'Du läser dokumentationen för {version}.',
            link: 'Gå till {current}'
        }
    };
    var lists = {};
    var currents = null;
    var renders = 0;

    // "/docs/sv/bms/2026.1.1/modules/x/" ->
    //   home "/docs/sv/", root "/docs/sv/bms/", product "bms", rest "2026.1.1/modules/x/"
    function locate() {
        var m = location.pathname.match(/^((\/docs\/(sv\/)?)(mod|bms|wwt)\/)(.*)$/);
        return m && { root: m[1], home: m[2], lang: m[3] ? 'sv' : 'en', product: m[4], rest: m[5] };
    }

    function getJson(url, fallback) {
        return fetch(url)
            .then(function (r) { return r.ok ? r.json() : fallback; })
            .catch(function () { return fallback; });
    }

    // The archived versions of one product, newest first
    function versions(root) {
        if (!lists[root]) {
            lists[root] = getJson(root + 'versions.json', []);
        }
        return lists[root];
    }

    // Each product's current version, the same in both languages
    function currentVersions() {
        if (!currents) {
            currents = getJson('/docs/current-versions.json', {});
        }
        return currents;
    }

    // An archive is a site of its own, so switching is a full page load rather than the theme's
    // instant navigation. Lands on the same page when the target version has it, else its start.
    function go(base, page) {
        fetch(base + page, { method: 'HEAD' })
            .then(function (r) { location.href = r.ok ? base + page : base; })
            .catch(function () { location.href = base; });
    }

    function menu(t, options, page) {
        var box = document.createElement('div');
        box.className = 'wq-version';
        var label = document.createElement('label');
        label.className = 'wq-version__label';
        label.htmlFor = 'wq-version-select';
        label.textContent = t.label;
        var select = document.createElement('select');
        select.id = 'wq-version-select';
        select.className = 'wq-version__select';
        options.forEach(function (o) {
            var option = document.createElement('option');
            option.value = o.base;
            option.textContent = o.title;
            option.selected = o.selected;
            select.appendChild(option);
        });
        select.addEventListener('change', function () {
            go(select.value, page);
        });
        box.appendChild(label);
        box.appendChild(select);
        return box;
    }

    function banner(t, version, current, page) {
        var box = document.createElement('div');
        box.className = 'admonition warning wq-version-banner';
        var p = document.createElement('p');
        p.textContent = t.banner.replace('{version}', version) + ' ';
        var a = document.createElement('a');
        a.href = current.base + page;
        a.textContent = t.link.replace('{current}', current.title);
        a.addEventListener('click', function (e) {
            e.preventDefault();
            go(current.base, page);
        });
        p.appendChild(a);
        box.appendChild(p);
        return box;
    }

    // Same markup as the theme's own breadcrumb items
    function homeCrumb(t, here) {
        var li = document.createElement('li');
        li.className = 'md-path__item wq-version-home';
        var a = document.createElement('a');
        a.className = 'md-path__link';
        a.href = here.home;
        var span = document.createElement('span');
        span.className = 'md-ellipsis';
        span.textContent = t.home;
        a.appendChild(span);
        li.appendChild(a);
        return li;
    }

    function render() {
        var mine = ++renders;
        var here = locate();
        if (!here) {
            return;
        }
        Promise.all([versions(here.root), currentVersions()]).then(function (results) {
            // A later page change has started its own render.
            if (mine !== renders) {
                return;
            }
            document.querySelectorAll('.wq-version, .wq-version-banner, .wq-version-home').forEach(function (el) {
                el.remove();
            });
            var list = results[0];
            var entry = results[1][here.product] || {};
            var t = TEXT[here.lang];
            var pinned = list.filter(function (v) { return v.version === entry.pinned; })[0];
            // Without a pinned archive the live pages are current, named or not
            var live = pinned ? null : (entry.live || (list.length ? t.latest : null));
            if (!live && !list.length) {
                return;
            }
            var first = here.rest.split('/')[0];
            var archived = list.filter(function (v) { return v.version === first; })[0];
            var page = archived ? here.rest.slice(first.length + 1) : here.rest;
            var current = pinned
                ? { title: pinned.title || pinned.version, base: here.root + pinned.version + '/' }
                : { title: live, base: here.root };

            var options = live ? [{ title: live, base: here.root, selected: !archived }] : [];
            list.forEach(function (v) {
                options.push({ title: v.title || v.version, base: here.root + v.version + '/', selected: v === archived });
            });
            var sidebar = document.querySelector('.md-sidebar--primary .md-sidebar__inner');
            if (sidebar) {
                sidebar.insertBefore(menu(t, options, page), sidebar.firstChild);
            }
            if (!archived) {
                return;
            }
            var content = document.querySelector('.md-content__inner');
            if (content && archived !== pinned) {
                content.insertBefore(banner(t, archived.title || archived.version, current, page), content.firstChild);
            }
            var crumbs = document.querySelector('.md-path__list');
            if (crumbs) {
                crumbs.insertBefore(homeCrumb(t, here), crumbs.firstChild);
            }
        });
    }

    document.addEventListener('DOMContentLoaded', render);
    if (typeof document$ !== 'undefined') {
        document$.subscribe(render);
    }
}());
