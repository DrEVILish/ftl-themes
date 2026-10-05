/* Scenario controls are demo behavior; live applications own their state. */
(function () {
  var select = document.getElementById("dashboard-scenario");
  var dashboard = document.getElementById("dashboard-demo");
  var connection = document.getElementById("dashboard-connection");
  var note = document.getElementById("dashboard-scenario-note");
  if (!select || !dashboard || !connection || !note) return;
  var states = {
    live: ["live", "Analytics feed live", "Live metrics are current."],
    stale: ["delayed", "Analytics feed delayed", "Showing the last received values; the feed is delayed."],
    offline: ["offline", "Analytics feed offline", "Values are unavailable until the connection returns."],
    alert: ["live", "Analytics feed live; Error rate alert", "One metric is in alert; zero and missing values remain distinct."],
    recovering: ["recovering", "Analytics feed recovering", "Connection restored; fresh values are arriving."]
  };
  function render() {
    var state = states[select.value] || states.live;
    dashboard.dataset.scenario = select.value;
    connection.dataset.state = state[0];
    connection.textContent = state[1];
    note.textContent = state[2];
    dashboard.querySelectorAll(".demo-metric").forEach(function (card, i) {
      card.classList.toggle("is-stale", select.value === "stale" || select.value === "offline");
      card.classList.toggle("is-error", select.value === "alert" && i === 3);
    });
  }
  select.addEventListener("change", render);
  render();
})();
