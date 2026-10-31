# AnkiDroid batch 087 (LABEL helper): Decks part 1 (40 methods, com/ichi2/libanki/Decks.java).
# The row list is in graphs/AnkiDroid/parts/label_087.md. 29 methods are REACHABLE (automatic CALL routes, see the .md).
# No e() edges: the Decks methods in this batch own no outgoing edges that are not automatic CALL edges, and the edges
# into them come from methods owned by other batches. No MISSING GATE notes.
# The 11 UNREACHABLE entries below are the methods with no route in the standard configuration.

UNREACHABLE['Decks._basename'] = ('no_trigger_in_app',
  'Private helper. Its only callers are renameForDragAndDrop (Decks.java 538 and 544) and _isParent (Decks.java 565). Both are unreachable, and no other call exists in the source root.',
  'com/ichi2/libanki/Decks.java:593-596; com/ichi2/libanki/Decks.java:538, 544, 565', 'SOURCE')

UNREACHABLE['Decks._canDragAndDrop'] = ('no_trigger_in_app',
  'Private. Its only caller is renameForDragAndDrop (Decks.java 540). renameForDragAndDrop has no caller in the source root (grep finds only its declaration at 530), so this method cannot run.',
  'com/ichi2/libanki/Decks.java:552-560; com/ichi2/libanki/Decks.java:540', 'SOURCE')

UNREACHABLE['Decks._isAncestor'] = ('no_trigger_in_app',
  'Private. Its only caller is _canDragAndDrop (Decks.java 555), which is unreachable because renameForDragAndDrop has no caller.',
  'com/ichi2/libanki/Decks.java:578-587; com/ichi2/libanki/Decks.java:555', 'SOURCE')

UNREACHABLE['Decks._isParent'] = ('no_trigger_in_app',
  'Private. Its only caller is _canDragAndDrop (Decks.java 554), which is unreachable because renameForDragAndDrop has no caller.',
  'com/ichi2/libanki/Decks.java:563-575; com/ichi2/libanki/Decks.java:554', 'SOURCE')

UNREACHABLE['Decks.cids(long)'] = ('no_trigger_in_app',
  'No caller in the source root. A grep for the call pattern finds only the two-argument form cids(mDid, true) at AnkiPackageExporter.java 97. The method itself only calls cids(did, false) at Decks.java 827, and nothing calls cids(long).',
  'com/ichi2/libanki/Decks.java:826-828; com/ichi2/libanki/AnkiPackageExporter.java:93-98', 'SOURCE')

UNREACHABLE['Decks.collapseBrowser'] = ('no_trigger_in_app',
  'No caller in the source root. A grep for collapseBrowser over the whole source root finds only its declaration at Decks.java 420.',
  'com/ichi2/libanki/Decks.java:420-429', 'SOURCE')

UNREACHABLE['Decks.confId(String)'] = ('no_trigger_in_app',
  'No caller in the source root. A grep for .confId( finds only the two-argument call at DeckOptions.java 239.',
  'com/ichi2/libanki/Decks.java:674-676; com/ichi2/anki/DeckOptions.java:239', 'SOURCE')

UNREACHABLE['Decks.count'] = ('no_trigger_in_app',
  'No caller in the source root. A grep for the call on getDecks(), mDecks and decks variables finds no call. The method is declared at Decks.java 435-437 and returns mDecks.size().',
  'com/ichi2/libanki/Decks.java:435-437', 'SOURCE')

UNREACHABLE['Decks.nameOrNone'] = ('no_trigger_in_app',
  'No caller in the source root. A grep for nameOrNone over the whole source root finds only its declaration at Decks.java 796.',
  'com/ichi2/libanki/Decks.java:796-806', 'SOURCE')

UNREACHABLE['Decks.rem(long)'] = ('no_trigger_in_app',
  'No caller. The one-argument form is never called: every call site found by grep passes two or three arguments (DeckTask.java 723, Syncer.java 644, Sched.java 390 and 406).',
  'com/ichi2/libanki/Decks.java:270-272; com/ichi2/async/DeckTask.java:723; com/ichi2/libanki/sync/Syncer.java:644; com/ichi2/libanki/Sched.java:390, 406', 'SOURCE')

UNREACHABLE['Decks.renameForDragAndDrop'] = ('no_trigger_in_app',
  'No caller in the source root. A grep for renameForDragAndDrop over the whole source root finds only its declaration at Decks.java 530. Its helpers (_canDragAndDrop, _isParent, _isAncestor, _basename) are reached only through it.',
  'com/ichi2/libanki/Decks.java:530-549; com/ichi2/libanki/Decks.java:552-575', 'SOURCE')


# ---- addendum (2026-10-28): edge for the Decks$1.compare row in batch 088; written here with allSorted
e('Decks.allSorted', 'Decks$1.compare', 'CALL',
  'Collections.sort in allSorted calls the anonymous comparator for each pair of decks it compares',
  env=None,
  note='MISSING GATE MG812: the comparator runs only when the collection has two or more decks (the Default deck always exists, so one more deck is needed). The sort is java.util and not in fw_src (source not read), so the call is INFERRED from the JDK contract.',
  evidence='SRC com/ichi2/libanki/Decks.java:388-398; INFERRED (JDK Collections.sort, source not read)')
