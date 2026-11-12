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
2. **Leather is matte and black.** Surfaces are neutral near-black
   (`#0b0a09` to `#1e1d1b`, red and blue within 3 of each other) with a
   visible pebble grain. No gloss, no brown tint; warmth lives only in
   the gold. A selected row or list item, an edited table cell and the
   bulk-selection bar are a neutral lift with a thin gold lead rule, not
   an amber fill.
3. **Stitching is on the edge, never under text.** The saddle stitch runs
   7px inside the edge of panels, cards, dialogs, drawers and the bar.
   Small elements (buttons, inputs, badges, transport, list cards) are
   not stitched. Content keeps 8px or more clear of it at every tier:
   `--panel-pad` / `--card-pad` start at the 9.5px stitch strip plus
   0.75rem / 0.6rem, and desktop windows pad their body inside it.
4. **Gold foil, not gold paint.** Type on leather is flat gold with a
   deboss shadow (dark above, faint light below), tracked uppercase in a
   Didone serif (h1 to h3, brand, titles). The foil is a worn, greyed
   old-gold (`#cdb47a`), softer than the polished hardware. No gradient
   text, no glow.
5. **Polished gold has a horizon.** Mirror gold is a hard gradient with
   a dark band just above the middle. Without that band it reads as
   yellow plastic.
6. **Restraint.** One gold, one thread colour, no ornament beyond the
   stitch, the gilt fillets and the two rail screws.

## Signature details

- Pebble grain is an SVG `feTurbulence` + `feDiffuseLighting` tile
  (200px, data-URI) under a 93%-opaque black wash. There are no bitmaps.
- The saddle stitch (`--tokie-stitch`) is twelve background layers: four
  runs of slanted champagne thread beads (a 60° repeating gradient in a
  3px strip, 6px pitch: about 2.4px of 72% champagne thread, a 0.8px dark
  shade on one side so the slant reads, then dark channel, like a
  pricking iron sets them), four corner arcs that turn the stitch on a 5px
  radius, and four creased grooves (75% black) with a faint lit lip. It
  costs no pseudo-elements, so any surface can wear it. On phones
  (≤480px) it drops to the four bead runs, and every SVG-filter tile
  (pebble grain, brushed hairlines) is switched off: flat leather and
  gradient-only gold keep scrolling within the frame budget on a
  throttled phone.
- The gold is aged brass, not new jewellery: brushed runs
  `#c9b072 → #b39650 → #a68a48`, and polished highlights cap at
  `#f0d68c` above a `#7a5718` horizon.
- Brushed gold is anisotropic noise (`baseFrequency='0.002 0.9'`),
  stretched into horizontal hairlines over a satin vertical gradient. The
  spine rail uses the same noise rotated so its hairlines run vertically.
- Panel and dialog titles are foil caps above a double gilt fillet (1px
  gold, 2px gap, 1px darker gold), the way a binder's roll lays a line.
  It is drawn through `--panel-header-bg` / `--modal-header-bg`.
- Slider grooves are drawn inside the input's content box (core grows the
  input to `--tap-min` and hides its border): a gold upper edge, a black
  channel and a faint lit lower lip; vertical sliders turn it on its side.
- Switch thumbs are brushed-gold domes when off and polished gold when on.
  No third metal.
- Buttons: the default is a leather key with a gold bezel; primary is
  polished gold with engraved dark text; danger and success are enamelled
  oxblood and bottle-green leather that keep the gold bezel. Toggle
  buttons speak the same voice (tracked caps; sentence case up to 900px,
  where toggle rows are packed tight) and turn polished gold when on; a danger toggle turns oxblood enamel.
- Readouts are black lacquer dials with applied gold Didone numerals and
  a thin gold chapter ring; padding `max(6px, .4em) max(8px, .6em)` keeps
  the numerals 4px+ off the ring. Knobs are polished watch crowns with a fluted
  edge.
- Alerts are debossed into the leather like inputs; alerts and toasts
  carry a 3px state-coloured lead rule on their leading edge; their other
  three sides are a dim `#3a3226` hairline so the rule reads as a state. Folder
  rails (`.nav-rail`) are a raised leather flap edged in dark gold.
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

## v5 layout

Tiers: mobile ≤480px, tablet 481–900px, desktop 901–1800px, XL ≥1801px (the shell is capped at 1800px and centred, with gutter art beside it).

- **Phone (≤480) and tablet (481–900):** one column. The brushed-gold spine rail is packed away (the rail opts in through `--app-rail-empty-display`, which outranks core's per-tier rail token, so the theme switches it off up to 900px). Phones get a slightly tighter box rim and lid padding. Main padding is set per tier (`--app-main-padding-mobile` / `-tablet`).
- **XL gutters (≥1801):** the lid lining, quilted: a diamond tuft in faint champagne thread with a dark brass button at every crossing, on the same black leather. Still.

## Typography

Display: `Didot, "Bodoni 72", "Bodoni MT", "Bodoni Moda", "Libre
Bodoni", "Playfair Display", "Linux Libertine", Georgia, "Liberation
Serif", …, serif`, set in tracked uppercase for headings, brand, panel
titles, stat values and prices. Bodoni Moda (OFL, Latin subset, wght
400–700 and opsz 6–96 axes) is vendored as
`assets/fonts/BodoniModa-Variable.woff2`; its optical-size axis follows
the font size, so h3 and panel titles get sturdier hairlines than h1
instead of losing their crossbars. h3, panel and dialog titles are set at
weight 500; badges inside them use the UI sans at 600. UI: `Optima, "Optima nova", "URW
Classico", "Linux Biolinum", Candara, "Segoe UI", "Noto
Sans", Lato, "Open Sans", …, sans-serif`, the engraved-sans of luxury
packaging. On a bare Linux box the UI falls to Noto Sans or DejaVu;
the vendored Bodoni Moda keeps the Didone. Inside desktop windows the tabs drop to sentence case
so four fit on one row.

## Contrast honesty

All lint pairs pass. `--text` `#ede4d1` on `--surface` `#151311` is
above 14:1; `--muted` `#b0a184` reaches 4.5:1 on both surfaces; dark
`#1b1408` is above 7:1 on the polished highlights and the light brushed
stops and 5.5:1 on the darkest brushed stop (`#a68a48`); the polished
horizon band is decorative and sits away from the text's centre. The
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

## Icons

`themes/tokie/icons.svg` redraws all 178 core icons as fine gold-tooling
line glyphs, like a binder's fillet laid into leather.

- 24×24 grid, line only, `stroke="currentColor"` (gold foil on leather, dark
  engraved ink on polished gold): 1.4 hairline, round caps and joins.
  The theme colours icons in the foil on leather; inside controls, gold
  plates and state-coloured text they keep `currentColor`.
- True curves and circles. Corners keep small radii.
- Dots are small solid round stamps. Fills only for carets, play and small
  status marks.
- No deboss shadow or second colour. The glyph stays one ink so it follows every state.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
