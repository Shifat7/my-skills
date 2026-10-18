# Review

Two passes. Blocker means the change does not merge.

## Pass 1. The change itself

- [ ] Behaviour matches the issue, not a second goal invented during the session.
- [ ] Deterministic work stayed in code. A model call has a reason and a cost log.
- [ ] User data cannot leak across users.
- [ ] New behaviour has a test that fails when the behaviour breaks.
- [ ] Migrations can go backwards, or the ADR says why not.
- [ ] External calls have a timeout. A retry cannot double-apply a side effect.

## Pass 2. The gate

- [ ] Every command in `AGENTS.md` Verification is in `.github/workflows/ci.yml`.
- [ ] The named CI checks are SUCCESS on this commit. Skipped is not success.
- [ ] The pull request has "decisions made without you", or an explicit None.
- [ ] A look-and-feel diff links both states and a test in the named checks.
- [ ] `docs/doc-drift.md` was applied. Stale docs are a Blocker.
- [ ] `scripts/session-status.sh` was run. Dirty files and an unarmed hook are named, not waved through.

## Severity

| Level | Action |
|---|---|
| Blocker | Fix before merge |
| Suggestion | This change or a follow-up issue |
| Note | Later |

A second pass, in a fresh context, gets the diff and the Verification
commands. It does not get the session that wrote the change. Use it when
the first pass found nothing on a non-trivial diff.
