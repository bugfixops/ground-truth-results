
# ---- Q-R7-9 decided: dead (reviewer, 2026-11-09)
# The api module (com.ichi2.anki.api) is compiled into the APK (AnkiDroid/build.gradle:69, compile project(":api")), but no
# AnkiDroid code outside api/ calls AddContentApi or any other class of the module: a grep over the app root for
# AddContentApi, NoteInfo and com.ichi2.anki.api finds no file outside api/ (2026-11-09). Another app that uses the client
# API runs its own copy of the library in its own process, so this APK's copy never executes. The 25 S_ENTRY ENTRY edges of
# batch 055 are removed (graph_def.py, part 055), and the 53 methods that they made reachable are UNREACHABLE with the same
# kind as the other entries that have no caller in the APK (no_trigger_in_app). The earlier closed_by_configuration and
# closed_by_api_level entries of parts 055 and 056 stay as they are.

_Q_R7_9_REASON = ('Q-R7-9 decided dead (reviewer, 2026-11-09). Client API class of the api module. No AnkiDroid code outside api/ '
                  'calls AddContentApi or another com.ichi2.anki.api class (grep over the app root); a caller app runs its own '
                  'copy of the library, so this APK copy never runs. The only callers are other methods of the same module.')

_Q_R7_9_FILES = {
    'AddContentApi': 'SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:57',
    'AddContentApi$CompatV1': 'SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:622',
    'AddContentApi$CompatV2': 'SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:687',
    'NoteInfo': 'SRC api/src/main/java/com/ichi2/anki/api/NoteInfo.java:30',
    'api.Utils': 'SRC api/src/main/java/com/ichi2/anki/api/Utils.java:32',
    'BasicModel': 'SRC api/src/main/java/com/ichi2/anki/api/BasicModel.java:6',
    'Basic2Model': 'SRC api/src/main/java/com/ichi2/anki/api/Basic2Model.java:6',
}

_Q_R7_9_METHODS = [
    'AddContentApi.<clinit>', 'AddContentApi.<init>', 'AddContentApi.addNewBasic2Model', 'AddContentApi.addNewBasicModel',
    'AddContentApi.addNewCustomModel', 'AddContentApi.addNewDeck', 'AddContentApi.addNote',
    'AddContentApi.addNoteForContentValues', 'AddContentApi.addNoteInternal', 'AddContentApi.addNotes',
    'AddContentApi.findDuplicateNotes(long,String)', 'AddContentApi.findDuplicateNotes(long,List)',
    'AddContentApi.getAnkiDroidPackageName', 'AddContentApi.getApiHostSpecVersion', 'AddContentApi.getCompat',
    'AddContentApi.getCurrentModelId', 'AddContentApi.getDeckList', 'AddContentApi.getDeckName', 'AddContentApi.getFieldList',
    'AddContentApi.getModelList()', 'AddContentApi.getModelList(int)', 'AddContentApi.getModelName', 'AddContentApi.getNote',
    'AddContentApi.getNoteCount', 'AddContentApi.getSelectedDeckName', 'AddContentApi.previewNewNote',
    'AddContentApi.updateNote', 'AddContentApi.updateNoteFields', 'AddContentApi.updateNoteTags',
    'AddContentApi$CompatV1.<init>', 'AddContentApi$CompatV1.addNoteToDuplicatesArray', 'AddContentApi$CompatV2.<init>',
    'AddContentApi$CompatV2.findDuplicateNotes', 'AddContentApi$CompatV2.insertNotes', 'AddContentApi$CompatV2.queryNotes',
    'Basic2Model.<clinit>', 'BasicModel.<clinit>',
    'NoteInfo.<init>(long,String[],Set)', 'NoteInfo.<init>(NoteInfo)', 'NoteInfo.buildFromCursor', 'NoteInfo.getFields',
    'NoteInfo.getId', 'NoteInfo.getKey', 'NoteInfo.getTags',
    'api.Utils.<clinit>', 'api.Utils.entsToTxt', 'api.Utils.fieldChecksum', 'api.Utils.joinFields', 'api.Utils.joinTags',
    'api.Utils.splitFields', 'api.Utils.splitTags', 'api.Utils.stripHTML', 'api.Utils.stripHTMLMedia',
]

for _q_m in _Q_R7_9_METHODS:
    _q_cls = _q_m.split('(')[0].rsplit('.', 1)[0]
    UNREACHABLE[_q_m] = ('no_trigger_in_app', _Q_R7_9_REASON,
                         _Q_R7_9_FILES[_q_cls] + '; AnkiDroid/build.gradle:69', 'SOURCE')
del _q_m, _q_cls

# ---- sup for Q-R7-9: the 65 auto CALL edges between methods of the api module. Every source is itself UNREACHABLE (above,
# or the closed entries of parts 055 and 056), so none of these calls runs in the APK.
sup(('AddContentApi$CompatV2.<init>', 'AddContentApi$CompatV1.<init>'),
    ('AddContentApi.getCompat', 'AddContentApi$CompatV1.<init>'),
    ('AddContentApi$CompatV1.findDuplicateNotes', 'AddContentApi$CompatV1.addNoteToDuplicatesArray'),
    ('AddContentApi$CompatV2.findDuplicateNotes', 'AddContentApi$CompatV1.addNoteToDuplicatesArray'),
    ('AddContentApi.getCompat', 'AddContentApi$CompatV2.<init>'),
    ('AddContentApi$CompatV1.findDuplicateNotes', 'AddContentApi.<clinit>'),
    ('AddContentApi$CompatV1.insertNotes', 'AddContentApi.<clinit>'),
    ('AddContentApi$CompatV1.queryNotes', 'AddContentApi.<clinit>'),
    ('AddContentApi$CompatV2.findDuplicateNotes', 'AddContentApi.<clinit>'),
    ('AddContentApi$CompatV2.insertNotes', 'AddContentApi.<clinit>'),
    ('AddContentApi$CompatV2.queryNotes', 'AddContentApi.<clinit>'),
    ('AddContentApi.addNewBasic2Model', 'AddContentApi.addNewCustomModel'),
    ('AddContentApi.addNewBasicModel', 'AddContentApi.addNewCustomModel'),
    ('AddContentApi$CompatV1.insertNotes', 'AddContentApi.addNoteForContentValues'),
    ('AddContentApi.addNoteInternal', 'AddContentApi.addNoteForContentValues'),
    ('AddContentApi.addNote', 'AddContentApi.addNoteInternal'),
    ('AddContentApi.previewNewNote', 'AddContentApi.addNoteInternal'),
    ('AddContentApi.getCompat', 'AddContentApi.getApiHostSpecVersion'),
    ('AddContentApi.addNotes', 'AddContentApi.getCompat'),
    ('AddContentApi.findDuplicateNotes(long,List)', 'AddContentApi.getCompat'),
    ('AddContentApi.findDuplicateNotes(long,String)', 'AddContentApi.getCompat'),
    ('AddContentApi.getNoteCount', 'AddContentApi.getCompat'),
    ('AddContentApi.getDeckName', 'AddContentApi.getDeckList'),
    ('AddContentApi$CompatV1.findDuplicateNotes', 'AddContentApi.getFieldList'),
    ('AddContentApi.getModelName', 'AddContentApi.getModelList()'),
    ('AddContentApi.getModelList()', 'AddContentApi.getModelList(int)'),
    ('AddContentApi$CompatV1.findDuplicateNotes', 'AddContentApi.getModelName'),
    ('AddContentApi$CompatV1.queryNotes', 'AddContentApi.getModelName'),
    ('AddContentApi.updateNoteFields', 'AddContentApi.updateNote'),
    ('AddContentApi.updateNoteTags', 'AddContentApi.updateNote'),
    ('AddContentApi.addNewBasic2Model', 'Basic2Model.<clinit>'),
    ('AddContentApi.addNewBasicModel', 'BasicModel.<clinit>'),
    ('AddContentApi$CompatV2.findDuplicateNotes', 'NoteInfo.<init>(NoteInfo)'),
    ('NoteInfo.buildFromCursor', 'NoteInfo.<init>(long,String[],Set)'),
    ('AddContentApi$CompatV1.findDuplicateNotes', 'NoteInfo.buildFromCursor'),
    ('AddContentApi$CompatV2.findDuplicateNotes', 'NoteInfo.buildFromCursor'),
    ('AddContentApi.getNote', 'NoteInfo.buildFromCursor'),
    ('NoteInfo.<init>(NoteInfo)', 'NoteInfo.getFields'),
    ('NoteInfo.getKey', 'NoteInfo.getFields'),
    ('NoteInfo.<init>(NoteInfo)', 'NoteInfo.getId'),
    ('AddContentApi$CompatV2.findDuplicateNotes', 'NoteInfo.getKey'),
    ('NoteInfo.<init>(NoteInfo)', 'NoteInfo.getTags'),
    ('AddContentApi$CompatV2.findDuplicateNotes', 'api.Utils.<clinit>'),
    ('AddContentApi.addNewCustomModel', 'api.Utils.<clinit>'),
    ('AddContentApi.addNoteInternal', 'api.Utils.<clinit>'),
    ('AddContentApi.addNotes', 'api.Utils.<clinit>'),
    ('AddContentApi.getFieldList', 'api.Utils.<clinit>'),
    ('AddContentApi.getModelList(int)', 'api.Utils.<clinit>'),
    ('AddContentApi.updateNote', 'api.Utils.<clinit>'),
    ('NoteInfo.buildFromCursor', 'api.Utils.<clinit>'),
    ('api.Utils.stripHTML', 'api.Utils.entsToTxt'),
    ('AddContentApi$CompatV2.findDuplicateNotes', 'api.Utils.fieldChecksum'),
    ('AddContentApi.addNewCustomModel', 'api.Utils.joinFields'),
    ('AddContentApi.addNoteInternal', 'api.Utils.joinFields'),
    ('AddContentApi.addNotes', 'api.Utils.joinFields'),
    ('AddContentApi.updateNote', 'api.Utils.joinFields'),
    ('AddContentApi.addNoteInternal', 'api.Utils.joinTags'),
    ('AddContentApi.addNotes', 'api.Utils.joinTags'),
    ('AddContentApi.updateNote', 'api.Utils.joinTags'),
    ('AddContentApi.getFieldList', 'api.Utils.splitFields'),
    ('AddContentApi.getModelList(int)', 'api.Utils.splitFields'),
    ('NoteInfo.buildFromCursor', 'api.Utils.splitFields'),
    ('NoteInfo.buildFromCursor', 'api.Utils.splitTags'),
    ('api.Utils.stripHTMLMedia', 'api.Utils.stripHTML'),
    ('api.Utils.fieldChecksum', 'api.Utils.stripHTMLMedia'))
