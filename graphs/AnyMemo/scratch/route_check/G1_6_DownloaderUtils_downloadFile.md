# G1-6 DownloaderUtils.downloadFile (checker G1)

- Label: REACHABLE (show_route: confirmed_by=INFERRED, path=UNCHECKED)
- Steps: 24 (show_route.py --dedupe; copy in scratchpad g1_6_route.txt); checked: 24
- Verdict: WRONG (5 wrong steps: 12, 17, 18, 22, 24)
- AGENT_NOTES claim checked: steps 12 and 24 cite the right lines (DownloadTabFragment.java:64-66; AnyMemoDownloaderFragment.java:85), but neither edge has a guard= field, so both are wrong here.

## WRONG steps

**Step 12** DownloadTabFragment.onClick -> AnyMemoDownloaderActivity.<init> (ENTRY)
- The startActivity is inside `if (v == amButton)` (DownloadTabFragment.java:64-66). show_route prints no guard line; the condition is in the description text only.
- Fix: graph_def.py:1372 add guard='v == amButton (DownloadTabFragment.java:64)'.

**Step 17** AbstractDownloaderFragment.onCreateView@AM -> DownloadListAdapter$1.onClick@AM (FRAMEWORK)
- First-resume shortcut (same as G1-2 step 10 and G1-5 step 10). onCreateView (:139-167) builds an empty adapter (:158, :163) and adds no rows. Rows arrive via onViewCreated -> refreshList (:170-173) -> RetrieveTask (:179-188) -> onPostExecute -> dlAdapter.addList (:229-230; add() at :369-372). The row click is set in getView (:386, :409), which runs when the list lays out those rows. The route skips all of that.
- The graph's onCreateView -> getView edge (graph_def.py:1121) has the same problem.
- Fix: graph_def.py:1121-1122 remove onCreateView as source. Add RetrieveTask.onPostExecute -> DownloadListAdapter.addList (CALL, :229-230), addList -> getView (FRAMEWORK, :369-373, ArrayAdapter notifies the list; INFERRED), keep getView -> onClick (:409). The chain before it is graph_def.py:1140-1145 (onViewCreated -> refreshList -> RetrieveTask -> $1.call -> onPostExecute). Also fix the description at graph_def.py:1118, which says onCreateView builds the row click (it does not).

**Step 18** AbstractDownloaderFragment$DownloadListAdapter$1.onClick@AM -> showFetchDatabaseDialog@AM (CALL)
- The call is the else branch (AbstractDownloaderFragment.java:433-435), after the `di == null` return (:413-416) and the Category (:417) and Back (:425) branches. No guard= field; the condition is in the description text only.
- Fix: graph_def.py:1130 add guard='di != null and di is neither Category nor Back (AbstractDownloaderFragment.java:413-435; else at :433)'.

**Step 22** AbstractDownloaderFragment.startFetchDatabaseTask@AM -> FetchDatabaseTask.doInBackground@AM (ASYNC)
- AsyncTask runs onPreExecute (main thread) before doInBackground (INFERRED platform rule). FetchDatabaseTask.onPreExecute (:305-313) creates and shows the ProgressDialog. The graph has a direct edge from startFetchDatabaseTask to doInBackground (graph_def.py:1136) that skips onPreExecute. The onPreExecute node (graph_def.py:1135) has no outgoing edge, so the route never passes through it. Same missing-hop pattern as G1-5 step 19.
- Fix: delete (or sup) graph_def.py:1136; add ASYNC FetchDatabaseTask.onPreExecute -> FetchDatabaseTask.doInBackground (AbstractDownloaderFragment.java:305-316). Keep :1135 and :1138. The RetrieveTask pair at graph_def.py:1141-1142 has the same shape.

**Step 24** AnyMemoDownloaderFragment.fetchDatabase -> DownloaderUtils.downloadFile (CALL, auto edge)
- Line 85 is the .zip branch: `else if` on fileName ending with .zip at :83, reached only when the .db test at :79 is false. graphs/AnyMemo/auto_calls.json has one record for this pair, at line 85, and graph_def.py has no EDIT guard for this key. The edge has no guard.
- auto_calls.json has no record at line 81 (the .db call), so the .db path has no edge.
- Fix: EDIT guard for key ('AnyMemoDownloaderFragment.fetchDatabase', 'DownloaderUtils.downloadFile'): guard='fileName ends with .zip, not .db (AnyMemoDownloaderFragment.java:79, 83-85)'. Covering the .db path needs a hand edge with guard 'fileName ends with .db (:79-81)' and a decision on the duplicate key.

## Steps checked OK
- 1-5: same edges as G1-4 steps 1-7 (AndroidManifest.xml:23-46; AnyMemo.java:115-141, guard :124-134; :187; :263 library dispatch, INFERRED). Checked in G1-4; not re-read here.
- 6: guard itemId == recent_tab_menu (AnyMemo.java:240-241). OK.
- 7: GUI tap on bottom nav (INFERRED Material). OK.
- 8: guard itemId == download_tab_menu (AnyMemo.java:247-248); replace at :254-256 under `fragment != null` (:253). OK.
- 9-10: onAttach (DownloadTabFragment.java:46-50); onCreateView (:52-61) with listeners at :58-59. OK (INFERRED androidx).
- 11: tap dispatches to onClick; listeners registered at :58-59. OK.
- 13-14: AnyMemoDownloaderActivity.java:9-13 (setContentView at :12); res/layout/anymemo_downloader.xml:2-7 <fragment android:name=...AnyMemoDownloaderFragment>. OK (INFERRED).
- 15: AnyMemoDownloaderFragment.java:35-39 injects downloaderUtils (@Inject at :33) before fetchDatabase uses it (:77-85). OK. The page is entered at fragment creation, the same pattern as S_MAIN_DOWNLOAD (steps 8-9).
- 16: onCreateView (AbstractDownloaderFragment.java:139-167) is the page's view. Edge OK; description wrong (see step 17).
- 19: showFetchDatabaseDialog :276-291; .show() at :291 is unconditional. ENTERS OK; its guard comes from step 18.
- 20: $2 numbering checked: anonymous classes at :182 ($1, Callable), :284 ($2, OnClickListener), :346 ($3, loadMoreOnClickListener); freeDebug has $1-$3. OK.
- 21: :286-287 inside onClick, unconditional. OK.
- 23: :317-319 inside try; fetchDatabase is virtual and dispatches to AnyMemoDownloaderFragment.fetchDatabase (:75). OK.

## Could not check / INFERRED
- androidx Fragment/DialogFragment dispatch, Material BottomNavigationView, AsyncTask thread model: library source not read (INFERRED labels).
- DownloaderUtils.downloadFile body not read (route endpoint only).
