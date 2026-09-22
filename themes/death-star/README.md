# Death Star Terminal

> Absolute black with glowing solid-colour indicator blocks, zero borders or shadows.

**Requires: L1** — sets `--ftl-app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

The Imperial control terminal aesthetic: a void of true black
punctuated only by solid-colour glowing indicator blocks — red, green,
blue — with no frame, border or shadow drawn anywhere to soften it.

## Core values

1. **Zero borders, zero shadows, zero radius.** Every panel/input/button
   border width is `0`. Structure comes only from solid fill against black.
2. **Indicators glow; everything else doesn't.** Only lamps and the focus
   ring carry any glow — restraint is what makes the glow read as a signal.
3. **Colour blocks are solid, not gradients.** A filled surface is one flat
   colour, full stop.
4. **True black, not near-black.** `--ftl-bg: #000`. This is the one theme
   in the catalogue that means it literally.

## Signature details

- Lamps carry a `0 0 10px` glow matched to their own state color
  (`.is-on` glows success-green, `.is-error` glows danger-red) — the only
  `box-shadow` this theme sets anywhere.
- Selected table rows fill solid accent blue with black text, not a tint —
  a "selected" row is a solid block, same discipline as everything else.
- Badges are square (`border-radius: 0`), overriding core's default pill —
  even the smallest decorative curve is stripped out here.

## Layout

No bar rule, no status rule — the bar and status strip are the same black
as the page, distinguished only by the content sitting on them.

## Tell-tales of an inauthentic result

- Any visible border on a panel, button or input.
- A gradient fill anywhere.
- A near-black (`#0a0a0a`-ish) background instead of true `#000`.

## Adoption

This theme sets `--ftl-app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.ftl-app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
