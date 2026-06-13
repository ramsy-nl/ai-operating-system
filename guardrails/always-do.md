---
name: always-do
description: Use before claiming any task complete — the non-negotiable steps required on every unit of work (run tests, update docs, review requirements, checkpoints, self-review, conventional commits).
enforcement: every-task
---

# Always Do

> Guardrails. Non-negotiable steps for **every** task. These are not aspirational
> — they are the minimum bar for calling work done.

- **Run the tests.** Execute them and read the output. "Should pass" is not "passed."
- **Update the docs.** If behaviour or structure changed, the relevant
  `knowledge/` and `specs/` files change with it, in the same unit of work.
- **Review the requirements.** Re-read `specs/requirements.md` before finishing —
  confirm you built what was asked, not what you assumed.
- **Create / update checkpoints.** Break work into reviewable units and keep
  `specs/checkpoints.md` current.
- **Self-review.** Walk `verification/review-checklist.md` before claiming done.
- **Write [Conventional Commits](https://www.conventionalcommits.org).** Every
  commit message is `type(optional-scope): summary` — imperative, ~72 chars or
  less. Types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`,
  `build`, `ci`, `chore`, `revert`. Mark breaking changes with `!` after the
  type/scope (e.g. `feat!:`) or a `BREAKING CHANGE:` footer.
- **Log non-obvious decisions.** Append to `specs/decisions.md` as you make them.
- **Leave the repo smarter.** Capture anything reusable in `knowledge/` and any
  surprise in `knowledge/lessons-learned.md`.

> If you're tempted to skip one of these "just this once," that's exactly the case
> the guardrail exists for.
