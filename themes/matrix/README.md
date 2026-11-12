# The Matrix

> Green phosphor on black — monospace terminal cascade.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

A **phosphor terminal** as filmed: monospace everything, black field,
green text with a faint bloom, and the sense that you are reading a machine
directly rather than an interface built for you.

## Core values

1. **Monospace is non-negotiable.** Every element, not just values.
2. **Green is the only colour with a job.** Semantic red exists for genuine
   errors and nothing else. Introducing a second decorative hue breaks the
   single-phosphor illusion. Warning is the white-hot head glyph `#e8ffe0`,
   `--accent-2` is a lighter green `#7dff9a`, and the six chart series are
   brightness steps of the one green.
3. **Bloom, not glow.** A 2px text-shadow across all text imitates
   phosphor persistence. It is deliberately subtle — a strong glow reads as
   neon, which is a different aesthetic entirely.
4. **Outline over fill.** Base controls are transparent with a green rule.
   Only semantic variants take a fill, so a delete button still reads as
   dangerous.
5. **Uppercase headings, tracked.** Terminal banner conventions.
6. **Hard rectangles.** Badges, filter chips, switches, slider thumbs,
   icon buttons, avatars, carousel arrows and dots, and checkboxes are
   square terminal cells, never capsules or discs (radios stay round).

## Signature details

- **The digital rain**: real glyph columns filling the frame top to bottom,
  mixing mirrored digits and capitals with katakana-like stroke glyphs drawn
  as SVG paths (about a third of the near layer's cells), each streak a
  bright `#00ff41` tail (full strength from 40% of its length) ending in a
  white-hot head with a doubled green blur glow, plus faint
  residual glyphs between streaks, at uneven column pitch. Two SVG tiles
  with coprime widths, so the wall never visibly repeats: a near 997px tile
  at 14px on `html::after` (layer opacity 1) and a far 613px, dimmer
  text-only tile at 10px on `body::before` (0.5; dropped on touch screens to keep the frame
  budget). Streaks wrap across the
  tile's bottom edge, so the loop has no seam. Each layer falls by `transform: translateY` of one
  tile height (13s and 19s), so it loops seamlessly and composites rather
  than repainting (both layers carry `will-change: transform`). With reduced motion the columns stand still.
- Light text carries the bloom plus a black halo (2px twice, then 8px), so
  glyphs standing on the rain have a dark moat; a bare `aside` standing on
  the rain also gets an 80% black backing, at zero class specificity so a
  drawer or panel keeps its own fill. The halo's alpha is
  computed from the text's own lightness (relative colour from
  `currentColor`), so dark labels on lit fills get none; controls keep
  bloom only.
  The content well is a 35% black wash over the rain, so the code wall
  stays bright between panels; panels and tables
  are opaque.
- Panel rules are a lit `#1a9a2a` with a 24px inward glow; modals, toasts
  and alerts get the SYSTEM FAILURE double rule (black gap, then a 1px lit
  line, in the alert's state colour). The app bar and panel headers carry
  the operator console's ruled LCD plate: faint 3px phosphor scanlines.
- Checkboxes and radios are drawn as green-ruled cells (phosphor fill and
  black tick when checked); the slider track is the lit rule colour (in Firefox the part up to
  the thumb lights `#00ff41`). The bar chart's highlighted column is a
  solid brighter step `#7dff9a`, not a pale gradient.

- A heading flicker animation, gated behind
  `@media (prefers-reduced-motion: no-preference)` and never carrying state
  on its own.
- Panels glow faintly *inward* (`inset` shadow) as though lit from behind.
- Selected rows wash green at 12%; the active-row marker stays a hard bar.

### Icons

`themes/matrix/icons.svg` redraws six icons (home, settings, search,
close, user, bell) as thin monospace/glyph-like line marks — a 1px
stroke with square terminal caps in place of the generic sprite's 2px
rounded default, so they read as hairline character strokes rather than
a UI icon set. Settings becomes an eight-point asterisk glyph instead of
a naturalistic gear, matching a terminal's habit of representing controls
as punctuation rather than pictures. The sprite ships 181 `<symbol>`s in total (`grep -c '<symbol'`), and each differs from the generic outline sprite in `assets/icons/icons.svg`; only the six above are described in detail. The sprite now covers the full core set (178/178). Style rules for the
whole file, followed by the 45 ids added in the 2026-10 top-up: 24 grid;
1px hairline stroke, square caps, miter joins; never filled (the sprite
inherits `fill: none`); true curves allowed; rects rx 1.5 when 6+ wide,
sharp below; dots are r1.2 hairline rings; colour is `currentColor` only.
- **Easter egg** (`data-easter-eggs`, `assets/js/eggs.js`): after a minute idle, digital rain falls until the next key or pointer move (`@keyframes matrix-egg-rain`, separate from the page rain).

## Layout

A **terminal**: black bar, one hairline rule, no rail, content filling the
frame. The least furniture of any theme in the catalogue — deliberately the
opposite extreme from LCARS.

## Extending it

Do: keep everything monospace; keep the bloom subtle; add new states as
brightness steps of green rather than as new hues.
Don't: add a second accent colour, use a sans-serif anywhere, or let the
flicker animation communicate anything.

## Tell-tales of an inauthentic result

- A proportional font anywhere → the illusion collapses immediately.
- Multiple accent hues → a "hacker" theme, not a phosphor terminal.
- Heavy neon glow → cyberpunk, not CRT.

## Typography

`--font` (and `--font-mono`) is `"IBM Plex Mono", "DejaVu Sans Mono", Consolas, Menlo, "Courier New", monospace`. Everything is monospace, and a clean sans mono leads so the width is similar on every platform (Courier New's serif typewriter face is last-resort only). **Nothing is vendored.** On phones the five-way toggle group and the bar nav trim their side padding so the wide mono keeps 4px clear of the box edge. The film's rain glyphs are mirrored katakana and numerals from a custom set; katakana has no reliable system font, so the rain mixes mirrored digits and Latin capitals in the system monospace with a dozen katakana-like shapes (ア イ ウ エ オ ハ ミ ヒ シ リ カ ツ) drawn as SVG strokes, which need no font.

## Contrast honesty

- **Phosphor green `#00ff41` is unlifted.** The `theme.css` header says it matches the reference on-screen code's hex; `RESEARCH.md` records no hex, so that claim could not be verified from the folder. It is 15.38:1 on black and 14.56:1 on `--surface` `#020c02`, so no AA adjustment was needed, and black `--on-accent` `#001a06` is 13.37:1 on it.
- **Body text** `#8cff9c` is a saturated phosphor green a step lighter than the accent (16.9:1 on black, 14.64:1 on `--surface-2`), so long copy is not pure accent; pale and white are kept for heads, focus and warnings.
- **`--muted` `#5cc860`** is 9.36:1 on `--surface` and 8.56:1 on `--surface-2`: AAA on every panel.
- **Red is the only non-green hue.** `--danger` `#ff3b3b` is 5.94:1 on black.
- **`--border` `#1a9a2a`** is about 5.7:1 on black, so the slider track and control rules clear the 3:1 non-text floor.

## Reference status

`references/matrix/` has 4 captures plus `RESEARCH.md`: digital-rain crops, a "SYSTEM FAILURE" code wall and a green terminal screencap (all people-free per the audit). They back the phosphor palette and the monospace look. `RESEARCH.md` states the operator-console (monitor wall) target remains uncovered, and records no hex values.

## v5 layout

Tiers (core): mobile ≤480px, tablet 481–900px, desktop 901–1800px, XL ≥1801px (shell capped at 1800px, centred). On phone and tablet the bar is two lines (brand and actions, then the nav scrolling sideways); the terminal has no rail or bar decoration to rearrange, so nothing else changes. On XL the gutters show the rain frozen: a still wall of dim code columns cut into glyph cells, on black (about 1.0:1 against `--bg`). The live rain keeps running on the page itself.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
