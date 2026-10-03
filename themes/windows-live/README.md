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
   then tabs; the selected tab is white, framed in `#b6bccc` and joined
   to the ribbon below.
3. **Light type.** Segoe UI Light for headings — dialog/page titles in
   Live green `#2b7a2b` ("Add your email accounts"), section headings in
   dark Live blue `#1e395b`.
4. **Windows 7 controls.** Grey-gloss push buttons with the pale-blue
   hover; the default button wears the cyan glow; Explorer's pale-blue
   selection in a `#99d1ff` frame; Win7 tooltips; glossy green progress.
5. **Presence.** Every avatar is a Messenger display picture: a rounded
   square in a glossy green frame.

## Signature details

- The **aurora** (`--live-aurora`): pale-blue light pools with a white
  ribbon of light sweeping across the top, behind the whole app and any
  page without the shell.
- Pane headers are the pale-blue gradient bars of Mail's "Quick views"
  and Gallery's folder pane.
- The status bar is Mail's pale strip ("1 message(s), 0 unread").

## Layout

App bar → ribbon tab strip (no padding round the window; the app fills
it), white panes on the aurora, pale status bar. No rail.

## v5 layout

Tiers: mobile ≤480px, tablet 481–900px, desktop 901–1800px, XL ≥1801px (the shell is capped at 1800px and centred, with gutter art beside it).

- **Phone (≤480) and tablet (481–900):** core puts the application button and the actions on the first line and the ribbon tabs on a scrolling second line. The application button is now a block with `max-width: max-content`, so its label ends in an ellipsis instead of being cut off, and it no longer stretches across the bar. The green h1 steps down a little on phones.
- **XL gutters (≥1801):** the aurora carries on beside the app window, as behind a Live sign-in screen: pale blue light down each side with two white ribbons of light sweeping through it. Still.

## Typography

`"Segoe UI", "Segoe UI Web", Tahoma, sans-serif` — **system fonts, not
vendored** (Segoe UI isn't freely licensed); off Windows, Tahoma or the
platform sans renders, and Segoe UI Light's weight-300 headings fall
back to whatever light weight is available.

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
the ribbon tab strip and the aurora fills the window.
