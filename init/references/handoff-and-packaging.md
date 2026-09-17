# INIT Handoff and Packaging Protocol

Use this during long-running work, at major milestones, after judge passes, and during `INIT-8 HANDOFF_PACKAGE`.

## Context truth

The model cannot reliably know the exact context capacity remaining or predict the exact context-exhaustion point. Do not claim an exact token threshold or wait for one.

Instead, maintain **progressive checkpoints**. Update handoff state:

- after initial requirements/acceptance criteria are stable;
- after substantial file or architecture changes;
- after a major regression pass;
- after each judge/re-review milestone;
- before producing a large artifact or output likely to consume significant context;
- before ending a session with material unfinished work.

A checkpoint is useful only if a fresh worker can resume from it without reconstructing hidden reasoning.

## Required handoff contents

`HANDOFF.md` should contain:

1. Original user request in concise faithful form.
2. Scope, explicit preferences, constraints, and assumptions.
3. Acceptance criteria and requirement IDs.
4. Current state: `COMPLETED`, `IN_PROGRESS`, or `BLOCKED` by workstream.
5. Latest actual deliverable version and exact known paths (relative and absolute where available).
6. Project structure and key dependencies/environment details.
7. Setup/build/test/run commands needed to resume.
8. Change log with major decisions and concise reasons.
9. Verification target, check IDs, actual results, failed evidence, retests, and unresolved gaps.
10. Judge findings, fixes, re-review outcomes, and remaining findings.
11. Access/tool/permission limitations.
12. Ordered next actions, including the **single immediate next step**.
13. Packaging state: what is already in the archive and what remains.

Do not include private chain-of-thought. Record conclusions and reasons at a level needed for continuation.

## Sensitive-data boundary

Before writing reports or an archive, exclude or redact unnecessary:

- secret values;
- API tokens/session tokens;
- credentials/passwords;
- `.env` contents;
- private key material;
- cookies or authentication exports;
- personal data not needed to resume the task.

A filename alone can also be sensitive. Review archive members, not only file contents.

## Standard file-based package

When the task creates actual files and tools allow packaging, produce:

```text
INIT_FINAL.zip
├── deliverables/
├── reports/INIT_REPORT.md
├── reports/TEST_RESULTS.md
├── reports/JUDGE_REPORT.md
└── HANDOFF.md
```

`deliverables/` preserves the final files and any necessary relative directory structure. Exclude caches, temporary build junk, dependency folders, duplicate intermediates, and unrelated source material unless required for the deliverable.

## Source-to-archive procedure

1. Identify the **source** paths for final deliverables and reports.
2. Confirm each required source exists and is nonempty where nonempty content is expected.
3. Copy/package to the required archive **destination** paths.
4. Close the writer.
5. **Reopen** the archive from disk.
6. Run a ZIP CRC/integrity check equivalent to Python `ZipFile.testzip()`; success requires `testzip()` to return `None`.
7. List archive members and compare them to the required layout.
8. Read/check required members and ensure they are nonempty.
9. Scan member names for obvious secret/credential/private key files and remove them if not explicitly required and authorized.
10. Compare important archived file sizes/hashes to their intended source when practical.
11. Only after these checks may the archive be called verified.

Example integrity check:

```python
from pathlib import Path
from zipfile import ZipFile

archive = Path("INIT_FINAL.zip")
with ZipFile(archive, "r") as zf:
    assert zf.testzip() is None
    names = set(zf.namelist())
    required = {
        "reports/INIT_REPORT.md",
        "reports/TEST_RESULTS.md",
        "reports/JUDGE_REPORT.md",
        "HANDOFF.md",
    }
    assert required <= names
    for name in required:
        assert len(zf.read(name)) > 0
```

## Upload boundary

Creating a local ZIP is not an **external upload**. Uploading, publishing, replacing, sharing, or sending a file requires:

- a named/understood destination;
- an **available tool** or connector that can perform the action;
- appropriate user **authorization** and account access;
- respect for overwrite/replacement semantics and any permission prompts.

If any requirement is missing, leave the archive local and report upload as `BLOCKED` or `NOT_APPLICABLE`. Never claim an upload succeeded based only on a local file existing.

## Handoff verification

Before final delivery, perform a handoff-read test:

- Can a fresh worker identify the original request?
- Can they locate the final files?
- Can they reproduce the build/test commands?
- Can they see which tests actually failed and which later passed?
- Can they see open judge findings and limitations?
- Is the single immediate next step unambiguous?
- Are secrets absent?

If any answer is no, repair `HANDOFF.md` before declaring the package complete.
