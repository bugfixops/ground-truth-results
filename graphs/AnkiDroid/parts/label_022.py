# AnkiDroid batch 022 (LABEL helper). AbstractFlashcardViewer part 4: 25 methods. The full row list is in
# graphs/AnkiDroid/parts/label_022.md. Methods: $7.onLongClick, $8 and $9 (DeckTask.TaskListener anonymous classes),
# $AnkiDroidWebChromeClient, $MyGestureDetector, $MyWebView and the two scroll runnables $MyWebView$1 and $MyWebView$2.
#
# Route ownership:
# - CALL edges from the outer constructor, createWebView and initLayout into the inner <init> methods, and the
#   DeckTask.TaskListener default calls into $8 and $9 (DeckTask.java 1300, 1306, 1312), come from auto_calls.json.
#   They are not written here. Neither are the in-method CALL edges that auto_calls.json already holds.
# - The ASYNC launch edges into $8 and $9 (DismissCard in dismiss, batch 019, and UPDATE_FACT in onActivityResult)
#   are not written here. label_019.py:43 writes the one into $8.onPostExecute.
# - The run body of the long-click runnable ($3.run, AbstractFlashcardViewer.java:373-378) is batch 021. The ASYNC edge
#   into it from $7.onLongClick is written here, because the source is in this batch.
# - Extractor anomaly: auto_calls.json maps $8.onProgressUpdate (AbstractFlashcardViewer.java:492) and $8.onPostExecute
#   (:501) to $8 itself, but the source calls mAnswerCardHandler ($10). No CALL edge is written for this; it is a lead.
#
# Gates: MG162-MG166 (batch range MG162-MG171). Predefined constants used: STATE_SETTINGS (long-click registration,
# which needs two preferences), STATE_CARDS (gesture edges). Page node: S_REVIEWER.

# --- Long-click on the touch layer (registered in initLayout, AbstractFlashcardViewer.java:1334-1335).
e('S_REVIEWER', 'AbstractFlashcardViewer$7.onLongClick', 'GUI',
  'long-press the card area (the touch layer) when the long-click workaround is on',
  env=None,
  needs_state=STATE_SETTINGS,
  gui=['long-press the card area (the touch layer) when the long-click workaround is on'],
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:468-481, 1333-1336, 1719-1720; FW-SRC core/java/android/view/View.java:6368-6374',
  note='The listener is set only when !mDisableClipboard and mLongClickWorkaround (the dictionary preference is not "0", and textSelectionLongclickWorkaround is true). The two preferences are STATE_SETTINGS. The long-press dispatch is View.performLongClickInternal (View.java:6368-6374).')

e('AbstractFlashcardViewer$7.onLongClick', 'AbstractFlashcardViewer$3.run', 'ASYNC',
  'the long-click handler posts the start-long-click runnable with a 300 ms delay',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:373-378, 478; FW-SRC core/java/android/os/Handler.java:427, 97-98, 789-790',
  note='The run body (executeCommand(mGestureLongclick)) is batch 021. The post is in this batch (AbstractFlashcardViewer.java:478). The dispatch to run is the Handler route in fw_src.')

# --- WebChromeClient (created in createWebView, AbstractFlashcardViewer.java:1448).
e('S_REVIEWER', 'AbstractFlashcardViewer$AnkiDroidWebChromeClient.onJsAlert', 'FRAMEWORK',
  'the card content runs a JavaScript alert(); the WebView calls the chrome client onJsAlert',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1448, 2583-2590',
  note='MISSING GATE MG162: the card HTML must call alert() (a card template with a script that runs alert). No predefined ENV or STATE kind covers the card content. env and needs_state unset. The WebView dispatch to WebChromeClient is not in fw_src: INFERRED.')

# --- MyWebView (created in createWebView, AbstractFlashcardViewer.java:1436).
e('S_REVIEWER', 'AbstractFlashcardViewer$MyWebView.onCheckIsTextEditor', 'FRAMEWORK',
  'an input method (keyboard) attached to the card WebView asks whether the view is a text editor',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1436, 1727, 2622-2628; FW-SRC core/java/android/view/View.java:12527',
  note='MISSING GATE MG163: an input method is attached to the card WebView (the card view has the focus). The override returns true only when mInputWorkaround is set (the input workaround preference, AbstractFlashcardViewer.java:1727), and super otherwise. The IME dispatch is not in fw_src: INFERRED. env and needs_state unset.')

e('S_REVIEWER', 'AbstractFlashcardViewer$MyWebView.onScrollChanged', 'GUI',
  'drag or fling the card content so that the card WebView scrolls',
  env=None,
  gui=['drag or fling the card content so that the card WebView scrolls'],
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:2632-2643; FW-SRC core/java/android/view/View.java:13505, 15226-15239',
  note='MISSING GATE MG164: the card content is larger than the card WebView, so a drag moves it (a content scroll). The WebView content scroll that calls onScrollChanged is Chromium code, not in fw_src: INFERRED. env and needs_state unset.')

e('AbstractFlashcardViewer$MyWebView.onScrollChanged', 'AbstractFlashcardViewer$MyWebView$1.run', 'ASYNC',
  'a horizontal scroll change posts the x-scroll reset runnable with a 300 ms delay',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:2634-2637, 2646-2650; FW-SRC core/java/android/os/Handler.java:427, 97-98, 789-790',
  note='MISSING GATE MG165: the horizontal branch is taken only when abs(horiz - oldHoriz) is larger than abs(vert - oldVert) (AbstractFlashcardViewer.java:2634). env and needs_state unset.')

e('AbstractFlashcardViewer$MyWebView.onScrollChanged', 'AbstractFlashcardViewer$MyWebView$2.run', 'ASYNC',
  'a vertical scroll change posts the y-scroll reset runnable with a 300 ms delay',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:2634, 2638-2641, 2652-2656; FW-SRC core/java/android/os/Handler.java:427, 97-98, 789-790',
  note='MISSING GATE MG166: the else branch is taken when abs(vert - oldVert) is at least abs(horiz - oldHoriz) (AbstractFlashcardViewer.java:2634, 2638). env and needs_state unset.')

# --- MyGestureDetector (created in initLayout, AbstractFlashcardViewer.java:1343; the touch layer uses it at 1333).
e('S_REVIEWER', 'AbstractFlashcardViewer$MyGestureDetector.onDoubleTap', 'GUI',
  'double-tap the card area (a second tap within the double-tap timeout)',
  env=None,
  needs_state=STATE_CARDS,
  gui=['double-tap the card area (a second tap within the double-tap timeout)'],
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1333, 1343, 2711-2716; FW-SRC core/java/android/view/GestureDetector.java:565',
  note='The command runs only when mGesturesEnabled is set (AbstractFlashcardViewer.java:2711-2716; set from AnkiDroidApp.initiateGestures at 1737). The second-tap branch is GestureDetector.java:565.')

e('S_REVIEWER', 'AbstractFlashcardViewer$MyGestureDetector.onFling', 'GUI',
  'swipe across the card area (a fling longer than the swipe thresholds)',
  env=None,
  needs_state=STATE_CARDS,
  gui=['swipe across the card area (a fling longer than the swipe thresholds)'],
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1333, 1343, 2664-2707; FW-SRC core/java/android/view/GestureDetector.java:655',
  note='The swipe commands run only when mGesturesEnabled is set (AbstractFlashcardViewer.java:2670). The fling branch is GestureDetector.java:655.')

e('S_REVIEWER', 'AbstractFlashcardViewer$MyGestureDetector.onSingleTapConfirmed', 'GUI',
  'single tap on the card area with no second tap',
  env=None,
  needs_state=STATE_CARDS,
  gui=['single tap on the card area with no second tap'],
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1333, 1343, 2730-2759; FW-SRC core/java/android/view/GestureDetector.java:642',
  note='The tap-zone commands run only when mGesturesEnabled is set and no text selection is active (mIsSelecting, AbstractFlashcardViewer.java:2730-2759). The confirm call is GestureDetector.java:642 (ACTION_UP with the double-tap listener set).')

e('S_REVIEWER', 'AbstractFlashcardViewer$MyGestureDetector.onSingleTapUp', 'GUI',
  'lift the finger after a tap on the card area',
  env=None,
  needs_state=STATE_CARDS,
  gui=['lift the finger after a tap on the card area'],
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1333, 1343, 2720-2726; FW-SRC core/java/android/view/GestureDetector.java:640',
  note='The body only clears mTouchStarted and removes longClickTestRunnable, then returns false. No command runs from this callback.')

# --- UNREACHABLE: no DISMISS (type 11) or UPDATE_FACT (type 7) DeckTask is ever cancelled, so onCancelled never runs.
_CANCEL_REASON = ("DeckTask.onCancelled calls the listener onCancelled (DeckTask.java:368-370) only after a cancel. "
                  "The in-app cancels of a DeckTask all go through DeckTask.cancelTask(int) (DeckTask.java:181-184), "
                  "which cancels the latest task only when its mType equals the argument. The only callers pass "
                  "TASK_TYPE_SEARCH_CARDS (30) and TASK_TYPE_RENDER_BROWSER_QA (37) (CardBrowser.java:528-529, 796-797, 1155). "
                  "The no-argument cancelTask() (DeckTask.java:168-178) has no caller besides cancelTask(int). "
                  "The other cancel(true) calls act on non-DeckTask tasks: TaskOperations.stopTaskGracefully (TaskOperations.java:33), "
                  "Connection (Connection.java:541), Statistics (Statistics.java:414, 585). "
                  "So the DISMISS task (DeckTask.java:73) and the UPDATE_FACT task (DeckTask.java:71) are never cancelled.")
_CANCEL_SOURCE = ('SRC com/ichi2/async/DeckTask.java:168-184, 368-370; SRC com/ichi2/anki/CardBrowser.java:528-529, 796-797, 1155; '
                  'SRC com/ichi2/anki/runtimetools/TaskOperations.java:33; SRC com/ichi2/async/Connection.java:541; '
                  'SRC com/ichi2/anki/Statistics.java:414, 585')

UNREACHABLE['AbstractFlashcardViewer$8.onCancelled'] = ('no_trigger_in_app', _CANCEL_REASON, _CANCEL_SOURCE, 'SOURCE')
UNREACHABLE['AbstractFlashcardViewer$9.onCancelled'] = ('no_trigger_in_app', _CANCEL_REASON, _CANCEL_SOURCE, 'SOURCE')
