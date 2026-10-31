# G3-5: FileBrowserFragment$3.<init> (checker G3, route 5 of 6)

- Method: FileBrowserFragment$3.<init>
- Label: not re-checked here (the route is what this file checks)
- Steps: 19. Checked: 19 (each step read against its cited lines, guards included).
- Verdict: WRONG (8 wrong steps: 6, 8, 9, 11, 12, 13, 18, 19)

Route (show_route.py --dedupe): S_ENTRY, AnyMemo.<init>, AnyMemo.onCreate, loadUiComponents, initDrawer, AnyMemo$2 (@INIT), S_MAIN_RECENT, AnyMemo$2.onNavigationItemSelected (tap), S_MAIN_MISC, MiscTabFragment.onCreateView, MiscTabFragment.onClick, S_DLG_EXPORT_ANYMEMO, FileBrowserFragment.onCreateView@EXPORT, FileBrowserAdapter$1.onClick@EXPORT, FileBrowserFragment.openFile@EXPORT, ExportAnyMemoDbFragment$1.onFileBrowserFileClick, ExportAnyMemoDbFragment.exportDatabase, ExportAnyMemoDbFragment.onActivityResult, FileBrowserFragment.onActivityResult, FileBrowserFragment$3.<init>.

## WRONG steps

Step 6. AnyMemo$2.onNavigationItemSelected@INIT -> S_MAIN_RECENT (ENTERS, graph_def.py:338, guard recent_tab_menu). The page is entered without RecentListFragment.<init>, onAttach, onCreate or onCreateView. The code builds the fragment at AnyMemo.java:240-241 (the CALL from $2@INIT already exists) and commits it at 253-257. The route takes this ENTERS because it is cheaper. Fix: delete the ENTERS at 338 and enter S_MAIN_RECENT after RecentListFragment.onCreateView. Same for graph_def.py:339 and 340 (OPEN, DOWNLOAD).

Step 8. AnyMemo$2.onNavigationItemSelected -> S_MAIN_MISC (ENTERS, graph_def.py:361, guard misc_tab_menu). Same shortcut: it skips MiscTabFragment.<init> (CALL at graph_def.py:347; AnyMemo.java:249-250), onAttach, onCreate and onCreateView (MiscTabFragment.java:128-222). Fix: delete the ENTERS at 361 and enter S_MAIN_MISC after MiscTabFragment.onCreateView, reached through the CALL at 347.

Step 9. S_MAIN_MISC -> MiscTabFragment.onCreateView (LIFECYCLE, graph_def.py:1377 loop). The edge is sourced from the page, which onCreateView itself builds, so it runs backwards. It also skips onAttach, which sets mActivity (MiscTabFragment.java:129-131) and is used by the export click (255), and onCreate, which injects and creates disposables (143-146). Fix: delete the page-sourced loop at 1377; add MiscTabFragment.<init> -> onAttach -> onCreate -> onCreateView lifecycle edges.

Step 11. MiscTabFragment.onClick -> S_DLG_EXPORT_ANYMEMO (ENTERS, graph_def.py:1380, needs_state NEED_DECK). The code (MiscTabFragment.java:253-256) constructs `new ExportAnyMemoDbFragment()` and calls df.show(...). The ENTERS skips that construction and onCreate (ExportAnyMemoDbFragment.java:33-41), which sets the file-click listener step 15 needs. Fix: delete the ENTERS at 1380; add MiscTabFragment.onClick -> ExportAnyMemoDbFragment.<init> (CALL), then onCreate (edge at 1052) -> onCreateView, and enter S_DLG_EXPORT_ANYMEMO after onCreateView. The STATE text on 1380 ("a deck was opened at least once ... recent list / Download folder") does not match the code: the export list shows the current folder (browseTo, FileBrowserFragment.java:222-232). Rewrite it as "the folder listing has at least one file".

Step 12. S_DLG_EXPORT_ANYMEMO -> FileBrowserFragment.onCreateView@EXPORT (LIFECYCLE, FB_PAGES loop near graph_def.py:537-548). Same backwards page-sourced edge as step 9; the list is built by onCreateView, which must run before the page. Fix: remove the S_DLG_EXPORT_ANYMEMO entries from the FB_PAGES lifecycle loop (this also covers onResume at the same loop) and use ExportAnyMemoDbFragment.onCreate -> FileBrowserFragment.onCreateView (inherited) -> S_DLG_EXPORT_ANYMEMO.

Step 13. FileBrowserFragment.onCreateView@EXPORT -> FileBrowserAdapter$1.onClick@EXPORT (FRAMEWORK, graph_def.py:550-551 loop). The row click listener is set in onBindViewHolder (FileBrowserFragment.java:480, 514-519), and rows exist only after onResume -> browseTo (216-232; fill at 228) -> fill -> setItems (272; 596, 614). onCreateView sets an empty adapter (202-203) and loads no rows. This is the same error as G3-1 step 10. Fix: delete the onCreateView -> row-click edges at 550-551 for all hosts; add browseTo -> fill -> setItems -> onBindViewHolder (FRAMEWORK, needs_state "the folder listing has at least one file") -> row click@v.

Step 18. ExportAnyMemoDbFragment.onActivityResult -> FileBrowserFragment.onActivityResult (CALL, ExportAnyMemoDbFragment.java:96-97). The edge is missing its guard. The super call runs only in the else branch (96-100), which requires NOT (requestCode == REQUEST_CODE_EXPORT_DB 1002 && RESULT_OK && data != null && getData() != null), the check at line 64. The forwarded requestCode is still 1002, not 1001. Fix: add that negated guard to the edge. The successful result goes to the write at 64-95 instead.

Step 19. FileBrowserFragment.onActivityResult -> FileBrowserFragment$3.<init> (CALL, bytecode; the listener is created at FileBrowserFragment.java:342). Infeasible on this route. The listener is created only inside the import branch: requestCode == REQUEST_CODE_IMPORT_DB (1001, line 106) && RESULT_OK && data != null && getData() != null (326) && newFile.exists() (338). Step 18 forwards 1002, so line 326 is false and the code reaches super at 354. The realizable origin is the import menu item (FileBrowserFragment.java:311-316, startActivityForResult at 315) -> RESULT at graph_def.py:571 -> onActivityResult. Fix: remove the export path to this node; put the guard from lines 326 and 338 on the CALL edge; take the origin from graph_def.py:571.

## Steps checked and OK (with notes)

1 S_ENTRY -> AnyMemo.<init> (AndroidManifest.xml:23-33, LAUNCHER): OK.
2 <init> -> onCreate (LIFECYCLE): OK; add FW-SRC core/java/android/app/Activity.java:6989-6999 to the citation.
3 onCreate -> loadUiComponents (AnyMemo.java:124-141; guard API <= 29 and permission granted): OK.
4 loadUiComponents -> initDrawer (AnyMemo.java:187): OK.
5 initDrawer -> AnyMemo$2.onNavigationItemSelected@INIT (AnyMemo.java:263, non_standard): OK as INFERRED; the material library dispatch was not read.
7 S_MAIN_RECENT -> AnyMemo$2.onNavigationItemSelected (GUI, graph_def.py:332-333 loop, tap a bottom-nav item): OK.
10 MiscTabFragment.onCreateView -> onClick (FRAMEWORK; listeners set at MiscTabFragment.java:156-221): OK once step 9 is fixed (the export click needs mActivity).
14 FileBrowserAdapter$1.onClick@EXPORT -> openFile@EXPORT (CALL, FileBrowserFragment.java:514-519): OK once step 13 is fixed.
15 openFile@EXPORT -> ExportAnyMemoDbFragment$1.onFileBrowserFileClick (CALL; guard isFile() at FileBrowserFragment.java:407 and onFileClickListener != null at 412): OK. The listener exists only after ExportAnyMemoDbFragment.onCreate (33-41), which the step 11-12 fixes supply.
16 $1.onFileBrowserFileClick -> exportDatabase (CALL, ExportAnyMemoDbFragment.java:39-41): OK.
17 exportDatabase -> onActivityResult (RESULT, startActivityForResult at ExportAnyMemoDbFragment.java:51; graph_def.py:2339): OK.

## Not checked

- Material BottomNavigationView dispatch (step 5) and androidx FragmentManager commit timing: INFERRED as the graph says.
- Whether any other FileBrowserFragment host (or MiscTabFragment's own import branch at line 418) reaches the import menu item: not traced. Only the origin named in step 19 was checked.
