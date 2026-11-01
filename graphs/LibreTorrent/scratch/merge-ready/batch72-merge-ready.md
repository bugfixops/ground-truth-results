**REVISION 2026-11-01 (OPEN-closing round 2, G12): no label changed. Row 21 (TorrentService.onBind) re-checked against a SAVED full-tree grep over all 252 app Java files in ~/workspace/ruleF-src/ (`~/workspace/b727374-openclose2-src/full_grep_bindservice_20261101.txt`: 0 bindService / 0 unbindService / 0 ServiceConnection; only start-service sites for TorrentService) plus the manifest declaration (AndroidManifest:252–254, no exported flag, no intent filter). Row 21 STAYS OPEN: the UNREACHABLE judgement on this evidence was recorded as the merger's, not made here — see the CONDITIONAL flip table added below. Counts unchanged: 39 REACHABLE / 0 UNREACHABLE / 1 OPEN. Build: not run. C1: not run. Original file backed up at ~/workspace/libretorrent-merge-backup-pre-openclose2/batch72-merge-ready.md. Round-1 flips untouched (rows 13, 15 Rx-error lambdas kept REACHABLE via the printed subscription route; no contradictory printed evidence found).**

**REVISION 2026-11-01 (OPEN-closing, batches 72-74 pass): no label changed. Row 21 (TorrentService.onBind) was re-checked against freshly printed TorrentService.java (525 lines, SHA f0c3cdc4..., onBind at :100-103 returning null) and AndroidManifest.xml (295 lines, SHA 875a8aa7..., TorrentService declared :252-253, not exported, no intent filter), plus a partial-corpus grep over 165-166 connector-fetched app Java files (saved in ~/workspace/b727374-openclose-src/partial_corpus_grep_20261101.txt) finding zero `bindService` hits and only startService sites for TorrentService (NotificationReceiver:58/:74/:79 and batch 71/72 prints). That grep is NOT a full-repo grep (252 app Java files exist; ~86 not yet in the corpus), so row 21 stays OPEN, NOT UNREACHABLE, per the task rule. Named target: a saved full-repo grep for bindService/TorrentService, or a printed bindService site. Counts unchanged: 39 REACHABLE / 0 UNREACHABLE / 1 OPEN. Build: not run. C1: not run. Original file backed up at ~/workspace/libretorrent-merge-backup-pre-openclose/batch72-merge-ready.md.**

**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 72 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 72 only, max 40 methods, no other batch, no other app, no device replay, no Aegis.
- Task: labels only. Prior proposals are INPUTS, not results. Every row below was
  re-checked against printed source in the prior proposal session, and the single
  OPEN row was re-checked in this session against the printed corpus (see below).

## Membership — verified first, not guessed

Exactly the 40 rows for batch 72 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/agent27-plan.tsv` (4,732 rows total; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
All 40 rows are `TODO_CANDIDATE_REACHABLE` in the plan. Classes: Scheduler (1 row:
setStopAppAlarm), TorrentService (36 rows), TorrentService$1 anonymous
TorrentEngineListener (2 rows), BaseAlertDialog (2 rows).

## Printed source used

Base path (all files):
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`

Prior session, connector, one file at a time, saved under `~/workspace/b71_src/`:
- `service/TorrentService.java` (525 lines, full; byte-identical to the local copy in `~/workspace/ground-truth-work/libretorrent/src/TorrentService.java`)
- `service/Scheduler.java` (145 lines, full)
- `ui/BaseAlertDialog.java` (199 lines, full)
- `ui/main/MainFragment.java` (637 lines, full)
- `ui/settings/sections/SchedulingSettingsFragment.java` (242 lines, full)
- `app/src/main/AndroidManifest.xml` (MainActivity LAUNCHER, TorrentService declared with foregroundServiceType dataSync, SchedulerReceiver declared)

This session, re-check of the OPEN row:
- Local grep over the printed corpus `~/workspace/b71_src/` and
  `~/workspace/b73-74-src/` for `bindService` returned zero hits in every file
  (including TorrentService.java, MainFragment.java, TorrentEngine.java, Utils.java).
  This is a printed-corpus grep, NOT a saved full-repo grep, and it is NOT used
  as evidence of absence: row 21 stays OPEN (see below). No fresh HTTP 429 was
  hit in this session. A `search_code` locate attempt failed on schema validation
  and was NOT used as evidence for any row.
- TorrentEngine fresh fetch in this session (branch `work-2026-10-31`, SHA
  `17d06efe1076675af0c41a6c929e8d2f04eabb68`) confirms the service/engine
  anchor for batch 71 rows 1–2; for batch 72 it additionally confirms that
  TorrentEngine starts TorrentService only via `startServiceBackground` /
  start-service Intents (TorrentEngine.java:152, :156–157, :283–284 in the
  numbered local copy), never via a bind call in the printed TorrentEngine
  file — again, printed-corpus only, not a full-repo claim.

No connector `search_code` result was used as evidence of absence anywhere in this file.
No full-repo grep was run.

## confirmed_by convention in this file

Same as batch 71 in this pass, recorded NOT decided:
- SOURCE = every link is a printed app-code line, or a standard framework
  lifecycle/entry step whose app-side registration or call is printed.
  A method directly called from a SOURCE anchor stays SOURCE. Per-row convention,
  not the whole-route convention; labels unaffected, only `confirmed_by` would
  change at merge under the whole-route convention.
- INFERRED = the chain crosses an unprinted dispatch — Rx subscription /
  method-reference dispatch, session-listener dispatch, Handler/Completable
  dispatch, or the JVM class-initialiser rule — or the method is a synthetic
  lambda, a `<clinit>`, or a framework-instantiated `<init>` / anonymous
  listener. Downstream internal calls of an INFERRED-dispatched method stay
  INFERRED (worker rule, following the batch 14 correction precedent).
- No row is flipped to UNREACHABLE on absence: no saved full-repo grep was run.

## Shared routes

**S1 — Service lifecycle (service-anchored, not launcher-anchored).**
MAN declares TorrentService. Framework (standard Service lifecycle, app-side
declaration printed) -> TorrentService.onCreate:106–114 -> initPendingIntents (:112),
makeForegroundNotify (:113). First start: TorrentService.onStartCommand:176–197 ->
init (:191, first-start branch) -> TorrentService.init:116–135. Who starts
TorrentService was NOT printed in this session, so S1 is service-anchored;
under a strict launcher-entry rule these rows revert to OPEN.
**S2 — Shutdown actions (service-anchored).** TorrentService.onStartCommand:183–186 ->
handleShutdownActions:199–212 -> shutdown (:204, for
NOTIFY_ACTION_SHUTDOWN_APP / ACTION_SHUTDOWN) -> Completable method-ref
this::stopEngine (:152, Rx dispatch INFERRED) -> stopEngine:157–162 ->
forceClearForeground (:160) and engine.doStop (:161).
ACTION_RESTART_FOREGROUND_NOTIFICATION -> makeForegroundNotify (:207).
**S3 — Session stop (session-anchored).** TorrentService.init:132 registers
engineListener (anonymous TorrentEngineListener, TorrentService:255–262) ->
session dispatch (unprinted, INFERRED) -> engineListener.onSessionStopped
(:257–261) -> stopService (:260) -> stopSelf (:172) -> framework
onDestroy (standard lifecycle, INFERRED here because its only printed
trigger chain crosses the session dispatch).
**S4 — Foreground-notify Rx flows (Rx-anchored).** TorrentService.init:121,123 ->
subscribeCombinedPauseButtonState / subscribeForceSortAndFilter ->
Rx subscribes -> lambdas $4–$6 -> getInfoListSingle / updateForegroundNotifyActions.
TorrentService.init:134 -> startUpdateForegroundNotify -> Rx chain -> lambdas $0/$1 ->
updateForegroundNotify -> makeDetailNotifyInboxStyle. All Rx steps are
INFERRED; the methods that only run through them are INFERRED.
**S5 — Alert dialog (fragment-anchored).** MainFragment.onActionItemClicked:477–479
(action-mode delete menu) -> MainFragment.deleteTorrentsDialog:501–519 ->
BaseAlertDialog.newInstance (:508, body BaseAlertDialog:94–112) -> `new BaseAlertDialog()` (BaseAlertDialog:98)
-> BaseAlertDialog.<init>, then dialog.show (:519). The step attaching
MainFragment to MainActivity was NOT printed in this session, so S5 is
fragment-anchored; under a strict launcher-entry rule rows 39–40 revert to OPEN.

Abbreviations: TS = TorrentService.java, SCH = Scheduler.java,
BAD = BaseAlertDialog.java, MF = MainFragment.java,
SSF = SchedulingSettingsFragment.java, MAN = AndroidManifest.xml.

## Lambda numbering (TorrentService, source order, NOT bytecode-confirmed)

Lambdas in TS in source order: startUpdateForegroundNotify flatMapSingle
(:284) = $0, its error lambda (:293) = $1, getInfoListSingle flatMap (:301)
= $2, its error lambda (:309) = $3, subscribeForceSortAndFilter filter
(:316) = $4, its subscribe lambda (:318) = $5, subscribeCombinedPauseButtonState
subscribe lambda (:324) = $6, forceClearForeground runnable (:331) = $7.
This reproduces every plan descriptor exactly (parameter types included:
$2/$0 take List, $3/$1 take Throwable, $4/$5/$6 take Boolean, $7 takes ()).
The shutdown Completable uses a method reference (this::stopEngine, :152),
not a lambda, so it takes no $ number. The settings-change subscribe in
init (:125–126) likewise uses a method reference (this::handleSettingsChanged).

## Table — 40 rows in plan order

| # | Method (plan) | Label proposed | confirmed_by | Route / printed citations |
|---|---|---|---|---|
| 1 | Scheduler.setStopAppAlarm (Landroid/content/Context;I)Z | REACHABLE proposed | SOURCE | Direct calls SSF:213 and SSF:229 (scheduling-shutdown on / shutdown-time changed). Body SCH:56–58: delegates to setStartStopAppAlarm with SCHEDULER_WORK_STOP_APP. Note: SchedulerReceiver.onStopApp as printed calls setStartAppAlarm (SchedulerReceiver.java:92 — see batch 71 file), NOT this method; this method's route is via SSF only. |
| 2 | TorrentService.<clinit> ()V | REACHABLE proposed | INFERRED | JVM class-init rule unprinted, hence INFERRED. First printed reference is the MAN service declaration (MAN:252–254) plus TS.onCreate body; static fields TS:68–76 (TAG, notification ids, action strings). |
| 3 | TorrentService.<init> ()V | REACHABLE proposed | INFERRED | No explicit constructor in TS; default constructor. Framework instantiates the Service (MAN declaration printed); instantiation dispatch unprinted, hence INFERRED. Field initialisers (disposables, subjects, engineListener TS:255) run during this <init>. |
| 4 | TorrentService.forceClearForeground ()V | REACHABLE proposed | INFERRED | Direct call TS.stopEngine:160, but stopEngine is reached only via the Completable method-ref in shutdown (TS:152, Rx dispatch INFERRED), so INFERRED here. Body TS:329–334: Completable.fromRunnable with row 11's lambda -> updateForegroundNotify(empty list). |
| 5 | TorrentService.getInfoListSingle ()Lio/reactivex/disposables/Disposable; | REACHABLE proposed | INFERRED | Only printed caller is row 18's lambda (TS:318, Rx subscribe), so INFERRED. Body TS:298–312: stateProvider.getInfoListSingle, flatMap row 12, subscribe updateForegroundNotify + row 13 error lambda. |
| 6 | TorrentService.handleActions (Ljava/lang/String;)V | REACHABLE proposed | SOURCE | Direct call TS.onStartCommand:194. Body TS:214–233: PAUSE_ALL -> engine.pauseAll, RESUME_ALL -> engine.resumeAll, PAUSE_RESUME_ALL -> resume/pause by combinedPauseButtonState value. |
| 7 | TorrentService.handleSettingsChanged (Ljava/lang/String;)V | REACHABLE proposed | INFERRED | Subscribed by method reference in TS.init:125–126 (`pref.observeSettingsChanged().subscribe(this::handleSettingsChanged)`); Rx emission unprinted, hence INFERRED. Body TS:264–275: cpu_do_not_sleep -> setKeepCpuAwake, filter/sorting keys -> setFilterAndSorting + forceSortAndFilter.onNext, combined-pause-button key -> updateForegroundNotifyActions. |
| 8 | TorrentService.handleShutdownActions (Ljava/lang/String;)I | REACHABLE proposed | SOURCE | Direct call TS.onStartCommand:183–186 (return >= 0 short-circuits onStartCommand). Body TS:199–212: shutdown actions -> shutdown (:204) + START_NOT_STICKY, RESTART_FOREGROUND_NOTIFICATION -> makeForegroundNotify (:207) + START_STICKY, else -1. |
| 9 | TorrentService.init ()V | REACHABLE proposed | SOURCE | Direct call TS.onStartCommand:191 (first-start compareAndSet branch). Body TS:116–135: makeForegroundNotify, subscribeCombinedPauseButtonState, setFilterAndSorting, subscribeForceSortAndFilter, settings subscribe, enableBootReceiverIfNeeded, setKeepCpuAwake, engine.doStart, engine.addListener(engineListener), startUpdateForegroundNotify. |
| 10 | TorrentService.initPendingIntents ()V | REACHABLE proposed | SOURCE | Direct call TS.onCreate:112. Body TS:497–525: shutdown/pause/resume/pause-resume PendingIntents built as broadcasts to NotificationReceiver. |
| 11 | TorrentService.lambda$forceClearForeground$7 ()V | REACHABLE proposed | INFERRED | Body TS:331 `Completable.fromRunnable(() -> updateForegroundNotify(Collections.emptyList()))` inside forceClearForeground. $7 by source order (see numbering above). Rx/Completable dispatch unprinted, hence INFERRED. |
| 12 | TorrentService.lambda$getInfoListSingle$2 (Ljava/util/List;)Lio/reactivex/SingleSource; | REACHABLE proposed | INFERRED | Body TS:301–306 `flatMap((infoList) -> Observable.fromIterable(infoList).filter(itemsFilter).sorted(itemsSorting).toList())` inside getInfoListSingle. $2 by source order. Rx dispatch unprinted, hence INFERRED. |
| 13 | TorrentService.lambda$getInfoListSingle$3 (Ljava/lang/Throwable;)V | REACHABLE proposed | INFERRED | Body TS:309–311 error lambda `(Throwable t) -> Log.e(...)` in getInfoListSingle's subscribe. $3 by source order. Runs only on an info-list error; that is a condition on the route, not a blocker. |
| 14 | TorrentService.lambda$startUpdateForegroundNotify$0 (Ljava/util/List;)Lio/reactivex/SingleSource; | REACHABLE proposed | INFERRED | Body TS:284–289 `flatMapSingle((infoList) -> Flowable.fromIterable(infoList).filter(itemsFilter).sorted(itemsSorting).toList())` inside startUpdateForegroundNotify. $0 by source order. Rx dispatch unprinted, hence INFERRED. |
| 15 | TorrentService.lambda$startUpdateForegroundNotify$1 (Ljava/lang/Throwable;)V | REACHABLE proposed | INFERRED | Body TS:293–295 error lambda `(Throwable t) -> Log.e(...)` in startUpdateForegroundNotify's subscribe. $1 by source order. Runs only on an info-list error. |
| 16 | TorrentService.lambda$subscribeCombinedPauseButtonState$6 (Ljava/lang/Boolean;)V | REACHABLE proposed | INFERRED | Body TS:324–326 `subscribe((paused) -> updateForegroundNotifyActions(pref.foregroundNotifyCombinedPauseButton()))` inside subscribeCombinedPauseButtonState. $6 by source order. Rx dispatch unprinted, hence INFERRED. |
| 17 | TorrentService.lambda$subscribeForceSortAndFilter$4 (Ljava/lang/Boolean;)Z | REACHABLE proposed | INFERRED | Body TS:316 `filter((force) -> force)` inside subscribeForceSortAndFilter. $4 by source order. Rx dispatch unprinted, hence INFERRED. |
| 18 | TorrentService.lambda$subscribeForceSortAndFilter$5 (Ljava/lang/Boolean;)V | REACHABLE proposed | INFERRED | Body TS:318 `subscribe((force) -> disposables.add(getInfoListSingle()))` inside subscribeForceSortAndFilter. $5 by source order; this is the only printed caller of row 5. Rx dispatch unprinted, hence INFERRED. |
| 19 | TorrentService.makeDetailNotifyInboxStyle (Ljava/util/List;)Landroidx/core/app/NotificationCompat$InboxStyle; | REACHABLE proposed | INFERRED | Only printed caller is TS.updateForegroundNotify:392, and updateForegroundNotify runs only via Rx subscribes (rows 14/12 chains and row 11's lambda), so INFERRED here. Body TS:398–453: builds InboxStyle lines per torrent state, big-content title, summary. |
| 20 | TorrentService.makeForegroundNotify ()V | REACHABLE proposed | SOURCE | Direct calls TS.onCreate:113, TS.init:120, TS.handleShutdownActions:207 — all SOURCE paths. Body TS:342–366: MainActivity startup intent, NotificationCompat.Builder, setForegroundNotifyActions (:361), startForeground (:365). |
| 21 | TorrentService.onBind (Landroid/content/Intent;)Landroid/os/IBinder; | OPEN | — | Definition TS:100–103 returns null. Framework calls onBind only for a bound service, not for a started service. ROUND-2 re-check (2026-11-01): saved full-tree grep over all 252 app Java files (`~/workspace/b727374-openclose2-src/full_grep_bindservice_20261101.txt`) finds zero `bindService`, zero `unbindService`, zero `ServiceConnection` hits in the whole tree; the only TorrentService sites are start-service sites (TorrentEngine:152/:156–157/:283–284 via startServiceBackground, NotificationReceiver:56/:67/:72/:77 via startService) plus a comment-only hit (ProxySettingsFragment:75). Manifest (AndroidManifest:252–254, SHA 875a8aa7… in round-1 prints) declares TorrentService with no `android:exported` and no intent filter, so no external binder can bind it either. This row nevertheless STAYS OPEN in this pass: the bind question was recorded as a merger judgement, not an agent flip (see CONDITIONAL flip table below). Resolves with: (a) a printed bindService site for TorrentService → REACHABLE INFERRED (framework dispatch); or (b) a merger judgement that the saved full grep + manifest together settle absence → UNREACHABLE no_trigger_in_app. That judgement is NOT made here. |
| 22 | TorrentService.onCreate ()V | REACHABLE proposed | SOURCE | Standard Service lifecycle entry; service declared in MAN:252–254. Body TS:106–114: settings/engine/stateProvider setup, initPendingIntents (:112), makeForegroundNotify (:113). |
| 23 | TorrentService.onDestroy ()V | REACHABLE proposed | INFERRED | Standard Service lifecycle, but its only printed trigger chain is S3: engineListener.onSessionStopped -> stopService -> stopSelf (TS:172) -> framework onDestroy, and the session dispatch is unprinted, so INFERRED here. Body TS:143–148 (super.onDestroy + log). Convention recorded, NOT decided: if the merger treats all standard lifecycle callbacks as SOURCE regardless of trigger chain, row 23 flips to SOURCE; the label does not change. |
| 24 | TorrentService.onStartCommand (Landroid/content/Intent;II)I | REACHABLE proposed | SOURCE | Standard Service lifecycle entry; service declared in MAN:252–254. Body TS:176–197: shutdown-action handling (:183–186), first-start init (:190–191), handleActions (:193–194), returns START_STICKY (:196). |
| 25 | TorrentService.setFilterAndSorting ()V | REACHABLE proposed | SOURCE | Direct calls TS.init:122 (SOURCE path) and TS.handleSettingsChanged:270. Body TS:137–140: Utils.getForegroundNotifyFilter / getForegroundNotifySorting. The init path alone makes this SOURCE. |
| 26 | TorrentService.setForegroundNotifyActions (Z)V | REACHABLE proposed | SOURCE | Direct calls TS.makeForegroundNotify:361 (SOURCE path) and TS.updateForegroundNotifyActions:493. Body TS:455–490: clears actions, adds combined pause/resume or separate pause+resume actions, plus shutdown action. The makeForegroundNotify path alone makes this SOURCE. |
| 27 | TorrentService.setKeepCpuAwake (Z)V | REACHABLE proposed | SOURCE | Direct calls TS.init:129 (SOURCE path), TS.handleSettingsChanged:267, TS.stopService:168. Body TS:235–254: acquire/release PARTIAL_WAKE_LOCK, null/held guards. The init path alone makes this SOURCE. |
| 28 | TorrentService.shutdown ()V | REACHABLE proposed | SOURCE | Direct call TS.handleShutdownActions:204 (SOURCE path). Body TS:150–155: Completable.fromRunnable(this::stopEngine) subscribed on computation scheduler. The Rx step affects stopEngine (row 30), not the execution of shutdown itself. |
| 29 | TorrentService.startUpdateForegroundNotify ()V | REACHABLE proposed | SOURCE | Direct call TS.init:134 (SOURCE path). Body TS:277–296: shuttingDown/foregroundNotify guards, observeInfoList chain with rows 14/15, 1-second delay, subscribe to updateForegroundNotify. |
| 30 | TorrentService.stopEngine ()V | REACHABLE proposed | INFERRED | Reached only via the Completable method-ref in shutdown (TS:152, Rx dispatch INFERRED). Body TS:157–162: shuttingDown.set(true), forceClearForeground (:160), engine.doStop (:161). |
| 31 | TorrentService.stopService ()V | REACHABLE proposed | INFERRED | Only printed caller is TorrentService$1.onSessionStopped (TS:260, session dispatch INFERRED, S3). Body TS:164–173: disposables.clear, removeListener, setKeepCpuAwake(false), isAlreadyRunning=false, stopForeground(true), stopSelf. |
| 32 | TorrentService.stopUpdateForegroundNotify ()V | REACHABLE proposed | INFERRED | Only printed caller is TS.updateForegroundNotify:377, and updateForegroundNotify runs only via Rx subscribes, so INFERRED here. Body TS:336–340: disposes foregroundDisposable if non-null. |
| 33 | TorrentService.subscribeCombinedPauseButtonState ()V | REACHABLE proposed | SOURCE | Direct call TS.init:121 (SOURCE path). Body TS:321–327: combinedPauseButtonState observed on main thread, subscribes row 16's lambda. |
| 34 | TorrentService.subscribeForceSortAndFilter ()V | REACHABLE proposed | SOURCE | Direct call TS.init:123 (SOURCE path). Body TS:314–319: forceSortAndFilter filtered (row 17) and subscribed (row 18). |
| 35 | TorrentService.updateForegroundNotify (Ljava/util/List;)V | REACHABLE proposed | INFERRED | Reached only via Rx method-ref subscribes (TS:292 in startUpdateForegroundNotify, TS:308 in getInfoListSingle) and row 11's lambda (:331); Rx dispatch unprinted, hence INFERRED. Body TS:368–396: shutdown branch (cancel shutdown intent, stopUpdateForegroundNotify :377, shutdown style) vs normal branch (online/offline text, makeDetailNotifyInboxStyle :392), startForeground (:395). |
| 36 | TorrentService.updateForegroundNotifyActions (Z)V | REACHABLE proposed | INFERRED | Only printed callers are row 16's Rx lambda (TS:324–326) and TS.handleSettingsChanged:273 (itself Rx, row 7), so INFERRED. Body TS:492–495: setForegroundNotifyActions (:493) + startForeground (:494). Package-private, not private. |
| 37 | TorrentService$1.<init> (Lorg/proninyaroslav/libretorrent/service/TorrentService;)V | REACHABLE proposed | INFERRED | Anonymous TorrentEngineListener instance created by the field initialiser TS:255 `new TorrentEngineListener() { ... }`, which runs during TorrentService.<init> (row 3, framework instantiation INFERRED). The anonymous constructor itself takes the enclosing TorrentService (plan descriptor (TorrentService)V). |
| 38 | TorrentService$1.onSessionStopped ()V | REACHABLE proposed | INFERRED | Session dispatch unprinted (S3), hence INFERRED. Body TS:257–261: log + stopService (:260). Listener registered at TS.init:132 (`engine.addListener(engineListener)`). |
| 39 | BaseAlertDialog.<clinit> ()V | REACHABLE proposed | INFERRED | JVM class-init rule unprinted, hence INFERRED. First printed execution reference is MF.deleteTorrentsDialog:508 `BaseAlertDialog.newInstance(...)` (S5); static TAG field BAD:45. |
| 40 | BaseAlertDialog.<init> ()V | REACHABLE proposed | SOURCE | S5, dialog-anchored: MF.onActionItemClicked:477–479 (delete menu) -> MF.deleteTorrentsDialog:501–519 -> BAD.newInstance (:508; body BAD:94–112) -> `new BaseAlertDialog()` (BAD:98) -> implicit default <init> (no explicit constructor in BAD:43–199; DialogFragment super-constructor). Dialog shown at MF:519. Caveat: the MainActivity -> MainFragment attachment step was not printed in this session, so under a strict launcher-entry rule this row reverts to OPEN. |

## Counts — mechanically verified

- 40 rows, sequence 1–40 intact, in plan order.
- **39 REACHABLE proposed / 0 UNREACHABLE proposed / 1 OPEN.**
- SOURCE 16 / INFERRED 23 among REACHABLE rows.
- **0 rows verified for merge.** Verification requires, in order: the main agent's
  1-in-5 spot-check of this part, `py_compile` + build on a full checkout, and the
  Mac build/C1 return — none of which has happened here.

## OPEN rows and what would resolve them

- Row 21, TorrentService.onBind: a printed bindService site for TorrentService,
  or a merger judgement on the round-2 saved full-tree grep
  (`~/workspace/b727374-openclose2-src/full_grep_bindservice_20261101.txt`: 0
  bindService / 0 ServiceConnection / 0 unbindService in 252 files) plus the
  manifest declaration (no exported flag, no intent filter). If a bound client
  exists, onBind becomes REACHABLE (framework dispatch INFERRED); if the merger
  judges the grep + manifest sufficient, it becomes UNREACHABLE
  no_trigger_in_app — that judgement is NOT made here (see CONDITIONAL flip
  table above).


## CONDITIONAL flip table for row 21 (round 2, 2026-11-01) — NO judgement made here

Saved evidence: `~/workspace/b727374-openclose2-src/full_grep_bindservice_20261101.txt` (all 252 app Java files: 0 bindService, 0 unbindService, 0 ServiceConnection; TorrentService sites are start-service only) + manifest declaration (AndroidManifest:252–254: service declared, no `android:exported`, no intent filter).

- If a bindService site for TorrentService is printed (in-app binder, or any ServiceConnection use naming TorrentService) → row 21 flips to REACHABLE, INFERRED (framework bind dispatch; the onBind body itself just returns null, TS:100–103).
- If the merger judges the saved full grep + manifest together sufficient to settle absence (no in-app binder can exist without a bindService call in app Java; no external binder can bind a non-exported service with no intent filter) → row 21 flips to UNREACHABLE, kind `no_trigger_in_app`, INFERRED.
- Until either happens, row 21 stays OPEN. This pass makes neither judgement.

## Caveats / merger must-do

1. Lambda numbering ($0–$7) is source-order inferred, NOT bytecode-confirmed.
   Merger must confirm against bytecode if disputed; the bodies cited are
   unambiguous regardless of the number.
2. Strict-entry caveat: no printed step starting TorrentService, and no printed
   MainActivity -> MainFragment attachment step, were printed in the prior session.
   Under a strict launcher-entry rule, all 39 REACHABLE rows revert to OPEN.
   This convention is recorded, NOT decided here. This does not change the proposed counts.
3. onDestroy (row 23) is INFERRED, not SOURCE, deliberately: unlike onCreate /
   onStartCommand, its only printed trigger chain crosses the unprinted session
   dispatch (S3). If the merger treats all standard lifecycle callbacks as SOURCE
   regardless of trigger chain, row 23 flips to SOURCE; the label does not change.
4. makeDetailNotifyInboxStyle (row 19) and stopUpdateForegroundNotify (row 32)
   are INFERRED, not SOURCE, deliberately: their only printed caller is the
   Rx-only updateForegroundNotify (row 35). Their SOURCE-looking direct
   call sites do not make them SOURCE while the enclosing route is Rx-only.
5. No UNREACHABLE row is claimed: no saved full-repo grep was run.
6. No build, sampler, grep, or C1 check was run; 0/40 verified for merge.

## What this part is not

- Not a merge: `graph_def.py` is untouched, and this file is not in `graph_def.py` format.
- Not a claim about batches 1–71, 73–120, about any other app, or about device replay.
- Not a claim that the plan's TODO_CANDIDATE_REACHABLE labels are verified: they
  happen to agree with the proposals here except for row 21, but agreement with
  the plan is not verification.
