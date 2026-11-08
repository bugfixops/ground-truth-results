# LibreTorrent batch 82 source audit

Membership is exactly the 40 batch 82 rows printed at the top of `batch_082_helper_printed.txt`. Bounded evidence includes AddTorrentViewModel decode-state/task code, Parcelable file item, list adapter, CreateTorrentActivity lifecycle/result handlers, CreateTorrentDialog class context, and caller/manifest searches. All rows remain OPEN because the complete input intent to decode task to UI/activity route and all framework callback/Parcelable dispatch links have not been traced end-to-end. Local calls and method bodies alone do not establish those full routes. No missing caller match is treated as proof of unreachability.

| # | Method | Finding | Printed source / unresolved route |
|---:|---|---|---|
| 1 | `AddTorrentViewModel$DecodeState.<init>(Status)V` | OPEN | `AddTorrentViewModel.java:114+`; state constructor printed; producer/callback route unresolved. |
| 2 | `AddTorrentViewModel$DecodeState.<init>(Status,Throwable)V` | OPEN | `AddTorrentViewModel.java:114+`; error-state constructor printed; decode error route unresolved. |
| 3 | `AddTorrentViewModel$Status.<clinit>()V` | OPEN | Enum declaration/constants printed; initialization through app input route not traced. |
| 4 | `AddTorrentViewModel$TorrentDecodeTask.<init>(AddTorrentViewModel)V` | OPEN | AsyncTask construction and surrounding task source printed; complete activity/decode route unresolved. |
| 5 | `AddTorrentViewModel$TorrentDecodeTask.doInBackground(Uri[])Throwable` | OPEN | `AddTorrentViewModel.java:217+`; background branches printed; incoming intent/data-origin route unresolved. |
| 6 | `AddTorrentViewModel$TorrentDecodeTask.onPostExecute(Throwable)V` | OPEN | `AddTorrentViewModel.java:301+`; callback body printed; AsyncTask framework dispatch route unresolved. |
| 7 | `AddTorrentViewModel$TorrentDecodeTask.onPreExecute()V` | OPEN | `AddTorrentViewModel.java:212+`; callback body printed; AsyncTask framework dispatch route unresolved. |
| 8 | `AddTorrentViewModel$TorrentDecodeTask.readTorrentFile(Uri)V` | OPEN | `AddTorrentViewModel.java:281+`; helper body printed; complete URI-origin and task entry route unresolved. |
| 9 | `DownloadableFileItem.<clinit>()V` | OPEN | `DownloadableFileItem.java` Parcelable source printed; initialization through app route not traced. |
| 10 | `DownloadableFileItem.<init>(Parcel)V` | OPEN | Parcelable constructor body printed; framework Parcel dispatch route unresolved. |
| 11 | `DownloadableFileItem.<init>(BencodeFileTree)V` | OPEN | Constructor body printed; complete decode-to-adapter route unresolved. |
| 12 | `DownloadableFileItem.describeContents()I` | OPEN | Parcelable method body printed; framework Parcel route unresolved. |
| 13 | `DownloadableFileItem.toString()String` | OPEN | Method body printed; caller route unresolved. |
| 14 | `DownloadableFileItem.writeToParcel(Parcel,int)V` | OPEN | Parcelable body printed; framework Parcel dispatch route unresolved. |
| 15 | `DownloadableFileItem$1.<init>()V` | OPEN | Parcelable `CREATOR` anonymous implementation printed; framework creation route unresolved. |
| 16 | `DownloadableFileItem$1.createFromParcel(Parcel)DownloadableFileItem` | OPEN | `CREATOR` callback body printed; Parcel framework dispatch unresolved. |
| 17 | `DownloadableFileItem$1.newArray(int)DownloadableFileItem[]` | OPEN | `CREATOR` callback body printed; Parcel framework dispatch unresolved. |
| 18 | `DownloadableFilesAdapter.<clinit>()V` | OPEN | Adapter source/static setup printed; initialization from fragment/list route unresolved. |
| 19 | `DownloadableFilesAdapter.<init>(ClickListener)V` | OPEN | Adapter constructor and fragment caller search printed; complete fragment entry route unresolved. |
| 20 | `DownloadableFilesAdapter.onBindViewHolder(ViewHolder,int)V` | OPEN | Adapter binding source printed; RecyclerView callback dispatch and list route unresolved. |
| 21 | `DownloadableFilesAdapter.onCreateViewHolder(ViewGroup,int)ViewHolder` | OPEN | Adapter source and binding inflation printed; RecyclerView callback dispatch unresolved. |
| 22 | `DownloadableFilesAdapter$1.<init>()V` | OPEN | Diff callback source printed; adapter/AsyncListDiffer construction route unresolved. |
| 23 | `DownloadableFilesAdapter$1.areContentsTheSame(DownloadableFileItem,DownloadableFileItem)Z` | OPEN | Diff callback body printed; list-diff library invocation route unresolved. |
| 24 | `DownloadableFilesAdapter$1.areItemsTheSame(DownloadableFileItem,DownloadableFileItem)Z` | OPEN | Diff callback body printed; list-diff library invocation route unresolved. |
| 25 | `DownloadableFilesAdapter$ViewHolder.<init>(ItemTorrentDownloadableFileBinding)V` | OPEN | View-holder constructor printed; RecyclerView creation callback route unresolved. |
| 26 | `DownloadableFilesAdapter$ViewHolder.bind(DownloadableFileItem,ClickListener)V` | OPEN | Bind body printed; adapter/list-to-view-holder path unresolved. |
| 27 | `DownloadableFilesAdapter$ViewHolder.lambda$bind$0(DownloadableFileItem,ClickListener,View)V` | OPEN | Click lambda body printed; Android view event dispatch route unresolved. |
| 28 | `DownloadableFilesAdapter$ViewHolder.lambda$bind$1(ClickListener,DownloadableFileItem,View)V` | OPEN | Click lambda body printed; Android view event dispatch route unresolved. |
| 29 | `CreateTorrentActivity.<init>()V` | OPEN | Activity class/constructor context printed; Android activity instantiation route unresolved. |
| 30 | `CreateTorrentActivity.lambda$subscribeAlertDialog$0(BaseAlertDialog.Event)V` | OPEN | Rx event handler source printed; observer subscription and dialog event path unresolved. |
| 31 | `CreateTorrentActivity.onBackPressed()V` | OPEN | `CreateTorrentActivity.java:136+`; override body printed; framework/back dispatcher route unresolved. |
| 32 | `CreateTorrentActivity.onCreate(Bundle)V` | OPEN | `CreateTorrentActivity.java:55+`; activity setup/results printed; app entry/manifest route unresolved. |
| 33 | `CreateTorrentActivity.onFragmentFinished(Fragment,Intent,ResultCode)V` | OPEN | Callback body and dialog context printed; fragment-to-activity callback registration route unresolved. |
| 34 | `CreateTorrentActivity.onStart()V` | OPEN | `CreateTorrentActivity.java:96+`; event subscription setup printed; framework callback route unresolved. |
| 35 | `CreateTorrentActivity.onStop()V` | OPEN | `CreateTorrentActivity.java:103+`; cleanup body printed; framework callback route unresolved. |
| 36 | `CreateTorrentActivity.subscribeAlertDialog()V` | OPEN | Subscription body printed; event source and lifecycle entry path unresolved. |
| 37 | `CreateTorrentActivity$1.<init>(CreateTorrentActivity,FragmentManager)V` | OPEN | Permission-result listener construction printed in activity setup; registration and permission result route unresolved. |
| 38 | `CreateTorrentActivity$1.onNotificationResult(boolean,boolean)V` | OPEN | Permission callback body printed; permission request/result framework route unresolved. |
| 39 | `CreateTorrentActivity$1.onStorageResult(boolean,boolean)V` | OPEN | Permission callback body printed; storage request/result framework route unresolved. |
| 40 | `CreateTorrentDialog.<clinit>()V` | OPEN | `CreateTorrentDialog.java` class/static context printed; creation/navigation route unresolved. |

Count: 40 plan rows = 40 OPEN, 0 REACHABLE labels, 0 UNREACHABLE labels. No graph edits or coverage evidence were used.
