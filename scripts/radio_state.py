#!/usr/bin/env python3
"""CSS-only selection for v5 (CONTRACT.md "CSS-only selection").

Reads a bundle on stdin and writes it out with every `.is-active` and
`[aria-selected="true"]` in a selector also matching an item whose own
radio/checkbox child is checked. That lets markup like

    <label class="list-item"><input type="radio" name="view" checked> …</label>

select items with no JS, and every theme's existing active styling applies
to it unchanged. The extra match sits in :where(), so no selector's
specificity changes. Occurrences already inside a :has(…) are left alone
(:has can't nest). Comments are copied untouched.
"""
import re
import sys

# A table row is selected by the checkbox in its first cell (selection column).
CHECKED = (':where(:has(> input:is([type="radio"], [type="checkbox"]):checked,'
           ' > td:first-child input[type="checkbox"]:checked))')
TOKENS = re.compile(r'\.is-active(?![\w-])|\[aria-selected="true"\]')


def rewrite(css):
    out, i, n = [], 0, len(css)
    has_depth = []  # paren depths at which a :has( opened
    depth = 0
    while i < n:
        if css.startswith("/*", i):
            j = css.find("*/", i + 2)
            j = n if j < 0 else j + 2
            out.append(css[i:j]); i = j; continue
        if css[i] in "\"'":  # strings (content: "…", urls) pass through
            q = css[i]; j = i + 1
            while j < n and css[j] != q:
                j += 2 if css[j] == "\\" else 1
            out.append(css[i:j + 1]); i = j + 1; continue
        if css.startswith(":has(", i):
            depth += 1; has_depth.append(depth); out.append(":has("); i += 5; continue
        if css[i] == "(":
            depth += 1
        elif css[i] == ")":
            if has_depth and has_depth[-1] == depth:
                has_depth.pop()
            depth -= 1
        m = TOKENS.match(css, i)
        if m and not has_depth:
            out.append(f":is({m.group(0)}, {CHECKED})"); i = m.end(); continue
        out.append(css[i]); i += 1
    return "".join(out)


if __name__ == "__main__":
    if sys.argv[1:] == ["--test"]:
        assert rewrite(".tab.is-active { x }") == f'.tab:is(.is-active, {CHECKED}) {{ x }}'
        assert rewrite(".a:has(.is-active) {}") == ".a:has(.is-active) {}"
        assert rewrite('/* .is-active */ .b[aria-selected="true"]{}').startswith("/* .is-active */ .b:is([aria-selected")
        assert rewrite('.c { content: ".is-active"; }') == '.c { content: ".is-active"; }'
        assert rewrite(".is-active-x {}") == ".is-active-x {}"
        print("ok"); sys.exit()
    sys.stdout.write(rewrite(sys.stdin.read()))
