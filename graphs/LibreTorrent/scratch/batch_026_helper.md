# LibreTorrent batch 26 helper audit

Membership comes only from `handoff/LIBRETORRENT_BATCH_PLAN.tsv`; it contains exactly 40 batch 26 rows. Printed plan rows, callback declarations, session dispatch sites, and callers are in `scratch/batch_026_helper_printed.txt`.

The five `TorrentEngine$5` overrides and `TorrentEngineListener` callbacks depend on session/event dispatch that this pass did not close; synthetic provider lambdas depend on Rx or listener delivery. Factory initialization and the base listener constructor have direct source routes. `getInfoListSingle` remains OPEN because app callers invoke it from Rx callbacks.

| # | Method | Finding | Evidence / route note |
|---:|---|---|---|
| 1 | `TorrentEngine$5.onTorrentFinished(String)` | OPEN | Registered engine listener override (`TorrentEngine.java:1306-1325`); torrent-finished event delivery through the session/task listener was not traced to a concrete app-triggered event. |
| 2 | `TorrentEngine$5.onTorrentLoaded(String)` | OPEN | Registered engine listener override (`TorrentEngine.java:1291-1303`); session restore/load event delivery not independently confirmed. |
| 3 | `TorrentEngine$5.onTorrentMetadataLoaded(String,Exception)` | OPEN | Registered engine listener override (`TorrentEngine.java:1420-1440`); callback delivery depends on metadata/session events. |
| 4 | `TorrentEngine$5.onTorrentMoved(String,boolean)` | OPEN | Registered engine listener override (`TorrentEngine.java:1348-1369`); move-event dispatch path not closed. |
| 5 | `TorrentEngine$5.onTorrentMoving(String)` | OPEN | Registered engine listener override (`TorrentEngine.java:1328-1345`); move-event dispatch path not closed. |
| 6 | `TorrentEngineListener.<init>()` | REACHABLE | `TorrentEngine` constructs its registered anonymous `engineListener` field (`TorrentEngine.java:1265-1270`) and registers it with the session in its constructor (`:130-141`), invoking the base constructor. |
| 7 | `TorrentEngineListener.onIpFilterParsed(int)` | OPEN | Default no-op callback (`TorrentEngineListener.java:54`); session can notify it after parsing (`TorrentSessionImpl.java:737-739`), but the listener event route is conditional and not fully traced. |
| 8 | `TorrentEngineListener.onMagnetLoaded(String,byte[])` | OPEN | Default no-op callback (`TorrentEngineListener.java:56`); session notification is at `TorrentSessionImpl.java:1165-1167`, driven by magnet metadata events not verified here. |
| 9 | `TorrentEngineListener.onNatError(String)` | OPEN | Default no-op callback (`TorrentEngineListener.java:66`); called from session error callback (`TorrentSessionImpl.java:1135-1137`), whose external event trigger is not established. |
| 10 | `TorrentEngineListener.onPieceFinished(String,int)` | OPEN | Default no-op callback (`TorrentEngineListener.java:70`); no app-source call site was found in this pass; session/native callback route remains unverified. |
| 11 | `TorrentEngineListener.onReadPiece(String,ReadPieceInfo)` | OPEN | Default no-op callback (`TorrentEngineListener.java:68`); no app-source call site was found in this pass; session/native callback route remains unverified. |
| 12 | `TorrentEngineListener.onRestoreSessionError(String)` | OPEN | Default no-op callback (`TorrentEngineListener.java:60`); session calls listeners during restore (`TorrentSessionImpl.java:1527-1529`), but error branch/event route is unresolved. |
| 13 | `TorrentEngineListener.onSessionError(String)` | OPEN | Default no-op callback (`TorrentEngineListener.java:64`); session calls it from error callbacks (`TorrentSessionImpl.java:1119-1128`), with trigger depending on session/library events. |
| 14 | `TorrentEngineListener.onSessionStarted()` | OPEN | Default no-op callback (`TorrentEngineListener.java:46`); session schedules notification from `onAfterStart` (`TorrentSessionImpl.java:1006-1012`), whose callback route depends on session startup. |
| 15 | `TorrentEngineListener.onSessionStats(SessionStats)` | OPEN | Default no-op callback (`TorrentEngineListener.java:72`); session notification is at `TorrentSessionImpl.java:1173-1175`; stats dispatch was not independently traced to an app entry. |
| 16 | `TorrentEngineListener.onSessionStopped()` | OPEN | Default no-op callback (`TorrentEngineListener.java:48`); session notification is at `TorrentSessionImpl.java:1041-1045`, downstream of session stop. |
| 17 | `TorrentEngineListener.onTorrentAdded(String)` | OPEN | Default no-op callback (`TorrentEngineListener.java:30`); session calls it during add/restore (`TorrentSessionImpl.java:1084-1088`), but source path into that event is not fully closed. |
| 18 | `TorrentEngineListener.onTorrentError(String,Exception)` | OPEN | Default no-op callback (`TorrentEngineListener.java:62`); no complete app-source event route was confirmed. |
| 19 | `TorrentEngineListener.onTorrentFinished(String)` | OPEN | Default no-op callback (`TorrentEngineListener.java:38`); completion dispatch depends on task/session event delivery. |
| 20 | `TorrentEngineListener.onTorrentLoaded(String)` | OPEN | Default no-op callback (`TorrentEngineListener.java:32`); session calls it during restore/load (`TorrentSessionImpl.java:1084-1088`), but source route into the event is unresolved. |
| 21 | `TorrentEngineListener.onTorrentMetadataLoaded(String,Exception)` | OPEN | Default no-op callback (`TorrentEngineListener.java:58`); metadata callback is session/library-driven and not traced end to end. |
| 22 | `TorrentEngineListener.onTorrentMoved(String,boolean)` | OPEN | Default no-op callback (`TorrentEngineListener.java:52`); move completion dispatch was not source-closed. |
| 23 | `TorrentEngineListener.onTorrentMoving(String)` | OPEN | Default no-op callback (`TorrentEngineListener.java:50`); move-start dispatch was not source-closed. |
| 24 | `TorrentEngineListener.onTorrentPaused(String)` | OPEN | Default no-op callback (`TorrentEngineListener.java:42`); pause event delivery depends on session/task callbacks. |
| 25 | `TorrentEngineListener.onTorrentRemoved(String)` | OPEN | Default no-op callback (`TorrentEngineListener.java:40`); a source call exists in session remove flow (`TorrentSessionImpl.java:388-390`), but the complete entry-to-removal path is not in this audit. |
| 26 | `TorrentEngineListener.onTorrentResumed(String)` | OPEN | Default no-op callback (`TorrentEngineListener.java:44`); resume event delivery depends on session/task callbacks. |
| 27 | `TorrentEngineListener.onTorrentStateChanged(String,TorrentStateCode,TorrentStateCode)` | OPEN | Default no-op callback (`TorrentEngineListener.java:34-36`); no complete app-source event path was established. |
| 28 | `TorrentInfoProvider.<clinit>()` | REACHABLE | Static initialization of `INSTANCE` occurs when app source first invokes `TorrentInfoProvider.getInstance`; call sites include `MainActivity` and `TorrentService` (call-site output in printed evidence). |
| 29 | `TorrentInfoProvider.<init>(TorrentEngine,TagRepository)` | REACHABLE | Both `getInstance` factories construct the provider (`TorrentInfoProvider.java:63-92`); the Context factory is called by `MainActivity`, `TorrentService`, and detail UI. |
| 30 | `TorrentInfoProvider.getInfoListSingle()` | OPEN | Called through MainViewModel/MainFragment and TorrentService (`MainViewModel.java:81-83`; service lines in printed evidence); actual caller is in an Rx callback chain. |
| 31 | `TorrentInfoProvider.getInstance(Context)` | REACHABLE | App call sites in `MainActivity`, `TorrentService`, and detail UI invoke the Context factory (`TorrentInfoProvider.java:76-87` plus printed caller search). |
| 32 | `TorrentInfoProvider.lambda$makeAdvancedInfoFlowable$12(String,AtomicReference,FlowableEmitter,Long)` | OPEN | Interval callback inside `makeAdvancedInfoFlowable` (`TorrentInfoProvider.java:323-355`); Rx timer delivery is external to source. |
| 33 | `TorrentInfoProvider.lambda$makeAdvancedInfoFlowable$13(String,Throwable)` | OPEN | Rx error consumer in `makeAdvancedInfoFlowable` (`TorrentInfoProvider.java:327-339`); error callback delivery not verified. |
| 34 | `TorrentInfoProvider.lambda$makeAdvancedInfoFlowable$14(String,AtomicReference,FlowableEmitter,Disposable)` | OPEN | Thread callback in `makeAdvancedInfoFlowable` (`TorrentInfoProvider.java:340-352`); outer Flowable source dispatch is Rx-driven. |
| 35 | `TorrentInfoProvider.lambda$makeAdvancedInfoFlowable$15(String,FlowableEmitter)` | OPEN | `Flowable.create` source in `makeAdvancedInfoFlowable` (`TorrentInfoProvider.java:323-355`); Rx invokes it on subscription. |
| 36 | `TorrentInfoProvider.lambda$makeInfoFlowable$0(String,AtomicReference,FlowableEmitter,String)` | OPEN | Event consumer inside `makeInfoFlowable` (`TorrentInfoProvider.java:130-145`); it is called from listener/tag observation callbacks. |
| 37 | `TorrentInfoProvider.lambda$makeInfoFlowable$1(TorrentEngineListener)` | OPEN | Listener-disposal cleanup (`TorrentInfoProvider.java:206-230`); invocation depends on Rx disposal. |
| 38 | `TorrentInfoProvider.lambda$makeInfoFlowable$2(Consumer,String,FlowableEmitter,List)` | OPEN | Tag repository subscription callback (`TorrentInfoProvider.java:219-228`); Rx delivery not verified. |
| 39 | `TorrentInfoProvider.lambda$makeInfoFlowable$3(String,AtomicReference,FlowableEmitter,TorrentEngineListener,Consumer)` | OPEN | Thread callback (`TorrentInfoProvider.java:206-232`); Flowable source must execute first. |
| 40 | `TorrentInfoProvider.lambda$makeInfoFlowable$4(String,FlowableEmitter)` | OPEN | `Flowable.create` source in `makeInfoFlowable` (`TorrentInfoProvider.java:130-235`); Rx invokes it on subscription. |

Totals: 40 rows = 4 REACHABLE, 0 UNREACHABLE, 36 OPEN. OPEN callback entries were not labeled from generator candidates or coverage. No graph, notes, output, or coverage files were changed.
