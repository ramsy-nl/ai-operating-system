# Glossary

> Layer 3 — Environment. Shared vocabulary so humans and agents mean the same
> thing by the same word. Ambiguous terms cause ambiguous code.

## Project terms
_Domain language specific to this project._

| Term | Definition | Notes / not to be confused with |
|------|------------|---------------------------------|
|      |            |                                 |

## Operating System terms
_Vocabulary of this template itself._

| Term | Definition |
|------|------------|
| **Operating model** | The three-layer process (Specification, Verification, Environment) every agent follows. Defined in `AGENTS.md`. |
| **Checkpoint** | A small, independently reviewable and shippable unit of work. See `specs/checkpoints.md`. |
| **Guardrail** | A rule constraining what an agent may do autonomously: always-do, ask-first, or never-do. |
| **Approval gate** | A point where work must stop for explicit human sign-off. |
| **Evaluation criterion** | An observable, binary check that defines "correct" for an output. |
| **ADR** | Architecture Decision Record — one logged decision in `specs/decisions.md`. |
| **Golden output** | A known-correct reference result used for comparison, stored in `verification/examples/`. |
