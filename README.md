# Apex Ultra

**Apex Ultra** is a suite of separate, harness-optimized AI skills for getting more reliable reasoning, planning, tool use, verification, long-horizon work, and agent orchestration out of the capabilities a runtime actually exposes.

Apex Ultra does **not** claim to increase a model's hidden compute, context limit, token budget, or native tool access. It improves the workflow around those limits. When a harness supports real subagents, parallel execution, shell access, repositories, computer use, memory, or connected apps, its dedicated skill uses them. When it does not, the skill uses an explicit fallback instead of pretending the capability exists.

## Editions

| Edition | Main target | Multi-agent policy |
|---|---|---|
| `chatgpt/` | Normal ChatGPT Chat | `CUSTOM_ULTRA`: four logically isolated workstreams; real agents only if explicitly exposed in the chat |
| `codex/` | OpenAI Codex | Native subagents/parallel work when exposed; repo, shell, tests and diffs are first-class |
| `claude/` | Claude Chat | Reasoning/workstream orchestration constrained to Claude Chat's visible tools |
| `claude-code/` | Claude Code | Native coding tools and agent teams/subagents when available; skills/MCP-aware workflow |
| `claude-cowork/` | Claude Cowork | Multi-file, multi-app, document and knowledge-work orchestration with human review gates |
| `claude-claw/` | Claude/Claw-style third-party harnesses | Capability-probed adapter; no assumptions about unofficial runtime features |
| `opencode/` | OpenCode | Native primary/subagent architecture, skills, shell/edit/search tools and child sessions |
| `generic-agent/` | Any tool-using agent harness | Capability detection + native-or-fallback orchestration |
| `generic-chat/` | Plain chat models | Reasoning-only Ultra emulation with no fake tools or agents |

## Core idea

For difficult tasks, Apex Ultra tries to obtain the useful behaviors of stronger inference-time systems:

1. Decompose the task and preserve constraints.
2. Use four independent workstreams by default on complex work: **Primary**, **Alternative**, **Critic**, **Verifier**.
3. Run truly independent work in parallel when the runtime supports it; otherwise keep the workstreams logically isolated and execute them sequentially.
4. Explore alternatives before committing to a fragile approach.
5. Use tools for evidence rather than guessing when verification is available.
6. Detect contradictions, failure modes and missing requirements.
7. Re-plan when evidence invalidates the current approach.
8. Synthesize the strongest result rather than concatenating agent outputs.
9. Perform a final requirement-by-requirement quality gate before claiming completion.

## Capability truth rule

Every edition follows this invariant:

```text
if capability_is_exposed_and_verified:
    use it natively
elif a safe workflow fallback exists:
    emulate the useful behavior
else:
    mark it unavailable and continue without pretending
```

Examples:

- No native subagents -> use independent reasoning workstreams, not the phrase "I ran four agents".
- No shell -> never claim commands or tests were executed.
- No persistent memory -> create an explicit checkpoint/state summary if files or conversation context permit.
- No extra reasoning/compute control -> allocate the available reasoning carefully; never claim a larger hidden budget.
- No background execution -> do the work in the current run or say the runtime cannot persist it.

## Installation

Copy the folder for the harness you use and follow that folder's `SKILL.md`. The editions are deliberately separate so a ChatGPT skill does not inherit Codex assumptions, and a coding-agent skill does not weaken itself to fit a plain chat runtime.

For Agent-Skills-compatible runtimes, prefer the runtime's current documented skill directory. OpenCode currently recognizes project/global skill directories including `.opencode/skills`, `.claude/skills`, and `.agents/skills`.

## Repository docs

- `docs/DESIGN.md` — architecture and invariants.
- `docs/CAPABILITY-MATRIX.md` — what the skill can improve, emulate, or only prepare for.
- `docs/IMPLEMENTATION-PLAN.md` — build and verification plan.
- `tests/PRESSURE-TESTS.md` — adversarial scenarios for validating future revisions.

## Status vocabulary

- **NATIVE** — the harness exposes the capability.
- **EMULATED** — workflow approximates the useful reasoning behavior without claiming the underlying feature.
- **WORKAROUND** — requires explicit files/tools/checkpoints or another visible mechanism.
- **CONDITIONAL** — only active when the current session exposes the required capability.
- **FUTURE** — cannot be implemented honestly by instructions alone today; a fallback is documented.

## License

Use, adapt, fork, and improve the skills for your own agent workflows. Keep the capability-truth rule intact: quality improvements are useful only when the system stays honest about what it actually executed.