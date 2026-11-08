# Proposed service, engine, session, and notification routes (audit 2)

Scope: read-only review of existing source-backed S3 route reports and printed application/AOSP source evidence. This is a proposed route audit, not graph authoring.

## Findings and edge proposals

1. **Boot-to-service start**: retain/propose `BootReceiver.onReceive -> TorrentEngine.getInstance -> TorrentEngine.start -> Utils.startServiceBackground -> Context.startForegroundService` for Android O+ and `Context.startService` for earlier API levels, gated by boot action and `pref.autostart() && pref.keepAlive()`. Receiver event entry is `ENV system_event`; the preference branch is state-dependent. AOSP service creation then dispatches `TorrentService.onCreate`; service args dispatch `onStartCommand`. Evidence: `s3_service_route_printed.txt` and `build_s3_torrent_service.txt`.

2. **Service first start/action handling**: propose `TorrentService.onCreate -> initPendingIntents -> makeForegroundNotify`; on first `onStartCommand`, `compareAndSet(false,true)` gates `init()`, which obtains repositories/providers, sets notification/observers/receiver state, calls `engine.doStart`, registers `engineListener`, and starts foreground updates. Shutdown actions can return before init; remaining actions dispatch only after the first-start branch. AOSP `handleCreateService` invokes `onCreate`; `handleServiceArgs` invokes `onStartCommand`.

3. **Notification button delivery**: propose `TorrentService.initPendingIntents -> PendingIntent.getBroadcast` registrations to `NotificationReceiver.onReceive` for shutdown, pause, resume, and pause/resume. Delivery is an ENV `system_event` route from notification activation; AOSP broadcast dispatch prints receiver construction and `onReceive`. Receiver action branches call `Context.startService(TorrentService)` with matching action; shutdown and add-torrent branches also start `MainActivity` with the corresponding action. Service dispatch then reaches `onStartCommand`. Scheduled notification refresh is separate and needs a time/event gate; Rx observer delivery remains unproven absent library source.

4. **Engine/session startup and persistence**: `TorrentService.init -> TorrentEngine.doStart` is printed, but downstream session initialization, loading, and native alert-loop dispatch must remain OPEN unless separately evidenced. Printed batch source shows local `TorrentEngine` and `TorrentSessionImpl` calls, but call sites alone do not establish full entry to each method. In particular, `TorrentSessionImpl$InnerListener.alert -> newTask` depends on native libtorrent alert delivery; keep unresolved pending direct callback registration/dispatch proof. Worker/native thread execution is not a direct same-thread call.

5. **Add-torrent path**: app submission evidence links UI submit worker to `TorrentEngine.addTorrentSync`; batch 003 prints `TorrentEngine.addTorrent(...) -> TorrentSessionImpl.addTorrent(...)` and repo persistence. This establishes only source-backed calls along the shown branch. Preserve magnet/decoded-torrent state gates; do not promote all session methods or generated callback lambdas from this partial route.

## Route status

Strongly supported by printed source: service component creation/start lifecycle; explicit PendingIntent registrations; notification receiver action-to-activity/service intent creation; BootReceiver condition and service-start helper; shown engine/session add-torrent local calls.

Remain OPEN or conditional: asynchronous Handler execution; Rx subscriptions and observer callbacks in TorrentService; service-to-engine listener callback dispatch; session/native alert callback dispatch (including `InnerListener.alert -> newTask`); load-torrents/task callback chains; blanket reachability of engine/session methods from a call site or coverage. Existing notes state native alert/thread routes remain incomplete; coverage must not supply route evidence.

No graph, labels, build outputs, or AGENT_NOTES were changed.
