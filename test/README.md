# Visual regression testing

`scripts/screenshot_themes.py` replaces the ad-hoc, throwaway Playwright
screenshot scripts this project used to spin up by hand for every "did I
break something" check. It screenshots every theme in `dist/themes.json`
against every `example*.html` QA page at a fixed 1280x900 viewport, and
either accepts those screenshots as the new baseline or diffs them
against the committed one.

## Usage

```sh
python3 scripts/screenshot_themes.py              # diff mode: compare against test/visual-baseline/
python3 scripts/screenshot_themes.py --baseline    # (re)write the committed baseline
python3 scripts/screenshot_themes.py --threshold 0.5   # tune diff sensitivity
```

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
- `test/visual-diffs/` — gitignored. Scratch output from a failing diff
  run, for local review only.

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

```sh
node scripts/v5_audit.mjs                                  # everything (report mode, exit 0)
node scripts/v5_audit.mjs --theme blue-future --page dashboard --device iphone-15-pro
node scripts/v5_audit.mjs --theme lcars~voyager --strict   # exit 1 on any failure
```

`--theme`, `--page` and `--device` repeat. Palette variants run on the
dashboard only. A summary table goes to stdout; the full report (worst
offenders with selectors and sizes) goes to `test/v5-audit/report.json`
(gitignored). Set `CHROMIUM_PATH` if Playwright's bundled browser is missing.
