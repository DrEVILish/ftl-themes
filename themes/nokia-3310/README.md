# Nokia 3310

> The reflective yellow-green monochrome LCD of the 3310/3210 era: no backlight colour, no anti-aliasing, and selection reads as a hard colour invert rather than a highlight.

**Requires: L1** — sets `--app-*` layout properties (the LCD top line, the centred "Menu" softkey line, the handset casing); recolours correctly at L0 but the phone-screen composition needs the app shell.

## What this theme is trying to achieve

The 3310's screen was genuinely one colour: a reflective, non-backlit
yellow-green LCD with dark olive pixels, the same in every lighting
condition a backlight would otherwise vary. There is no second hue on the
real device — every visual distinction (selected menu item, header bar)
comes from inverting which of the two tones is foreground and which is
background, never from introducing a new colour.

## Core values

1. **Selection is inversion, not colour.** `--row-selected-bg` /
   `--row-selected-fg` swap the two LCD tones outright — light-on-dark
   instead of dark-on-light — the only way this hardware could highlight
   anything. The same invert marks the active side-nav item
   (`--nav-item-bg-active`), a lit pad (`--pad-lit-alpha: 100%`) and the
   active filter chip; other badges are an ink outline, never a tint.
   Clear and icon buttons light up the same way on hover, focus and press
   (`--btn-clear-bg-hover` / `--btn-clear-bg-active` are the ink, the label
   flips to the LCD tone).
2. **Zero radius, zero gradient, zero shadow.** A reflective LCD segment
   display has none of these; every corner is square and every fill is
   flat. Every core round default is set to 0 (switch track and thumb,
   icon buttons, badges, avatars, status dots, lamps, presence, steps,
   calendar dates, swatches, scrollbars, the desktop monitor and more), and
   the two discs core hard-codes (the count badge on `.has-badge` and the
   presence dot) are squared by a rule, as are the loaders and dots core
   draws round: the htmx indicator and spinners (a square whose ink edge
   steps round in quarter turns), carousel markers and arrows, and the
   typing dots; the skeleton is a flat block with no shimmer. SVG chart
   points stay circles: core draws them as `<circle>` elements.
3. **danger/success/warning are a documented compromise.** True hardware
   has no second colour at all; those three tokens use barely-different
   dark tones within the same LCD family specifically so the theme stays
   usable as a real design system without pretending the phone had a
   colour screen — see the comment beside them in `theme.css`. Charts
   follow the same rule: the six series are ink-density steps of the one
   hue, and photos and placeholder art are filtered to LCD monochrome.

## Signature details

- Signal (left) and battery (right) as tall vertical ink stacks down the
  LCD's side edges, as on the 3310's idle screen (`nokia-3310-blue.png`):
  on desktop and XL they hang just below the top line as thin dashes,
  0.7rem wide and `clamp(7rem, 24vh, 18rem)` tall, in a gutter that the
  main area's inline padding (`--app-main-padding: 1rem 2.3rem`) keeps
  clear; on touch tiers they shrink into the bar's first-line corners.
  Stepped bars widest at the top, a Y antenna and a battery glyph at the
  base, drawn as pixel SVGs in the ink colour. On desktop only the bars
  stretch down the edge; the antenna and battery are a separate 7x8 layer
  that keeps its shape, about one bar tall.
- One LCD tone top to bottom, as in both lit captures: the top line is
  plain LCD with a 2px ink rule; the bottom line carries a single centred
  "Menu" (the Navi-key's one softkey label) on its own row, the heaviest
  line on the screen: 1.6rem bold pixel type (2rem on XL), clock-sized
  as in the photo. No
  inverted strips; inversion is kept for selection, so a free-standing
  `.nav` strip is the LCD with a 2px ink rule and only its current item
  inverts. On the desktop page
  only the front window's title is inverted; the others stay LCD tone
  above a 2px ink rule.
- The handset around the screen: navy casing (`#3c3e4e`, sampled), a 9px
  silver lens ring (`#b9bbb6`) and a darker navy bezel (`#343849`), 2rem
  deep above the LCD and 1.25rem at the sides and bottom. From 901px up,
  the top of the silver Navi-key with its cyan `#3aa0d8` line sits on the
  casing just below the screen. On XL
  each gutter carries one 3x4 number pad: silver oval keys with their
  numerals and letters, the outer columns tilted out and sitting higher
  than the centre one, on otherwise plain casing. A sidebar
  beside the shell (an `aside` sibling of `.app`) is its own LCD panel.
- The slider is an ink rail (`--slider-bg: var(--text)`) with a square
  ink thumb.
- Pixel type throughout, in Jersey 15, a squat bold pixel sans: headings,
  the bar brand, window titles, the "Menu" softkey, the short UI strings
  and body text alike. Numerals, ids, timestamps, log lines and file names
  (core's "mono" and readouts) are LCD readouts too: the same face with
  tabular digits. Only code, kbd, pre and samp keep a true monospace, the
  bitmap-cut Px437 IBM VGA 9x16, never a thin typewriter face. Its small
  x-height is lifted with `font-size-adjust: ex-height 0.5`; table heads,
  badges and small buttons never drop below 0.8rem, and the root steps up
  to 106.25% on XL, so the pixels stay whole on the LCD.
  `-webkit-font-smoothing: none` where honoured.
- Dialogs close with a "Back" softkey label; a window's title bar (a
  desktop window, or any header with min/max buttons) keeps the square ×
  beside its other window buttons.
- Alerts and toasts lead with an inverted pixel tag ("i" info, "OK"
  success, "!" warning, "!!" danger; hidden from the accessible name),
  and a danger alert or toast inverts as a whole, so severity reads by
  structure, not hue.
- A destructive button leads with a "!" pixel (hidden from the accessible
  name), so Delete differs from Confirm by structure, not hue.
- On a phone the bar links sit closer (0.3em inline padding, still
  `--tap-min` tall) so the menu takes one row.

## Icons

`themes/nokia-3310/icons.svg` redraws the full core icon set (178/178,
plus `sun-moon`) as coarse monochrome LCD glyphs. Style rules, taken from
the original hand-drawn subset and followed by every later addition:

- **Grid:** 24×24 viewBox, integer coordinates (half units only where a
  shape must centre); no fine detail below 2 units.
- **Fill vs line:** mostly flat `currentColor` rects and polygons. Frames
  (file, mail, clipboard, coin, screen) are outline rects or octagons,
  `fill="none" stroke="currentColor" stroke-width="3"`; open strokes
  (checks, slashes, axes, wheels) are 2.5–3 wide.
- **No curves:** circles become octagons (coin, album, disc, gps), arcs
  become stepped or angular runs (rainbow, storm, cloud).
- **Fallbacks:** icons outside the redrawn set (core's outline glyphs) get
  `shape-rendering: crispEdges` and mitred joins from the theme's `.icon`
  rule, so they at least render pixel-hard. They still contain core's
  circles and arcs.
- **Inherited outline:** the core `.icon` outline (2.5 units via `--icon-stroke-width`; the theme mitres the joins)
  also strokes every filled shape, so blocks look slightly soft and grow
  about 1.25 units per side. Gaps between filled parts are therefore at least 3
  units. The one exception is the pixel lettering on `file-type-pdf` and
  `file-type-png`, whose 2-unit blocks turn the stroke off so the letters
  stay legible.
- **Palette:** `currentColor` only, single tone.

## Tell-tales of an inauthentic result

- Any rounded corner or drop shadow.
- A saturated, clearly-differently-hued "accent" color — anything beyond
  the yellow-green/dark-olive family breaks the one-colour-screen premise.
- A soft/tinted selection highlight instead of a hard full invert.

## Don'ts

- **No second hue.** Everything is the yellow-green LCD tone or dark olive ink.
- **No radius, gloss, gradient or shadow.**
- **No soft or tinted selection**; selection is a hard two-tone invert.
- **No anti-aliased or thin type.** Bold, chunky.
- **No backlight glow.** The 3310's screen is reflective and unlit.
- **No colour-coded state beyond ink density**; danger/success/warning are barely different dark olives on purpose.

## Typography

`--font` and `--font-pixel` are `"Jersey 15", "Consolas", "Courier New", monospace`; `--font-mono` is the same pixel stack (with `tabular-nums`) for numerals and readouts; inside `code`, `kbd`, `pre` and `samp` it becomes `"Px437 IBM VGA 9x16", "Consolas", "Courier New", monospace` (CC BY-SA 4.0, already vendored as `assets/fonts/Web437_IBM_VGA_9x16.woff2`; see `assets/fonts/NOTICE.md`). **Jersey 15** (SIL OFL 1.1, vendored as a Latin subset in `assets/fonts/Jersey15-Regular.woff2`; see `assets/fonts/NOTICE.md`) is a bold, squat, proportional pixel sans with open counters (C, 2 and 8 stay distinct at UI sizes), the nearest open relative of the 3310's Series-20 screen font (`nokia-3310-blue.png` shows that font in "Menü" and the clock). It has one weight, already heavy; the `@font-face` claims weights 100–900 so the browser never adds synthetic bold, and no text stroke is used. `font-size-adjust: ex-height 0.5` lifts its 0.41em x-height to body size. It is not the Series-20 face itself: Nokia's font was never released. Pixelify Sans was tried first and dropped: its C and 2 close up into O and 8 at body sizes. `RESEARCH.md` also records that a native screen capture is still missing, so the face is judged only from that one photo.

## Contrast honesty

- **Reference hue reconciled.** `RESEARCH.md`'s outsider read says "blue-green" LCD; the README and `theme.css` say yellow-green. The one capture that shows a lit screen (`nokia-3310-blue.png`) reads as a pale yellow-green with dark olive ink, and the casing is dark blue, which is probably the source of "blue". The lit screen samples at `#749468`, `#789a68` and `#759b61`, a greyish, slightly bluish green. The shipped tones keep that hue (blue added rather than lightness) and sit as close to the sample as a near-black ink allows at 7:1: `--bg` `#80a56d`, `--surface` `#87ab73`, `--surface-2` `#789b64`, ink `#060b03` (7.1:1 on `--bg`, 7.7:1 on `--surface`, 6.3:1 on `--surface-2`). The true sampled tone would give even this ink only about 6:1, so the last few points of lightness give way to the AAA floor.
- **AAA:** `--text` clears 7:1 on `--bg` and `--surface` but is 6.3:1 on `--surface-2`; that is the real LCD's low contrast.
- **`--muted`** `#0b1007` (6.1:1 on `--surface-2`) is not really a second shade.
- **State inks are a departure.** `--danger` `#101306` (6.7:1 on `--bg`), `--success` `#081308` (6.8:1) and `--warning` `#14150a` (6.6:1) are within a few percent of the ink, so a Delete or Confirm button reads as ink, not as a brown or teal. The labels and shapes say which is which, not the hue; a danger button also leads with a "!". The real phone had no such colours.
- **Waveform cue tags** mix 30% of their ink into `--waveform-bg`; under the tag the theme sets a lighter LCD segment (`#b4cc9e`) so the ink stays above 4.5:1.
- `--on-accent` (`--bg`) on `--accent` is the same 7.1:1 invert used for selection.

## Reference status

`references/nokia-3310/` holds 3 device photos plus `RESEARCH.md`:

- `nokia-3310-blue.png` — front view of the blue-cased phone with a lit screen (clock, signal and battery bars on the sides, "Menü" softkey label). The only file that shows LCD tone, pixel font and status chrome.
- `nokia-3310-front.png` — an angled front view with an unlit grey screen; backs the casing, bezel and Navi-key.
- `nokia-3310-grey-front.jpg` — an Orange-branded grey 3310e front view (`RESEARCH.md`); backs casing and keypad only.

`RESEARCH.md` is explicit that the **LCD-screen gap is still open**: no original Series-20 menu screen capture exists in the folder. The top line and the single centred "Menu" softkey follow the two lit device photos; selection behaviour is from documented Series-20 behaviour, not from a screenshot. (An earlier note here claiming no reference folder was wrong.)

## v5 layout

Tiers (core): mobile ≤480px, tablet 481–900px, desktop 901–1800px, XL ≥1801px (shell capped at 1800px, centred). The handset framing is kept at every size. From 900px down the casing and its padding get thinner so the LCD keeps its width; the earpiece moves into the casing; and the signal and battery stacks sit on the bar's first line, smaller on a phone. From 901px up they hang below the bar down the LCD edges, and the main area (and the desktop wallpaper's icon column) gets matching inline padding. On a phone the segmented control's labels shrink to 0.85em so "Recovering" fits. The bar only sets inline padding, so core's block padding stays. The casing is painted on the page around the shell (`html:has(.app)`), not on `body`, which is the shell itself. On XL the gutters continue the casing with faint silver oval keys, three to a row.
