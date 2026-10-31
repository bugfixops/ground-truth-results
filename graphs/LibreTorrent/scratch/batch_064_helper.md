# LibreTorrent batch 64 source audit

Membership is exactly the 40 batch 64 rows printed at the top of `batch_064_helper_printed.txt`. Evidence is bounded to dialog/adapter binding call sites, the relevant layouts, and generated Java source searches. The generated `DialogSelectTagBinding*`, `Drawer*TagsListItemBinding*`, and `FragmentAddTorrentFilesBinding*` Java sources are absent from the uploaded source tree. All methods remain OPEN because their generated bodies and full Data Binding dispatch routes are unavailable. App-side inflation and XML context do not establish method-level routes. No missing generated file is used as proof of unreachability.

| # | Method | Finding | Printed evidence / unresolved route |
|---:|---|---|---|
| 1 | `DialogSelectTagBindingImpl.hasPendingBindings()Z` | OPEN | Generated binding source search has no uploaded match; implementation and dispatch unavailable. |
| 2 | `DialogSelectTagBindingImpl.invalidateAll()V` | OPEN | Generated binding source absent; invalidation dispatch unavailable. |
| 3 | `DialogSelectTagBindingImpl.onFieldChange(int,Object,int)Z` | OPEN | Generated binding source absent; field-change dispatch unavailable. |
| 4 | `DialogSelectTagBindingImpl.setVariable(int,Object)Z` | OPEN | Generated binding source absent; variable dispatch unavailable. |
| 5 | `DrawerEmptyTagsListItemBinding.<init>(Object,View,int,ImageView,TextView)V` | OPEN | Generated base binding absent; TagsAdapter inflation call and layout printed, constructor route unresolved. |
| 6 | `DrawerEmptyTagsListItemBindingImpl.<clinit>()V` | OPEN | Generated implementation absent; initialization/delegate dispatch unavailable. |
| 7 | `DrawerEmptyTagsListItemBindingImpl.<init>(DataBindingComponent,View)V` | OPEN | Generated implementation absent; framework construction route unresolved. |
| 8 | `DrawerEmptyTagsListItemBindingImpl.<init>(DataBindingComponent,View,Object[])V` | OPEN | Generated implementation absent; framework construction route unresolved. |
| 9 | `DrawerEmptyTagsListItemBindingImpl.executeBindings()V` | OPEN | Generated implementation absent; Data Binding execution route unresolved. |
| 10 | `DrawerEmptyTagsListItemBindingImpl.hasPendingBindings()Z` | OPEN | Generated implementation absent; Data Binding query route unresolved. |
| 11 | `DrawerEmptyTagsListItemBindingImpl.invalidateAll()V` | OPEN | Generated implementation absent; invalidation dispatch unresolved. |
| 12 | `DrawerEmptyTagsListItemBindingImpl.onFieldChange(int,Object,int)Z` | OPEN | Generated implementation absent; field-change dispatch unresolved. |
| 13 | `DrawerEmptyTagsListItemBindingImpl.setVariable(int,Object)Z` | OPEN | Generated implementation absent; variable dispatch unresolved. |
| 14 | `DrawerNoTagsListItemBinding.<init>(Object,View,int,ImageView,TextView)V` | OPEN | Generated base binding absent; TagsAdapter inflation call and layout printed, constructor route unresolved. |
| 15 | `DrawerNoTagsListItemBindingImpl.<clinit>()V` | OPEN | Generated implementation absent; initialization/delegate dispatch unavailable. |
| 16 | `DrawerNoTagsListItemBindingImpl.<init>(DataBindingComponent,View)V` | OPEN | Generated implementation absent; framework construction route unresolved. |
| 17 | `DrawerNoTagsListItemBindingImpl.<init>(DataBindingComponent,View,Object[])V` | OPEN | Generated implementation absent; framework construction route unresolved. |
| 18 | `DrawerNoTagsListItemBindingImpl.executeBindings()V` | OPEN | Generated implementation absent; Data Binding execution route unresolved. |
| 19 | `DrawerNoTagsListItemBindingImpl.hasPendingBindings()Z` | OPEN | Generated implementation absent; Data Binding query route unresolved. |
| 20 | `DrawerNoTagsListItemBindingImpl.invalidateAll()V` | OPEN | Generated implementation absent; invalidation dispatch unresolved. |
| 21 | `DrawerNoTagsListItemBindingImpl.onFieldChange(int,Object,int)Z` | OPEN | Generated implementation absent; field-change dispatch unresolved. |
| 22 | `DrawerNoTagsListItemBindingImpl.setVariable(int,Object)Z` | OPEN | Generated implementation absent; variable dispatch unresolved. |
| 23 | `DrawerTagsListItemBinding.<init>(Object,View,int,ColorView,ImageButton,TextView)V` | OPEN | Generated base binding absent; TagsAdapter inflation/click context and layout printed. |
| 24 | `DrawerTagsListItemBindingImpl.<clinit>()V` | OPEN | Generated implementation absent; initialization/delegate dispatch unavailable. |
| 25 | `DrawerTagsListItemBindingImpl.<init>(DataBindingComponent,View)V` | OPEN | Generated implementation absent; framework construction route unresolved. |
| 26 | `DrawerTagsListItemBindingImpl.<init>(DataBindingComponent,View,Object[])V` | OPEN | Generated implementation absent; framework construction route unresolved. |
| 27 | `DrawerTagsListItemBindingImpl.executeBindings()V` | OPEN | Generated implementation absent; Data Binding execution route unresolved. |
| 28 | `DrawerTagsListItemBindingImpl.hasPendingBindings()Z` | OPEN | Generated implementation absent; Data Binding query route unresolved. |
| 29 | `DrawerTagsListItemBindingImpl.invalidateAll()V` | OPEN | Generated implementation absent; invalidation dispatch unresolved. |
| 30 | `DrawerTagsListItemBindingImpl.onFieldChange(int,Object,int)Z` | OPEN | Generated implementation absent; field-change dispatch unresolved. |
| 31 | `DrawerTagsListItemBindingImpl.setVariable(int,Object)Z` | OPEN | Generated implementation absent; variable dispatch unresolved. |
| 32 | `FragmentAddTorrentFilesBinding.<init>(Object,View,int,RecyclerView,TextView,TextView,ContentLoadingProgressBar,LinearLayout)V` | OPEN | Generated base binding absent; fragment inflation call and layout printed. |
| 33 | `FragmentAddTorrentFilesBinding.getViewModel()AddTorrentViewModel` | OPEN | Generated base binding absent; generated getter implementation unavailable. |
| 34 | `FragmentAddTorrentFilesBindingImpl.<clinit>()V` | OPEN | Generated implementation absent; initialization/delegate dispatch unavailable. |
| 35 | `FragmentAddTorrentFilesBindingImpl.<init>(DataBindingComponent,View)V` | OPEN | Generated implementation absent; framework construction route unresolved. |
| 36 | `FragmentAddTorrentFilesBindingImpl.<init>(DataBindingComponent,View,Object[])V` | OPEN | Generated implementation absent; framework construction route unresolved. |
| 37 | `FragmentAddTorrentFilesBindingImpl.executeBindings()V` | OPEN | Generated implementation absent; Data Binding execution route unresolved. |
| 38 | `FragmentAddTorrentFilesBindingImpl.hasPendingBindings()Z` | OPEN | Generated implementation absent; Data Binding query route unresolved. |
| 39 | `FragmentAddTorrentFilesBindingImpl.invalidateAll()V` | OPEN | Generated implementation absent; invalidation dispatch unresolved. |
| 40 | `FragmentAddTorrentFilesBindingImpl.onChangeViewModelInfo(ObservableField,int)Z` | OPEN | Generated implementation absent; observable change dispatch unresolved. |

Count: 40 plan rows = 40 OPEN, 0 REACHABLE labels, 0 UNREACHABLE labels. No graph edits or coverage evidence were used.
