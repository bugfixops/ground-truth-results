# Aegis final logs — missing-inputs report (phase-2 leaf B, 2026-11-01)

Scope: Aegis ONLY, repo bugfixops/ground-truth-results, branch
work-2026-10-31. No push, no branch edit, no device work (no
emulator/adb/APKs/new repos). No file outside
`~/workspace/overnight/stream-C/logs_phase2/` was written by this leaf.

## Verdict: NO final verification.csv was produced — correctly

`make_verification.py` (in this same directory) was implemented and
self-tested (see §4), but it was NOT run to produce a final
`verification.csv`, because its required inputs do not exist. Running it
without them would have meant inventing rows or counts, which the task
forbids. Every number in this report is either quoted from a file read
this session or marked TO-VERIFY.

Note on file placement (resolving a task-text tension): the task text
says both "write a LOCAL make_verification.py under
`~/workspace/overnight/stream-C/work/tools/`" and "WRITE ONLY:
`~/workspace/overnight/stream-C/logs_phase2/`". The WRITE ONLY list
governs, so `make_verification.py` lives in `logs_phase2/` and is headed
as a NEW LOCAL tool, not a branch file. The coordinator copies it to
`tools/` at merge time, once the inputs below exist. This leaf did not
touch `work/tools/`.

## 1. What was checked locally this session

Local workdir `~/workspace/overnight/stream-C/work/` (listed by command
this session):

- PRESENT: `tools/build_graph.py`, `tools/build_all.sh`,
  `graphs/Aegis/AGENT_NOTES.md`, `graphs/Aegis/graph_def.py`,
  `graphs/Aegis/method_list.json`.
- ABSENT locally: `graphs/Aegis/out/` is an EMPTY directory (no
  `aegis_trigger_graph.json`, no `methods.csv`, no `sanity_check.csv`,
  no `build_report.txt`, no `README.md`); no `auto_calls.json`; no
  `tools/gen_readme_v2.py`, `verify_sample.py`, `show_route.py`,
  `check_citations.py`, `check_routes.py`, `check_bytecode_lines.py`,
  or `scan_unreachable.py`; no `graphs/Aegis/readme_notes.md`,
  `verification.csv`, or `LESSONS.md`; no `final_java_only/` sources;
  no `fw_src/`; no route dumps; no rows input.

Branch reads via the GitHub connector this session (one file at a time,
~30 s pauses, no token used/waited for/written anywhere, no 429 hit):

- `tools/gen_readme_v2.py` — fetched in full; SHA
  15337a8675cde3a08fe8722b238764a577e8303c matches the phase-1 leaf's
  read. Its aggregation logic was read from the script itself (see §3),
  not guessed.
- `graphs/Aegis/readme_notes.md` — fetched in full; SHA
  24dd171e34df2d037731985a500cd2c5cab713f8 matches the phase-1 leaf's
  read. Its Limits text is carried verbatim into the readme draft in
  this directory.

## 2. Precise missing-inputs list, in dependency order

1. **Applied decision edits.** Stream-C `DECISIONS.md` records 7
   decisions (D1–D7) plus related decisions R1–R8 as Muse's own, for
   user/Yang review, with graph edits DESCRIBED but not applied by that
   dossier (D2, D4, D6, D7, R1, R2, R5, R6 edits; D3 @SAVED and D5 @APP
   constructions to verify as present). Whether any of those edits are
   present on the current branch `graph_def.py` is TO-VERIFY — this leaf
   did not diff the branch file for them. No final log may cite a
   pre-decision graph.
2. **A full local checkout.** The full build is BLOCKED on
   `graphs/Aegis/auto_calls.json` (1,625,494 B per coordinator context;
   not re-measured this session — it exceeds the connector fetch limit
   and a token URL is forbidden). Without it, `tools/build_graph.py`
   cannot run to a final build, so there is no final
   `build_report.txt`, no final `methods.csv`, no final
   `aegis_trigger_graph.json`, and no final `sanity_check.csv`.
3. **Final build outputs.** No final build means no final method/edge
   counts, no final REACHABLE/UNREACHABLE split, no final
   `explicit_standard_route` / `confirmed_by` tallies. The only counts on
   record are stage-5 (2,995 methods, 5,466 edges, 0 errors, 0 warnings
   — AGENT_NOTES.md lines 574–579) and stage-1/stage-5 verdict split
   (REACHABLE 2,537 / UNREACHABLE 458). Those are STAGE-5 counts, NOT
   final counts, and are never used as final numbers in the drafts.
4. **Trigger-graph JSON `verification` object.** Whether the branch
   `graphs/Aegis/out/aegis_trigger_graph.json` already carries a
   `verification` object is TO-VERIFY (that file, ~4.9 MB per phase-1,
   was not fetched this session). Until the injector in
   `make_verification.py` runs, `gen_readme_v2.py` prints "No
   verification log yet" even if a CSV existed.
5. **Final sample + step-by-step route checks (the rows input).** No
   fresh `verify_sample.py` draw on a final build exists; no final
   `show_route` dumps saved under `graphs/Aegis/scratch/` exist. The
   round-7 sample (seed 20261025, 25 routes) is history, not the final
   sample, and only 2 of its 25 dumps are in the repo
   (`GlideRequests_asBitmap.txt`, `Slot_init.txt`, plus `sample_r7.txt`
   — confirmed by the steps 6–10 leaf's fresh directory listing). The
   remaining 23 round-7 routes are NOT CHECKED, and no final-sample
   route has been read at all. Therefore the rows input
   (`verification_rows_final.json` — a JSON list of individually
   checked label/edge/path rows) does not exist anywhere and cannot be
   reconstructed from round 7.
6. **The D7 missing print.** `Dialogs.showImportersDialog` source: the
   ListView's choice mode, any `setItemChecked` / `setSelection` /
   `setChoiceMode` call, the row-listener body, and the OK handler's
   checked-row read, printed together with file:line for each
   (DECISIONS.md D7). Until it lands, the GoogleAuthImporter.readFromApp
   route stays ERROR and no `correct` path row may be written for it.
7. **The E4db374dd edge text print.** DECISIONS.md R3: this edge is kept
   as INFERRED only if its evidence text says the source was not read;
   if it claims FW-SRC lines, that citation is wrong and must be
   corrected before the edge counts. Its current text was not printed
   this session — TO-VERIFY.
8. **Eight-check outputs on the final build.** No final-build check
   output exists (build, check_citations, check_routes,
   check_bytecode_lines, scan_unreachable, verify_sample +
   show_route step checks, DEAD/FRAMEWORK_ONLY grep — names grounded
   in AGENT_NOTES.md lines 574–579 and the phase-1 gap analysis). The
   complete eight-check inventory itself is TO-VERIFY against the
   handoff brief; no eight-item list is published as confirmed here.
   Any check that cannot run on the phase-2 checkout must be named as
   not run, never marked passed.
9. **Final `readme_notes.md` inputs.** The four Pending sections can
   only be finalised from the final build numbers, the final sample
   description, and the final device-plan state — all missing per items
   2, 3, 5 above. The draft in this directory carries TO-VERIFY marks
   at every such point.
10. **Device phase (separate, later).** Device checks on API 27 are NOT
    STARTED and are not part of this logs phase. The readme draft's
    device section is a handover list, not a claim that any device check
    passed.

## 3. DRAFT outline for the final verification.csv (never presented as final)

- Tool: `make_verification.py` in this directory (see its header for
  the full row plan and the resolved aggregation rule).
- Header, exactly: `type,item,result,confirmed_by,ref,edges,note`.
- Row types, exactly three: `label`, `edge`, `path`. No summary/count
  rows. `confirmed_by` only SOURCE or INFERRED (the tool rejects
  anything else and exits non-zero before writing).
- `result` values in the CSV: `correct`, `error_found`, `unclear`.
- JSON `verification` object shape (all three types always present):
  `{"label": {"checked": C, "correct": C1, "errors_found": E,
  "unclear": U}, "edge": {...}, "path": {...}}` where `checked` =
  correct + errors_found (EXCLUDES unclear). This resolves the phase-1
  §4c TO-VERIFY: it is confirmed from `gen_readme_v2.py` itself, which
  prints Rows as `v['checked'] + v['unclear']` — so a `checked` that
  included unclear rows would double-count in the published table.
- Expected final run (once items 1–8 above exist), from a full checkout:
  `python3 -I tools/make_verification.py --app Aegis --rows
  graphs/Aegis/scratch/verification_rows_final.json --graph-json
  graphs/Aegis/out/aegis_trigger_graph.json --csv-out
  graphs/Aegis/verification.csv`
  then `python3 -I tools/gen_readme_v2.py Aegis` for the final
  `out/README.md`. Only then may the readme draft in this directory be
  finalised with the printed numbers.
- Counts: ALL final counts are TO-VERIFY. No row count, no
  correct/error/unclear split, and no sample error rate is asserted for
  the final sample anywhere in this directory. The only error rate on
  record is the ROUND-7 rate: 25 ERROR steps over 12 of 25 sampled
  routes (12/25 = 48% of sampled routes with at least one ERROR step;
  13 routes with no ERROR step — 3 clean, 10 UNCLEAR-only), from
  AGENT_NOTES.md line 669 via the phase-1 gap analysis. That is history,
  not a final figure.

## 4. Tool self-test (synthetic data only — NOT Aegis data)

`make_verification.py` was compiled (`py_compile` OK) and run in
`/tmp/mv_test/` against a synthetic 6-row input (3 label, 2 edge,
1 path) and a synthetic schema-2 JSON. Observed output: label
rows=3 correct=2 errors_found=0 unclear=1 checked=2 (published
Rows=3); edge rows=2 correct=1 errors_found=1 unclear=0 checked=2
(Rows=2); path rows=1 correct=1 errors_found=0 unclear=0 checked=1
(Rows=1); CSV header exactly as specified; injected `verification`
object matches those counts; `--dry-run` wrote nothing. A rejection
test with `confirmed_by` UNVERIFIED failed with exit 1 and wrote
nothing. The synthetic rows used illustrative example names only and
are NOT in this directory's deliverables. The tool has never been run
on real Aegis inputs, because those inputs do not exist yet.
