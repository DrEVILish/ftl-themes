/* ftl-themes: window drag helper — a small reference implementation.
 *
 * Opt in per window: <div class="modal" data-drag> with a .modal-header
 * handle (give the header tabindex="0" for keyboard moves). Load once:
 *   - drag the header with mouse, pen or touch (Pointer Events; the CSS
 *     sets touch-action: none on the header only, so the body still scrolls);
 *   - the window stays inside the viewport, while dragging and on resize;
 *   - double-click or double-tap the header toggles maximize (the
 *     .window-max checkbox when one precedes the modal, else .is-maximized);
 *   - Alt+Arrow keys move it 16px while the header has focus (Shift: 1px).
 * Interactive elements in the header (buttons, links, inputs, the min/max
 * labels) stay clickable: drags start only from bare header surface.
 * State is inline left/top (correctly unthemeable) plus .is-dragging. */
(() => {
  const SKIP = 'button, a, input, select, textarea, summary, label';
  const head = (e) => {
    const h = e.target.closest?.('.modal-header');
    const win = h?.closest('[data-drag]');
    return win && h.parentElement === win && !e.target.closest(SKIP) ? [win, h] : [];
  };
  const maxed = (win) => win.classList.contains('is-maximized') ||
    win.previousElementSibling?.matches('.window-max:checked');
  const toggleMax = (win) => {
    const box = win.previousElementSibling;
    if (box?.matches('input.window-max')) box.checked = !box.checked;
    else win.classList.toggle('is-maximized');
  };
  // Pin the window at its current spot as position: fixed. A container-type
  // or transformed ancestor becomes the fixed containing block, so measure
  // the offset once and correct for it.
  const pin = (win) => {
    const r = win.getBoundingClientRect();
    if (!win.dataset.dragX) {
      Object.assign(win.style, { position: 'fixed', inset: 'auto', margin: '0', left: '0px', top: '0px', width: r.width + 'px' });
      const o = win.getBoundingClientRect();
      win.dataset.dragX = o.left; win.dataset.dragY = o.top;
    }
    return r;
  };
  // Move to viewport point (x, y), clamped so the whole window stays on screen.
  const place = (win, x, y) => {
    const vw = document.documentElement.clientWidth, vh = document.documentElement.clientHeight;
    x = Math.max(0, Math.min(x, vw - win.offsetWidth));
    y = Math.max(0, Math.min(y, vh - win.offsetHeight));
    win.style.left = x - win.dataset.dragX + 'px';
    win.style.top = y - win.dataset.dragY + 'px';
  };

  let last = { t: 0 };
  document.addEventListener('pointerdown', (e) => {
    const [win, h] = head(e);
    if (!win || !e.isPrimary || e.button !== 0) return;
    // Double-click / double-tap: our own timing, as touch browsers don't
    // reliably fire dblclick.
    if (e.timeStamp - last.t < 400 && last.win === win && Math.hypot(e.clientX - last.x, e.clientY - last.y) < 16) {
      last = { t: 0 };
      toggleMax(win);
      return;
    }
    last = { t: e.timeStamp, win, x: e.clientX, y: e.clientY };
    if (maxed(win)) return;
    const r = win.getBoundingClientRect(), dx = e.clientX - r.left, dy = e.clientY - r.top;
    h.setPointerCapture(e.pointerId);
    win.classList.add('is-dragging');
    // Pin on the first move, not on press: a plain click or double-click
    // must not lift the window out of the page flow.
    const move = (ev) => { pin(win); place(win, ev.clientX - dx, ev.clientY - dy); };
    const up = () => {
      win.classList.remove('is-dragging');
      h.removeEventListener('pointermove', move);
      h.removeEventListener('pointerup', up);
      h.removeEventListener('pointercancel', up);
    };
    h.addEventListener('pointermove', move);
    h.addEventListener('pointerup', up);
    h.addEventListener('pointercancel', up);
  });

  const STEP = { ArrowLeft: [-1, 0], ArrowRight: [1, 0], ArrowUp: [0, -1], ArrowDown: [0, 1] };
  document.addEventListener('keydown', (e) => {
    const [win, h] = head(e);
    if (!win || e.target !== h || !e.altKey || !STEP[e.key] || maxed(win)) return;
    e.preventDefault(); // Alt+Left/Right would otherwise navigate history
    const r = pin(win), n = e.shiftKey ? 1 : 16;
    place(win, r.left + STEP[e.key][0] * n, r.top + STEP[e.key][1] * n);
  });

  addEventListener('resize', () => {
    for (const win of document.querySelectorAll('[data-drag][data-drag-x]')) {
      if (maxed(win)) continue;
      const r = win.getBoundingClientRect();
      place(win, r.left, r.top);
    }
  });
})();
