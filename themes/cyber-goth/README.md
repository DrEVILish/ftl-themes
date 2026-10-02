# Cyber-Goth

> Pitch-black club aesthetic with toxic neon green, hot purple and vinyl gloss.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

The club-kid cyber-goth look: black vinyl surfaces, UV-reactive neon green
against hot purple structure, and a glow that reads as blacklight rather
than as a HUD's telemetry glow.

## Core values

1. **Purple structures, green signals.** `--flare` (purple) is the
   theme's borders, rules and headings; `--accent` (toxic green) is
   reserved for primary/interactive/success — the two must not swap roles.
2. **Black vinyl gloss, not matte.** Panels and buttons carry a subtle
   top-lit gradient — plastic under a club light, not flat paint.
3. **Glow is UV bloom.** Hover/focus glows are wide and colour-matched to
   whichever hue is glowing, not a tight HUD ring.
4. **Uppercase, geometric type** — flyer/rave typography, not corporate
   sans.
5. **Spiked, studded-leather chrome, not just neon-on-black.** Colour
   alone doesn't distinguish this from any other neon cyberpunk theme in
   the catalog — a jagged sawtooth trim on every structural bar and a
   hard-edged, riveted drop-shadow on buttons/panels are the theme's own
   silhouette, legible even in a colourless crop.

## Signature details

- Primary buttons' hover glow (`0 0 14px rgba(214, 31, 255, 0.6)`) is
  purple even though the button fill is green — the bloom always reads as
  the *structural* colour, never the signal one.
- Table headers and rules pick up `--flare` (purple), not the accent —
  structure stays purple everywhere, including inside components.
- A jagged sawtooth trim (a repeating 45°/-45° gradient pair, the classic
  "torn ticket edge" CSS technique) runs along the app bar, nav, and
  panel/modal headers — a studded-collar silhouette, not a smooth bevel
  like `alienware`'s clip-path corners and not `matrix`'s monospace rain.
  It's a decorative pseudo-element strip, so it never clips a focus ring,
  click target or label.
- Buttons carry a single asymmetric fang cut on the top-right corner only
  (`clip-path`) plus a hard black offset shadow underneath the neon
  bloom — riveted vinyl, not a soft glow alone. `alienware` cuts both
  opposing corners at matching size; this cuts one corner, deliberately
  uneven.
- The font stack leads with Eurostile, the same unvendored-face situation
  as `tron`/`death-star` — it silently falls back to a system sans on most
  real machines rather than the intended geometric face.

## Layout

A black bar and status strip both edged in the purple rule, with the
content area carrying the same vinyl-gloss panels throughout.

## v5 layout

- **Tiers.** No rail on any tier. On phone and tablet (≤900px) the nav
  gets its own scrolling line in the bar; its own sawtooth is dropped
  there (the scroller clipped it, and the bar's sawtooth already edges the
  whole bar).
- **Nesting.** A panel inside another surface gets a smaller, unlit
  sawtooth. Headers leave a wider gap below them so the teeth never touch
  the first line of the body.
- **XL gutter art.** The club wall beside the console: a fishnet lattice in
  dark violet with a faint sawtooth trim running down each side. Still,
  and within about 1.2:1 of `--bg`.

## Tell-tales of an inauthentic result

- Purple and green swapping jobs (purple as the primary action colour, or
  green as structure) → the two-colour logic collapses.
- Flat matte surfaces — this is glossy plastic, not a terminal.
- A tight, thin glow instead of a soft bloom.
- No sawtooth trim / no hard-edged studded shadow — without it this is
  just another neon-on-black palette, indistinguishable from any other
  cyberpunk theme in the catalog.

## Don'ts

- **No swapping of roles.** Purple is structure; green signals. Never a purple primary action or green borders.
- **No third neon colour.** Danger and warning exist for states only.
- **No matte flat panels.** Keep the top-lit vinyl gradient, sawtooth trim and hard offset shadow.
- **No smooth bevels or soft glows alone**; the fang cut and riveted shadow carry the silhouette.
- **No lowercase, corporate sans headings.**

## Typography

`--font` is `"Eurostile", "IBM Plex Sans", sans-serif`; `--font-mono` is `Consolas, monospace`. **Neither named face is vendored**: Eurostile is a commercial face, IBM Plex Sans only renders if installed, so on most machines the generic sans-serif is what shows. Headings are uppercase and geometric by CSS (case and tracking), not by the face. `references/cyber-goth/cyber-goth-neon-sign-typography.jpg` shows tube-letterform construction that no web font reproduces, so the theme does not try.

## Contrast honesty

- **Neon green on black is far above the floor:** `--accent` `#b6ff1a` is 17.15:1 on `--bg`, 16.41:1 on `--surface`; `--on-accent` `#0a0f00` is 16.01:1 on it.
- **Purple:** `--accent-2`/`--flare` `#d61fff` is 5.45:1 on `--bg`, 5.21:1 on `--surface`; `--border` `#7a1fbf` is only 2.75:1 on `--surface` (a structural line, not text).
- **Danger:** `--danger` `#d61048` is 3.99:1 as text on `--bg` (fails), so copy uses `--danger-text` `#f03d70`; the fill takes white text at 5.21:1.
- **Muted** `#9d7ec2` is 5.87:1 on `--surface`.
- **Why purple exists at all.** The captures show a single green UV-reactive neon (`cyber-goth-el-wire-closeup.jpg`) on black; `RESEARCH.md`'s outsider read is "a single UV-reactive neon accent". The hot purple `#d61fff`/`#7a1fbf` structure is **not in any capture**. It is a design decision (blacklight club association, and to stop the theme reading as a green-only cousin of `matrix`), documented here rather than sourced. The hexes are unmeasured.

## Reference status

`references/cyber-goth/` has 5 captures plus `RESEARCH.md`: `cyber-goth-el-wire-closeup.jpg` (green EL wire on black, backs the neon-glow falloff and the single-neon idea), `cyber-goth-black-leather-texture.jpg` (backs the vinyl/leather base and its specular response), `cyber-goth-neon-sign-typography.jpg` (tube lettering on a dark wall), plus a cyberpunk-admin dashboard screenshot and a dev-to webp that `RESEARCH.md` calls off-direction. Honest gaps in `RESEARCH.md`: no true UV-blacklight photo, no mesh/rivet macro, so the sawtooth trim, fang cut and studs are not captured evidence.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
