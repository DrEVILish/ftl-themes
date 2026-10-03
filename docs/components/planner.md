# Productivity kit: planner (v5)

Source: `core/components/planner.css`. Example page: `planner.html`.
Covers PLAN.md §22 "Productivity kit": kanban board, calendar (month, week, day,
agenda), Gantt timeline and the schedule list.

Shared conventions:

- **Apps provide behaviour, CSS styles states.** Apps move cards, lay events out in
  lanes and columns, compute overlaps and draw dependency paths; ftl-themes styles every
  state. Nothing here needs JavaScript to render.
- **Value APIs (inline custom properties):** `--day`/`--span`/`--lane` (month bars),
  `--start`/`--end` (hours for timed events, time units for Gantt bars),
  `--col`/`--cols` (overlaps), `--now`, `--at`, `--progress`, `--duration`, `--units`,
  `--days`, `--hour-start`/`--hour-end`, `--level`, `--lanes`.
- **Colour:** `data-series="1".."6"` (from `instruments.css`) colours events, labels,
  Gantt bars, milestones and schedule rows from the theme's chart palette. Fills are
  tints mixed into the surface, with `--text` on top, so text contrast holds in every
  theme; the solid series colour is only used for bars, edges and dots.
- **Colour is never the only signal:** over the WIP limit adds a "!" and a thick stripe;
  overdue is a bordered bold chip plus hidden "Overdue" text; priority is a glyph plus
  the word; today is a filled disc; tentative is a hatch; cancelled is struck through;
  critical path is thicker; blocked links are dashed; the current-time line has a dot.
- **Reuse:** the calendar is core's `.calendar` frame (forms.css: header, title, the
  `--calendar-*` tokens) with `.is-planner`; the view switch is core's CSS-only
  `.tabset`; counts and labels are `.badge`; assignees are `.avatar`; schedule rows
  wrap core's `.schedule` time badge.
- **Motion:** colour/border/tilt transitions only under
  `prefers-reduced-motion: no-preference`, and never under `html[data-motion="reduced"]`.
- **Forced colours:** event, bar and row edges use `CanvasText`; the now line, today
  marker, milestones and today's date use `Highlight`.

---

## Kanban board `.kanban`

```html
<div class="kanban" role="group" aria-label="Release board">
  <section class="kanban-column is-over-limit" aria-labelledby="col-doing">
    <header class="kanban-column-header">
      <h3 class="kanban-column-title" id="col-doing">In progress</h3>
      <span class="badge kanban-count" aria-label="4 cards, limit 3, over the limit">4<span class="kanban-limit">3</span></span>
      <button class="btn btn-icon btn-sm is-clear" aria-label="In progress column actions"
              popovertarget="col-menu" aria-haspopup="menu"><svg class="icon"><use href="assets/icons/icons.svg#icon-more-horizontal"/></svg></button>
    </header>
    <ol class="kanban-cards">
      <li class="kanban-card" draggable="true" tabindex="0">
        <ul class="kanban-labels" aria-label="Labels">
          <li><span class="badge" data-series="1">Core</span></li>
        </ul>
        <h4 class="kanban-card-title">Calendar agenda list on phones</h4>
        <div class="kanban-card-meta">
          <span class="kanban-priority" data-priority="urgent">Urgent</span>
          <time class="kanban-due is-overdue" datetime="2026-09-30"><svg class="icon" aria-hidden="true"><use href="assets/icons/icons.svg#icon-calendar"/></svg><span class="visually-hidden">Overdue, was due </span>30 Sep</time>
          <ul class="kanban-assignees" aria-label="Assignees">
            <li><span class="avatar" role="img" aria-label="Sam Reyes">SR</span></li>
            <li><span class="avatar" role="img" aria-label="Ada Kim">AK</span></li>
          </ul>
        </div>
      </li>
      <li class="kanban-placeholder"><span class="visually-hidden">Drop here</span></li>
    </ol>
    <button class="btn btn-clear btn-sm"><svg class="icon"><use href="assets/icons/icons.svg#icon-plus"/></svg> Add card</button>
  </section>
</div>
```

- **Parts.** `.kanban-column` (a `<section>`), `.kanban-column-header` with
  `.kanban-column-title`, `.badge.kanban-count` (with an optional `.kanban-limit`,
  printed as " / 3"), `ol.kanban-cards`, `.kanban-card` with `.kanban-labels`
  (`.badge[data-series]`), `.kanban-card-title`, an optional `<p>` description, and
  `.kanban-card-meta` holding `.kanban-priority`, `.kanban-due` and `.kanban-assignees`
  (pushed to the end).
- **States.**
  - Column: `.is-over-limit` (WIP exceeded: danger stripe on top, danger count with "!"),
    `.is-drop-target` (the column the dragged card is over: accent tint and dashed ring).
    The app sets both; CSS can't count against a limit.
  - Cards: `.is-dragging` (lifted, tilted `--kanban-drag-tilt`, accent ring, `grabbing`
    cursor); `[draggable="true"]` gets the `grab` cursor; `:focus-within` and hover ring.
  - `.kanban-placeholder`: the landing slot (dashed accent box). Set
    `style="--kanban-placeholder-size: 92px"` to the dragged card's height.
  - Empty column: an empty `ol.kanban-cards` draws a dashed drop area.
  - Due: `.kanban-due.is-soon` (warning, bold), `.is-overdue` (danger chip).
  - Priority: `data-priority="urgent|high|medium|low"` (▲▲, ▲, ◆, ▼ + the word).
- **Tiers.** The board scrolls sideways inside itself (never the page) with scroll
  snap. In a container ≤ 480px each column is the board's width minus a peek of the next
  one, and snapping is mandatory on phones: one column per screen.
- **Tokens (defaults):**

| Token | Default |
|---|---|
| `--kanban-gap` | `var(--space-s)` |
| `--kanban-column-width` | `17.5rem` |
| `--kanban-column-max` | `none` (cap a column's height; its cards scroll) |
| `--kanban-column-pad` | `var(--space-s)` |
| `--kanban-column-bg`, `--kanban-column-fg` | `var(--surface-2)`, `var(--text)` |
| `--kanban-column-border`, `--kanban-column-border-width` | `var(--hairline)`, `1px` |
| `--kanban-column-accent`, `--kanban-column-accent-width` | the border, `1px` (top edge) |
| `--kanban-column-radius` | `var(--panel-radius, var(--radius))` |
| `--kanban-over-limit` | `var(--danger)` |
| `--kanban-drop-bg`, `--kanban-drop-ring` | accent 12% into the column, `var(--accent)` |
| `--kanban-card-gap`, `--kanban-card-pad` | `var(--space-xs)`, `var(--space-s)` |
| `--kanban-card-bg`, `--kanban-card-fg` | `var(--surface)`, `var(--text)` |
| `--kanban-card-border`, `--kanban-card-border-width` | `var(--border)`, `1px` |
| `--kanban-card-border-hover`, `--kanban-card-border-focus` | `var(--accent)`, `var(--focus)` |
| `--kanban-card-radius`, `--kanban-card-shadow` | `var(--radius)`, `none` |
| `--kanban-drag-ring`, `--kanban-drag-shadow` | `var(--accent)`, a soft drop shadow |
| `--kanban-drag-tilt`, `--kanban-drag-opacity` | `2deg`, `1` |
| `--kanban-placeholder-bg`, `--kanban-placeholder-border`, `--kanban-placeholder-size` | accent 10%, `var(--accent)`, `4.5rem` |
| `--kanban-empty-size` | `3.5rem` |
| `--kanban-due-soon` | `var(--warning-text, var(--text))` |
| `--kanban-overdue-bg`, `--kanban-overdue-fg`, `--kanban-overdue-border` | danger 20%, `var(--danger-text, var(--text))`, `var(--danger)` |
| `--kanban-priority-{urgent,high,medium,low}-glyph` | `"▲▲"`, `"▲"`, `"◆"`, `"▼"` |
| `--kanban-avatar-size` | `1.6rem` |

- **Accessibility.** Columns are labelled sections; cards are list items with a heading.
  Give the count badge an `aria-label` that says the limit and the over-limit state.
  Drag and drop needs a keyboard path in the app (for example Space to pick up, arrows to
  move, Space to drop, Esc to cancel) and a live region announcing moves; `draggable`
  alone is mouse-only. Avatars need `role="img"` and a name.

---

## Calendar `.calendar.is-planner`

`.is-planner` turns forms.css's `.calendar` (an inline date-picker frame) into a
full-width, container-query-aware view. The header, title and buttons are the date
picker's (`.calendar-header`, `.calendar-title`), and the date picker's tokens
(`--calendar-bg`, `--calendar-border`, `--calendar-weekday-fg`, `--calendar-outside-fg`,
`--calendar-today-ring`, `--calendar-selected-bg`, `--calendar-day-bg-hover`) apply here
too.

### View switch (CSS only)

```html
<div class="tabset">
  <div class="tabs">
    <label class="tab"><input type="radio" name="cal-view" checked>Month</label>
    <label class="tab"><input type="radio" name="cal-view">Week</label>
    <label class="tab"><input type="radio" name="cal-view">Day</label>
  </div>
  <div class="tab-panel"><div class="calendar is-planner">…month…</div></div>
  <div class="tab-panel"><div class="calendar is-planner">…week…</div></div>
  <div class="tab-panel"><div class="calendar is-planner">…day…</div></div>
</div>
```

### Month view

```html
<div class="calendar is-planner" role="group" aria-label="October 2026">
  <div class="calendar-header">
    <button class="btn btn-icon is-clear btn-sm" aria-label="Previous month">…</button>
    <h3 class="calendar-title" aria-live="polite">October 2026</h3>
    <button class="btn btn-icon is-clear btn-sm" aria-label="Next month">…</button>
    <button class="btn btn-sm">Today</button>
  </div>
  <div class="calendar-weekdays" aria-hidden="true"><span>Mon</span>…<span>Sun</span></div>
  <div class="calendar-month">
    <div class="calendar-week">
      <!-- exactly seven cells first -->
      <div class="calendar-cell is-outside" data-events><time class="calendar-date" datetime="2026-09-30">30<span class="calendar-date-month"> Sep</span></time></div>
      <div class="calendar-cell" aria-current="date" data-events><time class="calendar-date" datetime="2026-10-02">2</time></div>
      <div class="calendar-cell is-weekend"><time class="calendar-date" datetime="2026-10-03">3</time></div>
      …
      <!-- then the events -->
      <a class="calendar-event" href="/e/12" data-series="2" style="--day:3; --span:3; --lane:1">Q4 planning offsite</a>
      <a class="calendar-event is-timed" href="/e/13" data-series="1" style="--day:5; --lane:3"><time>14:00</time> Retro</a>
      <button class="calendar-more" style="--day:5">+2 more</button>
    </div>
    …
  </div>
  <div class="calendar-agenda">…schedule lists, shown on phones…</div>
</div>
```

- **Layout.** Each `.calendar-week` is a seven-column grid. Its first seven children are
  the `.calendar-cell`s (they span the whole row height and paint the day, the grid lines
  and the backgrounds); after them come the events, laid over the cells in lanes:
  `--day` (1–7, the first column), `--span` (days, default 1), `--lane` (1…). The app
  assigns lanes. `.calendar-more` (a "+n more" button) sits under `--day` below the last
  lane. Set `--lanes` on a week (or `--calendar-lanes` on the theme) for more than 3.
- **Cell states:** `.is-outside` (another month), `.is-weekend`, `aria-current="date"`
  (today: a filled disc on the date), `.is-selected` / `aria-selected="true"` (inset
  ring), `data-events` (marks a busy day for the phone dot view).
- **Event states:** `.is-continued-before` / `.is-continued-after` (the bar runs on from
  or into another week: squared ends, dashed start, an arrow at the end),
  `.is-timed` (a dot and no fill, for a timed event in the month grid),
  `.is-tentative` (hatched), `.is-cancelled` (struck through; colour `--calendar-event-cancelled-fg`, default the event text).
- **Phones (container ≤ 480px):** the month grid becomes a compact grid of dates with a
  dot under busy days (`data-events`), bars and "+n more" are hidden, the
  `.calendar-date-month` text (" Sep") is visually hidden, and `.calendar-agenda` is
  shown: put the agenda (`.schedule-heading` + `.schedule-list`) there. It is hidden on
  wider containers.
- **Touch:** lanes grow to `--tap-min` (44px) on touch devices so bars and "+n more"
  are full-size targets.

### Week and day views (time grid)

```html
<div class="calendar is-planner">
  <div class="calendar-header">…</div>
  <div class="calendar-timegrid" style="--days:7; --hour-start:8; --hour-end:18"
       role="group" aria-label="Week of 28 September">
    <div class="calendar-corner">GMT+1</div>
    <div class="calendar-column-head"><span>Mon</span><span class="calendar-date">28</span></div>
    …
    <div class="calendar-column-head" aria-current="date"><span>Fri</span><span class="calendar-date">2</span></div>
    …
    <ol class="calendar-hours" aria-hidden="true"><li>08:00</li>…<li>17:00</li></ol>
    <div class="calendar-column" role="group" aria-label="Monday 28 September">
      <a class="calendar-event" href="/e/1" data-series="1" style="--start:9.5; --end:10">Standup<time>09:30–10:00</time></a>
    </div>
    <div class="calendar-column" aria-current="date" role="group" aria-label="Friday 2 October">
      <a class="calendar-event" href="/e/2" data-series="4" style="--start:11; --end:12.5; --col:1; --cols:2">Release 2.4<time>11:00–12:30</time></a>
      <a class="calendar-event" href="/e/3" data-series="6" style="--start:11.5; --end:12.5; --col:2; --cols:2">Infra check<time>11:30–12:30</time></a>
      <span class="calendar-now" style="--now:13.6"><span class="visually-hidden">Now, 13:36</span></span>
    </div>
    …
  </div>
</div>
```

- **Order:** corner, then one `.calendar-column-head` per day, then `.calendar-hours`
  (one `<li>` per hour from `--hour-start`), then one `.calendar-column` per day. A day
  view is the same with `--days:1`.
- **Events:** `--start` and `--end` in hours (9.5 = 09:30); overlapping events side by
  side with `--col` (1-based) of `--cols`. The app computes the overlap groups.
- **Now:** `.calendar-now` at `--now` (hours) inside today's column: a line with a dot.
- **States:** `aria-current="date"` on today's head (filled date disc) and column (tint);
  `.is-weekend` columns; event `.is-tentative`, `.is-cancelled`.
- **Scrolling:** the grid scrolls both ways inside itself; the head row and the hour
  gutter are sticky. `--calendar-timegrid-max` caps its height (default `none`).
- **Touch:** an hour is `max(3.5rem, 2 × --tap-min)` tall, so a 30-minute event is a
  full 44px target on touch and 28px on desktop. Shorter events are below the minimum:
  give them at least 30 minutes of height, or open them from the agenda.

### Calendar tokens

| Token | Default |
|---|---|
| `--calendar-grid-line` | `var(--hairline)` |
| `--calendar-event-color` | `var(--accent)` (when there's no `data-series`) |
| `--calendar-event-bg`, `--calendar-event-bg-hover` | the event colour 24% / 36% into `--calendar-bg` |
| `--calendar-event-fg` | `var(--text)` |
| `--calendar-event-bar` | `3px` (the leading edge) |
| `--calendar-event-radius` | `calc(var(--radius) * 0.75)` |
| `--calendar-lanes`, `--calendar-lane` | `3`, `1.75em` (at least `--tap-min`) |
| `--calendar-date-row` | `2.4em` |
| `--calendar-week-min` | `7.5em` |
| `--calendar-weekend-bg` | `--surface-2` at 45% |
| `--calendar-outside-bg` | `--surface-2` at 70% |
| `--calendar-date-radius` | `999px` |
| `--calendar-today-bg`, `--calendar-today-fg` | `var(--calendar-today-ring, var(--accent))`, `var(--on-accent)` |
| `--calendar-today-text` | `var(--accent-text, var(--text))` (today's column head) |
| `--calendar-today-column-bg` | accent at 6% |
| `--calendar-more-fg` | `var(--accent-text, var(--text))` |
| `--calendar-hour` | `max(3.5rem, calc(var(--tap-min) * 2))` |
| `--calendar-gutter` | `3.5rem` |
| `--calendar-column-min` | `6rem` |
| `--calendar-half-hour-line` | the grid line at 45% |
| `--calendar-now`, `--calendar-now-width` | `var(--danger)`, `2px` |
| `--calendar-timegrid-max` | `none` |

- **Accessibility.** Give each event link a name that includes its date or time (the
  time grid's `<time>` does; a month bar's title should carry its dates if they aren't
  obvious from the cell, for example "Offsite, 30 Sep to 2 Oct"). Columns are labelled
  groups. The weekday header is `aria-hidden` because each cell's `<time datetime>`
  carries the date. Keep `aria-live="polite"` on the title so view and period changes are
  announced. The month grid is not an ARIA grid: if your app adds arrow-key navigation
  between days, add `role="grid"`/`row`/`gridcell` and roving `tabindex`.

---

## Gantt timeline `.gantt`

```html
<div class="gantt" style="--units:23" role="group" aria-label="Website relaunch timeline">
  <div class="gantt-header">
    <span class="gantt-corner">Task</span>
    <ol class="gantt-scale">
      <li aria-label="Monday 28 September">M<br>28</li>
      <li class="is-off" aria-label="Saturday 3 October">S<br>3</li>
      <li aria-current="date" aria-label="Friday 2 October">F<br>2</li>
      …
    </ol>
  </div>
  <div class="gantt-body">
    <ol class="gantt-rows">
      <li class="gantt-row is-group"><span class="gantt-task">Website relaunch</span>
        <div class="gantt-track"><span class="gantt-bar is-summary" style="--start:0; --end:19.5" role="img" aria-label="Website relaunch, 28 Sep to 17 Oct"></span></div></li>
      <li class="gantt-row is-selected"><span class="gantt-task" style="--level:2">Wireframes</span>
        <div class="gantt-track"><a class="gantt-bar" href="/t/2" data-series="1" style="--start:4.5; --end:9; --progress:.4"><span>Wireframes · 40%</span></a></div></li>
      <li class="gantt-row"><span class="gantt-task" style="--level:2">Design sign-off</span>
        <div class="gantt-track"><span class="gantt-milestone" style="--at:9.5" role="img" aria-label="Milestone: design sign-off, 7 Oct"></span><span class="gantt-milestone-label" style="--at:9.5">Sign-off</span></div></li>
      …
    </ol>
    <svg class="gantt-links" viewBox="0 0 23 8" preserveAspectRatio="none" aria-hidden="true">
      <defs>
        <marker id="gantt-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse"
                markerWidth=".3" markerHeight=".3" orient="auto"><path class="gantt-link-head" d="M0 0 10 5 0 10z"/></marker>
      </defs>
      <path class="gantt-link" d="M9 2.5 H9.5 V3.2" marker-end="url(#gantt-arrow)"/>
    </svg>
    <span class="gantt-today" style="--at:4.55"><span class="visually-hidden">Today, 2 October</span></span>
  </div>
</div>
```

- **Axis.** `--units` is the number of time units (days, weeks…) on the axis; each is
  `--gantt-unit` wide. `.gantt-scale` has one `<li>` per unit, or `style="--span:7"` on
  an item to label a week. `li.is-off` shades a weekend or holiday;
  `li[aria-current="date"]` marks today.
- **Bars.** `--start` and `--end` in units from the start of the axis (fractions are
  fine), `--progress` 0–1 as a fill strip along the bar's bottom (text stays on the
  tint, so it reads in every theme). As an `<a>` or `<button>` the bar's hit area is the
  whole row height (wrap the text in a `<span>` so it can truncate). States:
  `.is-done` (paler, muted text), `.is-critical` (thick danger border), `.is-late`
  (dashed danger border), `.is-summary` (a thin bracket for a group).
- **Milestones.** `.gantt-milestone` at `--at` (a diamond); `.is-done` hollows it.
  `.gantt-milestone-label` at the same `--at` prints a name beside it.
- **Rows.** `.gantt-row.is-group` (bold task), `.is-selected` (or `aria-selected="true"` when the rows are a `role="grid"`/`treegrid`)
  (tinted task cell), `--level` on `.gantt-task` indents sub-tasks (1 = no indent).
- **Today.** `.gantt-today` at `--at` units: a full-height line over the rows.
- **Dependencies.** `svg.gantt-links` is laid over the time axis. Its user units are the
  grid: x = time unit, y = row (row *n*'s centre line is *n* + 0.5), so set
  `viewBox="0 0 <units> <rows>" preserveAspectRatio="none"` and draw paths in data
  coordinates; no pixel maths. Strokes don't scale (`vector-effect`). Cells are square by
  default (`--gantt-row` = `--gantt-unit`), so arrowheads keep their shape; use
  `markerUnits="userSpaceOnUse"` with marker sizes in units (0.3 ≈ a third of a cell).
  Class hooks: `.gantt-link` (plus `.is-critical`: thicker, danger; `.is-blocked`:
  dashed) and `.gantt-link-head` (plus `.is-critical`) for marker paths. In RTL the
  layer is mirrored.
- **Scrolling.** The Gantt scrolls inside itself; the task column is frozen (sticky)
  and the header sticks to the top when `--gantt-max` caps its height. In a container
  ≤ 480px the task column narrows to `--gantt-list-width-narrow`.
- **Touch.** A unit (and a row) is `max(--tap-min, 2.25rem)`, so rows are 44px on touch.
- **Tokens (defaults):**

| Token | Default |
|---|---|
| `--gantt-unit` | `max(var(--tap-min), 2.25rem)` |
| `--gantt-row` | `var(--gantt-unit)` |
| `--gantt-list-width`, `--gantt-list-width-narrow` | `13rem`, `8.5rem` |
| `--gantt-max` | `none` |
| `--gantt-bg`, `--gantt-fg` | `var(--surface)`, `var(--text)` |
| `--gantt-border`, `--gantt-border-width`, `--gantt-radius` | `var(--border)`, `1px`, `var(--panel-radius, var(--radius))` |
| `--gantt-header-bg` | `var(--surface-2)` |
| `--gantt-grid-line` | `var(--hairline)` |
| `--gantt-off-bg` | `--surface` at 55% |
| `--gantt-selected-bg` | accent 16% |
| `--gantt-bar` | `var(--accent)` (when there's no `data-series`) |
| `--gantt-bar-bg`, `--gantt-bar-fg` | the bar colour 26% into the surface, `var(--text)` |
| `--gantt-bar-size` | `max(66%, calc(1.45em + 14px))` |
| `--gantt-bar-radius` | `var(--radius)` |
| `--gantt-progress-size` | `0.25em` |
| `--gantt-critical` | `var(--danger)` |
| `--gantt-milestone`, `--gantt-milestone-size` | `var(--accent)`, `0.95rem` |
| `--gantt-today`, `--gantt-today-fg`, `--gantt-today-width` | `var(--danger)`, `var(--on-danger, #fff)`, `2px` |
| `--gantt-link`, `--gantt-link-width` | `var(--muted)`, `1.5px` |

- **Accessibility.** The SVG layer is decorative (`aria-hidden`): describe
  dependencies in text too (a "Depends on" column, or the bar's accessible name). Give
  summary bars and milestones `role="img"` and a name with their dates. Ship an
  accessible table of tasks next to a complex chart.

---

## Schedule list `.schedule-list`

Time-blocked agenda rows, built on core's `.schedule` time badge (CONTRACT.md
"Schedule badge").

```html
<h3 class="schedule-heading" aria-current="date">Today, Friday 2 October</h3>
<ol class="schedule-list">
  <li class="schedule-item is-past" data-series="1" style="--duration:.5">
    <time class="schedule" datetime="09:30">09:30<span class="schedule-end">10:00</span></time>
    <div class="schedule-body"><span class="schedule-title">Standup</span><span class="schedule-meta">Room 4</span></div>
  </li>
  <li class="schedule-item is-free" style="--duration:.5">
    <time class="schedule" datetime="12:30">12:30<span class="schedule-end">13:00</span></time>
    <div class="schedule-body"><span class="schedule-title">Free</span></div>
  </li>
  <li class="schedule-item" data-series="5" style="--duration:1" aria-current="time">
    <time class="schedule" datetime="13:00">13:00<span class="schedule-end">14:00</span></time>
    <div class="schedule-body"><span class="schedule-title"><a class="stretched-link" href="/e/9">Lunch &amp; learn</a></span><span class="schedule-meta">Kitchen</span></div>
    <span class="badge badge-accent">Now</span>
  </li>
</ol>
```

- **Parts.** Three columns: the `.schedule` badge (start, with an optional
  `.schedule-end` under it), `.schedule-body` (`.schedule-title`, `.schedule-meta`), and
  an optional trailing item (a badge or a `.btn-icon`).
- **Time blocks.** `--duration` (hours) makes a row `--schedule-hour` per hour tall (and
  never less than `--tap-min`), so the list reads as a day plan.
- **States.** `.is-past` (no fill, muted), `aria-current="time"` / `.is-current` (accent
  ring; add a "Now" badge for a text cue), `.is-free` (dashed edge, italic, no fill),
  `.is-conflict` (danger outline; add an "Overlaps" badge).
- **Row link.** Use core's `.stretched-link` on the title link to make the whole row the
  target (the row is `position: relative`).
- **Headings.** `.schedule-heading` labels a day; `aria-current="date"` colours today's.
- **Tokens (defaults):**

| Token | Default |
|---|---|
| `--schedule-color` | `var(--accent-2, var(--accent))` (when there's no `data-series`) |
| `--schedule-list-gap` | `var(--space-2xs)` |
| `--schedule-time-width` | `4.25em` |
| `--schedule-hour` | `3rem` |
| `--schedule-item-pad` | `var(--space-xs) var(--space-s)` |
| `--schedule-item-bg` | the row colour 12% into `--surface` |
| `--schedule-item-radius` | `var(--radius)` |
| `--schedule-bar-width` | `3px` |
| `--schedule-time-fg` | `var(--text)` |
| `--schedule-current-ring` | `var(--accent)` |
| `--schedule-heading-fg` | `var(--muted)` |

The badge's own tokens (`--schedule-gap`, `--schedule-font-size`) still apply.

- **Accessibility.** An ordered list in time order; `<time datetime>` on each start;
  `aria-current="time"` is announced. Don't rely on the past dimming alone: past rows
  are also plain-weight.
