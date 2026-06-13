# Debugging Prompt

> A parallel phase to the main rhythm (`discovery → planning → implementation →
> review`). Use whenever something breaks: a bug, a failing test, or unexpected
> behaviour. The discipline: **find the root cause before you change anything.**
>
> Based on the systematic-debugging skill from
> [Superpowers](https://github.com/obra/superpowers).

## The iron rule

No fix before a confirmed root cause. A fix applied to a symptom you don't
understand is a guess, and guesses scatter new bugs. If you're tempted to "just
try something," that's the red flag (`guardrails/red-flags.md`).

## The four phases

### 1. Reproduce
Make the failure happen on demand. A bug you can't reproduce is a bug you can't
verify you've fixed.
- What is the smallest, most reliable way to trigger it?
- Capture the exact error, stack trace, and inputs.

### 2. Diagnose (root cause)
Work from the symptom back to the cause. Don't stop at the first plausible
culprit.
- What did you *expect* to happen, and what happened instead?
- Form a hypothesis. **Make a prediction it implies, then test that prediction.**
- Narrow it: bisect, add targeted logging, check assumptions about data shape.
- Keep asking "but why did *that* happen?" until you reach the true cause, not a
  proximate one.

### 3. Fix
Only now, change code — the minimum that addresses the root cause.
- Write a failing test that reproduces the bug first (RED). Then fix it (GREEN).
  That test is now permanent regression protection.
- Don't fix unrelated things you noticed along the way; log them separately.

### 4. Verify & capture
- Run the reproduction from phase 1: it must now pass.
- Run the full test suite — confirm you didn't break anything else. Paste output.
- Record the cause and fix in `knowledge/lessons-learned.md` if it was
  non-obvious or could recur.

## The prompt

```
You are DEBUGGING. Do not propose or apply a fix yet.

1. REPRODUCE: give me the smallest reliable way to trigger this, with the exact
   error/stack/inputs.
2. DIAGNOSE: state your hypothesis for the root cause, the prediction it implies,
   and the result of testing that prediction. Keep going until you reach the true
   cause, not a symptom.
3. Only once the root cause is confirmed, FIX: write a failing regression test
   first, then the minimal fix.
4. VERIFY: rerun the reproduction and the full suite; paste real output. Capture
   a non-obvious cause in knowledge/lessons-learned.md.
```

## Done when
- The bug is reproduced, the **root cause** (not a symptom) is confirmed.
- A regression test exists and now passes.
- The full suite passes with pasted evidence.
- A non-obvious cause is recorded in `lessons-learned.md`.
