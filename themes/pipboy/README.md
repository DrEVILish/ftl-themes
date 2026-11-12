# Fallout Pip-Boy 3000

> Post-apocalyptic monochrome phosphor green with scanlines.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

A wrist-mounted CRT terminal in a ruined world: single-hue green phosphor,
static scanlines, and text that glows faintly rather than sitting flat on
the screen.

## Core values

1. **One hue, many brightnesses.** Every colour role (text, accent, success,
   even danger where possible) is a shade of the same phosphor green;
   `--danger`/`--warning` are the only deliberate departures,
   reserved for genuine hazard states.
2. **Outline buttons, not fills.** A Pip-Boy button is drawn, not painted —
   danger and success included (a 12% tint plus a coloured outline). A solid
   phosphor fill means one thing only: *selected* (the cursor bar).
3. **Scanlines are decoration, not motion.** A static repeating gradient,
   `pointer-events: none`, never an animated flicker — nothing here should
   fight `prefers-reduced-motion` for a cosmetic effect.
4. **Uppercase, lightly tracked labels** (0.04em) — headings, tabs, panel
   headers, buttons and the app bar (brand included) are Pip-Boy headers,
   not a stylized logo; list rows and body copy stay mixed case.
5. **Rectangular hardware.** No pills, circles or teardrops: `--radius` is
   0, so fields, buttons, cards and dropdowns are square, as are badges,
   avatars, switches, slider thumbs, comment pins, status dots and lamps,
   presence dots, carousel dots and arrows, typing dots, the pressed-button
   LED, the round minimap, the achievement icon and map pins. (Radio
   buttons stay round, since the native checked radio is.)
6. **Little boxing.** Panels and cards are a dim hairline with bright
   corner brackets, not a full phosphor box.

## Signature details

- The phosphor is Fallout 4's default Pip-Boy colour, `#1aff80`
  (RGB 26, 255, 128), on a green-black `#04140a`. Chart series are
  brightnesses of that one green; no second hue outside hazard states.
  Meter peak segments (`--meter-mid`) are the bright phosphor
  `--accent-2`; only the clip zone (`--meter-high`) turns amber.
  HUD rarity tiers (`--rarity-*`) are brightness steps of the same green,
  and the HP bar (`--hud-health`) is green, as in Fallout 4.
- **Media through the phosphor.** Images, videos, card/map SVGs and the
  HUD scene take one CSS filter chain (`--pipboy-phosphor`: grayscale,
  sepia, hue-rotate, saturate), so photos render in green, never colour.
- Native controls follow the phosphor via `accent-color`; unchecked
  checkboxes and radios are a `--border` outline on a transparent fill, not
  the grey dark-scheme box.
- Placeholders are a dimmed phosphor (`#15994d`, 5.1:1 on the field) with
  no glow, so an empty field reads unlit next to a typed value.
- Window minimise is a centred minus bar, level with the max box and BACK.
- **The cursor bar.** Selected rows, active list/sidebar nav items and
  hovered menu items are a solid `--accent` bar with the text knocked out in
  `--on-accent` (the INV/DATA list cursor), with no left marker.
- **The tab header.** `.tabs` is one 2px phosphor rule that breaks under
  the active tab; ticks rise from the rule at the active tab's ends to about 70% of the tab height,
  bracketing the uppercase label (the STAT / INV / DATA strip). The
  `.tab-add` button carries the rule too. The app bar nav is the same
  header: brand and nav uppercase (tracked above the phone tier), its
  active/open item bracketed by the same ticks, over a 2px phosphor bar
  rule. The brand keeps its full width; on phones the nav wraps instead.
  Inside windows and dialogs tab tracking tightens to 0.03em so the
  header stays on one continuous rule.
- **The status strip** (`.app-status`, not the taskbar variant) reads as
  the HP | LEVEL | AP bar: solid dim-green blocks (22% phosphor) with
  bright uppercase text, under a 2px phosphor rule.
- Type is Roboto Condensed (OFL, vendored Regular and Bold, Latin
  subset), Fallout 4's Pip-Boy `$MAIN_Font`, with "Arial Narrow" and
  "Liberation Sans Narrow" fallbacks. Share Tech Mono (OFL, vendored)
  stays as `--font-mono` for code and readouts. `font-synthesis-weight:
  none`, so only the real weights render; headings also glow brighter. At the phone
  tier tables set at 0.85em without the glow, and inputs in cells keep a
  `--tap-min` floor.
- Slider tracks are drawn in `--border` green (3:1 on bg and surface) on
  the content box, so the hit area stays at `--tap-min`.

- Scanlines are a fixed `::after` overlay on `.app` with
  `pointer-events: none` — a 1px-on/2px-off repeating gradient at 20%
  black (light enough that ~10px badge text keeps its strokes), plus a soft inset vignette for the curved glass, so they never
  intercept a click and never need JavaScript. The overlay is its own
  layer (`will-change`, `contain: strict`) so scrolling never repaints it. The vignette is a radial
  gradient in the same layer (no blurred shadow, so no frame cost).
- All body text carries a faint `text-shadow: 0 0 3px` phosphor glow in its
  own colour (`currentColor` at 35%, so dim text glows dim), not
  just headings — the whole screen glows a little, not just the display
  face.
- `--success` and `--accent` are the *same* green — this theme has
  no separate "success" hue at all, only the one phosphor color and the
  two genuine hazard departures (danger amber, warning yellow).

## Layout

Minimal chrome, matching the terminal's own screen: a plain bar with a
green rule, content filling the frame, scanlines over the whole shell.

## Tell-tales of an inauthentic result

- A second hue appearing outside hazard states.
- Filled, solid buttons — the Pip-Boy draws in outline.
- An animated flicker — static scanlines only.

## v5 layout

Tiers (core): mobile ≤480px, tablet 481–900px, desktop 901–1800px, XL ≥1801px (shell capped at 1800px, centred). No rail. Phone and tablet use the core two-line bar. The scanline overlay now sits just under the modal layer (`--z-modal` − 1), not at a literal 999. On XL the gutters show the MAP tab with the lamp turned down: a world graticule and scattered location pips in dim phosphor (about 1.0:1).

## Icons

`themes/pipboy/icons.svg` redraws all 178 core icons as monochrome CRT
pictograms. No Vault Boy, Vault-Tec or other franchise marks are used.

- 24×24 grid. Every vertex sits on the integer grid. `shape-rendering="crispEdges"`.
- Chunky line: 2px stroke, square caps, miter joins, `currentColor` only (one phosphor hue).
- Curves are faceted to flat-sided octagons, and rounded corners become 2px
  chamfers. Dots are square pixels (2×2 or 3×3).
- Dense glyphs are simplified so they still read at 16px: accessible,
  discount, disc, coin, network, cpu, thermometer, temperature, file-zip,
  fingerprint, invoice, device-watch and map-question.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
