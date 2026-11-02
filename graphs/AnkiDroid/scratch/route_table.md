# AnkiDroid route table — FINAL draw (seed 20261025), after Stream A fixes

Sample: `python3 -I tools/verify_sample.py AnkiDroid 30 20261025` on the
Stream A graph (methods 4186, pages 49, edges 9608, REACHABLE 3275,
UNREACHABLE 911, errors 0, warnings 0 — the single stale
pre-Stream-A verification.csv warning was cleared by regeneration in A4). Sample file:
`graphs/AnkiDroid/scratch/sample_30.txt` (30 of 3275, 325 distinct edges
on the Stream A graph). This table REPLACES the first-draw table: it
covers the final draw only, as ordered for Stream A (A3).

Verdicts are the AUDITED final-draw judgements (helpers judge-01-10,
judge-11-20, judge-21-30, each step checked against printed source; full
step tables in `helper/judge-final/judge-*/JUDGEMENTS.md`): CORRECT 20,
WRONG 10, UNCLEAR 0. Error rate = wrong / (correct + wrong) = 10/30 =
0.3333. There is no FIXED category in this draw: the Stream A graph
fixes are already in the graph, so a route whose printed steps are all
genuine is CORRECT, and a route with a fiction step is WRONG with its
corrected derivation below.

How to read the "steps" column: for CORRECT routes it is the final BFS
route's step count (the BFS route IS the judged route). For WRONG routes
it is the printed BFS route's step count (the BFS route is wrong; the
corrected derivation is the table route, from the judgement file cited).

WRONG and the tools/ clause (A3): every WRONG below is a route-builder
(tools/) limitation, stated per route. Stating a corrected route needs
no tools/ edit — each corrected derivation is built from printed source
edges. But making the BUILDER print the corrected route (instead of the
fiction) needs a tools/ change: the builder must become receiver-aware
for drawer/listener/interface dispatch, branch-aware for constructor
branches, and dialog-id-aware for shared dialog pages (see the per-route
reasons). Per-route graph_def patches are NOT applied here: they would
change edge ids, and the sampler spreads over route_edge_ids, so the
sample would move again. The graph fixes in Stream A (A1) were for the
18 first-draw WRONG routes; these 10 final-draw WRONGs are recorded with
their corrected routes, as the first-draw table did.

Composition vs the first draw: 16 methods carry over (Phrase,
EasyX509TrustManager, Stats$1.compare, libanki.Utils$1,
ModelEditorContextMenu, Template$1.compare, Sound, HttpFetcher,
Preferences.replaceString, Finder, AdvancedStatistics$Card.setIvl,
DiffEngine, libanki.Utils.base62, MetaDB, CollectionLoader, Decks.id);
AbstractFlashcardViewer.typeAnswer returns from the post-B6 redraw set;
13 are new to this draw (Sched._cntFnNew, Sched.revDue,
MediaCheckDialog$3, StudyOptionsActivity.closeStudyOptions,
Models$TransformFieldDelete, Anki2Importer._mediaPick,
DeckPicker$5.onProgressUpdate, Sched.sortCards, Sched.getToday,
DB.insert, BaseAsyncTask.onProgressUpdate, Collection.close(),
SimpleMessageDialog.<init>). 14 first-draw methods drop out of this draw
(StepsPreference, Sched.totalRevForCurrentDeck, SimpleMessageDialog$1,
FilteredDeckOptions, api.Utils.entsToTxt, Sched.haveBuried,
ModelFieldEditor$6$1, CustomTabsFallback, CardTemplateEditor$3, Hook,
ModelFieldEditor$1, NoteEditor.closeNoteEditor, DB.executeScript,
Models._availClozeOrds) — every one of them remains REACHABLE on the
Stream A graph; dropping out of a sample is not a label change.

Route-08 flag (auditor ruling owed): final-draw route 08
(ModelEditorContextMenu.onCreateDialog) is judged CORRECT here, but the
same method was UNCLEAR in the first draw (route 06) because its final
`<init> -> onCreateDialog` step has no printed framework evidence and
stays INFERRED (support-v4 DialogFragment source absent from the tree).
The final-draw judge marks that step genuine-INFERRED (the fragment's
own onCreateDialog is printed at ModelEditorContextMenu.java:31, and
support-v4 lifecycle calls it once the fragment is shown) and therefore
CORRECT, the same genuine-INFERRED convention used for route 02's Apache
dispatch and route 01's Gson step. If the table auditor rules UNCLEAR,
this row flips to UNCLEAR with no other change (totals become
CORRECT 19, UNCLEAR 1, error rate 10/29 = 0.3448).

Binding constraints carried from the first-draw table (still in force):
single EDIT definition (B3 EDIT chained through F3 and F2 wrappers and
the Stream A DeckTask wrapper, never replaced); no $16 edge for
SimpleMessageDialog (bytecode: $15 = CHECK_DATABASE, $16 = CHECK_MEDIA);
no suppression of the 16 confirm + 8 cancel dispatch edges;
BackgroundPost Ecba7dfd7 stays ENV_NETWORK; the direct hand edge
Stats.calculateDue -> AdvancedStatistics.runFilter (Edf6d8bd0) stays
deleted (route 19 runs only via @advancedStatistics).

| # | method | verdict | steps | reason / corrected route |
|---|---|---|---|---|
| 01 | Phrase.<init> | CORRECT | 38 | All 38 steps genuine. Reviewer-head GUI chain (StudyOptionsFragment -> Reviewer -> drawer -> CardBrowser -> NoteEditor media button -> multimedia field editor -> Glosbe translate -> TranslationActivity.showPickTranslationDialog -> Phrase). Final Gson step stays INFERRED (reflective construction, no printed Gson source), as in C01. Condition: cards due. |
| 02 | EasyX509TrustManager.<init> | CORRECT | 20 | All 20 steps genuine. SYNC task via the onResume head (DeckPicker.sync -> sync(String) -> Connection.sync -> doInBackground@SYNC -> doOneInBackground@SYNC -> doInBackgroundSync -> Syncer -> RemoteServer -> HttpSyncer.req chain -> EasySSLSocketFactory -> EasyX509TrustManager). Steps 17-20 are library-INFERRED (Apache Commons HttpClient absent from the tree; dispatch unavoidable once the https scheme is registered with that factory). Condition: logged-in hkey + online. |
| 03 | Stats$1.compare | CORRECT | 26 | All 26 steps genuine. Reviewer-head chain to Statistics chart (HOURLY_BREAKDOWN case at Statistics.java:503, not :514; checkAndUpdate -> createChart requires the created/measured/changed guard), sort at Stats.java:852-859, JDK-sort dispatch INFERRED (java.util not in fw_src). Condition: cards due. |
| 04 | Sched._cntFnNew | CORRECT | 15 | All 15 steps genuine as printed (full step table in judge-01-10). Condition: day rollover. |
| 05 | libanki.Utils$1.<init> | CORRECT | 14 | All 14 steps genuine. @SELECT dialog-id chain (DIALOG_IMPORT_SELECT entry -> ImportDialog -> getImportableDecks -> $1.<init>); the @SELECT split propagates unchanged through steps 8-12. |
| 06 | Sched.revDue | CORRECT | 16 | All 16 steps genuine as printed (full step table in judge-01-10). Evidence wording says androidx lifecycle; the tree imports android.support.v4.app.Fragment (e.g. StudyOptionsFragment.java:22) — dispatch is support-v4, still genuine-INFERRED. Condition: finished deck. |
| 07 | MediaCheckDialog$3.<init> | CORRECT | 16 | All 16 steps genuine as printed (full step table in judge-01-10). Condition: media-sync-server-error + check success; logged-in hkey + online. |
| 08 | ModelEditorContextMenu.onCreateDialog | CORRECT | 14 | All 14 steps genuine; final step genuine-INFERRED (support-v4 DialogFragment lifecycle, not androidx as the evidence says; onCreateDialog printed at ModelEditorContextMenu.java:31, called once the fragment is shown). Condition: model list loaded successfully (ModelBrowser onPostExecute requires result.getBoolean(), ModelBrowser.java:108-118). See the route-08 flag above: first-draw precedent was UNCLEAR for this step; auditor rules. |
| 09 | Finder.findNotes | CORRECT | 34 | All 34 steps genuine. Reviewer head + for-result tail: CardTemplateEditor starts Previewer with startActivityForResult, fragment onActivityResult unconditionally calls deleteDummyCards -> Collection.findNotes -> Finder.findNotes. Condition: cards due. |
| 10 | Template$1.compare | CORRECT | 17 | All 17 steps genuine. Steps 4-6 require a transient first-open failure followed by a successful retry inside exceededCursorSizeLimit -> getCol -> Storage.Collection; no printed line contradicts this. Condition: old schema + non-zero model id + multi-modifier absent-field template tag. (This also clears the stale verification.csv warning: the old Template$1.compare path is no longer best.) |
| 11 | StudyOptionsActivity.closeStudyOptions(int) | WRONG | 20 | Fiction at step 12 (E46c212fb, listener fan-out): the REBUILD_CRAM launch at StudyOptionsFragment.java:318 passes getDeckTaskListener(true) (StudyOptionsFragment.java:503-511+), whose onPostExecute only dismisses the dialog and refreshes views — it never calls onCreateCustomStudySession. The $4 listener that does (CustomStudyDialog.java:467) belongs to a different REBUILD_CRAM launch (CustomStudyDialog.createCustomStudySession, :455). Corrected route: steps 1-7, then custom-study menu item (StudyOptionsFragment.java:306-309) -> showCustomStudyContextMenu -> CustomStudyDialog -> createCustomStudySession (:421+) -> REBUILD_CRAM launch (:455) -> @REBUILD_CRAM -> $4.onPostExecute -> onCreateCustomStudySession -> openStudyOptions -> StudyOptionsActivity -> back press -> closeStudyOptions(int). Tools/ reason: the builder's @REBUILD_CRAM variant node conflates two listener instances from different launches; fixing needs producer-aware listener dispatch in tools/. |
| 12 | HttpFetcher.downloadFileToSdCardMethod | WRONG | 37 | Fiction at step 15 (Ea0eba485, wrong override): from a Reviewer receiver, nav_browser dispatches to Reviewer.openCardBrowser (Reviewer.java:508-518), not DeckPicker.openCardBrowser (DeckPicker.java:1707-1713, the cited evidence). Corrected route: identical except steps 15-16 relabelled to Reviewer.openCardBrowser -> CardBrowser.<init>; target still reachable. Tools/ reason: the builder's drawer dispatch is receiver-unaware (single onNavigationItemSelected node serves every activity); fixing needs receiver-variant dispatch in tools/. |
| 13 | Sound.notifyConfigurationChanged | CORRECT | 24 | All 24 steps genuine. Reviewer.onOptionsItemSelected -> playSounds (SRC Reviewer.java:152 bytecode) -> Sound chain -> VideoPlayer -> onConfigurationChanged -> target. Conditions: non-TTS replay, video sound with thumbnail, VideoPlayer's declared configChanges (AndroidManifest.xml:184). The design's ANSWER progress chain still exists ($10 via @ANSWER) but BFS finds this shorter genuine route. |
| 14 | Models$TransformFieldDelete.<init> | WRONG | 17 | Fiction at step 12 (Ef84c6616, shared-dialog page jump): ModelBrowser.deleteModelDialog's ConfirmationDialog confirm() calls deleteModel() (ModelBrowser.java:452-458, 470-476), never deleteField(). ModelFieldEditor$3.confirm (ModelFieldEditor.java:241-256) belongs to deleteFieldDialog in a different activity; the shared S_DLG_CONFIRMATION page let BFS jump activities. Corrected route: steps 1-6 to S_MODELBROWSER, then item click (ModelBrowser.java:271-280) -> ModelFieldEditor -> field context menu -> deleteFieldDialog (:235) -> $3.confirm -> deleteField (:279-283) -> @DELETE_FIELD -> remField -> TransformFieldDelete (guard: >=2 fields). Tools/ reason: shared dialog pages need dialog-id/activity-aware routing in tools/ (the B6 route-26 page splits show the graph-side pattern; the builder must not route one activity's dialog through another's confirm). |
| 15 | Anki2Importer._mediaPick | CORRECT | 16 | All 16 steps genuine as printed (full step table in judge-11-20). |
| 16 | Preferences.replaceString | CORRECT | 10 | All 10 steps genuine. InitPreference route (NOT the 9-edge page-GUI route): dir-inaccessible branch (DeckPicker.java:418-428) + initAllPreferences -> initPreference -> updateSummary -> replaceString, with a qualifying preference (Preferences.java:636). This is the Stream A Option A expectation. |
| 17 | DeckPicker$5.onProgressUpdate | CORRECT | 16 | All 16 steps genuine. The Stream A IMPORT progress chain: DeckPicker.importAdd -> doInBackground@IMPORT -> doInBackgroundImportAdd -> AnkiPackageImporter.run -> Anki2Importer.publishProgress (:89) -> ProgressCallback.publishProgress -> doProgress -> onProgressUpdate@IMPORT -> TaskListener@IMPORT -> $5 (DeckPicker.java:260-262). The importer does call the progress callback on the IMPORT path (callback installed with setProgressCallback at DeckTask.java:750, importer run at :751). |
| 18 | Sched.sortCards(long[],int,int,boolean,boolean) | CORRECT | 19 | All 19 steps genuine as printed (full step table in judge-11-20). Single consistent guard: includeSched=false. |
| 19 | AdvancedStatistics$Card.setIvl | CORRECT | 35 | All 35 steps genuine. @advancedStatistics variant chain (direct Stats.calculateDue -> AdvancedStatistics.runFilter edge deleted, correctly bypassed); hook installed only when pref advanced_statistics_enabled is on (Hooks.java:61-63); forecast tab (Statistics.java:485-488 -> ChartBuilder.java:73); 7-edge tail as designed. The 35th step vs the design's 34 is the Reviewer head (see fix_log.md). |
| 20 | libanki.Utils.base62 | WRONG | 21 | Fiction at step 19 (E62a24da3, guard-contradicted branch): Note.<init>(Collection,JSONObject,Long) calls guid64() only in the id == null (new-note) branch (Note.java:67-72); on the CHECK_MEDIA prefix the id is an existing note id from _normalizeNoteRefs -> getNote, so the constructor takes the load() branch and steps 20-21 (guid64 -> base91 -> base62) are unreachable there. The CHECK_MEDIA prefix steps 1-18 are genuine in isolation. Corrected route: NoteEditor new-note creation (CardBrowser action_add_card_from_card_browser, CardBrowser.java:630-634) -> NoteEditor.setNote(null) -> new Note(getCol(), model) (NoteEditor.java:1370) -> Note.<init>(Collection,JSONObject) -> Note.<init>(Collection,JSONObject,Long) with id == null (Note.java:58-60) -> else branch guid64 (Note.java:72) -> base91 -> base62. Tools/ reason: the builder routes every Note-constructor caller into both branches; fixing needs branch-sensitive (id-null vs id-set) constructor routing in tools/. |
| 21 | DiffEngine.diff_cleanupSemanticScore | CORRECT | 24 | All 24 steps genuine. Type-answer route: Reviewer.onKeyUp -> displayCardAnswer@Reviewer -> typeAnsAnswerFilter -> diff_main -> diff_compute -> diff_cleanupSemantic -> diff_cleanupSemanticLossless (DiffEngine.java:795 calls it) -> diff_cleanupSemanticScore. |
| 22 | MetaDB.getNotificationStatus | CORRECT | 14 | All 14 steps genuine as printed (full step table in judge-21-30). Support-v4-only dispatches marked genuine-but-INFERRED, never SOURCE, where the surrounding code makes the dispatch unavoidable. |
| 23 | Sched.getToday | WRONG | 18 | Fiction at step 18 (E594578a7, wrong branch): _fillDyn's query is user terms + -is:suspended -is:buried -deck:filtered (Sched.java:1569), and _findCardState calls getToday() only for val "due" (Finder.java:466-467); suspended/buried branches return constants (460-463). The printed route's query contains only is:suspended / is:buried / deck:filtered tokens, so getToday is never called on it. Corrected route: steps 1-17 exactly as printed, with the rebuilt dyn deck's first search term (terms[0], Sched.java:1558-1562) containing is:due, so _where -> _findCardState("due") (Finder.java:324, 465-467) -> getToday. Tools/ reason: the builder routes a query's tokens without checking which branch they select; fixing needs token-aware branch routing in tools/. |
| 24 | DB.insert | WRONG | 11 | Fiction at step 5 (Ea13b2167, wrong dialog id): the entered LOAD_FAILED dialog (DatabaseErrorDialog.java:76-96) has exactly two buttons, positive -> DIALOG_ERROR_HANDLING (85-91) and negative -> exit() (92-94); it has no button calling integrityCheck. Cited lines 294-302 are the different DIALOG_CONFIRM_DATABASE_CHECK dialog's onPositive, never shown on this prefix. Guard contradiction as well: ERROR_HANDLING's check_db option requires colIsOpen() (136-141), contradicted by the failed-load prefix (DeckPicker.java:414-433). Corrected route: collection-open prefix (DeckPicker menu action_check_database, DeckPicker.java:596-598) -> CONFIRM dialog -> onPositive -> integrityCheck (DatabaseErrorDialog.java:294-302) -> printed steps 6-11 (requiring orphan notes for _remNotes -> _logRem -> DB.insert). Tools/ reason: shared S_DLG_DATABASE_ERROR page needs dialog-id-aware routing in tools/ (same class as routes 25, 27, 30). |
| 25 | BaseAsyncTask.onProgressUpdate | WRONG | 11 | Fiction at step 5 (Ecfd88980, wrong dialog id): cited lines 251-270 are the DIALOG_RESTORE_BACKUP single-choice onSelection, never shown on the LOAD_FAILED prefix (whose buttons go only to ERROR_HANDLING or exit(), DatabaseErrorDialog.java:85-94). Corrected route: LOAD_FAILED positive -> ERROR_HANDLING -> select restore (value 3, always offered, :176-180) -> RESTORE_BACKUP dialog -> select a non-empty backup -> restoreFromBackup -> steps 7-11 (valid backup apkg required); or menu action_restore_backup (DeckPicker.java:617-619) -> CONFIRM_RESTORE_BACKUP -> RESTORE_BACKUP -> same continuation. Note the printed failed-load prefix also fails at step 10 (doInBackgroundImportReplace dereferences col.getPath(), DeckTask.java:758-762), so a usable collection context is required. Tools/ reason: shared dialog page needs dialog-id-aware routing in tools/ (same class as routes 24, 27, 30). |
| 26 | CollectionLoader.deliverResult | CORRECT | 11 | All 11 steps genuine as printed (full step table in judge-21-30). Support-v4 loader dispatch genuine-but-INFERRED, never SOURCE. |
| 27 | Collection.close() | WRONG | 10 | Fiction at step 5 (Ee8da2b4f, wrong dialog id): cited lines 207-212 are the DIALOG_REPAIR_COLLECTION onPositive -> repairDeck, not the entered LOAD_FAILED dialog (buttons only to ERROR_HANDLING or exit(), DatabaseErrorDialog.java:85-94). Corrected route: LOAD_FAILED positive -> ERROR_HANDLING -> select repair (value 2, requires sqlite3, :144-148) -> REPAIR dialog -> repairDeck -> steps 7-10, with a non-null collection (repairCollection dereferences col.getPath() at BackupManager.java:243 before col.close() at 245). Tools/ reason: shared dialog page needs dialog-id-aware routing in tools/ (same class as routes 24, 25, 30). |
| 28 | AbstractFlashcardViewer.typeAnswer | WRONG | 11 | Fiction at step 9 (Eed5b25c0, interface fan-out to an unregistered listener): the AFV listener whose onPreExecute calls blockControls() is mAnswerCardHandler (AbstractFlashcardViewer.java:578-585), registered only by AFV/Reviewer ANSWER_CARD launches (AbstractFlashcardViewer.java:1076, 1092, 1172, 1320; Reviewer.java:96-98). Step 6's LOAD_DECK_COUNTS launch (DeckPicker.java:1823) registers DeckPicker's own listener, never AFV's; DeckTask.onPreExecute (DeckTask.java:346) delegates only to that task's listener. Steps 10-11 genuine in isolation (blockControls at :584; typeAnswer predicate evaluation at :2449 IS a call). Corrected route: route-21 Reviewer prefix + ANSWER_CARD launch with mAnswerCardHandler (Reviewer.java:96-98) -> onPreExecute -> blockControls -> typeAnswer. Tools/ reason: the builder's interface dispatch ignores which listener a launch registered (the same producer-awareness gap as route 11, here at pre-execute); fixing needs producer-aware listener dispatch in tools/. |
| 29 | Decks.id(String,boolean) | CORRECT | 11 | All 11 steps genuine as printed (full step table in judge-21-30). |
| 30 | SimpleMessageDialog.<init> | WRONG | 10 | Fiction at step 5 (Ea13b2167, wrong dialog id), identical to route 24 step 5: entered LOAD_FAILED dialog's buttons go only to ERROR_HANDLING or exit(); cited lines 294-302 are the CONFIRM dialog's onPositive, never shown on this prefix, and ERROR_HANDLING's check_db option requires colIsOpen(), contradicted by the failed-load prefix. Judged on the printed <init> target (new SimpleMessageDialog() at SimpleMessageDialog.java:23, distinct from first-draw route 08's $1.<init> callback). Steps 6-10 genuine (step 7 requires a successful database check, DeckPicker.java:1170). Corrected route: collection-open prefix as route 24 (menu action_check_database -> CONFIRM dialog -> onPositive -> integrityCheck) -> printed steps 6-10. Tools/ reason: shared dialog page needs dialog-id-aware routing in tools/ (same class as routes 24, 25, 27). |

## Totals

- Routes: 30. CORRECT 20, WRONG 10, UNCLEAR 0.
- Error rate (final draw): 10/30 = 0.3333.
- Labels: 0 flips in Stream A (REACHABLE 3275, UNREACHABLE 911 throughout).
- Graph after Stream A: methods 4186, pages 49, edges 9608, errors 0, warnings 0 (stale verification.csv warning cleared by regeneration in A4).
- No route was left WRONG because a graph_def edit was pending: every WRONG above names the tools/ builder limitation that makes the builder print the fiction, with a corrected derivation from printed source. The first-draw table's WRONG routes are superseded by this table; their corrected derivations remain valid history but are not this draw's routes.
