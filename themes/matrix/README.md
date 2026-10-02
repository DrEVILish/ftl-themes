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
   single-phosphor illusion.
3. **Bloom, not glow.** A 2px text-shadow across all text imitates
   phosphor persistence. It is deliberately subtle — a strong glow reads as
   neon, which is a different aesthetic entirely.
4. **Outline over fill.** Base controls are transparent with a green rule.
   Only semantic variants take a fill, so a delete button still reads as
   dangerous.
5. **Uppercase headings, tracked.** Terminal banner conventions.

## Signature details

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
as punctuation rather than pictures. The sprite ships 136 `<symbol>`s in total (`grep -c '<symbol'`), and each differs from the generic outline sprite in `assets/icons/icons.svg`; only the six above are described here, and the rest were not audited one by one for style.

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

`--font` is `"Courier New", "IBM Plex Mono", Consolas, monospace`; `--font-mono` is `"Courier New", Consolas, monospace`. Everything is monospace. **Nothing is vendored** — Courier New is a system font (Windows/macOS; availability on Linux varies), IBM Plex Mono only renders if installed. The film's rain glyphs are mirrored katakana and numerals from a custom set; the theme ships no glyph face for them, so any katakana on the page is system-font fallback.

## Contrast honesty

- **Phosphor green `#00ff41` is unlifted.** The `theme.css` header says it matches the reference on-screen code's hex; `RESEARCH.md` records no hex, so that claim could not be verified from the folder. It is 15.38:1 on black and 14.56:1 on `--surface` `#020c02`, so no AA adjustment was needed, and black `--on-accent` `#001a06` is 13.37:1 on it.
- **Body text** `#b6ffb6` is a pale green (17.97:1 on black) so long copy is not pure accent.
- **`--muted` `#4caf50`** is 7.15:1 on `--surface` and 6.54:1 on `--surface-2`: AA, below AAA on the darkest panel.
- **Red is the only non-green hue.** `--danger` `#ff3b3b` is 5.94:1 on black.

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
