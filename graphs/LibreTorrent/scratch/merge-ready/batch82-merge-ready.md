# LibreTorrent batch 82 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to `graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** Build and C1 run on the user's Mac after a push, so both are marked "not run" here, never passed. No sampler or saved full-repo grep was run or is claimed.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 82 only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. Prior proposal `~/workspace/libretorrent-batch82-proposal.md` was used as an INPUT / lead list only; every row below was checked against printed source in this pass, and no prior verdict was copied as a result.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 82 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the local plan copy `~/workspace/agent27-plan.tsv` (4,732 rows total; plan blob SHA `0104806dd666c840049b3db52823d4b384fa1c92`), all `TODO_CANDIDATE_REACHABLE` (generator candidates, not evidence), in plan order. Method names and JVM descriptors below match the plan row for row. Classes: AddTorrentViewModel$DecodeState (2), AddTorrentViewModel$Status (1), AddTorrentViewModel$TorrentDecodeTask (5), DownloadableFileItem (6), DownloadableFileItem$1 (3), DownloadableFilesAdapter (4), DownloadableFilesAdapter$1 (3), DownloadableFilesAdapter$ViewHolder (4), CreateTorrentActivity (10), CreateTorrentActivity$1 (3), CreateTorrentDialog (1).

## Printed source used in this pass

Fresh connector fetches from branch `work-2026-10-31`, one file at a time with pauses, saved in `~/workspace/b81-82-src/` (base path `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`). No fresh HTTP 429 was hit in this pass.

- `ui/addtorrent/AddTorrentViewModel.java` — fresh, SHA `bec2f6eec2a538bd7223095b87014183530f4534`, 574 lines. Closes the prior session's carried-forward gap for rows 1–8: every ViewModel citation below was re-checked against this fresh fetch.
- `ui/addtorrent/DownloadableFileItem.java` — fresh, SHA `18e64cd35f1fb2a001a696201453f543ffba69e6`, 86 lines; text identical to the prior session's print.
- `ui/addtorrent/DownloadableFilesAdapter.java` — fresh, SHA `e84a92f1e60757f061b595a37b25cddbb20db7c6`, 155 lines; text identical to the prior session's print.
- `ui/addtorrent/AddTorrentFilesFragment.java` — fresh, SHA `b10cfc539cbadbb4c8eb37d88ecfe4e320c5ac88`, 197 lines; citations identical to the prior session's print (adapter construction :139, setAdapter :140, subscribeAdapter :113–123, map `DownloadableFileItem::new` :117, submitList :122).
- `ui/createtorrent/CreateTorrentActivity.java` — fresh, SHA `cfcdb7be9091cc8ce805287ea45a13914c616b45`, 140 lines; text identical to the prior session's print.
- `ui/createtorrent/CreateTorrentDialog.java` — fresh, SHA `bfb6fc626ae6deb509bd5c485549a83c8ddb892e`, 561 lines. This closes the prior session's gap for row 40 (dialog file not printed there) and upgrades row 33 (see below).
- `ui/addtorrent/AddTorrentActivity.java`, `ui/addtorrent/AddTorrentPagerAdapter.java`, `ui/addtorrent/AddTorrentInfoFragment.java`, `ui/addtorrent/AddTorrentMutableParams.java` — also freshly fetched this pass (see batch 81 file); used here only for the shared AddTorrent entry trunk.

Not freshly fetched this pass, and not relied on for any row's sole citation: `ui/main/MainFragment.java` (only the `createTorrentDialog()` → `startActivity(CreateTorrentActivity)` line cited in the prior proposal, from a local copy). The launcher → MainActivity → MainFragment steps were not re-printed this session — see strict-entry caveat below.

## Shared entry routes (printed this pass)

AddTorrent route (rows 1–28): batch 81 trunk — AddTorrentActivity.onCreate :103–104 `provider.get(AddTorrentViewModel.class)` → ViewModel.<init> → AddTorrentActivity :288–289 pager adapter + setAdapter → AddTorrentFilesFragment.onViewCreated :139–140 `new DownloadableFilesAdapter(this)` + `fileList.setAdapter(adapter)`, and onStart → subscribeAdapter :113–123 (children subject → map `DownloadableFileItem::new` :117 → submitList :122).
CreateTorrent route (rows 29–40): MainFragment.createTorrentDialog() :562–563 `startActivity(CreateTorrentActivity)` (prior-session local copy, not fresh) → CreateTorrentActivity.onCreate :55–93 (find-or-create CreateTorrentDialog :83, newInstance :85, show :86).

**STRICT-ENTRY CAVEAT (undecided convention, recorded not decided):** launcher → MainActivity → MainFragment steps were not re-printed this session, so under a strict printed-launcher rule every REACHABLE row below reverts to OPEN. The verdicts below follow the activity-anchored convention of the prior batches. The merger must pick one strict-entry convention for all batches; labels below do not decide it.

## confirmed_by convention used here

- SOURCE: a direct app-to-app call site naming the method is printed in app source, or a standard Android callback whose registration is printed (Activity/Fragment lifecycle, RecyclerView.Adapter / ListAdapter + DiffUtil callbacks, View click listeners, anonymous-class instantiation inside a printed method).
- INFERRED: the route crosses a dispatch step NOT printed from its own source (RxJava, AsyncTask, data-binding Observable, JVM <clinit>, PermissionManager permission-result callbacks, framework Parcelable dispatch).
- No row is flipped to UNREACHABLE on absence in the printed subset; rows with no printed caller stay OPEN pending a saved full-repo grep. No connector `search_code` 0-result was used as evidence of absence.

## Per-row verdicts

| # | Method | Label | confirmed_by | Printed citation / route |
|---|---|---|---|---|
| 1 | AddTorrentViewModel$DecodeState.<init>(Status) (Status)V | REACHABLE | SOURCE | Delegating ctor, ViewModel.java:123–125; called from <init> :142 (UNKNOWN) and decode-task paths :229, :234, :251, :318, :322 (all re-checked fresh). At least one call (:142) sits on a fully printed route. |
| 2 | AddTorrentViewModel$DecodeState.<init>(Status,Throwable) (Status,Throwable)V | REACHABLE | SOURCE | Target of the delegating ctor :124; also called :307 (ERROR,e) and :334. Def ViewModel.java:118–121. |
| 3 | AddTorrentViewModel$Status.<clinit> ()V | REACHABLE | INFERRED | Enum constants ViewModel.java:103–112; JVM class init on first use (new DecodeState(Status.UNKNOWN), ViewModel.java:142). |
| 4 | AddTorrentViewModel$TorrentDecodeTask.<init> (AddTorrentViewModel)V | REACHABLE | INFERRED | Created by startDecodeTask(), ViewModel.java:198; startDecodeTask itself is reached only through the Rx subscribe lambda in startDecode() :188–190, hence INFERRED. Def :205–209. |
| 5 | AddTorrentViewModel$TorrentDecodeTask.doInBackground (Uri[])Throwable | REACHABLE | INFERRED | AsyncTask framework dispatch after executeOnExecutor, ViewModel.java:199; AsyncTask dispatch not printed from its own source. Def :217–279. |
| 6 | AddTorrentViewModel$TorrentDecodeTask.onPostExecute (Throwable)V | REACHABLE | INFERRED | Same AsyncTask dispatch; def ViewModel.java:301–325. |
| 7 | AddTorrentViewModel$TorrentDecodeTask.onPreExecute ()V | REACHABLE | INFERRED | Same AsyncTask dispatch; def ViewModel.java:212–214. |
| 8 | AddTorrentViewModel$TorrentDecodeTask.readTorrentFile (Uri)V | REACHABLE | INFERRED | Private; called only from doInBackground(), ViewModel.java:272, so it inherits the AsyncTask crossing. Def :281–298. |
| 9 | DownloadableFileItem.<clinit> ()V | REACHABLE | INFERRED | Static CREATOR field, fresh DownloadableFileItem.java:61–75; JVM class init on first use (FilesFragment :117 `DownloadableFileItem::new`). |
| 10 | DownloadableFileItem.<init>(Parcel) (Parcel)V | OPEN | — | Called only by CREATOR.createFromParcel, fresh DownloadableFileItem.java:67. No printed site parcels or unparcels a DownloadableFileItem (no putParcelable/getParcelableExtra site in any file fetched this session). Pending saved full-repo grep — one parceling grep hit flips rows 10, 12, 14, 16, 17 together. NOT `no_trigger_in_app` on this evidence. |
| 11 | DownloadableFileItem.<init>(BencodeFileTree) (BencodeFileTree)V | REACHABLE | INFERRED | Method reference in fresh FilesFragment.java:117 `.map(DownloadableFileItem::new)` inside an Rx flatMapSingle chain (:113–119); Rx dispatch not printed. Def DownloadableFileItem.java:33–38. |
| 12 | DownloadableFileItem.describeContents ()I | OPEN | — | Parcelable callback, def DownloadableFileItem.java:48–51; runs only when an instance is parcelled — no printed parcel site (see row 10). Pending grep. |
| 13 | DownloadableFileItem.toString ()String | OPEN | — | Def DownloadableFileItem.java:79–85; no printed caller (no logging/concat site in fetched files). Pending grep. This row is NOT part of the parcel quartet: a parcel hit does not by itself close it; it needs its own caller or logging/concat grep hit. |
| 14 | DownloadableFileItem.writeToParcel (Parcel,I)V | OPEN | — | Def DownloadableFileItem.java:54–59; runs only when an instance is parcelled — no printed parcel site (see row 10). Pending grep. |
| 15 | DownloadableFileItem$1.<init> ()V | REACHABLE | INFERRED | Anonymous CREATOR instance created in the <clinit> field initialiser, DownloadableFileItem.java:61–62; inherits the <clinit> route (row 9). |
| 16 | DownloadableFileItem$1.createFromParcel (Parcel)DownloadableFileItem | OPEN | — | Def DownloadableFileItem.java:65–68 (returns new DownloadableFileItem(source)); framework Parcelable dispatch, no printed unparcel site (see row 10). Pending grep. |
| 17 | DownloadableFileItem$1.newArray (I)DownloadableFileItem[] | OPEN | — | Def DownloadableFileItem.java:71–74; same Parcelable-dispatch caveat as row 16. Pending grep. |
| 18 | DownloadableFilesAdapter.<clinit> ()V | REACHABLE | INFERRED | Non-constant static TAG field, fresh Adapter.java:44 (`class.getSimpleName()`); JVM class init on first use (FilesFragment :139 `new DownloadableFilesAdapter(this)`). |
| 19 | DownloadableFilesAdapter.<init> (ClickListener)V | REACHABLE | SOURCE | Fresh FilesFragment.java:139 `adapter = new DownloadableFilesAdapter(this)`; def Adapter.java:48–52 (super(diffCallback)). |
| 20 | DownloadableFilesAdapter.onBindViewHolder (ViewHolder,I)V | REACHABLE | SOURCE | Standard RecyclerView.Adapter callback after printed setAdapter, FilesFragment.java:140; def Adapter.java:69–71 (holder.bind(getItem(position), clickListener)). |
| 21 | DownloadableFilesAdapter.onCreateViewHolder (ViewGroup,I)ViewHolder | REACHABLE | SOURCE | Standard RecyclerView.Adapter callback, same registration; def Adapter.java:57–65 (inflates binding, returns new ViewHolder). |
| 22 | DownloadableFilesAdapter$1.<init> ()V | REACHABLE | INFERRED | Anonymous DiffUtil.ItemCallback instance created in the static diffCallback field initialiser, Adapter.java:74–90; runs in <clinit> (row 18 route). |
| 23 | DownloadableFilesAdapter$1.areContentsTheSame (DownloadableFileItem,DownloadableFileItem)Z | REACHABLE | SOURCE | Standard ListAdapter/DiffUtil callback, registered via super(diffCallback) Adapter.java:50 and exercised by printed submitList, FilesFragment.java:122; def Adapter.java:77–81 (oldItem.equals(newItem)). |
| 24 | DownloadableFilesAdapter$1.areItemsTheSame (DownloadableFileItem,DownloadableFileItem)Z | REACHABLE | SOURCE | Same registration and submitList trigger; def Adapter.java:84–88. |
| 25 | DownloadableFilesAdapter$ViewHolder.<init> (ItemTorrentDownloadableFileBinding)V | REACHABLE | SOURCE | Created by onCreateViewHolder, Adapter.java:65; def :95–99. |
| 26 | DownloadableFilesAdapter$ViewHolder.bind (DownloadableFileItem,ClickListener)V | REACHABLE | SOURCE | Called by onBindViewHolder, Adapter.java:71; def :102–145 (click listeners, name/icon/selected/size binding). |
| 27 | DownloadableFilesAdapter$ViewHolder.lambda$bind$0 (DownloadableFileItem,ClickListener,View)V | REACHABLE | SOURCE | itemView click listener registered in bind(), Adapter.java:106–112 (performs selected click, calls listener.onItemClicked → FilesFragment.java:183); standard View click dispatch. Numbering by source order, not bytecode-verified. |
| 28 | DownloadableFilesAdapter$ViewHolder.lambda$bind$1 (ClickListener,DownloadableFileItem,View)V | REACHABLE | SOURCE | selected-checkbox click listener, Adapter.java:114–117 (calls listener.onItemCheckedChanged → FilesFragment.java:192–194); standard View click dispatch. Numbering by source order, not bytecode-verified. |
| 29 | CreateTorrentActivity.<init> ()V | REACHABLE | SOURCE | Default constructor; framework instantiation on startActivity, MainFragment.java:563 (createTorrentDialog :562–563, prior-session local copy, not fresh). Standard Activity instantiation. |
| 30 | CreateTorrentActivity.lambda$subscribeAlertDialog$0 (BaseAlertDialog$Event)V | REACHABLE | INFERRED | Rx subscribe lambda in subscribeAlertDialog(), fresh CreateTorrentActivity.java:110–125; Rx dispatch not printed. subscribeAlertDialog called from onStart :99. |
| 31 | CreateTorrentActivity.onBackPressed ()V | REACHABLE | SOURCE | Standard Activity callback; def fresh CreateTorrentActivity.java:136–139 (createTorrentDialog.onBackPressed()). |
| 32 | CreateTorrentActivity.onCreate (Bundle)V | REACHABLE | SOURCE | Standard Activity lifecycle; def fresh :55–93, incl. dialog show :83–87. |
| 33 | CreateTorrentActivity.onFragmentFinished (Fragment,Intent,ResultCode)V | REACHABLE | SOURCE | **Upgraded from INFERRED in the prior proposal.** Fresh CreateTorrentDialog.java:555–559 `finish(...)` calls `((FragmentCallback)activity).onFragmentFinished(this, intent, code)`, with call sites at Dialog :312, :394, :401, :552; the host activity is CreateTorrentActivity, printed at CreateTorrentActivity.java:83–87 (findFragmentByTag / newInstance / show). The prior INFERRED rested on the dialog file not being printed; it is printed now. Def CreateTorrentActivity.java:130–133 (finish()). |
| 34 | CreateTorrentActivity.onStart ()V | REACHABLE | SOURCE | Standard Activity lifecycle; def fresh :96–100 (subscribeAlertDialog). |
| 35 | CreateTorrentActivity.onStop ()V | REACHABLE | SOURCE | Standard Activity lifecycle; def fresh :103–107 (disposable.clear()). |
| 36 | CreateTorrentActivity.subscribeAlertDialog ()V | REACHABLE | SOURCE | Called from onStart, fresh CreateTorrentActivity.java:99; def :109–127. (Its Rx lambda is row 30, INFERRED.) |
| 37 | CreateTorrentActivity$1.<init> (CreateTorrentActivity,FragmentManager)V | REACHABLE | SOURCE | Anonymous PermissionManager.Callback instantiated in onCreate, fresh CreateTorrentActivity.java:64–81. |
| 38 | CreateTorrentActivity$1.onNotificationResult (Z,Z)V | REACHABLE | INFERRED | Permission-result callback, def fresh :78–80; invoked by PermissionManager's permission flow, not printed from its own source. |
| 39 | CreateTorrentActivity$1.onStorageResult (Z,Z)V | REACHABLE | INFERRED | Permission-result callback, def fresh :66–75; same unprinted PermissionManager dispatch as row 38. |
| 40 | CreateTorrentDialog.<clinit> ()V | REACHABLE | INFERRED | Fresh dialog file confirms the <clinit> basis the prior proposal had to assume: non-constant static TAG at CreateTorrentDialog.java:71 (`class.getSimpleName()`), plus other static TAG constants :73–77. JVM class init on first use in fresh CreateTorrentActivity.onCreate :83 (findFragmentByTag cast) and :85–86 (newInstance + show). |

## Counts — batch 82 (proposed, NOT verified)

- REACHABLE proposed: 34 / 40 (SOURCE 19, INFERRED 15)
- UNREACHABLE proposed: 0 / 40
- OPEN: 6 / 40 (rows 10, 12, 13, 14, 16, 17 — all DownloadableFileItem Parcelable/toString rows)
- Verified for merge: 0 / 40

## Combined batches 81 + 82 (this pass)

- 80 rows: 73 REACHABLE proposed / 0 UNREACHABLE / 7 OPEN. Verified for merge: 0/80.

## Changes vs the prior proposal (all else held on fresh re-check)

1. Batch 82 row 33 `CreateTorrentActivity.onFragmentFinished`: INFERRED → SOURCE (fresh CreateTorrentDialog.java:555–559 printed caller, host CreateTorrentActivity printed at :83–87). Label unchanged (REACHABLE); only confirmed_by upgraded. Batch 82 SOURCE count therefore rises 18 → 19, INFERRED falls 16 → 15.
2. Batch 82 row 40 `CreateTorrentDialog.<clinit>`: prior caveat (dialog file not printed) is closed — fresh dialog file confirms non-constant TAG at :71.
3. Batch 81 rows 1–2 and batch 82 rows 1–8: prior carried-forward ViewModel gap is closed — AddTorrentViewModel.java freshly fetched, all prior ViewModel line numbers held.
4. No other verdict changed. In particular, the DownloadableFileItem parcel quartet (rows 10, 12, 14, 16, 17) stays OPEN, per the task note: one parceling grep hit would flip those five together; row 13 toString is separate and needs its own caller/logging grep hit.

## Still owed before merge

1. Saved full-repo grep for all 7 OPEN rows (batch 81 row 2; batch 82 rows 10, 12, 13, 14, 16, 17) — especially any putParcelable/getParcelableExtra site for DownloadableFileItem, which would flip rows 10, 12, 14, 16, 17 together.
2. Re-print the launcher → MainActivity → MainFragment steps if the strict-entry rule is applied.
3. Main-agent spot-check 1 in 5, py_compile, build, Mac build/C1 — not run here.
4. Lambda numbering is source-order, not bytecode-verified; a swap would not change any label in this batch.
