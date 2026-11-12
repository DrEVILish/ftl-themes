# Barbie

> Hot-pink glamour — glossy pill chrome, gold sparkle, all-caps confidence.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

The **Barbie brand aesthetic**: hot pink as the dominant color, not an
accent; everything glossy, rounded, and a little oversized, like packaging
for a toy rather than a productivity tool. The target is "confident and
glamorous," not "pastel and quiet" — this theme is loud on purpose.

## Core values

1. **Pink is the substrate.** `--accent` carries the whole identity;
   it shows up on every button, every active state, every header. A
   version of this theme with a muted or desaturated pink has missed the
   point.
2. **Round, everywhere, generously.** `--radius: 1.4rem`, pill buttons,
   pill badges, pill pagination, pill sliders (a hot-pink gradient track),
   and input-group addons keep the input's round outer ends. The selected
   desktop-icon label is a pill and tree rows take a `0.6rem` row-sized
   radius. Nothing here has a hard corner.
3. **Gloss over flat.** Every filled surface gets a light highlight band —
   the same "shiny plastic" cue as the button chrome, panels, and the app
   bar. Losing the highlight reads as a cheaper, flatter knockoff.
4. **Gold is the sparkle, not the workhorse.** `--flare` (gold) shows
   up only as a crisp 1px unblurred foil lip straight under the uppercase
   headings — it's the
   tiara, not a token you build components out of.
5. **Deep pink text, not black.** Body text is `#7a1250`, a pink-shifted
   dark plum — legible, but never plain black, which would read as a
   generic light theme wearing a pink accent.

## Signature details

- **The wordmark.** `h1` and `.nav-brand` are Pacifico script in white
  letters inside a thick hot-pink outline (`-webkit-text-stroke` painted
  under the fill, `0.12em`) with a deep solid pink slab stepped out to
  `0.14em` down-right, the logo's extrusion, sized in em so it reads at
  bar-brand size. In the app bar the outline and slab go deep pink `#8f1458`.
- Headings (`h2`/`h3`) are uppercase with a hard 1px gold lip underneath,
  the poster-title voice. On `.hero` and `.band.is-tinted` they stay
  accent pink (large text, 3:1 floor).
- **Desktop windows.** Inactive title bars stay saturated: a paler candy
  pink (`#ffc2e0` to `#ff99cc`) with plum text, never core's desaturating
  filter (that turned the bar dusty mauve). Caption buttons follow the
  title text colour.
- Sliders are slim pills in both orientations: the vertical slider insets
  its track on the physical sides so it is not a 24px pillar.
- Rising sparklines draw in toy mint-teal `#1f9e74` (the bar chart's alt
  series), not the text-weight green.
- The accent `#cc0077` is a fully saturated magenta (hue 325°, the logos'
  `#ed008d`/`#ff00a6` family) at the darkest step that still takes white
  text. Bar and status strip run `#e0007f` to `#b8006f`; gloss buttons run
  `#ff4fb3` to `#e0007f` to the accent, highlight band at the top.
- **Toy-box sections.** `.hero` sits on a rounded blush panel with the
  gutter's polka dots; `.band.is-tinted` on a blush gradient panel.
- Success state uses Barbie mint (`#3ddc97`) with dark text, not a generic
  green with white text — mint is too light for white to pass, and a
  generic green would clash with the palette.

## Layout

The app shell becomes a **glossy pink ribbon**: a rounded pink gradient
bar on top, a matching sparkle-gradient status strip on the bottom, and a
soft pale-pink backdrop (`radial-gradient`) that makes the white content
card in the middle pop — box art, not a dashboard.

## v5 layout

- **Tiers.** No rail; the glossy bar's pills wrap as core lays them out,
  so phone (≤480px) and tablet (481–900px) use the one-column shell as is.
- **Nesting.** A panel or card inside another surface drops the pink
  drop-glow, so stacked levels read as inserts in one toy box.
- **XL gutter art.** The packaging either side of the doll: soft polka
  dots in a deeper blush on a blush-to-pink fade. Still, and within about
  1.3:1 of `--bg`.

## Tell-tales of an inauthentic result

- Pastel/muted pink instead of the saturated hot pink.
- Sharp corners on any button, panel, or badge.
- Plain black body text.
- A generic green success state instead of the mint/dark-text pairing.

## Don'ts

- **No hard corners.** Buttons, badges and sliders are pills (`--btn-radius: 999px`); panels are `1.4rem`.
- **No black text.** Body copy is plum `#7a1250`; plain black reads as a generic light theme.
- **No pastel or desaturated pink.** A washed-out accent is the failure the theme exists to avoid.
- **No matte flat fills** on primary chrome: keep the highlight band.
- **No gold as a component colour.** `--flare` gold is the heading foil edge only.
- **No script face on body or buttons.** Pacifico is for the wordmark and `h1` only.
- **No generic green success with white text**; keep mint with dark text.

## Typography

- **Body/UI:** `"Baloo 2"`, then `"Segoe UI", "Helvetica Neue", Arial, sans-serif`. Baloo 2 **Bold (700)** is **vendored** (`assets/fonts/Baloo2-Bold.woff2`, SIL OFL, see `assets/fonts/NOTICE.md`); only that weight exists, so headings and buttons sit at 700. If it fails to load, the stack falls to Segoe UI/Arial, which is not rounded.
- **Wordmark voice:** `"Pacifico", cursive` (Regular, **vendored**) on `h1` and the nav brand only. The brand's wordmark is a cursive script (`barbie-wordmark-2023-logo.png`), which Pacifico approximates; it is not the actual logo lettering. Fallback is the browser's generic `cursive`.
- `--font-mono` is the rounded Baloo 2 stack, so readouts, order IDs,
  totals, timecodes and logs stay in the rounded voice (tabular figures on
  table cells, `.mono`, `.stat-value`, `.readout`). Only `code`, `pre`,
  `kbd` and `samp` use a real monospace (`ui-monospace, Consolas`).
- Known gap: only Baloo 2 Bold is vendored, so body copy and headings share
  700; a 500/600 cut would need a new file under `assets/fonts/`.

## Contrast honesty

- **Accent:** true "Barbie Pink" `#e0218a` (web reference from `RESEARCH.md`; the brand spec is Pantone 219C, which has no exact sRGB) is 4.42:1 under white text, and the logo files sample at `#ed008d`/`#ff00a6`/`#f200a2`. Shipped `--accent` is `#cc0077`: full saturation, 5.48:1 under white text, 4.66:1 as text on `--bg`. The chrome top stop `#e0007f` is 4.69:1 under white.
- **Wordmark:** the `h1` fill is white; the glyph is carried by its hot-pink outline and extrusion (5.5:1 against white), so it reads as large outlined text.
- **Status strip:** `--muted` turns white there (4.69:1 at the top stop; every pale pink fails it).
- **Inactive window title:** plum `#7a1250` on `#ff99cc` is 5.3:1 (on `#ffc2e0` higher).
- **Sparkline:** `#1f9e74` is 3.4:1 on white (non-text 3:1).
- **Tinted surfaces:** links, and headings except on the hero/band, on `.hero`, `.band.is-tinted`, `.order-summary` and the plain `.banner` use `--accent-text` (5.57:1 on `#ffd1e8`).
- **`--muted` lifted:** `#b5507e` (3.5:1) to `#9b416a` (5.32:1 on `--bg`, 6.25:1 on white, 4.63:1 on `--surface-2`).
- **Mint success:** `--success` `#3ddc97` is too light for white, so the foreground is dark `#052e1c` (8.40:1) instead of dulling the fill. As text, `--success-text` `#146c46`.
- **Nav gradient:** the pink-to-magenta bar range was chosen so white nav text stays 4.5:1 at every stop (per the `theme.css` comment: white bottomed out at 2.1:1 on earlier lighter stops and the darkest plum at 3.2:1).
- `--accent` on the pale `--bg` is 4.66:1: fine for large/UI use; `--accent-2` `#ff5cad` is 2.42:1 on `--bg` and is a decorative highlight only.
- **Pink text on pink tints:** the accent is 3.9:1 on its own badge tint and on a kanban column, so accent badges, kanban column titles, highlighted code and `.schedule` stamps use `--accent-text` `#a01565` (5.4:1 on the badge tint). `--danger-text` is `#ac0d47` (was `#c00f4f`, 4.4:1 on its badge tint).

## Reference status

`references/barbie/` has 5 files plus `RESEARCH.md`: three PD logo files (`barbie-wordmark-2023-logo.png`, `barbie-the-movie-logo.png`, `barbie-mattel-seal-logo.png`) plus `Barbie_Logo.svg` and `s-l1200.png`, which `RESEARCH.md` does not describe (provenance unverified). The logos back the gloss-pink pill/script identity and rounded type. `RESEARCH.md` states an honest gap: no people-free pink product or packaging photo exists in the set, so packaging colour beyond the logo (gold sparkle, backdrop pinks, mint) is design judgement, not sampled. The logos' pink samples at `#ed008d`-`#ff00a6`; `--accent` `#cc0077` is that hue at full saturation, darkened to take white text.

## Icons

`themes/barbie/icons.svg` redraws the whole core set (178/178) as soft,
rounded line icons:

- 24×24 grid, line only: no fills, colour from `currentColor` (the pink comes
  from the theme tokens, never the file).
- Uniform `stroke-width="2.6"` set per symbol with round caps and joins.
- True curves kept; rectangles get generous radii (rx up to 4–5), pages use
  the rounded dog-ear outline of `icon-file`.
- Dots are small stroked rings; a few icons carry a tiny accent dot. Dense
  glyphs (PDF/PNG pages, histogram, thermometer) are opened up so the heavy
  stroke does not clog at 16px.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
