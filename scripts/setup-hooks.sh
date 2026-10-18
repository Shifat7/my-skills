#!/usr/bin/env bash
# A hook file in the repo does nothing until this sets core.hooksPath.
set -euo pipefail
root=$(cd "$(dirname "$0")/.." && pwd)
git -C "$root" config core.hooksPath .githooks
echo "hooks armed: $(git -C "$root" config --get core.hooksPath)"
