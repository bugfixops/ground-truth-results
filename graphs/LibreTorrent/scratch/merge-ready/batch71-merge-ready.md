# LibreTorrent batch 71 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 71 only, max 40 methods, no other batch, no other app, no device replay, no Aegis.
- Task: labels only. Prior proposals are INPUTS, not results. Every row below was
  re-checked against printed source in the prior proposal session and, for the
  flagged gap, against a fresh connector fetch in this session (see below).
  No row was copied as a verdict without a printed citation.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 71 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/agent27-plan.tsv` (4,732 rows total; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
All 40 rows are `TODO_CANDIDATE_REACHABLE` in the plan. Classes: PowerReceiver (2),
SchedulerReceiver (4), FeedDownloaderWorker (6), FeedFetcherWorker (13),
SaveLogWorker (8), Scheduler (7).

## Printed source used

Base path (all files):
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`

Prior session, connector, one file at a time, saved under `~/workspace/b71_src/`:
- `receiver/PowerReceiver.java` (76 lines, full)
- `receiver/SchedulerReceiver.java` (104 lines, full)
- `service/FeedDownloaderWorker.java` (215 lines, full)
- `service/FeedFetcherWorker.java` (270 lines, full)
- `service/SaveLogWorker.java` (129 lines, full)
- `service/Scheduler.java` (145 lines, full)
- `service/TorrentService.java` (525 lines, full; byte-identical to the local copy in `~/workspace/ground-truth-work/libretorrent/src/TorrentService.java`)
- `ui/settings/sections/FeedSettingsFragment.java` (163 lines, full)
- `ui/settings/sections/SchedulingSettingsFragment.java` (242 lines, full)
- `ui/log/LogViewModel.java` (227 lines, full)
- `app/src/main/AndroidManifest.xml` (MainActivity LAUNCHER, TorrentService declared, SchedulerReceiver declared with no intent-filter)
- `ui/main/MainFragment.java` (637 lines, full; used only for batch 72's BaseAlertDialog rows)

This session, fresh connector fetch, one file, with a pause:
- `core/model/TorrentEngine.java` — fresh fetch from branch `work-2026-10-31` returned
  SHA `17d06efe1076675af0c41a6c929e8d2f04eabb68`, the same SHA recorded in the
  batch 73–74 session for this file. This CLOSES the prior session's flagged gap:
  TorrentEngine lines cited below (field :108, doStart :239, switchPowerReceiver
  :989–1005, settings branches :1467/:1471) are no longer "local copy only".
  The line numbers were re-checked against the numbered local copy in
  `~/workspace/b73-74-src/TorrentEngine.java` (1,659 lines), whose numbering
  matches the prior citations; the fresh fetch confirms branch-file identity by SHA.
  Saved copy (numbered local reprint, for citation checking) in `~/workspace/b717273-src/TorrentEngine.java`.
  No fresh HTTP 429 was hit in this session. A `search_code` locate attempt failed
  on schema validation and was NOT used as evidence for any row.

No connector `search_code` result was used as evidence of absence anywhere in this file.
No full-repo grep was run; a saved full-repo grep is still owed before any
UNREACHABLE row (none in this batch) could be merged — not applicable here, but
the REACHABLE rows below still need the main-agent spot-check, `py_compile`,
build, and Mac build/C1.

## confirmed_by convention in this file

- SOURCE = every link in the cited chain is a printed app-code line, or a standard
  framework lifecycle/entry step whose app-side registration or call is printed.
  Direct internal calls from such an anchor stay SOURCE. This is the PER-ROW
  convention, not the whole-route convention used in some earlier batches;
  labels are unaffected, only `confirmed_by` would change at merge if the merger
  adopts the whole-route convention. This convention is recorded, NOT decided here.
- INFERRED = the chain crosses an unprinted dispatch — WorkManager worker
  instantiation/doWork dispatch, AlarmManager/PendingIntent broadcast delivery,
  dynamic broadcast registration delivery, Rx/Handler dispatch, or the JVM
  class-initialiser rule — or the method itself is a synthetic lambda /
  `<clinit>` / framework-instantiated `<init>`. Downstream internal calls of an
  INFERRED-dispatched method stay INFERRED in this file (worker rule, following
  the batch 14 correction precedent). This convention is recorded, NOT decided here.
- No row is flipped to UNREACHABLE on absence: no saved full-repo grep was run.

## Shared routes

**R1 — Service/engine start (service-anchored, not launcher-anchored).**
Manifest TorrentService declared; TorrentService.onCreate (batch 72) -> init ->
engine.doStart (TorrentService.java:131) -> TorrentEngine.doStart:239
`switchPowerReceiver()` -> TorrentEngine.switchPowerReceiver:989–1005.
Who starts TorrentService was NOT printed in this session, so R1 is
service-anchored; under a strict launcher-entry rule these rows revert to OPEN.
**R2 — Alarm scheduling (settings-anchored).** SchedulingSettingsFragment.onPreferenceChange ->
Scheduler.set/cancel methods (SchedulingSettingsFragment:200,204,213,217,223,229);
SchedulerReceiver is declared in the manifest with no intent-filter, so it is
reached only via the explicit PendingIntent Scheduler:93–98 + AlarmManager.setExactAndAllowWhileIdle Scheduler:104.
The AlarmManager -> onReceive delivery itself is unprinted framework dispatch, hence INFERRED for SchedulerReceiver.onReceive and its callees.
**R3 — Periodic feed refresh (settings-anchored).** FeedSettingsFragment.onPreferenceChange:134
or :142 -> Scheduler.runPeriodicalRefreshFeeds:112–126 -> WorkManager
enqueueUniquePeriodicWork (Scheduler:124–125) -> FeedFetcherWorker.doWork (WorkManager dispatch
INFERRED) -> FeedFetcherWorker internal chain. FeedSettingsFragment:136 is the cancel branch.
**R4 — Fetched items -> downloader (worker-anchored).** FeedFetcherWorker.fetchChannel:183–184
(gate !noAutoDownload && channel.autoDownload) -> FeedFetcherWorker.sendFetchedItems:212–237
-> OneTimeWorkRequest.Builder(FeedDownloaderWorker.class) + WorkManager.enqueue (:232–236)
-> FeedDownloaderWorker.doWork (WorkManager dispatch INFERRED) -> FeedDownloaderWorker internal chain.
**R5 — Log save (viewmodel-anchored).** LogViewModel.saveLog:199–212 ->
OneTimeWorkRequest.Builder(SaveLogWorker.class) + WorkManager.enqueue (:208–212)
-> SaveLogWorker.doWork (WorkManager dispatch INFERRED) -> SaveLogWorker internal chain.
Who calls LogViewModel.saveLog was NOT printed in this session.

Abbreviations: PR = PowerReceiver.java, SR = SchedulerReceiver.java,
FDW = FeedDownloaderWorker.java, FFW = FeedFetcherWorker.java,
SLW = SaveLogWorker.java, SCH = Scheduler.java, TE = TorrentEngine.java,
FSF = FeedSettingsFragment.java, SSF = SchedulingSettingsFragment.java,
LVM = LogViewModel.java, MAN = AndroidManifest.xml.

## Table — 40 rows in plan order

| # | Method (plan) | Label proposed | confirmed_by | Route / printed citations |
|---|---|---|---|---|
| 1 | PowerReceiver.getFilter ()Landroid/content/IntentFilter; | REACHABLE proposed | SOURCE | R1: TE.switchPowerReceiver:989–1005, branch `batteryControl \|\| onlyCharging` (:1004–1005) `registerReceiver(powerReceiver, PowerReceiver.getFilter())`. Definition PR:53–64 (actions POWER_CONNECTED, POWER_DISCONNECTED, BATTERY_LOW, BATTERY_OKAY). Gate: STATE settings — batteryControl or onlyCharging true, customBatteryControl false. |
| 2 | PowerReceiver.onReceive (Landroid/content/Context;Landroid/content/Intent;)V | REACHABLE proposed | INFERRED | Registered dynamically TE:1001 (custom filter) / :1005 (getFilter); framework broadcast delivery unprinted, hence INFERRED. Body PR:36–50: switch on action, POWER/BATTERY cases -> TorrentEngine.getInstance + rescheduleTorrents (:47–48). Note: BATTERY_CHANGED (:46) is only in getCustomFilter (PR:66–75), not getFilter. |
| 3 | SchedulerReceiver.<init> ()V | REACHABLE proposed | INFERRED | No explicit constructor in SR (41–104); default constructor. Framework instantiates the receiver: MAN declares SchedulerReceiver (no intent-filter), and SCH:93–98 builds an explicit PendingIntent.getBroadcast for SchedulerReceiver.class. Instantiation dispatch unprinted, hence INFERRED. |
| 4 | SchedulerReceiver.onReceive (Landroid/content/Context;Landroid/content/Intent;)V | REACHABLE proposed | INFERRED | R2: SCH.setStartStopAppAlarm:93–98 explicit PendingIntent + :104 AlarmManager.setExactAndAllowWhileIdle; framework delivery unprinted, hence INFERRED. Body SR:44–63: null-action guard, SCHEDULER_WORK_START_APP -> onStartApp (:55), SCHEDULER_WORK_STOP_APP -> onStopApp (:59). Constants SCH:44–45, imported SR:34–35. |
| 5 | SchedulerReceiver.onStartApp (Landroid/content/Context;Lorg/proninyaroslav/libretorrent/core/settings/SettingsRepository;Lorg/proninyaroslav/libretorrent/ui/TorrentNotifier;)V | REACHABLE proposed | INFERRED | Direct call SR:55 from onReceive (INFERRED route, so INFERRED here). Body SR:65–82: gate `pref.enableSchedulingStart()` (:67); oneshot handling (:70–75, incl. setStartAppAlarm call :73); TorrentEngine.getInstance(...).start() (:80). |
| 6 | SchedulerReceiver.onStopApp (Landroid/content/Context;Lorg/proninyaroslav/libretorrent/core/settings/SettingsRepository;Lorg/proninyaroslav/libretorrent/ui/TorrentNotifier;)V | REACHABLE proposed | INFERRED | Direct call SR:59 from onReceive (INFERRED route). Body SR:84–103: gate `pref.enableSchedulingShutdown()` (:86); oneshot handling (:89–94, incl. setStartAppAlarm call :92 — the file as printed calls setStartAppAlarm, not setStopAppAlarm, in onStopApp); TorrentEngine.getInstance(...).forceStop() (:96). |
| 7 | FeedDownloaderWorker.<clinit> ()V | REACHABLE proposed | INFERRED | JVM class-init rule unprinted, hence INFERRED. First printed class reference: FFW.sendFetchedItems:232 `OneTimeWorkRequest.Builder(FeedDownloaderWorker.class)` (R4). Static TAG field FDW:57. |
| 8 | FeedDownloaderWorker.<init> (Landroid/content/Context;Landroidx/work/WorkerParameters;)V | REACHABLE proposed | INFERRED | Definition FDW:69–72 (super(context, params)). WorkManager instantiates the Worker; that dispatch is unprinted library code, hence INFERRED. Enqueue site R4, FFW:232–236. |
| 9 | FeedDownloaderWorker.addTorrents (Ljava/util/ArrayList;)Landroidx/work/ListenableWorker$Result; | REACHABLE proposed | INFERRED | Direct call FDW.doWork:89 `addTorrents(fetchTorrents(...))`, but doWork dispatch is INFERRED (R4), so INFERRED here. Body FDW:192–214: empty-list guard, engine.start loop (:197–209), engine.addTorrents(paramsList, true) (:211). |
| 10 | FeedDownloaderWorker.doWork ()Landroidx/work/ListenableWorker$Result; | REACHABLE proposed | INFERRED | WorkManager dispatch INFERRED (R4, FFW:232–236). Body FDW:76–92: action gate `ACTION_DOWNLOAD_TORRENT_LIST` (:88–89) -> addTorrents(fetchTorrents(...)) (:89); null action or other action -> Result.failure(). |
| 11 | FeedDownloaderWorker.fetchTorrent (Lorg/proninyaroslav/libretorrent/core/model/data/entity/FeedItem;)Lorg/proninyaroslav/libretorrent/core/model/AddTorrentParams; | REACHABLE proposed | INFERRED | Call FDW.fetchTorrents:101 inside the repo.getItemsById loop; chain via doWork (INFERRED). Body FDW:109–190: magnet branch via engine.parseMagnet (:125), else HTTP fetch + TorrentMetaInfo (:140–141), temp-file write, AddTorrentParams construction (:178–189). |
| 12 | FeedDownloaderWorker.fetchTorrents ([Ljava/lang/String;)Ljava/util/ArrayList; | REACHABLE proposed | INFERRED | Call FDW.doWork:89; chain via doWork (INFERRED). Body FDW:94–107: null-ids guard, loop repo.getItemsById -> fetchTorrent (:101). |
| 13 | FeedFetcherWorker.<clinit> ()V | REACHABLE proposed | INFERRED | JVM class-init rule unprinted, hence INFERRED. First printed class reference: SCH.runPeriodicalRefreshFeeds:116 `PeriodicWorkRequest.Builder(FeedFetcherWorker.class, ...)` (R3). Static TAG field FFW:53. |
| 14 | FeedFetcherWorker.<init> (Landroid/content/Context;Landroidx/work/WorkerParameters;)V | REACHABLE proposed | INFERRED | Definition FFW:67–70 (super(context, params)). WorkManager instantiates the Worker; dispatch unprinted, hence INFERRED. Enqueue site R3, SCH:116–125. |
| 15 | FeedFetcherWorker.deleteOldItems (J)V | REACHABLE proposed | INFERRED | Call FFW.doWork:83; chain via doWork (INFERRED). Body FFW:206–210: runs repo.deleteItemsOlderThan only if keepDateBorderTime > 0. |
| 16 | FeedFetcherWorker.doWork ()Landroidx/work/ListenableWorker$Result; | REACHABLE proposed | INFERRED | WorkManager dispatch INFERRED (R3, SCH:116–125, input ACTION_FETCH_ALL_CHANNELS at SCH:114). Body FFW:74–105: deleteOldItems (:83), action switch — FETCH_CHANNEL -> fetchChannel (:94–95), FETCH_CHANNEL_LIST -> fetchChannelsByUrl (:97–98), FETCH_ALL_CHANNELS -> fetchChannels (:100–101). |
| 17 | FeedFetcherWorker.fetchChannel (JJZ)Landroidx/work/ListenableWorker$Result; | REACHABLE proposed | INFERRED | Calls FFW.doWork:94–95, fetchChannelsByUrl:115, fetchChannels:134; chain via doWork (INFERRED). Body FFW:144–187: repo.getFeedById, FeedParser, filterItems (:167), filterItemDuplicates if pref.feedRemoveDuplicates (:169–170), repo.addItems, sendFetchedItems if !noAutoDownload && channel.autoDownload (:183–184). |
| 18 | FeedFetcherWorker.fetchChannels (Ljava/util/List;JZ)Landroidx/work/ListenableWorker$Result; | REACHABLE proposed | INFERRED | Call FFW.doWork:100–101 for ACTION_FETCH_ALL_CHANNELS — the action SCH puts in the periodic input data (SCH:114, R3). Body FFW:124–142: loop over channels -> fetchChannel (:134). |
| 19 | FeedFetcherWorker.fetchChannelsByUrl ([JJZ)Landroidx/work/ListenableWorker$Result; | REACHABLE proposed | INFERRED | Call FFW.doWork:97–98 for ACTION_FETCH_CHANNEL_LIST. Body FFW:107–122: loop over ids -> fetchChannel (:115). |
| 20 | FeedFetcherWorker.filterItemDuplicates (Ljava/util/List;)V | REACHABLE proposed | INFERRED | Call FFW.fetchChannel:169–170, gate pref.feedRemoveDuplicates(); chain via doWork (INFERRED). Body FFW:196–204. |
| 21 | FeedFetcherWorker.filterItems (JLjava/util/List;J)V | REACHABLE proposed | INFERRED | Call FFW.fetchChannel:167; chain via doWork (INFERRED). Body FFW:189–194, incl. removeIf lambda (row 24). |
| 22 | FeedFetcherWorker.isMatch (Lorg/proninyaroslav/libretorrent/core/model/data/entity/FeedItem;Ljava/lang/String;Z)Z | REACHABLE proposed | INFERRED | Call FFW.sendFetchedItems:219; chain via doWork (INFERRED). Body FFW:239–269: empty-filter -> true (:241–242), regex vs word matching. |
| 23 | FeedFetcherWorker.lambda$filterItemDuplicates$1 (Ljava/util/List;Lorg/proninyaroslav/libretorrent/core/model/data/entity/FeedItem;)Z | REACHABLE proposed | INFERRED | Body FFW:203 `items.removeIf(item -> item != null && existingTitles.contains(item.title))` inside filterItemDuplicates. Lambda numbering by source order across the class: filterItems removeIf (:193) is $0, this one is $1 — matches the plan descriptor (List,FeedItem)Z. Numbering is source-order inferred, NOT bytecode-confirmed. Runs via filterItemDuplicates (INFERRED route). |
| 24 | FeedFetcherWorker.lambda$filterItems$0 (JLjava/util/List;Lorg/proninyaroslav/libretorrent/core/model/data/entity/FeedItem;)Z | REACHABLE proposed | INFERRED | Body FFW:193 `items.removeIf(item -> item != null && (item.pubDate > 0 && item.pubDate <= acceptMinDate \|\| existingItemsId.contains(item.id)))` inside filterItems. First lambda in the class in source order, hence $0. Runs via filterItems (INFERRED route). |
| 25 | FeedFetcherWorker.sendFetchedItems (Lorg/proninyaroslav/libretorrent/core/model/data/entity/FeedChannel;Ljava/util/List;)V | REACHABLE proposed | INFERRED | Call FFW.fetchChannel:184, gate !noAutoDownload && channel.autoDownload (:183); chain via doWork (INFERRED). Body FFW:212–237: isMatch filter (:219), markAsRead (:221), builds FDW input data (:228–231) and enqueues FDW work (:232–236) — this is R4. |
| 26 | SaveLogWorker.<clinit> ()V | REACHABLE proposed | INFERRED | JVM class-init rule unprinted, hence INFERRED. First printed class reference: LVM.saveLog:208 `OneTimeWorkRequest.Builder(SaveLogWorker.class)` (R5). Static TAG field SLW:47. |
| 27 | SaveLogWorker.<init> (Landroid/content/Context;Landroidx/work/WorkerParameters;)V | REACHABLE proposed | INFERRED | Definition SLW:57–60 (super(context, params)). WorkManager instantiates the Worker; dispatch unprinted, hence INFERRED. Enqueue site R5, LVM:208–212. |
| 28 | SaveLogWorker.doWork ()Landroidx/work/ListenableWorker$Result; | REACHABLE proposed | INFERRED | WorkManager dispatch INFERRED (R5, LVM:208–212). Body SLW:64–82: engine/fs setup (:66–68), null filePath -> showFailToast + Result.failure() (:72–77), else saveLog(Uri.parse(filePath), resume) (:81). |
| 29 | SaveLogWorker.lambda$showFailToast$0 ()V | REACHABLE proposed | INFERRED | Body SLW:114–118 `handler.post(() -> Toast.makeText(... journal_save_log_failed ...).show())` inside showFailToast. First lambda in the class in source order, hence $0. Handler dispatch also unprinted; runs via showFailToast (INFERRED route). |
| 30 | SaveLogWorker.lambda$showSuccessToast$1 (Ljava/lang/String;)V | REACHABLE proposed | INFERRED | Body SLW:123–127 `handler.post(() -> Toast.makeText(... journal_save_log_success, fileName ...).show())` inside showSuccessToast. Second lambda in the class in source order, hence $1; descriptor (String)V matches the captured fileName parameter. Runs via showSuccessToast (INFERRED route). |
| 31 | SaveLogWorker.saveLog (Landroid/net/Uri;Z)Landroidx/work/ListenableWorker$Result; | REACHABLE proposed | INFERRED | Call SLW.doWork:81; chain via doWork (INFERRED). Body SLW:84–110: logger.pause, write/stopRecording to the file, showSuccessToast (:97), logger.resume in finally if resume (:105–106). |
| 32 | SaveLogWorker.showFailToast ()V | REACHABLE proposed | INFERRED | Call SLW.doWork:74 (null filePath branch); chain via doWork (INFERRED). Body SLW:112–119, posts row 29's lambda. |
| 33 | SaveLogWorker.showSuccessToast (Ljava/lang/String;)V | REACHABLE proposed | INFERRED | Call SLW.saveLog:97; chain via doWork (INFERRED). Body SLW:121–128, posts row 30's lambda. |
| 34 | Scheduler.cancelPeriodicalRefreshFeeds (Landroid/content/Context;)V | REACHABLE proposed | SOURCE | Direct call FSF:136 (auto-refresh turned off branch). Body SCH:142–144: WorkManager.cancelAllWorkByTag(SCHEDULER_WORK_PERIODICAL_REFRESH_FEEDS). No worker dispatch is crossed to reach this method itself. |
| 35 | Scheduler.cancelStartAppAlarm (Landroid/content/Context;)V | REACHABLE proposed | SOURCE | Direct call SSF:204 (scheduling-start turned off branch). Body SCH:60–68: PendingIntent for SchedulerReceiver + AlarmManager.cancel (:67). |
| 36 | Scheduler.cancelStopAppAlarm (Landroid/content/Context;)V | REACHABLE proposed | SOURCE | Direct call SSF:217 (scheduling-shutdown turned off branch). Body SCH:70–78: PendingIntent for SchedulerReceiver + AlarmManager.cancel (:77). |
| 37 | Scheduler.getRefreshFeedsConstraints (Landroid/content/Context;)Landroidx/work/Constraints; | REACHABLE proposed | SOURCE | Direct call SCH.runPeriodicalRefreshFeeds:120. Body SCH:128–140: network type from settings (CONNECTED, NOT_ROAMING if roaming allowed, UNMETERED if unmetered-only), Constraints built (:137–139). Private method; its only printed caller is row 38. |
| 38 | Scheduler.runPeriodicalRefreshFeeds (Landroid/content/Context;J)V | REACHABLE proposed | SOURCE | Direct calls FSF:134 (auto-refresh on) and FSF:142 (interval changed). Body SCH:112–126: input data ACTION_FETCH_ALL_CHANNELS (:113–115), PeriodicWorkRequest for FFW (:116–122, constraints row 37 at :120), enqueueUniquePeriodicWork REPLACE (:124–125). The WorkManager dispatch that follows is the entry to FFW, not a step needed to reach this method. |
| 39 | Scheduler.setStartAppAlarm (Landroid/content/Context;I)Z | REACHABLE proposed | SOURCE | Direct calls SSF:200 and SSF:223, and SR.onStartApp:73 / SR.onStopApp:92. Body SCH:52–54: delegates to setStartStopAppAlarm with SCHEDULER_WORK_START_APP. |
| 40 | Scheduler.setStartStopAppAlarm (Landroid/content/Context;Ljava/lang/String;I)Z | REACHABLE proposed | SOURCE | Direct calls SCH.setStartAppAlarm:53 and SCH.setStopAppAlarm:57 (batch 72 row 1). Body SCH:80–106: builds SchedulerReceiver intent + PendingIntent (:93–98), API gate `SDK_INT >= S && !canScheduleExactAlarms -> false` (:101–103) — at API 27 (S = 31) this gate is false, so it does not close the route — then AlarmManager.setExactAndAllowWhileIdle (:104), returns true (:105). |

## Counts — mechanically verified

- 40 rows, sequence 1–40 intact, in plan order.
- **40 REACHABLE proposed / 0 UNREACHABLE proposed / 0 OPEN.**
- SOURCE 8 / INFERRED 32.
- **0 rows verified for merge.** Verification requires, in order: the main agent's
  1-in-5 spot-check of this part, `py_compile` + build on a full checkout, and the
  Mac build/C1 return — none of which has happened here.

## OPEN rows and what would resolve them

None. Every row has a printed route above.

## Caveats / merger must-do

1. TorrentEngine gap CLOSED in this session (see "Printed source used"): fresh
   fetch SHA `17d06efe…` matches the prior session's SHA. The remaining merger
   items below are unchanged.
2. Strict-entry caveat: no printed launcher -> TorrentService step and no printed
   step showing the settings fragments from SettingsActivity were printed in the
   prior session (manifest LAUNCHER MainActivity is printed, but the
   MainActivity -> fragment / MainActivity -> TorrentService steps are not).
   Under a strict launcher-entry rule, all 40 REACHABLE rows revert to OPEN.
   This convention is recorded, NOT decided here. This does not change the proposed counts.
3. Lambda numbering ($0/$1 in FFW and SLW) is source-order inferred, NOT
   bytecode-confirmed. Merger must confirm against bytecode if disputed;
   the bodies cited are unambiguous regardless of the number.
4. SchedulerReceiver.onStopApp:92 calls setStartAppAlarm (not setStopAppAlarm)
   in the file as printed. That is upstream code as-is, not a proposal error;
   do not "fix" the citation to setStopAppAlarm.
5. No UNREACHABLE row is claimed: no saved full-repo grep was run. In
   particular, do NOT flip any row on the basis that its caller was not
   found in the printed subset.
6. No build, sampler, grep, or C1 check was run; 0/40 verified for merge.

## What this part is not

- Not a merge: `graph_def.py` is untouched, and this file is not in `graph_def.py` format.
- Not a claim about batches 1–70, 72–120, about any other app, or about device replay.
- Not a claim that the plan's TODO_CANDIDATE_REACHABLE labels are verified: they
  happen to agree with the proposals here, but agreement with the plan is not verification.
