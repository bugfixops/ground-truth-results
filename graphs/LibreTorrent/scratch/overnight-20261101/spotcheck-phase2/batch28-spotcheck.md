# LibreTorrent batch 28 — Phase 2 spot-check (UNVERIFIED spot-check, not a merge verdict)

- Source file checked: `~/workspace/overnight/stream-A/work/batch28-merge-ready.md` (UNVERIFIED proposal, not a result).
- Rows checked (8): sample rows 1, 6, 11, 16, 21, 26, 31, 36. Phase 1c made 0 label flips in this batch and the OPEN-closing round notes also made 0 flips, so no additional flipped rows were added to the check set. (The Phase 1c note's D12 rows 2 and 8 and D5b row 31 are noted: row 31 is in the sample and passes below; rows 2 and 8 were not in the check set and were not judged.)
- Evidence base: already-fetched local files only — `~/workspace/b262728-src/` (TorrentInfoProvider, TorrentEngine, TorrentSessionImpl, TorrentDownloadImpl, AdvancedTorrentInfo, AbstractInfoParcel, MagnetInfo, MainActivity) and `~/workspace/ruleF-src/core/model/data/` (super-caller lines). No GitHub connector fetch was made, no 429 encountered, no file was missing.
- Build / sampler / C1: not run (not this task). No edit was made to the merge-ready file.

## Per-row verdicts

| Row | Method | Filed label / confirmed_by | Verdict | Printed evidence (re-derived) |
|---|---|---|---|---|
| 1 | TorrentInfoProvider$1.<init>(TorrentInfoProvider,Consumer,FlowableEmitter,String) | REACHABLE / SOURCE | PASS | Anonymous listener instantiated at TorrentInfoProvider.java:147 in makeInfoFlowable (:130); route via observeInfo :94-95 ← DetailTorrentViewModel.observeTorrentInfo :167-168. Printed instantiation site, hence SOURCE under the file's convention. |
| 6 | TorrentInfoProvider$1.onTorrentStateChanged(String,TorrentStateCode,TorrentStateCode) | REACHABLE / SOURCE | PASS | Override TorrentInfoProvider.java:149-161; registration (engine.addListener) at :214 region; dispatch TorrentDownloadImpl.java:224-230 (STATE_CHANGED case → onTorrentStateChanged). |
| 11 | TorrentInfoProvider$2.onTorrentPaused(String) | REACHABLE / SOURCE | PASS | Override TorrentInfoProvider.java:262-266; registration (engine.addListener) at :293 region; dispatch TorrentDownloadImpl.java:237-240 (TORRENT_PAUSED case → onTorrentPaused). |
| 16 | TorrentInfoProvider$4.<init>(TorrentInfoProvider,AtomicReference,FlowableEmitter) | REACHABLE / SOURCE | PASS | Anonymous listener instantiated at TorrentInfoProvider.java:478 in makeSessionStatsFlowable (:474); route via observeSessionStats :126-127 ← MainActivity.subscribeSessionStats :456-460 (infoProvider.observeSessionStats() at :457). |
| 21 | AbstractInfoParcel.writeToParcel(Parcel,int) | OPEN / — | PASS | Def AbstractInfoParcel.java:52-55. Printed super-callers verified exactly as filed: AdvancedTorrentInfo.java:103, PeerInfo.java:152, SessionStats.java:69, TorrentInfo.java:151, TrackerInfo.java:185 — each inside that subclass's own writeToParcel, all of which are OPEN (no printed parcel site). Dependency rule correctly keeps this OPEN. |
| 26 | AdvancedTorrentInfo.describeContents() | OPEN / — | PASS | Def AdvancedTorrentInfo.java:95-98 (returns 0). No printed marshalling site for this class in the printed tree (no putExtra/getParcelable site naming it); OPEN (not UNREACHABLE) is correct on this evidence. |
| 31 | AdvancedTorrentInfo$1.<init>() | REACHABLE / INFERRED | PASS | Anonymous Creator instantiated only by the static field initializer AdvancedTorrentInfo.java:119-134; executed as part of <clinit> on first printed class use (TorrentEngine.java:846-860, `new AdvancedTorrentInfo(...)` in makeAdvancedInfoSync). Instantiation inside <clinit> only, hence INFERRED, per D5b Treatment A as filed. |
| 36 | MagnetInfo.<init>(String,String,String,List) | REACHABLE / SOURCE | PASS | Def MagnetInfo.java:48-54; called in TorrentSessionImpl.fetchMagnet :439-440 and parseMagnet :450-451, via TorrentEngine.fetchMagnet :415-419, :427-428 (verified in batch 22) and AddTorrentViewModel.java:237. |

## Totals

- PASS: 8 / 8. FAIL: 0.
- Proposed corrections: none.
