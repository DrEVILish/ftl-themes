# Aqua

> macOS Snow Leopard — brushed metal, pinstripes, candy gloss.

**Requires: L1** — sets `--ftl-app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

**Mac OS X circa 10.6**: glossy "candy" controls, brushed-metal window
chrome, pinstriped surfaces, and generous soft shadows. Optimistic,
tactile, unmistakably pre-flat-design.

## Core values

1. **Everything is lit from above.** A control is a gradient from light to
   dark with a bright top highlight inset. That single convention produces
   most of the look.
2. **Gloss on fills, gloss only.** Gradients belong on buttons, bars and
   panels — never on text or borders.
3. **Depth is soft, not hard.** Large blurred shadows at low opacity; no
   crisp 1px drop shadows.
4. **The window floats.** The shell has rounded corners and sits on a
   desktop gradient with a real shadow beneath it.
5. **Light theme discipline.** This is the catalogue's first light theme,
   so filled controls need explicit white foregrounds — the dark-theme
   habit of painting them `--ftl-bg` fails here. That's exactly what
   `--ftl-on-accent`/`-danger`/`-success` are for.

## Signature details

- Panels carry an actual **pinstripe**: a 3px repeating white-at-35%
  gradient over the surface gradient.
- The modal header is centred, with its own metal gradient — a Mac sheet.
- Selected table rows fill solid Aqua blue with white text.
- Focus adds a soft 3px blue halo rather than a hard ring.

## Layout

The shell becomes a **Mac window**: 0.75rem desktop margin, a rounded
brushed-metal title bar, a near-white content area, and a rounded metal
status strip, with a 28px blurred shadow under the whole frame.

## Extending it

Do: keep every fill a top-light gradient; keep shadows large and soft.
Don't: flatten a control to a solid fill, or use pure white text on a light
fill without checking the contrast floor.

## Tell-tales of an inauthentic result

- Flat solid buttons → this is the one theme where flat is wrong.
- Hard-edged shadows.
- Dark text on a mid-blue fill (fails contrast and looks unfinished).
- Square window corners.

## Adoption

This theme sets `--ftl-app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.ftl-app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
