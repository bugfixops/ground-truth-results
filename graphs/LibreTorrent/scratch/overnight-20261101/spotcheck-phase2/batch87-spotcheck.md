# LibreTorrent batch 87 — Phase 2 spot-check — UNVERIFIED (spot-check only, not a merge verdict)

- Batch: 87. Work file checked: `~/workspace/overnight/stream-A/work/batch87-merge-ready.md` (UNVERIFIED proposal, not a result).
- Rows checked (9): sample rows 1, 6, 11, 16, 21, 26, 31, 36, plus row 22, the one verdict changed in the file (OPEN → REACHABLE SOURCE on fresh evidence).
- Method: re-derived from already-fetched source on disk (`~/workspace/b8788-src/`); no GitHub connector fetch was needed, no 429 hit, no file missing.
- No edit was made to the merge-ready file. No push. Build/sampler/C1: not run (not this task).
- Strict-entry caveat: no launcher → MainActivity step was freshly printed in this batch's pass; under a strict printed-launcher rule all REACHABLE rows would revert to OPEN. That convention is undecided and NOT decided here.

## Per-row verdicts

| Row | Method | Filed label / confirmed_by | Verdict | Printed evidence (file:line, local copy) |
|---|---|---|---|---|
| 1 | DetailTorrentFragment.addTrackersDialog | REACHABLE / SOURCE | PASS | Caller DetailTorrentFragment.java:470 (onOptionsItemSelected); def :518-533. |
| 6 | DetailTorrentFragment.getTorrentId | REACHABLE / SOURCE | PASS | Caller DetailTorrentActivity.java:102 (subscribeTorrentDeleted lambda `detailTorrentFragment.getTorrentId()`); def DetailTorrentFragment.java:124-127. |
| 11 | DetailTorrentFragment.lambda$new$11 | REACHABLE / INFERRED | PASS | saveTorrentFileChoose ActivityResultLauncher callback DetailTorrentFragment.java:795-820 (→ saveErrorTorrentFileDialog / viewModel.copyTorrentFile); ActivityResult dispatch unprinted → INFERRED correct. Numbering by source order, not bytecode-verified. |
| 16 | DetailTorrentFragment.lambda$subscribeMsgViewModel$7 | REACHABLE / INFERRED | PASS | Subscribe lambda DetailTorrentFragment.java:278-287 (→ setTabLayoutColor); Rx dispatch unprinted → INFERRED correct. |
| 21 | DetailTorrentFragment.lambda$subscribeTorrentInfo$6 | REACHABLE / INFERRED | PASS | Advanced-info error lambda DetailTorrentFragment.java:275 (log only); Rx dispatch unprinted → INFERRED correct. |
| 22 | DetailTorrentFragment.newInstance | REACHABLE / SOURCE | PASS | Printed direct call MainActivity.java:656 `DetailTorrentFragment.newInstance(id)` in the two-pane branch of showDetailTorrent (subscribed :440), then fragment replace :665-668; def DetailTorrentFragment.java:115-121. The OPEN → REACHABLE change is supported; the single-pane branch starting DetailTorrentActivity instead does not undo a printed two-pane route. |
| 26 | DetailTorrentFragment.onCreateView | REACHABLE / INFERRED | PASS | Def DetailTorrentFragment.java:148-153 (DataBindingUtil.inflate fragment_detail_torrent); framework lifecycle dispatch unprinted → INFERRED correct. |
| 31 | DetailTorrentFragment.onStop | REACHABLE / INFERRED | PASS | Def DetailTorrentFragment.java:235-240 (disposables.clear()); lifecycle dispatch unprinted → INFERRED correct. |
| 36 | DetailTorrentFragment.setTabLayoutColor | REACHABLE / SOURCE | PASS | Caller DetailTorrentFragment.java:282 (subscribeMsgViewModel lambda); def :381-386 (two-pane early return :382-383; the method still runs). |

## Totals

- PASS: 9 / 9. FAIL: 0 / 9.

## Proposed corrections

- None. No row label or confirmed_by needs changing on the evidence checked.
