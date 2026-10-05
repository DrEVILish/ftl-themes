# Windows 7 Aero

> Frosted glass and soft blue gloss — more restrained than Luna.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

**Family:** Windows desktop; extends [Windows XP (Luna)](../winxp-luna/README.md).

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
5. **Glass is chrome, controls are not.** Title bar, frame and status
   strip are glass; buttons and tabs are Win7's opaque grey gloss
   (`#f2f2f2 → #ebebeb | #dddddd → #cfcfcf`, hard split at 50%, `#707070`
   frame), turning pale Aero blue with a `#3c7fb1` frame on hover. The
   primary (default) button wears that blue state plus a cyan glow.

## Signature details

- Panels, modals, dropdowns, the toolbar and the content well carry a real
  `backdrop-filter: blur(20px) saturate(1.6)`; the title bar and status
  strip 24px — the property that makes glass read as glass.
- The title bar carries Aero's faint diagonal **glare streaks**, a 1px
  dark outer frame, black caption text with a soft **white glow** behind
  it, and the joined **caption-button group** (min / max / red close)
  tucked under the top edge, drawn as one inline SVG.
- The desktop is the Windows 7 **"Harmony"** wallpaper: deep-to-bright
  blue, glowing light swooshes and a bloom where the logo sits — sharp
  enough shapes that the frost visibly softens them.
- Selection is Explorer's pale-blue fill in a `#99d1ff` frame; tabs are
  raised gloss tabs, the selected one white; progress is the glossy
  green bar.

## Icons

`themes/win7-aero/icons.svg` covers the full core icon set (178/178, plus
`sun-moon`) as soft glassy line work on the generic 24×24 grid. It uses
the inherited outline stroke, `fill="none"` and `currentColor`; boxes get
generous radii (`rx` 2.5, 5 on square buttons, pill bars) and triangles
get round joins. Most enclosed shapes (box, circle, page, cloud, bubble,
triangle) also carry the **catch-light**: a heavier
`stroke-width="2.2"`–`"3"`, `opacity="0.5"` stroke traced along their top
edge only, echoing the glass highlight on every panel and button. Pure
line glyphs (arrows, chevrons, carets, sort, shuffle, hash, frame, road,
repeat, dots) have no highlight.

## Layout

The shell becomes **one glass window**: title bar, a near-white frosted
client area (`rgba(255,255,255,0.72)`, so only a hint of desktop colour
comes through, as in a real Win7 window) and a frosted status strip,
joined inside one dark hairline frame over the Harmony desktop.

## v5 layout

Tiers: mobile ≤480px, tablet 481–900px, desktop 901–1800px, XL ≥1801px (the shell is capped at 1800px and centred, with gutter art beside it).

- **Phone (≤480) and tablet (481–900):** core puts brand and actions on the bar's first line and the nav on a second. The caption buttons get their own 20px strip along the top edge instead of the desktop's 7.5rem right-hand reserve, which on a phone had pushed the actions onto two extra lines.
- **Nested surfaces step down:** only a top-level panel is a glass window with a caption bar. A panel inside a panel, card, dialog, drawer or flyout is a group box: a pale tinted label strip, no reflection and no second blur. Buttons, toolbars and navs inside a surface skip the blur too. The title-bar reflection now paints under the header's content (isolated, `z-index: -1`) and follows the corners with `border-radius: inherit` instead of `overflow: hidden`, so it never washes over a title or clips a menu opened from a header control. Minimise and maximise take the caption's black.
- **XL gutters (≥1801):** the Harmony desktop either side of the window: two soft light swooshes and Aero's faint diagonal glare over the blue desktop. Still.

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
- **Primary button:** dark `#1a1a1a` text on the pale-blue gloss.
- **App bar:** brand `#000000` and nav items `#1a1a1a` on the frosted bar, with a white glow behind them.
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

## Window Color (theme tint) and its preset variants

Windows 7's *Personalize → Window Color* tinted all the glass. The theme
does the same through one token, `--aero-tint` (default Sky `#74b8fc`),
mixed into translucent white on the title bar, status strip and panel
captions (into dark on the taskbar), so the black caption text with its
white glow stays readable at every tint. The other fifteen presets are
variants: `twilight`, `sea`, `leaf`, `lime`, `sun`, `pumpkin`, `ruby`,
`fuchsia`, `blush`, `violet`, `lavender`, `taupe`, `chocolate`, `slate`,
`frost` (values in `references/win7-aero/RESEARCH.md`; approximate,
community-collected colorization values).

The token is declared as this theme's **tint** (`Tint:` header →
`tint` in `dist/themes.json`), so apps must offer it as a colour control
alongside the theme and sub-theme choice — any colour, not only the
presets, as Win7's colour mixer allowed. See CONTRACT.md "Theme tint".
