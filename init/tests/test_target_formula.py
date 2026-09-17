from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PROTO = ROOT / "references" / "verification-protocol.md"

class VerificationProtocolTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(PROTO.exists(), "verification-protocol.md must exist")
        self.text = PROTO.read_text(encoding="utf-8")
        self.lower = self.text.lower()

    def test_formula_examples(self):
        def target(f):
            if f < 0:
                raise ValueError
            return min(45, 10 + 5 * f)
        cases = [(0,10),(1,15),(3,25),(6,40),(7,45),(99,45)]
        for f, expected in cases:
            self.assertEqual(target(f), expected)
        self.assertIn("T = min(45, 10 + 5 * F)", self.text)

    def test_factor_catalog(self):
        for phrase in [
            "interacting components", "state, persistence, concurrency", "user-facing UI",
            "deployment/build/environment", "security, privacy, payments", "broad acceptance criteria",
            "prior failures or major unknowns",
        ]:
            self.assertIn(phrase, self.text)

    def test_distinct_concepts_and_statuses(self):
        for term in ["distinct check", "test execution", "improvement cycle"]:
            self.assertIn(term, self.lower)
        for status in ["PASS", "FAIL", "BLOCKED", "NOT_RUN", "NOT_APPLICABLE"]:
            self.assertIn(status, self.text)

    def test_ledger_ids_and_hypothesis_separation(self):
        for token in ["REQ-###", "CHK-###", "CYC-###", "HYPOTHESIS"]:
            self.assertIn(token, self.text)
        self.assertIn("unchanged rerun", self.lower)
        self.assertIn("not a new distinct check", self.lower)

if __name__ == "__main__":
    unittest.main()
