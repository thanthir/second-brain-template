---
type: project
status: active
created: 2026-01-01
due:
tags: [sample]
---

# Research Digest

**Outcome:** any web URL becomes a clean, linked atomic note in this project's `Knowledge/` — read once, keep forever.

**MOC:** [[Research Digest Map]] · **Workflows:** see `workflows/` · **Tools:** see `tools/README.md`

> [!info] This is a sample workspace
> It exists to demonstrate the **WAT execution plane** end to end — a [[WAT Guide|workflow]] that orchestrates a Python [tool](tools/fetch-url.py), writes intermediates to `.tmp/`, and lands a deliverable in `Knowledge/`. Read it, run it once, then delete it (or repurpose it) and build your own. See [[AI OS Manual]] loop 6.

## Tasks

- [ ] Run the [[digest-url]] workflow on one URL to see the loop work end to end

## Key decisions

<!-- locked decisions; link to atoms in Knowledge/ or the MOC -->

- Tool is **stdlib-only** (no `pip install`, no secrets) so the sample runs anywhere. Optional LLM-summary step is sketched but off by default.

## Log

- 2026-01-01 — created (template sample)

## Notes & links

- [[WAT Guide]] · [[Conventions]]
