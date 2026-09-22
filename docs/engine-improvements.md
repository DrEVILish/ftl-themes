# Engine improvement notes

Recommendations from a fidelity/documentation review pass (v3.5.1), split
into what was implemented immediately versus what's deferred and why.
Written so a future contributor doesn't have to re-derive the reasoning.

## Implemented this pass

1. **`example.html` compare mode.** Two themes rendered full-width side by
   side (each an embedded copy of the page itself, `?embed=1` stripping
   its own chrome), with both themes' "Signature details" pulled from
   their READMEs into the sidebar. This is now the fastest way to catch
   the class of bug it already found twice in one session: a
   theme-specific token override that reads fine in isolation but is
   objectively wrong next to a sibling theme (see #2, #3).
2. **`scripts/check.py` now requires "Signature details."** 11 of 26
   themes had no such section — not broken, just invisible to the compare
   tool that now exists specifically to surface it. The lint prevents a
   new theme from shipping the same gap silently.
3. **Source-accuracy pass on theme descriptions.** Every theme's one-line
   `Description:` header (which feeds `dist/themes.json` and pickers) now
   names a concrete signature detail instead of a generic palette summary.
   A handful of color claims were checked against external references
   (`trekcolors` for LCARS, the commonly-cited Matrix digital-rain hex);
   LCARS's `--ftl-lcars-sky` was corrected from an unsourced pastel to sit
   close to the documented Okuda blue family while staying inside the
   contrast floor. See `CONTRACT.md`'s theme index for the full account —
   deliberately not oversold as more "verified" than it is: most themes
   have no single canonical hex source to check against at all.

## Recommended, not yet implemented

Roughly in priority order.

### 1. A `verify` field per theme, not just per-review-pass prose

Right now "this color was checked against a source" lives in a comment
and a CONTRACT.md footnote. A structured alternative: a small
`sources.json` per theme (or a block in the header comment) naming which
tokens were checked, against what, and when — machine-readable enough
that `scripts/check.py` could eventually warn when a theme's last
verification predates a token's last edit (i.e., the color changed after
someone checked it against a reference, so the citation may be stale).
Low urgency: the catalog is mostly original/genre work, not license-plate
color-matching, so this matters for maybe six themes total (the licensed
or real-product ones: LCARS, Matrix, Windows 95/XP/7, WMP11, iMac G3).

### 2. Automated visual regression, not just lint

`scripts/check.py` catches cascade bugs, missing tokens, and contrast
failures — everything expressible as a rule over the CSS text. It cannot
catch "this renders wrong" the way the compare tool's screenshots did
twice in one session (Material/Vaporwave's invisible nav-bar text; a
JS bug in the compare tool's own README parser). A headless-browser
screenshot diff per theme per commit (Playwright is already used ad hoc
for this in review passes) would catch visual regressions lint cannot
express — e.g. a future core.css change that silently breaks one theme's
`clip-path` corner cut. Cost: needs a CI runner with a browser, and a
"golden image" review workflow (someone has to approve diffs). Worth
scoping once the catalog is large enough that manual spot-checks (the
current practice) start missing things — not yet, but soon.

### 3. A "theme diff" tool, not just compare

Compare mode shows two themes' *renders* side by side. A complementary
"token diff" view — a table of every `--ftl-*` value each theme sets,
aligned by row, with a `unique to A` / `unique to B` / `identical` marker
— would answer a different question the render alone can't: "what would
I actually change to make theme B look like theme A." Useful for
authoring a palette-only variant of an existing theme (the way
`winxp-luna`'s Royale/Olive/Silver follow-ons are scoped in
`docs/theme-backlog.md`) without re-deriving every token by eye.

### 4. `--ftl-*` token usage report

No tool currently answers "which tokens does theme X actually read" or
"which core components does theme X never touch" except the coverage
lint (informational, not itemized). A per-theme report — generated from
the same regex `scripts/check.py` already uses — listing every
`.ftl-*` class the theme's selectors touch and every token it overrides,
would make the "how thorough is this theme" question answerable at a
glance instead of by reading the whole file. Natural next step after #3;
low cost since the parsing already exists in `check.py`, just needs a
report mode instead of pass/fail.

### 5. Documented source citations belong in the theme file, not just the README

Right now contrast-driven color deviations are commented inline in
`theme.css` (e.g. `winxp-luna`'s green, `barbie`'s pink) but *reference*
citations (which official/community source a color is checked against)
live in prose scattered across READMEs and, now, CONTRACT.md's table
footnote. Consolidating to one place — a `Sources:` line in the theme's
own header comment, next to `Theme-Name:`/`Description:` — would make it
greppable (`grep -l "^ \* Sources:" themes/*/theme.css`) instead of
requiring a human read of each README. Deferred because it's a mechanical
follow-up to #1 above, not urgent on its own.

## Why these and not others

Things considered and explicitly not recommended:

- **A theme "authenticity score."** Turning the compare-tool checklist
  into a numeric score invites optimizing the number instead of the
  render — the checklist's value is a human reading it against the
  screenshot, not a computed pass rate.
- **Auto-generating READMEs from theme.css.** The README is the design
  *intent*; the CSS is the implementation. Generating one from the other
  collapses that distinction — exactly the gap this pass's fixes (Windows
  XP Luna's primary button contradicting its own README) came from
  needing to catch by inspection, not something a generator would have
  caught either.
