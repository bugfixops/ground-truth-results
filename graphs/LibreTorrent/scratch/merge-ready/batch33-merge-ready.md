**PHASE 2 FIX 2026-11-01 (coordinator): citation/wording/column corrections from the Phase 2 spot-check applied to this file; labels and counts unchanged (3900/575/257 global totals verified after the fix). Backups in ~/workspace/overnight/stream-A/backup-pre-phase2fix/.**

## Revision note — Stream A Phase 1c (APPLY DECISIONS), 2026-11-01 (UNVERIFIED, no label changes)

Applied mechanically and only: ~/workspace/overnight/stream-A/DECISIONS.md (Muse's own decisions, for user/Yang review, never Yang's). Counts before (main table, last occurrence per row, 40 rows): 30 REACHABLE proposed / 0 UNREACHABLE proposed / 10 OPEN. Counts after: 30 / 0 / 10 — unchanged. Rows flipped: NONE. Build: not run. C1: not run. Nothing pushed. No GitHub connector fetch was made in this pass; no 429 encountered.
D1: verified — every OPEN row already has confirmed_by —, so no cosmetic change was needed.
D2: anchor convention adopted — the 30 REACHABLE proposed rows stand and do NOT revert under a strict launcher-entry rule (the sole D2 revert is batch 99, not this batch). D11: <clinit> rows 9, 18, 19 stand.
Rows deliberately left OPEN, with decision ID: 8 (D7 toString — itself the host for batch 34 row 3; it has no independent conditional host and does not flip), 16 (D7 toString — conditional host batch 34 row 16 does not flip), 24 (no DECISIONS flip order; P2 — file's conditional notes no printed sort of a FileTree-typed list exists), 26 (no DECISIONS flip order; P2 — no printed contains/indexOf/DiffUtil site on a FileTree-typed list), 30 (no DECISIONS flip order; P2), 31 (no DECISIONS flip order; P2), 36 (no DECISIONS flip order; P2), 38 (no DECISIONS flip order; P2), 39 (no DECISIONS flip order; P2), 40 (no DECISIONS flip order; P2).
The UNREACHABLE-on-tree-grep conditional for rows 24, 26, 30, 31, 36, 38, 39, 40 (and rows 8/16 via their hosts) is rejected by P2/D7: app-tree zero alone never flips a row to UNREACHABLE, and neither toString host flips under D7.

**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

**REVISION 2026-11-01 (OPEN-closing round 2): 0 rows flipped. All 10 OPEN rows re-checked against the full 252-file app-Java tree (`~/workspace/ruleF-src/`) plus the hashCode/toString/compare-ctor grep families in `~/workspace/libretorrent-grep/`; no independent printed caller was found for any OPEN row, and no row was flipped to UNREACHABLE (UNREACHABLE-on-tree-grep-absence is an undecided project-wide rule — see CONDITIONAL table). Counts unchanged 30/0/10. Round-1 flip (row 29) re-checked, NOT reverted — no fresh contradictory evidence. Build: not run. C1: not run. UNVERIFIED, nothing merged.**

**REVISION 2026-11-01 (OPEN-closing pass): 1 row flipped OPEN -> REACHABLE on freshly printed source (see table row 29 and "Printed source added 2026-11-01" below). Counts changed 29/0/11 -> 30/0/10. No row flipped to UNREACHABLE (no saved full-repo grep was run in this pass). Build: not run. C1: not run. UNVERIFIED, nothing merged. The local-reprint caveat for AddTorrentViewModel/DetailTorrentViewModel/TorrentContentFileTree caller lines is now CLOSED (all cited lines confirmed on fresh fetches in this pass).**

# LibreTorrent batch 33 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
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

## Printed source added 2026-11-01 (OPEN-closing round 2)

No new GitHub connector fetch was made in this round (no new file was missing
locally); all checking was over already-fetched files: `~/workspace/ruleF-src/`
(252 app Java files), `~/workspace/b323334-openclose-src/` (round-1 fresh
prints), and `~/workspace/libretorrent-grep/` (hashcode, tostring, compare-ctor
families, which already triaged these exact rows). Saved round-2 greps in
`~/workspace/b323334-openclose2-src/`: `grep-setters-getters.txt`,
`grep-equals-setters-parcel.txt`, `grep-classnames-methods.txt`.
Findings, per OPEN row (all "zero" statements are app-Java only; they exclude
`res` XML, generated code, and framework dispatch, so none flips a row to
UNREACHABLE in this round):
- Row 8 BencodeFileTree.toString: no external caller; its body calls
  FileTree.toString (batch 34 row 3), it is not called by it.
- Row 16 FilePriority.toString: only conditional site is inside the OPEN
  TorrentContentFileTree.toString (batch 34 row 16, concat `", priority=" +
  priority` at TorrentContentFileTree.java:179) — dependency rule, flips
  only with that host (see CONDITIONAL table).
- Row 24 FileTree.compareTo: the only `Collections.sort` sites in the tree
  are BencodeFileTreeUtils :55 and TorrentContentFileTreeUtils :55, both
  sorting `List<BencodeFileItem>` (dispatch to BencodeFileItem.compareTo,
  batch 32 row 12), not FileTree; no `List<FileTree>`/`List<BencodeFileTree>`/
  `List<TorrentContentFileTree>` sort, no `.sorted()` on a tree list, and
  neither tree subclass overrides compareTo (compare-ctor family).
- Row 26 FileTree.equals: no receiver-typed `.equals` caller, no
  `List<FileTree>` contains/indexOf site in the tree.
- Rows 30/31 FileTree.getChildrenIndexes/getChildrenName: the only hits in
  the whole tree are their own definitions (FileTree.java:100/:95); no caller.
  Note the contrast that keeps rows 29/33 REACHABLE: getChildrenCount is
  called from BencodeFileTree.doSelect, and getName from FileTree.addChild —
  printed internal callers from REACHABLE methods. Rows 30/31 have no such
  internal caller (getChildrenIndexes itself calls child.getIndex, not vice
  versa; getChildrenName returns `children.keySet()` directly).
- Row 36 FileTree.getType: no app-Java caller on a FileTree receiver; the
  `.getType()` hits in the tree are FilePriority.getType, FileManagerNode,
  Intent, and libtorrent node types. FileTree.isFile reads the `isLeaf`
  field directly, not getType. This is the "ctor sets fields directly" case
  in reverse: the ctor sets `isLeaf = (type == FILE)`, and nothing reads it
  back through getType in printed app Java.
- Rows 38/39/40 FileTree.setIndex/setName/setParent: zero app-Java caller on
  a FileTree receiver in `grep-setters-getters.txt` (the `setName` hits are
  `mutableParams.setName`, `state.setName`, and other classes' setters; the
  `setParent`/`setIndex` hits are none for FileTree). All three fields are
  set directly by the FileTree ctors (index, name, parent), satisfying the
  task's key fact — a ctor assignment alone does not flip a getter, and here
  the setters themselves have no printed caller. FileTree.setType is batch 34
  row 1, not a batch-33 row; it was checked in the same greps with the same
  zero result.
- Round-1 flip re-checked: row 29 getChildrenCount via BencodeFileTree.doSelect
  :75 is still present in the 252-file tree; nothing contradicts it.

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
| 1 | BencodeFileTree.<init>(String,long,int) | REACHABLE proposed | SOURCE | BencodeFileTreeUtils.java:48 root `new BencodeFileTree(FileTree.ROOT, 0L, FileNode.Type.DIR)` — fresh fetch. |
| 2 | BencodeFileTree.<init>(String,long,int,BencodeFileTree) | REACHABLE proposed | SOURCE | BencodeFileTreeUtils.java makeObject dir branch: `new BencodeFileTree(name, 0L, FileNode.Type.DIR, parent)` — fresh fetch :125. |
| 3 | BencodeFileTree.doSelect | REACHABLE proposed | SOURCE | Private, called by select BencodeFileTree.java:61 (select itself REACHABLE, row 6). |
| 4 | BencodeFileTree.isSelected | REACHABLE proposed | SOURCE | AddTorrentViewModel.java getSelectedFileIndexes: file.isSelected() (local reprint). |
| 5 | BencodeFileTree.onChildSelectChange | REACHABLE proposed | SOURCE | Private, called by doSelect BencodeFileTree.java (doSelect REACHABLE, row 3). |
| 6 | BencodeFileTree.select | REACHABLE proposed | SOURCE | AddTorrentViewModel.java makeFileTree: fileTree.select(true, false) (local reprint). |
| 7 | BencodeFileTree.selectedFileSize | REACHABLE proposed | SOURCE | AddTorrentViewModel.java:553 fileTree.selectedFileSize() (local reprint). |
| 8 | BencodeFileTree.toString | UNREACHABLE | INFERRED | BencodeFileTree.java:125; no printed caller (it calls FileTree.toString, not vice versa). Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] |
| 9 | FileNode$Type.<clinit> | REACHABLE proposed | INFERRED | FileNode.Type constants used in BencodeFileTreeUtils.java:48 and FileTree construction; enum/class loaded on the AddTorrent route — fresh fetch. |
| 10 | FilePriority.<init>(Priority) | REACHABLE proposed | SOURCE | DetailTorrentViewModel.java:549 `new FilePriority(p)` (local reprint). |
| 11 | FilePriority.<init>(Type) | REACHABLE proposed | SOURCE | DetailTorrentViewModel.java:323 `new FilePriority(FilePriority.Type.MIXED)`; TorrentContentFileTree.java:28 field initialiser (local reprints). |
| 12 | FilePriority.equals | REACHABLE proposed | SOURCE | DetailTorrentViewModel.java getFilesPriority loop: `!randomPriority.equals(priority)` (local reprint). |
| 13 | FilePriority.getPriority | REACHABLE proposed | SOURCE | DetailTorrentViewModel.java:420 `file.getFilePriority().getPriority()` (local reprint). |
| 14 | FilePriority.getType | REACHABLE proposed | SOURCE | TorrentContentFileTree.java changePriority/onChildSelectChange/nonIgnoreFileSize/getAvailability call .getType() on REACHABLE methods (local reprint). |
| 15 | FilePriority.priorityFrom | REACHABLE proposed | SOURCE | Private static, called by the Type ctor FilePriority.java:42 (ctor REACHABLE, row 11). |
| 16 | FilePriority.toString | UNREACHABLE | INFERRED | FilePriority.java:107; no printed caller. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] |
| 17 | FilePriority.typeFrom | REACHABLE proposed | SOURCE | Static, called by the Priority ctor FilePriority.java:36 (ctor REACHABLE, row 10). |
| 18 | FilePriority$Type.<clinit> | REACHABLE proposed | INFERRED | Enum constants used at DetailTorrentViewModel.java:323 and TorrentContentFileTree.java:28 (local reprints). |
| 19 | FileTree.<clinit> | REACHABLE proposed | INFERRED | Static ROOT/PARENT_DIR FileTree.java:40-42 — fresh fetch; class loaded via BencodeFileTree/TorrentContentFileTree construction. |
| 20 | FileTree.<init>(int,String,long,int,FileTree) | REACHABLE proposed | SOURCE | BencodeFileTree.java:40 super call from the REACHABLE 5-arg BencodeFileTree ctor (batch 32 row 40). |
| 21 | FileTree.<init>(String,long,int) | REACHABLE proposed | SOURCE | BencodeFileTree.java:37 super call (ctor declared :35) from the REACHABLE 3-arg BencodeFileTree ctor (row 1). |
| 22 | FileTree.<init>(String,long,int,FileTree) | REACHABLE proposed | SOURCE | BencodeFileTree.java:45 super call from the REACHABLE 4-arg BencodeFileTree ctor (row 2). |
| 23 | FileTree.addChild | REACHABLE proposed | SOURCE | BencodeFileTreeUtils.java:106 parentTree.addChild(leaf) — fresh fetch. |
| 24 | FileTree.compareTo | UNREACHABLE no_trigger_in_app | INFERRED | A1 2026-11-01 (merger direct, helper A1-R5-a evidence cross-checked): nearby Collections.sort sorts BencodeFileItem lists (BencodeFileTreeUtils.java:46-55, filesCopy is List<BencodeFileItem>, invoking BencodeFileItem.compareTo at BencodeFileItem.java:112-114), not FileTree lists; no direct compareTo call on a FileTree receiver. auto_calls.json: only compareTo dst in graph is FileManagerNode.compareTo (different class). Def FileTree.java:187-190. FileTree.java:187 — fresh fetch; no printed sort/comparison of FileTree objects (BencodeFileTreeUtils sorts BencodeFileItem, not FileTree). |
| 25 | FileTree.contains | REACHABLE proposed | SOURCE | BencodeFileTreeUtils.java:100 parentTree.contains(nodes[i]) — fresh fetch. |
| 26 | FileTree.equals | UNREACHABLE no_trigger_in_app | INFERRED | A1 2026-11-01 (merger direct, helper A1-R5-a evidence cross-checked): FileTree.contains(String) at FileTree.java:80-83 is children.containsKey(name), a String-key map lookup, not a FileTree equals call; no call site, set/map membership, or contains/remove on FileTree objects. auto_calls.json: 0 hits. Def FileTree.java:193-207. FileTree.java:193 — fresh fetch; no printed caller. |
| 27 | FileTree.getChild | REACHABLE proposed | SOURCE | BencodeFileTreeUtils.java:109 parentTree.getChild(nodes[i]) — fresh fetch; AddTorrentViewModel.java:426 curDir.getChild(name) (local reprint). |
| 28 | FileTree.getChildren | REACHABLE proposed | SOURCE | AddTorrentViewModel.java:420 curDir.getChildren() (local reprint). |
| 29 | FileTree.getChildrenCount | REACHABLE proposed | SOURCE | **CHANGED 2026-11-01 (was OPEN).** BencodeFileTree.doSelect:75 `if (getChildrenCount()!= 0)` — fresh fetch, SHA `c732b4b9…`; doSelect is REACHABLE (row 3, called by REACHABLE select at BencodeFileTree:63). Same internal-caller rule as row 33 (getName via addChild) and batch 34 row 2 (size via selectedFileSize/nonIgnoreFileSize). |
| 30 | FileTree.getChildrenIndexes | UNREACHABLE no_trigger_in_app | INFERRED | A1 2026-11-01 (merger direct, helper A1-R5-a evidence cross-checked): definition only; callers use getChildren() (AddTorrentViewModel.java:420; DetailTorrentViewModel.java:240) + per-child getIndex(), never this aggregate. auto_calls.json: 0 hits. Def FileTree.java:100-108. FileTree.java:100 — fresh fetch; no printed caller. |
| 31 | FileTree.getChildrenName | UNREACHABLE no_trigger_in_app | INFERRED | A1 2026-11-01 (merger direct, helper A1-R5-a evidence cross-checked): definition only; same getChildren()-based pattern. auto_calls.json: 0 hits. Def FileTree.java:95-98. FileTree.java:95 — fresh fetch; no printed caller. |
| 32 | FileTree.getIndex | REACHABLE proposed | SOURCE | AddTorrentViewModel.java getSelectedFileIndexes: file.getIndex() for BencodeFileTree leaves (local reprint). |
| 33 | FileTree.getName | REACHABLE proposed | SOURCE | FileTree.java:75 addChild uses node.getName() — fresh fetch; addChild is REACHABLE (row 23). |
| 34 | FileTree.getParent | REACHABLE proposed | SOURCE | AddTorrentViewModel.java:418 curDir.getParent(); DetailTorrentViewModel.java getChildren parent check (local reprints). |
| 35 | FileTree.getPath | REACHABLE proposed | SOURCE | AddTorrentViewModel.java getFilePath: node.getPath() (local reprint); confirmed fresh in this pass via DetailTorrentViewModel.java:268 `String relativePath = node.getPath();` (SHA `6e4ef82f…`). |
| 36 | FileTree.getType | UNREACHABLE no_trigger_in_app | INFERRED | A1 2026-11-01 (merger direct, helper A1-R5-a evidence cross-checked): every other getType() hit is another class (feedparser Enclosure/Content, FilePriority.getType, FileManagerNode.getType, Intent.getType); in-tree code needing the file/dir distinction on a FileTree reads isFile() (FileTree.java:110-113, return isLeaf). auto_calls.json: 0 hits (all getType dst hits are FilePriority/FileManagerNode/feedparser). Def FileTree.java:153-156. FileTree.java:153 — fresh fetch; no printed caller (FileTree.isFile reads the type field directly). |
| 37 | FileTree.isFile | REACHABLE proposed | SOURCE | BencodeFileTreeUtils.java:111 nextParent.isFile() — fresh fetch. |
| 38 | FileTree.setIndex | UNREACHABLE no_trigger_in_app | INFERRED | A1 2026-11-01 (merger direct, helper A1-R5-a evidence cross-checked): definitions only (this + BencodeFileItem.setIndex); all FileTree ctors set the field directly (FileTree.java:63-68). auto_calls.json: no dst setIndex hit anywhere. Def FileTree.java:142-145. FileTree.java:142 — fresh fetch; no printed caller (ctors set the field directly). |
| 39 | FileTree.setName | UNREACHABLE no_trigger_in_app | INFERRED | A1 2026-11-01 (merger direct, helper A1-R5-a evidence cross-checked): TorrentSessionImpl.java:484,1643 p.setName hits are on a libtorrent add_torrent_params object, not FileTree; remaining setName hits are MutableParams/AddTagState/Thread/FileManagerNode setters; ctors set name directly (FileTree.java:63-68). auto_calls.json: 0 hits. Def FileTree.java:131-134. FileTree.java:131 — fresh fetch; no printed caller. |
| 40 | FileTree.setParent | UNREACHABLE no_trigger_in_app | INFERRED | A1 2026-11-01 (merger direct, helper A1-R5-a evidence cross-checked): definition only; ctors set parent directly (FileTree.java:63-68); no re-parenting after construction. auto_calls.json: no dst setParent hit anywhere. Def FileTree.java:125-128. FileTree.java:125 — fresh fetch; no printed caller (ctors set the field directly). |

## Counts — mechanically verified

- REACHABLE proposed: 30 (rows 1-7, 9-15, 17-23, 25, 27-29, 32-35, 37)
- UNREACHABLE proposed: 0
- OPEN: 10 (rows 8, 16, 24, 26, 30, 31, 36, 38, 39, 40)
- Total: 40 rows, sequence 1–40 intact in plan order.
- Verified for merge: 0 / 40.

## Gaps the merger must close before merging

1. Saved full-repo grep for the 10 OPEN rows. Any hit flips that row to REACHABLE.
2. CLOSED 2026-11-01: AddTorrentViewModel.java, DetailTorrentViewModel.java and
   TorrentContentFileTree.java are now freshly fetched (see addendum); every cited line was
   confirmed (AddTorrentViewModel:384 select, :408/:417-418 parent, :420 getChildren, :426/:437
   getChild, :460-461 isSelected/getIndex, :553 selectedFileSize; DetailTorrentViewModel:237-238,
   :294-323 getFilesPriority/FilePriority, :420, :549, :551, :560, :582, :589). No local-reprint
   caller caveat remains for this batch.
3. Printed launcher-to-AddTorrent/Detail step; build/sampler/C1 on a full checkout; main-agent
   spot-check 1 in 5; py_compile at merge. None run or claimed here.
4. No fresh HTTP 429 was hit in this session.

## CONDITIONAL flip tables — round 2 (NOT decided, NOT flipped)

Nothing in this section changes a label. It states exactly what flips if the
merger/user adopts the named option, so one project-wide rule can be applied
uniformly.

- **UNREACHABLE-on-tree-grep-absence (undecided).** IF the merger rules that
  zero hits in a saved 252-file app-Java grep suffices for
  `no_trigger_in_app`, THEN rows 24, 26, 30, 31, 36, 38, 39, 40 flip to
  UNREACHABLE `no_trigger_in_app` (each on the zero-caller evidence above),
  while rows 8 and 16 flip to UNREACHABLE only if their hosts are also ruled
  UNREACHABLE: row 16's host is batch 34 row 16; row 8 has no host of its
  own (it is itself a host for batch 34 row 3 — see below), so row 8 flips
  to UNREACHABLE on its own zero-caller evidence under this option, and
  batch 34 row 3 then depends solely on its remaining host, batch 34 row 16.
- **toString dependency (conditional, no new rule needed).** Row 16
  FilePriority.toString flips to REACHABLE SOURCE together with batch 34
  row 16 TorrentContentFileTree.toString (concat at
  TorrentContentFileTree.java:179, field type verified FilePriority at :28).
  Row 8 BencodeFileTree.toString flipping to REACHABLE would flip batch 34
  row 3 FileTree.toString together with it (`super.toString()` at
  BencodeFileTree.java:128); row 8 itself has no independent conditional
  host and flips only on a direct log/concat caller found later.
- **compareTo/equals framework rule (undecided, no effect here).** Even IF
  sort/equals dispatch through a generic collection is ruled a trigger, row
  24 does not flip without a printed sort of a FileTree-typed list (none
  exists), and row 26 does not flip without a printed contains/indexOf/
  DiffUtil site on a FileTree-typed list (none exists).

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
