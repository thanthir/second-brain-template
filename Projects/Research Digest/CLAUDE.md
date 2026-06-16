# Research Digest — Project Instructions

This is a **WAT execution workspace**. When working here, follow these rules in addition to the vault-wide [[Conventions]] and [[WAT Guide]]. (The root `CLAUDE.md` governs the knowledge OS; this file governs execution inside this project.)

## Workspace layout

```
Research Digest/
├── Research Digest.md        ← hub note (status, tasks, log, decisions)
├── Research Digest Map.md    ← project MOC → links up to [[Map of Maps]]
├── Knowledge/                ← project-local atomic notes (the deliverables)
├── workflows/*.md            ← SOPs (read before executing)
├── tools/*.py                ← Python; tools/README.md is the registry
├── .tmp/                     ← disposable intermediates
└── .env …                    ← secrets (never inline values into notes)
```

## Orchestration rules

- Read `workflows/digest-url.md` before doing the work. Check `tools/README.md` for an existing script before writing a new one.
- Run Python from `tools/`. Write intermediates to `.tmp/` (disposable). The deliverable is a note in `Knowledge/`.
- Secrets load at runtime from `.env`. Required env keys (by **name** only — never values):
  - `SUMMARY_API_KEY` — *optional*; only if you enable the LLM-summary step in `fetch-url.py`. The default path needs **no key**.
- On failure: read the trace, fix the tool, retest (confirm before re-running anything that costs credits), verify, then update the workflow. Don't overwrite workflows without asking.

## Knowledge rules

- New atomic notes born in this project → `Knowledge/`, linked from `Research Digest Map.md`.
- If a note becomes useful to a second project, promote it to the global `Notes/`.
- Keep the hub note's Log current; index every new atom from the MOC.

## Working instructions

- One source = one atom. Title the note after the idea, not the URL. Always fill the note's `**Source:**` with the original link.
- Keep the digest in your own words — a few crisp sentences, not a wall of quoted text.
