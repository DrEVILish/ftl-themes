# Desktop shell (v5)

Source: `core/components/desktop.css`. Example page: `desktop.html`.
Covers PLAN.md §23 "Signature navigation per theme" for the desktop and
home-screen themes.

One markup that each theme draws as its own operating-system shell: a
wallpaper with desktop icons, windows that open, minimize, maximize, close
and come to the front, and a bar with a Start menu, task buttons and a
tray. No JavaScript. Every state is a radio or checkbox read with `:has()`,
and the Start menu is a popover holding the same nested lists as any menu.

The fullest example is [`gallery.html`](../../gallery.html): eleven windows,
a two-column Start menu, tray popovers, a boot screen and a logon screen.

Shared conventions:

- The shell reuses the app shell: `body.app.desktop`, `main.app-main.desktop-screen`
  and `footer.app-status.taskbar.desktop-bar`. The page header stays the page header
  (on Aqua it becomes the menu bar).
- Windows are the [window pattern](../../CONTRACT.md) (`.modal` with `.modal-header`,
  `.btn-min` / `.btn-max` / `.btn-close`), so every theme's title bar and caption
  buttons apply as they are.
- The task bar is core's `.taskbar` (`.taskbar-start`, `.taskbar-task`, `.taskbar-tray`)
  and reads the `--taskbar-*` tokens the desktop themes already set.
- Every colour and size is a `--desktop-*`, `--window-*`, `--start-menu-*`, `--dock-*`
  or `--home-*` token with a fallback, set by themes at root scope.

---

## Arrangement: `--desktop-shell`

| Value | Looks like | Set by |
|---|---|---|
| `taskbar` (default) | Start button, Quick Launch, task buttons and tray along the bottom; icons down the left. | `windows95`, `winxp-luna`, `win7-aero`, every theme that sets nothing |
| `dock` | The page header is the menu bar: the Start button becomes a mark at its left end (the Start menu is its first menu) and the tray its right end. Icons run down the right edge; the bottom is a Dock that magnifies under the pointer, with a mark under each running app. Windows lose their menu bars. | `aqua` |
| `home` | A touch home screen: an icon grid with page dots, a Dock of four launchers, the tray as a status bar on top, and one app at a time filling the screen (a centred sheet on wide screens), with a home indicator to go back. | `ios-flat`, `ios-skeuomorphic` |

The component reads the token with container style queries. **Every theme switches
to `home` on the Mobile tier (≤ 480px)**; a `taskbar` theme keeps its Start button
there. Browsers without style queries keep the `taskbar` arrangement, which is laid
out to stay usable at any width.

---

## Markup

```html
<body class="app desktop">
  <header class="app-bar">…</header>
  <main class="app-main desktop-screen">
    <input type="radio" class="desktop-home" name="desk-app" id="app-home" checked aria-label="Show the desktop">

    <div class="desktop-icons" role="radiogroup" aria-label="Desktop icons">
      <div class="desktop-icon">
        <label><input type="radio" name="desk-icon"><svg class="icon" aria-hidden="true"><use href="…#icon-device-desktop"/></svg><span>My Computer</span></label>
        <label class="desktop-icon-open" for="open-computer"></label>
        <label class="desktop-icon-launch" for="app-computer"></label>
      </div>
      <div class="desktop-icon is-trash">…Recycle Bin…</div>
    </div>
    <div class="desktop-pages" aria-hidden="true"><span class="is-active"></span><span></span></div>

    <section class="desktop-window" aria-label="My Computer" style="--x: 9rem; --y: 1.5rem; --w: 36rem; --h: 23rem">
      <input type="radio" class="window-app" name="desk-app" id="app-computer" aria-label="Switch to My Computer">
      <input type="radio" class="window-open" name="vis-computer" id="open-computer" checked aria-label="My Computer: open">
      <input type="radio" class="window-minimize" name="vis-computer" id="min-computer" aria-label="My Computer: minimized">
      <input type="radio" class="window-close" name="vis-computer" id="closed-computer" aria-label="My Computer: closed">
      <input type="checkbox" class="window-max" id="max-computer" aria-label="Maximize My Computer">
      <div class="modal" role="dialog" aria-labelledby="title-computer" tabindex="-1">
        <div class="modal-header">
          <svg class="icon" aria-hidden="true">…</svg>
          <span class="window-title" id="title-computer">My Computer</span>
          <label class="btn-min" for="min-computer"><span class="visually-hidden">Minimize</span></label>
          <label class="btn-max" for="max-computer"><span class="visually-hidden">Maximize</span></label>
          <label class="btn-close" for="closed-computer"><span class="visually-hidden">Close</span></label>
        </div>
        <ul class="menubar" role="menubar">…</ul>
        <div class="window-body">… <div class="window-pane">…</div> …</div>
        <!-- or, with a task pane beside the content: -->
        <div class="window-body"><aside class="window-tasks" aria-label="Tasks">
            <section class="window-task is-special"><h2>System Tasks</h2><ul>…</ul></section>
            <section class="window-task"><h2>Other Places</h2><ul>…</ul></section>
          </aside><div class="window-pane">…</div></div>
        <div class="window-status"><span>6 object(s)</span><span>1.2 GB free</span></div>
        <label class="window-home" for="app-home"><span class="visually-hidden">Home</span></label>
      </div>
    </section>
  </main>

  <footer class="app-status taskbar desktop-bar">
    <button class="taskbar-start" popovertarget="start-menu"><svg class="icon" aria-hidden="true">…#icon-grid</svg><span class="taskbar-start-label">Start</span></button>
    <div class="start-menu" popover id="start-menu" aria-label="Start menu">
      <div class="start-menu-header"><span class="avatar">AL</span><span>Ada Lovelace</span></div>
      <ul class="context-menu start-menu-programs" role="menu">
        <li role="none" class="is-columns-only">…pinned…</li>
        <li role="none" class="has-submenu start-menu-all"><button role="menuitem" aria-haspopup="menu">…<span class="is-columns-only">All </span>Programs</button>
          <ul role="menu">…nested submenus…</ul></li>
      </ul>
      <ul class="context-menu start-menu-places" role="menu">…</ul>
      <ul class="context-menu start-menu-footer" role="menu">…</ul>
    </div>
    <nav class="desktop-dock" aria-label="Quick launch and open windows">
      <ul class="desktop-launchers"><li><a class="dock-item" href="…"><svg class="icon">…</svg><span>Mail</span></a></li>…<li class="is-trash">…</li></ul>
      <ul class="taskbar-tasks">
        <li><label class="taskbar-task" for="app-computer">…My Computer</label><label class="taskbar-restore" for="open-computer"><span class="visually-hidden">Restore My Computer</span></label></li>
      </ul>
    </nav>
    <div class="taskbar-tray" data-audit-edge="ignore">…icons… <svg class="icon is-battery">…</svg> <time>9:41 AM</time></div>
  </footer>
</body>
```

---

## States

- **Window visibility.** Each window has its own radio group: `.window-open`,
  `.window-minimize`, `.window-close`. Minimized and closed windows hide their
  `.modal`; the inputs stay, so a task button or a Start menu item (a `<label>` for
  `.window-open`) brings them back.
- **Switched-to window.** `.window-app` radios share one name across every window and
  `.desktop-home`. The checked one comes to the front, draws the active title bar and
  presses its task button; in the `home` arrangement it is the open app. The task
  button is a label for it.
- **Focus.** A window holding focus (`.modal` has `tabindex="-1"`, so any click in it
  counts) comes to the very front and is the active one. With nothing focused or
  switched to, the last window in the markup is active, as it is topmost.
- **Inactive windows** draw `--window-header-bg-inactive` / `-fg-inactive` and
  `--window-header-filter-inactive` (a desaturate by default).
- **Maximize.** The `.window-max` checkbox immediately before the `.modal` (core's
  maximize rule); the window fills the screen.
- **Task buttons** pair with windows by position (window N, task N; up to 12): pressed
  for the active window, hidden for a closed one, and while a window is minimized its
  `.taskbar-restore` label covers the task button and restores it.
- **Desktop icons.** The radio selects; a selected icon shows `.desktop-icon-open`
  over itself, so a second click opens its window (a double-click without script). In
  the `home` arrangement `.desktop-icon-launch` opens it with one tap.
- **Start menu.** `--start-menu-layout`: unset is one column (header, programs, places,
  footer); `classic` turns the header into a vertical banner (`--start-menu-banner` is
  its text); `columns` puts programs and places side by side under the header and shows
  items marked `.is-columns-only` (`.is-classic-only` hides there). The Start button
  draws pressed while the menu is open. Submenus are core's nested menus.
- **`.is-trash`** marks the trash: a desktop icon in `taskbar`, the last Dock item
  (after a separator) in `dock`.

---

## Tokens

| Token | Default |
|---|---|
| `--desktop-shell` | `taskbar` (`dock`, `home`) |
| `--desktop-bg` | none (the page background) |
| `--desktop-min-height` | `30rem` |
| `--desktop-inset-top` / `--desktop-inset-bottom` | `0px` (room for bars floating over the screen) |
| `--desktop-icon-fg` / `--desktop-icon-text-shadow` | `--text` / none |
| `--desktop-icon-glyph` / `--desktop-icon-filter` | `--accent` / none |
| `--desktop-icon-glyph-selected` / `--desktop-icon-filter-selected` | the unselected values |
| `--desktop-icon-label-bg-selected` / `-fg-selected` / `--desktop-icon-label-radius` | `--accent` / `--on-accent` / `0` |
| `--desktop-icon-size` / `--desktop-icon-cell` / `--desktop-icon-row` / `--desktop-icon-font-size` | `2rem` / `5.75rem` / `5rem` / `0.8rem` |
| `--desktop-icons-justify` | `start` (`end` in `dock`) |
| `--window-icon-glyph` | `--accent` (icons inside windows) |
| `--window-pad` / `--window-header-pad` / `--window-body-pad` | `3px` / `--modal-header-pad` / `--space-s` |
| `--window-header-bg-inactive` / `--window-header-fg-inactive` / `--window-header-filter-inactive` | the active header / `saturate(.45) opacity(.85)` |
| `--window-caption-opacity-inactive` | `1` (an inactive window's min / max / close buttons) |
| `--window-status-field-border` | transparent (1–4 colours) |
| `--window-pane-bg` / `--window-pane-border` | `--input-bg` / `--input-border` |
| `--window-tasks-bg` / `--window-tasks-gap` / `--window-tasks-padding` | `--surface-2` / `--space-s` / `--space-s` (the task pane) |
| `--window-task-bg` / `-fg` / `-border` / `-radius` / `-body-pad` / `-link-fg` | `--surface` / `--text` / `--border` / `--radius` / `0.4rem 0.6rem` / `--link` |
| `--window-task-font-size` | inherit |
| `--window-task-link-fg-hover` / `--window-task-item-pad` | the link colour (underlined on hover) / `0.2em 0` (a `.list` in a group loses its box) |
| `--window-task-header-bg` / `-header-fg` / `-header-pad` / `-header-font-size` | transparent / inherit / `0.35rem 0.6rem` / `0.85rem` |
| `--window-task-special-bg` / `-special-header-bg` / `-special-header-fg` | the plain group's values (`.window-task.is-special`) |
| `--taskbar-height` / `--taskbar-padding` / `--taskbar-gap` / `--taskbar-font-size` | `2.5rem` / `0.2rem 0.3rem` / `0.3rem` / `0.85rem` |
| `--taskbar-task-max` / `--taskbar-task-weight-active` | `10.5rem` / inherit |
| `--taskbar-start-bg-open` / `-border-open` / `-shadow-open` / `-outline-open` | the closed values |
| `--desktop-launchers-display` / `--desktop-launchers-rule` | `flex` / `--hairline` |
| `--start-menu-layout` | unset (`classic`, `columns`) |
| `--start-menu-bg` / `-border` / `-border-width` / `-radius` / `-shadow` | the `--context-menu-*` values |
| `--start-menu-header-bg` / `-header-fg` / `-header-radius` | transparent / inherit / `0` |
| `--start-menu-banner` / `-banner-bg` / `-banner-fg` | `""` / `--accent` / `--on-accent` |
| `--start-menu-programs-bg` / `-places-bg` / `-footer-bg` / `-footer-fg` / `-rule` | transparent / … / `--hairline` |
| `--start-menu-icon-size` / `-sub-icon-size` / `-font-size` | `1.25rem` / `1rem` / `0.9rem` |
| `--desktop-menubar-height` / `--desktop-tray-room` | `1.6rem` / `8.5rem` (`dock`) |
| `--dock-bg` / `-border` / `-radius` / `-shadow` / `-blur` | translucent `--surface` / white rim / `0.6rem` / soft / `blur(8px)` |
| `--dock-icon-size` / `--dock-magnify` | `2.9rem` / `1.55` |
| `--dock-tile` / `--dock-tile-gloss` / `--dock-glyph` / `--dock-tile-radius` / `--dock-tile-shadow` | a `--chart-series-n` gradient per item / none / `--accent` / `22%` / soft |
| `--dock-indicator` / `-size` / `-radius` / `-shape` / `-glow` | `currentColor` / `0.35rem` / `50%` / none / none |
| `--dock-label-bg` / `--dock-label-fg` | dark / white |
| `--home-icon-size` / `--home-cell-min` / `--home-grid-max` | `3.6rem` / `4.5rem` / `36rem` |
| `--home-tile` / `--home-tile-gloss` / `--home-glyph` / `--home-tile-radius` / `--home-tile-shadow` | a `--chart-series-n` gradient per icon / none / white / `22%` / soft |
| `--home-label-fg` / `--home-label-shadow` / `--home-label-size` | the desktop icon values / `0.75rem` |
| `--home-dot` / `--home-dot-active` | faded / full icon colour |
| `--home-statusbar-bg` / `--home-statusbar-fg` | transparent / `--app-bar-fg` |
| `--home-dock-bg` / `--home-dock-icon-size` / `--home-dock-glyph` | `--dock-bg` / `3.1rem` / `--home-glyph` |
| `--home-sheet-max` / `--home-sheet-radius` / `--home-indicator` | none / `0` / `--text` |
| `--desktop-battery-display` | none (shown in `home`) |

Tile colours are composed per item from `--chart-series-1..6`, so a theme's own
data palette colours its app icons. Don't put `var(--_tile)` in a root token (it
resolves at the root, empty); use `--dock-tile-gloss` / `--home-tile-gloss` for a
colour-independent highlight, or `--dock-tile` / `--home-tile` for one look for all.

---

## Touch

- On the Mobile tier every theme uses the `home` arrangement: 44px targets, one app
  at a time, a bottom bar of launchers (plus Start for a `taskbar` theme), and core's
  nested menus expand inline in the Start menu, which scrolls within the screen.
- Window positions (`--x`, `--y`, `--w`, `--h`) are clamped to the screen, so the
  `taskbar` fallback never scrolls sideways.
- Dock magnification and its transition only run with `(hover: hover)` and
  `prefers-reduced-motion: no-preference` (and stop under `data-motion="reduced"`).

---

## Accessibility

- Desktop icons are a `role="radiogroup"` of radios (arrow keys move the selection).
- Each window is `role="dialog"` with `aria-labelledby` on its title. Its state radios
  are real, named inputs: Tab reaches the window's open/minimized/closed group (arrow
  keys change it) and the shared "switch to" group (arrow keys move between windows,
  like Alt+Tab). A focused state radio outlines its window.
- The Start menu lists are `role="menu"` with `role="none"` items; submenu triggers
  carry `aria-haspopup="menu"`. Items that open a window are labels for its radio;
  links and buttons stay links and buttons.
- Buttons drawn as icons carry visually hidden names; decorative icons are
  `aria-hidden`.
