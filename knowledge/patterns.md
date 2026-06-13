# Patterns

> Layer 3 — Environment. The reusable, blessed ways of doing things in this
> project. When a problem matches a pattern here, use the pattern — don't invent
> a new one. When you invent something worth reusing, add it here.

## How to read this

Each pattern states **when** to use it, **how**, and **when not** to. A pattern
without a "when not to" is a trap.

---

## Pattern template

### P-NNN — _name_

- **Problem it solves:**
- **When to use:**
- **How:**
  ```
  // minimal canonical example
  ```
- **When *not* to use / anti-pattern:**
- **Related:** _decisions, other patterns_

---

## Starter conventions (replace with this project's reality)

- **Naming:** match the surrounding code; consistency beats personal preference.
- **Errors:** fail loud, fail early; never swallow exceptions silently.
- **Configuration:** no hard-coded secrets — read from the environment.
- **Side effects:** isolate them; keep the core logic pure and testable.
- **Tests:** every pattern ships with an example of how it's tested.
