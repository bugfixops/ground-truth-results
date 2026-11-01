**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

**REVISION 2026-11-01 (OPEN-closing pass): NO label changed in this file.** Every OPEN row was re-derived from 10 freshly connector-fetched files (branch work-2026-10-31, one at a time with ~25 s pauses, no fresh HTTP 429), saved in `~/workspace/b818284-openclose-src/`: AddTorrentMutableParams.java (171 lines, SHA ae21c26f…), DownloadableFileItem.java (86 lines, SHA 18e64cd3…), CreateTorrentMutableParams.java (190 lines, SHA 29c46f89…), AddTorrentViewModel.java (574 lines, SHA bec2f6ee…), AddTorrentActivity.java (577 lines, SHA 08c354d9…), AddTorrentFilesFragment.java (197 lines, SHA b10cfc53…), AddTorrentInfoFragment.java (244 lines, SHA 6be37532…), CreateTorrentViewModel.java (406 lines, SHA 99b9dff0…), CreateTorrentDialog.java (561 lines, SHA bfb6fc62…), plus FileItem.java (131 lines, SHA cda7f53d…) for the parent-dispatch check. Grep over that fresh corpus (`grep_fresh_corpus.txt` in the same directory) found NO caller of any OPEN row and NO parcel site for DownloadableFileItem. That printed-corpus grep is NOT a saved full-repo grep, so no row flips to UNREACHABLE; all OPEN rows stay OPEN pending a saved full-repo grep. Counts below were mechanically re-verified from the label column after this revision and are unchanged. Build: not run. C1: not run.

**REVISION 2026-11-01 (OPEN-closing round 2, group G13): NO label changed in this file. 0 flips.** The sole OPEN row (row 2) was re-checked against the already-fetched 252-file app-Java tree `~/workspace/ruleF-src/` (no new GitHub connector fetch was needed — all files needed were already local, so no 429 was hit and none was risked). Saved greps in `~/workspace/b818284-openclose2-src/`: `grep_AddTorrentMutableParams.txt` (3 hits: class declaration :31, toString definition :158, ViewModel field declaration :81 — no caller), `grep_mutableParams_all.txt` (all `mutableParams` uses in addtorrent are getter/setter/field uses only; the only `.toString()` hits near them are `uri.toString()` on Uri at AddTorrentViewModel:227/:232, not on the params object), `grep_toString.txt` (122 `.toString()` hits tree-wide, none naming an AddTorrentMutableParams instance). That tree is app Java only — it excludes res XML, generated databinding code, and library/framework code — so it is NOT a saved full-repo grep and, per the task rule, absence in it never flips this row to UNREACHABLE. CONDITIONAL TABLE for row 2 (toString convention, UNDECIDED project-wide, recorded not decided): (a) status quo / strict printed-caller rule → stays OPEN; (b) a printed log / concatenation / `String.valueOf` / `setText` site naming an AddTorrentMutableParams instance is found → flips to REACHABLE (confirmed_by per that site: SOURCE if the call is printed, INFERRED if it crosses unprinted dispatch); (c) a saved full-repo grep covering app Java + res XML + generated databinding returns zero such sites AND the merger adopts an absence-as-UNREACHABLE rule for toString → flips to UNREACHABLE `no_trigger_in_app`. No other row changed; counts below were mechanically re-verified after this revision and are unchanged. Build: not run. C1: not run.

# LibreTorrent batch 81 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to `graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** Build and C1 run on the user's Mac after a push, so both are marked "not run" here, never passed. No sampler or saved full-repo grep was run or is claimed.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 81 only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. Prior proposal `~/workspace/libretorrent-batch81-proposal.md` was used as an INPUT / lead list only; every row below was checked against printed source in this pass, and no prior verdict was copied as a result.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 81 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the local plan copy `~/workspace/agent27-plan.tsv` (4,732 rows total; plan blob SHA `0104806dd666c840049b3db52823d4b384fa1c92`), all `TODO_CANDIDATE_REACHABLE` (generator candidates, not evidence), in plan order. Method names and JVM descriptors below match the plan row for row. Classes: AddTorrentMutableParams (2), AddTorrentPagerAdapter (3), AddTorrentViewModel (33), AddTorrentViewModel$1 (2), AddTorrentViewModel$2 (3 rows counting its lambda).

## Printed source used in this pass

Fresh connector fetches from branch `work-2026-10-31`, one file at a time with pauses, saved in `~/workspace/b81-82-src/` (base path `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`). No fresh HTTP 429 was hit in this pass.

- `ui/addtorrent/AddTorrentViewModel.java` — fresh, SHA `bec2f6eec2a538bd7223095b87014183530f4534`, 574 lines. This closes the prior session's carried-forward gap: the prior proposal reused a batch 20/21 local copy for this file; every ViewModel citation below was re-checked against this fresh fetch, and all line numbers held.
- `ui/addtorrent/AddTorrentMutableParams.java` — fresh, SHA `ae21c26ff4eb1eaadbb6e1c4a91f716fce5f073a`, 171 lines. This closes the prior session's gap: the definition file for rows 1–2 was not printed there.
- `ui/addtorrent/AddTorrentActivity.java` — fresh, SHA `08c354d985cd7548368dd84bdc0c8d573a678fe5`, 577 lines.
- `ui/addtorrent/AddTorrentPagerAdapter.java` — fresh, SHA `b96347f79d1cecbfd7b87b330212c09a53ca4377`, 56 lines; text identical to the prior session's print.
- `ui/addtorrent/AddTorrentFilesFragment.java` — fresh, SHA `b10cfc539cbadbb4c8eb37d88ecfe4e320c5ac88`, 197 lines; citations identical to the prior session's print.
- `ui/addtorrent/AddTorrentInfoFragment.java` — fresh, SHA `6be3753268b5ff0bc7c8da8a896a4866fa76763e`, 244 lines; citations identical to the prior session's print.
- `ui/createtorrent/CreateTorrentActivity.java`, `ui/createtorrent/CreateTorrentDialog.java`, `ui/addtorrent/DownloadableFileItem.java`, `ui/addtorrent/DownloadableFilesAdapter.java` — also freshly fetched this pass (see batch 82 file); used here only for the shared entry-trunk note and for batch 82.

Not freshly fetched this pass, and not relied on for any row's sole citation: `ui/main/MainFragment.java` (only the `createTorrentDialog()` → `startActivity(CreateTorrentActivity)` line cited in the prior proposal, from a local copy). The launcher → MainActivity → MainFragment steps were not re-printed this session — see strict-entry caveat below.

## Shared entry route (printed this pass)

AddTorrentActivity.onCreate: `ViewModelProvider` at :103, `provider.get(AddTorrentViewModel.class)` at :104 → AddTorrentViewModel.<init> :128–147. AddTorrentActivity.initLayout :288 `new AddTorrentPagerAdapter(this)` + :289 `viewpager.setAdapter(adapter)` → FragmentStateAdapter dispatch → AddTorrentPagerAdapter.createFragment :41–50 (INFO_FRAG_POS → AddTorrentInfoFragment.newInstance, FILES_FRAG_POS → AddTorrentFilesFragment.newInstance) and getItemCount :53–55 (returns NUM_FRAGMENTS = 2). AddTorrentInfoFragment.onViewCreated uses `ViewModelProvider(activity).get(AddTorrentViewModel.class)` at :102.

**STRICT-ENTRY CAVEAT (undecided convention, recorded not decided):** the launcher → MainActivity → MainFragment steps were not re-printed this session, so under a strict printed-launcher rule every REACHABLE row below reverts to OPEN. The verdicts below follow the activity-anchored convention of the prior batches (and of batch 82). The merger must pick one strict-entry convention for all batches; labels below do not decide it.

## confirmed_by convention used here

- SOURCE: a direct app-to-app call site naming the method is printed in app source, or a standard Android callback whose registration is printed (Activity/Fragment lifecycle, FragmentStateAdapter, View click listeners, anonymous-class instantiation inside a printed method).
- INFERRED: the route crosses a dispatch step NOT printed from its own source — RxJava subscribe/observe, data-binding Observable callbacks, Thread.start → lambda, AsyncTask.executeOnExecutor → doInBackground/onPostExecute, or JVM class initialisation (<clinit>).
- No row is flipped to UNREACHABLE on absence in the printed subset; rows with no printed caller stay OPEN pending a saved full-repo grep. No connector `search_code` 0-result was used as evidence of absence.

## Per-row verdicts

| # | Method | Label | confirmed_by | Printed citation / route |
|---|---|---|---|---|
| 1 | AddTorrentMutableParams.setStorageFreeSpace (J)V | REACHABLE | INFERRED | Fresh definition AddTorrentMutableParams.java:100–104 (`setStorageFreeSpace`, notifies BR.storageFreeSpace). Printed caller AddTorrentViewModel.java:357 `mutableParams.setStorageFreeSpace(fs.getDirAvailableBytes(dirPath))` inside dirPathCallback ($2.onPropertyChanged :348–366); reaching that callback crosses data-binding Observable dispatch, hence INFERRED. |
| 2 | AddTorrentMutableParams.toString ()Ljava/lang/String; | OPEN | — | Fresh definition AddTorrentMutableParams.java:156–170. No printed caller in any file fetched this session (or in the prior proposal's printed set). Re-checked 2026-11-01 on the 10 fresh files above: no caller — the only toString() calls in that corpus are on Uri/Exception objects, logging sites log exceptions only, and mutableParams uses are getter/setter calls only. Pending saved full-repo grep; this printed-corpus grep is NOT a full-repo grep. NOT `no_trigger_in_app` on this evidence — toString is a common logging/concatenation route, and no grep closes it. ROUND-2 re-check 2026-11-01 (G13, no label change): re-grepped over the 252-file tree `~/workspace/ruleF-src/` (saved `~/workspace/b818284-openclose2-src/grep_AddTorrentMutableParams.txt`, 3 hits, and `grep_toString.txt`, 122 hits) — still no caller naming an AddTorrentMutableParams instance; `mutableParams` uses tree-wide are getter/setter/field uses only. App-Java-only tree, so still NOT a full-repo grep. CONDITIONAL TABLE (toString convention UNDECIDED, recorded not decided): strict printed-caller rule → OPEN; printed log/concat/`String.valueOf`/`setText` site naming the params instance → REACHABLE; saved full-repo grep (Java + res XML + generated databinding) zero sites AND merger adopts absence rule → UNREACHABLE `no_trigger_in_app`. Named resolver: that saved full-repo grep, plus the merger's toString-convention decision. |
| 3 | AddTorrentPagerAdapter.<init> (FragmentActivity)V | REACHABLE | SOURCE | Fresh AddTorrentActivity.java:288 `adapter = new AddTorrentPagerAdapter(this)`; def PagerAdapter.java:35–37. |
| 4 | AddTorrentPagerAdapter.createFragment (I)Fragment | REACHABLE | SOURCE | Standard FragmentStateAdapter callback after setAdapter, AddTorrentActivity.java:289; def PagerAdapter.java:41–50. |
| 5 | AddTorrentPagerAdapter.getItemCount ()I | REACHABLE | SOURCE | Same registration; def PagerAdapter.java:53–55 returns NUM_FRAGMENTS (2). |
| 6 | AddTorrentViewModel.<clinit> ()V | REACHABLE | INFERRED | JVM class initialisation on first active use: ViewModelProvider.get, AddTorrentActivity.java:104. Non-constant static TAG at ViewModel.java:79 (`class.getSimpleName()`). |
| 7 | AddTorrentViewModel.<init> (Application)V | REACHABLE | SOURCE | AddTorrentActivity.java:103–104 provider.get; also InfoFragment.java:102. Def ViewModel.java:128–147. |
| 8 | AddTorrentViewModel.addTag (TagInfo)V | REACHABLE | SOURCE | Fresh InfoFragment.java:144 `viewModel.addTag(tag)` (activity-result callback); def ViewModel.java:157–160. |
| 9 | AddTorrentViewModel.addTorrent ()Z | REACHABLE | SOURCE | Fresh AddTorrentActivity.java:374 `viewModel.addTorrent()`; def ViewModel.java:466–546. |
| 10 | AddTorrentViewModel.cancelFetchMagnet ()V | REACHABLE | SOURCE | Private; called by finish(), ViewModel.java:562; finish called AddTorrentActivity.java:567. Def :565–573. |
| 11 | AddTorrentViewModel.checkFreeSpace ()Z | REACHABLE | SOURCE | Private; called by addTorrent(), ViewModel.java:495. Def :548–556. |
| 12 | AddTorrentViewModel.chooseDirectory (String)V | REACHABLE | SOURCE | Fresh FilesFragment.java:188 `viewModel.chooseDirectory(item.name)`; def ViewModel.java:425–434. |
| 13 | AddTorrentViewModel.finish ()V | REACHABLE | SOURCE | AddTorrentActivity.finish():567 `viewModel.finish()`; def ViewModel.java:558–563. |
| 14 | AddTorrentViewModel.getChildren (BencodeFileTree)List | REACHABLE | SOURCE | Called by updateChildren(), ViewModel.java:451; updateChildren reached via updateCurDir :447 / makeFileTree :400 / selectFile :442. Def :411–423. |
| 15 | AddTorrentViewModel.getCurrentTags ()List | REACHABLE | SOURCE | Fresh InfoFragment.java:166 `viewModel.getCurrentTags()`; def ViewModel.java:149–151. |
| 16 | AddTorrentViewModel.getDecodeState ()LiveData | REACHABLE | SOURCE | Fresh AddTorrentActivity.java:307 `viewModel.getDecodeState().observe(...)`; def ViewModel.java:167–169. |
| 17 | AddTorrentViewModel.getSelectedFileIndexes ()Set | REACHABLE | SOURCE | Private; called by addTorrent(), ViewModel.java:487. Def :454–464. |
| 18 | AddTorrentViewModel.lambda$addTorrent$5 (AddTorrentParams,Exception[])V | REACHABLE | INFERRED | Thread lambda in addTorrent(), ViewModel.java:527–534, run via t.start() :535 (Thread dispatch not printed). Numbering by source order, not bytecode-verified; labels unaffected by a swap within this group (single Thread lambda in addTorrent). |
| 19 | AddTorrentViewModel.lambda$new$0 (Boolean)Z | REACHABLE | INFERRED | Rx filter lambda in <init>, ViewModel.java:137 `.filter((needStart) -> needStart)`; runs only on observeNeedStartEngine emission (Rx dispatch not printed). |
| 20 | AddTorrentViewModel.lambda$new$1 (Boolean)V | REACHABLE | INFERRED | Rx subscribe lambda in <init>, ViewModel.java:138 `.subscribe((needStart) -> engine.start())`; same Rx caveat. |
| 21 | AddTorrentViewModel.lambda$observeFetchedMetadata$3 (TorrentMetaInfo)V | REACHABLE | INFERRED | Success callback, ViewModel.java:330–333 (info.set + FETCHING_MAGNET_COMPLETED); Rx dispatch not printed. |
| 22 | AddTorrentViewModel.lambda$observeFetchedMetadata$4 (Throwable)V | REACHABLE | INFERRED | Error callback, ViewModel.java:334 (ERROR state); same Rx caveat. |
| 23 | AddTorrentViewModel.lambda$startDecode$2 (Uri,Boolean)V | REACHABLE | INFERRED | Rx subscribe lambda in startDecode(), ViewModel.java:188–194 (calls startDecodeTask :190); Rx dispatch not printed. |
| 24 | AddTorrentViewModel.makeFileTree ()V | REACHABLE | SOURCE | Fresh AddTorrentActivity.java:345 `viewModel.makeFileTree()` (decode-completed branch, onStopDecode); def ViewModel.java:368–401. |
| 25 | AddTorrentViewModel.observeFetchedMetadata (Single)V | REACHABLE | INFERRED | Private; called by TorrentDecodeTask.doInBackground magnet branch, ViewModel.java:243; reaching doInBackground crosses AsyncTask dispatch (see batch 82 rows 5–8), hence INFERRED. Def :328–335. |
| 26 | AddTorrentViewModel.observeTags ()Observable | REACHABLE | SOURCE | Fresh InfoFragment.java:187 `viewModel.observeTags()` in subscribeTags(), called from onStart; def ViewModel.java:153–155. |
| 27 | AddTorrentViewModel.onCleared ()V | REACHABLE | SOURCE | Standard ViewModel lifecycle callback (framework calls on Activity destroy); def ViewModel.java:175–180 (clears disposable, removes callbacks). No app-code call site exists by design. |
| 28 | AddTorrentViewModel.removeTag (TagInfo)V | REACHABLE | SOURCE | Fresh InfoFragment.java:182 `viewModel.removeTag(info)` (tagsListener.onTagRemoved); def ViewModel.java:162–165. |
| 29 | AddTorrentViewModel.restartForegroundNotification ()V | REACHABLE | SOURCE | Fresh AddTorrentActivity.java:123 `viewModel.restartForegroundNotification()` (notification-permission callback); def ViewModel.java:171–173. |
| 30 | AddTorrentViewModel.selectFile (String,Z)V | REACHABLE | SOURCE | Fresh FilesFragment.java:194 `viewModel.selectFile(item.name, selected)`; def ViewModel.java:436–443. |
| 31 | AddTorrentViewModel.startDecode (Uri)V | REACHABLE | SOURCE | Fresh AddTorrentActivity.java:312 `viewModel.startDecode(uri)` (UNKNOWN decode state); def ViewModel.java:182–195. |
| 32 | AddTorrentViewModel.startDecodeTask (Uri)V | REACHABLE | INFERRED | Called only from the Rx subscribe lambda in startDecode(), ViewModel.java:190; Rx crossing, hence INFERRED. Def :197–200 (new TorrentDecodeTask + executeOnExecutor). |
| 33 | AddTorrentViewModel.upToParentDirectory ()V | REACHABLE | SOURCE | Fresh FilesFragment.java:186 `viewModel.upToParentDirectory()`; def ViewModel.java:407–409. |
| 34 | AddTorrentViewModel.updateChildren ()V | REACHABLE | SOURCE | Private; called by updateCurDir :447, makeFileTree :400, selectFile :442. Def :450–452. |
| 35 | AddTorrentViewModel.updateCurDir (BencodeFileTree)V | REACHABLE | SOURCE | Private; called by makeFileTree :400, upToParentDirectory :408, chooseDirectory :433. Def :445–448. |
| 36 | AddTorrentViewModel$1.<init> (AddTorrentViewModel)V | REACHABLE | SOURCE | Anonymous infoCallback field, ViewModel.java:337–346; field initialisers run inside <init> (row 7 route). |
| 37 | AddTorrentViewModel$1.onPropertyChanged (Observable,I)V | REACHABLE | INFERRED | infoCallback registered ViewModel.java:140; fired by data-binding ObservableField dispatch when info.set(...) runs (TorrentDecodeTask :242, :331, :293 in the prior print; :331 re-checked fresh). Dispatch not printed, hence INFERRED. Def :339–345. |
| 38 | AddTorrentViewModel$2.<init> (AddTorrentViewModel)V | REACHABLE | SOURCE | Anonymous dirPathCallback field, ViewModel.java:348–366; instantiated inside <init> (row 7 route). |
| 39 | AddTorrentViewModel$2.lambda$onPropertyChanged$0 (Uri)V | REACHABLE | INFERRED | Completable runnable inside dirPathCallback, ViewModel.java:355–362, run via subscribeOn(Schedulers.io()).subscribe() :363–364 (Rx dispatch not printed). |
| 40 | AddTorrentViewModel$2.onPropertyChanged (Observable,I)V | REACHABLE | INFERRED | dirPathCallback registered ViewModel.java:141; fired by ObservableField dispatch when getDirPath().set(...) runs (ViewModel.java:146; InfoFragment.java:160). Dispatch not printed, hence INFERRED. Def :350–365. |

## Counts — batch 81 (proposed, NOT verified)

- REACHABLE proposed: 39 / 40 (SOURCE 26, INFERRED 13)
- UNREACHABLE proposed: 0 / 40
- OPEN: 1 / 40 (row 2, AddTorrentMutableParams.toString)
- Verified for merge: 0 / 40

## Changes vs the prior proposal (all else held on fresh re-check)

None of the 39 REACHABLE verdicts changed. The two prior gaps are now closed as evidence (not as verdict changes): AddTorrentViewModel.java is now freshly fetched (SHA above, all prior ViewModel line numbers held), and AddTorrentMutableParams.java is now freshly fetched (rows 1–2 definitions confirmed; row 2 stays OPEN because a definition is not a caller).

## Still owed before merge

1. Saved full-repo grep for row 2 (toString) — one hit flips it to REACHABLE.
2. Re-print the launcher → MainActivity → MainFragment steps if the strict-entry rule is applied (see caveat above).
3. Main-agent spot-check 1 in 5, py_compile, build, Mac build/C1 — not run here.
4. Lambda numbering is source-order, not bytecode-verified; a swap would not change any label in this batch (each lambda group is anchored by its enclosing method and signature).
