# hash-checker — agent notes (finish run, head 6805252)

Ticked app: LOG WORK ONLY. No label, edge, route, or `graph_def.py`
change in this run. No PROGRESS line change. No device run, no adb.

## Steps

### Setup (2026-11-01 ~13:27 EST)
- Lock: local merger lock (not pushed).
- Private tree: local copy (graphs/hash-checker copied from the clone
  at HEAD 6805252; tools/, handoff/, fw_src/, final_java_only/,
  work-emulator symlinked read-only). The shared clone is never edited
  in place.
- Prior inputs (inputs only): graphs/hash-checker/scratch/overnight-20261101/
  (AGENT_NOTES, DECISIONS D1-D6, LESSONS draft, readme_notes, scratch-outputs).

### Baseline local build (2026-11-01 ~13:29 EST)
- Command (private tree): `bash handoff/ci/rebuild.sh hash-checker`.
- SUMMARY matches the branch ci_latest SUMMARY (commit 60c27937) on
  every count: methods 529, REACHABLE 507, UNREACHABLE 22
  (closed_by_configuration 3, framework_never_calls 3,
  no_trigger_in_app 16), errors 0, warnings 0, check 2: 0 problems
  (15 distinct), check 3: 0 flagged, check 4: 0, check 5-7: 7 / 0 / 4,
  STRICT line 1, check 8: 4 of 22, verification path 37, DEVICE 0.
  Only the header commit/timestamp differ (private tree is not a git
  checkout). Local build log: merger work dir `build_baseline.txt`
  (not pushed). Local `scratch/ci_latest/` is never pushed (CI writes it).

### verification.csv analysis (2026-11-01 ~13:3x EST)
- 124 rows: path 37 (final sample 30 in order, then 7 earlier-read:
  LogUtils.e, AppTextWatcher.<init>, ThemeConfigImpl.setCurrentTheme,
  HashCalculatorFragment.selectFileFromSystemFileManager, and the three
  module <init>s), label 52 (22 UNREACHABLE + 30 sampled REACHABLE),
  edge 35. Results: path 24 correct / 13 fixed, label 50 / 2, edge
  9 / 26. confirmed_by: SOURCE 99, INFERRED 25, DEVICE 0.
- File order is path block, label block, edge block (not alphabetical);
  line endings are CRLF throughout (csv.writer default). A plain
  csv read/write round-trip is byte-identical.

### T3 writer (2026-11-01 ~13:3x EST)
- Wrote `graphs/hash-checker/make_verification.py` (portable, stdlib
  only, repo-relative paths, run from the repo root) and
  `graphs/hash-checker/scratch/verification_rows.json` (124 rows in
  file order, 59,268 B, seeded from the branch file).
- Validation (script stops on any mismatch): path rows REACHABLE with
  edges exactly equal to `route_edge_ids` and every edge id in the
  trigger JSON; ref files on route evidence, the method's own file, or
  the one documented exception below; label confirmed_by matches
  methods.csv and the UNREACHABLE label set equals the graph's
  unreachable set; edge ids exist and ref files are in the edge
  evidence; no duplicate (type, item); no empty note.
- Tests, all in private trees: output deleted, then regenerated
  byte-identical to the branch file (44,399 B); two runs identical;
  `py_compile` OK. D7 synthetic test: 3 results rows (reached/ok,
  not-reached/failed_at_step_2, unscriptable) append exactly 3 DEVICE
  rows with the expected result/note values and leave the first 124
  rows identical; wrong-edges and unknown-method inputs are refused
  (exit 1) with the output unchanged; a no-results run is byte-identical
  to the branch file. `verification.csv` itself is unchanged, so it is
  NOT pushed with the writer.

### readme_notes.md and LESSONS.md (2026-11-01 ~13:4x EST)
- `## Limits` gained three bullets (existing bullets untouched, five
  headings still in order): check 5 counts 7 lines (63, 79, 684, 692,
  695, 704, 706 — DEAD/FRAMEWORK_ONLY containers + conversion code);
  check 7 counts 4 lines (33, 460, 463, 464 — page id
  `S_MAIN_EXIT_PENDING`); check 8 shows 4 methods, each explained with
  its caller lines (BaseFragment pair by virtual dispatch;
  getThemeAnalogue and setRefreshSelectedFileStatus by
  closed_by_configuration + SUPPRESS).
- `LESSONS.md` written (7 bullets, grounded in readme_notes and the
  verification rows). `gen_readme_v2.py` run locally: exit 0, 53 lines,
  matches branch out/README.md except the app/commit line (CI
  regenerates out/README.md; not pushed by the merger).

### Route prints for D3 (2026-11-01 ~13:4x EST)
- `graphs/hash-checker/scratch/route_print.py` adapted from
  handoff/examples/route_print_template.py (APP_MODULES = src/main +
  src/thirdPartyStores; googlePlay deliberately excluded; the two sets
  share zero relative paths, so basename resolution is unique),
  `scratch/route_methods_37.txt` (header + 37 path methods in file
  order), `scratch/route_print/` (37 files, one per path method).
- Result: 0 SOURCE FILE NOT FOUND, 0 framework-not-printed,
  0 out-of-range; no template-app strings remain in route_print.py.

### D1 review (2026-11-01 ~13:4x EST)
- The device lead's D1 helper delivered
  `device/routes/hash-checker/ROUTES.csv` (37 rows) + ROUTES_NOTES.md
  into the device work dir. Merger review: 0 mismatches against
  verification.csv path rows (method, edges, source, in order) and
  methods.csv env/state kinds; 37 scripted, 0 unscriptable (0%, under
  the 10% cap); permissions empty on all rows (justified: no route
  edge names a permission gate, app code never checks one, the picker
  grants URI access); fixtures on 7 rows (all exist under
  work-emulator/fixtures); every edge chain starts at S_ENTRY, is
  contiguous, and ends at the method.
- Status: PENDING AUDITOR PASS. Not pushed yet. Flag for the auditor:
  the debug manifest declares storage permissions the app code never
  checks; they are treated as a harness precondition, not route gates
  (see decision HC-D1-1).

### D3 scripts (2026-11-01 ~13:4x EST)
- Helpers fanned out in ranges (at most 5 routes each, one app) to
  write `device/routes/hash-checker/route_NN.py` scripts against the
  staged harness API, the ROUTES.csv rows, and the printed routes.
  Helper output is delivered to the merger's helper dirs and is merged
  (copied into device/routes/hash-checker/) only after auditor PASS.
- Scripts are pushed only after auditor PASS and a local dry run
  (device/drycheck.py --load-scripts) showing all scripted routes PASS.

### Pushes
- T3 push (make_verification.py, verification_rows.json, AGENT_NOTES,
  LESSONS, readme_notes): attempt 1 failed "Update is not a fast
  forward" (branch head had moved to 2722b9a0 on other streams'
  pushes; all 5 T3 paths verified untouched at that head: readme_notes
  blob matches the 6805252 blob, the other 4 still absent); attempt 2
  landed as commit 21db8c53931959eab5bc7658e6bcf874946e14f4, verified
  by branch read-back (all 5 blob SHAs match local exactly).
- Push-lock protocol (coordinator, 2026-11-01, mandatory for all
  agents after MMEX B5 failed three times on the branch race): before
  any push-files call, atomically take the coordinator push lock in
  the local locks dir (owner + UTC time inside); if it exists, do
  other work and retry later, never spin or sleep-loop; re-check the
  branch head and confirm staged paths untouched immediately before
  the call; hold the lock through the call; remove it immediately
  after, success or fail. A lock older than 30 minutes may be broken
  by a waiter (record the broken lock's owner/time). Never push
  without holding the lock.
- Route-prints push attempt 1: failed "Update is not a fast forward"
  (head moved during the approval window). Retry follows the
  push-lock protocol above.

## Current step
D3 script helpers running (routes 01-37). T3 pushed (commit
21db8c53, read-back verified). Next: push route prints; routes push
waits for auditor PASS + local dry run. CI rebuild request and D9 dry
run go through the coordinator.

## Decisions made by Muse (for the user and Yang to review)
- **HC-T3-1 (writer order).** Seed order = current file order
  (path/label/edge blocks), not alphabetical sort, because T3
  acceptance is byte-identical output and the current file is in
  verification order. The order is fixed and deterministic via the
  seed JSON. Effect: writer output matches the branch file
  byte-for-byte; no row content changed. Reverse: re-sort the seed
  (breaks byte-identity; do not).
- **HC-T3-2 (path-ref exception).** The LogUtils.e path row's ref
  cites SharedPreferencesSettings.java:44-49, the getLastHashType()
  catch that calls LogUtils.e — the second printed LogUtils.e call
  site, retained as supporting evidence for this 'fixed' row. It is
  not on the route's edge evidence (the route ends at the
  openSystemFileManager catch, HashCalculatorFragment.java:196-199)
  and not the method's own file, so it is listed as the single named
  exception in the writer rather than weakening the rule. All other
  path refs validate against route evidence or the method's own file.
  Reverse: remove the exception entry (the writer then refuses the
  current file; only valid if the row's ref is changed after a route
  re-check).
- **HC-D1-1 (empty permissions).** ROUTES.csv permissions are empty
  because no route edge names a permission gate, app code never checks
  a runtime permission, and file/folder access goes through the Storage
  Access Framework (URI grants, not runtime permissions). The debug
  manifest's storage permissions are flagged as a harness precondition
  (the replay APK is a debug build; the picker may need pre-granted
  storage to see pushed fixtures), not as route gates. Auditor to
  confirm. Reverse: list READ/WRITE_EXTERNAL_STORAGE on picker routes
  (changes ROUTES.csv and the dry-run permission checks).
- **Overnight D1-D6 (carried).** See
  scratch/overnight-20261101/DECISIONS.md (on branch). D1 is resolved
  by this T3 writer. D2 (DEAD/FW containers + PENDING screen name) is
  recorded in `## Limits`. D3 (redraw rate basis) is reflected in
  readme_notes (historical 13/37 vs redraw 0/30). D4 (scan scope
  main+thirdPartyStores) matches the route-print source sets. D5 (AMS
  14/15 local caveat) is superseded: the local rebuild reads fw_src
  from disk and CI SUMMARY shows check 2: 0 problems on all 15
  citations. D6's gate call is superseded by this finish run (T3 +
  D1-D9 + CI dry run).
