# Windows 7 Aero

> Frosted glass and soft blue gloss — more restrained than Luna.

## What this theme is trying to achieve

**Windows 7's Aero Glass**: translucent, blurred window chrome over the
Aero blue desktop gradient, rounded corners, and a calmer, cooler gloss
than XP's opaque plastic. The generation that replaced "shiny" with
"glass."

## Core values

1. **Glass, not plastic.** Every chrome surface is translucent and
   genuinely blurred (`backdrop-filter`), not just a lighter opaque fill.
   An Aero theme with no blur is a `winxp-luna` palette swap wearing this
   theme's name.
2. **Restraint over Luna's saturation.** The blue is cooler and less
   saturated than Luna's `#0054e3`; gloss highlights are soft edges, not
   hard gradient stops.
3. **The desktop shows through.** Content areas are semi-transparent over
   the Aero blue gradient backdrop — the window is a pane of glass over
   the desktop, not an opaque card floating on it.
4. **Rounded, not sharp.** `--ftl-radius: 6px` — softer than Luna's 8px
   pill-adjacent buttons, closer to a subtle window-corner round.
5. **Light theme discipline.** Filled primary buttons need explicit white
   text (`--ftl-on-accent`), same reasoning as every light theme in this
   catalog.

## Signature details

- Buttons, panels, modals, the nav bar, and the toolbar all carry a real
  `backdrop-filter: blur(8px) saturate(1.4)` — this is the one CSS
  property that makes "glass" read as glass instead of "translucent gray."
- The app bar and status strip blur even harder (10px) and get an inset
  top highlight, the glass-edge catch-light.
- The page backdrop is the Aero blue gradient, not a flat color — glass
  needs something behind it worth seeing through.

## Layout

The shell becomes a **floating glass window**: a blurred, rounded title
bar, a near-transparent content well, and a frosted taskbar-style status
strip, with the Aero blue desktop gradient visible behind and through all
of it.

## Tell-tales of an inauthentic result

- No `backdrop-filter` anywhere — an opaque theme with a blue accent is
  `winxp-luna`, not this.
- A solid, non-transparent content background.
- Saturated Luna-blue instead of Aero's cooler, calmer tone.
- A flat page backdrop instead of the desktop gradient.

## Adoption

This theme sets `--ftl-app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.ftl-app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.

`backdrop-filter` support: this theme degrades gracefully in engines
without it — surfaces fall back to their plain translucent color with no
blur, still legible, just not glassy.

Requires: L1 — the app shell (`.ftl-app-*`) markup is needed for the
intended layout; at L0 the bundle renders recolored only.
