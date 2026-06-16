---
type: system
created: 2026-06-08
tags: [wat, execution]
---

# WAT Guide

How projects in this vault *run work*, not just store it. This is the bridge between the WAT framework (Workflows, Agents, Tools) and the Obsidian knowledge OS. Read this before building or running anything inside a project workspace.

## Two planes, one workspace

Every project folder under `Projects/<Name>/` holds two planes that meet at the **hub note** (`<Name>.md`):

- **Knowledge plane** — markdown Obsidian indexes and links: the hub note, the project MOC (`<Name> Map.md`), and atomic notes in `Knowledge/`. This is what shows in the graph.
- **Execution plane** — code and machinery Obsidian ignores: `workflows/` (SOPs), `tools/` (Python), `.tmp/` (disposable), `.env`/`credentials.json`/`token.json` (secrets). These produce **zero graph edges** — Obsidian only links `.md`.

The hub note links to both: its MOC (knowledge view) and its `workflows/*.md` (execution view).

## The three layers

1. **Workflows — the instructions.** Markdown SOPs in `workflows/`, one per repeatable job. Each states its objective, required inputs, which tools to call in what order, the expected deliverable (and where it lands), and how to handle edge cases. Written in plain language. Frontmatter: `type: workflow` plus `tools:`, `inputs:`, `outputs:`. Use [[Workflow]] template.
2. **Agents — the decision-maker.** That's Claude, working inside the project. It reads the relevant workflow, runs tools in sequence, recovers from failures, and asks when blocked. It orchestrates — it does not do execution by hand.
3. **Tools — the execution.** Python scripts in `tools/`. Deterministic, testable, fast: API calls, transforms, file ops. Each `tools/` folder has a `README.md` registering every script (name, purpose, inputs/outputs, required `.env` key *names*). Secrets load at runtime from `.env`; values never appear in notes.

**Why split this way:** if every step is 90% accurate, a five-step chain succeeds ~59% of the time. Offloading deterministic steps to scripts keeps Claude focused on orchestration, where it's strong, and keeps execution reliable.

## Operating rules

- **Look for an existing tool first.** Check `tools/README.md` before writing a new script.
- **Deliverables → cloud; intermediates → `.tmp/`.** Anything you need to see or use lives in a named cloud service (Google Sheets, Slides, Figma, …). Everything in `.tmp/` is disposable and regenerable.
- **Secrets stay in `.env`.** Never inline keys into notes, workflows, or tool source. Reference them by name.
- **Run scripts only from inside the project**, where the nested `CLAUDE.md` and `.env` apply — not from the vault root.

## The self-improvement loop

Every failure strengthens the system:

1. Identify what broke (read the full error/trace).
2. Fix the tool, then retest. *If it uses paid APIs or credits, confirm with the user before re-running.*
3. Verify the fix works.
4. Update the workflow with what you learned (rate limits, batch endpoints, timing quirks).
5. Move on with a more robust system.

Don't overwrite or create workflows without asking — they are refined instructions, not scratch.

## How it maps onto folders

```
Projects/<Name>/
├── <Name>.md        ← hub note (orchestration entry; links both planes)
├── CLAUDE.md        ← per-project execution rules (auto-loaded here)
├── <Name> Map.md    ← project MOC → links up to [[Map of Maps]]
├── Knowledge/       ← project-local atomic notes (knowledge plane)
├── workflows/*.md   ← layer 1 (SOPs)
├── tools/*.py       ← layer 3 (Python) + README.md registry
├── .tmp/            ← disposable intermediates
└── .env …           ← secrets (excluded + gitignored)
```

See [[Conventions]] for folder roles and naming, [[Capabilities]] for runtime/secret handling, and [[AI OS Manual]] loop 6 (Execute) for the run trigger.
