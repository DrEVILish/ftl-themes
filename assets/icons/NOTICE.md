# Third-party icon attribution

`assets/icons/icons.svg`'s generic icon set is a mix of original,
in-house line drawings (the initial ~100 icons — see
`docs/icon-library-roadmap.md` Phase 1) and bulk-vendored icons from
**Tabler Icons**, added to grow the set toward the 1,000-icon Phase 2
target (1,020 symbols total as of the follow-up additions noted below).

## Source

- **Project:** Tabler Icons (<https://github.com/tabler/tabler-icons>)
- **License:** MIT License
- **Copyright:** Copyright (c) 2020-2026 Paweł Kuna
- **Version vendored:** 3.48.0 (`package.json` at the pulled commit)
- **Commit:** `0239805680a36bab4e1070529b6744924402d804`
- **Commit date:** 2026-09-22
- **Date pulled:** 2026-09-24
- **Set used:** the `icons/outline/` variant only (24x24 viewBox,
  stroke-based, `currentColor`-friendly — matches this project's existing
  icon convention)
- **Icon count vendored:** 917 symbols (900 from the general category
  sweep below, plus 17 currency symbols added afterward), plus 3
  follow-up additions from the same Tabler source/version
  (`icon-qr-code` ← `qrcode`, `icon-hourglass` ← `hourglass`,
  `icon-timer` ← `stopwatch` artwork for the timer concept) requested by
  a consuming app — 920 vendored symbols total.

Verbatim license text, as retained in the upstream repository's `LICENSE`
file at the commit above:

```
MIT License

Copyright (c) 2020-2026 Paweł Kuna

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

This file is `ftl-themes`'s "include the license notice with substantial
portions of the Software" — the MIT license's one substantive
redistribution requirement — satisfied for this vendored batch. It sits
in the same repository as the vendored SVG data (`assets/icons/icons.svg`)
so it travels with the asset for any downstream consumer.

## What was changed from the upstream files

Each vendored icon was mechanically converted, with **no artwork
changes**, to fit this project's existing symbol convention:

- Wrapped in `<symbol id="icon-<name>" viewBox="0 0 24 24">...</symbol>`
  (Tabler's own `viewBox="0 0 24 24"` was already correct and untouched).
- The outer `<svg>` element's `width`, `height`, `stroke="currentColor"`,
  `stroke-width="2"`, `stroke-linecap`, `stroke-linejoin`, and
  `fill="none"` attributes were stripped, since this project's
  `.ftl-icon` class (`core/ftl-core.css`) supplies all of those via CSS
  on every symbol uniformly. This matches the convention of the
  original 100 icons.
- The per-file leading XML comment block (Tabler's tag/category/unicode
  metadata) was stripped; it was documentation for Tabler's own site, not
  needed here.
- A handful of Tabler source icons intentionally hardcode
  `fill="currentColor"` on small filled-dot details inside an otherwise
  stroke-only glyph (e.g. `icon-discount`, `icon-accessible`). That
  attribute was **kept as-is** — it already uses the same `currentColor`
  token as this project's `.ftl-icon` stroke color, so it is not a
  hardcoded color and needs no normalization.
- No path data, shapes, or geometry were altered.

## What was excluded

Per `docs/icon-library-roadmap.md`'s "hard exclusion: no third-party
company logos or trademarks" policy:

- Every file under Tabler's `icon-brand-*` naming (e.g.
  `brand-github`, `brand-spotify`) was excluded — those are actual
  company/product logos and belong in the separate `assets/logos/`
  system (see the roadmap's "Icon packs vs. logo packs" section), not
  this generic icon pack.
- Every `icon-flag-*` (national flags) was excluded — out of scope for
  this batch.
- Numbered stroke-style duplicates of an already-selected concept (e.g.
  Tabler ships some icons in both a base form and a `-2`/`-3` alternate
  line-weight variant) were skipped, keeping only one shape per concept.
- Generic currency symbols (`icon-currency-*`, e.g. dollar, euro, yen,
  bitcoin) are **not** company trademarks — they're universal financial
  symbols — so a curated set of the most common ones was included.

## Selection method

Given the scale (900+ icons out of Tabler's ~5,900), icons were selected
by keyword-matching against the categories in
`docs/icon-library-roadmap.md`'s Phase 2 batch list (file types, media,
hardware, communication, commerce, weather, maps, accessibility, social,
data/charts, security, dev/code, arrows, faces, seasonal, plus a few
extra categories: nature, people, sports, home, health, text-formatting),
capped per category to avoid one prolific category (arrows had 249
matches) crowding out smaller ones, then topped off alphabetically from
the remaining pool to reach the batch target. Icons whose id would
exactly collide with one of the original 100 hand-drawn ids were skipped
(the hand-drawn original is kept in that case).
