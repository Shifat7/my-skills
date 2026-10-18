#!/usr/bin/env python3
"""Fail when a Verification command in AGENTS.md is missing from CI.

The command is the gate. A fenced command that exists only in the
instruction file is the failure this script exists to catch.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


def extract_verification(markdown: str) -> str:
    match = re.search(r"^## Verification\s*$", markdown, re.M)
    if not match:
        raise ValueError("AGENTS.md has no ## Verification section")
    rest = markdown[match.end() :]
    nxt = re.search(r"^## ", rest, re.M)
    return rest[: nxt.start()] if nxt else rest


def commands_in(section: str) -> list[str]:
    commands: list[str] = []
    for fence in re.finditer(r"```(?:sh|bash)\n(.*?)```", section, re.S):
        for line in fence.group(1).splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            commands.append(stripped)
    if not commands:
        raise ValueError("## Verification contains no fenced sh commands")
    return commands


def missing(commands: list[str], workflow: str) -> list[str]:
    return [cmd for cmd in commands if cmd not in workflow]


def check(agents_path: Path, workflow_path: Path) -> list[str]:
    if not agents_path.is_file():
        return [f"missing {agents_path}"]
    if not workflow_path.is_file():
        return [f"missing {workflow_path}"]
    try:
        commands = commands_in(extract_verification(agents_path.read_text()))
    except ValueError as exc:
        return [str(exc)]
    return missing(commands, workflow_path.read_text())


def main(argv: list[str]) -> int:
    root = Path(__file__).resolve().parents[1]
    agents = Path(argv[1]) if len(argv) > 1 else root / "AGENTS.md"
    workflow = Path(argv[2]) if len(argv) > 2 else root / ".github" / "workflows" / "ci.yml"
    gaps = check(agents, workflow)
    if gaps:
        print("verify-block: these Verification commands are not in CI:", file=sys.stderr)
        for gap in gaps:
            print(f"  {gap}", file=sys.stderr)
        return 1
    print("verify-block: every Verification command is in CI")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
