# Cyber-Goth

> Pitch-black club aesthetic with toxic neon green, hot purple and vinyl gloss.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

The club-kid cyber-goth look: black vinyl surfaces, UV-reactive neon green
against hot purple structure, and a glow that reads as blacklight rather
than as a HUD's telemetry glow.

## Core values

1. **Purple structures, green signals.** Purple is the blacklight
   ambience: dim `--line` (`#9030d8`) and `--border` (`#7a1fbf`) for
   control outlines and rules, a dimmer `#4a1a70` (`--panel-border`,
   `--modal-border`) for decorative panel and window edges. Titles are not
   hot purple: h3, panel, window and table-head text is a dim lavender
   `--title` (`#b9a0d8`), page titles (h1/h2) pale `--text` under a purple
   bloom, and the bar sawtooth `#7a1fbf`, so the green neon is the
   brightest and most saturated thing on every page, as the captures show. `--accent` (toxic green) is
   the one neon, reserved for primary/interactive/success — the two must
   not swap roles. Green is lit, not just coloured: green signals carry an
   EL-wire bloom at rest, so they stay the brightest light on the page.
2. **Black vinyl gloss, not matte.** Surfaces are near-neutral black
   (`--surface` `#0b090c`, `--surface-2` `#141117`, vinyl `#151217` to
   `#070608`), as the leather capture; purple lives in rules, teeth,
   plates and titles, not in the fills. Panels and buttons carry a lit 1px
   lip and a specular band that fades from 7% through 3.5% (at 30%, max
   24px) to nothing at 60% (max 56px), so tall panels show a soft sheen,
   not a two-tone strip (`--gloss`), a faint 115° diagonal sheen, and on
   panels and windows a static 7% feTurbulence leather grain. Alerts,
   menus, popovers, lists, nav rails and boxed toolbars take the same
   gloss on a 3px slab.
3. **Glow is UV bloom.** Hover/focus glows are wide and colour-matched to
   whichever hue is glowing, not a tight HUD ring.
4. **Uppercase, geometric type** — flyer/rave typography, not corporate
   sans. Headings, panel titles, buttons, tabs, the brand (Audiowide) and
   navigation labels (bar nav and menubar, nav rails, settings section
   lists) are uppercase and tracked; body copy, message lists and data
   cells stay mixed case.
5. **Spiked, studded-leather chrome, not just neon-on-black.** Colour
   alone doesn't distinguish this from any other neon cyberpunk theme in
   the catalog — a jagged sawtooth trim on the structural bars, a
   hard-edged offset slab under buttons/panels and cone studs in panel
   corners are the theme's own silhouette, legible even in a colourless
   crop.

## Signature details

- Green signals glow at rest, as the EL-wire capture is all halo: primary
  and success buttons, checked toggles and the current pagination item
  take a two-layer bloom (`0 0 3px` at 0.5, `0 0 14px` at 0.4 of
  `#39ff5a`); the active tab, brand and current nav item a green
  `text-shadow`; sparklines and chart lines a 3px `drop-shadow` in their
  own series hue (desktop tiers only). The button clip polygon is the box
  grown 12px on every side minus only the cut triangle (and its 3px slab
  shadow), reached by a zero-width slit, so the bloom wraps the fang
  evenly while the cut corner stays empty.
- Primary buttons' hover glow (`0 0 14px rgba(214, 31, 255, 0.6)`) is
  purple even though the button fill is green — the bloom always reads as
  the *structural* colour, never the signal one.
- Table header text uses the lavender `--title`, and table rules, input, button
  and slider outlines the dimmer `--line` purple, never the accent:
  structure stays purple everywhere, including inside components. Info
  alerts are outlined in `--flare`, so green outlines only success.
- A jagged sawtooth trim (a repeating 45°/-45° gradient pair, the classic
  "torn ticket edge" CSS technique) runs along the app bar, nav and modal
  headers at full glow (`#7a1fbf`); panel headers get a smaller, unlit
  strip in `--border` (7px, 10px period, no solid rule under it) so the bars stay the loudest
  structure. The bar teeth glow at a 4px, 0.45-alpha purple `drop-shadow`,
  kept below the green signals. A studded-collar silhouette, not a
  smooth bevel like `alienware`'s clip-path corners and not `matrix`'s
  monospace rain. It's a decorative pseudo-element strip with room left
  under it, so it never covers the next line. On phone and tablet the
  teeth drop their `drop-shadow` filter (a scroll cost) and paint in the
  slightly brighter `--line` instead.
- Text buttons carry a single asymmetric fang cut on the top-right corner
  only (`clip-path`), with the border redrawn along the diagonal, over a
  hard dark-violet 3px offset slab (`#3a1550`; pure black vanished on the
  near-black page) that the clip polygon extends to include. `alienware`
  cuts both opposing corners at matching size; this cuts one, deliberately
  uneven. Standalone `.toggle-btn` shares the cut and slab; a
  `.toggle-group` row is cut on its last segment only, without a slab.
  Round icon buttons and avatars keep core's circle. Focus rings
  sit 4px inside the cut so the clip never hides them.
- Panels, cards and modals sit on a 4px offset plate (`#2a0e3a`, edged
  `#6a2d96`); alerts, menus, popovers, lists and toolbars ride a plain,
  unedged 3px slab. A 12px cone stud (lit tip, violet cone, near-black
  rim so it reads as raised metal) is riveted 2px into each corner, like
  a collar's. Titled
  modals and desktop windows keep only the bottom pair, so the title bar
  and its icon never sit on a stud; a resizable window keeps only the
  bottom-left one, clear of the grip. On phone and tablet panels drop the
  studs, grain, diagonal sheen, 12px halo, plate edge, line glows and
  heading blooms (scroll paint budget) and keep one plain plate and the
  gloss.
- Panel, modal and window titles are uppercase Audiowide in the lavender
  `--title`, including h2/h3 used inside a panel, at no less than 0.9rem
  with 0.05em tracking; popover titles, accordion triggers
  and kanban card titles take the same uppercase Audiowide at 0.9em; panel titles carry no bloom (it
  softened Audiowide's counters at that size). Window caption buttons are
  all `--muted` with no title bloom, lit green on hover.
- Green is never an edge: own-message bubbles and the bulk-selection bar
  keep a green-tinted fill but a `--line` purple outline; current-row,
  list, tree and nav-rail markers are `--line` purple bars; a featured
  list card takes a 2px `--flare` border. Only a semantic `is-success`
  card is outlined green. Selected rows
  take a 10% purple wash. A pending (dirty) cell keeps core's yellow bar
  over only a 5% yellow wash, so it never muddies a selected row.
- Table heads, stat labels and status chips never drop under 0.75rem. A
  disabled pager item sits at 0.6 opacity, not a near-background tone.
- Charts: series 1 is the green, series 2 the structural purple
  (`--flare-text`) and series 5 lavender `#b98cff`, since `--accent` and
  `--success` are the same green.
- Stat labels read a lighter lavender (`#b9a0d8`) than `--muted`.

## Layout

A black bar and status strip both edged in the purple rule, with the
content area carrying the same vinyl-gloss panels throughout.

## v5 layout

- **Tiers.** No rail on any tier. On phone and tablet (≤900px) the nav
  gets its own scrolling line in the bar, untracked so it stays one row,
  and the brand keeps its full name on the first line; the nav's own
  sawtooth is dropped there (the scroller clipped it, and the bar's sawtooth already edges the
  whole bar).
- **Nesting.** A panel inside another surface gets a smaller, unlit
  sawtooth. Headers leave a wider gap below them so the teeth never touch
  the first line of the body.
- **XL gutter art.** The club wall beside the console: a fishnet lattice in
  dark violet with a faint sawtooth trim running down each side. Still,
  and within about 1.2:1 of `--bg`.

## Tell-tales of an inauthentic result

- Purple and green swapping jobs (purple as the primary action colour, or
  green as structure) → the two-colour logic collapses.
- Flat matte surfaces — this is glossy plastic, not a terminal.
- A tight, thin glow instead of a soft bloom.
- No sawtooth trim / no hard-edged studded shadow — without it this is
  just another neon-on-black palette, indistinguishable from any other
  cyberpunk theme in the catalog.

## Don'ts

- **No swapping of roles.** Purple is structure; green signals. Never a purple primary action or green borders.
- **No third neon colour.** Danger and warning exist for states only.
- **No matte flat panels.** Keep the top-lit vinyl gradient, sawtooth trim and hard offset shadow.
- **No smooth bevels or soft glows alone**; the fang cut, offset slab and studs carry the silhouette.
- **No lowercase, corporate sans headings.**

## Icons

`icons.svg` redraws the full core set (178/178). Rules: 24 grid, core 2px
stroke, `stroke-linecap="square"` / `stroke-linejoin="miter"` forced on every
symbol. Every framed box is a polygon with ONE top-right "fang cut" (the
`.btn` clip-path), cut about a third of the short side, never two corners.
Circles become octagons, small marker dots are 1.4px stroked squares. Line
only: nothing is filled, so icons follow `currentColor` in every state. Curves
survive only where the concept needs them (cloud, moon, heart, droplet).

## Typography

Both faces are vendored (SIL OFL, `assets/fonts/`). `--font-display` is **Audiowide**, the rave-flyer face, for h1-h3, panel and modal titles, popover titles, accordion triggers and kanban card titles. `--font` is **Titillium Web**, a squared techno sans in Eurostile's family tree (Eurostile itself is commercial and not named), for body, buttons and tabs; buttons, toggle buttons, tabs and navigation labels are uppercase and tracked, and the brand is set in Audiowide. `--font-mono` is **Share Tech Mono** (vendored, same squared techno family) for readouts and stat values, at its single regular weight. `references/cyber-goth/cyber-goth-neon-sign-typography.jpg` shows rounded monoline tube letters; Audiowide's squared terminals are a rave-flyer reading, not a tube imitation. A rounded face (Righteous, Comfortaa) was considered for h1 and not adopted: a second display face would split the headline voice from the panel titles for a small fidelity gain.

## Contrast honesty

- **Neon green on black is far above the floor:** `--accent` `#39ff5a` (EL-wire green, from `cyber-goth-el-wire-closeup.jpg`: glow mean `#3de65d`, core `#87faac`) is 15.48:1 on `--bg`; `--on-accent` `#0a0f00` is 14.45:1 on it.
- **Purple:** `--accent-2`/`--flare` `#d61fff` is 5.45:1 on `--bg` but 4.41:1 on the tinted `#2d1137`, so purple text (chart series 2) uses `--flare-text` `#e04dff` (5.35:1 there); titles and table heads take the lavender `--title` `#b9a0d8` instead (8.85:1 on `--bg`, 7.28:1 on `#2d1137`); `--flare` stays for the sawtooth trims and bar rules. Control outlines (inputs, buttons, slider track, table rules) use `--line` `#9030d8`, 3.57:1 on `--bg` and 3.45:1 on the input fill, above the 3:1 non-text floor. `--border` `#7a1fbf` is only 2.75:1 on `--bg` (decorative, not text or a control boundary); panel and window edges go dimmer still, `#4a1a70`. The status strip text is `--muted`.
- **Danger:** `--danger` `#d61048` is 3.99:1 as text on `--bg` (fails), so copy uses `--danger-text` `#f03d70`; the fill takes white text at 5.21:1.
- **Muted** `#9d7ec2` is 5.87:1 on `--surface`, 4.92:1 on the brightest gloss stop.
- **Why purple exists at all.** The captures show a single green UV-reactive neon (`cyber-goth-el-wire-closeup.jpg`) on black; `RESEARCH.md`'s outsider read is "a single UV-reactive neon accent". The hot purple `#d61fff`/`#7a1fbf` structure is **not in any capture**. It is a design decision (blacklight club association, and to stop the theme reading as a green-only cousin of `matrix`), documented here rather than sourced. The hexes are unmeasured.

## Reference status

`references/cyber-goth/` has 5 captures plus `RESEARCH.md`: `cyber-goth-el-wire-closeup.jpg` (green EL wire on black, backs the neon-glow falloff and the single-neon idea), `cyber-goth-black-leather-texture.jpg` (backs the vinyl/leather base and its specular response), `cyber-goth-neon-sign-typography.jpg` (tube lettering on a dark wall), plus a cyberpunk-admin dashboard screenshot and a dev-to webp that `RESEARCH.md` calls off-direction. Honest gaps in `RESEARCH.md`: no true UV-blacklight photo, no mesh/rivet macro, so the sawtooth trim, fang cut and studs are not captured evidence.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
