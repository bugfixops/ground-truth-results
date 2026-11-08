# LibreTorrent batch 58 source audit

Membership is exactly the 40 rows printed at the top of `batch_058_helper_printed.txt`. Evidence includes all of `Utils.java`, the two activity sources and their layouts, source-root caller searches, and searches for generated binding Java. The generated `ActivityAddTorrentBinding*` and `ActivityFilemanagerDialogBinding*` sources are absent from the uploaded source tree; those methods remain OPEN rather than being inferred from Data Binding behavior. The Utils methods also remain OPEN because complete app-entry paths, including framework/runtime permission and service conditions, were not traced end-to-end. No missing call-site match is treated as proof of unreachability.

| # | Method | Finding | Printed source / unresolved route |
|---:|---|---|---|
| 1 | `Utils.isMetered(Context)boolean` | OPEN | `Utils.java` body and callers printed; complete network/settings entry route unresolved. |
| 2 | `Utils.isNetworkTypeAllowed(Context)boolean` | OPEN | `Utils.java` body and callers printed; full settings/network route unresolved. |
| 3 | `Utils.isRoaming(Context)boolean` | OPEN | `Utils.java` body and callers printed; framework/network query path unresolved. |
| 4 | `Utils.isSafPath(Context,Uri)boolean` | OPEN | `Utils.java` body and callers printed; complete URI-origin route unresolved. |
| 5 | `Utils.isTwoPane(Context)boolean` | OPEN | `Utils.java` body and callers printed; full UI caller route unresolved. |
| 6 | `Utils.isValidTrackerUrl(String)boolean` | OPEN | `Utils.java` body and callers printed; complete add/edit tracker route unresolved. |
| 7 | `Utils.lambda$startServiceBackground$0(Context,Intent)V` | OPEN | Lambda source printed; API-level/service dispatch path not fully traced. |
| 8 | `Utils.makeSha1Hash(String)String` | OPEN | `Utils.java` body and callers printed; complete caller route unresolved. |
| 9 | `Utils.normalizeMagnetHash(String)String` | OPEN | `Utils.java` body and callers printed; complete magnet input route unresolved. |
| 10 | `Utils.reportError(Throwable,String)V` | OPEN | `Utils.java` body and callers printed; full error-handler entry route unresolved. |
| 11 | `Utils.requestExactAlarmPermission(Context)V` | OPEN | `Utils.java` body and callers printed; API-level/UI permission flow unresolved. |
| 12 | `Utils.setBackground(View,Drawable)V` | OPEN | `Utils.java` body and callers printed; complete view lifecycle route unresolved. |
| 13 | `Utils.shouldRequestStoragePermission(Activity)boolean` | OPEN | `Utils.java` body and callers printed; complete activity/API-level route unresolved. |
| 14 | `Utils.showActionModeStatusBar(Activity,boolean)V` | OPEN | `Utils.java` body and callers printed; complete action-mode UI route unresolved. |
| 15 | `Utils.showManageAllFilesWarningDialog(Context,FragmentManager)V` | OPEN | `Utils.java` body and callers printed; full UI/permission route unresolved. |
| 16 | `Utils.startServiceBackground(Context,Intent)V` | OPEN | `Utils.java` body and callers printed; complete service-start entry path unresolved. |
| 17 | `Utils$1.<init>(byte[][],ArrayList)V` | OPEN | Anonymous callback construction printed in `Utils.java`; complete request call chain unresolved. |
| 18 | `Utils$1.onConnectionCreated(HttpURLConnection)V` | OPEN | Callback body printed; HTTP library callback dispatch route unresolved. |
| 19 | `Utils$1.onIOException(IOException)V` | OPEN | Callback body printed; HTTP library callback dispatch route unresolved. |
| 20 | `Utils$1.onMovedPermanently(String)V` | OPEN | Callback body printed; HTTP redirect callback dispatch route unresolved. |
| 21 | `Utils$1.onResponseHandle(HttpURLConnection,int,String)V` | OPEN | Callback body printed; HTTP response callback dispatch route unresolved. |
| 22 | `Utils$1.onTooManyRedirects()V` | OPEN | Callback body printed; HTTP redirect callback dispatch route unresolved. |
| 23 | `Utils$2.<init>(X509TrustManager)V` | OPEN | Anonymous trust-manager construction printed; complete TLS setup/use path unresolved. |
| 24 | `Utils$2.checkClientTrusted(X509Certificate[],String)V` | OPEN | Trust callback body printed; TLS provider invocation path unresolved. |
| 25 | `Utils$2.checkServerTrusted(X509Certificate[],String)V` | OPEN | Trust callback body printed; TLS provider invocation path unresolved. |
| 26 | `Utils$2.getAcceptedIssuers()X509Certificate[]` | OPEN | Trust callback body printed; TLS provider invocation path unresolved. |
| 27 | `ActivityAddTorrentBinding.<init>(Object,View,int,AppBarLayout,CoordinatorLayout,ProgressBar,TabLayout,Toolbar,ViewPager2)V` | OPEN | Generated binding source search has no uploaded match; constructor route unresolved. |
| 28 | `ActivityAddTorrentBindingImpl.<clinit>()V` | OPEN | Generated binding source absent; initialization/delegate dispatch unavailable for source confirmation. |
| 29 | `ActivityAddTorrentBindingImpl.<init>(DataBindingComponent,View)V` | OPEN | Generated binding source absent; framework binding construction route unresolved. |
| 30 | `ActivityAddTorrentBindingImpl.<init>(DataBindingComponent,View,Object[])V` | OPEN | Generated binding source absent; framework binding construction route unresolved. |
| 31 | `ActivityAddTorrentBindingImpl.executeBindings()V` | OPEN | Generated binding source absent; Data Binding execution dispatch unresolved. |
| 32 | `ActivityAddTorrentBindingImpl.hasPendingBindings()boolean` | OPEN | Generated binding source absent; Data Binding execution dispatch unresolved. |
| 33 | `ActivityAddTorrentBindingImpl.invalidateAll()V` | OPEN | Generated binding source absent; Data Binding invalidation dispatch unresolved. |
| 34 | `ActivityAddTorrentBindingImpl.onFieldChange(int,Object,int)boolean` | OPEN | Generated binding source absent; observable field-change dispatch unresolved. |
| 35 | `ActivityAddTorrentBindingImpl.setVariable(int,Object)boolean` | OPEN | Generated binding source absent; generated variable dispatch unresolved. |
| 36 | `ActivityFilemanagerDialogBinding.<init>(Object,View,int,FloatingActionButton,AppBarLayout,FrameLayout,CoordinatorLayout,RecyclerView,TextInputEditText,TextInputLayout,Spinner,ThemedSwipeRefreshLayout,Toolbar)V` | OPEN | Generated binding source search has no uploaded match; constructor route unresolved. |
| 37 | `ActivityFilemanagerDialogBinding.getViewModel()FileManagerViewModel` | OPEN | Generated binding source absent; Data Binding view-model getter route unresolved. |
| 38 | `ActivityFilemanagerDialogBindingImpl.<clinit>()V` | OPEN | Generated binding source absent; initialization/delegate dispatch unavailable for source confirmation. |
| 39 | `ActivityFilemanagerDialogBindingImpl.<init>(DataBindingComponent,View)V` | OPEN | Generated binding source absent; framework binding construction route unresolved. |
| 40 | `ActivityFilemanagerDialogBindingImpl.<init>(DataBindingComponent,View,Object[])V` | OPEN | Generated binding source absent; framework binding construction route unresolved. |

Count: 40 plan rows = 40 OPEN, 0 REACHABLE labels, 0 UNREACHABLE labels. No graph edits or coverage evidence were used.
