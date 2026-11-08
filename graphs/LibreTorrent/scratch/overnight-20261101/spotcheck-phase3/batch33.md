# Spot-check — batch 33 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json, plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). Row 16 is in both sets; checked once, under Changed. Verdicts D1–D36/R1–R5 are NOT re-decided. No work file edited.

## Changed rows (2)

- 33/8 BencodeFileTree.toString — UNREACHABLE no_trigger_in_app INFERRED — PASS. L1: definition BencodeFileTree.java:125-130 (its super.toString() call is a trigger for 34/3, not for this row); zero outside trigger in the L1 greps; AddTorrentViewModel children BehaviorSubject\<List\<BencodeFileTree\>\> is method/field use only. Work prose is neutral (definition + no printed caller) with Kind present and the Phase 3 note appended. Note: this row's flip is what breaks batch 34 row 3's old "(itself OPEN)" parenthetical — see batch34.md.
- 33/16 FilePriority.toString — UNREACHABLE no_trigger_in_app INFERRED — PASS. L1: definition FilePriority.java:107-114; zero independent outside trigger — follows host 34/16 (body concats priority, TorrentContentFileTree.java:178), which is UNREACHABLE here; TorrentContentFilesAdapter uses item.priority.getType() (enum) and a String `priority` local (:212/:237, NOT a FilePriority — near-miss rejected); DetailTorrentViewModel List\<FilePriority\> is construction only. Work prose is neutral with Kind present and the Phase 3 note appended.

## Sample rows (7 sample-only)

- 33/1 BencodeFileTree.\<init\>(String,long,int) — REACHABLE SOURCE — PASS. BencodeFileTreeUtils.java:48 root `new BencodeFileTree(FileTree.ROOT, 0L, FileNode.Type.DIR)` (fresh fetch).
- 33/6 BencodeFileTree.select — REACHABLE SOURCE — PASS. AddTorrentViewModel.java makeFileTree: fileTree.select(true, false).
- 33/11 FilePriority.\<init\>(Type) — REACHABLE SOURCE — PASS. DetailTorrentViewModel.java:323 `new FilePriority(FilePriority.Type.MIXED)`; TorrentContentFileTree.java:28 field initialiser.
- 33/21 FileTree.\<init\>(String,long,int) — REACHABLE SOURCE — PASS. BencodeFileTree.java:37 super call from the REACHABLE 3-arg BencodeFileTree ctor (row 1).
- 33/26 FileTree.equals — OPEN — PASS. FileTree.java:193 (fresh fetch); no printed caller. OPEN confirmed_by is —, as required.
- 33/31 FileTree.getChildrenName — OPEN — PASS. FileTree.java:95 (fresh fetch); no printed caller. OPEN confirmed_by is —, as required.
- 33/36 FileTree.getType — OPEN — PASS. FileTree.java:153 (fresh fetch); no printed caller (FileTree.isFile reads the type field directly). OPEN confirmed_by is —, as required.

Totals: checked 9 (2 changed + 7 sample-only) — PASS 9, FAIL-prose 0, FAIL-label 0.
