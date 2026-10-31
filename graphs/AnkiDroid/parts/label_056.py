# AnkiDroid batch 056 (LABEL helper). 39 methods, all labelled in graphs/AnkiDroid/parts/label_056.md:
# 28 REACHABLE (rows only, no entry here) and 11 UNREACHABLE (entries below), plus 1 e() edge.
# The 21 api library methods (com.ichi2.anki.api, source under the api root, outside the app source root) are 18 REACHABLE
# and 3 UNREACHABLE. The 6 AnkiDroidCrashReportDialog methods are closed_by_configuration (confirmed_by INFERRED).
#
# Route ownership:
# - The 18 REACHABLE api methods are reached from S_ENTRY through public AddContentApi methods (ENTRY edges written in
#   batch 055, parts/label_055.py). Every later step is an auto CALL record in graphs/AnkiDroid/auto_calls.json, so no
#   e() CALL edge is written here for them.
# - Automatic bytecode CALL edges (DialogHandler$1.<init> from DialogHandler.handleMessage, ContextMenuHelper statics from the
#   DeckPickerContextMenu and CustomStudyDialog callers, UnknownHttpResponseException.getResponseCode from Connection) come from
#   auto_calls.json and are not written here.
# - Edges into the REACHABLE methods from other batches (DeckPicker, IntentHandler, AnkiActivity, Connection, Decks,
#   HttpSyncer, RemoteMediaServer) are not written here.
# - One edge is written: the page S_DLG_CONFIRMATION (destination in this batch) into DialogHandler$1.confirm.
# - No MG id is used: the gate is the predefined STATE_SETTINGS constant, or the path is closed by configuration.

e('S_DLG_CONFIRMATION', 'DialogHandler$1.confirm', 'GUI',
  'tap Yes in the force-full-sync dialog (shown only after an upgrade from an older stored version)',
  needs_state=STATE_SETTINGS,
  gui=['tap Yes in the force-full-sync dialog (shown only after an upgrade from an older stored version)'],
  evidence='SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:42-44, 58; com/ichi2/anki/dialogs/DialogHandler.java:88-98; com/ichi2/anki/DeckPicker.java:810, 824, 866-868, 896-897',
  note='ConfirmationDialog.onPositive (lines 42-44) calls the abstract confirm() (line 43). The anonymous override (DialogHandler.java:92-95) calls getCol().modSchemaNoCheck() (line 94); that call edge is the builder automatic edge and is not written here. The dialog is created by MSG_SHOW_FORCE_FULL_SYNC_DIALOG (DialogHandler.java:88-98), which DeckPicker sends at DeckPicker.java:824 only when mRecommendFullSync is set (DeckPicker.java:810). mRecommendFullSync is set only when the stored lastUpgradeVersion is below 20301208 (DeckPicker.java:896-897). A fresh install sets previous = current (DeckPicker.java:866-868), so the flag stays false. STATE_SETTINGS is the stored lastUpgradeVersion preference.')

UNREACHABLE['Basic2Model.<init>'] = ('no_trigger_in_app',
  'Implicit default constructor of Basic2Model (Basic2Model.java:6). No new Basic2Model exists in the api root or the app root (grep over both). AddContentApi uses only the static arrays of Basic2Model (auto_calls.json record AddContentApi.addNewBasic2Model -> Basic2Model.<clinit>, AddContentApi.java:312), so no route from S_ENTRY constructs it.',
  'SRC api/src/main/java/com/ichi2/anki/api/Basic2Model.java:6; api/src/main/java/com/ichi2/anki/api/AddContentApi.java:312', 'SOURCE')

UNREACHABLE['BasicModel.<init>'] = ('no_trigger_in_app',
  'Implicit default constructor of BasicModel (BasicModel.java:6). No new BasicModel exists in the api root or the app root (grep over both). AddContentApi uses only the static arrays of BasicModel (auto_calls.json record AddContentApi.addNewBasicModel -> BasicModel.<clinit>, AddContentApi.java:300), so no route from S_ENTRY constructs it.',
  'SRC api/src/main/java/com/ichi2/anki/api/BasicModel.java:6; api/src/main/java/com/ichi2/anki/api/AddContentApi.java:300', 'SOURCE')

UNREACHABLE['api.Utils.<init>'] = ('no_trigger_in_app',
  'Implicit constructor of the package-private class Utils (Utils.java:32). The class has only static methods. No new Utils exists in the api root or the app root (grep over both), and no auto_calls.json record targets api.Utils.<init>, so no route from S_ENTRY constructs it.',
  'SRC api/src/main/java/com/ichi2/anki/api/Utils.java:32', 'SOURCE')

UNREACHABLE['StorageAccessException.<init>()'] = ('no_trigger_in_app',
  'No-argument constructor (StorageAccessException.java:6-7). Every new StorageAccessException in the app passes a String (CollectionHelper.java:172, 175, 183), so this constructor has no caller.',
  'SRC com/ichi2/anki/exception/StorageAccessException.java:6-7; com/ichi2/anki/CollectionHelper.java:172, 175, 183', 'SOURCE')

UNREACHABLE['ContextMenuHelper.<init>'] = ('no_trigger_in_app',
  'Implicit constructor (ContextMenuHelper.java:21). The class has only static methods, and no new ContextMenuHelper exists in com/ichi2/anki (grep).',
  'SRC com/ichi2/anki/dialogs/ContextMenuHelper.java:21', 'SOURCE')

UNREACHABLE['AnkiDroidCrashReportDialog.<init>'] = ('closed_by_configuration',
  'Implicit constructor (AnkiDroidCrashReportDialog.java:34). The class is started only by ACRA crash reporting (reportDialogClass, mode DIALOG, AnkiDroidApp.java:54-59). In a debug build AnkiDroidApp.onCreate calls setAcraReportingMode(NEVER) (AnkiDroidApp.java:155-159), which writes acra.disable=true (AnkiDroidApp.java:328-329). ACRA is a library not in the dataset and no ACRA source is cited, so confirmed_by is INFERRED: it does not start this dialog in the standard debug configuration. The release branch (AnkiDroidApp.java:164-168, default ASK) is outside the standard configuration and is not labeled here.',
  'SRC com/ichi2/anki/dialogs/AnkiDroidCrashReportDialog.java:34; com/ichi2/anki/AnkiDroidApp.java:54-59, 152, 155-159, 328-329', 'INFERRED')

UNREACHABLE['AnkiDroidCrashReportDialog.buildCustomView'] = ('closed_by_configuration',
  'Private (AnkiDroidCrashReportDialog.java:69-84), called from onCreate (line 54). Reached only through the crash-report route, which is closed in the debug build: AnkiDroidApp.java:155-159 sets ACRA to NEVER and acra.disable=true (AnkiDroidApp.java:328-329). ACRA is a library not in the dataset and no ACRA source is cited, so confirmed_by is INFERRED. The release branch (AnkiDroidApp.java:164-168) is not labeled here.',
  'SRC com/ichi2/anki/dialogs/AnkiDroidCrashReportDialog.java:54, 69-84; com/ichi2/anki/AnkiDroidApp.java:155-159, 328-329', 'INFERRED')

UNREACHABLE['AnkiDroidCrashReportDialog.onClick'] = ('closed_by_configuration',
  'Dialog button callback (AnkiDroidCrashReportDialog.java:86-105). The dialog is never shown in the standard debug configuration, because ACRA is set to NEVER (AnkiDroidApp.java:155-159, 328-329). ACRA is a library not in the dataset and no ACRA source is cited, so confirmed_by is INFERRED. The release branch (AnkiDroidApp.java:164-168) is not labeled here.',
  'SRC com/ichi2/anki/dialogs/AnkiDroidCrashReportDialog.java:86-105; com/ichi2/anki/AnkiDroidApp.java:155-159, 328-329', 'INFERRED')

UNREACHABLE['AnkiDroidCrashReportDialog.onCreate'] = ('closed_by_configuration',
  'Activity onCreate (AnkiDroidCrashReportDialog.java:41-62). The activity is never started in the standard debug configuration, because ACRA is set to NEVER (AnkiDroidApp.java:155-159, 328-329). ACRA is a library not in the dataset and no ACRA source is cited, so confirmed_by is INFERRED. The release branch (AnkiDroidApp.java:164-168) is not labeled here.',
  'SRC com/ichi2/anki/dialogs/AnkiDroidCrashReportDialog.java:41-62; com/ichi2/anki/AnkiDroidApp.java:155-159, 328-329', 'INFERRED')

UNREACHABLE['AnkiDroidCrashReportDialog.onDismiss'] = ('closed_by_configuration',
  'Dismiss callback (AnkiDroidCrashReportDialog.java:107-110). Reached only through the crash-report dialog, which is never started in the standard debug configuration because ACRA is set to NEVER (AnkiDroidApp.java:155-159, 328-329). ACRA is a library not in the dataset and no ACRA source is cited, so confirmed_by is INFERRED.',
  'SRC com/ichi2/anki/dialogs/AnkiDroidCrashReportDialog.java:107-110; com/ichi2/anki/AnkiDroidApp.java:155-159, 328-329', 'INFERRED')

UNREACHABLE['AnkiDroidCrashReportDialog.onSaveInstanceState'] = ('closed_by_configuration',
  'Activity callback (AnkiDroidCrashReportDialog.java:112-118). Reached only through the crash-report dialog, which is never started in the standard debug configuration because ACRA is set to NEVER (AnkiDroidApp.java:155-159, 328-329). ACRA is a library not in the dataset and no ACRA source is cited, so confirmed_by is INFERRED.',
  'SRC com/ichi2/anki/dialogs/AnkiDroidCrashReportDialog.java:112-118; com/ichi2/anki/AnkiDroidApp.java:155-159, 328-329', 'INFERRED')
