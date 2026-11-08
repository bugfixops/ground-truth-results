# LibreTorrent batch 66 source audit

Membership is exactly the 40 batch 66 rows printed at the top of `batch_066_helper_printed.txt`. Evidence is bounded to the detail fragment and three page binding setup excerpts, matching layouts, binding call-site search, and generated binding source inventory. The generated `FragmentDetailTorrentBindingImpl*`, `FragmentDetailTorrentFilesBindingImpl*`, `FragmentDetailTorrentInfoBindingImpl*`, and `FragmentDetailTorrentPeerListBinding*` Java classes are absent from the uploaded source tree. All target methods remain OPEN because generated bodies and complete Data Binding dispatch paths are unavailable. App-side inflation and XML structure alone do not establish individual binding-method routes.

| # | Method | Finding | Printed evidence / unresolved route |
|---:|---|---|---|
| 1 | `FragmentDetailTorrentBindingImpl.<clinit>()V` | OPEN | Generated implementation search has no uploaded match; initialization/delegate dispatch unavailable. |
| 2 | `FragmentDetailTorrentBindingImpl.<init>(DataBindingComponent,View)V` | OPEN | Generated source absent; framework binding construction route unresolved. |
| 3 | `FragmentDetailTorrentBindingImpl.<init>(DataBindingComponent,View,Object[])V` | OPEN | Generated source absent; framework binding construction route unresolved. |
| 4 | `FragmentDetailTorrentBindingImpl.executeBindings()V` | OPEN | Generated source absent; Data Binding execution dispatch unresolved. |
| 5 | `FragmentDetailTorrentBindingImpl.hasPendingBindings()Z` | OPEN | Generated source absent; Data Binding query dispatch unresolved. |
| 6 | `FragmentDetailTorrentBindingImpl.invalidateAll()V` | OPEN | Generated source absent; invalidation dispatch unresolved. |
| 7 | `FragmentDetailTorrentBindingImpl.onChangeAppbar(DetailTorrentAppbarBinding,int)Z` | OPEN | Generated source absent; observable binding-change dispatch unresolved. |
| 8 | `FragmentDetailTorrentBindingImpl.onFieldChange(int,Object,int)Z` | OPEN | Generated source absent; field-change dispatch unresolved. |
| 9 | `FragmentDetailTorrentBindingImpl.setLifecycleOwner(LifecycleOwner)V` | OPEN | Generated source absent; lifecycle-owner binding route unresolved. |
| 10 | `FragmentDetailTorrentBindingImpl.setVariable(int,Object)Z` | OPEN | Generated source absent; generated variable dispatch unresolved. |
| 11 | `FragmentDetailTorrentFilesBinding.<init>(Object,View,int,RecyclerView,TextView,ContentLoadingProgressBar)V` | OPEN | Generated base binding absent; page inflation call/layout printed, constructor route unresolved. |
| 12 | `FragmentDetailTorrentFilesBinding.getViewModel()DetailTorrentViewModel` | OPEN | Generated base binding absent; getter implementation unavailable. |
| 13 | `FragmentDetailTorrentFilesBindingImpl.<clinit>()V` | OPEN | Generated implementation absent; initialization/delegate dispatch unavailable. |
| 14 | `FragmentDetailTorrentFilesBindingImpl.<init>(DataBindingComponent,View)V` | OPEN | Generated implementation absent; framework construction route unresolved. |
| 15 | `FragmentDetailTorrentFilesBindingImpl.<init>(DataBindingComponent,View,Object[])V` | OPEN | Generated implementation absent; framework construction route unresolved. |
| 16 | `FragmentDetailTorrentFilesBindingImpl.executeBindings()V` | OPEN | Generated implementation absent; Data Binding execution dispatch unresolved. |
| 17 | `FragmentDetailTorrentFilesBindingImpl.hasPendingBindings()Z` | OPEN | Generated implementation absent; Data Binding query dispatch unresolved. |
| 18 | `FragmentDetailTorrentFilesBindingImpl.invalidateAll()V` | OPEN | Generated implementation absent; invalidation dispatch unresolved. |
| 19 | `FragmentDetailTorrentFilesBindingImpl.onChangeViewModelInfo(TorrentDetailsInfo,int)Z` | OPEN | Generated implementation absent; observable change dispatch unresolved. |
| 20 | `FragmentDetailTorrentFilesBindingImpl.onFieldChange(int,Object,int)Z` | OPEN | Generated implementation absent; field-change dispatch unresolved. |
| 21 | `FragmentDetailTorrentFilesBindingImpl.setVariable(int,Object)Z` | OPEN | Generated implementation absent; generated variable dispatch unresolved. |
| 22 | `FragmentDetailTorrentFilesBindingImpl.setViewModel(DetailTorrentViewModel)V` | OPEN | Generated implementation absent; view-model setter dispatch unresolved. |
| 23 | `FragmentDetailTorrentInfoBinding.<init>(Object,View,int,TextView,TextView,TextView,CheckBox,ImageButton,TextView,ImageButton,TextView,TextView,TextView,TextView,LinearLayout,LinearLayout,LinearLayout,LinearLayout,LinearLayout,TextView,TextView,CheckBox,TextView,TorrentTagsList,TextView)V` | OPEN | Generated base binding absent; info page inflation/layout printed, constructor route unresolved. |
| 24 | `FragmentDetailTorrentInfoBinding.getViewModel()DetailTorrentViewModel` | OPEN | Generated base binding absent; getter implementation unavailable. |
| 25 | `FragmentDetailTorrentInfoBindingImpl.<clinit>()V` | OPEN | Generated implementation absent; initialization/delegate dispatch unavailable. |
| 26 | `FragmentDetailTorrentInfoBindingImpl.<init>(DataBindingComponent,View)V` | OPEN | Generated implementation absent; framework construction route unresolved. |
| 27 | `FragmentDetailTorrentInfoBindingImpl.<init>(DataBindingComponent,View,Object[])V` | OPEN | Generated implementation absent; framework construction route unresolved. |
| 28 | `FragmentDetailTorrentInfoBindingImpl.executeBindings()V` | OPEN | Generated implementation absent; Data Binding execution dispatch unresolved. |
| 29 | `FragmentDetailTorrentInfoBindingImpl.hasPendingBindings()Z` | OPEN | Generated implementation absent; Data Binding query dispatch unresolved. |
| 30 | `FragmentDetailTorrentInfoBindingImpl.invalidateAll()V` | OPEN | Generated implementation absent; invalidation dispatch unresolved. |
| 31 | `FragmentDetailTorrentInfoBindingImpl.onChangeViewModelInfo(TorrentDetailsInfo,int)Z` | OPEN | Generated implementation absent; observable change dispatch unresolved. |
| 32 | `FragmentDetailTorrentInfoBindingImpl.onChangeViewModelMutableParams(TorrentDetailsMutableParams,int)Z` | OPEN | Generated implementation absent; observable change dispatch unresolved. |
| 33 | `FragmentDetailTorrentInfoBindingImpl.onFieldChange(int,Object,int)Z` | OPEN | Generated implementation absent; field-change dispatch unresolved. |
| 34 | `FragmentDetailTorrentInfoBindingImpl.setVariable(int,Object)Z` | OPEN | Generated implementation absent; generated variable dispatch unresolved. |
| 35 | `FragmentDetailTorrentInfoBindingImpl.setViewModel(DetailTorrentViewModel)V` | OPEN | Generated implementation absent; view-model setter dispatch unresolved. |
| 36 | `FragmentDetailTorrentInfoBindingImpl$1.<init>(FragmentDetailTorrentInfoBindingImpl)V` | OPEN | Generated observable wrapper absent; callback construction unavailable. |
| 37 | `FragmentDetailTorrentInfoBindingImpl$1.onChange()V` | OPEN | Generated observable wrapper absent; callback dispatch unavailable. |
| 38 | `FragmentDetailTorrentInfoBindingImpl$2.<init>(FragmentDetailTorrentInfoBindingImpl)V` | OPEN | Generated observable wrapper absent; callback construction unavailable. |
| 39 | `FragmentDetailTorrentInfoBindingImpl$2.onChange()V` | OPEN | Generated observable wrapper absent; callback dispatch unavailable. |
| 40 | `FragmentDetailTorrentPeerListBinding.<init>(Object,View,int,TextView,EmptyRecyclerView)V` | OPEN | Generated base binding source absent; peer-page inflation/layout context not fully followed from app entry. |

Count: 40 plan rows = 40 OPEN, 0 REACHABLE labels, 0 UNREACHABLE labels. No graph edits or coverage evidence were used.
