# Capabilities

The toolset behind this vault. This is a **registry, not an installer** — skills and connectors are installed in your AI app (e.g. Cowork → Settings → Capabilities / Connectors, or Claude Code), available app-wide. Claude can't install or modify them from a session; it reads this note to know what exists and when to reach for it.

> **"Refresh my capabilities"** — Claude re-inventories what's installed and updates this note.

> **This is a starter list.** The entries below are common defaults — yours will differ. After you set up your tools, run *"Refresh my capabilities"* so Claude rewrites this registry to match what you actually have installed.

Last verified: <!-- run "Refresh my capabilities" to stamp this -->

## Document & output skills

| Skill | Use for |
|---|---|
| docx | Word documents — reports, memos, letters |
| xlsx | Spreadsheets, budgets, data tables, charts |
| pptx | Slide decks and presentations |
| pdf | Read, create, merge, split, fill PDF forms |
| frontend-design | Production-grade web UI / components |

## Thinking & workflow skills

| Skill | Use for |
|---|---|
| deep-research | Multi-source, fact-checked research reports |
| schedule | Recurring/automated tasks ("every morning…") |
| skill-creator | Build or improve custom skills |

## Plugins

<!-- List installed plugins and the skills/connectors they bundle. Example:
### design
Skills: accessibility-review, design-critique, design-handoff
Connectors (auth on first use): Figma, Linear, Notion, Slack
-->

## MCP connectors

| Connector | Status | Use for |
|---|---|---|
| <!-- e.g. Figma --> | <!-- Connected --> | <!-- read/write designs --> |

<!-- Record any project-specific keys/IDs here (file IDs, sheet IDs, board URLs) so Claude can find them. Never record secret values — those live in a project's .env, referenced by name only. -->

## Built-in (always available)

Web search & fetch · scheduled tasks · live HTML artifacts · persistent memory · MCP registry search (find new connectors on demand)

## Execution runtime (WAT)

The execution plane that powers per-project [[WAT Guide|WAT]] workspaces. Unlike skills/connectors, this runs in the processor (Claude Code), not Obsidian.

| Capability | Notes |
|---|---|
| Python runtime | Tools are `tools/*.py` per project. Use a venv + `requirements.txt`; deterministic execution layer. |
| Secret handling | Per-project `.env` / `credentials.json` / `token.json`. Loaded at runtime, referenced by **name** only — never written into notes. Always excluded from Obsidian + gitignored. |
| Per-project tools registry | Each `tools/README.md` lists its scripts: name, purpose, inputs/outputs, required env-var names. That README is the registry — this note keeps only a one-line index per project pointing at it. |

**Project tools index** (one line per project as workspaces gain tools):

- [[Research Digest]] — `Projects/Research Digest/tools/README.md` — `fetch-url.py` (fetch a URL → cleaned plain text in `.tmp/`; stdlib-only, no secrets)

## Gaps / wishlist

<!-- Tools the OS needs but lacks. Log them here; build via skill-creator or install via Settings. -->

-

## Maintenance rules

- When a connector or skill is added/removed in Settings, update this note (or run "refresh my capabilities").
- Before saying "I can't do X," Claude searches the MCP registry for a connector first.
- New skills the OS needs but lacks → log under Gaps, build via skill-creator or install via Settings.
- WAT principle: deliverables → named cloud services; intermediates → `.tmp/`; offload deterministic work to `tools/` scripts so Claude orchestrates rather than executes by hand.
- When a project adds a tool, register it in that project's `tools/README.md` and add a one-line pointer to the *Project tools index* above.
