# Judgment: FileItem.<init>(int,String,boolean,long)

Route print: graphs/LibreTorrent/scratch/route_print/FileItem.<init>(int,String,boolean,long).txt (12 steps). Judged by Kiro (lead), 2026-11-03, by Appendix D.

Steps 1-1: same nodes and edges as first-draw row 5 step 1 (exported AddTorrentActivity, ENV other_app). Graded TRUE on that judged prefix.

| step | edge | from -> to | action true? | condition true? | grade | printed file:lines / note |
|---|---|---|---|---|---|---|
| 1 | Ec711e542 | S_ENTRY -> AddTorrentActivity.onCreate | yes | yes | TRUE | judged prefix; SRC AndroidManifest.xml:62-92; FW-SRC core/java/android/app/ActivityThread.java:2727-2732; core/java/android/app/Instrumentation.java:1212-1215 |
| 2 | E3176d46a | AddTorrentActivity.onCreate -> AddTorrentActivity.initLayout | yes | yes | TRUE | AddTorrentActivity.java:136-140 |
| 3 | Ee09520a5 | AddTorrentActivity.initLayout -> AddTorrentPagerAdapter.createFragment | yes | yes | TRUE | offscreen page limit = NUM_FRAGMENTS creates both pages (AddTorrentActivity.java:288-290; AddTorrentPagerAdapter.java:41-50) |
| 4 | E0085b998 | AddTorrentPagerAdapter.createFragment -> AddTorrentFilesFragment.newInstance | yes | yes | TRUE | position FILES_FRAG_POS (AddTorrentPagerAdapter.java:45-46) |
| 5 | Eb9fb47a2 | AddTorrentFilesFragment.newInstance -> AddTorrentFilesFragment.onAttach | yes | yes | TRUE | fragment lifecycle |
| 6 | E3910c3c3 | AddTorrentFilesFragment.onAttach -> AddTorrentFilesFragment.onCreateView | yes | yes | TRUE | fragment lifecycle |
| 7 | E8fd4f6b9 | AddTorrentFilesFragment.onCreateView -> AddTorrentFilesFragment.onViewCreated | yes | yes | TRUE | fragment lifecycle |
| 8 | E64667477 | AddTorrentFilesFragment.onViewCreated -> AddTorrentFilesFragment.onStart | yes | yes | TRUE | AddTorrentFilesFragment.java:103-109 |
| 9 | E0a529f46 | AddTorrentFilesFragment.onStart -> AddTorrentFilesFragment.subscribeAdapter | yes | yes | TRUE | AddTorrentFilesFragment.java:108 |
| 10 | E308bc858 | AddTorrentFilesFragment.subscribeAdapter -> AddTorrentFilesFragment.lambda$subscribeAdapter$0 | yes | yes (valid .torrent from the other app) | TRUE | children is a BehaviorSubject (AddTorrentViewModel.java:95) fed by makeFileTree after decode (AddTorrentActivity.java:345; AddTorrentViewModel.java:368-401,450-451); a torrent with at least one file gives a non-empty list. Prints: judge_files.txt |
| 11 | E02a038f2 | AddTorrentFilesFragment.lambda$subscribeAdapter$0 -> DownloadableFileItem.<init>(BencodeFileTree) | yes | yes | TRUE | map(DownloadableFileItem::new) (AddTorrentFilesFragment.java:115-118) |
| 12 | E850d53c3 | DownloadableFileItem.<init>(BencodeFileTree) -> FileItem.<init>(int,String,boolean,long) | yes | yes | TRUE | super(tree.getIndex(), tree.getName(), tree.isFile(), tree.size()) (DownloadableFileItem.java:35) |

**Route verdict: CORRECT.** Premise: another app opens a valid .torrent with at least one file in AddTorrentActivity (ENV other_app).
