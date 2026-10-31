# G1-5 CategoryEditorFragment$CategoryAdapter.hasItem (checker G1)

- Label: REACHABLE (show_route: confirmed_by=INFERRED, path=UNCHECKED)
- Steps: 25 (show_route.py --dedupe; copy in scratchpad g1_5_route.txt); checked: 25
- Verdict: WRONG (5 wrong steps: 10, 12, 14, 19, 23)

## WRONG steps

**Step 10** RecentListFragment.onCreateView -> RecentListAdapter.onBindViewHolder (FRAMEWORK)
- Same first-resume shortcut as G1-2 step 10 and G1-3 step 10. onCreateView only sets the adapter (RecentListFragment.java:182). Rows bind after the loader delivers data: onLoadFinished (:268-271), setItems (:464-468).
- Fix: graph_def.py:2309 remove onBindViewHolder from the onCreateView tuple. Add onLoadFinished -> setItems (CALL, guard 'recentListVersion.get() == loadedVersion (RecentListFragment.java:269)') and setItems -> onBindViewHolder (FRAMEWORK, non_standard, needs_state NEED_RECENT, :464-468).

**Step 12** RecentListAdapter$1.onClick -> S_STUDY (ENTERS, graph_def.py:460)
- Page-entry shortcut. The row tap starts StudyActivity (RecentListFragment.java:416-422). The Study page is shown by StudyActivity.onPostInit (graph_def.py:608, needs NEED_CARD), after onCreate, startInit and the loaders. The route skips all of that and then uses the Study menu (step 13), which needs the activity to exist.
- The guard at :460 (getSelectedItemCount() == 0) is correct, and it is a guard= field.
- Fix: delete graph_def.py:460. Keep the INTENT edge at :594 (to StudyActivity.<init>) and add guard='getSelectedItemCount() == 0 (RecentListFragment.java:416-422)'; :594 has the guard in its text only. The page then comes from StudyActivity.onPostInit (:608).

**Step 14** StudyActivity.onOptionsItemSelected -> StudyActivity.showCategoriesDialog (CALL, auto edge)
- The call at StudyActivity.java:164 sits in the else-if chain for `itemId == R.id.menu_memo_category` (:163-165). The edge has no guard=.
- Fix: EDIT guard for key ('StudyActivity.onOptionsItemSelected', 'StudyActivity.showCategoriesDialog'): guard='itemId == R.id.menu_memo_category (StudyActivity.java:163-164)'.

**Step 19** CategoryEditorFragment.onCreateView -> CategoryEditorFragment$InitTask.doInBackground (ASYNC)
- The call is real (CategoryEditorFragment.java:77-78, unconditional). But AsyncTask runs InitTask.onPreExecute on the main thread first (:135-141). It creates categoryAdapter (:137) and sets the list adapter (:140). onPostExecute (:154-165) and step 25's hasItem use that adapter. The route omits this hop, so this is a missing hop, not a wrong endpoint.
- Fix: add ASYNC CategoryEditorFragment.onCreateView -> InitTask.onPreExecute and InitTask.onPreExecute -> InitTask.doInBackground (both ASYNC, CategoryEditorFragment.java:135-141). Keep doInBackground -> onPostExecute. The graph has no onPreExecute node for this task (grep).

**Step 23** CategoryEditorFragment$1.onClick -> CategoryEditorFragment$NewCategoryTask.doInBackground (ASYNC)
- (a) No guard=. The call is inside `if (v == newButton)` (CategoryEditorFragment.java:111); the guard is in the description text only.
- (b) Missing hop. NewCategoryTask.onPreExecute (:241-246) runs first. It calls disableListeners() and sets editText (:244). doInBackground reads editText (:250, createOrReturn(editText)). The route skips onPreExecute, so editText would be null.
- Fix: add guard='v == newButton (CategoryEditorFragment.java:111)' to this edge. Add ASYNC $1.onClick -> NewCategoryTask.onPreExecute and NewCategoryTask.onPreExecute -> doInBackground (CategoryEditorFragment.java:241-246). Keep doInBackground -> onPostExecute.

## Steps checked OK
- 1-9: same chain as G1-4 steps 1-9 (AndroidManifest.xml:23-46; AnyMemo.java:115-141, guard :124-134; :187; :263; listener guards :240-241 and :249-257; RecentListFragment lifecycle :127-226; INFERRED androidx).
- 6: guard itemId == recent_tab_menu (AnyMemo.java:240-241). OK.
- 11: row tap, needs_state NEED_RECENT (RecentListFragment.java:413-428). OK once step 10 is fixed.
- 13: FRAMEWORK tap on a Study menu item to StudyActivity.onOptionsItemSelected (StudyActivity.java:144-145; graph_def.py:610). OK.
- 15: showCategoriesDialog -> CategoryEditorFragment.<init> (StudyActivity.java:516), unconditional. Precondition: a current card. Line 521 calls getCurrentCard().getCategory() when there is no category filter, before df.show at :528. The route gets that state only through StudyActivity.onPostInit (step 12 fix).
- 16-18: DialogFragment lifecycle <init> -> onAttach -> onCreate -> onCreateView (CategoryEditorFragment.java:50-64, args read at :59-61, onCreateView at :71). INFERRED androidx.
- 20: doInBackground -> onPostExecute (ASYNC; main thread). OK; onPreExecute hop is covered by step 19.
- 21: onPostExecute -> enableListeners (:170), unconditional within onPostExecute (:153-172). OK.
- 22: enableListeners (:412-417) -> CategoryEditorFragment$1.onClick (buttonOnClickListener, :94). $1 is the first anonymous class in the file (class file CategoryEditorFragment$1.class exists; $2 is listItemClickListener at :404). OK.
- 24: NewCategoryTask.doInBackground (:249-250) -> onPostExecute (:258). OK; onPreExecute hop is covered by step 23.
- 25: onPostExecute -> CategoryAdapter.hasItem (CategoryEditorFragment.java:261), unconditional within onPostExecute (:258-263). hasItem is declared at :348 in CategoryAdapter (:328). Needs categoryAdapter set by InitTask.onPreExecute (step 19 fix).

## Could not check / INFERRED
- androidx fragments, DialogFragment, RecyclerView, AppCompat, AsyncTask and Material: library source not read (INFERRED labels).
- hasItem body (CategoryEditorFragment.java:348 onward) not read; it is the route endpoint only.
- Study menu inflation (onCreateOptionsMenu) not read (step 13 is a gui edge).
