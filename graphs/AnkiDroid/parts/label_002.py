# AnkiDroid batch 002 (LABEL helper): DeckPicker methods. Items and routes are in label_002.md.
# Edges written here:
#   - edges whose source is a batch-002 method: FRAMEWORK, ENTERS, REGISTER, ASYNC;
#   - page -> batch-002 method edges (RESULT, GUI), written here because the destination is in this batch
#     (ownership rule: page-sourced edges are written by the part that holds the destination);
#   - UNREACHABLE for DeckPicker.hasErrorFiles.
# Edges whose source is outside batch 002 are not written here (see graphs/AnkiDroid/scratch/conflicts_002.md).
# Constants used (defined in graph_def.py): ENV_STORAGE, ENV_PERM_STORAGE, STATE_COLLECTION, STATE_DECK.
# MISSING GATE notes (MG1, MG4, MG5, MG6) are text only: no env or needs_state is set for them.

# ---- FRAMEWORK (5) ----

e('DeckPicker.onCreate', 'DeckPicker.onRestoreInstanceState', 'FRAMEWORK',
  'the framework restores saved instance state into the recreated activity',
  env=None,
  note='Written here because onCreate is the batch-002 source. Batch 003 REACHABLE rows depend on this edge (see conflicts_002.md). Only when saved state exists (ActivityThread 2746-2751).',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2747-2751; SRC com/ichi2/anki/DeckPicker.java:723-726')

e('DeckPicker.firstCollectionOpen', 'DeckPicker.onRequestPermissionsResult', 'FRAMEWORK',
  'the storage permission result from the request made in firstCollectionOpen is dispatched back to the activity',
  env=None,
  note='firstCollectionOpen calls ActivityCompat.requestPermissions (DeckPicker.java:450-451). Framework start at Activity.java 4382-4383; dispatch at 7267-7270 and 7412-7419. Batch 003 REACHABLE rows depend on this edge.',
  evidence='FW-SRC core/java/android/app/Activity.java:4382-4383, 7267-7270, 7412-7419; SRC com/ichi2/anki/DeckPicker.java:442-455, 680-682')

e('DeckPicker.onCreate', 'DeckPicker.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework builds the options menu for the activity',
  env=None,
  note='Activity.onCreatePanelMenu calls onCreateOptionsMenu. The exact time the panel is prepared is not modelled; the edge starts at onCreate, the batch-002 source on the route.',
  evidence='FW-SRC core/java/android/app/Activity.java:3386-3388; SRC com/ichi2/anki/DeckPicker.java:523-524')

e('DeckPicker.onCreate', 'DeckPicker.onAttachedToWindow', 'FRAMEWORK',
  'the decor view attaches to the window and the framework calls onAttachedToWindow',
  env=None,
  note='APPROXIMATION: the framework attaches the window after onResume (batch 003 owns onResume). The edge starts at onCreate because onCreate is the batch-002 source. See conflicts_002.md.',
  evidence='FW-SRC core/java/com/android/internal/policy/DecorView.java:1585-1590; FW-SRC core/java/android/app/Activity.java:3169; SRC com/ichi2/anki/DeckPicker.java:2113-2119')

e('DeckPicker.finishWithAnimation', 'DeckPicker.onDestroy', 'FRAMEWORK',
  'the activity finishes and the framework performs destroy, which calls onDestroy',
  env=None,
  note='finishWithAnimation -> AnkiActivity.finishWithAnimation -> Activity.finish -> performDestroy -> onDestroy.',
  evidence='FW-SRC core/java/android/app/Activity.java:5526-5528, 7204-7208; SRC com/ichi2/anki/AnkiActivity.java:206-209; SRC com/ichi2/anki/DeckPicker.java:749-750')

# ---- ENTERS (17): method -> page, condition in the trigger text ----

e('DeckPicker.onCreate', 'S_DECKPICKER', 'ENTERS',
  'the collection is open (colOpen true) so the deck list is shown',
  env=ENV_PERM_STORAGE, needs_state=STATE_COLLECTION,
  note='firstCollectionOpen (line 357) then startup screens when colOpen is true (lines 415-417). Storage permission is the ENV_PERM_STORAGE gate.',
  evidence='SRC com/ichi2/anki/DeckPicker.java:357; SRC com/ichi2/anki/DeckPicker.java:415-417')

e('DeckPicker.onCreate', 'S_PREFERENCES', 'ENTERS',
  'the collection is not open and the AnkiDroid directory is inaccessible: the advanced preferences open to update the path',
  env=ENV_STORAGE,
  note='OPEN DECISION: ENV_STORAGE is used for the directory-inaccessible branch (see conflicts_002.md). The branch runs only when the SD card is mounted.',
  evidence='SRC com/ichi2/anki/DeckPicker.java:418-428')

e('DeckPicker.onCreate', 'S_DLG_DATABASE_ERROR', 'ENTERS',
  'the collection is not open and the storage checks pass: the cursor-size dialog (id 9) or the load-failed dialog (id 0) is shown',
  env=None,
  note='MISSING GATE MG1: no STATE exists for an unopenable collection. The gate is not modelled here; env and needs_state are unset.',
  evidence='SRC com/ichi2/anki/DeckPicker.java:418, 430-433; SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:27-36')

e('DeckPicker.addNote', 'S_NOTEEDITOR', 'ENTERS',
  'the add-note floating button is tapped and the note editor opens for a new note',
  env=None,
  note='The editor returns through RESULT to onActivityResult (written below).',
  evidence='SRC com/ichi2/anki/DeckPicker.java:840-844')

e('DeckPicker.loginToSyncServer', 'S_MYACCOUNT', 'ENTERS',
  'a login for sync is needed, so the MyAccount activity opens for login',
  env=None,
  note='The caller of this method is the sync-error dialog (gui edge below, MG4).',
  evidence='SRC com/ichi2/anki/DeckPicker.java:1570-1573')

e('DeckPicker.onOptionsItemSelected', 'S_DLG_IMPORT', 'ENTERS',
  'the import menu item is tapped and the import dialog opens',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:561-563')

e('DeckPicker.onOptionsItemSelected', 'S_DLG_DATABASE_ERROR', 'ENTERS',
  'the check-database or restore-backup menu item is tapped and the database dialog opens (ids 6 and 7)',
  env=None,
  note='User-initiated, so no MG. The dialog is shown through the showDatabaseErrorDialog helper (DeckPicker.java:1026-1028).',
  evidence='SRC com/ichi2/anki/DeckPicker.java:595-598, 616-619, 1026-1028')

e('DeckPicker.onOptionsItemSelected', 'S_DLG_MEDIA_CHECK', 'ENTERS',
  'the check-media menu item is tapped and the media check dialog opens',
  env=None,
  note='The dialog is shown through the showMediaCheckDialog helper.',
  evidence='SRC com/ichi2/anki/DeckPicker.java:600-603')

e('DeckPicker.onOptionsItemSelected', 'S_DLG_EXPORT', 'ENTERS',
  'the export menu item is tapped and the export dialog opens',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:621-625')

e('DeckPicker.onOptionsItemSelected', 'S_MODELBROWSER', 'ENTERS',
  'the model browser menu item is tapped and the model browser opens',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:610-614')

e('DeckPicker.exportDeck', 'S_DLG_EXPORT', 'ENTERS',
  'a deck export is requested and the export dialog opens for that deck',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1909-1916')

e('DeckPicker.confirmDeckDeletion(long)', 'S_DLG_DECKPICKER_DELETE_DECK', 'ENTERS',
  'a deck other than the default deck (did != 1) that has cards (cnt != 0) is to be deleted: the delete-confirmation dialog opens',
  env=None, needs_state=STATE_DECK,
  note='Guard: did != 1 (line 1977) and cnt != 0 (line 1994). When cnt is 0, deleteDeck is called directly (line 1995).',
  evidence='SRC com/ichi2/anki/DeckPicker.java:1972-1978, 1991-1995, 2008')

e('DeckPicker.handleDbError', 'S_DLG_DATABASE_ERROR', 'ENTERS',
  'a database error result is reported and the load-failed dialog opens',
  env=None,
  note='MISSING GATE MG1: no STATE for an unopenable collection or load failure. The gate is not modelled here.',
  evidence='SRC com/ichi2/anki/DeckPicker.java:1243-1245')

e('DeckPicker.onCollectionLoadError', 'S_DLG_DATABASE_ERROR', 'ENTERS',
  'the collection load error is reported and the load-failed dialog opens through DialogHandler (indirect)',
  env=None,
  note='MISSING GATE MG1 (indirect through the DialogHandler message path).',
  evidence='SRC com/ichi2/anki/DeckPicker.java:835-837; SRC com/ichi2/anki/dialogs/DialogHandler.java:58-60')

e('DeckPicker.deleteUnused', 'S_DLG_SIMPLE_MESSAGE', 'ENTERS',
  'unused media is deleted and a simple message reports the result (indirect through showSimpleMessageDialog)',
  env=None,
  note='MISSING GATE MG6: no STATE for unused media. The gate is not modelled here.',
  evidence='SRC com/ichi2/anki/DeckPicker.java:1227-1233')

e('DeckPicker.loadStudyOptionsFragment', 'S_STUDYOPTIONS_FRAG', 'ENTERS',
  'the device uses the fragmented (tablet) layout and the study options fragment is loaded',
  env=None,
  note='Only when mFragmented is true (DeckPicker.java:829 under mFragmented; check at 1650-1655).',
  evidence='SRC com/ichi2/anki/DeckPicker.java:829, 1650-1655')

e('DeckPicker.onFinishedStartup', 'S_DLG_CONFIRMATION', 'ENTERS',
  'the mod-schema change needs confirmation (ConfirmModSchemaException) and the force-full-sync confirmation dialog opens through DialogHandler (indirect)',
  env=None,
  note='MISSING GATE MG5: the ConfirmModSchemaException path (catch at line 814) is not modelled. The gate is not modelled here.',
  evidence='SRC com/ichi2/anki/DeckPicker.java:805-832; SRC com/ichi2/anki/dialogs/DialogHandler.java:88-90')

# ---- RESULT (8): page -> DeckPicker.onActivityResult ----

e('S_NOTEEDITOR', 'DeckPicker.onActivityResult', 'RESULT',
  'the note editor finishes and returns a result to the deck picker',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:634-641, 840-844')

e('S_MYACCOUNT', 'DeckPicker.onActivityResult', 'RESULT',
  'the MyAccount login activity finishes and returns a result',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:634-641, 1570-1573')

e('S_PREFERENCES', 'DeckPicker.onActivityResult', 'RESULT',
  'the preferences activity opened for the path update (REQUEST_PATH_UPDATE) returns a result',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:428, 634-641')

e('S_INFO', 'DeckPicker.onActivityResult', 'RESULT',
  'the Info page opened for a new version returns a result',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:938-947')

e('S_STUDYOPTIONS', 'DeckPicker.onActivityResult', 'RESULT',
  'the study options activity finishes and returns a result',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1695-1703')

e('S_CARDBROWSER', 'DeckPicker.onActivityResult', 'RESULT',
  'the card browser finishes and returns a result (REQUEST_BROWSE_CARDS)',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1708-1713')

e('S_REVIEWER', 'DeckPicker.onActivityResult', 'RESULT',
  'the reviewer finishes and returns a result (REQUEST_REVIEW)',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:2128-2130')

e('S_MODELBROWSER', 'DeckPicker.onActivityResult', 'RESULT',
  'the model browser finishes and returns a result',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:610-614')

# ---- GUI (19): page -> method, via gui() ----

gui('S_DECKPICKER', 'DeckPicker.onBackPressed',
    'back key pressed on the deck list with the navigation drawer closed',
    evidence='SRC com/ichi2/anki/DeckPicker.java:773-786')

gui('S_DECKPICKER', 'DeckPicker.onOptionsItemSelected',
    'an options menu item is tapped on the deck list',
    evidence='SRC com/ichi2/anki/DeckPicker.java:544-549')

gui('S_DLG_DECKPICKER_CONTEXT', 'DeckPicker.confirmDeckDeletion()',
    'the delete item of the deck context menu is tapped',
    evidence='SRC com/ichi2/anki/dialogs/DeckPickerContextMenu.java:122-124')

gui('S_DLG_DECKPICKER_CONTEXT', 'DeckPicker.emptyFiltered',
    'the empty-filtered-deck item of the deck context menu is tapped',
    evidence='SRC com/ichi2/anki/dialogs/DeckPickerContextMenu.java:164-166')

gui('S_DLG_DECKPICKER_DELETE_DECK', 'DeckPicker.deleteContextMenuDeck',
    'the confirm button of the delete-deck dialog is tapped',
    evidence='SRC com/ichi2/anki/dialogs/DeckPickerConfirmDeleteDeckDialog.java:36-37')

gui('S_STUDYOPTIONS_FRAG', 'DeckPicker.confirmDeckDeletion(long)',
    'the delete item in the study options fragment is tapped (fragmented layout only)',
    evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:331-332')

gui('S_STUDYOPTIONS_FRAG', 'DeckPicker.exportDeck',
    'the export item in the study options fragment is tapped (fragmented layout only)',
    evidence='SRC com/ichi2/anki/StudyOptionsFragment.java:334-335')

gui('S_DLG_EXPORT', 'DeckPicker.exportApkg',
    'the positive button of the export dialog is tapped',
    evidence='SRC com/ichi2/anki/dialogs/ExportDialog.java:98-100')

gui('S_DLG_IMPORT', 'DeckPicker.importAdd',
    'the add button of the import dialog is tapped',
    evidence='SRC com/ichi2/anki/dialogs/ImportDialog.java:133-134')

gui('S_DLG_IMPORT', 'DeckPicker.importReplace',
    'the replace button of the import dialog is tapped',
    evidence='SRC com/ichi2/anki/dialogs/ImportDialog.java:147-148')

gui('S_DLG_DATABASE_ERROR', 'DeckPicker.integrityCheck',
    'the positive button of the database-check confirmation is tapped',
    evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:294-302')

gui('S_DLG_DATABASE_ERROR', 'DeckPicker.exit',
    'the negative button of the load-failed dialog is tapped',
    note='MISSING GATE MG1: the page is reached only through the unopenable-collection path (no STATE). The gate is not modelled here.',
    evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:89-92')

gui('S_DLG_MEDIA_CHECK', 'DeckPicker.mediaCheck',
    'the positive button of the media check dialog is tapped',
    evidence='SRC com/ichi2/anki/dialogs/MediaCheckDialog.java:69-70')

gui('S_DLG_MEDIA_CHECK', 'DeckPicker.deleteUnused',
    'the delete-unused button of the media check dialog is tapped',
    note='MISSING GATE MG6: unused-media state is not modelled. The gate is not modelled here.',
    evidence='SRC com/ichi2/anki/dialogs/MediaCheckDialog.java:126-128')

gui('S_DLG_DECKPICKER_EXPORT_DONE', 'DeckPicker.emailFile',
    'the email button of the export-complete dialog is tapped',
    evidence='SRC com/ichi2/anki/dialogs/DeckPickerExportCompleteDialog.java:34-36')

gui('S_DLG_SYNC_ERROR', 'DeckPicker.loginToSyncServer',
    'the login button of the sync-error dialog is tapped',
    note='MISSING GATE MG4: the failed-sync state is not modelled. S_DLG_SYNC_ERROR has no ENTERS owner yet (see conflicts_002.md).',
    evidence='SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:80-81')

gui('S_DLG_SYNC_ERROR', 'DeckPicker.mediaCheck',
    'the media check button of the sync-error dialog is tapped',
    note='MISSING GATE MG4: the failed-sync state is not modelled. S_DLG_SYNC_ERROR has no ENTERS owner yet.',
    evidence='SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:209-210')

gui('S_DLG_CUSTOM_STUDY', 'DeckPicker.onCreateCustomStudySession',
    'the positive button of the custom study dialog is tapped',
    evidence='SRC com/ichi2/anki/dialogs/CustomStudyDialog.java:467')

gui('S_DLG_CUSTOM_STUDY', 'DeckPicker.onExtendStudyLimits',
    'the extend-limits button of the custom study dialog is tapped',
    evidence='SRC com/ichi2/anki/dialogs/CustomStudyDialog.java:482-488')

# ---- REGISTER (3): listener registration in configureFloatingActionsMenu ----

e('DeckPicker.configureFloatingActionsMenu', 'DeckPicker$9.onClick', 'REGISTER',
  'the add-deck floating button listener is registered',
  env=None,
  note='REGISTER is not followed for reachability. The node DeckPicker$9.onClick belongs to batch 006.',
  evidence='SRC com/ichi2/anki/DeckPicker.java:461-463')

e('DeckPicker.configureFloatingActionsMenu', 'DeckPicker$10.onClick', 'REGISTER',
  'the add-shared-deck floating button listener is registered',
  env=None,
  note='REGISTER is not followed for reachability. The node DeckPicker$10.onClick belongs to batch 004.',
  evidence='SRC com/ichi2/anki/DeckPicker.java:488-492')

e('DeckPicker.configureFloatingActionsMenu', 'DeckPicker$11.onClick', 'REGISTER',
  'the add-note floating button listener is registered',
  env=None,
  note='REGISTER is not followed for reachability. The node DeckPicker$11.onClick belongs to batch 004.',
  evidence='SRC com/ichi2/anki/DeckPicker.java:495-499')

# ---- ASYNC (8): method -> listener onPostExecute ----

e('DeckPicker.integrityCheck', 'DeckPicker$15.onPostExecute', 'ASYNC',
  'the integrity check runs as a background task and its result is posted to onPostExecute',
  env=None,
  note='DeckPicker$15.onPostExecute (batch 004) calls handleDbError on failure (line 1172).',
  evidence='SRC com/ichi2/anki/DeckPicker.java:1146-1147')

e('DeckPicker.mediaCheck', 'DeckPicker$16.onPostExecute', 'ASYNC',
  'the media check runs as a background task and its result is posted to onPostExecute',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1190-1191')

e('DeckPicker.importAdd', 'DeckPicker$5.onPostExecute', 'ASYNC',
  'the add-import runs as a background task and its result is posted to onPostExecute',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1579-1581')

e('DeckPicker.importReplace', 'DeckPicker$6.onPostExecute', 'ASYNC',
  'the replace-import runs as a background task and its result is posted to onPostExecute',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1587-1588')

e('DeckPicker.exportApkg', 'DeckPicker$7.onPostExecute', 'ASYNC',
  'the apkg export runs as a background task and its result is posted to onPostExecute',
  env=None,
  note='DeckPicker$7.onPostExecute (batch 006) shows DeckPickerExportCompleteDialog at line 328, which is the route to emailFile.',
  evidence='SRC com/ichi2/anki/DeckPicker.java:1622-1623')

e('DeckPicker.deleteDeck', 'DeckPicker$24.onPostExecute', 'ASYNC',
  'the delete-deck task runs in the background and its result is posted to onPostExecute',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:2016-2017')

e('DeckPicker.emptyFiltered', 'DeckPicker$25.onPostExecute', 'ASYNC',
  'the empty-cram task runs in the background (TASK_TYPE_EMPTY_CRAM) and its result is posted to onPostExecute',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:2106-2109')

e('DeckPicker.handleEmptyCards', 'DeckPicker$27.onPostExecute', 'ASYNC',
  'the empty-cards task runs in the background and its result is posted to onPostExecute',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:2171-2172')

# ---- UNREACHABLE (1) ----

UNREACHABLE['DeckPicker.hasErrorFiles'] = ('no_trigger_in_app', 'the only caller is DatabaseErrorDialog.java:126, inside case DIALOG_DB_ERROR (id 1); no code passes or sends id 1, so the case never runs and hasErrorFiles is never called', 'SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:28; SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:96-126; SRC com/ichi2/anki/dialogs/DialogHandler.java:87', 'SOURCE')
