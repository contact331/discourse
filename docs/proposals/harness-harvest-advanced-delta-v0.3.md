# DISCOURSE — Advanced harness harvest delta v0.3

Auxiliary research, not adopted. Extends H001–H036 with 24 candidate entries and refinements; overlap is explicitly recorded. No correspondence turn, experiment or repository mutation. Source material is generalized; private records are not reproduced. No tests rerun or gain measured in this pass.

## Register

| ID | Method | Source lineage | Evidence status | Related v0.2 |
|---|---|---|---|---|
| H037 | Rival-model discrimination | D10; v1.1 rival_models | registered evidence contract | H025 |
| H038 | Elimination and ablation | D11; v1.1 rival_models optional elimination; parallel review provenance correction | source-inspired adaptation | H022 H033 |
| H039 | Assumption sensitivity thresholds | D12 | proposed | H025 |
| H040 | Analogical transfer mapping | D14; v1.1 semantic_transfer | registered evidence contract | H028 |
| H041 | Orthogonal numerical verification | D15; v1.1 quantitative_check | registered evidence contract | H022 H025 |
| H042 | Forecast resolution discipline | D16 | conditional proposal | H001 H032 |
| H043 | Decisive-observation selection | D18 | proposed | H025 |
| H044 | Cross-representation semantic fidelity | D22 | proposed | H023 H025 |
| H045 | Alternative interpretation prototyping | D23 | conditional proposal | H028 |
| H046 | Hypothesis workbench | D24; parallel review says agent-proposed with source analogues | agent-proposed adaptation | H005 H025 |
| H047 | Best-of-N and candidate selection | Gold I; Claude findings B-C | untested named method | H028 H034 |
| H048 | Self-consistency and independent disagreement | Gold I; Claude findings G warns of false matches | untested named method | H024 H025 |
| H049 | Quality-diversity search | Gold I: novelty search and MAP-Elites | untested named method | H028 |
| H050 | Bounded branching / debate | Gold I: tree of thoughts and multi-agent debate | untested named method | H024 H028 |
| H051 | Critique and revise | Gold V: self-refine/reflexion | untested named method | H023 H034 |
| H052 | Four-arm harness evaluation | Build docs/sd15plus/BENCHMARK_BATTERY.md | documented experimental design | H028 H034 |
| H053 | Rule scope, expiry and counterexamples | Build docs/sd15plus/SCOPE_ANTI_STRANGULATION.md; harness/rules.json; harness/check.py | partial implementation | H029 H035 |
| H054 | Suppressed-path and scope ablation | Build docs/sd15plus/SCOPE_ANTI_STRANGULATION.md; BENCHMARK_BATTERY.md | documented experimental design | H028 H034 H053 |
| H055 | Model routing under matched budget | Gold K | untested named method | H034 H035 |
| H056 | Proof of harness adoption | Build backend/artifact_run_usage.py | implemented local aggregation | H021 H031 H032 |
| H057 | Structure-aware corpus screening | Claude package tools/screen_corpus.py; 01_FINDINGS.md | implemented heuristic scanner; ranking improvements proposed | H007 H011 |
| H058 | Near-duplicate retrieval with source lineage | Claude package tools/screen_corpus.py | implemented heuristic scanner | H001 H004 |
| H059 | Independent gold-set and miss audit | Claude package 01_FINDINGS.md A3, B; 04_PROCESS_UPGRADES.csv | reported evaluation; improvement proposed | H028 H032 H057 |
| H060 | Lineage versus semantic support | SD15_V1_1_CLAUDE_PARALLEL_REVIEW.md; Claude package 03_GPT_REGISTER_QC.csv | reviewed provenance distinction | H001 H005 H025 |

## Activation and acceptance
### H037 — Rival-model discrimination
Compare plausible models and their distinct predictions; preserve inconclusive cases.
**Acceptance candidate:** Paired indistinguishable/discriminating cases produce justified abstention and correct discrimination.

### H038 — Elimination and ablation
Change one suspected cause; use a placebo and reproduce the original defect.
**Acceptance candidate:** Only targeted change removes the reproducible defect; placebo does not.

### H039 — Assumption sensitivity thresholds
Vary decision-driving assumptions within justified ranges and locate decision boundaries.
**Acceptance candidate:** A sign-changing case is qualified; a stable case reports tested range.

### H040 — Analogical transfer mapping
Bind source-target relationships, invariants, exceptions and tests.
**Acceptance candidate:** Held-out changed-domain case preserves invariant and rejects a false analogy.

### H041 — Orthogonal numerical verification
Use independent calculation, units or solved limit rather than duplicating assumptions.
**Acceptance candidate:** Detect shared-denominator error; accept a valid control.

### H042 — Forecast resolution discipline
Freeze issue time, input cutoff, horizon, resolution source and comparator.
**Acceptance candidate:** Late source excluded; unresolved stays unknown; resolved scores reproducible.

### H043 — Decisive-observation selection
Record conflicting or unknown evidence and the observation that would change a conclusion.
**Acceptance candidate:** New evidence updates only the claims it resolves.

### H044 — Cross-representation semantic fidelity
Check equivalent claims across figures, prose, data and machine outputs.
**Acceptance candidate:** Wrong denominator or changed conclusion is detected while valid alternate layout passes.

### H045 — Alternative interpretation prototyping
Develop two genuinely different treatments; allow rejection of both.
**Acceptance candidate:** Blind reader recovers intended meaning and distinguishes usable alternatives.

### H046 — Hypothesis workbench
Keep speculative objects distinct from factual claims and promotion criteria.
**Acceptance candidate:** Novel hypothesis can be explored; invented observation cannot enter supported results.

### H047 — Best-of-N and candidate selection
Compare multiple candidates against an explicit rubric and cost budget.
**Acceptance candidate:** Matched total resources; improvement over one stronger attempt must be measured.

### H048 — Self-consistency and independent disagreement
Compare multiple answers without treating agreement as proof.
**Acceptance candidate:** Include common-mode wrong consensus and valid minority answer.

### H049 — Quality-diversity search
Maintain distinct viable solution niches rather than only one highest score.
**Acceptance candidate:** Matched budget yields useful alternatives without degrading accepted quality.

### H050 — Bounded branching / debate
Compare independently developed alternatives with explicit evidence and bounded branches.
**Acceptance candidate:** Blind evaluation measures correction, costs and shared errors; dissent retained.

### H051 — Critique and revise
Revise a candidate against a specific rubric with an explicit stopping condition.
**Acceptance candidate:** Compare error correction and regression against equal-resource baseline.

### H052 — Four-arm harness evaluation
Compare native, shadow, guided and release-guarded modes at matched resources.
**Acceptance candidate:** Retain blinded ratings, human rescues, costs, failures and baseline non-regression.

### H053 — Rule scope, expiry and counterexamples
Each restrictive rule has owner, scope, purpose, severity, review/expiry, counterexample and override.
**Acceptance candidate:** Expired project-specific restrictions not silently inherited; soft rule cannot become hard block.

### H054 — Suppressed-path and scope ablation
Ask what valid solution a rule forbids; compare with/without the disputed rule.
**Acceptance candidate:** Seed known viable paths and measure missed approaches and false stops.

### H055 — Model routing under matched budget
Allocate inexpensive methods/models to suitable tasks and escalate when justified.
**Acceptance candidate:** Measure cost per accepted output and error rates; escalate difficult cases.

### H056 — Proof of harness adoption
Distinguish declared methods, submitted evidence, linked run IDs and review closure.
**Acceptance candidate:** Compare linked and unlinked artifact commits; empty denominator stays unknown.

### H057 — Structure-aware corpus screening
Shortlist by structure, method terms, mechanism coverage and per-file caps.
**Acceptance candidate:** Report unbiased held-out recall, missed leads and candidate reading workload.

### H058 — Near-duplicate retrieval with source lineage
Keep occurrence pointers when removing normalized exact or MinHash near duplicates from search shortlist.
**Acceptance candidate:** Same content at two locators remains traceable; distinct meaning not silently discarded.

### H059 — Independent gold-set and miss audit
Separate boosted screening from unboosted recall and audit false negatives on held-out material.
**Acceptance candidate:** Report recall@k and denominator without using the test anchors to tune retrieval.

### H060 — Lineage versus semantic support
Record exact source anchor, whether it supports the principle/procedure, and agent-added adaptation.
**Acceptance candidate:** Correctly locate but reject a passage that does not support the attributed method.

## Integration recommendation

Keep correspondence minimal; sort into validator, authority, profile or derived view. Activate reasoning recipes only for matching tasks. Benchmark native vs shadow vs guided vs release-guarded modes before enforcement. No score inflation or assumption that named Gold methods are implemented. The existing X0001 blind-harvest experiment remains separate; no extraction was generated, committed or inspected.

The JSON companion carries the same register. Source paths are references to the uploaded packages, not claims of independent external verification.
