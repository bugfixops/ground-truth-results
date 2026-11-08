# G3-4: DetailScreen.loadEntries (checker G3, route 4 of 6)

- Method: DetailScreen.loadEntries
- Label: not re-checked here (the route is what this file checks)
- Steps: 22. Checked: 22 (each step read against its cited lines, guards included).
- Verdict: WRONG (4 wrong steps: 10, 12, 14, 20)

Route (show_route.py --dedupe): S_ENTRY, AnyMemo.<init>, AnyMemo.onCreate, loadUiComponents, initDrawer, AnyMemo$2 (@INIT), RecentListFragment.<init>, onAttach, onCreate, onCreateView, RecentListAdapter.onBindViewHolder, RecentListAdapter$3.onClick, S_DLG_OPEN_ACTIONS, OpenActionsFragment$1.onClick, S_CARD_LIST, CardListActivity$10.onItemLongClick, showListItemLongClickPopup, CardListActivity$2.onMenuItemClick, DetailScreen.<init>, DetailScreen.onCreate, InitTask.doInBackground, InitTask.onPostExecute, DetailScreen.loadEntries.

## WRONG steps

Step 10. RecentListFragment.onCreateView -> RecentListAdapter.onBindViewHolder (FRAMEWORK, graph_def.py:2309). Same error as G3-1 step 10 and G3-2 step 10: the adapter is empty in onCreateView (RecentListFragment.java:182), and rows arrive only from RecentListLoaderCallbacks.onLoadFinished -> setItems (RecentListFragment.java:268-270, 464-467). Fix as in G3-2 step 10 (loop at graph_def.py:2306-2315; add onLoadFinished -> setItems CALL, and setItems -> onBindViewHolder FRAMEWORK with needs_state data "at least one deck is in the recent list").

Step 12. RecentListAdapter$3.onClick -> S_DLG_OPEN_ACTIONS (ENTERS, graph_def.py:472, cites RecentListFragment.java:450 df.show). The route skips OpenActionsFragment's onCreateView, where the buttons get their listeners (OpenActionsFragment.java:90-114). The GUI edge at graph_def.py:1354 (S_DLG_OPEN_ACTIONS -> $1.onClick) needs those listeners. The CALL at graph_def.py:471 (RecentListFragment.java:446-451) and the lc_chain at graph_def.py:1344 already model construction and lifecycle. Fix: delete the ENTERS at 472 and add OpenActionsFragment.onCreateView -> S_DLG_OPEN_ACTIONS ENTERS (SRC OpenActionsFragment.java:85-117). The same shortcut sits at graph_def.py:589 (OpenTabFragment$1 -> S_DLG_OPEN_ACTIONS); not on this route.

Step 14. OpenActionsFragment$1.onClick -> S_CARD_LIST (ENTERS, graph_def.py:1357, guard `v == listItem`). The route skips CardListActivity.onCreate (CardListActivity.java:112-146, loader registration at 144-146) and the onPostInit runnable CardListActivity$11.run (640-655), which attaches the list adapter and the long-click listener (649). The real start is startActivity(CardListActivity) at OpenActionsFragment.java:139-145, which the ENTRY at graph_def.py:815 already models. Fix: delete the ENTERS at 1357. S_CARD_LIST is then entered only from CardListActivity$11.run (graph_def.py:823, needs NEED_CARD). The same shortcut sits at graph_def.py:1355, 1356, 1358-1360 and 1366 for the other action-sheet items. Each already has a matching INTENT/ENTRY/CALL edge (593, 871, 683, 947, 1012, 1245), so the same fix applies; none of those is on this route.

Step 20. DetailScreen.onCreate -> DetailScreen$InitTask.doInBackground (ASYNC, graph_def.py:847). The route skips InitTask.onPreExecute (DetailScreen.java:242-260). That method is the only place that sets dbPath (line 246) and cardId (line 249) from the intent extras, and doInBackground reads both (dbPath at 264, cardId at 269). Without it, doInBackground runs with dbPath null and cardId -1. The edge DetailScreen.onCreate -> onPreExecute exists (graph_def.py:1546), but no onPreExecute -> doInBackground edge exists, so the route takes the shortcut. Fix: delete the edge at 847 and add DetailScreen$InitTask.onPreExecute -> DetailScreen$InitTask.doInBackground (ASYNC, FW-SRC AsyncTask.java:645-650). The same pattern (direct edge to doInBackground beside an onPreExecute edge with no onPreExecute -> doInBackground edge) appears at graph_def.py:732 vs 1538 (CardEditor), 795 vs 1544 (CategoryEditorFragment) and 686 vs 1551 (QuizLauncherDialogFragment). Not on this route; not checked in depth.

## Steps checked and OK (with notes)

1-9: same as G3-1 steps 1-9 (manifest LAUNCHER entry, AnyMemo.<init>/onCreate, loadUiComponents guard at AnyMemo.java:124-141, initDrawer at 187, AnyMemo$2 @INIT inferred, RecentListFragment.<init> guard at 240-241, fragment lifecycle inferred). OK.
11 onBindViewHolder -> $3.onClick (FRAMEWORK, graph_def.py:470; RecentListFragment.java:442-452): OK. The more-button listener is attached per bound row. The STATE "at least one entry" holds once step 10 is fixed.
13 S_DLG_OPEN_ACTIONS -> OpenActionsFragment$1.onClick (GUI, graph_def.py:1354; OpenActionsFragment.java:119-201): OK once step 12 is fixed.
15 S_CARD_LIST -> CardListActivity$10.onItemLongClick (FRAMEWORK, graph_def.py:835, NEED_CARD): OK once step 14 is fixed. The long-click listener is set in $11.run (CardListActivity.java:649), so the page is valid only after the loaders finish. The state text "The open deck has at least one card" matches NEED_CARD.
16 $10.onItemLongClick -> showListItemLongClickPopup (CALL, graph_def.py:836; CardListActivity.java:442-443): OK.
17 showListItemLongClickPopup -> $2.onMenuItemClick (FRAMEWORK, graph_def.py:837; CardListActivity.java:215-233): OK. The popup and its listener are both created in this method. The page node S_CARD_LIST_ROW_LONGMENU (graph_def.py:1535) is skipped; that is a naming shortcut, not a wrong edge.
18 $2.onMenuItemClick -> DetailScreen.<init> (ENTRY, graph_def.py:839; CardListActivity.java:225-226, 243-248): OK. R.id.detail exists in res/menu/card_list_long_click_popup_menu.xml. The menu tap is a gesture, so no guard. Graph_def.py:844 is a duplicate of 839 with the same text; remove it.
19 DetailScreen.<init> -> onCreate (LIFECYCLE): OK.
21 doInBackground -> onPostExecute (ASYNC, graph_def.py:848): OK. Tighten the citation to DetailScreen.java:263-274 and 277-283 (the graph cites 262-283).
22 InitTask.onPostExecute -> DetailScreen.loadEntries (CALL, bytecode, DetailScreen.java:280): OK. loadEntries (153-161) reads currentCard, which doInBackground set at 269 before onPostExecute runs. No guard is needed: the card exists because the long-press came from a card row (step 15, NEED_CARD).

## Not checked

- AsyncTask.execute ordering and DialogFragment show internals: platform source not read; INFERRED as the graph says.
- androidx LoaderManager and RecyclerView callbacks: library source not available; INFERRED. MultipleLoaderManager.java:104-114 does post the runnable through handler, so the edge at graph_def.py:822 holds.
- Steps 5 and 7-9 (library dispatch): INFERRED.
