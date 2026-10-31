# AnkiDroid batch 142 (LABEL helper). AbstractFlashcardViewer$MyGestureDetector (5 methods), BasicImageFieldController (5),
# BeolingusParser (3), CollectionLoader (5), LoadPronounciationActivity$BackgroundPost (5), PickStringDialogFragment (5),
# StepsPreference (6), Whiteboard$UndoStack (6). 40 methods in total.
# Source row: graphs/AnkiDroid/scratch/batches_ai.tsv, part 142. The full row list (label, kind, reason, printed file:lines)
# is in graphs/AnkiDroid/parts/label_142.md. All 40 methods are labelled REACHABLE. No UNREACHABLE entries are written here.
#
# Route gap in out/: all five CollectionLoader methods are UNRESOLVED in out/methods.csv. The only loader entry is
# AnkiActivity.startLoadingCollection -> AnkiActivity.onCreateLoader (graph_def.py:10948, parts/label_127.py:22), and no
# edge reaches CollectionLoader.onStartLoading, onStopLoading or onReset. The chain onStartLoading -> loadInBackground ->
# deliverResult already exists (graph_def.py:7943, 7948) and is not repeated here.
# Written here (all three are support-library steps, INFERRED, source not read):
# - AnkiActivity.onCreateLoader -> CollectionLoader.onStartLoading (starts the loader; reaches the chain above).
# - AnkiActivity.onStop -> CollectionLoader.onStopLoading (a second route for onStopLoading, not via onReset).
# - NoteEditor.onDestroy -> CollectionLoader.onReset (the loader reset on destroy; the source is the NoteEditor override,
#   because AnkiActivity has no onDestroy override and no AnkiActivity.onDestroy node exists in method_list.json).
# The other 35 methods have existing routes (see parts/label_142.md for each row).

e('AnkiActivity.onCreateLoader', 'CollectionLoader.onStartLoading', 'FRAMEWORK',
  'the support-library LoaderManager starts the collection loader that onCreateLoader returned',
  env=None,
  evidence='SRC com/ichi2/anki/AnkiActivity.java:261, 276-278; SRC com/ichi2/async/CollectionLoader.java:47-55',
  note='startLoadingCollection calls restartLoader(0, null, this) (AnkiActivity.java:261). The LoaderManager asks this activity for the loader (onCreateLoader, 276-278), which returns new CollectionLoader(this). The support library then calls the protected onStartLoading (CollectionLoader.java:47-55), which calls forceLoad (line 54) unless the collection is locked (lines 49-52). The LoaderManager is a support-library step, not in fw_src: INFERRED, source not read. Edge not in graph_def.py or parts/*.py at the time of writing.')

e('AnkiActivity.onStop', 'CollectionLoader.onStopLoading', 'FRAMEWORK',
  'the activity stops and the loader manager stops the collection loader',
  env=None,
  evidence='SRC com/ichi2/anki/AnkiActivity.java:71-74; FW-SRC android/app/Activity.java:1858 (Activity.onStop, which does not reach loaders); SRC com/ichi2/async/CollectionLoader.java:58-62',
  note='AnkiActivity.onStop calls super.onStop() (AnkiActivity.java:72). The support-library FragmentActivity stops its LoaderManager, which calls Loader.stopLoading and then the protected onStopLoading (CollectionLoader.java:58-62). The framework Activity.onStop does not touch loaders, so the second hop is INFERRED: support-library source not read. This route does not depend on onReset. Edge not in graph_def.py or parts/*.py at the time of writing.')

e('NoteEditor.onDestroy', 'CollectionLoader.onReset', 'FRAMEWORK',
  'the note editor is destroyed and the loader manager resets its collection loader',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:792-793, 309; SRC com/ichi2/async/CollectionLoader.java:65-69',
  note='NoteEditor.onDestroy calls super.onDestroy() (NoteEditor.java:793). The support-library FragmentActivity.onDestroy destroys its LoaderManager, and the loader info calls Loader.reset, which calls onReset (CollectionLoader.java:65-69). NoteEditor.onCreate starts this loader (startLoadingCollection, NoteEditor.java:309). AnkiActivity has no onDestroy override and no AnkiActivity.onDestroy node exists in method_list.json, so the NoteEditor override is the source of the route. Support-library source not read: INFERRED. The out/ source_ref for NoteEditor.onDestroy (NoteEditor.java:960-969) is closeNoteEditor, not this method; the declaration is at line 792. Edge not in graph_def.py or parts/*.py at the time of writing.')
