# NERV Terminal

> Industrial military-alert styling — deep black, hazard orange, signal red.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

A command-bunker terminal under permanent alert status: black steel,
stencilled orange warnings, and signal red reserved for the moment something
is actually wrong.

## Core values

1. **Orange is "operational alert" — always on, never urgent.** EVA's
   amber-orange (`#ff8a00`, 8.6:1 on the black, well clear of signal red) is the
   accent, the border colour, the heading colour. It marks that this
   terminal is a war-room fixture, not a calm state.
2. **Signal red (`#e0001b`) is reserved for danger alone**, and gets the one decorative
   flourish in the theme: diagonal hazard stripes on destructive actions
   and as the 8px tape band across the top of danger alerts.
3. **Sharp, condensed, uppercase.** `--radius: 0`, carried to badges,
   chips, switches, avatars, slider thumbs, lamps and carousel dots
   (radios stay round). Page titles and section heads (`h1`, `h2` outside
   frame headers) take the title-card face: `"Matisse EB"` named first,
   then the vendored Noto Serif Display instanced at width 62.5 / weight
   900, a compressed heavy serif, set with no tracking. `h3`, buttons, frame headers, tabs, table
   heads, badges, nav items, top-bar menus and KPI numerals in the vendored Antonio
   Bold, a tight condensed bold standing in for NERV's compressed readout
   sans. Labels, badges, filter chips, toggle and segmented buttons, nav
   items and the app brand are uppercase; Antonio is never set mixed-case,
   and its small readouts (table heads, badges) are floored at 0.8rem and
   tracked 0.08em wide. Body text stays in a plain Helvetica/Arial stack
   for legibility; labels and secondary readouts glow amber phosphor
   (`--muted: #d9a066`, 8.9:1) as on the EVA terminal screens.
4. **Thick rules.** 2–3px borders and bars, not hairlines — a bunker's
   markings are painted, not printed.

## Signature details

- Every panel and modal header carries a black flat-top hexagon (1.1em)
  before its label, the MAGI hex brought into the shell at every width;
  desktop windows whose title already leads with an app icon skip it.
  Page titles (`.app-main h1`) take the same hexagon as a bullet.
- The app bar's 3px orange rule is doubled by a 2px signal-red rule below
  a black gap: NERV's twin warning rule.
- Danger buttons alone get a `repeating-linear-gradient(135deg, ...)`
  hazard-stripe fill instead of a flat color. Danger alerts are the EVA
  emergency card: a 2px red frame on a red-black ground, an 8px hazard-tape
  band across the top and the message stencilled uppercase in Antonio —
  the theme's single decorative flourish, reserved for the danger state.
- The active-row marker is signal red (`--danger`, about 4:1 on the
  black) even though every other structural accent in the theme is
  orange — the one place danger's color, not orange, gets to mark something.
- Panel, modal and window headers reverse out like the table head: a solid
  orange strip with black, uppercase condensed text — the NERV warning-box
  label. Caption buttons on that strip are a stamped cluster: equal 1.4em
  squares in a 2px frame of the header ink (black on orange, orange on
  an inactive window's unlit strip). Cards stay plain frames.
- Carousel dots and arrows are square; the arrows are outlined in 2px
  orange like the buttons. Toolbars sit on the bunker black over a 2px
  orange rule.
- Headings are condensed uppercase set tight (`0` for the serif titles,
  `0.04em` for Antonio `h3`), not airy wide tracking, with a small
  `0.25em` trailing margin.
- Chart series step in lightness as well as hue: amber, phosphor green,
  grey, signal red, deep orange, pale amber.
- Inactive windows dim to an unlit dark strip with an orange label rather
  than a faded orange.
- Confirm (success) buttons are outlined in phosphor green, not filled:
  green stays a status signal inside an orange-forward palette.

## Layout

A black bar and status strip (and the desktop taskbar) both edged in a
3px orange rule — the
terminal's own frame — with the content area reading as the screen set
into that frame.

## Tell-tales of an inauthentic result

- Orange used sparingly, as an accent among others → this palette runs
  orange-forward everywhere.
- Hazard stripes anywhere other than a destructive action or danger alert.
- Thin, quiet borders — NERV's markings are bold.
- Wide, airy tracked headings → NERV type is condensed and tight.

## Note on fonts

NERV's title cards use Matisse EB (proprietary), named first in
`--nerv-title`; the vendored stand-in is Noto Serif Display instanced at
wdth 62.5 / wght 900 and subset to Latin
(`assets/fonts/NotoSerifDisplay-CondensedBlack.woff2`, SIL OFL 1.1), with
Liberation Serif behind it. Readouts use a compressed Helvetica-style
sans, for which the theme vendors Antonio Bold (SIL OFL 1.1). Mono is
`Consolas, "Liberation Mono", "Courier New", monospace`.

## v5 layout

Tiers (core): mobile ≤480px, tablet 481–900px, desktop 901–1800px, XL ≥1801px (shell capped at 1800px, centred). No rail. Phone and tablet use the core two-line bar. A panel nested in another box drops to a 1px dim-orange rule (`#a85400`, 3.8:1), so stacked boxes read as compartments rather than three full-strength frames. On XL the gutters show the MAGI hex field: a tiled honeycomb of flat-top hexagon cells in dim hazard orange (about 1.4:1 against the black, deliberately quiet).

## Icons

`icons.svg` draws the core set as emergency-terminal glyphs (no NERV or studio marks).

- **Grid and weight.** 24 grid, heavy 2.4px line, square caps, mitred joins, hard corners (radius 0).
- **Geometry.** Every circle is a flat-top hexagon (the MAGI hex motif); curves are rebuilt as angular runs; silhouettes are solid fills; marker dots are solid squares.
- **Condensed.** Each glyph is squeezed to 86% width by a wider `viewBox` with `preserveAspectRatio="none"`, like condensed stencil type. This also makes vertical strokes 0.86x the width of horizontal ones, which is not visible at 2.4px.
- Only the core set is redrawn: extended-set icons (coins, map pins, clocks, circle carets) keep their round core geometry.
- Generated from one shared 24-grid geometry, so every core-set id (178/178) is drawn; everything uses `currentColor`, so icons follow text, accent and selected states (and every variant) with no hard-coded colour.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
