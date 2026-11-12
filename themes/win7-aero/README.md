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
3. **The desktop shows through the frame.** The title bar, the side
   borders and the status strip are tinted glass over the Aero blue
   desktop; the client area inside them is opaque white, as in
   Explorer and every Win7 dialog.
4. **Rounded, not sharp.** `--radius: 6px` — softer than Luna's 8px
   pill-adjacent buttons, closer to a subtle window-corner round.
5. **Glass is chrome, controls are not.** Title bar, frame and status
   strip are glass; buttons and tabs are Win7's opaque grey gloss
   (`#f2f2f2 → #ebebeb | #dddddd → #cfcfcf`, hard split at 50%, `#707070`
   frame), turning pale Aero blue with a `#3c7fb1` frame on hover. The
   primary (default) button wears that blue state plus a cyan glow.

## Signature details

- Modals and dropdowns carry a real `backdrop-filter: blur(20px)
  saturate(0.8)`, the title bar and status strip 24px. The client area is
  opaque white and is not blurred (a full-height blurred scroller cost
  phones most of their frames); buttons, panels and toolbars on it do not
  blur either. Touch devices drop to a plain `blur(12px)`.
- The title bar carries Aero's faint diagonal **glare streaks**, a 1px
  dark outer frame, black caption text with a soft **white glow** behind
  it, and the joined **caption-button group** (min / max / red close)
  hanging flush from the top edge, drawn as one inline SVG. The glass
  desaturates what shows through it (`saturate(0.65)`), so the frame
  reads as Sky's cool blue-grey over the wallpaper, not cornflower. Bar text and
  breadcrumbs are `#000` with the glow, never Luna's white outline.
- The window frame: the white client area sits `--w7-frame` (7px) inside
  a tinted glass border down both sides, as dialogs (`--modal-bg`) do.
- Panel captions are a full-width glass strip across the panel top,
  padded in from its edges; headings are Segoe UI regular in Explorer's
  navy `#1e395b`.
- Desktop windows: glass frame and black-with-glow caption whether active
  or not, glass minimise/maximise beside the 43×20 red close with its
  white ×, also when the buttons are wrapped in their own span: one
  flush strip hanging from the top edge (min rounded bottom-left only,
  neighbours share a 1px `#1d3a5c` divider, a wrapper's gap is
  cancelled, the drawn close is dropped once a real one exists). The
  taskbar (and any `.app-status.taskbar`) is translucent blue-grey glass
  (`rgb(40 70 100 / 0.55)` plus 22% tint) with a white top highlight and
  white text on a dark text-shadow; the Start button is the round orb.
- Explorer's command bar (`--toolbar-bg`, pale blue `#f5faff → #dce8f6`),
  details-view headers (white → `#f1f5fb`, `#d5dfe5` divider), the Win7
  trackbar (a 4px `#d6d9dc` groove with a `#6e6e6e` top edge, 3:1 on
  white, and a white bottom
  edge, drawn on the content box inside core's 24/44px hit area, sideways
  for vertical faders; grey-gloss thumb),
  check boxes with a `#4a5f97` tick — no Luna beige, orange or green
  left on controls.
- Text boxes, selects and text areas are grey-framed (`#abadb3`) at rest
  and turn blue only on hover (`#7eb4ea`) and focus (`#569de5`).
- Toasts and alerts are notification balloons: white to `#e4e5f0`, a 1px
  `#767676` frame, 3px corners, and the Win7 message icon (blue *i*,
  green check, yellow *!*, red *x*) carrying the state, not a coloured
  border.
- Desktop icons stay white with a drop shadow when selected; the whole
  item gets Win7's `rgba(255,255,255,.25)` fill in a half-white frame.
- The desktop is the Windows 7 **"Harmony"** wallpaper: deep-to-bright
  blue, glowing light swooshes and a bloom where the logo sits — sharp
  enough shapes that the frost visibly softens them.
- Selection is Explorer's pale-blue fill (`#e5f1fd → #c4dcf9`) in a 1px
  `#7da2ce` frame with black text, never a leading accent bar or a solid
  blue block: tables (a stacked phone row frames the whole card, not each
  cell), lists, side nav, ticket cards, segmented and toggle buttons, the
  current page and pressed filter chips. The nav rail's current item gets
  the same framed fill instead of core's leading marker. Chips and badges are 3px boxes,
  not pills. Solid `#1265c7` is for links and focus. Tabs are raised gloss
  tabs, the selected one white; progress is the glossy green bar in a
  15px sunken grey trough (meters 12px).

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

The shell becomes **one glass window**: title bar, a white client area
(`rgb(255 255 255 / 0.94)`) inset in a 7px tinted glass border on both
sides, and a frosted status strip, joined inside one dark hairline frame
over the Harmony desktop. Outside the window the page is the light `--bg`
the text tokens are built for.

## v5 layout

Tiers: mobile ≤480px, tablet 481–900px, desktop 901–1800px, XL ≥1801px (the shell is capped at 1800px and centred, with gutter art beside it).

- **Phone (≤480) and tablet (481–900):** core puts brand and actions on the bar's first line and the nav on a second. The caption buttons get their own 20px strip along the top edge instead of the desktop's right-hand reserve (the group's 104px plus 1rem), which on a phone had pushed the actions onto two extra lines.
- **Nested surfaces step down:** only a top-level panel is a glass window with a caption bar. A panel inside a panel, card, dialog, drawer or flyout is a group box: a pale tinted label strip, no reflection and no second blur. Buttons, toolbars and navs inside a surface skip the blur too. The title-bar reflection now paints under the header's content (isolated, `z-index: -1`) and follows the corners with `border-radius: inherit` instead of `overflow: hidden`, so it never washes over a title or clips a menu opened from a header control. Minimise and maximise take the caption's black.
- **XL gutters (≥1801):** the Harmony desktop either side of the window: two soft light swooshes and Aero's faint diagonal glare over the blue desktop. Still.

## Tell-tales of an inauthentic result

- No `backdrop-filter` anywhere — an opaque theme with a blue accent is
  `winxp-luna`, not this.
- A solid, untinted window frame, or a client area tinted cyan by the
  desktop behind it.
- Saturated Luna-blue instead of Aero's cooler, calmer tone.
- A flat page backdrop instead of the desktop gradient.

## Don'ts

- **No opaque grey window frames.** Glass means real `backdrop-filter` blur over a coloured backdrop.
- **No flat, unblurred frame:** the title bar, side borders and status strip are glass.
- **No dark caption text without the light glow/shadow** on glass; captions are readable because of the halo.
- **No hard 1px black outlines.** Glass edges are pale inner highlights.
- **No Windows XP/Luna gloss or square Windows 95 bevels** as decoration.
- **No system-ui/Roboto in place of Segoe UI** where Segoe UI is available.

## Typography

`--font` is `"Segoe UI", Selawik, "Noto Sans", "Open Sans", "Liberation Sans", Tahoma, sans-serif`; `--font-mono` is `Consolas, "Lucida Console", "Liberation Mono", "DejaVu Sans Mono", monospace`. Segoe UI is the reference face (`references/win7-aero/RESEARCH.md` and the `Segoe_UI_Revision_Differences.png` capture) and is **system-only, not vendored**: Windows ships it, macOS/Linux do not. Segoe UI is not open-licensed, so vendoring is not an option; Selawik, its open (OFL) metric-compatible stand-in, comes next and is used where installed (vendoring it into `assets/fonts/` is requested; not done in this theme folder), then the nearest humanist faces. The page sets `font-size-adjust: 0.5`, Segoe UI's own x-height ratio, so it changes nothing where Segoe UI renders but scales a wide fallback (DejaVu, Tahoma) down to Segoe's x-height and keeps Win7's compact 9pt proportions.

## Contrast honesty

- **Accent lifted from the reference:** the Aero blue `#1c6fd1` is 2.69:1 against the desktop backdrop `--bg` `#a6c2e0` (a fail for text on the backdrop). Shipped `--accent` is `#1265c7`: 3.08:1 on `--bg` (the 3.0:1 soft floor), 5.21:1 on `--surface`, 5.66:1 under white text.
- **Primary button:** dark `#1a1a1a` text on the pale-blue gloss.
- **App bar:** brand, nav items and bar text `#000000` on the frosted bar, with a white glow behind them (`0 0 8px #fff, 0 0 2px #fff, 0 0 12px rgba(255,255,255,.8)`, as Win7's caption glow plate). Dark tints (Twilight, Ruby, Violet, Chocolate, Slate) mix into a denser frost (`rgb(236 241 248 / 0.64–0.72)`), as Win7's colour-intensity slider would, so the glass stays light enough for the black caption (Chocolate title glass measured about 5.5:1 against black, up from 3.2:1).
- **Status strip:** black text with the caption's white glow on the glass (the old `#2b3540` measured 3.6:1).
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
mixed into a pale sky frost (`--w7-frost`, `rgb(228 238 248 / 0.5–0.58)`)
on the title bar, dialogs, side frame and status strip (35% fading
to 41%; dark tints use a denser `rgb(236 241 248 / 0.64–0.72)` frost), so Sky glass lands near the
reference's `rgb(160,195,230)`; into a pale blue floor (not white, so the
Frost tint still shows a caption strip) on panel captions and into dark blue-grey
on the taskbar, so the desktop carries the colour and the black caption text with its
white glow stays readable at every tint. The other fifteen presets are
variants: `twilight`, `sea`, `leaf`, `lime`, `sun`, `pumpkin`, `ruby`,
`fuchsia`, `blush`, `violet`, `lavender`, `taupe`, `chocolate`, `slate`,
`frost` (values in `references/win7-aero/RESEARCH.md`; approximate,
community-collected colorization values).

The token is declared as this theme's **tint** (`Tint:` header →
`tint` in `dist/themes.json`), so apps must offer it as a colour control
alongside the theme and sub-theme choice — any colour, not only the
presets, as Win7's colour mixer allowed. See CONTRACT.md "Theme tint".
