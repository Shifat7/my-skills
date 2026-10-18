# 0002. Which external skills are copied

Date: 2026-10-19
Status: accepted

## Context

Public skill packs disagree on popularity, production coverage, and cost.
Superpowers has the most GitHub stars. Matt Pocock's skills have the most
installs and the strongest practitioner reuse. Addy Osmani's agent-skills
cover the production lifecycle the others leave thin. 2026 benchmarks also
show that injecting a broad skill catalog can lower pass rates and raise
token use. gstack is a large harness, not a folder of small skills.

## Decision

Copy only the skills a new production repo should be able to run without
installing a second lifecycle router.

From Matt Pocock, commit `49dd158d1076134a641b33efb035946536778336`:

- `grill-with-docs`, plus `grilling` and `domain-modeling`, because the
  first skill calls the other two
- `codebase-design`, because `tdd` consults it when the test seam is undecided
- `diagnosing-bugs`
- `tdd`
- `retro`
- `writing-for-agents`

From Addy Osmani, commit `aeac41d4d005999432bb7312f7ff06383a91d59d`:

- `source-driven-development`
- `security-and-hardening`
- `browser-testing-with-devtools`
- `performance-optimization`
- `observability-and-instrumentation`
- `ci-cd-and-automation`
- `shipping-and-launch`

The Addy checklists those skills link live in `references/`. Licenses are
`references/MATT-POCOCK-LICENSE` and `references/ADDY-OSMANI-LICENSE`.

Do not copy `using-agent-skills`, the rest of either catalog, Superpowers,
or gstack. gstack may be used from a global install. Superpowers may be
used only for a separately approved long autonomous run, in a repo that is
not also routing through this list.

## Consequences

`skills/` now contains the three local skills plus these copies. Agents
discover their descriptions. The README and `AGENTS.md` say when each one
runs. A skill that tells the agent to skip this repo's Verification
commands loses to `AGENTS.md`.

## Not decided

Re-vendoring on a later upstream commit. Do that as its own change, with
the new commit hashes in this ADR, after the paired with-and-without check
named in the research.
