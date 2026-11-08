# Currency — agent notes (finish run, branch work-2026-10-31)

Ticked app: log work only. No label, edge, route, or graph_def.py change
is made here, and the PROGRESS line stays exactly as it is.

## Current step

T1 writer done, tested, and pushed (commit 642a97b, read-back
verified); D1 audit PASS and D3 audit PASS (all six groups) now on
file; continuation merger pushing D1, then D3 (docstring path fix
applied to routes 06-25, drycheck re-verified 28 PASS, 0 FAIL);
D7 DEVICE support in the writer, tested on synthetic results.
CI request for Currency is the coordinator's step
(coordinator-only); F1 readiness is reported to the coordinator with
the evidence below.

## Steps

- 2026-11-01, private tree built from the clone (HEAD 6805252):
  graphs/Currency copied; tools/, handoff/, fw_src/,
  final_java_only/, work-emulator symlinked read-only. Lock created.
- 2026-11-01, local build `python3 -I tools/build_graph.py
  graphs/Currency currency`: 145 methods, 140 REACHABLE / 5 UNREACHABLE,
  393 edges, 0 errors, 0 warnings, STRICT=True. out/methods.csv and
  out/currency_trigger_graph.json are byte-identical to the branch CI
  out/ (commit 60c27937), so the tree is correct.
- 2026-11-01, sample check `python3 -I tools/verify_sample.py Currency
  30 20261025`: draws 27 methods / 107 edges, NOT the recorded 28-path
  final sample. In today's draw, Main.onDateResult and
  Parser$Handler.<init> appear; ChartActivity.updateRange,
  ChartParser$Handler.<init> and Parser.startParser(Context,int) do not.
  The 3 recorded-but-undrawn path rows still validate against the
  current build (edges equal the methods' routes, path_status
  SOURCE_OK), and the 2 newly drawn methods are UNCHECKED. Per decision
  CUR-T1-D1 below, the 28 recorded path rows are preserved; no row is
  dropped or added on sampler drift alone.
- 2026-11-01, T1 writer written: graphs/Currency/make_verification.py,
  seeded once from the branch verification.csv into
  graphs/Currency/scratch/verification_rows.json (98 rows: 28 path, 47
  label, 23 edge). Validation per brief section 4 (edge ids exist,
  label verdicts match, path edges equal the method's route, plus ref
  sanity against app/framework source). Result: py_compile OK; run 1
  byte-identical to the branch verification.csv (cmp prints nothing);
  two runs identical. The one AnyMemo-style ref check that does not
  apply here is documented under CUR-T1-D2.
- 2026-11-01, D7 synthetic test (private copy, not the tree): a
  synthetic device/results.csv with 4 routes (reached yes / not reached
  / script failed / unscriptable) adds exactly 4 DEVICE rows with the
  brief's result/ref/note mapping, and the seeded 98 rows stay
  byte-identical. Without a results file the output is byte-identical
  to today's file (proven by the run-1/run-2 cmp above).
- 2026-11-01, check 8 (T1 step 4): scan shows 1 of 5 unreachable methods
  with an outside caller: Singleton.getList <- ChartActivity.onCreate
  (ChartActivity.java:176). CONFIRMED: its reason already explains the
  caller — graph_def.py:54-57: "The only call site,
  ChartActivity.java:176, is the else-branch of "instance == null"
  (:163); instance is an instance field (:90), null whenever onCreate
  starts, so the branch never runs". Printed app source confirms
  onBindDialogView/AboutPreference lines used for the ref check (see
  CUR-T1-D2). No readme_notes.md change needed for check 8.
- 2026-11-01, readme_notes.md checked: the five headings are present
  exactly and in order (What the re-audit changed / How the checked
  paths were chosen / What waits for a device (API 27) / Hazard
  candidates / Limits). CI runs gen_readme_v2.py and commits
  out/README.md; no local README write is pushed.
- 2026-11-01, D1 verified: device/routes/Currency/ROUTES.csv (drafted
  by the device lead's D1 helper) checked mechanically against
  verification.csv, out/methods.csv, out/currency_trigger_graph.json,
  AndroidManifest.xml and work-emulator ci/apps.csv: 28 rows, method
  order equals path order, edges equal path edges, source equals path
  ref, env/state kinds equal methods.csv, 28 scripted, 0 unscriptable,
  permissions empty (manifest declares only INTERNET and
  ACCESS_NETWORK_STATE, both normal install-time; trigger graph has 0
  permission hits), fixtures empty (only STATE kind is data, created by
  fresh install / pm clear, not by a pushed file), setup on every row
  copied verbatim from ci/apps.csv ("network (ECB); cert issue on
  API<=27 images"). Adopted as the merger's D1 deliverable.
- 2026-11-01, D3 route prints generated with tools/show_route.py into
  graphs/Currency/scratch/route_print/ (28 files, one per path method),
  for the route-script headers.

## Decisions made by Muse (for the user and Yang to review)

- CUR-T1-D1 (Currency, T1, verification.csv path membership): options
  (a) rewrite path rows to today's 27-method redraw (drop 3, add 2),
  (b) preserve the recorded 28 path rows. Choice: (b). Printed
  evidence: verify_sample.py Currency 30 20261025 output (27 methods,
  107 edges) vs verification.csv (28 path rows); methods.csv shows the
  3 undrawn methods SOURCE_OK and the 2 newly drawn methods UNCHECKED;
  all 28 path rows' edges equal the current methods.csv routes.
  Effect: verification.csv unchanged; D1 uses the 28 recorded rows.
  Reverse: if the user directs a redraw, replace the path rows with the
  newly judged 27 and re-run the writer; the seed JSON is the only file
  that changes.
- CUR-T1-D2 (Currency, T1, writer validation scope): options (a)
  AnyMemo's stricter check (path ref base must appear on the route's
  edge evidence), (b) brief section 4 validation (edge ids exist,
  label verdicts match, path edges equal the route) plus ref sanity
  (ref names a real app/framework source file). Choice: (b). Printed
  evidence: the single row failing (a), AboutPreference.onBindDialogView
  ref AboutPreference.java:50, cites the method definition site
  (printed: AboutPreference.java:49-50, @Override onBindDialogView),
  while the route evidence cites the framework caller
  (DialogPreference.java). Effect: all 28 path rows validate; the
  writer fails loudly on any genuinely dangling ref. Reverse: add the
  evidence-substring check and the row would need its ref rewritten to
  a DialogPreference citation.
- 2026-11-01, D3 route scripts complete: 6 helpers delivered 28
  scripts (routes 01-28) to work/Currency/helper/d3-*/. Merger
  verification, all printed this session: device drycheck.py run
  against a test root with all 28 scripts at final placement gives
  Currency: 28 PASS, 0 FAIL; mechanical edge-coverage check shows
  every route edge used, none missing, none extra (duplicated log
  lines only where a script uses a fallback tap pair or a compound
  action on one edge). Scripts are NOT yet pushed: they await
  coordinator-assigned auditor PASS (at least 1 in 3 read against the
  printed route), after which the merger applies the docstring
  path fix (routes 06-25 cite the printed route by absolute
  private-tree path; routes 01-05 and 26-28 already repo-relative),
  re-runs py_compile + drycheck, and pushes scripts + route_print
  files + updated AGENT_NOTES in one D3 push under the push lock.
- 2026-11-01, D1 push blocked three times on the branch race (last
  attempt under the push lock, head 493450f7, paths confirmed
  untouched, still "not a fast forward"), so a concurrent push moved
  the head mid-call despite the lock. D1 staging is intact and the
  retry waits for auditor PASS on the ROUTES.csv + notes plus a lock
  window. T1 push (commit 642a97b) succeeded and was verified by
  branch read-back.
- 2026-11-01, route_05 rotation caveat (for auditor + device lead):
  the script rotates via the harness's private Runner._shell
  (settings put system accelerometer_rotation + user_rotation) and
  deliberately does not rotate back, so later routes would run in a
  rotated state unless run_app.sh resets orientation between routes.
  Suggested global fix: orientation reset in run_app.sh; alternative:
  rotate-back step in route_05. Auditor to judge; no script edited
  before auditor PASS.

- CUR-D3-D1 (Currency, D3, route_07 toast precondition): options (a)
  mark route_07 unscriptable, (b) keep scripted. Choice: (b). Printed
  evidence: route_07's target fires only when network is off, or
  non-Wi-Fi with default pref_wifi, or roaming; the Runner has no
  network toggle, but network-off IS creatable via adb (svc commands),
  so the route fails the brief's unscriptable test ("conditions adb
  cannot create"). Effect: script stands, dry-PASS; on a Wi-Fi
  emulator the real run may return not-reached, which becomes unclear,
  never wrong. Reverse: if the user requires the toast branch to be
  deterministically reachable, add a per-route network precondition to
  run_app.sh (device lead's call) or mark the route unscriptable.
- CUR-D3-D2 (Currency, D3, widget routes 24-27): options (a) require
  literal launcher widget placement (routes unscriptable), (b) accept
  broadcast substitution. Choice: (b). Printed evidence: brief
  section 5.6 D3 itself prescribes that a widget step "becomes
  start_intent or broadcast over adb with a comment"; the scripts use
  the identical system broadcasts (APPWIDGET_CONFIGURE,
  APPWIDGET_UPDATE with the exact extras from source, APPWIDGET_DELETED)
  the launcher/AppWidgetService would deliver. Effect: routes 24-27
  stand as scripted. Reverse: if literal placement is ever required,
  routes 24/25 (and the configure leg of 26/27) become unscriptable.
- No other decisions. Batch 5 rows 19/20/25/26 (user decision D29) do
  not concern Currency.

## Continuation merger 2026-11-01 (D1/D3 pushes)

- D1 audit PASS (audit/D1/AUDIT.md, 6,210 B): 28 rows = 28 path rows,
  mechanical all 28, statuses all scripted, 0 unscriptable.
  D3 audit PASS (audit/D3/AUDIT.md, 10,503 B): all six groups,
  12/28 scripts read against printed routes, independent dry run
  28 PASS, 0 FAIL. Auditor-accepted decisions CUR-D3-D1 (route_07
  toast stays scripted) and CUR-D3-D2 (broadcast substitution for
  widget routes 24-27) stand; recorded here for the coordinator's
  branch append to handoff/MUSE_DECISIONS.md.
- D3 merge condition applied by the continuation merger (auditor
  PASS, behavior-neutral): routes 06-25 docstrings rewritten from
  absolute private-tree paths to repo-relative
  graphs/Currency/scratch/route_print/<method>.txt; routes 01-05
  and 26-28 already repo-relative. Verified: exactly the 20
  scripts differ from helper originals, each by the single
  docstring line (20 old lines carry the absolute prefix, 20 new
  lines carry the repo-relative path); 0 absolute paths remain in
  staged scripts; py_compile OK on all 28.
- Dry run re-verified after the fix (private test root, staged
  scripts at final placement, ROUTES.csv from staging-D1, harness
  from the device stage tree, out/ from this tree, WEMU =
  work-emulator): Currency 28 PASS, 0 FAIL, exit 0.
- D1 staging (staging-D1, unchanged from the audited bytes):
  device/routes/Currency/ROUTES.csv (6,393 B, CRLF line endings
  as audited — valid CSV, parsed by drycheck without issue) +
  ROUTES_NOTES.md (10,808 B); 0 absolute paths, 0 tick-marker
  hits. Branch check before push: device/routes/Currency/
  ROUTES.csv absent from work-2026-10-31.
- D1 push: see continuation report (commit recorded there).
- D1 push LANDED 2026-11-01 (continuation #2): commit
  260d62f69fd85b9cfbd355565906ea5337c197bb (parent e93c5c1e Aegis
  C3), device/routes/Currency/ROUTES.csv (6,393 B, CRLF) blob
  c8dadfe02f3d4df5cacbe547d19bd0de661fef2d + ROUTES_NOTES.md
  (10,808 B) blob ef0dd9f2be849fc44b0d9c1dca41874db824eac0, both
  read-back verified exact (local git hash-object match).
- D3 push: 28 scripts + 28 route_print files + this AGENT_NOTES
  update, under the push lock, verified by read-back (commit
  recorded in the continuation report).
