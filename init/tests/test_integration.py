from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class IntegrationTests(unittest.TestCase):
    def test_skill_references_exist(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        refs = [
            "references/verification-protocol.md",
            "references/adversarial-judge.md",
            "references/handoff-and-packaging.md",
        ]
        for rel in refs:
            self.assertIn(rel, skill)
            self.assertTrue((ROOT / rel).exists(), rel)
        for rel in [
            "templates/INIT_REPORT.md", "templates/TEST_RESULTS.md",
            "templates/JUDGE_REPORT.md", "templates/HANDOFF.md",
        ]:
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_small_dry_run_no_padding(self):
        p = ROOT / "examples" / "small-task-dry-run.md"
        self.assertTrue(p.exists())
        text = p.read_text(encoding="utf-8")
        for token in ["Target T: 10", "REQ-001", "CHK-001", "FAIL", "CYC-001", "RETEST", "JDG-001", "Re-review", "HANDOFF", "NOT_APPLICABLE"]:
            self.assertIn(token, text)
        self.assertIn("no padding", text.lower())

    def test_multicomponent_dry_run_scaled_target(self):
        p = ROOT / "examples" / "multicomponent-dry-run.md"
        self.assertTrue(p.exists())
        text = p.read_text(encoding="utf-8")
        for token in ["Target T: 25", "F = 3", "REQ-001", "CHK-001", "FAIL", "CYC-001", "RETEST", "JDG-001", "Re-review", "Final gate", "HANDOFF"]:
            self.assertIn(token, text)
        self.assertIn("synthetic demonstration", text.lower())

if __name__ == "__main__":
    unittest.main()
