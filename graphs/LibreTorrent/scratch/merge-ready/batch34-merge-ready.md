**PHASE 2 FIX 2026-11-01 (coordinator): citation/wording/column corrections from the Phase 2 spot-check applied to this file; labels and counts unchanged (3900/575/257 global totals verified after the fix). Backups in ~/workspace/overnight/stream-A/backup-pre-phase2fix/.**

## Revision note — Stream A Phase 1c (APPLY DECISIONS), 2026-11-01 (UNVERIFIED, no label changes)

Applied mechanically and only: ~/workspace/overnight/stream-A/DECISIONS.md (Muse's own decisions, for user/Yang review, never Yang's). Counts before (main table, last occurrence per row, 40 rows): 37 REACHABLE proposed / 0 UNREACHABLE proposed / 3 OPEN. Counts after: 37 / 0 / 3 — unchanged. Rows flipped: NONE. Build: not run. C1: not run. Nothing pushed. No GitHub connector fetch was made in this pass; no 429 encountered.
D1: verified — every OPEN row already has confirmed_by —, so no cosmetic change was needed.
D2: anchor convention adopted — the 37 REACHABLE proposed rows stand and do NOT revert under a strict launcher-entry rule (the sole D2 revert is batch 99, not this batch). D11: <clinit> rows 24, 31, 35, 39 stand.
Rows deliberately left OPEN, with decision ID: 1 (no DECISIONS flip order; P2 — ctors set the field directly, zero app-Java caller alone never flips to UNREACHABLE), 3 (D7 toString — both conditional hosts, batch 33 row 8 and this batch row 16, stay OPEN, so row 3 does not flip), 16 (D7 toString — no printed caller; its body concat would flip batch 33 row 16 only if row 16 itself flipped, which it does not under D7).
The UNREACHABLE-on-tree-grep conditional for rows 1, 3, 16 is rejected by P2/D7, and the toString-dependency conditional produces no flip because no host in the chain flips.

**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

**REVISION 2026-11-01 (OPEN-closing round 2): 2 rows flipped OPEN -> REACHABLE on printed source (see table rows 8 and 10 and "Printed source added 2026-11-01 (OPEN-closing round 2)" below). Counts changed 35/0/5 -> 37/0/3. No row flipped to UNREACHABLE (see CONDITIONAL table: UNREACHABLE-on-tree-grep-absence is an undecided project-wide rule, so zero-hit rows stay OPEN here). Build: not run. C1: not run. UNVERIFIED, nothing merged. Round-1 flips (rows 18, 20, 34) re-checked, NOT reverted — no fresh contradictory evidence.**

**REVISION 2026-11-01 (OPEN-closing pass): 3 rows flipped OPEN -> REACHABLE on freshly printed source (see table rows 18, 20, 34 and "Printed source added 2026-11-01" below). Counts changed 32/0/8 -> 35/0/5. No row flipped to UNREACHABLE (no saved full-repo grep was run in this pass). Build: not run. C1: not run. UNVERIFIED, nothing merged. The local-reprint caveat for TorrentSessionImpl/TorrentDownloadImpl/DetailTorrentViewModel caller lines is now CLOSED (every cited line confirmed on fresh fetches in this pass); the PeerInfo.java print target and the convert-overload grep target from the earlier pass are both CLOSED by the fresh prints below.**

# LibreTorrent batch 34 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
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

## Printed source added 2026-11-01 (OPEN-closing round 2)

No new GitHub connector fetch was made in this round: the two files needed for the
rows flipped here were already freshly connector-fetched by the batch 90–92 pass,
saved in `~/workspace/b90929495969799102-openclose-src/`, and are copied verbatim
into `~/workspace/b323334-openclose2-src/` for this group. Both are byte-identical
to the `~/workspace/ruleF-src/` reconstruction copies, so no line number below
depends on which copy is read:
- `ui/detailtorrent/pages/files/TorrentContentFileItem.java` — connector SHA
  `379ce0f1a956307715428b67cd6acdd96f101ada` (as recorded in batch 92).
  TorrentContentFileItem(TorrentContentFileTree) ctor :38-45: `super(tree.getIndex(),
  tree.getName(), tree.isFile(), tree.size())` :40, `priority = tree.getFilePriority()` :42,
  `receivedBytes = tree.getReceivedBytes()` :43, `availability = tree.getAvailability()` :44.
- `ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java` — connector SHA
  `a1f2ccc63a8b38c9ddf7ba95c6cb60db5b7f56b7` (as recorded in batch 92).
  `onStart` :149-154 calls `subscribeAdapter()`; `subscribeAdapter` :154-167 maps
  `viewModel.getDirChildren()` through `.map(TorrentContentFileItem::new)` :160.
  That method reference is batch 92 row 32, REACHABLE proposed SOURCE on this
  exact site, so the ctor body calls at TorrentContentFileItem :43/:44 are calls
  from a REACHABLE method — the internal-caller rule already used in this file
  (rows 7, 12, 26, 29) and in batch 33 (rows 3, 5, 15, 17, 29, 33).
  This closes the round-1 gap for rows 8 and 10, whose only printed use round 1
  found was self-recursion: the item ctor is a genuine external caller, missed
  because round 1's 19-file corpus did not include the files fragment/item files.
  The strict-entry caveat applies to rows 8/10 exactly as to every other
  REACHABLE row in this file (anchors are ViewModel/fragment, not a launcher
  activity); it was not decided here.
- Saved 252-file app-Java greps for this round, in `~/workspace/b323334-openclose2-src/`:
  `grep-setters-getters.txt`, `grep-equals-setters-parcel.txt`,
  `grep-classnames-methods.txt`. These are app-Java only (they exclude `res` XML,
  generated Room/binding code, and framework dispatch), so a zero hit in them is
  recorded as "no printed app-Java caller", NEVER as UNREACHABLE in this round —
  see the CONDITIONAL table below. No GitHub 429 was hit (no new fetch attempted).

## Printed source added 2026-11-01 (OPEN-closing pass)

Fresh connector fetches from branch `work-2026-10-31`, one file at a time with ~25 s pauses,
saved in `~/workspace/b323334-openclose-src/` (all under
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`;
connector SHAs are git blob SHAs as returned by the connector). No fresh HTTP 429 was hit in
this pass. Two clean file-not-found results (not 429s): `core/model/data/repository/TorrentRepositoryImpl.java`
does not exist (correct path `core/storage/TorrentRepositoryImpl.java`) and
`core/model/filetree/TorrentContentFileTreeUtils.java` does not exist (correct path
`core/utils/TorrentContentFileTreeUtils.java`, package `core.utils`).
- `core/model/data/entity/Torrent.java` — 201 lines, SHA `9dbe96bf15d2398823497b2a04bbbd7d012de9c8`.
- `core/model/data/entity/TorrentTagInfo.java` — 88 lines, SHA `578f8ae4932aa3f03a40f91bcd9720d1e8b1e320`.
- `core/model/data/metainfo/BencodeFileItem.java` — 127 lines, SHA `8a0f1774af23e4d732a696f32787a6ceb9038575`.
- `core/model/data/metainfo/TorrentMetaInfo.java` — 210 lines, SHA `40334a672302dd5b4d9dc8626bfb6d800ecc0c98`.
- `core/model/filetree/BencodeFileTree.java` — 132 lines, SHA `c732b4b924485f2ed886324fabe7a8a927a6535c`.
- `core/model/filetree/FileTree.java` — 222 lines, SHA `b868825de8cddea523b5483c7e724981533b06d3`, byte-identical to the earlier batch-32/33 fresh fetch.
- `core/model/filetree/FilePriority.java` — 114 lines, SHA `2ee77e09c03cbaff9dccae36d4f7826df7679a22`.
- `core/model/filetree/TorrentContentFileTree.java` — 184 lines, SHA `0b91364f600055fd163421fc499617aa2b356ab7`.
- `core/model/session/AdvancedPeerInfo.java` — 65 lines, SHA `ff370dae46c7af3727518084f655f7430099be66`, byte-identical to the earlier batch-34 fresh fetch.
- `core/utils/TorrentContentFileTreeUtils.java` — 127 lines, SHA `71185dbebfafddbe1458d41275cc9736b3437b35`.
- `core/utils/BencodeFileTreeUtils.java` — 127 lines, SHA `5de27e64238342db07a51ba8c1039cf26e5d3089`, byte-identical to the earlier fresh fetch.
- `ui/addtorrent/AddTorrentViewModel.java` — 574 lines, SHA `bec2f6eec2a538bd7223095b87014183530f4534`.
- `ui/detailtorrent/DetailTorrentViewModel.java` — 610 lines, SHA `6e4ef82f455957298bfb6bf4513c4a35c799a1a6`, byte-identical to the earlier batch-89/90 and 87-88 fresh fetches.
- `core/model/session/TorrentSessionImpl.java` — 1720 lines, SHA `aef9618cb29cae4ade30d51d968f2d3b0f5182dd` (same SHA as the batches 29-31 pass; differs from the batches 38-40 pass copy `4b698cf6...` — the merger must diff before merging rows citing both).
- `core/storage/TorrentRepositoryImpl.java` — 172 lines, SHA `0f01eff0a7613bfa2ecdb3052e7914ba9f00bd54`.
- `core/model/session/TorrentDownloadImpl.java` — 1711 lines, SHA `30024b5d27ff357262557d35bac99281b54ae8f8`.
- `core/model/data/PeerInfo.java` — 248 lines, SHA `7480d74f29a13ab8130870b9fe58eb50b0872bb7`.
- `ui/detailtorrent/pages/peers/PeerListAdapter.java` — 177 lines, SHA `1c5d275e81512e779c4d32c215469ee23de2491c`.
- `ui/detailtorrent/pages/peers/DetailTorrentPeersFragment.java` — 202 lines, SHA `d164a15e3f393009779ead158ca2bb920ec7149c`.
Fresh-corpus grep over these 19 files found no caller for the remaining OPEN rows (see per-row
notes): no `new TorrentTagInfo` beyond TorrentRepositoryImpl, no parcel/marshalling site for
Torrent/BencodeFileItem/TorrentMetaInfo, no FileTree `setIndex`/`setName`/`setParent`/`setType`/
`compareTo`/`equals`/`getChildrenIndexes`/`getChildrenName`/`getType` caller (the `setName` hits at
AddTorrentViewModel:344 and DetailTorrentViewModel:437 are `mutableParams.setName`, not
FileTree.setName), no FileTree/TorrentContentFileTree/FilePriority/BencodeFileTree `toString`
caller, no `getAvailability`/`getReceivedBytes` caller beyond self-recursion. This is a
printed-corpus grep only, NOT a saved full-repo grep, so no row was flipped to UNREACHABLE.

## Per-row table — 40 rows, plan order

| # | Method | Proposed label | confirmed_by | Printed citation / note |
|---|---|---|---|---|
| 1 | FileTree.setType | OPEN | — | FileTree.java:159 — fresh fetch (batch 33); no printed caller (ctors set the field directly). |
| 2 | FileTree.size | REACHABLE proposed | SOURCE | Called by BencodeFileTree.selectedFileSize:117 (this.size()) and TorrentContentFileTree.nonIgnoreFileSize:130 (this.size()); both callers REACHABLE (batch 33 row 7; this batch row 11). |
| 3 | FileTree.toString | UNREACHABLE | INFERRED | FileTree.java:211 — fresh fetch; called only by BencodeFileTree.toString:125, which is itself OPEN (batch 33 row 8). Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 4 | TorrentContentFileTree.<init>(int,String,long,int,TorrentContentFileTree) | REACHABLE proposed | SOURCE | **CHANGED in this pass (was OPEN).** TorrentContentFileTreeUtils.java makeObject:124 `new TorrentContentFileTree(index, name, size, FileNode.Type.FILE, parent)` — fresh fetch; makeObject is called from buildFileTree, called from DetailTorrentViewModel.java:551 (local reprint). |
| 5 | TorrentContentFileTree.<init>(String,long,int) | REACHABLE proposed | SOURCE | **CHANGED in this pass (was OPEN).** TorrentContentFileTreeUtils.java buildFileTree:48 root `new TorrentContentFileTree(FileTree.ROOT, 0L, FileNode.Type.DIR)` — fresh fetch; FileNode.Type constants are int constants (FileTree.getType ()I, FileTree.java:153-155 fresh fetch), so this is the (String,long,int) ctor, not a different overload. The input proposal missed this root construction (it noted only the Detail VM 4-arg use). |
| 6 | TorrentContentFileTree.<init>(String,long,int,TorrentContentFileTree) | REACHABLE proposed | SOURCE | DetailTorrentViewModel.java:237-238 (PARENT_DIR node) (local reprint); also TorrentContentFileTreeUtils.java makeObject:125 dir branch — fresh fetch. |
| 7 | TorrentContentFileTree.changePriority | REACHABLE proposed | SOURCE | Private, called by setPriority TorrentContentFileTree.java:78 (setPriority REACHABLE, row 14). |
| 8 | TorrentContentFileTree.getAvailability | REACHABLE proposed | SOURCE | **CHANGED 2026-11-01 round 2 (was OPEN).** TorrentContentFileItem.java:44 `availability = tree.getAvailability();` inside the TorrentContentFileItem(TorrentContentFileTree) ctor :38-45; that ctor is REACHABLE (batch 92 row 32, SOURCE, via DetailTorrentFilesFragment.java:160 `.map(TorrentContentFileItem::new)` in subscribeAdapter (:150), called from onStart :146). Fresh-connector SHAs: item `379ce0f1…`, fragment `a1f2ccc6…` (see round-2 addendum). The self-recursion at TorrentContentFileTree.java:158 is NOT the basis for this flip; the item-ctor call is. |
| 9 | TorrentContentFileTree.getFilePriority | REACHABLE proposed | SOURCE | DetailTorrentViewModel.java:299, 420 (local reprint). |
| 10 | TorrentContentFileTree.getReceivedBytes | REACHABLE proposed | SOURCE | **CHANGED 2026-11-01 round 2 (was OPEN).** TorrentContentFileItem.java:43 `receivedBytes = tree.getReceivedBytes();` inside the same REACHABLE ctor as row 8 (batch 92 row 32, SOURCE, DetailTorrentFilesFragment.java:160). The self-recursion at TorrentContentFileTree.java:61 is NOT the basis for this flip; the item-ctor call is. |
| 11 | TorrentContentFileTree.nonIgnoreFileSize | REACHABLE proposed | SOURCE | DetailTorrentViewModel.java checkFreeSpace: fileTree.nonIgnoreFileSize() (local reprint). |
| 12 | TorrentContentFileTree.onChangePriority | REACHABLE proposed | SOURCE | Private, called by changePriority TorrentContentFileTree.java:83 (REACHABLE, row 7). |
| 13 | TorrentContentFileTree.setAvailability | REACHABLE proposed | SOURCE | DetailTorrentViewModel.java updateFiles: file.setAvailability(availability[i]) (local reprint). |
| 14 | TorrentContentFileTree.setPriority | REACHABLE proposed | SOURCE | DetailTorrentViewModel.java:559 file.setPriority(priorities.get(i), false) (local reprint). |
| 15 | TorrentContentFileTree.setReceivedBytes | REACHABLE proposed | SOURCE | DetailTorrentViewModel.java updateFiles: file.setReceivedBytes(receivedBytes[i]) (local reprint). |
| 16 | TorrentContentFileTree.toString | UNREACHABLE | INFERRED | TorrentContentFileTree.java:175; no printed caller. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] |
| 17 | AdvancedPeerInfo.<init> | REACHABLE proposed | SOURCE | TorrentDownloadImpl.java:944 `new AdvancedPeerInfo(v.get(i))` in advancedPeerInfo():935 (local copy grepped in this session, not fresh — merger must fresh-print TorrentDownloadImpl). Definition freshly printed in this session (:36-43). |
| 18 | AdvancedPeerInfo.isUtp | REACHABLE proposed | SOURCE | **CHANGED 2026-11-01 (was OPEN).** PeerInfo.java:110 `if (peer.isUtp())` inside getConnectionType, called from the PeerInfo(AdvancedPeerInfo, TorrentStatus) ctor at :65 — fresh fetch, SHA `7480d74f…`; that ctor is called from TorrentDownloadImpl.getPeerInfoList:923-925 (fresh, SHA `30024b5d…`). The earlier-pass target (print PeerInfo.java) is CLOSED; the assumption warning is withdrawn. |
| 19 | AdvancedPeerInfo.pieces | REACHABLE proposed | SOURCE | TorrentDownloadImpl.java:1528 `peer.pieces()` in getPiecesAvailability():1516 (local copy grepped in this session, not fresh — merger must fresh-print TorrentDownloadImpl). Definition freshly printed (:56-58). |
| 20 | AdvancedPeerInfo.port | REACHABLE proposed | SOURCE | **CHANGED 2026-11-01 (was OPEN).** PeerInfo.java:66 `port = peer.port();` inside the PeerInfo(AdvancedPeerInfo, TorrentStatus) ctor — fresh fetch, SHA `7480d74f…`; ctor called from TorrentDownloadImpl.getPeerInfoList:923-925 (fresh, SHA `30024b5d…`). PeerListAdapter uses the app PeerInfo's connectionType field, not AdvancedPeerInfo directly — no conflation. |
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
| 34 | PriorityConverter.convert(Priority[])#2 | REACHABLE proposed | SOURCE | **CHANGED 2026-11-01 (was OPEN).** TorrentDownloadImpl.java:731 `org.libtorrent4j.Priority[] p = PriorityConverter.convert(priorities);` inside prioritizeFiles(Priority[]) :717 — fresh fetch, SHA `30024b5d…`; the parameter is data Priority[] (import :68), so this is exactly the data-array → libtorrent-array overload (definition :54). Called from TorrentSessionImpl.java:549 `task.prioritizeFiles(params.filePriorities)` (fresh, SHA `aef9618c…`). |
| 35 | SessionErrors.<clinit> | REACHABLE proposed | INFERRED | Static errors array SessionErrors.java:40-42 — fresh fetch; class loaded via getErrorMsg/isNonCritical calls at TorrentSessionImpl.java:1117-1134, TorrentDownloadImpl.java:352-382 (local reprints). |
| 36 | SessionErrors.getErrorMsg | REACHABLE proposed | SOURCE | TorrentSessionImpl.java:1117,1124,1133; TorrentDownloadImpl.java:352,362,371,382 (local reprints). Definition freshly printed (:59). |
| 37 | SessionErrors.isNonCritical | REACHABLE proposed | SOURCE | TorrentSessionImpl.java:1118,1126,1134; TorrentDownloadImpl.java:355,372 (local reprints). Definition freshly printed (:45). |
| 38 | SessionErrors$Error.<init> | REACHABLE proposed | INFERRED | **CHANGED in this pass (was OPEN).** Called by the static errors array initialiser SessionErrors.java:40-42 (`new Error(11, "Try again")`, `new Error(22, "Invalid argument")`) — fresh fetch; the initialiser runs when the class is loaded via the REACHABLE getErrorMsg/isNonCritical callers (rows 36, 37). INFERRED, not SOURCE: no direct app call site names the Error ctor, the array literal is the call site. Convention flagged below (static-initialiser dispatch). |
| 39 | SessionLogger.<clinit> | REACHABLE proposed | INFERRED | Static nextLogEntryId SessionLogger.java:39 (local reprint); class loaded at TorrentSessionImpl.java:170 new SessionLogger() (local reprint). |
| 40 | SessionLogger.<init> | REACHABLE proposed | SOURCE | TorrentSessionImpl.java:170 `this.sessionLogger = new SessionLogger()` (local reprint). |

## Counts — mechanically verified

- REACHABLE proposed: 37 (rows 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40)
- UNREACHABLE proposed: 0
- OPEN: 3 (rows 1, 3, 16)
- Total: 40 rows, sequence 1–40 intact in plan order.
- Verified for merge: 0 / 40.
- Change versus input proposal: 29/0/11 → 32/0/8 (rows 4, 5, 38 flipped OPEN → REACHABLE on fresh prints).

## Gaps the merger must close before merging

1. Saved full-repo grep for the 3 OPEN rows (rows 1, 3, 16). Any hit flips that
   row to REACHABLE. CLOSED 2026-11-01: PeerInfo.java print (rows 18, 20) and the
   data-array → libtorrent-array convert site (row 34) — both found on fresh prints, see table.
   CLOSED 2026-11-01 round 2: rows 8, 10 (see round-2 addendum); the 252-file
   app-Java greps saved in `~/workspace/b323334-openclose2-src/` are the
   round-2 evidence for rows 1, 3, 16 (zero app-Java caller), but they do NOT
   by themselves flip those rows to UNREACHABLE — see CONDITIONAL table.
2. CLOSED 2026-11-01: TorrentSessionImpl.java, TorrentDownloadImpl.java and
   DetailTorrentViewModel.java are now freshly fetched and every cited line was confirmed
   (TorrentSessionImpl:170 SessionLogger, :730-731 IPFilter, :1117-1134 SessionErrors, :549
   prioritizeFiles; TorrentDownloadImpl:944 AdvancedPeerInfo ctor, :1528 pieces, :352-372
   SessionErrors, :406/:1194 TorrentMetaInfo, :717/:731 prioritizeFiles; DetailTorrentViewModel:
   :237-238, :299, :420, :428, :551, :560, :582, :589). Still outstanding: SessionLogger.java
   and IPFilterImpl.java definitions themselves were not freshly fetched (rows 39-40, 21-23
   definitions rest on local reprints; their caller sites are now fresh).
3. Printed launcher-to-service step; build/sampler/C1 on a full checkout; main-agent
   spot-check 1 in 5; py_compile at merge. None run or claimed here.
4. No fresh HTTP 429 was hit in this session.

## CONDITIONAL flip tables — round 2 (NOT decided, NOT flipped)

Nothing in this section changes a label. Each table states exactly what flips
if the merger/user adopts the named option, so one project-wide rule can be
applied uniformly (in particular, the same rule must be applied to the
parcel/hashCode/toString rows in batches 21/22/28/29/39-42, which were left
OPEN on the same evidence class).

- **UNREACHABLE-on-tree-grep-absence (undecided).** IF the merger rules that
  zero hits in a saved 252-file app-Java grep, with no `res`-XML / generated-code
  / framework site, suffices for `no_trigger_in_app`, THEN: row 1
  FileTree.setType → UNREACHABLE `no_trigger_in_app` (ctors set `isLeaf`
  directly; zero app-Java `.setType(` caller on a FileTree receiver in
  `grep-setters-getters.txt`); row 3 FileTree.toString → UNREACHABLE
  `no_trigger_in_app` ONLY IF its two conditional hosts (batch 33 row 8,
  this batch row 16) are also ruled UNREACHABLE — a toString with only OPEN
  hosts is not independently unreachable while a host could still flip;
  row 16 TorrentContentFileTree.toString → UNREACHABLE `no_trigger_in_app`
  (zero app-Java caller; its body is a caller of rows 34/3 and 33/16, not
  vice versa). IF the merger does NOT adopt that rule, all three stay OPEN.
  The greps supporting the "zero" premise are saved in
  `~/workspace/b323334-openclose2-src/`; they do not cover `res` XML, Room-
  generated code, or framework dispatch, and that gap is why this round did
  not flip them.
- **toString dependency (conditional, no new rule needed).** Row 3 flips to
  REACHABLE SOURCE together with EITHER host: batch 33 row 8
  BencodeFileTree.toString (`super.toString()` at BencodeFileTree.java:128)
  or this batch row 16 TorrentContentFileTree.toString (`super.toString()` at
  TorrentContentFileTree.java:178). Row 16 flipping alone does NOT flip row 3's
  other host. Row 16's own body concat `", priority=" + priority`
  (TorrentContentFileTree.java:179) would flip batch 33 row 16
  FilePriority.toString together with row 16 — that row is in batch 33, not
  flipped here. The `", parent=" + parent` concat inside FileTree.toString
  itself (FileTree.java:218) is self-recursion, not a flip for row 3.
- **Strict-entry.** Applies to ALL 37 REACHABLE proposals, including rows 8
  and 10 flipped this round. Under a strict launcher-entry rule they would
  fall back to OPEN with the rest; this round did not decide the rule.

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
