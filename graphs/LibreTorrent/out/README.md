# LibreTorrent 3.5.2: page-jump and method-call graph (generated)

A map of how every method of the open-source Android app **LibreTorrent** (proninyaroslav/libretorrent@3.5.2, source commit `d93e92ea`, package `org.proninyaroslav.libretorrent.debug`, APK sha256 `5e05d2ff…a1bd36bf`) can be triggered: from which page, by which user gesture or system event, through which framework callback or call. It is the build in `final_java_only/LibreTorrent`.

**How this one differs from Currency, hash-checker, openlauncher and Omni-Notes:** those graphs were written by hand from reading the source. This one was **generated** by `tools/gen_edges.py` from the bytecode, `AndroidManifest.xml` and `res/` XML, and then checked against the baseline coverage and reviewed (see "How much to trust it"). Every number below is recomputed from the files in this folder.

## What is in this folder

| File | What it is |
|---|---|
| `libretorrent_trigger_graph.json` | The graph: pages, methods, verdicts, edges. Every edge has an `evidence` label; an edge may carry `env` (needs something outside the app) and `needs_state` (needs an earlier action or setting). |
| `methods.csv` | One row per method: verdict, steps from launch, the user taps on the best path, the path, number of incoming edges, note. Extra columns: `jvm_descriptor`, `monkey_hit`, `ape_hit` (1-hour API 27 baseline runs; empty = JaCoCo does not report the method), and for methods the baseline never ran `frontier_from`, `frontier_first_unrun`, `frontier_edge_kind`, `frontier_edge_evidence`, `steps_after_frontier` (where the chain from code that ran first enters code that never ran). |
| `libretorrent_trigger_graph.html` | The same data in the viewer from the Currency example. Optional. |
| `build_report.txt` | Output of the validation script (0 errors, 0 warnings, baseline cross-check, the list of reachable methods the baseline never ran). |

## Numbers

- **4732 methods** (the app's own code, aligned with what JaCoCo reports), **73 pages** (12 of them `S_NEW_<Class>` anchors: a class whose empty default constructor is not in the JaCoCo method universe is constructed through such a node), **12622 edges**: 3968 from the bytecode call extractor, 8654 added by the generator or by hand.
- Edge kinds: ASYNC 130, CALL 4945, ENTERS 55, ENTRY 9, FRAMEWORK 4283, GUI 48, INTENT 54, LIFECYCLE 3042, REGISTER 2, SYSTEM 54.
- Verdicts: **3108 reachable**, **1215 reachable after setup**, **409 dead**, 0 framework-only.
- 113 edges are gated by an outside environment, 2077 need an earlier action or setting; 240 methods are reached only through an environment gate, 1215 only after setup. Average route length: 11.4 edges.
- Evidence labels: 7662 `FW-MEMORY`, 54 `INFERRED`, 4906 `SRC`.
- Largest dead groups (auto-classified, see limits): `NanoHTTPD` (19 of 37), `SafFileSystem` (8 of 24), `AtomFeed` (7 of 11), `Rss1Feed` (7 of 11), `Rss2Feed` (7 of 11), `EzRssTorrentItem` (6 of 11), `TorrentDownloadImpl` (6 of 112), `ActivityAddTorrentBinding` (6 of 7), `ActivityFilemanagerDialogBinding` (6 of 8), `ActivityLogBinding` (6 of 8), `AddTorrentInfoBinding` (6 of 8), `DetailTorrentAppbarBinding` (6 of 7), `DialogAddFeedChannelBinding` (6 of 8), `DialogAddLinkBinding` (6 of 8).

## Comparison with the baseline coverage (APE and Monkey, 1 hour each, API 27)

- 2080 of the 4726 observable methods ran in at least one run (Monkey 1560, APE 2063, both 1543). **0 dead or framework-only methods ran**, so the coverage contradicts no verdict.
- **2646 methods were run by neither tool.** By the graph: 403 are dead; 240 are reachable only through an outside environment; 1147 need an earlier in-app action or setting; **856 are reachable with no modelled setup and no outside help, yet were never run** (the clearest target list for the paper). Classes holding most of them: `SettingsRepositoryImpl` (43), `TorrentSessionImpl` (33), `MainFragment` (15), `TorrentEngine` (14), `TorrentFilterCollection` (12), `Torrent` (12), `DateUtils` (11), `FragmentAddTorrentInfoBindingLargeLandNotouchImpl` (11), `FragmentAddTorrentInfoBindingSw600dpLandImpl` (11), `FeedFragment` (11), `MagnetInfo` (10), `TorrentInfo` (9), `DatabaseMigration$RoomDatabaseMigration` (9), `SafFsModule` (9).
- **Where the baseline stopped (frontier).** For 2239 of the never-run reachable methods the graph gives the edge where the chain from methods that ran first enters code that never ran (`frontier_*` columns of `methods.csv`: `frontier_from` is the source of that edge, a method that ran or a screen entered from one; `frontier_first_unrun` is its target): 1070 FRAMEWORK, 1055 CALL, 47 LIFECYCLE, 38 ASYNC, 19 GUI, 9 INTENT, 1 SYSTEM. A `CALL` frontier is a branch inside code that ran and was not taken (a data, setting or error condition); a `FRAMEWORK`, `GUI`, `INTENT` or `SYSTEM` frontier is a callback, tap or start that no tool triggered. The ten frontier nodes that unlock the most never-run methods:
  - `MainActivity.showDetailTorrent` (506 never-run methods behind it): reached from `MainActivity.subscribeMsgViewModel` by a `FRAMEWORK` edge (SRC MainActivity.java:439 (bytecode))
  - `NanoHTTPD.createClientHandler` (120 never-run methods behind it): reached from `NanoHTTPD$ServerRunnable.run` by a `CALL` edge (SRC NanoHTTPD.java:1347 (bytecode))
  - `TorrentSessionImpl.newTask` (95 never-run methods behind it): reached from `TorrentSessionImpl$InnerListener.alert` by a `CALL` edge (SRC TorrentSessionImpl.java:1081 (bytecode))
  - `FeedParser.getItems` (91 never-run methods behind it): reached from `FeedFetcherWorker.fetchChannel` by a `CALL` edge (SRC FeedFetcherWorker.java:165 (bytecode))
  - `FeedChannelListAdapter$KeyProvider.getKey` (52 never-run methods behind it): reached from `FeedChannelListAdapter$KeyProvider.<init>` by a `FRAMEWORK` edge (FW-MEMORY the framework / library calls this callback on an instance created by the app)
  - `DefaultFeedParser.parse` (44 never-run methods behind it): reached from `FeedParser.<init>` by a `CALL` edge (SRC FeedParser.java:71 (bytecode))
  - `CreateTorrentDialog.buildTorrent` (43 never-run methods behind it): reached from `CreateTorrentDialog.lambda$new$11` by a `CALL` edge (SRC CreateTorrentDialog.java:546 (bytecode))
  - `AddTorrentViewModel.makeFileTree` (36 never-run methods behind it): reached from `AddTorrentActivity.onStopDecode` by a `CALL` edge (SRC AddTorrentActivity.java:345 (bytecode))
  - `AddTorrentViewModel.lambda$addTorrent$5` (28 never-run methods behind it): reached from `AddTorrentViewModel.addTorrent` by a `ASYNC` edge (SRC AddTorrentViewModel.java:527 (bytecode))
  - `TorrentEngine.makeInfo` (28 never-run methods behind it): reached from `TorrentEngine.makeInfoListSync` by a `CALL` edge (SRC TorrentEngine.java:822 (bytecode))
- Harness facts that matter for target selection: `merged.ec` omits the launch dump `00000.ec`, so first-launch code can show `monkey_hit = 0` although it ran; one dump per tool may be unreadable, and a process that dies between 30-second dumps loses its coverage, so "never hit" does not strictly prove "never ran".

## How much to trust it

- **Method.** `gen_edges.py` applies Android framework rules to the compiled classes: process entry (Application, launcher, exported components behind an `env` gate), lifecycle callbacks and one page `S_<Activity|Fragment>` per screen, UI and system callbacks of every constructed class with a framework ancestor, lambdas and method references (creator method -> body, the tap label is read from the source line), `startActivity(new Intent(ctx, X.class))` and custom intent actions, classes named in layout / xml / menu / navigation files and where they are inflated, activity and permission results, `Handler` messages, ButterKnife / EventBus / data binding / Dagger / Glide / Icepick / Parceler / ORMLite / Room glue, static initialisers, and template-method receiver variants (`Base.m@Sub`). Direct calls come from the bytecode (`extract_calls.py`, class-hierarchy analysis for virtual calls). Methods that nothing reaches are reported DEAD (`AUTO_DEAD`).
- **Calibration on the five hand-written apps** (the generator run on the same inputs, compared with the hand-written verdicts; `tools/calibrate.py`): dead-versus-alive agreement 97.2% (Currency), 96.5% (Diary), 98.5% (hash-checker), 92.9% (openlauncher), 93.8% (Omni-Notes); exact verdict agreement 93.8% (Currency), 95.5% (Diary), 71.1% (hash-checker), 76.9% (openlauncher), 63.1% (Omni-Notes). The gap is almost entirely `needs_state`: a human reads "needs a note / a folder / a setting" out of the code, the generator only knows list rows. (openlauncher and Omni-Notes were used while the generator rules were developed; Currency, Diary and hash-checker were not.)
- **Checks done on this app:** the validation script (0 errors, 0 warnings: every method has a route or a DEAD verdict, every page is reachable); the baseline cross-check above (0 contradictions after the generator rules were completed by reading the contradictions one by one); random shortest paths were read for shortcuts.
- **Not checked on a device.** Framework rules are `FW-MEMORY` (recalled, not checked against AOSP source); guesses are `INFERRED`.

## Limits (read before using a verdict)

- **`REACHABLE` means "no modelled setup", not "no setup".** Gates beyond list rows (data that must exist, settings, earlier actions, incoming intents, files on the device) are modelled only where listed in the review notes. Adapter row callbacks, row-based listeners and action modes carry `needs_state` = "the list shows at least one row".
- A callback is reachable as soon as an instance of its class is constructed; the real trigger (a tap on one specific control) is shown in the `gui_steps` column only where the source line names the control. Menu and click handlers that switch on `R.id.x` give one labelled edge per case (`case R.id.x`), found by the nearest preceding case label (`INFERRED`).
- `Handler.handleMessage`, EventBus subscribers and Dagger-provided objects are linked from every send / post / graph-build site (`INFERRED`), so their routes can be shorter than the real ones.
- DEAD is automatic: nothing in the bytecode, manifest, XML or the modelled libraries reaches the method. Entries through reflection, JNI, other generated code or libraries that are not modelled would be missed (the baseline contradiction check found and fixed every such case that the 1-hour runs exercised).
- Calls inside catch blocks, data-dependent branches and feature flags are ordinary calls unless the review notes say otherwise.

## Review notes for this app

What was reviewed by hand (class level, from method names, the manifest, the layouts and the baseline hit counts):

- **What the baseline reached.** 2,080 of 4,732 methods ran: the main list, the add-torrent dialogs, the create-torrent dialog, the settings screens, the feed screens, the Room database (`AppDatabase_Impl`, `*Dao_Impl`) and the torrent engine start-up. **No method of the torrent detail screens ran** (`DetailTorrentActivity`, `DetailTorrentFragment` and its info / files / peers / pieces / trackers / state fragments, `DetailTorrentViewModel`), and `TorrentDownloadImpl` (the wrapper around a torrent handle) ran in 6 of 112 methods.
- **Content gate (`needs_state`):** the classes that need a torrent to exist (`DetailTorrent*`, `TorrentDownloadImpl`, `TorrentInputStream`, `TorrentContentFileTree`, `TorrentDetailsInfo`, `TrackerInfo`, `BencodeFileItem`, `FileTree`, `AdvancedTorrentInfo`, `AdvancedPeerInfo`, `PeerInfo`, `PieceInfo`, `TorrentInfoProvider`, `TorrentStream*`, `NanoHTTPD*`: the streaming HTTP server) carry "a torrent is in the list". The baseline fixtures contain no `.torrent` file.
- **Environment gates:** the RSS / Atom feed parsers and workers (`EzRss01Parser`, `MediaRssParser`, `DefaultFeedParser`, `FeedHandler`, `FeedFetcherWorker`, `FeedDownloaderWorker`, `XMLInputStream`: a reachable feed URL) and the system receivers (`BootReceiver`, `SchedulerReceiver`, `PowerReceiver`). Services (`TorrentService`) and the notification receiver hang below `S_SYS_<Class>` anchors, entered from the app's own `startService` calls or from `S_ENTRY`.
- **Branch gates read from the source at the frontier (`CFG['EDGES']`):** `MainActivity.showDetailTorrent` (a torrent row was tapped: `needs_state`), `TorrentSessionImpl$InnerListener.alert` -> `newTask` (the add-torrent alert of the native session: `needs_state`), `TorrentEngine.makeInfoListSync` -> `makeInfo` (the loop over the stored torrents: `needs_state`), `AddTorrentActivity.onStopDecode` -> `AddTorrentViewModel.makeFileTree` (a decoded `.torrent` / magnet link: `needs_state`), `CreateTorrentDialog` save-location callback -> `buildTorrent` (the system document picker returned a location: `env`).
- **Data binding.** The project uses data binding with many layouts: `*Binding` (abstract) / `*BindingImpl` (concrete, plus `...Sw600dpLandImpl` and `...LargeLandNotouchImpl` variants) are in the method universe. The generator links each `...Impl` constructor to the method that mentions `R.layout.<name>` (DataBindingUtil inflate / setContentView) and to the generated `DataBinderMapperImpl`. The `inflate` / `bind` factories of the abstract `*Binding` classes are dead (the app only goes through `DataBindingUtil`).
- **Room, Rx, WorkManager.** `AppDatabase_Impl` is linked from `Room.databaseBuilder(.., AppDatabase.class, ..)` (class literal of an abstract class with a generated implementation); RxJava lambdas and `Consumer` / `Function` anonymous classes are linked from the method that creates them; the feed workers are linked from the `OneTimeWorkRequest` builders (class literals).
- **Node names.** Two classes are called `TagsAdapter` (in `ui.tag` and `ui.main.drawer`) and two `TagItem`: their methods are named `tag.TagsAdapter.<init>(...)` / `drawer.TagsAdapter...` in the CSV and JSON.
- **Dead code** is mostly the bundled `NanoHTTPD` library (19 of 37 methods, the rest are behind the streaming server), `SafFileSystem` (8 of 24), the feed model classes of unused formats (`AtomFeed`, `Rss1Feed`, `Rss2Feed`, `EzRssTorrentItem` getters) and the `inflate` / `bind` factories of the data-binding classes.
- **Not gated but never run (the target list):** `SettingsRepositoryImpl` preference accessors (43 of 184: battery, scheduling, roaming, watch-dir settings), `TorrentSessionImpl` / `TorrentEngine` add / delete / magnet-fetch paths, `CreateTorrentViewModel` and `TorrentBuilder` (building a torrent), `AddTorrentViewModel` metadata handling, `MainFragment` delete and filter lambdas, `TorrentFilterCollection` date filters, `DateUtils`.

## JSON shape (short)

```
{ "title", "screens": {page: description}, "methods": [...], "verdict": {method: REACHABLE|REACHABLE_AFTER_SETUP|DEAD|FRAMEWORK_ONLY},
  "dead": {method: reason}, "framework_only": {method: reason},
  "edges": [ {id, src, dst, kind, trigger, gui[], guard, reads[], writes[], note, needs_state, evidence, env} ] }
```
`src`/`dst` are methods (`Class.method`, overloads as `Class.method(Type,Type)`, classes that share a simple name get a package prefix) or pages (`S_...`). A suffix `@CONTEXT` is the same method in a specific receiver class (`Base.m@Sub`) or context.
