# Spot-check — Batch 34 (Stream A Phase 2)

- Work file: `~/workspace/overnight/stream-A/work/batch34-merge-ready.md` (UNVERIFIED proposal, not a result).
- Method: re-derived from already-fetched local source only (`~/workspace/b323334-openclose-src/`, `~/workspace/b323334-openclose2-src/`, `~/workspace/b3234-src/`, `~/workspace/overnight/stream-A/corpus/java/`). No GitHub connector fetch was needed; no 429 encountered. No edit was made to the work file.
- Phase 1 label changes in this batch: rows 18, 20, 34 flipped OPEN → REACHABLE in the 2026-11-01 OPEN-closing pass (32/0/8 → 35/0/5); rows 8, 10 flipped OPEN → REACHABLE in OPEN-closing round 2 (35/0/5 → 37/0/3); Phase 1c flips: NONE. Rows checked = sample rows 1, 6, 11, 16, 21, 26, 31, 36 + Phase 1 flips 8, 10, 18, 20, 34.
- Build / sampler / C1: not run (not this task).

## Per-row verdicts

| Row | Method | Table label | Verdict | Printed evidence |
|---|---|---|---|---|
| 1 | FileTree.setType | OPEN | PASS | Def FileTree.java:159 (`public void setType(int type)`) confirmed. No printed caller (ctors set the field directly); OPEN stands. |
| 6 | TorrentContentFileTree.<init>(String,long,int,TorrentContentFileTree) | REACHABLE / SOURCE | PASS | DetailTorrentViewModel.java:237–238 `new TorrentContentFileTree(TorrentContentFileTree.PARENT_DIR, 0L, FileNode.Type.DIR, curDir.getParent())` and TorrentContentFileTreeUtils.java:125 dir-branch `new TorrentContentFileTree(name, 0L, FileNode.Type.DIR, parent)` — both exactly as cited. |
| 8 | TorrentContentFileTree.getAvailability | REACHABLE / SOURCE | PASS (round-2 flip holds; minor range nit below) | TorrentContentFileItem.java:44 `availability = tree.getAvailability();` inside the TorrentContentFileItem(TorrentContentFileTree) ctor (:38–45) — exact. That ctor is reached via DetailTorrentFilesFragment.java:160 `.map(TorrentContentFileItem::new)` in subscribeAdapter, called from onStart. Nit: onStart is declared at :146 with the subscribeAdapter() call at :150, so the row's "onStart :149-154" range straddles the method boundary rather than naming the call line; the route itself is correct. The self-recursion at TorrentContentFileTree.java:158 is correctly NOT used as the basis. |
| 10 | TorrentContentFileTree.getReceivedBytes | REACHABLE / SOURCE | PASS (round-2 flip holds) | TorrentContentFileItem.java:43 `receivedBytes = tree.getReceivedBytes();` inside the same REACHABLE ctor as row 8 — exact. |
| 11 | TorrentContentFileTree.nonIgnoreFileSize | REACHABLE / SOURCE | PASS | DetailTorrentViewModel.java:428 `fileTree.nonIgnoreFileSize()` inside checkFreeSpace() (:425) — as cited. |
| 16 | TorrentContentFileTree.toString | OPEN | PASS | Def TorrentContentFileTree.java:175 (`public String toString()`) confirmed. No printed caller; OPEN stands. |
| 18 | AdvancedPeerInfo.isUtp | REACHABLE / SOURCE | PASS (Phase 1 flip holds) | PeerInfo.java:110 `if (peer.isUtp())` inside getConnectionType() (:108) — exact; called from the PeerInfo(AdvancedPeerInfo, TorrentStatus) ctor at :65 (`connectionType = getConnectionType(peer)`); that ctor is called at TorrentDownloadImpl.java:923–925 (`new PeerInfo(peer, status)` in the getPeerInfoList loop) — all exactly as cited. |
| 20 | AdvancedPeerInfo.port | REACHABLE / SOURCE | PASS (Phase 1 flip holds) | PeerInfo.java:66 `port = peer.port();` inside the same ctor as row 18 — exact; same TorrentDownloadImpl.java:923–925 anchor. |
| 21 | IPFilterImpl.<init> | REACHABLE / SOURCE | PASS | TorrentSessionImpl.java:730 `IPFilterImpl filter = new IPFilterImpl();` inside the parseIpFilterThread block, with the parseFile call at :731 — as cited. |
| 26 | IPFilterParser.errLog | REACHABLE / SOURCE | PASS | Private errLog call sites in IPFilterParser.java confirmed at exactly :142, :149, :157, :168 (parseDAT) and :212, :220, :227, :235, :246 (parseP2P) as cited; def at :263. parseDAT/parseP2P are REACHABLE (rows 27, 30). |
| 31 | PriorityConverter.<clinit> | REACHABLE / INFERRED | PASS | Class loaded via printed convert calls at TorrentSessionImpl.java:437, :451, :1574 — all three confirmed (`PriorityConverter.convert(...)`). INFERRED (class-init convention) is correct; convention itself not decided here. |
| 34 | PriorityConverter.convert(Priority[])#2 | REACHABLE / SOURCE | PASS (Phase 1 flip holds) | TorrentDownloadImpl.java:731 `org.libtorrent4j.Priority[] p = PriorityConverter.convert(priorities);` inside prioritizeFiles(Priority[]) — exact; import at :68 is the data Priority, so this is the data-array → libtorrent-array overload, whose definition is at PriorityConverter.java:54 — exact. Called from TorrentSessionImpl.java:549 `task.prioritizeFiles(params.filePriorities)` (confirmed in the corpus copy). |
| 36 | SessionErrors.getErrorMsg | REACHABLE / SOURCE | PASS | TorrentSessionImpl.java:1117, :1124, :1133 and TorrentDownloadImpl.java:352, :362, :371, :382 `SessionErrors.getErrorMsg(...)` sites — all confirmed exactly. |

## Totals

- Rows checked: 13. **PASS: 13. FAIL: 0.**
- Proposed corrections (citation only, no label change): row 8 — change "onStart :149-154" to "onStart :146, subscribeAdapter() call :150, .map at :160".
