# Windows Live

> Windows Live Essentials 2011 — white ribbon apps on a pale-blue aurora.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

The Windows Live Essentials apps — Mail, Messenger, Photo Gallery,
Movie Maker — as they shipped for Windows 7 (Wave 3/4, 2009–2011). A
calm, white, *application* look rather than an OS shell: the Windows 7
controls those apps used, the Scenic Ribbon's tab strip, and the Live
brand moments — the aurora swooshes behind sign-in and splash screens,
Segoe UI Light headings, and Messenger's glossy green display-picture
frame.

## Core values

1. **The app is white; colour is in the chrome.** Panes are white with a
   `#c5d2df` frame; the colour lives in the blue application button, the
   ribbon tabs, the aurora and the presence frames.
2. **The ribbon.** The app bar is a Scenic Ribbon tab strip, flat pale
   blue (`#e4edf8` to `#dfe9f5`), with a blue application button at the
   left (with a small Windows flag) seated in the strip like Mail's File
   tab: same height as the tabs, rounded on top, square at the foot and
   down over the strip's rule,
   then tabs (nav items and menu-bar items alike) with 13px (9pt) labels
   and tight padding, still --tap-min tall; the selected tab is
   white to `#f5faff`, framed in `#9faec2` and joined to a 24px ribbon
   body hung under the strip, `#f5faff` to `#e3ebf6` over the ribbon's
   `#9faec2` rule (one `--app-main-bg` background at the top of main,
   which pads 24px more to clear it, so it takes no layout and never
   covers a menu; no painted command groups, the page's toolbars are the
   commands). A ribbon always has
   one tab open: with no current nav item the first is drawn open.
   Toolbars are ribbon groups: the white-to-`#e3ebf6` band over a
   `#9faec2` rule.
3. **Light type.** Segoe UI Light (bundled Selawik Light off Windows) for headings — dialog/page titles in
   Live green `#2b7a2b` ("Add your email accounts"), section headings in
   dark Live blue `#1e395b`.
4. **Windows 7 controls.** Grey-gloss push buttons with the pale-blue
   hover; the default button is the same gloss faintly tinted blue in a
   `#3c7fb1` frame with the cyan inner glow, turning pale blue only on
   hover; Explorer's pale-blue selection in a `#99d1ff` frame (rows,
   tree, folder pane, desktop and file-view icons; no accent bar); Win7 tooltips; tall glossy green
   progress. Every pressed/selected control (toggle buttons, segmented,
   pagination, filter chips) uses that pale-blue selection with a
   `#7da2ce` frame and dark text, never a saturated fill. Delete and
   Confirm (`.btn-danger`, `.btn-success`, a danger toggle) are the same
   grey gloss faintly tinted red or green, the tone only in the label.
   A plain `.nav` outside the ribbon, the featured list card and the
   navigation patterns' current link take the same pale-blue selection
   in a `#99d1ff` frame; a bare nav brand is regular-weight dark blue. Check boxes and
   radios are the Win7 grey-gradient boxes with a dark-blue tick; the
   slider is the trackbar's thin grey groove with a grey-gloss thumb;
   disabled buttons are flat `#f4f4f4` with grey text; GO is a grey-gloss
   push button; ghost/tertiary buttons and resting filter chips are flat
   until the hot-track hover. The toggle switch is drawn from the
   trackbar: grey groove, grey-gloss thumb, pale-blue track when on.
   Alerts take the information-bar tints per tone (info `#f2f8fd`,
   warning `#ffffe1`, danger `#fdf0ee`, success `#f0f8ee`).
5. **Presence.** Every avatar is a Messenger display picture: an 8px
   rounded square, a pale `#e8f6df` ring round the picture, then a glossy
   green bezel (lime `#9be27a` across the top with a white highlight on
   its inner edge, darker `#3f9a22` below, dark-green edge) whose thickness follows the picture
   (3px small, 4px default, 6px large), drawn with solid shadows only.

## Signature details

- The **aurora** (`--live-aurora`): pale-blue light pools with a white
  ribbon of light sweeping across the top, behind heroes, the XL gutters
  and any page without the shell, and as the desktop page's wallpaper.
  Inside the shell it is a band under the ribbon lip (a white ribbon of
  light over pale blue, gone by ~210px; phones keep only the plain wash, never darker than about `#dceaf8`
  so muted text keeps 4.5:1). A sign-in card (one holding a password or
  code field) carries it across its head, Mail's "Add your email
  accounts" dialog, with a green Light title.
- Menus are Live 2011's: white with a pale `#f1f4f8` icon gutter, labels
  past it, items hot-tracked in the framed pale-blue selection. Dropdown
  lists are plain white with the same hot-track.
- Labels are sentence case: stat labels, field-group titles and footer
  headings drop core's tracked capitals. Table headers are Explorer's:
  regular weight on a white-to-`#f1f4f8` header with `#e3e8ef` column
  separators.
- Windows (desktop windows and any modal with caption buttons) wear the
  Windows 7 Aero frame: a 7px pale-blue glass border (`#d6e5f6` to
  `#abc3e1`, paler and greyer `#eef2f7` to `#d6dfea` when inactive) in a
  `#6a7f99` outer edge with a white inner highlight, 6px corners, the
  caption on the glass and the white client area inset in a `#8ea2bb`
  rule (background layers only, no extra layout). Captions are Windows
  7's: a plain dark title with a soft white glow (grey when inactive),
  caption buttons hanging from the frame's top edge,
  blue-grey glass minimise/maximise (`#dbe6f3` to `#c3d4e7`, white top
  highlight, slate frame) joined to each other and to the wide glossy
  red close, the group's outer bottom corners rounded 4px. The glyphs are
  drawn: a thick white bar and a 2px white box, each in a dark edge, and
  a bold white X outlined in dark red.
- Text-link actions (`a.btn-clear`: "Forgot password?", "Back to sign
  in") are Live's blue hyperlinks `#1e6fbf`, underlined on hover.
- A dirty cell in a selected row keeps the Explorer selection, marked
  only by its amber leading bar.
- Pane headers are the pale-blue gradient bars of Mail's "Quick views"
  and Gallery's folder pane, titled in regular-weight Live blue `#1e5aa0`.
  A folder rail beside a list (`.master-detail > .nav-rail`) is a framed
  `#c5d2df` pane like its neighbours, headed on desktop by that bar
  carrying the nav's own label (decorative, empty alt text).
- Full-colour icons where Live had them: in folder panes, trees, lists,
  toolbars, toolbar icon buttons and desktop/file-view icons, folders are
  yellow `#c8901a`, trash red `#d03a2a`, mail glyphs and the globe blue
  `#2f6fc2`, settings grey `#5b6878`, the star gold `#e0a800` and
  people green `#3a8e3a` (CSS `color`, the sprite stays `currentColor`).
- The status bar is Mail's pale strip ("1 message(s), 0 unread").
- The fifth chart series is a Live purple `#8b3fa8`, so it never doubles
  series 2's green.

## Layout

App bar → ribbon tab strip (no padding round the window; the app fills
it), white work area, pale status bar. No rail.

## v5 layout

Tiers: mobile ≤480px, tablet 481–900px, desktop 901–1800px, XL ≥1801px (the shell is capped at 1800px and centred, with gutter art beside it).

- **Phone (≤480) and tablet (481–900):** core puts the application button and the actions on the first line and the ribbon tabs on a scrolling second line. The application button becomes Photo Gallery's square blue menu button: the flag alone (the label stays in the accessibility tree). The green h1 steps down a little on phones.
- **XL gutters (≥1801):** the aurora carries on beside the app window, as behind a Live sign-in screen: pale blue light down each side with two white ribbons of light sweeping through it. Still.

## Typography

`"Segoe UI", Selawik, Tahoma, sans-serif`. Segoe UI isn't freely
licensed, so it is used only where Windows has it. Everywhere else the
theme's bundled **Selawik** takes over. It is Microsoft's metric-compatible
Segoe UI stand-in (SIL OFL 1.1), vendored unmodified from its 1.01 release
as `assets/fonts/Selawik-Light.woff2` (300), `-Regular` (400) and
`-Semibold` (600–700), about 44 KiB in all, and recorded in
`assets/fonts/NOTICE.md`. The Light headings stay light on every
platform. Code uses `Consolas, "Lucida Console"`, then Liberation Mono
(metric-compatible with Courier New) and DejaVu Sans Mono off Windows.
Body copy is 15px, a step under the browser default, so text
and tables sit close to the 9pt controls as in the Essentials apps.

## Contrast honesty

- `--accent` `#1e6fbf` (links, active states) is 5.0:1 on white. Text on
  tints uses `--accent-text` `#1b63ab` and `--success-text` `#287028`,
  which clear 4.5:1 on the badge tints and code diff rows.
- `--muted` `#5b6878` is 5.6:1 on white.
- The application button's white label is checked against its own blue
  gradient (`--nav-brand-bg`, `#3574c7` to `#1d5cb0` split at 50%),
  deeper than the reference's brighter `#4f8fd9` top so it clears 4.5:1
  end to end; the gloss comes from inset white highlights and a dark
  1px text shadow instead.

## Icons

`icons.svg` redraws all 178 core-set icons as soft Wave 3/4 glyphs:

- 24 grid, heavy 2.2 line with round caps and round joins, true curves.
- Rects rounded (radius up to 3); nothing has a hard corner.
- Every closed body (envelope, page, folder, lens, bubble) is filled with
  a 30% `currentColor` tint under the outline: the "glass" of the real
  glossy icons, done without hard-coded colours. Small silhouettes (play,
  star, bookmark, pins) are solid.
- `currentColor` only, so the icons follow text, hover and selected states.
  The theme CSS colours a few ids in panes and toolbars (see Signature
  details).
  Ids outside the core set fall back to the generic outline set.

## Reference status

`references/windows-live/` — 14 captures: Mail 2007/2009 splash, Mail
2011 inbox and add-account dialog, Messenger 2011 sign-in, contact list
and conversation, Photo Gallery ribbon, Movie Maker 2009 and 2011
(ribbon, menu, trim), the Live Gallery web page and the logo. Notes in
`RESEARCH.md` there.

## Adoption

At **L0** it recolours; at **L1** (the `.app` shell) the app bar becomes
the ribbon tab strip over a white work area.
