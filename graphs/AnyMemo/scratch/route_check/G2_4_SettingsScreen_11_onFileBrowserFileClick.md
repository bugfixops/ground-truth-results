# G2-4 route check: SettingsScreen$11.onFileBrowserFileClick

- Method: SettingsScreen$11.onFileBrowserFileClick = the anonymous listener `qTypefaceEditFbListener` (SettingsScreen.java:737-743). Naming by javac source order: $6 is onPostInitRunnable (268), $10 is settingFieldOnClickListener (640), $11 is this listener (737).
- Label: REACHABLE
- Steps: 21; checked: 21 (every step read in the source)
- Verdict: WRONG (3 wrong steps: 12, 17, 21)

Rule used: a step is WRONG if the transition cannot happen, or if its guard or STATE is false or missing. Kind labels and skipped hops that do not change the outcome are listed separately and not counted.

## Wrong steps

**Step 12. SettingsScreen.<init> -> SettingsScreen$SettingLoaderCallbacks.onCreateLoader (FRAMEWORK; graph_def.py:950)**
- The loader is registered and started in SettingsScreen.onCreate (SettingsScreen.java:137-139), not in the constructor. The graph has no SettingsScreen.onCreate node or lifecycle edge (grep finds none), so the route jumps from <init> straight to onCreateLoader.
- Fix: add a LIFECYCLE edge SettingsScreen.<init> -> SettingsScreen.onCreate, and make the loader edge start at SettingsScreen.onCreate.

**Step 17. SettingsScreen$10.onClick -> S_DLG_TYPEFACE_Q (ENTERS; graph_def.py:992)**
- The guard `v == qTypefaceEdit` is right (SettingsScreen.java:712-721). The missing part is the STATE: qTypefaceEdit is VISIBLE only when the question font is set (updateViews, SettingsScreen.java:467-473) or after the Q checkbox is ticked (658-661). Setting.questionFont defaults to "" (entity/Setting.java:89), so on the empty-db route from step 11 the field is GONE and cannot be tapped.
- The route is reachable only through a prior tap on qTypefaceCheckbox (same listener, step 16) or a saved question font.
- Fix: add a STATE text to the edge (`question typeface field VISIBLE: Q checkbox ticked or font set`). The builder ignores guard text, so also add the checkbox tap as a hand edge to that state, so the cheapest route goes through it.

**Step 21. FileBrowserFragment.openFile@SETTINGS_Q -> SettingsScreen$11.onFileBrowserFileClick (CALL; no guard in graph)**
- Source FileBrowserFragment.java:402-416: `if (clickedFile.isDirectory()) browseTo(...); else if (clickedFile.isFile()) { ...; if (onFileClickListener != null) onFileClickListener.onFileBrowserFileClick(clickedFile); ... }`. The listener is reached only for a regular file (line 407). A directory row or ".." browses instead (line 405).
- The graph gives this edge no guard (the route dump shows none), so the guard is missing.
- Fix: add a GATE entry for (`FileBrowserFragment.openFile@SETTINGS_Q`, `SettingsScreen$11.onFileBrowserFileClick`) with guard text `clickedFile.isFile() (FileBrowserFragment.java:407); a directory or ".." row browses instead`. The edge comes from the FB_TARGET mapping (graph_def.py:521, SETTINGS_Q).

## Steps checked as OK (short)
- 1-2 cold start, as in G2-1 steps 1-2 (manifest; AnyMemo.<init> -> onCreate).
- 3 onCreate -> loadUiComponents, guard API <= Q and permission granted (AnyMemo.java:124-141; ENV on the route).
- 4 loadUiComponents -> initDrawer (AnyMemo.java:187). 5 initDrawer -> listener via setSelectedItemId (263; material library not read).
- 6 guard itemId == recent_tab_menu (240-241). 7 GUI tap on the bottom bar (listener 234-261). 8 guard itemId == misc_tab_menu (249-250).
- 9 MiscTabFragment.onCreateView lifecycle (INFERRED FragmentManager). 10 onCreateView -> onClick: all buttons share the listener (156-194).
- 11 ENTRY, guard v == defaultSettingsButton (MiscTabFragment.java:339-344; button set at 202-203; misc_tab.xml:392, visible). Kind is a click, so GUI would fit better; not counted.
- 13 loader ASYNC onCreateLoader -> onLoadFinished (SettingsScreen.java:398-408).
- 14 onLoadFinished -> checkAllLoadersCompleted -> handler.post (MultipleLoaderManager.java:104-114). Only one loader is registered here, so the STATE holds.
- 15 onPostInitRunnable.run -> updateViews (SettingsScreen.java:268-353; call at 348; definition at 416).
- 16 updateViews -> settingFieldOnClickListener.onClick (listeners at 323-331, 658 onward).
- 18 DialogFragment show -> FileBrowserFragment.onCreateView. The listener is set at SettingsScreen.java:719 before show (720), so the SETTINGS_Q host is non-null.
- 19 row click set in onBindViewHolder (FileBrowserFragment.java:514-519, after the empty-name return at 483-485).
- 20 row click -> openFile(selectedFileName) (517).

## Not checked
- androidx DialogFragment, LoaderManager and RecyclerView source not read (INFERRED reasons kept for steps 9, 13, 14, 16, 18, 19).
- The anonymous class numbers ($6, $10, $11) were matched by javac source order, not by javap.
- The default font value on the real empty-db row was assumed from the entity default "" (not read from the DB).
