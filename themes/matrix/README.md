# The Matrix

> Green phosphor on black — monospace terminal cascade.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

A **phosphor terminal** as filmed: monospace everything, black field,
green text with a faint bloom, and the sense that you are reading a machine
directly rather than an interface built for you.

## Core values

1. **Monospace is non-negotiable.** Every element, not just values.
2. **Green is the only colour with a job.** Semantic red exists for genuine
   errors and nothing else. Introducing a second decorative hue breaks the
   single-phosphor illusion. Warning is the white-hot head glyph `#e8ffe0`,
   `--accent-2` is a lighter green `#7dff9a`, and the six chart series are
   brightness steps of the one green.
3. **Bloom, not glow.** A 2px text-shadow across all text imitates
   phosphor persistence. It is deliberately subtle — a strong glow reads as
   neon, which is a different aesthetic entirely.
4. **Outline over fill.** Base controls are a green rule on black (black,
   not transparent, so the rain never falls through a label). Only semantic
   variants take a fill, so a delete button still reads as dangerous.
5. **Uppercase headings, tracked.** Terminal banner conventions.
6. **Hard rectangles.** Badges, filter chips, switches, slider thumbs,
   icon buttons, avatars, carousel arrows and dots, and checkboxes are
   square terminal cells (`--radius: 0`), never capsules or discs (radios
   stay round).

## Signature details

- **The digital rain**: real glyph columns filling the frame top to bottom,
  all mirrored: about two thirds katakana-like stroke glyphs drawn as SVG
  paths, the rest digits and the film's few symbols (`Z : = * " < > . + |`),
  no Latin capitals. Columns sit at a 13-15px pitch (about one glyph's gap,
  packed like the film's wall), each carrying four to six streaks of 10-22
  glyphs whose opacity ramps from 1.0 behind the head to about 0.35 at the
  tail, ending in a white-hot `#f0fff0` head whose glow is baked in as two
  tight translucent strokes (a 2.5px `#b8ffc8` halo at 0.45, a 5px `#00ff41`
  bloom at 0.22; no SVG filter), so heads stay one cell size. Residual
  glyphs at 0.1 fill the gaps between streaks, with smaller, dimmer far
  columns in the wider gaps for depth. One 997x960 tile on `html::after`
  wraps across its bottom edge, so the loop has no seam; the layer falls by
  `transform: translateY` of one tile height every 13s and composites
  rather than repainting (`will-change: transform`, `contain: strict`). With reduced motion
  the columns stand still.
- All text carries a 2px bloom. Text that can stand on the rain (the
  content well and a bare `aside`) adds a black halo (2px, then 5px; phones keep only the 2px layer, which
  keeps scrolling cheap on low-end devices), so
  its glyphs have a dark moat; panels, cards, tables, alerts, dialogs and
  popovers drop back to the bloom alone, which keeps scrolling cheap. A
  bare `aside` and the page-level lines (breadcrumb, h1/h2, lede, a
  control row) also get an 80% black backing, the lines cut to their own
  width with 6px of black round the text, at zero class specificity so a
  drawer or panel keeps its own fill. Desktop icon names on the rain get
  the same black cell. The halo's alpha is
  computed from the text's own lightness (relative colour from
  `currentColor`), so dark labels on lit fills get none; controls keep
  bloom only.
  The content well is a 30% black wash over the rain, so the code wall
  stays bright between panels; panels and tables
  are opaque. Pagination is a strip of cells on black; the current page is
  a `--surface-2` cell with a lit `#00ff41` rule.
- Panel rules are a lit `#1a9a2a` with a 24px inward glow; modals, toasts
  and alerts get the SYSTEM FAILURE double rule (black gap, then a 1px lit
  line, in the alert's state colour). The app bar is the operator console's toolbar plate: a dark green
  `#0b3d1c` to `#062a12` gradient with faint 3px scanlines and a 2px bevel
  (lit `#1f6a3a` top, dark bottom). Window and dialog title bars
  (`.modal-header`) are the same plate and bevel; an inactive window's
  bar drops to the near-black scanlined panel header. A window's tab strip
  keeps mixed case so its tabs fit on one row; panel headers keep the scanlines on
  near-black, and their icon buttons (and a `.toolbar`'s) are the same
  raised plate cells. A focused input lights up as the film's "Searching..." field:
  a bright `#00ff41` rim, outer and inner glow, and a `#06200d` fill.
- Warning is white-hot only in its text: the warning alert's rules and the
  solid warning badge use the brighter green step `#7dff9a`; the soft
  warning badge is a `#0f2a14` cell under a `#7dff9a` rule. A comment's anchored
  text and highlighted `mark` text sit on the same `#0f2a14` cell (an anchor is `#1d5a2a` when active).
- Checkboxes and radios are drawn as green-ruled cells (phosphor fill and
  black tick when checked); the slider track is the lit rule colour (in Firefox the part up to
  the thumb lights `#00ff41`). The bar chart's highlighted column is a
  solid brighter step `#7dff9a`, not a pale gradient.

- At `data-alert` the main view glitches like a CRT losing sync: green-only
  ghost offsets (`#00ff41`, `#7dff9a`) and a brightness jolt at red, never
  a red/cyan fringe.
- A heading flicker animation, gated behind
  `@media (prefers-reduced-motion: no-preference)` and never carrying state
  on its own.
- Panels glow faintly *inward* (`inset` shadow) as though lit from behind.
- Selected rows wash green at 12%; the active-row marker stays a hard bar.

### Icons

`themes/matrix/icons.svg` redraws six icons (home, settings, search,
close, user, bell) as thin monospace/glyph-like line marks — a 1px
stroke with square terminal caps in place of the generic sprite's 2px
rounded default, so they read as hairline character strokes rather than
a UI icon set. Settings becomes an eight-point asterisk glyph instead of
a naturalistic gear, matching a terminal's habit of representing controls
as punctuation rather than pictures. The sprite ships 181 `<symbol>`s in total (`grep -c '<symbol'`), and each differs from the generic outline sprite in `assets/icons/icons.svg`; only the six above are described in detail. The sprite now covers the full core set (178/178). Style rules for the
whole file, followed by the 45 ids added in the 2026-10 top-up: 24 grid;
1px hairline stroke, square caps, miter joins; never filled (the sprite
inherits `fill: none`); true curves allowed; rects rx 1.5 when 6+ wide,
sharp below; dots are r1.2 hairline rings; colour is `currentColor` only.
- **Easter egg** (`data-easter-eggs`, `assets/js/eggs.js`): after a minute idle, digital rain falls until the next key or pointer move (`@keyframes matrix-egg-rain`, separate from the page rain).

## Layout

A **terminal**: black bar, one hairline rule, no rail, content filling the
frame. The least furniture of any theme in the catalogue — deliberately the
opposite extreme from LCARS.

## Extending it

Do: keep everything monospace; keep the bloom subtle; add new states as
brightness steps of green rather than as new hues.
Don't: add a second accent colour, use a sans-serif anywhere, or let the
flicker animation communicate anything.

## Tell-tales of an inauthentic result

- A proportional font anywhere → the illusion collapses immediately.
- Multiple accent hues → a "hacker" theme, not a phosphor terminal.
- Heavy neon glow → cyberpunk, not CRT.

## Typography

`--font` (and `--font-mono`) is `"DejaVu Sans Mono", Consolas, Menlo, "Courier New", monospace`: a clean sans mono for running text, so long copy stays legible and lands at a similar width everywhere (Courier New's serif typewriter face is last-resort only). The app bar (`--app-bar-font`), h1-h3, the big numerals (`.stat-value`, `.timecode`, `.price`) and the console captions (panel and window title bars, table heads, `.stat-label`, at weight 400 with `font-synthesis: none`, since the face has no bold) use `--font-console`, **Share Tech Mono** (vendored, OFL, `assets/fonts/ShareTechMono-Regular.woff2`), the squared LCD-style mono closest to the operator console's "Searching..." field, falling back to `--font`. On phones the five-way toggle group and the bar nav trim their side padding so the wide mono keeps 4px clear of the box edge. The film's rain glyphs are mirrored katakana and numerals from a custom set; katakana has no reliable system font, so the rain draws a score of katakana-like shapes as SVG strokes (no font needed) beside mirrored digits and symbols in the system monospace.

## Contrast honesty

- **Phosphor green `#00ff41` is unlifted.** The `theme.css` header says it matches the reference on-screen code's hex; `RESEARCH.md` records no hex, so that claim could not be verified from the folder. It is 15.38:1 on black and 14.73:1 on `--surface` `#000a02` (black with green light only), so no AA adjustment was needed, and black `--on-accent` `#001a06` is 13.37:1 on it.
- **Body text** `#3cf060` is a saturated phosphor green on the film's 140deg axis, between `#00ff41` and `#008f11` (13.83:1 on black, 12.51:1 on `--surface-2` `#021405`), so long copy is not pure accent; pale and white are kept for heads, focus and warnings.
- **`--muted` `#5cc860`** is 9.47:1 on `--surface` and 8.95:1 on `--surface-2`: AAA on every panel.
- **Red is the only non-green hue.** `--danger` `#ff3b3b` is 5.94:1 on black.
- **`--border` `#1a9a2a`** is about 5.7:1 on black, so the slider track and control rules clear the 3:1 non-text floor.

## Reference status

`references/matrix/` has 4 captures plus `RESEARCH.md`: digital-rain crops, a "SYSTEM FAILURE" code wall and a green terminal screencap (all people-free per the audit). They back the phosphor palette and the monospace look. `RESEARCH.md` states the operator-console (monitor wall) target remains uncovered, and records no hex values.

## v5 layout

Tiers (core): mobile ≤480px, tablet 481–900px, desktop 901–1800px, XL ≥1801px (shell capped at 1800px, centred). On phone and tablet the bar is two lines (brand and actions, then the nav scrolling sideways); the terminal has no rail or bar decoration to rearrange, so nothing else changes. On XL the gutters show the rain frozen: a still wall of dim code columns cut into glyph cells, on black (about 1.0:1 against `--bg`). The live rain keeps running on the page itself.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
