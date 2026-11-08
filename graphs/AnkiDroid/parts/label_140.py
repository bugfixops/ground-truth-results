# AnkiDroid batch 140 (LABEL helper). AbstractFlashcardViewer$18 (1 method), MetaDB (9), NoteEditor (7),
# PieChart (7), PlotSheet (9), YGrid (7). 40 methods in total.
# Source row: graphs/AnkiDroid/scratch/batches_ai.tsv, part 140. The full row list (label, kind, reason, printed file:lines)
# is in graphs/AnkiDroid/parts/label_140.md. All 40 methods are labelled REACHABLE. No UNREACHABLE entries are written here.
#
# Route gaps in out/ that the edges below close:
# - AnkiActivity.onLoadFinished has no inbound edge (base and @NoteEditor variant), so NoteEditor.onCollectionLoaded
#   has no loader route. Written here: ASYNC NoteEditor.onCreate -> NoteEditor.onCollectionLoaded (same pattern as
#   parts/label_137.py for Reviewer.onCollectionLoaded).
# - S_DLG_RESCHEDULE_CARD has no inbound ENTERS edge, so NoteEditorRescheduleCard$1.onInput (parts/label_044.py:57)
#   and NoteEditor.onRescheduleCard stay UNRESOLVED. Written here: ENTERS NoteEditor.onOptionsItemSelected -> S_DLG_RESCHEDULE_CARD.
# - AbstractFlashcardViewer$18.run has only a REGISTER edge in out/ (REGISTER does not count). The route is the postDelayed
#   call in displayCardAnswer (AbstractFlashcardViewer.java:2031-2033). Written here: FRAMEWORK
#   AbstractFlashcardViewer.displayCardAnswer -> AbstractFlashcardViewer$18.run (the batch_019 lead named in parts/label_021.py:83).
#
# Not written here (outside this batch, both ends or the gap is in another part):
# - WidgetStatus.update -> UpdateDeckStatusAsyncTask.execute -> doInBackground -> onPostExecute (ASYNC). Owned by part 080.
#   Until those edges exist, MetaDB.storeSmallWidgetStatus, closeDB, resetWidget, getWidgetSmallStatus and getNotificationStatus
#   are UNRESOLVED in out/ even though their rows are labelled REACHABLE (see parts/label_140.md).
#
# Already in graph_def.py and not repeated here: NoteEditor.onCollectionLoaded -> onDestroy (FRAMEWORK, graph_def.py:2186),
# NoteEditor.onCollectionLoaded -> JSONNameComparator.compare (CALL, graph_def.py:2230), S_STATISTICS -> ChartView.onDraw,
# S_REVIEWER -> ReadText$1.onSelection (GUI, graph_def.py:6693), AbstractFlashcardViewer$18.run -> AbstractFlashcardViewer$5.onClick
# (FRAMEWORK, graph_def.py:3252), the Reviewer.onCollectionLoaded chain written by parts/label_137.py.
# Automatic CALL edges come from auto_calls.json (bytecode) and are not written here.

e('NoteEditor.onCreate', 'NoteEditor.onCollectionLoaded', 'ASYNC',
  'the collection loader finishes and delivers the collection to the note editor (loader route from onCreate)',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:287-309, 331; SRC com/ichi2/anki/AnkiActivity.java:255-262, 283-290',
  note='onCreate calls startLoadingCollection (NoteEditor.java:309), which restarts the collection loader (AnkiActivity.java:261). The loader result reaches onCollectionLoaded through AnkiActivity.onLoadFinished (283-286) by virtual dispatch. The loader is an androidx library step: INFERRED, source not read. AnkiActivity.onLoadFinished@NoteEditor (receiver variant) has no inbound edge in out/, so the edge is written from the base onCreate, following the Reviewer precedent in parts/label_137.py.')

e('NoteEditor.onOptionsItemSelected', 'S_DLG_RESCHEDULE_CARD', 'ENTERS',
  'the reschedule menu item is tapped and the reschedule dialog opens',
  env=None,
  needs_state=STATE_NOTE,
  evidence='SRC com/ichi2/anki/NoteEditor.java:871-873; SRC com/ichi2/anki/NoteEditor.java:801-808; SRC com/ichi2/anki/AnkiActivity.java:337-340',
  note='showDialogFragment(NoteEditorRescheduleCard.newInstance()) opens the dialog (NoteEditor.java:873). The menu item is visible only when the editor is not adding a note (NoteEditor.java:803-808), so a note exists (STATE_NOTE). Precedent: DeckPicker.onOptionsItemSelected -> S_DLG_IMPORT ENTERS in parts/label_002.py:75-76. Without this edge the page has no inbound edge, and NoteEditorRescheduleCard$1.onInput (parts/label_044.py:57) and NoteEditor.onRescheduleCard stay UNRESOLVED.')

e('AbstractFlashcardViewer.displayCardAnswer', 'AbstractFlashcardViewer$18.run', 'FRAMEWORK',
  'the answer is shown and the auto-advance timer posts the show-question runnable (Handler.postDelayed)',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1863-1871, 1991, 2031-2033',
  note='displayCardAnswer posts mShowQuestionTask with mTimeoutHandler.postDelayed only when mPrefUseTimer and mWaitQuestionSecond > 0 (lines 2031-2033). The Handler delivers the runnable later, so the edge kind is FRAMEWORK. The gate is a user preference (auto-advance timer), not a build setting. The REGISTER edge from $18.<init> (parts/label_021.py:128) is not followed for reachability. No edge with this pair exists in graph_def.py or parts/*.py at the time of writing.')
