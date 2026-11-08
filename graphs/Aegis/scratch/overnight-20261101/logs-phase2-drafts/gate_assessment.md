# Gate assessment DRAFT — Aegis (phase-2 leaf B, 2026-11-01)

DRAFT ONLY. This assessment does NOT write the "[K] Aegis" status line
to any PROGRESS file — that is for the coordinator/parent only, in the
morning, and only if the gates pass. The candidate line is quoted below
once, for identification, with its verdict.

Verdict key: PASS = the condition is met on final evidence. FAIL = the
condition is not met on evidence already in hand. BLOCKED = the
condition cannot be judged yet because a required step has not run or
a required input does not exist. No number below is invented: every
figure cites a file read in phase 1 or phase 2, or is marked TO-VERIFY.

## Gate 1 — Labels: UNRESOLVED 0 / errors 0 / warnings 0 — BLOCKED

- Evidence in hand (history, NOT final): the stage-5 build read
  2,995 methods, 5,466 edges, 0 errors, 0 warnings (AGENT_NOTES.md
  lines 574–579). The stage-1 / stage-5 verdict split was REACHABLE
  2,537 / UNREACHABLE 458.
- Why not PASS: the stage-5 build is not the final build. Round 6/7
  edits followed it, the Stream-C decision edits (D2, D4, D6, D7, R1,
  R2, R5, R6) are described but their presence on the current branch
  is TO-VERIFY, and no final build has run. A final build's error,
  warning, and UNRESOLVED counts are therefore unknown.
- Missing step: full local checkout (blocked on
  `graphs/Aegis/auto_calls.json`, 1,625,494 B per coordinator context,
  over the connector fetch limit; token URL forbidden), apply decision
  edits, run the final build, and print its error/warning/UNRESOLVED
  counts from `build_report.txt`. Until then this gate is BLOCKED,
  not passed — the stage-5 0/0 must not be carried forward as a final
  result.

## Gate 2 — Route checks, including the sample error rate — BLOCKED (with FAIL content on the old sample)

- Evidence in hand (round 7, history, NOT final): sample seed 20261025,
  25 routes; 25 ERROR steps over 12 routes; 13 routes with no ERROR
  step (3 clean, 10 UNCLEAR-only) — AGENT_NOTES.md line 669. Round-7
  route error rate: 12/25 = 48% of sampled routes with at least one
  ERROR step.
- Evidence in hand (steps 6–10 slice, re-derived): GlideRequests.asBitmap
  steps 6–10 CORRECT; Slot.<init> steps 6–10 CORRECT as mechanics with
  step 8 a decision item (now carried as DECISIONS.md R1/D2 treatment:
  UNCLEAR on fresh-declared routes, correct on relaunch-declared
  routes). Neither route is cleared as a whole: GlideRequests has
  round-7 errors at steps 25, 28, 53, 65 (line 652); Slot at steps 21,
  27, 30 (line 655). The other 23 round-7 routes are NOT CHECKED — only
  2 of 25 round-7 dumps are in the repo, confirmed by the steps 6–10
  leaf's fresh listing.
- Why not PASS, and why the old sample also fails on its own terms:
  the round-7 error rate (48% of sampled routes with ERROR steps) is a
  FAIL-level result for that sample, and the structural errors behind
  it (shared relay, state-blind router, saveAndFinish sharing, bind
  producer) are fixed only by the decision edits, which are not yet
  verified as applied. The final sample error rate — the figure this
  gate actually requires — does not exist, because no final sample has
  been drawn and no final route has been read step by step.
- Missing steps: apply decision edits; rebuild; fresh `verify_sample.py`
  draw; fresh `show_route` dumps for every sampled route saved under
  `graphs/Aegis/scratch/`; step-by-step reads with ERROR/UNCLEAR
  verdicts per step and per route; final error rate computed from
  those verdicts. Also still missing: the D7 checked-row print (without
  it the GoogleAuthImporter.readFromApp route stays ERROR) and the
  E4db374dd edge text print. Until then this gate is BLOCKED.

## Gate 3 — Logs complete — FAIL (drafts exist locally; no final log exists)

- `verification.csv`: FAIL — absent from the branch (phase-1 listings
  of `graphs/Aegis/` and `graphs/Aegis/out/`), and no final CSV was
  produced this session because its rows input does not exist (see
  `missing_inputs_report.md`). The tool to produce it
  (`make_verification.py`, local draft in this directory) is
  implemented and self-tested on synthetic data, but has not run on
  real inputs.
- Trigger-graph JSON `verification` object: BLOCKED — whether the branch
  `out/aegis_trigger_graph.json` already carries one is TO-VERIFY (not
  fetched this session); the injector in `make_verification.py` has not
  run. Until it runs, `gen_readme_v2.py` prints "No verification log
  yet".
- `readme_notes.md`: FAIL — branch file's first four headings are all
  "Pending" (fetched in full this session, SHA
  24dd171e34df2d037731985a500cd2c5cab713f8); only Limits is written.
  A five-heading draft exists locally in this directory, with TO-VERIFY
  marks at every final-build/final-sample point.
- `LESSONS.md`: FAIL — absent from the branch. A 7-bullet draft exists
  locally in this directory, each bullet sourced.
- `AGENT_NOTES.md` final entry: FAIL — the branch file's "Final checks"
  section (lines 574–579) is explicitly stage-5 history ("This does not
  mean the Aegis graph is done"). An append-style draft exists locally
  in this directory and must not be appended until the final logs land.
- `out/README.md` (v2): BLOCKED — the branch `out/README.md` (15,314
  bytes, per phase 1) has not been verified as `gen_readme_v2.py` output
  from final inputs (TO-VERIFY); `gen_readme_v2.py` must not be run for
  a final readme until the notes and verification object above exist.
- Overall gate 3 verdict: FAIL, because final logs do not exist — with
  the tool and all four drafts now existing locally as the path to
  closing it once gates 1 and 2 produce their inputs.

## Gate 4 — Eight checks — BLOCKED

- Evidence in hand (history, NOT final): stage-5 check figures only —
  build 0 errors / 0 warnings; check_citations 22 distinct / 0
  problems; check_bytecode_lines 3,654 checked / 0 mismatches; DEAD /
  FRAMEWORK_ONLY grep 0 (AGENT_NOTES.md lines 574–579). Those figures
  describe the stage-5 build, not any final build.
- Why not PASS: no check has run on a final build, because no final
  build exists (Gate 1 blocker). Additionally, the complete eight-check
  inventory itself is TO-VERIFY against the handoff brief — no
  eight-item list is published as confirmed here. Check names grounded
  in files read are: build, check_citations, check_routes,
  check_bytecode_lines, scan_unreachable, verify_sample + show_route
  step checks, and the DEAD / FRAMEWORK_ONLY grep.
- Missing steps: final build, then all eight checks on that build, with
  printed outputs saved; any check that cannot run must be named as not
  run, never marked passed. Until then this gate is BLOCKED.

## Overall: the "[K] Aegis" status line is BLOCKED, not proposed

Candidate line (quoted for identification only, NOT written to any
PROGRESS file by this leaf):

> "[K] Aegis (labels, route checks and logs DONE <date>; device checks
> not started; awaiting user tick)"

Verdict: BLOCKED. All four gates fail to pass: Gate 1 BLOCKED (no final
build), Gate 2 BLOCKED (no final sample; round-7 sample fails at a 48%
route error rate), Gate 3 FAIL (no final verification.csv, readme_notes,
LESSONS, AGENT_NOTES entry, or v2 README), Gate 4 BLOCKED (no final
eight-check outputs; inventory itself TO-VERIFY).

Exact blockers, in order: (1) decision edits applied + verified present
on the branch (D2, D4, D6, D7, R1, R2, R5, R6; D3/D5 constructions
verified); (2) full local checkout + final build (blocked on
`auto_calls.json` fetch limit); (3) final sample + step-by-step route
checks with dumps in the repo + final error rate; (4) D7 checked-row
print + E4db374dd edge text print; (5) rows input + `make_verification.py`
run + `gen_readme_v2.py` run; (6) final readme_notes (four sections +
Limits re-confirmation grep) + final LESSONS + final AGENT_NOTES entry;
(7) final eight-check outputs. Device checks (API 27) remain NOT STARTED
in all cases and are a separate later phase; they do not block the logs
gates, but the status line may only be written once gates 1–4 pass AND
the morning push decision is made by the coordinator/parent.

Progress this session (not a pass): the missing tool now exists as a
tested local draft, all four log drafts exist locally with sources and
TO-VERIFY marks, the `gen_readme_v2.py` aggregation question (checked
excludes unclear) is resolved from the script itself, and the "2 of 25
dumps" figure is confirmed by fresh listing.
