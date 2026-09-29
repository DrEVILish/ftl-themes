# Vaporwave

> Outrun synthwave — magenta/cyan grid horizon on deep purple.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

**80s-retrofuturist outrun aesthetics**: hot magenta and electric cyan
gradients over a deep purple void, chrome-gradient text, and a perspective
grid horizon — the sunset-and-grid album-cover look, not a clean sci-fi
HUD.

## Core values

1. **Two hues, always together.** Magenta (`--accent`) and cyan
   (`--accent-2`) appear as a pair — gradients between them, not either
   color alone as a single accent. A version of this theme using only one
   has missed the point.
2. **Chrome text.** Headings are a magenta-to-cyan gradient clipped to the
   glyphs (`background-clip: text`), the genre's signature title treatment
   — not a solid color.
3. **Glow over grid-lines, not a clean HUD.** This is the deliberate
   contrast point against `tron`: tron is a crisp cyan grid on black with
   sharp edges; this is soft glow, saturated gradient fills, and a
   perspective horizon, not straight technical lines.
4. **Purple is the void.** `--bg`/`--surface` are deep purple, not
   black — black reads as `matrix`/`alienware`, not synthwave.
5. **The horizon lives in the status strip.** The perspective grid-floor
   pattern belongs to the bottom of the shell, echoing the genre's classic
   sunset-over-grid composition.

## Signature details

- `h1`/`h2`/`h3` use a clipped gradient fill rather than a solid color —
  the one detail that reads "synthwave" before anything else does.
- Buttons default to the magenta-to-cyan gradient fill; `--on-accent`
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

## Don'ts

- **No flat single-colour headings.** The magenta-to-cyan gradient clipped to the glyphs is the signature; a solid pink `h1` reads as a generic dark theme.
- **No warm neutrals.** Greys and blacks lean purple (`#1a0b2e`, `#241242`); pure `#000` or neutral grey breaks the void.
- **No lowercase, tight-tracked display type.** Headings are uppercase with `0.14em` tracking.
- **No more than the pink/cyan pair** doing the loud work; extra hues dilute it.
- **No dense, corporate layout.** Space and horizon matter more than information density.

## Typography

- **Display (h1–h3):** Audiowide, **vendored** (`assets/fonts/Audiowide-Regular.woff2`, SIL OFL, `assets/fonts/NOTICE.md`), uppercase, `0.14em` tracking, under the gradient-text fill. It is the "wide, chunky geometric" stand-in for vaporwave's extended display type; it is not a true full-width face.
- **Body:** `--font` is `"Segoe UI", Verdana, sans-serif` — system fonts, **not vendored**. `--font-mono` is `Consolas, monospace`.
- **Full-width Latin and katakana:** the aesthetic leans on full-width text (ＶＡＰＯＲ) and Japanese katakana, but the theme ships no face for either. Audiowide is a Latin display face; whether the vendored file covers full-width forms or katakana was not checked, so treat both as system-font fallback (`--font`, then the OS's CJK font). Put katakana in body-weight text or set an explicit CJK `font-family` in the app; do not expect Audiowide to render it. `RESEARCH.md` lists the mall/katakana-text target as still uncovered by the captures.

## Contrast honesty

- **Danger lifted:** the reference "hot" red-pink `#ff3864` is 3.5:1 under white; shipped `--danger` is `#d81c48` (5.02:1 with white text, 3.69:1 as text on `--bg`, so text uses `--danger-text`).
- **Border:** `--border` `#8a5fc0` is picked to be ~3.6:1 against `--surface` (the least that keeps a 1px outline perceptible while staying purple).
- **Accent pair:** `--accent` `#ff71ce` is 7.52:1 on `--bg` (6.86:1 on `--surface`); `--accent-2` `#01cdfe` is 9.87:1 / 9.0:1. The gradient headings therefore pass on every stop; the neon values themselves are not lifted.
- **Nav bar:** the bright pink-purple-cyan bar makes the default nav colours near-invisible. Dark `#1a0b2e` text clears 5.7:1 at the mid-purple stop, but reads weakly on a busy gradient, so a light text-shadow halo is added (math passes; the halo is for perceived contrast).
- `--muted` `#b79ee0` is 7.24:1 on `--surface`.

## Reference status

`references/vaporwave/` has 4 captures plus `RESEARCH.md`: all grid-horizon/sunset scenes (wireframe mountains, palms, cityscape); `Vaporwave.webp` is a sun over wireframe mountains, not a statue. They back the perspective grid floor, the sunset bar and the pink/cyan-on-purple palette. `RESEARCH.md` names two uncovered targets: the statue-glitch motif and the mall/katakana-text scenes, so nothing in the folder backs the theme's typography choices. No hex values are recorded; only the `#ff3864` "hot" red-pink is cited in `theme.css`.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
