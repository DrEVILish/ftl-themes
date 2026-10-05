# Repository instructions

## CSS before JavaScript

- When touching a JavaScript style, DOM action, transition or animation,
  first check whether HTML, modern CSS available at Baseline 2024, or a native
  browser feature can do the job. Prefer CSS for presentation and state; keep
  JS for data, app logic, persistence, or behavior CSS cannot express.
- Do not add JS to calculate layout already available through CSS media,
  container, or viewport features. A small JS bridge is appropriate only when
  app code needs a CSS result or browser-only metadata exposed as data.

## Versioning and releases

- Use semantic versions in `MAJOR.MINOR.PATCH` order. Determine the current
  release from the latest versioned heading in `CHANGELOG.md` and confirm it
  against Git tags when available. Do not infer the release number from a
  plan title, feature size, commit count, or the contract number.
- A patch release (`x.y.Z`) fixes defects or documentation without adding
  public capability. A minor release (`x.Y.0`) adds backward-compatible
  features, components, themes, or supported behavior. A major release
  (`X.0.0`) changes the public contract incompatibly, such as removing or
  renaming classes, tokens, or required integration behavior.
- “Major feature” describes scope, not the SemVer major digit. If the current
  major line is already established, ship compatible feature sets as the
  next minor release (for example, `5.1.0` to `5.2.0`). Never reset an active
  line to `5.0.0` because a feature set feels substantial.
- Keep the library release number separate from the theme contract version.
  `dist/themes.json`'s `contract` field and `CONTRACT` in
  `scripts/build_manifest.py` change only when markup/token compatibility
  changes. The manifest's `version` is a generated content hash; never set it
  to a SemVer string by hand.
- Update release-facing references together: the versioned `CHANGELOG.md`
  heading, `README.md`, `PLAN.md` release status when relevant, and any
  minimum-library-version examples or fixtures affected by new features.
  Keep a pack's `minimumLibraryVersion` at the oldest release that supports
  the pack's requirements, not automatically at the newest release.
- Before choosing a bump, record whether the change adds compatible public
  capability or breaks an existing contract, then apply the patch/minor/major
  rules above. Base a changelog heading's summary and date on what actually
  shipped, not the original plan or implementation start date.
- Keep unreleased notes under `## Unreleased`. At release, move the shipped
  notes under one newest-first `## vX.Y.Z — summary (YYYY-MM-DD)` heading and
  leave `Unreleased` ready for future work. Group notes under `Added`,
  `Changed`, `Fixed`, and `Removed` when that makes the changes easier to
  scan; omit empty groups. Describe user-visible effects and link migration
  guidance for breaking changes.
- Add or update a migration guide for breaking releases. Do not describe an
  additive minor release as breaking solely because it contains a large
  feature set.
- Rebuild generated distribution files with `scripts/build.sh`; do not edit
  `dist/` outputs by hand. Check the manifest contract field, generated
  component index, changelog, README and package/version examples for
  consistency before committing a release.
