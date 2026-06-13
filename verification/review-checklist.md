# Review Checklist

> Layer 2 — Verification. Run this self-review before claiming a checkpoint is
> done and before requesting human review. Don't tick a box you haven't actually
> checked.

## Specification fidelity
- [ ] Output matches the requirement it implements (`specs/requirements.md`), not a reinterpretation.
- [ ] Nothing out-of-scope was added (`specs/project-goal.md` → Out of scope).
- [ ] Non-obvious decisions are logged in `specs/decisions.md`.

## Correctness
- [ ] Works for the normal/expected case.
- [ ] Handles edge cases: empty, large, malformed, concurrent, boundary values.
- [ ] Error paths fail loudly and safely — no silent swallow.
- [ ] No off-by-one, no incorrect assumptions about data shape.

## Verification evidence
- [ ] Tests written and passing — **actual output pasted**, not summarised.
- [ ] Evaluation criteria (`evaluation-criteria.md`) all pass.
- [ ] Compared against reference examples in `verification/examples/` where applicable.

## Safety & guardrails
- [ ] No secrets, keys, or tokens in code, logs, or commits.
- [ ] No action from `guardrails/never-do.md` was taken.
- [ ] Anything from `guardrails/ask-first.md` was explicitly approved.
- [ ] Inputs validated; least-privilege respected.

## Quality
- [ ] Reads like the surrounding code — naming, style, idioms match.
- [ ] No dead code, no leftover debug output, no commented-out blocks.
- [ ] Public behaviour and any gotchas are documented.

## Environment / handoff
- [ ] `knowledge/` updated if anything reusable was learned.
- [ ] `lessons-learned.md` updated if a mistake or surprise occurred.
- [ ] Checkpoint status updated in `specs/checkpoints.md`.

> If any box can't be honestly ticked, the work is not done. Say so plainly and
> report what's outstanding.
