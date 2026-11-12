# TRON

> Electric cyan line-grid on black — glowing, angular edges.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

**The Grid**: a black void inscribed with glowing cyan circuitry, hard
angular geometry, and light used as a construction material. Everything
looks *drawn in light* rather than painted.

## Core values

1. **Light is the material.** Edges glow; surfaces stay near-black. A
   filled, non-glowing surface reads as off.
2. **Cut corners, never rounded ones.** `--radius: 0` plus `clip-path`
   corner cuts on buttons and panels, with the diagonal drawn in light so the
   frame never breaks. Switches, slider thumbs, chips, avatars, icon buttons,
   comment pins, status dots, lamps, spinners, carousel dots and checkboxes
   are square too (radios are a square turned to a diamond). The chamfer is
   the signature.
3. **Cyan builds, orange opposes.** `--accent` cyan is the system;
   `--accent-2` orange is the adversary — reserved for danger and
   warning. Never use orange decoratively.
4. **The grid is always present.** A 2.5rem cyan line-grid at 6% underlies
   everything.
5. **Wide tracking, uppercase.** Headings and the brand in Michroma (a wide
   squared face) at `0.18em` — display type from a title sequence. On
   phones (≤480px) tracking drops to `0.08em` and h1/h2 shrink so a heading
   doesn't break one word per line. Code inside a heading stays literal (no
   caps, no tracking). Body in Titillium Web; readouts in Share Tech Mono.

## Signature details

- Buttons, panels, cards, modals, menus, toggle buttons, segmented
  controls, alerts, toasts and framed lists share one chamfer (18px; 10px
  for buttons, toggles, segmented controls, framed lists and nested surfaces; 7px for small buttons,
  alerts and toasts). Where `corner-shape: bevel` is supported it is a real
  bevelled border; elsewhere a `clip-path` polygon with two background
  layers tracing each diagonal in the component's border colour.
- Surfaces are light-lines: a second 1px inner ring makes the edge read
  2px lit, with an inner glow and, above phone width, a 10px outer bloom.
  The bloom shows only with `corner-shape`, because `clip-path` cuts it
  away. Phones keep the clip-path chamfer and the 1px inner ring but drop
  the inner glow and the readout/table-head text glow, since glow on every
  surface drops frames while scrolling on a mid-range phone. Keyboard focus is drawn inside the cut: a 2px
  outline inset 5px plus an inner bloom.
- Alerts and toasts carry a lit 0.2rem bar down the start edge in their
  status colour.
- Active and destructive states trace rather than fill: danger and success
  buttons, toggles (a danger toggle that is on included), active chips and
  selected labels are outlined in their colour over a faint tint.
- Checkboxes are lit square frames holding a square node when checked.
  Avatars are a 1px lit frame over a faint tint; skeleton loaders are
  traced outlines, not filled slabs.
- The slider track (and the vertical fader's column) is a 3px lit line
  inside a --tap-min hit area, with a white-hot square thumb; the h1
  glow has a white-hot core under the cyan.
- Numeric readouts (`.stat-value`) glow faintly in Share Tech Mono.
- Your own chat messages are framed in white light. Charts use one orange
  (warning) and white for the fifth series, so no two series share a colour.
- The top bar casts a 12px cyan bloom downward.
- Selected rows and list/nav items carry a cyan marker. Only the
  playing/now table row (`.is-current`, `aria-current="time"`) is marked
  *orange* — the one place the two colours meet, to separate "selected"
  from "playing".

## Layout

The shell becomes **an enclosure**: 0.75rem padding all round, a thin
0.35rem lit conduit down the left edge (the rail, drawn as a vertical light
gradient with a bloom rather than as a panel), and a glowing bar above.

## v5 layout

Tiers: mobile ≤480px, tablet 481–900px, desktop 901–1800px, XL ≥1801px (the shell is capped at 1800px and centred, with gutter art beside it).

- **Phone (≤480) and tablet (481–900):** core's one-column shell; the 0.35rem lit conduit rail is dropped.
- **Nested surfaces:** a panel or card inside another surface takes the smaller 10px bevel. A surface that holds an in-flow `.anchor` menu keeps square corners, because `clip-path` would cut the menu off at its edge (top-layer popovers escape either way).
- **XL gutters (≥1801):** light-cycle trails on the Grid floor: thin right-angled jetwalls in cyan and one rival orange over the page's own grid. Still.
- **Desktop windows:** label tracking tightens to `0.04em` inside a window so a four-tab dialog keeps its tabs on one row and its footer inside the fixed-height window.

## Known compromise

Eurostile, the reference face, is not web-available. Stat labels and table
heads use Titillium at 600 rather than Michroma, whose width overflows
narrow table columns at label size. Michroma (vendored,
SIL OFL) stands in for the extended display cut; Titillium Web (vendored)
carries body text.

On phones, and in browsers without `corner-shape`, chamfered surfaces can't cast an outer
glow: `clip-path` clips box-shadow and any filter on the same element, so
only the inset glow shows there.

## Tell-tales of an inauthentic result

- Rounded corners → the chamfer language is the whole identity.
- Orange used for emphasis rather than danger → the cyan/orange opposition
  stops meaning anything.
- Solid bright surfaces → light should trace edges, not fill shapes.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.

## Icons

`icons.svg` redraws the 178 original core icons as lines drawn in light.
Icons added to core later fall back to the generic set, drawn with square
caps and mitred joins so they sit closer to the redrawn ones:

- 24×24 grid, 2px stroke, square caps, mitred joins.
- Every box is chamfered top-left and bottom-right like the theme's
  clip-path, and every circle becomes an octagon. Curves are rebuilt as
  45° runs (bell, cloud, lock shackle, wifi).
- Outline only, with no filled surfaces. The only solids are small marks:
  square nodes, carets and level indicators.
- `currentColor` everywhere, with no hard-coded cyan or orange, so state
  colours still apply.
