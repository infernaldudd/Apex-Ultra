from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PROTO = ROOT / "references" / "adversarial-judge.md"

class JudgeContractTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(PROTO.exists(), "adversarial-judge.md must exist")
        self.text = PROTO.read_text(encoding="utf-8")
        self.lower = self.text.lower()

    def test_review_dimensions(self):
        phrases = [
            "requirement coverage", "functionality", "robustness", "usability",
            "performance", "security/privacy", "reproducibility", "honesty of testing claims"
        ]
        for phrase in phrases:
            self.assertIn(phrase, self.lower)

    def test_finding_schema(self):
        for field in ["ID", "severity", "requirement", "evidence_or_suspicion", "reproduction", "proposed_fix", "status"]:
            self.assertIn(field, self.text)
        for sev in ["critical", "high", "medium", "low"]:
            self.assertIn(sev, self.lower)

    def test_verdicts_and_re_review(self):
        for verdict in ["PASS", "PASS WITH LIMITATIONS", "FAIL", "UNVERIFIED"]:
            self.assertIn(verdict, self.text)
        self.assertIn("re-review", self.lower)
        self.assertIn("self-review", self.lower)
        self.assertIn("independent", self.lower)

    def test_no_invented_findings(self):
        self.assertIn("do not invent", self.lower)
        self.assertIn("suspicion", self.lower)
        self.assertIn("evidence", self.lower)

if __name__ == "__main__":
    unittest.main()
