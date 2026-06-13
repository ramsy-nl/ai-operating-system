# Reference Examples

> Layer 2 — Verification. Known-good outputs to compare new work against. When an
> agent produces something, it checks it against the closest example here.

## What belongs here

- Golden outputs (the canonical correct result for a given input).
- Worked examples of the right shape, tone, or structure.
- "Before / after" pairs that show what good looks like.

## What does not

- Secrets or real customer data — use synthetic or anonymised samples.
- One-off scratch files. Examples are curated, not a dumping ground.

## Convention

Name each example for what it demonstrates and, where useful, pair the input with
its expected output:

```
examples/
  churn-report.input.json
  churn-report.expected.md
```

Reference the relevant example from the corresponding test case in
`verification/test-plan.md`.
