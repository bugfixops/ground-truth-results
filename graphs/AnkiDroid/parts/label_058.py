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
