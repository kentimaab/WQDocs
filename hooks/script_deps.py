"""
Pre-build preprocessor for Zensical.

Reads docs/mod/reference/script_deps.yml and auto-generates a standardised
???+ info "Requirements" admonition on every .md file that has a `scripts:`
frontmatter key. Also injects the deps JSON into the ScriptHierarchy widget.

Run before `zensical build`, then restore source files afterwards:

    python hooks/script_deps.py docs
    zensical build --clean
    git checkout docs/

Usage:
    python hooks/script_deps.py [docs_dir]   (default: "docs")
"""

import json
import os
import re
import sys

import yaml

_SCRIPT_HIERARCHY_REL = os.path.join("mod", "reference", "Script_Widget.html")
_WIDGET_PLACEHOLDER = "{} /* __SCRIPT_DEPS__ */"

_DEPS: dict = {}
_LAYER_MEMO: dict = {}


def _load_deps(docs_dir: str) -> None:
    global _DEPS, _LAYER_MEMO
    deps_file = os.path.join(docs_dir, "mod", "reference", "script_deps.yml")
    with open(deps_file, encoding="utf-8") as fh:
        _DEPS = yaml.safe_load(fh) or {}
    _LAYER_MEMO = {}


def _get_layer(s: str) -> int:
    if s in _LAYER_MEMO:
        return _LAYER_MEMO[s]
    parents = _DEPS.get(s) or []
    if not parents:
        _LAYER_MEMO[s] = 0
        return 0
    _LAYER_MEMO[s] = 1 + max(_get_layer(d) for d in parents)
    return _LAYER_MEMO[s]


def _all_deps(entry_scripts: list) -> set:
    visited: set = set()

    def walk(s: str) -> None:
        if s in visited:
            return
        visited.add(s)
        for d in (_DEPS.get(s) or []):
            walk(d)

    for s in entry_scripts:
        walk(s)
    return visited


def _sort_scripts(all_scripts: set, entry_scripts: list) -> list:
    entry_set = set(entry_scripts)
    entries = [s for s in entry_scripts if s in all_scripts]
    non_entries = sorted(
        [s for s in all_scripts if s not in entry_set],
        key=lambda s: (-_get_layer(s), s),
    )
    return entries + non_entries


def _parse_frontmatter(text: str):
    """Return (meta_dict, body_text). meta_dict is {} if no frontmatter."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm_text = text[3:end].strip()
    body = text[end + 4:].lstrip("\n")
    try:
        meta = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError:
        meta = {}
    return meta, body


def _build_admonition(meta: dict) -> str:
    scripts = meta.get("scripts") or []
    all_scripts = _all_deps(scripts)
    sorted_scripts = _sort_scripts(all_scripts, scripts)

    title = (
        meta.get("title", "")
        .split(" — ")[0]
        .split(" - ")[0]
        .strip()
        or "this module"
    )

    lines = ['???+ info "Requirements"']
    lines.append(f"    The following scripts are required to use {title} and all")
    lines.append(f"    related functionality covered in the {title} guides:")
    lines.append("    ")
    for s in sorted_scripts:
        lines.append(f"    * `{s}`")

    obj_libs = meta.get("object_libraries")
    if obj_libs:
        lines.append("    ")
        lines.append("    And the following Object Libraries:")
        lines.append("    ")
        for lib in obj_libs:
            lines.append(f"    * `{lib}`")

    return "\n".join(lines)


def _replace_or_inject(markdown: str, new_admonition: str) -> str:
    lines = markdown.split("\n")
    admonition_re = re.compile(r"^(\?\?\?\+|\!\!\!)")

    start = None
    for i, line in enumerate(lines):
        if admonition_re.match(line):
            start = i
            break

    if start is not None:
        last_content = start
        i = start + 1
        while i < len(lines):
            if lines[i].startswith("    ") or lines[i].startswith("\t"):
                last_content = i
                i += 1
            elif lines[i] == "":
                i += 1
            else:
                break
        end = last_content + 1
        while end < len(lines) and lines[end] == "":
            end += 1
        effective_start = start
        if start > 0 and lines[start - 1] == "":
            effective_start = start - 1
        lines = lines[:effective_start] + lines[end:]

    h1_idx = None
    for i, line in enumerate(lines):
        if line.startswith("# "):
            h1_idx = i
            break

    if h1_idx is None:
        return "\n".join(lines)

    new_lines = (
        lines[: h1_idx + 1]
        + new_admonition.split("\n")
        + [""]
        + lines[h1_idx + 1 :]
    )
    return "\n".join(new_lines)


def _process_file(path: str) -> bool:
    """Process a single .md file. Returns True if the file was modified."""
    with open(path, encoding="utf-8-sig") as fh:
        original = fh.read()

    meta, body = _parse_frontmatter(original)

    # Inject deps JSON into ScriptHierarchy widget
    rel = os.path.relpath(path).replace("\\", "/")
    if rel.endswith(_SCRIPT_HIERARCHY_REL.replace("\\", "/")):
        deps_json = json.dumps(_DEPS, separators=(",", ":"))
        new_body = body.replace(_WIDGET_PLACEHOLDER, deps_json)
        if new_body != body:
            # Reconstruct with frontmatter
            fm_block = original[: len(original) - len(body)]
            new_text = fm_block + new_body
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(new_text)
            return True
        return False

    if not meta.get("scripts"):
        return False

    admonition = _build_admonition(meta)
    new_body = _replace_or_inject(body, admonition)

    if new_body == body:
        return False

    fm_block = original[: len(original) - len(body)]
    new_text = fm_block + new_body
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(new_text)
    return True


def main(docs_dir: str = "docs") -> None:
    _load_deps(docs_dir)
    modified = 0
    for root, _, files in os.walk(docs_dir):
        for fname in files:
            if fname.endswith(".md") or fname.endswith(".html"):
                if _process_file(os.path.join(root, fname)):
                    modified += 1
    print(f"script_deps: processed {modified} file(s) in '{docs_dir}'")


if __name__ == "__main__":
    docs_arg = sys.argv[1] if len(sys.argv) > 1 else "docs"
    main(docs_arg)
