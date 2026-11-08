# AnkiDroid fix log — Stream A (user order 2026-11-02 ~00:25 EST, A1)

Fixes the 18 first-draw WRONG routes IN THE GRAPH (B6 step 5), in one
combined build. Three independently audited designs, each re-audit PASS
(defect list empty), translated into drop-in fragments by implementation
helpers (merger tree and branch never touched by helpers):

- Dialog/hook variants (routes 05, 07, 19): helper/apply-dialog/02-dialog.py
  (33 e() calls). @101 chain (05, 17 steps), @SELECT chain (07, 14 steps),
  @advancedStatistics chain (19, 35 steps on the real build; design table
  said 34 — the 1-edge delta is the Reviewer head, see below).
  Generic getText1 -> totalRev (E0ca39dd5) and generic getImportableDecks
  (Ee61e1dd8) suppressed with NO restoration; generic runFilter
  (E70b0401a) suppressed; MG943 verbatim on the dispatch guard.
  Dialog tie: the @101 chain won on the real build (variant first).
- DeckTask/Connection split (routes 01, 04, 12, 20, 22, 23, 30, 02):
  helper/apply-decktask/02-decktask.py (227 e() calls: 50 entry edges for
  51 launch lines, 34 body edges, 108 post-chain edges, 28 progress-chain
  edges) + EDIT-wrapper-decktask.py appended to graph_def.py AFTER the
  B6 wrapper (never in a mod file: the mod loader runs before the B3/B6
  EDIT definitions). Connection: single SYNC entry (Connection.sync) and
  single LOGIN entry (MyAccount.login, call at MyAccount.java:140).
- Best-route Set G (routes 03, 13, 14, 18, 21, 26, 28):
  helper/apply-bestroute/02-bestroute.py (28 base sup() pairs + 28 D1
  @-variant sup() pairs + 6 NEW producer ASYNC edges + $24 suppression +
  fragmented summary edge + receiver-variant entry + Previewer for-result
  split + route-21 summary edge + route-14 Option A suppression, the last
  acceptance-gated). D1 apply-time fix: sup() on a base TaskListener pair
  does NOT kill its @-variant copies (variant edges are separate
  auto_calls.json entries), so all 28 @ pairs are listed explicitly.

Assembled as graphs/AnkiDroid/graph_def_mod/02.py (2048 lines, 143,809 B
before the IMPORT fix below; py_compile passes; 0 tick markers).
Hand deletions a fragment cannot do (applied with replacement comments):

- graph_def_mod/01.py part 100: Stats.calculateDue -> AdvancedStatistics.runFilter
  (Edf6d8bd0) deleted — replaced by the @advancedStatistics path.
- graph_def_mod/01.py part 137: three base-onCreate Reviewer edges deleted
  (Ee2fb37d3 onCollectionLoaded, E3e5784f2 restorePreferences, Ea1ef11ff
  getContentViewAttr) — replaced by Reviewer.<init> ->
  AbstractFlashcardViewer.onCreate@Reviewer -> Reviewer.onCollectionLoaded
  (auto edges carry restorePreferences/getContentViewAttr).
- graph_def.py: CardBrowser.<clinit> -> CardBrowser.<init> (Eefecf867) deleted
  (route 13; a static call triggers <clinit> but never constructs an
  Activity; INTENT edges from openCardBrowser cover launch).
- graph_def.py: S_PREVIEWER -> CardTemplateEditor$CardTemplateFragment
  .onActivityResult (Eb9d6a916) deleted — MOVED, not copied, to
  S_PREVIEWER_FORRESULT (route 18; generic page must lose it or the
  CardBrowser plain-startActivity shortcut survives).

## Build proof (combined build, second build after the IMPORT fix)

- Command: python3 -I tools/build_graph.py "graphs/AnkiDroid" ankidroid
  (TMPDIR under ~/workspace; /tmp is full).
- Baseline (pre-Stream A): methods 4186, pages 48, edges 9183,
  REACHABLE 3275, UNREACHABLE 911, errors 0, warnings 0.
- Stream A build 1: methods 4186, pages 49, edges 9604, REACHABLE 3274,
  UNREACHABLE 911, errors 1, warnings 1. The error was
  DeckPicker$5.onProgressUpdate stranded (no path, no UNREACHABLE entry).
  Root cause: variant progress hand edges (onProgressUpdate@T ->
  TaskListener@T) suppress, by base-pair hand-covering, the auto edge
  DeckTask.onProgressUpdate -> DeckTask$TaskListener.onProgressUpdate
  (Eb7581a2a), the base TaskListener's only entry; the DeckTask fragment
  wrote no IMPORT progress chain ("its progress goes via doProgress"),
  so the IMPORT listener $5 lost its only route. The baseline $5 route
  was itself a fiction (RENDER_BROWSER_QA launch -> ... -> $5), so this
  was a design gap, not a regression to restore.
- Stream A build 2 (final for this log): methods 4186, pages 49
  (+1 S_PREVIEWER_FORRESULT), edges 9608, REACHABLE 3275, UNREACHABLE 911,
  errors 0, warnings 1. The single warning is the stale verification.csv
  (Template$1.compare path no longer best) and clears on A4 regeneration.
- Checks on build 2: check 2 (check_citations.py) 274 distinct, 0 problems;
  check 3 (check_routes.py) 0 routes flagged; check 4
  (check_bytecode_lines.py) 7033 checked, 0 where the cited line does not
  show the callee. No label flips vs baseline (3275/911 throughout).

## Merger fix: IMPORT progress chain (audited before merge)

Appended to graph_def_mod/02.py (2 hand edges, mirroring the
IMPORT_REPLACE chain in the DeckTask fragment):

- DeckTask.doProgress -> DeckTask.onProgressUpdate@IMPORT (ASYNC;
  evidence DeckTask.java:750, 1320-1350, 1348-1349, 352-355).
- DeckTask.onProgressUpdate@IMPORT ->
  DeckTask$TaskListener.onProgressUpdate@IMPORT (CALL; evidence
  DeckTask.java:352-355, 1311-1312).
- TaskListener@IMPORT -> DeckPicker$5.onProgressUpdate arrives by auto
  fan-out and stays CALL (Eda073348) under the EDIT wrapper's existing
  _PROG_LISTENERS['IMPORT'] = {DeckPicker$5.onProgressUpdate} allowance;
  all other variant copies to $5 are REGISTER.
- Genuine path (printed source): doInBackgroundImportAdd builds the only
  ProgressCallback in the source root (DeckTask.java:750);
  ProgressCallback.publishProgress calls task.doProgress (:1340-1342);
  doProgress calls publishProgress (:1348-1349); AsyncTask dispatches
  onProgressUpdate (:352-355) to the registered listener (:1311-1312).
  Resulting $5 path: DeckPicker.importAdd -> doInBackground@IMPORT ->
  doInBackgroundImportAdd -> AnkiPackageImporter.run ->
  Anki2Importer.publishProgress -> ProgressCallback.publishProgress ->
  doProgress -> onProgressUpdate@IMPORT -> TaskListener@IMPORT -> $5.
- Deliberately NOT done: restoring the base onProgressUpdate ->
  TaskListener edge would restore the base TaskListener fan-out (any
  publishing body reaching every progress listener) and break the
  ANSWER/DISMISS distinction for route 12. Base TaskListener
  .onProgressUpdate still has no entry in build 2.

## New BFS routes for the 18 fixed targets (from build 2 methods.csv)

All 18 targets are REACHABLE with genuine BFS routes; no genuine edge was
suppressed to force any of them. Design YES predictions that match
exactly: 02 (20 edges, onResume head, @SYNC), 03 (12, filtered-deck),
05 (17, @101), 07 (14, @SELECT), 13 (37, Reviewer head),
14 (10, initPreference — Option A, NOT the 9-edge page-GUI route),
18 (34, Reviewer head + for-result tail), 21 (14), 26 (12, route A),
28 (23, onActivityResult — ruling (ii)). Design NOs resolved by
re-judgement of the genuine BFS route (coordinator decision; merger
recommends re-judge, never suppression):

- 01 Phrase.<init> (38): Reviewer-head GUI chain to TranslationActivity
  (tail from S_CARDBROWSER matches C01 steps 17-36). Design predicted a
  28-edge drawer head; the real BFS prefers the Reviewer head because
  STRICT ranks (env kinds, state kinds, steps) and the Reviewer head
  carries 1 env kind (network) vs the drawer head's 2 (permission +
  network). Same mechanism explains 04, 19 (+1 edge vs design table),
  and 23.
- 04 Stats$1.compare (26): Reviewer-head chain, Statistics tail matches
  C04 (HOURLY_BREAKDOWN, sort at Stats.java:852-859). Design drawer 17.
- 12 Sound.notifyConfigurationChanged (24): Reviewer.onOptionsItemSelected
  -> playSounds (SRC Reviewer.java:152 bytecode) -> Sound chain ->
  VideoPlayer -> onConfigurationChanged -> target. The design's ANSWER
  progress chain still exists ($10 via @ANSWER), but BFS finds the
  shorter playSounds-direct route; no suppression involved.
- 19 AdvancedStatistics$Card.setIvl (35): @advancedStatistics chain won;
  prefix is the Reviewer head (1 edge longer than the design's 24-edge
  drawer prefix), tail matches the design's 7-edge tail + dispatch.
- 20 DiffEngine.diff_cleanupSemanticScore (24): Reviewer.onKeyUp ->
  displayCardAnswer@Reviewer -> typeAnsAnswerFilter -> diff chain
  (type-answer route, as designed).
- 22 libanki.Utils.base62 (21): CHECK_MEDIA route — DeckPicker.sync ->
  $17.onPostExecute -> showSyncErrorDialog (DeckPicker.java:1495) ->
  S_DLG_SYNC_ERROR_MEDIA -> mediaCheck (SyncErrorDialog.java:209-210) ->
  doInBackground@CHECK_MEDIA (DeckPicker.java:1191) -> Media.check ->
  _normalizeNoteRefs -> getNote -> Note.<init> -> guid64 -> base91 ->
  base62. Genuine; the design's enumerated NoteEditor (29) / provider
  routes are longer. Merger recommends re-judge of this route.
- 30 Models._availClozeOrds(JSONObject,String,boolean) (14): Storage
  upgrade route (0,0,14) — CollectionHelper -> Storage.Collection ->
  Storage._upgrade -> Models.save -> _syncTemplates -> genCards ->
  availOrds -> _availClozeOrds. Provider QUERY (1,0,6) exists as a
  non-best derivation (loses on env kinds). Fallback: keep C30 with a
  BFS caveat, as the current table does for 13/21/26/28.

## Redraw (A2) — see route_table.md for the final-draw judgements

- Command: python3 -I tools/verify_sample.py AnkiDroid 30 20261025 >
  graphs/AnkiDroid/scratch/sample_30.txt (on build 2).
- Final draw: 30 methods, 325 distinct edges. 16 carry over from the
  first draw; typeAnswer returns from the post-B6 redraw set; 13 are new
  to this draw (incl. DeckPicker$5.onProgressUpdate, the IMPORT fix
  route). Dropped first-draw methods (14): 03, 05, 08 ($1), 11, 15, 16,
  17, 21, 23, 24, 26, 28, 29, 30 — their targets remain REACHABLE.
- Judgements by three helpers (routes 01-10, 11-20, 21-30) + one
  independent auditor for the full table before merge (audit-before-merge).
