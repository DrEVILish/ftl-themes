# Aqua

> macOS Snow Leopard — brushed metal, pinstripes, candy gloss.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

**Mac OS X circa 10.6**: glossy "candy" controls, brushed-metal window
chrome, pinstriped surfaces, and generous soft shadows. Optimistic,
tactile, unmistakably pre-flat-design.

## Core values

1. **Gel, lit from above and glowing below.** A push button is a flat
   light upper third, a hard step darker, then lighter again to a lit
   underside (measured on the Snow Leopard capture; see `RESEARCH.md`).
   Panels and bars still run light to dark. That convention produces most
   of the look.
2. **Gloss on fills, gloss only.** Gradients belong on buttons, bars and
   panels — never on text or borders.
3. **Depth is soft, not hard.** Floating surfaces (sheets, menus,
   popovers, toasts, drawers) get large blurred shadows at low opacity;
   group boxes (panels, cards) sit flat in a 1px `#b8b8b8` rim with only a
   faint 2px shadow. Corners are small (`--radius` 0.35rem, ~5px), as on
   Snow Leopard group boxes and menus; only the window itself is rounder,
   and push buttons are full capsules (`--btn-radius` 999px).
4. **The window floats.** The shell has rounded corners and sits on a
   desktop gradient with a real shadow beneath it.
5. **Light theme discipline.** This is the catalogue's first light theme,
   so filled controls need explicit white foregrounds — the dark-theme
   habit of painting them `--bg` fails here. That's exactly what
   `--on-accent`/`-danger`/`-success` are for.

## Signature details

- Panels carry an actual **pinstripe**: a 3px repeating white-at-35%
  gradient over a neutral `#ededed`→`#dcdcdc` gradient (surfaces are
  R=G=B grey, as on the capture). Phones drop the stripe for scroll cost
  and keep the gradient.
- The modal header is centred, with its own metal gradient — a Mac sheet,
  with no traffic lights. A modal header that carries close / minimize /
  zoom buttons is a window title bar: it gets the lights, and the buttons
  sit over the red, yellow and green ones, clear until hovered.
- Traffic lights belong to windows only (the app shell, window title
  bars). A panel header is a group box title: bold near-black, no lights.
- Selections are the source-list gradient (`#3a75c8`→`#2a68c4`→`#1f56b0`
  under a 1px lighter top line, white text at 4.6:1 or better): nav items,
  list items, tree items. Selected table rows use the mid stop `#2a68c4`
  with the top line as an inset shadow, since core layers the selection
  over frozen cells in a way that can't take a gradient.
- Focus adds a soft 3px blue halo rather than a hard ring.
- Every push button is a gel capsule with a black label, secondary,
  tertiary and ghost included (the quieter two with a lighter #9a9a9a
  rim). Latched `.toggle-btn`s keep the square 4px 'Textured' corner.
- Off filter chips (`.badge-button`) are small grey push gels in the
  #9a9a9a rim with a near-black label.
- Latched states are the blue gel with a black label: a switch's on
  track (off: grey push gel; knob: a white gel ball in a grey rim), the
  current pagination page and an active filter chip (both in a `#2a2190`
  rim). Badges keep their tints under a gel highlight.
- Horizontal tabs, `.segmented` and latched `.toggle-btn`s are joined gel
  segments: grey push gel, the selected one the measured blue tab gel with
  a black label, sized to their content. Vertical tab rails keep core's
  shape.
- Sliders are a ~5.6px dark grey groove (`#8a8a8a`→`#c4c4c4`, a `#5f5f5f`
  top and `#bdbdbd` bottom rim) with a blue gel knob, painted on the
  content box (border zeroed) so core's 24/44px hit area stays.
- Square text fields with an inset top shadow; selects carry the blue gel
  double-arrow cap; checkboxes and radios are white gel wells that turn
  blue gel with a black mark; progress bars are the capture's 16px,
  3px-cornered bar (blue gel fill with a faint ripple in a light grey gel
  track, `#9a9a9a` rim), and an indeterminate `<progress>` is the blue
  barber pole. A `.spinner.is-grow` dot is a blue gel ball; skeletons are
  light grey (`#e4e4e4`) with a `#f4f4f4` shimmer.
- Alerts and toasts are grey gel sheets with a neutral rim; their state is
  a 3px start bar in the state's text colour.
- A source-list selection (`.nav-rail`) is a blue gradient bar with a
  white label; in the title bar the current nav item is a darker grey inset.

## Layout

The shell becomes a **Mac window**: 0.75rem desktop margin, a rounded
brushed-metal title bar, a neutral grey (`#ececec`) window body with white
kept for fields, tables and list views, and a rounded metal
status strip, with a 28px blurred shadow under the whole frame.

## v5 layout

- **Tiers.** No rail on any tier. On every tier the traffic lights hang
  off the brand (its `::before`, positioned against the bar), so they stay
  centred on the brand's line whichever row a wrapped bar puts it on; a bar
  without a brand centres them as before. On phones the status strip's
  tray truncates rather than run under the rounded corner. On phones (≤480px) the
  window goes nearly full-screen and the bar's lights shrink to
  three-quarter size; with a brand, only the brand steps clear of them, so
  the bar's wrapped rows start at its normal edge. Phones also trade the
  large blurred shadows (window, panels, floating surfaces) for tight ones
  and hold the default button still, for scroll cost.
- **Nesting.** A panel or card inside another surface becomes an Aqua group
  box: a lighter flat inset (the parent's pinstripe shows through), no
  drop shadow.
- **XL gutter art.** The original Aqua pinstripe carried out across the
  gradient desktop either side of the window. Still, and within about
  1.2:1 of `--bg`.

## Extending it

Do: keep every fill a top-light gradient; keep shadows large and soft.
Don't: flatten a control to a solid fill, or use pure white text on a light
fill without checking the contrast floor.

## Tell-tales of an inauthentic result

- Flat solid buttons → this is the one theme where flat is wrong.
- Hard-edged shadows.
- Dark text on a mid-blue fill (fails contrast and looks unfinished).
- Square window corners.

## Typography

`--font` is `"Lucida Grande", "Lucida Sans Unicode", "Lucida Sans", "Helvetica Neue", Helvetica, Arial, "Liberation Sans", Arimo, "Nimbus Sans", sans-serif` (the last three are open, metric-close fallbacks for Linux); `--font-mono` is `Monaco, Consolas, monospace`. Lucida Grande is the authentic face (named in `references/aqua/RESEARCH.md`) and it is **system-only, not vendored**: it ships with macOS and is absent on Windows and most Linux, where Lucida Sans Unicode (Windows, a close match) or Helvetica Neue/Arial render instead. Headings get a 1px white `text-shadow` (the "engraved" look); do not swap it for a heavier weight. Aqua titles are small, so `h1` is 1.75rem and `h2` 1.35rem, bold (700), not display type.

## Contrast honesty

- **`--muted` lifted:** `#6e7075` was 4.2:1; shipped `#58595e` is 5.16:1 on `--bg`, 5.91:1 on `--surface`, 6.99:1 on white. Checked against the darker panel gradient stop too.
- **Accent blue as text is not free.** `--accent` `#2a74d0` is 4.66:1 under white text (filled controls fine) but only 3.44:1 on `--bg` and 3.94:1 on `--surface`, so accent-as-text (active tab, secondary button, links, readouts, `.schedule` stamps) uses the darker `--accent-text` `#20589d`. The app bar is the measured grey title bar (`#cdcdcd` to `#a8a8a8`), so its brand and items are near-black (`#1c1c1e`, `#2a2b2e`); the accent-blue brand measured 3.5:1 on its foot. A standalone `.nav` brand uses `--accent-text` too (raw accent was 3.9:1 on the nav gradient).
- **Gel buttons, measured:** the default (`.btn-primary`) button is Snow Leopard's pale blue gel with a black label, and the push button is the flat-topped grey gel that lightens to white at the bottom, both sampled from `31db2b68338d1ae9.png` (see `RESEARCH.md`). Black on the palest stop of the blue gel is well over 7:1.
- `--accent-2` `#5aa6ff` is 1.86:1 on `--bg`: decoration/flare only, never text. `--warning` `#b0741a` is 2.89:1 on `--bg`; text uses `--warning-text` `#764d10`.
- **State text tokens** are dark enough for their own 20% badge tints and the diff-line tints: `--success-text` `#2c6024` (4.95:1 on the success badge), `--danger-text` `#a02818` (4.73:1), `--warning-text` `#764d10` (5.06:1). They were `#37762c`, raw `--danger` and `#915f15`, about 3.4–3.7:1 there.

## Reference status

`references/aqua/` has 6 captures plus `RESEARCH.md` (one Leopard icon grid with people in icons was removed): a Panther Finder window, a Leopard Guest Finder window, a Snow Leopard widget gallery, Aqua toolbar controls, a Leopard icon set (`leopard-huge-iconpack-650-screenshot.avif`) and a Leopard app-icon grid. They back the gel buttons, pinstripes, brushed metal and traffic-light controls. Gaps: no dedicated Dock-reflection capture, and the folder is Panther/Leopard-heavy rather than 10.6 Snow Leopard (the theme's stated target), apart from the Snow Leopard controls sheet `31db2b68338d1ae9.png`, which `RESEARCH.md` measures for the title bar, traffic lights and buttons.

## Icons

`themes/aqua/icons.svg` redraws the whole core set (178/178) as pillowy
candy-UI line icons:

- 24×24 grid, line only: no fills, colour from `currentColor`, weight and
  round caps/joins inherited from `.icon` (no `<g>` wrapper, no cap overrides).
- True curves kept; rectangles get generous radii (rx 2–4), pages use the
  rounded dog-ear outline of `icon-file`.
- Dots are r 0.7 stroked rings.
- Gloss: on about one icon in six, a short `stroke-width="3"` arc rides the
  top-left inside of the lead circle or box (info, clock, search, lock…),
  only where that corner is empty. It is the only hard-coded weight.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
