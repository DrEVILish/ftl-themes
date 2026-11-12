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
   glyphs (`background-clip: text`), led by the references' hot pink
   `#ff2975` (5.2:1 on `--bg`) through `--accent` at 35% to `--accent-2`,
   the genre's signature title treatment — not a solid color.
3. **Glow over grid-lines, not a clean HUD.** This is the deliberate
   contrast point against `tron`: tron is a crisp cyan grid on black with
   sharp edges; this is soft glow, saturated gradient fills, and a
   perspective horizon, not straight technical lines. Panels and cards
   carry a pink edge ring plus, on fine-pointer screens, a pink-and-cyan outer bloom (`--panel-shadow`; phones skip the blur for scroll cost), `h1`/`h2` a soft
   pink drop-shadow (dropped on phones and touch screens, where the filter
   layer costs scroll frames), focus a cyan glow ring, and the slider track
   is the pink-to-cyan pair with a glowing thumb (bottom-to-top on a
   vertical fader, kept to the thin track).
4. **Purple is the void.** `--bg`/`--surface` are deep purple, not
   black — black reads as `matrix`/`alienware`, not synthwave.
5. **The horizon lives at the foot of the shell.** The status strip's top
   edge is the glowing horizon line, and the sun, pinned to the bottom of
   the viewport, sets directly on it at the page end; the perspective grid floor fills the
   strip below: the genre's classic sunset-over-grid composition, with no
   text ever sitting on the sun or on a grid line.

## Signature details

- `h1`/`h2`/`h3` use a clipped gradient fill rather than a solid color —
  the one detail that reads "synthwave" before anything else does.
- The magenta-to-cyan gradient marks what is primary or selected:
  `.btn-primary`, a checked `.toggle-btn` and an active `.segmented-item`
  get the gradient with dark `#1a0b2e` ink (7.5:1 / 9.9:1 on the stops).
  Plain buttons are the quiet `--surface-2` chip with a `--border` edge, so
  a range group (7d / 30d / 90d) shows which one is on.
- Title-bar caption controls (minimise, maximise, close, wrapped or not)
  are dark `#1a0b2e` ink on the gradient header with a soft dark hover
  wash; no grey bevel.
- The app bar is the sunset gradient (orange → magenta → purple → cyan).
  Panel and card headers carry it too, as a 2px rule on their bottom edge
  over a faint magenta wash (`--panel-header-bg`).
- Alerts tint their fill with their tone at 12% (`color-mix` over
  `--surface-2`) as well as the edge, so the four states differ at a glance.
- A disabled button is a flat `--surface-2` chip with a dashed `--border`
  edge and `--muted` ink, never a dimmed gradient that could read as the
  selected primary.
- The horizon: a gold-to-magenta setting sun
  (`#ffd319` → `#ff8c3a` → `#ff2975` → `#c800c8`, the references' sun),
  `min(12rem, 46vw)` wide, its upper half with five slits near the
  horizon, on a fixed layer (`body::after`) under the whole shell, so it is
  on screen at every scroll position and panels cover it. A second fixed
  layer (`body::before`) is the magenta haze and warm glow over the bottom
  45vh of the viewport, so the sunset warmth is above the fold. The well
  itself is transparent onto `--bg`, so a long page repaints nothing on
  scroll. The sun's base sits 3.9rem (a status strip) above the viewport
  bottom, so at the page end it sets right on the strip; the well's bottom
  padding is the sun's height plus 0.75rem, so no content sits on it there.
  While content can still scroll over it the sun is dimmed to 0.3 (text
  over it keeps its contrast); a scroll-driven animation
  (`animation-timeline: scroll(root)`) brings it to full strength over the
  last 10% of scroll, and a page that does not scroll shows it at full
  strength. Browsers without scroll timelines keep it at 0.3. The status
  strip is pulled up over the grid gap and its top rule is the glowing pink
  `#ff2975` horizon. Below, the floor fills only the strip's 2.4rem bottom
  padding band (sized in rem, not %, so a taller strip never puts a line
  behind its text), with no 3D transform: cyan rays (0.85 alpha,
  soft-edged `repeating-conic-gradient`) fanning from a vanishing point
  above the strip, and four pink cross-lines spaced wider toward the
  viewer, faded in from the band's top edge. A desktop taskbar
  (`.desktop-bar`) has no reserved band, so it keeps the horizon rule and
  drops the floor.
- Heading boxes hug their glyphs (`width: fit-content`; auto inline
  margins in core's centred `.hero`/`.band-head`/`.empty-state`/`.dropzone`
  and inline `text-align: center` blocks), so every title, however short,
  runs the whole magenta-to-cyan sweep. They carry 4px of padding inside
  the gradient box (with a matching negative margin, so layout is
  unchanged), so the glyphs never touch the painted edge.
- On phones (≤480px) only the brand row (2.75rem) keeps the sunset band,
  with dark brand ink; the wrapped nav rows below are the dark strip colour
  with light nav ink, so the wrapped bar is not a slab of gradient.
- Danger is one step darker than the "hot" reference red-pink — the
  literal value fails 4.5:1 against white button text.

## Icons

`themes/vaporwave/icons.svg` covers the full core icon set (178/178, plus
`sun-moon`) in clean geometric line work. It keeps the generic set's
24×24 grid, `fill="none"`, inherited `currentColor` stroke at the shared
`--icon-stroke-width`, and round caps and joins; no stroke width is baked
in. Forms are simplified toward pure geometry, for example straight
3→21 rules, spoked rather than toothed settings, and a crisper check. A
few ground or motion icons (home, folder, star, logout, refresh, cloud, map,
globe, plane, car, bus, road, rainbow) add the horizon cue: a pair of
short diagonal floor lines in the bottom corners
(`M2 22.5l4-2.4M18 20.1l4 2.4`, `stroke-width="1"`). Never put it on
every icon.

## Layout

The shell becomes an **outrun horizon**: a gradient sunset bar on top, a
perspective grid-line floor in the status strip at the bottom, and the
deep-purple void filling the content well between them.

## v5 layout

Tiers: mobile ≤480px, tablet 481–900px, desktop 901–1800px, XL ≥1801px (the shell is capped at 1800px and centred, with gutter art beside it).

- **Phone, tablet and desktop (≤1800):** core's shell. The fixed sunset (haze and sun, under the shell) is the same at every tier; the gradient bar, chrome headings and the status strip's horizon carry the rest. The old top-right sun-and-grid corner emblem is gone (its sun hung at the top of the sky, not on a horizon). Signage surfaces drop the sunset layers.
- **XL gutters (≥1801):** the outrun floor. A perspective grid recedes to a vanishing point behind the app (cyan rays from the screen centre, pink cross-lines spaced wider toward the viewer), so each gutter shows the floor sweeping in from the side. Still.

## Tell-tales of an inauthentic result

- Only one of magenta/cyan used, the other dropped.
- Solid-color headings instead of the clipped gradient.
- Black instead of deep purple as the base color.
- Crisp, straight grid-lines everywhere (that's `tron`, not this).

## Don'ts

- **No flat single-colour headings.** The magenta-to-cyan gradient clipped to the glyphs is the signature; a solid pink `h1` reads as a generic dark theme.
- **No warm neutrals.** Greys and blacks lean purple (`#1a0b2e`, `#241242`); pure `#000` or neutral grey breaks the void.
- **No lowercase, tight-tracked display type.** Headings are uppercase with `0.14em` tracking (`h3` card titles `0.08em` so they fit).
- **No more than the pink/cyan pair** doing the loud work; extra hues dilute it.
- **No dense, corporate layout.** Space and horizon matter more than information density.

## Typography

- **Big figures:** KPI values (`.stat-value`) and plan prices (`.price`) are Audiowide at weight 400 (it has no bold), `0.04em` tracking.
- **Chrome titles:** the bar brand, panel and modal headers, tabs, KPI labels (`.stat-label`), buttons and table heads also use Audiowide, uppercase, `0.06em` tracking, weight 400; tabs drop to `0.75em` and buttons to `0.8em` (`--btn-font-size`) so a strip or row keeps its width.
- **Display (h1–h3):** Audiowide, **vendored** (`assets/fonts/Audiowide-Regular.woff2`, SIL OFL, `assets/fonts/NOTICE.md`), uppercase, `0.14em` tracking (`0.08em` on `h3`), under the gradient-text fill. It is the "wide, chunky geometric" stand-in for vaporwave's extended display type; it is not a true full-width face.
- **Body:** `--font` is `"Segoe UI", "Trebuchet MS", Verdana, "DejaVu Sans", sans-serif` — system fonts, **not vendored**. `--font-mono` is `Consolas, monospace`.
- **Full-width Latin and katakana:** the aesthetic leans on full-width text (ＶＡＰＯＲ) and Japanese katakana, but the theme ships no face for either. Audiowide is a Latin display face; whether the vendored file covers full-width forms or katakana was not checked, so treat both as system-font fallback (`--font`, then the OS's CJK font). Put katakana in body-weight text or set an explicit CJK `font-family` in the app; do not expect Audiowide to render it. `RESEARCH.md` lists the mall/katakana-text target as still uncovered by the captures.

## Contrast honesty

- **Danger lifted:** the reference "hot" red-pink `#ff3864` is 3.5:1 under white; shipped `--danger` is `#d81c48` (5.02:1 with white text, 3.69:1 as text on `--bg`, so text uses `--danger-text`).
- **Border:** `--border` `#8a5fc0` is picked to be ~3.6:1 against `--surface` (the least that keeps a 1px outline perceptible while staying purple).
- **Accent pair:** `--accent` `#ff71ce` is 7.52:1 on `--bg` (6.86:1 on `--surface`); `--accent-2` `#01cdfe` is 9.87:1 / 9.0:1. The gradient headings therefore pass on every stop; the neon values themselves are not lifted.
- **Nav bar:** the bright orange-pink-purple-cyan bar makes the default nav colours near-invisible. Dark `#1a0b2e` text clears 5.7:1 at the mid-purple stop, but reads weakly on a busy gradient, so a tight light halo (`0 0 2px` white at 0.6) is added to the brand, nav items and breadcrumbs (math passes; the halo is for perceived contrast, kept crisp rather than an embossed glow). `#1a0b2e` is 8.0:1 on the orange stop.
- **Haze:** the well's darkest-lightest stop `#3d1250` still gives `--muted` 6.4:1 and `--danger-text` 5.0:1.
- `--muted` `#b79ee0` is 7.24:1 on `--surface`.

## Reference status

`references/vaporwave/` has 4 captures plus `RESEARCH.md`: all grid-horizon/sunset scenes (wireframe mountains, palms, cityscape); `Vaporwave.webp` is a sun over wireframe mountains, not a statue. They back the perspective grid floor, the sunset bar and the pink/cyan-on-purple palette. `RESEARCH.md` names two uncovered targets: the statue-glitch motif and the mall/katakana-text scenes, so nothing in the folder backs the theme's typography choices. `RESEARCH.md` records no hex values; the sun stops (`#ffd319`/`#ff8c3a`/`#ff2975`/`#c800c8`) were sampled from the captures, and the `#ff3864` "hot" red-pink is cited in `theme.css`.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
