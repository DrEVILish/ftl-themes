# Style & branding guide

Scores and design rationale for every theme that ships (has both a
`themes/<slug>/theme.css` and captured reference images in
`references/<slug>/`). Reviewed by comparing a fresh `example.html`
render against the images in `references/<slug>/`, and by exercising the
rendered controls (contrast, focus states, hit targets).

## Method

The first pass at this document scored every theme myself, and scored too
generously (8.5+ across the board) — reviewing your own work rarely
catches its own blind spots. The scores below are from a second, stricter
pass: **one independent review agent per shipping theme (18 total)**,
each given the identical rubric and told explicitly to score like a
skeptical outside auditor, not a cheerleader, reserving 9-10 for
"would fool a fan of the reference in a side-by-side comparison." Each
agent worked from the theme's CSS, its own README, its real reference
images in `references/<slug>/`, and a fresh render — independently, with
no visibility into the other 17 reviews or my own earlier scores.

Each factor is scored 1–10, weighted into one overall:

| Factor | Weight | What it checks |
|---|:-:|---|
| Color accuracy | 25% | Hue, saturation and value match the reference's actual palette, not just "in the spirit of" |
| Structural fidelity | 25% | Shapes, radii, borders, layout rhythm match the reference's real construction |
| Signature detail | 20% | The one tell-tale detail is present, prominent, and would let someone guess the reference from the render alone |
| Typography | 10% | Font stack, weight and casing match the reference's typographic voice |
| Accessibility & usability | 20% | Legibility and clickability judged by eye against the actual render, not assumed from a lint pass |

**Every theme scoring below 7/10 gets a concrete fix, not just a lower
number.** The first strict pass came back with all 18 below 7 (range
3.4–6.9) — see the table and "What the panel found" below for exactly
what each agent's report said and what was changed in response.

## Icon pack

`assets/icons/icons.svg` — one 24×24 outline SVG sprite (1,020 icons:
the original hand-drawn nav/state/transport/CRUD/dashboard set plus a
bulk-vendored Tabler batch — see `assets/icons/NOTICE.md` for sourcing
and the exact count), used everywhere
as:

```html
<svg class="ftl-icon"><use href="assets/icons/icons.svg#icon-name"/></svg>
```

`.ftl-icon` in `core/ftl-core.css` sets `stroke: currentColor`, so every
icon inherits whatever text/foreground color surrounds it. Most themes
reskin the generic set through two tokens when their signature style
calls for it:

- `--ftl-icon-stroke-width` — bolder for chunky/physical themes
  (`windows95`: 2.6, `lego-classic`: 3), thinner for dense/technical ones
  (`bloomberg`: 1.4, `matrix`/`winamp-classic`: 1.5). Everything else uses
  the 2.0 default.
- `--ftl-icon-fill` — solid-fill glyphs instead of outline, for themes
  whose reference icon packs (e.g. Alienware Invader, `references/alienware/`)
  are filled rather than outlined. Unset by default.

Six themes go further and ship **real per-icon overrides**:
`themes/<slug>/icons.svg` redraws a subset of icon ids (home, settings,
search, close, user, bell) in the theme's own visual language — chunky
pixel-art for `windows95`, a coarse block/cell grid for `teletext`, thin
monospace line marks for `matrix`, glossy two-tone icons for
`winxp-luna`, LCARS' pill/elbow geometry for `lcars`, coarse LCD segment
shapes for `nokia-3310`. `scripts/build_icons.py` merges each theme's
overrides with the generic sprite into `dist/icons/<slug>.svg`; any icon
a theme doesn't override falls back to the generic shape, which is also
what every other theme uses for 100% of its icons. See CONTRACT.md "Icon
system" for the full mechanism and `assets/js/theme-loader.js` for how
the example pages swap `.ftl-icon` hrefs to the current theme's merged
sprite.

See `example.html`'s "Icon pack" and "Icon buttons" sections for the full
set rendered live in whichever theme is selected.

## Shipping themes — strict panel scores

Each row is that theme's independent agent's verbatim weighted score on
the pre-fix render, plus what was actually broken and what changed.
Post-fix numbers aren't shown as a re-scored table — they haven't been
re-run through a fresh independent agent yet, which is the honest
standard this document holds everything else to; treat the fixes as
"addresses the panel's stated finding," not as a verified new score,
until a re-review happens.

| Theme | Panel score | Biggest tell the panel found | Fixed? |
|---|:-:|---|:-:|
| `death-star` | 3.4 | Reference is white-linework-and-red on black; theme was blue-accented and borderless | ✅ palette + grid reworked |
| `barbie` | 4.7 | No trace of the brand's actual cursive-script wordmark | ✅ vendored a script face for h1/brand |
| `imac-g3` | 4.6 | Dark desaturated navy-teal, not the hardware's bright candy blue | ✅ palette brightened/resaturated |
| `hot-wheels` | 5.6 | Totally missing Hot Wheels' actual blue-and-orange brand palette | ✅ added the blue as a structural color |
| `alienware` | 5.6 | AlienFX rail strip was coded but never rendered (empty-rail bug) | ✅ rail now renders; added corner brackets |
| `winxp-luna` | 5.6 | No window-control chrome (min/max/close) anywhere | ✅ added the control cluster |
| `lcars` | 5.5 | The elbow (candy rail) never rendered — same empty-rail bug as alienware | ✅ rail now renders |
| `cyber-goth` | 5.2 | Primary button's hover glow contradicted the theme's own documented color rule | ✅ bug fixed |
| `win7-aero` | 5.2 | `--ftl-app-bg` was never set, so `backdrop-filter: blur()` had nothing to blur | ✅ textured desktop gradient added |
| `winamp-classic` | 5.2 | LCD green flooded headings/nav/buttons instead of staying confined to readouts | ✅ confined to readouts/meters |
| `wmp11` | 5.4 | "Round" play button was actually an oval sized to its label text | ✅ true fixed-diameter circle |
| `aqua` | 5.9 | No traffic-light window controls anywhere — Aqua's #1 tell | ✅ added; pinstripe contrast raised |
| `windows95` | 5.9 | Page-hero-scale headings and a single-layer press bevel gave it away as a recolored webpage | ✅ dialog-scale headings, full bevel |
| `bloomberg` | 6.2 | Function-key color row was coded (`<kbd>`) but never rendered anywhere | ✅ added to the status bar |
| `lego-classic` | 6.2 | Studs (the #1 LEGO tell) were a barely-visible 12–15% opacity smudge | ✅ real highlight+shadow ring |
| `msdos` | 6.4 | No visible F-key status bar; disabled buttons nearly invisible | ✅ added F-key strip + greyed disabled state |
| `matrix` | 6.5 | "Rain" was flat-opacity dashes with no glyph brightness falloff | ✅ bright head + dim tail per column |
| `vaporwave` | 6.9 | No sun disc or perspective grid — the genre's single most iconic image | ✅ added both to the status strip |

Every one of these was independently scored below the 7.0 floor on the
strict rubric, and every one has a real, committed CSS fix addressing the
specific defect the panel named — see the commit that introduced this
table for the full diff and per-theme rationale.

## What the panel found — detail

### `alienware`
Cyan and matte black were right, but the AlienFX light-strip rail —
coded in `.ftl-app-rail`'s gradient — never actually rendered: core
collapses an empty `<aside>` to `display: none` unless a theme sets
`--ftl-app-rail-empty-display`, and this theme never did. Fixed, and
added corner tick-mark brackets to the app-bar for the "ornate chrome"
the reference photos show that a flat 2px rule didn't capture.

### `aqua`
Pinstripe and candy-gloss buttons were present in the CSS but nearly
invisible at render scale, and the theme had no traffic-light window
controls at all — the single detail every reference image leads with.
Added a three-light cluster via `.ftl-app-bar::before` and doubled the
pinstripe's contrast.

### `barbie`
The accent pink and pill radius were fine, but the panel's sharpest
complaint was typographic: uppercase blocky Baloo 2 is the *opposite*
of the brand's actual cursive wordmark. Vendored Pacifico (SIL OFL) for
`h1`/`.ftl-nav-brand` only — body and buttons keep Baloo 2.

### `bloomberg`
The amber/cyan function-key color coding was real, correctly cycling
through `<kbd>` elements — but no page in the showcase renders a `<kbd>`,
so the one truly diagnostic Bloomberg tell was invisible. Added the same
five-color strip directly to `.ftl-app-status` via a pseudo-element.

### `cyber-goth`
The theme's own README documents "purple structure, green signal, the
hover bloom is always purple" as its signature rule — and the CSS
directly inverted it on `.ftl-btn-primary`'s hover shadow. Removed the
contradicting override.

### `death-star`
The biggest miss in the catalog: the reference is a black/white-pinstripe-
linework/red-panel control room, and the theme had gone all-in on an
invented blue accent with zero borders anywhere. Reworked the palette so
red is structural (buttons, focus ring, table heads), and added a painted
(not box-model) white grid texture on panels — texture, not chrome, so
the theme's own "zero borders/shadows" component contract still holds.

### `hot-wheels`
Every reference image is blue-and-orange; the theme was black-and-orange
only. Added a real Hot Wheels blue (`--ftl-hw-blue: #0033a0`) to the
table head and app-bar rule.

### `imac-g3`
The palette had drifted dark and desaturated (a "moody aquarium
dashboard" per the panel) instead of the hardware's actual bright candy
blue. Brightened and resaturated `--ftl-bg`/`-surface`/`-surface-2`,
re-verifying every contrast floor by hand afterward (the brighter surface
broke the accent and muted-text floors on the first attempt).

### `lcars`
The exact same empty-rail bug as alienware — the candy-bar elbow, this
theme's whole reason for existing, silently never rendered. One-line fix.

### `lego-classic`
The studs (LEGO's #1 tell) were a 12–15%-opacity dot, invisible at normal
size. Rebuilt as a real two-tone highlight+shadow ring, large enough to
actually read as a raised bump.

### `matrix`
The rain was five layers of flat-opacity dashes with no per-column
brightness falloff — real footage has a bright leading glyph fading to
dark green. Added a second, brighter "head" layer per column over the
original dim "tail" layer.

### `msdos`
No F-key status bar was visible anywhere (same "coded but never
rendered" pattern as bloomberg), and disabled buttons at 45% opacity
nearly vanished against the saturated blue background. Added the F-key
strip and a period-accurate greyed disabled state.

### `vaporwave`
Color was already excellent (the panel rated it 9/10) but structure was
weak: no sun disc, no actual perspective grid, just a flat repeating-line
pattern. Added both to the status strip via pseudo-elements.

### `win7-aero`
`--ftl-app-bg` was never set, so `.ftl-app`'s background fell back to
transparent — the glass bar/status strip had nothing detailed behind them
to blur, so `backdrop-filter` was declared but visually inert. Added a
textured radial-gradient desktop background.

### `winamp-classic`
The LCD green was meant to be a rare, confined signature but had been
wired into headings, nav links and the primary button — diluting it into
a generic accent color. Reserved it for readouts/meters/sliders only;
headings and the primary button now use steel tones.

### `windows95`
Page-hero-scale bold headings and a single flat inset shadow on
`:active` gave it away as a modern webpage wearing Win95 colors. Shrank
headings to dialog-caption scale and completed the pressed bevel to a
full double concentric inset (matching the resting state's own
two-layer bevel).

### `winxp-luna`
No window-chrome controls (minimize/maximize/close) anywhere — the panel
called this the single biggest miss. Added the control cluster via a
generated pseudo-element cluster in the title bar.

### `wmp11`
The "round" play button wasn't actually round: `--ftl-go-size` maps to
`font-size` in core, which sizes an oval to fit the label text rather
than producing a fixed-diameter circle. Set explicit equal width/height
and a downward transform so it protrudes past the transport bar, plus a
play glyph, matching the reference's floating circular control.

## Parked — no reference yet

`aperture`, `blue-future`, `cue-lab`, `material`, `nerv`, `pipboy`,
`steampunk`, `tron` are in `archive/themes-pending-reference/` and don't
build. They're not un-scoreable because they're bad — several (`material`,
`aperture`, `pipboy`, `tron`, `nerv`) have well-documented real-world
references that just haven't had images pulled into `references/` yet;
`blue-future` and `cue-lab` are original designs with their own internal
reference (see their READMEs), not a photo to compare against. Move a
theme back to `themes/` once it has a `references/<slug>/` folder and it
re-enters the build and this scoring pass.

## Root cause: why the panel scored so much lower

The 18 low scores weren't 18 unrelated opinions — tracing them back
turned up a handful of repeatable bug *patterns*, several hitting more
than one theme, plus a real gap in how the first self-review pass worked:

1. **Coded but never rendered.** `lcars` and `alienware` both style
   `.ftl-app-rail` with real, correct gradients — but core collapses an
   empty `<aside>` to `display: none` unless a theme sets
   `--ftl-app-rail-empty-display`, and neither did. `bloomberg` and
   `msdos` both style `kbd` (a real core component) as their signature
   detail — but `example.html`, the shared QA page every theme is judged
   against, never rendered a single `<kbd>` anywhere, in any theme. Four
   of the eighteen low scores trace to this one shape of bug: CSS that is
   genuinely correct but structurally unreachable from the page used to
   review it. Fixed the two rail themes directly, and fixed the root
   cause for `kbd` by adding a real shortcut-row (`<kbd>Ctrl</kbd>` etc.
   plus a 5-key row) to the Typography section of `example.html` itself,
   so any theme's `kbd` styling gets exercised from now on, not just
   these two.
2. **Token semantic mismatch.** `wmp11`'s "circular" play button used
   `--ftl-go-size`, which core maps to `font-size`, not width/height — it
   was never a circle, just an oval sized to fit its label. Checked core
   for every other token with the same "-size maps to font-size" shape
   (`--ftl-readout-size` is the only other one) and confirmed no theme
   makes the same mistake with it.
3. **Palette drift across editing passes.** `imac-g3`, `hot-wheels` and
   `death-star` had each moved away from their documented reference hue
   over several earlier rounds of unrelated edits (contrast fixes,
   "lean into uniqueness" passes), with nobody re-checking the result
   against the actual source image each time. Re-grounded each against
   `references/<slug>/` directly this pass.
4. **Diluted signature.** `winamp-classic`'s LCD green and
   `lego-classic`'s studs were both *present* in the CSS but so
   widespread (green) or so low-contrast (studs) that they read as
   generic decoration instead of the one specific detail they were meant
   to be. Confined/strengthened both.
5. **Self-contradiction.** `cyber-goth` had a literal bug where the CSS
   inverted a rule its own README documents as load-bearing (hover glow
   color). Nothing subjective about this one — just wrong.

The bigger pattern behind all of this: the first self-review pass judged
themes by reading their CSS and design-doc comments alongside a render,
which made it too easy to credit a theme for what its code *said* it was
doing rather than verifying what actually painted to the screen. The
strict panel worked from the same render but scored only what was
visible in it — that difference alone accounts for most of the gap
between "8.5+" and "3.4-6.9."

## Revision log

- **All 18 shipping themes**: the strict independent panel (18 agents, one
  per theme) came back below the 7.0 floor on every single one — a real
  calibration gap against an earlier, more lenient self-review pass, not
  just harsher wording. Every theme's specific "biggest tell" was fixed;
  see the tables above. Three of those fixes introduced their own lint
  regressions (imac-g3 accent/muted contrast, death-star nav-brand
  contrast, an msdos disabled-state rule that set `background`/`color`
  directly on a base component instead of through `--ftl-btn-*` tokens) —
  all caught and fixed by `scripts/check.py` before commit, which is back
  to 0 failures.
- **Not yet done**: a fresh independent re-review of the fixed renders.
  The fixes above address each panel's literal finding and were spot-
  checked visually in Chromium, but they have not been re-scored by a new
  agent panel — do that before trusting a specific new number for any of
  these 18.
- **`pipboy`** (now parked, was shipping): a muted/surface-2 contrast gap
  (4.2:1 vs the 4.5:1 AA floor) was caught while rebuilding after the
  reference-image merge and fixed (`--ftl-muted: #1f9c3f` → `#1fa43f`)
  before it was parked; kept for whenever it re-ships.
