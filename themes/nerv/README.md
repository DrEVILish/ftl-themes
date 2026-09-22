# NERV Terminal

> Industrial military-alert styling — deep black, hazard orange, dark crimson.

**Requires: L1** — sets `--ftl-app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

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
3. **Sharp, stencilled, uppercase.** `--ftl-radius: 0`; tracked uppercase
   headings; a bold, geometric font stack.
4. **Thick rules.** 2–3px borders and bars, not hairlines — a bunker's
   markings are painted, not printed.

## Signature details

- Danger buttons alone get a `repeating-linear-gradient(135deg, ...)`
  hazard-stripe fill instead of a flat color — the theme's single
  decorative flourish, reserved exclusively for that one state.
- The active-row marker is crimson (`--ftl-danger`) even though every
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

## Adoption

This theme sets `--ftl-app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.ftl-app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
