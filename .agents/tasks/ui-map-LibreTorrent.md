# LibreTorrent 3.5.2 (org.proninyaroslav.libretorrent.debug): UI map and modeling plan

Read-only investigation for the trigger-graph build. Nothing in the app folder was changed.

## Summary

- **One launcher screen, no onboarding, no account, no vault.** The only first-run gate is the WRITE_EXTERNAL_STORAGE runtime permission (API 27). The baseline evidently ran with it pre-granted: `MainActivity$1.onStorageResult` and `Utils.shouldRequestStoragePermission` never ran, while the empty-array permission callback `MainActivity$1.onNotificationResult` ran in both tools.
- **What actually stopped the baseline is an empty torrent list.** `TorrentListItem.<init>` never ran in either run, so the whole torrent-details area never ran (596 methods; 0 hits from either tool). The same goes for the main-list selection/action mode and most per-torrent engine code (`TorrentDownloadImpl`, 122 methods, 0 hits). The fixtures have no `.torrent` file. In the add flow, decoding was attempted and failed every time (`AddTorrentViewModel.makeFileTree` and `TorrentEngine.fetchMagnet` never ran).
- **Feeds stop at "channel added".** `FeedParser.<init>` threw every time, so there are no feed items. The bundled `com.ernieyu.feedparser` (179 methods) has 0 hits. This needs a reachable RSS/Atom URL.
- **Selection mode was never entered in any list.** No `ItemLookup.getItemDetails` ran, even though APE tapped feed rows. The four action-mode pages (main, feeds, detail files, detail trackers) are therefore unreached. A tool-type hypothesis is in §2.3 (UNVERIFIED).
- **Coverage blind spot.** `ErrorReportActivity` runs in the `:acra` process, and the coverage receiver only dumps the main process. Its 0 hits say nothing, even though APE logged 2 app crashes.
- **Size.** 4728 JaCoCo methods (705 of them generated data-binding code). Monkey hit 1560, APE 2063, either 2080, neither 2648.
- **Dead-code candidates (no bytecode caller):**
  - 238 generated binding helpers: the static `inflate`/`bind` of 37 binding classes, plus 16 getters.
  - 86 hand-written methods.
  - 12 methods gated by API level or flavor, and about 43 tablet-only methods (§5.3).
- **Plan proposed below:** 104 candidate pages and 8 feature areas, covering all 688 class files. Leftovers are 3 JacocoInstrument classes (excluded) and 23 enum switch-map classes that JaCoCo does not report.

Path abbreviations used below:
- `J/` = `/Users/darshan/Desktop/yang/work/final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`
- `RES/` = `.../app/src/main/res/`
- `MF` = `.../app/src/main/AndroidManifest.xml`
- `DBG/` = `.../app/src/debug/res/`
- `CLS/` = `.../app/build/intermediates/javac/baseDebug/compileBaseDebugJavaWithJavac/classes/`
- MK = Monkey and AP = APE JaCoCo report (`.../LibreTorrent/{monkey,ape}/report/report.xml`). A "hit" is a METHOD counter with covered > 0.

Evidence labels: SRC (read in app source), FW-MEMORY (Android/library behaviour recalled, not checked; no framework source is available offline), INFERRED, UNVERIFIED.

### What was read
- **Read in full:**
  - the manifest, the debug shortcuts, `build.gradle`
  - all menus, the preference XMLs, the layout aliases/bools
  - the binding expressions of every screen layout
  - every class in `ui/**`, `service/**`, `receiver/**`, `MainApplication`
  - `core/utils/Utils`, `core/FeedParser`, `core/RepositoryHelper`, `core/storage/AppDatabase`, `TorrentEngine.java:90-510` and `:1046-1175`
- **Read in part:** `TorrentSessionImpl` (add/magnet/restore), `TorrentInfoProvider`, `SettingsRepositoryImpl` (defaults, change observer), `SafFileSystem`, `FileSystemFacadeImpl`.
- **Not read line by line:** `TorrentDownloadImpl`, `NanoHTTPD`, the `com.ernieyu.feedparser` sources, the Room/DataBinding generated code (only bytecode is available for the generated code).
- **Bytecode analysis:** a read-only Python class-file parser extracted every Methodref/InterfaceMethodref and invokedynamic MethodHandle from all 688 class files. It found which never-hit methods have no caller anywhere in the APK code (§5).

---

## 1. Entry points

No merged manifest exists: `app/build/intermediates` contains only `javac/` (checked with `find`). The base flavor has no source set of its own (`src/` has androidTest, debug, main, play, release, test). So the components come from `MF`, with the debug build-type resources (`applicationIdSuffix '.debug'`, `build.gradle` debug block) layered on top. `src/play/AndroidManifest.xml` (removes MANAGE_EXTERNAL_STORAGE) is not part of this APK.

The application class is `MainApplication` (`MF:31-41`). No activity declares `configChanges`, and only ErrorReportActivity sets a `launchMode`, so rotation recreates every activity. Permissions are at `MF:5-20`, including WRITE/READ/MANAGE_EXTERNAL_STORAGE, POST_NOTIFICATIONS, SCHEDULE_EXACT_ALARM, RECEIVE_BOOT_COMPLETED and FOREGROUND_SERVICE_DATA_SYNC.

| Component | Exported | Intent filters / entry | Theme / mode | Cite |
|---|---|---|---|---|
| `MainApplication` (MultiDexApplication) | – | Process start. `onCreate` runs ACRA.init with the dialog = ErrorReportActivity, then `increaseCursorWindowSize`, then `TorrentNotifier.makeNotifyChans` | – | `J/MainApplication.java:45-71` |
| `ui.main.MainActivity` | yes | MAIN + LAUNCHER + LEANBACK_LAUNCHER; `android.intent.action.SEARCH` (meta `@xml/searchable`, no code reads the query); meta `android.app.shortcuts` | `AppTheme.Launcher` (splash background); real theme set in `onCreate` (`MainActivity.java:137`) | `MF:43-60`, `RES/xml/searchable.xml` |
| ↳ static shortcut "addTorrent" | – | action `org.proninyaroslav.libretorrent.ADD_TORRENT_SHORTCUT` → MainActivity → `MainFragment.showAddTorrentMenu` (context menu) | – | `DBG/xml-v25/shortcuts.xml:6-16`, `J/ui/main/MainFragment.java:202-221` |
| ↳ static shortcut "addFeed" | – | VIEW → AddFeedActivity | – | `DBG/xml-v25/shortcuts.xml:18-28` |
| ↳ intent action `NOTIFY_ACTION_SHUTDOWN_APP` | – | Started by NotificationReceiver; `onCreate` finishes immediately | – | `MainActivity.java:140-144` |
| `ui.addtorrent.AddTorrentActivity` | yes | SEND+DEFAULT with no type (`MF:65-68`). VIEW+BROWSABLE: file/content with mime `application/x-bittorrent`; file/content with path `.*\.torrent`; http/https with path `.*\.torrent` (with and without `*/*`); http/https with mime x-bittorrent; scheme `magnet`. The URI comes from `getData()`, else `EXTRA_TEXT`, else the extra `uri` | default | `MF:62-135`, `AddTorrentActivity.java:350-360` |
| `ui.filemanager.FileManagerDialog` | no | Internal only (needs extra `config`, else `finish`) | normal activity | `MF:137`, `FileManagerDialog.java:124-129` |
| `ui.detailtorrent.DetailTorrentActivity` | no | From MainActivity (phone) and from the "torrent finished" notification (action `ACTION_OPEN_FILES`) | finishes itself in two-pane | `MF:139`, `DetailTorrentActivity.java:52-77`, `J/ui/TorrentNotifier.java:230-239` |
| `ui.SendTextToClipboard` | yes | SEND + DEFAULT + ALTERNATIVE, mime `text/*` (label "Copy to clipboard") | `@android:style/Theme.NoDisplay`; copies EXTRA_TEXT, toasts, finishes | `MF:141-153`, `SendTextToClipboard.java:37-61` |
| `ui.settings.SettingsActivity` | yes | `android.intent.action.APPLICATION_PREFERENCES` | `AppTheme.Settings*` set in code | `MF:155-162`, `SettingsActivity.java:41-62` |
| `ui.settings.PreferenceActivity` | no | Hosts one settings section (extra `config`) | finishes on large screens | `MF:164-165`, `PreferenceActivity.java:51-83` |
| `ui.errorreport.ErrorReportActivity` | no | Started by ACRA after a crash (FW-MEMORY) | `AppTheme.Translucent`, `process=":acra"`, `launchMode=singleInstance`, `excludeFromRecents`, `finishOnTaskLaunch` | `MF:167-172` |
| `ui.feeds.FeedActivity` | no | From the Main menu "Feed" | default | `MF:174`, `MainActivity.java:740-741` |
| `ui.feeditems.FeedItemsActivity` | no | From FeedFragment row tap (phone) | finishes in two-pane | `MF:176`, `FeedActivity.java:220-224` |
| `ui.addfeed.AddFeedActivity` | yes | SEND+DEFAULT (no type); VIEW+BROWSABLE http/https host * mime `*/*` path `.*\.xml` or `.*\.rss`; VIEW http/https with mime text/xml, application/rss+xml, application/atom+xml, application/xml. Edit mode through internal action `ACTION_EDIT_FEED`. The `<data android:name=...>` entries are not valid data attributes (ignored, FW-MEMORY) | `AppTheme.Translucent` (hosts a DialogFragment) | `MF:178-228`, `AddFeedActivity.java:46-81` |
| `ui.createtorrent.CreateTorrentActivity` | no | Main FAB "Create torrent" | `AppTheme.Translucent` | `MF:230-232` |
| `ui.addlink.AddLinkActivity` | no | Main FAB / context menu "Add link" | `AppTheme.Translucent` | `MF:234-236` |
| `ui.log.LogActivity`, `ui.log.LogSettingsActivity` | no | Main menu "Log"; Log menu "Log settings" | default | `MF:238-242` |
| `ui.addtag.AddTagActivity`, `ui.tag.SelectTagActivity` | no | Drawer / tag popup / SelectTag "New tag"; Add/Detail info "+" tag chip | `AppTheme.Translucent` | `MF:244-250` |
| `service.TorrentService` | no | `startForegroundService` from `TorrentEngine.start`, `restartForegroundNotification`, `forceStop` (ACTION_SHUTDOWN); `startService` from NotificationReceiver. `foregroundServiceType=dataSync`. START_STICKY; `onBind` returns null | – | `MF:252-254`, `TorrentService.java:98-197`, `J/core/utils/Utils.java:426-434` |
| `receiver.NotificationReceiver` | no | Listed actions are SHUTDOWN_APP and ADD_TORRENT, but it is reached only through explicit PendingIntents from the foreground notification (pause all, resume all, pause/resume all, shutdown). The ADD_TORRENT branch has no sender in the app | – | `MF:256-263`, `NotificationReceiver.java:41-82`, `TorrentService.java:497-520` |
| `receiver.BootReceiver` | yes | BOOT_COMPLETED, QUICKBOOT_POWERON (android and htc), SCHEDULE_EXACT_ALARM_PERMISSION_STATE_CHANGED. The component is disabled at run time unless autostart or scheduling is on (`Utils.enableBootReceiverIfNeeded`, called from `TorrentService.init`) | – | `MF:265-274`, `BootReceiver.java:38-73`, `Utils.java:449-460`, `TorrentService.java:128` |
| `receiver.SchedulerReceiver` | no (no filter) | AlarmManager PendingIntent with action `scheduler_work_start_app` or `scheduler_work_stop_app` | – | `MF:276-277`, `J/service/Scheduler.java:80-106` |
| `androidx.core.content.FileProvider` | no | Authority `${applicationId}.provider` = `org.proninyaroslav.libretorrent.debug.provider`, `root-path .` (library code; used to open downloaded files) | – | `MF:279-287`, `RES/xml/provider_paths.xml` |
| `JacocoInstrument.SMSInstrumentedReceiver` | yes | `edu.gatech.m3.emma.COLLECT_COVERAGE` (excluded harness; dumps only its own process) | – | `MF:288-293`, `J/JacocoInstrument/SMSInstrumentedReceiver.java:13-24` |
| Dynamic receivers | – | PowerReceiver (registered only with battery or only-charging settings); ConnectionReceiver (registered when "unmetered only" or "roaming" is set; roaming defaults to true, so it is on by default); FileManagerDialog.MediaReceiver (MEDIA_MOUNTED/UNMOUNTED while the file manager is open) | – | `TorrentEngine.java:993-1022` (`switchPowerReceiver`/`switchConnectionReceiver`; register calls at :1001, :1005, :1020), `FileManagerDialog.java:281-295`, `SettingsRepositoryImpl.java:75-76` |

There are no widgets, no app-defined ContentProvider, no WebView, no JobScheduler and no ShortcutManager code (grep over `J/` found no matches).

---

## 2. First-run flow and setup gates

### 2.1 Launch sequence (SRC)
1. `MainApplication.onCreate`: ACRA, cursor window, notification channels (`MainApplication.java:45-71`).
2. `MainActivity.onCreate`:
   - creates `PermissionManager` (`MainActivity.java:153-173`);
   - `if (!checkPermissions() && permDeniedDialog == null) requestPermissions()` (`:177-179`);
   - `Utils.showManageAllFilesWarningDialog` (`:180`);
   - `setContentView(activity_main)`, which is `activity_main_drawer` on phones (`RES/values/layouts.xml:3`, `RES/values-sw600dp-land/layouts.xml:3`);
   - drawer and toolbar setup (`:191-293`).
3. On API 27 `checkNotificationsPermissions()` always returns false (`PermissionManager.java:137-144`), so `checkPermissions()` is always false (`:146-148`) and `requestPermissions()` runs on **every** creation of Main, AddTorrent and CreateTorrent.
   - If storage is already granted, the permission array is empty. FW-MEMORY: `RequestMultiplePermissions` then returns an immediate empty result.
   - The callback sets `notificationsResult = true` (below API 33; `PermissionManager.java:75-79`), so `onNotificationResult(true)` runs `viewModel.restartForegroundNotification()` (`MainActivity.java:166-172`).
4. `onStart` subscribes to `observeNeedStartEngine` and calls `engine.start()`, which runs `startForegroundService(TorrentService)`. `TorrentService.init` then runs `engine.doStart()` and the libtorrent session starts asynchronously (`MainActivity.java:380-389, 463-468`; `TorrentEngine.java:148-153, 234-261`; `TorrentService.java:116-135`).
5. Session started: if enabled, the IP filter, watch dir and streaming server (127.0.0.1:8800 by default) start, then the saved torrents are restored (`TorrentEngine.java:1046-1061`; defaults at `SettingsRepositoryImpl.java:161-163`).

### 2.2 Gates (what must hold before parts of the UI are usable)

| # | Gate | Enforced by | Effect if missing | Baseline evidence |
|---|---|---|---|---|
| G1 | WRITE_EXTERNAL_STORAGE granted (runtime, API 23-29). On API ≥ 30 in the base flavor, MANAGE_EXTERNAL_STORAGE goes through Settings | `PermissionManager.java:96-114, 128-135` | System dialog. If denied with rationale, `PermissionDeniedDialog` (Yes = `setDoNotAskStorage`, a no-op on API 27; No = ask again). File manager listings and downloads fail | Granted at install (INFERRED, e.g. `adb install -g`): `MainActivity$1.onStorageResult`, `AddTorrentActivity$1.onStorageResult` and `Utils.shouldRequestStoragePermission` have 0 hits in MK and AP, while `PermissionManager.lambda$new$1` hit in both |
| G2 | **≥1 torrent in the session/DB** | `MainFragment.observeTorrents` (`MainFragment.java:285-300`); TorrentListAdapter rows (`TorrentListAdapter.java:171-202`) | No rows: no details screen, no selection/action mode, no delete/recheck/announce/pause, no streaming, no "finished" notification | `TorrentListItem.<init>`, `TorrentListAdapter$ViewHolder.bind`, every `ui/detailtorrent/**` method and every `TorrentDownloadImpl` method: 0 hits in MK and AP |
| G3 | A **decodable source** for the add screen: a valid `.torrent` (file or content URI), a reachable http(s) `.torrent`, or a valid magnet (40-hex btih). `AddLinkViewModel` turns any 5-40 hex string into `magnet:?xt=urn:btih:<hex>` | `AddTorrentViewModel.TorrentDecodeTask.doInBackground` (`AddTorrentViewModel.java:217-279`); `Utils.HASH_PATTERN` (`Utils.java:120`); `AddLinkViewModel.java:61-73` | Error dialog; no file tree; Add does nothing (`addTorrent` returns false when `info == null`, `:466-469`) | `readTorrentFile` and `handleDecodeException` hit (MK, AP); `makeFileTree`, `AddTorrentViewModel$1.onPropertyChanged`, `lambda$addTorrent$5` 0; `TorrentEngine.fetchMagnet` 0 (although AP hit `Utils.normalizeMagnetHash`); `DownloadableFileItem` 0 |
| G4 | Metadata present for the per-file UI (details Files and Pieces tabs, priorities, stream URL, open file) | `DetailTorrentViewModel.makeFileTree` returns early without metaInfo/files (`DetailTorrentViewModel.java:529-568`); `RES/layout/fragment_detail_torrent_files.xml:31,39` | A magnet-only torrent (added offline) shows a progress placeholder instead of files | – |
| G5 | Engine running | `AddTorrentViewModel.startDecode` waits for `observeEngineRunning` (`:182-195`); `fetchMagnet`/`addTorrentSync` return null when not running (`TorrentEngine.java:401-425`) | Add screen stalls | The session did start: `TorrentEngine$5.onSessionStarted` and `handleOnSessionStarted` hit in MK and AP |
| G6 | Network content: a reachable feed URL, http torrent link, peers/DHT, trackers | `Utils.fetchHttpUrl` (`Utils.java:462-526`) needs `checkConnectivity`; `FeedParser.<init>` (`J/core/FeedParser.java:62-82`) | Feed channel shows "fetch error"; no feed items; trackers/peers empty; magnet metadata never arrives | `FeedParser.<init>` hit (AP) but `getItems`/`getTitle` 0; `FeedItem` 0; feedparser 0/179; `Utils.fetchHttpUrl` and `HttpConnection.run` hit (AP) and failed. Emulator network state: UNVERIFIED |
| G7 | ≥1 user tag (for tag rows, edit, select) | `MainActivity.subscribeTags` (`:470-488`); `SelectTagDialog.subscribeTags` (`SelectTagDialog.java:165-176`) | Only the "All" and "No tags" pseudo items | AP created a tag (`AddTagViewModel.saveTag`, `TagsAdapter$ItemViewHolder.bind(TagItem)` AP only); MK 0 |
| G8 | Settings-gated features: watch dir, IP filtering (+file), battery control, scheduling, feed auto-refresh, proxy, anonymous mode, "move after download", streaming (on by default) | `TorrentEngine.handleSettingsChanged`/`handleOnSessionStarted` (`TorrentEngine.java:1046-1061, ~1457-1575`); `Scheduler.java:80-126` | Code paths dormant | Watch-dir observer was started (`TorrentEngine$4.onEvent` hit MK, AP) but no `.torrent` event (`lambda$onEvent$0` 0) |
| G9 | Time / boot / OS events: alarm time reached, device boot, power or battery change, SD mount | `SchedulerReceiver`, `BootReceiver` (disabled unless autostart/scheduling, `Utils.java:449-460`), `PowerReceiver`, `FileManagerDialog.MediaReceiver` | Receivers never run | All 0 |
| G10 | Things outside the app package: share sheet (SEND text → SendTextToClipboard; SEND/VIEW → AddTorrent/AddFeed), launcher shortcuts, notification shade, APPLICATION_PREFERENCES, external HTTP client for the stream server | `MF` filters; `TorrentStreamServer.serve` | Unreached by `-p`-restricted tools (FW-MEMORY: Monkey's controller blocks activity starts outside the package) | `SendTextToClipboard` 0, `MainFragment.showAddTorrentMenu` 0, `TorrentStreamServer.serve` 0; `NotificationReceiver.onReceive` hit by MK only (Monkey reached the notification shade) |

### 2.3 Screens the baseline never reached, and the likely gate (per-class JaCoCo)

| Never reached (MK and AP) | Methods | Likely gate |
|---|---|---|
| `DetailTorrentActivity`, `DetailTorrentFragment`, the 6 tab fragments, their adapters and dialogs, `DetailTorrentViewModel` | 596 (all of DETAIL) | G2: no torrent ever added (G3 failed every time) |
| Main list rows, `MainFragment$2.onSelectionChanged`/`$3` action mode, delete-torrents dialog, open-file error dialog | `MainFragment` 30/63 (MK), 31/63 (AP); `TorrentListAdapter` 6/27 | G2. The open-file error needs RESULT_OK with null data, which FileManagerDialog never returns (INFERRED) |
| AddTorrent "ready" states (file tree, Add success), `DownloadableFilesAdapter.onBindViewHolder`, `AddTorrentFilesFragment.onItemClicked`/`onItemCheckedChanged` | `AddTorrentViewModel` 26/43 | G3 |
| CreateTorrent build (`CreateTorrentViewModel.buildTorrent`, `onBuildSuccess`, `downloadTorrent`), `core/TorrentBuilder` (22) | 13/34 + 0/22 | Multi-step form. AP reached `choosePathToSaveDialog`, but the save-path result was never RESULT_OK (`CreateTorrentDialog.lambda$new$11` hit, `buildTorrent` 0) |
| FeedItems rows, item popup, item click → add torrent, `FeedDownloaderWorker`, `com.ernieyu.feedparser.**` | Feed items 40/71 (AP only; 0 in MK), feedparser 0/179 | G6 |
| Feed selection/action mode, AddFeed **edit** mode, delete feed dialogs | `FeedFragment` 24/49 | Selection never entered (below); edit mode is only reachable from the action mode |
| AddTag **edit** mode (`AddTagViewModel.setInitValues` 0) | – | AP chose "Delete" in the tag popup, never "Edit" (`MainActivity$3.lambda$onTagMenuClicked$0` hit) |
| Restore-feeds success/error, replace-file dialog, custom-battery dialog, IP-filter file chooser, theme "Apply" snackbar | small | Chance plus missing fixtures (no feed backup JSON, no IP-filter file) |
| `PermissionDeniedDialog` | 3 | G1 satisfied |
| `ManageAllFilesWarningDialog` | 3 | API ≥ 30 **and** play flavor only (§5); unreachable in this build |
| `ErrorReportActivity` | 9 | Needs a crash, and runs in `:acra`, so it is **unmeasurable** with this coverage harness (`SMSInstrumentedReceiver` dumps only the process it runs in, `SMSInstrumentedReceiver.java:13-24`). APE logged `app_crashes=2` (`final_java_only/summary_ape_api27.csv`) |
| `SendTextToClipboard`, the shortcut context menu, `BootReceiver`, `SchedulerReceiver`, `PowerReceiver.onReceive`, `SaveLogWorker`, `TorrentStreamServer.serve` | – | G9/G10 (outside the app package, time, boot, power) |
| `BlankFragment`, every two-pane branch, `*Sw600dpLandImpl`/`*LargeLandNotouchImpl` bindings | 3 + 38 | Phone emulator: `BlankFragment` 0 although `showBlankFragment` is called on every launch (`MainActivity.java:192, 676-685`) |
| Reached only by APE | – | AddTag/SelectTag; FeedItems; LogSettings; settings Behavior, Network, Limitations, Scheduling, Streaming, Proxy, Anonymous; About dialog; drawer item/tag taps. Monkey reached Settings, Appearance, Storage, Feed settings, Log and Feed |

**Selection never entered (UNVERIFIED cause).** In every selection-enabled list, `ItemLookup.getItemDetails`, `KeyProvider.getKey` and `SelectionObserver.onSelectionChanged` have 0 hits in MK and AP. That covers TorrentListAdapter, FeedChannelListAdapter, TorrentContentFilesAdapter and TrackerListAdapter. Yet APE tapped feed rows: `FeedFragment.onItemClicked` hit through the row's `View.OnClickListener` (`FeedChannelListAdapter.java:217-224`). Two explanations are possible:
- Hypothesis (a), FW-MEMORY: Monkey/APE inject MotionEvents with `TOOL_TYPE_UNKNOWN`, and recyclerview-selection 1.1.0 may route by tool type, ignoring them.
- Hypothesis (b): neither tool performed a long press on a row.

To decide, long-press a feed row once through UiAutomator (finger tool type) and once through `adb shell input swipe x y x y 800`, then compare `getItemDetails` coverage.

### 2.4 What a test harness must prepare

1. **Permission.** Grant storage permission (`adb install -g`, or `pm grant <pkg> android.permission.WRITE_EXTERNAL_STORAGE`), as the baseline evidently did.
2. **Torrent files.** Push valid `.torrent` files to `/sdcard/Download/`, the default save, watch and file-manager start directory (`FileSystemFacadeImpl.java:80-90`, `SettingsRepositoryImpl.java:102-104, 120-122`, `FileManagerDialog.java:134`). Include:
   - (a) a single-file torrent built from a fixture file (e.g. `Download/sample.pdf`);
   - (b) a multi-file torrent with a sub-folder (e.g. from `Music/`), which exercises directory navigation in the AddTorrent/Detail file trees (`AddTorrentFilesFragment.java:182-196`, `DetailTorrentFilesFragment.java:331-347`);
   - leave the payload files where the torrent expects them, so recheck turns the torrent into Seeding/Finished. That enables the finished notification, open-file and streaming.
   
   No external tool is needed for (a) in principle: the app's own CreateTorrent flow (file → Add → save as `x.torrent` → OK, optionally with "Start seeding") produces a `.torrent` and a seeding torrent offline (`CreateTorrentViewModel.java:151-175, 352-384`; UNVERIFIED on a device).
3. **Magnet on the clipboard.** Put a magnet on the clipboard, e.g. `magnet:?xt=urn:btih:<40 hex>&dn=test`. `AddLinkViewModel.initLinkFromClipboard` pre-fills it (`AddLinkViewModel.java:45-59`). This adds a metadata-less torrent offline (`TorrentSessionImpl.java:273-277, 344`), which is enough for the detail screen, menus, Info/State/Trackers/Peers tabs and the action modes. The exported `SendTextToClipboard` sets the clipboard from adb: `am start -n <pkg>/org.proninyaroslav.libretorrent.ui.SendTextToClipboard -a android.intent.action.SEND -t text/plain --es android.intent.extra.TEXT "<magnet>"` (INFERRED from `SendTextToClipboard.java:44-51`).
4. **Local HTTP server.** Run a server reachable from the emulator (e.g. host `10.0.2.2`; cleartext is allowed, `MF:40`) serving:
   - an RSS 2.0 or Atom feed whose items carry `.torrent` enclosures and magnet links (`FeedParser.java:89-116`), for the feed and feed-item pages and the auto-download worker;
   - a `.torrent` URL for the Add-link http path.
5. **Feed backup.** Provide a JSON backup in the format of `FeedRepositoryImpl.serializeAllFeeds` (or create one in-run through Feed → Backup) for Restore.
6. **IP filter.** Provide an IP-filter file (`.dat`/`.p2p`) in Download for Network → IP filtering (`IPFilterParser`, `IPFilterImpl`; 11 methods, 0 hits).
7. **Optional pre-seeded data.** The app is debuggable, so a pre-populated DB and prefs can be copied with `run-as` (`databases/libretorrent.db` with torrents, tags and feeds) instead of driving the UI (INFERRED). `allowBackup=true` (`MF:38`).
8. **Settings for gated code** (at run start or as part of tool targets):
   - watch dir on;
   - battery control / only-when-charging, then `dumpsys battery` changes to trigger PowerReceiver;
   - scheduling start/stop 1-2 min in the future, which fires SchedulerReceiver (works on API 27; no exact-alarm permission check below API 31, `Scheduler.java:101-105`);
   - feed auto-refresh;
   - keep-alive off, to see the engine stop on Back (`TorrentEngine.java:275-281`).
9. **Outside-the-app triggers:**
   - `am start -a android.intent.action.VIEW -d magnet:?... -n <pkg>/...AddTorrentActivity`
   - `-a org.proninyaroslav.libretorrent.ADD_TORRENT_SHORTCUT -n <pkg>/...MainActivity`
   - `-a android.intent.action.APPLICATION_PREFERENCES`
   - share text to `SendTextToClipboard`
   - pull down the notification shade (foreground notification actions)
   - `curl http://127.0.0.1:8800/...` from `adb shell` against a stream URL (`DetailTorrentViewModel.getStreamUrl`, `:338-343`)
10. **Tablet AVD (optional).** Only needed if the study wants the two-pane code (sw600dp-land) or the TV layouts (large-land-notouch).

---

## 3. Screens and navigation

### 3.1 Windows and how the user moves between them

No Navigation component (not in `build.gradle` dependencies), no bottom sheets, no WebView (grep). Navigation uses:
- explicit intents;
- `ActivityResultLauncher` (StartActivityForResult) for every picker;
- static `FragmentContainerView`s (`RES/layout/activity_main_drawer.xml:22-24`, `activity_detail_torrent.xml:8-10`, `activity_feed_portrait.xml:12-14`, `activity_feed_items.xml:9-11`, `activity_settings_portrait.xml:11-13`, `activity_log_settings.xml:13-15`);
- `FragmentTransaction.replace` only in two-pane and in PreferenceActivity (`PreferenceActivity.java:85-92`);
- ViewPager2 + TabLayoutMediator in AddTorrent (2 tabs, `AddTorrentActivity.java:288-302`) and Detail (6 tabs, `DetailTorrentFragment.java:185-212`, `DetailPagerAdapter.java:34-75`).

| From | Gesture / event | To | Mechanism, cite |
|---|---|---|---|
| Launcher | tap icon | MainActivity | MAIN/LAUNCHER `MF:52-56` |
| Main toolbar (`RES/menu/main.xml`): search (SearchView, ifRoom) L5-9; Feed (ifRoom) L11; Pause all / Resume all (ifRoom) L16/L21; overflow: Log L26, Settings L29, About L33, Shutdown L37 | menu item | FeedActivity / engine.pauseAll / resumeAll / LogActivity / SettingsActivity / About dialog / `stopEngine`+`finish` | `MainActivity.java:697-759` (listener `toolbar.setOnMenuItemClickListener(this::onOptionsItemSelected)` L702) |
| Main | hamburger or edge swipe | drawer | `ActionBarDrawerToggle` `MainActivity.java:218-225` (FW) |
| Drawer | tap a status/sorting/date item | filter/sort applied, drawer closes | `DrawerExpandableAdapter.java:116` → `MainActivity.onDrawerItemSelected` L610-631 |
| Drawer | tap the tags header; "Add tag" button; tag row; tag ⋮ → Edit/Delete | expand/collapse; AddTagActivity; filter; AddTagActivity (edit) or delete | `MainActivity.java:270-350`; `J/ui/main/drawer/TagsAdapter.java:192-210, 249, 295` |
| Main | FAB (speed dial) → Create torrent / Open file / Add link | CreateTorrentActivity / FileManagerDialog (FILE, highlight `torrent`) / AddLinkActivity | `MainFragment.java:414-450, 523-564` |
| Main (shortcut intent) | context menu Add link / Open file | as above | `MainFragment.java:202-221, 392-412`; `RES/menu/main_context.xml` |
| Main list | tap row; tap pause button; long-press row | DetailTorrentActivity (phone); `pauseResumeTorrent`; selection, then action mode `main_action_mode.xml` (Delete, Force recheck, Force announce, Select all) | `TorrentListAdapter.java:189-202`; `MainFragment.java:378-390, 157-194, 457-499`; `MainActivity.showDetailTorrent` L653-674 |
| FileManagerDialog (OPEN torrent) | pick file | RESULT → `MainFragment.lambda$new$18`, then AddTorrentActivity with extra `uri` | `MainFragment.java:619-636` |
| AddLink dialog | Add | AddTorrentActivity (`uri`), and AddLinkActivity finishes | `AddLinkDialog.java:260-288` |
| AddTorrent | Up / Back; Add (check icon) | finish; `engine.addTorrentSync`, then finish (or snackbar/error dialog) | `AddTorrentActivity.java:551-576, 362-450` |
| AddTorrent Info tab | folder button; "+" tag chip; ✕ on a chip | FileManagerDialog (DIR) → RESULT; SelectTagActivity → RESULT; remove tag | `AddTorrentInfoFragment.java:105-120, 137-213`; `J/ui/tag/TorrentTagsList.java:54-87` |
| CreateTorrent dialog | file / folder buttons; Add | FileManagerDialog FILE / DIR; FileManagerDialog SAVE (mime x-bittorrent), then build | `CreateTorrentDialog.java:257-275, 291-336, 517-548` |
| DetailTorrent toolbar (`RES/menu/detail_torrent.xml`): pause/resume, delete, force recheck, force announce, share magnet, save .torrent, add trackers, speed limit | menu items | dialogs; FileManagerDialog SAVE; share chooser (outside the app) | `DetailTorrentFragment.java:412-606` |
| Detail Info tab | edit name; folder; tag chips | edit-name dialog; FileManagerDialog DIR; SelectTagActivity | `DetailTorrentInfoFragment.java:110-193, 262-323` |
| Detail Files tab | tap dir/".."; tap file; priority checkbox; long-press → action mode (`detail_torrent_files_action_mode.xml`: change priority, share stream URL) | navigate; open-file chooser (outside); `applyPriority`; priority dialog / share | `DetailTorrentFilesFragment.java:331-357, 362-534`; `TorrentContentFilesAdapter.java:166,173` |
| Detail Trackers / Peers | long-press tracker → action mode (share URL, delete, select all); long-press peer → share IP | dialogs / share chooser | `DetailTorrentTrackersFragment.java:295-394`; `PeerListAdapter.java:138`; `DetailTorrentPeersFragment.java:186-201` |
| FeedActivity toolbar (`feed.xml`): refresh, backup, restore; Up | menu | WorkManager refresh; FileManagerDialog SAVE / FILE (highlight `json`) | `FeedActivity.java:109-119, 238-290` |
| Feed list | FAB add; tap row; swipe down; long-press → `feed_action_mode.xml` | AddFeedActivity; FeedItemsActivity (phone); refresh; action mode | `FeedFragment.java:185-188, 340-346, 353-410`; `FeedActivity.java:203-225` |
| Feed items | tap item; ⋮ → popup (`feed_item_popup.xml`); toolbar refresh / mark all read; swipe | AddTorrentActivity (`downloadUrl`) or snackbar; browser (open article, outside); mark read/unread | `FeedItemsFragment.java:245-318`; `FeedItemsAdapter.java:144-167` |
| LogActivity: switch bar; toolbar `log.xml` group (pause/resume, record, save, filter, log settings) | menu | in-place modes; FileManagerDialog SAVE (text/plain); filter dialog; LogSettingsActivity | `LogActivity.java:194-336`; `RES/layout/activity_log.xml:28-33` |
| Settings headers (`RES/xml/pref_headers.xml`) | tap a header | PreferenceActivity with that section (phone) | `SettingsFragment.java:81-241` |
| Network section | Proxy; Anonymous mode; IP-filter file | PreferenceActivity(Proxy); PreferenceActivity(Anonymous) for result; FileManagerDialog FILE | `NetworkSettingsFragment.java:205-297, 380-414` |
| Storage section | 4 directory prefs | FileManagerDialog DIR → RESULT | `StorageSettingsFragment.java:95-271` |
| Notification shade | content tap / Pause all / Resume all / Shutdown (or combined pause) | MainActivity / NotificationReceiver → TorrentService / MainActivity(shutdown)+service | `TorrentService.java:342-366, 455-520`; `NotificationReceiver.java:41-82` |
| "Torrent finished" notification | tap | DetailTorrentActivity with `ACTION_OPEN_FILES` (Files tab) | `TorrentNotifier.java:212-242`; `DetailTorrentActivity.java:73-76` |
| Any app crash | – | ErrorReportActivity (`:acra`) | ACRA config `MainApplication.java:56-59` (FW-MEMORY for the launch) |

Back stack: all standard. Translucent hosts (AddLink, AddFeed, CreateTorrent, AddTag, SelectTag) show a DialogFragment over the paused caller. Each dialog installs a BACK `OnKeyListener` (e.g. `AddLinkDialog.java:92-110`, `AddTagDialog.java:86-101`) that calls `finish(BACK)`, and the host activity then finishes. So the hosts' own `onBackPressed` is effectively bypassed (§5.2). Back on MainActivity finishes it. `onDestroy` calls `requestStopEngine`, which does nothing with the default keep-alive = true (`MainActivity.java:398-404`, `TorrentEngine.java:275-281`, `SettingsRepositoryImpl.java:68`), so the foreground service and process survive into the next launch.

### 3.2 Modes per window (what changes the active handlers or menu items)

| Window | Modes (predicate, cite) |
|---|---|
| MainActivity + MainFragment | **Empty vs list**: `adapter.getItemCount()`; the empty view (`MainFragment.java:151`). **Selection**: `selectionTracker.hasSelection()` starts `main_action_mode` (`:166-194`). **Search expanded**: SearchView listeners (`MainActivity.java:707-735`). **FAB open**: speed-dial items only clickable while open. **Drawer open**; tags section expanded (pref `drawer_tags_is_expanded`, `:277-292`). **Shortcut context menu**. Two-pane (tablet) embeds the detail fragment and BlankFragment (`:653-695`), config-gated |
| AddTorrentActivity | `decodeState.status`: UNKNOWN → DECODE_TORRENT_FILE / FETCHING_HTTP / FETCHING_MAGNET (progress; `showAddButton = !isTorrentFile`) → *_COMPLETED (file tree, Add) or ERROR (dialog) (`AddTorrentActivity.java:305-348, 539-549`). The tab (Info vs Files); Files shows progress until `info.fileCount > 0` (`RES/layout/fragment_add_torrent_files.xml:25,49,57`) |
| CreateTorrentDialog | BUILDING hides Add and changes the title (`CreateTorrentDialog.java:295-309`); FINISHED → toast + optional `downloadTorrent`; ERROR → field error or dialog (`:348-403`) |
| FileManagerDialog | `config.showMode`: FILE_CHOOSER (tap file returns; OK hidden, `FileManagerDialog.java:483-491`), DIR_CHOOSER (OK returns dir; add-folder FAB, `RES/layout/activity_filemanager_dialog.xml:74`), SAVE_FILE (filename bar `:94`; OK creates file; replace dialog `FileManagerDialog.java:570-619`) |
| DetailTorrentFragment | Tab 0-5. `torrent.downloadingMetadata` hides "Save .torrent" (`DetailTorrentFragment.java:444-448`). PAUSED switches pause/resume title/icon (`:428-442`). In action mode (files/trackers) the tab bar recolours (`:278-288`) |
| Detail Files | metaInfo.fileCount == 0 → placeholder (`fragment_detail_torrent_files.xml:31,39`). Selection → action mode; share-stream-URL only when exactly 1 file is selected (`DetailTorrentFilesFragment.java:366-381`); ".." not selectable (`:228-246`) |
| Detail Trackers / Peers / Pieces | Selection → action mode (trackers). Peers rows long-clickable. Pieces placeholder when `numPieces == 0` (`fragment_detail_torrent_pieces.xml:58,65`) |
| FeedActivity/FeedFragment | Empty vs list; selection with size ≤ 1 (edit/refresh/copy visible) vs ≥ 2 (`FeedFragment.java:146-179, 355-368`); refreshing (swipe spinner bound to `observeRefreshStatus`, `:333-338`) |
| AddFeedDialog | ADD vs EDIT (`AddFeedViewModel.Mode`; EDIT adds a neutral Delete button, `AddFeedDialog.java:258-289`); clipboard button visible iff a clip exists (`:115-119`); filter expandable (`:250`) |
| FeedItems | Empty vs list; the popup shows "mark read" iff unread, else "mark unread" (`FeedItemsAdapter.java:148-154`) |
| LogActivity | Logging on/off (`setGroupVisible(log_menu, isLogging)`, `LogActivity.java:204-206`; default ON in debug because `DEFAULT_LOGGING = BuildConfig.SESSION_LOGGING`, `SessionSettings.java:64`, `build.gradle` debug field); paused manually (`:208-216`); recording (`:218-226`; recording cannot start while paused, `:281-287`); list empty vs non-empty; FAB up/down appear after scrolling (`:338-406`) |
| AddTagDialog | Add vs Edit (`existsTagId`, `AddTagDialog.java:172-181`) |
| SelectTagDialog | Empty vs list (`SelectTagDialog.java:138-142`) |
| AddLinkDialog | Clipboard button iff a clip exists (`AddLinkDialog.java:163-167`) |
| Settings sections | Dependent prefs enabled by their parent switch (`android:dependency` in `RES/xml/pref_*.xml`, e.g. `pref_network.xml:133`, `pref_scheduling.xml:15,30`, `pref_storage.xml:53,71`). Proxy fields enabled iff type ≠ none (`ProxySettingsFragment.java:184-205`). Appearance legacy notification prefs only below API 26 (`AppearanceSettingsFragment.java:118-119`; `RES/xml-v26/pref_appearance.xml` omits them) |

### 3.3 Candidate page list (104 pages)

The baseline column says which tool reached the page (MK, AP, or – for neither), judged from the methods that only run on that page.

| # | Page | Description | Window class(es) | Mode predicate | Area | Baseline |
|---|---|---|---|---|---|---|
| 1 | S_ENTRY | Outside the app: launcher, other app, adb | – | – | SHELL | – |
| 2 | S_EXIT | App finished; process and TorrentService may survive (keep-alive) | – | – | SHELL | – |
| 3 | S_NOTIFICATION_SHADE | Status bar with the foreground notification (actions) plus finished/error notifications | SystemUI; TorrentService, TorrentNotifier | service running | ENGINE | MK |
| 4 | S_OUTSIDE_APP | Another app on top: share chooser, browser, file viewer (variants @SHARE @BROWSER @OPEN_FILE) | external | – | SHELL | – |
| 5 | S_SYS_PERMISSION | System runtime-permission dialog (@MAIN @ADDTORRENT @CREATETORRENT) | packageinstaller | storage not granted | SHELL | – (pre-granted) |
| 6 | S_MAIN_EMPTY | Main, no visible torrents: toolbar `main.xml`, FAB, drawer closed | MainActivity, MainFragment | itemCount == 0 | SHELL | MK, AP |
| 7 | S_MAIN_LIST | Main with ≥1 torrent row (tap → details, pause button, long-press) | same | itemCount > 0, no selection | SHELL | – |
| 8 | S_MAIN_SELECT | Action mode `main_action_mode.xml` | MainFragment$3 | `hasSelection()` | SHELL | – |
| 9 | S_MAIN_SEARCH | SearchView expanded (query text and close listeners) | MainActivity$4 | search action expanded | SHELL | MK, AP |
| 10 | S_MAIN_FAB | Speed dial open (Create torrent / Open file / Add link) | MainFragment | FAB expanded | SHELL | MK, AP |
| 11 | S_MAIN_ADD_MENU | Floating context menu `main_context.xml` | MainFragment | started with ADD_TORRENT_SHORTCUT | SHELL | – |
| 12 | S_MAIN_DRAWER | Drawer open: status/sorting/date groups, tags header, Add tag, session stats | MainActivity, DrawerExpandableAdapter | drawer open | SHELL | AP |
| 13 | S_MAIN_DRAWER_TAGS | Drawer with tags expanded and ≥1 user tag row (tap filters, ⋮) | drawer TagsAdapter | expanded && tags ≥ 1 | SHELL | AP |
| 14 | S_POPUP_DRAWER_TAG | PopupMenu `tag_item_popup.xml` (Edit, Delete) | drawer TagsAdapter$ItemViewHolder | – | SHELL | AP |
| 15 | S_DLG_ABOUT | About (OK, Changelog → browser) | BaseAlertDialog `about_dialog` | – | SHELL | AP |
| 16 | S_DLG_DELETE_TORRENTS | Delete selected torrents (+ "with files" checkbox) | BaseAlertDialog in MainFragment child FM | from S_MAIN_SELECT | SHELL | – |
| 17 | S_DLG_OPEN_FILE_ERROR | "Error opening torrent file" (OK) | BaseAlertDialog | picker returned OK with null data | SHELL | – |
| 18 | S_DLG_PERM_DENIED | Permission denied (Yes/No) (@MAIN @ADDTORRENT @CREATETORRENT) | PermissionDeniedDialog | denied && rationale | SHELL | – |
| 19 | S_DLG_ERROR_REPORT | Error with details expander (Report/Cancel); owner variants @ADDTORRENT @CREATETORRENT @FILEMANAGER @FEED_BACKUP @FEED_RESTORE @DETAIL_SAVE | ErrorReportDialog | – | SHELL | MK, AP |
| 20 | S_ERRORREPORT_ACRA | Crash report (Report/Cancel) in `:acra` | ErrorReportActivity + ErrorReportDialog | after a crash | SHELL | unmeasurable |
| 21 | S_MAIN_PAUSED | MainActivity paused/stopped under another activity or in the background | MainActivity | – | SHELL | MK, AP (Feed, Log and Settings were opened over it) |
| 22 | S_ADDLINK | Add link dialog (field, clipboard button, Add/Cancel) | AddLinkActivity, AddLinkDialog | – | ADD | MK, AP |
| 23 | S_DLG_CLIPBOARD | Clipboard item list (@ADDLINK @ADDFEED) | ClipboardDialog | clip present | ADD | MK, AP |
| 24 | S_ADDTORRENT_PENDING | Add torrent while decoding/fetching or after an error: Info tab widgets live, Add hidden (file) or inert (http) | AddTorrentActivity + Info/Files fragments | `info == null` | ADD | MK, AP |
| 25 | S_ADDTORRENT_MAGNET | FETCHING_MAGNET: name/hash known, Add works, Files tab shows progress | same | status FETCHING_MAGNET | ADD | – |
| 26 | S_ADDTORRENT_READY_INFO | Decoded, Info tab (name, path, 4 checkboxes, tags, Add) | AddTorrentInfoFragment | *_COMPLETED && tab 0 | ADD | – |
| 27 | S_ADDTORRENT_READY_FILES | Decoded, Files tab (tree navigation, checkboxes) | AddTorrentFilesFragment | *_COMPLETED && tab 1 | ADD | – |
| 28 | S_DLG_ADDTORRENT_ERROR | Decode/fetch/invalid/OOM/add error (OK does nothing, see §8) | BaseAlertDialog (5 tags) | ERROR | ADD | MK, AP |
| 29 | S_ADDTORRENT_PAUSED | AddTorrent under FileManager/SelectTag | AddTorrentActivity | – | ADD | MK, AP |
| 30 | S_CREATETORRENT | Create-torrent form idle | CreateTorrentActivity, CreateTorrentDialog | status ≠ BUILDING | ADD | MK, AP |
| 31 | S_CREATETORRENT_BUILDING | Building (Add hidden, Cancel only) | same | BUILDING | ADD | – |
| 32 | S_DLG_CREATETORRENT_ERROR | Folder empty / not found / cannot open / cannot create (OK) | BaseAlertDialog (4 tags) | build or picker error | ADD | – |
| 33 | S_SPINNER_DROPDOWN | Spinner popup (@PIECE_SIZE @VERSION @FM_STORAGE) | AdapterView popup | – | ADD | UNVERIFIED (`onItemSelected` hit in MK, AP, but it also fires on initial layout, FW-MEMORY) |
| 34 | S_CREATETORRENT_PAUSED | CreateTorrent under FileManagerDialog | CreateTorrentActivity | – | ADD | MK, AP |
| 35 | S_DETAIL_INFO | Detail, Info tab (edit name, folder, 2 checkboxes, tags) + toolbar | DetailTorrentActivity/Fragment, DetailTorrentInfoFragment | tab 0 | DETAIL | – |
| 36 | S_DETAIL_STATE | State tab (read-only) | DetailTorrentStateFragment | tab 1 | DETAIL | – |
| 37 | S_DETAIL_FILES_EMPTY | Files tab without metadata (placeholder) | DetailTorrentFilesFragment | fileCount == 0 | DETAIL | – |
| 38 | S_DETAIL_FILES | Files tab tree (navigate, open file, priority checkbox, long-press) | same | fileCount > 0, no selection | DETAIL | – |
| 39 | S_DETAIL_FILES_SELECT | Files action mode (priority, stream URL if exactly 1 file) | DetailTorrentFilesFragment$4 | `hasSelection()` | DETAIL | – |
| 40 | S_DETAIL_TRACKERS | Trackers tab | DetailTorrentTrackersFragment | tab 3 | DETAIL | – |
| 41 | S_DETAIL_TRACKERS_SELECT | Trackers action mode (share, delete, select all) | DetailTorrentTrackersFragment$3 | `hasSelection()` | DETAIL | – |
| 42 | S_DETAIL_PEERS | Peers tab (long-press → share IP) | DetailTorrentPeersFragment | tab 4 | DETAIL | – |
| 43 | S_DETAIL_PIECES | Pieces tab (PiecesView, read-only) | DetailTorrentPiecesFragment | tab 5 | DETAIL | – |
| 44 | S_DLG_DELETE_TORRENT | Delete this torrent (+ with files) | BaseAlertDialog `delete_torrent_dialog` | – | DETAIL | – |
| 45 | S_DLG_SHARE_MAGNET | Include priorities? (Yes/No → share chooser) | BaseAlertDialog `include_prior_dialog` | – | DETAIL | – |
| 46 | S_DLG_ADD_TRACKERS | Multi-line URLs (Add/Replace/Cancel, validation) | BaseAlertDialog `add_trackers_dialog` | – | DETAIL | – |
| 47 | S_DLG_SPEED_LIMIT | Upload/download limits (OK/Cancel) | BaseAlertDialog `speed_limit_dialog` | – | DETAIL | – |
| 48 | S_DLG_EDIT_NAME | Rename torrent (OK/Cancel) | BaseAlertDialog `edit_name_dialog` | – | DETAIL | – |
| 49 | S_DLG_CHANGE_PRIORITY | Low/Normal/High radio (OK/Cancel) | BaseAlertDialog `priority_dialog` | from S_DETAIL_FILES_SELECT | DETAIL | – |
| 50 | S_DLG_DELETE_TRACKERS | Delete selected trackers | BaseAlertDialog `delete_trackers_dialog` | from S_DETAIL_TRACKERS_SELECT | DETAIL | – |
| 51 | S_DLG_OPEN_DIR_ERROR | "Unable to open folder" (@DETAIL @ADDTORRENT) | BaseAlertDialog | DIR picker returned null | DETAIL | – |
| 52 | S_DETAIL_PAUSED | Detail under FileManager/SelectTag | DetailTorrentActivity | – | DETAIL | – |
| 53 | S_FEED_EMPTY | Feed list empty (FAB, toolbar `feed.xml`, swipe) | FeedActivity, FeedFragment | itemCount == 0 | FEEDS | MK, AP |
| 54 | S_FEED_LIST | ≥1 channel (tap → items, long-press) | same | itemCount > 0 | FEEDS | AP |
| 55 | S_FEED_SELECT_ONE | Feed action mode, 1 selected (refresh/edit/copy visible) | FeedFragment$3 | size == 1 | FEEDS | – |
| 56 | S_FEED_SELECT_MULTI | Feed action mode, ≥ 2 selected | FeedFragment$3 | size ≥ 2 | FEEDS | – |
| 57 | S_DLG_DELETE_FEEDS | Delete selected channels | BaseAlertDialog | – | FEEDS | – |
| 58 | S_DLG_FEED_RESTORE_ERROR | Invalid backup format (OK) | BaseAlertDialog | JsonSyntaxException on a backup failure (§8 swap) | FEEDS | – |
| 59 | S_FEED_PAUSED | FeedActivity under AddFeed/FeedItems/FileManager | FeedActivity | – | FEEDS | MK, AP |
| 60 | S_ADDFEED_ADD | Add channel dialog (URL, name, filter+regex, auto-download, no-download-now, clipboard) | AddFeedActivity, AddFeedDialog | mode ADD | FEEDS | MK, AP |
| 61 | S_ADDFEED_EDIT | Edit channel (Edit/Delete/Cancel) | same | mode EDIT | FEEDS | – |
| 62 | S_DLG_DELETE_FEED | Confirm delete from edit mode | BaseAlertDialog | – | FEEDS | – |
| 63 | S_FEEDITEMS_EMPTY | Feed items empty (toolbar `feed_items.xml`, swipe) | FeedItemsActivity, FeedItemsFragment | itemCount == 0 | FEEDS | AP |
| 64 | S_FEEDITEMS_LIST | ≥1 item (tap → add torrent, ⋮) | same | itemCount > 0 | FEEDS | – |
| 65 | S_POPUP_FEED_ITEM | Open article / Mark read / Mark unread | FeedItemsAdapter popup | read flag | FEEDS | – |
| 66 | S_FEEDITEMS_PAUSED | Under AddTorrent, or in the background | FeedItemsActivity | – | FEEDS | UNVERIFIED (never under AddTorrent, because no item was ever tapped) |
| 67 | S_LOG_DISABLED | Log with logging off (menu group hidden; switch bar) | LogActivity | `!isLogging` | SETTINGS_LOG | MK, AP |
| 68 | S_LOG_RUNNING | Logging on, live (pause, record, save, filter, settings, row tap copies) | LogActivity | logging && !paused && !recording | SETTINGS_LOG | MK, AP |
| 69 | S_LOG_PAUSED_MANUAL | Paused manually (Resume; record blocked) | LogActivity | `logPausedManually` | SETTINGS_LOG | AP |
| 70 | S_LOG_RECORDING | Recording (Stop → save dialog) | LogActivity | `logRecording` | SETTINGS_LOG | AP |
| 71 | S_DLG_LOG_FILTER | 5 filter checkboxes (two-way bound), Cancel | SessionLogFilterDialog | – | SETTINGS_LOG | MK, AP |
| 72 | S_LOG_PAUSED | LogActivity under LogSettings/FileManager | LogActivity | – | SETTINGS_LOG | MK, AP |
| 73 | S_LOGSETTINGS | Max log size pref | LogSettingsActivity, LogSettingsFragment | – | SETTINGS_LOG | AP |
| 74 | S_SETTINGS | Settings headers | SettingsActivity, SettingsFragment | phone | SETTINGS_LOG | MK, AP |
| 75 | S_PREF_APPEARANCE | Theme, finish notify, foreground filter/sort, combined pause | PreferenceActivity + AppearanceSettingsFragment | – | SETTINGS_LOG | MK, AP |
| 76 | S_PREF_BEHAVIOR | Autostart, keep alive, power, network-type, default trackers | + BehaviorSettingsFragment | – | SETTINGS_LOG | AP |
| 77 | S_DLG_CUSTOM_BATTERY | Custom battery warning (Yes/No) | BaseAlertDialog | toggling custom battery | SETTINGS_LOG | – |
| 78 | S_PREF_NETWORK | Ports, DHT/LSD/uTP/UPnP/NAT-PMP, encryption, IP filter, proxy and anonymous entries | + NetworkSettingsFragment | – | SETTINGS_LOG | AP |
| 79 | S_PREF_PROXY | Proxy prefs + Save FAB | + ProxySettingsFragment | – | SETTINGS_LOG | AP |
| 80 | S_PREF_ANONYMOUS | Anonymous mode switch bar | + AnonymousModeSettingsFragment | – | SETTINGS_LOG | AP |
| 81 | S_PREF_STORAGE | Save/move/torrent-files/watch dirs, posix IO | + StorageSettingsFragment | – | SETTINGS_LOG | MK, AP |
| 82 | S_PREF_LIMITATIONS | Speed/connection/active limits, auto manage | + LimitationsSettingsFragment | – | SETTINGS_LOG | AP |
| 83 | S_PREF_SCHEDULING | Start/stop schedules, run once, Wi-Fi | + SchedulingSettingsFragment | – | SETTINGS_LOG | AP |
| 84 | S_DLG_TIME_PICKER | TimePicker dialog | TimePreferenceDialogFragmentCompat | – | SETTINGS_LOG | AP |
| 85 | S_PREF_FEED | Auto refresh, interval, keep time, start torrents, duplicates | + FeedSettingsFragment | – | SETTINGS_LOG | MK, AP |
| 86 | S_PREF_STREAMING | Enable, host, port | + StreamingSettingsFragment | – | SETTINGS_LOG | AP |
| 87 | S_DLG_PREF_LIST | ListPreference dialog (@key) | androidx ListPreferenceDialogFragmentCompat | – | SETTINGS_LOG | MK, AP |
| 88 | S_DLG_PREF_EDITTEXT | EditTextPreference dialog (@key) | androidx EditTextPreferenceDialogFragmentCompat | – | SETTINGS_LOG | AP |
| 89 | S_SETTINGS_PAUSED | SettingsActivity under PreferenceActivity | SettingsActivity | – | SETTINGS_LOG | MK, AP |
| 90 | S_PREFERENCE_PAUSED | PreferenceActivity under FileManager / Proxy / Anonymous | PreferenceActivity | – | SETTINGS_LOG | MK, AP |
| 91 | S_FM_FILE | File chooser (@OPEN_TORRENT @CREATE_FILE @FEED_RESTORE @IPFILTER) | FileManagerDialog | FILE_CHOOSER_MODE | FILES_TAGS | MK, AP |
| 92 | S_FM_DIR | Folder chooser (@ADDTORRENT_DIR @CREATE_DIR @DETAIL_DIR @STORAGE_DIR) | FileManagerDialog | DIR_CHOOSER_MODE | FILES_TAGS | MK, AP |
| 93 | S_FM_SAVE | Save-as (@CREATE_SAVE @FEED_BACKUP @DETAIL_SAVE @LOG_SAVE) | FileManagerDialog | SAVE_FILE_MODE | FILES_TAGS | AP (MK UNVERIFIED) |
| 94 | S_DLG_FM_NEW_FOLDER | New folder name (OK/Cancel) | BaseAlertDialog `input_name_dialog` | DIR/SAVE | FILES_TAGS | MK, AP |
| 95 | S_DLG_FM_GOTO | Go to folder path (OK/Cancel) | GoToFolderDialog | – | FILES_TAGS | MK, AP |
| 96 | S_DLG_FM_REPLACE | Replace existing file? (Yes/No) | BaseAlertDialog | SAVE && file exists | FILES_TAGS | – |
| 97 | S_DLG_FM_ERROR | Cannot create folder / cannot open dir (OK) | BaseAlertDialog | – | FILES_TAGS | AP |
| 98 | S_ADDTAG_NEW | Add tag (name, color, Add/Cancel) | AddTagActivity, AddTagDialog | existsTagId == null | FILES_TAGS | AP |
| 99 | S_ADDTAG_EDIT | Edit tag (Apply) | same | existsTagId != null | FILES_TAGS | – |
| 100 | S_DLG_COLOR_PICKER | ColorPickerDialog (library) | com.jaredrummler ColorPickerDialog → `AddTagActivity.onColorSelected` | – | FILES_TAGS | AP |
| 101 | S_SELECTTAG_EMPTY | Select tag, no selectable tags (New tag/Cancel) | SelectTagActivity, SelectTagDialog | list empty | FILES_TAGS | AP |
| 102 | S_SELECTTAG_LIST | Select tag list (tap returns RESULT_OK) | same | list non-empty | FILES_TAGS | AP |
| 103 | S_SELECTTAG_PAUSED | SelectTag under AddTag | SelectTagActivity | – | FILES_TAGS | AP |
| 104 | S_ADDTORRENT_ERROR_REPORT | IO-error report over AddTorrent. Kept apart from #19 because both buttons also finish AddTorrentActivity (`AddTorrentActivity.java:241-263`); Report → `Utils.reportError` | ErrorReportDialog `io_err_report_dialog` | IOException in decode or add | ADD | MK, AP |

Deliberately **not** pages (record them as UNREACHABLE notes):
- two-pane Main/Feed/Settings (tablet only);
- ManageAllFilesWarningDialog (play flavor and API ≥ 30);
- exact-alarm permission dialog and notification (API ≥ 31);
- legacy ringtone/LED/vibration prefs (API < 26).

**Variants (`X@CONTEXT`) the graph will need:**

- **FileManagerDialog (13 callers).** Each RESULT goes to a different launcher lambda:
  - `MainFragment.lambda$new$18`;
  - `AddTorrentInfoFragment.lambda$new$2`;
  - three CreateTorrentDialog launchers (`chooseFile`, `chooseDir`, `choosePathToSave`);
  - `FeedActivity` backup and restore;
  - `DetailTorrentInfoFragment` (chooseDir) and `DetailTorrentFragment.saveTorrentFileChoose`;
  - `StorageSettingsFragment.downloadDirChoose` (4 prefs share it via `dirChooserBindPref`, `StorageSettingsFragment.java:250-270`);
  - `NetworkSettingsFragment.fileChoose`;
  - `LogActivity.saveLogPathChoose`.
- **BaseAlertDialog event bus.** `SharedViewModel` is activity-scoped (`BaseAlertDialog.java:118`), and every subscriber in that activity receives every event and filters by `dialogTag`. In DetailTorrentActivity alone that is DetailTorrentFragment, DetailTorrentInfoFragment, DetailTorrentFilesFragment and DetailTorrentTrackersFragment. Model this as variants of the button lambdas keyed by tag (`BaseAlertDialog.lambda$buildDialog$N@<TAG>`).
- PermissionDeniedDialog, ErrorReportDialog and ClipboardDialog per owner.
- SelectTagActivity@ADDTORRENT/@DETAIL; AddTagActivity@NEW (drawer, SelectTag) / @EDIT.
- AddTorrentActivity by source (FILE/MAGNET/HTTP) and caller (Main picker, AddLink, FeedItems, external VIEW/SEND).
- PreferenceActivity@<section> (10 sections).
- `MainActivity.onCreate@SHUTDOWN` and `DetailTorrentActivity.onCreate@OPEN_FILES`.

---

## 4. Framework mechanisms (edges the graph will need)

| Mechanism | App classes (cite) | Modeling note |
|---|---|---|
| RecyclerView ListAdapters + DiffUtil | TorrentListAdapter, FeedChannelListAdapter, FeedItemsAdapter, FileManagerAdapter, DownloadableFilesAdapter, TorrentContentFilesAdapter, TrackerListAdapter, PeerListAdapter, tag/TagsAdapter, drawer TagsAdapter; `LogAdapter` is a PagedListAdapter | `submitList` diffs off-thread, then `onCreateViewHolder`/`onBindViewHolder` and the `$1` DiffUtil callbacks (FRAMEWORK). Click listeners are registered in `ViewHolder.bind` (REGISTER), and the GUI edge targets the bind lambda |
| Expandable adapter (advrecyclerview) | DrawerExpandableAdapter, `RecyclerViewExpandableItemManager` listeners | `MainActivity.java:230-260` |
| recyclerview-selection | 4 trackers: `MainFragment.java:157-198`, `FeedFragment.java:137-183`, `DetailTorrentFilesFragment.java:220-300`, `DetailTorrentTrackersFragment.java:178-226`; KeyProvider/ItemLookup/ItemDetails inner classes | Long-press → `SelectionObserver.onSelectionChanged` → `startSupportActionMode` → ActionMode.Callback (`onCreate`/`onPrepare`/`onActionItemClicked`/`onDestroy`). Back finishes the action mode → `onDestroyActionMode` → `clearSelection` |
| ViewPager2 FragmentStateAdapter | AddTorrentPagerAdapter (offscreen = 2, `AddTorrentActivity.java:290`), DetailPagerAdapter (`createFragment` FRAMEWORK) | Tab tap or swipe → `onPageSelected` (`DetailTorrentFragment$1`) |
| ViewModel / LiveData | One AndroidViewModel per screen. LiveData: `AddTorrentViewModel.decodeState` (`AddTorrentViewModel.java:83`, observed at `AddTorrentActivity.java:305-327`), `CreateTorrentViewModel.state`/`buildProgress`, `SettingsViewModel.detailTitleChanged`, `LogViewModel.observeLog` (LiveData<PagedList>, `LogActivity.java:119-120`), WorkManager `getWorkInfoByIdLiveData().observeForever` (`FeedViewModel.java:153-171`, `FeedItemsViewModel.java:136-154`) | LiveData observers run on the main thread while STARTED (FW-MEMORY) |
| Rx "message" ViewModels (PublishSubject/BehaviorSubject) | MsgMainViewModel, MsgFeedViewModel, MsgDetailTorrentViewModel, BaseAlertDialog.SharedViewModel, ClipboardDialog.SharedViewModel | Subscribed in `onStart`, cleared in `onStop`: events while stopped are lost (`MainActivity.java:380-396`, etc.) |
| RxJava 2 everywhere | TorrentInfoProvider (Flowable.create + `new Thread`, `TorrentInfoProvider.java:207-302`), Room RxJava Flowables, `Schedulers.io` → `AndroidSchedulers.mainThread` | ASYNC edges; subscriber lambdas are separate methods |
| AsyncTask | `AddTorrentViewModel.TorrentDecodeTask` (THREAD_POOL_EXECUTOR, `:197-326`) | `doInBackground` → `onPostExecute` posts decode state |
| Threads/executors/Handler | `TorrentEngine.exec` (`:112`); TorrentSessionImpl `loadTorrentsExec` and IP-filter thread (`:175, 726`); TorrentCriticalWork pool; Logger sender; `AddTorrentViewModel.addTorrent` Thread+join (`:525-540`); AddFeedViewModel Thread+join (`:129-140, 185-199`); main-looper posts in `Utils.startServiceBackground` (`:426-434`), `SaveLogWorker` toasts, `MainFragment.showAddTorrentMenu` (`v.post`), `AddLinkDialog.handleUrlClipItem` (postDelayed 500 ms) | ASYNC |
| WorkManager | FeedFetcherWorker (OneTime from AddFeed/Feed/FeedItems refresh; Periodic from `Scheduler.runPeriodicalRefreshFeeds`), FeedDownloaderWorker (from `FeedFetcherWorker.sendFetchedItems`, `:212-237`), SaveLogWorker (from `LogViewModel.saveLog`) | `doWork` on a WorkManager thread (FW) |
| AlarmManager | `Scheduler.setStartStopAppAlarm` → SchedulerReceiver | Time-gated SYSTEM edge |
| Foreground service | TorrentService (started, never bound), libtorrent session lifecycle, foreground notification actions | `onStartCommand` dispatch (`:175-233`) |
| Broadcast receivers | Manifest: NotificationReceiver, BootReceiver, SchedulerReceiver. Dynamic: PowerReceiver, ConnectionReceiver, FileManagerDialog.MediaReceiver. Clipboard listener (AddLink/AddFeed). SharedPreferences listener (`SettingsRepositoryImpl.observeSettingsChanged`, `:195-209`) → TorrentEngine/TorrentService `handleSettingsChanged` | Settings changes in any preference screen fan out to the engine (FRAMEWORK) |
| libtorrent4j native session | TorrentSessionImpl extends SessionManager; `InnerListener` AlertListeners in TorrentSessionImpl/TorrentDownloadImpl → TorrentEngineListener callbacks (`TorrentEngine$5`, TorrentInfoProvider) | Alerts arrive on the libtorrent alert thread (FW-MEMORY) |
| FileObserver | `TorrentEngine$4` extends TorrentFileObserver (`TorrentEngine.java:1136-1164`) | `.torrent` created in the watch dir → `addTorrentCompletable` |
| HTTP server | TorrentStreamServer extends NanoHTTPD (started on session start, `TorrentEngine.java:1063-1077`) | `serve()` only from an external HTTP client |
| Data binding | 38 binding layouts; DataBinderMapperImpl. Two-way bindings (InverseBindingListener `XBindingImpl$N.onChange`) in add_torrent_info, dialog_add_feed_channel, dialog_add_link, dialog_add_tag, dialog_create_torrent, dialog_go_to_folder, dialog_log_filter, activity_log, fragment_detail_torrent_info. BaseObservable params with OnPropertyChangedCallbacks (`AddTorrentActivity$2`, `AddTorrentViewModel$1/$2`, `DetailTorrentViewModel$1/$2`, `LogActivity$1`, `LogViewModel$1`, `CreateTorrentViewModel$1`, `FileManagerDialog$3`); BindingAdapterUtils adapters | User edit → `$N.onChange` → setter → `notifyPropertyChanged` → callbacks and `executeBindings` on the next frame (FRAMEWORK) |
| Database | Room `AppDatabase` v9 (entities Torrent, FastResume, FeedChannel, FeedItem, TagInfo, TorrentTagInfo; `AppDatabase.java:41-86`), generated `*_Impl`, DatabaseMigration (7 migrations + legacy), repositories via `RepositoryHelper` singletons | Migrations run only on upgrade (FRAMEWORK_ONLY on a fresh install) |
| SAF / file pickers | The app's own `FileManagerDialog` (java.io.File based) for every pick. `SafFileSystem`/`SafFsModule` treat any `content://` URI as SAF (`SafFileSystem.java:191-198`); reached only through external content URIs (VIEW intents); no system SAF picker is launched (grep) | – |
| Notifications | TorrentService foreground notification (PendingIntents → NotificationReceiver); TorrentNotifier error/info/NAT/moving/finished (finished → DetailTorrentActivity) | – |
| ACRA | `MainApplication.java:49-66`; ErrorReportActivity in `:acra` | Unmeasured by the coverage harness |
| Library dialogs | ColorPickerDialog (→ `ColorPickerDialogListener`), androidx Preference dialogs, SpeedDialView, SearchView, Snackbar action (`AppearanceSettingsFragment.java:231-236`) | – |

---

## 5. Unreachable-code candidates (evidence only; verdicts are for the graph builders)

### 5.1 No caller anywhere in the APK bytecode (DEAD candidates)
Method: scan every Methodref/InterfaceMethodref (including those behind invokedynamic MethodHandles) in `CLS/`. A never-hit method counts as uncalled if no reference with the same name and descriptor exists, and it is private/static or its class hierarchy is app-only.

- **Generated data binding, 238 methods:**
  - all static `inflate(...)` ×4 and `bind(...)` ×2 of 37 base binding classes (222). The app always uses `DataBindingUtil.inflate`/`setContentView`;
  - `getViewModel()` ×15 and `DialogErrorBinding.getDetailError` (getters nobody calls).
- **Hand-written, 86 methods:**
  - **CORE (17):**
    - `Utils.normalizeURL`;
    - `NormalizeUrl.normalize(String)` (1-arg);
    - `BaseSorting$Direction.fromValue`;
    - `DefaultFsModule.getName`, `SafFsModule.getName`;
    - `FileSystemFacadeImpl.isValidFatFilename` (used only by androidTest `FileSystemFacadeTest.java:130-135`);
    - `TorrentRepositoryImpl.getTorrentDataDir`;
    - `SafFileSystem` FakePath API: `delete`/`exists`/`mkdirs`/`stat`/`openFD` overloads, `FakePath.deserialize`/`isFakePath`/`relativePath`.
  - **ENGINE (24 + 2 constructors):**
    - `TorrentEngine.addTorrent(AddTorrentParams,boolean)` (`:331`);
    - `TorrentInfoProvider.getInstance(TorrentEngine,TagRepository)` (test hook; used in `androidTest/.../AbstractTest.java:72`);
    - `TorrentSessionImpl.mergeTrackersAndSeeds`;
    - `TorrentDownloadImpl.getMaxConnections`/`getMaxUploads`/`isAutoManaged`/`isDownloading`;
    - `TorrentCriticalWork.isMoving`/`isSaveResume`;
    - `PriorityConverter.convert(Priority)`;
    - unused NanoHTTPD API (`closeAllConnections`, `decodeParameters`, `getHostname`, `getListeningPort`, `getMimeTypeForFile`, `getTempFileManagerFactory`, `makeSSLSocketFactory`, `makeSecure`, `newChunkedResponse`, `newFixedLengthResponse(String)`, `setServerSocketFactory`, `DefaultAsyncRunner.getRunning`, `DefaultTempFile.open`, `HTTPSession.getCookies`);
    - constructors `FileTree.<init>(int,String,long,int)` and the 5-arg `NanoHTTPD$HTTPSession.<init>`.
  - **FEEDS (35):**
    - unused feedparser getters: Atom/Rss1/Rss2 Feed `getCategories`/`getCopyright`/`getLanguage`/`getLink`/`getType`; Item `getAuthor`/`getCategories`/`getType`; `BaseElement.getElementKeys`; `Enclosure.getLength`; `EzRssTorrentItem` ×5; `MediaRss.getPeerLinks`; `PeerLink.getHref`;
    - `FeedRepositoryImpl.getSerializeFileFormat`/`getSerializeMimeType`.
  - **SETTINGS_LOG (6):** `SettingsFragment.newInstance` and `LogSettingsFragment.newInstance` (both fragments come from XML `class=`), `Logger.getEntry`, `Logger.stopRecording(OutputStream)`, `Logger.write(OutputStream)`, `LogEntry.getTimeStamp`.
  - **FILES_TAGS (2):** `FileManagerSpinnerAdapter$StorageSpinnerItem.setSize`/`setStoragePath`.
- **Branch-level dead code (methods themselves live):**
  - `NotificationReceiver` NOTIFY_ACTION_ADD_TORRENT (`:60-65`, no sender);
  - `MainApplication.lambda$onCreate$0`: the stub handler is only installed when no default uncaught handler exists (`:61-65`), and Android's runtime always installs one (FW-MEMORY).
- **Also no caller in the APK, but the class has a JDK supertype**, so the heuristic could not rule out a framework override: `FixedRingBuffer.isFull`/`getAllocatedSize` (used only by `src/test/.../FixedRingBufferTest`, which is not in the APK).

### 5.2 Framework-callback candidates likely never called in practice (FRAMEWORK_ONLY candidates)
- `describeContents()` of every Parcelable: FileItem, DownloadableFileItem, TorrentContentFileItem, FileManagerConfig, PreferenceActivityConfig, TagInfo, FeedChannel, FeedItem, Torrent, AddTorrentParams, AdvancedTorrentInfo, BencodeFileItem, MagnetInfo, PeerInfo, SessionStats, TorrentInfo, TorrentMetaInfo, TorrentStream, TrackerInfo. `FileManagerConfig.describeContents` never ran even though the object is an intent extra on every picker launch.
- `TorrentService.onBind` (the service is never bound).
- `onNothingSelected` of the static spinners (`CreateTorrentDialog$3/$4`, `FileManagerDialog$2`; FW-MEMORY: only fires when the selection becomes invalid).
- The host activities' `onBackPressed` when their DialogFragment consumes BACK: AddTagActivity, AddFeedActivity, CreateTorrentActivity (0 hits each), AddLinkActivity and SelectTagActivity (same pattern).
- Room: `AppDatabase_Impl$1.onValidateSchema`/`onPreMigrate`/`onPostMigrate`/`dropAllTables`, `clearAllTables`, `DatabaseMigration$1..$7.migrate`, `RoomDatabaseMigration.migrate` (upgrade only).
- `EmptyRecyclerView$1.onChanged` (ListAdapter dispatches range events, not `onChanged`; FW-MEMORY).
- Selection predicates `canSetStateAtPosition`/`canSelectMultiple`.
- `TimePreference.onGetDefaultValue` (no `android:defaultValue` in `pref_scheduling.xml`) and `onSetInitialValue(boolean,Object)` (called only when the key is persisted; FW-MEMORY).
- The Detail fragment's `android.R.id.home` branch (`DetailTorrentFragment.java:455-456`): on phones the later `setNavigationOnClickListener` (`:183`) replaces the action-bar Up listener. FW-MEMORY; consistent with FeedItemsFragment, where AP hit the navigation lambda.

### 5.3 Gated by API level, flavor, configuration or build (compiled in)

| Gate | Code | Evidence |
|---|---|---|
| API < 26 only | `AppearanceSettingsFragment.initLegacyNotifySettings`, its ringtone lambda and `ringtonePicker` result; `TorrentNotifier.applyLegacyNotifySettings` body | `AppearanceSettingsFragment.java:118-217`, `TorrentNotifier.java:275-293`; `RES/xml-v26/pref_appearance.xml` has no legacy keys |
| API ≥ 30 | `PermissionManager.lambda$new$0` (all-files-access result), MANAGE_EXTERNAL_STORAGE branches | `PermissionManager.java:60-68, 99-106, 129-131` |
| API ≥ 30 **and play flavor** | `ManageAllFilesWarningDialog` (3) and the `showManageAllFilesWarningDialog` body: the base manifest requests MANAGE_EXTERNAL_STORAGE, so `hasManageExternalStoragePermission` is true and the method returns early | `Utils.java:699-718`, `MF:18`, `src/play/AndroidManifest.xml:6-8` |
| API ≥ 31 | `SchedulingSettingsFragment.showExactAlarmPermissionDialog` + `lambda$subscribeAlertDialog$0`; `Utils.buildExactAlarmPermissionRequest`/`requestExactAlarmPermission`; `TorrentNotifier.makeExactAlarmPermissionNotify` body (reached only when `Scheduler.set*` returns false, which needs API ≥ 31) | `Scheduler.java:101-103`, `Utils.java:665-675`, `TorrentNotifier.java:244-267` |
| API ≥ 33 | POST_NOTIFICATIONS branches | `PermissionManager.java:75-79, 110-112, 123-126, 138-141` |
| Tablet / TV config (`isTwoPane`, `isLargeScreenDevice`) | `BlankFragment` (3); `*BindingSw600dpLandImpl`/`*LargeLandNotouchImpl` (4 classes, 38 methods); `SettingsFragment.setFragment`, `NetworkSettingsFragment.setFragment`; two-pane branches in MainActivity/FeedActivity/MainFragment/FeedFragment/FeedItemsFragment/DetailTorrentFragment | `RES/values*/bool.xml`, `layouts.xml`; `SettingsFragment.java:220-230` |
| Debug build | `SESSION_LOGGING=true`, so logging is ON by default (Log screen starts in "enabled" mode) | `build.gradle` debug `buildConfigField`; `SessionSettings.java:64` |
| Test helpers in main | `TorrentInfoProvider.getInstance(engine, tagRepo)`, `FileSystemFacadeImpl.isValidFatFilename`, FixedRingBuffer size helpers | androidTest/test call sites above |
| Excluded harness | `JacocoInstrument/*` (3 classes, 10 methods) | `MF:288-293` |

### 5.4 Environment-gated (reachable, but only with external state)
- **Network:** feed fetch (G6), http torrent links, magnet metadata (`TorrentEngine$2.onMagnetLoaded`, `$3.onTorrentMetadataLoaded`), trackers/peers lists, NAT errors.
- **Peers/time:** download completion (`onTorrentFinished`, finished notification, "move after download" `onTorrentMoving`/`onTorrentMoved`, auto shutdown `handleAutoStop`).
- **Boot / alarm / power:** BootReceiver, SchedulerReceiver, PowerReceiver.
- **SD card mount:** `FileManagerDialog.MediaReceiver`.
- **External HTTP client:** `TorrentStreamServer.serve`, `TorrentInputStream`, `TorrentStream`.
- **Crash:** ErrorReportActivity (also unmeasurable).
- **Share sheet:** SendTextToClipboard.

### 5.5 What the baseline cannot see at all
- `ErrorReportActivity` (`:acra` process).
- About 81 methods that `tools/list_methods.py` lists but JaCoCo filters: enum `values`/`valueOf` (40), enum and private no-arg constructors (19), and the `<clinit>` of 23 enum switch-map classes (`MainFragment$4`, `TorrentService$2`, …; verified with `strings` showing `$SwitchMap$`).
- Coverage lost when the main process dies between two 30-second dumps (INFERRED from 118 coverage segments).

---

## 6. Decomposition (8 areas)

Assignment is a deterministic ordered prefix rule (first match wins); every one of the 688 class files lands in exactly one area. Method counts come from JaCoCo (4728 total). "gen" = generated data binding (assigned to the area whose screen inflates the layout).

| Area | Owns (packages / classes) | Class files | Methods (gen) | Pages owned (§3.3 #) | Entry edges from other areas | Shared infra it owns |
|---|---|---|---|---|---|---|
| **SHELL**: app shell, main list, drawer, shared UI | `MainApplication`; `ui/main/**` incl. drawer; `ui/BaseAlertDialog`, `PermissionManager`, `PermissionDeniedDialog`, `ManageAllFilesWarningDialog`, `FragmentCallback`, `Selectable`, `SendTextToClipboard`, `FileItem`; `ui/customviews/**`; `ui/errorreport/**`; `BR`, `BuildConfig`, `DataBinderMapperImpl`, `DataBindingTriggerClass`, `androidx/databinding/**`; bindings fragment_main, item_torrent_list, drawer_*_list_item ×3, dialog_error | 88 | 468 (105) | 1,2,4-21 | S_ENTRY (launcher, SEARCH, shortcut, notification content/shutdown); FILES_TAGS RESULT → `MainFragment.lambda$new$18`; SETTINGS_LOG `restartMainActivity`; ENGINE NotificationReceiver | BaseAlertDialog + SharedViewModel event bus, ErrorReportDialog, PermissionManager, custom views, binding mapper |
| **ADD**: adding torrents | `ui/addtorrent/**`, `ui/addlink/**`, `ui/createtorrent/**`, `ui/ClipboardDialog`, `core/TorrentBuilder`; bindings activity_add_torrent, add_torrent_info, fragment_add_torrent_info ×3 variants, fragment_add_torrent_files, item_torrent_downloadable_file, dialog_add_link, dialog_create_torrent | 78 | 518 (172) | 22-34, 104 | SHELL FAB/context menu/picker result; FEEDS `FeedItemsFragment.openDownloadUrl`; S_ENTRY VIEW/SEND; FILES_TAGS RESULTs | ClipboardDialog (also used by AddFeed) |
| **DETAIL**: torrent details | `ui/detailtorrent/**` (activity, fragment, VM, pager, BlankFragment, 6 pages, adapters, PiecesView); bindings fragment_detail_torrent*, detail_torrent_appbar ×3, item_torrent_content_file, item_peers_list, item_trackers_list | 83 | 596 (200) | 35-52 | SHELL `MainActivity.showDetailTorrent`; ENGINE finished notification (ACTION_OPEN_FILES); FILES_TAGS RESULTs | – |
| **FEEDS**: RSS/Atom | `ui/feeds/**`, `ui/feeditems/**`, `ui/addfeed/**`; `service/FeedFetcherWorker`, `FeedDownloaderWorker`; `core/FeedParser`; `com/ernieyu/feedparser/**`; `core/storage/FeedRepository*`, `dao/FeedDao*`; entities FeedChannel, FeedItem; bindings fragment_feed, fragment_feed_items, item_feed_channel_list, item_feed_items_list, dialog_add_feed_channel | 103 | 694 (91) | 53-66 | SHELL Main menu "Feed"; S_ENTRY shortcut/VIEW/SEND → AddFeedActivity; SETTINGS_LOG periodic WorkManager; FILES_TAGS RESULTs | Feed DB tables and repository |
| **SETTINGS_LOG**: settings, log, scheduling | `ui/settings/**`, `ui/log/**`; `service/Scheduler`, `SaveLogWorker`; `receiver/SchedulerReceiver`, `BootReceiver`; `core/settings/**`, `core/logger/**`, `core/InputFilterRange`; bindings activity_log, item_log_list, dialog_log_filter | 66 | 645 (63) | 67-90 | SHELL menu Settings/Log; S_ENTRY APPLICATION_PREFERENCES, boot, alarm; ENGINE reads SettingsRepository and listens to its changes | **SettingsRepositoryImpl** (195 methods; getters/setters called from every area) |
| **FILES_TAGS**: file manager and tags | `ui/filemanager/**`, `ui/tag/**`, `ui/addtag/**`; `core/storage/TagRepository*`, `dao/TagInfoDao*`; entities TagInfo, TorrentTagInfo; bindings activity_filemanager_dialog, dialog_go_to_folder, dialog_add_tag, dialog_select_tag, tags_list_item | 62 | 383 (87) | 91-103 | SHELL (open file, drawer tags), ADD, DETAIL, FEEDS, SETTINGS_LOG (pickers, SelectTag); returns RESULT edges to each caller | FileManagerDialog (13 callers), TorrentTagsList/AddTagButton (used by ADD and DETAIL) |
| **ENGINE**: torrent engine, service, notifications | `core/model/**` (TorrentEngine, TorrentInfoProvider, listeners, data, filetree, session, stream; entities Torrent, FastResume); `service/TorrentService`; `receiver/NotificationReceiver`, `PowerReceiver`, `ConnectionReceiver`; `ui/TorrentNotifier`; `org/nanohttpd/**` | 119 | 985 (0) | 3 | Every UI area (`TorrentEngine.getInstance(...)` calls, `TorrentInfoProvider.observe*`); S_ENTRY notification actions, broadcasts, file observer, HTTP clients | Engine/session singletons, notification channels |
| **CORE**: utilities and storage | remaining `core/**`: `utils/**` (Utils, BindingAdapterUtils, DateUtils, *FileTreeUtils), `system/**` (FileSystemFacade*, SAF, SystemFacade*), `storage/` AppDatabase(+_Impl), DatabaseMigration, TorrentRepositoryImpl, dao TorrentDao*/FastResumeDao*, converter; `sorting/**`, `filter/**`, `collections/**`, `exception/**`, `urlnormalizer/**`, `RepositoryHelper`, `HttpConnection`, `TorrentFileObserver` | 86 | 439 (0) | – | Everyone (CALL edges only) | RepositoryHelper singletons, Room DB, file system facade, Utils |
| Excluded | `JacocoInstrument/**` | 3 | 10 | – | – | – |

Leftovers:
- 23 enum switch-map classes (`*$N` containing `$SwitchMap$…`) have no JaCoCo methods; they go to their outer class's area (list_methods emits one `<clinit>` each).
- 53 further class files without code (interfaces, listener interfaces, `TorrentRepositoryImpl$FileDataModel`) also follow their package's area (e.g. `TorrentSession`, `FsModule`, `SettingsRepository`, the DAO interfaces, `com.ernieyu.feedparser.Feed`/`Item`/`Element`/`FeedParser`).
- No class is unassigned (checked by script).

**Naming caution for all areas.** `tools/list_methods.py` and `coverage_methods.py` key methods by simple class name (`tools/list_methods.py:76-77, 113`, `tools/coverage_methods.py:33`). Seven simple names collide and must be qualified in the graph (e.g. `drawer.TagsAdapter.onBindViewHolder` vs `tag.TagsAdapter.onBindViewHolder`):
- `BR` ×2 and `DataBinderMapperImpl` ×2 (app and androidx);
- `FeedParser` (core vs feedparser interface);
- `TagItem`, `TagsAdapter`, `TagsAdapter$1`, `TagsAdapter$OnClickListener` (ui/main/drawer vs ui/tag).

list_methods prints 4809 rows versus 4728 JaCoCo methods (§5.5).

---

## 7. Baseline coverage by area and screen

Per area, JaCoCo methods split by which tool hit them:

| Area | Methods | Monkey only | APE only | Both | Neither | Neither, of which no bytecode caller (§5.1) |
|---|---|---|---|---|---|---|
| SHELL | 468 | 0 | 46 | 234 | 188 | 37 gen |
| ADD | 518 | 1 | 29 | 286 | 202 | 47 gen |
| DETAIL | 596 | 0 | 0 | 0 | 596 | 70 gen |
| FEEDS | 694 | 0 | 115 | 177 | 402 | 31 gen + 35 |
| SETTINGS_LOG | 645 | 8 | 165 | 324 | 148 | 20 gen + 6 |
| FILES_TAGS | 383 | 0 | 116 | 143 | 124 | 33 gen + 2 |
| ENGINE | 985 | 7 | 9 | 241 | 728 | 26 |
| CORE | 439 | 1 | 40 | 138 | 260 | 17 |
| **Total** | **4728** | **17** | **520** | **1543** | **2648** | **238 gen + 86** |

Totals match the brief: Monkey 1560, APE 2063, either 2080. Generated binding inside these areas totals 718 methods (705 in `.../databinding` plus 13 mapper/BR): 199 both, 42 APE only, 477 neither.

Per screen (outer-class method totals, Monkey/APE hits):
- **Main:** MainActivity 61 (39/54); MainFragment 63 (30/31); TorrentListAdapter 27 (6/6); TorrentListItem 4 (0/0); drawer TagsAdapter 25 (16/25); DrawerExpandableAdapter 18 (18/18).
- **AddLink:** AddLinkDialog 32 (24/32); ClipboardDialog 11 (7/11).
- **AddTorrent:** Activity 30 (25/26); Info 24 (15/21); Files 17 (11/12); VM 43 (24/26); DownloadableFileItem 9 (0/0).
- **CreateTorrent:** Dialog 48 (34/36); VM 34 (13/13); TorrentBuilder 22 (0/0).
- **FileManager:** FileManagerDialog 49 (36/44); GoToFolderDialog 19 (16/19).
- **Detail:** every class 0/0 (596 methods).
- **Feed:** FeedActivity 31 (16/23); FeedFragment 49 (23/24); FeedChannelListAdapter 26 (7/15).
- **FeedItems:** Activity 4 (0/4); Fragment 31 (0/21); Adapter 15 (0/4); FeedItemsListItem 5 (0/0).
- **AddFeed:** Dialog 45 (35/38); VM 16 (5/9).
- **Log:** LogActivity 35 (27/31); LogSettings 4+8 (0/4, 0/6); SessionLogFilterDialog 10 (10/9).
- **Settings:**
  - SettingsActivity 5 (3/4); PreferenceActivity 6 (5/6);
  - sections Appearance 12 (7/7), Storage 15 (14/15), Feed 7 (7/7);
  - Behavior 15 (0/11), Network 19 (0/14), Limitations 16 (0/8), Scheduling 12 (0/10), Streaming 8 (0/7), Proxy 14 (0/11), Anonymous 7 (0/7).
- **Tags:** AddTagDialog 24 (0/23); SelectTagDialog 19 (0/18); tag/TagItem 5 (0/0).
- **Other:** ErrorReportActivity 9 (0/0); ErrorReportDialog 6 (5/6); PermissionDeniedDialog / ManageAllFiles / SendTextToClipboard / BlankFragment all 0/0.
- **Services:** TorrentService 37 (33/28); FeedFetcherWorker 13 (5/6); FeedDownloaderWorker 6 and SaveLogWorker 8 (0/0); NotificationReceiver 2 (2/0).

Screens never reached and why: see §2.3. In short:
- **DETAIL (all):** no torrent was ever added (G2/G3).
- **Main list/selection:** G2.
- **AddTorrent ready states:** G3.
- **CreateTorrent build:** the save step was never confirmed.
- **Feed items:** network/feed content (G6).
- **Feed/files/trackers selection modes:** the selection library was never engaged (cause UNVERIFIED).
- **Edit modes:** need selection or the popup's "Edit".
- **Permission and all-files dialogs:** permission granted / API- and flavor-gated.
- **ErrorReport:** separate process.
- **External entries (share, shortcut, boot, alarm, stream client):** outside the tools' package-restricted exploration.
- Monkey missed every APE-only screen listed in §2.3 (drawer actions, tags, most settings sections, About, feed items).

---

## 8. Conclusions and recommendations

**Modeling recommendations:**
1. Model **the empty-list state as the default**. Make S_MAIN_LIST, the whole DETAIL area and S_ADDTORRENT_READY_* reachable through explicit `needs_state` edges ("a torrent exists", "the torrent has metadata", "a feed with items exists", "a user tag exists"). Most of the 2648 never-hit methods sit behind these four states.
2. Put an explicit add-torrent path in the graph:
   - **offline-capable, no metadata:** AddLink → 40-hex hash or magnet with `dn=` → S_ADDTORRENT_MAGNET → Add;
   - **with metadata:** FAB → Open file → S_FM_FILE@OPEN_TORRENT → pick `.torrent` → S_ADDTORRENT_READY_* → Add;
   - **local creation:** CreateTorrent → seed file → Add → S_FM_SAVE@CREATE_SAVE → OK → Start seeding.
   
   The second needs a `.torrent` fixture; the third needs none.
3. Treat BaseAlertDialog buttons as an **activity-wide event bus**. One click can fire 2-4 subscriber lambdas, each filtering by tag (e.g. `DetailTorrentFragment.java:297-354` vs `DetailTorrentInfoFragment.java:205-240` vs `DetailTorrentFilesFragment.java:170-190`). All of them are dropped while the subscriber is stopped (CompositeDisposable cleared in `onStop`).
4. Use the `@CONTEXT` variants of §3.3 for FileManagerDialog (13 RESULT targets), PermissionDeniedDialog, ErrorReportDialog, ClipboardDialog, SelectTag/AddTag and PreferenceActivity sections.
5. Record two-way data-binding edges (user edit → `XBindingImpl$N.onChange` → params setter → OnPropertyChangedCallback). For AddTorrent, Detail Info and Log they are the only path to several ViewModel callbacks (`AddTorrentActivity$2`, `DetailTorrentViewModel$1.checkParamsChanged`, `LogViewModel$1`).
6. Generated binding code is about 15% of the methods and highly regular. Model it with a per-layout template:
   - `DataBinderMapperImpl.getDataBinder` → `XBindingImpl.<init>`;
   - `setViewModel`/`setVariable` from the owner;
   - `executeBindings` (FRAMEWORK);
   - `onFieldChange` for observable fields;
   - `$N.onChange` (GUI for two-way fields);
   - mark the 238 static helpers and getters DEAD.
7. Qualify the 7 colliding simple class names before joining with JaCoCo.
8. Flag `ErrorReportActivity` as unmeasurable in comparisons against the baseline, and do not treat its 0 hits as evidence.

**Hazard candidates found while reading (not reproduced; the fixes are suggestions only, nothing was changed):**
- **OK does nothing on AddTorrent error dialogs.** The decode, fetch, invalid-link, OOM and add-error dialogs are created with `autoDismiss=false`, and `handleAlertDialogEvent` handles no event for their tags. Only Back (or an outside tap, FW-MEMORY) closes them (`AddTorrentActivity.java:237-275, 436-444, 462-534`).
  - Model the OK edge as a no-op self-loop.
  - Possible fix: pass `autoDismiss=true`.
- **FeedActivity swaps its error handlers.** A backup failure shows the *restore* error dialog and a restore failure shows the *backup* one (`FeedActivity.java:346-371`).
  - Model the edges as written.
  - Possible fix: swap the two method references.
- **Scheduling uses the wrong times.** Enabling "shutdown" schedules the stop alarm at the **start** time (`SchedulingSettingsFragment.java:212-213`), and `SchedulerReceiver.onStopApp` re-arms through `setStartAppAlarm` (`SchedulerReceiver.java:92`).
  - Possible fix: use `schedulingShutdownTime()` and `setStopAppAlarm`.
- **Speed limit ignores the download field.** `DetailTorrentFragment.setSpeedLimit` checks the upload field twice and never the download field (`:777`). An empty download field becomes 0 through the caught NumberFormatException.

**Open questions (UNVERIFIED):**
- Why the selection library never ran (§2.3; test with UiAutomator vs `input` long-press).
- Whether the baseline emulator had network.
- Whether the fixtures were pushed to `/sdcard/Download` during the baseline. The add flow opened files with `readTorrentFile`, but which files is unknown.
- That the offline magnet add and the CreateTorrent+seed path work on the API 27 x86 emulator (libtorrent native).
- The exact `RequestMultiplePermissions` behaviour for an empty array (FW-MEMORY).
