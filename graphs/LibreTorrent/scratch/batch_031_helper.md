# LibreTorrent batch 31 helper audit

Membership comes only from `handoff/LIBRETORRENT_BATCH_PLAN.tsv`; it contains exactly 40 batch 31 rows. Printed plan rows, entity source, app callers, and the FeedItem adapter path are in `scratch/batch_031_helper_printed.txt`.

OPEN means this audit did not establish a complete route, especially where a target depends on Parcelable framework dispatch, Room-generated code, or the TorrentEngine/Rx session path. AndroidX DiffUtil and WorkManager links are library dispatches and therefore inferred from app registration/use.

| # | Method | Finding | Evidence / route note |
|---:|---|---|---|
| 1 | `FeedChannel.hashCode()` | OPEN | Implementation is at `FeedChannel.java:120-124`; no app call site was found. |
| 2 | `FeedChannel.toString()` | OPEN | Implementation is at `FeedChannel.java:132-146`; no app call site was found. |
| 3 | `FeedChannel.writeToParcel(Parcel,int)` | OPEN | Parcelable implementation is at `FeedChannel.java:92-102`; no app source passes FeedChannel through a Parcel. |
| 4 | `FeedChannel$1.<init>()` | REACHABLE | AddFeedViewModel constructs FeedChannel (`AddFeedViewModel.java:173-180`), initializing the class and its static `CREATOR` object (`FeedChannel.java:104-118`). |
| 5 | `FeedChannel$1.createFromParcel(Parcel)` | OPEN | Creator callback is at `FeedChannel.java:104-112`; no app Parcel route for FeedChannel was found. |
| 6 | `FeedChannel$1.newArray(int)` | OPEN | Creator callback is at `FeedChannel.java:113-117`; no app array-unparcel route for FeedChannel was found. |
| 7 | `FeedItem.<clinit>()` | REACHABLE | FeedFetcherWorker creates FeedParser (`FeedFetcherWorker.java:156`); its `getItems` constructs FeedItem (`FeedParser.java:109-112`), initializing the class. The app enqueues FeedFetcherWorker for feed refreshes (call sites printed). |
| 8 | `FeedItem.<init>(long,String,String,String,long)` | REACHABLE | Directly constructed by `FeedParser.getItems` (`FeedParser.java:109-112`), called from FeedFetcherWorker (`FeedFetcherWorker.java:156`); app source enqueues the worker for user feed fetches. |
| 9 | `FeedItem.<init>(Parcel)` | OPEN | Only source call is its Creator (`FeedItem.java:114-128`); no app Parcel route for FeedItem was found. |
| 10 | `FeedItem.<init>(String,long,String,String,String,long)` | REACHABLE | Called directly by the convenience constructor (`FeedItem.java:74-80`), which is reached by FeedParser (`:109-112`). |
| 11 | `FeedItem.describeContents()` | OPEN | Parcelable implementation is at `FeedItem.java:95-99`; no app Parcel route for FeedItem was found. |
| 12 | `FeedItem.equals(Object)` | REACHABLE | FeedItemsListItem delegates `equals` to `super.equals` (`FeedItemsListItem.java:50-54`); FeedItemsAdapter's DiffUtil callback calls `oldItem.equals(newItem)` (`FeedItemsAdapter.java:105-120`) after the feed screen submits items. AndroidX callback dispatch is inferred. |
| 13 | `FeedItem.hashCode()` | OPEN | Implementation is at `FeedItem.java:130-134`; FeedItemsListItem overrides `hashCode` (`FeedItemsListItem.java:37-41`), and no other app call site was found. |
| 14 | `FeedItem.toString()` | OPEN | Implementation is at `FeedItem.java:142-155`; no app call site was found. |
| 15 | `FeedItem.writeToParcel(Parcel,int)` | OPEN | Parcelable implementation is at `FeedItem.java:101-112`; no app source passes FeedItem through a Parcel. |
| 16 | `FeedItem$1.<init>()` | REACHABLE | FeedParser constructs FeedItem (`FeedParser.java:109-112`), initializing its static Creator object (`FeedItem.java:114-128`). |
| 17 | `FeedItem$1.createFromParcel(Parcel)` | OPEN | Creator callback is at `FeedItem.java:114-122`; no app Parcel route for FeedItem was found. |
| 18 | `FeedItem$1.newArray(int)` | OPEN | Creator callback is at `FeedItem.java:123-127`; no app array-unparcel route for FeedItem was found. |
| 19 | `TagInfo.<clinit>()` | REACHABLE | AddTagViewModel creates TagInfo objects (`AddTagViewModel.java:55-62`), initializing the class and its Creator. |
| 20 | `TagInfo.<init>(long,String,int)` | REACHABLE | AddTagViewModel constructs this overload when editing an existing tag (`AddTagViewModel.java:57-62`), from the add/edit dialog save path. |
| 21 | `TagInfo.<init>(Parcel)` | OPEN | Creator calls this constructor (`TagInfo.java:69-79`); app code passes TagInfo through Intent/Bundle APIs, but framework unparcel dispatch was not independently source-verified. |
| 22 | `TagInfo.<init>(String,int)` | REACHABLE | AddTagViewModel constructs this overload when adding a new tag (`AddTagViewModel.java:57-60`), from the add dialog save path. |
| 23 | `TagInfo.describeContents()` | OPEN | Parcelable implementation is at `TagInfo.java:57-60`; framework callback dispatch from the Bundle/Intent path was not source-verified. |
| 24 | `TagInfo.equals(Object)` | OPEN | Implementation is at `TagInfo.java:81-91`; no complete app call route was established. |
| 25 | `TagInfo.toString()` | OPEN | Implementation is at `TagInfo.java:101-109`; no app call site was found. |
| 26 | `TagInfo.writeToParcel(Parcel,int)` | OPEN | AddTagDialog passes TagInfo through `putParcelable` (`AddTagDialog.java:71,119-122`), but the Parcelable framework call into this method was not independently source-verified. |
| 27 | `TagInfo$1.<init>()` | REACHABLE | AddTagViewModel constructs TagInfo (`AddTagViewModel.java:59-62`), initializing the static Creator object (`TagInfo.java:69-79`). |
| 28 | `TagInfo$1.createFromParcel(Parcel)` | OPEN | AddTagActivity/Dialog read TagInfo via Parcelable APIs, but Creator callback dispatch was not independently verified from framework source (`AddTagActivity.java:57`; `AddTagDialog.java:119`). |
| 29 | `TagInfo$1.newArray(int)` | OPEN | Creator array callback is at `TagInfo.java:75-78`; no app array-unparcel use was found. |
| 30 | `Torrent.<clinit>()` | OPEN | Torrent is constructed in `TorrentSessionImpl.addTorrent` (`TorrentSessionImpl.java:263-270`), but the entry-to-session Rx route was not closed in this audit. |
| 31 | `Torrent.<init>(Parcel)` | OPEN | Only source caller is Torrent's Creator (`Torrent.java:157-170`); no app Parcel route for Torrent was found. |
| 32 | `Torrent.<init>(String,Uri,String,boolean,long,boolean,boolean)` | OPEN | Direct construction appears in `TorrentSessionImpl.addTorrent` (`TorrentSessionImpl.java:263-270`); reaching that session operation depends on the asynchronous add-torrent path not verified here. |
| 33 | `Torrent.<init>(String,String,Uri,String,boolean,long,boolean,boolean)` | OPEN | No app source constructor call was found; Room-generated entity materialization is outside the printed app source. |
| 34 | `Torrent.describeContents()` | OPEN | Parcelable implementation is at `Torrent.java:135-139`; no app Parcel route for Torrent was found. |
| 35 | `Torrent.equals(Object)` | OPEN | Implementation is at `Torrent.java:178-182`; no app call site was found. |
| 36 | `Torrent.getMagnet()` | OPEN | Called from `TorrentSessionImpl` metadata restore (`TorrentSessionImpl.java:413-416`); full restore callback path was not closed. |
| 37 | `Torrent.hashCode()` | OPEN | Implementation is at `Torrent.java:172-176`; no app call site was found. |
| 38 | `Torrent.isDownloadingMetadata()` | OPEN | Called in `TorrentSessionImpl` add/restore paths (`TorrentSessionImpl.java:290,343,413`); entry to those session operations remains open. |
| 39 | `Torrent.setMagnetUri(String)` | OPEN | Called during add/metadata handling (`TorrentSessionImpl.java:277`; `TorrentDownloadImpl.java:428`); the session/event routes were not closed. |
| 40 | `Torrent.toString()` | OPEN | Implementation is at `Torrent.java:184-195`; no app call site was found. |

Totals: 40 rows = 10 REACHABLE, 0 UNREACHABLE, 30 OPEN. No graph, notes, output, or coverage files were changed.
