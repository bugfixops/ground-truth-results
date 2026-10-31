# G4-1: ShareUtil.<init>

- Method: ShareUtil.<init>
- Label: REACHABLE (cold start AnyMemo -> bottom nav Open tab -> OpenTabFragment row -> OpenActionsFragment -> Dagger provider)
- Steps: 19 (show_route.py --dedupe). Checked: 19.
- Verdict: WRONG (3 wrong steps: 9, 10, 12; steps 9 and 10 share one root cause)

## Wrong steps

Step 9: S_MAIN_OPEN -> FileBrowserFragment.onCreateView@OPEN (LIFECYCLE), graph_def.py:548 (loop over FB_PAGES).
- Wrong: the route enters onCreateView straight from the page. The Open tab is OpenTabFragment, whose onAttach sets the file-click listener (OpenTabFragment.java:35-38, `setOnFileClickListener(fileClickListener);`). The file list is filled only by onResume -> browseTo (FileBrowserFragment.java:208-212, `browseTo(currentDirectory);`). Steps 10 and 12 both need these, and the route skips both.
- Fix: for S_MAIN_OPEN only, remove the direct page edges in the loops at graph_def.py:537-541 (onAttach/onCreate/onCreateView/onResume) and :547-549 (onCreateView@OPEN). Keep S_MAIN_OPEN -> OpenTabFragment.onAttach (graph_def.py:586) and add hand edges: OpenTabFragment.onAttach -> FileBrowserFragment.onCreate (LIFECYCLE), FileBrowserFragment.onCreate -> FileBrowserFragment.onCreateView@OPEN (LIFECYCLE), FileBrowserFragment.onCreateView@OPEN -> FileBrowserFragment.onResume (LIFECYCLE).

Step 10: FileBrowserFragment.onCreateView@OPEN -> FileBrowserFragment$FileBrowserAdapter$1.onClick@OPEN (FRAMEWORK), graph_def.py:550.
- Wrong: the row click listener is set in FileBrowserAdapter.onBindViewHolder (FileBrowserFragment.java:480, `holder.itemView.setOnClickListener(...)` at :514-518), not in onCreateView (:183-206, which only sets an empty adapter at :202-203). A row exists only after browseTo (:222) calls fileListAdapter.setItems (:272), which calls notifyDataSetChanged (:594-614).
- Fix: change the source of graph_def.py:550 to FileBrowserFragment$FileBrowserAdapter.onBindViewHolder, and add a hand edge FileBrowserFragment.browseTo -> FileBrowserFragment$FileBrowserAdapter.onBindViewHolder (FRAMEWORK; RecyclerView binds the rows after notifyDataSetChanged; androidx source not read, so INFERRED). Same error at graph_def.py:2579 (onBindViewHolder from onCreateView, the comment says "while it lays out the file rows"): its source must also be browseTo, not onCreateView.

Step 12: FileBrowserFragment.openFile@OPEN -> OpenTabFragment$1.onFileBrowserFileClick (CALL), graph_def.py:531 (loop over FB_CALLERS, OPEN branch).
- Wrong: the edge has no guard. The code guards it: the name is not "." or ".." (FileBrowserFragment.java:388-392); clickedFile != null (:402); clickedFile.isFile() (:407; a directory goes to browseTo at :405 instead); onFileClickListener != null (:412, else notifyFileClick at :415). The listener is set only by OpenTabFragment.onAttach (step 9), so the route also needs that state.
- Fix: add guard='row is a file, not "." or ".." (FileBrowserFragment.java:388-412); onFileClickListener != null (set by OpenTabFragment.onAttach, OpenTabFragment.java:38)' to this edge. Easiest: a {'guard': ...} entry for ('FileBrowserFragment.openFile@OPEN', 'OpenTabFragment$1.onFileBrowserFileClick') in the dict at graph_def.py:2786.

## Steps checked and OK

- 1 ENTRY: AndroidManifest.xml:23-46 (MAIN/LAUNCHER on ui.AnyMemo) OK.
- 2 onCreate: AnyMemo.java:116-143 OK.
- 3 onCreate -> loadUiComponents: guard (API <= 29 and WRITE_EXTERNAL_STORAGE granted) matches AnyMemo.java:124-134; the API > 29 else branch (:136-140) does not apply on API 27. OK.
- 4 loadUiComponents -> initDrawer: AnyMemo.java:187 inside loadUiComponents (:184). OK.
- 5 initDrawer -> AnyMemo$2.onNavigationItemSelected@INIT: setSelectedItemId at :263, listener set earlier at :234 in the same method (:205-265). Library dispatch INFERRED (material BottomNavigationView, not read).
- 6 guard itemId == recent_tab_menu (:240-241) OK.
- 7 tap on bottom nav: INFERRED (material), listener at :234-261 OK.
- 8 guard itemId == open_tab_menu (:242-246), commit at :253-257 OK.
- 11 onClick -> openFile: FileBrowserFragment.java:514-519 OK.
- 13 OpenTabFragment$1.onFileBrowserFileClick -> OpenActionsFragment.<init>: OpenTabFragment.java:42-47 (no if in the body) OK.
- 14-15 OpenActionsFragment <init> -> onAttach -> onCreate: OpenActionsFragment.java:70-82 OK (DialogFragment lifecycle INFERRED).
- 16 onCreate -> Dagger inject: OpenActionsFragment.java:78 OK.
- 17-18 Dagger generated injector -> provider: INFERRED (generated code, no source; @Inject field at OpenActionsFragment.java:63).
- 19 ActivityModules.providesShareUtil -> ShareUtil.<init>: ActivityModules.java:29-32 (@Provides, `return new ShareUtil(activity);`, no guard) OK.

## Not checked

- androidx Fragment/DialogFragment/RecyclerView and the material BottomNavigationView dispatch: source not in the tree; INFERRED stays.
- Dagger generated classes: no source file; INFERRED stays.
