STATUS: RUNNING 2026-10-30 14:01 EDT

# AnkiDroid batch 148 (LABEL helper). 40 methods. Edges: graphs/AnkiDroid/parts/label_148.py (5 edges).

Labels are copied from the REACHABLE rows in other parts (name match). No UNREACHABLE entry is written. Pending rows depend on routes owned by other batches (see the notes under the table).

| method | label | kind | reason | printed file:lines |
|---|---|---|---|---|
| AbstractFlashcardViewer$20.onChronometerTick | REACHABLE | FRAMEWORK | new edge from AbstractFlashcardViewer.initTimer (label_148.py); tick is INFERRED | AbstractFlashcardViewer.java:1883-1910 |
| AbstractFlashcardViewer$21.handleMessage | REACHABLE | FRAMEWORK | new edge from AbstractFlashcardViewer.delayedHide (label_148.py) | AbstractFlashcardViewer.java:2763-2775; Handler.java:95-98, 558-564 |
| AbstractFlashcardViewer$3.run | REACHABLE | FRAMEWORK | existing edge $2.run -> $3.run (graph_def.py:3204; label_021.py:153) | label_021.md:39 (copied row) |
| AbstractFlashcardViewer$4.onClick | REACHABLE | FRAMEWORK | existing edge $19.run -> $4.onClick (graph_def.py:3258) | label_021.md:41 (copied row); AbstractFlashcardViewer.java:382-395, 1384 |
| AbstractFlashcardViewer$5.onClick | REACHABLE | FRAMEWORK | existing edge $18.run -> $5.onClick (graph_def.py:3252) | label_021.md:43 (copied row) |
| AbstractFlashcardViewer$6.onTouch | REACHABLE | GUI | edge S_REVIEWER -> $6.onTouch is written once, in label_146.py (edge 8); not repeated here | AbstractFlashcardViewer.java:428-466, 1326-1333 |
| AbstractFlashcardViewer$7.onLongClick | REACHABLE | GUI | existing edge S_REVIEWER -> $7.onLongClick (graph_def.py:3299; label_022.py:20) | label_022.md:7 (copied row) |
| AbstractFlashcardViewer$AnkiDroidWebChromeClient.onJsAlert | REACHABLE | FRAMEWORK | existing edge S_REVIEWER -> onJsAlert (graph_def.py:3314) | label_022.md:19 (copied row) |
| AbstractFlashcardViewer$MyWebView$1.run | REACHABLE | ASYNC | existing edge onScrollChanged -> $1.run (graph_def.py:3334) | label_022.md:29 (copied row) |
| AbstractFlashcardViewer$MyWebView$2.run | REACHABLE | ASYNC | existing edge onScrollChanged -> $2.run (graph_def.py:3340) | label_022.md:31 (copied row) |
| AnkiDroidWidgetSmall$UpdateService$1.<init> | REACHABLE | CALL | pending: needs part 080 ASYNC pair (see notes); auto CALL from buildUpdate | AnkiDroidWidgetSmall.java:111; label_018.md:15 (copied row) |
| AnkiStatsTaskHandler$CreateChartTask.onCancelled | REACHABLE | ASYNC | pending: needs Statistics batch cancel(true) edge (see notes) | label_065.md:20 (copied row) |
| AnkiStatsTaskHandler$CreateStatisticsOverview.onCancelled | REACHABLE | ASYNC | pending: needs Statistics batch cancel(true) edge (see notes) | label_065.md:24 (copied row) |
| AnkiStatsTaskHandler.setStatType | REACHABLE | CALL | auto CALL | label_065.md:16 (copied row) |
| AudioField.setHasTemporaryMedia | REACHABLE | CALL | auto CALL | label_058.md:19 (copied row) |
| AudioView$PlayPauseButton$1.onClick | REACHABLE | GUI | existing edge S_MULTIMEDIA_EDIT_FIELD -> onClick (graph_def.py:6766; label_057.py:14) | label_057.md:25 (copied row) |
| AudioView$PlayPauseButton.update | REACHABLE | CALL | auto CALL | label_057.md:23 (copied row) |
| AudioView$RecordButton.update | REACHABLE | CALL | auto CALL | label_057.md:29 (copied row) |
| NoteEditor$JSONNameComparator.<init> | REACHABLE | CALL | auto CALL | label_014.md:13 (copied row) |
| NoteEditor$JSONNameComparator.compare | REACHABLE | CALL | auto CALL from NoteEditor.onCollectionLoaded (graph_def.py:2230) | label_014.md:14 (copied row) |
| ReadText$3.<init> | REACHABLE | CALL | auto CALL | label_053.md:42 (copied row) |
| ReadText$3.onInit | REACHABLE | FRAMEWORK | existing edge ReadText.initializeTts -> onInit (graph_def.py:6709; label_053.py:32) | label_053.md:43 (copied row) |
| ReadText.initializeTts | REACHABLE | CALL | auto CALL | label_053.md:32 (copied row) |
| ReadText.releaseTts | REACHABLE | CALL | auto CALL | label_053.md:33 (copied row) |
| Reviewer$1.<init> | REACHABLE | CALL | auto CALL | label_008.md:29 (copied row) |
| Reviewer$1.onTouch | REACHABLE | GUI | existing edge S_REVIEWER -> onTouch (graph_def.py:1413; label_008.py:114) | label_008.md:30 (copied row) |
| ServiceConnection.onCustomTabsServiceConnected | REACHABLE | FRAMEWORK | new edge from CustomTabActivityHelper.bindCustomTabsService (label_148.py); support-library callback INFERRED | ServiceConnection.java:27, 36-39; CustomTabActivityHelper.java:96-104 |
| ServiceConnection.onServiceDisconnected | REACHABLE | FRAMEWORK | new edge from CustomTabActivityHelper.bindCustomTabsService (label_148.py); INFERRED | ServiceConnection.java:42-45 |
| Sound.getMediaCompletionListener | REACHABLE | CALL | auto CALL from VideoPlayer$1.onCompletion route; S_VIDEOPLAYER reached via ENTERS edge (label_145.py) | label_099.md:14 (copied row); VideoPlayer.java:54 |
| Sound.notifyConfigurationChanged | REACHABLE | CALL | auto CALL; S_VIDEOPLAYER reached via ENTERS edge (label_145.py) | label_099.md:20 (copied row); VideoPlayer.java:73-75 |
| StrokeWrap.<init> | REACHABLE | CALL | auto CALL | label_125.md:35 (copied row) |
| StrokeWrap.getStrokeSize | REACHABLE | CALL | auto CALL | label_125.md:36 (copied row) |
| SyncErrorDialog$6.onNeutral | REACHABLE | GUI | existing edge S_DLG_SYNC_ERROR -> onNeutral (graph_def.py:5903; label_045.py:56) | label_045.md:30 (copied row) |
| SyncErrorDialog$6.onPositive | REACHABLE | GUI | existing edge S_DLG_SYNC_ERROR -> onPositive (graph_def.py:5895; label_045.py:48) | label_045.md:31 (copied row) |
| TranslationActivity$1.<init> | REACHABLE | CALL | auto CALL | label_049.md:31 (copied row) |
| TranslationActivity$1.onClick | REACHABLE | GUI | existing edge S_TRANSLATION -> onClick (graph_def.py:6356; label_049.py:24) | label_049.md:32 (copied row) |
| VideoPlayer$1.<init> | REACHABLE | CALL | auto CALL from VideoPlayer.surfaceCreated; S_VIDEOPLAYER reached via ENTERS edge (label_145.py) | label_039.md:16 (copied row); VideoPlayer.java:50 |
| VideoPlayer$1.onCompletion | REACHABLE | FRAMEWORK | existing edge S_VIDEOPLAYER -> onCompletion (graph_def.py:4870; label_039.py:7) | label_039.md:17 (copied row) |
| WidgetStatus.fetchDue | REACHABLE | CALL | pending: needs part 080 ASYNC pair (see notes); auto CALL from NotificationService.onStartCommand | NotificationService.java:60; label_080.md:23 (copied row) |
| WidgetStatus.fetchSmall | REACHABLE | CALL | pending: needs part 080 ASYNC pair (see notes); auto CALL from buildUpdate | AnkiDroidWidgetSmall.java:138; label_080.md:24 (copied row) |

## Notes on pending rows (not written in label_148.py)

- Part 080 owns WidgetStatus.update -> WidgetStatus$UpdateDeckStatusAsyncTask.doInBackground and doInBackground -> onPostExecute (ASYNC). The 080 header says so, and parts 135, 140 and 146 say the same. Until part 080 writes them, these three rows (UpdateService$1.<init>, fetchSmall, fetchDue) stay UNRESOLVED in out/.
- The Statistics batch owns the cancel(true) ASYNC edges into AnkiStatsTaskHandler$CreateChartTask.onCancelled and CreateStatisticsOverview.onCancelled (graph_def.py:7590-7594 note). Parts 144 and 145 do not yet contain them, so these two rows stay UNRESOLVED until one of those parts writes them.

STATUS: DONE 2026-10-30 14:04 EDT (label_148.py passes ast.parse; the build was not run)
