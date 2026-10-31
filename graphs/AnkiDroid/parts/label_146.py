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
