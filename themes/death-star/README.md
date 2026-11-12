# Death Star Terminal

> Black console zones framed by bright white inlay outlines, solid red header bands, a pale tile row and square multicolour push-button chips.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

An Imperial control console as the reference diorama
(`references/death-star/il_fullxfull.7108820316_cpn8.webp`) builds it: true
black zones, each framed by a bright white inlay outline, solid red bands
across the middle, a row of pale grey tiles along the top and small square
push-buttons in red, blue, yellow, white and green.

## Core values

1. **One white outline box per zone.** `.panel`, `.card`, `.modal` and
   `.transport` draw a 3px `#e6e6e6` outline with a small 4px inlay corner;
   a surface nested in another steps down to 2px. Inner padding stays black.
2. **Red is a band, not a tint.** Top-level panel and modal headers, the
   bulk-action bar and selected rows are solid brick red `#c4352a` (sampled
   from the diorama's bands) with white text.
3. **Everything else is square.** Buttons, inputs, switches, avatars,
   badges, lamps, alerts, toasts, the slider and fader caps and carousel
   dots, lamps, the connection lamp and table status dots have zero radius
   (native checkboxes keep the UA shape; core's avatar presence dot stays
   round because its shape encodes status). Buttons have no border; buttons
   and inputs sit one visible step above the panel black, and inputs carry a
   2px `#6a6a6a` inlay outline (3.7:1 on black) so fields read as sub-boxes.
4. **True black, not near-black.** `--bg: #000`.

## Signature details

- **Tile row.** The app bar carries a 2.25rem-tall row of pale green-grey
  `#d7e4df` tiles in bays of four, as on the diorama: near-portrait 2rem
  blocks with 5px black seams, whole bays only (`background-repeat: space`),
  inset 1rem from the edges, above the bar content and its 3px red rule.
- **Red header bands.** `--panel-header-bg`/`--modal-header-bg` are the
  accent with white text (5.4:1); muted and success text on the band are
  re-pointed to `#fff0f0` and `#c8ffd8`.
- **Push-button chips.** Badges are solid square chips: default pale tile
  grey with black text, accent red with white, danger/success/warning solid
  with black. On a red header the accent chip turns black.
- **Focus** is a white outline (`--focus: #fff`): 16:1 on black and 5.4:1
  on the red bands, bulk bar and selected rows, where red focus vanished.
- **White labelling.** The nav brand, table header text, GO label and
  desktop icon glyphs are white, as the diorama's linework; red stays a
  fill or rule (the table head keeps its red rule, GO its red frame).
  `--accent-text` is kept for links, readouts and text buttons.
- **Avatars** are pale `#d7e4df` chips with black caps; an avatar with a
  user colour is a solid chip in that colour with black or white caps
  (computed from its lightness), never a tint.
- **Disabled buttons** are an unlit `#1c1c1c` key with `#777` text, not a
  dimmed red one.
- **Edit states** in tables keep only their non-colour signal (leading
  bar, tick, ring): no dirty, saved, editing or error tint.
- **Lamps** are square, borderless and carry a `0 0 10px` glow in their
  own state colour — the only `box-shadow` the theme sets.
- **Selected rows and options** fill solid red with white text.
- **Alerts and toasts** are a dark block with a 4px solid colour block at
  the leading edge, no frame.
- **Floating menus** (dropdown, popover, context menu) are `#161616` with
  a 2px white outline, so an open menu reads as a raised surface.
- **Slider track** is `#8a8a8a` linework (5.9:1 on black) with an 18px
  square white cap; core's transparent border and content-box clip keep the
  24px/44px hit area.
- **Inactive windows** take a neutral `#1c1c1c` title band with no filter,
  the own-message bubble is the same neutral step, and chart/sparkline
  areas carry no fill: red never appears as a muddy tint.
- **Switches** are square: grey `#5a5a5a` track and pale thumb off, red
  track with white thumb on.

## Layout

The bar and status strip are black; the bar has the tile row on top and a
3px red rule beneath. No rail.

## v5 layout

- **Tiers.** No rail, so phone (≤480px) and tablet (481–900px) use core's
  one-column shell as is.
- **Nesting.** A surface inside another draws a 2px outline, and a nested
  panel's header is a slim red block at its left edge instead of a second
  full red band. Fields sit one step above `--surface-2`.
- **XL gutter art.** More bulkhead: a very faint lattice, a short four-tile
  row, a few unlit `#1a1a1a` control blocks and one cluster of five small
  push-button squares (blue matched to the reference paint, `#5281b8`). Still.

## Tell-tales of an inauthentic result

- A panel or card without its white outline, or a grey/dim outline.
- Red as a tint or thin rule where the reference has a solid band.
- A rounded pill or circle (switch, avatar, icon button, badge).
- A near-black (`#0a0a0a`-ish) page background instead of true `#000`.
- Graph-paper lattice behind text.

## Don'ts

- **No lattice behind content**; the faint grid lives only in the XL gutter.
- **No blue blocks**; blue appears only as one tiny push-button in the gutter art.
- **No Star Wars display lettering** (see Typography).
- **No red as body text** — `--accent` fails as text on black; use `--accent-text`.
- **No shadows** other than the lamp glow.

## Icons

`icons.svg` redraws the full core set (178/178); `--icon-stroke-width: 1.5` thins the extended fallback glyphs toward it. Rules: 24 grid, 1px hairline
stroke (overrides core's 2px), `square` caps and `miter` joins, sharp
right-angled rects, true circles only where the concept is round. Minimal
marks per glyph; a few sit inside a hexagonal bulkhead frame (home, check,
play, player-play, bell, user) or a square panel (close, menu, download, pause). Line only: nothing is filled, marker dots are
r1.1 rings, colour is always `currentColor`.

## Typography

Headings (h1–h3), panel and modal headers and the nav brand use
**Michroma** (Vernon Adams, SIL OFL 1.1, already vendored as
`assets/fonts/Michroma-Regular.woff2`) in uppercase with 0.08em tracking:
the squared, extended labelling of a 1970s console. Michroma ships one
weight, so these stay at 400, with line-height 1.25 and a 0.35em bottom margin so
the tall caps clear the text below. Body text is a neutral sans
(`"Helvetica Neue", Helvetica, Arial, "Liberation Sans", "Nimbus Sans",
sans-serif`) and `--font-mono` is **Share Tech Mono** (SIL OFL, vendored
as `assets/fonts/ShareTechMono-Regular.woff2`), squared console figures,
then `Consolas, monospace`. `h1` tracks tighter (0.03em) so the widest
heading does not outweigh the nearly text-free console. Code inside a
heading keeps its case.

## Contrast honesty

- **Accent red fails as text.** `--accent` `#c4352a` is 3.89:1 on black; white on it is 5.4:1, so red is safe only as a fill/lamp/rule. Red as text — links, the active tab, accent badges, readouts, code keywords and the secondary button — uses `--accent-text` `#ff6a5c` (7.47:1 on black).
- **Muted lifted:** `#6a6a6a` (3.8:1) to `#777777`, then to `#888888` (5.92:1 on black, 4.81:1 on the `#1c1c1c` current-time schedule row). On the red header block `--muted` is re-pointed to `#fff0f0` (4.88:1) and `--success-text` to `#c8ffd8` (4.82:1).
- **Nav items** `#8a8a8a` (6.08:1 on black), a hair above `--muted`.
- `--text` `#e6e6e6` is 16.83:1. Semantic fills (`#ff3b3b`, muted phosphor green `#5cc872` from the reference readout, `#ffcf2f`) are 5.9–15.7:1 on black with black `--on-*` text.
- White on the red band and on selected rows is 5.4:1. Buttons (`#1c1c1c`) and menus (`#161616`) are distinct from the `#050505` panel fill.
- `.pattern-nav a[aria-current="page"]` is forced to `--on-accent`: the page pairs `--accent-text` with the accent fill (1.92:1 here).
- The red `#c4352a` is sampled from the diorama's bands (`#cf3a2f`, `#c33427`, `#bf352b`).

## Reference status

`references/death-star/` has 4 captures plus `RESEARCH.md`: `death-star-superlaser-still.jpeg` and `death-star-station-still.jpeg` (film stills), `death-star-executor-still.jpeg` (a further still, not described in `RESEARCH.md`) and `il_fullxfull.7108820316_cpn8.webp` (a builder's isolated console diorama with red/black panels, indicator dots and a green readout, which `RESEARCH.md` credits as the console reference). No isolated Imperial console-screen capture exists; the layout follows the diorama: white outline boxes, red bands, tile row and colour push-buttons.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
