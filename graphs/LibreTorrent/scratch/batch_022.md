# Batch 22 source audit

Membership is the exact 40 rows in `batch_022_plan.txt`; printed source excerpts and caller searches are in `batch_022_helper_printed.txt`, with independent Parcel search in `batch_022_independent_printed.txt`.

The helper found 37 source-local routes through TorrentService, view models, workers, and engine calls. I kept those OPEN because graph_def.py does not yet contain complete hand-written entry routes. Three AddTorrentParams parcel transport methods have no in-scope app route and are UNREACHABLE `no_trigger_in_app`.

| Method | Label | Evidence / reason |
|---|---|---|
| `AddTorrentParams.writeToParcel` | UNREACHABLE | no_trigger_in_app; no app Parcel transport. `AddTorrentParams.java:90-107`; independent Parcel search. |
| `AddTorrentParams$1.<init>` | OPEN | Static CREATOR initialization route exists; no hand entry route. `AddTorrentParams.java:34,109-119`. |
| `AddTorrentParams$1.createFromParcel` | UNREACHABLE | no_trigger_in_app; no app Parcel transport. `AddTorrentParams.java:109-113`; independent Parcel search. |
| `AddTorrentParams$1.newArray` | UNREACHABLE | no_trigger_in_app; no app Parcel path invokes array factory. `AddTorrentParams.java:109,116-118`. |
| `DownloadsCompletedListener.<init>` | OPEN | Constructed by TorrentEngine; full engine entry route not handwritten. `TorrentEngine.java:128-139`; listener `40-43`. |
| `DownloadsCompletedListener.lambda$listen$0` | OPEN | Listener completion/removal callback path; full route not handwritten. `DownloadsCompletedListener.java:45-84`; `TorrentEngine.java:234-251`. |
| `DownloadsCompletedListener.lambda$listen$1` | OPEN | Registered listener/action path; full route not handwritten. `DownloadsCompletedListener.java:47-78`; `TorrentEngine.java:243-251,307-309`. |
| `DownloadsCompletedListener.lambda$listen$2` | OPEN | Disposal action; full engine/service route not handwritten. `DownloadsCompletedListener.java:80-84`; `TorrentEngine.java:292-300`; `TorrentService.java:157-168`. |
| `DownloadsCompletedListener.listen` | OPEN | Subscribed in engine startup; service entry path not handwritten. `DownloadsCompletedListener.java:45-85`; `TorrentEngine.java:234-251`. |
| `DownloadsCompletedListener$1.<init>` | OPEN | Constructed in listen; full entry route not handwritten. `DownloadsCompletedListener.java:55-78`. |
| `DownloadsCompletedListener$1.onTorrentFinished` | OPEN | Listener callback forwarded by download/engine; complete listener route not handwritten. `DownloadsCompletedListener.java:55-70,80-84`; `TorrentDownloadImpl.java:483`; `TorrentEngine.java:307-309`. |
| `DownloadsCompletedListener$1.onTorrentRemoved` | OPEN | Listener callback forwarded by session; complete listener route not handwritten. `DownloadsCompletedListener.java:55,72-77,80-84`; `TorrentSessionImpl.java:389`. |
| `DownloadsCompletedListener$1.onTorrentStateChanged` | OPEN | Listener callback forwarded by download; complete listener route not handwritten. `DownloadsCompletedListener.java:55-64,80-84`; `TorrentDownloadImpl.java:227`. |
| `SessionErrorFilter.<clinit>` | OPEN | Created in TorrentEngine field initialization; full engine route not handwritten. `TorrentEngine.java:113,128-139`; `SessionErrorFilter.java:24-28`. |
| `SessionErrorFilter.<init>` | OPEN | Engine field initialization constructs it; full route not handwritten. `TorrentEngine.java:113,128-139`; `SessionErrorFilter.java:30-32`. |
| `SessionErrorFilter.skip(String)` | OPEN | Called from engine error listener; external session callback route not handwritten. `TorrentEngine.java:1384-1390`; `SessionErrorFilter.java:30-32`. |
| `TorrentEngine.<clinit>` | OPEN | Singleton getter invoked by service; complete service path not handwritten. `TorrentEngine.java:96-97,115-125`; `TorrentService.java:108-110`. |
| `TorrentEngine.<init>(Context)` | OPEN | Singleton constructor route exists; complete service path not handwritten. `TorrentEngine.java:117-141`. |
| `TorrentEngine.addListener(TorrentEngineListener)` | OPEN | Service and listener register; complete service route not handwritten. `TorrentEngine.java:307-309`; `TorrentService.java:131-134`. |
| `TorrentEngine.addTorrent(Uri)` | OPEN | Watch-directory and UI paths exist; full engine entry route not handwritten. `TorrentEngine.java:359-361,1140-1175`. |
| `TorrentEngine.addTorrent(Uri,Uri)` | OPEN | CreateTorrentViewModel calls it; complete UI route not handwritten. `TorrentEngine.java:363-368`; `CreateTorrentViewModel.java:376`. |
| `TorrentEngine.addTorrentCompletable(Uri)` | OPEN | Watch-directory path calls it; full route not handwritten. `TorrentEngine.java:370-372,1140-1150`. |
| `TorrentEngine.addTorrentCompletable(Uri,Uri)` | OPEN | Called from addTorrent overload; full route not handwritten. `TorrentEngine.java:363-368,374-394`. |
| `TorrentEngine.addTorrentSync(Uri,TorrentMetaInfo,Uri)` | OPEN | Internal add path exists; full route not handwritten. `TorrentEngine.java:374-394,1177-1204`. |
| `TorrentEngine.addTorrentSync(AddTorrentParams,boolean)` | OPEN | App paths invoke it; full engine/UI route not handwritten. `TorrentEngine.java:329-339,401-413`; `AddTorrentViewModel.java:510-529`. |
| `TorrentEngine.addTorrents(List,boolean)` | OPEN | FeedDownloaderWorker submits params; complete worker route not handwritten. `TorrentEngine.java:342-357`; `FeedDownloaderWorker.java:192-211`. |
| `TorrentEngine.addTrackers(String,List)` | OPEN | DetailTorrentViewModel forwards to engine; UI route not handwritten. `TorrentEngine.java:568-575`; `DetailTorrentViewModel.java:353-354`. |
| `TorrentEngine.cancelFetchMagnet(String)` | OPEN | AddTorrentViewModel invokes it; full UI route not handwritten. `TorrentEngine.java:481-486`; `AddTorrentViewModel.java:562-572`. |
| `TorrentEngine.checkPauseTorrents` | OPEN | Called in rescheduling and metadata paths; complete service/session route not handwritten. `TorrentEngine.java:315-326,1023-1043,1442-1452`. |
| `TorrentEngine.cleanTemp` | OPEN | Called by doStop; complete service shutdown route not handwritten. `TorrentEngine.java:292-301,1223-1230`; `TorrentService.java:157-162`. |
| `TorrentEngine.createFetchMagnetSingle(String)` | OPEN | Called from fetchMagnet; full UI route not handwritten. `TorrentEngine.java:415-424,431-458`; `AddTorrentViewModel.java:230-243`. |
| `TorrentEngine.deleteTorrents(List,boolean)` | OPEN | Main/detail ViewModels call it; full UI route not handwritten. `TorrentEngine.java:533-541`; helper call sites. |
| `TorrentEngine.deleteTrackers(String,List)` | OPEN | Detail ViewModel calls it; full UI route not handwritten. `TorrentEngine.java:543-555`; `DetailTorrentViewModel.java:345-346`. |
| `TorrentEngine.doStart` | OPEN | TorrentService init path calls it; complete service entry route not handwritten. `TorrentEngine.java:234-260`; `TorrentService.java:116-134`. |
| `TorrentEngine.doStop` | OPEN | Service stop path calls it; complete service entry route not handwritten. `TorrentEngine.java:292-301`; `TorrentService.java:150-162`. |
| `TorrentEngine.fetchMagnet(String)` | OPEN | AddTorrentViewModel calls it; full UI route not handwritten. `TorrentEngine.java:415-424`; `AddTorrentViewModel.java:230-243`. |
| `TorrentEngine.forceAnnounceTorrents(List)` | OPEN | Main/detail ViewModels call it; full UI route not handwritten. `TorrentEngine.java:520-531`; helper call sites. |
| `TorrentEngine.forceRecheckTorrents(List)` | OPEN | Main/detail ViewModels call it; full UI route not handwritten. `TorrentEngine.java:507-518`; helper call sites. |
| `TorrentEngine.forceStop` | OPEN | UI/receiver/engine paths call it; complete entry routes not handwritten. `TorrentEngine.java:143-145,275-286`; `SchedulerReceiver.java:96`. |
| `TorrentEngine.getBencode(String)` | OPEN | DetailTorrentViewModel calls it; complete UI route not handwritten. `TorrentEngine.java:927-936`; `DetailTorrentViewModel.java:386`. |

Count: 40 plan rows; 0 REACHABLE; 3 `UNREACHABLE/no_trigger_in_app`; 37 OPEN. No coverage evidence was used.
