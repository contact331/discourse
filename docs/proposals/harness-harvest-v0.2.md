# DISCOURSE — Generalized harness harvest v0.2

Status: research supplement; not adopted, not a correspondence turn. 36 consolidated candidates. Source-derived terminology and proposed DISCOURSE adaptations are distinguished by lineage. Hard = proposed mandatory when applicable; conditional = job/profile selected. No new tests or repository changes are claimed.

## Source checks
- 50 SD15 register rows; 87 Gold terms (20 starred); four Claude residual methods; nine registered v1.1 methods.
- Both supplied ZIPs passed CRC checks. All 14 Claude manifest payloads matched declared byte counts and SHA-256.
- Earlier cumulative log is exact byte prefix of later log. Do not count both histories as independent evidence.
- Source archives include private material; no raw extracts copied into this report.

## Identity and authority

| ID | Mechanism | Source lineage | Activation / profile | Contract | Acceptance fixture |
|---|---|---|---|---|---|
| H001 | Source pinning | D01; Artifact Engine run suite | hard / core | Exact source version and digest; conflicting equal authority stays unresolved | Reject stale or ambiguous authoritative input |
| H002 | Precedence map / WinnerMap | D01; Gold O | hard / core | Record decision, scope and competing sources; do not silently settle ties | Two equally ranked contradictory sources remain open |
| H003 | Lexicon lock and alias map | D06; Gold R | conditional / core | Version scoped terms and aliases; detect semantic changes, not just renames | Rename passes; semantic drift fails |
| H004 | Canonical / derived separation | D08; D47 | hard / core | Projections cite original source and transformation; repetition confers no authority | Repeated stale projection does not supersede source |
| H005 | Inference and authority typing | D02; D47; CL02 | hard / core | Differentiate explicit requirement, assumption, open decision, observation | Inferred default cannot acquire authority |
| H006 | Typed bindings and joins | D05; D34 | conditional / research | Pin identity, cardinality, meaning, units and prerequisites | Detect missing keys, fan-out and changed units |

## Context and continuity

| ID | Mechanism | Source lineage | Activation / profile | Contract | Acceptance fixture |
|---|---|---|---|---|---|
| H007 | Context packing | D07; D46; Gold R | conditional / core | Role-relevant source references, read order, budget and omissions; raw source preserved | Cold reader recovers critical facts without stale copies |
| H008 | Continuation snapshot | D49; D38 | hard / core | Pin current inputs, accepted decisions, remaining uncertainty and next step | Fresh session catches superseded assumption |
| H009 | Checkpoint and resume | D38; Gold X; run suite | hard / core | Preserve last-good outputs; repeat safely | Interrupt and resume without duplicates |
| H010 | Run fingerprint | D37; Gold X; run suite | conditional / core | Record input/output hashes, method versions and relevant environment | Detect changed input or verifier; replay deterministic component |
| H011 | Scoped compaction | D07; D46; Gold M | conditional / core | Derived summaries and indexes reference exact originals; no destructive replacement | Rebuild projection after source change |
| H012 | Receipt invalidation | D27; run suite exact-attempt binding | hard / core | Scope receipt to exact inputs/output/check version; mark affected receipts stale | Relevant change invalidates; unrelated edit does not |

## Orchestration and synchronization

| ID | Mechanism | Source lineage | Activation / profile | Contract | Acceptance fixture |
|---|---|---|---|---|---|
| H013 | Disjoint lane ownership | D42; Gold O | conditional / core | Assign write boundaries, pinned common base, conflict resolution | Detect overlapping edits before integration |
| H014 | Atomic turn envelope | D42; D49; proposed adaptation | hard / correspondence | Commit message, envelope, next prompt and applicable sync record together | Missing referenced file blocks integration |
| H015 | Work queue lease | Gold O; CP0 Job | conditional / automation | Lease only when multiple workers can claim same task; expiry and recovery | Two workers cannot accept same task |
| H016 | Idempotent submission | D38; run suite | hard / core | Logical attempt ID and exact payload deduplication | Retry after timeout cannot duplicate turn |
| H017 | Detached handoff manifest | Artifact Engine R0 standards F5; D49 | hard / core | Generate after push; verify remote branch head; avoid SHA self-reference | Deliberately stale handoff detected |
| H018 | Failure classification and reconciliation | D40; D50; Gold V/O | hard / core | Transient, missing evidence, unsupported method, substantive failure, disputed judgment | Transient retry bounded; failed invariant never becomes pass by retry |
| H019 | Explicit acknowledgement boundary | D44; Gold G; proposed adaptation | hard / correspondence | Separate operator synchronization, merge authorization and intellectual agreement | Agent cannot self-certify operator receipt |
| H020 | Bounded retry / degraded mode | D38; D50; Gold X/O | hard / core | After ambiguous effect inspect remote state; retry with limit; safe fallback | Simulated timeout after commit discovers actual state |

## Verification and evaluation

| ID | Mechanism | Source lineage | Activation / profile | Contract | Acceptance fixture |
|---|---|---|---|---|---|
| H021 | Resolution → conformance → exercised-path proof | D04; D21; D36 | hard / core | Separate address, definition, binding, actual execution and independent review | Schema-valid disconnected path fails exercised-path claim |
| H022 | Adversarial controls | D19; registered method | conditional / core | Plausible bad case and strong clean control; boundary cases as needed | Reject persuasive error; accept valid variation |
| H023 | Changed surface and regression | D20; D41 | hard / core | Check touched surfaces and unaffected invariants; preserve restorable baseline | Catch unauthorized change without blocking valid representation change |
| H024 | Independent review | D26; run suite | conditional / research | Separate session inspects exact pinned evidence; state trust limitations | Recover same bytes, distinguish local attribution from trusted receipt |
| H025 | Claim–evidence and non-claims | D03; CL04; registered methods | conditional / research | Bind consequential claims to exact evidence/falsifier; check stated scope | Detect overclaim in summary despite correct arithmetic |
| H026 | Expert-expectation gap audit | CL03 | conditional / research | Reviewer identifies consequential missing evidence with justification | Detect planted omission; accept defensible alternative |
| H027 | Worked examples / anchored rubric | CL01; Gold V | conditional / batch | Two or three examples, small job-selected checklist; held-out controls separate | Matched review improves detection without raising false rejects |
| H028 | Blind and held-out comparison | D30; D29 | conditional / research | Freeze source, equal budget, predeclare rubric; independently sealed results | Compare without prior access; retain disagreement |

## Governance, telemetry and learning

| ID | Mechanism | Source lineage | Activation / profile | Contract | Acceptance fixture |
|---|---|---|---|---|---|
| H029 | Evidence / state / authority separation | D35; CP0 policy | hard / core | Measurements cannot authorize release; approvals scoped to action | Self-authored attractive metric cannot promote state |
| H030 | Privacy partition and untrusted content | D47; Gold G; CP0 policy | hard / core | Imported text is evidence, not instruction; access/rights checked before transfer | Private source cannot be exported by hash match |
| H031 | Event catalogue versus observed records | D33; AngelNet catalogue | hard / core | Separate event type registry, actual emitted events and writer health | Empty log or disconnected writer yields unknown, not success |
| H032 | Metric contract | D32; D13 | conditional / automation | Unit, formula, denominator, window, source, missing-data behavior | Empty denominator yields unknown |
| H033 | Incident-to-regression / lessons register | D28; D40; Gold F | conditional / core | Failure, cause hypothesis, fix, clean control and transfer evidence; retire if invalid | Reproduce failure, pass fix, test on another work item |
| H034 | Method ROI and retirement | D29; Gold F | conditional / research | Compare quality, time, interventions and cost under matched conditions | Retain only net-beneficial scoped methods |
| H035 | Conditional profiles / minimal infrastructure | D45; D48; CP0 policy | hard / core | Select only applicable gates; avoid resident infrastructure until need measured | Small dialogue remains operable without unrelated gates |
| H036 | Version compatibility and migration | D39 | conditional / core | Additive versioned contracts or explicit migration; preserve originals | Old packet opens or yields recoverable incompatibility |

## Pilot order

P0: H001, H002, H004, H008, H012, H014, H016–H020, H021, H023, H029–H031, H035. Select only those necessary for an integrated correspondence turn. P1: optional discovery and research checks. P2: concurrent relay/automation only after measured need.

## Current failure fixture

A PR merge times out. Fetch remote head and PR state before retrying. If already integrated, verify expected tree and close integration; if still pending, bounded retry or delegated integration; if head diverged, stop. Never infer failure solely from a timeout or record operator acknowledgement without explicit authorization. Distinguish valid branch from integrated main.

## Exclusions

No wholesale adoption of the 87 Gold terms, no 6,500-event target, no inferred Bench uplift, no auto-launch, no actual private-source transfers. The pilot must demonstrate benefit against ordinary operation with comparable inputs and budget.
