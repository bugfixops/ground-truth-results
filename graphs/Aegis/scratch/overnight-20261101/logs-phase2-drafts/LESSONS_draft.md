# DRAFT LESSONS.md — Aegis (phase-2 leaf B, 2026-11-01)

DRAFT ONLY. Not the branch file (no `LESSONS.md` exists on branch
work-2026-10-31, per the phase-1 leaf's listing of `graphs/Aegis/`).
Each bullet cites the source actually read; line numbers are
AGENT_NOTES.md lines of the branch file fetched in phase 1, unless
another file is named. No bullet decides a Yang item — the Stream-C
decisions (D1–D7, R1–R8) are recorded as Muse's own decisions in
stream-C `DECISIONS.md`, for user/Yang review, and are referenced here
only as the standing treatment, not as settled project doctrine.
Finalise after the final round, so the lessons describe the final round
as well as rounds 5–7.

- Lesson 1 — A state-blind router makes "add the producer edge" a
  non-fix. The router compares env, needs_state count and steps and
  never checks that a state is produced (AGENT_NOTES.md line 10, citing
  tools/build_graph.py:147–175, 436–470), so a producer edge alone never
  puts the producer on the chosen route (AGENT_NOTES.md lines 604, 614:
  "The router stays state-blind and unchanged. Its effect is the main
  cause of the remaining ERROR steps"). Fixes need variant nodes that
  only the producer chain reaches, or a state-aware router — the latter
  needs approval as a tools/schema change (DECISIONS.md R4: no tools
  change requested; variant nodes are the approved Aegis workaround,
  precedent @SCAN, @SAVED).
- Lesson 2 — One shared dialog node cannot serve callers with different
  listeners. The shared text-input relay (edges E41c33149 / E02b5fa3e)
  and the shared error-dialog OK relay
  (Dialogs.lambda$showErrorDialog$15) dispatch every caller's OK to one
  listener; round 6/7 errors on GlideRequests steps 24/27, Slot step 26,
  and ExportResultListener steps 24–29 all trace to this (AGENT_NOTES.md
  lines 626, 635; stage-5 log lines 464, 488: the @FILE/@APP split was
  needed because "one dialog node is shared by both rows and the router
  is state-blind"). The partial fix that did land — typing before OK in
  the shared text-input dialog (AGENT_NOTES.md lines 634, 643: "OK in the
  shared text-input dialog needs typing first", Dialogs.java:201–205
  watcher, 226–229 OK disabled until text) — fixed the no-typing errors
  without fixing the relay itself. Standing treatment (DECISIONS.md R2):
  split into caller-context variants; wrong-listener steps stay ERROR
  until the split.
- Lesson 3 — Cross-run state is UNCLEAR, not ERROR, once the rule is
  stated. Round 7 applied rule D2: cross-run vault or icon-pack states
  are UNCLEAR, not ERROR (AGENT_NOTES.md round-7 section). Slot step 8
  and EntryAdapter step 8 were reclassified ERROR to UNCLEAR under D2,
  and the round-7 totals (25 ERROR steps over 12 routes, AGENT_NOTES.md
  line 669) already reflect that rule. Stating the classification rule
  before judging steps prevents re-litigating the same steps every
  round. Standing treatment (DECISIONS.md D2/D4/R1/R7): keep the
  cross-run edges with a needs_state; fresh-declared routes using them
  are UNCLEAR, relaunch-declared routes using them are correct.
- Lesson 4 — A tool run beats a configuration reading. The first plan
  closed the export-groups filter path with closed_by_configuration
  because allow_filtering=false stops typing; the sanity check then
  showed getFilter, its anonymous Filter, performFiltering and
  publishResults running in a tool run, so the plan was corrected and
  the four were kept as REACHABLE framework routes (INFERRED), with the
  trigger left as an open device item (AGENT_NOTES.md line 27).
  Configuration text alone does not settle what the framework runs.
- Lesson 5 — Splitting a shared node beats moving its edge. The stage-5
  import-dialog fix split E72c20578 into @FILE (opened by the file
  import row, OK to lambda$onCreatePreferences$5) and @APP (opened by
  the app import row, OK to lambda$onCreatePreferences$7), because
  moving a single edge would have moved an edge correct for its own
  branch (AGENT_NOTES.md lines 464, 473). When one edge is right for
  one branch and wrong for another, the node — not the edge — is the
  unit to change. The same pattern recurs in DECISIONS.md (D3 @SAVED,
  D5 @APP, R5 @VAULT/@ICON, R6 @ADD/@DELETE).
- Lesson 6 — A 0-error build is not a done graph. The stage-5 final
  checks read: build 0 errors / 0 warnings, check_citations 22 distinct
  / 0 problems, check_bytecode_lines 3,654 checked / 0 mismatches,
  DEAD / FRAMEWORK_ONLY grep 0 (AGENT_NOTES.md lines 574–579) — and the
  same section warns "This does not mean the Aegis graph is done."
  Round 7 then found 25 ERROR steps on that graph family (AGENT_NOTES.md
  line 669). Final checks must be re-run on the FINAL build and
  reported with the sample error rate, not inherited from an earlier
  stage.
- Lesson 7 — Route dumps must live in the repo, or the check cannot be
  repeated. Only 2 of the 25 round-7 dumps are in the repo under
  graphs/Aegis/scratch/route_check_r7/
  (`GlideRequests_asBitmap.txt`, `Slot_init.txt`, plus `sample_r7.txt`)
  — CONFIRMED by the steps 6–10 leaf's fresh directory listing this
  phase, which upgrades the phase-1 TO-VERIFY on this figure to
  confirmed; the other 23 were in "scratchpad r7/", outside the repo
  copy (AGENT_NOTES.md round-7 section: "Dumps: scratchpad r7/"), so
  their steps 6–10 could not be re-checked from the branch. Future
  samples must save every dump under graphs/Aegis/scratch/ before the
  round is called checked.
