# Page templates (v5)

Six ready pages an app can copy (PLAN.md §22). Each is a plain HTML file at
the repo root using the full app shell (`.app` with bar, rail, main and
status), only library classes, and **no JavaScript** for anything HTML and
CSS can do: tabs and selection are radios, sections switch with radios,
accordions are `<details>`. Each passes the v5 audit (no overflow, touch
targets, spacing, edge text, XL cap) on `blue-future` at all five target
devices.

To use one: copy the file, keep `<link id="theme-link" href="dist/<slug>.css">`
(or your own theme link), delete the demo nav and theme picker, and replace
the content. The extra components they need live in
`core/components/prose.css` ([docs](components/prose.md#template-pieces)).

| Template | Shows | Built from |
|---|---|---|
| `auth.html` | Sign in, sign up, forgot password, two-factor code, check your email | `.tabset`, `.input-group` + `.input-icon`, `.check`, `.btn-brand`, `.otp`, `.empty-state`, `.field-error` |
| `settings.html` | Section nav (sidebar / drill-in), forms, switch rows, `.prefs`, danger zone | `.master-detail`, `.list`, `.field-row` + `.switch`, `.prefs`, `.panel.is-danger` |
| `master-detail.html` | Ticket list and ticket detail | `.master-detail`, two-line `.list-item`, `dl.props`, `.thread`/`.message` |
| `inbox.html` | Folders, message list, reading pane | `.master-detail` + `.nav-rail`, `.toolbar`, `.prose` message bodies |
| `onboarding.html` | Five-step setup wizard with back, skip and continue | `ol.steps` as a radio group, `.wizard`, `.dropzone`, `.radio-group` |
| `pricing.html` | Plan cards, highlighted plan, monthly/annual toggle, comparison table, FAQ | `.pricing` + `data-billing`, `.card.is-featured`, `.price`, `.feature-list`, `.table`, `.accordion-item` |

---

## `auth.html`

Every screen of a sign-in flow, side by side so each state can be checked
in every theme. In an app each card is its own page.

- **Sign in / Create account** share a `.tabset` (radio tabs). Leading icons
  sit inside the fields (`.input-icon`). "Forgot password?" is a
  `.btn-clear` link, so it is a full-size target. Brand buttons
  (`.btn-brand.is-google`, `.is-microsoft`) follow the companies' rules and
  are deliberately not themed.
- **Reset password** shows the invalid state (`aria-invalid` +
  `.field-error`).
- **Two-step verification** uses `.otp`: one real `<input>` whose digits are
  spaced onto six drawn boxes, so typing, paste, password managers and the
  OS one-time-code suggestion (`autocomplete="one-time-code"`) all work with
  no JS. `aria-invalid="true"` turns every box red (the wrong-code state is
  shown under it).

  ```html
  <div class="otp">
    <input class="otp-input" inputmode="numeric" autocomplete="one-time-code"
           maxlength="6" pattern="[0-9]{6}" aria-label="6-digit code">
    <span></span><span></span><span></span><span></span><span></span><span></span>
  </div>
  ```
  For another length, use that many spans and `style="--otp-length: 4"`.
  The boxes shrink to fit a narrow box (a container query on `.otp`); the
  digits stay at least 16px so iOS doesn't zoom. Focus shows on the boxes.
- **Check your email** is an `.empty-state` with resend and change-address
  actions.

## `settings.html`

A sidebar of sections beside the chosen section on wider screens; on a
phone the sections are a drill-in list (with chevrons) and the chosen
section covers it, with a Back button.

```html
<form id="settings-nav" hidden></form>
<div class="master-detail">
  <nav class="master-detail-list" aria-label="Settings sections"><ul class="list">
    <li><label class="list-item"><input type="radio" name="section" form="settings-nav">
      <input type="radio" name="section" form="settings-nav" class="master-detail-home" checked hidden>
      <svg class="icon">…</svg><span>Profile</span><svg class="icon">…chevron-right</svg></label></li>
    <li><label class="list-item"><input type="radio" name="section" form="settings-nav">…Account…</label></li>
  </ul></nav>
  <section class="master-detail-pane panel stack">
    <button class="btn btn-ghost btn-sm master-detail-back" type="reset" form="settings-nav">Settings</button>
    …
  </section>
  <section class="master-detail-pane panel stack">…</section>
</div>
```

How it works (the same in master-detail and inbox):

- Item *n* shows pane *n* (up to 12). The panes keep their own display, so
  a pane can be a `.stack` or a grid.
- The hidden `.master-detail-home` radio is the "list" state. It sits in
  item 1, so on a wide screen item 1 is selected and pane 1 shows by
  default; on a phone (the `.master-detail` box 480px wide or less) the list
  shows until an item is picked.
- **Back** is a real `<button type="reset">` for the nav radios' own empty
  form (`form="settings-nav"`), so it is focusable and announced as a
  button, restores the home radio, and resets nothing else on the page (the
  settings forms inside the panes are separate forms; never nest them).
  It only shows when the list drills in.
- The pane slides in on phones under full motion (`@starting-style`),
  and not under reduced motion.
- **Server-rendered apps** drop the radios: render the one pane, make each
  list row a link, add `.is-detail` to `.master-detail` on the detail URL,
  and make Back a link to the list URL.

Sections show forms with validation, `.field-row` switch rows, the `.prefs`
display panel from experience.css (live when `assets/js/prefs.js` is
loaded, as here), and a `.panel.is-danger` danger zone with the destructive
action in `.btn-danger`.

## `master-detail.html`

A support queue: two-line list rows (`.list-item-title` + `.list-item-meta`
with a `.status`) beside the ticket (`dl.props`, a `.thread`, a reply form).
Same mechanism as settings. Width of the list column:
`--master-detail-list-width` (default `minmax(14rem, 20rem)`).

## `inbox.html`

Three panes: a `.nav-rail` of folders in front of the `.master-detail`.

| Width | Layout |
|---|---|
| Desktop and XL | Folder rail with labels, message list, reading pane. |
| Tablet (up to 900px) | The rail goes icon-only (navigation.css; labels stay as accessible names), list and reading pane side by side. |
| Phone (box 480px or narrower) | Icon rail and list; opening a message covers both, with Back. |

Folders are links (`aria-current="page"` on the open one). The reading pane
is a `.prose` body, so HTML email content (lists, quotes, tables) is styled
with no classes. The reply/forward/archive/delete buttons are labelled icon
buttons with tooltips.

## `onboarding.html`

`ol.steps` from navigation.css whose step labels are a radio group:

```html
<div class="card wizard">
  <ol class="steps" aria-label="Setup steps">
    <li><label><input type="radio" name="setup-step" id="step-1" checked>Workspace <small>Name and URL</small></label></li>
    <li><label><input type="radio" name="setup-step" id="step-2">Your show</label></li>
    …
  </ol>
  <section class="wizard-step">…
    <div class="wizard-actions">
      <label class="btn btn-clear push" for="step-5">Skip setup</label>
      <label class="btn btn-primary" for="step-2">Continue</label>
    </div>
  </section>
  …
</div>
```

- The checked step is current; every step before it shows as done (tick,
  filled line), using the same `--steps-*` tokens and glyphs as `.is-done`
  and `aria-current="step"`. `.wizard-step` *n* shows for step *n* (up to 8).
- Each step label covers its marker and reaches `--tap-min`, so tapping a
  marker jumps to that step. The steps stack vertically on phones.
- Back, Skip and Continue are `<label for>` shortcuts for pointer users;
  keyboard and screen-reader users move through the steps as a radio group
  (Tab to it, arrow keys). In an app, Continue is a submit button that saves
  the step and the server renders the next one with `aria-current="step"`.

## `pricing.html`

- **Billing toggle:** a `.segmented` radio pair (`value="monthly"` /
  `value="annual"`) inside `.pricing`. Every pair of
  `[data-billing="monthly"]` / `[data-billing="annual"]` siblings shares one
  grid cell; the inactive one is `visibility: hidden` (so it is out of the
  accessibility tree too) and nothing moves when the period changes. Inside
  a table cell, wrap the pair in a `<span>`.
  ```html
  <div class="price"><span data-billing="monthly">$49<span class="price-period">/mo</span></span>
    <span data-billing="annual">$39<span class="price-period">/mo</span></span></div>
  ```
- **Highlighted plan:** `.card.is-featured` (an accent ring) with a visible
  "Most popular" badge, so colour isn't the only signal.
- **Comparison table:** `.table-wrap > .table.is-striped` with row headers;
  "not included" is a dash with a visually hidden "Not included".
- **FAQ:** `details.accordion-item` with a shared `name`, so one is open at
  a time.
