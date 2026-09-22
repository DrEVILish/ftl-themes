# Material

> Google Material Design — flat color, layered elevation shadows.

## What this theme is trying to achieve

**Google's Material Design language (MD2 era)**: bold flat color, no
gradients, and depth expressed entirely through a layered "elevation"
shadow system instead of gloss or bevel. Paper that lifts off the page,
not plastic or glass.

## Core values

1. **Elevation, not gloss.** Depth comes from `box-shadow` stacks at
   increasing "dp" levels (resting vs. hover vs. modal) — never a
   gradient fill. This is the deliberate contrast point against
   `aqua`/`winxp-luna`'s gloss and `win7-aero`'s blur: three different
   answers to "how does this surface show depth."
2. **Flat fills, bold color.** `--ftl-accent` is a saturated flat purple,
   painted solid — no gradient, no gloss highlight.
3. **Underlined text fields.** Inputs have no box border, only a 2px
   underline that goes solid accent on focus — the Material text-field
   convention, distinct from every boxed-input theme in the catalog.
4. **Uppercase button labels.** Buttons set their text
   `text-transform: uppercase` with tracked-out letter-spacing — the MD2
   button-label voice.
5. **The app bar is a flat accent slab.** No gradient, no rule — just the
   accent color and its own elevation shadow lifting it above the content.

## Signature details

- Three elevation levels are visible: resting buttons/cards (dp2), hover
  (dp4), and the modal (dp16-ish, the heaviest shadow in the catalog).
- Primary buttons fill solid `--ftl-accent` with white text; secondary and
  ghost buttons drop the shadow entirely — Material's "text button" and
  "outlined button" variants have no elevation.
- Selected/active table rows tint with a translucent accent wash rather
  than a hard fill, keeping to flat-color discipline.

## Layout

The shell keeps the page background flat and puts all its depth into the
**app bar**, which floats above the content on its own elevation shadow —
no border, no gradient, just color and shadow.

## Tell-tales of an inauthentic result

- Any gradient or gloss highlight on a button or panel.
- Boxed (bordered-on-all-sides) text inputs instead of the underline.
- Title-case or lowercase button labels instead of tracked uppercase.
- A flat, shadowless app bar — the elevation is the point.

## Adoption

This theme sets `--ftl-app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.ftl-app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.

Requires: L1 — the app shell (`.ftl-app-*`) markup is needed for the
intended layout; at L0 the bundle renders recolored only.
