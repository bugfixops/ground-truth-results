# LibreTorrent batch 60 source audit

Membership is exactly the 40 batch 60 rows printed at the top of `batch_060_helper_printed.txt`. Evidence is bounded to the direct activity/dialog binding setup, relevant layout XML (including the detail app-bar include), binding invocation search, and source-tree inventories for the generated Java binding classes. The generated `AddTorrentInfoBindingImpl`, `DetailTorrentAppbarBinding*`, and `DialogAddFeedChannelBinding*` implementations are absent from the uploaded Java source, so all 40 rows remain OPEN. XML and app-side `DataBindingUtil` calls show context, but do not provide the missing generated dispatch bodies or a complete route. No missing generated file is used as proof of unreachability.

| # | Method | Finding | Printed evidence / unresolved route |
|---:|---|---|---|
| 1 | `AddTorrentInfoBindingImpl$4.onChange()V` | OPEN | Source search shows generated binding class absent; observable callback body and dispatch unavailable. |
| 2 | `AddTorrentInfoBindingImpl$5.<init>(AddTorrentInfoBindingImpl)V` | OPEN | Generated implementation source absent; callback construction route unavailable. |
| 3 | `AddTorrentInfoBindingImpl$5.onChange()V` | OPEN | Generated implementation source absent; observable callback dispatch unavailable. |
| 4 | `DetailTorrentAppbarBinding.<init>(Object,View,int,TabLayout,Toolbar)V` | OPEN | Generated base binding source absent; `fragment_detail_torrent` include printed, full binding route unresolved. |
| 5 | `DetailTorrentAppbarBindingImpl.<clinit>()V` | OPEN | Generated source inventory has no uploaded class; initialization/delegate dispatch unavailable. |
| 6 | `DetailTorrentAppbarBindingImpl.<init>(DataBindingComponent,View)V` | OPEN | Generated source absent; framework binding construction dispatch unresolved. |
| 7 | `DetailTorrentAppbarBindingImpl.<init>(DataBindingComponent,View,Object[])V` | OPEN | Generated source absent; framework binding construction dispatch unresolved. |
| 8 | `DetailTorrentAppbarBindingImpl.executeBindings()V` | OPEN | Generated source absent; Data Binding execution route unresolved. |
| 9 | `DetailTorrentAppbarBindingImpl.hasPendingBindings()Z` | OPEN | Generated source absent; Data Binding query route unresolved. |
| 10 | `DetailTorrentAppbarBindingImpl.invalidateAll()V` | OPEN | Generated source absent; invalidation dispatch unresolved. |
| 11 | `DetailTorrentAppbarBindingImpl.onFieldChange(int,Object,int)Z` | OPEN | Generated source absent; observable field-change dispatch unresolved. |
| 12 | `DetailTorrentAppbarBindingImpl.setVariable(int,Object)Z` | OPEN | Generated source absent; generated variable dispatch unresolved. |
| 13 | `DetailTorrentAppbarBindingLargeLandNotouchImpl.<clinit>()V` | OPEN | Generated variant source absent; initialization/delegate dispatch unavailable. |
| 14 | `DetailTorrentAppbarBindingLargeLandNotouchImpl.<init>(DataBindingComponent,View)V` | OPEN | Generated variant source absent; framework construction route unresolved. |
| 15 | `DetailTorrentAppbarBindingLargeLandNotouchImpl.<init>(DataBindingComponent,View,Object[])V` | OPEN | Generated variant source absent; framework construction route unresolved. |
| 16 | `DetailTorrentAppbarBindingLargeLandNotouchImpl.executeBindings()V` | OPEN | Generated variant source absent; Data Binding execution route unresolved. |
| 17 | `DetailTorrentAppbarBindingLargeLandNotouchImpl.hasPendingBindings()Z` | OPEN | Generated variant source absent; Data Binding query route unresolved. |
| 18 | `DetailTorrentAppbarBindingLargeLandNotouchImpl.invalidateAll()V` | OPEN | Generated variant source absent; invalidation dispatch unresolved. |
| 19 | `DetailTorrentAppbarBindingLargeLandNotouchImpl.onFieldChange(int,Object,int)Z` | OPEN | Generated variant source absent; observable field-change dispatch unresolved. |
| 20 | `DetailTorrentAppbarBindingLargeLandNotouchImpl.setVariable(int,Object)Z` | OPEN | Generated variant source absent; generated variable dispatch unresolved. |
| 21 | `DetailTorrentAppbarBindingSw600dpLandImpl.<clinit>()V` | OPEN | Generated variant source absent; initialization/delegate dispatch unavailable. |
| 22 | `DetailTorrentAppbarBindingSw600dpLandImpl.<init>(DataBindingComponent,View)V` | OPEN | Generated variant source absent; framework construction route unresolved. |
| 23 | `DetailTorrentAppbarBindingSw600dpLandImpl.<init>(DataBindingComponent,View,Object[])V` | OPEN | Generated variant source absent; framework construction route unresolved. |
| 24 | `DetailTorrentAppbarBindingSw600dpLandImpl.executeBindings()V` | OPEN | Generated variant source absent; Data Binding execution route unresolved. |
| 25 | `DetailTorrentAppbarBindingSw600dpLandImpl.hasPendingBindings()Z` | OPEN | Generated variant source absent; Data Binding query route unresolved. |
| 26 | `DetailTorrentAppbarBindingSw600dpLandImpl.invalidateAll()V` | OPEN | Generated variant source absent; invalidation dispatch unresolved. |
| 27 | `DetailTorrentAppbarBindingSw600dpLandImpl.onFieldChange(int,Object,int)Z` | OPEN | Generated variant source absent; observable field-change dispatch unresolved. |
| 28 | `DetailTorrentAppbarBindingSw600dpLandImpl.setVariable(int,Object)Z` | OPEN | Generated variant source absent; generated variable dispatch unresolved. |
| 29 | `DialogAddFeedChannelBinding.<init>(Object,View,int,CheckBox,ImageButton,View,CheckBox,ExpandableLayout,TextInputEditText,TextInputLayout,TextInputLayout,TextInputLayout,TextInputEditText,TextInputEditText,CheckBox)V` | OPEN | Generated base binding source absent; `AddFeedDialog` inflation call and XML printed, generated constructor route unresolved. |
| 30 | `DialogAddFeedChannelBinding.getViewModel()AddFeedViewModel` | OPEN | Generated base binding source absent; Data Binding getter implementation unavailable. |
| 31 | `DialogAddFeedChannelBindingImpl.<clinit>()V` | OPEN | Generated implementation source absent; initialization/delegate dispatch unavailable. |
| 32 | `DialogAddFeedChannelBindingImpl.<init>(DataBindingComponent,View)V` | OPEN | Generated implementation source absent; framework binding construction route unresolved. |
| 33 | `DialogAddFeedChannelBindingImpl.<init>(DataBindingComponent,View,Object[])V` | OPEN | Generated implementation source absent; framework binding construction route unresolved. |
| 34 | `DialogAddFeedChannelBindingImpl.executeBindings()V` | OPEN | Generated implementation source absent; Data Binding execution route unresolved. |
| 35 | `DialogAddFeedChannelBindingImpl.hasPendingBindings()Z` | OPEN | Generated implementation source absent; Data Binding query route unresolved. |
| 36 | `DialogAddFeedChannelBindingImpl.invalidateAll()V` | OPEN | Generated implementation source absent; invalidation dispatch unresolved. |
| 37 | `DialogAddFeedChannelBindingImpl.onChangeViewModelMutableParams(AddFeedMutableParams,int)Z` | OPEN | Generated implementation source absent; observable change dispatch unresolved. |
| 38 | `DialogAddFeedChannelBindingImpl.onChangeViewModelShowClipboardButton(ObservableBoolean,int)Z` | OPEN | Generated implementation source absent; observable change dispatch unresolved. |
| 39 | `DialogAddFeedChannelBindingImpl.onFieldChange(int,Object,int)Z` | OPEN | Generated implementation source absent; field-change dispatch unresolved. |
| 40 | `DialogAddFeedChannelBindingImpl.setVariable(int,Object)Z` | OPEN | Generated implementation source absent; generated variable dispatch unresolved. |

Count: 40 plan rows = 40 OPEN, 0 REACHABLE labels, 0 UNREACHABLE labels. No graph edits or coverage evidence were used.
