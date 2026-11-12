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
2. **The ribbon.** The app bar is a Scenic Ribbon tab strip: a blue
   rounded application button at the left (with a small Windows flag),
   then tabs (nav items and menu-bar items alike); the selected tab is
   white, framed in `#b6bccc` and joined to a 24px ribbon band hung under
   the strip, white fading to `#e3ebf6` (box-shadows on the bar, so it
   takes no layout; main pads 24px more to clear it). A ribbon always has
   one tab open: with no current nav item the first is drawn open.
   Toolbars are ribbon groups: the white-to-`#eef3fa` band over a
   `#b6bccc` rule.
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
   `#7da2ce` frame and dark text, never a saturated fill. Check boxes and
   radios are the Win7 grey-gradient boxes with a dark-blue tick; the
   slider is the trackbar's thin grey groove with a grey-gloss thumb;
   disabled buttons are flat `#f4f4f4` with grey text; GO is a grey-gloss
   push button; ghost/tertiary buttons and resting filter chips are flat
   until the hot-track hover. The toggle switch is drawn from the
   trackbar: grey groove, grey-gloss thumb, pale-blue track when on.
   Alerts take the information-bar tints per tone (info `#f2f8fd`,
   warning `#ffffe1`, danger `#fdf0ee`, success `#f0f8ee`).
5. **Presence.** Every avatar is a Messenger display picture: a rounded
   square in a glossy green frame.

## Signature details

- The **aurora** (`--live-aurora`): pale-blue light pools with a white
  ribbon of light sweeping across the top, behind heroes, the XL gutters
  and any page without the shell. Inside the shell the work area is
  white, with only a faint wash of it under the ribbon (gone by 240px).
- Desktop windows have Windows 7 captions: a plain dark title (grey when
  inactive), grey-gloss minimise/maximise joined to the wide red close.
- Pane headers are the pale-blue gradient bars of Mail's "Quick views"
  and Gallery's folder pane.
- The status bar is Mail's pale strip ("1 message(s), 0 unread").
- The fifth chart series is a Live purple `#8b3fa8`, so it never doubles
  series 2's green.

## Layout

App bar → ribbon tab strip (no padding round the window; the app fills
it), white work area, pale status bar. No rail.

## v5 layout

Tiers: mobile ≤480px, tablet 481–900px, desktop 901–1800px, XL ≥1801px (the shell is capped at 1800px and centred, with gutter art beside it).

- **Phone (≤480) and tablet (481–900):** core puts the application button and the actions on the first line and the ribbon tabs on a scrolling second line. The application button is now a block with `max-width: max-content`, so its label ends in an ellipsis instead of being cut off, and it no longer stretches across the bar. The green h1 steps down a little on phones.
- **XL gutters (≥1801):** the aurora carries on beside the app window, as behind a Live sign-in screen: pale blue light down each side with two white ribbons of light sweeping through it. Still.

## Typography

`"Segoe UI", Selawik, Tahoma, sans-serif`. Segoe UI isn't freely
licensed, so it is used only where Windows has it. Everywhere else the
theme's bundled **Selawik** takes over. It is Microsoft's metric-compatible
Segoe UI stand-in (SIL OFL 1.1), vendored unmodified from its 1.01 release
as `assets/fonts/Selawik-Light.woff2` (300), `-Regular` (400) and
`-Semibold` (600–700), about 44 KiB in all, and recorded in
`assets/fonts/NOTICE.md`. The Light headings stay light on every
platform.

## Contrast honesty

- `--accent` `#1e6fbf` (links, active states) is 5.0:1 on white. Text on
  tints uses `--accent-text` `#1b63ab` and `--success-text` `#287028`,
  which clear 4.5:1 on the badge tints and code diff rows.
- `--muted` `#5b6878` is 5.6:1 on white.
- The application button's white label is checked against its own blue
  gradient (`--nav-brand-bg`), deepened from the reference's brighter
  `#4f8fd9` top so it clears 4.5:1 end to end.

## Icons

`icons.svg` redraws all 178 core-set icons as soft Wave 3/4 glyphs:

- 24 grid, heavy 2.2 line with round caps and round joins, true curves.
- Rects rounded (radius up to 3); nothing has a hard corner.
- Every closed body (envelope, page, folder, lens, bubble) is filled with
  a 30% `currentColor` tint under the outline: the "glass" of the real
  glossy icons, done without hard-coded colours. Small silhouettes (play,
  star, bookmark, pins) are solid.
- `currentColor` only, so the icons follow text, hover and selected states.
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
