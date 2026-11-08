# conflicts_004 (batch 004: DeckPicker anonymous classes)

Files: label_004.md and label_004.py in graphs/AnkiDroid/parts/. Paths below are relative to final_java_only/AnkiDroid/app/AnkiDroid-#4200/AnkiDroid/src/main/java/com/ichi2/ unless noted.

## Cross-batch links this batch depends on (not written by label_004.py)

1. ASYNC DeckPicker.undo (DeckPicker.java:999) -> DeckTask TASK_TYPE_UNDO -> DeckPicker$13 onPreExecute/onPostExecute/onProgressUpdate (1006, 1011, 1019). Owner: DeckTask batch.
2. ASYNC DeckPicker.repairDeck (1112) -> $14 callbacks (1115, 1122, 1134). Owner: DeckTask batch.
3. ASYNC DeckPicker.integrityCheck (1147) -> $15 callbacks (1149, 1156, 1178). Owner: DeckTask batch.
4. ASYNC DeckPicker.mediaCheck (1191) -> $16 callbacks (1193, 1200, 1215). Owner: DeckTask batch.
5. ASYNC DeckTask dispatch to TaskListener adapter (DeckTask.java:344-347, 360-361, 368-369, 1299-1313). Owner: DeckTask batch.
6. ASYNC Connection dispatch to $17 callbacks (Connection.java:83-86 offline onDisconnected, 109-116, 124-131, 138-145, 152-158; Connection.java:287 publish). Owner: Connection batch.
7. Connection.cancel (Connection.java:539-543) is called from $17$1.onKey (DeckPicker.java:1340) and $17$1$1.onPositive (1354), then reaches $17.onCancelled. The static call is in batch 004; the Connection.onCancelled hop is owned by the Connection batch.
8. BROADCAST SdCardReceiver.onReceive (receiver/SdCardReceiver.java:42-56, sendBroadcast at 47 and 56) -> DeckPicker$18.onReceive (DeckPicker.java:1674-1680). Owner: SdCardReceiver batch.
9. INTENT IntentHandler.onCreate (IntentHandler.java:138 startActivityIfNeeded) -> DeckPicker.<init>. Owner: IntentHandler batch. DeckPicker.<init> then runs field initializers for $2.<init> (DeckPicker.java:193) and $17.<init> (1291).
10. INTENT DO_SYNC (IntentHandler.java:126-131) -> DialogHandler MSG_DO_SYNC (dialogs/DialogHandler.java:99-105) -> DeckPicker.sync(). Owner: IntentHandler and DialogHandler batches.
11. DIRECT calls (auto-extracted, not written here): dialogs/DatabaseErrorDialog.java:210 -> repairDeck; :302 -> integrityCheck; :177 and :181 -> showDatabaseErrorDialog; dialogs/MediaCheckDialog.java:70 -> mediaCheck; DeckPicker.java:928-929 -> integrityCheck; DeckPicker.java:369 -> registerExternalStorageListener.

## Nodes outside batch 004 that appear in the same source region (not labeled here)

- DeckPicker$10.<init> (created at DeckPicker.java:488), and $2.onClick (195-205). Owner batch to label these.

## MISSING GATE (no constant in graph_def.py lines 1-160)

- MG1 damaged or unopenable collection: $14.* (repair route), $15.<init> route (a), $15.onPostExecute failure path. The DatabaseErrorDialog is shown at DeckPicker.java:433 (LOAD_FAILED) and from handleDbError (1243-1245). Suggested text: "file: the collection cannot be opened or is damaged".
- MG2 undo available: all $13.* routes. The menu item is visible only when getCol().undoAvailable() (DeckPicker.java:511-517).
- MG3 collection written by an older schema (upgrade): $15.<init> route (b) via DeckPicker.java:928-929.
- MG4 device offline (negated ENV_NETWORK): $17.onDisconnected (Connection.java:83-86).
- MG5 API 14+ FAB menu (layout-v14): $10.onClick, $11.<init>, $11.onClick. minSdkVersion is 10 (build.gradle:12).

## Unreachable nodes and why

- onCancelled for $13, $14, $15, $16 (kind no_trigger_in_app). DeckTask.cancelTask(int) (DeckTask.java:181-185) cancels only when the type matches. Its only callers are CardBrowser for SEARCH_CARDS and RENDER_BROWSER_QA (CardBrowser.java:528-529, 796-797, 1155). TaskOperations.stopTaskGracefully (runtimetools/TaskOperations.java:33) is called only by LoadPronounciationActivity and TranslationActivity. If another batch later adds a cancel path to DeckTask, these four labels change.
- onProgressUpdate for $14, $15, $16 (kind framework_never_calls). None of the three doInBackground methods (DeckTask.java:667-694 and 1015-1021) calls publishProgress. ProgressCallback is used only by the importer (DeckTask.java:750).
- Total unreachable: 7 (4 onCancelled + 3 onProgressUpdate). Reachable: 33.

## Notes

- UNREACHABLE is not defined in graph_def.py lines 1-160, so the labels are written only in label_004.md. label_004.py holds only GUI edges.
- needs_state: the build report shows "needs_state edges: 0", so the keyword has never been used. label_004.py passes needs_state=STATE_ACCOUNT / STATE_CARDS as a text value, the same form as env=. The lead should confirm the e() keyword name.
- graphs/AnkiDroid/scratch/node_names.tsv decl_line values for anonymous classes are unreliable (same-name lookup). That file was not edited. Source lines were read directly.
- No coverage files, build_graph.py, network, gradle, adb, or git were used.
