# AnkiDroid batch 139 (LABEL helper). AnkiActivity (4 methods), AudioView (9), BarGraph (9),
# BasicTextFieldController (9), DeckPicker (9). 40 methods in total.
# Source row: graphs/AnkiDroid/scratch/batches_ai.tsv, part 139. The full row list (label, kind, reason, printed file:lines)
# is in graphs/AnkiDroid/parts/label_139.md. 39 methods are labelled REACHABLE, 1 is UNREACHABLE (DeckPicker.sendErrorReport).
#
# Route gaps in out/ that the edges below close:
# - AnkiActivity.onLoadFinished and AnkiActivity.onLoaderReset have no inbound edge. Written here: FRAMEWORK
#   AnkiActivity.startLoadingCollection -> onLoadFinished and -> onLoaderReset (LoaderManager is INFERRED).
# - S_DLG_DECKPICKER_CONTEXT, S_DLG_DECKPICKER_EXPORT_DONE and S_DLG_SYNC_ERROR have GUI edges in graph_def.py but no
#   inbound ENTERS edge. Written here: ENTERS from DeckPicker$4.onLongClick, DeckPicker$7.onPostExecute and
#   DeckPicker.showSyncErrorDialog(int,String).
#
# Already routed, not repeated here: AudioView listeners and BasicAudioFieldController (graph_def.py:6766-6787, 7168-7175);
# BasicTextFieldController listeners and callers (graph_def.py:7376-7442); MultimediaEditFieldActivity.onActivityResult
# RESULT edge (graph_def.py:7422); ChartView.onDraw from S_STATISTICS (graph_def.py:7657); Statistics.onCreate ->
# S_STATISTICS (graph_def.py:11196); S_DLG_DECKPICKER_DELETE_DECK (graph_def.py:897); DeckPickerContextMenu,
# DeckPickerExportCompleteDialog and SyncErrorDialog listeners (graph_def.py:5399, 5439, 5853);
# AnkiActivity.startLoadingCollection -> onCreateLoader (graph_def.py:10948).
# Automatic CALL edges come from auto_calls.json (bytecode) and are not written here.

# --- Loader callbacks: restartLoader in startLoadingCollection hands the result to onLoadFinished.
e('AnkiActivity.startLoadingCollection', 'AnkiActivity.onLoadFinished', 'FRAMEWORK',
  'the collection loader is restarted and the loader framework delivers the result to onLoadFinished',
  env=None,
  evidence='SRC com/ichi2/anki/AnkiActivity.java:254-262, 283-290',
  note='restartLoader(0, null, this) (AnkiActivity.java:261) makes this the LoaderCallbacks. The delivery to onLoadFinished is the support-library LoaderManager step: INFERRED, source not read. onLoadFinished then calls onCollectionLoaded (AnkiActivity.java:286) or onCollectionLoadError (AnkiActivity.java:288), which are automatic CALL edges. Precedent: parts/label_127.py:22 (onCreateLoader).')

e('AnkiActivity.startLoadingCollection', 'AnkiActivity.onLoaderReset', 'FRAMEWORK',
  'the loader framework resets the collection loader and calls onLoaderReset',
  env=None,
  evidence='SRC com/ichi2/anki/AnkiActivity.java:254-262, 294-296',
  note='INFERRED, source not read: restarting the loader with the same id replaces the existing loader instance, and the LoaderManager resets it. The body is empty (AnkiActivity.java:294-296), so this edge only gives reachability.')

# --- Page ENTERS: the deck context menu opens from the deck row long-press listener.
e('DeckPicker$4.onLongClick', 'S_DLG_DECKPICKER_CONTEXT', 'ENTERS',
  'a deck row is long-pressed: the deck context menu dialog opens',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:227-236',
  note='showDialogFragment(DeckPickerContextMenu.newInstance(deckId)) at DeckPicker.java:233. The listener has no guard. Existing GUI edges from S_DLG_DECKPICKER_CONTEXT: graph_def.py:985, 989, 5399.')

# --- Page ENTERS: the export-complete dialog opens from the export task's onPostExecute.
e('DeckPicker$7.onPostExecute', 'S_DLG_DECKPICKER_EXPORT_DONE', 'ENTERS',
  'the deck export task finishes with an export path: the export-complete dialog opens',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:321-332',
  note='The dialog opens only when exportPath is not null (DeckPicker.java:327-328); otherwise a toast is shown (DeckPicker.java:330). The export task reaches this listener through graph_def.py:1100 (exportApkg ASYNC). Existing GUI edges from S_DLG_DECKPICKER_EXPORT_DONE: graph_def.py:1035, 5439, 5446.')

# --- Page ENTERS: the sync error dialog opens from DeckPicker.showSyncErrorDialog(int,String).
e('DeckPicker.showSyncErrorDialog(int,String)', 'S_DLG_SYNC_ERROR', 'ENTERS',
  'a sync error dialog is requested with an id: the sync error dialog opens',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1048-1051, 1058-1062, 1281-1282',
  note='MISSING GATE MG4: the dialog id (SyncErrorDialog.DIALOG_*) is not modelled as a state, as in the existing S_DLG_SYNC_ERROR edges (graph_def.py:1039-1046). The not-logged-in path enters through showSyncErrorDialog(int) (DeckPicker.java:1050), called from sync() (DeckPicker.java:1282). Existing GUI edges from S_DLG_SYNC_ERROR: graph_def.py:1039, 1044, 5853.')

# --- UNREACHABLE: DatabaseErrorDialog case DIALOG_DB_ERROR (id 1) is the only path to sendErrorReport.
UNREACHABLE['DeckPicker.sendErrorReport'] = ('branch_never_taken',
    "The only caller is DatabaseErrorDialog$2.onNegative (DatabaseErrorDialog.java:115), inside case DIALOG_DB_ERROR (id 1, DatabaseErrorDialog.java:96-117). The dialog is created only by DeckPicker.showDatabaseErrorDialog(int) (DeckPicker.java:1026-1027), and every caller of that method passes a constant other than DIALOG_DB_ERROR (DeckPicker.java:431, 433, 597, 618, 1244; DatabaseErrorDialog.java:86, 110, 178-194, 232, 288, 317; DialogHandler.java:60). The one non-constant caller, DialogHandler.java:87, replays a message stored by AnkiActivity.java:365 from DatabaseErrorDialog.getDialogHandlerMessage (DatabaseErrorDialog.java:428-430), so it only ever replays a value that came from one of those constants. No value 1 enters the cycle, so the method is never entered. The existing DatabaseErrorDialog$2 entries (graph_def.py:5562-5577) are not duplicated here.",
    'SRC com/ichi2/anki/DeckPicker.java:431, 433, 597, 618, 1026-1027, 1244; SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:28, 47-52, 86, 96-117, 110, 178-194, 232, 288, 317, 358, 383, 428-430; SRC com/ichi2/anki/dialogs/DialogHandler.java:60, 85-87; SRC com/ichi2/anki/AnkiActivity.java:365',
    'SOURCE')
