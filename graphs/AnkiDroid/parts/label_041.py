# AnkiDroid batch 041 (LABEL helper). DatabaseErrorDialog: 35 methods. The full row list is in
# graphs/AnkiDroid/parts/label_041.md.
# Methods: <clinit>, <init>, dismissAllDialogFragments, getDialogHandlerMessage, getMessage, getNotificationMessage,
# getNotificationTitle, getTitle, newInstance, onCreateDialog, and the anonymous callbacks $1 to $11.
#
# Route ownership:
# - CALL edges (for example onCreateDialog -> $N.<init>, and the callback bodies calling DeckPicker methods) come from
#   auto_calls.json. They are not written here.
# - The callbacks of the page S_DLG_DATABASE_ERROR are written here: an edge belongs to the part that contains its
#   destination method.
# - $2 (DB_ERROR, id 1) is never created. No caller passes DIALOG_DB_ERROR (grep over the source root).
#
# Gates: MG352 (load failure), MG353 (sqlite3 present), MG355 (a backup exists). MG354 is on method rows only.
# Predefined constants are not used: no ENV or STATE kind fits these gates.
# Page node: S_DLG_DATABASE_ERROR.

# --- Load-failed dialog (id 0, LOAD_FAILED case, DatabaseErrorDialog.java:73-94).
e('S_DLG_DATABASE_ERROR', 'DatabaseErrorDialog$1.onPositive', 'GUI',
  'tap error handling options on the load-failed dialog',
  gui=['tap error handling options on the load-failed dialog'],
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:80-87; SRC com/ichi2/anki/DeckPicker.java:433, 1243-1245, 1478-1479',
  note='MISSING GATE MG352: the load-failed dialog opens only after a collection open failure or a database or I/O failure (DeckPicker.java:433, 1243-1245, 1478-1479). No predefined ENV or STATE kind covers it; env and needs_state unset.')

e('S_DLG_DATABASE_ERROR', 'DatabaseErrorDialog$1.onNegative', 'GUI',
  'tap close on the load-failed dialog (DeckPicker.exit)',
  gui=['tap close on the load-failed dialog (DeckPicker.exit)'],
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:89-92',
  note='MISSING GATE MG352: the load-failed dialog opens only after a collection open failure or a database or I/O failure. No predefined ENV or STATE kind covers it; env and needs_state unset.')

# --- Error handling list (id 2, ERROR_HANDLING case, DatabaseErrorDialog.java:129-199).
e('S_DLG_DATABASE_ERROR', 'DatabaseErrorDialog$3.onSelection', 'GUI',
  'pick one repair option in the error handling list',
  gui=['pick one repair option in the error handling list'],
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:134-156, 168-196',
  note='The list itself has no gate: the list is offered from the no-backup restore dialog (standard route) and from the load-failed dialog (MG352). Option 1 (check database) is offered only when the collection is open (line 134). Option 2 (repair) is offered only with sqlite3 (line 144, MISSING GATE MG353).')

# --- Repair (id 3, REPAIR case, DatabaseErrorDialog.java:201-214).
e('S_DLG_DATABASE_ERROR', 'DatabaseErrorDialog$4.onPositive', 'GUI',
  'tap repair on the repair dialog (repairDeck)',
  gui=['tap repair on the repair dialog (repairDeck)'],
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:65-70, 144-147, 207-212',
  note='MISSING GATE MG353: the repair option is offered only when the sqlite3 command runs with exit code 0 (Runtime exec sqlite3 --version, DatabaseErrorDialog.java:65-70). No predefined ENV or STATE kind covers it; env and needs_state unset.')

# --- Restore, no backup (id 5, RESTORE_BACKUP case, DatabaseErrorDialog.java:216-234).
e('S_DLG_DATABASE_ERROR', 'DatabaseErrorDialog$5.onPositive', 'GUI',
  'tap OK on the no-backup restore dialog (back to the error handling list)',
  gui=['tap OK on the no-backup restore dialog (back to the error handling list)'],
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:224-234; SRC com/ichi2/anki/BackupManager.java:311-326',
  note='No gate on the standard route: the menu item action_restore_backup has no enabled attribute (res/menu/deck_picker.xml:35-38 (src/main)). Caveat: a fresh install is assumed to have no backup file. env and needs_state unset.')

# --- Restore with backups (ids 7 and 6, DatabaseErrorDialog.java:235-273).
e('S_DLG_DATABASE_ERROR', 'DatabaseErrorDialog$6.onSelection', 'GUI',
  'pick a backup date in the restore list (restoreFromBackup)',
  gui=['pick a backup date in the restore list (restoreFromBackup)'],
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:251-270; SRC com/ichi2/anki/BackupManager.java:311-326',
  note='MISSING GATE MG355: the restore list is built only when at least one backup .apkg exists (BackupManager.getBackups non-empty, BackupManager.java:311-326). No predefined ENV or STATE kind covers it; env and needs_state unset.')

e('S_DLG_DATABASE_ERROR', 'DatabaseErrorDialog$7.onNegative', 'GUI',
  'tap cancel on the restore list (dismiss only)',
  gui=['tap cancel on the restore list (dismiss only)'],
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:243-248',
  note='MISSING GATE MG355: the restore list is built only when at least one backup .apkg exists (BackupManager.getBackups non-empty, BackupManager.java:311-326). No predefined ENV or STATE kind covers it; env and needs_state unset.')

# --- New collection (id 5, NEW_COLLECTION case, DatabaseErrorDialog.java:275-292).
e('S_DLG_DATABASE_ERROR', 'DatabaseErrorDialog$8.onPositive', 'GUI',
  'tap create on the new-collection dialog (the old database moves to the broken folder)',
  gui=['tap create on the new-collection dialog (the old database moves to the broken folder)'],
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:280-290',
  note='No gate on the standard route: the error handling list always offers option 5 (DatabaseErrorDialog.java:155-156, 192-194). env and needs_state unset.')

# --- Database check (id 6, CONFIRM_DATABASE_CHECK case, DatabaseErrorDialog.java:294-306).
e('S_DLG_DATABASE_ERROR', 'DatabaseErrorDialog$9.onPositive', 'GUI',
  'tap OK on the database-check confirmation (integrityCheck)',
  gui=['tap OK on the database-check confirmation (integrityCheck)'],
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:139-141, 299-304; SRC com/ichi2/anki/DeckPicker.java:528, 595-598',
  note='No gate on the error handling list route (option 1 is offered when the collection is open, line 134). The menu route (action_check_database) needs ENV_STORAGE (DeckPicker.java:528; res/menu/deck_picker.xml:20-24 (src/main)). env and needs_state unset.')

# --- Restore confirmation (id 7, CONFIRM_RESTORE_BACKUP case, DatabaseErrorDialog.java:308-320).
e('S_DLG_DATABASE_ERROR', 'DatabaseErrorDialog$10.onPositive', 'GUI',
  'tap continue on the restore confirmation (the restore dialog for id 4 follows)',
  gui=['tap continue on the restore confirmation (the restore dialog for id 4 follows)'],
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:313-318; SRC com/ichi2/anki/DeckPicker.java:616-619',
  note='No gate: the menu item action_restore_backup has no enabled attribute and is hidden only on ChromeOS (DeckPicker.java:535). env and needs_state unset.')

# --- Full sync from server (id 8, FULL_SYNC_FROM_SERVER case, DatabaseErrorDialog.java:322-334).
e('S_DLG_DATABASE_ERROR', 'DatabaseErrorDialog$11.onPositive', 'GUI',
  'tap overwrite on the full-sync confirmation (sync download)',
  gui=['tap overwrite on the full-sync confirmation (sync download)'],
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:155-156, 188-191, 327-332',
  note='No gate on the dialog: the error handling list always offers option 4 (DatabaseErrorDialog.java:151-153). The sync it starts needs ENV_NETWORK and belongs to the sync batch; env and needs_state unset.')

# --- DB_ERROR (id 1): never created. Grep over the source root: no caller passes DIALOG_DB_ERROR, and the replayed
# dialogType (DialogHandler.java:87) is the stored id of a fragment, which is never 1.
UNREACHABLE['DatabaseErrorDialog$2.<init>'] = ('branch_never_taken',
    "The DB_ERROR case (id 1, DatabaseErrorDialog.java:96-127) is never entered. DIALOG_DB_ERROR (1) has no caller in the source root. The ids passed to showDatabaseErrorDialog and newInstance are 0, 2, 3, 4, 5, 6, 7, 8 and 9 (DeckPicker.java:431, 433, 597, 618, 1244; DatabaseErrorDialog.java:86, 110, 178-194, 232, 288, 317; DialogHandler.java:60). The replayed id (DialogHandler.java:87) is the stored dialogType of a fragment, so it is never 1 either.",
    'SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:28, 47-53, 96-106; SRC com/ichi2/anki/DeckPicker.java:431, 433, 597, 618, 1026-1027, 1243-1245; SRC com/ichi2/anki/dialogs/DialogHandler.java:60, 87',
    'SOURCE')

UNREACHABLE['DatabaseErrorDialog$2.onNegative'] = ('branch_never_taken',
    "The DB_ERROR case (id 1, DatabaseErrorDialog.java:96-127) is never entered. DIALOG_DB_ERROR (1) has no caller in the source root. The ids passed to showDatabaseErrorDialog and newInstance are 0, 2, 3, 4, 5, 6, 7, 8 and 9 (DeckPicker.java:431, 433, 597, 618, 1244; DatabaseErrorDialog.java:86, 110, 178-194, 232, 288, 317; DialogHandler.java:60). The replayed id (DialogHandler.java:87) is the stored dialogType of a fragment, so it is never 1 either. The callback is created only with the DB_ERROR dialog, so it never runs.",
    'SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:96-106, 113-117; SRC com/ichi2/anki/DeckPicker.java:431, 433, 597, 618, 1026-1027, 1243-1245; SRC com/ichi2/anki/dialogs/DialogHandler.java:60, 87',
    'SOURCE')

UNREACHABLE['DatabaseErrorDialog$2.onNeutral'] = ('branch_never_taken',
    "The DB_ERROR case (id 1, DatabaseErrorDialog.java:96-127) is never entered. DIALOG_DB_ERROR (1) has no caller in the source root. The ids passed to showDatabaseErrorDialog and newInstance are 0, 2, 3, 4, 5, 6, 7, 8 and 9 (DeckPicker.java:431, 433, 597, 618, 1244; DatabaseErrorDialog.java:86, 110, 178-194, 232, 288, 317; DialogHandler.java:60). The replayed id (DialogHandler.java:87) is the stored dialogType of a fragment, so it is never 1 either. The callback is created only with the DB_ERROR dialog, so it never runs.",
    'SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:96-106, 119-122; SRC com/ichi2/anki/DeckPicker.java:431, 433, 597, 618, 1026-1027, 1243-1245; SRC com/ichi2/anki/dialogs/DialogHandler.java:60, 87',
    'SOURCE')

UNREACHABLE['DatabaseErrorDialog$2.onPositive'] = ('branch_never_taken',
    "The DB_ERROR case (id 1, DatabaseErrorDialog.java:96-127) is never entered. DIALOG_DB_ERROR (1) has no caller in the source root. The ids passed to showDatabaseErrorDialog and newInstance are 0, 2, 3, 4, 5, 6, 7, 8 and 9 (DeckPicker.java:431, 433, 597, 618, 1244; DatabaseErrorDialog.java:86, 110, 178-194, 232, 288, 317; DialogHandler.java:60). The replayed id (DialogHandler.java:87) is the stored dialogType of a fragment, so it is never 1 either. The callback is created only with the DB_ERROR dialog, so it never runs.",
    'SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:96-111; SRC com/ichi2/anki/DeckPicker.java:431, 433, 597, 618, 1026-1027, 1243-1245; SRC com/ichi2/anki/dialogs/DialogHandler.java:60, 87',
    'SOURCE')
