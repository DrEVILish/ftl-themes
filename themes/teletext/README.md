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

- The page number ("P100") opens the header row in plain white, followed
  by a small block-mosaic mark before the brand (lower-half, full and
  upper-half cells in yellow over a hard blue offset shadow, as the
  Ceefax wordmark sat on its page), as on
  every real page; the nav links that follow each take a different
  broadcast colour (cyan / green / yellow / magenta), like a page's index
  lines, on both `.nav-item` links and the demo `.menubar`; the current
  item is a red block with black text. A yellow clock (`16:24/41`) closes
  the row, as on every real header (hidden on phones). The rest of the
  row is text only: the theme select and bar buttons have no edge and
  invert to a cyan cell on hover, the search key hint has a blue edge,
  and on phones the tools stay on one row with no key hint.
- `h1` is the section banner: a full-width blue band with the headline
  in yellow at true double height: body cell size with
  `transform: scaleY(2)`, so the glyphs keep the body column advance and
  read tall and narrow, as the SAA5050's double-height row did. It opens
  with a strip of yellow sextant mosaic cells (U+1FB00 block graphics),
  the Ceefax wordmark's block lettering at double height. A plain `h2`
  (no class) in page flow is a body-size strapline band: blue with
  yellow ink first, then green, cyan and magenta with black ink by
  position; `h3` stays cyan ink.
- Panel titles are full-width colour bands (blue / green / magenta /
  yellow by position, each with the text colour it needs); cards carry a
  thick band of the same colour on top. Nothing draws a white line: table
  rules and hairlines are gone, as on the real service, and every edge
  core draws from `--border` (toolbars, drop zones, settings rows, kbd
  keys, fieldsets, progress, `.divide-y` rules) is a blue cell edge. White is kept for the
  focus ring alone.
- Tabs are coloured words; the selected one is white on a blue band.
- **Fastext:** the status strip ends with a blue strapline row (yellow
  *Teletext: the world at your fingertips*) and then the four key words
  on a row of their own — red *Headlines*, green *Sport*, yellow
  *Weather*, cyan *TV Guide* — in one monospaced string coloured by a
  hard-stopped gradient (25/50/75%) clipped to the text. Both rows span
  the whole strip, as they spanned the screen: the strip is a size
  container, the cell size follows it (`100cqi / 24.5`, capped at
  1.5rem), each key word starts a quarter (tab stops at `25cqi`, the
  10-cell columns) and the strapline is centred in its band. On phones
  (≤480px) the keys shorten to *News / Sport / Weather / TV* so each sits
  clear in its quarter.
- **No tints, no circles.** Badges are black cells with colour ink; the
  notification count is a square red cell with black ink and no ring;
  transparent buttons hover to a blue cell and press to a cyan cell with
  black ink, never an accent wash; the
  bulk bar and skeletons are flat blue blocks; avatars are flat palette
  cells; edited cells, poll rows, invalid inputs and sparklines carry no
  wash. The presence cell is a small square outside the avatar's corner,
  so the initials (at the 0.875rem cell) stay clear. Switches, slider thumbs, icon buttons, avatars, presence dots,
  status dots, lamps, carousel dots, the display-properties monitor and
  the spinner/indicator rings (including a table cell's inline "saving"
  ring) are square; the rings step round a quarter at a time
  (`steps(4)`) on a blue track, and a saving cell keeps full-brightness
  ink (`--pending-opacity: 1`). Checkboxes and radios are drawn cells
  (black, cyan edge; checked fills cyan with a black stepped tick, or a
  black centre for a radio), not the browser's grey dark-scheme box;
  forced-colours mode keeps the native control.
- **Charts in flat cells.** The heatmap and its scale legend step through
  black / blue / green / cyan on hard switches (no oklab ramp), cells
  square and touching like mosaic blocks; line charts have no area fill,
  aliased (`crispEdges`) lines with square joins and small aliased points.
  The donut stays a curved ring: a data-vis exception, in palette
  colours. Inactive desktop windows carry
  a blue title band (active ones magenta) with no desaturating filter.
  Disabled buttons are black with grey ink and edge, not a dimmed fill.
- **One cell size:** badges, stat labels and trends, table heads, small
  buttons, field hints, status labels, list meta and thread times never
  drop under 0.875rem, so small print sits at most a step under body. At
  1600px and wider the root steps to 20px, the 20px cell where each
  Bedstead pixel is exactly two device pixels (chunky 2px stems); below
  that the 16px base is kept, since 20px wraps the 1280 bar and stat
  rows, and on phones 16px is the 40-column row.
- **Colour, not white outlines:** inputs have a cyan edge; menus,
  popovers, lists and logs a blue one. Secondary lines (list meta, stat
  labels, `.text-muted` text, ledes, breadcrumbs, the status strip and
  hero copy) are cyan, as on an index page; nav links are white and form
  labels yellow, as a listings page labels its rows. Grey is left only
  for true hint text and the disabled state.
- Selected/active rows invert to a solid colour fill with black text
  (`--row-selected-bg`), not a tint or outline — real teletext has no
  concept of a translucent highlight.

## Icons

`themes/teletext/icons.svg` redraws the original core icon subset (178
glyphs plus `sun-moon`); the newer core icons (about 840 more) fall back
to core's outline sprite, so a page mixing the two shows both styles as solid colour-cell block graphics, like the real
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
- **Cut-outs:** `file`, `file-zip`, `mouse`, `message`,
  `message-circle`, `cash` and `map` are single `fill-rule="evenodd"`
  paths with their detail cut out, so they no longer read as plain
  blocks.
- **Second tone:** a dimmed cell (`fill-opacity` 0.3–0.5) marks secondary
  detail such as map folds, a pie slice or disc glare. A dim cell must
  never sit on top of a solid one, because it would vanish. Where a mark
  sits inside a solid block (compass, layout, terminal, globe, file-check,
  file-code, file-text) it is cut out with `fill-rule="evenodd"` instead.
  A few original glyphs (coin and others) still stack them, so their
  inner mark is invisible.
- **Lettering:** the `PDF`/`PNG` labels are 3×5-cell block letters, not
  text.
- **Palette:** `currentColor` only.

## v5 layout

Tiers: mobile ≤480px, tablet 481–900px, desktop 901–1800px, XL ≥1801px (the shell is capped at 1800px and centred, with gutter art beside it).

Core's tiers do the work; the theme's one breakpoint (≤480px) hides the header clock.

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

`--font` and `--font-mono` are **Bedstead**, vendored (`assets/fonts/Bedstead.woff2`, CC0 — see `assets/fonts/NOTICE.md`): Ben Harris's outline recreation of the SAA5050 character generator, so the blocky, stepped glyphs in all three captures are the real shapes. The font has one weight and `font-synthesis: none` stops the browser smearing a faux bold over it, as teletext had no bold. The subset keeps the teletext sextant mosaics (U+1FB00–1FBAF) for block graphics.

## Contrast honesty

- **Palette is exact; the deviations are two.** `--muted` `#b3b3b3` (10.02:1 on black) is not in the 8-colour set and exists only because the design system needs a secondary-text role; `--hairline` `#4d4d4d` is a rule colour, not text.
- **White-on-red lifted to black-on-red.** Real teletext printed white on red, which is 4.0:1, under the 4.5:1 floor. `--on-danger` and the active header nav item are black on `#ff0000` (5.25:1), still inside the 8-colour set. Black on cyan 16.75:1, on green 15.30:1.
- **On black:** cyan 16.75:1, yellow 19.56:1, magenta `#ff00ff` 6.70:1, red 5.25:1, green 15.30:1, white 21:1. So all eight clear AA on black; red is the tightest.
- In the ARTE capture, red text sits on a white ground and white on blue; the theme is black-ground only, so those pairings (red on white ~4:1) are not reproduced.

## Reference status

`references/teletext/` holds 8 captures plus `RESEARCH.md`, all pure text screens with no people:

- `ceefax-p100-index.webp` — the Ceefax P100 index: the bottom two rows span the full width, a centred strapline in its band over the four-colour Fastext row (red/green/yellow/cyan). Backs the full-width Fastext strip and the mosaic mark.
- `ceefax-p324-football-table.png` — a football table: rows separated by colour and blank lines, at most a red rule, no white boxes. Backs the blue edges and the absence of white hairlines.
- `ceefax-p696-bbc1-listings.webp` — BBC1 listings: yellow times, white titles, cyan descriptions. Backs the cyan meta and the yellow labels.
- `ceefax-p299-newsreel.png` — yellow mosaic CEEFAX blocks with a drop shadow on a blue frame. Backs the mosaic brand mark and its hard blue shadow.
- `teletext-arte-page100.png` — an ARTE page 100: page-number/clock header row, blue-band panels, a blue footer bar. Backs the `P100` header.
- `teletext-ceefax-football-index.jpg` — a Ceefax football index: cyan headline list, double-height lead lines and a blue title band.
- `teletext-screen-teletexnews.png` — a news page (300): double-height headlines and an index list.
- `football-nostalgia-print.webp` — mosaic wordmarks and centred multicolour paragraphs.
