# AnkiDroid batch 085 (LABEL helper): libanki Collection methods, part 2 (33 methods; 10 UNREACHABLE here).
# The row list is in graphs/AnkiDroid/parts/label_085.md.
# No e() edges: none of these methods is the source of a GUI, ASYNC, INTENT, RESULT or framework edge.
# The routes into the REACHABLE methods are automatic CALL edges from app code (not repeated) or belong to other batches.

UNREACHABLE['Collection.name'] = ('no_trigger_in_app',
  'Declared at Collection.java 169-172 (returns the file name without the .anki2 extension). The grep for .name() over the source root finds no call on a Collection. The only matches are Enum.name() calls on mChartType in AnkiStatsTaskHandler.java 101 and 104, which are a different method.',
  'com/ichi2/libanki/Collection.java:169-172; com/ichi2/anki/stats/AnkiStatsTaskHandler.java:101-104', 'SOURCE')

UNREACHABLE['Collection.noteCount'] = ('no_trigger_in_app',
  'Declared at Collection.java 478-480. The grep for noteCount over the source root finds only this declaration, so nothing calls it.',
  'com/ichi2/libanki/Collection.java:478-480', 'SOURCE')

UNREACHABLE['Collection.setTimeLimit'] = ('no_trigger_in_app',
  'Declared at Collection.java 1122-1124 (writes timeLim to the collection config). The grep for setTimeLimit over the source root finds only this declaration.',
  'com/ichi2/libanki/Collection.java:1122-1124', 'SOURCE')

UNREACHABLE['Collection.save(long)'] = ('no_trigger_in_app',
  'Declared at Collection.java 252-254; it calls save(null, mod) at 253. No caller passes a single long to Collection.save. The calls to save() with no argument (Collection.java 248, 299, 1347) go to the no-argument overload. The only two-argument call on a Collection is Syncer.java 432, which is save(String, long). The grep for save with an argument over the source root finds no other match.',
  'com/ichi2/libanki/Collection.java:247-254; com/ichi2/libanki/sync/Syncer.java:432', 'SOURCE')

UNREACHABLE['Collection.renderQA()'] = ('no_trigger_in_app',
  'Declared at Collection.java 932-934; it calls renderQA(null, card) at 933. The grep for renderQA over the source root finds no call of renderQA() with no arguments. The other matches are _renderQA in Card.java 303-308 and Models.java 1081-1114, which are different methods.',
  'com/ichi2/libanki/Collection.java:932-934; com/ichi2/libanki/Card.java:303-308; com/ichi2/libanki/Models.java:1081-1114', 'SOURCE')

UNREACHABLE['Collection.renderQA(int[],String)'] = ('no_trigger_in_app',
  'Declared at Collection.java 937-959. Its only call is renderQA(null, card) at 933, inside renderQA(), which has no caller. The grep for renderQA finds no other call of this overload.',
  'com/ichi2/libanki/Collection.java:933-959', 'SOURCE')

UNREACHABLE['Collection.previewCards(Note)'] = ('no_trigger_in_app',
  'Declared at Collection.java 746-748; it calls previewCards(note, 0) at 747. The grep for previewCards over the source root finds only the two declarations (717 and 746) and the call at 747. No caller exists.',
  'com/ichi2/libanki/Collection.java:746-748', 'SOURCE')

UNREACHABLE['Collection.previewCards(Note,int)'] = ('no_trigger_in_app',
  'Declared at Collection.java 717-745. Its only call is previewCards(note, 0) at 747, inside previewCards(Note), which has no caller.',
  'com/ichi2/libanki/Collection.java:717-747', 'SOURCE')

UNREACHABLE['Collection.newNote()'] = ('no_trigger_in_app',
  'Declared at Collection.java 486-488; it calls newNote(true) at 487. The grep for newNote over the source root finds no call with no arguments. The only call of a newNote overload outside Collection is CardTemplateEditor.java 530, which passes a model (newNote(JSONObject)).',
  'com/ichi2/libanki/Collection.java:486-488; com/ichi2/anki/CardTemplateEditor.java:530', 'SOURCE')

UNREACHABLE['Collection.newNote(boolean)'] = ('no_trigger_in_app',
  'Declared at Collection.java 496-498. Its only caller is newNote() at 487, which has no caller, so this overload is never reached. The grep finds no other call with a boolean argument.',
  'com/ichi2/libanki/Collection.java:487; com/ichi2/libanki/Collection.java:496-498', 'SOURCE')
