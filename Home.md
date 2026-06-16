---
type: system
created: 2026-01-01
---

# 🏠 Home

> [!tip] Welcome
> This is your Second Brain. Capture into `Inbox/`, then tell Claude **"Process my inbox."** Read the [[AI OS Manual]] for the five loops, and the [README](README.md) for setup. The tables below are live [Dataview](https://github.com/blacksmithgu/obsidian-dataview) queries — install the Dataview plugin to see them render. There's one sample workspace to learn from: [[Research Digest]].

## Active projects

```dataview
TABLE status, due, file.mtime AS "updated"
FROM "Projects"
WHERE status = "active" OR status = "waiting"
SORT status ASC, due ASC
```

## Open tasks

```dataview
TASK
FROM "Projects" OR "Daily"
WHERE !completed
GROUP BY file.link
```

## Workspaces

```dataview
TABLE status, file.folder AS "workspace"
FROM "Projects"
WHERE type = "project"
SORT status ASC
```

```dataview
TABLE inputs, outputs, file.folder AS "in"
FROM "Projects"
WHERE type = "workflow"
SORT file.folder ASC
```

## Inbox

```dataview
LIST
FROM "Inbox"
SORT file.ctime DESC
```

## Recent notes

```dataview
TABLE file.mtime AS "modified"
FROM "Notes"
SORT file.mtime DESC
LIMIT 10
```

---

Manual: [[AI OS Manual]] · Rules: [[Conventions]] · Maps: [[Map of Maps]] · Capabilities: [[Capabilities]]
