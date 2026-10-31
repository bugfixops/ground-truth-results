# Batch 18 helper report

Membership is exactly the 40 rows with `batch==18` in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`. The complete plan output, source excerpts, and searches are in `scratch/batch_018_helper_printed.txt`. Source shows app-startup routes for `MainApplication`, UI/worker routes through feed parsing and torrent creation, and utility call sites for HTTP, input filters, and repositories. The two generated mapper lookup initializers remain OPEN because the required source-root grep found no generated implementation to inspect; the synthetic uncaught-handler lambda also remains OPEN because its registration is conditional and external callback execution is not established by the source alone.

| Method | Label | Kind | Reason | Printed evidence |
|---|---|---|---|---|
| `libretorrent.DataBinderMapperImpl$InnerBrLookup.<clinit>` | OPEN | — | Generated implementation is not present in the app Java source root; exact initialization route is not inspectable from source. | source-root grep in `batch_018_helper_printed.txt` |
| `libretorrent.DataBinderMapperImpl$InnerLayoutIdLookup.<clinit>` | OPEN | — | Generated implementation is not present in the app Java source root; exact initialization route is not inspectable from source. | source-root grep in `batch_018_helper_printed.txt` |
| `MainApplication.<clinit>` | REACHABLE | — | Static initializer executes on application class initialization and calls `AppCompatDelegate.setCompatVectorFromResourcesEnabled`. | `MainApplication.java:37-43`; `AndroidManifest.xml:31-32` |
| `MainApplication.<init>` | REACHABLE | — | Manifest names MainApplication as the Application class; its implicit constructor is run when Android creates the application instance. | `AndroidManifest.xml:31-32`; `MainApplication.java:37` |
| `MainApplication.increaseCursorWindowSize` | REACHABLE | — | `onCreate()` calls this helper. | `MainApplication.java:45-48,68-70,73-78` |
| `MainApplication.lambda$onCreate$0` | OPEN | — | The lambda body is registered only if the current default uncaught-exception handler is null; runtime callback delivery is not established by the printed app source. | `MainApplication.java:60-65` |
| `MainApplication.onCreate` | REACHABLE | — | Android creates the manifest-declared Application and dispatches its `onCreate()` lifecycle callback. | `AndroidManifest.xml:31-32`; `MainApplication.java:37,45-70` |
| `FeedParser.<init>` | REACHABLE | — | FeedFetcherWorker constructs FeedParser when fetching an existing channel. | `FeedFetcherWorker.java:144-162`; `FeedParser.java:62-82` |
| `FeedParser.findDownloadUrl` | REACHABLE | — | `getItems()` invokes it when ordinary links contain no downloadable magnet/torrent URL. | `FeedParser.java:95-103,141-161` |
| `FeedParser.getFirstNotNullLink` | REACHABLE | — | Called while processing each feed item. | `FeedParser.java:95-98,118-126` |
| `FeedParser.getItems` | REACHABLE | — | FeedFetcherWorker invokes it after constructing FeedParser. | `FeedFetcherWorker.java:154-167`; `FeedParser.java:89-116` |
| `FeedParser.getTitle` | REACHABLE | — | Worker reads title when a channel currently has no name. | `FeedFetcherWorker.java:174-179`; `FeedParser.java:84-87` |
| `FeedParser.isMagnetOrTorrent` | REACHABLE | — | Called from downloadable-link, enclosure, and GUID parsing branches. | `FeedParser.java:128-138,168-180,254-266` |
| `FeedParser.watchDownloadableLink` | REACHABLE | — | Called unconditionally for each parsed item's links. | `FeedParser.java:95-103,128-139` |
| `FeedParser.watchEnclosure` | REACHABLE | — | `findDownloadUrl` checks enclosure metadata first. | `FeedParser.java:141-151,168-180` |
| `FeedParser.watchGuid` | REACHABLE | — | `findDownloadUrl` checks GUID after earlier torrent metadata fields fail to provide a URL. | `FeedParser.java:141-160,254-261` |
| `FeedParser.watchMediaContent` | REACHABLE | — | `findDownloadUrl` checks MediaRSS content after enclosure and EZRSS info hash. | `FeedParser.java:141-157,188-208` |
| `FeedParser.watchMediaHash` | REACHABLE | — | Called by MediaRSS content parsing when content URLs do not yield a download URL. | `FeedParser.java:188-208,215-229` |
| `FeedParser.watchTorrentInfoHash` | REACHABLE | — | `findDownloadUrl` checks the EZRSS torrent info hash after enclosure parsing. | `FeedParser.java:141-155,236-247` |
| `HttpConnection.<init>` | REACHABLE | — | `Utils.fetchHttpUrl` constructs it for feed fetching and other app HTTP fetches. | `Utils.java:462-475`; `HttpConnection.java:66-70` |
| `HttpConnection.run` | REACHABLE | — | `Utils.fetchHttpUrl` calls `connection.run()` after installing a listener. | `Utils.java:477-512`; `HttpConnection.java:77-120` |
| `HttpConnection.setListener` | REACHABLE | — | `Utils.fetchHttpUrl` registers the listener that consumes connection and response callbacks. | `Utils.java:477-511`; `HttpConnection.java:72-75` |
| `InputFilterRange.<clinit>` | REACHABLE | — | Initializes PORT_FILTER and UNSIGNED_INT, referenced by settings and detail-torrent screens. | `InputFilterRange.java:31-41`; caller search in printed output |
| `InputFilterRange.<init>` | REACHABLE | — | Builder.build constructs the range filter. | `InputFilterRange.java:46-50,107-113` |
| `InputFilterRange.filter` | REACHABLE | — | App registers InputFilterRange instances on EditText fields; Android invokes registered InputFilter.filter while editing. | `InputFilterRange.java:64-81`; app `setFilters` call sites in printed output |
| `InputFilterRange.getMax` | UNREACHABLE | no_trigger_in_app | No source caller; full source-root search finds only the declaration. | `InputFilterRange.java:58-62`; `getMax/getMin` search output |
| `InputFilterRange.getMin` | UNREACHABLE | no_trigger_in_app | No source caller; full source-root search finds only the declaration. | `InputFilterRange.java:52-56`; `getMax/getMin` search output |
| `InputFilterRange.inRange` | REACHABLE | — | `filter()` calls it for parsed integer input. | `InputFilterRange.java:71-85` |
| `InputFilterRange$Builder.<init>` | REACHABLE | — | Static filter initialization and settings code construct Builder instances. | `InputFilterRange.java:33-41,88-93`; caller search in printed output |
| `InputFilterRange$Builder.build` | REACHABLE | — | Static filters and settings filter configuration call `build()`. | `InputFilterRange.java:33-41,107-113`; caller search in printed output |
| `InputFilterRange$Builder.setMax` | REACHABLE | — | Static filters and settings builders set maximum values. | `InputFilterRange.java:33-41,100-105`; caller search in printed output |
| `InputFilterRange$Builder.setMin` | REACHABLE | — | Static filters and settings builders set minimum values. | `InputFilterRange.java:33-41,93-98`; caller search in printed output |
| `RepositoryHelper.getFeedRepository` | REACHABLE | — | Called by feed ViewModels and fetch workers. | `RepositoryHelper.java:52-59`; caller search in printed output |
| `RepositoryHelper.getSettingsRepository` | REACHABLE | — | Called across services, receivers, ViewModels, and utility code. | `RepositoryHelper.java:61-67`; caller search in printed output |
| `RepositoryHelper.getTagRepository` | REACHABLE | — | Called by TorrentEngine, ViewModels, and TorrentInfoProvider. | `RepositoryHelper.java:69-75`; caller search in printed output |
| `RepositoryHelper.getTorrentRepository` | REACHABLE | — | Called by TorrentEngine and DetailTorrentViewModel. | `RepositoryHelper.java:43-50`; caller search in printed output |
| `TorrentBuilder.<init>` | REACHABLE | — | CreateTorrentViewModel constructs it in its builder path. | `CreateTorrentViewModel.java:151-158,177-194`; `TorrentBuilder.java:88-92` |
| `TorrentBuilder.addTrackers` | REACHABLE | — | Called in CreateTorrentViewModel's makeBuilder chain. | `CreateTorrentViewModel.java:189-195`; `TorrentBuilder.java:116-125` |
| `TorrentBuilder.addUrlSeeds` | REACHABLE | — | Called in CreateTorrentViewModel's makeBuilder chain. | `CreateTorrentViewModel.java:189-195`; `TorrentBuilder.java:127-132` |
| `TorrentBuilder.build` | REACHABLE | — | `CreateTorrentViewModel.buildTorrent()` calls it and subscribes to its result. | `CreateTorrentViewModel.java:151-174`; `TorrentBuilder.java:174-182` |

Count: 40 plan rows; 35 REACHABLE; 2 UNREACHABLE (`no_trigger_in_app`); 3 OPEN. No coverage evidence was used. These helper labels are source research only, not graph edits.
