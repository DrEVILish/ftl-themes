# Windows 7 Aero

> Frosted glass and soft blue gloss — more restrained than Luna.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

**Windows 7's Aero Glass**: translucent, blurred window chrome over the
Aero blue desktop gradient, rounded corners, and a calmer, cooler gloss
than XP's opaque plastic. The generation that replaced "shiny" with
"glass."

## Core values

1. **Glass, not plastic.** Every chrome surface is translucent and
   genuinely blurred (`backdrop-filter`), not just a lighter opaque fill.
   An Aero theme with no blur is a `winxp-luna` palette swap wearing this
   theme's name.
2. **Restraint over Luna's saturation.** The blue is cooler and less
   saturated than Luna's `#0054e3`; gloss highlights are soft edges, not
   hard gradient stops.
3. **The desktop shows through.** Content areas are semi-transparent over
   the Aero blue gradient backdrop — the window is a pane of glass over
   the desktop, not an opaque card floating on it.
4. **Rounded, not sharp.** `--radius: 6px` — softer than Luna's 8px
   pill-adjacent buttons, closer to a subtle window-corner round.
5. **Light theme discipline.** Filled primary buttons need explicit white
   text (`--on-accent`), same reasoning as every light theme in this
   catalog.

## Signature details

- Buttons, panels, modals, the nav bar, and the toolbar all carry a real
  `backdrop-filter: blur(8px) saturate(1.4)` — this is the one CSS
  property that makes "glass" read as glass instead of "translucent gray."
- The app bar and status strip blur even harder (10px) and get an inset
  top highlight, the glass-edge catch-light.
- The page backdrop is the Aero blue gradient, not a flat color — glass
  needs something behind it worth seeing through.

## Layout

The shell becomes a **floating glass window**: a blurred, rounded title
bar, a near-transparent content well, and a frosted taskbar-style status
strip, with the Aero blue desktop gradient visible behind and through all
of it.

## Tell-tales of an inauthentic result

- No `backdrop-filter` anywhere — an opaque theme with a blue accent is
  `winxp-luna`, not this.
- A solid, non-transparent content background.
- Saturated Luna-blue instead of Aero's cooler, calmer tone.
- A flat page backdrop instead of the desktop gradient.

## Don'ts

- **No opaque grey window frames.** Glass means real `backdrop-filter` blur over a coloured backdrop.
- **No flat, unblurred panels** on the frame, nav, toolbar and main well.
- **No dark caption text without the light glow/shadow** on glass; captions are readable because of the halo.
- **No hard 1px black outlines.** Glass edges are pale inner highlights.
- **No Windows XP/Luna gloss or square Windows 95 bevels** as decoration.
- **No system-ui/Roboto in place of Segoe UI** where Segoe UI is available.

## Typography

`--font` is `"Segoe UI", Tahoma, sans-serif`; `--font-mono` is `Consolas, monospace`. Segoe UI is the reference face (`references/win7-aero/RESEARCH.md` and the `Segoe_UI_Revision_Differences.png` capture) and is **system-only, not vendored**: Windows ships it, macOS/Linux do not, so there Tahoma or the generic sans renders and the look shifts noticeably. Segoe UI is not open-licensed, so vendoring is not an option.

## Contrast honesty

- **Accent lifted from the reference:** the Aero blue `#1c6fd1` is 2.69:1 against the desktop backdrop `--bg` `#a6c2e0` (a fail for text on the backdrop). Shipped `--accent` is `#1265c7`: 3.08:1 on `--bg` (the 3.0:1 soft floor), 5.21:1 on `--surface`, 5.66:1 under white text.
- **Primary button:** the white label was 2.8:1 on the old pale glass top stop; the glass is deepened (rgba(40,110,200) to rgba(14,74,150)).
- **App bar:** the accent measured 4.3:1 on the frosted bar over the desktop gradient, so the brand uses `#0b4a94` (8.67:1 on the backdrop) and nav items `#3f4852`.
- **`--muted`** `#55606b` is 5.91:1 on `--surface` but 3.49:1 directly on `--bg`; do not set muted text on the bare backdrop.
- `--danger`, `--success`, `--warning` on `--bg` are 2.96 / 2.79 / 1.77:1: fills only; use the `-text` variants for copy.

## Reference status

`references/win7-aero/` has 5 captures plus `RESEARCH.md`: `Aero_Example.png` (glass frames), `Aero_Peek.png` (glass sheets), `Segoe_UI_Revision_Differences.png` (type comparison), `maxresdefault.jpg` (Personalization window) and the Frutiger-Aero glass-texture collage (`updated-guide-to-original-frutiger-aero…webp`). They back the frosted glass, the blue-teal aurora and Segoe UI. Two captures with faces were removed; no Flip3D or glass-taskbar capture is in the folder. No hex values are recorded, so `#1c6fd1` (cited in `theme.css`) is the only reference blue and its source is not in the folder.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.

`backdrop-filter` support: this theme degrades gracefully in engines
without it — surfaces fall back to their plain translucent color with no
blur, still legible, just not glassy.
