---
description: Show landing state from the tree. Read-only.
---

Run `scripts/session-status.sh`.

Show the raw output. Do not trim it.

Under that, at most three bullets for what to do next. Prefer, in order:
a non-zero dirty count, an unarmed hook, a failing verify-block, then an
unpushed branch.

Do not commit, push, open issues, or edit files. If the script is missing,
stop.
