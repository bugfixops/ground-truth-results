# LibreTorrent batch 27 source audit

Membership is the exact 40-row set in `scratch/batch_027_plan.txt`; printed source excerpts and call-site searches are in `scratch/batch_027_helper_printed.txt`. I independently checked the provider implementation and callers against that evidence.

The helper found 16 public/private provider methods with app-source callers and locally connected call chains. I retained them as OPEN because graph_def.py currently has no hand-authored entry-to-screen/service paths for these methods. The 23 synthetic lambda methods depend on Rx subscription, emitter, listener, timer, thread, or disposal callback delivery, which also remains OPEN. `makeInfoListSingle` is reached from an Rx settings-change chain and is OPEN for the same missing callback route. No method is labeled from generated candidates or coverage.

| # | Method | Label | Evidence / route note |
|---:|---|---|---|
| 1 | `TorrentInfoProvider.lambda$makeInfoListFlowable$5(AtomicReference,FlowableEmitter)` | OPEN | Captured update runnable in `TorrentInfoProvider.java:242-250`; invoked from session listener and tag-observer callbacks (`:253-285,298-300`), delivery unresolved. |
| 2 | `TorrentInfoProvider.lambda$makeInfoListFlowable$6(TorrentEngineListener)` | OPEN | Listener-disposal cleanup in `TorrentInfoProvider.java:287-307`; Rx disposal route unresolved. |
| 3 | `TorrentInfoProvider.lambda$makeInfoListFlowable$7(Runnable,List)` | OPEN | Async update callback in `TorrentInfoProvider.java:238-307`; listener/Rx delivery unresolved. |
| 4 | `TorrentInfoProvider.lambda$makeInfoListFlowable$8(AtomicReference,FlowableEmitter,TorrentEngineListener,Runnable)` | OPEN | Thread callback inside Flowable source (`TorrentInfoProvider.java:287-305`); Rx subscription route unresolved. |
| 5 | `TorrentInfoProvider.lambda$makeInfoListFlowable$9(FlowableEmitter)` | OPEN | Flowable source lambda in `TorrentInfoProvider.java:238-308`; subscription dispatch unresolved. |
| 6 | `TorrentInfoProvider.lambda$makeInfoListSingle$10(SingleEmitter)` | OPEN | Single source in `TorrentInfoProvider.java:310-320`; Rx subscription dispatch unresolved. |
| 7 | `TorrentInfoProvider.lambda$makeInfoListSingle$11(SingleEmitter)` | OPEN | Thread callback under that Single source (`TorrentInfoProvider.java:313-319`); Rx source execution unresolved. |
| 8 | `TorrentInfoProvider.lambda$makePeersInfoFlowable$20(String,AtomicReference,FlowableEmitter,Long)` | OPEN | Timer callback in `TorrentInfoProvider.java:390-420`; Rx interval delivery unresolved. |
| 9 | `TorrentInfoProvider.lambda$makePeersInfoFlowable$21(String,Throwable)` | OPEN | Rx error consumer in `TorrentInfoProvider.java:394-406`; delivery unresolved. |
| 10 | `TorrentInfoProvider.lambda$makePeersInfoFlowable$22(AtomicReference,String,FlowableEmitter,Disposable)` | OPEN | Thread callback in `TorrentInfoProvider.java:408-418`; Flowable source execution unresolved. |
| 11 | `TorrentInfoProvider.lambda$makePeersInfoFlowable$23(String,FlowableEmitter)` | OPEN | Flowable source in `TorrentInfoProvider.java:390-420`; subscription dispatch unresolved. |
| 12 | `TorrentInfoProvider.lambda$makePiecesFlowable$24(String,AtomicReference,FlowableEmitter,Long)` | OPEN | Timer callback in `TorrentInfoProvider.java:423-452`; Rx interval delivery unresolved. |
| 13 | `TorrentInfoProvider.lambda$makePiecesFlowable$25(String,Throwable)` | OPEN | Rx error consumer in `TorrentInfoProvider.java:427-438`; delivery unresolved. |
| 14 | `TorrentInfoProvider.lambda$makePiecesFlowable$26(AtomicReference,String,FlowableEmitter,Disposable)` | OPEN | Thread callback in `TorrentInfoProvider.java:440-450`; Flowable source execution unresolved. |
| 15 | `TorrentInfoProvider.lambda$makePiecesFlowable$27(String,FlowableEmitter)` | OPEN | Flowable source in `TorrentInfoProvider.java:423-452`; subscription dispatch unresolved. |
| 16 | `TorrentInfoProvider.lambda$makeSessionStatsFlowable$30(TorrentEngineListener)` | OPEN | Session listener callback in `TorrentInfoProvider.java:478-488`; session event delivery unresolved. |
| 17 | `TorrentInfoProvider.lambda$makeSessionStatsFlowable$31(FlowableEmitter)` | OPEN | Flowable source in `TorrentInfoProvider.java:474-496`; Rx subscription dispatch unresolved. |
| 18 | `TorrentInfoProvider.lambda$makeTorrentsDeletedFlowable$28(TorrentEngineListener)` | OPEN | Listener callback in `TorrentInfoProvider.java:457-463`; torrent-removed event delivery unresolved. |
| 19 | `TorrentInfoProvider.lambda$makeTorrentsDeletedFlowable$29(FlowableEmitter)` | OPEN | Flowable source in `TorrentInfoProvider.java:455-471`; Rx subscription dispatch unresolved. |
| 20 | `TorrentInfoProvider.lambda$makeTrackersInfoFlowable$16(String,AtomicReference,FlowableEmitter,Long)` | OPEN | Timer callback in `TorrentInfoProvider.java:357-387`; Rx interval delivery unresolved. |
| 21 | `TorrentInfoProvider.lambda$makeTrackersInfoFlowable$17(String,Throwable)` | OPEN | Rx error consumer in `TorrentInfoProvider.java:361-374`; delivery unresolved. |
| 22 | `TorrentInfoProvider.lambda$makeTrackersInfoFlowable$18(AtomicReference,String,FlowableEmitter,Disposable)` | OPEN | Thread callback in `TorrentInfoProvider.java:375-385`; Flowable source execution unresolved. |
| 23 | `TorrentInfoProvider.lambda$makeTrackersInfoFlowable$19(String,FlowableEmitter)` | OPEN | Flowable source in `TorrentInfoProvider.java:357-387`; subscription dispatch unresolved. |
| 24 | `TorrentInfoProvider.makeAdvancedInfoFlowable(String)` | OPEN | `observeAdvancedInfo` delegates at `TorrentInfoProvider.java:106-108`; DetailTorrentViewModel and detail screen use it, but the entry route is not authored in graph_def.py. |
| 25 | `TorrentInfoProvider.makeInfoFlowable(String)` | OPEN | `observeInfo` delegates at `TorrentInfoProvider.java:94-96`; detail ViewModel/screen use it, but the entry route is not authored. |
| 26 | `TorrentInfoProvider.makeInfoListFlowable()` | OPEN | `observeInfoList` delegates at `TorrentInfoProvider.java:98-100`; MainViewModel and TorrentService use it, but the entry route is not authored. |
| 27 | `TorrentInfoProvider.makeInfoListSingle()` | OPEN | `getInfoListSingle` delegates at `TorrentInfoProvider.java:102-104`; service invocation is in the settings-change Rx chain (`TorrentService.java:264-275,314-319`), whose callback route is unresolved. |
| 28 | `TorrentInfoProvider.makePeersInfoFlowable(String)` | OPEN | `observePeersInfo` delegates at `TorrentInfoProvider.java:114-116`; detail ViewModel/screen use it, but the entry route is not authored. |
| 29 | `TorrentInfoProvider.makePiecesFlowable(String)` | OPEN | `observePiecesInfo` delegates at `TorrentInfoProvider.java:118-120`; detail ViewModel/screen use it, but the entry route is not authored. |
| 30 | `TorrentInfoProvider.makeSessionStatsFlowable()` | OPEN | `observeSessionStats` delegates at `TorrentInfoProvider.java:126-128`; MainActivity subscribes, but the entry route is not authored. |
| 31 | `TorrentInfoProvider.makeTorrentsDeletedFlowable()` | OPEN | `observeTorrentsDeleted` delegates at `TorrentInfoProvider.java:122-124`; main/detail activities subscribe, but the entry route is not authored. |
| 32 | `TorrentInfoProvider.makeTrackersInfoFlowable(String)` | OPEN | `observeTrackersInfo` delegates at `TorrentInfoProvider.java:110-112`; detail ViewModel/screen use it, but the entry route is not authored. |
| 33 | `TorrentInfoProvider.observeAdvancedInfo(String)` | OPEN | DetailTorrentViewModel calls at `:172-173` and detail screen subscribes; app-entry route is not authored. |
| 34 | `TorrentInfoProvider.observeInfo(String)` | OPEN | DetailTorrentViewModel calls at `:168-170` and detail screen subscribes; app-entry route is not authored. |
| 35 | `TorrentInfoProvider.observeInfoList()` | OPEN | MainViewModel and TorrentService call at `MainViewModel.java:77-79` and `TorrentService.java:282-284`; entry routes are not authored. |
| 36 | `TorrentInfoProvider.observePeersInfo(String)` | OPEN | DetailTorrentViewModel calls at `:180-185` and detail screen subscribes; app-entry route is not authored. |
| 37 | `TorrentInfoProvider.observePiecesInfo(String)` | OPEN | DetailTorrentViewModel calls at `:188-189` and detail screen subscribes; app-entry route is not authored. |
| 38 | `TorrentInfoProvider.observeSessionStats()` | OPEN | MainActivity subscribes at `MainActivity.java:456-460`; app-entry route is not authored. |
| 39 | `TorrentInfoProvider.observeTorrentsDeleted()` | OPEN | MainActivity and DetailTorrentActivity subscribe at `:446-448` and `DetailTorrentActivity.java:95-99`; entry routes are not authored. |
| 40 | `TorrentInfoProvider.observeTrackersInfo(String)` | OPEN | DetailTorrentViewModel calls at `:176-181` and detail screen subscribes; app-entry route is not authored. |

Totals: 40 rows = 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. No graph labels changed, so no graph build was run for this batch.
