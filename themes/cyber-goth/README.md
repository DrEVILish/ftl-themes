# Cyber-Goth

> Pitch-black club aesthetic with toxic neon green, hot purple and vinyl gloss.

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

## Signature details

- Primary buttons' hover glow (`0 0 14px rgba(214, 31, 255, 0.6)`) is
  purple even though the button fill is green — the bloom always reads as
  the *structural* colour, never the signal one.
- Table headers and rules pick up `--ftl-flare` (purple), not the accent —
  structure stays purple everywhere, including inside components.
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

## Adoption

This theme sets `--ftl-app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.ftl-app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
