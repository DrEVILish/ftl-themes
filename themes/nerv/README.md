# NERV Terminal

> Industrial military-alert styling — deep black, hazard orange, dark crimson.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

A command-bunker terminal under permanent alert status: black steel,
stencilled orange warnings, and crimson reserved for the moment something
is actually wrong.

## Core values

1. **Orange is "operational alert" — always on, never urgent.** It is the
   accent, the border colour, the heading colour. It marks that this
   terminal is a war-room fixture, not a calm state.
2. **Crimson is reserved for danger alone**, and gets the one decorative
   flourish in the theme: diagonal hazard stripes on destructive actions.
3. **Sharp, stencilled, uppercase.** `--radius: 0`; tracked uppercase
   headings; a bold, geometric font stack.
4. **Thick rules.** 2–3px borders and bars, not hairlines — a bunker's
   markings are painted, not printed.

## Signature details

- Danger buttons alone get a `repeating-linear-gradient(135deg, ...)`
  hazard-stripe fill instead of a flat color — the theme's single
  decorative flourish, reserved exclusively for that one state.
- The active-row marker is crimson (`--danger`) even though every
  other structural accent in the theme is orange — the one place danger's
  color, not orange, gets to mark something.
- Headings carry `letter-spacing: 0.15em`, the widest tracking in the
  catalog — a stencilled, painted-on-metal feel rather than a printed one.

## Layout

A black bar and status strip both edged in a thick orange rule — the
terminal's own frame — with the content area reading as the screen set
into that frame.

## Tell-tales of an inauthentic result

- Orange used sparingly, as an accent among others → this palette runs
  orange-forward everywhere.
- Hazard stripes anywhere other than a destructive action.
- Thin, quiet borders — NERV's markings are bold.

## v5 layout

Tiers (core): mobile ≤480px, tablet 481–900px, desktop 901–1800px, XL ≥1801px (shell capped at 1800px, centred). No rail. Phone and tablet use the core two-line bar. A panel nested in another box drops to a 1px dim-orange rule, so stacked boxes read as compartments rather than three full-strength frames. On XL the gutters show the MAGI hex field: a triangle lattice in dim hazard orange (about 1.0:1).

## Icons

`icons.svg` draws the core set as emergency-terminal glyphs (no NERV or studio marks).

- **Grid and weight.** 24 grid, heavy 2.4px line, square caps, mitred joins, hard corners (radius 0).
- **Geometry.** Every circle is a flat-top hexagon (the MAGI hex motif); curves are rebuilt as angular runs; silhouettes are solid fills; marker dots are solid squares.
- **Condensed.** Each glyph is squeezed to 86% width by a wider `viewBox` with `preserveAspectRatio="none"`, like condensed stencil type. This also makes vertical strokes 0.86x the width of horizontal ones, which is not visible at 2.4px.
- Generated from one shared 24-grid geometry, so every core-set id (178/178) is drawn; everything uses `currentColor`, so icons follow text, accent and selected states (and every variant) with no hard-coded colour.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
