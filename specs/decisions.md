# Decision Log

> Layer 1 — Specification. An **append-only** record of non-obvious decisions:
> what was decided, why, and what was rejected. Future agents read this to avoid
> re-litigating settled questions. Never delete an entry — supersede it with a
> new one.

Use one lightweight ADR (Architecture Decision Record) block per decision.

---

## ADR-000 — Adopt the AI Operating System template (example)

- **Date:** 2026-06-13
- **Status:** Accepted
- **Context:** AI-assisted work was failing on unclear goals, unverified
  completion claims, and repeated mistakes across projects.
- **Decision:** Standardise on a three-layer operating model (Specification,
  Verification, Environment) with shared guardrails, inherited by every AI tool
  from a single `AGENTS.md`.
- **Alternatives considered:** Per-tool ad-hoc instructions (drifts out of sync);
  no formal process (status quo, the problem).
- **Consequences:** Every project starts with the same scaffolding; the model
  becomes swappable; some upfront ceremony per task.

---

## ADR-001 — _title_

- **Date:**
- **Status:** Proposed | Accepted | Superseded by ADR-NNN
- **Context:**
- **Decision:**
- **Alternatives considered:**
- **Consequences:**
