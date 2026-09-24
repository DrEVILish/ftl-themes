# Windows Media Player 11

> Black glass with a cool blue glow — WMP11's signature skin.

**Requires: L1** — sets `--ftl-app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

**Windows Media Player 11's black-glass skin**: a dark translucent chassis,
cool blue illumination from beneath the controls, and softly rounded glass
panels. The Vista-era "glass" idiom done in its most restrained form.

## Core values

1. **Glass, not solid.** Surfaces are translucent gradients with a blur
   behind them. A fully opaque panel loses the idiom.
2. **Light comes from below.** Blue glow sits under controls and behind the
   bar — the player is lit from inside.
3. **Cool blue only.** `#3fa9f5`/`#7fd1ff`. Warmth anywhere reads as a
   different era.
4. **Generously rounded.** `--ftl-radius: 0.8rem` — glass panes have soft
   edges, unlike WinAmp's hard chassis.
5. **Restraint.** Vista glass is easy to overdo; the bloom should be
   noticeable only in motion and on hover.

## Signature details

- The top bar and status strip both carry a real `backdrop-filter` blur,
  plus a visible cool-blue backlight glow along their edge — the chassis
  is lit from inside, not just tinted.
- Panels and the modal carry a genuine specular highlight band across
  their upper half (a bright-to-transparent gradient layer), the actual
  glossy-glass reflection, not just a faint ambient shadow — that band is
  what makes the idiom read as glass at a glance instead of as a plain
  dark panel with a blue border.
- Buttons are a dark top-lit gradient that gains a strong blue halo on
  hover.
- The round GO button carries the same idea at its most concentrated: a
  bright convex highlight cap over its top half plus a wide blue bloom —
  WMP11's single most recognizable lit element.
- Semantic variants keep gradient fills so danger/success still read
  against the neutral glass base button.
- The slider thumb glows — the volume/seek control is the lit part.

## Layout

The shell becomes a **glass stack**: 0.6rem padding, a rounded blurred bar,
a translucent rounded content well, and a rounded glass status strip,
floating over the radial backdrop.

## Tell-tales of an inauthentic result

- Opaque panels → the glass is gone.
- Warm or saturated accent colours.
- Sharp corners.
- Glow on everything rather than on hover and the active control.

## Adoption

This theme sets `--ftl-app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.ftl-app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
