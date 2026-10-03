# Cyberpunk 2077

> Night City menus and HUD: coral-red condensed caps on near-black maroon, cyan for whatever is live or selected, yellow tags, angled cut corners, scanlines, glitch offsets, and netrunner breach-grid tables.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

The in-game menus and HUD of *Cyberpunk 2077* (CD PROJEKT RED, 2020) as
players see them on every pause: the inventory, character, journal,
database, crafting and settings screens, the breach-protocol minigame and
the combat HUD. Each menu is a dark, slightly maroon field lit from the
top edge, written almost entirely in one coral red: labels, item names,
descriptions, rules and frames. Cyan marks whatever is live: the active
tab, the selected setting, ON, values, the cursor. Yellow is rare and loud
(NEW tags, quest markers, the brand colour). The breach-protocol screen
switches to yellow-green on dark teal, and this theme borrows it for every
table.

It is *inspired by* the game. No logo, wordmark, corporation mark, game
art or screenshot ships in the theme. Sources, palette samples and a
component-by-component mapping are in `references/cyberpunk-2077/RESEARCH.md`.

## Core values

1. **Red is the ink, not an alarm.** Body text, labels and frames are the
   menu red (`--text #ff8a82`, rules `#ff5f58`). Danger is a different,
   hotter red used as a *fill* (`--danger #ff2a3d`) and a pink-red as text
   (`--danger-text #ff4d7a`). Don't "fix" the theme by making body text
   white.
2. **Cyan means live.** Active tab, selected row, ON, focus, values,
   readouts and the hover cursor are cyan `#5ef6ff`. Nothing decorative is
   cyan except the breach corner brackets.
3. **Angles, never curves.** `--radius: 0`. Panels, cards, modals and
   menus have their bottom-right corner cut on a 45° diagonal with the
   frame line following it; buttons and badges are clipped the same way;
   bars end in an angle. Status dots, avatars and switch thumbs are square;
   only genuinely round instruments (gauges, the FAB) stay round.
4. **Condensed, squared caps.** One squared condensed sans (Rajdhani as
   the stand-in) for everything; titles, buttons, tabs and column heads in
   tracked uppercase, body in sentence case.
5. **Tables are the breach grid.** A solid yellow-green head bar with dark
   text, a dark teal matrix with faint grid lines, the steel band under the
   cursor, cyan for selection, cyan corner brackets around a scrolling
   table. This is deliberately a second palette inside the theme.
6. **Glitch is punctuation.** A static cyan/pink split on `h1`; with full
   motion, a 0.3s jitter on hover and focus and on arriving danger
   alerts. Never a constant animation on content.

## Signature details

- Every surface has a 1px red frame drawn in its background, a short 3px
  red tab at the top-left, a red wash falling from the top edge, and a
  cut bottom-right corner whose diagonal is part of the frame.
- `.btn`: dark red plate, red rule, cut corner with a matching diagonal;
  hover turns border and label cyan with an inner cyan glow. `.btn-primary`
  is a solid red slab that turns cyan on hover.
- `.modal-header > .btn-close` is the game's `[ESC]` key cap, cyan outline;
  minimise and maximise are matching cyan boxes.
- `kbd` is a cyan outlined key cap, as in the key-hint strip.
- `.table`: breach-yellow head bar, teal matrix, cyan selected row with a
  cyan marker; inside `.table-wrap`, cyan corner brackets.
- `.segmented` and `.switch`: the settings OFF/ON pair; red when off, cyan
  when on. `.slider`: dark track with a red slab thumb.
- `.hud-bar`: flat fill with a glow in its own colour and an angled end;
  health red, RAM (mana) cyan, stamina yellow; slots glow in the game's
  rarity colours.
- The rail is a 1.5rem data strip of tick marks and code bars, like the
  micro-print along the game's screen edge; the bar is a maroon strip cut
  off by one long glowing red rule.

## Typography

The game's menu face is a squared condensed technical sans,
community-identified as **Blender Pro** (commercial; not verified from the
game files). It is not vendored and not named in the stack. The theme
vendors **Rajdhani** Medium and Bold (Indian Type Foundry, SIL OFL 1.1,
`assets/fonts/Rajdhani-*.woff2`, Latin subset, about 15 KB each), whose
squared counters and short descenders are the closest open match, and
reuses the already-vendored **Share Tech Mono** for code and logs.

## Contrast honesty

All pairs meet the lint floors; no exemptions are claimed.

| Pair | Ratio |
|---|---|
| `--text` `#ff8a82` on `--surface` `#1a1119` | 8.1 |
| `--muted` `#e3645d` on `--surface` / `--surface-2` `#110d15` | 5.5 / 5.7 |
| `--accent` `#5ef6ff` on `--surface` | 14.2 |
| `--on-accent` / `--on-danger` / `--on-success` `#0b0a0f` on their fills | 15.1 / 5.3 / 10.6 |
| `--danger-text` `#ff4d7a` / `--warning-text` `#fcee0a` / `--success-text` `#2bd97c` on surface | 5.8 / 15.3 / 10.0 |
| Breach cells `#cfec58` on `#121f1f` | 12.7 |

The sampled label red (`#d7443d`, anti-aliased) is 4.4:1 on the backdrop,
so text reds are lifted; the sampled red stays as the rule and fill colour.

## Layout

The shell becomes a **menu screen**: a transparent maroon top bar ended by
one long glowing red rule (the LEVEL / tabs / eddies strip), a 1.5rem data
rail of tick marks down the left edge, content on the dark field, and a
key-hint status strip along the bottom.

## v5 layout

- **Tiers:** core's. Mobile ≤480px and tablet 481–900px drop the rail (core
  default) and use `--app-main-padding-mobile|-tablet`; the bar keeps its
  red rule and the nav takes its own scrolling line. Desktop 901–1800px is
  the full shell; XL ≥1801px caps it at 1800px.
- **Gutter art (XL):** faint red scanlines, a column of edge tick marks
  each side, a cyan data line and a ghost diagonal of a cut corner, all a
  few percent over `--bg` (about 1.1:1). The scanlines crawl one band every
  40s only with `prefers-reduced-motion: no-preference` and not under
  `data-motion="reduced"`.
- **Nesting:** an inner panel or card loses the red tab, the wash and the
  red frame and gets a hairline frame with a smaller 8px cut on
  `--surface-2`; a third level is a plain tinted block with a hairline
  left rule.
- **Touch:** controls grow to `--tap-min` (core); cut corners scale with the
  control.

## Don'ts

- Don't round anything, and don't use clip-path on panels (it would clip
  focus rings and anchored menus; the frame is drawn in the background).
- Don't make body text white or grey; don't use cyan for decoration.
- Don't add the game logo, the yellow wordmark, corporation marks
  (Arasaka, Militech, NetWatch) or character art.
- Don't run glitch animations continuously or on content; keep them on
  hover, focus and arriving alerts, under full motion only.

## Tell-tales of an inauthentic result

- A purple/pink "synthwave" palette or a magenta-and-cyan neon look:
  that is vaporwave, not Night City. The game is red on maroon-black.
- Rounded corners, pill buttons or soft drop shadows.
- A wide geometric or humanist sans; the condensed squared caps are the
  biggest cue after the colour.
- Tables in the same red as everything else (they lose the breach grid),
  or selection shown as a red fill instead of cyan.
- Yellow everywhere: the yellow is for tags and quest marks only.
- Constant flicker or scrolling glitch on text.

## Print

The frames, wash, scanlines, rail and clip-paths are dropped in a small
`@media print` block; tables print black on white.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement. Adopt the
`.app`/`-bar`/`-rail`/`-main`/`-status` shell (CONTRACT.md "The app shell"
/ "Adoption levels") to get the menu-screen layout at **L1**.

## Reference status

Researched from fifteen 1920×1080 in-game screenshots on *Interface In
Game* (inventory, settings, breach protocol, save confirmation, database,
journal, crafting, difficulty select, level-up, pause menu, messages,
stats, job objectives and the driving HUD). Unverified: the exact
typeface, the quickhack wheel and the full combat HUD (only the
health/XP bar and RAM pips are covered), and any controller-only
widgets. See `references/cyberpunk-2077/RESEARCH.md` "Gaps".

## Icons

`icons.svg` redraws the whole core set (178/178) in the style of the
in-game menu tab glyphs (see `references/cyberpunk-2077/`):

- 24×24 grid, 2px stroke, square caps, mitred joins; angles, not curves.
- Every box has its bottom-right corner cut at 45°, like the panels.
- Simple silhouettes (heart, bell, bookmark, folder, user, play, shield)
  are solid fills. Containers are a frame with solid inner bars (the
  table's head bar, the card stripe). Only things that are really round
  (clock, disc, coin) keep circles.
- `currentColor` everywhere, so the red ink and the cyan selection both
  apply. No game marks or logos.
