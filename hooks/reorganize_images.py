"""
Image reorganization script.

Phase 1: Move images scattered outside <docs_dir>/Images/ into <docs_dir>/Images/<subfolder>/
Phase 2: Update all broken references in md files caused by the moves
Phase 3: Update remaining /Images/ references to <web_prefix>Images/

Skips <docs_dir>/assets/ entirely (theme/branding files).

Usage:
    # English docs (dry run)
    python hooks/reorganize_images.py

    # English docs (apply)
    python hooks/reorganize_images.py --execute

    # Swedish docs (dry run)
    python hooks/reorganize_images.py --docs-dir docs-sv --web-prefix /docs/sv/

    # Swedish docs (apply)
    python hooks/reorganize_images.py --docs-dir docs-sv --web-prefix /docs/sv/ --execute
"""

import os
import re
import shutil
import sys
from urllib.parse import unquote

# ---------------------------------------------------------------------------
# Parse arguments
# ---------------------------------------------------------------------------

args = sys.argv[1:]
DRY_RUN = "--execute" not in args

DOCS_DIR = "docs"
WEB_PREFIX = "/docs/"

if "--docs-dir" in args:
    idx = args.index("--docs-dir")
    DOCS_DIR = args[idx + 1]

if "--web-prefix" in args:
    idx = args.index("--web-prefix")
    WEB_PREFIX = args[idx + 1]
    if not WEB_PREFIX.endswith("/"):
        WEB_PREFIX += "/"

IMAGES_ROOT = os.path.join(DOCS_DIR, "Images")
ASSETS_DIR = os.path.normpath(os.path.join(DOCS_DIR, "assets"))
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp"}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def is_image(name):
    return os.path.splitext(name)[1].lower() in IMAGE_EXTS


def target_subfolder(src):
    """
    Determine the subfolder under <docs>/Images/ for a stray image.
    If the image lives in a folder called 'Images' or 'pics', use the
    grandparent folder name instead.
    """
    parent = os.path.basename(os.path.dirname(src))
    grandparent = os.path.basename(os.path.dirname(os.path.dirname(src)))
    if parent.lower() in ("images", "pics"):
        return grandparent
    return parent


def collect_stray_images():
    images_abs = os.path.normpath(os.path.abspath(IMAGES_ROOT))
    assets_abs = os.path.normpath(os.path.abspath(ASSETS_DIR))
    stray = []
    for root, _, files in os.walk(DOCS_DIR):
        abs_root = os.path.normpath(os.path.abspath(root))
        if abs_root.startswith(images_abs):
            continue
        if abs_root.startswith(assets_abs):
            continue
        for f in files:
            if is_image(f):
                stray.append(os.path.normpath(os.path.join(root, f)))
    return stray


def build_move_plan(stray):
    """Returns {norm_src: norm_dst}."""
    plan = {}
    dst_used = {}

    for src in stray:
        sub = target_subfolder(src)
        fname = os.path.basename(src)
        dst = os.path.normpath(os.path.join(IMAGES_ROOT, sub, fname))

        if dst in dst_used and dst_used[dst] != src:
            base, ext = os.path.splitext(fname)
            dst = os.path.normpath(os.path.join(IMAGES_ROOT, sub, f"{base}_{sub}{ext}"))

        dst_used[dst] = src
        plan[src] = dst

    return plan


def all_md_files():
    mds = []
    for root, _, files in os.walk(DOCS_DIR):
        for f in files:
            if f.endswith(".md"):
                mds.append(os.path.normpath(os.path.join(root, f)))
    return mds


def resolve_ref(ref, md_path):
    """Resolve an image reference to a normalised path relative to cwd."""
    decoded = unquote(ref)
    if decoded.startswith("/"):
        return os.path.normpath(os.path.join(DOCS_DIR, decoded.lstrip("/")))
    return os.path.normpath(os.path.join(os.path.dirname(md_path), decoded))


def to_web_path(abs_img):
    """docs-sv/Images/foo/bar.png + web_prefix /docs/sv/ → /docs/sv/Images/foo/bar.png"""
    rel = os.path.relpath(abs_img, DOCS_DIR).replace("\\", "/")
    return WEB_PREFIX + rel


# ---------------------------------------------------------------------------
# Phase 2 — update references to moved images
# ---------------------------------------------------------------------------

def update_moved_refs(md_path, plan, dry):
    with open(md_path, encoding="utf-8-sig") as fh:
        original = fh.read()

    replacements = []

    for m in re.finditer(r'(!\[[^\]]*\]\()([^)\s"\'#][^)"\'#]*)([^)]*\))', original):
        ref = m.group(2).strip()
        resolved = resolve_ref(ref, md_path)

        if resolved in plan:
            new_ref = to_web_path(plan[resolved])
            new_full = m.group(1) + new_ref + m.group(3)
            replacements.append((m.start(), m.end(), m.group(0), new_full))

    if not replacements:
        return 0

    result = original
    for start, end, old, new in reversed(replacements):
        result = result[:start] + new + result[end:]

    rel = os.path.relpath(md_path)
    print(f"  {rel}  ({len(replacements)} ref(s))")
    for _, _, old, new in replacements:
        print(f"    - {old}")
        print(f"    + {new}")

    if not dry:
        with open(md_path, "w", encoding="utf-8") as fh:
            fh.write(result)

    return len(replacements)


# ---------------------------------------------------------------------------
# Phase 3 — patch remaining /Images/ → <web_prefix>Images/
# ---------------------------------------------------------------------------

def patch_slash_images(md_path, dry):
    with open(md_path, encoding="utf-8-sig") as fh:
        original = fh.read()

    # Replace /Images/ that isn't already prefixed correctly
    escaped_prefix = re.escape(WEB_PREFIX)
    pattern = r'(?<!' + re.escape(WEB_PREFIX.rstrip('/')) + r')/Images/'
    new = re.sub(pattern, WEB_PREFIX + 'Images/', original)

    if new == original:
        return 0

    count = len(re.findall(pattern, original))
    rel = os.path.relpath(md_path)
    print(f"  {rel}  ({count} path(s))")

    if not dry:
        with open(md_path, "w", encoding="utf-8") as fh:
            fh.write(new)

    return count


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    mode = "DRY RUN" if DRY_RUN else "EXECUTE"
    print(f"=== Image Reorganisation — {mode} ===")
    print(f"    docs_dir   : {DOCS_DIR}")
    print(f"    web_prefix : {WEB_PREFIX}\n")

    # ---- Phase 1 ----
    stray = collect_stray_images()
    plan = build_move_plan(stray)

    print(f"Phase 1 — {len(plan)} image(s) to move:")
    for src, dst in sorted(plan.items()):
        print(f"  {src}")
        print(f"    → {dst}")

    if not DRY_RUN:
        for src, dst in plan.items():
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.move(src, dst)
        for src in plan:
            parent = os.path.dirname(src)
            while os.path.normpath(parent) != os.path.normpath(DOCS_DIR):
                try:
                    if not os.listdir(parent):
                        os.rmdir(parent)
                        parent = os.path.dirname(parent)
                    else:
                        break
                except OSError:
                    break
        print(f"  Moved {len(plan)} file(s).")

    print()

    # ---- Phase 2 ----
    md_files = all_md_files()
    print(f"Phase 2 — updating references in {len(md_files)} md files:")
    total_refs = sum(update_moved_refs(md, plan, DRY_RUN) for md in md_files)
    print(f"  Total: {total_refs} reference(s) updated\n")

    # ---- Phase 3 ----
    print(f"Phase 3 — patching /Images/ → {WEB_PREFIX}Images/:")
    total_patch = sum(patch_slash_images(md, DRY_RUN) for md in md_files)
    print(f"  Total: {total_patch} path(s) patched\n")

    if DRY_RUN:
        print("=== Dry run complete. Run with --execute to apply changes. ===")
    else:
        print("=== Done. Run the image check script to verify. ===")


if __name__ == "__main__":
    main()
