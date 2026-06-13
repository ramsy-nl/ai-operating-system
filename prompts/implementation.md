# Implementation Prompt

> Reusable phase 3 of 4: `discovery → planning → implementation → review`.
> Use to build **one checkpoint at a time** against the approved plan.

## When to use
After the plan in `specs/checkpoints.md` is approved. Take one checkpoint.

## The prompt

```
You are in IMPLEMENTATION. Work on exactly ONE checkpoint: CP-N.

Before coding:
- Re-read the checkpoint's goal, its requirements, and knowledge/patterns.md.
- Confirm CP-N triggers no unapproved action in guardrails/ask-first.md. If it
  does, stop and ask.

While coding (test-first — RED-GREEN-REFACTOR):
- RED: write a failing test that captures the requirement; run it, watch it fail
  for the right reason.
- GREEN: write the minimum code to make it pass.
- REFACTOR: clean up with the test holding you safe.
- Match the surrounding code's style and conventions.
- Prefer existing patterns; if you invent a reusable one, add it to patterns.md.
- Make the smallest change that satisfies the requirement. No scope creep.
- Log any non-obvious decision in specs/decisions.md as you go.
- If something breaks, switch to prompts/debugging.md — root cause before fix.

When the checkpoint's code is written:
- Re-run the tests and paste the real output.
- Do NOT mark it done — that happens in REVIEW.

Follow guardrails/always-do.md and guardrails/never-do.md at all times.
```

## Output
Working code for one checkpoint, with tests, ready for review. Not yet marked
`Done`.

## Done when
- The checkpoint's requirement is implemented and nothing extra.
- Tests exist and run; output captured.
- Decisions/patterns updated.
