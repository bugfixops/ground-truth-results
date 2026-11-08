# Judgment: SafFileSystem$FakePath.serialize

Route print: graphs/LibreTorrent/scratch/route_print/SafFileSystem_FakePath.serialize.txt (15 steps). Judged by Kiro (lead), 2026-11-03, by Appendix D.

Steps 1-12: same nodes and edges as first-draw row 5 (SafFileSystem$FakePath.normalizeRelativePath), edge-identical up to step 12 except step 10 (citation form only); re-read in this print. Graded TRUE on that judged prefix.

| step | edge | from -> to | action true? | condition true? | grade | printed file:lines / note |
|---|---|---|---|---|---|---|
| 1 | Ec711e542 | S_ENTRY -> AddTorrentActivity.onCreate | yes | yes | TRUE | judged prefix; SRC AndroidManifest.xml:62-92; FW-SRC core/java/android/app/ActivityThread.java:2727-2732; core/java/android/app/Instrumentation.java:1212-1215 |
| 2 | Ee1225b55 | AddTorrentActivity.onCreate -> AddTorrentActivity.onStart | yes | yes | TRUE | judged prefix; SRC ui/addtorrent/AddTorrentActivity.java:96-140,178-185; FW-SRC core/java/android/app/ActivityThread.java:2738-2745; core/java/android/app/Instrumentation.java:1333-1335 |
| 3 | Ee73669cc | AddTorrentActivity.onStart -> AddTorrentActivity.onPrepareOptionsMenu | yes | yes | TRUE | judged prefix; SRC ui/addtorrent/AddTorrentActivity.java:277-280,539-548 |
| 4 | Eae09e857 | AddTorrentActivity.onPrepareOptionsMenu -> AddTorrentActivity.onOptionsItemSelected | yes | yes | TRUE | judged prefix; SRC ui/addtorrent/AddTorrentActivity.java:539-562; FW-SRC core/java/android/app/Activity.java:3431-3451 |
| 5 | Ef943d0a6 | AddTorrentActivity.onOptionsItemSelected -> AddTorrentActivity.addTorrent | yes | yes | TRUE | judged prefix; SRC ui/addtorrent/AddTorrentActivity.java:552-562; ui/addtorrent/AddTorrentActivity.java:362-389 |
| 6 | E95dff3d5 | AddTorrentActivity.addTorrent -> AddTorrentViewModel.addTorrent | yes | yes | TRUE | judged prefix; SRC ui/addtorrent/AddTorrentActivity.java:362-389; ui/addtorrent/AddTorrentViewModel.java:466-520 |
| 7 | E3915b22f | AddTorrentViewModel.addTorrent -> AddTorrentViewModel.lambda$addTorrent$5 | yes | yes | TRUE | judged prefix; SRC ui/addtorrent/AddTorrentViewModel.java:527-536 |
| 8 | E7d8bf649 | AddTorrentViewModel.lambda$addTorrent$5 -> TorrentEngine.addTorrentSync(AddTorrentParams,boolean) | yes | yes | TRUE | judged prefix; SRC ui/addtorrent/AddTorrentViewModel.java:527-534 |
| 9 | Ed404c00b | TorrentEngine.addTorrentSync(AddTorrentParams,boolean) -> TorrentSessionImpl.addTorrent | yes | yes | TRUE | judged prefix; SRC TorrentEngine.java:412; SRC TorrentSessionImpl.java:251 |
| 10 | Eb1a24a4a | TorrentSessionImpl.addTorrent -> TorrentSessionImpl.download(String,AddTorrentParams,byte[]) | yes | yes | TRUE | judged prefix; SRC TorrentSessionImpl.java:251-310 |
| 11 | E8472da01 | TorrentSessionImpl.download(String,AddTorrentParams,byte[]) -> FileSystemFacadeImpl.makeFileSystemPath(Uri) | yes | yes | TRUE | judged prefix; SRC TorrentSessionImpl.java:328-341; SRC FileSystemFacadeImpl.java:248-251 |
| 12 | Ec2f76e6f | FileSystemFacadeImpl.makeFileSystemPath(Uri) -> FileSystemFacadeImpl.makeFileSystemPath(Uri,String) | yes | yes | TRUE | judged prefix; SRC FileSystemFacadeImpl.java:248-260; SRC FileSystemFacadeImpl.java:254-260 |
| 13 | E127a23cd | FileSystemFacadeImpl.makeFileSystemPath(Uri,String) -> SafFsModule.makeFileSystemPath | yes | no | FALSE | resolveFsByUri returns SafFsModule only for a content:// dir (FsModuleResolverImpl.java:42-49; SafFileSystem.java:191-198 isSafPath = scheme content). The add-torrent dir is pref.saveTorrentsIn() (AddTorrentViewModel.java:145-146,478) whose default is "file://" + download path (SettingsRepositoryImpl.java:102-103) and whose only writer is StorageSettingsFragment.java:267 fed by the in-app FileManagerDialog (StorageSettingsFragment.java:227-239), which returns Uri.fromFile (FileManagerViewModel.java:282); the per-torrent chooser is the same dialog (AddTorrentInfoFragment.java:160,192-213). So the dir is file:// and DefaultFsModule is chosen. Prints: scratch/kiro/prints/judge_saf.txt |
| 14 | E377479af | SafFsModule.makeFileSystemPath -> SafFileSystem$FakePath.toString | - | - | NOT REACHED | follows step 13 |
| 15 | E8085cfad | SafFileSystem$FakePath.toString -> SafFileSystem$FakePath.serialize | - | - | NOT REACHED | follows step 13 |

**Route verdict: WRONG.** Step 13, edge E127a23cd (FileSystemFacadeImpl.makeFileSystemPath(Uri,String) -> SafFsModule.makeFileSystemPath) FALSE: the download dir on this route is file://, so the resolver picks DefaultFsModule, not SafFsModule.
