**REVISION 2026-11-01 (OPEN-closing round 2, group G8 — batches 56/57/58 only). Status remains UNVERIFIED, NOT verified for merge. Build: not run. C1: not run. Nothing pushed.**
Flip in this revision (1): row 8 OPEN -> REACHABLE SOURCE, on a caller found by the saved full-repo grep in `~/workspace/b565758-openclose2-src/grep-full-tree-252.txt` over the 252-file app Java tree (`~/workspace/ruleF-src/`; TorrentStream SHA `1de9a2f3a1bf98c3a25a32173c62f949091eddd327199e87e393238f4c20c9d0`, TorrentDownloadImpl SHA `c2741dabb910048988e866080daab1342c2325321996b49599f93d636212fc65`, TorrentStreamServer SHA `5b5a60b9b756348a87418ac0a0e9b0b32b35213921ab86ba952c210d6b645852`) — the round-1 fresh corpus (70 files) did not contain TorrentStream, which is why the caller was missed. Checked, label UNCHANGED: rows 32, 34, 35, 37 stay OPEN (see their updated texts and the conditional table below). No other row changed. Counts: 35/0/5 -> 36/0/4.

**Conditional flip table (round 2, NOT decided — merger/user decides):** row 37 `ActivityFilemanagerDialogBinding.getViewModel` flips to REACHABLE INFERRED if and only if convention (v-getter) is adopted (generated `executeBindings` reads the view-model through the abstract getter); it stays OPEN under (v-field) (generated code reads the `mViewModel` field directly), which is the current position. Rows 32/34/35 do NOT flip under (v) either way: (v) concerns only the abstract getter. Rows 34/35 would become UNREACHABLE candidates (not claimed here) only under a further, undecided no-variable-layout rule (xv): `activity_add_torrent.xml` declares no `<data>` variable, so no observable exists for `onFieldChange`/`setVariable` to dispatch on — but generated/framework dispatch bodies are unprinted, so no UNREACHABLE claim is made on that basis. Row 32 (`hasPendingBindings`) needs a printed generated Impl body or framework dispatch body, or a framework-callback convention decision, under either option.

**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 58 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
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

## Revision note — OPEN-closing pass, 2026-11-01 (UNVERIFIED)

Counts before: 24 REACHABLE / 0 UNREACHABLE / 16 OPEN. Counts after: 35 / 0 / 5.
Flips, all OPEN → REACHABLE on freshly printed source in `~/workspace/b565758-openclose-src/`:
row 6 (`isValidTrackerUrl`, CreateTorrentViewModel:317 + DetailTorrentFragment:662) SOURCE;
row 9 (`normalizeMagnetHash`, AddLinkViewModel:64 + FeedParser:226/:244) SOURCE;
row 10 (`reportError`, five call sites) SOURCE; row 11 (`requestExactAlarmPermission`,
SchedulingSettingsFragment:137 dialog-positive callback) SOURCE; row 12 (`setBackground`, eight
call sites) SOURCE; row 13 (`shouldRequestStoragePermission`, PermissionManager:83 callback;
ctor runs ungated at API 27) SOURCE; row 14 (`showActionModeStatusBar`, eight call sites)
SOURCE; rows 23-26 (Utils$2 quartet) → REACHABLE INFERRED via `getSSLContext` (batch 57 row 28,
now REACHABLE) + TLS dispatch (HttpConnection.run() sets the socket factory, fresh :87-88).
Still OPEN (5): row 8 (`makeSha1Hash` — definition only in the fresh corpus, named grep target,
NOT UNREACHABLE without a saved full-repo grep); rows 32/34/35 (binding, no printed caller/use —
fresh AddTorrentActivity grep confirms zero `setViewModel`/`setVariable` calls); row 37
(`getViewModel` — convention conflict (v) deliberately NOT decided, see convention section).
No row flipped to UNREACHABLE. Build: not run. C1: not run. Nothing merged, nothing pushed.
Corrections (labels unchanged): `connection.run()` is at fresh Utils :512, not :515 (rows 18-22).

## Counts — mechanically verified

- **40 rows, sequence 1–40 intact, in plan order.**
- **35 REACHABLE proposed / 0 UNREACHABLE proposed / 5 OPEN.**
- REACHABLE confirmed_by: SOURCE 14 / INFERRED 21 (rows 1-5, 15, 16 SOURCE as before, plus newly flipped rows 6, 9-14 SOURCE; rows 23-26 newly INFERRED).
- **0 rows verified for merge** until main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1.

## Rows

| # | Method | Label | confirmed_by | Printed citation / route |
|---|---|---|---|---|
| 1 | Utils.isMetered (Context)Z | REACHABLE | SOURCE | Fresh Utils :196-201. Called from TorrentEngine (fresh) `checkPauseTorrents` :1035 (`unmeteredOnly` branch). |
| 2 | Utils.isNetworkTypeAllowed (Context)Z | REACHABLE | SOURCE | Fresh Utils :164-194. Called internally from `checkConnectivity` fresh :161, REACHABLE via `fetchHttpUrl` (batch 57 row 11; upstream carried from batch 19). |
| 3 | Utils.isRoaming (Context)Z | REACHABLE | SOURCE | Fresh Utils :204-215. Called from TorrentEngine (fresh) `checkPauseTorrents` :1033 (`roaming` branch). |
| 4 | Utils.isSafPath (Context,Uri)Z | REACHABLE | SOURCE | Fresh Utils :657-659 (`SafFileSystem.getInstance(appContext).isSafPath(path)`). Caller now fresh: FsModuleResolverImpl (fresh) `resolveFsByUri` :43. The resolver's own facade caller was not freshly printed this pass (batch-55 print, local copies) — if the merger requires a fresh facade caller, this row's SOURCE rests on the resolver call site alone. |
| 5 | Utils.isTwoPane (Context)Z | REACHABLE | SOURCE | Fresh Utils :241-244. Called from MainActivity (fresh) :654, :677, :688, :808 (detail-pane decisions in the launcher activity). |
| 6 | Utils.isValidTrackerUrl (String)Z | REACHABLE | SOURCE | Fresh Utils :261-269. Called from `CreateTorrentViewModel.java` (fresh) :317 inside `normalizeAndValidateUrl()` and `DetailTorrentFragment.java` (fresh) :662 (tracker-URL validation loop). |
| 7 | Utils.lambda$startServiceBackground$0 (Context,Intent)V | REACHABLE | INFERRED | Fresh Utils :429-430 (`() -> context.startForegroundService(i)`), posted by `new Handler(Looper.getMainLooper()).post(...)` at :429-430 inside `startServiceBackground` (:426-434, API ≥ O branch — true on API 27). Handler dispatch is framework dispatch, INFERRED; `startServiceBackground` itself is row 16. |
| 8 | Utils.makeSha1Hash (String)String | REACHABLE | SOURCE | Definition Utils :567-583. Direct caller printed: `TorrentStream` ctor :44 `this.id = Utils.makeSha1Hash(torrentId + selectedFileIndex)`. Route: TorrentService -> TorrentEngine `doStart` -> session start -> `onSessionStarted` -> `handleOnSessionStarted` :1046 (streaming branch :1056-1058, `pref.enableStreaming()` — a satisfiable settings flag, not a never-taken branch) -> `startStreamingServer` :1063 -> `new TorrentStreamServer` :1069 + `start()` -> NanoHTTPD `serve` dispatch (library, INFERRED step) -> `handleTorrent` :124 -> `engine.getStream` :142 -> TorrentEngine `getStream` :747 -> `TorrentDownloadImpl.getStream` :1607 -> `new TorrentStream(...)` :1621 -> ctor :40-44 -> here. The stream URL itself is shared from DetailTorrentFilesFragment `shareStreamUrl()` :509-522 via `viewModel.getStreamUrl` / `TorrentStreamServer.makeStreamUrl`. Corrects the round-1 'definition only' note: the caller was outside the 70-file round-1 corpus. |
| 9 | Utils.normalizeMagnetHash (String)String | REACHABLE | SOURCE | Fresh Utils :233-236. Called from `AddLinkViewModel.java` (fresh) :64 (inside `normalizeUrl()`) and `FeedParser.java` (fresh) :226/:244 (inside `watchMediaHash`/`watchTorrentInfoHash`). |
| 10 | Utils.reportError (Throwable,String)V | REACHABLE | SOURCE | Fresh Utils :319-325. Called from `CreateTorrentDialog.java` (fresh) :156, `FeedActivity.java` (fresh) :343, `FileManagerDialog.java` (fresh) :356, `DetailTorrentFragment.java` (fresh) :318, `AddTorrentActivity.java` (fresh) :251. |
| 11 | Utils.requestExactAlarmPermission (Context)V | REACHABLE | SOURCE | Fresh Utils :671-675. Called from `SchedulingSettingsFragment.java` (fresh) :137 inside the dialog-positive callback of `subscribeAlertDialog()`, subscribed from `onStart()`. Note: the method's own body calls `buildExactAlarmPermissionRequest` (fresh :673) only under `SDK_INT >= S` — that affects batch 57 row 5, not this method, which runs (as a call) on the dialog-positive path. |
| 12 | Utils.setBackground (View,Drawable)V | REACHABLE | SOURCE | Fresh Utils :152-155. Called from `TorrentListAdapter.java` (fresh) :186/:274, `TorrentContentFilesAdapter.java` (fresh) :163, `DrawerExpandableAdapter.java` (fresh) :241, `FeedChannelListAdapter.java` (fresh) :214/:255, `TrackerListAdapter.java` (fresh) :166/:168, `SwitchBar.java` (fresh) :62. |
| 13 | Utils.shouldRequestStoragePermission (Activity)Z | REACHABLE | SOURCE | Fresh Utils :413-418. Called from `PermissionManager.java` (fresh) :83 inside the permissions-result callback registered unconditionally in the constructor (:71); the constructor runs ungated at API 27 in `AddTorrentActivity.onCreate` (fresh) :105 and `CreateTorrentActivity.onCreate` (fresh) :64. (MainActivity fresh :155-156 is an unrelated local variable of the same name, not a call.) |
| 14 | Utils.showActionModeStatusBar (Activity,boolean)V | REACHABLE | SOURCE | Fresh Utils :613-616 (calls `getAttributeColor` :615). Called from `FeedFragment.java` (fresh) :374/:408, `MainFragment.java` (fresh) :469/:497, `DetailTorrentTrackersFragment.java` (fresh) :307/:334, `DetailTorrentFilesFragment.java` (fresh) :387/:412 (action-mode create/destroy pairs). |
| 15 | Utils.showManageAllFilesWarningDialog (Context,FragmentManager)V | REACHABLE | SOURCE | Fresh Utils :699-718. Called from MainActivity (fresh) :180 (`onCreate`) and from AddTorrentActivity (fresh) :136 (`onCreate`) — two fresh anchors. Note: on API 27 the method returns early (fresh :703-706, `SDK_INT < R`), so the method runs but the dialog branch does not; the row is the method, and it is reached. Its internal call to `hasManageExternalStoragePermission` (fresh :705) is short-circuited off on API 27 (see batch 57 row 34). |
| 16 | Utils.startServiceBackground (Context,Intent)V | REACHABLE | SOURCE | Fresh Utils :426-434. Called from TorrentEngine (fresh) `forceStop()` :285, reached via `handleAutoStop` :143-146 subscribed in `doStart` (prior print; TorrentEngine fresh file contains the subscription context). (The other two printed sites, TorrentEngine `start()` :152 and `restartForegroundNotification()` :158, have no printed upstream caller and are not needed for this verdict.) |
| 17 | Utils$1.<init> ([[B,ArrayList)V | REACHABLE | INFERRED | Anonymous `HttpConnection.Listener` created inside `fetchHttpUrl` at fresh Utils :477 (`connection.setListener(new HttpConnection.Listener() { ... })`). Anonymous ctor dispatch is INFERRED; instantiation site printed; inherits the `fetchHttpUrl` route (batch 57 row 11). Descriptor `([[B,ArrayList;)V` matches the captured `response` (`byte[][]`) and `errorArray` (`ArrayList`) — the two captured locals of `fetchHttpUrl`. |
| 18 | Utils$1.onConnectionCreated (HttpURLConnection)V | REACHABLE | INFERRED | Listener method fresh Utils :479-482 (body empty, `/* Nothing */`). Registered at :477, `connection.run()` at :512; invocation by HttpConnection's dispatch is INFERRED (HttpConnection.java not printed). |
| 19 | Utils$1.onIOException (IOException)V | REACHABLE | INFERRED | Listener method fresh Utils :504-507 (`errorArray.add(e)`). Same registration/run as row 18; dispatch INFERRED. |
| 20 | Utils$1.onMovedPermanently (String)V | REACHABLE | INFERRED | Listener method fresh Utils :501-503 (body empty). Same registration/run as row 18; dispatch INFERRED. |
| 21 | Utils$1.onResponseHandle (HttpURLConnection,int,String)V | REACHABLE | INFERRED | Listener method fresh Utils :485-499 (HTTP_OK → read body, else FetchLinkException). Same registration/run as row 18; dispatch INFERRED. |
| 22 | Utils$1.onTooManyRedirects ()V | REACHABLE | INFERRED | Listener method fresh Utils :509-512 (`errorArray.add(new FetchLinkException("Too many redirects"))`). Same registration/run as row 18; dispatch INFERRED. |
| 23 | Utils$2.<init> (X509TrustManager)V | REACHABLE | INFERRED | Anonymous `X509TrustManager` created inside `getSSLContext` at fresh Utils :595-609. `getSSLContext` is now REACHABLE (batch 57 row 28, via `HttpConnection.java` (fresh) :69, constructed by `fetchHttpUrl` at fresh Utils :472, run :512), so the anonymous class inherits REACHABLE; anonymous ctor dispatch is INFERRED. |
| 24 | Utils$2.checkClientTrusted ([X509Certificate,String)V | REACHABLE | INFERRED | Method fresh Utils :602-604 (delegates to `origTrustManager`). Invoked by the TLS stack when the `getSSLContext` result is used for a connection (`HttpConnection.run()` (fresh) :87-88 sets the socket factory); TLS dispatch unprinted, hence INFERRED. Inherits row 23 route. |
| 25 | Utils$2.checkServerTrusted ([X509Certificate,String)V | REACHABLE | INFERRED | Method fresh Utils :605-607 (delegates to `origTrustManager`). Same TLS-dispatch note as row 24. |
| 26 | Utils$2.getAcceptedIssuers ()[X509Certificate | REACHABLE | INFERRED | Method fresh Utils :598-600 (delegates to `origTrustManager.getAcceptedIssuers()`). Same TLS-dispatch note as row 24. |
| 27 | ActivityAddTorrentBinding.<init> (Object,View,int,AppBarLayout,CoordinatorLayout,ProgressBar,TabLayout,Toolbar,ViewPager2)V | REACHABLE | INFERRED | Base binding ctor, called by the generated `ActivityAddTorrentBindingImpl` ctor (generated file not printed). Binding created by AddTorrentActivity (fresh) :102 `DataBindingUtil.setContentView(this, R.layout.activity_add_torrent)` in `onCreate`. |
| 28 | ActivityAddTorrentBindingImpl.<clinit> ()V | REACHABLE | INFERRED | Generated class initialisation on first load of the Impl class, i.e. on the AddTorrentActivity (fresh) :102 setContentView path. JVM/generated dispatch, INFERRED. |
| 29 | ActivityAddTorrentBindingImpl.<init> (DataBindingComponent,View)V | REACHABLE | INFERRED | Generated 2-arg ctor, invoked by the DataBinderMapper via `DataBindingUtil.setContentView` (AddTorrentActivity fresh :102). Mapper file not printed; dispatch INFERRED. |
| 30 | ActivityAddTorrentBindingImpl.<init> (DataBindingComponent,View,Object[])V | REACHABLE | INFERRED | Generated 3-arg ctor, invoked by the generated 2-arg ctor after view mapping (standard generated pattern; generated file not printed, so pattern itself is INFERRED). |
| 31 | ActivityAddTorrentBindingImpl.executeBindings ()V | REACHABLE | INFERRED | Framework rebind flow: generated ctor calls `invalidateAll()` (row 33), the binding framework then runs `executeBindings()`. Generated file not printed; flow INFERRED. |
| 32 | ActivityAddTorrentBindingImpl.hasPendingBindings ()Z | OPEN | — | No printed caller, per the batches 67-68 convention adopted here. Round-2 check: zero hits for `hasPendingBindings` in the saved 252-file Java-tree grep (`~/workspace/b565758-openclose2-src/grep-full-tree-252.txt` and the binding-callbacks family grep over the same tree), and generated Impl bodies are not in that corpus, so generated/framework dispatch is unprinted. Zero hits alone never flips to UNREACHABLE. Resolver: a printed generated Impl body or framework dispatch body, or a framework-callback convention decision. |
| 33 | ActivityAddTorrentBindingImpl.invalidateAll ()V | REACHABLE | INFERRED | Called by the generated Impl ctor (standard generated pattern; generated file not printed, so pattern INFERRED) on the AddTorrentActivity (fresh) :102 creation path. |
| 34 | ActivityAddTorrentBindingImpl.onFieldChange (int,Object,int)Z | OPEN | — | No printed observable registration or variable use in AddTorrentActivity (fresh): binding fields used are views only (`toolbar`, `viewpager`, `tabLayout`, `progress`, `coordinatorLayout`, :279-402 in prior print); no `setViewModel`/`setVariable` call printed (fresh grep confirms none). Round-2 check strengthened: `activity_add_torrent.xml` (SHA `aac68fa7fcf1a3a2d67741a6266bccf1c260cb49fc57d220f1169a74ad781e91`, saved in `~/workspace/b565758-openclose2-src/`) declares NO `<data>` block and no variable at all, so no observable exists for this callback to dispatch on — but generated dispatch is unprinted, so this stays OPEN, not UNREACHABLE, pending the no-variable-layout convention decision (xv). Per the batches 67-68 convention, OPEN without a printed observable use. |
| 35 | ActivityAddTorrentBindingImpl.setVariable (int,Object)Z | OPEN | — | No printed `setVariable` call in AddTorrentActivity (fresh grep confirms none) or anywhere printed this session; round-2 saved 252-file grep also finds zero `setVariable` hits tree-wide. Generated method exists, but nothing printed assigns a variable through it. Round-2 note: `activity_add_torrent.xml` declares no `<data>` variable (see row 34), which would make this an UNREACHABLE candidate only under the undecided no-variable-layout rule (xv) — not claimed here, since generated `setVariable` dispatch is unprinted and the batch-65 direction (setVariable-via-setViewModel) is itself disputed: in generated code `setVariable` calls the typed setter, not vice versa. Stays OPEN. |
| 36 | ActivityFilemanagerDialogBinding.<init> (Object,View,int,FloatingActionButton,AppBarLayout,FrameLayout,CoordinatorLayout,RecyclerView,TextInputEditText,TextInputLayout,Spinner,ThemedSwipeRefreshLayout,Toolbar)V | REACHABLE | INFERRED | Base binding ctor, called by the generated Impl ctor. Binding created by FileManagerDialog (fresh) :142 `DataBindingUtil.setContentView(this, R.layout.activity_filemanager_dialog)` in `onCreate` (:120-143). Who starts FileManagerDialog (startActivity site) was not printed — dialog-anchored only, strict-entry caveat. |
| 37 | ActivityFilemanagerDialogBinding.getViewModel ()FileManagerViewModel | OPEN | — | **CONVENTION CONFLICT — NOT decided (see convention section above and the round-2 conditional table at the top of this file).** Generated getter for the `viewModel` variable. No printed `binding.getViewModel(...)` call: FileManagerDialog (fresh) :143 calls the *setter* (`binding.setViewModel(viewModel)`), which is a different method, and generated `executeBindings` reads the field directly, not via this getter. No printed getter call site. Round-2 check: zero `getViewModel` hits in the saved 252-file Java-tree grep; the layout `activity_filemanager_dialog.xml` (SHA `016b7bd2b7045bb1895678479e09242f4ee472f30121332144900db37981a1e4`) DOES declare a `viewModel` variable (:6-16) and uses `@{viewModel.config...}` expressions (:74, :94), so the variable is genuinely bound — the only question is the (v) read path. OPEN under the 58/63-64 convention; would flip to REACHABLE INFERRED under the 65-66 `executeBindings`-read convention. Do NOT flip it on the setter call. |
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

- Saved full-repo grep for the 5 remaining OPEN rows: `makeSha1Hash` (row 8 — no caller in any
  freshly fetched file, definition only at fresh Utils :567; NOT flipped to UNREACHABLE without a
  saved full-repo grep) and a printed observable/layout use for rows 32/34/35 or a printed getter
  call for row 37 (under the OPEN convention; under the 65-66 convention row 37 needs no grep).
  Rows 6, 9-14 and 23-26 are closed by the fresh call sites above, not by a grep.
- Fresh prints for the two carried items (row 2 `fetchHttpUrl` upstream beyond `checkConnectivity`,
  FileManagerDialog startActivity site, TorrentService → TorrentEngine step) if the merger
  requires them fresh.
- Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — not run.
- No fresh HTTP 429 was hit in this pass (10 fresh connector fetches across batches 56-58, one at a time
  with 20-25 s pauses, all succeeded).
