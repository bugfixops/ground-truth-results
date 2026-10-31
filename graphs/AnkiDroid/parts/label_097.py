# AnkiDroid batch 097 (LABEL helper): Sched part 3, 40 methods of com/ichi2/libanki/Sched.java.
# The row list is in graphs/AnkiDroid/parts/label_097.md.
# No e() edges: every outgoing call from a Sched method in this batch is an automatic CALL edge, and the
# entries into these methods come from callers owned by other batches (DeckTask, Reviewer, CardContentProvider,
# DeckPicker, AbstractFlashcardViewer, NoteEditor, StudyOptionsFragment, AnkiPackageExporter, Anki2Importer,
# CustomStudyDialog, DeckPickerContextMenu, WidgetStatus).

UNREACHABLE['Sched.dueForecast()'] = ('no_trigger_in_app',
  'The method calls dueForecast(7). No caller exists in the source root: grep for dueForecast finds only the declarations in Sched.java 212-217.',
  'com/ichi2/libanki/Sched.java:212-217', 'SOURCE')

UNREACHABLE['Sched.dueForecast(int)'] = ('no_trigger_in_app',
  'The body is a TODO stub that returns 0. Its only caller is dueForecast() (Sched.java 213), which has no caller.',
  'com/ichi2/libanki/Sched.java:212-220', 'SOURCE')

UNREACHABLE['Sched.getName'] = ('no_trigger_in_app',
  'The method returns mName. No caller exists in the source root: grep for getName on a Sched receiver (getSched().getName, mSched.getName, sched.getName) finds only the declaration.',
  'com/ichi2/libanki/Sched.java:2334-2336', 'SOURCE')

UNREACHABLE['Sched.leechActionSuspend'] = ('no_trigger_in_app',
  'No caller exists in the source root: grep for leechActionSuspend finds only the declaration.',
  'com/ichi2/libanki/Sched.java:2476-2484', 'SOURCE')

UNREACHABLE['Sched.maybeRandomizeDeck()'] = ('no_trigger_in_app',
  'The no-argument overload only calls maybeRandomizeDeck(null) (Sched.java 2293). The only other caller in the source root uses the Long overload (Anki2Importer 695). No caller of the no-argument overload exists.',
  'com/ichi2/libanki/Sched.java:2292-2294; com/ichi2/libanki/importer/Anki2Importer.java:692-696', 'SOURCE')

UNREACHABLE['Sched.rebuildDyn()'] = ('no_trigger_in_app',
  'The no-argument overload only calls rebuildDyn(0) (Sched.java 1527). Every caller in the source root passes a deck id: DeckTask (731) passes col.getDecks().selected(). No caller of the no-argument overload exists.',
  'com/ichi2/libanki/Sched.java:1526-1528; com/ichi2/async/DeckTask.java:728-733', 'SOURCE')

UNREACHABLE['Sched.removeLrn()'] = ('no_trigger_in_app',
  'The method only calls removeLrn(null) (Sched.java 1154). No caller exists in the source root: grep for removeLrn finds only the two declarations and that call.',
  'com/ichi2/libanki/Sched.java:1153-1155', 'SOURCE')