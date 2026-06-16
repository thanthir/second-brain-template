---
type: workflow
created: 2026-01-01
tags: [sample]
tools: [fetch-url.py]   # tools/<name>.py scripts this workflow calls
inputs: [url]           # what the agent must have before starting
outputs: [Knowledge/<slug>.md]   # an atomic note in this project's Knowledge/
---

# digest-url

**Goal:** turn one web URL into a clean, linked atomic note in `Knowledge/`.

## Preconditions

- [ ] A URL to digest.
- [ ] Python 3 available (the tool is stdlib-only — no install, no secrets).
- [ ] *Optional:* `SUMMARY_API_KEY` in `.env` if you enable the LLM-summary step in `fetch-url.py`. Not needed for the default path.

## Steps

1. **Fetch & clean.** Run the tool from the project root:
   ```
   python3 tools/fetch-url.py "<url>"
   ```
   It downloads the page, strips HTML/scripts, and writes plain text to `.tmp/<slug>.txt` (printing the slug + path).
2. **Read** `.tmp/<slug>.txt` and distill it: pull the single core idea, stated in your own words.
3. **Write the atom.** Create `Knowledge/<slug>.md` from the [[Note]] template:
   - Title = the idea (not the URL).
   - Body = a few crisp sentences in your own words.
   - `**Source:**` = the original URL.
   - `**Related:**` = `[[wikilinks]]` to at least one other note or `[[Research Digest Map]]`.
4. **Index it.** Add the new note under *Knowledge* in `Research Digest Map.md`, and append a line to the hub note's Log.

## Deliverable

An atomic note at `Knowledge/<slug>.md`, linked from the MOC. The `.tmp/<slug>.txt` extraction is disposable and regenerable — never the deliverable.

## Failure & retry

- **403 / blocked:** some sites reject non-browser agents. The tool sends a basic User-Agent; if still blocked, note it and digest from a pasted excerpt instead.
- **Paywalled / JS-only pages:** stdlib fetch can't render JavaScript. Fall back to a reader view or manual paste; consider a browser-automation tool if this recurs.
- Update this section as you learn (the self-improvement loop in [[WAT Guide]]).
