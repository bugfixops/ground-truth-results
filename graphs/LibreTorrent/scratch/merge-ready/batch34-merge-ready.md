# LibreTorrent batch 34 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler or full-repo grep was run or is
claimed in this file. No `search_code` 0-result was used as evidence of absence.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 34 only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, from printed source. Prior work (`~/workspace/libretorrent-batch34-proposal.md`,
  Agent 7) was used as an INPUT / lead list only; every row below was re-checked, and the
  previously 429-blocked definition files were freshly printed in this pass (see below).
  **Three labels changed versus the input proposal in this pass, all OPEN → REACHABLE, on the
  fresh prints: rows 4, 5, and 38.** No other label changed.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 34 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/b27scratch/LIBRETORRENT_BATCH_PLAN.tsv` (4,732 rows total; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
All 40 batch-34 rows are `TODO_CANDIDATE_REACHABLE` in the plan. Method names, JVM descriptors,
and order in the table below match the plan row for row (checked mechanically in this session).

## Printed source used in this pass — batch 34 definitions FRESHLY printed

Fresh connector fetches from branch `work-2026-10-31`, one file at a time with ~20 s pauses,
saved in `~/workspace/b3234-src/` (all under
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/`).
No fresh HTTP 429 was hit in this session. Fresh SHAs (git blob SHA):
- `org/proninyaroslav/libretorrent/core/model/session/AdvancedPeerInfo.java` — fresh, SHA
  `ff370dae46c7af3727518084f655f7430099be66`, byte-identical to `~/workspace/b34-src/AdvancedPeerInfo.java`.
  Confirms: ctor `AdvancedPeerInfo(peer_info p)` :36-43 (port :40, pieces :41, isUtp :42),
  `port()` :45-47, `pieces()` :56-58, `isUtp()` :61-63.
- `org/proninyaroslav/libretorrent/core/model/session/IPFilterParser.java` — fresh, SHA
  `ead6fb8b8916769f496bc0458c4d4398c703f0e7`, byte-identical to
  `~/workspace/libretorrent-merge/b3-src/core/model/session/IPFilterParser.java` and to
  `~/workspace/batch20_21/src/IPFilterParser.java`. Confirms: static TAG :43 (`<clinit>`),
  ctor :49, `parseFile` :59, `parseDAT` :96, `parseP2P` :180, private `parseIpAddress` (after :246),
  private `errLog` :263 (called from parseDAT/parseP2P at :142,:149,:157,:168,:212,:220,:227,:235,:246).
- `org/proninyaroslav/libretorrent/core/utils/TorrentContentFileTreeUtils.java` — fresh, SHA
  `71185dbebfafddbe1458d41275cc9736b3437b35`, byte-identical to
  `~/workspace/b4-src/TorrentContentFileTreeUtils.java`. **Decisive for rows 4–5:**
  `buildFileTree` :46, root `new TorrentContentFileTree(FileTree.ROOT, 0L, FileNode.Type.DIR)` :48
  (the 3-arg ctor, row 5), and `makeObject` :119-125 — file branch
  `new TorrentContentFileTree(index, name, size, FileNode.Type.FILE, parent)` :124 (the 5-arg ctor,
  row 4) and dir branch `new TorrentContentFileTree(name, 0L, FileNode.Type.DIR, parent)` :125
  (the 4-arg ctor, row 6, already SOURCE). `buildFileTree` is called from
  DetailTorrentViewModel.java:551 (local reprint, see below), so both constructions run on the
  detail route — the input proposal's "makeObject NOT printed" gap is closed.
- `org/proninyaroslav/libretorrent/core/model/session/PriorityConverter.java` — fresh, SHA
  `916d29cd69689f25753c3488c6624e743b0882a1`, byte-identical to
  `~/workspace/libretorrent-merge/b3-src/core/model/session/PriorityConverter.java`.
  Confirms all four converts and disambiguates the #2 rows: `convert(Priority[])` data→lib :54,
  `convert(org.libtorrent4j.Priority[])` lib→data :74, `convert(Priority)` data→lib single :94,
  `convert(org.libtorrent4j.Priority)` lib→data single :103. Static SparseArray initialisers
  (`<clinit>`) are the two static blocks preceding them.
- `org/proninyaroslav/libretorrent/core/model/session/SessionErrors.java` — fresh, SHA
  `238207db877f1ab179a12187308b18c1597fc528`, byte-identical to
  `~/workspace/libretorrent-merge/b3-src/core/model/session/SessionErrors.java`.
  **Decisive for row 38:** private static class `Error` :28, `Error(int, String)` ctor :33,
  static `errors` array :40-42 constructing `new Error(11, "Try again")` and
  `new Error(22, "Invalid argument")`; `isNonCritical` :45, `getErrorMsg` :59.
  The ctor is therefore called by the class's own static initialiser whenever the class is
  loaded via the REACHABLE getErrorMsg/isNonCritical callers — INFERRED, not SOURCE (no direct
  app call site names the Error ctor; the array literal is the call site).
- Also fresh in this session, for batches 32–33 anchors (same fetch run, same pauses):
  `core/utils/BencodeFileTreeUtils.java` SHA `5de27e64238342db07a51ba8c1039cf26e5d3089`,
  `core/model/filetree/FileTree.java` SHA `b868825de8cddea523b5483c7e724981533b06d3`,
  both byte-identical to the Agent 7 local copies.

Local reprints re-read/grepped in this session (NOT freshly connector-fetched in this session;
the merger must fresh-print the caller files named below before merging rows that rest on them):
- `~/workspace/agent7/src/` — FileTree.java (223 lines), TorrentContentFileTree.java (185 lines),
  IPFilterImpl.java (69 lines: ctor :33, addRange :39, getFilter :64).
- Caller sites carried from the input proposal: TorrentSessionImpl.java — parseIpFilterThread block
  (`new IPFilterImpl()`, `new IPFilterParser().parseFile(path, fs, filter)` :731,
  `filter.getFilter()` passed to `swig().set_ip_filter`), :170 `this.sessionLogger = new SessionLogger()`,
  :437/:451 `PriorityConverter.convert(...)` on filePriorities arrays, :1574
  `PriorityConverter.convert(priority).swig()` (single Priority), :1117-1134
  `SessionErrors.getErrorMsg(error)` / `isNonCritical(error)` in alert handling;
  TorrentDownloadImpl.java (b3 local copy, grepped in this session) — :935 `advancedPeerInfo()`,
  :944 `l.add(new AdvancedPeerInfo(v.get(i)))`, :1516 `getPiecesAvailability()`, :1528 `peer.pieces()`,
  :352/:362/:371/:382 `SessionErrors.getErrorMsg` / `isNonCritical`;
  DetailTorrentViewModel.java (b27scratch copy) — :237-238 `new TorrentContentFileTree(PARENT_DIR, 0L,
  DIR, curDir.getParent())` (4-arg), :299/:420 `file.getFilePriority()`, :551 `buildFileTree`,
  :559 `file.setPriority(priorities.get(i), false)`, updateFiles (`file.setReceivedBytes(...)`,
  `file.setAvailability(...)`), checkFreeSpace (`fileTree.nonIgnoreFileSize()`).

## Per-row table — 40 rows, plan order

| # | Method | Proposed label | confirmed_by | Printed citation / note |
|---|---|---|---|---|
| 1 | FileTree.setType | OPEN | — | FileTree.java:159 — fresh fetch (batch 33); no printed caller (ctors set the field directly). |
| 2 | FileTree.size | REACHABLE proposed | SOURCE | Called by BencodeFileTree.selectedFileSize:117 (this.size()) and TorrentContentFileTree.nonIgnoreFileSize:130 (this.size()); both callers REACHABLE (batch 33 row 7; this batch row 11). |
| 3 | FileTree.toString | OPEN | — | FileTree.java:211 — fresh fetch; called only by BencodeFileTree.toString:125, which is itself OPEN (batch 33 row 8). |
| 4 | TorrentContentFileTree.<init>(int,String,long,int,TorrentContentFileTree) | REACHABLE proposed | SOURCE | **CHANGED in this pass (was OPEN).** TorrentContentFileTreeUtils.java makeObject:124 `new TorrentContentFileTree(index, name, size, FileNode.Type.FILE, parent)` — fresh fetch; makeObject is called from buildFileTree, called from DetailTorrentViewModel.java:551 (local reprint). |
| 5 | TorrentContentFileTree.<init>(String,long,int) | REACHABLE proposed | SOURCE | **CHANGED in this pass (was OPEN).** TorrentContentFileTreeUtils.java buildFileTree:48 root `new TorrentContentFileTree(FileTree.ROOT, 0L, FileNode.Type.DIR)` — fresh fetch; FileNode.Type constants are int constants (FileTree.getType ()I, FileTree.java:153-155 fresh fetch), so this is the (String,long,int) ctor, not a different overload. The input proposal missed this root construction (it noted only the Detail VM 4-arg use). |
| 6 | TorrentContentFileTree.<init>(String,long,int,TorrentContentFileTree) | REACHABLE proposed | SOURCE | DetailTorrentViewModel.java:237-238 (PARENT_DIR node) (local reprint); also TorrentContentFileTreeUtils.java makeObject:125 dir branch — fresh fetch. |
| 7 | TorrentContentFileTree.changePriority | REACHABLE proposed | SOURCE | Private, called by setPriority TorrentContentFileTree.java:78 (setPriority REACHABLE, row 14). |
| 8 | TorrentContentFileTree.getAvailability | OPEN | — | TorrentContentFileTree.java:150; no printed external caller. Its only printed use is self-recursion (node.getAvailability() :158 inside getAvailability itself) — recursion alone is not an entry route. Detail VM sets availability, does not get it in printed lines. |
| 9 | TorrentContentFileTree.getFilePriority | REACHABLE proposed | SOURCE | DetailTorrentViewModel.java:299, 420 (local reprint). |
| 10 | TorrentContentFileTree.getReceivedBytes | OPEN | — | TorrentContentFileTree.java:56; only printed use is self-recursion (node.getReceivedBytes() :61 inside getReceivedBytes itself) — recursion alone is not an entry route. No printed external caller. |
| 11 | TorrentContentFileTree.nonIgnoreFileSize | REACHABLE proposed | SOURCE | DetailTorrentViewModel.java checkFreeSpace: fileTree.nonIgnoreFileSize() (local reprint). |
| 12 | TorrentContentFileTree.onChangePriority | REACHABLE proposed | SOURCE | Private, called by changePriority TorrentContentFileTree.java:83 (REACHABLE, row 7). |
| 13 | TorrentContentFileTree.setAvailability | REACHABLE proposed | SOURCE | DetailTorrentViewModel.java updateFiles: file.setAvailability(availability[i]) (local reprint). |
| 14 | TorrentContentFileTree.setPriority | REACHABLE proposed | SOURCE | DetailTorrentViewModel.java:559 file.setPriority(priorities.get(i), false) (local reprint). |
| 15 | TorrentContentFileTree.setReceivedBytes | REACHABLE proposed | SOURCE | DetailTorrentViewModel.java updateFiles: file.setReceivedBytes(receivedBytes[i]) (local reprint). |
| 16 | TorrentContentFileTree.toString | OPEN | — | TorrentContentFileTree.java:175; no printed caller. |
| 17 | AdvancedPeerInfo.<init> | REACHABLE proposed | SOURCE | TorrentDownloadImpl.java:944 `new AdvancedPeerInfo(v.get(i))` in advancedPeerInfo():935 (local copy grepped in this session, not fresh — merger must fresh-print TorrentDownloadImpl). Definition freshly printed in this session (:36-43). |
| 18 | AdvancedPeerInfo.isUtp | OPEN | — | Definition freshly printed (:61-63). No printed caller in printed files (PeerInfo.java was not printed here; do not assume its getConnectionType calls isUtp). Target: print PeerInfo.java + a saved full-repo grep for isUtp. |
| 19 | AdvancedPeerInfo.pieces | REACHABLE proposed | SOURCE | TorrentDownloadImpl.java:1528 `peer.pieces()` in getPiecesAvailability():1516 (local copy grepped in this session, not fresh — merger must fresh-print TorrentDownloadImpl). Definition freshly printed (:56-58). |
| 20 | AdvancedPeerInfo.port | OPEN | — | Definition freshly printed (:45-47). No printed caller in printed files. Target: print PeerInfo.java + a saved full-repo grep for port(). |
| 21 | IPFilterImpl.<init> | REACHABLE proposed | SOURCE | TorrentSessionImpl.java parseIpFilterThread block (`new IPFilterImpl()`, parseFile call :731) (local reprint). |
| 22 | IPFilterImpl.addRange | REACHABLE proposed | SOURCE | IPFilterParser.java parseDAT/parseP2P: filter.addRange(startAddr, endAddr) — fresh fetch. |
| 23 | IPFilterImpl.getFilter | REACHABLE proposed | SOURCE | TorrentSessionImpl.java parseIpFilterThread block: swig().set_ip_filter(filter.getFilter()) (local reprint). |
| 24 | IPFilterParser.<clinit> | REACHABLE proposed | INFERRED | Static TAG IPFilterParser.java:43 — fresh fetch; class loaded at TorrentSessionImpl.java:731 new IPFilterParser() (local reprint). |
| 25 | IPFilterParser.<init>() | REACHABLE proposed | SOURCE | TorrentSessionImpl.java:731 `new IPFilterParser().parseFile(path, fs, filter)` (local reprint). |
| 26 | IPFilterParser.errLog | REACHABLE proposed | SOURCE | Private, called from parseDAT/parseP2P IPFilterParser.java:142,149,157,168,212,220,227,235,246 — fresh fetch (parseDAT/parseP2P REACHABLE, rows 27, 30). |
| 27 | IPFilterParser.parseDAT | REACHABLE proposed | SOURCE | Called by parseFile IPFilterParser.java:77 — fresh fetch (parseFile REACHABLE, row 28). |
| 28 | IPFilterParser.parseFile | REACHABLE proposed | SOURCE | TorrentSessionImpl.java:731 (local reprint). |
| 29 | IPFilterParser.parseIpAddress | REACHABLE proposed | SOURCE | Private, called from parseDAT/parseP2P IPFilterParser.java — fresh fetch (parseDAT/parseP2P REACHABLE). |
| 30 | IPFilterParser.parseP2P | REACHABLE proposed | SOURCE | Called by parseFile IPFilterParser.java:79 — fresh fetch. |
| 31 | PriorityConverter.<clinit> | REACHABLE proposed | INFERRED | Static SparseArray initialisers, PriorityConverter.java — fresh fetch; class loaded via convert calls at TorrentSessionImpl.java:437,451,1574 (local reprint). |
| 32 | PriorityConverter.convert(Priority)#2 | REACHABLE proposed | SOURCE | Descriptor (data Priority;) → libtorrent Priority = convert(Priority) :94 — fresh fetch. TorrentSessionImpl.java:1574 `PriorityConverter.convert(priority).swig()` (local reprint). Distinguished from batch 3 convert(Priority) (libtorrent → data) by descriptor direction; the #2 suffix is plan numbering for the second single-Priority overload, confirmed by the fresh definition (two single-arg converts, :94 and :103). |
| 33 | PriorityConverter.convert(Priority[]) | REACHABLE proposed | SOURCE | Descriptor ([libtorrent Priority;) → [data Priority] = convert(org.libtorrent4j.Priority[]) :74 — fresh fetch. TorrentSessionImpl.java:437,451 convert(resParams/p.filePriorities()) (local reprint). |
| 34 | PriorityConverter.convert(Priority[])#2 | OPEN | — | Descriptor ([data Priority;) → [libtorrent Priority] = convert(Priority[]) :54 — fresh fetch. No printed caller in printed files (no printed data-array → libtorrent-array conversion site). Target: saved full-repo grep for this overload's callers. |
| 35 | SessionErrors.<clinit> | REACHABLE proposed | INFERRED | Static errors array SessionErrors.java:40-42 — fresh fetch; class loaded via getErrorMsg/isNonCritical calls at TorrentSessionImpl.java:1117-1134, TorrentDownloadImpl.java:352-382 (local reprints). |
| 36 | SessionErrors.getErrorMsg | REACHABLE proposed | SOURCE | TorrentSessionImpl.java:1117,1124,1133; TorrentDownloadImpl.java:352,362,371,382 (local reprints). Definition freshly printed (:59). |
| 37 | SessionErrors.isNonCritical | REACHABLE proposed | SOURCE | TorrentSessionImpl.java:1118,1126,1134; TorrentDownloadImpl.java:355,372 (local reprints). Definition freshly printed (:45). |
| 38 | SessionErrors$Error.<init> | REACHABLE proposed | INFERRED | **CHANGED in this pass (was OPEN).** Called by the static errors array initialiser SessionErrors.java:40-42 (`new Error(11, "Try again")`, `new Error(22, "Invalid argument")`) — fresh fetch; the initialiser runs when the class is loaded via the REACHABLE getErrorMsg/isNonCritical callers (rows 36, 37). INFERRED, not SOURCE: no direct app call site names the Error ctor, the array literal is the call site. Convention flagged below (static-initialiser dispatch). |
| 39 | SessionLogger.<clinit> | REACHABLE proposed | INFERRED | Static nextLogEntryId SessionLogger.java:39 (local reprint); class loaded at TorrentSessionImpl.java:170 new SessionLogger() (local reprint). |
| 40 | SessionLogger.<init> | REACHABLE proposed | SOURCE | TorrentSessionImpl.java:170 `this.sessionLogger = new SessionLogger()` (local reprint). |

## Counts — mechanically verified

- REACHABLE proposed: 32 (rows 2, 4, 5, 6, 7, 9, 11, 12, 13, 14, 15, 17, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39, 40)
- UNREACHABLE proposed: 0
- OPEN: 8 (rows 1, 3, 8, 10, 16, 18, 20, 34)
- Total: 40 rows, sequence 1–40 intact in plan order.
- Verified for merge: 0 / 40.
- Change versus input proposal: 29/0/11 → 32/0/8 (rows 4, 5, 38 flipped OPEN → REACHABLE on fresh prints).

## Gaps the merger must close before merging

1. Saved full-repo grep for the 8 OPEN rows (rows 1, 3, 8, 10, 16, 18, 20, 34). Any hit flips that
   row to REACHABLE. In particular: PeerInfo.java print + grep for AdvancedPeerInfo.isUtp/port
   (rows 18, 20); grep for the data-array → libtorrent-array convert overload (row 34).
2. Fresh connector prints of the caller files flagged as local reprints above
   (TorrentSessionImpl.java, TorrentDownloadImpl.java, DetailTorrentViewModel.java) before merging
   rows that rest on them. The batch-34 definition files themselves are freshly printed in this
   session and need no re-print, except that SessionLogger.java was not freshly fetched here
   (rows 39–40 rest on a local reprint + a local-reprint caller).
3. Printed launcher-to-service step; build/sampler/C1 on a full checkout; main-agent
   spot-check 1 in 5; py_compile at merge. None run or claimed here.
4. No fresh HTTP 429 was hit in this session.

## Undecided conventions — flagged per row, NOT decided here

- Strict-entry: applies to ALL 32 REACHABLE proposals. No route in this file is printed all the
  way from a launcher activity; anchors are TorrentService/TorrentSessionImpl/DetailTorrentViewModel.
  Under a strict launcher-entry rule those rows would fall back to OPEN. This session did not
  decide the rule either way.
- Static-initialiser dispatch: rows 24, 31, 35, 39 (`<clinit>`) are INFERRED, not SOURCE, because
  JVM class-initialisation timing is not printed source; row 38 (Error ctor, called only by a
  static initialiser) is INFERRED on the same ground. Whether `<clinit>` / static-initialiser-only
  methods count as REACHABLE on first-use evidence alone is undecided project-wide; flagged,
  not decided here. If the merger requires a printed first-use site naming the class, rows 24,
  31, 35, 39 stay INFERRED (their first-use callers are printed) but row 38's label rests entirely
  on the initialiser convention and would revert to OPEN under a stricter rule.
- Internal-caller / self-recursion rule: a private method called by a printed REACHABLE method in
  the same file is REACHABLE (rows 7, 12, 26, 29); a public method whose only printed caller is
  itself (self-recursion) is OPEN, not REACHABLE (rows 8, 10) — recursion alone is not an entry route.
- confirmed_by vocabulary: SOURCE or INFERRED only in the table, never DYN, FW-MEMORY, or UNVERIFIED.
  For OPEN rows confirmed_by is shown as — (none).
