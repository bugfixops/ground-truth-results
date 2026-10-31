# AnkiDroid batch 149 (LABEL helper): 40 methods, rows in graphs/AnkiDroid/parts/label_149.md. 39 are already REACHABLE in other parts;
# LinesPoints.<init> is already UNREACHABLE (label_113, graph_def.py:10295), so no UNREACHABLE entry is written here.
# Five edges close routes that were missing: the two no-space dialog pages (opened by DeckPicker.showStartupScreensAndDialogs),
# DeckTask$1.compare (its sort caller), DB$MyDbErrorHandler.onCorruption (its constructor caller, MG802 in the note), and the
# crash-report page, which has no opener in the app source other than ACRA (see the last edge).

e('DeckPicker.showStartupScreensAndDialogs', 'S_DLG_DECKPICKER_BACKUP_NO_SPACE', 'ENTERS',
  'free space is enough and the noSpaceLeft preference is set: the backup-no-space dialog is shown',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/anki/DeckPicker.java:848-854',
  note='The else-if branch at DeckPicker.java:851 runs only when BackupManager.enoughDiscSpace is true (line 848). The noSpaceLeft preference is STATE_SETTINGS. It is set by BackupManager.performBackup (BackupManager.java:156, as in label_042) and removed at line 854 after the dialog is shown. The OK and cancel edges from this page are in label_042 (graph_def.py:5422, 5430).')

e('DeckPicker.showStartupScreensAndDialogs', 'S_DLG_DECKPICKER_NO_SPACE', 'ENTERS',
  'free space is below the threshold (BackupManager.enoughDiscSpace is false): the no-space-left dialog is shown',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:848-850',
  note='MISSING GATE MG362: the page is shown only when free space is low (BackupManager.java:207-209, as in label_042). No predefined ENV or STATE kind covers low free space, so env and needs_state are unset. This is the first branch of the if chain, so it is checked before noSpaceLeft. The OK and cancel edges are in label_042 (graph_def.py:5454, 5461).')

e('DeckTask.doInBackgroundCountModels', 'DeckTask$1.compare', 'FRAMEWORK',
  'Collections.sort calls the Comparator to order the note types when there are two or more',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:1095-1104; INFERRED java.util.Collections.sort calls Comparator.compare (Collections.java not in fw_src, source not read)',
  note='Gate not modelled: the comparator runs only when the list has at least two models. No predefined STATE covers the note-type count, so env and needs_state are unset. The sort call is at DeckTask.java:1095, inside doInBackgroundCountModels (line 1089).')

e('DB.<init>', 'DB$MyDbErrorHandler.onCorruption', 'FRAMEWORK',
  'SQLite finds the collection file damaged and calls DatabaseErrorHandler.onCorruption on the handler that the constructor passed',
  env=None,
  evidence='SRC com/ichi2/libanki/DB.java:64-67, 84-90; INFERRED android.database.sqlite.SQLiteDatabase calls DatabaseErrorHandler.onCorruption (SQLiteDatabase.java not in fw_src, source not read)',
  note='MISSING GATE MG802: the collection file must be damaged. No predefined ENV or STATE kind covers file corruption, so env and needs_state are unset. The handler is passed only in the honeycomb branch (DB.java:64-67, CompatHelper.isHoneycomb); the else branch (68-71) passes no handler. The constructor is DB.java:61-81.')

e('AnkiDroidApp.onCreate', 'S_CRASH_REPORT', 'ENTERS',
  'the app crashes and ACRA opens its report dialog (reportDialogClass)',
  env=None,
  evidence='SRC com/ichi2/anki/AnkiDroidApp.java:54-59 (reportDialogClass = AnkiDroidCrashReportDialog); AnkiDroidApp.java:146, 152 (ACRA.init inside onCreate)',
  note='Opener of the page only. ACRA is set to NEVER in the debug build (AnkiDroidApp.java:155-159, 326-330), so this path is closed by configuration; the four AnkiDroidCrashReportDialog methods keep their closed_by_configuration entries in graph_def.py (around lines 7119-7139) and no method edge is written here.')
