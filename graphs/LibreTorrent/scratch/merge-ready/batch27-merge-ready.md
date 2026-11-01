# LibreTorrent batch 27 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler or full-repo grep was run or is claimed.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 27 only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. The prior Agent 6 re-derivation was used as
  INPUT / lead list only; every row below was re-judged against the TorrentInfoProvider source
  freshly fetched in this pass, and no prior verdict was copied as a result. No label changed
  from Agent 6's version; the descriptor check below is the new evidence for keeping all 40 rows
  REACHABLE.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 27 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/b27scratch/LIBRETORRENT_BATCH_PLAN.tsv` (4,732 rows total; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
All 40 batch-27 rows are `TODO_CANDIDATE_REACHABLE` in the plan — a generator candidate, not evidence.
Composition: all 40 rows belong to TorrentInfoProvider — 23 lambdas (rows 1–23) and 17 named
methods (rows 24–40: 9 `make*Flowable`/`make*Single` methods and 8 `observe*` methods).

## Counts — mechanically verified

- **REACHABLE proposed: 40 / 40**
- **UNREACHABLE proposed: 0**
- **OPEN: 0**
- **Verified for merge: 0**
- confirmed_by among REACHABLE: **SOURCE 17 / INFERRED 23**.
- Table rows 1–40 intact, in plan order, method names and JVM descriptors matched against the plan.

## confirmed_by convention used in this file (labels unaffected by the convention choice)

- SOURCE = a printed app-code line names the method as a call target (an `observe*` method called
  by a ViewModel/Fragment/Activity method, or a `make*` method called by its `observe*` method).
- INFERRED = the method is a lambda whose body is printed but whose invocation crosses unprinted
  RxJava `Flowable.create` / `Observable.interval` / thread dispatch, even though its enclosing
  flowable's subscription route is printed.
- Never `DYN`, `FW-MEMORY`, or `UNVERIFIED` as confirmed_by.
- Lambda `$n` numbering is matched to plan JVM descriptors (captured variables + arguments, see
  the descriptor notes in the table), NOT bytecode-verified. The descriptor check is what pins
  each `$n` to its body: e.g. `$0` in batch 26 is the handleEvent consumer because its descriptor
  (String, AtomicReference, FlowableEmitter, String) is exactly its captured variables plus its
  argument. A swap of two same-descriptor lambdas (batch 27 rows 6/7, both (SingleEmitter)) is
  resolved by body, not descriptor alone: row 6 is the `Single.create` body, row 7 the thread body
  inside it — both run on the same subscription route, so a swap would not change either label.

## Printed source used in this pass (fresh connector fetches, branch work-2026-10-31, one at a time, with pauses)

Source root for all files:
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`
Saved under `~/workspace/b262728-src/`. No fresh HTTP 429 was hit in this pass.

- `core/model/TorrentInfoProvider.java` — fresh, 498 lines, SHA-256
  `6d70d61fa0c808d9904ae7f6b3111aacbb086d478a94e4d223db9043b7ecf4fc`, byte-identical to the
  local copy in `~/workspace/b27scratch/`. This single fresh file carries every batch-27
  definition and lambda body; all line numbers below are from this fresh fetch.
- `ui/detailtorrent/DetailTorrentViewModel.java` — fresh, SHA-256
  `de6c860e0d5386cdcd01612e8fd7e0b582cf7cf08f4c02f8abcbdc3042b39c91`, byte-identical to the
  local copy in `~/workspace/b27scratch/`.
- `ui/detailtorrent/DetailTorrentFragment.java` — fresh, SHA-256
  `580c1b0ce3da3ec74b2e1e7b356459326985008bc477f535d2b5876a0947e307`, byte-identical to the
  local copy in `~/workspace/b27scratch/`.
- `ui/main/MainViewModel.java` — fresh, SHA-256
  `251f206bfed7b3bd58bde30246996bf3dae4dd15259658a8df5969c0e6378343`, byte-identical to the
  local copy in `~/workspace/b27scratch/`.
- `ui/main/MainActivity.java` — fresh, SHA-256
  `b98a504934ed44800b9505539e4c12dd952606141fcbb04e4b0f40780a4d8454`, byte-identical to the
  local copy in `~/workspace/b27scratch/`.
- `core/model/TorrentEngine.java`, `core/model/session/TorrentSessionImpl.java`,
  `core/model/session/TorrentDownloadImpl.java`, `core/model/TorrentEngineListener.java` — fresh,
  used for the listener-dispatch background of the `$1`–`$4` analogues in batch 28 and for the
  engine methods (`makeInfoSync`, `makeInfoListSync`, `makeAdvancedInfoSync`, `makeTrackerInfoList`,
  `makePeerInfoList`, `getPieces`) that the batch-27 flowables call; the engine methods themselves
  are not batch-27 rows.
- `ui/main/MainFragment.java`, `ui/detailtorrent/DetailTorrentPeersFragment.java`,
  `ui/detailtorrent/DetailTorrentPiecesFragment.java`,
  `ui/detailtorrent/DetailTorrentTrackersFragment.java` — re-read from local copies in
  `~/workspace/b27scratch/` (previously connector-fetched), NOT freshly fetched in this pass;
  flagged as such wherever a citation below rests on them. Every `observe*`/`make*` link in the
  chain below is fresh except the fragment → ViewModel step, which rests on those local copies.

## Printed route anchors (all TorrentInfoProvider line numbers fresh)

- Info list: MainFragment (local) :287 `viewModel.observeAllTorrentsInfo()` →
  MainViewModel (fresh) :77–78 `stateProvider.observeInfoList()` →
  TorrentInfoProvider (fresh) `observeInfoList` :98–99 → `makeInfoListFlowable` :238–239.
- Info list single: MainFragment (local) :335 `viewModel.getAllTorrentsInfoSingle()` →
  MainViewModel (fresh) :81–83 `stateProvider.getInfoListSingle()` →
  TorrentInfoProvider (fresh) `getInfoListSingle` :102–103 → `makeInfoListSingle` :310–321.
- Trackers: DetailTorrentTrackersFragment (local) :260 → DetailTorrentViewModel (fresh)
  `observeTrackers` :179–180 → TorrentInfoProvider `observeTrackersInfo` :110–111 →
  `makeTrackersInfoFlowable` :357.
- Peers: DetailTorrentPeersFragment (local) :174 → DetailTorrentViewModel (fresh)
  `observePeers` :183–184 → TorrentInfoProvider `observePeersInfo` :114–115 →
  `makePeersInfoFlowable` :390.
- Pieces: DetailTorrentPiecesFragment (local) :138 → DetailTorrentViewModel (fresh)
  `observePieces` :187–188 → TorrentInfoProvider `observePiecesInfo` :118–119 →
  `makePiecesFlowable` :423.
- Session stats: MainActivity (fresh) `onStart` :386 → `subscribeSessionStats` :456–460
  (`infoProvider.observeSessionStats()`) → TorrentInfoProvider `observeSessionStats` :126–127 →
  `makeSessionStatsFlowable` :474.
- Torrents deleted: MainFragment (local) :352 `viewModel.observeTorrentsDeleted()` →
  MainViewModel (fresh) :85–86 `stateProvider.observeTorrentsDeleted()` →
  TorrentInfoProvider `observeTorrentsDeleted` :122–123 → `makeTorrentsDeletedFlowable` :455.
- Advanced / info (batch-26 closure, reused here only as the anchor pattern):
  DetailTorrentFragment (fresh) `subscribeTorrentInfo` :251, :265/:271 →
  DetailTorrentViewModel (fresh) `observeTorrentInfoPair` / `observeAdvancedTorrentInfo` →
  TorrentInfoProvider `observeInfo` / `observeAdvancedInfo`.

## Strict-entry caveat (explicit, all REACHABLE rows)

Routes are anchored at fragment onStart/subscribe steps and MainActivity onStart, not at a fully
printed launcher → detail/main chain (hosting / pager attachment not printed in this pass).
Under a strict launcher-entry rule all 40 REACHABLE rows revert to OPEN. Under the anchor
convention used by sibling detail/main batches, they are REACHABLE as tabled. The merger must
pick one strict-entry convention for all batches; this file does not decide it.

## Caveats (not verdict changes)

- Interval error consumers (rows 9, 13, 21) run only if the Rx interval source errors; proposed
  REACHABLE via the printed subscription route — re-mark OPEN only if the project rule requires
  an observed error trigger (undecided, recorded not decided).
- Lambda rows rest on RxJava / thread dispatch, hence INFERRED, even though every lambda body
  was printed fresh in this pass.
- No UNREACHABLE row is claimed, so no saved full-repo grep is owed for a UNREACHABLE verdict here.

## Per-row table (plan order)

| # | Method | Label | confirmed_by | Printed route / citations |
|---|---|---|---|---|
| 1 | TorrentInfoProvider.lambda$makeInfoListFlowable$5 (AtomicReference, FlowableEmitter) | REACHABLE | INFERRED | Descriptor match: the `handleInfo` Runnable in `makeInfoListFlowable` :242–252 (captures infoList + emitter; runs `engine.makeInfoListSync()` and emits on change). Invoked by the $2 listener callbacks :258, :263, :268, :273, :278, :283 and the tag-repo consumer row 3. Route: info-list anchor above. Rx dispatch INFERRED. |
| 2 | TorrentInfoProvider.lambda$makeInfoListFlowable$6 (TorrentEngineListener) | REACHABLE | INFERRED | Descriptor match: the `Disposables.fromAction` dispose action :295–297 (`engine.removeListener(listener)`, captures the listener). Runs on Rx disposal (MainFragment onStop clears disposables — local copy, not freshly re-verified here). |
| 3 | TorrentInfoProvider.lambda$makeInfoListFlowable$7 (Runnable, List) | REACHABLE | INFERRED | Descriptor match: the `tagRepo.observeAll().subscribe(...)` consumer :298–299 (captures handleInfo Runnable; argument is the observed List). Calls `handleInfo.run()`. |
| 4 | TorrentInfoProvider.lambda$makeInfoListFlowable$8 (AtomicReference, FlowableEmitter, TorrentEngineListener, Runnable) | REACHABLE | INFERRED | Descriptor match: the `Thread` body :288–304 (captures infoList, emitter, listener, handleInfo; initial `engine.makeInfoListSync()`, `emitter.onNext`, `engine.addListener(listener)` :293, disposables). `t.start()` :304. |
| 5 | TorrentInfoProvider.lambda$makeInfoListFlowable$9 (FlowableEmitter) | REACHABLE | INFERRED | Descriptor match: the `Flowable.create` body of `makeInfoListFlowable` :239–306 (captures nothing but the emitter argument; defines infoList locally). Rx dispatch INFERRED. |
| 6 | TorrentInfoProvider.lambda$makeInfoListSingle$10 (SingleEmitter) | REACHABLE | INFERRED | Descriptor match (by body, same descriptor as row 7): the `Single.create` body :311–320. Route: info-list-single anchor above. |
| 7 | TorrentInfoProvider.lambda$makeInfoListSingle$11 (SingleEmitter) | REACHABLE | INFERRED | Descriptor match (by body): the `Thread` body :313–318 (`engine.makeInfoListSync()`, `emitter.onSuccess`) inside row 6's create body; `t.start()` :318. |
| 8 | TorrentInfoProvider.lambda$makePeersInfoFlowable$20 (String, AtomicReference, FlowableEmitter, Long) | REACHABLE | INFERRED | Descriptor match: the `Observable.interval` tick consumer :394–405 (captures id, infoList, emitter; Long tick argument; `engine.makePeerInfoList(id)` + emit on change). Route: peers anchor above. |
| 9 | TorrentInfoProvider.lambda$makePeersInfoFlowable$21 (String, Throwable) | REACHABLE | INFERRED | Descriptor match: the interval error consumer :406–407 (`Log.e` on error; captures id + Throwable argument). Runs only if the interval source errors (see caveat). |
| 10 | TorrentInfoProvider.lambda$makePeersInfoFlowable$22 (AtomicReference, String, FlowableEmitter, Disposable) | REACHABLE | INFERRED | Descriptor match: the `Thread` body :409–417 (captures infoList, id, emitter, interval Disposable; initial `engine.makePeerInfoList(id)`, emit, `emitter.setDisposable(d)`); `t.start()` :417. |
| 11 | TorrentInfoProvider.lambda$makePeersInfoFlowable$23 (String, FlowableEmitter) | REACHABLE | INFERRED | Descriptor match: the `Flowable.create` body of `makePeersInfoFlowable` :391–421 (captures id + emitter). Rx dispatch INFERRED. |
| 12 | TorrentInfoProvider.lambda$makePiecesFlowable$24 (String, AtomicReference, FlowableEmitter, Long) | REACHABLE | INFERRED | Descriptor match: the `Observable.interval` tick consumer :427–438 (`engine.getPieces(id)` + emit on change). Route: pieces anchor above. |
| 13 | TorrentInfoProvider.lambda$makePiecesFlowable$25 (String, Throwable) | REACHABLE | INFERRED | Descriptor match: the interval error consumer :439–440. Runs only if the interval source errors (see caveat). |
| 14 | TorrentInfoProvider.lambda$makePiecesFlowable$26 (AtomicReference, String, FlowableEmitter, Disposable) | REACHABLE | INFERRED | Descriptor match: the `Thread` body :441–449 (initial `engine.getPieces(id)`, emit, `emitter.setDisposable(d)`); `t.start()` :449. |
| 15 | TorrentInfoProvider.lambda$makePiecesFlowable$27 (String, FlowableEmitter) | REACHABLE | INFERRED | Descriptor match: the `Flowable.create` body of `makePiecesFlowable` :424–452 (captures id + emitter). Rx dispatch INFERRED. |
| 16 | TorrentInfoProvider.lambda$makeSessionStatsFlowable$30 (TorrentEngineListener) | REACHABLE | INFERRED | Descriptor match: the `Disposables.fromAction` dispose action :492–493 (`engine.removeListener(listener)`, captures the $4 listener). Route: session-stats anchor above. |
| 17 | TorrentInfoProvider.lambda$makeSessionStatsFlowable$31 (FlowableEmitter) | REACHABLE | INFERRED | Descriptor match: the `Flowable.create` body of `makeSessionStatsFlowable` :475–496 (captures emitter; listener registered :491). Rx dispatch INFERRED. |
| 18 | TorrentInfoProvider.lambda$makeTorrentsDeletedFlowable$28 (TorrentEngineListener) | REACHABLE | INFERRED | Descriptor match: the `Disposables.fromAction` dispose action :467–468 (`engine.removeListener(listener)`, captures the $3 listener). Route: torrents-deleted anchor above. |
| 19 | TorrentInfoProvider.lambda$makeTorrentsDeletedFlowable$29 (FlowableEmitter) | REACHABLE | INFERRED | Descriptor match: the `Flowable.create` body of `makeTorrentsDeletedFlowable` :456–471 (captures emitter; `onTorrentRemoved` listener :457, registered :466). Rx dispatch INFERRED. |
| 20 | TorrentInfoProvider.lambda$makeTrackersInfoFlowable$16 (String, AtomicReference, FlowableEmitter, Long) | REACHABLE | INFERRED | Descriptor match: the `Observable.interval` tick consumer :361–372 (`engine.makeTrackerInfoList(id)` + emit on change). Route: trackers anchor above. |
| 21 | TorrentInfoProvider.lambda$makeTrackersInfoFlowable$17 (String, Throwable) | REACHABLE | INFERRED | Descriptor match: the interval error consumer :373–374. Runs only if the interval source errors (see caveat). |
| 22 | TorrentInfoProvider.lambda$makeTrackersInfoFlowable$18 (AtomicReference, String, FlowableEmitter, Disposable) | REACHABLE | INFERRED | Descriptor match: the `Thread` body :376–384 (initial `engine.makeTrackerInfoList(id)`, emit, `emitter.setDisposable(d)`); `t.start()` :384. |
| 23 | TorrentInfoProvider.lambda$makeTrackersInfoFlowable$19 (String, FlowableEmitter) | REACHABLE | INFERRED | Descriptor match: the `Flowable.create` body of `makeTrackersInfoFlowable` :358–388 (captures id + emitter). Rx dispatch INFERRED. |
| 24 | TorrentInfoProvider.makeAdvancedInfoFlowable (String) | REACHABLE | SOURCE | Definition :323–354 (fresh). Called by `observeAdvancedInfo` :106–107 (fresh). |
| 25 | TorrentInfoProvider.makeInfoFlowable (String) | REACHABLE | SOURCE | Definition :130–236 (fresh). Called by `observeInfo` :94–95 (fresh). |
| 26 | TorrentInfoProvider.makeInfoListFlowable () | REACHABLE | SOURCE | Definition :238–308 (fresh). Called by `observeInfoList` :98–99 (fresh). |
| 27 | TorrentInfoProvider.makeInfoListSingle () | REACHABLE | SOURCE | Definition :310–321 (fresh). Called by `getInfoListSingle` :102–103 (fresh). |
| 28 | TorrentInfoProvider.makePeersInfoFlowable (String) | REACHABLE | SOURCE | Definition :390–421 (fresh). Called by `observePeersInfo` :114–115 (fresh). |
| 29 | TorrentInfoProvider.makePiecesFlowable (String) | REACHABLE | SOURCE | Definition :423–453 (fresh). Called by `observePiecesInfo` :118–119 (fresh). |
| 30 | TorrentInfoProvider.makeSessionStatsFlowable () | REACHABLE | SOURCE | Definition :474–497 (fresh). Called by `observeSessionStats` :126–127 (fresh). |
| 31 | TorrentInfoProvider.makeTorrentsDeletedFlowable () | REACHABLE | SOURCE | Definition :455–472 (fresh). Called by `observeTorrentsDeleted` :122–123 (fresh). |
| 32 | TorrentInfoProvider.makeTrackersInfoFlowable (String) | REACHABLE | SOURCE | Definition :357–388 (fresh). Called by `observeTrackersInfo` :110–111 (fresh). |
| 33 | TorrentInfoProvider.observeAdvancedInfo (String) | REACHABLE | SOURCE | Definition :106–107 → row 24 (fresh). Called by DetailTorrentViewModel.observeAdvancedTorrentInfo :171–172 (fresh) ← DetailTorrentFragment.subscribeTorrentInfo :271 (fresh). |
| 34 | TorrentInfoProvider.observeInfo (String) | REACHABLE | SOURCE | Definition :94–95 → row 25 (fresh). Called by DetailTorrentViewModel.observeTorrentInfo :167–168 (fresh) ← DetailTorrentFragment.observeTorrentInfoPair :191–192 (fresh) ← subscribeTorrentInfo :265 (fresh). |
| 35 | TorrentInfoProvider.observeInfoList () | REACHABLE | SOURCE | Definition :98–99 → row 26 (fresh). Called by MainViewModel.observeAllTorrentsInfo :77–78 (fresh) ← MainFragment :287 (local copy). |
| 36 | TorrentInfoProvider.observePeersInfo (String) | REACHABLE | SOURCE | Definition :114–115 → row 28 (fresh). Called by DetailTorrentViewModel.observePeers :183–184 (fresh) ← DetailTorrentPeersFragment :174 (local copy). |
| 37 | TorrentInfoProvider.observePiecesInfo (String) | REACHABLE | SOURCE | Definition :118–119 → row 29 (fresh). Called by DetailTorrentViewModel.observePieces :187–188 (fresh) ← DetailTorrentPiecesFragment :138 (local copy). |
| 38 | TorrentInfoProvider.observeSessionStats () | REACHABLE | SOURCE | Definition :126–127 → row 30 (fresh). Called by MainActivity.subscribeSessionStats :456–460 (fresh), from MainActivity.onStart :386 (fresh). |
| 39 | TorrentInfoProvider.observeTorrentsDeleted () | REACHABLE | SOURCE | Definition :122–123 → row 31 (fresh). Called by MainViewModel.observeTorrentsDeleted :85–86 (fresh) ← MainFragment :352 (local copy). |
| 40 | TorrentInfoProvider.observeTrackersInfo (String) | REACHABLE | SOURCE | Definition :110–111 → row 32 (fresh). Called by DetailTorrentViewModel.observeTrackers :179–180 (fresh) ← DetailTorrentTrackersFragment :260 (local copy). |

## Gaps / what the merger must still close (not verdict changes)

- Main-agent spot-check (1 in 5), `py_compile`, build, and Mac build/C1 are not run here.
- Fragment → ViewModel steps (MainFragment, Peers/Pieces/Trackers page fragments) rest on local
  copies re-read in this session, not fresh fetches; the merger's spot-check should re-print at
  least one of those files fresh if it requires fresh evidence for every row. All
  TorrentInfoProvider / ViewModel / MainActivity / DetailTorrentFragment lines above are fresh
  connector fetches from branch work-2026-10-31 in this session.
- Strict-entry convention and the Rx-error-trigger question (rows 9, 13, 21) are undecided
  project conventions, recorded here, not decided.
