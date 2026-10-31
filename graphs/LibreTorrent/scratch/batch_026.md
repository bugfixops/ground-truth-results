# LibreTorrent batch 26 source audit

Membership is the 40 rows in `scratch/batch_026_plan.txt`. I independently re-read the corrected source excerpts in `scratch/batch_026_helper_printed.txt` against the Java files listed below.

The helper proposed four locally reachable labels (the base listener constructor, provider class initialization and constructor, and the Context factory). These findings establish local construction/call sites, but the required route from an app entry point, with every step represented by hand-authored edges, is not present. I left those methods OPEN. The remaining callbacks depend on session/library dispatch, and provider lambdas depend on Rx, listener or thread dispatch. Those methods also remain OPEN until the full entry route and required dispatch edges are printed and authored. No method is labeled from a generator candidate or coverage.

| # | Method | Label | Evidence / reason |
|---:|---|---|---|
| 1 | `TorrentEngine$5.onTorrentFinished(String)` | OPEN | Engine listener override at `TorrentEngine.java:1306-1325`; session/task event route not closed. |
| 2 | `TorrentEngine$5.onTorrentLoaded(String)` | OPEN | Override at `TorrentEngine.java:1291-1303`; restore/load event route not closed. |
| 3 | `TorrentEngine$5.onTorrentMetadataLoaded(String,Exception)` | OPEN | Override at `TorrentEngine.java:1420-1440`; metadata callback dispatch not closed. |
| 4 | `TorrentEngine$5.onTorrentMoved(String,boolean)` | OPEN | Override at `TorrentEngine.java:1348-1369`; move event route not closed. |
| 5 | `TorrentEngine$5.onTorrentMoving(String)` | OPEN | Override at `TorrentEngine.java:1328-1345`; move event route not closed. |
| 6 | `TorrentEngineListener.<init>()` | OPEN | `TorrentEngine.java:1265-1270` constructs the listener, but a complete entry-to-engine route is not represented in hand-authored edges. |
| 7 | `TorrentEngineListener.onIpFilterParsed(int)` | OPEN | Session notification at `TorrentSessionImpl.java:737-739`; triggering event route is not closed. |
| 8 | `TorrentEngineListener.onMagnetLoaded(String,byte[])` | OPEN | Session notification at `TorrentSessionImpl.java:1165-1167`; event source is not closed. |
| 9 | `TorrentEngineListener.onNatError(String)` | OPEN | Session callback at `TorrentSessionImpl.java:1135-1137`; external event trigger is not closed. |
| 10 | `TorrentEngineListener.onPieceFinished(String,int)` | OPEN | No app-source call found; native/session dispatch route remains unresolved. |
| 11 | `TorrentEngineListener.onReadPiece(String,ReadPieceInfo)` | OPEN | No app-source call found; native/session dispatch route remains unresolved. |
| 12 | `TorrentEngineListener.onRestoreSessionError(String)` | OPEN | Session notification at `TorrentSessionImpl.java:1527-1529`; error branch route not closed. |
| 13 | `TorrentEngineListener.onSessionError(String)` | OPEN | Session callback at `TorrentSessionImpl.java:1119-1128`; triggering event route not closed. |
| 14 | `TorrentEngineListener.onSessionStarted()` | OPEN | Scheduled from session `onAfterStart` at `TorrentSessionImpl.java:1006-1012`; app entry route not closed. |
| 15 | `TorrentEngineListener.onSessionStats(SessionStats)` | OPEN | Session notification at `TorrentSessionImpl.java:1173-1175`; event route not closed. |
| 16 | `TorrentEngineListener.onSessionStopped()` | OPEN | Session notification at `TorrentSessionImpl.java:1041-1045`; session-stop route not closed. |
| 17 | `TorrentEngineListener.onTorrentAdded(String)` | OPEN | Session notification at `TorrentSessionImpl.java:1084-1088`; add/restore route not closed. |
| 18 | `TorrentEngineListener.onTorrentError(String,Exception)` | OPEN | No complete app-source event route established. |
| 19 | `TorrentEngineListener.onTorrentFinished(String)` | OPEN | Completion dispatch depends on task/session events; route not closed. |
| 20 | `TorrentEngineListener.onTorrentLoaded(String)` | OPEN | Session notification at `TorrentSessionImpl.java:1084-1088`; restore/load route not closed. |
| 21 | `TorrentEngineListener.onTorrentMetadataLoaded(String,Exception)` | OPEN | Metadata callback dispatch is session/library-driven; route not closed. |
| 22 | `TorrentEngineListener.onTorrentMoved(String,boolean)` | OPEN | Move completion dispatch route not closed. |
| 23 | `TorrentEngineListener.onTorrentMoving(String)` | OPEN | Move-start dispatch route not closed. |
| 24 | `TorrentEngineListener.onTorrentPaused(String)` | OPEN | Pause callback route through session/task events not closed. |
| 25 | `TorrentEngineListener.onTorrentRemoved(String)` | OPEN | Session remove call at `TorrentSessionImpl.java:388-390`; complete entry-to-removal route not represented. |
| 26 | `TorrentEngineListener.onTorrentResumed(String)` | OPEN | Resume callback route through session/task events not closed. |
| 27 | `TorrentEngineListener.onTorrentStateChanged(String,TorrentStateCode,TorrentStateCode)` | OPEN | No complete app-source event route established. |
| 28 | `TorrentInfoProvider.<clinit>()` | OPEN | App code calls `getInstance`, but the entry-to-call route is not represented in hand-authored edges. |
| 29 | `TorrentInfoProvider.<init>(TorrentEngine,TagRepository)` | OPEN | Factory methods invoke the constructor at `TorrentInfoProvider.java:63-92`; entry route not represented. |
| 30 | `TorrentInfoProvider.getInfoListSingle()` | OPEN | Callers include `MainViewModel.java:81-83` and `TorrentService.java:298-299`; invocation is in an Rx chain and its entry route is not closed. |
| 31 | `TorrentInfoProvider.getInstance(Context)` | OPEN | App callers include `MainActivity`, `TorrentService`, and detail UI; full entry route not represented in hand-authored edges. |
| 32 | `TorrentInfoProvider.lambda$makeAdvancedInfoFlowable$12(String,AtomicReference,FlowableEmitter,Long)` | OPEN | Interval callback inside `makeAdvancedInfoFlowable`; Rx timer delivery not established. |
| 33 | `TorrentInfoProvider.lambda$makeAdvancedInfoFlowable$13(String,Throwable)` | OPEN | Rx error consumer; callback delivery not established. |
| 34 | `TorrentInfoProvider.lambda$makeAdvancedInfoFlowable$14(String,AtomicReference,FlowableEmitter,Disposable)` | OPEN | Thread callback under an Rx Flowable source; route not closed. |
| 35 | `TorrentInfoProvider.lambda$makeAdvancedInfoFlowable$15(String,FlowableEmitter)` | OPEN | Flowable source lambda invoked on subscription; Rx dispatch route not established. |
| 36 | `TorrentInfoProvider.lambda$makeInfoFlowable$0(String,AtomicReference,FlowableEmitter,String)` | OPEN | Event consumer called by listener/tag observation callbacks; dispatch not established. |
| 37 | `TorrentInfoProvider.lambda$makeInfoFlowable$1(TorrentEngineListener)` | OPEN | Listener-disposal cleanup callback; Rx disposal route not established. |
| 38 | `TorrentInfoProvider.lambda$makeInfoFlowable$2(Consumer,String,FlowableEmitter,List)` | OPEN | Tag-repository subscription callback; Rx delivery not established. |
| 39 | `TorrentInfoProvider.lambda$makeInfoFlowable$3(String,AtomicReference,FlowableEmitter,TorrentEngineListener,Consumer)` | OPEN | Thread callback under an Rx Flowable source; route not closed. |
| 40 | `TorrentInfoProvider.lambda$makeInfoFlowable$4(String,FlowableEmitter)` | OPEN | Flowable source lambda invoked on subscription; Rx dispatch route not established. |

Totals: 40 rows = 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. No graph labels were changed, so no graph build was run for this batch.
