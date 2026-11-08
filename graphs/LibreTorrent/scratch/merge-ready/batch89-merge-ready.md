**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 89 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 89 only, max 40 methods, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, from printed source. The prior proposal
  (`~/workspace/libretorrent-batch89-proposal.md`) was used as an INPUT / lead list only;
  rows below were re-checked in this session against printed source (see Sources), and no
  proposal verdict was copied as a result.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 89 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, plan SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, all status TODO_CANDIDATE_REACHABLE, all
current label "REACHABLE (generator candidate, no hand route yet)" — candidates, not evidence.
Rows 1-39: DetailTorrentViewModel and its $1/$2 callbacks. Row 40:
MsgDetailTorrentViewModel.<init>.

## Sources printed / re-read in this session

Fresh connector fetch in THIS session, branch `work-2026-10-31`, one file at a time:
- `ui/detailtorrent/DetailTorrentViewModel.java` — 610 lines, connector SHA
  `6e4ef82f455957298bfb6bf4513c4a35c799a1a6`, identical to the prior-session fresh copy
  (`~/workspace/b89-90-src/dvm_fresh.java`) except for the connector's download-notice
  prefix on line 1. Spot-checked in the fresh text: addTag :151-152, removeTag :155,
  observeTags :147, makeMagnet :381-382, observeTorrentInfoPair :191,
  mutableParamsCallback :112/:122/:136/:138/:443, infoCallback :113/:123/:133/:135/:467,
  setTorrentId :126, getFilePath :262, applyPriority :326. No fresh HTTP 429 was hit.

Re-read in this session from `~/workspace/b89-90-src/` (fresh connector fetches in the
prior session, connector SHAs as recorded there; local hash-object values differ, likely
from the stripped download-notice prefix, so the merger should re-verify these four
fresh if it needs byte identity):
- `ui/detailtorrent/pages/DetailTorrentInfoFragment.java` — 324 lines, prior SHA
  `f7d056f5f960c5a7097cf50385ed0ac92dc0595e`. Re-checked: subscribeTags :177-178,
  tagsListener.onTagRemoved :169-170, selectTag ActivityResult lambda :139-147,
  binding.setViewModel :105.
- `ui/detailtorrent/MsgDetailTorrentViewModel.java` — prior SHA
  `9974c5b60051ae7feed0849f3f3752557788d7eb`.
- `ui/detailtorrent/TorrentDetailsInfo.java` — prior SHA
  `7ea66875e83d4921bb861ff6cb810ff875f64b8f`.
- `ui/detailtorrent/TorrentDetailsMutableParams.java` — prior SHA
  `e38bdbe9c17034de3c2109a4157ab5c23156ca05`.

NOT freshly fetched in this session — citations from prior-session local copies,
merger must re-verify line numbers before merging:
- `ui/detailtorrent/DetailTorrentFragment.java` (832 lines)
- `ui/detailtorrent/pages/peers/DetailTorrentPeersFragment.java`
- `ui/detailtorrent/pages/pieces/DetailTorrentPiecesFragment.java`
- `ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java`
- `ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java`
- `ui/detailtorrent/DetailPagerAdapter.java`

No full-repo grep was run, so no UNREACHABLE label is claimed for any row.
No connector `search_code` 0-result was used as evidence of absence.

## confirmed_by convention used here

SOURCE = a direct app-to-app call site naming the method is printed in app source
(including a printed lambda body calling it, or a printed `new` construction).
INFERRED = the method is reached only through unprinted framework/library dispatch
(lifecycle, ViewModelProvider instantiation, data-binding property callbacks, RxJava
subscription/emission, method references, view click / ActivityResult dispatch).
This is the per-row convention, not the whole-route convention used in some earlier
batches; labels are unaffected, only `confirmed_by` would change at merge if the
merger adopts the whole-route convention.
Lambda $ numbering for DetailTorrentViewModel matches source order in the fresh file
(addTag $0, removeTag $1, getFilePath $2, applyPriority map $3 / subscribe $4,
startMakeFileTree subscribe $5, updateFiles runnable $6); $1 = mutableParamsCallback
(defined first, DVM:443), $2 = infoCallback (DVM:467). Numbering is source-order,
NOT bytecode-verified.

## Shared trunk (proposed, strict-entry caveat below)

DetailTorrentFragment.onViewCreated (local copy, NOT freshly fetched here):
ViewModelProvider provider :162, viewModel = provider.get(DetailTorrentViewModel.class) :163,
viewModel.setTorrentId(torrentId) :167, msgViewModel = provider.get(MsgDetailTorrentViewModel.class) :168,
DetailPagerAdapter created :185. onStart :233-239 calls subscribeTorrentInfo(),
subscribeMsgViewModel(), subscribeFreeSpaceError(). DetailPagerAdapter.createFragment
returns the page fragments (INFO :59-60, FILES :61-62, TRACKERS :63-64, PEERS :65-66,
PIECES :67-68 in the prior pass's fresh copy). The launcher → DetailTorrentActivity →
DetailTorrentFragment step was NOT printed in this pass, so under a strict entry-route
rule all 40 rows below revert to OPEN. They are judged REACHABLE (proposed) on the
fragment-anchored trunk, as in prior detail batches. This strict-entry convention is
UNDECIDED for the project — it is recorded per row, not decided here.

## Counts — proposed, not verified (mechanically verified: 40 rows, sequence 1-40 intact)

- REACHABLE proposed: 40 / 40 (22 SOURCE / 18 INFERRED)
- UNREACHABLE proposed: 0
- OPEN: 0
- Verified for merge: 0

## Rows (plan order)

| # | Method | Label | confirmed_by | Printed route / citation |
|---|---|---|---|---|
| 1 | DetailTorrentViewModel.lambda$addTag$0 | REACHABLE proposed | INFERRED | Runnable inside addTag, DVM:151-152 (`Completable.fromRunnable(() -> repo.addTag(...))`). addTag subscribed by DetailTorrentInfoFragment selectTag ActivityResult lambda :139-147. Rx dispatch INFERRED. |
| 2 | DetailTorrentViewModel.lambda$applyPriority$3 | REACHABLE proposed | INFERRED | Map lambda in applyPriority, DVM:326-329. applyPriority called by DetailTorrentFilesFragment :353 and :502 (local copy). Rx chain dispatch INFERRED. |
| 3 | DetailTorrentViewModel.lambda$applyPriority$4 | REACHABLE proposed | INFERRED | Subscribe lambda in applyPriority, DVM:332-335 (setPriority, updateChildren, setPrioritiesChanged). Same FilesFragment callers as row 2. |
| 4 | DetailTorrentViewModel.lambda$getFilePath$2 | REACHABLE proposed | INFERRED | Single.fromCallable lambda in getFilePath, DVM:262-289. getFilePath called by DetailTorrentFilesFragment :340 and subscribed there (local copy). Rx dispatch INFERRED. |
| 5 | DetailTorrentViewModel.lambda$removeTag$1 | REACHABLE proposed | INFERRED | Runnable inside removeTag, DVM:155-156. removeTag subscribed by DetailTorrentInfoFragment tagsListener.onTagRemoved :169-178. Rx dispatch INFERRED. |
| 6 | DetailTorrentViewModel.lambda$startMakeFileTree$5 | REACHABLE proposed | INFERRED | Subscribe lambda `() -> updateCurDir(fileTree)` in startMakeFileTree, DVM:522-526. Rx dispatch INFERRED. |
| 7 | DetailTorrentViewModel.lambda$updateFiles$6 | REACHABLE proposed | INFERRED | Runnable inside updateFiles, DVM:570-596. updateFiles called by infoCallback :473. Rx + property-callback dispatch INFERRED. |
| 8 | DetailTorrentViewModel.makeFileTree | REACHABLE proposed | INFERRED | Definition DVM:529-568. Reached only via method reference `this::makeFileTree` in startMakeFileTree :523 inside a Completable. Rx/method-ref dispatch INFERRED. |
| 9 | DetailTorrentViewModel.makeMagnet | REACHABLE proposed | SOURCE | Called directly by DetailTorrentFragment :598 (`viewModel.makeMagnet(includePriorities)`) (local copy). Definition DVM:381-382. |
| 10 | DetailTorrentViewModel.makeOpenFileIntent | REACHABLE proposed | SOURCE | Called directly by DetailTorrentFilesFragment :532 (`startActivity(viewModel.makeOpenFileIntent(...))`) (local copy). Definition DVM:398-410. |
| 11 | DetailTorrentViewModel.observeAdvancedTorrentInfo | REACHABLE proposed | SOURCE | Called directly by DetailTorrentFragment.subscribeTorrentInfo :271 (local copy). Definition DVM:171-172. |
| 12 | DetailTorrentViewModel.observeFreeSpaceError | REACHABLE proposed | SOURCE | Called directly by DetailTorrentFragment.subscribeFreeSpaceError :292 (local copy). Definition DVM:159-160. |
| 13 | DetailTorrentViewModel.observePeers | REACHABLE proposed | SOURCE | Called directly by DetailTorrentPeersFragment.subscribeAdapter :174 (local copy). Definition DVM:183-184. |
| 14 | DetailTorrentViewModel.observePieces | REACHABLE proposed | SOURCE | Called directly by DetailTorrentPiecesFragment.subscribeAdapter :138 (local copy). Definition DVM:187-188. |
| 15 | DetailTorrentViewModel.observeTags | REACHABLE proposed | SOURCE | Called directly by DetailTorrentInfoFragment.subscribeTags :177-178, called from onStart :201. Definition DVM:147-148. This fresh InfoFragment print closes the gap batch 88 left OPEN; it is NOT copied from batch 88. |
| 16 | DetailTorrentViewModel.observeTorrent | REACHABLE proposed | SOURCE | Called directly inside observeTorrentInfoPair, DVM:192 (`combineLatest(observeTorrent(), observeTorrentInfo(), ...)`), itself called by DetailTorrentFragment :265 (local copy). Definition DVM:175-176. |
| 17 | DetailTorrentViewModel.observeTorrentInfo | REACHABLE proposed | SOURCE | Same DVM:192 combineLatest call as row 16. Definition DVM:167-168. |
| 18 | DetailTorrentViewModel.observeTorrentInfoPair | REACHABLE proposed | SOURCE | Called directly by DetailTorrentFragment.subscribeTorrentInfo :265 (local copy). Definition DVM:191-192. |
| 19 | DetailTorrentViewModel.observeTorrentMetaInfo | REACHABLE proposed | SOURCE | Called directly by DetailTorrentFragment.subscribeTorrentInfo :256 (local copy). Definition DVM:195-196. |
| 20 | DetailTorrentViewModel.observeTrackers | REACHABLE proposed | SOURCE | Called directly by DetailTorrentTrackersFragment.subscribeAdapter :260 (local copy). Definition DVM:179-180. |
| 21 | DetailTorrentViewModel.onCleared | REACHABLE proposed | INFERRED | Definition DVM:118-124 (disposable.clear, callback removal). Invoked only by ViewModelStore lifecycle dispatch when the owner is destroyed; ViewModel obtained via provider.get, DetailTorrentFragment :163 (local copy). Lifecycle dispatch INFERRED. |
| 22 | DetailTorrentViewModel.pauseResumeTorrent | REACHABLE proposed | SOURCE | Called directly by DetailTorrentFragment menu handler :458 (local copy). Definition DVM:357-358. |
| 23 | DetailTorrentViewModel.removeTag | REACHABLE proposed | SOURCE | Called directly by DetailTorrentInfoFragment tagsListener.onTagRemoved :169-170. Definition DVM:155-156. Fresh InfoFragment print closes this; batch 88's OPEN list predates it. |
| 24 | DetailTorrentViewModel.replaceTrackers | REACHABLE proposed | SOURCE | Called directly by DetailTorrentFragment :734 (local copy). Definition DVM:349-350. |
| 25 | DetailTorrentViewModel.setSpeedLimit | REACHABLE proposed | SOURCE | Called directly by DetailTorrentFragment.setSpeedLimit() :792, itself reached from the dialog branch :324 (local copy). Definition DVM:393-395. |
| 26 | DetailTorrentViewModel.setTorrentId | REACHABLE proposed | SOURCE | Called directly by DetailTorrentFragment.onViewCreated :167 (local copy). Definition DVM:126-127. |
| 27 | DetailTorrentViewModel.startMakeFileTree | REACHABLE proposed | SOURCE | Called directly in updateInfo(TorrentMetaInfo) DVM:203 and updateInfo(Torrent,TorrentInfo) DVM:215. Definition DVM:522-526. Note: the route into updateInfo itself crosses Rx (see rows 32-34), so under a whole-route rule this row would read INFERRED, not SOURCE — convention recorded, not decided. |
| 28 | DetailTorrentViewModel.upToParentDirectory | REACHABLE proposed | SOURCE | Called directly by DetailTorrentFilesFragment.onItemClicked :336 (local copy). Definition DVM:226-227. |
| 29 | DetailTorrentViewModel.updateChildren | REACHABLE proposed | SOURCE | Called directly in updateCurDir, DVM:604 (`updateChildren()`), and via method reference in updateFiles :596. Definition DVM:607-609. |
| 30 | DetailTorrentViewModel.updateCurDir | REACHABLE proposed | SOURCE | Called directly in upToParentDirectory DVM:227 and chooseDirectory DVM:253. Definition DVM:602-604. |
| 31 | DetailTorrentViewModel.updateFiles | REACHABLE proposed | SOURCE | Called directly by infoCallback.onPropertyChanged, DVM:473. Definition DVM:570-596. |
| 32 | DetailTorrentViewModel.updateInfo(AdvancedTorrentInfo) | REACHABLE proposed | INFERRED | Reached only via Rx subscribe lambda in DetailTorrentFragment.subscribeTorrentInfo :274 (local copy). Definition DVM:218-220. |
| 33 | DetailTorrentViewModel.updateInfo(Torrent,TorrentInfo) | REACHABLE proposed | INFERRED | Reached only via Rx method reference `this::handleTorrentInfo` in DetailTorrentFragment :268 (local copy), handleTorrentInfo calling updateInfo :363. Definition DVM:206-216. |
| 34 | DetailTorrentViewModel.updateInfo(TorrentMetaInfo) | REACHABLE proposed | INFERRED | Reached only via Rx subscribe lambda in DetailTorrentFragment.subscribeTorrentInfo :259 (local copy). Definition DVM:199-204. |
| 35 | DetailTorrentViewModel$1.<init> | REACHABLE proposed | INFERRED | $1 = mutableParamsCallback anonymous class, DVM:443. Field initialisation runs when DetailTorrentViewModel is constructed, which happens only via provider.get, DetailTorrentFragment :163 (local copy). Framework instantiation INFERRED. |
| 36 | DetailTorrentViewModel$1.lambda$onPropertyChanged$0 | REACHABLE proposed | INFERRED | Completable.fromRunnable lambda inside $1.onPropertyChanged, DVM:457-464 (setStorageFreeSpace / setDirName). Runs only via Rx + databinding callback dispatch. |
| 37 | DetailTorrentViewModel$1.onPropertyChanged | REACHABLE proposed | INFERRED | Definition DVM:445-465. Invoked only by databinding Observable dispatch when a mutableParams property changes; registered DVM:112. |
| 38 | DetailTorrentViewModel$2.<init> | REACHABLE proposed | INFERRED | $2 = infoCallback anonymous class, DVM:467. Same provider.get construction basis as row 35. |
| 39 | DetailTorrentViewModel$2.onPropertyChanged | REACHABLE proposed | INFERRED | Definition DVM:469-475. Invoked only by databinding Observable dispatch when an info property changes (e.g. setAdvancedInfo); registered DVM:113. |
| 40 | MsgDetailTorrentViewModel.<init> | REACHABLE proposed | INFERRED | No `new` printed; instance obtained only via provider.get, DetailTorrentFragment :168 (also TrackersFragment :154, FilesFragment :202 in local copies). Framework instantiation INFERRED. Definition in MsgDetailTorrentViewModel.java (no explicit constructor; default). |

## Cross-batch note (not judged here, no other batch file touched)

This pass's fresh InfoFragment print closes three gaps batch 88 left OPEN — observeTags
(row 15 above), removeTag (row 23 above), and addTag's lambda $0 (row 1 above, via the
selectTag callback subscribing addTag :139-147). Those batch-88 rows still need their own
merger re-check; nothing here flips them.

## Still owed before merge

- Saved full-repo grep (not run; no UNREACHABLE claimed on absence).
- Printed launcher → DetailTorrentActivity → DetailTorrentFragment step (strict-entry caveat).
- Fresh re-verification of local-copy line numbers (DetailTorrentFragment, page fragments,
  DetailPagerAdapter) against a fresh fetch.
- Bytecode confirmation of lambda $ numbering and $1/$2 assignment.
- Main-agent spot-check (1 in 5), py_compile, build, Mac build/C1 — all not run.
- Build, sampler, C1 on a full checkout (git clone still unavailable in this VM for the
  private repo — named missing check, not passed).
