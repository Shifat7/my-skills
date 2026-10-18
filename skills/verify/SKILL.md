---
name: verify
description: Use after research, implementation, or a review to check the change without editing it. Return pass, fail, or blocked.
---

# Verify

The verifier does not modify the tree. A summary is not a result.

## Do

1. Read the Verification section of `AGENTS.md`.
2. Run those commands. Record each exit status.
3. Run `docs/doc-drift.md` against the diff. A disagreement is a fail.
4. Return exactly one of `pass`, `fail`, or `blocked`, then the command output that supports it.

## Meanings

- `pass`: every Verification command exited 0, and the docs that should have changed did.
- `fail`: a command exited non-zero, or a doc contradicts the code.
- `blocked`: a command could not be run (missing tool, missing secret, service down). Say what is missing. Do not estimate a pass.

## Do not

- Fix the failure in this same pass. A fix is a new change, then verify again.
- Treat a screenshot, a checkbox, or "looks good" as `pass`.
- Treat a skipped CI check as `pass`.
