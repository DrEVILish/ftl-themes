#!/usr/bin/env python3
"""Regression cases for theme-family inheritance edge conditions."""
import tempfile
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import theme_inheritance


def test_missing_parent_fails_with_slug():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "themes" / "child").mkdir(parents=True)
        (root / "themes" / "child" / "theme.css").write_text("/*\n * Extends: absent\n */")
        old_root = theme_inheritance.ROOT
        theme_inheritance.ROOT = root
        try:
            try:
                theme_inheritance.chain("child")
            except ValueError as error:
                assert "missing theme source: absent" in str(error)
            else:
                raise AssertionError("missing parent was accepted")
        finally:
            theme_inheritance.ROOT = old_root


def test_cycle_fails_instead_of_looping():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        themes = root / "themes"
        themes.mkdir()
        (themes / "a").mkdir()
        (themes / "b").mkdir()
        (themes / "a" / "theme.css").write_text("/*\n * Extends: b\n */")
        (themes / "b" / "theme.css").write_text("/*\n * Extends: a\n */")
        old_root = theme_inheritance.ROOT
        theme_inheritance.ROOT = root
        try:
            try:
                theme_inheritance.chain("a")
            except ValueError as error:
                assert "theme inheritance cycle" in str(error)
                assert "a -> b -> a" in str(error)
            else:
                raise AssertionError("inheritance cycle was accepted")
        finally:
            theme_inheritance.ROOT = old_root


def test_inheritance_rewrites_only_base_selectors_inside_groups():
    css = '''
      html[data-theme="parent"], html[data-theme="parent"][data-variant="dark"] { --x: 1; }
      @media (min-width: 1px) {
        html[data-theme="parent"] .button { color: red; }
        html[data-theme="parent"][data-accent="blue"] .button { color: blue; }
      }
    '''
    out = theme_inheritance.base_rules(css)
    assert 'html[data-theme="parent"] { --x: 1;' in out
    assert 'html[data-theme="parent"][data-variant="dark"]' not in out
    assert '@media (min-width: 1px)' in out
    assert 'html[data-theme="parent"] .button' in out
    assert 'data-accent="blue"' not in out


if __name__ == "__main__":
    tests = [(name, fn) for name, fn in sorted(globals().items()) if name.startswith("test_")]
    for name, fn in tests:
        fn()
        print(f"PASS  {name}")
    print(f"{len(tests)} inheritance edge test(s), 0 failed")
