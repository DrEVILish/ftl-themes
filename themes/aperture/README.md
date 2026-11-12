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
3. **No decoration.** Flat fills, quiet 1px borders, small shadows. This is
   institutional software, not a HUD.
4. **Headings are chamber signs** — black, light and large, never
   uppercase: the sign plate's numeral, not a marketing headline.

## Signature details

- Danger is the portal orange (`--danger: #ff8a1e`, dark `--on-danger`
  text, `--danger-text: #8f4500`) everywhere — buttons, badges, alerts,
  invalid fields, status, danger menu items — not red. Warning takes the
  facility's hazard yellow (`#f4c430`, text `#6b5600`) so the two never
  share a colour.
- Blue is portal blue: fills take `--accent: #0b78c2` (4.7:1 under white
  text), text takes the deeper `#13609a` (5.4:1 on the page), and every
  blue that carries no text (focus ring, spinner, slider thumb, chart
  series 1) takes the brighter portal azure `--aperture-portal: #1a8ad8`
  (3:1 on the page).
- Type: Titillium Web (vendored, OFL) stands in for the chamber signage
  grotesk — headings light (400) and lightly tracked, panel h3 at 600;
  readouts and KPI values use the same light face as chamber numerals;
  Share Tech Mono for code. Headings are `--text` black and never
  uppercase; h1 gets `margin-block-end: var(--space-xs)` because the
  face's line box is trimmed for controls.
- Chamber sign plate: the page h1 sits under a 5px `#2b2b2b` rule with a
  row of short dashes under it (the chamber progress bar); panel headers
  are black text over a 2px `#2b2b2b` rule; KPI labels carry the plate's
  black pictogram square.
- Neutrals are cool lab greys: `--bg #e6e8e9`, `--surface #f3f4f5`,
  `--app-bg #dcdfe1`, `--border #c3c7ca`, `--muted #5a5e62`.
  `--app-main-bg` is flat; the 128px panel seams live in the XL gutter.
- Sliders are a 0.375rem grey groove (`--slider-bg: #7f8488`, 3:1 on the
  page) with a 1.1rem azure thumb; charts use only blue, orange and greys.
- Shadows never exceed `0 1px 3px` — this is the flattest, quietest theme
  in the catalog; anything heavier reads as a different theme entirely.

## Layout

A plain white bar and status strip on a slightly darker page backdrop —
the panel sits in the room rather than filling it.

## v5 layout

- **Tiers.** No rail and no bar decoration, so phone (≤480px) and tablet
  (481–900px) use core's one-column shell as is: brand and actions on the
  first line, the nav scrolling on the second.
- **XL gutter art.** The test chamber's wall continues past the console:
  square white wall panels with recessed seams and one faint portal ring
  each side (blue left, orange right). Still, and within about 1.3:1 of
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
