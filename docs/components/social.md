# Collaboration and notifications (v5)

Source: `core/components/social.css`. Live examples: `components-social.html`.
Covers PLAN.md §19 "Collaboration" and "Notifications and activity": presence,
live cursors, comment threads, mentions, the typing indicator, the
notification centre and the activity feed.

Built on existing components rather than new ones wherever they fit:
core's `.avatar`, `.thread`/`.message`/`.message-reactions`, `.typing`,
`.badge-button`, `.list`, `.popover[popover]`, `.drawer[popover]`, `.tabset`,
`.switch`, `.empty-state`, `.input-group` and `.context-menu`; the forms
group's `.has-badge`, `.combobox` and `.listbox`; the instruments group's
`ol.timeline`.

Tokens are listed as `token: default`. Set them on `html[data-theme="x"]`
like every other component token.

Nothing on the example page uses JavaScript: the bell, the comment pins and
the avatar stack open popovers with `popovertarget`, the drawer is a popover,
tabs are a `.tabset`, reactions and do-not-disturb are checkboxes. Apps add
live data (positions, counts, read state).

---

## Per-user colours `data-color="1..6"`

One colour per person, used by their avatar, live cursor and comment pins.

```html
<span class="avatar" data-color="2">LP</span>
<span class="live-cursor" data-color="2" style="--x: 40%; --y: 30%" aria-hidden="true">Leo Park</span>
```

- `data-color="n"` sets `--user-color` from `--presence-color-n`.
- On an `.avatar` it tints the avatar (28% of the colour over `--surface`,
  text in `--text`).
- On a `.live-cursor` or `.comment-pin` the text on the colour is black or
  white, picked from the colour's lightness (CSS relative colour syntax;
  engines without it use `--live-cursor-fg`).

| Token | Default |
|---|---|
| `--presence-color-1` … `-6` | `--chart-series-1` … `-6` (accent, success, warning, danger, accent-2, muted) |
| `--live-cursor-fg` | `#fff` (fallback text on a user colour, old engines only) |

The chart palette is the default because every theme already keeps it
distinct. A theme whose chart palette is close in hue (e.g. a monochrome
theme) should set its own `--presence-color-*`.

## Status on an avatar `[data-status]`

```html
<span class="avatar" data-status="online">AT<span class="visually-hidden">, online</span></span>
<span class="presence-status" data-status="away">Away</span>
```

| `data-status` | Shape | Colour token (default) |
|---|---|---|
| `online` | filled disc | `--presence-online` (`--success`) |
| `away` | crescent | `--presence-away` (`--warning`) |
| `busy` | disc with a bar | `--presence-busy` (`--danger`) |
| `offline` | hollow ring | `--presence-offline` (`--muted`) |

Shapes differ, so colour is never the only signal. On an avatar the dot sits
on the bottom-end corner and stays above the next avatar in a stack (the
avatar's `overflow` becomes visible; an `<img>` inside keeps the avatar's
radius). `.presence-status` is the same shape before a text label.

| Token | Default |
|---|---|
| `--presence-dot-size` | `0.7rem` |
| `--presence-dot-ring` | `var(--surface)` (separating ring, and the crescent's cut-out) |
| `--presence-dot-ring-width` | `2px` |
| `--presence-status-fg` | `var(--muted)` |

**Accessibility:** the dot is drawn in CSS. Put the status in text too: a
`.visually-hidden` span inside the avatar, or `.presence-status` beside it.

## Presence stack `.presence`

```html
<!-- Opens who's viewing -->
<button class="presence" popovertarget="viewers"
        aria-label="6 people viewing: Ava Tran, Leo Park, Mia Chen and 3 more">
  <span class="avatar" data-color="1" data-status="online">AT</span>
  <span class="avatar" data-color="2" data-status="online">LP</span>
  <span class="avatar" data-color="3" data-status="away">MC</span>
  <span class="avatar presence-more">+3</span>
</button>
<div class="popover" popover id="viewers" aria-label="Who's viewing">
  <ul class="presence-list">
    <li><span class="avatar avatar-sm" data-color="1">AT</span>Ava Tran
        <span class="presence-status" data-status="online">Online</span></li>
    …
  </ul>
</div>

<!-- A picture with a label, opens nothing -->
<div class="presence" role="group" aria-label="3 people editing">
  <span class="avatar avatar-sm" data-color="4">SO</span>…
  <span class="presence-label" aria-hidden="true">3 editing</span>
</div>
```

- Avatars overlap by a quarter of their size (`.avatar-sm`/`.avatar-lg`
  follow), each ringed in the surface colour.
- `.presence-more` is the “+n” overflow avatar.
- The button form rings every avatar in the accent on hover, keyboard focus
  and while its popover is open (`aria-expanded="true"`), and keeps core's
  focus ring. The popover (`.presence-list` in a `.popover[popover]`) is the
  touch and keyboard path to the names, so no tooltip is needed; per-avatar
  `data-tooltip` still works for mouse users.

| Token | Default |
|---|---|
| `--presence-overlap` | `calc(var(--avatar-size) * 0.25)` |
| `--presence-ring` / `--presence-ring-width` | `var(--surface)` / `2px` |
| `--presence-ring-hover` | `var(--accent)` |
| `--presence-radius` | `999px` (focus ring shape of the button) |
| `--presence-more-bg` / `--presence-more-fg` | `var(--surface-2)` / `var(--text)` |
| `--presence-label-fg` | `var(--muted)` |

**Touch:** `button.presence` is at least `--tap-min` tall (44px on touch
tiers). **Accessibility:** give the button an `aria-label` that names the
count and the first people; initials alone are not a name.

## Live cursors `.collab-layer` + `.live-cursor`

```html
<div class="panel collab-layer">
  …the shared document…
  <span class="live-cursor" data-color="2" style="--x: 62%; --y: 30%" aria-hidden="true">Leo Park</span>
  <span class="live-cursor is-idle" data-color="5" style="--x: 74%; --y: 58%" aria-hidden="true">Jo</span>
</div>
```

- `.collab-layer` is the positioned box the app's coordinates are relative
  to (`position: relative`, `overflow: clip`, its own stacking context). Put
  it on the document surface itself (a `.panel`, a canvas wrapper).
- The app sets `--x`/`--y` (lengths or percentages of the layer). The arrow's
  tip is the point; the name label hangs below and to the right of it.
- `.is-idle`: faded arrow, neutral label (text stays readable).
- Movement eases over 120ms only with `prefers-reduced-motion:
  no-preference`; it stops under `data-motion="reduced"`/`"none"`.
- Cursors ignore the pointer (`pointer-events: none`).

| Token | Default |
|---|---|
| `--live-cursor-radius` | `var(--radius)` |
| `--live-cursor-shadow` | `0 1px 3px rgba(0,0,0,.35)` |
| `--live-cursor-outline` | `var(--surface)` (1px halo round the arrow) |
| `--live-cursor-idle-bg` / `-fg` | `var(--surface-2)` / `var(--text)` |
| `--live-cursor-idle-opacity` | `0.45` (the arrow) |

**Accessibility:** cursors are decoration; mark them `aria-hidden="true"` and
let the presence stack say who is here.

## Comment anchors and pins

```html
<p>We ship in <mark class="comment-anchor is-active">week 42</mark>.</p>
<mark class="comment-anchor is-resolved">annual discount</mark>

<!-- In a .collab-layer: positioned; its tail is the (x, y) point -->
<button class="comment-pin" data-color="1" style="--x: 30%; --y: 42%"
        popovertarget="thread-1" aria-label="Comment thread by Ava Tran, 3 comments"><span>3</span></button>
<button class="comment-pin is-resolved" popovertarget="thread-2" aria-label="Resolved comment by Leo Park"><span>LP</span></button>
<div class="popover" popover id="thread-1"><div class="thread">…</div></div>
```

| State | `mark.comment-anchor` | `.comment-pin` |
|---|---|---|
| idle | tint + dashed underline | user colour bubble |
| `.is-active` / `aria-current` (anchor), `.is-active` / `aria-expanded="true"` (pin) | stronger tint, solid underline | larger bubble, `--text` ring, raised |
| `.is-resolved` | no tint, muted underline | neutral grey bubble with a border |

Outside a `.collab-layer`, `.comment-pin` is an inline button (a margin
rail, a table cell). Its hit area is `--tap-min` square whatever the drawn
size; keyboard focus draws core's focus colour round the bubble.

| Token | Default |
|---|---|
| `--comment-anchor-bg` / `-bg-active` | 22% / 40% `--warning` over transparent |
| `--comment-anchor-line` | `var(--warning-text, var(--warning))` |
| `--comment-pin-size` | `1.6rem` (`2rem` when active) |
| `--comment-pin-radius` | `50% 50% 50% 0` (speech bubble; square themes can set `0 0 0 0`) |
| `--comment-pin-bg` / `-fg` | `var(--accent)` / `var(--on-accent)` (no `data-color`) |
| `--comment-pin-ring` / `-ring-active` | `var(--surface)` / `var(--text)` |
| `--comment-pin-shadow` | `0 1px 3px rgba(0,0,0,.4)` |
| `--comment-pin-resolved-bg` / `-fg` | `var(--surface-2)` / `var(--muted)` |

## Comment thread `details.comment-thread`

```html
<details class="comment-thread is-active" open>
  <summary class="comment-thread-summary">
    <span class="comment-thread-quote">“week 42, after the freeze lifts”</span>
    <span class="comment-thread-count">3 comments</span>
  </summary>
  <div class="thread">
    <div class="message"><span class="avatar" data-color="1">AT</span>
      <div class="message-bubble">
        <div class="message-meta"><strong>Ava Tran</strong> <time datetime="…">10:02</time></div>
        <p>Can we move this? <a class="mention" href="/u/leo">@Leo Park</a></p>
        <div class="message-reactions">
          <label class="badge badge-button"><input type="checkbox" checked><span aria-hidden="true">👍</span> 2<span class="visually-hidden"> people agree; you reacted</span></label>
        </div>
      </div></div>
    <div class="message is-reply"><span class="avatar" data-color="2">LP</span>…</div>
    <div class="typing">Leo is typing…</div>
  </div>
  <form class="comment-thread-footer">
    <div class="input-group"><input class="input" aria-label="Reply" placeholder="Reply…"><button class="btn btn-primary">Reply</button></div>
    <button class="btn btn-ghost" type="button">Resolve</button>
  </form>
</details>
```

- **Collapsed:** the `<details>` closed: only the summary (quote + count).
- **Resolved:** `.is-resolved` dashes the border, strikes the quote and
  greys its rule. Put `<span class="badge badge-success">Resolved</span>` in
  the summary so the state is in text. Usually also closed.
- **Active** (its pin or anchor is selected): `.is-active` draws an accent
  border.
- Messages are core's `.message`; inside a thread their bubbles drop fill
  and border (comments read as a list, not a chat). `.message.is-reply`
  indents a reply under the root and shrinks its avatar. `.message.is-reply`
  also works in any `.thread`.
- **Reactions** are core's `.badge-button` in `.message-reactions`. A hidden
  checkbox inside makes one toggle with no script (the build maps its
  `:checked` onto `.is-active`); `aria-pressed="true"` on a `<button>` works
  too.
- Keep buttons out of `<summary>` (interactive content there is invalid);
  actions live in `.comment-thread-footer`.

| Token | Default |
|---|---|
| `--comment-thread-bg` | `var(--surface)` |
| `--comment-thread-border` / `-border-width` | `var(--border)` / `1px` |
| `--comment-thread-border-active` | `var(--accent)` |
| `--comment-thread-radius` | `var(--radius)` |
| `--comment-thread-shadow` | `none` |
| `--comment-thread-pad` | `var(--space-s)` |
| `--comment-thread-rule` | `var(--hairline)` |
| `--comment-thread-resolved-bg` | `var(--surface)` |
| `--comment-thread-marker` | `"›"` (rotates when open; also the group marker in notifications) |
| `--comment-thread-summary-bg-hover` | 6% `--text` |

**Touch:** the summary is at least `--tap-min` tall; reaction chips are
`--tap-min` square (core's `.badge-button`). Hover tints sit inside
`@media (hover: hover)`; the summary shows core's focus colour on keyboard
focus.

## Mentions `.mention`

```html
<a class="mention" href="/u/ava">@Ava Tran</a>
<a class="mention is-self" href="/u/me">@you</a>
<span class="mention">@design-team</span>
```

Inline chips that wrap with the sentence (so they count as text links, not
standalone targets, under WCAG 2.5.8). `.is-self` adds a warning tint and an
underline bar, so "you" is not marked by colour alone.

**Suggestion list:** forms.css `.combobox` + `.listbox`. An option that holds
an `.avatar` lays out as a person row; a trailing `<small>` (the handle) goes
to the end:

```html
<div class="combobox">
  <input class="input" role="combobox" aria-expanded="true" aria-controls="people"
         aria-autocomplete="list" aria-activedescendant="p2" value="Over to @a">
  <ul class="listbox" role="listbox" id="people" popover="manual" aria-label="People">
    <li role="option" id="p1"><span class="avatar avatar-sm" data-color="1" data-status="online">AT</span>
        <span><mark>A</mark>va Tran</span><small>@ava</small></li>
    <li role="option" id="p2" class="is-active">…</li>
  </ul>
</div>
```

The app opens the list after "@", filters it and inserts the chip. All
listbox states (active, selected, disabled, empty) are the forms group's.

| Token | Default |
|---|---|
| `--mention-bg` / `-fg` | 16% `--accent` / `var(--accent-text, var(--text))` |
| `--mention-radius` | `var(--radius)` |
| `--mention-self-bg` / `-fg` / `-line` | 30% `--warning` / `var(--text)` / `var(--warning-text, var(--warning))` |

## Typing indicator `.typing`

Core's, unchanged: `<div class="typing">Leo is typing…</div>`. Dots pulse
only with motion allowed. Token: `--typing-dot`.

## Notification centre `.notifications`

The same markup in three places:

```html
<!-- The bell -->
<button class="btn btn-icon is-clear has-badge" data-count="4"
        popovertarget="notif-pop" aria-label="Notifications, 4 unread">
  <svg class="icon"><use href="assets/icons/icons.svg#icon-bell"/></svg></button>

<!-- 1. A page panel -->
<section class="panel notifications" aria-labelledby="n-title">…</section>
<!-- 2. A popover from the bell (anchored beside it where supported) -->
<div class="popover notifications" popover id="notif-pop" aria-labelledby="…">…</div>
<!-- 3. A drawer -->
<aside class="drawer notifications" popover id="notif-drawer" aria-labelledby="…">…</aside>
```

Contents:

```html
<div class="notifications-header">
  <h2 id="n-title">Notifications</h2>
  <span class="badge badge-accent">4 new</span>
  <button class="btn btn-clear btn-sm">Mark all read</button>   <!-- or .btn-close in a drawer -->
</div>
<label class="notifications-dnd">Do not disturb
  <span class="switch"><input type="checkbox"><span class="switch-track"><span class="switch-thumb"></span></span></span>
</label>
<p class="notifications-paused" role="status">Paused until 09:00.</p>
<ul class="list">
  <li class="notification is-unread">
    <span class="avatar avatar-sm" data-color="2">LP</span>
    <div class="notification-body">
      <p><span class="visually-hidden">Unread: </span>Leo Park mentioned you in <a href="…">Q4 plan</a></p>
      <time datetime="…">5 min ago</time>
    </div>
    <div class="notification-actions">
      <button class="btn btn-icon btn-sm is-clear" aria-label="Mark as read">…</button>
      <button class="btn btn-icon btn-sm is-clear" popovertarget="menu" aria-haspopup="menu" aria-label="More actions">…</button>
    </div>
  </li>
  <li class="notification is-group is-unread">
    <details>
      <summary class="notification-summary">
        <span class="presence" aria-hidden="true">…avatars…</span>
        <span class="notification-body"><span>3 new comments on <strong>Q4 plan</strong></span><time>12 min ago</time></span>
      </summary>
      <ul class="notification-group"><li class="notification is-unread">…</li>…</ul>
      <div class="notification-group-footer"><button class="btn btn-clear btn-sm">Mark 3 read</button></div>
    </details>
  </li>
</ul>
```

| State | Markup | Look |
|---|---|---|
| Read | `.notification` | `--muted` text |
| Unread | `.notification.is-unread` | tinted row, a dot at the start, the first line bold; add a visually hidden "Unread:" |
| Grouped | `.notification.is-group` > `<details>` | summary row with a stacked avatar and a marker that turns when open; children indented on a rule |
| Per-item actions | `.notification-actions` | always visible icon buttons (no hover-only reveal); "more" opens a `.context-menu[popover]` |
| Do not disturb | checked switch in `.notifications-dnd`, or `.notifications.is-dnd` from the app | shows `.notifications-paused` |
| Paused bell | `.has-badge.is-muted` on the bell, a moon icon and a label that says so | grey count instead of red |
| Empty | core `.empty-state` (with experience.css's icon disc) | |
| Filters | core `.tabset` with radio tabs (All / Mentions / Following) | |

| Token | Default |
|---|---|
| `--notifications-width` | `24rem` (popover form; never wider than the screen − 1rem) |
| `--notifications-max-height` | `36rem` (popover form; scrolls inside) |
| `--notification-pad` | `var(--space-xs) var(--space-s)` |
| `--notification-read-fg` | `var(--muted)` |
| `--notification-unread-bg` / `-fg` | 9% `--accent` / `var(--text)` |
| `--notification-dot` / `-dot-size` | `var(--accent)` / `0.5rem` |
| `--notification-bg-hover` | 6% `--text` (group summary) |
| `--notification-group-rule` | `var(--hairline)` |
| `--notifications-paused-bg` / `-fg` | `var(--surface-2)` / `var(--text)` |
| `--has-badge-muted-bg` / `-fg` | `var(--surface-2)` / `var(--muted)` |

The list is core's `.list` (its `--list-*` tokens apply; the centre makes its
fill transparent so it takes the panel's, drawer's or popover's surface).

**Touch:** the DND label and the group summary are `--tap-min` tall; the
action buttons are core's `.btn-icon` (44px on touch tiers). **Accessibility:**
the bell's `aria-label` carries the count (the badge number is decoration);
unread is said in text; the paused note is `role="status"`.

## Activity feed `ol.timeline.activity`

```html
<div class="thread-divider">Today</div>
<ol class="timeline activity">
  <li><span class="avatar" data-color="3">MC</span>
    <p><strong>Mia Chen</strong> commented on <a href="…">Q4 plan</a></p>
    <blockquote class="activity-quote">Support is ready either way.</blockquote>
    <time datetime="2026-10-02T10:21">12 min ago</time></li>
  <li class="is-done"><p>Export <strong>EXP-412</strong> finished</p><time>53 min ago</time></li>
</ol>
```

- The instruments group's timeline, with the actor's avatar in place of the
  dot; the rail joins the avatars. A row with no avatar (a system event)
  keeps the timeline dot and its states (`.is-done`, `.is-warn`, `.is-error`,
  `aria-current`).
- Actor, verb and object are plain text and links in the `<p>`; the relative
  time is the `<time>` (the app updates its text; keep `datetime`).
- Day groups: core's `.thread-divider` between lists.

| Token | Default |
|---|---|
| `--activity-avatar-size` | `1.8rem` |
| `--activity-gap` | `var(--space-s)` |
| `--activity-fg` | `var(--text)` |
| `--activity-quote-rule` | `var(--hairline)` |

Plus the timeline's `--timeline-line`, `--timeline-time-fg` and dot tokens.

---

## Tiers and touch, all components

- No component sets a width; all wrap or truncate inside their box (the
  thread quote truncates with an ellipsis, notification text wraps, the
  centre's header wraps). Verified with no horizontal overflow at 393px and
  1280px in `blue-future`, `windows95`, `lcars` and `liquid-glass`.
- Every control reaches `--tap-min` (44px up to 900px and on coarse
  pointers, 24px otherwise) without changing its drawn size.
- Hover styles sit inside `@media (hover: hover)` with a focus-visible
  equivalent; motion sits inside `prefers-reduced-motion: no-preference` and
  stops under `data-motion="reduced"`/`"none"`.
