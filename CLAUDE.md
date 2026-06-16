This folder is my Second Brain — an Obsidian vault that is **both** a knowledge OS and a WAT execution environment.

- **Knowledge plane** — atomic notes, maps, and project hub notes (markdown, linked, in the Obsidian graph). This is the default at the vault root.
- **Execution plane** — per-project WAT workspaces (`workflows/` SOPs, `tools/` Python, `.tmp/`, `.env`) that run agentic work. Obsidian ignores these; they live inside `Projects/<Name>/`.

Follow the vault rules before reading or writing anything here:

@System/Conventions.md

The toolset (skills, plugins, MCP connectors) available to this vault is documented in:

@System/Capabilities.md

## How to work here

- **At the root, default to the knowledge OS:** capture → process → link → synthesize. See [[AI OS Manual]] for the loops.
- **Inside `Projects/<Name>/`, a nested `CLAUDE.md` adds execution rules.** Read it (and the project's `workflows/`) before running anything. Don't run scripts, touch `.env`, or write to `.tmp/` from the root — do that from within the project.
- **WAT principle:** Claude orchestrates; deterministic work is offloaded to `tools/` scripts. Deliverables → named cloud services; intermediates → `.tmp/`; secrets stay in `.env` (never inline). See [[WAT Guide]].
