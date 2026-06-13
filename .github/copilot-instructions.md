# GitHub Copilot Instructions

GitHub Copilot inherits the full operating model from **[`AGENTS.md`](../AGENTS.md)**
at the repository root. That file is the single source of truth — read it first.

## The three layers (summary)

1. **Specification** — Before generating code, the Goal, Constraints, Success
   criteria, and Deliverable must each be stateable in one sentence.
2. **Verification** — Define evaluation criteria up front, self-review against
   `verification/review-checklist.md`, run tests, and never claim completion
   without evidence.
3. **Environment** — Reuse `knowledge/` (architecture, patterns, glossary) and
   `knowledge/lessons-learned.md` before inventing. Update docs after significant work.

## Guardrails

- `guardrails/always-do.md` — required every task.
- `guardrails/ask-first.md` — stop and get human approval.
- `guardrails/never-do.md` — hard stops.

When a fast path conflicts with a guardrail, the guardrail wins.
