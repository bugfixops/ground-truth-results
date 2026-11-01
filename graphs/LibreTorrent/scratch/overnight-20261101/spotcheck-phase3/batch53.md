# Spot-check — batch 53 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). No work file edited.

## Changed rows (0)

None.

## Sample rows (8)

- 53/1 TorrentDao_Impl.deleteTag — REACHABLE INFERRED — PASS. Interface call TRI.deleteTag L136-138 (db.torrentDao().deleteTag(…)); Room dispatch to _Impl.deleteTag INFERRED (generated class not in upload).
- 53/6 TorrentDao_Impl.getTorrentByIdSingle — REACHABLE INFERRED — PASS. Interface call TRI.getTorrentByIdSingle L76-78; Room dispatch INFERRED.
- 53/11 TorrentDao_Impl$1.bind — REACHABLE INFERRED — PASS. Same as row 10: $1 identity unprinted; cell's final substantive statement is the applied decision: "[APPLIED 2026-11-01 D3a: OPEN → REACHABLE INFERRED per DECISIONS.md]" under the Room $N SET convention (as already applied in batches 51-52); set membership verified in the round-2 note.
- 53/16 TorrentDao_Impl$3.\<init\> — REACHABLE INFERRED — PASS. Same as row 10; [APPLIED D3a] under the Room $N SET convention; set membership verified in the round-2 note.
- 53/21 TorrentDao_Impl$4.createQuery — REACHABLE INFERRED — PASS. Same as row 10; [APPLIED D3a] under the Room $N SET convention; set membership verified in the round-2 note.
- 53/26 TorrentDao_Impl$6.createQuery — REACHABLE INFERRED — PASS. Same as row 25; [APPLIED D3a] under the Room $N SET convention; set membership verified in the round-2 note.
- 53/31 TorrentDao_Impl$8.call — REACHABLE INFERRED — PASS. Same as row 30; [APPLIED D3a] under the Room $N SET convention; set membership verified in the round-2 note.
- 53/36 DefaultFsModule.getDirAvailableBytes — REACHABLE INFERRED — PASS. Definition DFM L91-106; dispatcher: FSFI.getDirAvailableBytes L268-282 calls fsModule.getDirAvailableBytes(dir) L274; facade reachable via TE L1200 (local copy); file-URI branch INFERRED.

Totals: checked 8 (0 changed + 8 sample-only) — PASS 8, FAIL-prose 0, FAIL-label 0.
