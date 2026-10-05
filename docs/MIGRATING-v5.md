# Migrating to v5

v5 adds screen tiers and component behavior while retaining the v4 class and
token contract. The manifest continues to report `contract: 4`; that field is
the markup/token compatibility version, not the library release number.

## Check app-specific CSS

- Replace shell overrides based on the old 720px breakpoint with the mobile,
  tablet, desktop and XL tiers in [CONTRACT.md](../CONTRACT.md#screen-tiers-v5).
- Replace `--app-areas-sm` with `--app-areas-mobile` and
  `--app-areas-tablet` where you define shell areas.
- Check fixed-height layouts around controls. Touch layouts now target 44px
  minimum controls.
- Check content positioned against the viewport from inside panels; component
  containment can change containing-block behavior.
- Check pages that assumed `.app` always spans the viewport. Its width is
  capped at 1800px.

## Update deprecated or custom behavior

- Replace button-based `.context-menu` markup with the nested-list form when
  convenient. The button form remains supported in v5.
- Remove custom hand-cursor rules if they only duplicate the old library
  behavior. Controls use the arrow cursor; hover and focus styles communicate
  affordance.
- If your app swaps theme stylesheets directly, it continues to work; use
  `theme-loader.js` if you want its view-transition behavior.
- Compare related themes after upgrading. Shared theme-family bases can shift
  small visual details between family members.

No class or token was renamed or removed for this release. Apps that do not
override the affected layout behavior can adopt the rebuilt v5 bundles
without markup changes.
