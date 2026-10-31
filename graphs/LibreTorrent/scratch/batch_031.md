# LibreTorrent batch 31 source audit

Membership is the exact 40-row set in `scratch/batch_031_plan.txt`. Printed target source, parser/UI/repository callers, and parcel searches are in `scratch/batch_031_helper_printed.txt`. I independently checked the TagInfo Parcelable route and local model construction/use against the complete-entry-route rule.

The helper identified 10 local construction or call chains. They include feed parsing, FeedChannel/TagInfo constructors and static initialization, and FeedItem adapter equality. Those chains do not yet form complete routes from app entry points made of hand-authored edges in graph_def.py. Parcel and session callback candidates likewise remain unresolved. I kept all rows OPEN; no method is classified from a generator candidate or coverage.

| # | Method | Label | Evidence / route note |
|---:|---|---|---|
| 1 | `FeedChannel.hashCode()` | OPEN | Definition at `FeedChannel.java:120-124`; no full route established. |
| 2 | `FeedChannel.toString()` | OPEN | Definition at `FeedChannel.java:132-146`; no full route established. |
| 3 | `FeedChannel.writeToParcel(Parcel,int)` | OPEN | Parcelable implementation at `FeedChannel.java:92-102`; app Parcel route not established. |
| 4 | `FeedChannel$1.<init>()` | OPEN | AddFeedViewModel constructs FeedChannel (`AddFeedViewModel.java:173-180`), initializing Creator (`FeedChannel.java:104-118`); entry route not authored. |
| 5 | `FeedChannel$1.createFromParcel(Parcel)` | OPEN | Creator callback at `FeedChannel.java:104-112`; no app Parcel route found. |
| 6 | `FeedChannel$1.newArray(int)` | OPEN | Creator callback at `FeedChannel.java:113-117`; no app array-unparcel route found. |
| 7 | `FeedItem.<clinit>()` | OPEN | FeedFetcherWorker invokes FeedParser and parser creates FeedItem (`FeedFetcherWorker.java:156`; `FeedParser.java:109-112`); full worker entry route not authored. |
| 8 | `FeedItem.<init>(long,String,String,String,long)` | OPEN | Constructed by FeedParser (`FeedParser.java:109-112`); full worker entry route not authored. |
| 9 | `FeedItem.<init>(Parcel)` | OPEN | Creator-only source caller (`FeedItem.java:114-128`); app Parcel route not established. |
| 10 | `FeedItem.<init>(String,long,String,String,String,long)` | OPEN | Convenience constructor called from parser (`FeedItem.java:74-80`, `FeedParser.java:109-112`); entry route not authored. |
| 11 | `FeedItem.describeContents()` | OPEN | Parcelable implementation at `FeedItem.java:95-99`; app Parcel route not established. |
| 12 | `FeedItem.equals(Object)` | OPEN | FeedItemsListItem delegates equality and FeedItemsAdapter's DiffUtil callback calls it (`FeedItemsListItem.java:50-54`; `FeedItemsAdapter.java:105-120`); library callback route remains unverified. |
| 13 | `FeedItem.hashCode()` | OPEN | Implementation at `FeedItem.java:130-134`; FeedItemsListItem overrides it; no complete route established. |
| 14 | `FeedItem.toString()` | OPEN | Implementation at `FeedItem.java:142-155`; no complete route established. |
| 15 | `FeedItem.writeToParcel(Parcel,int)` | OPEN | Parcelable implementation at `FeedItem.java:101-112`; app Parcel route not established. |
| 16 | `FeedItem$1.<init>()` | OPEN | FeedParser creates FeedItem (`FeedParser.java:109-112`), initializing the Creator at `FeedItem.java:114-128`; entry route not authored. |
| 17 | `FeedItem$1.createFromParcel(Parcel)` | OPEN | Creator callback at `FeedItem.java:114-122`; no app Parcel route found. |
| 18 | `FeedItem$1.newArray(int)` | OPEN | Creator callback at `FeedItem.java:123-127`; no app array-unparcel route found. |
| 19 | `TagInfo.<clinit>()` | OPEN | AddTagViewModel creates TagInfo (`AddTagViewModel.java:55-62`), but entry route is not authored. |
| 20 | `TagInfo.<init>(long,String,int)` | OPEN | AddTagViewModel creates it for editing (`AddTagViewModel.java:57-62`); complete dialog/save route not authored. |
| 21 | `TagInfo.<init>(Parcel)` | OPEN | Creator calls this constructor (`TagInfo.java:69-79`); Intent/Bundle transfer exists, but framework unparcel dispatch is unverified. |
| 22 | `TagInfo.<init>(String,int)` | OPEN | AddTagViewModel creates it for a new tag (`AddTagViewModel.java:57-60`); complete entry route not authored. |
| 23 | `TagInfo.describeContents()` | OPEN | Parcelable method at `TagInfo.java:57-60`; framework dispatch from arguments was not source-verified. |
| 24 | `TagInfo.equals(Object)` | OPEN | Implementation at `TagInfo.java:81-91`; no complete app route established. |
| 25 | `TagInfo.toString()` | OPEN | Implementation at `TagInfo.java:101-109`; no complete app route established. |
| 26 | `TagInfo.writeToParcel(Parcel,int)` | OPEN | AddTagDialog passes TagInfo through `putParcelable` (`AddTagDialog.java:71,119-122`); framework dispatch plus complete entry route is not represented. |
| 27 | `TagInfo$1.<init>()` | OPEN | TagInfo construction initializes Creator (`TagInfo.java:69-79`); entry route not authored. |
| 28 | `TagInfo$1.createFromParcel(Parcel)` | OPEN | AddTagActivity/Dialog read TagInfo (`AddTagActivity.java:57`; `AddTagDialog.java:119`); Creator callback dispatch and entry route are unverified. |
| 29 | `TagInfo$1.newArray(int)` | OPEN | Creator array callback at `TagInfo.java:75-78`; no app array-unparcel use found. |
| 30 | `Torrent.<clinit>()` | OPEN | Constructed in `TorrentSessionImpl.addTorrent` (`TorrentSessionImpl.java:263-270`); complete app-to-session route not established. |
| 31 | `Torrent.<init>(Parcel)` | OPEN | Creator-only source call (`Torrent.java:157-170`); no app Parcel route found. |
| 32 | `Torrent.<init>(String,Uri,String,boolean,long,boolean,boolean)` | OPEN | Constructed in `TorrentSessionImpl.addTorrent` (`TorrentSessionImpl.java:263-270`); async add route not closed. |
| 33 | `Torrent.<init>(String,String,Uri,String,boolean,long,boolean,boolean)` | OPEN | No app source call found; Room materialization path is not source-closed. |
| 34 | `Torrent.describeContents()` | OPEN | Parcelable method at `Torrent.java:135-139`; no app Parcel route found. |
| 35 | `Torrent.equals(Object)` | OPEN | Definition at `Torrent.java:178-182`; no complete app route established. |
| 36 | `Torrent.getMagnet()` | OPEN | Called in session metadata restore (`TorrentSessionImpl.java:413-416`); restore callback path not closed. |
| 37 | `Torrent.hashCode()` | OPEN | Definition at `Torrent.java:172-176`; no complete route established. |
| 38 | `Torrent.isDownloadingMetadata()` | OPEN | Called in session add/restore paths (`TorrentSessionImpl.java:290,343,413`); entry to those paths unresolved. |
| 39 | `Torrent.setMagnetUri(String)` | OPEN | Called during add/metadata handling (`TorrentSessionImpl.java:277`; `TorrentDownloadImpl.java:428`); session/event route unresolved. |
| 40 | `Torrent.toString()` | OPEN | Definition at `Torrent.java:184-195`; no complete route established. |

Totals: 40 rows = 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. No graph labels changed, so no graph build was run for this batch.
