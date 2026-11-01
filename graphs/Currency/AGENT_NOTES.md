# Currency — agent notes (finish run, branch work-2026-10-31)

Ticked app: log work only. No label, edge, route, or graph_def.py change
is made here, and the PROGRESS line stays exactly as it is.

## Current step

T1 writer done and tested (see below); D1 ROUTES.csv verified and
adopted; D3 route scripts in progress (helpers); D7 DEVICE support in
the writer, tested on synthetic results. CI request for Currency is the
coordinator's step (coordinator-only); F1 readiness is reported to the
coordinator with the evidence below.

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
- No other decisions. Batch 5 rows 19/20/25/26 (user decision D29) do
  not concern Currency.
