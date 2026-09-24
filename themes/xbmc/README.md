# XBMC

> The original Xbox Media Center: a near-black home-theatre shell, a wide horizontal top menu, and a glowing blue underline marking whichever item is selected — driven by a remote, not a mouse.

**Requires: L1** — sets `--ftl-app-*` layout properties (the wide top menu bar); recolours correctly at L0 but the horizontal-menu-plus-underline composition needs the app shell.

## What this theme is trying to achieve

XBMC (later renamed Kodi) ran a horizontal top-level menu — Pictures,
Music, Videos, Weather, Programs, System — navigated with a d-pad/remote
from a couch, not a mouse from a desk. Its brand colour was always a
clean, saturated blue, carried through as a glow rather than a filled
highlight, against a near-black "home theatre" backdrop that vignettes
toward the edges.

## Core values

1. **The underline is the selection state, not a filled pill.** A glowing
   blue line beneath the active label, never a solid background block —
   see `.ftl-nav-item.is-active::after`.
2. **Near-black, not pure black, and vignetted.** The frame should read
   as a dim room, darkening toward the edges via the radial-gradient page
   background, not a flat single colour.
3. **One blue, used as light, not as fill.** `--ftl-accent` (`#1e90ff`)
   is a glow colour — box-shadow and border-highlight — more often than a
   background fill.

## Signature details

- The glowing underline on the active top-menu item
  (`box-shadow: 0 0 8px rgba(30,144,255,0.8)`).
- The vignette page background (radial-gradient darkening from top-centre
  outward).
- Thin, quiet chrome: 1px borders, small border-radius, no gloss or
  gradient buttons — a remote-driven UI has no hover state to sell with
  gloss.

## Tell-tales of an inauthentic result

- A filled/solid highlight block on the active nav item instead of an
  underline glow.
- A flat, unvignetted background — the "home theatre" read depends on the
  edges going darker than the centre.
- Rounded, glossy buttons — this UI's affordances are flat rectangles with
  a border, not skeuomorphic buttons.
