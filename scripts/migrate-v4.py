#!/usr/bin/env python3
"""ftl-themes v3 -> v4 migration: drops the `ftl-` prefix everywhere.

v4 removes the prefix from CSS class names (`.ftl-btn` -> `.btn`), custom
properties (`--ftl-text` -> `--text`), keyframe names, element ids, and the
core file names (`ftl-core.css` -> `core.css`). There is NO compatibility
layer: run this over your own templates/CSS/JS when you upgrade.

    scripts/migrate-v4.py --dry-run  PATH...   show what would change
    scripts/migrate-v4.py            PATH...   rewrite files in place
    scripts/migrate-v4.py --check    PATH...   exit 1 if any legacy name remains
    scripts/migrate-v4.py --build-map PATH...  regenerate scripts/v4-rename-map.json
                                               from a v3 tree (maintainers only)

The rewrite is driven by an exact-name map (scripts/v4-rename-map.json), not
a blind regex, so an unrelated `ftl-` string in your own code is left alone
unless it is a name the v3 library actually shipped. Names are matched as
whole identifiers only (never inside a longer name), longest first.

Not rewritten (by design): the product/repo name `ftl-themes`, and this
map file itself. Review `git diff` afterwards -- in particular JS that builds
class names dynamically (`"ftl-" + kind`) cannot be found statically;
`--check` flags those too.
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MAP_PATH = os.path.join(HERE, "v4-rename-map.json")
SKIP_DIRS = {".git", "node_modules", "__pycache__", "visual-baseline", "visual-diffs"}
SKIP_FILES = {"v4-rename-map.json", "MIGRATING-v4.md", "CHANGELOG.md", "migrate-v4.py"}
# Names whose bare stripped form would be a generic keyframe/global that an
# app could plausibly already define.
OVERRIDES = {"ftl-spin": "spinner-rotate"}
PRODUCT = "ftl-themes"
IDENT = re.compile(r"(?<![A-Za-z0-9_])(--)?ftl-[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*")
BOUND_L = r"(?<![A-Za-z0-9_-])"
BOUND_R = r"(?![A-Za-z0-9_-])"
LEFTOVER = re.compile(r"(?<![A-Za-z0-9_])(?:--)?ftl-(?!themes)[A-Za-z0-9]|\bftl[A-Z][A-Za-z0-9]*|data-ftl|ftl_")


def iter_files(paths):
    for root in paths:
        if os.path.isfile(root):
            yield root
            continue
        for dirpath, dirs, files in os.walk(root):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for name in files:
                yield os.path.join(dirpath, name)


def read_text(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except (UnicodeDecodeError, OSError):
        return None


def new_name(old):
    if old in OVERRIDES:
        return OVERRIDES[old]
    return "--" + old[6:] if old.startswith("--ftl-") else old[4:]


def build_map(paths):
    found = set()
    for path in iter_files(paths):
        if os.path.basename(path) in SKIP_FILES:
            continue
        text = read_text(path)
        if text is None:
            continue
        for m in IDENT.finditer(text):
            name = m.group(0)
            if name.startswith(PRODUCT) or name == PRODUCT:
                continue
            found.add(name)
    mapping = {old: new_name(old) for old in sorted(found)}
    clashes = {}
    for old, new in mapping.items():
        clashes.setdefault(new, []).append(old)
    bad = {n: o for n, o in clashes.items() if len(o) > 1}
    if bad:
        sys.exit(f"rename map has colliding targets: {bad}")
    with open(MAP_PATH, "w", encoding="utf-8") as f:
        json.dump(mapping, f, indent=1, sort_keys=True)
        f.write("\n")
    print(f"wrote {len(mapping)} names to {MAP_PATH}")


def compile_rules():
    with open(MAP_PATH, encoding="utf-8") as f:
        mapping = json.load(f)
    keys = sorted(mapping, key=len, reverse=True)
    pattern = re.compile(BOUND_L + "(" + "|".join(re.escape(k) for k in keys) + ")" + BOUND_R)
    return mapping, pattern


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--build-map", action="store_true")
    args = ap.parse_args()

    if args.build_map:
        return build_map(args.paths)

    mapping, pattern = compile_rules()
    changed = leftovers = 0
    for path in iter_files(args.paths):
        if os.path.basename(path) in SKIP_FILES:
            continue
        text = read_text(path)
        if text is None:
            continue
        if args.check:
            for n, line in enumerate(text.split("\n"), 1):
                if LEFTOVER.search(line.replace(PRODUCT, "")):
                    leftovers += 1
                    print(f"{path}:{n}: legacy name: {line.strip()[:100]}")
            continue
        out, n = pattern.subn(lambda m: mapping[m.group(1)], text)
        if n:
            changed += 1
            print(f"{'would change' if args.dry_run else 'rewrote'} {path} ({n} names)")
            if not args.dry_run:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(out)
    if args.check:
        print(f"{leftovers} legacy name(s) remain")
        sys.exit(1 if leftovers else 0)
    print(f"{changed} file(s) {'would change' if args.dry_run else 'changed'}")


if __name__ == "__main__":
    main()
