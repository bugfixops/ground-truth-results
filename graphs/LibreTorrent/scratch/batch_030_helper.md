# LibreTorrent batch 30 helper audit

Membership is taken only from `handoff/LIBRETORRENT_BATCH_PLAN.tsv`; it contains exactly 40 batch 30 rows. Printed plan rows, target class source, and caller searches are in `scratch/batch_030_helper_printed.txt`.

I mark direct constructors and internal helpers REACHABLE when the app source shows their use. Parcel callbacks, value methods with only Parcel callers, and comparator/string methods without a traced call remain OPEN. Fast-resume construction is inside a session callback; its external event route was not closed.

| # | Method | Finding | Evidence / route note |
|---:|---|---|---|
| 1 | `TorrentInfo.<clinit>()` | REACHABLE | Engine creates TorrentInfo instances (`TorrentEngine.java:776-801`), initializing the class and its static Creator. |
| 2 | `TorrentInfo.<init>(Parcel)` | OPEN | Only source caller is `TorrentInfo.CREATOR.createFromParcel` (`TorrentInfo.java:173-183`); no app Parcel route for this type was found. |
| 3 | `TorrentInfo.<init>(String,String,long,String,List)` | REACHABLE | Called by `TorrentEngine.makeInfo` on its stopped/invalid task branch (`TorrentEngine.java:776-785`). |
| 4 | `TorrentInfo.<init>(String,String,TorrentStateCode,int,long,long,long,long,long,long,long,int,int,String,boolean,Priority[],List,boolean)` | REACHABLE | Called by `TorrentEngine.makeInfo` for a valid task (`TorrentEngine.java:787-801`). |
| 5 | `TorrentInfo.compareTo(Object)` | OPEN | Implementation is present (`TorrentInfo.java:185-188`); no app caller or typed sort route was found. |
| 6 | `TorrentInfo.describeContents()` | OPEN | Parcelable implementation is present (`TorrentInfo.java:145-147`); app code does not parcel this type in the printed search. |
| 7 | `TorrentInfo.equals(Object)` | OPEN | Provider compares info snapshots through list membership (`TorrentInfoProvider.java:242-250`), but the callback route is asynchronous/Rx and remains open. |
| 8 | `TorrentInfo.hashCode()` | OPEN | No app call site was found; method implementation alone does not establish a route. |
| 9 | `TorrentInfo.toString()` | OPEN | No app call site was found; method implementation alone does not establish a route. |
| 10 | `TorrentInfo.writeToParcel(Parcel,int)` | OPEN | Parcelable implementation is present; no app source Parcel path for TorrentInfo was found. |
| 11 | `TorrentInfo$1.<init>()` | REACHABLE | Creator anonymous object is initialized in `TorrentInfo`'s static Creator field (`TorrentInfo.java:173-183`), loaded when the engine constructs TorrentInfo. |
| 12 | `TorrentInfo$1.createFromParcel(Parcel)` | OPEN | Creator callback (`TorrentInfo.java:173-178`); no app Parcel route for TorrentInfo was found. |
| 13 | `TorrentInfo$1.newArray(int)` | OPEN | Creator callback (`TorrentInfo.java:179-182`); no app Parcel route for TorrentInfo was found. |
| 14 | `TorrentStateCode.<clinit>()` | REACHABLE | Engine/UI/session code references enum constants; source examples include `TorrentDownloadImpl.java:1349-1387` and `TorrentListAdapter.java:198-205`. |
| 15 | `TorrentStateCode.<init>(String,int,int)` | REACHABLE | Enum values are initialized by the enum class initializer (`TorrentStateCode.java:26-66`). |
| 16 | `TorrentStateCode.fromValue(int)` | OPEN | Its source caller is `TorrentInfo(Parcel)` (`TorrentInfo.java:120-127`); no TorrentInfo Parcel route was found. |
| 17 | `TorrentStateCode.value()` | OPEN | Its source caller in app code is `TorrentInfo.writeToParcel` (`TorrentInfo.java:150-171`); no TorrentInfo Parcel route was found. |
| 18 | `TrackerInfo.<clinit>()` | REACHABLE | `TorrentDownloadImpl` constructs TrackerInfo values (`TorrentDownloadImpl.java:900-910`), initializing the class and its Creator. |
| 19 | `TrackerInfo.<init>(Parcel)` | OPEN | Only source caller is its Creator (`TrackerInfo.java:193-204`); no app Parcel route for TrackerInfo was found. |
| 20 | `TrackerInfo.<init>(String,String,int,int)` | OPEN | Constructor implementation is present (`TrackerInfo.java:79-86`), but no source call site for this overload was found. |
| 21 | `TrackerInfo.<init>(AnnounceEntry)` | REACHABLE | `TorrentDownloadImpl` constructs it from each announce entry (`TorrentDownloadImpl.java:900-910`). |
| 22 | `TrackerInfo.calcStatusCount(AnnounceEntry,AnnounceInfohash,Map)` | REACHABLE | Directly called by `getMessageAndStatus` for V1 and V2 info hashes (`TrackerInfo.java:88-99,147-155`), reached from `TrackerInfo(AnnounceEntry)` (`:67-77`). |
| 23 | `TrackerInfo.compareTo(Object)` | OPEN | Implementation is present (`TrackerInfo.java:207-210`); no typed comparator/sort call was found. |
| 24 | `TrackerInfo.describeContents()` | OPEN | Parcelable implementation is present (`TrackerInfo.java:178-181`); no app Parcel route for TrackerInfo was found. |
| 25 | `TrackerInfo.equals(Object)` | OPEN | Provider compares tracker snapshots (`TorrentInfoProvider.java:361-370`), but this occurs inside timer/Rx dispatch not closed in this audit. |
| 26 | `TrackerInfo.getMessageAndStatus(AnnounceEntry,List)` | REACHABLE | Direct call from `TrackerInfo(AnnounceEntry)` (`TrackerInfo.java:67-77`); that constructor is used in `TorrentDownloadImpl.java:900-910`. |
| 27 | `TrackerInfo.hashCode()` | OPEN | No app call site was found. |
| 28 | `TrackerInfo.infoHashStatus(AnnounceEntry,AnnounceInfohash)` | REACHABLE | Directly called from `calcStatusCount` (`TrackerInfo.java:147-166`), which runs from the reachable announce-entry constructor path. |
| 29 | `TrackerInfo.toString()` | OPEN | No app call site was found. |
| 30 | `TrackerInfo.writeToParcel(Parcel,int)` | OPEN | Parcelable implementation is present (`TrackerInfo.java:183-191`); no app source Parcel path for TrackerInfo was found. |
| 31 | `TrackerInfo$1.<init>()` | REACHABLE | Creator anonymous object is initialized in `TrackerInfo`'s static Creator field (`TrackerInfo.java:193-204`), loaded when TrackerInfo is constructed. |
| 32 | `TrackerInfo$1.createFromParcel(Parcel)` | OPEN | Creator callback (`TrackerInfo.java:193-199`); no app Parcel route for TrackerInfo was found. |
| 33 | `TrackerInfo$1.newArray(int)` | OPEN | Creator callback (`TrackerInfo.java:200-203`); no app Parcel route for TrackerInfo was found. |
| 34 | `TrackerInfo$Result.<init>(TrackerInfo,int,String)` | REACHABLE | `getMessageAndStatus` directly constructs Result for its status branches (`TrackerInfo.java:88-145`). |
| 35 | `FastResume.<init>(String,byte[])` | OPEN | Created in `TorrentDownloadImpl`'s resume-data handling (`TorrentDownloadImpl.java:508-521`); invocation depends on session/native save-resume callback. |
| 36 | `FeedChannel.<clinit>()` | REACHABLE | App creates FeedChannel in AddFeedViewModel (`AddFeedViewModel.java:173-180`), initializing its static Creator field (`FeedChannel.java:104-118`). |
| 37 | `FeedChannel.<init>(Parcel)` | OPEN | Only source caller is its Creator (`FeedChannel.java:104-118`); no app Parcel route for FeedChannel was found. |
| 38 | `FeedChannel.<init>(String,String,long,boolean,String,boolean,String)` | REACHABLE | AddFeedViewModel constructs FeedChannel for adding/updating a feed (`AddFeedViewModel.java:165-185`). |
| 39 | `FeedChannel.describeContents()` | OPEN | Parcelable implementation is present (`FeedChannel.java:94-97`); no app source Parcel path for this type was found. |
| 40 | `FeedChannel.equals(Object)` | OPEN | Implementation is present (`FeedChannel.java:126-130`); no call site was found in the app source search. |

Totals: 40 rows = 15 REACHABLE, 0 UNREACHABLE, 25 OPEN. No graph, notes, output, or coverage files were changed.
