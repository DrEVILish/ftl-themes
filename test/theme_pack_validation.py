#!/usr/bin/env python3
"""Exercise local pack validation through its CLI, including hostile CSS."""
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
TOKENS = '--bg:#111; --surface:#222; --surface-2:#333; --border:#555; --hairline:#444; --text:#fff; --muted:#ccc; --accent:#0af; --accent-2:#f0a; --danger:#f00; --success:#0f0; --warning:#ff0; --on-accent:#000; --on-danger:#000; --on-success:#000; --radius:4px; --font:sans-serif; --font-mono:monospace; --flare:#0af;'
BASE = 'html[data-theme="test"] {' + TOKENS + '}\n'


class ThemePackValidation(unittest.TestCase):
    def validate(self, css, assets=(), manifest_updates=None):
        with tempfile.TemporaryDirectory(prefix='ftl-pack-validation-') as temp:
            pack = Path(temp)
            (pack / 'theme.css').write_text(css)
            (pack / 'LICENSE.txt').write_text('CC0')
            for name in assets:
                (pack / name).write_text('<svg xmlns="http://www.w3.org/2000/svg"/>')
            manifest = dict(formatVersion=1, name='Test', slug='test', contract=4,
                            minimumLibraryVersion='5.1.0', css='theme.css', assets=list(assets),
                            license=dict(name='CC0', notice='LICENSE.txt'))
            manifest.update(manifest_updates or {})
            (pack / 'manifest.json').write_text(json.dumps(manifest))
            return subprocess.run(['python3', str(ROOT / 'scripts/validate_theme_pack.py'), temp],
                                  capture_output=True, text=True)

    def test_unscoped_selectors_are_rejected(self):
        for css in ['body { display:none; }',
                    'html[data-theme="test"] .btn, body { color:red; }',
                    '@media (width > 1px) { body { color:red; } }',
                    '@starting-style { body { opacity:0; } }']:
            with self.subTest(css=css):
                result = self.validate(BASE + css)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('PACK-SCOPE', result.stderr)

    def test_escaped_network_references_are_rejected(self):
        for css in [r'@\69mport "https://example.invalid/tracker.css";',
                    r'html[data-theme="test"] { background:u\rl(https://example.invalid/a.png); }',
                    r'html[data-theme="test"] { background:url("https\3a //example.invalid/a.png"); }']:
            with self.subTest(css=css):
                result = self.validate(css + BASE)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('PACK-CSS-ESCAPE', result.stderr)

    def test_scoped_groups_fonts_keyframes_and_literal_text_are_accepted(self):
        css = BASE + '''
@font-face { font-family:"Test"; src:url("asset.svg"); }
@keyframes pulse { from { opacity:0; } to { opacity:1; } }
@media (width > 1px) { @supports (display:grid) {
  html[data-theme="test"] .btn, html[data-theme="test"][data-variant="a"] .btn { color:red; }
} }
html[data-theme="test"] .badge::after { content:"@import url(https://example.invalid/not-a-request) \\"quoted\\""; }
/* @import "https://example.invalid/comment.css"; body {color:red} */
'''
        result = self.validate(css, ['asset.svg'])
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_ordinary_remote_references_are_rejected(self):
        for css in ['@import "https://example.invalid/style.css";',
                    'html[data-theme="test"] { background:url("https://example.invalid/image.png"); }']:
            with self.subTest(css=css):
                result = self.validate(css + BASE)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('PACK-REMOTE-CSS', result.stderr)

    def test_image_set_cannot_hide_string_asset_references(self):
        result = self.validate(BASE + 'html[data-theme="test"] { background:image-set("https://example.invalid/image.png" 1x); }')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('PACK-ASSET', result.stderr)

    def test_numeric_slug_is_rejected(self):
        result = self.validate(BASE.replace('"test"', '"123"'), manifest_updates={'slug': 123})
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('PACK-SLUG', result.stderr)


if __name__ == '__main__':
    unittest.main()
