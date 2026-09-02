---
name: apex-ultra-claude-claw
description: Use when Claude is running inside a Claw-style or other third-party agent harness whose exact tools, persistence, subagent, shell, browser, or file capabilities must be discovered at runtime before complex work.
---

# Apex Ultra — Claude Claw / Third-Party Claude Harness

## Why this edition probes first

"Claw"-style Claude harnesses are not treated as one stable capability contract. Different builds can expose different shells, files, browsers, MCP servers, memory, schedulers and agent systems. Therefore **never infer a capability from the harness name**.

## Capability probe

Before complex execution, determine from the actual tool catalog/session whether the runtime provides:

```text
FILES_READ
FILES_WRITE
SHELL
CODE_EXECUTION
GIT
WEB_SEARCH
BROWSER_CONTROL
COMPUTER_CONTROL
MCP_OR_CONNECTORS
SUBAGENTS
PARALLEL_SUBAGENTS
CHILD_MODEL_SELECTION
PERSISTENT_STATE
SCHEDULER_OR_EVENTS
ARTIFACT_PREVIEW
```

Do not probe by performing dangerous or irreversible actions. Prefer metadata/tool discovery and harmless reads.

## Ultra orchestration

For complex tasks use four roles:

1. **Planner/Explorer**
2. **Primary Worker**
3. **Critic/Alternative**
4. **Verifier**

If `SUBAGENTS` is confirmed, instantiate bounded specialists. If `PARALLEL_SUBAGENTS` is confirmed, dispatch independent work concurrently. Otherwise execute isolated reasoning passes in the parent. Never label emulated roles as real agents.

## Delegation packet

Give each real child only the context it needs:

```text
OBJECTIVE
CONSTRAINTS
AVAILABLE TOOLS
SCOPE
KNOWN EVIDENCE
EXPECTED OUTPUT
VERIFICATION
```

If child permissions differ from the parent, verify what the child can actually access before assigning work.

## Tool policy

- Use shell/Git only when confirmed.
- Inspect before mutating files.
- Batch independent reads; serialize dependent writes.
- After external/app actions, verify resulting state.
- After tool failure, diagnose instead of blind retry.
- Never assume MCP/connectors are authenticated merely because they are configured.
- Never claim persistent/background execution without an actual persistence/scheduler primitive.

## Coding path

When files + shell/code execution exist:

`instructions -> repo inspect -> reproduce/spec -> dependency map -> minimal edit -> focused test -> repair -> regression -> diff -> QA`

When they do not exist, downgrade honestly to analysis/code generation and provide verification steps rather than invented execution evidence.

## Long-horizon path

If persistent files/state exist, maintain a compact checkpoint. If a scheduler/event system exists, use it only when the task genuinely needs future execution and the user requested it. If neither exists, do not promise work after the current run.

## Recovery

Detect loops, repeated identical errors, context loss and permission failures. Preserve known-good state, record the failed route, choose a distinct alternative and verify it before proceeding.

## Future compatibility

This adapter intentionally becomes more powerful automatically as the harness exposes verifiable capabilities. New capabilities move from `UNAVAILABLE/EMULATED` to `NATIVE` only after current-session confirmation.