---
type: system
created: 2026-06-07
---

# AI OS Manual

How this system runs. Obsidian is the display layer; Claude (via Cowork, pointed at this folder) is the processor. You capture and read — Claude organizes, links, and synthesizes.

## The five loops

### 1. Capture → Process
Dump anything into `Inbox/` — a thought, a pasted article, a link, a voice-memo transcript. Then tell Claude:

> **"Process my inbox"** — Claude turns each item into atomic notes in `Notes/`, links them, files tasks into the right project, updates maps, and empties the inbox.

### 2. Daily dashboard
[[Home]] is the front page. Tell Claude:

> **"Update my dashboard"** — Claude refreshes Home: open tasks across projects, what's stalled, what's due, a short "needs attention" briefing. Also creates today's note in `Daily/` if missing.

This can run automatically every morning — ask Claude to schedule it.

### 3. Synthesis
Once notes accumulate:

> **"Synthesize my notes on X"** or **"Find connections I'm missing"** — Claude reads across `Notes/`, writes or updates Maps in `Maps/`, and flags contradictions or clusters worth a project.

### 4. Projects
> **"New project: ..."** — Claude creates it from the template.
> **"Project review"** — Claude sweeps `Projects/`, flags stalled active projects, surfaces waiting-on items, suggests status changes.

### 5. Capabilities
The toolset (skills, plugins, MCP connectors) is registered in [[Capabilities]].

> **"Refresh my capabilities"** — Claude re-inventories what's installed and updates the registry.

### 6. Execute (WAT)
Projects aren't just notes — each is a workspace that can *run work*. See [[WAT Guide]].

> **"Run the X workflow in project Y"** — Claude opens `Projects/Y/`, reads its `CLAUDE.md` and `workflows/X.md`, checks `tools/` for an existing script, runs it (intermediates → `.tmp/`, deliverable → the named cloud target), and updates the workflow with anything learned.

> **"New workflow / new tool for project Y"** — Claude scaffolds from [[Workflow]] template into `workflows/`, and adds the script + `tools/README.md` entry. It asks before overwriting an existing workflow.

The self-improvement loop (fix tool → verify → update workflow) lives in [[WAT Guide]].

## Obsidian setup (one-time, 5 min)

1. Open Obsidian → **Open folder as vault** → select this `Second Brain` folder.
2. Settings → Community plugins → turn off Restricted mode → install **Dataview** → enable it. (Powers the live queries on [[Home]].)
3. Optional: set [[Home]] as your start page via the **Homepage** plugin.

## Rules Claude follows

- Read [[Conventions]] before writing anything; check [[Capabilities]] before claiming a tool doesn't exist.
- Inside a project workspace, read its nested `CLAUDE.md` and `workflows/` before executing; run scripts and touch `.env`/`.tmp/` only from within the project, never from the root.
- Never delete user-written content; archive or ask.
- Inbox items are sacred input — process fully, don't skim.
- Prefer editing existing notes over creating near-duplicates.
