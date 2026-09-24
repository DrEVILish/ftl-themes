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
