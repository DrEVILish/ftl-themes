#!/usr/bin/env python3
"""Tests for cssparse — the cases the old regex scanning got wrong.

Run: python3 scripts/test_cssparse.py (CI runs it before the lint).
"""
import sys

import build_bundles
import build_manifest
import cssparse


def test_selector_list_respects_parens():
    rules = cssparse.rules('html[data-theme="x"] :is(h1, h2), .a:not(.b, .c) { color: red; }')
    assert [r.selector for r in rules] == ['html[data-theme="x"] :is(h1, h2)', ".a:not(.b, .c)"]


def test_context_is_recorded():
    rules = cssparse.rules("@media (min-width: 1px) { @supports (x: y) { .a { b: c; } } } .d { e: f; }")
    assert rules[0].context == ("@media (min-width: 1px)", "@supports (x: y)")
    assert not cssparse.unconditional(rules[0].context)
    assert rules[1].context == () and cssparse.unconditional(rules[1].context)
    assert cssparse.unconditional(cssparse.rules("@layer t { .a { b: c; } }")[0].context)


def test_opaque_at_rules_are_not_style_rules():
    css = "@font-face { font-family: F; } @keyframes k { from { a: b; } to { a: c; } } .x { y: z; }"
    assert [r.selector for r in cssparse.rules(css)] == [".x"]


def test_strings_and_comments():
    css = '.a { content: "}{ /* not a comment */"; } /* .gone { x: y; } */ .b { c: d; }'
    rules = cssparse.rules(css)
    assert [r.selector for r in rules] == [".a", ".b"]
    assert cssparse.declarations(rules[0].body) == [("content", '"}{ /* not a comment */"')]


def test_declarations_keep_parenthesised_semicolons_and_custom_case():
    decls = cssparse.declarations("--ftl-Bg: url(a;b.png); COLOR: red; broken")
    assert decls == [("--ftl-Bg", "url(a;b.png)"), ("color", "red")]


def test_root_tokens_ignore_conditional_and_variant_blocks():
    src = '''
      html[data-theme="t"] { --ftl-surface: #102030; }
      @media (min-width: 1px) { html[data-theme="t"] { --ftl-surface: #ffffff; } }
      html[data-theme="t"][data-variant="v"] { --ftl-surface: #eeeeee; }
    '''
    assert build_manifest.root_tokens(src, "t") == {"--ftl-surface": "#102030"}
    assert build_manifest.scheme_of(src, "t")[0] == "dark"


def test_tokens_bundle_keeps_whole_selectors():
    out = build_bundles.tokens_only('html[data-theme="t"] :is(h1, h2), .ftl-x { a: b; }')
    assert out == 'html[data-theme="t"] :is(h1, h2) { a: b; }'


def test_parse_color_syntaxes():
    p = build_manifest.parse_color
    assert p("#fff") == (255, 255, 255, 1.0)
    assert p("#00000080")[3] == 128 / 255
    assert p("rgb(1 2 3 / 50%)") == (1.0, 2.0, 3.0, 0.5)
    assert p("rgba(1, 2, 3, 0.25)") == (1.0, 2.0, 3.0, 0.25)
    assert p("oklch(0.7 0.1 150)") is None


if __name__ == "__main__":
    tests = [(n, f) for n, f in sorted(globals().items()) if n.startswith("test_")]
    failed = 0
    for name, fn in tests:
        try:
            fn()
        except AssertionError as e:
            failed += 1
            print(f"FAIL  {name}: {e!r}")
    print(f"{len(tests)} cssparse test(s), {failed} failed")
    sys.exit(1 if failed else 0)
