---
name: issue-first
description: Use before implementing a bug or feature. Capture the ask in the user's words as a GitHub issue, then stop if that issue cannot be opened.
---

# Issue first

The issue is the ask. A later commit message is not a substitute.

## Do

1. Write the issue title and body from the user's words. Do not widen the goal.
2. Open it with `gh issue create` when `gh` is authenticated.
3. Carry the issue number into the branch name and the commit subject.

## Stop

- `gh` is missing or not authenticated. Report that and do not start the change.
- The user already pointed at an issue number. Read it. Do not open a second one.
- The change is an invisible chore (formatting, a dependency bump with no behaviour change). Say that you are skipping the issue and why.

## Do not

- Invent a second statement of the goal in a todo file and treat that file as newer than the issue.
- Start `/ship`, a plan review, or an implementation session before the issue exists.
