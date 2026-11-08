# Spot-check — batch 34 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json, plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). Row 16 is in both sets; checked once, under Changed. Verdicts D1–D36/R1–R5 are NOT re-decided. No work file edited.

## Changed rows (2)

- 34/3 FileTree.toString — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose (label, kind, confirmed_by correct per L1: definition FileTree.java:211-221; trigger sites ONLY inside now-UNREACHABLE host bodies — BencodeFileTree.toString:125-128 (33/8) and TorrentContentFileTree.toString:178 (34/16), both UNREACHABLE here; the `", parent=" + parent` concat inside its own body is self-type recursion, not an external trigger; zero other trigger in the L1 greps). Stale prose: the evidence cell still says "called only by BencodeFileTree.toString:125, which is itself OPEN (batch 33 row 8)" — but 33/8 is now UNREACHABLE, so the parenthetical that formed this row's OPEN rationale is false post-flip. (It does not contradict this row's own UNREACHABLE label — if anything the flip strengthens it — but it misstates the dependency state the row's justification rests on, so it is counted FAIL-prose, not PASS.)
- 34/16 TorrentContentFileTree.toString — UNREACHABLE no_trigger_in_app INFERRED — PASS. L1: definition TorrentContentFileTree.java:175-184; zero outside trigger in the L1 greps; DetailTorrentViewModel/AddTorrentViewModel fileTree use is method calls returning longs passed as format args — the tree object itself is never a format/log/concat arg. Work prose is neutral with Kind present and the Phase 3 note appended.

## Sample rows (7 sample-only)

- 34/1 FileTree.setType — OPEN — PASS. FileTree.java:159 (fresh fetch, batch 33); no printed caller (ctors set the field directly). OPEN confirmed_by is —, as required.
- 34/6 TorrentContentFileTree.\<init\>(String,long,int,TorrentContentFileTree) — REACHABLE SOURCE — PASS. DetailTorrentViewModel.java:237-238 (PARENT_DIR node); also TorrentContentFileTreeUtils.java makeObject:125 dir branch (fresh fetch).
- 34/11 TorrentContentFileTree.nonIgnoreFileSize — REACHABLE SOURCE — PASS. DetailTorrentViewModel.java checkFreeSpace: fileTree.nonIgnoreFileSize().
- 34/21 IPFilterImpl.\<init\> — REACHABLE SOURCE — PASS. TorrentSessionImpl.java parseIpFilterThread block (`new IPFilterImpl()`, parseFile call :731).
- 34/26 IPFilterParser.errLog — REACHABLE SOURCE — PASS. Private; called from parseDAT/parseP2P IPFilterParser.java:142,149,157,168,212,220,227,235,246 (fresh fetch; parseDAT/parseP2P REACHABLE, rows 27, 30).
- 34/31 PriorityConverter.\<clinit\> — REACHABLE INFERRED — PASS. Static SparseArray initialisers, PriorityConverter.java (fresh fetch); class loaded via convert calls at TorrentSessionImpl.java:437,451,1574.
- 34/36 SessionErrors.getErrorMsg — REACHABLE SOURCE — PASS. TorrentSessionImpl.java:1117,1124,1133; TorrentDownloadImpl.java:352,362,371,382; definition freshly printed (:59).

Totals: checked 9 (2 changed + 7 sample-only) — PASS 8, FAIL-prose 1, FAIL-label 0.
