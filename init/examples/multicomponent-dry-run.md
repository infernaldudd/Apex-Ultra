# Multi-Component Task Dry Run — Synthetic Demonstration

This is a **synthetic demonstration**, not evidence from a real user product.

## Scope

Task: package a small desktop app with a UI, local settings persistence, and a distributable archive.

## Requirements

- `REQ-001`: UI launches and primary action works.
- `REQ-002`: local setting survives restart.
- `REQ-003`: distribution archive contains runnable files and reports.

## Target

Applicable factors:

1. interacting components / multiple file types (+5)
2. state/persistence (+5)
3. user-facing UI (+5)

`F = 3`

`Target T: 25`

The check plan allocates coverage across launch, primary flow, error behavior, persistence, restart, UI state, packaging, archive integrity, and regressions rather than repeating the easiest checks.

## Representative baseline checks

- `CHK-001` (`REQ-001`) — app launch — PASS.
- `CHK-002` (`REQ-001`) — primary action — **FAIL** when settings file is absent.
- `CHK-003` (`REQ-002`) — setting persists after restart — PASS.
- `CHK-004` (`REQ-003`) — archive includes required executable — PASS.
- Additional distinct checks cover invalid settings, recovery, UI empty state, restart consistency, archive integrity, file naming, and final-artifact reopen.

## Improvement cycle

### CYC-001

- Trigger: `CHK-002` FAIL.
- HYPOTHESIS: primary action reads configuration before first-run defaults are initialized.
- Change: initialize defaults before the primary action can execute.
- RETEST: `CHK-002` PASS.
- Regression: launch, persistence, restart, and invalid-settings recovery checks remain PASS.

## Judge

### JDG-001 — high

- Requirement: `REQ-003`
- Evidence: first package contains the executable but omits the required `HANDOFF.md`.
- Reproduction: list archive members.
- Proposed fix: rebuild package using the standard INIT layout and verify members after close/reopen.
- Status: FIXED.

## Repair and repackage

Package rebuilt with the required handoff. Archive reopened and integrity checked.

## Re-review

`JDG-001` is FIXED. `REQ-003` now passes archive-member and nonempty-file checks. No new packaging regression observed.

## Final gate

Final gate checks the actual rebuilt package: launch artifact, persisted setting behavior, required archive members, archive integrity, and reports.

## HANDOFF

State: COMPLETED for this demonstration. Single immediate next step in a real project would be to deliver the verified archive or upload it only if an authorized destination/tool exists.
