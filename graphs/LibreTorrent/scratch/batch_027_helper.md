# LibreTorrent batch 27 helper audit

Membership comes only from `handoff/LIBRETORRENT_BATCH_PLAN.tsv`; it contains exactly 40 batch 27 rows. Printed plan rows, provider implementations, and app callers are in `scratch/batch_027_helper_printed.txt`.

The 23 synthetic lambda methods are OPEN because their bodies are invoked through Rx subscription, emitter, listener, timer, or disposal callbacks. The observable factory and public observation methods are REACHABLE where the app source shows direct UI or service calls. `makeInfoListSingle` remains OPEN because its only call route is the settings-change Rx chain in `TorrentService`.

| # | Method | Finding | Evidence / route note |
|---:|---|---|---|
| 1 | `TorrentInfoProvider.lambda$makeInfoListFlowable$5(AtomicReference,FlowableEmitter)` | OPEN | Captured update runnable in `TorrentInfoProvider.java:242-250`; it is invoked from session listener and tag-observer callbacks (`:253-285,298-300`), whose delivery remains open. |
| 2 | `TorrentInfoProvider.lambda$makeInfoListFlowable$6(TorrentEngineListener)` | OPEN | Listener-disposal cleanup in `TorrentInfoProvider.java:287-307`; invoked on Rx disposal. |
| 3 | `TorrentInfoProvider.lambda$makeInfoListFlowable$7(Runnable,List)` | OPEN | Asynchronous update callback in `TorrentInfoProvider.java:238-307`; callback execution depends on the listener/Rx source. |
| 4 | `TorrentInfoProvider.lambda$makeInfoListFlowable$8(AtomicReference,FlowableEmitter,TorrentEngineListener,Runnable)` | OPEN | Thread callback inside the Flowable source (`TorrentInfoProvider.java:287-305`); triggered when Rx subscribes. |
| 5 | `TorrentInfoProvider.lambda$makeInfoListFlowable$9(FlowableEmitter)` | OPEN | `Flowable.create` source in `TorrentInfoProvider.java:238-308`; Rx source callback runs on subscription. |
| 6 | `TorrentInfoProvider.lambda$makeInfoListSingle$10(SingleEmitter)` | OPEN | `Single.create` source in `TorrentInfoProvider.java:310-320`; Rx subscription invokes it. |
| 7 | `TorrentInfoProvider.lambda$makeInfoListSingle$11(SingleEmitter)` | OPEN | Thread callback in the `Single.create` source (`TorrentInfoProvider.java:313-319`); depends on Rx source execution. |
| 8 | `TorrentInfoProvider.lambda$makePeersInfoFlowable$20(String,AtomicReference,FlowableEmitter,Long)` | OPEN | Timer/onNext callback in `TorrentInfoProvider.java:390-420`; interval subscription dispatch not source-closed. |
| 9 | `TorrentInfoProvider.lambda$makePeersInfoFlowable$21(String,Throwable)` | OPEN | Rx error consumer registered in `TorrentInfoProvider.java:394-406`; error delivery depends on Rx. |
| 10 | `TorrentInfoProvider.lambda$makePeersInfoFlowable$22(AtomicReference,String,FlowableEmitter,Disposable)` | OPEN | Thread callback in `TorrentInfoProvider.java:408-418`; depends on Flowable source execution. |
| 11 | `TorrentInfoProvider.lambda$makePeersInfoFlowable$23(String,FlowableEmitter)` | OPEN | `Flowable.create` source in `TorrentInfoProvider.java:390-420`; Rx source callback runs on subscription. |
| 12 | `TorrentInfoProvider.lambda$makePiecesFlowable$24(String,AtomicReference,FlowableEmitter,Long)` | OPEN | Timer/onNext callback in `TorrentInfoProvider.java:423-452`; interval subscription dispatch not source-closed. |
| 13 | `TorrentInfoProvider.lambda$makePiecesFlowable$25(String,Throwable)` | OPEN | Rx error consumer registered in `TorrentInfoProvider.java:427-438`; error delivery depends on Rx. |
| 14 | `TorrentInfoProvider.lambda$makePiecesFlowable$26(AtomicReference,String,FlowableEmitter,Disposable)` | OPEN | Thread callback in `TorrentInfoProvider.java:440-450`; depends on Flowable source execution. |
| 15 | `TorrentInfoProvider.lambda$makePiecesFlowable$27(String,FlowableEmitter)` | OPEN | `Flowable.create` source in `TorrentInfoProvider.java:423-452`; Rx source callback runs on subscription. |
| 16 | `TorrentInfoProvider.lambda$makeSessionStatsFlowable$30(TorrentEngineListener)` | OPEN | Session listener callback in `TorrentInfoProvider.java:478-488`; event delivery from session was not confirmed. |
| 17 | `TorrentInfoProvider.lambda$makeSessionStatsFlowable$31(FlowableEmitter)` | OPEN | `Flowable.create` source in `TorrentInfoProvider.java:474-496`; Rx source callback runs on subscription. |
| 18 | `TorrentInfoProvider.lambda$makeTorrentsDeletedFlowable$28(TorrentEngineListener)` | OPEN | Listener callback in `TorrentInfoProvider.java:457-463`; torrent-removed event dispatch was not confirmed. |
| 19 | `TorrentInfoProvider.lambda$makeTorrentsDeletedFlowable$29(FlowableEmitter)` | OPEN | `Flowable.create` source in `TorrentInfoProvider.java:455-471`; Rx source callback runs on subscription. |
| 20 | `TorrentInfoProvider.lambda$makeTrackersInfoFlowable$16(String,AtomicReference,FlowableEmitter,Long)` | OPEN | Timer/onNext callback in `TorrentInfoProvider.java:357-387`; interval subscription dispatch not source-closed. |
| 21 | `TorrentInfoProvider.lambda$makeTrackersInfoFlowable$17(String,Throwable)` | OPEN | Rx error consumer registered in `TorrentInfoProvider.java:361-374`; error delivery depends on Rx. |
| 22 | `TorrentInfoProvider.lambda$makeTrackersInfoFlowable$18(AtomicReference,String,FlowableEmitter,Disposable)` | OPEN | Thread callback in `TorrentInfoProvider.java:375-385`; depends on Flowable source execution. |
| 23 | `TorrentInfoProvider.lambda$makeTrackersInfoFlowable$19(String,FlowableEmitter)` | OPEN | `Flowable.create` source in `TorrentInfoProvider.java:357-387`; Rx source callback runs on subscription. |
| 24 | `TorrentInfoProvider.makeAdvancedInfoFlowable(String)` | REACHABLE | Called directly by `observeAdvancedInfo` (`TorrentInfoProvider.java:106-108`); `DetailTorrentViewModel` exposes it and `DetailTorrentFragment` subscribes (`DetailTorrentViewModel.java:168-173`; fragment lines in printed evidence). |
| 25 | `TorrentInfoProvider.makeInfoFlowable(String)` | REACHABLE | Called directly by `observeInfo` (`TorrentInfoProvider.java:94-96`); `DetailTorrentViewModel` exposes it and the detail fragment subscribes (`DetailTorrentViewModel.java:168-170`). |
| 26 | `TorrentInfoProvider.makeInfoListFlowable()` | REACHABLE | Called by `observeInfoList` (`TorrentInfoProvider.java:98-100`); main ViewModel and TorrentService call that public method (`MainViewModel.java:77-79`; `TorrentService.java:282-284`). |
| 27 | `TorrentInfoProvider.makeInfoListSingle()` | OPEN | Called by `getInfoListSingle` (`TorrentInfoProvider.java:102-104`); service reaches it from the settings-change Rx chain (`TorrentService.java:264-275,314-319`), whose callback dispatch is unverified. |
| 28 | `TorrentInfoProvider.makePeersInfoFlowable(String)` | REACHABLE | Called directly by `observePeersInfo` (`TorrentInfoProvider.java:114-116`); detail ViewModel and fragment use that observation (`DetailTorrentViewModel.java:180-185`). |
| 29 | `TorrentInfoProvider.makePiecesFlowable(String)` | REACHABLE | Called directly by `observePiecesInfo` (`TorrentInfoProvider.java:118-120`); detail ViewModel and fragment use that observation (`DetailTorrentViewModel.java:188-189`). |
| 30 | `TorrentInfoProvider.makeSessionStatsFlowable()` | REACHABLE | Called directly by `observeSessionStats` (`TorrentInfoProvider.java:126-128`); `MainActivity` subscribes (`MainActivity.java:456-460`). |
| 31 | `TorrentInfoProvider.makeTorrentsDeletedFlowable()` | REACHABLE | Called directly by `observeTorrentsDeleted` (`TorrentInfoProvider.java:122-124`); main and detail activities subscribe (`MainActivity.java:446-448`; `DetailTorrentActivity.java:95-99`). |
| 32 | `TorrentInfoProvider.makeTrackersInfoFlowable(String)` | REACHABLE | Called directly by `observeTrackersInfo` (`TorrentInfoProvider.java:110-112`); detail ViewModel and fragment use the observation (`DetailTorrentViewModel.java:176-181`). |
| 33 | `TorrentInfoProvider.observeAdvancedInfo(String)` | REACHABLE | Direct ViewModel bridge to provider (`DetailTorrentViewModel.java:172-173`), subscribed by the detail screen. |
| 34 | `TorrentInfoProvider.observeInfo(String)` | REACHABLE | Direct ViewModel bridge to provider (`DetailTorrentViewModel.java:168-170`), subscribed by the detail screen. |
| 35 | `TorrentInfoProvider.observeInfoList()` | REACHABLE | Main ViewModel and service call it (`MainViewModel.java:77-79`; `TorrentService.java:282-284`). |
| 36 | `TorrentInfoProvider.observePeersInfo(String)` | REACHABLE | Direct ViewModel bridge (`DetailTorrentViewModel.java:180-185`), subscribed by the detail screen. |
| 37 | `TorrentInfoProvider.observePiecesInfo(String)` | REACHABLE | Direct ViewModel bridge (`DetailTorrentViewModel.java:188-189`), subscribed by the detail screen. |
| 38 | `TorrentInfoProvider.observeSessionStats()` | REACHABLE | `MainActivity` subscribes directly (`MainActivity.java:456-460`). |
| 39 | `TorrentInfoProvider.observeTorrentsDeleted()` | REACHABLE | Main and detail activities subscribe (`MainActivity.java:446-448`; `DetailTorrentActivity.java:95-99`). |
| 40 | `TorrentInfoProvider.observeTrackersInfo(String)` | REACHABLE | Direct ViewModel bridge (`DetailTorrentViewModel.java:176-181`), subscribed by the detail screen. |

Totals: 40 rows = 16 REACHABLE, 0 UNREACHABLE, 24 OPEN. OPEN lambda methods are not labeled from generator candidates or coverage data. No graph, notes, output, or coverage files were changed.
