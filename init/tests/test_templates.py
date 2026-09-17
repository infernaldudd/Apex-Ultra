from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
TDIR = ROOT / "templates"
FILES = ["INIT_REPORT.md", "TEST_RESULTS.md", "JUDGE_REPORT.md", "HANDOFF.md"]

class TemplateTests(unittest.TestCase):
    def setUp(self):
        for name in FILES:
            self.assertTrue((TDIR / name).exists(), f"missing template {name}")

    def test_common_truthfulness_instruction(self):
        for name in FILES:
            text = (TDIR / name).read_text(encoding="utf-8")
            self.assertIn("never fabricate evidence", text.lower())
            self.assertNotIn("T" + "BD", text)
            self.assertNotIn("T" + "ODO", text)

    def test_init_report_sections(self):
        text = (TDIR / "INIT_REPORT.md").read_text(encoding="utf-8")
        for term in ["Scope", "Target calculation", "Requirement matrix", "Completion state", "Limitations", "Deliverables"]:
            self.assertIn(term, text)

    def test_test_results_separate_counts(self):
        text = (TDIR / "TEST_RESULTS.md").read_text(encoding="utf-8")
        for term in ["Distinct checks", "Test executions", "Improvement cycles", "Evidence", "Status"]:
            self.assertIn(term, text)

    def test_judge_report_has_both_passes(self):
        text = (TDIR / "JUDGE_REPORT.md").read_text(encoding="utf-8")
        for term in ["Initial self-review", "Fixes and retests", "Re-review", "JDG-###"]:
            self.assertIn(term, text)

    def test_handoff_is_restart_oriented(self):
        text = (TDIR / "HANDOFF.md").read_text(encoding="utf-8")
        for term in ["Original request", "Current state", "Resume commands", "Single immediate next action", "Packaging status"]:
            self.assertIn(term, text)

if __name__ == "__main__":
    unittest.main()
