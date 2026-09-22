# Vaporwave

> Outrun synthwave — magenta/cyan grid horizon on deep purple.

## What this theme is trying to achieve

**80s-retrofuturist outrun aesthetics**: hot magenta and electric cyan
gradients over a deep purple void, chrome-gradient text, and a perspective
grid horizon — the sunset-and-grid album-cover look, not a clean sci-fi
HUD.

## Core values

1. **Two hues, always together.** Magenta (`--ftl-accent`) and cyan
   (`--ftl-accent-2`) appear as a pair — gradients between them, not either
   color alone as a single accent. A version of this theme using only one
   has missed the point.
2. **Chrome text.** Headings are a magenta-to-cyan gradient clipped to the
   glyphs (`background-clip: text`), the genre's signature title treatment
   — not a solid color.
3. **Glow over grid-lines, not a clean HUD.** This is the deliberate
   contrast point against `tron`: tron is a crisp cyan grid on black with
   sharp edges; this is soft glow, saturated gradient fills, and a
   perspective horizon, not straight technical lines.
4. **Purple is the void.** `--ftl-bg`/`--ftl-surface` are deep purple, not
   black — black reads as `matrix`/`alienware`, not synthwave.
5. **The horizon lives in the status strip.** The perspective grid-floor
   pattern belongs to the bottom of the shell, echoing the genre's classic
   sunset-over-grid composition.

## Signature details

- `h1`/`h2`/`h3` use a clipped gradient fill rather than a solid color —
  the one detail that reads "synthwave" before anything else does.
- Buttons default to the magenta-to-cyan gradient fill; `--ftl-on-accent`
  is dark purple, not white, since the gradient is bright enough that dark
  text is what actually passes the contrast floor.
- The app bar is the full three-stop sunset gradient (magenta → purple →
  cyan); the status strip carries a horizon-line grid pattern instead.
- Danger is one step darker than the "hot" reference red-pink — the
  literal value fails 4.5:1 against white button text.

## Layout

The shell becomes an **outrun horizon**: a gradient sunset bar on top, a
perspective grid-line floor in the status strip at the bottom, and the
deep-purple void filling the content well between them.

## Tell-tales of an inauthentic result

- Only one of magenta/cyan used, the other dropped.
- Solid-color headings instead of the clipped gradient.
- Black instead of deep purple as the base color.
- Crisp, straight grid-lines everywhere (that's `tron`, not this).

## Adoption

This theme sets `--ftl-app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.ftl-app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
