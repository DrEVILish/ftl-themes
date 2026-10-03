# Teletext

> BBC Ceefax-era broadcast teletext: the fixed 8-colour palette on solid black, laid out in flat colour blocks with no gradient, blur or anti-aliasing.

**Requires: L0** — tokens only; recolours and reflows correctly without adopting the app shell, though the app-bar's page-number badge is the one detail that needs L1 to show up.

## What this theme is trying to achieve

Teletext services (Ceefax in the UK, similar systems across Europe) ran on
a genuinely primitive display: a fixed 40x25 character grid, 8 possible
colours per character cell (foreground and background chosen from the same
set), and nothing else — no shading, no transparency, no smooth edges.
Everything that reads as "content design" on a teletext page is really
just which of those 8 colours got assigned to which block of text. This
theme reproduces that constraint deliberately rather than treating it as
a limitation to soften.

## Core values

1. **Exactly 8 colours, used flat.** Black, red, green, yellow, blue,
   magenta, cyan, white — anything else (even a tint or shade of one of
   these) breaks the premise. `--muted` is the one deliberate
   exception, documented in the token comment.
2. **Zero roundness, zero softness.** No border-radius, no box-shadow, no
   gradient, anywhere. A teletext frame is drawn from flat rectangular
   colour cells; a rounded corner or drop shadow is the fastest way to
   look like a modern UI wearing a teletext palette rather than the real
   thing.
3. **Colour blocks carry meaning, not decoration.** A red block is a
   warning/index colour, cyan is the page-header colour, yellow is
   reserved for headlines — matching the real service's own colour
   conventions, not chosen for visual variety.

## Signature details

- The page number ("P100") opens the header row in plain white, as on
  every real page; the nav links that follow each take a different
  broadcast colour (cyan / green / yellow / magenta), like a page's index
  lines.
- `h1` is the section banner: a full-width blue band with the headline
  in yellow at true double height (`transform: scaleY(2)`, the band
  stretching with it as the hardware row did).
- Panel titles are full-width colour bands (blue / green / magenta /
  yellow by position, each with the text colour it needs); cards carry a
  thick band of the same colour on top. Nothing draws a line: table rules
  and hairlines are gone, as on the real service.
- Tabs are coloured words; the selected one is white on a blue band.
- **Fastext:** the status strip ends with the four key words — red
  *Headlines*, green *Sport*, yellow *Weather*, cyan *TV Guide* — one
  monospaced string coloured cell-for-cell by a gradient clipped to the
  text.
- Selected/active rows invert to a solid colour fill with black text
  (`--row-selected-bg`), not a tint or outline — real teletext has no
  concept of a translucent highlight.

## Icons

`themes/teletext/icons.svg` redraws the full core icon set (178/178,
plus `sun-moon`) as solid colour-cell block graphics, like the real
service's character-cell display. Style rules, taken from the original
subset and followed by every later addition:

- **Cells, not lines:** each glyph is a union of filled axis-aligned
  rectangles in `<g fill="currentColor" stroke="none">`, with no strokes,
  curves, diagonals or anti-aliasing. Circles, slashes and arcs are
  stair-stepped cells.
- **Grid:** 24×24 viewBox. The original subset uses whole-unit blocks
  (mostly 2–4 units). The later additions sit on a 12×12 grid of 2-unit
  cells (strokes 1–2 cells thick, gaps of at least 1 cell) and pack each
  glyph's cells into one path per tone to keep the sprite small.
- **Second tone:** a dimmed cell (`fill-opacity` 0.3–0.5) marks secondary
  detail such as map folds, a pie slice or disc glare. A dim cell must
  never sit on top of a solid one, because it would vanish. A few
  original glyphs (coin, compass, layout and others) do stack them, so
  their inner mark is invisible.
- **Lettering:** the `PDF`/`PNG` labels are 3×5-cell block letters, not
  text.
- **Palette:** `currentColor` only.

## v5 layout

Tiers: mobile ≤480px, tablet 481–900px, desktop 901–1800px, XL ≥1801px (the shell is capped at 1800px and centred, with gutter art beside it).

Core's tiers do the work; the theme has no breakpoints of its own.

- **Phone (≤480) and tablet (481–900):** bar, main and status in one column. The "P100" page number is now part of the bar's first line rather than an absolute overlay, so on a phone the brand truncates after it instead of sliding underneath it. The double-height headline scales down (`clamp`) so it still fits a 393px screen at double height.
- **Nested surfaces:** a panel inside a panel, card, dialog, drawer or popover drops its full-width colour band and shows its title in the band's colour over a thin band, as a card does, so bands never stack.
- **XL gutters (≥1801):** a dark teletext page beside the frame: dim blue header bands every ten character rows and sparse mosaic blocks in the broadcast eight, dimmed to within 1.5:1 of black. Hard stops only, and still.

## Tell-tales of an inauthentic result

- Any rounded corner, drop shadow, or gradient fill.
- A colour outside the 8-value set (a muted grey button fill, a pastel
  accent, anything with partial opacity over content).
- Smooth/anti-aliased type — the real thing is aliased bitmap type; a
  system sans with subpixel rendering will never fully sell this, but at
  minimum stay monospace and avoid font smoothing tricks that fight it.

## Don'ts

- **No radius, shadow, gradient or transparency.** Flat colour cells only.
- **No colour outside the 8-value set** (the one documented exception is `--muted` `#b3b3b3` and the `--hairline` rule).
- **No white text on the red fill** (see Contrast honesty), even though real teletext did it.
- **No proportional or smoothed type.** Monospace, no font-smoothing tricks.
- **No translucent hover/selection.** Selection is a full solid invert.

## Typography

`--font` and `--font-mono` are **Bedstead**, vendored (`assets/fonts/Bedstead.woff2`, CC0 — see `assets/fonts/NOTICE.md`): Ben Harris's outline recreation of the SAA5050 character generator, so the blocky, stepped glyphs in all three captures are the real shapes. The subset keeps the teletext sextant mosaics (U+1FB00–1FBAF) for block graphics.

## Contrast honesty

- **Palette is exact; the deviations are two.** `--muted` `#b3b3b3` (10.02:1 on black) is not in the 8-colour set and exists only because the design system needs a secondary-text role; `--hairline` `#4d4d4d` is a rule colour, not text.
- **White-on-red lifted to black-on-red.** Real teletext printed white on red, which is 4.0:1, under the 4.5:1 floor. `--on-danger` and the active header nav item are black on `#ff0000` (5.25:1), still inside the 8-colour set. Black on cyan 16.75:1, on green 15.30:1.
- **On black:** cyan 16.75:1, yellow 19.56:1, magenta `#ff00ff` 6.70:1, red 5.25:1, green 15.30:1, white 21:1. So all eight clear AA on black; red is the tightest.
- In the ARTE capture, red text sits on a white ground and white on blue; the theme is black-ground only, so those pairings (red on white ~4:1) are not reproduced.

## Reference status

`references/teletext/` holds 3 captures plus `RESEARCH.md`, all pure text screens with no people:

- `teletext-arte-page100.png` — an ARTE page 100: blocky aliased type, a page-number/clock header row, blue-band panels and a blue `101 SOMMAIRE` footer bar. Backs the flat colour-cell blocks and the page-number header idea (the `P100` badge).
- `teletext-ceefax-football-index.jpg` — a BBC Ceefax football index: cyan headline list with page numbers, white double-height lead lines and a blue title band. Backs the cyan index look, double-height headlines and the 8-colour palette.
- `teletext-screen-teletexnews.png` — a teletext news page (300): double-height headlines, an index list and a blue footer strip. Backs the double-height and newsflash frame.

Uncertain: `RESEARCH.md` describes a red/green/yellow/blue Fastext bar, but I could not see a four-colour Fastext key bar in any of the three files at their resolution (only blue/yellow footer bands); the Fastext row follows the service's own four-colour key convention rather than any one capture.
