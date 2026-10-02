# Contributing a theme

The checklist from brief to merge. [`authoring-a-theme.md`](authoring-a-theme.md)
explains how a theme file works. This page is the order of work and what a
reviewer will check. If an agent is building the theme, give it
[`agent-theme-brief.md`](agent-theme-brief.md).

You can help without building a theme: gathering references for a theme
that has none (see [`references/README.md`](../references/README.md)) is
just as useful.

## 1. Brief

Write down, before any CSS:

- **The slug**: lowercase kebab-case (`westworld`, `win7-aero`). It names
  the theme folder, the references folder, the bundle and `data-theme`.
- **The primary source**: the one product, film, game or material the
  theme reproduces, and what you will do where sources disagree.
- **Palette variants**, if any, with their ids (`lcars~voyager`). Each id
  names a references subfolder and a `[data-variant]` block.
- **Fonts**: what the original uses, and whether a free (OFL, Apache, CC0)
  face is close enough to vendor.

## 2. References

Everything goes in **`references/<slug>/`**. Material that backs only one
palette variant goes one level down in **`references/<slug>/<variant>/`**,
using the variant id from `dist/themes.json`. Never name a folder after the
website it came from, and never file another interface's material under
this theme: reference material for a theme that doesn't exist yet gets its
own folder named for that would-be theme (`references/star-trek-tos/`).

**File names describe the components the image shows**, in camelCase, with
`-` between components: `elbowFrame-pillButton.webp`,
`table-tabs-selectedRow.webp`, `progressDialog-openingDrive.jpg`.

**Keep only what earns its place.** Score each image out of 10 for how much
it tells you about the look. Delete anything under 5, duplicates, and
images another one already covers. Resize to at most 1600px (JPEG quality
70-80, or WebP). Ten to fifteen good images beat fifty.

**Licences and credits.** References are filed as design references for
comparison only; the theme reproduces none of them, and no logo, emblem,
screenshot or game art ships in a theme. Record the source page, the image
URL and the credit or licence for every file. Prefer Wikimedia Commons and
other openly licensed sources where the subject allows it.

### RESEARCH.md

`references/<slug>/RESEARCH.md` is required. Sections, in this order:

1. **Intro paragraph** (no heading): what the theme is, whose work the
   images are (© holder), that they are filed only as design references,
   when the research was done, and anything that could not be fetched.
2. **`## Primary direction`** (or `## Primary source`): the source the
   theme follows and why, and what it takes from secondary sources.
3. **`## Images`**: a table of `File | Source / credit | What it shows`,
   one row per file, with the source page URL, the image URL and the
   licence or credit. Variant subfolders get their own rows (or their own
   RESEARCH.md).
4. **`## Sampled palette`**: colours sampled from the images (say how:
   eyedropper, ImageMagick quantisation) next to the token values the
   theme uses, and why they differ where they do (usually contrast).
5. **`## Typography`**: the faces the original uses, what the theme uses
   instead, and what is vendored.
6. **`## Component mapping`**: a table of `Component | Reference |
   Treatment`, from page and `.app` shell through panels, buttons, tables,
   tabs, inputs, modals and their close control, to badges and meters.
7. **`## Gaps`**: what no good reference was found for, and what the theme
   did there.

Add the theme's row to `references/README.md` (reference links and "what
to compare"), and list any variant folders there.

## 3. Fonts

A face the theme names must be one that ships. Vendor it in
**`assets/fonts/`** as woff2, subset to Latin plus the glyphs the theme
uses, with a local `@font-face` whose `url("assets/fonts/…")` the build
rewrites for `dist/`. Add an entry to **`assets/fonts/NOTICE.md`**: family,
weights and files, designer, licence (verified on the family's own page,
not assumed), source URL and the themes that use it. Ship the licence text
beside the font when the licence asks for it (`DSEG-LICENSE.txt`).

A face that can't be vendored is not named in the stack. Say so in a "Note
on fonts" in the theme's header comment instead (see `skyrim` or `tron`).
No remote `url()` or `@import`, ever (the lint fails it).

Budgets (warnings for now, see `scripts/check.py`): 40 KiB per font file,
64 KiB of fonts per theme.

## 4. Build the theme

`scripts/new-theme.sh <slug>` scaffolds `themes/<slug>/theme.css`. Fill in
`Theme-Name:` and `Description:` in the header, then:

- **Tokens only on base components.** Set component looks through
  `--<component>-*` custom properties at root scope. Never declare
  `background`, `background-color` or `color` on a base component selector
  (`html[data-theme="x"] .btn`): it outranks core's `.btn-danger` and
  friends and erases them. Shape properties (radius, clip-path, border
  colours) on the base selector are fine. The lint enforces this.
- **Contrast**: `--on-accent`, `--on-danger`, `--on-success` reach 4.5:1 on
  their fills; body text 4.5:1 on `--surface`. Declare `color-scheme`.
- **Layout**: set `--app-*` so the shell rearranges for the theme.
- **v5 tiers.** No breakpoints of your own: mobile ≤480, tablet 481-900,
  desktop 901-1800, XL ≥1801 are core's. Set per-tier tokens at the root
  (`--app-areas-mobile|-tablet`, `--app-rows-*`, `--app-rail-display-*`,
  `--app-main-padding-*`, `--app-columns-*`). On touch tiers the bar is
  brand and actions on line one, the nav scrolling on line two; don't fight
  it with fixed bar heights or absolutely positioned decoration. Scale
  display type down on mobile. Where a theme rule really must depend on
  width, use the tier numbers in `@media`/`@container`.
- **XL gutter art**: `--app-gutter-art`, CSS background layers only (no
  bitmaps), in the theme's own language, within about 1.5:1 of `--bg`, still
  by default. Any motion is slow, inside
  `@media (prefers-reduced-motion: no-preference)` and
  `:not([data-motion="reduced"])`, with keyframes prefixed by the slug
  (see `blue-future`).
- **Nesting steps down.** A panel, card, modal or drawer inside another is
  quieter than the outer one: drop the second title bar, window controls,
  reflections, blur, corner ornaments and heavy shadows (Win7's nested
  windows become group boxes; Aqua's lose their traffic lights). Check every
  combination on `nesting.html`.
- **A period-correct close button**, through the close tokens:
  `--btn-close-glyph`, `--btn-close-bg`, `--btn-close-width`,
  `--btn-close-height`, `--btn-close-pad`, `--btn-close-font-size`,
  `--btn-close-glyph-size`, and `--btn-close-order: -1` with
  `--btn-close-push: 0` to put it at the start of the title bar (Mac OS).
  Minimise and maximise follow the title bar and group with close.
- **Layers and cursor**: global layers use the `--z-*` scale; controls keep
  the arrow cursor (no `cursor: pointer`).
- **Motion**: infinite animation only inside
  `prefers-reduced-motion: no-preference`; state is never carried by motion
  or colour alone.
- **CSS-only interaction keeps working**: style selection with `.is-active`
  / `[aria-selected="true"]` (the build extends them to checked hidden
  radios), and hover inside `@media (hover: hover)` with a
  `:focus-visible` equivalent.

## 5. Document it

- **`themes/<slug>/README.md`**: what the theme is trying to achieve, core
  values as numbered rules, signature details, why the significant token
  values are what they are, what not to change, the tell-tales of an
  inauthentic result, a `Requires: L0` or `L1` badge, a `contrast-exempt:`
  rationale if a soft contrast floor is waived on purpose, and a "v5
  layout" section (tiers, phone and tablet, gutter art, nesting).
- A row in **`CONTRACT.md`**'s theme index.

## 6. Run `scripts/theme-ready.sh <slug>`

```sh
scripts/theme-ready.sh <slug>                  # Chromium
scripts/theme-ready.sh <slug> --engine webkit  # and WebKit, if installed
```

It builds, lints the theme, runs the core regressions, the v5 audit (theme
and variants; dashboard, components and nesting; all five devices), axe
(failing only on serious or critical issues the theme causes), the size
budgets and the render cost, and prints PASS/FAIL/WARN per gate. Every gate
must PASS; read each WARN. See [`test/README.md`](../test/README.md) for
each check and for installing Playwright and axe-core.

Then **look**: screenshot `dashboard.html`, `components.html` and
`nesting.html` at 393x852, 890x626, 1280x800 and 2560x1440, and compare
them with your references. Nothing overlapping or clipped, the theme reads
as itself at every size, gutter art visible but quiet at 2560. The checks
catch regressions; they don't judge likeness.

## 7. Merge

- `scripts/build.sh` and commit `dist/` with the source (consumers can't
  build), plus `python3 scripts/screenshot_themes.py --baseline --theme <slug>`
  for the new theme's screenshots.
- A `CHANGELOG.md` entry under Unreleased.
- `python3 scripts/check.py` with no failures across the repo.
