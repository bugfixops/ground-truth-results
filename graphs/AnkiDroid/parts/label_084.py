# AnkiDroid batch 084 (LABEL helper): libanki Collection methods, part 1 of 2 (40 methods).
# The row list is in graphs/AnkiDroid/parts/label_084.md.
# No e() edges: none of the 40 methods owns a source-side gate; they are callees of other owners' methods.
# The 13 UNREACHABLE entries are below; each reason is repeated inline.

UNREACHABLE['Collection.<init>(Context,DB,String)'] = ('no_trigger_in_app',
  'The body only calls this(context, db, path, false). The source root has no call with three arguments: the one constructor call is Storage.java line 63, which passes five arguments. No other constructor calls this one.',
  'com/ichi2/libanki/Collection.java:129-131; com/ichi2/libanki/Storage.java:63', 'SOURCE')

UNREACHABLE['Collection.<init>(Context,DB,String,boolean)'] = ('no_trigger_in_app',
  'The body calls this(context, db, path, false, false), so the server argument is dropped (passed as false). The only caller of this constructor is the three-argument constructor, which has no caller itself. Storage uses the five-argument form.',
  'com/ichi2/libanki/Collection.java:133-135; com/ichi2/libanki/Collection.java:129-131; com/ichi2/libanki/Storage.java:63', 'SOURCE')

UNREACHABLE['Collection._qaData()'] = ('no_trigger_in_app',
  'No caller in the source root. The one-argument _qaData(String) is called from this method (Collection.java:1030) and from renderQA(int[],String) (Collection.java:951). renderQA() (Collection.java:932) and renderQA(int[],String) have no caller in the source root, so no entry point reaches either.',
  'com/ichi2/libanki/Collection.java:1029-1031; com/ichi2/libanki/Collection.java:930-938; com/ichi2/libanki/Collection.java:951', 'SOURCE')

UNREACHABLE['Collection._qaData(String)'] = ('no_trigger_in_app',
  'Called only from _qaData() (Collection.java:1030) and from renderQA(int[],String) (Collection.java:951). Neither caller is reached from an entry point (see _qaData() and renderQA above).',
  'com/ichi2/libanki/Collection.java:1034-1036; com/ichi2/libanki/Collection.java:1030; com/ichi2/libanki/Collection.java:951', 'SOURCE')

UNREACHABLE['Collection.emptyCardReport'] = ('no_trigger_in_app',
  'Declared at Collection.java:868. No call exists in the source root (grep for emptyCardReport finds only the declaration). The find-empty-cards task calls emptyCids (DeckTask.java:1230) and not this method.',
  'com/ichi2/libanki/Collection.java:868-870; com/ichi2/async/DeckTask.java:1226-1234', 'SOURCE')

UNREACHABLE['Collection.findCards(String)'] = ('no_trigger_in_app',
  'No caller in the source root. The one Collection.findCards call site found is Sched.java:1569, which passes two arguments (search, orderlimit) and so uses findCards(String,String). No call uses the one-argument form.',
  'com/ichi2/libanki/Collection.java:1059-1061; com/ichi2/libanki/Sched.java:1569', 'SOURCE')

UNREACHABLE['Collection.findDupes(String)'] = ('no_trigger_in_app',
  'No caller in the source root. The grep for findDupes finds only the declarations in Collection.java and the Finder helpers, which are called only from the Collection overloads.',
  'com/ichi2/libanki/Collection.java:1101-1103; com/ichi2/libanki/Finder.java:955-957', 'SOURCE')

UNREACHABLE['Collection.findDupes(String,String)'] = ('no_trigger_in_app',
  'No caller in the source root. The one-argument overload calls Finder.findDupes directly (Collection.java:1102), not this overload. Finder.findDupes(Collection,String,String) is called only from Collection.',
  'com/ichi2/libanki/Collection.java:1106-1108; com/ichi2/libanki/Collection.java:1102; com/ichi2/libanki/Finder.java:963', 'SOURCE')

UNREACHABLE['Collection.findReplace(List,String,String)'] = ('no_trigger_in_app',
  'No caller in the source root. The Finder static overloads are called only from the Collection overloads, and none of those has a caller.',
  'com/ichi2/libanki/Collection.java:1081-1083; com/ichi2/libanki/Finder.java:806-810', 'SOURCE')

UNREACHABLE['Collection.findReplace(List,String,String,String)'] = ('no_trigger_in_app',
  'No call site in the source root. The Finder overload with a field argument (Finder.java:818-820) is called only from this Collection overload.',
  'com/ichi2/libanki/Collection.java:1091-1093; com/ichi2/libanki/Finder.java:818-820', 'SOURCE')

UNREACHABLE['Collection.findReplace(List,String,String,boolean)'] = ('no_trigger_in_app',
  'No call site in the source root. The Finder overload with a regex flag (Finder.java:813-815) is called only from this Collection overload.',
  'com/ichi2/libanki/Collection.java:1086-1088; com/ichi2/libanki/Finder.java:813-815', 'SOURCE')

UNREACHABLE['Collection.findReplace(List,String,String,boolean,String,boolean)'] = ('no_trigger_in_app',
  'No call site in the source root. The full Finder.findReplace (Finder.java:823-826) is called only from the Collection overloads.',
  'com/ichi2/libanki/Collection.java:1096-1098; com/ichi2/libanki/Finder.java:823-826', 'SOURCE')

UNREACHABLE['Collection.getTimeLimit'] = ('no_trigger_in_app',
  'Declared at Collection.java:1131; it reads the timeLim configuration value. No call exists in the source root (grep for getTimeLimit finds only the declaration).',
  'com/ichi2/libanki/Collection.java:1131-1139', 'SOURCE')
