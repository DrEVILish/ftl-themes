# Prose, code and template pieces (v5)

Markdown and CMS output, a library-neutral code palette, GitHub-style
callouts, and the small components the page templates need (PLAN.md §22).

- CSS: `core/components/prose.css` (in every `dist/<slug>.css` bundle)
- Example: `components-prose.html`; templates: see [`docs/templates.md`](../templates.md)
- No JavaScript and no highlighting library ships. Apps run Prism,
  highlight.js or Shiki themselves (at build time or in the browser) and
  load none of their theme CSS: the theme colours the class names.

---

## Prose (`.prose`)

```html
<article class="prose">
  <h1>Calling a show</h1>
  <p>…</p>
  <!-- anything a Markdown renderer writes, with no classes -->
</article>
```

Styled inside `.prose` with no classes: `h1`–`h6`, paragraphs, links
(underlined, so colour isn't the only signal), `strong`/`em`, inline `code`,
`kbd` (core), `mark`, `abbr[title]` (dotted underline), `del`/`ins`,
`sup`/`sub` (no line-height jump), nested `ul`/`ol` (disc → circle → square,
decimal → alpha → roman), GitHub task lists, `blockquote`, `dl`, `hr`,
`img`/`video`, `figure` + `figcaption`, `table`, `details`/`summary`, code
blocks, footnotes and callouts.

**Measure and breakouts.** Every top-level child is capped at
`--prose-measure` (70ch). `pre`, `figure`, `.code-block`, `.table-wrap`,
`video`, `iframe` and a paragraph holding only an image (how Markdown
writes `![alt](src)`) run to `--prose-wide` (default: the container's
width). Text is start-aligned; `.prose.is-centered` centres the column and
the wide blocks.

**Rhythm.** Siblings are spaced by `--prose-flow` (`--space-m`); `h1`/`h2`
get `--space-2xl` above, `h3`/`h4` `--space-xl`, `h5`/`h6` `--space-l`, and
the block after any heading `--space-xs`. `hr` gets `--space-xl` both sides.
All of these come from the `--space-*` scale, so the rhythm tightens on
phones and opens up on XL.

**Headings.** Sizes (`--prose-h1-size` … `--prose-h6-size`: 2, 1.5, 1.25,
1.1, 1, 0.9em) outrank a theme's global heading rule (`:root .prose h2`),
so the hierarchy holds even in a theme that draws every `h2` as a small
label. Case, tracking and colour stay the theme's. A theme styles prose
headings with `html[data-theme="x"] .prose h2 { … }`.

**Tables** need no wrapper: a `.prose table` is `display: block`, as wide as
its content up to the container, and scrolls sideways when its cells can't
wrap any further. Chromium and Firefox keep table semantics on a
`display: block` table; WebKit has historically dropped them. **When your
renderer can wrap tables, use `<div class="table-wrap"><table>`**, which
keeps `display: table`. Cells read the core `.table` tokens
(`--table-head-bg/-fg/-rule/-transform/-tracking`, `--table-rule`) and
honour `align="center|right"`.

**Footnotes** as GitHub (`section[data-footnotes]`, `.sr-only` heading),
markdown-it-footnote (`.footnotes`, `hr.footnotes-sep`) and Pandoc
(`[role="doc-endnotes"]`, `a[role="doc-noteref"]`) write them: a rule above,
smaller muted text, and the targeted note or reference highlighted with a
tint and a dashed outline.

| Token | Default |
|---|---|
| `--prose-measure` / `--prose-wide` | `70ch` / `none` |
| `--prose-font-size` / `--prose-leading` / `--prose-fg` | `1rem` / `1.65` / inherit |
| `--prose-flow` / `--prose-heading-gap` | `--space-m` / `--space-xs` |
| `--prose-h2-space` / `--prose-h3-space` | `--space-2xl` / `--space-xl` |
| `--prose-h1-size` … `--prose-h6-size` | `2em` … `0.9em` |
| `--prose-heading-leading` | `1.25` |
| `--prose-list-indent` / `--prose-list-gap` / `--prose-marker` | `1.6em` / `--space-2xs` / `--muted` |
| `--prose-quote-rule` / `--prose-quote-rule-width` / `--prose-quote-fg` | `--border` / `3px` / `--muted` |
| `--prose-rule` | `--hairline` (hr, footnote rule) |
| `--mark-bg` / `--mark-fg` | warning at 35% / inherit |
| `--prose-media-radius` | `--radius` |
| `--prose-details-border` / `--prose-details-bg` / `--prose-details-glyph` | `--border` / transparent / `"▸"` |
| `--prose-target-bg` | accent at 16% |

**Touch and accessibility.** Links in running text are exempt from the
target size (WCAG 2.5.8); `summary` reaches `--tap-min`. Code blocks and tables
scroll sideways, so give them `tabindex="0"` (or the `.table-wrap`) so
keyboard users can scroll them; Chromium already focuses scrollers, other
engines don't. Glyphs drawn with `content` carry
an empty alt text (`/ ""`).

---

## Code palette

Library-neutral, like the chart contract: themes set colours, any
highlighter's output picks them up. Nothing is bundled.

| Token | Default | Prism | highlight.js | Shiki (`css-variables`) |
|---|---|---|---|---|
| `--code-keyword` | `--accent-text` | `keyword`, `atrule`, `important`, `rule` | `hljs-keyword`, `-doctag`, `-meta` | `--shiki-token-keyword` |
| `--code-string` | `--success-text` | `string`, `char`, `attr-value`, `regex`, `url` | `hljs-string`, `-regexp`, `-char`, `-link` | `--shiki-token-string`, `-string-expression`, `-link` |
| `--code-comment` (+ `--code-comment-style`: italic) | `--muted` | `comment`, `prolog`, `doctype`, `cdata` | `hljs-comment`, `-quote` | `--shiki-token-comment` |
| `--code-number` | `--warning-text` | `number`, `boolean`, `constant`, `symbol`, `entity` | `hljs-number`, `-literal`, `-symbol`, `-bullet` | `--shiki-token-constant` |
| `--code-function` | accent-2 mixed 60% into `--text` | `function` | `hljs-title`, `-section` | `--shiki-token-function` |
| `--code-type` | `--flare` mixed 55% into `--text` | `class-name`, `builtin` | `hljs-type`, `-built_in`, `-title.class_` | – |
| `--code-punctuation` | `--muted` mixed 55% into `--text` | `punctuation`, `operator` | `hljs-punctuation`, `-operator`, `-tag` | `--shiki-token-punctuation` |
| `--code-tag` | `--danger-text` | `tag`, `selector` | `hljs-name`, `-selector-tag` | – |
| `--code-attr` | accent mixed 50% into `--text` | `attr-name`, `property` | `hljs-attr`, `-attribute`, `-property`, `-selector-class/-id/-attr/-pseudo` | – |
| `--code-variable` | the block's text colour | `variable`, `parameter` | `hljs-variable`, `-template-variable`, `-params`, `-subst` | `--shiki-token-parameter` |
| `--code-inserted` / `--code-inserted-bg` | `--success-text` / success at 14% | `inserted` | `hljs-addition` | `.line.diff.add` |
| `--code-deleted` / `--code-deleted-bg` | `--danger-text` / danger at 14% | `deleted` | `hljs-deletion` | `.line.diff.remove` |

A theme with a dark `--code-block-bg` on a light page must also set
`--code-block-fg` and the `--code-*` colours: the defaults are tuned for
`--surface`.

Defaults are the semantic text colours (which `check.py` holds at 4.5:1 on
`--surface`) or a hue mixed towards `--text`, which can only raise its
contrast. The rules sit in `@layer ui`, so if an app *does* load a
Prism/hljs theme, that unlayered CSS wins. Shiki: use its `css-variables`
theme; core maps `--shiki-foreground` (`--code-block-fg`, default `--text`), `--shiki-background` and every
`--shiki-token-*` onto the palette on `pre.shiki`.

Also: `--code-block-fg` (pre text, default inherited), `--code-pad` (pre padding, `--space-m` × density), `--code-tab-size`
(2), `--code-block-font-size` (0.875em), `--code-leading` (1.6), and the core
`--code-bg/-fg`, `--code-block-bg/-border`.

### Lines, line numbers, highlights and diffs

```html
<pre class="shiki css-variables line-numbers"><code>
<span class="line">…</span>
<span class="line highlighted">…</span>
<span class="line diff add">…</span>
<span class="line diff remove">…</span>
</code></pre>
```

- **Lines** (`.line` from Shiki, `[data-line]` from rehype-pretty-code, and
  the diff spans of hljs and Prism) become full-width strips that bleed into
  the padding, so tints reach both edges.
- **Line numbers:** `.line-numbers` on the `pre` (Prism's class name) or
  `data-line-numbers` on the `code` (rehype-pretty-code) numbers the line
  spans with a CSS counter (`--code-gutter` 3ch, `--code-line-number`
  `--muted`). Prism's own plugin markup (`.line-numbers-rows`) is styled too.
  Numbers are generated content, so they never copy.
- **Highlighted lines:** `.line.highlighted` (Shiki), `.line.is-highlighted`,
  `[data-highlighted-line]` (rehype-pretty-code), and Prism's
  `.line-highlight` boxes: a tint plus a start-edge bar
  (`--code-highlight-bg`, `--code-highlight-bar`, `--code-highlight-bar-width`).
- **Diffs:** hljs and Prism diffs keep their own `+`/`-`; Shiki's notation
  removes them, so core draws `+`/`−` in the padding band. `.has-focused`
  dims every line but `.focused`.

### Code block with a header and copy button

```html
<figure class="code-block">
  <figcaption class="code-block-header"><span>standby.ts</span>
    <button class="btn btn-sm btn-clear code-copy" type="button">
      <svg class="icon" aria-hidden="true"><use href="…#icon-copy"/></svg>
      <span>Copy</span><span aria-live="polite">Copied</span>
    </button></figcaption>
  <pre><code class="language-ts">…</code></pre>
</figure>
```

The app copies the text and sets `.is-copied` (or `data-copied`) for a
moment; both labels share one grid cell, so the button never changes width.
rehype-pretty-code's `figure[data-rehype-pretty-code-figure]` and
`[data-rehype-pretty-code-title]` get the same look. Tokens:
`--code-block-header-bg` (`--surface-2`), `--code-block-header-fg`
(`--muted`). The button is a `.btn`, so it reaches `--tap-min`.

---

## Callouts (`> [!NOTE]` …)

```html
<div class="markdown-alert markdown-alert-warning">
  <p class="markdown-alert-title"><svg …></svg>Warning</p>
  <p>Renumbering cues during a run renumbers them for everyone.</p>
</div>
<blockquote data-callout="tip"><p class="callout-title">Tip</p><p>…</p></blockquote>
```

`.markdown-alert-note|tip|important|warning|caution` is what GitHub,
remark-github-blockquote-alert and markdown-it-github-alerts write;
`[data-callout]` (+ `.callout-title`) is the Obsidian/rehype-callouts form.
They work inside or outside `.prose`. A 4px start rule, a 9% tint and a
coloured title; the title word is the non-colour signal. Renderers that
don't support alerts leave `[!NOTE]` as text in a plain blockquote, which
CSS can't detect; it renders as a normal quote.

| Type | Rule / title colour | Tokens |
|---|---|---|
| note | `--accent` / `--accent-text` | `--callout-note`, `--callout-note-text` |
| tip (`success`) | `--success` / `--success-text` | `--callout-tip`, `--callout-tip-text` |
| important | `--accent-2` / accent-2 mixed into `--text` | `--callout-important`, `--callout-important-text` |
| warning | `--warning` / `--warning-text` | `--callout-warning`, `--callout-warning-text` |
| caution (`danger`) | `--danger` / `--danger-text` | `--callout-caution`, `--callout-caution-text` |

Shared: `--callout-bg`, `--callout-fg`, `--callout-rule-width` (4px),
`--callout-radius`.

---

## Template pieces

Used by the page templates; each is generic and documented with its
template in [`docs/templates.md`](../templates.md).

| Class | What | Tokens |
|---|---|---|
| `.master-detail` (+ `-list`, `-pane`, `-home`, `-back`, `.is-detail`) | List beside detail; drill-in at 480px or narrower; optional leading `.nav-rail` makes it three-pane | `--master-detail-list-width` (`minmax(14rem, 20rem)`), `--master-detail-gap` (`--space-m`) |
| `.otp` + `.otp-input` | One-time code in per-digit boxes, one real input | `--otp-length` (6), `--otp-cell-size` (2.75rem), `--otp-gap`, `--otp-height`, `--otp-radius`; reads `--input-*` |
| `.wizard` + `.wizard-step`, `.wizard-actions`; radios in `ol.steps` labels | Radio-driven setup wizard | the `--steps-*` tokens from navigation.css |
| `.pricing` + `[data-billing="monthly|annual"]` | CSS-only billing-period price swap | – |
| `.card.is-featured` | The highlighted plan | `--card-featured-border` (`--accent`), `--card-featured-ring-width` (2px) |
| `.panel.is-danger` | A danger zone | `--panel-danger-border` (`--danger`) |

Forced colours: callouts, highlighted/diff lines, OTP boxes and the
featured card map to system colours.

## Code inputs: width, groups and letters

- `.otp` now has its natural width anywhere (it is a container, so it had none): the
  cells at `--otp-cell-size` and their gaps, shrinking on narrow screens.
- **Grouped codes (XXXX-XXXX):** add an `<span class="otp-sep">` cell where the dash
  goes and count it in `--otp-length` (9); the app inserts the dash into the value as the
  user types. **`.otp.is-alnum`** upper-cases (pair it with `inputmode="text"` and
  `autocapitalize="characters"`).
- **Pasting:** with `maxlength="6"` a pasted "123 456" is cut to "123 45" before any
  script sees it. Leave room in `maxlength` (or drop it) and strip separators on `input`.
