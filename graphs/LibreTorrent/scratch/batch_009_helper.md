# LibreTorrent batch 9 helper review

Membership source is `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, exactly its 40 rows with `batch=9`. Source and call-site prints are in `scratch/batch_009_helper_printed.txt`.

These are generated Data Binding methods. No generated binding Java source for these classes is present in the supplied `app/src/main/java` tree. App code imports/holds the generated binding types and calls `DataBindingUtil.inflate`, but a search found no direct invocation of any listed `ClassName.bind(...)` or `ClassName.inflate(...)` method. The generated mapper/implementation and Data Binding library source that could establish an indirect target call are unavailable. I therefore leave every method OPEN rather than inferring either a route or a no-trigger label.

| # | Plan method | Result | Evidence and reason |
|---:|---|---|---|
| 1 | `FragmentFeedItemsBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | `FeedItemsFragment.java:111` calls `DataBindingUtil.inflate`; target overload not directly invoked; generated source unavailable. |
| 2 | `FragmentFeedItemsBinding.inflate(LayoutInflater,Object)` | OPEN | Same fragment DataBindingUtil call; indirect generated/library route unknown. |
| 3 | `FragmentMainBinding.bind(View)` | OPEN | `MainFragment.java:119` calls `DataBindingUtil.inflate`; no direct `bind(View)` call; generated source unavailable. |
| 4 | `FragmentMainBinding.bind(View,Object)` | OPEN | Same; target overload not directly invoked. |
| 5 | `FragmentMainBinding.inflate(LayoutInflater)` | OPEN | Same fragment DataBindingUtil call; target overload not directly invoked. |
| 6 | `FragmentMainBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | Same; generated mapper route unavailable. |
| 7 | `FragmentMainBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | Same; generated mapper route unavailable. |
| 8 | `FragmentMainBinding.inflate(LayoutInflater,Object)` | OPEN | Same; generated mapper route unavailable. |
| 9 | `ItemFeedChannelListBinding.bind(View)` | OPEN | `FeedChannelListAdapter.java:82` calls `DataBindingUtil.inflate`; not direct bind call. |
| 10 | `ItemFeedChannelListBinding.bind(View,Object)` | OPEN | Same adapter call; generated implementation absent. |
| 11 | `ItemFeedChannelListBinding.inflate(LayoutInflater)` | OPEN | Adapter uses DataBindingUtil, not this method directly. |
| 12 | `ItemFeedChannelListBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | Adapter uses DataBindingUtil, not this method directly. |
| 13 | `ItemFeedChannelListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | Adapter uses DataBindingUtil, not this method directly. |
| 14 | `ItemFeedChannelListBinding.inflate(LayoutInflater,Object)` | OPEN | Adapter uses DataBindingUtil, not this method directly. |
| 15 | `ItemFeedItemsListBinding.bind(View)` | OPEN | `FeedItemsAdapter.java:67` calls `DataBindingUtil.inflate`; not direct bind call. |
| 16 | `ItemFeedItemsListBinding.bind(View,Object)` | OPEN | Same adapter call; generated implementation absent. |
| 17 | `ItemFeedItemsListBinding.inflate(LayoutInflater)` | OPEN | Adapter uses DataBindingUtil, not this method directly. |
| 18 | `ItemFeedItemsListBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | Adapter uses DataBindingUtil, not this method directly. |
| 19 | `ItemFeedItemsListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | Adapter uses DataBindingUtil, not this method directly. |
| 20 | `ItemFeedItemsListBinding.inflate(LayoutInflater,Object)` | OPEN | Adapter uses DataBindingUtil, not this method directly. |
| 21 | `ItemLogListBinding.bind(View)` | OPEN | `LogAdapter.java:51` calls `DataBindingUtil.inflate`; not direct bind call. |
| 22 | `ItemLogListBinding.bind(View,Object)` | OPEN | Same adapter call; generated implementation absent. |
| 23 | `ItemLogListBinding.inflate(LayoutInflater)` | OPEN | Adapter uses DataBindingUtil, not this method directly. |
| 24 | `ItemLogListBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | Adapter uses DataBindingUtil, not this method directly. |
| 25 | `ItemLogListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | Adapter uses DataBindingUtil, not this method directly. |
| 26 | `ItemLogListBinding.inflate(LayoutInflater,Object)` | OPEN | Adapter uses DataBindingUtil, not this method directly. |
| 27 | `ItemPeersListBinding.bind(View)` | OPEN | `PeerListAdapter.java:62` calls `DataBindingUtil.inflate`; not direct bind call. |
| 28 | `ItemPeersListBinding.bind(View,Object)` | OPEN | Same adapter call; generated implementation absent. |
| 29 | `ItemPeersListBinding.inflate(LayoutInflater)` | OPEN | Adapter uses DataBindingUtil, not this method directly. |
| 30 | `ItemPeersListBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | Adapter uses DataBindingUtil, not this method directly. |
| 31 | `ItemPeersListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | Adapter uses DataBindingUtil, not this method directly. |
| 32 | `ItemPeersListBinding.inflate(LayoutInflater,Object)` | OPEN | Adapter uses DataBindingUtil, not this method directly. |
| 33 | `ItemTorrentContentFileBinding.bind(View)` | OPEN | `TorrentContentFilesAdapter.java:76` calls `DataBindingUtil.inflate`; not direct bind call. |
| 34 | `ItemTorrentContentFileBinding.bind(View,Object)` | OPEN | Same adapter call; generated implementation absent. |
| 35 | `ItemTorrentContentFileBinding.inflate(LayoutInflater)` | OPEN | Adapter uses DataBindingUtil, not this method directly. |
| 36 | `ItemTorrentContentFileBinding.inflate(LayoutInflater,ViewGroup,boolean)` | OPEN | Adapter uses DataBindingUtil, not this method directly. |
| 37 | `ItemTorrentContentFileBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)` | OPEN | Adapter uses DataBindingUtil, not this method directly. |
| 38 | `ItemTorrentContentFileBinding.inflate(LayoutInflater,Object)` | OPEN | Adapter uses DataBindingUtil, not this method directly. |
| 39 | `ItemTorrentDownloadableFileBinding.bind(View)` | OPEN | `DownloadableFilesAdapter.java:60` calls `DataBindingUtil.inflate`; not direct bind call. |
| 40 | `ItemTorrentDownloadableFileBinding.bind(View,Object)` | OPEN | Same adapter call; generated implementation absent. |

Total: exactly 40 plan members, all OPEN because the available source does not establish the generated-method route. No generator or coverage evidence was consulted.
