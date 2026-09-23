# Style & branding guide

Scores and design rationale for every theme that ships (has both a
`themes/<slug>/theme.css` and captured reference images in
`references/<slug>/`). Reviewed by comparing a fresh `example.html`
render against the images in `references/<slug>/`, and by exercising the
rendered controls (contrast, focus states, hit targets).

## Method

Each theme is scored 1–10 across four factors, then combined into one
**likeness** score (how close the render reads to the real thing) and one
**ease-of-use** score (can someone actually use this UI):

| Factor | What it checks |
|---|---|
| Color | Hue, saturation and value match the reference's actual palette, not just "in the spirit of" |
| Structure | Shapes, radii, borders, layout rhythm match the reference's real construction |
| Signature | The one tell-tale detail (see CONTRACT.md's Theme index) is present and reads clearly |
| Type | Font stack, weight and casing match the reference's typographic voice |

Ease-of-use leans on what `scripts/check.py` already enforces mechanically
(4.5:1 text contrast, visible focus rings, motion gated behind
`prefers-reduced-motion`) plus a manual pass on hit-target size and
whether the theme's decoration ever competes with legibility.

**Any theme scoring below 8/10 gets fixed and re-rendered before this
document ships** — see "Revision log" at the bottom for what that caught
this pass.

## Icon pack

`assets/icons/icons.svg` — one 24×24 outline SVG sprite (26 icons: nav,
state, transport and CRUD glyphs), used everywhere as:

```html
<svg class="ftl-icon"><use href="assets/icons/icons.svg#icon-name"/></svg>
```

`.ftl-icon` in `core/ftl-core.css` sets `stroke: currentColor`, so every
icon inherits whatever text/foreground color surrounds it — no per-theme
icon variants to maintain. A theme only overrides two tokens when its
signature style calls for it:

- `--ftl-icon-stroke-width` — bolder for chunky/physical themes
  (`windows95`: 2.6, `lego-classic`: 3), thinner for dense/technical ones
  (`bloomberg`: 1.4, `matrix`/`winamp-classic`: 1.5). Everything else uses
  the 2.0 default.
- `--ftl-icon-fill` — solid-fill glyphs instead of outline, for themes
  whose reference icon packs (e.g. Alienware Invader, `references/alienware/`)
  are filled rather than outlined. Unset by default.

See `example.html`'s "Icon pack" and "Icon buttons" sections for the full
set rendered live in whichever theme is selected.

## Shipping themes — scores

| Theme | Accent | Likeness | Ease of use | Overall |
|---|---|:-:|:-:|:-:|
| `alienware` | `#00d4ff` | 8.5 | 9.0 | **8.8** |
| `aqua` | `#2a74d0` | 9.0 | 9.0 | **9.0** |
| `barbie` | `#c81b7a` | 8.5 | 9.0 | **8.8** |
| `bloomberg` | `#ffcc00` | 9.0 | 8.5 | **8.8** |
| `cyber-goth` | `#b6ff1a` | 8.5 | 8.5 | **8.5** |
| `death-star` | `#2f6fff` | 8.5 | 9.0 | **8.8** |
| `hot-wheels` | `#ff5f00` | 8.5 | 8.5 | **8.5** |
| `imac-g3` | `#00b0d4` | 9.0 | 8.5 | **8.8** |
| `lcars` | `#ff9900` | 8.5 | 8.5 | **8.5** |
| `lego-classic` | `#d0111b` | 9.0 | 9.0 | **9.0** |
| `matrix` | `#00ff41` | 9.5 | 8.5 | **9.0** |
| `msdos` | `#00aaaa` | 9.0 | 8.5 | **8.8** |
| `vaporwave` | `#ff71ce` | 8.5 | 8.5 | **8.5** |
| `win7-aero` | `#1265c7` | 9.0 | 9.0 | **9.0** |
| `winamp-classic` | `#00ff00` | 8.5 | 8.5 | **8.5** |
| `windows95` | `#000080` | 9.5 | 9.5 | **9.5** |
| `winxp-luna` | `#0054e3` | 9.0 | 9.0 | **9.0** |
| `wmp11` | `#3fa9f5` | 8.5 | 8.5 | **8.5** |

All 18 clear the 8.0 floor. Notes on the closest calls and what keeps
each one honest, below.

### `alienware` — 8.8
Reference: `references/alienware/` (Alienware Invader icon pack, AlienFX
Eclipse Rainmeter skin). Color and the angular `clip-path`-cut corners
match the reference chrome closely; the real thing wraps a light strip
around all four corners where this theme runs one down the rail — a
deliberate simplification for a reusable app-bar, not a miss.

### `aqua` — 9.0
Reference: `references/aqua/` (Mac OS X 10.6 UI kit, Leopard icon pack).
The 3px pinstripe-over-gloss texture and candy-pill buttons match the kit
almost exactly, including the blue accent on the scrollbar-thumb
equivalent (`.ftl-btn-primary`).

### `barbie` — 8.8
Reference: `references/barbie/` (brand logo, packaging pink). Hot-pink/
mint palette and 999px pill radius match; the logo's specific magenta is
slightly warmer than `--ftl-accent`, kept as-is because it's still inside
the "Barbie pink" family and holds AA contrast where the exact logo hex
does not.

### `bloomberg` — 8.8
Reference: `references/bloomberg/` (terminal photos, function-key row).
Amber-on-black monospace density matches; ease-of-use is capped by the
theme's own intentional `--ftl-density: 0.7` extreme-density design,
which trades comfort for the authentic "wall of data" read.

### `cyber-goth` — 8.5
No single photographic reference (a genre, not a product) — scored
against the described convention (toxic green + hot purple on black
vinyl gloss) rather than one image.

### `death-star` — 8.5
Reference: `references/death-star/`. True `#000000` background and
hard-edged blue readouts match the Imperial-terminal aesthetic; no
gradients or soft shadows anywhere, which is the point.

### `hot-wheels` — 8.5
Reference: `references/hot-wheels/` (box art, game screenshots). Orange
flame-gradient band and black chrome match; box art's flame is more
red-hot at the core than the CSS gradient's midpoint, a minor departure.

### `imac-g3` — 8.8
Reference: `references/imac-g3/` (Bondi Blue hardware photos, Mac OS 9
screenshots). Translucent ribbed-plastic gloss and the verified Bondi
Blue-family accent (`#00b0d4`, see `themes/imac-g3/theme.css` header for
the contrast-floor tradeoff) match well.

### `lcars` — 8.5
Reference: `references/lcars/` (LCARS console art). The elbow curve
(horizontal bar into vertical rail) is present and correct; real LCARS
leans on a wider palette (tan, lilac, salmon blocks) than this theme's
orange/black/blue, which stays deliberately narrower for legibility as a
general-purpose UI kit rather than a screen-accurate recreation.

### `lego-classic` — 9.0
Reference: `references/lego-classic/`. Primary-color blocking, thick
black borders and corner studs read as a physical brick immediately.

### `matrix` — 9.0
Reference: `references/matrix/` (film stills, code-rain shots). `#00FF41`
is the actual on-screen hex; the staggered digital-rain background
(5 layered `radial-gradient`s at prime-ish periods) avoids the grid
artifact a single repeating gradient produces. Ease-of-use docked slightly
for the deliberately low-contrast monospace body text against black,
which is the reference's own convention.

### `msdos` — 8.8
Reference: `references/msdos/` (Norton Commander screenshots). Blue
background, cyan/yellow "bright" palette and double-line box borders all
present.

### `vaporwave` — 8.5
Reference: `references/vaporwave/` (aesthetic mood images). Magenta-to-
cyan gradient clipped to heading glyphs is the strongest tell; genre-based
so no single photographic ground truth.

### `win7-aero` — 9.0
Reference: `references/win7-aero/` (Aero screenshots, Segoe UI specimen).
Real `backdrop-filter` blur on the app-bar/status strip is the
distinguishing detail versus Luna's opaque gloss, and it's present and
correct.

### `winamp-classic` — 8.5
Reference: `references/winamp-classic/`. LCARS-green LCD-style readouts,
tiny uppercase labels and the grip-texture drag handle all match; the
UI's small type sizes throughout are period-accurate but the reason
ease-of-use sits below likeness.

### `windows95` — 9.5
Reference: `references/windows95/` (desktop, IE, Freecell screenshots).
The strongest match in the catalog: the bevel-inverts-on-press language,
zero border-radius, and the exact 16-color VGA palette (`#c0c0c0` /
`#000080` / `#008080`) all check out directly against the screenshots.

### `winxp-luna` — 9.0
Reference: `references/winxp-luna/` (Luna theme screenshots). Glossy
round-cornered blue chrome, the tan/beige content well, and green
reserved for the primary "go" action all match the reference dialogs
directly.

### `wmp11` — 8.5
Reference: `references/wmp11/` (WMP11 screenshots, mini-mode). Black
glass with a cool blue glow on the primary transport control matches; the
theme keeps the rest of the chrome flatter than WMP11's own more elaborate
visualizer chrome, a legibility tradeoff for a general-purpose kit.

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

## Revision log

- **`pipboy`** (now parked, was shipping): a muted/surface-2 contrast gap
  (4.2:1 vs the 4.5:1 AA floor) was caught while rebuilding after the
  reference-image merge and fixed (`--ftl-muted: #1f9c3f` → `#1fa43f`)
  before this pass; kept for whenever it re-ships.
- No shipping theme in the table above required a second pass to clear
  8.0 — the color-research work from the prior grounding pass (documented
  in each theme's own header comment) already covered every hard case.
