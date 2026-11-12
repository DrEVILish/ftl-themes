# Aperture Science

> Sterile laboratory off-whites and dark greys, accented by testing-chamber blue and orange.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

A clean, sterile test-chamber control panel: cool off-white surfaces,
neutral grey structure, and the two portal colours — blue and orange — used
exactly where the reference used them, as the only saturated colours in an
otherwise clinical space.

## Core values

1. **The first light theme in this batch of clinical calm.** Cool,
   near-neutral off-white (lab, not paper), not stark white — `--bg`/`--surface` sit a shade apart so
   surfaces read as physical panels, not a blank page.
2. **Blue is primary/interactive; orange is the second portal, reserved
   for danger** — a direct, deliberate swap of the usual red-for-danger
   convention across every danger state, because orange is what the
   reference uses for its second state.
3. **No decoration.** Flat fills, quiet 1px edges, no shadow on surfaces.
   Surfaces are rounded sign plates (`--panel-radius: 0.6rem`); controls
   stay square-ish hardware (`--radius: 0.2rem`). This is institutional
   software, not a HUD.
4. **Headings are chamber signs** — black, light and large, never
   uppercase: the sign plate's numeral, not a marketing headline.

## Signature details

- Danger is the portal orange (`--danger: #ff9a1f`, dark `--on-danger`
  text, `--danger-text: #9a4a00`) everywhere — buttons, badges, alerts,
  invalid fields, status, danger menu items — not red. Where danger is
  text, the orange itself still shows: error/rec status dots are
  `#ff9a1f` and danger menu items carry a 3px orange leading edge.
- Success is a filled state only, a grey teal (`--success: #3f6f66`,
  white text) so it never reads as a third brand colour; meters fill
  portal blue (`--meter-low`), warn in hazard yellow and peak in orange,
  and a rising sparkline is portal blue, not green. Warning takes the
  facility's hazard yellow (`#f4c430`, text `#6b5600`) so the two never
  share a colour.
- Blue is the cyan-azure of the blue portal: fills take `--accent:
  #0b8ccc` (hue ~200, full saturation) under dark `--on-accent: #0d1b26`
  text (4.7:1), not a corporate link blue; the same azure
  (`--aperture-portal`) is every mark that carries no text (focus ring,
  spinner, slider thumb, chart series 1; 3:1 on the page). The brighter
  in-game `#2fa3e0` is kept to the black brand tile and the XL gutter
  ring, where it does not have to clear 3:1 on the light page; chart
  series 1 and the rising sparkline, which sit on the white plate, take
  the brighter `#1a9ad8` (3.15:1 on `#fff`). Blue text takes the deeper `#13609a`
  (5.4:1 on the page), including sort headers and scrollspy links.
- Type: `--font` names Univers (`"Univers LT Std", Univers`) first, the
  chamber signage face; Inter (vendored as `"Aperture Inter"`, OFL, one
  variable Latin file at weights 300–700) stands in where it is absent,
  as the closest open neutral grotesk to Univers' Swiss proportions. h1/h2 are Light 300
  and lightly tracked, h3 at 600; readouts and KPI values (`.stat-value`
  1.9rem) are Light 300 chamber numerals; labels (brand, panel headers)
  are SemiBold 600 at most, uppercase KPI labels at least 0.75rem. Share
  Tech Mono for code. Headings are `--text` black and never
  uppercase; h1 gets `margin-block-end: var(--space-xs)` because the
  face's line box is trimmed for controls.
- Chamber sign plate: the page h1 is its own white plate (`--panel-bg`,
  `--panel-radius`, 1px `--panel-border` edge, sized to the sign, at
  least 18.5rem wide) under a 5px `#2b2b2b` rule, led by a light black
  "04" chamber numeral at 1.5em; under it, the chamber progress bar —
  eleven 1.25rem × 0.5rem dashes, the first four black and the rest
  `#c3c7ca` — with an "04/11" counter, then the hazard row of eight 2rem
  tiles: this chamber's hazards lit black (cube, button, water, pellet)
  and the rest unlit, a white glyph on a `#c3c7ca` tile (fling, turret,
  laser, cake), as on the in-game sign. On a phone the hazard row drops
  so content starts on the first screen. A hero h1 keeps the rule and
  strip but no plate. Both pseudo-elements are hidden from assistive
  tech. Panel headers, modal headers and window title bars are black
  text over a 2px `#2b2b2b` rule; the active tab sits on a 4px black rule
  (core's 2px `--tab-underline-active` border plus a 2px inset), not a
  blue one.
- Sign pictograms: the app-bar brand carries a black tile with the blue
  and orange portal pair, at every width; panel headers and KPI labels
  carry a black tile (1.5em, at least 20px; 1.4em on KPI labels) with a
  white chamber-sign pictogram that cycles
  cube, cube-on-button, water hazard and energy pellet by position, so a
  dashboard shows a row of them like a chamber sign (inline SVG data
  URIs, `--aperture-picto-*`).
- Panels, cards and modals are flat sign plates: `--panel-radius:
  0.6rem`, a darker `#b5babd` edge and no shadow. Initials avatars are a
  `--surface` disc with a 1px `--border` ring, so they read on the white
  plate.
- Neutrals are cool lab greys: `--bg #e6e8e9`, `--surface #f3f4f5`,
  `--app-bg #dcdfe1`, `--border #c3c7ca`, `--muted #5a5e62`.
  `--app-main-bg` is flat; the 128px panel seams live in the XL gutter.
- Sliders are a 0.375rem grey groove (`--slider-bg: #7f8488`, 3:1 on the
  page) with a 1.1rem azure thumb; charts use only blue, orange and greys.
- Surfaces have no shadow and buttons `0 1px 2px` at most — this is the
  flattest, quietest theme in the catalog; anything heavier reads as a
  different theme entirely.
- Alerts and toasts take a 4px leading edge in their state colour; the
  warning one is a single 8px left edge painted with the hazard stripe.
- Pager items are `--text` at 0.8125rem and `.status` at 0.8125rem or
  more, so small secondary text stays legible in the light face.

## Layout

A plain white bar and status strip on a slightly darker page backdrop —
the panel sits in the room rather than filling it.

## v5 layout

- **Tiers.** No rail and no bar decoration, so phone (≤480px) and tablet
  (481–900px) use core's one-column shell, except that on a phone the
  brand takes its own full line so its name is not elided to the tile,
  the actions keep one row (the switcher shrinks, the search button
  drops its Ctrl K hint), and the page sign drops its hazard row.
- **XL gutter art.** The test chamber's wall continues past the console:
  square white wall panels with recessed seams and one faint portal ring
  each side (azure `#27a7d8` left, orange `#ff9a1f` right). Still, and within about 1.3:1 of
  `--bg`.

## Tell-tales of an inauthentic result

- Red used for danger instead of orange → loses the portal-colour logic.
- Any glow, gradient or heavy shadow — this is the calmest theme in the
  catalogue by design.
- Saturated colour anywhere except the two accents (and the hazard
  yellow, which is signage for warnings only).

## Icons

`icons.svg` draws the core set as test-chamber sign pictograms (no Aperture or Valve marks).

- **Plate.** Every icon is a sign plate: a 1.25px rounded-square outline (radius 3.5) filling the 24 box, with the pictogram inside it at 78% scale.
- **Pictogram.** Bold 1.9px line with round caps and joins, true curves; silhouettes (bookmark, play, filter, pin, star) are solid fills; small solid dots for markers.
- **Scaling.** The 78% is done by zooming the symbol's `viewBox` out to 30.77 units, so the attributes read `stroke-width="2.44"` and `1.6` for the 1.9px and 1.25px rendered widths.
- Generated from one shared 24-grid geometry, so every core-set id (178/178) is drawn; everything uses `currentColor`, so icons follow text, accent and selected states (and every variant) with no hard-coded colour.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
