# TRON

> Electric cyan line-grid on black — glowing, angular edges.

**Requires: L1** — sets `--ftl-app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

**The Grid**: a black void inscribed with glowing cyan circuitry, hard
angular geometry, and light used as a construction material. Everything
looks *drawn in light* rather than painted.

## Core values

1. **Light is the material.** Edges glow; surfaces stay near-black. A
   filled, non-glowing surface reads as off.
2. **Cut corners, never rounded ones.** `--ftl-radius: 0` plus `clip-path`
   corner cuts on buttons and panels. The chamfer is the signature.
3. **Cyan builds, orange opposes.** `--ftl-accent` cyan is the system;
   `--ftl-accent-2` orange is the adversary — reserved for danger and
   warning. Never use orange decoratively.
4. **The grid is always present.** A 2.5rem cyan line-grid at 6% underlies
   everything.
5. **Wide tracking, uppercase.** Headings set at `0.25em` — display type
   from a title sequence.

## Signature details

- Buttons and panels share the same 8px/12px chamfer polygon.
- The top bar casts a 12px cyan bloom downward.
- The active-row marker is *orange* against cyan selection — the one place
  the two colours meet, and only to separate "selected" from "playing".

## Layout

The shell becomes **an enclosure**: 0.75rem padding all round, a thin
0.35rem lit conduit down the left edge (the rail, drawn as a vertical light
gradient with a bloom rather than as a panel), and a glowing bar above.

## Known compromise

Eurostile, the reference face, is not web-available; the stack falls
through Orbitron to a generic sans. Vendoring a substitute is tracked in
`docs/theme-backlog.md`.

## Tell-tales of an inauthentic result

- Rounded corners → the chamfer language is the whole identity.
- Orange used for emphasis rather than danger → the cyan/orange opposition
  stops meaning anything.
- Solid bright surfaces → light should trace edges, not fill shapes.

## Adoption

This theme sets `--ftl-app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.ftl-app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
