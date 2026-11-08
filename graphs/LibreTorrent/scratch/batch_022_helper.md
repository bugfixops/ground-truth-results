# Batch 22 helper report

Membership is exactly the 40 rows with `batch==22` in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`. Printed plan rows, source excerpts, and call-site searches are in `scratch/batch_022_helper_printed.txt`. TorrentEngine construction/start/stop and its torrent operations are reachable from TorrentService, view models, workers, receivers, and its own listener callbacks. DownloadsCompletedListener registers its callbacks from `TorrentEngine.doStart`. SessionErrorFilter is initialized as an engine field and consulted by its session-error listener.

Three AddTorrentParams parcel transport methods are UNREACHABLE: app source constructs the object and passes it directly to engine/session methods, but does not put it in a Bundle/Intent or parcel it. Its anonymous Creator constructor is reachable because AddTorrentParams class initialization creates the static CREATOR field when the class is first used.

| Method | Label | Kind | Reason | Printed evidence |
|---|---|---|---|---|
| `AddTorrentParams.writeToParcel` | UNREACHABLE | no_trigger_in_app | No app call parcels AddTorrentParams; source uses it as an in-memory value for TorrentEngine/TorrentSession. | `AddTorrentParams.java:90-107`; source-wide AddTorrentParams/Parcelable use search |
| `AddTorrentParams$1.<init>` | REACHABLE | — | The static CREATOR field instantiates this anonymous Creator when AddTorrentParams initializes; AddTorrentParams is constructed by AddTorrentViewModel and FeedDownloaderWorker. | `AddTorrentParams.java:34,109-119`; `AddTorrentViewModel.java:510-529`; `FeedDownloaderWorker.java:178-181` |
| `AddTorrentParams$1.createFromParcel` | UNREACHABLE | no_trigger_in_app | CREATOR is never used to transport/unparcel AddTorrentParams in app source; it is only declared and passed as an in-memory parameter object. | `AddTorrentParams.java:109-113`; source-wide AddTorrentParams/Parcelable use search |
| `AddTorrentParams$1.newArray` | UNREACHABLE | no_trigger_in_app | No source parcel path invokes the Creator's array factory for AddTorrentParams. | `AddTorrentParams.java:109,116-118`; source-wide AddTorrentParams/Parcelable use search |
| `DownloadsCompletedListener.<init>` | REACHABLE | — | TorrentEngine's constructor creates one listener instance. | `TorrentEngine.java:128-139`; `DownloadsCompletedListener.java:40-43` |
| `DownloadsCompletedListener.lambda$listen$0` | REACHABLE | — | The listener's lambdas are created in `listen()`, which TorrentEngine subscribes during startup; the callback/event action runs on completion/removal. | `DownloadsCompletedListener.java:45-84`; `TorrentEngine.java:234-251` |
| `DownloadsCompletedListener.lambda$listen$1` | REACHABLE | — | A callback lambda in `listen()` participates in the subscribed completion listener/event action path. | `DownloadsCompletedListener.java:47-78`; `TorrentEngine.java:243-251,307-309` |
| `DownloadsCompletedListener.lambda$listen$2` | REACHABLE | — | The disposal-action lambda in `listen()` removes the registered listener when the service clears its disposables. | `DownloadsCompletedListener.java:80-84`; `TorrentEngine.java:292-300`; `TorrentService.java:157-168` |
| `DownloadsCompletedListener.listen` | REACHABLE | — | `TorrentEngine.doStart()` subscribes to this Completable. | `DownloadsCompletedListener.java:45-85`; `TorrentEngine.java:234-251` |
| `DownloadsCompletedListener$1.<init>` | REACHABLE | — | `listen()` constructs this TorrentEngineListener anonymous implementation. | `DownloadsCompletedListener.java:55-78` |
| `DownloadsCompletedListener$1.onTorrentFinished` | REACHABLE | — | Registered listener handles finished events forwarded by torrent download/session code. | `DownloadsCompletedListener.java:55-70,80-84`; `TorrentDownloadImpl.java:483`; `TorrentEngine.java:307-309` |
| `DownloadsCompletedListener$1.onTorrentRemoved` | REACHABLE | — | Registered listener handles removal events forwarded by session code. | `DownloadsCompletedListener.java:55,72-77,80-84`; `TorrentSessionImpl.java:389`; `TorrentEngine.java:307-309` |
| `DownloadsCompletedListener$1.onTorrentStateChanged` | REACHABLE | — | Registered listener handles state changes forwarded by torrent download code. | `DownloadsCompletedListener.java:55-64,80-84`; `TorrentDownloadImpl.java:227`; `TorrentEngine.java:307-309` |
| `SessionErrorFilter.<clinit>` | REACHABLE | — | TorrentEngine's field initialization creates SessionErrorFilter, triggering initialization of its static filteredErrors set. | `TorrentEngine.java:113,128-139`; `SessionErrorFilter.java:24-28` |
| `SessionErrorFilter.<init>` | REACHABLE | — | TorrentEngine constructs it in its instance field initializer. | `TorrentEngine.java:113,128-139`; `SessionErrorFilter.java:24-32` |
| `SessionErrorFilter.skip` | REACHABLE | — | TorrentEngine's session-error listener calls it before notifying. | `TorrentEngine.java:1384-1390`; `SessionErrorFilter.java:30-32` |
| `TorrentEngine.<clinit>` | REACHABLE | — | App code obtains the singleton through `getInstance`, which initializes the class and its static fields. | `TorrentEngine.java:96-97,115-125`; `TorrentService.java:108-110` |
| `TorrentEngine.<init>` | REACHABLE | — | `getInstance()` constructs the singleton on first access. | `TorrentEngine.java:117-125,128-141` |
| `TorrentEngine.addListener` | REACHABLE | — | DownloadsCompletedListener and TorrentService register engine listeners. | `TorrentEngine.java:307-309`; `DownloadsCompletedListener.java:80-84`; `TorrentService.java:131-134` |
| `TorrentEngine.addTorrent(Uri)` | REACHABLE | — | TorrentEngine's watch-directory scan calls this overload for discovered torrent files. | `TorrentEngine.java:359-361,1140-1175` |
| `TorrentEngine.addTorrent(Uri,Uri)` | REACHABLE | — | CreateTorrentViewModel adds the created torrent with its selected save path. | `TorrentEngine.java:363-368`; `CreateTorrentViewModel.java:376` |
| `TorrentEngine.addTorrentCompletable(Uri)` | REACHABLE | — | The watch-directory scan calls this overload. | `TorrentEngine.java:370-372,1140-1150` |
| `TorrentEngine.addTorrentCompletable(Uri,Uri)` | REACHABLE | — | The public `addTorrent(Uri,Uri)` overload subscribes to it. | `TorrentEngine.java:363-368,374-394` |
| `TorrentEngine.addTorrentSync(Uri,TorrentMetaInfo,Uri)` | REACHABLE | — | The file-adding Completable parses the torrent and calls this helper. | `TorrentEngine.java:374-394,1177-1204` |
| `TorrentEngine.addTorrentSync(AddTorrentParams,boolean)` | REACHABLE | — | Asynchronous add and add-torrent UI paths invoke the session add helper. | `TorrentEngine.java:329-339,401-413`; `AddTorrentViewModel.java:510-529` |
| `TorrentEngine.addTorrents` | REACHABLE | — | FeedDownloaderWorker submits its collected AddTorrentParams list. | `TorrentEngine.java:342-357`; `FeedDownloaderWorker.java:192-211` |
| `TorrentEngine.addTrackers` | REACHABLE | — | DetailTorrentViewModel forwards tracker additions to the engine. | `TorrentEngine.java:568-575`; `DetailTorrentViewModel.java:353-354` |
| `TorrentEngine.cancelFetchMagnet` | REACHABLE | — | AddTorrentViewModel cancels the pending magnet fetch. | `TorrentEngine.java:481-486`; `AddTorrentViewModel.java:562-572` |
| `TorrentEngine.checkPauseTorrents` | REACHABLE | — | Called by rescheduling and torrent metadata handling to apply battery/network pause preferences. | `TorrentEngine.java:315-326,1023-1043,1442-1452` |
| `TorrentEngine.cleanTemp` | REACHABLE | — | `doStop()` invokes it during service shutdown. | `TorrentEngine.java:292-301,1223-1230`; `TorrentService.java:157-162` |
| `TorrentEngine.createFetchMagnetSingle` | REACHABLE | — | `fetchMagnet()` returns the Single from this helper after fetching a magnet. | `TorrentEngine.java:415-424,431-458`; `AddTorrentViewModel.java:230-243` |
| `TorrentEngine.deleteTorrents` | REACHABLE | — | Main and detail torrent ViewModels call it for user deletion. | `TorrentEngine.java:533-541`; `MainViewModel.java:142-143`; `DetailTorrentViewModel.java:362` |
| `TorrentEngine.deleteTrackers` | REACHABLE | — | DetailTorrentViewModel calls it for tracker removal. | `TorrentEngine.java:543-555`; `DetailTorrentViewModel.java:345-346` |
| `TorrentEngine.doStart` | REACHABLE | — | TorrentService's init path starts the engine. | `TorrentEngine.java:234-260`; `TorrentService.java:116-134` |
| `TorrentEngine.doStop` | REACHABLE | — | TorrentService.stopEngine invokes it during shutdown. | `TorrentEngine.java:292-301`; `TorrentService.java:150-162` |
| `TorrentEngine.fetchMagnet` | REACHABLE | — | AddTorrentViewModel calls it while resolving magnet metadata. | `TorrentEngine.java:415-424`; `AddTorrentViewModel.java:230-243` |
| `TorrentEngine.forceAnnounceTorrents` | REACHABLE | — | Main and detail torrent ViewModels invoke it from announce actions. | `TorrentEngine.java:520-531`; `MainViewModel.java:150-151`; `DetailTorrentViewModel.java:370` |
| `TorrentEngine.forceRecheckTorrents` | REACHABLE | — | Main and detail torrent ViewModels invoke it from recheck actions. | `TorrentEngine.java:507-518`; `MainViewModel.java:146-147`; `DetailTorrentViewModel.java:366` |
| `TorrentEngine.forceStop` | REACHABLE | — | UI, scheduled receiver, and engine auto-stop paths invoke it. | `TorrentEngine.java:143-145,275-286`; `MainViewModel.java:171`; `SchedulerReceiver.java:96` |
| `TorrentEngine.getBencode` | REACHABLE | — | DetailTorrentViewModel obtains a torrent's bencoded data through it. | `TorrentEngine.java:927-936`; `DetailTorrentViewModel.java:386` |

Count: 40 plan rows; 37 REACHABLE; 3 UNREACHABLE (`no_trigger_in_app`); 0 OPEN. No coverage evidence was used. These helper labels are source research only, not graph edits.
