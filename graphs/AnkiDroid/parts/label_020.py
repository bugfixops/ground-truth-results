# AnkiDroid batch 020 (LABEL helper). AbstractFlashcardViewer part 2: 40 methods.
# The full row list is in graphs/AnkiDroid/parts/label_020.md (40 method rows and 11 edge rows).
#
# Route ownership:
# - Page edges whose destination is in this batch are written here (S_REVIEWER, S_NOTEEDITOR, S_DECKOPTIONS).
# - ASYNC launch edges from the methods in this batch (onActivityResult, undo) are written here. Each launch method
#   gets one edge to the listener's onPostExecute.
# - REGISTER edges from registerExternalStorageListener and showDeleteNoteDialog are written here.
# - onCreate, onPause and onResume LIFECYCLE edges come from lc_chain (graph_def.py:158) and are not written here.
#   onDestroy is skipped by lc_chain (LC_NO_TRIGGER, graph_def.py:37), so its edge is written here.
# - Automatic CALL edges from auto_calls.json are not written here. The keyboard path Reviewer.onKeyUp -> super
#   (Reviewer.java:391) is a CALL, so no GUI edge is written to AbstractFlashcardViewer.onKeyUp.
#
# Gates: MG142-MG146. MG142 playVideo (video media), MG143 removeFrontSideAudio (FrontSide audio template),
# MG144 type-answer methods (type: field), MG145 undo (an undo step), MG146 showLookupButtonIfNeeded (clipboard state).
# Predefined constants used: ENV_CONFIG_CHANGE, ENV_SDCARD_EVENT, STATE_SETTINGS. Page nodes: S_REVIEWER,
# S_NOTEEDITOR, S_DECKOPTIONS.

# --- Keyboard input on the reviewer page (hardware keys dispatched to the viewer).
e('S_REVIEWER', 'AbstractFlashcardViewer.onKeyDown', 'GUI',
  'hardware key press on the reviewer page: page up and page down scroll the card',
  env=None,
  needs_state=None,
  gui=['hardware page up and page down keys scroll the card (always on)'],
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:977-1007',
  note='Reviewer does not override onKeyDown. The scrolling_buttons branches (PICTSYMBOLS, SWITCH_CHARSET) are preference-gated inside the method. The Activity key dispatch is not printed: INFERRED.')

# --- Back key (framework dispatch through Activity.onKeyUp).
e('S_REVIEWER', 'AbstractFlashcardViewer.onBackPressed', 'FRAMEWORK',
  'back key: the framework calls onBackPressed from Activity.onKeyUp',
  env=None,
  needs_state=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:967-974; FW-SRC core/java/android/app/Activity.java:2975-2980',
  note='Activity.onKeyUp calls onBackPressed at 2980 when targetSdk is at least ECLAIR. Outside the drawer the method calls closeReviewer(RESULT_DEFAULT, false).')

# --- Device configuration change (rotation, locale, screen size) on Reviewer.
e('S_REVIEWER', 'AbstractFlashcardViewer.onConfigurationChanged', 'SYSTEM',
  'device configuration changes while the reviewer runs (rotation, locale, screen size)',
  env=ENV_CONFIG_CHANGE,
  needs_state=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:867-871; AndroidManifest.xml (src/main) 171-173; FW-SRC core/java/android/app/Activity.java:2198',
  note='The manifest declares configChanges="keyboardHidden|orientation|locale|screenSize" on Reviewer (line 173), so the system calls this method instead of recreating the activity.')

# --- Activity destroy. lc_chain skips onDestroy (LC_NO_TRIGGER), so the edge is written here.
e('S_REVIEWER', 'AbstractFlashcardViewer.onDestroy', 'LIFECYCLE',
  'the reviewer activity is destroyed (the framework calls onDestroy)',
  env=None,
  needs_state=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:949-963; graph_def.py:37, 158; FW-SRC core/java/android/app/Activity.java:7208',
  note='performDestroy calls onDestroy at Activity.java:7208. The lc_chain call at graph_def.py:158 lists onDestroy but skips it because LC_NO_TRIGGER contains onDestroy (graph_def.py:37).')

# --- Result from the note editor (edit current card).
e('S_NOTEEDITOR', 'AbstractFlashcardViewer.onActivityResult', 'RESULT',
  'the note editor returns to the reviewer after the user edits the card',
  env=None,
  needs_state=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:937-951 (RESULT_OK at 940); com/ichi2/anki/AbstractFlashcardViewer.java:1060-1098, 1183-1189',
  note='closeNoteEditor sets RESULT_OK only when the note changed (mChanged). Otherwise RESULT_CANCELED, and the card is redrawn with fillFlashcard (AbstractFlashcardViewer.java:1088).')

# --- Result from deck options (preference change).
e('S_DECKOPTIONS', 'AbstractFlashcardViewer.onActivityResult', 'RESULT',
  'the deck options screen returns RESULT_OK after a preference change',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/anki/DeckOptions.java:589-595; com/ichi2/anki/AbstractFlashcardViewer.java:1090-1094; com/ichi2/anki/Reviewer.java:208-211',
  note='closeWithResult sets RESULT_OK only when mPreferenceChanged is set. STATE_SETTINGS is the changed preference. The launch is Reviewer.java:208-211 with DECK_OPTIONS.')

# --- ASYNC launches from onActivityResult: UPDATE_FACT (listener $9) and ANSWER_CARD (listener $10).
e('AbstractFlashcardViewer.onActivityResult', 'AbstractFlashcardViewer$9.onPostExecute', 'ASYNC',
  'UPDATE_FACT task launched on mUpdateCardHandler when the note editor saved the card',
  env=None,
  needs_state=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1084-1085; com/ichi2/async/DeckTask.java:360-362',
  note='The listener onPostExecute is reached through DeckTask.onPostExecute (DeckTask.java:360-362).')

e('AbstractFlashcardViewer.onActivityResult', 'AbstractFlashcardViewer$10.onPostExecute', 'ASYNC',
  'ANSWER_CARD task launched on mAnswerCardHandler after a reloadRequired result or a deck options change',
  env=None,
  needs_state=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1076-1077, 1092-1093; com/ichi2/async/DeckTask.java:360-362',
  note='Two launch sites in this method (reloadRequired at 1076 and DECK_OPTIONS at 1092) share one edge to the same listener.')

# --- ASYNC launch from undo (listener $10).
e('AbstractFlashcardViewer.undo', 'AbstractFlashcardViewer$10.onPostExecute', 'ASYNC',
  'TASK_TYPE_UNDO launched on mAnswerCardHandler when an undo step exists',
  env=None,
  needs_state=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1170-1174; com/ichi2/async/DeckTask.java:360-362',
  note='The undo gate (getCol().undoAvailable()) is MG145 (no predefined constant covers an undo step).')

# --- Media-eject receiver registration (ENV_SDCARD_EVENT).
e('AbstractFlashcardViewer.registerExternalStorageListener', 'AbstractFlashcardViewer$12.onReceive', 'REGISTER',
  'the SD card is ejected while the reviewer is open (MEDIA_EJECT broadcast)',
  env=ENV_SDCARD_EVENT,
  needs_state=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1125-1139',
  note='The receiver is registered at line 1137 with SdCardReceiver.MEDIA_EJECT. onReceive calls finishWithoutAnimation (1131).')

# --- Delete dialog positive callback (registered when the dialog is shown).
e('AbstractFlashcardViewer.showDeleteNoteDialog', 'AbstractFlashcardViewer$13.onPositive', 'REGISTER',
  'the user taps the positive button of the delete-note dialog',
  env=None,
  needs_state=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1239-1256',
  note='The callback is set at 1248-1254. onPositive calls dismiss(Collection.DismissType.DELETE_NOTE) at 1252.')
