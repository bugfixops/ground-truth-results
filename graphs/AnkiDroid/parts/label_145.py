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
