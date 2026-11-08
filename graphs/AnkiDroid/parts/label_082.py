# AnkiDroid batch 082 (LABEL helper): libanki Card methods, part 2 of 2 (27 methods).
# The row list is in graphs/AnkiDroid/parts/label_082.md.
# No e() edges: the setters and the other Card methods own no outgoing edges except automatic CALL edges,
# and the edges into them come from callers owned by other batches (Sched, DeckTask, AbstractFlashcardViewer,
# CardContentProvider, NoteEditor, Collection, CardBrowser).

UNREACHABLE['Card.setCol'] = ('no_trigger_in_app',
  'Only the declaration exists in the source root. The method is marked "Needed for tests", so its only caller would be test code, which is not in the app. A grep for setCol over the source root finds no other call.',
  'com/ichi2/libanki/Card.java:610-613', 'SOURCE')

UNREACHABLE['Card.shouldShowTimer'] = ('no_trigger_in_app',
  'Declared at Card.java 365-372. No call site exists in the source root (grep for the call finds none). The viewer asks showTimer instead (AbstractFlashcardViewer.java 1885).',
  'com/ichi2/libanki/Card.java:365-372; com/ichi2/anki/AbstractFlashcardViewer.java:1883-1886', 'SOURCE')

UNREACHABLE['Card.toString'] = ('no_trigger_in_app',
  'Overrides Object.toString. No explicit call and no implicit string conversion of a libanki Card was found in the source root. The one Card concatenation (AdvancedStatistics.java 1499) uses the inner class Card of AdvancedStatistics, which has its own toString. Confidence is moderate.',
  'com/ichi2/libanki/Card.java:634-648; com/ichi2/libanki/hooks/AdvancedStatistics.java:1497-1500', 'SOURCE')
