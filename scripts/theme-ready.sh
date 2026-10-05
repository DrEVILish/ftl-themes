#!/usr/bin/env bash
# "Ready for review" gate for one theme (PLAN.md §24): build, lint, core
# regressions, the v5 audit, axe, size budgets and render cost, then a
# PASS/FAIL/WARN line per gate. Exit 1 if any gate FAILs; WARN gates
# (budgets, render cost) are reported until v5 ships.
#
#   scripts/theme-ready.sh <slug> [--engine chromium|firefox|webkit]...
#
# The engine flags go to the rendered checks (default chromium; an engine
# that isn't installed is skipped). Full logs: $TMPDIR/theme-ready-<slug>/.
set -uo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"

slug="${1:-}"
[[ "$slug" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ && -f "themes/$slug/theme.css" ]] || { echo "usage: scripts/theme-ready.sh <slug> [--engine name]..." >&2; exit 2; }
shift
engines=("$@")
if ! logs="$(mktemp -d "${TMPDIR:-/tmp}/theme-ready-$slug.XXXXXX")"; then
  echo "could not create theme-ready log directory" >&2
  exit 1
fi

summary=()
# gate <name> <log> <fail-status> <command...>: runs it, keeps the log,
# records PASS or <fail-status> with the log's last line.
gate() {
  local name="$1" log="$logs/$2.log" bad="$3"; shift 3
  [ -t 1 ] && printf '%-18s running…\r' "$name"
  if "$@" >"$log" 2>&1; then st=PASS; else st="$bad"; fi
  local last; last="$(awk 'NF {line=$0} END {print line}' "$log" | cut -c1-110)"
  summary+=("$(printf '%-5s %-18s %s' "$st" "$name" "$last")")
  printf '%-5s %-18s %s\n' "$st" "$name" "$last"
  [ "$st" = PASS ]
}

budget_check() {
  local n
  n="$(grep -Fc "warn  $slug: [budget]" "$logs/lint.log" || true)"
  echo "$n budget warning(s)"
  [ "$n" -eq 0 ]
}

echo "theme-ready: $slug"
gate build          build          FAIL scripts/build.sh || exit 1

# The theme plus its palette variants (variants run on the dashboard only).
entries=()
while IFS= read -r entry; do entries+=("$entry"); done < <(python3 -c '
import json, sys
for t in json.load(open("dist/themes.json")):
    if t["slug"] == sys.argv[1]:
        print(t["slug"]); [print(t["slug"] + "~" + v["id"]) for v in t.get("variants", [])]
' "$slug" 2>/dev/null)
[ ${#entries[@]} -gt 0 ] || entries=("$slug")
theme_args=(); for e in "${entries[@]}"; do theme_args+=(--theme "$e"); done
# axe attributes a rule to the theme by comparing it with a reference theme.
ref=blue-future; [ "$slug" = blue-future ] && ref=windows95

echo "variants: ${entries[*]}"
gate lint           lint           FAIL python3 scripts/check.py --theme "$slug" --budgets
gate core-regress   core           FAIL node scripts/core_regressions.mjs "${engines[@]}" "$slug"
gate v5-audit       v5-audit       FAIL node scripts/v5_audit.mjs "${theme_args[@]}" --page dashboard --page components --page nesting --strict "${engines[@]}"
gate a11y           a11y           FAIL node scripts/a11y_audit.mjs "${theme_args[@]}" --theme "$ref" --blame "$slug" "${engines[@]}"
# Budgets are warnings in check.py; this gate turns its [budget] lines into WARN.
gate budgets        budgets        WARN budget_check
gate render-cost    render         WARN node scripts/render_cost.mjs --theme "$slug" --strict

echo
echo "Budgets (KiB):"
sed -n '/^theme .*bundle gz/,/^$/p' "$logs/lint.log"
grep "^warn  $slug: \[budget\]" "$logs/lint.log"
sed -n '/avg ms/,/^$/p' "$logs/render.log"

grep -h '^SKIP' "$logs"/*.log | sort -u
echo
echo "---- ready for review: $slug ----"
printf '%s\n' "${summary[@]}"
echo "Logs: $logs/"
if printf '%s\n' "${summary[@]}" | grep -q '^FAIL'; then
  echo "NOT READY: fix the FAIL gates (open the log beside each)."; exit 1
fi
echo "READY for review (check WARN gates and look at the theme at every tier yourself)."
