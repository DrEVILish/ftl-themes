# WinAmp Classic

> Indigo-grey skinned player — silver keys, tiny caps, llama-green readouts.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

A **skinned desktop media player** from the late 1990s: a compact
indigo-grey window (the 2.x base skin's chassis, `#32324f`), brushed
horizontal texture, pale silver-blue keys, tiny uppercase labels, and a bright
green LCD-style readout. It really whips the llama's ass.

## Core values

1. **Small, tight, compact.** This is a player window that lives in a
   corner of the screen, not a full-page app. Type is small; the title bar
   is 1.8rem.
2. **Steel texture, not flat grey.** A 4px repeating horizontal gradient
   gives the brushed-metal body.
3. **The readout is green-on-black.** Track info and values set in the
   monospace face on true black — an LCD panel inset into the chassis.
4. **Beveled hardware.** Like Windows 95 but subtler: 1px two-tone borders,
   inverted on press.
5. **Uppercase micro-labels.** Buttons are tiny caps, as on the original's
   transport row.

## Signature details

- Inputs are black with green monospace text — they read as the display,
  not as form fields.
- Sliders are square-thumbed with a llama-green cap.
- The status strip repeats the chassis gradient, framing the window.

## Icons

`icons.svg` redraws the whole core set (178/178, 182 `<symbol>`s) as thin
LCD-segment line work with a hardware readout feel:

- 24×24 grid, outline only. The stroke comes from the theme's
  `--icon-stroke-width: 1.5`. Symbols set no stroke or fill of their own,
  so caps and joins stay core's round default.
- Geometric and blocky, never curvy. Circles become octagons (vertices at
  22.5° + k·45°), ellipses become six-sided lozenges, and arcs become
  straight angled segments (moon, clouds, rainbow, coins).
- `currentColor` only, so icons read green-on-black and in the selected
  state alike.
- From "Round 2" on, shapes share geometry with `windows95` (same
  octagons, thinner line). The last 47 ids ("Round 3", core-set top-up)
  came from a generator that reproduces that rendering.
  `icon-player-play` copies `icon-play`.

## Layout

The shell is a **player window**: 0.25rem outer padding, a 1.8rem beveled
gradient title bar, a bordered inset content area, and a gradient footer.
Everything is snug against everything else.

## v5 layout

Tiers: mobile ≤480px, tablet 481–900px, desktop 901–1800px, XL ≥1801px (the shell is capped at 1800px and centred, with gutter art beside it).

- **Phone (≤480) and tablet (481–900):** core's one-column shell; the compact player chrome already fits a phone. The bar's right padding now clears the dotted grip, so the last action never sits on it (on desktop too).
- **XL gutters (≥1801):** the spectrum analyser along the foot of the desk: twelve-band bars in a dim, translucent analyser green, with the page's brushed 4px ribbing showing through as LED segments. Paused, not animated.

## Tell-tales of an inauthentic result

- Large comfortable type → a modern music app, not a skin.
- Flat grey with no texture.
- Green used as a general accent rather than confined to readouts.
- Rounded corners anywhere.

## Don'ts

- **No LCD green as a general accent.** It is confined to readouts, meters, slider caps, the playlist's selected row text and the default (`.btn-primary`) button, drawn as the LCD (green on black); headings, nav and other buttons stay khaki or silver.
- **No radius above `0.1rem`, no gloss.** Chunky 2px bevels only.
- **No body copy in the LCD face.** Only h1 and the readout/table digits use the mono stack.
- **No yellow fader caps here** without knowing this deviates from the reference (see Contrast honesty).

## Typography

`--font` is `Arial, Helvetica, sans-serif`; `--font-mono` is `"Fixedsys", "Courier New", Consolas, monospace`. **All system fonts, none vendored.** The real skin's readout uses a bitmap pixel font (Fixedsys is the closest system relative on Windows); on other systems Courier New renders, which is thinner and rounder. Labels are tiny and uppercase.

## Contrast honesty

- **LCD green `#00ff00` (`--accent`)** is 12.42:1 on `--bg` and 8.29:1 on `--surface`. `RESEARCH.md` records no hex for the real skin's green, so that value is the theme's own, unverified against captures.
- **Yellow fader deviation.** The reference has yellow EQ faders (`RESEARCH.md`). The theme's slider thumb is `--accent-2` lime `#a4ff30` (13.74:1 on `--bg`), not yellow. The only yellow is `--warning` `#ffcc00` (11.27:1), used for warning states. This is a colour deviation, not a contrast lift: yellow would also pass.
- **Muted lifted:** `#9a9a8c` (3.1:1) to `#c2c2ba` (clears 4.5:1 on `--surface-2` and on the planner's series tints). User, series and highlight tints mix into `--bg`, not `--surface`, so the beige text keeps 4.5:1 on them.
- **Nav items lifted** from `--muted` (4.1:1 on the bar's lighter top stop) to `#c8c8b8` (6.72:1 on `--surface`, 5.24:1 on `--surface-2`).
- **State text:** `--success-text` `#00d900` (5.92:1 on `--surface`) and `--danger-text` `#f1a8a8` (5.91:1); the raw `--danger` `#cc2020` is 3.08:1 on `--bg` (fill only, white text 5.53:1).

## Reference status

`references/winamp-classic/` has 3 captures plus `RESEARCH.md`: `WinAmp_5.9.2,_Windows_10.png` (the classic base skin: main window, EQ and playlist, slightly rescaled), `ddbr1i4-….png` (a Classic Modern lite skin, full stack) and `winamp-classic-screenshot.avif`. They back the indigo-grey chassis, the silver keys, the green LCD readout and the playlist editor; `RESEARCH.md` tables the colours sampled from the base-skin capture. `ddbr1i4-….png` is a modern remake of the classic skin, not the original.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
