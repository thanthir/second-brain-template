# Second Brain — a vault template

A clone-and-go template for a **dual-plane Second Brain**: an Obsidian vault that is *both* a knowledge OS *and* an agentic execution environment.

- **Knowledge plane** — atomic notes, maps, and project hubs (markdown, linked, in the Obsidian graph). You capture and read; Claude organizes, links, and synthesizes.
- **Execution plane** — per-project **WAT** workspaces (`workflows/` SOPs + `tools/` Python + `.env`) that *run work*. Obsidian ignores these; they live inside each project folder.

It ships the full machinery (conventions, manual, templates, config) plus **one worked sample project** so you can see the whole loop run, then build your own.

> **WAT = Workflows · Agents · Tools.** Workflows are markdown SOPs; the Agent is Claude orchestrating; Tools are deterministic Python scripts. Claude orchestrates, scripts execute. See [WAT Guide](System/WAT%20Guide.md).

## Quickstart

1. **Get the files** — either clone with git:
   ```
   git clone https://github.com/thanthir/second-brain-template.git "Second Brain" && cd "Second Brain"
   ```
   **No git?** On the repo page click **`< > Code` → Download ZIP**, unzip it, and rename the `second-brain-template-main` folder to `Second Brain`. (The ZIP includes the hidden `.obsidian/` config and `.env.example`; gitignored files like real `.env`/`.tmp/` are correctly left out. You can always `git init` later if you change your mind.)
2. **Open in Obsidian:** *Open folder as vault* → select this folder.
3. **Enable Dataview:** Settings → Community plugins → turn off Restricted mode → install **[Dataview](https://github.com/blacksmithgu/obsidian-dataview)** → enable it. (It powers the live queries on [Home](Home.md). The bundled `.obsidian/` config already lists it and hides `tools/`/`.tmp/`/`.env` from the file explorer.)
4. **Point your agent at the folder:** open this folder in **Claude Code** (or your AI app, e.g. Cowork). The root [`CLAUDE.md`](CLAUDE.md) auto-loads the vault rules.
5. **Try it:** tell Claude *"Process my inbox"* or run the sample — *"Run the digest-url workflow in Research Digest on `<some article URL>`."*

## The five loops

Drive the system with plain-language triggers (full detail in the [AI OS Manual](System/AI%20OS%20Manual.md)):

| Loop | Say to Claude |
|---|---|
| **Capture → Process** | *"Process my inbox"* — turns `Inbox/` items into linked atoms in `Notes/`. |
| **Daily dashboard** | *"Update my dashboard"* — refreshes [Home](Home.md), creates today's daily note. |
| **Synthesis** | *"Synthesize my notes on X"* / *"Find connections I'm missing"* — writes/updates Maps. |
| **Projects** | *"New project: …"* — scaffolds a workspace from the templates. |
| **Execute (WAT)** | *"Run the X workflow in project Y"* — orchestrates a workflow + its tools. |

## Structure

```
Second Brain/
├── README.md            ← this file
├── LICENSE              ← MIT
├── CLAUDE.md            ← root rules (knowledge OS); auto-loaded by Claude
├── Home.md             ← dashboard (Dataview queries)
├── .obsidian/           ← bundled config (Dataview enabled; execution folders hidden)
├── Inbox/               ← raw capture; Claude processes & empties it
├── Notes/               ← atomic, processed notes (one idea each, linked)
├── Daily/               ← daily notes, YYYY-MM-DD.md
├── Maps/                ← Maps of Content; top of the chain is Map of Maps.md
├── System/              ← the machinery
│   ├── Conventions.md   ← the rules (read first)
│   ├── AI OS Manual.md  ← the five loops
│   ├── WAT Guide.md     ← the execution plane
│   ├── Capabilities.md  ← registry of your skills/connectors ("Refresh my capabilities")
│   └── Templates/       ← Note · Daily · Project · Project MOC · Project CLAUDE · Workflow
└── Projects/
    └── Research Digest/  ← SAMPLE WAT workspace (see below)
```

## Add your own project

Say *"New project: &lt;Name&gt;"* (Claude scaffolds it from `System/Templates/`), or copy the templates by hand. A project is a **folder** whose name matches its hub note, holding two planes that meet at the hub:

- **Knowledge:** `<Name>.md` (hub), `<Name> Map.md` (MOC), `Knowledge/` (atoms).
- **Execution:** `CLAUDE.md` (rules), `workflows/*.md` (SOPs), `tools/*.py` (+ `tools/README.md`), `.tmp/` (disposable), `.env` (secrets — by name only).

List every project MOC in [Map of Maps](Maps/Map%20of%20Maps.md) so no workspace is orphaned. Full rules: [Conventions](System/Conventions.md).

## The sample: Research Digest

[`Projects/Research Digest/`](Projects/Research%20Digest/) is a complete, runnable WAT loop:

- [`workflows/digest-url.md`](Projects/Research%20Digest/workflows/digest-url.md) — the SOP: fetch a URL → clean text → draft an atomic note.
- [`tools/fetch-url.py`](Projects/Research%20Digest/tools/fetch-url.py) — **stdlib-only** (no install, no secrets): downloads a page, strips HTML, writes plain text to `.tmp/`.
- [`tools/README.md`](Projects/Research%20Digest/tools/README.md) — the tool registry.
- `.env.example` — shows the secrets-by-name pattern (the default path needs no key).

Run it once, read how the pieces connect, then delete it or repurpose it.

## Publishing your own copy

This template ships with no git history of your content. To put your own vault on GitHub, create an empty repo on GitHub (no README/license/.gitignore) and push:

```
git remote add origin https://github.com/<your-username>/<your-repo>.git
git branch -M main
git push -u origin main
```

`.env`, `.tmp/`, credentials, and Python caches are gitignored — secrets and disposable intermediates never leave your machine.

## License

[MIT](LICENSE). Use it, fork it, make it yours.
