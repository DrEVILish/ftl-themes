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

### Icons

`themes/nokia-3310/icons.svg` redraws six icons (home, settings, search,
close, user, bell) as coarse, low-resolution monochrome LCD segment
shapes: big flat `currentColor` polygons and rects with minimal internal
detail, no anti-aliasing and almost no curves — the kind of menu glyph a
real feature-phone screen could actually render at its native
resolution. The sprite ships 123 `<symbol>`s in total (`grep -c '<symbol'`), and each differs from the generic outline sprite in `assets/icons/icons.svg`; only the six above are described here, and the rest were not audited one by one for style.

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

- **Reference hue reconciled.** `RESEARCH.md`'s outsider read says "blue-green" LCD; the README and `theme.css` say yellow-green. The one capture that shows a lit screen (`nokia-3310-blue.png`) reads as a pale yellow-green with dark olive ink, and the casing is dark blue, which is probably the source of "blue". The shipped tones (`--bg` `#9ead86`, `--surface` `#a3b58c`, `--surface-2` `#94a17c`, ink `#2b3320`) are hand-picked olives, **not sampled from that photo** (unverified).
- **AAA warnings (`scripts/check.py`):** `--text` on `--surface` is 6.0:1 and on `--bg` 5.5:1 (floor 7.0:1). It clears AA everywhere but not AAA; that is the real LCD's low contrast, and darkening the ink further would look unlike the device.
- **`--muted` lifted:** `#363e24` (4.1:1 on `--surface-2`) to `#2d341e` (5.89:1 on `--surface`, 4.72:1 on `--surface-2`). It is not really a second shade.
- **State inks are a departure.** `--danger` `#4a2a1f` (5.34:1 on `--bg`), `--success` `#1f3a28` (5.18:1) and `--warning` `#4a3d1a` (4.45:1 on `--bg`, just under 4.5:1 if used as text there) are dark olive-family tones. The real phone had no such colours.
- `--on-accent` `#9ead86` on `--accent` `#2b3320` is the same 5.49:1 invert used for selection.

## Reference status

`references/nokia-3310/` holds 3 device photos plus `RESEARCH.md`:

- `nokia-3310-blue.png` — front view of the blue-cased phone with a lit screen (clock, signal and battery bars on the sides, "Menü" softkey label). The only file that shows LCD tone, pixel font and status chrome.
- `nokia-3310-front.png` — an angled front view with an unlit grey screen; backs the casing, bezel and Navi-key.
- `nokia-3310-grey-front.jpg` — an Orange-branded grey 3310e front view (`RESEARCH.md`); backs casing and keypad only.

`RESEARCH.md` is explicit that the **LCD-screen gap is still open**: no original Series-20 menu screen capture exists in the folder. The inverted title strip, softkey layout and selection behaviour are therefore from documented behaviour, not from a screenshot. (An earlier note here claiming no reference folder was wrong.)
