# Migrating from v4 to v5

v5 keeps the v4 token contract, the `@layer ui` bundles, the L0/L1 adoption
levels and every theme slug. Class names and custom properties are **not**
renamed, so there is no codemod. What changes is layout and sizing: the shell
gains screen tiers, controls grow to touch size on phones and tablets, and
controls keep the arrow cursor. Re-check your app at a phone width and at a
wide-screen width after upgrading. The last v4 release is the `v4` branch
(v4.1.0); pin it if you cannot upgrade yet.

## What changed

| Area | v4 | v5 |
|---|---|---|
| Shell breakpoints | One small-screen breakpoint at 720px | Four tiers: mobile (≤480px), tablet (481–900px), desktop (901–1800px), xl (1801px+). `--tier` reports the current one. |
| Small-screen shell tokens | `--app-areas-sm`, `--app-rows-sm`, `--app-rail-display-sm`, `--app-main-padding-sm` | `-mobile` and `-tablet` versions of each. The `-sm` tokens still work as the fallback for both. |
| Wide screens | `.app` grows to the full window | `.app` stops at `--app-max` (1800px) and centres; the theme's gutter art fills the sides |
| Touch | Controls use the theme's own sizes | Every control's hit area is at least `--tap-min`: 44px on mobile and tablet tiers, on a coarse pointer, or with `html[data-pointer="touch"]`; 24px otherwise |
| Cursor | Buttons and links switch to the hand pointer | Controls keep the arrow; hover and focus states carry the affordance |
| Popovers and menus | `.context-menu` made of buttons; dropdowns could be clipped by a scrolling parent | `ul.context-menu[popover]` with nested `ul` submenus, in the top layer. The button form still works but is deprecated. |
| Stacking | Ad hoc `z-index` values | A `--z-*` scale in core |
| Components | – | Container queries (`container-type`) on several components, so they adapt to their panel instead of the window |
| Theme switching | `theme-loader.js` swaps the stylesheet | The swap runs in a view transition when motion is allowed |
| Manifest | `"contract": 4` | `"contract": 5` |

New in v5 and opt-in (nothing to migrate): the component groups in
`core/components/` (forms, instruments, navigation, surfaces, tables,
experience, social, media, planner, HUD, prose), the accessibility attributes
and `.prefs` panel, CSS-only tabs and selection, page templates, themed
emails and `schedule.js`. See CHANGELOG.md and `docs/components/`.

## What to check in your app

1. **Your own small-screen overrides.** If you wrote
   `@media (max-width: 720px)` rules around the shell, they now fire inside
   the tablet tier. Move them to the tier tokens (`--app-areas-tablet`,
   `--app-areas-mobile`, …) or to the tier widths above.
2. **Fixed heights around controls.** Buttons, tabs, nav items and menu
   items are at least 44px tall on phones and tablets. A toolbar or table
   row with a fixed pixel height may clip them.
3. **The 1800px cap.** An app that needs the full window width on a large
   monitor sets `--app-max: none` on `.app`.
4. **The hand cursor.** If your own CSS relied on core setting
   `cursor: pointer`, it no longer does. Your unlayered CSS can still set it.
5. **Positioning inside panels.** Components that are now containment
   contexts change what `position: fixed` and container units resolve
   against inside them. Check anything you position relative to the
   viewport from inside a card, panel or table.
6. **Button-based context menus.** They keep working. Move to the `ul` form
   when convenient to get submenus and top-layer placement (CONTRACT.md,
   "Floating surfaces, menus and nesting").
7. **Manifest consumers.** Code that checks `contract === 4` in
   `dist/themes.json` should accept 5.

## Upgrade

```sh
git submodule update --remote third_party/ftl-themes   # or however you pin it
git -C third_party/ftl-themes checkout v5.0.0
```
