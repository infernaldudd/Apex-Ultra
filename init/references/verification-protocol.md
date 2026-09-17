# INIT Verification Protocol

Use this reference during `INIT-1 TARGET`, `INIT-3 EXECUTE_LOOP`, and `INIT-4 REGRESSION`.

## Core terms

A **distinct check** is a unique falsifiable verification of a requirement, risk, integration point, artifact, or operating condition.

A **test execution** is one actual run/inspection of a check. Re-running the same check after a change is useful evidence, but an unchanged rerun is not a new distinct check.

An **improvement cycle** is one evidence-driven repair unit: failed/weak evidence -> diagnosis -> targeted change -> targeted retest -> regression as needed.

Keep these three counts separate.

## Verification target

Compute the planning target only after scoping the task:

```text
T = min(45, 10 + 5 * F)
```

`F` is the count of applicable factors below. Add each factor at most once.

1. **+5 — interacting components** or multiple file types/subsystems whose behavior must work together.
2. **+5 — state, persistence, concurrency** or external integration / complex behavioral state.
3. **+5 — user-facing UI**, 3D asset, animation, document layout, or other visually judged output requiring visual QA.
4. **+5 — deployment/build/environment** complexity, meaningful platform variation, packaging/build pipelines, or cross-platform support.
5. **+5 — security, privacy, payments**, authorization, or data-integrity risk, limited to safe and permitted checks.
6. **+5 — broad acceptance criteria** or many independent deliverables.
7. **+5 — prior failures or major unknowns** requiring investigation.

Reference implementation:

```python
def verification_target(applicable_factors: int) -> int:
    if applicable_factors < 0:
        raise ValueError("applicable_factors must be >= 0")
    return min(45, 10 + 5 * applicable_factors)
```

Examples: `F=0 -> 10`, `F=1 -> 15`, `F=3 -> 25`, `F=6 -> 40`, `F>=7 -> 45`.

The target is not a quota. If only seven meaningful distinct checks exist, run those seven and mark the remaining target gap `NOT_APPLICABLE` with a reason. Never invent near-duplicate checks to reach a number.

## Requirement ledger

Give each material requirement an ID:

```text
REQ-###
criterion: observable success condition
verification_strategy: how it will be checked
status: PASS | FAIL | BLOCKED | NOT_RUN | NOT_APPLICABLE
evidence: file/log/command/inspection/source reference
```

A requirement may need multiple checks. Every material check should map to at least one `REQ-###` or explicitly to a documented risk.

## Check ledger

Use one row/object per distinct check:

```text
CHK-###
purpose:
requirement_or_risk:
method:
environment:
execution_count:
actual_outcome:
evidence:
status: PASS | FAIL | BLOCKED | NOT_RUN | NOT_APPLICABLE
```

Rules:

- `PASS` requires observed evidence.
- `FAIL` preserves the failure and its evidence even after a later retest passes.
- `BLOCKED` means the check is meaningful but cannot currently run because a required capability/dependency/access item is missing.
- `NOT_RUN` means it could run but was not executed; explain why.
- `NOT_APPLICABLE` means the check/target category genuinely does not apply; explain why.
- A timeout/crash is not automatically a product failure; classify based on what the evidence establishes.
- Never rewrite a prior failed execution as if it never occurred.

## Hypotheses are not evidence

Predicted outcomes and plausible failure modes must be stored separately:

```text
HYPOTHESIS: [what might fail and why]
OBSERVED: [actual result, only after execution/inspection]
```

A hypothesis may motivate a new `CHK-###`, but it never counts as a passed or failed test until checked.

## Improvement cycle ledger

For every material repair, record:

```text
CYC-###
triggering_check_or_judge_finding:
failing_evidence:
hypothesis:
change:
targeted_retest:
regression_checks:
result:
```

A cycle count is not a quality score. Repeat cycles only while the next action has a distinct, falsifiable benefit.

## Building a useful check set

Prefer coverage across different failure surfaces rather than many variants of one easy check. Depending on the task, candidate categories include:

- acceptance-criterion fidelity
- unit behavior
- integration behavior
- startup/build/install
- primary user flow
- error flow/recovery
- persistence/state transition
- edge/boundary input
- artifact open/render/parse
- visual/layout/reference comparison
- accessibility/usability
- performance/resource behavior when measurable
- packaging/file completeness
- deployment/environment compatibility
- security/privacy/permission boundaries
- regression of previously working behavior

Only use categories that materially apply.

## Retest rules

After a targeted fix:

1. Re-run the exact failing/weak check first.
2. If it passes, run nearby regression checks that could plausibly be affected.
3. If regression fails, open a new cycle rather than calling the repair complete.
4. Count these as additional **test executions**; they do not become new distinct checks unless they test a genuinely different condition.

## Stop conditions

Stop adding cycles when any of these is true:

- all acceptance criteria pass with adequate evidence;
- remaining failures are disclosed and blocked/unresolved;
- the user imposed a hard limit;
- available tools cannot create new evidence;
- the next repetition would be an unchanged rerun with no new falsifiable condition;
- continuing would violate scope, safety, authorization, or resource constraints.

## Minimum reporting summary

At regression completion, report:

```text
Target T:
Applicable +5 factors:
Distinct checks planned:
Distinct checks executed:
Test executions total:
Improvement cycles:
PASS / FAIL / BLOCKED / NOT_RUN / NOT_APPLICABLE counts:
Material unresolved risks:
```
