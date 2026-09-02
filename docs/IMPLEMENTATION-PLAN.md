# Apex Ultra Implementation Plan

> **For agentic workers:** When extending this repository, use a plan-driven workflow with review checkpoints. For code-bearing future modules, use test-driven development and verification before completion.

**Goal:** Build a suite of separate harness-specific Apex Ultra skills that improve complex reasoning/orchestration while never claiming capabilities a runtime does not expose.

**Architecture:** Each harness gets its own standalone `SKILL.md`; ChatGPT additionally gets `CUSTOM_ULTRA.md`. Shared design principles are documented centrally, but runtime assumptions stay inside each edition.

**Tech Stack:** Markdown Agent Skills / harness instruction files; no runtime dependency required.

**Spec:** `docs/DESIGN.md`

## Global Constraints

- Separate editions, not one universal skill.
- ChatGPT `CUSTOM_ULTRA` must target normal ChatGPT Chat, not ChatGPT Work or Codex.
- Four real agents by default only on complex parallelizable work where real subagents are exposed.
- Otherwise use four logically isolated workstreams and never call them real agents.
- Never claim extra hidden compute, tokens, context, tools, execution, persistence, or permissions.
- Prefer inspect -> refine -> verify -> deliver over one-shot generation.
- Preserve user constraints and reduce unnecessary user round-trips without guessing critical missing requirements.

---

### Task 1: Core architecture

**Files:**
- `README.md`
- `docs/DESIGN.md`
- `docs/CAPABILITY-MATRIX.md`

- [x] Define capability truth statuses: NATIVE, EMULATED, WORKAROUND, CONDITIONAL, FUTURE.
- [x] Define four-workstream architecture.
- [x] Define evidence, context, tool, coding, debugging, recovery and final-QA rules.
- [x] Map all 42 requested Ultra properties to honest instruction-level implementations.

### Task 2: ChatGPT CUSTOM_ULTRA

**Files:**
- `chatgpt/SKILL.md`
- `chatgpt/CUSTOM_ULTRA.md`

- [x] Restrict scope to normal ChatGPT Chat.
- [x] Add capability detection and no-fake-agent rule.
- [x] Add Primary / Alternative / Critic / Verifier workstreams.
- [x] Add context, research, tool, coding, debugging, computer-use, files/artifacts and long-horizon logic.
- [x] Add re-plan triggers and final Ultra quality gate.
- [x] Add future capability adapters without claiming availability.

### Task 3: Coding harness editions

**Files:**
- `codex/SKILL.md`
- `claude-code/SKILL.md`
- `opencode/SKILL.md`

- [x] Use native subagents/agent teams when current runtime exposes them.
- [x] Add bounded child-context packets.
- [x] Add repository inspection, dependency mapping, focused tests, regression and final diff review.
- [x] Add parallelization rules that avoid same-file/shared-state races.
- [x] Add stuck recovery and context-compaction resume logic.

### Task 4: Conversational and knowledge-work editions

**Files:**
- `claude/SKILL.md`
- `claude-cowork/SKILL.md`
- `claude-claw/SKILL.md`
- `generic-agent/SKILL.md`
- `generic-chat/SKILL.md`

- [x] Keep Claude Chat reasoning-only unless tools are exposed.
- [x] Optimize Cowork for multi-file/multi-app deliverables and review gates.
- [x] Make Claw-style harness support capability-probed because third-party runtimes vary.
- [x] Provide a generic tool-using agent adapter.
- [x] Provide a generic chat fallback with no fake tools/agents.

### Task 5: Pressure-test suite

**Files:**
- `tests/PRESSURE-TESTS.md`

- [x] Define capability-hallucination tests.
- [x] Define false-completion/execution tests.
- [x] Define anchoring/alternative-solution tests.
- [x] Define agent-conflict and orchestration tests.
- [x] Define stuck-loop and context-loss tests.
- [x] Define artifact-inspection and long-horizon tests.
- [ ] Run tests with independent subagents in each target harness. This repository creation session did not expose an independent subagent test runner, so this remains an explicit external verification task rather than a fabricated result.

### Task 6: Repository verification

- [ ] Re-fetch committed files from GitHub.
- [ ] Confirm all expected edition paths exist.
- [ ] Search for placeholders/TODOs that could weaken behavior.
- [ ] Verify ChatGPT files do not assume Work/Codex-only execution.
- [ ] Verify capability-truth language exists in every edition.
- [ ] Record final repository state/commit evidence before declaring completion.
