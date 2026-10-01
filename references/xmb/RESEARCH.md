# xmb — visual reference notes

Outsider read: Sony XMB (PSX 2003/PSP/PS3): dark translucent backdrop over blue wave, horizontal category icons crossed by vertical sub-list, white glow + scale on selection.

Capture targets: Home menu cross; wave backdrop; sub-list drop.

Sources: PlayStation PS3 manual; PS3 Dev Wiki; RetroArch XMB docs.

Use side-by-side with example.html; local captures are copyrighted originals — this file is the textual checklist.

Canonical UI (v2, hunted): xmb-ps3-screenshot.jpg (fair-use PS3 capture) + xmb-retroarch-{main-menu,thumbnails,theme-alt} (open-source RetroArch recreation, docs.libretro.com) showing the primary row + sub-column cross, wave backdrop, glow selection. Hardware photos removed as non-UI.

Audit 2026-09-26: kept xmb-ps3-screenshot.jpg + xmb-retroarch-main-menu.jpg (both clean XMB cross UI). Removed theme-alt (James Pond 3 box art = cartoon characters) and thumbnails (Cybermorph box art = alien face) per zero-people/characters rule. GAP: no people-free game-thumbnail example left — main-menu covers the cross + wave language alone.

Overlays, 2026-10-01 (modal readability review). Added four captures from Sony's own PS3 online user's guide (manuals.playstation.net/document/en/ps3/current/imgs/, retrieved via the Wayback Machine since the live manual now 404s). Each is the manual's screen plus a magnified callout; the black rounded callout frame is the manual's, not the UI's.
- `modalDialog.jpg` (hddinstall001.jpg) — a Yes/No system confirm: the XMB is dimmed almost to black, the dialog is white text on a dark band with thin white rules, choices as plain text with the focused one bright. Backs the near-opaque dark --modal-bg, the heavy --overlay-bg dim and the light --modal-border.
- `modalDialog-form.jpg` (savepw001.jpg) — the PSN sign-in dialog: labels over dark recessed fields, checkboxes, grey pill-ish buttons on the same dimmed backdrop. Backs form inputs inside a modal.
- `modalDialog-optionsMenu.jpg` (xmb002.jpg) — the (triangle) Options menu sliding in from the right: a dark translucent column with a thin light edge and grey/white item text. Backs dropdown/context-menu/popover (--dropdown-bg).
- `toast.jpg` (notification001.jpg) — the top-right "XXXXX is now online" notification: a small dark rounded bubble with an icon and white text over the XMB. Backs --toast-bg.
Still no reference for: tooltip, the "O Enter / X Back" button-hint footer as a standalone capture (it appears only tiny in the uncropped half of the manual screens), a native PS3 error dialog.
