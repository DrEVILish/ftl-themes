# Nokia 3310

> The reflective yellow-green monochrome LCD of the 3310/3210 era: no backlight colour, no anti-aliasing, and selection reads as a hard colour invert rather than a highlight.

**Requires: L1** — sets `--app-*` layout properties (the inverted title strip); recolours correctly at L0 but the phone-screen composition needs the app shell.

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
   anything.
2. **Zero radius, zero gradient, zero shadow.** A reflective LCD segment
   display has none of these; every corner is square and every fill is
   flat.
3. **danger/success/warning are a documented compromise.** True hardware
   has no second colour at all; those three tokens use barely-different
   dark tones within the same LCD family specifically so the theme stays
   usable as a real design system without pretending the phone had a
   colour screen — see the comment beside them in `theme.css`.

## Signature details

- The signal-bars and battery-bars pseudo-elements in the corners of the
  app-bar — the one piece of chrome every candybar phone screen had.
- The inverted dark title strip across the top (`--app-bar-bg` set to
  the text colour, not the background) — the carrier-name bar convention.
- Bold, chunky text with no smoothing — this is a low-resolution segment
  display, not a modern hinted font.

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
- **Inherited outline:** the core `.icon` outline (2 units, round joins)
  also strokes every filled shape, so blocks look slightly soft and grow
  1 unit per side. Gaps between filled parts are therefore at least 3
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

`--font` and `--font-mono` are both `"Consolas", "Courier New", monospace`, bold at small sizes. **Nothing is vendored.** The real device uses a 5x7-ish pixel font on an 84x48 screen (`nokia-3310-blue.png` shows it in "Menü" and the clock); no faithful web copy is shipped, so the pixel shapes are lost and only the monospace feel remains. `RESEARCH.md` also records that a native screen capture is still missing, so the face is judged only from that one photo.

## Contrast honesty

- **Reference hue reconciled.** `RESEARCH.md`'s outsider read says "blue-green" LCD; the README and `theme.css` say yellow-green. The one capture that shows a lit screen (`nokia-3310-blue.png`) reads as a pale yellow-green with dark olive ink, and the casing is dark blue, which is probably the source of "blue". The shipped tones (`--bg` `#9ead86`, `--surface` `#a3b58c`, `--surface-2` `#94a17c`, ink `#1c2214`, darkened from `#2b3320` so core's tinted fills clear 4.5:1) are hand-picked olives, **not sampled from that photo** (unverified).
- **AAA warnings (`scripts/check.py`):** `--text` on `--surface` is 7.41:1 but on `--bg` 6.81:1 and on `--surface-2` 5.94:1 (floor 7.0:1). It clears AA everywhere but not AAA throughout; that is the real LCD's low contrast, and darkening the ink to near-black would look unlike the device.
- **`--muted` lifted:** `#363e24` (4.1:1 on `--surface-2`) to `#2d341e`, then to `#20271a` with the darker ink (6.99:1 on `--surface`, 5.6:1 on `--surface-2`). It is not really a second shade. On the dark strips (app bar, status bar, `.nav`) `--muted` and the state-text tokens flip to `--bg` (6.81:1).
- **Ink darkened:** `--text`/`--accent`/`--border` `#2b3320` (5.49:1 on `--bg`, 4.41:1 under an accent badge's 20% tint) to `#1c2214` (6.81:1 on `--bg`, 5.27:1 under the tint). The mark/comment-anchor tints are lighter so the ink stays above 4.5:1 on them.
- **State inks are a departure.** `--danger` `#3f2219` (6.03:1 on `--bg`), `--success` `#1a3122` (5.83:1) and `--warning` `#352b10` (5.83:1), darkened from `#4a2a1f`/`#1f3a28`/`#4a3d1a` so their 20% badge tints pass, are dark olive-family tones. The real phone had no such colours.
- `--on-accent` `#9ead86` on `--accent` `#1c2214` is the same 6.81:1 invert used for selection.

## Reference status

`references/nokia-3310/` holds 3 device photos plus `RESEARCH.md`:

- `nokia-3310-blue.png` — front view of the blue-cased phone with a lit screen (clock, signal and battery bars on the sides, "Menü" softkey label). The only file that shows LCD tone, pixel font and status chrome.
- `nokia-3310-front.png` — an angled front view with an unlit grey screen; backs the casing, bezel and Navi-key.
- `nokia-3310-grey-front.jpg` — an Orange-branded grey 3310e front view (`RESEARCH.md`); backs casing and keypad only.

`RESEARCH.md` is explicit that the **LCD-screen gap is still open**: no original Series-20 menu screen capture exists in the folder. The inverted title strip, softkey layout and selection behaviour are therefore from documented behaviour, not from a screenshot. (An earlier note here claiming no reference folder was wrong.)

## v5 layout

Tiers (core): mobile ≤480px, tablet 481–900px, desktop 901–1800px, XL ≥1801px (shell capped at 1800px, centred). The handset framing is kept at every size. From 900px down the casing and its padding get thinner so the LCD keeps its width; the earpiece moves into the casing; and the signal and battery bars sit on the bar's first line, smaller on a phone. The casing is painted on the page around the shell (`html:has(.app)`), not on `body`, which is the shell itself. On XL the gutters continue the casing with a moulded keypad of rounded keys, three to a row, a shade lighter than the plastic (about 1.1:1 against the casing).
