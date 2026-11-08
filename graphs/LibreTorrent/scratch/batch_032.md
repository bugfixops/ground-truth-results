# LibreTorrent batch 32 source audit

Membership is the exact 40-row set in `scratch/batch_032_plan.txt`. I checked the target source and call-site/Parcel searches in `scratch/batch_032_helper_printed.txt`. The only conclusive no-trigger findings are the three Torrent Parcelable hooks: app intents pass Torrent IDs, and no source transfers a Torrent entity through a Parcel. Those three labels were added to graph_def.py. All other rows remain OPEN because their local callers do not establish complete hand-authored entry routes, or framework/session dispatch remains unresolved.

| # | Method | Label | Evidence / route note |
|---:|---|---|---|
| 1 | `Torrent.writeToParcel(Parcel,int)` | UNREACHABLE — `no_trigger_in_app` | App sends Torrent IDs, not Torrent Parcelables; `Torrent.java:142-170`; parcel/Intent search in helper evidence. |
| 2 | `Torrent$1.<init>()` | OPEN | Creator declared at `Torrent.java:157-170`; full class-init entry route not established. |
| 3 | `Torrent$1.createFromParcel(Parcel)` | UNREACHABLE — `no_trigger_in_app` | No app Parcel transport of Torrent; `Torrent.java:157-170`; focused parcel/Intent search. |
| 4 | `Torrent$1.newArray(int)` | UNREACHABLE — `no_trigger_in_app` | No app Parcel array transport; `Torrent.java:157-170`; focused parcel/Intent search. |
| 5 | `TorrentTagInfo.<init>(long,String)` | OPEN | Repository association construction at `TorrentRepositoryImpl.java:123-137`; app-entry route not recorded. |
| 6 | `TorrentTagInfo.equals(Object)` | OPEN | No hand-authored equality route established. |
| 7 | `TorrentTagInfo.hashCode()` | OPEN | No hand-authored hash route established. |
| 8 | `TorrentTagInfo.toString()` | OPEN | No hand-authored string conversion route established. |
| 9 | `BencodeFileItem.<clinit>()` | OPEN | Created during file-list conversion (`Utils.java:145`); complete app-entry route not recorded. |
| 10 | `BencodeFileItem.<init>(Parcel)` | OPEN | Parcel constructor/Creator (`BencodeFileItem.java:44-49,95-109`); framework dispatch unresolved. |
| 11 | `BencodeFileItem.<init>(String,int,long)` | OPEN | Called by `Utils.getFileList` (`Utils.java:145`); entry route unresolved. |
| 12 | `BencodeFileItem.compareTo(BencodeFileItem)` | OPEN | Definition at `BencodeFileItem.java:111-115`; comparator route not established. |
| 13 | `BencodeFileItem.describeContents()` | OPEN | Parcelable callback at `BencodeFileItem.java:81-85`; app transport route unresolved. |
| 14 | `BencodeFileItem.getIndex()` | OPEN | Definition at `BencodeFileItem.java:71-74`; entry route unresolved. |
| 15 | `BencodeFileItem.getPath()` | OPEN | Definition at `BencodeFileItem.java:51-54`; entry route unresolved. |
| 16 | `BencodeFileItem.getSize()` | OPEN | Definition at `BencodeFileItem.java:61-64`; entry route unresolved. |
| 17 | `BencodeFileItem.setIndex(int)` | OPEN | No hand-authored setter route established. |
| 18 | `BencodeFileItem.setPath(String)` | OPEN | No hand-authored setter route established. |
| 19 | `BencodeFileItem.setSize(long)` | OPEN | No hand-authored setter route established. |
| 20 | `BencodeFileItem.toString()` | OPEN | No hand-authored string conversion route established. |
| 21 | `BencodeFileItem.writeToParcel(Parcel,int)` | OPEN | Parcelable override (`BencodeFileItem.java:87-109`); complete app transport route not established. |
| 22 | `BencodeFileItem$1.<init>()` | OPEN | Creator declaration at `BencodeFileItem.java:95-109`; class-init route not established. |
| 23 | `BencodeFileItem$1.createFromParcel(Parcel)` | OPEN | Used by typed-list parcel reader (`TorrentMetaInfo.java:113-125`); parent Parcel transport route unresolved. |
| 24 | `BencodeFileItem$1.newArray(int)` | OPEN | Creator array callback (`BencodeFileItem.java:95-109`); framework dispatch unresolved. |
| 25 | `TorrentMetaInfo.<clinit>()` | OPEN | App source constructs TorrentMetaInfo (`TorrentEngine.java:379-384,461-464`); entry route not recorded. |
| 26 | `TorrentMetaInfo.<init>(Parcel)` | OPEN | Parcel constructor (`TorrentMetaInfo.java:113-163`); app transport route not established. |
| 27 | `TorrentMetaInfo.<init>(FileInputStream)` | OPEN | Engine/AddTorrentViewModel callers; full entry route not recorded. |
| 28 | `TorrentMetaInfo.<init>(String,String)` | OPEN | AddTorrentViewModel caller (`AddTorrentViewModel.java:237-242`); UI entry route not authored. |
| 29 | `TorrentMetaInfo.<init>(TorrentInfo)` | OPEN | Session download callers (`TorrentDownloadImpl.java:406,1186-1200`); callback/entry route unresolved. |
| 30 | `TorrentMetaInfo.<init>(byte[])` | OPEN | Engine emitter helper caller (`TorrentEngine.java:461-464`); full route not recorded. |
| 31 | `TorrentMetaInfo.describeContents()` | OPEN | Parcelable callback (`TorrentMetaInfo.java:128-132`); dispatch unresolved. |
| 32 | `TorrentMetaInfo.equals(Object)` | OPEN | No hand-authored equality route established. |
| 33 | `TorrentMetaInfo.getMetaInfo(TorrentInfo)` | OPEN | Called from constructors (`TorrentMetaInfo.java:63-111`); constructor entry routes unresolved. |
| 34 | `TorrentMetaInfo.hashCode()` | OPEN | No hand-authored hash route established. |
| 35 | `TorrentMetaInfo.toString()` | OPEN | No hand-authored string conversion route established. |
| 36 | `TorrentMetaInfo.writeToParcel(Parcel,int)` | OPEN | Parcelable override (`TorrentMetaInfo.java:134-163`); app transport route unresolved. |
| 37 | `TorrentMetaInfo$1.<init>()` | OPEN | Creator declaration at `TorrentMetaInfo.java:149-163`; full class-init route not recorded. |
| 38 | `TorrentMetaInfo$1.createFromParcel(Parcel)` | OPEN | Creator callback (`TorrentMetaInfo.java:149-163`); framework dispatch unresolved. |
| 39 | `TorrentMetaInfo$1.newArray(int)` | OPEN | Creator callback (`TorrentMetaInfo.java:149-163`); framework dispatch unresolved. |
| 40 | `BencodeFileTree.<init>(int,String,long,int,BencodeFileTree)` | OPEN | Constructed by BencodeFileTreeUtils (`BencodeFileTreeUtils.java:124-125`); UI entry route not recorded. |

Totals: 40 rows = 0 REACHABLE, 3 UNREACHABLE (`no_trigger_in_app`), 37 OPEN. Graph build after label edits: `scratch/build_19.txt` (0 errors, 230 warnings).
