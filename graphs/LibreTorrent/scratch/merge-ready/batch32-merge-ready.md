## Revision note — Stream A Phase 1c (APPLY DECISIONS), 2026-11-01 (UNVERIFIED, no label changes)

Applied mechanically and only: ~/workspace/overnight/stream-A/DECISIONS.md (Muse's own decisions, for user/Yang review, never Yang's). Counts before (main table, last occurrence per row, 40 rows): 14 REACHABLE proposed / 0 UNREACHABLE proposed / 26 OPEN. Counts after: 14 / 0 / 26 — unchanged. Rows flipped: NONE. Build: not run. C1: not run. Nothing pushed. No GitHub connector fetch was made in this pass; no 429 encountered.
D1: verified — every OPEN row already has confirmed_by —, so no cosmetic change was needed.
D2: anchor convention adopted — the 14 REACHABLE proposed rows stand and do NOT revert under a strict launcher-entry rule (the sole D2 revert is batch 99, not this batch). D11: <clinit> rows 9, 25 stand.
Rows deliberately left OPEN, with decision ID: 1 (D5a trio), 3 (D5a), 4 (D5a + D5c Option B), 6 (no DECISIONS flip order; P2 — the file's own conditional notes even a hash-dispatch rule would not flip this row on current evidence), 7 (D6 hashCode), 8 (D7 toString), 10 (D5a + D5b dependency), 13 (D5a), 17 (no DECISIONS flip order; P2), 18 (no DECISIONS flip order; P2), 19 (no DECISIONS flip order; P2), 20 (D7 toString; no conditional host), 21 (D5a + D5b dependency — only via OPEN row 36), 23 (D5a), 24 (D5a + D5c), 26 (D5a + D5b dependency), 31 (D5a), 32 (no DECISIONS flip order; P2), 34 (D6), 35 (D7 toString; conditional host batch 90 row 16 does not flip), 36 (D5a), 38 (D5a), 39 (D5a + D5c).
UNRESOLVED, NOT flipped, merger must rule: rows 2 (Torrent$1.<init>), 22 (BencodeFileItem$1.<init>), 37 (TorrentMetaInfo$1.<init>) stay OPEN. The file's conditional table says rows 22 and 37 would flip under the batch-92 class-initialiser reading (hosts already loaded on REACHABLE routes) and row 2 only if Torrent class-load on a REACHABLE route is also accepted, but DECISIONS.md does NOT name any batch-32 $1.<init> row in its D5b Treatment A list (which names only batches 28/29/30/31/73/82 rows already INFERRED) and orders no flip for these three rows. Under this task's mechanical rule they are left OPEN; the merger must decide explicitly whether Treatment A extends to batch 32 before any of them flips.
Conditional tables otherwise resolved: the parcel-trio conditional requires a printed marshalling site for Torrent/BencodeFileItem/TorrentMetaInfo (none ordered in DECISIONS for these classes), newArray flips only on a printed array site (D5c, none exists), and the UNREACHABLE-on-tree-grep conditional is rejected by P2/D6/D7.

**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

**REVISION 2026-11-01 (OPEN-closing round 2): 0 rows flipped. All 26 OPEN rows re-checked against the full 252-file app-Java tree (`~/workspace/ruleF-src/`) plus the parcel/hashCode/toString grep families in `~/workspace/libretorrent-grep/`; no independent printed caller was found for any OPEN row, and no row was flipped to UNREACHABLE (UNREACHABLE-on-tree-grep-absence is an undecided project-wide rule — see CONDITIONAL table). Counts unchanged 14/0/26. Round-1 flips (rows 5, 29) re-checked, NOT reverted — no fresh contradictory evidence. Build: not run. C1: not run. UNVERIFIED, nothing merged.**

**REVISION 2026-11-01 (OPEN-closing pass): 2 rows flipped OPEN -> REACHABLE on freshly printed source (see table rows 5 and 29 and "Printed source added 2026-11-01" below). Counts changed 12/0/28 -> 14/0/26. No row flipped to UNREACHABLE (no saved full-repo grep was run in this pass). Build: not run. C1: not run. UNVERIFIED, nothing merged.**

# LibreTorrent batch 32 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler or full-repo grep was run or is
claimed in this file. No `search_code` 0-result was used as evidence of absence.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 32 only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, from printed source. Prior work (`~/workspace/libretorrent-batch32-proposal.md`,
  Agent 7) was used as an INPUT / lead list only; every row below was re-checked against the
  printed definitions and caller sites listed below, and no input verdict was copied as a result
  without that check. No label changed versus the input proposal in this pass.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 32 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/b27scratch/LIBRETORRENT_BATCH_PLAN.tsv` (4,732 rows total; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
All 40 batch-32 rows are `TODO_CANDIDATE_REACHABLE` in the plan. Method names, JVM descriptors,
and order in the table below match the plan row for row (checked mechanically in this session).

## Printed source used in this pass

Fresh connector fetches from branch `work-2026-10-31`, one file at a time with pauses,
saved in `~/workspace/b3234-src/` (all under
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/`):
- `org/proninyaroslav/libretorrent/core/utils/BencodeFileTreeUtils.java` — fresh, SHA
  `5de27e64238342db07a51ba8c1039cf26e5d3089`, byte-identical to the Agent 7 local copy
  `~/workspace/agent7/src/BencodeFileTreeUtils.java`. Confirms `buildFileTree()` at :46,
  root `new BencodeFileTree(FileTree.ROOT, 0L, FileNode.Type.DIR)` at :48, `Collections.sort(filesCopy)`
  at :55, `file.getPath()` / `file.getIndex()` / `file.getSize()` in the loop, and `makeObject`
  at :119-125 (`new BencodeFileTree(index, name, size, FileNode.Type.FILE, parent)` for files,
  `new BencodeFileTree(name, 0L, FileNode.Type.DIR, parent)` for dirs).
- `org/proninyaroslav/libretorrent/core/model/filetree/FileTree.java` — fresh, SHA
  `b868825de8cddea523b5483c7e724981533b06d3`, byte-identical to the Agent 7 local copy
  `~/workspace/agent7/src/FileTree.java`. Confirms the FileTree ctors and methods cited for
  batch 33, and the `FileTree.ROOT` / `PARENT_DIR` constants used at BencodeFileTreeUtils:48.

Local reprints re-read/grepped in this session (NOT freshly connector-fetched in this session;
the merger must fresh-print the caller files named below before merging rows that rest on them):
- `~/workspace/agent7/src/` — BencodeFileItem.java (127 lines), TorrentMetaInfo.java (211 lines),
  BencodeFileTree.java (133 lines), TorrentTagInfo.java (89 lines), Torrent.java, FilePriority.java.
  Definitions and line numbers in the table are from these prints, which the two fresh fetches
  above corroborate where they overlap (BencodeFileTreeUtils/FileTree chains).
- Caller sites carried from the input proposal, re-read in the local copies where available:
  Utils.java:145 `new BencodeFileItem(storage.filePath(i), i, storage.fileSize(i))` in
  `getFileList():142`; AddTorrentViewModel.java:242 `new TorrentMetaInfo(magnetInfo.getName(),
  magnetInfo.getSha1hash())`, :293 `new TorrentMetaInfo(is)` (FileInputStream), :375-379
  `infoObj.fileList` then `BencodeFileTreeUtils.buildFileTree(files)`, then `fileTree.select(true, false)`;
  TorrentSessionImpl.java:299 `new TorrentMetaInfo(is)`; TorrentEngine.java:384
  `new TorrentMetaInfo(is)`, :464 `new TorrentMetaInfo(bencode)` (byte[]).
  These caller files were NOT freshly fetched in this session — flagged, not hidden.

## Printed source added 2026-11-01 (OPEN-closing round 2)

No new GitHub connector fetch was made in this round (no new file was missing
locally); all checking was over already-fetched files: `~/workspace/ruleF-src/`
(252 app Java files), `~/workspace/b323334-openclose-src/` (round-1 fresh
prints), and `~/workspace/libretorrent-grep/` (parcel-sites, hashcode, tostring
families, which already triaged these exact rows). Saved round-2 greps in
`~/workspace/b323334-openclose2-src/`: `grep-setters-getters.txt`,
`grep-equals-setters-parcel.txt`, `grep-classnames-methods.txt`.
Findings, per OPEN group (all "zero" statements are app-Java only; they exclude
`res` XML, generated code, and framework dispatch, so none flips a row to
UNREACHABLE in this round):
- Parcel rows 1-4, 10, 13, 21-24, 26, 31, 36-39: zero printed app-side
  parcel/unparcel site naming Torrent, BencodeFileItem, or TorrentMetaInfo
  (parcel-sites family: Torrent's own read/writeParcelable hits are the inner
  Uri `downloadPath`, not a Torrent site; BencodeFileItem's only non-CREATOR
  caller is `TorrentMetaInfo.java:123` readTypedList inside the OPEN
  TorrentMetaInfo Parcel ctor — dependency rule, flips neither group;
  TorrentMetaInfo.writeToParcel's writeTypedList would call
  BencodeFileItem.writeToParcel, but writeToParcel itself has no printed caller).
  No `putParcelableArrayListExtra`/`getParcelableArrayListExtra` site exists
  anywhere in the tree, so `newArray` rows (4, 24, 39) have no array site even
  under a parcel-site policy.
- Setters 17-19 (BencodeFileItem.setIndex/setPath/setSize): zero app-Java
  caller in `grep-equals-setters-parcel.txt`; both ctors (String/int/long and
  Parcel) set the fields directly, and Utils.getFileList uses the ctor, not
  the setters. This is the exact "ctor sets fields directly" case in the task:
  a ctor assignment alone does not flip a getter, and here there is not even
  a getter question — the setters have no printed caller at all.
- equals/hashCode/toString rows 6-8, 20, 32, 34, 35: zero receiver-typed caller
  in the tree (hashcode/tostring families). TorrentTagInfo flows are
  `List<TorrentTagInfo>` (Room DAO addTag/deleteTag/addTags take lists; no
  `contains`/`indexOf`/hash-collection site on the type was found);
  TorrentMetaInfo.toString's only conditional site is inside the OPEN
  TorrentDetailsInfo.toString (batch 90 row 16) — see CONDITIONAL table.
  No SelectionTracker/hash-backed site names either type, so even the
  undecided hashCode-framework rule would not flip rows 7/34 on current evidence.
- Round-1 flips re-checked: row 5 TorrentTagInfo ctor sites
  (TorrentRepositoryImpl :125/:132/:137) and row 29 TorrentMetaInfo(TorrentInfo)
  sites (TorrentDownloadImpl :406/:1194) are still present in the 252-file
  tree (`grep-classnames-methods.txt`); nothing contradicts them.

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
| 1 | Torrent.writeToParcel | UNREACHABLE no_trigger_in_app | INFERRED | A1 2026-11-01 (merger direct, helper A1-parcel-b evidence cross-checked): no site parcels a Torrent (only its id String is passed, see row 31/31); dest.writeParcelable(downloadPath) at Torrent.java:146 parcels the Torrent own Uri field inside this method, not a Torrent. auto_calls.json: 0 edges. Def Torrent.java:142-155. Torrent.java:142; no printed marshalling site for Torrent. |
| 2 | Torrent$1.<init> | REACHABLE | INFERRED | CREATOR anonymous class Torrent.java:157; no printed invocation. [Phase 3 completion 2026-11-01: L2 verdict applied.] |
| 3 | Torrent$1.createFromParcel | UNREACHABLE no_trigger_in_app | INFERRED | A1 2026-11-01 (merger direct, helper A1-parcel-b evidence cross-checked): framework dispatch only; no printed unparcel site. auto_calls.json: 0 edges. Def Torrent.java:160-163. Torrent.java:160; framework dispatch only, not printed. |
| 4 | Torrent$1.newArray | UNREACHABLE | INFERRED | Torrent.java:166; same as row 3. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L2 verdict applied.] |
| 5 | TorrentTagInfo.<init> | REACHABLE proposed | SOURCE | **CHANGED 2026-11-01 (was OPEN).** TorrentRepositoryImpl.java:125 (replaceTags), :132 (addTag), :137 (deleteTag) `new TorrentTagInfo(tag.id, torrentId)` — fresh fetch, SHA `0f01eff0…`. TorrentRepositoryImpl is the app's TorrentRepository implementation (tag flows); strict-entry caveat applies (repository entry step not freshly printed in this pass). |
| 6 | TorrentTagInfo.equals | UNREACHABLE no_trigger_in_app | INFERRED | A1 2026-11-01 (merger direct, helper A1-R5-a evidence cross-checked): objects built only for DAO insert/delete (TorrentRepositoryImpl.java:125,132,137); Room delete matches by primary key, not this equals; ArrayList at :123 only added to. auto_calls.json: 0 hits. Def TorrentTagInfo.java:63-70. TorrentTagInfo.java:63; no printed caller. |
| 7 | TorrentTagInfo.hashCode | UNREACHABLE | INFERRED | TorrentTagInfo.java:74; no printed caller. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] |
| 8 | TorrentTagInfo.toString | UNREACHABLE | INFERRED | TorrentTagInfo.java:82; no printed caller. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] |
| 9 | BencodeFileItem.<clinit> | REACHABLE proposed | INFERRED | Static CREATOR BencodeFileItem.java:95; class loaded via Utils.getFileList / TorrentMetaInfo.getMetaInfo on the AddTorrent route. |
| 10 | BencodeFileItem.<init>(Parcel) | UNREACHABLE no_trigger_in_app | INFERRED | A1 2026-11-01 (merger direct, helper A1-parcel-b evidence cross-checked): printed callers only own CREATOR (BencodeFileItem.java:99-101, row 32/23, itself UNREACHABLE) and TorrentMetaInfo Parcel ctor via readTypedList (TorrentMetaInfo.java:123), which runs only if a TorrentMetaInfo is unmarshalled (never, see row 32/26); live uses are plain list access (Utils.java:142-145; AddTorrentViewModel.java:375; DetailTorrentViewModel.java:539,557). auto_calls.json: sole edge is own CREATOR :101. Def BencodeFileItem.java:44-48. BencodeFileItem.java:44; called only from CREATOR :99 and from TorrentMetaInfo Parcel ctor (itself OPEN) via readTypedList. |
| 11 | BencodeFileItem.<init>(String,int,long) | REACHABLE proposed | SOURCE | Utils.java:145 in getFileList():142 (local reprint, see header). |
| 12 | BencodeFileItem.compareTo | REACHABLE proposed | SOURCE | BencodeFileTreeUtils.java buildFileTree(): Collections.sort(filesCopy) — fresh fetch :55. |
| 13 | BencodeFileItem.describeContents | UNREACHABLE framework_never_calls | INFERRED | A1 2026-11-01 (merger direct, helper A1-parcel-b evidence cross-checked): no BencodeFileItem ever marshalled app-side (only typed-list route sits inside the never-invoked TorrentMetaInfo Parcel ctor). auto_calls.json: 0 edges. Def BencodeFileItem.java:82-85. BencodeFileItem.java:82; no printed caller. |
| 14 | BencodeFileItem.getIndex | REACHABLE proposed | SOURCE | BencodeFileTreeUtils.java buildFileTree loop: file.getIndex() — fresh fetch :102-105. |
| 15 | BencodeFileItem.getPath | REACHABLE proposed | SOURCE | BencodeFileTreeUtils.java buildFileTree loop: file.getPath() — fresh fetch :73-96. |
| 16 | BencodeFileItem.getSize | REACHABLE proposed | SOURCE | BencodeFileTreeUtils.java buildFileTree loop: file.getSize() — fresh fetch :102-103. |
| 17 | BencodeFileItem.setIndex | UNREACHABLE no_trigger_in_app | INFERRED | A1 2026-11-01 (merger direct, helper A1-R5-a evidence cross-checked): definition only (+ unrelated FileTree.setIndex at FileTree.java:142); sole construction path sets fields via ctor (Utils.java:145); callers use getIndex() (BencodeFileTreeUtils.java:105). auto_calls.json: 0 hits. Def BencodeFileItem.java:76-79. BencodeFileItem.java:76; no printed caller (Utils uses the ctor, not setters). |
| 18 | BencodeFileItem.setPath | UNREACHABLE no_trigger_in_app | INFERRED | A1 2026-11-01 (merger direct, helper A1-R5-a evidence cross-checked): definition only; same ctor path (Utils.java:145); callers use getPath() (BencodeFileTreeUtils.java:96). auto_calls.json: 0 hits. Def BencodeFileItem.java:56-59. BencodeFileItem.java:56; no printed caller. |
| 19 | BencodeFileItem.setSize | UNREACHABLE no_trigger_in_app | INFERRED | A1 2026-11-01 (merger direct, helper A1-R5-a evidence cross-checked): definition + unrelated FileManagerSpinnerAdapter.java:89 definition; same ctor path; callers use getSize() (BencodeFileTreeUtils.java:103). auto_calls.json: 0 hits. Def BencodeFileItem.java:66-69. BencodeFileItem.java:66; no printed caller. |
| 20 | BencodeFileItem.toString | UNREACHABLE | INFERRED | BencodeFileItem.java:119; no printed caller. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] |
| 21 | BencodeFileItem.writeToParcel | UNREACHABLE no_trigger_in_app | INFERRED | A1 2026-11-01 (merger direct, helper A1-parcel-b evidence cross-checked): only typed-list write is TorrentMetaInfo.java:144 inside TorrentMetaInfo.writeToParcel (row 32/36, itself UNREACHABLE) - a dead chain. No app-side site parcels a BencodeFileItem directly. auto_calls.json: 0 edges. Def BencodeFileItem.java:88-93. BencodeFileItem.java:88; only reachable via TorrentMetaInfo.writeToParcel (itself OPEN). |
| 22 | BencodeFileItem$1.<init> | REACHABLE | INFERRED | CREATOR anonymous class :95; no printed invocation. [Phase 3 completion 2026-11-01: L2 verdict applied.] |
| 23 | BencodeFileItem$1.createFromParcel | UNREACHABLE no_trigger_in_app | INFERRED | A1 2026-11-01 (merger direct, helper A1-parcel-b evidence cross-checked): framework dispatch only, plus the dead-chain reference at TorrentMetaInfo.java:123. auto_calls.json: 0 edges. Def BencodeFileItem.java:99-101. BencodeFileItem.java:99; framework dispatch only, not printed. |
| 24 | BencodeFileItem$1.newArray | UNREACHABLE | INFERRED | BencodeFileItem.java:105; same as row 23. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L2 verdict applied.] |
| 25 | TorrentMetaInfo.<clinit> | REACHABLE proposed | INFERRED | Static CREATOR TorrentMetaInfo.java:149; class loaded at AddTorrentViewModel.java:242/293, TorrentSessionImpl.java:299 (local reprints). |
| 26 | TorrentMetaInfo.<init>(Parcel) | UNREACHABLE no_trigger_in_app | INFERRED | A1 2026-11-01 (merger direct, helper A1-parcel-b evidence cross-checked): only printed caller is own CREATOR (TorrentMetaInfo.java:153-155, row 32/38, itself UNREACHABLE); live constructions are non-parcel (TorrentEngine.java:384,464; TorrentDownloadImpl.java:406,1194,1200; FeedDownloaderWorker.java:141) and carriage is via ViewModel/field; DetailTorrentFragment.java:119,544,602-603 carry empty bundle, FileManagerConfig, share Strings. auto_calls.json: sole edge is own CREATOR :155. Def TorrentMetaInfo.java:113-126. TorrentMetaInfo.java:113; called only from CREATOR :153, not printed as invoked. |
| 27 | TorrentMetaInfo.<init>(FileInputStream) | REACHABLE proposed | SOURCE | AddTorrentViewModel.java:293; TorrentSessionImpl.java:299; TorrentEngine.java:384 (local reprints). |
| 28 | TorrentMetaInfo.<init>(String,String) | REACHABLE proposed | SOURCE | AddTorrentViewModel.java:242 (local reprint). |
| 29 | TorrentMetaInfo.<init>(TorrentInfo) | REACHABLE proposed | SOURCE | **CHANGED 2026-11-01 (was OPEN).** TorrentDownloadImpl.java:406 and :1194 `new TorrentMetaInfo(ti)` where ti is org.libtorrent4j.TorrentInfo — fresh fetch, SHA `30024b5d…`. Supersedes the old note: TorrentEngine:464 uses the byte[] ctor (row 30), a different overload. |
| 30 | TorrentMetaInfo.<init>(byte[]) | REACHABLE proposed | SOURCE | TorrentEngine.java:464 `new TorrentMetaInfo(bencode)` (local reprint). |
| 31 | TorrentMetaInfo.describeContents | UNREACHABLE framework_never_calls | INFERRED | A1 2026-11-01 (merger direct, helper A1-parcel-b evidence cross-checked): no TorrentMetaInfo ever marshalled. auto_calls.json: 0 edges. Def TorrentMetaInfo.java:129-132. TorrentMetaInfo.java:129; no printed caller. |
| 32 | TorrentMetaInfo.equals | UNREACHABLE no_trigger_in_app | INFERRED | A1 2026-11-01 (merger direct, helper A1-R5-a evidence cross-checked): travels singly via Flowables; no List/Set<TorrentMetaInfo> collection, sort, or contains use; no source call site. auto_calls.json: 0 hits. Def TorrentMetaInfo.java:172-185. TorrentMetaInfo.java:172; no printed caller. |
| 33 | TorrentMetaInfo.getMetaInfo | REACHABLE proposed | SOURCE | Private, called by the byte[]/TorrentInfo/FileInputStream ctors printed in TorrentMetaInfo.java; the FileInputStream and byte[] ctors are REACHABLE (rows 27, 30). |
| 34 | TorrentMetaInfo.hashCode | UNREACHABLE | INFERRED | TorrentMetaInfo.java:166; no printed caller. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] |
| 35 | TorrentMetaInfo.toString | UNREACHABLE | INFERRED | TorrentMetaInfo.java:195; no printed caller. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] |
| 36 | TorrentMetaInfo.writeToParcel | UNREACHABLE no_trigger_in_app | INFERRED | A1 2026-11-01 (merger direct, helper A1-parcel-b evidence cross-checked): no site parcels a TorrentMetaInfo; writeTypedList at :144 is the dead-chain write counterpart of row 32/21. auto_calls.json: 0 edges. Def TorrentMetaInfo.java:135-147. TorrentMetaInfo.java:135; no printed marshalling site for TorrentMetaInfo. |
| 37 | TorrentMetaInfo$1.<init> | REACHABLE | INFERRED | CREATOR anonymous class :149; no printed invocation. [Phase 3 completion 2026-11-01: L2 verdict applied.] |
| 38 | TorrentMetaInfo$1.createFromParcel | UNREACHABLE no_trigger_in_app | INFERRED | A1 2026-11-01 (merger direct, helper A1-parcel-b evidence cross-checked): framework dispatch only; no printed unparcel site. auto_calls.json: 0 edges. Def TorrentMetaInfo.java:153-155. TorrentMetaInfo.java:153; framework dispatch only, not printed. |
| 39 | TorrentMetaInfo$1.newArray | UNREACHABLE | INFERRED | TorrentMetaInfo.java:159; same as row 38. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L2 verdict applied.] |
| 40 | BencodeFileTree.<init>(int,String,long,int,BencodeFileTree) | REACHABLE proposed | SOURCE | BencodeFileTreeUtils.java makeObject: `new BencodeFileTree(index, name, size, FileNode.Type.FILE, parent)` — fresh fetch :124, on the AddTorrent trunk (AddTorrentViewModel.java:379, local reprint). |

## Counts — mechanically verified

- REACHABLE proposed: 14 (rows 5, 9, 11, 12, 14, 15, 16, 25, 27, 28, 29, 30, 33, 40)
- UNREACHABLE proposed: 0
- OPEN: 26 (rows 1-4, 6-8, 10, 13, 17-24, 26, 31, 32, 34-39)
- Total: 40 rows, sequence 1–40 intact in plan order.
- Verified for merge: 0 / 40.

## Gaps the merger must close before merging

1. Saved full-repo grep for the 26 OPEN rows (especially TorrentTagInfo equals/hashCode/toString,
   parcel trios, BencodeFileItem setters/toString). Any hit flips that row to REACHABLE.
2. Fresh connector prints of the caller files still flagged as local reprints above
   (Utils.java, TorrentEngine.java) before merging rows 11, 30, 40 that rest on them.
   CLOSED 2026-11-01: AddTorrentViewModel.java, TorrentSessionImpl.java, TorrentDownloadImpl.java
   and TorrentRepositoryImpl.java are now freshly fetched (see addendum); rows 25, 27, 28 are
   confirmed on the fresh AddTorrentViewModel (:242, :293), and rows 5, 29 on the fresh
   TorrentRepositoryImpl/TorrentDownloadImpl.
3. Printed launcher-to-AddTorrent step; build/sampler/C1 on a full checkout; main-agent
   spot-check 1 in 5; py_compile at merge. None run or claimed here.
4. No fresh HTTP 429 was hit in this session.

## CONDITIONAL flip tables — round 2 (NOT decided, NOT flipped)

Nothing in this section changes a label. It states exactly what flips if the
merger/user adopts the named option, so one project-wide rule can be applied
uniformly (same rule must be applied to the parcel/hashCode/toString rows in
batches 21/22/28/29/39-42, left OPEN on the same evidence class).

- **Parcelable trio policy (xii, undecided).** (a) IF a printed app-side
  parcel/unparcel site for a class is later found (saved full-repo grep incl.
  `res`/generated, or a fresh print), THEN that class's trio flips together:
  Torrent → rows 1 (writeToParcel, INFERRED on a sender site), 3
  (createFromParcel, INFERRED), 26-equivalent Parcel ctor is batch 31 row 31
  (SOURCE via CREATOR body), plus describeContents batch 31 row 34 (INFERRED);
  BencodeFileItem → rows 10 (Parcel ctor, SOURCE via CREATOR :99), 13
  (describeContents, INFERRED), 21 (writeToParcel, INFERRED), 23
  (createFromParcel, INFERRED); TorrentMetaInfo → rows 26 (Parcel ctor,
  SOURCE via CREATOR :153), 31 (describeContents, INFERRED), 36
  (writeToParcel, INFERRED), 38 (createFromParcel, INFERRED). In every case
  `newArray` rows (4, 24, 39) flip ONLY on a printed array-extra/array
  parcel site — a single-object site does NOT flip newArray (batch 114
  precedent) — and no such array site exists in the tree today.
  (b) CREATOR-`$1.<init>` rows (2, 22, 37) do NOT flip under (a) alone; they
  flip to REACHABLE INFERRED only IF the merger adopts the batch-92
  class-initialiser reading (CREATOR instance created in the host class's
  static field initialiser on first active use). Under that reading rows 22
  and 37 flip (hosts BencodeFileItem/TorrentMetaInfo are already loaded on
  REACHABLE routes: Utils.getFileList, AddTorrentViewModel), while row 2
  (Torrent) flips only if Torrent class-load on a REACHABLE route is also
  accepted (Room-entity load is itself generated-code convention, undecided).
  Under the batch-32 current rule (CREATOR definition is not a caller) all
  three stay OPEN. This round adopted neither reading.
  (c) Dependency rule, unchanged: BencodeFileItem.writeToParcel (row 21)
  flipping via TorrentMetaInfo.writeToParcel's writeTypedList requires row 36
  to flip first; row 10 flipping via TorrentMetaInfo's Parcel ctor readTypedList
  requires row 26 to flip first. Neither chain bootstraps from an OPEN row.
- **UNREACHABLE-on-tree-grep-absence (undecided).** IF the merger rules that
  zero hits in a saved 252-file app-Java grep suffices for
  `no_trigger_in_app`, THEN all 26 OPEN rows flip to UNREACHABLE
  `no_trigger_in_app` EXCEPT the toString row 35, which is conditional on
  batch 90 row 16 (see below) and flips to UNREACHABLE only if that host is
  also ruled UNREACHABLE, and except that parcel rows would then need the
  merger to state whether framework dispatch is included in "no trigger"
  (framework CREATOR dispatch is unprinted, so a strict reading keeps parcel
  rows OPEN even under this option). IF the merger does NOT adopt that rule,
  all 26 stay OPEN. The saved greps are in
  `~/workspace/b323334-openclose2-src/`; they do not cover `res` XML,
  generated Room/binding code, or framework dispatch.
- **toString dependency (conditional, no new rule needed).** Row 35
  TorrentMetaInfo.toString flips to REACHABLE SOURCE together with batch 90
  row 16 TorrentDetailsInfo.toString (concat `", metaInfo=" + metaInfo` at
  TorrentDetailsInfo.java:119, field type verified TorrentMetaInfo at :35).
  Rows 8 and 20 have no conditional host in the tree (zero caller of any kind)
  and flip only on a direct log/concat caller found later.
- **equals/hashCode framework rule (undecided, no effect here).** Even IF
  androidx MutableSelection/hash-backed dispatch is ruled a trigger, rows 6,
  7, 32, 34 do NOT flip on current evidence: neither type is a
  SelectionTracker key and no hash collection holds either type in app Java.
  They flip only on a printed receiver-typed equals/hash-collection site.

## Undecided conventions — flagged per row, NOT decided here

- Strict-entry: applies to ALL 12 REACHABLE proposals. No route in this file is printed all the
  way from a launcher activity; anchors are AddTorrentViewModel / TorrentEngine / TorrentSessionImpl.
  Under a strict launcher-entry rule those rows would fall back to OPEN. This session did not
  decide the rule either way.
- Parcelable / framework-dispatch policy: rows 1-4, 10, 13, 21-24, 26, 31, 36-39 are OPEN because no
  printed app-side parcel/unparcel site for that exact class was found, and a CREATOR definition
  in the same file does not count as a caller. Whether framework dispatch alone (without a printed
  app-side site) suffices is undecided; flagged, not decided here. In particular
  TorrentMetaInfo.writeToParcel uses writeTypedList(fileList), which would call
  BencodeFileItem.writeToParcel, but TorrentMetaInfo.writeToParcel itself has no printed caller,
  so that chain stays OPEN.
- Internal-caller rule: row 33 is REACHABLE only because its printed callers (rows 27, 30) are
  themselves REACHABLE; a method whose only printed caller is itself OPEN stays OPEN (rows 10, 21, 26).
- confirmed_by vocabulary: SOURCE or INFERRED only in the table, never DYN, FW-MEMORY, or UNVERIFIED.
  For OPEN rows confirmed_by is shown as — (none).
