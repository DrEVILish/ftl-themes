#!/usr/bin/env python3
"""Resolve the small, build-time theme inheritance chain."""
import re
import sys
from pathlib import Path

import cssparse

ROOT = Path(__file__).resolve().parent.parent
HEADER = re.compile(r"(?m)^\s*\*\s*Extends:\s*([a-z0-9-]+)\s*$")
# `* Inherit: none` beside Extends keeps the family link (themes.json `family`
# and `extends`) but copies none of the parent's rules, for a child that sets
# every token and draws all of its own chrome. Otherwise the parent's
# component rules sit under the child's, scoped to it, and leak through.
INHERIT = re.compile(r"(?m)^\s*\*\s*Inherit:\s*([a-z-]+)\s*$")
INHERIT_MODES = ("all", "none")


def chain(slug):
    result, seen = [], set()
    while slug:
        if slug in seen:
            raise ValueError("theme inheritance cycle: " + " -> ".join([name for name, _ in result] + [slug]))
        seen.add(slug)
        path = ROOT / "themes" / slug / "theme.css"
        if not path.is_file():
            raise ValueError(f"missing theme source: {slug}")
        source = path.read_text()
        result.append((slug, source))
        match = HEADER.search(source)
        slug = match.group(1) if match else ""
    return list(reversed(result))


def base_rules(css):
    """Retain base rules while leaving parent-specific user choices to child themes."""
    out = []
    for prelude, body in cssparse.statements(cssparse.strip_comments(css)):
        if body is None:
            out.append(prelude)
        else:
            body = "\n".join(line.rstrip() for line in body.splitlines())
            if prelude.startswith("@"):
                if prelude.lower().startswith(cssparse.GROUPING):
                    inner = base_rules(body)
                    if inner:
                        out.append(f"{prelude} {{\n{inner}\n}}")
                else:
                    out.append(f"{prelude} {{{body}}}")
            else:
                selectors = [s for s in cssparse.split_top(prelude)
                             if not re.search(r"\[data-(?:variant|accent|tint)(?:[=~|^$*\s\]])", s)]
                if selectors:
                    out.append(f"{', '.join(selectors)} {{{body}}}")
    return "\n".join(out)


def inherit_mode(source):
    match = INHERIT.search(source)
    mode = match.group(1) if match else "all"
    if mode not in INHERIT_MODES:
        raise ValueError(f"unknown Inherit mode: {mode} (expected {' or '.join(INHERIT_MODES)})")
    return mode


def rules(slug):
    out = []
    links = chain(slug)
    # A theme that says `Inherit: none` cuts off everything above it.
    start = max((i for i, (_, source) in enumerate(links) if inherit_mode(source) == "none"), default=0)
    for ancestor, source in links[start:]:
        folder = ROOT / "themes" / ancestor
        chrome = folder / "chrome.css"
        if chrome.exists():
            source += "\n" + chrome.read_text()
        if ancestor != slug:
            source = base_rules(source)
            source = re.sub(r'html\[data-theme=(["\'])%s\1\]' % re.escape(ancestor),
                            lambda _: f'html[data-theme="{slug}"]', source)
        out.append(f"/* theme source: {ancestor} */\n{source}")
    return "\n".join(out)


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1 and sys.argv[1] == "--check":
            for path in sorted((ROOT / "themes").glob("*/theme.css")):
                chain(path.parent.name)
                inherit_mode(path.read_text())
            print("theme inheritance: valid")
        else:
            print(rules(sys.argv[1]))
    except (IndexError, ValueError) as exc:
        print(f"theme inheritance: {exc}", file=sys.stderr)
        raise SystemExit(1)
