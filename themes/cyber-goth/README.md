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
   control outlines, rules and panel edges, `--flare-text` for h3, panel
   and window titles. Page titles (h1/h2) are pale `--text` under a purple
   bloom, and the bar sawtooth is a dimmer `#a020d8`, so the green neon
   carries the eye as the captures show. `--accent` (toxic green) is
   the one neon, reserved for primary/interactive/success — the two must
   not swap roles.
2. **Black vinyl gloss, not matte.** Surfaces are near-neutral black
   (`--surface` `#0b090c`, `--surface-2` `#141117`, vinyl `#151217` to
   `#070608`), as the leather capture; purple lives in rules, teeth,
   plates and titles, not in the fills. Panels and buttons carry a lit 1px
   lip and a 7.5% specular band over their top ~40%, capped at 28-40px so
   tall panels show no seam (`--gloss`), a faint 115° diagonal sheen, and
   on panels and windows a static 4% feTurbulence leather grain. Alerts,
   menus, popovers, lists, nav rails and boxed toolbars take the same
   gloss on a 3px slab.
3. **Glow is UV bloom.** Hover/focus glows are wide and colour-matched to
   whichever hue is glowing, not a tight HUD ring.
4. **Uppercase, geometric type** — flyer/rave typography, not corporate
   sans.
5. **Spiked, studded-leather chrome, not just neon-on-black.** Colour
   alone doesn't distinguish this from any other neon cyberpunk theme in
   the catalog — a jagged sawtooth trim on the structural bars, a
   hard-edged offset slab under buttons/panels and cone studs in panel
   corners are the theme's own silhouette, legible even in a colourless
   crop.

## Signature details

- Primary buttons' hover glow (`0 0 14px rgba(214, 31, 255, 0.6)`) is
  purple even though the button fill is green — the bloom always reads as
  the *structural* colour, never the signal one.
- Table header text uses `--flare-text`, and table rules, input, button
  and slider outlines the dimmer `--line` purple, never the accent:
  structure stays purple everywhere, including inside components. Info
  alerts are outlined in `--flare`, so green outlines only success.
- A jagged sawtooth trim (a repeating 45°/-45° gradient pair, the classic
  "torn ticket edge" CSS technique) runs along the app bar, nav and modal
  headers at full glow; panel headers get a smaller, unlit strip (7px,
  10px period, no solid rule under it) so the bars stay the loudest
  structure. A studded-collar silhouette, not a
  smooth bevel like `alienware`'s clip-path corners and not `matrix`'s
  monospace rain. It's a decorative pseudo-element strip with room left
  under it, so it never covers the next line. On phone and tablet the
  teeth drop their `drop-shadow` filter (a scroll cost) and paint in the
  brighter `--flare` instead.
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
  `#6a2d96`), with an 8px cone stud (lit tip, violet cone, dark rim)
  riveted into the outer 9px of each corner, like a collar's. Titled
  modals and desktop windows keep only the bottom pair, so the title bar
  and its icon never sit on a stud; a resizable window keeps only the
  bottom-left one, clear of the grip. On phone and tablet panels drop the
  studs, grain, 12px halo and heading blooms (scroll paint budget) and
  keep the plate and gloss.
- Panel, modal and window titles are uppercase Audiowide in `--flare-text`,
  including h2/h3 used inside a panel; panel titles carry no bloom (it
  softened Audiowide's counters at that size). Window caption buttons are
  all `--muted`, lit green on hover.
- Green is never an edge: own-message bubbles and the bulk-selection bar
  keep a green-tinted fill but a `--line` purple outline. Selected rows
  take a 10% purple wash.
- Table heads and stat labels never drop under 0.75rem.
- Charts: series 1 is the green, series 2 the structural purple
  (`--flare-text`) and series 5 lavender `#b98cff`, since `--accent` and
  `--success` are the same green.
- Stat labels read a lighter lavender (`#b9a0d8`) than `--muted`.

## Layout

A black bar and status strip both edged in the purple rule, with the
content area carrying the same vinyl-gloss panels throughout.

## v5 layout

- **Tiers.** No rail on any tier. On phone and tablet (≤900px) the nav
  gets its own scrolling line in the bar; its own sawtooth is dropped
  there (the scroller clipped it, and the bar's sawtooth already edges the
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

Both faces are vendored (SIL OFL, `assets/fonts/`). `--font-display` is **Audiowide**, the rave-flyer face, for h1-h3, panel and modal titles. `--font` is **Titillium Web**, a squared techno sans in Eurostile's family tree (Eurostile itself is commercial and not named), for body, buttons and tabs; buttons, toggle buttons and tabs are uppercase and tracked. `--font-mono` is **Share Tech Mono** (vendored, same squared techno family) for readouts and stat values, at its single regular weight. `references/cyber-goth/cyber-goth-neon-sign-typography.jpg` shows rounded monoline tube letters; Audiowide's squared terminals are a rave-flyer reading, not a tube imitation. A rounded face (Righteous, Comfortaa) was considered for h1 and not adopted: a second display face would split the headline voice from the panel titles for a small fidelity gain.

## Contrast honesty

- **Neon green on black is far above the floor:** `--accent` `#39ff5a` (EL-wire green, from `cyber-goth-el-wire-closeup.jpg`: glow mean `#3de65d`, core `#87faac`) is 15.48:1 on `--bg`; `--on-accent` `#0a0f00` is 14.45:1 on it.
- **Purple:** `--accent-2`/`--flare` `#d61fff` is 5.45:1 on `--bg` but 4.41:1 on the tinted `#2d1137`, so text (headings, panel titles, table heads) uses `--flare-text` `#e04dff` (5.35:1 there); `--flare` stays for the sawtooth trims and bar rules. Control outlines (inputs, buttons, slider track, table rules) use `--line` `#9030d8`, 3.57:1 on `--bg` and 3.45:1 on the input fill, above the 3:1 non-text floor. `--border` `#7a1fbf` is only 2.75:1 on `--bg` (a decorative panel edge, not text or a control boundary). The status strip text is `--muted`.
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
