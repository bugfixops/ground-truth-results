# AnkiDroid batch 102 (LABEL helper). libanki Utils, 40 methods. The full row list is in
# graphs/AnkiDroid/parts/label_102.md.
#
# One e() call: the FRAMEWORK edge from getImportableDecks to its anonymous FileFilter, because the JDK
# calls FileFilter.accept and auto_calls.json does not record that step. Every other caller into these methods is a bytecode CALL edge that is already in
# graphs/AnkiDroid/auto_calls.json, so none is written here. The UNREACHABLE entries below are the
# ten methods with no route from an entry point (8 no_trigger_in_app, 2 branch_never_taken).
# Text is repeated inline on each entry, with no module-level names.

e('libanki.Utils.getImportableDecks', 'libanki.Utils$1.accept', 'FRAMEWORK',
  'the directory listing hands each entry to the anonymous FileFilter: java.io.File.listFiles(FileFilter) calls FileFilter.accept, which keeps .apkg files',
  cls='non_standard',
  via=['java.io.File.listFiles(FileFilter) calls FileFilter.accept once per directory entry (JDK library dispatch; fw_src File.java is a 404 stub)'],
  evidence='SRC com/ichi2/libanki/Utils.java:904-921, 910-914; INFERRED java.io.File.listFiles calls FileFilter.accept once per entry (JDK behaviour, not in fw_src)',
  note='The listing runs only when the AnkiDroid directory exists and is a directory (Utils.java:909).')

UNREACHABLE['libanki.Utils.<init>'] = ('no_trigger_in_app', "Private no-argument constructor of a class that holds only static members (the comment says it prevents instantiation). The grep for 'new Utils(' over the source root finds no match, and auto_calls.json has no record that targets libanki.Utils.<init>. Nothing constructs the class.", 'SRC com/ichi2/libanki/Utils.java:109-112; grep new Utils( over the source root: no match', 'SOURCE')

UNREACHABLE['libanki.Utils._incGuid'] = ('branch_never_taken', "Only called from incGuid (Utils.java:432) and from itself (440). incGuid is reached only through Anki2Importer.java:295, which sits behind the guard at 291-293 (return false while mDupeOnSchemaChange is false). The field is set false in the constructor (84). The only setter, setDupeOnSchemaChange (770-772), has no caller, so the branch is never taken.", 'SRC com/ichi2/libanki/Utils.java:431-445; com/ichi2/libanki/importer/Anki2Importer.java:82-86, 286-297, 770-772', 'SOURCE')

UNREACHABLE['libanki.Utils.compress'] = ('no_trigger_in_app', "Deflater helper with no caller. The grep for compress( over the source root finds only the definition and Bitmap.compress at BasicImageFieldController.java:204, which is a Bitmap method and not this one. auto_calls.json has no record that targets it.", 'SRC com/ichi2/libanki/Utils.java:670-684; com/ichi2/anki/multimediacard/fields/BasicImageFieldController.java:200-206', 'SOURCE')

UNREACHABLE['libanki.Utils.fmtPercentage(Double)'] = ('no_trigger_in_app', "Its body calls the two-argument overload. The grep for fmtPercentage( over the source root finds only the two definitions and the call at Utils.java:224. No caller of this one-argument overload exists, and auto_calls.json has no record that targets it.", 'SRC com/ichi2/libanki/Utils.java:221-232', 'SOURCE')

UNREACHABLE['libanki.Utils.fmtPercentage(Double,int)'] = ('no_trigger_in_app', "The only caller is fmtPercentage(Double) (Utils.java:224), and that overload has no caller (see the previous entry). auto_calls.json has one record for this overload, from fmtPercentage(Double) at Utils.java:224.", 'SRC com/ichi2/libanki/Utils.java:224, 226-232', 'SOURCE')

UNREACHABLE['libanki.Utils.ids2str(JSONArray)'] = ('no_trigger_in_app', "No call site passes a JSONArray. The grep for ids2str( over the source root lists every call site, and each argument is an int[], long[], Long[], List or the result of arrayList2array. auto_calls.json resolves all ids2str calls to the int[], long[], Long[] or List overloads, with zero records for JSONArray.", 'SRC com/ichi2/libanki/Utils.java:346-368; com/ichi2/libanki/Collection.java:818-830, 934-946, 1322-1330; com/ichi2/libanki/sync/Syncer.java:830-842', 'SOURCE')

UNREACHABLE['libanki.Utils.incGuid'] = ('branch_never_taken', "Anki2Importer._uniquifyNote calls it at line 295 only after the guard at 291-293 returns false when mDupeOnSchemaChange is false. The constructor sets that field to false (Anki2Importer.java:84). The only setter, setDupeOnSchemaChange (770-772), has no caller (the grep over the source root finds only its definition), so the call at 295 never runs.", 'SRC com/ichi2/libanki/Utils.java:431-433; com/ichi2/libanki/importer/Anki2Importer.java:82-86, 286-297, 768-772', 'SOURCE')

UNREACHABLE['libanki.Utils.printDate'] = ('no_trigger_in_app', "Debug logger with no caller. The grep for printDate( over the source root finds only the definition, and auto_calls.json has no record that targets it.", 'SRC com/ichi2/libanki/Utils.java:752-758', 'SOURCE')

UNREACHABLE['libanki.Utils.replaceLineBreak'] = ('no_trigger_in_app', "Helper with no caller. The grep for replaceLineBreak( over the source root finds only the definition, and auto_calls.json has no record that targets it.", 'SRC com/ichi2/libanki/Utils.java:584-586', 'SOURCE')

UNREACHABLE['libanki.Utils.toPrimitive(Long[])'] = ('no_trigger_in_app', "All seven call sites pass a Collection<Long>, so they resolve to toPrimitive(Collection). auto_calls.json has seven records for the Collection overload and none for the Long[] overload.", 'SRC com/ichi2/libanki/Utils.java:807-815; com/ichi2/libanki/Sched.java:2258-2270; com/ichi2/libanki/Models.java:515-519, 574-578, 792-795, 1003-1008; com/ichi2/libanki/Finder.java:890-896', 'SOURCE')
