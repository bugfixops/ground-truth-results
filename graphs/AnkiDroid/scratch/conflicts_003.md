# Batch 003 conflicts and open items (LABEL helper, DeckPicker)

Outputs: graphs/AnkiDroid/parts/label_003.py (15 e() calls, 0 UNREACHABLE), graphs/AnkiDroid/parts/label_003.md (40 REACHABLE rows, 15 EDGE rows). Checker c1_check.py: problems 0.

## Node-name data issues
- node_names.tsv decl_line is wrong for several batch 003 classes. Decl lines were taken from grep and auto_calls.json instead.
  - DeckPicker$1.onClick decl 183: correct (expander onClick at 183-187).
  - DeckPicker$10.onClick decl 183: wrong. Actual listener is at 488-492 (add-shared FAB).
  - DeckPicker$13.onPostExecute decl 240, DeckPicker$13.onCancelled decl 266, DeckPicker$13.onPreExecute decl 251: wrong. These copy the decl lines of the import listener at 238-266. Actual undo listener is at 999-1014.
  - DeckPicker$17.onPostExecute: wrong by the same pattern. Actual onPostExecute is at 1404 (mSyncListener starts at 1291).
  - DeckPicker$14/$15/$16 rows copy 240/251/260/266 too.
  - Summary notes said openReviewer, sync, undo, and mSyncListener onPostExecute decl_lines were unreliable. Confirmed.
- Anonymous class numbers were checked against auto_calls.json (the source of truth for these edges), not against textual order: $1.<init> 181, $10.<init> 488, $13.<init> 999, $16.<init> 1191, $17.<init> 1291, $18.<init> 1672, $22.<init> 1823, $25.<init> 2073.

## Edge ownership (coordinator rule 1)
- Page edges S_DECKPICKER -> destination are written here when the destination is a batch 003 method: openCardBrowser, onPrepareOptionsMenu, openReviewer, openStudyOptions, undo, sync(), showImportDialog(int), showMediaCheckDialog(int), DeckPicker$1.onClick.
- ASYNC edges written here (source calls execute or Connection.sync): updateDeckList -> DeckPicker$22.onPostExecute (batch_005); undo -> DeckPicker$13.onPostExecute (batch_004); sync(String) -> DeckPicker$17.onPostExecute (batch_004).
- DeckPicker$17.onDisconnected (DeckPicker.java:1299, offline) is reached through Connection (Connection.java:85, batch_068), not through an edge from sync(String), so no extra ASYNC edge was written for it.
- REGISTER edges written here ($1.<init> -> $1.onClick, $10.<init> -> $10.onClick) do not carry reachability (builder rule, see label_001.py note). Reachability for those two onClick methods comes from the S_DECKPICKER edges.
- Two page edges duplicate routes owned by other batches: openCardBrowser (NavigationDrawerActivity.java:263, batch_036) and openReviewer/openStudyOptions (handleDeckSelection, batch_002). Both are kept; duplicates should be harmless but the lead should confirm.

## Missing gates
- MG1 damaged or unopenable collection: used for repairDeck, restoreFromBackup, sendErrorReport, showDatabaseErrorDialog.
- MG2 undo available: used on the undo page edge and the undo -> $13 ASYNC route (undo menu item visibility, DeckPicker.java:511-517).
- MG3 older-schema upgrade: used on upgradePreferences (DeckPicker.java:925).
- MG4 offline: used on the sync(String) -> $17 ASYNC edge and the showSyncLogMessage row (DeckPicker.java:1299).
- Unnumbered gates, not assigned an MG number (coordinator to assign or confirm):
  - storage permission not yet granted (onRequestPermissionsResult, DeckPicker.java:450-451, firstCollectionOpen batch_002)
  - saved instance bundle exists (onRestoreInstanceState)
  - activity not finishing and no saved state (onSaveInstanceState, ActivityThread.java:4023-4025)
  - SD card not mounted at startup (onSdCardNotMounted from onCreate, DeckPicker.java:424)
  - deck has subdecks (DeckPicker$1.onClick, DeckPicker.java:185)
  - chosen deck is a filtered deck (rebuildFiltered, DeckPickerContextMenu.java:99-102)
  - backup file exists (restoreFromBackup)
- No env constant was invented. ENV_SDCARD_EVENT is cited in a reason only (the receiver route, DeckPicker.java:1676). STATE_CARDS and STATE_DECK are used on the two deck-tap edges. ENV_NETWORK is not used; MG4 is used for offline as the coordinator directed.

## Cross-batch dependencies (not written here)
- batch_002: DeckPicker.onCreate (calls configureFloatingActionsMenu 393, registerExternalStorageListener 369, showStartupScreensAndDialogs 417, onSdCardNotMounted 424, showDatabaseErrorDialog 433); firstCollectionOpen (442, requestPermissions 450-451); edges onCreate -> onRestoreInstanceState and firstCollectionOpen -> onRequestPermissionsResult; DeckPicker.<init> (field init 181); handleDeckSelection (1715-1798); onOptionsItemSelected (551-563, 596-618).
- batch_004: DeckPicker$10.onClick (492); DeckPicker$12.onPositive (477); DeckPicker$13 (undo listener, onPostExecute 1011-1014, openReviewer call 1014); DeckPicker$16 (mediaCheck listener, onPostExecute 1207); DeckPicker$17 (mSyncListener, onDisconnected 1299, onPostExecute 1404-1541); DeckPicker$18 (mUnmountReceiver, onReceive 1676-1678).
- batch_005: DeckPicker$22 (updateDeckList listener, onPostExecute 1834-1868); DeckPicker$25 (mSimpleProgressListener, 2073).
- batch_036: NavigationDrawerActivity.onNavigationItemSelected (case nav_browser 262-263).
- batch_038: StudyOptionsFragment (line 329 renameDeckDialog(long); line 658 onRequireDeckListUpdate via mListener). Note: the enclosing method at line 658 is a StudyOptionsFragment method, not StudyOptionsFragment$3. The name StudyOptionsFragment$3 in the earlier notes is not a node in batch files.
- batch_041: DatabaseErrorDialog (115 sendErrorReport, 210 repairDeck, 258 restoreFromBackup).
- batch_042: DeckPickerContextMenu (99-102 filtered items; 129 showContextMenuDeckOptions; 142 renameDeckDialog; 147 showContextMenuExportDialog; 154 onRequireDeckListUpdate; 160 rebuildFiltered); DeckPickerContextMenu$1.onSelection.
- batch_044: MediaCheckDialog (70, $1.onPositive -> mediaCheck).
- batch_045: SyncErrorDialog (94 sync(); 139/153/186/199 sync(String); 210 mediaCheck).
- batch_056: DialogHandler (66 showImportDialog(int,String); 70 showSyncErrorDialog(int,String); 83 showMediaCheckDialog(int,List); 87 showDatabaseErrorDialog; 105 sync()).
- batch_068: Connection (sync dispatch; Connection.java:85 onDisconnected, 143 onPostExecute).

## Unsettled
- Unnumbered gates above need MG numbers or a ruling.
- Whether page edges that duplicate other batches' routes should be kept (see Edge ownership).
- DeckPicker$17.onDisconnected and the other $17 callbacks depend on Connection dispatch (batch_068); not written here.
