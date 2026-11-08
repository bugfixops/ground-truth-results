# AnkiDroid batch 069 (LABEL helper). DeckTask part 1: 40 methods, all REACHABLE (no UNREACHABLE entries).
# The full row list is in graphs/AnkiDroid/parts/label_069.md.
#
# Route ownership:
# - The launch edges into the DeckTask bodies (for example StudyOptionsFragment, DeckPicker, CardBrowser) belong to the
#   launch-site batches. The CALL edges (cancelTask(int) -> cancelTask(), ProgressCallback -> doProgress, the getCard callers,
#   Finder -> getInstance) come from auto_calls.json and are not written here.
# - Written here: doInBackground -> DeckTask.onPostExecute (the AsyncTask result hop), and each task body that calls
#   publishProgress -> DeckTask.onProgressUpdate, plus doProgress -> DeckTask.onProgressUpdate. The line of each publishProgress
#   is in the EDGE row of label_069.md.
# - No gate is needed in this batch (MG632-MG641 are not used).

e('DeckTask.doInBackground', 'DeckTask.onPostExecute', 'ASYNC',
  'the worker result is delivered to DeckTask.onPostExecute on the UI thread (AsyncTask finish)',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:203-228, 360-365',
  note='DeckTask.onPostExecute forwards to mListener.onPostExecute (DeckTask.java:362). The AsyncTask finish dispatch is framework code and was not read in this batch. No gate of its own.')

e('DeckTask.doInBackgroundAddNote', 'DeckTask.onProgressUpdate', 'ASYNC',
  'publishProgress posts the added note to onProgressUpdate on the UI thread',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:378-381, 352-355',
  note='publishProgress is at DeckTask.java:380, inside the transaction. onProgressUpdate forwards to the listener (DeckTask.java:354). The UI-thread dispatch is AsyncTask (framework, not read in this batch).')

e('DeckTask.doInBackgroundUpdateNote', 'DeckTask.onProgressUpdate', 'ASYNC',
  'publishProgress posts the updated card to onProgressUpdate on the UI thread',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:418-423, 352-355',
  note='publishProgress is at DeckTask.java:420 and 422 (one per branch). onProgressUpdate forwards to the listener (DeckTask.java:354). The UI-thread dispatch is AsyncTask (framework, not read in this batch).')

e('DeckTask.doInBackgroundAnswerCard', 'DeckTask.onProgressUpdate', 'ASYNC',
  'publishProgress posts the answered card to onProgressUpdate on the UI thread',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:455-458, 352-355',
  note='publishProgress is at DeckTask.java:457. onProgressUpdate forwards to the listener (DeckTask.java:354). The UI-thread dispatch is AsyncTask (framework, not read in this batch).')

e('DeckTask.doInBackgroundDismissNote', 'DeckTask.onProgressUpdate', 'ASYNC',
  'publishProgress posts the dismissed card to onProgressUpdate on the UI thread',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:563-566, 352-355',
  note='publishProgress is at DeckTask.java:565. onProgressUpdate forwards to the listener (DeckTask.java:354). The UI-thread dispatch is AsyncTask (framework, not read in this batch).')

e('DeckTask.doInBackgroundUndo', 'DeckTask.onProgressUpdate', 'ASYNC',
  'publishProgress posts the undone card to onProgressUpdate on the UI thread',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:599-602, 352-355',
  note='publishProgress is at DeckTask.java:601. onProgressUpdate forwards to the listener (DeckTask.java:354). The UI-thread dispatch is AsyncTask (framework, not read in this batch).')

e('DeckTask.doInBackgroundSearchCards', 'DeckTask.onProgressUpdate', 'ASYNC',
  'publishProgress posts the search results to onProgressUpdate on the UI thread',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:629-634, 352-355',
  note='publishProgress is at DeckTask.java:633, in the else branch of the isCancelled check (line 629). onProgressUpdate forwards to the listener (DeckTask.java:354).')

e('DeckTask.doInBackgroundRenderBrowserQA', 'DeckTask.onProgressUpdate', 'ASYNC',
  'publishProgress posts the render progress to onProgressUpdate on the UI thread',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:657-660, 352-355',
  note='publishProgress is at DeckTask.java:659. onProgressUpdate forwards to the listener (DeckTask.java:354). The UI-thread dispatch is AsyncTask (framework, not read in this batch).')

e('DeckTask.doInBackgroundImportReplace', 'DeckTask.onProgressUpdate', 'ASYNC',
  'publishProgress posts the import progress messages to onProgressUpdate on the UI thread',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:805-810, 855-860, 352-355',
  note='publishProgress is at DeckTask.java:809 (before the collection import) and 859 (in the media loop). onProgressUpdate forwards to the listener (DeckTask.java:354).')

e('DeckTask.doProgress', 'DeckTask.onProgressUpdate', 'ASYNC',
  'doProgress publishes the importer progress, which reaches onProgressUpdate on the UI thread',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:1348-1350, 352-355',
  note='doProgress calls publishProgress (DeckTask.java:1349), the AsyncTask method. The importer path is ProgressCallback.publishProgress (DeckTask.java:1340-1344), created in doInBackgroundImportAdd (DeckTask.java:750).')
