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

- The page-number badge ("P100") in the top-left of the app-bar, in white
  on a solid red block — every real teletext page opens with exactly this.
- `h1` renders at double height (`transform: scaleY(1.9)`), the one
  hardware trick reserved for headlines on real teletext frames.
- Selected/active rows invert to a solid colour fill with black text
  (`--row-selected-bg`), not a tint or outline — real teletext has no
  concept of a translucent highlight.

### Icons

`themes/teletext/icons.svg` redraws six icons (home, settings, search,
close, user, bell) as solid colour-cell block graphics on a coarse pixel
grid, exactly like the real service's character-cell display: every
shape is a union of filled rectangles snapped to a 4-unit grid, with zero
strokes, zero curves and zero anti-aliasing — a hollow square-and-handle
stands in for the search icon's usual circle, and settings is abstracted
to a plus of blocks rather than a naturalistic gear, since real teletext
graphics were never skeuomorphic. The sprite ships 123 `<symbol>`s in total (`grep -c '<symbol'`), and each differs from the generic outline sprite in `assets/icons/icons.svg`; only the six above are described here, and the rest were not audited one by one for style.

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

`--font` and `--font-mono` are both `"Consolas", "Courier New", monospace`. **Nothing is vendored.** The real face is the teletext character-generator bitmap font on a 40x24/25 grid (Bedstead is the usual web recreation); it is not shipped because it has no faithful system equivalent, so the block-shaped glyphs are lost and only the monospace grid remains. All three captures show that blocky face; the fallback does not match it.

## Contrast honesty

- **Palette is exact; the deviations are two.** `--muted` `#b3b3b3` (10.02:1 on black) is not in the 8-colour set and exists only because the design system needs a secondary-text role; `--hairline` `#4d4d4d` is a rule colour, not text.
- **White-on-red lifted to black-on-red.** Real teletext printed white on red, which is 4.0:1, under the 4.5:1 floor. `--on-danger` is black on `#ff0000` (5.25:1), still inside the 8-colour set. Black on cyan 16.75:1, on green 15.30:1.
- **On black:** cyan 16.75:1, yellow 19.56:1, magenta `#ff00ff` 6.70:1, red 5.25:1, green 15.30:1, white 21:1. So all eight clear AA on black; red is the tightest.
- In the ARTE capture, red text sits on a white ground and white on blue; the theme is black-ground only, so those pairings (red on white ~4:1) are not reproduced.

## Reference status

`references/teletext/` holds 3 captures plus `RESEARCH.md`, all pure text screens with no people:

- `teletext-arte-page100.png` — an ARTE page 100: blocky aliased type, a page-number/clock header row, blue-band panels and a blue `101 SOMMAIRE` footer bar. Backs the flat colour-cell blocks and the page-number header idea (the `P100` badge).
- `teletext-ceefax-football-index.jpg` — a BBC Ceefax football index: cyan headline list with page numbers, white double-height lead lines and a blue title band. Backs the cyan index look, double-height headlines and the 8-colour palette.
- `teletext-screen-teletexnews.png` — a teletext news page (300): double-height headlines, an index list and a blue footer strip. Backs the double-height and newsflash frame.

Uncertain: `RESEARCH.md` describes a red/green/yellow/blue Fastext bar, but I could not see a four-colour Fastext key bar in any of the three files at their resolution (only blue/yellow footer bands); the theme's double-height `h1` is `transform: scaleY(1.9)`, an approximation of the hardware trick.
