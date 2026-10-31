# Batch 002 conflicts and evidence (DeckPicker, LABEL helper)

Files: parts/label_002.py (edges and UNREACHABLE), parts/label_002.md (item rows and EDGE rows).
Source root: final_java_only/AnkiDroid/app/AnkiDroid-#4200/AnkiDroid/src/main/java/com/ichi2/anki (abbreviated below as com/ichi2/anki).

## 1. UNREACHABLE: DeckPicker.hasErrorFiles (no_trigger_in_app)

Chain: DeckPicker.hasErrorFiles (DeckPicker.java:1254) is called only from DatabaseErrorDialog.java:126, which sits in the switch case for DIALOG_DB_ERROR (case label at DatabaseErrorDialog.java:96). Id 1 is never produced.

Grep evidence (run with grep -F across the java tree):
- DIALOG_DB_ERROR: DatabaseErrorDialog.java:28 (declaration = 1), :96 (case), :358 and :383 (switch labels in other methods). No other file.
- MSG_SHOW_DATABASE_ERROR_DIALOG: DialogHandler.java:41 (constant), :85 and :87 (receiver), DatabaseErrorDialog.java:428 (only sender).
- DatabaseErrorDialog.newInstance: only DeckPicker.java:1027 (inside showDatabaseErrorDialog, DeckPicker.java:1026-1028).
- showDatabaseErrorDialog( callers: DeckPicker.java:431 (id DIALOG_CURSOR_SIZE_LIMIT_EXCEEDED = 9), 433 (DIALOG_LOAD_FAILED = 0), 597 (DIALOG_CONFIRM_DATABASE_CHECK = 6), 618 (DIALOG_CONFIRM_RESTORE_BACKUP = 7), 1244 (DIALOG_LOAD_FAILED = 0); DatabaseErrorDialog.java:86 (DIALOG_ERROR_HANDLING = 2); DialogHandler.java:60 (DIALOG_LOAD_FAILED = 0); DialogHandler.java:87 (dialogType from the message).
- hasErrorFiles( references: DeckPicker.java:1254 (declaration), DatabaseErrorDialog.java:126 (only call).

Circularity: DialogHandler.java:87 takes dialogType from a message. The only sender (DatabaseErrorDialog.java:428) copies the dialog's own type, which came from one of the constant callers above (0, 2, 6, 7, 9). Nothing creates 1.

Open issue: the extractor will write CALL DatabaseErrorDialog.java:126 -> DeckPicker.hasErrorFiles. The authored UNREACHABLE overrides route search but warns while that non-REGISTER incoming edge remains. Suppressing it needs sup() in graph_def.py, which is not this helper's file. Recorded as open decision 1.

## 2. Kind convention for REACHABLE rows

The kind written in a REACHABLE row is the kind of the last non-CALL edge on the chosen route. CALL hops are extractor-written and are skipped. Where the route runs through ASYNC (handleDbError, onCollectionLoadError, joinSyncMessages), the row kind is ASYNC.

## 3. Cross-batch dependencies (routes that need edges owned elsewhere)

Batch 003 (its REACHABLE rows depend on this part):
- DeckPicker.onCreate -> DeckPicker.onRestoreInstanceState (FRAMEWORK, written here).
- DeckPicker.firstCollectionOpen -> DeckPicker.onRequestPermissionsResult (FRAMEWORK, written here).
- Batch 003 owns onResume (updateDeckList, startup, sync entry), showStartupScreensAndDialogs (calls onFinishedStartup at DeckPicker.java:858 and 958), sync() and sync(String), openStudyOptions, and showDatabaseErrorDialog (DeckPicker.java:1026-1028).
- onAttachedToWindow is framework-called after onResume. Route here starts at onCreate (approximation, open decision 7).

Batch 004 (listener nodes):
- DeckPicker$10.onClick (add-shared; route for addSharedDeck), DeckPicker$11.onClick (add-note; route for addNote). Existing graph edges S_DECKPICKER -> $10.onClick and $11.onClick are already in graph_def.py.
- DeckPicker$14 (repair listener; second onCollectionLoadError call at DeckPicker.java:1128).
- DeckPicker$15.onPostExecute (integrityCheck ASYNC target; calls handleDbError at line 1172).
- DeckPicker$16.onPostExecute (mediaCheck ASYNC target).
- DeckPicker$17 (sync listener; calls joinSyncMessages at line 1448; IOException path to handleDbError near line 1479).

Batch 005:
- S_DECKPICKER -> DeckPicker$2.onClick (deck tap; route for handleDeckSelection; label_005.py line 11).
- DeckPicker$4.onLongClick (DeckPicker.java:233, showDialogFragment(DeckPickerContextMenu.newInstance)). This is the ENTERS owner for S_DLG_DECKPICKER_CONTEXT; it is needed by confirmDeckDeletion(), emptyFiltered and the routes that pass through them.
- DeckPicker$5.onPostExecute (importAdd ASYNC target), DeckPicker$22.onPostExecute (deck-count result; null leads to onCollectionLoadError at DeckPicker.java:1842), DeckPicker$24.onPostExecute (deleteDeck target), DeckPicker$25 (emptyFiltered target; mSimpleProgressListener), DeckPicker$27.onPostExecute (handleEmptyCards target).

Batch 006:
- DeckPicker$6.onPostExecute (importReplace target), DeckPicker$7.onPostExecute (exportApkg target). Its ENTERS S_DLG_DECKPICKER_EXPORT_DONE at DeckPicker.java:328 is needed for the emailFile route.
- DeckPicker$9 (add-deck listener; the REGISTER edge from configureFloatingActionsMenu targets it). Batch 006 also writes DeckPicker$9.<init> -> DeckPicker$9.onClick REGISTER (graph_def.py, around line 578). The sources differ, so there is no duplicate.

Unassigned ENTERS owners (no batch currently writes these; both gate routes in this batch):
- S_DLG_SYNC_ERROR: DeckPicker.showSyncErrorDialog (DeckPicker.java:1058-1061; SyncErrorDialog.newInstance at 1060) and showSyncErrorMessage (DeckPicker.java:1068). Needed for loginToSyncServer (MG4) and mediaCheck (MG4).
- S_DLG_CUSTOM_STUDY: CustomStudyDialog.newInstance is called at DeckPicker.java:1749 and 1789. Both are inside anonymous OnClickListener.onClick bodies created in handleDeckSelection (DeckPicker.java:1717; snackbar listeners at 1746-1752 and 1786-1792). Those listener classes are not in batch 002. StudyOptionsFragment.java:273 is the other caller. Needed for onCreateCustomStudySession, onExtendStudyLimits and getFragment.

AnkiActivity loader route (only for onCollectionLoadError, secondary): AnkiActivity.java:261 (startLoadingCollection restartLoader) -> AnkiActivity.java:288 (onLoadFinished -> onCollectionLoadError). Owned outside batch 002.

Already in graph_def.py, not written here: IntentHandler.onCreate -> DeckPicker.<init> (INTENT, graph_def.py lines 545-564).

## 4. ENTERS decisions

Written (17), all with a method source in batch 002: onCreate (S_DECKPICKER, S_PREFERENCES, S_DLG_DATABASE_ERROR), addNote (S_NOTEEDITOR), loginToSyncServer (S_MYACCOUNT), onOptionsItemSelected (S_DLG_IMPORT, S_DLG_DATABASE_ERROR, S_DLG_MEDIA_CHECK, S_DLG_EXPORT, S_MODELBROWSER), exportDeck (S_DLG_EXPORT), confirmDeckDeletion(long) (S_DLG_DECKPICKER_DELETE_DECK), handleDbError (S_DLG_DATABASE_ERROR), onCollectionLoadError (S_DLG_DATABASE_ERROR, indirect), deleteUnused (S_DLG_SIMPLE_MESSAGE, indirect), loadStudyOptionsFragment (S_STUDYOPTIONS_FRAG), onFinishedStartup (S_DLG_CONFIRMATION, indirect).

Not written (no direct page): handleDeckSelection and onCreateCustomStudySession (helper and listener methods; their pages are owned by listener or helper owners). Listener-only methods integrityCheck, mediaCheck, importAdd, importReplace, exportApkg, deleteDeck, emptyFiltered and handleEmptyCards also get no ENTERS.

Overlap: showDatabaseErrorDialog (batch 003) also reaches S_DLG_DATABASE_ERROR. The edges written here start at different sources (onCreate, onOptionsItemSelected, handleDbError, onCollectionLoadError), so they do not duplicate. The helper's own edge belongs to batch 003.

## 5. Open decisions

1. sup() for DatabaseErrorDialog.java:126 -> hasErrorFiles (CALL). Needs a graph_def.py helper; not this part's file.
2. ENV_STORAGE on onCreate -> S_PREFERENCES (directory-inaccessible branch). ENV_STORAGE was chosen; the coordinator may prefer another constant.
3. RESULT owner for S_CRASH_REPORT: not written. No RESULT edge from S_CRASH_REPORT to onActivityResult was found in this batch.
4. MG6 gate for deleteUnused (ENTERS to S_DLG_SIMPLE_MESSAGE and GUI from S_DLG_MEDIA_CHECK). Text only.
5. Fallback FAB DeckPicker$8 (DeckPicker.java:399-404): not registered by configureFloatingActionsMenu here. Only $9, $10 and $11 have REGISTER edges.
6. onCreate -> onAttachedToWindow (FRAMEWORK) is an approximation: the framework calls it after onResume.
7. MG notes (text only, env and needs_state unset): MG1 (unopenable or failed collection; no STATE), MG4 (failed sync; no STATE), MG5 (mod-schema confirmation; no STATE), MG6 (unused media; no STATE).
8. Batch-membership check: grep of label_003 to label_006 finds none of the batch-002 page ENTERS edges. No duplicates were found.

## 6. Other grep and source evidence

- onFinishedStartup( callers: DeckPicker.java:858 (fresh-install branch) and 958 (default branch). Both are inside showStartupScreensAndDialogs (805-960 is the onFinishedStartup region).
- onOptionsItemSelected dialog branches: 595-598 (check database, id 6), 600-603 (check media via showMediaCheckDialog), 610-614 (model browser, direct startActivityForResultWithAnimation), 616-619 (restore backup, id 7), 621-625 (export via showDialogFragment(ExportDialog.newInstance)).
- onCreate branches: 415-417 (colOpen true, startup screens), 418-434 (else, not open: 420-428 directory checks; 430-433 dialog ids 9 and 0).
- Framework lines (fw_src/android-8.1.0_r1): Activity.java 3169 (onAttachedToWindow, empty), 3386-3388 (onCreatePanelMenu -> onCreateOptionsMenu), 4382-4383 (permission request start), 5526-5528 (finish()), 7204-7208 (performDestroy -> onDestroy), 7267-7270 (dispatch -> dispatchRequestPermissionsResult), 7412-7419 (dispatchRequestPermissionsResult -> onRequestPermissionsResult); DecorView.java 1585-1590 (onAttachedToWindow -> window callback); ActivityThread.java 2747-2751 (callActivityOnRestoreInstanceState).
- Constants used (graph_def.py): ENV_STORAGE, ENV_PERM_STORAGE, STATE_COLLECTION, STATE_DECK.
