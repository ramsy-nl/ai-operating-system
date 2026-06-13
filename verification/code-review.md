# Code Review

> Layer 2 — Verification. How to **request** review of your work and how to
> **receive** review of it. Self-review (`review-checklist.md`) comes first; this
> is the second pair of eyes — human or agent.
>
> Based on the requesting-code-review and receiving-code-review skills from
> [Superpowers](https://github.com/obra/superpowers).

## Severity levels

Review findings are graded so everyone knows what blocks a merge and what
doesn't. Don't treat every comment as equal.

| Severity | Meaning | Blocks merge? |
|----------|---------|---------------|
| **Critical** | Correctness, security, or data-loss defect; violates a guardrail. | Yes — must fix. |
| **Major** | Wrong behaviour in a real case, missing requirement, no test for risky code. | Yes — fix or get explicit waiver. |
| **Minor** | Style, naming, small clarity or maintainability nit. | No — fix if cheap, else log. |
| **Question** | Reviewer needs to understand intent before judging. | No — answer it. |

A review with no Critical or Major findings, against the agreed plan, is a pass.

---

## Requesting review

You are asking someone to check your work, not to bless it. Make that cheap for them.

- **Review against the plan.** Point the reviewer at the requirement / checkpoint
  this implements (`specs/checkpoints.md`) so they judge it against intent, not vibes.
- **State what you verified.** Which tests run, what output, which evaluation
  criteria pass. Paste the evidence.
- **Flag your own risks.** Call out the parts you're least sure about and the
  decisions you made (`specs/decisions.md`). Honesty here gets you better review.
- **Keep it small.** A checkpoint-sized diff gets a real review; a giant one gets
  a rubber stamp.

### Prompt

```
Review CP-N against specs/checkpoints.md and specs/requirements.md.
Grade each finding Critical / Major / Minor / Question.
I have run: <tests + output>. I'm least sure about: <X>.
Block me on anything Critical or Major.
```

---

## Receiving review

Feedback is a technical claim to evaluate, **not** a verdict to obey or resist.

- **Don't perform agreement.** "Great catch, fixing now!" before you've understood
  the point is noise. Understand first.
- **Don't blindly implement.** If a suggestion seems wrong, verify it. The
  reviewer can be mistaken; so can you. Resolve it with evidence, not deference.
- **Don't get defensive.** A Critical finding is a gift — it found the bug before
  production did.
- **Triage by severity.** Fix Critical/Major before merge. For Minor, fix if
  cheap or log it. For Questions, answer them.
- **Verify the fix.** A change made in response to review still needs its own
  test and evidence. Re-run `review-checklist.md`.

### Prompt

```
For each review finding: restate it in my own words, decide if I agree (with a
reason), and either fix-with-a-test or push back with evidence. Resolve all
Critical/Major before claiming done. No performative agreement.
```

> The goal of review is correct software, not a comfortable conversation. Rigor on
> both sides.
