# Aegis device routes — collect / compare wiring and D7

No change to `collect.py`, `compare.py`, `jacoco_lookup.py`, or any
shared tool is proposed or made by this package. The wiring below is the
unchanged shared chain, with the Aegis inputs this package stages.

## Chain (unchanged shared tools, Aegis inputs)

1. `device/run_app.sh Aegis "route_*.py" <outdir>` (or `--dry-run`)
   writes `<outdir>/results.csv` with columns `app,route,method,edges,
   reached,script_status,steps_done,steps_total,error,run_id`, plus
   steps logs, screens, and logcat evidence.
2. `device/collect.py collected <dest>` copies ONLY small text files
   (`results.csv`, `run.log`, `steps/*.log`, `dryrun_report.txt`) into
   `device/<kind>/<run>/` (screenshots, UI dumps, coverage files stay in
   the 30-day artifacts and are never committed); logs over 5 MB are
   truncated with a marker; it writes `SUMMARY.md` with per-app counts
   (routes, reached, not reached, script failed, unscriptable — or
   PASS/FAIL for a dry run). A row can count in both "not reached" and
   "script failed"; the columns are per-column counts, not a partition.
3. `device/compare.py <results_dir> [--out-root R]` reads the committed
   `<results_dir>/Aegis/results.csv` and writes
   `graphs/Aegis/device/results.csv` with columns
   `route,method,edges,reached,script_status,run,script`
   (`run` = input directory basename, `script` = `<route>.py`).
   Unscriptable rows are kept (`reached=not_run`) so D7 can emit unclear
   DEVICE rows for them. With `--out-root` pointing at a temp dir, no
   real graphs tree is touched — that is the test path.
4. Aegis `make_verification.py` consumes
   `graphs/Aegis/device/results.csv` and appends DEVICE rows to
   `verification.csv` on the next rebuild.

## D7 block (existing; verification performed in assembly — see the AGENT_NOTES D7 section)

The D7 block already exists in the merger tree's Aegis
`make_verification.py` (per the D7 plan, around lines 284-310). The
merger's D7 work was verification of that existing block
against the shared `device/D7_SPEC.md` plus the synthetic test below —
NOT writing D7 from scratch, and NOT claimed by this package:

- If `graphs/Aegis/device/results.csv` does NOT exist, running
  `make_verification.py` must produce output byte-identical to the
  current committed `verification.csv` (the DEVICE code path must not
  run at all in that case).
- If it exists, append one row per results row AFTER all existing rows,
  in `device/results.csv` order (route order). Do NOT re-sort existing
  rows. For Aegis, the current committed `verification.csv` has 534
  rows (483 label, 26 edge, 25 path, verified in staging); DEVICE rows
  go after row 534, never interleaved.
- Row fields: `type=path`, `item`=route method, `result=correct` only
  when `reached=yes`, otherwise `unclear` (never `wrong`),
  `confirmed_by=DEVICE`, `ref=device run <run>/<script>`,
  `edges`=route edges unchanged, `note`=script status with the reason
  for unclear rows (not reached, script failed, or unscriptable).
- A route not reached NEVER becomes `wrong`. No label changes. DEVICE
  rows never feed back into labels, edges, or route checks.
- WRONG-row note: if AuthActivity.lambda$onCreate$3 (new row 17, judged
  wrong) ever showed `reached=yes`, its DEVICE row would read
  `result=correct`, appended AFTER the existing wrong row, which stays
  untouched. The two rows coexist; the DEVICE row does not correct,
  override, or delete the judged row. (Row 17 is unscriptable as drawn
  in this package, so no such DEVICE row is expected from it.)
- Synthetic-results test (required before pushing any D7 change, in a
  private copy, never the shared tree): run once with no
  `device/results.csv` (byte-identical output); add a synthetic
  `device/results.csv` with at least one `reached=yes, script_status=ok`
  route (expect DEVICE `correct`), one `reached=no, script_status=ok`
  route (expect `unclear`, not reached), one
  `script_status=failed_at_step_3` route (expect `unclear`, script
  failure), and one `script_status=unscriptable` route (expect
  `unclear`, unscriptable); run again (ONLY differences are the
  appended DEVICE rows, in input order, after all existing rows); run
  twice (both runs byte-identical); report the added-rows-only diff to
  merger review.

## Coverage signals and Aegis mapping gaps (report, don't reinterpret)

- `reached=yes`: target method instructions executed in the route's
  final coverage window (JaCoCo XML instruction covered > 0 for the
  mapped method). `reached=no`: script ran (or partly ran) but the
  method did not execute. `reached=not_run`: no coverage evidence
  (missing/invalid final dump, or unscriptable) — NOT evidence for or
  against the label.
- A `method_absent_in_report` outcome for a generated-code method must
  be reported as a mapping gap, never read as "the route does not reach
  the method". Aegis methods needing a mapping pre-check before any
  real run is interpreted: Hilt_AegisApplication (row 24, generated Hilt
  superclass), MigrationPayload.parser (row 16) and DigitCountVerifier
  (row 23, generated protobuf), AuditLogDao_Impl tail (row 18, generated
  Room), and every `<init>` / lambda / overload method (rows 02, 05 is
  getType not init; the init/lambda rows are 02, 06, 07, 08 decrypt
  lambdas/overloads, 12 scanner lambda, 17 Auth lambda, 19
  SlotIntegrityException init, 20 IconPack Icon init, 23 verifier init).
  The merger must pre-check, for all 25 methods, that each maps to a
  class present in `classes/Aegis/0` / `method_list.json` as the
  instrumented build sees it. This pre-check is still open (see report).
