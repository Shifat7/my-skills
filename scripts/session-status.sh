#!/usr/bin/env bash
# Print landing state. This output is the status. Do not copy it into a
# checkbox file and then treat the file as newer than the tree.
set -euo pipefail

root=$(cd "$(dirname "$0")/.." && pwd)
cd "$root"

branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || true)
[ -n "$branch" ] || branch="no-git"
hooks=$(git config --get core.hooksPath || echo "unset")
dirty=$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ')
worktrees=$(git worktree list 2>/dev/null | wc -l | tr -d ' ')
upstream=$(git rev-parse --abbrev-ref --symbolic-full-name '@{upstream}' 2>/dev/null || echo "none")

echo "branch: $branch"
echo "upstream: $upstream"
echo "dirty: $dirty"
echo "worktrees: $worktrees"
echo "hooksPath: $hooks"

if python3 scripts/check-verify-block.py >/dev/null 2>&1; then
  echo "verify-block: pass"
else
  echo "verify-block: fail"
fi

if [ "$dirty" != "0" ] || [ "$hooks" = "unset" ] || [ "$upstream" = "none" ]; then
  echo "landing: not-done"
  exit 1
fi

echo "landing: check the open PR or default branch before calling this done"
exit 0
