#!/usr/bin/env python3
"""Resolve the small, build-time theme inheritance chain."""
import re
import sys
from pathlib import Path

import cssparse

ROOT = Path(__file__).resolve().parent.parent
HEADER = re.compile(r"(?m)^\s*\*\s*Extends:\s*([a-z0-9-]+)\s*$")


def chain(slug):
    result, seen = [], set()
    while slug:
        if slug in seen:
            raise ValueError("theme inheritance cycle: " + " -> ".join(result + [slug]))
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


def rules(slug):
    out = []
    for ancestor, source in chain(slug):
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
            print("theme inheritance: valid")
        else:
            print(rules(sys.argv[1]))
    except (IndexError, ValueError) as exc:
        print(f"theme inheritance: {exc}", file=sys.stderr)
        raise SystemExit(1)
