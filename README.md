# ftl-themes

An app-agnostic design system and theme library for Go + HTMX (or any
server-rendered, htmx-swapped) applications: a small `.ftl-*` component
class vocabulary, a `--ftl-*` design-token contract, and a growing catalog
of fully switchable themes — from a futuristic sci-fi HUD to LCARS to
Windows 95 to TRON.

- **Using it in an app:** read [`CONTRACT.md`](CONTRACT.md).
- **Building a new theme:** read [`docs/authoring-a-theme.md`](docs/authoring-a-theme.md)
  and run `scripts/new-theme.sh <slug>`.
- **Trying themes without any app:** open [`demo.html`](demo.html) in a
  browser, or serve the repo root and visit it — it has an in-page theme
  switcher exercising every component.
- **What's planned next:** [`docs/theme-backlog.md`](docs/theme-backlog.md).

## Layout

```
CONTRACT.md              token + component contract, the thing to read first
core/                     ftl-reset.css + ftl-core.css — theme-independent structure
themes/<name>/theme.css   one file per theme: tokens + look-only overrides
themes/lcars/chrome.css   optional decorative LCARS chrome (docs/lcars-chrome.md)
dist/<name>.css           built bundle (reset+core+theme), the file apps link
assets/                   fonts and other binary assets themes reference
scripts/build.sh          regenerates dist/ from core/ + themes/
scripts/new-theme.sh      scaffolds a new themes/<slug>/theme.css
docs/                     authoring guide, LCARS chrome spec, theme backlog
```

No app-specific integration notes live in this repo — those belong in
each consuming app's own repository.
