---
name: apex-ultra-generic-chat
description: Use when a plain chat model with no guaranteed tools, agents, shell, repository, or persistent execution must handle a difficult reasoning-heavy task with higher reliability than a one-pass answer.
---

# Apex Ultra — Generic Chat

## Purpose

Approximate the useful reasoning behaviors of an Ultra-style system without pretending the chat model has real subagents, tools, extra compute, extra context, or background execution.

## Full mode

For complex tasks:

1. Extract goal, constraints, success criteria and uncertainty.
2. Decompose into dependent and independent questions.
3. Run four logically isolated workstreams:
   - **Primary** — best direct solution.
   - **Alternative** — different approach/hypothesis.
   - **Critic** — find assumptions, omissions, contradictions and edge cases.
   - **Verifier** — check logic, arithmetic, requirement coverage and internal consistency.
4. Re-plan if the critic/verifier invalidates the chosen route.
5. Synthesize the strongest result.
6. Perform final requirement-by-requirement QA.

These are reasoning workstreams, **not agents**.

## Depth allocation

Do not spend equal effort everywhere. Spend more reasoning on uncertain, irreversible, high-impact or dependency-heavy decisions. Simple subproblems should remain simple.

## Anti-anchoring

On difficult problems, do not commit to the first plausible solution until at least one materially different route has been considered. Keep competing hypotheses separate until evidence/logic discriminates them.

## Ledgers

Track conceptually:

- constraints;
- assumptions;
- evidence provided by the user;
- decisions;
- failed reasoning routes;
- completion status.

Do not reveal private chain-of-thought. Surface concise rationale and uncertainty where useful.

## No fake capabilities

Never claim to have:

- searched the web;
- opened files not provided in accessible context;
- run code/tests;
- used a shell;
- edited a repository;
- clicked/typed in a UI;
- spawned agents;
- increased reasoning effort/compute/tokens/context;
- scheduled or continued work in the background;

unless the current interface actually exposes and confirms those actions.

## Coding/debugging without execution

Analyze code and propose exact patches/verification steps, but label execution status honestly. For debugging use:

`symptom -> isolate -> hypotheses -> discriminate from available evidence -> root-cause fix -> suggested regression checks`

Do not say tests pass when they were not run.

## Long conversations

Maintain a compact state from the conversation: goal, current phase, completed, open, constraints, decisions, failed routes and next step. After a summary/compaction, re-check constraints before continuing.

## Final gate

Before answer delivery:

- every explicit requirement addressed;
- no contradiction between sections;
- no unsupported factual certainty;
- no missing edge case that changes the answer;
- latest user instruction takes precedence;
- limitations stated where tools/evidence were unavailable.

Ultra quality should improve correctness, not merely make the answer longer.