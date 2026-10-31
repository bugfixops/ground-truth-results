# AnkiDroid batch 057 (LABEL helper). AudioView (31 methods) and BeolingusParser (4 methods): 35 methods.
# The full row list is in graphs/AnkiDroid/parts/label_057.md.
#
# Route ownership:
# - Automatic CALL edges (constructors and field-initializer listeners, the notify* fan-out, the recorder route from
#   BasicAudioFieldController.createUI, the processPostFinished calls into BeolingusParser, and the in-class calls such as
#   RecordButton$1.onClick -> notifyStopRecord) come from auto_calls.json. They are not written here.
# - GUI edges from the page S_MULTIMEDIA_EDIT_FIELD to the play, record and stop listeners (the destinations are in this batch).
# - FRAMEWORK edge from the IDLE play branch to the completion listener (MediaPlayer dispatch, MediaPlayer.java:3235-3240).
#
# Gates: ENV_PERM_RECORD (RECORD_AUDIO granted: the audio view and its buttons exist only then).
# MG512: a playable recording must exist in the audio field before the completion dispatch can run.

e('S_MULTIMEDIA_EDIT_FIELD', 'AudioView$PlayPauseButton$1.onClick', 'GUI',
  'tap the play button of an audio field in the multimedia field editor',
  env=ENV_PERM_RECORD,
  gui=['tap the play button of an audio field in the multimedia field editor'],
  evidence='SRC com/ichi2/anki/multimediacard/AudioView.java:213-216, 290; SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:128-133; FW-SRC core/java/android/view/View.java:6289-6294',
  note='The play listener is set in PlayPauseButton.<init> (AudioView.java:290). The audio view and its buttons are created only when RECORD_AUDIO is granted (MultimediaEditFieldActivity.java:128-133). Dispatch is View.performClick (View.java:6289-6294).')

e('S_MULTIMEDIA_EDIT_FIELD', 'AudioView$RecordButton$1.onClick', 'GUI',
  'tap the record button of an audio field in the multimedia field editor',
  env=ENV_PERM_RECORD,
  gui=['tap the record button of an audio field in the multimedia field editor'],
  evidence='SRC com/ichi2/anki/multimediacard/AudioView.java:357-362, 437; SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:128-133; FW-SRC core/java/android/view/View.java:6289-6294',
  note='The record listener is set in RecordButton.<init> (AudioView.java:437). The recorder view is created only when RECORD_AUDIO is granted (MultimediaEditFieldActivity.java:128-133). Dispatch is View.performClick (View.java:6289-6294).')

e('S_MULTIMEDIA_EDIT_FIELD', 'AudioView$StopButton$1.onClick', 'GUI',
  'tap the stop button of an audio field in the multimedia field editor',
  env=ENV_PERM_RECORD,
  gui=['tap the stop button of an audio field in the multimedia field editor'],
  evidence='SRC com/ichi2/anki/multimediacard/AudioView.java:316-317, 338; SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:128-133; FW-SRC core/java/android/view/View.java:6289-6294',
  note='The stop listener is set in StopButton.<init> (AudioView.java:338). The audio view and its buttons are created only when RECORD_AUDIO is granted (MultimediaEditFieldActivity.java:128-133). The action runs only in PAUSED or PLAYING (AudioView.java:316-323).')

e('AudioView$PlayPauseButton$1.onClick', 'AudioView$PlayPauseButton$1$1.onCompletion', 'FRAMEWORK',
  'MediaPlayer finishes playing the audio field recording and dispatches the completion listener',
  evidence='SRC com/ichi2/anki/multimediacard/AudioView.java:224-226; FW-SRC media/java/android/media/MediaPlayer.java:3235-3240',
  note='MISSING GATE MG512: a playable recording must exist in the audio field before play is tapped, so that playback runs to the end. No predefined STATE or ENV kind covers a recorded file. The completion listener is set in the IDLE play branch (AudioView.java:226). The dispatch is MediaPlayer.java:3235-3240 (MEDIA_PLAYBACK_COMPLETE). env and needs_state unset.')

UNREACHABLE['AudioView.createPlayerInstance'] = ('no_trigger_in_app', 'No call site in src/main. grep for createPlayerInstance over src/main (java and res) finds only the definition at AudioView.java:79. The constructor it calls stays reachable through AudioView.java:125.', 'com/ichi2/anki/multimediacard/AudioView.java:79-82', 'SOURCE')

UNREACHABLE['AudioView.setRecordButtonVisible'] = ('no_trigger_in_app', 'No call site in src/main. grep for setRecordButtonVisible over src/main (java and res) finds only the definition at AudioView.java:141.', 'com/ichi2/anki/multimediacard/AudioView.java:141-147', 'SOURCE')

UNREACHABLE['BeolingusParser.<init>'] = ('no_trigger_in_app', 'The class has only static methods and no explicit constructor. No new BeolingusParser exists in src/main: grep finds the class declaration (BeolingusParser.java:25) and only the static calls at LoadPronounciationActivity.java:288 and 323.', 'com/ichi2/anki/multimediacard/beolingus/parsing/BeolingusParser.java:25, 132; com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:288, 323', 'SOURCE')
