# Aqua

> macOS Snow Leopard — brushed metal, pinstripes, candy gloss.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

**Mac OS X circa 10.6**: glossy "candy" controls, brushed-metal window
chrome, pinstriped surfaces, and generous soft shadows. Optimistic,
tactile, unmistakably pre-flat-design.

## Core values

1. **Everything is lit from above.** A control is a gradient from light to
   dark with a bright top highlight inset. That single convention produces
   most of the look.
2. **Gloss on fills, gloss only.** Gradients belong on buttons, bars and
   panels — never on text or borders.
3. **Depth is soft, not hard.** Large blurred shadows at low opacity; no
   crisp 1px drop shadows.
4. **The window floats.** The shell has rounded corners and sits on a
   desktop gradient with a real shadow beneath it.
5. **Light theme discipline.** This is the catalogue's first light theme,
   so filled controls need explicit white foregrounds — the dark-theme
   habit of painting them `--bg` fails here. That's exactly what
   `--on-accent`/`-danger`/`-success` are for.

## Signature details

- Panels carry an actual **pinstripe**: a 3px repeating white-at-35%
  gradient over the surface gradient.
- The modal header is centred, with its own metal gradient — a Mac sheet.
- Selected table rows fill solid Aqua blue with white text.
- Focus adds a soft 3px blue halo rather than a hard ring.

## Layout

The shell becomes a **Mac window**: 0.75rem desktop margin, a rounded
brushed-metal title bar, a near-white content area, and a rounded metal
status strip, with a 28px blurred shadow under the whole frame.

## v5 layout

- **Tiers.** No rail on any tier. On phone and tablet (≤900px) the
  traffic lights stay level with the bar's first line (brand and actions)
  instead of centring on the wrapped two-line bar. On phones (≤480px) the
  window goes nearly full-screen and the bar's lights shrink to
  panel-header size so the brand keeps some room.
- **Nesting.** A panel or card inside another surface becomes an Aqua group
  box: a lighter flat inset (the parent's pinstripe shows through), no
  drop shadow, and no traffic lights, since only a window has window
  controls.
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

`--font` is `"Lucida Grande", "Helvetica Neue", Helvetica, Arial, sans-serif`; `--font-mono` is `Monaco, Consolas, monospace`. Lucida Grande is the authentic face (named in `references/aqua/RESEARCH.md`) and it is **system-only, not vendored**: it ships with macOS and is absent on Windows and most Linux, where Helvetica Neue/Arial render instead. Headings get a 1px white `text-shadow` (the "engraved" look); do not swap it for a heavier weight.

## Contrast honesty

- **`--muted` lifted:** `#6e7075` was 4.2:1; shipped `#58595e` is 5.16:1 on `--bg`, 5.91:1 on `--surface`, 6.99:1 on white. Checked against the darker panel gradient stop too.
- **Accent blue as text is not free.** `--accent` `#2a74d0` is 4.66:1 under white text (filled controls fine) but only 3.44:1 on `--bg` and 3.94:1 on `--surface`, so accent-as-text (active tab, secondary button, links, readouts, `.schedule` stamps) uses the darker `--accent-text` `#20589d`, and the app-bar brand uses `#174f9c` (the accent measured 3.8:1 there; muted items 4.0:1).
- **Gel button:** the primary gel's lower stop is deepened so its white label holds 4.5:1 across the whole button, at the cost of a slightly darker bottom than a raw Aqua screenshot.
- `--accent-2` `#5aa6ff` is 1.86:1 on `--bg`: decoration/flare only, never text. `--warning` `#b0741a` is 2.89:1 on `--bg`; text uses `--warning-text` `#764d10`.
- **State text tokens** are dark enough for their own 20% badge tints and the diff-line tints: `--success-text` `#2c6024` (4.95:1 on the success badge), `--danger-text` `#a02818` (4.73:1), `--warning-text` `#764d10` (5.06:1). They were `#37762c`, raw `--danger` and `#915f15`, about 3.4–3.7:1 there.

## Reference status

`references/aqua/` has 6 captures plus `RESEARCH.md` (one Leopard icon grid with people in icons was removed): a Panther Finder window, a Leopard Guest Finder window, a Snow Leopard widget gallery, Aqua toolbar controls, a Leopard icon set (`leopard-huge-iconpack-650-screenshot.avif`) and a Leopard app-icon grid. They back the gel buttons, pinstripes, brushed metal and traffic-light controls. Gaps: no dedicated Dock-reflection capture, and the folder is Panther/Leopard-heavy rather than 10.6 Snow Leopard (the theme's stated target). `RESEARCH.md` gives no hex values.

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
