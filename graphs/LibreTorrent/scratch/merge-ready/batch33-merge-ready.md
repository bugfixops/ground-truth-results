# LibreTorrent batch 33 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler or full-repo grep was run or is
claimed in this file. No `search_code` 0-result was used as evidence of absence.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 33 only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, from printed source. Prior work (`~/workspace/libretorrent-batch33-proposal.md`,
  Agent 7) was used as an INPUT / lead list only; every row below was re-checked against the
  printed definitions and caller sites listed below. No label changed versus the input proposal
  in this pass.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 33 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/b27scratch/LIBRETORRENT_BATCH_PLAN.tsv` (4,732 rows total; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
All 40 batch-33 rows are `TODO_CANDIDATE_REACHABLE` in the plan. Method names, JVM descriptors,
and order in the table below match the plan row for row (checked mechanically in this session).

## Printed source used in this pass

Fresh connector fetches from branch `work-2026-10-31`, one file at a time with pauses,
saved in `~/workspace/b3234-src/` (all under
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/`):
- `org/proninyaroslav/libretorrent/core/utils/BencodeFileTreeUtils.java` — fresh, SHA
  `5de27e64238342db07a51ba8c1039cf26e5d3089`, byte-identical to the Agent 7 local copy.
  Confirms `buildFileTree()` :46, root `new BencodeFileTree(FileTree.ROOT, 0L, FileNode.Type.DIR)` :48,
  `parentTree.contains` :100, `parentTree.addChild` :106, `parentTree.getChild` :109,
  `nextParent.isFile()` :111, and `makeObject` :119-125.
- `org/proninyaroslav/libretorrent/core/model/filetree/FileTree.java` — fresh, SHA
  `b868825de8cddea523b5483c7e724981533b06d3`, byte-identical to the Agent 7 local copy.
  Confirms ctors :51/:56/:61/:66 (via the 5-arg ctor), `addChild` :75 (uses `node.getName()`),
  `contains` :80, `getChild` :85, `getChildren` :90, `getChildrenName` :95, `getChildrenIndexes` :100,
  `getChildrenCount` :110, `isFile` :115, `getParent` :120, `setParent` :125, `setName` :131,
  `getName` :137, `setIndex` :142, `getIndex` :147, `getType` :153, `setType` :159, `size()` :164
  (sums children if size 0 and children present), `getPath` :173 (walks parents),
  `compareTo` :187 (name compare), `equals` :193, `toString` :211.

Local reprints re-read/grepped in this session (NOT freshly connector-fetched in this session;
the merger must fresh-print the caller files named below before merging rows that rest on them):
- `~/workspace/agent7/src/` — BencodeFileTree.java (133 lines: ctors :35/:40/:45, isSelected :50,
  select :61 calling private doSelect, private onChildSelectChange, selectedFileSize :107,
  toString :125), FilePriority.java (114 lines: enum Type :34, ctors :36/:42, getPriority :48,
  getType :53, static typeFrom :58, private static priorityFrom :77, equals :92, toString :107).
- Caller sites carried from the input proposal (local reprints, not fresh in this session):
  AddTorrentViewModel.java:379 `BencodeFileTreeUtils.buildFileTree(files)`, :385 `fileTree.select(true, false)`,
  :411-426 getChildren (`new BencodeFileTree(PARENT_DIR, 0L, DIR, curDir.getParent())` 4-arg,
  `curDir.getChildren()`, `curDir.getChild(name)`), :458-461 getSelectedFileIndexes
  (`file.isSelected()`, `file.getIndex()`), :553 `fileTree.selectedFileSize()`, getFilePath
  (`node.getPath()`); DetailTorrentViewModel.java (b27scratch copy): getChildren
  (`curDir.getParent()`, `curDir.getChildren()`), getFilesPriority (`curDir.getChild(name)`,
  `file.getFilePriority()`, `randomPriority.equals(priority)`, `new FilePriority(FilePriority.Type.MIXED)` :323),
  makeFileTree (`new FilePriority(p)` :549); TorrentContentFileTree.java:28 field initialiser
  `new FilePriority(FilePriority.Type.IGNORE)`; FileTree.java:75 addChild uses `node.getName()`.

## Per-row table — 40 rows, plan order

| # | Method | Proposed label | confirmed_by | Printed citation / note |
|---|---|---|---|---|
| 1 | BencodeFileTree.<init>(String,long,int) | REACHABLE proposed | SOURCE | BencodeFileTreeUtils.java:48 root `new BencodeFileTree(FileTree.ROOT, 0L, FileNode.Type.DIR)` — fresh fetch. |
| 2 | BencodeFileTree.<init>(String,long,int,BencodeFileTree) | REACHABLE proposed | SOURCE | BencodeFileTreeUtils.java makeObject dir branch: `new BencodeFileTree(name, 0L, FileNode.Type.DIR, parent)` — fresh fetch :125. |
| 3 | BencodeFileTree.doSelect | REACHABLE proposed | SOURCE | Private, called by select BencodeFileTree.java:61 (select itself REACHABLE, row 6). |
| 4 | BencodeFileTree.isSelected | REACHABLE proposed | SOURCE | AddTorrentViewModel.java getSelectedFileIndexes: file.isSelected() (local reprint). |
| 5 | BencodeFileTree.onChildSelectChange | REACHABLE proposed | SOURCE | Private, called by doSelect BencodeFileTree.java (doSelect REACHABLE, row 3). |
| 6 | BencodeFileTree.select | REACHABLE proposed | SOURCE | AddTorrentViewModel.java makeFileTree: fileTree.select(true, false) (local reprint). |
| 7 | BencodeFileTree.selectedFileSize | REACHABLE proposed | SOURCE | AddTorrentViewModel.java:553 fileTree.selectedFileSize() (local reprint). |
| 8 | BencodeFileTree.toString | OPEN | — | BencodeFileTree.java:125; no printed caller (it calls FileTree.toString, not vice versa). |
| 9 | FileNode$Type.<clinit> | REACHABLE proposed | INFERRED | FileNode.Type constants used in BencodeFileTreeUtils.java:48 and FileTree construction; enum/class loaded on the AddTorrent route — fresh fetch. |
| 10 | FilePriority.<init>(Priority) | REACHABLE proposed | SOURCE | DetailTorrentViewModel.java:549 `new FilePriority(p)` (local reprint). |
| 11 | FilePriority.<init>(Type) | REACHABLE proposed | SOURCE | DetailTorrentViewModel.java:323 `new FilePriority(FilePriority.Type.MIXED)`; TorrentContentFileTree.java:28 field initialiser (local reprints). |
| 12 | FilePriority.equals | REACHABLE proposed | SOURCE | DetailTorrentViewModel.java getFilesPriority loop: `!randomPriority.equals(priority)` (local reprint). |
| 13 | FilePriority.getPriority | REACHABLE proposed | SOURCE | DetailTorrentViewModel.java:420 `file.getFilePriority().getPriority()` (local reprint). |
| 14 | FilePriority.getType | REACHABLE proposed | SOURCE | TorrentContentFileTree.java changePriority/onChildSelectChange/nonIgnoreFileSize/getAvailability call .getType() on REACHABLE methods (local reprint). |
| 15 | FilePriority.priorityFrom | REACHABLE proposed | SOURCE | Private static, called by the Type ctor FilePriority.java:42 (ctor REACHABLE, row 11). |
| 16 | FilePriority.toString | OPEN | — | FilePriority.java:107; no printed caller. |
| 17 | FilePriority.typeFrom | REACHABLE proposed | SOURCE | Static, called by the Priority ctor FilePriority.java:36 (ctor REACHABLE, row 10). |
| 18 | FilePriority$Type.<clinit> | REACHABLE proposed | INFERRED | Enum constants used at DetailTorrentViewModel.java:323 and TorrentContentFileTree.java:28 (local reprints). |
| 19 | FileTree.<clinit> | REACHABLE proposed | INFERRED | Static ROOT/PARENT_DIR FileTree.java:40-42 — fresh fetch; class loaded via BencodeFileTree/TorrentContentFileTree construction. |
| 20 | FileTree.<init>(int,String,long,int,FileTree) | REACHABLE proposed | SOURCE | BencodeFileTree.java:40 super call from the REACHABLE 5-arg BencodeFileTree ctor (batch 32 row 40). |
| 21 | FileTree.<init>(String,long,int) | REACHABLE proposed | SOURCE | BencodeFileTree.java:35 super call from the REACHABLE 3-arg BencodeFileTree ctor (row 1). |
| 22 | FileTree.<init>(String,long,int,FileTree) | REACHABLE proposed | SOURCE | BencodeFileTree.java:45 super call from the REACHABLE 4-arg BencodeFileTree ctor (row 2). |
| 23 | FileTree.addChild | REACHABLE proposed | SOURCE | BencodeFileTreeUtils.java:106 parentTree.addChild(leaf) — fresh fetch. |
| 24 | FileTree.compareTo | OPEN | — | FileTree.java:187 — fresh fetch; no printed sort/comparison of FileTree objects (BencodeFileTreeUtils sorts BencodeFileItem, not FileTree). |
| 25 | FileTree.contains | REACHABLE proposed | SOURCE | BencodeFileTreeUtils.java:100 parentTree.contains(nodes[i]) — fresh fetch. |
| 26 | FileTree.equals | OPEN | — | FileTree.java:193 — fresh fetch; no printed caller. |
| 27 | FileTree.getChild | REACHABLE proposed | SOURCE | BencodeFileTreeUtils.java:109 parentTree.getChild(nodes[i]) — fresh fetch; AddTorrentViewModel.java:426 curDir.getChild(name) (local reprint). |
| 28 | FileTree.getChildren | REACHABLE proposed | SOURCE | AddTorrentViewModel.java:420 curDir.getChildren() (local reprint). |
| 29 | FileTree.getChildrenCount | OPEN | — | FileTree.java:110 — fresh fetch; no printed caller. |
| 30 | FileTree.getChildrenIndexes | OPEN | — | FileTree.java:100 — fresh fetch; no printed caller. |
| 31 | FileTree.getChildrenName | OPEN | — | FileTree.java:95 — fresh fetch; no printed caller. |
| 32 | FileTree.getIndex | REACHABLE proposed | SOURCE | AddTorrentViewModel.java getSelectedFileIndexes: file.getIndex() for BencodeFileTree leaves (local reprint). |
| 33 | FileTree.getName | REACHABLE proposed | SOURCE | FileTree.java:75 addChild uses node.getName() — fresh fetch; addChild is REACHABLE (row 23). |
| 34 | FileTree.getParent | REACHABLE proposed | SOURCE | AddTorrentViewModel.java:418 curDir.getParent(); DetailTorrentViewModel.java getChildren parent check (local reprints). |
| 35 | FileTree.getPath | REACHABLE proposed | SOURCE | AddTorrentViewModel.java getFilePath: node.getPath() (local reprint). |
| 36 | FileTree.getType | OPEN | — | FileTree.java:153 — fresh fetch; no printed caller (FileTree.isFile reads the type field directly). |
| 37 | FileTree.isFile | REACHABLE proposed | SOURCE | BencodeFileTreeUtils.java:111 nextParent.isFile() — fresh fetch. |
| 38 | FileTree.setIndex | OPEN | — | FileTree.java:142 — fresh fetch; no printed caller (ctors set the field directly). |
| 39 | FileTree.setName | OPEN | — | FileTree.java:131 — fresh fetch; no printed caller. |
| 40 | FileTree.setParent | OPEN | — | FileTree.java:125 — fresh fetch; no printed caller (ctors set the field directly). |

## Counts — mechanically verified

- REACHABLE proposed: 29 (rows 1-7, 9-15, 17-23, 25, 27, 28, 32-35, 37)
- UNREACHABLE proposed: 0
- OPEN: 11 (rows 8, 16, 24, 26, 29, 30, 31, 36, 38, 39, 40)
- Total: 40 rows, sequence 1–40 intact in plan order.
- Verified for merge: 0 / 40.

## Gaps the merger must close before merging

1. Saved full-repo grep for the 11 OPEN rows. Any hit flips that row to REACHABLE.
2. Fresh connector prints of the caller files flagged as local reprints above
   (AddTorrentViewModel.java, DetailTorrentViewModel.java, TorrentContentFileTree.java) before
   merging rows that rest on them (rows 4, 6, 7, 10-14, 17, 18, 28, 32, 34, 35).
3. Printed launcher-to-AddTorrent/Detail step; build/sampler/C1 on a full checkout; main-agent
   spot-check 1 in 5; py_compile at merge. None run or claimed here.
4. No fresh HTTP 429 was hit in this session.

## Undecided conventions — flagged per row, NOT decided here

- Strict-entry: applies to ALL 29 REACHABLE proposals. No route in this file is printed all the
  way from a launcher activity; anchors are AddTorrentViewModel / BencodeFileTreeUtils /
  DetailTorrentViewModel. Under a strict launcher-entry rule those rows would fall back to OPEN.
  This session did not decide the rule either way.
- Internal-caller rule: a private method called by a printed REACHABLE method in the same file is
  REACHABLE via that chain (rows 3, 5, 15, 17); a method whose only printed caller is itself OPEN
  is OPEN; a public method with no printed caller at all is OPEN.
- confirmed_by vocabulary: SOURCE or INFERRED only in the table, never DYN, FW-MEMORY, or UNVERIFIED.
  For OPEN rows confirmed_by is shown as — (none).
