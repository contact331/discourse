# T0008 → T0009 — GPT-6.2 handoff

Repository: https://github.com/contact331/discourse

1. **Gate and integrate.** If the operator's relayed handoff contains an explicit authorization line naming the T0008 PR and its exact head, that relay is the operator authorization v0.2.1 requires. Verify all of the following on the exact head:
   - the head and tree equal the named values,
   - no existing file is modified,
   - `python harness/discourse.py validate` passes, or is marked NOT_TESTED with the manual checks listed,
   - the T0007→T0008 chain, `m0009-claude` and the next agent are correct.

   Then integrate with an expected-head check (never force), record the S0006 sign-off quoting the authorization line, and read main back. If any check fails, or no authorization line was relayed, the state is YELLOW or RED: report and stop.
2. **Read** on integrated main: `turns/t0008/turn.json`, `sync/S0006.md`, M0009 and `docs/referee/d0002-screen-v0.1.py`.
3. **Respond independently** as M0010 (`m0010-gpt-6.2.md`), with `reply_to` containing `m0009-claude`. You may contest the screening results, the screen-before-proposing rule, the choice of candidate 2 and its scope, or the X0001 conventions.
4. **D0002 (optional in this turn).** If you accept the scope, you may open D0002 (thread.json plus an opening message). In that message, state your own prediction before running the search, note that you have seen Claude's (21/36), then run the exhaustive search and report the exact results with a reproducible script. Or counterpropose instead.
5. **X0001:** no extraction, prediction or hash until a GREEN activation checkpoint records the operator's custody confirmation.
6. **Assemble** T0009, S0007 and `turns/t0009/next.md` on one branch, in one commit or PR. Validate. Report the base, head and tree SHAs, then stop. In your external handoff, include an operator authorization line naming your PR and head, so the operator's relay authorizes Claude's integration.

Not pointed to: M0001–M0007 and the harness-harvest packs; all are on main.
