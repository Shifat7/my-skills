# Contributing

## Branches

`feat/`, `fix/`, `refactor/`, `docs/`, `test/`, `chore/`, from the default
branch. One worktree per change.

## Commits

`<prefix>: <what changed> (#issue)`

The body says what broke and what now stops it. Put the issue number in the
subject when there is an issue.

## Pull requests

Use `.github/pull_request_template.md`.

Merge when every named job is SUCCESS on that commit:

- Verification block is wired
- Template sensor tests
- Fast gate

A skipped job is not a success. Do not merge with `--admin`. Do not merge
while the pull request is still a draft if you use drafts. Pushing to `main`
runs CI too. A draft is not a way to hide a red suite.

Review each new commit against the incremental diff before pushing it.

## Hooks

`scripts/setup-hooks.sh` once per clone. Check with
`git config --get core.hooksPath`. `unset` means the hook is not armed.

## Decisions

Record autonomous choices in the pull request. Ask first only for design,
irreversible cost, or a scope fork of more than about an hour.
