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
2. **Zero radius, zero gradient, zero shadow.** A reflective LCD segment
   display has none of these; every corner is square and every fill is
   flat.
3. **danger/success/warning are a documented compromise.** True hardware
   has no second colour at all; those three tokens use barely-different
   dark tones within the same LCD family specifically so the theme stays
   usable as a real design system without pretending the phone had a
   colour screen — see the comment beside them in `theme.css`.

## Signature details

- Signal (left) and battery (right) as vertical ink stacks at the app
  bar's outer edges: stepped bars widest at the top, an antenna and a
  battery glyph at the base, as on the 3310's idle screen
  (`nokia-3310-blue.png`), drawn as pixel-exact SVGs in the ink colour.
- One LCD tone top to bottom, as in both lit captures: the top line is
  plain LCD with a 2px ink rule; the bottom line carries a single centred
  bold "Menu" (the Navi-key's one softkey label) on its own row. No
  inverted strips; inversion is kept for selection.
- The handset around the screen: navy casing (`#3c3e4e`, sampled), a
  silver lens ring (`#b9bbb6`) and a darker navy bezel (`#343849`). On XL
  the gutters carry faint silver oval keys, three to a row. A sidebar
  beside the shell (an `aside` sibling of `.app`) is its own LCD panel.
- The slider is an ink rail (`--slider-bg: var(--text)`) with a square
  ink thumb.
- Bold, chunky text: body 600 (the mono's bold cut), headings, labels,
  nav and buttons 700, `-webkit-font-smoothing: none` where honoured.

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
- **Inherited outline:** the core `.icon` outline (2.5 units via `--icon-stroke-width`, round joins)
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

`--font` and `--font-mono` are both `"Consolas", "Courier New", monospace`, at weight 600 for body and 700 for headings, labels, nav and buttons. **Nothing is vendored.** A pixel face (an OFL bitmap-style family such as Pixelify Sans) would need adding to `assets/fonts/` with its NOTICE entry, which is outside this theme's folder; it is requested, not shipped. The real device uses a 5x7-ish pixel font on an 84x48 screen (`nokia-3310-blue.png` shows it in "Menü" and the clock); no faithful web copy is shipped, so the pixel shapes are lost and only the monospace feel remains. `RESEARCH.md` also records that a native screen capture is still missing, so the face is judged only from that one photo.

## Contrast honesty

- **Reference hue reconciled.** `RESEARCH.md`'s outsider read says "blue-green" LCD; the README and `theme.css` say yellow-green. The one capture that shows a lit screen (`nokia-3310-blue.png`) reads as a pale yellow-green with dark olive ink, and the casing is dark blue, which is probably the source of "blue". The lit screen samples at `#6f9462`–`#749468`. The shipped tones move toward it but sit a step lighter so the ink keeps 7:1: `--bg` `#8fae78`, `--surface` `#98b682`, `--surface-2` `#84a06e`, ink `#121a0e` (7.2:1 on `--bg`, 7.9:1 on `--surface`, 6.1:1 on `--surface-2`).
- **AAA:** `--text` clears 7:1 on `--bg` and `--surface` but is 6.1:1 on `--surface-2`; that is the real LCD's low contrast.
- **`--muted`** `#1a2312` (5.6:1 on `--surface-2`) is not really a second shade. On a free-standing dark `.nav` strip `--muted` and the state-text tokens flip to `--bg`.
- **State inks are a departure.** `--danger` `#2e2a14` (an olive-brown, 5.8:1 on `--bg`; was a visible maroon `#3f2219`), `--success` `#1a3122` and `--warning` `#352b10` (5.6:1) are dark olive-family tones. The real phone had no such colours.
- **Waveform cue tags** mix 30% of their ink into `--waveform-bg`; under the tag the theme sets a lighter LCD segment (`#b4cc9e`) so the ink stays above 4.5:1.
- `--on-accent` (`--bg`) on `--accent` is the same 7.2:1 invert used for selection.

## Reference status

`references/nokia-3310/` holds 3 device photos plus `RESEARCH.md`:

- `nokia-3310-blue.png` — front view of the blue-cased phone with a lit screen (clock, signal and battery bars on the sides, "Menü" softkey label). The only file that shows LCD tone, pixel font and status chrome.
- `nokia-3310-front.png` — an angled front view with an unlit grey screen; backs the casing, bezel and Navi-key.
- `nokia-3310-grey-front.jpg` — an Orange-branded grey 3310e front view (`RESEARCH.md`); backs casing and keypad only.

`RESEARCH.md` is explicit that the **LCD-screen gap is still open**: no original Series-20 menu screen capture exists in the folder. The top line and the single centred "Menu" softkey follow the two lit device photos; selection behaviour is from documented Series-20 behaviour, not from a screenshot. (An earlier note here claiming no reference folder was wrong.)

## v5 layout

Tiers (core): mobile ≤480px, tablet 481–900px, desktop 901–1800px, XL ≥1801px (shell capped at 1800px, centred). The handset framing is kept at every size. From 900px down the casing and its padding get thinner so the LCD keeps its width; the earpiece moves into the casing; and the signal and battery stacks sit on the bar's first line, smaller on a phone. On a phone the segmented control's labels shrink to 0.85em so "Recovering" fits. The bar only sets inline padding, so core's block padding stays. The casing is painted on the page around the shell (`html:has(.app)`), not on `body`, which is the shell itself. On XL the gutters continue the casing with faint silver oval keys, three to a row.
