# AnkiDroid batch 092 (LABEL helper): libanki Media methods, 37 methods (com/ichi2/libanki/Media.java).
# The row list is in graphs/AnkiDroid/parts/label_092.md.
# No e() edges: every edge into these methods comes from a caller owned by another part
# (sync, DeckTask, AbstractFlashcardViewer, CardContentProvider, AnkiPackageExporter, Anki2Importer, NoteService, MyAccount).

UNREACHABLE['Media.strip'] = ('no_trigger_in_app',
  'Public method that applies the media regexps to a string. No call in the app source root. Its only callers are the androidTest unit tests (MediaTest lines 108-110 of the androidTest file). A search for a call on a Media receiver finds only those tests. The String.strip() calls in the app are a different method.',
  'AnkiDroid/src/androidTest/java/com.ichi2.anki.tests/libanki/MediaTest.java:108-110; com/ichi2/libanki/Media.java:358-363', 'SOURCE')
