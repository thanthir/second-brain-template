---
type: system
created: 2026-06-07
---

# Conventions

The rules of this vault. Claude reads this before doing any work here.

## Folder roles

| Folder      | Purpose                                                                                                                                    |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `Inbox/`    | Raw capture. Anything goes. Claude processes and empties it.                                                                               |
| `Notes/`    | Atomic, processed notes. One idea per note, linked.                                                                                        |
| `Projects/` | One **folder per project** (a workspace). See *Project workspaces* below.                                                                  |
| `Maps/`     | Maps of Content (MOCs) — curated indexes by theme. Holds [[Map of Maps]] and cross-cutting maps; project MOCs live inside their workspace. |
| `Daily/`    | Daily notes, `YYYY-MM-DD.md`.                                                                                                              |
| `System/`   | This machinery. Conventions, manual, WAT guide, templates.                                                                                 |

## Project workspaces

A project is a **folder** under `Projects/<Name>/` holding two planes that meet at the hub note — a knowledge plane Obsidian indexes, and a WAT execution plane it ignores. See [[WAT Guide]].

| Path | Role | Plane |
|---|---|---|
| `Projects/<Name>/` | The workspace. Folder name **==** hub-note name (keeps `[[wikilinks]]` resolving). | — |
| `<Name>.md` | Hub note (`type: project`) — status, tasks, log, decisions. Graph entry point. | knowledge |
| `<Name> Map.md` | Project MOC (`type: map`) — indexes the project's atoms; links up to [[Map of Maps]]. | knowledge |
| `Knowledge/` | Project-local atomic notes. | knowledge |
| `CLAUDE.md` | Per-project execution rules (auto-loaded when working here). | execution |
| `workflows/*.md` | SOPs (`type: workflow`). | execution |
| `tools/` | Python scripts; `tools/README.md` is the registry. | execution |
| `.tmp/` `.env` `credentials.json` `token.json` | Machinery — **never** knowledge. Always excluded from Obsidian + gitignored. | execution |

**Knowledge locality:** a note born in a project lives in that project's `Knowledge/`. When a second project links it, **promote** it to the global `Notes/`. Cross-cutting notes start in `Notes/`.

**Naming:** folder name == hub-note name; knowledge folders Title-Case (`Knowledge/`); execution folders lowercase (`workflows/ tools/`); workflows `kebab-case.md` (imperative verb); tools `kebab-case.py` matching their workflow step.

## Frontmatter schema

Every note gets:

```yaml
type: note | project | daily | map | system | workflow
created: YYYY-MM-DD
tags: []
```

Projects additionally:

```yaml
status: active | waiting | someday | done
due: YYYY-MM-DD   # optional
```

Workflows additionally:

```yaml
tools: []     # tools/<name>.py scripts called
inputs: []    # required before starting
outputs: []   # where the deliverable lands
```

## Statuses

- **active** — being worked now
- **waiting** — blocked on someone/something (note what in the body)
- **someday** — not now, don't lose it
- **done** — keep for reference

## Tasks

Use standard markdown checkboxes `- [ ]` inside project and daily notes. No separate task system — Dataview aggregates them onto [[Home]].

## Linking

- Link aggressively with `[[wikilinks]]`. A link to a note that doesn't exist yet is a TODO, not an error.
- Every processed note should link to at least one other note or map.
- New themes (3+ related notes) get a Map in `Maps/`.
- Roll-up chain: atom → project MOC (`<Name> Map`) → [[Map of Maps]]. Every project MOC must be listed in [[Map of Maps]] so no workspace becomes an orphan island.

## Capabilities

The skills and connectors available to Claude are documented in [[Capabilities]]. Consult it before reaching for external tools; update it when the toolset changes. Skills/connectors are installed in the Cowork app, not in this vault — the vault only documents them.

## Naming

- Notes: plain descriptive titles, `Spaced repetition beats rereading.md`
- Projects: noun phrases, `AI Operating System.md`
- Maps: theme + ` Map` suffix, `AI Persona Map.md` — avoids name collisions with projects on the same theme
- No dates in note titles except `Daily/`.
- Workspaces & execution: see *Project workspaces* above (folder == hub note; lowercase execution folders; `kebab-case` for workflows and tools).
