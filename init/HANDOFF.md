# INIT Handoff

## Original request

Create a custom `init` skill that pushes a capable model toward maximum product quality through substantially more deliberate iteration: choose 10–45 meaningful checks, repeatedly test/study/reason/draft/predict/fix/retest, perform a harsh original-prompt-aware judge pass, repair and judge again, preserve progress before context becomes a problem, and package file-based outputs with judge and test evidence.

## Current state

**COMPLETED WITH ONE DISCLOSED VALIDATION LIMITATION.**

Final skill source:

`/mnt/data/INIT_WORKSPACE/init/`

Final distribution archive:

`/mnt/data/INIT_FINAL.zip`

## Key structure

- `init/SKILL.md` — compact activation + phase state machine
- `init/references/verification-protocol.md` — 10–45 target, ledgers, anti-padding
- `init/references/adversarial-judge.md` — severity, findings, re-review
- `init/references/handoff-and-packaging.md` — checkpoints, ZIP verification, upload boundary
- `init/templates/` — four report/handoff templates
- `init/examples/` — small + multi-component synthetic dry-runs
- `init/tests/` — standard-library `unittest` contract suite

## Resume commands

```bash
cd /mnt/data/INIT_WORKSPACE
python -m unittest discover -s init/tests -v
wc -w init/SKILL.md
```

## Verification state

- Derived INIT target for this build: 20
- Final automated tests: 29
- Final regression: 29 PASS / 0 FAIL, exit code 0
- Judge finding `JDG-001`: fixed (skill compacted to 456 shell words)
- Judge finding `JDG-002`: accepted limitation — no fresh-agent/subagent pressure harness in this environment

## Important decisions

- Repetition is evidence-driven, not a forced 10–45 full-cycle loop; duplicate unchanged reruns do not count as new checks.
- Same-model judge is called self-review, never independent audit.
- The skill does not claim it can alter GPT-5.6 Sol's hidden internal thinking budget; it increases deliberate workflow effort through explicit phase gates.
- Exact context exhaustion is not predictable, so checkpoints are progressive instead of waiting for an exact threshold.
- External upload is separate from local ZIP creation and remains tool/authorization-gated.

## Single immediate next action

Install/copy the `init/` directory into the target agent runtime's skills directory, then run fresh-agent pressure scenarios there if the runtime supports subagents.

## Packaging status

`INIT_FINAL.zip` contains the complete skill under `deliverables/init/`, build reports under `reports/`, and this handoff. Final ZIP integrity is verified after archive creation and reported in the delivery response.
