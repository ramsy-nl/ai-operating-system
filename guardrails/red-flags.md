---
name: red-flags
description: Use continuously while working — when you catch yourself thinking a rationalization ("it should work", "just this once", "I'll test it after", "it's probably this line"), stop; the thought is the warning that you're about to skip the operating model.
enforcement: self-check
---

# Red Flags

> Guardrails. Certain thoughts are a signal that you're about to rationalize a
> shortcut past the operating model. When you catch yourself thinking one of
> these, **stop** — the thought is the warning, not the permission.
>
> Inspired by the rationalization tables in
> [Superpowers](https://github.com/obra/superpowers).

## Skipping specification (Layer 1)

| The thought | The reality |
|-------------|-------------|
| "It's obvious what they want." | If it were obvious you could state Goal / Constraints / Success / Deliverable in one sentence each. Can you? |
| "I'll figure out the requirements as I code." | Code built on guessed requirements gets thrown away. Ask first. |
| "This is too small to need a checkpoint." | Small things grow. A 5-minute checkpoint costs nothing and bounds the blast radius. |

## Skipping verification (Layer 2)

| The thought | The reality |
|-------------|-------------|
| "It should work." | "Should" is a guess. Run it and find out. |
| "I'll write the test after." | After is never. Test-first or the test bends to fit the bug. |
| "The change is trivial, no test needed." | Trivial changes are where unverified assumptions hide. |
| "I'll just summarize that the tests passed." | A summary isn't evidence. Paste the real output. |
| "I'm confident this is right." | Confidence is not verification. The repo exists precisely for confident-but-wrong moments. |

## Skipping the environment (Layer 3)

| The thought | The reality |
|-------------|-------------|
| "I'll just invent my own way to do this." | Check `knowledge/patterns.md` first — there may be a blessed way. |
| "I don't have time to read the architecture." | You don't have time to break an invariant you didn't know existed. |
| "I'll document it later." | Later you've forgotten why. Update docs in the same unit of work. |

## Pushing past guardrails

| The thought | The reality |
|-------------|-------------|
| "Just this once, I'll skip the gate." | "Just this once" is the exact case the gate exists for. |
| "Asking for approval will slow things down." | Unapproved irreversible action slows things down far more. |
| "I'll route around the failing check to ship." | A disabled check is a hidden defect, not a fix. |
| "Nobody will notice if I touch production directly." | `never-do.md`. No exceptions. |

## Debugging under pressure

| The thought | The reality |
|-------------|-------------|
| "I'll just try a fix and see if it works." | Guessing scatters new bugs. Find the root cause first (`prompts/debugging.md`). |
| "It's probably this line." | "Probably" means you haven't reproduced it. Reproduce, then diagnose. |
| "I'll suppress the error to make it pass." | Hiding a symptom keeps the disease. |

> The honest move when you hit a red flag is to slow down, name what you were
> about to skip, and do it properly — or escalate.
