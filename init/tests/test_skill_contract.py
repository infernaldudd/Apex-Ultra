from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"

class SkillContractTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(SKILL.exists(), "SKILL.md must exist")
        self.text = SKILL.read_text(encoding="utf-8")
        self.lower = self.text.lower()

    def test_frontmatter_and_discovery_description(self):
        self.assertRegex(self.text, r"(?s)^---\nname: init\ndescription: Use when .+?\n---")

    def test_explicit_activation_and_phase_machine(self):
        self.assertIn("explicit activation", self.lower)
        for phase in [
            "INIT-0 DISCOVER", "INIT-1 TARGET", "INIT-2 BASELINE",
            "INIT-3 EXECUTE_LOOP", "INIT-4 REGRESSION", "INIT-5 JUDGE",
            "INIT-6 REPAIR_LOOP", "INIT-7 FINAL_GATE", "INIT-8 HANDOFF_PACKAGE",
        ]:
            self.assertIn(phase, self.text)

    def test_target_formula_is_bounded_and_deterministic(self):
        self.assertIn("T = min(45, 10 + 5 * F)", self.text)
        self.assertIn("10", self.text)
        self.assertIn("45", self.text)
        self.assertIn("unchanged rerun", self.lower)

    def test_requested_execution_loop_exists(self):
        required = ["TEST", "STUDY", "THINK", "DRAFT/IMPLEMENT", "RE-EVALUATE", "PREDICT FAILURES", "FIX", "RETEST"]
        for term in required:
            self.assertIn(term, self.text)

    def test_judge_repair_rejudge_required(self):
        self.assertIn("self-review", self.lower)
        self.assertIn("re-review", self.lower)
        self.assertIn("critical", self.lower)
        self.assertIn("high", self.lower)

    def test_final_artifact_gate_and_handoff(self):
        self.assertIn("actual final deliverable", self.lower)
        self.assertIn("HANDOFF.md", self.text)
        self.assertIn("INIT_FINAL.zip", self.text)
        self.assertIn("TEST_RESULTS.md", self.text)
        self.assertIn("JUDGE_REPORT.md", self.text)

    def test_honesty_and_private_reasoning_boundaries(self):
        self.assertIn("never fabricate", self.lower)
        self.assertIn("private chain-of-thought", self.lower)
        self.assertIn("does not change", self.lower)
        self.assertIn("thinking budget", self.lower)
        self.assertIn("never claim init guarantees perfection", self.lower)
        self.assertNotRegex(self.text, r"(?mi)^INIT guarantees perfection[.!]?")

    def test_reference_files_are_named(self):
        for ref in [
            "references/verification-protocol.md",
            "references/adversarial-judge.md",
            "references/handoff-and-packaging.md",
        ]:
            self.assertIn(ref, self.text)

    def test_skill_is_compact_enough_for_repeated_loading(self):
        words = re.findall(r"\b\w+[\w'-]*\b", self.text)
        self.assertLessEqual(len(words), 550, f"SKILL.md is too large: {len(words)} words")

if __name__ == "__main__":
    unittest.main()
