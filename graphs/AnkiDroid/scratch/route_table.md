# AnkiDroid — FINAL route table (combined merge, redraw seed 20261025)

Sample: `python3 -I tools/verify_sample.py AnkiDroid 30 20261025` on the
combined-merge graph (new mod file `graph_def_mod/03.py` + chained EDIT
wrappers after the final EDIT; 16 generic DatabaseErrorDialog deletions).
Graph: 4186 methods, 56 pages, 9815 edges; labels REACHABLE 3275 /
UNREACHABLE 911 (zero flips vs the round-commit baseline); build errors 0.
Judgments: independent per-method reads of the new prints
(`turn/merge/newsample-routes-30.log`, `turn/merge/JUDGE-A.md`,
`turn/merge/JUDGE-B.md`, `turn/merge/JUDGE-C.md`), plus the gate judge
(`turn/merge/JUDGE-GATES.md`) for four dropped-out targets.

Totals: CORRECT 27 / WRONG 3 / UNCLEAR 0. Rate = WRONG / (CORRECT + WRONG)
= 3 / 30 = 0.1000.

Composition vs the old final draw (seed 20261025, old graph): 23 methods
carried over, 7 dropped, 7 new. Dropped: Preferences.replaceString,
DeckPicker$5.onProgressUpdate, libanki.Utils.base62, MetaDB.getNotificationStatus,
BaseAsyncTask.onProgressUpdate, Collection.close(),
AbstractFlashcardViewer.typeAnswer — all still REACHABLE (labels unchanged).
New: Models.rem, Models$TransformFieldMove.<init>, Models.validateBrackets,
FullSyncer.syncURL, UIUtils$1.onPostExecute, Collection.getServer,
AnkiActivity.openUrl.

Binding constraints carried from the old table (still in force on this graph):
the generic `S_DLG_DATABASE_ERROR` page now has ZERO incoming and ZERO
outgoing edges (the 16 deletions killed it; it is not re-provided); no
suppression of the 16 confirm + 8 cancel dispatch edges (they stay
auto-dispatched); the single-EDIT rule (r11/r12/r14v2/r28 wrappers chain the
previous EDIT, never replace it); Stats Edf6d8bd0 stays deleted (the
predecessor edge is gone; no new edge for it); BackgroundPost Ecba7dfd7 stays
ENV_NETWORK (ENV label set is not the correctness set, and its route still
exists in the graph).

Route-08 flag (carried, not re-litigated): row 08 is judged CORRECT here, but
the same method was UNCLEAR in the first draw (row 06) because its final
`<init> -> onCreateDialog` step has no printed framework evidence and stays
INFERRED (support-v4 DialogFragment source absent from the tree). If the
table auditor rules UNCLEAR, row 08 flips to UNCLEAR with no other change
(totals become CORRECT 26, WRONG 3, UNCLEAR 1, rate 3/29 = 0.1034).

## Final table (new draw, redraw order)

| # | Method | Verdict | Steps | Reason |
|---|---|---|---|---|
| 01 | Phrase.<init> | CORRECT | 38 | All steps genuine; Reviewer-head GUI chain to TranslationActivity; final Gson step INFERRED. Condition: cards due. |
| 02 | EasyX509TrustManager.<init> | CORRECT | 20 | All steps genuine; SYNC task via the onResume head; Apache steps library-INFERRED. Condition: logged-in hkey + online. |
| 03 | Stats$1.compare | CORRECT | 26 | All steps genuine; HOURLY_BREAKDOWN case (Statistics.java:503), sort at Stats.java:852-859, JDK-sort INFERRED. Condition: cards due. |
| 04 | Sched._cntFnNew | CORRECT | 15 | All steps genuine as printed. Condition: day rollover. |
| 05 | libanki.Utils$1.<init> | CORRECT | 14 | All steps genuine; @SELECT dialog-id chain (DIALOG_IMPORT_SELECT entry -> ImportDialog -> getImportableDecks); dir-exists guard. |
| 06 | Sched.revDue | CORRECT | 16 | All steps genuine as printed; _nextDueMsg calls revDue as a predicate. Condition: finished deck. |
| 07 | MediaCheckDialog$3.<init> | CORRECT | 16 | All steps genuine as printed. Condition: media-sync-server-error + check success; logged-in hkey + online. |
| 08 | ModelEditorContextMenu.onCreateDialog | CORRECT | 14 | All steps genuine; final lifecycle step genuine-INFERRED (support-v4 DialogFragment, not androidx; onCreateDialog at ModelEditorContextMenu.java:31). Condition: model list loaded successfully. See the route-08 flag above. |
| 09 | StudyOptionsActivity.closeStudyOptions(int) | WRONG | 33 | Fiction at step 23 (E10ee7f20): the TagsDialog shown by CardBrowser installs CardBrowser's own search listener, never CustomStudyDialog$1$1; PLUS guard contradiction (step 6 needs mFragmented true, step 28's openStudyOptions else branch needs mFragmented false for the same DeckPicker). Step 25 is producer-exact in isolation ($4 created inside createCustomStudySession, CustomStudyDialog.java:455-468, calling onCreateCustomStudySession) but the chain never starts on this prefix. The old E46c212fb fiction is dead; BFS now prints a longer pre-existing interface fiction. No corrected derivation proven on this graph: the old custom-study-menu derivation shares the mFragmented tension. Follow-up owed: TagsDialog producer-split fix + phone-pure prefix investigation (new scope, not in this merge). |
| 10 | Finder.findNotes | CORRECT | 34 | All steps genuine; Reviewer head + for-result tail (startActivityForResult -> fragment onActivityResult -> deleteDummyCards -> findNotes). This print contains no Finder/_where steps, so the route-23 query fix is irrelevant here. Condition: cards due. |
| 11 | Template$1.compare | CORRECT | 17 | All steps genuine; upgrade-time save chain renders a two-modifier template tag through the sort comparator; transient first-open failure + successful retry. Condition: old schema + non-zero model id + multi-modifier absent-field template tag. |
| 12 | HttpFetcher.downloadFileToSdCardMethod | CORRECT | 37 | All steps genuine; drawer dispatch now resolves to the Reviewer override (step 14 new variant page id Ebf481404, step 15 new variant dispatch id E09ef790a, step 16 pre-existing E5285c072 — NOT the old step-16 id E0e89f361, because the receiver changed from DeckPicker.openCardBrowser to Reviewer.openCardBrowser; steps 17-37 same; old fiction Ea0eba485 gone, 0 occurrences). Pronunciation download in the field editor. Condition: network + Beolingus. |
| 13 | Sound.notifyConfigurationChanged | CORRECT | 24 | All steps genuine; replay menu plays a video sound with a thumbnail, VideoPlayer rotation calls back into Sound. Conditions: non-TTS replay, video sound with thumbnail, VideoPlayer configChanges (AndroidManifest.xml:184). |
| 14 | Anki2Importer._mediaPick | CORRECT | 16 | All steps genuine; import chain reaches media comparison, which picks bytes from both streams. |
| 15 | Models.rem | CORRECT | 16 | All steps genuine; long-press delete confirmation launches the delete-model task, which calls rem. (New to the sample.) |
| 16 | Models$TransformFieldDelete.<init> | CORRECT | 21 | All steps genuine; the field-delete confirmation (not sort) drives the delete-field task into remField's TransformFieldDelete: $3.confirm -> deleteField -> DeckTask.doInBackground@DELETE_FIELD -> DeckTask.doInBackGroundDeleteField -> Models.remField -> TransformFieldDelete. NOT a sort-prefix print ($9.onSelection takes the FIELD_DELETE case, ModelFieldEditor.java:601; sort is a separate case; deleteFieldDialog guard mFieldLabels.size() >= 2, ModelFieldEditor.java:236-237). Only the $3 leg is exhibited by this print; source checks confirm the siblings ($4 second confirm also calls deleteField; $2$1 nested confirm in addFieldDialog launches ADD_FIELD, ModelFieldEditor.java:205-209; $7/$8 confirms in deleteModelDialog call deleteModel, ModelBrowser.java:455, 472). |
| 17 | Models$TransformFieldMove.<init> | CORRECT | 20 | All steps genuine; the reposition dialog confirmation launches the reposition task into moveField's TransformFieldMove. (New to the sample.) |
| 18 | Models.validateBrackets | WRONG | 17 | Fiction at step 7: its guard picks repair (value 2, case 2 -> REPAIR_COLLECTION, DatabaseErrorDialog.java:180-183) but step 8 requires restore (value 3, case 3 -> RESTORE_BACKUP, DatabaseErrorDialog.java:184-187) from the same single onSelection call. The genuine continuation exists with the corrected guard (pick restore, value 3, always offered): steps 9-17 check out (RESTORE_BACKUP -> restoreFromBackup -> importReplace -> IMPORT_REPLACE -> tmpCol.validCollection at DeckTask.java:791 -> validateModel -> validateBrackets at Models.java:1392, conditional on a valid non-empty backup). Verdict stays WRONG because the printed route, as printed, contains the contradiction. Note: the same guard-text pattern (repair-guarded $3 edge carrying restore traffic) appears in the legacy underscore ERROR_HANDLING page — see the disclosure below; a guard-neutralization fix is follow-up work, not in this merge. (New to the sample.) |
| 19 | FullSyncer.syncURL | CORRECT | 19 | All steps genuine; the empty-collection full-sync download runs req on a FullSyncer receiver, so syncURL dispatches to the FullSyncer override (HttpSyncer.java:207 calls syncURL() virtually). (New to the sample.) |
| 20 | Sched.sortCards(long[],int,int,boolean,boolean) | CORRECT | 19 | All steps genuine as printed; single consistent guard includeSched=false; filtered export resets cards, forgets them, and repositions via the two-argument sortCards. |
| 21 | Sched.getToday | CORRECT | 18 | Corrected pattern confirmed: step 17 _where -> _findCardState@due with is:due in terms[0], step 18 @due -> getToday for val "due" (Finder.java:466). Condition: the rebuilt deck's first search term actually contains is:due. |
| 22 | AdvancedStatistics$Card.setIvl | CORRECT | 35 | All steps genuine, including the forecast-tab chain into the advanced-statistics hook and the simulation tail ending at setIvl. Condition: advanced_statistics_enabled on, or the hook is never installed. |
| 23 | DiffEngine.diff_cleanupSemanticScore | CORRECT | 24 | All steps genuine along the typed-answer route from the Reviewer key release through the diff cleanup chain. Condition: the typed answer differs from the correct answer. |
| 24 | UIUtils$1.onPostExecute | CORRECT | 11 | All steps genuine, from DeckPicker onStop saving the collection in the background to the registered task listener's onPostExecute. Condition: the collection is open at onStop. (New to the sample.) |
| 25 | DB.insert | CORRECT | 11 | All steps genuine on the new showStartup integrity-check route, with no base-page dialog step and no Ea13b2167 edge. Condition: the integrity check finds orphan notes to delete. |
| 26 | CollectionLoader.deliverResult | CORRECT | 11 | All steps genuine from the no-space dialog through the loader restart to deliverResult; support-library dispatch genuine-but-INFERRED. |
| 27 | Decks.id(String,boolean) | CORRECT | 11 | All steps genuine from the deck-list refresh through the parent-deck fallback to id(String, boolean). Condition: the deck is missing from the displayed list. |
| 28 | Collection.getServer | WRONG | 10 | Fiction at step 8: on the load-failed prefix the collection object is null (or closed with a null database), so closeCollection's null guard and Collection.close's mDb-null guard skip Collection.close, and steps 9-10 (Media.close -> getServer) never run on this prefix. The close-to-getServer calls are real code, just unreachable after a failed first open. A corrected route needs an open-collection prefix, not the load-failed prefix. (New to the sample; pre-existing print fiction, NOT caused by the merge.) |
| 29 | SimpleMessageDialog.<init> | CORRECT | 10 | All steps genuine on the new showStartup integrity-check route via $15.onPostExecute; step 7 requires a successful database check (DeckPicker.java:1170). No Ea13b2167 edge. Condition: the integrity check reports success. |
| 30 | AnkiActivity.openUrl | CORRECT | 11 | All steps genuine from the not-logged-in sync dialog through MyAccount to the sign-up button opening the registration page. Condition: empty sync key so the login dialog appears and the login view is shown. (New to the sample.) |

## Dropped-out targets: gate verdicts (not sample rows; do not count in the totals)

The four dropped old-WRONG targets were re-printed on the merged graph and
independently judged GENUINE (`turn/merge/JUDGE-GATES.md`, GATES-PASS):

- libanki.Utils.base62 — 28 steps GENUINE: NoteEditor add-mode (head
  S_NOTEEDITOR) -> setNote() -> setNote(Note) -> 2-arg -> 3-arg @id-null ->
  guid64 -> base91 -> base62 (Note.java:58-72, Utils.java:421/427); old
  CHECK_MEDIA route gone as best route; base62's sole incoming is E4a0aec25
  from base91; @id-set leads only to Note.load; 3-arg + base62 REACHABLE.
- BaseAsyncTask.onProgressUpdate — 13-step sync route GENUINE (final
  super-call Connection.java:152-153, Connection extends BaseAsyncTask) AND
  the restore chain hand-traced at exactly 17 edges via @ pages
  (@LOAD_FAILED -> $1 -> @ERROR_HANDLING -> $3 -> @RESTORE_BACKUP -> $6 ->
  restoreFromBackup -> importReplace -> IMPORT_REPLACE task -> onProgressUpdate
  -> target). $6's sole incoming is from @RESTORE_BACKUP; every route to $6
  passes through the $3 error-handling selection.
- Collection.close() — 14 steps GENUINE: download via $17 (fullSync +
  empty-collection branch DeckPicker.java:1450-1452 -> sync("download") ->
  download branch Connection.java:334-337 -> FullSyncer.download -> close()).
  Download incoming exactly [$11.onPositive, $17.onPostExecute, SyncErrorDialog$5,
  SyncErrorDialog$8]; upload incoming exactly [SyncErrorDialog$4, SyncErrorDialog$7].
  REPAIR chain exists (14 edges via underscore pages, 15 via @ pages):
  $3 -> REPAIR page -> $4 -> repairDeck -> REPAIR_DECK task -> repairCollection
  -> close().
- AbstractFlashcardViewer.typeAnswer — 16 steps GENUINE: Reviewer prefix +
  ANSWER_CARD launch with mAnswerCardHandler (Reviewer.java:110-111) ->
  @ANSWER_CARD -> $10 -> blockControls -> typeAnswer. NO LOAD_DECK_COUNTS /
  updateDeckList step; NO receiver-variant auto edge used (step 14 is E3a9489a8
  from the @ANSWER_CARD node). @ANSWER_CARD has exactly 1 non-REGISTER
  outgoing edge (the hand edge to $10) plus 27 REGISTER edges.

Mechanical re-confirmation on the merged graph (all PASS): integrityCheck
incoming exactly [V03, showStartup]; @CONFIRM sole outgoing Efb51fa08 to
$9@CONFIRM; @CONFIRM variant path to DB.insert available at exactly 14 edges;
generic page 0 in / 0 out; plain $9.onPositive 0 incoming; $8.onPositive sole
incoming E80338edd from @NEW_COLLECTION; all six @ variant pages
BFS-reachable from S_ENTRY.

Disclosure (does not change any verdict): a raw 16-edge restore variant via
the legacy underscore ERROR_HANDLING page exists but is guard-inconsistent
(repair guard in, restore branch out); the guard-consistent chain is the
17-edge @ chain. The literal "@-only" bypass wording is therefore FALSE in
the narrow sense, but NO path bypasses the error-handling STAGE or
@RESTORE_BACKUP, so the r25 no-bypass gate holds in substance. The same
repair-guard text on the underscore $3 edge is what makes row 18
(validateBrackets) WRONG as printed: restore traffic through that edge
contradicts its guard. Neutralizing the D01/V05 $3-edge guards to
branch-neutral wording is follow-up work (guard-text change + rebuild +
re-judge of row 18 only); it is NOT in this merge, and the audited r27 v4
fragment text was not altered to chase it.

The three other dropped targets (Preferences.replaceString, DeckPicker$5,
MetaDB) were not re-printed; their old CORRECT verdicts stand as history
only and are not counted here.

## Notes on the fixed routes (for the device delta)

- r11 closeStudyOptions: NOT fixed by this merge — row 09 stays WRONG (see
  above). The r11 fragment did its audited job (old E46c212fb fiction dead),
  but the printed route is a different, longer pre-existing fiction.
- r12 HttpFetcher: FIXED — row 12 CORRECT (37 steps, variant dispatch).
- r14 TransformFieldDelete: FIXED — row 16 CORRECT (21 steps, DELETEFIELD
  variant sequence; $3 leg exhibited, siblings confirmed in source).
- r20 base62: FIXED as a route (gate-verified 28-step genuine print) but
  dropped from the sample; the old CHECK_MEDIA fiction is gone.
- r23 getToday: FIXED — row 21 CORRECT (18 steps, is:due pattern).
- r24/r30 DB.insert + SimpleMessageDialog: FIXED — rows 25/29 CORRECT
  (11/10 steps, showStartup route; @CONFIRM variant path also available at
  14 edges to DB.insert for the device drive).
- r25 BaseAsyncTask: FIXED as a route (gate-verified 13-step sync print +
  17-edge @ restore chain) but dropped from the sample.
- r27 Collection.close: FIXED as a route (gate-verified 14-step download
  print + REPAIR chain) but dropped from the sample.
- r28 typeAnswer: FIXED as a route (gate-verified 16-step print) but dropped
  from the sample.
- New WRONG rows (validateBrackets, Collection.getServer) are pre-existing
  print fictions surfaced by the redraw, not regressions from the merge:
  neither method's route was touched by any fragment.
