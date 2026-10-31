# AnkiDroid batch 021 (LABEL helper). AbstractFlashcardViewer part 3: $1.handleMessage, $2 to $6, $7.<init>, and $10 to $21
# (40 methods in graphs/AnkiDroid/scratch/batches/batch_021.txt). The full row list is in graphs/AnkiDroid/parts/label_021.md.
#
# Ownership: AbstractFlashcardViewer$1.<init> is batch_020; $7.onLongClick, $8, $9 and the MyGestureDetector callbacks are
# batch_022; initLayout, initControls, initTimer, createWebView, answerCard, displayCardQuestion, displayCardAnswer and
# delayedHide are batch_019; onActivityResult, registerExternalStorageListener, showDeleteNoteDialog and undo are batch_020.
# Edges written here all have a source method of batch 021. Edges from other batches into these methods are leads in
# label_021.md.
#
# Auto CALL edges (the <init> edges of the anonymous classes, and callee calls such as answerCard, displayCardAnswer,
# displayCardQuestion, executeCommand, setFullScreen) come from auto_calls.json and are not written here.
#
# REGISTER edges go from $N.<init> to each callback. The builder does not follow REGISTER for reachability, so each
# callback's route is written by the part that calls it (see the leads in label_021.md).
#
# Gates: MG152 to MG156 are used on the edges below. Gates whose only condition is a predefined ENV_ or STATE_ kind are not
# used here. env and needs_state are unset on every MG edge.

# --- REGISTER edges from the anonymous-class constructors to their callbacks.
e('AbstractFlashcardViewer$2.<init>', 'AbstractFlashcardViewer$2.run', 'REGISTER',
  'the long-click test runnable is a field of AbstractFlashcardViewer and is created with the viewer',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:359-372',
  note='The builder does not follow REGISTER for reachability. The route into run is AbstractFlashcardViewer$6.onTouch -> $2.run (FRAMEWORK, below).')

e('AbstractFlashcardViewer$3.<init>', 'AbstractFlashcardViewer$3.run', 'REGISTER',
  'the start-long-click runnable is a field of AbstractFlashcardViewer',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:373-378',
  note='The builder does not follow REGISTER for reachability. The route into run is AbstractFlashcardViewer$2.run -> $3.run (FRAMEWORK, below).')

e('AbstractFlashcardViewer$4.<init>', 'AbstractFlashcardViewer$4.onClick', 'REGISTER',
  'the show-answer listener is set on the flip-card layout in initLayout',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:382-395, 1384',
  note='The builder does not follow REGISTER. The registration is at line 1384 (initLayout, owned by batch_019); the route is the lead in label_021.md.')

e('AbstractFlashcardViewer$5.<init>', 'AbstractFlashcardViewer$5.onClick', 'REGISTER',
  'the ease-button listener is set on the four ease layouts in initLayout',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:396-426, 1348, 1353, 1358, 1363',
  note='The builder does not follow REGISTER. Registrations at lines 1348, 1353, 1358 and 1363 (initLayout, batch_019). The route is the lead in label_021.md.')

e('AbstractFlashcardViewer$6.<init>', 'AbstractFlashcardViewer$6.onTouch', 'REGISTER',
  'the gesture and long-click touch listener is set on the touch layer in initLayout',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:428-466, 1333',
  note='The builder does not follow REGISTER. The registration is mTouchLayer.setOnTouchListener at line 1333 (initLayout, batch_019).')

e('AbstractFlashcardViewer$7.<init>', 'AbstractFlashcardViewer$7.onLongClick', 'REGISTER',
  'the long-click listener is set on the touch layer in initLayout',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:468-481, 1335',
  note='onLongClick is batch_022. The builder does not follow REGISTER. The registration is at line 1335 (initLayout, batch_019).')

e('AbstractFlashcardViewer$10.<init>', 'AbstractFlashcardViewer$10.onPreExecute', 'REGISTER',
  'the answer-card task listener (mAnswerCardHandler) is a field; DeckTask calls its callbacks',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:578-651, 1320-1321',
  note='The builder does not follow REGISTER. The ASYNC route from AbstractFlashcardViewer.answerCard is written in label_019.py. Other ANSWER_CARD and UNDO launches with this listener are leads in label_021.md.')

e('AbstractFlashcardViewer$10.<init>', 'AbstractFlashcardViewer$10.onProgressUpdate', 'REGISTER',
  'the answer-card task listener (mAnswerCardHandler) is a field; DeckTask calls its callbacks',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:578-651, 1320-1321',
  note='The builder does not follow REGISTER. The ASYNC route from AbstractFlashcardViewer.answerCard is written in label_019.py. Other ANSWER_CARD and UNDO launches with this listener are leads in label_021.md.')

e('AbstractFlashcardViewer$10.<init>', 'AbstractFlashcardViewer$10.onPostExecute', 'REGISTER',
  'the answer-card task listener (mAnswerCardHandler) is a field; DeckTask calls its callbacks',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:578-651, 1320-1321',
  note='The builder does not follow REGISTER. The ASYNC route from AbstractFlashcardViewer.answerCard is written in label_019.py. Other ANSWER_CARD and UNDO launches with this listener are leads in label_021.md.')

e('AbstractFlashcardViewer$10.<init>', 'AbstractFlashcardViewer$10.onCancelled', 'REGISTER',
  'the answer-card task listener (mAnswerCardHandler) is a field; DeckTask calls its callbacks',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:578-651; SRC com/ichi2/async/DeckTask.java:368-369',
  note='The builder does not follow REGISTER. onCancelled is UNREACHABLE (no_trigger_in_app, below), so no route is written for it.')

e('AbstractFlashcardViewer$11.<init>', 'AbstractFlashcardViewer$11.run', 'REGISTER',
  'the chosen-answer clearing runnable is a field of AbstractFlashcardViewer',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:825-830',
  note='The builder does not follow REGISTER. The route is the FRAMEWORK edge AbstractFlashcardViewer.answerCard -> $11.run (batch_019, line 1316), a lead in label_021.md.')

e('AbstractFlashcardViewer$12.<init>', 'AbstractFlashcardViewer$12.onReceive', 'REGISTER',
  'the unmount receiver is created in registerExternalStorageListener and registered at line 1137',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1127-1134, 1137',
  note='The builder does not follow REGISTER. registerExternalStorageListener is batch_020; the broadcast source is a lead in label_021.md.')

e('AbstractFlashcardViewer$13.<init>', 'AbstractFlashcardViewer$13.onPositive', 'REGISTER',
  'the delete-note dialog callback is created in showDeleteNoteDialog',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1248-1254',
  note='The builder does not follow REGISTER. The route is the dialog callback edge from showDeleteNoteDialog (batch_020, lead in label_021.md).')

e('AbstractFlashcardViewer$14.<init>', 'AbstractFlashcardViewer$14.onClick', 'REGISTER',
  'the lookup icon listener is set in initLayout',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1418-1428',
  note='The builder does not follow REGISTER. Registration at line 1418 (initLayout, batch_019). The route is the GUI lead from the S_REVIEWER page (label_021.md).')

e('AbstractFlashcardViewer$15.<init>', 'AbstractFlashcardViewer$15.shouldOverrideUrlLoading', 'REGISTER',
  'the WebViewClient is set on the card web view in createWebView',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1454, 1458; FW-SRC core/java/android/webkit/WebViewClient.java:49',
  note='The builder does not follow REGISTER. The registration is at line 1454 (createWebView, batch_019). The route is the WebView link-navigation lead in label_021.md.')

e('AbstractFlashcardViewer$15.<init>', 'AbstractFlashcardViewer$15.onPageFinished', 'REGISTER',
  'the WebViewClient is set on the card web view in createWebView',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1454, 1542-1545',
  note='The builder does not follow REGISTER. The registration is at line 1454 (createWebView, batch_019). The route is the WebView page-finished lead in label_021.md.')

e('AbstractFlashcardViewer$16.<init>', 'AbstractFlashcardViewer$16.onEditorAction', 'REGISTER',
  'the answer-field editor action listener is set in initControls',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1689-1698; FW-SRC core/java/android/widget/TextView.java:7430',
  note='The builder does not follow REGISTER. Registration at line 1689 (initControls, batch_019).')

e('AbstractFlashcardViewer$17.<init>', 'AbstractFlashcardViewer$17.onKey', 'REGISTER',
  'the answer-field key listener is set in initControls',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1699-1709; FW-SRC core/java/android/view/View.java:11709',
  note='The builder does not follow REGISTER. Registration at line 1699 (initControls, batch_019).')

e('AbstractFlashcardViewer$18.<init>', 'AbstractFlashcardViewer$18.run', 'REGISTER',
  'the show-question timeout runnable is a field of AbstractFlashcardViewer',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1863-1871, 2031-2033',
  note='The builder does not follow REGISTER. The route is the postDelayed lead from displayCardAnswer (batch_019, line 2033).')

e('AbstractFlashcardViewer$19.<init>', 'AbstractFlashcardViewer$19.run', 'REGISTER',
  'the show-answer timeout runnable is a field of AbstractFlashcardViewer',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1873-1880, 1947-1949',
  note='The builder does not follow REGISTER. The route is the postDelayed lead from displayCardQuestion (batch_019, line 1949).')

e('AbstractFlashcardViewer$20.<init>', 'AbstractFlashcardViewer$20.onChronometerTick', 'REGISTER',
  'the card timer tick listener is set in initTimer',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1901-1910',
  note='The builder does not follow REGISTER. Registration at line 1901 (initTimer, batch_019). Chronometer is not in fw_src: INFERRED.')

e('AbstractFlashcardViewer$21.<init>', 'AbstractFlashcardViewer$21.handleMessage', 'REGISTER',
  'the fullscreen handler is a field of AbstractFlashcardViewer',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:2763-2770, 2772-2775',
  note='The builder does not follow REGISTER. The route is the FRAMEWORK lead from delayedHide (batch_019, line 2774).')

# --- FRAMEWORK edges from a listener of this batch to a callback that the framework dispatches, or that a view performs.
e('AbstractFlashcardViewer$2.run', 'AbstractFlashcardViewer$3.run', 'FRAMEWORK',
  'the 300 ms long-click timer posts the start-long-click runnable',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:364, 370; FW-SRC core/java/android/os/Handler.java:427',
  note='No gate: the post at line 370 is unconditional in run (the if at line 364 only controls the lookup toast). run is posted by AbstractFlashcardViewer$6.onTouch (800 ms, line 438).')

e('AbstractFlashcardViewer$6.onTouch', 'AbstractFlashcardViewer$2.run', 'FRAMEWORK',
  'an ACTION_DOWN touch posts the long-click test runnable after 800 ms',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:430-438; FW-SRC core/java/android/os/Handler.java:427',
  note='MISSING GATE MG152: the post at line 438 runs only when the gesture detector did not consume the event (line 431), the action is ACTION_DOWN (line 436), and the two flags at line 434 (mDisableClipboard and mLongClickWorkaround) are both false. The detector result and the flags form one condition that no predefined ENV or STATE kind covers. env and needs_state unset.')

e('AbstractFlashcardViewer$6.onTouch', 'AbstractFlashcardViewer$MyGestureDetector.onFling', 'FRAMEWORK',
  'a fling on the touch layer: the gesture detector created in initLayout dispatches it from onTouchEvent',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:431, 1343, 2661, 2664; FW-SRC core/java/android/view/GestureDetector.java:115, 490, 655',
  note='The gesture is input, not a gate. MyGestureDetector (line 2661) extends SimpleOnGestureListener, so onFling is batch_022; it is written here because the source is in batch 021. The dispatch in GestureDetector.onTouchEvent is at line 655. The hop from GestureDetectorCompat (line 1343) to the framework GestureDetector is not in fw_src: INFERRED.')

e('AbstractFlashcardViewer$6.onTouch', 'AbstractFlashcardViewer$MyGestureDetector.onDoubleTap', 'FRAMEWORK',
  'a double tap on the touch layer: the gesture detector dispatches it from onTouchEvent',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:431, 1343, 2711; FW-SRC core/java/android/view/GestureDetector.java:142, 565',
  note='The gesture is input, not a gate. The dispatch is GestureDetector.onTouchEvent at line 565; the GestureDetectorCompat hop is not in fw_src: INFERRED. The callback is batch_022.')

e('AbstractFlashcardViewer$6.onTouch', 'AbstractFlashcardViewer$MyGestureDetector.onSingleTapUp', 'FRAMEWORK',
  'a single-tap-up on the touch layer: the gesture detector dispatches it from onTouchEvent',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:431, 1343, 2720; FW-SRC core/java/android/view/GestureDetector.java:75, 640',
  note='The gesture is input, not a gate. The dispatch is GestureDetector.onTouchEvent at line 640; the GestureDetectorCompat hop is not in fw_src: INFERRED. The callback is batch_022.')

e('AbstractFlashcardViewer$6.onTouch', 'AbstractFlashcardViewer$MyGestureDetector.onSingleTapConfirmed', 'FRAMEWORK',
  'a confirmed single tap on the touch layer: the gesture detector dispatches it from onTouchEvent',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:431, 1343, 2730; FW-SRC core/java/android/view/GestureDetector.java:134, 642',
  note='The gesture is input, not a gate. The dispatch is GestureDetector.onTouchEvent at line 642; the GestureDetectorCompat hop is not in fw_src: INFERRED. The callback is batch_022.')

e('AbstractFlashcardViewer$15.shouldOverrideUrlLoading', 'AbstractFlashcardViewer$1.handleMessage', 'FRAMEWORK',
  'the card link with the playsound: scheme is intercepted and its sound path is sent to the handler that plays it',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1458-1465; FW-SRC core/java/android/os/Handler.java:97, 536',
  note='MISSING GATE MG153: the card page must contain a sound link that produces a playsound: URL, and the user must tap it (the URL comes from the card HTML and page JavaScript, not in this dataset). No predefined kind covers it. env and needs_state unset.')

e('AbstractFlashcardViewer$15.shouldOverrideUrlLoading', 'AbstractFlashcardViewer$4.onClick', 'FRAMEWORK',
  'the typeentertext: link performs a click on the flip-card layout, which calls the show-answer listener',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1477-1483; FW-SRC core/java/android/view/View.java:6289-6294',
  note='MISSING GATE MG154: the card must be a type-in-the-answer card (typeAnswer() true, line 1688) and the user must press Enter in the typing box so the page loads the typeentertext: URL. No predefined kind covers it. env and needs_state unset.')

e('AbstractFlashcardViewer$18.run', 'AbstractFlashcardViewer$5.onClick', 'FRAMEWORK',
  'the auto-advance question timer clicks the Again (ease 1) layout, which calls the ease listener',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1863-1871, 2031-2033; FW-SRC core/java/android/view/View.java:6289-6294',
  note='MISSING GATE MG155: the timer is posted only when mPrefUseTimer and mWaitQuestionSecond > 0 (line 2031, displayCardAnswer), and the click happens only when mEase1Layout is enabled and visible (line 1867, checked in run). No predefined kind covers the view state. env and needs_state unset.')

e('AbstractFlashcardViewer$19.run', 'AbstractFlashcardViewer$4.onClick', 'FRAMEWORK',
  'the auto-advance answer timer clicks the flip-card layout, which calls the show-answer listener',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1873-1880, 1947-1949; FW-SRC core/java/android/view/View.java:6289-6294',
  note='MISSING GATE MG156: the timer is posted only when mPrefUseTimer and mWaitAnswerSecond > 0 (line 1947, displayCardQuestion), and the click happens only when mFlipCardLayout is enabled and visible (line 1876, checked in run). No predefined kind covers the view state. env and needs_state unset.')

# --- UNREACHABLE
UNREACHABLE['AbstractFlashcardViewer$10.onCancelled'] = (
    'no_trigger_in_app',
    "AsyncTask calls onCancelled only after cancel(true) on the task (FW-SRC AsyncTask.java:462-463 and 479). DeckTask forwards the call to its listener (DeckTask.java:368-369). "
    "The only app code that cancels a DeckTask is DeckTask.cancelTask() and cancelTask(int) (DeckTask.java:168-186). cancelTask(int) cancels only when the latest task has the given type, and "
    "every caller passes TASK_TYPE_SEARCH_CARDS or TASK_TYPE_RENDER_BROWSER_QA (CardBrowser.java:528-529, 796-797, 1155). No caller passes a type that this listener serves: "
    "TASK_TYPE_ANSWER_CARD (DeckTask.java:69) is launched at AbstractFlashcardViewer.java:1076, 1092 and 1320-1321 and at Reviewer.java:110, and TASK_TYPE_UNDO is launched at AbstractFlashcardViewer.java:1172, "
    "all with mAnswerCardHandler. TaskOperations.stopTaskGracefully (TaskOperations.java:30-33) is called only with other activities' tasks (LoadPronounciationActivity.java:474-478, TranslationActivity.java:405). "
    "No code in the dataset cancels this listener's task, so onCancelled never runs.",
    'SRC com/ichi2/anki/AbstractFlashcardViewer.java:578, 649-651, 1076, 1092, 1172, 1320-1321; SRC com/ichi2/anki/Reviewer.java:110; SRC com/ichi2/async/DeckTask.java:69, 168-186, 368-369; SRC com/ichi2/anki/CardBrowser.java:528-529, 796-797, 1155; SRC com/ichi2/anki/runtimetools/TaskOperations.java:30-33; SRC com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:474-478; SRC com/ichi2/anki/multimediacard/activity/TranslationActivity.java:405; FW-SRC core/java/android/os/AsyncTask.java:462-463, 479',
    'SOURCE')
