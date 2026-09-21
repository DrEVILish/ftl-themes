# Fallout Pip-Boy 3000

> Post-apocalyptic monochrome phosphor green with scanlines.

## What this theme is trying to achieve

A wrist-mounted CRT terminal in a ruined world: single-hue green phosphor,
static scanlines, and text that glows faintly rather than sitting flat on
the screen.

## Core values

1. **One hue, many brightnesses.** Every colour role (text, accent, success,
   even danger where possible) is a shade of the same phosphor green;
   `--ftl-danger`/`--ftl-warning` are the only deliberate departures,
   reserved for genuine hazard states.
2. **Outline buttons, not fills.** A Pip-Boy button is drawn, not painted.
3. **Scanlines are decoration, not motion.** A static repeating gradient,
   `pointer-events: none`, never an animated flicker — nothing here should
   fight `prefers-reduced-motion` for a cosmetic effect.
4. **Uppercase, tracked headings** — terminal readouts, not a stylized logo.

## Layout

Minimal chrome, matching the terminal's own screen: a plain bar with a
green rule, content filling the frame, scanlines over the whole shell.

## Tell-tales of an inauthentic result

- A second hue appearing outside hazard states.
- Filled, solid buttons — the Pip-Boy draws in outline.
- An animated flicker — static scanlines only.

## Adoption

This theme sets `--ftl-app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.ftl-app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
