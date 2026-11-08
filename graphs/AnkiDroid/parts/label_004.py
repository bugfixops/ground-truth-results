# Batch 004 (DeckPicker anonymous classes).
# Names used (graph_def.py): gui (line 25), ENV_NETWORK (120), ENV_STORAGE (121), STATE_CARDS (128), STATE_ACCOUNT (132).
# UNREACHABLE is a local dict for this part (not a graph_def name). Its keys are the 7 UNREACHABLE rows in label_004.md.
# REACHABLE rows are only in label_004.md. AsyncTask/Connection dispatch edges are owned by the DeckPicker part that calls execute() (not written here).
# Routes owned by other batches (DeckTask, Connection, SdCardReceiver, IntentHandler, dialog callers) are in graphs/AnkiDroid/scratch/conflicts_004.md.

UNREACHABLE = {}

UNREACHABLE['DeckPicker$13.onCancelled'] = (
    'no_trigger_in_app',
    "The undo task is never cancelled in the app. DeckTask.cancelTask(int) cancels only when the type matches (DeckTask.java:181-185), and its only callers are CardBrowser for SEARCH_CARDS and RENDER_BROWSER_QA (CardBrowser.java:528-529, 796-797, 1155). TaskOperations.stopTaskGracefully is called only by LoadPronounciationActivity and TranslationActivity, not by DeckTask. AsyncTask runs onCancelled only after cancel() (FW-SRC core/java/android/os/AsyncTask.java:479-480,525-527).",
    'SRC com/ichi2/anki/DeckPicker.java:1001-1003',
    'SOURCE')

UNREACHABLE['DeckPicker$14.onCancelled'] = (
    'no_trigger_in_app',
    "The repair task type is never cancelled (DeckTask.cancelTask(int) callers are CardBrowser only, see $13.onCancelled). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:1139-1141',
    'SOURCE')

UNREACHABLE['DeckPicker$14.onProgressUpdate'] = (
    'framework_never_calls',
    "doInBackgroundRepairDeck (DeckTask.java:687-694) calls no publishProgress. The publishProgress calls in DeckTask.java are at 380, 420, 422, 457, 565, 601, 633, 659, 809 and 859, none inside this method. ProgressCallback is used only by the importer (DeckTask.java:750). AsyncTask dispatches onProgressUpdate only from publishProgress (FW-SRC core/java/android/os/AsyncTask.java:684-689,714-716). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:1134-1135',
    'SOURCE')

UNREACHABLE['DeckPicker$15.onCancelled'] = (
    'no_trigger_in_app',
    "The check-database task type is never cancelled (see $13.onCancelled). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:1183-1184',
    'SOURCE')

UNREACHABLE['DeckPicker$15.onProgressUpdate'] = (
    'framework_never_calls',
    "doInBackgroundCheckDatabase (DeckTask.java:667-684) calls no publishProgress (see $14.onProgressUpdate for the full check). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:1178-1179',
    'SOURCE')

UNREACHABLE['DeckPicker$16.onCancelled'] = (
    'no_trigger_in_app',
    "The check-media task type is never cancelled (see $13.onCancelled). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:1220-1221',
    'SOURCE')

UNREACHABLE['DeckPicker$16.onProgressUpdate'] = (
    'framework_never_calls',
    "doInBackgroundCheckMedia (DeckTask.java:1015-1021) calls no publishProgress. The only progress path outside DeckTask is ProgressCallback, which is used only by the importer (DeckTask.java:750). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:1215-1216',
    'SOURCE')

gui('S_DECKPICKER', 'DeckPicker$10.onClick',
    'tap the + button, then the add-shared-deck button in the add menu',
    evidence='SRC com/ichi2/anki/DeckPicker.java:488-494; SRC res/layout-v14/floating_add_button.xml:27')

gui('S_DECKPICKER', 'DeckPicker$11.onClick',
    'tap the + button, then the add-note button in the add menu',
    evidence='SRC com/ichi2/anki/DeckPicker.java:495-500; SRC res/layout-v14/floating_add_button.xml:36')

gui('S_DECKPICKER', 'DeckPicker$12.onPositive',
    'options menu: New filtered deck, then Create in the name dialog (menu item enabled only with SD card mounted)',
    env=ENV_STORAGE,
    evidence='SRC com/ichi2/anki/DeckPicker.java:527,566-590')

gui('S_DECKPICKER', 'DeckPicker$17$1.onKey',
    'press Back while a sync progress dialog is showing (cancel the running sync)',
    env=ENV_NETWORK, needs_state=STATE_ACCOUNT,
    evidence='SRC com/ichi2/anki/DeckPicker.java:1328-1340')

gui('S_DECKPICKER', 'DeckPicker$17$1$1.onPositive',
    'during sync, press Back after 2 s, then OK in the cancel-sync confirmation',
    env=ENV_NETWORK, needs_state=STATE_ACCOUNT,
    evidence='SRC com/ichi2/anki/DeckPicker.java:1350-1354')

gui('S_DECKPICKER', 'DeckPicker$19.onClick',
    'select a deck whose daily study limit is reached (new or review cards still waiting), then the Study more snackbar button',
    needs_state=STATE_CARDS,
    evidence='SRC com/ichi2/anki/DeckPicker.java:1744-1752')
