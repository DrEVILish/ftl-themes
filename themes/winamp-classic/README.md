# WinAmp Classic

> Steel-gray skinned player — tiny caps, llama-green readouts.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

A **skinned desktop media player** from the late 1990s: a compact steel
window, brushed horizontal texture, tiny uppercase labels, and a bright
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

## Layout

The shell is a **player window**: 0.25rem outer padding, a 1.8rem beveled
gradient title bar, a bordered inset content area, and a gradient footer.
Everything is snug against everything else.

## Tell-tales of an inauthentic result

- Large comfortable type → a modern music app, not a skin.
- Flat grey with no texture.
- Green used as a general accent rather than confined to readouts.
- Rounded corners anywhere.

## Don'ts

- **No LCD green as a general accent.** It is confined to readouts, meters and slider caps; headings, nav and buttons stay steel/khaki.
- **No radius above `0.1rem`, no gloss.** Chunky 2px bevels only.
- **No body copy in the LCD face.** Only h1 and the readout/table digits use the mono stack.
- **No yellow fader caps here** without knowing this deviates from the reference (see Contrast honesty).

## Typography

`--font` is `Arial, Helvetica, sans-serif`; `--font-mono` is `"Fixedsys", "Courier New", Consolas, monospace`. **All system fonts, none vendored.** The real skin's readout uses a bitmap pixel font (Fixedsys is the closest system relative on Windows); on other systems Courier New renders, which is thinner and rounder. Labels are tiny and uppercase.

## Contrast honesty

- **LCD green `#00ff00` (`--accent`)** is 12.42:1 on `--bg` and 8.29:1 on `--surface`. `RESEARCH.md` records no hex for the real skin's green, so that value is the theme's own, unverified against captures.
- **Yellow fader deviation.** The reference has yellow EQ faders (`RESEARCH.md`). The theme's slider thumb is `--accent-2` lime `#a4ff30` (13.74:1 on `--bg`), not yellow. The only yellow is `--warning` `#ffcc00` (11.27:1), used for warning states. This is a colour deviation, not a contrast lift: yellow would also pass.
- **Muted lifted:** `#9a9a8c` (3.1:1) to `#bbbbb2` (8.82:1 on `--bg`, 5.88:1 on `--surface`, 4.58:1 on `--surface-2`).
- **Nav items lifted** from `--muted` (4.1:1 on the bar's lighter top stop) to `#c8c8b8` (6.72:1 on `--surface`, 5.24:1 on `--surface-2`).
- **State text:** `--success-text` `#00d900` (5.92:1 on `--surface`) and `--danger-text` `#f1a8a8` (5.91:1); the raw `--danger` `#cc2020` is 3.08:1 on `--bg` (fill only, white text 5.53:1).

## Reference status

`references/winamp-classic/` has 3 captures plus `RESEARCH.md`: `WinAmp_5.9.2,_Windows_10.png` (a Vista-glass skin showing main window, EQ and playlist), `ddbr1i4-….png` (a Classic Modern lite skin, full stack) and `winamp-classic-screenshot.avif`. They back the steel-grey bevelled buttons, green LCD readout and playlist editor. Note that two are modern-skin variants, not the 2.x classic skin the theme names; `RESEARCH.md` records no hex values.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
