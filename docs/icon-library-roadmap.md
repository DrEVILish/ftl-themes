# Icon library roadmap

## Current state (as of this doc)

- `assets/icons/icons.svg` — **1,020 generic icons**, stroke-based outline
  style: 24x24 `viewBox`, `stroke="currentColor"`, `fill="none"` by
  default, sized/weighted entirely through `--ftl-icon-fill` and
  `--ftl-icon-stroke-width` (`core/ftl-core.css`, `.ftl-icon`). No per-icon
  color or stroke-width is ever baked into a symbol — that's what lets one
  sprite reskin across 22 very different themes with zero per-theme icon
  variants required. The original 100 are in-house line drawings; the
  other 920 are bulk-vendored, unmodified-artwork icons from **Tabler
  Icons** (MIT license, v3.48.0) — see `assets/icons/NOTICE.md` for the
  full attribution, exact commit/version, and exactly what was
  mechanically normalized (symbol wrapper, stripped presentation
  attributes) versus left untouched (all path data).
- Per-theme overrides exist for **6 of 22 themes** (`windows95`,
  `teletext`, `matrix`, `winxp-luna`, `lcars`, `nokia-3310`), each
  redefining **6 icon ids** in `themes/<slug>/icons.svg`.
- `scripts/build_icons.py` merges generic + override by id into
  `dist/icons/<slug>.svg` per theme, plus `dist/icons/generic.svg` as the
  fallback sprite. `scripts/check.py` validates every override only
  redefines an id the generic set actually has, and that every built
  sprite is well-formed XML.

## The target

- **2,000+ generic icons** — broad enough to cover file types, hardware,
  communication, commerce, weather, maps, accessibility, data
  visualization, security, dev tooling, directional/arrows, status/emoji
  faces, and seasonal/misc, without a consuming app ever needing to draw
  its own icon for a common concept.
- **100+ unique icons per theme, for all 22 themes** — enough that a
  theme's signature visual language (Windows 95's chunky pixel bevels,
  LCARS' swept panel shapes, Nokia 3310's 1-bit dot-matrix look, etc.)
  shows up not just in 5-6 flagship icons but across most of the icons an
  app actually uses day to day.

This is a **large, multi-year content-production effort** (2,000 generic
icons alone is a ~20x expansion from today's 100; 100 icons x 22 themes
is 2,200 more themed drawings on top of that). It is explicitly **not**
attempted in one pass. What follows is the phased plan.

## Phased plan

### Phase 1 — Core baseline (DONE, this change)

55 -> 100 generic icons. Categories added: media/playback transport
(volume, shuffle, repeat, skip-forward/back, music-note, album, video,
headphones), hardware/connectivity (power, wifi, bluetooth, usb,
hard-drive, terminal, server, battery), security (shield, key,
fingerprint), navigation (globe, map-pin, compass, layers), layout/view
(layout, sidebar, columns, maximize, minimize, zoom-in, zoom-out),
data/analytics (activity, trending-up, bar-chart, pie-chart, table), and
general utility (bookmark, pin, eye, eye-off, code, palette, at-sign,
hash). Selection was informed by grepping the sibling consumer apps
(`cutepi`, `playlist-lab`, `pi9696`) for the UI concepts they actually
reach for (transport controls, remote/hardware glyphs, dashboard chrome),
not picked abstractly.

### Phase 2 — Generic set: 100 -> 2,000

**Status: 100 -> 1,020, DONE for this session's 1,000-icon target.**
Rather than hand-drawing ~15 batches of ~200 originals, the project
owner opted to bulk-vendor a large batch verbatim from Tabler Icons
(MIT-licensed, confirmed safe for bulk redistribution in
`docs/icon-license-research.md`) — see `assets/icons/NOTICE.md` for the
full sourcing, license text, exact version/commit, and normalization
details. 917 icons were added in one pass, plus 3 follow-ups from the
same Tabler source (`qr-code`, `hourglass`, `timer`) requested by a
consuming app, bringing the
generic set from 100 to 1,020. The category list below remains the
reference for what got prioritized in that pass and what a future
hand-drawn or further-vendored pass should still fill in (the vendored
batch covers broad ground per category but is not exhaustive — Tabler's
full outline set has ~5,900 icons, of which only a curated ~900 were
pulled in this batch).

The remaining path toward the longer-term 2,000-icon target is: either
vendor a second batch from Tabler (or a second permissive source, e.g.
Lucide, for icons Tabler doesn't have a good match for) using the same
process, or fill gaps with original hand-drawn icons where a needed
concept doesn't exist in any permissive source. Each batch remains
additive-only and independently `check.py`-verified, per the original
plan below.

Original proposed batch order, roughly most- to least-broadly-needed
(now used as the category checklist for the vendored batch above, not
as a sequence of separate hand-drawn PRs):

1. File types & documents (pdf, doc, spreadsheet, archive/zip, code file,
   font file, font, config, log, database file, ...)
2. Media & transport controls, extended (equalizer, waveform, mic,
   mic-off, cast, airplay-style output-select, closed-caption, loop-one,
   crossfade, ...)
3. Hardware & devices (router, modem, nas, gpu, cpu, ram, keyboard,
   mouse, gamepad, remote-control, smartwatch, tablet, printer-3d, ...)
4. Communication (chat bubble variants, send, reply, forward, video-call,
   voicemail, contacts, address-book, ...)
5. Commerce (credit-card, receipt, invoice, wallet, price-tag variants,
   discount, refund, storefront, ...)
6. Weather (sun, moon, rain, snow, storm, wind, fog, rainbow, uv-index, ...)
7. Maps & location (route, waypoint, geofence, parking, traffic-light,
   train, bus, plane, ship, walking, cycling, ...)
8. Accessibility (wheelchair, closed-caption, sign-language, high-contrast,
   screen-reader, braille, ...)
9. Generic placeholder "brand-shaped" social icons (deliberately generic
   share/network/community glyphs — never a real trademarked logo; see
   licensing policy below)
10. Data & charts, extended (scatter-plot, funnel, gauge-chart, heatmap,
    candlestick, treemap, sankey-ish, ...)
11. Security, extended (2fa, biometric-face, incognito, firewall, vpn,
    audit-log, ...)
12. Dev/code, extended (git-branch, git-commit, pull-request, bug,
    package, api, webhook, terminal-window, ...)
13. Arrows & directional, extended (all 8 compass directions x
    single/double, corner arrows, swap, sync-arrows, ...)
14. Status/emoji-adjacent faces (happy, sad, neutral, love, thinking,
    surprised — simple line-drawn expressions, not copies of any emoji
    vendor's art)
15. Seasonal & misc (snowflake, pumpkin, firework, balloon, cake — kept
    small; a theme's own overrides are the better place for a lot of
    seasonal flavor)

Each batch is additive-only to `assets/icons/icons.svg`, never renames or
removes an existing id (per-theme overrides and consumer apps' `<use
href="...#icon-name">` references must never break), and gets verified
with `scripts/check.py` before merging.

### Phase 3 — Per-theme expansion: 6 -> 22 themes, ~10-15 -> 100 icons each

For each theme, the plan is: identify the theme's 10-15 most-recognizable
real-world icon categories (the ones its target aesthetic is actually
"about"), draw those first, and let the rest continue falling back to the
generic set indefinitely — that fallback is not a stopgap, it is the
permanent, correct behavior for icons a theme has no signature take on.

Starter category lists per theme (illustrative, refine per-theme when the
work starts):

- **windows95** — folder (manila), file, computer/my-computer, trash
  (recycle bin), floppy-disk (save), control-panel, wallpaper, taskbar,
  start-menu, notepad, calculator, paint
- **winxp-luna** — folder (blue tabbed), file, my-computer, recycle-bin,
  control-panel, network-places, media-player, messenger, search-dog,
  start-orb
- **win7-aero** — folder (glassy), file, computer, recycle-bin,
  control-panel, taskbar, gadget, aero-peek, jump-list, action-center
- **teletext** — page-number, subtitle/caption, broadcast, antenna,
  channel, index-page, ceefax-style block-character glyphs, tv-set
- **matrix** — terminal, binary/code-rain, eye, phone-booth, floppy-disk,
  server-room, hacker-hood, red-pill/blue-pill (abstracted, not literal
  film references), circuit
- **lcars** — sensor, comm-badge, warp, shield, phaser, transporter,
  starfleet-delta (abstracted geometric badge, not the literal insignia),
  console-panel, stardate, viewscreen
- **nokia-3310** — signal-bars, battery (1-bit), sms, snake-game,
  antenna, keypad, ringtone, infrared, phonebook, alarm-clock
- **winamp-classic** — equalizer, playlist, visualizer, skin, shade-mode,
  milkdrop-ish plugin, media-library, crossfade, winamp-llama (abstracted
  mascot silhouette, not the literal artwork)
- **wmp11** — now-playing, library, rip-cd, burn-cd, sync-device,
  visualization, media-guide, playlist
- **xbmc** — media-center-grid, now-playing-fullscreen, addon,
  skin-select, weather-widget, remote-control, library-scan
- **xmb** — cross-media-bar-column, game, photo, music, video, network,
  settings-wheel, memory-card
- **msdos** — blinking-cursor, floppy-disk, directory-tree, batch-file,
  command-prompt, boot-screen, autoexec
- **aqua** — dock, genie-effect, brushed-metal-panel, aqua-button,
  finder, trash (translucent), widget
- **lego-classic** — brick, minifig, baseplate, instruction-booklet,
  stud, set-box
- **hot-wheels** — track-piece, checkered-flag, speedometer, garage,
  loop-track, car-silhouette
- **barbie** — dress, shoe, house, convertible-car, bow, sparkle
- **alienware** — spaceship, alien-head (generic, not any franchise's),
  rgb-lighting, cooling-fan, overclock-gauge
- **cyber-goth** — skull (line-art), chain, spike, gas-mask, neon-cross
- **death-star** — trench-run-line-art (abstracted), superlaser-dish,
  hangar-bay, tie-fighter-silhouette (kept generic/abstracted — see
  licensing note), control-room
- **bloomberg** — ticker, candlestick-chart, terminal-key, market-bell,
  order-book, watchlist
- **imac-g3** — bondi-blue-shell (abstracted rounded-corner motif),
  handle, tray-cd, iMac-silhouette
- **vaporwave** — palm-tree, grid-horizon, statue-bust, cassette,
  vhs-tape, sunset

Some of these category names lean toward specific media/IP aesthetics
(Star Trek for lcars, Star Wars for death-star, Alienware's own branding
for alienware). Per the licensing policy below, these get drawn as
**generic, abstracted shapes that evoke the aesthetic without
reproducing any specific copyrighted design** (e.g. lcars' "starfleet
delta" becomes an abstract rounded-triangle badge, not the actual
insignia; death-star's icons stay silhouette/line-art riffs on general
sci-fi shapes, not frame-accurate reproductions of Lucasfilm artwork).
This is consistent with how the existing 6 theme overrides are already
drawn — reference `themes/lcars/icons.svg` and `themes/matrix/icons.svg`
for the existing precedent of "evokes the theme, infringes on nothing."

Work order suggestion: do the 6 themes that already have partial
overrides first (finish them to 100 before starting a 7th theme from
zero), since finishing an in-progress theme is lower-risk than starting a
new one, then proceed roughly by how popular/high-traffic the theme is
in consuming apps.

## Sourcing & licensing policy

- **All icons in this library are original line drawings**, authored in
  house, in a simple geometric outline style (24x24 grid, ~2px stroke,
  rounded caps/joins, `currentColor`, no fill by default). This visual
  convention — minimal stroke-based outline icons on a 24x24 grid — is
  shared across many icon families (Bootstrap Icons, Feather, Lucide,
  Tabler, etc.) and is a general style, not a protectable expression;
  matching that convention is not the same as copying anyone's specific
  artwork, and no glyph in this library is traced or derived from another
  icon set's actual path data.
- **Bootstrap Icons (MIT license)** was evaluated as a possible vendor-in
  source, since the project owner already uses it elsewhere (`cutepi`
  vendors `bootstrap-icons@1.11.3.css` + the compiled webfont). That
  vendored copy is a **compiled font + CSS**, not raw SVG source — there
  is no accessible SVG path data to extract from it in this environment.
  **No Bootstrap Icons artwork was copied into this library.** If the
  project owner later supplies the actual Bootstrap Icons SVG source
  files (e.g. from the upstream `icons/` directory of the
  twbs/bootstrap-icons release), those can be vendored verbatim under
  their MIT license and swapped in for the equivalent hand-drawn originals
  — MIT permits that; it would need attribution retained per the
  license's terms (a `NOTICE` or a comment block, consistent with how
  `cutepi` already credits it).
- **Font Awesome is not a source for this library.** Its glyphs are CC BY
  4.0 (Free tier), which requires attribution — workable for a single
  app, but a bad fit for 2,000+ icons reused across 22 themes and
  N consuming apps, where tracking and rendering attribution correctly at
  that scale is real ongoing overhead. No Font Awesome path data is used
  here.
- **Hard exclusion: no third-party company logos or trademarks.** Real
  brand marks (e.g. the service logos vendored in `playlist-lab`'s
  `service-logos/` folder) are out of scope entirely — a generic,
  theme-library icon set must never ship someone else's trademarked brand
  as a "generic" icon. This also applies to the "brand-shaped" social
  icon batch in Phase 2 above: those are original generic
  share/community/network glyphs, never redrawn versions of a specific
  platform's actual logo.
- **The project owner's own app logos are out of scope for a different
  reason: they're the owner's own product IP, not this library's to
  ship as a generic icon.** `cutepi`'s `public/img/cutepi-logo.svg` and
  `LOGOs/cutepi-logo-80s-corporate.svg`, and `playlist-lab`'s
  `static/logo.svg`, were reviewed only for visual-weight/line-style
  inspiration (how much detail a mark carries at icon size, corner
  treatment, stroke weight) when Phase 1 was drawn — none of their
  artwork was copied into `assets/icons/icons.svg`. Those same files (and
  any future real third-party brand marks a consuming app needs to
  display) now have a home: see "Icon packs vs. logo packs" below.

## Icon packs vs. logo packs

This roadmap is entirely about **icon packs** — `assets/icons/icons.svg`
plus the per-theme overrides in `themes/<slug>/icons.svg`, merged by
`scripts/build_icons.py`. Everything in that system is a **generic UI
icon** (folder, arrow, play button, wifi glyph, ...): original artwork or
verifiably permissively-licensed third-party artwork (per
`docs/icon-license-research.md`), covered by this repo's own MIT-style
license, and safe to reskin per theme with zero legal complication
because nothing in it depicts a specific real-world brand.

**Logo packs are a separate system, on purpose: `assets/logos/`.** A
company logo or product wordmark is a **trademark**, not just a
copyrighted graphic — freely downloadable does not mean freely
redistributable, and it doesn't become "generic" just because a
consuming app wants to show it next to a generic icon (e.g. a "Connect
your Spotify account" button needing Spotify's actual mark). Key
differences from the icon-pack system, spelled out here so future
contributors never conflate the two:

| | Icon packs (`assets/icons/`) | Logo packs (`assets/logos/`) |
|---|---|---|
| What it contains | Generic, non-branded UI icons | Real third-party trademarks + consuming apps' own product logos |
| License model | This repo's own MIT-style license (or verified permissive upstream, tracked in `docs/icon-license-research.md`) | Each mark stays the property of its own owner; not covered by this repo's license at all |
| Per-theme variants | Yes — `themes/<slug>/icons.svg` overrides, merged by `scripts/build_icons.py` | No — a brand's logo must stay visually unmodified per that brand's own guidelines; there is no themed reskinning |
| Build integration | Bundled into every theme's `dist/icons/<slug>.svg` automatically | **Not** wired into `scripts/build.sh` at all — opt-in, explicitly imported per consuming app via `assets/logos/logos.css` |
| CSS helper | `.ftl-icon` (`core/ftl-core.css`) | `.ftl-logo` (`assets/logos/logos.css`) — separate namespace, no shared tokens |
| Governance | This roadmap + `docs/icon-license-research.md` | `assets/logos/README.md` + `assets/logos/manifest.json` |

See `assets/logos/README.md` for the full rules (never fabricate a
brand's logo; always record the official brand-guidelines URL; a real
third-party mark needs either that brand's own verified official SVG or
the project owner's explicit rights-confirmed file). `assets/logos/`
currently holds the project owner's own `cutepi` and `playlist-lab`
logos, plus documented `pending` placeholders in `manifest.json` for
real third-party marks (Spotify, Apple Music, Amazon Music) that are
referenced by `playlist-lab`'s `service-logos/` folder but were
deliberately **not** vendored into this shared library — that folder's
existing files are `playlist-lab`'s own concern, not something this repo
has redistribution rights over.

## Worked example: the folder-icon pattern

This is the concrete pattern every themed override in Phase 3 follows,
using `icon-folder` as the running example:

- The **generic** `icon-folder` in `assets/icons/icons.svg` is a plain
  outline folder tab shape — the fallback every theme gets automatically
  with zero effort.
- **windows95** ships its own `icon-folder` in `themes/windows95/icons.svg`
  drawn as a chunky manila-folder look (hard corners, thick stroke,
  matching that theme's already-established pixel-art convention).
- **winxp-luna** ships its own `icon-folder`, a blue tabbed folder look,
  consistent with its other existing overrides.
- **win7-aero** has *no* `icons.svg` override file yet, so it currently
  falls back to the plain generic folder — this is correct, working
  behavior today, not a bug. When win7-aero's icon work is scheduled
  (Phase 3), it gets its own `icon-folder` with a glassy/Aero look added
  to a new `themes/win7-aero/icons.svg`.
- **Every other theme** with no folder override (currently everyone
  except windows95 and winxp-luna) automatically uses the generic folder
  via the exact same merge mechanism in `scripts/build_icons.py` — no
  code change is ever needed to "add" fallback behavior; it's the default
  for every icon id a theme doesn't explicitly redefine.

The takeaway for future contributors: adding a themed icon is always a
**pure addition** — create (or extend) `themes/<slug>/icons.svg`, add a
`<symbol id="icon-existing-id">` with that id redrawn in the theme's
style, run `scripts/build.sh`, and `scripts/check.py` confirms the id
already exists generically and the sprite is well-formed. Nothing else in
the build, in consuming apps' `<use href="...#icon-name">` references, or
in other themes' overrides needs to change.
