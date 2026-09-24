# Cyber-Goth

> Pitch-black club aesthetic with toxic neon green, hot purple and vinyl gloss.

**Requires: L1** — sets `--ftl-app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

The club-kid cyber-goth look: black vinyl surfaces, UV-reactive neon green
against hot purple structure, and a glow that reads as blacklight rather
than as a HUD's telemetry glow.

## Core values

1. **Purple structures, green signals.** `--ftl-flare` (purple) is the
   theme's borders, rules and headings; `--ftl-accent` (toxic green) is
   reserved for primary/interactive/success — the two must not swap roles.
2. **Black vinyl gloss, not matte.** Panels and buttons carry a subtle
   top-lit gradient — plastic under a club light, not flat paint.
3. **Glow is UV bloom.** Hover/focus glows are wide and colour-matched to
   whichever hue is glowing, not a tight HUD ring.
4. **Uppercase, geometric type** — flyer/rave typography, not corporate
   sans.
5. **Spiked, studded-leather chrome, not just neon-on-black.** Colour
   alone doesn't distinguish this from any other neon cyberpunk theme in
   the catalog — a jagged sawtooth trim on every structural bar and a
   hard-edged, riveted drop-shadow on buttons/panels are the theme's own
   silhouette, legible even in a colourless crop.

## Signature details

- Primary buttons' hover glow (`0 0 14px rgba(214, 31, 255, 0.6)`) is
  purple even though the button fill is green — the bloom always reads as
  the *structural* colour, never the signal one.
- Table headers and rules pick up `--ftl-flare` (purple), not the accent —
  structure stays purple everywhere, including inside components.
- A jagged sawtooth trim (a repeating 45°/-45° gradient pair, the classic
  "torn ticket edge" CSS technique) runs along the app bar, nav, and
  panel/modal headers — a studded-collar silhouette, not a smooth bevel
  like `alienware`'s clip-path corners and not `matrix`'s monospace rain.
  It's a decorative pseudo-element strip, so it never clips a focus ring,
  click target or label.
- Buttons carry a single asymmetric fang cut on the top-right corner only
  (`clip-path`) plus a hard black offset shadow underneath the neon
  bloom — riveted vinyl, not a soft glow alone. `alienware` cuts both
  opposing corners at matching size; this cuts one corner, deliberately
  uneven.
- The font stack leads with Eurostile, the same unvendored-face situation
  as `tron`/`death-star` — it silently falls back to a system sans on most
  real machines rather than the intended geometric face.

## Layout

A black bar and status strip both edged in the purple rule, with the
content area carrying the same vinyl-gloss panels throughout.

## Tell-tales of an inauthentic result

- Purple and green swapping jobs (purple as the primary action colour, or
  green as structure) → the two-colour logic collapses.
- Flat matte surfaces — this is glossy plastic, not a terminal.
- A tight, thin glow instead of a soft bloom.
- No sawtooth trim / no hard-edged studded shadow — without it this is
  just another neon-on-black palette, indistinguishable from any other
  cyberpunk theme in the catalog.

## Adoption

This theme sets `--ftl-app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.ftl-app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
