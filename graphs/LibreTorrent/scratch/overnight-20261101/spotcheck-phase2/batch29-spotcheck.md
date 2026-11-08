# LibreTorrent batch 29 — Phase 2 spot-check (UNVERIFIED spot-check, not a merge verdict)

- Source file checked: `~/workspace/overnight/stream-A/work/batch29-merge-ready.md` (UNVERIFIED proposal, not a result).
- Rows checked (11): sample rows 1, 6, 11, 16, 21, 26, 31, 36, PLUS round-notes rows 10 and 13 (round-1 GREPFAMILY flips, preserved in round 2) and row 25 (round-2 flip OPEN → REACHABLE). Phase 1c made 0 label flips in this batch.
- Evidence base: already-fetched local files only — `~/workspace/ruleF-src/` (MagnetInfo, PeerInfo, PeerItem, PeerListAdapter, Priority, PriorityConverter, FilePriority, SessionStats, TorrentDownloadImpl, TorrentEngine, TorrentInfoProvider) and `~/workspace/b232425-src/DetailTorrentViewModel.java` (row 25 chain). No GitHub connector fetch was made, no 429 encountered, no file was missing.
- Build / sampler / C1: not run (not this task). No edit was made to the merge-ready file.

## Per-row verdicts

| Row | Method | Filed label / confirmed_by | Verdict | Printed evidence (re-derived) |
|---|---|---|---|---|
| 1 | MagnetInfo.getUri | OPEN / — | PASS | Def MagnetInfo.java:95-98 (`return uri;`). A ruleF-tree grep for `.getUri()` finds only SafFileSystem (DocumentFile receivers) and TorrentStreamServer/session getUri hits — no MagnetInfo.getUri caller. OPEN (not UNREACHABLE) is correct on printed-subset evidence. |
| 6 | MagnetInfo$1.createFromParcel | OPEN / — | PASS | Def MagnetInfo.java:82-86 (`return new MagnetInfo(source)`); framework dispatch only, no printed unparcel site for a MagnetInfo in the printed tree. OPEN correct. |
| 10 | PeerInfo.<init>(String,String,long,long,double,int,int,int,int,int) | REACHABLE / SOURCE | PASS (round-1 flip preserved) | Def PeerInfo.java:72-91 (10-arg ctor). Printed construction via super-call: PeerItem.java:30 (`super(state.ip, state.client, state.totalDownload, state.totalUpload, state.relevance, state.connectionType, state.port, state.progress, state.downSpeed, state.upSpeed)` — 10 args). The GREPFAMILY flip is verified; the prior "no 10-arg construction" claim missed the super-call form, as the file notes. |
| 11 | PeerInfo.<init>(AdvancedPeerInfo,TorrentStatus) | REACHABLE / SOURCE | PASS | TorrentDownloadImpl.java:924 (`PeerInfo state = new PeerInfo(peer, status);` inside getPeerInfoList), reached via TorrentEngine.makePeerInfoList:872-881 and TorrentInfoProvider.java:396, :410. |
| 13 | PeerInfo.compareTo | REACHABLE / INFERRED | PASS (round-1 flip preserved) | Def PeerInfo.java:183-185 (`ip.compareTo(...)`); PeerListAdapter.java:80 `Collections.sort(list)` over a PeerItem list; PeerItem extends PeerInfo and does not override compareTo, so sort dispatches to PeerInfo.compareTo. Dispatch via sort is unprinted-library dispatch, hence INFERRED. |
| 16 | PeerInfo.getConnectionType(AdvancedPeerInfo) | REACHABLE / SOURCE | PASS | Called from the 2-arg ctor itself, PeerInfo.java:65 (`connectionType = getConnectionType(peer);`); def :108-120 (private). |
| 21 | PeerInfo$1.createFromParcel | OPEN / — | PASS | Def PeerInfo.java:170-172; framework dispatch only, no printed unparcel site. OPEN correct. |
| 25 | Priority.fromValue | REACHABLE / SOURCE | PASS (round-2 flip verified) | Direct printed call FilePriority.java:50 (`return Priority.fromValue(priority);`, inside getPriority :48-51); called at DetailTorrentViewModel.java:420 (`file.getFilePriority().getPriority()`, inside getFilePriorities :413-423), called at :505 inside checkParamsChanged :478-520 (BR.prioritiesChanged branch); upstream callback registered in the ViewModel constructor at :112 and triggered by applyPriority :334 (`mutableParams.setPrioritiesChanged(true)`). Def Priority.java:70-78. The round-2 OPEN → REACHABLE flip is verified on this chain. |
| 26 | Priority.value() | REACHABLE / SOURCE | PASS | PriorityConverter.java static initializer :32-39 (`Priority.IGNORE.value()` … `Priority.TOP_PRIORITY.value()`), :64 and :96 (app→lib converts); def Priority.java:65-68. |
| 31 | SessionStats.<init>(Parcel) | OPEN / — | PASS | Def SessionStats.java:48-58 (calls super(source) at :50); only printed caller is its own CREATOR.createFromParcel :82-86, itself OPEN (row 39). Dependency rule correctly keeps this OPEN. |
| 36 | SessionStats.toString | OPEN / — | PASS | Def SessionStats.java:135-147; no printed logging/concatenation caller for a SessionStats value in the printed tree. OPEN (not UNREACHABLE) is correct on this evidence. |

## Totals

- PASS: 11 / 11 (including both round-1 flips, rows 10 and 13, and the round-2 flip, row 25). FAIL: 0.
- Proposed corrections: none. Note (not a correction): the file's table rows 10 and 13 still contain a stale "Stays OPEN" sentence before their GREPFAMILY FLIP sentence, as the Phase 1c note itself records; the Label column (REACHABLE) governs and is verified above.
