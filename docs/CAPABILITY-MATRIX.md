# Apex Ultra Capability Matrix

This document maps the requested "Ultra" properties to what an instruction skill can honestly improve.

## Requested 42-point Ultra mapping

| # | Requested property | Skill-level implementation |
|---:|---|---|
| 1 | Multi-Agent-System | Native agents when exposed; otherwise four role-separated reasoning workstreams. |
| 2 | 4 Agents parallel by default | Four native agents for complex parallelizable work when supported; otherwise four isolated passes. |
| 3 | Subagents | Use native subagents only when exposed. Fallback: specialist workstream roles. |
| 4 | Parallel Reasoning | Parallel native calls where possible; otherwise independent candidate paths executed serially. |
| 5 | Agent-Orchestration | Explicit orchestrator owns decomposition, dispatch, conflict resolution, synthesis and QA. |
| 6 | Task Delegation | Assign bounded work packages with inputs, outputs and success checks. |
| 7 | Workstream-Aufteilung | Separate independent work from dependent work and define a task graph. |
| 8 | Independent Problem Solving | Require alternative approaches to avoid anchoring on the first solution. |
| 9 | Mehrere Lösungsansätze gleichzeitig | Generate materially different candidates before selection on difficult tasks. |
| 10 | Cross-Checking | Critic and verifier compare claims, requirements, evidence and outputs. |
| 11 | Mehrfache Fehlerkontrolle | Use implementation check, verifier check and final requirement gate. |
| 12 | Alternative Lösungswege | Preserve at least one viable alternate path until evidence justifies commitment. |
| 13 | Final Synthesis | Orchestrator merges the strongest supported conclusions; never concatenate blindly. |
| 14 | Higher Compute Budget | `FUTURE/UNCONTROLLABLE` unless runtime exposes an effort control. Skill can only allocate available effort better. |
| 15 | Higher Token Budget | `FUTURE/UNCONTROLLABLE` unless runtime exposes limits. Use context budgeting/compression instead. |
| 16 | Mehr Inference-Compute | `FUTURE/UNCONTROLLABLE` from instructions alone. Emulate with structured iterative passes. |
| 17 | Deep Reasoning | Use multi-stage problem formulation, alternatives, critique, verification and re-planning. |
| 18 | Long-Horizon Reasoning | Maintain task state, dependency graph, checkpoints and resume protocol where persistence exists. |
| 19 | Mehrstufige Planung | Plan phases and dependencies before consequential multi-step execution. |
| 20 | Bessere Tool-Koordination | Select tools by evidence need, batch independent reads and serialize dependent writes. |
| 21 | Bessere Iteration | Inspect result, compare to requirements, repair and reverify. |
| 22 | Selbstkorrektur | Detect -> diagnose -> repair -> verify instead of silently changing answers. |
| 23 | Ansatz überarbeiten | Trigger re-planning when assumptions fail or evidence conflicts. |
| 24 | Mehr Exploration vor der Antwort | Use candidate/hypothesis generation proportionate to task difficulty. |
| 25 | Weniger frühes Festlegen | Keep alternative hypotheses alive until discriminating evidence is available. |
| 26 | Bessere komplexe Aufgabenzerlegung | Build work packages with clear boundaries, dependencies and success conditions. |
| 27 | Bessere Abhängigkeitserkennung | Map prerequisite relationships before parallel dispatch or mutation. |
| 28 | Mehr parallele Recherche | Parallelize independent searches when tools/agents support it; otherwise batch or sequence independent queries. |
| 29 | Bessere Informationsfilterung | Rank information by relevance, authority, recency and directness. |
| 30 | Bessere Konsistenzkontrolle | Run contradiction scan across requirements, evidence, decisions and final output. |
| 31 | Stärkere QA / Review | Mandatory final requirement coverage, evidence and completion checks. |
| 32 | Bessere Code-Analyse | Inspect architecture, dependencies, tests and change surface before editing. |
| 33 | Bessere Debugging-Workflows | Reproduce -> isolate -> hypotheses -> discriminate -> root fix -> regression. |
| 34 | Bessere lange Coding-Aufgaben | Checkpoint state, keep plan/task graph, review between milestones and run regressions. |
| 35 | Bessere Computer-Use-Aufgaben | Observe -> act -> observe; verify UI state after meaningful actions when computer tools exist. |
| 36 | Besser bei vielen Dateien / Komponenten | Map relevant files/components and retrieve targeted context instead of loading blindly. |
| 37 | Besser bei komplexen Tool-Workflows | Explicit preconditions, tool outputs, dependencies, retry policy and completion checks. |
| 38 | Weniger Model-Round-Trips nötig | Resolve non-critical ambiguity from evidence/context; ask only when missing info changes the safe/correct action. |
| 39 | Weniger User-Guidance nötig | Maintain state and self-check rather than asking the user to supervise each internal step. |
| 40 | Bessere Design-Judgement | Compare alternatives against constraints, trade-offs, references and failure modes. |
| 41 | Besseres Inspect -> Refine -> Deliver | Hard workflow invariant for artifacts and consequential work. |
| 42 | Stärkere Endergebnisse / faster parallel work | Use native parallelism where possible, but never trade correctness for superficial concurrency. |

## Additional improvements that skills can influence

### Reasoning discipline

- task difficulty triage;
- constraint extraction;
- assumption tracking;
- evidence tracking;
- independent hypothesis generation;
- adversarial criticism;
- counterexample search;
- edge-case analysis;
- contradiction scanning;
- confidence calibration;
- stopping rules;
- re-plan triggers;
- requirement coverage checks.

### Context and memory behavior

- retrieve relevant history/files before asking for repetition;
- preserve exact constraints through summaries;
- compact stale details while keeping decisions and blockers;
- maintain project state and decision logs in files when supported;
- reconstruct state on resume;
- avoid flooding subagents with irrelevant context;
- hand off bounded context to specialist agents.

### Tools and research

- capability discovery;
- choose the right tool for the evidence needed;
- avoid unnecessary tool spam;
- batch independent tool calls;
- serialize conflicting writes;
- inspect tool errors before retrying;
- source authority/recency ranking;
- primary-source preference;
- citation/evidence verification;
- distinguish source facts from inference;
- stop after adequate evidence rather than searching indefinitely.

### Coding and debugging

- inspect before modifying;
- read repository instructions;
- map dependencies;
- minimal coherent change;
- tests as executable requirements;
- reproduce bugs first;
- systematic hypothesis testing;
- focused test -> broader regression;
- lint/typecheck/build where relevant;
- inspect final diff;
- avoid speculative refactors;
- detect stuck loops and change approach;
- verification before completion.

### Computer use

When native computer/browser control is present:

- state observation before action;
- explicit action goal;
- post-action observation;
- detect unexpected navigation/dialogs;
- minimize irreversible actions;
- preserve user control for consequential external actions;
- verify completion in the actual UI.

A text skill cannot create computer control in a runtime that lacks it.

### Files, documents, visual, 3D and game work

If the runtime exposes the needed tools, a skill can enforce:

- reference extraction before creation;
- measurement/constraint tracking;
- versioned artifacts;
- preview/render/inspection before delivery;
- comparison against references;
- structured refinement passes;
- optimization checks;
- regression screenshots/renders;
- file-format validation;
- performance/complexity budgets.

Without those tools, the skill can specify or critique but must not claim it rendered, opened, measured or executed the artifact.

## Workarounds for unavailable capabilities

| Desired feature | Present workaround |
|---|---|
| Real multi-agent in plain chat | Four isolated reasoning roles; label them workstreams, not agents. |
| Parallel execution without concurrency | Execute independent workstreams sequentially with separate assumptions and outputs. |
| Persistent memory | Write/read a compact `STATE.md` or project note when file access exists; otherwise summarize state in conversation. |
| Huge context window | Targeted retrieval + summaries + constraint/decision preservation. |
| More compute | Structured depth allocation and extra verification passes; never claim actual extra compute. |
| Model routing | Only route when the harness exposes selectable child models; otherwise use role specialization on the current model. |
| Background work | Use scheduler/event mechanism only if exposed; otherwise perform current-turn work and do not promise later execution. |
| Full desktop control | Use available browser/app/file tools; otherwise provide instructions rather than pretend to click/type. |
| Automatic visual QA | Use preview/render/screenshot tools if exposed; otherwise flag visual QA as unperformed. |
| Shared agent blackboard | Use durable project files or orchestrator summaries when agents can read them. |
| Unlimited agent swarm | Use a small set of high-value roles; scale only when runtime capacity and task decomposition justify it. |

## Future / experimental capability layer

These are intentionally documented as `FUTURE` unless a harness exposes them:

- 10-100+ agent swarms with independent context;
- dynamic creation/destruction of specialist agents;
- automatically selected heterogeneous models per task;
- independent adversarial agent tournaments;
- run 20+ candidate solutions, execute tests/benchmarks on each and select the winner;
- massive parallel web/repository exploration;
- continuously maintained project model across days/weeks;
- native persistent shared memory between agents and harnesses;
- automatic project maintenance triggered by repository/product events;
- autonomous AI project manager + technical lead + QA/research/design/development team;
- true runtime control of context window, token allocation and inference compute;
- one conversation coordinating long-running work across many computers/services.

Activation rule: a future feature becomes `NATIVE` only after the current runtime exposes and confirms the underlying primitive. Until then use the documented fallback or skip it.