
UNREACHABLE['AddContentApi$CompatV1.insertNotes'] = ('closed_by_configuration',
  'Overridden by CompatV2.insertNotes (api/src/main/java/com/ichi2/anki/api/AddContentApi.java:695-699). getCompat (line 594) picks CompatV1 only when getApiHostSpecVersion() is below 2. The manifest declares provider spec 2 (AndroidManifest.xml:329), so CompatV2 is chosen on the installed configuration. The value -1 (lines 575-576) appears only when AnkiDroid is not installed, and then no provider call here can succeed. CompatV2 does not call super, so this body never runs on the installed configuration.',
  'SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:633-643, 594; AndroidManifest.xml:329',
  'SOURCE')

UNREACHABLE['AddContentApi$CompatV1.findDuplicateNotes'] = ('closed_by_configuration',
  'Overridden by CompatV2.findDuplicateNotes (api/src/main/java/com/ichi2/anki/api/AddContentApi.java:702-741). getCompat (line 594) picks CompatV1 only when getApiHostSpecVersion() is below 2. The manifest declares provider spec 2 (AndroidManifest.xml:329), so CompatV2 is chosen on the installed configuration. The value -1 (lines 575-576) appears only when AnkiDroid is not installed, and then no provider call here can succeed. CompatV2 does not call super, so this body never runs on the installed configuration.',
  'SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:645-671, 594; AndroidManifest.xml:329',
  'SOURCE')

UNREACHABLE['AddContentApi.hasReadWritePermission'] = ('closed_by_api_level',
  'The only caller is previewNewNote (api/src/main/java/com/ichi2/anki/api/AddContentApi.java:263). The guard SDK_INT < Build.VERSION_CODES.M && !hasReadWritePermission() short-circuits on API 27, where SDK_INT (27) is not below M (23), so the call never runs. minSdkVersion is 10 (AnkiDroid/build.gradle:12), so the call is reachable only on API 10 to 22.',
  'SRC api/src/main/java/com/ichi2/anki/api/AddContentApi.java:263, 585-588',
  'SOURCE')

# ---- sup for part 055
sup(('AddContentApi.addNotes', 'AddContentApi$CompatV1.insertNotes'))
sup(('AddContentApi.findDuplicateNotes(long,String)', 'AddContentApi$CompatV1.findDuplicateNotes'))
sup(('AddContentApi.findDuplicateNotes(long,List)', 'AddContentApi$CompatV1.findDuplicateNotes'))
sup(('AddContentApi.getNoteCount', 'AddContentApi$CompatV1.queryNotes'))
sup(('AddContentApi.previewNewNote', 'AddContentApi.hasReadWritePermission'))

# ---- part 054 (2026-10-28)
e('S_REVIEWER', 'Whiteboard.onDraw', 'FRAMEWORK', 'Review screen shows the whiteboard overlay and the view system draws it', env=None, needs_state=STATE_SETTINGS, evidence='SRC com/ichi2/anki/Whiteboard.java:98-103; SRC com/ichi2/anki/Reviewer.java:453-459, 476-483; FW-SRC fw_src/android-8.1.0_r1/core/java/android/view/View.java:19161-19192', note='Reviewer adds the whiteboard view (Reviewer.java:459) and shows it through setWhiteboardVisibility (476-483); View.draw calls onDraw (View.java:19192, 19308). Gate: whiteboard enabled for the deck (STATE_SETTINGS).')

UNREACHABLE['UIUtils.<init>'] = ('no_trigger_in_app', 'UIUtils declares no constructor, nothing instantiates or subclasses it, and all of its members are static', 'com/ichi2/anki/UIUtils.java:20', 'SOURCE')

UNREACHABLE['UIUtils$1.onCancelled'] = ('no_trigger_in_app', 'The SAVE_COLLECTION task is never cancelled: cancelTask(int) is only called with SEARCH_CARDS or RENDER_BROWSER_QA', 'com/ichi2/anki/UIUtils.java:134-135; com/ichi2/async/DeckTask.java:168-172, 181-184, 368-370; com/ichi2/anki/CardBrowser.java:528-529, 796-797, 1155', 'SOURCE')

UNREACHABLE['UIUtils$1.onProgressUpdate'] = ('no_trigger_in_app', 'Only the SAVE_COLLECTION task reaches this listener, and its body calls col.save() without publishProgress', 'com/ichi2/anki/UIUtils.java:129-130; com/ichi2/async/DeckTask.java:237-238, 352-355, 494-504', 'SOURCE')

# ---- sup for part 054
sup(('DeckTask.onCancelled', 'UIUtils$1.onCancelled'))
sup(('DeckTask$TaskListener.onProgressUpdate', 'UIUtils$1.onProgressUpdate'))
sup(('DeckTask$TaskListener.onProgressUpdate@UIUtils$1', 'UIUtils$1.onProgressUpdate'))

# ---- part 059 (2026-10-28)
# AnkiDroid batch 059 (LABEL helper). BasicImageFieldController (com/ichi2/anki/multimediacard/fields/BasicImageFieldController.java)
# with its click listeners $1 and $2: 15 methods, all REACHABLE (no UNREACHABLE entries). The full row list is in
# graphs/AnkiDroid/parts/label_059.md.
#
# Route ownership:
# - The automatic CALL edges (BasicControllerFactory -> <init>, createUI -> $1/$2 <init>, recreateEditingUi -> createUI,
#   onActivityResult -> rotateAndCompress and setPreviewImage, the activity -> controller calls) come from auto_calls.json.
#   They are not written here.
# - The page edges into the listeners ($1.onClick, $2.onClick) are written here, because the destination is in this batch.
# - The RESULT edges from the two listeners into MultimediaEditFieldActivity.onActivityResult are written here, because the
#   source (the listener that starts the activity) is in this batch.
#
# Gates: MG532 (picker app returns a result), MG533 (camera app returns a result). Predefined constant used: ENV_STORAGE
# (the camera temp file is written to the public Pictures folder). Page node: S_MULTIMEDIA_EDIT_FIELD.

# --- REGISTER: the listeners are set on the two buttons in createUI (BasicImageFieldController.java:98-110).
e('BasicImageFieldController$1.<init>', 'BasicImageFieldController$1.onClick', 'REGISTER',
  'the gallery click listener is set on mBtnGallery',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicImageFieldController.java:98-106',
  note='The builder does not follow REGISTER for reachability; the route is the S_MULTIMEDIA_EDIT_FIELD -> BasicImageFieldController$1.onClick edge below.')

e('BasicImageFieldController$2.<init>', 'BasicImageFieldController$2.onClick', 'REGISTER',
  'the camera click listener is set on mBtnCamera',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicImageFieldController.java:108-110',
  note='The builder does not follow REGISTER for reachability; the route is the S_MULTIMEDIA_EDIT_FIELD -> BasicImageFieldController$2.onClick edge below.')

# --- GUI: the user taps the buttons of the image field editor (page node).
e('S_MULTIMEDIA_EDIT_FIELD', 'BasicImageFieldController$1.onClick', 'GUI',
  'tap the gallery button under the image preview of the image field editor',
  env=None,
  gui=['tap the gallery button under the image preview of the image field editor'],
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicImageFieldController.java:98-106',
  note='Page edge; the destination is in this batch, so this part writes it. No state gate: the editor needs no data state. The page edges of the activity menu are in label_048.py.')

e('S_MULTIMEDIA_EDIT_FIELD', 'BasicImageFieldController$2.onClick', 'GUI',
  'tap the camera button under the gallery button of the image field editor (not on a Chromebook)',
  env=None,
  gui=['tap the camera button under the gallery button of the image field editor (not on a Chromebook)'],
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicImageFieldController.java:108-134',
  note='Page edge; the destination is in this batch. The button is hidden only on a Chromebook (BasicImageFieldController.java:131-134); the standard configuration is not one. No state gate.')

# --- RESULT: the listeners start an activity for a result; it returns to MultimediaEditFieldActivity.onActivityResult
#     (activity line 312-319), which forwards to the controller. The framework dispatch is FW-SRC Activity.java:7259-7266.
e('BasicImageFieldController$1.onClick', 'MultimediaEditFieldActivity.onActivityResult', 'RESULT',
  'the picker app returns the selected image (ACTION_PICK, request ACTIVITY_SELECT_IMAGE)',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicImageFieldController.java:103-104, 156-166; com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:312-319; FW-SRC core/java/android/app/Activity.java:7259-7266',
  note='MISSING GATE MG532: a picker app must be installed and return a result. No ENV or STATE kind covers another app returning a result. env and needs_state unset. The activity forwards the result to the controller (MultimediaEditFieldActivity.java:315).')

e('BasicImageFieldController$2.onClick', 'MultimediaEditFieldActivity.onActivityResult', 'RESULT',
  'the camera app returns after the photo is taken (ACTION_IMAGE_CAPTURE, request ACTIVITY_TAKE_PICTURE)',
  env=ENV_STORAGE,
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicImageFieldController.java:117-125, 158; com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:312-319; FW-SRC core/java/android/app/Activity.java:7259-7266',
  note='ENV_STORAGE: the temp file is created in the public Pictures folder (BasicImageFieldController.java:119-120); an IOException stops the launch (lines 126-128). MISSING GATE MG533: a camera app must be installed and return a result other than RESULT_CANCELED (line 158). No ENV or STATE kind covers another app returning a result, so that part is not set here. needs_state unset.')

# ---- part 056 (2026-10-28)
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

e('S_DLG_CONFIRMATION_DECKPICKER_FULLSYNC', 'DialogHandler$1.confirm', 'GUI',
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

# ---- sup for part 056
sup(('AnkiDroidCrashReportDialog.onCreate', 'AnkiDroidCrashReportDialog.buildCustomView'))

# ---- part 058 (2026-10-28)
# AnkiDroid batch 058 (LABEL helper). Audio field classes: AudioField (18 methods), BasicAudioFieldController
# (6 methods, plus its anonymous listener $1 with 2 methods), BasicControllerFactory (3 methods). 29 methods.
# The full row list is in graphs/AnkiDroid/parts/label_058.md.
#
# Route ownership:
# - Automatic CALL edges (factory to controller, activity to controller, note editor and NoteService to AudioField)
#   come from auto_calls.json. They are not written here.
# - The three GUI edges from the page S_MULTIMEDIA_EDIT_FIELD are owned by this part, because their destinations
#   (the listener and the controller methods) are in this batch.
#
# Gates: the recording and the audio controller need the RECORD_AUDIO permission (ENV_PERM_RECORD). No MG id is
# needed in this batch.
#
# UNREACHABLE entries are for AudioField methods (see label_058.md).

e('S_MULTIMEDIA_EDIT_FIELD', 'BasicAudioFieldController$1.onRecordingFinish', 'GUI',
  'tap the record button, then the stop button, in the audio field editor (the audio view stops the recorder and fires the listener)',
  env=ENV_PERM_RECORD,
  gui=['tap the record button, then the stop button, in the audio field editor (the audio view stops the recorder and fires the listener)'],
  evidence='SRC com/ichi2/anki/multimediacard/AudioView.java:192-205, 410-412; com/ichi2/anki/multimediacard/fields/BasicAudioFieldController.java:80-87',
  note='The stop button in RECORDING state calls AudioView.notifyStopRecord, which stops the recorder and calls the listener only when a recording is in progress. Recording starts only when RECORD_AUDIO is granted (ENV_PERM_RECORD). The listener sets the temporary audio path and the temporary flag on the field.')

e('S_MULTIMEDIA_EDIT_FIELD', 'BasicAudioFieldController.onDone', 'GUI',
  'tap the Done (save) menu item of the field editor while an audio field is shown',
  env=ENV_PERM_RECORD,
  gui=['tap the Done (save) menu item of the field editor while an audio field is shown'],
  evidence='SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:184-187, 242-244; com/ichi2/anki/multimediacard/fields/BasicAudioFieldController.java:92-95',
  note='The done route calls the controller onDone first. onDone dereferences the audio view, which exists only after createUI, so the route needs RECORD_AUDIO granted (ENV_PERM_RECORD). With the permission denied, onDone throws a NullPointerException (flagged in label_058.md).')

e('S_MULTIMEDIA_EDIT_FIELD', 'BasicAudioFieldController.onFocusLost', 'GUI',
  'tap the to-text or to-image menu item of the field editor while an audio field is shown',
  env=ENV_PERM_RECORD,
  gui=['tap the to-text or to-image menu item of the field editor while an audio field is shown'],
  evidence='SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:153, 155, 163-166, 170-173; com/ichi2/anki/multimediacard/fields/BasicAudioFieldController.java:101-104',
  note='The to-text and to-image items are visible for an audio field (menu lines 153 and 155). The activity calls onFocusLost before the type switch. onFocusLost dereferences the audio view, so the route needs RECORD_AUDIO granted (ENV_PERM_RECORD).')

UNREACHABLE['AudioField.getHtml'] = (
    'no_trigger_in_app',
    'Declared in the field interface only. Grep of the source root for getHtml( finds the declaration and the field overrides, and no caller. Body returns null.',
    'com/ichi2/anki/multimediacard/fields/IField.java:40; com/ichi2/anki/multimediacard/fields/AudioField.java:59-61',
    'SOURCE')

UNREACHABLE['AudioField.getImagePath'] = (
    'branch_never_taken',
    'All interface call sites are inside an IMAGE type branch that an AudioField never takes: the activity done (IMAGE test at line 250), NoteService.importMediaToDirectory (case IMAGE), and the image controller (built only for IMAGE by the factory). Body returns null.',
    'com/ichi2/anki/multimediacard/fields/AudioField.java:77-79; com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:250-251; com/ichi2/anki/servicelayer/NoteService.java:158-164; com/ichi2/anki/multimediacard/fields/BasicImageFieldController.java:91, 178; com/ichi2/anki/multimediacard/fields/BasicControllerFactory.java:41-42',
    'SOURCE')

UNREACHABLE['AudioField.getName'] = (
    'no_trigger_in_app',
    'No caller of the field interface getName in the source root. Grep finds only the declarations (interface, image, audio, text fields) and an unrelated view class. Name is set only on TextField objects. Body returns mName.',
    'com/ichi2/anki/multimediacard/fields/IField.java:81; com/ichi2/anki/multimediacard/fields/AudioField.java:121-123',
    'SOURCE')

UNREACHABLE['AudioField.getText'] = (
    'branch_never_taken',
    'Interface call sites in the text controller are guarded: the loop skips every field whose type is not TEXT before calling getText. The other calls are on the text controller own field, and the factory builds that controller only for TEXT. Body returns null.',
    'com/ichi2/anki/multimediacard/fields/AudioField.java:97-99; com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:218-241; com/ichi2/anki/multimediacard/fields/BasicControllerFactory.java:37-39',
    'SOURCE')

UNREACHABLE['AudioField.isModified'] = (
    'branch_never_taken',
    'The only caller is MultimediaEditableNote.setField, inside the same-object guard (getField(index) == field). Every setField caller passes a new object or a deserialized copy, so the guard is never true: the note editor result handler (fields from the intent extras), the popup items (new AudioField, ImageField or TextField), and NoteService.updateMultimediaNoteFromJsonNote (new field per loop). Body returns the modified flag. Judgment call, flagged to the orchestrator.',
    'com/ichi2/anki/multimediacard/fields/AudioField.java:53-55; com/ichi2/anki/multimediacard/impl/MultimediaEditableNote.java:104-113; com/ichi2/anki/NoteEditor.java:1036-1039, 1151-1171; com/ichi2/anki/servicelayer/NoteService.java:77-86',
    'SOURCE')

UNREACHABLE['AudioField.setHtml'] = (
    'no_trigger_in_app',
    'Declared in the field interface only. Grep of the source root finds no call. Body returns false.',
    'com/ichi2/anki/multimediacard/fields/IField.java:43; com/ichi2/anki/multimediacard/fields/AudioField.java:65-67',
    'SOURCE')

UNREACHABLE['AudioField.setImagePath'] = (
    'branch_never_taken',
    'Call sites are the image branch of NoteService.importMediaToDirectory (case IMAGE) and the image controller (built only for IMAGE by the factory). Neither gives an AudioField receiver. Body returns false.',
    'com/ichi2/anki/multimediacard/fields/AudioField.java:71-73; com/ichi2/anki/servicelayer/NoteService.java:181-186; com/ichi2/anki/multimediacard/fields/BasicImageFieldController.java:166-176; com/ichi2/anki/multimediacard/fields/BasicControllerFactory.java:41-42',
    'SOURCE')

UNREACHABLE['AudioField.setName'] = (
    'no_trigger_in_app',
    'The only setName call on a field in the source root is NoteService.createEmptyNote on a TextField local (uiTextField), so no call dispatches to AudioField. Body sets mName.',
    'com/ichi2/anki/multimediacard/fields/AudioField.java:126-129; com/ichi2/anki/servicelayer/NoteService.java:55-56',
    'SOURCE')

UNREACHABLE['AudioField.setText'] = (
    'branch_never_taken',
    'Interface call sites receive only TextField objects: the note editor text popup item (a new TextField), NoteService line 57 (TextField local), and the text controller onDone (TEXT-only controller, factory lines 37-39). Body returns false.',
    'com/ichi2/anki/multimediacard/fields/AudioField.java:103-105; com/ichi2/anki/NoteEditor.java:1167-1171; com/ichi2/anki/servicelayer/NoteService.java:55-57; com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:340-341; com/ichi2/anki/multimediacard/fields/BasicControllerFactory.java:37-39',
    'SOURCE')

UNREACHABLE['AudioField.setType'] = (
    'no_trigger_in_app',
    'Declared in the field interface only. Grep of the source root finds no call on a field (the only setType calls are on a card and an intent). Body returns false.',
    'com/ichi2/anki/multimediacard/fields/IField.java:33; com/ichi2/anki/multimediacard/fields/AudioField.java:47-49',
    'SOURCE')

# ---- sup for part 058
sup(('MultimediaEditFieldActivity.done', 'AudioField.getImagePath'))
sup(('BasicImageFieldController.createUI', 'AudioField.getImagePath'))
sup(('BasicImageFieldController.onActivityResult', 'AudioField.getImagePath'))
sup(('NoteService.importMediaToDirectory', 'AudioField.getImagePath'))
sup(('BasicTextFieldController.createUI', 'AudioField.getText'))
sup(('BasicTextFieldController.createCloneButton', 'AudioField.getText'))
sup(('MultimediaEditableNote.setField', 'AudioField.isModified'))
sup(('BasicImageFieldController.onActivityResult', 'AudioField.setImagePath'))
sup(('NoteService.importMediaToDirectory', 'AudioField.setImagePath'))
sup(('NoteEditor$11$1.onMenuItemClick', 'AudioField.setText'))
sup(('BasicTextFieldController.onDone', 'AudioField.setText'))

# ---- part 061 (2026-10-28)
# AnkiDroid batch 061 (LABEL helper). ImageField and TextField: 36 methods. Rows are in graphs/AnkiDroid/parts/label_061.md.
# No e() calls: every route into these methods is an automatic CALL edge from auto_calls.json.
# UNREACHABLE entries only. Each reason is inline (no module-level names).

UNREACHABLE['ImageField.getAudioPath'] = ('branch_never_taken', 'Returns null. Callers run only for AudioField receivers: MultimediaEditFieldActivity.done under getType()==AUDIO (lines 261-267), NoteService.importMediaToDirectory under case AUDIO (line 160), BasicAudioFieldController.createUI (line 52). ImageField.getType() is IMAGE, so the branch is never taken.', 'com/ichi2/anki/multimediacard/fields/ImageField.java:91-93; com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:261-267; com/ichi2/anki/servicelayer/NoteService.java:158-160; com/ichi2/anki/multimediacard/fields/BasicAudioFieldController.java:50-53; com/ichi2/anki/multimediacard/fields/BasicControllerFactory.java:44-45', 'SOURCE')
UNREACHABLE['ImageField.getHtml'] = ('no_trigger_in_app', 'No call site anywhere in the source root. grep for getHtml( finds only the declaration and the overrides. Nothing reads the HTML of a field.', 'com/ichi2/anki/multimediacard/fields/ImageField.java:59-61; com/ichi2/anki/multimediacard/fields/IField.java:40', 'SOURCE')
UNREACHABLE['ImageField.getName'] = ('no_trigger_in_app', 'No call site on an IField receiver. grep for getName( finds only the definition, the declaration and unrelated calls on File, AnkiFont and Models.', 'com/ichi2/anki/multimediacard/fields/ImageField.java:121-123; com/ichi2/anki/multimediacard/fields/IField.java:81', 'SOURCE')
UNREACHABLE['ImageField.getText'] = ('branch_never_taken', 'Returns null. Callers: BasicTextFieldController.createUI (line 73), where the text controller exists only for TEXT fields (BasicControllerFactory lines 38-39); and createCloneButton (line 241), guarded by getType()!=TEXT then continue (lines 223-225). An ImageField is never TEXT.', 'com/ichi2/anki/multimediacard/fields/ImageField.java:97-99; com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:70-74, 218-242; com/ichi2/anki/multimediacard/fields/BasicControllerFactory.java:38-39', 'SOURCE')
UNREACHABLE['ImageField.isModified'] = ('branch_never_taken', 'The only call is MultimediaEditableNote.setField line 108, which runs only when getField(index) == field (line 107). No setField caller passes a field already stored in the note: NoteEditor lines 1039, 1158, 1164, 1171 and NoteService lines 58, 86 all pass new objects. Judgment call for the orchestrator.', 'com/ichi2/anki/multimediacard/impl/MultimediaEditableNote.java:104-115; com/ichi2/anki/NoteEditor.java:1036-1039, 1157-1171; com/ichi2/anki/servicelayer/NoteService.java:50-58, 79-86; com/ichi2/anki/multimediacard/fields/ImageField.java:53-55', 'SOURCE')
UNREACHABLE['ImageField.setAudioPath'] = ('branch_never_taken', 'Returns false. Callers: NoteService.importMediaToDirectory line 183 (inside case AUDIO, which an ImageField never reaches because getType() is IMAGE), and BasicAudioFieldController.onRecordingFinish line 84 (AudioField receiver). BasicTextFieldController line 304 uses a separate AudioField.', 'com/ichi2/anki/multimediacard/fields/ImageField.java:85-87; com/ichi2/anki/servicelayer/NoteService.java:181-186; com/ichi2/anki/multimediacard/fields/BasicAudioFieldController.java:82-86; com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:303-304', 'SOURCE')
UNREACHABLE['ImageField.setHtml'] = ('no_trigger_in_app', 'No call site anywhere in the source root. grep for setHtml( finds only the declaration and the overrides.', 'com/ichi2/anki/multimediacard/fields/ImageField.java:65-67; com/ichi2/anki/multimediacard/fields/IField.java:43', 'SOURCE')
UNREACHABLE['ImageField.setName'] = ('no_trigger_in_app', 'No call site on an ImageField receiver. The only setName call on a field is NoteService line 56, on a TextField created at line 55.', 'com/ichi2/anki/multimediacard/fields/ImageField.java:127-129; com/ichi2/anki/servicelayer/NoteService.java:55-56; com/ichi2/anki/multimediacard/fields/IField.java:84', 'SOURCE')
UNREACHABLE['ImageField.setText'] = ('branch_never_taken', 'Returns false. Callers: NoteEditor popup menu (line 1170), where the object is a TextField created at line 1169; and BasicTextFieldController.onDone (line 341), where mField is a TextField from BasicControllerFactory (lines 38-39). The receivers are always TextField.', 'com/ichi2/anki/multimediacard/fields/ImageField.java:103-105; com/ichi2/anki/NoteEditor.java:1167-1172; com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:338-342; com/ichi2/anki/multimediacard/fields/BasicControllerFactory.java:38-39', 'SOURCE')
UNREACHABLE['ImageField.setType'] = ('no_trigger_in_app', 'No call site anywhere in the source root. grep for setType( finds only the declarations and the overrides, plus unrelated Intent, Card and Sched calls.', 'com/ichi2/anki/multimediacard/fields/ImageField.java:47-49; com/ichi2/anki/multimediacard/fields/IField.java:33', 'SOURCE')
UNREACHABLE['TextField.getAudioPath'] = ('branch_never_taken', 'Returns null. Callers are the same as for ImageField.getAudioPath: MultimediaEditFieldActivity.done (lines 261-267, AUDIO branch), NoteService.importMediaToDirectory (lines 158-160, case AUDIO), and BasicAudioFieldController.createUI (line 52, AudioField receiver). A TextField getType() is TEXT, so none reaches it.', 'com/ichi2/anki/multimediacard/fields/TextField.java:82-84; com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:261-267; com/ichi2/anki/servicelayer/NoteService.java:158-160; com/ichi2/anki/multimediacard/fields/BasicAudioFieldController.java:50-53', 'SOURCE')
UNREACHABLE['TextField.getHtml'] = ('no_trigger_in_app', 'No call site anywhere in the source root. grep for getHtml( finds only the declaration and the overrides.', 'com/ichi2/anki/multimediacard/fields/TextField.java:52-54; com/ichi2/anki/multimediacard/fields/IField.java:40', 'SOURCE')
UNREACHABLE['TextField.getImagePath'] = ('branch_never_taken', 'Returns null. Callers: MultimediaEditFieldActivity.done (line 256) under getType()==IMAGE (lines 250-251); BasicImageFieldController.createUI (line 91) and onActivityResult (line 178), whose receiver is always an ImageField from BasicControllerFactory (lines 41-42); and NoteService.importMediaToDirectory (case IMAGE, line 164). A TextField never reaches any of them.', 'com/ichi2/anki/multimediacard/fields/TextField.java:70-72; com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:250-256; com/ichi2/anki/multimediacard/fields/BasicImageFieldController.java:91, 170-179; com/ichi2/anki/servicelayer/NoteService.java:163-164', 'SOURCE')
UNREACHABLE['TextField.getName'] = ('no_trigger_in_app', 'No call site on an IField receiver. grep for getName( finds only the definition, the declaration and unrelated calls.', 'com/ichi2/anki/multimediacard/fields/TextField.java:114-116; com/ichi2/anki/multimediacard/fields/IField.java:81', 'SOURCE')
UNREACHABLE['TextField.hasTemporaryMedia'] = ('branch_never_taken', 'Returns false. The only call is NoteService.importMediaToDirectory line 177 (cha CALL), inside if (tmpMediaPath != null) (line 171). tmpMediaPath stays null for TEXT: it starts null (line 157) and the TEXT case breaks without assigning it (lines 167-169). So the call never runs for a TextField.', 'com/ichi2/anki/servicelayer/NoteService.java:157-177; com/ichi2/anki/multimediacard/fields/TextField.java:106-110', 'SOURCE')
UNREACHABLE['TextField.isModified'] = ('branch_never_taken', 'The only call is MultimediaEditableNote.setField line 108, which runs only when getField(index) == field (line 107). No setField caller passes a field already stored in the note (see ImageField.isModified). Judgment call for the orchestrator.', 'com/ichi2/anki/multimediacard/impl/MultimediaEditableNote.java:104-115; com/ichi2/anki/NoteEditor.java:1036-1039, 1157-1171; com/ichi2/anki/servicelayer/NoteService.java:50-58, 79-86; com/ichi2/anki/multimediacard/fields/TextField.java:46-48', 'SOURCE')
UNREACHABLE['TextField.setAudioPath'] = ('branch_never_taken', 'Returns false. Callers: NoteService.importMediaToDirectory line 183 (case AUDIO, inside the tmpMediaPath block that a TEXT field never enters, line 171), and BasicAudioFieldController.onRecordingFinish line 84 (AudioField receiver). BasicTextFieldController line 304 sets the path on a separate AudioField.', 'com/ichi2/anki/multimediacard/fields/TextField.java:76-78; com/ichi2/anki/servicelayer/NoteService.java:171, 181-186; com/ichi2/anki/multimediacard/fields/BasicAudioFieldController.java:82-86; com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:303-304', 'SOURCE')
UNREACHABLE['TextField.setHasTemporaryMedia'] = ('branch_never_taken', 'The body is empty. Callers: BasicImageFieldController.onActivityResult line 176 (receiver is an ImageField from BasicControllerFactory lines 41-42) and BasicAudioFieldController.onRecordingFinish line 85 (receiver is an AudioField). BasicTextFieldController line 306 calls it on an AudioField. None passes a TextField.', 'com/ichi2/anki/multimediacard/fields/TextField.java:102-103; com/ichi2/anki/multimediacard/fields/BasicImageFieldController.java:170-179; com/ichi2/anki/multimediacard/fields/BasicAudioFieldController.java:82-86; com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:303-306', 'SOURCE')
UNREACHABLE['TextField.setHtml'] = ('no_trigger_in_app', 'No call site anywhere in the source root. grep for setHtml( finds only the declaration and the overrides.', 'com/ichi2/anki/multimediacard/fields/TextField.java:58-60; com/ichi2/anki/multimediacard/fields/IField.java:43', 'SOURCE')
UNREACHABLE['TextField.setImagePath'] = ('branch_never_taken', 'Returns false. Callers: BasicImageFieldController.onActivityResult lines 172 and 175 (receiver is always an ImageField from BasicControllerFactory lines 41-42), and NoteService.importMediaToDirectory line 186 (case IMAGE, inside the tmpMediaPath block that a TEXT field never enters, line 171).', 'com/ichi2/anki/multimediacard/fields/TextField.java:64-66; com/ichi2/anki/multimediacard/fields/BasicImageFieldController.java:170-179; com/ichi2/anki/servicelayer/NoteService.java:171, 181-186', 'SOURCE')
UNREACHABLE['TextField.setType'] = ('no_trigger_in_app', 'No call site anywhere in the source root. grep for setType( finds only the declarations and the overrides, plus unrelated Intent, Card and Sched calls.', 'com/ichi2/anki/multimediacard/fields/TextField.java:40-42; com/ichi2/anki/multimediacard/fields/IField.java:33', 'SOURCE')

# ---- sup for part 061
sup(('NoteEditor$11$1.onMenuItemClick', 'ImageField.setText'))
sup(('MultimediaEditableNote.setField', 'TextField.isModified'))
sup(('MultimediaEditableNote.setField', 'ImageField.isModified'))
sup(('MultimediaEditFieldActivity.done', 'TextField.getAudioPath'))
sup(('MultimediaEditFieldActivity.done', 'ImageField.getAudioPath'))
sup(('MultimediaEditFieldActivity.done', 'TextField.getImagePath'))
sup(('BasicTextFieldController.createUI', 'ImageField.getText'))
sup(('BasicTextFieldController.createCloneButton', 'ImageField.getText'))
sup(('BasicTextFieldController.onDone', 'ImageField.setText'))
sup(('BasicImageFieldController.createUI', 'TextField.getImagePath'))
sup(('BasicImageFieldController.onActivityResult', 'TextField.getImagePath'))
sup(('BasicImageFieldController.onActivityResult', 'TextField.setHasTemporaryMedia'))
sup(('BasicImageFieldController.onActivityResult', 'TextField.setImagePath'))
sup(('BasicAudioFieldController$1.onRecordingFinish', 'TextField.setHasTemporaryMedia'))
sup(('BasicAudioFieldController$1.onRecordingFinish', 'TextField.setAudioPath'))
sup(('BasicAudioFieldController$1.onRecordingFinish', 'ImageField.setAudioPath'))
sup(('BasicAudioFieldController.createUI', 'TextField.getAudioPath'))
sup(('BasicAudioFieldController.createUI', 'ImageField.getAudioPath'))
sup(('NoteService.importMediaToDirectory', 'TextField.setImagePath'))
sup(('NoteService.importMediaToDirectory', 'TextField.setAudioPath'))
sup(('NoteService.importMediaToDirectory', 'ImageField.setAudioPath'))
sup(('NoteService.importMediaToDirectory', 'TextField.hasTemporaryMedia'))
sup(('NoteService.importMediaToDirectory', 'TextField.getImagePath'))
sup(('NoteService.importMediaToDirectory', 'TextField.getAudioPath'))
sup(('NoteService.importMediaToDirectory', 'ImageField.getAudioPath'))

# ---- part 062 (2026-10-28)
UNREACHABLE['Meaning.setLanguage'] = ('no_trigger_in_app', 'No call site in the source root: setLanguage( calls outside glosbe/json are TTS and AnkiDroidApp methods. Meaning objects are built only by Gson (library, not in dataset: INFERRED); TranslationActivity reads them with getters only.', 'com/ichi2/anki/multimediacard/glosbe/json/Meaning.java:35-37; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:323-333', 'SOURCE')
UNREACHABLE['Meaning.setText'] = ('no_trigger_in_app', 'No call site: the setText( calls at TranslationActivity.java:116, 120, 133 and 152 are on TextView and Button objects (tv, tvFrom, tvTo, btnDone), not on Meaning. Meaning objects are built only by Gson (library: INFERRED).', 'com/ichi2/anki/multimediacard/glosbe/json/Meaning.java:45-47; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:116, 120, 133, 152', 'SOURCE')
UNREACHABLE['Phrase.setLanguage'] = ('no_trigger_in_app', 'No call site in the source root: setLanguage( calls outside glosbe/json are TTS and AnkiDroidApp methods. Phrase objects are built only by Gson (library: INFERRED); TranslationActivity reads them with getters only (lines 339-345).', 'com/ichi2/anki/multimediacard/glosbe/json/Phrase.java:35-37; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:339-345', 'SOURCE')
UNREACHABLE['Phrase.setText'] = ('no_trigger_in_app', 'No call site: the setText( calls at TranslationActivity.java:116, 120, 133 and 152 are on TextView and Button objects, not on Phrase. Phrase objects are built only by Gson (library: INFERRED).', 'com/ichi2/anki/multimediacard/glosbe/json/Phrase.java:45-47; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:116, 120, 133, 152', 'SOURCE')
UNREACHABLE['Response.getDest'] = ('no_trigger_in_app', 'No call site: grep for getDest() finds no caller in the source root outside glosbe/json. Response is built only by Gson (library: INFERRED) at TranslationActivity.java:264.', 'com/ichi2/anki/multimediacard/glosbe/json/Response.java:36-38; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:264', 'SOURCE')
UNREACHABLE['Response.getFrom'] = ('no_trigger_in_app', 'No call site: grep for getFrom() finds no caller in the source root outside glosbe/json. Response is built only by Gson (library: INFERRED) at TranslationActivity.java:264.', 'com/ichi2/anki/multimediacard/glosbe/json/Response.java:46-48; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:264', 'SOURCE')
UNREACHABLE['Response.getPhrase'] = ('no_trigger_in_app', 'No call site: the only getPhrase() call in the source root is tuc.getPhrase() at TranslationActivity.java:339, which is Tuc.getPhrase. Response.getPhrase returns String and nothing calls it.', 'com/ichi2/anki/multimediacard/glosbe/json/Response.java:56-58; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:339', 'SOURCE')
UNREACHABLE['Response.setDest'] = ('no_trigger_in_app', 'No call site: grep for setDest( finds no caller in the source root outside glosbe/json. Response is built only by Gson (library: INFERRED) at TranslationActivity.java:264.', 'com/ichi2/anki/multimediacard/glosbe/json/Response.java:41-43; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:264', 'SOURCE')
UNREACHABLE['Response.setFrom'] = ('no_trigger_in_app', 'No call site: grep for setFrom( finds no caller in the source root outside glosbe/json. Response is built only by Gson (library: INFERRED) at TranslationActivity.java:264.', 'com/ichi2/anki/multimediacard/glosbe/json/Response.java:51-53; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:264', 'SOURCE')
UNREACHABLE['Response.setPhrase'] = ('no_trigger_in_app', 'No call site: grep for setPhrase( finds no caller in the source root outside glosbe/json. Response is built only by Gson (library: INFERRED) at TranslationActivity.java:264.', 'com/ichi2/anki/multimediacard/glosbe/json/Response.java:61-63; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:264', 'SOURCE')
UNREACHABLE['Response.setResult'] = ('no_trigger_in_app', 'No call site: the setResult( calls in the source root (for example AbstractFlashcardViewer.java:2600 and MyAccount.java:251) are Activity.setResult, not this method. Response is built only by Gson (library: INFERRED).', 'com/ichi2/anki/multimediacard/glosbe/json/Response.java:71-73; com/ichi2/anki/AbstractFlashcardViewer.java:2600; com/ichi2/anki/MyAccount.java:251', 'SOURCE')
UNREACHABLE['Response.setTuc'] = ('no_trigger_in_app', 'No call site: grep for setTuc( finds no caller in the source root outside glosbe/json. Response is built only by Gson (library: INFERRED) at TranslationActivity.java:264.', 'com/ichi2/anki/multimediacard/glosbe/json/Response.java:81-83; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:264', 'SOURCE')
UNREACHABLE['Tuc.getAuthors'] = ('no_trigger_in_app', 'No call site: grep for getAuthors() finds no caller in the source root outside glosbe/json. Tuc objects are built only by Gson (library: INFERRED) and read at TranslationActivity.java:311-323.', 'com/ichi2/anki/multimediacard/glosbe/json/Tuc.java:34-36; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:311, 323', 'SOURCE')
UNREACHABLE['Tuc.getMeaningId'] = ('no_trigger_in_app', 'No call site: grep for getMeaningId() finds no caller in the source root outside glosbe/json. Tuc objects are built only by Gson (library: INFERRED).', 'com/ichi2/anki/multimediacard/glosbe/json/Tuc.java:44-46; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:311', 'SOURCE')
UNREACHABLE['Tuc.setAuthors'] = ('no_trigger_in_app', 'No call site: grep for setAuthors( finds no caller in the source root outside glosbe/json. Tuc objects are built only by Gson (library: INFERRED).', 'com/ichi2/anki/multimediacard/glosbe/json/Tuc.java:39-41; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:323', 'SOURCE')
UNREACHABLE['Tuc.setMeaningId'] = ('no_trigger_in_app', 'No call site: grep for setMeaningId( finds no caller in the source root outside glosbe/json. Tuc objects are built only by Gson (library: INFERRED).', 'com/ichi2/anki/multimediacard/glosbe/json/Tuc.java:49-51; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:311', 'SOURCE')
UNREACHABLE['Tuc.setMeanings'] = ('no_trigger_in_app', 'No call site: grep for setMeanings( finds no caller in the source root outside glosbe/json. TranslationActivity reads tuc.getMeanings() at line 323 only.', 'com/ichi2/anki/multimediacard/glosbe/json/Tuc.java:59-61; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:323', 'SOURCE')
UNREACHABLE['Tuc.setPhrase'] = ('no_trigger_in_app', 'No call site: grep for setPhrase( finds no caller in the source root outside glosbe/json. TranslationActivity reads tuc.getPhrase() at line 339 only.', 'com/ichi2/anki/multimediacard/glosbe/json/Tuc.java:69-71; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:339', 'SOURCE')

# ---- addendum for part 062 (orchestrator, 2026-10-28): Gson reflection at the fromJson call in showPickTranslationDialog (batch 049 method); batch 062 did not write these edges
e('TranslationActivity.showPickTranslationDialog', 'Response.<init>', 'CALL',
  'parse the Glosbe reply: Gson creates the root Response object (TranslationActivity.java:264)',
  env=None,
  cls='non_standard',
  via='com.google.gson.Gson.fromJson (library, not in the dataset)',
  evidence='INFERRED Gson reflection at TranslationActivity.java:264 (library source not read); SRC com/ichi2/anki/multimediacard/glosbe/json/Response.java:28',
  note='Implicit constructor of a Gson target class. The FAILED check at line 258 returns first, so the route exists only when the reply is not FAILED.')
e('TranslationActivity.showPickTranslationDialog', 'Tuc.<init>', 'CALL',
  'parse the Glosbe reply: Gson creates each Tuc in Response.tuc (TranslationActivity.java:264)',
  env=None,
  cls='non_standard',
  via='com.google.gson.Gson.fromJson (library, not in the dataset)',
  evidence='INFERRED Gson reflection at TranslationActivity.java:264 (library source not read); SRC com/ichi2/anki/multimediacard/glosbe/json/Tuc.java:30-31',
  note='Implicit constructor of a Gson target class, reached through Response.tuc. Same FAILED-check gate as Response.<init>.')
e('TranslationActivity.showPickTranslationDialog', 'Meaning.<init>', 'CALL',
  'parse the Glosbe reply: Gson creates each Meaning in Tuc.meanings (TranslationActivity.java:264)',
  env=None,
  cls='non_standard',
  via='com.google.gson.Gson.fromJson (library, not in the dataset)',
  evidence='INFERRED Gson reflection at TranslationActivity.java:264 (library source not read); SRC com/ichi2/anki/multimediacard/glosbe/json/Tuc.java:30',
  note='Implicit constructor of a Gson target class, reached through Tuc.meanings. Same FAILED-check gate as Response.<init>.')
e('TranslationActivity.showPickTranslationDialog', 'Phrase.<init>', 'CALL',
  'parse the Glosbe reply: Gson creates the Phrase of each Tuc (TranslationActivity.java:264)',
  env=None,
  cls='non_standard',
  via='com.google.gson.Gson.fromJson (library, not in the dataset)',
  evidence='INFERRED Gson reflection at TranslationActivity.java:264 (library source not read); SRC com/ichi2/anki/multimediacard/glosbe/json/Tuc.java:31',
  note='Implicit constructor of a Gson target class, reached through Tuc.phrase. Same FAILED-check gate as Response.<init>.')

# ---- part 060 (2026-10-28)
# AnkiDroid batch 060 (LABEL helper). BasicTextFieldController (text editor of the multimedia field editor) and its
# listeners $1-$4, $3$1, the pick-dialog callback, the translation starters, plus FieldBase and FieldControllerBase.
# The full row list is in graphs/AnkiDroid/parts/label_060.md.
#
# Route ownership:
# - Automatic CALL edges (createUI -> createClearButton and the other create* methods, startTranslation* calls from the
#   dialog listeners, MultimediaEditFieldActivity -> FieldControllerBase setters, onDone, EFieldType.<clinit>) come from
#   auto_calls.json. They are not written here.
# - Edges written here: page edges from S_MULTIMEDIA_EDIT_FIELD and S_DLG_PICK_STRING into the listeners of this batch,
#   the INTENT edges from the say and translate paths, the ENTERS edges into the pick dialog, and the RESULT edge from the
#   ColorDict path (the source is in this batch).
#
# Gates: MG542 (clone button), MG543 (ColorDict installed). No predefined ENV_* or STATE_* constant fits, so env and
# needs_state are unset on the gated edges. Predefined constants used in this part: none.

# --- Text editor buttons (the page S_MULTIMEDIA_EDIT_FIELD is the text editor screen).
e('S_MULTIMEDIA_EDIT_FIELD', 'BasicTextFieldController$1.onClick', 'GUI',
  'tap the clear button under the text box (built by createUI on every text editor)',
  env=None,
  gui=['tap the clear button under the text box (built by createUI on every text editor)'],
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:83, 103-116; SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:98, 116-146',
  note='createClearButton is called from createUI (line 83) with no condition. The listener sets the text box to an empty string (line 112).')

e('S_MULTIMEDIA_EDIT_FIELD', 'BasicTextFieldController$2.onClick', 'GUI',
  'tap the say button (pronounce; built by createUI on every text editor)',
  env=None,
  needs_state=STATE_FIELD_TEXT,
  gui=['tap the say button (pronounce; built by createUI on every text editor)'],
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:93, 123-140',
  note='createPronounceButton is called from createUI (line 93) with no condition. Empty text shows a toast and returns (lines 131-134). Text starts LoadPronounciationActivity (edge below).')

e('BasicTextFieldController$2.onClick', 'LoadPronounciationActivity.<init>', 'INTENT',
  'the say button starts the pronunciation screen with the field text (non-empty text)',
  env=None,
  guard='source text non-empty',
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:136-138',
  note='Explicit intent to LoadPronounciationActivity with EXTRA_SOURCE, started with startActivityForResult. The network check is inside the child screen (page S_LOAD_PRONOUNCIATION, another batch), so no gate is set here. The RESULT edge S_LOAD_PRONOUNCIATION -> MultimediaEditFieldActivity.onActivityResult is already in graph_def.py.')

e('S_MULTIMEDIA_EDIT_FIELD', 'BasicTextFieldController$3.onClick', 'GUI',
  'tap the translate button (built by createUI on every text editor)',
  env=None,
  gui=['tap the translate button (built by createUI on every text editor)'],
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:92, 147-150',
  note='createTranslateButton is called from createUI (line 92) with no condition. Empty text shows a toast and returns (lines 156-159). Text with a space shows a warning toast and the flow goes on (lines 161-163).')

e('BasicTextFieldController$3.onClick', 'S_DLG_PICK_STRING', 'ENTERS',
  'non-empty text opens the translation source picker (Glosbe.com, and ColorDict unless a Chromebook)',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:166, 168-173, 191; SRC com/ichi2/anki/multimediacard/activity/PickStringDialogFragment.java:49',
  note='The picker is PickStringDialogFragment (page S_DLG_PICK_STRING), shown with the tag pick.translation.source (line 191). The ColorDict choice is listed only when CompatHelper.isChromebook() is false (lines 75-77).')

e('S_DLG_PICK_STRING', 'BasicTextFieldController$3$1.onClick', 'GUI',
  'pick a translation source in the picker (Glosbe.com or ColorDict)',
  env=None,
  gui=['pick a translation source in the picker (Glosbe.com or ColorDict)'],
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:176-187; SRC com/ichi2/anki/multimediacard/activity/PickStringDialogFragment.java:49',
  note='The anonymous listener $3$1 (line 176) calls startTranslationWithGlosbe (line 182) or startTranslationWithColorDict (line 184). Those two calls are automatic CALL edges and are not written here.')

e('BasicTextFieldController.startTranslationWithGlosbe', 'TranslationActivity.<init>', 'INTENT',
  'Glosbe.com chosen in the translation source picker: explicit intent to TranslationActivity with the field text, started for a result',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:393-398',
  note='Explicit component (TranslationActivity.class). The network check is in the child (TranslationActivity.translate, page S_TRANSLATION, another batch), so no gate is set here. The RESULT edge S_TRANSLATION -> MultimediaEditFieldActivity.onActivityResult is already in graph_def.py.')

e('BasicTextFieldController.startTranslationWithColorDict', 'MultimediaEditFieldActivity.onActivityResult', 'RESULT',
  'ColorDict chosen and installed: the external picker returns to the editor, which forwards the result to the field controller',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:364-390; SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:313-315',
  note='MISSING GATE MG543: ColorDict (an external app with no page node) must be installed. The check is isIntentAvailable (line 385); without the app the toast at line 386 shows and the method returns. No predefined ENV covers an app that AnkiDroid starts (ENV_OTHER_APP_INTENT is for apps that send intents to AnkiDroid). The Chromebook check (lines 75-77) also hides this choice. env and needs_state unset. The request code is REQUEST_CODE_TRANSLATE_COLORDICT (line 389).')

# --- Clone button (exists only when the note has another non-empty text field).
e('S_MULTIMEDIA_EDIT_FIELD', 'BasicTextFieldController$4.onClick', 'GUI',
  'tap the clone button (only when the note has another non-empty text field)',
  env=None,
  gui=['tap the clone button (only when the note has another non-empty text field)'],
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:82, 207-209, 246-256',
  note='MISSING GATE MG542: the clone button is built only when the note has more than one field (line 209) and at least one other non-empty TEXT field that is not this one (lines 216-243; return at 246-248). No predefined STATE or ENV fits (STATE_NOTE only says a note exists). env and needs_state unset. createCloneButton is called from createUI (line 82).')

e('BasicTextFieldController$4.onClick', 'S_DLG_PICK_STRING', 'ENTERS',
  'the clone source picker opens with the other non-empty text fields',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:256-266; SRC com/ichi2/anki/multimediacard/activity/PickStringDialogFragment.java:49',
  note='MISSING GATE MG542 (inherited: the button exists only then). The choices are mPossibleClones (line 262), the listener is the controller (line 263), and the picker is shown with the tag pick.clone (line 266). env and needs_state unset.')

e('S_DLG_PICK_STRING', 'BasicTextFieldController.onClick', 'GUI',
  'pick a clone source: the field text is replaced with the chosen text',
  env=None,
  gui=['pick a clone source: the field text is replaced with the chosen text'],
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:263, 345-349; SRC com/ichi2/anki/multimediacard/activity/PickStringDialogFragment.java:49',
  note='MISSING GATE MG542 (inherited from the clone button). The controller is the listener (line 263). onClick sets the text box to mPossibleClones[which] (line 348). env and needs_state unset.')

# --- UNREACHABLE: the identity guard in MultimediaEditableNote.setField is never true for a field the app passes in.
UNREACHABLE['FieldBase.getThisModified'] = (
    'branch_never_taken',
    'Only callers are the isModified methods of TextField, ImageField and AudioField. The one app call of isModified on a field is '
    'MultimediaEditableNote.setField line 108, which runs only inside the branch where the field passed in is the same object as the '
    'one already stored (line 107). Every app call of setField passes a newly created field or a field from the activity result '
    'extras (NoteEditor lines 1036-1039, NoteService lines 79-86, NoteFactory lines 19-33, NoteEditor lines 1157-1171). '
    'So the identity never holds, line 108 never runs, and getThisModified is never called.',
    'com/ichi2/anki/multimediacard/fields/FieldBase.java:36-38; com/ichi2/anki/multimediacard/fields/TextField.java:46-48; '
    'com/ichi2/anki/multimediacard/fields/ImageField.java:53-55; com/ichi2/anki/multimediacard/fields/AudioField.java:53-55; '
    'com/ichi2/anki/multimediacard/impl/MultimediaEditableNote.java:104-113; com/ichi2/anki/NoteEditor.java:1034-1039, 1157-1158, '
    '1163-1164, 1169-1171; com/ichi2/anki/servicelayer/NoteService.java:79-86; com/ichi2/anki/multimediacard/impl/NoteFactory.java:19-33',
    'SOURCE')

# ---- sup for part 060
sup(('TextField.isModified', 'FieldBase.getThisModified'))
sup(('ImageField.isModified', 'FieldBase.getThisModified'))
sup(('AudioField.isModified', 'FieldBase.getThisModified'))

# ---- part 063 (2026-10-28)
# AnkiDroid batch 063 (LABEL helper). 34 methods: MultimediaEditableNote (11), NoteFactory (2), LanguageListerBase with $1 (6),
# LanguageListerBeolingus (1), LanguagesLister with $1 (5), LanguagesListerGlosbe (3), MockNoteFactory (2),
# MockPronounciationPageFetcher (2), MockTranslationFetcher (2). The full row list is in graphs/AnkiDroid/parts/label_063.md.
#
# Route ownership: the automatic CALL edges (auto_calls.json) into and out of these methods are not written here.
# Edges written here: the two Collections.sort -> Comparator.compare edges, whose source method is in this batch.
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

# ---- sup for part 063
sup(('NoteService.updateJsonNoteFromMultimediaNote', 'MultimediaEditableNote.getModelId'))
sup(('LanguagesLister.getLanguages', 'LanguagesLister$1.<init>'))


# ---- part 064 (2026-10-28)
# AnkiDroid batch 064 (LABEL helper). 18 methods; the full row list is in graphs/AnkiDroid/parts/label_064.md.
# Three UNREACHABLE entries and no e() calls. The other 15 methods are REACHABLE through automatic CALL edges (see the .md).
# Every string is written inline; no module-level names.

UNREACHABLE['TaskOperations.<init>'] = ('no_trigger_in_app', 'TaskOperations has only static methods and no explicit constructor. A grep for "new TaskOperations" over the app source root finds no instance creation; every use is a static call to stopTaskGracefully. No route creates an instance.', 'SRC com/ichi2/anki/runtimetools/TaskOperations.java:25-38; SRC com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:474-478; SRC com/ichi2/anki/multimediacard/activity/TranslationActivity.java:405', 'SOURCE')

UNREACHABLE['NoteService.<init>'] = ('no_trigger_in_app', 'NoteService has only static methods and no explicit constructor. A grep for "new NoteService" over the app source root finds nothing; every use is a static call in NoteEditor.', 'SRC com/ichi2/anki/servicelayer/NoteService.java:38-45; SRC com/ichi2/anki/NoteEditor.java:1037-1038; SRC com/ichi2/anki/NoteEditor.java:1055; SRC com/ichi2/anki/NoteEditor.java:1138-1139; SRC com/ichi2/anki/NoteEditor.java:1151-1152', 'SOURCE')

UNREACHABLE['NoteService.updateJsonNoteFromMultimediaNote'] = ('no_trigger_in_app', 'Public static method with no caller. A grep for the name over the app source root finds only its definition, so the reverse copy (multimedia note into the editor note) is never called.', 'SRC com/ichi2/anki/servicelayer/NoteService.java:101-113', 'SOURCE')

# ---- part 065 (2026-10-28)
# AnkiDroid batch 065 (LABEL helper). AnkiStatsTaskHandler (with its nested tasks CreateChartTask,
# CreateStatisticsOverview and DeckPreviewStatistics) and ChartBuilder: 35 methods. The full row list is in
# graphs/AnkiDroid/parts/label_065.md.
#
# Route ownership:
# - CALL edges (constructors, accessors, createChart, createStatisticsOverview, createReviewSummaryStatistics,
#   renderChart and its setup and tick methods, the <clinit> pseudo-edges) come from auto_calls.json. Not written here.
# - The ASYNC edges below have their source in this batch: the start of each AsyncTask (execute in the three
#   create methods, into the doInBackground of the task) and the hand-back from doInBackground to onPostExecute.
# - The cancel(true) edges into the onCancelled methods come from Statistics.java (Statistics batch). Not written here.
# - No gate is needed: the task edges carry no environment or state.
#
# Gates: none (no MG id used in this batch).

e('AnkiStatsTaskHandler.createChart', 'AnkiStatsTaskHandler$CreateChartTask.doInBackground', 'ASYNC',
  'execute() on a chart task runs doInBackground on the AsyncTask worker thread',
  env=None,
  evidence='SRC com/ichi2/anki/stats/AnkiStatsTaskHandler.java:65-69; FW-SRC core/java/android/os/AsyncTask.java:594-595, 632-654',
  note='execute calls executeOnExecutor, which runs onPreExecute on the caller thread (AsyncTask.java:648), then exec.execute(mFuture) (AsyncTask.java:651). The FutureTask (AsyncTask.java:345-359) runs the worker. CreateChartTask does not override onPreExecute.')

e('AnkiStatsTaskHandler$CreateChartTask.doInBackground', 'AnkiStatsTaskHandler$CreateChartTask.onPostExecute', 'ASYNC',
  'the chart result returns to the UI thread, where the chart is shown',
  env=None,
  evidence='SRC com/ichi2/anki/stats/AnkiStatsTaskHandler.java:94-114, 121-129; FW-SRC core/java/android/os/AsyncTask.java:369-375, 691-696, 700-713',
  note='doInBackground returns the PlotSheet. postResult sends a message to the UI thread handler (AsyncTask.java:369-375). InternalHandler calls finish (AsyncTask.java:712), and finish calls onPostExecute when the task was not cancelled (AsyncTask.java:691-695). The dispatch is the framework handler route.')

e('AnkiStatsTaskHandler.createStatisticsOverview', 'AnkiStatsTaskHandler$CreateStatisticsOverview.doInBackground', 'ASYNC',
  'execute() on the overview task runs doInBackground on the AsyncTask worker thread',
  env=None,
  evidence='SRC com/ichi2/anki/stats/AnkiStatsTaskHandler.java:70-74; FW-SRC core/java/android/os/AsyncTask.java:594-595, 632-654',
  note='Same dispatch as the chart task: executeOnExecutor runs onPreExecute on the caller thread (AsyncTask.java:648), then exec.execute(mFuture) (AsyncTask.java:651). CreateStatisticsOverview does not override onPreExecute.')

e('AnkiStatsTaskHandler$CreateStatisticsOverview.doInBackground', 'AnkiStatsTaskHandler$CreateStatisticsOverview.onPostExecute', 'ASYNC',
  'the overview HTML returns to the UI thread, where it is loaded into the WebView',
  env=None,
  evidence='SRC com/ichi2/anki/stats/AnkiStatsTaskHandler.java:143-162, 169-183; FW-SRC core/java/android/os/AsyncTask.java:369-375, 691-696, 700-713',
  note='Same hand-back as the chart task: postResult (AsyncTask.java:369-375), InternalHandler and finish (AsyncTask.java:691-695, 712), then onPostExecute when the task was not cancelled.')

e('AnkiStatsTaskHandler.createReviewSummaryStatistics', 'AnkiStatsTaskHandler$DeckPreviewStatistics.doInBackground', 'ASYNC',
  'execute() on the deck preview task runs doInBackground on the AsyncTask worker thread',
  env=None,
  evidence='SRC com/ichi2/anki/stats/AnkiStatsTaskHandler.java:75-79; FW-SRC core/java/android/os/AsyncTask.java:594-595, 632-654',
  note='Same dispatch as the chart task (executeOnExecutor, onPreExecute on the caller thread at AsyncTask.java:648, exec.execute at AsyncTask.java:651). DeckPreviewStatistics does not override onPreExecute.')

e('AnkiStatsTaskHandler$DeckPreviewStatistics.doInBackground', 'AnkiStatsTaskHandler$DeckPreviewStatistics.onPostExecute', 'ASYNC',
  'the studied-today text returns to the UI thread, where it is set on the deck list text view',
  env=None,
  evidence='SRC com/ichi2/anki/stats/AnkiStatsTaskHandler.java:197-237, 245-251; FW-SRC core/java/android/os/AsyncTask.java:369-375, 691-696, 700-713',
  note='Same hand-back as the chart task: postResult (AsyncTask.java:369-375), InternalHandler and finish (AsyncTask.java:691-695, 712), then onPostExecute when the task was not cancelled.')

UNREACHABLE['AnkiStatsTaskHandler$DeckPreviewStatistics.onCancelled'] = ('no_trigger_in_app', "DeckPreviewStatistics.onCancelled runs only after cancel(true) on that task. No in-app code holds or cancels a DeckPreviewStatistics: createReviewSummaryStatistics returns it and DeckPicker discards the result (DeckPicker.java:1873). The cancel(true) calls in Statistics.java (543, 574, 681, 692) cancel only the chart and overview tasks, and the DeckTask cancel (DeckTask.java:172) acts on a DeckTask. So the method never runs.", "SRC com/ichi2/anki/stats/AnkiStatsTaskHandler.java:75-78, 240-242; SRC com/ichi2/anki/DeckPicker.java:1873; SRC com/ichi2/anki/Statistics.java:543, 574, 681, 692; SRC com/ichi2/async/DeckTask.java:172; FW-SRC core/java/android/os/AsyncTask.java:462-463, 691-693", 'SOURCE')

# ---- part 066 (2026-10-28)
# AnkiDroid batch 066 (LABEL helper). Batch file: graphs/AnkiDroid/scratch/batches/batch_066.txt (36 methods).
# Full row list: graphs/AnkiDroid/parts/label_066.md.
# Methods: ChartView (3 constructors, addFragment, onDraw, onSizeChanged, setData), OverviewStatsBuilder (constructor and
# private helpers), OverviewStatsBuilder$OverviewStats.<init>, StatsMetaInfo (implicit constructor and 18 accessors).
#
# Route ownership:
# - Automatic CALL edges into and out of these methods (Statistics -> addFragment, AnkiStatsTaskHandler -> setData and the
#   OverviewStatsBuilder constructor, the OverviewStatsBuilder internal calls, Stats.calculateDue -> StatsMetaInfo) come
#   from the builder. They are not written here.
# - The three framework edges below have the page S_STATISTICS as source, so they belong to this part (the destination is
#   a method of this batch).
# Gates: STATE_SETTINGS (the advanced statistics preference, for the StatsMetaInfo accessors reached through
# Stats.calculateDue). No MG id is used.

# --- Chart view inflated from fragment_anki_stats.xml (Statistics.ChartFragment.onCreateView, Statistics.java:428).
e('S_STATISTICS', 'ChartView.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'the statistics chart pages inflate the chart view from fragment_anki_stats.xml',
  cls='non_standard',
  via=['layout XML and LayoutInflater reflection'],
  evidence='SRC com/ichi2/anki/Statistics.java:421-428; SRC res/layout/fragment_anki_stats.xml:5; FW-SRC core/java/android/view/LayoutInflater.java:90-91, 615',
  note='LayoutInflater builds the view with the (Context, AttributeSet) constructor by reflection (LayoutInflater.java:615). The page is opened from the navigation drawer (NavigationDrawerActivity.java:265-268) and its fragments come from SectionsPagerAdapter.getItem (Statistics.java:305-309). No gate.')

# --- View.draw calls onDraw (framework callback on the statistics page).
e('S_STATISTICS', 'ChartView.onDraw', 'FRAMEWORK',
  'the statistics screen draws the chart view; View.draw calls onDraw',
  evidence='SRC com/ichi2/anki/stats/ChartView.java:56-57; FW-SRC core/java/android/view/View.java:19161-19166, 19192, 19308',
  note='onDraw runs for the chart view on every draw of the page. With no data set it calls super.onDraw (ChartView.java:74-75). No gate.')

# --- View.setFrame -> sizeChange -> onSizeChanged (framework callback on the statistics page).
e('S_STATISTICS', 'ChartView.onSizeChanged', 'FRAMEWORK',
  'the chart view is laid out with a new size; View.setFrame calls sizeChange, which calls onSizeChanged',
  evidence='SRC com/ichi2/anki/stats/ChartView.java:91-92; FW-SRC core/java/android/view/View.java:19720, 19752-19753, 19791-19792',
  note='The override calls mFragment.checkAndUpdate() once addFragment has run (ChartView.java:95-96). No gate.')

# --- Unreachable: the layout inflater and the app never use these constructors.
UNREACHABLE['ChartView.<init>(Context)'] = ('framework_never_calls', 'LayoutInflater builds chart views with the (Context, AttributeSet) constructor only, and nothing in the app calls the one-argument constructor (no new ChartView in the source root and no subclass of ChartView)', 'com/ichi2/anki/stats/ChartView.java:40-43; FW-SRC core/java/android/view/LayoutInflater.java:90-91, 615; res/layout/fragment_anki_stats.xml:5', 'SOURCE')

UNREACHABLE['ChartView.<init>(Context,AttributeSet,int)'] = ('framework_never_calls', 'The three-argument constructor runs only when a subclass calls it through super or when code calls new ChartView with a style; the layout inflater uses the two-argument constructor, the two-argument ChartView constructor calls super(context, attrs) (ChartView.java:46), and the source root has no new ChartView and no subclass of ChartView', 'com/ichi2/anki/stats/ChartView.java:45-53; FW-SRC core/java/android/view/LayoutInflater.java:90-91, 615', 'SOURCE')

# ---- part 067 (2026-10-28)
# AnkiDroid batch 067 (LABEL helper). 39 methods: HttpFetcher, DeckAdapter (and its ViewHolder), DeckDropDownAdapter
# (and its ViewHolder), FabBehavior, PopupMenuWithIcons.<init>, ActivityTransitionAnimation.<init>, ViewAnimation.
# The full row list is in graphs/AnkiDroid/parts/label_067.md.
#
# Route ownership:
# - Automatic CALL edges (auto_calls.json) are not written here, for example HttpFetcher -> LoadPronounciationActivity,
#   DeckPicker.onCreate -> DeckAdapter setters, DeckAdapter.buildDeckList -> processNodes, FabBehavior.onDependentViewChanged
#   -> getFabTranslationYForSnackbar, and AbstractFlashcardViewer -> ViewAnimation.fade.
# - Edges written here: page-sourced framework dispatch (S_DECKPICKER, S_STATISTICS, S_CARDBROWSER) into methods of this batch.
#   Support library dispatch (RecyclerView, CoordinatorLayout) is INFERRED, source not read.
#
# Gates: STATE_CARDS on the congrats or no-cards Snackbar path (FabBehavior.onDependentViewChanged). No MISSING GATE edge
# is written; the subdeck guard of DeckAdapter.setDeckExpander is MG612, described in the .md row only.

# --- Home screen deck list (S_DECKPICKER): RecyclerView adapter callbacks.
e('S_DECKPICKER', 'DeckAdapter.onCreateViewHolder', 'FRAMEWORK',
  'the home screen deck list asks the adapter for a new row view',
  env=None,
  needs_state=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:375-388; com/ichi2/anki/widgets/DeckAdapter.java:154-158; RecyclerView dispatch is support library, INFERRED, source not read')

e('S_DECKPICKER', 'DeckAdapter.onBindViewHolder', 'FRAMEWORK',
  'the home screen deck list binds the data of each visible row',
  env=None,
  needs_state=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:375-388; com/ichi2/anki/widgets/DeckAdapter.java:161-217; RecyclerView dispatch is support library, INFERRED, source not read')

e('S_DECKPICKER', 'DeckAdapter.getItemCount', 'FRAMEWORK',
  'the RecyclerView asks the number of decks for its layout',
  env=None,
  needs_state=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:375-388; com/ichi2/anki/widgets/DeckAdapter.java:220-222; RecyclerView dispatch is support library, INFERRED, source not read')

# --- Home screen FAB behavior (S_DECKPICKER): CoordinatorLayout behavior callbacks.
e('S_DECKPICKER', 'FabBehavior.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'the support library creates the FAB behavior from layout_behavior when the home screen is inflated',
  env=None,
  needs_state=None,
  cls='non_standard',
  via='CoordinatorLayout behavior from layout_behavior (support library, not in the dataset)',
  evidence='SRC res/layout-v14/floating_add_button.xml:16; res/layout/deck_picker.xml:2-3, 36; res/layout/homescreen.xml:7; com/ichi2/anki/widgets/FabBehavior.java:42-44; CoordinatorLayout dispatch is support library, INFERRED, source not read')

e('S_DECKPICKER', 'FabBehavior.layoutDependsOn', 'FRAMEWORK',
  'the CoordinatorLayout asks the FAB behavior whether it depends on each sibling view during layout',
  env=None,
  needs_state=None,
  evidence='SRC res/layout/deck_picker.xml:2-3, 36; com/ichi2/anki/widgets/FabBehavior.java:62-64; CoordinatorLayout dispatch is support library, INFERRED, source not read')

e('S_DECKPICKER', 'FabBehavior.onDependentViewChanged', 'FRAMEWORK',
  'a Snackbar on the home screen root changes the dependency and the FAB behavior is told',
  env=None,
  needs_state=STATE_CARDS,
  evidence='SRC com/ichi2/anki/widgets/FabBehavior.java:67-77; com/ichi2/anki/UIUtils.java:33-35; com/ichi2/anki/DeckPicker.java:656-664; CoordinatorLayout dispatch is support library, INFERRED, source not read',
  note='Gate STATE_CARDS: the congrats or no-cards-due Snackbar follows a study session with RESULT_NO_MORE_CARDS (DeckPicker.java:656-664).')

# --- Toolbar deck spinner of the Statistics screen (S_STATISTICS): framework Spinner calls into DeckDropDownAdapter.
e('S_STATISTICS', 'DeckDropDownAdapter.getCount', 'FRAMEWORK',
  'the toolbar deck spinner measures its content and reads the count of decks',
  env=None,
  needs_state=None,
  evidence='FW-SRC core/java/android/widget/Spinner.java:601-606, 831-847; com/ichi2/anki/Statistics.java:100')

e('S_STATISTICS', 'DeckDropDownAdapter.getView', 'FRAMEWORK',
  'the closed toolbar deck spinner draws its selected deck',
  env=None,
  needs_state=None,
  evidence='FW-SRC core/java/android/widget/Spinner.java:660, 698-712; com/ichi2/anki/Statistics.java:100')

e('S_STATISTICS', 'DeckDropDownAdapter.getDropDownView', 'GUI',
  'the user opens the toolbar deck spinner and each row of its list is drawn',
  env=None,
  needs_state=None,
  gui=['the user opens the toolbar deck spinner and each row of its list is drawn'],
  evidence='FW-SRC core/java/android/widget/AbsListView.java:2365; FW-SRC core/java/android/widget/Spinner.java:989-994; com/ichi2/anki/Statistics.java:100-101')

e('S_STATISTICS', 'DeckDropDownAdapter.getItemId', 'GUI',
  'the user taps a row of the open toolbar deck list',
  env=None,
  needs_state=None,
  gui=['the user taps a row of the open toolbar deck list'],
  evidence='FW-SRC core/java/android/widget/AbsListView.java:3108-3127; FW-SRC core/java/android/widget/Spinner.java:985-987; com/ichi2/anki/Statistics.java:100-101')

# --- Toolbar deck spinner of the card browser (S_CARDBROWSER): same framework paths, CardBrowser.java:372-385.
e('S_CARDBROWSER', 'DeckDropDownAdapter.getCount', 'FRAMEWORK',
  'the toolbar deck spinner of the card browser measures its content and reads the count of decks',
  env=None,
  needs_state=None,
  evidence='FW-SRC core/java/android/widget/Spinner.java:601-606, 831-847; com/ichi2/anki/CardBrowser.java:372-373')

e('S_CARDBROWSER', 'DeckDropDownAdapter.getView', 'FRAMEWORK',
  'the closed toolbar deck spinner of the card browser draws its selected deck',
  env=None,
  needs_state=None,
  evidence='FW-SRC core/java/android/widget/Spinner.java:660, 698-712; com/ichi2/anki/CardBrowser.java:372-373')

e('S_CARDBROWSER', 'DeckDropDownAdapter.getDropDownView', 'GUI',
  'the user opens the card browser toolbar deck spinner and each row of its list is drawn',
  env=None,
  needs_state=None,
  gui=['the user opens the card browser toolbar deck spinner and each row of its list is drawn'],
  evidence='FW-SRC core/java/android/widget/AbsListView.java:2365; FW-SRC core/java/android/widget/Spinner.java:989-994; com/ichi2/anki/CardBrowser.java:372-373')

e('S_CARDBROWSER', 'DeckDropDownAdapter.getItemId', 'GUI',
  'the user taps a row of the open card browser toolbar deck list',
  env=None,
  needs_state=None,
  gui=['the user taps a row of the open card browser toolbar deck list'],
  evidence='FW-SRC core/java/android/widget/AbsListView.java:3108-3127; FW-SRC core/java/android/widget/Spinner.java:985-987; com/ichi2/anki/CardBrowser.java:372-373')

# --- UNREACHABLE entries (one per method with no route).
UNREACHABLE['HttpFetcher.<init>'] = ('no_trigger_in_app',
  'HttpFetcher declares no constructor and no code creates an instance; every caller uses the static methods',
  'com/ichi2/anki/web/HttpFetcher.java:47; com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:212, 252; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:182',
  'SOURCE')

UNREACHABLE['ActivityTransitionAnimation.<init>'] = ('no_trigger_in_app',
  'ActivityTransitionAnimation declares no constructor and no code creates an instance; only the static slide method is used',
  'com/ichi2/anim/ActivityTransitionAnimation.java:9-20; com/ichi2/anki/AnkiActivity.java:232, 249',
  'SOURCE')

UNREACHABLE['ViewAnimation.<init>'] = ('no_trigger_in_app',
  'ViewAnimation declares no constructor and no code creates an instance; callers use the static fade method',
  'com/ichi2/anim/ViewAnimation.java:10-21; com/ichi2/anki/AbstractFlashcardViewer.java:1221, 1224, 1233',
  'SOURCE')

UNREACHABLE['ViewAnimation.slide'] = ('no_trigger_in_app',
  'no caller: the only class that uses ViewAnimation calls fade, and no code calls ViewAnimation.slide',
  'com/ichi2/anim/ViewAnimation.java:23-62; com/ichi2/anki/AbstractFlashcardViewer.java:76, 1221, 1224, 1233',
  'SOURCE')

UNREACHABLE['DeckDropDownAdapter.getItem'] = ('framework_never_calls',
  'the framework reaches the spinner getItem only through getSelectedItem or getItemAtPosition, and neither is called for this spinner; AbsSpinner.java not read',
  'FW-SRC core/java/android/widget/AdapterView.java:590-594, 796-798; FW-SRC core/java/android/widget/Spinner.java:981-983; FW-SRC core/java/android/preference/PreferenceFragment.java:452; com/ichi2/anki/Statistics.java:99-101, 112; com/ichi2/anki/CardBrowser.java:372-374, 385',
  'INFERRED')

UNREACHABLE['FabBehavior.<init>()'] = ('no_trigger_in_app',
  'no code calls new FabBehavior(); the support library uses the (Context, AttributeSet) constructor from layout_behavior (INFERRED, source not read)',
  'com/ichi2/anki/widgets/FabBehavior.java:38-40; res/layout-v14/floating_add_button.xml:16',
  'SOURCE')

# ---- part 071 (2026-10-28)
UNREACHABLE['DeckTask$TaskData.getType'] = ('no_trigger_in_app', 'No caller passes a DeckTask.TaskData receiver to getType(). The only definition is DeckTask.java:1538-1540. A grep for getType() over the source root gives 45 matches, all on other receivers (EFieldType field getters, Card, AdvancedStatistics, Intent). No trigger in the app reaches this accessor.', 'com/ichi2/async/DeckTask.java:1538-1540', 'SOURCE')
UNREACHABLE['DeckTask$TaskData.setCards'] = ('no_trigger_in_app', 'The only setCards( occurrence in the source root is the definition at DeckTask.java:1493-1495 (the other grep hit, resetCards, is a different method). No caller sets mCards on a TaskData, so no trigger in the app reaches it.', 'com/ichi2/async/DeckTask.java:1493-1495', 'SOURCE')

# ---- part 069 (2026-10-28)
# AnkiDroid batch 069 (LABEL helper). DeckTask part 1: 40 methods, all REACHABLE (no UNREACHABLE entries).
# The full row list is in graphs/AnkiDroid/parts/label_069.md.
#
# Route ownership:
# - The launch edges into the DeckTask bodies (for example StudyOptionsFragment, DeckPicker, CardBrowser) belong to the
#   launch-site batches. The CALL edges (cancelTask(int) -> cancelTask(), ProgressCallback -> doProgress, the getCard callers,
#   Finder -> getInstance) come from auto_calls.json and are not written here.
# - Written here: doInBackground -> DeckTask.onPostExecute (the AsyncTask result hop), and each task body that calls
#   publishProgress -> DeckTask.onProgressUpdate, plus doProgress -> DeckTask.onProgressUpdate. The line of each publishProgress
#   is in the EDGE row of label_069.md.
# - No gate is needed in this batch (MG632-MG641 are not used).

e('DeckTask.doInBackground', 'DeckTask.onPostExecute', 'ASYNC',
  'the worker result is delivered to DeckTask.onPostExecute on the UI thread (AsyncTask finish)',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:203-228, 360-365',
  note='DeckTask.onPostExecute forwards to mListener.onPostExecute (DeckTask.java:362). The AsyncTask finish dispatch is framework code and was not read in this batch. No gate of its own.')

e('DeckTask.doInBackgroundAddNote', 'DeckTask.onProgressUpdate', 'ASYNC',
  'publishProgress posts the added note to onProgressUpdate on the UI thread',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:378-381, 352-355',
  note='publishProgress is at DeckTask.java:380, inside the transaction. onProgressUpdate forwards to the listener (DeckTask.java:354). The UI-thread dispatch is AsyncTask (framework, not read in this batch).')

e('DeckTask.doInBackgroundUpdateNote', 'DeckTask.onProgressUpdate', 'ASYNC',
  'publishProgress posts the updated card to onProgressUpdate on the UI thread',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:418-423, 352-355',
  note='publishProgress is at DeckTask.java:420 and 422 (one per branch). onProgressUpdate forwards to the listener (DeckTask.java:354). The UI-thread dispatch is AsyncTask (framework, not read in this batch).')

e('DeckTask.doInBackgroundAnswerCard', 'DeckTask.onProgressUpdate', 'ASYNC',
  'publishProgress posts the answered card to onProgressUpdate on the UI thread',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:455-458, 352-355',
  note='publishProgress is at DeckTask.java:457. onProgressUpdate forwards to the listener (DeckTask.java:354). The UI-thread dispatch is AsyncTask (framework, not read in this batch).')

e('DeckTask.doInBackgroundDismissNote', 'DeckTask.onProgressUpdate', 'ASYNC',
  'publishProgress posts the dismissed card to onProgressUpdate on the UI thread',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:563-566, 352-355',
  note='publishProgress is at DeckTask.java:565. onProgressUpdate forwards to the listener (DeckTask.java:354). The UI-thread dispatch is AsyncTask (framework, not read in this batch).')

e('DeckTask.doInBackgroundUndo', 'DeckTask.onProgressUpdate', 'ASYNC',
  'publishProgress posts the undone card to onProgressUpdate on the UI thread',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:599-602, 352-355',
  note='publishProgress is at DeckTask.java:601. onProgressUpdate forwards to the listener (DeckTask.java:354). The UI-thread dispatch is AsyncTask (framework, not read in this batch).')

e('DeckTask.doInBackgroundSearchCards', 'DeckTask.onProgressUpdate', 'ASYNC',
  'publishProgress posts the search results to onProgressUpdate on the UI thread',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:629-634, 352-355',
  note='publishProgress is at DeckTask.java:633, in the else branch of the isCancelled check (line 629). onProgressUpdate forwards to the listener (DeckTask.java:354).')

e('DeckTask.doInBackgroundRenderBrowserQA', 'DeckTask.onProgressUpdate', 'ASYNC',
  'publishProgress posts the render progress to onProgressUpdate on the UI thread',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:657-660, 352-355',
  note='publishProgress is at DeckTask.java:659. onProgressUpdate forwards to the listener (DeckTask.java:354). The UI-thread dispatch is AsyncTask (framework, not read in this batch).')

e('DeckTask.doInBackgroundImportReplace', 'DeckTask.onProgressUpdate', 'ASYNC',
  'publishProgress posts the import progress messages to onProgressUpdate on the UI thread',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:805-810, 855-860, 352-355',
  note='publishProgress is at DeckTask.java:809 (before the collection import) and 859 (in the media loop). onProgressUpdate forwards to the listener (DeckTask.java:354).')

e('DeckTask.doProgress', 'DeckTask.onProgressUpdate', 'ASYNC',
  'doProgress publishes the importer progress, which reaches onProgressUpdate on the UI thread',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:1348-1350, 352-355',
  note='doProgress calls publishProgress (DeckTask.java:1349), the AsyncTask method. The importer path is ProgressCallback.publishProgress (DeckTask.java:1340-1344), created in doInBackgroundImportAdd (DeckTask.java:750).')

# ---- part 068 (2026-10-28)
# AnkiDroid batch 068 (LABEL helper). BaseAsyncTask (5 methods), CollectionLoader (6), Connection (20),
# Connection$CancelCallback (3) and Connection$Payload (4). The full row list is in
# graphs/AnkiDroid/parts/label_068.md.
#
# Route ownership:
# - The ASYNC framework-dispatch edges from Connection.launchConnectionTask, Connection.cancel, the three
#   Connection.publishProgress overloads and the CollectionLoader callbacks are written here.
# - Auto CALL edges (super calls, call sites) come from auto_calls.json and are not repeated here.
# - The DeckPicker key listener into Connection.cancel is owned by the DeckPicker part.
#
# Gates: MG622 (batch range MG622-MG631). The CollectionLoader onStartLoading -> loadInBackground edge uses MG622.

# --- Connection.launchConnectionTask: the AsyncTask framework dispatch (Connection.java:97-100).
e('Connection.launchConnectionTask', 'Connection.onPreExecute', 'ASYNC',
  'AsyncTask.execute runs onPreExecute on the calling thread before the worker starts',
  evidence='SRC com/ichi2/async/Connection.java:81-102, 124-131; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-650',
  note='Framework dispatch (FW-SRC line 648). ASYNC follows the AsyncTask convention in label_019.py.')

e('Connection.launchConnectionTask', 'Connection.doInBackground', 'ASYNC',
  'execute starts the AsyncTask worker, which calls doInBackground on the background thread',
  evidence='SRC com/ichi2/async/Connection.java:81-102, 173-179; FW-SRC core/java/android/os/AsyncTask.java:326-340, 594-596',
  note='Framework dispatch: the worker calls doInBackground (FW-SRC line 333). The executor step is not printed (INFERRED).')

e('Connection.launchConnectionTask', 'Connection.onPostExecute', 'ASYNC',
  'finish calls onPostExecute on the main thread when the task was not cancelled',
  evidence='SRC com/ichi2/async/Connection.java:81-102, 138-145; FW-SRC core/java/android/os/AsyncTask.java:691-697',
  note='Framework dispatch (FW-SRC line 695). ASYNC follows the AsyncTask convention in label_019.py.')

# --- Connection.publishProgress overloads: posted progress is delivered to onProgressUpdate (FW-SRC 684-718).
e('Connection.publishProgress(int)', 'Connection.onProgressUpdate', 'ASYNC',
  'publishProgress posts a progress message that handleMessage delivers to onProgressUpdate on the main thread',
  evidence='SRC com/ichi2/async/Connection.java:461-463, 152-157; FW-SRC core/java/android/os/AsyncTask.java:684-689, 706-718',
  note='Framework dispatch: publishProgress (FW-SRC 684-689), then handleMessage calls onProgressUpdate (FW-SRC 706-718, line 715).')

e('Connection.publishProgress(int,long,long)', 'Connection.onProgressUpdate', 'ASYNC',
  'publishProgress posts a progress message that handleMessage delivers to onProgressUpdate on the main thread',
  evidence='SRC com/ichi2/async/Connection.java:471-473, 152-157; FW-SRC core/java/android/os/AsyncTask.java:684-689, 706-718',
  note='Framework dispatch, as for publishProgress(int) (FW-SRC 684-689, 706-718).')

e('Connection.publishProgress(String)', 'Connection.onProgressUpdate', 'ASYNC',
  'publishProgress posts a progress message that handleMessage delivers to onProgressUpdate on the main thread',
  evidence='SRC com/ichi2/async/Connection.java:466-468, 152-157; FW-SRC core/java/android/os/AsyncTask.java:684-689, 706-718',
  note='Framework dispatch, as for publishProgress(int) (FW-SRC 684-689, 706-718).')

# --- Connection.cancel: cancel(true) reaches onCancelled through the framework (Connection.java:539-543).
e('Connection.cancel', 'Connection.onCancelled', 'ASYNC',
  'cancel(true) makes the framework call onCancelled(result) on the main thread',
  evidence='SRC com/ichi2/async/Connection.java:539-543, 109-117; FW-SRC core/java/android/os/AsyncTask.java:345-358, 462-464, 525-528, 691-697',
  note='Framework cancel path: cancel(true) (FW-SRC 525-528), the future done step (FW-SRC 345-358), then finish calls onCancelled(result) (FW-SRC 691-697, 462-464). The DeckPicker route into cancel is owned by the DeckPicker part.')

# --- CollectionLoader: the start and the background load (CollectionLoader.java:47-55, 19-29).
e('CollectionLoader.onStartLoading', 'CollectionLoader.loadInBackground', 'ASYNC',
  'forceLoad runs loadInBackground on a background thread when the collection is not locked',
  guard='collection not locked (CollectionHelper.isCollectionLocked() false)',
  evidence='SRC com/ichi2/async/CollectionLoader.java:47-55, 19-29',
  note='MISSING GATE MG622: the collection is not locked when the load starts (CollectionLoader.java:49-52). Connection.java:279 locks the collection during a sync and Connection.java:456 unlocks it. No predefined ENV or STATE constant fits, so env and needs_state are unset. The support-library forceLoad step is INFERRED, source not read.')

e('CollectionLoader.loadInBackground', 'CollectionLoader.deliverResult', 'ASYNC',
  'the support-library AsyncTaskLoader delivers the loadInBackground result to deliverResult',
  evidence='SRC com/ichi2/async/CollectionLoader.java:19-29, 31-44',
  note='The support-library AsyncTaskLoader delivers the result after loadInBackground returns (INFERRED, source not read). deliverResult forwards the value when the loader is started (line 41).')

# --- UNREACHABLE: Connection$CancelCallback is never constructed in the source root (Connection.java:549-566).
UNREACHABLE['Connection$CancelCallback.<init>'] = ('no_trigger_in_app', 'No code in the source root creates a CancelCallback. The class has only the implicit constructor. Its references are the parameter type (HttpSyncer.java:152-153) and a call on a parameter (HttpSyncer.java:231), which create no instance.', 'SRC com/ichi2/async/Connection.java:549-551; com/ichi2/libanki/sync/HttpSyncer.java:152-153, 230-232', 'SOURCE')

UNREACHABLE['Connection$CancelCallback.cancelAllConnections'] = ('no_trigger_in_app', 'No call site in the source root. The method is reached only through a CancelCallback object, and none is created in the source root.', 'SRC com/ichi2/async/Connection.java:558-566', 'SOURCE')

UNREACHABLE['Connection$CancelCallback.setConnectionManager'] = ('branch_never_taken', 'The only call is inside if (cancelCallback != null) (HttpSyncer.java:230-232). The only 5-argument req call in the source root is HttpSyncer.java:148, which passes the literal null, and the other req calls have at most four arguments. So cancelCallback is always null and the branch is never taken.', 'SRC com/ichi2/async/Connection.java:553-555; com/ichi2/libanki/sync/HttpSyncer.java:143-155, 230-232; com/ichi2/libanki/sync/RemoteMediaServer.java:94-100, 113-120, 143-148', 'SOURCE')

# --- UNREACHABLE: the zero-, two- and three-argument Connection$Payload constructors have no call site (Connection.java:514-536).
UNREACHABLE['Connection$Payload.<init>()'] = ('no_trigger_in_app', 'No call with zero arguments in the source root. The grep of Payload( finds the declaration (Connection.java:514) and only the one-argument constructions (MyAccount.java:140, DeckPicker.java:1285).', 'SRC com/ichi2/async/Connection.java:514-517; com/ichi2/anki/MyAccount.java:139-143; com/ichi2/anki/DeckPicker.java:1284-1286', 'SOURCE')

UNREACHABLE['Connection$Payload.<init>(int,Object[])'] = ('no_trigger_in_app', 'No call with two arguments in the source root. The grep of Payload( finds the declaration (Connection.java:526) and only the one-argument constructions (MyAccount.java:140, DeckPicker.java:1285). login and sync set taskType themselves (Connection.java:161, 167).', 'SRC com/ichi2/async/Connection.java:526-530, 160-169; com/ichi2/anki/MyAccount.java:139-143; com/ichi2/anki/DeckPicker.java:1284-1286', 'SOURCE')

UNREACHABLE['Connection$Payload.<init>(int,Object[],String)'] = ('no_trigger_in_app', 'No call with three arguments in the source root. The grep of Payload( finds the declaration (Connection.java:532) and only the one-argument constructions. The path argument is not stored in the body (lines 533-535).', 'SRC com/ichi2/async/Connection.java:532-536', 'SOURCE')

# ---- sup for part 068 (2026-10-28): the only 5-argument req() call passes null and no CancelCallback is constructed, so line 231 never runs.
sup(('HttpSyncer.req(String,InputStream,int,JSONObject,CancelCallback)', 'Connection$CancelCallback.setConnectionManager'))
sup(('HttpSyncer.req(String,InputStream,int,JSONObject,CancelCallback)@FullSyncer', 'Connection$CancelCallback.setConnectionManager'))
sup(('HttpSyncer.req(String,InputStream,int,JSONObject,CancelCallback)@RemoteMediaServer', 'Connection$CancelCallback.setConnectionManager'))

# ---- part 070 (2026-10-28)
e('DeckTask$ProgressCallback.publishProgress', 'DeckTask.onProgressUpdate', 'ASYNC',
  'worker progress: ProgressCallback.publishProgress forwards to DeckTask.doProgress, which calls AsyncTask.publishProgress; the framework handler then calls onProgressUpdate on the main thread',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:1340-1344, 1348-1350, 352-355; FW-SRC core/java/android/os/AsyncTask.java:684-689, 712-716',
  note='The route goes through the framework handler, not a direct call in the app source, so it is not a bytecode CALL. The import task doInBackgroundImportAdd is the one that publishes this progress. No MG gate is needed.')

UNREACHABLE['DeckTask$ProgressCallback.getResources'] = ('no_trigger_in_app', 'no caller: the only ProgressCallback is held in the importer field mProgress, and the importer calls only mProgress.publishProgress (Anki2Importer.publishProgress, line 762); the getResources( calls in files that mention ProgressCallback are only the app Context calls in the DeckTask class at lines 746 and 760', 'SRC com/ichi2/async/DeckTask.java:1335-1337, 746, 760; SRC com/ichi2/libanki/importer/Importer.java:44, 80-81; SRC com/ichi2/libanki/importer/Anki2Importer.java:761-762', 'SOURCE')
UNREACHABLE['DeckTask$TaskData.<init>(int,Card)'] = ('no_trigger_in_app', 'No call passes an int first with a Card second. Card-first calls use the (Card,int), (Card,String) or (Card,boolean) forms (lines 422, 565, 601, and the viewer and reviewer launches). The three-argument int calls take a long or an Object[] second (lines 682, 1119).', 'SRC com/ichi2/async/DeckTask.java:1378, 422, 565, 601, 682, 1119; SRC com/ichi2/anki/AbstractFlashcardViewer.java:1077, 1085, 1093; SRC com/ichi2/anki/Reviewer.java:111', 'SOURCE')
UNREACHABLE['DeckTask$TaskData.<init>(int,String)'] = ('no_trigger_in_app', 'No call passes an int first with a String second. The String calls are the one-argument TaskData(String) (Anki2Importer lines 761-762) and the two-argument TaskData(String,boolean) (importAdd, lines 1579-1581, and the removeTemplateFailed return at line 1057).', 'SRC com/ichi2/async/DeckTask.java:1475, 1057; SRC com/ichi2/anki/DeckPicker.java:1579-1581; SRC com/ichi2/libanki/importer/Anki2Importer.java:761-762', 'SOURCE')
UNREACHABLE['DeckTask$TaskData.<init>(int,boolean)'] = ('no_trigger_in_app', 'No call passes an int first with a boolean second. Boolean-only calls use TaskData(boolean) (line 390). Two-argument boolean calls take a Card first (CardBrowser line 698, AbstractFlashcardViewer line 1085) or a String first (importAdd, lines 1579-1581).', 'SRC com/ichi2/async/DeckTask.java:1443, 390; SRC com/ichi2/anki/CardBrowser.java:698; SRC com/ichi2/anki/AbstractFlashcardViewer.java:1085; SRC com/ichi2/anki/DeckPicker.java:1579-1581', 'SOURCE')
UNREACHABLE['DeckTask$TaskData.<init>(long,boolean)'] = ('no_trigger_in_app', 'No call passes a long first with a boolean second. The only long-argument launches pass a single long (deleteDeck at line 2067, deleteModel at lines 578-580).', 'SRC com/ichi2/async/DeckTask.java:1437; SRC com/ichi2/anki/DeckPicker.java:2067; SRC com/ichi2/anki/ModelBrowser.java:578-580', 'SOURCE')
UNREACHABLE['DeckTask$TaskData.<init>(Context,int,int)'] = ('no_trigger_in_app', 'No call passes a Context. Every three-argument call starts with an int (0 or -2), as at lines 682, 782 and 1119.', 'SRC com/ichi2/async/DeckTask.java:1408, 682, 782, 1119', 'SOURCE')
UNREACHABLE['DeckTask$TaskData.<init>(String,long,boolean)'] = ('no_trigger_in_app', 'No call passes a String first with a long second. The three-argument calls start with an int (0 or -2), as at lines 682, 782 and 1119.', 'SRC com/ichi2/async/DeckTask.java:1481, 682, 782, 1119', 'SOURCE')
UNREACHABLE['DeckTask$TaskData.<init>(List,Comparator)'] = ('no_trigger_in_app', 'No call passes a List and a Comparator. The List calls (lines 633 and 663) take one argument, and the Comparator getter has no caller (getComparator, line 1498).', 'SRC com/ichi2/async/DeckTask.java:1420, 633, 663, 1498', 'SOURCE')
UNREACHABLE['DeckTask$TaskData.getComparator'] = ('no_trigger_in_app', 'No caller. No TaskData carries a Comparator, since the List,Comparator constructor has no caller, and a grep for .getComparator( in the files that mention TaskData finds no call.', 'SRC com/ichi2/async/DeckTask.java:1420, 1498', 'SOURCE')
UNREACHABLE['DeckTask$TaskData.getContext'] = ('no_trigger_in_app', 'No caller on a TaskData. The grep of getContext() in the files that mention TaskData shows only Activity, fragment and dialog calls (ModelBrowser line 661, DeckPicker line 1345, StudyOptionsFragment line 675); the Context constructor has no caller either.', 'SRC com/ichi2/async/DeckTask.java:1408, 1533; SRC com/ichi2/anki/ModelBrowser.java:661; SRC com/ichi2/anki/DeckPicker.java:1345; SRC com/ichi2/anki/StudyOptionsFragment.java:675', 'SOURCE')

# ---- part 072 (2026-10-28)
# AnkiDroid batch 072 (LABEL helper). CompatHelper static methods, CompatV10 base bodies and its anonymous classes,
# CompatV11, CompatV15 ($1 listener), CompatV16 and CompatV17: 36 methods. The full row list is in
# graphs/AnkiDroid/parts/label_072.md.
#
# Route ownership: the three e() calls are the TTS listener edges from CompatV15.setTtsOnUtteranceProgressListener
# (CompatV15.java:13-30). The other CALL edges come from auto_calls.json and are not written here.
# Gates: ENV_TTS and STATE_SETTINGS (the TTS preference, as in label_053). No MISSING GATE is needed.
# UNREACHABLE: isNook (no caller) and 18 closed members on the standard API 27 path (12 CompatV10 base bodies that a
# CompatV11..CompatV21 class overrides, and 6 members of their anonymous classes).

e('CompatV15.setTtsOnUtteranceProgressListener', 'CompatV15$1.onDone', 'FRAMEWORK',
  'the TTS engine reports that an utterance finished and the listener speaks the next queued text',
  env=ENV_TTS,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/compat/CompatV15.java:13-22; SRC com/ichi2/anki/ReadText.java:195',
  note='The TTS engine dispatch is not in fw_src (android/speech not read): INFERRED. The body runs only when ReadText.sTextQueue is not empty.')

e('CompatV15.setTtsOnUtteranceProgressListener', 'CompatV15$1.onError', 'FRAMEWORK',
  'the TTS engine reports an error for an utterance',
  env=ENV_TTS,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/compat/CompatV15.java:13-25; SRC com/ichi2/anki/ReadText.java:195',
  note='The TTS engine dispatch is not in fw_src (android/speech not read): INFERRED. The body is empty.')

e('CompatV15.setTtsOnUtteranceProgressListener', 'CompatV15$1.onStart', 'FRAMEWORK',
  'the TTS engine reports that an utterance started',
  env=ENV_TTS,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/compat/CompatV15.java:13-28; SRC com/ichi2/anki/ReadText.java:195',
  note='The TTS engine dispatch is not in fw_src (android/speech not read): INFERRED. The body is empty.')

UNREACHABLE['CompatHelper.isNook'] = ('no_trigger_in_app',
  'No caller in the app source. The constructor uses the private isNookHdOrHdPlus (CompatHelper.java:33), not this method. A grep over src/main/java finds no other reference.',
  'com/ichi2/compat/CompatHelper.java:33, 101-103', 'SOURCE')

UNREACHABLE['CompatV10.detagged'] = ('closed_by_api_level',
  'CompatV16 overrides it (Html.escapeHtml). The base body runs only on API 10 to 15, not on the standard API 27 path.',
  'com/ichi2/compat/CompatV10.java:49-55; com/ichi2/compat/CompatV16.java:34-37; com/ichi2/compat/CompatHelper.java:35-36', 'SOURCE')

UNREACHABLE['CompatV10.flushWebViewCookies'] = ('closed_by_api_level',
  'CompatV21 overrides it (CookieManager.flush). The base body (CookieSyncManager.sync) does not run on API 27.',
  'com/ichi2/compat/CompatV10.java:88-90; com/ichi2/compat/CompatV21.java:31-34; com/ichi2/compat/CompatHelper.java:35-36', 'SOURCE')

UNREACHABLE['CompatV10.getPreferenceSubscreenIntent'] = ('closed_by_api_level',
  'CompatV11 overrides it. The base body (legacy headers, action only) does not run on API 11 and up, including API 27.',
  'com/ichi2/compat/CompatV10.java:183-188; com/ichi2/compat/CompatV11.java:40-49; com/ichi2/compat/CompatHelper.java:45-46', 'SOURCE')

UNREACHABLE['CompatV10.isImmersiveSystemUiVisible'] = ('closed_by_api_level',
  'CompatV19 overrides it (SYSTEM_UI_FLAG_HIDE_NAVIGATION check). The base body (always false) does not run on API 27.',
  'com/ichi2/compat/CompatV10.java:196-198; com/ichi2/compat/CompatV19.java:90-93', 'SOURCE')

UNREACHABLE['CompatV10.openUrl'] = ('closed_by_api_level',
  'CompatV16 overrides it (Custom Tabs). The base body (CustomTabsFallback.openUri) does not run on API 27.',
  'com/ichi2/compat/CompatV10.java:132-134; com/ichi2/compat/CompatV16.java:76-87; com/ichi2/anki/AnkiActivity.java:322-323', 'SOURCE')

UNREACHABLE['CompatV10.restartActivityInvalidateBackstack'] = ('closed_by_api_level',
  'CompatV11 overrides it (TaskStackBuilder restart). The base body runs only on API 10, below the CompatV11 threshold.',
  'com/ichi2/compat/CompatV10.java:105-111; com/ichi2/compat/CompatV11.java:24-32; com/ichi2/compat/CompatHelper.java:45-46', 'SOURCE')

UNREACHABLE['CompatV10.setFullScreen'] = ('closed_by_api_level',
  'CompatV19 overrides it (sticky immersive flags, no super call). The base body does not run on API 27.',
  'com/ichi2/compat/CompatV10.java:113-120; com/ichi2/compat/CompatV19.java:25-26', 'SOURCE')

UNREACHABLE['CompatV10.setHTML5MediaAutoPlay'] = ('closed_by_api_level',
  'CompatV17 overrides it (setMediaPlaybackRequiresUserGesture). The empty base body does not run on API 27.',
  'com/ichi2/compat/CompatV10.java:93-95; com/ichi2/compat/CompatV17.java:13-16', 'SOURCE')

UNREACHABLE['CompatV10.setSelectableBackground'] = ('closed_by_api_level',
  'CompatV21 overrides it (ripple effect). The base body (colorBackground) does not run on API 27.',
  'com/ichi2/compat/CompatV10.java:123-130; com/ichi2/compat/CompatV21.java:14-21', 'SOURCE')

UNREACHABLE['CompatV10.setStatusBarColor'] = ('closed_by_api_level',
  'CompatV21 overrides it (window.setStatusBarColor). The empty base body does not run on API 27.',
  'com/ichi2/compat/CompatV10.java:191-193; com/ichi2/compat/CompatV21.java:36-39', 'SOURCE')

UNREACHABLE['CompatV10.setTtsOnUtteranceProgressListener'] = ('closed_by_api_level',
  'CompatV15 overrides it (UtteranceProgressListener). The API 27 route into the TTS init callback reaches CompatV15 (ReadText.java:195). The base body (deprecated OnUtteranceCompletedListener) does not run on API 27.',
  'com/ichi2/compat/CompatV10.java:57-67; com/ichi2/compat/CompatV15.java:13-30; com/ichi2/anki/ReadText.java:195', 'SOURCE')

UNREACHABLE['CompatV10.supportAddContentMenu'] = ('closed_by_api_level',
  'Called only from the DeckPicker fallback, which runs only when the add_content_menu view is absent. That id is in the layout-v14 resource only, so API 27 does not take the fallback.',
  'com/ichi2/compat/CompatV10.java:141-180; com/ichi2/anki/DeckPicker.java:391-404; res/layout-v14/floating_add_button.xml:7; res/layout/floating_add_button.xml:1-14', 'SOURCE')

UNREACHABLE['CompatV10$1.<init>'] = ('closed_by_api_level',
  'Created only inside CompatV10.setTtsOnUtteranceProgressListener, which CompatV15 overrides on API 27.',
  'com/ichi2/compat/CompatV10.java:57-67', 'SOURCE')

UNREACHABLE['CompatV10$1.onUtteranceCompleted'] = ('closed_by_api_level',
  'Body of the deprecated listener above. Never registered on API 27.',
  'com/ichi2/compat/CompatV10.java:58-66', 'SOURCE')

UNREACHABLE['CompatV10$2.<init>'] = ('closed_by_api_level',
  'Created only inside supportAddContentMenu, which is closed on API 27.',
  'com/ichi2/compat/CompatV10.java:147-178', 'SOURCE')

UNREACHABLE['CompatV10$2.onSelection'] = ('closed_by_api_level',
  'Runs only from the dialog opened by supportAddContentMenu. Closed with it.',
  'com/ichi2/compat/CompatV10.java:147-178', 'SOURCE')

UNREACHABLE['CompatV10$2$1.<init>'] = ('closed_by_api_level',
  'Created by the case 2 branch of onSelection. Closed with supportAddContentMenu.',
  'com/ichi2/compat/CompatV10.java:161-175', 'SOURCE')

UNREACHABLE['CompatV10$2$1.onClick'] = ('closed_by_api_level',
  'onPositive callback of the new-deck dialog. Reachable only through supportAddContentMenu, closed on API 27.',
  'com/ichi2/compat/CompatV10.java:165-173', 'SOURCE')

# ---- sup for part 072 (2026-10-28): on API 27 CompatHelper.java:35-36 selects CompatV21, whose chain (CompatV19, V17, V16, V15, V12, V11) overrides each CompatV10 member listed here; supportAddContentMenu is reached only by the DeckPicker fallback, which API 27 does not take (DeckPicker.java:391-404).
sup(('CompatV19.setFullScreen', 'CompatV10.setStatusBarColor'))
sup(('CompatV10$2.onSelection', 'CompatV10$2$1.<init>'))
sup(('CompatV10.setTtsOnUtteranceProgressListener', 'CompatV10$1.<init>'))
sup(('CompatV10.supportAddContentMenu', 'CompatV10$2.<init>'))
sup(('AbstractFlashcardViewer$21.handleMessage', 'CompatV10.setFullScreen'))
sup(('AbstractFlashcardViewer.onPause', 'CompatV10.flushWebViewCookies'))
sup(('AbstractFlashcardViewer.fillFlashcard', 'CompatV10.setHTML5MediaAutoPlay'))
sup(('AbstractFlashcardViewer.fillFlashcard@Previewer', 'CompatV10.setHTML5MediaAutoPlay'))
sup(('DeckPicker.onCreate', 'CompatV10.getPreferenceSubscreenIntent'))
sup(('Preferences$7.onPreferenceClick', 'CompatV10.getPreferenceSubscreenIntent'))
sup(('Preferences$3.onPreferenceClick', 'CompatV10.getPreferenceSubscreenIntent'))
sup(('Preferences$6.onPreferenceClick', 'CompatV10.getPreferenceSubscreenIntent'))
sup(('Reviewer$1.onTouch', 'CompatV10.isImmersiveSystemUiVisible'))
sup(('AbstractFlashcardViewer$MyGestureDetector.onFling', 'CompatV10.isImmersiveSystemUiVisible'))
sup(('AbstractFlashcardViewer$MyGestureDetector.onSingleTapConfirmed', 'CompatV10.isImmersiveSystemUiVisible'))
sup(('ReadText$3.onInit', 'CompatV10.setTtsOnUtteranceProgressListener'))
sup(('AnkiActivity.openUrl', 'CompatV10.openUrl'))
sup(('Reviewer.onCollectionLoaded', 'CompatV10.setFullScreen'))
sup(('DeckPicker$8.onClick', 'CompatV10.supportAddContentMenu'))
sup(('NavigationDrawerActivity$2.onCheckedChanged', 'CompatV10.restartActivityInvalidateBackstack'))
sup(('NavigationDrawerActivity.onActivityResult', 'CompatV10.restartActivityInvalidateBackstack'))
sup(('DeckAdapter.onBindViewHolder', 'CompatV10.setSelectableBackground'))
sup(('DiffEngine.wrapBad', 'CompatV10.detagged'))
sup(('DiffEngine.wrapGood', 'CompatV10.detagged'))
sup(('DiffEngine.wrapMissing', 'CompatV10.detagged'))

# ---- part 074 (2026-10-28)
# AnkiDroid batch 074 (LABEL helper). StepsPreference (9 methods), HtmlColors (4), StyledProgressDialog (9),
# Themes (7), DividerItemDecoration (2). The full row list is in graphs/AnkiDroid/parts/label_074.md.
#
# Route ownership:
# - Auto CALL edges (bytecode builder, auto_calls.json) are not written here: StepsPreference internal calls,
#   the convertFromJSON and convertToJSON callers, HtmlColors.invertColors and nameToHex, the StyledProgressDialog
#   four-argument to five-argument delegation, the Themes overload calls, and DividerItemDecoration.<init> from DeckPicker.onCreate.
# - No MG ids are used. Gates are the predefined constants STATE_SETTINGS (invertedColors preference) and STATE_DECK.

# --- StepsPreference: inflated from XML by the framework preference inflater (GenericInflater reflection on the
# --- (Context, AttributeSet) constructor). Both screens that show the steps tags.
e('S_DECKOPTIONS', 'StepsPreference.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'DeckOptions shows deck_options.xml, whose StepsPreference tags (newSteps, lapSteps) are inflated by the framework preference inflater through the (Context, AttributeSet) constructor, found by reflection',
  env=None,
  cls='non_standard',
  via=['PreferenceInflater reflection (GenericInflater constructor lookup)'],
  evidence='SRC res/xml/deck_options.xml:66-69, 138-141; SRC com/ichi2/anki/DeckOptions.java:499-500, 523; FW-SRC core/java/android/preference/GenericInflater.java:56-57, 378',
  note='Non-standard (XML instantiation). The destination is a method of this batch, so the edge belongs here. No gate.')

e('S_FILTEREDDECKOPTIONS', 'StepsPreference.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'FilteredDeckOptions shows cram_deck_options.xml for a filtered deck (else branch), whose StepsPreference tag (steps) is inflated through the (Context, AttributeSet) constructor by reflection',
  env=None,
  cls='non_standard',
  via=['PreferenceInflater reflection (GenericInflater constructor lookup)'],
  evidence='SRC res/xml/cram_deck_options.xml:50-54; SRC com/ichi2/anki/FilteredDeckOptions.java:369-378; FW-SRC core/java/android/preference/GenericInflater.java:56-57, 378',
  note='Non-standard (XML instantiation). The else branch runs only when the deck is a filtered deck, FilteredDeckOptions.java:370-374. No gate constant covers this; env and needs_state unset.')

# --- StepsPreference.onDialogClosed: framework dispatch from DialogPreference.onDismiss (no app call site).
e('S_DECKOPTIONS', 'StepsPreference.onDialogClosed', 'FRAMEWORK',
  'the user taps a steps preference and the dialog closes; DialogPreference.onDismiss calls onDialogClosed',
  env=None,
  evidence='SRC com/ichi2/preferences/StepsPreference.java:69-82; SRC com/ichi2/anki/DeckOptions.java:499-523; FW-SRC core/java/android/preference/DialogPreference.java:274-278, 318, 390-395',
  note='The dialog is shown by DialogPreference.onClick (showDialog at line 277). The dismiss listener is set at line 318. The dispatch to onDialogClosed is at line 395, a framework call with no app call site. No gate.')

e('S_FILTEREDDECKOPTIONS', 'StepsPreference.onDialogClosed', 'FRAMEWORK',
  'the same steps dialog on the filtered-deck options screen closes; DialogPreference.onDismiss calls onDialogClosed',
  env=None,
  evidence='SRC com/ichi2/preferences/StepsPreference.java:69-82; SRC com/ichi2/anki/FilteredDeckOptions.java:370-378; FW-SRC core/java/android/preference/DialogPreference.java:274-278, 318, 390-395',
  note='Same framework dispatch as the DeckOptions edge. No gate.')

# --- HtmlColors static initialiser: runs at the invokestatic of HtmlColors.invertColors in AbstractFlashcardViewer.updateCard.
e('S_REVIEWER', 'HtmlColors.<clinit>', 'FRAMEWORK',
  'the first night-mode card display initialises the HtmlColors class, which runs its static initialiser before invertColors',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1722, 2112-2118; SRC com/ichi2/themes/HtmlColors.java:10-16, 84-85; JVM class-initialisation rule is not in fw_src: INFERRED, source not read',
  note='Gate STATE_SETTINGS: the invertedColors preference (AbstractFlashcardViewer.java:1722) is needed for mNightMode (line 2112). The initialisation happens at the invokestatic in updateCard (line 2118), so the source is the reviewer page. INFERRED.')

# --- DividerItemDecoration.onDrawOver: support-library RecyclerView dispatch (not in fw_src).
e('S_DECKPICKER', 'DividerItemDecoration.onDrawOver', 'FRAMEWORK',
  'the deck list RecyclerView draws the item decoration over its rows',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/anki/DeckPicker.java:375-376; SRC com/ichi2/ui/DividerItemDecoration.java:28-44; support-library RecyclerView dispatch is not in fw_src: INFERRED, source not read',
  note='Gate STATE_DECK: decks (rows) are on screen, so onDrawOver has children to draw dividers under. INFERRED.')

# --- UNREACHABLE entries.
UNREACHABLE['StepsPreference.<init>(Context)'] = ('framework_never_calls',
  'No app caller; the framework inflater looks up only the (Context, AttributeSet) constructor',
  'com/ichi2/preferences/StepsPreference.java:51-55; FW-SRC core/java/android/preference/GenericInflater.java:56-57, 378',
  'SOURCE')

UNREACHABLE['StepsPreference.<init>(Context,AttributeSet,int)'] = ('framework_never_calls',
  'No app caller; the framework inflater uses only the (Context, AttributeSet) constructor',
  'com/ichi2/preferences/StepsPreference.java:37-41; FW-SRC core/java/android/preference/GenericInflater.java:56-57, 378',
  'SOURCE')

UNREACHABLE['HtmlColors.<init>'] = ('no_trigger_in_app',
  'HtmlColors has only static members; no code creates an instance',
  'com/ichi2/themes/HtmlColors.java:9-30; com/ichi2/anki/AbstractFlashcardViewer.java:88, 2118',
  'SOURCE')

UNREACHABLE['StyledProgressDialog.<init>'] = ('no_trigger_in_app',
  'The constructor runs only from new StyledProgressDialog(...), which does not occur in the source root; the static show overloads return MaterialDialog',
  'com/ichi2/themes/StyledProgressDialog.java:31-39, 53-73; com/ichi2/anki/DeckPicker.java:253-254',
  'SOURCE')

UNREACHABLE['StyledProgressDialog.animationEnabled'] = ('no_trigger_in_app',
  'Private static helper with no caller in the source root',
  'com/ichi2/themes/StyledProgressDialog.java:43-73, 76-82; com/ichi2/anki/AnkiActivity.java:119',
  'SOURCE')

UNREACHABLE['StyledProgressDialog.setMax'] = ('no_trigger_in_app',
  'No-op setter with no instance of StyledProgressDialog; the setMax callers are on SeekBar',
  'com/ichi2/themes/StyledProgressDialog.java:84-86; com/ichi2/ui/SeekBarPreference.java:70, 82',
  'SOURCE')

UNREACHABLE['StyledProgressDialog.setProgress'] = ('no_trigger_in_app',
  'No-op setter with no instance of StyledProgressDialog; the setProgress callers are on SeekBar',
  'com/ichi2/themes/StyledProgressDialog.java:89-91; com/ichi2/ui/SeekBarPreference.java:71, 83',
  'SOURCE')

UNREACHABLE['StyledProgressDialog.setProgressStyle'] = ('no_trigger_in_app',
  'No-op setter with no caller in the source root and no instance',
  'com/ichi2/themes/StyledProgressDialog.java:94-96',
  'SOURCE')

UNREACHABLE['StyledProgressDialog.show()'] = ('no_trigger_in_app',
  'Instance override of Dialog.show; no StyledProgressDialog instance is created, and the app uses the static show overloads',
  'com/ichi2/themes/StyledProgressDialog.java:42-50; com/ichi2/anki/DeckPicker.java:253-254',
  'SOURCE')

UNREACHABLE['StyledProgressDialog.show(Context,CharSequence,CharSequence)'] = ('no_trigger_in_app',
  'Three-argument overload; every app call site passes four arguments, so nothing calls it',
  'com/ichi2/themes/StyledProgressDialog.java:53-55; com/ichi2/anki/DeckPicker.java:253-254, 294-296, 316-317; com/ichi2/anki/StudyOptionsFragment.java:316-317',
  'SOURCE')

UNREACHABLE['Themes.<init>'] = ('no_trigger_in_app',
  'Themes has only static members; no code creates an instance',
  'com/ichi2/themes/Themes.java:30-41; com/ichi2/anki/NoteEditor.java:1110',
  'SOURCE')

UNREACHABLE['Themes.getResFromAttr(Context,int)'] = ('no_trigger_in_app',
  'Single-attribute overload; both app call sites pass an int array and resolve to the array overload',
  'com/ichi2/themes/Themes.java:94-97; com/ichi2/anki/NoteEditor.java:1110; com/ichi2/anki/AbstractFlashcardViewer.java:1580',
  'SOURCE')

# ---- part 075 (2026-10-28)
# AnkiDroid batch 075 (LABEL helper). SeekBarPreference (10 methods) and SlidingTabLayout with its inner classes
# InternalViewPagerListener (4) and TabClickListener (2): 29 methods in total. The full row list is in
# graphs/AnkiDroid/parts/label_075.md.
#
# Route ownership:
# - Automatic CALL edges (the SlidingTabLayout constructor chain, setViewPager to populateTabStrip, the listener
#   constructors, scrollToTab, createDefaultTabView) come from the builder and are not written here.
# - Page edges from S_PREFERENCES, S_CARDTEMPLATEEDITOR and S_STATISTICS into methods of this batch are written here,
#   because the destination is in the batch.
# - One edge with a source in this batch: SeekBarPreference.onStopTrackingTouch -> Preferences$SettingsFragment.onSharedPreferenceChanged.
# - Gates: STATE_COLLECTION (the dayOffset row is enabled only with an open collection; the tabs exist only after
#   onCollectionLoaded); STATE_SETTINGS (a later open, after dayOffset has been stored). No MG ids are needed here.
# - The support ViewPager is not in the dataset, so the pager dispatch edges are INFERRED (source not read).

# --- SeekBarPreference: page edges and the persist edge.
e('S_PREFERENCES', 'SeekBarPreference.<init>', 'FRAMEWORK',
  'Opening the reviewing settings screen inflates the day-offset SeekBarPreference.',
  env=None,
  evidence='SRC com/ichi2/ui/SeekBarPreference.java:34-43; SRC res/xml/preferences_reviewing.xml:36-39; FW-SRC core/java/android/preference/GenericInflater.java:376-385',
  note='Inflated when the reviewing subscreen is built (Preferences.java:242-243, 788). No gate: the screen opens without a collection.')

e('S_PREFERENCES', 'SeekBarPreference.onBindDialogView', 'FRAMEWORK',
  'Tap on the day-offset row; the framework calls the dialog binder after the view is built.',
  env=None,
  needs_state=STATE_COLLECTION,
  evidence='SRC com/ichi2/ui/SeekBarPreference.java:80-84; FW-SRC core/java/android/preference/DialogPreference.java:287-300; FW-SRC core/java/android/preference/Preference.java:1129-1135',
  note='Gate: the row is disabled when the collection is closed (Preferences.java:434-436), and Preference.performClick returns early when disabled (Preference.java:1131-1132).')

e('S_PREFERENCES', 'SeekBarPreference.onCreateDialogView', 'GUI',
  'Tap on the day-offset row opens the dialog.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Tap on the day-offset row opens the dialog.'],
  evidence='SRC com/ichi2/ui/SeekBarPreference.java:47-76; FW-SRC core/java/android/preference/PreferenceScreen.java:240-249',
  note='Gate: open collection (see onBindDialogView).')

e('S_PREFERENCES', 'SeekBarPreference.onPrepareDialogBuilder', 'FRAMEWORK',
  'Tap on the day-offset row; the framework calls the builder hook on the same tap.',
  env=None,
  needs_state=STATE_COLLECTION,
  evidence='SRC com/ichi2/ui/SeekBarPreference.java:135-140; FW-SRC core/java/android/preference/DialogPreference.java:287-306',
  note='Gate: open collection (see onBindDialogView).')

e('S_PREFERENCES', 'SeekBarPreference.onProgressChanged', 'GUI',
  'Drag the thumb or tap the bar in the open dialog.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Drag the thumb or tap the bar in the open dialog.'],
  evidence='SRC com/ichi2/ui/SeekBarPreference.java:99-105; FW-SRC core/java/android/widget/SeekBar.java:91-96',
  note='Gate: open collection (the dialog exists only on an enabled row). The fromTouch branch (lines 100-104) is taken.')

e('S_PREFERENCES', 'SeekBarPreference.onSetInitialValue', 'FRAMEWORK',
  'A later open of the screen, after dayOffset has been stored; the restore branch runs.',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/ui/SeekBarPreference.java:88-96, 116-119; FW-SRC core/java/android/preference/Preference.java:1547-1561',
  note='Gate: STATE_SETTINGS (dayOffset must have been stored by a prior setValue, which needs the collection: Preferences.java:400-402, 424-428).')

e('S_PREFERENCES', 'SeekBarPreference.onStartTrackingTouch', 'GUI',
  'Press the thumb of the open dialog SeekBar.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Press the thumb of the open dialog SeekBar.'],
  evidence='SRC com/ichi2/ui/SeekBarPreference.java:121-122; FW-SRC core/java/android/widget/SeekBar.java:112-117',
  note='Gate: open collection (see onBindDialogView). The body is empty.')

e('S_PREFERENCES', 'SeekBarPreference.onStopTrackingTouch', 'GUI',
  'Lift the finger after a drag; the dialog closes.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Lift the finger after a drag; the dialog closes.'],
  evidence='SRC com/ichi2/ui/SeekBarPreference.java:125-131; FW-SRC core/java/android/widget/SeekBar.java:119-125',
  note='Gate: open collection (see onBindDialogView). The body persists the value and dismisses the dialog (lines 127-130).')

e('SeekBarPreference.onStopTrackingTouch', 'Preferences$SettingsFragment.onSharedPreferenceChanged', 'FRAMEWORK',
  'persistInt commits the new value to SharedPreferences, which notifies the listener registered in SettingsFragment.onResume.',
  env=None,
  evidence='SRC com/ichi2/ui/SeekBarPreference.java:125-131; SRC com/ichi2/anki/Preferences.java:796, 811-812; FW-SRC core/java/android/preference/Preference.java:1716-1735, 1587-1595; FW-SRC core/java/android/app/SharedPreferencesImpl.java:547, 551-563',
  note='The notify is skipped when the stored value is unchanged (Preference.java:1721-1724). No gate beyond the open dialog.')

# --- SlidingTabLayout: page edges (card template editor and statistics) into the batch methods.
e('S_CARDTEMPLATEEDITOR', 'SlidingTabLayout.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'Opening the card template editor inflates the tab strip from its layout.',
  env=None,
  evidence='SRC res/layout/card_template_editor_activity.xml:21-24; SRC com/ichi2/anki/CardTemplateEditor.java:127-130; FW-SRC core/java/android/view/LayoutInflater.java:90-91, 615',
  note='No gate: setContentView in onCreate (line 130) runs before the collection loads.')

e('S_STATISTICS', 'SlidingTabLayout.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'Opening the statistics screen inflates the tab strip from its layout.',
  env=None,
  evidence='SRC res/layout/activity_anki_stats.xml:18-21; SRC com/ichi2/anki/Statistics.java:84-88; FW-SRC core/java/android/view/LayoutInflater.java:90-91, 615',
  note='No gate: setContentView in onCreate (line 86) runs before the collection loads.')

e('S_CARDTEMPLATEEDITOR', 'SlidingTabLayout.onAttachedToWindow', 'FRAMEWORK',
  'The window attaches the card template editor layout, which runs onAttachedToWindow.',
  env=None,
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:229-236; FW-SRC core/java/android/view/View.java:17420, 17445',
  note='No gate. scrollToTab runs only when mViewPager is set (line 233).')

e('S_STATISTICS', 'SlidingTabLayout.onAttachedToWindow', 'FRAMEWORK',
  'The window attaches the statistics layout, which runs onAttachedToWindow.',
  env=None,
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:229-236; FW-SRC core/java/android/view/View.java:17420, 17445',
  note='No gate. scrollToTab runs only when mViewPager is set (line 233).')

e('S_CARDTEMPLATEEDITOR', 'SlidingTabLayout$TabClickListener.onClick', 'GUI',
  'Tap a tab title in the card template editor.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Tap a tab title in the card template editor.'],
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:223, 304-314; SRC com/ichi2/anki/CardTemplateEditor.java:231-232',
  note='Gate: the tabs exist only after onCollectionLoaded (setViewPager at line 232).')

e('S_STATISTICS', 'SlidingTabLayout$TabClickListener.onClick', 'GUI',
  'Tap a tab title on the statistics screen.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Tap a tab title on the statistics screen.'],
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:223, 304-314; SRC com/ichi2/anki/Statistics.java:92, 125-126',
  note='Gate: the tabs exist only after onCollectionLoaded (setViewPager at line 126).')

e('S_CARDTEMPLATEEDITOR', 'SlidingTabLayout$InternalViewPagerListener.onPageScrollStateChanged', 'GUI',
  'Swipe between the card template pages.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Swipe between the card template pages.'],
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:282-288; SRC com/ichi2/anki/CardTemplateEditor.java:231-232',
  note='Gate: STATE_COLLECTION. INFERRED: the support ViewPager dispatch is not in the dataset (source not read).')

e('S_CARDTEMPLATEEDITOR', 'SlidingTabLayout$InternalViewPagerListener.onPageScrolled', 'GUI',
  'Swipe between the card template pages.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Swipe between the card template pages.'],
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:261-279; SRC com/ichi2/anki/CardTemplateEditor.java:231-232',
  note='Gate: STATE_COLLECTION. INFERRED: the support ViewPager dispatch is not in the dataset (source not read).')

e('S_CARDTEMPLATEEDITOR', 'SlidingTabLayout$InternalViewPagerListener.onPageSelected', 'GUI',
  'Swipe to another template page, or tap a tab.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Swipe to another template page, or tap a tab.'],
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:291-300, 309; SRC com/ichi2/anki/CardTemplateEditor.java:231-232',
  note='Gate: STATE_COLLECTION. INFERRED: the support ViewPager dispatch is not in the dataset (source not read).')

e('S_STATISTICS', 'SlidingTabLayout$InternalViewPagerListener.onPageScrollStateChanged', 'GUI',
  'Swipe between the statistics pages.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Swipe between the statistics pages.'],
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:282-288; SRC com/ichi2/anki/Statistics.java:125-126',
  note='Gate: STATE_COLLECTION. INFERRED: the support ViewPager dispatch is not in the dataset (source not read).')

e('S_STATISTICS', 'SlidingTabLayout$InternalViewPagerListener.onPageScrolled', 'GUI',
  'Swipe between the statistics pages.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Swipe between the statistics pages.'],
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:261-279; SRC com/ichi2/anki/Statistics.java:125-126',
  note='Gate: STATE_COLLECTION. INFERRED: the support ViewPager dispatch is not in the dataset (source not read).')

e('S_STATISTICS', 'SlidingTabLayout$InternalViewPagerListener.onPageSelected', 'GUI',
  'Swipe to another statistics page, or tap a tab.',
  env=None,
  needs_state=STATE_COLLECTION,
  gui=['Swipe to another statistics page, or tap a tab.'],
  evidence='SRC com/ichi2/ui/SlidingTabLayout.java:291-300, 309; SRC com/ichi2/anki/Statistics.java:125-126',
  note='Gate: STATE_COLLECTION. INFERRED: the support ViewPager dispatch is not in the dataset (source not read).')

# --- UNREACHABLE: no trigger in the app (every call site was grepped over src/main/java).
UNREACHABLE['SlidingTabLayout.<init>(Context)'] = ('no_trigger_in_app',
    'No new SlidingTabLayout(...) with one argument exists in the source root (grep finds no call site). LayoutInflater builds XML views with the (Context, AttributeSet) constructor only, so the one-argument form has no trigger.',
    'SRC com/ichi2/ui/SlidingTabLayout.java:83-85; FW-SRC core/java/android/view/LayoutInflater.java:90-91, 615',
    'SOURCE')

UNREACHABLE['SlidingTabLayout.setCustomTabColorizer'] = ('no_trigger_in_app',
    'No call site in the source root. The matches are its declaration and SlidingTabStrip.setCustomTabColorizer, a different method on a different class.',
    'SRC com/ichi2/ui/SlidingTabLayout.java:112-114; SRC com/ichi2/ui/SlidingTabStrip.java:90-93',
    'SOURCE')

UNREACHABLE['SlidingTabLayout.setCustomTabView'] = ('no_trigger_in_app',
    'No call site in the source root. Without it mTabViewLayoutId stays 0, so the custom-view branch is never taken and createDefaultTabView is always used.',
    'SRC com/ichi2/ui/SlidingTabLayout.java:149-152, 207-212',
    'SOURCE')

UNREACHABLE['SlidingTabLayout.setDividerColors'] = ('no_trigger_in_app',
    'No call site in the source root. The matches are its declaration and SlidingTabStrip.setDividerColors, a different method; the SlidingTabStrip calls at lines 75 and 105 are made inside SlidingTabStrip itself.',
    'SRC com/ichi2/ui/SlidingTabLayout.java:128-130; SRC com/ichi2/ui/SlidingTabStrip.java:73-76, 102-106',
    'SOURCE')

UNREACHABLE['SlidingTabLayout.setOnPageChangeListener'] = ('no_trigger_in_app',
    'No call site in the source root, so mViewPagerPageChangeListener stays null and the forwarding branches in InternalViewPagerListener are never taken.',
    'SRC com/ichi2/ui/SlidingTabLayout.java:139-141, 275-278, 285-287, 297-299',
    'SOURCE')

UNREACHABLE['SlidingTabLayout.setSelectedIndicatorColors'] = ('no_trigger_in_app',
    'No call site in the source root. The only other match is SlidingTabStrip.setSelectedIndicatorColors, a different method.',
    'SRC com/ichi2/ui/SlidingTabLayout.java:120-122; SRC com/ichi2/ui/SlidingTabStrip.java:95-100',
    'SOURCE')

# ---- part 073 (2026-10-28)
# AnkiDroid batch 073 (LABEL helper). CompatV19 and CompatV21 display paths, the CompatV16 openUrl route into the
# Custom Tabs helper, the Custom Tabs service callbacks, CustomDialogPreference and NumberRangePreference: 38 methods.
# The full row list is in graphs/AnkiDroid/parts/label_073.md.
#
# Route ownership:
# - The automatic CALL edges (auto_calls.json) are not written here. The rows name them.
# - Page edges (S_DECKOPTIONS, S_PREFERENCES, S_FILTEREDDECKOPTIONS) into methods of this batch are written here.
# - Edges into CustomTabActivityHelper.bindCustomTabsService (CustomTabActivityHelper.java:96-104) belong to the batch
#   that holds AnkiActivity.onStart. The support-library callbacks therefore have no inbound edge in this part.
# - Preferences.initPreference line 413 calls NumberRangePreference.setValue with no automatic edge. That edge belongs
#   to the batch that holds Preferences.initPreference and is not written here.
# - MG672 is the only MISSING GATE written on an edge here. MG673 to MG675 (Custom Tabs) appear in the rows only.

e('CompatV19$1.<init>', 'CompatV19$1.onSystemUiVisibilityChange', 'REGISTER',
  'decor view listener registered in setFullScreen; the framework calls it when the system UI visibility changes',
  evidence='SRC com/ichi2/compat/CompatV19.java:42-43; FW-SRC core/java/android/view/View.java:22684-22700; FW-SRC core/java/android/view/ViewRootImpl.java:5990-6007',
  note='MISSING GATE MG672: the callback fires when the system bars show or hide (a system or touch event). The app does not drive it and no constant fits, so env and needs_state are unset.')

e('CompatV19$2.<init>', 'CompatV19$2.onAnimationEnd', 'REGISTER',
  'AnimatorListenerAdapter set on the hide animation; the animator calls onAnimationEnd when the fade-out ends',
  evidence='SRC com/ichi2/compat/CompatV19.java:78-88; FW-SRC core/java/android/view/ViewPropertyAnimator.java:375-378, 1112-1122',
  note='setListener (CompatV19.java:82) stores the listener and ViewPropertyAnimator dispatches onAnimationEnd to it (1121-1122). No gate: the animation starts in hideViewWithAnimation.')

e('S_DECKOPTIONS', 'CustomDialogPreference.<init>', 'FRAMEWORK',
  'deck options screen inflates deck_options.xml, which holds the CustomDialogPreference entries',
  evidence='SRC com/ichi2/anki/DeckOptions.java:521-524; SRC res/xml/deck_options.xml:34-55; FW-SRC core/java/android/preference/GenericInflater.java:56-57',
  note='addPreferencesFromResource at DeckOptions.java:523 inflates the XML. The inflater uses the (Context, AttributeSet) constructor (GenericInflater.java:56-57). No gate.')

e('S_PREFERENCES', 'CustomDialogPreference.<init>', 'FRAMEWORK',
  'advanced preferences subscreen inflates preferences_advanced.xml, which holds the Reset Languages CustomDialogPreference',
  evidence='SRC com/ichi2/anki/Preferences.java:307-309; SRC res/xml/preferences_advanced.xml:106; FW-SRC core/java/android/preference/GenericInflater.java:56-57',
  note='addPreferencesFromResource at Preferences.java:308. No gate.')

e('S_DECKOPTIONS', 'CustomDialogPreference.onClick', 'GUI',
  'tap a deck option group preference (reset, remove, set subdecks) and then OK on its dialog',
  evidence='SRC com/ichi2/preferences/CustomDialogPreference.java:40-66; FW-SRC core/java/android/preference/DialogPreference.java:274-296, 386-388',
  gui=['tap a deck option group preference (reset, remove, set subdecks) and then OK on its dialog'],
  note='The preference opens its dialog through DialogPreference.onClick() (274-277) and showDialog (287-296). The positive button calls CustomDialogPreference.onClick (40). The preference title picks the branch (lines 42-56).')

e('S_PREFERENCES', 'CustomDialogPreference.onClick', 'GUI',
  'tap Reset Languages on the advanced preferences screen and then OK on its dialog',
  evidence='SRC com/ichi2/preferences/CustomDialogPreference.java:40-66; SRC res/xml/preferences_advanced.xml:106; FW-SRC core/java/android/preference/DialogPreference.java:274-296, 386-388',
  gui=['tap Reset Languages on the advanced preferences screen and then OK on its dialog'],
  note='Same dialog path as the deck options edge. Reset Languages takes the else branch (MetaDB.resetLanguages, CustomDialogPreference.java:59).')

e('S_PREFERENCES', 'NumberRangePreference.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'reviewing preferences subscreen inflates preferences_reviewing.xml, which holds NumberRangePreference entries',
  evidence='SRC com/ichi2/anki/Preferences.java:241-244; SRC res/xml/preferences_reviewing.xml:43-49; FW-SRC core/java/android/preference/GenericInflater.java:56-57',
  note='addPreferencesFromResource at Preferences.java:243. No gate.')

e('S_DECKOPTIONS', 'NumberRangePreference.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'deck options screen inflates deck_options.xml, which holds NumberRangePreference entries (lines 76-167)',
  evidence='SRC com/ichi2/anki/DeckOptions.java:521-524; SRC res/xml/deck_options.xml:76-167; FW-SRC core/java/android/preference/GenericInflater.java:56-57',
  note='addPreferencesFromResource at DeckOptions.java:523. No gate.')

e('S_FILTEREDDECKOPTIONS', 'NumberRangePreference.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'filtered deck options screen inflates cram_deck_options.xml, which holds one NumberRangePreference (line 26)',
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:376-379; SRC res/xml/cram_deck_options.xml:26; FW-SRC core/java/android/preference/GenericInflater.java:56-57',
  note='addPreferencesFromResource at FilteredDeckOptions.java:378. No gate.')

e('S_PREFERENCES', 'NumberRangePreference.getPersistedString', 'FRAMEWORK',
  'the screen reads the stored number preference value on load (Preference.dispatchSetInitialValue, then EditTextPreference.onSetInitialValue)',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/anki/Preferences.java:241-244; SRC com/ichi2/preferences/NumberRangePreference.java:74-77; FW-SRC core/java/android/preference/Preference.java:1547-1562; FW-SRC core/java/android/preference/EditTextPreference.java:158-161',
  note='Runs only when the key is stored (Preference.java:1555-1560). If a preference data store is set (1548-1549) the call runs without a stored value; whether DeckOptions sets a data store was not checked.')

e('S_DECKOPTIONS', 'NumberRangePreference.getPersistedString', 'FRAMEWORK',
  'the deck options screen reads the stored number preference value on load',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/anki/DeckOptions.java:521-524; SRC com/ichi2/preferences/NumberRangePreference.java:74-77; FW-SRC core/java/android/preference/Preference.java:1547-1562; FW-SRC core/java/android/preference/EditTextPreference.java:158-161',
  note='Same route as the reviewing screen. The key must be stored (Preference.java:1555-1560). The data-store branch (1548-1549) is not checked.')

e('S_FILTEREDDECKOPTIONS', 'NumberRangePreference.getPersistedString', 'FRAMEWORK',
  'the filtered deck options screen reads the stored number preference value on load',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:376-379; SRC com/ichi2/preferences/NumberRangePreference.java:74-77; FW-SRC core/java/android/preference/Preference.java:1547-1562; FW-SRC core/java/android/preference/EditTextPreference.java:158-161',
  note='Same route as the reviewing screen. The key must be stored (Preference.java:1555-1560). The data-store branch (1548-1549) is not checked.')

e('S_PREFERENCES', 'NumberRangePreference.onDialogClosed', 'GUI',
  'tap a number preference on the reviewing screen, then OK on its dialog',
  evidence='SRC com/ichi2/preferences/NumberRangePreference.java:58-64; FW-SRC core/java/android/preference/DialogPreference.java:274-296, 386-396',
  gui=['tap a number preference on the reviewing screen, then OK on its dialog'],
  note='DialogPreference.onDismiss calls onDialogClosed with the positive result (FW-SRC 395). showDialog sets up the dialog (287-296). Lines 61-62 call getValidatedRangeFromString and setValue (automatic edges).')

e('S_DECKOPTIONS', 'NumberRangePreference.onDialogClosed', 'GUI',
  'tap a number on the deck options screen, then OK on its dialog',
  evidence='SRC com/ichi2/preferences/NumberRangePreference.java:58-64; SRC com/ichi2/anki/DeckOptions.java:521-524; FW-SRC core/java/android/preference/DialogPreference.java:274-296, 386-396',
  gui=['tap a number on the deck options screen, then OK on its dialog'],
  note='Same dialog path as the reviewing screen (FW-SRC 395 calls onDialogClosed).')

e('S_FILTEREDDECKOPTIONS', 'NumberRangePreference.onDialogClosed', 'GUI',
  'tap a number on the filtered deck options screen, then OK on its dialog',
  evidence='SRC com/ichi2/preferences/NumberRangePreference.java:58-64; SRC com/ichi2/anki/FilteredDeckOptions.java:376-379; FW-SRC core/java/android/preference/DialogPreference.java:274-296, 386-396',
  gui=['tap a number on the filtered deck options screen, then OK on its dialog'],
  note='Same dialog path as the reviewing screen (FW-SRC 395 calls onDialogClosed).')

e('NumberRangePreference.setValue', 'NumberRangePreference.persistString', 'FRAMEWORK',
  'setValue writes the value through setText, which persists the text',
  evidence='SRC com/ichi2/preferences/NumberRangePreference.java:179-183; FW-SRC core/java/android/preference/EditTextPreference.java:88-94',
  note='setValue calls setText (181). EditTextPreference.setText calls persistString (FW-SRC 94), which dispatches to the override at NumberRangePreference.java:81-82 (persistInt). No gate.')

e('CustomTabActivityHelper.onServiceConnected', 'CustomTabActivityHelper.getSession', 'CALL',
  'the Custom Tabs service connected: onServiceConnected calls getSession to create a session',
  evidence='SRC com/ichi2/compat/customtabs/CustomTabActivityHelper.java:120-125, 83-90',
  note='Direct call at line 124. Not in auto_calls.json: the exact-match inbound query for getSession lists only CompatV16.openUrl (line 79). Gate MG673 applies to the callback, not to this call.')

# UNREACHABLE entries. Source references are printed lines in the .md rows.
UNREACHABLE['CustomTabsHelper.<init>'] = ('no_trigger_in_app', 'private empty constructor; no caller in the source root (grep for "new CustomTabsHelper" and "CustomTabsHelper()" finds only the declaration)', 'com/ichi2/compat/customtabs/CustomTabsHelper.java:47', 'SOURCE')
UNREACHABLE['CustomTabsHelper.getPackages'] = ('no_trigger_in_app', 'no caller in the source root (grep for CustomTabsHelper.getPackages finds only the declaration at line 144)', 'com/ichi2/compat/customtabs/CustomTabsHelper.java:144-146', 'SOURCE')
UNREACHABLE['NumberRangePreference.<init>(Context)'] = ('framework_never_calls', 'the inflater selects constructors with the (Context, AttributeSet) signature only (GenericInflater.java:56-57); no app code calls new NumberRangePreference(context)', 'com/ichi2/preferences/NumberRangePreference.java:50-55; core/java/android/preference/GenericInflater.java:56-57', 'SOURCE')
UNREACHABLE['NumberRangePreference.<init>(Context,AttributeSet,int)'] = ('framework_never_calls', 'the inflater uses the (Context, AttributeSet) signature only (GenericInflater.java:56-57); the (Context, AttributeSet) constructor calls super(context, attrs) and does not chain to this one; no app caller', 'com/ichi2/preferences/NumberRangePreference.java:34-39; core/java/android/preference/GenericInflater.java:56-57', 'SOURCE')

# ---- part 078 (2026-10-28)
UNREACHABLE['Base64$OutputStream.suspendEncoding'] = ('no_trigger_in_app', 'No code under src/ calls suspendEncoding(); the only hits are the method itself and the boolean field of the same name. The stream class is created only inside the public static methods of com.ichi2.utils.Base64 (encodeObject, encodeBytesToBytes, encodeToFile, decodeToFile), and none of those has a caller under src/ (the name Base64 is referenced in no file under src/ except Base64.java).', 'SRC com/ichi2/utils/Base64.java:466-468, 499-500, 513-514, 680-681, 703-706, 730-731, 757-761, 1232-1241, 1268-1273, 1676-1680, 1860-1881', 'SOURCE')
UNREACHABLE['Base64$OutputStream.write(int)'] = ('no_trigger_in_app', 'The only call of write(int) under src/ is inside write(byte[],int,int) (the loop at com/ichi2/utils/Base64.java:1814). write(byte[],int,int) is used only by the stream writes at Base64.java:761 (gzos.write, the GZIP stream over this stream), 1241 and 1273 (bos.write on this stream), which sit in encodeBytesToBytes, encodeToFile and decodeToFile. Those public static methods have no caller under src/ (the name Base64 is referenced in no file under src/ except Base64.java).', 'SRC com/ichi2/utils/Base64.java:1754-1758, 1806-1816, 757-761, 1232-1241, 1268-1273', 'SOURCE')
UNREACHABLE['Base64$OutputStream.write(byte[],int,int)'] = ('no_trigger_in_app', 'No instance of the stream is created anywhere in the app. It is created only at com/ichi2/utils/Base64.java:514, 758, 1240 and 1272, inside encodeObject, encodeBytesToBytes, encodeToFile and decodeToFile, and none of those public static methods has a caller under src/ (the name Base64 is referenced in no file under src/ except Base64.java). The writes on this stream under src/ are only Base64.java:761 (through the GZIP stream), 1241 and 1273, all inside those methods.', 'SRC com/ichi2/utils/Base64.java:513-514, 757-761, 1232-1241, 1268-1273, 1806-1816', 'SOURCE')

# ---- sup for part 078 (2026-10-28): write(byte[],int,int) is itself UNREACHABLE (its stream is created only in closed Base64 static methods), so its loop call at Base64.java:1814 cannot make write(int) reachable.
sup(('Base64$OutputStream.write(byte[],int,int)', 'Base64$OutputStream.write(int)'))

# ---- part 076 (2026-10-28)
e('S_STATISTICS', 'SlidingTabStrip.onDraw', 'FRAMEWORK',
  'the statistics screen draws its sliding tab strip (the tab underline, bottom border and dividers)',
  env=None,
  evidence='SRC com/ichi2/anki/Statistics.java:86, 125-126; res/layout/activity_anki_stats.xml:18-21 (src/main); SRC com/ichi2/ui/SlidingTabLayout.java:101-102; SRC com/ichi2/ui/SlidingTabStrip.java:62, 115-118; FW-SRC core/java/android/view/ViewGroup.java:4235-4236; FW-SRC core/java/android/view/View.java:9807-9809, 13438-13449, 18833, 19056-19063, 19163, 19188-19192',
  note='The strip is a child of SlidingTabLayout (added at SlidingTabLayout.java:102). The view tree draws it through ViewGroup.drawChild (ViewGroup.java:4235-4236). onDraw runs because setWillNotDraw(false) (SlidingTabStrip.java:62) clears the skip-draw flag (View.java:13438-13449). No gate: the strip draws whenever the statistics screen is shown.')

e('S_CARDTEMPLATEEDITOR', 'SlidingTabStrip.onDraw', 'FRAMEWORK',
  'the card template editor draws its sliding tab strip (the tab underline, bottom border and dividers)',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:130, 231-232; res/layout/card_template_editor_activity.xml:21-24 (src/main); SRC com/ichi2/ui/SlidingTabLayout.java:101-102; SRC com/ichi2/ui/SlidingTabStrip.java:62, 115-118; FW-SRC core/java/android/view/ViewGroup.java:4235-4236; FW-SRC core/java/android/view/View.java:9807-9809, 13438-13449, 18833, 19056-19063, 19163, 19188-19192',
  note='The strip is a child of SlidingTabLayout (added at SlidingTabLayout.java:102). The view tree draws it through ViewGroup.drawChild (ViewGroup.java:4235-4236). onDraw runs because setWillNotDraw(false) (SlidingTabStrip.java:62) clears the skip-draw flag (View.java:13438-13449). No gate: the strip draws whenever the card template editor is shown.')

UNREACHABLE['SlidingTabStrip.blendColors'] = ('branch_never_taken',
  'The only call is at SlidingTabStrip.java:134, inside the branch where color != nextColor (line 133). Both colours come from the same colorizer, and its indicator array has one element: it is set once at line 74 to DEFAULT_SELECTED_INDICATOR_COLOR (line 33). getIndicatorColor returns mIndicatorColors[position % length] (lines 190-192), so nextColor always equals color. mCustomTabColorizer becomes non-null only at line 91, in setCustomTabColorizer, which has no caller. The other writer of the indicator array, setSelectedIndicatorColors, has no caller either.',
  'com/ichi2/ui/SlidingTabStrip.java:33, 74, 90-98, 129-134, 190-192; com/ichi2/ui/SlidingTabLayout.java:112-114, 120-122 (no callers)',
  'SOURCE')

UNREACHABLE['SlidingTabStrip.setCustomTabColorizer'] = ('no_trigger_in_app',
  'The only caller is SlidingTabLayout.setCustomTabColorizer (SlidingTabLayout.java:113). That public method has no caller in the source root: its definition is at line 112, and its own javadoc (lines 105-111) is text, not a call. The layout files name the view only (activity_anki_stats.xml:18-21; card_template_editor_activity.xml:21-24).',
  'com/ichi2/ui/SlidingTabStrip.java:90-93; com/ichi2/ui/SlidingTabLayout.java:105-114; res/layout/activity_anki_stats.xml:18-21 (src/main); res/layout/card_template_editor_activity.xml:21-24 (src/main)',
  'SOURCE')

UNREACHABLE['SlidingTabStrip.setDividerColors'] = ('no_trigger_in_app',
  'The only caller is SlidingTabLayout.setDividerColors (SlidingTabLayout.java:129), which has no caller in the source root: its definition is at line 128, and a link to it at line 109 is javadoc text, not a call.',
  'com/ichi2/ui/SlidingTabStrip.java:102-107; com/ichi2/ui/SlidingTabLayout.java:109, 128-130',
  'SOURCE')

UNREACHABLE['SlidingTabStrip.setSelectedIndicatorColors'] = ('no_trigger_in_app',
  'The only caller is SlidingTabLayout.setSelectedIndicatorColors (SlidingTabLayout.java:121), which has no caller in the source root: its definition is at line 120, and its own javadoc (lines 116-119) and a link at line 109 are text, not calls.',
  'com/ichi2/ui/SlidingTabStrip.java:95-100; com/ichi2/ui/SlidingTabLayout.java:109, 116-122',
  'SOURCE')

UNREACHABLE['Upgrade.<init>'] = ('no_trigger_in_app',
  'Upgrade declares no constructor, so only the implicit default one exists, and no code creates an instance. The class holds only the static method upgradeJSONIfNecessary (Upgrade.java:11). In the source root the class is referenced only by its declaration (Upgrade.java:9), the import (CardBrowser.java:70) and the static call (CardBrowser.java:399).',
  'com/ichi2/upgrade/Upgrade.java:9-11; com/ichi2/anki/CardBrowser.java:70, 399',
  'SOURCE')

# ---- sup for part 076 (2026-10-28): each destination is UNREACHABLE; the call sites are in a branch never taken or in a setter with no caller.
sup(('SlidingTabStrip.onDraw', 'SlidingTabStrip.blendColors'))
sup(('SlidingTabLayout.setCustomTabColorizer', 'SlidingTabStrip.setCustomTabColorizer'))
sup(('SlidingTabLayout.setDividerColors', 'SlidingTabStrip.setDividerColors'))
sup(('SlidingTabLayout.setSelectedIndicatorColors', 'SlidingTabStrip.setSelectedIndicatorColors'))

# ---- part 077 (2026-10-28)
UNREACHABLE['Base64.<clinit>'] = ('no_trigger_in_app', 'Static initializer of Base64 (constants and lookup tables). It runs only when the class is first used, which needs a static member access or an instance from app code. No app source file other than Base64.java names the class.', 'com/ichi2/utils/Base64.java:50-273', 'SOURCE')
UNREACHABLE['Base64.<init>'] = ('no_trigger_in_app', 'Private constructor (defeats instantiation). No code creates an instance: the file has no new Base64(...) and no other file names the class.', 'com/ichi2/utils/Base64.java:311-312', 'SOURCE')
UNREACHABLE['Base64.decode(String)'] = ('no_trigger_in_app', 'No call site. The name occurs only as its declaration and in javadoc, and the class has no caller outside the file.', 'com/ichi2/utils/Base64.java:1049-1051', 'SOURCE')
UNREACHABLE['Base64.decode(String,int)'] = ('no_trigger_in_app', 'Called from decode(String) (line 1050) and from decodeToObject(String,int,ClassLoader) (line 1167). Both callers have no route (see their rows).', 'com/ichi2/utils/Base64.java:1064-1131; call sites 1050, 1167', 'SOURCE')
UNREACHABLE['Base64.decode(byte[])'] = ('no_trigger_in_app', 'No call site. The name occurs only as its declaration, and the class has no caller outside the file.', 'com/ichi2/utils/Base64.java:949-957', 'SOURCE')
UNREACHABLE['Base64.decode(byte[],int,int,int)'] = ('no_trigger_in_app', 'Called from decode(byte[]) (line 952) and from decode(String,int) (line 1080). Both callers have no route.', 'com/ichi2/utils/Base64.java:974-1038; call sites 952, 1080', 'SOURCE')
UNREACHABLE['Base64.decode4to3'] = ('no_trigger_in_app', 'Called from decode(byte[],int,int,int) (line 1018), from Base64$InputStream.read() (line 1589) and from Base64$OutputStream.write(int) (line 1785). read() and write(int) run only on Base64.InputStream and Base64.OutputStream instances, and those are created only in methods with no route (see their rows).', 'com/ichi2/utils/Base64.java:867-936; call sites 1018, 1589, 1785', 'SOURCE')
UNREACHABLE['Base64.decodeFileToFile'] = ('no_trigger_in_app', 'No call site.', 'com/ichi2/utils/Base64.java:1439-1456', 'SOURCE')
UNREACHABLE['Base64.decodeFromFile'] = ('no_trigger_in_app', 'Called only from decodeFileToFile (line 1441), which has no call site.', 'com/ichi2/utils/Base64.java:1300-1343; call site 1441', 'SOURCE')
UNREACHABLE['Base64.decodeToFile'] = ('no_trigger_in_app', 'No call site.', 'com/ichi2/utils/Base64.java:1268-1285', 'SOURCE')
UNREACHABLE['Base64.decodeToObject(String)'] = ('no_trigger_in_app', 'No call site. Its body (line 1146) calls the three-argument overload.', 'com/ichi2/utils/Base64.java:1144-1147; call site 1146', 'SOURCE')
UNREACHABLE['Base64.decodeToObject(String,int,ClassLoader)'] = ('no_trigger_in_app', 'Called only from decodeToObject(String) (line 1146), which has no call site. It also creates the anonymous ObjectInputStream subclass Base64$1 (line 1184).', 'com/ichi2/utils/Base64.java:1163-1216; call site 1146', 'SOURCE')
UNREACHABLE['Base64.encode(ByteBuffer,ByteBuffer)'] = ('no_trigger_in_app', 'No call site.', 'com/ichi2/utils/Base64.java:414-424', 'SOURCE')
UNREACHABLE['Base64.encode(ByteBuffer,CharBuffer)'] = ('no_trigger_in_app', 'No call site.', 'com/ichi2/utils/Base64.java:436-448', 'SOURCE')
UNREACHABLE['Base64.encode3to4(byte[],int,int,byte[],int,int)'] = ('no_trigger_in_app', 'Called from encode3to4(byte[],byte[],int,int) (line 330), from encodeBytesToBytes(byte[],int,int,int) (lines 812 and 823), and from Base64$InputStream.read() (line 1561). Those callers have no route (see their rows).', 'com/ichi2/utils/Base64.java:356-402; call sites 330, 812, 823, 1561', 'SOURCE')
UNREACHABLE['Base64.encode3to4(byte[],byte[],int,int)'] = ('no_trigger_in_app', 'Called from encode(ByteBuffer,ByteBuffer) (line 421), from encode(ByteBuffer,CharBuffer) (line 443), from Base64$OutputStream.write(int) (line 1766) and from flushBase64 (line 1828). The two ByteBuffer methods have no call site, and the two OutputStream methods run only on instances that no route creates.', 'com/ichi2/utils/Base64.java:329-332; call sites 421, 443, 1766, 1828', 'SOURCE')
UNREACHABLE['Base64.encodeBytes(byte[])'] = ('no_trigger_in_app', 'No call site. Its body (line 575) calls the four-argument overload.', 'com/ichi2/utils/Base64.java:569-581; call site 575', 'SOURCE')
UNREACHABLE['Base64.encodeBytes(byte[],int)'] = ('no_trigger_in_app', 'No call site. Its body (line 614) calls the four-argument overload.', 'com/ichi2/utils/Base64.java:613-615; call site 614', 'SOURCE')
UNREACHABLE['Base64.encodeBytes(byte[],int,int)'] = ('no_trigger_in_app', 'No call site. Its body (line 639) calls the four-argument overload.', 'com/ichi2/utils/Base64.java:633-645; call site 639', 'SOURCE')
UNREACHABLE['Base64.encodeBytes(byte[],int,int,int)'] = ('no_trigger_in_app', 'Called from the one-, two- and three-argument encodeBytes overloads (lines 575, 614, 639). Those have no call site.', 'com/ichi2/utils/Base64.java:680-691; call sites 575, 614, 639', 'SOURCE')
UNREACHABLE['Base64.encodeBytesToBytes(byte[])'] = ('no_trigger_in_app', 'No call site. Its body (line 706) calls the four-argument overload.', 'com/ichi2/utils/Base64.java:703-711; call site 706', 'SOURCE')
UNREACHABLE['Base64.encodeBytesToBytes(byte[],int,int,int)'] = ('no_trigger_in_app', 'Called from encodeBytes(byte[],int,int,int) (line 681) and from encodeBytesToBytes(byte[]) (line 706). Both callers have no route.', 'com/ichi2/utils/Base64.java:730-841; call sites 681, 706', 'SOURCE')
UNREACHABLE['Base64.encodeFileToFile'] = ('no_trigger_in_app', 'No call site. Its body (line 1413) calls encodeFromFile.', 'com/ichi2/utils/Base64.java:1411-1428; call site 1413', 'SOURCE')
UNREACHABLE['Base64.encodeFromFile'] = ('no_trigger_in_app', 'Called only from encodeFileToFile (line 1413), which has no call site.', 'com/ichi2/utils/Base64.java:1358-1400; call site 1413', 'SOURCE')
UNREACHABLE['Base64.encodeObject(Serializable)'] = ('no_trigger_in_app', 'No call site. Its body (line 467) calls the two-argument overload.', 'com/ichi2/utils/Base64.java:466-468; call site 467', 'SOURCE')
UNREACHABLE['Base64.encodeObject(Serializable,int)'] = ('no_trigger_in_app', 'Called only from encodeObject(Serializable) (line 467), which has no call site.', 'com/ichi2/utils/Base64.java:499-558; call sites 467, 514, 540', 'SOURCE')
UNREACHABLE['Base64.encodeToFile'] = ('no_trigger_in_app', 'No call site. Its body creates Base64.OutputStream at line 1240.', 'com/ichi2/utils/Base64.java:1232-1253; call site 1240', 'SOURCE')
UNREACHABLE['Base64.getAlphabet'] = ('no_trigger_in_app', 'Private helper. Called only from encode3to4 with six arguments (line 359), which is reached only through encode3to4 with four arguments, which has no route.', 'com/ichi2/utils/Base64.java:283-291; call site 359', 'SOURCE')
UNREACHABLE['Base64.getDecodabet'] = ('no_trigger_in_app', 'Private helper. Called from decode4to3 (line 887), from decode(byte[],int,int,int) (line 993), and from the InputStream and OutputStream two-argument constructors (lines 1529 and 1741). Those callers have no route.', 'com/ichi2/utils/Base64.java:299-307; call sites 887, 993, 1529, 1741', 'SOURCE')
UNREACHABLE['Base64$1.<init>'] = ('no_trigger_in_app', 'Implicit constructor of the anonymous ObjectInputStream subclass, created at line 1184 inside decodeToObject(String,int,ClassLoader). That method is reached only from decodeToObject(String), which has no call site.', 'com/ichi2/utils/Base64.java:1184-1195; call site 1184', 'SOURCE')
UNREACHABLE['Base64$1.resolveClass'] = ('no_trigger_in_app', 'Override in the anonymous ObjectInputStream subclass. Only an instance created at line 1184 can call it, and that code has no route.', 'com/ichi2/utils/Base64.java:1186-1194', 'SOURCE')
UNREACHABLE['Base64$InputStream.<init>(InputStream)'] = ('no_trigger_in_app', 'No call site. The file creates Base64.InputStream only with the two-argument constructor (lines 1319 and 1377).', 'com/ichi2/utils/Base64.java:1494-1496', 'SOURCE')
UNREACHABLE['Base64$InputStream.<init>(InputStream,int)'] = ('no_trigger_in_app', 'Called from decodeFromFile (line 1319) and encodeFromFile (line 1377). Those are reached only from decodeFileToFile (line 1441) and encodeFileToFile (line 1413), which have no call site.', 'com/ichi2/utils/Base64.java:1519-1530; call sites 1319, 1377', 'SOURCE')
UNREACHABLE['Base64$InputStream.read()'] = ('no_trigger_in_app', 'Called from read(byte[],int,int) (line 1652). Instances are created only at lines 1319 and 1377, in methods with no route (see Base64$InputStream.<init>(InputStream,int)).', 'com/ichi2/utils/Base64.java:1540-1634; call site 1652', 'SOURCE')
UNREACHABLE['Base64$InputStream.read(byte[],int,int)'] = ('no_trigger_in_app', 'Called from decodeFromFile (line 1323) and encodeFromFile (line 1381), which have no route.', 'com/ichi2/utils/Base64.java:1648-1663; call sites 1323, 1381', 'SOURCE')
UNREACHABLE['Base64$OutputStream.<init>(OutputStream)'] = ('no_trigger_in_app', 'No call site. The file creates Base64.OutputStream only with the two-argument constructor (lines 514, 758, 1240, 1272).', 'com/ichi2/utils/Base64.java:1705-1707', 'SOURCE')
UNREACHABLE['Base64$OutputStream.<init>(OutputStream,int)'] = ('no_trigger_in_app', 'Called from encodeObject(Serializable,int) (line 514), encodeBytesToBytes(byte[],int,int,int) (line 758), encodeToFile (line 1240) and decodeToFile (line 1272). Those methods have no route.', 'com/ichi2/utils/Base64.java:1730-1742; call sites 514, 758, 1240, 1272', 'SOURCE')
UNREACHABLE['Base64$OutputStream.close'] = ('no_trigger_in_app', 'Called from encodeObject(Serializable,int) (line 540), encodeBytesToBytes(byte[],int,int,int) (line 775), encodeToFile (line 1248) and decodeToFile (line 1280). Those callers have no route.', 'com/ichi2/utils/Base64.java:1845-1855; call sites 540, 775, 1248, 1280', 'SOURCE')
UNREACHABLE['Base64$OutputStream.flushBase64'] = ('no_trigger_in_app', 'Called from close() (line 1847) and suspendEncoding() (line 1866). Both are instance methods of Base64.OutputStream, and no route creates such an instance.', 'com/ichi2/utils/Base64.java:1825-1836; call sites 1847, 1866', 'SOURCE')
UNREACHABLE['Base64$OutputStream.resumeEncoding'] = ('no_trigger_in_app', 'No call site in the file. It is an instance method that only a Base64.OutputStream instance could call, and no route creates one.', 'com/ichi2/utils/Base64.java:1877-1879', 'SOURCE')

# ---- sup for part 077 (2026-10-28): every Base64 method is UNREACHABLE (no app file names Base64), so these bytecode calls between them create no route.
sup(('Base64$OutputStream.<init>(OutputStream,int)', 'Base64.<clinit>'))
sup(('Base64$OutputStream.write(int)', 'Base64.<clinit>'))
sup(('Base64$OutputStream.flushBase64', 'Base64.<clinit>'))
sup(('Base64$InputStream.<init>(InputStream,int)', 'Base64.<clinit>'))
sup(('Base64$InputStream.read()', 'Base64.<clinit>'))
sup(('Base64.decode(String)', 'Base64.decode(String,int)'))
sup(('Base64.decodeToObject(String,int,ClassLoader)', 'Base64.decode(String,int)'))
sup(('Base64.decode(byte[])', 'Base64.decode(byte[],int,int,int)'))
sup(('Base64.decode(String,int)', 'Base64.decode(byte[],int,int,int)'))
sup(('Base64$OutputStream.write(int)', 'Base64.decode4to3'))
sup(('Base64$InputStream.read()', 'Base64.decode4to3'))
sup(('Base64.decode(byte[],int,int,int)', 'Base64.decode4to3'))
sup(('Base64.decodeFileToFile', 'Base64.decodeFromFile'))
sup(('Base64.decodeToObject(String)', 'Base64.decodeToObject(String,int,ClassLoader)'))
sup(('Base64$InputStream.read()', 'Base64.encode3to4(byte[],int,int,byte[],int,int)'))
sup(('Base64.encode3to4(byte[],byte[],int,int)', 'Base64.encode3to4(byte[],int,int,byte[],int,int)'))
sup(('Base64.encodeBytesToBytes(byte[],int,int,int)', 'Base64.encode3to4(byte[],int,int,byte[],int,int)'))
sup(('Base64$OutputStream.write(int)', 'Base64.encode3to4(byte[],byte[],int,int)'))
sup(('Base64$OutputStream.flushBase64', 'Base64.encode3to4(byte[],byte[],int,int)'))
sup(('Base64.encode(ByteBuffer,ByteBuffer)', 'Base64.encode3to4(byte[],byte[],int,int)'))
sup(('Base64.encode(ByteBuffer,CharBuffer)', 'Base64.encode3to4(byte[],byte[],int,int)'))
sup(('Base64.encodeBytes(byte[])', 'Base64.encodeBytes(byte[],int,int,int)'))
sup(('Base64.encodeBytes(byte[],int)', 'Base64.encodeBytes(byte[],int,int,int)'))
sup(('Base64.encodeBytes(byte[],int,int)', 'Base64.encodeBytes(byte[],int,int,int)'))
sup(('Base64.encodeBytes(byte[],int,int,int)', 'Base64.encodeBytesToBytes(byte[],int,int,int)'))
sup(('Base64.encodeBytesToBytes(byte[])', 'Base64.encodeBytesToBytes(byte[],int,int,int)'))
sup(('Base64.encodeFileToFile', 'Base64.encodeFromFile'))
sup(('Base64.encodeObject(Serializable)', 'Base64.encodeObject(Serializable,int)'))
sup(('Base64.encode3to4(byte[],int,int,byte[],int,int)', 'Base64.getAlphabet'))
sup(('Base64$OutputStream.<init>(OutputStream,int)', 'Base64.getDecodabet'))
sup(('Base64$InputStream.<init>(InputStream,int)', 'Base64.getDecodabet'))
sup(('Base64.decode4to3', 'Base64.getDecodabet'))
sup(('Base64.decode(byte[],int,int,int)', 'Base64.getDecodabet'))
sup(('Base64.decodeToObject(String,int,ClassLoader)', 'Base64$1.<init>'))
sup(('Base64$InputStream.<init>(InputStream)', 'Base64$InputStream.<init>(InputStream,int)'))
sup(('Base64.decodeFromFile', 'Base64$InputStream.<init>(InputStream,int)'))
sup(('Base64.encodeFromFile', 'Base64$InputStream.<init>(InputStream,int)'))
sup(('Base64$InputStream.read(byte[],int,int)', 'Base64$InputStream.read()'))
sup(('Base64.decodeFromFile', 'Base64$InputStream.read(byte[],int,int)'))
sup(('Base64.encodeFromFile', 'Base64$InputStream.read(byte[],int,int)'))
sup(('Base64$OutputStream.<init>(OutputStream)', 'Base64$OutputStream.<init>(OutputStream,int)'))
sup(('Base64.encodeObject(Serializable,int)', 'Base64$OutputStream.<init>(OutputStream,int)'))
sup(('Base64.encodeBytesToBytes(byte[],int,int,int)', 'Base64$OutputStream.<init>(OutputStream,int)'))
sup(('Base64.encodeToFile', 'Base64$OutputStream.<init>(OutputStream,int)'))
sup(('Base64.decodeToFile', 'Base64$OutputStream.<init>(OutputStream,int)'))
sup(('Base64.encodeBytesToBytes(byte[],int,int,int)', 'Base64$OutputStream.close'))
sup(('Base64.encodeToFile', 'Base64$OutputStream.close'))
sup(('Base64.decodeToFile', 'Base64$OutputStream.close'))
sup(('Base64$OutputStream.close', 'Base64$OutputStream.flushBase64'))
sup(('Base64$OutputStream.suspendEncoding', 'Base64$OutputStream.flushBase64'))

# ---- part 079 (2026-10-28)
# AnkiDroid batch 079 (LABEL helper). 38 methods; the full row list is in graphs/AnkiDroid/parts/label_079.md.
# This part writes only UNREACHABLE entries (8, all no_trigger_in_app) and no e() edges (0).
# Source paths are relative to final_java_only/AnkiDroid/app/AnkiDroid-#4200/AnkiDroid/src/main/java.
# Text is repeated inline; no module-level names are defined.

UNREACHABLE['BitmapUtil.<init>'] = ('no_trigger_in_app', 'BitmapUtil has only static methods and no explicit constructor. A grep for new BitmapUtil under the source root finds no call site, so the default constructor is never invoked.', 'SRC com/ichi2/utils/BitmapUtil.java:35-93', 'SOURCE')

UNREACHABLE['ExifUtil.<init>'] = ('no_trigger_in_app', 'ExifUtil has only the static method rotateFromCamera and no explicit constructor. A grep for new ExifUtil under the source root finds no call site.', 'SRC com/ichi2/utils/ExifUtil.java:29-55', 'SOURCE')

UNREACHABLE['HttpUtility.<init>'] = ('no_trigger_in_app', 'HttpUtility has only the static method postReport and no explicit constructor. A grep for new HttpUtility under the source root finds no call site.', 'SRC com/ichi2/utils/HttpUtility.java:18-43', 'SOURCE')

UNREACHABLE['HttpUtility.postReport'] = ('no_trigger_in_app', 'postReport posts feedback reports with DefaultHttpClient. A grep for postReport under the source root finds no call site, so no in-app trigger reaches it.', 'SRC com/ichi2/utils/HttpUtility.java:19-42', 'SOURCE')

UNREACHABLE['LanguageUtil.<init>'] = ('no_trigger_in_app', 'LanguageUtil has only static members and no explicit constructor. A grep for new LanguageUtil under the source root finds no call site.', 'SRC com/ichi2/utils/LanguageUtil.java:27-67', 'SOURCE')

UNREACHABLE['LanguageUtil.getLocale()'] = ('no_trigger_in_app', 'The only caller under the source root is Utils.fmtPercentage(Double,int) at line 229. That method is called only from fmtPercentage(Double) at Utils.java:224, and no code under the source root calls fmtPercentage(Double), so the chain has no in-app trigger.', 'SRC com/ichi2/utils/LanguageUtil.java:41-43; SRC com/ichi2/libanki/Utils.java:223-232', 'SOURCE')

UNREACHABLE['DiffEngine$DiffAction.equals'] = ('no_trigger_in_app', 'The equals override runs only when a DiffAction is compared with equals, or through a collection contains, remove or indexOf. A grep under the source root finds no such comparison: the contains and remove calls act on Long sets and iterators, and DiffAction objects are compared by reference only.', 'SRC com/ichi2/utils/DiffEngine.java:1158-1164', 'SOURCE')

UNREACHABLE['DiffEngine$DiffAction.toString'] = ('no_trigger_in_app', 'The toString override runs only when a DiffAction is converted to a String implicitly (string concatenation, String.valueOf, print or log). A grep under the source root finds no such conversion; the diff results are read through the operation and text fields only.', 'SRC com/ichi2/utils/DiffEngine.java:1145-1148', 'SOURCE')

# ---- sup for part 079 (2026-10-28): Utils.fmtPercentage(Double,int) has no caller (its only caller fmtPercentage(Double) has none), so its call to getLocale is not on any route.
sup(('libanki.Utils.fmtPercentage(Double,int)', 'LanguageUtil.getLocale()'))

# ---- part 080 (2026-10-28)
# AnkiDroid batch 080 (LABEL helper). MethodLogger, Threads, VersionUtils, WidgetStatus (with UpdateDeckStatusAsyncTask),
# AnkiExporter and AnkiPackageExporter (APKG export). 34 methods; the full row list is in graphs/AnkiDroid/parts/label_080.md.
#
# Route ownership: the two INTENT edges from WidgetStatus$UpdateDeckStatusAsyncTask.onPostExecute are written here (the source
# is in this batch). The ASYNC edge into onPostExecute is written by the batch that contains WidgetStatus.update. Automatic CALL
# edges come from auto_calls.json and are not written here. Gate: STATE_SETTINGS (widget and notification preferences).
# No MG id is needed.

e('WidgetStatus$UpdateDeckStatusAsyncTask.onPostExecute', 'AnkiDroidWidgetSmall$UpdateService.<init>', 'INTENT',
  'the status task starts the small widget service when the widget preference is enabled',
  guard='sSmallWidgetEnabled is true (set in WidgetStatus.update from widgetSmallEnabled, WidgetStatus.java:55); the start is at WidgetStatus.java:106-110',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/widget/WidgetStatus.java:55, 106-110; SRC com/ichi2/widget/AnkiDroidWidgetSmall.java:77',
  note='Explicit intent start (WidgetStatus.java:108-109). The framework creates the service through its constructor; the next hop UpdateService.onStart is the LIFECYCLE edge in label_018.py. Gate STATE_SETTINGS (widget preference). env None: the start needs no outside event.')

e('WidgetStatus$UpdateDeckStatusAsyncTask.onPostExecute', 'NotificationService.<init>', 'INTENT',
  'the status task starts the notification service when the notification preference is enabled',
  guard='sNotificationEnabled is true (set in WidgetStatus.update from minimumCardsDueForNotification, WidgetStatus.java:56); the start is at WidgetStatus.java:111-115',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/widget/WidgetStatus.java:56, 111-115; SRC com/ichi2/anki/services/NotificationService.java (line 37)',
  note='Explicit intent start (WidgetStatus.java:113-114). The framework creates the service through its constructor; the next hops NotificationService.onCreate and onStartCommand are the FRAMEWORK edge in label_049.py. Gate STATE_SETTINGS (notification preference). env None: the start needs no outside event.')

UNREACHABLE['MethodLogger.<init>'] = ('no_trigger_in_app', 'Private constructor of a static utility class. grep for new MethodLogger over the source root finds nothing.', 'SRC com/ichi2/utils/MethodLogger.java:42-45', 'SOURCE')

UNREACHABLE['MethodLogger.log()'] = ('branch_never_taken', 'The seven callers in BaseAsyncTask are MethodLogger.log() calls inside if (DEBUG) blocks. DEBUG is the constant false, so the calls never run and javac emits no bytecode for them. No other caller exists in the source root.', 'SRC com/ichi2/async/BaseAsyncTask.java:27, 39-40, 47-48, 56-57, 66-67, 76-77, 86-87, 96-97; SRC com/ichi2/utils/MethodLogger.java:61-63', 'SOURCE')

UNREACHABLE['MethodLogger.log(String)'] = ('no_trigger_in_app', 'No call site. The source root has no call to log(String). MethodLogger.java:36 is a javadoc example, not code, and the BaseAsyncTask calls use log() with no argument.', 'SRC com/ichi2/utils/MethodLogger.java:36, 53-55; SRC com/ichi2/async/BaseAsyncTask.java:40', 'SOURCE')

UNREACHABLE['MethodLogger.logInternal'] = ('no_trigger_in_app', 'Private helper. Its callers are log(String), which has no call site, and log(), which is reached only under the constant-false DEBUG branch. No trigger in the app reaches it.', 'SRC com/ichi2/utils/MethodLogger.java:54, 62, 73-107', 'SOURCE')

UNREACHABLE['Threads.<init>'] = ('no_trigger_in_app', 'Private constructor of a static utility class. grep for new Threads over the source root finds nothing.', 'SRC com/ichi2/utils/Threads.java:26-27', 'SOURCE')

UNREACHABLE['Threads.newCurrentThreadChecker'] = ('no_trigger_in_app', 'Factory with no caller in the source root. grep for newCurrentThreadChecker finds only its declaration.', 'SRC com/ichi2/utils/Threads.java:59-60', 'SOURCE')

UNREACHABLE['Threads.newLazySingleThreadChecker'] = ('no_trigger_in_app', 'Factory with no caller in the source root. grep for newLazySingleThreadChecker finds only its declaration.', 'SRC com/ichi2/utils/Threads.java:69-70', 'SOURCE')

UNREACHABLE['Threads.newSingleThreadChecker'] = ('no_trigger_in_app', 'Factory with no caller in the source root. grep for newSingleThreadChecker and SingleThreadChecker finds only Threads.java.', 'SRC com/ichi2/utils/Threads.java:48-52', 'SOURCE')

UNREACHABLE['Threads$SingleThreadChecker.<init>'] = ('no_trigger_in_app', 'Private constructor. Its only callers are the three factories above (Threads.java:52, 60, 70), and none of those factories has a caller.', 'SRC com/ichi2/utils/Threads.java:52, 60, 70, 123-124', 'SOURCE')

UNREACHABLE['Threads$SingleThreadChecker.checkThread'] = ('no_trigger_in_app', 'No call site in the source root (grep for checkThread finds only Threads.java). The checker object is built only by the unreached factories.', 'SRC com/ichi2/utils/Threads.java:129-136', 'SOURCE')

UNREACHABLE['VersionUtils.<init>'] = ('no_trigger_in_app', 'No explicit constructor (VersionUtils.java:14 is the class line; the implicit constructor is never used). grep for new VersionUtils finds nothing, and every caller uses a static method.', 'SRC com/ichi2/utils/VersionUtils.java:14', 'SOURCE')

UNREACHABLE['WidgetStatus.<init>'] = ('no_trigger_in_app', 'Private constructor ("This class should not be instantiated"). grep for new WidgetStatus finds nothing.', 'SRC com/ichi2/widget/WidgetStatus.java:46-47', 'SOURCE')

# ---- sup for part 080 (2026-10-28): each source is UNREACHABLE (MethodLogger.log/log(String) have no live caller; the Threads factories have no caller), so these bytecode calls are not on any route.
sup(('MethodLogger.log(String)', 'MethodLogger.logInternal'))
sup(('MethodLogger.log()', 'MethodLogger.logInternal'))
sup(('Threads.newSingleThreadChecker', 'Threads$SingleThreadChecker.<init>'))
sup(('Threads.newCurrentThreadChecker', 'Threads$SingleThreadChecker.<init>'))
sup(('Threads.newLazySingleThreadChecker', 'Threads$SingleThreadChecker.<init>'))

# ---- part 081 (2026-10-28)
# AnkiDroid batch 081 (LABEL helper). libanki Card, part 1 of 2: 40 methods. The full row list is in
# graphs/AnkiDroid/parts/label_081.md. This part writes one UNREACHABLE entry (Card.getCol). The other 39 methods
# are REACHABLE through builder CALL edges (not written here). No e() edges are written in this part.

UNREACHABLE['Card.getCol'] = ('no_trigger_in_app',
  "Card.getCol() has no caller in src/main with a Card receiver. Its comment says Needed for tests. "
  "All 13 call sites of getCol() in src/main are on activity receivers, not on a Card: "
  "CompatV10.java:170; CardTemplateEditor.java:386, 451, 601, 609, 641, 662, 676, 697, 698; "
  "DialogHandler.java:94; CustomStudyDialog.java:148, 330. No class extends Card, so no app trigger reaches it.",
  'SRC com/ichi2/libanki/Card.java:604-607; SRC com/ichi2/compat/CompatV10.java:168-171; '
  'SRC com/ichi2/anki/CardTemplateEditor.java:384-387, 449-452, 599-610, 639-642, 660-663, 674-677, 695-699; '
  'SRC com/ichi2/anki/dialogs/DialogHandler.java:92-95; SRC com/ichi2/anki/dialogs/CustomStudyDialog.java:146-149, 328-331',
  'SOURCE')

# ---- part 082 (2026-10-28)
# AnkiDroid batch 082 (LABEL helper): libanki Card methods, part 2 of 2 (27 methods).
# The row list is in graphs/AnkiDroid/parts/label_082.md.
# No e() edges: the setters and the other Card methods own no outgoing edges except automatic CALL edges,
# and the edges into them come from callers owned by other batches (Sched, DeckTask, AbstractFlashcardViewer,
# CardContentProvider, NoteEditor, Collection, CardBrowser).

UNREACHABLE['Card.setCol'] = ('no_trigger_in_app',
  'Only the declaration exists in the source root. The method is marked "Needed for tests", so its only caller would be test code, which is not in the app. A grep for setCol over the source root finds no other call.',
  'com/ichi2/libanki/Card.java:610-613', 'SOURCE')

UNREACHABLE['Card.shouldShowTimer'] = ('no_trigger_in_app',
  'Declared at Card.java 365-372. No call site exists in the source root (grep for the call finds none). The viewer asks showTimer instead (AbstractFlashcardViewer.java 1885).',
  'com/ichi2/libanki/Card.java:365-372; com/ichi2/anki/AbstractFlashcardViewer.java:1883-1886', 'SOURCE')

UNREACHABLE['Card.toString'] = ('no_trigger_in_app',
  'Overrides Object.toString. No explicit call and no implicit string conversion of a libanki Card was found in the source root. The one Card concatenation (AdvancedStatistics.java 1499) uses the inner class Card of AdvancedStatistics, which has its own toString. Confidence is moderate.',
  'com/ichi2/libanki/Card.java:634-648; com/ichi2/libanki/hooks/AdvancedStatistics.java:1497-1500', 'SOURCE')

# ---- part 083 (2026-10-28)
# AnkiDroid batch 083 (LABEL helper). CardStats (com/ichi2/libanki/CardStats.java; the batch file says com.ichi2.anki).
# Methods: CardStats.<init> and CardStats.report. Both are UNREACHABLE (no_trigger_in_app). No e() edges in this part.
# Gates: none (no MG ids used). The outgoing calls of report are the builder's automatic CALL edges and are not repeated here.

# --- CardStats.<init>: the class declares no constructor; no code creates an instance (grep over src/main/java).
UNREACHABLE['CardStats.<init>'] = ('no_trigger_in_app',
  "CardStats declares no constructor, so its only constructor is the implicit default one. No code creates an instance: "
  "grep -rn CardStats over the source root (src/main/java) returns only the class declaration at CardStats.java:12, and no other "
  "file in the app folder names the class (the build output holds only its own compiled class). The class has only the static "
  "method report, which has no caller either (see CardStats.report). So the constructor is never run.",
  "SRC com/ichi2/libanki/CardStats.java:12; SRC com/ichi2/libanki/CardStats.java:14-123",
  'SOURCE')

# --- CardStats.report: the only method of the class (static, lines 14-123). No call site in the source root.
UNREACHABLE['CardStats.report'] = ('no_trigger_in_app',
  "report is the only method of CardStats and it is static. No call site exists: grep -rn CardStats over the source root "
  "returns only the class declaration at CardStats.java:12. A call from another class has to name CardStats (a qualified "
  "call, a static import or a subclass), and no such reference exists. The build output holds only the class's own compiled "
  "file. Nothing in the app reaches report from an entry point, so it never runs.",
  "SRC com/ichi2/libanki/CardStats.java:12; SRC com/ichi2/libanki/CardStats.java:14-123",
  'SOURCE')

# ---- part 086 (2026-10-28)
# AnkiDroid batch 086 (LABEL helper): libanki Consts and DB, 4 methods. Rows are in graphs/AnkiDroid/parts/label_086.md.
# No e() edges in this part. Outgoing calls are automatic CALL edges (builder). Incoming edges belong to other batches.
# MISSING GATE MG802 (for the FRAMEWORK edge DB.<init> -> DB$MyDbErrorHandler.onCorruption, owned by the batch that holds DB.<init>):
#   the collection file is damaged, so SQLite reports corruption and calls DatabaseErrorHandler.onCorruption.

UNREACHABLE['Consts.<init>'] = ('no_trigger_in_app', "Consts only declares static final fields and has no constructor, so Consts.<init> is the implicit default constructor. No code creates an instance: a grep over the source root for new Consts, Consts() and extends Consts finds nothing, and the other references are imports or Consts.NAME static reads.", 'SRC com/ichi2/libanki/Consts.java:19-71', 'SOURCE')
UNREACHABLE['DB.getPath'] = ('no_trigger_in_app', "DB.getPath has no call site in the app. The only getPath() calls inside DB are mDatabase.getPath() on the SQLiteDatabase (DB.java:100, 353), which are not DB.getPath. The other getPath() call sites in the source root are listed in the source reference (printed): none of their receivers is a DB, since a grep for getDb().getPath, db.getPath, mDb.getPath, tempDb.getPath and DB::getPath finds nothing.", 'SRC com/ichi2/libanki/DB.java:352-354, 100; com/ichi2/libanki/Collection.java:1635-1637; com/ichi2/anki/Preferences.java:757; com/ichi2/async/DeckTask.java:763; com/ichi2/anki/BackupManager.java:171, 223, 242, 346; com/ichi2/anki/DeckPicker.java:807, 1595, 1619; com/ichi2/anki/IntentHandler.java:95; com/ichi2/anki/AnkiFont.java:143; com/ichi2/anki/CustomExceptionHandler.java:67, 76; com/ichi2/anki/multimediacard/fields/BasicImageFieldController.java:121; com/ichi2/anki/provider/CardContentProvider.java:1298; com/ichi2/anki/dialogs/DatabaseErrorDialog.java:259; com/ichi2/utils/ExifUtil.java:33; com/ichi2/libanki/Sound.java:286; com/ichi2/libanki/AnkiPackageExporter.java:325, 337, 364; com/ichi2/libanki/importer/AnkiPackageImporter.java:51; com/ichi2/libanki/sync/FullSyncer.java:93, 155; com/ichi2/libanki/sync/RemoteMediaServer.java:117; com/ichi2/libanki/Media.java:121, 801', 'SOURCE')

# ---- part 084 (2026-10-28)
# AnkiDroid batch 084 (LABEL helper): libanki Collection methods, part 1 of 2 (40 methods).
# The row list is in graphs/AnkiDroid/parts/label_084.md.
# No e() edges: none of the 40 methods owns a source-side gate; they are callees of other owners' methods.
# The 13 UNREACHABLE entries are below; each reason is repeated inline.

UNREACHABLE['Collection.<init>(Context,DB,String)'] = ('no_trigger_in_app',
  'The body only calls this(context, db, path, false). The source root has no call with three arguments: the one constructor call is Storage.java line 63, which passes five arguments. No other constructor calls this one.',
  'com/ichi2/libanki/Collection.java:129-131; com/ichi2/libanki/Storage.java:63', 'SOURCE')

UNREACHABLE['Collection.<init>(Context,DB,String,boolean)'] = ('no_trigger_in_app',
  'The body calls this(context, db, path, false, false), so the server argument is dropped (passed as false). The only caller of this constructor is the three-argument constructor, which has no caller itself. Storage uses the five-argument form.',
  'com/ichi2/libanki/Collection.java:133-135; com/ichi2/libanki/Collection.java:129-131; com/ichi2/libanki/Storage.java:63', 'SOURCE')

UNREACHABLE['Collection._qaData()'] = ('no_trigger_in_app',
  'No caller in the source root. The one-argument _qaData(String) is called from this method (Collection.java:1030) and from renderQA(int[],String) (Collection.java:951). renderQA() (Collection.java:932) and renderQA(int[],String) have no caller in the source root, so no entry point reaches either.',
  'com/ichi2/libanki/Collection.java:1029-1031; com/ichi2/libanki/Collection.java:930-938; com/ichi2/libanki/Collection.java:951', 'SOURCE')

UNREACHABLE['Collection._qaData(String)'] = ('no_trigger_in_app',
  'Called only from _qaData() (Collection.java:1030) and from renderQA(int[],String) (Collection.java:951). Neither caller is reached from an entry point (see _qaData() and renderQA above).',
  'com/ichi2/libanki/Collection.java:1034-1036; com/ichi2/libanki/Collection.java:1030; com/ichi2/libanki/Collection.java:951', 'SOURCE')

UNREACHABLE['Collection.emptyCardReport'] = ('no_trigger_in_app',
  'Declared at Collection.java:868. No call exists in the source root (grep for emptyCardReport finds only the declaration). The find-empty-cards task calls emptyCids (DeckTask.java:1230) and not this method.',
  'com/ichi2/libanki/Collection.java:868-870; com/ichi2/async/DeckTask.java:1226-1234', 'SOURCE')

UNREACHABLE['Collection.findCards(String)'] = ('no_trigger_in_app',
  'No caller in the source root. The one Collection.findCards call site found is Sched.java:1569, which passes two arguments (search, orderlimit) and so uses findCards(String,String). No call uses the one-argument form.',
  'com/ichi2/libanki/Collection.java:1059-1061; com/ichi2/libanki/Sched.java:1569', 'SOURCE')

UNREACHABLE['Collection.findDupes(String)'] = ('no_trigger_in_app',
  'No caller in the source root. The grep for findDupes finds only the declarations in Collection.java and the Finder helpers, which are called only from the Collection overloads.',
  'com/ichi2/libanki/Collection.java:1101-1103; com/ichi2/libanki/Finder.java:955-957', 'SOURCE')

UNREACHABLE['Collection.findDupes(String,String)'] = ('no_trigger_in_app',
  'No caller in the source root. The one-argument overload calls Finder.findDupes directly (Collection.java:1102), not this overload. Finder.findDupes(Collection,String,String) is called only from Collection.',
  'com/ichi2/libanki/Collection.java:1106-1108; com/ichi2/libanki/Collection.java:1102; com/ichi2/libanki/Finder.java:963', 'SOURCE')

UNREACHABLE['Collection.findReplace(List,String,String)'] = ('no_trigger_in_app',
  'No caller in the source root. The Finder static overloads are called only from the Collection overloads, and none of those has a caller.',
  'com/ichi2/libanki/Collection.java:1081-1083; com/ichi2/libanki/Finder.java:806-810', 'SOURCE')

UNREACHABLE['Collection.findReplace(List,String,String,String)'] = ('no_trigger_in_app',
  'No call site in the source root. The Finder overload with a field argument (Finder.java:818-820) is called only from this Collection overload.',
  'com/ichi2/libanki/Collection.java:1091-1093; com/ichi2/libanki/Finder.java:818-820', 'SOURCE')

UNREACHABLE['Collection.findReplace(List,String,String,boolean)'] = ('no_trigger_in_app',
  'No call site in the source root. The Finder overload with a regex flag (Finder.java:813-815) is called only from this Collection overload.',
  'com/ichi2/libanki/Collection.java:1086-1088; com/ichi2/libanki/Finder.java:813-815', 'SOURCE')

UNREACHABLE['Collection.findReplace(List,String,String,boolean,String,boolean)'] = ('no_trigger_in_app',
  'No call site in the source root. The full Finder.findReplace (Finder.java:823-826) is called only from the Collection overloads.',
  'com/ichi2/libanki/Collection.java:1096-1098; com/ichi2/libanki/Finder.java:823-826', 'SOURCE')

UNREACHABLE['Collection.getTimeLimit'] = ('no_trigger_in_app',
  'Declared at Collection.java:1131; it reads the timeLim configuration value. No call exists in the source root (grep for getTimeLimit finds only the declaration).',
  'com/ichi2/libanki/Collection.java:1131-1139', 'SOURCE')

# ---- part 085 (2026-10-28)
# AnkiDroid batch 085 (LABEL helper): libanki Collection methods, part 2 (33 methods; 10 UNREACHABLE here).
# The row list is in graphs/AnkiDroid/parts/label_085.md.
# No e() edges: none of these methods is the source of a GUI, ASYNC, INTENT, RESULT or framework edge.
# The routes into the REACHABLE methods are automatic CALL edges from app code (not repeated) or belong to other batches.

UNREACHABLE['Collection.name'] = ('no_trigger_in_app',
  'Declared at Collection.java 169-172 (returns the file name without the .anki2 extension). The grep for .name() over the source root finds no call on a Collection. The only matches are Enum.name() calls on mChartType in AnkiStatsTaskHandler.java 101 and 104, which are a different method.',
  'com/ichi2/libanki/Collection.java:169-172; com/ichi2/anki/stats/AnkiStatsTaskHandler.java:101-104', 'SOURCE')

UNREACHABLE['Collection.noteCount'] = ('no_trigger_in_app',
  'Declared at Collection.java 478-480. The grep for noteCount over the source root finds only this declaration, so nothing calls it.',
  'com/ichi2/libanki/Collection.java:478-480', 'SOURCE')

UNREACHABLE['Collection.setTimeLimit'] = ('no_trigger_in_app',
  'Declared at Collection.java 1122-1124 (writes timeLim to the collection config). The grep for setTimeLimit over the source root finds only this declaration.',
  'com/ichi2/libanki/Collection.java:1122-1124', 'SOURCE')

UNREACHABLE['Collection.save(long)'] = ('no_trigger_in_app',
  'Declared at Collection.java 252-254; it calls save(null, mod) at 253. No caller passes a single long to Collection.save. The calls to save() with no argument (Collection.java 248, 299, 1347) go to the no-argument overload. The only two-argument call on a Collection is Syncer.java 432, which is save(String, long). The grep for save with an argument over the source root finds no other match.',
  'com/ichi2/libanki/Collection.java:247-254; com/ichi2/libanki/sync/Syncer.java:432', 'SOURCE')

UNREACHABLE['Collection.renderQA()'] = ('no_trigger_in_app',
  'Declared at Collection.java 932-934; it calls renderQA(null, card) at 933. The grep for renderQA over the source root finds no call of renderQA() with no arguments. The other matches are _renderQA in Card.java 303-308 and Models.java 1081-1114, which are different methods.',
  'com/ichi2/libanki/Collection.java:932-934; com/ichi2/libanki/Card.java:303-308; com/ichi2/libanki/Models.java:1081-1114', 'SOURCE')

UNREACHABLE['Collection.renderQA(int[],String)'] = ('no_trigger_in_app',
  'Declared at Collection.java 937-959. Its only call is renderQA(null, card) at 933, inside renderQA(), which has no caller. The grep for renderQA finds no other call of this overload.',
  'com/ichi2/libanki/Collection.java:933-959', 'SOURCE')

UNREACHABLE['Collection.previewCards(Note)'] = ('no_trigger_in_app',
  'Declared at Collection.java 746-748; it calls previewCards(note, 0) at 747. The grep for previewCards over the source root finds only the two declarations (717 and 746) and the call at 747. No caller exists.',
  'com/ichi2/libanki/Collection.java:746-748', 'SOURCE')

UNREACHABLE['Collection.previewCards(Note,int)'] = ('no_trigger_in_app',
  'Declared at Collection.java 717-745. Its only call is previewCards(note, 0) at 747, inside previewCards(Note), which has no caller.',
  'com/ichi2/libanki/Collection.java:717-747', 'SOURCE')

UNREACHABLE['Collection.newNote()'] = ('no_trigger_in_app',
  'Declared at Collection.java 486-488; it calls newNote(true) at 487. The grep for newNote over the source root finds no call with no arguments. The only call of a newNote overload outside Collection is CardTemplateEditor.java 530, which passes a model (newNote(JSONObject)).',
  'com/ichi2/libanki/Collection.java:486-488; com/ichi2/anki/CardTemplateEditor.java:530', 'SOURCE')

UNREACHABLE['Collection.newNote(boolean)'] = ('no_trigger_in_app',
  'Declared at Collection.java 496-498. Its only caller is newNote() at 487, which has no caller, so this overload is never reached. The grep finds no other call with a boolean argument.',
  'com/ichi2/libanki/Collection.java:487; com/ichi2/libanki/Collection.java:496-498', 'SOURCE')

# ---- part 087 (2026-10-28)
# AnkiDroid batch 087 (LABEL helper): Decks part 1 (40 methods, com/ichi2/libanki/Decks.java).
# The row list is in graphs/AnkiDroid/parts/label_087.md. 29 methods are REACHABLE (automatic CALL routes, see the .md).
# No e() edges: the Decks methods in this batch own no outgoing edges that are not automatic CALL edges, and the edges
# into them come from methods owned by other batches. No MISSING GATE notes.
# The 11 UNREACHABLE entries below are the methods with no route in the standard configuration.

UNREACHABLE['Decks._basename'] = ('no_trigger_in_app',
  'Private helper. Its only callers are renameForDragAndDrop (Decks.java 538 and 544) and _isParent (Decks.java 565). Both are unreachable, and no other call exists in the source root.',
  'com/ichi2/libanki/Decks.java:593-596; com/ichi2/libanki/Decks.java:538, 544, 565', 'SOURCE')

UNREACHABLE['Decks._canDragAndDrop'] = ('no_trigger_in_app',
  'Private. Its only caller is renameForDragAndDrop (Decks.java 540). renameForDragAndDrop has no caller in the source root (grep finds only its declaration at 530), so this method cannot run.',
  'com/ichi2/libanki/Decks.java:552-560; com/ichi2/libanki/Decks.java:540', 'SOURCE')

UNREACHABLE['Decks._isAncestor'] = ('no_trigger_in_app',
  'Private. Its only caller is _canDragAndDrop (Decks.java 555), which is unreachable because renameForDragAndDrop has no caller.',
  'com/ichi2/libanki/Decks.java:578-587; com/ichi2/libanki/Decks.java:555', 'SOURCE')

UNREACHABLE['Decks._isParent'] = ('no_trigger_in_app',
  'Private. Its only caller is _canDragAndDrop (Decks.java 554), which is unreachable because renameForDragAndDrop has no caller.',
  'com/ichi2/libanki/Decks.java:563-575; com/ichi2/libanki/Decks.java:554', 'SOURCE')

UNREACHABLE['Decks.cids(long)'] = ('no_trigger_in_app',
  'No caller in the source root. A grep for the call pattern finds only the two-argument form cids(mDid, true) at AnkiPackageExporter.java 97. The method itself only calls cids(did, false) at Decks.java 827, and nothing calls cids(long).',
  'com/ichi2/libanki/Decks.java:826-828; com/ichi2/libanki/AnkiPackageExporter.java:93-98', 'SOURCE')

UNREACHABLE['Decks.collapseBrowser'] = ('no_trigger_in_app',
  'No caller in the source root. A grep for collapseBrowser over the whole source root finds only its declaration at Decks.java 420.',
  'com/ichi2/libanki/Decks.java:420-429', 'SOURCE')

UNREACHABLE['Decks.confId(String)'] = ('no_trigger_in_app',
  'No caller in the source root. A grep for .confId( finds only the two-argument call at DeckOptions.java 239.',
  'com/ichi2/libanki/Decks.java:674-676; com/ichi2/anki/DeckOptions.java:239', 'SOURCE')

UNREACHABLE['Decks.count'] = ('no_trigger_in_app',
  'No caller in the source root. A grep for the call on getDecks(), mDecks and decks variables finds no call. The method is declared at Decks.java 435-437 and returns mDecks.size().',
  'com/ichi2/libanki/Decks.java:435-437', 'SOURCE')

UNREACHABLE['Decks.nameOrNone'] = ('no_trigger_in_app',
  'No caller in the source root. A grep for nameOrNone over the whole source root finds only its declaration at Decks.java 796.',
  'com/ichi2/libanki/Decks.java:796-806', 'SOURCE')

UNREACHABLE['Decks.rem(long)'] = ('no_trigger_in_app',
  'No caller. The one-argument form is never called: every call site found by grep passes two or three arguments (DeckTask.java 723, Syncer.java 644, Sched.java 390 and 406).',
  'com/ichi2/libanki/Decks.java:270-272; com/ichi2/async/DeckTask.java:723; com/ichi2/libanki/sync/Syncer.java:644; com/ichi2/libanki/Sched.java:390, 406', 'SOURCE')

UNREACHABLE['Decks.renameForDragAndDrop'] = ('no_trigger_in_app',
  'No caller in the source root. A grep for renameForDragAndDrop over the whole source root finds only its declaration at Decks.java 530. Its helpers (_canDragAndDrop, _isParent, _isAncestor, _basename) are reached only through it.',
  'com/ichi2/libanki/Decks.java:530-549; com/ichi2/libanki/Decks.java:552-575', 'SOURCE')


# ---- addendum (2026-10-28): edge for the Decks$1.compare row in batch 088; written here with allSorted
e('Decks.allSorted', 'Decks$1.compare', 'CALL',
  'Collections.sort in allSorted calls the anonymous comparator for each pair of decks it compares',
  env=None,
  note='MISSING GATE MG812: the comparator runs only when the collection has two or more decks (the Default deck always exists, so one more deck is needed). The sort is java.util and not in fw_src (source not read), so the call is INFERRED from the JDK contract.',
  evidence='SRC com/ichi2/libanki/Decks.java:388-398; INFERRED (JDK Collections.sort, source not read)')

# ---- part 088 (2026-10-28)
# AnkiDroid batch 088 (LABEL helper): Decks part 2, 10 methods. The row list is in graphs/AnkiDroid/parts/label_088.md.
# No e() calls. The calls into these methods are automatic CALL edges (written by the builder) or belong to the
# batches that hold their callers (DeckOptions, DeckTask, DeckPicker, Sched, AnkiPackageExporter, Anki2Importer, Syncer).
# The FRAMEWORK edge from Decks.allSorted to Decks$1.compare belongs to the batch that holds allSorted.

UNREACHABLE['Decks.setDeck'] = ('no_trigger_in_app',
  'Declared at Decks.java 809-812 and not called anywhere in src/main. A grep for setDeck over the whole src/main tree finds only this declaration. The card move it would do (update cards set did, using Utils.ids2str) is not reached from any UI, DeckTask, provider, importer or sync path. Confidence is high because the search covers the full src/main tree.',
  'com/ichi2/libanki/Decks.java:809-812', 'SOURCE')

# ---- part 089 (2026-10-28)
# AnkiDroid batch 089 (LABEL helper). Exporter constructors (2 methods), class Exporter in
# com/ichi2/libanki/AnkiPackageExporter.java:42-56. The row list is in graphs/AnkiDroid/parts/label_089.md.
# No e() edges: Exporter.<init>(Collection) is reached through the automatic super call in
# AnkiPackageExporter (line 299), and the export route (DeckPicker, ExportDialog, DeckTask) is owned by other batches.

UNREACHABLE['Exporter.<init>(Collection,Long)'] = ('no_trigger_in_app',
  'No call site exists in the source root. The only subclasses, AnkiExporter and AnkiPackageExporter, call the one-argument super(col) (AnkiPackageExporter.java:70, 299). A grep for new Exporter(, new AnkiExporter( and the two-argument super form finds none. The one construction of a subclass, new AnkiPackageExporter(col) at DeckTask.java:891, uses the one-argument form, and the deck id is passed later through setDid (DeckTask.java:894; AnkiPackageExporter.java:289-291), not through this constructor. A grep for the bare word Exporter finds only the declarations at AnkiPackageExporter.java:42, 47, 53 and 61.',
  'com/ichi2/libanki/AnkiPackageExporter.java:42-56, 61-70, 289-291, 296-299; com/ichi2/async/DeckTask.java:891, 894', 'SOURCE')

# ---- suppressed auto edges (2026-10-28, orchestrator): each warned target is UNREACHABLE (parts 084, 085, 087, 088) and each auto edge below starts in an UNREACHABLE method, or in the three-argument constructor that has no caller
sup(('Collection.<init>(Context,DB,String)', 'Collection.<init>(Context,DB,String,boolean)'),
    ('Collection.renderQA(int[],String)', 'Collection._qaData(String)'),
    ('Collection._qaData()', 'Collection._qaData(String)'),
    ('Collection.newNote()', 'Collection.newNote(boolean)'),
    ('Collection.previewCards(Note)', 'Collection.previewCards(Note,int)'),
    ('Collection.renderQA()', 'Collection.renderQA(int[],String)'),
    ('Decks.renameForDragAndDrop', 'Decks._basename'),
    ('Decks._isParent', 'Decks._basename'),
    ('Decks.renameForDragAndDrop', 'Decks._canDragAndDrop'),
    ('Decks._canDragAndDrop', 'Decks._isAncestor'),
    ('Decks._canDragAndDrop', 'Decks._isParent'))

# ---- part 090 (2026-10-28)
# AnkiDroid batch 090 (LABEL helper): Finder, part 1 of 2 (40 methods, com/ichi2/libanki/Finder.java).
# The row list is in graphs/AnkiDroid/parts/label_090.md.
# No e() edges: every call inside Finder is an automatic CALL edge (written by the builder), and the entries into
# Finder come from Collection, CardContentProvider, Sched, DeckTask, CardBrowser and CardTemplateEditor, which other batches own.
# The 28 REACHABLE methods need no entry here. The 12 UNREACHABLE methods follow.

UNREACHABLE['Finder.fieldNames(Collection)'] = ('no_trigger_in_app',
  'No caller. The only fieldNames calls in the source root are Models.fieldNames on a model object (CardTemplateEditor.java 531, declared at Models.java 490), not this Finder method. The Collection wrappers that create a Finder (Collection.java 1060, 1066, 1071, 1077) never call fieldNames.',
  'com/ichi2/libanki/Finder.java:902-904; com/ichi2/anki/CardTemplateEditor.java:531; com/ichi2/libanki/Collection.java:1059-1077', 'SOURCE')

UNREACHABLE['Finder.fieldNames(Collection,boolean)'] = ('no_trigger_in_app',
  'Its only caller is fieldNames(Collection) at Finder.java 903, which has no caller (see the row above).',
  'com/ichi2/libanki/Finder.java:903-904, 906-927', 'SOURCE')

UNREACHABLE['Finder.findCards(String)'] = ('no_trigger_in_app',
  'No caller. Collection.findCards(String) (Collection.java 1059-1061) calls the two-argument Finder overload with null at 1060, not this one, and no code calls that wrapper. A grep for one-argument findCards calls over the source root finds none. Finder.findCards(String) calls only findCards(String,boolean) at Finder.java 71.',
  'com/ichi2/libanki/Finder.java:70-72; com/ichi2/libanki/Collection.java:1059-1061', 'SOURCE')

UNREACHABLE['Finder.findCards(String,boolean)'] = ('no_trigger_in_app',
  'Its only caller is findCards(String) at Finder.java 71, which has no caller (see the row above). Collection passes null at 1060 and a String order at 1066, so the boolean overload is never selected.',
  'com/ichi2/libanki/Finder.java:71, 80-82; com/ichi2/libanki/Collection.java:1060, 1066', 'SOURCE')

UNREACHABLE['Finder.findCardsForCardBrowser(String,String,Map)'] = ('no_trigger_in_app',
  'The only calls over the source root are Collection.findCardsForCardBrowser (Collection.java 1070-1072), which takes a boolean and passes it at 1071, and DeckTask.doInBackgroundSearchCards (DeckTask.java 619-622), which passes a Boolean that Java unboxes to boolean. The String overload is therefore never selected (Finder.java 1018-1020).',
  'com/ichi2/libanki/Finder.java:1013-1020; com/ichi2/libanki/Collection.java:1070-1072; com/ichi2/async/DeckTask.java:619-622', 'SOURCE')

UNREACHABLE['Finder.findDupes(Collection,String)'] = ('no_trigger_in_app',
  'No caller. Collection.findDupes(String) (Collection.java 1101-1103) calls the three-argument overload at 1102, not this one, and no other call site was found over the source root.',
  'com/ichi2/libanki/Finder.java:955-957; com/ichi2/libanki/Collection.java:1101-1103', 'SOURCE')

UNREACHABLE['Finder.findDupes(Collection,String,String)'] = ('no_trigger_in_app',
  'Its callers are findDupes(Collection,String) at Finder.java 956, which is itself uncalled, and the Collection wrappers at Collection.java 1102 (findDupes(String)) and 1107 (findDupes(String,String)). Those wrappers have no caller (1101-1108), so this method is never called.',
  'com/ichi2/libanki/Finder.java:955-957, 963-1005; com/ichi2/libanki/Collection.java:1101-1108', 'SOURCE')

UNREACHABLE['Finder.findReplace(Collection,List,String,String)'] = ('no_trigger_in_app',
  'Its only caller is Collection.findReplace(List,String,String) at Collection.java 1082, which has no caller (1081-1083). The Finder.java calls at 809, 814 and 819 go to the seven-argument overload, not to this one.',
  'com/ichi2/libanki/Finder.java:808-810; com/ichi2/libanki/Collection.java:1081-1083', 'SOURCE')

UNREACHABLE['Finder.findReplace(Collection,List,String,String,String)'] = ('no_trigger_in_app',
  'Its only caller is Collection.findReplace(List,String,String,String) at Collection.java 1092 inside the wrapper at 1091-1093, which no code calls.',
  'com/ichi2/libanki/Finder.java:818-820; com/ichi2/libanki/Collection.java:1091-1093', 'SOURCE')

UNREACHABLE['Finder.findReplace(Collection,List,String,String,boolean)'] = ('no_trigger_in_app',
  'Its only caller is Collection.findReplace(List,String,String,boolean) at Collection.java 1087 inside the wrapper at 1086-1088, which no code calls.',
  'com/ichi2/libanki/Finder.java:813-815; com/ichi2/libanki/Collection.java:1086-1088', 'SOURCE')

UNREACHABLE['Finder.findReplace(Collection,List,String,String,boolean,String,boolean)'] = ('no_trigger_in_app',
  'Its callers are the three shorter Finder.findReplace overloads (Finder.java 809, 814, 819), which are themselves uncalled, and Collection.findReplace(List,String,String,boolean,String,boolean) at Collection.java 1097 inside the wrapper at 1096-1098. That wrapper has no caller, so this method is never called.',
  'com/ichi2/libanki/Finder.java:808-820, 823-899; com/ichi2/libanki/Collection.java:1096-1098', 'SOURCE')

UNREACHABLE['Finder.ordForMid'] = ('no_trigger_in_app',
  'Its only caller is findDupes (three-argument) at Finder.java 981, which is reached only through the uncalled Collection.findDupes wrappers (Collection.java 1101-1108).',
  'com/ichi2/libanki/Finder.java:935-952, 963-1005, 981; com/ichi2/libanki/Collection.java:1101-1108', 'SOURCE')

# ---- part 091 (2026-10-28)
# AnkiDroid batch 091 (LABEL helper): Finder part 2, 3 methods (Finder$SearchState.<init>, add(String), add(String,boolean)).
# The row list is in graphs/AnkiDroid/parts/label_091.md.
# All three methods are REACHABLE (see the rows), so there are no UNREACHABLE entries.
# No e() edges: the only outgoing edge is the automatic CALL add(String) -> add(String,boolean), which the builder writes.

# ---- suppressed auto edges (2026-10-28, orchestrator, part 090): each warned target is UNREACHABLE and each auto edge below starts in an UNREACHABLE method (the Collection and Finder wrappers, which have no caller)
sup(('Finder.fieldNames(Collection)', 'Finder.fieldNames(Collection,boolean)'),
    ('Finder.findCards(String)', 'Finder.findCards(String,boolean)'),
    ('Collection.findDupes(String)', 'Finder.findDupes(Collection,String,String)'),
    ('Collection.findDupes(String,String)', 'Finder.findDupes(Collection,String,String)'),
    ('Finder.findDupes(Collection,String)', 'Finder.findDupes(Collection,String,String)'),
    ('Finder.findDupes(Collection,String,String)', 'Finder.ordForMid'),
    ('Collection.findReplace(List,String,String)', 'Finder.findReplace(Collection,List,String,String)'),
    ('Collection.findReplace(List,String,String,String)', 'Finder.findReplace(Collection,List,String,String,String)'),
    ('Collection.findReplace(List,String,String,boolean)', 'Finder.findReplace(Collection,List,String,String,boolean)'),
    ('Collection.findReplace(List,String,String,boolean,String,boolean)', 'Finder.findReplace(Collection,List,String,String,boolean,String,boolean)'),
    ('Finder.findReplace(Collection,List,String,String)', 'Finder.findReplace(Collection,List,String,String,boolean,String,boolean)'),
    ('Finder.findReplace(Collection,List,String,String,boolean)', 'Finder.findReplace(Collection,List,String,String,boolean,String,boolean)'),
    ('Finder.findReplace(Collection,List,String,String,String)', 'Finder.findReplace(Collection,List,String,String,boolean,String,boolean)'))

# ---- part 092 (2026-10-28)
# AnkiDroid batch 092 (LABEL helper): libanki Media methods, 37 methods (com/ichi2/libanki/Media.java).
# The row list is in graphs/AnkiDroid/parts/label_092.md.
# No e() edges: every edge into these methods comes from a caller owned by another part
# (sync, DeckTask, AbstractFlashcardViewer, CardContentProvider, AnkiPackageExporter, Anki2Importer, NoteService, MyAccount).

UNREACHABLE['Media.strip'] = ('no_trigger_in_app',
  'Public method that applies the media regexps to a string. No call in the app source root. Its only callers are the androidTest unit tests (MediaTest lines 108-110 of the androidTest file). A search for a call on a Media receiver finds only those tests. The String.strip() calls in the app are a different method.',
  'AnkiDroid/src/androidTest/java/com.ichi2.anki.tests/libanki/MediaTest.java:108-110; com/ichi2/libanki/Media.java:358-363', 'SOURCE')

# ---- part 093 (2026-10-28)
# AnkiDroid batch 093 (LABEL helper): libanki Models.java, 30 methods, part 1 of 1.
# The row list is in graphs/AnkiDroid/parts/label_093.md.
# No e() edges: none of these methods sources a non-CALL edge.
# The six entries below are the methods with no call site in the source root.

UNREACHABLE['Models.byName'] = ('no_trigger_in_app',
  'Declared at Models.java 292-304. No call to Models.byName exists in the source root. The only byName call (CustomStudyDialog.java 423) is on col.getDecks(), so it is Decks.byName (Decks.java 459-460), a different method. No route from any entry.',
  'com/ichi2/libanki/Models.java:292-304; com/ichi2/libanki/Decks.java:459-460; com/ichi2/anki/dialogs/CustomStudyDialog.java:421-424', 'SOURCE')

UNREACHABLE['Models.copy'] = ('no_trigger_in_app',
  'Declared at Models.java 443-453. A grep for copy( with a receiver over the source root finds no call. No route from any entry.',
  'com/ichi2/libanki/Models.java:443-453', 'SOURCE')

UNREACHABLE['Models.getId'] = ('no_trigger_in_app',
  'Declared at Models.java 1372-1374 (returns mId). No call site in the source root: a grep for getId() on getModels() and on model, models or mModels receivers finds none. The getId() calls that exist belong to other classes. No route from any entry.',
  'com/ichi2/libanki/Models.java:1372-1374', 'SOURCE')

UNREACHABLE['Models.getName'] = ('no_trigger_in_app',
  'Declared at Models.java 1380-1382 (returns mName). No call on a Models receiver in the source root. The getName() calls in ModelBrowser (lines 277, 285, 669) are on DisplayPair objects (ModelBrowser.java 624-637). CardStats.java 115 is commented out. No route from any entry.',
  'com/ichi2/libanki/Models.java:1380-1382; com/ichi2/anki/ModelBrowser.java:274-290, 624-637, 658-670; com/ichi2/libanki/CardStats.java:112-120', 'SOURCE')

UNREACHABLE['Models.getTemplateNames'] = ('no_trigger_in_app',
  'Declared at Models.java 1349-1351. A grep over the source root for getTemplateNames( finds only its declaration. No route from any entry.',
  'com/ichi2/libanki/Models.java:1349-1351', 'SOURCE')

UNREACHABLE['Models.moveTemplate'] = ('no_trigger_in_app',
  'Declared at Models.java 842-846. A grep over the source root for moveTemplate( finds only its declaration. No route from any entry.',
  'com/ichi2/libanki/Models.java:842-846', 'SOURCE')

# ---- part 094 (2026-10-28)
# AnkiDroid batch 094 (LABEL helper): libanki Note methods (35 methods, com/ichi2/libanki/Note.java).
# The row list is in graphs/AnkiDroid/parts/label_094.md.
# No e() edges: every caller of these methods is an automatic CALL edge or belongs to another batch.
# Four methods have no caller in the app (contains, getCol, keys, setItem). Their entries are below.

UNREACHABLE['Note.contains'] = ('no_trigger_in_app',
  'No caller. A grep of the source root for contains( on Note receivers finds none, and the bytecode call list (auto_calls.json) has no edge into Note.contains. The body returns mFMap.containsKey(key) (Note.java 222), a plain key test.',
  'com/ichi2/libanki/Note.java:221-223', 'SOURCE')

UNREACHABLE['Note.getCol'] = ('no_trigger_in_app',
  'No caller. A grep of the source root for getCol() calls on Note receivers finds none, and the bytecode call list (auto_calls.json) has no edge into Note.getCol.',
  'com/ichi2/libanki/Note.java:338-340', 'SOURCE')

UNREACHABLE['Note.keys'] = ('no_trigger_in_app',
  'No caller. The keys() calls in the source root are on JSON objects and return iterators (CardBrowser.java 646, Tags.java 73), not on Note receivers. The bytecode call list (auto_calls.json) has no edge into Note.keys. The body casts Object[] to String[] (Note.java 185), which would fail at run time if it were ever called.',
  'com/ichi2/libanki/Note.java:184-186; com/ichi2/anki/CardBrowser.java:646; com/ichi2/libanki/Tags.java:73', 'SOURCE')

UNREACHABLE['Note.setItem'] = ('no_trigger_in_app',
  'No caller. A grep of the source root for setItem( finds no call, and the bytecode call list (auto_calls.json) has no edge into Note.setItem. Its reader getItem is reachable, but nothing writes a field by key.',
  'com/ichi2/libanki/Note.java:217-219', 'SOURCE')

# ---- part 095 (2026-10-28)
# AnkiDroid batch 095 (LABEL helper): libanki Sched part 1, 40 methods, all REACHABLE (no UNREACHABLE entries).
# The row list is in graphs/AnkiDroid/parts/label_095.md. Automatic bytecode CALL edges are not written here.

e('Sched._deckNewLimit(long,Method)', 'Sched._deckNewLimitSingle', 'CALL',
  'a new-card fetch (getCard, _getCard, _getNewCard, _fillNew) computes the deck new limit through _deckNewLimit(long), which passes null so the default Method _deckNewLimitSingle is invoked reflectively',
  cls='non_standard',
  via=['reflection (Sched.class.getDeclaredMethod + Method.invoke)'],
  evidence='SRC com/ichi2/libanki/Sched.java:695-717 (697-698, 706);com/ichi2/libanki/Sched.java:690-692 (691); com/ichi2/libanki/Sched.java:588-634 (597)',
  note='Reflective call: Method.invoke at line 706 on the default Method set at lines 697-698. No gate constant applies; env and needs_state are unset.')

e('Sched._deckNewLimit(long,Method)', 'Sched._deckRevLimitSingle', 'CALL',
  'a review-card fetch (_getRevCard, _fillRev) computes the deck review limit through _deckRevLimit(long), which passes the _deckRevLimitSingle Method object to _deckNewLimit(long,Method)',
  cls='non_standard',
  via=['reflection (Sched.class.getDeclaredMethod + Method.invoke)'],
  evidence='SRC com/ichi2/libanki/Sched.java:695-717 (706);com/ichi2/libanki/Sched.java:1195-1201 (1197); com/ichi2/libanki/Sched.java:1249-1312 (1258)',
  note='Reflective call: Method.invoke at line 706 on the Method built at line 1197. No gate constant applies; env and needs_state are unset.')

e('Sched._checkLeech', 'Leech$LeechHook.runHook', 'CALL',
  'a review card answered with ease 1 reaches the leech threshold while a reviewer activity is attached to the scheduler; Hooks.runHook("leech") calls the always-on LeechHook',
  cls='explicit',
  evidence='SRC com/ichi2/libanki/Sched.java:1365, 1702,1721-1723, 2487-2489; com/ichi2/libanki/hooks/Hooks.java:52, 114-121; com/ichi2/libanki/hooks/Leech.java:35, 60-62; com/ichi2/anki/Reviewer.java:115',
  note='MISSING GATE MG892: the leech hook runs only when Sched.mContextReference is non-null (set by Reviewer.setContext at Reviewer.java:115; Sched.java:2487-2489). No constant covers an activity context reference, so env and needs_state are unset.')

# ---- part 096 (2026-10-28)
# AnkiDroid batch 096 (LABEL helper): Sched part 2, 40 methods.
# The row list is in graphs/AnkiDroid/parts/label_096.md.
# No UNREACHABLE entries: all 40 methods have a route from an entry point.
# Only two e() edges: the reflective calls from Sched._walkingCount to the count functions
# that _resetNewCount and _resetRevCount register (no automatic edge exists for them).

e('Sched._walkingCount', 'Sched._cntFnNew', 'CALL',
  'reflective call: _walkingCount invokes the count function that _resetNewCount passes to it (Method.invoke)',
  cls='non_standard',
  via=['reflection (Sched.class.getDeclaredMethod + Method.invoke)'],
  env=None,
  evidence='SRC com/ichi2/libanki/Sched.java:337-353; SRC com/ichi2/libanki/Sched.java:564-565')

e('Sched._walkingCount', 'Sched._cntFnRev', 'CALL',
  'reflective call: _walkingCount invokes the count function that _resetRevCount passes to it (Method.invoke)',
  cls='non_standard',
  via=['reflection (Sched.class.getDeclaredMethod + Method.invoke)'],
  env=None,
  evidence='SRC com/ichi2/libanki/Sched.java:337-353; SRC com/ichi2/libanki/Sched.java:1225-1226')

# ---- part 097 (2026-10-28)
# AnkiDroid batch 097 (LABEL helper): Sched part 3, 40 methods of com/ichi2/libanki/Sched.java.
# The row list is in graphs/AnkiDroid/parts/label_097.md.
# No e() edges: every outgoing call from a Sched method in this batch is an automatic CALL edge, and the
# entries into these methods come from callers owned by other batches (DeckTask, Reviewer, CardContentProvider,
# DeckPicker, AbstractFlashcardViewer, NoteEditor, StudyOptionsFragment, AnkiPackageExporter, Anki2Importer,
# CustomStudyDialog, DeckPickerContextMenu, WidgetStatus).

UNREACHABLE['Sched.dueForecast()'] = ('no_trigger_in_app',
  'The method calls dueForecast(7). No caller exists in the source root: grep for dueForecast finds only the declarations in Sched.java 212-217.',
  'com/ichi2/libanki/Sched.java:212-217', 'SOURCE')

UNREACHABLE['Sched.dueForecast(int)'] = ('no_trigger_in_app',
  'The body is a TODO stub that returns 0. Its only caller is dueForecast() (Sched.java 213), which has no caller.',
  'com/ichi2/libanki/Sched.java:212-220', 'SOURCE')

UNREACHABLE['Sched.getName'] = ('no_trigger_in_app',
  'The method returns mName. No caller exists in the source root: grep for getName on a Sched receiver (getSched().getName, mSched.getName, sched.getName) finds only the declaration.',
  'com/ichi2/libanki/Sched.java:2334-2336', 'SOURCE')

UNREACHABLE['Sched.leechActionSuspend'] = ('no_trigger_in_app',
  'No caller exists in the source root: grep for leechActionSuspend finds only the declaration.',
  'com/ichi2/libanki/Sched.java:2476-2484', 'SOURCE')

UNREACHABLE['Sched.maybeRandomizeDeck()'] = ('no_trigger_in_app',
  'The no-argument overload only calls maybeRandomizeDeck(null) (Sched.java 2293). The only other caller in the source root uses the Long overload (Anki2Importer 695). No caller of the no-argument overload exists.',
  'com/ichi2/libanki/Sched.java:2292-2294; com/ichi2/libanki/importer/Anki2Importer.java:692-696', 'SOURCE')

UNREACHABLE['Sched.rebuildDyn()'] = ('no_trigger_in_app',
  'The no-argument overload only calls rebuildDyn(0) (Sched.java 1527). Every caller in the source root passes a deck id: DeckTask (731) passes col.getDecks().selected(). No caller of the no-argument overload exists.',
  'com/ichi2/libanki/Sched.java:1526-1528; com/ichi2/async/DeckTask.java:728-733', 'SOURCE')

UNREACHABLE['Sched.removeLrn()'] = ('no_trigger_in_app',
  'The method only calls removeLrn(null) (Sched.java 1154). No caller exists in the source root: grep for removeLrn finds only the two declarations and that call.',
  'com/ichi2/libanki/Sched.java:1153-1155', 'SOURCE')

# ---- suppressed auto edge (2026-10-28, orchestrator, build 146): dueForecast() has no caller and is UNREACHABLE, so its auto CALL edge into dueForecast(int) starts in an UNREACHABLE method
sup(('Sched.dueForecast()', 'Sched.dueForecast(int)'))

# ---- part 098 (2026-10-28)
# AnkiDroid batch 098 (LABEL helper): libanki Sched, part 4 (16 methods).
# The row list is in graphs/AnkiDroid/parts/label_098.md.
# No e() edges: the methods in this batch have no outgoing edges except automatic CALL edges and
# JDK dispatch (Collections.sort), and the edges into them come from callers owned by other batches
# (DeckTask, StudyOptionsFragment, CustomStudyDialog, DeckPickerContextMenu, NoteEditor, Syncer,
# WidgetStatus, CardContentProvider, DeckPicker).

UNREACHABLE['Sched.setToday'] = ('no_trigger_in_app',
  'Plain setter of mToday. A text search of the whole app source root for setToday finds only this declaration, so no app code calls it.',
  'com/ichi2/libanki/Sched.java:2344-2346', 'SOURCE')

UNREACHABLE['Sched$DeckDueTreeNode.toString'] = ('no_trigger_in_app',
  'Overrides Object.toString (String.format over the names, did, depth, counts and children). No explicit call exists in the app source root. The app code that reads DeckDueTreeNode objects reads their fields, not the node as a string (WidgetStatus.java:126-128 reads newCount, lrnCount and revCount; CardContentProvider.java:367 iterates the list). Confidence is moderate: the check covered Timber, format and concatenation lines that mention node, deck or children, not every expression.',
  'com/ichi2/libanki/Sched.java:2554-2557; com/ichi2/widget/WidgetStatus.java:116-128; com/ichi2/anki/provider/CardContentProvider.java:364-367', 'SOURCE')

# ---- part 099 (2026-10-28)
# AnkiDroid batch 099 (LABEL helper): libanki Sound, 28 methods.
# 1 UNREACHABLE entry (Sound.resetSounds(int)), 4 FRAMEWORK edges from Sound.playSound (3-arg) to its listener callbacks.
# The row list is in graphs/AnkiDroid/parts/label_099.md. Automatic bytecode CALL edges are not written here.

e('Sound.playSound(String,OnCompletionListener,VideoView)', 'Sound$1.onAudioFocusChange', 'FRAMEWORK',
  'an audio focus change from the system or another app runs the callback that playSound registers through requestAudioFocus',
  cls='standard',
  note='MISSING GATE MG934: the callback fires only when the system or another app changes audio focus while a sound plays. No constant covers audio focus, so env and needs_state are unset. The source is the registration point (requestAudioFocus at Sound.java:329-330), as in label_001.py. The callback body is empty.',
  evidence='SRC com/ichi2/libanki/Sound.java:106-109, 329-330; FW-SRC media/java/android/media/AudioManager.java:2136-2144, 2190-2193')

e('Sound.playSound(String,OnCompletionListener,VideoView)', 'Sound$2.onVideoSizeChanged', 'FRAMEWORK',
  'a video file with a thumbnail is played in VideoPlayer and the player reports its video size, which runs the callback registered in playSound',
  cls='standard',
  note='MISSING GATE MG933: the callback needs a video file with a thumbnail and a VideoView (Sound.java:307-309). No constant covers this, so env and needs_state are unset. The source is the registration point (setOnVideoSizeChangedListener at Sound.java:309), as in label_001.py.',
  evidence='SRC com/ichi2/libanki/Sound.java:307-314; FW-SRC media/java/android/media/MediaPlayer.java:3286-3290')

e('Sound.playSound(String,OnCompletionListener,VideoView)', 'Sound$3.onPrepared', 'FRAMEWORK',
  'a playable sound file is prepared asynchronously by MediaPlayer and the framework calls the prepared listener',
  cls='standard',
  note='MISSING GATE MG932: the callback needs a [sound:] marker whose media file exists and can be prepared by MediaPlayer. No constant covers this, so env and needs_state are unset. The source is the registration point (setOnPreparedListener at Sound.java:319), as in label_001.py.',
  evidence='SRC com/ichi2/libanki/Sound.java:319-328; FW-SRC media/java/android/media/MediaPlayer.java:3191, 3203-3205')

e('Sound.playSound(String,OnCompletionListener,VideoView)', 'Sound$PlayAllCompletionListener.onCompletion', 'FRAMEWORK',
  'a playable sound finishes and the framework calls the completion listener set by playSound',
  cls='standard',
  note='MISSING GATE MG932: the callback needs a [sound:] marker whose media file exists and can be prepared by MediaPlayer. No constant covers this, so env and needs_state are unset. The source is the registration point (setOnCompletionListener at Sound.java:326), as in label_001.py.',
  evidence='SRC com/ichi2/libanki/Sound.java:325-327, 387-395; FW-SRC media/java/android/media/MediaPlayer.java:3235-3240')

UNREACHABLE['Sound.resetSounds(int)'] = ('no_trigger_in_app', 'Declared at Sound.java lines 121-123 with no caller in the source root. A grep for resetSounds over src/main/java finds only the no-argument calls at AbstractFlashcardViewer.java:544 and 2078 and no call with an int argument. auto_calls.json has no record whose dst is Sound.resetSounds(int).', 'SRC com/ichi2/libanki/Sound.java:121-123; com/ichi2/anki/AbstractFlashcardViewer.java:544, 2078', 'SOURCE')

# ---- part 100 (2026-10-28)
# AnkiDroid batch 100 (LABEL helper): libanki Stats (32 methods across Stats, Stats$1, Stats$ChartType) and Storage.
# The row list is in graphs/AnkiDroid/parts/label_100.md. Automatic bytecode CALL edges are not written here.
# Only one batch method is UNREACHABLE (Storage.<init>); the others are REACHABLE and need no entry here.

e('Stats.calculateBreakdown', 'Stats$1.compare', 'CALL',
  'The hourly breakdown chart sorts its rows with an anonymous Comparator (Stats$1). Collections.sort calls the compare method through library dispatch, so there is no bytecode CALL edge from calculateBreakdown to compare.',
  cls='non_standard',
  via=['library dispatch (java.util.Collections.sort invokes Comparator.compare on the anonymous Stats$1 instance)'],
  evidence='SRC com/ichi2/libanki/Stats.java:852-858; INFERRED java.util.Collections.sort calls Comparator.compare (java.util is not in fw_src)',
  note='No gate constant applies. The compare call happens only when the list has two or more rows (JDK behaviour, INFERRED).')

e('Stats.calculateDue(Context,AxisType)', 'AdvancedStatistics.runFilter', 'CALL',
  'The forecast entry point runs the advancedStatistics hook through Hooks.runFilter. The hook list holds AdvancedStatistics only when the preference advanced_statistics_enabled is true, so the hook runFilter runs only then.',
  cls='non_standard',
  via=['hook registry dispatch (Hooks.runFilter loops over the Hook objects registered under the key advancedStatistics)'],
  evidence='SRC com/ichi2/libanki/Stats.java:308-311; com/ichi2/libanki/hooks/Hooks.java:61-62, 138-150; com/ichi2/libanki/hooks/AdvancedStatistics.java:141-148',
  note='MISSING GATE MG943: the preference advanced_statistics_enabled (default false, Hooks.java:61) must be true for AdvancedStatistics to be installed. Without it, calculateDue(AxisType) at Stats.java:331 runs instead.')

UNREACHABLE['Storage.<init>'] = ('no_trigger_in_app',
  'Storage declares no constructor, so only the implicit default constructor exists. Nothing in the source roots constructs it: there is no new Storage expression, no subclass of Storage, and no Storage.class reference. Every use of Storage is a static call (Storage.Collection, Storage.addIndices), so no instance is ever created.',
  'com/ichi2/libanki/Storage.java:35, 40-41; com/ichi2/async/DeckTask.java:790', 'SOURCE')

# ---- part 101 (2026-10-28)
# AnkiDroid batch 101 (LABEL helper): com.ichi2.libanki.Tags, 19 methods. The full row list is in
# graphs/AnkiDroid/parts/label_101.md.
# Four UNREACHABLE entries (no_trigger_in_app). The other 15 methods are REACHABLE and need no entry here.
# No e() calls: every link in the routes is an ordinary Java call (CALL, written by the builder).

UNREACHABLE['Tags.addToStr'] = ('no_trigger_in_app', 'No live route: the only call to addToStr is in bulkAdd(List,String,boolean) (Tags.java:262), and that method has no live caller (bulkAdd(List,String) and bulkRem have none). A grep of the app source tree finds no other call to addToStr.', 'com/ichi2/libanki/Tags.java:262, 315-323', 'SOURCE')

UNREACHABLE['Tags.bulkAdd(List,String)'] = ('no_trigger_in_app', 'No caller: the body is only bulkAdd(ids, tags, true) (Tags.java:221). A grep of the app source tree finds no call to bulkAdd(List,String). The FIXME at Tags.java:212-219 says it must be fixed before use.', 'com/ichi2/libanki/Tags.java:212-222', 'SOURCE')

UNREACHABLE['Tags.bulkAdd(List,String,boolean)'] = ('no_trigger_in_app', 'Callers are bulkAdd(List,String) (Tags.java:221) and bulkRem (Tags.java:282); neither has a caller. The javadoc at Tags.java:225-228 says the method is unused in AnkiDroid and its behaviour is currently incorrect.', 'com/ichi2/libanki/Tags.java:220-222, 225-228, 229-278, 282', 'SOURCE')

UNREACHABLE['Tags.bulkRem'] = ('no_trigger_in_app', 'No caller: a grep of the app source tree finds no call to bulkRem. Its body is only bulkAdd(ids, tags, false) (Tags.java:282), which has no live caller.', 'com/ichi2/libanki/Tags.java:281-283', 'SOURCE')

# ---- sup for part 101 (2026-10-28, orchestrator, build 150): automatic CALL edges between UNREACHABLE Tags methods
sup(('Tags.bulkAdd(List,String,boolean)', 'Tags.addToStr'))
sup(('Tags.bulkAdd(List,String)', 'Tags.bulkAdd(List,String,boolean)'))
sup(('Tags.bulkRem', 'Tags.bulkAdd(List,String,boolean)'))

# ---- part 102 (2026-10-28)
# AnkiDroid batch 102 (LABEL helper). libanki Utils, 40 methods. The full row list is in
# graphs/AnkiDroid/parts/label_102.md.
#
# One e() call: the FRAMEWORK edge from getImportableDecks to its anonymous FileFilter, because the JDK
# calls FileFilter.accept and auto_calls.json does not record that step. Every other caller into these methods is a bytecode CALL edge that is already in
# graphs/AnkiDroid/auto_calls.json, so none is written here. The UNREACHABLE entries below are the
# ten methods with no route from an entry point (8 no_trigger_in_app, 2 branch_never_taken).
# Text is repeated inline on each entry, with no module-level names.

e('libanki.Utils.getImportableDecks', 'libanki.Utils$1.accept', 'FRAMEWORK',
  'the directory listing hands each entry to the anonymous FileFilter: java.io.File.listFiles(FileFilter) calls FileFilter.accept, which keeps .apkg files',
  cls='non_standard',
  via=['java.io.File.listFiles(FileFilter) calls FileFilter.accept once per directory entry (JDK library dispatch; fw_src File.java is a 404 stub)'],
  evidence='SRC com/ichi2/libanki/Utils.java:904-921, 910-914; INFERRED java.io.File.listFiles calls FileFilter.accept once per entry (JDK behaviour, not in fw_src)',
  note='The listing runs only when the AnkiDroid directory exists and is a directory (Utils.java:909).')

UNREACHABLE['libanki.Utils.<init>'] = ('no_trigger_in_app', "Private no-argument constructor of a class that holds only static members (the comment says it prevents instantiation). The grep for 'new Utils(' over the source root finds no match, and auto_calls.json has no record that targets libanki.Utils.<init>. Nothing constructs the class.", 'SRC com/ichi2/libanki/Utils.java:109-112; grep new Utils( over the source root: no match', 'SOURCE')

UNREACHABLE['libanki.Utils._incGuid'] = ('branch_never_taken', "Only called from incGuid (Utils.java:432) and from itself (440). incGuid is reached only through Anki2Importer.java:295, which sits behind the guard at 291-293 (return false while mDupeOnSchemaChange is false). The field is set false in the constructor (84). The only setter, setDupeOnSchemaChange (770-772), has no caller, so the branch is never taken.", 'SRC com/ichi2/libanki/Utils.java:431-445; com/ichi2/libanki/importer/Anki2Importer.java:82-86, 286-297, 770-772', 'SOURCE')

UNREACHABLE['libanki.Utils.compress'] = ('no_trigger_in_app', "Deflater helper with no caller. The grep for compress( over the source root finds only the definition and Bitmap.compress at BasicImageFieldController.java:204, which is a Bitmap method and not this one. auto_calls.json has no record that targets it.", 'SRC com/ichi2/libanki/Utils.java:670-684; com/ichi2/anki/multimediacard/fields/BasicImageFieldController.java:200-206', 'SOURCE')

UNREACHABLE['libanki.Utils.fmtPercentage(Double)'] = ('no_trigger_in_app', "Its body calls the two-argument overload. The grep for fmtPercentage( over the source root finds only the two definitions and the call at Utils.java:224. No caller of this one-argument overload exists, and auto_calls.json has no record that targets it.", 'SRC com/ichi2/libanki/Utils.java:221-232', 'SOURCE')

UNREACHABLE['libanki.Utils.fmtPercentage(Double,int)'] = ('no_trigger_in_app', "The only caller is fmtPercentage(Double) (Utils.java:224), and that overload has no caller (see the previous entry). auto_calls.json has one record for this overload, from fmtPercentage(Double) at Utils.java:224.", 'SRC com/ichi2/libanki/Utils.java:224, 226-232', 'SOURCE')

UNREACHABLE['libanki.Utils.ids2str(JSONArray)'] = ('no_trigger_in_app', "No call site passes a JSONArray. The grep for ids2str( over the source root lists every call site, and each argument is an int[], long[], Long[], List or the result of arrayList2array. auto_calls.json resolves all ids2str calls to the int[], long[], Long[] or List overloads, with zero records for JSONArray.", 'SRC com/ichi2/libanki/Utils.java:346-368; com/ichi2/libanki/Collection.java:818-830, 934-946, 1322-1330; com/ichi2/libanki/sync/Syncer.java:830-842', 'SOURCE')

UNREACHABLE['libanki.Utils.incGuid'] = ('branch_never_taken', "Anki2Importer._uniquifyNote calls it at line 295 only after the guard at 291-293 returns false when mDupeOnSchemaChange is false. The constructor sets that field to false (Anki2Importer.java:84). The only setter, setDupeOnSchemaChange (770-772), has no caller (the grep over the source root finds only its definition), so the call at 295 never runs.", 'SRC com/ichi2/libanki/Utils.java:431-433; com/ichi2/libanki/importer/Anki2Importer.java:82-86, 286-297, 768-772', 'SOURCE')

UNREACHABLE['libanki.Utils.printDate'] = ('no_trigger_in_app', "Debug logger with no caller. The grep for printDate( over the source root finds only the definition, and auto_calls.json has no record that targets it.", 'SRC com/ichi2/libanki/Utils.java:752-758', 'SOURCE')

UNREACHABLE['libanki.Utils.replaceLineBreak'] = ('no_trigger_in_app', "Helper with no caller. The grep for replaceLineBreak( over the source root finds only the definition, and auto_calls.json has no record that targets it.", 'SRC com/ichi2/libanki/Utils.java:584-586', 'SOURCE')

UNREACHABLE['libanki.Utils.toPrimitive(Long[])'] = ('no_trigger_in_app', "All seven call sites pass a Collection<Long>, so they resolve to toPrimitive(Collection). auto_calls.json has seven records for the Collection overload and none for the Long[] overload.", 'SRC com/ichi2/libanki/Utils.java:807-815; com/ichi2/libanki/Sched.java:2258-2270; com/ichi2/libanki/Models.java:515-519, 574-578, 792-795, 1003-1008; com/ichi2/libanki/Finder.java:890-896', 'SOURCE')

# ---- sup for part 102 (2026-10-28, orchestrator, build 151): automatic CALL edges inside UNREACHABLE Utils methods
sup(('libanki.Utils.fmtPercentage(Double)', 'libanki.Utils.fmtPercentage(Double,int)'))
sup(('libanki.Utils.incGuid', 'libanki.Utils._incGuid'))
sup(('libanki.Utils._incGuid', 'libanki.Utils._incGuid'))
# dead branch: mDupeOnSchemaChange is false in the app (Anki2Importer.java:84), so the call at 295 is never reached
sup(('Anki2Importer._uniquifyNote', 'libanki.Utils.incGuid'))

# ---- part 103 (2026-10-28)
# Batch 103: libanki.Utils part 2 (utcOffset, writeToFile, Utils$1.<init>, Utils$1.accept).
# All four methods are REACHABLE (see label_103.md), so there are no UNREACHABLE entries.
# This batch owns no e() edges. The FRAMEWORK edge libanki.Utils.getImportableDecks ->
# libanki.Utils$1.accept belongs to batch 102 (getImportableDecks is in batch_102.txt).

# ---- part 104 (2026-10-28)
# AnkiDroid batch 104 (LABEL helper): libanki hooks (Hook, Hooks, Leech, ChessFilter, HebrewFixFilter, ExternalHookLoader,
# AdvancedStatistics inner classes), and the AnkiPackageExporter ZipFile class. 32 methods.
# The row list is in graphs/AnkiDroid/parts/label_104.md. Automatic bytecode CALL edges are not written here.
# Two e() edges are written (the registry dispatch into the leech hook, and the UI-thread post of its toast).
# 19 methods are UNREACHABLE (18 no_trigger_in_app, 1 branch_never_taken). The rest are REACHABLE and need no entry here.

e('Hooks.runHook', 'Leech$LeechHook.runHook', 'CALL',
  'a review answer makes a card a leech: Hooks.runHook loops over the hooks registered under the key leech and calls runHook on each, which is LeechHook.runHook',
  cls='non_standard',
  via=['hook registry dispatch (Hooks.runHook loops over the Hook objects registered under the key leech and calls func.runHook; the only registrant is Leech.LeechHook, installed by the Hooks constructor)'],
  evidence='SRC com/ichi2/libanki/hooks/Hooks.java:52, 114-128; com/ichi2/libanki/hooks/Leech.java:33-37, 60-62; com/ichi2/libanki/Sched.java:1721-1723',
  note='MISSING GATE MG982: the card must reach the leech threshold of its deck on a lapse answer (Sched.java:1697-1702 and 1365). No predefined STATE constant covers this, so env and needs_state are unset. The call at Sched.java:1723 also needs mContextReference to be set (Reviewer.java:115), otherwise the block at Sched.java:1721 is skipped.')

e('Leech$LeechHook.runHook', 'Leech$LeechHook$1.run', 'ASYNC',
  'the leech hook posts the toast Runnable to the UI thread, because the answer runs on the background DeckTask thread',
  cls='non_standard',
  via=['Handler message dispatch (Activity.runOnUiThread posts the Runnable to the UI-thread Handler when called off the UI thread; the Handler runs Message.callback.run)'],
  evidence='SRC com/ichi2/libanki/hooks/Leech.java:38, 46-51; FW-SRC core/java/android/app/Activity.java:6170-6176; FW-SRC core/java/android/os/Handler.java:355-358, 789-791',
  note='MISSING GATE MG983: the Activity passed to the hook must be non-null (Leech.java:38). It is the Reviewer, held by the WeakReference set at Reviewer.java:115 and still alive. No predefined constant covers this, so env and needs_state are unset. runOnUiThread posts only when the current thread is not the UI thread (Activity.java:6171-6172).')

UNREACHABLE['AdvancedStatistics$ArrayUtils.createIntMatrix'] = ('no_trigger_in_app',
  'Declared in the private inner class ArrayUtils. The field ArrayUtils (AdvancedStatistics.java:136) is used for transposeMatrix, stringToLongArray, formatMatrix, createDoubleMatrix and toIntMatrix only. Nothing in the source root calls createIntMatrix.',
  'com/ichi2/libanki/hooks/AdvancedStatistics.java:136, 1119-1129', 'SOURCE')

UNREACHABLE['AdvancedStatistics$ArrayUtils.append'] = ('no_trigger_in_app',
  'The only calls to ArrayUtils.append are in commented-out lines (AdvancedStatistics.java:340 and 393). No live caller exists in the source root.',
  'com/ichi2/libanki/hooks/AdvancedStatistics.java:339-340, 393, 1162-1169', 'SOURCE')

UNREACHABLE['AdvancedStatistics$ArrayUtils.nCols'] = ('no_trigger_in_app',
  'The only calls to ArrayUtils.nCols are in the commented-out lines 339-340. No live caller exists in the source root.',
  'com/ichi2/libanki/hooks/AdvancedStatistics.java:339-340, 1175-1179', 'SOURCE')

UNREACHABLE['AdvancedStatistics$ArrayUtils.nRows'] = ('no_trigger_in_app',
  'No call to nRows exists anywhere in the source root (grep finds only the declaration at line 1171).',
  'com/ichi2/libanki/hooks/AdvancedStatistics.java:1171-1173', 'SOURCE')

UNREACHABLE['AdvancedStatistics$Card.getId'] = ('no_trigger_in_app',
  'Declared in the private inner class Card. No call to getId() exists in AdvancedStatistics.java (grep finds only the declaration), and the class is private, so no other file can call it.',
  'com/ichi2/libanki/hooks/AdvancedStatistics.java:399, 442-444', 'SOURCE')

UNREACHABLE['AdvancedStatistics$Card.setDue'] = ('no_trigger_in_app',
  'Declared in the private inner class Card. No call to setDue exists in AdvancedStatistics.java (grep finds only the declaration). The class is private, so no other file can call it.',
  'com/ichi2/libanki/hooks/AdvancedStatistics.java:399, 466-468', 'SOURCE')

UNREACHABLE['AdvancedStatistics$Card.setFactor'] = ('no_trigger_in_app',
  'Declared in the private inner class Card. The only call is the commented-out line 836 (c.setFactor(factor)). No live caller exists.',
  'com/ichi2/libanki/hooks/AdvancedStatistics.java:399, 458-460, 836', 'SOURCE')

UNREACHABLE['AdvancedStatistics$Card.toString'] = ('no_trigger_in_app',
  'Declared in the private inner class Card. The implicit calls come only from string concatenation in ReviewOutcome.toString (line 1499) and in Review.writeLog (lines 1715-1716). Both are unreachable (see the rows for those methods), so nothing reaches Card.toString.',
  'com/ichi2/libanki/hooks/AdvancedStatistics.java:399, 409-412, 1497-1499, 1710-1716', 'SOURCE')

UNREACHABLE['AdvancedStatistics$Review.writeLog'] = ('no_trigger_in_app',
  'Private method of the inner class Review. Its only call is commented out (AdvancedStatistics.java:1685, //writeLog(newCard, outcomeProb)). No live caller exists.',
  'com/ichi2/libanki/hooks/AdvancedStatistics.java:1685, 1710-1714', 'SOURCE')

UNREACHABLE['AdvancedStatistics$ReviewOutcome.toString'] = ('no_trigger_in_app',
  'Declared in the private inner class ReviewOutcome. The only mention in a call position is the commented-out Timber line at 1680. ReviewOutcome has no live string concatenation in the source root.',
  'com/ichi2/libanki/hooks/AdvancedStatistics.java:1474, 1497-1500, 1680', 'SOURCE')

UNREACHABLE['ExternalHookLoader.<init>'] = ('no_trigger_in_app',
  'The class ExternalHookLoader has no construction site in the source root (grep for ExternalHookLoader outside its own file finds nothing). Without an instance, its constructor never runs.',
  'com/ichi2/libanki/hooks/ExternalHookLoader.java:16, 31-34', 'SOURCE')

UNREACHABLE['ExternalHookLoader.importExternalHook'] = ('no_trigger_in_app',
  'Public method of ExternalHookLoader. The class is never instantiated and the method has no caller in the source root (grep finds no reference outside the file).',
  'com/ichi2/libanki/hooks/ExternalHookLoader.java:43-77', 'SOURCE')

UNREACHABLE['ExternalHookLoader.prepareDex'] = ('no_trigger_in_app',
  'Private method. Its only caller is PrepareDexTask.doInBackground (line 130), which is created only in importExternalHook (line 52). importExternalHook has no caller, so prepareDex never runs.',
  'com/ichi2/libanki/hooks/ExternalHookLoader.java:80-112, 128-130, 52', 'SOURCE')

UNREACHABLE['ExternalHookLoader$PrepareDexTask.<init>'] = ('no_trigger_in_app',
  'Implicit constructor of the private inner class PrepareDexTask. The only creation site is line 52, inside importExternalHook, which has no caller.',
  'com/ichi2/libanki/hooks/ExternalHookLoader.java:52, 114', 'SOURCE')

UNREACHABLE['ExternalHookLoader$PrepareDexTask.doInBackground'] = ('no_trigger_in_app',
  'AsyncTask calls doInBackground only after execute() on a PrepareDexTask. The only execute() call is at line 52, inside importExternalHook, which has no caller.',
  'com/ichi2/libanki/hooks/ExternalHookLoader.java:52, 128-132', 'SOURCE')

UNREACHABLE['ExternalHookLoader$PrepareDexTask.onCancelled'] = ('no_trigger_in_app',
  'AsyncTask calls onCancelled only for a task that was started by execute(). The only execute() call is at line 52, inside importExternalHook, which has no caller.',
  'com/ichi2/libanki/hooks/ExternalHookLoader.java:52, 116-120', 'SOURCE')

UNREACHABLE['ExternalHookLoader$PrepareDexTask.onPostExecute'] = ('no_trigger_in_app',
  'AsyncTask calls onPostExecute only for a task that was started by execute(). The only execute() call is at line 52, inside importExternalHook, which has no caller.',
  'com/ichi2/libanki/hooks/ExternalHookLoader.java:52, 122-126', 'SOURCE')

UNREACHABLE['Hook.hashCode'] = ('no_trigger_in_app',
  'Hooks keeps Hook objects in an ArrayList (Hooks.java:75, 85, 100) and compares them with equals (Hooks.java:79, 99). The Map key is a String (Hooks.java:36). No HashSet or HashMap keyed by a Hook exists in the source root, so nothing calls Hook.hashCode.',
  'com/ichi2/libanki/hooks/Hook.java:34-40; com/ichi2/libanki/hooks/Hooks.java:36, 73-87, 96-105', 'SOURCE')

UNREACHABLE['Hook.runHook'] = ('branch_never_taken',
  'The base body is empty (Hook.java:64-66). Hooks.runHook calls func.runHook (Hooks.java:121), but the only key dispatched through runHook is leech (Sched.java:1723), and its only registrant is LeechHook, which overrides runHook (Leech.java:35). So the base body never runs.',
  'com/ichi2/libanki/hooks/Hook.java:64-66; com/ichi2/libanki/hooks/Hooks.java:114-128; com/ichi2/libanki/hooks/Leech.java:33-37, 61; com/ichi2/libanki/Sched.java:1723', 'SOURCE')

# ---- sup for part 104 (2026-10-28, orchestrator, build 153): automatic CALL edges into UNREACHABLE hook and ExternalHookLoader methods
# the only registrant of the leech hook is LeechHook, which overrides runHook, so the base body never runs
sup(('Hooks.runHook', 'Hook.runHook'))
sup(('ExternalHookLoader.importExternalHook', 'ExternalHookLoader$PrepareDexTask.<init>'))
sup(('ExternalHookLoader$PrepareDexTask.doInBackground', 'ExternalHookLoader.prepareDex'))

# ---- part 105 (2026-10-28)
# AnkiDroid batch 105 (LABEL helper): libanki importer package, 37 methods.
# 10 UNREACHABLE entries (all no_trigger_in_app), 27 REACHABLE rows in graphs/AnkiDroid/parts/label_105.md.
# No e() edges: the in-batch dispatch is covered by automatic CALL edges. Automatic bytecode CALL edges are not written here.

UNREACHABLE['Anki2Importer._mediaData(String)'] = ('no_trigger_in_app', 'One-argument helper with no call site: a grep over src main and androidTest finds no call with one argument. Its body delegates to the two-argument form (line 598), so no in-app path reaches it.', 'SRC com/ichi2/libanki/importer/Anki2Importer.java:597-599, 619, 627', 'SOURCE')

UNREACHABLE['Anki2Importer._srcMediaData'] = ('no_trigger_in_app', 'Protected body of a method that AnkiPackageImporter overrides. The two in-app call sites (Anki2Importer.java:591 and 652) dispatch on the AnkiPackageImporter receiver to AnkiPackageImporter._srcMediaData (AnkiPackageImporter.java:126-135). The base body runs only for a direct Anki2Importer receiver. No main code constructs Anki2Importer; the only direct receiver is in androidTest (ImportTest.java:62-97). Grep of src main and androidTest: call sites are 591 and 652 only. Conflict to report: automatic base-receiver CALL edges calls[6900] (_importStaticMedia, line 591) and calls[6927] (_mungeMedia, line 652) point at this body. They are suppression candidates for the orchestrator; no sup() is written here.', 'SRC com/ichi2/libanki/importer/Anki2Importer.java:618-620, 591, 652; SRC com/ichi2/libanki/importer/AnkiPackageImporter.java:126-135; ../../androidTest/java/com.ichi2.anki.tests/libanki/ImportTest.java:62-97', 'SOURCE')

UNREACHABLE['Anki2Importer.getAdded'] = ('no_trigger_in_app', 'Test-only getter. Anki2Importer.java:768 says the methods below are only used for testing. No call in src main. The androidTest callers are ImportTest.java:203, 209, 218 and 302.', 'SRC com/ichi2/libanki/importer/Anki2Importer.java:768, 780-782; ../../androidTest/java/com.ichi2.anki.tests/libanki/ImportTest.java:203, 209, 218, 302', 'SOURCE')

UNREACHABLE['Anki2Importer.getDupes'] = ('no_trigger_in_app', 'Test-only getter (see the comment at Anki2Importer.java:768). No call in src main. The androidTest callers are ImportTest.java:202, 208, 217 and 301.', 'SRC com/ichi2/libanki/importer/Anki2Importer.java:768, 775-777; ../../androidTest/java/com.ichi2.anki.tests/libanki/ImportTest.java:202, 208, 217, 301', 'SOURCE')

UNREACHABLE['Anki2Importer.getUpdated'] = ('no_trigger_in_app', 'Test-only getter (see the comment at Anki2Importer.java:768). No call in src main. The androidTest callers are ImportTest.java:204, 210, 219 and 303.', 'SRC com/ichi2/libanki/importer/Anki2Importer.java:768, 785-787; ../../androidTest/java/com.ichi2.anki.tests/libanki/ImportTest.java:204, 210, 219, 303', 'SOURCE')

UNREACHABLE['Anki2Importer.setDupeOnSchemaChange'] = ('no_trigger_in_app', 'Test-only setter (see the comment at Anki2Importer.java:768). No call in src main. The androidTest callers are ImportTest.java:147, 152, 158, 167, 181 and 186.', 'SRC com/ichi2/libanki/importer/Anki2Importer.java:768, 770-772; ../../androidTest/java/com.ichi2.anki.tests/libanki/ImportTest.java:147, 152, 158, 167, 181, 186', 'SOURCE')

UNREACHABLE['Importer.ts'] = ('no_trigger_in_app', 'Protected helper that increments mTs, with no call site. A grep over src main and androidTest for ts() finds only the definition at Importer.java:69.', 'SRC com/ichi2/libanki/importer/Importer.java:69-72', 'SOURCE')

UNREACHABLE['NoteImporter.<init>'] = ('no_trigger_in_app', 'Reached only from TextImporter.<init> (TextImporter.java:10-12). TextImporter is constructed only in androidTest (ImportTest.java:228 and 276). No main code constructs TextImporter or NoteImporter.', 'SRC com/ichi2/libanki/importer/NoteImporter.java:9-11; SRC com/ichi2/libanki/importer/TextImporter.java:10-12; ../../androidTest/java/com.ichi2.anki.tests/libanki/ImportTest.java:228, 276', 'SOURCE')

UNREACHABLE['NoteImporter.run'] = ('no_trigger_in_app', 'Empty body. No call site anywhere. TextImporter.run (TextImporter.java:14-17) overrides it with an empty body and no super call, and NoteImporter is never constructed directly.', 'SRC com/ichi2/libanki/importer/NoteImporter.java:13-16; SRC com/ichi2/libanki/importer/TextImporter.java:14-17', 'SOURCE')

UNREACHABLE['NoteImporter.getTotal'] = ('no_trigger_in_app', 'Getter for mTotal with no in-app caller. The only callers are androidTest ImportTest.java:234, 238, 249 and 255.', 'SRC com/ichi2/libanki/importer/NoteImporter.java:18-20; ../../androidTest/java/com.ichi2.anki.tests/libanki/ImportTest.java:234, 238, 249, 255', 'SOURCE')

# ---- sup for part 105 (2026-10-28, orchestrator, build 154): base-receiver dispatch into the overridden Anki2Importer._srcMediaData
# DeckTask constructs only AnkiPackageImporter, which overrides _srcMediaData, so the base body never runs
sup(('Anki2Importer._importStaticMedia', 'Anki2Importer._srcMediaData'))
sup(('Anki2Importer._mungeMedia', 'Anki2Importer._srcMediaData'))

# ---- part 106 (2026-10-28)
# AnkiDroid batch 106 (LABEL helper). TextImporter (4 methods), FullSyncer (4), HttpSyncer (26) and
# HttpSyncer$ProgressByteEntity (6). The full row list is in graphs/AnkiDroid/parts/label_106.md.
#
# Route ownership:
# - Automatic CALL edges from auto_calls.json are not repeated here. Exact CALL pairs whose target is a base
#   HttpSyncer method that the runtime receiver overrides point at the wrong node; they are named as suppress
#   candidates in the final answer (Connection.java:202, 322, 337; Syncer.java:89, 157, 170, 179, 197, 204, 212, 909).
#   The MediaSyncer.java:108 pair to base finish is live (RemoteMediaServer does not override finish).
# - The three FRAMEWORK edges start from the base req(...CancelCallback) node. The receiver variants
#   (@FullSyncer, @RemoteMediaServer) do not get them here.
#
# Gate: ENV_NETWORK on the three FRAMEWORK edges. No MG id is used and no MISSING GATE note is needed.

# --- ProgressByteEntity callbacks reached from the HTTP client while it sends the request body (req, HttpSyncer.java:210-236).
e('HttpSyncer.req(String,InputStream,int,JSONObject,CancelCallback)', 'HttpSyncer$ProgressByteEntity.writeTo', 'FRAMEWORK',
  'the HTTP client sends the request and writes the multipart body through the request entity',
  env=ENV_NETWORK,
  cls='non_standard',
  via=['Apache HttpClient 4.x DefaultHttpClient.execute (library source not read)'],
  evidence='SRC com/ichi2/libanki/sync/HttpSyncer.java:210, 213, 235-236; INFERRED (Apache HttpClient 4.x source not read)',
  note='The request entity is set at HttpSyncer.java:213 and executed at :236. The body is written by writeTo (HttpSyncer.java:393-406), which calls publishProgress (:400). The library dispatch is INFERRED (library source not read).')

e('HttpSyncer.req(String,InputStream,int,JSONObject,CancelCallback)', 'HttpSyncer$ProgressByteEntity.getContentLength', 'FRAMEWORK',
  'the HTTP client reads the request body length for the Content-Length header while it sends the request',
  env=ENV_NETWORK,
  cls='non_standard',
  via=['Apache HttpClient 4.x DefaultHttpClient.execute (library source not read)'],
  evidence='SRC com/ichi2/libanki/sync/HttpSyncer.java:210, 213, 235-236; INFERRED (Apache HttpClient 4.x source not read)',
  note='getContentLength returns mLength (HttpSyncer.java:416-418), set from the temp file length in the constructor (:383). The library dispatch is INFERRED (library source not read).')

e('HttpSyncer.req(String,InputStream,int,JSONObject,CancelCallback)', 'HttpSyncer$ProgressByteEntity.isRepeatable', 'FRAMEWORK',
  'the HTTP client asks whether the request body can be replayed when it retries or re-authenticates the request',
  env=ENV_NETWORK,
  cls='non_standard',
  via=['Apache HttpClient 4.x DefaultHttpClient.execute (library source not read)'],
  evidence='SRC com/ichi2/libanki/sync/HttpSyncer.java:210, 213, 235-236; INFERRED (Apache HttpClient 4.x source not read)',
  note='isRepeatable returns false (HttpSyncer.java:421-424). The route exists only on a library retry or re-authentication of the same request. The library dispatch is INFERRED (library source not read).')

# --- TextImporter: a stub whose only constructions are in the androidTest ImportTest.
UNREACHABLE['TextImporter.<init>'] = ('no_trigger_in_app',
  'Stub importer constructor. Only the androidTest ImportTest constructs TextImporter; the app source root has no call site.',
  'SRC com/ichi2/libanki/importer/TextImporter.java:10-12; SRC AnkiDroid/src/androidTest/java/com.ichi2.anki.tests/libanki/ImportTest.java:228, 276',
  'SOURCE')

UNREACHABLE['TextImporter.initMapping'] = ('no_trigger_in_app',
  'Empty stub body. Called only from the androidTest ImportTest on a TextImporter, which the app never constructs.',
  'SRC com/ichi2/libanki/importer/TextImporter.java:19-21; SRC AnkiDroid/src/androidTest/java/com.ichi2.anki.tests/libanki/ImportTest.java:229, 277',
  'SOURCE')

UNREACHABLE['TextImporter.run'] = ('no_trigger_in_app',
  'Empty stub body. Called only from the androidTest ImportTest on a TextImporter, which the app never constructs.',
  'SRC com/ichi2/libanki/importer/TextImporter.java:14-17; SRC AnkiDroid/src/androidTest/java/com.ichi2.anki.tests/libanki/ImportTest.java:230, 248, 253, 278',
  'SOURCE')

UNREACHABLE['TextImporter.setImportMode'] = ('no_trigger_in_app',
  'Empty stub body. Called only from the androidTest ImportTest on a TextImporter, which the app never constructs.',
  'SRC com/ichi2/libanki/importer/TextImporter.java:23-25; SRC AnkiDroid/src/androidTest/java/com.ichi2.anki.tests/libanki/ImportTest.java:247, 252',
  'SOURCE')

# --- HttpSyncer base bodies. HttpSyncer is never instantiated (no "new HttpSyncer" in the source root); every runtime
# receiver is a RemoteServer or FullSyncer, and each one overrides the method, so the base body never runs.
UNREACHABLE['HttpSyncer.applyChanges'] = ('no_trigger_in_app',
  'Base body returns null. Its only caller is Syncer.java:170 on a RemoteServer (Connection.java:280-281), which overrides applyChanges.',
  'SRC com/ichi2/libanki/sync/HttpSyncer.java:327-329; SRC com/ichi2/libanki/sync/Syncer.java:170; SRC com/ichi2/libanki/sync/RemoteServer.java:74-77; SRC com/ichi2/async/Connection.java:280-281',
  'SOURCE')

UNREACHABLE['HttpSyncer.applyChunk'] = ('no_trigger_in_app',
  'Base body is empty. Its only caller is Syncer.java:197 on a RemoteServer, which overrides applyChunk.',
  'SRC com/ichi2/libanki/sync/HttpSyncer.java:372-373; SRC com/ichi2/libanki/sync/Syncer.java:197; SRC com/ichi2/libanki/sync/RemoteServer.java:93-96',
  'SOURCE')

UNREACHABLE['HttpSyncer.chunk()'] = ('no_trigger_in_app',
  'Base body returns null. Its only caller is Syncer.java:179 on a RemoteServer, which overrides chunk(). Syncer.java:192 calls Syncer own chunk().',
  'SRC com/ichi2/libanki/sync/HttpSyncer.java:342-344; SRC com/ichi2/libanki/sync/Syncer.java:179, 192; SRC com/ichi2/libanki/sync/RemoteServer.java:86-90',
  'SOURCE')

UNREACHABLE['HttpSyncer.chunk(JSONObject)'] = ('no_trigger_in_app',
  'Base body returns null. No caller: every chunk call is the no-argument form (Syncer.java:179, 192).',
  'SRC com/ichi2/libanki/sync/HttpSyncer.java:337-339; SRC com/ichi2/libanki/sync/Syncer.java:179, 192, 497',
  'SOURCE')

UNREACHABLE['HttpSyncer.download'] = ('no_trigger_in_app',
  'Base body returns null. Its only caller is Connection.java:337 on a FullSyncer (Connection.java:318), which overrides download.',
  'SRC com/ichi2/libanki/sync/HttpSyncer.java:357-359; SRC com/ichi2/async/Connection.java:318, 337; SRC com/ichi2/libanki/sync/FullSyncer.java:76-80',
  'SOURCE')

UNREACHABLE['HttpSyncer.hostKey'] = ('no_trigger_in_app',
  'Base body returns null. Its only caller is Connection.java:202 on a RemoteServer (Connection.java:199), which overrides hostKey.',
  'SRC com/ichi2/libanki/sync/HttpSyncer.java:322-324; SRC com/ichi2/async/Connection.java:199, 202; SRC com/ichi2/libanki/sync/RemoteServer.java:43-54',
  'SOURCE')

UNREACHABLE['HttpSyncer.meta'] = ('no_trigger_in_app',
  'Base body returns null. Its only caller is Syncer.java:89 on a RemoteServer, which overrides meta.',
  'SRC com/ichi2/libanki/sync/HttpSyncer.java:352-354; SRC com/ichi2/libanki/sync/Syncer.java:89; SRC com/ichi2/libanki/sync/RemoteServer.java:57-71',
  'SOURCE')

UNREACHABLE['HttpSyncer.register'] = ('no_trigger_in_app',
  'Base body returns null. No caller in the source root. The string "register" is only compared in req (HttpSyncer.java:201).',
  'SRC com/ichi2/libanki/sync/HttpSyncer.java:444-446, 201',
  'SOURCE')

UNREACHABLE['HttpSyncer.req(String,int,InputStream)'] = ('no_trigger_in_app',
  'No caller. Every req call in the source root passes a String first, then an InputStream with or without an int after it. No call site passes an int before the InputStream.',
  'SRC com/ichi2/libanki/sync/HttpSyncer.java:137-139; SRC com/ichi2/libanki/sync/FullSyncer.java:80, 159; SRC com/ichi2/libanki/sync/RemoteMediaServer.java:133; SRC com/ichi2/libanki/sync/RemoteServer.java:50, 67, 108, 120',
  'SOURCE')

UNREACHABLE['HttpSyncer.sanityCheck2'] = ('no_trigger_in_app',
  'Base body returns null. Its only caller is Syncer.java:204 on a RemoteServer, which overrides sanityCheck2.',
  'SRC com/ichi2/libanki/sync/HttpSyncer.java:367-369; SRC com/ichi2/libanki/sync/Syncer.java:204; SRC com/ichi2/libanki/sync/RemoteServer.java:99-102',
  'SOURCE')

UNREACHABLE['HttpSyncer.start'] = ('no_trigger_in_app',
  'Base body returns null. Its only caller is Syncer.java:157 on a RemoteServer, which overrides start.',
  'SRC com/ichi2/libanki/sync/HttpSyncer.java:332-334; SRC com/ichi2/libanki/sync/Syncer.java:157; SRC com/ichi2/libanki/sync/RemoteServer.java:80-83',
  'SOURCE')

UNREACHABLE['HttpSyncer.upload'] = ('no_trigger_in_app',
  'Base body returns null. Its only caller is Connection.java:322 on a FullSyncer (Connection.java:318), which overrides upload.',
  'SRC com/ichi2/libanki/sync/HttpSyncer.java:362-364; SRC com/ichi2/async/Connection.java:318, 322; SRC com/ichi2/libanki/sync/FullSyncer.java:143-159',
  'SOURCE')

# --- ProgressByteEntity: the two methods no app code calls. Library dispatch is INFERRED (Apache HttpClient 4.x source not read).
UNREACHABLE['HttpSyncer$ProgressByteEntity.getContent'] = ('framework_never_calls',
  'INFERRED (Apache HttpClient 4.x source not read): the request body is read through writeTo, not getContent. App code calls getContent only on response entities.',
  'SRC com/ichi2/libanki/sync/HttpSyncer.java:409-412; SRC com/ichi2/async/Connection.java:223; SRC com/ichi2/libanki/sync/FullSyncer.java:84; INFERRED (Apache HttpClient 4.x source not read)',
  'SOURCE')

UNREACHABLE['HttpSyncer$ProgressByteEntity.isStreaming'] = ('framework_never_calls',
  'INFERRED (Apache HttpClient 4.x source not read): returns false (HttpSyncer.java:427-430), and the send path uses writeTo and getContentLength. No app code calls it.',
  'SRC com/ichi2/libanki/sync/HttpSyncer.java:427-430, 210, 236; INFERRED (Apache HttpClient 4.x source not read)',
  'SOURCE')

# ---- sup for part 106 (2026-10-28, orchestrator, build 155): automatic CALL edges into UNREACHABLE HttpSyncer methods that every runtime receiver overrides
# Connection.java:199 and 280 create RemoteServer, which overrides hostKey, meta, start, applyChanges, chunk(), applyChunk and sanityCheck2 (RemoteServer.java:44-100)
# Syncer is constructed only at Connection.java:281, with a RemoteServer, so the mServer calls in Syncer.sync never run the HttpSyncer bodies
# Connection.java:318 reassigns server to FullSyncer before upload (322) and download (337); FullSyncer overrides both (FullSyncer.java:77, 144)
sup(('Connection.doInBackgroundLogin', 'HttpSyncer.hostKey'))
sup(('Connection.doInBackgroundSync', 'HttpSyncer.upload'))
sup(('Connection.doInBackgroundSync', 'HttpSyncer.download'))
sup(('Syncer.sync(Connection)', 'HttpSyncer.meta'))
sup(('Syncer.sync(Connection)', 'HttpSyncer.start'))
sup(('Syncer.sync(Connection)', 'HttpSyncer.applyChanges'))
sup(('Syncer.sync(Connection)', 'HttpSyncer.chunk()'))
sup(('Syncer.sync(Connection)', 'HttpSyncer.applyChunk'))
sup(('Syncer.sync(Connection)', 'HttpSyncer.sanityCheck2'))
# TextImporter.<init> is UNREACHABLE (no_trigger_in_app): its only constructions are in the androidTest ImportTest
sup(('TextImporter.<init>', 'NoteImporter.<init>'))

# ---- part 107 (2026-10-28)
# AnkiDroid batch 107 (LABEL helper). MediaSyncer (3 methods), RemoteMediaServer (8) and RemoteServer (10): 21 methods, all REACHABLE.
# The full row list is in graphs/AnkiDroid/parts/label_107.md.
#
# No e() edges and no UNREACHABLE entries in this part. Every edge into or out of these 21 methods is an automatic
# CALL edge written by the builder (Connection.doInBackgroundSync and doInBackgroundLogin, Syncer.sync,
# HttpSyncer.req, and Syncer.throwExceptionIfCancelled), so none is repeated here.
# The AsyncTask launch edges that start the sync and login routes are owned by the Connection and DeckPicker batches.

# ---- part 108 (2026-10-28)
# AnkiDroid batch 108 (LABEL helper). Syncer part: 35 methods (34 Syncer methods and Template$1.compare).
# The full row list is in graphs/AnkiDroid/parts/label_108.md.
# 31 methods are REACHABLE (no entries here). 4 methods are UNREACHABLE (no_trigger_in_app, entries below).
# No e() edges are written. The render_unescaped -> Template$1.compare edge (non_standard, via Collections.sort)
# belongs to the Template batch.

UNREACHABLE['Syncer.applyChanges'] = ('no_trigger_in_app', "No caller. Syncer is referenced only in Connection.java (lines 281, 288 and 289) and in Syncer.java. The only call with this name in Syncer.java is line 170, mServer.applyChanges(sch). Its receiver is the HttpSyncer field, so it resolves to HttpSyncer.applyChanges (HttpSyncer.java:327) and not to this method. Connection.java does not call it.", 'SRC com/ichi2/libanki/sync/Syncer.java:170, 275-281; SRC com/ichi2/libanki/sync/HttpSyncer.java:327; SRC com/ichi2/async/Connection.java:281-289', 'SOURCE')

UNREACHABLE['Syncer.finish()'] = ('no_trigger_in_app', "No caller. Nothing in Connection.java or Syncer.java calls the no-argument finish() (418-420). The finish calls at Syncer.java:212 and 909 are mServer.finish() on the HttpSyncer field and resolve to HttpSyncer.finish() (HttpSyncer.java:347). Line 419 calls finish(long), not this method.", 'SRC com/ichi2/libanki/sync/Syncer.java:212, 418-420, 909; SRC com/ichi2/libanki/sync/HttpSyncer.java:347; SRC com/ichi2/async/Connection.java:281-289', 'SOURCE')

UNREACHABLE['Syncer.start'] = ('no_trigger_in_app', "No caller. The only call with this name in Syncer.java is mServer.start(o) at line 157. It passes one argument and resolves to HttpSyncer.start(JSONObject) (HttpSyncer.java:332). This method takes three arguments, so line 157 cannot call it. Connection.java does not call it.", 'SRC com/ichi2/libanki/sync/Syncer.java:157, 622-629; SRC com/ichi2/libanki/sync/HttpSyncer.java:332; SRC com/ichi2/async/Connection.java:281-289', 'SOURCE')

UNREACHABLE['Syncer.sync()'] = ('no_trigger_in_app', "No caller. Syncer.sync() (79-81) has no call site outside itself (line 80 is the self-call sync(null)). Connection.java:288 calls client.sync(this) with one argument, which is the other overload sync(Connection) (84). DeckPicker.sync() (DeckPicker.java:1266-1268) is a different method on a different class.", 'SRC com/ichi2/libanki/sync/Syncer.java:79-81, 84; SRC com/ichi2/async/Connection.java:288; SRC com/ichi2/anki/DeckPicker.java:1266-1268', 'SOURCE')

# ---- part 109 (2026-10-28)
UNREACHABLE['Atom.<init>'] = ('no_trigger_in_app',
    'The constructor runs only when Pow builds an Atom (new Atom at Pow.java:44, 60, 84). Pow is built only by Factor.java:77, inside the parser. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/Atom.java:27-53; com/wildplot/android/parsing/Pow.java:44, 60, 84; com/wildplot/android/parsing/Factor.java:77; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['Atom.getAtomType'] = ('no_trigger_in_app',
    'Getter. Callers are Pow.java:45, 61, 85 (atom.getAtomType()), inside the Pow chain. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/Atom.java:149-151; com/wildplot/android/parsing/Pow.java:45, 61, 85; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['Atom.getValue'] = ('no_trigger_in_app',
    'Callers are Pow.java:105, 107, 109 (atom.getValue()), inside the Pow chain. Its body dispatches to atomObject at Atom.java:162. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/Atom.java:153-167; com/wildplot/android/parsing/Pow.java:105, 107, 109; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['Atom.initAsExpInBrackets'] = ('no_trigger_in_app',
    'Private. The only caller is the constructor Atom.<init> (Atom.java:35), so it is unreachable with it. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/Atom.java:35, 56-69; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['Atom.initAsFunctionMath'] = ('no_trigger_in_app',
    'Private. The only caller is the constructor Atom.<init> (Atom.java:37), so it is unreachable with it. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/Atom.java:37, 71-81; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['Atom.initAsFunctionX'] = ('no_trigger_in_app',
    'Private. The only caller is the constructor Atom.<init> (Atom.java:39), so it is unreachable with it. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/Atom.java:39, 83-93; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['Atom.initAsFunctionXY'] = ('no_trigger_in_app',
    'Private. The only caller is the constructor Atom.<init> (Atom.java:41), so it is unreachable with it. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/Atom.java:41, 95-105; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['Atom.initAsNumber'] = ('no_trigger_in_app',
    'Private. The only caller is the constructor Atom.<init> (Atom.java:43), so it is unreachable with it. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/Atom.java:43, 107-116; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['Atom.initAsXVariable'] = ('no_trigger_in_app',
    'Private. The only caller is the constructor Atom.<init> (Atom.java:45), so it is unreachable with it. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/Atom.java:45, 118-126; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['Atom.initAsYVariable'] = ('no_trigger_in_app',
    'Private. The only caller is the constructor Atom.<init> (Atom.java:47), so it is unreachable with it. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/Atom.java:47, 128-136; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['Atom.initAsVariable'] = ('no_trigger_in_app',
    'Private. The only caller is the constructor Atom.<init> (Atom.java:49), so it is unreachable with it. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/Atom.java:49, 138-147; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['Atom.isVariable'] = ('no_trigger_in_app',
    'Callers are Pow.java:120, 123 (atom.isVariable()), inside the Pow chain. Its body dispatches to atomObject at Atom.java:179. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/Atom.java:169-184; com/wildplot/android/parsing/Pow.java:120, 123; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['Atom$AtomType.<clinit>'] = ('no_trigger_in_app',
    'The enum initializer runs on the first use of Atom.AtomType. Every use is inside com/wildplot/android/parsing (Atom.java:22-23, 31, 51, 63; NumberAtom.java:27; VariableAtom.java:28; FunctionXAtom.java:23; FunctionXYAtom.java:31), and none is outside the package. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/Atom.java:22-23, 31, 51, 63; com/wildplot/android/parsing/AtomTypes/NumberAtom.java:27; com/wildplot/android/parsing/AtomTypes/VariableAtom.java:28; com/wildplot/android/parsing/AtomTypes/FunctionXAtom.java:23; com/wildplot/android/parsing/AtomTypes/FunctionXYAtom.java:31; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['FunctionXAtom.<init>'] = ('no_trigger_in_app',
    'The only construction is new FunctionXAtom in Atom.java:84 (Atom.<init> chain). '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/FunctionXAtom.java:28-35; com/wildplot/android/parsing/Atom.java:84; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['FunctionXAtom.getAtomType'] = ('no_trigger_in_app',
    'Getter. The only caller is Atom.java:85 (functionXAtom.getAtomType()), inside the Atom.<init> chain. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/FunctionXAtom.java:85-87; com/wildplot/android/parsing/Atom.java:85; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['FunctionXAtom.getValue'] = ('no_trigger_in_app',
    'Reached only as atomObject.getValue() at Atom.java:162 (Atom.getValue, Pow chain). The method has no other caller. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/FunctionXAtom.java:64-72; com/wildplot/android/parsing/Atom.java:162; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['FunctionXAtom.init'] = ('no_trigger_in_app',
    'Private. The only caller is the constructor FunctionXAtom.<init> (FunctionXAtom.java:31). '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/FunctionXAtom.java:31, 37-62; com/wildplot/android/parsing/Atom.java:84; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['FunctionXAtom.isVariable'] = ('no_trigger_in_app',
    'Reached only as atomObject.isVariable() at Atom.java:179 (Atom.isVariable, Pow chain). '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/FunctionXAtom.java:74-83; com/wildplot/android/parsing/Atom.java:179; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['FunctionXYAtom.<init>'] = ('no_trigger_in_app',
    'The only construction is new FunctionXYAtom in Atom.java:96 (Atom.<init> chain). '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/FunctionXYAtom.java:37-44; com/wildplot/android/parsing/Atom.java:96; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['FunctionXYAtom.getAtomType'] = ('no_trigger_in_app',
    'Getter. The only caller is Atom.java:97 (functionXYAtom.getAtomType()), inside the Atom.<init> chain. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/FunctionXYAtom.java:27-29; com/wildplot/android/parsing/Atom.java:97; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['FunctionXYAtom.getValue'] = ('no_trigger_in_app',
    'Reached only as atomObject.getValue() at Atom.java:162 (Atom.getValue, Pow chain). '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/FunctionXYAtom.java:84-92; com/wildplot/android/parsing/Atom.java:162; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['FunctionXYAtom.init'] = ('no_trigger_in_app',
    'Private. The only caller is the constructor FunctionXYAtom.<init> (FunctionXYAtom.java:40). '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/FunctionXYAtom.java:40, 46-82; com/wildplot/android/parsing/Atom.java:96; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['FunctionXYAtom.isVariable'] = ('no_trigger_in_app',
    'Reached only as atomObject.isVariable() at Atom.java:179 (Atom.isVariable, Pow chain). '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/FunctionXYAtom.java:94-102; com/wildplot/android/parsing/Atom.java:179; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['MathFunctionAtom.<init>'] = ('no_trigger_in_app',
    'The only construction is new MathFunctionAtom in Atom.java:72 (Atom.<init> chain). '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/MathFunctionAtom.java:32-42; com/wildplot/android/parsing/Atom.java:72; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['MathFunctionAtom.getMathType'] = ('no_trigger_in_app',
    'Getter. The only caller is Atom.java:73 (mathFunctionAtom.getMathType()), inside the Atom.<init> chain. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/MathFunctionAtom.java:138-140; com/wildplot/android/parsing/Atom.java:73; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['MathFunctionAtom.getValue'] = ('no_trigger_in_app',
    'Reached only as atomObject.getValue() at Atom.java:162 (Atom.getValue, Pow chain). Its one other call is the constructor self-call at MathFunctionAtom.java:39. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/MathFunctionAtom.java:39, 95-126; com/wildplot/android/parsing/Atom.java:162; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['MathFunctionAtom.init'] = ('no_trigger_in_app',
    'Private. The only caller is the constructor MathFunctionAtom.<init> (MathFunctionAtom.java:34). '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/MathFunctionAtom.java:34, 46-92; com/wildplot/android/parsing/Atom.java:72; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['MathFunctionAtom.isVariable'] = ('no_trigger_in_app',
    'Reached only as atomObject.isVariable() at Atom.java:179 (Atom.isVariable, Pow chain), and the constructor self-call at MathFunctionAtom.java:38. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/MathFunctionAtom.java:38, 128-136; com/wildplot/android/parsing/Atom.java:179; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['MathFunctionAtom$MathType.<clinit>'] = ('no_trigger_in_app',
    'The enum initializer runs on the first use of MathFunctionAtom.MathType: the constructor init (MathFunctionAtom.java:56-76) and Atom.java:73. Every use is inside com/wildplot/android/parsing, and none is outside it. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/MathFunctionAtom.java:26-27, 56-76; com/wildplot/android/parsing/Atom.java:73; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['NumberAtom.<init>'] = ('no_trigger_in_app',
    'The only construction is new NumberAtom in Atom.java:108 (Atom.<init> chain). '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/NumberAtom.java:30-37; com/wildplot/android/parsing/Atom.java:108; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['NumberAtom.getAtomType'] = ('no_trigger_in_app',
    'Getter. Callers are Atom.java:109 and 111 (numberAtom.getAtomType()), inside the Atom.<init> chain. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/NumberAtom.java:23-25; com/wildplot/android/parsing/Atom.java:109, 111; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['NumberAtom.getValue'] = ('no_trigger_in_app',
    'Reached only as atomObject.getValue() at Atom.java:162 (Atom.getValue, Pow chain). '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/NumberAtom.java:39-45; com/wildplot/android/parsing/Atom.java:162; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['NumberAtom.isVariable'] = ('no_trigger_in_app',
    'Reached only as atomObject.isVariable() at Atom.java:179 (Atom.isVariable, Pow chain). '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/NumberAtom.java:47-53; com/wildplot/android/parsing/Atom.java:179; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['VariableAtom.<init>'] = ('no_trigger_in_app',
    'The only construction is new VariableAtom in Atom.java:139 (Atom.<init> chain). '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/VariableAtom.java:32-40; com/wildplot/android/parsing/Atom.java:139; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['VariableAtom.getAtomType'] = ('no_trigger_in_app',
    'Getter. Callers are Atom.java:140 and 142 (variableAtom.getAtomType()), inside the Atom.<init> chain. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/VariableAtom.java:42-44; com/wildplot/android/parsing/Atom.java:140, 142; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['VariableAtom.getValue'] = ('no_trigger_in_app',
    'Reached only as atomObject.getValue() at Atom.java:162 (Atom.getValue, Pow chain). '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/VariableAtom.java:46-55; com/wildplot/android/parsing/Atom.java:162; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['VariableAtom.isVariable'] = ('no_trigger_in_app',
    'Reached only as atomObject.isVariable() at Atom.java:179 (Atom.isVariable, Pow chain). '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/VariableAtom.java:57-60; com/wildplot/android/parsing/Atom.java:179; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

# ---- part 110 (2026-10-28)
# AnkiDroid batch 110 (LABEL helper). com.wildplot.android.parsing expression tree: 40 methods, all UNREACHABLE (no_trigger_in_app).
# The full row list is in graphs/AnkiDroid/parts/label_110.md. No e() edges: no batch method is the source of a non-CALL edge.
# Every reason states the closed chain inline: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165;
# its only caller path is createCopy() at TopLevelParser.java:158, called only from ReliefDrawer.java:632 and :693 under instanceof guards
# (:631, :692); ReliefDrawer is not referenced outside its own file.

UNREACHABLE['XVariableAtom.<init>'] = ('no_trigger_in_app', "Built only at Atom.java:121 (initAsXVariable, Atom.java:118-126), which runs only for atoms of the parser tree. Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/AtomTypes/XVariableAtom.java:27-29; com/wildplot/android/parsing/Atom.java:118-126; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['XVariableAtom.getAtomType'] = ('no_trigger_in_app', "No call site in src/main/java: getAtomType() is called only on Atom, FunctionXAtom, FunctionXYAtom, NumberAtom and VariableAtom receivers (Atom.java:85, 97, 109, 140, 142; Pow.java:45, 61, 85), never on an XVariableAtom, so no route reaches it.", 'SRC com/wildplot/android/parsing/AtomTypes/XVariableAtom.java:31-33; com/wildplot/android/parsing/Atom.java:85, 97, 109, 140, 142; com/wildplot/android/parsing/Pow.java:45, 61, 85', 'SOURCE')
UNREACHABLE['XVariableAtom.getValue'] = ('no_trigger_in_app', "Reached only through the TreeElement dispatch in Atom.getValue (Atom.java:162; atomObject is declared TreeElement at Atom.java:24), and Atom.getValue runs only inside the parser tree. Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/AtomTypes/XVariableAtom.java:36-44; com/wildplot/android/parsing/Atom.java:24, 153-167; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['XVariableAtom.isVariable'] = ('no_trigger_in_app', "Reached only through the TreeElement dispatch in Atom.isVariable (Atom.java:179; atomObject at Atom.java:24), and Atom.isVariable runs only inside the parser tree. Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/AtomTypes/XVariableAtom.java:47-49; com/wildplot/android/parsing/Atom.java:24, 179; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['YVariableAtom.<init>'] = ('no_trigger_in_app', "Built only at Atom.java:131 (initAsYVariable, Atom.java:128-136), which runs only for atoms of the parser tree. Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/AtomTypes/YVariableAtom.java:27-29; com/wildplot/android/parsing/Atom.java:128-136; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['YVariableAtom.getAtomType'] = ('no_trigger_in_app', "No call site in src/main/java: getAtomType() is called only on Atom, FunctionXAtom, FunctionXYAtom, NumberAtom and VariableAtom receivers (Atom.java:85, 97, 109, 140, 142; Pow.java:45, 61, 85), never on a YVariableAtom, so no route reaches it.", 'SRC com/wildplot/android/parsing/AtomTypes/YVariableAtom.java:31-33; com/wildplot/android/parsing/Atom.java:85, 97, 109, 140, 142; com/wildplot/android/parsing/Pow.java:45, 61, 85', 'SOURCE')
UNREACHABLE['YVariableAtom.getValue'] = ('no_trigger_in_app', "Reached only through the TreeElement dispatch in Atom.getValue (Atom.java:162; atomObject at Atom.java:24). Its body calls TopLevelParser.getY (TopLevelParser.java:123). Atom.getValue runs only inside the parser tree. Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/AtomTypes/YVariableAtom.java:36-44; com/wildplot/android/parsing/Atom.java:24, 153-167; com/wildplot/android/parsing/TopLevelParser.java:123, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['YVariableAtom.isVariable'] = ('no_trigger_in_app', "Reached only through the TreeElement dispatch in Atom.isVariable (Atom.java:179; atomObject at Atom.java:24), and Atom.isVariable runs only inside the parser tree. Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/AtomTypes/YVariableAtom.java:47-49; com/wildplot/android/parsing/Atom.java:24, 179; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['Expression.<init>'] = ('no_trigger_in_app', "Built only at TopLevelParser.java:43 (the chain root) and inside the parser tree at Expression.java:56, Atom.java:59, AtomTypes/MathFunctionAtom.java:52, AtomTypes/FunctionXAtom.java:50 and AtomTypes/FunctionXYAtom.java:67-68. Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/Expression.java:27-40, 56; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/parsing/Atom.java:59; com/wildplot/android/parsing/AtomTypes/MathFunctionAtom.java:52; com/wildplot/android/parsing/AtomTypes/FunctionXAtom.java:50; com/wildplot/android/parsing/AtomTypes/FunctionXYAtom.java:67-68; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['Expression.getExpressionType'] = ('no_trigger_in_app', "Callers: TopLevelParser.java:44 (ctor), Expression.java:57, Atom.java:60, AtomTypes/MathFunctionAtom.java:53, AtomTypes/FunctionXAtom.java:51, AtomTypes/FunctionXYAtom.java:69-70; all are in the parser tree. Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/Expression.java:100-102, 57; com/wildplot/android/parsing/TopLevelParser.java:44, 155-166; com/wildplot/android/parsing/Atom.java:60; com/wildplot/android/parsing/AtomTypes/MathFunctionAtom.java:53; com/wildplot/android/parsing/AtomTypes/FunctionXAtom.java:51; com/wildplot/android/parsing/AtomTypes/FunctionXYAtom.java:69-70; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['Expression.getValue'] = ('no_trigger_in_app', "Callers: TopLevelParser.java:135 and :149 (f(x) and f(x,y)), Atom.java:156 (EXP_IN_BRACKETS branch of Atom.getValue), and Expression.java:107, 109, 111 (self). The TopLevelParser callers need a TopLevelParser instance, which the chain rules out. Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/Expression.java:104-116, 107, 109, 111; com/wildplot/android/parsing/TopLevelParser.java:135, 149, 155-166; com/wildplot/android/parsing/Atom.java:156; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['Expression.initAsExpPlusOrMinusTerm'] = ('no_trigger_in_app', "Only caller: Expression.<init> at Expression.java:34, which runs only inside the parser tree. Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/Expression.java:34, 42-84; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['Expression.initAsTerm'] = ('no_trigger_in_app', "Only caller: Expression.<init> at Expression.java:36, which runs only inside the parser tree. Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/Expression.java:36, 86-97; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['Expression.isVariable'] = ('no_trigger_in_app', "Callers: Expression.java:123, 125 (self) and Atom.java:173 (EXP_IN_BRACKETS branch of Atom.isVariable). Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/Expression.java:118-130, 123, 125; com/wildplot/android/parsing/Atom.java:173; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['Expression$ExpressionType.<clinit>'] = ('no_trigger_in_app', "The enum initialiser runs on first use of ExpressionType, which happens only in Expression.<init> (Expression.java:30, 38) and TopLevelParser.<init> (TopLevelParser.java:44). Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/Expression.java:21, 27-40; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['ExpressionFormatException.<init>()'] = ('no_trigger_in_app', "No call site: every new ExpressionFormatException( in src/main/java passes a message string (for example TopLevelParser.java:137 and Expression.java:114), so the no-argument constructor is never called.", 'SRC com/wildplot/android/parsing/ExpressionFormatException.java:19-22; com/wildplot/android/parsing/TopLevelParser.java:137; com/wildplot/android/parsing/Expression.java:114', 'SOURCE')
UNREACHABLE['ExpressionFormatException.<init>(String)'] = ('no_trigger_in_app', "Thrown only from throw sites in the parser tree (TopLevelParser.java:137, 151; Expression.java:114, 128; Term.java:112, 126; Factor.java:101, 116; Pow.java:112, 126; Atom.java:165, 182). Those methods are reached only through the closed chain. Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/ExpressionFormatException.java:24-26; com/wildplot/android/parsing/TopLevelParser.java:137, 151, 155-166; com/wildplot/android/parsing/Expression.java:114, 128; com/wildplot/android/parsing/Term.java:112, 126; com/wildplot/android/parsing/Factor.java:101, 116; com/wildplot/android/parsing/Pow.java:112, 126; com/wildplot/android/parsing/Atom.java:165, 182; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['Factor.<init>'] = ('no_trigger_in_app', "Built at Factor.java:48 and :64 (initAsPlusFactor, initAsMinusFactor), Term.java:68 and :88, and Pow.java:63 and :87, all inside the parser tree. Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/Factor.java:27-42, 48, 64; com/wildplot/android/parsing/Term.java:68, 88; com/wildplot/android/parsing/Pow.java:63, 87; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['Factor.getFactorType'] = ('no_trigger_in_app', "Callers: Factor.java:49, 65; Term.java:69, 89; Pow.java:64, 88. Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/Factor.java:87-89, 49, 65; com/wildplot/android/parsing/Term.java:69, 89; com/wildplot/android/parsing/Pow.java:64, 88; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['Factor.getValue'] = ('no_trigger_in_app', "Callers: Factor.java:94, 96 (self), Term.java:105, 107, 109 and Pow.java:107, 109. Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/Factor.java:91-104, 94, 96; com/wildplot/android/parsing/Term.java:105, 107, 109; com/wildplot/android/parsing/Pow.java:107, 109; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['Factor.initAsMinusFactor'] = ('no_trigger_in_app', "Only caller: Factor.<init> at Factor.java:37, which runs only inside the parser tree. Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/Factor.java:37, 60-74; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['Factor.initAsPlusFactor'] = ('no_trigger_in_app', "Only caller: Factor.<init> at Factor.java:35, which runs only inside the parser tree. Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/Factor.java:35, 44-58; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['Factor.initAsPow'] = ('no_trigger_in_app', "Only caller: Factor.<init> at Factor.java:39, which runs only inside the parser tree. Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/Factor.java:39, 76-85; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['Factor.isVariable'] = ('no_trigger_in_app', "Callers: Factor.java:111, 113 (self), Term.java:121, 123 and Pow.java:123. Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/Factor.java:106-118, 111, 113; com/wildplot/android/parsing/Term.java:121, 123; com/wildplot/android/parsing/Pow.java:123; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['Factor$FactorType.<clinit>'] = ('no_trigger_in_app', "The enum initialiser runs on first use of FactorType, which happens only in Factor.<init> (Factor.java:30, 27-42). Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/Factor.java:22, 27-42; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['Pow.<init>'] = ('no_trigger_in_app', "Only caller: Factor.initAsPow at Factor.java:77, which runs only inside the parser tree. Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/Pow.java:26-41; com/wildplot/android/parsing/Factor.java:77; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['Pow.getPowType'] = ('no_trigger_in_app', "Only caller: Factor.initAsPow at Factor.java:78, which runs only inside the parser tree. Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/Pow.java:130-132; com/wildplot/android/parsing/Factor.java:78; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['Pow.getValue'] = ('no_trigger_in_app', "Only caller: Factor.getValue at Factor.java:98, which runs only inside the parser tree. Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/Pow.java:101-114; com/wildplot/android/parsing/Factor.java:98; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['Pow.initAsAtom'] = ('no_trigger_in_app', "Only caller: Pow.<init> at Pow.java:34, which runs only inside the parser tree. Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/Pow.java:34, 43-52; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['Pow.initAsAtomPowFactor'] = ('no_trigger_in_app', "Only caller: Pow.<init> at Pow.java:36, which runs only inside the parser tree. Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/Pow.java:36, 53-75; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['Pow.initAsAtomSqrtFactor'] = ('no_trigger_in_app', "Only caller: Pow.<init> at Pow.java:38, which runs only inside the parser tree. Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/Pow.java:38, 77-99; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['Pow.isVariable'] = ('no_trigger_in_app', "Only caller: Factor.isVariable at Factor.java:113, which runs only inside the parser tree. Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/Pow.java:116-128; com/wildplot/android/parsing/Factor.java:113; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['Pow$PowType.<clinit>'] = ('no_trigger_in_app', "The enum initialiser runs on first use of PowType, which happens only in Pow.<init> (Pow.java:29, 26-41). Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/Pow.java:21, 26-41; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['Term.<init>'] = ('no_trigger_in_app', "Built at Term.java:58, Expression.java:66 and Expression.java:89, all inside the parser tree. Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/Term.java:28-43, 58; com/wildplot/android/parsing/Expression.java:66, 89; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['Term.getTermType'] = ('no_trigger_in_app', "Callers: Term.java:59; Expression.java:67, 90. Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/Term.java:99-101, 59; com/wildplot/android/parsing/Expression.java:67, 90; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['Term.getValue'] = ('no_trigger_in_app', "Callers: Expression.java:107, 109, 111 and Term.java:105, 107 (self). Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/Term.java:102-114, 105, 107; com/wildplot/android/parsing/Expression.java:107, 109, 111; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['Term.initAsFactor'] = ('no_trigger_in_app', "Only caller: Term.<init> at Term.java:40, which runs only inside the parser tree. Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/Term.java:40, 87-96; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['Term.initAsTermMulOrDivFactor'] = ('no_trigger_in_app', "Only caller: Term.<init> at Term.java:38, which runs only inside the parser tree. Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/Term.java:38, 45-85; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['Term.isVariable'] = ('no_trigger_in_app', "Callers: Expression.java:123, 125; Term.java:121, 123 (self). Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/Term.java:116-128, 121, 123; com/wildplot/android/parsing/Expression.java:123, 125; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
UNREACHABLE['Term$TermType.<clinit>'] = ('no_trigger_in_app', "The enum initialiser runs on first use of TermType, which happens only in Term.<init> (Term.java:32, 28-43). Closed chain: TopLevelParser has no construction in src/main/java except TopLevelParser.java:165 (new TopLevelParser inside createCopy(HashMap)); createCopy(HashMap) is called only from createCopy() at TopLevelParser.java:158; createCopy() is called only from ReliefDrawer.java:632 and :693, inside the instanceof guards at :631 and :692; ReliefDrawer is not referenced outside its own file, so the chain never starts.", 'SRC com/wildplot/android/parsing/Term.java:22, 28-43; com/wildplot/android/parsing/TopLevelParser.java:37-46, 155-166; com/wildplot/android/rendering/ReliefDrawer.java:631-633, 692-694', 'SOURCE')
# ---- sup for parts 109 and 110 (2026-10-28, orchestrator, build 159): automatic CALL edges inside the wildplot parser tree
# every source is UNREACHABLE (batches 109 and 110). TopLevelParser has one construction (TopLevelParser.java:165, in createCopy);
# createCopy is called only from ReliefDrawer.java:632 and 693; ReliefDrawer is never constructed (no 'new ReliefDrawer(' in the source root).
sup(('Atom.<init>', 'Atom$AtomType.<clinit>'))
sup(('Atom.<init>', 'Atom.initAsExpInBrackets'))
sup(('Atom.<init>', 'Atom.initAsFunctionMath'))
sup(('Atom.<init>', 'Atom.initAsFunctionX'))
sup(('Atom.<init>', 'Atom.initAsFunctionXY'))
sup(('Atom.<init>', 'Atom.initAsNumber'))
sup(('Atom.<init>', 'Atom.initAsVariable'))
sup(('Atom.<init>', 'Atom.initAsXVariable'))
sup(('Atom.<init>', 'Atom.initAsYVariable'))
sup(('Atom.getValue', 'Atom$AtomType.<clinit>'))
sup(('Atom.getValue', 'Atom.getValue'))
sup(('Atom.getValue', 'Expression.getValue'))
sup(('Atom.getValue', 'ExpressionFormatException.<init>(String)'))
sup(('Atom.getValue', 'Factor.getValue'))
sup(('Atom.getValue', 'FunctionXAtom.getValue'))
sup(('Atom.getValue', 'FunctionXYAtom.getValue'))
sup(('Atom.getValue', 'MathFunctionAtom.getValue'))
sup(('Atom.getValue', 'NumberAtom.getValue'))
sup(('Atom.getValue', 'Pow.getValue'))
sup(('Atom.getValue', 'Term.getValue'))
sup(('Atom.getValue', 'VariableAtom.getValue'))
sup(('Atom.getValue', 'XVariableAtom.getValue'))
sup(('Atom.getValue', 'YVariableAtom.getValue'))
sup(('Atom.initAsExpInBrackets', 'Atom$AtomType.<clinit>'))
sup(('Atom.initAsExpInBrackets', 'Expression$ExpressionType.<clinit>'))
sup(('Atom.initAsExpInBrackets', 'Expression.<init>'))
sup(('Atom.initAsExpInBrackets', 'Expression.getExpressionType'))
sup(('Atom.initAsFunctionMath', 'Atom$AtomType.<clinit>'))
sup(('Atom.initAsFunctionMath', 'MathFunctionAtom$MathType.<clinit>'))
sup(('Atom.initAsFunctionMath', 'MathFunctionAtom.<init>'))
sup(('Atom.initAsFunctionMath', 'MathFunctionAtom.getMathType'))
sup(('Atom.initAsFunctionX', 'Atom$AtomType.<clinit>'))
sup(('Atom.initAsFunctionX', 'FunctionXAtom.<init>'))
sup(('Atom.initAsFunctionX', 'FunctionXAtom.getAtomType'))
sup(('Atom.initAsFunctionXY', 'Atom$AtomType.<clinit>'))
sup(('Atom.initAsFunctionXY', 'FunctionXYAtom.<init>'))
sup(('Atom.initAsFunctionXY', 'FunctionXYAtom.getAtomType'))
sup(('Atom.initAsNumber', 'Atom$AtomType.<clinit>'))
sup(('Atom.initAsNumber', 'NumberAtom.<init>'))
sup(('Atom.initAsNumber', 'NumberAtom.getAtomType'))
sup(('Atom.initAsVariable', 'Atom$AtomType.<clinit>'))
sup(('Atom.initAsVariable', 'VariableAtom.<init>'))
sup(('Atom.initAsVariable', 'VariableAtom.getAtomType'))
sup(('Atom.initAsXVariable', 'Atom$AtomType.<clinit>'))
sup(('Atom.initAsXVariable', 'XVariableAtom.<init>'))
sup(('Atom.initAsYVariable', 'Atom$AtomType.<clinit>'))
sup(('Atom.initAsYVariable', 'YVariableAtom.<init>'))
sup(('Atom.isVariable', 'Atom$AtomType.<clinit>'))
sup(('Atom.isVariable', 'Atom.isVariable'))
sup(('Atom.isVariable', 'Expression.isVariable'))
sup(('Atom.isVariable', 'ExpressionFormatException.<init>(String)'))
sup(('Atom.isVariable', 'Factor.isVariable'))
sup(('Atom.isVariable', 'FunctionXAtom.isVariable'))
sup(('Atom.isVariable', 'FunctionXYAtom.isVariable'))
sup(('Atom.isVariable', 'MathFunctionAtom.isVariable'))
sup(('Atom.isVariable', 'NumberAtom.isVariable'))
sup(('Atom.isVariable', 'Pow.isVariable'))
sup(('Atom.isVariable', 'Term.isVariable'))
sup(('Atom.isVariable', 'VariableAtom.isVariable'))
sup(('Atom.isVariable', 'XVariableAtom.isVariable'))
sup(('Atom.isVariable', 'YVariableAtom.isVariable'))
sup(('Expression.<init>', 'Expression$ExpressionType.<clinit>'))
sup(('Expression.<init>', 'Expression.initAsExpPlusOrMinusTerm'))
sup(('Expression.<init>', 'Expression.initAsTerm'))
sup(('Expression.getValue', 'Expression$ExpressionType.<clinit>'))
sup(('Expression.getValue', 'Expression.getValue'))
sup(('Expression.getValue', 'ExpressionFormatException.<init>(String)'))
sup(('Expression.getValue', 'Term.getValue'))
sup(('Expression.initAsExpPlusOrMinusTerm', 'Expression$ExpressionType.<clinit>'))
sup(('Expression.initAsExpPlusOrMinusTerm', 'Expression.<init>'))
sup(('Expression.initAsExpPlusOrMinusTerm', 'Expression.getExpressionType'))
sup(('Expression.initAsExpPlusOrMinusTerm', 'Term$TermType.<clinit>'))
sup(('Expression.initAsExpPlusOrMinusTerm', 'Term.<init>'))
sup(('Expression.initAsExpPlusOrMinusTerm', 'Term.getTermType'))
sup(('Expression.initAsTerm', 'Expression$ExpressionType.<clinit>'))
sup(('Expression.initAsTerm', 'Term$TermType.<clinit>'))
sup(('Expression.initAsTerm', 'Term.<init>'))
sup(('Expression.initAsTerm', 'Term.getTermType'))
sup(('Expression.isVariable', 'Expression$ExpressionType.<clinit>'))
sup(('Expression.isVariable', 'Expression.isVariable'))
sup(('Expression.isVariable', 'ExpressionFormatException.<init>(String)'))
sup(('Expression.isVariable', 'Term.isVariable'))
sup(('Factor.<init>', 'Factor$FactorType.<clinit>'))
sup(('Factor.<init>', 'Factor.initAsMinusFactor'))
sup(('Factor.<init>', 'Factor.initAsPlusFactor'))
sup(('Factor.<init>', 'Factor.initAsPow'))
sup(('Factor.getValue', 'ExpressionFormatException.<init>(String)'))
sup(('Factor.getValue', 'Factor$FactorType.<clinit>'))
sup(('Factor.getValue', 'Factor.getValue'))
sup(('Factor.getValue', 'Pow.getValue'))
sup(('Factor.initAsMinusFactor', 'Factor$FactorType.<clinit>'))
sup(('Factor.initAsMinusFactor', 'Factor.<init>'))
sup(('Factor.initAsMinusFactor', 'Factor.getFactorType'))
sup(('Factor.initAsPlusFactor', 'Factor$FactorType.<clinit>'))
sup(('Factor.initAsPlusFactor', 'Factor.<init>'))
sup(('Factor.initAsPlusFactor', 'Factor.getFactorType'))
sup(('Factor.initAsPow', 'Factor$FactorType.<clinit>'))
sup(('Factor.initAsPow', 'Pow$PowType.<clinit>'))
sup(('Factor.initAsPow', 'Pow.<init>'))
sup(('Factor.initAsPow', 'Pow.getPowType'))
sup(('Factor.isVariable', 'ExpressionFormatException.<init>(String)'))
sup(('Factor.isVariable', 'Factor$FactorType.<clinit>'))
sup(('Factor.isVariable', 'Factor.isVariable'))
sup(('Factor.isVariable', 'Pow.isVariable'))
sup(('FunctionXAtom.<init>', 'Atom$AtomType.<clinit>'))
sup(('FunctionXAtom.<init>', 'FunctionXAtom.init'))
sup(('FunctionXAtom.getValue', 'Atom$AtomType.<clinit>'))
sup(('FunctionXAtom.getValue', 'Expression.getValue'))
sup(('FunctionXAtom.getValue', 'ExpressionFormatException.<init>(String)'))
sup(('FunctionXAtom.init', 'Atom$AtomType.<clinit>'))
sup(('FunctionXAtom.init', 'Expression$ExpressionType.<clinit>'))
sup(('FunctionXAtom.init', 'Expression.<init>'))
sup(('FunctionXAtom.init', 'Expression.getExpressionType'))
sup(('FunctionXAtom.isVariable', 'Atom$AtomType.<clinit>'))
sup(('FunctionXAtom.isVariable', 'Expression.isVariable'))
sup(('FunctionXAtom.isVariable', 'ExpressionFormatException.<init>(String)'))
sup(('FunctionXYAtom.<init>', 'Atom$AtomType.<clinit>'))
sup(('FunctionXYAtom.<init>', 'FunctionXYAtom.init'))
sup(('FunctionXYAtom.getValue', 'Atom$AtomType.<clinit>'))
sup(('FunctionXYAtom.getValue', 'Expression.getValue'))
sup(('FunctionXYAtom.getValue', 'ExpressionFormatException.<init>(String)'))
sup(('FunctionXYAtom.init', 'Atom$AtomType.<clinit>'))
sup(('FunctionXYAtom.init', 'Expression$ExpressionType.<clinit>'))
sup(('FunctionXYAtom.init', 'Expression.<init>'))
sup(('FunctionXYAtom.init', 'Expression.getExpressionType'))
sup(('FunctionXYAtom.isVariable', 'Atom$AtomType.<clinit>'))
sup(('FunctionXYAtom.isVariable', 'Expression.isVariable'))
sup(('FunctionXYAtom.isVariable', 'ExpressionFormatException.<init>(String)'))
sup(('MathFunctionAtom.<init>', 'MathFunctionAtom$MathType.<clinit>'))
sup(('MathFunctionAtom.<init>', 'MathFunctionAtom.getValue'))
sup(('MathFunctionAtom.<init>', 'MathFunctionAtom.init'))
sup(('MathFunctionAtom.<init>', 'MathFunctionAtom.isVariable'))
sup(('MathFunctionAtom.getValue', 'Expression.getValue'))
sup(('MathFunctionAtom.getValue', 'ExpressionFormatException.<init>(String)'))
sup(('MathFunctionAtom.getValue', 'MathFunctionAtom$MathType.<clinit>'))
sup(('MathFunctionAtom.init', 'Expression$ExpressionType.<clinit>'))
sup(('MathFunctionAtom.init', 'Expression.<init>'))
sup(('MathFunctionAtom.init', 'Expression.getExpressionType'))
sup(('MathFunctionAtom.init', 'MathFunctionAtom$MathType.<clinit>'))
sup(('MathFunctionAtom.isVariable', 'Expression.isVariable'))
sup(('MathFunctionAtom.isVariable', 'ExpressionFormatException.<init>(String)'))
sup(('MathFunctionAtom.isVariable', 'MathFunctionAtom$MathType.<clinit>'))
sup(('NumberAtom.<init>', 'Atom$AtomType.<clinit>'))
sup(('NumberAtom.getValue', 'Atom$AtomType.<clinit>'))
sup(('NumberAtom.getValue', 'ExpressionFormatException.<init>(String)'))
sup(('NumberAtom.isVariable', 'Atom$AtomType.<clinit>'))
sup(('NumberAtom.isVariable', 'ExpressionFormatException.<init>(String)'))
sup(('Pow.<init>', 'Pow$PowType.<clinit>'))
sup(('Pow.<init>', 'Pow.initAsAtom'))
sup(('Pow.<init>', 'Pow.initAsAtomPowFactor'))
sup(('Pow.<init>', 'Pow.initAsAtomSqrtFactor'))
sup(('Pow.getValue', 'Atom.getValue'))
sup(('Pow.getValue', 'ExpressionFormatException.<init>(String)'))
sup(('Pow.getValue', 'Factor.getValue'))
sup(('Pow.getValue', 'Pow$PowType.<clinit>'))
sup(('Pow.initAsAtom', 'Atom$AtomType.<clinit>'))
sup(('Pow.initAsAtom', 'Atom.<init>'))
sup(('Pow.initAsAtom', 'Atom.getAtomType'))
sup(('Pow.initAsAtom', 'Pow$PowType.<clinit>'))
sup(('Pow.initAsAtomPowFactor', 'Atom$AtomType.<clinit>'))
sup(('Pow.initAsAtomPowFactor', 'Atom.<init>'))
sup(('Pow.initAsAtomPowFactor', 'Atom.getAtomType'))
sup(('Pow.initAsAtomPowFactor', 'Factor$FactorType.<clinit>'))
sup(('Pow.initAsAtomPowFactor', 'Factor.<init>'))
sup(('Pow.initAsAtomPowFactor', 'Factor.getFactorType'))
sup(('Pow.initAsAtomPowFactor', 'Pow$PowType.<clinit>'))
sup(('Pow.initAsAtomSqrtFactor', 'Atom$AtomType.<clinit>'))
sup(('Pow.initAsAtomSqrtFactor', 'Atom.<init>'))
sup(('Pow.initAsAtomSqrtFactor', 'Atom.getAtomType'))
sup(('Pow.initAsAtomSqrtFactor', 'Factor$FactorType.<clinit>'))
sup(('Pow.initAsAtomSqrtFactor', 'Factor.<init>'))
sup(('Pow.initAsAtomSqrtFactor', 'Factor.getFactorType'))
sup(('Pow.initAsAtomSqrtFactor', 'Pow$PowType.<clinit>'))
sup(('Pow.isVariable', 'Atom.isVariable'))
sup(('Pow.isVariable', 'ExpressionFormatException.<init>(String)'))
sup(('Pow.isVariable', 'Factor.isVariable'))
sup(('Pow.isVariable', 'Pow$PowType.<clinit>'))
sup(('Term.<init>', 'Term$TermType.<clinit>'))
sup(('Term.<init>', 'Term.initAsFactor'))
sup(('Term.<init>', 'Term.initAsTermMulOrDivFactor'))
sup(('Term.getValue', 'ExpressionFormatException.<init>(String)'))
sup(('Term.getValue', 'Factor.getValue'))
sup(('Term.getValue', 'Term$TermType.<clinit>'))
sup(('Term.getValue', 'Term.getValue'))
sup(('Term.initAsFactor', 'Factor$FactorType.<clinit>'))
sup(('Term.initAsFactor', 'Factor.<init>'))
sup(('Term.initAsFactor', 'Factor.getFactorType'))
sup(('Term.initAsFactor', 'Term$TermType.<clinit>'))
sup(('Term.initAsTermMulOrDivFactor', 'Factor$FactorType.<clinit>'))
sup(('Term.initAsTermMulOrDivFactor', 'Factor.<init>'))
sup(('Term.initAsTermMulOrDivFactor', 'Factor.getFactorType'))
sup(('Term.initAsTermMulOrDivFactor', 'Term$TermType.<clinit>'))
sup(('Term.initAsTermMulOrDivFactor', 'Term.<init>'))
sup(('Term.initAsTermMulOrDivFactor', 'Term.getTermType'))
sup(('Term.isVariable', 'ExpressionFormatException.<init>(String)'))
sup(('Term.isVariable', 'Factor.isVariable'))
sup(('Term.isVariable', 'Term$TermType.<clinit>'))
sup(('Term.isVariable', 'Term.isVariable'))
sup(('TopLevelParser.<init>', 'Expression$ExpressionType.<clinit>'))
sup(('TopLevelParser.<init>', 'Expression.<init>'))
sup(('TopLevelParser.<init>', 'Expression.getExpressionType'))
sup(('TopLevelParser.f(double)', 'Expression.getValue'))
sup(('TopLevelParser.f(double)', 'ExpressionFormatException.<init>(String)'))
sup(('TopLevelParser.f(double,double)', 'Expression.getValue'))
sup(('TopLevelParser.f(double,double)', 'ExpressionFormatException.<init>(String)'))
sup(('VariableAtom.<init>', 'Atom$AtomType.<clinit>'))
sup(('VariableAtom.getValue', 'Atom$AtomType.<clinit>'))
sup(('VariableAtom.getValue', 'ExpressionFormatException.<init>(String)'))
sup(('XVariableAtom.<init>', 'Atom$AtomType.<clinit>'))
sup(('XVariableAtom.getValue', 'Atom$AtomType.<clinit>'))
sup(('XVariableAtom.getValue', 'ExpressionFormatException.<init>(String)'))
sup(('YVariableAtom.<init>', 'Atom$AtomType.<clinit>'))
sup(('YVariableAtom.getValue', 'Atom$AtomType.<clinit>'))
sup(('YVariableAtom.getValue', 'ExpressionFormatException.<init>(String)'))

# ---- part 114 (2026-10-28)
# AnkiDroid batch 114 (LABEL helper). wildplot rendering: MultiScreenPart (8 methods) and PieChart (11 methods).
# Four UNREACHABLE entries. No e() calls: this batch owns no edges. The full row list is in graphs/AnkiDroid/parts/label_114.md.
UNREACHABLE['MultiScreenPart.<init>(double[],double[],Vector)'] = ('no_trigger_in_app', "Only the 5-argument PlotSheet constructor calls this constructor. Nothing calls that PlotSheet constructor: a whole-root grep for new PlotSheet( finds only the 4-argument calls at ChartBuilder.java:134 and 147. Drawable is an app interface, so no framework path exists.", "com/wildplot/android/rendering/MultiScreenPart.java:57-62; com/wildplot/android/rendering/PlotSheet.java:112-116; com/ichi2/anki/stats/ChartBuilder.java:134; com/ichi2/anki/stats/ChartBuilder.java:147", 'SOURCE')
UNREACHABLE['MultiScreenPart.setxRange'] = ('no_trigger_in_app', "The only callers are PlotSheet.updateX (PlotSheet.java:138-141) and the PlotSheet.setxRange wrapper (PlotSheet.java:565-567). Neither has a caller: a whole-root grep for updateX and setxRange finds no call outside those bodies, with or without a space before the parenthesis.", "com/wildplot/android/rendering/MultiScreenPart.java:76-78; com/wildplot/android/rendering/PlotSheet.java:138-141; com/wildplot/android/rendering/PlotSheet.java:565-567", 'SOURCE')
UNREACHABLE['MultiScreenPart.setyRange'] = ('no_trigger_in_app', "The only callers are PlotSheet.updateY (PlotSheet.java:148-151) and the PlotSheet.setyRange wrapper (PlotSheet.java:581-583). Neither has a caller: a whole-root grep for updateY and setyRange finds no call outside those bodies, with or without a space before the parenthesis.", "com/wildplot/android/rendering/MultiScreenPart.java:92-94; com/wildplot/android/rendering/PlotSheet.java:148-151; com/wildplot/android/rendering/PlotSheet.java:581-583", 'SOURCE')
UNREACHABLE['PieChart.abortAndReset'] = ('no_trigger_in_app', "The only call to abortAndReset in the source root is DrawableContainer.java:62, inside DrawableContainer.abortAndReset (lines 59-63). Nothing calls DrawableContainer.abortAndReset or PlotSheet.abortAndReset (PlotSheet.java:711-714): a whole-root grep for abortAndReset finds only definitions and that one call. Drawable is an app interface, so no framework path exists.", "com/wildplot/android/rendering/PieChart.java:141-144; com/wildplot/android/rendering/DrawableContainer.java:59-63; com/wildplot/android/rendering/PlotSheet.java:711-714", 'SOURCE')

# ---- part 111 (2026-10-28)
UNREACHABLE['TopLevelParser.<init>'] = ('no_trigger_in_app', "No instance of TopLevelParser is created in the app. Its only constructor call is inside createCopy(HashMap) (TopLevelParser.java:165), which needs an existing TopLevelParser as its receiver. createCopy() (TopLevelParser.java:158) and the ReliefDrawer calls (ReliefDrawer.java:632, 693) sit behind instanceof TopLevelParser checks (ReliefDrawer.java:631, 692) that are never true. No route from an entry point.", 'SRC com/wildplot/android/parsing/TopLevelParser.java:37-46, 158, 164-166; SRC com/wildplot/android/rendering/ReliefDrawer.java:631-632, 692-693', 'SOURCE')
UNREACHABLE['TopLevelParser.createCopy()'] = ('no_trigger_in_app', "Instance method. Its receiver must be an existing TopLevelParser, and none is ever created (see TopLevelParser.<init>). Its callers are the ReliefDrawer calls at lines 632 and 693, both behind an instanceof TopLevelParser check (lines 631 and 692) that is never true. No route from an entry point.", 'SRC com/wildplot/android/parsing/TopLevelParser.java:155-162; SRC com/wildplot/android/rendering/ReliefDrawer.java:631-632, 692-693', 'SOURCE')
UNREACHABLE['TopLevelParser.createCopy(HashMap)'] = ('no_trigger_in_app', "Its only in-app caller is createCopy() (TopLevelParser.java:158), which needs an existing TopLevelParser instance. The only new TopLevelParser is in this method (line 165). No route from an entry point.", 'SRC com/wildplot/android/parsing/TopLevelParser.java:158, 164-166', 'SOURCE')
UNREACHABLE['TopLevelParser.f(double)'] = ('no_trigger_in_app', "Instance method (Function2D.f). A call through the Function2D interface reaches it only when the receiver is a TopLevelParser, and none is created. Its in-class caller getFuncVal (line 170) needs an instance. The automatic cha edge BarGraph.paint -> TopLevelParser.f(double) (BarGraph.java:133) sits in the hasFunction branch that is never entered on this route; it is the suppression candidate.", 'SRC com/wildplot/android/parsing/TopLevelParser.java:131-138, 168-171; SRC com/wildplot/android/rendering/BarGraph.java:127-135', 'SOURCE')
UNREACHABLE['TopLevelParser.f(double,double)'] = ('no_trigger_in_app', "Instance method (Function3D or Function2D f). Its in-class caller getFuncVal (line 175) needs an instance. Interface callers in the rendering package reach it only for a TopLevelParser receiver, which is never created. No route from an entry point.", 'SRC com/wildplot/android/parsing/TopLevelParser.java:144-152, 173-176', 'SOURCE')
UNREACHABLE['TopLevelParser.getFuncName'] = ('no_trigger_in_app', "No call site in the source root (grep finds only the definition). Instance method; no instance is ever created.", 'SRC com/wildplot/android/parsing/TopLevelParser.java:186-188', 'SOURCE')
UNREACHABLE['TopLevelParser.getFuncVal(String,double)'] = ('no_trigger_in_app', "Its only in-app caller is FunctionXAtom.getValue (FunctionXAtom.java:68) through parser.getFuncVal. That parser is a TopLevelParser, which is never created; the atom classes are built only inside the parser tree rooted at the TopLevelParser constructor.", 'SRC com/wildplot/android/parsing/TopLevelParser.java:168-171; SRC com/wildplot/android/parsing/AtomTypes/FunctionXAtom.java:68', 'SOURCE')
UNREACHABLE['TopLevelParser.getFuncVal(String,double,double)'] = ('no_trigger_in_app', "Its only in-app caller is FunctionXYAtom.getValue (FunctionXYAtom.java:88) through parser.getFuncVal. Same reason as getFuncVal(String,double): the parser is never created.", 'SRC com/wildplot/android/parsing/TopLevelParser.java:173-176; SRC com/wildplot/android/parsing/AtomTypes/FunctionXYAtom.java:88', 'SOURCE')
UNREACHABLE['TopLevelParser.getVarVal'] = ('no_trigger_in_app', "Its only in-app caller is VariableAtom.getValue (VariableAtom.java:51) through parser.getVarVal. The parser is never created, so this call never runs.", 'SRC com/wildplot/android/parsing/TopLevelParser.java:105-107; SRC com/wildplot/android/parsing/AtomTypes/VariableAtom.java:51', 'SOURCE')
UNREACHABLE['TopLevelParser.getX'] = ('no_trigger_in_app', "Its only in-app caller is XVariableAtom.getValue (XVariableAtom.java:40) through parser.getX. The parser is never created, so this call never runs.", 'SRC com/wildplot/android/parsing/TopLevelParser.java:115-117; SRC com/wildplot/android/parsing/AtomTypes/XVariableAtom.java:40', 'SOURCE')
UNREACHABLE['TopLevelParser.getY'] = ('no_trigger_in_app', "Its only in-app caller is YVariableAtom.getValue (YVariableAtom.java:40) through parser.getY. The parser is never created, so this call never runs.", 'SRC com/wildplot/android/parsing/TopLevelParser.java:123-125; SRC com/wildplot/android/parsing/AtomTypes/YVariableAtom.java:40', 'SOURCE')
UNREACHABLE['TopLevelParser.getxName'] = ('no_trigger_in_app', "Its only in-app caller is Atom.initAsXVariable (Atom.java:119) through parser.getxName. The parser is never created, so this call never runs.", 'SRC com/wildplot/android/parsing/TopLevelParser.java:178-180; SRC com/wildplot/android/parsing/Atom.java:119', 'SOURCE')
UNREACHABLE['TopLevelParser.getyName'] = ('no_trigger_in_app', "Its only in-app caller is Atom.initAsYVariable (Atom.java:129) through parser.getyName. The parser is never created, so this call never runs.", 'SRC com/wildplot/android/parsing/TopLevelParser.java:182-184; SRC com/wildplot/android/parsing/Atom.java:129', 'SOURCE')
UNREACHABLE['TopLevelParser.initExpressionString'] = ('no_trigger_in_app', "Private. Its only caller is the constructor (line 41), which is never run.", 'SRC com/wildplot/android/parsing/TopLevelParser.java:41, 53-103', 'SOURCE')
UNREACHABLE['TopLevelParser.initVarMap'] = ('no_trigger_in_app', "Private. Its only caller is the constructor (line 38), which is never run.", 'SRC com/wildplot/android/parsing/TopLevelParser.java:38, 48-51', 'SOURCE')
UNREACHABLE['TopLevelParser.isValid'] = ('no_trigger_in_app', "No call of TopLevelParser.isValid() in the source root; the grep matches are local variables named isValid. Instance method; no instance is ever created.", 'SRC com/wildplot/android/parsing/TopLevelParser.java:140-142', 'SOURCE')
UNREACHABLE['TopLevelParser.setVarVal(String,String)'] = ('no_trigger_in_app', "No call site in the source root (grep finds only the two definitions). Instance method; no instance is ever created.", 'SRC com/wildplot/android/parsing/TopLevelParser.java:108-110', 'SOURCE')
UNREACHABLE['TopLevelParser.setVarVal(String,double)'] = ('no_trigger_in_app', "No call site in the source root (grep finds only the two definitions). Instance method; no instance is ever created.", 'SRC com/wildplot/android/parsing/TopLevelParser.java:111-113', 'SOURCE')
UNREACHABLE['TopLevelParser.setX'] = ('no_trigger_in_app', "No call site in the source root (the grep matches for setX are setXfermode calls in GraphicsWrap, which are unrelated). Instance method; no instance is ever created.", 'SRC com/wildplot/android/parsing/TopLevelParser.java:119-121', 'SOURCE')
UNREACHABLE['TopLevelParser.setY'] = ('no_trigger_in_app', "No call site in the source root (grep finds only the definition). Instance method; no instance is ever created.", 'SRC com/wildplot/android/parsing/TopLevelParser.java:127-129', 'SOURCE')
UNREACHABLE['TopLevelParser.stringHasValidBrackets'] = ('no_trigger_in_app', "Static method, so no instance is needed. Its callers are the parser classes Expression, Atom, Term, Factor and Pow (Expression.java:29, 54, 63, 87; Atom.java:30; Term.java:31, 56, 66; Factor.java:29; Pow.java:28, 58, 82). Each of those classes is created only inside the parser tree rooted at the TopLevelParser constructor (TopLevelParser.java:43 and the new sites in Expression.java:56, 89 and the AtomTypes files), so no entry point reaches the callers.", 'SRC com/wildplot/android/parsing/TopLevelParser.java:190-208; SRC com/wildplot/android/parsing/Expression.java:29, 54, 63, 87; SRC com/wildplot/android/parsing/Atom.java:30; SRC com/wildplot/android/parsing/Term.java:31, 56, 66; SRC com/wildplot/android/parsing/Factor.java:29; SRC com/wildplot/android/parsing/Pow.java:28, 58, 82', 'SOURCE')
UNREACHABLE['BarGraph.<init>(PlotSheet,double,Function2D,double,ColorWrap)'] = ('no_trigger_in_app', "No caller in the app. The only BarGraph creation is ChartBuilder.java:240, which uses the double[][] constructor. XAxisBarGraph and YAxisBarGraph do not extend BarGraph and never call it, so no other route exists.", 'SRC com/wildplot/android/rendering/BarGraph.java:91-98; SRC com/ichi2/anki/stats/ChartBuilder.java:240', 'SOURCE')
UNREACHABLE['BarGraph.<init>(PlotSheet,double,Function2D,ColorWrap)'] = ('no_trigger_in_app', "No caller in the app, for the same reason as the other Function2D constructor: the only creation site is ChartBuilder.java:240 with a double[][].", 'SRC com/wildplot/android/rendering/BarGraph.java:75-81; SRC com/ichi2/anki/stats/ChartBuilder.java:240', 'SOURCE')
UNREACHABLE['BarGraph.abortAndReset'] = ('no_trigger_in_app', "The only call in the source root is DrawableContainer.abortAndReset (DrawableContainer.java:62, through a Drawable reference). Nothing calls DrawableContainer.abortAndReset (its definition at line 59 is the only match), and PlotSheet.abortAndReset (PlotSheet.java:711) has no caller either. No route from an entry point reaches this method.", 'SRC com/wildplot/android/rendering/BarGraph.java:216-220; SRC com/wildplot/android/rendering/DrawableContainer.java:59-63; SRC com/wildplot/android/rendering/PlotSheet.java:708-713', 'SOURCE')
# ---- sup for part 111 (2026-10-28, orchestrator, build 161): automatic CALL edges inside the parser tree from UNREACHABLE parser methods
# BarGraph.paint -> TopLevelParser.f(double) (BarGraph.java:133) sits in the hasFunction branch; hasFunction is set only by the Function2D constructors (BarGraph.java:79, 96), both UNREACHABLE, and the only new BarGraph is the double[][] constructor at ChartBuilder.java:240
sup(('Atom.<init>', 'TopLevelParser.stringHasValidBrackets'))
sup(('Atom.initAsXVariable', 'TopLevelParser.getxName'))
sup(('Atom.initAsYVariable', 'TopLevelParser.getyName'))
sup(('BarGraph.paint', 'TopLevelParser.f(double)'))
sup(('Expression.<init>', 'TopLevelParser.stringHasValidBrackets'))
sup(('Expression.initAsExpPlusOrMinusTerm', 'TopLevelParser.stringHasValidBrackets'))
sup(('Expression.initAsTerm', 'TopLevelParser.stringHasValidBrackets'))
sup(('Factor.<init>', 'TopLevelParser.stringHasValidBrackets'))
sup(('FunctionXAtom.getValue', 'TopLevelParser.getFuncVal(String,double)'))
sup(('FunctionXYAtom.getValue', 'TopLevelParser.getFuncVal(String,double,double)'))
sup(('Pow.<init>', 'TopLevelParser.stringHasValidBrackets'))
sup(('Pow.initAsAtomPowFactor', 'TopLevelParser.stringHasValidBrackets'))
sup(('Pow.initAsAtomSqrtFactor', 'TopLevelParser.stringHasValidBrackets'))
sup(('Term.<init>', 'TopLevelParser.stringHasValidBrackets'))
sup(('Term.initAsTermMulOrDivFactor', 'TopLevelParser.stringHasValidBrackets'))
sup(('TopLevelParser.<init>', 'TopLevelParser.initExpressionString'))
sup(('TopLevelParser.<init>', 'TopLevelParser.initVarMap'))
sup(('TopLevelParser.createCopy()', 'TopLevelParser.createCopy(HashMap)'))
sup(('TopLevelParser.createCopy(HashMap)', 'TopLevelParser.<init>'))
sup(('TopLevelParser.getFuncVal(String,double)', 'TopLevelParser.f(double)'))
sup(('TopLevelParser.getFuncVal(String,double,double)', 'TopLevelParser.f(double,double)'))
sup(('VariableAtom.getValue', 'TopLevelParser.getVarVal'))
sup(('XVariableAtom.getValue', 'TopLevelParser.getX'))
sup(('YVariableAtom.getValue', 'TopLevelParser.getY'))

# ---- part 113 (2026-10-28)
# AnkiDroid batch 113 (LABEL helper). wildplot rendering: Integral, LegendDrawable, Lines, LinesPoints (40 methods).
# The full row list is in graphs/AnkiDroid/parts/label_113.md. This batch has no e() edges.
# Each UNREACHABLE entry repeats its text inline (no module-level names, no imports).

UNREACHABLE['Integral.<init>(Function2D,PlotSheet,double,double)'] = ('no_trigger_in_app', "Class Integral is never instantiated in the app. grep -rn -w Integral over src/main/java finds only Integral.java (class at line 29, constructors at lines 59 and 75). No new Integral(...) exists, so this constructor has no caller.", 'SRC com/wildplot/android/rendering/Integral.java:59-65; com/wildplot/android/rendering/Integral.java:29', 'SOURCE')

UNREACHABLE['Integral.<init>(Function2D,Function2D,PlotSheet,double,double)'] = ('no_trigger_in_app', "Same grep result as the first Integral constructor: the class is never instantiated, so this constructor has no caller.", 'SRC com/wildplot/android/rendering/Integral.java:75-82', 'SOURCE')

UNREACHABLE['Integral.abortAndReset'] = ('no_trigger_in_app', "Empty body. No Integral object exists to receive the call. The only abortAndReset call in src/main/java is DrawableContainer.java:62, inside DrawableContainer.abortAndReset, which has no caller. PlotSheet.abortAndReset has no caller either.", 'SRC com/wildplot/android/rendering/Integral.java:127-130; com/wildplot/android/rendering/DrawableContainer.java:59-63; com/wildplot/android/rendering/PlotSheet.java:711-714', 'SOURCE')

UNREACHABLE['Integral.isClusterable'] = ('no_trigger_in_app', "Class never instantiated. The dispatch sites PlotSheet.java:500 and :519 only receive drawables that were added to a sheet, and no Integral is ever added.", 'SRC com/wildplot/android/rendering/Integral.java:132-135; com/wildplot/android/rendering/PlotSheet.java:500, 519', 'SOURCE')

UNREACHABLE['Integral.isCritical'] = ('no_trigger_in_app', "Class never instantiated. The call sites are PlotSheet.java:501, 507, 520 and 526, on drawables from a sheet; no Integral is ever added to a sheet.", 'SRC com/wildplot/android/rendering/Integral.java:137-140; com/wildplot/android/rendering/PlotSheet.java:501, 520', 'SOURCE')

UNREACHABLE['Integral.isOnFrame'] = ('no_trigger_in_app', "Class never instantiated. The call sites PlotSheet.java:357 and :499 only see drawables already in a sheet.", 'SRC com/wildplot/android/rendering/Integral.java:122-124; com/wildplot/android/rendering/PlotSheet.java:357, 499', 'SOURCE')

UNREACHABLE['Integral.paint'] = ('no_trigger_in_app', "Class never instantiated. The paint call sites PlotSheet.java:366 and :473 paint only drawables already in a sheet.", 'SRC com/wildplot/android/rendering/Integral.java:88-116; com/wildplot/android/rendering/PlotSheet.java:366, 473', 'SOURCE')

UNREACHABLE['Integral.setColor'] = ('no_trigger_in_app', "Class never instantiated, so no receiver can have type Integral. The 79 setColor( lines in src/main/java were grepped; the legend calls are ChartBuilder.java:184-186 on LegendDrawable receivers, and none is on an Integral.", 'SRC com/wildplot/android/rendering/Integral.java:48-50; com/ichi2/anki/stats/ChartBuilder.java:184-186', 'SOURCE')

UNREACHABLE['LegendDrawable.abortAndReset'] = ('no_trigger_in_app', "Empty body. The only abortAndReset call in src/main/java is DrawableContainer.java:62, inside DrawableContainer.abortAndReset, which has no caller. PlotSheet.abortAndReset has no caller. No path reaches LegendDrawable.abortAndReset.", 'SRC com/wildplot/android/rendering/LegendDrawable.java:43-46; com/wildplot/android/rendering/DrawableContainer.java:59-63; com/wildplot/android/rendering/PlotSheet.java:711-714', 'SOURCE')

UNREACHABLE['LegendDrawable.isCritical'] = ('branch_never_taken', "isCritical is called only inside clusterable branches: PlotSheet.java:501 and :507 (on-frame, guarded by isClusterable at :500), and PlotSheet.java:520 and :526 (off-frame, guarded by isClusterable at :519). LegendDrawable.isOnFrame is false (LegendDrawable.java:38-41) and LegendDrawable.isClusterable is false (LegendDrawable.java:48-51). The guard at PlotSheet.java:519 is therefore never true for a LegendDrawable, so isCritical is never called on one.", 'SRC com/wildplot/android/rendering/LegendDrawable.java:53-56; com/wildplot/android/rendering/PlotSheet.java:500-501, 507, 519-520, 526', 'SOURCE')

UNREACHABLE['Lines.abortAndReset'] = ('no_trigger_in_app', "Empty body. The only abortAndReset call in src/main/java is DrawableContainer.java:62, inside DrawableContainer.abortAndReset, which has no caller. PlotSheet.abortAndReset has no caller. No path reaches Lines.abortAndReset.", 'SRC com/wildplot/android/rendering/Lines.java:128-132; com/wildplot/android/rendering/DrawableContainer.java:59-63; com/wildplot/android/rendering/PlotSheet.java:711-714', 'SOURCE')

UNREACHABLE['Lines.drawPoint'] = ('no_trigger_in_app', "The only mention of a call is the commented line Lines.java:95. grep for drawPoint in src/main/java finds no live call of Lines.drawPoint.", 'SRC com/wildplot/android/rendering/Lines.java:111-118; com/wildplot/android/rendering/Lines.java:95', 'SOURCE')

UNREACHABLE['Lines.unsetShadow'] = ('no_trigger_in_app', "No call in src/main/java. Lines.java:98 is the commented line g.unsetShadow(). grep for unsetShadow finds only the declarations at Lines.java:170 and GraphicsWrap.java:177.", 'SRC com/wildplot/android/rendering/Lines.java:170-172; com/wildplot/android/rendering/Lines.java:97-99; com/wildplot/android/rendering/graphics/wrapper/GraphicsWrap.java:177', 'SOURCE')

UNREACHABLE['LinesPoints.<init>'] = ('no_trigger_in_app', "Class never instantiated. A word-boundary grep over src/main/java for Integral and LinesPoints finds LinesPoints only in LinesPoints.java and in the javadoc of Lines.java (lines 24-25). No new LinesPoints(...) exists.", 'SRC com/wildplot/android/rendering/LinesPoints.java:42-46; com/wildplot/android/rendering/Lines.java:24-25', 'SOURCE')

UNREACHABLE['LinesPoints.abortAndReset'] = ('no_trigger_in_app', "Empty body. The class is never instantiated. The only abortAndReset call in src/main/java is DrawableContainer.java:62, inside an uncalled method.", 'SRC com/wildplot/android/rendering/LinesPoints.java:93-97; com/wildplot/android/rendering/DrawableContainer.java:59-63', 'SOURCE')

UNREACHABLE['LinesPoints.drawPoint'] = ('no_trigger_in_app', "The only call of LinesPoints.drawPoint is LinesPoints.java:64, inside LinesPoints.paint, which is never reached because the class is never instantiated. PointDrawer2D.java:52 and the Whiteboard.java calls are on other classes.", 'SRC com/wildplot/android/rendering/LinesPoints.java:76-83; com/wildplot/android/rendering/LinesPoints.java:64', 'SOURCE')

UNREACHABLE['LinesPoints.isClusterable'] = ('no_trigger_in_app', "Class never instantiated. The dispatch sites PlotSheet.java:500 and :519 only receive drawables added to a sheet.", 'SRC com/wildplot/android/rendering/LinesPoints.java:99-102; com/wildplot/android/rendering/PlotSheet.java:500, 519', 'SOURCE')

UNREACHABLE['LinesPoints.isCritical'] = ('no_trigger_in_app', "Class never instantiated. The call sites PlotSheet.java:501 and :520 only see drawables added to a sheet.", 'SRC com/wildplot/android/rendering/LinesPoints.java:104-107; com/wildplot/android/rendering/PlotSheet.java:501, 520', 'SOURCE')

UNREACHABLE['LinesPoints.isOnFrame'] = ('no_trigger_in_app', "Class never instantiated. The call sites PlotSheet.java:357 and :499 only see drawables added to a sheet.", 'SRC com/wildplot/android/rendering/LinesPoints.java:89-91; com/wildplot/android/rendering/PlotSheet.java:357, 499', 'SOURCE')

UNREACHABLE['LinesPoints.paint'] = ('no_trigger_in_app', "Class never instantiated. The paint call sites PlotSheet.java:366 and :473 only paint drawables added to a sheet.", 'SRC com/wildplot/android/rendering/LinesPoints.java:51-67; com/wildplot/android/rendering/PlotSheet.java:366, 473', 'SOURCE')
# ---- sup for part 113 (2026-10-28, orchestrator, build 162): Integral and LinesPoints are never instantiated (UNREACHABLE), so their outgoing automatic CALL edges are dead
sup(('Integral.paint', 'TopLevelParser.f(double)'))
sup(('LinesPoints.paint', 'LinesPoints.drawPoint'))

# ---- part 112 (2026-10-28)
# AnkiDroid batch 112 (LABEL helper). com/wildplot/android/rendering: DrawableContainer (8 methods, 2 UNREACHABLE),
# FunctionDrawer (16 methods) and FunctionDrawer_y (16 methods). The full row list is in graphs/AnkiDroid/parts/label_112.md.
# Source root: final_java_only/AnkiDroid/app/AnkiDroid-#4200/AnkiDroid/src/main/java.
# No e() edges: the calls inside these classes and along the chart route are automatic CALL edges owned by the builder.
# No MG gate is needed.

UNREACHABLE['DrawableContainer.abortAndReset'] = ('no_trigger_in_app', 'No caller reaches DrawableContainer.abortAndReset. The only call to abortAndReset in the java root is DrawableContainer.java:62, a call on child drawables inside the method body itself. PlotSheet.abortAndReset (PlotSheet.java:711-714) is empty and calls nothing.', 'SRC com/wildplot/android/rendering/DrawableContainer.java:58-63; com/wildplot/android/rendering/PlotSheet.java:711-714', 'SOURCE')

UNREACHABLE['DrawableContainer.isClusterable'] = ('branch_never_taken', 'The calls at PlotSheet.java:500 and 519 run inside the prepareDrawables loop over the drawable list. A DrawableContainer is in that list only on a second prepare pass, which needs mDrawablesPrepared reset to false by PlotSheet.addDrawable (PlotSheet.java:161). addDrawable is called only from ChartBuilder setup code inside renderChart (ChartBuilder.java:112-170), before the sheet is painted. The standard run makes one prepare pass, so DrawableContainer.isClusterable (returns false, DrawableContainer.java:65-68) never runs. The automatic CHA edge at PlotSheet.java:519 cannot fire in the standard run.', 'SRC com/wildplot/android/rendering/DrawableContainer.java:65-68; com/wildplot/android/rendering/PlotSheet.java:159-162, 484, 500, 519; com/ichi2/anki/stats/ChartBuilder.java:112-170', 'SOURCE')

UNREACHABLE['FunctionDrawer.<init>(Function2D,PlotSheet,ColorWrap)'] = ('no_trigger_in_app', 'FunctionDrawer is never instantiated in the app: no new FunctionDrawer and no reference to FunctionDrawer outside its own file (grep of the java root), so no trigger reaches this constructor.', 'SRC com/wildplot/android/rendering/FunctionDrawer.java:29, 79-83', 'SOURCE')

UNREACHABLE['FunctionDrawer.<init>(Function2D,PlotSheet,ColorWrap,double,double)'] = ('no_trigger_in_app', 'FunctionDrawer is never instantiated in the app: no new FunctionDrawer and no reference to FunctionDrawer outside its own file (grep of the java root), so no trigger reaches this constructor.', 'SRC com/wildplot/android/rendering/FunctionDrawer.java:29, 91-98', 'SOURCE')

UNREACHABLE['FunctionDrawer.abortAndReset'] = ('no_trigger_in_app', 'FunctionDrawer is never instantiated in the app: no new FunctionDrawer and no reference to FunctionDrawer outside its own file (grep of the java root), so no trigger reaches this method. The automatic CHA edge DrawableContainer.abortAndReset -> FunctionDrawer.abortAndReset (DrawableContainer.java:62) cannot fire.', 'SRC com/wildplot/android/rendering/FunctionDrawer.java:29, 257-261; com/wildplot/android/rendering/DrawableContainer.java:62', 'SOURCE')

UNREACHABLE['FunctionDrawer.getExtraScaleFactor'] = ('no_trigger_in_app', 'FunctionDrawer is never instantiated in the app: no new FunctionDrawer and no reference to FunctionDrawer outside its own file (grep of the java root), so no trigger reaches this method.', 'SRC com/wildplot/android/rendering/FunctionDrawer.java:29, 249-251', 'SOURCE')

UNREACHABLE['FunctionDrawer.getMaxValue'] = ('no_trigger_in_app', 'FunctionDrawer is never instantiated in the app: no new FunctionDrawer and no reference to FunctionDrawer outside its own file (grep of the java root), so no trigger reaches this method.', 'SRC com/wildplot/android/rendering/FunctionDrawer.java:29, 194-207', 'SOURCE')

UNREACHABLE['FunctionDrawer.isClusterable'] = ('no_trigger_in_app', 'FunctionDrawer is never instantiated in the app: no new FunctionDrawer and no reference to FunctionDrawer outside its own file (grep of the java root), so no trigger reaches this method. The automatic CHA edge PlotSheet.prepareDrawables -> FunctionDrawer.isClusterable (PlotSheet.java:519) cannot fire.', 'SRC com/wildplot/android/rendering/FunctionDrawer.java:29, 263-266; com/wildplot/android/rendering/PlotSheet.java:519', 'SOURCE')

UNREACHABLE['FunctionDrawer.isCritical'] = ('no_trigger_in_app', 'FunctionDrawer is never instantiated in the app: no new FunctionDrawer and no reference to FunctionDrawer outside its own file (grep of the java root), so no trigger reaches this method. The automatic CHA edge PlotSheet.prepareDrawables -> FunctionDrawer.isCritical (PlotSheet.java:526) cannot fire.', 'SRC com/wildplot/android/rendering/FunctionDrawer.java:29, 268-271; com/wildplot/android/rendering/PlotSheet.java:526', 'SOURCE')

UNREACHABLE['FunctionDrawer.isOnFrame'] = ('no_trigger_in_app', 'FunctionDrawer is never instantiated in the app: no new FunctionDrawer and no reference to FunctionDrawer outside its own file (grep of the java root), so no trigger reaches this method. The automatic CHA edges PlotSheet.drawSingleMode -> FunctionDrawer.isOnFrame (PlotSheet.java:357) and PlotSheet.prepareDrawables -> FunctionDrawer.isOnFrame (PlotSheet.java:499) cannot fire.', 'SRC com/wildplot/android/rendering/FunctionDrawer.java:29, 217-219; com/wildplot/android/rendering/PlotSheet.java:357, 499', 'SOURCE')

UNREACHABLE['FunctionDrawer.paint'] = ('no_trigger_in_app', 'FunctionDrawer is never instantiated in the app: no new FunctionDrawer and no reference to FunctionDrawer outside its own file (grep of the java root), so no trigger reaches this method. The automatic CHA edges PlotSheet.drawSingleMode -> FunctionDrawer.paint (PlotSheet.java:473) and DrawableContainer.paint -> FunctionDrawer.paint (DrawableContainer.java:49) cannot fire.', 'SRC com/wildplot/android/rendering/FunctionDrawer.java:29, 104-192; com/wildplot/android/rendering/PlotSheet.java:473; com/wildplot/android/rendering/DrawableContainer.java:49', 'SOURCE')

UNREACHABLE['FunctionDrawer.setAutoscale'] = ('no_trigger_in_app', 'FunctionDrawer is never instantiated in the app: no new FunctionDrawer and no reference to FunctionDrawer outside its own file (grep of the java root), so no trigger reaches this method.', 'SRC com/wildplot/android/rendering/FunctionDrawer.java:29, 241-244', 'SOURCE')

UNREACHABLE['FunctionDrawer.setExtraScaleFactor'] = ('no_trigger_in_app', 'FunctionDrawer is never instantiated in the app: no new FunctionDrawer and no reference to FunctionDrawer outside its own file (grep of the java root), so no trigger reaches this method.', 'SRC com/wildplot/android/rendering/FunctionDrawer.java:29, 253-255', 'SOURCE')

UNREACHABLE['FunctionDrawer.setOnFrame()'] = ('no_trigger_in_app', 'FunctionDrawer is never instantiated in the app: no new FunctionDrawer and no reference to FunctionDrawer outside its own file (grep of the java root), so no trigger reaches this method.', 'SRC com/wildplot/android/rendering/FunctionDrawer.java:29, 237-239', 'SOURCE')

UNREACHABLE['FunctionDrawer.setOnFrame(double)'] = ('no_trigger_in_app', 'FunctionDrawer is never instantiated in the app: no new FunctionDrawer and no reference to FunctionDrawer outside its own file (grep of the java root), so no trigger reaches this method.', 'SRC com/wildplot/android/rendering/FunctionDrawer.java:29, 232-235', 'SOURCE')

UNREACHABLE['FunctionDrawer.setSize'] = ('no_trigger_in_app', 'FunctionDrawer is never instantiated in the app: no new FunctionDrawer and no reference to FunctionDrawer outside its own file (grep of the java root), so no trigger reaches this method.', 'SRC com/wildplot/android/rendering/FunctionDrawer.java:29, 213-215', 'SOURCE')

UNREACHABLE['FunctionDrawer.unsetAutoscale'] = ('no_trigger_in_app', 'FunctionDrawer is never instantiated in the app: no new FunctionDrawer and no reference to FunctionDrawer outside its own file (grep of the java root), so no trigger reaches this method.', 'SRC com/wildplot/android/rendering/FunctionDrawer.java:29, 245-247', 'SOURCE')

UNREACHABLE['FunctionDrawer.unsetOnFrame'] = ('no_trigger_in_app', 'FunctionDrawer is never instantiated in the app: no new FunctionDrawer and no reference to FunctionDrawer outside its own file (grep of the java root), so no trigger reaches this method.', 'SRC com/wildplot/android/rendering/FunctionDrawer.java:29, 224-227', 'SOURCE')

UNREACHABLE['FunctionDrawer_y.<init>(Function2D,PlotSheet,ColorWrap)'] = ('no_trigger_in_app', 'FunctionDrawer_y is never instantiated in the app: no new FunctionDrawer_y and no reference to FunctionDrawer_y outside its own file (grep of the java root), so no trigger reaches this constructor.', 'SRC com/wildplot/android/rendering/FunctionDrawer_y.java:29, 78-82', 'SOURCE')

UNREACHABLE['FunctionDrawer_y.<init>(Function2D,PlotSheet,ColorWrap,double,double)'] = ('no_trigger_in_app', 'FunctionDrawer_y is never instantiated in the app: no new FunctionDrawer_y and no reference to FunctionDrawer_y outside its own file (grep of the java root), so no trigger reaches this constructor.', 'SRC com/wildplot/android/rendering/FunctionDrawer_y.java:29, 90-97', 'SOURCE')

UNREACHABLE['FunctionDrawer_y.abortAndReset'] = ('no_trigger_in_app', 'FunctionDrawer_y is never instantiated in the app: no new FunctionDrawer_y and no reference to FunctionDrawer_y outside its own file (grep of the java root), so no trigger reaches this method. The automatic CHA edge DrawableContainer.abortAndReset -> FunctionDrawer_y.abortAndReset (DrawableContainer.java:62) cannot fire.', 'SRC com/wildplot/android/rendering/FunctionDrawer_y.java:29, 258-262; com/wildplot/android/rendering/DrawableContainer.java:62', 'SOURCE')

UNREACHABLE['FunctionDrawer_y.getExtraScaleFactor'] = ('no_trigger_in_app', 'FunctionDrawer_y is never instantiated in the app: no new FunctionDrawer_y and no reference to FunctionDrawer_y outside its own file (grep of the java root), so no trigger reaches this method.', 'SRC com/wildplot/android/rendering/FunctionDrawer_y.java:29, 250-252', 'SOURCE')

UNREACHABLE['FunctionDrawer_y.getMaxValue'] = ('no_trigger_in_app', 'FunctionDrawer_y is never instantiated in the app: no new FunctionDrawer_y and no reference to FunctionDrawer_y outside its own file (grep of the java root), so no trigger reaches this method.', 'SRC com/wildplot/android/rendering/FunctionDrawer_y.java:29, 197-210', 'SOURCE')

UNREACHABLE['FunctionDrawer_y.isClusterable'] = ('no_trigger_in_app', 'FunctionDrawer_y is never instantiated in the app: no new FunctionDrawer_y and no reference to FunctionDrawer_y outside its own file (grep of the java root), so no trigger reaches this method. The automatic CHA edge PlotSheet.prepareDrawables -> FunctionDrawer_y.isClusterable (PlotSheet.java:519) cannot fire.', 'SRC com/wildplot/android/rendering/FunctionDrawer_y.java:29, 264-267; com/wildplot/android/rendering/PlotSheet.java:519', 'SOURCE')

UNREACHABLE['FunctionDrawer_y.isCritical'] = ('no_trigger_in_app', 'FunctionDrawer_y is never instantiated in the app: no new FunctionDrawer_y and no reference to FunctionDrawer_y outside its own file (grep of the java root), so no trigger reaches this method. The automatic CHA edge PlotSheet.prepareDrawables -> FunctionDrawer_y.isCritical (PlotSheet.java:526) cannot fire.', 'SRC com/wildplot/android/rendering/FunctionDrawer_y.java:29, 269-272; com/wildplot/android/rendering/PlotSheet.java:526', 'SOURCE')

UNREACHABLE['FunctionDrawer_y.isOnFrame'] = ('no_trigger_in_app', 'FunctionDrawer_y is never instantiated in the app: no new FunctionDrawer_y and no reference to FunctionDrawer_y outside its own file (grep of the java root), so no trigger reaches this method. The automatic CHA edges PlotSheet.drawSingleMode -> FunctionDrawer_y.isOnFrame (PlotSheet.java:357) and PlotSheet.prepareDrawables -> FunctionDrawer_y.isOnFrame (PlotSheet.java:499) cannot fire.', 'SRC com/wildplot/android/rendering/FunctionDrawer_y.java:29, 218-220; com/wildplot/android/rendering/PlotSheet.java:357, 499', 'SOURCE')

UNREACHABLE['FunctionDrawer_y.paint'] = ('no_trigger_in_app', 'FunctionDrawer_y is never instantiated in the app: no new FunctionDrawer_y and no reference to FunctionDrawer_y outside its own file (grep of the java root), so no trigger reaches this method. The automatic CHA edges PlotSheet.drawSingleMode -> FunctionDrawer_y.paint (PlotSheet.java:473) and DrawableContainer.paint -> FunctionDrawer_y.paint (DrawableContainer.java:49) cannot fire.', 'SRC com/wildplot/android/rendering/FunctionDrawer_y.java:29, 103-194; com/wildplot/android/rendering/PlotSheet.java:473; com/wildplot/android/rendering/DrawableContainer.java:49', 'SOURCE')

UNREACHABLE['FunctionDrawer_y.setAutoscale'] = ('no_trigger_in_app', 'FunctionDrawer_y is never instantiated in the app: no new FunctionDrawer_y and no reference to FunctionDrawer_y outside its own file (grep of the java root), so no trigger reaches this method.', 'SRC com/wildplot/android/rendering/FunctionDrawer_y.java:29, 242-245', 'SOURCE')

UNREACHABLE['FunctionDrawer_y.setExtraScaleFactor'] = ('no_trigger_in_app', 'FunctionDrawer_y is never instantiated in the app: no new FunctionDrawer_y and no reference to FunctionDrawer_y outside its own file (grep of the java root), so no trigger reaches this method.', 'SRC com/wildplot/android/rendering/FunctionDrawer_y.java:29, 254-256', 'SOURCE')

UNREACHABLE['FunctionDrawer_y.setOnFrame()'] = ('no_trigger_in_app', 'FunctionDrawer_y is never instantiated in the app: no new FunctionDrawer_y and no reference to FunctionDrawer_y outside its own file (grep of the java root), so no trigger reaches this method.', 'SRC com/wildplot/android/rendering/FunctionDrawer_y.java:29, 238-240', 'SOURCE')

UNREACHABLE['FunctionDrawer_y.setOnFrame(double)'] = ('no_trigger_in_app', 'FunctionDrawer_y is never instantiated in the app: no new FunctionDrawer_y and no reference to FunctionDrawer_y outside its own file (grep of the java root), so no trigger reaches this method.', 'SRC com/wildplot/android/rendering/FunctionDrawer_y.java:29, 233-236', 'SOURCE')

UNREACHABLE['FunctionDrawer_y.setSize'] = ('no_trigger_in_app', 'FunctionDrawer_y is never instantiated in the app: no new FunctionDrawer_y and no reference to FunctionDrawer_y outside its own file (grep of the java root), so no trigger reaches this method.', 'SRC com/wildplot/android/rendering/FunctionDrawer_y.java:29, 214-216', 'SOURCE')

UNREACHABLE['FunctionDrawer_y.unsetAutoscale'] = ('no_trigger_in_app', 'FunctionDrawer_y is never instantiated in the app: no new FunctionDrawer_y and no reference to FunctionDrawer_y outside its own file (grep of the java root), so no trigger reaches this method.', 'SRC com/wildplot/android/rendering/FunctionDrawer_y.java:29, 246-248', 'SOURCE')

UNREACHABLE['FunctionDrawer_y.unsetOnFrame'] = ('no_trigger_in_app', 'FunctionDrawer_y is never instantiated in the app: no new FunctionDrawer_y and no reference to FunctionDrawer_y outside its own file (grep of the java root), so no trigger reaches this method.', 'SRC com/wildplot/android/rendering/FunctionDrawer_y.java:29, 225-228', 'SOURCE')

# ---- sup for part 112 (2026-10-28, orchestrator, build 163): Integral, LinesPoints, FunctionDrawer and FunctionDrawer_y have no construction or subclass in the java root; DrawableContainer.abortAndReset has no caller except its own body; FunctionDrawer(_y).getMaxValue has no call site
sup(('DrawableContainer.paint', 'FunctionDrawer.paint'))
sup(('DrawableContainer.paint', 'FunctionDrawer_y.paint'))
sup(('DrawableContainer.paint', 'Integral.paint'))
sup(('DrawableContainer.paint', 'LinesPoints.paint'))
sup(('DrawableContainer.abortAndReset', 'DrawableContainer.abortAndReset'))
sup(('DrawableContainer.abortAndReset', 'BarGraph.abortAndReset'))
sup(('DrawableContainer.abortAndReset', 'FunctionDrawer.abortAndReset'))
sup(('DrawableContainer.abortAndReset', 'FunctionDrawer_y.abortAndReset'))
sup(('DrawableContainer.abortAndReset', 'Integral.abortAndReset'))
sup(('DrawableContainer.abortAndReset', 'LegendDrawable.abortAndReset'))
sup(('DrawableContainer.abortAndReset', 'Lines.abortAndReset'))
sup(('DrawableContainer.abortAndReset', 'LinesPoints.abortAndReset'))
sup(('DrawableContainer.abortAndReset', 'PieChart.abortAndReset'))
sup(('FunctionDrawer.setOnFrame()', 'FunctionDrawer.setOnFrame(double)'))
sup(('FunctionDrawer_y.setOnFrame()', 'FunctionDrawer_y.setOnFrame(double)'))
sup(('FunctionDrawer.paint', 'TopLevelParser.f(double)'))
sup(('FunctionDrawer_y.paint', 'TopLevelParser.f(double)'))
sup(('FunctionDrawer.getMaxValue', 'TopLevelParser.f(double)'))
sup(('FunctionDrawer_y.getMaxValue', 'TopLevelParser.f(double)'))

# ---- part 117 (2026-10-28)
UNREACHABLE['PointDrawer2D.<init>'] = ('no_trigger_in_app', "grep -rn over the source root for new PointDrawer2D and extends PointDrawer2D finds nothing; the only matches are the class declaration and this constructor. The constructor never runs and no instance of the class exists.", 'SRC com/wildplot/android/rendering/PointDrawer2D.java:28, 36-40', 'SOURCE')
UNREACHABLE['PointDrawer2D.paint'] = ('no_trigger_in_app', "paint is the Drawable.paint implementation. The interface call sites that could reach it are DrawableContainer.java:49 and PlotSheet.java:473, and they can only reach an object that exists. No PointDrawer2D object is created (see PointDrawer2D.<init>), so the body at lines 47-54 never runs.", 'SRC com/wildplot/android/rendering/PointDrawer2D.java:46-55; com/wildplot/android/rendering/DrawableContainer.java:40-50; com/wildplot/android/rendering/PlotSheet.java:470-474', 'SOURCE')
UNREACHABLE['PointDrawer2D.drawPoint'] = ('no_trigger_in_app', "The only call of this method on the class is PointDrawer2D.java:52, inside paint (lines 51-53). paint has no route (see the paint row), so drawPoint has none. Other drawPoint calls in the root are on other classes (LinesPoints.drawPoint, and Canvas.drawPoint in Whiteboard.java), per grep -rn.", 'SRC com/wildplot/android/rendering/PointDrawer2D.java:52, 64-70', 'SOURCE')
UNREACHABLE['PointDrawer2D.isOnFrame'] = ('no_trigger_in_app', "Called through the Drawable interface at PlotSheet.java:357 and :499. These calls reach only an existing PointDrawer2D object, and none is created (see PointDrawer2D.<init>). The body returns false (line 77).", 'SRC com/wildplot/android/rendering/PointDrawer2D.java:76-78; com/wildplot/android/rendering/PlotSheet.java:357, 499', 'SOURCE')
UNREACHABLE['PointDrawer2D.abortAndReset'] = ('no_trigger_in_app', "Called through the Drawable interface at DrawableContainer.java:62 (currentDrawable.abortAndReset). It reaches only an existing object, and none is created. The body is an empty TODO stub (lines 81-83).", 'SRC com/wildplot/android/rendering/PointDrawer2D.java:80-84; com/wildplot/android/rendering/DrawableContainer.java:58-63', 'SOURCE')
UNREACHABLE['PointDrawer2D.isClusterable'] = ('no_trigger_in_app', "Called through the Drawable interface at PlotSheet.java:500 and :519. It reaches only an existing object, and none is created. The body returns true (line 88).", 'SRC com/wildplot/android/rendering/PointDrawer2D.java:86-89; com/wildplot/android/rendering/PlotSheet.java:500, 519', 'SOURCE')
UNREACHABLE['PointDrawer2D.isCritical'] = ('no_trigger_in_app', "Called through the Drawable interface at PlotSheet.java:501, 507, 520 and 526. It reaches only an existing object, and none is created. The body returns true (line 93).", 'SRC com/wildplot/android/rendering/PointDrawer2D.java:91-94; com/wildplot/android/rendering/PlotSheet.java:501-526', 'SOURCE')
UNREACHABLE['RelativeColorGradient.<init>'] = ('no_trigger_in_app', "The class declares no constructor, so <init> is the implicit default constructor. grep -rn over the source root finds no new RelativeColorGradient and no subclass. The class is used only through its static methods (makeGradient, delta), so the constructor never runs.", 'SRC com/wildplot/android/rendering/RelativeColorGradient.java:24-78', 'SOURCE')
UNREACHABLE['RelativeColorGradient.makeGradient'] = ('no_trigger_in_app', "Its only callers are ReliefDrawer.java:132 (inside the constructor that starts at line 120) and :179 (inside the constructor that starts at line 165). ReliefDrawer is never instantiated: grep -rn over the root finds no new ReliefDrawer and no reference to the class outside ReliefDrawer.java. So both constructors never run. ChartBuilder.java in com/ichi2/anki/stats constructs PieChart, LegendDrawable, BarGraph, Lines, XAxis, XGrid and YGrid, not ReliefDrawer, PointDrawer2D or RelativeColorGradient.", 'SRC com/wildplot/android/rendering/RelativeColorGradient.java:25-71; com/wildplot/android/rendering/ReliefDrawer.java:120-132, 165-179; com/ichi2/anki/stats/ChartBuilder.java:173, 181, 240, 267, 279, 342-343', 'SOURCE')
UNREACHABLE['RelativeColorGradient.delta'] = ('no_trigger_in_app', "Its only callers are inside makeGradient (RelativeColorGradient.java:47-49), which has no route (see the makeGradient row). The body (line 73) returns Math.pow(Math.abs(first - second), 3).", 'SRC com/wildplot/android/rendering/RelativeColorGradient.java:47-49, 72-74', 'SOURCE')

# ---- sup for part 117 (2026-10-28, orchestrator, build 164): PointDrawer2D is never instantiated (no new PointDrawer2D( and no subclass in the java root), so CHA edges into its methods are not on any route
sup(('DrawableContainer.paint', 'PointDrawer2D.paint'))
sup(('DrawableContainer.abortAndReset', 'PointDrawer2D.abortAndReset'))
sup(('PointDrawer2D.paint', 'PointDrawer2D.drawPoint'))

# ---- part 116 (2026-10-28)
UNREACHABLE['PlotSheet.xToCoordinateLog'] = ('no_trigger_in_app', "Reached only from xToCoordinate, which has two callers: toCoordinatePoint and the Integral class (line 99). toCoordinatePoint has seven caller classes (FunctionDrawer, FunctionDrawer_y, ReliefDrawer, XAxisBarGraph, YAxisBarGraph, XAxisHistoGram, YAxisHistoGram), and Integral is also never constructed. No code constructs these classes or refers to them outside their own files. The Log branch is also never selected, because isLogX stays false. The callers never run, so the kind is no_trigger_in_app.", 'SRC com/wildplot/android/rendering/PlotSheet.java:40, 246-249, 261-267, 312-313; SRC com/wildplot/android/rendering/Integral.java:29, 99; SRC com/wildplot/android/rendering/FunctionDrawer.java:29, 121-122, 134-136, 162, 196, 200; SRC com/wildplot/android/rendering/FunctionDrawer_y.java:29, 117-118, 130-132, 161, 199, 203; SRC com/wildplot/android/rendering/ReliefDrawer.java:34, 301-303, 313-315, 354, 639, 652, 700, 709; SRC com/wildplot/android/rendering/XAxisBarGraph.java:29, 100-101; SRC com/wildplot/android/rendering/YAxisBarGraph.java:29, 102-103; SRC com/wildplot/android/rendering/XAxisHistoGram.java:29, 106-107; SRC com/wildplot/android/rendering/YAxisHistoGram.java:29, 104-105', 'SOURCE')
UNREACHABLE['PlotSheet.yToCoordinate'] = ('no_trigger_in_app', "The only caller is toCoordinatePoint (line 313). Its seven caller classes are never constructed, and no code outside their own files refers to them.", 'SRC com/wildplot/android/rendering/PlotSheet.java:280-283, 312-313; SRC com/wildplot/android/rendering/FunctionDrawer.java:29, 121-122, 134-136, 162, 196, 200; SRC com/wildplot/android/rendering/FunctionDrawer_y.java:29, 117-118, 130-132, 161, 199, 203; SRC com/wildplot/android/rendering/ReliefDrawer.java:34, 301-303, 313-315, 354, 639, 652, 700, 709; SRC com/wildplot/android/rendering/XAxisBarGraph.java:29, 100-101; SRC com/wildplot/android/rendering/YAxisBarGraph.java:29, 102-103; SRC com/wildplot/android/rendering/XAxisHistoGram.java:29, 106-107; SRC com/wildplot/android/rendering/YAxisHistoGram.java:29, 104-105', 'SOURCE')
UNREACHABLE['PlotSheet.yToCoordinateLinear'] = ('no_trigger_in_app', "The only caller is yToCoordinate (line 283), which is reached only through toCoordinatePoint (line 313). Those callers never run, as listed for yToCoordinate.", 'SRC com/wildplot/android/rendering/PlotSheet.java:283, 286-292, 312-313', 'SOURCE')
UNREACHABLE['PlotSheet.yToCoordinateLog'] = ('no_trigger_in_app', "Same chain as yToCoordinate (lines 283 and 313), so the callers never run. The Log branch is also never selected, because isLogY stays false (line 43).", 'SRC com/wildplot/android/rendering/PlotSheet.java:43, 280-283, 295-304, 312-313', 'SOURCE')
UNREACHABLE['PlotSheet.xToGraphicLog'] = ('branch_never_taken', "xToGraphic (line 174) is reached, but it selects this method only when isLogX is true. isLogX starts false (line 40). The only assignment of true is in setLogX (line 693), and setLogX has no call in the source root (grep over the source root shows only its definition). The only other assignment, in unsetLogX (line 701), sets it false.", 'SRC com/wildplot/android/rendering/PlotSheet.java:40, 172-175, 184-190, 692-694, 700-702', 'SOURCE')
UNREACHABLE['PlotSheet.yToGraphicLog'] = ('branch_never_taken', "yToGraphic (line 202) is reached, but it selects this method only when isLogY is true. isLogY starts false (line 43). The only assignment of true is in setLogY (line 697), and setLogY has no call in the source root (grep over the source root shows only its definition). No other code sets isLogY true.", 'SRC com/wildplot/android/rendering/PlotSheet.java:43, 201-203, 215-223, 696-698, 704-706', 'SOURCE')

# ---- part 118 (2026-10-28)
# AnkiDroid batch 118 (LABEL helper). ReliefDrawer (com/wildplot/android/rendering/ReliefDrawer.java), 31 methods, all UNREACHABLE.
# Full rows: graphs/AnkiDroid/parts/label_118.md. No e() edges: the trigger edges from this class are automatic CALL edges
# (createCopy and Function3D.f), and the edges into it are class-hierarchy dispatches from PlotSheet and DrawableContainer,
# which are not written here (see the final answer for the pairs to suppress).

UNREACHABLE['ReliefDrawer.<init>(double,int,Function3D,PlotSheet,boolean)'] = ('no_trigger_in_app', 'No code in the source root creates a ReliefDrawer. A case-insensitive grep for relief over the source root finds no reference outside ReliefDrawer, so no new ReliefDrawer( runs for this signature. The constructor has no caller, so no instance exists and no method of the class can run.', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:120-136', 'SOURCE')
UNREACHABLE['ReliefDrawer.<init>(double,int,Function3D,PlotSheet,boolean,ColorWrap)'] = ('no_trigger_in_app', 'Same as the five-argument constructor: no caller anywhere in the source root (the grep finds no ReliefDrawer reference outside its own file), so no instance is created.', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:165-183', 'SOURCE')
UNREACHABLE['ReliefDrawer.<init>(double,Function3D,PlotSheet)'] = ('no_trigger_in_app', 'Same as the other constructors: no caller in the source root, so no instance is created and this constructor never runs.', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:145-152', 'SOURCE')
UNREACHABLE['ReliefDrawer.abortAndReset'] = ('no_trigger_in_app', 'Drawable.abortAndReset reaches an object only through DrawableContainer.abortAndReset (currentDrawable.abortAndReset). That needs a ReliefDrawer object in the list, and none is created (see the constructors). The class-hierarchy edge DrawableContainer.abortAndReset -> ReliefDrawer.abortAndReset is not a real route.', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:722-726; com/wildplot/android/rendering/DrawableContainer.java:59-62', 'SOURCE')
UNREACHABLE['ReliefDrawer.drawBorders'] = ('no_trigger_in_app', 'Private. The only caller is paint (line 215). paint is unreachable because no ReliefDrawer instance is created.', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:299-326; com/wildplot/android/rendering/ReliefDrawer.java:215', 'SOURCE')
UNREACHABLE['ReliefDrawer.drawColoredRelief'] = ('no_trigger_in_app', 'Private. The only caller is paint (line 208). Unreachable with paint.', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:227-293; com/wildplot/android/rendering/ReliefDrawer.java:208', 'SOURCE')
UNREACHABLE['ReliefDrawer.getColor'] = ('no_trigger_in_app', 'Private. Called only from ReliefLegend.paint (line 540) and PartRenderer.run (line 711), both inside ReliefDrawer. Those run only through paint or getLegend, which are unreachable.', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:442-463; com/wildplot/android/rendering/ReliefDrawer.java:540, 711', 'SOURCE')
UNREACHABLE['ReliefDrawer.getLegend'] = ('no_trigger_in_app', 'No caller: a grep for getLegend over the source root finds only the declaration (line 473). It also needs a ReliefDrawer instance, and none exists. It creates ReliefLegend (line 474).', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:473-475', 'SOURCE')
UNREACHABLE['ReliefDrawer.getPixelSkip'] = ('no_trigger_in_app', 'No caller: a grep for getPixelSkip over the source root finds only the declaration (line 728). No ReliefDrawer instance exists.', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:728-730', 'SOURCE')
UNREACHABLE['ReliefDrawer.isClusterable'] = ('no_trigger_in_app', 'Drawable.isClusterable is called by PlotSheet.prepareDrawables on the drawables in the list (PlotSheet.java:500, 519). The list never holds a ReliefDrawer, because none is created. The cha edges PlotSheet.prepareDrawables -> ReliefDrawer.isClusterable are not real routes.', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:736-739; com/wildplot/android/rendering/PlotSheet.java:499-526', 'SOURCE')
UNREACHABLE['ReliefDrawer.isCritical'] = ('no_trigger_in_app', 'Drawable.isCritical is called by PlotSheet.prepareDrawables (PlotSheet.java:501, 520, 526) on the drawables in the list. No ReliefDrawer is ever created, so the cha edges into this method are not real routes.', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:741-744; com/wildplot/android/rendering/PlotSheet.java:499-526', 'SOURCE')
UNREACHABLE['ReliefDrawer.isOnFrame'] = ('no_trigger_in_app', 'Drawable.isOnFrame is called by PlotSheet.drawSingleMode (PlotSheet.java:357) and PlotSheet.prepareDrawables (PlotSheet.java:499) on the drawables in the list. No ReliefDrawer is ever created, so the cha edges into this method are not real routes.', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:469-471; com/wildplot/android/rendering/PlotSheet.java:357, 499', 'SOURCE')
UNREACHABLE['ReliefDrawer.onBorder'] = ('no_trigger_in_app', 'Private. The only caller is drawBorders (line 320, two calls). drawBorders is unreachable.', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:420-435; com/wildplot/android/rendering/ReliefDrawer.java:320', 'SOURCE')
UNREACHABLE['ReliefDrawer.paint'] = ('no_trigger_in_app', 'Drawable.paint is dispatched to the drawables in a list from PlotSheet.drawSingleMode (PlotSheet.java:366, 473) and DrawableContainer.paint (DrawableContainer.java:49). The list never holds a ReliefDrawer, because none is created (see the constructors). The cha edges PlotSheet.drawSingleMode -> ReliefDrawer.paint (PlotSheet.java:473) and DrawableContainer.paint -> ReliefDrawer.paint (DrawableContainer.java:49) are not real routes.', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:189-221; com/wildplot/android/rendering/PlotSheet.java:322-327, 366, 473; com/wildplot/android/rendering/DrawableContainer.java:47-50; com/ichi2/anki/stats/ChartView.java:70', 'SOURCE')
UNREACHABLE['ReliefDrawer.rangeHasChanged'] = ('no_trigger_in_app', 'Private. Called from paint (line 195) and ReliefLegend.paint (line 508). Both are unreachable.', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:332-346; com/wildplot/android/rendering/ReliefDrawer.java:195, 508', 'SOURCE')
UNREACHABLE['ReliefDrawer.scanDepth'] = ('no_trigger_in_app', 'Private. The only caller is paint (line 197). Unreachable with paint.', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:352-412; com/wildplot/android/rendering/ReliefDrawer.java:197', 'SOURCE')
UNREACHABLE['ReliefDrawer.setPixelSkip'] = ('no_trigger_in_app', 'No caller: a grep for setPixelSkip over the source root finds only the declaration (line 732). No ReliefDrawer instance exists.', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:732-734', 'SOURCE')
UNREACHABLE['ReliefDrawer.setThreadCnt'] = ('no_trigger_in_app', 'No caller: a grep for setThreadCnt over the source root finds only the declaration (line 480). No ReliefDrawer instance exists.', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:480-482', 'SOURCE')
UNREACHABLE['ReliefDrawer$DepthSearcher.<init>'] = ('no_trigger_in_app', 'Private inner class constructor. Created only in scanDepth (new DepthSearcher at lines 369, 372, 378). scanDepth is reachable only from paint (line 197), which is unreachable because no ReliefDrawer instance is created. The createCopy call at line 632 is an automatic CALL edge and runs only in this constructor.', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:626-634; com/wildplot/android/rendering/ReliefDrawer.java:369, 372, 378', 'SOURCE')
UNREACHABLE['ReliefDrawer$DepthSearcher.getF_xHighest'] = ('no_trigger_in_app', 'Called only from scanDepth (lines 393-394), on DepthSearcher objects that exist only inside scanDepth. scanDepth is unreachable.', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:667-669; com/wildplot/android/rendering/ReliefDrawer.java:393-394', 'SOURCE')
UNREACHABLE['ReliefDrawer$DepthSearcher.getF_xLowest'] = ('no_trigger_in_app', 'Called only from scanDepth (lines 395-396), on DepthSearcher objects that exist only inside scanDepth. scanDepth is unreachable.', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:672-674; com/wildplot/android/rendering/ReliefDrawer.java:395-396', 'SOURCE')
UNREACHABLE['ReliefDrawer$DepthSearcher.run'] = ('no_trigger_in_app', 'Runs only as a Thread started in scanDepth (thread.start at lines 384-386; the threads are built at lines 361-382). scanDepth is unreachable.', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:637-665; com/wildplot/android/rendering/ReliefDrawer.java:384-386', 'SOURCE')
UNREACHABLE['ReliefDrawer$PartRenderer.<init>'] = ('no_trigger_in_app', 'Created only in drawColoredRelief (new PartRenderer at lines 256, 264, 274). drawColoredRelief is called only from paint (line 208), which is unreachable. The createCopy call at line 693 is an automatic CALL edge and runs only in this constructor.', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:686-695; com/wildplot/android/rendering/ReliefDrawer.java:256, 264, 274', 'SOURCE')
UNREACHABLE['ReliefDrawer$PartRenderer.run'] = ('no_trigger_in_app', 'Runs only as a Thread started in drawColoredRelief (thread.start at lines 280-282). drawColoredRelief is unreachable.', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:698-718; com/wildplot/android/rendering/ReliefDrawer.java:280-282', 'SOURCE')
UNREACHABLE['ReliefDrawer$ReliefLegend.<init>'] = ('no_trigger_in_app', 'The class declares no constructor (its fields are at lines 497-500), so this is the default constructor. It runs only at new ReliefLegend() in getLegend (line 474). getLegend has no caller and no ReliefDrawer instance exists.', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:492-500; com/wildplot/android/rendering/ReliefDrawer.java:474', 'SOURCE')
UNREACHABLE['ReliefDrawer$ReliefLegend.abortAndReset'] = ('no_trigger_in_app', 'Drawable.abortAndReset dispatch from DrawableContainer.abortAndReset reaches it only if a ReliefLegend object exists. ReliefLegend is created only in getLegend, which has no caller. Not a real route.', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:600-604; com/wildplot/android/rendering/DrawableContainer.java:59-62', 'SOURCE')
UNREACHABLE['ReliefDrawer$ReliefLegend.isClusterable'] = ('no_trigger_in_app', 'Drawable.isClusterable is called by PlotSheet.prepareDrawables (PlotSheet.java:500, 519) on the list members. getLegend() has no caller and its enclosing class is never constructed, so the creation site never runs; the cha edges into this method are not real routes.', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:605-608; com/wildplot/android/rendering/PlotSheet.java:499-526', 'SOURCE')
UNREACHABLE['ReliefDrawer$ReliefLegend.isCritical'] = ('no_trigger_in_app', 'Drawable.isCritical is called by PlotSheet.prepareDrawables (PlotSheet.java:501, 520, 526) on the list members. getLegend() has no caller and its enclosing class is never constructed, so the creation site never runs; the cha edges into this method are not real routes.', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:610-613; com/wildplot/android/rendering/PlotSheet.java:499-526', 'SOURCE')
UNREACHABLE['ReliefDrawer$ReliefLegend.isOnFrame'] = ('no_trigger_in_app', 'Drawable.isOnFrame is called by PlotSheet.drawSingleMode (PlotSheet.java:357) and PlotSheet.prepareDrawables (PlotSheet.java:499) on the list members. getLegend() has no caller and its enclosing class is never constructed, so the creation site never runs; the cha edges into this method are not real routes.', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:596-598; com/wildplot/android/rendering/PlotSheet.java:357, 499', 'SOURCE')
UNREACHABLE['ReliefDrawer$ReliefLegend.paint'] = ('no_trigger_in_app', 'Drawable.paint dispatch from PlotSheet.drawSingleMode (PlotSheet.java:366, 473) and DrawableContainer.paint (DrawableContainer.java:49). A ReliefLegend object exists only after getLegend, which has no caller. The cha edges PlotSheet.drawSingleMode -> ReliefDrawer$ReliefLegend.paint and DrawableContainer.paint -> ReliefDrawer$ReliefLegend.paint are not real routes.', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:506-573; com/wildplot/android/rendering/PlotSheet.java:366, 473; com/wildplot/android/rendering/DrawableContainer.java:47-50', 'SOURCE')
UNREACHABLE['ReliefDrawer$ReliefLegend.ticsCalc'] = ('no_trigger_in_app', 'Private. Called only from ReliefLegend.paint (line 550). It is not ChartBuilder.ticsCalc (com/ichi2/anki/stats/ChartBuilder.java:389), which is a different method. Unreachable with ReliefLegend.paint.', 'SRC com/wildplot/android/rendering/ReliefDrawer.java:581-590; com/wildplot/android/rendering/ReliefDrawer.java:550; com/ichi2/anki/stats/ChartBuilder.java:389', 'SOURCE')

# ---- part 119 (2026-10-28)
# AnkiDroid batch 119 (LABEL helper): com/wildplot/android/rendering/XAxis, 25 methods.
# Full rows are in graphs/AnkiDroid/parts/label_119.md.
# No e() edges: every edge into or out of these methods is an automatic CALL edge (builder bytecode, not repeated here)
# or belongs to another batch.

UNREACHABLE['XAxis.<init>(PlotSheet,double,float,float)'] = ('no_trigger_in_app', "The only new XAxis call in the source root is ChartBuilder.java:279 and it passes two doubles, so this float overload is never selected.", 'SRC com/ichi2/anki/stats/ChartBuilder.java:279; com/wildplot/android/rendering/XAxis.java:155-161', 'SOURCE')
UNREACHABLE['XAxis.abortAndReset'] = ('no_trigger_in_app', "The body is an empty stub. The only abortAndReset() call in the source root is in DrawableContainer.abortAndReset, and nothing calls DrawableContainer.abortAndReset. PlotSheet.abortAndReset is also empty.", 'SRC com/wildplot/android/rendering/XAxis.java:486-489; com/wildplot/android/rendering/DrawableContainer.java:59-63; com/wildplot/android/rendering/PlotSheet.java:711-713', 'SOURCE')
UNREACHABLE['XAxis.drawDownwardsMarker'] = ('branch_never_taken', "Both callers guard the call with markOnDownside. setOnFrame sets it to false at ChartBuilder.java:280 before paint, and the only later writer that sets it to true, unsetOnFrame, has no caller. The branch is never taken during paint.", 'SRC com/wildplot/android/rendering/XAxis.java:343-348, 253-254, 277-278, 376-380, 385-389; com/ichi2/anki/stats/ChartBuilder.java:280', 'SOURCE')
UNREACHABLE['XAxis.drawDownwardsMinorMarker'] = ('branch_never_taken', "The only caller is drawMinorMarkers, which guards the call with markOnDownside. The guard is false for the same reason as drawDownwardsMarker: setOnFrame runs before paint and unsetOnFrame has no caller.", 'SRC com/wildplot/android/rendering/XAxis.java:476-481, 430-431, 376-380; com/ichi2/anki/stats/ChartBuilder.java:280', 'SOURCE')
UNREACHABLE['XAxis.getyOffset'] = ('no_trigger_in_app', "No call to getyOffset exists in the source root. A search finds only the definition.", 'SRC com/wildplot/android/rendering/XAxis.java:354-356', 'SOURCE')
UNREACHABLE['XAxis.setyOffset'] = ('no_trigger_in_app', "No call to setyOffset exists in the source root. A search finds only the definition.", 'SRC com/wildplot/android/rendering/XAxis.java:362-364', 'SOURCE')
UNREACHABLE['XAxis.unsetExplicitTics'] = ('no_trigger_in_app', "No call to unsetExplicitTics exists in the source root. A search finds only the definition in XAxis.", 'SRC com/wildplot/android/rendering/XAxis.java:504-507', 'SOURCE')
UNREACHABLE['XAxis.unsetOnFrame'] = ('no_trigger_in_app', "No call to unsetOnFrame exists in the source root. A search finds only the definitions in the axis classes.", 'SRC com/wildplot/android/rendering/XAxis.java:385-389', 'SOURCE')
UNREACHABLE['XAxis.unsetyOffset'] = ('no_trigger_in_app', "No call to unsetyOffset exists in the source root. A search finds only the definition.", 'SRC com/wildplot/android/rendering/XAxis.java:369-371', 'SOURCE')
# ---- sup for part 118 (2026-10-29, orchestrator, build 167): ReliefDrawer has no new site and no subclass, so it is never constructed; ReliefDrawer$ReliefLegend is created only in ReliefDrawer.getLegend and DepthSearcher/PartRenderer only in ReliefDrawer methods, so none of these run; RelativeColorGradient.makeGradient is called only from ReliefDrawer constructors
sup(('DrawableContainer.paint', 'ReliefDrawer.paint'))
sup(('DrawableContainer.paint', 'ReliefDrawer$ReliefLegend.paint'))
sup(('DrawableContainer.abortAndReset', 'ReliefDrawer.abortAndReset'))
sup(('DrawableContainer.abortAndReset', 'ReliefDrawer$ReliefLegend.abortAndReset'))
sup(('DrawableContainer.abortAndReset', 'XAxis.abortAndReset'))
sup(('ReliefDrawer.paint', 'ReliefDrawer.drawBorders'))
sup(('ReliefDrawer.paint', 'ReliefDrawer.drawColoredRelief'))
sup(('ReliefDrawer.paint', 'ReliefDrawer.scanDepth'))
sup(('ReliefDrawer.paint', 'ReliefDrawer.rangeHasChanged'))
sup(('ReliefDrawer$ReliefLegend.paint', 'ReliefDrawer.rangeHasChanged'))
sup(('ReliefDrawer$ReliefLegend.paint', 'ReliefDrawer.getColor'))
sup(('ReliefDrawer$ReliefLegend.paint', 'ReliefDrawer$ReliefLegend.ticsCalc'))
sup(('ReliefDrawer.drawBorders', 'ReliefDrawer.onBorder'))
sup(('ReliefDrawer.drawBorders', 'TopLevelParser.f(double,double)'))
sup(('ReliefDrawer.scanDepth', 'ReliefDrawer$DepthSearcher.<init>'))
sup(('ReliefDrawer.scanDepth', 'ReliefDrawer$DepthSearcher.getF_xHighest'))
sup(('ReliefDrawer.scanDepth', 'ReliefDrawer$DepthSearcher.getF_xLowest'))
sup(('ReliefDrawer.scanDepth', 'TopLevelParser.f(double,double)'))
sup(('ReliefDrawer.drawColoredRelief', 'ReliefDrawer$PartRenderer.<init>'))
sup(('ReliefDrawer.getLegend', 'ReliefDrawer$ReliefLegend.<init>'))
sup(('ReliefDrawer$DepthSearcher.<init>', 'TopLevelParser.createCopy()'))
sup(('ReliefDrawer$PartRenderer.<init>', 'TopLevelParser.createCopy()'))
sup(('ReliefDrawer$DepthSearcher.run', 'TopLevelParser.f(double,double)'))
sup(('ReliefDrawer$PartRenderer.run', 'TopLevelParser.f(double,double)'))
sup(('ReliefDrawer$PartRenderer.run', 'ReliefDrawer.getColor'))
sup(('ReliefDrawer.<init>(double,int,Function3D,PlotSheet,boolean)', 'RelativeColorGradient.makeGradient'))
sup(('ReliefDrawer.<init>(double,int,Function3D,PlotSheet,boolean,ColorWrap)', 'RelativeColorGradient.makeGradient'))
sup(('RelativeColorGradient.makeGradient', 'RelativeColorGradient.delta'))
# ---- sup for part 119 (2026-10-29, orchestrator, build 167): XAxis.markOnDownside is false during paint (ChartBuilder.java:280 calls setOnFrame on the only XAxis, and unsetOnFrame has no caller), so the downwards-marker branches are never taken
sup(('XAxis.drawImplicitMarker', 'XAxis.drawDownwardsMarker'))
sup(('XAxis.drawExplicitMarkers', 'XAxis.drawDownwardsMarker'))
sup(('XAxis.drawMinorMarkers', 'XAxis.drawDownwardsMinorMarker'))

# ---- part 115 (2026-10-28)
# AnkiDroid batch 115 (LABEL helper). com.wildplot.android.rendering.PlotSheet: 40 methods, 15 REACHABLE and 25 UNREACHABLE.
# The full row list is in graphs/AnkiDroid/parts/label_115.md. No e() edges in this batch.

UNREACHABLE['PlotSheet.<init>(double,double,double,double,Vector)'] = ('no_trigger_in_app', "Constructor that takes a Vector of drawables. Whole-root grep for the constructor finds only the two 4-argument calls in ChartBuilder (lines 134 and 147). The 4-argument constructor does not chain to this one. No app path builds a PlotSheet with a drawables vector.", "SRC com/wildplot/android/rendering/PlotSheet.java:112-116, 126-130; com/ichi2/anki/stats/ChartBuilder.java:134, 147", 'SOURCE')
UNREACHABLE['PlotSheet.drawMultiMode'] = ('branch_never_taken', "paint calls drawMultiMode only when isMultiMode is true. The field is set only by its initializer (false) and no setter exists; a root-wide grep of isMultiMode finds only PlotSheet.java lines 60, 324, 688 and 689 (the getter). The body is empty (TODO), so the branch never runs.", "SRC com/wildplot/android/rendering/PlotSheet.java:60, 322-333", 'SOURCE')
UNREACHABLE['PlotSheet.setBorder'] = ('no_trigger_in_app', "Whole-root grep for the method finds no call. Only unsetBorder is called (ChartBuilder.java:192).", "SRC com/wildplot/android/rendering/PlotSheet.java:619-621", 'SOURCE')
UNREACHABLE['PlotSheet.setBorderThickness'] = ('no_trigger_in_app', "Whole-root grep for the method finds no call.", "SRC com/wildplot/android/rendering/PlotSheet.java:611-613", 'SOURCE')
UNREACHABLE['PlotSheet.setLogX'] = ('no_trigger_in_app', "Whole-root grep for the method finds no call, so the log x-axis is never enabled.", "SRC com/wildplot/android/rendering/PlotSheet.java:692-694", 'SOURCE')
UNREACHABLE['PlotSheet.setLogY'] = ('no_trigger_in_app', "Whole-root grep for the method finds no call, so the log y-axis is never enabled.", "SRC com/wildplot/android/rendering/PlotSheet.java:696-698", 'SOURCE')
UNREACHABLE['PlotSheet.unsetLogX'] = ('no_trigger_in_app', "Whole-root grep for the method finds no call.", "SRC com/wildplot/android/rendering/PlotSheet.java:700-702", 'SOURCE')
UNREACHABLE['PlotSheet.unsetLogY'] = ('no_trigger_in_app', "Whole-root grep for the method finds no call.", "SRC com/wildplot/android/rendering/PlotSheet.java:704-706", 'SOURCE')
UNREACHABLE['PlotSheet.setTitle'] = ('no_trigger_in_app', "Whole-root grep for .setTitle( finds only activity, menu item, fragment and dialog builder receivers; none is a PlotSheet.", "SRC com/wildplot/android/rendering/PlotSheet.java:680-683", 'SOURCE')
UNREACHABLE['PlotSheet.setTypeface'] = ('no_trigger_in_app', "Whole-root grep for .setTypeface( finds only TextView, EditText, Button, View and GraphicsWrap receivers; no call has a PlotSheet receiver.", "SRC com/wildplot/android/rendering/PlotSheet.java:726-728", 'SOURCE')
UNREACHABLE['PlotSheet.unsetFontSize'] = ('no_trigger_in_app', "Whole-root grep for the method finds no call.", "SRC com/wildplot/android/rendering/PlotSheet.java:730-732", 'SOURCE')
UNREACHABLE['PlotSheet.updateX'] = ('no_trigger_in_app', "Whole-root grep for the method finds no call. Its body calls MultiScreenPart.setxRange (PlotSheet.java:140).", "SRC com/wildplot/android/rendering/PlotSheet.java:138-143", 'SOURCE')
UNREACHABLE['PlotSheet.updateY'] = ('no_trigger_in_app', "Whole-root grep for the method finds no call.", "SRC com/wildplot/android/rendering/PlotSheet.java:148-153", 'SOURCE')
UNREACHABLE['PlotSheet.setxRange'] = ('no_trigger_in_app', "Whole-root grep finds no call with a PlotSheet receiver. The only setxRange calls in the root are MultiScreenPart calls inside PlotSheet.updateX and PlotSheet.setxRange.", "SRC com/wildplot/android/rendering/PlotSheet.java:138-143, 565-567", 'SOURCE')
UNREACHABLE['PlotSheet.setyRange'] = ('no_trigger_in_app', "Whole-root grep finds no call with a PlotSheet receiver. The only setyRange calls in the root are MultiScreenPart calls inside PlotSheet.updateY and PlotSheet.setyRange.", "SRC com/wildplot/android/rendering/PlotSheet.java:148-153, 581-583", 'SOURCE')
UNREACHABLE['PlotSheet.abortAndReset'] = ('no_trigger_in_app', "Body is an empty TODO stub. The only call site of any abortAndReset in the source root is DrawableContainer.java:62, inside DrawableContainer.abortAndReset, and that method has no caller. PlotSheet is never added to a DrawableContainer, because prepareDrawables fills containers only from the drawables of its screen part.", "SRC com/wildplot/android/rendering/PlotSheet.java:710-714; com/wildplot/android/rendering/DrawableContainer.java:58-63", 'SOURCE')
UNREACHABLE['PlotSheet.isClusterable'] = ('no_trigger_in_app', "Returns true. The only dispatch sites are drawable.isClusterable() in prepareDrawables, on elements of the screen part. PlotSheet implements Drawable (PlotSheet.java:39), but no code adds a PlotSheet to a screen part: ChartBuilder adds only the pie chart, legends, bar graph, lines, axes and grids.", "SRC com/wildplot/android/rendering/PlotSheet.java:39, 716-719, 499-527; com/ichi2/anki/stats/ChartBuilder.java:193-196, 245, 273, 307, 331, 364-365", 'SOURCE')
UNREACHABLE['PlotSheet.isCritical'] = ('no_trigger_in_app', "Returns false. The only dispatch sites are drawable.isCritical() in prepareDrawables (lines 501 and 520), on the same screen-part elements; PlotSheet is never one of them.", "SRC com/wildplot/android/rendering/PlotSheet.java:721-724, 499-527", 'SOURCE')
UNREACHABLE['PlotSheet.isMultiMode'] = ('no_trigger_in_app', "Getter for isMultiMode. A root-wide grep finds no call to it. The field is read in paint (line 324) and in the getter, and no code in the source root assigns it true (its only assignment is the initializer at line 60).", "SRC com/wildplot/android/rendering/PlotSheet.java:60, 322-324, 686-690", 'SOURCE')
UNREACHABLE['PlotSheet.isOnFrame'] = ('no_trigger_in_app', "Returns false. The only dispatch sites are draw.isOnFrame() in drawSingleMode (line 357) and drawable.isOnFrame() in prepareDrawables (line 499), both on screen-part drawables. PlotSheet is never one of them.", "SRC com/wildplot/android/rendering/PlotSheet.java:634-636, 355-357", 'SOURCE')
UNREACHABLE['PlotSheet.ticsCalcX'] = ('branch_never_taken', "Called only under if(isAutoTic) in XAxis.paint and in YGrid.paint. isAutoTic is set only by the float and int constructors. ChartBuilder builds XAxis with the double constructor (ChartBuilder.java:279) and YGrid with the double constructor (ChartBuilder.java:343, YGrid.java:91-96), so the guard is false.", "SRC com/wildplot/android/rendering/PlotSheet.java:644-655; com/wildplot/android/rendering/XAxis.java:178-179, 155-161; com/wildplot/android/rendering/YGrid.java:154-155, 91-96; com/ichi2/anki/stats/ChartBuilder.java:279, 343", 'SOURCE')
UNREACHABLE['PlotSheet.ticsCalcY'] = ('branch_never_taken', "Called only under if(isAutoTic) in YAxis.paint and in XGrid.paint. isAutoTic is set only by the float and int constructors. ChartBuilder builds YAxis with the double constructor (ChartBuilder.java:315, 317) and XGrid with the double constructor (ChartBuilder.java:342, XGrid.java:92-97), so the guard is false.", "SRC com/wildplot/android/rendering/PlotSheet.java:662-674; com/wildplot/android/rendering/YAxis.java:166-167; com/wildplot/android/rendering/XGrid.java:158-159, 92-97; com/ichi2/anki/stats/ChartBuilder.java:315, 317, 342", 'SOURCE')
UNREACHABLE['PlotSheet.toCoordinatePoint'] = ('no_trigger_in_app', "Every caller is in a class that is never constructed: FunctionDrawer_y, FunctionDrawer, ReliefDrawer, YAxisHistoGram, YAxisBarGraph, XAxisBarGraph and XAxisHistoGram. A root-wide grep for new and extends of each of these classes finds no construction and no subclass; the only ReliefDrawer hits are Javadoc text.", "SRC com/wildplot/android/rendering/PlotSheet.java:312-316; com/wildplot/android/rendering/FunctionDrawer_y.java:116-118; com/wildplot/android/rendering/FunctionDrawer.java:120-122; com/wildplot/android/rendering/ReliefDrawer.java:300-302; com/wildplot/android/rendering/YAxisHistoGram.java:104-105; com/wildplot/android/rendering/YAxisBarGraph.java:101-103; com/wildplot/android/rendering/XAxisBarGraph.java:100-101; com/wildplot/android/rendering/XAxisHistoGram.java:105-107", 'SOURCE')
UNREACHABLE['PlotSheet.xToCoordinate'] = ('no_trigger_in_app', "Callers are PlotSheet.toCoordinatePoint (reached only from classes that are never constructed, see the row above) and Integral.java:99. Integral is never constructed, so no path reaches xToCoordinate.", "SRC com/wildplot/android/rendering/PlotSheet.java:246-250, 312-316; com/wildplot/android/rendering/Integral.java:92-100", 'SOURCE')
UNREACHABLE['PlotSheet.xToCoordinateLinear'] = ('no_trigger_in_app', "Private helper. Its only caller is xToCoordinate (line 249), which is itself unreachable.", "SRC com/wildplot/android/rendering/PlotSheet.java:246-262", 'SOURCE')
# ---- sup for part 115 (2026-10-29, orchestrator, build 168): PlotSheet paths into classes never constructed (FunctionDrawer, FunctionDrawer_y, Integral, LinesPoints, PointDrawer2D, ReliefDrawer, ReliefDrawer$ReliefLegend; see sup163, sup164, sup167) and into the bar/histogram axis classes XAxisBarGraph, XAxisHistoGram, YAxisBarGraph, YAxisHistoGram, which have no construction or subclass in the java root
sup(('PlotSheet.prepareDrawables', 'FunctionDrawer.isClusterable'))
sup(('PlotSheet.prepareDrawables', 'FunctionDrawer.isCritical'))
sup(('PlotSheet.drawSingleMode', 'FunctionDrawer.isOnFrame'))
sup(('PlotSheet.prepareDrawables', 'FunctionDrawer.isOnFrame'))
sup(('PlotSheet.drawSingleMode', 'FunctionDrawer.paint'))
sup(('PlotSheet.prepareDrawables', 'FunctionDrawer_y.isClusterable'))
sup(('PlotSheet.prepareDrawables', 'FunctionDrawer_y.isCritical'))
sup(('PlotSheet.drawSingleMode', 'FunctionDrawer_y.isOnFrame'))
sup(('PlotSheet.prepareDrawables', 'FunctionDrawer_y.isOnFrame'))
sup(('PlotSheet.drawSingleMode', 'FunctionDrawer_y.paint'))
sup(('PlotSheet.prepareDrawables', 'Integral.isClusterable'))
sup(('PlotSheet.prepareDrawables', 'Integral.isCritical'))
sup(('PlotSheet.drawSingleMode', 'Integral.isOnFrame'))
sup(('PlotSheet.prepareDrawables', 'Integral.isOnFrame'))
sup(('PlotSheet.drawSingleMode', 'Integral.paint'))
sup(('PlotSheet.prepareDrawables', 'LinesPoints.isClusterable'))
sup(('PlotSheet.prepareDrawables', 'LinesPoints.isCritical'))
sup(('PlotSheet.drawSingleMode', 'LinesPoints.isOnFrame'))
sup(('PlotSheet.prepareDrawables', 'LinesPoints.isOnFrame'))
sup(('PlotSheet.drawSingleMode', 'LinesPoints.paint'))
sup(('PlotSheet.prepareDrawables', 'PointDrawer2D.isClusterable'))
sup(('PlotSheet.prepareDrawables', 'PointDrawer2D.isCritical'))
sup(('PlotSheet.drawSingleMode', 'PointDrawer2D.isOnFrame'))
sup(('PlotSheet.prepareDrawables', 'PointDrawer2D.isOnFrame'))
sup(('PlotSheet.drawSingleMode', 'PointDrawer2D.paint'))
sup(('PlotSheet.prepareDrawables', 'ReliefDrawer.isClusterable'))
sup(('PlotSheet.prepareDrawables', 'ReliefDrawer.isCritical'))
sup(('PlotSheet.drawSingleMode', 'ReliefDrawer.isOnFrame'))
sup(('PlotSheet.prepareDrawables', 'ReliefDrawer.isOnFrame'))
sup(('PlotSheet.drawSingleMode', 'ReliefDrawer.paint'))
sup(('PlotSheet.prepareDrawables', 'ReliefDrawer$ReliefLegend.isClusterable'))
sup(('PlotSheet.prepareDrawables', 'ReliefDrawer$ReliefLegend.isCritical'))
sup(('PlotSheet.drawSingleMode', 'ReliefDrawer$ReliefLegend.isOnFrame'))
sup(('PlotSheet.prepareDrawables', 'ReliefDrawer$ReliefLegend.isOnFrame'))
sup(('PlotSheet.drawSingleMode', 'ReliefDrawer$ReliefLegend.paint'))
# ---- PlotSheet dispatch: LegendDrawable.isClusterable and isOnFrame return false, so the clusterable branch that calls its isCritical is never taken (LegendDrawable.java:38-41, 48-51); DrawableContainer.isClusterable runs only on a second prepare pass, which needs addDrawable after the first pass, and every addDrawable call is in the ChartBuilder setup chain before painting; no PlotSheet is ever added to a drawable list
sup(('PlotSheet.prepareDrawables', 'LegendDrawable.isCritical'))
sup(('PlotSheet.prepareDrawables', 'DrawableContainer.isClusterable'))
sup(('PlotSheet.prepareDrawables', 'PlotSheet.isClusterable'))
sup(('PlotSheet.prepareDrawables', 'PlotSheet.isCritical'))
sup(('PlotSheet.drawSingleMode', 'PlotSheet.isOnFrame'))
sup(('PlotSheet.prepareDrawables', 'PlotSheet.isOnFrame'))
# ---- dead branches in PlotSheet, verified in source: isMultiMode is never true (PlotSheet.java:60); isAutoTic is set only by the float and int constructors of XAxis, YAxis, XGrid and YGrid, and ChartBuilder uses the double constructors (ChartBuilder.java:279, 315, 317, 342, 343); setLogX and setLogY have no caller (PlotSheet.java:692-704)
sup(('PlotSheet.paint', 'PlotSheet.drawMultiMode'))
sup(('XAxis.paint', 'PlotSheet.ticsCalcX'))
sup(('YGrid.paint', 'PlotSheet.ticsCalcX'))
sup(('XGrid.paint', 'PlotSheet.ticsCalcY'))
sup(('YAxis.paint', 'PlotSheet.ticsCalcY'))
sup(('PlotSheet.xToGraphic', 'PlotSheet.xToGraphicLog'))
sup(('PlotSheet.yToGraphic', 'PlotSheet.yToGraphicLog'))
# ---- PlotSheet multi-screen and constructor paths with only UNREACHABLE callers (PlotSheet 5-argument constructor, updateX, updateY, setxRange, setyRange, DrawableContainer.abortAndReset)
sup(('PlotSheet.<init>(double,double,double,double,Vector)', 'MultiScreenPart.<init>(double[],double[],Vector)'))
sup(('PlotSheet.updateX', 'MultiScreenPart.setxRange'))
sup(('PlotSheet.setxRange', 'MultiScreenPart.setxRange'))
sup(('PlotSheet.updateY', 'MultiScreenPart.setyRange'))
sup(('PlotSheet.setyRange', 'MultiScreenPart.setyRange'))
sup(('DrawableContainer.abortAndReset', 'PlotSheet.abortAndReset'))
# ---- coordinate conversion chain: toCoordinatePoint is called only from classes never constructed (see the list above); xToCoordinate and yToCoordinate are reached only through toCoordinatePoint or Integral.paint
sup(('FunctionDrawer.getMaxValue', 'PlotSheet.toCoordinatePoint'))
sup(('FunctionDrawer.paint', 'PlotSheet.toCoordinatePoint'))
sup(('FunctionDrawer_y.getMaxValue', 'PlotSheet.toCoordinatePoint'))
sup(('FunctionDrawer_y.paint', 'PlotSheet.toCoordinatePoint'))
sup(('ReliefDrawer$DepthSearcher.run', 'PlotSheet.toCoordinatePoint'))
sup(('ReliefDrawer$PartRenderer.run', 'PlotSheet.toCoordinatePoint'))
sup(('ReliefDrawer.drawBorders', 'PlotSheet.toCoordinatePoint'))
sup(('ReliefDrawer.scanDepth', 'PlotSheet.toCoordinatePoint'))
sup(('XAxisBarGraph.paint', 'PlotSheet.toCoordinatePoint'))
sup(('XAxisHistoGram.paint', 'PlotSheet.toCoordinatePoint'))
sup(('YAxisBarGraph.paint', 'PlotSheet.toCoordinatePoint'))
sup(('YAxisHistoGram.paint', 'PlotSheet.toCoordinatePoint'))
sup(('Integral.paint', 'PlotSheet.xToCoordinate'))
sup(('PlotSheet.toCoordinatePoint', 'PlotSheet.xToCoordinate'))
sup(('PlotSheet.xToCoordinate', 'PlotSheet.xToCoordinateLinear'))
sup(('PlotSheet.xToCoordinate', 'PlotSheet.xToCoordinateLog'))
sup(('PlotSheet.toCoordinatePoint', 'PlotSheet.yToCoordinate'))
sup(('PlotSheet.yToCoordinate', 'PlotSheet.yToCoordinateLinear'))
sup(('PlotSheet.yToCoordinate', 'PlotSheet.yToCoordinateLog'))

# ---- part 120 (2026-10-29)
UNREACHABLE['XAxisBarGraph.<init>'] = ('no_trigger_in_app', "No new XAxisBarGraph in the source root; ChartBuilder builds a BarGraph instead (lines 240-245). Class is never constructed.", "com/wildplot/android/rendering/XAxisBarGraph.java:29, 61-67; com/ichi2/anki/stats/ChartBuilder.java:240-245", 'SOURCE')
UNREACHABLE['XAxisBarGraph.abortAndReset'] = ('no_trigger_in_app', "Empty Drawable override. Only caller is the cha dispatch in DrawableContainer.abortAndReset (line 62), which has no caller in the source root; no XAxisBarGraph is ever created.", "com/wildplot/android/rendering/XAxisBarGraph.java:226-230; com/wildplot/android/rendering/DrawableContainer.java:58-63", 'SOURCE')
UNREACHABLE['XAxisBarGraph.drawBar(double,double,GraphicsWrap,RectangleWrap)'] = ('no_trigger_in_app', "Private. Only caller in the class is paint (line 118), which runs only on an XAxisBarGraph instance; none is ever created.", "com/wildplot/android/rendering/XAxisBarGraph.java:118, 132-134", 'SOURCE')
UNREACHABLE['XAxisBarGraph.drawBar(double,double,GraphicsWrap,RectangleWrap,double)'] = ('no_trigger_in_app', "Private. Callers are paint (line 116) and the 4-argument drawBar (line 133); both need an XAxisBarGraph instance, and none is ever created.", "com/wildplot/android/rendering/XAxisBarGraph.java:116, 133, 144-184", 'SOURCE')
UNREACHABLE['XAxisBarGraph.getExtraScaleFactor'] = ('no_trigger_in_app', "Getter with no call anywhere in the source root; no XAxisBarGraph is ever created.", "com/wildplot/android/rendering/XAxisBarGraph.java:218-220", 'SOURCE')
UNREACHABLE['XAxisBarGraph.isClusterable'] = ('no_trigger_in_app', "Drawable override returning true. Reached only by dispatch in PlotSheet.prepareDrawables (line 519) on added drawables; no XAxisBarGraph is ever added. The cha edge has no instance behind it.", "com/wildplot/android/rendering/XAxisBarGraph.java:231-234; com/wildplot/android/rendering/PlotSheet.java:519", 'SOURCE')
UNREACHABLE['XAxisBarGraph.isCritical'] = ('no_trigger_in_app', "Drawable override returning false. Reached only by dispatch in PlotSheet.prepareDrawables (line 526); no XAxisBarGraph is ever added. The cha edge has no instance behind it.", "com/wildplot/android/rendering/XAxisBarGraph.java:236-239; com/wildplot/android/rendering/PlotSheet.java:526", 'SOURCE')
UNREACHABLE['XAxisBarGraph.isOnFrame'] = ('no_trigger_in_app', "Getter. Reached only by dispatch in PlotSheet.drawSingleMode (line 357; batch 115, not yet labelled) and PlotSheet.prepareDrawables (line 499); no XAxisBarGraph is ever added.", "com/wildplot/android/rendering/XAxisBarGraph.java:207-209; com/wildplot/android/rendering/PlotSheet.java:357, 499", 'SOURCE')
UNREACHABLE['XAxisBarGraph.paint'] = ('no_trigger_in_app', "Drawable override. Reached only by dispatch in DrawableContainer.paint (line 49) and PlotSheet.drawSingleMode (line 473; batch 115, not yet labelled, reached via PlotSheet.paint lines 322-329). No XAxisBarGraph is ever added to a drawable list.", "com/wildplot/android/rendering/XAxisBarGraph.java:91-123; com/wildplot/android/rendering/DrawableContainer.java:41-51; com/wildplot/android/rendering/PlotSheet.java:322-329, 473; com/ichi2/anki/stats/ChartView.java:69-70", 'SOURCE')
UNREACHABLE['XAxisBarGraph.setAutoscale'] = ('no_trigger_in_app', "No-argument setter with no call anywhere in the source root; no XAxisBarGraph is ever created.", "com/wildplot/android/rendering/XAxisBarGraph.java:211-213", 'SOURCE')
UNREACHABLE['XAxisBarGraph.setExtraScaleFactor'] = ('no_trigger_in_app', "Setter with no call anywhere in the source root; no XAxisBarGraph is ever created.", "com/wildplot/android/rendering/XAxisBarGraph.java:222-224", 'SOURCE')
UNREACHABLE['XAxisBarGraph.setFillColor'] = ('no_trigger_in_app', "No call on an XAxisBarGraph; the only setFillColor calls are on a BarGraph (ChartBuilder lines 240, 244). No XAxisBarGraph is ever created.", "com/wildplot/android/rendering/XAxisBarGraph.java:84-86; com/ichi2/anki/stats/ChartBuilder.java:240, 244", 'SOURCE')
UNREACHABLE['XAxisBarGraph.setFilling'] = ('no_trigger_in_app', "No call on an XAxisBarGraph; the only setFilling call is on a BarGraph (ChartBuilder lines 240-241). No XAxisBarGraph is ever created.", "com/wildplot/android/rendering/XAxisBarGraph.java:73-78; com/ichi2/anki/stats/ChartBuilder.java:240-241", 'SOURCE')
UNREACHABLE['XAxisBarGraph.setOnFrame()'] = ('no_trigger_in_app', "Calls setOnFrame(0) (line 201). Callers in the source root are ChartBuilder lines 280 (XAxis) and 327 (YAxis), not this class; no XAxisBarGraph is ever created.", "com/wildplot/android/rendering/XAxisBarGraph.java:200-202; com/ichi2/anki/stats/ChartBuilder.java:279-280, 327", 'SOURCE')
UNREACHABLE['XAxisBarGraph.setOnFrame(double)'] = ('no_trigger_in_app', "Called only by setOnFrame() (line 201), which has no call on an XAxisBarGraph; none is ever created.", "com/wildplot/android/rendering/XAxisBarGraph.java:195-198, 201", 'SOURCE')
UNREACHABLE['XAxisBarGraph.unsetAutoscale'] = ('no_trigger_in_app', "No call anywhere in the source root; no XAxisBarGraph is ever created.", "com/wildplot/android/rendering/XAxisBarGraph.java:214-216", 'SOURCE')
UNREACHABLE['XAxisBarGraph.unsetOnFrame'] = ('no_trigger_in_app', "No call anywhere in the source root; no XAxisBarGraph is ever created.", "com/wildplot/android/rendering/XAxisBarGraph.java:190-193", 'SOURCE')
UNREACHABLE['XAxisHistoGram.<init>'] = ('no_trigger_in_app', "No new XAxisHistoGram in the source root; ChartBuilder builds a BarGraph instead (lines 240-245). Class is never constructed.", "com/wildplot/android/rendering/XAxisHistoGram.java:29, 66-73; com/ichi2/anki/stats/ChartBuilder.java:240-245", 'SOURCE')
UNREACHABLE['XAxisHistoGram.abortAndReset'] = ('no_trigger_in_app', "Drawable override that sets isOnReset (line 280). Only caller is the cha dispatch in DrawableContainer.abortAndReset (line 62), which has no caller in the source root; no XAxisHistoGram is ever created.", "com/wildplot/android/rendering/XAxisHistoGram.java:278-282; com/wildplot/android/rendering/DrawableContainer.java:58-63", 'SOURCE')
UNREACHABLE['XAxisHistoGram.drawBar(double,double,GraphicsWrap,RectangleWrap)'] = ('no_trigger_in_app', "Private. Only caller is paint (line 131), which runs only on an XAxisHistoGram instance; none is ever created.", "com/wildplot/android/rendering/XAxisHistoGram.java:131, 162-164", 'SOURCE')
UNREACHABLE['XAxisHistoGram.drawBar(double,double,GraphicsWrap,RectangleWrap,double)'] = ('no_trigger_in_app', "Private. Only caller is the 4-argument drawBar (line 163), reached only from paint (line 131); none is ever created.", "com/wildplot/android/rendering/XAxisHistoGram.java:163, 174-214", 'SOURCE')
UNREACHABLE['XAxisHistoGram.getExtraScaleFactor'] = ('no_trigger_in_app', "Getter with no call anywhere in the source root; no XAxisHistoGram is ever created.", "com/wildplot/android/rendering/XAxisHistoGram.java:270-272", 'SOURCE')
UNREACHABLE['XAxisHistoGram.getMaxValue'] = ('no_trigger_in_app', "Public method with no call anywhere in the source root (no unqualified call in the file either); no XAxisHistoGram is ever created.", "com/wildplot/android/rendering/XAxisHistoGram.java:138-153", 'SOURCE')
UNREACHABLE['XAxisHistoGram.getSizeInRange'] = ('no_trigger_in_app', "Private. Called only from paint (line 129) and getMaxValue (line 146); both need an XAxisHistoGram instance, and none is ever created.", "com/wildplot/android/rendering/XAxisHistoGram.java:129, 146, 224-236", 'SOURCE')
UNREACHABLE['XAxisHistoGram.isClusterable'] = ('no_trigger_in_app', "Drawable override returning true. Reached only by dispatch in PlotSheet.prepareDrawables (line 519) on added drawables; no XAxisHistoGram is ever added. The cha edge has no instance behind it.", "com/wildplot/android/rendering/XAxisHistoGram.java:283-286; com/wildplot/android/rendering/PlotSheet.java:519", 'SOURCE')
UNREACHABLE['XAxisHistoGram.isCritical'] = ('no_trigger_in_app', "Drawable override returning false. Reached only by dispatch in PlotSheet.prepareDrawables (line 526); no XAxisHistoGram is ever added. The cha edge has no instance behind it.", "com/wildplot/android/rendering/XAxisHistoGram.java:288-291; com/wildplot/android/rendering/PlotSheet.java:526", 'SOURCE')
UNREACHABLE['XAxisHistoGram.isOnFrame'] = ('no_trigger_in_app', "Getter. Reached only by dispatch in PlotSheet.drawSingleMode (line 357; batch 115, not yet labelled) and PlotSheet.prepareDrawables (line 499); no XAxisHistoGram is ever added.", "com/wildplot/android/rendering/XAxisHistoGram.java:258-260; com/wildplot/android/rendering/PlotSheet.java:357, 499", 'SOURCE')
UNREACHABLE['XAxisHistoGram.paint'] = ('no_trigger_in_app', "Drawable override. Reached only by dispatch in DrawableContainer.paint (line 49) and PlotSheet.drawSingleMode (line 473; batch 115, not yet labelled, reached via PlotSheet.paint lines 322-329). Local isOnReset (line 99) hides the field, so the return at lines 127-128 never runs.", "com/wildplot/android/rendering/XAxisHistoGram.java:97-136; com/wildplot/android/rendering/DrawableContainer.java:41-51; com/wildplot/android/rendering/PlotSheet.java:322-329, 473; com/ichi2/anki/stats/ChartView.java:69-70", 'SOURCE')
UNREACHABLE['XAxisHistoGram.setAutoscale'] = ('no_trigger_in_app', "Setter with no call anywhere in the source root; no XAxisHistoGram is ever created.", "com/wildplot/android/rendering/XAxisHistoGram.java:262-265", 'SOURCE')
UNREACHABLE['XAxisHistoGram.setExtraScaleFactor'] = ('no_trigger_in_app', "Setter with no call anywhere in the source root; no XAxisHistoGram is ever created.", "com/wildplot/android/rendering/XAxisHistoGram.java:274-276", 'SOURCE')
UNREACHABLE['XAxisHistoGram.setFillColor'] = ('no_trigger_in_app', "No call on an XAxisHistoGram; the only setFillColor calls are on a BarGraph (ChartBuilder lines 240, 244). No XAxisHistoGram is ever created.", "com/wildplot/android/rendering/XAxisHistoGram.java:90-92; com/ichi2/anki/stats/ChartBuilder.java:240, 244", 'SOURCE')
UNREACHABLE['XAxisHistoGram.setFilling'] = ('no_trigger_in_app', "No call on an XAxisHistoGram; the only setFilling call is on a BarGraph (ChartBuilder lines 240-241). No XAxisHistoGram is ever created.", "com/wildplot/android/rendering/XAxisHistoGram.java:79-84; com/ichi2/anki/stats/ChartBuilder.java:240-241", 'SOURCE')
UNREACHABLE['XAxisHistoGram.setOnFrame()'] = ('no_trigger_in_app', "Calls setOnFrame(0) (line 252). Callers in the source root are ChartBuilder lines 280 (XAxis) and 327 (YAxis), not this class; no XAxisHistoGram is ever created.", "com/wildplot/android/rendering/XAxisHistoGram.java:251-253; com/ichi2/anki/stats/ChartBuilder.java:279-280, 327", 'SOURCE')
UNREACHABLE['XAxisHistoGram.setOnFrame(double)'] = ('no_trigger_in_app', "Called only by setOnFrame() (line 252), which has no call on an XAxisHistoGram; none is ever created.", "com/wildplot/android/rendering/XAxisHistoGram.java:246-249, 252", 'SOURCE')
UNREACHABLE['XAxisHistoGram.unsetAutoscale'] = ('no_trigger_in_app', "No call anywhere in the source root; no XAxisHistoGram is ever created.", "com/wildplot/android/rendering/XAxisHistoGram.java:266-268", 'SOURCE')
UNREACHABLE['XAxisHistoGram.unsetOnFrame'] = ('no_trigger_in_app', "No call anywhere in the source root; no XAxisHistoGram is ever created.", "com/wildplot/android/rendering/XAxisHistoGram.java:241-244", 'SOURCE')

# ---- sup for part 120 (2026-10-29)
sup(
    ('DrawableContainer.abortAndReset', 'XAxisBarGraph.abortAndReset'),
    ('XAxisBarGraph.paint', 'XAxisBarGraph.drawBar(double,double,GraphicsWrap,RectangleWrap)'),
    ('XAxisBarGraph.paint', 'XAxisBarGraph.drawBar(double,double,GraphicsWrap,RectangleWrap,double)'),
    ('XAxisBarGraph.drawBar(double,double,GraphicsWrap,RectangleWrap)', 'XAxisBarGraph.drawBar(double,double,GraphicsWrap,RectangleWrap,double)'),
    ('PlotSheet.prepareDrawables', 'XAxisBarGraph.isClusterable'),
    ('PlotSheet.prepareDrawables', 'XAxisBarGraph.isCritical'),
    ('PlotSheet.drawSingleMode', 'XAxisBarGraph.isOnFrame'),
    ('PlotSheet.prepareDrawables', 'XAxisBarGraph.isOnFrame'),
    ('DrawableContainer.paint', 'XAxisBarGraph.paint'),
    ('PlotSheet.drawSingleMode', 'XAxisBarGraph.paint'),
    ('XAxisBarGraph.setOnFrame()', 'XAxisBarGraph.setOnFrame(double)'),
    ('DrawableContainer.abortAndReset', 'XAxisHistoGram.abortAndReset'),
    ('XAxisHistoGram.paint', 'XAxisHistoGram.drawBar(double,double,GraphicsWrap,RectangleWrap)'),
    ('XAxisHistoGram.drawBar(double,double,GraphicsWrap,RectangleWrap)', 'XAxisHistoGram.drawBar(double,double,GraphicsWrap,RectangleWrap,double)'),
    ('XAxisHistoGram.paint', 'XAxisHistoGram.getSizeInRange'),
    ('XAxisHistoGram.getMaxValue', 'XAxisHistoGram.getSizeInRange'),
    ('PlotSheet.prepareDrawables', 'XAxisHistoGram.isClusterable'),
    ('PlotSheet.prepareDrawables', 'XAxisHistoGram.isCritical'),
    ('PlotSheet.drawSingleMode', 'XAxisHistoGram.isOnFrame'),
    ('PlotSheet.prepareDrawables', 'XAxisHistoGram.isOnFrame'),
    ('DrawableContainer.paint', 'XAxisHistoGram.paint'),
    ('PlotSheet.drawSingleMode', 'XAxisHistoGram.paint'),
    ('XAxisHistoGram.setOnFrame()', 'XAxisHistoGram.setOnFrame(double)'),
)

# ---- part 121 (2026-10-29)
UNREACHABLE['XGrid.<init>(PlotSheet,double,int)'] = ('no_trigger_in_app', "No new XGrid(PlotSheet,double,int) anywhere in the source root. The only creation site, ChartBuilder.setupGrid line 342, passes the double yTicks as the third argument, so the (PlotSheet,double,double) overload is chosen and this int overload is never selected.", "com/wildplot/android/rendering/XGrid.java:117-123; com/ichi2/anki/stats/ChartBuilder.java:335, 342", 'SOURCE')
UNREACHABLE['XGrid.<init>(ColorWrap,PlotSheet,double,double)'] = ('no_trigger_in_app', "No new XGrid with a ColorWrap first argument anywhere in the source root. The only creation site, ChartBuilder.java:342, uses the 3-argument form, so this 4-argument overload is never selected.", "com/wildplot/android/rendering/XGrid.java:105-111; com/ichi2/anki/stats/ChartBuilder.java:342", 'SOURCE')
UNREACHABLE['XGrid.<init>(ColorWrap,PlotSheet,double,int)'] = ('no_trigger_in_app', "No new XGrid with a ColorWrap first argument and an int pixel distance anywhere in the source root. The only creation site, ChartBuilder.java:342, uses the 3-argument double form, so this overload is never selected.", "com/wildplot/android/rendering/XGrid.java:130-137; com/ichi2/anki/stats/ChartBuilder.java:342", 'SOURCE')
UNREACHABLE['XGrid.abortAndReset'] = ('no_trigger_in_app', "Empty Drawable override. Its only caller is the cha dispatch in DrawableContainer.abortAndReset (line 62), and DrawableContainer.abortAndReset has no caller in the source root (grep for abortAndReset() finds only its definition). PlotSheet.abortAndReset (line 711) is also empty and has no caller, so the dispatch never runs.", "com/wildplot/android/rendering/XGrid.java:237-241; com/wildplot/android/rendering/DrawableContainer.java:58-63; com/wildplot/android/rendering/PlotSheet.java:711-714", 'SOURCE')
UNREACHABLE['XGrid.setGridOnDownside'] = ('no_trigger_in_app', "Setter with no call anywhere in the source root (grep for setGridOnDownside finds only the definition). The field keeps its default true (line 79).", "com/wildplot/android/rendering/XGrid.java:218-220, 79", 'SOURCE')
UNREACHABLE['XGrid.setGridOnRight'] = ('no_trigger_in_app', "Setter with no call anywhere in the source root (grep for setGridOnRight finds only the definition). The field keeps its default true (line 74).", "com/wildplot/android/rendering/XGrid.java:211-213, 74", 'SOURCE')
UNREACHABLE['XGrid.setGridOnUpside'] = ('no_trigger_in_app', "Setter with no call anywhere in the source root (grep for setGridOnUpside finds only the definition). The field keeps its default true (line 84).", "com/wildplot/android/rendering/XGrid.java:225-227, 84", 'SOURCE')
UNREACHABLE['XGrid.setGridkOnLeft'] = ('no_trigger_in_app', "Setter with no call anywhere in the source root (grep for setGridkOnLeft finds only the definition). The field keeps its default true (line 69).", "com/wildplot/android/rendering/XGrid.java:204-206, 69", 'SOURCE')

# ---- sup for part 121 (2026-10-29, orchestrator, build 170): DrawableContainer.abortAndReset has no caller (DrawableContainer.java:59-63), so its automatic CHA edge into XGrid.abortAndReset cannot fire
sup(('DrawableContainer.abortAndReset','XGrid.abortAndReset'))

# ---- part 122 (2026-10-29)
UNREACHABLE['YAxis.<init>(PlotSheet,double,float,float)'] = ('no_trigger_in_app', "Overload is never selected. The only construction sites are ChartBuilder.setupYaxis (lines 315 and 317), which pass a double yTicks and a double yTicks/2.0 with an int 0. Double to float is a narrowing conversion, so this (PlotSheet,double,float,float) constructor is not applicable. No other 'new YAxis(' exists in the source root.", "com/wildplot/android/rendering/YAxis.java:144-150; com/ichi2/anki/stats/ChartBuilder.java:311-312, 315, 317", 'SOURCE')
UNREACHABLE['YAxis.abortAndReset'] = ('no_trigger_in_app', "Only call site is DrawableContainer.abortAndReset (line 62). DrawableContainer.abortAndReset (line 59) has no caller in the source root, and PlotSheet.abortAndReset (line 711, empty body) has no caller either. The auto cha edge DrawableContainer.abortAndReset -> YAxis.abortAndReset is listed in the batch note, not suppressed.", "com/wildplot/android/rendering/YAxis.java:549-553; com/wildplot/android/rendering/DrawableContainer.java:59-63; com/wildplot/android/rendering/PlotSheet.java:711-714", 'SOURCE')
UNREACHABLE['YAxis.getxOffset'] = ('no_trigger_in_app', "Getter with no caller in the source root. A grep for '.getxOffset(' and for unqualified calls inside YAxis.java finds only the definition.", "com/wildplot/android/rendering/YAxis.java:380-382", 'SOURCE')
UNREACHABLE['YAxis.setIntersectionOffset'] = ('no_trigger_in_app', "Setter with no caller in the source root and no in-file call (grep).", "com/wildplot/android/rendering/YAxis.java:403-405", 'SOURCE')
UNREACHABLE['YAxis.setLog'] = ('no_trigger_in_app', "Setter with no caller in the source root and no in-file call (grep). isLog keeps its default false (field declaration line 40), so the log branches in drawMarkers and drawMinorMarkers are never taken.", "com/wildplot/android/rendering/YAxis.java:40, 202, 463, 541-543", 'SOURCE')
UNREACHABLE['YAxis.setxOffset'] = ('no_trigger_in_app', "Setter with no caller in the source root and no in-file call (grep). setOnFrame and setOnRightSideFrame set xOffset directly and do not call this setter.", "com/wildplot/android/rendering/YAxis.java:388-390, 410-414, 427-432", 'SOURCE')
UNREACHABLE['YAxis.unsetHasNumbersRotated'] = ('no_trigger_in_app', "Setter with no caller in the source root and no in-file call (grep). ChartBuilder.setupYaxis only calls setHasNumbersRotated (line 330).", "com/wildplot/android/rendering/YAxis.java:567-569; com/ichi2/anki/stats/ChartBuilder.java:330", 'SOURCE')
UNREACHABLE['YAxis.unsetLog'] = ('no_trigger_in_app', "Setter with no caller in the source root and no in-file call (grep). setLog is never called either, so isLog stays at its default false.", "com/wildplot/android/rendering/YAxis.java:40, 545-547", 'SOURCE')
UNREACHABLE['YAxis.unsetOnFrame'] = ('no_trigger_in_app', "Setter with no caller in the source root and no in-file call (grep). The same-named methods in YAxisBarGraph and YAxisHistoGram belong to YAxisBarGraph and YAxisHistoGram, which have no extends clause (grep) and so are not YAxis subclasses; they do not reach this one.", "com/wildplot/android/rendering/YAxis.java:419-425; com/wildplot/android/rendering/YAxisBarGraph.java:63, 199; com/wildplot/android/rendering/YAxisHistoGram.java:65, 240", 'SOURCE')
UNREACHABLE['YAxis.unsetxOffset'] = ('no_trigger_in_app', "Setter with no caller in the source root and no in-file call (grep).", "com/wildplot/android/rendering/YAxis.java:395-397", 'SOURCE')

# ---- sup for part 122 (2026-10-29, orchestrator, build 171): DrawableContainer.abortAndReset has no caller (DrawableContainer.java:59-63), so its automatic CHA edge into YAxis.abortAndReset cannot fire
sup(('DrawableContainer.abortAndReset','YAxis.abortAndReset'))

# ---- part 123 (2026-10-29)
# AnkiDroid batch 123 (LABEL helper): com/wildplot/android/rendering/YAxisBarGraph and YAxisHistoGram, 36 methods.
# Full rows are in graphs/AnkiDroid/parts/label_123.md. No e() edges: no method has a route from an entry point.
UNREACHABLE['YAxisBarGraph.<init>'] = ('no_trigger_in_app', "grep -rn 'new YAxisBarGraph' over the source root finds nothing; the class name occurs only in YAxisBarGraph.java (lines 29, 62), so the constructor never runs and no instance exists. The chart builder creates a BarGraph instead (line 240).", "com/wildplot/android/rendering/YAxisBarGraph.java:29, 62-69; com/ichi2/anki/stats/ChartBuilder.java:240", 'SOURCE')
UNREACHABLE['YAxisBarGraph.abortAndReset'] = ('no_trigger_in_app', "Drawable override with an empty body. The only dispatch site is DrawableContainer.abortAndReset line 62; grep -rn 'abortAndReset' finds no call other than that one, so DrawableContainer.abortAndReset has no caller. No YAxisBarGraph instance is ever created (grep 'YAxisBarGraph' finds only its own file).", "com/wildplot/android/rendering/YAxisBarGraph.java:235-239; com/wildplot/android/rendering/DrawableContainer.java:58-63", 'SOURCE')
UNREACHABLE['YAxisBarGraph.drawBar(double,double,GraphicsWrap,RectangleWrap)'] = ('no_trigger_in_app', "Private 4-argument drawBar. Its only caller is paint (line 126); grep 'drawBar(' in the file finds lines 124, 126, 139, 140, 151. paint runs only on an instance, and none is ever created.", "com/wildplot/android/rendering/YAxisBarGraph.java:126, 139-141", 'SOURCE')
UNREACHABLE['YAxisBarGraph.drawBar(double,double,GraphicsWrap,RectangleWrap,double)'] = ('no_trigger_in_app', "Private 5-argument drawBar. Its callers in the file are paint (line 124) and the 4-argument drawBar (line 140); both need an instance, and none is ever created.", "com/wildplot/android/rendering/YAxisBarGraph.java:124, 140, 151-193", 'SOURCE')
UNREACHABLE['YAxisBarGraph.getExtraScaleFactor'] = ('no_trigger_in_app', "Getter. grep -rn 'getExtraScaleFactor' over the source root finds only declarations (no call); paint reads the field directly (lines 124, 126). No YAxisBarGraph instance is ever created.", "com/wildplot/android/rendering/YAxisBarGraph.java:124, 126, 227-229", 'SOURCE')
UNREACHABLE['YAxisBarGraph.isClusterable'] = ('no_trigger_in_app', "Drawable override returning true. Dispatch site: PlotSheet.prepareDrawables line 519, in the loop over the screen drawables (line 493). A YAxisBarGraph would have to be added to a drawable list, and grep 'YAxisBarGraph' finds no construction or add.", "com/wildplot/android/rendering/YAxisBarGraph.java:241-244; com/wildplot/android/rendering/PlotSheet.java:482, 493, 519", 'SOURCE')
UNREACHABLE['YAxisBarGraph.isCritical'] = ('no_trigger_in_app', "Drawable override returning false. Dispatch site: PlotSheet.prepareDrawables line 526 (loop at line 493). No YAxisBarGraph is ever constructed or added (grep 'YAxisBarGraph' finds only its own file).", "com/wildplot/android/rendering/YAxisBarGraph.java:246-249; com/wildplot/android/rendering/PlotSheet.java:493, 526", 'SOURCE')
UNREACHABLE['YAxisBarGraph.isOnFrame'] = ('no_trigger_in_app', "Getter returning true. Dispatch sites: PlotSheet.drawSingleMode line 357 (drawSingleMode starts at line 335) and PlotSheet.prepareDrawables line 499. No YAxisBarGraph is ever constructed or added (grep 'YAxisBarGraph' finds only its own file).", "com/wildplot/android/rendering/YAxisBarGraph.java:216-218; com/wildplot/android/rendering/PlotSheet.java:335, 357, 499", 'SOURCE')
UNREACHABLE['YAxisBarGraph.paint'] = ('no_trigger_in_app', "Drawable override. Dispatch sites: DrawableContainer.paint line 49, and PlotSheet.drawSingleMode lines 366 and 473. The screen route is ChartView.onDraw lines 69-70, then PlotSheet.paint lines 322-329, then drawSingleMode. It ends at a missing instance: no YAxisBarGraph is ever constructed or added (grep 'YAxisBarGraph' finds only its own file).", "com/wildplot/android/rendering/YAxisBarGraph.java:94-130; com/wildplot/android/rendering/DrawableContainer.java:41-51; com/wildplot/android/rendering/PlotSheet.java:322-329, 335, 366, 473; com/ichi2/anki/stats/ChartView.java:57, 69-70", 'SOURCE')
UNREACHABLE['YAxisBarGraph.setAutoscale'] = ('no_trigger_in_app', "No-argument setter. grep -rn 'setAutoscale' over the source root finds only declarations (no call); no YAxisBarGraph instance is ever created.", "com/wildplot/android/rendering/YAxisBarGraph.java:220-222", 'SOURCE')
UNREACHABLE['YAxisBarGraph.setExtraScaleFactor'] = ('no_trigger_in_app', "Setter. grep -rn 'setExtraScaleFactor' finds only declarations (no call); no YAxisBarGraph instance is ever created.", "com/wildplot/android/rendering/YAxisBarGraph.java:231-233", 'SOURCE')
UNREACHABLE['YAxisBarGraph.setFillColor'] = ('no_trigger_in_app', "Setter. The only setFillColor call in the source root is on a BarGraph (ChartBuilder line 244; barGraph is a new BarGraph at line 240), not on this class. No YAxisBarGraph instance is ever created.", "com/wildplot/android/rendering/YAxisBarGraph.java:86-88; com/ichi2/anki/stats/ChartBuilder.java:240, 244", 'SOURCE')
UNREACHABLE['YAxisBarGraph.setFilling'] = ('no_trigger_in_app', "Setter. The only setFilling call in the source root is ChartBuilder line 241, on a BarGraph (line 240). No YAxisBarGraph instance is ever created.", "com/wildplot/android/rendering/YAxisBarGraph.java:75-80; com/ichi2/anki/stats/ChartBuilder.java:240-241", 'SOURCE')
UNREACHABLE['YAxisBarGraph.setOnFrame()'] = ('no_trigger_in_app', "Calls setOnFrame(0) (line 210). Its callers in the source root are ChartBuilder line 280, on an XAxis (line 279), and line 327, on a YAxis (declared at line 313). Neither receiver is a YAxisBarGraph, and none is ever created.", "com/wildplot/android/rendering/YAxisBarGraph.java:209-211; com/ichi2/anki/stats/ChartBuilder.java:279-280, 313-317, 327", 'SOURCE')
UNREACHABLE['YAxisBarGraph.setOnFrame(double)'] = ('no_trigger_in_app', "Called only from setOnFrame() (line 210), which has no caller on a YAxisBarGraph. No instance is ever created.", "com/wildplot/android/rendering/YAxisBarGraph.java:204-207, 210", 'SOURCE')
UNREACHABLE['YAxisBarGraph.unsetAutoscale'] = ('no_trigger_in_app', "grep -rn 'unsetAutoscale' over the source root finds only declarations (no call); no YAxisBarGraph instance is ever created.", "com/wildplot/android/rendering/YAxisBarGraph.java:223-225", 'SOURCE')
UNREACHABLE['YAxisBarGraph.unsetOnFrame'] = ('no_trigger_in_app', "grep -rn 'unsetOnFrame' over the source root finds only declarations (no call); no YAxisBarGraph instance is ever created.", "com/wildplot/android/rendering/YAxisBarGraph.java:199-202", 'SOURCE')
UNREACHABLE['YAxisHistoGram.<init>'] = ('no_trigger_in_app', "grep -rn 'new YAxisHistoGram' over the source root finds nothing; the class name occurs only in YAxisHistoGram.java (lines 29, 64), so the constructor never runs and no instance exists.", "com/wildplot/android/rendering/YAxisHistoGram.java:29, 64-71", 'SOURCE')
UNREACHABLE['YAxisHistoGram.abortAndReset'] = ('no_trigger_in_app', "Drawable override that sets isOnReset (line 279). The only dispatch site is DrawableContainer.abortAndReset line 62, and nothing calls that method. No YAxisHistoGram instance is ever created.", "com/wildplot/android/rendering/YAxisHistoGram.java:277-281; com/wildplot/android/rendering/DrawableContainer.java:58-63", 'SOURCE')
UNREACHABLE['YAxisHistoGram.drawBar(double,double,GraphicsWrap,RectangleWrap)'] = ('no_trigger_in_app', "Private 4-argument drawBar. Its caller in the file is paint (line 130), and it calls the 5-argument overload at line 161. paint runs only on an instance, and none is ever created.", "com/wildplot/android/rendering/YAxisHistoGram.java:130, 160-162", 'SOURCE')
UNREACHABLE['YAxisHistoGram.drawBar(double,double,GraphicsWrap,RectangleWrap,double)'] = ('no_trigger_in_app', "Private 5-argument drawBar. Its callers in the file are the 4-argument drawBar (line 161); that caller has only paint (line 130) above it, and no instance of the class is ever created.", "com/wildplot/android/rendering/YAxisHistoGram.java:161, 172-214", 'SOURCE')
UNREACHABLE['YAxisHistoGram.getExtraScaleFactor'] = ('no_trigger_in_app', "Getter. grep -rn 'getExtraScaleFactor' over the source root finds only declarations (no call); no YAxisHistoGram instance is ever created.", "com/wildplot/android/rendering/YAxisHistoGram.java:269-271", 'SOURCE')
UNREACHABLE['YAxisHistoGram.getMaxValue'] = ('no_trigger_in_app', "grep -rn 'getMaxValue' over the source root finds only declarations (YAxisHistoGram.java:136 and sibling classes); no call site exists. Its own call to getSizeInRange (line 144) needs an instance, and none is ever created.", "com/wildplot/android/rendering/YAxisHistoGram.java:136-151", 'SOURCE')
UNREACHABLE['YAxisHistoGram.getSizeInRange'] = ('no_trigger_in_app', "Private helper. Its callers in the file are paint (line 128) and getMaxValue (line 144), and both need an instance. No YAxisHistoGram instance is ever created.", "com/wildplot/android/rendering/YAxisHistoGram.java:128, 144, 224-235", 'SOURCE')
UNREACHABLE['YAxisHistoGram.isClusterable'] = ('no_trigger_in_app', "Drawable override returning true. Dispatch site: PlotSheet.prepareDrawables line 519, in the loop over the screen drawables (line 493). No YAxisHistoGram is ever constructed or added (grep 'YAxisHistoGram' finds only its own file).", "com/wildplot/android/rendering/YAxisHistoGram.java:282-285; com/wildplot/android/rendering/PlotSheet.java:493, 519", 'SOURCE')
UNREACHABLE['YAxisHistoGram.isCritical'] = ('no_trigger_in_app', "Drawable override returning false. Dispatch site: PlotSheet.prepareDrawables line 526 (loop at line 493). No YAxisHistoGram is ever constructed or added (grep 'YAxisHistoGram' finds only its own file).", "com/wildplot/android/rendering/YAxisHistoGram.java:287-290; com/wildplot/android/rendering/PlotSheet.java:493, 526", 'SOURCE')
UNREACHABLE['YAxisHistoGram.isOnFrame'] = ('no_trigger_in_app', "Getter returning true. Dispatch sites: PlotSheet.drawSingleMode line 357 (drawSingleMode starts at line 335) and PlotSheet.prepareDrawables line 499. No YAxisHistoGram is ever constructed or added (grep 'YAxisHistoGram' finds only its own file).", "com/wildplot/android/rendering/YAxisHistoGram.java:257-259; com/wildplot/android/rendering/PlotSheet.java:335, 357, 499", 'SOURCE')
UNREACHABLE['YAxisHistoGram.paint'] = ('no_trigger_in_app', "Drawable override; the isOnReset guard (lines 125-126) is inside it. Dispatch sites: DrawableContainer.paint line 49, and PlotSheet.drawSingleMode lines 366 and 473. The screen route is ChartView.onDraw lines 69-70, then PlotSheet.paint lines 322-329, then drawSingleMode. It ends at a missing instance: no YAxisHistoGram is ever constructed or added (grep 'YAxisHistoGram' finds only its own file).", "com/wildplot/android/rendering/YAxisHistoGram.java:95-135; com/wildplot/android/rendering/DrawableContainer.java:41-51; com/wildplot/android/rendering/PlotSheet.java:322-329, 335, 366, 473; com/ichi2/anki/stats/ChartView.java:57, 69-70", 'SOURCE')
UNREACHABLE['YAxisHistoGram.setAutoscale'] = ('no_trigger_in_app', "Setter taking binWidth. grep -rn 'setAutoscale' over the source root finds only declarations (no call); no YAxisHistoGram instance is ever created.", "com/wildplot/android/rendering/YAxisHistoGram.java:261-264", 'SOURCE')
UNREACHABLE['YAxisHistoGram.setExtraScaleFactor'] = ('no_trigger_in_app', "Setter. grep -rn 'setExtraScaleFactor' finds only declarations (no call); no YAxisHistoGram instance is ever created.", "com/wildplot/android/rendering/YAxisHistoGram.java:273-275", 'SOURCE')
UNREACHABLE['YAxisHistoGram.setFillColor'] = ('no_trigger_in_app', "Setter. The only setFillColor call in the source root is on a BarGraph (ChartBuilder line 244; barGraph is a new BarGraph at line 240), not on this class. No YAxisHistoGram instance is ever created.", "com/wildplot/android/rendering/YAxisHistoGram.java:88-90; com/ichi2/anki/stats/ChartBuilder.java:240, 244", 'SOURCE')
UNREACHABLE['YAxisHistoGram.setFilling'] = ('no_trigger_in_app', "Setter. The only setFilling call in the source root is ChartBuilder line 241, on a BarGraph (line 240). No YAxisHistoGram instance is ever created.", "com/wildplot/android/rendering/YAxisHistoGram.java:77-82; com/ichi2/anki/stats/ChartBuilder.java:240-241", 'SOURCE')
UNREACHABLE['YAxisHistoGram.setOnFrame()'] = ('no_trigger_in_app', "Calls setOnFrame(0) (line 251). Its callers in the source root are ChartBuilder line 280, on an XAxis (line 279), and line 327, on a YAxis (declared at line 313). Neither receiver is a YAxisHistoGram, and none is ever created.", "com/wildplot/android/rendering/YAxisHistoGram.java:250-252; com/ichi2/anki/stats/ChartBuilder.java:279-280, 313-317, 327", 'SOURCE')
UNREACHABLE['YAxisHistoGram.setOnFrame(double)'] = ('no_trigger_in_app', "Called only from setOnFrame() (line 251), which has no caller on a YAxisHistoGram. No instance is ever created.", "com/wildplot/android/rendering/YAxisHistoGram.java:245-248, 251", 'SOURCE')
UNREACHABLE['YAxisHistoGram.unsetAutoscale'] = ('no_trigger_in_app', "grep -rn 'unsetAutoscale' over the source root finds only declarations (no call); no YAxisHistoGram instance is ever created.", "com/wildplot/android/rendering/YAxisHistoGram.java:265-267", 'SOURCE')
UNREACHABLE['YAxisHistoGram.unsetOnFrame'] = ('no_trigger_in_app', "grep -rn 'unsetOnFrame' over the source root finds only declarations (no call); no YAxisHistoGram instance is ever created.", "com/wildplot/android/rendering/YAxisHistoGram.java:240-243", 'SOURCE')

# ---- sup for part 123 (2026-10-29, orchestrator, build 172): YAxisBarGraph and YAxisHistoGram are never constructed or subclassed (grep of the java root finds only their own constructor declarations), so the automatic CHA edges into them cannot fire
sup(
    ('YAxisBarGraph.paint', 'YAxisBarGraph.drawBar(double,double,GraphicsWrap,RectangleWrap)'),
    ('YAxisBarGraph.paint', 'YAxisBarGraph.drawBar(double,double,GraphicsWrap,RectangleWrap,double)'),
    ('YAxisBarGraph.drawBar(double,double,GraphicsWrap,RectangleWrap)', 'YAxisBarGraph.drawBar(double,double,GraphicsWrap,RectangleWrap,double)'),
    ('YAxisBarGraph.setOnFrame()', 'YAxisBarGraph.setOnFrame(double)'),
    ('YAxisHistoGram.paint', 'YAxisHistoGram.drawBar(double,double,GraphicsWrap,RectangleWrap)'),
    ('YAxisHistoGram.paint', 'YAxisHistoGram.getSizeInRange'),
    ('YAxisHistoGram.getMaxValue', 'YAxisHistoGram.getSizeInRange'),
    ('YAxisHistoGram.drawBar(double,double,GraphicsWrap,RectangleWrap)', 'YAxisHistoGram.drawBar(double,double,GraphicsWrap,RectangleWrap,double)'),
    ('YAxisHistoGram.setOnFrame()', 'YAxisHistoGram.setOnFrame(double)'),
    ('DrawableContainer.paint', 'YAxisHistoGram.paint'),
    ('DrawableContainer.paint', 'YAxisBarGraph.paint'),
    ('DrawableContainer.abortAndReset', 'YAxisHistoGram.abortAndReset'),
    ('DrawableContainer.abortAndReset', 'YAxisBarGraph.abortAndReset'),
    ('PlotSheet.drawSingleMode', 'YAxisHistoGram.paint'),
    ('PlotSheet.drawSingleMode', 'YAxisBarGraph.paint'),
    ('PlotSheet.drawSingleMode', 'YAxisHistoGram.isOnFrame'),
    ('PlotSheet.drawSingleMode', 'YAxisBarGraph.isOnFrame'),
    ('PlotSheet.prepareDrawables', 'YAxisHistoGram.isCritical'),
    ('PlotSheet.prepareDrawables', 'YAxisBarGraph.isCritical'),
    ('PlotSheet.prepareDrawables', 'YAxisHistoGram.isClusterable'),
    ('PlotSheet.prepareDrawables', 'YAxisBarGraph.isClusterable'),
    ('PlotSheet.prepareDrawables', 'YAxisHistoGram.isOnFrame'),
    ('PlotSheet.prepareDrawables', 'YAxisBarGraph.isOnFrame'),
)

# ---- part 124 (2026-10-29)
UNREACHABLE['YGrid.<init>(PlotSheet,double,int)'] = ('no_trigger_in_app', "Constructor with an int last argument. The only YGrid built in the source root is ChartBuilder line 343, new YGrid(plotSheet, 0, xTicks), and xTicks is a double (setupGrid, line 335), so the double overload is selected. No call selects this one.", "com/wildplot/android/rendering/YGrid.java:118-124; com/ichi2/anki/stats/ChartBuilder.java:335, 343", 'SOURCE')
UNREACHABLE['YGrid.<init>(ColorWrap,PlotSheet,double,double)'] = ('no_trigger_in_app', "Constructor with a ColorWrap first argument. The only YGrid construction in the source root (ChartBuilder line 343) passes a PlotSheet first, so this overload is never selected.", "com/wildplot/android/rendering/YGrid.java:105-111; com/ichi2/anki/stats/ChartBuilder.java:343", 'SOURCE')
UNREACHABLE['YGrid.<init>(ColorWrap,PlotSheet,double,int)'] = ('no_trigger_in_app', "Constructor with a ColorWrap first argument and an int last argument. The only YGrid construction in the source root (ChartBuilder line 343) passes a PlotSheet first and a double last, so this overload is never selected.", "com/wildplot/android/rendering/YGrid.java:132-135; com/ichi2/anki/stats/ChartBuilder.java:343", 'SOURCE')
UNREACHABLE['YGrid.abortAndReset'] = ('no_trigger_in_app', "Empty override (only a TODO comment). Its only caller is the cha dispatch in DrawableContainer.abortAndReset (line 62). DrawableContainer.abortAndReset (line 59) has no caller in the source root (grep for abortAndReset( finds only the declarations and line 62), so no YGrid is ever aborted.", "com/wildplot/android/rendering/YGrid.java:249-252; com/wildplot/android/rendering/DrawableContainer.java:59-63", 'SOURCE')
UNREACHABLE['YGrid.setGridOnDownside'] = ('no_trigger_in_app', "Setter with no call anywhere in the source root (grep finds only the declaration). No YGrid receives this setting.", "com/wildplot/android/rendering/YGrid.java:233-235", 'SOURCE')
UNREACHABLE['YGrid.setGridOnRight'] = ('no_trigger_in_app', "Setter with no call anywhere in the source root (grep finds only the declaration). No YGrid receives this setting.", "com/wildplot/android/rendering/YGrid.java:226-228", 'SOURCE')
UNREACHABLE['YGrid.setGridOnUpside'] = ('no_trigger_in_app', "Setter with no call anywhere in the source root (grep finds only the declaration). No YGrid receives this setting.", "com/wildplot/android/rendering/YGrid.java:240-242", 'SOURCE')
UNREACHABLE['YGrid.setGridkOnLeft'] = ('no_trigger_in_app', "Setter with no call anywhere in the source root (grep finds only the declaration). No YGrid receives this setting.", "com/wildplot/android/rendering/YGrid.java:219-221", 'SOURCE')
UNREACHABLE['YGrid.unsetExplicitTics'] = ('no_trigger_in_app', "No call anywhere in the source root (grep finds only the declaration). ChartBuilder calls setExplicitTicks (lines 351, 355, 359) but never unsetExplicitTics.", "com/wildplot/android/rendering/YGrid.java:270-272; com/ichi2/anki/stats/ChartBuilder.java:348-361", 'SOURCE')
UNREACHABLE['BufferedImageWrap.<clinit>'] = ('no_trigger_in_app', "Static initializer, run only on first use of BufferedImageWrap. TYPE_INT_ARGB is not a compile-time constant (line 27), so the first use is ReliefDrawer line 232 in drawColoredRelief. No ReliefDrawer is ever constructed (its constructors at lines 120, 145, 165 have no caller and grep finds no new ReliefDrawer( ), so drawColoredRelief never runs.", "com/wildplot/android/rendering/graphics/wrapper/BufferedImageWrap.java:27; com/wildplot/android/rendering/ReliefDrawer.java:120, 145, 165, 227-232", 'SOURCE')
UNREACHABLE['BufferedImageWrap.<init>'] = ('no_trigger_in_app', "Constructor. Its only call in the source root is ReliefDrawer line 232, inside drawColoredRelief (line 227). ReliefDrawer is never constructed, so drawColoredRelief never runs.", "com/wildplot/android/rendering/graphics/wrapper/BufferedImageWrap.java:29-31; com/wildplot/android/rendering/ReliefDrawer.java:227-232", 'SOURCE')
UNREACHABLE['BufferedImageWrap.createGraphics'] = ('no_trigger_in_app', "Called only by getGraphics (line 47). getGraphics is called only from ReliefDrawer.drawColoredRelief (lines 254, 262, 272), which never runs (see BufferedImageWrap.<clinit>).", "com/wildplot/android/rendering/graphics/wrapper/BufferedImageWrap.java:33-44, 46-48; com/wildplot/android/rendering/ReliefDrawer.java:254, 262, 272", 'SOURCE')
UNREACHABLE['BufferedImageWrap.getBitmap'] = ('no_trigger_in_app', "Called only by GraphicsWrap.drawImage (line 108). drawImage is called only from ReliefDrawer line 289, inside drawColoredRelief, which never runs.", "com/wildplot/android/rendering/graphics/wrapper/BufferedImageWrap.java:50-52; com/wildplot/android/rendering/graphics/wrapper/GraphicsWrap.java:103, 108; com/wildplot/android/rendering/ReliefDrawer.java:289", 'SOURCE')
UNREACHABLE['BufferedImageWrap.getGraphics'] = ('no_trigger_in_app', "Called only from ReliefDrawer.drawColoredRelief (lines 254, 262, 272), which never runs (see BufferedImageWrap.<clinit>).", "com/wildplot/android/rendering/graphics/wrapper/BufferedImageWrap.java:46-48; com/wildplot/android/rendering/ReliefDrawer.java:254, 262, 272", 'SOURCE')
UNREACHABLE['ColorWrap.<init>(float,float,float)'] = ('no_trigger_in_app', "Constructor with three float parameters. No call in the source root selects it: every three-argument new ColorWrap(...) passes int literals or int variables (ReliefDrawer line 109, RelativeColorGradient lines 31, 33, 65, FunctionDrawer line 69, FunctionDrawer_y line 68), so the int overload is chosen.", "com/wildplot/android/rendering/graphics/wrapper/ColorWrap.java:81-83; com/wildplot/android/rendering/RelativeColorGradient.java:31, 33, 65; com/wildplot/android/rendering/ReliefDrawer.java:109", 'SOURCE')
UNREACHABLE['ColorWrap.<init>(int,int,int)'] = ('no_trigger_in_app', "Constructor with three int parameters. Its callers are all in code that never runs: ReliefDrawer line 109 (field initializer; ReliefDrawer is never constructed), FunctionDrawer line 69 and FunctionDrawer_y line 68 (field initializers; neither class is ever constructed, grep finds no new FunctionDrawer or FunctionDrawer_y), and RelativeColorGradient lines 31, 33, 65 (in makeGradient, which is called only from ReliefDrawer lines 132 and 179).", "com/wildplot/android/rendering/graphics/wrapper/ColorWrap.java:69-71; com/wildplot/android/rendering/RelativeColorGradient.java:25, 31, 33, 65; com/wildplot/android/rendering/ReliefDrawer.java:109, 120, 132, 145, 165, 179; com/wildplot/android/rendering/FunctionDrawer.java:69; com/wildplot/android/rendering/FunctionDrawer_y.java:68", 'SOURCE')
UNREACHABLE['ColorWrap.brighter'] = ('no_trigger_in_app', "Called only from setFilling of XAxisBarGraph (line 76), YAxisBarGraph (line 78), XAxisHistoGram (line 82) and YAxisHistoGram (line 80). None of these four classes is ever constructed in the source root (grep finds no new XAxisBarGraph, YAxisBarGraph, XAxisHistoGram or YAxisHistoGram), so none of these setFilling methods has an instance to run on.", "com/wildplot/android/rendering/graphics/wrapper/ColorWrap.java:104-111; com/wildplot/android/rendering/XAxisBarGraph.java:76; com/wildplot/android/rendering/YAxisBarGraph.java:78; com/wildplot/android/rendering/XAxisHistoGram.java:82; com/wildplot/android/rendering/YAxisHistoGram.java:80", 'SOURCE')
UNREACHABLE['ColorWrap.darker'] = ('no_trigger_in_app', "Called only from the field initializer of ReliefDrawer (line 81, twice). ReliefDrawer is never constructed. The call in ChartBuilder line 243 is commented out.", "com/wildplot/android/rendering/graphics/wrapper/ColorWrap.java:113-120; com/wildplot/android/rendering/ReliefDrawer.java:81; com/ichi2/anki/stats/ChartBuilder.java:243", 'SOURCE')

# ---- sup for part 124 (2026-10-29, orchestrator, build 173): ReliefDrawer, FunctionDrawer(_y), RelativeColorGradient, XAxisBarGraph, YAxisBarGraph, XAxisHistoGram and YAxisHistoGram are never constructed (their sources have no caller); BufferedImageWrap is constructed only in ReliefDrawer.drawColoredRelief; DrawableContainer.abortAndReset has no caller
sup(
    ('XAxisBarGraph.setFilling', 'ColorWrap.brighter'),
    ('RelativeColorGradient.makeGradient', 'ColorWrap.<init>(int,int,int)'),
    ('YAxisBarGraph.setFilling', 'ColorWrap.brighter'),
    ('FunctionDrawer_y.<init>(Function2D,PlotSheet,ColorWrap)', 'ColorWrap.<init>(int,int,int)'),
    ('FunctionDrawer_y.<init>(Function2D,PlotSheet,ColorWrap,double,double)', 'ColorWrap.<init>(int,int,int)'),
    ('XAxisHistoGram.setFilling', 'ColorWrap.brighter'),
    ('ReliefDrawer.<init>(double,int,Function3D,PlotSheet,boolean)', 'ColorWrap.<init>(int,int,int)'),
    ('ReliefDrawer.<init>(double,int,Function3D,PlotSheet,boolean)', 'ColorWrap.darker'),
    ('ReliefDrawer.<init>(double,Function3D,PlotSheet)', 'ColorWrap.<init>(int,int,int)'),
    ('ReliefDrawer.<init>(double,Function3D,PlotSheet)', 'ColorWrap.darker'),
    ('ReliefDrawer.<init>(double,int,Function3D,PlotSheet,boolean,ColorWrap)', 'ColorWrap.<init>(int,int,int)'),
    ('ReliefDrawer.<init>(double,int,Function3D,PlotSheet,boolean,ColorWrap)', 'ColorWrap.darker'),
    ('ReliefDrawer.drawColoredRelief', 'BufferedImageWrap.<clinit>'),
    ('ReliefDrawer.drawColoredRelief', 'BufferedImageWrap.getGraphics'),
    ('ReliefDrawer.drawColoredRelief', 'BufferedImageWrap.<init>'),
    ('YAxisHistoGram.setFilling', 'ColorWrap.brighter'),
    ('DrawableContainer.abortAndReset', 'YGrid.abortAndReset'),
    ('FunctionDrawer.<init>(Function2D,PlotSheet,ColorWrap)', 'ColorWrap.<init>(int,int,int)'),
    ('FunctionDrawer.<init>(Function2D,PlotSheet,ColorWrap,double,double)', 'ColorWrap.<init>(int,int,int)'),
    ('BufferedImageWrap.getGraphics', 'BufferedImageWrap.createGraphics'),
    ('GraphicsWrap.drawImage', 'BufferedImageWrap.getBitmap'),
)

# ---- addendum to part 106 (2026-10-29): dispatch edges from HttpSyncer.req to EasySSLSocketFactory.
# The source method is in part 106 (HttpSyncer.java:226-236), so these edges belong to part 106.
# Batch 126 has REACHABLE rows for the three targets and needs these routes.

e('HttpSyncer.req(String,InputStream,int,JSONObject,CancelCallback)', 'EasySSLSocketFactory.connectSocket', 'FRAMEWORK',
  'the HTTP client opens the https connection through the socket factory that req registered for the https scheme',
  env=ENV_NETWORK,
  cls='non_standard',
  via=['Apache HttpClient 4.x DefaultHttpClient.execute, DefaultClientConnectionOperator (library source not read)'],
  evidence='SRC com/ichi2/libanki/sync/HttpSyncer.java:228, 236; INFERRED (Apache HttpClient 4.x source not read)',
  note='The factory is registered at HttpSyncer.java:228 and the request is executed at :236. The library dispatch to connectSocket is INFERRED (library source not read).')

e('HttpSyncer.req(String,InputStream,int,JSONObject,CancelCallback)', 'EasySSLSocketFactory.createSocket(Socket,String,int,boolean)', 'FRAMEWORK',
  'the HTTP client layers TLS on the opened socket through the https socket factory',
  env=ENV_NETWORK,
  cls='non_standard',
  via=['Apache HttpClient 4.x DefaultHttpClient.execute, LayeredSocketFactory (library source not read)'],
  evidence='SRC com/ichi2/libanki/sync/HttpSyncer.java:228, 236; INFERRED (Apache HttpClient 4.x source not read)',
  note='The https scheme is registered at HttpSyncer.java:228. The library dispatch to the layered-socket method is INFERRED (library source not read).')

e('HttpSyncer.req(String,InputStream,int,JSONObject,CancelCallback)', 'EasySSLSocketFactory.isSecure', 'FRAMEWORK',
  'the HTTP client asks the https socket factory whether the opened connection is secure',
  env=ENV_NETWORK,
  cls='non_standard',
  via=['Apache HttpClient 4.x DefaultHttpClient.execute (library source not read)'],
  evidence='SRC com/ichi2/libanki/sync/HttpSyncer.java:228, 236; INFERRED (Apache HttpClient 4.x source not read)',
  note='The https scheme is registered at HttpSyncer.java:228. The library dispatch to isSecure is INFERRED (library source not read).')

# ---- part 125 (2026-10-29)
UNREACHABLE['GraphicsWrap.dispose'] = ('no_trigger_in_app', 'Empty body (TODO comment only). No call to dispose() exists in the source root (grep finds only the definition). GraphicsWrap is constructed in ChartView.onDraw (ChartView.java:64), which does not call it.', 'SRC com/wildplot/android/rendering/graphics/wrapper/GraphicsWrap.java:143-145; SRC com/ichi2/anki/stats/ChartView.java:64', 'SOURCE')
UNREACHABLE['GraphicsWrap.drawImage'] = ('no_trigger_in_app', 'Only caller is ReliefDrawer (ReliefDrawer.java:289). ReliefDrawer has three constructors (lines 120, 145, 165), and no code in the source root constructs it or subclasses it (grep finds no new ReliefDrawer call and no extends ReliefDrawer), so no chart screen reaches the call.', 'SRC com/wildplot/android/rendering/graphics/wrapper/GraphicsWrap.java:103-112; SRC com/wildplot/android/rendering/ReliefDrawer.java:34, 120, 145, 165, 284-290', 'SOURCE')
UNREACHABLE['GraphicsWrap.getCanvas'] = ('no_trigger_in_app', 'No call to getCanvas() exists in the source root (grep finds only the definition). ChartView passes its canvas into the wrapper (ChartView.java:64) and does not read it back.', 'SRC com/wildplot/android/rendering/graphics/wrapper/GraphicsWrap.java:122-124; SRC com/ichi2/anki/stats/ChartView.java:64', 'SOURCE')
UNREACHABLE['GraphicsWrap.getTypeface'] = ('no_trigger_in_app', 'No call to the no-argument getTypeface() exists in the source root (grep finds only the definition, whose body calls Paint.getTypeface()). PlotSheet calls setTypeface (PlotSheet.java:343) instead.', 'SRC com/wildplot/android/rendering/graphics/wrapper/GraphicsWrap.java:169-171; SRC com/wildplot/android/rendering/PlotSheet.java:343', 'SOURCE')
UNREACHABLE['GraphicsWrap.setShadow'] = ('no_trigger_in_app', 'Only call is commented out (Lines.java:73). ChartBuilder calls Lines.setShadow (ChartBuilder.java:269), a different method that only stores fields (Lines.java:163-169) and does not call this one.', 'SRC com/wildplot/android/rendering/graphics/wrapper/GraphicsWrap.java:173-176; SRC com/wildplot/android/rendering/Lines.java:73, 163-169; SRC com/ichi2/anki/stats/ChartBuilder.java:269', 'SOURCE')
UNREACHABLE['GraphicsWrap.unsetShadow'] = ('no_trigger_in_app', 'Only call is commented out (Lines.java:98). Lines.unsetShadow only clears a field (Lines.java:170-172).', 'SRC com/wildplot/android/rendering/graphics/wrapper/GraphicsWrap.java:177-179; SRC com/wildplot/android/rendering/Lines.java:98, 170-172', 'SOURCE')
UNREACHABLE['RectangleWrap.getRect'] = ('no_trigger_in_app', 'No call to getRect() exists in the source root (grep finds only the definition).', 'SRC com/wildplot/android/rendering/graphics/wrapper/RectangleWrap.java:49-51', 'SOURCE')
UNREACHABLE['RectangleWrap.height'] = ('no_trigger_in_app', 'No call to the height() method exists in the source root (the only .height() calls are android Rect.height() at RectangleWrap.java:37). Callers read the public field instead (PlotSheet.java:345 uses field.height).', 'SRC com/wildplot/android/rendering/graphics/wrapper/RectangleWrap.java:37, 45-47; SRC com/wildplot/android/rendering/PlotSheet.java:345', 'SOURCE')
UNREACHABLE['RectangleWrap.width'] = ('no_trigger_in_app', 'No call to the width() method exists in the source root (the only .width() calls are android Rect.width() at RectangleWrap.java:38). Callers read the public field instead (PlotSheet.java:345 uses field.width).', 'SRC com/wildplot/android/rendering/graphics/wrapper/RectangleWrap.java:38, 41-43; SRC com/wildplot/android/rendering/PlotSheet.java:345', 'SOURCE')
UNREACHABLE['GraphicsWrap.drawRect'] = ('branch_never_taken', 'BarGraph.drawBar calls drawRect only in its else branch (BarGraph.java:193-199), which runs only when filling is false (BarGraph.java:180). The only BarGraph construction is ChartBuilder.java:240 (points constructor), and ChartBuilder.java:241 always calls setFilling(true); the function constructors (BarGraph.java:79, 96) are never called. Lines.drawPoint (Lines.java:111-113) is called only from a commented line (Lines.java:95). The drawRect callers in LinesPoints.java:78, XAxisBarGraph.java:178, YAxisBarGraph.java:187, XAxisHistoGram.java:208 and YAxisHistoGram.java:208 are in classes that no code constructs or extends.', 'SRC com/wildplot/android/rendering/graphics/wrapper/GraphicsWrap.java:46-51; SRC com/wildplot/android/rendering/BarGraph.java:79, 96, 180, 193-199; SRC com/ichi2/anki/stats/ChartBuilder.java:240-241; SRC com/wildplot/android/rendering/Lines.java:95, 111-113; SRC com/wildplot/android/rendering/LinesPoints.java:78; SRC com/wildplot/android/rendering/XAxisBarGraph.java:178; SRC com/wildplot/android/rendering/YAxisBarGraph.java:187; SRC com/wildplot/android/rendering/XAxisHistoGram.java:208; SRC com/wildplot/android/rendering/YAxisHistoGram.java:208', 'SOURCE')

# ---- sup for part 125 (2026-10-29): automatic CALL edges into GraphicsWrap.drawRect and GraphicsWrap.drawImage whose source is in a closed branch or in a class that no code constructs or extends (grep of the source root, 2026-10-29).
sup(
    ('BarGraph.drawBar(double,double,GraphicsWrap,RectangleWrap,double)', 'GraphicsWrap.drawRect'),
    ('XAxisBarGraph.drawBar(double,double,GraphicsWrap,RectangleWrap,double)', 'GraphicsWrap.drawRect'),
    ('YAxisBarGraph.drawBar(double,double,GraphicsWrap,RectangleWrap,double)', 'GraphicsWrap.drawRect'),
    ('XAxisHistoGram.drawBar(double,double,GraphicsWrap,RectangleWrap,double)', 'GraphicsWrap.drawRect'),
    ('YAxisHistoGram.drawBar(double,double,GraphicsWrap,RectangleWrap,double)', 'GraphicsWrap.drawRect'),
    ('LinesPoints.drawPoint', 'GraphicsWrap.drawRect'),
    ('Lines.drawPoint', 'GraphicsWrap.drawRect'),
    ('ReliefDrawer.drawColoredRelief', 'GraphicsWrap.drawImage'),
)

# ---- part 126 (2026-10-29)
# AnkiDroid batch 126 (LABEL helper). EasySSLSocketFactory (9 methods) and EasyX509TrustManager (4 methods).
# The full row list is in graphs/AnkiDroid/parts/label_126.md.
#
# Route ownership:
# - Direct CALL edges inside this batch (EasySSLSocketFactory.<init>, createEasySSLContext, createSocket(),
#   getSSLContext, EasyX509TrustManager.<init>, and connectSocket into createSocket()) come from auto_calls.json.
#   They are not written here.
# - The library dispatch edges from HttpSyncer.req (to connectSocket, createSocket(Socket,String,int,boolean) and
#   isSecure) belong to batch 106 and are not written here (see the Leads in the .md).
# - This batch owns the one edge whose source is in this batch: createSocket(Socket,...) -> checkServerTrusted.
# Gate: ENV_NETWORK (the sync server is reachable).

e('EasySSLSocketFactory.createSocket(Socket,String,int,boolean)', 'EasyX509TrustManager.checkServerTrusted', 'FRAMEWORK',
  'the HTTP library layers TLS on the socket, and the TLS handshake checks the server certificate chain',
  env=ENV_NETWORK,
  cls='non_standard',
  via=['Apache HttpClient 4.x and the platform TLS stack (library and platform source not read)'],
  evidence='SRC org/apache/commons/httpclient/contrib/ssl/EasySSLSocketFactory.java:94-98; SRC org/apache/commons/httpclient/contrib/ssl/EasyX509TrustManager.java:46-53, 91; SRC com/ichi2/libanki/sync/HttpSyncer.java:226-228, 236; INFERRED (library and platform source not read)',
  note='createSocket(Socket,...) returns the layered socket at line 97; the handshake that calls checkServerTrusted runs on that socket after it is returned. checkServerTrusted always delegates to the platform trust manager at line 91 of EasyX509TrustManager. The dispatch from HttpSyncer.req to createSocket(Socket,...) is owned by batch 106 and is not written here.')

UNREACHABLE['EasySSLSocketFactory.equals'] = ('no_trigger_in_app',
  'No app code calls equals on this factory. The factory is built only at HttpSyncer.req line 228 and registered there with SchemeRegistry. A grep of the source root for SchemeRegistry and new Scheme( lists only HttpSyncer. The HTTP library could compare a scheme that holds this factory, but its source is not read, so no such route is seen. Least certain entry of this batch.',
  'SRC org/apache/commons/httpclient/contrib/ssl/EasySSLSocketFactory.java:107-110; SRC com/ichi2/libanki/sync/HttpSyncer.java:33, 43, 226-228; INFERRED (Apache HttpClient 4.x source not read)',
  'INFERRED')

UNREACHABLE['EasySSLSocketFactory.hashCode'] = ('no_trigger_in_app',
  'No app code calls hashCode on this factory. Its only construction is at HttpSyncer.req line 228, and the only SchemeRegistry use is there. The HTTP library could hash a scheme that holds this factory, but its source is not read, so no such route is seen.',
  'SRC org/apache/commons/httpclient/contrib/ssl/EasySSLSocketFactory.java:113-116; SRC com/ichi2/libanki/sync/HttpSyncer.java:33, 43, 226-228; INFERRED (Apache HttpClient 4.x source not read)',
  'INFERRED')

UNREACHABLE['EasyX509TrustManager.checkClientTrusted'] = ('framework_never_calls',
  'No app call site: a grep of the source root for checkClientTrusted, checkServerTrusted and getAcceptedIssuers finds no call outside EasyX509TrustManager (its only call is its own delegate at line 39). The factory only creates client-side sockets (lines 77 and 97 use SSLContext.getSocketFactory() with no server socket), and a TLS client calls checkServerTrusted, not checkClientTrusted (INFERRED; platform TLS source not read).',
  'SRC org/apache/commons/httpclient/contrib/ssl/EasyX509TrustManager.java:37-40; SRC org/apache/commons/httpclient/contrib/ssl/EasySSLSocketFactory.java:77, 97; INFERRED (platform TLS source not read)',
  'INFERRED')

UNREACHABLE['EasyX509TrustManager.getAcceptedIssuers'] = ('framework_never_calls',
  'No app call site: a grep of the source root for getAcceptedIssuers finds no call outside EasyX509TrustManager (its only call is its own delegate at line 100). The TLS client does not ask its trust manager for accepted issuers (INFERRED; platform TLS source not read), and the factory only creates client-side sockets (lines 77 and 97).',
  'SRC org/apache/commons/httpclient/contrib/ssl/EasyX509TrustManager.java:98-101; SRC org/apache/commons/httpclient/contrib/ssl/EasySSLSocketFactory.java:77, 97; INFERRED (platform TLS source not read)',
  'INFERRED')

# ---- part 127 (2026-10-29)
# AnkiDroid batch 127 (LABEL helper). ActivityTransitionAnimation, AnkiActivity, AnkiDroidApp,
# AnkiDroidApp$ProductionCrashReportingTree, CollectionHelper, CollectionHelper$LazyHolder: 36 methods.
# The full row list is in graphs/AnkiDroid/parts/label_127.md.
#
# Route ownership:
# - Bytecode CALL edges between the methods of this batch and into them are written by the builder. They are not
#   repeated here.
# - Guard-less automatic CALL to suppress (not written here): AnkiDroidApp.onCreate -> AnkiDroidApp$ProductionCrashReportingTree.<init>.
#   The new at AnkiDroidApp.java:166 sits in the else branch of if (BuildConfig.DEBUG), which is never taken in the debug APK.
# - The S_ENTRY edge into AnkiDroidApp.onCreate is already in graph_def.py (lines 143-144) and is not repeated.
#
# Gates: no MG ids are used. No predefined ENV or STATE constant is needed for these two edges.

# --- Process start: the framework creates the Application, which initialises AnkiDroidApp first.
e('S_ENTRY', 'AnkiDroidApp.<clinit>', 'FRAMEWORK',
  'the process starts and the framework creates the Application, which initialises AnkiDroidApp first',
  env=None,
  evidence='FW-SRC core/java/android/app/Instrumentation.java:1099-1104; SRC com/ichi2/anki/AnkiDroidApp.java:119-139',
  note='Same route as the existing S_ENTRY to AnkiDroidApp.<init> (graph_def.py lines 310-314). The JVM class-initialisation step is not in fw_src: INFERRED.')

# --- Loader restart in startLoadingCollection; the loader framework calls back onCreateLoader.
e('AnkiActivity.startLoadingCollection', 'AnkiActivity.onCreateLoader', 'FRAMEWORK',
  'the collection loader is restarted and the loader framework calls back onCreateLoader',
  env=None,
  evidence='SRC com/ichi2/anki/AnkiActivity.java:254-262, 275-279',
  note='restartLoader (AnkiActivity.java:261) is not gated in startLoadingCollection. The support-library LoaderManager is not in fw_src: INFERRED.')

# --- UNREACHABLE: the crash reporting tree is only created in the release branch (BuildConfig.DEBUG is false there).
UNREACHABLE['AnkiDroidApp$ProductionCrashReportingTree.<clinit>'] = ('closed_by_configuration', 'The only construction of the tree is Timber.plant(new ProductionCrashReportingTree()) at AnkiDroidApp.java:166, in the else branch of if (BuildConfig.DEBUG) (AnkiDroidApp.java:155 and 164). The dataset APK is a debug build (final_java_only/AnkiDroid/app/DATASET.txt:4), so BuildConfig.DEBUG is true and that branch is never taken. No other reference to the class exists in the source root.', 'SRC com/ichi2/anki/AnkiDroidApp.java:155-167, 383-386; final_java_only/AnkiDroid/app/DATASET.txt:4', 'SOURCE')

UNREACHABLE['AnkiDroidApp$ProductionCrashReportingTree.<init>'] = ('closed_by_configuration', 'The constructor runs only from the new at AnkiDroidApp.java:166, in the else branch of if (BuildConfig.DEBUG) (AnkiDroidApp.java:155 and 164). The dataset APK is a debug build (final_java_only/AnkiDroid/app/DATASET.txt:4), so BuildConfig.DEBUG is true and that branch is never taken. The automatic CALL from AnkiDroidApp.onCreate to this constructor must be suppressed.', 'SRC com/ichi2/anki/AnkiDroidApp.java:155-167, 383-386; final_java_only/AnkiDroid/app/DATASET.txt:4', 'SOURCE')

# ---- sup for part 127 (2026-10-29): AnkiDroidApp.onCreate creates the release tree only in the else branch of if (BuildConfig.DEBUG) (AnkiDroidApp.java:155-166); the dataset APK is the debug build (DATASET.txt apk line).
sup(
    ('AnkiDroidApp.onCreate', 'AnkiDroidApp$ProductionCrashReportingTree.<init>'),
    ('AnkiDroidApp.onCreate', 'AnkiDroidApp$ProductionCrashReportingTree.<clinit>'),
)

# ---- part 128 (2026-10-29)
# AnkiDroid batch 128 (LABEL helper). 39 methods; the full row list is in graphs/AnkiDroid/parts/label_128.md.
# Batch: IntentHandler and its $1 constructor, NoteEditor and its $1 constructor, UIUtils.getDayStart,
# UIUtils.saveCollectionInBackground, UIUtils$1.<init>, DialogHandler (3 methods), ConfirmModSchemaException.<init>,
# StorageAccessException.<init>(String), 18 StatsMetaInfo setters, BaseAsyncTask.<clinit> and BaseAsyncTask.<init>.
#
# Route ownership:
# - Every other route into this batch is an automatic CALL edge from the builder (auto_calls.json). Those are not
#   written here.
# - The S_ENTRY, LIFECYCLE and INTENT edges into IntentHandler, NoteEditor and the NoteEditor constructor already
#   exist in graph_def.py (lines 139-141, 147, 185-186, 197-198, 316-320, 328-332, 545-564, 1253, 1324, 1925,
#   2090, 2127, 2982). They are not repeated.
# - Two edges have a source in this batch and a destination the builder does not link: the listener methods of the
#   anonymous DeckTask.TaskListener created in UIUtils.saveCollectionInBackground (UIUtils$1.onPreExecute and
#   onPostExecute, both UNRESOLVED in methods.csv).
# - One edge models the Handler dispatch of a stored dialog message: DialogHandler.readMessage -> handleMessage.
#
# No UNREACHABLE entries: every method in this batch has a route.

e('UIUtils.saveCollectionInBackground', 'UIUtils$1.onPreExecute', 'ASYNC',
  'the save-collection task starts and DeckTask.onPreExecute delivers onPreExecute to the listener',
  env=None,
  needs_state=STATE_COLLECTION,
  evidence='SRC com/ichi2/async/DeckTask.java:344-346, 1276-1279; SRC com/ichi2/anki/UIUtils.java:113-119',
  note='The listener is the anonymous DeckTask.TaskListener created at UIUtils.java:115 (UIUtils$1). The edge is taken only when colIsOpen() holds (guard at UIUtils.java:114), so the state is STATE_COLLECTION. The DeckTask dispatch is the AsyncTask lifecycle, so the kind is ASYNC.')

e('UIUtils.saveCollectionInBackground', 'UIUtils$1.onPostExecute', 'ASYNC',
  'the save-collection task finishes and DeckTask.onPostExecute delivers the result to the listener',
  env=None,
  needs_state=STATE_COLLECTION,
  evidence='SRC com/ichi2/async/DeckTask.java:359-362, 1276-1287; SRC com/ichi2/anki/UIUtils.java:113-125',
  note='Same listener and the same colIsOpen() guard (UIUtils.java:114) as the onPreExecute edge. The onPostExecute body (UIUtils.java:123-125) only logs.')

e('DialogHandler.readMessage', 'DialogHandler.handleMessage', 'ASYNC',
  'the stored dialog message is posted to the Handler queue and dispatched to handleMessage on the main looper',
  env=None,
  needs_state=STATE_SESSION,
  guard='sStoredMessage is not null: a message was stored earlier in this process by DialogHandler.storeMessage',
  evidence='SRC com/ichi2/anki/dialogs/DialogHandler.java:28, 56, 130-136; FW-SRC core/java/android/os/Handler.java:97-106, 596-600',
  note='DialogHandler extends Handler (DialogHandler.java:28). readMessage calls sendMessage(sStoredMessage) (line 133). The Handler route is sendMessage -> sendMessageDelayed (Handler.java:596-600), then the looper calls dispatchMessage, which calls handleMessage (Handler.java:97-106). The stored-message precondition has no ENV constant. STATE_SESSION is the closest fit, because the static field is set only in the same process. No MG id is used.')

# ---- part 129 (2026-10-29)
# AnkiDroid batch 129 (LABEL helper). CompatHelper, the Compat implementations on the API 27 path, the DeckTask launch
# and listener, and the Custom Tabs helpers. 37 methods: 30 REACHABLE, 7 UNREACHABLE (closed_by_api_level).
# The full row list is in graphs/AnkiDroid/parts/label_129.md.
#
# Route ownership:
# - The CALL edges out of CompatHelper, the Compat* constructors, AnkiActivity, DeckPicker, DB, Storage and the widget
#   code come from auto_calls.json and are not written here. Among them, the CHA targets on CompatV10 and the branch
#   edges of the CompatHelper constructor that API 27 never takes are named in the final answer for suppression.
# - Written here: the AsyncTask hops out of DeckTask.launchDeckTask (execute, then onPreExecute on the calling thread,
#   then doInBackground on the worker thread), because the source method is in this batch.
# - No gate constant is used by these two edges (env=None). Browser and widget gates are named in the row reasons.

e('DeckTask.launchDeckTask', 'DeckTask.doInBackground', 'ASYNC',
  'AsyncTask.execute hands the task to the worker thread, which calls DeckTask.doInBackground (the task body)',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-595, 632-651, 326-333',
  note='executeOnExecutor (AsyncTask.java:632-651) hands mWorker to exec.execute at line 651; the worker call at line 333 runs doInBackground.')

e('DeckTask.launchDeckTask', 'DeckTask.onPreExecute', 'FRAMEWORK',
  'AsyncTask.executeOnExecutor calls onPreExecute on the calling UI thread before the worker starts; DeckTask.onPreExecute forwards to the listener',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:129-134, 344-347; FW-SRC core/java/android/os/AsyncTask.java:594-595, 632-648, 412-413',
  note='Runs synchronously inside execute() on the thread that called launchDeckTask.')

UNREACHABLE['CompatV10.disableDatabaseWriteAheadLogging'] = ('closed_by_api_level', 'Overridden by CompatV16.disableDatabaseWriteAheadLogging, and no override calls super. On API 27 CompatHelper selects CompatV21, and the nearest override up its superclass chain is CompatV16, so this empty body never runs.', 'com/ichi2/compat/CompatV10.java:69-71; com/ichi2/compat/CompatV16.java:29-32; com/ichi2/compat/CompatHelper.java:35-36; com/ichi2/compat/CompatV21.java:13', 'SOURCE')

UNREACHABLE['CompatV10.enableCookiesForFileSchemePages'] = ('closed_by_api_level', 'Overridden by CompatV12.enableCookiesForFileSchemePages. CompatV15 to CompatV21 do not override it and no override calls super, so on API 27 the CompatV12 body runs (AnkiDroidApp.onCreate:177) and this Timber.w body never does.', 'com/ichi2/compat/CompatV10.java:74-77; com/ichi2/compat/CompatV12.java:14-21; com/ichi2/compat/CompatV15.java:11; com/ichi2/anki/AnkiDroidApp.java:177', 'SOURCE')

UNREACHABLE['CompatV10.prepareWebViewCookies'] = ('closed_by_api_level', 'Overridden by CompatV21.prepareWebViewCookies (empty body). API 27 selects CompatV21, so the CompatV10 CookieSyncManager body never runs (AnkiDroidApp.onCreate:180 dispatches to CompatV21).', 'com/ichi2/compat/CompatV10.java:79-83; com/ichi2/compat/CompatV21.java:23-27; com/ichi2/anki/AnkiDroidApp.java:180', 'SOURCE')

UNREACHABLE['CompatV10.updateWidgetDimensions'] = ('closed_by_api_level', 'Overridden by CompatV16.updateWidgetDimensions. API 27 selects CompatV21, whose chain reaches CompatV16 first, so this empty body never runs; the automatic CHA edges to it (AnkiDroidWidgetSmall.java:72, 171) name a target that does not run on API 27.', 'com/ichi2/compat/CompatV10.java:97-100; com/ichi2/compat/CompatV16.java:42-43; com/ichi2/widget/AnkiDroidWidgetSmall.java:171', 'SOURCE')

UNREACHABLE['CompatV11.disableDatabaseWriteAheadLogging'] = ('closed_by_api_level', 'Shadowed by the CompatV16 override (db.disableWriteAheadLogging), which is the nearest override above CompatV21 and does not call super. On API 27 the rawQuery PRAGMA body never runs.', 'com/ichi2/compat/CompatV11.java:34-38; com/ichi2/compat/CompatV16.java:29-32; com/ichi2/compat/CompatHelper.java:35-36', 'SOURCE')

UNREACHABLE['CompatV15NookHdOrHdPlus.<init>'] = ('closed_by_api_level', 'Created only when isNookHdOrHdPlus() is true and getSdkVersion() == 15 (CompatHelper.java:33-34). API 27 fails the SDK test, so this constructor never runs. The automatic exact edge CompatHelper.<init> -> CompatV15NookHdOrHdPlus.<init> is a suppression candidate.', 'com/ichi2/compat/CompatHelper.java:33-34; com/ichi2/compat/CompatV15NookHdOrHdPlus.java:14', 'SOURCE')

UNREACHABLE['CompatV15NookHdOrHdPlus.disableDatabaseWriteAheadLogging'] = ('closed_by_api_level', 'Only reachable through a CompatV15NookHdOrHdPlus instance, which API 27 never creates (the instance needs SDK 15, CompatHelper.java:33-34). The method is not on the API 21+ superclass chain of CompatV21.', 'com/ichi2/compat/CompatV15NookHdOrHdPlus.java:16-19; com/ichi2/compat/CompatHelper.java:33-34', 'SOURCE')

# ---- sup for part 129 (2026-10-29): on API 27 CompatHelper picks CompatV21 (CompatHelper.java:35-36), and CompatV21 inherits each Compat method from a later override (CompatV16 for disableDatabaseWriteAheadLogging and updateWidgetDimensions, CompatV12 for enableCookiesForFileSchemePages, CompatV21 for prepareWebViewCookies). The CompatV10 and CompatV11 bodies and the Nook class are shadowed on API 27; their automatic CHA CALL edges are suppressed here. CompatHelper.<init> reaches the Nook constructor only when getSdkVersion() == 15 (CompatHelper.java:34).
sup(
    ('CompatHelper.<init>', 'CompatV15NookHdOrHdPlus.<init>'),
    ('AnkiDroidWidgetSmall$UpdateService.buildUpdate', 'CompatV10.updateWidgetDimensions'),
    ('AnkiDroidWidgetSmall.onReceive', 'CompatV10.updateWidgetDimensions'),
    ('AnkiDroidApp.onCreate', 'CompatV10.prepareWebViewCookies'),
    ('AnkiDroidApp.onCreate', 'CompatV10.enableCookiesForFileSchemePages'),
    ('Collection.close(boolean)', 'CompatV15NookHdOrHdPlus.disableDatabaseWriteAheadLogging'),
    ('Collection.close(boolean)', 'CompatV11.disableDatabaseWriteAheadLogging'),
    ('Collection.close(boolean)', 'CompatV10.disableDatabaseWriteAheadLogging'),
    ('DB.<init>', 'CompatV15NookHdOrHdPlus.disableDatabaseWriteAheadLogging'),
    ('DB.<init>', 'CompatV11.disableDatabaseWriteAheadLogging'),
    ('DB.<init>', 'CompatV10.disableDatabaseWriteAheadLogging'),
)

# ---- part 130 (2026-10-29)
# Batch 130 LABEL output (AnkiDroid, com/ichi2/libanki/Collection.java)
# 34 methods labelled REACHABLE, 0 UNREACHABLE, 0 e() edges written.
# Per-method rows and citations are in label_130.md in this directory.
# No outgoing hop from these methods is a non-CALL edge; the hops are direct Java calls
# already covered by the builder CALL edges, so nothing is repeated here.

# ---- part 131 (2026-10-29)
# AnkiDroid batch 131 (LABEL helper, schema 2). DB, Decks and LaTeX: 40 methods, all REACHABLE.
# The full row list with source cites is in graphs/AnkiDroid/parts/label_131.md.
#
# Methods: DB.<clinit>, DB.<init>, DB$MyDbErrorHandler.<init>, DB.close, DB.commit, DB.execute(String),
# DB.execute(String,Object[]), DB.executeMany, DB.executeScript, DB.getCursorMethodName, DB.getDatabase,
# DB.getMod, DB.insert, DB.queryColumn, DB.queryLongScalar, DB.queryScalar(String),
# DB.queryScalar(String,String[]), DB.setMod, DB.update(String,ContentValues),
# DB.update(String,ContentValues,String,String[]), Decks.<clinit>, Decks.<init>, Decks.all, Decks.allConf,
# Decks.confForDid, Decks.flush, Decks.get(long), Decks.get(long,boolean), Decks.getConf, Decks.isDyn,
# Decks.load, Decks.name(long), Decks.name(long,boolean), Decks.save(JSONObject), LaTeX.<clinit>,
# LaTeX.<init>, LaTeX._imgLink, LaTeX._latexFromHtml, LaTeX.installHook, LaTeX.mungeQA.
#
# Route ownership:
# - The DB, Decks, LaTeX and MyDbErrorHandler constructors and the static initialisers run on collection open
#   (Storage.java:45-63; Collection.java:140-157). The Collection constructor calls are CALL edges that the builder
#   writes from auto_calls.json. They are not written here.
# - The DB and Decks write methods run inside Collection.save (Collection.java:257-268) and the delete-note,
#   undo and check-database paths in DeckTask. Those edges are automatic CALL edges, not written here.
# - LaTeX.mungeQA runs through the Hooks.runFilter("mungeQA") route (Collection.java:1010; Hooks.java:138-150).
#   The card-render route is in the rows of the .md. The edge is automatic and not written here.
# - No e() calls and no UNREACHABLE entries: every method above has a route in the standard configuration.
#
# Caveats recorded in the .md:
# - DeckAdapter.processNodes queryScalar (DeckAdapter.java:251) needs a second deck in the deck list.
# - LaTeX._imgLink and _latexFromHtml need a card field that carries a LaTeX tag (content condition).
# - Decks.<clinit> body is not decoded (javap is not available); the source has only constant String fields.

# ---- part 132 (2026-10-29)
# AnkiDroid batch 132 (LABEL helper). Methods: Media.<clinit>, Media.<init>, Media.connect, Media._initDB,
# Media.close, Media.dir, Media.maybeUpgrade, LaTeX$LaTeXFilter.<init>, LaTeX$LaTeXFilter.runFilter.
#
# All nine are REACHABLE through automatic CALL edges (graphs/AnkiDroid/auto_calls.json). No e() edge and no
# UNREACHABLE entry is written here. The row list with the route and source lines is in
# graphs/AnkiDroid/parts/label_132.md.

# ---- part 133 (2026-10-29)
# AnkiDroid batch 133 (LABEL helper). Models part: 39 methods, all labelled REACHABLE.
# The full row list (label, kind, reason, source) is in graphs/AnkiDroid/parts/label_133.md.
#
# No e() edges and no UNREACHABLE entries are written here:
# - Every caller of these methods is an automatic CALL edge in graphs/AnkiDroid/auto_calls.json. Each row names
#   the caller and its call line.
# - The page-owned edges (S_*) that reach these methods belong to other batches.
#
# Recorded in the rows, not as edges:
# - Gate STATE_NOTE: the Models$TransformFieldAdd, Delete and Move transform bodies run only inside the per-note
#   loop of Models._transformFields (Models.java:722-726), so the model needs at least one note.
# - Over-approximation: auto_calls.json maps Models._transformFields (Models.java:726) to all three transform bodies
#   (dispatch cha). Each call site passes one visitor, so no pair is suppressed.

# ---- part 136 (2026-10-30)
# AnkiDroid batch 136 (LABEL helper). LoadPronounciationActivity (20 methods) and TranslationActivity (20 methods).
# All 40 methods are labelled REACHABLE. The full row list (label, kind, reason, printed file:lines) is in
# graphs/AnkiDroid/parts/label_136.md. No UNREACHABLE entries are written here.
#
# Route dependency (not written here): every route into these two activities starts at the text editor page
# S_MULTIMEDIA_EDIT_FIELD (GUI edges BasicTextFieldController$2.onClick at graph_def.py:7383 and $3.onClick at 7396).
# That page has no inbound ENTERS edge yet. The ENTERS edge from MultimediaEditFieldActivity.onCreate belongs to batch 138.
# Until it exists, the build reports these methods as UNRESOLVED.
#
# Edges written here are page ENTERS edges whose source is a method of this batch (the DeckPicker.onCreate ->
# S_DECKPICKER pattern, graph_def.py:835). Edges already in graph_def.py and not repeated here:
# - LIFECYCLE <init> -> onCreate -> onPause (lc_chain, graph_def.py:282 and 291).
# - Page GUI and FRAMEWORK edges (graph_def.py:6265-6284, 6349-6393) and part 049 (S_DLG_PICK_STRING -> TranslationActivity.onClick).
# - INTENT edges into <init> (graph_def.py:7390 and 7416).
# Automatic CALL edges come from auto_calls.json and are not written here.

e('LoadPronounciationActivity.onCreate', 'S_LOAD_PRONOUNCIATION', 'ENTERS',
  'the pronunciation screen is created and shown (not a restore after shut-off)',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:91-140',
  note='onCreate returns early at lines 96-98 (finishCancel) when the saved state has the shut-off flag written by onSaveInstanceState (lines 400-403). Otherwise the layout is set at line 102 and the controls are built at lines 103-137. The network check is in onLoadPronunciation (line 155), inside the page, so no gate is set here.')

e('TranslationActivity.onCreate', 'S_TRANSLATION', 'ENTERS',
  'the translation screen is created and shown (not a restore after shut-off)',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/activity/TranslationActivity.java:91-168',
  note='onCreate returns early at lines 96-98 (finishCancel) when the saved state has the shut-off flag written by onSaveInstanceState (lines 382-388). Otherwise the layout is set at line 102 and the controls are built at lines 104-166. The network check is in translate (line 197), inside the page, so no gate is set here.')

e('TranslationActivity.showPickTranslationDialog', 'S_DLG_PICK_STRING', 'ENTERS',
  'the Glosbe lookup returns ok with at least one translation: the translation pick list is shown',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/activity/TranslationActivity.java:257-297',
  note='The pick list (PickStringDialogFragment, page S_DLG_PICK_STRING) is shown at line 297 only when the response is ok and parseJson returns at least one translation (lines 271-289). Otherwise returnFailure runs. The same page is also entered by the field picker edges (BasicTextFieldController$3.onClick at graph_def.py:7403 and $4.onClick at 7436), which are another batch. Page node shared; no gate is set here.')

# ---- part 137 (2026-10-30)
# AnkiDroid batch 137 (LABEL helper). Reviewer (15 methods), Whiteboard (13 methods) and YAxis (12 methods).
# Source row: graphs/AnkiDroid/scratch/batches_ai.tsv, part 137. (scratch/batches/batch_137.txt lists other classes and was not used.)
# All 40 methods are labelled REACHABLE. The full row list (label, kind, reason, printed file:lines) is in
# graphs/AnkiDroid/parts/label_137.md. No UNREACHABLE entries are written here.
#
# Route gaps in out/ that the edges below close (every batch method is UNRESOLVED there without them):
# - S_REVIEWER has no inbound ENTERS edge. Written here: Reviewer.onCollectionLoaded -> S_REVIEWER.
# - AnkiActivity.onLoadFinished@Reviewer (receiver variant) has no inbound edge, so the loader route into
#   Reviewer.onCollectionLoaded is missing. Written here: ASYNC AbstractFlashcardViewer.onCreate -> Reviewer.onCollectionLoaded.
# - AbstractFlashcardViewer.onCreate@Reviewer (receiver variant) has no inbound edge, so its callees are blocked.
#   Written here: base-node CALL edges AbstractFlashcardViewer.onCreate -> Reviewer.restorePreferences and -> Reviewer.getContentViewAttr.
# - S_STATISTICS has no inbound ENTERS edge, and the YAxis chain runs through ChartView.onDraw from that page.
#   Written here: Statistics.onCreate -> S_STATISTICS (page edge outside the batch).
#
# Already in graph_def.py and not repeated here: S_REVIEWER GUI and FRAMEWORK edges (graph_def.py:1361-1444),
# Whiteboard.onDraw from S_REVIEWER (7002), S_STATISTICS -> ChartView.onDraw (7657), the Reviewer.<init> lifecycle chain.
# Automatic CALL edges come from auto_calls.json and are not written here.

e('AbstractFlashcardViewer.onCreate', 'Reviewer.onCollectionLoaded', 'ASYNC',
  'the collection finishes loading and the loader calls onCollectionLoaded on the Reviewer (AnkiActivity.onLoadFinished dispatch)',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:859; SRC com/ichi2/anki/AnkiActivity.java:255-262, 283-290; SRC com/ichi2/anki/Reviewer.java:96-98',
  note='The loader callback is androidx Loader, a library step: INFERRED, source not read. AnkiActivity.onLoadFinished has no inbound edge in out/, so the edge is written from the base onCreate, following the CardBrowser.onCreate -> CardBrowser.onCollectionLoaded ASYNC precedent (graph_def.py:1500-1510). Reviewer.java:96-97 is an @Override of AnkiActivity.onCollectionLoaded, so the virtual call at AnkiActivity.java:286 reaches the Reviewer method.')

e('Reviewer.onCollectionLoaded', 'S_REVIEWER', 'ENTERS',
  'the review screen is live once the collection is loaded: the cards and the controls are set up',
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:97-115; SRC com/ichi2/anki/AbstractFlashcardViewer.java:879-890',
  note='Page ENTERS from a method of this batch, following Previewer.onCollectionLoaded -> S_PREVIEWER (parts/label_036.py:151-155). Without it S_REVIEWER has no inbound edge, so every S_REVIEWER page edge (onCreateOptionsMenu, onKeyUp, onOptionsItemSelected, onWindowFocusChanged, Whiteboard.onDraw, Reviewer$1.onTouch and the AbstractFlashcardViewer page edges) stays UNRESOLVED.')

e('AbstractFlashcardViewer.onCreate', 'Reviewer.restorePreferences', 'CALL',
  'AbstractFlashcardViewer.onCreate calls restorePreferences(), which dispatches to the Reviewer override',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:849-855; SRC com/ichi2/anki/Reviewer.java:396-397',
  note='Virtual dispatch: Reviewer.java:396 overrides restorePreferences (super call at line 397). The auto edge from the variant AbstractFlashcardViewer.onCreate@Reviewer has no inbound edge in out/, so this base-node edge is the route.')

e('AbstractFlashcardViewer.onCreate', 'Reviewer.getContentViewAttr', 'CALL',
  'AbstractFlashcardViewer.onCreate calls getContentViewAttr() to choose the layout, which dispatches to the Reviewer override',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:855, 862-864; SRC com/ichi2/anki/Reviewer.java:82',
  note='Same reason as the restorePreferences edge above. Reviewer.java:82 overrides AbstractFlashcardViewer.getContentViewAttr(int).')

e('Statistics.onCreate', 'S_STATISTICS', 'ENTERS',
  'the statistics screen is created and its layout is set (activity_anki_stats)',
  env=None,
  evidence='SRC com/ichi2/anki/Statistics.java:81-88',
  note='Page edge whose source and destination are both outside batch 137, written under the page-edge exception: S_STATISTICS has no inbound edge in out/, and the YAxis route (ChartView.onDraw, FRAMEWORK, graph_def.py:7657) cannot be reached without it. Precedent: DeckPicker.onCreate -> S_DECKPICKER (graph_def.py:835). No S_STATISTICS ENTERS exists in graph_def.py or parts/*.py at the time of writing. If the Statistics batch writes the same edge, delete this one.')

# ---- part 135 (2026-10-30)
# AnkiDroid batch 135 (LABEL helper). 40 methods: AnkiDroidWidgetSmall$UpdateService (3), CardTemplateEditor$CardTemplateFragment
# (15) and GraphicsWrap (22). The full row list is in graphs/AnkiDroid/parts/label_135.md.
#
# Labels: all 40 are REACHABLE. There are no UNREACHABLE entries here.
#
# Route ownership:
# - One page-entry ENTERS edge is written here (method to page, env None, same convention as StudyOptionsActivity.onCreate in
#   label_007.py): CardTemplateEditor.onCreate -> S_CARDTEMPLATEEDITOR. Its source method is in batch 025, which did not write it.
#   Without it S_CARDTEMPLATEEDITOR is not reachable from S_ENTRY (build_report.txt line 852), so every page-owned edge into this
#   batch is unrouted. Possible duplicate if 025 adds the same edge later.
# - The Statistics.onCreate -> S_STATISTICS ENTERS edge is not written here: it is already in graph_def.py:11196 and in
#   label_137.py:43 (batch 137).
# - Not written here: the AsyncTask edges that lead into UpdateService.<init>, namely WidgetStatus.update -> UpdateDeckStatusAsyncTask
#   .doInBackground (ASYNC) and doInBackground -> onPostExecute (ASYNC). Neither is in graph_def.py or any part. Their source is in
#   the batch that contains WidgetStatus.update, which has no label row yet. The INTENT edges out of onPostExecute into
#   UpdateService.<init> and NotificationService.<init> are already written in label_080.py.
# - Automatic CALL edges (auto_calls.json) are not written here. The same labels for these 40 methods already exist in
#   label_018.md (UpdateService), label_025.md and label_026.md (CardTemplateFragment) and label_125.md (GraphicsWrap).
#
# Gates: no new gate. The fragment routes need S_CARDTEMPLATEEDITOR; the GraphicsWrap routes need S_STATISTICS and
# ChartView.setData (mDataIsSet). The onActivityResult route needs S_PREVIEWER, whose loader step is not in the graph yet
# (label_036.md). No STATE or ENV constant fits these gates, so env and needs_state are unset.

e('CardTemplateEditor.onCreate', 'S_CARDTEMPLATEEDITOR', 'ENTERS',
  'the template editor screen is shown: the activity starts the collection load and its page is on screen',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:127, 157, 205',
  note='Method to page (ENTERS). The start edges into this activity are INTENT edges from NoteEditor.showCardTemplateEditor (graph_def.py:2134) and ModelBrowser.openTemplateEditor (graph_def.py:4265), written in other batches. The collection load is started at line 157; onCollectionLoaded (line 205) is the ASYNC route written in label_025.py. Possible duplicate of a page-entry edge that batch 025 may add later.')


# ---- part 138 (2026-10-30)
# AnkiDroid batch 138 (LABEL helper). 40 methods in 5 classes: AbstractFlashcardViewer$11 (1), Lines (7),
# ModelFieldEditor (11, including closeActivity()), MultimediaEditFieldActivity (10), XAxis (11).
# All 40 are labelled REACHABLE from printed source. No UNREACHABLE entries are written here, because no method
# has a printed path that is provably dead. The row list (label, kind, reason, printed file:lines) is in
# graphs/AnkiDroid/parts/label_138.md.
#
# Edges written here (page ENTERS edges; the source is a method of this batch, same pattern as DeckPicker.onCreate
# -> S_DECKPICKER at graph_def.py:835):
#  1. MultimediaEditFieldActivity.onCreate -> S_MULTIMEDIA_EDIT_FIELD. Required by batch 136 (parts/label_136.py:7).
#  2. ModelFieldEditor.onCreate -> S_MODELFIELDEDITOR. The batch 033 header (graph_def.py:4591-4596) says these
#     ENTERS edges are written there, but no S_MODELFIELDEDITOR ENTERS edge exists in graph_def.py or parts/
#     (grep checked). Without it the 11 ModelFieldEditor rows cannot resolve. Batch 033 should not write it again.
#
# Not written here:
#  - S_STATISTICS has no inbound ENTERS edge. The Statistics page belongs to batch 144. The Lines and XAxis rows
#    depend on it (ChartView.onDraw FRAMEWORK edge at graph_def.py:7657).
#  - AbstractFlashcardViewer.answerCard -> AbstractFlashcardViewer$11.run (ASYNC, Handler.postDelayed at
#    AbstractFlashcardViewer.java:1316). The launch site belongs to the batch that holds answerCard, so this row
#    stays UNRESOLVED until that edge exists.
#  - ModelFieldEditor$1.onItemClick and ModelFieldEditor$9.onSelection edges are already in graph_def.py
#    (4635 and 4449), owned by batch 034.
# Automatic CALL edges come from auto_calls.json and are not written here.

e('MultimediaEditFieldActivity.onCreate', 'S_MULTIMEDIA_EDIT_FIELD', 'ENTERS',
  'the multimedia field editor screen is created and shown (not a restore after shut-off)',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:74-106',
  note='onCreate returns early at lines 77-82 (finishCancel) when the saved state has the shut-off flag written by onSaveInstanceState (lines 352-355). Otherwise the layout is set at line 85, the field, note and index are read at lines 92-96, the editing UI is built at line 98, and the spare menu is created only at API <= GINGERBREAD_MR1 (lines 101-105, closed by API level). Entry is the INTENT NoteEditor.startMultimediaFieldEditor -> MultimediaEditFieldActivity.<init> (graph_def.py:2140), whose gates belong to the NoteEditor batch, so no gate is set here. The LIFECYCLE <init> -> onCreate edge comes from lc_chain (graph_def.py:284-285).')

e('ModelFieldEditor.onCreate', 'S_MODELFIELDEDITOR', 'ENTERS',
  'the field editor screen is created; its field list is shown once the collection is loaded (onCollectionLoaded)',
  env=None, needs_state=STATE_COLLECTION,
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:72-89; SRC com/ichi2/anki/AnkiActivity.java:255-262, 283-290',
  note='onCreate sets the content view and calls startLoadingCollection (ModelFieldEditor.java:72-89; AnkiActivity.java:255-262). The loader result reaches onCollectionLoaded through onLoadFinished (AnkiActivity.java:283-290), which is the ASYNC edge at graph_def.py:4599. STATE_COLLECTION follows the note at graph_def.py:4633 (the list is filled after the collection loads). Entry is the INTENT ModelBrowser$4.onItemClick -> ModelFieldEditor.<init> (graph_def.py:4259). No env is set here: the storage gate belongs to the route that opens the app. Batch 033 header (graph_def.py:4591-4596) planned this edge and did not write it.')

# ---- part 134 (2026-10-30)
# AnkiDroid batch 134 (LABEL helper): AbstractFlashcardViewer (32 methods), AbstractFlashcardViewer$1.handleMessage,
# and DeckOptions$DeckPreferenceHack$Editor (5 methods). Labels: 38 REACHABLE, no UNREACHABLE. putString and remConf are labelled in batch 028.
# Edges written here (both are cited to printed source; neither is a batch-134 method pair):
#  - DeckOptions.onCreate -> S_DECKOPTIONS ENTERS: page-entry fix. No ENTERS into S_DECKOPTIONS exists in graph_def.py or any parts/*.py.
#  - AbstractFlashcardViewer.answerCard -> AbstractFlashcardViewer$11.run ASYNC: coordinator request. The destination is batch 138's
#    method; label_138.py:17 has this edge only as a comment, so no duplicate.
# Constants used: STATE_DECK (graph_def.py:128). No new constants.

e('DeckOptions.onCreate', 'S_DECKOPTIONS', 'ENTERS',
  'the deck options preference screen is live once onCreate has loaded the deck and built the preference tree',
  needs_state=STATE_DECK,
  env=None,
  evidence='SRC com/ichi2/anki/DeckOptions.java:499-523',
  note='Page-entry edge from a method outside batch 134, because S_DECKOPTIONS had no ENTERS edge. Mirrors Reviewer.onCollectionLoaded -> S_REVIEWER (graph_def.py:11178). Without it, DeckPreferenceHack.edit, Editor.<init>, apply, commit, the putX methods and remConf have no graph route. If another part later adds the same ENTERS, keep one copy.')

e('AbstractFlashcardViewer.answerCard', 'AbstractFlashcardViewer$11.run', 'ASYNC',
  'answerCard posts the delayed removeChosenAnswerText runnable, which clears the chosen-answer dots after a short delay',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1316; SRC com/ichi2/anki/AbstractFlashcardViewer.java:825-830',
  note='Handler.postDelayed at line 1316 posts removeChosenAnswerText, the anonymous Runnable field at 825. Anonymous-class numbering in source order gives $1 Handler (349), $4 flip listener (382), $5 select-ease listener (396), $11 at 825, $13 dialog (1248), $14 look-up listener (1418), $15 WebViewClient (1435). Written at coordinator request; the destination belongs to batch 138.')

# ---- part 140 (2026-10-30)
# AnkiDroid batch 140 (LABEL helper). AbstractFlashcardViewer$18 (1 method), MetaDB (9), NoteEditor (7),
# PieChart (7), PlotSheet (9), YGrid (7). 40 methods in total.
# Source row: graphs/AnkiDroid/scratch/batches_ai.tsv, part 140. The full row list (label, kind, reason, printed file:lines)
# is in graphs/AnkiDroid/parts/label_140.md. All 40 methods are labelled REACHABLE. No UNREACHABLE entries are written here.
#
# Route gaps in out/ that the edges below close:
# - AnkiActivity.onLoadFinished has no inbound edge (base and @NoteEditor variant), so NoteEditor.onCollectionLoaded
#   has no loader route. Written here: ASYNC NoteEditor.onCreate -> NoteEditor.onCollectionLoaded (same pattern as
#   parts/label_137.py for Reviewer.onCollectionLoaded).
# - S_DLG_RESCHEDULE_CARD has no inbound ENTERS edge, so NoteEditorRescheduleCard$1.onInput (parts/label_044.py:57)
#   and NoteEditor.onRescheduleCard stay UNRESOLVED. Written here: ENTERS NoteEditor.onOptionsItemSelected -> S_DLG_RESCHEDULE_CARD.
# - AbstractFlashcardViewer$18.run has only a REGISTER edge in out/ (REGISTER does not count). The route is the postDelayed
#   call in displayCardAnswer (AbstractFlashcardViewer.java:2031-2033). Written here: FRAMEWORK
#   AbstractFlashcardViewer.displayCardAnswer -> AbstractFlashcardViewer$18.run (the batch_019 lead named in parts/label_021.py:83).
#
# Not written here (outside this batch, both ends or the gap is in another part):
# - WidgetStatus.update -> UpdateDeckStatusAsyncTask.execute -> doInBackground -> onPostExecute (ASYNC). Owned by part 080.
#   Until those edges exist, MetaDB.storeSmallWidgetStatus, closeDB, resetWidget, getWidgetSmallStatus and getNotificationStatus
#   are UNRESOLVED in out/ even though their rows are labelled REACHABLE (see parts/label_140.md).
#
# Already in graph_def.py and not repeated here: NoteEditor.onCollectionLoaded -> onDestroy (FRAMEWORK, graph_def.py:2186),
# NoteEditor.onCollectionLoaded -> JSONNameComparator.compare (CALL, graph_def.py:2230), S_STATISTICS -> ChartView.onDraw,
# S_REVIEWER -> ReadText$1.onSelection (GUI, graph_def.py:6693), AbstractFlashcardViewer$18.run -> AbstractFlashcardViewer$5.onClick
# (FRAMEWORK, graph_def.py:3252), the Reviewer.onCollectionLoaded chain written by parts/label_137.py.
# Automatic CALL edges come from auto_calls.json (bytecode) and are not written here.

e('NoteEditor.onCreate', 'NoteEditor.onCollectionLoaded', 'ASYNC',
  'the collection loader finishes and delivers the collection to the note editor (loader route from onCreate)',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:287-309, 331; SRC com/ichi2/anki/AnkiActivity.java:255-262, 283-290',
  note='onCreate calls startLoadingCollection (NoteEditor.java:309), which restarts the collection loader (AnkiActivity.java:261). The loader result reaches onCollectionLoaded through AnkiActivity.onLoadFinished (283-286) by virtual dispatch. The loader is an androidx library step: INFERRED, source not read. AnkiActivity.onLoadFinished@NoteEditor (receiver variant) has no inbound edge in out/, so the edge is written from the base onCreate, following the Reviewer precedent in parts/label_137.py.')

e('NoteEditor.onOptionsItemSelected', 'S_DLG_RESCHEDULE_CARD', 'ENTERS',
  'the reschedule menu item is tapped and the reschedule dialog opens',
  env=None,
  needs_state=STATE_NOTE,
  evidence='SRC com/ichi2/anki/NoteEditor.java:871-873; SRC com/ichi2/anki/NoteEditor.java:801-808; SRC com/ichi2/anki/AnkiActivity.java:337-340',
  note='showDialogFragment(NoteEditorRescheduleCard.newInstance()) opens the dialog (NoteEditor.java:873). The menu item is visible only when the editor is not adding a note (NoteEditor.java:803-808), so a note exists (STATE_NOTE). Precedent: DeckPicker.onOptionsItemSelected -> S_DLG_IMPORT ENTERS in parts/label_002.py:75-76. Without this edge the page has no inbound edge, and NoteEditorRescheduleCard$1.onInput (parts/label_044.py:57) and NoteEditor.onRescheduleCard stay UNRESOLVED.')

e('AbstractFlashcardViewer.displayCardAnswer', 'AbstractFlashcardViewer$18.run', 'FRAMEWORK',
  'the answer is shown and the auto-advance timer posts the show-question runnable (Handler.postDelayed)',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1863-1871, 1991, 2031-2033',
  note='displayCardAnswer posts mShowQuestionTask with mTimeoutHandler.postDelayed only when mPrefUseTimer and mWaitQuestionSecond > 0 (lines 2031-2033). The Handler delivers the runnable later, so the edge kind is FRAMEWORK. The gate is a user preference (auto-advance timer), not a build setting. The REGISTER edge from $18.<init> (parts/label_021.py:128) is not followed for reachability. No edge with this pair exists in graph_def.py or parts/*.py at the time of writing.')

# ---- part 141 (2026-10-30)
# AnkiDroid batch 141 (LABEL helper): 40 methods in 7 classes (BasicAudioFieldController, DeckOptions,
# DrawableContainer, FilteredDeckOptions$DeckPreferenceHack$Editor, LegendDrawable, Lookup, MyAccount).
# Labels: 40 REACHABLE, 0 UNREACHABLE. Every method already has a row and route edges in an earlier part
# (overlap: label_058, 027, 112, 029, 113, 052, 035; chart route through label_065/066). Edges written here:
#  - FilteredDeckOptions.onCreate -> S_FILTEREDDECKOPTIONS ENTERS: page-entry fix. The src is outside batch 141
#    (its row is label_029.md:11), and no ENTERS into S_FILTEREDDECKOPTIONS exists in graph_def.py or any parts/*.py.
# Constants used: STATE_DECK (graph_def.py:128). No new constants.

e('FilteredDeckOptions.onCreate', 'S_FILTEREDDECKOPTIONS', 'ENTERS',
  'the filtered deck options screen is live once onCreate has loaded the filtered deck and built the preference tree',
  needs_state=STATE_DECK,
  env=None,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:351-400',
  note='Page-entry edge from a method outside batch 141, because S_FILTEREDDECKOPTIONS had no ENTERS edge (grep of graph_def.py and parts/*.py). The page GUI and SYSTEM edges at graph_def.py:3797-3827 and the Editor write chain at 3858-3893 have no entry without it. The screen is built only for a dyn deck (lines 369-381); otherwise finish() at 357 or 372. Mirrors label_134.py:10 (DeckOptions.onCreate -> S_DECKOPTIONS ENTERS). If another part adds the same ENTERS, keep one copy.')

# ---- part 139 (2026-10-30)
# AnkiDroid batch 139 (LABEL helper). AnkiActivity (4 methods), AudioView (9), BarGraph (9),
# BasicTextFieldController (9), DeckPicker (9). 40 methods in total.
# Source row: graphs/AnkiDroid/scratch/batches_ai.tsv, part 139. The full row list (label, kind, reason, printed file:lines)
# is in graphs/AnkiDroid/parts/label_139.md. 39 methods are labelled REACHABLE, 1 is UNREACHABLE (DeckPicker.sendErrorReport).
#
# Route gaps in out/ that the edges below close:
# - AnkiActivity.onLoadFinished and AnkiActivity.onLoaderReset have no inbound edge. Written here: FRAMEWORK
#   AnkiActivity.startLoadingCollection -> onLoadFinished and -> onLoaderReset (LoaderManager is INFERRED).
# - S_DLG_DECKPICKER_CONTEXT, S_DLG_DECKPICKER_EXPORT_DONE and S_DLG_SYNC_ERROR have GUI edges in graph_def.py but no
#   inbound ENTERS edge. Written here: ENTERS from DeckPicker$4.onLongClick, DeckPicker$7.onPostExecute and
#   DeckPicker.showSyncErrorDialog(int,String).
#
# Already routed, not repeated here: AudioView listeners and BasicAudioFieldController (graph_def.py:6766-6787, 7168-7175);
# BasicTextFieldController listeners and callers (graph_def.py:7376-7442); MultimediaEditFieldActivity.onActivityResult
# RESULT edge (graph_def.py:7422); ChartView.onDraw from S_STATISTICS (graph_def.py:7657); Statistics.onCreate ->
# S_STATISTICS (graph_def.py:11196); S_DLG_DECKPICKER_DELETE_DECK (graph_def.py:897); DeckPickerContextMenu,
# DeckPickerExportCompleteDialog and SyncErrorDialog listeners (graph_def.py:5399, 5439, 5853);
# AnkiActivity.startLoadingCollection -> onCreateLoader (graph_def.py:10948).
# Automatic CALL edges come from auto_calls.json (bytecode) and are not written here.

# --- Loader callbacks: restartLoader in startLoadingCollection hands the result to onLoadFinished.
e('AnkiActivity.startLoadingCollection', 'AnkiActivity.onLoadFinished', 'FRAMEWORK',
  'the collection loader is restarted and the loader framework delivers the result to onLoadFinished',
  env=None,
  evidence='SRC com/ichi2/anki/AnkiActivity.java:254-262, 283-290',
  note='restartLoader(0, null, this) (AnkiActivity.java:261) makes this the LoaderCallbacks. The delivery to onLoadFinished is the support-library LoaderManager step: INFERRED, source not read. onLoadFinished then calls onCollectionLoaded (AnkiActivity.java:286) or onCollectionLoadError (AnkiActivity.java:288), which are automatic CALL edges. Precedent: parts/label_127.py:22 (onCreateLoader).')

e('AnkiActivity.startLoadingCollection', 'AnkiActivity.onLoaderReset', 'FRAMEWORK',
  'the loader framework resets the collection loader and calls onLoaderReset',
  env=None,
  evidence='SRC com/ichi2/anki/AnkiActivity.java:254-262, 294-296',
  note='INFERRED, source not read: restarting the loader with the same id replaces the existing loader instance, and the LoaderManager resets it. The body is empty (AnkiActivity.java:294-296), so this edge only gives reachability.')

# --- Page ENTERS: the deck context menu opens from the deck row long-press listener.
e('DeckPicker$4.onLongClick', 'S_DLG_DECKPICKER_CONTEXT', 'ENTERS',
  'a deck row is long-pressed: the deck context menu dialog opens',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:227-236',
  note='showDialogFragment(DeckPickerContextMenu.newInstance(deckId)) at DeckPicker.java:233. The listener has no guard. Existing GUI edges from S_DLG_DECKPICKER_CONTEXT: graph_def.py:985, 989, 5399.')

# --- Page ENTERS: the export-complete dialog opens from the export task's onPostExecute.
e('DeckPicker$7.onPostExecute', 'S_DLG_DECKPICKER_EXPORT_DONE', 'ENTERS',
  'the deck export task finishes with an export path: the export-complete dialog opens',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:321-332',
  note='The dialog opens only when exportPath is not null (DeckPicker.java:327-328); otherwise a toast is shown (DeckPicker.java:330). The export task reaches this listener through graph_def.py:1100 (exportApkg ASYNC). Existing GUI edges from S_DLG_DECKPICKER_EXPORT_DONE: graph_def.py:1035, 5439, 5446.')

# --- Page ENTERS: the sync error dialog opens from DeckPicker.showSyncErrorDialog(int,String).
e('DeckPicker.showSyncErrorDialog(int,String)', 'S_DLG_SYNC_ERROR', 'ENTERS',
  'a sync error dialog is requested with an id: the sync error dialog opens',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1048-1051, 1058-1062, 1281-1282',
  note='MISSING GATE MG4: the dialog id (SyncErrorDialog.DIALOG_*) is not modelled as a state, as in the existing S_DLG_SYNC_ERROR edges (graph_def.py:1039-1046). The not-logged-in path enters through showSyncErrorDialog(int) (DeckPicker.java:1050), called from sync() (DeckPicker.java:1282). Existing GUI edges from S_DLG_SYNC_ERROR: graph_def.py:1039, 1044, 5853.')

# --- UNREACHABLE: DatabaseErrorDialog case DIALOG_DB_ERROR (id 1) is the only path to sendErrorReport.
UNREACHABLE['DeckPicker.sendErrorReport'] = ('branch_never_taken',
    "The only caller is DatabaseErrorDialog$2.onNegative (DatabaseErrorDialog.java:115), inside case DIALOG_DB_ERROR (id 1, DatabaseErrorDialog.java:96-117). The dialog is created only by DeckPicker.showDatabaseErrorDialog(int) (DeckPicker.java:1026-1027), and every caller of that method passes a constant other than DIALOG_DB_ERROR (DeckPicker.java:431, 433, 597, 618, 1244; DatabaseErrorDialog.java:86, 110, 178-194, 232, 288, 317; DialogHandler.java:60). The one non-constant caller, DialogHandler.java:87, replays a message stored by AnkiActivity.java:365 from DatabaseErrorDialog.getDialogHandlerMessage (DatabaseErrorDialog.java:428-430), so it only ever replays a value that came from one of those constants. No value 1 enters the cycle, so the method is never entered. The existing DatabaseErrorDialog$2 entries (graph_def.py:5562-5577) are not duplicated here.",
    'SRC com/ichi2/anki/DeckPicker.java:431, 433, 597, 618, 1026-1027, 1244; SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:28, 47-52, 86, 96-117, 110, 178-194, 232, 288, 317, 358, 383, 428-430; SRC com/ichi2/anki/dialogs/DialogHandler.java:60, 85-87; SRC com/ichi2/anki/AnkiActivity.java:365',
    'SOURCE')

# ---- sup for part 139 (2026-10-30): DatabaseErrorDialog$2.onNegative is UNREACHABLE (branch_never_taken), so its automatic
# CALL edge to DeckPicker.sendErrorReport would give that UNREACHABLE method a live incoming edge. The UNREACHABLE entry stays.
sup(('DatabaseErrorDialog$2.onNegative', 'DeckPicker.sendErrorReport'))

# ---- UNREACHABLE and sup for DeckTask.waitToFinish() (2026-10-30 run decision; see HANDOFF_V2.md)
UNREACHABLE['DeckTask.waitToFinish()'] = ('no_trigger_in_app', 'The only caller under the source root is StudyOptionsFragment.onActivityResult at line 430 (the else branch of the DECK_OPTIONS result). That method is UNREACHABLE (framework_never_calls, UNREACHABLE entry for StudyOptionsFragment.onActivityResult in this file): the fragment starts its activities through getActivity(), so results do not reach the fragment. The no-argument overload therefore has no in-app trigger. waitToFinish(Integer) stays REACHABLE through Connection.java:260.', 'SRC com/ichi2/anki/StudyOptionsFragment.java:430; SRC com/ichi2/async/DeckTask.java:140-141; SRC com/ichi2/async/Connection.java:260', 'INFERRED')
sup(('StudyOptionsFragment.onActivityResult', 'DeckTask.waitToFinish()'))

# ---- route edges into the two AnkiStatsTaskHandler onCancelled methods (2026-10-30 run; the Statistics batch never wrote them)
e('Statistics$ChartFragment.checkAndUpdate', 'AnkiStatsTaskHandler$CreateChartTask.onCancelled', 'ASYNC',
  'a new chart request while the previous chart task is still running cancels that task, and the task reports onCancelled',
  env=None,
  evidence='SRC com/ichi2/anki/Statistics.java:522-546 (cancel at 543); SRC com/ichi2/anki/stats/AnkiStatsTaskHandler.java:117-119; FW-SRC core/java/android/os/AsyncTask.java:691-693',
  note='Gate: mCreateChartTask != null and not already cancelled (Statistics.java:542). AsyncTask.finish calls onCancelled only when the task is cancelled (AsyncTask.java:692-693); a task that has already finished ignores the cancel, so this is a route, not a guarantee.')

e('Statistics$ChartFragment.onDestroy', 'AnkiStatsTaskHandler$CreateChartTask.onCancelled', 'ASYNC',
  'the chart fragment is destroyed while its chart task is still running: onDestroy cancels the task, and the task reports onCancelled',
  env=None,
  evidence='SRC com/ichi2/anki/Statistics.java:571-576 (cancel at 574); SRC com/ichi2/anki/stats/AnkiStatsTaskHandler.java:117-119; FW-SRC core/java/android/os/AsyncTask.java:691-693',
  note='Gate: mCreateChartTask != null and not already cancelled (Statistics.java:573). Same AsyncTask.finish path as the checkAndUpdate edge.')

e('Statistics$OverviewStatisticsFragment.checkAndUpdate', 'AnkiStatsTaskHandler$CreateStatisticsOverview.onCancelled', 'ASYNC',
  'a new overview request while the previous overview task is still running cancels that task, and the task reports onCancelled',
  env=None,
  evidence='SRC com/ichi2/anki/Statistics.java:669-684 (cancel at 681); SRC com/ichi2/anki/stats/AnkiStatsTaskHandler.java:165-167; FW-SRC core/java/android/os/AsyncTask.java:691-693',
  note='Gate: mCreateStatisticsOverviewTask != null and not already cancelled (Statistics.java:680). Same AsyncTask.finish path as the chart edges.')

e('Statistics$OverviewStatisticsFragment.onDestroy', 'AnkiStatsTaskHandler$CreateStatisticsOverview.onCancelled', 'ASYNC',
  'the overview fragment is destroyed while its overview task is still running: onDestroy cancels the task, and the task reports onCancelled',
  env=None,
  evidence='SRC com/ichi2/anki/Statistics.java:689-694 (cancel at 692); SRC com/ichi2/anki/stats/AnkiStatsTaskHandler.java:165-167; FW-SRC core/java/android/os/AsyncTask.java:691-693',
  note='Gate: mCreateStatisticsOverviewTask != null and not already cancelled (Statistics.java:691). Same AsyncTask.finish path as the chart edges.')

# ---- part 142 (2026-10-30)
# AnkiDroid batch 142 (LABEL helper). AbstractFlashcardViewer$MyGestureDetector (5 methods), BasicImageFieldController (5),
# BeolingusParser (3), CollectionLoader (5), LoadPronounciationActivity$BackgroundPost (5), PickStringDialogFragment (5),
# StepsPreference (6), Whiteboard$UndoStack (6). 40 methods in total.
# Source row: graphs/AnkiDroid/scratch/batches_ai.tsv, part 142. The full row list (label, kind, reason, printed file:lines)
# is in graphs/AnkiDroid/parts/label_142.md. All 40 methods are labelled REACHABLE. No UNREACHABLE entries are written here.
#
# Route gap in out/: all five CollectionLoader methods are UNRESOLVED in out/methods.csv. The only loader entry is
# AnkiActivity.startLoadingCollection -> AnkiActivity.onCreateLoader (graph_def.py:10948, parts/label_127.py:22), and no
# edge reaches CollectionLoader.onStartLoading, onStopLoading or onReset. The chain onStartLoading -> loadInBackground ->
# deliverResult already exists (graph_def.py:7943, 7948) and is not repeated here.
# Written here (all three are support-library steps, INFERRED, source not read):
# - AnkiActivity.onCreateLoader -> CollectionLoader.onStartLoading (starts the loader; reaches the chain above).
# - AnkiActivity.onStop -> CollectionLoader.onStopLoading (a second route for onStopLoading, not via onReset).
# - NoteEditor.onDestroy -> CollectionLoader.onReset (the loader reset on destroy; the source is the NoteEditor override,
#   because AnkiActivity has no onDestroy override and no AnkiActivity.onDestroy node exists in method_list.json).
# The other 35 methods have existing routes (see parts/label_142.md for each row).

e('AnkiActivity.onCreateLoader', 'CollectionLoader.onStartLoading', 'FRAMEWORK',
  'the support-library LoaderManager starts the collection loader that onCreateLoader returned',
  env=None,
  evidence='SRC com/ichi2/anki/AnkiActivity.java:261, 276-278; SRC com/ichi2/async/CollectionLoader.java:47-55',
  note='startLoadingCollection calls restartLoader(0, null, this) (AnkiActivity.java:261). The LoaderManager asks this activity for the loader (onCreateLoader, 276-278), which returns new CollectionLoader(this). The support library then calls the protected onStartLoading (CollectionLoader.java:47-55), which calls forceLoad (line 54) unless the collection is locked (lines 49-52). The LoaderManager is a support-library step, not in fw_src: INFERRED, source not read. Edge not in graph_def.py or parts/*.py at the time of writing.')

e('AnkiActivity.onStop', 'CollectionLoader.onStopLoading', 'FRAMEWORK',
  'the activity stops and the loader manager stops the collection loader',
  env=None,
  evidence='SRC com/ichi2/anki/AnkiActivity.java:71-74; FW-SRC android/app/Activity.java:1858 (Activity.onStop, which does not reach loaders); SRC com/ichi2/async/CollectionLoader.java:58-62',
  note='AnkiActivity.onStop calls super.onStop() (AnkiActivity.java:72). The support-library FragmentActivity stops its LoaderManager, which calls Loader.stopLoading and then the protected onStopLoading (CollectionLoader.java:58-62). The framework Activity.onStop does not touch loaders, so the second hop is INFERRED: support-library source not read. This route does not depend on onReset. Edge not in graph_def.py or parts/*.py at the time of writing.')

e('NoteEditor.onDestroy', 'CollectionLoader.onReset', 'FRAMEWORK',
  'the note editor is destroyed and the loader manager resets its collection loader',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:792-793, 309; SRC com/ichi2/async/CollectionLoader.java:65-69',
  note='NoteEditor.onDestroy calls super.onDestroy() (NoteEditor.java:793). The support-library FragmentActivity.onDestroy destroys its LoaderManager, and the loader info calls Loader.reset, which calls onReset (CollectionLoader.java:65-69). NoteEditor.onCreate starts this loader (startLoadingCollection, NoteEditor.java:309). AnkiActivity has no onDestroy override and no AnkiActivity.onDestroy node exists in method_list.json, so the NoteEditor override is the source of the route. Support-library source not read: INFERRED. The out/ source_ref for NoteEditor.onDestroy (NoteEditor.java:960-969) is closeNoteEditor, not this method; the declaration is at line 792. Edge not in graph_def.py or parts/*.py at the time of writing.')

# ---- part 143 (2026-10-30)
# AnkiDroid batch 143 (LABEL helper). CardTemplateEditor (4 methods), CardTemplateEditor$2 (3), CardTemplateEditor$CardTemplateFragment$1 (4),
# CardTemplateEditor$TemplatePagerAdapter (4), Reviewer$BuryProvider (5), Reviewer$SuspendProvider (5), SlidingTabStrip (5),
# SlidingTabStrip$SimpleTabColorizer (5), XGrid (5). 40 methods in total.
# Source row: graphs/AnkiDroid/scratch/batches_ai.tsv, part 143. The full row list (label, kind, reason, printed file:lines)
# is in graphs/AnkiDroid/parts/label_143.md.
#
# All 40 methods were already labelled REACHABLE by other parts (parts 008, 025, 026, 076, 121; cross-references in 115, 125,
# 135, 137). They are not labelled again here, and no UNREACHABLE entries are written here.
#
# Route gaps in out/ that the edges below close (both methods were UNRESOLVED with incoming 0 in out/methods.csv,
# although parts/label_026.md labels them REACHABLE):
# - CardTemplateEditor$TemplatePagerAdapter.getItemPosition: the override returns POSITION_NONE (CardTemplateEditor.java:311-315).
#   It is reached when selectTemplate calls notifyDataSetChanged (CardTemplateEditor.java:286). Written here: FRAMEWORK
#   CardTemplateEditor.selectTemplate -> CardTemplateEditor$TemplatePagerAdapter.getItemPosition (same pattern as
#   Statistics$SectionsPagerAdapter.getItemPosition at graph_def.py:5195-5199).
# - CardTemplateEditor$TemplatePagerAdapter.getPageTitle: the title is read by SlidingTabLayout.populateTabStrip
#   (SlidingTabLayout.java:222). That path is shared with Statistics, so the edge is drawn from the page node, not from
#   onCollectionLoaded, to avoid a false route through the shared tab strip. Written here: FRAMEWORK
#   S_CARDTEMPLATEEDITOR -> CardTemplateEditor$TemplatePagerAdapter.getPageTitle (same pattern as graph_def.py:5207-5212).
#
# No new constants are defined here. The existing getItem and getItemId edges from S_CARDTEMPLATEEDITOR
# (graph_def.py:3562-3572, parts/label_026.py:51-57) are not repeated.

e('CardTemplateEditor.selectTemplate', 'CardTemplateEditor$TemplatePagerAdapter.getItemPosition', 'FRAMEWORK',
  'the tab set is refreshed after a template is added or removed (notifyDataSetChanged)',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:97-100, 282-286, 311-315',
  note='selectTemplate calls notifyChangeInPosition(1) (line 284) and then notifyDataSetChanged (line 286). The support-library PagerAdapter then calls getItemPosition for each page (INFERRED, support library, source not read). The override returns POSITION_NONE (line 314), so every page is rebuilt. selectTemplate is reached from the success branch at CardTemplateEditor.java:97-100 (the automatic CALL edge already in graph_def.py). No gate beyond that route. Precedent: Statistics.selectDropDownItem -> Statistics$SectionsPagerAdapter.getItemPosition (graph_def.py:5195-5199).')

e('S_CARDTEMPLATEEDITOR', 'CardTemplateEditor$TemplatePagerAdapter.getPageTitle', 'FRAMEWORK',
  'the tab strip draws the tab titles',
  env=None,
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:232, 288, 339-345; SRC com/ichi2/ui/SlidingTabLayout.java:158-166, 199-203, 222',
  note='Tab titles are set by SlidingTabLayout.populateTabStrip (SlidingTabLayout.java:222). populateTabStrip runs from setViewPager (SlidingTabLayout.java:158-164), which onCollectionLoaded calls at CardTemplateEditor.java:232 and selectTemplate calls at line 288. The edge is drawn from the page node, not from those methods (same design as graph_def.py:5207-5212 for Statistics). The receiver of getPageTitle at line 222 is typed PagerAdapter (SlidingTabLayout.java:200), so the dispatch to TemplatePagerAdapter.getPageTitle is INFERRED: the automatic app CALL does not resolve library-typed calls. parts/label_026.md labels this method CALL; the edge written here is FRAMEWORK for that reason.')

# ---- part 144 (2026-10-30)
# AnkiDroid batch 144 (LABEL helper, 2026-10-30). 40 methods in 10 classes, 4 each: ChartView, CompatV15$1, CompatV19,
# FilteredDeckOptions, FontMetricsWrap, HttpFetcher, LanguageListerBase, LoadPronounciationActivity$DownloadFileTask,
# SlidingTabLayout, Statistics.
# Source row: graphs/AnkiDroid/scratch/batches_ai.tsv, part 144. The full row list (label, kind, reason, printed
# file:lines) is in graphs/AnkiDroid/parts/label_144.md.
#
# Labels: all 40 methods already have REACHABLE rows in parts 029, 037, 047, 063, 066, 067, 072, 073, 075 and 125.
# None is labelled again here. No UNREACHABLE entry is written.
#
# Route gap closed here: build_report.txt lines 288-289 report "no path" for CompatV19.showViewWithAnimation and
# CompatV19.hideViewWithAnimation. Their only automatic CALL edges come from CompatV19$1.onSystemUiVisibilityChange
# (CompatV19.java:56-65, auto_calls.json exact). That listener has only a REGISTER edge from CompatV19$1.<init>
# (part 073, graph_def.py:8458-8461), and REGISTER does not count for reachability. The framework delivers the callback
# through View.dispatchSystemUiVisibilityChanged (View.java:22695-22700), which ViewRootImpl calls at ViewRootImpl.java:6007.
# The edge below starts from the registering method CompatV19.setFullScreen, the same pattern as the CompatV15 TTS
# listener edges (label_072.py:11-27). Its destination is a part 073 method. It is written here only so that the
# batch 144 methods have a route.
#
# Not written here: CompatV19$2.onAnimationEnd (build_report.txt line 292) has the same gap. It has only a REGISTER edge
# (graph_def.py:8463-8466), it is in part 073 and not in batch 144, so it is reported to the parent.
#
# Gate: the same missing gate as MG672 in part 073. No constant fits, so env and needs_state are unset.

e('CompatV19.setFullScreen', 'CompatV19$1.onSystemUiVisibilityChange', 'FRAMEWORK',
  'the framework calls the decor view listener that setFullScreen registers when the system bar visibility changes',
  evidence='SRC com/ichi2/compat/CompatV19.java:41-43; FW-SRC core/java/android/view/View.java:22684-22700; FW-SRC core/java/android/view/ViewRootImpl.java:5990-6007',
  note='MISSING GATE MG672 (as on the REGISTER edge in part 073): the callback runs only when the global system UI visibility changes (ViewRootImpl.java:6005-6007), for example after a touch reveals the bars. The app does not call it directly. The null guard at CompatV19.java:49-51 returns early when a view is missing.')

# ---- part 145 (2026-10-30)
# AnkiDroid batch 145 (LABEL helper). 40 methods in 13 classes, all already REACHABLE in other parts (no relabel, no UNREACHABLE entry here).
# Three route edges close batch methods that were UNRESOLVED in out/methods.csv. Details per method: graphs/AnkiDroid/parts/label_145.md.

e('AbstractFlashcardViewer.displayCardQuestion', 'AbstractFlashcardViewer$19.run', 'FRAMEWORK',
  'the answer timer runs for the question just shown: when the wait time expires the Handler runs the show-answer Runnable (mShowAnswerTask)',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1873-1881, 1947-1949',
  note='Gate: mPrefUseTimer is true and mWaitAnswerSecond > 0 (AbstractFlashcardViewer.java:1947). The Handler dispatch is INFERRED (android.os.Handler source not read). The source is the base node displayCardQuestion, reached from AbstractFlashcardViewer$9.onProgressUpdate (auto CALL). The variant nodes displayCardQuestion@Reviewer and @Previewer have no edge into $19.run in out/, so the timer route for those two screens is not covered here.')

e('Previewer.onCreate', 'Previewer.onCollectionLoaded', 'ASYNC',
  'the collection finishes loading after startLoadingCollection (called from the base onCreate through super.onCreate) and the loader delivers the result to onCollectionLoaded on the preview screen',
  env=None,
  evidence='SRC com/ichi2/anki/Previewer.java:32-39, 46-51; SRC com/ichi2/anki/AbstractFlashcardViewer.java:854, 859; SRC com/ichi2/anki/AnkiActivity.java:254-262, 283-286',
  note='The loader callback is androidx Loader, a library step: INFERRED (source not read). The source is Previewer.onCreate, not the base AbstractFlashcardViewer.onCreate used for Reviewer (graph_def.py:11172), because the base node is shared with Reviewer and an edge from it would route Reviewer loads into Previewer.onCollectionLoaded. The auto CALL Previewer.onCreate -> AbstractFlashcardViewer.onCreate (Previewer.java:39) carries the flow to startLoadingCollection. Previewer.initLayout follows from the auto CALL AbstractFlashcardViewer.onCollectionLoaded@Previewer -> Previewer.initLayout (AbstractFlashcardViewer.java:888), so no edge is written for it.')

e('VideoPlayer.onCreate', 'S_VIDEOPLAYER', 'ENTERS',
  'the video player screen is shown once onCreate has set up the surface holder and the sound',
  env=None,
  evidence='SRC com/ichi2/anki/VideoPlayer.java:37-48',
  note='Page ENTERS from a method of this batch, mirroring Previewer.onCollectionLoaded -> S_PREVIEWER (graph_def.py:5087). S_VIDEOPLAYER had no inbound edge in out/, so the surface callbacks (VideoPlayer.java:49-71), onConfigurationChanged (73-77) and VideoPlayer$1.onCompletion were all dead. VideoPlayer.onCreate is reached through VideoPlayer.<init> (LIFECYCLE), which the playVideo route starts (AbstractFlashcardViewer.java:2796-2803).')

# ---- part 147 (2026-10-30)
# AnkiDroid batch 147 (LABEL helper, 2026-10-30). 40 methods in 20 classes, 2 each: BasicTextFieldController$3$1, CardTemplateEditor$3,
# ColorWrap, CompatV19$1, CompatV19$2, CustomTabActivityHelper, DeckOptions$DeckPreferenceHack$Editor$1, DeckPicker$26,
# DeckPickerExportCompleteDialog$1, DeckTask, Decks, LanguageListerBase$1, LoadPronounciationActivity$1, Lookup$1, ModelFieldEditor$2,
# ModelFieldEditor$5, ModelFieldEditor$6, MyAccount$1, MyAccount$2, MyAccount$3. Row list: graphs/AnkiDroid/parts/label_147.md.
#
# Labels: each of the 40 methods already has a row in another part (exact name match), so no label is repeated here.
# No UNREACHABLE entry is written: no method is provably never entered.
#
# Route gaps: out/methods.csv marks 7 batch methods UNRESOLVED. The six edges below close six of them:
#   CompatV19$2.onAnimationEnd (part 073 has a REGISTER edge only, which gives no path),
#   DeckPicker$26.onDismissed and DeckPicker$26.onShown (part 005 names the route in text but writes no edge),
#   DeckTask.onCancelled (part 070 names the route in text but writes no edge),
#   CustomTabActivityHelper.onServiceConnected and CustomTabActivityHelper.onServiceDisconnected (part 073 relies on the
#   ServiceConnection wrapper methods, which have no inbound edge; these two edges skip the wrapper, see the notes).
# DeckTask.waitToFinish() has no reachable caller; its UNREACHABLE entry and suppression are at the end of this file.
# CompatV19$1.onSystemUiVisibilityChange is already REACHABLE through the part 144 edge (CompatV19.setFullScreen), not written here.

e('CompatV19.hideViewWithAnimation', 'CompatV19$2.onAnimationEnd', 'FRAMEWORK',
  'the animator calls the end listener that hideViewWithAnimation sets, when the fade-out ends',
  env=None,
  evidence='SRC com/ichi2/compat/CompatV19.java:78-88; FW-SRC core/java/android/view/ViewPropertyAnimator.java:375-377, 1111-1123',
  note='hideViewWithAnimation sets the listener at CompatV19.java:82 and starts the fade. ViewPropertyAnimator stores the listener in setListener (375-377). Its inner listener onAnimationEnd (1111-1112) calls mListener.onAnimationEnd (1122). The library makes this call, so the kind is FRAMEWORK. Route to the source: CompatV19$1.onSystemUiVisibilityChange calls hideViewWithAnimation (automatic CALL, CompatV19.java:62, 64-65), and part 144 reaches that listener from CompatV19.setFullScreen. MISSING GATE MG672 applies to the chain start, as in parts 073 and 144. The toolbar call at line 62 has no preference gate; the fullscreenMode preference (CompatV19.java:39) gates only lines 63-65. No constant fits, so env is unset.')

e('DeckPicker.handleDeckSelection', 'DeckPicker$26.onDismissed', 'FRAMEWORK',
  'the snackbar that handleDeckSelection shows calls the show/hide callback when it is dismissed',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1746-1754, 1773-1778, 1786-1794, 2151-2168; SRC com/ichi2/anki/UIUtils.java:56-60, 64-80; INFERRED Snackbar.Callback dispatch (support library, no source in the dataset)',
  note='handleDeckSelection (DeckPicker.java:1717) passes mSnackbarShowHideCallback to UIUtils.showSnackbar in three branches: 1746-1754 (study limit reached), 1773-1778 (empty deck) and 1786-1794 (empty schedule). The int overload at UIUtils.java:56-60 delegates to the String overload, which calls sb.setCallback at lines 79-80. The Snackbar dispatch is library code and INFERRED. The empty-deck branch carries MISSING GATE MG6 (label_005.md). handleDeckSelection is REACHABLE in out/methods.csv. No preference or constant gate.')

e('DeckPicker.handleDeckSelection', 'DeckPicker$26.onShown', 'FRAMEWORK',
  'the snackbar that handleDeckSelection shows calls the show/hide callback when it is shown',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1746-1754, 1773-1778, 1786-1794, 2151-2168; SRC com/ichi2/anki/UIUtils.java:56-60, 64-80; INFERRED Snackbar.Callback dispatch (support library, no source in the dataset)',
  note='Same three snackbar branches and the same callback as the onDismissed edge (see that note). The onShown body disables the add-note button (DeckPicker.java:2162-2168). No preference or constant gate.')

e('DeckTask.cancelTask()', 'DeckTask.onCancelled', 'ASYNC',
  'cancel(true) on the running DeckTask makes the framework call the task listener onCancelled',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:168-178 (cancel(true) at 172), 181-186 (cancelTask(int) calls cancelTask() at 184), 367-370; FW-SRC core/java/android/os/AsyncTask.java:525-528, 345-350, 369-376, 691-698, 712, 462-464, 479-480',
  note='cancel(true) sets mCancelled and cancels the future (AsyncTask.java:525-528). The future calls done(), which posts a result through postResultIfNotInvoked (345-350; the CancellationException catch branch is not reprinted in this run). postResult sends MESSAGE_POST_RESULT (369-376), and the handler calls finish (712). finish calls onCancelled(result) when isCancelled (691-693), which calls onCancelled() (462-464). DeckTask.java:368-370 overrides that method and calls mListener.onCancelled() (369). cancelTask() runs only when the latest task is still running (DeckTask.java:171), and cancelTask(int) allows it only for the matching task type (183). Callers: out/methods.csv marks cancelTask() REACHABLE through cancelTask(int). The auto CALL edges out of DeckTask.onCancelled to the listeners whose tasks are never cancelled are suppressed by sup tuples in graph_def.py. CardBrowser$16.onCancelled (search listener, CardBrowser.java:1051, 1080) and CardBrowser$17.onCancelled (render listener, CardBrowser.java:1085, 1114) are not suppressed. Their tasks are cancelled in the app (CardBrowser.java:528-529, 796-797, 1155-1156), so they become live by design. The mapping is inferred from javac anonymous-class order: $13-$15 match the named handlers at 900, 1000 and 1028 by the same count.')

e('CustomTabActivityHelper.bindCustomTabsService', 'CustomTabActivityHelper.onServiceConnected', 'FRAMEWORK',
  'the Custom Tabs service connects after the bind, and the framework calls back into the helper',
  env=None,
  evidence='SRC com/ichi2/compat/customtabs/CustomTabActivityHelper.java:96-104, 120-125; SRC com/ichi2/compat/customtabs/ServiceConnection.java:31-39; INFERRED CustomTabsClient.bindCustomTabsService (support library, no source in the dataset)',
  note='bindCustomTabsService creates ServiceConnection(this) (CustomTabActivityHelper.java:102) and binds it (line 103). The framework calls the ServiceConnection wrapper, which calls the helper callback (ServiceConnection.java:36-38). This edge skips the wrapper because the wrapper methods are outside batch 147. ServiceConnection.onCustomTabsServiceConnected is UNRESOLVED with 0 incoming in out/methods.csv; its owner needs a FRAMEWORK edge from bindCustomTabsService into it. The wrapper-to-helper CALL edge is automatic and stays in place. Gates: bindCustomTabsService returns at line 97 when mClient is already set and at line 100 when no browser package is found (MG673, label_073.md). No constant fits, so env is unset. bindCustomTabsService is REACHABLE in out/methods.csv from AnkiActivity.onStart (AnkiActivity.java:67).')

e('CustomTabActivityHelper.bindCustomTabsService', 'CustomTabActivityHelper.onServiceDisconnected', 'FRAMEWORK',
  'the Custom Tabs service disconnects, and the framework calls back into the helper',
  env=None,
  evidence='SRC com/ichi2/compat/customtabs/CustomTabActivityHelper.java:96-104, 127-131; SRC com/ichi2/compat/customtabs/ServiceConnection.java:41-45; INFERRED CustomTabsClient.bindCustomTabsService (support library, no source in the dataset)',
  note='Same shortcut as the connect edge. The framework calls the wrapper onServiceDisconnected (ServiceConnection.java:41-44), which calls the helper callback at line 44. ServiceConnection.onServiceDisconnected is UNRESOLVED with 0 incoming in out/methods.csv and is outside batch 147; its owner needs the FRAMEWORK edge from bindCustomTabsService. MG673 (label_073.md) applies as on the connect edge.')

# ---- part 146 (2026-10-30)
# AnkiDroid batch 146 (LABEL helper). 40 methods: AbstractFlashcardViewer$12 to $17, $2.run, AbstractFlashcardViewer$MyWebView
# (two callbacks), AudioView (4 methods), Statistics (9), SyncErrorDialog$3 (3), TranslationActivity$BackgroundPost (3), Tuc (3),
# WidgetStatus$UpdateDeckStatusAsyncTask (3). Full row list: graphs/AnkiDroid/parts/label_146.md.
# All 40 methods are already REACHABLE in other parts (copied labels, no relabel). No UNREACHABLE entry is written here.
#
# Route edges written here close the gaps where a batch 146 method had no non-REGISTER route (build_report "no path").
# Route edges 9 and 10: the two WidgetStatus AsyncTask edges (WidgetStatus.update -> doInBackground, doInBackground -> onPostExecute).
# At 14:02 a grep of graph_def.py and parts/ found neither edge (label_145.py no longer has them), so both are written here, kind ASYNC.
#
# Route edge 1: the SD-card eject receiver on the reviewer screen. Precedent: S_CARDBROWSER -> CardBrowser$18.onReceive (SYSTEM).
# AbstractFlashcardViewer.java:879-890 (onCollectionLoaded calls registerExternalStorageListener at 884);
# :1125-1137 (guard 1126, receiver onReceive 1129-1133, eject check 1130, registerReceiver 1137).
e('S_REVIEWER', 'AbstractFlashcardViewer$12.onReceive', 'SYSTEM',
  'the SD card is ejected while the card reviewer is open (the eject receiver is registered when the collection loads)',
  env=ENV_SDCARD_EVENT,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:879-890, 1125-1137',
  note='Page edge. The reviewer screen owns the receiver, so the page is the source (same shape as the CardBrowser precedent). The receiver ignores every action except MEDIA_EJECT (1130-1131). The REGISTER edge registerExternalStorageListener -> $12.onReceive is not followed for reachability. label_021 named registerExternalStorageListener as the source of this SYSTEM route; the page is used here.')

# Route edge 2: the delete-note dialog confirm. AbstractFlashcardViewer.java:1239-1256 (builder, callback 1248-1254, onPositive 1250-1253,
# dismiss(DELETE_NOTE) at 1252); :2565-2569 (executeCommand GESTURE_DELETE calls showDeleteNoteDialog at 2568).
e('S_REVIEWER', 'AbstractFlashcardViewer$13.onPositive', 'GUI',
  'the user confirms Delete on the delete-note dialog that showDeleteNoteDialog shows',
  gui=['open the delete-note dialog (a swipe or gesture that runs executeCommand GESTURE_DELETE), then tap Delete'],
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1239-1256, 2565-2569',
  note='The dialog is MaterialDialog (library code, not in fw_src: INFERRED). The dismiss call is at 1252. The REGISTER edge showDeleteNoteDialog -> $13.onPositive (graph_def.py:3498) is not followed for reachability. showDeleteNoteDialog itself is upstream REACHABLE (build_report).')

# Route edge 3: the lookup icon on the reviewer screen. AbstractFlashcardViewer.java:1412-1430 (listener 1418-1428, clipboardHasText() check 1423);
# :1217-1227 (showLookupButtonIfNeeded: icon visible only when the clipboard holds text and Lookup.isAvailable()).
e('S_REVIEWER', 'AbstractFlashcardViewer$14.onClick', 'GUI',
  'tap the lookup icon on the reviewer screen (the icon is shown when the clipboard holds text)',
  gui=['copy text to the clipboard, then tap the lookup icon that appears above the card'],
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1217-1227, 1412-1430',
  note='MISSING GATE: the icon is visible only when the clipboard holds text and Lookup.isAvailable() (1217-1227). No STATE constant fits clipboard content, so needs_state is not set. onClick re-checks clipboardHasText() at 1423 and then calls lookUp().')

# Route edges 4 and 5: the card WebView after fillFlashcard loads the card page. AbstractFlashcardViewer.java:2269-2290
# (loadDataWithBaseURL at 2274 for mNextCard and at 2284 for mCard); :1541-1546 (onPageFinished loads javascript:onPageFinished());
# :1458-1466 (shouldOverrideUrlLoading, playsound branch 1459-1465). FW-SRC core/java/android/webkit/WebViewClient.java:49, 106-107.
e('AbstractFlashcardViewer.fillFlashcard', 'AbstractFlashcardViewer$15.onPageFinished', 'FRAMEWORK',
  'the card page finishes loading in the WebView after fillFlashcard calls loadDataWithBaseURL',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1541-1546, 2269-2290; FW-SRC core/java/android/webkit/WebViewClient.java:106-107',
  note='The load is the fillFlashcard step (lines 2274 and 2284). The WebView dispatch of onPageFinished is not in fw_src (INFERRED). The REGISTER edge $15.<init> -> $15.onPageFinished is not followed for reachability.')

e('AbstractFlashcardViewer.fillFlashcard', 'AbstractFlashcardViewer$15.shouldOverrideUrlLoading', 'FRAMEWORK',
  'after the card page is loaded, a link in the card is tapped and the WebView asks shouldOverrideUrlLoading',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1458-1466, 2269-2290; FW-SRC core/java/android/webkit/WebViewClient.java:49',
  note='MISSING GATE: a link must be tapped on the card page. The playsound: and typeentertext: links come from the card HTML and page JavaScript, which are not in this dataset (MG153 and MG154 in label_021). The WebView dispatch is not in fw_src (INFERRED). The class overrides the deprecated overload that WebViewClient.java:49 declares.')

# Route edges 6 and 7: the type-answer field on the reviewer screen. AbstractFlashcardViewer.java:1686-1698 (answer field visible only when
# typeAnswer() at 1688; Done calls displayCardAnswer 1692-1693); :1699-1709 (key listener; ACTION_UP with ENTER 1702-1703, displayCardAnswer 1704);
# :1715-1717 (mShowTypeAnswerField from the writeAnswersDisable preference); :2326-2328 (typeAnswer). FW-SRC TextView.java:7429-7432
# (editor action dispatch), View.java:11707-11710 (key listener dispatch).
e('S_REVIEWER', 'AbstractFlashcardViewer$16.onEditorAction', 'FRAMEWORK',
  'press Done (the IME action) in the type-the-answer field on the reviewer screen',
  needs_state=STATE_SETTINGS,
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1686-1698, 1715-1717, 2326-2328; FW-SRC core/java/android/widget/TextView.java:7429-7432',
  note='Gate: the field is visible only when typeAnswer() is true (1688, 2326-2328). mShowTypeAnswerField is false when the writeAnswersDisable preference is on or useInputTag is on (1716-1717). STATE_SETTINGS models that preference. The card also needs a type-answer field (mTypeCorrect set from the note at grep line 679): that is card content, not a STATE constant (INFERRED). IME_ACTION_DONE calls displayCardAnswer (1692-1693).')

e('S_REVIEWER', 'AbstractFlashcardViewer$17.onKey', 'FRAMEWORK',
  'press Enter (key up) with the type-the-answer field focused on the reviewer screen',
  needs_state=STATE_SETTINGS,
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1699-1709, 1715-1717, 2326-2328; FW-SRC core/java/android/view/View.java:11707-11710',
  note='Same field gate as onEditorAction (typeAnswer() at 1688; preference at 1716-1717). ACTION_UP with KEYCODE_ENTER or NUMPAD_ENTER (1702-1703) calls displayCardAnswer (1704). The key dispatch is View.java:11707-11710 (FRAMEWORK, printed).')

# Route edge 8: the touch layer on the reviewer screen. It is written here because $2.run (in this batch) is reached only through
# $6.onTouch (graph_def.py:3210, FRAMEWORK). $6.onTouch belongs to batch 021, not batch 146. AbstractFlashcardViewer.java:1331-1333
# (touch layer gets mGestureListener at 1333), :428-438 (onTouch; ACTION_DOWN starts the 800 ms long-click timer at 437-438).
e('S_REVIEWER', 'AbstractFlashcardViewer$6.onTouch', 'GUI',
  'touch the card area of the reviewer screen (the touch layer carries the gesture listener)',
  gui=['touch and hold or move a finger on the card area of the reviewer screen'],
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1331-1333, 428-438',
  note='Overlap risk: $6.onTouch is a batch 021 method (label_021.md lead "S_REVIEWER -> $6.onTouch" was left to the screen-part owner, who has not written it). The gesture detector runs first (431) and the long-click timer starts at 437-438. The MyGestureDetector edges from S_REVIEWER (graph_def.py:3347-3371) are upstream of the same listener and are not duplicated here.')

# Route edge 9: WidgetStatus.update starts the task at WidgetStatus.java:61 (execute(context)), inside the gate at 57-58
# (widgetSmallEnabled or minimumCardsDueForNotification set, and the previous task null or FINISHED). Caller -> doInBackground, ASYNC.
e('WidgetStatus.update', 'WidgetStatus$UpdateDeckStatusAsyncTask.doInBackground', 'ASYNC',
  'the widget or notification update starts its AsyncTask (execute with the context) when the small widget or the notification is enabled',
  needs_state=STATE_SETTINGS,
  env=None,
  evidence='SRC com/ichi2/widget/WidgetStatus.java:53-61',
  note='Gate: sSmallWidgetEnabled (widgetSmallEnabled, line 55) or sNotificationEnabled (minimumCardsDueForNotification below 1000000, line 56), and the previous task is null or FINISHED (57-58). The SD-card check at 89-91 is inside doInBackground, so it limits updateCounts (93), not this edge. The entry into update is not part of this edge.')

# Route edge 10: the AsyncTask result returns to onPostExecute. WidgetStatus.java:85-98 (doInBackground returns at 90 without the SD card, and at 97 otherwise);
# :102-110 (onPostExecute: MetaDB.storeSmallWidgetStatus at 105, then the widget start at 106-110). FW-SRC core/java/android/os/AsyncTask.java:333
# (doInBackground call), 339 (postResult in finally), 369-375 (postResult sends MESSAGE_POST_RESULT), 691-695 (finish calls onPostExecute when not cancelled).
e('WidgetStatus$UpdateDeckStatusAsyncTask.doInBackground', 'WidgetStatus$UpdateDeckStatusAsyncTask.onPostExecute', 'ASYNC',
  'the worker finishes doInBackground and the framework posts the result back to the UI thread, which calls onPostExecute',
  env=None,
  evidence='SRC com/ichi2/widget/WidgetStatus.java:85-98, 102-110; FW-SRC core/java/android/os/AsyncTask.java:333, 339, 369-375, 691-695',
  note='Framework route, printed. The Handler dispatch of MESSAGE_POST_RESULT is INFERRED (source not read). onPostExecute runs whether or not the SD card is mounted, because both returns in doInBackground (90, 97) go through postResult. The INTENT edges out of onPostExecute (graph_def.py:8740, 8748) belong to label_080. label_145.py had kind FRAMEWORK for this edge; it is not duplicated here.')

# ---- part 148 (2026-10-30)
# AnkiDroid batch 148 (LABEL helper, 2026-10-30). 40 methods: AbstractFlashcardViewer$20, $21, $3 to $7, $AnkiDroidWebChromeClient,
# $MyWebView$1 and $2; AnkiDroidWidgetSmall$UpdateService$1; AnkiStatsTaskHandler (two onCancelled, setStatType); AudioField;
# AudioView; NoteEditor$JSONNameComparator; ReadText; Reviewer$1; ServiceConnection; Sound; StrokeWrap; SyncErrorDialog$6;
# TranslationActivity$1; VideoPlayer$1; WidgetStatus (fetchDue, fetchSmall). Row list: graphs/AnkiDroid/parts/label_148.md.
#
# Labels: each method already has a REACHABLE row in another part (exact name match), so labels are copied, not repeated here.
# No UNREACHABLE entry: no method in this batch is provably dead.
#
# Route ownership. Written here, because the target is in this batch and no other part writes the edge:
#   AbstractFlashcardViewer.initTimer -> $20.onChronometerTick (FRAMEWORK), AbstractFlashcardViewer.delayedHide -> $21.handleMessage (FRAMEWORK),
#   CustomTabActivityHelper.bindCustomTabsService -> the two ServiceConnection callbacks (FRAMEWORK).
# Not written here, owned by other batches (their edges close these methods when written):
#   WidgetStatus.update -> UpdateDeckStatusAsyncTask.doInBackground and doInBackground -> onPostExecute (ASYNC) belong to part 080
#   (label_080.py header; label_140, label_135, label_146 notes). They make UpdateService$1.<init>, fetchSmall and fetchDue reachable.
#   The cancel(true) ASYNC edges into the two AnkiStatsTaskHandler onCancelled methods belong to the Statistics batch
#   (graph_def.py:7590-7594 note; parts 144 and 145).
#   VideoPlayer.onCreate -> S_VIDEOPLAYER (ENTERS) is written in part 145 and is already in out/. It makes VideoPlayer$1.<init>,
#   VideoPlayer$1.onCompletion, Sound.getMediaCompletionListener and Sound.notifyConfigurationChanged reachable.
# Automatic CALL edges come from auto_calls.json and are not written here. No MG id is used.

# --- Chronometer tick (initTimer sets the listener at AbstractFlashcardViewer.java:1901; the framework ticks the chronometer).
e('AbstractFlashcardViewer.initTimer', 'AbstractFlashcardViewer$20.onChronometerTick', 'FRAMEWORK',
  'the card timer ticks while it runs, and the tick listener checks the time limit',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1883-1910; INFERRED android.widget.Chronometer tick dispatch (Chronometer source is not in fw_src)',
  note='initTimer shows the timer only when mCurrentCard.showTimer() is true (line 1885), starts the chronometer (line 1893), and sets the anonymous OnChronometerTickListener (line 1901). The framework calls onChronometerTick on each tick (INFERRED). The gate is the show-timer option read by showTimer(), so it is STATE_SETTINGS.')

# --- Delayed full-screen hide (delayedHide posts a message to mFullScreenHandler; Handler dispatches it to handleMessage).
e('AbstractFlashcardViewer.delayedHide', 'AbstractFlashcardViewer$21.handleMessage', 'FRAMEWORK',
  'a delayed full-screen hide message runs handleMessage on the UI thread',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:2763-2775; FW-SRC core/java/android/os/Handler.java:558-564, 95-98',
  note='delayedHide removes pending messages and calls sendEmptyMessageDelayed(0, delayMillis) (AbstractFlashcardViewer.java:2773-2774). Handler.dispatchMessage (Handler.java:95-98) calls handleMessage. The body calls setFullScreen only when mPrefFullscreenReview > 0 (line 2766-2767). That is a body condition, not a route gate.')

# --- Custom Tabs service connection (the wrapper class forwards the support-library callbacks to the helper).
e('CustomTabActivityHelper.bindCustomTabsService', 'ServiceConnection.onCustomTabsServiceConnected', 'FRAMEWORK',
  'the support library reports the Custom Tabs service connection after the bind call',
  env=None,
  evidence='SRC com/ichi2/compat/customtabs/CustomTabActivityHelper.java:96-104; SRC com/ichi2/compat/customtabs/ServiceConnection.java:27, 36-39; INFERRED CustomTabsClient.bindCustomTabsService (support library source is not in fw_src)',
  note='bindCustomTabsService creates new ServiceConnection(this) (CustomTabActivityHelper.java:102) and binds it with CustomTabsClient.bindCustomTabsService (line 103). The support library calls the ServiceConnection.onServiceConnected override (INFERRED). The wrapper class extends CustomTabsServiceConnection (ServiceConnection.java:27), and onCustomTabsServiceConnected (lines 36-39) forwards to the helper. Part 147 writes the helper callbacks directly and skips these wrappers.')

e('CustomTabActivityHelper.bindCustomTabsService', 'ServiceConnection.onServiceDisconnected', 'FRAMEWORK',
  'the support library reports that the Custom Tabs browser service disconnected',
  env=None,
  evidence='SRC com/ichi2/compat/customtabs/CustomTabActivityHelper.java:96-104; SRC com/ichi2/compat/customtabs/ServiceConnection.java:42-45; INFERRED CustomTabsClient.bindCustomTabsService (support library source is not in fw_src)',
  note='The same bind as the connect edge. The support library calls the wrapper onServiceDisconnected (INFERRED). The wrapper (ServiceConnection.java:42-45) calls connectionCallback.onServiceDisconnected when the callback is set (line 44).')

# ---- part 150 (2026-10-30)
# AnkiDroid batch 150 (LABEL helper). 32 whole-class methods (scratch/batches_ai.tsv row 150; names in scratch/h150/methods.txt).
# All 32 were already labelled REACHABLE by other parts (overlap column in parts/label_150.md). They are not labelled again here.
# No UNREACHABLE entries: none of the 32 is provably never entered.
#
# Four e() edges below close route gaps that out/methods.csv reports as UNRESOLVED with incoming 0:
# Sched$1.compare, Sched$DeckDueTreeNode.compareTo, Template$1.compare (comparators and Comparable hooks dispatched by
# java.util.Collections.sort; JDK source not read) and StudyOptionsFragment.onDestroy (destroyed by FragmentManager on replace;
# support-library source not read). Checked before writing: no existing edge in graph_def.py or parts/*.py has any of the four as dst.

e('Sched._fillLrn', 'Sched$1.compare', 'CALL',
  'two or more learning cards are due and the learning queue is refilled',
  env=None,
  needs_state=STATE_CARDS,
  evidence='SRC com/ichi2/libanki/Sched.java:773-805 (query 783-788; Collections.sort at 793; anonymous Comparator 793-798; compare 795-797)',
  note='java.util.Collections.sort (JDK source not read: INFERRED) calls compare only for a list of two or more entries. The gate is two or more learning cards with queue = 1 and due < mDayCutoff, returned by the query at lines 786-788 (capped by mReportLimit). _fillLrn is called at Sched.java:814 (existing route). Precedent for a comparator dispatched by Collections.sort: Decks$1.compare (graph_def.py:9010).')

e('Sched._groupChildren', 'Sched$DeckDueTreeNode.compareTo', 'CALL',
  'the deck tree is built (deckDueTree) and the deck list has two or more entries',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/libanki/Sched.java:432-433, 437-446, 2502, 2532-2551',
  note='Collections.sort(grps) at Sched.java:443 calls compareTo on the Comparable element type (JDK source not read: INFERRED). The JDK calls compareTo only for a list of two or more nodes, so the gate is one deck beyond the first (assumed: the Default deck is listed, not checked). The sort is reached from deckDueTree (Sched.java:432-433). Precedent: Stats$1.compare (graph_def.py:9323).')

e('Template.render_unescaped', 'Template$1.compare', 'CALL',
  'a field tag with two or more modifiers that is not itself a context key (a two-colon tag in a note type template)',
  env=None,
  needs_state=STATE_NOTE,
  evidence='SRC com/ichi2/libanki/template/Template.java:199-200, 209-218, 228-240 (Collections.sort at 229; compare at 233-238)',
  note='MG1022: the gate is a tag with two or more modifiers (mods has two or more entries, line 216). No stock template in src/main has such a tag (existing label note). Collections.reverse(mods) at line 228 and Collections.sort at line 229 call compare only for two or more entries (JDK source not read: INFERRED). needs_state is STATE_NOTE because a card with such a template renders only when a note exists. render_unescaped is called at Template.java:169 and 188 (existing route).')

e('DeckPicker.loadStudyOptionsFragment', 'StudyOptionsFragment.onDestroy', 'FRAMEWORK',
  'a second load replaces the StudyOptionsFragment that is still in the studyoptions container of the tablet layout',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1651-1655, 365-367; SRC res/layout-xlarge/homescreen.xml (id studyoptions_fragment); SRC com/ichi2/anki/StudyOptionsFragment.java:195-202; FW-SRC core/java/android/app/FragmentManager.java:1407-1433; FW-SRC core/java/android/app/Fragment.java:2761-2768',
  note='ft.replace at DeckPicker.java:1654 removes the fragment already in that container, and the FragmentManager destroys it. Framework analog: FragmentManager.java:1407-1433 (moveToState) and Fragment.java:2768 (performDestroy calls onDestroy). DeckPicker uses the support-library FragmentManager (getSupportFragmentManager), whose source is not read, so the mechanism is INFERRED. The container id exists only in the xlarge layout (homescreen.xml) and is found at DeckPicker.java:365; mFragmented (367) is true only there. The activity-finish route to onDestroy is not written here (existing LIFECYCLE label; no edge for it).')

# ---- part 149 (2026-10-30)
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
  guard='BackupManager.enoughDiscSpace is false (not enough disc space for backup)',
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
