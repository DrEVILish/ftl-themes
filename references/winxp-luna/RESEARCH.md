# winxp-luna — visual reference notes

Outsider read: Luna Blue glossy royal-blue titlebar w/ white highlight, tan content, Tahoma, green Start pill, red-orange Close button.

Capture targets: Start menu; Bliss; window chrome.

Sources: Wikipedia XP visual styles.

Use side-by-side with example.html; local captures are copyrighted originals — this file is the textual checklist.

Audit 2026-09-26: inspected 7 files; removed 2 (xvksk31u5p391.jpg — fake Win10-skin meme with user avatar photo + non-XP apps; sddefault.jpg — cursor/Clippy-mascot collage on black, not Luna chrome); kept 5 (Luna Start-button crop, March Mountain XP icon promo, tall XP icon grid, Luna Sample dialog, Bliss desktop + real Start menu).

## Visual styles in the 2026-10 captures

- `start-buttons-all-styles.webp` — the Start button of every style
  side by side: Luna Blue (green), Silver, Olive Green, Royale, Embedded
  (blue), Zune (orange on black), Royale Noir (green on black), Classic.
- **Royale** (`royale/`): brighter glassy blue title bar with a
  strong upper highlight; Start menu with a deep navy header, white left
  column, blue-lavender right column; Display Properties dialog.
- **Royale Noir** (`royale-noir/`): glossy black title bars with white
  text, dark caption buttons with a **red** close, black taskbar, green
  Start, black-headed Start menu with a dark-grey right column.
- **Zune** (`zune/`): black/charcoal glass title bars and taskbar, an
  **orange** Start button, dark Start menu; the free theme Microsoft
  released with the Zune player in 2006.
- **Embedded** (`embedded/`): deeper, flatter steel blue; **blue** Start
  button; Start menu all blue with a lighter right column; "Windows
  Embedded Standard" wallpaper of pale tiles on blue.
- `notification-balloon.png` — the cream (`#ffffe1`) balloon tooltip with
  rounded corners, tail to the tray icon, info icon, bold title, close ×.
- `taskbar-properties-dialog.jpg`, `taskbar-tray-links.jpg` — taskbar
  toolbars, tray chevron, clock area.


## Icons and wallpapers (added 2026-10-07)

- `icons-original/` — 107 icons from the shipping Windows XP set (Explorer,
  My Computer, Recycle Bin, drives, Control Panel applets, IE, WMP, MSN):
  the 48px look to compare a theme's icon overrides against. Includes some
  re-drawn "blur" variants (Cyrillic file names, from a Russian pack).
- `icons-modern/` — 592 PNGs: a modern high-resolution redraw of the XP
  set (named by function, e.g. `Accessibility.png`), useful for large
  desktop icons where the originals pixelate.
- `wallpapers/` — the shipped XP wallpapers: Bliss (full 4800px original
  by Charles O'Rear), New Bliss, Autumn, Azul, Ascent, Full Moon Dunes,
  Sunset, Yellow Tulips and the Professional edition wallpaper.
  `embedded/Windows XP - Embedded.png` is the Embedded edition's.

Audit 2026-10-07: all new icons and wallpapers inspected. No people; the
generic user pictograms and the Search companion's wizard and dog are UI
glyphs and were kept.

## External evidence (measured 2026-10-08, not stored here)

These genuine, lossless Windows XP captures are non-free, so they are cited,
not copied. Each one is on English Wikipedia under `File:<name>`. Values were read pixel by
pixel. The 640x480 desktops are downscaled from 1024x768: their taskbar is
19px against XP's 30px, so they give flat colours, not sizes or edges.

| Capture | Size | What it settled |
|---|---|---|
| `Windows_XP_Start_menu.png` | 282x354, 1:1 (aliased Tahoma, 5 colours in a text run) | Start menu: 141px columns, programs every 30px, places every 22px, 48px header (`#0c5fcb` to `#4792ec`), 30px footer |
| `Windows_XP_Luna.png` | 640x480 | Inactive caption (`#9bb6ea` lip, `#7a96df`, `#82a9e9`), task pane (`#7ba2e7` to `#6375d6`, groups `#d6dff7`, headers white to `#c6d3f7`), inactive caption buttons at ~60% |
| `Windows_XP_Olive_Green.png`, `_Silver.png` | 640x480 | Both schemes' taskbar, tray, Start menu, inactive caption, task pane |
| `Windows_XP_Royale.png`, `_Royale_Noir.png`, `_Zune.png`, `_Embedded.png` | 640x480 | Each scheme's active caption, taskbar, task buttons, tray, dark Start menu columns, task pane header bars |
| `Windows_XP_task_grouping_(Luna).png` | 800x24 | Task buttons: flat `#3980f4` between a lighter top band and a darker bottom edge |
| `Windows_XP_Shutdown.png` | 398x198 | Turn Off dialog: `#003399` bands, `#d5e4f8` rule, body `#94b1f4` centre to `#5a7dde` edges |
| `Windows_XP_Desktop_Cleanup_Wizard.png` | 358x279 | Push buttons (white to beige face, dark blue border) and the default button's inner blue ring |
| `Windows_XP_scaling_at_200%.png` | 2736x1624, lossless | Explorer content flush with the frame; section heading bold black over a 1px rule from `#4197ff` fading to white; trackbar thumb (`#f3f3ef` face, `#778892` edge, green ends) |

Inbox captures used: `DisplaySettings.png` (lossless 640x480: taskbar, Start
pill, tray), `images-1.jpg` (genuine logon), `01AppearanceTab.png` (Silver
active caption at 1:1). `104660324-…png` is a web recreation, not XP.

Derived, not measured: Olive Green's active caption (follows its Start menu
header, as Silver's does) and the inactive captions of Royale, Royale Noir,
Zune and Embedded (the active caption desaturated). No capture shows them.
