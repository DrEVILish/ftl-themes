# teletext — visual reference notes

Outsider read: BBC Ceefax 1974-2012: black bg, 40x24 blocky text, 7 colors (red/green/yellow/blue/magenta/cyan/white), double-height headlines, Fastext red/green/yellow/blue bottom bar. Green/cyan/yellow most readable.

Capture targets: Ceefax frame; Fastext close-up; double-height headline.

Sources: BBC Archive; Wikipedia Ceefax/Teletext; mb21 Teletext Museum.

Use side-by-side with example.html; local captures are copyrighted originals — this file is the textual checklist.

Audit 2026-09-26: all 3 kept — ARTE page 100 (blocky double-height + Fastext bar), Ceefax football index (cyan index-list language), teletexnews 300 (newsflash frame). Pure text screens, zero people, on-target.

## Display constraints (designed for SD CRT televisions)

- A fixed grid of **40 columns × 25 rows** (row 0 is the header), each cell
  one character from the Mullard **SAA5050** character generator: blocky,
  stepped glyphs, no anti-aliasing, no proportional spacing.
- **Eight colours only:** black, red, green, yellow, blue, magenta, cyan,
  white. No tints, no gradients. Keep the boxy, blocky styling.
- **Double height** rows for headlines; block-mosaic (sextant) graphics
  for logos and banners (the BBC / CEEFAX / FOOTBALL wordmarks are built
  from mosaic cells, often with a 1-cell shadow).
- Header row: `P100  CEEFAX 1 100 Wed 22 Dec 16:24/41` — page number,
  service, date in white, clock in yellow.
- Index pages: yellow/white labels with page numbers right-aligned in
  columns (`NEWS HEADLINES 101`). Listings: yellow times, white titles,
  cyan descriptions, magenta flags.
- Section banners are a coloured background block (blue) with a mosaic
  title in a contrasting colour; tables use coloured rows and blank rows
  instead of lines (a single coloured rule at most).
- Bottom row is **Fastext**: four labels in red, green, yellow, cyan,
  one per remote-control key; often a blue strapline row above it.

## Fonts

- **Bedstead** (Ben Harris, CC0) — outline recreation of the SAA5050,
  including the teletext mosaic characters; vendored as
  `assets/fonts/Bedstead.woff2`. This is the matching font.
- edit.tf (https://github.com/rawles/edit.tf) uses its own
  **TeletextKit** font — GPLv3, so not vendorable into this library.
- teletextart.co.uk (https://teletextart.co.uk/make-teletext-art) points
  to edit.tf / zxnet-style editors for drawing mosaic art.

## Reference images (described; files to be added to this folder)

1. CEEFAX 1 P100 index — BBC block logo, CEEFAX mosaic wordmark on blue,
   two-column yellow index with white page numbers, blue strapline, Fastext.
2. P324 Football — BBC FOOTBALL mosaic banner, league table with cyan
   highlight rows and red separator rules.
3. BBC1 P696 listings — cyan BBC1 mosaic logo, yellow times, white
   titles, cyan descriptions, magenta "N".
4. P299 Newsreel intro — yellow mosaic CEEFAX blocks with drop shadow on
   a blue frame, black inset panel with double-height yellow text.
5. "Football Nostalgia" print — green-on-blue and black-on-white mosaic
   wordmarks, centred multicolour paragraphs.

