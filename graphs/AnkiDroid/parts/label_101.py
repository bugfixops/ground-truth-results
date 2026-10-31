# AnkiDroid batch 101 (LABEL helper): com.ichi2.libanki.Tags, 19 methods. The full row list is in
# graphs/AnkiDroid/parts/label_101.md.
# Four UNREACHABLE entries (no_trigger_in_app). The other 15 methods are REACHABLE and need no entry here.
# No e() calls: every link in the routes is an ordinary Java call (CALL, written by the builder).

UNREACHABLE['Tags.addToStr'] = ('no_trigger_in_app', 'No live route: the only call to addToStr is in bulkAdd(List,String,boolean) (Tags.java:262), and that method has no live caller (bulkAdd(List,String) and bulkRem have none). A grep of the app source tree finds no other call to addToStr.', 'com/ichi2/libanki/Tags.java:262, 315-323', 'SOURCE')

UNREACHABLE['Tags.bulkAdd(List,String)'] = ('no_trigger_in_app', 'No caller: the body is only bulkAdd(ids, tags, true) (Tags.java:221). A grep of the app source tree finds no call to bulkAdd(List,String). The FIXME at Tags.java:212-219 says it must be fixed before use.', 'com/ichi2/libanki/Tags.java:212-222', 'SOURCE')

UNREACHABLE['Tags.bulkAdd(List,String,boolean)'] = ('no_trigger_in_app', 'Callers are bulkAdd(List,String) (Tags.java:221) and bulkRem (Tags.java:282); neither has a caller. The javadoc at Tags.java:225-228 says the method is unused in AnkiDroid and its behaviour is currently incorrect.', 'com/ichi2/libanki/Tags.java:220-222, 225-228, 229-278, 282', 'SOURCE')

UNREACHABLE['Tags.bulkRem'] = ('no_trigger_in_app', 'No caller: a grep of the app source tree finds no call to bulkRem. Its body is only bulkAdd(ids, tags, false) (Tags.java:282), which has no live caller.', 'com/ichi2/libanki/Tags.java:281-283', 'SOURCE')
