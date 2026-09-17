from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PROTO = ROOT / "references" / "handoff-and-packaging.md"

class PackagingContractTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(PROTO.exists(), "handoff-and-packaging.md must exist")
        self.text = PROTO.read_text(encoding="utf-8")
        self.lower = self.text.lower()

    def test_archive_layout(self):
        for token in [
            "INIT_FINAL.zip", "deliverables/", "reports/INIT_REPORT.md",
            "reports/TEST_RESULTS.md", "reports/JUDGE_REPORT.md", "HANDOFF.md"
        ]:
            self.assertIn(token, self.text)

    def test_progressive_checkpoint_and_context_truth(self):
        self.assertIn("progressive checkpoint", self.lower)
        self.assertIn("exact context", self.lower)
        self.assertIn("cannot", self.lower)
        self.assertIn("single immediate next step", self.lower)

    def test_archive_verification(self):
        for phrase in ["reopen", "testzip", "nonempty", "source", "destination"]:
            self.assertIn(phrase, self.lower)

    def test_secret_and_upload_boundaries(self):
        for phrase in ["secret", "credential", "private key", "authorization", "external upload", "available tool"]:
            self.assertIn(phrase, self.lower)

if __name__ == "__main__":
    unittest.main()
