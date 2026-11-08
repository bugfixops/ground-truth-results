# LibreTorrent batch 28 source audit

Membership is the exact 40-row set in `scratch/batch_028_plan.txt`. I checked the helper's corrected printed source/caller evidence in `scratch/batch_028_helper_printed.txt` against `TorrentInfoProvider`, `TorrentEngine`, `TorrentSessionImpl`, `AdvancedTorrentInfo`, `AbstractInfoParcel`, `MagnetInfo`, and AddTorrentViewModel sources.

The helper proposed nine REACHABLE methods based on local calls (constructors, class initialization, and `MagnetInfo` getters among them). These local calls do not establish the required entry-to-method route through hand-authored edges, so they remain OPEN. Provider listener constructors/callbacks depend on Rx subscription or session events. Parcelable constructors and callbacks lack an app-source parcel route. The remaining model methods have no established call route. No method is labeled from generator candidates or coverage.

| # | Method | Label | Evidence / route note |
|---:|---|---|---|
| 1 | `TorrentInfoProvider$1.<init>(TorrentInfoProvider,Consumer,FlowableEmitter,String)` | OPEN | Listener is created inside `makeInfoFlowable`'s Flowable source (`TorrentInfoProvider.java:130-235`); Rx source dispatch unresolved. |
| 2 | `TorrentInfoProvider$1.onRestoreSessionError(String)` | OPEN | Calls captured event consumer (`TorrentInfoProvider.java:147-181`); session error delivery unresolved. |
| 3 | `TorrentInfoProvider$1.onSessionStats(SessionStats)` | OPEN | Calls captured event consumer (`TorrentInfoProvider.java:194-203`); session stats delivery unresolved. |
| 4 | `TorrentInfoProvider$1.onTorrentError(String,Exception)` | OPEN | Calls captured event consumer (`TorrentInfoProvider.java:183-192`); session error delivery unresolved. |
| 5 | `TorrentInfoProvider$1.onTorrentPaused(String)` | OPEN | Calls captured event consumer (`TorrentInfoProvider.java:161-170`); pause delivery unresolved. |
| 6 | `TorrentInfoProvider$1.onTorrentStateChanged(String,TorrentStateCode,TorrentStateCode)` | OPEN | Calls captured event consumer (`TorrentInfoProvider.java:147-159`); session state-event delivery unresolved. |
| 7 | `TorrentInfoProvider$2.<init>(TorrentInfoProvider,Runnable)` | OPEN | Listener is created inside `makeInfoListFlowable`'s Rx source (`TorrentInfoProvider.java:238-308`); source dispatch unresolved. |
| 8 | `TorrentInfoProvider$2.onRestoreSessionError(String)` | OPEN | Calls captured refresh runnable (`TorrentInfoProvider.java:253-285`); session restore-event delivery unresolved. |
| 9 | `TorrentInfoProvider$2.onSessionStats(SessionStats)` | OPEN | Calls refresh runnable (`TorrentInfoProvider.java:281-284`); event delivery unresolved. |
| 10 | `TorrentInfoProvider$2.onTorrentError(String,Exception)` | OPEN | Calls refresh runnable (`TorrentInfoProvider.java:276-279`); event delivery unresolved. |
| 11 | `TorrentInfoProvider$2.onTorrentPaused(String)` | OPEN | Calls refresh runnable (`TorrentInfoProvider.java:261-264`); event delivery unresolved. |
| 12 | `TorrentInfoProvider$2.onTorrentRemoved(String)` | OPEN | Calls refresh runnable (`TorrentInfoProvider.java:266-269`); event delivery unresolved. |
| 13 | `TorrentInfoProvider$2.onTorrentStateChanged(String,TorrentStateCode,TorrentStateCode)` | OPEN | Calls refresh runnable (`TorrentInfoProvider.java:253-259`); event delivery unresolved. |
| 14 | `TorrentInfoProvider$3.<init>(TorrentInfoProvider,FlowableEmitter)` | OPEN | Removal listener is created inside `makeTorrentsDeletedFlowable` (`TorrentInfoProvider.java:455-471`); Rx source dispatch unresolved. |
| 15 | `TorrentInfoProvider$3.onTorrentRemoved(String)` | OPEN | Emits deleted id (`TorrentInfoProvider.java:457-463`); session event dispatch unresolved. |
| 16 | `TorrentInfoProvider$4.<init>(TorrentInfoProvider,AtomicReference,FlowableEmitter)` | OPEN | Stats listener is created inside `makeSessionStatsFlowable` (`TorrentInfoProvider.java:474-496`); Rx source dispatch unresolved. |
| 17 | `TorrentInfoProvider$4.onSessionStats(SessionStats)` | OPEN | Emits changed stats (`TorrentInfoProvider.java:478-488`); session event dispatch unresolved. |
| 18 | `AbstractInfoParcel.<init>()` | OPEN | Implicit base call from `AdvancedTorrentInfo()` (`AdvancedTorrentInfo.java:49-52`); no app call to that no-argument subclass constructor was found. |
| 19 | `AbstractInfoParcel.<init>(Parcel)` | OPEN | Called only by `AdvancedTorrentInfo(Parcel)` (`AdvancedTorrentInfo.java:76-79`); app Parcel path not found. |
| 20 | `AbstractInfoParcel.<init>(String)` | OPEN | Called by populated `AdvancedTorrentInfo` constructor (`AdvancedTorrentInfo.java:54-74`); engine construction at `TorrentEngine.java:846-855` is local evidence, but app-entry route is not authored. |
| 21 | `AbstractInfoParcel.writeToParcel(Parcel,int)` | OPEN | Called by `AdvancedTorrentInfo.writeToParcel` (`AdvancedTorrentInfo.java:101-116`); app Parcel path not found. |
| 22 | `AdvancedTorrentInfo.<clinit>()` | OPEN | Engine creates `AdvancedTorrentInfo` (`TorrentEngine.java:846-855`) and class has static `CREATOR` (`AdvancedTorrentInfo.java:119-133`); entry route not authored. |
| 23 | `AdvancedTorrentInfo.<init>(Parcel)` | OPEN | Called by `CREATOR.createFromParcel` (`AdvancedTorrentInfo.java:119-127`); app Parcel path not found. |
| 24 | `AdvancedTorrentInfo.<init>(String,long[],int,int,int,double,long,long,double,double[],int,int)` | OPEN | Direct construction by `TorrentEngine.makeAdvancedInfoSync` (`TorrentEngine.java:846-855`) is local evidence; full app-entry route not authored. |
| 25 | `AdvancedTorrentInfo.compareTo(Object)` | OPEN | No app comparator call found; no triggering route established. |
| 26 | `AdvancedTorrentInfo.describeContents()` | OPEN | Parcelable method; app Parcel route not found. |
| 27 | `AdvancedTorrentInfo.equals(Object)` | OPEN | Provider snapshot comparison at `TorrentInfoProvider.java:327-335` is inside a timer/Rx callback whose dispatch is unresolved. |
| 28 | `AdvancedTorrentInfo.hashCode()` | OPEN | No app-source call found; no trigger established. |
| 29 | `AdvancedTorrentInfo.toString()` | OPEN | No app-source call found; no trigger established. |
| 30 | `AdvancedTorrentInfo.writeToParcel(Parcel,int)` | OPEN | Parcelable implementation exists; app source does not pass this value through a Parcel. |
| 31 | `AdvancedTorrentInfo$1.<init>()` | OPEN | Creator is constructed in the class static initializer (`AdvancedTorrentInfo.java:119-133`); entry route to class use not authored. |
| 32 | `AdvancedTorrentInfo$1.createFromParcel(Parcel)` | OPEN | Creator callback (`AdvancedTorrentInfo.java:119-128`); app Parcel route not found. |
| 33 | `AdvancedTorrentInfo$1.newArray(int)` | OPEN | Creator callback (`AdvancedTorrentInfo.java:129-133`); app Parcel route not found. |
| 34 | `MagnetInfo.<clinit>()` | OPEN | Session constructs `MagnetInfo` (`TorrentSessionImpl.java:439-451`) and class defines static `CREATOR` (`MagnetInfo.java:79-93`); app-entry route not authored. |
| 35 | `MagnetInfo.<init>(Parcel)` | OPEN | Called from `MagnetInfo.CREATOR.createFromParcel` (`MagnetInfo.java:79-87`); app Parcel route not found. |
| 36 | `MagnetInfo.<init>(String,String,String,List)` | OPEN | Session directly constructs it while parsing magnet data (`TorrentSessionImpl.java:439-451`); local construction route is not a complete app-entry path. |
| 37 | `MagnetInfo.describeContents()` | OPEN | Parcelable method; app Parcel route not found. |
| 38 | `MagnetInfo.getFilePriorities()` | OPEN | AddTorrentViewModel reads the result (`AddTorrentViewModel.java:245-246`); full entry route to that flow not authored. |
| 39 | `MagnetInfo.getName()` | OPEN | AddTorrentViewModel reads it (`AddTorrentViewModel.java:242`); full entry route to that flow not authored. |
| 40 | `MagnetInfo.getSha1hash()` | OPEN | AddTorrentViewModel reads it (`AddTorrentViewModel.java:242`); full entry route to that flow not authored. |

Totals: 40 rows = 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. No graph labels changed, so no graph build was run for this batch.
