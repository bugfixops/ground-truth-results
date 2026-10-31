# LibreTorrent batch 72 source audit

Membership is exactly the 40 batch 72 rows printed at the top of `batch_072_helper_printed.txt`. Evidence is bounded to Scheduler, TorrentService lifecycle/intent/notification excerpts, BaseAlertDialog, the manifest service declaration, and a caller search. I leave all rows OPEN because this pass has not read every branch from service entry through each target; framework lifecycle delivery, notification/alarm dispatch, and Rx callback dispatch also need their individual edges checked. Local calls in the service are not complete entry routes. No UNREACHABLE label is inferred from a missing caller.

| # | Method | Finding | Printed evidence / unresolved route |
|---:|---|---|---|
| 1 | `Scheduler.setStopAppAlarm(Context,int)boolean` | OPEN | `Scheduler.java:56+`; method and callers printed; alarm delivery and full user/scheduler route unresolved. |
| 2 | `TorrentService.<clinit>()V` | OPEN | Service class/static setup printed; class initialization from a service entry not traced. |
| 3 | `TorrentService.<init>()V` | OPEN | Service source printed; Android service instantiation/framework route unresolved. |
| 4 | `TorrentService.forceClearForeground()V` | OPEN | `TorrentService.java:329+`; callers printed; complete teardown entry route unresolved. |
| 5 | `TorrentService.getInfoListSingle()Disposable` | OPEN | `TorrentService.java:298+`; Rx chain printed; full subscription/error callback route unresolved. |
| 6 | `TorrentService.handleActions(String)V` | OPEN | `TorrentService.java:214+`; intent dispatch branch printed; full service-start entry route unresolved. |
| 7 | `TorrentService.handleSettingsChanged(String)V` | OPEN | `TorrentService.java:264+`; observer subscription printed; Rx event route unresolved. |
| 8 | `TorrentService.handleShutdownActions(String)int` | OPEN | `TorrentService.java:199+`; start-command dispatch printed; framework/intent route unresolved. |
| 9 | `TorrentService.init()V` | OPEN | `TorrentService.java:116+`; `onCreate` call printed; full Android service creation route unresolved. |
| 10 | `TorrentService.initPendingIntents()V` | OPEN | `TorrentService.java:112+` and helper body printed; notification action dispatch route unresolved. |
| 11 | `TorrentService.lambda$forceClearForeground$7()V` | OPEN | Lambda source printed near foreground teardown; Rx scheduling/execution dispatch unresolved. |
| 12 | `TorrentService.lambda$getInfoListSingle$2(List)SingleSource` | OPEN | Lambda source printed in list/notification chain; Rx callback dispatch unresolved. |
| 13 | `TorrentService.lambda$getInfoListSingle$3(Throwable)V` | OPEN | Error lambda source printed; Rx error delivery route unresolved. |
| 14 | `TorrentService.lambda$startUpdateForegroundNotify$0(List)SingleSource` | OPEN | Lambda source printed in foreground update chain; Rx dispatch unresolved. |
| 15 | `TorrentService.lambda$startUpdateForegroundNotify$1(Throwable)V` | OPEN | Error lambda source printed; Rx error delivery route unresolved. |
| 16 | `TorrentService.lambda$subscribeCombinedPauseButtonState$6(Boolean)V` | OPEN | Observer lambda printed; Observable subscription/delivery route unresolved. |
| 17 | `TorrentService.lambda$subscribeForceSortAndFilter$4(Boolean)boolean` | OPEN | Filter lambda printed; observable/filter dispatch route unresolved. |
| 18 | `TorrentService.lambda$subscribeForceSortAndFilter$5(Boolean)V` | OPEN | Observer lambda printed; Observable subscription/delivery route unresolved. |
| 19 | `TorrentService.makeDetailNotifyInboxStyle(List)InboxStyle` | OPEN | `TorrentService.java:398+`; notification formatting body printed; complete notification update path unresolved. |
| 20 | `TorrentService.makeForegroundNotify()V` | OPEN | `TorrentService.java:342+`; create/update callers printed; service entry route unresolved. |
| 21 | `TorrentService.onBind(Intent)IBinder` | OPEN | `TorrentService.java:100+`; override body printed; framework bind callback route unresolved. |
| 22 | `TorrentService.onCreate()V` | OPEN | `TorrentService.java:106+`; manifest service and override printed; framework service callback route unresolved. |
| 23 | `TorrentService.onDestroy()V` | OPEN | `TorrentService.java:143+`; override body printed; framework/service teardown route unresolved. |
| 24 | `TorrentService.onStartCommand(Intent,int,int)int` | OPEN | `TorrentService.java:176+`; intent/action branches printed; framework start callback and intent entry route unresolved. |
| 25 | `TorrentService.setFilterAndSorting()V` | OPEN | `TorrentService.java:137+`; initialization/settings callers printed; complete settings event route unresolved. |
| 26 | `TorrentService.setForegroundNotifyActions(boolean)V` | OPEN | `TorrentService.java:455+`; notification builder callers printed; UI/notification entry route unresolved. |
| 27 | `TorrentService.setKeepCpuAwake(boolean)V` | OPEN | `TorrentService.java:235+`; lifecycle/settings callers printed; service state route unresolved. |
| 28 | `TorrentService.shutdown()V` | OPEN | `TorrentService.java:150+`; lifecycle callers printed; service shutdown entry route unresolved. |
| 29 | `TorrentService.startUpdateForegroundNotify()V` | OPEN | `TorrentService.java:277+`; initialization callers printed; complete service-entry/Rx route unresolved. |
| 30 | `TorrentService.stopEngine()V` | OPEN | `TorrentService.java:157+`; shutdown caller printed; complete teardown entry route unresolved. |
| 31 | `TorrentService.stopService()V` | OPEN | `TorrentService.java:164+`; shutdown/callback callers printed; service stop dispatch route unresolved. |
| 32 | `TorrentService.stopUpdateForegroundNotify()V` | OPEN | `TorrentService.java:336+`; update callers printed; full Rx/service lifecycle route unresolved. |
| 33 | `TorrentService.subscribeCombinedPauseButtonState()V` | OPEN | `TorrentService.java:321+`; observer setup printed; state-change subscription/delivery route unresolved. |
| 34 | `TorrentService.subscribeForceSortAndFilter()V` | OPEN | `TorrentService.java:314+`; observer setup printed; state-change subscription/delivery route unresolved. |
| 35 | `TorrentService.updateForegroundNotify(List)V` | OPEN | `TorrentService.java:368+`; Rx callers and body printed; complete notification event path unresolved. |
| 36 | `TorrentService.updateForegroundNotifyActions(boolean)V` | OPEN | `TorrentService.java:492+`; settings/observer callers printed; complete action route unresolved. |
| 37 | `TorrentService$1.<init>(TorrentService)V` | OPEN | Anonymous listener construction printed in service source; service/session registration route unresolved. |
| 38 | `TorrentService$1.onSessionStopped()V` | OPEN | Listener callback body and registration context printed; session callback dispatch route unresolved. |
| 39 | `BaseAlertDialog.<clinit>()V` | OPEN | `BaseAlertDialog.java` static setup printed; dialog class initialization route not traced. |
| 40 | `BaseAlertDialog.<init>()V` | OPEN | Constructor and factory/caller context printed; complete dialog navigation route unresolved. |

Count: 40 plan rows = 40 OPEN, 0 REACHABLE labels, 0 UNREACHABLE labels. No graph edits or coverage evidence were used.
