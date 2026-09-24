# ftl-themes

An app-agnostic design system and theme library for Go + HTMX (or any
server-rendered, htmx-swapped) applications: a small `.ftl-*` component
class vocabulary, a `--ftl-*` design-token contract, and a growing catalog
of fully switchable themes — from LCARS to Windows 95 to a Matrix
terminal.

- **Using it in an app:** read [`CONTRACT.md`](CONTRACT.md).
- **Icon pack, style & branding guide, per-theme scores against real
  references:** [`docs/branding-guide.md`](docs/branding-guide.md).
- **Building a new theme:** read [`docs/authoring-a-theme.md`](docs/authoring-a-theme.md)
  and run `scripts/new-theme.sh <slug>`.
- **Trying themes without any app:** serve the repo root over HTTP and open
  [`example.html`](example.html) — the one example page. A picker (built
  from `dist/themes.json`) and a stepper (buttons or ←/→) switch the
  applied theme; the markup never changes, so this is also the fair way to
  compare two themes' own CSS rather than two different pages' content.
  Every `.ftl-*` component appears once, htmx states included, an L0/L1
  toggle shows the app-shell-adopted layout difference, and the current
  theme's own `README.md` renders beside the render as a live "Core
  values" / "Tell-tales of an inauthentic result" checklist, so drift
  between a theme and its design doc is visible while you tick items off.
  A "Compare two" mode puts two themes side by side.
- **Browsing every theme at once:** [`gallery.html`](gallery.html) — a
  filterable grid with a live, scaled-down preview of each theme (pick
  which example page renders in each card).
- **What's planned next:** [`docs/theme-backlog.md`](docs/theme-backlog.md).
- **Engine-level recommendations** (what's been reviewed and what's still
  open): [`docs/engine-improvements.md`](docs/engine-improvements.md).
- **Upgrading:** [`CHANGELOG.md`](CHANGELOG.md) — v2.0.0 renamed the tokens
  and changed how themes override components.

Themes control **layout**, not just colour: adopt the app shell once
(`.ftl-app` + bar/rail/main/status) and switching theme re-arranges it —
LCARS opens its candy rail and elbows the bar into it, a HUD theme runs
edge-to-edge. It ships **instrument primitives** (`.ftl-meter`,
`.ftl-readout`, `.ftl-transport`/`.ftl-btn-go`, `.ftl-lamp`) for control
surfaces, and handles htmx's own swap states (`.htmx-request`,
`.ftl-indicator`) so consuming apps don't hand-roll pending UI.

Every theme has a `README.md` beside its CSS explaining what it is trying
to achieve and how to extend it without drifting.

## Icons

One generic SVG sprite (`assets/icons/icons.svg`, ~55 outline icons) backs
every `.ftl-icon`, with a per-theme override mechanism on top:
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
core/                     ftl-reset.css + ftl-core.css — theme-independent structure
themes/<name>/theme.css   one file per theme: tokens + look-only overrides
themes/lcars/chrome.css   optional decorative LCARS chrome (docs/lcars-chrome.md)
dist/<name>.css           built bundle (reset+core+theme), the file apps link
dist/ftl-core.css         reset+core alone, no theme/shell (color-only adoption)
dist/tokens.css           every theme's tokens only, one file, for apps that keep their own markup
dist/themes.json          machine-readable theme index for pickers, incl. build version
assets/                   fonts and other binary assets themes reference
scripts/build.sh          regenerates dist/ from core/ + themes/
scripts/check.sh          contract lint (tokens, contrast, focus, variants, dist sync)
scripts/new-theme.sh      scaffolds a new themes/<slug>/theme.css
docs/                     authoring guide, LCARS chrome spec, theme backlog
```

Serve `dist/` and `assets/` as siblings — bundled CSS resolves fonts as
`../assets/…`.

No app-specific integration notes live in this repo — those belong in
each consuming app's own repository.
