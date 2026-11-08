# Batch 18 source audit

Membership is exactly the 40 rows in `batch_018_plan.txt`; helper excerpts and call-site findings are in `batch_018_helper_printed.txt`. Independent source search for InputFilterRange getter callers and rule-F generated mapper declarations is in `batch_018_independent_printed.txt`.

The helper found 35 source-supported local paths, but these still need full hand-authored graph routes before they can be labeled REACHABLE. Two InputFilterRange getters have no caller in the source tree and are labeled UNREACHABLE `no_trigger_in_app`. The two generated mapper lookup initializers and the conditional uncaught-handler callback remain OPEN. All other rows remain OPEN pending complete entry routes.

| Method | Label | Reason / evidence |
|---|---|---|
| `libretorrent.DataBinderMapperImpl$InnerBrLookup.<clinit>` | OPEN | Generated source and route unavailable; source-root grep in `batch_018_helper_printed.txt`. |
| `libretorrent.DataBinderMapperImpl$InnerLayoutIdLookup.<clinit>` | OPEN | Generated source and route unavailable; source-root grep in `batch_018_helper_printed.txt`. |
| `MainApplication.<clinit>` | OPEN | Manifest application class; route not yet hand-authored. `MainApplication.java:37-43`; manifest `31-32`. |
| `MainApplication.<init>` | OPEN | Manifest application class; route not yet hand-authored. manifest `31-32`; source print in helper. |
| `MainApplication.increaseCursorWindowSize` | OPEN | Called by onCreate; complete graph route not handwritten. `MainApplication.java:45-48,68-78`. |
| `MainApplication.lambda$onCreate$0` | OPEN | Conditional uncaught-handler callback; runtime dispatch unresolved. `MainApplication.java:60-65`. |
| `MainApplication.onCreate` | OPEN | Manifest lifecycle callback; complete graph route not handwritten. manifest `31-32`; `MainApplication.java:37,45-70`. |
| `FeedParser.<init>` | OPEN | FeedFetcherWorker constructs it; full worker route not handwritten. `FeedFetcherWorker.java:144-162`; `FeedParser.java:62-82`. |
| `FeedParser.findDownloadUrl` | OPEN | Called by getItems; full worker entry path not handwritten. `FeedParser.java:95-103,141-161`. |
| `FeedParser.getFirstNotNullLink` | OPEN | Called in item processing; full worker entry path not handwritten. `FeedParser.java:95-98,118-126`. |
| `FeedParser.getItems` | OPEN | Worker invokes it; full worker entry path not handwritten. `FeedFetcherWorker.java:154-167`; `FeedParser.java:89-116`. |
| `FeedParser.getTitle` | OPEN | Worker calls it; full worker entry path not handwritten. `FeedFetcherWorker.java:174-179`; `FeedParser.java:84-87`. |
| `FeedParser.isMagnetOrTorrent` | OPEN | Internal caller paths exist; full worker route not handwritten. `FeedParser.java:128-138,168-180,254-266`. |
| `FeedParser.watchDownloadableLink` | OPEN | Called by getItems; full worker route not handwritten. `FeedParser.java:95-103,128-139`. |
| `FeedParser.watchEnclosure` | OPEN | Called in URL fallback; full worker route not handwritten. `FeedParser.java:141-151,168-180`. |
| `FeedParser.watchGuid` | OPEN | Called in URL fallback; full worker route not handwritten. `FeedParser.java:141-160,254-261`. |
| `FeedParser.watchMediaContent` | OPEN | Called in URL fallback; full worker route not handwritten. `FeedParser.java:141-157,188-208`. |
| `FeedParser.watchMediaHash` | OPEN | Called in URL fallback; full worker route not handwritten. `FeedParser.java:188-208,215-229`. |
| `FeedParser.watchTorrentInfoHash` | OPEN | Called in URL fallback; full worker route not handwritten. `FeedParser.java:141-155,236-247`. |
| `HttpConnection.<init>` | OPEN | Utils constructs it; complete app caller route not handwritten. `Utils.java:462-475`; `HttpConnection.java:66-70`. |
| `HttpConnection.run` | OPEN | Utils calls run; full app route not handwritten. `Utils.java:477-512`; `HttpConnection.java:77-120`. |
| `HttpConnection.setListener` | OPEN | Utils registers listener; full app route not handwritten. `Utils.java:477-511`; `HttpConnection.java:72-75`. |
| `InputFilterRange.<clinit>` | OPEN | Static filter use sites exist; complete app route not handwritten. `InputFilterRange.java:31-41`; helper caller print. |
| `InputFilterRange.<init>` | OPEN | Builder constructs it; complete app route not handwritten. `InputFilterRange.java:46-50,107-113`. |
| `InputFilterRange.filter` | OPEN | App registers as EditText filter; framework callback needs route evidence. `InputFilterRange.java:64-81`; `setFilters` sites in helper. |
| `InputFilterRange.getMax` | UNREACHABLE | no_trigger_in_app; full source search shows only declaration. `InputFilterRange.java:58-62`; `batch_018_independent_printed.txt`. |
| `InputFilterRange.getMin` | UNREACHABLE | no_trigger_in_app; full source search shows only declaration. `InputFilterRange.java:52-56`; `batch_018_independent_printed.txt`. |
| `InputFilterRange.inRange` | OPEN | Called by filter; framework callback route remains OPEN. `InputFilterRange.java:71-85`. |
| `InputFilterRange$Builder.<init>` | OPEN | Source constructors exist; full app route not handwritten. `InputFilterRange.java:33-41,88-93`. |
| `InputFilterRange$Builder.build` | OPEN | Called in app code; full entry route not handwritten. `InputFilterRange.java:33-41,107-113`. |
| `InputFilterRange$Builder.setMax` | OPEN | Called in app code; full entry route not handwritten. `InputFilterRange.java:33-41,100-105`. |
| `InputFilterRange$Builder.setMin` | OPEN | Called in app code; full entry route not handwritten. `InputFilterRange.java:33-41,93-98`. |
| `RepositoryHelper.getFeedRepository` | OPEN | Called by workers/ViewModels; full entry routes not handwritten. `RepositoryHelper.java:52-59`; helper caller print. |
| `RepositoryHelper.getSettingsRepository` | OPEN | Called throughout app; full entry routes not handwritten. `RepositoryHelper.java:61-67`; helper caller print. |
| `RepositoryHelper.getTagRepository` | OPEN | Called by app components; full entry routes not handwritten. `RepositoryHelper.java:69-75`; helper caller print. |
| `RepositoryHelper.getTorrentRepository` | OPEN | Called by engine/ViewModel; full entry routes not handwritten. `RepositoryHelper.java:43-50`; helper caller print. |
| `TorrentBuilder.<init>` | OPEN | CreateTorrentViewModel constructs it; full screen route not handwritten. `CreateTorrentViewModel.java:151-158,177-194`; `TorrentBuilder.java:88-92`. |
| `TorrentBuilder.addTrackers` | OPEN | App makeBuilder calls it; full screen route not handwritten. `CreateTorrentViewModel.java:189-195`; `TorrentBuilder.java:116-125`. |
| `TorrentBuilder.addUrlSeeds` | OPEN | App makeBuilder calls it; full screen route not handwritten. `CreateTorrentViewModel.java:189-195`; `TorrentBuilder.java:127-132`. |
| `TorrentBuilder.build` | OPEN | ViewModel calls and subscribes; full screen route not handwritten. `CreateTorrentViewModel.java:151-174`; `TorrentBuilder.java:174-182`. |

Count: 40 plan rows; 0 REACHABLE; 2 `UNREACHABLE/no_trigger_in_app`; 38 OPEN. No coverage evidence was used.
