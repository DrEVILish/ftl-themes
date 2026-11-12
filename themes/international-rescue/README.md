# International Rescue

> Gerry Anderson's Thunderbirds (1965): a cream 1960s atomic-age control console, navy IR bands, gold trim, flat Technicolor craft-colour lamps.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

The Tracy Island **control room** as a light, mid-century instrument panel:
cream and putty housings, stout navy outlines, chunky rounded-rectangle keys,
big round bezelled lamps, and a wide diagonal gold sash, with the five
Thunderbird craft colours doing the work of status semantics. It is the
opposite of this catalogue's dark neon themes: a **light** theme
(`color-scheme: light`) whose colour comes from flat blocks, never glow.

Sources and what could not be verified are in
`references/international-rescue/RESEARCH.md`. Palette, shape and type
guidance only: no logo, insignia artwork, likeness or screenshot is used.

## Core values

1. **Cream console, navy outline.** Surfaces are cream (`#f6f1e3`) on a putty
   backdrop (`#d9d3bf`); every raised object wears a 3px IR-navy (`#0a2f6e`)
   outline; that includes the instrument family (gauges, compass, compass
   strip, map, calendar) and the FAB, which also take the hard navy drop.
   Idle keys are cream (`#fbf6e8`), never optical white. Dark panels are the exception (bar, status strip, panel headers,
   readouts), not the base. The painted bands (bar, status strip, caption
   bars, table head) are uniform royal blue `#123f8f`; navy `#0a2f6e` stays
   the ink of outlines, drops and readouts.
2. **Flat colour blocks, hard shadows.** No gradients for depth, no blur, no
   glow. Depth is a hard navy offset (`0 4px 0`), like a keycap.
3. **Craft colours are the status language.** Blue = TB1 = accent/info,
   green = TB2 = success/lamp-on, orange-red = TB3 = danger, yellow = TB4 =
   warning. Gold is IR trim and the GO key. Don't add other hues.
4. **GO is the hero.** `.btn-go` is the biggest, gold, navy-outlined key,
   captioned upright in the wide display face, with a deeper drop; it
   depresses 5px on `:active`.
5. **Big round lamps with a bezel.** `.lamp` is a 1.3rem circle inside a navy
   ring; the rail carries five bezelled craft lamps.
6. **The sash is the only ornament.** One wide (3.6rem) gold diagonal
   crosses the bar's left end over a solid gold rule (the uniform sash; on
   phones a shortened diagonal clipped to the brand row); the rule's right
   end carries a 16rem five-segment craft-colour strip (TB1-TB5); every
   panel, modal and window caption bar repeats a short (1.4rem box) gold
   diagonal at its start; under `h1` a single wide gold sash with a diagonal end. Built
   from CSS only. Solid gold fills are kept for GO, the sash, rules and the
   fader knob; selection (rows, options, the current folder) is a 30% gold
   wash with a TB1 tab.
7. **Rounded-rectangle, never pill, never sharp.** Radius 0.5-1.1rem.
8. **Headlines are wide squared capitals.** Microgramma/Eurostile Extended
   when installed, else the vendored Michroma; the bar brand and GO key use
   the same face, upright and widely tracked (Michroma has no bold, so the
   brand and captions carry a thin text stroke).

## Signature details

- **App shell = control room**: navy bar with the gold sash and rule (its right
  end a TB1-TB5 craft-colour strip); a 4.5rem putty
  instrument rail with five bezelled lamps (blue, green, orange-red, yellow,
  silver-gold) drawn as five small inline-SVG lamp images (cheaper to repaint
  than gradients); a cream console panel with
  a hard navy drop; navy status strip with a gold rule; a map-room graticule
  (one inline-SVG tile) shows through the backdrop. On desktop each rail lamp carries its craft
  number (1-5) in the display face, large enough to read across the room. On phones the rail becomes a horizontal
  lamp row.
- **Segmented LED meters** (green to yellow to orange-red bands under a white
  slit mask), and a navy readout window with gold digits.
- **Rocker switch**: square-shouldered thumb in a stout slot; gold slot when on.
- Panel, modal and desktop-window headers: uniform-blue caption bar with a
  short gold sash at its start and a gold underline band, captioned
  uppercase in the display face with a 0.35px stroke (a thinner band when
  nested), the same voice as h1-h3.
  Inactive desktop windows keep the navy bar (no fading filter, which turned
  it slate); only the caption dims to #c7d3ee.
- Keys share one keycap and one voice (bold uppercase): `.btn`,
  `.toggle-btn`, `.segmented-item` and filter chips
  (`.badge-button`, same size and 2px navy outline as `.badge`; idle chips are
  cream with navy ink, the active one TB1 blue). Toggle keys carry the 4px
  navy drop and press flat.
- Tabs sit on a 3px navy rail; the active tab is a TB1-blue key outlined on
  three sides. Inside windows and modals tabs track tighter and run smaller,
  so a four-tab dialog keeps one row.
- Rail lamps have a TB1/TB5 silver ring inside the navy bezel.
- Tables: navy head, gold rule, italic uppercase captions, cream zebra.
- Alerts carry a 1rem tab in the craft status colour (TB1 blue info, TB2
  green success, TB4 yellow warning, TB3 orange-red danger; gold when plain).
- Sliders are faders: a navy groove with a chunky gold knob in a navy bezel
  (the thumb border is navy, so no cream ring). The groove keeps square ends:
  core paints it on the content box with `background-clip`, which a radius
  does not reach. The vertical fader uses physical-axis padding
  (`padding-block` under `vertical-lr`) so its groove stays 0.5rem wide inside
  the --tap-min hit box (core centres it on the wrong axis).
- `.connection` is a mini craft lamp: flat TB2 (live), TB4 (delayed,
  reconnecting), TB3 (offline) or TB1 (recovering) in a 2px navy bezel, with
  no halo or pulse.
- Selected rows and active list items take a gold wash
  (`--ir-gold` 30% into cream) with the 4px TB1 tab; hover is the paler
  #fff3c4.
- The bulk-action strip is the gold selection wash in the 3px navy bezel
  with the 4px drop; own chat bubbles are an 18% gold wash on cream.
- A table followed by `.table-blank-rows` squares its lower corners and the
  ruled tray carries the frame's sides and foot.
- Lists and chat bubbles keep the navy outline (3px, 2px inside a console);
  ghost and tertiary keys have no keycap drop until hovered.
- Navy surfaces re-point `--text/--muted/--link` and state-text tokens locally
  so nested muted text, ghost buttons and state text remain legible.

## Icons

`icons.svg` redraws the full core set (178/178) as bold 1960s pictograms:
- 24 grid, stroke only at 2.8 (`--icon-stroke-width`), round caps/joins from
  core; nothing is filled, solid shapes (play, bookmark, caret) are outlines.
- True circles and curves; boxes always rounded, rx about 30% of the short
  side (max 3, min 0.8). Circle enclosures for state marks (close, check,
  plus, minus, info).
- Dots are `r=".6"` circles that the heavy stroke turns into round blobs.
- The stroke closes up fine detail, so dense glyphs are simplified: bars are
  single fat strokes, at most 3 keys/lines inside a frame, wide tubes.
- `currentColor` only, no hard-coded colours.
- Dense generic glyphs the set does not redraw (file-type lettering,
  currency marks, QR) are copied at `stroke-width="2"` so their letters stay
  readable.

## Typography (honest)

`--font`: Univers, Helvetica Neue, Helvetica, Arial, Liberation Sans: the
1960s signage grotesque (renders as metric-compatible Liberation Sans here).
Headings and panel headers (`--ir-display`): Eurostile Extended, Microgramma
D Extended, Microgramma, then **Michroma** (SIL OFL, already vendored in
`assets/fonts/`, see `assets/fonts/NOTICE.md`), uppercase, upright, weight
400 with a 0.6px `-webkit-text-stroke` on h1/h2 and the bar brand and 0.35px
on panel/modal/window captions, so the single-weight face holds its own
beside 3px outlines (phones drop it on headings and captions to save paint);
h3 is unstroked (the stroke blurred it) and tracked wider instead. h2/h3 get 0.4em below.
Microgramma is the reported credits/title-card face; Michroma is an
open Microgramma-alike, not the original. The bar brand, window titles and
the GO key use the same face, upright (the earlier heavy italic was an
invention and is gone). Univers 59 (craft lettering) is not matched; bar nav
(`--app-bar-font: var(--font)`) and key labels use the bold uppercase body
stack. Readouts (`--font-mono`): Lucida Console, then DejaVu Sans Mono and
Liberation Mono, so the instrument digits stay sturdy where Lucida is absent.

## Contrast honesty

All computed with WCAG 2.x relative luminance.

| Pair | Ratio |
|---|---|
| `--text` #12203c on `--surface` #f6f1e3 / `--surface-2` #e8e2cf / `--bg` #d9d3bf | 14.3 / 12.5 / 10.8 |
| `--muted` #4a5570 on surface / surface-2 / bg | 6.6 / 5.7 / 5.0 |
| `--on-accent` #fff on `--accent` #0a4fb4 | 7.5 |
| `--on-danger` #fff on `--danger` #b32d07 | 6.4 |
| `--on-success` #fff on `--success` #17693a | 6.7 |
| danger / success text on surface-2 | 4.9 / 5.2 |
| `--warning-text` #7a5300 on surface / surface-2 | 6.1 / 5.3 |
| navy `#0a2f6e` vs cream text / gold #f5b800 / #c7d3ee | 11.3 / 7.1 / 8.5 |
| uniform blue `#123f8f` vs cream / #ffd23d / #c7d3ee / #ffab8f | 8.7 / 6.8 / 6.6 / 5.4 |
| GO: `--text` on gold `#f5b800` | 9.1 |

**Deviations:** `--danger` is darkened from a true TB3 orange-red so white
text passes; lamps use brighter craft colours (`--ir-tb1..5`) that never carry
text. `--warning` #f5b800 is a fill only (dark text on it, 9.1:1); its text
variant is amber-brown. The yellow-on-cream contrast of lamps/borders is not
relied on for information: state is also carried by position and labels.
Focus ring blue `#0a4fb4` on cream 6.7:1; on navy surfaces it becomes gold.

## Tell-tales of an inauthentic result

- Dark background, neon glow, or gradients for depth: it's a cyberpunk theme.
- Bevels or grey `#c0c0c0`: that is windows95. Primary-colour toy studs: lego.
- Sharp corners or pill-shaped buttons.
- Thin outlines (under 2px) or missing hard navy offset shadow.
- Lamps without bezels, or traffic-light colours other than the craft ones.
- Gold used for body text or as a text-on-cream colour.

## Don'ts

- Don't paint the IR emblem, sash artwork, craft silhouettes or faces.
- Don't set `background`/`color` on base component selectors.
- Don't use red for GO; danger is orange-red, GO is gold.
- Don't drop `--density` below 1.1: keys are chunky.

## Reference status

Research is search-summary based (direct fetches were blocked); craft colours
(TB1 blue/silver, TB2 green, TB3 orange-red, TB4 yellow, TB5 gold/silver) and
"dark blue" uniform with coloured sash are consistently reported; all hexes,
the cream console finish and the switch styling are period-plausible design
choices, not sampled. See RESEARCH.md.

## v5 layout

- **Tiers.** Phones (up to 480px): the lamp rail becomes a horizontal strip of the five craft lamps under the bar. Tablets (481–900px, often a short landscape screen): the rail is hidden so the console keeps its full width and height. Both tighten the shell gap and padding, and the 44px nav keys centre their labels. On phones the bar brand takes its own line (it never truncates) and the nav keys tighten; the theme picker, search key (without its Ctrl K hint) and icon keys share one row, and the lamp row is 2.1rem; the segmented keys, the status strip and its tray lamp tighten so labels stay inside their boxes, and one-line code blocks wrap instead of scrolling.
- **Nesting.** Panel headers read core's `--surface-pad`, so the navy caption bar sits flush in its panel at every tier. A panel or card inside another surface drops its hard drop shadow, takes a 2px outline and a thinner hazard band. Tables round their corner cells instead of clipping (`overflow: hidden` cut off row-action menus), readouts never wrap, and stacked-table labels use `--muted`.
- **XL gutter art (1801px+).** Tracy Island's long-range radar: faint navy range rings spread in from both screen edges over the map-room graticule.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware: true`). At
**L0** it renders correctly recolored but not in its control-room layout.
Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell (CONTRACT.md "The app
shell" / "Adoption levels") to get the real layout at **L1**.
