# Spot-check — Batch 40 (Stream A Phase 2)

- Work file: `~/workspace/overnight/stream-A/work/batch40-merge-ready.md` (UNVERIFIED proposal, not a result).
- Method: re-derived from already-fetched local source only (`~/workspace/overnight/stream-A/greps/recheck_complete_tree_grep_20261101.txt` §G4, `~/workspace/overnight/stream-A/corpus/java/`). No GitHub connector fetch was needed; no 429 encountered. No edit was made to the work file.
- Phase 1 label changes in this batch: NONE (the OPEN-closing pass changed 0 labels — batch 40 had 0 OPEN rows; the grep-flip re-check re-verified row 3 with no label change). Rows checked = sample rows 1, 6, 11, 16, 21, 26, 31, 36 + row 3, the batch's sole UNREACHABLE row and the subject of the Phase 1 re-check (included explicitly although it did not change label).
- Build / sampler / C1: not run (not this task).

## Per-row verdicts

| Row | Method | Table label | Verdict | Printed evidence |
|---|---|---|---|---|
| 1 | TorrentSessionImpl.loadSettings | REACHABLE / SOURCE | PASS | TorrentSessionImpl.java:867 `SessionParams params = loadSettings();` inside start() (:862–908) — exact; def at :1192 — exact. |
| 3 | TorrentSessionImpl.mergeTrackersAndSeeds | UNREACHABLE / SOURCE (branch_never_taken) | PASS (Phase 1 re-check holds) | Private method, so the within-file proof is complete: sole call at TorrentSessionImpl.java:556 inside `if (false)` at :554 (TODO at :553, same bug link), definition at :570–588 — all exact in the corpus copy. Recheck grep §G4 independently shows only the :556 call and the :570 definition, no other mention. Its callees (batch 39 rows 3–4) are UNREACHABLE for the same reason, as the row states. |
| 6 | TorrentSessionImpl.onAfterStart | REACHABLE / INFERRED | PASS | Trigger chain printed: TorrentEngine.doStart :259 `session.start()`; TorrentSessionImpl.start :907 `super.start(params)`; onAfterStart at :991–1013 — all exact. Library dispatch from super.start to onAfterStart is unprinted, so INFERRED is correct. |
| 11 | TorrentSessionImpl.operationNotAllowed | REACHABLE / SOURCE | PASS | TorrentSessionImpl.java:398 (restoreTorrents guard), :1455 (runNextLoadTorrentTask guard), :260 (fetchMagnet guard) — all confirmed. (Row's further sites :330, :379 not re-checked, not needed.) |
| 16 | TorrentSessionImpl.removeListener | REACHABLE / SOURCE | PASS | TorrentEngine.java:312 `session.removeListener(listener)` — exact, plus :453 and :616 as the row states; TorrentSessionImpl.java:1036–1037 removeListener calls in onBeforeStop — exact. |
| 21 | TorrentSessionImpl.resumeAll | REACHABLE / SOURCE | PASS | TorrentEngine.java:323 `session.resumeAll()` in rescheduleTorrents — exact. |
| 26 | TorrentSessionImpl.setAutoManaged | REACHABLE / SOURCE | PASS | TorrentEngine.java:1579 `session.setAutoManaged(pref.autoManage())` in the pref_key_auto_manage branch (:1578–1579) — exact. |
| 31 | TorrentSessionImpl.setSettings(SessionSettings) | REACHABLE / SOURCE | PASS | TorrentEngine session.setSettings sites confirmed at :1105 and :1476 (row lists further sites :1481–1653 etc., spot-checked by pattern, not line-by-line); def TorrentSessionImpl.java:202 delegates to the 2-arg overload with keepPort=true — exact. One confirmed caller suffices for the label. |
| 36 | TorrentSessionImpl$1.<init> | REACHABLE / INFERRED | PASS | Anonymous TorrentEngineListener field initialiser at TorrentSessionImpl.java:1053–1059 (`torrentTaskListener`) — exact; TorrentSessionImpl is constructed by TorrentEngine at :136 — exact. Anonymous-class numbering is inferred from source order (first anonymous class in the file) and the row itself flags that the merger must confirm it against bytecode — that caveat is preserved, not resolved, here. |

## Totals

- Rows checked: 9. **PASS: 9. FAIL: 0.**
- Proposed corrections: none.
