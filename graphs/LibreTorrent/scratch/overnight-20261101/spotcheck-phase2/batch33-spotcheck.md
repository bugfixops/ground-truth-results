# Spot-check — Batch 33 (Stream A Phase 2)

- Work file: `~/workspace/overnight/stream-A/work/batch33-merge-ready.md` (UNVERIFIED proposal, not a result).
- Method: re-derived from already-fetched local source only (`~/workspace/b323334-openclose-src/`). No GitHub connector fetch was needed; no 429 encountered. No edit was made to the work file.
- Phase 1 label changes in this batch: row 29 flipped OPEN → REACHABLE in the 2026-11-01 OPEN-closing pass (counts 29/0/11 → 30/0/10); OPEN-closing round 2 and Phase 1c flips: NONE. Rows checked = sample rows 1, 6, 11, 16, 21, 26, 31, 36 + Phase 1 flip 29.
- Build / sampler / C1: not run (not this task).

## Per-row verdicts

| Row | Method | Table label | Verdict | Printed evidence |
|---|---|---|---|---|
| 1 | BencodeFileTree.<init>(String,long,int) | REACHABLE / SOURCE | PASS | BencodeFileTreeUtils.java:48 `BencodeFileTree root = new BencodeFileTree(FileTree.ROOT, 0L, FileNode.Type.DIR)` — exactly as cited. |
| 6 | BencodeFileTree.select | REACHABLE / SOURCE | PASS | AddTorrentViewModel.java:384 `fileTree.select(true, false)` inside makeFileTree() (:368) — exactly as cited. |
| 11 | FilePriority.<init>(Type) | REACHABLE / SOURCE | PASS | DetailTorrentViewModel.java:323 `return new FilePriority(FilePriority.Type.MIXED)` — exactly as cited. |
| 16 | FilePriority.toString | OPEN | PASS | Def FilePriority.java:107 (`public String toString()`) confirmed. No printed caller; OPEN stands. |
| 21 | FileTree.<init>(String,long,int) | REACHABLE / SOURCE | PASS (label) — citation nit, see below | The 3-arg BencodeFileTree ctor (row 1, REACHABLE) calls `super(name, size, type)` into this FileTree ctor. Citation nit: the ctor declaration is at BencodeFileTree.java:35, but the `super(...)` call itself is at **:37**, not :35 as the row states. The call and its target are unambiguous, so the label is correct. |
| 26 | FileTree.equals | OPEN | PASS | Def FileTree.java:193 (`public boolean equals(@Nullable Object o)`) confirmed. No printed caller; OPEN stands. |
| 29 | FileTree.getChildrenCount | REACHABLE / SOURCE | PASS (Phase 1 flip holds) | BencodeFileTree.java:75 `if (getChildrenCount() != 0)` inside doSelect() — exactly as cited. doSelect is REACHABLE: called by REACHABLE select() at BencodeFileTree.java:63 (`doSelect(check, true, forceUpdateParent)`; select at :61–63), and row 6's route reaches select. Same internal-caller rule as the row cites. |
| 31 | FileTree.getChildrenName | OPEN | PASS | Def FileTree.java:95 (`public Set<String> getChildrenName()`) confirmed. No printed caller; OPEN stands. |
| 36 | FileTree.getType | OPEN | PASS | Def FileTree.java:153 (`public int getType()`) confirmed. No printed caller (FileTree.isFile reads the type field directly, as the row states); OPEN stands. |

## Totals

- Rows checked: 9. **PASS: 9. FAIL: 0.**
- Proposed corrections (citation only, no label change): row 21 — change "BencodeFileTree.java:35 super call" to "BencodeFileTree.java:37 super call (ctor declared :35)".
