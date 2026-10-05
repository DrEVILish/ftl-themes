# Testing

All the rendered checks run through Playwright from `scripts/node_modules`
(gitignored, no package.json). Install Playwright and axe-core there in
**one** command: npm prunes any package a later `npm i` doesn't name, so
installing axe-core alone deletes Playwright.

```sh
npm i --no-save --no-package-lock --prefix scripts playwright@1.63.0 axe-core
npx --prefix scripts playwright install chromium   # skip if a Chromium is already in ~/.cache/ms-playwright
```

Any Playwright-downloaded Chromium works (CDP tolerates a version
mismatch): if the one this Playwright expects is missing, the scripts use
the newest `chromium_headless_shell-*` or `chromium-*` in
`$PLAYWRIGHT_BROWSERS_PATH` or `~/.cache/ms-playwright`. `CHROMIUM_PATH`,
`FIREFOX_PATH` and `WEBKIT_PATH` override the executable. Shared plumbing
(engines, known issues, the static server, the theme-ready wait) lives in
`scripts/_harness.mjs`.

| Script | What it checks |
|---|---|
| `scripts/theme-ready.sh <slug>` | Every gate below for one theme, with a PASS/FAIL/WARN summary |
| `scripts/check.sh` (`check.py`) | Contract lint; optional `--budgets` size report |
| `scripts/core_regressions.mjs` | Core layout bugs reported by adopting apps |
| `scripts/v5_audit.mjs` | Overflow, touch targets, spacing, text-to-edge, XL cap |
| `scripts/a11y_audit.mjs` | axe-core on every example page |
| `scripts/render_cost.mjs` | Scrolling frame time on a throttled phone |
| `scripts/screenshot_themes.py` | Screenshot baselines |

# Ready for review: `scripts/theme-ready.sh`

```sh
scripts/theme-ready.sh westworld                    # chromium
scripts/theme-ready.sh westworld --engine webkit    # add engines (repeatable)
```

Runs, in order: `build.sh`; `check.py --theme <slug>`;
`core_regressions.mjs <slug>`; `v5_audit.mjs` on the theme and its
variants (dashboard, components, nesting; all five devices; `--strict`);
`a11y_audit.mjs` on the theme and a reference theme with `--blame <slug>`
(fails only on serious/critical rules the theme causes, not ones every theme
shares); and `render_cost.mjs`. Render cost is a WARN gate. Budgets are
deferred and excluded from the default gate; run `python3 scripts/check.py
--budgets` when doing a later optimization pass. Logs go to
`$TMPDIR/theme-ready-<slug>/`
(default `/tmp`). Exit 1 when any gate FAILs.

# Engines and known issues

`v5_audit.mjs`, `core_regressions.mjs`, `a11y_audit.mjs` and
`screenshot_themes.py` take `--engine chromium|firefox|webkit`
(repeatable, default chromium). An engine that isn't installed prints a
`SKIP` line and the run carries on with the others.

`test/engine-known-issues.json` lists engine-specific differences that are
reported as warnings instead of failures:

```json
{ "webkit": [ { "script": "v5_audit", "match": "^aqua iphone-15-pro \\S+ overflow$",
                "reason": "WebKit sizes the gel scrollbar into the layout (bug link)" } ] }
```

`match` is a regular expression tested against the failure's key:

| script | key |
|---|---|
| `v5_audit` | `<theme> <device> <page> <check>`, check one of `overflow`, `targets`, `spacing`, `edgeText`, `xl`, `error` |
| `core_regressions` | `<theme>: <message>` (the FAIL line's text) |
| `screenshots` | `<theme>/<page>` |
| `a11y` | `<theme> <tier> <page> <axe rule id>` |

Keep entries narrow, give a reason (with the browser bug where there is
one), and delete them when the engine is fixed.

# Visual regression testing

`scripts/screenshot_themes.py` screenshots every theme in `dist/themes.json`
against every `example*.html` QA page at a fixed 1280x900 viewport, and
either accepts those screenshots as the new baseline or diffs them against
the committed one. `v5_audit.mjs` separately checks five device sizes;
`a11y_audit.mjs` checks Mobile and Desktop.

## Usage

```sh
python3 scripts/screenshot_themes.py              # diff mode: compare against test/visual-baseline/
python3 scripts/screenshot_themes.py --baseline    # (re)write the committed baseline
python3 scripts/screenshot_themes.py --threshold 0.5   # tune diff sensitivity
python3 scripts/screenshot_themes.py --engine webkit   # another engine (repeatable)
```

Chromium's baseline is `test/visual-baseline/`; each other engine has its
own, `test/visual-baseline-<engine>/` (engines rasterise text and gradients
differently, so they are never compared with each other). The diff needs
Pillow (`python3 -m pip install pillow`).

Diff mode reports a pass/fail and a diff percentage per theme/page, and
writes any failing comparisons to `test/visual-diffs/` (gitignored
scratch output, not committed) for manual review.

## When to use `--baseline`

Only after confirming a rendering change is *intentional* — e.g. one of
this project's theme fidelity fixes, a new theme, or a core CSS change
that's meant to affect how existing themes render. Re-running with
`--baseline` overwrites `test/visual-baseline/` with the current
rendering, so don't run it reflexively just because diff mode reported
failures — read the diffs first.

## What's committed vs. not

- `test/visual-baseline/<slug>/<page>.png` — committed. This is the
  accepted-good rendering of every theme × example page combination.
- `test/visual-baseline-<engine>/` — committed, once someone with that
  engine installed writes it.
- `test/visual-diffs/` — gitignored. Scratch output from a failing diff
  run, for local review only (`test/visual-diffs/<engine>/` for engines
  other than Chromium).

This is a local dev tool, not a CI gate — consistent with this project's
convention of running checks locally/manually rather than via GitHub
Actions (see CONTRACT.md).

# v5 audit (overflow, touch targets, spacing)

`scripts/v5_audit.mjs` is the PLAN.md §5 "Enforced by a check" pass. It
serves the repo root itself and loads every example page (plus
`nesting.html` when it exists) per theme at the five §2 target devices
(`iphone-15-pro`, `duo-folded`, `duo-unfolded`, `macbook-air`,
`desktop-1440p`), then checks horizontal overflow, touch-target size (44px
on mobile/tablet, 24px on desktop/xl), 8px gaps between targets on touch
tiers, text within 4px of a bordered/filled box edge, and the 1800px
centred `.app` cap on xl.

The text-to-edge check skips, whatever their `display`: chips whose tight
padding is the design (`.badge`, `code`, `kbd`, `samp`, `mark`, `.mention`,
`.tag`), anything inside `.visually-hidden`, `legend` (a caption that sits
on its fieldset's frame line by design), and anything with
`data-audit-edge="ignore"` on itself, an ancestor or the box it is measured
against. Use the attribute only for text that sits on a frame line by
design, and say why in a comment beside it.

```sh
node scripts/v5_audit.mjs                                  # everything (report mode, exit 0)
node scripts/v5_audit.mjs --theme blue-future --page dashboard --device iphone-15-pro
node scripts/v5_audit.mjs --theme lcars~voyager --strict   # exit 1 on any failure
```

`--theme`, `--page` and `--device` repeat. Palette variants run on the
dashboard only. A summary table goes to stdout; the full report (worst
offenders with selectors and sizes) goes to `test/v5-audit/report.json`
(gitignored). `--engine` repeats (see "Engines and known issues").

# Accessibility: `scripts/a11y_audit.mjs`

axe-core's WCAG 2.0/2.1/2.2 A and AA rules on every example page (each
root `*.html` that loads a theme, so new pages are picked up), per theme,
at Mobile (393x852, touch) and Desktop (1280x800). Palette variants run on
the dashboard only.

```sh
node scripts/a11y_audit.mjs --theme blue-future --theme windows95   # report mode
node scripts/a11y_audit.mjs --theme silo --page dashboard --tier mobile
node scripts/a11y_audit.mjs --strict                                # exit 1 on any serious/critical
node scripts/a11y_audit.mjs --theme silo --theme blue-future --blame silo   # exit 1 only on what silo causes
```

It prints rules and nodes by impact per theme, page and tier, then every
rule worst first, attributed to **core/page** (it fails the same way, same
node count, in every theme run on that page and tier) or to the **themes**
it fails only in, or fails worse in. Attribution needs two or more themes
in the run. Full report: `test/a11y/report.json` (gitignored).

# Performance budgets

`check.py --budgets` reports when a theme's bundle is over its gzipped budget,
its own CSS exceeds the theme threshold, or vendored fonts exceed the
per-file/total thresholds. This diagnostic is intentionally outside the
default lint and theme-ready gates while optimization is deferred.
`python3 scripts/check.py --budgets` prints the table; `--theme <slug>`
(repeatable) limits the lint to those themes, and failures outside them
(core, stale dist, other themes) become notes that don't affect the exit
status.

`scripts/render_cost.mjs` scrolls `dashboard.html` at 393x852 with the CPU
throttled 4x (CDP `Emulation.setCPUThrottlingRate`, Chromium only) and
reports frame times per theme, flagging an average over 20ms (flat themes
measure 16.7ms, one 60Hz frame):

```sh
node scripts/render_cost.mjs                        # every theme, about 4 minutes
node scripts/render_cost.mjs --theme liquid-glass --frames 480 --strict
```
