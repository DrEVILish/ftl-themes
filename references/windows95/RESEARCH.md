# windows95 — visual reference notes

Outsider read: Battleship grey #c0c0c0 dialogs, 2px two-tone bevels, solid navy #000080 titlebar, teal #008080 desktop, dotted focus.

Capture targets: Desktop; dialog bevels; Explorer window.

Sources: Wikipedia Win95; Commons screenshots.

Use side-by-side with example.html; local captures are copyrighted originals — this file is the textual checklist.

Audit 2026-09-26: inspected 10 files; removed 1 (themed-my-phone-*.webp — modern Android launcher, not Win95 chrome); kept 9 (desktop/Notepad, My Computer/Paint/WordPad/Calc, German Explorer/Media Player, DLL icon grid, Win95 icon/cursor sheet, FreeCell, htg Start-menu shot, Internet icon close-up, splash screen). All 4 AVIFs verified decodable via ffmpeg.

## Dialog references

1. `dialog-run.jpg` — **Run** — 105px-ish dialog, title bar navy with white bold "Run" and
   `?` `×` caption buttons; icon + two-line prompt; "Open:" label with
   underlined accelerator and a combo box (sunken white field + raised
   drop arrow button); OK / Cancel / Browse... buttons right-aligned at
   the bottom, OK with the extra black default-button frame.
2. `dialog-save-as.png` — **Save As** — "Save in:" combo open as a drop-down tree (Desktop, My
   Computer, 3½ Floppy, drives, Network Neighborhood highlighted in navy
   with white text); toolbar icon buttons (up folder, new folder, list/
   details toggle); file list in a sunken white well; "File name:" and
   "Save as type:" rows; Save / Cancel stacked at the right.
3. `dialog-font.png` — **Font** — three list boxes with their own edit fields above (Font,
   Font style, Size), each with a classic scrollbar (raised arrow buttons,
   dithered track, raised thumb); "Effects" and "Sample" group boxes with
   etched frames and the caption breaking the line; checkboxes (sunken
   white square); Color and Script combos; OK/Cancel stacked right.
4. `dialog-welcome.png` — **Welcome to Windows 95** — large serif/sans wordmark, pale yellow
   tip panel with a bulb icon in a sunken frame, right column of equal-
   width buttons, checkbox at the bottom-left, Close button.
5. `start-menu-cascade.png` — **Start menu** — vertical grey "Windows95" banner on the left, items
   with 16/32px icons, cascading submenus (Programs → Accessories →
   Multimedia) with navy highlight and white text, ► arrows; taskbar with
   raised Start button and a sunken clock tray.

Patterns to carry over: accelerator underlines, `?` help caption button,
right-stacked dialog buttons, etched group boxes with caption-on-line,
combo boxes as sunken field + raised arrow button, navy selection with
white text, classic 3D scrollbars.


## Measured bevels (2026-10-09)

Sampled pixel by pixel with ImageMagick (`convert dialog-font.png -crop
1x1+X+Y +repage txt:-`) on `dialog-font.png`, a lossless 401×344 PNG at
native size, so the values are exact palette entries, not estimates.

| What | Where in `dialog-font.png` | Measured (outside → inside) | Theme token / rule |
|---|---|---|---|
| Title bar | x=2–395, y=3–20 | flat `#000080` across the full width (18px tall); no gradient | `--app-bar-bg`, `--modal-header-bg`, `--panel-header-bg` |
| Window frame | left edge y=150; bottom edge x=200 | top/left `#c0c0c0`, `#ffffff`; bottom/right `#000000`, `#808080`; caption starts after one more `#c0c0c0` row | `.panel`/`.card` 1px `#ffffff`/`#000000` border + `--panel-shadow: inset -1px -1px 0 #808080`; `.panel-header` 1px inside the frame |
| Push button (Cancel) | column x=340, y=74–96; row y=85 | top/left `#ffffff` then face; bottom/right `#808080` then `#000000` | `--btn-border-width: 1px`, `--btn-shadow: inset -1px -1px 0 #808080` |
| Default button (OK) | column x=340, y=48–70; row y=60 | an extra 1px `#000000` frame outside the push-button edge | `.btn-primary` `0 0 0 1px #000000` |
| Sunken field (Font box) | column x=80, y=48–70; row y=55 | top/left `#808080`, `#000000`; bottom/right `#ffffff`, `#c0c0c0` | `--input-border-width: 1px`, `--input-shadow`, and the `.app-main` well |
| Checkbox | row y=208, x=23–35 | the same four sunken lines round a white square | core checkbox (unchanged) |
| Group box (Effects) | row y=230, x=14–15 | etched: `#808080` then `#ffffff` | nested `.panel-header` rule (unchanged) |

What this changed: Windows 95's "3D light" system colour was the face
colour `#c0c0c0`, so a 95 bevel has no `#dfdfdf` inner line; the theme had
drawn 98's 3px edge (2px border plus a `#dfdfdf` line). Buttons, inputs,
panels, cards, toasts, keys and the content well now draw the measured 2px
edge.

Derived, not measured (no capture shows them): the pressed button (the
resting edge mirrored: `#000000`, then `#808080` on the top-left), and the
default button keeping a navy fill with white text (README core value 4),
where the real OK button is grey with the black frame.
