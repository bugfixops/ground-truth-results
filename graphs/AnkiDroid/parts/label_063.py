# AnkiDroid batch 063 (LABEL helper). 34 methods: MultimediaEditableNote (11), NoteFactory (2), LanguageListerBase with $1 (6),
# LanguageListerBeolingus (1), LanguagesLister with $1 (5), LanguagesListerGlosbe (3), MockNoteFactory (2),
# MockPronounciationPageFetcher (2), MockTranslationFetcher (2). The full row list is in graphs/AnkiDroid/parts/label_063.md.
#
# Route ownership: the automatic CALL edges (auto_calls.json) into and out of these methods are not written here.
# Edge written here: the Collections.sort -> Comparator.compare edge of LanguageListerBase, whose source method is in this batch.
# The routes into the language listers and the mocks start from activities and buttons in other batches (NoteEditor,
# BasicTextFieldController, LoadPronounciationActivity, TranslationActivity).

e('LanguageListerBase.getLanguages', 'LanguageListerBase$1.compare', 'FRAMEWORK',
  'Collections.sort calls the anonymous Comparator to order the language names',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/language/LanguageListerBase.java:61-69',
  note='java.util.Collections is not in fw_src (no Collections.java under fw_src/android-8.1.0_r1): INFERRED (source not read). No gate: the sort calls compare for any list with at least two names, and both listers add more than two (com/ichi2/anki/multimediacard/language/LanguageListerBeolingus.java:36-38 adds three, com/ichi2/anki/multimediacard/language/LanguagesListerGlosbe.java:37-45 lists 19 codes). The automatic CALL into LanguageListerBase$1.<init> is not repeated here.')

UNREACHABLE['MultimediaEditableNote.circularSwap'] = ('no_trigger_in_app',
  'No call site in the app. The grep over the app source folder finds only the interface declaration and the implementation.',
  'SRC com/ichi2/anki/multimediacard/IMultimediaEditableNote.java:43; com/ichi2/anki/multimediacard/impl/MultimediaEditableNote.java:41-56',
  'SOURCE')

UNREACHABLE['MultimediaEditableNote.getModelId'] = ('no_trigger_in_app',
  'The only call is in NoteService.updateJsonNoteFromMultimediaNote, and that method has no caller in the app (the grep finds only its declaration), so no route reaches getModelId.',
  'SRC com/ichi2/anki/multimediacard/impl/MultimediaEditableNote.java:128-130; com/ichi2/anki/servicelayer/NoteService.java:101-104',
  'SOURCE')

UNREACHABLE['MultimediaEditableNote.isModified'] = ('no_trigger_in_app',
  'Implements IMultimediaEditableNote.isModified, but no code calls it on a note. Every isModified() call in the app is on an IField object, and the one in setField dispatches to the field class, not to this method.',
  'SRC com/ichi2/anki/multimediacard/IMultimediaEditableNote.java:40; com/ichi2/anki/multimediacard/fields/IField.java:36; com/ichi2/anki/multimediacard/impl/MultimediaEditableNote.java:64-67, 104-109',
  'SOURCE')

UNREACHABLE['NoteFactory.<init>'] = ('no_trigger_in_app',
  'NoteFactory declares no constructor and is never instantiated. Its only member createNote is static and has no caller (the grep finds the class declaration only).',
  'SRC com/ichi2/anki/multimediacard/impl/NoteFactory.java:14-15',
  'SOURCE')

UNREACHABLE['NoteFactory.createNote'] = ('no_trigger_in_app',
  'No call site in the app. The grep over the app source folder finds no reference to NoteFactory or createNote.',
  'SRC com/ichi2/anki/multimediacard/impl/NoteFactory.java:15-36',
  'SOURCE')

UNREACHABLE['LanguagesLister.<init>'] = ('no_trigger_in_app',
  'No new LanguagesLister exists anywhere in the app. The class name occurs only in its own file (grep over the app source folder).',
  'SRC com/ichi2/anki/multimediacard/language/LanguagesLister.java:27-31',
  'SOURCE')

UNREACHABLE['LanguagesLister.getCodeFor'] = ('no_trigger_in_app',
  'The class is never instantiated (see LanguagesLister.<init>), and it does not extend LanguageListerBase, so no base-type call reaches this method.',
  'SRC com/ichi2/anki/multimediacard/language/LanguagesLister.java:27, 45-51',
  'SOURCE')

UNREACHABLE['LanguagesLister.getLanguages'] = ('no_trigger_in_app',
  'The class is never instantiated (see LanguagesLister.<init>), and it does not extend LanguageListerBase, so no base-type call reaches this method.',
  'SRC com/ichi2/anki/multimediacard/language/LanguagesLister.java:27, 54-64',
  'SOURCE')

UNREACHABLE['LanguagesLister$1.<init>'] = ('no_trigger_in_app',
  'The anonymous Comparator is created only in LanguagesLister.getLanguages, which has no route.',
  'SRC com/ichi2/anki/multimediacard/language/LanguagesLister.java:54-62',
  'SOURCE')

UNREACHABLE['LanguagesLister$1.compare'] = ('no_trigger_in_app',
  'Called only by Collections.sort inside LanguagesLister.getLanguages, which has no route.',
  'SRC com/ichi2/anki/multimediacard/language/LanguagesLister.java:54-62',
  'SOURCE')

UNREACHABLE['MockNoteFactory.<init>'] = ('no_trigger_in_app',
  'MockNoteFactory is a test helper with no constructor. No code creates an instance (the grep finds the class declaration only).',
  'SRC com/ichi2/anki/multimediacard/test/MockNoteFactory.java:27-30',
  'SOURCE')

UNREACHABLE['MockNoteFactory.makeNote'] = ('no_trigger_in_app',
  'No call site in the app. The grep over the app source folder finds only the class declaration.',
  'SRC com/ichi2/anki/multimediacard/test/MockNoteFactory.java:30-52',
  'SOURCE')

UNREACHABLE['MockPronounciationPageFetcher.<init>'] = ('no_trigger_in_app',
  'Test helper with no constructor. No code creates an instance.',
  'SRC com/ichi2/anki/multimediacard/test/MockPronounciationPageFetcher.java:22-25',
  'SOURCE')

UNREACHABLE['MockPronounciationPageFetcher.get'] = ('no_trigger_in_app',
  'The only reference is a commented-out call in LoadPronounciationActivity.doInBackground (test branch). No code calls get.',
  'SRC com/ichi2/anki/multimediacard/test/MockPronounciationPageFetcher.java:25-45; com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:200-213',
  'SOURCE')

UNREACHABLE['MockTranslationFetcher.<init>'] = ('no_trigger_in_app',
  'Test helper with no constructor. No code creates an instance.',
  'SRC com/ichi2/anki/multimediacard/test/MockTranslationFetcher.java:22-25',
  'SOURCE')

UNREACHABLE['MockTranslationFetcher.get'] = ('no_trigger_in_app',
  'The only reference is a commented-out call in LoadPronounciationActivity.doInBackground (test branch). No code calls get.',
  'SRC com/ichi2/anki/multimediacard/test/MockTranslationFetcher.java:25-41; com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:200-213',
  'SOURCE')
