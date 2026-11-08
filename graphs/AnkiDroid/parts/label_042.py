# AnkiDroid batch 042 (LABEL helper). Five DeckPicker dialog classes, 36 methods: DeckPickerBackupNoSpaceLeftDialog,
# DeckPickerConfirmDeleteDeckDialog, DeckPickerContextMenu, DeckPickerExportCompleteDialog, DeckPickerNoSpaceLeftDialog.
# The full row list is in graphs/AnkiDroid/parts/label_042.md. All 36 methods are REACHABLE; there are no UNREACHABLE entries.
#
# Route ownership:
# - CALL edges from the dialog methods into their callees and the newInstance/constructor calls come from auto_calls.json.
#   They are not written here. The automatic edge DeckPickerContextMenu$1.onSelection -> DeckPicker.renameDeckDialog()
#   (DeckPickerContextMenu.java:142) is present in auto_calls.json, so it is not repeated.
# - Button and cancel listeners are dispatched by the MaterialDialog library (not in fw_src), so every GUI edge below is INFERRED.
# - The page edges below belong here because their destination is a method of this batch.
# - Existing label_002 page edges (S_DLG_DECKPICKER_CONTEXT -> DeckPicker.confirmDeckDeletion() and emptyFiltered,
#   S_DLG_DECKPICKER_DELETE_DECK -> DeckPicker.deleteContextMenuDeck, S_DLG_DECKPICKER_EXPORT_DONE -> DeckPicker.emailFile)
#   skip these listeners. They are not changed here.
#
# Gates: MG362 (NO_SPACE page, free space below the threshold). MG363 (DeckPickerExportCompleteDialog.getDialogHandlerMessage,
# the activity is stopped; no edge written, see the .md row). STATE_SETTINGS (BACKUP_NO_SPACE page, noSpaceLeft preference).

# --- DeckPickerContextMenu (long-press menu of a deck row). Page: S_DLG_DECKPICKER_CONTEXT.
e('S_DLG_DECKPICKER_CONTEXT', 'DeckPickerContextMenu$1.onSelection', 'GUI',
  'tap a row of the deck long-press context menu',
  env=None,
  gui=['tap a row of the deck long-press context menu'],
  evidence='SRC com/ichi2/anki/dialogs/DeckPickerContextMenu.java:60-74, 117-119',
  note='The list callback mContextMenuListener is set on the builder at line 72. Each case calls an automatic CALL edge. The GUI dispatch is the MaterialDialog library (not in fw_src): INFERRED. The CHA edge DeckPickerContextMenu$1.onSelection -> StudyOptionsActivity.onRequireDeckListUpdate (line 154) cannot run here: DeckPicker is the activity and implements StudyOptionsListener (DeckPicker.java:110-111). It is already listed in the sup() of graph_def.py (line 1236).')

# --- DeckPickerConfirmDeleteDeckDialog. Page: S_DLG_DECKPICKER_DELETE_DECK.
e('S_DLG_DECKPICKER_DELETE_DECK', 'DeckPickerConfirmDeleteDeckDialog$1.onPositive', 'GUI',
  'press the positive (delete) button of the confirm-delete dialog',
  env=None,
  gui=['press the positive (delete) button of the confirm-delete dialog'],
  evidence='SRC com/ichi2/anki/dialogs/DeckPickerConfirmDeleteDeckDialog.java:34-39',
  note='The button callback is set at line 34. Body: deleteContextMenuDeck (automatic CALL, line 37), then dismissAllDialogFragments (line 38). The existing label_002 GUI edge from the same page to DeckPicker.deleteContextMenuDeck skips this listener. Library dispatch INFERRED.')

e('S_DLG_DECKPICKER_DELETE_DECK', 'DeckPickerConfirmDeleteDeckDialog$1.onNegative', 'GUI',
  'press the negative (cancel) button of the confirm-delete dialog',
  env=None,
  gui=['press the negative (cancel) button of the confirm-delete dialog'],
  evidence='SRC com/ichi2/anki/dialogs/DeckPickerConfirmDeleteDeckDialog.java:41-44',
  note='Body: dismissAllDialogFragments (automatic CALL, line 43). Library dispatch INFERRED.')

# --- DeckPickerBackupNoSpaceLeftDialog. Page: S_DLG_DECKPICKER_BACKUP_NO_SPACE (shown only when the noSpaceLeft preference is set).
e('S_DLG_DECKPICKER_BACKUP_NO_SPACE', 'DeckPickerBackupNoSpaceLeftDialog$2.onPositive', 'GUI',
  'press OK on the backup-no-space dialog',
  env=None,
  needs_state=STATE_SETTINGS,
  gui=['press OK on the backup-no-space dialog'],
  evidence='SRC com/ichi2/anki/dialogs/DeckPickerBackupNoSpaceLeftDialog.java:30-34; SRC com/ichi2/anki/DeckPicker.java:851-854',
  note='The page is shown only when the noSpaceLeft preference is true (DeckPicker.java:851; the preference is set by BackupManager.performBackup at BackupManager.java:156). The preference is STATE_SETTINGS. Body: finishWithoutAnimation (automatic CALL, line 33). Library dispatch INFERRED.')

e('S_DLG_DECKPICKER_BACKUP_NO_SPACE', 'DeckPickerBackupNoSpaceLeftDialog$1.onCancel', 'GUI',
  'cancel the backup-no-space dialog (back key or outside tap)',
  env=None,
  needs_state=STATE_SETTINGS,
  gui=['cancel the backup-no-space dialog (back key or outside tap)'],
  evidence='SRC com/ichi2/anki/dialogs/DeckPickerBackupNoSpaceLeftDialog.java:36-41',
  note='cancelable(true) at line 36. The page gate is STATE_SETTINGS, as on the OK edge. Body: finishWithoutAnimation (automatic CALL, line 40). Library cancel dispatch INFERRED.')

# --- DeckPickerExportCompleteDialog. Page: S_DLG_DECKPICKER_EXPORT_DONE.
e('S_DLG_DECKPICKER_EXPORT_DONE', 'DeckPickerExportCompleteDialog$1.onPositive', 'GUI',
  'press OK on the export-complete dialog (email the exported file)',
  env=None,
  gui=['press OK on the export-complete dialog (email the exported file)'],
  evidence='SRC com/ichi2/anki/dialogs/DeckPickerExportCompleteDialog.java:32-37',
  note='Body: dismissAllDialogFragments (line 35), then DeckPicker.emailFile (automatic CALL, line 36). The existing label_002 GUI edge from the same page to DeckPicker.emailFile skips this listener. Library dispatch INFERRED.')

e('S_DLG_DECKPICKER_EXPORT_DONE', 'DeckPickerExportCompleteDialog$1.onNegative', 'GUI',
  'press Cancel on the export-complete dialog',
  env=None,
  gui=['press Cancel on the export-complete dialog'],
  evidence='SRC com/ichi2/anki/dialogs/DeckPickerExportCompleteDialog.java:39-42',
  note='Body: dismissAllDialogFragments (automatic CALL, line 41). Library dispatch INFERRED.')

# --- DeckPickerNoSpaceLeftDialog. Page: S_DLG_DECKPICKER_NO_SPACE (MISSING GATE MG362: shown only when free space is low).
e('S_DLG_DECKPICKER_NO_SPACE', 'DeckPickerNoSpaceLeftDialog$2.onPositive', 'GUI',
  'press OK on the no-space-left dialog',
  env=None,
  gui=['press OK on the no-space-left dialog'],
  evidence='SRC com/ichi2/anki/dialogs/DeckPickerNoSpaceLeftDialog.java:28-32; SRC com/ichi2/anki/DeckPicker.java:848-850',
  note='MISSING GATE MG362: the page is shown only when BackupManager.enoughDiscSpace is false (free space below MIN_FREE_SPACE, BackupManager.java:207-209). No predefined ENV or STATE kind covers low free space, so env and needs_state are unset. Body: startLoadingCollection (automatic CALL, line 31). Library dispatch INFERRED.')

e('S_DLG_DECKPICKER_NO_SPACE', 'DeckPickerNoSpaceLeftDialog$1.onCancel', 'GUI',
  'cancel the no-space-left dialog (back key or outside tap)',
  env=None,
  gui=['cancel the no-space-left dialog (back key or outside tap)'],
  evidence='SRC com/ichi2/anki/dialogs/DeckPickerNoSpaceLeftDialog.java:26, 34-39',
  note='MISSING GATE MG362, as on the OK edge (the page is shown only when free space is low); env and needs_state are unset. cancelable(true) at line 26. Body: startLoadingCollection (automatic CALL, line 37). Library cancel dispatch INFERRED.')
