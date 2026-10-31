# AnkiDroid batch 068 (LABEL helper). BaseAsyncTask (5 methods), CollectionLoader (6), Connection (20),
# Connection$CancelCallback (3) and Connection$Payload (4). The full row list is in
# graphs/AnkiDroid/parts/label_068.md.
#
# Route ownership:
# - The ASYNC framework-dispatch edges from Connection.launchConnectionTask, Connection.cancel, the three
#   Connection.publishProgress overloads and the CollectionLoader callbacks are written here.
# - Auto CALL edges (super calls, call sites) come from auto_calls.json and are not repeated here.
# - The DeckPicker key listener into Connection.cancel is owned by the DeckPicker part.
#
# Gates: MG622 (batch range MG622-MG631). The CollectionLoader onStartLoading -> loadInBackground edge uses MG622.

# --- Connection.launchConnectionTask: the AsyncTask framework dispatch (Connection.java:97-100).
e('Connection.launchConnectionTask', 'Connection.onPreExecute', 'ASYNC',
  'AsyncTask.execute runs onPreExecute on the calling thread before the worker starts',
  evidence='SRC com/ichi2/async/Connection.java:81-102, 124-131; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-650',
  note='Framework dispatch (FW-SRC line 648). ASYNC follows the AsyncTask convention in label_019.py.')

e('Connection.launchConnectionTask', 'Connection.doInBackground', 'ASYNC',
  'execute starts the AsyncTask worker, which calls doInBackground on the background thread',
  evidence='SRC com/ichi2/async/Connection.java:81-102, 173-179; FW-SRC core/java/android/os/AsyncTask.java:326-340, 594-596',
  note='Framework dispatch: the worker calls doInBackground (FW-SRC line 333). The executor step is not printed (INFERRED).')

e('Connection.launchConnectionTask', 'Connection.onPostExecute', 'ASYNC',
  'finish calls onPostExecute on the main thread when the task was not cancelled',
  evidence='SRC com/ichi2/async/Connection.java:81-102, 138-145; FW-SRC core/java/android/os/AsyncTask.java:691-697',
  note='Framework dispatch (FW-SRC line 695). ASYNC follows the AsyncTask convention in label_019.py.')

# --- Connection.publishProgress overloads: posted progress is delivered to onProgressUpdate (FW-SRC 684-718).
e('Connection.publishProgress(int)', 'Connection.onProgressUpdate', 'ASYNC',
  'publishProgress posts a progress message that handleMessage delivers to onProgressUpdate on the main thread',
  evidence='SRC com/ichi2/async/Connection.java:461-463, 152-157; FW-SRC core/java/android/os/AsyncTask.java:684-689, 706-718',
  note='Framework dispatch: publishProgress (FW-SRC 684-689), then handleMessage calls onProgressUpdate (FW-SRC 706-718, line 715).')

e('Connection.publishProgress(int,long,long)', 'Connection.onProgressUpdate', 'ASYNC',
  'publishProgress posts a progress message that handleMessage delivers to onProgressUpdate on the main thread',
  evidence='SRC com/ichi2/async/Connection.java:471-473, 152-157; FW-SRC core/java/android/os/AsyncTask.java:684-689, 706-718',
  note='Framework dispatch, as for publishProgress(int) (FW-SRC 684-689, 706-718).')

e('Connection.publishProgress(String)', 'Connection.onProgressUpdate', 'ASYNC',
  'publishProgress posts a progress message that handleMessage delivers to onProgressUpdate on the main thread',
  evidence='SRC com/ichi2/async/Connection.java:466-468, 152-157; FW-SRC core/java/android/os/AsyncTask.java:684-689, 706-718',
  note='Framework dispatch, as for publishProgress(int) (FW-SRC 684-689, 706-718).')

# --- Connection.cancel: cancel(true) reaches onCancelled through the framework (Connection.java:539-543).
e('Connection.cancel', 'Connection.onCancelled', 'ASYNC',
  'cancel(true) makes the framework call onCancelled(result) on the main thread',
  evidence='SRC com/ichi2/async/Connection.java:539-543, 109-117; FW-SRC core/java/android/os/AsyncTask.java:345-358, 462-464, 525-528, 691-697',
  note='Framework cancel path: cancel(true) (FW-SRC 525-528), the future done step (FW-SRC 345-358), then finish calls onCancelled(result) (FW-SRC 691-697, 462-464). The DeckPicker route into cancel is owned by the DeckPicker part.')

# --- CollectionLoader: the start and the background load (CollectionLoader.java:47-55, 19-29).
e('CollectionLoader.onStartLoading', 'CollectionLoader.loadInBackground', 'ASYNC',
  'forceLoad runs loadInBackground on a background thread when the collection is not locked',
  evidence='SRC com/ichi2/async/CollectionLoader.java:47-55, 19-29; com/ichi2/async/Connection.java:277-279, 452-456',
  note='MISSING GATE MG622: the collection is not locked when the load starts (CollectionLoader.java:49-52). Connection.java:279 locks the collection during a sync and Connection.java:456 unlocks it. No predefined ENV or STATE constant fits, so env and needs_state are unset. The support-library forceLoad step is INFERRED, source not read.')

e('CollectionLoader.loadInBackground', 'CollectionLoader.deliverResult', 'ASYNC',
  'the support-library AsyncTaskLoader delivers the loadInBackground result to deliverResult',
  evidence='SRC com/ichi2/async/CollectionLoader.java:19-29, 31-44',
  note='The support-library AsyncTaskLoader delivers the result after loadInBackground returns (INFERRED, source not read). deliverResult forwards the value when the loader is started (line 41).')

# --- UNREACHABLE: Connection$CancelCallback is never constructed in the source root (Connection.java:549-566).
UNREACHABLE['Connection$CancelCallback.<init>'] = ('no_trigger_in_app', 'No code in the source root creates a CancelCallback. The class has only the implicit constructor. Its references are the parameter type (HttpSyncer.java:152-153) and a call on a parameter (HttpSyncer.java:231), which create no instance.', 'SRC com/ichi2/async/Connection.java:549-551; com/ichi2/libanki/sync/HttpSyncer.java:152-153, 230-232', 'SOURCE')

UNREACHABLE['Connection$CancelCallback.cancelAllConnections'] = ('no_trigger_in_app', 'No call site in the source root. The method is reached only through a CancelCallback object, and none is created in the source root.', 'SRC com/ichi2/async/Connection.java:558-566', 'SOURCE')

UNREACHABLE['Connection$CancelCallback.setConnectionManager'] = ('branch_never_taken', 'The only call is inside if (cancelCallback != null) (HttpSyncer.java:230-232). The only 5-argument req call in the source root is HttpSyncer.java:148, which passes the literal null, and the other req calls have at most four arguments. So cancelCallback is always null and the branch is never taken.', 'SRC com/ichi2/async/Connection.java:553-555; com/ichi2/libanki/sync/HttpSyncer.java:143-155, 230-232; com/ichi2/libanki/sync/RemoteMediaServer.java:94-100, 113-120, 143-148', 'SOURCE')

# --- UNREACHABLE: the zero-, two- and three-argument Connection$Payload constructors have no call site (Connection.java:514-536).
UNREACHABLE['Connection$Payload.<init>()'] = ('no_trigger_in_app', 'No call with zero arguments in the source root. The grep of Payload( finds the declaration (Connection.java:514) and only the one-argument constructions (MyAccount.java:140, DeckPicker.java:1285).', 'SRC com/ichi2/async/Connection.java:514-517; com/ichi2/anki/MyAccount.java:139-143; com/ichi2/anki/DeckPicker.java:1284-1286', 'SOURCE')

UNREACHABLE['Connection$Payload.<init>(int,Object[])'] = ('no_trigger_in_app', 'No call with two arguments in the source root. The grep of Payload( finds the declaration (Connection.java:526) and only the one-argument constructions (MyAccount.java:140, DeckPicker.java:1285). login and sync set taskType themselves (Connection.java:161, 167).', 'SRC com/ichi2/async/Connection.java:526-530, 160-169; com/ichi2/anki/MyAccount.java:139-143; com/ichi2/anki/DeckPicker.java:1284-1286', 'SOURCE')

UNREACHABLE['Connection$Payload.<init>(int,Object[],String)'] = ('no_trigger_in_app', 'No call with three arguments in the source root. The grep of Payload( finds the declaration (Connection.java:532) and only the one-argument constructions. The path argument is not stored in the body (lines 533-535).', 'SRC com/ichi2/async/Connection.java:532-536', 'SOURCE')
