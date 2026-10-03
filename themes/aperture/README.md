# Aperture Science

> Sterile laboratory off-whites and dark greys, accented by testing-chamber blue and orange.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

A clean, sterile test-chamber control panel: off-white surfaces, quiet
grey structure, and the two portal colours — blue and orange — used
exactly where the reference used them, as the only saturated colours in an
otherwise clinical space.

## Core values

1. **The first light theme in this batch of clinical calm.** Off-white,
   not stark white — `--bg`/`--surface` sit a shade apart so
   surfaces read as physical panels, not a blank page.
2. **Blue is primary/interactive; orange is the second portal, reserved
   for destructive actions** — a direct, deliberate swap of the usual
   red-for-danger convention, because orange is what the reference uses
   for its second state.
3. **No decoration.** Flat fills, quiet 1px borders, small shadows. This is
   institutional software, not a HUD.
4. **Grey, understated headings** — a section label on a clipboard, not a
   marketing headline.

## Signature details

- Danger buttons fill with the portal orange (`--accent-2`), not red —
  the one place this theme breaks from every other theme's convention on
  purpose, with dark text since orange is too light for white to pass.
- Headings are muted grey, `font-weight: 700`, and never uppercase — a
  clipboard label, not a marketing headline.
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
- Saturated colour anywhere except the two accents.

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
