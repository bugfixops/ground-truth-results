# AnkiDroid batch 010 (LABEL helper). CardBrowser anonymous listeners and callbacks: $2, $3, $4, $5,
# $13 to $17 (DeckTask TaskListeners) and $18 (runtime BroadcastReceiver). 40 methods; the full row list is in
# graphs/AnkiDroid/parts/label_010.md.
#
# Route ownership: CardBrowser.<init>, onCollectionLoaded, onActivityResult, searchCards, onStop, onDestroy,
# registerExternalStorageListener and the context-menu listener CardBrowser$1.onSelection belong to batch_009.
# CardBrowser$7.onItemClick, RenderOnScroll.onScroll, onScrollStateChanged and CardBrowser$6 belong to batch_011.
# SdCardReceiver (the manifest receiver) belongs to batch_017. The ASYNC edges from those launchers to the
# DeckTask callbacks here are NOT written in this part; the launcher's part writes them. Those callbacks are
# REACHABLE rows in the .md with "confirmed_by INFERRED" in the reason.
# CardBrowser$6 has no method in this batch (batch_011 owns its two callbacks).
# REGISTER edges from an <init> are written here with a note: the builder does not follow REGISTER for
# reachability, so the route is the GUI or FRAMEWORK edge from the page or the framework node.
# The saved-search dialog edges carry needs_state=STATE_SETTINGS: saved searches live in col.conf 'savedFilters'
# and there is no saved-search STATE kind (MG note).

# --- sort-order dialog listener ($2). Set in CardBrowserOrderDialog.newInstance (CardBrowser.java:657).
e('CardBrowser$2.<init>', 'CardBrowser$2.onSelection', 'REGISTER',
  'the sort-order listener is passed to the order dialog and stored in its static field',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:216-217, 657; SRC com/ichi2/anki/dialogs/CardBrowserOrderDialog.java:15, 24, 50',
  note='onSelection is in this part. The builder does not follow REGISTER for reachability; the route is the S_DLG_CARDBROWSER_ORDER -> CardBrowser$2.onSelection GUI edge below.')

e('S_DLG_CARDBROWSER_ORDER', 'CardBrowser$2.onSelection', 'GUI',
  'open the sort dialog from the card browser menu, then tap a sort order',
  gui=['open the sort dialog from the card browser menu, then tap a sort order'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:655-658, 219-254; SRC com/ichi2/anki/dialogs/CardBrowserOrderDialog.java:50',
  note='Page edge; the destination is in this part. The MaterialDialog callback dispatch is library code not in the dataset: INFERRED. No env or needs_state gate.')

# --- saved-searches dialog listener ($3). Set in CardBrowserMySearchesDialog.newInstance (CardBrowser.java:638, 652).
e('CardBrowser$3.<init>', 'CardBrowser$3.OnSelection', 'REGISTER',
  'the saved-searches listener is passed to the dialog and stored in its static field',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:259-260, 638, 652; SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:37, 46',
  note='OnSelection is in this part. The builder does not follow REGISTER for reachability; the route is the S_DLG_CARDBROWSER_SEARCHES -> CardBrowser$3.OnSelection GUI edge below.')

e('CardBrowser$3.<init>', 'CardBrowser$3.OnRemoveSearch', 'REGISTER',
  'the saved-searches listener is passed to the dialog and stored in its static field',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:259-260, 638, 652; SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:37, 46',
  note='OnRemoveSearch is in this part. The builder does not follow REGISTER for reachability; the route is the S_DLG_CARDBROWSER_SEARCHES -> CardBrowser$3.OnRemoveSearch GUI edge below.')

e('CardBrowser$3.<init>', 'CardBrowser$3.OnSaveSearch', 'REGISTER',
  'the saved-searches listener is passed to the dialog and stored in its static field',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:259-260, 638, 652; SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:37, 46',
  note='OnSaveSearch is in this part. The builder does not follow REGISTER for reachability; the route is the S_DLG_CARDBROWSER_SEARCHES -> CardBrowser$3.OnSaveSearch GUI edge below.')

e('S_DLG_CARDBROWSER_SEARCHES', 'CardBrowser$3.OnSelection', 'GUI',
  'open My searches from the card browser menu, then tap a saved search',
  gui=['open My searches from the card browser menu, then tap a saved search'],
  needs_state=STATE_SETTINGS,
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:642-654, 262-270; SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:73',
  note='Page edge. Needs at least one saved search in col.conf savedFilters (CardBrowser.java:263), modelled as STATE_SETTINGS (MG note). The dialog item click is library-backed: INFERRED.')

e('S_DLG_CARDBROWSER_SEARCHES', 'CardBrowser$3.OnRemoveSearch', 'GUI',
  'open My searches from the card browser menu, tap the remove button of a saved search, then OK',
  gui=['open My searches from the card browser menu, tap the remove button of a saved search, then OK'],
  needs_state=STATE_SETTINGS,
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:109-112, 161-166; SRC com/ichi2/anki/CardBrowser.java:273-288',
  note='Page edge. Needs at least one saved search (STATE_SETTINGS, MG note). The confirm callback is library-backed: INFERRED.')

e('S_DLG_CARDBROWSER_SEARCHES', 'CardBrowser$3.OnSaveSearch', 'GUI',
  'open the save-search dialog from the card browser menu, enter a name, then save',
  gui=['open the save-search dialog from the card browser menu, enter a name, then save'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:636-640, 291-296; SRC com/ichi2/anki/dialogs/CardBrowserMySearchesDialog.java:85',
  note='Page edge. No gate: the empty-name case returns at CardBrowser.java:292-296 and the non-empty name reaches the method. The dialog callback is library-backed: INFERRED.')

# --- toolbar deck spinner ($4). Created in onCollectionLoaded (CardBrowser.java:373-374).
e('CardBrowser$4.<init>', 'CardBrowser$4.onItemSelected', 'REGISTER',
  'the toolbar spinner listener is registered on the deck spinner',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:373-374',
  note='onItemSelected is in this part. The builder does not follow REGISTER for reachability; the routes are the S_CARDBROWSER edges below.')

e('CardBrowser$4.<init>', 'CardBrowser$4.onNothingSelected', 'REGISTER',
  'the toolbar spinner listener is registered on the deck spinner',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:373-374',
  note='onNothingSelected is in this part (UNREACHABLE below). The builder does not follow REGISTER for reachability.')

e('S_CARDBROWSER', 'CardBrowser$4.onItemSelected', 'FRAMEWORK',
  'the card browser opens: the framework lays out the deck spinner and selects position 0 (the default deck), which fires onItemSelected',
  env=None,
  evidence='FW-SRC core/java/android/widget/AdapterView.java:1034-1085, 937-947, 1103-1110; FW-SRC core/java/android/widget/Spinner.java:637-648, 681; SRC com/ichi2/anki/CardBrowser.java:373-378',
  note='Page edge. The default selection (position 0 after setAdapter) is set in AbsSpinner, which is not in fw_src: INFERRED for that step. The GUI edge below is the alternative route.')

e('S_CARDBROWSER', 'CardBrowser$4.onItemSelected', 'GUI',
  'pick another deck in the toolbar drop-down of the card browser',
  gui=['pick another deck in the toolbar drop-down of the card browser'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:376-378, 772-792; SRC com/ichi2/anki/widgets/DeckDropDownAdapter.java:19',
  note='Page edge. Needs two or more decks in the drop-down (no STATE kind written: the default deck always exists, see the UNREACHABLE note on onNothingSelected).')

# --- first-column spinner ($5). Created in onCollectionLoaded (CardBrowser.java:415-417).
e('CardBrowser$5.<init>', 'CardBrowser$5.onItemSelected', 'REGISTER',
  'the first-column spinner listener is registered on the column spinner',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:415-417',
  note='onItemSelected is in this part. The builder does not follow REGISTER for reachability; the routes are the S_CARDBROWSER edges below.')

e('CardBrowser$5.<init>', 'CardBrowser$5.onNothingSelected', 'REGISTER',
  'the first-column spinner listener is registered on the column spinner',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:415-417',
  note='onNothingSelected is in this part (UNREACHABLE below). The builder does not follow REGISTER for reachability.')

e('S_CARDBROWSER', 'CardBrowser$5.onItemSelected', 'FRAMEWORK',
  'the card browser opens: the framework lays out the first-column spinner and selects position 0, which fires onItemSelected (the body changes nothing when the position is unchanged)',
  env=None,
  evidence='FW-SRC core/java/android/widget/AdapterView.java:1034-1085, 937-947, 1103-1110; FW-SRC core/java/android/widget/Spinner.java:637-648, 681; SRC com/ichi2/anki/CardBrowser.java:419-427',
  note='Page edge. The default selection is set in AbsSpinner, which is not in fw_src: INFERRED for that step. The GUI edge below is the alternative route.')

e('S_CARDBROWSER', 'CardBrowser$5.onItemSelected', 'GUI',
  'pick another first column in the card browser column spinner',
  gui=['pick another first column in the card browser column spinner'],
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:419-427; SRC res/layout/card_browser.xml:25-30',
  note='Page edge. The spinner has no visibility gate in the layout (card_browser.xml:25-30).')

# --- SD-card receiver ($18). Registered in registerExternalStorageListener (CardBrowser.java:1320-1330).
e('CardBrowser$18.<init>', 'CardBrowser$18.onReceive', 'REGISTER',
  'the MEDIA_EJECT receiver is registered while the card browser is open',
  env=None,
  evidence='SRC com/ichi2/anki/CardBrowser.java:1318-1330',
  note='onReceive is in this part. The builder does not follow REGISTER for reachability; the route is the S_CARDBROWSER -> CardBrowser$18.onReceive SYSTEM edge below.')

e('S_CARDBROWSER', 'CardBrowser$18.onReceive', 'SYSTEM',
  'the SD card is ejected while the card browser is open (ACTION_MEDIA_EJECT, delivered to SdCardReceiver, which re-broadcasts MEDIA_EJECT)',
  env=ENV_SDCARD_EVENT,
  evidence='SRC AndroidManifest.xml:268-282; SRC com/ichi2/anki/receiver/SdCardReceiver.java:42-47; SRC com/ichi2/anki/CardBrowser.java:1322-1326; FW-SRC core/java/android/content/Intent.java:2701',
  note='Page edge; the destination is in this part. The first hop (system delivery of ACTION_MEDIA_EJECT to a manifest receiver on API 27) is not verifiable from fw_src: INFERRED. SdCardReceiver is batch_017; the edge is written here, not in that part.')

# --- UNREACHABLE entries.
UNREACHABLE['CardBrowser$13.onCancelled'] = (
    'no_trigger_in_app',
    "The update-note task (TASK_TYPE_UPDATE_FACT) is never cancelled. DeckTask.cancelTask(int) cancels only when the type matches (DeckTask.java:181-186), and its only callers are CardBrowser SEARCH_CARDS and RENDER_BROWSER_QA (CardBrowser.java:528-529, 796-797, 1155). The no-argument DeckTask.cancelTask() (DeckTask.java:168-178) is reached only from cancelTask(int) (DeckTask.java:184). The only direct cancel(true) on a DeckTask is sLatestInstance inside cancelTask() (DeckTask.java:172); TaskOperations.stopTaskGracefully cancels only the activities' own BackgroundPost and DownloadFileTask fields (LoadPronounciationActivity.java:474-478, TranslationActivity.java:405). AsyncTask runs onCancelled only after cancel() (AsyncTask.java:525-528, 691-698). Body is empty (CardBrowser.java:924-925).",
    'SRC com/ichi2/async/DeckTask.java:168-186; SRC com/ichi2/anki/CardBrowser.java:528-529, 796-797, 924-925, 1155; SRC com/ichi2/anki/runtimetools/TaskOperations.java:30-35; SRC com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:474-478; SRC com/ichi2/anki/multimediacard/activity/TranslationActivity.java:405; FW-SRC core/java/android/os/AsyncTask.java:525-528, 691-698',
    'SOURCE')

UNREACHABLE['CardBrowser$14.onCancelled'] = (
    'no_trigger_in_app',
    "The suspend task (TASK_TYPE_DISMISS, suspend) is never cancelled. The reasons are the same as for CardBrowser$13.onCancelled: DeckTask.cancelTask(int) has only the SEARCH_CARDS and RENDER_BROWSER_QA callers (CardBrowser.java:528-529, 796-797, 1155), and the no-argument cancelTask() is reached only from cancelTask(int) (DeckTask.java:184). Body is empty (CardBrowser.java:1024-1025).",
    'SRC com/ichi2/async/DeckTask.java:168-186; SRC com/ichi2/anki/CardBrowser.java:528-529, 796-797, 1024-1025, 1155; FW-SRC core/java/android/os/AsyncTask.java:525-528, 691-698',
    'SOURCE')

UNREACHABLE['CardBrowser$15.onCancelled'] = (
    'no_trigger_in_app',
    "The delete-note task (TASK_TYPE_DISMISS, delete) is never cancelled. The reasons are the same as for CardBrowser$13.onCancelled: DeckTask.cancelTask(int) has only the SEARCH_CARDS and RENDER_BROWSER_QA callers (CardBrowser.java:528-529, 796-797, 1155), and the no-argument cancelTask() is reached only from cancelTask(int) (DeckTask.java:184). Body is empty (CardBrowser.java:1047-1048).",
    'SRC com/ichi2/async/DeckTask.java:168-186; SRC com/ichi2/anki/CardBrowser.java:528-529, 796-797, 1047-1048, 1155; FW-SRC core/java/android/os/AsyncTask.java:525-528, 691-698',
    'SOURCE')

UNREACHABLE['CardBrowser$4.onNothingSelected'] = (
    'framework_never_calls',
    "The toolbar deck spinner is filled from the deck list (DeckDropDownAdapter over mDropDownDecks = allSorted(), CardBrowser.java:366-373). AdapterView fires onNothingSelected only when the selected position is negative (fireOnSelected, AdapterView.java:937-947), and handleDataChanged leaves nothing selected only when the adapter has no selectable item (AdapterView.java:1038, 1057-1085). The deck list is never empty because the default deck (id 1) cannot be deleted (Decks.java:285-287), so the adapter always has a selectable item (DeckDropDownAdapter.java:19, BaseAdapter.java:68). The claim that the default deck always exists in the collection is INFERRED. Body is '// do nothing' (CardBrowser.java:381-383).",
    'SRC com/ichi2/anki/CardBrowser.java:366-373, 381-383; SRC com/ichi2/libanki/Decks.java:285-287; SRC com/ichi2/anki/widgets/DeckDropDownAdapter.java:19; FW-SRC core/java/android/widget/AdapterView.java:937-947, 1038, 1057-1085; FW-SRC core/java/android/widget/BaseAdapter.java:68',
    'INFERRED')

UNREACHABLE['CardBrowser$5.onNothingSelected'] = (
    'framework_never_calls',
    "The first-column spinner is filled from ArrayAdapter.createFromResource over R.array.browser_column1_headings (CardBrowser.java:412-415), a static array of two items (res/values/02-strings.xml:56-59). The array is never empty and its items are enabled (ArrayAdapter has no isEnabled override; BaseAdapter.isEnabled defaults to true, BaseAdapter.java:68), so handleDataChanged always finds a selectable position (AdapterView.java:1038, 1057-1085) and fireOnSelected never receives a negative position (AdapterView.java:937-947). Body is '// Do Nothing' (CardBrowser.java:432-434).",
    'SRC com/ichi2/anki/CardBrowser.java:412-415, 432-434; SRC res/values/02-strings.xml:56-59; FW-SRC core/java/android/widget/ArrayAdapter.java:73, 506; FW-SRC core/java/android/widget/BaseAdapter.java:68; FW-SRC core/java/android/widget/AdapterView.java:937-947, 1038, 1057-1085',
    'SOURCE')
