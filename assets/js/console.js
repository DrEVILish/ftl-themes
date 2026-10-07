/* ftl-themes: console curves (docs/components/console.md) — a reference
 * script, not part of the library contract (like controls.js). It does the
 * maths CSS can't:
 *
 * - [data-peq]: a parametric EQ. Range inputs marked data-band="1..n" and
 *   data-param="f" (0–1, log position 20 Hz–20 kHz), "g" (dB), "q", and an
 *   optional checkbox data-param="shelf" (band 1 low shelf, last band high
 *   shelf) or "on" (the whole EQ). Redraws its svg.eq-graph-curve path and
 *   moves each .eq-node[data-band] (--f, --g). data-range on the [data-peq]
 *   is the displayed ± dB (default 15).
 * - [data-dyn="comp"|"gate"]: a compressor or gate. Inputs with
 *   data-param="threshold" (dB), "ratio" (n:1), "range" (dB, gate), or the
 *   same as data-* attributes on the group. Redraws every .dyn-graph-line
 *   and .dyn-graph-fill (the area under it) and a .dyn-graph-threshold
 *   line inside it, over -60…0 dB.
 * - <output for="id" data-unit="dB" data-format="hz">: shows that input's
 *   value as you move it ("hz" turns a 0–1 log position into Hz).
 *
 * - A <label for> inside a [popover] (a device or preset menu) closes the
 *   popover when chosen, as a menu item should.
 * - [data-link="name"]: every input sharing a link name follows the others
 *   (a faceplate knob and its twin on the assignable controls).
 *
 * - [data-tap-tempo] buttons: tap a tempo; every [data-tempo-out] shows the
 *   average interval ("ms": "500 mS", "s": "0.50") and <html> gets --tempo.
 * - [data-scene-step="1"|"-1"]: moves the checked [name=ps-scene] radio
 *   (any radio group named in data-scene-group) to the next or previous one.
 * - [data-history="id"]: the checkboxes inside are an undoable patch.
 *   Buttons with data-undo, data-redo, data-checkpoint, data-restore or
 *   data-clear and data-for="id" act on it.
 *
 * Listens for "input" on the document, so controls.js's knob drags update
 * the curves too. Each group is drawn once on load. */
(function () {
  function num(el, scope, param, fallback) {
    var input = scope.querySelector('[data-param="' + param + '"]');
    var v = input ? +input.value : +scope.dataset[param];
    return isNaN(v) ? fallback : v;
  }
  function hz(v) {
    var f = 20 * Math.pow(10, 3 * v);
    return f >= 1000 ? (f / 1000).toFixed(f >= 10000 ? 1 : 2).replace(/\.?0+$/, "") + "k" : Math.round(f) + "";
  }

  // --- parametric EQ ---------------------------------------------------------
  function drawPeq(box) {
    var range = +box.dataset.range || 15;
    var on = box.querySelector('[data-param="on"]');
    var bands = {};
    box.querySelectorAll("[data-band][data-param]").forEach(function (i) {
      var b = bands[i.dataset.band] || (bands[i.dataset.band] = { f: 0.5, g: 0, q: 1, shelf: false });
      b[i.dataset.param] = i.type === "checkbox" ? i.checked : +i.value;
    });
    var keys = Object.keys(bands).sort();
    function db(x) {
      var sum = 0;
      keys.forEach(function (k, n) {
        var b = bands[k], oct = (x - b.f) * 3 * Math.LN10 / Math.LN2;
        if (b.shelf && n === 0) sum += b.g / (1 + Math.exp(oct * 3));
        else if (b.shelf && n === keys.length - 1) sum += b.g / (1 + Math.exp(-oct * 3));
        else sum += b.g / (1 + Math.pow(oct * b.q * 1.2, 2));
      });
      return on && !on.checked ? 0 : sum;
    }
    var d = "";
    for (var i = 0; i <= 200; i++) {
      var x = i / 200, y = 200 - Math.max(-1, Math.min(1, db(x) / range)) * 190;
      d += (i ? " L" : "M") + (x * 1000).toFixed(1) + " " + y.toFixed(1);
    }
    var path = box.querySelector(".eq-graph-curve path:not(.is-band)");
    if (path) path.setAttribute("d", d);
    keys.forEach(function (k) {
      var node = box.querySelector('.eq-node[data-band="' + k + '"]');
      if (!node) return;
      node.style.setProperty("--f", bands[k].f.toFixed(4));
      node.style.setProperty("--g", Math.max(-1, Math.min(1, bands[k].g / range)).toFixed(4));
    });
  }

  // --- dynamics transfer curves ---------------------------------------------
  function drawDyn(group) {
    var kind = group.dataset.dyn;
    var thr = num(null, group, "threshold", -20);
    var ratio = Math.max(1, num(null, group, "ratio", 4));
    var range = Math.abs(num(null, group, "range", 40));
    function out(i) {
      if (kind === "gate") return i >= thr ? i : Math.max(-60, i - range);
      return i <= thr ? i : thr + (i - thr) / ratio;
    }
    function px(db) { return ((db + 60) / 60 * 100).toFixed(2); }
    var d = "";
    for (var i = -60; i <= 0; i += 1) {
      if (kind === "gate" && i === Math.ceil(thr) && i > -60) d += " L" + px(thr) + " " + (100 - px(out(thr - 0.01))).toFixed(2);
      d += (d ? " L" : "M") + px(i) + " " + (100 - px(out(i))).toFixed(2);
    }
    group.querySelectorAll(".dyn-graph-line").forEach(function (p) { p.setAttribute("d", d); });
    group.querySelectorAll(".dyn-graph-fill").forEach(function (p) { p.setAttribute("d", d + " L100.00 100.00 L0.00 100.00 Z"); });
    group.querySelectorAll(".dyn-graph-threshold").forEach(function (l) {
      l.setAttribute("x1", px(thr)); l.setAttribute("x2", px(thr));
      l.setAttribute("y1", "0"); l.setAttribute("y2", "100");
    });
  }

  // --- readouts ---------------------------------------------------------------
  function show(o) {
    var input = document.getElementById((o.getAttribute("for") || "").split(" ")[0]);
    if (!input) return;
    var v = +input.value;
    var text = o.dataset.format === "hz" ? hz(v) : (Math.abs(v) < 10 && v % 1 ? v.toFixed(1) : Math.round(v * 10) / 10) + "";
    o.textContent = text + (o.dataset.unit ? " " + o.dataset.unit : "");
  }

  function link(target) {
    var name = target.dataset && target.dataset.link;
    if (!name) return;
    document.querySelectorAll('[data-link="' + name + '"]').forEach(function (other) {
      if (other === target || other.value === target.value) return;
      other.value = target.value;
      other.dispatchEvent(new Event("input", { bubbles: true }));
    });
  }

  function update(target) {
    link(target);
    var peq = target.closest && target.closest("[data-peq]");
    if (peq) drawPeq(peq);
    var dyn = target.closest && target.closest("[data-dyn]");
    if (dyn) drawDyn(dyn);
    if (target.id) document.querySelectorAll('output[for~="' + target.id + '"]').forEach(show);
  }
  document.addEventListener("click", function (e) {
    var item = e.target.closest && e.target.closest("[popover] label[for]");
    var pop = item && item.closest("[popover]");
    if (pop && pop.hidePopover) pop.hidePopover();
  });
  // Tap tempo: the average of the last four intervals, reset after 2 s.
  var taps = [];
  document.addEventListener("click", function (e) {
    var b = e.target.closest && e.target.closest("[data-tap-tempo]");
    if (!b) return;
    var now = performance.now();
    if (taps.length && now - taps[taps.length - 1] > 2000) taps = [];
    taps.push(now);
    taps = taps.slice(-5);
    if (taps.length < 2) return;
    var ms = (taps[taps.length - 1] - taps[0]) / (taps.length - 1);
    document.documentElement.style.setProperty("--tempo", Math.round(ms) + "ms");
    document.querySelectorAll("[data-tempo-out]").forEach(function (o) {
      o.textContent = o.dataset.tempoOut === "s" ? (ms / 1000).toFixed(2) : Math.round(ms) + " mS";
    });
  });

  // Next / previous in a radio list.
  document.addEventListener("click", function (e) {
    var b = e.target.closest && e.target.closest("[data-scene-step]");
    if (!b) return;
    var radios = [].slice.call(document.querySelectorAll('[name="' + (b.dataset.sceneGroup || "ps-scene") + '"]'));
    var i = radios.findIndex(function (r) { return r.checked; }) + (+b.dataset.sceneStep);
    if (radios[i]) { radios[i].checked = true; radios[i].dispatchEvent(new Event("change", { bubbles: true })); }
  });

  // Patch history: undo, redo, checkpoint, restore and clear.
  var hist = {};
  function scope(id) { return hist[id] || (hist[id] = { done: [], undone: [], mark: null }); }
  function boxes(id) { var r = document.getElementById(id); return r ? [].slice.call(r.querySelectorAll("input[type=checkbox]")) : []; }
  function snap(id) { return boxes(id).map(function (b) { return b.checked; }); }
  function apply(id, state) { boxes(id).forEach(function (b, i) { b.checked = state[i]; }); }
  document.addEventListener("change", function (e) {
    var r = e.target.closest && e.target.closest("[data-history]");
    if (!r || e.target.type !== "checkbox" || e.isTrusted === false) return;
    var h = scope(r.id), before = snap(r.id);
    before[boxes(r.id).indexOf(e.target)] = !e.target.checked;
    h.done.push(before);
    h.undone = [];
  });
  document.addEventListener("click", function (e) {
    var b = e.target.closest && e.target.closest("[data-for]:is([data-undo], [data-redo], [data-checkpoint], [data-restore], [data-clear])");
    if (!b) return;
    var id = b.dataset.for, h = scope(id), now = snap(id);
    if (b.hasAttribute("data-undo") && h.done.length) { h.undone.push(now); apply(id, h.done.pop()); }
    else if (b.hasAttribute("data-redo") && h.undone.length) { h.done.push(now); apply(id, h.undone.pop()); }
    else if (b.hasAttribute("data-checkpoint")) h.mark = now;
    else if (b.hasAttribute("data-restore") && h.mark) { h.done.push(now); apply(id, h.mark); }
    else if (b.hasAttribute("data-clear")) { h.done.push(now); apply(id, now.map(function () { return false; })); }
  });

  document.addEventListener("input", function (e) { update(e.target); });
  document.addEventListener("change", function (e) { if (e.target.type === "checkbox") update(e.target); });
  document.querySelectorAll("[data-peq]").forEach(drawPeq);
  document.querySelectorAll("[data-dyn]").forEach(drawDyn);
  document.querySelectorAll("output[for]").forEach(show);
})();
