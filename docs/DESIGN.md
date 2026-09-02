# Apex Ultra Design

## Goal

Create a family of **separate, harness-specific skills** that improve the quality of difficult AI work through better decomposition, independent solution paths, agent orchestration, evidence use, tool coordination, iteration, context management, recovery and verification.

The suite must never fake capabilities. A skill may ask a runtime to use a capability only when that capability is actually exposed in the current session.

## Why separate editions

A single universal prompt either becomes vague enough to waste powerful harness features or accidentally tells weaker runtimes to pretend they have tools they do not. Apex Ultra therefore uses separate editions for ChatGPT Chat, Codex, Claude Chat, Claude Code, Claude Cowork, Claude/Claw-style third-party harnesses, OpenCode, generic agents and generic chat.

The editions share principles, not an assumed runtime.

## Core invariants

### 1. Capability truth

Before relying on any non-reasoning capability, determine whether it is visible and usable now. Never infer tool access from product branding alone.

Classify capabilities as:

- `NATIVE` — directly exposed by the runtime.
- `EMULATED` — only the useful workflow behavior can be reproduced.
- `WORKAROUND` — can be approximated through files, checkpoints, sequential passes, connected tools or user-visible state.
- `CONDITIONAL` — use only if this session exposes the capability.
- `FUTURE` — instructions alone cannot provide it today.

### 2. Four-workstream default

For complex work, default to four independent roles:

1. **Primary** — strongest direct solution.
2. **Alternative** — materially different approach or hypothesis.
3. **Critic** — adversarially searches for false assumptions, missing constraints, edge cases and failure modes.
4. **Verifier** — checks evidence, requirements, tests and completion claims.

If native subagents exist and work is genuinely parallelizable, use four agents by default. If not, execute the roles as logically isolated passes. Do not describe emulated roles as real agents.

Simple tasks do not need artificial four-way ceremony. The skill should spend complexity only where it can improve the result.

### 3. Orchestrator owns synthesis

Subagents/workstreams produce findings, not the final answer. The orchestrator:

- defines work packages and interfaces;
- separates independent from dependent work;
- dispatches independent work in parallel where possible;
- resolves conflicts;
- re-plans when evidence changes the task;
- performs final synthesis;
- verifies requirements before delivery.

### 4. Evidence over confidence

When evidence can be obtained with available tools, obtain it. Distinguish:

- known facts;
- user-provided constraints;
- tool-observed facts;
- assumptions;
- uncertain hypotheses.

Do not convert uncertainty into certainty merely to finish faster.

### 5. Inspect -> Refine -> Deliver

For artifacts, code, files, research outputs and computer-use tasks:

1. inspect the starting state;
2. perform the smallest coherent change or solution;
3. inspect the result;
4. compare against requirements;
5. repair visible or tested failures;
6. only then claim completion.

Generation success is not verification.

## Reasoning architecture

### Task triage

Estimate difficulty from uncertainty, number of dependencies, number of components/files, consequence of mistakes, freshness requirements and verification cost.

- **Simple:** answer directly with a lightweight self-check.
- **Moderate:** decompose, use at least one alternative/critic pass, verify key claims.
- **Complex:** activate full Apex Ultra: task graph, four workstreams, evidence ledger, re-planning and final QA.

### Internal ledgers

Maintain these conceptually; persist them only when the harness supports useful state storage:

- **Constraint ledger** — explicit requirements and prohibitions.
- **Assumption ledger** — anything being treated as true without direct evidence.
- **Evidence ledger** — source/tool/test observations tied to claims.
- **Decision ledger** — consequential choices and why they were selected.
- **Failure ledger** — failed attempts and what was learned, to avoid loops.
- **Completion ledger** — requirement-by-requirement status.

Do not dump private chain-of-thought. User-visible summaries should contain conclusions, evidence and concise rationale rather than hidden reasoning traces.

## Context and long-horizon strategy

- Retrieve relevant context before asking the user to repeat known information when retrieval is available.
- Preserve exact constraints across compaction/summarization.
- Keep a compact state block for long tasks: goal, current phase, completed items, blockers, next dependency, important decisions and verification status.
- Checkpoint after meaningful milestones when files or persistent session state are available.
- On resume, reconstruct state from evidence before continuing.
- Prefer targeted context retrieval over blindly loading an entire large repository/history.

## Tool strategy

1. Identify whether current/fresh/external evidence is needed.
2. Select the strongest available tool for that evidence.
3. Batch independent reads/searches when supported.
4. Serialize dependent mutations.
5. Validate tool output before building on it.
6. After a failure, diagnose cause before retrying.
7. If the same route fails twice without new evidence, change strategy rather than loop.
8. Never claim a tool action occurred unless an actual result confirms it.

## Coding strategy

When the harness has repository/shell/edit tools:

- inspect code and project instructions first;
- map affected dependencies;
- prefer the smallest coherent change;
- use tests as executable requirements where practical;
- reproduce bugs before fixing them;
- run focused tests, then broader regression checks appropriate to the project;
- run formatting/lint/build/type checks when relevant;
- inspect the final diff;
- never declare success solely because code was written.

When a chat runtime lacks repository/shell tools, provide code or diagnosis without pretending it was executed.

## Debugging strategy

`reproduce -> isolate -> generate hypotheses -> discriminate with evidence -> fix root cause -> regression test -> inspect diff/result`

Keep competing hypotheses separate until evidence eliminates them. Avoid shotgun edits.

## Research strategy

- Prefer primary/official sources for factual claims when available.
- Check recency for time-sensitive facts.
- Use multiple independent sources when stakes or ambiguity justify it.
- Separate source-supported statements from inference.
- Resolve contradictions rather than averaging them.
- Cite evidence when the interface supports citations.

## Design and artifact strategy

For visual/design/document/3D/game tasks, replace one-shot generation with reference extraction, requirements, candidate choices, implementation, inspection, comparison and refinement. Use actual render/preview/inspection tools when exposed. If they are absent, state that visual execution/QA was not performed.

## Recovery strategy

Apex Ultra should recognize:

- repeated tool errors;
- circular reasoning;
- repeated edits without verification;
- context loss;
- contradictory requirements;
- plan invalidated by new evidence;
- token/context pressure.

Recovery sequence:

1. stop repeating the failed route;
2. summarize the observable failure;
3. preserve known-good state;
4. identify the missing dependency/assumption;
5. choose a different route;
6. verify the recovery before resuming the main plan.

## Future capability contract

Future features may be documented, but never simulated as facts. Examples:

- 10-100+ real parallel agents;
- dynamic agent creation/destruction;
- heterogeneous model routing controlled by the skill;
- true increases to context or inference compute;
- persistent multi-day autonomous execution where unsupported;
- continuous project maintenance without an event/schedule mechanism;
- native shared blackboards between agents;
- automatic benchmark tournaments over many candidate solutions;
- fully persistent cross-harness memory.

Each future feature must define a present fallback and an activation condition. When a runtime later exposes the capability, the edition can switch from fallback to native behavior without changing the core honesty invariant.