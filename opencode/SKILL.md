---
name: apex-ultra-opencode
description: Use when OpenCode is handling complex coding, repository exploration, debugging, multi-file implementation, review, or long-horizon work that benefits from native subagents and rigorous verification.
---

# Apex Ultra — OpenCode

## Native architecture

Use OpenCode's actual primary/subagent model when available. Current OpenCode builds can expose primary agents, child-session subagents, skills, shell/edit/search tools and permission controls; confirm the current runtime rather than assuming a specific version.

## Four-agent default for complex work

For complex parallelizable tasks, the primary orchestrator should use four specialist roles by default:

1. **Explore/Planner** — read-only repository exploration, architecture and dependency map.
2. **Builder** — primary bounded implementation.
3. **Reviewer/Alternative** — independent approach plus adversarial code review; prefer read-only permissions.
4. **Verifier** — focused tests, regression/build/lint/type checks and requirement validation.

Use configured native subagents when they exist. If a role is not configured or subagents are disabled by permission, use an available equivalent or emulate it as an isolated parent-agent pass. Do not invent child sessions.

## Subagent hygiene

- Give children fresh/bounded context when the runtime permits.
- Do not send the entire parent history unless required.
- Specify file ownership for write-capable children.
- Prevent overlapping edits from independent builders.
- Use read-only permissions for exploration/review when possible.
- The primary agent owns conflict resolution and final synthesis.

Task packet:

```text
OBJECTIVE
CONSTRAINTS
SCOPE / FILE OWNERSHIP
RELEVANT CONTEXT
KNOWN EVIDENCE
EXPECTED OUTPUT
VERIFICATION
```

## Skills/instructions

- Read applicable `AGENTS.md` and project instructions before editing.
- Load relevant OpenCode/Agent Skills on demand instead of pasting giant instruction blocks.
- Respect skill and tool permissions.
- If a skill/tool is hidden or denied, do not pretend it was loaded.
- Keep stable project rules in project instruction files, not fragile chat recollection.

## Engineering loop

`inspect -> reproduce/specify -> dependency graph -> plan -> smallest coherent edit -> focused verification -> diagnose -> repair -> broader regression -> final diff/result review`

For bugs, reproduce first when feasible. For new behavior, use tests as executable requirements when practical.

## Parallelism

Good parallel work:

- explore separate subsystems;
- inspect independent large files;
- research external APIs/docs;
- implement disjoint work packages with explicit ownership;
- review while another independent verification stream runs.

Do not parallelize dependent mutations, same-file edits, migrations relying on earlier output, or Git ref operations that can race.

## Debugging/stuck recovery

1. capture exact error/tool output;
2. isolate failing boundary;
3. list plausible hypotheses;
4. run the cheapest discriminating experiment;
5. update the failure ledger;
6. fix root cause;
7. add/retain regression evidence;
8. verify broadly enough for the change.

If the same approach fails twice without new evidence, stop retrying it. Choose a different path, agent, tool, command, or hypothesis.

## Compaction/resume

OpenCode sessions may compact context. Maintain a durable compact state where appropriate:

```text
GOAL
ACTIVE TASK
VERIFIED DONE
OPEN
DECISIONS
FAILED ROUTES
FILES CHANGED
TEST STATUS
NEXT DEPENDENCY
```

After compaction or `continue`, reconstruct the latest unfinished task from repository/session evidence before acting. Never assume a pre-compaction command succeeded.

## Tool discipline

- Prefer native repo scripts/commands over guessed invocations.
- Read output and exit status.
- Batch independent reads/searches.
- Serialize writes with dependencies.
- Re-read/inspect changed state after mutations.
- Never claim a test/build/commit succeeded without returned evidence.
- Preserve unrelated user changes.

## Final quality gate

The primary agent must inspect the final diff/result and check:

- every requirement;
- accidental/unrelated changes;
- test/build/lint/type evidence;
- edge cases and error paths;
- API/config/schema compatibility;
- placeholders/debug leftovers;
- unresolved reviewer findings;
- unverified claims.

No completion claim until this gate passes or remaining limitations are explicitly stated.

## Capability truth

A skill can improve orchestration and discipline, but cannot create extra context, token budget, hidden compute, permissions, models or tools. Use runtime configuration when exposed; otherwise use the best honest fallback.