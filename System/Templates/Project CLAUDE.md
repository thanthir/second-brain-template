# {{title}} — Project Instructions

This is a **WAT execution workspace**. When working here, follow these rules in addition to the vault-wide [[Conventions]] and [[WAT Guide]]. (The root `CLAUDE.md` governs the knowledge OS; this file governs execution inside this project.)

## Workspace layout

```
{{title}}/
├── {{title}}.md        ← hub note (status, tasks, log, decisions)
├── {{title}} Map.md    ← project MOC → links up to [[Map of Maps]]
├── Knowledge/          ← project-local atomic notes
├── workflows/*.md      ← SOPs (read before executing)
├── tools/*.py          ← Python; tools/README.md is the registry
├── .tmp/               ← disposable intermediates
└── .env …              ← secrets (never inline values into notes)
```

## Orchestration rules

- Read the relevant `workflows/<wf>.md` before doing the work. Check `tools/README.md` for an existing script before writing a new one.
- Run Python from `tools/`. Write intermediates to `.tmp/` (disposable). Deliverables go to a **named cloud target** (state it in the workflow).
- Secrets load at runtime from `.env`. Required env keys (by **name** only — never values):
  - `<KEY_NAME>` — <!-- what it's for -->
- On failure: read the trace, fix the tool, retest (confirm before re-running anything that costs credits), verify, then update the workflow. Don't overwrite workflows without asking.

## Knowledge rules

- New atomic notes born in this project → `Knowledge/`, linked from `{{title}} Map.md`.
- If a note becomes useful to a second project, promote it to the global `Notes/`.
- Keep the hub note's Log current; index every new atom from the MOC.

## Working instructions

<!-- project-specific conventions: UI/output style, naming, hand-off format, anything that used to live inline in the hub note -->
