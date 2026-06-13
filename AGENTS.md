# AI Operating Rules

> This is the **single source of truth** for how any AI agent operates in this
> repository. Claude (`CLAUDE.md`), Cursor (`.cursor/rules/`), and GitHub Copilot
> (`.github/copilot-instructions.md`) all inherit from this file. Edit it here.
>
> The model is interchangeable. The operating system is not.

The operating model has three layers. Work through them in order: you cannot
verify (Layer 2) what you never specified (Layer 1), and you cannot specify or
verify well without the environment (Layer 3).

---

## Layer 1: Specification

Before writing any code, you must be able to state four things in one sentence each:

1. **Goal** — what decision or outcome does this work enable?
2. **Constraints** — time, budget, technical, legal.
3. **Success criteria** — how we will know it worked, measurably.
4. **Deliverable** — the concrete artifact produced.

If you cannot fill all four in, you are not ready to implement.

**Before implementation:**
- Interview the user when goals are unclear. Ask, don't assume. One sharp
  question now saves a wasted afternoon later.
- Break work into small checkpoints (see `specs/checkpoints.md`). Each checkpoint
  is independently reviewable and shippable.
- Require explicit approval for major decisions and anything in
  `guardrails/ask-first.md`.
- Record non-obvious choices in `specs/decisions.md` as you make them.

## Layer 2: Verification

Verification is not a final gate you arrive at — it's a discipline you work
*inside*. Wherever the deliverable is testable, **write the test before the
code**:

- **RED** — write a failing test that captures the requirement. Run it; watch it fail for the right reason.
- **GREEN** — write the minimum code to make it pass.
- **REFACTOR** — clean up with the passing test holding you safe.

Around that loop:
- Define evaluation criteria *up front* (`verification/evaluation-criteria.md`), not after the fact.
- Self-review against `verification/review-checklist.md`; compare to known-good `verification/examples/`.
- For work others will review, follow `verification/code-review.md` — severity-based, rigor over agreement, both when requesting and receiving review.
- Run tests and paste the **actual** output, not a summary of it.

**Never claim something is complete without verification.** "It should work" is
not "it works." Evidence before assertions, always.

## Layer 3: Environment

Use what already exists before inventing:
- The knowledge base (`knowledge/`) — architecture, patterns, glossary.
- The existing architecture and conventions of the host project.
- Lessons already learned (`knowledge/lessons-learned.md`) — do not re-learn them.

After any significant work, **update the documentation** so the next agent (or
the next you) starts ahead of where you started.

---

## Guardrails

Three lists govern what you may do autonomously. Read them before acting.

- `guardrails/always-do.md` — non-negotiable steps for every task.
- `guardrails/ask-first.md` — stop and get explicit human approval.
- `guardrails/never-do.md` — hard stops, no exceptions.
- `guardrails/red-flags.md` — thoughts that mean you're rationalizing a shortcut. When you catch one, stop.

## Working rhythm

The `prompts/` directory holds the reusable phases of a unit of work:
`discovery → planning → implementation → review`. When something breaks, switch
to `prompts/debugging.md` and find the root cause before touching a fix. When in
doubt about how to start, open `prompts/discovery.md`.

## The one rule that overrides convenience

When a fast path conflicts with a guardrail, the guardrail wins. The whole point
of this repository is that correctness and approval are not optional, even when
the model is confident.

---

## Lineage

The disciplines here — test-first (RED-GREEN-REFACTOR), root-cause debugging,
severity-based code review, evidence over claims, and the red-flag self-checks —
draw on Jesse Vincent's [Superpowers](https://github.com/obra/superpowers)
methodology. Superpowers is an *executable* auto-activating skills system; this
repository is the *documented* operating model that any tool can follow. They
compose well: if your environment has the Superpowers skills installed, they
enforce at runtime what these files describe.
