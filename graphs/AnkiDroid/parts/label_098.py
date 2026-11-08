# AnkiDroid batch 098 (LABEL helper): libanki Sched, part 4 (16 methods).
# The row list is in graphs/AnkiDroid/parts/label_098.md.
# No e() edges: the methods in this batch have no outgoing edges except automatic CALL edges and
# JDK dispatch (Collections.sort), and the edges into them come from callers owned by other batches
# (DeckTask, StudyOptionsFragment, CustomStudyDialog, DeckPickerContextMenu, NoteEditor, Syncer,
# WidgetStatus, CardContentProvider, DeckPicker).

UNREACHABLE['Sched.setToday'] = ('no_trigger_in_app',
  'Plain setter of mToday. A text search of the whole app source root for setToday finds only this declaration, so no app code calls it.',
  'com/ichi2/libanki/Sched.java:2344-2346', 'SOURCE')

UNREACHABLE['Sched$DeckDueTreeNode.toString'] = ('no_trigger_in_app',
  'Overrides Object.toString (String.format over the names, did, depth, counts and children). No explicit call exists in the app source root. The app code that reads DeckDueTreeNode objects reads their fields, not the node as a string (WidgetStatus.java:126-128 reads newCount, lrnCount and revCount; CardContentProvider.java:367 iterates the list). Confidence is moderate: the check covered Timber, format and concatenation lines that mention node, deck or children, not every expression.',
  'com/ichi2/libanki/Sched.java:2554-2557; com/ichi2/widget/WidgetStatus.java:116-128; com/ichi2/anki/provider/CardContentProvider.java:364-367', 'SOURCE')
