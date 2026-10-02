/* ftl-themes: theme scheduling (PLAN.md §20) — a reference snippet, not
 * part of the library contract (like window.js and prefs.js).
 *
 * Switches theme, palette variant or seasonal palette by time of day or
 * date. The rules are declared on <html> as JSON:
 *
 *   <html data-theme="blue-future" data-schedule='[
 *     {"from": "19:00", "to": "07:00", "variant": "night"},
 *     {"from": "10-24", "to": "11-01", "season": "halloween"},
 *     {"from": "12-01", "to": "12-31", "theme": "lego-classic"}
 *   ]'>
 *
 * "HH:MM" ranges are times of day, "MM-DD" ranges are dates; both may wrap
 * (19:00 to 07:00, 12-20 to 01-05). The first matching rule of each kind
 * wins; outside every rule the page's own attributes stand. A choice the
 * user made (stored by prefs.js or the app, marked with data-user-theme /
 * data-user-variant on <html>) always wins over the schedule. Re-checked
 * every minute.
 */
(function () {
  var html = document.documentElement;
  var rules;
  try { rules = JSON.parse(html.dataset.schedule || "[]"); } catch (e) { return; }
  if (!rules.length) return;
  var base = { theme: html.dataset.theme, variant: html.dataset.variant, season: html.dataset.season };

  function within(from, to, now) {
    return from <= to ? now >= from && now < to : now >= from || now < to;
  }
  function matches(rule, d) {
    var pad = function (n) { return String(n).padStart(2, "0"); };
    var time = pad(d.getHours()) + ":" + pad(d.getMinutes());
    var date = pad(d.getMonth() + 1) + "-" + pad(d.getDate());
    var now = /^\d\d:\d\d$/.test(rule.from) ? time : date;
    return within(rule.from, rule.to, now);
  }
  function setAttr(name, value) {
    if (value) html.dataset[name] = value; else delete html.dataset[name];
  }
  function apply() {
    var d = new Date(), pick = {};
    rules.forEach(function (r) {
      if (!matches(r, d)) return;
      ["theme", "variant", "season"].forEach(function (k) { if (r[k] && !(k in pick)) pick[k] = r[k]; });
    });
    if (!html.hasAttribute("data-user-theme")) setAttr("theme", pick.theme || base.theme);
    if (!html.hasAttribute("data-user-variant")) setAttr("variant", pick.variant || base.variant);
    setAttr("season", pick.season || base.season);
  }
  apply();
  setInterval(apply, 60000);
})();
