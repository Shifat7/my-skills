# Agent instructions

This file is the source of truth for humans and agents. `CLAUDE.md` is a
symlink to it so Claude and Codex cannot drift apart.

## Product

REPLACE_ME: one sentence describing what a user can do when this works.

## Precedence

1. A failing command beats a paragraph in this file.
2. If gstack (or another installed skill pack) is present, use its skill for
   the matching task below. Do not invent a second copy of that workflow.
3. The local skills in `skills/` are the floor. They still apply when no
   external skill pack is installed.
4. Repo-specific exceptions to an external skill are written here as numbered
   amendments. An unlisted exception is the agent improvising.

Numbered amendments:

1. Do not merge with `--admin`, and do not treat a BLOCKED merge state as
   success. Those belong to one GitHub ruleset on one other repo.
2. A look-and-feel change needs the default state and the after-interaction
   state, plus a test that fails if both states are selected. That test
   command must appear in the Verification section and in CI.
3. Ask only for the three triggers in Decision policy. Otherwise decide, and
   record the choice in the pull request.

## Skill routing

Use one skill for the step you are on. Do not load a second lifecycle
router (`using-agent-skills` or Superpowers) in this repo. gstack and
Superpowers stay outside the repo: gstack only if it is already installed
globally, Superpowers only for an approved long autonomous run.

| Order | Skill | Condition |
|---|---|---|
| 1 | `/office-hours` if gstack is installed | The product sentence above is still `REPLACE_ME`, or the user outcome is unknown. Otherwise write that sentence and continue. |
| 2 | `skills/grill-with-docs` | Requirements or domain words are still fuzzy. It calls `grilling` and `domain-modeling`. Skip when the issue already states the behaviour and the words. |
| 3 | `skills/issue-first` | The change is a bug or feature. Skip only an invisible chore, and say why. |
| 4 | `/plan-ceo-review`, then `/plan-eng-review`, if gstack is installed | A boundary, a new service or datastore, or a wrong guess that would waste more than about an hour. |
| 5 | `skills/diagnosing-bugs` | Something fails and the cause is unknown. Use `/investigate` only when gstack is installed and this skill is not enough. |
| 6 | `skills/tdd` | Implementing or changing behaviour. Agree the public seam first. Consult `codebase-design` only when the seam itself is undecided. |
| 7 | `skills/source-driven-development` | A framework, API, or library choice would otherwise come from model memory. |
| 8 | `skills/security-and-hardening` | The change touches untrusted input, auth, secrets, or stored user data. |
| 9 | `skills/browser-testing-with-devtools` | The change has a running browser surface. |
| 10 | `skills/performance-optimization` | A measurement shows a regression. No measurement, no performance work. |
| 11 | `skills/observability-and-instrumentation` | The change is on a production service and a failure would be invisible. |
| 12 | `skills/ci-cd-and-automation` | The change is to the build, test, or deploy pipeline. |
| 13 | `skills/verify` | About to claim the change works. It runs Verification and does not edit. |
| 14 | `/qa` if gstack is installed | A person can click or see the change. A screenshot counts only beside a command that exited 0. |
| 15 | `/review` if gstack is installed, else `docs/review-template.md` | Every commit before it is pushed. |
| 16 | Fresh-context second pass | The review found no Blocker and the diff is non-trivial. |
| 17 | `skills/shipping-and-launch` | Preparing a production deploy, not merely opening a pull request. |
| 18 | `/ship` if gstack is installed | Verify passed, review is done, and the tree is clean. Named CI checks must still be SUCCESS. |
| 19 | `skills/session-end` | Leaving the session. |
| 20 | `skills/retro` | The session was painful or repeated a mistake. It calls `writing-for-agents`. A mechanical miss becomes a check, not another paragraph. |

`writing-for-agents` also applies whenever you edit `AGENTS.md` or a skill.
`scripts/session-status.sh` is the status command for step 19. It is not a skill.

## Principles

1. Deterministic by default. Use a model only where a program cannot do the job. Log the cost of every model call.
2. User data is scoped to a user. A query that can see another user's rows is a defect.
3. Done means the named CI checks succeeded on this commit, on the default branch or an open pull request. A dirty tree is not done.
4. Decide, and log the decision, except for the three ask triggers. When thorough and fast conflict, pick thorough.
5. Superseded instructions stay in the ADR, marked superseded. Deleting them lets the next agent restore them.

## Decision policy

Ask only when one of these is true:

1. Design or look-and-feel, including copy tone.
2. Irreversible or costly: money, production data, publishing, deleting something the agent did not create.
3. A scope fork where a wrong guess wastes more than about an hour.

Everything else: choose the recommended option and add it to the pull request under "decisions made without you", with why and an undo cost of low, med, or high.

An allowlist is not a sandbox. Do not run this repo unattended, merge it, or deploy it from a session that nobody is watching.

## Working agreements

1. Issue first. The issue states the ask in the user's words before implementation starts. Invisible chores (formatting, a dependency bump with no behaviour change) may skip the issue.
2. Branch from the default branch: `feat/`, `fix/`, `refactor/`, `docs/`, `test/`, `chore/`.
3. One worktree for the change. If `git worktree list` already has the work, continue there. Remove the worktree after it merges.
4. Tests land with the behaviour they protect. A test that cannot fail when the behaviour breaks does not count.
5. Review the incremental diff before every push to an open pull request, not only the first commit.
6. Merge only when every named check in `.github/workflows/ci.yml` is SUCCESS. A skipped check is not success. Do not chain "ready" and "merge".
7. Change a step in these agreements only in the same change as the script or workflow that enforces it.
8. Docs that disagree with the code are a defect. Run `docs/doc-drift.md` on any non-trivial change.
9. Bump `VERSION` only when runtime behaviour changes. Docs, CI, scripts, and agent instructions do not bump it.

## Verification

These commands must also appear, unchanged, in `.github/workflows/ci.yml`.
`scripts/check-verify-block.py` fails the build when they do not.

When you add a project test or linter, add the exact command here and in that
workflow in the same change. Point the linter at a mode that exits non-zero.
A warning-only linter is not a gate.

```sh
python3 scripts/check-verify-block.py
python3 -m unittest tests/test_check_verify_block.py
bash scripts/fast-gate.sh
```

## Commit messages

Subject: `<prefix>: <what changed> (#issue)`

Prefixes: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`.

Body: the failure shape, then the mechanism. Not a list of files.

## What this file will not tell you

Voice, punctuation, brand, model vendor, and merge-bypass flags are product
choices. Write them in an ADR when they exist. Do not import them from
another repo.
