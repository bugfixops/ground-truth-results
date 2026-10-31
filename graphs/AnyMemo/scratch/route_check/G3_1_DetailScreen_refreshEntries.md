# G3-1: DetailScreen.refreshEntries (checker G3, route 1 of 6)

- Method: DetailScreen.refreshEntries
- Label: REACHABLE
- Steps: 22. Checked: 22 (every step read against its cited lines, guards around each call included).
- Verdict: WRONG (4 wrong steps: 10, 12, 14, 16)

Route (show_route.py, --dedupe): S_ENTRY, AnyMemo.onCreate, loadUiComponents, initDrawer, AnyMemo$2 (@INIT), RecentListFragment lifecycle, onCreateView, RecentListAdapter.onBindViewHolder, adapter $1.onClick, S_STUDY, Study menu, S_PREVIEW_EDIT, PreviewEdit menu, S_DETAIL, Detail menu, save dialog, DetailScreen$1.onClick, SaveCardTask.doInBackground, saveEntries, refreshEntries.

## WRONG steps

Step 10. RecentListFragment.onCreateView -> RecentListFragment$RecentListAdapter.onBindViewHolder (FRAMEWORK, non_standard). The edge is written by the loop at graph_def.py:2309 (tuple) and 2312-2316 (e call).
- Code: RecentListFragment.java:182 sets the adapter in onCreateView, but the adapter list is empty then. Rows come only from RecentListLoaderCallbacks.onLoadFinished (RecentListFragment.java:268-270: `recentListAdapter.setItems(ril)`), started from onResume (RecentListFragment.java:218). setItems (RecentListFragment.java:464-467) fills items and calls notifyDataSetChanged. With no items RecyclerView calls neither onBindViewHolder nor onCreateViewHolder.
- Fix: in the loop at graph_def.py:2309-2316 keep only onDraw and getItemOffsets from onCreateView. Remove getItemCount, onCreateViewHolder, onBindViewHolder from onCreateView. Add hand edges: RecentListFragment$RecentListLoaderCallbacks.onLoadFinished -> RecentListFragment$RecentListAdapter.setItems (CALL, guard `recentListVersion.get() == loadedVersion`, SRC RecentListFragment.java:269-270) and RecentListFragment$RecentListAdapter.setItems -> RecentListFragment$RecentListAdapter.onBindViewHolder (FRAMEWORK, non_standard via RecyclerView, needs_state data "the recent list has at least one deck", SRC RecentListFragment.java:466-467). The existing onResume -> onCreateLoader edges (graph_def.py:447) stay.

Step 12. RecentListFragment$RecentListAdapter$1.onClick -> S_STUDY (ENTERS). Edge at graph_def.py:460.
- Code: RecentListFragment.java:416-422 calls context.startActivity(StudyActivity). The start runs StudyActivity.onCreate (StudyActivity.java:119-121 loader setup), then onPostInit (graph_def.py:608 is the only edge that reaches S_STUDY with the card loaded). The route jumps over both, then taps the Study menu, which exists only after onCreateOptionsMenu.
- Fix: delete the ENTERS edge at graph_def.py:460. The same tap already has an INTENT edge to StudyActivity.<init> (graph_def.py:594, SRC RecentListFragment.java:417-422), and that edge goes through StudyActivity.onCreate (route 2 of G3 reads it). S_STUDY is then entered only by StudyActivity.onPostInit (graph_def.py:608, needs_state NEED_CARD).

Step 14. StudyActivity.onOptionsItemSelected -> S_PREVIEW_EDIT (ENTERS). Edge at graph_def.py:626.
- Code: StudyActivity.java:175-177 calls gotoPreviewEdit(), which (StudyActivity.java:701-709) calls startActivity(PreviewEditActivity). The route skips PreviewEditActivity.onCreate (PreviewEditActivity.java:96-98) and its onPostInit (PreviewEditActivity.java:140; graph_def.py:877). The next step taps the PreviewEdit menu, which needs onCreateOptionsMenu (PreviewEditActivity.java:245).
- Fix: change the target at graph_def.py:626 to PreviewEditActivity.<init>, kind ENTRY (the convention of graph_def.py:840 and 871; <init> then reaches onCreate by lc_chain). S_PREVIEW_EDIT stays entered only through PreviewEditActivity.onPostInit (graph_def.py:877). The menu tap itself (StudyActivity.onOptionsItemSelected branch, text "menu_context_gotoprev") is a gesture, so no guard is needed.

Step 16. PreviewEditActivity.onOptionsItemSelected -> S_DETAIL (ENTERS, guard getCurrentCard() != null). Edge at graph_def.py:894.
- Code: PreviewEditActivity.java:277-282 calls startActivityForResult(DetailScreen). The route skips DetailScreen.onCreate (DetailScreen.java:82-100: setContentView and every findViewById field). It also skips InitTask (DetailScreen.java:103-104): InitTask.doInBackground (DetailScreen.java:264-274) sets helper, cardDao, currentCard, and InitTask.onPostExecute (DetailScreen.java:277-282) fills the fields. Without them refreshEntries (DetailScreen.java:172-187) and saveEntries (189-193) throw a null pointer (cardDao, currentCard, the EditText fields).
- Fix: change the target at graph_def.py:894 to DetailScreen.<init>, kind ENTRY, keep the guard `getCurrentCard() != null` (PreviewEditActivity.java:278). S_DETAIL then comes only from DetailScreen$InitTask.onPostExecute (graph_def.py:849). The same error sits at graph_def.py:613 (StudyActivity.onOptionsItemSelected -> S_DETAIL, needs_state NEED_CARD): change it to DetailScreen.<init>, kind ENTRY, too. It is not on this route.

## Steps checked and OK (with notes)

1 manifest LAUNCHER entry (AndroidManifest.xml:23-33): OK.
2 AnyMemo.<init> -> onCreate (LIFECYCLE): OK. The FW-SRC citation in the graph has no line numbers; the lines I read are fw_src core/java/android/app/Activity.java:6989-6999 (performCreate calls onCreate). Add them to the citation.
3 onCreate -> loadUiComponents (AnyMemo.java:124-141): OK. The guard and ENV text match the code (SDK_INT <= Q and permission granted; the else branch at 136-140 is not taken on API 27).
4 loadUiComponents -> initDrawer (AnyMemo.java:187): OK, unguarded call.
5 initDrawer -> AnyMemo$2.onNavigationItemSelected@INIT (non_standard, setSelectedItemId at AnyMemo.java:263): OK as INFERRED. The Material BottomNavigationView dispatch is not read (library source not available here).
6 AnyMemo$2 -> RecentListFragment.<init> (guard itemId == recent_tab_menu, AnyMemo.java:240-241): OK.
7-9 fragment lifecycle <init> -> onAttach -> onCreate -> onCreateView: OK (INFERRED androidx FragmentManager, RecentListFragment.java:135, 128, 169).
11 onBindViewHolder -> adapter $1.onClick (RecentListFragment.java:413): OK; the listener is attached per bound row.
13 S_STUDY -> StudyActivity.onOptionsItemSelected (menu tap): OK once step 12 is fixed.
15 S_PREVIEW_EDIT -> PreviewEditActivity.onOptionsItemSelected: OK once step 14 is fixed.
17 S_DETAIL -> DetailScreen.onOptionsItemSelected (detail_screen_menu.xml has @+id/save): OK once step 16 is fixed.
18 onOptionsItemSelected -> S_DLG_DETAIL_SAVE (`save` branch, DetailScreen.java:117-131): OK (menu tap is a gesture).
19 S_DLG_DETAIL_SAVE -> DetailScreen$1.onClick (only anonymous class of DetailScreen before line 122): OK.
20 DetailScreen$1.onClick -> SaveCardTask.doInBackground (ASYNC, DetailScreen.java:125-126): OK as INFERRED (AsyncTask.execute, platform flow not read).
21 doInBackground -> saveEntries (DetailScreen.java:217, inside try, unguarded): OK.
22 saveEntries -> refreshEntries (DetailScreen.java:190, unconditional): OK.

## Not checked

- BottomNavigationView.setSelectedItemId dispatch, androidx FragmentManager, LoaderManager and RecyclerView callbacks: library source not available; INFERRED as the graph says.
- AsyncTask.execute ordering: platform flow not read beyond the base class.
