# LibreTorrent batch 22 — Phase 2 spot-check (UNVERIFIED spot-check, not a merge verdict)

- Source file checked: `~/workspace/overnight/stream-A/work/batch22-merge-ready.md` (UNVERIFIED proposal, not a result).
- Rows checked (9): sample rows 1, 6, 11, 16, 21, 26, 31, 36, PLUS row 2 (must-include: Phase 1c D5b confirmed_by SOURCE → INFERRED, label REACHABLE unchanged). Phase 1c made 0 label flips in this batch; rows 1, 3, 4 stay OPEN under D5a as filed.
- Evidence base: already-fetched local files only — `~/workspace/overnight/stream-A/corpus/java/` (AddTorrentParams, DownloadsCompletedListener, SessionErrorFilter, TorrentEngine), `~/workspace/b232425-src/` (FeedDownloaderWorker, AddTorrentViewModel). No GitHub connector fetch was made, no 429 encountered, no file was missing.
- Build / sampler / C1: not run (not this task). No edit was made to the merge-ready file.

## Per-row verdicts

| Row | Method | Filed label / confirmed_by | Verdict | Printed evidence (re-derived) |
|---|---|---|---|---|
| 1 | AddTorrentParams.writeToParcel | OPEN / — | PASS | Def AddTorrentParams.java:96-107 only. No printed marshalling site naming AddTorrentParams in the corpus tree (its readParcelable/writeParcelable hits at :83/:102 concern its own fields, Uri/tags). OPEN (not UNREACHABLE) is the correct conservative verdict on this evidence. |
| 2 | AddTorrentParams$1.<init> | REACHABLE / INFERRED | PASS (must-include D5b check) | Anonymous Creator instantiated by the field initializer AddTorrentParams.java:109-119; class constructed in-app at AddTorrentViewModel.java:510 and TorrentEngine.java:1187, so class initialisation (and hence this implicit ctor) runs. INFERRED is correct: the construction site is a CREATOR field initializer, not an app-code call site naming this ctor. Label REACHABLE unchanged, as filed. |
| 6 | DownloadsCompletedListener.lambda$listen$0 | REACHABLE / INFERRED | PASS | Body DownloadsCompletedListener.java:47-85 (Completable.create lambda; listener registered :81, dispose :82-83); subscribed in TorrentEngine.doStart:243-251 (`downloadsCompleted.listen()`). Rx dispatch unprinted, hence INFERRED. |
| 11 | DownloadsCompletedListener$1.onTorrentFinished | REACHABLE / INFERRED | PASS | Def DownloadsCompletedListener.java:66-70; registration :81 → TorrentEngine.addListener:307-309 → session.addListener. Session invocation of the callback is library dispatch, hence INFERRED. |
| 16 | SessionErrorFilter.skip | REACHABLE / SOURCE | PASS | Def SessionErrorFilter.java:30-32; call site TorrentEngine.java:1386 (`errorFilter.skip(errorMsg)` inside engineListener.onSessionError :1385-1389); listener registered TorrentEngine.java:140. |
| 21 | TorrentEngine.addTorrent(Uri,Uri) | REACHABLE / SOURCE | PASS | Def TorrentEngine.java:363-367; internal call site TorrentEngine.java:360 (1-arg addTorrent delegates to it). |
| 26 | TorrentEngine.addTorrents | REACHABLE / SOURCE | PASS | Def TorrentEngine.java:342-356; fresh-closure caller FeedDownloaderWorker.java:211 (`engine.addTorrents(paramsList, true)`). |
| 31 | TorrentEngine.createFetchMagnetSingle | REACHABLE / SOURCE | PASS | Def TorrentEngine.java:431-479 (private); internal call site TorrentEngine.fetchMagnet:422. |
| 36 | TorrentEngine.fetchMagnet | REACHABLE / SOURCE | PASS | Def TorrentEngine.java:415-429 (calls session.fetchMagnet :419, createFetchMagnetSingle :422); call site AddTorrentViewModel.java:237. |

## Totals

- PASS: 9 / 9. FAIL: 0.
- Proposed corrections: none. Row 2's confirmed_by change (SOURCE → INFERRED) is verified correct and the label correctly unchanged.
