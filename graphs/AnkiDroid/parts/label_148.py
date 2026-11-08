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
