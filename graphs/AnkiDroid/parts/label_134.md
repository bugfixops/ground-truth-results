STATUS: RUNNING 13:25

# Part 134 LABEL (AnkiDroid)

Printed-source base: final_java_only/AnkiDroid/app/AnkiDroid-#4200/AnkiDroid/src/main/java/ (paths below are relative to it, starting at com/ichi2/).
Counts: REACHABLE 38, UNREACHABLE 0, edges written 2 (graphs/AnkiDroid/parts/label_134.py). putString and remConf are labelled in batch 028 (REACHABLE) and are not repeated here.

| method | label | kind | reason | printed file:lines |
|---|---|---|---|---|
| AbstractFlashcardViewer$1.handleMessage | REACHABLE | FRAMEWORK | Handler that plays the playsound: message posted by WebViewClient $15.shouldOverrideUrlLoading (mHandler.sendMessage, AFV:1458-1464). The route into $15 is a WebView link tap, which is batch 021's edge and not yet in graph_def.py. Least certain. | com/ichi2/anki/AbstractFlashcardViewer.java:352-358, 1435-1466 |
| AbstractFlashcardViewer.answerCard | REACHABLE | CALL | Reviewer.onKeyUp calls answerCard(getDefaultEase()) (Reviewer.java:352). executeCommand gesture cases call it too (2526, 2533). The body posts the delayed clear at 1316 (ASYNC edge in label_134.py). | com/ichi2/anki/AbstractFlashcardViewer.java:1279-1325, 2522-2536; com/ichi2/anki/Reviewer.java:350-353 |
| AbstractFlashcardViewer.clipboardGetText | REACHABLE | CALL | Private helper called by lookUp (1210) and showLookupButtonIfNeeded (1219). | com/ichi2/anki/AbstractFlashcardViewer.java:1053, 1207-1221 |
| AbstractFlashcardViewer.clipboardHasText | REACHABLE | CALL | Reviewer.onCreateOptionsMenu calls it on the review options menu (Reviewer.java:300). The look-up icon listener (1423) and lookUpOrSelectText call it too. | com/ichi2/anki/AbstractFlashcardViewer.java:1026, 1416-1428; com/ichi2/anki/Reviewer.java:296-304 |
| AbstractFlashcardViewer.delayedHide | REACHABLE | CALL | Reviewer.onWindowFocusChanged calls it (Reviewer.java:526; S_REVIEWER FRAMEWORK). MyGestureDetector.onFling and onSingleTapConfirmed call it (2668, 2734). | com/ichi2/anki/AbstractFlashcardViewer.java:2640-2778; com/ichi2/anki/Reviewer.java:522-528 |
| AbstractFlashcardViewer.dismiss | REACHABLE | CALL | executeCommand dismiss cases call it (2556-2565). The delete-note dialog callback $13.onPositive calls it (1248). | com/ichi2/anki/AbstractFlashcardViewer.java:2556-2565, 2824-2827 |
| AbstractFlashcardViewer.editCard | REACHABLE | CALL | executeCommand edit case calls it (2547). Reviewer.onOptionsItemSelected and Reviewer.onKeyUp also call it. Starts NoteEditor with CALLER_REVIEWER. | com/ichi2/anki/AbstractFlashcardViewer.java:1183-1190, 2547 |
| AbstractFlashcardViewer.executeCommand | REACHABLE | CALL | Command dispatcher. MyGestureDetector.onFling, onDoubleTap and onSingleTapConfirmed call it (2681-2752). Which command a gesture maps to depends on user settings. | com/ichi2/anki/AbstractFlashcardViewer.java:2487-2600, 2640-2760 |
| AbstractFlashcardViewer.getDefaultEase | REACHABLE | CALL | Reviewer.onKeyUp passes getDefaultEase() to answerCard (Reviewer.java:352). | com/ichi2/anki/AbstractFlashcardViewer.java:835-840; com/ichi2/anki/Reviewer.java:350-353 |
| AbstractFlashcardViewer.getEditorCard | REACHABLE | CALL | Static accessor called from the NoteEditor CALLER_REVIEWER branch (NoteEditor.java:371), inside NoteEditor.onCollectionLoaded. That method is reached only through AnkiActivity.onLoadFinished, a loader callback (FRAMEWORK, INFERRED, androidx Loader source not read). The graph has no inbound edge into onLoadFinished. Least certain. | com/ichi2/anki/AbstractFlashcardViewer.java:2295-2300; com/ichi2/anki/NoteEditor.java:326-334, 366-373; com/ichi2/anki/AnkiActivity.java:255-262, 283-290 |
| AbstractFlashcardViewer.getGestureDetector | REACHABLE | CALL | Reviewer$1.onTouch (whiteboard touch, Reviewer.java:467) forwards touches to the gesture detector. | com/ichi2/anki/AbstractFlashcardViewer.java:1117-1119; com/ichi2/anki/Reviewer.java:460-470 |
| AbstractFlashcardViewer.getParentDid | REACHABLE | CALL | Reviewer.onCollectionLoaded, Reviewer.onCreateOptionsMenu (Reviewer.java:302) and Reviewer.setWhiteboardEnabledState call it. | com/ichi2/anki/AbstractFlashcardViewer.java:1106-1108; com/ichi2/anki/Reviewer.java:296-304 |
| AbstractFlashcardViewer.getRecommendedEase | REACHABLE | CALL | executeCommand gesture cases call it (2526, 2533). Needs a user-configured gesture setting (gate). | com/ichi2/anki/AbstractFlashcardViewer.java:1259-1262, 2522-2536 |
| AbstractFlashcardViewer.hideLookupButton | REACHABLE | CALL | answerCard calls it (1284). | com/ichi2/anki/AbstractFlashcardViewer.java:1230-1233, 1279-1285 |
| AbstractFlashcardViewer.initControls | REACHABLE | CALL | initLayout calls it (1429). Reviewer.initControls also calls it. | com/ichi2/anki/AbstractFlashcardViewer.java:1326-1430, 1678-1684 |
| AbstractFlashcardViewer.initLayout | REACHABLE | CALL | onCollectionLoaded calls it (888). | com/ichi2/anki/AbstractFlashcardViewer.java:879-913, 1326-1330 |
| AbstractFlashcardViewer.lookUp | REACHABLE | CALL | lookUpOrSelectText calls it (1200). The look-up icon listener calls it (1424). | com/ichi2/anki/AbstractFlashcardViewer.java:1197-1212, 1416-1428 |
| AbstractFlashcardViewer.lookUpOrSelectText | REACHABLE | CALL | executeCommand look-up case calls it (2553). Reviewer.onOptionsItemSelected calls it (Reviewer.java:205). | com/ichi2/anki/AbstractFlashcardViewer.java:1197-1217, 2553; com/ichi2/anki/Reviewer.java:200-216 |
| AbstractFlashcardViewer.onBackPressed | REACHABLE | FRAMEWORK | S_REVIEWER FRAMEWORK edge (graph_def.py:3427). The Back key on the review page calls it. | com/ichi2/anki/AbstractFlashcardViewer.java:967-975 |
| AbstractFlashcardViewer.onCollectionLoaded | REACHABLE | CALL | Reviewer.onCollectionLoaded calls super (Reviewer.java:98), and Previewer.onCollectionLoaded also calls it. Reviewer.onCollectionLoaded is reached through the ASYNC edge from AbstractFlashcardViewer.onCreate. | com/ichi2/anki/AbstractFlashcardViewer.java:879-913; com/ichi2/anki/Reviewer.java:96-106 |
| AbstractFlashcardViewer.onConfigurationChanged | REACHABLE | SYSTEM | S_REVIEWER SYSTEM edge (graph_def.py:3435). | com/ichi2/anki/AbstractFlashcardViewer.java:867-870 |
| AbstractFlashcardViewer.onDestroy | REACHABLE | LIFECYCLE | S_REVIEWER LIFECYCLE edge (graph_def.py:3443). | com/ichi2/anki/AbstractFlashcardViewer.java:949-955 |
| AbstractFlashcardViewer.onKeyDown | REACHABLE | GUI | S_REVIEWER GUI edge (graph_def.py:3418). Hardware key press on the review page. | com/ichi2/anki/AbstractFlashcardViewer.java:977-1011 |
| AbstractFlashcardViewer.onKeyUp | REACHABLE | CALL | Reviewer.onKeyUp calls super (Reviewer.java:391). Reviewer.onKeyUp is reached by S_REVIEWER GUI. | com/ichi2/anki/AbstractFlashcardViewer.java:1012-1025; com/ichi2/anki/Reviewer.java:386-392 |
| AbstractFlashcardViewer.onMark | REACHABLE | CALL | executeCommand mark case calls it (2550). Reviewer.onOptionsItemSelected and Reviewer.onKeyUp also call it. | com/ichi2/anki/AbstractFlashcardViewer.java:2813-2822, 2550 |
| AbstractFlashcardViewer.registerExternalStorageListener | REACHABLE | CALL | onCollectionLoaded calls it (884). | com/ichi2/anki/AbstractFlashcardViewer.java:879-890, 1125-1127 |
| AbstractFlashcardViewer.selectAndCopyText | REACHABLE | CALL | lookUpOrSelectText calls it on the select-text path. | com/ichi2/anki/AbstractFlashcardViewer.java:1197-1217, 2459-2466 |
| AbstractFlashcardViewer.shouldUseQuickUpdate | REACHABLE | CALL | onCollectionLoaded assigns it at 886. | com/ichi2/anki/AbstractFlashcardViewer.java:879-890, 2482-2492 |
| AbstractFlashcardViewer.showDeleteNoteDialog | REACHABLE | CALL | executeCommand delete case calls it (2568). Reviewer.onOptionsItemSelected also calls it. | com/ichi2/anki/AbstractFlashcardViewer.java:1239-1242, 2568 |
| AbstractFlashcardViewer.showLookupButtonIfNeeded | REACHABLE | CALL | MyGestureDetector.onSingleTapConfirmed calls it (2757). | com/ichi2/anki/AbstractFlashcardViewer.java:1217-1221, 2740-2760 |
| AbstractFlashcardViewer.showSelectTtsDialogue | REACHABLE | CALL | Reviewer.onOptionsItemSelected calls it (Reviewer.java:215). | com/ichi2/anki/AbstractFlashcardViewer.java:2232-2240; com/ichi2/anki/Reviewer.java:200-216 |
| AbstractFlashcardViewer.ttsInitialized | REACHABLE | CALL | ReadText$3.onInit calls it (ReadText.java:187) after the TTS engine starts. Needs ENV_TTS and the "tts" setting (mSpeakText). | com/ichi2/anki/AbstractFlashcardViewer.java:2806-2812; com/ichi2/anki/ReadText.java:168-192 |
| AbstractFlashcardViewer.undo | REACHABLE | CALL | executeCommand undo case calls it (2543). Reviewer.onKeyUp (387) and Reviewer.onOptionsItemSelected also call it. | com/ichi2/anki/AbstractFlashcardViewer.java:1170-1172, 2543; com/ichi2/anki/Reviewer.java:386-392 |
| DeckOptions$DeckPreferenceHack$Editor.<init> | REACHABLE | CALL | DeckPreferenceHack.edit creates it (DeckOptions.java:422). edit is reached from S_DECKOPTIONS GUI (graph_def.py:4041), which needs the page-entry ENTERS edge in label_134.py. | com/ichi2/anki/DeckOptions.java:137-139, 421-422 |
| DeckOptions$DeckPreferenceHack$Editor.apply | REACHABLE | FRAMEWORK | Preference framework calls apply after a put* (graph_def.py:4065, 4071). apply calls commit (353). | com/ichi2/anki/DeckOptions.java:352-354 |
| DeckOptions$DeckPreferenceHack$Editor.commit | REACHABLE | CALL | apply calls commit (DeckOptions.java:353). commit loops over mUpdate (151-160). | com/ichi2/anki/DeckOptions.java:151-160, 352-355 |
| DeckOptions$DeckPreferenceHack$Editor.putBoolean | REACHABLE | GUI | S_DECKOPTIONS GUI edge (graph_def.py:4049). Stores into mUpdate. | com/ichi2/anki/DeckOptions.java:310-312 |
| DeckOptions$DeckPreferenceHack$Editor.putInt | REACHABLE | GUI | S_DECKOPTIONS GUI edge (graph_def.py:4057). Stores into mUpdate. | com/ichi2/anki/DeckOptions.java:324-326 |

Notes:
- Edges written in label_134.py: DeckOptions.onCreate -> S_DECKOPTIONS ENTERS (page-entry fix outside the batch; none existed); AbstractFlashcardViewer.answerCard -> AbstractFlashcardViewer$11.run ASYNC (coordinator request; its destination is batch 138).
- Graph gaps found, not fixed here: AbstractFlashcardViewer$15.shouldOverrideUrlLoading has only a REGISTER inbound edge (batch 021), so $1.handleMessage depends on it. AnkiActivity.onLoadFinished has no inbound edge, so getEditorCard and NoteEditor.onCollectionLoaded depend on it.

STATUS: DONE 13:37
