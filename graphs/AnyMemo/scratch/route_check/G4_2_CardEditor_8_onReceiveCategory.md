# G4-2: CardEditor$8.onReceiveCategory

- Method: CardEditor$8.onReceiveCategory (the categoryResultListener of CardEditor, CardEditor.java:634-639)
- Label: REACHABLE (cold start AnyMemo -> Recent tab -> deck row -> StudyActivity -> Study menu Edit -> CardEditor -> category button -> category dialog)
- Steps: 21 (show_route.py --dedupe). Checked: 21.
- Verdict: WRONG (2 wrong steps: 10 and 21)

## Wrong steps

Step 10: RecentListFragment.onCreateView -> RecentListFragment$RecentListAdapter.onBindViewHolder (FRAMEWORK, non_standard), graph_def.py:2312 (loop over the adapter callbacks, one line per name).
- Wrong: the rows of the Recent list exist only after the loaders deliver data. The chain is RecentListFragment.onResume (RecentListFragment.java:216-219, restartLoader) -> AsyncTaskLoader loadInBackground -> RecentListLoaderCallbacks.onLoadFinished (:268-270, guarded by `recentListVersion.get() == loadedVersion`) -> RecentListAdapter.setItems (:464) -> notifyDataSetChanged (:467). onCreateView (:169-182) only builds an empty adapter and calls setAdapter (:182). The route skips onResume and the loader, so the STATE the next step needs (NEED_RECENT, "At least one entry exists") is never produced on this route.
- Fix: in the loop at graph_def.py:2312, take onBindViewHolder (and onCreateViewHolder) off onCreateView. Add FRAMEWORK edges RecentListFragment$RecentListLoaderCallbacks.onLoadFinished -> RecentListFragment$RecentListAdapter.onBindViewHolder and RecentListFragment$RecentListDetailLoaderCallbacks.onLoadFinished -> ... onBindViewHolder, each with the version guard as guard= (RecentListFragment.java:268-270 and :300-302, `compareAndSet(loadedVersion, loadedVersion + 1)`), and keep needs_state=NEED_RECENT (graph_def.py:158). The cold-start chain must reach onResume before onLoadFinished: add a LIFECYCLE edge RecentListFragment.onCreateView -> RecentListFragment.onResume (the existing onResume -> loader edges are at graph_def.py:447 and :450).

Step 21: S_DLG_CATEGORY_CARD -> CardEditor$8.onReceiveCategory (CALL, "a category is picked"), graph_def.py:775.
- Wrong: the guards of the call are missing. CategoryEditorFragment calls the listener only inside `if (v == okButton)` (CategoryEditorFragment.java:96) and `if (resultListener != null)` (:105), then `resultListener.onReceiveCategory(selectedCategory)` (:106). The category is null when no list row is checked (:100-101, `INVALID_POSITION`). Checked with CS.guard_of: ['v == okButton', 'resultListener != null'].
- The second guard is satisfied on this route: CardEditor$7.onClick sets it with setResultListener(categoryResultListener) at CardEditor.java:567, before df.show at :572. The first guard is the OK press, which the prose "a category is picked" does not say.
- Fix: add guard='the OK button is tapped (CategoryEditorFragment.java:96); resultListener != null, set by CardEditor$7.onClick (CardEditor.java:567) before show (:572); the category is null when no row is checked (:100-101)' to the edge at graph_def.py:775. Optionally change the label to "tap OK in the category dialog".

## Steps checked and OK

- 1 ENTRY: AndroidManifest.xml:23-46 OK.
- 2 onCreate: AnyMemo.java:116-143 OK.
- 3 onCreate -> loadUiComponents: guard matches AnyMemo.java:124-134 OK.
- 4 loadUiComponents -> initDrawer: AnyMemo.java:187 OK.
- 5 initDrawer -> AnyMemo$2.onNavigationItemSelected@INIT: setSelectedItemId at :263 after the listener at :234. Library dispatch INFERRED.
- 6 guard itemId == recent_tab_menu (AnyMemo.java:240-241) OK.
- 7 AnyMemo$2 -> RecentListFragment.<init> path and 8 onAttach -> onCreate: RecentListFragment.java:127-142 OK (androidx INFERRED).
- 9 onCreate -> onCreateView (LIFECYCLE): edge valid; the problem is step 10 (the route needs onResume after this).
- 11 onBindViewHolder -> RecentListAdapter$1.onClick: RecentListFragment.java:411-428; no enclosing if before the listener (guard_of = []). STATE NEED_RECENT is correct text for the click, but its producer is missing (step 10).
- 12 onClick -> S_STUDY: guard getSelectedItemCount() == 0 (RecentListFragment.java:416-422); startActivity(StudyActivity) with EXTRA_DBPATH = currentItem.dbPath (a deck path string, not a URI). OK.
- 13 S_STUDY -> StudyActivity.onOptionsItemSelected (FRAMEWORK, menu tap): StudyActivity.java:144-145 OK (AppCompat INFERRED).
- 14 guard itemId == menu_context_edit (StudyActivity.java:166-168); menu_context_edit is in res/menu/study_activity_menu.xml. OK.
- 15 showEditDialog -> CardEditor.<init> (ENTRY, startActivityForResult): StudyActivity.java:662-668; STATE "open deck has at least one card" matches getCurrentCard().getId(). OK.
- 16 CardEditor.<init> -> onCreate: CardEditor.java:101-107 OK.
- 17 onCreate -> InitTask.doInBackground: CardEditor.java:105-106 OK (AsyncTask INFERRED).
- 18 doInBackground -> onPostExecute: CardEditor.java:512-545 OK.
- 19 onPostExecute -> CardEditor$7.onClick: categoryButton.setOnClickListener at CardEditor.java:553 is not under an if (guard_of = []). OK.
- 20 CardEditor$7.onClick -> S_DLG_CATEGORY_CARD: CardEditor.java:567 (setResultListener) and :572 (df.show) OK. The page is the _CARD variant (not the STUDY/PREVIEW/QUIZ dialogs), so it goes to the right host.

## Not checked

- androidx Fragment / LoaderManager / RecyclerView and AsyncTask ordering: no source in the tree, so INFERRED stays.
- The Study menu's item visibility (menu XML, not read beyond the id presence) and the AppCompat options-menu dispatch: INFERRED.
