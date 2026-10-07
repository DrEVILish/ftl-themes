# Windows XP (Luna)

> The default Luna Blue desktop — glossy blue chrome, green go, rounded windows.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

**Family:** Windows desktop; extends [Windows 95](../windows95/README.md).

## What this theme is trying to achieve

The **Windows XP desktop as it shipped**, before anyone changed a setting:
the royal-blue glossy title bar with rounded corners, the tan/silver
"Luna" content background, Tahoma set everywhere, and the confident green
of the Start button. This is the theme most people picture the instant
someone says "Windows XP."

## Core values

1. **Gloss is the whole personality.** A light highlight band over every
   filled surface — the title bar, buttons, the nav bar — is what separates
   Luna from the flat Windows 95 look it replaced. Losing the highlight
   line at the top of the title bar is the single biggest tell.
2. **Round, never sharp.** `--radius: 8px`, and windows themselves get
   rounded top corners. XP retired square dialogs on purpose.
3. **Blue chrome, tan content.** The title bar and taskbar are the vivid
   royal blue (`#0054e3`); the actual working area is the calmer
   `#ece9d8` tan, with white cards for real content. Don't paint the
   content area blue — that's the chrome's color, not the page's.
4. **Green is Start, blue is selection.** The Start-button green is kept
   for the Start pill and the transport's GO (`.btn-go`); dialog buttons,
   including the primary one, are the white-to-beige Luna push button —
   the primary one marked, as XP marked its default button, by a blue
   inner glow. `.btn-success` stays green. The selection blue (`#316ac5`)
   is for "this row is chosen," not "click me."
5. **Tahoma, not a modern system font.** Segoe UI is the *next* Windows —
   swapping it in undoes the one typographic signal that says "XP."

## Signature details

- Modal headers repeat the title bar's exact three-stop gloss gradient.
- The title bar is Luna's own multi-stop gradient (bright `#0997ff` lip,
  `#0050ee` body, lighter `#0066ff` lower band, `#003dd7` bottom edge),
  with white bold Trebuchet MS text carrying a 1px `#0f1089` drop shadow,
  and three separate 21px caption buttons (blue minimize/maximize,
  red-orange close) drawn as one inline SVG.
- Push buttons: `#ffffff → #ecebe6 → #d6d0c5` face, 1px `#003c74` border,
  3px corners; hover lights XP's orange inner glow, the primary/default
  button wears the blue one.
- Panels and cards are **group boxes**: a `#d0d0bf` hairline frame with
  3px corners and the caption in `#0046d5`, sitting on the frame line.
- Tabs are raised, round-topped, the selected one white with the orange
  `#ffc83c`/`#e68b2c` hot-track line on top.
- Checkboxes and radios are the Luna glyphs: beige-to-white wells in a
  `#1c5180` frame, green tick / green dot, orange glow on hover.
- Progress is XP's segmented green block bar; the status strip is the
  taskbar's own gradient.
- **Boot screen** (`.splash`): black, the four-pane flag, and three blue
  blocks marching through a rounded grey track (core's indeterminate
  sweep). `gallery.html` shows it while the themes load.

## Icons

`themes/winxp-luna/icons.svg` redraws the whole core set (178/178, 182
`<symbol>`s) as glossy two-tone glyphs: a `currentColor` fill for the base
shape, a soft white highlight band across the top for the gloss line Luna
put on every filled surface, and a thin `currentColor` outline to keep
edges crisp. That is the same three-layer recipe as the title bar and
buttons, applied at icon scale. Style rules:

- 24×24 grid. Closed shapes (rects, circles, closed paths) are filled
  `currentColor` at 0.85 opacity with a 1-unit `currentColor` outline and
  round joins.
- Open strokes are `currentColor`, 1.4 wide, with round caps and joins.
- Details that sit on a filled body (file text lines, fold corners, clock
  hands, envelope flaps, film perforations) are white strokes 1.4 wide,
  and small dots are filled white, like the white X on the close button.
  A slash across a filled body (eye-off, cloud-off) has a white gap under
  it.
- Gloss: one white ellipse at 0.3 opacity over the top-left of the
  icon's bounding box (centre 35%/22%, radii 28%/14% of the box). Glyphs
  that are only open lines get no gloss band.
- Shapes from "Round 2" on use the same straight-segment geometry as
  `windows95`, `winamp-classic` and `wmp11`, with real circles. The last
  47 ids ("Round 3", core-set top-up) came from a generator that applies
  these rules. `icon-player-play` copies `icon-play`.
- Known limit: in the selected state (`currentColor` turns white on
  blue), the white details merge into the fill, as on the original
  Round 1 icons.

## Variants

Select with `data-variant` on `<html>` (CONTRACT.md "Palette variants");
the window shape is shared, only the paint changes.

| `data-variant` | Look |
|---|---|
| *(none)* | Luna Blue: royal-blue gloss, beige `#ece9d8` dialog face. |
| `royale` | Royale / Media Center "Energy Blue": a glassier title bar with a strong upper highlight, cool grey-lilac `#ebe9ed` face, deep navy taskbar. |
| `royale-noir` | Royale Noir: glossy black chrome and caption buttons, neutral grey `#ececec` face, graphite `#4a4a4a` selection. The orange hot-track and green Start survive. |
| `zune` | The Zune theme (2006): Royale Noir's black glass with burnt-orange Start/GO, selection and headings on a neutral grey face. Orange deepened to `#a54400` for 4.5:1 under white. |
| `embedded` | XP Embedded / Windows Embedded Standard: deeper, flatter steel-blue title bar and taskbar, grey-blue face, **blue** Start/GO instead of green. |
| `olive` | Olive Green ("HomeStead"): olive title bar and taskbar, Luna's beige face, olive selection, green Start. The olive is held dark enough for white title text (the real highlight band was lighter). |
| `silver` | Silver ("Metallic"): light silver title bar and taskbar with **dark** title and taskbar text, silver caption buttons with dark glyphs (red close kept), cool grey face, grey selection with black text. |

## Layout

The app shell becomes an **XP window**: a glossy round-cornered blue title
bar on top, a darker-blue taskbar-style strip on the bottom, and the tan
Luna background filling the well between them.

## Tell-tales of an inauthentic result

- A flat, single-color title bar with no gloss highlight.
- Square corners anywhere on the window frame.
- Segoe UI or a modern system font in place of Tahoma.
- Blue used for the content background instead of the tan/white pairing.

## Don'ts

- **No flat, single-colour title bar** — the gloss highlight line at the top is the theme.
- **No square window corners**, and no pill/stadium shapes either: XP is `8px` rounding, not Barbie.
- **No blue content area.** Blue is chrome; the well is tan `#ece9d8` and white.
- **No green on selection.** Green is Start/GO, `#316ac5` blue is selection.
- **No Segoe UI or system-ui swapped in for Tahoma** where Tahoma exists.

## Typography

`--font` is `Tahoma, "Segoe UI", Verdana, sans-serif`; `--font-mono` is `"Courier New", Consolas, monospace`. Tahoma is the authentic XP face (named in `references/winxp-luna/RESEARCH.md`) but it is a **system font, not vendored**: Windows and macOS ship it, most Linux installs do not, and there Segoe UI/Verdana or the generic sans render instead.

## Contrast honesty

Luna's greens and blues sit on tan/white, and several needed adjustment:

- **Start green lifted.** The community-recreation green `#3d9f1e` is 3.4:1 under white text; shipped `--success` is `#2e7a14` (5.37:1). No official hex exists (`luna.msstyles` is a compiled resource), so this is a documented departure from folk consensus, not from a published value.
- **Success text on tan:** `--success` itself is only 4.40:1 on the `#ece9d8` background, so text uses `--success-text` `#296e12` (5.1:1 on tan, 6.2:1 on white; deepened from `#2c7613` so it also clears 4.5:1 on badge, callout and diff tints).
- **Blue on tan:** `--accent` `#0054e3` is 5.10:1 on tan and 6.22:1 on white/under white text. The selection blue `--accent-2` `#316ac5` is 4.31:1 on tan, so use it as a fill with white text (5.25:1), not as text on the tan well.
- **Warning:** `--warning` `#ff8c00` is 1.91:1 on tan and is a lamp/fill only; text uses `--warning-text` `#955200` (4.95:1 on tan; deepened from `#9e5700` for the warning callout tint).
- `--danger` `#cc0000` is 4.83:1 on tan, 5.89:1 under white text; as text on its own badge tint it uses `--danger-text` `#bb0000`. `--muted` `#5a5a5a` is 5.65:1 on tan.
- The app-bar nav text uses pale tints because the black tokens tuned for the tan area measured 1.0:1 on the blue bar.

## Reference status

`references/winxp-luna/` has 5 captures plus `RESEARCH.md`: a Luna Start-button crop (`RESEARCH.md` does not map which filename is which), a March Mountain XP icon promo, a tall XP icon grid, a Luna Sample dialog and a Bliss desktop with a real Start menu. They back the royal-blue gloss title bar, the tan content colour, the green Start pill and the red-orange Close button. `RESEARCH.md` lists no hex values, so `#0054e3`, `#ece9d8`, `#316ac5` and `#7f9db9` are the theme's own numbers, not sampled from these files (unverified against them).

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.

## Dialogs and the taskbar

- **Every modal is an XP window:** the Luna title bar across the full
  width (rounded top corners, white bold Trebuchet caption, red close
  button), the title-bar blue carried down both sides and the bottom as a
  3px frame, the beige dialog face inside, square-cornered text fields
  and Luna push buttons (`.btn-secondary` included). Each variant's title
  bar and frame follow automatically.
- **The status strip is the taskbar:** the Start button at the left —
  italic "start" with the flag, rounded on its right, green (orange for
  Zune, blue for Embedded via `--taskbar-start-bg`) — status items along
  the bar, and the last item in the notification-area tray (a lighter
  well with a dark left edge; charcoal on Royale Noir/Zune). The Start
  button is dropped on phones.

## v5 layout

- **Tiers.** Desktop is unchanged. Tablet keeps the glossy title bar; it
  wraps to two lines and the caption buttons pin to the first line's right
  end. Mobile drops the decorative caption buttons (their 5.4rem would push
  the actions onto a line of their own) and the Start button on the
  taskbar. No rail on any tier. A bare checkbox in a table cell is drawn at
  24px on touch tiers, as in core.
- **Nesting.** Group-box captions sit on the frame line at every depth.
  Where a caption can't sit on a frame (a scrolling panel clips it, or the
  header holds a search field and selects) it becomes a plain strip across
  the box's top. A drawer's header is the Luna title bar with the
  red-orange close button. `.btn-min`/`.btn-max` on a title bar are the
  blue glossy caption squares, cropped from each variant's own
  `--luna-caption` strip, so every variant matches.
- **XL gutter art.** Bliss, washed almost out: a pale sky band and the
  rolling green hill within about 1.15:1 of the tan `--bg`. The
  full-strength Bliss behind the page gives way to `--bg` at XL. Still.
