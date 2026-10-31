# AnkiDroid batch 006 (LABEL helper). DeckPicker anonymous listeners: $5 (onPreExecute, onProgressUpdate),
# $6 (all five methods), $7 (all five), $8 (both), $9 (both), $9$1 (both). 18 methods; the full row list is in
# graphs/AnkiDroid/parts/label_006.md.
#
# Route ownership: the launchers importAdd (DeckPicker.java:1579-1582), importReplace (1587-1589) and exportApkg (1593-1623)
# belong to batch_002 (no label_002.py yet). Their ASYNC edges to the listener callbacks are NOT written here; the launcher's
# part writes them (see graphs/AnkiDroid/scratch/conflicts_006.md). Those callbacks are REACHABLE rows in the .md with
# "confirmed_by INFERRED" in the reason.
# The fallback FAB branch ($8) is closed on the standard API 27 config (closed_by_api_level).
# UNREACHABLE entries are assigned one key at a time.
# No env or needs_state gate is set on the GUI edges below: the screen is already open with the collection loaded.

e('DeckPicker$9.<init>', 'DeckPicker$9.onClick', 'REGISTER',
  'the add-deck listener is registered on the New deck button of the add menu',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:461-463',
  note='onClick is in this part. The builder does not follow REGISTER for reachability; the route is the S_DECKPICKER -> DeckPicker$9.onClick GUI edge below.')

e('S_DECKPICKER', 'DeckPicker$9.onClick', 'GUI',
  'tap the + button, then New deck in the add menu',
  gui=['tap the + button, then New deck in the add menu'],
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:391-393, 463-467; SRC res/layout-v14/floating_add_button.xml:7, 18',
  note='Page edge; the destination is in this part. The guard at line 464 passes on the standard API 27 path because mActionsMenu is set at line 391 and configureFloatingActionsMenu runs at line 393.')

e('DeckPicker$9$1.<init>', 'DeckPicker$9$1.onPositive', 'REGISTER',
  'the new-deck dialog callback is registered in the MaterialDialog builder',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:471-475',
  note='onPositive is in this part. The builder does not follow REGISTER for reachability; the route is the S_DECKPICKER -> DeckPicker$9$1.onPositive GUI edge below.')

e('S_DECKPICKER', 'DeckPicker$9$1.onPositive', 'GUI',
  'tap the + button, tap New deck in the add menu, then OK in the new-deck name dialog',
  gui=['tap the + button, tap New deck in the add menu, then OK in the new-deck name dialog'],
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:463-485',
  note='Page edge. The dialog is built only by DeckPicker$9.onClick (lines 471-485), so the route goes through the add-deck click. No env or needs_state gate is set.')

UNREACHABLE['DeckPicker$6.onCancelled'] = (
    'no_trigger_in_app',
    "The import-replace task type is never cancelled. DeckTask.cancelTask(int) cancels only when the type matches (DeckTask.java:181-185), and its callers are CardBrowser only (CardBrowser.java:528-529, 796-797, 1155). The no-argument DeckTask.cancelTask() (DeckTask.java:168-178) has no caller except cancelTask(int) (DeckTask.java:184). TaskOperations.stopTaskGracefully is called only with the activities' own task fields (LoadPronounciationActivity.java:471-479, TranslationActivity.java:404-405). DeckPicker.java:1340 and 1354 call Connection.cancel(), which cancels the sync Connection task (Connection.java:541), not DeckTask. AsyncTask runs onCancelled only after cancel() (FW-SRC core/java/android/os/AsyncTask.java:525-528, 691-698). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:307-309; SRC com/ichi2/async/DeckTask.java:181-186',
    'SOURCE')

UNREACHABLE['DeckPicker$7.onCancelled'] = (
    'no_trigger_in_app',
    "The export task type is never cancelled. The reasons are the same as for DeckPicker$6.onCancelled: DeckTask.cancelTask(int) (DeckTask.java:181-185) has only CardBrowser callers (CardBrowser.java:528-529, 796-797, 1155); the no-argument cancelTask() (DeckTask.java:168-178) is called only from cancelTask(int); TaskOperations.stopTaskGracefully is called only with the activities' own task fields (LoadPronounciationActivity.java:471-479, TranslationActivity.java:404-405); Connection.cancel() (DeckPicker.java:1340, 1354) cancels the sync Connection task, not DeckTask. AsyncTask runs onCancelled only after cancel() (FW-SRC core/java/android/os/AsyncTask.java:525-528, 691-698). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:340-342; SRC com/ichi2/async/DeckTask.java:181-186',
    'SOURCE')

UNREACHABLE['DeckPicker$7.onProgressUpdate'] = (
    'framework_never_calls',
    "The export task never publishes progress. doInBackgroundExportApkg (DeckTask.java:881-909) calls exporter.exportInto (line 895) and contains no publishProgress. The publishProgress calls in DeckTask.java are at 380, 420, 422, 457, 565, 601, 633, 659, 809 and 859, none inside 881-909. Across the app's java tree, publishProgress, ProgressCallback and doProgress occur only in DeckTask, Connection, the importers and the syncers; AnkiPackageExporter has none. AsyncTask dispatches onProgressUpdate only from publishProgress (FW-SRC core/java/android/os/AsyncTask.java:684-689, 714-716). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:335-337; SRC com/ichi2/async/DeckTask.java:881-909; FW-SRC core/java/android/os/AsyncTask.java:684-689',
    'SOURCE')

UNREACHABLE['DeckPicker$8.<init>'] = (
    'closed_by_api_level',
    "Created only in the fallback else branch (DeckPicker.java:394-405), which runs only when findViewById(R.id.add_content_menu) returns null (line 391). On the standard API 27 config the layout-v14 variant of floating_add_button.xml is selected (res/layout/deck_picker.xml:36 includes @layout/floating_add_button, and the v14 variant declares add_content_menu at line 7; the base layout has only add_note_action), so mActionsMenu is non-null and configureFloatingActionsMenu runs (line 393). minSdkVersion is 10 (build.gradle), so the branch is reachable only on API 10 to 13. The auto CALL edge DeckPicker.onCreate -> DeckPicker$8.<init> (line 399) is an over-approximation; see conflicts_006.md.",
    'SRC com/ichi2/anki/DeckPicker.java:391-405; SRC res/layout-v14/floating_add_button.xml:7; SRC res/layout/deck_picker.xml:36',
    'SOURCE')

UNREACHABLE['DeckPicker$8.onClick'] = (
    'closed_by_api_level',
    "Its only creator is the fallback else branch at DeckPicker.java:399-404, which is closed on the standard API 27 config for the same reason as DeckPicker$8.<init> (layout-v14 declares add_content_menu, line 391 is non-null, the else branch never runs). Reachable only on API 10 to 13 (minSdkVersion 10).",
    'SRC com/ichi2/anki/DeckPicker.java:391-405; SRC res/layout-v14/floating_add_button.xml:7',
    'SOURCE')
