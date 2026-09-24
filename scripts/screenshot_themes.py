#!/usr/bin/env python3
"""Visual-regression tool for ftl-themes.

Screenshots every theme in dist/themes.json against every example*.html QA
page at a fixed 1280x900 viewport, and either writes those screenshots as
the committed baseline (--baseline) or diffs them against the existing
baseline and reports what changed (default).

This replaces the ad-hoc throwaway Playwright scripts previously used to
eyeball theme changes: run it, read the report, and if a change is
intentional, re-run with --baseline to accept the new rendering.

Usage:
    python3 scripts/screenshot_themes.py              # diff mode
    python3 scripts/screenshot_themes.py --baseline    # (re)write baseline
    python3 scripts/screenshot_themes.py --threshold 0.5   # tune sensitivity

See test/README.md for the full explanation.
"""
from __future__ import annotations

import argparse
import http.server
import json
import os
import shutil
import socket
import subprocess
import sys
import tempfile
import threading
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASELINE_DIR = ROOT / "test" / "visual-baseline"
DIFF_DIR = ROOT / "test" / "visual-diffs"
THEMES_JSON = ROOT / "dist" / "themes.json"
SHOT_HELPER = ROOT / "scripts" / "_pw_shot.mjs"
PLAYWRIGHT_SRC = "/opt/node22/lib/node_modules/playwright"
EXAMPLE_PAGES = ["example", "example-2", "example-3", "example-4"]

# Percentage of pixels (0-100) that must differ, beyond DIFF_PIXEL_TOLERANCE
# per-channel noise, before a page is reported as changed. Anti-aliasing and
# font hinting can wobble a handful of pixels between runs even with no
# real change, so this isn't 0.
DEFAULT_THRESHOLD = 0.10
# Per-channel (0-255) delta below which a pixel doesn't count as "different"
# at all -- filters out sub-visual rounding noise before the percentage above
# is computed.
DIFF_PIXEL_TOLERANCE = 24


def find_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def serve_repo(port: int):
    handler = lambda *a, **kw: QuietHandler(*a, directory=str(ROOT), **kw)
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    return httpd


def wait_for_server(port: int, timeout: float = 10.0):
    import urllib.request

    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            urllib.request.urlopen(f"http://127.0.0.1:{port}/dist/themes.json", timeout=1)
            return
        except Exception:
            time.sleep(0.1)
    raise RuntimeError("local http server did not come up in time")


def ensure_playwright_symlink():
    """Node resolves `playwright` by walking up node_modules/ from the
    script's own directory, so scripts/node_modules/playwright must exist.
    Playwright itself isn't a repo dependency (no package.json here) --
    it's provided by the sandbox at PLAYWRIGHT_SRC -- so point at that."""
    node_modules = ROOT / "scripts" / "node_modules"
    link = node_modules / "playwright"
    if link.exists():
        return
    if not os.path.isdir(PLAYWRIGHT_SRC):
        raise RuntimeError(
            f"playwright not found at {PLAYWRIGHT_SRC} and no scripts/node_modules/playwright "
            "symlink exists -- install playwright or create the symlink yourself."
        )
    node_modules.mkdir(parents=True, exist_ok=True)
    os.symlink(PLAYWRIGHT_SRC, link)


def run_screenshots(base_url: str, outdir: Path) -> dict:
    env = dict(os.environ)
    env.setdefault("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
    env.setdefault("PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD", "1")
    proc = subprocess.run(
        ["node", str(SHOT_HELPER), "--base", base_url, "--outdir", str(outdir)],
        cwd=str(ROOT),
        env=env,
        capture_output=True,
        text=True,
    )
    if proc.returncode not in (0, 1):
        sys.stderr.write(proc.stdout)
        sys.stderr.write(proc.stderr)
        raise RuntimeError(f"screenshot helper crashed (exit {proc.returncode})")
    try:
        result = json.loads(proc.stdout.strip().splitlines()[-1])
    except (IndexError, ValueError):
        sys.stderr.write(proc.stdout)
        sys.stderr.write(proc.stderr)
        raise RuntimeError("could not parse screenshot helper output")
    if result.get("failures"):
        for f in result["failures"]:
            sys.stderr.write(f"  navigation failed: {f['slug']} {f['pageName']}: {f['error']}\n")
    return result


def load_theme_slugs() -> list[str]:
    with open(THEMES_JSON) as f:
        data = json.load(f)
    return sorted(t["slug"] for t in data)


def _changed_mask(baseline, actual):
    """L-mode (0/255) mask of pixels whose max per-channel delta between
    baseline and actual exceeds DIFF_PIXEL_TOLERANCE. Built entirely out of
    Pillow's own (C-implemented) per-band ops, so no numpy dependency is
    needed for what would otherwise be a slow per-pixel Python loop."""
    from PIL import ImageChops

    diff = ImageChops.difference(baseline, actual)
    r, g, b = diff.split()
    threshold = lambda band: band.point(lambda x: 255 if x > DIFF_PIXEL_TOLERANCE else 0)
    return ImageChops.lighter(ImageChops.lighter(threshold(r), threshold(g)), threshold(b))


def diff_images(baseline_path: Path, actual_path: Path):
    """Returns diff_percent: the share of pixels (0-100) whose per-channel
    delta exceeds DIFF_PIXEL_TOLERANCE. A simple tolerance-gated pixel diff
    -- not perceptual/SSIM-grade, but enough signal for "did this theme
    visibly change"."""
    from PIL import Image

    if not baseline_path.exists():
        return 100.0  # no baseline at all -> treat as fully new/changed

    baseline = Image.open(baseline_path).convert("RGB")
    actual = Image.open(actual_path).convert("RGB")

    if baseline.size != actual.size:
        return 100.0  # dimension mismatch is itself a hard fail

    mask = _changed_mask(baseline, actual)
    changed = mask.histogram()[255]
    total = mask.size[0] * mask.size[1]
    return 100.0 * changed / total


def make_diff_visual(baseline_path: Path, actual_path: Path):
    """A red-highlight visualization of where actual differs from baseline,
    for the failing-diffs folder a human will actually look at."""
    from PIL import Image

    baseline = Image.open(baseline_path).convert("RGB")
    actual = Image.open(actual_path).convert("RGB")
    if baseline.size != actual.size:
        return actual

    mask = _changed_mask(baseline, actual)
    red = Image.new("RGB", actual.size, (255, 0, 0))
    highlight = Image.blend(actual, red, 0.6)
    return Image.composite(highlight, actual, mask)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--baseline", action="store_true", help="write/overwrite the committed baseline instead of diffing against it")
    parser.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD, help=f"diff-mode fail threshold, percent of pixels changed (default {DEFAULT_THRESHOLD})")
    parser.add_argument("--theme", action="append", help="limit to this theme slug (repeatable); default is every theme in dist/themes.json")
    args = parser.parse_args()

    if not THEMES_JSON.exists():
        sys.exit(f"error: {THEMES_JSON} not found -- run scripts/build.sh first")

    ensure_playwright_symlink()

    port = find_free_port()
    httpd = serve_repo(port)
    base_url = f"http://127.0.0.1:{port}"
    tmp_root = None
    try:
        wait_for_server(port)

        if args.baseline:
            BASELINE_DIR.mkdir(parents=True, exist_ok=True)
            print(f"Writing baseline screenshots to {BASELINE_DIR} ...")
            result = run_screenshots(base_url, BASELINE_DIR)
            print(f"Wrote {result['shots']} screenshot(s) across {result['themes']} theme(s) x {result['pages']} page(s).")
            if result.get("failures"):
                sys.exit(f"{len(result['failures'])} page(s) failed to load -- see stderr above.")
            return

        if not BASELINE_DIR.exists() or not any(BASELINE_DIR.iterdir()):
            sys.exit(
                f"error: no baseline at {BASELINE_DIR}. Run with --baseline first "
                "(only after confirming any current rendering differences are intentional)."
            )

        tmp_root = Path(tempfile.mkdtemp(prefix="ftl-visual-"))
        print("Taking screenshots for comparison ...")
        result = run_screenshots(base_url, tmp_root)
        print(f"Captured {result['shots']} screenshot(s). Diffing against baseline ...\n")

        themes = load_theme_slugs()
        if args.theme:
            themes = [t for t in themes if t in set(args.theme)]

        rows = []
        any_fail = False
        if DIFF_DIR.exists():
            shutil.rmtree(DIFF_DIR)

        for slug in themes:
            for page in EXAMPLE_PAGES:
                baseline_path = BASELINE_DIR / slug / f"{page}.png"
                actual_path = tmp_root / slug / f"{page}.png"
                if not actual_path.exists():
                    rows.append((slug, page, "FAIL", None, "no screenshot captured (nav error?)"))
                    any_fail = True
                    continue
                pct = diff_images(baseline_path, actual_path)
                status = "FAIL" if pct > args.threshold else "pass"
                note = ""
                if not baseline_path.exists():
                    note = "no baseline"
                rows.append((slug, page, status, pct, note))
                if status == "FAIL":
                    any_fail = True
                    diff_out_dir = DIFF_DIR / slug
                    diff_out_dir.mkdir(parents=True, exist_ok=True)
                    if baseline_path.exists():
                        shutil.copy(baseline_path, diff_out_dir / f"{page}.baseline.png")
                        visual = make_diff_visual(baseline_path, actual_path)
                        visual.save(diff_out_dir / f"{page}.diff.png")
                    shutil.copy(actual_path, diff_out_dir / f"{page}.actual.png")

        name_w = max(len(f"{s}/{p}") for s, p, *_ in rows)
        for slug, page, status, pct, note in rows:
            label = f"{slug}/{page}".ljust(name_w)
            pct_str = f"{pct:6.3f}%" if pct is not None else "   n/a "
            suffix = f"  ({note})" if note else ""
            print(f"  {status:5s} {label} {pct_str}{suffix}")

        fails = sum(1 for r in rows if r[2] == "FAIL")
        print(f"\n{len(rows)} checked, {len(rows) - fails} passed, {fails} failed (threshold {args.threshold}%).")
        if fails:
            print(f"Failing diffs written to {DIFF_DIR} for review.")
            print("If these changes are intentional, re-run with --baseline to accept them.")
        sys.exit(1 if any_fail else 0)
    finally:
        httpd.shutdown()
        if tmp_root and tmp_root.exists():
            shutil.rmtree(tmp_root, ignore_errors=True)


if __name__ == "__main__":
    main()
