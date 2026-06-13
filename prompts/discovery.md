---
name: discovery
description: Use at the start of a unit of work when the goal, constraints, or success criteria aren't all crystal clear — turns a vague request into a confirmed specification (Layer 1) before any planning or code.
phase: 1
---

# Discovery Prompt

> Reusable phase 1 of 4: `discovery → planning → implementation → review`.
> Use this to turn a vague request into a clear specification (Layer 1) before
> any planning or code.

## When to use
At the very start of a unit of work, whenever the goal, constraints, or success
criteria are not all crystal clear.

## The prompt

```
You are in DISCOVERY. Do not write code or a plan yet.

Goal: turn this request into a clear specification.

1. Restate the request in your own words.
2. Identify what's unknown. Ask me the smallest set of sharp questions that would
   let you fill in all four of: Goal, Constraints, Success criteria, Deliverable.
3. Surface hidden assumptions and risks.
4. Propose what is explicitly OUT of scope.

When you can state Goal / Constraints / Success criteria / Deliverable each in one
sentence, write them into specs/project-goal.md and stop for my confirmation.
```

## Output
A filled-in `specs/project-goal.md` (and `requirements.md` if detail warrants),
confirmed by the user. Do not proceed to planning until confirmed.

## Done when
- All four specification elements are stated in one sentence each.
- Out-of-scope is explicit.
- Open questions are either answered or logged for the relevant checkpoint.
