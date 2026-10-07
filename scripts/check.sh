#!/usr/bin/env bash
# Lints every theme against the contract. Each rule here exists because the
# corresponding bug actually shipped once — see CHANGELOG.md.
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"
python3 scripts/check.py "$@"
python3 scripts/test_cssparse.py
python3 scripts/motion_always.py --test
python3 scripts/build_component_index.py --check
python3 test/feature_extensions.py
python3 test/feature_edge_cases.py
node test/feature_bridges.mjs
node test/feature_extensions_browser.mjs
