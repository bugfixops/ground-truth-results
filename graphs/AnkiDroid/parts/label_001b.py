# AnkiDroid batch 001, part B (LABEL helper). Writes the INTENT edges from IntentHandler.onCreate to the
# activity it starts (DeckPicker), as directed by the coordinator. IntentHandler.onCreate is not listed in
# scratch/batches/batch_001.txt, and no batch file lists it, so no other part writes these edges.
# DeckPicker is started from three branches of onCreate; each start site is its own edge because the
# outside-intent condition (env) differs by site. IntentHandler.<init> and IntentHandler$1.onPositive start no activity.
# ENV_OTHER_APP_INTENT is predefined in graph_def.py (line 108).

e('IntentHandler.onCreate', 'DeckPicker.<init>', 'INTENT',
  'the user opens AnkiDroid from the launcher (ACTION_MAIN with CATEGORY_LAUNCHER); IntentHandler.onCreate starts DeckPicker with startActivityIfNeeded',
  guard='action is neither Intent.ACTION_VIEW (line 46) nor com.ichi2.anki.DO_SYNC (line 126), so the else branch at lines 132-138 runs; DeckPicker starts only if no other task exists, otherwise the previous task is shown (comment lines 133-134)',
  env=None,
  note='Launcher start site (1 of 3 in IntentHandler.onCreate that start DeckPicker). No outside intent is needed, so env is None.',
  evidence='SRC com/ichi2/anki/IntentHandler.java:43; SRC com/ichi2/anki/IntentHandler.java:132-138; SRC AndroidManifest.xml:85-89')

e('IntentHandler.onCreate', 'DeckPicker.<init>', 'INTENT',
  'another app (or adb) sends a VIEW intent for an .apkg file or content URI; IntentHandler.onCreate starts DeckPicker after the import dialog message is stored',
  guard='action equals Intent.ACTION_VIEW (line 46) and successful is true (lines 105-108): content scheme with a name ending .apkg (lines 79-82; the dummy name unknown_filename.apkg at lines 68-71 when the MIME type is application/apkg or the data is a valid zip) and copyFileToCache succeeded (line 85), or file scheme with a path ending .apkg (lines 93-99)',
  env=ENV_OTHER_APP_INTENT,
  note='VIEW start site (2 of 3). The start depends on an outside intent, so env is ENV_OTHER_APP_INTENT.',
  evidence='SRC com/ichi2/anki/IntentHandler.java:46; SRC com/ichi2/anki/IntentHandler.java:43; SRC com/ichi2/anki/IntentHandler.java:85; SRC com/ichi2/anki/IntentHandler.java:93-108')

e('IntentHandler.onCreate', 'DeckPicker.<init>', 'INTENT',
  'another app (or adb) sends the com.ichi2.anki.DO_SYNC action; IntentHandler.onCreate stores MSG_DO_SYNC and starts DeckPicker',
  guard='action is not Intent.ACTION_VIEW (line 46) and equals com.ichi2.anki.DO_SYNC (line 126); sendDoSyncMsg (line 127) stores MSG_DO_SYNC, then startActivity at line 130',
  env=ENV_OTHER_APP_INTENT,
  note='DO_SYNC start site (3 of 3). The start depends on an outside intent, so env is ENV_OTHER_APP_INTENT.',
  evidence='SRC com/ichi2/anki/IntentHandler.java:126-130; SRC com/ichi2/anki/IntentHandler.java:172-177')
