"""The verify-block check fails when a documented command never runs in CI.

A command that exists only in AGENTS.md is the defect. A command that
exists in both places is the passing case. Comments are not commands.
"""

import importlib.util
import tempfile
import unittest
from pathlib import Path

_PATH = Path(__file__).resolve().parents[1] / "scripts" / "check-verify-block.py"
_spec = importlib.util.spec_from_file_location("check_verify_block", _PATH)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
check = _mod.check
commands_in = _mod.commands_in
extract_verification = _mod.extract_verification


AGENTS = """# Instructions

## Verification

```sh
# not a command
python3 scripts/check-verify-block.py
echo kept
```

## Later

```sh
echo not in verification
```
"""


class VerifyBlockTest(unittest.TestCase):
    def test_verification_section_stops_at_the_next_heading(self):
        section = extract_verification(AGENTS)
        cmds = commands_in(section)
        self.assertEqual(cmds, ["python3 scripts/check-verify-block.py", "echo kept"])

    def test_missing_ci_command_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            agents = root / "AGENTS.md"
            workflow = root / "ci.yml"
            agents.write_text(AGENTS)
            workflow.write_text("run: python3 scripts/check-verify-block.py\n")
            self.assertEqual(check(agents, workflow), ["echo kept"])

    def test_wired_commands_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            agents = root / "AGENTS.md"
            workflow = root / "ci.yml"
            agents.write_text(AGENTS)
            workflow.write_text(
                "run: python3 scripts/check-verify-block.py\nrun: echo kept\n"
            )
            self.assertEqual(check(agents, workflow), [])

    def test_this_template_is_wired(self):
        root = Path(__file__).resolve().parents[1]
        self.assertEqual(
            check(root / "AGENTS.md", root / ".github" / "workflows" / "ci.yml"),
            [],
        )


if __name__ == "__main__":
    unittest.main()
