# LibreTorrent batch 80 source audit

Membership is exactly the 40 batch 80 rows printed at the top of `batch_080_helper_printed.txt`. Evidence is bounded to AddTorrentInfoFragment lifecycle, Activity Result launchers, tag/directory actions, AddTorrentMutableParams, activity initialization, and manifest/caller searches. I leave all rows OPEN because the fragment's complete route from an app entry through pager setup and each result/listener branch has not been verified end-to-end. Framework activity-result and lifecycle callback dispatch also need their route edges checked. No method is labeled unreachable based on absent call-site evidence.

| # | Method | Finding | Printed source / unresolved route |
|---:|---|---|---|
| 1 | `AddTorrentInfoFragment.lambda$new$1(ActivityResult)V` | OPEN | `AddTorrentInfoFragment.java:137+`; Activity Result callback body printed; registration/launch route unresolved. |
| 2 | `AddTorrentInfoFragment.lambda$new$2(ActivityResult)V` | OPEN | `AddTorrentInfoFragment.java:150+`; Activity Result callback body printed; registration/launch route unresolved. |
| 3 | `AddTorrentInfoFragment.lambda$onViewCreated$0(View)V` | OPEN | `AddTorrentInfoFragment.java:105+`; folder click callback body printed; fragment entry/view route unresolved. |
| 4 | `AddTorrentInfoFragment.newInstance()AddTorrentInfoFragment` | OPEN | `AddTorrentInfoFragment.java:74+`; factory and activity setup printed; complete pager/activity route unresolved. |
| 5 | `AddTorrentInfoFragment.onAttach(Context)V` | OPEN | `AddTorrentInfoFragment.java:84+`; lifecycle override printed; framework callback route unresolved. |
| 6 | `AddTorrentInfoFragment.onCreateView(LayoutInflater,ViewGroup,Bundle)View` | OPEN | `AddTorrentInfoFragment.java:92+`; inflation body printed; complete fragment navigation route unresolved. |
| 7 | `AddTorrentInfoFragment.onStart()V` | OPEN | `AddTorrentInfoFragment.java:124+`; lifecycle/tag subscription setup printed; framework callback and event route unresolved. |
| 8 | `AddTorrentInfoFragment.onStop()V` | OPEN | `AddTorrentInfoFragment.java:131+`; lifecycle cleanup printed; framework callback route unresolved. |
| 9 | `AddTorrentInfoFragment.onViewCreated(View,Bundle)V` | OPEN | `AddTorrentInfoFragment.java:99+`; listener setup body printed; complete fragment entry route unresolved. |
| 10 | `AddTorrentInfoFragment.showChooseDirDialog()V` | OPEN | `AddTorrentInfoFragment.java:192+`; view callback/use printed; complete UI/result path unresolved. |
| 11 | `AddTorrentInfoFragment.showOpenDirErrorDialog()V` | OPEN | `AddTorrentInfoFragment.java:215+`; result callback caller printed; full URI result route unresolved. |
| 12 | `AddTorrentInfoFragment.subscribeTags()V` | OPEN | `AddTorrentInfoFragment.java:186+`; Rx subscription body printed; `onStart`/event delivery route unresolved. |
| 13 | `AddTorrentInfoFragment$1.<init>(AddTorrentInfoFragment)V` | OPEN | TextWatcher creation printed; registration and text-input parent route unresolved. |
| 14 | `AddTorrentInfoFragment$1.afterTextChanged(Editable)V` | OPEN | TextWatcher callback body printed; framework text-change dispatch route unresolved. |
| 15 | `AddTorrentInfoFragment$1.beforeTextChanged(CharSequence,int,int,int)V` | OPEN | TextWatcher callback body printed; framework text-change dispatch route unresolved. |
| 16 | `AddTorrentInfoFragment$1.onTextChanged(CharSequence,int,int,int)V` | OPEN | TextWatcher callback body printed; framework text-change dispatch route unresolved. |
| 17 | `AddTorrentInfoFragment$2.<init>(AddTorrentInfoFragment)V` | OPEN | Tag-list listener construction printed; adapter registration and fragment route unresolved. |
| 18 | `AddTorrentInfoFragment$2.lambda$onAddTagClick$0(TagInfo)Long` | OPEN | Rx mapping lambda body printed; tag click and Rx execution route unresolved. |
| 19 | `AddTorrentInfoFragment$2.lambda$onAddTagClick$1(List)V` | OPEN | Rx completion lambda body printed; subscription and tag-click route unresolved. |
| 20 | `AddTorrentInfoFragment$2.onAddTagClick()V` | OPEN | Listener method and source search printed; complete fragment/listener entry route unresolved. |
| 21 | `AddTorrentInfoFragment$2.onTagRemoved(TagInfo)V` | OPEN | Listener method and source search printed; adapter callback route unresolved. |
| 22 | `AddTorrentMutableParams.<init>()V` | OPEN | `AddTorrentMutableParams.java` constructor/state source printed; view-model/activity route unresolved. |
| 23 | `AddTorrentMutableParams.getDirName()String` | OPEN | `AddTorrentMutableParams.java:83+`; accessor and callers printed; complete UI route unresolved. |
| 24 | `AddTorrentMutableParams.getDirPath()ObservableField` | OPEN | `AddTorrentMutableParams.java:77+`; observable accessor and callers printed; complete UI route unresolved. |
| 25 | `AddTorrentMutableParams.getName()String` | OPEN | `AddTorrentMutableParams.java:66+`; accessor and callers printed; complete activity route unresolved. |
| 26 | `AddTorrentMutableParams.getSource()String` | OPEN | `AddTorrentMutableParams.java:45+`; accessor and callers printed; complete activity route unresolved. |
| 27 | `AddTorrentMutableParams.getStorageFreeSpace()long` | OPEN | `AddTorrentMutableParams.java:95+`; accessor and callers printed; complete filesystem/UI route unresolved. |
| 28 | `AddTorrentMutableParams.isFirstLastPiecePriority()Z` | OPEN | `AddTorrentMutableParams.java:143+`; accessor and callers printed; complete UI/activity route unresolved. |
| 29 | `AddTorrentMutableParams.isFromMagnet()Z` | OPEN | `AddTorrentMutableParams.java:55+`; accessor and callers printed; incoming-intent route unresolved. |
| 30 | `AddTorrentMutableParams.isIgnoreFreeSpace()Z` | OPEN | `AddTorrentMutableParams.java:131+`; accessor and callers printed; complete UI/activity route unresolved. |
| 31 | `AddTorrentMutableParams.isSequentialDownload()Z` | OPEN | `AddTorrentMutableParams.java:107+`; accessor and callers printed; complete UI/activity route unresolved. |
| 32 | `AddTorrentMutableParams.isStartAfterAdd()Z` | OPEN | `AddTorrentMutableParams.java:119+`; accessor and callers printed; complete UI/activity route unresolved. |
| 33 | `AddTorrentMutableParams.setDirName(String)V` | OPEN | `AddTorrentMutableParams.java:88+`; setter and callers printed; complete UI input route unresolved. |
| 34 | `AddTorrentMutableParams.setFirstLastPiecePriority(boolean)V` | OPEN | `AddTorrentMutableParams.java:148+`; setter and callers printed; complete UI input route unresolved. |
| 35 | `AddTorrentMutableParams.setFromMagnet(boolean)V` | OPEN | `AddTorrentMutableParams.java:60+`; setter and callers printed; incoming-intent route unresolved. |
| 36 | `AddTorrentMutableParams.setIgnoreFreeSpace(boolean)V` | OPEN | `AddTorrentMutableParams.java:136+`; setter and callers printed; complete UI input route unresolved. |
| 37 | `AddTorrentMutableParams.setName(String)V` | OPEN | `AddTorrentMutableParams.java:71+`; setter and callers printed; complete UI input route unresolved. |
| 38 | `AddTorrentMutableParams.setSequentialDownload(boolean)V` | OPEN | `AddTorrentMutableParams.java:112+`; setter and callers printed; complete UI input route unresolved. |
| 39 | `AddTorrentMutableParams.setSource(String)V` | OPEN | `AddTorrentMutableParams.java:50+`; setter and callers printed; complete activity/intent route unresolved. |
| 40 | `AddTorrentMutableParams.setStartAfterAdd(boolean)V` | OPEN | `AddTorrentMutableParams.java:124+`; setter and callers printed; complete UI input route unresolved. |

Count: 40 plan rows = 40 OPEN, 0 REACHABLE labels, 0 UNREACHABLE labels. No graph edits or coverage evidence were used.
