---
name: planning
description: Use after the spec is confirmed and before writing implementation code — breaks the goal into small, independently reviewable checkpoints and decides how before doing.
phase: 2
---

# Planning Prompt

> Reusable phase 2 of 4: `discovery → planning → implementation → review`.
> Use after the spec is confirmed, to break the goal into reviewable checkpoints
> and decide *how* before doing.

## When to use
After `specs/project-goal.md` is confirmed and before writing implementation code.

## The prompt

```
You are in PLANNING. Do not write implementation code yet.

Inputs: specs/project-goal.md, specs/requirements.md, knowledge/.

1. Reuse first: check knowledge/architecture.md and knowledge/patterns.md. Prefer
   existing patterns over new ones.
2. Break the work into small checkpoints (each independently reviewable and
   shippable). Map each to the requirements it implements.
3. For each checkpoint, state its verification (how we'll know it's done) and any
   approval gate it triggers (guardrails/ask-first.md).
4. Call out the riskiest assumption and how the plan de-risks it early.
5. Log any non-obvious architectural choice in specs/decisions.md.

Write the checkpoints into specs/checkpoints.md and stop for my approval before
starting CP-1.
```

## Output
A populated `specs/checkpoints.md`, decisions logged, approved by the user.

## Done when
- Each checkpoint is small, ordered, and has named verification.
- Approval gates are identified.
- The user has approved the plan.
