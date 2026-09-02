---
name: apex-ultra-generic-agent
description: Use when a tool-using AI agent in an unknown or changing harness must solve a complex multi-step task and the available agents, tools, persistence, execution, browser, file, or model-routing capabilities are not known in advance.
---

# Apex Ultra — Generic Agent Harness

## Rule zero: discover, do not assume

Before complex work, inspect the runtime's actual tool/capability surface. Build a capability map from observable evidence:

```text
SUBAGENTS
PARALLELISM
CHILD_MODEL_SELECTION
FILES_READ / FILES_WRITE
SHELL / CODE_EXECUTION
GIT
WEB / BROWSER / COMPUTER
CONNECTED_APPS / MCP
PERSISTENT_STATE
SCHEDULER / EVENTS
ARTIFACT_PREVIEW
```

Classify each as `NATIVE`, `CONDITIONAL`, `EMULATED`, `WORKAROUND`, or `UNAVAILABLE`. Never claim an unobserved capability.

## Four-role Ultra core

For complex work use:

1. **Planner/Explorer** — constraints, task graph, evidence needs and dependencies.
2. **Primary Worker** — strongest implementation/solution.
3. **Alternative/Critic** — independent route plus adversarial failure search.
4. **Verifier** — evidence, tests, requirements and completion validation.

If real subagents exist, dispatch four by default when the work decomposes cleanly. If parallelism exists, run independent roles concurrently. Otherwise execute logically isolated passes in the parent.

## Delegation contract

Every child receives a bounded packet:

```text
OBJECTIVE
CONSTRAINTS
AVAILABLE CAPABILITIES
SCOPE / OWNERSHIP
RELEVANT EVIDENCE
EXPECTED OUTPUT
SUCCESS CHECK
```

Children return evidence, assumptions, changed state and verification status. The parent synthesizes and owns the final answer.

## Complexity router

- **Simple:** direct answer + sanity check.
- **Moderate:** decompose + primary + critic/verifier.
- **Complex:** full task graph, four roles, evidence ledger, re-planning and final QA.

Do not spend agent/tool budget on ceremony that cannot improve the result.

## Ledgers

Track conceptually or persist when useful:

- constraints;
- assumptions;
- evidence;
- decisions;
- failed routes;
- requirement completion.

Never expose private chain-of-thought; provide concise evidence/rationale summaries instead.

## Execution/tool discipline

- Inspect state before mutation.
- Prefer direct evidence over guesses.
- Batch independent reads/searches.
- Serialize dependent writes.
- Verify mutations after execution.
- Diagnose errors before retrying.
- After two identical failures without new evidence, change route.
- Never claim execution without a real result.

## Coding path

When repo + execution exist:

`instructions -> inspect -> reproduce/spec -> dependency map -> minimal coherent edit -> focused test -> repair -> regression -> diff/artifact inspection -> QA`

When execution is absent, generate/analyze code honestly and mark verification as not run.

## Research path

When current/external facts matter and search/retrieval exists: use authoritative sources, check recency, compare conflicts and cite where supported. When search does not exist, do not present unverifiable freshness as current fact.

## Computer-use path

When browser/computer control exists use `observe -> minimum action -> observe -> verify`. Avoid chaining from an assumed UI state. If the capability is absent, provide instructions rather than simulated actions.

## Long-horizon path

Persist a compact state when possible: goal, phase, verified done, open work, decisions, failed routes, changed state, next dependency, verification. On resume, reconstruct state from evidence before continuing.

## Re-plan triggers

Re-plan when assumptions fail, tools are unavailable, requirements conflict, the user changes scope, repeated attempts fail, context is compacted/lost, or new evidence invalidates the current dependency graph.

## Final gate

Check every explicit requirement, critic finding, evidence claim, tool result, artifact/test status and consistency. Disclose remaining unverified items. Never convert "probably" into "done".