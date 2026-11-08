# Batch 045 (LABEL helper). SyncErrorDialog, 31 methods. Rows are in graphs/AnkiDroid/parts/label_045.md.
# Edges owned here: 11 GUI edges from page S_DLG_SYNC_ERROR into the anonymous ButtonCallback methods of
# SyncErrorDialog (the destinations are in this batch). UNREACHABLE: SyncErrorDialog$2 (3 entries).
# Automatic CALL edges from auto_calls.json are not written here.

e('S_DLG_SYNC_ERROR', 'SyncErrorDialog$1.onPositive', 'GUI',
  'tap Log in on the not-logged-in sync dialog (type 0)',
  gui=['tap Log in on the not-logged-in sync dialog (type 0)'],
  evidence='SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:78-84; SRC com/ichi2/anki/DeckPicker.java:1277-1283',
  note='MISSING GATE MG393: no account is logged in (the hkey preference is empty, DeckPicker.java:1281-1282). No constant fits, so env and needs_state are unset. The callback runs the activity listener loginToSyncServer (automatic CALL). The button dispatch is MaterialDialog (library, source not read): INFERRED. The direct edge S_DLG_SYNC_ERROR -> DeckPicker.loginToSyncServer (graph_def.py:1039) bypasses this callback; both routes exist.')

e('S_DLG_SYNC_ERROR', 'SyncErrorDialog$3.onPositive', 'GUI',
  'tap keep local on the sync conflict dialog (type 2)',
  env=ENV_NETWORK,
  needs_state=STATE_ACCOUNT,
  gui=['tap keep local on the sync conflict dialog (type 2)'],
  evidence='SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:111-116; SRC com/ichi2/anki/DeckPicker.java:1450-1458',
  note='Type 2 opens from the fullSync answer when the local collection is not empty (DeckPicker.java:1457). The answer needs the network and a stored hkey. The tap calls showSyncErrorDialog(3) (automatic CALL to DeckPicker.showSyncErrorDialog(int)).')

e('S_DLG_SYNC_ERROR', 'SyncErrorDialog$3.onNegative', 'GUI',
  'tap keep remote on the sync conflict dialog (type 2)',
  env=ENV_NETWORK,
  needs_state=STATE_ACCOUNT,
  gui=['tap keep remote on the sync conflict dialog (type 2)'],
  evidence='SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:118-122; SRC com/ichi2/anki/DeckPicker.java:1450-1458',
  note='Same route as the keep-local tap (type 2 opens from the fullSync answer, DeckPicker.java:1457). The tap calls showSyncErrorDialog(4) (automatic CALL to DeckPicker.showSyncErrorDialog(int)).')

e('S_DLG_SYNC_ERROR', 'SyncErrorDialog$3.onNeutral', 'GUI',
  'tap Cancel on the sync conflict dialog (type 2)',
  env=ENV_NETWORK,
  needs_state=STATE_ACCOUNT,
  gui=['tap Cancel on the sync conflict dialog (type 2)'],
  evidence='SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:124-127; SRC com/ichi2/anki/DeckPicker.java:1450-1458',
  note='Same route as the keep-local tap (type 2 opens from the fullSync answer, DeckPicker.java:1457). The callback calls dismissAllDialogFragments (SyncErrorDialog.java:126) and no server call.')

e('S_DLG_SYNC_ERROR', 'SyncErrorDialog$4.onPositive', 'GUI',
  'confirm overwrite with the local collection (type 3)',
  gui=['confirm overwrite with the local collection (type 3)'],
  evidence='SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:135-142, 114-115',
  note='MISSING GATE MG394: type 3 is on screen only after the local-version tap on type 2 (SyncErrorDialog.java:114-115). No constant fits, so env and needs_state are unset. The callback calls sync("upload") and dismissAllDialogFragments (lines 139-140).')

e('S_DLG_SYNC_ERROR', 'SyncErrorDialog$5.onPositive', 'GUI',
  'confirm overwrite with the remote collection (type 4)',
  gui=['confirm overwrite with the remote collection (type 4)'],
  evidence='SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:149-156, 119-121',
  note='MISSING GATE MG394: type 4 is on screen only after the remote-version tap on type 2 (SyncErrorDialog.java:119-121). No constant fits, so env and needs_state are unset. The callback calls sync("download") and dismissAllDialogFragments (lines 153-154).')

e('S_DLG_SYNC_ERROR', 'SyncErrorDialog$6.onPositive', 'GUI',
  'tap keep local on the sanity-check error dialog (type 6)',
  env=ENV_NETWORK,
  needs_state=STATE_ACCOUNT,
  gui=['tap keep local on the sanity-check error dialog (type 6)'],
  evidence='SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:164-170; SRC com/ichi2/anki/DeckPicker.java:1486-1489',
  note='Type 6 opens from the sanityCheckError answer (DeckPicker.java:1486-1489). The answer needs the network and a stored hkey. The tap calls showSyncErrorDialog(7) (automatic CALL to DeckPicker.showSyncErrorDialog(int)).')

e('S_DLG_SYNC_ERROR', 'SyncErrorDialog$6.onNeutral', 'GUI',
  'tap keep remote on the sanity-check error dialog (type 6)',
  env=ENV_NETWORK,
  needs_state=STATE_ACCOUNT,
  gui=['tap keep remote on the sanity-check error dialog (type 6)'],
  evidence='SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:171-175; SRC com/ichi2/anki/DeckPicker.java:1486-1489',
  note='Same route as the keep-local tap (type 6 opens from the sanityCheckError answer, DeckPicker.java:1486-1489). The tap calls showSyncErrorDialog(8) (automatic CALL to DeckPicker.showSyncErrorDialog(int)).')

e('S_DLG_SYNC_ERROR', 'SyncErrorDialog$7.onPositive', 'GUI',
  'confirm overwrite with the local collection after a sanity error (type 7)',
  gui=['confirm overwrite with the local collection after a sanity error (type 7)'],
  evidence='SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:183-189, 167-168',
  note='MISSING GATE MG394: type 7 is on screen only after the local-version tap on type 6 (SyncErrorDialog.java:167-168). No constant fits, so env and needs_state are unset. The callback calls sync("upload") and dismissAllDialogFragments (lines 186-187).')

e('S_DLG_SYNC_ERROR', 'SyncErrorDialog$8.onPositive', 'GUI',
  'confirm overwrite with the remote collection after a sanity error (type 8)',
  gui=['confirm overwrite with the remote collection after a sanity error (type 8)'],
  evidence='SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:196-202, 173-174',
  note='MISSING GATE MG394: type 8 is on screen only after the remote-version tap on type 6 (SyncErrorDialog.java:173-174). No constant fits, so env and needs_state are unset. The callback calls sync("download") and dismissAllDialogFragments (lines 199-200).')

e('S_DLG_SYNC_ERROR', 'SyncErrorDialog$9.onPositive', 'GUI',
  'tap Check media on the media sync error dialog (type 9)',
  env=ENV_NETWORK,
  needs_state=STATE_ACCOUNT,
  gui=['tap Check media on the media sync error dialog (type 9)'],
  evidence='SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:207-213; SRC com/ichi2/anki/DeckPicker.java:1492-1496',
  note='Type 9 opens from the mediaSyncServerError answer (DeckPicker.java:1493-1495). The answer needs the network and a stored hkey. The callback calls mediaCheck() (automatic CALL) and dismissAllDialogFragments (line 211). The direct edge S_DLG_SYNC_ERROR -> DeckPicker.mediaCheck (graph_def.py:1044) bypasses this callback; both routes exist.')

UNREACHABLE['SyncErrorDialog$2.<init>'] = (
    'branch_never_taken',
    'Created only in the case for id 1 (DIALOG_CONNECTION_ERROR, SyncErrorDialog.java:86). No caller passes 1: newInstance is called with 0, 2, 6 and 9 (DeckPicker.java:1282, 1430, 1457, 1488, 1495), and the taps pass 3, 4, 7 and 8 (SyncErrorDialog.java:115, 121, 168, 174). The only other sender of MSG_SHOW_SYNC_ERROR_DIALOG is getDialogHandlerMessage (SyncErrorDialog.java:291), which copies the dialogType of an existing instance (line 293), so id 1 cannot be created. Grep over the source root finds DIALOG_CONNECTION_ERROR only at its declaration (SyncErrorDialog.java:13) and in the switch labels (lines 86 and 255), and no showSyncErrorDialog(1) call.',
    'com/ichi2/anki/dialogs/SyncErrorDialog.java:12-13, 86-91, 255, 288-297; com/ichi2/anki/DeckPicker.java:1049-1061, 1282, 1430, 1457, 1488, 1495; com/ichi2/anki/dialogs/DialogHandler.java:38, 67-70',
    'SOURCE')

UNREACHABLE['SyncErrorDialog$2.onNegative'] = (
    'branch_never_taken',
    'Callback of the case for id 1 (SyncErrorDialog.java:86), which is never taken because no caller creates id 1 (see SyncErrorDialog$2.<init>). Its only call is dismissAllDialogFragments (line 100).',
    'com/ichi2/anki/dialogs/SyncErrorDialog.java:86-102',
    'SOURCE')

UNREACHABLE['SyncErrorDialog$2.onPositive'] = (
    'branch_never_taken',
    'Callback of the case for id 1 (SyncErrorDialog.java:86), which is never taken because no caller creates id 1 (see SyncErrorDialog$2.<init>). Its sync() call and dismissAllDialogFragments (lines 94-95) are in that branch only.',
    'com/ichi2/anki/dialogs/SyncErrorDialog.java:86-96',
    'SOURCE')
