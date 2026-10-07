#!/usr/bin/env python3
"""html[data-motion="always"] for unattended screens (docs/components/signage.md).

Reads a bundle on stdin and writes it out with every
`@media (prefers-reduced-motion: no-preference) { … }` block followed by a
copy that applies whatever the device reports, its selectors scoped to
`:root[data-motion="always"]` (any other condition in the query, such as a
width, is kept). Every `@media (prefers-reduced-motion: reduce) { … }` block
is scoped to `:root:not([data-motion="always"])`, so its "motion off" rules
stand down. Sources keep one motion block per component; nothing else
changes. @keyframes are copied untouched.
"""
import re
import sys

NO_PREF = re.compile(r"\(\s*prefers-reduced-motion\s*:\s*no-preference\s*\)")
REDUCE = re.compile(r"\(\s*prefers-reduced-motion\s*:\s*reduce\s*\)")
ROOTISH = re.compile(r"^(:root|html)(?![\w-])")


def skip(css, i, n):
    """Index after the comment or string starting at i, else None."""
    if css.startswith("/*", i):
        j = css.find("*/", i + 2)
        return n if j < 0 else j + 2
    if css[i] in "\"'":
        q, j = css[i], i + 1
        while j < n and css[j] != q:
            j += 2 if css[j] == "\\" else 1
        return j + 1
    return None


def match(css, i):
    """Index of the } closing the { at i."""
    n, depth = len(css), 0
    while i < n:
        j = skip(css, i, n)
        if j is not None:
            i = j
            continue
        if css[i] == "{":
            depth += 1
        elif css[i] == "}":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    raise ValueError("unbalanced braces")


def split_selectors(sel):
    out, depth, start = [], 0, 0
    for k, ch in enumerate(sel):
        if ch in "([":
            depth += 1
        elif ch in ")]":
            depth -= 1
        elif ch == "," and depth == 0:
            out.append(sel[start:k])
            start = k + 1
    out.append(sel[start:])
    return out


def scope(sel, attr):
    s = sel.strip()
    m = ROOTISH.match(s)
    if m:
        return m.group(1) + attr + s[m.end():]
    if s.startswith("::"):
        return ":root" + attr + s
    return ":root" + attr + " " + s


def walk(css, attr):
    """Scope every style rule's selectors in css (a block's contents)."""
    out, i, n = [], 0, len(css)
    while i < n:
        j = skip(css, i, n)
        if j is not None:
            out.append(css[i:j]); i = j; continue
        if css[i].isspace() or css[i] == ";":
            out.append(css[i]); i += 1; continue
        # A statement: prelude up to { or ;
        k = i
        while k < n and css[k] not in "{;":
            s2 = skip(css, k, n)
            k = s2 if s2 is not None else k + 1
        if k >= n or css[k] == ";":
            out.append(css[i:k + 1]); i = k + 1; continue
        end = match(css, k)
        prelude, body = css[i:k], css[k + 1:end]
        if prelude.lstrip().startswith("@"):
            if re.match(r"\s*@(-\w+-)?keyframes", prelude):
                out.append(css[i:end + 1])
            else:
                out.append(prelude + "{" + walk(body, attr) + "}")
        else:
            sels = ",".join(scope(x, attr) for x in split_selectors(prelude))
            out.append(sels + " {" + body + "}")
        i = end + 1
    return "".join(out)


def rewrite(css):
    out, i, n = [], 0, len(css)
    while i < n:
        j = skip(css, i, n)
        if j is not None:
            out.append(css[i:j]); i = j; continue
        if css.startswith("@media", i):
            k = css.find("{", i)
            prelude = css[i + 6:k]
            if NO_PREF.search(prelude) or REDUCE.search(prelude):
                end = match(css, k)
                body = css[k + 1:end]
                if REDUCE.search(prelude):
                    out.append(css[i:k + 1] + walk(body, ':not([data-motion="always"])') + "}")
                else:
                    out.append(css[i:end + 1])
                    rest = re.sub(r"\s*\band\b\s*$", "", re.sub(r"^\s*and\b", "", NO_PREF.sub("", prelude).strip()).strip()).strip()
                    copy = walk(body, '[data-motion="always"]')
                    out.append("\n" + (f"@media {rest} {{{copy}}}" if rest else copy))
                i = end + 1
                continue
        out.append(css[i]); i += 1
    return "".join(out)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        src = ('@media (prefers-reduced-motion: no-preference) { :root:not([data-motion="reduced"]) .a, .b::after { animation: x 1s; }'
               ' @starting-style { .c { opacity: 0; } } @keyframes k { to { opacity: 1; } } }\n'
               '@media (min-width: 1801px) and (prefers-reduced-motion:no-preference) { html[data-theme="t"] .d { transition: none; } }\n'
               '@media (prefers-reduced-motion: reduce) { .e { transition: none; } }\n/* @media (prefers-reduced-motion: reduce) { .f {} } */')
        got = rewrite(src)
        assert ':root[data-motion="always"]:not([data-motion="reduced"]) .a' in got
        assert ':root[data-motion="always"] .b::after' in got
        assert ':root[data-motion="always"] .c' in got and "@keyframes k { to { opacity: 1; } }" in got
        assert '@media (min-width: 1801px) { html[data-motion="always"][data-theme="t"] .d' in got
        assert ':root:not([data-motion="always"]) .e' in got
        assert "/* @media (prefers-reduced-motion: reduce) { .f {} } */" in got
        assert got.count('[data-motion="always"]') == 5, got
        print("motion_always self-test passed")
    else:
        sys.stdout.write(rewrite(sys.stdin.read()))
