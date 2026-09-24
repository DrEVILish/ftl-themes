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
   these) breaks the premise. `--ftl-muted` is the one deliberate
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
  (`--ftl-row-selected-bg`), not a tint or outline — real teletext has no
  concept of a translucent highlight.

## Tell-tales of an inauthentic result

- Any rounded corner, drop shadow, or gradient fill.
- A colour outside the 8-value set (a muted grey button fill, a pastel
  accent, anything with partial opacity over content).
- Smooth/anti-aliased type — the real thing is aliased bitmap type; a
  system sans with subpixel rendering will never fully sell this, but at
  minimum stay monospace and avoid font smoothing tricks that fight it.
