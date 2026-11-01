# LibreTorrent batch 32 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
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

## Per-row table — 40 rows, plan order

| # | Method | Proposed label | confirmed_by | Printed citation / note |
|---|---|---|---|---|
| 1 | Torrent.writeToParcel | OPEN | — | Torrent.java:142; no printed marshalling site for Torrent. |
| 2 | Torrent$1.<init> | OPEN | — | CREATOR anonymous class Torrent.java:157; no printed invocation. |
| 3 | Torrent$1.createFromParcel | OPEN | — | Torrent.java:160; framework dispatch only, not printed. |
| 4 | Torrent$1.newArray | OPEN | — | Torrent.java:166; same as row 3. |
| 5 | TorrentTagInfo.<init> | OPEN | — | TorrentTagInfo.java:54; no printed `new TorrentTagInfo` site. |
| 6 | TorrentTagInfo.equals | OPEN | — | TorrentTagInfo.java:63; no printed caller. |
| 7 | TorrentTagInfo.hashCode | OPEN | — | TorrentTagInfo.java:74; no printed caller. |
| 8 | TorrentTagInfo.toString | OPEN | — | TorrentTagInfo.java:82; no printed caller. |
| 9 | BencodeFileItem.<clinit> | REACHABLE proposed | INFERRED | Static CREATOR BencodeFileItem.java:95; class loaded via Utils.getFileList / TorrentMetaInfo.getMetaInfo on the AddTorrent route. |
| 10 | BencodeFileItem.<init>(Parcel) | OPEN | — | BencodeFileItem.java:44; called only from CREATOR :99 and from TorrentMetaInfo Parcel ctor (itself OPEN) via readTypedList. |
| 11 | BencodeFileItem.<init>(String,int,long) | REACHABLE proposed | SOURCE | Utils.java:145 in getFileList():142 (local reprint, see header). |
| 12 | BencodeFileItem.compareTo | REACHABLE proposed | SOURCE | BencodeFileTreeUtils.java buildFileTree(): Collections.sort(filesCopy) — fresh fetch :55. |
| 13 | BencodeFileItem.describeContents | OPEN | — | BencodeFileItem.java:82; no printed caller. |
| 14 | BencodeFileItem.getIndex | REACHABLE proposed | SOURCE | BencodeFileTreeUtils.java buildFileTree loop: file.getIndex() — fresh fetch :102-105. |
| 15 | BencodeFileItem.getPath | REACHABLE proposed | SOURCE | BencodeFileTreeUtils.java buildFileTree loop: file.getPath() — fresh fetch :73-96. |
| 16 | BencodeFileItem.getSize | REACHABLE proposed | SOURCE | BencodeFileTreeUtils.java buildFileTree loop: file.getSize() — fresh fetch :102-103. |
| 17 | BencodeFileItem.setIndex | OPEN | — | BencodeFileItem.java:76; no printed caller (Utils uses the ctor, not setters). |
| 18 | BencodeFileItem.setPath | OPEN | — | BencodeFileItem.java:56; no printed caller. |
| 19 | BencodeFileItem.setSize | OPEN | — | BencodeFileItem.java:66; no printed caller. |
| 20 | BencodeFileItem.toString | OPEN | — | BencodeFileItem.java:119; no printed caller. |
| 21 | BencodeFileItem.writeToParcel | OPEN | — | BencodeFileItem.java:88; only reachable via TorrentMetaInfo.writeToParcel (itself OPEN). |
| 22 | BencodeFileItem$1.<init> | OPEN | — | CREATOR anonymous class :95; no printed invocation. |
| 23 | BencodeFileItem$1.createFromParcel | OPEN | — | BencodeFileItem.java:99; framework dispatch only, not printed. |
| 24 | BencodeFileItem$1.newArray | OPEN | — | BencodeFileItem.java:105; same as row 23. |
| 25 | TorrentMetaInfo.<clinit> | REACHABLE proposed | INFERRED | Static CREATOR TorrentMetaInfo.java:149; class loaded at AddTorrentViewModel.java:242/293, TorrentSessionImpl.java:299 (local reprints). |
| 26 | TorrentMetaInfo.<init>(Parcel) | OPEN | — | TorrentMetaInfo.java:113; called only from CREATOR :153, not printed as invoked. |
| 27 | TorrentMetaInfo.<init>(FileInputStream) | REACHABLE proposed | SOURCE | AddTorrentViewModel.java:293; TorrentSessionImpl.java:299; TorrentEngine.java:384 (local reprints). |
| 28 | TorrentMetaInfo.<init>(String,String) | REACHABLE proposed | SOURCE | AddTorrentViewModel.java:242 (local reprint). |
| 29 | TorrentMetaInfo.<init>(TorrentInfo) | OPEN | — | TorrentMetaInfo.java:73; no printed caller (TorrentEngine:464 uses the byte[] ctor). |
| 30 | TorrentMetaInfo.<init>(byte[]) | REACHABLE proposed | SOURCE | TorrentEngine.java:464 `new TorrentMetaInfo(bencode)` (local reprint). |
| 31 | TorrentMetaInfo.describeContents | OPEN | — | TorrentMetaInfo.java:129; no printed caller. |
| 32 | TorrentMetaInfo.equals | OPEN | — | TorrentMetaInfo.java:172; no printed caller. |
| 33 | TorrentMetaInfo.getMetaInfo | REACHABLE proposed | SOURCE | Private, called by the byte[]/TorrentInfo/FileInputStream ctors printed in TorrentMetaInfo.java; the FileInputStream and byte[] ctors are REACHABLE (rows 27, 30). |
| 34 | TorrentMetaInfo.hashCode | OPEN | — | TorrentMetaInfo.java:166; no printed caller. |
| 35 | TorrentMetaInfo.toString | OPEN | — | TorrentMetaInfo.java:195; no printed caller. |
| 36 | TorrentMetaInfo.writeToParcel | OPEN | — | TorrentMetaInfo.java:135; no printed marshalling site for TorrentMetaInfo. |
| 37 | TorrentMetaInfo$1.<init> | OPEN | — | CREATOR anonymous class :149; no printed invocation. |
| 38 | TorrentMetaInfo$1.createFromParcel | OPEN | — | TorrentMetaInfo.java:153; framework dispatch only, not printed. |
| 39 | TorrentMetaInfo$1.newArray | OPEN | — | TorrentMetaInfo.java:159; same as row 38. |
| 40 | BencodeFileTree.<init>(int,String,long,int,BencodeFileTree) | REACHABLE proposed | SOURCE | BencodeFileTreeUtils.java makeObject: `new BencodeFileTree(index, name, size, FileNode.Type.FILE, parent)` — fresh fetch :124, on the AddTorrent trunk (AddTorrentViewModel.java:379, local reprint). |

## Counts — mechanically verified

- REACHABLE proposed: 12 (rows 9, 11, 12, 14, 15, 16, 25, 27, 28, 30, 33, 40)
- UNREACHABLE proposed: 0
- OPEN: 28 (rows 1-8, 10, 13, 17-24, 26, 29, 31, 32, 34-39)
- Total: 40 rows, sequence 1–40 intact in plan order.
- Verified for merge: 0 / 40.

## Gaps the merger must close before merging

1. Saved full-repo grep for the 28 OPEN rows (especially TorrentTagInfo all 4, parcel trios,
   TorrentMetaInfo(TorrentInfo), BencodeFileItem setters/toString). Any hit flips that row to REACHABLE.
2. Fresh connector prints of the caller files flagged as local reprints above
   (Utils.java, AddTorrentViewModel.java, TorrentSessionImpl.java, TorrentEngine.java) before
   merging rows 11, 25, 27, 28, 30, 40 that rest on them.
3. Printed launcher-to-AddTorrent step; build/sampler/C1 on a full checkout; main-agent
   spot-check 1 in 5; py_compile at merge. None run or claimed here.
4. No fresh HTTP 429 was hit in this session.

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
