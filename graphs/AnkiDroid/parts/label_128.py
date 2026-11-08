# AnkiDroid batch 128 (LABEL helper). 39 methods; the full row list is in graphs/AnkiDroid/parts/label_128.md.
# Batch: IntentHandler and its $1 constructor, NoteEditor and its $1 constructor, UIUtils.getDayStart,
# UIUtils.saveCollectionInBackground, UIUtils$1.<init>, DialogHandler (3 methods), ConfirmModSchemaException.<init>,
# StorageAccessException.<init>(String), 18 StatsMetaInfo setters, BaseAsyncTask.<clinit> and BaseAsyncTask.<init>.
#
# Route ownership:
# - Every other route into this batch is an automatic CALL edge from the builder (auto_calls.json). Those are not
#   written here.
# - The S_ENTRY, LIFECYCLE and INTENT edges into IntentHandler, NoteEditor and the NoteEditor constructor already
#   exist in graph_def.py (lines 139-141, 147, 185-186, 197-198, 316-320, 328-332, 545-564, 1253, 1324, 1925,
#   2090, 2127, 2982). They are not repeated.
# - Two edges have a source in this batch and a destination the builder does not link: the listener methods of the
#   anonymous DeckTask.TaskListener created in UIUtils.saveCollectionInBackground (UIUtils$1.onPreExecute and
#   onPostExecute, both UNRESOLVED in methods.csv).
# - One edge models the Handler dispatch of a stored dialog message: DialogHandler.readMessage -> handleMessage.
#
# No UNREACHABLE entries: every method in this batch has a route.

e('UIUtils.saveCollectionInBackground', 'UIUtils$1.onPreExecute', 'ASYNC',
  'the save-collection task starts and DeckTask.onPreExecute delivers onPreExecute to the listener',
  env=None,
  needs_state=STATE_COLLECTION,
  evidence='SRC com/ichi2/async/DeckTask.java:344-346, 1276-1279; SRC com/ichi2/anki/UIUtils.java:113-119',
  note='The listener is the anonymous DeckTask.TaskListener created at UIUtils.java:115 (UIUtils$1). The edge is taken only when colIsOpen() holds (guard at UIUtils.java:114), so the state is STATE_COLLECTION. The DeckTask dispatch is the AsyncTask lifecycle, so the kind is ASYNC.')

e('UIUtils.saveCollectionInBackground', 'UIUtils$1.onPostExecute', 'ASYNC',
  'the save-collection task finishes and DeckTask.onPostExecute delivers the result to the listener',
  env=None,
  needs_state=STATE_COLLECTION,
  evidence='SRC com/ichi2/async/DeckTask.java:359-362, 1276-1287; SRC com/ichi2/anki/UIUtils.java:113-125',
  note='Same listener and the same colIsOpen() guard (UIUtils.java:114) as the onPreExecute edge. The onPostExecute body (UIUtils.java:123-125) only logs.')

e('DialogHandler.readMessage', 'DialogHandler.handleMessage', 'ASYNC',
  'the stored dialog message is posted to the Handler queue and dispatched to handleMessage on the main looper',
  env=None,
  needs_state=STATE_SESSION,
  guard='sStoredMessage is not null: a message was stored earlier in this process by DialogHandler.storeMessage',
  evidence='SRC com/ichi2/anki/dialogs/DialogHandler.java:28, 56, 130-136; FW-SRC core/java/android/os/Handler.java:97-106, 596-600',
  note='DialogHandler extends Handler (DialogHandler.java:28). readMessage calls sendMessage(sStoredMessage) (line 133). The Handler route is sendMessage -> sendMessageDelayed (Handler.java:596-600), then the looper calls dispatchMessage, which calls handleMessage (Handler.java:97-106). The stored-message precondition has no ENV constant. STATE_SESSION is the closest fit, because the static field is set only in the same process. No MG id is used.')
