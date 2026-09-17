# Small Task Dry Run — Synthetic Demonstration

This is a **synthetic demonstration**, not evidence from a real user product.

## Scope

Task: correct a one-line text formatter so empty input returns an empty string instead of raising.

### Requirement

- `REQ-001`: empty input must return `""` without error.

## Target

Applicable +5 factors: none.

- `F = 0`
- `Target T: 10`

Only four distinct checks are meaningful for this tiny example. The remaining target gap is explicitly `NOT_APPLICABLE`; **no padding** with duplicate checks is allowed.

## Baseline

- `CHK-001` — empty input behavior — **FAIL**: formatter raises `IndexError`.
- `CHK-002` — ordinary word behavior — PASS.
- `CHK-003` — whitespace-only behavior — PASS.
- `CHK-004` — non-ASCII text behavior — PASS.
- CHK-005 through CHK-010 — `NOT_APPLICABLE`: no additional distinct requirement/risk surfaces exist in this deliberately tiny example.

## Improvement cycle

### CYC-001

- Trigger: `CHK-001` FAIL.
- HYPOTHESIS: implementation indexes the first character before checking length.
- Change: handle empty input before indexing.
- RETEST: `CHK-001` now PASS.
- Regression: `CHK-002`, `CHK-003`, `CHK-004` remain PASS.

## Judge

### JDG-001 — medium

- Requirement: `REQ-001`
- Evidence: the implementation behavior is fixed, but no regression note initially linked `CHK-001` to the final criterion.
- Proposed fix: add requirement traceability to the final report.
- Status: FIXED.

## Re-review

`REQ-001` now has both targeted evidence (`CHK-001`) and regression evidence. Verdict: PASS.

## Final gate

The final formatter behavior is checked using the repaired artifact, not the pre-fix baseline.

## HANDOFF

State: COMPLETED for this demonstration. Immediate next step: none; this example only demonstrates INIT semantics.
