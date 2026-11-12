# Barbie

> Hot-pink glamour — glossy pill chrome, a fat outlined script wordmark, all-caps confidence.

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
   desktop-icon label is a pill; tree rows, desktop window panes, the
   notepad field and table corners (header band and last row) take a
   `0.6rem` row-sized radius; fieldsets get a pink hairline box at the
   panel radius instead of the browser's grey groove. Nothing here has a
   hard corner.
3. **Gloss over flat.** Every filled control gets a hard-edged bright
   band over its top third (`--gloss-pink`: `#ff4fb3`/`#ff3da6`, then
   `#e3007f` to the accent): plain, primary, danger (`--gloss-danger`) and
   mint success (`--gloss-success`) buttons, the active nav pill (a deep
   plum gloss in the bar), the active pagination pill and the active
   segmented item. Core re-sets `--btn-bg` on `.btn-primary`/`-danger`/
   `-success`, so the theme re-points it on those classes too. Losing the
   highlight reads as a cheaper, flatter knockoff.
4. **Pink on pink, no foil.** The logo is white, hot pink and a pink
   extrusion; `h2` takes a small pink step of that extrusion
   (`0.06em` in `#ffb3d9`), never a gold lip (it read as an offset-print
   fringe). `--flare` gold is defined only because core requires it.
5. **Deep pink text, not black.** Body text is `#7a1250`, a pink-shifted
   dark plum — legible, but never plain black, which would read as a
   generic light theme wearing a pink accent.

## Signature details

- **The wordmark.** `h1` and `.nav-brand` are Shrikhand: fat, separate
  letters with ball terminals and flared slab-like serifs, as on the logo
  (a connected brush script read as a diner sign). They are white letters
  inside a hot-pink outline (`-webkit-text-stroke` painted under the fill,
  `0.14em`, so the pink mass about equals the white stroke as on the logo)
  with a solid pink slab stepped out in three steps to `0.18em`
  down-right, the logo's extrusion. The brand is set at `1.2em` with a
  `0.06em` outline and one `0.06em` step, so the counters stay open at
  bar size. In the app bar the brand sits on its own white sticker pill,
  so the white/pink-outline/slab stack reads as on white.
- Headings (`h2`/`h3`) are uppercase. `h2` is set at weight 800 with a
  crisp `0.04em` step in 40% `--accent-2`, the poster-title voice; `h3`
  stays flat. On `.hero` and `.band.is-tinted` they stay accent pink
  (large text, 3:1 floor).
- **Glossy pills.** Filled buttons, active nav/segmented/pagination items
  and checked toggles take `--gloss-pink`: a `#ff4fb3`-`#ff3da6` band over
  the top 36%, then `#e3007f` to the accent. White labels take a plum
  `0 1px 0` text-shadow so a cap height or wrapped line in the band reads.
- **Toggle buttons.** Off is a white pill with a pink edge (like
  Secondary); on is the glossy pink pill (`.is-danger`: the danger gloss).
- **Packaging inserts.** Panels and cards have a `2px` pink edge; a panel
  header is a white-to-blush band under a `3px` `--accent-2` top rule.
- **Checkboxes and radios.** No browser-grey box: a white well in a `2px`
  pink edge (`0.35em` corners on checkboxes), filled with the accent and a
  white tick or dot when on.
- **Desktop windows.** Inactive title bars stay saturated: a paler candy
  pink (`#ffc2e0` to `#ff99cc`) with plum text, never core's desaturating
  filter (that turned the bar dusty mauve). Caption buttons follow the
  title text colour.
- Sliders are slim pills in both orientations, an accent-to-hot-pink
  gradient track on the content box (the hit area stays `--tap-min`); in
  Firefox the filled side takes the gradient over a blush rest. The
  vertical slider insets its track on the physical sides so it is not a
  24px pillar.
- The modal backdrop is an accent-pink scrim (`rgba(204,0,119,.35)`), not
  a plum-grey one.
- Rising sparklines draw in toy mint-teal `#1f9e74` (the bar chart's alt
  series), not the text-weight green.
- The accent `#cc0077` is a fully saturated magenta (hue 325°, the logos'
  `#ed008d`/`#ff00a6` family) at the darkest step that still takes white
  text. Bar and status strip run `#e5007f` to the accent (the logo's
  `#ec008c` takes white at only 4.25:1, so `#e5007f`, 4.53:1, is the nearest passing
  top stop). Filled chrome leads with the brighter logo pink through the
  gloss band, and the label sits on `#e3007f` (4.6:1) to the accent.
- **Toy-box sections.** `.hero` sits on a rounded blush panel with the
  gutter's polka dots; `.band.is-tinted` on a blush gradient panel. A
  full-bleed one (a direct child of `body`) is inset by `--app-padding`
  so its rounded edge never meets the window edge.
- Small uppercase labels (stat labels, table heads) are Baloo 600 with
  `0.06em` tracking, never under `0.75rem`.
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
- **Phone tier.** For scroll paint cost: a flat `#ffe6f2` backdrop
  instead of the radial gradient, no card/panel drop-glow (the 1px pink
  border separates them), no `h2` extrusion step.
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
- **No gold.** Nothing on the logo is gold; `--flare` exists only as a required token.
- **No script face on body or buttons.** Shrikhand is for the wordmark and `h1` only.
- **No generic green success with white text**; keep mint with dark text.

## Typography

- **Body/UI:** `"Baloo 2"`, then `"Segoe UI", "Helvetica Neue", Arial, sans-serif`. The Baloo 2 **variable** cut (wght 400-800, Latin subset) is **vendored** (`assets/fonts/Baloo2-Variable.woff2`, SIL OFL, see `assets/fonts/NOTICE.md`), so body copy is 400, labels 600 and headings/buttons 700. If it fails to load, the stack falls to Segoe UI/Arial, which is not rounded.
- **Wordmark voice:** `"Shrikhand", "Cooper Black", Georgia, cursive` (Regular, **vendored** Latin subset, SIL OFL) on `h1` and the nav brand only. The brand's wordmark (`barbie-wordmark-2023-logo.png`, `s-l1200.png`) is fat, separate letters with ball terminals and flared serifs, which Shrikhand approximates; it is not the actual logo lettering. Cooper Black is the nearest common system face.
- `--font-mono` is the rounded Baloo 2 stack, so readouts, order IDs,
  totals, timecodes and logs stay in the rounded voice (tabular figures on
  table cells, `.mono`, `.stat-value`, `.readout`). Only `code`, `pre`,
  `kbd` and `samp` use a real monospace (`ui-monospace, Consolas`).
- Known gap: no open face reproduces the logo's custom lettering (its
  slab-like serifs and ball terminals); Shrikhand is the nearest open face,
  though it leans more than the logo's letters.

## Contrast honesty

- **Accent:** true "Barbie Pink" `#e0218a` (web reference from `RESEARCH.md`; the brand spec is Pantone 219C, which has no exact sRGB) is 4.42:1 under white text, and the logo files sample at `#ed008d`/`#ff00a6`/`#f200a2`. Shipped `--accent` is `#cc0077`: full saturation, 5.48:1 under white text, 4.66:1 as text on `--bg`. The bar and status strip run `#e5007f` (4.53:1 under white, the nearest stop to the logo's `#ec008c` at 4.25:1 that passes) to the accent; nav labels are regular-weight small text, so the 3:1 large-text floor does not apply and the chrome stays one step deeper than the logo.
- **Gloss band:** white is 3.0-3.25:1 on the band (`#ff4fb3`-`#ff3da6`), large-text level; labels sit mostly on the `#e3007f`+ mass (4.6:1+) and take a plum text-shadow.
- **Wordmark:** the `h1` fill is white; the glyph is carried by its hot-pink outline and extrusion (5.5:1 against white), so it reads as large outlined text.
- **Status strip:** `--muted` turns white there (4.53:1 at the top stop; every pale pink fails it).
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
