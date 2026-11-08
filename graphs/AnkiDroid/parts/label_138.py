# AnkiDroid batch 138 (LABEL helper). 40 methods in 5 classes: AbstractFlashcardViewer$11 (1), Lines (7),
# ModelFieldEditor (11, including closeActivity()), MultimediaEditFieldActivity (10), XAxis (11).
# All 40 are labelled REACHABLE from printed source. No UNREACHABLE entries are written here, because no method
# has a printed path that is provably dead. The row list (label, kind, reason, printed file:lines) is in
# graphs/AnkiDroid/parts/label_138.md.
#
# Edges written here (page ENTERS edges; the source is a method of this batch, same pattern as DeckPicker.onCreate
# -> S_DECKPICKER at graph_def.py:835):
#  1. MultimediaEditFieldActivity.onCreate -> S_MULTIMEDIA_EDIT_FIELD. Required by batch 136 (parts/label_136.py:7).
#  2. ModelFieldEditor.onCreate -> S_MODELFIELDEDITOR. The batch 033 header (graph_def.py:4591-4596) says these
#     ENTERS edges are written there, but no S_MODELFIELDEDITOR ENTERS edge exists in graph_def.py or parts/
#     (grep checked). Without it the 11 ModelFieldEditor rows cannot resolve. Batch 033 should not write it again.
#
# Not written here:
#  - S_STATISTICS has no inbound ENTERS edge. The Statistics page belongs to batch 144. The Lines and XAxis rows
#    depend on it (ChartView.onDraw FRAMEWORK edge at graph_def.py:7657).
#  - AbstractFlashcardViewer.answerCard -> AbstractFlashcardViewer$11.run (ASYNC, Handler.postDelayed at
#    AbstractFlashcardViewer.java:1316). The launch site belongs to the batch that holds answerCard, so this row
#    stays UNRESOLVED until that edge exists.
#  - ModelFieldEditor$1.onItemClick and ModelFieldEditor$9.onSelection edges are already in graph_def.py
#    (4635 and 4449), owned by batch 034.
# Automatic CALL edges come from auto_calls.json and are not written here.

e('MultimediaEditFieldActivity.onCreate', 'S_MULTIMEDIA_EDIT_FIELD', 'ENTERS',
  'the multimedia field editor screen is created and shown (not a restore after shut-off)',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:74-106',
  note='onCreate returns early at lines 77-82 (finishCancel) when the saved state has the shut-off flag written by onSaveInstanceState (lines 352-355). Otherwise the layout is set at line 85, the field, note and index are read at lines 92-96, the editing UI is built at line 98, and the spare menu is created only at API <= GINGERBREAD_MR1 (lines 101-105, closed by API level). Entry is the INTENT NoteEditor.startMultimediaFieldEditor -> MultimediaEditFieldActivity.<init> (graph_def.py:2140), whose gates belong to the NoteEditor batch, so no gate is set here. The LIFECYCLE <init> -> onCreate edge comes from lc_chain (graph_def.py:284-285).')

e('ModelFieldEditor.onCreate', 'S_MODELFIELDEDITOR', 'ENTERS',
  'the field editor screen is created; its field list is shown once the collection is loaded (onCollectionLoaded)',
  env=None, needs_state=STATE_COLLECTION,
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:72-89; SRC com/ichi2/anki/AnkiActivity.java:255-262, 283-290',
  note='onCreate sets the content view and calls startLoadingCollection (ModelFieldEditor.java:72-89; AnkiActivity.java:255-262). The loader result reaches onCollectionLoaded through onLoadFinished (AnkiActivity.java:283-290), which is the ASYNC edge at graph_def.py:4599. STATE_COLLECTION follows the note at graph_def.py:4633 (the list is filled after the collection loads). Entry is the INTENT ModelBrowser$4.onItemClick -> ModelFieldEditor.<init> (graph_def.py:4259). No env is set here: the storage gate belongs to the route that opens the app. Batch 033 header (graph_def.py:4591-4596) planned this edge and did not write it.')
