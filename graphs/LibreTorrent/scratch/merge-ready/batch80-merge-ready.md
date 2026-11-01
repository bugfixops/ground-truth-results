**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 80 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 80 only, max 40 methods, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. The prior batch-80 proposal
  (`~/workspace/libretorrent-batch80-proposal.md`, 34 REACHABLE / 0 / 6 OPEN) was used as an
  INPUT / lead list only; every row below was re-judged against the source freshly
  printed in this pass, and no prior verdict was copied as a result. The headline
  change versus that proposal is that all 6 of its OPEN rows are now resolved (see
  "OPEN rows resolved in this pass" below) — the prior proposal's own grep targets
  (AddTorrentViewModel, plus the bound layout for the two setters) are exactly the
  files printed fresh here.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 80 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/agent27-plan.tsv` (4,732 rows total; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
All 40 batch-80 rows are `TODO_CANDIDATE_REACHABLE` in the plan. The table below is in
plan order, sequence 1–40 intact. Note the plan/membership traps the prior proposal
already flagged and which are respected here: `AddTorrentMutableParams.setStorageFreeSpace`
is NOT a batch-80 row and is not judged here; `AddTorrentMutableParams.toString` is NOT
a batch-80 row and is not judged here.

## Printed source used in this pass

Fresh connector fetches from branch `work-2026-10-31`, one file at a time with pauses,
saved in `~/workspace/b7980-src/` (all under
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`
unless noted; SHA-256 of the saved copies):

- `ui/addtorrent/AddTorrentInfoFragment.java` — 244 lines, SHA-256 `85a15039…`.
- `ui/addtorrent/AddTorrentPagerAdapter.java` — 56 lines, SHA-256 `3f03d9da…`.
- `ui/addtorrent/AddTorrentActivity.java` — 577 lines, SHA-256 `41e027a5…`.
- `ui/addtorrent/AddTorrentMutableParams.java` — 171 lines, SHA-256 `ae4c366b…`.
- `ui/addtorrent/AddTorrentViewModel.java` — 574 lines, SHA-256 `46c7152d…` — **the
  file that resolves the 6 prior OPEN rows** (see below).
- `src/main/res/layout/fragment_add_torrent_info.xml` — wrapper layout, 699 bytes,
  SHA-256 `2c440a47…`.
- `src/main/res/layout/add_torrent_info.xml` — included layout, 13,217 bytes,
  SHA-256 `b765b5ab…`; its bindings are quoted below from this freshly fetched copy.
- `src/main/AndroidManifest.xml` — 295 lines, SHA-256 `b011d747…` (entry, see Strict-entry).

No fresh HTTP 429 was hit in this pass. No connector `search_code` result was used as
evidence of absence anywhere in this file.

## Shared trunk (printed this session)

Same trunk as batch 79, printed fresh here: AndroidManifest.xml:62-64 declares
`AddTorrentActivity`, exported, with SEND/VIEW intent filters; AddTorrentActivity
onCreate:97-139 → initLayout:138 → pager adapter → AddTorrentPagerAdapter
createFragment:44 → AddTorrentInfoFragment.newInstance:74-81 → fragment lifecycle.
InfoFragment onViewCreated:99-121 obtains the ViewModel (`new ViewModelProvider(activity).get(AddTorrentViewModel.class)` at :101),
sets it on the binding (:102), registers the folder-chooser click lambda (:105),
the name TextWatcher (:106), and the tags listener (:120).
InfoFragment onStart:124-128 → subscribeTags:127.

## OPEN rows resolved in this pass — all 6 prior OPEN rows, now REACHABLE SOURCE

The prior proposal left these OPEN for want of a printed caller in the files it had
fetched, naming AddTorrentViewModel as the likely caller. AddTorrentViewModel.java,
freshly printed here, supplies a direct printed caller for every one:

| Prior OPEN row | Now | Printed caller (fresh, AddTorrentViewModel.java unless noted) |
|---|---|---|
| 26 `getSource` | REACHABLE SOURCE | `:269` (`tmpSource = v.mutableParams.getSource()`) and `:474` (`source = mutableParams.getSource()` in addTorrent). |
| 29 `isFromMagnet` | REACHABLE SOURCE | `:270` (`fromMagnet = v.mutableParams.isFromMagnet()`) and `:471` (same in addTorrent). |
| 33 `setDirName` | REACHABLE SOURCE | `:358` (`mutableParams.setDirName(fs.getDirPath(dirPath))` inside the dirPathCallback runnable). |
| 35 `setFromMagnet` | REACHABLE SOURCE | `:235` (`v.mutableParams.setFromMagnet(true)` in the MAGNET decode branch). |
| 37 `setName` | REACHABLE SOURCE | `:344` (`mutableParams.setName(downloadInfo.torrentName)` in the metadata observer); independently, the included layout binds it two-way (`android:text="@={viewModel.mutableParams.name}"` in add_torrent_info.xml). |
| 39 `setSource` | REACHABLE SOURCE | `:227` and `:232` (`v.mutableParams.setSource(uri.toString())`, FILE/CONTENT and MAGNET branches) and `:258` (`v.mutableParams.setSource(v.fs.normalizeFileSystemPath(...))`, HTTP branch). |

Two further upgrades versus the prior proposal, both from the same fresh prints:

- Row 22 `<init>`: was INFERRED ("construction site not printed"); now SOURCE —
  the construction site is printed at AddTorrentViewModel.java:81
  (`public AddTorrentMutableParams mutableParams = new AddTorrentMutableParams();`),
  and the ViewModel itself is obtained in-app at AddTorrentActivity.java:103-104
  (`provider.get(AddTorrentViewModel.class)`; ViewModelProvider dispatch itself is
  INFERRED, the params construction site is not).
- Row 27 `getStorageFreeSpace`: was INFERRED (binding only); now SOURCE —
  direct printed caller at AddTorrentViewModel.java:552
  (`mutableParams.getStorageFreeSpace()` in checkFreeSpace), in addition to the
  layout binding (`app:fileSize="@{viewModel.mutableParams.storageFreeSpace}"`).
- Row 23 `getDirName`: stays INFERRED, but its evidence is now stronger than the
  prior proposal's "must confirm layout" caveat — the layout IS now printed and
  does bind it (`android:text="@{viewModel.mutableParams.dirName}"` on the save_path
  TextView in add_torrent_info.xml), and InfoFragment onViewCreated:102 sets the
  viewModel on the binding. The getter itself is still reached only through
  generated `executeBindings` code, which is not in the upload, so it remains
  INFERRED, not SOURCE — see the binding-getter convention note below.

## confirmed_by convention in this file

- `SOURCE` = a direct app-to-app call site naming the method is printed in app source
  (including a printed construction site for `<init>` rows).
- `INFERRED` = the method is reached only through unprinted framework/library dispatch
  (fragment lifecycle, ActivityResult dispatch, view-click/TextWatcher/listener
  dispatch, Rx dispatch, ViewModelProvider dispatch, generated data-binding
  `executeBindings` reads) where the registration, show, or construction site is printed.
  This is the per-row convention, not the whole-route convention used in some earlier
  batches; labels are unaffected, only `confirmed_by` would change at merge if the
  merger adopts the whole-route convention.
- No row uses `DYN`, `FW-MEMORY`, or `UNVERIFIED` as `confirmed_by`.

## Table — 40 rows, plan order

| # | Method | Label proposed | confirmed_by | Printed citation / reason |
|---|---|---|---|---|
| 1 | AddTorrentInfoFragment.lambda$new$1 | REACHABLE | INFERRED | AddTorrentInfoFragment.java:137-148: selectTag ActivityResult callback (first registerForActivityResult in source order); framework result dispatch INFERRED; body adds tag via viewModel.addTag. |
| 2 | AddTorrentInfoFragment.lambda$new$2 | REACHABLE | INFERRED | AddTorrentInfoFragment.java:150-162: chooseDir ActivityResult callback (second registerForActivityResult); dispatch INFERRED; body calls showOpenDirErrorDialog:157 or mutableParams.getDirPath().set(...):160. |
| 3 | AddTorrentInfoFragment.lambda$onViewCreated$0 | REACHABLE | INFERRED | AddTorrentInfoFragment.java:105: folderChooserButton click lambda in onViewCreated; view click dispatch INFERRED; calls showChooseDirDialog. |
| 4 | AddTorrentInfoFragment.newInstance | REACHABLE | SOURCE | AddTorrentInfoFragment.java:74-81, called by AddTorrentPagerAdapter.java:44. |
| 5 | AddTorrentInfoFragment.onAttach | REACHABLE | INFERRED | AddTorrentInfoFragment.java:84-89 body printed; FragmentManager lifecycle dispatch INFERRED. |
| 6 | AddTorrentInfoFragment.onCreateView | REACHABLE | INFERRED | AddTorrentInfoFragment.java:92-96 body printed; lifecycle dispatch INFERRED. |
| 7 | AddTorrentInfoFragment.onStart | REACHABLE | INFERRED | AddTorrentInfoFragment.java:124-128 body printed; lifecycle dispatch INFERRED; calls subscribeTags:127. |
| 8 | AddTorrentInfoFragment.onStop | REACHABLE | INFERRED | AddTorrentInfoFragment.java:131-135 body printed; lifecycle dispatch INFERRED. |
| 9 | AddTorrentInfoFragment.onViewCreated | REACHABLE | INFERRED | AddTorrentInfoFragment.java:99-121 body printed; lifecycle dispatch INFERRED; registers click lambda:105, TextWatcher:106, tagsListener:120. |
| 10 | AddTorrentInfoFragment.showChooseDirDialog | REACHABLE | SOURCE | AddTorrentInfoFragment.java:192-213, called from click lambda:105. |
| 11 | AddTorrentInfoFragment.showOpenDirErrorDialog | REACHABLE | SOURCE | AddTorrentInfoFragment.java:215-231, called from chooseDir callback:157. |
| 12 | AddTorrentInfoFragment.subscribeTags | REACHABLE | SOURCE | AddTorrentInfoFragment.java:186-189, called from onStart:127. |
| 13 | AddTorrentInfoFragment$1.<init> | REACHABLE | SOURCE | Anonymous TextWatcher constructed in onViewCreated:106-119; <init> runs at that construction site. $1 = first anonymous class in source order (TextWatcher); $2 = second (TorrentTagsList.Listener field, :163). |
| 14 | AddTorrentInfoFragment$1.afterTextChanged | REACHABLE | INFERRED | Body AddTorrentInfoFragment.java:116-118 printed (calls checkNameField:117, batch 79 row 40); EditText/TextWatcher dispatch INFERRED. |
| 15 | AddTorrentInfoFragment$1.beforeTextChanged | REACHABLE | INFERRED | Body AddTorrentInfoFragment.java:108-109 printed (empty); same listener registered onViewCreated:106, dispatch INFERRED. Empty body does not make it unreachable — it is still invoked on text change. |
| 16 | AddTorrentInfoFragment$1.onTextChanged | REACHABLE | INFERRED | Body AddTorrentInfoFragment.java:112-113 printed (empty); same registration/dispatch as row 15. |
| 17 | AddTorrentInfoFragment$2.<init> | REACHABLE | SOURCE | Field tagsListener declared AddTorrentInfoFragment.java:163-183; registered via binding.info.tagsList.setListener(tagsListener) in onViewCreated:120. |
| 18 | AddTorrentInfoFragment$2.lambda$onAddTagClick$0 | REACHABLE | INFERRED | AddTorrentInfoFragment.java:166-167 map lambda inside onAddTagClick; Rx dispatch INFERRED; extracts tag.id. |
| 19 | AddTorrentInfoFragment$2.lambda$onAddTagClick$1 | REACHABLE | INFERRED | AddTorrentInfoFragment.java:169-175 subscribe lambda inside onAddTagClick; Rx dispatch INFERRED; launches selectTag:175. |
| 20 | AddTorrentInfoFragment$2.onAddTagClick | REACHABLE | INFERRED | Body AddTorrentInfoFragment.java:165-179 printed; TorrentTagsList listener dispatch INFERRED (listener set at onViewCreated:120). |
| 21 | AddTorrentInfoFragment$2.onTagRemoved | REACHABLE | INFERRED | Body AddTorrentInfoFragment.java:181-183 printed (viewModel.removeTag); same listener dispatch INFERRED. |
| 22 | AddTorrentMutableParams.<init> | REACHABLE | SOURCE | Construction site printed at AddTorrentViewModel.java:81 (`new AddTorrentMutableParams()` as a field initialiser); ViewModel obtained in-app at AddTorrentActivity.java:103-104. See upgrade note above. |
| 23 | AddTorrentMutableParams.getDirName | REACHABLE | INFERRED | Definition AddTorrentMutableParams.java:83-86, @Bindable (:82); layout binds it (add_torrent_info.xml save_path `android:text="@{viewModel.mutableParams.dirName}"`), and InfoFragment onViewCreated:102 sets the viewModel on the binding. Generated `executeBindings` read of a @Bindable getter is INFERRED (generated code not in the upload) — see binding-getter convention note below. |
| 24 | AddTorrentMutableParams.getDirPath | REACHABLE | SOURCE | Definition AddTorrentMutableParams.java:77-80; printed callers: InfoFragment.java:160 (chooseDir callback set) and :200 (showChooseDirDialog get). |
| 25 | AddTorrentMutableParams.getName | REACHABLE | SOURCE | Definition AddTorrentMutableParams.java:66-69, @Bindable (:65); printed callers AddTorrentActivity.java:364 (addTorrent reads getName) and AddTorrentViewModel.java:482 (addTorrent check). |
| 26 | AddTorrentMutableParams.getSource | REACHABLE | SOURCE | Definition AddTorrentMutableParams.java:45-48; printed callers AddTorrentViewModel.java:269 and :474. Was OPEN in the prior proposal; resolved in this pass (see above). |
| 27 | AddTorrentMutableParams.getStorageFreeSpace | REACHABLE | SOURCE | Definition AddTorrentMutableParams.java:95-98, @Bindable (:94); printed caller AddTorrentViewModel.java:552; layout also binds it (fileSize). Was INFERRED in the prior proposal; upgraded to SOURCE in this pass. |
| 28 | AddTorrentMutableParams.isFirstLastPiecePriority | REACHABLE | SOURCE | Definition AddTorrentMutableParams.java:143-146; printed caller AddTorrentActivity.java:230 (onMutableParamsChanged). |
| 29 | AddTorrentMutableParams.isFromMagnet | REACHABLE | SOURCE | Definition AddTorrentMutableParams.java:55-58; printed callers AddTorrentViewModel.java:270 and :471. Was OPEN in the prior proposal; resolved in this pass. |
| 30 | AddTorrentMutableParams.isIgnoreFreeSpace | REACHABLE | SOURCE | Definition AddTorrentMutableParams.java:131-134; printed caller AddTorrentActivity.java:223. |
| 31 | AddTorrentMutableParams.isSequentialDownload | REACHABLE | SOURCE | Definition AddTorrentMutableParams.java:107-110; printed caller AddTorrentActivity.java:209. |
| 32 | AddTorrentMutableParams.isStartAfterAdd | REACHABLE | SOURCE | Definition AddTorrentMutableParams.java:119-122; printed caller AddTorrentActivity.java:216. |
| 33 | AddTorrentMutableParams.setDirName | REACHABLE | SOURCE | Definition AddTorrentMutableParams.java:88-91 (notifyPropertyChanged BR.dirName); printed caller AddTorrentViewModel.java:358. Was OPEN in the prior proposal; resolved in this pass. |
| 34 | AddTorrentMutableParams.setFirstLastPiecePriority | REACHABLE | SOURCE | Definition AddTorrentMutableParams.java:148-151; printed caller AddTorrentActivity.java:161 (fillMutableParams). |
| 35 | AddTorrentMutableParams.setFromMagnet | REACHABLE | SOURCE | Definition AddTorrentMutableParams.java:60-63; printed caller AddTorrentViewModel.java:235. Was OPEN in the prior proposal; resolved in this pass. |
| 36 | AddTorrentMutableParams.setIgnoreFreeSpace | REACHABLE | SOURCE | Definition AddTorrentMutableParams.java:136-139; printed caller AddTorrentActivity.java:155. |
| 37 | AddTorrentMutableParams.setName | REACHABLE | SOURCE | Definition AddTorrentMutableParams.java:71-74 (notifyPropertyChanged BR.name); printed caller AddTorrentViewModel.java:344; layout also binds it two-way (`@={viewModel.mutableParams.name}`). Was OPEN in the prior proposal; resolved in this pass. |
| 38 | AddTorrentMutableParams.setSequentialDownload | REACHABLE | SOURCE | Definition AddTorrentMutableParams.java:112-115; printed caller AddTorrentActivity.java:143. |
| 39 | AddTorrentMutableParams.setSource | REACHABLE | SOURCE | Definition AddTorrentMutableParams.java:50-53; printed callers AddTorrentViewModel.java:227,232,258. Was OPEN in the prior proposal; resolved in this pass. |
| 40 | AddTorrentMutableParams.setStartAfterAdd | REACHABLE | SOURCE | Definition AddTorrentMutableParams.java:124-127; printed caller AddTorrentActivity.java:149. |

## Counts — mechanically verified

- Rows in table: 40, sequence 1–40 intact, in plan order.
- REACHABLE proposed: 40.
- UNREACHABLE proposed: 0.
- OPEN: 0.
- confirmed_by: SOURCE 24 / INFERRED 16.
- **Verified for merge: 0 rows.** This part is UNVERIFIED until the main agent
  spot-checks 1 in 5, runs `py_compile`, and the Mac build/C1 return.

## Strict-entry caveat — CLOSED in this pass (with one nuance)

Same as batch 79, printed fresh here: AddTorrentActivity is exported with SEND and
VIEW intent filters (AndroidManifest.xml:62-72+), and the activity → pager →
InfoFragment chain is printed end-to-end above, so no row in this batch reverts
under an entry rule that accepts a manifest-registered external-intent entry.
Nuance, recorded not decided: the manifest has no MAIN/LAUNCHER filter for
AddTorrentActivity, so under a stricter rule requiring a launcher MAIN entry for
every route, these rows would still revert to OPEN. The merger must pick that rule;
this file does not decide it.

## Undecided conventions recorded per row, not decided

1. **Binding-getter convention (row 23, getDirName):** this file marks a @Bindable
   getter REACHABLE via the generated `executeBindings` read path once the layout
   binding is printed — the same convention batches 65–66 used. Other batches
   (Agent 21 batches 63–64, Agent 18 batch 58 FileManager `getViewModel`) deliberately
   left such getters OPEN because `executeBindings` reads the field, not the getter.
   If the merger picks the stricter convention, row 23 reverts to OPEN; no other
   row in this batch depends on that convention (rows 25/27 have direct callers,
   rows 33/37 have direct callers plus layout bindings).
2. **Lambda/anonymous numbering is by source order, NOT verified against bytecode**
   — merger must confirm, especially lambda$new$1/$2 and $1/$2 in
   AddTorrentInfoFragment. A swap within a group would not change any label.
3. **Empty-body listener methods (rows 15–16)** are REACHABLE, not UNREACHABLE:
   registration at onViewCreated:106 and framework dispatch are printed/standard,
   and an empty body is still invoked. This is a labelling judgement, flagged for
   the merger's 1-in-5 spot-check.

## Gaps the merger must close before merging

1. **Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1** — not run here.
2. **No UNREACHABLE row is claimed:** no saved full-repo grep was run, so absence
   of a caller is never used as evidence here; that matters only if a future
   revision flips a row, since all 40 rows here have a printed caller or
   registration site.
3. **No other gap:** all 40 plan rows are judged (40 proposed, 0 OPEN); no row was
   guessed, no row rests on a 429 response, and no row rests on the prior proposal
   alone — the prior proposal's 6 OPEN rows were closed from the fresh ViewModel
   print above, and its 2 INFERRED rows (22, 27) were upgraded from fresh prints.

## Not claimed

No build, sampler, grep, or C1 check was run — a true git clone of the repo fails
in this VM with no credential device (named missing check, not passed); build and
C1 run on the user's Mac after a push, so both are marked "not run" here.
Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]) (task instruction). Nothing was edited in `graph_def.py`, `out/`,
`PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.
