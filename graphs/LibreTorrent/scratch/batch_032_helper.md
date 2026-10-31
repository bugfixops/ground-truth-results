# Batch 32 helper report

Membership is exactly the 40 rows with `batch==32` in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`; the TSV is the sole membership source. Definitions and a bounded source-use search are recorded in `scratch/batch_032_helper_printed.txt`. I mark rows OPEN unless the source establishes an allowed label without assuming a missing entry route.

| Method | Label | Kind | Reason | Printed evidence |
|---|---|---|---|---|
| `Torrent.writeToParcel` | UNREACHABLE | no_trigger_in_app | App hand-written Intent uses pass torrent IDs; no source use transports Torrent as Parcelable. | `Torrent.java:142-170`; printed parcel and Intent search |
| `Torrent$1.<init>` | OPEN | — | CREATOR declaration is present, but class initialization path to this synthetic ctor is not traced from an entry. | `Torrent.java:157-170`; `TorrentSessionImpl.java:263` |
| `Torrent$1.createFromParcel` | UNREACHABLE | no_trigger_in_app | No app Parcelable transport of Torrent is established; only ID extras appear in the focused Intent search. | `Torrent.java:157-170`; printed parcel and Intent search |
| `Torrent$1.newArray` | UNREACHABLE | no_trigger_in_app | No app Parcelable array transport for Torrent is established. | `Torrent.java:157-170`; printed parcel and Intent search |
| `TorrentTagInfo.<init>` | OPEN | — | Repository constructs rows for tag associations, but complete app-entry route is not recorded here. | `TorrentTagInfo.java:48-60`; `TorrentRepositoryImpl.java:123-137` |
| `TorrentTagInfo.equals` | OPEN | — | No hand-written equality call route established. | `TorrentTagInfo.java:62-71`; usage search |
| `TorrentTagInfo.hashCode` | OPEN | — | No hand-written hash call route established. | `TorrentTagInfo.java:73-78`; usage search |
| `TorrentTagInfo.toString` | OPEN | — | No hand-written string conversion route established. | `TorrentTagInfo.java:80-87`; usage search |
| `BencodeFileItem.<clinit>` | OPEN | — | Item instances are constructed by file-list conversion, but full app-entry route is not recorded. | `BencodeFileItem.java:31-42`; `Utils.java:145` |
| `BencodeFileItem.<init>(Parcel)` | OPEN | — | Parcel constructor read; framework dispatch route is not established. | `BencodeFileItem.java:44-49,95-109`; printed parcel search |
| `BencodeFileItem.<init>(String,int,long)` | OPEN | — | Constructed by Utils.getFileList; complete entry route is not established. | `BencodeFileItem.java:37-42`; `Utils.java:145` |
| `BencodeFileItem.compareTo` | OPEN | — | No source comparator invocation established. | `BencodeFileItem.java:111-115`; usage search |
| `BencodeFileItem.describeContents` | OPEN | — | Parcelable callback; transport dispatch route not established. | `BencodeFileItem.java:81-85`; printed parcel search |
| `BencodeFileItem.getIndex` | OPEN | — | Definition read; complete entry route not established. | `BencodeFileItem.java:71-74`; usage search |
| `BencodeFileItem.getPath` | OPEN | — | Definition read; complete entry route not established. | `BencodeFileItem.java:51-54`; usage search |
| `BencodeFileItem.getSize` | OPEN | — | Definition read; complete entry route not established. | `BencodeFileItem.java:61-64`; usage search |
| `BencodeFileItem.setIndex` | OPEN | — | No hand-written setter call route established. | `BencodeFileItem.java:76-79`; usage search |
| `BencodeFileItem.setPath` | OPEN | — | No hand-written setter call route established. | `BencodeFileItem.java:56-59`; usage search |
| `BencodeFileItem.setSize` | OPEN | — | No hand-written setter call route established. | `BencodeFileItem.java:66-69`; usage search |
| `BencodeFileItem.toString` | OPEN | — | No hand-written string conversion route established. | `BencodeFileItem.java:117-126`; usage search |
| `BencodeFileItem.writeToParcel` | OPEN | — | Parcelable override, but no complete app transport route is established. | `BencodeFileItem.java:87-109`; printed parcel search |
| `BencodeFileItem$1.<init>` | OPEN | — | CREATOR declaration is read; complete class-init entry route is not established. | `BencodeFileItem.java:95-109`; `TorrentMetaInfo.java:113-163` |
| `BencodeFileItem$1.createFromParcel` | OPEN | — | Used by the typed-list parcel reader only; no parent parcel transport route is established. | `BencodeFileItem.java:95-109`; `TorrentMetaInfo.java:113-125` |
| `BencodeFileItem$1.newArray` | OPEN | — | No framework array dispatch route established. | `BencodeFileItem.java:95-109`; printed parcel search |
| `TorrentMetaInfo.<clinit>` | OPEN | — | App source constructs TorrentMetaInfo, but full entry route to class initialization is not recorded. | `TorrentMetaInfo.java:40-55`; `TorrentEngine.java:379-384,461-464` |
| `TorrentMetaInfo.<init>(Parcel)` | OPEN | — | Parcel constructor exists; no app Parcelable transport route established. | `TorrentMetaInfo.java:113-163`; printed parcel search |
| `TorrentMetaInfo.<init>(FileInputStream)` | OPEN | — | Called by engine and add-torrent view model paths; complete entry route not recorded. | `TorrentMetaInfo.java:83-96`; `TorrentEngine.java:379-384`; `AddTorrentViewModel.java:293` |
| `TorrentMetaInfo.<init>(String,String)` | OPEN | — | Constructed by AddTorrentViewModel; full UI entry route not recorded. | `TorrentMetaInfo.java:57-61`; `AddTorrentViewModel.java:237-242` |
| `TorrentMetaInfo.<init>(TorrentInfo)` | OPEN | — | Constructed by session download code; complete entry route not recorded. | `TorrentMetaInfo.java:73-81`; `TorrentDownloadImpl.java:406,1186-1200` |
| `TorrentMetaInfo.<init>(byte[])` | OPEN | — | Called in TorrentEngine's emitter helper; complete route is not recorded. | `TorrentMetaInfo.java:63-71`; `TorrentEngine.java:461-464` |
| `TorrentMetaInfo.describeContents` | OPEN | — | Parcelable callback; transport dispatch route is not established. | `TorrentMetaInfo.java:128-132`; printed parcel search |
| `TorrentMetaInfo.equals` | OPEN | — | No hand-written equality call route established. | `TorrentMetaInfo.java:171-191`; usage search |
| `TorrentMetaInfo.getMetaInfo` | OPEN | — | Constructors call this helper; complete app-entry route is not established. | `TorrentMetaInfo.java:63-111` |
| `TorrentMetaInfo.hashCode` | OPEN | — | No hand-written hash call route established. | `TorrentMetaInfo.java:165-169`; usage search |
| `TorrentMetaInfo.toString` | OPEN | — | No hand-written string conversion route established. | `TorrentMetaInfo.java:193-209`; usage search |
| `TorrentMetaInfo.writeToParcel` | OPEN | — | Parcelable override; no complete app transport route is established. | `TorrentMetaInfo.java:134-163`; printed parcel search |
| `TorrentMetaInfo$1.<init>` | OPEN | — | CREATOR declaration is visible; full class-init entry route not recorded. | `TorrentMetaInfo.java:149-163`; constructor call sites |
| `TorrentMetaInfo$1.createFromParcel` | OPEN | — | No framework parcel dispatch route established. | `TorrentMetaInfo.java:149-163`; printed parcel search |
| `TorrentMetaInfo$1.newArray` | OPEN | — | No framework parcel array dispatch route established. | `TorrentMetaInfo.java:149-163`; printed parcel search |
| `BencodeFileTree.<init>(int,String,long,int,BencodeFileTree)` | OPEN | — | Constructed by BencodeFileTreeUtils, but complete UI entry route is not recorded. | `BencodeFileTree.java:40-43`; `BencodeFileTreeUtils.java:124-125` |

Count: 40 plan rows; 0 REACHABLE; 3 UNREACHABLE (`no_trigger_in_app`); 37 OPEN. No coverage evidence was used. These helper labels are source research only, not graph edits.
