# AnkiDroid batch 043 (LABEL helper). ExportDialog and ImportDialog: 27 methods. The full row list is in
# graphs/AnkiDroid/parts/label_043.md. All 27 methods are REACHABLE, so this part has no UNREACHABLE entries.
#
# Route ownership:
# - Auto CALL edges (auto_calls.json) are not written here: the button callbacks, the DialogHandler and IntentHandler
#   routes, the newInstance factories and the anonymous-class constructors.
# - Written here: the page edges from S_DLG_EXPORT and S_DLG_IMPORT to the anonymous callbacks (the page is the source,
#   so the edge belongs to this part), and the two dismissAllDialogFragments forwards to AnkiActivity, which
#   auto_calls.json does not record.
# - Batch 002 has S_DLG_EXPORT -> DeckPicker.exportApkg and S_DLG_IMPORT -> DeckPicker.importAdd / importReplace
#   directly. Those routes coexist with the callback routes written here.
#
# Gates: MG372 (no importable .apkg file, as on a fresh install: the SELECT list is empty). Range MG372-MG381.
# Predefined constants used: STATE_APKG (an .apkg file is available to import).

# --- Export dialog page (S_DLG_EXPORT, created by DeckPicker.java:624 and 1916).
e('S_DLG_EXPORT', 'ExportDialog$1.onClick', 'GUI',
  'the Cancel button of the export dialog is tapped',
  env=None,
  gui=['the Cancel button of the export dialog is tapped'],
  evidence='SRC com/ichi2/anki/dialogs/ExportDialog.java:104-109',
  note='The negative button callback. Its only call is the auto CALL to ExportDialog.dismissAllDialogFragments at line 107.')

e('S_DLG_EXPORT', 'ExportDialog$2.onClick', 'GUI',
  'the OK button of the export dialog is tapped',
  env=None,
  gui=['the OK button of the export dialog is tapped'],
  evidence='SRC com/ichi2/anki/dialogs/ExportDialog.java:96-103',
  note='The positive button callback: exportApkg at line 100 (auto CALL to DeckPicker.exportApkg) and dismiss at line 101 (auto CALL). Batch 002 also has S_DLG_EXPORT -> DeckPicker.exportApkg directly; both routes stay.')

e('S_DLG_EXPORT', 'ExportDialog$3.onSelection', 'GUI',
  'an export option (schedule or media) is checked or unchecked',
  env=None,
  gui=['an export option (schedule or media) is checked or unchecked'],
  evidence='SRC com/ichi2/anki/dialogs/ExportDialog.java:75-95',
  note='The multi-choice callback sets mIncludeSched and mIncludeMedia (lines 81-93); the positive button reads them at line 100.')

# --- Import dialog page (S_DLG_IMPORT, created by DeckPicker.java:1096 and reached from action_import at 563).
e('S_DLG_IMPORT', 'ImportDialog$1.onNegative', 'GUI',
  'the Cancel button of the import hint dialog is tapped',
  env=None,
  gui=['the Cancel button of the import hint dialog is tapped'],
  evidence='SRC com/ichi2/anki/dialogs/ImportDialog.java:80-82; SRC com/ichi2/anki/DeckPicker.java:561-563',
  note='The hint dialog comes from action_import, which has no guard. Its only call is the auto CALL to ImportDialog.dismissAllDialogFragments at line 81.')

e('S_DLG_IMPORT', 'ImportDialog$1.onPositive', 'GUI',
  'the OK button of the import hint dialog is tapped',
  env=None,
  gui=['the OK button of the import hint dialog is tapped'],
  evidence='SRC com/ichi2/anki/dialogs/ImportDialog.java:75-77',
  note='Calls DeckPicker.showImportDialog(int) with DIALOG_IMPORT_SELECT (auto CALL, cha, line 76).')

e('S_DLG_IMPORT', 'ImportDialog$2.onShow', 'FRAMEWORK',
  'the import list is empty, so the dialog is shown and closes at once',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/ImportDialog.java:89-97; FW-SRC core/java/android/app/Dialog.java:333, 392-395, 1367',
  note='MISSING GATE MG372: no .apkg file is importable (the import folder is empty, as on a fresh install). No predefined ENV or STATE constant covers this, so env and needs_state are unset. The framework path is Dialog.show calling sendShowMessage (Dialog.java:333, 392-395), and the handler calling onShow (Dialog.java:1367). The MaterialDialog hop from showListener to setOnShowListener is not in fw_src: INFERRED.')

e('S_DLG_IMPORT', 'ImportDialog$3.onSelection', 'GUI',
  'an .apkg file is chosen from the import list',
  env=None,
  needs_state=STATE_APKG,
  gui=['an .apkg file is chosen from the import list'],
  evidence='SRC com/ichi2/anki/dialogs/ImportDialog.java:108-122',
  note='The list exists only when at least one .apkg file is importable (STATE_APKG). Line 116 chooses REPLACE_CONFIRM for collection.apkg and line 119 chooses ADD_CONFIRM otherwise; auto_calls.json records the same DeckPicker.showImportDialog(int,String) pair at line 119 only.')

e('S_DLG_IMPORT', 'ImportDialog$4.onPositive', 'GUI',
  'the Add button of the add confirmation is tapped',
  env=None,
  needs_state=STATE_APKG,
  gui=['the Add button of the add confirmation is tapped'],
  evidence='SRC com/ichi2/anki/dialogs/ImportDialog.java:131-137',
  note='Calls DeckPicker.importAdd (auto CALL, cha, line 134) and ImportDialog.dismissAllDialogFragments (auto CALL, line 135).')

e('S_DLG_IMPORT', 'ImportDialog$5.onPositive', 'GUI',
  'the Replace button of the replace confirmation is tapped',
  env=None,
  needs_state=STATE_APKG,
  gui=['the Replace button of the replace confirmation is tapped'],
  evidence='SRC com/ichi2/anki/dialogs/ImportDialog.java:145-151',
  note='Calls DeckPicker.importReplace (auto CALL, cha, line 148) and ImportDialog.dismissAllDialogFragments (auto CALL, line 149).')

# --- Missing listener forwards to the activity (auto_calls.json has no record for these two pairs).
e('ExportDialog.dismissAllDialogFragments', 'AnkiActivity.dismissAllDialogFragments', 'CALL',
  'the export dialog asks its activity to dismiss the dialog stack (listener call at line 115)',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/ExportDialog.java:114-116; SRC com/ichi2/anki/AnkiActivity.java:464-466; SRC com/ichi2/anki/DeckPicker.java:110-112',
  note='The call goes through the ExportDialogListener interface, which DeckPicker implements. DeckPicker does not declare dismissAllDialogFragments, so the target is AnkiActivity.dismissAllDialogFragments (AnkiActivity.java:464).')

e('ImportDialog.dismissAllDialogFragments', 'AnkiActivity.dismissAllDialogFragments', 'CALL',
  'the import dialog asks its activity to dismiss the dialog stack (listener call at line 160)',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/ImportDialog.java:159-161; SRC com/ichi2/anki/AnkiActivity.java:464-466; SRC com/ichi2/anki/DeckPicker.java:110-112',
  note='The call goes through the ImportDialogListener interface, which DeckPicker implements. DeckPicker does not declare dismissAllDialogFragments, so the target is AnkiActivity.dismissAllDialogFragments (AnkiActivity.java:464).')
