# Batch 53 — Phase 2 spot-check (UNVERIFIED proposal check only; nothing merged, nothing pushed)

- Source file checked: `~/workspace/overnight/stream-A/work/batch53-merge-ready.md`
- Evidence base: already-fetched files only (`~/workspace/b505152-openclose-src/`, `~/workspace/b5354-openclose-src/`).
  No connector fetch was needed; no 429; no missing file.
- Rows checked (13): sample 1, 6, 11, 16, 21, 26, 31, 36 + flipped SET rows 10, 12, 29, 32 + D3c row 4
  (rows 11, 16, 21, 26, 31, 32 are both sample and flipped; task minimum of three flipped SET rows exceeded).
- Batch Counts verified mechanically from the label column: 40 REACHABLE / 0 UNREACHABLE / 0 OPEN — fully closed,
  matching the Phase 1c header (before: 16/0/24).
- Build/sampler/C1: not run (not this task).

## Per-row verdicts

| Row | Label in file | Verdict | Evidence (printed source) |
|-----|---------------|---------|---------------------------|
| 1 `TorrentDao_Impl.deleteTag` | REACHABLE INFERRED | PASS | TorrentRepositoryImpl.java:136-138 (`deleteTag` def :136, `db.torrentDao().deleteTag(...)` :137). Generated dispatch unprinted, so INFERRED is correct. |
| 4 `TorrentDao_Impl.getRequiredConverters` | REACHABLE INFERRED | PASS* | Label matches Phase 1c D3c, same AppDatabase build print as batch 51 row 6. *Conditional on D3c standing. Pre-flip "stays OPEN" sentence remains alongside the [APPLIED D3c] tag — text cleanup only. |
| 6 `TorrentDao_Impl.getTorrentByIdSingle` | REACHABLE INFERRED | PASS | TorrentRepositoryImpl.java:76-78 (def :76, `db.torrentDao().getTorrentByIdSingle(id)` :77). INFERRED correct. |
| 10 `TorrentDao_Impl$1.<init>` | REACHABLE INFERRED | PASS* | SET membership verified: all TorrentDao operations called at DAO-interface level in TorrentRepositoryImpl — add :57, update :62, delete :67, getTorrentById :72, getTorrentByIdSingle :77, observeTorrentById :82, getAllTorrents :87, replaceTags :127, addTag :132, deleteTag :137 (addTags/deleteTagsByTorrentId via the replaceTags transaction body). The five bind adapters ($1-$5) therefore all run; individual $1 identity is not claimed. *Label conditional on D3a (Room $N SET) standing — this spot-check does not decide the SET-vs-STRICT convention. |
| 11 `TorrentDao_Impl$1.bind` | REACHABLE INFERRED | PASS* | Same SET evidence as row 10. *Conditional on D3a. |
| 12 `TorrentDao_Impl$1.createQuery` | REACHABLE INFERRED | PASS* | Same SET evidence as row 10. *Conditional on D3a. |
| 16 `TorrentDao_Impl$3.<init>` | REACHABLE INFERRED | PASS* | Same SET evidence as row 10 (5 bind adapters, all operations called). *Conditional on D3a. |
| 21 `TorrentDao_Impl$4.createQuery` | REACHABLE INFERRED | PASS* | Same SET evidence as row 10. *Conditional on D3a. |
| 26 `TorrentDao_Impl$6.createQuery` | REACHABLE INFERRED | PASS* | Statement set $6 is pinned, not merely set-assigned: deleteTagsByTorrentId is the sole @Query method that is neither a plain select nor an Rx method, called through TorrentDao.replaceTags (repository :127). *Conditional on D3a for the set framing; the pin itself is verified. |
| 29 `TorrentDao_Impl$7.finalize` | REACHABLE INFERRED | PASS* | Callable set $7-$8: both Torrent-returning Rx methods called (getTorrentByIdSingle repository :77, observeTorrentById :82), so the enclosing Callable is a set member; label matches Phase 1c D3b. *Conditional on D3a + D3b standing. |
| 31 `TorrentDao_Impl$8.call` | REACHABLE INFERRED | PASS* | Same Callable-set evidence as row 29. *Conditional on D3a. |
| 32 `TorrentDao_Impl$8.finalize` | REACHABLE INFERRED | PASS* | Same as row 29. *Conditional on D3a + D3b standing. |
| 36 `DefaultFsModule.getDirAvailableBytes` | REACHABLE INFERRED | PASS | FileSystemFacadeImpl.java:268 (def) / :274 `fsModule.getDirAvailableBytes(dir)`; TorrentEngine.java:1200 `fs.getDirAvailableBytes(downloadPath)` — verified in the fresh b5354 TorrentEngine print as well as the cited local copy, so the "(local copy)" caveat no longer weakens the citation. File-URI branch INFERRED, correct. |

## Totals

- PASS: 13, FAIL: 0 (of 13 checked).
- Proposed corrections: none to any label. Text cleanup only: superseded "stays OPEN" sentence in row 4.
- Note for the coordinator: batch 53's SET flips (21 rows) are the harmonisation counterpart to batches 51-52 (already SET);
  the merger must still apply one rule project-wide, but within the D3a decision the flips are mechanically correct and complete
  (Phase 1c list: rows 4, 10-28, 30, 31, 29, 32 — all present with the correct labels in the table).
