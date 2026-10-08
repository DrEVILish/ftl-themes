#!/usr/bin/env python3
"""Small stdlib checks for the generated indexes and local theme packs."""
import json
import pathlib
import subprocess
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]

def run(*args):
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True)

assert run("python3", "scripts/build_component_index.py", "--check").returncode == 0
themes = ("windows95", "winxp-luna", "win7-aero", "ios-skeuomorphic", "ios-flat", "liquid-glass")
report = run("python3", "scripts/theme_report.py", *sum((["--theme", slug] for slug in themes), []))
assert report.returncode == 0, report.stderr
coverage = json.loads(report.stdout)["themes"]
assert {row["slug"] for row in coverage} == set(themes)
assert all(row["componentCoverage"]["total"] > 0 for row in coverage)
catalogue = json.loads((ROOT / "dist/themes.json").read_text())
assert all({"tokens", "fonts", "iconCoverage", "references", "componentCoverage", "navigationPatterns", "family", "extends"} <= set(row) for row in catalogue)
assert all(row["iconCoverage"]["total"] == 178 for row in catalogue)
assert all(".app-status.tabbar" in (ROOT / "dist" / (row["slug"] + ".css")).read_text() for row in catalogue)
by_slug = {row["slug"]: row for row in catalogue}
# winxp-luna no longer extends windows95 (its bevels beat XP's tokens), so the
# Windows family is rooted at winxp-luna; alienware re-skins XP.
assert by_slug["win7-aero"]["family"] == "winxp-luna" and by_slug["win7-aero"]["extends"] == "winxp-luna"
assert by_slug["alienware"]["family"] == "winxp-luna" and by_slug["alienware"]["extends"] == "winxp-luna"
assert by_slug["winxp-luna"]["extends"] is None
assert by_slug["liquid-glass"]["family"] == "ios-skeuomorphic" and by_slug["liquid-glass"]["extends"] == "ios-flat"
assert 'html[data-theme="windows95"]' not in (ROOT / "dist/winxp-luna.css").read_text()
assert 'html[data-theme="win7-aero"]' in (ROOT / "dist/tokens.css").read_text()
assert "--cursor-default" in (ROOT / "core/cursors.css").read_text()
assert '"theme-feedback-v1"' in (ROOT / "theme-feedback.html").read_text()

with tempfile.TemporaryDirectory(prefix="ftl-theme-pack-") as temp:
    pack = pathlib.Path(temp)
    (pack / "theme.css").write_text('html[data-theme="my-theme"] { --bg:#111; --surface:#222; --surface-2:#333; --border:#555; --hairline:#444; --text:#fff; --muted:#ccc; --accent:#0af; --accent-2:#f0a; --danger:#f00; --success:#0f0; --warning:#ff0; --on-accent:#000; --on-danger:#000; --on-success:#000; --radius:4px; --font:sans-serif; --font-mono:monospace; --flare:#0af; }')
    (pack / "LICENSE.txt").write_text("CC0")
    manifest = {"formatVersion": 1, "name": "Test Pack", "slug": "my-theme", "contract": 4,
                "minimumLibraryVersion": "5.1.0", "css": "theme.css", "assets": [],
                "license": {"name": "CC0-1.0", "notice": "LICENSE.txt"}}
    manifest_path = pack / "manifest.json"
    manifest_path.write_text(json.dumps(manifest))
    valid = run("python3", "scripts/validate_theme_pack.py", str(pack), "--preview")
    assert valid.returncode == 0, valid.stderr
    assert (pack / "preview.html").is_file()
    manifest["css"] = "../outside.css"
    manifest_path.write_text(json.dumps(manifest))
    invalid = run("python3", "scripts/validate_theme_pack.py", str(pack))
    assert invalid.returncode != 0 and "PACK-CSS" in invalid.stderr

layout = (ROOT / "core/layout.css").read_text()
assert "(display-mode: standalone)" in layout and "--folding-mode: book" in layout and "--folding-mode: tabletop" in layout
assert "foldMode" in (ROOT / "assets/js/foldable.js").read_text()
assert "getComputedStyle(html)" in (ROOT / "assets/js/foldable.js").read_text()
assert "window.viewport" not in (ROOT / "assets/js/foldable.js").read_text()
assert "window.ftlAppReady" in (ROOT / "assets/js/boot.js").read_text()
assert "prefers-reduced-motion" in (ROOT / "core/components/experience.css").read_text()
print("feature extension checks passed (Windows and iOS theme families)")
