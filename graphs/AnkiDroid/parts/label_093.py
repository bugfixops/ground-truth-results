# AnkiDroid batch 093 (LABEL helper): libanki Models.java, 30 methods, part 1 of 1.
# The row list is in graphs/AnkiDroid/parts/label_093.md.
# No e() edges: none of these methods sources a non-CALL edge.
# The six entries below are the methods with no call site in the source root.

UNREACHABLE['Models.byName'] = ('no_trigger_in_app',
  'Declared at Models.java 292-304. No call to Models.byName exists in the source root. The only byName call (CustomStudyDialog.java 423) is on col.getDecks(), so it is Decks.byName (Decks.java 459-460), a different method. No route from any entry.',
  'com/ichi2/libanki/Models.java:292-304; com/ichi2/libanki/Decks.java:459-460; com/ichi2/anki/dialogs/CustomStudyDialog.java:421-424', 'SOURCE')

UNREACHABLE['Models.copy'] = ('no_trigger_in_app',
  'Declared at Models.java 443-453. A grep for copy( with a receiver over the source root finds no call. No route from any entry.',
  'com/ichi2/libanki/Models.java:443-453', 'SOURCE')

UNREACHABLE['Models.getId'] = ('no_trigger_in_app',
  'Declared at Models.java 1372-1374 (returns mId). No call site in the source root: a grep for getId() on getModels() and on model, models or mModels receivers finds none. The getId() calls that exist belong to other classes. No route from any entry.',
  'com/ichi2/libanki/Models.java:1372-1374', 'SOURCE')

UNREACHABLE['Models.getName'] = ('no_trigger_in_app',
  'Declared at Models.java 1380-1382 (returns mName). No call on a Models receiver in the source root. The getName() calls in ModelBrowser (lines 277, 285, 669) are on DisplayPair objects (ModelBrowser.java 624-637). CardStats.java 115 is commented out. No route from any entry.',
  'com/ichi2/libanki/Models.java:1380-1382; com/ichi2/anki/ModelBrowser.java:274-290, 624-637, 658-670; com/ichi2/libanki/CardStats.java:112-120', 'SOURCE')

UNREACHABLE['Models.getTemplateNames'] = ('no_trigger_in_app',
  'Declared at Models.java 1349-1351. A grep over the source root for getTemplateNames( finds only its declaration. No route from any entry.',
  'com/ichi2/libanki/Models.java:1349-1351', 'SOURCE')

UNREACHABLE['Models.moveTemplate'] = ('no_trigger_in_app',
  'Declared at Models.java 842-846. A grep over the source root for moveTemplate( finds only its declaration. No route from any entry.',
  'com/ichi2/libanki/Models.java:842-846', 'SOURCE')
