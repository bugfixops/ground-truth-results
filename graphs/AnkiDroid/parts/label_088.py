# AnkiDroid batch 088 (LABEL helper): Decks part 2, 10 methods. The row list is in graphs/AnkiDroid/parts/label_088.md.
# No e() calls. The calls into these methods are automatic CALL edges (written by the builder) or belong to the
# batches that hold their callers (DeckOptions, DeckTask, DeckPicker, Sched, AnkiPackageExporter, Anki2Importer, Syncer).
# The FRAMEWORK edge from Decks.allSorted to Decks$1.compare belongs to the batch that holds allSorted.

UNREACHABLE['Decks.setDeck'] = ('no_trigger_in_app',
  'Declared at Decks.java 809-812 and not called anywhere in src/main. A grep for setDeck over the whole src/main tree finds only this declaration. The card move it would do (update cards set did, using Utils.ids2str) is not reached from any UI, DeckTask, provider, importer or sync path. Confidence is high because the search covers the full src/main tree.',
  'com/ichi2/libanki/Decks.java:809-812', 'SOURCE')
