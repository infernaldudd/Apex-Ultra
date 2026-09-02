---
name: apex-ultra-claude-code
description: Use when Claude Code is handling complex implementation, debugging, refactoring, code review, repository research, or long-running engineering work that benefits from agent teams and strict verification.
---

# Apex Ultra — Claude Code

## Use the harness, not just the model

Exploit repository access, shell, edits, tests, skills, MCP/connectors, hooks and native agent-team/subagent features **only when the current Claude Code runtime exposes them**.

## Four-agent default

For complex parallelizable work, prefer four roles:

1. **Architect/Explorer** — project instructions, architecture, dependency/change map.
2. **Implementer** — primary implementation or bounded work package.
3. **Independent Reviewer** — adversarial read-only review and alternative design.
4. **Verifier** — tests, build/lint/type checks, requirement coverage and regression evidence.

Use real agent teams/subagents when available. Give children bounded context rather than dumping the entire session. If teams are unavailable, perform the roles as separate passes and state that they were not real agents.

## Agent packet

Every delegated task should contain:

```text
OBJECTIVE
RELEVANT CONSTRAINTS
ALLOWED SCOPE
RELEVANT FILES/AREAS
KNOWN EVIDENCE
EXPECTED DELIVERABLE
DO-NOT-DO
VERIFICATION
```

Agents should return evidence and changed-file/test status, not vague confidence.

## Repository-first workflow

1. Read `CLAUDE.md`, relevant skills and project instructions.
2. Inspect status, structure and existing conventions.
3. Identify tests/build/lint/type commands from the project.
4. Map dependencies and file ownership.
5. Separate independent work packages.
6. Implement the smallest coherent change.
7. Run focused verification.
8. Diagnose failures before further edits.
9. Run appropriate regression checks.
10. Inspect the final diff and artifacts.

Preserve unrelated user changes. Do not perform broad cleanup merely because it is available.

## Parallel work

Parallelize independent exploration, disjoint file ownership, research, read-only review and independent verification. Serialize changes that touch the same files/state or depend on prior outputs.

The coordinator owns integration and must inspect child work before accepting it.

## Debugging

`reproduce -> exact evidence -> isolate -> competing hypotheses -> discriminating experiment -> root fix -> regression -> diff review`

Do not repeatedly patch symptoms. After two failed attempts using the same theory without new evidence, explicitly change hypothesis/route.

## Skills/MCP/hooks

- Load relevant skills rather than copying giant instruction blocks into the task context.
- Use MCP/connectors only for data/actions actually authorized and available.
- Treat hooks as observable automation, not proof of correctness.
- If a hook or tool fails, inspect its result before retrying.
- Keep high-value persistent project conventions in the runtime's supported instruction mechanism rather than long chat history.

## Context/compaction

For long work, keep a compact state containing goal, milestone, verified work, open work, decisions, failed routes, test status and next dependency. After context compaction, reconstruct this state and re-read critical project instructions before modifying files.

## Verification before completion

Require actual evidence for any claimed command/test/build. Review final diff for accidental edits, placeholders/debug code, API/schema compatibility, missing tests, edge cases and documentation/config fallout.

## Future/native capability rule

If a future Claude Code version exposes better heterogeneous model routing, larger teams, persistent agents or richer shared state, use them only after capability detection. Until then, do not simulate runtime metadata or claim extra compute/context.