# Ask First

> Guardrails. **Stop and get explicit human approval** before doing any of these.
> These are reversible-but-consequential or hard-to-undo actions. Approval in one
> context does not extend to the next — ask each time.

- **Spend money.** Provisioning paid resources, calling paid APIs at volume,
  anything that shows up on a bill.
- **Delete data.** Dropping tables, removing files you didn't create, purging
  records, destructive migrations.
- **Change infrastructure.** Modifying cloud resources, networking, IAM, CI/CD
  configuration, deployment topology.
- **Merge to main.** Or to any protected/shared branch.
- **Install new dependencies** or upgrade major versions.
- **Change a public interface / API contract** other systems rely on.
- **Anything matching a checkpoint's "approval gate"** in `specs/checkpoints.md`.

## How to ask

State plainly: *what* you intend to do, *why*, what the *blast radius* is, and how
to *undo* it. Then wait for an explicit yes. Do not proceed on silence or a vague
"sounds good" for irreversible actions.
