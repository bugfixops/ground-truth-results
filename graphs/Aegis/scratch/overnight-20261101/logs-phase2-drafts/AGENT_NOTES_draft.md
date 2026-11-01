# DRAFT AGENT_NOTES update — Aegis (phase-2 leaf B, 2026-11-01)

APPEND-STYLE DRAFT ONLY. This is NOT the branch
`graphs/Aegis/AGENT_NOTES.md` (670 lines, SHA
ff62d457ca067aa0153295821a2e985eb471a3e4, per phase 1). It is the text
to APPEND to that file when the final logs land — after the final build,
the final sample, and the final checks exist. Do NOT append it yet: it
records drafts and blockers, not finished work, and several of its
sentences are only true once the steps they describe have run. No
tick-box mark is written anywhere in this draft. Nothing here counts as
a merge verdict.

---

## Logs phase 2 (drafts, 2026-11-01; final logs NOT produced)

Inputs used: stream-C `logs_gap.md` (phase-1 gap analysis),
`DECISIONS.md` (7 decisions D1–D7 plus related decisions R1–R8, recorded
as Muse's own decisions for user/Yang review — none in anyone else's
name), and `steps6-10_report.md` (GlideRequests steps 6–10 CORRECT; Slot
steps 6–10 mechanics CORRECT with step 8 a decision item; 23 round-7
routes NOT CHECKED). Branch reads via the GitHub connector only, one
file at a time, ~30 s pauses, no token used/waited for/written anywhere,
no 429 hit this session. No push, no branch edit, no device work.

What was verified from the script itself this session:
`tools/gen_readme_v2.py` (140 lines, SHA
15337a8675cde3a08fe8722b238764a577e8303c) reads verification counts
only from the trigger-graph JSON's `verification` object and prints Rows
as `checked + unclear` per type. Consequence, now confirmed rather than
open: the JSON `checked` field must EXCLUDE unclear rows (checked =
correct + errors_found), or the published Rows figure double-counts.
`make_verification.py` (new local tool, see below) enforces this.

What was produced (LOCAL drafts in
`~/workspace/overnight/stream-C/logs_phase2/`, NOT on the branch):
- `make_verification.py` — NEW LOCAL tool (not a branch file). Emits
  `verification.csv` with the exact header
  `type,item,result,confirmed_by,ref,edges,note` for row types label /
  edge / path, rejects any `confirmed_by` other than SOURCE or INFERRED
  (never DYN, FW-MEMORY, UNVERIFIED), and injects the `verification`
  object (all three types, `checked`/`correct`/`errors_found`/`unclear`)
  into the schema-2 trigger-graph JSON. Self-tested on synthetic data
  only (compile OK; 6-row synthetic run aggregated correctly; UNVERIFIED
  rejection exits 1 and writes nothing). It has NOT been run on real
  Aegis inputs, because those inputs do not exist yet (see blockers).
- `missing_inputs_report.md` — precise missing-inputs list (final
  build, final sample + dumps, rows input, D7 print, E4db374dd print,
  eight-check outputs) plus the draft outline for the final CSV.
- `readme_notes_draft.md` — five headings in order, from the phase-1
  drafts + decisions + steps verdicts, with TO-VERIFY marks wherever
  the sample/checks are missing. The branch Limits text is carried
  verbatim, with a DRAFT dated addendum (batch-36 "96 errors" figure
  superseded by the stage-5 build; re-confirmation grep still to run).
- `LESSONS_draft.md` — 7 bullets, each with its source. Lesson 7's
  "2 of 25 dumps" figure is now CONFIRMED by the steps 6–10 leaf's fresh
  directory listing (was TO-VERIFY in phase 1).
- `gate_assessment.md` — gate-by-gate PASS / FAIL / BLOCKED assessment.
  Headline: the "[K] Aegis" status line is BLOCKED, not proposed (see
  that file for the exact blockers). This draft does NOT write that
  line to any PROGRESS file; the coordinator/parent does that, in the
  morning, only if the gates pass.

What was also confirmed this session (branch reads):
`graphs/Aegis/readme_notes.md` fetched in full, SHA
24dd171e34df2d037731985a500cd2c5cab713f8 — matches phase 1: first four
headings "Pending", only Limits written. The stage-5 "Final checks"
section (AGENT_NOTES.md lines 574–579) is still stage-5 history and must
not be copied forward as a final check.

Blockers to final logs, in dependency order (unchanged from phase 1,
plus the two prints now named exactly):
1. Decision edits applied (D2, D4, D6, D7, R1, R2, R5, R6) and D3/D5
   constructions verified present on the current branch — TO-VERIFY
   whether any are present yet.
2. Full local checkout (blocked on `graphs/Aegis/auto_calls.json`,
   1,625,494 B per coordinator context, over the connector fetch limit;
   token URL forbidden) and a final build.
3. Final sample (`verify_sample.py` redraw) + every `show_route` dump
   saved under `graphs/Aegis/scratch/` + step-by-step reads (final error
   rate computed from these, not from round 7).
4. D7 missing print (showImportersDialog choice mode, setItemChecked /
   selection calls, row-listener body, OK checked-row read) and the
   E4db374dd edge text print.
5. Rows input + `make_verification.py` run + `gen_readme_v2.py` run for
   the final `out/README.md`.
6. Final readme_notes.md (four Pending sections + Limits addendum with
   the re-confirmation grep) and final LESSONS.md.
7. Final eight-check outputs recorded here (inventory itself still
   TO-VERIFY against the handoff brief; any check that cannot run is
   named as not run, never marked passed).
8. Device checks (API 27) remain NOT STARTED — a separate phase after
   the logs; the readme draft's device section is its handover.

Round-7 reference figures (history, NOT final): sample seed 20261025,
25 routes; 25 ERROR steps over 12 routes; 13 routes with no ERROR step
(3 clean, 10 UNCLEAR-only); round-7 route error rate 12/25 = 48% of
sampled routes with at least one ERROR step. Stage-5 reference figures
(history, NOT final): 2,995 methods, 5,466 edges, 0 errors, 0 warnings;
check_citations 22 distinct / 0 problems; check_bytecode_lines 3,654
checked / 0 mismatches; DEAD / FRAMEWORK_ONLY grep 0.
