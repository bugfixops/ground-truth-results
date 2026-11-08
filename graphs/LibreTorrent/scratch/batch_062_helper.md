# LibreTorrent batch 62 source audit

Membership is exactly the 40 plan rows printed at the top of `batch_062_helper_printed.txt`. Evidence is bounded to the four dialog inflation call sites, corresponding layout XML files, binding call-site search, and generated binding source inventory. The generated `DialogAddTagBinding*`, `DialogCreateTorrentBinding*`, `DialogErrorBinding*`, and `DialogGoToFolderBinding*` Java sources are not present in the uploaded tree. Their methods remain OPEN; the app-side inflation and XML context do not include the generated binding implementations or full dispatch behavior. No missing generated source is used as proof of unreachability.

| # | Method | Finding | Printed evidence / unresolved route |
|---:|---|---|---|
| 1 | `DialogAddTagBindingImpl$1.<init>(DialogAddTagBindingImpl)V` | OPEN | Generated binding source search has no uploaded match; observable callback construction unavailable. |
| 2 | `DialogAddTagBindingImpl$1.onChange()V` | OPEN | Generated binding source absent; observable callback body/dispatch unavailable. |
| 3 | `DialogCreateTorrentBinding.<init>(Object,View,int,FixHintTextInputEditText,ProgressBar,ImageButton,TextInputEditText,ImageButton,TextInputLayout,TextInputLayout,TextInputLayout,TextInputLayout,TextInputLayout,Spinner,CheckBox,FixHintTextInputEditText,CheckBox,Spinner,FixHintTextInputEditText,FixHintTextInputEditText)V` | OPEN | Generated base binding source absent; create dialog inflation/layout context printed, constructor route unresolved. |
| 4 | `DialogCreateTorrentBinding.getViewModel()CreateTorrentViewModel` | OPEN | Generated binding source absent; view-model getter implementation unavailable. |
| 5 | `DialogCreateTorrentBindingImpl.<clinit>()V` | OPEN | Generated implementation absent; initialization/delegate dispatch unavailable. |
| 6 | `DialogCreateTorrentBindingImpl.<init>(DataBindingComponent,View)V` | OPEN | Generated implementation absent; framework construction dispatch unresolved. |
| 7 | `DialogCreateTorrentBindingImpl.<init>(DataBindingComponent,View,Object[])V` | OPEN | Generated implementation absent; framework construction dispatch unresolved. |
| 8 | `DialogCreateTorrentBindingImpl.executeBindings()V` | OPEN | Generated implementation absent; Data Binding execution route unresolved. |
| 9 | `DialogCreateTorrentBindingImpl.hasPendingBindings()Z` | OPEN | Generated implementation absent; Data Binding query route unresolved. |
| 10 | `DialogCreateTorrentBindingImpl.invalidateAll()V` | OPEN | Generated implementation absent; invalidation dispatch unresolved. |
| 11 | `DialogCreateTorrentBindingImpl.onChangeViewModelBuildProgress(LiveData,int)Z` | OPEN | Generated implementation absent; observable change dispatch unresolved. |
| 12 | `DialogCreateTorrentBindingImpl.onChangeViewModelMutableParams(CreateTorrentMutableParams,int)Z` | OPEN | Generated implementation absent; observable change dispatch unresolved. |
| 13 | `DialogCreateTorrentBindingImpl.onChangeViewModelState(LiveData,int)Z` | OPEN | Generated implementation absent; observable change dispatch unresolved. |
| 14 | `DialogCreateTorrentBindingImpl.onFieldChange(int,Object,int)Z` | OPEN | Generated implementation absent; field-change dispatch unresolved. |
| 15 | `DialogCreateTorrentBindingImpl.setVariable(int,Object)Z` | OPEN | Generated implementation absent; generated variable dispatch unresolved. |
| 16 | `DialogCreateTorrentBindingImpl.setViewModel(CreateTorrentViewModel)V` | OPEN | Generated implementation absent; view-model setter dispatch unresolved. |
| 17 | `DialogCreateTorrentBindingImpl$1.<init>(DialogCreateTorrentBindingImpl)V` | OPEN | Generated observable wrapper source absent; callback construction unavailable. |
| 18 | `DialogCreateTorrentBindingImpl$1.onChange()V` | OPEN | Generated observable wrapper source absent; callback dispatch unavailable. |
| 19 | `DialogCreateTorrentBindingImpl$2.<init>(DialogCreateTorrentBindingImpl)V` | OPEN | Generated observable wrapper source absent; callback construction unavailable. |
| 20 | `DialogCreateTorrentBindingImpl$2.onChange()V` | OPEN | Generated observable wrapper source absent; callback dispatch unavailable. |
| 21 | `DialogCreateTorrentBindingImpl$3.<init>(DialogCreateTorrentBindingImpl)V` | OPEN | Generated observable wrapper source absent; callback construction unavailable. |
| 22 | `DialogCreateTorrentBindingImpl$3.onChange()V` | OPEN | Generated observable wrapper source absent; callback dispatch unavailable. |
| 23 | `DialogCreateTorrentBindingImpl$4.<init>(DialogCreateTorrentBindingImpl)V` | OPEN | Generated observable wrapper source absent; callback construction unavailable. |
| 24 | `DialogCreateTorrentBindingImpl$4.onChange()V` | OPEN | Generated observable wrapper source absent; callback dispatch unavailable. |
| 25 | `DialogCreateTorrentBindingImpl$5.<init>(DialogCreateTorrentBindingImpl)V` | OPEN | Generated observable wrapper source absent; callback construction unavailable. |
| 26 | `DialogCreateTorrentBindingImpl$5.onChange()V` | OPEN | Generated observable wrapper source absent; callback dispatch unavailable. |
| 27 | `DialogCreateTorrentBindingImpl$6.<init>(DialogCreateTorrentBindingImpl)V` | OPEN | Generated observable wrapper source absent; callback construction unavailable. |
| 28 | `DialogCreateTorrentBindingImpl$6.onChange()V` | OPEN | Generated observable wrapper source absent; callback dispatch unavailable. |
| 29 | `DialogErrorBinding.<init>(Object,View,int,TextInputEditText,TextView,View,View,ExpandableLayout,ExpansionHeader,TextInputLayout)V` | OPEN | Generated base binding source absent; error dialog inflation/layout context printed. |
| 30 | `DialogErrorBinding.getDetailError()String` | OPEN | Generated binding source absent; data getter implementation unavailable. |
| 31 | `DialogErrorBindingImpl.<clinit>()V` | OPEN | Generated implementation absent; initialization/delegate dispatch unavailable. |
| 32 | `DialogErrorBindingImpl.<init>(DataBindingComponent,View)V` | OPEN | Generated implementation absent; framework construction dispatch unresolved. |
| 33 | `DialogErrorBindingImpl.<init>(DataBindingComponent,View,Object[])V` | OPEN | Generated implementation absent; framework construction dispatch unresolved. |
| 34 | `DialogErrorBindingImpl.executeBindings()V` | OPEN | Generated implementation absent; Data Binding execution route unresolved. |
| 35 | `DialogErrorBindingImpl.hasPendingBindings()Z` | OPEN | Generated implementation absent; Data Binding query route unresolved. |
| 36 | `DialogErrorBindingImpl.invalidateAll()V` | OPEN | Generated implementation absent; invalidation dispatch unresolved. |
| 37 | `DialogErrorBindingImpl.onFieldChange(int,Object,int)Z` | OPEN | Generated implementation absent; field-change dispatch unresolved. |
| 38 | `DialogErrorBindingImpl.setDetailError(String)V` | OPEN | Generated implementation absent; generated property setter route unresolved. |
| 39 | `DialogErrorBindingImpl.setVariable(int,Object)Z` | OPEN | Generated implementation absent; generated variable dispatch unresolved. |
| 40 | `DialogGoToFolderBinding.<init>(Object,View,int,TextInputLayout,TextInputEditText)V` | OPEN | Generated base binding source absent; Go To Folder dialog inflation/layout context printed. |

Count: 40 plan rows = 40 OPEN, 0 REACHABLE labels, 0 UNREACHABLE labels. No graph edits or coverage evidence were used.
