# ftl-themes

> **v4.0.0 — BREAKING.** The `ftl-` prefix is gone from every class name,
> custom property, keyframe and id (`.ftl-btn` → `.btn`, `--ftl-text` →
> `--text`), every bundle now sits in `@layer ui`, and there is **no
> backward-compatibility layer**. Migrate with `scripts/migrate-v4.py` — see
> [`docs/MIGRATING-v4.md`](docs/MIGRATING-v4.md) (including the class names that
> now collide with Bootstrap and Tailwind). The last v3 release lives on the
> `v3` branch; `main` always follows the latest version.

An app-agnostic design system and theme library for Go + HTMX (or any
server-rendered, htmx-swapped) applications: a small component
class vocabulary, a `--*` design-token contract, and a growing catalog
of 42 fully switchable themes — from LCARS to Windows 95 to a Matrix
terminal, Skyrim, Liquid Glass and black leather with gold.

**Live examples:** https://drevilish.github.io/ftl-themes/ — the gallery,
the component page and six demo apps, published from `main` by GitHub Pages.

- **Using it in an app:** read [`CONTRACT.md`](CONTRACT.md).
- **Icon pack, style & branding guide, per-theme scores against real
  references:** [`docs/branding-guide.md`](docs/branding-guide.md).
- **Building a new theme:** read [`docs/authoring-a-theme.md`](docs/authoring-a-theme.md)
  and run `scripts/new-theme.sh <slug>`.
- **Trying themes without any app:** serve the repo root over HTTP and open
  [`components.html`](components.html) — the component QA page. A picker (built
  from `dist/themes.json`) and a stepper (buttons or ←/→) switch the
  applied theme; the markup never changes, so this is also the fair way to
  compare two themes' own CSS rather than two different pages' content.
  Every component appears once, htmx states included, an L0/L1
  toggle shows the app-shell-adopted layout difference, and the current
  theme's own `README.md` renders beside the render as a live "Core
  values" / "Tell-tales of an inauthentic result" checklist, so drift
  between a theme and its design doc is visible while you tick items off.
  A "Compare two" mode puts two themes side by side.
- **Browsing every theme at once:** [`gallery.html`](gallery.html) — a
  filterable grid with a screenshot of each theme (pick which example page
  shows in each card). The screenshots live in `test/visual-baseline/`;
  regenerate a theme's with `scripts/screenshot_themes.py --baseline --theme <slug>`.
- **Demo apps:** [`dashboard.html`](dashboard.html),
  [`marketing.html`](marketing.html), [`ticketsystem.html`](ticketsystem.html),
  [`powerstation.html`](powerstation.html), [`soundmixer.html`](soundmixer.html)
  and [`livechat.html`](livechat.html), each with the theme picker.
- **What each theme is copying:** [`references/`](references/README.md) —
  real reference images, one folder per theme (`references/<theme>/`) and
  one subfolder per palette variant (`references/<theme>/<variant>/`),
  each with a `RESEARCH.md`. Image filenames name the UI components they
  show, in camelCase, `-` between components (`elbowFrame-pillButton.webp`).
- **Engine-level recommendations** (what's been reviewed and what's still
  open): [`docs/engine-improvements.md`](docs/engine-improvements.md).
- **Upgrading:** [`CHANGELOG.md`](CHANGELOG.md) — v2.0.0 renamed the tokens
  and changed how themes override components.

Themes control **layout**, not just colour: adopt the app shell once
(`.app` + bar/rail/main/status) and switching theme re-arranges it —
LCARS opens its candy rail and elbows the bar into it, a HUD theme runs
edge-to-edge. It ships **instrument primitives** (`.meter`,
`.readout`, `.transport`/`.btn-go`, `.lamp`) for control
surfaces, and handles htmx's own swap states (`.htmx-request`,
`.indicator`) so consuming apps don't hand-roll pending UI.

Every theme has a `README.md` beside its CSS explaining what it is trying
to achieve and how to extend it without drifting.

## Icons

One generic SVG sprite (`assets/icons/icons.svg`, ~55 outline icons) backs
every `.icon`, with a per-theme override mechanism on top:
`themes/<slug>/icons.svg` (optional) redraws a subset of icon ids in that
theme's own visual language, and `scripts/build.sh` merges it with the
generic set into `dist/icons/<slug>.svg` — any icon a theme doesn't
override still falls back to the generic shape, which is also what a
theme with no `icons.svg` at all uses for everything. Six themes
currently ship real custom icon sets this way — `windows95`, `teletext`,
`matrix`, `winxp-luna`, `lcars` and `nokia-3310` — and any other theme can
add its own the same way, by dropping a `themes/<slug>/icons.svg` beside
its `theme.css`. See CONTRACT.md "Icon system" for the full mechanism.

## Layout

```
CONTRACT.md              token + component contract, the thing to read first
core/                     reset.css + core.css — theme-independent structure
themes/<name>/theme.css   one file per theme: tokens + look-only overrides
themes/lcars/chrome.css   optional decorative LCARS chrome (docs/lcars-chrome.md)
dist/<name>.css           built bundle (reset+core+theme), the file apps link
dist/core.css         reset+core alone, no theme/shell (color-only adoption)
dist/tokens.css           every theme's tokens only, one file, for apps that keep their own markup
dist/themes.json          machine-readable theme index for pickers, incl. build version
assets/                   fonts and other binary assets themes reference
scripts/build.sh          regenerates dist/ from core/ + themes/
scripts/check.sh          contract lint (tokens, contrast, focus, variants, dist sync)
scripts/new-theme.sh      scaffolds a new themes/<slug>/theme.css
references/<name>/        reference images + RESEARCH.md per theme (variants in subfolders)
test/visual-baseline/     per-theme screenshots, shown by gallery.html
index.html                redirects the Pages site root to gallery.html
docs/                     authoring guide, LCARS chrome spec, branding guide
```

Serve `dist/` and `assets/` as siblings — bundled CSS resolves fonts as
`../assets/…`.

No app-specific integration notes live in this repo — those belong in
each consuming app's own repository.
