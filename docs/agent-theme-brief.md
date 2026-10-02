# Agent brief: build (or v5-update) a theme

A reusable brief for an agent building a new theme, or bringing an existing
one up to v5. It is the brief used for `tokie`, `silo`, `westworld` and
`skyrim`, merged with the v5 rollout brief and updated with what changed
since (tiers, the nesting pass, close tokens, CSS-only interaction). Replace
the `<…>` placeholders and paste it as the task. The human checklist is
[`contributing-a-theme.md`](contributing-a-theme.md).

---

Repo: `<repo path>` (ftl-themes, a CSS design system: core component
classes plus switchable themes, built into `dist/<slug>.css`). Your theme:
**`<slug>`**, reproducing **`<primary source>`**. Variants: `<none | ids>`.
Scratch directory: `<scratch dir>` (screenshots and throwaway scripts go
here, never in the repo).

Read first: `CONTRACT.md` ("How a theme overrides a component", "Screen
tiers (v5)", "Touch and pointer (v5)", "v5 component groups" including the
close button tokens, "CSS-only selection, tabs and panes (v5)", "Floating
surfaces, menus and nesting (v5)"), `docs/authoring-a-theme.md`,
`docs/contributing-a-theme.md`, and `themes/blue-future/theme.css` (the
reference v5 theme: its XL gutter-art block) plus the closest existing
theme in spirit.

## What you own

ONLY `themes/<slug>/`, `references/<slug>/` (new theme), and new font files
plus their entries in `assets/fonts/NOTICE.md`. Do NOT edit `core/`,
`scripts/`, `dist/` (the build regenerates it), `CONTRACT.md`, `PLAN.md`,
`CHANGELOG.md`, example pages, or other themes. Other agents work in
parallel. Do not commit or push. If core needs a change, say so in your
report with the change you recommend.

## 1. References (new theme)

- Gather 10-15 strong images into `references/<slug>/` (variant-only
  material in `references/<slug>/<variant>/`). Name each by the components
  it shows, camelCase, `-` between components:
  `relicDatabase-headerPlate-fieldGrid.jpg`. Score each out of 10 and
  delete anything under 5, duplicates and already-covered images. Resize to
  ≤1600px.
- Record the source page, image URL and credit/licence for every file.
  Prefer openly licensed sources (Wikimedia Commons). Nothing from the
  references ships in the theme: no logos, emblems or screenshots.
- Write `references/<slug>/RESEARCH.md` with: an intro paragraph (what,
  whose, design-reference-only, date, what couldn't be fetched);
  `## Primary direction`; `## Images` (File | Source / credit | What it
  shows); `## Sampled palette` (sampled vs theme values); `## Typography`;
  `## Component mapping` (Component | Reference | Treatment);
  `## Gaps`. Add the theme's row to `references/README.md`.

## 2. Fonts

Vendor any face the theme names into `assets/fonts/` (woff2, Latin subset,
OFL/Apache/CC0 only, licence verified on the family's own page) with a
local `@font-face` using `url("assets/fonts/…")`, and add its entry to
`assets/fonts/NOTICE.md`. If no free face is close enough, don't name the
original in the stack: write a "Note on fonts" in the theme header. No
remote URLs anywhere. Budget: 40 KiB per file, 64 KiB per theme.

## 3. The theme

1. `scripts/new-theme.sh <slug>` (new theme). Fill `Theme-Name:` and
   `Description:`.
2. **Tokens**: every required token; `--on-*` at 4.5:1 on their fills;
   `color-scheme`. Component looks through `--<component>-*` at root scope.
   **Never** `background`/`background-color`/`color` on a base component
   selector (it erases `.btn-danger` and the other variants). Shape
   properties on the base selector are fine.
3. **Layout**: `--app-*` so the shell rearranges for the theme.
4. **Tiers**: mobile ≤480, tablet 481-900, desktop 901-1800, XL ≥1801. No
   ad-hoc `@media (max-width: 720px)` (or 960/1000px): set the per-tier
   tokens at the theme root (`--app-areas-mobile|-tablet`,
   `--app-rows-*`, `--app-rail-display-*`, `--app-main-padding-*`,
   `--app-columns-*`); core applies them per tier. Decide what tablet
   (890x626 landscape foldable) gets: a decorative rail can stay if it costs
   no content width.
5. **Phone and tablet quality**: the bar is brand + actions on line 1
   (brand truncates) and nav scrolling on line 2 (core does this). Don't
   fight it with fixed bar heights, absolutely positioned decoration, huge
   brand type or pseudo-element window buttons over content. Scale display
   type down on mobile. Keep the theme recognisable.
6. **XL gutter art**: `--app-gutter-art`, CSS background layers only, in
   the theme's language, within about 1.5:1 of `--bg`, still by default.
   Motion only slow, inside `prefers-reduced-motion: no-preference` and
   `:not([data-motion="reduced"])`; keyframes prefixed with the slug.
7. **Nesting pass**: nested panels, cards, modals and drawers step down
   instead of repeating full decoration: no second title bar, window
   controls, blur, reflection, corner ornaments or heavy shadow inside a
   surface. Check every case on `nesting.html`.
8. **Close button**: period-correct, through the tokens
   (`--btn-close-glyph`, `--btn-close-bg`, `--btn-close-width`,
   `--btn-close-height`, `--btn-close-pad`, `--btn-close-font-size`,
   `--btn-close-glyph-size`; `--btn-close-order: -1` +
   `--btn-close-push: 0` for start placement). Minimise/maximise follow the
   title bar's colour and group with close.
9. **Layers and cursor**: global layers on the `--z-*` scale (local
   `z-index: 1` inside a component may stay); no `cursor: pointer`.
10. **CSS-only interaction**: pages switch tabs and select items with hidden
    radios and open drawers/menus with `popover`. Style selected states with
    `.is-active` / `[aria-selected="true"]` (the build extends them to
    checked radios); keep hover inside `@media (hover: hover)` with a
    `:focus-visible` equivalent; a toggle's two labels must not change its
    width.
11. **Motion**: infinite animation only inside
    `prefers-reduced-motion: no-preference`. State never by colour or
    motion alone.
12. **README.md**: intent, core values (numbered), signature details, token
    rationale, what not to change, tell-tales of an inauthentic result,
    `Requires: L0|L1` badge, and a "v5 layout" section (tiers, phone/tablet,
    gutter art, nesting). New theme: also say what CONTRACT.md's theme index
    row should be (in your report; you don't edit CONTRACT.md).

## 4. Verify

```sh
scripts/theme-ready.sh <slug>
```

Every gate must PASS (build, lint, core regressions, v5 audit, axe for
issues the theme causes); report each WARN (budgets, render cost). Gate
logs are in `$TMPDIR/theme-ready-<slug>/`. A lint note about stale `dist/`
or other themes is not yours.

Then screenshot with Playwright and LOOK at every image. Serve the repo
(`python3 -m http.server <random free port>`; pages take `?theme=<slug>`
and `&variant=<id>`) and shoot `dashboard.html`, `components.html` and
`nesting.html` at 393x852 (isMobile, hasTouch), 890x626 (hasTouch),
1280x800 and 2560x1440. Import Playwright from the repo and point it at the
installed browser, for example:

```js
import { chromium } from '<repo path>/scripts/node_modules/playwright/index.mjs';
const browser = await chromium.launch({
  executablePath: '/root/.cache/ms-playwright/chromium-1234/chrome-linux64/chrome', // this machine's path; yours may differ
});
```

(The repo's own scripts find an installed Chromium by themselves; set
`CHROMIUM_PATH` to override.) The theme must read as itself at every size,
nothing overlapping or clipped, gutter art visible but quiet at 2560.
Compare 1280 with `test/visual-baseline/<slug>/dashboard.png` by eye when
updating an existing theme.

## 5. Report

- What you built or changed, and the gutter art in one line.
- The `theme-ready.sh` summary (each gate's line), plus overflow per device
  and small targets on mobile from the v5 audit.
- Anything you could not fix in the theme, with the core change you
  recommend.
- New theme: the reference count and gaps, fonts vendored (with licence),
  and the CONTRACT.md theme index row.
