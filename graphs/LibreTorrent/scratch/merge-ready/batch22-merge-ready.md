# LibreTorrent batch 22 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED merge-ready part only. NOT verified for merge. NOT pushed. No edit to `graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**

**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push, so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1 check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 22 only, 40 methods, no other batch, no other app, no device replay, no Aegis.
- Source: existing proposal `~/workspace/libretorrent-batch22-proposal.md` (plus its Agent 4 update header: 36/0/4) used as an INPUT / lead list only. Every row below was re-derived in this pass against source freshly fetched from branch `work-2026-10-31` via the GitHub connector, one file at a time with pauses. No verdict was copied without that re-check. Two resolutions CHANGE against the prior proposal on fresh evidence: row 26 `TorrentEngine.addTorrents` moves OPEN → REACHABLE (fresh `FeedDownloaderWorker.java:211`), and rows 27/28/32/33/37/38 are now confirmed against freshly fetched `DetailTorrentViewModel` / `AddTorrentViewModel` / `MainViewModel` call sites, not the local corpus.
- Membership verified first, not guessed: exactly the 40 batch-22 rows in `handoff/LIBRETORRENT_BATCH_PLAN.tsv` (local plan copy `~/workspace/agent27-plan.tsv`, plan blob SHA `0104806dd666c840049b3db52823d4b384fa1c92`), all `TODO_CANDIDATE_REACHABLE`, in plan order. Plan status is a generator candidate, not evidence.
- Printed source freshly fetched in this pass, saved in `~/workspace/b202122-src/`, no fresh HTTP 429 hit, no `search_code` result used as evidence for any row:
  - `org/proninyaroslav/libretorrent/core/model/AddTorrentParams.java` — SHA `7e349c3d…`, 144 lines.
  - `org/proninyaroslav/libretorrent/core/model/DownloadsCompletedListener.java` — SHA `deabede82…`, 88 lines.
  - `org/proninyaroslav/libretorrent/core/model/SessionErrorFilter.java` — SHA `c18996cb…`, 34 lines.
  - `org/proninyaroslav/libretorrent/core/model/TorrentEngine.java` — SHA `17d06efe…`, 1659 lines.
  - `org/proninyaroslav/libretorrent/service/TorrentService.java` — SHA `f0c3cdc4…`, 526 lines.
  - `org/proninyaroslav/libretorrent/service/FeedDownloaderWorker.java` — SHA `f45dda6f…`, 216 lines.
  - `org/proninyaroslav/libretorrent/ui/addtorrent/AddTorrentViewModel.java` — SHA `bec2f6ee…`, 575 lines.
  - `org/proninyaroslav/libretorrent/ui/main/MainViewModel.java` — SHA `73938fbb…`, 190 lines.
  - `org/proninyaroslav/libretorrent/ui/detailtorrent/DetailTorrentViewModel.java` — SHA `6e4ef82f…`, 611 lines.
- `confirmed_by` convention used here, per row (not decided project-wide): SOURCE = a printed app-code line names the method (direct call, construction, or an internal call from a REACHABLE method printed in this pass); INFERRED = unprinted framework/library/Rx/JVM dispatch where the definition plus registration, thread creation, or first use is printed. Under a whole-route INFERRED convention, SOURCE rows whose routes pass through unprinted dispatch would flip to INFERRED; labels are unaffected. This convention is recorded, not decided.

## Counts — mechanically verified

- 40 rows, sequence 1–40 intact, in plan order.
- **REACHABLE proposed: 37 / 40 (SOURCE 29 / INFERRED 8)**
- **UNREACHABLE proposed: 0**
- **OPEN: 3 / 40 (rows 1, 3, 4 — the AddTorrentParams Parcelable trio)**
- **Verified for merge: 0**

## Trunks (fresh prints)

- TorrentService anchor (fresh): `onCreate:106-109` (`engine = TorrentEngine.getInstance(appContext)`), `init:116-132` (`engine.doStart()` :131, `engine.addListener(engineListener)` :132), `stopEngine:161` (`engine.doStop()`), `onStartCommand` calls `init` at :191.
- DownloadsCompletedListener (fresh, 88 lines): `listen:45-86` is a `Completable.create` body (:47-85) holding an `eventHandler` Runnable (:50-53) and an anonymous `TorrentEngineListener` (:55-78); `engine.addListener(listener)` at :81; dispose action at :82-83.
- TorrentEngine singleton: `getInstance:117-126` (double-checked locking, `new TorrentEngine(appContext)` at :121); ctor :128-141 (`downloadsCompleted = new DownloadsCompletedListener(this)` :135, `session.addListener(engineListener)` :140); `engineListener` field :1265-1444 (onSessionError at :1385-1389 calls `errorFilter.skip` at :1386).

## Table — 40 rows, plan order

| # | Method | Label proposed | confirmed_by | Printed citation / route |
|---|---|---|---|---|
| 1 | AddTorrentParams.writeToParcel | OPEN | — | Def AddTorrentParams.java:96-107 only. No printed marshalling site for AddTorrentParams in any file freshly fetched in this pass (no putExtra/getParcelableExtra/putParcelable for this class, and no Intent/Bundle site naming it). The framework calls writeToParcel only when the object is actually parcelled, which was not printed. Pending printed marshalling site or saved full-repo grep. NOT UNREACHABLE on this evidence. |
| 2 | AddTorrentParams$1.<init> | REACHABLE | SOURCE | Anonymous `Parcelable.Creator<AddTorrentParams>` instance created at AddTorrentParams.java:109-119 (field `CREATOR`, instantiated as part of class initialisation). Class loaded via construction sites AddTorrentViewModel.java:510 and TorrentEngine.java:1187. The ctor body itself is the implicit default ctor; the construction site is printed. |
| 3 | AddTorrentParams$1.createFromParcel | OPEN | — | Def AddTorrentParams.java:111-113 (`return new AddTorrentParams(source)`). Same missing-marshalling-site note as row 1: the body is printed, but no printed caller actually parcels/unparcels an AddTorrentParams in this pass. Pending printed marshalling site. NOT UNREACHABLE on this evidence. NOTE the interaction with batch 21 row 36 (`AddTorrentParams.<init>(Parcel)`, REACHABLE SOURCE on this very body :112): the merger must judge 21/36 and 22/3 under one Parcelable convention (see Caveats). |
| 4 | AddTorrentParams$1.newArray | OPEN | — | Def AddTorrentParams.java:116-118 (`return new AddTorrentParams[size]`). Same missing-marshalling-site note as row 1. Pending printed marshalling site. NOT UNREACHABLE on this evidence. |
| 5 | DownloadsCompletedListener.<init> | REACHABLE | SOURCE | Def DownloadsCompletedListener.java:40-43. Construction site TorrentEngine.java:135 (`downloadsCompleted = new DownloadsCompletedListener(this)` inside the ctor). |
| 6 | DownloadsCompletedListener.lambda$listen$0 | REACHABLE | INFERRED | Body DownloadsCompletedListener.java:47-85 (the `Completable.create` lambda: tracks in-progress torrents, registers the listener at :81, dispose action at :82-83). Subscribed in TorrentEngine.doStart:243-251. Rx create/subscribe dispatch unprinted, hence INFERRED. $n mapping source-order, NOT bytecode-verified (see Caveats). |
| 7 | DownloadsCompletedListener.lambda$listen$1 | REACHABLE | INFERRED | Body DownloadsCompletedListener.java:50-53 (the `eventHandler` Runnable: `torrentsInProgress.remove(id); emitter.onComplete()`). Invoked from onTorrentFinished :69 and onTorrentRemoved :76. Session dispatch unprinted, hence INFERRED. $n mapping source-order, NOT bytecode-verified (see Caveats). |
| 8 | DownloadsCompletedListener.lambda$listen$2 | REACHABLE | INFERRED | Body DownloadsCompletedListener.java:82-83 (dispose action: `session.removeListener(listener)`). Disposed via TorrentEngine.doStop:296 (`disposables.clear()`), itself called from TorrentService.stopEngine:161. Rx dispose dispatch unprinted, hence INFERRED. $n mapping source-order, NOT bytecode-verified (see Caveats). |
| 9 | DownloadsCompletedListener.listen | REACHABLE | SOURCE | Def DownloadsCompletedListener.java:45-86. Call site TorrentEngine.doStart:243 (`disposables.add(downloadsCompleted.listen()...)`). |
| 10 | DownloadsCompletedListener$1.<init> | REACHABLE | SOURCE | Anonymous `TorrentEngineListener` instance created at DownloadsCompletedListener.java:55-78, inside the listen() body (row 9). The ctor body itself is the implicit default ctor; the construction site is printed. |
| 11 | DownloadsCompletedListener$1.onTorrentFinished | REACHABLE | INFERRED | Def DownloadsCompletedListener.java:66-70 (calls eventHandler :69, removes from in-progress set). Registration printed: DownloadsCompletedListener.java:81 → TorrentEngine.addListener:307-309 → session.addListener. The session's invocation of this callback is library dispatch, unprinted, hence INFERRED. |
| 12 | DownloadsCompletedListener$1.onTorrentRemoved | REACHABLE | INFERRED | Def DownloadsCompletedListener.java:73-77 (calls eventHandler :76). Same registration/dispatch note as row 11. |
| 13 | DownloadsCompletedListener$1.onTorrentStateChanged | REACHABLE | INFERRED | Def DownloadsCompletedListener.java:57-63 (adds id to in-progress set when state is DOWNLOADING). Same registration/dispatch note as row 11. |
| 14 | SessionErrorFilter.<clinit> | REACHABLE | INFERRED | Static block SessionErrorFilter.java:26-28 (initialises `errors` set). First use printed: TorrentEngine.java:113 (field initialiser `new SessionErrorFilter()`). JVM class-initialisation dispatch unprinted, hence INFERRED. |
| 15 | SessionErrorFilter.<init> | REACHABLE | SOURCE | Def SessionErrorFilter.java:20-24 (implicit default ctor body region; class body :18-33). Construction site TorrentEngine.java:113. |
| 16 | SessionErrorFilter.skip | REACHABLE | SOURCE | Def SessionErrorFilter.java:30-32. Call site TorrentEngine.java:1386 (`errorFilter.skip(errorMsg)` inside engineListener.onSessionError :1385-1389). Listener registered at TorrentEngine.java:140. |
| 17 | TorrentEngine.<clinit> | REACHABLE | INFERRED | Static fields TorrentEngine.java:97 (`TAG = TorrentEngine.class.getSimpleName()`, not a compile-time constant) and :115 (`INSTANCE`). Initialised before getInstance:117. JVM class-initialisation dispatch unprinted, hence INFERRED. |
| 18 | TorrentEngine.<init> | REACHABLE | SOURCE | Def TorrentEngine.java:128-141 (private). Construction site TorrentEngine.getInstance:121 (`INSTANCE = new TorrentEngine(appContext)`), itself called from TorrentService.onCreate:109. |
| 19 | TorrentEngine.addListener | REACHABLE | SOURCE | Def TorrentEngine.java:307-309. Call sites TorrentService.init:132, DownloadsCompletedListener.java:81, TorrentEngine.java:223 (observeEngineRunning). |
| 20 | TorrentEngine.addTorrent(Uri) | REACHABLE | SOURCE | Def TorrentEngine.java:359-361 (delegates :360 to row 21). Internal call site TorrentEngine.scanTorrentsInDir:1173 (`addTorrent(Uri.fromFile(file))`), itself called from startWatchDir:1123. |
| 21 | TorrentEngine.addTorrent(Uri,Uri) | REACHABLE | SOURCE | Def TorrentEngine.java:363-367 (delegates :364 to row 23). Internal call site TorrentEngine.java:360 (row 20). |
| 22 | TorrentEngine.addTorrentCompletable(Uri) | REACHABLE | SOURCE | Def TorrentEngine.java:370-372 (delegates :371 to row 23). Internal call site TorrentEngine.java:1149 (file-observer onEvent: `addTorrentCompletable(uri)`), inside makeTorrentFileObserver, itself called from startWatchDir:1125. |
| 23 | TorrentEngine.addTorrentCompletable(Uri,Uri) | REACHABLE | SOURCE | Def TorrentEngine.java:374-390 (delegates :389 to row 24). Internal call site TorrentEngine.java:364 (row 21). |
| 24 | TorrentEngine.addTorrentSync(Uri,TorrentMetaInfo,Uri) | REACHABLE | SOURCE | Def TorrentEngine.java:1177-1205 (builds AddTorrentParams :1187, delegates :1204 to row 25). Internal call site TorrentEngine.java:389 (row 23). |
| 25 | TorrentEngine.addTorrentSync(AddTorrentParams,boolean) | REACHABLE | SOURCE | Def TorrentEngine.java:401-413 (delegates :412 to session.addTorrent). Internal call sites TorrentEngine.java:333 (addTorrent(params,boolean) :329-334) and :1204 (row 24). |
| 26 | TorrentEngine.addTorrents | REACHABLE | SOURCE | Def TorrentEngine.java:342-356. **Fresh closure in this pass (prior proposal had this OPEN):** FeedDownloaderWorker.java:211 (`engine.addTorrents(paramsList, true);`) — freshly fetched in this pass (SHA `f45dda6f…`, 216 lines), after the engine-start retry loop (:198/:204 `engine.start()`). The batch 23 merge-ready file's `FeedDownloaderWorker:211` claim is now independently confirmed on the same fresh print. |
| 27 | TorrentEngine.addTrackers | REACHABLE | SOURCE | Def TorrentEngine.java:568-575. Call site DetailTorrentViewModel.java:354, freshly fetched in this pass (SHA `6e4ef82f…`, 611 lines). |
| 28 | TorrentEngine.cancelFetchMagnet | REACHABLE | SOURCE | Def TorrentEngine.java:481-486. Call site AddTorrentViewModel.java:572, freshly fetched in this pass (SHA `bec2f6ee…`, 575 lines). |
| 29 | TorrentEngine.checkPauseTorrents | REACHABLE | SOURCE | Def TorrentEngine.java:1023-1032 (private). Internal call sites TorrentEngine.java:320 (rescheduleTorrents), :1277 (engineListener.onTorrentAdded), :1292 (onTorrentLoaded), :1442 (listener site). |
| 30 | TorrentEngine.cleanTemp | REACHABLE | SOURCE | Def TorrentEngine.java:1223-1227 (private, delegates to fs.cleanTempDir :1225). Call site TorrentEngine.doStop:300. |
| 31 | TorrentEngine.createFetchMagnetSingle | REACHABLE | SOURCE | Def TorrentEngine.java:431-479 (private, registers a listener at :451, removes at :453). Internal call site TorrentEngine.fetchMagnet:422. |
| 32 | TorrentEngine.deleteTorrents | REACHABLE | SOURCE | Def TorrentEngine.java:533-541. Call site MainViewModel.java:143, freshly fetched in this pass (SHA `73938fbb…`, 190 lines). |
| 33 | TorrentEngine.deleteTrackers | REACHABLE | SOURCE | Def TorrentEngine.java:543-557. Call site DetailTorrentViewModel.java:346, freshly fetched in this pass. |
| 34 | TorrentEngine.doStart | REACHABLE | SOURCE | Def TorrentEngine.java:234-260. Call site TorrentService.init:131, freshly fetched in this pass (SHA `f0c3cdc4…`, 526 lines). |
| 35 | TorrentEngine.doStop | REACHABLE | SOURCE | Def TorrentEngine.java:292-304. Call site TorrentService.stopEngine:161, freshly fetched in this pass. |
| 36 | TorrentEngine.fetchMagnet | REACHABLE | SOURCE | Def TorrentEngine.java:415-429 (calls session.fetchMagnet :419, createFetchMagnetSingle :422). Call site AddTorrentViewModel.java:237, freshly fetched in this pass. |
| 37 | TorrentEngine.forceAnnounceTorrents | REACHABLE | SOURCE | Def TorrentEngine.java:520-531. Call site MainViewModel.java:151, freshly fetched in this pass. |
| 38 | TorrentEngine.forceRecheckTorrents | REACHABLE | SOURCE | Def TorrentEngine.java:507-518. Call site MainViewModel.java:147, freshly fetched in this pass. |
| 39 | TorrentEngine.forceStop | REACHABLE | SOURCE | Def TorrentEngine.java:282-286 (sends ACTION_SHUTDOWN intent to TorrentService). Internal call sites TorrentEngine.java:145 (handleAutoStop, subscribed in doStart:243-251) and :279 (requestStop). |
| 40 | TorrentEngine.getBencode | REACHABLE | SOURCE | Def TorrentEngine.java:927-936. Internal call site TorrentEngine.saveTorrentFile:974, itself called from saveTorrentFileIn:965, itself called from engineListener.onTorrentAdded :1273-1275 and a second listener site :1431-1432. |

## OPEN rows — what resolves them (all stay OPEN, none flipped to UNREACHABLE)

- Rows 1, 3, 4 (writeToParcel / createFromParcel / newArray): one printed marshalling site for AddTorrentParams (an Intent/Bundle putExtra/getParcelableExtra naming AddTorrentParams, or a fragment-arguments site), or a saved full-repo grep for `AddTorrentParams` parcel use. Row 3's resolution is shared with batch 21 row 36 — see Caveats.
- Row 2 (`$1.<init>`) is deliberately NOT OPEN on the same grounds: its construction site (the CREATOR field at :109-119) is printed, and class initialisation follows from the printed AddTorrentParams construction sites. If the merger instead requires a marshalling site for every Parcelable row, row 2 flips to OPEN as well.

## Caveats the merger must see (recorded, not decided)

1. **Strict-entry:** no launcher step was printed in this pass. Engine rows anchor at TorrentService (init/stopEngine, themselves called from onStartCommand/onCreate) and at MainViewModel/DetailTorrentViewModel/AddTorrentViewModel/FeedDownloaderWorker. Under a strict launcher-entry rule all 37 REACHABLE rows revert to OPEN on that point alone.
2. **Parcelable convention (rows 1–4 + batch 21 rows 36–38):** this file keeps `$1.<init>` REACHABLE on its printed CREATOR construction site while rows 1, 3, 4 stay OPEN for lack of a printed marshalling site; batch 21 keeps `<init>(Parcel)` REACHABLE on the printed CREATOR.createFromParcel body (:112). The merger must pick one convention and apply it consistently across batches 21–22: either (a) CREATOR presence + class construction suffices for all parcel rows (then 22/1, 22/3, 22/4, 21/38 flip to REACHABLE), or (b) a printed marshalling site is required for all parcel rows (then 22/2 and 21/36 flip to OPEN). Labels in this file follow the split convention and are flagged, not decided.
3. **Lambda $n mapping (rows 6–8):** source-order only, NOT bytecode-verified. The plan descriptors for $1 (`(TorrentEngineListener)V`) and $2 (`(CompletableEmitter)V`) do not naively match the Runnable/Action bodies at :50-53 and :82-83, so the merger must confirm the $n-to-body mapping against bytecode before merging. Labels are unaffected: all three bodies sit inside the single printed listen() body, and each runs within the listen() flow (create body on subscribe, eventHandler on finish/remove events, dispose action on dispose via doStop:296).
4. **confirmed_by:** per-row convention stated at the top. Rows 11–13 read INFERRED here because no printed app code names them (session dispatch); under a "registration printed ⇒ SOURCE" convention they would read SOURCE. Labels unaffected.
5. **Overload traps avoided:** `TorrentEngine.addTorrent(AddTorrentParams,boolean)` :329 is NOT row 20/21 (it is the non-plan overload feeding row 25); `stopRecording`/`write` overloads in Logger are not batch 22 rows; `TorrentEngine.start()` (FeedDownloaderWorker :198/:204) is not a batch 22 row.

## Not claimed / still owed before merge

- No build, sampler, full-repo grep, or C1 — build and C1 marked **not run** (Mac after push, never claimed passed). No push made. Main-agent spot-check (1 in 5) and `py_compile` remain outstanding.
- Saved full-repo grep or a printed marshalling site for the 3 OPEN rows before any flip to UNREACHABLE, plus the bytecode $n check and the Parcelable-convention decision above.
- Scope strictly batch 22, LibreTorrent labels only, branch `work-2026-10-31` only, no other batch/app, no device replay, no Aegis.
