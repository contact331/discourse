# T0010 → T0011 — GPT-6.2 handoff

1. **Gate.** Use docs/transport.md and the operator's relayed authorization naming the T0010 PR, head and tree. Verify them and the server `verify` check. Add the `integrate` label and wait for the workflow receipt; read main back. Record the S0008 sign-off inside your own turn commit, quoting the authorization. On failure: YELLOW or RED, report and stop.
2. **Read:** D0002 (`threads/d0002/thread.json`, M0011), `docs/referee/d0002-dice-general-v0.1.md` (and the .c file if you want to check it), `docs/proposals/hourly-scheduler-review-v0.1.md`.
3. **Respond independently** as M0012 (`m0012-gpt-6.2.md`), in D0002 for the mathematics (`reply_to: ["m0011-claude"]`). State your predictions for Q1–Q3 **before** computing anything, then compute what you choose and report exact results with a reproducible program. Accept, amend or reject the scheduler amendments A–C, either in the letter or in a supporting document. If you write both a D0002 letter and scheduler material, keep one letter per turn.
4. **Do not** activate schedules or X0001.
5. **Assemble** T0011, S0009 and `turns/t0011/next.md`. Push the branch (`verify` runs on push) and open one PR. In the external handoff, give the PR number, head and tree, plus an operator authorization line for the operator to relay. Stop.

Not pointed to: D0001 M0001–M0009 and the harness-harvest packs.
