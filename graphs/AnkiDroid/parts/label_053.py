# AnkiDroid batch 053 (LABEL helper): MetaDB (21 methods) and ReadText (16 methods), package com.ichi2.anki.
# The full row list is in graphs/AnkiDroid/parts/label_053.md.
#
# Route ownership:
# - Automatic CALL edges (static calls into MetaDB and ReadText, and the anonymous-class constructors
#   ReadText$1.<init>, ReadText$2.<init>, ReadText$3.<init>) come from the builder. They are not written here.
# - E1 (S_REVIEWER -> ReadText$1.onSelection, GUI): the source is a page, so the edge is in the part that
#   contains the destination method (this batch).
# - E2 (ReadText.selectTts -> ReadText$2.run, ASYNC): Handler post with a 500 ms delay.
# - E3 (ReadText.initializeTts -> ReadText$3.onInit, FRAMEWORK): the TextToSpeech init callback.
#
# Gates: ENV_TTS (a TTS engine with at least one locale) and STATE_SETTINGS (the tts preference).
# No MISSING GATE is needed in this batch.

# --- Select TTS dialog: Reviewer menu action_select_tts -> AbstractFlashcardViewer.showSelectTtsDialogue -> ReadText.selectTts.
e('S_REVIEWER', 'ReadText$1.onSelection', 'GUI',
  'pick a language in the Select TTS list',
  env=ENV_TTS,
  needs_state=STATE_SETTINGS,
  gui=['pick a language in the Select TTS list'],
  evidence='SRC com/ichi2/anki/ReadText.java:114-131; SRC com/ichi2/anki/AbstractFlashcardViewer.java:2232-2243; SRC com/ichi2/anki/Reviewer.java:213-215, 305-307',
  note='The list is built only when at least one locale is available (ReadText.java:94-99). The select_tts menu item shows only when mSpeakText is set (Reviewer.java:305-307). The MaterialDialog click dispatch is not in fw_src: INFERRED (source not read).')

# --- Dialog show after a 500 ms delay (posted in ReadText.selectTts).
e('ReadText.selectTts', 'ReadText$2.run', 'ASYNC',
  'the Select TTS dialog is shown after a 500 ms delay',
  env=None,
  evidence='SRC com/ichi2/anki/ReadText.java:134-141; FW-SRC core/java/android/os/Handler.java:427-428, 97-99, 789-791',
  note='The Runnable calls builder.build().show() (ReadText.java:139). The dispatch to run is the Handler route in fw_src.')

# --- TTS engine init callback (created in ReadText.initializeTts, called from AbstractFlashcardViewer.onCollectionLoaded).
e('ReadText.initializeTts', 'ReadText$3.onInit', 'FRAMEWORK',
  'the TTS engine reports that its initialization has finished',
  env=ENV_TTS,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/anki/ReadText.java:174-178, 180-196; the TextToSpeech init dispatch is not in fw_src (source not read)',
  note='initializeTts runs only when mSpeakText is set (AbstractFlashcardViewer.java:904-905). The engine calls onInit with a status; SUCCESS and at least one locale lead to ttsInitialized. The engine callback is INFERRED.')

# --- UNREACHABLE entries (7): no caller found in the app source.
UNREACHABLE['MetaDB.<init>'] = ('no_trigger_in_app',
  'MetaDB declares only static members and no constructor; nothing in the app source creates an instance (no "new MetaDB"), and every use is a static call.',
  'SRC com/ichi2/anki/MetaDB.java:25; grep for "new MetaDB" over src/main/java/com/ichi2 finds nothing',
  'SOURCE')

UNREACHABLE['MetaDB.getLookupDictionary'] = ('no_trigger_in_app',
  'public static getLookupDictionary has no caller in the app source; the grep finds only its declaration.',
  'SRC com/ichi2/anki/MetaDB.java:340-341; grep over src/main/java/com/ichi2 finds no caller',
  'SOURCE')

UNREACHABLE['MetaDB.stripQuotes'] = ('no_trigger_in_app',
  'private helper stripQuotes has no caller in the app source; the grep finds only its declaration.',
  'SRC com/ichi2/anki/MetaDB.java:41, 48-52; grep over src/main/java/com/ichi2 finds no caller',
  'SOURCE')

UNREACHABLE['MetaDB.resetDB'] = ('no_trigger_in_app',
  'public static resetDB has no caller in the app source; the grep finds only its declaration.',
  'SRC com/ichi2/anki/MetaDB.java:135-137; grep over src/main/java/com/ichi2 finds no caller',
  'SOURCE')

UNREACHABLE['MetaDB.resetDeckLanguages'] = ('no_trigger_in_app',
  'public static resetDeckLanguages has no caller in the app source; the grep finds only its declaration.',
  'SRC com/ichi2/anki/MetaDB.java:266-268; grep over src/main/java/com/ichi2 finds no caller',
  'SOURCE')

UNREACHABLE['MetaDB.storeLookupDictionary'] = ('no_trigger_in_app',
  'public static storeLookupDictionary has no caller in the app source; the grep finds only its declaration.',
  'SRC com/ichi2/anki/MetaDB.java:366-368; grep over src/main/java/com/ichi2 finds no caller',
  'SOURCE')

UNREACHABLE['ReadText.<init>'] = ('no_trigger_in_app',
  'ReadText has only static members and no explicit constructor; the grep for "new ReadText" finds nothing, and every use is a static call.',
  'SRC com/ichi2/anki/ReadText.java:37; grep for "new ReadText" over src/main/java/com/ichi2 finds nothing',
  'SOURCE')
