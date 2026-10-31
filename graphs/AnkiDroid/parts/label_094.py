# AnkiDroid batch 094 (LABEL helper): libanki Note methods (35 methods, com/ichi2/libanki/Note.java).
# The row list is in graphs/AnkiDroid/parts/label_094.md.
# No e() edges: every caller of these methods is an automatic CALL edge or belongs to another batch.
# Four methods have no caller in the app (contains, getCol, keys, setItem). Their entries are below.

UNREACHABLE['Note.contains'] = ('no_trigger_in_app',
  'No caller. A grep of the source root for contains( on Note receivers finds none, and the bytecode call list (auto_calls.json) has no edge into Note.contains. The body returns mFMap.containsKey(key) (Note.java 222), a plain key test.',
  'com/ichi2/libanki/Note.java:221-223', 'SOURCE')

UNREACHABLE['Note.getCol'] = ('no_trigger_in_app',
  'No caller. A grep of the source root for getCol() calls on Note receivers finds none, and the bytecode call list (auto_calls.json) has no edge into Note.getCol.',
  'com/ichi2/libanki/Note.java:338-340', 'SOURCE')

UNREACHABLE['Note.keys'] = ('no_trigger_in_app',
  'No caller. The keys() calls in the source root are on JSON objects and return iterators (CardBrowser.java 646, Tags.java 73), not on Note receivers. The bytecode call list (auto_calls.json) has no edge into Note.keys. The body casts Object[] to String[] (Note.java 185), which would fail at run time if it were ever called.',
  'com/ichi2/libanki/Note.java:184-186; com/ichi2/anki/CardBrowser.java:646; com/ichi2/libanki/Tags.java:73', 'SOURCE')

UNREACHABLE['Note.setItem'] = ('no_trigger_in_app',
  'No caller. A grep of the source root for setItem( finds no call, and the bytecode call list (auto_calls.json) has no edge into Note.setItem. Its reader getItem is reachable, but nothing writes a field by key.',
  'com/ichi2/libanki/Note.java:217-219', 'SOURCE')
