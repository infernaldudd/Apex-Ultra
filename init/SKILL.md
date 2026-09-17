---
name: init
description: Use when a task is complex, quality-critical, failure-prone, file-producing, or explicitly asks for INIT or maximum verification before completion.
---

# INIT

## Overview

INIT is a quality-first execution discipline: **evidence before confidence**. It increases workflow deliberateness but does not change the model's configured thinking budget, tool permissions, hidden reasoning access, or exact context capacity. Keep private chain-of-thought private; expose concise decisions, evidence, assumptions, and results.

## Explicit activation

Activate only when the user invokes `init`, asks for maximum-quality verification, or an authorized higher-priority workflow activates it. Preserve the original prompt, files, constraints, acceptance criteria, safety rules, and permissions. Never fabricate tests, outputs, screenshots, citations, judge findings, or uploads.

Read when relevant:
- `references/verification-protocol.md`
- `references/adversarial-judge.md`
- `references/handoff-and-packaging.md`

Use `templates/` for file-based reports.

## Required phase machine

```text
INIT-0 DISCOVER
INIT-1 TARGET
INIT-2 BASELINE
INIT-3 EXECUTE_LOOP
INIT-4 REGRESSION
INIT-5 JUDGE
INIT-6 REPAIR_LOOP
INIT-7 FINAL_GATE
INIT-8 HANDOFF_PACKAGE
```

**DISCOVER:** inspect accessible materials; create `REQ-###` acceptance criteria; record assumptions, blockers, and unavailable tools.

**TARGET:** choose meaningful verification count:

```text
T = min(45, 10 + 5 * F)
```

`F` is the count of applicable +5 factors from the verification protocol. `T` ranges 10–45. An unchanged rerun is another execution, not a new distinct check. Never pad the count.

**BASELINE:** capture the strongest practical pre-change evidence before editing.

**EXECUTE_LOOP:** for each bounded work item:

```text
TEST -> STUDY -> THINK (internal) -> DRAFT/IMPLEMENT -> RE-EVALUATE -> PREDICT FAILURES -> FIX -> RETEST
```

Predictions are hypotheses, not test results. Diagnose failures before editing. Repeat only while another cycle has a distinct falsifiable benefit.

**REGRESSION:** record each meaningful check as `PASS`, `FAIL`, `BLOCKED`, `NOT_RUN`, or `NOT_APPLICABLE`; preserve failed evidence and relevant retests.

**JUDGE:** perform a skeptical **self-review** against the original prompt and acceptance criteria. Findings need evidence or must be labeled suspicion. Prioritize `critical` and `high` findings. Same-model judgment is never independent review.

**REPAIR_LOOP:** meaningful findings require targeted repair, targeted retest, regression, and **re-review**. Do not delete persistent findings to obtain a pass.

**FINAL_GATE:** inspect/open/build/run/render the **actual final deliverable** where tools allow. Verify required files, final regression, and requirement verdicts: `PASS`, `PASS WITH LIMITATIONS`, `FAIL`, or `UNVERIFIED`. Never claim completion from test count alone.

**HANDOFF_PACKAGE:** maintain progressive checkpoints because exact context exhaustion cannot be predicted reliably. For file-based work, when possible create and verify:

```text
INIT_FINAL.zip
├── deliverables/
├── reports/INIT_REPORT.md
├── reports/TEST_RESULTS.md
├── reports/JUDGE_REPORT.md
└── HANDOFF.md
```

Reopen the archive and verify integrity before presenting it. External upload requires an available tool, destination, and authorization.

## Completion rule

INIT completes only when material actionable defects are fixed or disclosed, the final artifact has passed the strongest available final gate, meaningful repairs received re-review, evidence is truthful, and handoff/package state is recoverable. Never claim INIT guarantees perfection.
