# tools/ — Research Digest

The execution layer for this workspace. Scripts are deterministic; Claude orchestrates them via the workflows. This file is the **registry** — add a row whenever you add a script.

| Script | Purpose | Inputs | Outputs | Env keys |
|---|---|---|---|---|
| `fetch-url.py` | Fetch a web page, strip HTML/scripts, write cleaned plain text | `<url>` (argv) | `.tmp/<slug>.txt` (disposable) | none (optional `SUMMARY_API_KEY` for the off-by-default summary step) |

## Conventions

- Run from the **project root**: `python3 tools/fetch-url.py "<url>"`.
- Intermediates → `.tmp/` (disposable, gitignored). Deliverables → notes in `Knowledge/`.
- Secrets load from `.env` at runtime, referenced **by name** only — never inline values into scripts or notes. See `.env.example`.
- `requirements.txt` lists optional deps; the default path is stdlib-only.
