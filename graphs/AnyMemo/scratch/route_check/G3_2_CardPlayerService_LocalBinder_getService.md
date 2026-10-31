# G3-2: CardPlayerService$LocalBinder.getService (checker G3, route 2 of 6)

- Method: CardPlayerService$LocalBinder.getService
- Label: REACHABLE
- Steps: 22. Checked: 22 (each step read against its cited lines, guards included).
- Verdict: WRONG (3 wrong steps: 10, 18, 19)

Route (show_route.py --dedupe): S_ENTRY, AnyMemo.<init>, AnyMemo.onCreate, loadUiComponents, initDrawer, AnyMemo$2 (@INIT), RecentListFragment.<init>, onAttach, onCreate, onCreateView, RecentListAdapter.onBindViewHolder, adapter $1.onClick, StudyActivity.<init>, StudyActivity.onCreate, QACardActivity.startInit, SettingLoaderCallbacks.onCreateLoader, onLoadFinished, QACardActivity$2.run, CardPlayerActivity.onPostInit, CardPlayerService.onCreate, onBind, CardPlayerActivity$3.onServiceConnected, LocalBinder.getService.

## WRONG steps

Step 10. RecentListFragment.onCreateView -> RecentListFragment$RecentListAdapter.onBindViewHolder (FRAMEWORK, non_standard). Edge written by the loop at graph_def.py:2306-2315 (the onBindViewHolder pair at line 2309).
- Code: onCreateView sets the adapter (RecentListFragment.java:182), but the adapter is empty then. Rows come only from RecentListLoaderCallbacks.onLoadFinished (RecentListFragment.java:268-270, setItems), which runs after onResume (RecentListFragment.java:216-220). setItems (464-467) calls notifyDataSetChanged. With no items, RecyclerView calls no onBindViewHolder.
- Fix: in the loop at graph_def.py:2306-2315 keep only onDraw and getItemOffsets for onCreateView; remove getItemCount, onCreateViewHolder, onBindViewHolder. Add these edges: RecentListLoaderCallbacks.onLoadFinished -> RecentListAdapter.setItems (CALL, SRC RecentListFragment.java:269-270) and setItems -> onBindViewHolder (FRAMEWORK, non_standard, needs_state data "at least one deck is in the recent list", SRC RecentListFragment.java:466-467).

Step 18. QACardActivity$2.run -> CardPlayerActivity.onPostInit (CALL, graph_def.py:430, CHA expansion).
- Code: QACardActivity.java:658-662 (onPostInitRunnable.run calls onPostInit()) runs on the instance that stored it (startInit registers it at QACardActivity.java:166-168). In this route that instance is the StudyActivity started at step 12, whose loader fires the runnable. The virtual call goes to StudyActivity.onPostInit (graph_def.py:426-427 already has that edge), not to CardPlayerActivity.onPostInit.
- The CHA expansion at graph_def.py:430 links the shared node to every QACardActivity subclass. The comment at graph_def.py:424-425 says this is a cross-host route, but the edge is still there.
- Fix: sup((QACardActivity$2.run, QACardActivity.onPostInit)) at graph_def.py:430, then split QACardActivity$2.run per host (@STUDY, @QUIZ, @CARD_PLAYER, @PREVIEW_EDIT), each variant with one CALL edge to its own host's onPostInit. The loader edges at graph_def.py:420 and 422 need a host variant for each host that owns the loader. The bytecode cannot say which host it is, so each variant needs its own hand edge.

Step 19. CardPlayerActivity.onPostInit -> CardPlayerService.onCreate (ENTRY, graph_def.py:1240, bindCardPlayerService). Missing STATE.
- Code: CardPlayerActivity.java:111 calls bindCardPlayerService() before the null check at 112-114. bindCardPlayerService (210-215) reads getCurrentCard().getId() at line 213 (EXTRA_CURRENT_CARD_ID), so with no card it throws a NullPointerException before bindService runs. The card comes from cardDao.queryForId / queryFirstOrdinal (CardPlayerActivity.java:103-107), which return null for an empty deck.
- Fix: add needs_state=NEED_CARD (graph_def.py:159, "The open deck has at least one card", data) to the edge at graph_def.py:1240.

## Steps checked and OK (with notes)

1 S_ENTRY -> AnyMemo.<init> (AndroidManifest.xml:23-33, LAUNCHER): OK.
2 AnyMemo.<init> -> AnyMemo.onCreate (LIFECYCLE): OK. Citation has no lines; add FW-SRC core/java/android/app/Activity.java:6989-6999 (performCreate calls onCreate).
3 onCreate -> loadUiComponents (AnyMemo.java:124-141): OK. Guard matches code (SDK_INT <= Q and permission granted).
4 loadUiComponents -> initDrawer (AnyMemo.java:187): OK.
5 initDrawer -> AnyMemo$2.onNavigationItemSelected@INIT (AnyMemo.java:263): OK as INFERRED (BottomNavigationView dispatch not read).
6 AnyMemo$2 -> RecentListFragment.<init> (AnyMemo.java:240-241): OK.
7-9 fragment <init> -> onAttach -> onCreate -> onCreateView: OK, INFERRED (androidx FragmentManager; RecentListFragment.java:127-226).
11 onBindViewHolder -> $1.onClick (RecentListFragment.java:413): OK; needs_state data holds once step 10 is fixed.
12 $1.onClick -> StudyActivity.<init> (INTENT, RecentListFragment.java:416-422): OK.
13 StudyActivity.<init> -> onCreate: OK (lifecycle via performCreate; add the FW-SRC line numbers).
14 StudyActivity.onCreate -> QACardActivity.startInit (StudyActivity.java:121, bytecode): OK.
15 startInit -> SettingLoaderCallbacks.onCreateLoader (QACardActivity.java:162-168): OK, INFERRED (androidx LoaderManager).
16 onCreateLoader -> onLoadFinished (ASYNC, DBLoader worker thread): OK, INFERRED.
17 onLoadFinished -> QACardActivity$2.run (graph_def.py:420, needs_state LOADERS_DONE; MultipleLoaderManager.java:104-114; QACardActivity.java:167): OK as an edge. The target is the shared node that step 18 breaks.
20 CardPlayerService.onCreate -> onBind (CardPlayerService.java:79-83, 87-109; FW-SRC ActivityThread.java:3311-3339): OK.
21 onBind -> CardPlayerActivity$3.onServiceConnected (INFERRED bindService callback; CardPlayerActivity.java:221-227): OK.
22 onServiceConnected -> LocalBinder.getService (CardPlayerActivity.java:226, bytecode): OK.

## Not checked

- androidx LoaderManager, FragmentManager and RecyclerView callbacks; BottomNavigationView dispatch; bindService platform path beyond ActivityThread.handleBindService. Library source not available: INFERRED as the graph says.
