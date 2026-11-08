# AnkiDroid batch 055 (LABEL helper). AddContentApi (client API class in the api module): 39 methods. The full row list is
# in graphs/AnkiDroid/parts/label_055.md. Source: api/src/main/java/com/ichi2/anki/api/AddContentApi.java, cited relative to
# final_java_only/AnkiDroid/app/AnkiDroid-#4200/. The api module is outside the c1_check roots (AnkiDroid/src/main, fw_src),
# so every api/ cite is reported as file not found by the checker.
#
# Route ownership:
# - The 24 public methods and AddContentApi.<clinit> are the client API. A caller app (its own code, S_ENTRY) runs them in
#   its own process. The 25 ENTRY edges from S_ENTRY are written here. Methods that call the ContentResolver use
#   ENV_PROVIDER_CALL. <init>, <clinit>, getAnkiDroidPackageName and getApiHostSpecVersion use env unset and MG492.
# - Private helpers, getCompat and the Compat objects are reached by CALL edges that auto_calls.json holds. They are not
#   written here.
# - Configuration: getCompat (line 594) picks CompatV1 only when getApiHostSpecVersion() < 2. The manifest declares provider
#   spec 2 (AndroidManifest.xml:329), so CompatV2 runs. CompatV2 overrides queryNotes, insertNotes and findDuplicateNotes
#   without calling super, so the three CompatV1 bodies never run on the installed configuration.
# - CompatV1.<init> is reachable: CompatV2 extends CompatV1 (line 687), so new CompatV2() runs the CompatV1 constructor
#   through the implicit super() call.
# - Auto CALL edges from CompatV2 instance methods to AddContentApi.<clinit> (auto_calls.json, lines 690, 698, 717) are
#   suppression candidates. The outer class is already initialised when an inner instance exists. No sup() is written here.
#
# Gates: MG492 only (batch range MG492-MG501).

# --- Client API: public methods, called from the caller app (S_ENTRY). ENV_PROVIDER_CALL where ContentResolver is used.

e('S_ENTRY', 'AddContentApi.<init>', 'ENTRY',
  'the caller app code constructs the client (new AddContentApi(context)) in its own process',
  env=None,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:67-70',
  note='MISSING GATE MG492: the caller app code is outside AnkiDroid, so no predefined ENV kind covers it. env unset. The constructor only reads the application context and its ContentResolver (lines 68-69), no provider call.')

e('S_ENTRY', 'AddContentApi.<clinit>', 'ENTRY',
  'the caller app code first uses AddContentApi, so the class is initialised in the caller process',
  env=None,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:58-65',
  note='MISSING GATE MG492: same caller as <init>. PROJECTION (line 65) is a non-constant array, so the static initializer exists. env unset.')

e('S_ENTRY', 'AddContentApi.addNewBasic2Model', 'ENTRY',
  'another app calls addNewBasic2Model (new Basic2 note type)',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:311-314',
  note='Calls addNewCustomModel (line 312). The provider writes are in addNewCustomModel (insert at 343, update at 356).')

e('S_ENTRY', 'AddContentApi.addNewBasicModel', 'ENTRY',
  'another app calls addNewBasicModel (new Basic note type)',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:299-302',
  note='Calls addNewCustomModel (line 300). The provider writes are in addNewCustomModel.')

e('S_ENTRY', 'AddContentApi.addNewCustomModel', 'ENTRY',
  'another app calls addNewCustomModel (new note type with its fields and templates)',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:329-359',
  note='ContentResolver.insert on Model.CONTENT_URI (line 343) and update of each template (line 356).')

e('S_ENTRY', 'AddContentApi.addNewDeck', 'ENTRY',
  'another app calls addNewDeck (new deck)',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:466-476',
  note='ContentResolver.insert on Deck.CONTENT_ALL_URI (line 470).')

e('S_ENTRY', 'AddContentApi.addNote', 'ENTRY',
  'another app calls addNote (one new note with fields and tags)',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:81-87',
  note='Calls addNoteInternal (line 82). Provider insert at line 100 and cards query and update at lines 106 and 116.')

e('S_ENTRY', 'AddContentApi.addNotes', 'ENTRY',
  'another app calls addNotes (bulk add of notes into one deck)',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:133-152',
  note='An empty list returns 0 (line 149). Otherwise getCompat().insertNotes (line 151); on the live spec-2 branch that is CompatV2.insertNotes (bulkInsert, line 698).')

e('S_ENTRY', 'AddContentApi.findDuplicateNotes(long,String)', 'ENTRY',
  'another app calls findDuplicateNotes for one key',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:161-167',
  note='Calls getCompat().findDuplicateNotes (line 162). On the live spec-2 branch that is CompatV2.findDuplicateNotes.')

e('S_ENTRY', 'AddContentApi.findDuplicateNotes(long,List)', 'ENTRY',
  'another app calls findDuplicateNotes for a list of keys',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:176-178',
  note='Calls getCompat().findDuplicateNotes (line 177). On the live spec-2 branch that is CompatV2.findDuplicateNotes.')

e('S_ENTRY', 'AddContentApi.getAnkiDroidPackageName', 'ENTRY',
  'the caller app code calls the static getAnkiDroidPackageName(context)',
  env=None,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:547-555',
  note='MISSING GATE MG492: same caller as <init>. env unset. Uses PackageManager.resolveContentProvider (line 549), no ContentResolver call. Returns null when AnkiDroid is not installed (lines 550-553).')

e('S_ENTRY', 'AddContentApi.getApiHostSpecVersion', 'ENTRY',
  'the caller app code calls getApiHostSpecVersion',
  env=None,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:571-583; AndroidManifest.xml:329',
  note='MISSING GATE MG492: same caller as <init>. env unset. Reads the provider spec meta-data via PackageManager (lines 574-579), no ContentResolver call. Also called by getCompat (line 594).')

e('S_ENTRY', 'AddContentApi.getCurrentModelId', 'ENTRY',
  'another app calls getCurrentModelId',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:365-380',
  note='ContentResolver.query on Model.CONTENT_URI (line 368).')

e('S_ENTRY', 'AddContentApi.getDeckList', 'ENTRY',
  'another app calls getDeckList',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:502-519',
  note='ContentResolver.query on Deck.CONTENT_ALL_URI (line 504).')

e('S_ENTRY', 'AddContentApi.getDeckName', 'ENTRY',
  'another app calls getDeckName for one deck id',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:527-537',
  note='Calls getDeckList() (line 528).')

e('S_ENTRY', 'AddContentApi.getFieldList', 'ENTRY',
  'another app calls getFieldList for one note type',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:388-405',
  note='ContentResolver.query on the model URI (line 391).')

e('S_ENTRY', 'AddContentApi.getModelList()', 'ENTRY',
  'another app calls getModelList()',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:411-413',
  note='Calls getModelList(1) (line 412). Provider query in getModelList(int) at line 422.')

e('S_ENTRY', 'AddContentApi.getModelList(int)', 'ENTRY',
  'another app calls getModelList with a minimum field count',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:420-442',
  note='ContentResolver.query on Model.CONTENT_URI (line 422).')

e('S_ENTRY', 'AddContentApi.getModelName', 'ENTRY',
  'another app calls getModelName for one note type id',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:449-459',
  note='Calls getModelList() (line 451).')

e('S_ENTRY', 'AddContentApi.getNote', 'ENTRY',
  'another app calls getNote for one note id',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:224-238',
  note='ContentResolver.query on the note URI (line 226).')

e('S_ENTRY', 'AddContentApi.getNoteCount', 'ENTRY',
  'another app calls getNoteCount for one note type',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:185-195',
  note='Calls getCompat().queryNotes (line 186). On the live spec-2 branch that is CompatV2.queryNotes.')

e('S_ENTRY', 'AddContentApi.getSelectedDeckName', 'ENTRY',
  'another app calls getSelectedDeckName',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:482-496',
  note='ContentResolver.query on Deck.CONTENT_SELECTED_URI (line 483).')

e('S_ENTRY', 'AddContentApi.previewNewNote', 'ENTRY',
  'another app calls previewNewNote (card HTML for a field list, then the temporary note is deleted)',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:262-292',
  note='The guard at line 263 is false on API 27, so the SecurityException is not thrown. Calls addNoteInternal (line 267), query (271) and delete (290).')

e('S_ENTRY', 'AddContentApi.updateNoteFields', 'ENTRY',
  'another app calls updateNoteFields for one note',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:215-217',
  note='Calls updateNote (line 216), which calls ContentResolver.update (line 250).')

e('S_ENTRY', 'AddContentApi.updateNoteTags', 'ENTRY',
  'another app calls updateNoteTags for one note',
  env=ENV_PROVIDER_CALL,
  evidence='SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:204-206',
  note='Calls updateNote (line 205), which calls ContentResolver.update (line 250).')

# --- UNREACHABLE entries (configuration and API level).

UNREACHABLE['AddContentApi$CompatV1.queryNotes'] = ('closed_by_configuration',
  'Overridden by CompatV2.queryNotes (api/src/main/java/com/ichi2/anki/api/AddContentApi.java:689-692). getCompat (line 594) picks CompatV1 only when getApiHostSpecVersion() is below 2. On an installed AnkiDroid the manifest declares provider spec 2 (AndroidManifest.xml:329), so CompatV2 is chosen. The value -1 (lines 575-576) appears only when AnkiDroid is not installed, and then no provider call here can succeed. CompatV2 does not call super, so this body never runs on the installed configuration.',
  'SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:623-631, 594; AndroidManifest.xml:329',
  'SOURCE')

UNREACHABLE['AddContentApi$CompatV1.insertNotes'] = ('closed_by_configuration',
  'Overridden by CompatV2.insertNotes (api/src/main/java/com/ichi2/anki/api/AddContentApi.java:695-699). getCompat (line 594) picks CompatV1 only when getApiHostSpecVersion() is below 2. The manifest declares provider spec 2 (AndroidManifest.xml:329), so CompatV2 is chosen on the installed configuration. The value -1 (lines 575-576) appears only when AnkiDroid is not installed, and then no provider call here can succeed. CompatV2 does not call super, so this body never runs on the installed configuration.',
  'SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:633-643, 594; AndroidManifest.xml:329',
  'SOURCE')

UNREACHABLE['AddContentApi$CompatV1.findDuplicateNotes'] = ('closed_by_configuration',
  'Overridden by CompatV2.findDuplicateNotes (api/src/main/java/com/ichi2/anki/api/AddContentApi.java:702-741). getCompat (line 594) picks CompatV1 only when getApiHostSpecVersion() is below 2. The manifest declares provider spec 2 (AndroidManifest.xml:329), so CompatV2 is chosen on the installed configuration. The value -1 (lines 575-576) appears only when AnkiDroid is not installed, and then no provider call here can succeed. CompatV2 does not call super, so this body never runs on the installed configuration.',
  'SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:645-671, 594; AndroidManifest.xml:329',
  'SOURCE')

UNREACHABLE['AddContentApi.hasReadWritePermission'] = ('closed_by_api_level',
  'The only caller is previewNewNote (api/src/main/java/com/ichi2/anki/api/AddContentApi.java:263). The guard SDK_INT < Build.VERSION_CODES.M && !hasReadWritePermission() short-circuits on API 27, where SDK_INT (27) is not below M (23), so the call never runs. minSdkVersion is 10 (AnkiDroid/build.gradle:12), so the call is reachable only on API 10 to 22.',
  'SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:263, 585-588',
  'SOURCE')
