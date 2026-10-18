# 0001. Operating system for a new repo

Date: 2026-10-18
Status: accepted

## Context

Several of our repos grew instruction files faster than they grew checks.
A task list said work had not started while another worktree had already
built it. Verification commands lived in `AGENTS.md` and never in CI. A
passing test suite sat on a branch the default branch did not contain.
Screenshots stood in for a command. A staff-run app (mynextjob2) showed the
opposite shape: one instruction file, issues before skills, and a script
the commit after a model dropped a prose step. It also carried rules that
do not travel: a personal voice guide, an admin merge bypass, and a
Firefox-only planning tool.

## Decision

This template ships the sensors, not that app's product rules.

- `AGENTS.md` is the only instruction file. `CLAUDE.md` points at it.
- `skills/` holds three local skills: issue-first, verify, session-end.
  External skill packs are routed from `AGENTS.md` and are not copied here.
- `scripts/check-verify-block.py` fails when a Verification command is
  missing from CI. The template's own CI runs that check.
- `scripts/fast-gate.sh` and `.githooks/pre-push` fail on syntax errors.
  The hook does nothing until `scripts/setup-hooks.sh` sets
  `core.hooksPath`.
- `scripts/session-status.sh` is the status. Checkbox files are plans.
- Pull requests record autonomous decisions. Look-and-feel changes need
  both states and a test in the named checks.
- There is no paths-ignore list and no `--admin` merge. A skipped check is
  not success. CI runs on pushes to `main` and on pull requests.
- `VERSION` bumps only when runtime behaviour changes.

## Consequences

A new repo starts with a green check that the instructions and the workflow
name the same commands. Adding a real test without adding it to both places
fails CI. The template does not know the project's language. The first
feature replaces the placeholder product sentence and adds that language's
failing test command in the same change as the workflow step.

## Not decided

Unattended overnight runs. An allowlist cannot enforce "never deploy". That
waits until a real sandbox exists.
