# AnkiDroid route table — final draw (seed 20261025), after B6 fixes

Sample: `python3 -I tools/verify_sample.py AnkiDroid 30 20261025` on the
post-B6 graph (methods 4186, edges 9183, REACHABLE 3275, UNREACHABLE 911,
errors 0, warnings 0). First-draw sample file:
`graphs/AnkiDroid/scratch/sample_30.txt` (30 of 3275, 299 distinct edges
on the pre-fix graph). Final BFS routes were re-printed from the post-B6
graph into `scratch/route_print/` (30 files).

Verdicts are the AUDITED first-draw verdicts (audits b6-r01-09, b6-r10-18,
b6-r19-30, plus B6 fix audits F1–F5, all PASS): WRONG 18, FIXED 9,
UNCLEAR 2, CORRECT 1. Error rate = (fixed + wrong) / (correct + fixed +
wrong) = (9 + 18) / (1 + 9 + 18) = 27/28 = 0.9643. This is the FIRST-DRAW
error rate, not a final-draw rate: the fixes below are graph guard/evidence
fixes and corrected derivations, not label changes (0 label flips in B6).

How to read the "steps" column: for FIXED and CORRECT routes it is the
final BFS route's step count (the fix is in the graph, so the BFS route
is now the judged route). For UNCLEAR route 08 it is the final BFS count.
For WRONG routes it is the CORRECTED route's step count (the BFS route
is wrong; the corrected derivation is the table route, from the helper
file cited). For UNCLEAR route 06 the corrected route C06 has the same
14 steps as the BFS route (no sequence change; verdict stands).

REDRAW NOTE (honest, for the coordinator): re-running verify_sample on
the post-B6 graph gives a DIFFERENT sample (297 distinct edges): 5
methods leave the sample (Template$1.compare, FilteredDeckOptions,
ModelFieldEditor$1, NoteEditor.closeNoteEditor, Models._availClozeOrds)
and 5 enter it (CardTemplateEditor$CardTemplateFragment$4.<init>,
Info.copyDebugInfo, AbstractFlashcardViewer.typeAnswer,
BackupManager.deleteDeckBackups, CustomTabsHelper.hasSpecializedHandlerIntents).
That happens because the sampler spreads over route_edge_ids, which
change when fix edits change edge ids, and because F5 added ENV/STATE
kinds to more methods. Per the merger's assigned task, this table covers
the FIRST-draw 30 routes (the audited, fixed set); the 5 redraw-only
methods are NOT judged here and need a coordinator ruling (judge them as
a follow-up sample, or accept this table as the B6 table). The 5 dropped
routes' corrected derivations are still in this table, and their targets
remain REACHABLE.

Binding constraints applied (from the fix audits): single EDIT definition
(B3 EDIT chained through F3 and F2 wrappers, never replaced); F3's
fragment folded in; route-17 step-6 applied by edge+line (887 block only,
evidence line 890; the RESULT edge at line 973/980 is byte-identical);
no second route-11 call-site edge (the :958 edge is the traversable
final-else branch; :855-858 has no separate graph edge); no $16 edge
for route 08 (rename HELD, bytecode proof: $15 = CHECK_DATABASE,
$16 = CHECK_MEDIA); no suppression of the 16 confirm + 8 cancel dispatch
edges; BackgroundPost Ecba7dfd7 stays ENV_NETWORK (the second cycle was
not expanded into explicit steps, so the ENV_BEOLINGUS condition does not
fire); route 08 stays UNCLEAR (no $16 edge ever).

| # | method | verdict | steps | reason / corrected route |
|---|---|---|---|---|
| 01 | Phrase.<init> | WRONG | 36 | C01: printed route launched LOAD_DECK_COUNTS then took the RENDER_BROWSER_QA branch (steps 8, 10 wrong). Corrected route: LOAD_DECK_COUNTS dispatch (DeckTask.java:234-235), deck-list page, drawer openCardBrowser (Ed1dad133), CardBrowser launch. One corrected step (DeckPicker$22.onPostExecute -> S_DECKPICKER) is a page abstraction with no dedicated graph edge. Corrected edge ids (final graph): E48de6d58 E26d20f74 E1ad4ef9b E553ad2d8 E0b111c68 E8b5d2971 E460971ee Ee1634710 E3e610385 Eee369b5f E10a14596 Ed1dad133 E0e89f361 Eb06cba16 E352d419a E0281e707 E37ba8c1f E94833ec9 E44749e19 Ed63b7964 E7b61f827 Eb7034235 Ed31d10af Eabfa7572 E92aeb8ec Ebb46b041 E31bccb82 Eaa5fd795 E57ec0f8c Ece92d132 E4591472f E2c3f2e9e Eb9c36e0c Ec32ee4bb Edd1d361a. |
| 02 | EasyX509TrustManager.<init> | WRONG | 19 | C02: printed route used a LOGIN Connection task, but sync() needs mSyncOnResume; the SYNC task (Connection.java:187-188, not LOGIN :160-162) is the genuine prefix. Steps 13-15 carry the auditor-verified ids: step 13 Syncer.sync(Connection) -> RemoteServer.meta E3a5b3438, step 14 RemoteServer.meta -> HttpSyncer.req(String,InputStream) E51823c2c, step 15 HttpSyncer.req(String,InputStream,int,JSONObject,CancelCallback) -> EasySSLSocketFactory.createSocket(Socket,String,int,boolean) E0c0d5268. Apache dispatch step stays INFERRED. |
| 03 | StepsPreference.updateSettings | WRONG | 23 | C03: printed steps 8-11 used updateDeckList's listener, not the undo listener that calls openReviewer. Corrected chain: undo listener + DeckPicker$13 + isReview (DeckPicker.java:996-999, 997-998, 1011-1014); target itself sound via DeckOptions inflation. All 23 corrected steps resolve to final-graph edges (resolver output on file). |
| 04 | Stats$1.compare | WRONG | 25 | C04: LOAD_DECK_COUNTS vs RENDER_BROWSER_QA dispatch break (same class as route 01). Corrected route: LOAD_DECK_COUNTS dispatch, HOURLY_BREAKDOWN via ChartBuilder.java:84-85, sort at Stats.java:852-859, no split; the RENDER detour ends at the DeckTask.java:652 static call; JDK-sort only is INFERRED. |
| 05 | Sched.totalRevForCurrentDeck | WRONG | 19 | C05: dialog id 0 goes to buildContextMenu, not buildInputDialog. Corrected route is the two-dialog sequence: 0 -> buildContextMenu -> pick 101 -> buildInputDialog -> CustomStudyDialog.java:362-363. Support-v4 links stay INFERRED. |
| 06 | ModelEditorContextMenu.onCreateDialog | UNCLEAR | 14 | C06: no sequence change; final step (<init> -> onCreateDialog) has no printed framework evidence and stays INFERRED (support-v4 imports: CustomStudyDialog.java:24, ModelEditorContextMenu.java:5). Verdict stands. |
| 07 | libanki.Utils$1.<init> | WRONG | 11 | F2: getImportableDecks is called only in DIALOG_IMPORT_SELECT, not ADD_CONFIRM. Corrected derivation (SELECT entry): HINT dialog positive -> ImportDialog (SELECT) -> getImportableDecks (guard mType == DIALOG_IMPORT_SELECT, ImportDialog.java:86-88) -> $1.<init> (dir.exists() && dir.isDirectory(), Utils.java:909-910). Graph guards for steps 8/12/13 applied; the printed ADD_CONFIRM prefix is discarded. |
| 08 | SimpleMessageDialog$1.<init> | UNCLEAR | 12 | F2, audit binding correction: originally FIXED, corrected to UNCLEAR (step 11 unresolved). Fixes applied: steps 4, 5, 7, 12 (incl. :39 -> :40) + support-v4 wording correction. Step 6 rename $15 -> $16 HELD (bytecode: $15 = CHECK_DATABASE, $16 = CHECK_MEDIA; renaming would create a false edge). Step 11 stays explicitly INFERRED (support-v4 DialogFragment source absent from tree; only framework android.app.DialogFragment exists, a different class). No $16 edge ever. |
| 09 | MetaDB.getNotificationStatus | FIXED | 14 | F2: both guards applied (DeckPicker.onStop -> WidgetStatus.update colIsOpen(); WidgetStatus.update -> doInBackground verbatim gate, WidgetStatus.java:57-58). Final BFS route is the judged route. |
| 10 | Template$1.compare | FIXED | 15 | F2: all 6 fixes applied, incl. colOpen, pre-2.6alpha23 font-familiy typo STATE, model id, non-cloze + >=1 template, plain-tag, multi-modifier tag state. Final BFS route is the judged route. |
| 11 | FilteredDeckOptions.onSharedPreferenceChanged | FIXED | 15 | F2: all 7 fixes applied (shared step-4 edge with route 10 applied once). Step 5: the :958 edge is the traversable final-else branch; NO second call-site edge for :855-858 (auditor ruling; the applied guard records :858 as the other call site). Final BFS route is the judged route. |
| 12 | Sound.notifyConfigurationChanged | WRONG | 19 | F2, no graph edit (auditor ruling): rebuilt reviewer-flow route, never the printed route. Printed route's LOAD_DECK_COUNTS -> RENDER_BROWSER_QA break + empty DeckPicker listener. Rebuilt route (19 steps): launcher -> DeckPicker -> Reviewer (openReviewer) -> answerCard (TASK_TYPE_ANSWER_CARD, mAnswerCardHandler) -> doInBackgroundAnswerCard -> onProgressUpdate chain -> displayCardQuestion -> updateCard -> playSounds -> Sound chain -> VideoPlayer -> onConfigurationChanged -> Sound.notifyConfigurationChanged. |
| 13 | HttpFetcher.downloadFileToSdCardMethod | WRONG | 27 | F3 (+rework, re-audit PASS): rebuilt prefix R1-R7 (launcher -> DeckPicker page S_DECKPICKER -> drawer openCardBrowser Ed1dad133, expanded as E02986fa7 + Ea0eba485 -> CardBrowser.<init> E0e89f361 -> onCreate -> S_CARDBROWSER) + surviving printed steps 12-31 with EDITS.md corrections (step 14 E37ba8c1f with !editModelMode per audit C1; step 15 E94833ec9; step 16 E44749e19; step 20 E1e29f3f5; step 21 Ea9606e5d; step 26 Ece5d578d with ENV_BEOLINGUS; step 29 E19aee917; step 31 Ef9fac826, citation :125 unconditional GET). Step 9 (E3f1b0491, <clinit> -> <init>) is UNCLEAR per the Finder convention and is NOT carried into the rebuilt route. Full-cycle annotation: step 29's second BackgroundPost cycle is compressed (translation post -> pronunciation post, LoadPronounciationActivity.java:288-306); the intermediate BackgroundPost edge Ecba7dfd7 stays ENV_NETWORK because the second cycle was not expanded into explicit steps. BFS best route is unchanged in structure (guards do not change BFS cost; the dispatch chain still wins on cost despite being wrong) — the table must NOT be copied from the redraw. |
| 14 | Preferences.replaceString | WRONG | 10 | F3: step 4 graph-fixed (Ea2e5a92a -> Edd09dca3: dir-NOT-accessible branch, ENV_PREFS_PATH). Step 10 is not a graph fault: advanced_statistics_link is a plain <Preference>, so updateSummary returns at Preferences.java:636 before replaceString. Corrected terminal path via key backupMax (SeekBarPreference, summary "XXX"): steps 8' onSharedPreferenceChanged -> updatePreference (E249f9a1a), 9' updatePreference -> updateSummary, 10' updateSummary -> replaceString (Ec779c0bd). Sampled route verdict stays WRONG. |
| 15 | api.Utils.entsToTxt | FIXED | 6 | F3: spec guard >= 2 + resolver pins to api/Utils.java (steps 2-6: api/Utils.java:68/86/96 and AddContentApi.java:162/708, lines unchanged). show_route confirms all three Utils citations resolve to the api file. Final BFS route is the judged route. Table-only citation: class declaration :37 (not :25 for route 16's table entry; see route 16). |
| 16 | Sched.haveBuried(long) | CORRECT | 10 | F3: no graph edit. All 10 steps correct as printed. Table citation: import at DeckPickerContextMenu.java:21 (not :25), class declaration :37. First CORRECT route of the sample. |
| 17 | ModelFieldEditor$6$1.<init> | FIXED | 17 | F3: all 4 edges applied (step-6 menu guard, step-14 FIELD_REPOSITION guard, step-15 citation 357 -> 358, step-17 modSchema-exception guard). Step-6 applied by edge+line ONLY (887 block, evidence line 890 -> Ec31ec494); the RESULT edge (evidence line 973/980) is byte-identical, and the EDITS.md uniqueness sentence was amended at merge time to record the two-occurrence exception. Final BFS route is the judged route. |
| 18 | Finder.findNotes | WRONG | 16 | F3 (+rework, re-audit PASS): rebuilt prefix R1-R7 (as route 13) + re-anchored tail T1-T9 from S_CARDTEMPLATEEDITOR (Ef2bc6ed3 -> E35d06ed2 -> E37519322 -> Ecb6f2b21 -> E8a25b1c0 -> Eb9d6a916 -> E2a61410a -> E94ef2a85 -> E2d26f33d). Printed steps 11-19 are genuine edges in isolation but not a valid continuation: the CardBrowser Previewer was launched with startActivity (not for-result, AnkiActivity.java:158-161), so its result cannot return to the fragment; step 20 borrows the fragment's RESULT edge out of context. Scope note: the head into S_CARDTEMPLATEEDITOR is NOT re-derived here; the merger's redraw supplies it, and the tail above is the audited chain from that page. Step 5's shared edge fix (E47fbe466 -> Ecdba007c) applied once under route 13. |
| 19 | AdvancedStatistics$Card.setIvl | WRONG | 13 | F4, no graph edit: hook-name mismatch — the printed route invokes mungeQA, but AdvancedStatistics registers only under "advancedStatistics" (AdvancedStatistics.java:148; Hooks.java:144-150 dispatches by name only). Corrected prefix (5 steps): ChartBuilder.calcStats -> Stats.calculateDue (Stats.java:311) -> runFilter("advancedStatistics") -> AdvancedStatistics.runFilter; tail = printed steps 13-20 (calculateDueAsMetaInfo -> ... -> c.setIvl(ivl)). The old _renderQA head's guards do NOT carry over. |
| 20 | DiffEngine.diff_cleanupSemanticScore | WRONG | 13 | F4, no graph edit, NO-split honoured: corrected prefix (5 steps) via TASK_TYPE_UPDATE_FACT + mUpdateCardHandler (AFV.java:1084, DeckTask.java:419,422), NOT RenderBrowserQA + reviewer listener (RenderBrowserQA launches only from CardBrowser with mRenderQAHandler, percent-int payload, DeckTask.java:657-659; it cannot reach AFV$9). Tail = printed steps 13-20 (displayCardAnswer -> typeAnsAnswerFilter -> diff chain -> diff_cleanupSemanticScore). Auditor-added alternative: the reviewer-direct displayCardAnswer route is equally genuine. Table must NOT use RenderBrowserQA -> AFV$9. |
| 21 | CustomTabsFallback.openUri | WRONG | 11 | F4, SPLIT APPLIED: S_DLG_SYNC_ERROR split into NOT_LOGGED_IN (type 0) + MEDIA (type 9) variant pages; 4 GUI edges moved (E2e661eb4, E12ec6751, Ecfb331a6, E45ca1a65), 2 ENTERS added (E81c3cc95, E6b094d43); generic page kept for types 2,3,4,6,7,8. Corrected prefix (6 steps): onResume (mSyncOnResume, LOG_IN_FOR_SYNC RESULT_OK) -> sync() -> sync(String) with hkey EMPTY -> showSyncErrorDialog(DIALOG_USER_NOT_LOGGED_IN_SYNC) -> variant page S_DLG_SYNC_ERROR_NOT_LOGGED_IN -> $1.onPositive -> loginToSyncServer -> MyAccount (STATE_LOG_IN, hkey empty, consistent). Tail = printed steps 12-16 (sign-up -> openUrl -> CompatV16.openUrl -> CustomTabActivityHelper.openCustomTab -> fallback.openUri, guard: no custom-tabs browser installed). BFS caveat: the post-fix BFS best route still assembles the onPostExecute head onto the not-logged-in variant page (BFS ignores guard text); the table uses the call-site-correct hkey-empty prefix, never the BFS route. |
| 22 | libanki.Utils.base62 | WRONG | 16 | F4, no graph edit: (a) LOAD_DECK_COUNTS dispatches to LoadDeckCounts (DeckTask.java:235), never to DismissNote (only TASK_TYPE_DISMISS :256); (b) the Note-constructor id==null branch conflicts with the non-null id supplied by getNote (Collection.java:425-426 -> Note.java:54-55). Corrected route: new-note construction (NoteEditor.setNote :1370 -> Note(col,model,null) -> guid64 -> base91 -> base62); DISMISS launch alone cannot save the tail. Printed step count 16 shown for reference; the corrected route's steps are the new-note chain in helper/b6fix-r19-24/CORRECTED_ROUTES.md. |
| 23 | CardTemplateEditor$3.onPositive | WRONG | 23 | F4, no graph edit: LOAD_DECK_COUNTS -> RENDER_BROWSER_QA again, plus static updateSearchItemQA mistaken for a CardBrowser activity launch. Corrected prefix: DeckPicker.openCardBrowser (:1708-1713); tail = printed steps 12-23 with audited fixes. The static-call edge to CardBrowser.updateSearchItemQA already exists; <clinit> -> <init> is genuinely needed for Intent entry. Printed step count 23 shown for reference; the corrected route is in helper/b6fix-r19-24/CORRECTED_ROUTES.md. |
| 24 | Hook.<init> | FIXED | 11 | F4: 5 guard replacements (steps 4, 6, 8, 9, 11; new ids E45d63a96, E4c7e034e, E98cbc59f, Eeb9f51d0, Ef693ef80 in the F4-only build; in the combined build the steps 4/6 edges also carry F5's duplicate hand edges — see combined-build note below). Post-fix best route is exactly the 11 printed steps, cold-start satisfiable. Tally correction: route 24 is 6 correct / 5 fixed (the helper verdict file's "5/6" prose is wrong). |
| 25 | CollectionLoader.deliverResult | FIXED | 11 | F5: 3 guards (colOpen, not enough disc space, collection not locked) + irrelevant Connection citation dropped from step 10. Final BFS route is the judged route. |
| 26 | ModelFieldEditor$1.<init> | WRONG | 9 / 14 | F5, SPLIT APPLIED: new pages DECKPICKER_FULLSYNC + MODELFIELDEDITOR_RENAME; DeckPicker + rename ENTERS retargeted with guards; rename confirm+cancel + DialogHandler$1.confirm moved to variant pages; old direct edge Eeded0833 gone. Corrected route A (open route, 9 steps): launcher -> DeckPicker -> menu -> ModelBrowser.<init> -> ModelBrowser$4.onItemClick -> ModelFieldEditor.<init> -> onCreate -> onCollectionLoaded -> createfieldLabels -> $1.<init>. Corrected route B (rename-flow route, 14 steps): A steps 1-5, then field-row tap -> context menu -> Rename -> $5.onPositive -> renameField (throws ConfirmModSchemaException) -> $5.onPositive -> S_DLG_CONFIRMATION_MODELFIELDEDITOR_RENAME -> $5$1.confirm -> renameField -> fullRefreshList -> createfieldLabels -> $1.<init>. BFS caveat: the $5$1.confirm BFS route still runs via the generic page through ModelBrowser deleteModelDialog (dispatch edges left unsuppressed by scope discipline); the table uses route A or B, never the BFS dispatch route. Step-5 guard is :958-only (auto_calls.json exactly one record; :858 has no auto record; modelling it is a separate edge addition). |
| 27 | Decks.id(String,boolean) | FIXED | 11 | F5: 4 guards. Final BFS route is the judged route. |
| 28 | NoteEditor.closeNoteEditor(int,Intent) | WRONG | 10 | F5, SPLIT APPLIED: NoteEditor variant page created, $6.confirm moved to it, previously missing ENTERS from changeNoteTypeWithErrorHandling added (E30f7c51d); old edge Ef2c97ad2 gone. Corrected route (from the note-editor page, 10 steps): onOptionsItemSelected -> saveNote -> changeNoteTypeWithErrorHandling -> changeNoteType (throws) -> variant page S_DLG_CONFIRMATION_NOTEEDITOR_CHANGETYPE -> $6.confirm -> changeNoteType (second call) -> closeNoteEditor() -> closeNoteEditor(Intent) -> closeNoteEditor(int,Intent). changeNoteType appears twice because the first call throws and the confirm re-calls it (not a duplicated graph edge). Dispatch caveat: virtual-dispatch auto edges ConfirmationDialog$1.onPositive -> every confirm still connect the generic page to $5$1.confirm; the 16 confirm + 8 cancel implementations are deliberately left unsuppressed (scope discipline, auditor-confirmed). |
| 29 | DB.executeScript | FIXED | 11 | F5: 4 guards. Final BFS route is the judged route. |
| 30 | Models._availClozeOrds(JSONObject,String,boolean) | WRONG | 10 | F5: corrected route via DeckTask SAVE_MODEL (10 steps): template-editor onOptionsItemSelected (Save model, action_confirm + modelHasChanged) -> launchDeckTask (TASK_TYPE_SAVE_MODEL) -> doInBackground -> doInBackgroundSaveModel -> save(model,true) (DeckTask.java:1075) -> _syncTemplates (guard templates == true, Models.java:191-192) -> genCards (guard >=1 note row, Collection.java:653-655) -> availOrds -> _availClozeOrds(JSONObject,String) (guard MODEL_CLOZE, Models.java:1127-1129) -> target (Models.java:1186). BFS caveat: the builder's best route still shows the old DeckPicker prefix, now guard-inconsistent (save(m,false) vs templates==true guard); a guard-checking redraw must reject it in favour of this SAVE_MODEL prefix. |

## Combined-build note (F4 + F5 hand-edge duplicates)

The builder does not deduplicate hand edges with the same (src, dst, kind)
but different guards: the combined graph therefore contains BOTH the F4
and the F5 hand edges for DeckPicker.onCreate ->
CollectionHelper.exceededCursorSizeLimit (E45d63a96 F4, E18aeeb0c F5) and
for CollectionHelper.getCol -> Storage.Collection(Context,String,boolean,boolean)
(E4c7e034e F4, Ea49432e0 F5). Both guards are true conditions for the same
call sites (:430 and CollectionHelper.java:99) and are compatible (F5's
are the broader else-chain / stricter colIsOpen + init-success forms).
No label, route target, or verdict is affected; the route table uses the
audited corrected routes, not BFS dispatch through these pairs. The two
other duplicate pairs in the graph (S_ENTRY -> IntentHandler.onCreate,
IntentHandler.onCreate -> DeckPicker.<init>) are pre-existing guard
variants from the baseline graph, not B6 additions.

## Totals

- Routes: 30. WRONG 18, FIXED 9, UNCLEAR 2, CORRECT 1.
- Error rate (first-draw): 27/28 = 0.9643.
- Labels: 0 flips in B6 (REACHABLE 3275, UNREACHABLE 911 throughout).
- Graph after B6: methods 4186, pages 48, edges 9183, errors 0, warnings 0.
- No route was left WRONG because a tools/ edit was needed; every WRONG
  verdict above is a route-builder error (dispatch, dialog-variant, or
  listener confusion) with an audited corrected derivation, except route
  06/08 UNCLEAR (missing printed framework evidence / held rename).
