# LibreTorrent batch 58 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** Build and C1 run on the user's Mac after a push, so they
are marked "not run" here, never passed. No sampler, full-repo grep, or C1 check was run
or is claimed in this file. No connector `search_code` 0-result was used as evidence of
absence. No row was flipped to UNREACHABLE: no saved full-repo grep exists.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 58 only, LibreTorrent labels only, no other batch/app, no device replay, no Aegis.
- Membership: exactly the 40 rows of batch 58 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`,
  local copy `~/workspace/agent27-plan.tsv`, plan SHA `0104806dd666c840049b3db52823d4b384fa1c92`,
  all `TODO_CANDIDATE_REACHABLE`, in plan order. Method names/descriptors checked against that copy.
- Prior proposal (`~/workspace/libretorrent-batch58-proposal.md`) was used as a lead list only;
  every row below was re-checked in this pass against the printed source listed below.

## Printed source in this pass

Fresh connector fetches from branch `work-2026-10-31`, one file at a time with pauses,
saved in `~/workspace/b565758-src/` (base
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`):
- `core/utils/Utils.java` (926 lines) — fresh definitions for all Utils rows; grep confirms no new
  caller for any OPEN Utils row beyond the internal callers already known.
- `ui/main/MainActivity.java` (811 lines) — fresh: :654, :677, :688, :808 `Utils.isTwoPane`;
  :180 `Utils.showManageAllFilesWarningDialog`; :137 `Utils.getAppTheme`.
- `ui/addtorrent/AddTorrentActivity.java` (577 lines) — fresh: :99 `Utils.getAppTheme`,
  :102 `DataBindingUtil.setContentView(this, R.layout.activity_add_torrent)`, :136
  `Utils.showManageAllFilesWarningDialog`; grep finds NO `setVariable` and NO `getViewModel` call
  in this file.
- `ui/filemanager/FileManagerDialog.java` (691 lines, an Activity despite the name) — fresh:
  :142 `DataBindingUtil.setContentView(this, R.layout.activity_filemanager_dialog)`, :143
  `binding.setViewModel(viewModel)`; grep finds NO `binding.getViewModel(...)` call in this file.
- `core/model/TorrentEngine.java` — fresh, upgrading previously carried engine citations:
  `checkPauseTorrents()` :1023-1043 with `isRoaming` :1033, `isMetered` :1035;
  `handleAutoStop` :143-146 → `forceStop()` :282-285 → `Utils.startServiceBackground` :285.
- `core/system/FsModuleResolverImpl.java` — fresh, upgrading the batch-55 carried citation:
  `resolveFsByUri` :42-49, `Utils.isSafPath(appContext, uri)` at :43.
- `core/utils/DateUtils.java`, `core/filter/TorrentFilterCollection.java`,
  `ui/detailtorrent/DetailTorrentFragment.java`, `ui/addtorrent/AddTorrentViewModel.java` — fresh,
  used for cross-batch checks only (no batch-58 row rests on them except where noted).

Still carried (NOT freshly printed this pass, flagged, merger must re-verify):
- `Utils.isNetworkTypeAllowed` upstream beyond `checkConnectivity`/`fetchHttpUrl` (batch 57 row 11,
  itself carried from batch 19). Row 2 rests on that chain.
- Who starts FileManagerDialog (startActivity site) — not printed; rows 36-40 are dialog-anchored
  (strict-entry caveat). Who starts AddTorrentActivity — carried from batch 77/78 (AddLinkDialog →
  startActivity → onCreate); the setContentView site itself is fresh here.

## Generated-binding convention (recorded, NOT decided)

Generated data-binding classes (`*Binding`, `*BindingImpl`) are NOT in `final_java_only`
(build-generated), so every Impl verdict is INFERRED, never SOURCE. This file follows the
batches 67-68 convention, aligned with the prior batch-58 proposal, and records the conflict
explicitly for the merger:
- Creation/rebind-flow methods are INFERRED REACHABLE once the binding is created by a printed
  `DataBindingUtil.setContentView` call (generated ctor calls `invalidateAll()`, the framework
  rebind flow then calls `executeBindings()`).
- Variable/observable-specific methods are OPEN unless a printed use exists: `hasPendingBindings`
  (no printed caller), `onFieldChange` / `setVariable` (no printed observable registration or
  variable assignment), and a generated getter such as `getViewModel` (no printed getter call —
  a printed *setter* call is not a getter call, and generated `executeBindings` reads the field
  directly, not via the getter).
- **CONVENTION CONFLICT, deliberately NOT decided here (batch 58 row 37):** batches 65-66 marked
  binding `getViewModel` getters REACHABLE via the generated `executeBindings` read path, while
  batches 58 (this file), 63-64 (Agent 21), and 59-60 (abstract `getViewModel`) left them OPEN
  because `executeBindings` reads the `mViewModel` field, not the getter. Row 37 below is therefore
  OPEN under the 58/63-64 convention and would flip to REACHABLE INFERRED under the 65-66 convention.
  The merger must pick ONE convention for all binding getters; do not mix them batch by batch.
  The same conflict does not affect rows 32/34/35, which are OPEN under both conventions on this
  evidence (no printed caller, no printed observable use, no printed variable assignment).

## Counts — mechanically verified

- **40 rows, sequence 1–40 intact, in plan order.**
- **24 REACHABLE proposed / 0 UNREACHABLE proposed / 16 OPEN.**
- REACHABLE confirmed_by: SOURCE 7 / INFERRED 17 (mechanically counted from the table below;
  the prior proposal's header said 6/18, which was a miscount — the table itself contains 7 SOURCE
  rows: 1, 2, 3, 4, 5, 15, 16).
- **0 rows verified for merge** until main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1.

## Rows

| # | Method | Label | confirmed_by | Printed citation / route |
|---|---|---|---|---|
| 1 | Utils.isMetered (Context)Z | REACHABLE | SOURCE | Fresh Utils :196-201. Called from TorrentEngine (fresh) `checkPauseTorrents` :1035 (`unmeteredOnly` branch). |
| 2 | Utils.isNetworkTypeAllowed (Context)Z | REACHABLE | SOURCE | Fresh Utils :164-194. Called internally from `checkConnectivity` fresh :161, REACHABLE via `fetchHttpUrl` (batch 57 row 11; upstream carried from batch 19). |
| 3 | Utils.isRoaming (Context)Z | REACHABLE | SOURCE | Fresh Utils :204-215. Called from TorrentEngine (fresh) `checkPauseTorrents` :1033 (`roaming` branch). |
| 4 | Utils.isSafPath (Context,Uri)Z | REACHABLE | SOURCE | Fresh Utils :657-659 (`SafFileSystem.getInstance(appContext).isSafPath(path)`). Caller now fresh: FsModuleResolverImpl (fresh) `resolveFsByUri` :43. The resolver's own facade caller was not freshly printed this pass (batch-55 print, local copies) — if the merger requires a fresh facade caller, this row's SOURCE rests on the resolver call site alone. |
| 5 | Utils.isTwoPane (Context)Z | REACHABLE | SOURCE | Fresh Utils :241-244. Called from MainActivity (fresh) :654, :677, :688, :808 (detail-pane decisions in the launcher activity). |
| 6 | Utils.isValidTrackerUrl (String)Z | OPEN | — | Fresh Utils :261-269. No printed caller in fresh files. |
| 7 | Utils.lambda$startServiceBackground$0 (Context,Intent)V | REACHABLE | INFERRED | Fresh Utils :429-430 (`() -> context.startForegroundService(i)`), posted by `new Handler(Looper.getMainLooper()).post(...)` at :429-430 inside `startServiceBackground` (:426-434, API ≥ O branch — true on API 27). Handler dispatch is framework dispatch, INFERRED; `startServiceBackground` itself is row 16. |
| 8 | Utils.makeSha1Hash (String)String | OPEN | — | Fresh Utils :567-583. No printed caller in fresh files. |
| 9 | Utils.normalizeMagnetHash (String)String | OPEN | — | Fresh Utils :233-236. No printed caller in fresh files. |
| 10 | Utils.reportError (Throwable,String)V | OPEN | — | Fresh Utils :319-325. No printed caller in fresh files. |
| 11 | Utils.requestExactAlarmPermission (Context)V | OPEN | — | Fresh Utils :671-675. No printed caller of this method itself in fresh files. Note its guarded call to `buildExactAlarmPermissionRequest` (fresh :673) does not run on API 27 (guard `SDK_INT >= S` false) — that affects batch 57 row 5, not the reachability of this method, which still needs a printed caller. |
| 12 | Utils.setBackground (View,Drawable)V | OPEN | — | Fresh Utils :152-155. No printed caller in fresh files. |
| 13 | Utils.shouldRequestStoragePermission (Activity)Z | OPEN | — | Fresh Utils :413-418. No printed caller in fresh files (MainActivity fresh :155-156 is an unrelated local variable of the same name, not a call to this method). |
| 14 | Utils.showActionModeStatusBar (Activity,boolean)V | OPEN | — | Fresh Utils :613-616 (calls `getAttributeColor` :615). No printed caller in fresh files. |
| 15 | Utils.showManageAllFilesWarningDialog (Context,FragmentManager)V | REACHABLE | SOURCE | Fresh Utils :699-718. Called from MainActivity (fresh) :180 (`onCreate`) and from AddTorrentActivity (fresh) :136 (`onCreate`) — two fresh anchors. Note: on API 27 the method returns early (fresh :703-706, `SDK_INT < R`), so the method runs but the dialog branch does not; the row is the method, and it is reached. Its internal call to `hasManageExternalStoragePermission` (fresh :705) is short-circuited off on API 27 (see batch 57 row 34). |
| 16 | Utils.startServiceBackground (Context,Intent)V | REACHABLE | SOURCE | Fresh Utils :426-434. Called from TorrentEngine (fresh) `forceStop()` :285, reached via `handleAutoStop` :143-146 subscribed in `doStart` (prior print; TorrentEngine fresh file contains the subscription context). (The other two printed sites, TorrentEngine `start()` :152 and `restartForegroundNotification()` :158, have no printed upstream caller and are not needed for this verdict.) |
| 17 | Utils$1.<init> ([[B,ArrayList)V | REACHABLE | INFERRED | Anonymous `HttpConnection.Listener` created inside `fetchHttpUrl` at fresh Utils :477 (`connection.setListener(new HttpConnection.Listener() { ... })`). Anonymous ctor dispatch is INFERRED; instantiation site printed; inherits the `fetchHttpUrl` route (batch 57 row 11). Descriptor `([[B,ArrayList;)V` matches the captured `response` (`byte[][]`) and `errorArray` (`ArrayList`) — the two captured locals of `fetchHttpUrl`. |
| 18 | Utils$1.onConnectionCreated (HttpURLConnection)V | REACHABLE | INFERRED | Listener method fresh Utils :479-482 (body empty, `/* Nothing */`). Registered at :477, `connection.run()` at :515; invocation by HttpConnection's dispatch is INFERRED (HttpConnection.java not printed). |
| 19 | Utils$1.onIOException (IOException)V | REACHABLE | INFERRED | Listener method fresh Utils :504-507 (`errorArray.add(e)`). Same registration/run as row 18; dispatch INFERRED. |
| 20 | Utils$1.onMovedPermanently (String)V | REACHABLE | INFERRED | Listener method fresh Utils :501-503 (body empty). Same registration/run as row 18; dispatch INFERRED. |
| 21 | Utils$1.onResponseHandle (HttpURLConnection,int,String)V | REACHABLE | INFERRED | Listener method fresh Utils :485-499 (HTTP_OK → read body, else FetchLinkException). Same registration/run as row 18; dispatch INFERRED. |
| 22 | Utils$1.onTooManyRedirects ()V | REACHABLE | INFERRED | Listener method fresh Utils :509-512 (`errorArray.add(new FetchLinkException("Too many redirects"))`). Same registration/run as row 18; dispatch INFERRED. |
| 23 | Utils$2.<init> (X509TrustManager)V | OPEN | — | Anonymous `X509TrustManager` created inside `getSSLContext` at fresh Utils :595-609. `getSSLContext` is OPEN (batch 57 row 28, fresh, no printed caller), so the anonymous class inherits OPEN. |
| 24 | Utils$2.checkClientTrusted ([X509Certificate,String)V | OPEN | — | Method fresh Utils :602-604 (delegates to `origTrustManager`). Invoked by the TLS stack only when the `getSSLContext` result is used for a connection; no printed use. Inherits row 23 OPEN. |
| 25 | Utils$2.checkServerTrusted ([X509Certificate,String)V | OPEN | — | Method fresh Utils :605-607 (delegates to `origTrustManager`). Same as row 24. |
| 26 | Utils$2.getAcceptedIssuers ()[X509Certificate | OPEN | — | Method fresh Utils :598-600 (delegates to `origTrustManager.getAcceptedIssuers()`). Same as row 24. |
| 27 | ActivityAddTorrentBinding.<init> (Object,View,int,AppBarLayout,CoordinatorLayout,ProgressBar,TabLayout,Toolbar,ViewPager2)V | REACHABLE | INFERRED | Base binding ctor, called by the generated `ActivityAddTorrentBindingImpl` ctor (generated file not printed). Binding created by AddTorrentActivity (fresh) :102 `DataBindingUtil.setContentView(this, R.layout.activity_add_torrent)` in `onCreate`. |
| 28 | ActivityAddTorrentBindingImpl.<clinit> ()V | REACHABLE | INFERRED | Generated class initialisation on first load of the Impl class, i.e. on the AddTorrentActivity (fresh) :102 setContentView path. JVM/generated dispatch, INFERRED. |
| 29 | ActivityAddTorrentBindingImpl.<init> (DataBindingComponent,View)V | REACHABLE | INFERRED | Generated 2-arg ctor, invoked by the DataBinderMapper via `DataBindingUtil.setContentView` (AddTorrentActivity fresh :102). Mapper file not printed; dispatch INFERRED. |
| 30 | ActivityAddTorrentBindingImpl.<init> (DataBindingComponent,View,Object[])V | REACHABLE | INFERRED | Generated 3-arg ctor, invoked by the generated 2-arg ctor after view mapping (standard generated pattern; generated file not printed, so pattern itself is INFERRED). |
| 31 | ActivityAddTorrentBindingImpl.executeBindings ()V | REACHABLE | INFERRED | Framework rebind flow: generated ctor calls `invalidateAll()` (row 33), the binding framework then runs `executeBindings()`. Generated file not printed; flow INFERRED. |
| 32 | ActivityAddTorrentBindingImpl.hasPendingBindings ()Z | OPEN | — | No printed caller, per the batches 67-68 convention adopted here. The framework's pending-rebind flag is checked internally, not via this query method, on the evidence printed. |
| 33 | ActivityAddTorrentBindingImpl.invalidateAll ()V | REACHABLE | INFERRED | Called by the generated Impl ctor (standard generated pattern; generated file not printed, so pattern INFERRED) on the AddTorrentActivity (fresh) :102 creation path. |
| 34 | ActivityAddTorrentBindingImpl.onFieldChange (int,Object,int)Z | OPEN | — | No printed observable registration or variable use in AddTorrentActivity (fresh): binding fields used are views only (`toolbar`, `viewpager`, `tabLayout`, `progress`, `coordinatorLayout`, :279-402 in prior print); no `setViewModel`/`setVariable` call printed (fresh grep confirms none). Per the batches 67-68 convention, OPEN without a printed observable use. Layout file not printed. |
| 35 | ActivityAddTorrentBindingImpl.setVariable (int,Object)Z | OPEN | — | No printed `setVariable` call in AddTorrentActivity (fresh grep confirms none) or anywhere printed this session. Generated method exists, but nothing printed assigns a variable through it. |
| 36 | ActivityFilemanagerDialogBinding.<init> (Object,View,int,FloatingActionButton,AppBarLayout,FrameLayout,CoordinatorLayout,RecyclerView,TextInputEditText,TextInputLayout,Spinner,ThemedSwipeRefreshLayout,Toolbar)V | REACHABLE | INFERRED | Base binding ctor, called by the generated Impl ctor. Binding created by FileManagerDialog (fresh) :142 `DataBindingUtil.setContentView(this, R.layout.activity_filemanager_dialog)` in `onCreate` (:120-143). Who starts FileManagerDialog (startActivity site) was not printed — dialog-anchored only, strict-entry caveat. |
| 37 | ActivityFilemanagerDialogBinding.getViewModel ()FileManagerViewModel | OPEN | — | **CONVENTION CONFLICT — NOT decided (see convention section above).** Generated getter for the `viewModel` variable. No printed `binding.getViewModel(...)` call: FileManagerDialog (fresh) :143 calls the *setter* (`binding.setViewModel(viewModel)`), which is a different method, and generated `executeBindings` reads the field directly, not via this getter. No printed getter call site. OPEN under the 58/63-64 convention; would flip to REACHABLE INFERRED under the 65-66 `executeBindings`-read convention. Do NOT flip it on the setter call. |
| 38 | ActivityFilemanagerDialogBindingImpl.<clinit> ()V | REACHABLE | INFERRED | Generated class initialisation on the FileManagerDialog (fresh) :142 setContentView path. Dispatch INFERRED. |
| 39 | ActivityFilemanagerDialogBindingImpl.<init> (DataBindingComponent,View)V | REACHABLE | INFERRED | Generated 2-arg ctor via DataBinderMapper on the FileManagerDialog (fresh) :142 path. Mapper not printed; dispatch INFERRED. |
| 40 | ActivityFilemanagerDialogBindingImpl.<init> (DataBindingComponent,View,Object[])V | REACHABLE | INFERRED | Generated 3-arg ctor via the generated 2-arg ctor (standard pattern, generated file not printed, pattern INFERRED). |

## Undecided conventions recorded, not decided

- **Binding getViewModel (row 37):** see convention section above. Merger must pick one convention
  for all binding getters (58/63-64 OPEN vs 65-66 REACHABLE INFERRED).
- **Strict-entry:** TorrentEngine-anchored rows (1, 3, 16, and via `fetchHttpUrl` rows 2, 17-22) revert
  to OPEN if the merger requires a printed launcher → TorrentService → TorrentEngine step; that step
  was not freshly printed here. FileManagerDialog-anchored rows (36-40) revert to OPEN if the merger
  requires a printed startActivity site for FileManagerDialog. AddTorrentActivity-anchored rows
  (27-35) rest on the carried AddLinkDialog → startActivity → onCreate step plus the fresh :102
  setContentView site. MainActivity-anchored rows (5, 15) carry no such caveat.
- **Confirmed_by:** per-row convention — SOURCE = a printed direct app-code call site naming the method
  (including internal calls from a SOURCE-anchored method); INFERRED = JVM/generated/framework dispatch
  where registration or first use is printed. Labels unaffected; only `confirmed_by` would change
  under a whole-route convention.
- **Lambda numbering:** Utils$1/$2 and `lambda$startServiceBackground$0` numbering is by source order /
  descriptor match, NOT bytecode-verified; a swap within a group would not change any label, except
  that the descriptor match is what pins Utils$1 to the HttpConnection listener vs Utils$2 to the
  trust manager.

## Still owed before merge

- Saved full-repo grep for the 16 OPEN rows, priority: `getSSLContext` + Utils$2 quartet
  (rows 23-26, inheriting batch 57 row 28), `isValidTrackerUrl`, `makeSha1Hash`,
  `normalizeMagnetHash`, `reportError`, `requestExactAlarmPermission` (rows 6, 8-11),
  `setBackground`, `shouldRequestStoragePermission`, `showActionModeStatusBar` (rows 12-14),
  and a printed observable/layout use for rows 32/34/35 or a printed getter call for row 37
  (under the OPEN convention; under the 65-66 convention row 37 needs no grep).
- Fresh prints for the two carried items (row 2 `fetchHttpUrl` upstream beyond `checkConnectivity`,
  FileManagerDialog startActivity site, TorrentService → TorrentEngine step) if the merger
  requires them fresh.
- Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — not run.
- No fresh HTTP 429 was hit in this pass (10 fresh connector fetches across batches 56-58, one at a time
  with 20-25 s pauses, all succeeded).
