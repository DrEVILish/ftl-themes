# WinAmp Classic

> Steel-gray skinned player — tiny caps, llama-green readouts.

## What this theme is trying to achieve

A **skinned desktop media player** from the late 1990s: a compact steel
window, brushed horizontal texture, tiny uppercase labels, and a bright
green LCD-style readout. It really whips the llama's ass.

## Core values

1. **Small, tight, compact.** This is a player window that lives in a
   corner of the screen, not a full-page app. Type is small; the title bar
   is 1.8rem.
2. **Steel texture, not flat grey.** A 4px repeating horizontal gradient
   gives the brushed-metal body.
3. **The readout is green-on-black.** Track info and values set in the
   monospace face on true black — an LCD panel inset into the chassis.
4. **Beveled hardware.** Like Windows 95 but subtler: 1px two-tone borders,
   inverted on press.
5. **Uppercase micro-labels.** Buttons are tiny caps, as on the original's
   transport row.

## Signature details

- Inputs are black with green monospace text — they read as the display,
  not as form fields.
- Sliders are square-thumbed with a llama-green cap.
- The status strip repeats the chassis gradient, framing the window.

## Layout

The shell is a **player window**: 0.25rem outer padding, a 1.8rem beveled
gradient title bar, a bordered inset content area, and a gradient footer.
Everything is snug against everything else.

## Tell-tales of an inauthentic result

- Large comfortable type → a modern music app, not a skin.
- Flat grey with no texture.
- Green used as a general accent rather than confined to readouts.
- Rounded corners anywhere.

## Adoption

This theme sets `--ftl-app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.ftl-app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.

Requires: L1 — the app shell (`.ftl-app-*`) markup is needed for the
intended layout; at L0 the bundle renders recolored only.
