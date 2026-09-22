# Barbie

> Hot-pink glamour — glossy pill chrome, gold sparkle, all-caps confidence.

## What this theme is trying to achieve

The **Barbie brand aesthetic**: hot pink as the dominant color, not an
accent; everything glossy, rounded, and a little oversized, like packaging
for a toy rather than a productivity tool. The target is "confident and
glamorous," not "pastel and quiet" — this theme is loud on purpose.

## Core values

1. **Pink is the substrate.** `--ftl-accent` carries the whole identity;
   it shows up on every button, every active state, every header. A
   version of this theme with a muted or desaturated pink has missed the
   point.
2. **Round, everywhere, generously.** `--ftl-radius: 1.4rem`, pill buttons,
   pill badges, pill sliders. Nothing here has a hard corner.
3. **Gloss over flat.** Every filled surface gets a light highlight band —
   the same "shiny plastic" cue as the button chrome, panels, and the app
   bar. Losing the highlight reads as a cheaper, flatter knockoff.
4. **Gold is the sparkle, not the workhorse.** `--ftl-flare` (gold) shows
   up in heading glow only — it's the tiara, not a token you build
   components out of.
5. **Deep pink text, not black.** Body text is `#7a1250`, a pink-shifted
   dark plum — legible, but never plain black, which would read as a
   generic light theme wearing a pink accent.

## Signature details

- Headings are uppercase with a gold glow, the poster-title voice.
- The accent (`#c81b7a`) is one step darker than "true" Barbie Pink
  (`#e0218a`) — purely because the true value fails 4.5:1 against white
  button text; it's the minimum shift that clears the floor while still
  reading as the same pink.
- Success state uses Barbie mint (`#3ddc97`) with dark text, not a generic
  green with white text — mint is too light for white to pass, and a
  generic green would clash with the palette.

## Layout

The app shell becomes a **glossy pink ribbon**: a rounded pink gradient
bar on top, a matching sparkle-gradient status strip on the bottom, and a
soft pale-pink backdrop (`radial-gradient`) that makes the white content
card in the middle pop — box art, not a dashboard.

## Tell-tales of an inauthentic result

- Pastel/muted pink instead of the saturated hot pink.
- Sharp corners on any button, panel, or badge.
- Plain black body text.
- A generic green success state instead of the mint/dark-text pairing.

## Adoption

This theme sets `--ftl-app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.ftl-app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.

Requires: L1 — the app shell (`.ftl-app-*`) markup is needed for the
intended layout; at L0 the bundle renders recolored only.
