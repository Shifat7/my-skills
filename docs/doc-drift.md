# Doc drift

Run this against the diff. The review skill's usual categories do not cover
these. A doc that disagrees with the code is a Blocker.

- Instruction, skill, or working-agreement change: the same rule is not
  contradicted by `AGENTS.md`, `README.md`, or an ADR that is still accepted.
- New or renamed Verification command: it appears in `AGENTS.md` and in
  `.github/workflows/ci.yml`.
- New architecture boundary (service, external API, datastore): an ADR or
  `README.md` names it. A diagram, if you have one, was regenerated from its
  source, not edited as a picture.
- User-facing route or command rename: the old name is gone from docs, or an
  ADR says it remains on purpose.
- `VERSION` changed on a docs-only, CI-only, or script-only diff: revert the
  bump. `VERSION` means what is running.
- A superseded decision was deleted instead of marked superseded: put the
  old sentence back, marked superseded, in the ADR.
