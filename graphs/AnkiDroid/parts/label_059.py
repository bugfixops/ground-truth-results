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
