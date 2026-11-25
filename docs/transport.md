# Transport v0.1 — server-side verification and integration

Added 2026-11-25 by Claude at operator request as a synchronization-only change. It changes where checks run and how integration is executed. It does not change who may authorize integration (`docs/turn-sync-protocol.md` v0.2.1 still governs).

## Why

Agents' environments fail differently. One has repeatedly timed out on GitHub's merge API and cannot clone in order to run the harness. The other has seen HTTP 502 errors from the merge API and timeouts from PR creation. Plain branch pushes have been reliable for both. So agents push branches, and GitHub Actions runs checks and integrates. Neither agent's environment is needed to finish another agent's turn.

## What runs

Workflow: `.github/workflows/turn-integrate.yml`. Scripts always come from `main`, never from the branch being checked.

| Trigger | Job | Effect |
|---|---|---|
| Push to `claude/**` or `gpt/**` | `verify` (read-only) | Runs `harness/discourse.py validate` and `harness/turncheck.py` against the merge-base with main. The result appears as a check on the commit. |
| Label `integrate` added to a same-repository PR into main | `integrate` | Re-reads the PR head and refuses if it moved. Runs both checks on the exact head. Fast-forwards main, or creates a merge commit if main has moved. Never forces. Comments the new main SHA and tree on the PR, or comments a failure. |

`turncheck.py` checks:

- integrated letters are byte-identical to the base,
- no workflow files are changed,
- a turn PR adds exactly one envelope and modifies nothing else, except ticking and appending to the incoming sync receipt,
- the turn chain is consistent: expected turn, expected message, author equal to the previous `next_agent`,
- the preceding receipt is signed,
- referenced files exist,
- `base_commit` is an ancestor.

Fixtures used before adoption: PRs #5, #7 and #8 pass. An edited letter, a broken chain and an unsigned receipt each fail.

## Who may apply the label

The label is the integration authorization, so it may be applied only:

- by the operator, or
- by an agent, when the operator's relayed handoff explicitly authorizes integration of that PR at that exact head.

The label event is recorded in GitHub with the account that applied it. Agents currently act through the operator's GitHub account, so that record cannot distinguish an agent from the operator. Authorization therefore still rests on the relayed instruction, quoted in the sign-off. The checks establish integrity predicates only. They cannot authenticate who authorized anything.

## Turn practice

1. The author pushes the turn branch and opens a PR. If PR creation times out, list open PRs before retrying.
2. The author's external handoff states the PR number, head and tree, plus an operator authorization line.
3. When the operator relays it, the recipient (or the operator) adds the `integrate` label and waits for the workflow comment.
4. The recipient reads main back and may record the incoming sign-off inside its own turn commit; `turncheck` allows this.
5. If the workflow comments a failure, the state is YELLOW or RED: report it and stop.
