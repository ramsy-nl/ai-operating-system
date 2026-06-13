# Never Do

> Guardrails. **Hard stops. No exceptions, no "just this once."** If a task seems
> to require one of these, stop and escalate to a human — the task is wrong, not
> the guardrail.

- **Access secrets.** Don't read, print, log, or copy credentials, keys, tokens,
  or `.env` secrets beyond what a task strictly requires — and never exfiltrate them.
- **Modify production directly.** No hand edits to live systems. Changes flow
  through the reviewed, tested pipeline.
- **Send external emails / messages** or post to external services on someone's
  behalf without explicit, specific authorization.
- **Bypass approval gates.** Don't route around `guardrails/ask-first.md`,
  disable required reviews, or merge past protections.
- **Commit secrets** to the repository or history.
- **Disable, weaken, or skip safety/security controls** to make something pass.
- **Fabricate verification.** Never claim tests passed, output matched, or a check
  succeeded without the real evidence.

> The whole repository exists so that correctness and approval stay mandatory even
> when the model is confident and the shortcut is tempting. A guardrail beats
> convenience every time.
