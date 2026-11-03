# AnkiDroid 2.6beta6: method-level trigger graph (schema 2)

How every method of **AnkiDroid** is triggered, in the standard configuration: the instrumented debug build (`tingsu/Anki-Android@instrumented-version-2.6beta6`, commit `58725f6db609`, APK sha256 `e21f15cb...`), an API 27 emulator, permissions and fixtures as in `final_java_only`. Labels follow `handoff/SCHEMA_V2.md`: REACHABLE or UNREACHABLE, ENV and STATE gates, edge classes (explicit, standard, non-standard), and how each label was confirmed.

## What is in this folder

| File | What it is |
|---|---|
| `ankidroid_trigger_graph.json` | pages, methods, `verdict`, `labels` (per-method fields), `edges` (with `edge_class`, `env_kinds`, `state_kinds`, stable ids), `paths` (verified paths only), `verification` (counts) |
| `methods.csv` | one row per method: verdict, UNREACHABLE reason, ENV and STATE kinds and texts, edge classes on the best route, whether an explicit/standard-only route exists, how the label was confirmed, path status, and the derived best route (`shortest_path`, `route_edge_ids`) |
| `../verification.csv` | the audit log: one row per label, edge or path that was checked, with result, how, and where (file:line) |
| `sanity_check.csv` | tool coverage (Monkey / APE, API 27) next to the labels; a one-way check only, it never sets a label |
| `ankidroid_trigger_graph.html`, `build_report.txt` | the viewer and the validation report |

## Numbers

- **4186 methods**, **56 pages** (including pseudo pages), **9815 edges**. Verdicts: **3275 REACHABLE**, **911 UNREACHABLE**.
- UNREACHABLE by reason: branch_never_taken 48, closed_by_api_level 44, closed_by_configuration 22, framework_never_calls 48, no_trigger_in_app 749.
- ENV gates (methods): hardware 78, network 68, other 10, other_app 93, permission 439, system_event 19. STATE gates (methods): account 14, data 2033, file 274, session 18, settings 70. Methods with no gate: 1016.
- Edge classes: explicit 8599, non_standard 25, page 81, standard 1110. Non-standard edges: 25 (Apache HttpClient 4.x DefaultHttpClient.execute (library source not read); Apache HttpClient 4.x DefaultHttpClient.execute, DefaultClientConnectionOperator (library source not read); Apache HttpClient 4.x DefaultHttpClient.execute, LayeredSocketFactory (library source not read); Apache HttpClient 4.).
- 27 reachable methods have a non-standard edge on their best route; 27 have no explicit-or-standard-only route at all.
- Labels confirmed by: INFERRED 261, SOURCE 3925 (SOURCE: every edge of the best route cites a source line, in the app or in the Android 8.1 / library source; INFERRED: some edge rests on inference or on another app).

## How much to trust it

Verification log (`verification.csv`), counts of what was checked and found:

| Checked | Rows | Correct | Errors found (fixed) | Unclear |
|---|---:|---:|---:|---:|
| labels | 941 | 938 | 3 | 0 |
| edges (framework and other claims read against source) | 232 | 232 | 0 | 0 |
| paths (stratified sample, read step by step) | 30 | 27 | 3 | 0 |

Device replay on the emulator (API 27): 0 of 30 routes reached their target method; 0 of these ran the whole script and are `DEVICE_OK`. The other routes are unclear (not reached, script stopped, or unscriptable), never wrong; see `../device/results.csv`.

Path status over all reachable methods: SOURCE_OK 20, UNCHECKED 3252, WRONG 3.
The rows are the items that were individually checked, not a random sample of all labels; see the notes below for how they were chosen and what the unclear rows wait for.

Edges whose evidence is not a source line (75 of 9815): E9509db65 (S_ENTRY -> AnkiDroidApp.onCreate); E1af92d11 (S_ENTRY -> CardContentProvider.onCreate); Ea208d220 (AnkiDroidApp.<init> -> AnkiDroidApp.onCreate); E1672b7a2 (StudyOptionsFragment.<init> -> StudyOptionsFragment.onAttach); Ee3b9f7fe (StudyOptionsFragment.onAttach -> StudyOptionsFragment.onCreateView); E1210f896 (StudyOptionsFragment.onCreateView -> StudyOptionsFragment.onResume); Ee7300d2c (CardBrowserContextMenu.<init> -> CardBrowserContextMenu.onCreateDialog); Ee2ff47c1 (CardBrowserMySearchesDialog.<init> -> CardBrowserMySearchesDialog.onCreateDialog); Ef6c16a28 (CardBrowserOrderDialog.<init> -> CardBrowserOrderDialog.onCreateDialog); Ef71a2817 (ConfirmationDialog.<init> -> ConfirmationDialog.onCreateDialog); E90f59cc0 (CustomStudyDialog.<init> -> CustomStudyDialog.onCreateDialog); Ebcff9edf (DatabaseErrorDialog.<init> -> DatabaseErrorDialog.onCreateDialog) ...

Sanity check against tool coverage (never used to set a label): 2011 methods ran in the 1-hour Monkey / APE runs on API 27; **1** of them are labelled UNREACHABLE.

## What the re-audit changed (compared with the schema 1 graph)

- STRICT mode on (B1, graph_def.py line 10: STRICT = True).
- Check 2 (B2): the 3 NotificationService citation problems were a
  checker-regex artefact (tools/check_citations.py ROOT_STYLE matches the
  services/NotificationService.java:<digits> substring inside the full-path
  citation). Fixed on the citation side only, keeping the full path and
  writing line numbers in words (:47 -> (line 47), :46-54 -> (lines 46-54),
  :37 -> (line 37)). Check 2 is now 0 problems (274 distinct on the
  Stream A graph).
- Check 4 (B3): one combined EDIT (single EDIT definition) fixes all 48
  bytecode lines from the checker's own keys: 23 TaskData/ChartBuilder/
  DisplayPair line moves + 18 libanki Utils path pins (bare Utils.java ->
  com/ichi2/libanki/Utils.java) + 7 MockNoteFactory INFERRED rewrites
  (source under multimediacard/test/ is pruned from the checker source
  index; it is NOT absent from the upload). Check 4 is now 0 not-show
  (7033 checked on the Stream A graph, with the disclosed caveat that
  the 23 B3-a edges drop out of the checker's checked set because their
  "(bytecode line was N)" form does not match its pattern; verification
  rests on printed lines and auditor re-prints).
- Check 8 (B4): all 169 scan lines explained in
  scratch/check8_explained.md (106 sibling-only + 52 remainder-only +
  11 mixed). The paint-sync helper's "8 NEW entries" already existed in
  graph_def_mod/01.py sup() blocks (VERIFY-ONLY, never duplicated); one
  ReliefLegend reason reworded (getLegend has no caller and ReliefDrawer
  itself is never constructed).
- Route checks (B6): no label changes (REACHABLE 3275, UNREACHABLE 911
  throughout). Fixes are guard/evidence additions, two variant-page
  splits (SyncErrorDialog NOT_LOGGED_IN/MEDIA; ConfirmationDialog
  FULLSYNC/RENAME/NOTEEDITOR_CHANGETYPE), and audited corrected
  derivations for the 18 WRONG routes. Final graph: methods 4186,
  pages 48, edges 9183, errors 0, warnings 0.
- Route checks (Stream A, user order 2026-11-02 ~00:25 EST): the 18
  first-draw WRONG routes fixed IN THE GRAPH in one combined build —
  DeckTask/Connection variant split (34 task types, EDIT wrapper chained
  after the B6 wrapper), dialog-id variants (@101, @SELECT) and
  hook-name variants (@advancedStatistics), best-route Set G (TaskListener
  suppression incl. @-variant pairs, receiver-variant Reviewer entry,
  Previewer for-result split), plus a merger IMPORT progress chain
  (doProgress -> onProgressUpdate@IMPORT -> TaskListener@IMPORT ->
  DeckPicker$5.onProgressUpdate) that restored one stranded method with
  no label change. Stream A graph: methods 4186, pages 49, edges 9608,
  REACHABLE 3275, UNREACHABLE 911, errors 0, warnings 1 (stale
  verification.csv only, cleared by regeneration). Checks 2/4 at 0.

## How the checked paths were chosen

- `python3 -I tools/verify_sample.py AnkiDroid 30 20261025` on the
  Stream A graph: 30 of 3275 REACHABLE methods, stratified
  (NONSTD 4, INFERRED 4, STATE 3, ENV 6, LONG 6, PLAIN 7), spreading over
  route edges (325 distinct edges). Every route was printed with its
  edge ids and evidence and judged step by step against printed source
  (including if/catch/for conditions) by three helpers (routes 01-10,
  11-20, 21-30), and the full table was independently audit-PASS before
  merging (including a ruling that route 08's genuine-INFERRED final
  step sustains CORRECT).
- The route table (scratch/route_table.md) covers the FINAL-draw 30
  routes (this draw supersedes the first-draw table: WRONG 18, FIXED 9,
  UNCLEAR 2, CORRECT 1; first-draw error rate 27/28 = 0.9643, kept as
  history): CORRECT 20, WRONG 10, UNCLEAR 0; final-draw error rate
  10/30 = 0.3333. For CORRECT routes the table route is the final BFS
  route (the fix is in the graph). For WRONG routes the table route
  is the audited corrected derivation, and each WRONG names the tools/
  builder limitation that makes the builder print the fiction
  (receiver/producer-unaware dispatch, branch-insensitive constructor
  routing, token-unaware query routing, dialog-id-unaware shared
  pages). verification.csv path rows use the built (BFS) route's edge
  ids with the audited verdict, and their notes point at the corrected
  derivation for WRONG routes.
- Work-order rate (combined-merge redraw, step 2 item 3): rate =
  (fixed + wrong) / (correct + fixed + wrong), where fixed means
  WRONG in an earlier draw AND CORRECT in the final draw (the
  Aegis definition), correct means the final-draw CORRECT count
  (27, which includes the fixed routes), and wrong means the
  final-draw WRONG count (3). Fixed routes (5, verified against
  both the earlier-draw table and the final table, in final-table
  row order): HttpFetcher.downloadFileToSdCardMethod (row 12, 37
  steps), Models$TransformFieldDelete.<init> (row 16, 21 steps),
  Sched.getToday (row 21, 18 steps), DB.insert (row 25, 11 steps),
  SimpleMessageDialog.<init> (row 29, 10 steps). Arithmetic:
  (5 + 3) / (27 + 5 + 3) = 8 / 35 = 0.2286 (approx). This
  supersedes the 3 / 30 = 0.1000 figure, which used the WRONG /
  (CORRECT + WRONG) definition; scratch/route_table.md has been
  updated to this definition (no verdict changed).
- Corrected rate (round 2, user order 2026-11-02): rate =
  (fixed + wrong) / (correct-only + fixed + wrong), where fixed
  means WRONG in ANY earlier draw (first draw at 3213cea2 included)
  AND CORRECT in the final draw, correct-only means CORRECT in the
  final draw and never WRONG in any earlier draw, and each route is
  counted once. Fixed routes (13, verified mechanically against the
  first-draw table, the earlier-draw table, and the final table):
  Phrase.<init>, EasyX509TrustManager.<init>, Stats$1.compare,
  libanki.Utils$1.<init>, Finder.findNotes,
  HttpFetcher.downloadFileToSdCardMethod,
  Sound.notifyConfigurationChanged,
  Models$TransformFieldDelete.<init>, Sched.getToday,
  AdvancedStatistics$Card.setIvl,
  DiffEngine.diff_cleanupSemanticScore, DB.insert,
  SimpleMessageDialog.<init>. Correct-only 14, wrong 3 (rows
  09/18/28). Arithmetic: (13 + 3) / (14 + 13 + 3) = 16 / 30 =
  0.5333 (approx). This supersedes the 8 / 35 = 0.2286 figure,
  which double-counted the fixed routes inside correct. Row-08
  contingency: row 08's method ModelEditorContextMenu.onCreateDialog
  is correct-only (UNCLEAR in the first draw, CORRECT in the earlier
  draw, never WRONG), so if it flips to UNCLEAR the rate becomes
  (13 + 3) / (13 + 13 + 3) = 16 / 29 = 0.5517 (approx).

## What waits for a device (API 27)

- **Device run 41593209101-1 (2026-11-03, Google APIs, API 27, x86).** 0 of 30 routes reached their target method; 0 of them ran the whole script and are now `DEVICE_OK`. The other routes are unclear (not reached, script stopped, or unscriptable), never wrong; the reason for each route is in `handoff/DEVICE_RUN_SUMMARY.md`. What is listed below still waits for a device.

- Device preparation (D1/D3) is separate from this log work: the final
  sample's 30 routes need device/routes/AnkiDroid/ROUTES.csv and one
  script per scripted route, plus DEVICE rows in make_verification.py,
  before the CI device dry run (D9). No device run has been made in
  this run (no emulator/adb use); the user runs
  .github/workflows/device-replay.yml later.
- Routes whose table route is a corrected derivation (the 10 WRONG
  routes of the final draw) must be scripted from the CORRECTED route,
  not from the BFS route: route 11 from the CustomStudyDialog
  REBUILD_CRAM launch; route 12 from Reviewer.openCardBrowser;
  route 14 from ModelFieldEditor deleteFieldDialog; route 20 from
  NoteEditor new-note creation; route 23 from a filtered deck whose
  terms[0] contains is:due; routes 24 and 30 from the collection-open
  check-database prefix (menu action_check_database -> CONFIRM
  dialog); route 25 from ERROR_HANDLING -> restore -> RESTORE_BACKUP;
  route 27 from ERROR_HANDLING -> repair -> REPAIR dialog; route 28
  from the Reviewer ANSWER_CARD launch with mAnswerCardHandler.
  CORRECT routes are scripted from their BFS routes.

## Hazard candidates (from reading the code, not reproduced)

- Card.toString is UNREACHABLE (no_trigger_in_app) but ran in a tool
  run (coverage_baseline.json; the build's sanity check still reports
  this contradiction). The label is unchanged: the contradiction is a
  candidate for a future caller hunt, not a flip on coverage alone
  (labels come only from printed source).
- The graph's best-route finder does not evaluate guard text against
  actual arguments: for routes 13, 21 and 30 the BFS best route still
  shows a guard-inconsistent prefix even after the fix (dispatch chain
  wins on cost for route 13; the old DeckPicker prefix for route 30).
  A guard-checking redraw must reject those prefixes in favour of the
  corrected routes in route_table.md; this is a cost-model limitation,
  not a reason to split or suppress edges without a separate audited
  proposal.
- The builder does not deduplicate hand edges with the same
  (src, dst, kind) but different guards: the combined graph contains
  both the F4 and F5 hand edges for DeckPicker.onCreate ->
  CollectionHelper.exceededCursorSizeLimit and for
  CollectionHelper.getCol -> Storage.Collection (both guards true for
  the same call sites). No label or route effect; recorded in
  route_table.md.

## Limits

- Check 5 counts the schema-1 DEAD/FRAMEWORK_ONLY container lines and
  SUPPRESS lines in graph_def.py / graph_def_mod/01.py; they are
  temporary containers converted to UNREACHABLE entries, not placeholder
  labels. Greps for DEAD|FRAMEWORK_ONLY, FW-MEMORY and PENDING are
  reported in the CI SUMMARY; the PENDING count is 0 in the final graph
  files (see the B6 build record).
- The final draw differs from the first-draw sample (16 carry over,
  typeAnswer returns from the post-B6 redraw set, 13 new, 14 drop out;
  325 vs 299 distinct edges) because the sampler spreads over
  route_edge_ids, which change when fix edits change edge ids, and
  because Stream A added ENV/STATE kinds to more methods. This table
  covers the final draw per the merger's assigned task (Stream A A3);
  the first-draw table is superseded history. Of the 5 post-B6
  redraw-only methods, typeAnswer IS judged here (final-draw route 28,
  WRONG with a corrected ANSWER_CARD route); the other 4
  (CardTemplateEditor$CardTemplateFragment$4.<init>, Info.copyDebugInfo,
  BackupManager.deleteDeckBackups,
  CustomTabsHelper.hasSpecializedHandlerIntents) are not in the final
  draw and remain unjudged; their targets remain REACHABLE.
- Final-draw verdicts: CORRECT 20, WRONG 10, UNCLEAR 0. Route 08
  (ModelEditorContextMenu.onCreateDialog) is CORRECT under the
  genuine-INFERRED convention (support-v4 lifecycle dispatch, final
  step at ModelEditorContextMenu.java:31), as ruled by the table audit;
  the first-draw UNCLEAR precedent for this method is disclosed in
  route_table.md, not copied. The first-draw route 08
  (SimpleMessageDialog$1.<init>, UNCLEAR, $15 -> $16 rename held on
  bytecode proof) is not in the final draw. All 30 final-draw targets
  remain REACHABLE (no label was changed by any route verdict).
- tools/show_route.py crashes on multi-citation lifecycle edges; this
  is pre-existing (identical on the unmodified baseline) and tools/
  was not edited. The merger used its own dump methods for those
  routes.

## JSON shape (short)

```
{ "schema": 2, "title", "screens": {page: description}, "methods": [...], "verdict": {method: REACHABLE|UNREACHABLE},
  "labels": {method: {unreachable: {kind, text}, env: [{kinds, text}], state: [{kinds, text}], route_edge_classes, explicit_standard_route,
                      confirmed_by, source_ref, path_status}},
  "edges": [ {id, src, dst, kind, edge_class, via, trigger, gui[], guard, reads[], writes[], note, needs_state, state_kinds, env, env_kinds, evidence, class_basis} ],
  "paths": [ {method, edges[], edge_classes, explicit_standard_only, env, state, verified_by, ref} ], "verification": {...} }
```

`src`/`dst` are methods (`Class.method`, overloads as `Class.method(Type,Type)`) or pages (`S_...`). A suffix `@CONTEXT` is the same method or page in a specific context. Edge ids are a hash of the edge content, so they stay stable when other edges change.
