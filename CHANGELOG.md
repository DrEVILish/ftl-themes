# Changelog

Consuming apps pin `ftl-themes` as a git submodule, so breaking contract
changes are called out explicitly here.

## Unreleased

- **v5 kits, emails, scheduling and quality tooling.**
  - New component groups with pages and docs: social (`components-social.html`),
    game HUD (`hud.html`: overlay regions, resource bars with damage trail,
    minimap, quest tracker, hotbar/inventory slots with cooldown and
    `data-rarity`, floating numbers, achievement toast, key/gamepad prompts)
    and productivity (`planner.html`: kanban, month/week/day calendar,
    Gantt timeline with dependency links, schedule list) and media
    (`player.html`: track list, now-playing bar and mini player, scrubber,
    volume and waveform with JS-free played fill, CSS-only repeat
    off/all/one, album grid, lyrics, queue).
  - Accessibility fixes from the new axe audit: `.slider.is-range` inputs
    span the full touch target, the nested-menu pattern in CONTRACT.md
    marks wrapper `<li>`s `role="none"`, blue-future's `--muted` reaches
    4.5:1 on every surface.
  - Themed transactional emails: `scripts/build_emails.py` writes six
    table-based, inline-styled emails per theme to `dist/email/<slug>/`
    (HTML + plain text), run by `build.sh`.
  - `assets/js/schedule.js` switches theme, variant or season by time of
    day or date; a user's own choice always wins.
  - Quality: `--engine chromium|firefox|webkit` on every browser script
    (`scripts/_harness.mjs`, per-engine known issues in
    `test/engine-known-issues.json`), `scripts/a11y_audit.mjs` (axe-core,
    `--blame <slug>`), size budgets in `check.py` (`--theme`, `--budgets`),
    `scripts/render_cost.mjs` (frame times under 4x CPU throttle) and
    `scripts/theme-ready.sh <slug>` running every gate. New docs:
    `docs/contributing-a-theme.md`, `docs/agent-theme-brief.md`.

- **CSS-only tabs, panes and selection; knobs; button widths; hovers.**
  - Hidden radios select list items, nav items, tabs, pagination, segmented
    items and menu items with no JS; the build (`scripts/radio_state.py`)
    gives them every theme's existing `.is-active` / `[aria-selected]`
    look. `.tabset` shows the panel for the checked tab. `.drawer[popover]`
    opens and closes with `popovertarget`.
  - Demo pages converted: tabs switch panels (ticket details as a property
    list, activity as a timeline), channel/view/ticket/cue lists select,
    drawers are popovers, menu entries are buttons, breadcrumbs link to real
    pages, and no `href="#"` remains (it scrolled to the top).
  - Knobs turn by dragging up and down (`controls.js`), their labels and
    `[data-for]` / fader readouts drag too, and the mixer's EQ curves redraw
    live from the band knobs.
  - `.toggle-btn` keeps its width when its label changes ("Rec" →
    "Recording"), and follows the theme's button padding and border so it
    lines up with buttons beside it (Windows Live, Windows 95, Liquid Glass,
    LCARS mixer transport).
  - Hover feedback added where every theme had none: accordion triggers,
    breadcrumbs, interactive list items, mixer keys; Win7 tabs light up blue
    (`--tab-bg-hover`, `--tab-border-hover`).

- **v5: six component groups, all 41 themes rolled out, integration fixes.**
  - Component groups in `core/components/` with pages and docs: tables
    (editable cells, stacked/frozen/grouped/tree tables, bulk bar),
    instruments and charts (needle gauge, compass, map, rings, donut,
    heatmap, timeline, clock, library-neutral chart contract), buttons and
    forms (19 components incl. date picker, combobox, tag input), navigation
    (menubar, tree, tab bar, sheet, rail, steps, command palette, split
    panes, keyboard layer), surfaces (image cards, draggable windows, brand
    sign-in buttons) and display settings (accessibility attributes, forced
    colours, `.prefs` + `prefs.js`, motion tokens, view-transition theme
    switching, splash, themed empty states, `404.html`). See CONTRACT.md
    "v5 component groups".
  - Every theme: v5 tiers (v4 720px queries replaced), phone and tablet
    layout fixes, XL gutter art, and a nesting pass so nested panels, cards,
    modals and drawers step down instead of repeating full decoration
    (e.g. Win7 nested title bars become group boxes, LCARS frames no longer
    collide, Aqua/Windows nested windows lose their window controls).
  - Period-correct modal close controls in every theme, with new close
    tokens (size, width, start placement); minimise/maximise follow the
    title bar's colour and group with close.
  - Core fixes found on the way: `data-accent` and `data-contrast="high"`
    now actually apply (they lost to every theme's root block); meter warn
    and peak bands are sized to the track, not the fill; switches and
    sliders get touch hit areas without changing their look; nav items
    centre their labels; `.btn` reaches the touch width; panel headers with
    controls wrap; `aria-current="page"` nav items and `aria-selected`
    table rows are styled; the tap-size rule no longer outranks components;
    a rail's tier display now beats `.app-rail:empty`; per-tier
    `--app-columns-mobile|-tablet`.
  - `scripts/v5_audit.mjs` covers the component pages and ignores inline
    chips (code, kbd, badges) in the text-to-edge check.

- **Fix: scrolling and carousels.** `.app-main` is no longer a scroll
  container (`overflow-x: clip; overflow-y: visible`). With v4's
  `overflow: auto`, anything sticking out of it (an open menu near the
  bottom) turned it into an inner scroller inside the scrolling page.
  Sticky elements inside main now stick to the screen. Carousel dots and
  prev/next no longer jump the page: `assets/js/carousel.js` scrolls only
  the carousel, steps prev/next from the current slide, and marks the
  current dot with `aria-current` (links still work without JS).

- **v5: containers and hover.** `.modal`, `.drawer` and the new opt-in `.cq`
  are size containers for `@container` rules (not `.app-main` or panels:
  a container traps fixed overlays and creates a stacking context).
  `.columns` collapses up to 900px (was 960px) and in containers narrower
  than 480px. Hover-only styles in core now sit inside
  `@media (hover: hover)`.

- **v5, slice 2: floating surfaces, nested menus, nesting fixes** (found by
  `nesting.html`).
  - `[popover]` popovers, context menus and dropdowns now open in the top
    layer correctly. v4's `position: absolute` had sent them off-screen.
    They open beside their button and flip at the screen edges where anchor
    positioning is supported. `.is-at-pointer` with `--x`/`--y` places a
    context menu at the pointer.
  - `.toast-region[popover="manual"]` works: it is hidden until shown, sits
    top-right without the browser's popover box, and appears above an open
    modal.
  - Nested `<ul>` context menus: flyouts on desktop that flip at the screen
    edge, inline expansion on touch tiers, separators and a submenu marker.
  - Anchored surfaces size to their content instead of the trigger.
  - `.drawer` pads its content, so a `.panel-header` inside one is no
    longer clipped.
  - Sticky headers in modals cover the padding band. `.table-wrap` scrolls
    wide tables inside their box. `--scroll-max` caps a `.scroll` region.
  - Long unbroken text wraps instead of spilling into the next column.
  - Hidden tooltips no longer widen the page. Tooltips wrap within the
    screen width.

- **v5, first slice (PLAN.md phases 0–2, on `blue-future`).** Breaking for
  layouts; v4 stays on the `v4` branch.
  - **Tiers:** mobile ≤480, tablet 481–900, desktop 901–1800, XL ≥1801px,
    replacing v4's single 720px breakpoint. Per-tier shell tokens
    (`--app-*-mobile|-tablet`, with the v4 `-sm` tokens as fallback), and
    `--tier` for container style queries.
  - **XL:** the shell is capped at `--app-max` (1800px) and centred, with
    theme art in the side gutters (`--app-gutter-art`). `blue-future`
    ships a starfield and drifting telemetry grid.
  - **Spacing:** the `--space-*` scale steps per tier, and container
    padding moved onto it through `--*-pad` tokens. Fixes a v4 bug where a
    density-scaled panel's header was pulled back by a fixed 1rem.
  - **Layers:** a `--z-*` scale replaces every literal z-index in core.
  - **Touch:** `--tap-min` (44px on touch tiers and coarse pointers, 24px
    otherwise) for every control's hit area; carousel dots and table
    checkboxes get bigger targets; inputs are 16px on touch devices.
  - **Cursor:** controls keep the arrow cursor (`cursor: pointer` removed
    from core and three themes).
  - **Bar:** wraps instead of overflowing; on touch tiers the brand
    truncates and the nav scrolls on its own line. Tabs scroll instead of
    wrapping up to 900px. The demo pages' bars now use the contract's brand
    / nav / actions markup (`lcars` adapted to it).
  - **New harness:** `nesting.html` (41 nesting and layering cases) and
    `scripts/v5_audit.mjs` (overflow, touch targets, spacing, edge text and
    the XL cap, across five target devices).

- **Core fixes from adopting ftl-themes in Playlist Lab.** All six are
  checked across every theme by the new `scripts/core_regressions.mjs`
  (Chromium, at 1280px and 390px).
  - `hidden` now hides components that set their own `display`
    (`.alert`, `.badge`, `.btn`, `.stack`, `.field`…). The reset adds
    `[hidden] { display: none !important }`, leaving `until-found` alone.
  - `.nav-collapse` paints on desktop in Chromium 131+, whose
    `::details-content` hid a closed `<details>`. Its open-state column
    layout only applies under 720px.
  - `.modal` and `.modal-sm|-lg|-xl` set a width, not just a maximum, so
    form modals no longer shrink to their content.
  - `.modal-header` is a flex row with the close button at the end, in the
    title bar's colour. A heading used as the title takes the header's type
    and colour. `winxp-luna` shows a real close button as its red Luna ×
    (no second, decorative one). `lcars`, `msdos` and `prometheus`, whose
    headers are only as wide as the title, put it in the modal's corner.
  - `.btn-secondary`, `.btn-ghost` and `.text-muted` in `.app-bar` take
    `--app-bar-fg` (or `--nav-item-fg`), so they no longer vanish on a
    coloured bar. `check.py` now also checks `--app-bar-fg` against the bar.
  - A `.table.is-sticky` header cell holding an open dropdown or popover is
    raised above its neighbours.

- **New theme: `westworld`.** The Delos tablet and Mesa control-room UI (by Chris Kieffer): cyan line-work on slate e-paper, condensed caps in the vendored Antonio, `[bracketed]` values. The shell becomes a tri-fold tablet of rounded panes with a right-hand rail of segmented attribute sliders, under a red cove-light status strip. Meters and progress bars are segmented ladders. 14 stills plus RESEARCH.md in `references/westworld/`. Self-scored fidelity 7/10.

- **New theme: `silo`** (Apple TV+'s Silo). Teal phosphor on CRT glass inside a steel monitor bezel; PACT-style bar with auto-numbered nav between pale-yellow double rules, pale-teal title/status plates, yellow-outline selection. Ships a `legacy` variant (Territory Studio's gold S2 tablet); 15 reference stills in `references/silo/` (`legacy/` for the variant). Self-scored fidelity 7.5/10.

- **New theme: `tokie`.** Black full-grain leather with saddle-stitched panel edges and gold-foil debossed Didone headings, textures CSS-only. Brushed gold for structure (spine rail, bar hinge rail, status nameplate), polished mirror gold for buttons, thumbs, the knob's watch crown and the focus ring. Watch-box layout: inset leather tray on a gold spine rail. 13 Commons references in `references/tokie/`. Self-scored fidelity 7/10.

- **xmb: readable modals.** Modals, toasts and tooltips are near-opaque navy smoked glass (`--modal-bg`/`--toast-bg`/`--tooltip-bg`) over a heavier, blurred `--overlay-bg`, as on real PS3 system dialogs; page content no longer shows through an open dialog. Modal title now 12.5:1 (was as low as 4.1), `.field-error` 6.2:1 (was 2.8). Four PS3 user's-guide captures added to `references/xmb/`.

- **New theme: `skyrim`** (The Elder Scrolls V: Skyrim + SkyUI). Smoke-black panels in thin silver rules with knotwork corners, a chevron-capped title bar, SkyUI column tables with an arrow-tipped selected band, diamond-capped health/magicka/stamina bars and MCM diamond toggles. 15 references in `references/skyrim/`. Self-scored fidelity 7/10.

- **New theme: `cassette-futurism`** (light). 1970s-80s retro-future hardware: beige housing, dark recessed VFD/LED windows, sculpted TR-808-coloured keycaps, Dymo-tape badges, a yellow/orange/red/brown stripe and a right-hand ribbed vent rail. `.switch` is a chrome bat-handle toggle, not a pill. Readouts use the newly vendored DSEG7 (OFL, `assets/fonts/`). 16 Commons references. Self-scored fidelity 7/10.

- **New theme: `liquid-glass`** (iOS 26 / macOS Tahoe 26), with a `dark` variant. Translucent capsule controls (blur + saturate, four-layer specular rim) over a CSS Tahoe-style wallpaper; content cards are frosted with no rim. Inset full-height glass sidebar, a frosted window, and sticky capsule toolbar and tab bar that content scrolls under. Honours `prefers-reduced-transparency`. 14 Apple Newsroom references (`dark/` for the variant). Self-scored fidelity 7/10.

- **check: palette variants may declare their own `color-scheme`.** The one-`color-scheme` rule now counts only the theme's root block, so a `dark` variant can say `color-scheme: dark;` instead of working around the lint.

- **New theme: `ios-flat`** (iOS 7 to 18, the flat era between `ios-skeuomorphic` and `liquid-glass`), with a `dark` variant on the iOS 13+ dark system colours. A frosted large-title nav bar (page nav as a segmented control) over grouped grey, inset grouped cards under uppercase section headers, a frosted tab-bar status strip, the green 51x31 switch, round checkmarks, centred alerts and iMessage bubbles. systemBlue is deepened to `#0071E3` for 4.5:1 under white text. 14 archived Apple HIG references. Self-scored fidelity 7/10.

- **New theme: `ios-skeuomorphic`** (iPhone OS 1 to iOS 6). Glossy blue nav bar with an embossed title over a black status strip, the Settings pinstripe behind rounded grouped cells, the black glossy tab bar, ON/OFF lettered switches, the navy alert view, iPad popover frame, red SpringBoard badge and iOS 5 banner toasts. CSS-only linen, legal pad, felt and stitched leather. The nav bar gradient is darker than the real `#bdcbdc` so the white title holds 4.5:1. 15 references. Self-scored fidelity 8/10.

- **`game-ui` category** in `themes/categories.json` (for `skyrim`); `gallery.html` now labels `game-ui`, `design-system` and `app-shell`.

- **References: Star Trek set culled and renamed (972 → 391 images).** Every
  capture in `references/lcars/` was tagged with the 1-3 UI components it
  uniquely shows and scored 0-10. Deleted: score < 5 (132), near-duplicates
  (28, the larger file kept), and images whose components a better image
  in the same gallery already shows (421). Files are now named by their
  components in camelCase, `-` between them (`elbowFrame-pillButton.webp`);
  `INDEX.md` lists each one's score and original lcars.org.uk number.

- **References: one folder per theme, one subfolder per variant.**
  `references/lcars/lcars-org-uk/` is gone. Its LCARS galleries moved into
  `lcars/` (default look), `lcars/tng/`, `lcars/tng-films/` and
  `lcars/voyager/` (DS9 panels). The Picard capture is in `lcars/picard/`.
  The non-LCARS Trek galleries now have their own folders:
  `references/star-trek-{alien,enterprise,tos,kelvin}/`. Variant-only images
  moved into variant folders for `weyland-yutani` (`mother`, `emergency`,
  `earth`), `winxp-luna` (`royale`, `royale-noir`, `zune`, `embedded`;
  filename prefixes dropped) and `prometheus` (`suit`). Every doc that names
  these files is updated.

- **`docs/theme-backlog.md` deleted.** Docs that pointed to it now say
  plainly what is not done yet.

- **GitHub Pages serves `main` again.** Pages was set to deploy from a
  workflow, and there have been no workflows since CI was removed. It now
  deploys straight from the branch root. `index.html` redirects to
  `gallery.html`, and `.nojekyll` makes Pages skip Jekyll.

- **References: the rest of lcars.org.uk.** The Alien-species, Enterprise
  (NX-01), TOS/TOS-films and Star Trek (2009) galleries are captured and
  component-tagged in `references/lcars/lcars-org-uk/` (446 screens,
  #513–#958), with a per-gallery table in INDEX.md. Marked as non-LCARS
  references; the Voyager gallery remains Flash-only.

- **winxp-luna: `olive` (Olive Green) and `silver` (Silver) variants,**
  completing the XP colour schemes. Silver has dark title-bar, dialog and
  taskbar text and silver caption buttons; the dialog title now follows
  `--modal-header-fg`.

- **steampunk: Nixie tubes, needle gauges, knife switches, filigree.**
  Counters and timecode glow in Nixie tubes; horizontal meters are
  edgewise panel meters with a needle; switches are hinged copper knife
  switches; cards and dialogs carry brass scrollwork corners. From the
  reference notes' "not yet done" list.

- **v4.1 components styled in 22 more themes.** Each gives the
  conversation, file chip and bar chart its own character: Aqua's iChat
  gel bubbles and gel columns, Barbie's pink speech bubbles, Winamp's
  spectrum analyser, Windows 95's sunken fields and navy progress blocks,
  steampunk's riveted-leather and brass message plates over copper-pipe
  columns, teletext's Ceefax colour bands, MS-DOS double-line boxes,
  Tron's hollow light-line columns, Hot Wheels' checkered-flag highlight,
  NERV's hazard stripes, and matching treatments for alienware,
  bloomberg, imac-g3, lego-classic, material, matrix, nokia-3310, pipboy,
  vaporwave, wmp11, xbmc and xmb.

## v4.1.0 — conversation, charts and console components; two new themes (2026-10-01)

Additive over v4.0.0: no class or token was renamed or removed. Two
behaviour notes for upgraders: a `.nav` inside `.app-bar` no longer
paints its own box (themes opt back in with `--app-bar-nav-bg`), and
popover/`<dialog>` modals are positioned by core in the top layer. New
themes: `windows-live`, `prometheus`. New core components: the
mixing-console primitives and the v4.1 conversation, row, chart and page
components (CONTRACT.md). Theme tint is a documented appearance setting.

- **Demo top bars stay on one line.** The theme picker is capped at
  11rem, marketing drops its "Sign in" button and "Power station" is
  "Power"; at 1280px the bar now wraps only in three wide-lettered
  theme/page combinations (it wrapped in 52).
- **v4.1 components, upstreamed from the example pages** (CONTRACT.md
  "v4.1 additions"): `.thread` / `.message` (`.is-own`) /
  `.thread-divider` / `.typing`, `.attachment`, two-line `.list-item`
  (`.list-item-title` / `-meta`), `.bar-chart`, `.value-row`,
  `.meter-bank`, `.table.is-matrix`, `.toolbar.is-plain`, `.hero`,
  `.band`, `.price`, `.feature-list`; layout helpers `.push`, `.columns`
  and `.is-auto`. All token-driven; added to the lint's base-component
  rule, with message, own-message and attachment text added to the
  contrast pairs. Styled in lcars, winxp-luna, win7-aero, windows-live,
  weyland-yutani and prometheus. Shown on components.html.
- **Example pages use them.** The chat and ticket threads, ticket inbox,
  dashboard chart and goals, power-station tanks and setpoints, mixer
  routing table and the marketing hero/bands/pricing are now core
  markup; the page-local grids are `.columns`; inline margins are
  `.mt-*`. The scaffolding that stays demo-only (static modal stages,
  inline previews of floating surfaces, top-bar wrapping) moved into one
  shared `assets/css/demo.css` instead of six drifting copies.

- **Demo pages link to each other.** The six example apps' top-bar nav
  is now real navigation between them (Dashboard, Marketing, Support,
  Power station, Mixer, Chat; the current page active), and the links
  carry the current `?theme=`/`&variant=` along. The gallery has a row of
  links to every example page at the top.

- **New theme: `prometheus`** — the USCSS Prometheus's holographic ship
  displays (2012): cyan holo-glass on deep navy, every panel opened by a
  rounded left bracket and named on a filled pill tab, outlined pill
  controls, dark value-box readouts, a dash-and-cross grid behind the
  shell and orange edge codes up the rail. `suit` variant: the suit
  room's amber over blue glass. Vendors Michroma, Share Tech and Share
  Tech Mono (SIL OFL). Seven reference frames.
- **weyland-yutani: screen variants `mother` (MU/TH/UR green),
  `emergency` (red) and `earth` (Alien: Earth cyan).** One phosphor each,
  with an inverse-video phosphor band replacing the beige plate and the
  top bar as the screen's header row. All palettes now draw the status
  strip as a row of outlined soft keys. The theme's hard-coded line and
  glass colours became `--wy-*` hooks; the default renders as before.
  19 new reference frames.
- **Demo pages:** the ticket inbox column is a panel, the chat's side
  columns are a fixed 17rem so names don't wrap, and marketing's dialog
  stage is larger so framed modals fit.

- **winxp-luna: real XP dialogs and taskbar.** Modals get the full Luna
  window frame (title bar with red close, blue side/bottom frame, beige
  face, Luna buttons, square fields); the status strip becomes the
  taskbar with the Start button and the notification-area tray, per
  variant (green / orange Zune / blue Embedded; charcoal tray on the
  black styles).

- **New theme: `windows-live`** — Windows Live Essentials 2011: Scenic
  Ribbon tab strip with the blue application button and Windows flag,
  white panes on a pale-blue aurora, Segoe UI Light headings (Live green
  titles), Windows 7 controls, Explorer selection and Messenger's glossy
  green presence frame on every avatar. 14 reference captures.
- **winxp-luna: `zune` and `embedded` variants** (orange-on-black;
  steel blue with a blue Start), XP balloon-tooltip corners, and new
  Royale / Royale Noir / Zune / Embedded / balloon references.
- **win7-aero:** flyouts and balloons are white in a tinted-glass frame;
  tray, balloon and Start-search references.
- **check:** a brand with its own fill (`--nav-brand-bg`, e.g. an
  application button) is measured against that fill.

- **No-JS modals:** `<div class="modal" popover>` opened by
  `<button popovertarget>` (and `<dialog class="modal">` via showModal)
  now sit centred in the top layer with the themed `::backdrop`, even in
  themes that set `position` on `.modal`. Every demo page has an **Open
  dialog** button that opens its dialog for real.
- **Theme tint is documented HTML/CSS-first:** render
  `style="--token: #rrggbb"` on `<html>` from a plain `<input type=color>`
  setting; JS only for optional live preview.
- **win7-aero dialogs:** tinted glass frame with the caption on the glass,
  white client area, #f0f0f0 command strip, and standard push buttons for
  `.btn-secondary` (was an outlined blue link look).

- **Theme tint — a required appearance setting.** A theme can declare a
  user-chosen colour (`Tint: --token #default Label` header →
  `tint: {token, default, label}` in `dist/themes.json`); apps must offer
  it as a colour control beside the theme/sub-theme picker, set the token
  on `<html>`, persist it per theme, and clear it when a preset sub-theme
  is chosen (CONTRACT.md "Theme tint"). win7-aero declares
  `--aero-tint` (Window Color). Every demo page and the components QA
  page show the control (`assets/js/tint.js`); `?tint=` sets it for
  screenshots. The lint checks a declared tint matches its root token.

- **win7-aero: Window Color.** One `--aero-tint` token tints every glass
  surface; Win7's fifteen other presets ship as variants (`twilight` …
  `frost`).
- **check: `color-mix()` is evaluated** (premultiplied, CSS Color 5) when
  measuring gradient stops, instead of reading the raw colour inside it.
- **Visual baseline: variants are shot on `dashboard` only** — a variant
  only repaints, and seven pages per variant bloated the baseline.
- **References:** 512 lcars.org.uk panels captured and component-tagged
  (`references/lcars/lcars-org-uk/INDEX.md`); five WMP11 captures; written
  reference notes for steampunk (new), teletext (CRT grid, Bedstead vs
  edit.tf's GPL TeletextKit), Windows 95 dialogs and Win7 Explorer/colour.

- **lcars: per-page review fixes.** Compact modals (no longer clipped in
  fixed-height boxes), panel titles that stop before the cap and keep
  their controls, wrapping two-line keys instead of overflowing rows,
  one-row scrolling tabs, visible tracks on horizontal meters, Antonio for
  codes and logs, no zebra, LCARS accordion rows and section links, and an
  elbow frame on pages without the app shell. Review notes in the README.

- **lcars: corner geometry follows the guide.** One elbow rule for every
  swept (outer `(leg + r) × (bar + r)`, inner a true circle), square
  corners everywhere else (`--radius: 0`), flat arm ends with separate
  semicircular caps, and the transport drawn as a bracket. Fixes the
  mismatched inner/outer curves at the top-left of the shell and the odd
  rounded ends on panel arms and overlays.

- **lcars: reference rules pass.** `references/lcars/RESEARCH.md` now
  summarises the LCARS guideline and manifesto (Bracer Jack, via
  lcars-terminal.de) plus four new captures. Every demo page was reviewed
  against it: thick-leg/thin-bar frames; three type sizes and two text
  colours; five structural colours with assigned meanings (sky/rose/gold
  now alias into them); flat knobs, fader caps and keys; no outlines on
  overlays, dropzones or keycaps; two spacing constants; 3:1 buttons;
  modal titles no longer clipped; gauge-style meters and a bracketed
  signal-trace EQ curve.

- **lcars: frames follow the originals.** Audited against the TNG and
  Sovereign-class references: the shell is now the split double frame
  (a second, upward elbow from the rail into a bar over the content);
  bars are segmented along their whole run; panel titles are coloured
  text in a break in the bar; panels/cards/modals are closed brackets
  with a bottom elbow; every outline and hairline is gone (fills only);
  button labels sit bottom-right. Findings in the theme README.

- **steampunk: valves and sight glasses.** Knobs become valve handwheels,
  faders sight glasses filled to their level (brass T-handle), progress
  and sliders glass tubes, keys glowing brass push-buttons, scribble
  strips nameplates, the EQ curve a parchment chart-recorder trace.
- **wmp11: closer to the player.** Black-glass panels with dark gloss
  header bars; the blue glossy tab capsule for every selected state (tabs,
  segments, pagination, rows, lists); a glowing seek-line progress bar and
  orb slider thumbs; white headings; brighter silk, now also behind pages
  that don't use the app shell.
- **windows95: the newer demo pages in 95 chrome.** A real title bar with
  caption buttons (the nav's grey strip is gone); panels as navy
  child-window caption bars; raised 95 tabs; segmented navy progress;
  sunken status-bar fields; square icon buttons; and the mixing console in
  95 bevels (sunken bay, raised strips, sinking lit keys, trackbar thumb,
  sunken scribble and EQ fields).
- **core:** `--fader-track` replaces a fader's whole groove, and
  `assets/js/controls.js` now also keeps each `.fader`'s `--value` (0–1)
  in step, so a theme can draw a track that fills to the fader.

- **Mixing-console primitives** (new core components), from the channel
  strips of the Yamaha CL/QL StageMix, Midas Heritage 3000 / HD96 and SSL
  4000: `.mixer` bay and `.strip` channel strip; `.knob` rotary control
  (value arc, centre-detent `.is-bipolar`, SSL band caps
  `.knob-hf|hmf|lmf|lf`); `.fader` long-throw fader with `.scale` dB
  legend and unity mark; `.meter.is-segmented` LED ladder and
  `.meter.is-gr` gain reduction; `.key` backlit keys (`.key-on|mute|solo|sel`);
  `.scribble` strip; `.eq-curve` thumbnail. `assets/js/controls.js` keeps
  knob rotation in step with its input. lcars, msdos and teletext paint
  them in their own palettes. See CONTRACT.md "Mixing-console primitives".
- **soundmixer demo rebuilt as a console:** eight input strips and a
  master in a bay (gain/48V/Ø, EQ curve + band knobs, gate lamps + GR,
  pan, mute/solo/sel, dB readout, scale + fader + LED meter, scribble
  strip), plus a selected-channel EQ / dynamics / aux-sends section.

- **Palette variants are now discoverable.** A theme lists its variants in
  its header (`Variants: id=Label, …`); `dist/themes.json` carries them as
  `variants: [{id, label}]`, the demo picker offers each one, pages accept
  `?variant=`, and the visual baseline shoots each as `<slug>~<variant>`.
- **lcars: `voyager` and `picard` era variants** alongside the default LCARS palette.
- **winxp-luna: fidelity pass + `royale` / `royale-noir` variants.** Real
  Luna title-bar and taskbar gradients, separate 21px caption buttons, a
  thick blue window frame, group-box panels with the caption on the frame
  line, raised tabs with the orange hot-track line, Luna push buttons
  (orange hover glow, blue default-button glow — primary is no longer
  green), Luna checkboxes/radios and the segmented green progress bar. The
  brand no longer vanishes into a white nav box in the title bar.
- **wmp11: more of the actual player.** The shell is one player window:
  the black glossy tab strip with evenly spaced tabs, a blue glossy active
  tab with its ▼, and round back/forward orbs; a blue-silk visualization
  behind the content; and the transport bar with its blue seek line and
  centred stop / prev / play-orb / next / volume capsule.
- **win7-aero: authentic chrome on the existing glass.** Harmony-blue
  desktop instead of pastel blobs; one glass window with diagonal glare
  streaks, glowing black caption text and the joined min/max/red-close
  caption group; a near-white client area; Win7 grey-gloss buttons and
  tabs with the pale-blue hover (primary is the default-button glow, no
  longer a blue fill); Explorer selection and the green glossy progress
  bar. The nav no longer paints a frosted box inside the title bar.
- **core: a `.nav` inside `.app-bar` no longer paints its own box.** It
  drew `--nav-bg` (tuned for a free-standing nav) as a second strip
  inside the bar, which hid the brand and nav items outright on barbie,
  material and vaporwave and left stray white boxes on aqua, aperture and
  imac-g3. The contrast lint already measured nav text against the bar,
  so this is what it assumed. A theme that wants the strip opts in with
  `--app-bar-nav-bg` (+ `-rule-width`, `-radius`); windows95 and
  hot-wheels do, and render unchanged.
- **msdos: Norton/EDIT chrome.** Grey menu bar with inverted open item;
  cyan double-line boxes with the title set into the frame; yellow
  headings and column heads; shadowed block buttons; grey dialogs with a
  hard drop shadow; the two-tone `1Help … 10Quit` F-key bar; and the
  real IBM VGA 9x16 text-mode font, vendored (Px437 by VileR, CC BY-SA
  4.0 — see `assets/fonts/NOTICE.md`).
- **steampunk: steam-age furniture.** Vendored IM Fell English SC (OFL)
  for display text with engraved headings; brass nameplates with screws
  for panel titles; copper steam pipes with bolted flanges along the bar
  and status strip; a meshing brass/copper gear train at the bar's end,
  turning only when reduced motion isn't requested.
- **teletext: the real character generator and page furniture.** Vendored
  Bedstead (CC0 SAA5050 recreation) for every glyph; a white P100 header
  row with rainbow index links; a double-height yellow-on-blue section
  banner; full-width colour-band panel titles; no rules anywhere; and a
  real Fastext row (red/green/yellow/cyan key words) replacing the stripe.
- **barbie:** numerals and readouts set in Baloo instead of Consolas;
  pale state-text tints on the magenta status strip.

- **lcars: fidelity pass against the on-screen references.** The shell is
  now a real elbow frame — a thick orange leg curving into a thin bar with
  pill-capped end segments, fixed-height labelled rail blocks, and a
  mirrored tan bottom elbow on the status strip. Panels, cards and modals
  are candy elbow frames on black (no grey cards) with the panel title set
  black in the top bar, flush right; colours rotate by position. Antonio
  now sets all text, body copy is tan and secondary text periwinkle,
  buttons are right-labelled pills, tabs are touching blocks, and the
  brand is the large right-aligned screen title.
- **check: pill nav items are measured against their own fill.** The
  app-bar nav-item contrast lint now reads `--nav-item-bg` when a theme
  sets one, instead of always measuring against the bar behind it.

## v4.0.0 — the `ftl-` prefix is gone (2026-09-29)

> ### ⚠ BREAKING — read [`docs/MIGRATING-v4.md`](docs/MIGRATING-v4.md) before upgrading
>
> v4 has **no backward-compatibility layer**. Nothing from v3 keeps working
> under its old name, and an un-migrated app renders **unstyled** — there is no
> warning at runtime because the library is CSS. Pin the `v3` branch
> (v3.14.0) if you are not ready.
>
> 1. **Every class name lost its prefix**: `.ftl-btn` → `.btn`, `.ftl-card` →
>    `.card`, `.ftl-app` → `.app`, … (all 190+ of them).
> 2. **Every custom property lost its prefix**: `--ftl-text` → `--text`,
>    `--ftl-btn-bg` → `--btn-bg`, … (500+). Bare names such as `--text`,
>    `--bg`, `--border`, `--accent` and `--radius` will collide with an app
>    that already defines them.
> 3. **Keyframes, ids, storage keys and files were renamed too**
>    (`ftl-spin` → `spinner-rotate`, `dist/ftl-core.css` → `dist/core.css`,
>    `core/ftl-*.css` → `core/*.css`, `window.ftlApplyIconTheme` →
>    `window.applyIconTheme`, `data-ftl-drag` → `data-drag`).
> 4. **Every bundle is wrapped in `@layer ui`.** Your unlayered CSS now always
>    beats the library, and an unlayered framework (Bootstrap, …) now beats it
>    wherever both define the same class — see the collision list in the
>    migration guide.
> 5. **`dist/themes.json`**: `version` is the bare content hash (it was
>    `ftl-<hash>`), and every entry has `"contract": 4`.
>
> **Names that now collide with popular frameworks** (documented, not aliased):
> 35 class names match Bootstrap 5 (`.btn`, `.card`, `.table`, `.modal`, `.nav`,
> `.badge`, `.alert`, `.row`, `.text-muted`, …) and `.flex`, `.grid`,
> `.container`, `.table`, `.divide-y` match Tailwind utilities with different
> meanings.

### Added

- Restored seven themes from `archive/themes-pending-reference/`: `aperture`, `cue-lab`, `material`, `nerv`, `pipboy`, `steampunk`, `tron` (32 themes now ship). The archive folder is gone.
- `screenshot_themes.py --theme X` now limits capture in `--baseline` mode too, so re-baselining one theme no longer rewrites the rest.
- Fixed: `.btn-primary` text was dark-on-dark in `tron`, `pipboy` and `alienware`; `build_manifest.py` now fails loudly if `git hash-object` fails.

- **Three themes**: `blue-future` (restored from the archive with the full
  original CuTePi default spec — #49, #60), `weyland-yutani` (Alien-franchise
  industrial: bone-beige equipment plates, amber phosphor readouts, hazard
  striping confined to danger states) and `international-rescue`
  (*Thunderbirds*, a light 1960s control-room theme). 25 themes now ship.
- **Components** (#51–#59): `.table-blank-rows`, `.switch` as
  `<button role="switch" aria-checked>`, `.slider.is-vertical`,
  `.toggle-btn` / `.is-danger`, `.schedule`, `.input.is-mirror`, form states and
  sizes (`.is-invalid`, `[aria-invalid]`, `.field-error`, `.input-sm`/`-lg`,
  readonly), `.btn-group`, `.btn-toolbar`. CONTRACT.md gains "Using v4 next to
  Bootstrap" (layer order) and a Recipes section (the canvas fade envelope,
  #55, is documented rather than shipped as a component).
- **Design docs** (#50): every theme README has Typography, Contrast honesty
  and Reference status sections with recomputed ratios; stale "no references
  folder" claims replaced with real citations.
- `docs/MIGRATING-v4.md`, `scripts/migrate-v4.py`, a `prefix` lint rule.

### Changed

- **A theme can no longer out-rank the app's own CSS.** With bundles in
  `@layer ui`, theme rules that target the *app's* classes (rather than
  library classes) lose to the app's unlayered rules. The example pages
  showed it: xbmc/xmb's nav-centring no longer overrides the pages' own
  `.demo-topbar`, and the msdos "twin-pane divider" that styled the example
  pages' private `.demo-two-col`/`.demo-split` classes was **removed** — it
  could never work for a real consumer.
- `dist/tokens.css` no longer carries theme rules that target any class
  (previously it leaked two page-specific msdos rules).
- `scripts/_pw_shot.mjs` counts nested rules when waiting for a bundle (a
  layered bundle has one top-level rule).

### Migration tooling

- `scripts/migrate-v4.py` rewrites your templates/CSS/JS from the v3 names to
  v4 (`--dry-run`, `--check`), driven by `scripts/v4-rename-map.json` (725
  names). It is exact-name, not a blind regex.
- `scripts/check.py` gained a `prefix` rule: any `ftl-` class/property/id
  in `core/`, `themes/`, `assets/js/` or the example pages fails the build.

## v3.14.0 — window pattern, taskbars, carousel/scrollspy, and v3.13 regression fixes (2026-09-28)

**Last v3 release.** v4.0.0 (next) removes the `ftl-` prefix from every
class name, custom property, keyframe and id; see the v4 section once it
lands. Pin the `v3` branch to stay on this contract.

### Fixed (regressions from v3.13.0 — upgrade if you are on it)

- **Spacing utilities were dead and `.ftl-stack` lost its gap.** A stray
  `*/` inside a comment in `core/ftl-core.css` closed it early, so the
  `:root { --ftl-space-* }` block was parsed as part of an invalid selector
  and dropped; the utility layer also redefined the existing `.ftl-stack`
  component, overriding its density-scaled gap and the `-sm`/`-lg`
  modifiers. `.ftl-stack` is left alone again, `.is-gap-*` set `gap`
  directly (they no longer inherit into nested containers), and the
  `--ftl-space-*` scale works.
- **`scripts/build_icons.py` read commented-out `<symbol>` stubs as live
  overrides**, so a freshly scaffolded theme shipped three placeholder icons.
- **Print:** the universal reset no longer erases meter/progress fills, chart
  bars or the selected-row marker (background and box-shadow are reset on
  named surfaces only); text is forced black on every element, not just
  `html, body` (a heading's own colour used to survive).
- **RTL:** `.ftl-select`'s arrow now mirrors with the padding.
- **`.ftl-table.is-striped`:** even rows keep their hover/focus highlight.
- **`assets/js/theme-loader.js`:** `?theme=` and the stored value are
  validated against `dist/themes.json`; it no longer overwrites the stored
  preference for a theme chosen by URL, guards a missing `#ftl-theme-link`,
  and builds the picker with DOM calls instead of `innerHTML`.

### Added / changed in this release

- **Window pattern (v3.14.0): `.ftl-btn-min` / `.ftl-btn-max`** mirroring
  `.ftl-btn-close` (glyph tokens `--ftl-btn-min-glyph` /
  `--ftl-btn-max-glyph`, usable as buttons or checkbox-hack labels);
  **maximize** (`.is-maximized` ≡ `.ftl-window-max:checked + .ftl-modal`),
  **minimize** (`.is-minimized` ≡ `.ftl-window-min:checked + .ftl-modal`,
  tray restore via app sibling rule), **focus stacking**
  (`:focus-within` → `--ftl-window-focus-z`), **`.is-resizable`**;
  **drag** stays a ~10-line `assets/js/window.js` reference snippet
  (non-contract). See CONTRACT.md "Window pattern" and the live
  `example.html` demo.

- **Taskbars for the desktop-OS themes (v3.14.0): new `.ftl-taskbar` /
  `-start` / `-task` / `-tray` family** — pair with `.ftl-app-status`
  for an OS task strip. windows95 paints raised bevels, a pressed +
  dotted active task and a sunken tray; winxp-luna paints the green
  Start pill and lighter-blue tasks (all white-text pairs ≥4.5:1);
  win7-aero paints the glowing orb and glassy tasks with an accent
  light-bar on the running one. All other themes keep the plain
  fallback. Token-driven (`--ftl-taskbar-*`, 4-sided bevels fit one
  token); all four classes join the base-component lint.
- **Tighter buttons on the same three themes:** windows95 gets compact
  dialog-scale padding plus the authentic extra black frame on the
  default (primary) button, pressed state included; winxp-luna radius
  4px → 3px; win7-aero command buttons break out of the 6px window
  radius to their own 3px.

- **Icon-only buttons no longer collapse:** `.ftl-icon` carries
  `min-width: var(--ftl-icon-size, 1.2em)` so the reset's
  `max-width: 100%` can't resolve circularly to 0 inside shrink-to-fit
  buttons (`.ftl-btn-icon .ftl-icon` floors at its own 1.1em). No-op
  everywhere the width already resolves.

- **New components (v3.14.0): `.ftl-drawer`, `.ftl-input-group`,
  `.ftl-list`** — slide-in side panel (app-toggled `.is-open`,
  `.is-start` edge, print-hidden, reduced-motion aware), joined
  input addons (unit/prefix/attached button sharing one border), and a
  bordered row stack with `.is-active` background + marker. All
  token-driven (`--ftl-drawer-*`, `--ftl-input-addon-*`,
  `--ftl-list-*`, reusing `--ftl-row-*` state tokens); all three join
  `scripts/check.py`'s base-component lint.
- **New utilities (v3.14.0): `.ftl-ratio`** (`--ftl-ratio`, default
  16/9, plus `-1x1`/`-4x3`/`-16x9`/`-21x9`), **`.ftl-text-truncate`**,
  **`.ftl-clamp-2`/`-3`**, **`.ftl-stretched-link`**,
  **`.ftl-divide-y`**, **`.ftl-container`**
  (`--ftl-container-max`, default 64rem). See CONTRACT.md
  "v3.14.0 additions" and `example.html` for live demos.
- **No-JS carousel, scrollspy, nav toggler (v3.14.0): `.ftl-carousel`**
  (scroll-snap track + anchor dots/arrows, smooth scroll
  reduced-motion gated), **`.ftl-scrollspy`** (sticky nav, smooth
  scroll, `--ftl-scrollspy-offset`; active-link mapping is one
  app-side `:target` rule per section — see CONTRACT.md — or
  `.is-active` from a scroll observer), **`.ftl-nav-collapse`**
  (native `<details>` toggler, hamburger below 720px, always laid out
  above). All three join the base-component lint.
- **`.ftl-meter` band fix:** `--ftl-meter-span` now defaults to `100%`
  (the element's own track) instead of `100vw`/`100vh`, so the default
  warn/peak bands land on-track. Apps that set the token explicitly are
  unaffected.
- **`.ftl-scroll` reads the browser-chrome tokens** (`--ftl-scrollbar-*`),
  so one tuning point drives both the page scrollbar and opted-in inner
  boxes; inner scroll containers are documented as opt-in via
  `.ftl-scroll` in CONTRACT.md.
- **New switch tokens** `--ftl-switch-border-on` / `--ftl-switch-thumb-bg-on`
  (both fall back to `--ftl-accent`); `nokia-3310` uses them for a
  hard-invert on-state instead of an accent-vs-muted thumb change.
- **`vaporwave` `--ftl-border` lightened** to `#8a5fc0` (3.6:1 on the
  panel) so secondary-button/input outlines are perceptible.
- **`windows95` tables get an opaque canvas** so badge fills can't bleed
  into whatever sits behind the rows.
- **3 new generic icons** (`icon-qr-code`, `icon-hourglass`,
  `icon-timer`, same Tabler source/version as the bulk batch);
  CONTRACT.md no longer hardcodes the 55-id list — grep the sprite.
- **`youtube` added as a `pending` logo** with its brand-resources URL,
  plus a "Self-hosting a third-party mark" path in
  `assets/logos/README.md`.

## v3.13.0 — four new themes, an extensible icon+logo system, layout primitives (2026-09-24)

**First git-tagged release.** Every version above this one shipped and is
recorded here, but was never tagged in git — there's no `v3.12.0` (etc.)
tag to check out. Going forward, a version heading in this file gets a
matching git tag at the commit that closes it, so consuming apps that
pin `ftl-themes` as a submodule have something more specific than `main`
HEAD to point at.

### Added

- **Vertical `.ftl-tabs` variant** (`aria-orientation="vertical"`): the left
  hand tab rail a settings sheet reaches for — column stack, selection
  marker on the inline edge, lead-aligned labels, inline-end hairline;
  same `--ftl-tab-*` tokens as the horizontal strip.

- **4 new themes: Teletext, Nokia 3310, XMB, XBMC.** All four ship a
  `README.md`, `theme.css` and `icons.svg`, and pass `scripts/check.py`.
  Unlike the rest of the catalog, none of the four has a
  `references/<slug>/` folder of captured real-world reference images yet
  — each was built from well-documented real-world facts about its
  reference platform instead. That's a deliberate, accepted,
  permanent-for-now state for these four (not a TODO to archive them
  over): they're fully built, documented, and already have icon
  overrides and fixes riding on them, so pulling them into
  `archive/themes-pending-reference/` the way the material/nerv/etc.
  batch was would undo real shipped work over a missing screenshot
  folder. Each theme's README now says so under a "Reference status"
  heading.
- **3 generic example layout pages**, plus a strict multi-category
  independent review-panel pass across the full theme set and the fixes
  it surfaced (signature-detail visibility, fidelity scores raised past
  8.0 for a dozen themes, `alienware`/`win7-aero` polish, `imac-g3`
  tangerine-variant AAA contrast).
- **Icon system built out further**: the generic set grew to 100 icons;
  every one of the 22 shipping themes now has a `themes/<slug>/icons.svg`
  override file (falling back to the generic set for any id it doesn't
  redraw); `docs/icon-library-roadmap.md` documents the scaling approach
  and a packs-vs-logos comparison; `docs/icon-license-research.md`
  records the licensing diligence behind the generic set's sourcing.
- **`assets/logos/`**: a separate, opt-in third-party brand-mark pack
  (not part of the MIT-style-licensed icon library — see
  `assets/logos/README.md` for the licensing rationale and rules).
- **`assets/fonts/NOTICE.md`**: license/designer/source audit for every
  vendored font family (Antonio, Audiowide, Baloo 2, Orbitron, Pacifico —
  all verified SIL OFL 1.1, checked per family rather than assumed
  uniform).
- **`scripts/new-theme.sh`** now also scaffolds a starter
  `themes/<slug>/icons.svg` (with commented-out example `<symbol>`
  stubs), so a new theme's author sees the icon-override option instead
  of discovering it later.
- **Core: layout utilities, `.ftl-btn-close`, table zebra striping, and
  modal sizes** — the feature set CONTRACT.md's own prose labels
  "v3.8.0" in its component-vocabulary section. Note: that label collides
  with this file's own already-used `v3.8.0` heading below (example
  pages / contrast fixes); the two are different, unrelated pieces of
  work that ended up sharing a version number in CONTRACT.md's inline
  notes. Recorded here under Unreleased rather than re-numbered, since
  this project hasn't cut a formal tag for either and reusing a number
  a second time would only compound the confusion.

### Removed — breaking for integrators that reference these paths

- **No GitHub Actions CI.** `.github/workflows/ci.yml`, `package.json`,
  `package-lock.json` and `scripts/audit_layers.mjs` are gone. Review
  happens directly on GitHub instead of via a runner; there is no
  `rendered` job, and no npm/Playwright dev-dependency to install. Run
  `python3 scripts/check.py` locally instead — it covers the same
  contract/lint ground the `check` job did.

- **`examples/` is gone** (26 per-theme pages + `index.html`, generated by
  the now-deleted `scripts/build_examples.py`). There is one example page
  now: `example.html` at the repo root, with a picker/stepper that
  switches the applied theme without changing the markup — the fair way to
  compare two themes' own CSS, and the thing to link instead of any
  `examples/<slug>.html` URL. One consequence: the "library classes only,
  no inline styles or app-specific markup" rule `build_examples.py`
  enforced on those 26 pages has no automated check anymore; `example.html`
  itself is a QA harness and was never held to that rule.
- **`demo.html` is gone.** It was a strict subset of `example.html`'s
  single-theme view (same components, same picker) minus the design-doc
  checklist and compare mode; `example.html` replaces it.
- **`dist/<slug>.layered.css` (26 files) is gone.** Wrap a bundle in a
  layer yourself instead — `@import url("dist/<slug>.css") layer(ftl);` —
  which needs no prebuilt file and does the same thing. See CONTRACT.md
  "Cascade layers" for the two behavioral differences from the old
  prebuilt form (mainly `@font-face` inside the layer) and how to recover
  the old form's finer-grained `reset`/`core`/`layout`/`theme` layer split
  if you genuinely need it.
- **`dist/<slug>-tokens.css` (26 files) is now one file, `dist/tokens.css`,
  holding every theme's tokens.** Each theme's rules stay scoped under its
  own `html[data-theme="slug"]`, so nothing collides — link it once and
  switch palettes via `data-theme` instead of swapping stylesheets.
- **`references/<slug>/SOURCES.md` (26 files) folded into
  `references/README.md`** as a "Capture targets, by theme" section.

`dist/` dropped from 80 files to 29 (26 theme bundles + `ftl-core.css` +
`tokens.css` + `themes.json`); the repo root and `examples/` together
dropped from 30 HTML files to 1.

### Changed

- **`themes.json` `version` no longer carries a `-dirty` suffix.** It is
  the content hash of the bundles and nothing else. The suffix described
  the author's working tree, not the build, and forced every source change
  into two commits. Integrators that matched on `-dirty` should stop; the
  hash still changes iff any served CSS changes.

### Fixed

- `scheme`/`luminance` are derived from the theme's unconditional root
  block only; imac-g3's luminance was read from its Tangerine variant.
- Bundles of deleted themes are removed from `dist/` by the build.
- The tokens bundle no longer splits `:is(a, b)`-style selectors at the
  inner comma (which produced invalid CSS).

### Lint

- A shared CSS reader (`scripts/cssparse.py`) replaces regex scanning:
  rules inside `@media`/`@supports` no longer count as root tokens, and
  selector lists split correctly.
- `chrome.css` is linted like `theme.css`; the app-bar contrast check runs
  per palette variant; the motion rule catches
  `animation-iteration-count: infinite`; the focus rule catches
  `outline: 0`.
- `scripts/audit_rendered.mjs` reads text colors of any syntax (oklch,
  lab, color-mix) instead of assuming `rgb()`.

## v3.12.0 — all text meets WCAG AA

**Visible change:** muted text is darker (light themes) or lighter (dark
themes) in 8 themes, and a few buttons and badges shift slightly. No
tokens or classes were renamed.

### Changed

- **Muted text floor raised from 3.0:1 to 4.5:1**, on `--ftl-surface` and
  `--ftl-surface-2`. Muted carries labels, table headers and tabs, which are
  essential small text. New `--ftl-muted` in aqua, aperture, barbie,
  bloomberg, death-star, imac-g3 (near-white: its variants' inset surfaces
  are mid-tones), material and winamp-classic. Each keeps its hue; the old
  value and ratio are in a comment beside it.
- **Badge tints are mixed into the surface**, not into transparent. A
  translucent badge in a tinted table row stacked on the row color, so its
  contrast depended on where it sat.
- aqua: accent text (active tab, secondary button, transport trigger) uses a
  deeper `--ftl-accent-text`; the primary gel's top stop is deeper so its
  white label holds 4.5:1.
- winxp-luna: the green gloss top stop is deeper for the same reason.
- aperture, alienware, hot-wheels, lego-classic, win7-aero: state/muted text
  nudged where it sat on a selected row or a badge tint.

### Audit

- `audit_rendered.mjs` skips content inside a closed `<details>` (it has a
  box but is not painted).
- Result: **0 text elements below 4.5:1** across all 26 example pages
  (was 69).

## v3.11.0 — layout, levels, anchoring, radios

Everything the example pages couldn't express without custom CSS. All
additive.

### Added

- **Layout primitives**: `.ftl-stack`, `.ftl-cluster`, `.ftl-grid` (+ `-sm`/
  `-lg`), density-scaled gaps. Components still carry no outer margin.
- **Native levels**: `<progress class="ftl-progress">` and
  `<meter class="ftl-meter">` are styled, so levels need no inline style.
  Meter bands use `--ftl-meter-low`/`-mid`/`-high`. The div forms still work.
- **`.ftl-anchor`** with `.is-below`/`.is-above`/`.is-end`: a positioned
  parent for popovers, context menus and dropdowns.
- **`.ftl-radio`, `.ftl-radio-group`** (fieldset + legend, `.is-inline`),
  **`.ftl-check`** (inline control + label).

### Fixed

- imac-g3 secondary buttons: accent text was 2.6:1 on the lighter part of
  the card gloss.
- `audit_rendered.mjs` no longer measures `<meter>`/`<progress>` fallback
  text, which browsers never display.

## v3.10.0 — cascade layers and token-only bundles

### Added

- **`dist/<slug>.layered.css`** (#29): each bundle wrapped in
  `@layer ftl.reset, ftl.core, ftl.layout, ftl.theme`, so unlayered app CSS
  always beats the library. Opt-in; the default bundles are unchanged. All
  26 themes compute identical styles in both forms.
- **`dist/<slug>-tokens.css`** (#4): a theme's tokens, fonts and
  element-level rules without any `.ftl-*` component or shell CSS, for apps
  that keep their own markup.
- Both are built by `scripts/build_bundles.py`, called from `build.sh`.

### Lint

- The dist staleness check now sees uncommitted *new* files in `dist/`, not
  only modified ones.

## v3.9.0 — open issues

### Added

- `.ftl-lamp.is-active`: an accent lamp that pulses for work happening now
  (#22). The pulse is gated on `prefers-reduced-motion: no-preference`.
- `.ftl-table` row highlight on hover and `:focus-within`
  (`--ftl-row-hover-bg`) (#30). Sticky headers already exist as
  `.ftl-table.is-sticky`.
- `--ftl-btn-icon-radius`, so `.ftl-btn-icon` can be square as well as
  round (#20).
- `prefers-contrast: more` applies the high-contrast boost automatically;
  `data-contrast="standard"` opts out (#27).
- Chart palette tokens `--ftl-chart-text`, `-grid`, `-series-1`…`-6` with
  base-token defaults; pipboy overrides them as a worked example (#24).
- `.ftl-log`, `.ftl-log-line[data-level]`, `.ftl-log-time`: a log console
  (#28).

## v3.8.0 — example pages, and the contrast bugs they exposed

Building one page per theme from library classes only (`examples/`, no
custom CSS, no inline styles) surfaced defects the token lint couldn't see.
Every fix below was found on a rendered page first, then measured.

### Fixed

- **Invisible app-bar text in 8 themes.** `.ftl-nav-brand`/`-item` read
  `--ftl-nav-*-fg`, never `--ftl-app-bar-fg`, so themes with a colored bar
  rendered their brand and nav at down to 1.0:1 (lcars, winxp-luna 1.0;
  windows95 1.3; barbie 1.5; aqua, death-star, win7-aero, winamp-classic
  3.8–4.3). Each now re-points the nav tokens in a `.ftl-app-bar` block, the
  pattern material and vaporwave already used. vaporwave's own fix still
  failed over its purple middle stop (3.6:1) and is corrected too. Barbie's
  bar and status strip are a deeper pink, because no text color reached
  4.5:1 across the old gradient.
- **State colors as text below 4.5:1 in 21 themes**, on `--ftl-surface`
  (16 themes) or on `--ftl-surface-2` / a translucent selection where
  status text also sits (5 more). As low as 1.3:1: barbie's mint and
  yellow on its own pink rows. New optional
  `--ftl-success-text`/`-warning-text`/`-danger-text`/`-accent-text` tokens
  keep each fill for lamps and buttons and give text a readable version of
  the same hue. `.ftl-status`, `.ftl-stat-trend`, colored badges and danger
  menu items read them.
- **State text on selected rows.** A green status on a solid blue selection
  measured 1.0:1. Status and trend text in `tr.is-selected` now follows
  `--ftl-row-selected-fg` when the theme sets one.
- **Row marker on every cell.** `tr.is-active`'s marker was a box-shadow on
  every `td`, so it drew a bar at every column. Now only the first cell.
- **`.ftl-field-row` spacing.** Consecutive rows touched, and a following
  label sat directly on the row above. Rows now have a bottom gap
  (`--ftl-field-row-gap`, default `0.5rem`).
- **imac-g3 Tangerine: body text at 3.8:1.** Surfaces deepened to a burnt
  tangerine (white text now 6.3:1). Blueberry and Grape accents lightened
  so link and active-tab text is legible (2.4 and 2.8 → 3.5 and 4.0:1).
- **imac-g3 gloss never rendered.** The pinstripe rule set
  `background-image` on `.ftl-panel` and `.ftl-app-bar`, replacing the
  gloss gradient and the panel fill. The stripe is now layered into the
  token value instead.
- **Smaller fixes:** winxp-luna's title-bar top stop (white text sat at
  exactly 4.5:1) and its footer status text (1.3:1); win7-aero's primary
  button (white on its pale glass top stop, 2.8:1); status-strip text in
  aqua, death-star, win7-aero and winamp-classic.

### Added

- **`examples/`**: one page per theme, written for that theme's world and
  built by `scripts/build_examples.py`, which refuses to emit a page with
  inline styles or undefined classes. `examples/README.md` lists the
  library gaps the pages exposed.
- **`references/README.md`**: where to see the real thing each theme is
  modelled on (links only; the originals are copyrighted).
- **`scripts/audit_rendered.mjs`**: measures every text element on the
  example pages against the pixels actually behind it. Fails below 3:1,
  reports below 4.5:1. Needs Playwright.

### Lint

- Contrast floors now run for every `data-variant` palette, not only the
  default one. Previously only the first value of each token was read.
- New hard rules: success/warning/danger text on `--ftl-surface` (4.5:1),
  app-bar brand and nav text against every stop of the bar background
  (4.5:1), and status-strip text (4.5:1).
- Translucent surfaces are composited over `--ftl-bg` instead of skipped.

## v3.7.0 — segmented control, sortable/sticky tables, remaining chrome gaps

Closes out the backlog flagged alongside v3.6.0: a component pattern
common enough to add speculatively (segmented control), two `.ftl-table`
hooks a data-heavy consumer will need, and the three browser-chrome
surfaces v3.6.0 didn't reach (native `<select>`'s closed-box arrow,
autofill, native `<dialog>`'s `::backdrop`). All additive, all
token-driven with base-token fallbacks.

### Added

- **`.ftl-segmented`** (+ `.ftl-segmented-item`, `.is-active`) — a
  segmented control / toggle group for mutually-exclusive view switches,
  distinct from `.ftl-tabs` (navigates) and `.ftl-badge-button`
  (multi-select filter chips).
- **`.ftl-table` sticky header** — `.ftl-table.is-sticky thead th` pins
  the header within the table's own scroll container.
- **`.ftl-table` sort indicator** — a clickable cursor, hover tint, and
  themed arrow on any `<th aria-sort="ascending"/"descending">`, reusing
  the attribute a screen reader already wants rather than adding a
  parallel `.is-sorted` class.
- **`.ftl-select` closed-box arrow** now themed via a CSS-triangle
  (`--ftl-select-arrow-fg`, default `--ftl-muted`) instead of the
  browser's own. The open dropdown list stays native OS chrome — no CSS
  can reach it.
- **Autofill** on `.ftl-input` now respects `--ftl-input-bg`/`-fg`
  instead of the browser's forced yellow/blue fill.
- **`dialog.ftl-modal::backdrop`** themed via `--ftl-overlay-bg`/`-blur`,
  for apps using the native `<dialog>` element instead of the
  `.ftl-modal-overlay` div pattern.

## v3.6.0 — browser-chrome theming

Closes the gap between "every `.ftl-*` component is themed" and "the whole
page looks themed": platform-painted surfaces (text selection, scrollbars,
form placeholder text, the input caret, `<kbd>`/`<code>`/`<pre>`) previously
fell back to the browser's own default appearance regardless of theme,
which was the most visible remaining "generic browser" tell in an
otherwise fully-themed retro/console page. All additive, all token-driven
with base-token fallbacks — no theme file needs to change to pick these up.

### Added

- **`::selection`** now themed (`--ftl-selection-bg`/`-fg`, default accent /
  on-accent).
- **Scrollbars** themed via `scrollbar-color`/`scrollbar-width` (Firefox)
  and the `::-webkit-scrollbar*` pseudo-elements (Chromium/Safari):
  `--ftl-scrollbar-thumb` (default `--ftl-border`), `-thumb-hover` (default
  `--ftl-accent`), `-track` (default transparent), `-size`, `-radius`,
  `-width`.
- **`::placeholder`** on `.ftl-input`/`.ftl-textarea` (`--ftl-input-placeholder`,
  default `--ftl-muted`) — previously always the browser's own gray.
- **Input caret color** (`--ftl-input-caret`, default `--ftl-focus`).
- **`<kbd>`** — a themed inline keyboard-shortcut glyph
  (`--ftl-kbd-bg`/`-fg`/`-border`/`-radius`/`-shadow`).
- **`<code>`/`<pre>`** — themed inline and block code
  (`--ftl-code-bg`/`-fg`, `--ftl-code-block-bg`/`-border`), distinct from
  `.ftl-readout` (a live machine value) and `.ftl-mono` (a bare
  font-family utility).

## v3.5.2 — consumer-reported fixes: color-scheme, density-scaled targets, offline lint

Addresses issues filed from real integration work in CuTePi, PI9696, and
Playlist Lab.

### Added

- **`color-scheme` per theme** (#21). Every theme's root block now
  declares `color-scheme: light;`/`dark;` matching its palette, judged
  from `--ftl-surface` (the substrate that actually carries content, not
  `--ftl-bg`, which can be purely decorative — windows95's teal desktop
  is the case that mattered here). UA-owned chrome (scrollbars, native
  date/time pickers, autofill) now matches instead of defaulting to light
  under every dark theme. `scripts/check.py` fails a theme with zero or
  more than one declaration. Themes still don't respond to
  `prefers-color-scheme` — this only declares what they already are.
- **`--ftl-density` now scales interactive targets** (#26): `.ftl-checkbox`,
  `.ftl-switch`, and `.ftl-slider`'s thumb size with density, not just
  padding. A touch-first theme at density 1.15+ gets bigger grab targets
  to match its roomier spacing. Default density renders byte-identical to
  before; per-part tokens (`--ftl-switch-*`, `--ftl-slider-thumb-size`)
  still override.
- **`.ftl-badge-warning`** (#19) — the fourth severity variant, matching
  `-accent`/`-danger`/`-success`.
- **Lint: no remote URLs** (#25). `scripts/check.py` now fails any theme
  or core file containing a remote `url(...)` or `@import` — a
  field-offline consumer embeds the bundles specifically so the UI works
  with zero network access; one remote reference upstream would silently
  break that guarantee.
- **"Requires: L0/L1" badge rolled out to all 26 READMEs** (#18), all
  `Requires: L1` (every current theme sets `--ftl-app-*`). The lint is
  promoted from warn to fail now that the rollout is complete.

### Verified already fixed (stale issue reports)

Issues #8 (LCARS headings), #9 (TRON focus-outline clipping), #10
(windows95 body-text contrast), and #11 (cue-lab GO min-target) were
already resolved in an earlier pass — confirmed against current source,
no further change needed.

## v3.5.1 — compare mode, signature-detail pass, source-accuracy fixes

### Added

- **`example.html` compare mode.** Pick two themes and see both rendered
  full-width side by side (each an embedded copy of the page itself), with
  each theme's "Signature details" pulled from its README into the
  sidebar for a read-without-scrolling comparison. Deep-linkable via
  `?compare=1&a=<slug>&b=<slug>`.
- **`docs/engine-improvements.md`** — a written set of recommendations
  from this review pass: what was implemented, what's deferred and why
  (visual regression testing, a token-diff tool, a per-theme token-usage
  report), and what was deliberately rejected (an authenticity "score",
  auto-generating READMEs from CSS).
- Every theme's README now has a "Signature details" section (11 of 26
  didn't); `scripts/check.py`'s docs rule now warns if a new theme ships
  without one, since that's the section compare mode surfaces.

### Changed

- Every theme's one-line `Description:` (feeds `dist/themes.json` and
  theme pickers) now names a concrete signature detail instead of a
  generic palette summary. `CONTRACT.md`'s theme index rewritten
  accordingly, with a new "Signature detail" column.
- **`lcars`**: `--ftl-lcars-sky` corrected from an unsourced pastel
  periwinkle (`#9999ff`) to `#6699ff`, closer to the Okuda reference
  palette's documented blue family ("mariner"/"bahama-blue") while
  staying inside the button-text contrast floor (the literal reference
  blue fails at 3.9:1). `--ftl-accent` and `--ftl-lcars-lavender` were
  verified exact matches to the reference and needed no change.
- **`winxp-luna`**: softened an overclaiming comment about the Start-button
  green being "the actual" color to "the commonly cited" one — no single
  hex was ever an officially published constant.

## v3.5.0 — five more themes: Windows 7 Aero, Alienware, Vaporwave, Material, Bloomberg Terminal

### Added

- **`win7-aero`** — frosted glass via real `backdrop-filter` blur over the
  Aero blue desktop gradient, distinct from `winxp-luna`'s opaque gloss.
- **`alienware`** — matte black, angular `clip-path`-cut corners (reusing
  tron's clipped-focus workaround), a single AlienFX cyan glow.
- **`vaporwave`** — outrun synthwave: magenta/cyan gradient chrome text,
  deep-purple void, perspective grid-floor status strip.
- **`material`** — Google Material Design: flat color, layered elevation
  `box-shadow` stacks instead of gloss/blur, underlined text fields.
- **`bloomberg`** — black-and-amber monospace data density; `--ftl-density:
  0.7` as a deliberate extreme-density stress test for `.ftl-table`.

All five contrast-checked (≥4.5:1 on required pairs) before landing;
`vaporwave`'s danger red was darkened one step past the literal reference
(`#ff3864` fails 4.5:1 against white) for the same reason `winxp-luna`'s
success green and `barbie`'s accent pink were.

### Fixed

- **`winxp-luna`**: `.ftl-btn-primary` and `.ftl-btn-go` used the chrome
  blue, contradicting this theme's own README ("green means go, blue means
  select"). Both now use the Start-button green; the title bar, focus
  ring, and "this is selected" states stay blue.
- **`material`**, **`vaporwave`**: the app bar's `.ftl-nav-brand` and
  active `.ftl-nav-item` used the shared `--ftl-nav-*` token defaults
  (accent-colored text), which are invisible or near-invisible against
  these two themes' accent-colored bars. Re-pointed the tokens on
  `.ftl-app-bar` specifically so the standalone `.ftl-nav` component
  (different background) is unaffected.

## v3.4.2 — remove `winxp-zune`

**Breaking for any app pinning `data-theme="winxp-zune"` or serving
`dist/winxp-zune.css`.** The theme is removed: `themes/winxp-zune/` and
`dist/winxp-zune.css` are deleted, and its row is gone from `dist/themes.json`
and the CONTRACT.md theme index. `winxp-luna` (the default Luna Blue XP
desktop, added in v3.3.0) remains and is unaffected — the two were always
visually distinct, not a swap of one for the other. An app still on
`winxp-zune` should switch its `data-theme`/link to `winxp-luna` or another
theme; there is no automatic redirect.

## v3.4.1 — flagship-theme fidelity pass on the v3.4.0 components

Fixes the gap where all 22 themes rendered the 19 new v3.4.0 components
(toast, alert, card, context menu, dropzone, avatar, tooltip, popover,
pagination, breadcrumbs, skeleton) with plain unstyled fallback tokens.
Seven themes with the strongest visual identity now give them real
theme-specific chrome, matching their existing idiom: `lcars` (candy-bar
borders, elbow radii), `matrix` (green glow, phosphor shadows), `tron`
(cyan glow, cut corners kept square on these), `windows95` (beveled
chrome, marching-ants tooltip), `winxp-luna` (Luna gloss), `barbie`
(pink/gold gloss), `hot-wheels` (flame glow). All new fg/bg pairs
contrast-checked (≥5:1) before landing. The remaining 15 themes are
unaffected — token-only theming is still a legitimate baseline.

## v3.4.0 — component library expansion

Non-breaking: every token and class from prior versions is unchanged. All
additions read existing base tokens with fallbacks, so every theme picks
them up with zero theme-file changes.

### Added

Sourced from real duplication found in the three consuming apps (CuTePi's
context menu and dropzone, PI9696's icon button and settings rows,
Playlist-Lab's toast/card/badge-button/empty-state) plus a curated set of
generic primitives the component landscape was conspicuously missing:

- `.ftl-toast` / `.ftl-toast-region` — transient dismissable notifications.
- `.ftl-spinner` — a bare loading indicator for non-htmx async work.
- `.ftl-context-menu` (+ `-item`, `-divider`) — cursor/anchor-positioned menu.
- `.ftl-dropzone` — drag-and-drop file target, with `.is-dragover` state.
- `.ftl-field-group` (+ `-title`) — a titled group of `.ftl-field` rows.
- `.ftl-btn-icon` — a circular icon-only button modifier on `.ftl-btn`.
- `.ftl-card` — a lighter-weight `.ftl-panel` sibling.
- `.ftl-badge-button` — a clickable badge (filter chip).
- `.ftl-empty-state` (+ `-icon`, `-title`, `-hint`).
- `.ftl-tooltip` via `[data-tooltip]` — CSS-only, no JS required.
- `.ftl-popover` — a `.ftl-dropdown`-style surface, app-toggled.
- `.ftl-accordion-item`/`-trigger`/`-panel` — built on native `<details>`.
- `.ftl-breadcrumbs` (+ `-item`, `.is-current`).
- `.ftl-pagination` (+ `-item`, `.is-active`, `.is-disabled`).
- `.ftl-alert` (+ `-info/-success/-warning/-danger`) — persistent inline banner.
- `.ftl-skeleton` (+ `-text`, `-block`) — shimmer loading placeholder.
- `.ftl-avatar` (+ `-sm`, `-lg`).
- `.ftl-stat` (+ `-value`, `-label`, `-trend`) — KPI tile.
- `.ftl-divider` / `.ftl-divider-v`.

See CONTRACT.md "Component vocabulary — v3.4.0 additions" for markup
examples of each. `demo.html` has a new "v3.4.0 additions" section.

## v3.3.0 — three more themes: Windows XP (Luna), Barbie, Hot Wheels

### Added

- **`winxp-luna`** — the default Luna Blue Windows XP desktop (glossy
  round-cornered blue title bar, tan/white content, Tahoma), distinct from
  the already-shipped `winxp-zune` reskin.
- **`barbie`** — hot-pink glamour: glossy pill chrome, gold sparkle
  headings, mint success state with dark-on-fill text.
- **`hot-wheels`** — blister-pack orange on track-black: a diagonal flame
  stripe across the app bar, a checkered-flag status strip, bold italic
  uppercase type.

All three ship a full `--ftl-app-*` layout personality (`shellAware:
true`), a `README.md`, and pass `scripts/check.py` at 0 failures / 0
warnings, including contrast: two of the three needed their accent one
shade darker than the "true" brand color to clear 4.5:1 against white fill
text (`winxp-luna`'s success green `#3d9f1e` → `#2e7a14`; `barbie`'s pink
`#e0218a` → `#c81b7a`) — noted inline in each theme's source so the
deviation from the brand reference is documented, not silent.

All additive, all inside individual themes or a single component's fixed
floor — no token or component contract changed shape.

### Fixed

- **`lcars` headings rendered in Trebuchet, not Antonio** (#8). Antonio is
  already shipped for the shell bar and readouts; `h1`-`h3` now lead with
  it too, so section titles stop reading as a second, unrelated theme next
  to the readouts.
- **`tron`'s cut-corner `clip-path` silently clipped the focus outline**
  (#9). `clip-path` clips everything the box paints, including core's
  `:focus-visible` outline — a keyboard user got no visible focus on
  buttons or panels, undetectable by `scripts/check.py`'s `outline: none`
  lint since nothing sets it to `none`. Added a `filter: drop-shadow(...)`
  focus treatment, which isn't clipped because it post-processes the
  already-cut shape. Also dropped `Eurostile, Orbitron` from the font
  stack: neither is vendored in `assets/`, so naming them just meant every
  real system silently rendered the generic-sans fallback while the stack
  claimed a face the theme doesn't ship.
- **`windows95`'s `--ftl-text` on `--ftl-bg` was 4.4:1, just under the
  4.5:1 floor** (#10). `--ftl-bg` moves from `#008080` to `#008282` — 2/255
  of extra green/blue, imperceptible on a decorative desktop backdrop that
  never carries body text, and the minimal change that crosses the floor.
  Real dialog contrast is unaffected: panels read `--ftl-surface`, not
  this token.
- **`.ftl-btn-go` had no minimum hit target** (#11): `--ftl-density`
  scaling (e.g. `cue-lab`'s `0.85` for a dense cue list) could shrink the
  one control every other element in a theme is allowed to compress
  around. Added a fixed `min-width`/`min-height: 44px` floor
  (`--ftl-go-min-target`) that density scaling cannot shrink — every other
  `.ftl-btn` in a theme keeps compressing freely.

## v3.2.0 — layout-tier themes degrade gracefully; adoption levels documented

Filed as ftl-themes#3 and #4 after real integrations (PI9696, CuTePi,
Playlist-Lab) all shipped as token-only: linking a layout-defining theme
like LCARS without adopting the `.ftl-app` shell produced "an orange-tinted
blue-future," not LCARS — technically correct, but not what "generic
project other apps can use easily" should mean without a documented path
to the real experience. All additive.

### Added

- **`.ftl-app-rail` degrades gracefully with no shell markup.**
  `core/ftl-layout.css`: `.ftl-app-rail:empty { display: none }` collapses
  a theme's decorative rail when the app added the element but left it
  empty (the documented, `aria-hidden`, no-content case); `.ftl-app:not(:has(>
  .ftl-app-rail))` collapses the column track itself when the app never
  added the element at all. Either way, a theme that opens a rail (LCARS,
  tron, wmp11, aqua, …) no longer paints an unexplained empty gutter in an
  app that hasn't adopted the shell — it just quietly doesn't reserve the
  space, per CONTRACT.md's new degrade rule: *a theme must not look broken
  one level down from what it was authored for*.
- **CONTRACT.md "Adoption levels"**: formalizes L0 (tokens only — today's
  actual state for every sibling app), L1 (the `.ftl-app` shell — layout-
  tier theming), L2 (theme-specific chrome or full `.ftl-*` component
  adoption), replacing the previous informal "adopting the shell is
  optional" note with an explicit, named ladder an integrator can point at.
- **`shellAware` field on every `dist/themes.json` entry** — `true` when a
  theme sets any `--ftl-app-*` property (the same detection
  `scripts/check.py`'s existing `layout` warning already used), so a
  picker can tell the user up front that a theme's full intent needs L1,
  instead of them discovering the gap after linking it.
- **A "Requires" note in every theme's `README.md`** naming what's lost at
  L0 and pointing at CONTRACT.md's "Adoption levels" for the fix.
- **`demo.html` L0/L1 toggle** — unchecking "App shell" strips the
  `.ftl-app*` classes from the same elements live, so the fidelity gap is
  visible in the one place a theme is meant to be evaluated, rather than
  only discoverable after a real app integration.

## v3.1.1 — contract gaps found by the first real integration

CuTePi's integration (DrEVILish/CuTePi#1) surfaced six gaps between what
the contract implied and what it actually guaranteed. All additive; no
existing field changed shape.

### Added

- **`dataTheme` field on every `dist/themes.json` entry**, explicitly equal
  to `slug` — CONTRACT.md already guaranteed this by construction, but an
  integrator had to infer or verify it themselves. Use `dataTheme`, not
  `slug`, when building a picker id.
- **`version`/`builtAt` on every manifest entry**, from `scripts/build.sh`
  (`git describe` + UTC timestamp). Since dist bundles inline the core
  component structure, every core change touches every theme's file — this
  is how an integrator confirms which build a deployment is actually
  serving. `scripts/check.py`'s dist-sync check now diffs `themes.json`'s
  content *excluding* these two fields (they legitimately change on every
  rebuild) while still failing on any other drift.
- **`dist/ftl-core.css`** — the reset + `.ftl-*` component structure alone,
  no theme, no app shell. For an app doing colour-only adoption (a token
  bridge onto its own existing classes, no `.ftl-*` markup) that doesn't
  want to load a full theme bundle just to get the component CSS it will
  never use. See CONTRACT.md "Color-only adoption".
- **CONTRACT.md**: a "Cache-busting" section recommending `?v=<manifest
  version>`, so family apps stop each inventing their own scheme (CuTePi's
  binary-mtime scheme predates this and still works — this just gives the
  next app a documented default); an "Avoiding name collisions with an
  app's own themes" section documenting the qualified-picker-id pattern
  (`app:lcars` / `ftl:lcars`) CuTePi had to invent from scratch; and the
  sibling-asset-serving requirement (previously a paragraph under "Serving
  the assets") promoted and spelled out as load-bearing, not incidental.

## v3.1.0 — palette variants, accent swatches, display options, 10 new themes

### Added

- **Palette variants** (`data-variant`) — a theme may ship more than one
  colorway under one identity, selected by an extra attribute on the
  theme's own selector (`html[data-theme="x"][data-variant="y"]`, which at
  specificity `(0,2,1)` outranks the theme's `(0,1,1)` root block, so no
  core mechanism is needed). `imac-g3` ships Bondi Blue (default) plus
  Blueberry/Grape/Tangerine.
- **Accent swatches** (`data-accent="1".."6"`) — a theme may offer curated,
  contrast-checked alternate accents as `--ftl-accent-swatch-<n>` /
  `--ftl-on-accent-swatch-<n>` pairs; core reads whichever the theme
  defines. This is the supported replacement for a "paste your own theme
  JSON" feature: every swatch is a colour the theme's author vouched for.
- **User display options**, independent of theme choice: a density
  override via inline style (`<html style="--ftl-density: 0.85">`, which
  wins over any stylesheet regardless of specificity); `data-motion`
  (`"reduced"`) to force animations/transitions off from an in-app toggle,
  not just the OS setting; `data-contrast` (`"high"`) to pull
  `--ftl-hairline`/`--ftl-muted` up to `--ftl-border`/`--ftl-text` and
  thicken the focus ring, without leaving the theme.
- **Ten new themes**: `imac-g3`, `winxp-zune`, `msdos`, `pipboy`, `nerv`,
  `aperture`, `death-star`, `lego-classic`, `steampunk`, `cyber-goth` —
  each with a `README.md`, contrast-checked, and given a distinct
  `--ftl-app-*` layout personality.

## v3.0.0 — themes control layout; instrument primitives; theme docs

### Added

- **The app shell (`core/ftl-layout.css`).** A theme is a layout as much as
  a palette. One markup contract — `.ftl-app` + `.ftl-app-bar` +
  `.ftl-app-rail` + `.ftl-app-main` + `.ftl-app-status` — which every theme
  re-arranges through `--ftl-app-*` properties, so switching theme moves the
  furniture instead of only recolouring it. LCARS opens a 6rem candy rail
  and elbows its sweep bar into it; blue-future runs edge-to-edge with no
  rail; Aqua and WMP11 become floating rounded windows; Windows 95 and
  WinAmp become beveled window chrome. The rail is decorative and painted
  in CSS, so no app ships theme-specific markup. Adopting the shell is
  optional.
- **Instrument primitives**: `.ftl-meter` (+ `.ftl-meter-v`, peak hold,
  tokenised band thresholds), `.ftl-readout` (+ `-lg`/`-sm`/`-unit`),
  `.ftl-transport` + `.ftl-btn-go`, and `.ftl-lamp`. These exist because the
  themes here are control surfaces — a recorder, a show console, a starship
  computer — and a palette alone cannot express that.
- **`--ftl-density`** — scales button, table-cell and panel padding.
  `cue-lab` sets `0.85` (fit the cue list), `lcars` sets `1.15` (wall panel).
- **A `README.md` beside every theme's CSS**, stating what that theme is
  trying to achieve: the reference, its core values, why the significant
  token values are what they are, what not to change, and the tell-tales of
  an inauthentic result. The lint now fails a theme that has none.
- Lint rules for the two above: `docs` (README present, with the expected
  sections) and `layout` (warns when a theme defines no `--ftl-app-*`
  personality).

### Changed

- **`blue-future`'s palette is reconciled against its reference device**
  rather than approximating it: `--ftl-accent` `#2fd6ff`→`#00d9ff`,
  `--ftl-border` `#176095`→`#0f3a5c`, `--ftl-surface` `#07172a`→`#0a1526`,
  `--ftl-text` `#dff4ff`→`#cfeeff`, `--ftl-muted` `#7ca6c3`→`#5b8aa8`,
  `--ftl-danger` `#ff5f87`→`#ff3355`, `--ftl-success` `#42ddb2`→`#2bffb0`,
  `--ftl-warning` → `#ff8c1a`, and the font stack leads with Consolas.
  Apps that used the old values will see a slight shift.
- `themes/lcars/chrome.css` is demoted to the optional richer frame; the
  shell is the default path. The Antonio `@font-face` moved into
  `theme.css`, since the shell's bar and the readouts both use it.
- `demo.html` is built on the shell, so the theme switcher demonstrates the
  layout change, and exercises the instrument primitives.

## v2.0.0 — app-agnostic contract, hardened

### Breaking

- **`--ctp-*` tokens renamed to `--ftl-*`.** An app bridging its own tokens
  must update its alias block.
- **Bootstrap class names dropped.** Themes no longer style `.btn`,
  `.form-control`, `.table-dark`, `.navbar`, `.modal-content`; the
  vocabulary is now `.ftl-*` (see `CONTRACT.md`). An app can bridge by
  aliasing tokens and adopting the `.ftl-*` classes incrementally.
- **All app-specific selectors removed.** Nothing in this repo references
  any particular application's markup any more.
- **New required tokens**: `--ftl-on-accent`, `--ftl-on-danger`,
  `--ftl-on-success`. A theme omitting them now fails the lint.
- **Themes must set component look via `--ftl-<component>-*` at root
  scope**, not by declaring `background`/`color` on base component
  selectors. See the fix below for why.

### Fixed

- **Button variants were silently erased in 6 of 9 themes.** A theme's
  `html[data-theme="x"] .ftl-btn` rule (specificity 0,2,1) outranked core's
  unscoped `.ftl-btn-danger` (0,1,0), so semantic fills never applied — a
  delete button rendered identically to a normal one in `matrix`, `tron`,
  `winamp-classic` and `wmp11`. Components now read local custom properties
  with inline fallbacks, and variants set those properties on the element,
  where a declaration always beats an inherited one regardless of
  specificity. Verified: all 9 themes now resolve their semantic fills.
- **The LCARS display font never loaded** — the vendored Antonio files had
  no `@font-face` rule. Added, and `scripts/build.sh` now rewrites relative
  asset URLs for the `dist/` bundles so they resolve from there.
- **Invalid `border-radius` in the LCARS chrome** (a comma-separated list,
  which browsers drop whole) replaced with a valid shorthand.
- **`windows95` inputs had no focus indicator**: the theme set
  `outline: none` and replaced it with a `box-shadow` identical to its
  resting state. Core now always draws the outline; themes recolor it via
  `--ftl-focus` or add a glow via `--ftl-focus-ring`.
- **`cue-lab`'s `* { box-shadow: none !important }`** also erased
  `.ftl-table tr.is-active`'s row marker. "Flat" is now expressed by
  leaving shadow properties unset; row states additionally carry a
  background so no single language is load-bearing.
- **Contrast failures** in `aqua` (primary), `cue-lab` (danger) and `lcars`
  (danger) — palettes adjusted to clear 4.5:1.
- **Core's achromatic fallbacks**: were the blue-future palette, so a theme
  with a missing token inherited a plausible-looking dark navy that went
  invisible on light themes. Now obviously-wrong grays.

### Added

- `scripts/check.sh` — contract lint (token completeness, the variant rule,
  focus indicators, universal `!important`, contrast floors, stale `dist/`,
  manifest sync), run in CI by `.github/workflows/ci.yml`. Every rule maps
  to a bug in the "Fixed" list above.
- `dist/themes.json` — machine-readable theme index, so apps and `demo.html`
  stop hardcoding or scraping the theme list.
- **htmx state styling**: `.ftl-indicator`, plus `.htmx-request`,
  `.htmx-swapping`, `.htmx-added` and `.htmx-settling` treatments, themeable
  per theme. Previously every consuming app would have hand-rolled this.
- **New components**: `.ftl-modal-overlay` (was left to each app to
  reinvent), `.ftl-tabs`/`.ftl-tab`, `.ftl-label`/`.ftl-field`/
  `.ftl-field-hint`, `.ftl-textarea`, `.ftl-toolbar`, `.ftl-panel-header`,
  and the `.ftl-mono` tabular-numerals utility.
- Six new themes: `windows95`, `matrix`, `tron`, `aqua`, `winamp-classic`,
  `wmp11`.
- `demo.html` now builds its switcher from the manifest, exercises every
  component including htmx states, and has a `?chrome=1` mode that renders
  the LCARS chrome primitive.
- `docs/theme-backlog.md`, `docs/lcars-chrome.md`, `docs/authoring-a-theme.md`,
  `scripts/new-theme.sh`.
- `color-mix()` uses are now behind `@supports` with flat-color fallbacks.

### Known issues

- `windows95`'s body text on its teal *page backdrop* is 4.4:1 (the lint
  warns). Text in that theme sits on `#c0c0c0` panels at 11.5:1; the teal is
  a decorative desktop color that carries no body text, which is why this is
  a warning rather than a failure.
- `windows95` and `tron` name reference fonts (MS Sans Serif, Eurostile)
  that aren't web-available and fall back. Vendoring open substitutes is
  tracked in `docs/theme-backlog.md`.
