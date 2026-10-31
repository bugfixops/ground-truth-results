# LibreTorrent batch 29 source audit

Membership is the exact 40-row set in `scratch/batch_029_plan.txt`. I independently printed and searched the target source and focused call sites in `scratch/batch_029_integrator_printed.txt`, then compared those findings with `scratch/batch_029_helper_printed.txt` and the helper report.

I accepted the three source-supported `no_trigger_in_app` recommendations for MagnetInfo's parcel hooks: the app constructs/uses MagnetInfo in memory and no app source transfers it through a Parcel. The anonymous Creator constructor is locally reached by class initialization, but remains OPEN because the full app-entry route is not represented by hand-authored edges. Other source-local method calls likewise remain OPEN unless the route is complete.

| # | Method | Label | Evidence / route note |
|---:|---|---|---|
| 1 | `MagnetInfo.getUri` | OPEN | Definition and focused usage search; full app-entry route not established. |
| 2 | `MagnetInfo.hashCode` | OPEN | No hand-authored call route established. |
| 3 | `MagnetInfo.toString` | OPEN | No hand-authored call route established. |
| 4 | `MagnetInfo.writeToParcel` | UNREACHABLE — `no_trigger_in_app` | No app source parcels MagnetInfo; implementation at `MagnetInfo.java:71-77`; Parcel/caller search in both printed files. |
| 5 | `MagnetInfo$1.<init>` | OPEN | Creator is initialized at `MagnetInfo.java:79-93`; app constructs MagnetInfo in `TorrentSessionImpl.java:427-452`, but the full entry route is not hand-authored. |
| 6 | `MagnetInfo$1.createFromParcel` | UNREACHABLE — `no_trigger_in_app` | No app Parcel transport reads MagnetInfo; callback implementation at `MagnetInfo.java:79-87`; focused Parcel search. |
| 7 | `MagnetInfo$1.newArray` | UNREACHABLE — `no_trigger_in_app` | No app Parcel transport requests a MagnetInfo Creator array; implementation at `MagnetInfo.java:79-93`; focused Parcel search. |
| 8 | `PeerInfo.<clinit>` | OPEN | Class is associated with `TorrentDownloadImpl.java:911-928` construction; complete hand-authored entry route absent. |
| 9 | `PeerInfo.<init>(Parcel)` | OPEN | Parcel constructor at `PeerInfo.java:92-106`; framework dispatch/app Parcel route not established. |
| 10 | `PeerInfo.<init>(String,String,long,long,double,int,int,int,int,int)` | OPEN | Constructor at `PeerInfo.java:72-90`; focused usage scan found no call site, but no final no-trigger decision made. |
| 11 | `PeerInfo.<init>(AdvancedPeerInfo,TorrentStatus)` | OPEN | Called while mapping session peers at `TorrentDownloadImpl.java:911-928`; complete app-entry route absent. |
| 12 | `PeerInfo.calcRelevance` | OPEN | Private helper called by PeerInfo constructor (`PeerInfo.java:56-70,122-141`); constructor entry route unresolved. |
| 13 | `PeerInfo.compareTo` | OPEN | `Collections.sort(list)` appears in `PeerListAdapter.java:80`; full entry route not authored. |
| 14 | `PeerInfo.describeContents` | OPEN | Parcelable callback at `PeerInfo.java:143-147`; app Parcel dispatch not established. |
| 15 | `PeerInfo.equals` | OPEN | Called by the peer-info update comparison in `TorrentInfoProvider.java:390-403`; full entry/callback route unresolved. |
| 16 | `PeerInfo.getConnectionType` | OPEN | Private helper called by constructor (`PeerInfo.java:56-70,108-120`); constructor entry route unresolved. |
| 17 | `PeerInfo.hashCode` | OPEN | No hand-authored call route established. |
| 18 | `PeerInfo.toString` | OPEN | No hand-authored call route established. |
| 19 | `PeerInfo.writeToParcel` | OPEN | Parcelable implementation at `PeerInfo.java:149-180`; app/framework dispatch route not established. |
| 20 | `PeerInfo$1.<init>` | OPEN | Static Creator initialization visible at `PeerInfo.java:166-180`; full class-use entry route not established. |
| 21 | `PeerInfo$1.createFromParcel` | OPEN | Creator callback at `PeerInfo.java:166-180`; Parcel dispatch route unresolved. |
| 22 | `PeerInfo$1.newArray` | OPEN | Creator callback at `PeerInfo.java:166-180`; Parcel dispatch route unresolved. |
| 23 | `Priority.<clinit>` | OPEN | Converter and FilePriority code use the enum, but complete entry route not authored. |
| 24 | `Priority.<init>(String,int,int)` | OPEN | Enum constants invoke the constructor (`Priority.java:22-63`); entry route not established. |
| 25 | `Priority.fromValue` | OPEN | Called by FilePriority; complete app-entry route not established. |
| 26 | `Priority.value` | OPEN | Called by PriorityConverter and FilePriority; complete app-entry route not established. |
| 27 | `ReadPieceInfo.<init>(int,int,long,Exception)` | OPEN | Called from `TorrentDownloadImpl.java:442-454`; entry depends on session read-piece callback. |
| 28 | `ReadPieceInfo.toString` | OPEN | No hand-authored call route established. |
| 29 | `SessionStats.<clinit>` | OPEN | Stats object constructed in `TorrentSessionImpl.java:1168-1181`; full entry route not authored. |
| 30 | `SessionStats.<init>(long,long,long,long,long,int)` | OPEN | Constructed by session stats handler (`TorrentSessionImpl.java:1168-1181`); callback-entry route unresolved. |
| 31 | `SessionStats.<init>(Parcel)` | OPEN | Parcel constructor/Creator at `SessionStats.java:48-93`; app Parcel route not established. |
| 32 | `SessionStats.compareTo` | OPEN | No comparator call route established. |
| 33 | `SessionStats.describeContents` | OPEN | Parcelable callback at `SessionStats.java:60-64`; app Parcel route not established. |
| 34 | `SessionStats.equals` | OPEN | Called by provider stats flow (`TorrentInfoProvider.java:474-487`); full Rx/session entry route unresolved. |
| 35 | `SessionStats.hashCode` | OPEN | No hand-authored call route established. |
| 36 | `SessionStats.toString` | OPEN | No hand-authored call route established. |
| 37 | `SessionStats.writeToParcel` | OPEN | Parcelable implementation at `SessionStats.java:66-93`; app Parcel route not established. |
| 38 | `SessionStats$1.<init>` | OPEN | Creator construction at `SessionStats.java:79-93`; complete class-init route not authored. |
| 39 | `SessionStats$1.createFromParcel` | OPEN | Creator callback at `SessionStats.java:79-93`; Parcel dispatch route unresolved. |
| 40 | `SessionStats$1.newArray` | OPEN | Creator callback at `SessionStats.java:79-93`; Parcel dispatch route unresolved. |

Totals: 40 rows = 0 REACHABLE, 3 UNREACHABLE (`no_trigger_in_app`), 37 OPEN. The three no-trigger labels were added to `graph_def.py`; the saved graph build is `scratch/build_18.txt`.
