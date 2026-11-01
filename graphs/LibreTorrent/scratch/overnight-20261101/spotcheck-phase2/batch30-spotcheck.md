# LibreTorrent batch 30 — Phase 2 spot-check (UNVERIFIED spot-check, not a merge verdict)

- Source file checked: `~/workspace/overnight/stream-A/work/batch30-merge-ready.md` (UNVERIFIED proposal, not a result).
- Rows checked (8): sample rows 1, 6, 11, 16, 21, 26, 31, 36. Phase 1c made 0 label flips in this batch and the OPEN-closing round notes also made 0 flips, so no additional flipped rows were added to the check set. (Sample rows already cover the Phase 1c-named D5b rows 11 and 31 and D11 rows 1 and 36.)
- Evidence base: already-fetched local files only — `~/workspace/ruleF-src/` (TorrentInfo, TorrentStateCode, TrackerInfo, TorrentDownloadImpl, TorrentEngine, TorrentInfoProvider, AddFeedViewModel). No GitHub connector fetch was made, no 429 encountered, no file was missing.
- Build / sampler / C1: not run (not this task). No edit was made to the merge-ready file.

## Per-row verdicts

| Row | Method | Filed label / confirmed_by | Verdict | Printed evidence (re-derived) |
|---|---|---|---|---|
| 1 | TorrentInfo.<clinit> | REACHABLE / INFERRED | PASS | Class init precedes first use: TorrentEngine.makeInfo:779/787 region (`new TorrentInfo(...)`); CREATOR field at TorrentInfo.java:173-183 runs at class init. JVM timing unprinted, hence INFERRED. |
| 6 | TorrentInfo.describeContents | OPEN / — | PASS | Def TorrentInfo.java:145-146 (returns 0); framework marshalling only, no printed parcel site for TorrentInfo in the printed tree. OPEN correct. |
| 11 | TorrentInfo$1.<init> | REACHABLE / INFERRED | PASS | Anonymous Creator at TorrentInfo.java:173-183; field initializer runs at class init on first use (rows 3-4 route, makeInfo above). Same convention as batch 29 row 5, as filed. |
| 16 | TorrentStateCode.fromValue | OPEN / — | PASS | Def TorrentStateCode.java:68-75; only printed caller is TorrentInfo.java:125 (`stateCode = TorrentStateCode.fromValue(source.readInt())`), inside the OPEN Parcel ctor (row 2). Dependency rule correctly keeps this OPEN, standing/falling with row 2. |
| 21 | TrackerInfo.<init>(AnnounceEntry) | REACHABLE / SOURCE | PASS | TorrentDownloadImpl.getTrackerInfoList:904-905 (`states.add(new TrackerInfo(entry));`), reached via TorrentEngine.makeTrackerInfoList ← TorrentInfoProvider.java:363 (`engine.makeTrackerInfoList(id)`); def TrackerInfo.java:67-77. |
| 26 | TrackerInfo.getMessageAndStatus(AnnounceEntry,List) | REACHABLE / SOURCE | PASS | Called from the AnnounceEntry ctor itself, TrackerInfo.java:74 (`var result = getMessageAndStatus(entry, endpoints);`); def :88-145 (private). |
| 31 | TrackerInfo$1.<init> | REACHABLE / INFERRED | PASS | Anonymous Creator at TrackerInfo.java:193-204; field initializer runs at class init on first use (row 21 route). |
| 36 | FeedChannel.<clinit> | REACHABLE / INFERRED | PASS | Class init precedes first use: AddFeedViewModel.applyParams:173 (`new FeedChannel(url, ...)`). JVM timing unprinted, hence INFERRED. |

## Totals

- PASS: 8 / 8. FAIL: 0.
- Proposed corrections: none to any checked row. Note (not a correction): the file's older Counts section says 20/0/20 while the table governs at 21/0/19, as the Phase 1c note itself records; no checked row's label is affected.
