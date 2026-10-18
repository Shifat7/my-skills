# Agentic project template

Starter for a production repo, whether or not agents write the code.

The checks fail when the instructions and the CI workflow disagree. That is
the point. A paragraph that says "run the tests" does not.

## Start a repo from this

1. Copy this directory. Do not clone it and keep building on the template history.
2. Replace the `REPLACE_ME` product sentence in `AGENTS.md` and the title below.
3. Add the project's test command to the Verification section of `AGENTS.md`
   and to `.github/workflows/ci.yml` in the same change. Use the mode that
   exits non-zero on failure.
4. Run `scripts/setup-hooks.sh` once. Until you do, `.githooks/pre-push` does
   not run.
5. Run the Verification commands. They should pass before the first feature.

## Skills, in order

Run the step whose condition is true. Skip the rest. Do not install a second
lifecycle router beside this list.

1. **`/office-hours`**, if gstack is already installed globally. Condition: the product sentence is still `REPLACE_ME`, or the user outcome is unknown. Otherwise write that sentence. gstack is not copied into this repo.
2. **`skills/grill-with-docs`**. Condition: requirements or domain words are still fuzzy. It calls the vendored `grilling` and `domain-modeling` skills and can write a glossary and ADRs. Skip when the issue already states the behaviour and the words.
3. **`skills/issue-first`**. Condition: the next change is a bug or a feature. Skip only an invisible chore, and say why. If `gh` cannot open the issue, stop.
4. **`/plan-ceo-review`**, then **`/plan-eng-review`**, if gstack is installed. Condition: a module boundary, a new service or datastore, or a wrong guess that would waste more than about an hour.
5. **`skills/diagnosing-bugs`**. Condition: something fails and the cause is unknown. Use gstack `/investigate` only when this loop is not enough.
6. **`skills/tdd`**. Condition: you are implementing or changing behaviour. Agree the public test seam first. Open `codebase-design` only when that seam is itself undecided.
7. **`skills/source-driven-development`**. Condition: a framework, API, or library choice would otherwise come from model memory. Cite the current official source.
8. **`skills/security-and-hardening`**. Condition: the change touches untrusted input, auth, secrets, or stored user data.
9. **`skills/browser-testing-with-devtools`**. Condition: the change has a running browser surface. Skip for a change nobody can click.
10. **`skills/performance-optimization`**. Condition: a measurement shows a regression. No measurement, no performance work.
11. **`skills/observability-and-instrumentation`**. Condition: this is a production service and a failure would be invisible.
12. **`skills/ci-cd-and-automation`**. Condition: the change is to the build, test, or deploy pipeline.
13. **`skills/verify`**. Condition: you are about to claim the change works. It runs the Verification commands and does not edit. `blocked` is not a pass.
14. **`/qa`**, if gstack is installed. Condition: a person can click or see the change. A screenshot counts only beside a command that exited 0.
15. **`/review`**, if gstack is installed, otherwise `docs/review-template.md`. Condition: every commit before it is pushed, including later commits on the same pull request.
16. **Fresh-context second pass**. Condition: the review found no Blocker and the diff is non-trivial. Give that context the diff and the Verification commands, not the writing session.
17. **`skills/shipping-and-launch`**. Condition: you are preparing a production deploy. Opening a pull request is not a deploy.
18. **`/ship`**, if gstack is installed. Condition: verify passed, review is done, and the tree is clean. The named CI checks still have to be SUCCESS. Otherwise open the pull request with `.github/pull_request_template.md`.
19. **`skills/session-end`**. Condition: you are leaving. It runs `scripts/session-status.sh`. Dirty files, an unarmed hook, no upstream, or a failing verify-block means not done.
20. **`skills/retro`**. Condition: the session was painful or repeated a mistake. It calls `writing-for-agents`. A mechanical miss becomes a check, not another paragraph.

`writing-for-agents` also applies whenever you edit `AGENTS.md` or a skill.
Superpowers is not installed here. Use that whole pack only for a separately
approved, large autonomous implementation, in a repo that does not also route
through this list.

## What you get

| Path | Role |
|---|---|
| `AGENTS.md` | Only instruction file. `CLAUDE.md` points here. |
| `skills/issue-first` | Open the issue before building. |
| `skills/verify` | Run the commands. Do not edit. Return pass, fail, or blocked. |
| `skills/session-end` | Dirty, unhooked, or unpushed is not done. |
| `scripts/check-verify-block.py` | Fails if a Verification command is missing from CI. |
| `scripts/fast-gate.sh` | Syntax gate. Add the language linter here, in failing mode. |
| `scripts/session-status.sh` | Status from the tree, not from a checkbox file. |
| `docs/adr/` | Decisions. Supersede in place. Do not delete the old sentence. |
| `docs/review-template.md` | Two-pass review. Blockers include a skipped check. |
| `docs/doc-drift.md` | The checklist review skills usually skip. |
| `.github/workflows/ci.yml` | Named checks. They run on pull requests and on pushes to `main`. |
| `.github/pull_request_template.md` | Decisions made without the user, plus the commands you ran. |

Selected skills from Matt Pocock (`49dd158`) and Addy Osmani (`aeac41d`)
are copied under `skills/`, with the shared checklists they link under
`references/`. Pins and licenses are in `docs/adr/0002-vendored-skills.md`.
gstack and Superpowers are not copied. The local `issue-first`, `verify`,
and `session-end` skills still apply if those packs are absent.

## What was left out on purpose

Personal voice and punctuation rules, a specific model vendor, merging with
`--admin`, treating a BLOCKED pull request as success, and opening a browser
by name. Those were true for one app and one GitHub ruleset. Add them in an
ADR if this product needs them.

## Version

`VERSION` is `0.0.0` until runtime behaviour exists. Docs, CI, scripts, and
these instructions do not bump it.
