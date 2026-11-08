# Batch 29 helper report

Membership is exactly the 40 rows with `batch==29` in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`; no other source was used for membership. The source excerpts and focused usage search are saved in `scratch/batch_029_helper_printed.txt`.

| Method | Label | Kind | Reason | Printed evidence |
|---|---|---|---|---|
| `MagnetInfo.getUri` | OPEN | — | Definition read; a complete app-entry-to-method route is not established in this audit. | `MagnetInfo.java:95-98`; usage search in printed file |
| `MagnetInfo.hashCode` | OPEN | — | No hand-written call route established. | `MagnetInfo.java:115-119`; usage search |
| `MagnetInfo.toString` | OPEN | — | No hand-written call route established. | `MagnetInfo.java:121-131`; usage search |
| `MagnetInfo.writeToParcel` | UNREACHABLE | no_trigger_in_app | Source search finds no app parcel transport of MagnetInfo; only its Parcelable implementation. | `MagnetInfo.java:33,71-93`; printed type and parcel search |
| `MagnetInfo$1.<init>` | REACHABLE | — | MagnetInfo static CREATOR initialization constructs the anonymous creator; app source constructs MagnetInfo in TorrentSessionImpl. | `MagnetInfo.java:79-93`; `TorrentSessionImpl.java:427-452` |
| `MagnetInfo$1.createFromParcel` | UNREACHABLE | no_trigger_in_app | No app parcel transport path for MagnetInfo is present in the printed source search. | `MagnetInfo.java:79-93`; printed parcel search |
| `MagnetInfo$1.newArray` | UNREACHABLE | no_trigger_in_app | No app parcel transport path for MagnetInfo is present in the printed source search. | `MagnetInfo.java:79-93`; printed parcel search |
| `PeerInfo.<clinit>` | OPEN | — | Type initialization is associated with construction, but a complete hand-written entry route is not established here. | `PeerInfo.java:36-70,166-180`; `TorrentDownloadImpl.java:911-928` |
| `PeerInfo.<init>(Parcel)` | OPEN | — | Parcel constructor read; whether framework parcel dispatch reaches it is not established. | `PeerInfo.java:92-106,166-180`; printed parcel search |
| `PeerInfo.<init>(String,String,long,long,double,int,int,int,int,int)` | OPEN | — | No call site for this constructor established in focused search; other constructor is used. | `PeerInfo.java:72-90`; printed construction search |
| `PeerInfo.<init>(AdvancedPeerInfo,TorrentStatus)` | OPEN | — | Directly called while mapping session peers, but complete entry route is not recorded here. | `PeerInfo.java:56-70`; `TorrentDownloadImpl.java:911-928` |
| `PeerInfo.calcRelevance` | OPEN | — | Constructor calls this private helper; complete entry route remains unestablished. | `PeerInfo.java:56-70,122-141` |
| `PeerInfo.compareTo` | OPEN | — | No comparator use route established. | `PeerInfo.java:182-186`; printed usage search |
| `PeerInfo.describeContents` | OPEN | — | Parcelable callback; app parcel dispatch route not established. | `PeerInfo.java:143-147`; printed parcel search |
| `PeerInfo.equals` | OPEN | — | Peer list comparison invokes equality in the info provider, but complete route is not established. | `PeerInfo.java:208-229`; `TorrentInfoProvider.java:390-403` |
| `PeerInfo.getConnectionType` | OPEN | — | Constructor calls this private helper; complete entry route remains unestablished. | `PeerInfo.java:56-70,108-120` |
| `PeerInfo.hashCode` | OPEN | — | No hand-written call route established. | `PeerInfo.java:188-206`; printed usage search |
| `PeerInfo.toString` | OPEN | — | No hand-written call route established. | `PeerInfo.java:231-247`; printed usage search |
| `PeerInfo.writeToParcel` | OPEN | — | Parcelable override, but framework dispatch and complete app entry route are not established. | `PeerInfo.java:149-180`; printed parcel search |
| `PeerInfo$1.<init>` | OPEN | — | Static CREATOR initialization is visible; class initialization route is not fully documented here. | `PeerInfo.java:166-180`; `PeerInfo.java:56-70` |
| `PeerInfo$1.createFromParcel` | OPEN | — | No parcel dispatch route established. | `PeerInfo.java:166-180`; printed parcel search |
| `PeerInfo$1.newArray` | OPEN | — | No parcel dispatch route established. | `PeerInfo.java:166-180`; printed parcel search |
| `Priority.<clinit>` | OPEN | — | Enum is used in converter code, but full app-entry route is not established. | `Priority.java:22-79`; printed PriorityConverter search |
| `Priority.<init>(String,int,int)` | OPEN | — | Enum constants initialize the enum constructor; app-entry route is not established. | `Priority.java:22-63` |
| `Priority.fromValue` | OPEN | — | Called from FilePriority; complete entry route not established. | `Priority.java:70-78`; printed usage search |
| `Priority.value` | OPEN | — | Called by PriorityConverter and FilePriority; complete entry route not established. | `Priority.java:63-68`; printed usage search |
| `ReadPieceInfo.<init>` | OPEN | — | Called by TorrentDownloadImpl's read-piece handler; complete callback-entry route is not established. | `ReadPieceInfo.java:24-37`; `TorrentDownloadImpl.java:442-454` |
| `ReadPieceInfo.toString` | OPEN | — | No hand-written call route established. | `ReadPieceInfo.java:39-49`; printed usage search |
| `SessionStats.<clinit>` | OPEN | — | Static CREATOR initializes with the class; complete entry route is not established. | `SessionStats.java:27-93`; `TorrentSessionImpl.java:1168-1181` |
| `SessionStats.<init>(long,long,long,long,long,int)` | OPEN | — | Constructed by session stats handler; complete entry route is not established. | `SessionStats.java:36-46`; `TorrentSessionImpl.java:1168-1181` |
| `SessionStats.<init>(Parcel)` | OPEN | — | Parcel constructor read; framework parcel dispatch route is not established. | `SessionStats.java:48-58,79-93`; printed parcel search |
| `SessionStats.compareTo` | OPEN | — | No comparator call route established. | `SessionStats.java:110-114`; printed usage search |
| `SessionStats.describeContents` | OPEN | — | Parcelable callback; app parcel dispatch route is not established. | `SessionStats.java:60-64`; printed parcel search |
| `SessionStats.equals` | OPEN | — | Called by TorrentInfoProvider's stats flow; full entry route is not established. | `SessionStats.java:117-133`; `TorrentInfoProvider.java:474-487` |
| `SessionStats.hashCode` | OPEN | — | No hand-written call route established. | `SessionStats.java:95-108`; printed usage search |
| `SessionStats.toString` | OPEN | — | No hand-written call route established. | `SessionStats.java:135-148`; printed usage search |
| `SessionStats.writeToParcel` | OPEN | — | Parcelable override, but framework dispatch and complete app entry route are not established. | `SessionStats.java:66-93`; printed parcel search |
| `SessionStats$1.<init>` | OPEN | — | Static CREATOR initialization is visible; complete class-init entry route is not established. | `SessionStats.java:79-93`; `TorrentSessionImpl.java:1168-1181` |
| `SessionStats$1.createFromParcel` | OPEN | — | No parcel dispatch route established. | `SessionStats.java:79-93`; printed parcel search |
| `SessionStats$1.newArray` | OPEN | — | No parcel dispatch route established. | `SessionStats.java:79-93`; printed parcel search |

Count: 40 plan rows; 1 REACHABLE; 3 UNREACHABLE (`no_trigger_in_app`); 36 OPEN. No coverage evidence was used. These helper labels are source research only, not graph edits.
