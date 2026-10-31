# AnkiDroid batch 031 (LABEL helper). ModelBrowser part 1: 40 methods (ModelBrowser, its listeners $1 to $6$1 and their constructors).
# The full row list is in graphs/AnkiDroid/parts/label_031.md.
# Edges here: source in batch 031, or page S_* with the destination in batch 031. Automatic CALL edges (auto_calls.json)
# are not written here. The ASYNC launch edges use the launching method as the source.

# --- Options menu of the note type list (page S_MODELBROWSER).
e('S_MODELBROWSER', 'ModelBrowser.onCreateOptionsMenu', 'FRAMEWORK',
  'the note type list builds its options menu (the add button in the toolbar)',
  env=None,
  evidence='FW-SRC core/java/android/app/Activity.java:3386-3388; SRC com/ichi2/anki/ModelBrowser.java:203-207',
  note='The framework calls onCreatePanelMenu, which calls onCreateOptionsMenu (Activity.java:3388). The menu is inflated from R.menu.model_browser (ModelBrowser.java:205). No gate.')

e('S_MODELBROWSER', 'ModelBrowser.onOptionsItemSelected', 'GUI',
  'tap the add button or the up arrow in the note type list toolbar',
  env=None,
  gui=['tap the add button or the up arrow in the note type list toolbar'],
  evidence='FW-SRC core/java/android/app/Activity.java:3439-3450; SRC com/ichi2/anki/ModelBrowser.java:210-221; RES src/main/res/menu/model_browser.xml:5-8',
  note='Activity.onMenuItemSelected calls onOptionsItemSelected (Activity.java:3450). The add item is shown always (model_browser.xml:5-8). The up arrow (android.R.id.home) calls onBackPressed (ModelBrowser.java:212-213). No gate.')

# --- List rows (the list is filled in fillModelList after COUNT_MODELS delivers the note types).
e('S_MODELBROWSER', 'ModelBrowser$4.onItemClick', 'GUI',
  'tap a note type in the list (opens its field editor)',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['tap a note type in the list (opens its field editor)'],
  evidence='FW-SRC core/java/android/widget/AdapterView.java:314-318; SRC com/ichi2/anki/ModelBrowser.java:271-281, 108-118, 240',
  note='The listener is set in fillModelList (ModelBrowser.java:271-281), which runs after COUNT_MODELS delivers the list (ModelBrowser.java:108-118, 240). Before that the list is empty, so the gate is STATE_COLLECTION. The click is dispatched by AdapterView.performItemClick (AdapterView.java:318).')

e('S_MODELBROWSER', 'ModelBrowser$5.onItemLongClick', 'GUI',
  'long-press a note type in the list (opens the note type context menu)',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['long-press a note type in the list (opens the note type context menu)'],
  evidence='FW-SRC core/java/android/widget/AbsListView.java:3237, 3314; SRC com/ichi2/anki/ModelBrowser.java:283-292, 108-118, 240',
  note='Same list gate as the click edge: the listener is set in fillModelList after the collection loads (ModelBrowser.java:283-292, 240). AbsListView calls the listener at AbsListView.java:3237 and :3314.')

# --- Context menu of a note type row (page S_DLG_MODELBROWSER_CONTEXT).
e('S_DLG_MODELBROWSER_CONTEXT', 'ModelBrowser$3.onSelection', 'GUI',
  'tap Template, Rename or Delete in the note type long-press menu',
  env=None,
  gui=['tap Template, Rename or Delete in the note type long-press menu'],
  evidence='SRC com/ichi2/anki/dialogs/ModelBrowserContextMenu.java:12-14, 28-41; SRC com/ichi2/anki/ModelBrowser.java:160-175, 288-289',
  note='The menu is built with itemsCallback(mContextMenuListener) (ModelBrowserContextMenu.java:39). The three entries are MODEL_TEMPLATE, MODEL_RENAME and MODEL_DELETE (ModelBrowserContextMenu.java:32-34). The menu opens from the long press (ModelBrowser.java:288-289). No gate of its own: the list gate is on the long-press edge.')

# --- Add note type dialog (opened by the add button; the dialog has no page node of its own).
e('S_MODELBROWSER', 'ModelBrowser$6.onPositive', 'GUI',
  'tap OK in the Add note type dialog that the add button opens',
  env=None,
  gui=['tap OK in the Add note type dialog that the add button opens'],
  evidence='SRC com/ichi2/anki/ModelBrowser.java:215-217, 309-390',
  note='The dialog is a MaterialDialog built in addNewNoteTypeDialog (ModelBrowser.java:353-390), not a DialogFragment, so it has no page node; its page is S_MODELBROWSER. addNewNoteTypeDialog is called from onOptionsItemSelected (ModelBrowser.java:216, automatic CALL). No gate.')

# --- Field editor and template editor (INTENT).
e('ModelBrowser$4.onItemClick', 'ModelFieldEditor.<init>', 'INTENT',
  'open the field editor of the tapped note type (explicit Intent with noteTypeID)',
  env=None,
  evidence='SRC com/ichi2/anki/ModelBrowser.java:274-279; SRC com/ichi2/anki/AnkiActivity.java:186-190',
  note='INTENT check: explicit component (ModelFieldEditor.class), no framework gate. The extras are title and noteTypeID (ModelBrowser.java:277-278). The start goes through AnkiActivity.startActivityForResultWithAnimation (AnkiActivity.java:186-190). The ModelFieldEditor.<init> node is the constructor of the lifecycle chain (graph_def.py:191-192).')

e('ModelBrowser.openTemplateEditor', 'CardTemplateEditor.<init>', 'INTENT',
  'open the card template editor of the chosen note type (explicit Intent with modelId)',
  env=None,
  evidence='SRC com/ichi2/anki/ModelBrowser.java:549-553; SRC com/ichi2/anki/AnkiActivity.java:186-190',
  note='INTENT check: explicit component (CardTemplateEditor.class) with the modelId extra (ModelBrowser.java:550-551), started with REQUEST_TEMPLATE_EDIT (ModelBrowser.java:552). No framework gate. The same destination is used by graph_def.py:2134 (NoteEditor).')

# --- Result of the template editor (page S_CARDTEMPLATEEDITOR is the child).
e('S_CARDTEMPLATEEDITOR', 'ModelBrowser.onActivityResult', 'RESULT',
  'return from the card template editor to the note type list (request code 3)',
  env=None,
  evidence='SRC com/ichi2/anki/ModelBrowser.java:60, 552, 677-682; FW-SRC core/java/android/app/Activity.java:5679, 7259-7266',
  note='Page edge; S_CARDTEMPLATEEDITOR is the child launched by openTemplateEditor (edge above). The framework dispatches the result to onActivityResult (Activity.java:7266). Request code 3 relaunches COUNT_MODELS (ModelBrowser.java:679-680). No gate: the child returns to the parent in any result code.')

# --- Collection loaded (same pattern as the CardBrowser precedent, label_009.py:35-39).
e('ModelBrowser.onCreate', 'ModelBrowser.onCollectionLoaded', 'ASYNC',
  'the collection loader delivers onLoadFinished after startLoadingCollection',
  env=None,
  evidence='SRC com/ichi2/anki/ModelBrowser.java:182-192, 237-241; SRC com/ichi2/anki/AnkiActivity.java:255-262, 283-290',
  note='startLoadingCollection restarts the loader (AnkiActivity.java:261), and AnkiActivity.onLoadFinished calls onCollectionLoaded (AnkiActivity.java:286). The loader callback that reaches onLoadFinished is the Android LoaderManager, not in fw_src: INFERRED. The call from onLoadFinished to onCollectionLoaded is automatic.')

# --- DeckTask launch sites for the COUNT_MODELS listener $1. The DeckTask.TaskListener default edges into $1 are automatic.
e('ModelBrowser.onCollectionLoaded', 'ModelBrowser$1.onPreExecute', 'ASYNC',
  'the COUNT_MODELS task starts (launched from onCollectionLoaded) and runs its pre-execute callback',
  env=None,
  evidence='SRC com/ichi2/anki/ModelBrowser.java:240, 103-105; SRC com/ichi2/async/DeckTask.java:129-134, 344-347, 1299-1301; FW-SRC core/java/android/os/AsyncTask.java:632-648',
  note='AsyncTask.executeOnExecutor calls onPreExecute (AsyncTask.java:648); DeckTask.onPreExecute delegates to the listener (DeckTask.java:346); the interface default into $1 is automatic (DeckTask.java:1300). This edge is the launch link.')

e('ModelBrowser.onCollectionLoaded', 'ModelBrowser$1.onPostExecute', 'ASYNC',
  'the COUNT_MODELS task finishes and delivers its result to the note type list',
  env=None,
  evidence='SRC com/ichi2/anki/ModelBrowser.java:240, 108-118; SRC com/ichi2/async/DeckTask.java:129-134, 360-365, 1305-1307; FW-SRC core/java/android/os/AsyncTask.java:691-695',
  note='AsyncTask.finish calls onPostExecute when the task is not cancelled (AsyncTask.java:693-695); DeckTask.onPostExecute delegates to the listener (DeckTask.java:362); the interface default into $1 is automatic (DeckTask.java:1306). This edge is the launch link.')

e('ModelBrowser.fullRefresh', 'ModelBrowser$1.onPreExecute', 'ASYNC',
  'a full reload of the note type list starts the COUNT_MODELS task again',
  env=None,
  evidence='SRC com/ichi2/anki/ModelBrowser.java:571-573, 103-105; SRC com/ichi2/async/DeckTask.java:129-134, 344-347, 1299-1301; FW-SRC core/java/android/os/AsyncTask.java:648',
  note='fullRefresh is called from addNewNoteType (ModelBrowser.java:432, automatic CALL). The launch link is the same as the onCollectionLoaded edge; the launch is in fullRefresh (ModelBrowser.java:572).')

e('ModelBrowser.fullRefresh', 'ModelBrowser$1.onPostExecute', 'ASYNC',
  'the reloaded COUNT_MODELS task delivers the note types to the list',
  env=None,
  evidence='SRC com/ichi2/anki/ModelBrowser.java:571-573, 108-118; SRC com/ichi2/async/DeckTask.java:129-134, 360-365, 1305-1307; FW-SRC core/java/android/os/AsyncTask.java:691-695',
  note='Same launch link as above, for the result: AsyncTask.finish calls onPostExecute (AsyncTask.java:695), DeckTask forwards it (DeckTask.java:362), and the interface default is automatic (DeckTask.java:1306).')

e('ModelBrowser.onActivityResult', 'ModelBrowser$1.onPreExecute', 'ASYNC',
  'returning from the template editor reloads the note type list (COUNT_MODELS starts)',
  env=None,
  evidence='SRC com/ichi2/anki/ModelBrowser.java:677-682; SRC com/ichi2/async/DeckTask.java:129-134, 344-347, 1299-1301; FW-SRC core/java/android/os/AsyncTask.java:648',
  note='The launch is in onActivityResult for request code 3 (ModelBrowser.java:679-680). The launch link is the same as the onCollectionLoaded edge.')

e('ModelBrowser.onActivityResult', 'ModelBrowser$1.onPostExecute', 'ASYNC',
  'the COUNT_MODELS task started after the template editor returns delivers the list',
  env=None,
  evidence='SRC com/ichi2/anki/ModelBrowser.java:677-682, 108-118; SRC com/ichi2/async/DeckTask.java:129-134, 360-365, 1305-1307; FW-SRC core/java/android/os/AsyncTask.java:691-695',
  note='Same launch link for the result, as in the onCollectionLoaded edge.')

# --- Delete note type task: DELETE_MODEL listener $2 (launched from deleteModel).
e('ModelBrowser.deleteModel', 'ModelBrowser$2.onPreExecute', 'ASYNC',
  'the DELETE_MODEL task starts (launched from deleteModel) and shows the progress bar',
  env=None,
  evidence='SRC com/ichi2/anki/ModelBrowser.java:578-586, 137-140; SRC com/ichi2/async/DeckTask.java:129-134, 344-347, 1299-1301; FW-SRC core/java/android/os/AsyncTask.java:648',
  note='deleteModel launches DELETE_MODEL with the listener $2 (ModelBrowser.java:579-580). AsyncTask.executeOnExecutor calls onPreExecute (AsyncTask.java:648); the interface default into $2 is automatic (DeckTask.java:1300).')

e('ModelBrowser.deleteModel', 'ModelBrowser$2.onPostExecute', 'ASYNC',
  'the DELETE_MODEL task finishes and refreshes the note type list',
  env=None,
  evidence='SRC com/ichi2/anki/ModelBrowser.java:578-586, 143-149; SRC com/ichi2/async/DeckTask.java:129-134, 360-365, 1305-1307; FW-SRC core/java/android/os/AsyncTask.java:691-695',
  note='AsyncTask.finish calls onPostExecute when not cancelled (AsyncTask.java:695); DeckTask forwards it (DeckTask.java:362); the interface default into $2 is automatic (DeckTask.java:1306). The body calls refreshList (ModelBrowser.java:148).')

# --- Second dialog of the add note type flow (MaterialDialog, no page node). Its OK callback is $6$1 (batch 032 owns $6$1.onPositive).
e('ModelBrowser$6.onPositive', 'ModelBrowser$6$1.onPositive', 'FRAMEWORK',
  'tap OK in the second Add note type dialog (the name input) that the first OK opens',
  env=None,
  gui=['tap OK in the second Add note type dialog (the name input) that the first OK opens'],
  evidence='SRC com/ichi2/anki/ModelBrowser.java:374-386',
  note='Method edge: $6.onPositive builds the second MaterialDialog with the ButtonCallback $6$1 (:374-378) and shows it (.show() at :386). The OK dispatch to $6$1.onPositive is library code (not in the dataset): INFERRED. $6$1.onPositive calls addNewNoteType at :382 (batch 032). No gate.')

# --- Rename note type dialog (MaterialDialog, no page node). Its OK callback is $9 (batch 032 owns $9.onPositive).
e('ModelBrowser.renameModelDialog', 'ModelBrowser$9.onPositive', 'FRAMEWORK',
  'tap OK in the rename note type dialog (opened by the context menu Rename entry)',
  env=None,
  gui=['tap OK in the rename note type dialog (opened by the context menu Rename entry)'],
  evidence='SRC com/ichi2/anki/ModelBrowser.java:503-508, 531',
  note='Method edge: renameModelDialog builds the MaterialDialog with the ButtonCallback $9 (:503-508) and shows it (.show() at :531). The OK dispatch is library code (not in the dataset): INFERRED. No gate.')

# --- Delete note type confirmation (ConfirmationDialog page). Two show calls: :466 and :484. Confirm and cancel callbacks are batch 032.
e('ModelBrowser.deleteModelDialog', 'S_DLG_CONFIRMATION', 'ENTERS',
  'the delete note type confirmation dialog (ConfirmationDialog) is shown',
  env=None,
  evidence='SRC com/ichi2/anki/ModelBrowser.java:448, 466, 484, 490',
  note='MISSING GATE MG252: the dialog opens only when the note type list holds at least two note types (mModelIds.size() > 1, ModelBrowser.java:448); no predefined STATE kind covers the count. Two show calls use this page: :466 (dialog d, when col.modSchema() does not throw at :450) and :484 (dialog c, the catch branch at :467, full-sync text). The confirm and cancel callbacks are batch 032 (label_032.py). The else branch shows the last-model toast (:490).')

# --- Context menu of a note type row (ModelBrowserContextMenu page), shown by the long-press listener.
e('ModelBrowser$5.onItemLongClick', 'S_DLG_MODELBROWSER_CONTEXT', 'ENTERS',
  'the note type context menu is shown for the long-pressed row',
  env=None,
  evidence='SRC com/ichi2/anki/ModelBrowser.java:283-292 (newInstance at :288, showDialogFragment at :289)',
  note='ENTERS edge: method to page. The listener runs only after the list is filled (STATE_COLLECTION on the S_MODELBROWSER edge above). No gate of its own.')

# --- UNREACHABLE: the listener callbacks onCancelled and onProgressUpdate of $1 (COUNT_MODELS) and $2 (DELETE_MODEL).
UNREACHABLE['ModelBrowser$1.onCancelled'] = ('no_trigger_in_app',
  ("DeckTask.onCancelled (DeckTask.java:367-370) calls the listener onCancelled only after the task is cancelled. "
   "COUNT_MODELS (41) is never cancelled in the app: DeckTask.cancelTask(int) (DeckTask.java:181-184) cancels the latest task only when its type equals the argument, "
   "and its only callers pass TASK_TYPE_SEARCH_CARDS and TASK_TYPE_RENDER_BROWSER_QA (CardBrowser.java:528-529, 796-797, 1155). "
   "The no-argument cancelTask() (DeckTask.java:168-178) is called only from cancelTask(int) (DeckTask.java:184)."
   "No class extends DeckTask. The other cancel(true) calls act on non-DeckTask tasks (Connection.java:541; Statistics.java:543, 574, 681, 692; "
   "TaskOperations.java:33 with the LoadPronounciationActivity and TranslationActivity callers). So ModelBrowser$1.onCancelled never runs."),
  ('SRC com/ichi2/async/DeckTask.java:168-184, 367-370; SRC com/ichi2/anki/CardBrowser.java:528-529, 796-797, 1155; '
   'SRC com/ichi2/anki/runtimetools/TaskOperations.java:30-33; SRC com/ichi2/async/Connection.java:541; '
   'SRC com/ichi2/anki/Statistics.java:543, 574, 681, 692; SRC com/ichi2/anki/ModelBrowser.java:98-100'),
  'SOURCE')

UNREACHABLE['ModelBrowser$1.onProgressUpdate'] = ('no_trigger_in_app',
  ("DeckTask.onProgressUpdate (DeckTask.java:352-355) calls the listener only when a DeckTask calls publishProgress. "
   "COUNT_MODELS (DeckTask.java:1089-1126) does not publish: no publishProgress call lies in DeckTask.java:1089-1139, and the publishProgress calls "
   "(DeckTask.java:380, 420, 422, 457, 565, 601, 633, 659, 809, 859) all lie outside that range. "
   "The listener body is empty (ModelBrowser.java:121-123: 'This decktask does not publish updates'). So ModelBrowser$1.onProgressUpdate never runs."),
  ('SRC com/ichi2/async/DeckTask.java:352-355, 380, 420, 422, 457, 565, 601, 633, 659, 809, 859, 1089-1139; SRC com/ichi2/anki/ModelBrowser.java:121-123'),
  'SOURCE')

UNREACHABLE['ModelBrowser$2.onCancelled'] = ('no_trigger_in_app',
  ("DeckTask.onCancelled (DeckTask.java:367-370) calls the listener onCancelled only after the task is cancelled. "
   "DELETE_MODEL (42) is never cancelled in the app: DeckTask.cancelTask(int) (DeckTask.java:181-184) cancels the latest task only when its type equals the argument, "
   "and its only callers pass TASK_TYPE_SEARCH_CARDS and TASK_TYPE_RENDER_BROWSER_QA (CardBrowser.java:528-529, 796-797, 1155). "
   "The no-argument cancelTask() (DeckTask.java:168-178) is called only from cancelTask(int) (DeckTask.java:184)."
   "No class extends DeckTask. The other cancel(true) calls act on non-DeckTask tasks (Connection.java:541; Statistics.java:543, 574, 681, 692; "
   "TaskOperations.java:33 with the LoadPronounciationActivity and TranslationActivity callers). The listener body is empty (ModelBrowser.java:133-135). So ModelBrowser$2.onCancelled never runs."),
  ('SRC com/ichi2/async/DeckTask.java:168-184, 367-370; SRC com/ichi2/anki/CardBrowser.java:528-529, 796-797, 1155; '
   'SRC com/ichi2/anki/runtimetools/TaskOperations.java:30-33; SRC com/ichi2/async/Connection.java:541; '
   'SRC com/ichi2/anki/Statistics.java:543, 574, 681, 692; SRC com/ichi2/anki/ModelBrowser.java:133-135'),
  'SOURCE')

UNREACHABLE['ModelBrowser$2.onProgressUpdate'] = ('no_trigger_in_app',
  ("DeckTask.onProgressUpdate (DeckTask.java:352-355) calls the listener only when a DeckTask calls publishProgress. "
   "DELETE_MODEL (DeckTask.java:1127-1139) does not publish: no publishProgress call lies in DeckTask.java:1089-1139, and the publishProgress calls "
   "(DeckTask.java:380, 420, 422, 457, 565, 601, 633, 659, 809, 859) all lie outside that range. "
   "The listener body is empty (ModelBrowser.java:152-154: 'This decktask does not publish updates'). So ModelBrowser$2.onProgressUpdate never runs."),
  ('SRC com/ichi2/async/DeckTask.java:352-355, 380, 420, 422, 457, 565, 601, 633, 659, 809, 859, 1089-1139; SRC com/ichi2/anki/ModelBrowser.java:152-154'),
  'SOURCE')
