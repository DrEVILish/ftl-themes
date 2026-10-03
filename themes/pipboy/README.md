# Fallout Pip-Boy 3000

> Post-apocalyptic monochrome phosphor green with scanlines.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

A wrist-mounted CRT terminal in a ruined world: single-hue green phosphor,
static scanlines, and text that glows faintly rather than sitting flat on
the screen.

## Core values

1. **One hue, many brightnesses.** Every colour role (text, accent, success,
   even danger where possible) is a shade of the same phosphor green;
   `--danger`/`--warning` are the only deliberate departures,
   reserved for genuine hazard states.
2. **Outline buttons, not fills.** A Pip-Boy button is drawn, not painted.
3. **Scanlines are decoration, not motion.** A static repeating gradient,
   `pointer-events: none`, never an animated flicker — nothing here should
   fight `prefers-reduced-motion` for a cosmetic effect.
4. **Uppercase, tracked headings** — terminal readouts, not a stylized logo.

## Signature details

- Scanlines are a fixed `::after` overlay on `.app` at `z-index: 999`
  with `pointer-events: none` — a 1px-on/2px-off repeating gradient, so
  they never intercept a click and never need JavaScript.
- All body text carries a faint `text-shadow: 0 0 3px` phosphor glow in its
  own colour (`currentColor` at 35%, so dim text glows dim), not
  just headings — the whole screen glows a little, not just the display
  face.
- `--success` and `--accent` are the *same* green — this theme has
  no separate "success" hue at all, only the one phosphor color and the
  two genuine hazard departures (danger amber, warning yellow).

## Layout

Minimal chrome, matching the terminal's own screen: a plain bar with a
green rule, content filling the frame, scanlines over the whole shell.

## Tell-tales of an inauthentic result

- A second hue appearing outside hazard states.
- Filled, solid buttons — the Pip-Boy draws in outline.
- An animated flicker — static scanlines only.

## v5 layout

Tiers (core): mobile ≤480px, tablet 481–900px, desktop 901–1800px, XL ≥1801px (shell capped at 1800px, centred). No rail. Phone and tablet use the core two-line bar. The scanline overlay now sits just under the modal layer (`--z-modal` − 1), not at a literal 999. On XL the gutters show the MAP tab with the lamp turned down: a world graticule and scattered location pips in dim phosphor (about 1.0:1).

## Icons

`themes/pipboy/icons.svg` redraws all 178 core icons as monochrome CRT
pictograms. No Vault Boy, Vault-Tec or other franchise marks are used.

- 24×24 grid. Every vertex sits on the integer grid. `shape-rendering="crispEdges"`.
- Chunky line: 2px stroke, square caps, miter joins, `currentColor` only (one phosphor hue).
- Curves are faceted to flat-sided octagons, and rounded corners become 2px
  chamfers. Dots are square pixels (2×2 or 3×3).
- Dense glyphs are simplified so they still read at 16px: accessible,
  discount, disc, coin, network, cpu, thermometer, temperature, file-zip,
  fingerprint, invoice, device-watch and map-question.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
