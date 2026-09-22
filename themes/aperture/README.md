# Aperture Science

> Sterile laboratory off-whites and dark greys, accented by testing-chamber blue and orange.

## What this theme is trying to achieve

A clean, sterile test-chamber control panel: off-white surfaces, quiet
grey structure, and the two portal colours — blue and orange — used
exactly where the reference used them, as the only saturated colours in an
otherwise clinical space.

## Core values

1. **The first light theme in this batch of clinical calm.** Off-white,
   not stark white — `--ftl-bg`/`--ftl-surface` sit a shade apart so
   surfaces read as physical panels, not a blank page.
2. **Blue is primary/interactive; orange is the second portal, reserved
   for destructive actions** — a direct, deliberate swap of the usual
   red-for-danger convention, because orange is what the reference uses
   for its second state.
3. **No decoration.** Flat fills, quiet 1px borders, small shadows. This is
   institutional software, not a HUD.
4. **Grey, understated headings** — a section label on a clipboard, not a
   marketing headline.

## Layout

A plain white bar and status strip on a slightly darker page backdrop —
the panel sits in the room rather than filling it.

## Tell-tales of an inauthentic result

- Red used for danger instead of orange → loses the portal-colour logic.
- Any glow, gradient or heavy shadow — this is the calmest theme in the
  catalogue by design.
- Saturated colour anywhere except the two accents.

## Adoption

This theme sets `--ftl-app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.ftl-app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.

Requires: L1 — the app shell (`.ftl-app-*`) markup is needed for the
intended layout; at L0 the bundle renders recolored only.
