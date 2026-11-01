# Spot-check — Batch 32 (Stream A Phase 2)

- Work file: `~/workspace/overnight/stream-A/work/batch32-merge-ready.md` (UNVERIFIED proposal, not a result).
- Method: re-derived from already-fetched local source only (`~/workspace/b323334-openclose-src/`, `~/workspace/overnight/stream-A/corpus/java/`). No GitHub connector fetch was needed; no 429 encountered. No edit was made to the work file.
- Phase 1 label changes in this batch: rows 5 and 29 flipped OPEN → REACHABLE in the 2026-11-01 OPEN-closing pass (counts 12/0/28 → 14/0/26); Phase 1c flips: NONE. Rows checked = sample rows 1, 6, 11, 16, 21, 26, 31, 36 + Phase 1 flips 5, 29 + must-include extras 2, 22, 37.
- Build / sampler / C1: not run (not this task).

## Per-row verdicts

| Row | Method | Table label | Verdict | Printed evidence |
|---|---|---|---|---|
| 1 | Torrent.writeToParcel | OPEN | PASS | Def Torrent.java:142 (`public void writeToParcel(Parcel dest, int flags)`) confirmed. No printed marshalling site for Torrent cited or found; OPEN stands. |
| 2 | Torrent$1.<init> | OPEN | PASS (as recorded) | CREATOR anonymous class at Torrent.java:157 confirmed. No printed invocation. OPEN status is correctly recorded: the Phase 1c note lists this row UNRESOLVED/NOT flipped, and DECISIONS.md's D5b Treatment A list names no batch-32 $1.<init> row. **Not flipped here** — any extension of Treatment A to this row is a merger ruling. |
| 5 | TorrentTagInfo.<init> | REACHABLE / SOURCE | PASS (Phase 1 flip holds) | TorrentRepositoryImpl.java:125, :132, :137 all `new TorrentTagInfo(tag.id, torrentId)` — exactly as cited, three independent construction sites. Def TorrentTagInfo.java:54 (2-arg ctor) confirmed. The strict-entry caveat disclosed in the row (repository entry step not freshly printed) does not change the label under the adopted anchor convention. |
| 6 | TorrentTagInfo.equals | OPEN | PASS | Def TorrentTagInfo.java:63 (`public boolean equals(Object o)`) confirmed. No printed caller; OPEN stands. |
| 11 | BencodeFileItem.<init>(String,int,long) | REACHABLE / SOURCE | PASS | Utils.java:145 `BencodeFileItem file = new BencodeFileItem(storage.filePath(i), i, storage.fileSize(i))` inside getFileList() (:142) — argument types (String, int, long) match the descriptor exactly. Def BencodeFileItem.java:37 confirmed. |
| 16 | BencodeFileItem.getSize | REACHABLE / SOURCE | PASS | BencodeFileTreeUtils.java:102–103 `file.getSize()` inside the buildFileTree loop, exactly as cited. |
| 21 | BencodeFileItem.writeToParcel | OPEN | PASS | Def BencodeFileItem.java:88 confirmed. Only route is via TorrentMetaInfo.writeToParcel, itself OPEN (row 36); OPEN stands. |
| 22 | BencodeFileItem$1.<init> | OPEN | PASS (as recorded) | CREATOR anonymous class at BencodeFileItem.java:95 confirmed. No printed invocation. OPEN correctly recorded per the Phase 1c note (conditional batch-92 class-initialiser reading NOT ordered for this row); **not flipped here**, merger ruling pending. |
| 26 | TorrentMetaInfo.<init>(Parcel) | OPEN | PASS | Def TorrentMetaInfo.java:113 (`public TorrentMetaInfo (Parcel source)`) confirmed. Only caller is its own CREATOR.createFromParcel (:155), not printed as invoked; OPEN stands. |
| 29 | TorrentMetaInfo.<init>(TorrentInfo) | REACHABLE / SOURCE | PASS (Phase 1 flip holds) | TorrentDownloadImpl.java:406 and :1194 `new TorrentMetaInfo(ti)` where `ti` is org.libtorrent4j.TorrentInfo (`TorrentInfo ti = th.torrentFile()` at both sites) — exactly as cited. Def TorrentMetaInfo.java:73 (TorrentInfo ctor) confirmed; distinguished from the byte[] ctor used at TorrentEngine:464 (row 30) as the row states. |
| 31 | TorrentMetaInfo.describeContents | OPEN | PASS | Def TorrentMetaInfo.java:129 confirmed. No printed caller; OPEN stands. |
| 36 | TorrentMetaInfo.writeToParcel | OPEN | PASS | Def TorrentMetaInfo.java:135 confirmed. No printed marshalling site for TorrentMetaInfo; OPEN stands. |
| 37 | TorrentMetaInfo$1.<init> | OPEN | PASS (as recorded) | CREATOR anonymous class at TorrentMetaInfo.java:149 confirmed. No printed invocation. OPEN correctly recorded per the Phase 1c note (same pending merger ruling as row 22); **not flipped here**. |

## Totals

- Rows checked: 13. **PASS: 13. FAIL: 0.**
- Proposed corrections: none. The three $1.<init> rows (2, 22, 37) are verified as correctly recorded OPEN pending a merger ruling on a D5b Treatment A extension — this spot-check neither flips them nor decides that ruling.
