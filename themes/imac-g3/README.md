# iMac G3

> Translucent ribbed plastic in Bondi Blue, with Blueberry/Grape/Tangerine variants.

## What this theme is trying to achieve

The 1998 iMac's defining trick: consumer electronics as candy. Translucent
coloured plastic over a light gloss highlight, rounded everything, and a
sense that the interface is a physical object you could pick up.

## Core values

1. **Gloss is a highlight band, never a flat sheen.** A light-to-dark
   gradient with a bright top edge, the same trick Aqua uses, but with the
   base colour itself translucent rather than metal.
2. **Every colorway is the same shape.** The plastic case comes in four
   colours; the case itself never changes. Only tokens change between
   variants — gloss, radius and pinstripe rules are shared once.
3. **Big, round, friendly.** `--ftl-radius: 1.3rem`. Nothing here is sharp.
4. **White text on saturated colour**, always — this is a light-on-dark
   theme regardless of which fruit colour is active.

## Variants

Bondi Blue is the default (no attribute needed). Select the others with
`data-variant` on `<html>`:

| Variant | `data-variant` |
|---|---|
| Bondi Blue | *(default)* |
| Blueberry | `blueberry` |
| Grape | `grape` |
| Tangerine | `tangerine` |

A lighter option — an **accent swatch** picker (`data-accent="1..4"`) —
recolours only the accent, not the whole shell, for an app that wants a
color pick without a full theme change.

## Layout

The shell reads as **one plastic case**: a glossy rounded top bar, a
pinstriped body, and a rounded status foot — all one continuous rounded
shape (`0.75rem` outer padding, `1.3rem` corners top and bottom), floating
on a radial vignette of its own colour.

## Tell-tales of an inauthentic result

- A flat, opaque fill anywhere → the plastic stops reading as translucent.
- Sharp corners.
- A colorway that changes gloss or radius, not just palette tokens — the
  case is one shape in four colours, not four different cases.

## Adoption

This theme sets `--ftl-app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.ftl-app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.

Requires: L1 — the app shell (`.ftl-app-*`) markup is needed for the
intended layout; at L0 the bundle renders recolored only.
