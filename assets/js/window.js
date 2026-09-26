/* ftl-themes: window drag helper — a non-contract reference implementation.
 *
 * Only dragging genuinely needs JS (maximize/minimize/focus/close/resize
 * all decompose into CSS — see CONTRACT.md "Window pattern"). Like
 * theme-loader.js, this is an example a real app wires however it wants,
 * not part of the library contract.
 *
 * Opt in per window: <div class="ftl-modal" data-ftl-drag> with a
 * .ftl-modal-header drag handle. Interactive elements inside the header
 * (buttons, links, inputs, the min/max labels) stay clickable: the drag
 * only starts from bare header surface.
 */
document.addEventListener('pointerdown', (e) => {
  const win = e.target.closest('[data-ftl-drag]');
  if (!win || e.button !== 0) return;
  if (!e.target.closest('.ftl-modal-header')) return;
  if (e.target.closest('button, a, input, select, textarea, summary, label')) return;
  const r = win.getBoundingClientRect();
  Object.assign(win.style, {
    position: 'fixed', left: r.left + 'px', top: r.top + 'px',
    margin: '0', width: r.width + 'px',
  });
  const dx = e.clientX - r.left, dy = e.clientY - r.top;
  const move = (ev) => {
    win.style.left = (ev.clientX - dx) + 'px';
    win.style.top = (ev.clientY - dy) + 'px';
  };
  const up = () => {
    removeEventListener('pointermove', move);
    removeEventListener('pointerup', up);
  };
  addEventListener('pointermove', move);
  addEventListener('pointerup', up);
});
