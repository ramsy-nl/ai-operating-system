# Evaluation Criteria

> Layer 2 — Verification. Define these **before** building, not after. They turn
> "looks good" into a pass/fail judgement. Every success criterion in
> `specs/project-goal.md` should map to one or more criteria here.

## How to write a good criterion

A good criterion is **observable** and **binary**: someone other than the author
can check it and get the same answer. "Fast" is not a criterion; "p95 response
under 200ms on the test dataset" is.

## Criteria

| ID | Criterion | Measures (requirement) | Threshold / definition of pass |
|----|-----------|------------------------|--------------------------------|
| E1 | _what we check_ | R1 | _what counts as passing_ |
| E2 |           | R2 |                                |

## Dimensions to consider

- **Correctness** — does it produce the right output for known inputs?
- **Completeness** — are all in-scope requirements covered?
- **Robustness** — does it handle edge cases, bad input, and failure modes?
- **Performance** — within the stated constraints?
- **Security & privacy** — no secrets leaked, least privilege, input validated?
- **Maintainability** — would the next person understand and safely change it?
- **Fidelity to spec** — does it match `requirements.md`, not a reinterpretation?

## Scoring

For subjective outputs, score each criterion (e.g. 0–2: fail / partial / pass)
and set a minimum total to ship. For deterministic outputs, every criterion must
pass. Record the result in the checkpoint before marking it `Done`.
