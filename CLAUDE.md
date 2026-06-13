# CLAUDE.md

Claude Code inherits the full operating model from **[`AGENTS.md`](./AGENTS.md)**.
Read it first — it is the single source of truth. This file only adds
Claude-specific notes.

## Quick reference

1. **Specify** before you build — Goal, Constraints, Success criteria, Deliverable.
2. **Verify** before you claim done — define criteria, self-review, run tests, paste output.
3. **Use the environment** — `knowledge/`, existing architecture, `lessons-learned.md`.

## Guardrails (read these)

- [`guardrails/always-do.md`](./guardrails/always-do.md)
- [`guardrails/ask-first.md`](./guardrails/ask-first.md)
- [`guardrails/never-do.md`](./guardrails/never-do.md)

## Claude-specific

- Prefer the dedicated file/search tools over shell `cat`/`grep`/`sed`.
- Make independent tool calls in parallel.
- When you make a non-obvious decision, append it to `specs/decisions.md`.
- Do not mark a task complete in `specs/checkpoints.md` until verification passes.

> If anything here conflicts with `AGENTS.md`, `AGENTS.md` wins. If the user's
> direct instructions conflict with either, the user wins.
