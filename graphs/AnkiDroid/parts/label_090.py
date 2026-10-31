# AnkiDroid batch 090 (LABEL helper): Finder, part 1 of 2 (40 methods, com/ichi2/libanki/Finder.java).
# The row list is in graphs/AnkiDroid/parts/label_090.md.
# No e() edges: every call inside Finder is an automatic CALL edge (written by the builder), and the entries into
# Finder come from Collection, CardContentProvider, Sched, DeckTask, CardBrowser and CardTemplateEditor, which other batches own.
# The 28 REACHABLE methods need no entry here. The 12 UNREACHABLE methods follow.

UNREACHABLE['Finder.fieldNames(Collection)'] = ('no_trigger_in_app',
  'No caller. The only fieldNames calls in the source root are Models.fieldNames on a model object (CardTemplateEditor.java 531, declared at Models.java 490), not this Finder method. The Collection wrappers that create a Finder (Collection.java 1060, 1066, 1071, 1077) never call fieldNames.',
  'com/ichi2/libanki/Finder.java:902-904; com/ichi2/anki/CardTemplateEditor.java:531; com/ichi2/libanki/Collection.java:1059-1077', 'SOURCE')

UNREACHABLE['Finder.fieldNames(Collection,boolean)'] = ('no_trigger_in_app',
  'Its only caller is fieldNames(Collection) at Finder.java 903, which has no caller (see the row above).',
  'com/ichi2/libanki/Finder.java:903-904, 906-927', 'SOURCE')

UNREACHABLE['Finder.findCards(String)'] = ('no_trigger_in_app',
  'No caller. Collection.findCards(String) (Collection.java 1059-1061) calls the two-argument Finder overload with null at 1060, not this one, and no code calls that wrapper. A grep for one-argument findCards calls over the source root finds none. Finder.findCards(String) calls only findCards(String,boolean) at Finder.java 71.',
  'com/ichi2/libanki/Finder.java:70-72; com/ichi2/libanki/Collection.java:1059-1061', 'SOURCE')

UNREACHABLE['Finder.findCards(String,boolean)'] = ('no_trigger_in_app',
  'Its only caller is findCards(String) at Finder.java 71, which has no caller (see the row above). Collection passes null at 1060 and a String order at 1066, so the boolean overload is never selected.',
  'com/ichi2/libanki/Finder.java:71, 80-82; com/ichi2/libanki/Collection.java:1060, 1066', 'SOURCE')

UNREACHABLE['Finder.findCardsForCardBrowser(String,String,Map)'] = ('no_trigger_in_app',
  'The only calls over the source root are Collection.findCardsForCardBrowser (Collection.java 1070-1072), which takes a boolean and passes it at 1071, and DeckTask.doInBackgroundSearchCards (DeckTask.java 619-622), which passes a Boolean that Java unboxes to boolean. The String overload is therefore never selected (Finder.java 1018-1020).',
  'com/ichi2/libanki/Finder.java:1013-1020; com/ichi2/libanki/Collection.java:1070-1072; com/ichi2/async/DeckTask.java:619-622', 'SOURCE')

UNREACHABLE['Finder.findDupes(Collection,String)'] = ('no_trigger_in_app',
  'No caller. Collection.findDupes(String) (Collection.java 1101-1103) calls the three-argument overload at 1102, not this one, and no other call site was found over the source root.',
  'com/ichi2/libanki/Finder.java:955-957; com/ichi2/libanki/Collection.java:1101-1103', 'SOURCE')

UNREACHABLE['Finder.findDupes(Collection,String,String)'] = ('no_trigger_in_app',
  'Its callers are findDupes(Collection,String) at Finder.java 956, which is itself uncalled, and the Collection wrappers at Collection.java 1102 (findDupes(String)) and 1107 (findDupes(String,String)). Those wrappers have no caller (1101-1108), so this method is never called.',
  'com/ichi2/libanki/Finder.java:955-957, 963-1005; com/ichi2/libanki/Collection.java:1101-1108', 'SOURCE')

UNREACHABLE['Finder.findReplace(Collection,List,String,String)'] = ('no_trigger_in_app',
  'Its only caller is Collection.findReplace(List,String,String) at Collection.java 1082, which has no caller (1081-1083). The Finder.java calls at 809, 814 and 819 go to the seven-argument overload, not to this one.',
  'com/ichi2/libanki/Finder.java:808-810; com/ichi2/libanki/Collection.java:1081-1083', 'SOURCE')

UNREACHABLE['Finder.findReplace(Collection,List,String,String,String)'] = ('no_trigger_in_app',
  'Its only caller is Collection.findReplace(List,String,String,String) at Collection.java 1092 inside the wrapper at 1091-1093, which no code calls.',
  'com/ichi2/libanki/Finder.java:818-820; com/ichi2/libanki/Collection.java:1091-1093', 'SOURCE')

UNREACHABLE['Finder.findReplace(Collection,List,String,String,boolean)'] = ('no_trigger_in_app',
  'Its only caller is Collection.findReplace(List,String,String,boolean) at Collection.java 1087 inside the wrapper at 1086-1088, which no code calls.',
  'com/ichi2/libanki/Finder.java:813-815; com/ichi2/libanki/Collection.java:1086-1088', 'SOURCE')

UNREACHABLE['Finder.findReplace(Collection,List,String,String,boolean,String,boolean)'] = ('no_trigger_in_app',
  'Its callers are the three shorter Finder.findReplace overloads (Finder.java 809, 814, 819), which are themselves uncalled, and Collection.findReplace(List,String,String,boolean,String,boolean) at Collection.java 1097 inside the wrapper at 1096-1098. That wrapper has no caller, so this method is never called.',
  'com/ichi2/libanki/Finder.java:808-820, 823-899; com/ichi2/libanki/Collection.java:1096-1098', 'SOURCE')

UNREACHABLE['Finder.ordForMid'] = ('no_trigger_in_app',
  'Its only caller is findDupes (three-argument) at Finder.java 981, which is reached only through the uncalled Collection.findDupes wrappers (Collection.java 1101-1108).',
  'com/ichi2/libanki/Finder.java:935-952, 963-1005, 981; com/ichi2/libanki/Collection.java:1101-1108', 'SOURCE')
