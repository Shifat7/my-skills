#!/usr/bin/env bash
# Fast local gate. It must exit non-zero on a real defect.
# A linter that only prints warnings is not a gate. When you add one,
# invoke it here in the mode that fails the process.
set -euo pipefail

root=$(cd "$(dirname "$0")/.." && pwd)

python3 -m py_compile "$root/scripts/check-verify-block.py"

for script in "$root"/scripts/*.sh "$root"/.githooks/pre-push; do
  bash -n "$script"
done

if command -v shellcheck >/dev/null 2>&1; then
  shellcheck "$root"/scripts/*.sh "$root"/.githooks/pre-push
fi

echo "fast-gate: syntax ok"
