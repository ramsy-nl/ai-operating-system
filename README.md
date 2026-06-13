# AI Operating System

A reusable repository template that gives every project the same **operating
model** for AI-assisted work. The model (Claude, Cursor, Copilot, Codex, or
whatever comes next) is an interchangeable execution engine. This repository is
the institutional knowledge and workflow that stays constant around it.

## Why this exists

Most AI-assisted work fails in predictable ways: the agent builds the wrong
thing because the goal was never pinned down, claims completion without
verifying, and re-learns lessons the team already paid for. This template fixes
that with three layers that every agent follows:

| Layer | Question it answers | Where it lives |
|-------|---------------------|----------------|
| **1. Specification** | Are we building the right thing? | `specs/` |
| **2. Verification** | Did we actually build it correctly? | `verification/` |
| **3. Environment** | What do we already know? | `knowledge/` |

Around those, **guardrails** govern what an agent may do on its own, and
**prompts** provide the reusable phases of a unit of work.

## Single source of truth

[`AGENTS.md`](./AGENTS.md) defines the operating model. Every tool-specific file
inherits from it:

- `CLAUDE.md` → Claude Code
- `.cursor/rules/operating-model.mdc` → Cursor
- `.github/copilot-instructions.md` → GitHub Copilot

Edit the model in `AGENTS.md`. The tool files just point back to it, so the rules
never drift between tools.

## Structure

```
.
├── AGENTS.md                      # The operating model (source of truth)
├── CLAUDE.md                      # Claude inherits AGENTS.md
├── README.md
│
├── .claude/                       # Claude-specific config
├── .cursor/rules/                 # Cursor inherits AGENTS.md
├── .github/copilot-instructions.md# Copilot inherits AGENTS.md
│
├── specs/                         # Layer 1 — what & why
│   ├── project-goal.md
│   ├── requirements.md
│   ├── decisions.md               # Decision log (append-only)
│   ├── checkpoints.md             # Small, reviewable units of work
│   └── project-spec-template.md   # Copy this to kick off a project
│
├── verification/                  # Layer 2 — did we build it right
│   ├── evaluation-criteria.md
│   ├── review-checklist.md        # Self-review before claiming done
│   ├── code-review.md             # Requesting & receiving review (severity-based)
│   ├── test-plan.md               # Test-first (RED-GREEN-REFACTOR)
│   └── examples/                  # Known-good reference outputs
│
├── knowledge/                     # Layer 3 — what we already know
│   ├── architecture.md
│   ├── lessons-learned.md
│   ├── patterns.md
│   └── glossary.md
│
├── guardrails/                    # What an agent may do autonomously
│   ├── always-do.md
│   ├── ask-first.md
│   ├── never-do.md
│   └── red-flags.md               # "Thoughts that mean STOP" self-checks
│
└── prompts/                       # Reusable phases of work
    ├── discovery.md
    ├── planning.md
    ├── implementation.md          # Test-first
    ├── review.md
    └── debugging.md               # Root cause before fix
```

## How to use it

1. **Start a project** — copy `specs/project-spec-template.md` into
   `specs/project-goal.md` and fill it in. Don't skip the Constraints and
   Verification sections.
2. **Plan** — break the goal into `specs/checkpoints.md`. Each checkpoint is
   independently reviewable.
3. **Build** — work one checkpoint at a time, test-first. Follow `guardrails/`.
   Log non-obvious choices in `specs/decisions.md`. Commit with
   [Conventional Commits](https://www.conventionalcommits.org)
   (`type(scope): summary`).
4. **Verify** — before marking anything done, run `verification/review-checklist.md`
   and the `test-plan.md`. Paste real output.
5. **Capture** — record anything reusable in `knowledge/`. Leave the repo
   smarter than you found it.

Each phase in `prompts/` carries `when-to-use` frontmatter (`name`,
`description`, `phase`), so a skills-aware harness can select the right phase
automatically — and a human can scan them at a glance.

## Adopting it in a new project

Copy this repository's structure into the new project (or start the new project
from this template). The model files at the root are picked up automatically by
each tool. Replace the placeholder content in `specs/` and `knowledge/` with the
specifics of that project; keep `guardrails/`, `verification/`, and `prompts/`
as your baseline and tighten them as you learn.

## Credits

The core disciplines — test-first (RED-GREEN-REFACTOR), root-cause debugging,
severity-based code review, evidence over claims, and the red-flag self-checks —
are adapted from Jesse Vincent's
[Superpowers](https://github.com/obra/superpowers). Superpowers is an
*executable* auto-activating skills system; this repository is the *documented*
operating model that any tool can follow. The two compose: with the Superpowers
skills installed, they enforce at runtime what these files describe.

Licensed under [MIT](./LICENSE).
