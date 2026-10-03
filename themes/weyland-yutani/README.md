# Weyland-Yutani

> Alien-franchise corporate industrial: bone-beige label plates, amber CRT readouts, hazard tape for danger only.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

The hardware of a **used-future commercial freighter** as seen in *Alien*
(1979), *Aliens* (1986) and *Alien: Isolation* (2014): warm near-black
steel, off-white equipment plates with stencil-style tracked capitals, and
amber phosphor CRT readouts. The target is a control room built by a
company that only cares about cargo, not a sci-fi HUD. Sources and honest
gaps are in `references/weyland-yutani/RESEARCH.md`. No logo or artwork is
reproduced.

## Core values

1. **Utilitarian, never glossy.** `--radius: 0`, no gradients, no
   bevels, no blurs. Panels are thin flat outlines.
2. **Labels are stencil.** Headings, buttons, table heads, panel titles,
   badges, nav and the status strip are uppercase with wide tracking
   (`--label-tracking: 0.14em`).
3. **Amber is the phosphor, and only readouts glow.** `.readout` and
   `.meter` get a faint glow and scanlines; nothing else does.
4. **Hazard striping is a danger signal, not a palette.** Yellow/black
   45deg stripes appear on `.btn-danger`, `.alert-danger`, `.toast-danger`,
   `.badge-danger` and `.status-error` only, as a leading strap. Text never
   sits on the stripes.
5. **The beige plate is the one light element.** The app bar, modal title
   bar and tooltips are bone-beige with near-black text, like a riveted
   label plate on dark equipment.
6. **Buttons are chunky caps.** 2px edge, dark underside lip, drops 2px on
   press. Primary is a solid amber block.

## Signature details

- Heavy beige top bar over a 4px amber rule; a 3rem left rail drawn in CSS
  as a ruler of tick marks with an amber marker block (empty, `aria-hidden`).
- Two registration corner marks (top-left, bottom-right) on every panel; a
  solid amber square before each panel title.
- Segmented LED-style meter bars (amber, then pale amber, then red) with a
  scanline overlay; amber mono readouts on glass-black.
- Inputs are recessed with a heavy amber underline and amber caret.
- Status strip in tracked micro-caps, its items drawn as a row of
  outlined soft keys like the terminals' function-key row; the first one
  is lit in the accent.

### Variants

The default is the hardware. The variants are the screens, one phosphor
each, from the frames in `references/weyland-yutani/` (see RESEARCH.md).
In every variant the beige plate becomes an inverse-video phosphor band
(modal title, tooltips), the top bar becomes the screen's header row
(phosphor text on black over a phosphor rule), panels get thin phosphor
outlines, and headings and readouts glow.

| Variant | Label | Source |
|---|---|---|
| (default) | Weyland-Yutani | Nostromo / Isolation hardware: beige plates, amber CRT. |
| `mother` | MU/TH/UR (green) | The MU/TH/UR 6000 interface: green phosphor `#4dff7c`. |
| `emergency` | Emergency (red) | The red "ENVIRON CTR / PURGE" and Hyperdyne terminals: red `#ff5640`. Danger moves to hazard yellow `#ffd21f` so it stays distinct from the accent. |
| `earth` | Alien: Earth (cyan) | Kirsh's specimen monitors (2025): cyan `#4fe0ff`. |

### Icons

`themes/weyland-yutani/icons.svg` redraws the full core set (178/178) as
blocky, machined stencil glyphs:
- 24 grid, stroke only at 2.2 (`--icon-stroke-width`), with
  `stroke-linecap="square"` and `stroke-linejoin="miter"` on every symbol.
- Radius 0 everywhere. Circles become squares (small) or chamfered octagons
  (r >= 5); curves become straight 45-degree runs (bell, cloud, lock shackle).
  The power arc is the one curve kept.
- Nothing is filled; dots are short square-cap ticks (`v1`).
- `currentColor` only.

## Typography

Reference: an extended Eurostile/Microgramma-class sans (the wordmark) plus
a Helvetica/Futura-like face for signage. **Nothing is vendored.** Stack:
`Eurostile, "Bank Gothic", "Century Gothic", "Segoe UI", "Helvetica Neue",
Arial, sans-serif`. Eurostile ships on macOS, Bank Gothic on Windows with
Office; elsewhere you get a generic sans, and the uppercase and tracking
carry the look. Monospace (readouts, inputs): `"Lucida Console", "DejaVu Sans
Mono", "Liberation Mono", Consolas, monospace`. The wordmark's striped
slogan face is not imitated.

## Contrast honesty

All pairs meet the lint floors; no exemptions are claimed.

| Pair | Ratio |
|---|---|
| `--text` `#e4dcc8` on `--surface` `#17150f` / `--bg` `#0e0d0a` | 13.4 / 14.2 |
| `--muted` `#a89f88` on `--surface` / `--surface-2` `#201d15` | 6.9 / 6.4 |
| `--accent` `#ffa81f` on `--surface` | 9.5 |
| `--on-accent` `#0e0d0a` on accent | 10.1 |
| `--on-danger` `#0e0d0a` on `--danger` `#ff5a3d` | 6.3 |
| `--on-success` `#0e0d0a` on `--success` `#8fd16a` | 10.6 |
| `--danger-text` `#ff7a5c` on `--surface-2` | 6.6 |
| beige bar `#d4cbb1` with `#14120d` text | above 11 |

Deviations from the reference: the amber, beige and bone values are
chosen for contrast and are not sampled from any source (none gives
official hexes). `--border` `#57503f` is 2.3:1 on the surface, deliberately
a structural line only. Danger is safety red-orange `#ff5a3d`, an addition
of mine; the reference's danger cue is hazard yellow/black, which is
carried by the stripes.

## Layout

The shell becomes a **control room**: slim ruled rail on the left, a
heavy beige label-plate bar with an amber rule, flat content on the warm
black, and a stencil status strip. At phone width the rail collapses per
core's default.

## v5 layout

Tiers: mobile ≤480px, tablet 481–900px, desktop 901–1800px, XL ≥1801px (the shell is capped at 1800px and centred, with gutter art beside it).

- **Phone (≤480) and tablet (481–900):** bar, main and status in one column. The 3rem equipment rail is switched off up to 900px (its `--app-rail-empty-display` opt-in outranks core's per-tier rail token).
- **Window caption buttons:** minimise and maximise take the label plate's ink, as close already does.
- **XL gutters (≥1801):** the bay wall: a ruled plotting grid in `--hairline` with the rail's tick-ruler marks, all in the active screen's line colours, so the MU/TH/UR, Emergency and Earth variants follow. Still.

## Don'ts

- Don't stripe anything that is not a danger state, and don't use hazard
  yellow as a background or accent.
- Don't add rounded corners, shadows (beyond the button lip), gradients or
  glass.
- Don't make green or cyan the default accent; they belong to the
  `mother` and `earth` screen variants. Don't use DOS-style boxes
  (`msdos`) or a dense all-orange terminal (`bloomberg`).
- Don't animate the scanlines or add flicker; keep them static so
  `prefers-reduced-motion` needs no special case.
- Don't put text on the striped strap, and don't add the corporate logo.

## Tell-tales of an inauthentic result

- Amber-on-black with rounded corners and no beige plate: a generic retro
  terminal.
- Hazard stripes across headers, rails or backgrounds: costume, not
  signalling.
- Sentence-case, lightly tracked labels: the stencil voice is gone.
- Glossy bevelled buttons instead of flat caps with a dark lip.
- Heavy glow or CRT curvature on ordinary text.

## Print

Scanline overlays, glow, panel corner marks and the readout/meter dark
backgrounds are neutralised in a small `@media print` block.

## Reference status

Researched from search-result summaries only; several primary pages were
blocked. Verified: wordmark set in Eurostile/Microgramma extended, Ron Cobb
as production designer, CRT terminals with scanlines, Isolation's
deliberate 1970s analogue look. Unverified: exact colours, hazard tape
placement on screen, rocker-switch proportions. See RESEARCH.md.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
