# ftl-themes

An app-agnostic design system and theme library for Go + HTMX (or any
server-rendered, htmx-swapped) applications: a small `.ftl-*` component
class vocabulary, a `--ftl-*` design-token contract, and a growing catalog
of fully switchable themes — from a futuristic sci-fi HUD to LCARS to
Windows 95 to TRON.

- **Using it in an app:** read [`CONTRACT.md`](CONTRACT.md).
- **Building a new theme:** read [`docs/authoring-a-theme.md`](docs/authoring-a-theme.md)
  and run `scripts/new-theme.sh <slug>`.
- **Trying themes without any app:** serve the repo root over HTTP and open
  [`demo.html`](demo.html) — an in-page switcher (built from
  `dist/themes.json`) exercises every component, htmx states included, plus
  a `?chrome=1` LCARS chrome mode.
- **Auditing a theme against its own design doc:** serve the repo root over
  HTTP and open [`example.html`](example.html) — every `.ftl-*` component in
  one scroll, a theme stepper (buttons or ←/→), and the current theme's own
  `README.md` rendered as a live "Core values" / "Tell-tales of an
  inauthentic result" checklist beside the render, so drift between a theme
  and its design doc is visible while you tick items off.
- **What's planned next:** [`docs/theme-backlog.md`](docs/theme-backlog.md).
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

## Layout

```
CONTRACT.md              token + component contract, the thing to read first
core/                     ftl-reset.css + ftl-core.css — theme-independent structure
themes/<name>/theme.css   one file per theme: tokens + look-only overrides
themes/lcars/chrome.css   optional decorative LCARS chrome (docs/lcars-chrome.md)
dist/<name>.css           built bundle (reset+core+theme), the file apps link
dist/ftl-core.css         reset+core alone, no theme/shell (color-only adoption)
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
