# G3-6: CardDaoImpl.getCardsByCategory (checker G3, route 6 of 6)

- Method: CardDaoImpl.getCardsByCategory
- Label: not re-checked here (the route is what this file checks)
- Steps: 22. Checked: 22 (each step read against its cited lines, guards included).
- Verdict: WRONG (5 wrong steps: 10, 12, 14, 16, 21)

Route (show_route.py --dedupe): S_ENTRY, AnyMemo.<init>, AnyMemo.onCreate, loadUiComponents, initDrawer, AnyMemo$2 (@INIT), RecentListFragment.<init>, onAttach, onCreate, onCreateView, RecentListAdapter.onBindViewHolder, RecentListAdapter$3.onClick, S_DLG_OPEN_ACTIONS, OpenActionsFragment$1.onClick, S_DLG_QUIZ_LAUNCHER, QuizLauncherDialogFragment$2.onClick, QuizActivity.<init>, QuizActivity.onCreate, QuizQueueManagerLoaderCallbacks.onCreateLoader, QuizQueueManagerLoader.dbLoadInBackground, QuizQueueManager$Builder.build, QuizQueueManager.refill(Category), CardDaoImpl.getCardsByCategory.

## WRONG steps

Step 10. RecentListFragment.onCreateView -> RecentListAdapter.onBindViewHolder (FRAMEWORK, graph_def.py:2309). Same error as G3-1 step 10: the adapter is empty in onCreateView (RecentListFragment.java:182); rows come only from onLoadFinished -> setItems (268-270, 464-467). Fix as in G3-1 step 10.

Step 12. RecentListAdapter$3.onClick -> S_DLG_OPEN_ACTIONS (ENTERS, graph_def.py:472). Same error as G3-4 step 12: it skips OpenActionsFragment construction and onCreateView (OpenActionsFragment.java:90-114), which set the button listeners the GUI edge at graph_def.py:1354 needs. Fix: delete the ENTERS at 472 (the CALL at 471 and lc_chain at 1344 already model construction and lifecycle) and enter S_DLG_OPEN_ACTIONS after OpenActionsFragment.onCreateView.

Step 14. OpenActionsFragment$1.onClick -> S_DLG_QUIZ_LAUNCHER (ENTERS, graph_def.py:1358, guard v == quizItem). Same error as the G3-4 step 14 note: it skips QuizLauncherDialogFragment construction, onAttach, onCreate and onCreateDialog (QuizLauncherDialogFragment.java:120-213), which build the dialog and attach the listeners. The real start is the CALL at graph_def.py:683 (OpenActionsFragment.java:147-153) with the lc_chain at 684-685. Fix: delete the ENTERS at 1358 and enter S_DLG_QUIZ_LAUNCHER after onCreateDialog. The same shortcut sits at 1355, 1356, 1359, 1360 and 1366 (see G3-4).

Step 16. QuizLauncherDialogFragment$2.onClick -> QuizActivity.<init> (ENTRY, graph_def.py:696; guard both radios not checked). The route takes the group branch (QuizLauncherDialogFragment.java:255-266). Only the category branch sets EXTRA_CATEGORY_ID (line 237), so QuizActivity.categoryId stays -1 (QuizActivity.java:123), the loader's filterCategory is null (QuizActivity.java:264-268), and refill(Category) is never reached. The default group radio is checked (quiz_launcher_dialog.xml:14-15), so the route must first tap the category radio (QuizLauncherDialogFragment$1.onCheckedChanged, radio listener at line 216; graph_def.py:688) and pick a category (category button $3.onClick at 270-274, graph_def.py:700; then S_DLG_CATEGORY_QUIZ -> QuizLauncherDialogFragment$10.onReceiveCategory, lines 520-531, which sets categoryId at 524). Fix: use the category edge at graph_def.py:694 (ENTRY, guard quizByCategoryRadio is checked, needs_state QZ_CAT_STATE) and add those steps before step 15.

Step 21. QuizQueueManager$Builder.build -> QuizQueueManager.refill(Category) (CALL, QuizQueueManager.java:199-202). The edge lacks its guard. refill(filterCategory) runs only in the else of `if (filterCategory == null)` (line 199), so only when filterCategory != null. That needs EXTRA_CATEGORY_ID != -1 (QuizActivity.java:123; dbLoadInBackground 266-268) and a category row found by queryForId. With filterCategory null the call is refill(startOrd, quizSize) (line 200) instead. Fix: add guard "filterCategory != null (QuizQueueManager.java:199-202)" and needs_state "the category id from EXTRA_CATEGORY_ID exists in the category table (QuizActivity.java:266-268)".

## Steps checked and OK (with notes)

1-9: same as G3-1 steps 1-9 (AnyMemo cold start, loadUiComponents guard at AnyMemo.java:124-141, initDrawer at 187, AnyMemo$2 @INIT, RecentListFragment.<init> guard at 240-241, lifecycle <init> -> onAttach -> onCreate -> onCreateView). OK.
11 onBindViewHolder -> $3.onClick (FRAMEWORK with STATE "at least one entry", graph_def.py:470; RecentListFragment.java:442-452): OK once step 10 is fixed.
13 S_DLG_OPEN_ACTIONS -> OpenActionsFragment$1.onClick (GUI, graph_def.py:1354): OK once step 12 is fixed.
15 S_DLG_QUIZ_LAUNCHER -> QuizLauncherDialogFragment$2.onClick (GUI, "Tap Start quiz", graph_def.py:689): OK as a gesture. javac numbering checked: the radio listener at line 216 is $1, the start listener at 231 is $2, the category button at 270 is $3, and onReceiveCategory at 521 is $10, which matches the graph. The category-branch precondition is charged to step 16.
17 QuizActivity.<init> -> onCreate (LIFECYCLE): OK.
18 onCreate -> QuizQueueManagerLoaderCallbacks.onCreateLoader (FRAMEWORK; registerLoaderCallbacks and startInit at QuizActivity.java:131-133): OK.
19 onCreateLoader -> QuizQueueManagerLoader.dbLoadInBackground (ASYNC, loader.forceLoad; graph_def.py:658): OK, INFERRED (androidx loader worker thread not read).
20 dbLoadInBackground -> QuizQueueManager$Builder.build (CALL, QuizActivity.java:282, unconditional): OK.
22 QuizQueueManager.refill(Category) -> CardDaoImpl.getCardsByCategory (CALL, QuizQueueManager.java:115; field CardDao at line 38; CardDao.java:78 declares it; CardDaoImpl.java:572 implements it, and grep finds no other CardDao implementation): OK.

## Not checked

- androidx LoaderManager and AsyncTaskLoader worker dispatch (step 19), and RecyclerView callbacks (steps 10-11): library source not available; INFERRED as the graph says.
- Dagger injection of the CardDao instance into QuizQueueManager.Builder (dbOpenHelper.getCardDao()): not traced beyond the interface.
