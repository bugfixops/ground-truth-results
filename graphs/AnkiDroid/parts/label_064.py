# AnkiDroid batch 064 (LABEL helper). 18 methods; the full row list is in graphs/AnkiDroid/parts/label_064.md.
# Three UNREACHABLE entries and no e() calls. The other 15 methods are REACHABLE through automatic CALL edges (see the .md).
# Every string is written inline; no module-level names.

UNREACHABLE['TaskOperations.<init>'] = ('no_trigger_in_app', 'TaskOperations has only static methods and no explicit constructor. A grep for "new TaskOperations" over the app source root finds no instance creation; every use is a static call to stopTaskGracefully. No route creates an instance.', 'SRC com/ichi2/anki/runtimetools/TaskOperations.java:25-38; SRC com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:474-478; SRC com/ichi2/anki/multimediacard/activity/TranslationActivity.java:405', 'SOURCE')

UNREACHABLE['NoteService.<init>'] = ('no_trigger_in_app', 'NoteService has only static methods and no explicit constructor. A grep for "new NoteService" over the app source root finds nothing; every use is a static call in NoteEditor.', 'SRC com/ichi2/anki/servicelayer/NoteService.java:38-45; SRC com/ichi2/anki/NoteEditor.java:1037-1038; SRC com/ichi2/anki/NoteEditor.java:1055; SRC com/ichi2/anki/NoteEditor.java:1138-1139; SRC com/ichi2/anki/NoteEditor.java:1151-1152', 'SOURCE')

UNREACHABLE['NoteService.updateJsonNoteFromMultimediaNote'] = ('no_trigger_in_app', 'Public static method with no caller. A grep for the name over the app source root finds only its definition, so the reverse copy (multimedia note into the editor note) is never called.', 'SRC com/ichi2/anki/servicelayer/NoteService.java:101-113', 'SOURCE')
