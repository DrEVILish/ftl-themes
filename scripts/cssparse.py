"""Minimal CSS reader shared by the build and the lint.

Both used to scan CSS with regexes, which got two things wrong: a selector
list was split on every comma, including the ones inside :is(a, b) or
:not(a, b), and a rule nested in @media/@supports was indistinguishable
from an unconditional one — so a root block inside a media query stood in
for the theme's default tokens. This reader is string-, paren- and
bracket-aware and records the at-rule context of every style rule.

Deliberately small (no dependency, since CI and submodule consumers run
the build with a bare python3): it understands exactly what theme sources
use — comments, strings, style rules, grouping at-rules, and opaque
at-rules like @font-face/@keyframes. It does not do CSS nesting.
"""
from collections import namedtuple

# At-rules whose body holds ordinary style rules.
GROUPING = ("@media", "@supports", "@layer", "@container", "@scope")
# Of those, the ones that make their rules apply only sometimes.
CONDITIONAL = ("@media", "@supports", "@container", "@scope")

Rule = namedtuple("Rule", "selector body context")
Rule.__doc__ = """One (selector, declarations) pair. A comma-separated
selector list yields one Rule per selector. context is the tuple of
enclosing at-rule preludes, outermost first; () at top level."""


def strip_comments(css):
    """Remove /* … */ comments, leaving comment-like text in strings alone."""
    out, i, n, quote = [], 0, len(css), None
    while i < n:
        ch = css[i]
        if quote:
            out.append(ch)
            if ch == "\\" and i + 1 < n:
                out.append(css[i + 1])
                i += 1
            elif ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
            out.append(ch)
        elif css.startswith("/*", i):
            end = css.find("*/", i + 2)
            i = n if end == -1 else end + 2
            continue
        else:
            out.append(ch)
        i += 1
    return "".join(out)


def split_top(text, sep=","):
    """Split on sep where it is not inside quotes, (), [] or {}."""
    parts, depth, quote, start, i = [], 0, None, 0, 0
    while i < len(text):
        ch = text[i]
        if quote:
            if ch == "\\":
                i += 1
            elif ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
        elif ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth -= 1
        elif ch == sep and depth == 0:
            parts.append(text[start:i])
            start = i + 1
        i += 1
    parts.append(text[start:])
    return [p.strip() for p in parts if p.strip()]


def statements(css):
    """Top-level statements of comment-free CSS: (prelude, body) for a
    block, (text, None) for a ;-terminated statement like `@layer a, b;`."""
    out, i, n = [], 0, len(css)
    while i < n:
        depth, quote, j = 0, None, i
        while j < n:
            ch = css[j]
            if quote:
                if ch == "\\":
                    j += 1
                elif ch == quote:
                    quote = None
            elif ch in "\"'":
                quote = ch
            elif ch in "([":
                depth += 1
            elif ch in ")]":
                depth -= 1
            elif depth == 0 and ch in "{;":
                break
            j += 1
        if j >= n:
            break  # trailing whitespace or an unterminated statement
        if css[j] == ";":
            out.append((css[i:j + 1].strip(), None))
            i = j + 1
            continue
        start, depth, quote, k = j + 1, 1, None, j + 1
        while k < n and depth:
            ch = css[k]
            if quote:
                if ch == "\\":
                    k += 1
                elif ch == quote:
                    quote = None
            elif ch in "\"'":
                quote = ch
            elif ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
            k += 1
        out.append((css[i:j].strip(), css[start:k - 1]))
        i = k
    return out


def rules(css, context=()):
    """Every style rule in css (comments are stripped here), in source order."""
    if not context:
        css = strip_comments(css)
    out = []
    for prelude, body in statements(css):
        if body is None or not prelude:
            continue
        if prelude.startswith("@"):
            if prelude.lower().startswith(GROUPING):
                out.extend(rules(body, context + (prelude,)))
            continue  # @font-face, @keyframes, @page, @property: not style rules
        for sel in split_top(prelude):
            out.append(Rule(sel, body, context))
    return out


def unconditional(context):
    """True if a rule in this context always applies (layers don't gate)."""
    return not any(p.lower().startswith(CONDITIONAL) for p in context)


def declarations(body):
    """[(property, value)] of a declaration block, in order. Property names
    are lowercased except custom properties, which are case-sensitive."""
    out = []
    for decl in split_top(body, ";"):
        name, colon, value = decl.partition(":")
        if not colon:
            continue
        name = name.strip()
        out.append((name if name.startswith("--") else name.lower(), value.strip()))
    return out
