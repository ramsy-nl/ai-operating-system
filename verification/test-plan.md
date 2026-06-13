# Test Plan

> Layer 2 — Verification. How the deliverable is tested. Tie every test back to a
> requirement (`specs/requirements.md`) or evaluation criterion
> (`verification/evaluation-criteria.md`).

## Test strategy

| Level | What it covers | When it runs |
|-------|----------------|--------------|
| Unit | Individual functions / units in isolation | On every change |
| Integration | Units working together, real boundaries | Before merge |
| End-to-end | Full user-facing flow | Before release |
| Manual / exploratory | Things automation can't yet catch | Per checkpoint |

## Test cases

| ID | Verifies | Input / setup | Expected result | Status |
|----|----------|---------------|-----------------|--------|
| T1 | R1 / E1 |               |                 | Todo   |
| T2 | R2 / E2 |               |                 | Todo   |

## Edge cases & failure modes
_Enumerate the nasty ones deliberately — they are where bugs hide._
- Empty / missing input:
- Maximum size / volume:
- Malformed input:
- Concurrent access:
- Dependency unavailable / times out:

## How to run

```bash
# Replace with this project's commands.
# e.g. npm test, pytest, go test ./...
```

## Evidence

When reporting results, paste the **actual** command output (pass and fail
counts, any failures). A claim of "tests pass" without the output does not
satisfy Layer 2.
