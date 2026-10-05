# Local theme packs

Theme packs are local folders. They are validated and previewed without a
registry, account, or network request. The supported format is described by
[`theme-pack.schema.json`](theme-pack.schema.json).

```text
my-theme/
  manifest.json
  theme.css
  LICENSE.txt
  assets/ (optional)
```

Minimal manifest:

```json
{
  "formatVersion": 1,
  "name": "My Theme",
  "slug": "my-theme",
  "contract": 4,
  "minimumLibraryVersion": "5.1.0",
  "css": "theme.css",
  "assets": [],
  "license": {"name": "CC0-1.0", "notice": "LICENSE.txt"}
}
```

`manifest.json` declares `formatVersion: 1`, a lowercase `slug`, contract
version `4`, the minimum library version, CSS path, optional asset/icon paths,
variants, and a license name plus notice path. Keep theme rules under
`html[data-theme="<slug>"]`; assets must be pack-local and declared. Remote
imports, remote/data URLs, and paths escaping the pack are rejected.

Validate and write an HTML preview beside the pack:

```sh
python3 scripts/validate_theme_pack.py ./my-theme --preview
```

Open `my-theme/preview.html` in a browser. The preview uses the pack CSS,
this checkout's core bundle and small component examples; it does not install
the pack into the catalogue or share it with other users. Fonts, icons, and other third-party assets still need compatible
licenses and attribution in the notice file.
