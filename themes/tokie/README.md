# Tokie

> Black full-grain leather, saddle-stitched, with brushed-gold rails and polished mirror-gold buttons: a bespoke watch box as an interface.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

The inside of a luxury leather-goods object: a watch box, a writing
case, a bank director's briefcase. Black pebble-grain leather you could
rest a hand on, panels finished with a saddle stitch, lettering struck
into the leather in gold foil, and gold hardware in two finishes: brushed
(satin) for the fixed structure and polished (mirror) for what you press.
It should feel restrained and expensive. It is not a casino, and not
steampunk brass. Sources are in `references/tokie/RESEARCH.md`.

## Core values

1. **Three materials, each with one job.** Leather for surfaces (page,
   panels, cards, inputs, menus). Brushed gold for structure (spine rail,
   the bar's hinge rail, the status nameplate, table-head and nav rules,
   tooltips, scribble strips). Polished gold for what you press or what
   is focused (primary/GO buttons, active segmented, pagination and
   filter badges, thumbs, the knob crown, progress fill, the focus ring).
   Don't swap them.
2. **Leather is matte and black.** Surfaces are near-black (`#0b0a09` to
   `#1d1a17`) with a visible pebble grain. No gloss, no brown tint.
3. **Stitching is on the edge, never under text.** The saddle stitch runs
   7px inside the edge of panels, cards, dialogs, drawers and the bar.
   Small elements (buttons, inputs, badges, transport) are not stitched.
4. **Gold foil, not gold paint.** Type on leather is flat gold with a
   deboss shadow (dark above, faint light below), tracked uppercase in a
   Didone serif. No gradient text, no glow.
5. **Polished gold has a horizon.** Mirror gold is a hard gradient with
   a dark band just above the middle. Without that band it reads as
   yellow plastic.
6. **Restraint.** One gold, one thread colour, no ornament beyond the
   stitch, the gilt fillets and the two rail screws.

## Signature details

- Pebble grain is an SVG `feTurbulence` + `feDiffuseLighting` tile
  (200px, data-URI) under a 93%-opaque black wash. There are no bitmaps.
- The saddle stitch (`--tokie-stitch`) is eight background layers: four
  dashed champagne threads (5px stitch, 3px hole) over four darker
  creased grooves. It costs no pseudo-elements, so any surface can wear it.
- Brushed gold is anisotropic noise (`baseFrequency='0.002 0.9'`),
  stretched into horizontal hairlines over a satin vertical gradient. The
  spine rail uses the same noise rotated so its hairlines run vertically.
- Panel and dialog titles are foil caps above a double gilt fillet (1px
  gold, 2px gap, 1px darker gold), the way a binder's roll lays a line.
- Buttons: the default is a leather key with a gold bezel; primary is
  polished gold with engraved dark text; danger and success are enamelled
  oxblood and bottle-green leather that keep the gold bezel.
- Readouts are black lacquer dials with applied gold Didone numerals and
  a thin gold chapter ring. Knobs are polished watch crowns with a fluted
  edge.
- The focus ring is 2px polished gold at a 3px offset with a soft gold
  halo. It is visible on every control, on leather and on gold.

## Layout

A watch box. The page is the box's outer leather, with 14px padding and
12px gaps. A 1.5rem brushed-gold spine rail runs down the left with a
polished screw head at each end. The bar is a stitched leather lid strip
that sits on a brushed-gold hinge rail. Content sits in a recessed,
inset-shadowed tray with rounded corners. The status strip is a
brushed-gold nameplate with engraved uppercase lettering; state text on
it switches to dark inks. Below 720px the rail drops away (core default).

## Typography

Nothing is vendored. Display: `Didot, "Bodoni 72", "Bodoni MT",
"Libre Bodoni", Georgia, serif`, set in tracked uppercase for headings,
brand, panel titles, stat values and prices. UI: `Optima, Candara,
"Segoe UI", …, sans-serif`, the engraved-sans of luxury packaging. On
Linux without these faces you get Georgia and the system sans; the
tracking and foil colour carry the look.

## Contrast honesty

All lint pairs pass. `--text` `#ede4d1` on `--surface` `#151311` is
above 14:1; `--muted` `#b0a184` reaches 4.5:1 on both surfaces; dark
`#1b1408` on every polished and brushed gold stop is above 7:1. The
stitch thread is decorative and is never behind text. For that reason
the bar's stitch is laid in the `.app-bar` rule, not in `--app-bar-bg`.

## Tell-tales of an inauthentic result

- Brown or grey leather, or a flat black with no grain: it's become a
  generic dark theme.
- Gold gradients without a dark horizon band, or the same gold finish
  on rails and buttons: polished and brushed are no longer distinct.
- Stitching on buttons or inputs, or stitches crossing text.
- Glowing gold text, gradient-clipped headings, filigree or rivets.
  That drifts towards casino or steampunk.
- Sentence-case sans headings: the foil-struck voice is gone.
- Light text on the brushed-gold status plate.

## Print

Leather, grain and shadows are dropped to white in a small `@media print`
block.

## Reference status

13 images in `references/tokie/`, all from Wikimedia Commons, covering
leather grain, saddle stitching, brushed and polished gold, gold-foil
debossing on black leather, gilt tooling and leather case hardware. No
luxury *software* UI was found under a usable licence, so the component
mapping is an interpretation of physical objects. See RESEARCH.md.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
