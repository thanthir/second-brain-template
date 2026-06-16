---
type: workflow
created: {{date}}
tags: []
tools: []        # tools/<name>.py scripts this workflow calls
inputs: []       # what the agent must have before starting
outputs: []      # where the deliverable lands (named cloud service / path)
---

# {{title}}

**Goal:** <!-- what this workflow accomplishes, one sentence -->

## Preconditions

<!-- required inputs, env keys (by name), and any cloud auth that must already be set up -->

- [ ]

## Steps

1. <!-- step → which tool in tools/ to run, with what inputs -->
2.

## Deliverable

<!-- exactly what is produced and where it lands. Deliverables → cloud; intermediates → .tmp/ -->

## Failure & retry

<!-- known edge cases, rate limits, retry strategy. Update this as you learn (self-improvement loop). -->
