"""
Image reference checker.

Scans all markdown files in a docs directory and verifies that every
image reference resolves to a file that actually exists on disk.
Exits with code 1 if any broken references are found.

On Linux the filesystem is case-sensitive, so a wrong-case filename
that exists on Windows will be caught here before the build.

Run this script prior to upload. It validates that the image links are correct for site launch. It also resolves broken links. 
The script also allows for custom paths, meaning a test launch is able to be validated with the custom deployment path. 

Note. This script dosent cover all types of error! Test launch is recomended to validate paths! When testing, apply this script to ftp-test-build.yml 
This updates all images link with the relative path to the test launch site. If all images resolves correctly and is visible on test site. All image links work and ready for offical launch (remove from ftp-test-build)

Usage:
    # English docs  (web prefix defaults to /docs/)
    python hooks/check_images.py

    # Swedish docs
    python hooks/check_images.py --docs-dir docs-sv --web-prefix /docs/sv/

    # Custom deployment path, e.g. test environment at /docs/test/
    python hooks/check_images.py --web-prefix /docs/test/
    python hooks/check_images.py --docs-dir docs-sv --web-prefix /docs/test/sv/
"""

import os
import re
import sys
from urllib.parse import unquote

# ---------------------------------------------------------------------------
# Args
# ---------------------------------------------------------------------------

_args = sys.argv[1:]

DOCS_DIR = "docs"
WEB_PREFIX = "/docs/"

if "--docs-dir" in _args:
    DOCS_DIR = _args[_args.index("--docs-dir") + 1]

if "--web-prefix" in _args:
    WEB_PREFIX = _args[_args.index("--web-prefix") + 1]
    if not WEB_PREFIX.endswith("/"):
        WEB_PREFIX += "/"

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp"}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def is_image_ref(ref):
    path = ref.split("?")[0].split("#")[0]
    return os.path.splitext(path)[1].lower() in IMAGE_EXTS


def resolve(ref, md_path):
    """
    Returns the expected filesystem path for an image reference,
    or None if the reference is external / out of scope.
    """
    decoded = unquote(ref)

    if decoded.startswith(("http://", "https://", "data:", "//")):
        return None

    if decoded.startswith("/"):
        if decoded.startswith(WEB_PREFIX):
            rel = decoded[len(WEB_PREFIX):]
            return os.path.normpath(os.path.join(DOCS_DIR, rel))
        # Absolute path that doesn't match our prefix — out of scope
        return None

    # Relative path — resolve from the md file's directory
    return os.path.normpath(os.path.join(os.path.dirname(md_path), decoded))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    errors = []
    checked = 0

    for root, _, files in os.walk(DOCS_DIR):
        for fname in sorted(files):
            if not fname.endswith(".md"):
                continue
            md_path = os.path.join(root, fname)
            with open(md_path, encoding="utf-8-sig") as fh:
                content = fh.read()

            for m in re.finditer(r'!\[[^\]]*\]\(([^)\s"\'#][^)"\'#]*)', content):
                ref = m.group(1).strip()
                if not is_image_ref(ref):
                    continue

                checked += 1
                target = resolve(ref, md_path)

                if target is None:
                    continue

                if not os.path.isfile(target):
                    rel_md = os.path.relpath(md_path).replace("\\", "/")
                    errors.append((rel_md, ref, target))

    label = f"docs_dir={DOCS_DIR}  web_prefix={WEB_PREFIX}"
    print(f"Image check — {label}")
    print(f"Checked {checked} reference(s) across {DOCS_DIR}/\n")

    if errors:
        print(f"FAILED — {len(errors)} broken reference(s):\n")
        for md, ref, path in errors:
            print(f"  {md}")
            print(f"    ref  : {ref}")
            print(f"    path : {path}")
            print()
        sys.exit(1)

    print("All image references OK.")


if __name__ == "__main__":
    main()
