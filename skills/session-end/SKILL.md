---
name: session-end
description: Use at the end of a working session. The session is not done until the tree is clean, the hook is armed, and the commit is on the default branch or an open pull request.
---

# Session end

Run `scripts/session-status.sh` and paste its output. That output is the status.

## Not done

Any of these means the session is not done:

- `dirty` is not 0
- `hooksPath` is `unset` (run `scripts/setup-hooks.sh` once per clone)
- `upstream` is `none`
- `verify-block` is `fail`
- `git worktree list` shows another tree holding this same change
- The only evidence of QA is an image

Say which line failed and the next command. Do not write a checkbox file to stand in for the script.

## Done

`dirty` is 0, `hooksPath` is set, `verify-block` is pass, and this commit is on the default branch or an open pull request whose named CI checks are SUCCESS.

One change per session. Leave the next session a commit it can trust, not a pile of uncommitted files.
