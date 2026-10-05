#!/usr/bin/env python3
"""Per-theme favicons and app icons (PLAN.md §23) -> dist/favicons/

One SVG template, filled from each theme's resolved tokens: the title-bar
colour as the tile, the accent as a framed window mark, the radius from
--radius. Writes, per theme:
  <slug>.svg               favicon (rel="icon" type="image/svg+xml")
  <slug>-maskable.svg      full-bleed tile, mark inside the 80% safe zone
  <slug>-180.png           apple-touch-icon
  <slug>-192.png, -512.png PWA manifest icons
  <slug>-maskable-512.png  PWA "maskable" icon
PNGs need librsvg (`rsvg-convert`); without it only the SVGs are written.

Usage: python3 scripts/build_favicons.py [slug ...]   (default: every theme)
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build_emails import palette, ink_on, contrast  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "dist" / "favicons"


def tile_radius(radius):
    """--radius (px/rem/em) mapped onto a 64-unit tile, 4..22."""
    m = re.match(r"([\d.]+)(px|rem|em)?", radius or "")
    px = float(m.group(1)) * (16 if m and m.group(2) in ("rem", "em") else 1) if m else 4
    return max(4, min(22, round(px * 2)))


def svg(p, maskable=False):
    bg = p["bar"]
    mark = p["accent"] if contrast(p["accent"], bg) >= 3 else ink_on(bg, p["on_bar"])
    dot = p["on_bar"]
    r = tile_radius(p["radius"])
    tile = (f'<rect width="64" height="64" fill="{bg}"/>' if maskable
            else f'<rect width="64" height="64" rx="{r}" fill="{bg}"/>')
    s = 0.8 if maskable else 1.0  # maskable: keep the mark in the safe zone
    inner = max(2, round(r * 0.45))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">{tile}'
            f'<g transform="translate({32 - 32 * s} {32 - 32 * s}) scale({s})">'
            f'<rect x="13" y="15" width="38" height="34" rx="{inner}" fill="none" stroke="{mark}" stroke-width="5"/>'
            f'<rect x="13" y="15" width="38" height="9" rx="{inner}" fill="{mark}"/>'
            f'<circle cx="24" cy="37" r="4.5" fill="{dot}"/>'
            f'<rect x="32" y="34" width="12" height="6" rx="2" fill="{dot}"/></g></svg>\n')


def png(src, dest, size):
    subprocess.run(["rsvg-convert", "-w", str(size), "-h", str(size), "-o", str(dest), str(src)], check=True)


def main(slugs):
    OUT.mkdir(parents=True, exist_ok=True)
    has_convert = shutil.which("rsvg-convert") is not None
    for slug in slugs:
        try:
            p = palette(slug)
        except ValueError as exc:
            raise SystemExit(str(exc))
        fav, mask = OUT / f"{slug}.svg", OUT / f"{slug}-maskable.svg"
        fav.write_text(svg(p))
        mask.write_text(svg(p, maskable=True))
        if has_convert:
            for size in (180, 192, 512):
                png(fav, OUT / f"{slug}-{size}.png", size)
            png(mask, OUT / f"{slug}-maskable-512.png", 512)
    print(f"built dist/favicons for {len(slugs)} theme(s)" + ("" if has_convert else " (SVG only: no rsvg-convert)"))


if __name__ == "__main__":
    if sys.argv[1:] == ["--test"]:
        assert tile_radius("0") == 4 and tile_radius("0.5rem") == 16 and tile_radius("40px") == 22
        out = svg(palette("blue-future"))
        assert out.startswith("<svg") and "var(" not in out and 'rx="' in out
        assert 'scale(0.8)' in svg(palette("blue-future"), maskable=True)
        print("ok"); sys.exit()
    main(sys.argv[1:] or sorted(p.parent.name for p in (ROOT / "themes").glob("*/theme.css")))
