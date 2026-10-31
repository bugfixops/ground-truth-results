# LibreTorrent batch 28 helper audit

Membership is taken only from `handoff/LIBRETORRENT_BATCH_PLAN.tsv`; it contains exactly 40 batch 28 rows. Printed plan rows, provider listener implementations, data classes, and call-site searches are in `scratch/batch_028_helper_printed.txt`.

Provider listener instances and callbacks remain OPEN because construction is inside Rx source callbacks and later invocation depends on session events. Parcelable construction paths are REACHABLE where app code directly constructs an object; parcel callback methods remain OPEN because this pass did not find app code passing these specific types through a Parcel.

| # | Method | Finding | Evidence / route note |
|---:|---|---|---|
| 1 | `TorrentInfoProvider$1.<init>(TorrentInfoProvider,Consumer,FlowableEmitter,String)` | OPEN | Listener is created inside `makeInfoFlowable`'s `Flowable.create` source (`TorrentInfoProvider.java:130-235`); Rx source dispatch is unverified. |
| 2 | `TorrentInfoProvider$1.onRestoreSessionError(String)` | OPEN | Callback invokes the captured event consumer (`TorrentInfoProvider.java:147-181`); invocation depends on session restore error delivery. |
| 3 | `TorrentInfoProvider$1.onSessionStats(SessionStats)` | OPEN | Callback invokes the captured event consumer (`TorrentInfoProvider.java:194-203`); session stats event delivery not established. |
| 4 | `TorrentInfoProvider$1.onTorrentError(String,Exception)` | OPEN | Callback invokes the captured event consumer (`TorrentInfoProvider.java:183-192`); session error event delivery not established. |
| 5 | `TorrentInfoProvider$1.onTorrentPaused(String)` | OPEN | Callback invokes the captured event consumer (`TorrentInfoProvider.java:161-170`); pause event delivery not established. |
| 6 | `TorrentInfoProvider$1.onTorrentStateChanged(String,TorrentStateCode,TorrentStateCode)` | OPEN | Callback invokes the captured event consumer (`TorrentInfoProvider.java:147-159`); session state event delivery not established. |
| 7 | `TorrentInfoProvider$2.<init>(TorrentInfoProvider,Runnable)` | OPEN | Listener is created inside `makeInfoListFlowable`'s Rx source (`TorrentInfoProvider.java:238-308`). |
| 8 | `TorrentInfoProvider$2.onRestoreSessionError(String)` | OPEN | Calls the captured info refresh runnable (`TorrentInfoProvider.java:253-285`); session restore error delivery unresolved. |
| 9 | `TorrentInfoProvider$2.onSessionStats(SessionStats)` | OPEN | Calls the captured info refresh runnable (`TorrentInfoProvider.java:281-284`); session stats event delivery unresolved. |
| 10 | `TorrentInfoProvider$2.onTorrentError(String,Exception)` | OPEN | Calls the captured info refresh runnable (`TorrentInfoProvider.java:276-279`); session error delivery unresolved. |
| 11 | `TorrentInfoProvider$2.onTorrentPaused(String)` | OPEN | Calls the captured info refresh runnable (`TorrentInfoProvider.java:261-264`); pause event delivery unresolved. |
| 12 | `TorrentInfoProvider$2.onTorrentRemoved(String)` | OPEN | Calls the captured info refresh runnable (`TorrentInfoProvider.java:266-269`); removal event delivery unresolved. |
| 13 | `TorrentInfoProvider$2.onTorrentStateChanged(String,TorrentStateCode,TorrentStateCode)` | OPEN | Calls the captured info refresh runnable (`TorrentInfoProvider.java:253-259`); state event delivery unresolved. |
| 14 | `TorrentInfoProvider$3.<init>(TorrentInfoProvider,FlowableEmitter)` | OPEN | Removal listener is created inside `makeTorrentsDeletedFlowable`'s Rx source (`TorrentInfoProvider.java:455-471`). |
| 15 | `TorrentInfoProvider$3.onTorrentRemoved(String)` | OPEN | Emits a deleted id in the listener (`TorrentInfoProvider.java:457-463`); session event dispatch remains open. |
| 16 | `TorrentInfoProvider$4.<init>(TorrentInfoProvider,AtomicReference,FlowableEmitter)` | OPEN | Stats listener is created inside `makeSessionStatsFlowable`'s Rx source (`TorrentInfoProvider.java:474-496`). |
| 17 | `TorrentInfoProvider$4.onSessionStats(SessionStats)` | OPEN | Emits changed stats in the listener (`TorrentInfoProvider.java:478-488`); session stats event dispatch remains open. |
| 18 | `AbstractInfoParcel.<init>()` | OPEN | Implicit base constructor is called by `AdvancedTorrentInfo()` (`AdvancedTorrentInfo.java:49-52`); no app source call to the no-argument subclass constructor was found. |
| 19 | `AbstractInfoParcel.<init>(Parcel)` | OPEN | Called only by `AdvancedTorrentInfo(Parcel)` in the source (`AdvancedTorrentInfo.java:76-79`); Parcel construction path for this type was not found. |
| 20 | `AbstractInfoParcel.<init>(String)` | REACHABLE | Called by `AdvancedTorrentInfo`'s populated constructor (`AdvancedTorrentInfo.java:54-74`); app engine creates that object (`TorrentEngine.java:846-855`). |
| 21 | `AbstractInfoParcel.writeToParcel(Parcel,int)` | OPEN | Base parcel writer is called by `AdvancedTorrentInfo.writeToParcel` (`AdvancedTorrentInfo.java:101-116`); no app Parcel use for this type was found. |
| 22 | `AdvancedTorrentInfo.<clinit>()` | REACHABLE | The engine creates `AdvancedTorrentInfo` (`TorrentEngine.java:846-855`), which initializes the class and its static `CREATOR` field (`AdvancedTorrentInfo.java:119-133`). |
| 23 | `AdvancedTorrentInfo.<init>(Parcel)` | OPEN | Called by its `CREATOR.createFromParcel` implementation (`AdvancedTorrentInfo.java:119-127`); no app parceling route for this type was found. |
| 24 | `AdvancedTorrentInfo.<init>(String,long[],int,int,int,double,long,long,double,double[],int,int)` | REACHABLE | `TorrentEngine.makeAdvancedInfoSync` directly constructs it (`TorrentEngine.java:846-855`); detail UI consumes the resulting information. |
| 25 | `AdvancedTorrentInfo.compareTo(Object)` | OPEN | Source implementation is printed, but no app call site or comparator use for this type was found. |
| 26 | `AdvancedTorrentInfo.describeContents()` | OPEN | Parcelable method implementation is printed; no app parceling route for this type was found. |
| 27 | `AdvancedTorrentInfo.equals(Object)` | OPEN | The provider compares advanced-info snapshots (`TorrentInfoProvider.java:327-335`), but that call is inside an Rx timer callback whose execution is unresolved. |
| 28 | `AdvancedTorrentInfo.hashCode()` | OPEN | No app call site was found; implementation alone does not prove a route. |
| 29 | `AdvancedTorrentInfo.toString()` | OPEN | No app call site was found; implementation alone does not prove a route. |
| 30 | `AdvancedTorrentInfo.writeToParcel(Parcel,int)` | OPEN | Parcelable implementation is printed; no app source passes this value through a Parcel. |
| 31 | `AdvancedTorrentInfo$1.<init>()` | REACHABLE | Anonymous `Parcelable.Creator` is created in the class's static initializer (`AdvancedTorrentInfo.java:119-133`), which runs when the engine constructs this type. |
| 32 | `AdvancedTorrentInfo$1.createFromParcel(Parcel)` | OPEN | Parcelable Creator callback (`AdvancedTorrentInfo.java:119-128`); no app Parcel route for `AdvancedTorrentInfo` was found. |
| 33 | `AdvancedTorrentInfo$1.newArray(int)` | OPEN | Parcelable Creator callback (`AdvancedTorrentInfo.java:129-133`); no app Parcel route for `AdvancedTorrentInfo` was found. |
| 34 | `MagnetInfo.<clinit>()` | REACHABLE | Session code constructs `MagnetInfo` (`TorrentSessionImpl.java:439-451`), initializing the class and its static `CREATOR` field (`MagnetInfo.java:79-93`). |
| 35 | `MagnetInfo.<init>(Parcel)` | OPEN | Called by `MagnetInfo.CREATOR.createFromParcel` (`MagnetInfo.java:79-87`); no app Parcel route for this type was found. |
| 36 | `MagnetInfo.<init>(String,String,String,List)` | REACHABLE | `TorrentSessionImpl` directly creates it while parsing magnet information (`TorrentSessionImpl.java:439-451`); AddTorrent UI consumes the result (`AddTorrentViewModel.java:237-246`). |
| 37 | `MagnetInfo.describeContents()` | OPEN | Parcelable method implementation is printed; no app parceling route for this type was found. |
| 38 | `MagnetInfo.getFilePriorities()` | REACHABLE | AddTorrent ViewModel reads it from parsed magnet info (`AddTorrentViewModel.java:245-246`). |
| 39 | `MagnetInfo.getName()` | REACHABLE | AddTorrent ViewModel reads it while preparing torrent metadata (`AddTorrentViewModel.java:242`). |
| 40 | `MagnetInfo.getSha1hash()` | REACHABLE | AddTorrent ViewModel reads it while preparing torrent metadata (`AddTorrentViewModel.java:242`). |

Totals: 40 rows = 9 REACHABLE, 0 UNREACHABLE, 31 OPEN. No graph, notes, output, or coverage files were changed.
