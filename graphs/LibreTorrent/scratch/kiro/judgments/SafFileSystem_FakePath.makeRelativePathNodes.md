# Judgment: SafFileSystem$FakePath.makeRelativePathNodes

Route print: graphs/LibreTorrent/scratch/route_print/SafFileSystem_FakePath.makeRelativePathNodes.txt (26 steps). Judged by Kiro (lead), 2026-11-03, by Appendix D.

Steps 1-22: same nodes and edges as first-draw row 19 (SafFileSystem$FakePath.safRoot), edge-identical through step 25; re-read steps 22-23 in this print. Graded TRUE on that judged prefix.

| step | edge | from -> to | action true? | condition true? | grade | printed file:lines / note |
|---|---|---|---|---|---|---|
| 1 | Ef4711e98 | S_ENTRY -> MainActivity.onCreate | yes | yes | TRUE | judged prefix; SRC AndroidManifest.xml:43-59; FW-SRC core/java/android/app/ActivityThread.java:2727-2732; core/java/android/app/Instrumentation.java:1212-1215 |
| 2 | Ed8e7f5f9 | MainActivity.onCreate -> MainFragment.<init> | yes | yes | TRUE | judged prefix; SRC ui/main/MainActivity.java:182-185; res/values/layouts.xml:1-4; notouch/layouts.xml:1-4; res/layout/activity_main_drawer.xml:22-28; res/layout/activity_main_two_pane.xml:26-32; ui/main/MainFragment |
| 3 | Ee453d286 | MainFragment.<init> -> MainFragment.onAttach | yes | yes | TRUE | judged prefix; SRC ui/main/MainFragment.java:85-87,223-230 |
| 4 | E28c54333 | MainFragment.onAttach -> MainFragment.onCreateView | yes | yes | TRUE | judged prefix; SRC ui/main/MainFragment.java:223-230,113-122 |
| 5 | E2e46bfdf | MainFragment.onCreateView -> MainFragment.onViewCreated | yes | yes | TRUE | judged prefix; SRC ui/main/MainFragment.java:115-127 |
| 6 | E3b5adb16 | MainFragment.onViewCreated -> TorrentListAdapter.onBindViewHolder | yes | yes | TRUE | judged prefix; SRC ui/main/MainFragment.java:136-155; ui/main/TorrentListAdapter.java:74-104 |
| 7 | E9d948322 | TorrentListAdapter.onBindViewHolder -> TorrentListAdapter$ViewHolder.bind | yes | yes | TRUE | judged prefix; SRC ui/main/TorrentListAdapter.java:88-104,171-202 |
| 8 | Ef521ec44 | TorrentListAdapter$ViewHolder.bind -> TorrentListAdapter$ViewHolder.lambda$bind$0 | yes | yes | TRUE | judged prefix; SRC ui/main/TorrentListAdapter.java:189-196; FW-SRC core/java/android/view/View.java:6289-6305 |
| 9 | Efe87970e | TorrentListAdapter$ViewHolder.lambda$bind$0 -> MainFragment.onItemClicked | yes | yes | TRUE | judged prefix; SRC ui/main/TorrentListAdapter.java:189-196; ui/main/MainFragment.java:378-384 |
| 10 | Ee6073c26 | MainFragment.onItemClicked -> MsgMainViewModel.torrentDetailsOpened | yes | yes | TRUE | judged prefix; SRC ui/main/MainFragment.java:378-384 |
| 11 | E9fb4a1ea | MsgMainViewModel.torrentDetailsOpened -> MainActivity.showDetailTorrent | yes | yes | TRUE | judged prefix; SRC ui/main/MsgMainViewModel.java:30-40; ui/main/MainActivity.java:437-440; ui/main/MainFragment.java:378-384 |
| 12 | E883c34be | MainActivity.showDetailTorrent -> DetailTorrentActivity.onCreate | yes | yes | TRUE | judged prefix; SRC ui/main/MainActivity.java:669-673; AndroidManifest.xml:139; FW-SRC core/java/android/app/ActivityThread.java:2727-2732; core/java/android/app/Instrumentation.java:1212-1215 |
| 13 | E87241f3c | DetailTorrentActivity.onCreate -> DetailTorrentFragment.onAttach | yes | yes | TRUE | judged prefix; SRC ui/detailtorrent/DetailTorrentActivity.java:53-78; SRC ui/detailtorrent/DetailTorrentFragment.java:139-145 |
| 14 | E2c864273 | DetailTorrentFragment.onAttach -> DetailTorrentFragment.onCreateView | yes | yes | TRUE | judged prefix; SRC ui/detailtorrent/DetailTorrentFragment.java:147-153 |
| 15 | Efd617da3 | DetailTorrentFragment.onCreateView -> DetailTorrentFragment.onViewCreated | yes | yes | TRUE | judged prefix; SRC ui/detailtorrent/DetailTorrentFragment.java:155-221 |
| 16 | E00bf2e7e | DetailTorrentFragment.onViewCreated -> DetailPagerAdapter.createFragment | yes | yes | TRUE | judged prefix; SRC ui/detailtorrent/DetailTorrentFragment.java:185-212; ui/detailtorrent/DetailPagerAdapter.java:48-73 |
| 17 | Ef51bc0e5 | DetailPagerAdapter.createFragment -> DetailTorrentFilesFragment.onViewCreated | yes | yes | TRUE | judged prefix; SRC ui/detailtorrent/DetailPagerAdapter.java:59-60; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:193-289 |
| 18 | Ef41957c6 | DetailTorrentFilesFragment.onViewCreated -> TorrentContentFilesAdapter.onBindViewHolder | yes | yes | TRUE | judged prefix; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:205-208; ui/detailtorrent/pages/files/TorrentContentFilesAdapter.java:85-92 |
| 19 | E8ff2bbfd | TorrentContentFilesAdapter.onBindViewHolder -> TorrentContentFilesAdapter$ViewHolder.bind | yes | yes | TRUE | judged prefix; SRC ui/detailtorrent/pages/files/TorrentContentFilesAdapter.java:85-92 |
| 20 | Edbafd5b4 | TorrentContentFilesAdapter$ViewHolder.bind -> DetailTorrentFilesFragment.onItemClicked | yes | yes | TRUE | judged prefix; SRC ui/detailtorrent/pages/files/TorrentContentFilesAdapter.java:166-171; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:207; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragm |
| 21 | E8f02bbd2 | DetailTorrentFilesFragment.onItemClicked -> DetailTorrentViewModel.getFilePath | yes | yes | TRUE | judged prefix; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:340; SRC ui/detailtorrent/DetailTorrentViewModel.java:262-292 |
| 22 | E86642109 | DetailTorrentViewModel.getFilePath -> FileSystemFacadeImpl.getFileUri(String,Uri) | yes | yes | TRUE | judged prefix; SRC ui/detailtorrent/DetailTorrentViewModel.java:262-275; SRC FileSystemFacadeImpl.java:144-150 |
| 23 | E58e81758 | FileSystemFacadeImpl.getFileUri(String,Uri) -> SafFsModule.getFileUri(String,Uri) | yes | no | FALSE | resolveFsByUri(torrent.downloadPath) picks SafFsModule only for content:// (FileSystemFacadeImpl.java:144-150; FsModuleResolverImpl.java:42-49; SafFileSystem.java:191-198); a fresh install can only store file:// download paths (see SafFileSystem$FakePath.serialize judgment, judge_saf.txt) |
| 24 | E856ccd7c | SafFsModule.getFileUri(String,Uri) -> SafFileSystem.getFileUri(FakePath,boolean) | - | - | NOT REACHED | follows step 23 |
| 25 | Ec45f82f9 | SafFileSystem.getFileUri(FakePath,boolean) -> SafFileSystem.getFile(FakePath,boolean) | - | - | NOT REACHED | follows step 23 |
| 26 | Ec5f0acef | SafFileSystem.getFile(FakePath,boolean) -> SafFileSystem$FakePath.makeRelativePathNodes | - | - | NOT REACHED | follows step 23 |

**Route verdict: WRONG.** Step 23, edge E58e81758 (FileSystemFacadeImpl.getFileUri(String,Uri) -> SafFsModule.getFileUri(String,Uri)) FALSE: the torrent download path is file://. Same decisive edge as first-draw row 19.
