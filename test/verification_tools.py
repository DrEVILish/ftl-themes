#!/usr/bin/env python3
"""Regression checks for screenshot acceptance and isolated verification runs."""
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("screenshots", ROOT / "scripts/screenshot_themes.py")
screenshots = importlib.util.module_from_spec(spec)
spec.loader.exec_module(screenshots)


class VerificationTools(unittest.TestCase):
    def test_failed_capture_keeps_accepted_baseline(self):
        with tempfile.TemporaryDirectory() as tmp:
            baseline = Path(tmp) / "baseline"
            baseline.mkdir()
            accepted = baseline / "accepted.png"
            accepted.write_bytes(b"accepted rendering")

            def capture(base, out, themes, engine):
                (out / "accepted.png").write_bytes(b"partial replacement")
                return dict(shots=1, themes=1, pages=2, failures=[dict(error="CSS failed")])

            with patch.object(screenshots, "baseline_dir", return_value=baseline), patch.object(screenshots, "run_screenshots", side_effect=capture):
                self.assertTrue(screenshots.run_engine("chromium", SimpleNamespace(baseline=True, theme=None), "http://unused"))
            self.assertEqual(accepted.read_bytes(), b"accepted rendering")

    def test_complete_capture_updates_baseline(self):
        with tempfile.TemporaryDirectory() as tmp:
            baseline = Path(tmp) / "baseline"

            def capture(base, out, themes, engine):
                (out / "accepted.png").write_bytes(b"complete rendering")
                return dict(shots=1, themes=1, pages=1, failures=[])

            with patch.object(screenshots, "baseline_dir", return_value=baseline), patch.object(screenshots, "run_screenshots", side_effect=capture):
                self.assertFalse(screenshots.run_engine("chromium", SimpleNamespace(baseline=True, theme=None), "http://unused"))
            self.assertEqual((baseline / "accepted.png").read_bytes(), b"complete rendering")

    def workspace(self, tmp, script):
        root = Path(tmp)
        (root / "scripts").mkdir()
        (root / "test").mkdir()
        for name in (script, "_harness.mjs"):
            shutil.copy(ROOT / "scripts" / name, root / "scripts" / name)
        (root / "scripts/node_modules").symlink_to(ROOT / "scripts/node_modules", target_is_directory=True)
        return root

    @unittest.skipUnless((ROOT / "scripts/node_modules/playwright").exists(), "Playwright is not installed")
    def test_core_run_preserves_another_runs_fixture(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.workspace(tmp, "core_regressions.mjs")
            (root / "dist").symlink_to(ROOT / "dist", target_is_directory=True)
            (root / "assets").symlink_to(ROOT / "assets", target_is_directory=True)
            other = root / "test/.core-regressions.html"
            other.write_text("another run's fixture")
            result = subprocess.run(["node", str(root / "scripts/core_regressions.mjs"), "blue-future"], capture_output=True, text=True, timeout=90)
            if "SKIP  chromium" in result.stdout:
                self.skipTest("Chromium is not installed")
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertTrue(other.exists(), "core check removed another run's fixture")
            self.assertEqual(other.read_text(), "another run's fixture")

    @unittest.skipUnless((ROOT / "scripts/node_modules/axe-core").exists() and (ROOT / "scripts/node_modules/playwright").exists(), "Playwright and axe-core are required")
    def test_a11y_blame_fails_on_measurement_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.workspace(tmp, "a11y_audit.mjs")
            (root / "dist").mkdir()
            (root / "dist/themes.json").write_text(json.dumps([dict(slug=s) for s in ("blue-future", "windows95")]))
            for slug in ("blue-future", "windows95"):
                (root / "dist" / (slug + ".css")).write_text("html {color:black} body {background:white} p {margin:0}")
            (root / "fixture.html").write_text('''<!doctype html><html lang="en"><head><title>Fixture</title>
<link id="theme-link" rel="stylesheet"><script>
const slug = new URLSearchParams(location.search).get('theme');
document.documentElement.dataset.theme = slug;
document.getElementById('theme-link').href = 'dist/' + slug + '.css';
Object.defineProperty(window, 'axe', { get() { throw new Error('measurement fixture failed'); }, set() {} });
</script></head><body><p>Fixture</p></body></html>''')
            result = subprocess.run(["node", str(root / "scripts/a11y_audit.mjs"), "--theme", "blue-future", "--theme", "windows95", "--page", "fixture", "--tier", "desktop", "--blame", "blue-future"], capture_output=True, text=True, timeout=90)
            report = json.loads((root / "test/a11y/report.json").read_text())
            if all(row.get("skipped") for row in report["results"]):
                self.skipTest("Chromium is not installed")
            self.assertTrue(any("measurement fixture failed" in row.get("error", "") for row in report["results"]), result.stdout + result.stderr)
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
