# aqua — visual reference notes

Outsider read: Gel candy buttons (blue pulsing default), fine pinstripes -> brushed metal, red/yellow/green traffic-light spheres, Lucida Grande.

Capture targets: Snow Leopard window; gel buttons; Dock reflection.

Sources: Wikipedia Aqua UI.

Use side-by-side with example.html; local captures are copyrighted originals — this file is the textual checklist.

Audit 2026-09-26: inspected 7 files; removed 1 (8660e88781d6..._600.webp — Leopard icon grid with photographic people in icons); kept 6 (Panther Finder window, Leopard Guest Finder window, Snow Leopard widget gallery, Aqua toolbar controls, Leopard icon set sheet, leopard-huge-iconpack-650-screenshot.avif — previously flagged undecodable, now verified decodable via ffmpeg, Leopard app-icon grid, no people).

## Measured: Snow Leopard window and controls (2026-10-09)

`31db2b68338d1ae9.png` is a lossless 1070×700 PNG of a Snow Leopard window
with one of every standard control. It is a 2x capture (every 1px rule is
2px wide), so sizes below are halved to 1x. Sampled with ImageMagick
(`convert 31db2b68338d1ae9.png -crop 1x1+X+Y +repage txt:-`), coordinates
in the PNG's own pixels.

| What | Where | Measured | Theme |
|---|---|---|---|
| Title bar | column x=300, y=50–97 | 22px tall (at 1x); `#cbcbcb` top edge, `#e2e2e2` 1px highlight, then `#cdcdcd` down to `#a8a8a8`; `#5f5f5f` rule below | `--app-bar-bg`, `--app-bar-rule` |
| Red light | column x=143, y=61–88; row y=76 | about 13.5px across (1x); rim `#680000`/`#a90000`; white specular cap (`#eacbcb` at y=64); body `#de2a2a` (y=70), `#f66d6d` (y=76), `#fb9999` (y=80), `#efbfbf` (y=84) | `--aqua-lights` |
| Yellow light | column x=185 | rim `#792800`; `#d69928`, `#f6cc5d`, `#f6f282`, `#e4e07f` top to bottom | `--aqua-lights` |
| Green light | column x=226 | rim `#0e5200`; `#89c648`, `#baf07f`, `#d6f69d`, `#cee1a2` | `--aqua-lights` |
| Light pitch | red x=143, yellow x=185, green x=226 | 41–42px apart, so about 21px at 1x | `background-position` 0 / 1.3rem / 2.6rem |
| Push button | column x=560, y=182–223 | rim `#5d5d5d`; flat `#f1f1f1`–`#f3f3f3` for the upper 37%, a hard step to `#e5e5e5`, then lighter to `#ffffff` at the bottom | `--btn-bg`, `--btn-border` |
| Default button | column x=760, y=182–223 | rim `#212a95` (top) to `#6d737b` (bottom); `#d8ecff` to `#c2e1fd` over the upper 37%, a hard step to `#8bc5f9`, then `#a5d6fe` and `#d9fdfe` at the bottom; black label | `.btn-primary` |
| Selected tab segment | column x=440, y=122–148 | rim `#2a2190`; `#d7e3f2` to `#bfd8f2`, a step to `#7db0e4`, then lighter | not applied (see below) |

Derived, not measured: the default button's side rim `#45508a` (between
the measured top and bottom), its hover gradient (each stop a few percent
darker), the lights' rim drawn as a 75% tint of the sampled rim colour over
the body, and the specular cap's shape. Not applied: the tab view's
segmented look (the theme keeps core's underline tabs), and the red/green
filled buttons, which Snow Leopard did not have.
