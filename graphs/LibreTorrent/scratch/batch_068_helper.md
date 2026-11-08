# LibreTorrent batch 68 source audit

Membership is exactly the 40 batch 68 rows printed at the top of `batch_068_helper_printed.txt`. Evidence is bounded to the fragment/adapter binding call sites, corresponding layout XML, binding invocation search, and generated Java binding source inventories. The generated `FragmentFeed*Binding*`, `FragmentMainBinding*`, feed item binding, and tracker-list binding classes are absent from the uploaded Java source tree. All rows remain OPEN because generated implementations and complete Data Binding dispatch paths are not present in the evidence. App-side inflation context does not establish individual generated method routes.

| # | Method | Finding | Printed evidence / unresolved route |
|---:|---|---|---|
| 1 | `FragmentDetailTorrentTrackerListBindingImpl.setVariable(int,Object)Z` | OPEN | Generated tracker binding source search has no uploaded match; variable dispatch unavailable. |
| 2 | `FragmentFeedBinding.<init>(Object,View,int,FloatingActionButton,CoordinatorLayout,TextView,EmptyRecyclerView,ThemedSwipeRefreshLayout)V` | OPEN | Generated base binding absent; `FeedFragment` inflation/layout printed, constructor route unresolved. |
| 3 | `FragmentFeedBindingImpl.<clinit>()V` | OPEN | Generated implementation absent; initialization/delegate dispatch unavailable. |
| 4 | `FragmentFeedBindingImpl.<init>(DataBindingComponent,View)V` | OPEN | Generated implementation absent; framework binding construction route unresolved. |
| 5 | `FragmentFeedBindingImpl.<init>(DataBindingComponent,View,Object[])V` | OPEN | Generated implementation absent; framework binding construction route unresolved. |
| 6 | `FragmentFeedBindingImpl.executeBindings()V` | OPEN | Generated implementation absent; Data Binding execution dispatch unresolved. |
| 7 | `FragmentFeedBindingImpl.hasPendingBindings()Z` | OPEN | Generated implementation absent; Data Binding query dispatch unresolved. |
| 8 | `FragmentFeedBindingImpl.invalidateAll()V` | OPEN | Generated implementation absent; invalidation dispatch unresolved. |
| 9 | `FragmentFeedBindingImpl.onFieldChange(int,Object,int)Z` | OPEN | Generated implementation absent; field-change dispatch unresolved. |
| 10 | `FragmentFeedBindingImpl.setVariable(int,Object)Z` | OPEN | Generated implementation absent; variable dispatch unresolved. |
| 11 | `FragmentFeedItemsBinding.<init>(Object,View,int,AppBarLayout,CoordinatorLayout,TextView,EmptyRecyclerView,ThemedSwipeRefreshLayout,Toolbar)V` | OPEN | Generated base binding absent; `FeedItemsFragment` inflation/layout printed. |
| 12 | `FragmentFeedItemsBindingImpl.<clinit>()V` | OPEN | Generated implementation absent; initialization/delegate dispatch unavailable. |
| 13 | `FragmentFeedItemsBindingImpl.<init>(DataBindingComponent,View)V` | OPEN | Generated implementation absent; framework construction route unresolved. |
| 14 | `FragmentFeedItemsBindingImpl.<init>(DataBindingComponent,View,Object[])V` | OPEN | Generated implementation absent; framework construction route unresolved. |
| 15 | `FragmentFeedItemsBindingImpl.executeBindings()V` | OPEN | Generated implementation absent; Data Binding execution dispatch unresolved. |
| 16 | `FragmentFeedItemsBindingImpl.hasPendingBindings()Z` | OPEN | Generated implementation absent; Data Binding query dispatch unresolved. |
| 17 | `FragmentFeedItemsBindingImpl.invalidateAll()V` | OPEN | Generated implementation absent; invalidation dispatch unresolved. |
| 18 | `FragmentFeedItemsBindingImpl.onFieldChange(int,Object,int)Z` | OPEN | Generated implementation absent; field-change dispatch unresolved. |
| 19 | `FragmentFeedItemsBindingImpl.setVariable(int,Object)Z` | OPEN | Generated implementation absent; variable dispatch unresolved. |
| 20 | `FragmentMainBinding.<init>(Object,View,int,TextView,ThemedSpeedDialView,SpeedDialOverlayLayout,CoordinatorLayout,EmptyRecyclerView)V` | OPEN | Generated base binding absent; `MainFragment` inflation/layout printed. |
| 21 | `FragmentMainBindingImpl.<clinit>()V` | OPEN | Generated implementation absent; initialization/delegate dispatch unavailable. |
| 22 | `FragmentMainBindingImpl.<init>(DataBindingComponent,View)V` | OPEN | Generated implementation absent; framework construction route unresolved. |
| 23 | `FragmentMainBindingImpl.<init>(DataBindingComponent,View,Object[])V` | OPEN | Generated implementation absent; framework construction route unresolved. |
| 24 | `FragmentMainBindingImpl.executeBindings()V` | OPEN | Generated implementation absent; Data Binding execution dispatch unresolved. |
| 25 | `FragmentMainBindingImpl.hasPendingBindings()Z` | OPEN | Generated implementation absent; Data Binding query dispatch unresolved. |
| 26 | `FragmentMainBindingImpl.invalidateAll()V` | OPEN | Generated implementation absent; invalidation dispatch unresolved. |
| 27 | `FragmentMainBindingImpl.onFieldChange(int,Object,int)Z` | OPEN | Generated implementation absent; field-change dispatch unresolved. |
| 28 | `FragmentMainBindingImpl.setVariable(int,Object)Z` | OPEN | Generated implementation absent; variable dispatch unresolved. |
| 29 | `ItemFeedChannelListBinding.<init>(Object,View,int,TextView,View,TextView,TextView,TextView)V` | OPEN | Generated base binding absent; adapter inflation/layout printed, constructor route unresolved. |
| 30 | `ItemFeedChannelListBindingImpl.<clinit>()V` | OPEN | Generated implementation absent; initialization/delegate dispatch unavailable. |
| 31 | `ItemFeedChannelListBindingImpl.<init>(DataBindingComponent,View)V` | OPEN | Generated implementation absent; framework construction route unresolved. |
| 32 | `ItemFeedChannelListBindingImpl.<init>(DataBindingComponent,View,Object[])V` | OPEN | Generated implementation absent; framework construction route unresolved. |
| 33 | `ItemFeedChannelListBindingImpl.executeBindings()V` | OPEN | Generated implementation absent; Data Binding execution dispatch unresolved. |
| 34 | `ItemFeedChannelListBindingImpl.hasPendingBindings()Z` | OPEN | Generated implementation absent; Data Binding query dispatch unresolved. |
| 35 | `ItemFeedChannelListBindingImpl.invalidateAll()V` | OPEN | Generated implementation absent; invalidation dispatch unresolved. |
| 36 | `ItemFeedChannelListBindingImpl.onFieldChange(int,Object,int)Z` | OPEN | Generated implementation absent; field-change dispatch unresolved. |
| 37 | `ItemFeedChannelListBindingImpl.setVariable(int,Object)Z` | OPEN | Generated implementation absent; variable dispatch unresolved. |
| 38 | `ItemFeedItemsListBinding.<init>(Object,View,int,ImageButton,TextView,TextView)V` | OPEN | Generated base binding absent; feed-items adapter inflation/layout context not fully traced. |
| 39 | `ItemFeedItemsListBindingImpl.<clinit>()V` | OPEN | Generated implementation absent; initialization/delegate dispatch unavailable. |
| 40 | `ItemFeedItemsListBindingImpl.<init>(DataBindingComponent,View)V` | OPEN | Generated implementation absent; framework binding construction route unresolved. |

Count: 40 plan rows = 40 OPEN, 0 REACHABLE labels, 0 UNREACHABLE labels. No graph edits or coverage evidence were used.
