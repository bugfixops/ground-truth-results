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
