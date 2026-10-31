# LibreTorrent batch 30 source audit

Membership is the exact 40-row set in `scratch/batch_030_plan.txt`. I checked the helper's printed target source and caller searches in `scratch/batch_030_helper_printed.txt`.

The helper found 15 local construction/call chains. They include engine-created TorrentInfo objects, enum use, TrackerInfo conversion helpers, Creator initialization, and FeedChannel construction. These source paths do not yet form a full entry-to-method route made of hand-authored edges in graph_def.py, so those methods remain OPEN. Parcelable methods have no established app Parcel transport; FastResume construction depends on an unresolved session/native callback. No method is labeled from generated candidates or coverage.

| # | Method | Label | Evidence / route note |
|---:|---|---|---|
| 1 | `TorrentInfo.<clinit>()` | OPEN | Engine creates TorrentInfo (`TorrentEngine.java:776-801`); full entry route not authored. |
| 2 | `TorrentInfo.<init>(Parcel)` | OPEN | Only source caller is its Creator (`TorrentInfo.java:173-183`); app Parcel route not established. |
| 3 | `TorrentInfo.<init>(String,String,long,String,List)` | OPEN | `TorrentEngine.makeInfo` constructs it (`TorrentEngine.java:776-785`); entry route not authored. |
| 4 | `TorrentInfo.<init>(String,String,TorrentStateCode,int,long,long,long,long,long,long,long,int,int,String,boolean,Priority[],List,boolean)` | OPEN | `TorrentEngine.makeInfo` constructs it (`TorrentEngine.java:787-801`); entry route not authored. |
| 5 | `TorrentInfo.compareTo(Object)` | OPEN | Implementation at `TorrentInfo.java:185-188`; no typed sort/caller route established. |
| 6 | `TorrentInfo.describeContents()` | OPEN | Parcelable method (`TorrentInfo.java:145-147`); no app Parcel path established. |
| 7 | `TorrentInfo.equals(Object)` | OPEN | Provider compares list snapshots (`TorrentInfoProvider.java:242-250`); asynchronous/Rx dispatch route unresolved. |
| 8 | `TorrentInfo.hashCode()` | OPEN | No app call route established. |
| 9 | `TorrentInfo.toString()` | OPEN | No app call route established. |
| 10 | `TorrentInfo.writeToParcel(Parcel,int)` | OPEN | Parcelable implementation; no app Parcel path established. |
| 11 | `TorrentInfo$1.<init>()` | OPEN | Creator object initialized by TorrentInfo's static field (`TorrentInfo.java:173-183`); class-use entry route not authored. |
| 12 | `TorrentInfo$1.createFromParcel(Parcel)` | OPEN | Creator callback (`TorrentInfo.java:173-178`); no app Parcel path established. |
| 13 | `TorrentInfo$1.newArray(int)` | OPEN | Creator callback (`TorrentInfo.java:179-182`); no app Parcel path established. |
| 14 | `TorrentStateCode.<clinit>()` | OPEN | Enum is referenced in engine/UI/session code; full app-entry route not authored. |
| 15 | `TorrentStateCode.<init>(String,int,int)` | OPEN | Enum initialization at `TorrentStateCode.java:26-66`; entry route not authored. |
| 16 | `TorrentStateCode.fromValue(int)` | OPEN | Only source caller is `TorrentInfo(Parcel)` (`TorrentInfo.java:120-127`); Parcel route unresolved. |
| 17 | `TorrentStateCode.value()` | OPEN | Source caller is `TorrentInfo.writeToParcel` (`TorrentInfo.java:150-171`); Parcel route unresolved. |
| 18 | `TrackerInfo.<clinit>()` | OPEN | `TorrentDownloadImpl` constructs TrackerInfo (`:900-910`); complete entry route not authored. |
| 19 | `TrackerInfo.<init>(Parcel)` | OPEN | Creator-only source caller (`TrackerInfo.java:193-204`); app Parcel route unresolved. |
| 20 | `TrackerInfo.<init>(String,String,int,int)` | OPEN | Constructor at `TrackerInfo.java:79-86`; no source call site found. |
| 21 | `TrackerInfo.<init>(AnnounceEntry)` | OPEN | Constructed from announce entries (`TorrentDownloadImpl.java:900-910`); complete session entry route not authored. |
| 22 | `TrackerInfo.calcStatusCount(AnnounceEntry,AnnounceInfohash,Map)` | OPEN | Called by tracker status logic (`TrackerInfo.java:88-99,147-155`); outer entry route unresolved. |
| 23 | `TrackerInfo.compareTo(Object)` | OPEN | Implementation at `TrackerInfo.java:207-210`; no typed comparator route established. |
| 24 | `TrackerInfo.describeContents()` | OPEN | Parcelable method (`TrackerInfo.java:178-181`); no app Parcel path established. |
| 25 | `TrackerInfo.equals(Object)` | OPEN | Provider compares tracker snapshots (`TorrentInfoProvider.java:361-370`); timer/Rx dispatch route unresolved. |
| 26 | `TrackerInfo.getMessageAndStatus(AnnounceEntry,List)` | OPEN | Called by `TrackerInfo(AnnounceEntry)` (`TrackerInfo.java:67-77`); complete constructor entry route unresolved. |
| 27 | `TrackerInfo.hashCode()` | OPEN | No app call route established. |
| 28 | `TrackerInfo.infoHashStatus(AnnounceEntry,AnnounceInfohash)` | OPEN | Called through status helpers (`TrackerInfo.java:147-166`); complete entry route unresolved. |
| 29 | `TrackerInfo.toString()` | OPEN | No app call route established. |
| 30 | `TrackerInfo.writeToParcel(Parcel,int)` | OPEN | Parcelable implementation (`TrackerInfo.java:183-191`); no app Parcel path established. |
| 31 | `TrackerInfo$1.<init>()` | OPEN | Creator initialized in static field (`TrackerInfo.java:193-204`); full class-use entry route not authored. |
| 32 | `TrackerInfo$1.createFromParcel(Parcel)` | OPEN | Creator callback (`TrackerInfo.java:193-199`); app Parcel route unresolved. |
| 33 | `TrackerInfo$1.newArray(int)` | OPEN | Creator callback (`TrackerInfo.java:200-203`); app Parcel route unresolved. |
| 34 | `TrackerInfo$Result.<init>(TrackerInfo,int,String)` | OPEN | Constructed by `getMessageAndStatus` (`TrackerInfo.java:88-145`); complete outer route unresolved. |
| 35 | `FastResume.<init>(String,byte[])` | OPEN | Created during resume-data handling (`TorrentDownloadImpl.java:508-521`); session/native callback route unresolved. |
| 36 | `FeedChannel.<clinit>()` | OPEN | AddFeedViewModel constructs FeedChannel (`AddFeedViewModel.java:173-180`); app-entry route not authored. |
| 37 | `FeedChannel.<init>(Parcel)` | OPEN | Creator-only caller (`FeedChannel.java:104-118`); app Parcel path not established. |
| 38 | `FeedChannel.<init>(String,String,long,boolean,String,boolean,String)` | OPEN | AddFeedViewModel constructs it (`AddFeedViewModel.java:165-185`); entry route not authored. |
| 39 | `FeedChannel.describeContents()` | OPEN | Parcelable implementation (`FeedChannel.java:94-97`); no app Parcel path established. |
| 40 | `FeedChannel.equals(Object)` | OPEN | Implementation at `FeedChannel.java:126-130`; no caller route established. |

Totals: 40 rows = 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. No graph labels changed, so no graph build was run for this batch.
