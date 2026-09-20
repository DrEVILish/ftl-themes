#!/usr/bin/env bash
# Lints every theme against the contract. Each rule here exists because the
# corresponding bug actually shipped once — see CHANGELOG.md.
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"
exec python3 scripts/check.py "$@"
