# Review Prompt

> Reusable phase 4 of 4: `discovery → planning → implementation → review`.
> Use to verify a checkpoint (Layer 2) before marking it done. This is where
> "done" is earned, not declared.

## When to use
After a checkpoint is implemented, before marking it `Done` and before requesting
human review.

## The prompt

```
You are in REVIEW. Verify CP-N rigorously and without optimism.

1. Walk verification/review-checklist.md item by item. Tick only what you have
   actually checked.
2. Run every evaluation criterion in verification/evaluation-criteria.md that
   applies. Paste real evidence — command output, comparisons, numbers.
3. Compare output against the relevant verification/examples/ where applicable.
4. Confirm no guardrails/never-do.md action was taken and any ask-first action
   was approved.
5. Report honestly:
   - If everything passes: state it plainly, with the evidence, and update
     specs/checkpoints.md to Done. Capture anything reusable in knowledge/.
   - If anything fails or is uncertain: say so, list what's outstanding, and do
     NOT mark it done.

No success claim without pasted evidence. Evidence before assertions.
```

## Output
A verified checkpoint marked `Done` with evidence — or an honest list of what's
still outstanding.

## Done when
- The review checklist passes with real evidence.
- `knowledge/` and `lessons-learned.md` updated as warranted.
- `specs/checkpoints.md` reflects the true status.
