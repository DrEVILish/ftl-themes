# Skyrim

> The Elder Scrolls V: Skyrim menus, with SkyUI's column tables: smoke-black panels in thin silver rules, condensed white type, chevron-capped title bars and diamond-capped attribute bars.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

The in-game menus of *The Elder Scrolls V: Skyrim* (Bethesda, 2011) as
most PC players know them: the **vanilla menu chrome** (character
creation, skills, the journal tab bar, the health / magicka / stamina
bars, the key-hint strip along the bottom of the screen) combined with
**SkyUI** (schlangster et al.), the mod that replaced the vanilla
inventory with sortable column tables and category icons. Each menu is a
dim, smoky overlay on top of the game world, with very little colour and
no rounded corners. The only colour comes from the game's state: red
health, blue magicka, green stamina, gold legendary stars.

**Primary direction: vanilla chrome + SkyUI tables.** `.table` follows
SkyUI. The bar, tabs, progress, sliders and status strip follow vanilla.
The quest journal's parchment book is *not* the default look. It would
need a light palette and is not backed by a reference image yet (see
RESEARCH.md "Gaps").

Sources, palette samples and a component-by-component mapping are in
`references/skyrim/RESEARCH.md`. No logo, dragon emblem or game art is
reproduced.

## Core values

1. **Smoke, not glass and not solid.** Surfaces are near-black warm smoke
   (`#161512`–`#24231f`, sampled from SkyUI lists). They fade at the edges,
   with no blur and no colour tint. Don't make them opaque grey slabs.
2. **Thin silver rules with knotwork corners.** Frames are 1px
   `#6f6f6c` lines. Every panel and modal has a small interlaced square in
   each corner and a faint inner second rule. Don't add rounded corners or
   thick borders.
3. **Condensed, white, quiet type.** One condensed sans for everything.
   Titles are uppercase with almost no tracking. Column heads are tiny grey
   caps. Body text is sentence case. Nothing is bold except emphasis.
4. **Selection is light, not colour.** A selected row or item is a white
   band that fades out at both ends (`--sky-select`). In tables it ends in
   an arrow tip, as in SkyUI. There are no blue highlight fills.
5. **Colour belongs to the game state.** Health red `#b33e3f` is danger,
   stamina green is success, legendary gold is warning, and the level-bar
   frost blue `#aec0d5` is the only interactive accent. Magicka blue is the
   second series.
6. **Chevrons and diamonds are the ornament vocabulary.** Title bars and
   bars end in points. The active tab is flanked by `◁ ▷`. Checkboxes and
   switch thumbs are diamonds (SkyUI's MCM). Section rules end in an open
   diamond.

## Signature details

- The app bar is a long, inset strip with chevron-pointed ends and
  1px silver rules top and bottom (the creation / journal title bar).
- `.tab.is-active` reads `◁ OVERVIEW ▷`. Inactive tabs are dimmed grey.
- `.table`: tiny uppercase grey heads over one silver rule, no row rules,
  and a selected row drawn as a fading white band that ends in an arrow tip.
- `.panel-header`: white caps followed by a thin rule running to an open
  diamond (the MCM section header).
- `.progress` and horizontal `.meter`: diamond end caps (clip-path). The
  progress fill is the level bar's frost-steel gradient. Meter bands run
  stamina green, then gold, then health red.
- `.checkbox` is a rotated diamond: hollow when off, a white diamond with
  a black inset when on. `.switch-thumb` is a diamond.
- `kbd` is a key-hint box: white outline, black fill, white glyph.
- The left rail is a smoke strip with one vertical silver rule and a
  diamond on it, like the vanilla category-column divider.

## Typography

The game uses a condensed Futura (community-identified as Futura Condensed
/ Futura Std Condensed; not verified from the game files). Futura is
commercial and is not vendored. The stack names `"Futura PT Cond"`,
`"Futura Condensed"` and `"Futura Std Condensed"` first, then falls back to
**Antonio** (Vernon Adams, SIL OFL 1.1). Antonio is already vendored in
`assets/fonts/` for LCARS, so this theme adds no files. Antonio is
narrower and more squared than Futura Condensed, but it keeps the tall,
condensed, light voice. Stat values (`.stat-value`) use the UI font, not
monospace, because the game has no monospace anywhere. `code` and `.mono`
keep the mono stack.

## Contrast honesty

All pairs meet the lint floors. No exemptions are claimed.

| Pair | Ratio |
|---|---|
| `--text` `#ecebe6` on `--surface` `#161512` / `--bg` `#101213` | 15.3 / 15.7 |
| `--muted` `#a7a7a5` on `--surface` / `--surface-2` `#0d0d0c` | 7.6 / 8.1 |
| `--accent` `#aec0d5` on `--surface` | 9.8 |
| `--on-accent` `#111110` on accent | 10.2 |
| `--on-danger` `#ffffff` on `--danger` `#b33e3f` | 5.7 |
| `--on-success` `#ffffff` on `--success` `#2a7a4b` | 5.3 |
| `--danger-text` `#e8787a` / `--success-text` `#74c795` / `--warning-text` `#e3c35a` on surface | 6.4 / 9.0 / 10.6 |

Deviations from the samples: stamina green is sampled between `#1f6636`
and `#338d5c`. `#2a7a4b` was chosen so that white text clears 4.5:1. The
`--border` `#6f6f6c` is 3.6:1 and is a structural line only.

## Layout

The shell becomes a **menu screen**. A chevron-capped title bar is inset
across the top. A slim smoke rail on the left carries a silver divider
and a diamond. Content sits on the misty slate backdrop, and the
key-hint strip runs along the bottom edge. At phone width the rail
collapses as core sets by default.

## Don'ts

- Don't add a coloured accent fill for selection or hover. Selection is
  white light.
- Don't round corners, add drop-shadow "cards", or use glassmorphism blur
  on panels.
- Don't use the dragon emblem, the Skyrim wordmark or any game art.
- Don't let magicka blue, health red or stamina green leak into the
  chrome. They are state and series colours only.
- Don't add parchment to the default palette. A journal variant would need
  its own `references/skyrim/<variant>/` images first.

## Tell-tales of an inauthentic result

- A wide humanist or geometric sans at normal width: the condensed voice
  is the single biggest cue.
- Selected rows filled with a solid accent colour instead of a fading
  white band.
- Thick or coloured panel borders, or no corner ornaments at all, which
  reads as a generic dark dashboard.
- Rectangular progress bars with rounded ends instead of diamond points.
- Gold or bronze "fantasy RPG" chrome (that is Oblivion or a generic
  MMO). Skyrim's chrome is grey silver.

## Print

Smoke, the knotwork panel background, the rail and the clip-path end
caps are neutralised in a small `@media print` block.

## Reference status

Researched from real screenshots: UESP menu images (skills menu,
character creation, statistics/journal tab bar, the health bar), SkyUI's
own repository (icon-theme previews), and the Steam guide "SkyUI -
Features Overview" (inventory/container tables, magic list with info
card, MCM config page, favorites, map search). Unverified: the
exact typeface, the vanilla parchment journal, the compass bar (only a
partial crop is referenced) and the dialogue menu. See
`references/skyrim/RESEARCH.md`.

## v5 layout

Tiers (core): mobile ≤480px, tablet 481–900px, desktop 901–1800px, XL ≥1801px (shell capped at 1800px, centred). The rail is hidden up to 900px. On touch tiers the chevron-capped bar is shallower and less inset. On a phone the `h1` steps down, and panels use smaller corner knots and a full 1rem padding, so text clears them. Nested panels drop the knotwork and the drop shadow. Panel titles clear the corner knot, and a header holding controls wraps with the title kept whole. On XL the gutters show knotwork border bands: a woven lattice between silver rules with a chain of diamonds, a few percent over `--bg` (about 1.0:1).

## Icons

`themes/skyrim/icons.svg` redraws all 178 core icons as rune-cut glyphs,
carved rather than drawn. No SkyUI icon art, emblem or game artwork is used.

- 24×24 grid, line only, `stroke="currentColor"`: 1.6 stroke, butt caps, miter joins.
- No curves. Every circle and arc is cut into straight facets on hexagon
  angles (pointy top). Small rings become the menu diamond.
- Rounded corners become chamfers. Dots are solid diamonds (the ◈ vocabulary).
- Solid fills only for carets and the filled play glyph.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement, not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
