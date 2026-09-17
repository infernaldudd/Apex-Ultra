# INIT Adversarial Judge Protocol

Use this during `INIT-5 JUDGE`, `INIT-6 REPAIR_LOOP`, and the final completion review.

## Purpose

Judge the deliverable against the **original prompt, requirement ledger, acceptance criteria, and actual evidence**. The goal is to find real acceptance risks before the user does, not to reward effort or manufacture criticism.

When the same model performs this review, call it a **self-review**. Never present it as an independent audit or independent reviewer.

## Review dimensions

Inspect each dimension when relevant:

1. **Requirement coverage** — every material requested behavior/output is present and traceable.
2. **Functionality** — the actual output behaves correctly, including integration behavior.
3. **Robustness** — edge cases, invalid states, failures, recovery, and regression exposure.
4. **Usability** — accessibility, clarity, interaction quality, and visual quality where applicable.
5. **Performance** — measurable latency, memory/resource use, size, or throughput where relevant and actually testable.
6. **Security/privacy** — permission boundaries, data handling, secret exposure, unsafe assumptions, and permitted security checks.
7. **Reproducibility** — setup/build/run instructions, maintainability, determinism where expected, and packaging completeness.
8. **Honesty of testing claims** — claims match real commands, observations, limitations, and evidence.

## Judge posture

Be skeptical and demanding:

- Compare to what the user asked for, not what was easiest to build.
- Treat unsupported success claims as defects in evidence quality.
- Inspect the actual final/candidate artifact, not only source snippets or intentions.
- Prefer a concrete reproduction or inspection path over vague criticism.
- Do not invent a defect to sound harsh.
- If evidence is incomplete, record a **suspicion** or `UNVERIFIED`, not a fabricated failure.
- A polished surface does not compensate for broken core behavior.
- A high test count does not compensate for missing requirement coverage.

## Severity

Use these labels consistently:

- **critical** — unsafe, destructive, corrupting, fundamentally unusable, or core deliverable cannot perform its primary purpose.
- **high** — material requested behavior is broken/missing; serious integration, correctness, permission, or packaging failure.
- **medium** — meaningful quality/edge-case/usability defect that affects acceptance but does not destroy the primary path.
- **low** — minor polish, maintainability, wording, or non-blocking inconsistency.

Do not inflate severity to make the review look stricter.

## Finding schema

Every finding uses this shape:

```text
ID: JDG-###
severity: critical | high | medium | low
requirement: REQ-### or documented risk
title: concise defect/risk name
evidence_or_suspicion: OBSERVED evidence | SUSPICION with reason
reproduction: exact command, path, user flow, inspection, or reason reproduction is unavailable
impact: why this matters to the original prompt
proposed_fix: smallest credible repair
status: OPEN | FIXED | ACCEPTED_LIMITATION | BLOCKED | NOT_REPRODUCED
retest_evidence: populated after repair
re_review_result: populated after re-review
```

Evidence can be an exit code, test output, file path/content, screenshot/render inspection, source verification, deterministic calculation, or other observable artifact. A bare feeling is not evidence.

## First-pass judge procedure

1. Re-read the original prompt and requirement ledger.
2. Inspect the candidate final deliverable itself.
3. Review actual test/check evidence and all skipped/blocked areas.
4. Walk every applicable review dimension.
5. Record findings using `JDG-###`; keep suspicions visibly distinct from observed defects.
6. Produce a criterion-level verdict matrix.

## Criterion verdicts

Use only:

- `PASS` — acceptance criterion is satisfied with adequate observed evidence.
- `PASS WITH LIMITATIONS` — materially satisfied, but a disclosed limitation remains.
- `FAIL` — observed evidence shows the criterion is not satisfied.
- `UNVERIFIED` — available evidence cannot establish the criterion either way.

Do not average these into a cosmetic numerical score unless the user explicitly needs a metric for a non-political task. The criterion-level evidence matters more than a score.

## Repair gate

After the first judge pass:

1. Fix all actionable **critical** findings first.
2. Fix actionable **high** findings next.
3. Fix **medium** findings that affect acceptance or important quality goals.
4. Address low findings only when they materially improve the requested product and do not distract from higher priorities.
5. For every fix, run the exact targeted retest plus plausible regression checks.
6. Preserve the original finding and attach disposition/retest evidence; do not erase history.

## Re-review

A meaningful repair triggers a **re-review**. Re-read the original requirement and inspect the repaired artifact/evidence rather than merely trusting the fix description.

For every previous finding:

- confirm whether it is actually fixed;
- check whether the fix created a new regression;
- update `status`, `retest_evidence`, and `re_review_result`;
- open a new `JDG-###` if a distinct new defect is discovered.

If no material changes occurred after the judge pass, do not perform fake repeated judge passes just to increase repetition.

## Harshness calibration

“Harsh” means a high acceptance standard, not abusive language, pessimism, or imaginary defects. A strong judge report should be able to say either:

- “No material defect found in this area; evidence is sufficient,” or
- “This does not pass, and here is the exact evidence and repair path.”

Both are rigorous outcomes.

## Final judge summary

End with:

```text
Original-prompt fidelity:
Open critical findings:
Open high findings:
Open acceptance-affecting medium findings:
Criterion verdicts: PASS / PASS WITH LIMITATIONS / FAIL / UNVERIFIED
Testing-claim honesty check:
Packaging/handoff check:
Final limitations:
```
