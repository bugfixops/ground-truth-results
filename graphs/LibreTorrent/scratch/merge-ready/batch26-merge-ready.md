**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 26 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler or full-repo grep was run or is claimed.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 26 only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. Prior proposals (Agent 5 / batch-26 proposal)
  were used as INPUT / lead lists only; every row below was re-judged against source printed in
  this pass, and no prior verdict was copied as a result. The one verdict change from the prior
  proposal is the point of this file: rows 32–40 were OPEN there for want of a printed caller of
  `observeAdvancedInfo` / `observeInfo`; that caller is now printed fresh (see below), so rows
  32–40 are REACHABLE proposed here, not OPEN.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 26 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/b27scratch/LIBRETORRENT_BATCH_PLAN.tsv` (4,732 rows total; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
All 40 batch-26 rows are `TODO_CANDIDATE_REACHABLE` in the plan — a generator candidate, not evidence.
Composition: TorrentEngine$5 (5 rows), TorrentEngineListener (22 rows), TorrentInfoProvider (13 rows).

## Counts — mechanically verified

- **REACHABLE proposed: 40 / 40**
- **UNREACHABLE proposed: 0**
- **OPEN: 0**
- **Verified for merge: 0**
- confirmed_by among REACHABLE: **SOURCE 30 / INFERRED 10** (see convention below).
- Table rows 1–40 intact, in plan order, method names and JVM descriptors matched against the plan.

## confirmed_by convention used in this file (labels unaffected by the convention choice)

- SOURCE = a printed app-code line names the method as a call target: a direct call, a
  `notifyListeners` call site naming the callback, or a printed `new X(...)` / anonymous
  instantiation site for a `<init>` row.
- INFERRED = the method is reached only through unprinted framework/library/Rx/JVM dispatch
  (libtorrent alert delivery to a notify site, Rx `Flowable.create`/thread dispatch, JVM class
  initialisation), even though its body and its registration are printed.
- Never `DYN`, `FW-MEMORY`, or `UNVERIFIED` as confirmed_by. OPEN rows would show — (none);
  there are no OPEN rows in this batch.
- Lambda `$n` numbering is matched to plan JVM descriptors, NOT bytecode-verified. A swap of two
  same-descriptor lambdas would not change any label in this batch, because every lambda in
  rows 32–40 belongs to a flowable whose subscription route is printed.

## Printed source used in this pass (fresh connector fetches, branch work-2026-10-31, one at a time, with pauses)

Source root for all files:
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`
Saved under `~/workspace/b262728-src/`. No fresh HTTP 429 was hit in this pass.

- `core/model/TorrentInfoProvider.java` — fresh, 498 lines, SHA-256
  `6d70d61fa0c808d9904ae7f6b3111aacbb086d478a94e4d223db9043b7ecf4fc`, byte-identical to the
  local copy in `~/workspace/b27scratch/`.
- `ui/detailtorrent/DetailTorrentViewModel.java` — fresh, SHA-256
  `de6c860e0d5386cdcd01612e8fd7e0b582cf7cf08f4c02f8abcbdc3042b39c91`, byte-identical to the
  local copy in `~/workspace/b27scratch/`.
- `ui/detailtorrent/DetailTorrentFragment.java` — fresh, SHA-256
  `580c1b0ce3da3ec74b2e1e7b356459326985008bc477f535d2b5876a0947e307`, byte-identical to the
  local copy in `~/workspace/b27scratch/`.
- `core/model/TorrentEngineListener.java` — fresh, 73 lines, SHA-256
  `845e222fbd95a4d014b401c702f60a9dde9e98055cbd2234137dad04a4fc7c50`, byte-identical to the
  local copy in `~/workspace/b26-src/`.
- `core/model/TorrentEngine.java` — fresh, 1,658 lines. (The local copy in
  `~/workspace/b73-74-src/` is a numbered dump, so its SHA differs; the fresh raw file's key
  lines below were read from the fresh fetch, not from that dump.)
- `core/model/session/TorrentSessionImpl.java` — fresh, 1,720 lines.
- `core/model/session/TorrentDownloadImpl.java` — fresh, 1,711 lines.
- `ui/main/MainViewModel.java` — fresh, SHA-256
  `251f206bfed7b3bd58bde30246996bf3dae4dd15259658a8df5969c0e6378343`, byte-identical to the
  local copy in `~/workspace/b27scratch/`.
- `ui/main/MainActivity.java` — fresh, SHA-256
  `b98a504934ed44800b9505539e4c12dd952606141fcbb04e4b0f40780a4d8454`, byte-identical to the
  local copy in `~/workspace/b27scratch/`.
- `core/model/data/AdvancedTorrentInfo.java`, `core/model/data/MagnetInfo.java`,
  `core/model/data/AbstractInfoParcel.java`, `ui/addtorrent/AddTorrentViewModel.java` — fresh,
  used for batch 28; cited here only where a batch-26 route touches them (it does not, except
  via TorrentInfoProvider's `makeAdvancedInfoSync` call, whose engine side is fresh TorrentEngine).
- `ui/main/MainFragment.java`, `ui/detailtorrent/DetailTorrentPeersFragment.java`,
  `ui/detailtorrent/DetailTorrentPiecesFragment.java`,
  `ui/detailtorrent/DetailTorrentTrackersFragment.java`, `ui/service/TorrentService.java` —
  re-read from local copies in `~/workspace/b27scratch/` (previously connector-fetched), NOT
  freshly fetched in this pass; flagged as such wherever a citation below rests on them.
  TorrentService citations (onCreate :109–110, init doStart/addListener) are local-copy only.

## Printed route anchors

1. **Service entry.** TorrentService.onCreate (local copy) :109
   `engine = TorrentEngine.getInstance(...)`, :110
   `stateProvider = TorrentInfoProvider.getInstance(...)`; TorrentService.init (local copy)
   calls `engine.doStart()` and `engine.addListener(engineListener)`.
2. **Engine listener registration.** TorrentEngine (fresh) :140
   `session.addListener(engineListener)`; engineListener field :1265
   `new TorrentEngineListener() { ... }` with the five batch-26 overrides at :1291
   (onTorrentLoaded), :1306 (onTorrentFinished), :1329 (onTorrentMoving), :1348 (onTorrentMoved),
   :1420 (onTorrentMetadataLoaded). Trap avoided: TorrentEngine :592 `onTorrentMetadataLoaded`
   is a *different* anonymous listener inside `observeTorrentMetaInfo`, not the $5 override, and
   is not cited for any batch-26 row.
3. **Session listener registration and the base-method mechanism.** TorrentSessionImpl (fresh):
   `torrentTaskListener` :1053–1059 overrides **only** `onTorrentRemoved`; it is added in
   `onBeforeStart` :986 and removed in `onBeforeStop` :1036. Therefore, for every event except
   `onTorrentRemoved`, a notify during a running session reaches the **base** (empty)
   `TorrentEngineListener` method through `torrentTaskListener` (Java virtual dispatch to the
   unoverridden base method is the one INFERRED step; registration and every notify site are
   printed). For `onTorrentRemoved`, the base method runs through `engineListener`, which does
   **not** override it (TorrentEngine :1265–1454 override list). For `onSessionStopped`,
   `torrentTaskListener` has already been removed in `onBeforeStop`, so the base method runs
   through `engineListener`, which also does not override it.
4. **Notify loops (fresh).** TorrentSessionImpl `notifyListeners` :1445–1451 iterates `listeners`;
   TorrentDownloadImpl `notifyListeners` :187–193 does the same over the shared queue
   (TorrentSessionImpl `newTask` passes the session `listeners` queue to new downloads).
5. **The batch-26 OPEN-row closure (the change from the prior proposal).**
   DetailTorrentFragment (fresh) `subscribeTorrentInfo` :251, called from `onStart` :228,
   subscribes `viewModel.observeTorrentInfoPair()` :265 and `viewModel.observeAdvancedTorrentInfo()`
   :271. DetailTorrentViewModel (fresh) `observeTorrentInfo` :167–168 calls
   `infoProvider.observeInfo(torrentId)` (observeTorrentInfoPair :191–192 combines it), and
   `observeAdvancedTorrentInfo` :171–172 calls `infoProvider.observeAdvancedInfo(torrentId)`.
   TorrentInfoProvider (fresh) `observeInfo` :94–95 calls `makeInfoFlowable`, and
   `observeAdvancedInfo` :106–107 calls `makeAdvancedInfoFlowable`. Hence every lambda inside
   those two flowables (rows 32–40) is subscribed through a printed chain, and none stays OPEN.
   The prior proposal's missing evidence is no longer missing.

## Strict-entry caveat (explicit, all REACHABLE rows)

Routes are anchored at TorrentService (a Service entry, not a launcher entry) and at
DetailTorrentFragment / MainFragment / MainActivity onStart/subscribe steps. Which component
starts TorrentService, and the launcher → DetailTorrentFragment / MainActivity step, were not
printed in this pass. Under a strict launcher-entry rule all 40 REACHABLE rows revert to OPEN.
Under the anchor convention used by sibling detail/main batches, they are REACHABLE as tabled.
The merger must pick one strict-entry convention for all batches; this file does not decide it.

## Per-row table (plan order)

| # | Method | Label | confirmed_by | Printed route / citations |
|---|---|---|---|---|
| 1 | TorrentEngine$5.onTorrentFinished (String) | REACHABLE | SOURCE | Override TorrentEngine:1306–1326 (fresh). Notify: TorrentDownloadImpl:482–483 `notifyListeners((listener) -> listener.onTorrentFinished(id))` (fresh), reached from the TORRENT_FINISHED alert case :231–232. Registration: TorrentEngine:140, TorrentService.init (local). Alert dispatch INFERRED. |
| 2 | TorrentEngine$5.onTorrentLoaded (String) | REACHABLE | SOURCE | Override TorrentEngine:1291–1303 (fresh). Notify: TorrentSessionImpl:1082–1087 ADD_TORRENT case — `onTorrentLoaded(hash)` when the hash is not in `addTorrentsList` (else `onTorrentAdded`) (fresh). |
| 3 | TorrentEngine$5.onTorrentMetadataLoaded (String, Exception) | REACHABLE | SOURCE | Override TorrentEngine:1420–1453 (fresh). Notify: TorrentDownloadImpl:438–439 `notifyListeners((listener) -> listener.onTorrentMetadataLoaded(id, err[0]))` (fresh). Not the :592 listener (see trap above). |
| 4 | TorrentEngine$5.onTorrentMoved (String, boolean) | REACHABLE | SOURCE | Override TorrentEngine:1348–1369 (fresh). Notify: TorrentDownloadImpl:287 `onStorageMoved` → `listener.onTorrentMoved(id, success)` (fresh), from STORAGE_MOVED / STORAGE_MOVED_FAILED cases :250–255. |
| 5 | TorrentEngine$5.onTorrentMoving (String) | REACHABLE | SOURCE | Override TorrentEngine:1329–1345 (fresh). Notify: TorrentDownloadImpl:1226 `notifyListeners((listener) -> listener.onTorrentMoving(id))` (fresh), in `setDownloadPath` before `moveStorage`. |
| 6 | TorrentEngineListener.<init> () | REACHABLE | SOURCE | Abstract base (fresh TorrentEngineListener.java, 73 lines, all callbacks empty). Instantiated as part of every printed anonymous `new TorrentEngineListener() {…}` — first via the `engineListener` field at TorrentEngine:1265 (fresh), during TorrentEngine construction (getInstance, called from TorrentService.onCreate:109, local). JVM super-call dispatch INFERRED; construction site printed. |
| 7 | TorrentEngineListener.onIpFilterParsed (int) | REACHABLE | SOURCE | Notify: TorrentSessionImpl:737–738 `listener.onIpFilterParsed(ruleCount)` (fresh), after IP-filter parsing :730–731. Base runs via `torrentTaskListener` (overrides only `onTorrentRemoved`). |
| 8 | TorrentEngineListener.onMagnetLoaded (String, byte[]) | REACHABLE | SOURCE | Notify: TorrentSessionImpl:1164–1165 `listener.onMagnetLoaded(hash, loadedMagnets.get(hash))` (fresh). Base runs via `torrentTaskListener`. |
| 9 | TorrentEngineListener.onNatError (String) | REACHABLE | SOURCE | Notify: TorrentSessionImpl `checkError` PORTMAP_ERROR case :1130–1135 `listener.onNatError(msg)` when not non-critical (fresh). Base runs via `torrentTaskListener`. |
| 10 | TorrentEngineListener.onPieceFinished (String, int) | REACHABLE | SOURCE | Notify: TorrentDownloadImpl PIECE_FINISHED case :259–260 `listener.onPieceFinished(id, piece)` (fresh). Base runs via `torrentTaskListener` (shared listeners queue). |
| 11 | TorrentEngineListener.onReadPiece (String, ReadPieceInfo) | REACHABLE | SOURCE | Notify: TorrentDownloadImpl `handleReadPiece` :452–453 `listener.onReadPiece(id, info)` (fresh). Base runs via `torrentTaskListener`. |
| 12 | TorrentEngineListener.onRestoreSessionError (String) | REACHABLE | SOURCE | Notify: TorrentSessionImpl:1527–1528 `listener.onRestoreSessionError(torrentId)` (fresh), restore-failure catch path :1519–1529. Base runs via `torrentTaskListener`. |
| 13 | TorrentEngineListener.onSessionError (String) | REACHABLE | SOURCE | Notify: TorrentSessionImpl `checkError` SESSION_ERROR :1114–1119 and LISTEN_FAILED :1122–1127, both `listener.onSessionError(msg)` when not non-critical (fresh). Base runs via `torrentTaskListener`. |
| 14 | TorrentEngineListener.onSessionStarted () | REACHABLE | SOURCE | Notify: TorrentSessionImpl `onAfterStart` :1009–1012 `notifyListeners(TorrentEngineListener::onSessionStarted)` (fresh), after `torrentTaskListener` was added in `onBeforeStart` :986. Base runs via `torrentTaskListener` (engineListener overrides this one, so the base does not run through engineListener). |
| 15 | TorrentEngineListener.onSessionStats (SessionStats) | REACHABLE | SOURCE | Notify: TorrentSessionImpl `handleStats` :1173–1180 `listener.onSessionStats(...)` (fresh). Base runs via `torrentTaskListener`. |
| 16 | TorrentEngineListener.onSessionStopped () | REACHABLE | SOURCE | Notify: TorrentSessionImpl `onAfterStop` :1041–1044 `notifyListeners(TorrentEngineListener::onSessionStopped)` (fresh). Base runs via `engineListener`, which does not override it and is never removed (registered TorrentEngine:140); `torrentTaskListener` was already removed in `onBeforeStop` :1036, so it is not cited for this row. |
| 17 | TorrentEngineListener.onTorrentAdded (String) | REACHABLE | SOURCE | Notify: TorrentSessionImpl ADD_TORRENT case :1082–1084 `listener.onTorrentAdded(hash)` when in `addTorrentsList` (fresh). Base runs via `torrentTaskListener`. |
| 18 | TorrentEngineListener.onTorrentError (String, Exception) | REACHABLE | SOURCE | Notify: TorrentDownloadImpl :334–335 and :422–423 `listener.onTorrentError(id, …)` (fresh). Base runs via `torrentTaskListener`. |
| 19 | TorrentEngineListener.onTorrentFinished (String) | REACHABLE | SOURCE | Notify: TorrentDownloadImpl `handleTorrentFinished` :482–483 (fresh). Base runs via `torrentTaskListener` (engineListener overrides this one, so the base does not run through engineListener). |
| 20 | TorrentEngineListener.onTorrentLoaded (String) | REACHABLE | SOURCE | Notify: TorrentSessionImpl ADD_TORRENT case :1085–1087 `listener.onTorrentLoaded(hash)` when not in `addTorrentsList` (fresh). Base runs via `torrentTaskListener`. |
| 21 | TorrentEngineListener.onTorrentMetadataLoaded (String, Exception) | REACHABLE | SOURCE | Notify: TorrentDownloadImpl :438–439 (fresh). Base runs via `torrentTaskListener` (engineListener overrides this one). |
| 22 | TorrentEngineListener.onTorrentMoved (String, boolean) | REACHABLE | SOURCE | Notify: TorrentDownloadImpl `onStorageMoved` :287 (fresh). Base runs via `torrentTaskListener` (engineListener overrides this one). |
| 23 | TorrentEngineListener.onTorrentMoving (String) | REACHABLE | SOURCE | Notify: TorrentDownloadImpl `setDownloadPath` :1226 (fresh). Base runs via `torrentTaskListener` (engineListener overrides this one). |
| 24 | TorrentEngineListener.onTorrentPaused (String) | REACHABLE | SOURCE | Notify: TorrentDownloadImpl TORRENT_PAUSED case :238–239 `listener.onTorrentPaused(id)` (fresh). Base runs via `torrentTaskListener`. |
| 25 | TorrentEngineListener.onTorrentRemoved (String) | REACHABLE | SOURCE | Notify: TorrentSessionImpl :388–389 and TorrentDownloadImpl `torrentRemoved` :458–459 (fresh). Base runs via `engineListener`, which does not override it (registered TorrentEngine:140); `torrentTaskListener` **does** override this one (TorrentSessionImpl:1055–1058), so it is not cited for this row. |
| 26 | TorrentEngineListener.onTorrentResumed (String) | REACHABLE | SOURCE | Notify: TorrentDownloadImpl TORRENT_RESUMED case :244–245 `listener.onTorrentResumed(id)` (fresh). Base runs via `torrentTaskListener`. |
| 27 | TorrentEngineListener.onTorrentStateChanged (String, TorrentStateCode, TorrentStateCode) | REACHABLE | SOURCE | Notify: TorrentDownloadImpl STATE_CHANGED case :226–229 `listener.onTorrentStateChanged(id, …)` (fresh). Base runs via `torrentTaskListener`. |
| 28 | TorrentInfoProvider.<clinit> () | REACHABLE | INFERRED | JVM class initialisation for static fields TorrentInfoProvider:55–59 (`TAG`, `GET_INFO_SYNC_TIME`, `INSTANCE`) (fresh). First use is the REACHABLE `getInstance(Context)` call (row 31); class-init timing itself is not a printed call, hence INFERRED. |
| 29 | TorrentInfoProvider.<init> (TorrentEngine, TagRepository) | REACHABLE | SOURCE | Printed `new TorrentInfoProvider(...)` at TorrentInfoProvider:70 (other overload) and :80–82 (`getInstance(Context)`, fresh). Definition :89–92 (fresh). Route via row 31. |
| 30 | TorrentInfoProvider.getInfoListSingle () | REACHABLE | SOURCE | Definition TorrentInfoProvider:102–104 `return makeInfoListSingle();` (fresh). Called from MainViewModel.getAllTorrentsInfoSingle :81–83 (fresh) and TorrentService.getInfoListSingle (local copy, :298–299). Rx subject/settings dispatch INFERRED; the call sites are printed. |
| 31 | TorrentInfoProvider.getInstance (Context) | REACHABLE | SOURCE | Definition TorrentInfoProvider:76–87 (fresh). Called from MainViewModel constructor (fresh: `stateProvider = TorrentInfoProvider.getInstance(application);`) and TorrentService.onCreate:110 (local copy). The other overload `getInstance(engine, tagRepo)` :63–74 is **not** a batch-26 row and is not judged here. |
| 32 | TorrentInfoProvider.lambda$makeAdvancedInfoFlowable$12 (String, AtomicReference, FlowableEmitter, Long) | REACHABLE | INFERRED | Descriptor match: the `Observable.interval` tick consumer in `makeAdvancedInfoFlowable` :327–338 (periodic `engine.makeAdvancedInfoSync(id)` + `emitter.onNext`) (fresh). Runs on subscription via `observeAdvancedInfo` :106–107 ← DetailTorrentViewModel.observeAdvancedTorrentInfo :171–172 (fresh) ← DetailTorrentFragment.subscribeTorrentInfo :271 (fresh). Rx interval dispatch INFERRED; subscription route printed. **Changed from prior proposal (OPEN) on this fresh chain.** |
| 33 | TorrentInfoProvider.lambda$makeAdvancedInfoFlowable$13 (String, Throwable) | REACHABLE | INFERRED | Descriptor match: the interval error consumer :337–338 `Log.e(TAG, "Getting advanced info …")` (fresh). Same subscription route as row 32. Runs only if the interval source errors; proposed REACHABLE via the printed subscription route — re-mark OPEN only if the project rule requires an observed error trigger (undecided, recorded not decided). **Changed from prior proposal (OPEN).** |
| 34 | TorrentInfoProvider.lambda$makeAdvancedInfoFlowable$14 (String, AtomicReference, FlowableEmitter, Disposable) | REACHABLE | INFERRED | Descriptor match: the `Thread` Runnable in `makeAdvancedInfoFlowable` :341–351 (initial `engine.makeAdvancedInfoSync(id)`, `emitter.onNext`, `emitter.setDisposable(d)`) (fresh). Same subscription route as row 32. **Changed from prior proposal (OPEN).** |
| 35 | TorrentInfoProvider.lambda$makeAdvancedInfoFlowable$15 (String, FlowableEmitter) | REACHABLE | INFERRED | Descriptor match: the `Flowable.create` body of `makeAdvancedInfoFlowable` :324–355 (fresh). Same subscription route as row 32. Rx dispatch INFERRED. **Changed from prior proposal (OPEN).** |
| 36 | TorrentInfoProvider.lambda$makeInfoFlowable$0 (String, AtomicReference, FlowableEmitter, String) | REACHABLE | INFERRED | Descriptor match: the `handleEvent` Consumer in `makeInfoFlowable` :134–145 (fresh). Invoked from the $1 listener overrides :153, :164, :175, :186, :197 and from row 38, all inside `makeInfoFlowable`, called by `observeInfo` :94–95 (fresh) ← DetailTorrentViewModel.observeTorrentInfo :167–168 (fresh) ← DetailTorrentFragment.subscribeTorrentInfoPair :265 (fresh). **Changed from prior proposal (OPEN).** |
| 37 | TorrentInfoProvider.lambda$makeInfoFlowable$1 (TorrentEngineListener) | REACHABLE | INFERRED | Descriptor match: the `Disposables.fromAction` dispose action in `makeInfoFlowable` :216–218 (`engine.removeListener(listener)`) (fresh). Runs on disposal after subscription via row 36's route. **Changed from prior proposal (OPEN).** |
| 38 | TorrentInfoProvider.lambda$makeInfoFlowable$2 (Consumer, String, FlowableEmitter, List) | REACHABLE | INFERRED | Descriptor match: the `tagRepo.observeByTorrentId(id).subscribe(...)` consumer in `makeInfoFlowable` :219–227 (calls `handleEvent.accept(id)`) (fresh). Runs inside the row-39 thread after subscription via row 36's route. **Changed from prior proposal (OPEN).** |
| 39 | TorrentInfoProvider.lambda$makeInfoFlowable$3 (String, AtomicReference, FlowableEmitter, TorrentEngineListener, Consumer) | REACHABLE | INFERRED | Descriptor match: the `Thread` Runnable in `makeInfoFlowable` :207–232 (initial `engine.makeInfoSync(id)`, `engine.addListener(listener)` :214, tag-repo subscription) (fresh). Same subscription route as row 36. **Changed from prior proposal (OPEN).** |
| 40 | TorrentInfoProvider.lambda$makeInfoFlowable$4 (String, FlowableEmitter) | REACHABLE | INFERRED | Descriptor match: the `Flowable.create` body of `makeInfoFlowable` :131–236 (fresh). Same subscription route as row 36. Rx dispatch INFERRED. **Changed from prior proposal (OPEN).** |

## Gaps / what the merger must still close (not verdict changes)

- No UNREACHABLE row is claimed in this batch, so no saved full-repo grep is owed for a
  UNREACHABLE verdict here. A saved full-repo grep would still strengthen every REACHABLE row
  whose final step crosses library/Rx dispatch, but it is not required to keep a REACHABLE label
  that already has a printed subscription/notify chain.
- Strict-entry convention (see above) and the Rx-error-trigger question for row 33 are
  undecided project conventions, recorded here, not decided.
- Main-agent spot-check (1 in 5), `py_compile`, build, and Mac build/C1 are not run here.
- TorrentService and MainFragment citations rest on local copies re-read in this session, not
  fresh fetches; the merger's spot-check should re-print at least TorrentService fresh if it
  requires fresh evidence for every row. All other definition/caller files above are fresh
  connector fetches from branch work-2026-10-31 in this session.
