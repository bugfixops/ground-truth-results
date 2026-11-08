# LibreTorrent batch 9 source audit

Membership: exactly the 40 batch `9` rows in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`. I independently printed the plan rows, generated binding class search and app DataBindingUtil call lines. Evidence is in `scratch/batch_009_independent_printed.txt`; the helper's per-method direct-call scan and report are in `scratch/batch_009_helper_printed.txt` and `scratch/batch_009_helper.md`.

These are generated Data Binding APIs. Source has layout requests through DataBindingUtil, but no generated class or mapper/dispatcher implementation. The app calls do not name the listed static overloads. The method-level routes are unresolved, so no labels or edges were authored.

| Class | Plan methods | Label | Evidence / note |
|---|---:|---|---|
| `FragmentFeedItemsBinding` | 2 | OPEN | Matching layout request at `FeedItemsFragment.java:111`; generated overload unknown. |
| `FragmentMainBinding` | 6 | OPEN | Matching layout request at `MainFragment.java:119`; generated overload unknown. |
| `ItemFeedChannelListBinding` | 6 | OPEN | DataBindingUtil request at `FeedChannelListAdapter.java:82-85`; overload unknown. |
| `ItemFeedItemsListBinding` | 6 | OPEN | DataBindingUtil request at `FeedItemsAdapter.java:67-70`; overload unknown. |
| `ItemLogListBinding` | 6 | OPEN | DataBindingUtil request at `LogAdapter.java:51-54`; overload unknown. |
| `ItemPeersListBinding` | 6 | OPEN | DataBindingUtil request at `PeerListAdapter.java:62-65`; overload unknown. |
| `ItemTorrentContentFileBinding` | 6 | OPEN | DataBindingUtil request at `TorrentContentFilesAdapter.java:76-79`; overload unknown. |
| `ItemTorrentDownloadableFileBinding` | 2 | OPEN | DataBindingUtil request at `DownloadableFilesAdapter.java:60-63`; overload unknown. |

Result: 40 plan rows reviewed; 0 labels authored; 40 remain OPEN.
