# AnkiDroid batch 005 (LABEL helper). DeckPicker anonymous listeners and callbacks: deck taps and long-press,
# the deck-count load, the snackbar actions and callbacks, rename, delete, rebuild and empty filtered decks,
# find empty cards, and import.
# Edges written here: (a) GUI edges from S_DECKPICKER to batch 005 listeners (the destination is in batch 005,
# coordinator rule 1); (b) REGISTER edges whose source is a batch 005 <init> node.
# ASYNC edges belong to the part that starts the task (batch_002 or batch_003) and are not written here.
# UNREACHABLE entries: the 9 callbacks with no trigger in the app or no publishProgress call.
# The other rows are REACHABLE in graphs/AnkiDroid/parts/label_005.md (no UNREACHABLE entry for them).
# Names used (graph_def.py): gui (line 25), STATE_DECK (line 128). Missing gates MG6 and MG7 are notes in label_005.md only.

gui('S_DECKPICKER', 'DeckPicker$2.onClick',
    'tap a deck in the deck list (the deck row, not the counts area)',
    needs_state=STATE_DECK,
    evidence='SRC com/ichi2/anki/DeckPicker.java:195-207,384')

gui('S_DECKPICKER', 'DeckPicker$3.onClick',
    'tap the due counts of a deck in the deck list',
    needs_state=STATE_DECK,
    evidence='SRC com/ichi2/anki/DeckPicker.java:212-224,385; SRC com/ichi2/anki/DeckPicker.java:1735')

gui('S_DECKPICKER', 'DeckPicker$4.onLongClick',
    'long-press a deck in the deck list (opens the deck context menu)',
    needs_state=STATE_DECK,
    evidence='SRC com/ichi2/anki/DeckPicker.java:229-235,387')

gui('S_DECKPICKER', 'DeckPicker$20.onClick',
    'select an empty deck (no cards, no subdecks, not filtered), then tap Help in the snackbar',
    evidence='SRC com/ichi2/anki/DeckPicker.java:1769-1778')

gui('S_DECKPICKER', 'DeckPicker$21.onClick',
    'select a deck with subdecks or cards but nothing due, then tap Custom study in the snackbar',
    evidence='SRC com/ichi2/anki/DeckPicker.java:1784-1794')

e('DeckPicker$3.<init>', 'DeckPicker$3.onClick', 'REGISTER',
  'the counts listener is set on the deck adapter',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:210,385',
  note='The builder does not follow REGISTER for reachability; the route to onClick is the S_DECKPICKER -> DeckPicker$3.onClick edge.')

e('DeckPicker$4.<init>', 'DeckPicker$4.onLongClick', 'REGISTER',
  'the long-click listener is set on the deck adapter',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:227,387',
  note='The builder does not follow REGISTER for reachability; the route to onLongClick is the S_DECKPICKER -> DeckPicker$4.onLongClick edge.')

e('DeckPicker$20.<init>', 'DeckPicker$20.onClick', 'REGISTER',
  'the Help action listener is passed to UIUtils.showSnackbar',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1773-1778; SRC com/ichi2/anki/UIUtils.java:56-58',
  note='The builder does not follow REGISTER for reachability; the route to onClick is the S_DECKPICKER -> DeckPicker$20.onClick edge.')

e('DeckPicker$21.<init>', 'DeckPicker$21.onClick', 'REGISTER',
  'the Custom study action listener is passed to UIUtils.showSnackbar',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1786-1794; SRC com/ichi2/anki/UIUtils.java:56-58',
  note='The builder does not follow REGISTER for reachability; the route to onClick is the S_DECKPICKER -> DeckPicker$21.onClick edge.')

e('DeckPicker$26.<init>', 'DeckPicker$26.onDismissed', 'REGISTER',
  'the show/hide callback is passed to every snackbar that handleDeckSelection shows',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1754,1778,1794,2151; SRC com/ichi2/anki/UIUtils.java:56-58',
  note='Snackbar.Callback dispatch is library code with no source in the dataset; onDismissed is INFERRED in label_005.md.')

e('DeckPicker$26.<init>', 'DeckPicker$26.onShown', 'REGISTER',
  'the show/hide callback is passed to every snackbar that handleDeckSelection shows',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1754,1778,1794,2151; SRC com/ichi2/anki/UIUtils.java:56-58',
  note='Snackbar.Callback dispatch is library code with no source in the dataset; onShown is INFERRED in label_005.md.')

e('DeckPicker$23.<init>', 'DeckPicker$23.onPositive', 'FRAMEWORK',
  'the rename dialog calls onPositive when its positive button is tapped (MaterialDialog.ButtonCallback)',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1921-1925,1938-1956',
  note='Library dispatch (no source in the dataset). The dialog is shown only after $23.<init> is constructed in renameDeckDialog(long).')

e('DeckPicker$23.<init>', 'DeckPicker$23.onNegative', 'FRAMEWORK',
  'the rename dialog calls onNegative when its negative button is tapped (MaterialDialog.ButtonCallback)',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1921-1925,1958-1961',
  note='Library dispatch (no source in the dataset). Same dialog as onPositive.')

e('DeckPicker$27$1.<init>', 'DeckPicker$27$1.confirm', 'FRAMEWORK',
  'the confirmation dialog calls confirm() when its positive button is tapped',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:2188-2195; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-43',
  note='Library dispatch (no source in the dataset). The dialog is shown only from DeckPicker$27.onPostExecute when the count is non-zero.')

UNREACHABLE['DeckPicker$5.onCancelled'] = (
    'no_trigger_in_app',
    "The import task is never cancelled in the app. DeckTask.cancelTask(int) cancels only when the task type matches (DeckTask.java:181-186), and its only callers are CardBrowser for SEARCH_CARDS and RENDER_BROWSER_QA (CardBrowser.java:528-529, 796-797, 1155). TaskOperations.stopTaskGracefully is called only with the caller's own task (TranslationActivity.java:405). AsyncTask runs onCancelled only after cancel() (FW-SRC core/java/android/os/AsyncTask.java:525-527,691-698). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:265-267; SRC com/ichi2/async/DeckTask.java:181-186; SRC com/ichi2/anki/CardBrowser.java:528-529; SRC com/ichi2/anki/multimediacard/activity/TranslationActivity.java:405',
    'SOURCE')

UNREACHABLE['DeckPicker$22.onCancelled'] = (
    'no_trigger_in_app',
    "The deck-count load task is never cancelled in the app (DeckTask.cancelTask(int) callers are CardBrowser only, see $5.onCancelled). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:1881-1882; SRC com/ichi2/async/DeckTask.java:181-186',
    'SOURCE')

UNREACHABLE['DeckPicker$22.onProgressUpdate'] = (
    'framework_never_calls',
    "doInBackgroundLoadDeckCounts (DeckTask.java:480-491) calls no publishProgress, so AsyncTask never dispatches onProgressUpdate for this task type. AsyncTask dispatches onProgressUpdate only from publishProgress (FW-SRC core/java/android/os/AsyncTask.java:684-689,714-716). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:1877-1878; SRC com/ichi2/async/DeckTask.java:480-491; FW-SRC core/java/android/os/AsyncTask.java:684-689,714-716',
    'SOURCE')

UNREACHABLE['DeckPicker$24.onCancelled'] = (
    'no_trigger_in_app',
    "The delete-deck task is never cancelled in the app (DeckTask.cancelTask(int) callers are CardBrowser only, see $5.onCancelled). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:2065-2066; SRC com/ichi2/async/DeckTask.java:181-186',
    'SOURCE')

UNREACHABLE['DeckPicker$24.onProgressUpdate'] = (
    'framework_never_calls',
    "doInBackgroundDeleteDeck (DeckTask.java:719-725) calls no publishProgress, so AsyncTask never dispatches onProgressUpdate for this task type (see $22.onProgressUpdate). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:2060-2061; SRC com/ichi2/async/DeckTask.java:719-725; FW-SRC core/java/android/os/AsyncTask.java:684-689,714-716',
    'SOURCE')

UNREACHABLE['DeckPicker$25.onCancelled'] = (
    'no_trigger_in_app',
    "The rebuild and empty filtered-deck tasks are never cancelled in the app (DeckTask.cancelTask(int) callers are CardBrowser only, see $5.onCancelled). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:2096-2097; SRC com/ichi2/async/DeckTask.java:181-186',
    'SOURCE')

UNREACHABLE['DeckPicker$25.onProgressUpdate'] = (
    'framework_never_calls',
    "doInBackgroundRebuildCram (DeckTask.java:728-733) and doInBackgroundEmptyCram (DeckTask.java:736-741) call no publishProgress, so AsyncTask never dispatches onProgressUpdate for these task types (see $22.onProgressUpdate). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:2091-2092; SRC com/ichi2/async/DeckTask.java:728-741; FW-SRC core/java/android/os/AsyncTask.java:684-689,714-716',
    'SOURCE')

UNREACHABLE['DeckPicker$27.onCancelled'] = (
    'no_trigger_in_app',
    "The find-empty-cards task is never cancelled in the app (DeckTask.cancelTask(int) callers are CardBrowser only, see $5.onCancelled). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:2209-2211; SRC com/ichi2/async/DeckTask.java:181-186',
    'SOURCE')

UNREACHABLE['DeckPicker$27.onProgressUpdate'] = (
    'framework_never_calls',
    "doInBackGroundFindEmptyCards (DeckTask.java:1228-1232) calls no publishProgress, so AsyncTask never dispatches onProgressUpdate for this task type (see $22.onProgressUpdate). Body is empty.",
    'SRC com/ichi2/anki/DeckPicker.java:2204-2206; SRC com/ichi2/async/DeckTask.java:1228-1232; FW-SRC core/java/android/os/AsyncTask.java:684-689,714-716',
    'SOURCE')
