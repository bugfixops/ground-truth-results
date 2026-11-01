# LibreTorrent batch 90 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 90 only, max 40 methods, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, from printed source. The prior proposal
  (`~/workspace/libretorrent-batch90-proposal.md`) was used as an INPUT / lead list only;
  rows below were re-checked in this session against printed source (see Sources), and no
  proposal verdict was copied as a result.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 90 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, plan SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, all status TODO_CANDIDATE_REACHABLE, all
current label "REACHABLE (generator candidate, no hand route yet)" — candidates, not evidence.
Rows 1-2: MsgDetailTorrentViewModel. Rows 3-16: TorrentDetailsInfo. Rows 17-28:
TorrentDetailsMutableParams. Rows 29-40: DetailTorrentInfoFragment.

## Sources printed / re-read in this session

Fresh connector fetch in THIS session, branch `work-2026-10-31`, one file at a time:
- `ui/detailtorrent/DetailTorrentViewModel.java` — 610 lines, connector SHA
  `6e4ef82f455957298bfb6bf4513c4a35c799a1a6`, identical to the prior-session fresh copy
  (`~/workspace/b89-90-src/dvm_fresh.java`) except for the connector's download-notice
  prefix on line 1. This fresh DVM text anchors the ViewModel-side caller sites for
  rows 3-15 and 17-27 below (field initialisers :91-92, clearData :134/:137,
  initMutableParams :437-440, mutableParamsCallback :447/:453-454, infoCallback :471,
  checkParamsChanged :486/:492/:498/:504/:513, updateInfo :200/:208-209/:219,
  makeFileTree :536, checkFreeSpace :426, applyPriority subscribe :334).
  No fresh HTTP 429 was hit.

Re-read in this session from `~/workspace/b89-90-src/` (fresh connector fetches in the
prior session, connector SHAs as recorded there; local hash-object values differ, likely
from the stripped download-notice prefix, so the merger should re-verify these four
fresh if it needs byte identity):
- `ui/detailtorrent/pages/DetailTorrentInfoFragment.java` — 324 lines, prior SHA
  `f7d056f5f960c5a7097cf50385ed0ac92dc0595e`. Re-checked: onCreateView :99-115,
  binding.setViewModel :105, chooseDir callback :117-131, selectTag callback :132-145,
  click lambdas :110-111, subscribeAlertDialog :211-242, initEditNameDialog :294-323.
- `ui/detailtorrent/MsgDetailTorrentViewModel.java` — prior SHA
  `9974c5b60051ae7feed0849f3f3752557788d7eb`. Definitions: fragmentInActionMode :31-34,
  observeFragmentInActionMode :36-39.
- `ui/detailtorrent/TorrentDetailsInfo.java` — prior SHA
  `7ea66875e83d4921bb861ff6cb810ff875f64b8f`. Definitions: getTorrent :42-45,
  setTorrent :47-50, getTorrentInfo :54-57, setTorrentInfo :59-62, getAdvancedInfo :66-69,
  setAdvancedInfo :71-74, getDirName :78-81, setDirName :83-86, getStorageFreeSpace :90-93,
  setStorageFreeSpace :95-98, getMetaInfo :102-105, setMetaInfo :107-110, toString :115-125.
- `ui/detailtorrent/TorrentDetailsMutableParams.java` — prior SHA
  `e38bdbe9c17034de3c2109a4157ab5c23156ca05`. Definitions: getName :38-41,
  setName :43-46, isSequentialDownload :50-53, setSequentialDownload :55-58,
  getDirPath :62-65, setDirPath :67-70, isPrioritiesChanged :74-77,
  setPrioritiesChanged :79-82, isFirstLastPiecePriority :86-89,
  setFirstLastPiecePriority :91-94, toString :99-109.

NOT freshly fetched in this session — citations from prior-session local copies,
merger must re-verify line numbers before merging:
- `ui/detailtorrent/DetailTorrentFragment.java` (832 lines) — e.g. subscribeMsgViewModel :280,
  getTorrent/getTorrentInfo uses :431-432, getName use :541.
- `ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java` — fragmentInActionMode
  uses :308/:333.
- `ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java` — fragmentInActionMode
  uses :388/:411.
- `ui/detailtorrent/DetailPagerAdapter.java` — InfoFragment newInstance :59-60.

No full-repo grep was run, so no UNREACHABLE label is claimed for any row.
No connector `search_code` 0-result was used as evidence of absence.

## confirmed_by convention used here

SOURCE = a direct app-to-app call site naming the method is printed in app source
(including a printed lambda body calling it, or a printed `new` construction).
INFERRED = the method is reached only through unprinted framework/library dispatch
(activity lifecycle, ActivityResult dispatch, ViewModelProvider/Rx dispatch, JVM class
initialisation, generated data binding).
This is the per-row convention, not the whole-route convention used in some earlier
batches; labels are unaffected, only `confirmed_by` would change at merge if the
merger adopts the whole-route convention.
For the @Bindable getter row 5: INFERRED rests on DetailTorrentInfoFragment.onCreateView
inflating fragment_detail_torrent_info and calling binding.setViewModel(viewModel)
(:99-105); the layout XML itself was NOT printed, so this row reverts to OPEN if the
merger requires the printed layout binding viewModel.info.dirName.
For the two OPEN rows (16, 28): `confirmed_by` INFERRED in the table means, following
the batch 1-2 merge-ready convention, "at best inferred, no positive route printed" —
it is NOT evidence for a label, and the rows stay OPEN.
Lambda $ numbering for DetailTorrentInfoFragment matches lexical source order
(onCreateView click lambdas $0/$1, chooseDir callback $2, selectTag callback $3);
numbering is source-order, NOT bytecode-verified.

## Shared trunk (proposed, strict-entry caveat below)

DetailTorrentFragment.onViewCreated (local copy, NOT freshly fetched here):
provider.get(DetailTorrentViewModel.class) :163, provider.get(MsgDetailTorrentViewModel.class) :168,
DetailPagerAdapter created :185. DetailPagerAdapter.createFragment returns
DetailTorrentInfoFragment.newInstance() at INFO_FRAG_POS (:59-60, prior fresh copy).
DetailTorrentInfoFragment.onCreateView :99-115 inflates the binding, obtains the shared
DetailTorrentViewModel, and calls binding.setViewModel(viewModel) :105. The launcher →
DetailTorrentActivity → DetailTorrentFragment step was NOT printed in this pass, so
under a strict entry-route rule all 40 rows below revert to OPEN. They are judged
REACHABLE (proposed) on the fragment-anchored trunk, as in prior detail batches.
This strict-entry convention is UNDECIDED for the project — it is recorded per row,
not decided here.

## Counts — proposed, not verified (mechanically verified: 40 rows, sequence 1-40 intact)

- REACHABLE proposed: 38 / 40 (29 SOURCE / 9 INFERRED)
- UNREACHABLE proposed: 0
- OPEN: 2 (rows 16 and 28, both toString rows — see below)
- Verified for merge: 0

## Rows (plan order)

| # | Method | Label | confirmed_by | Printed route / citation |
|---|---|---|---|---|
| 1 | MsgDetailTorrentViewModel.fragmentInActionMode | REACHABLE proposed | SOURCE | Called directly by DetailTorrentTrackersFragment :308 (true) and :333 (false), and by DetailTorrentFilesFragment :388 (true) and :411 (false) in local copies. Definition MsgDetailTorrentViewModel.java:31-34. |
| 2 | MsgDetailTorrentViewModel.observeFragmentInActionMode | REACHABLE proposed | SOURCE | Called directly by DetailTorrentFragment.subscribeMsgViewModel :280 (local copy). Definition MsgDetailTorrentViewModel.java:36-39. |
| 3 | TorrentDetailsInfo.<init> | REACHABLE proposed | SOURCE | Constructed with `new TorrentDetailsInfo()` in DetailTorrentViewModel field initialiser :91 and in clearData() :134 (fresh DVM text). Implicit default constructor. |
| 4 | TorrentDetailsInfo.getAdvancedInfo | REACHABLE proposed | SOURCE | Called directly by DetailTorrentViewModel infoCallback :471 (fresh DVM text). Definition TorrentDetailsInfo.java:66-69. |
| 5 | TorrentDetailsInfo.getDirName | REACHABLE proposed | INFERRED | @Bindable getter, TorrentDetailsInfo.java:78-81. No printed Java caller; reached only via generated data binding for the detail-info layout, whose fragment inflates and sets the viewModel (DetailTorrentInfoFragment :99-105). Layout XML NOT printed — reverts to OPEN if merger requires it. |
| 6 | TorrentDetailsInfo.getMetaInfo | REACHABLE proposed | SOURCE | Called directly by DetailTorrentViewModel.makeFileTree :536 (fresh DVM text). Definition TorrentDetailsInfo.java:102-105. |
| 7 | TorrentDetailsInfo.getStorageFreeSpace | REACHABLE proposed | SOURCE | Called directly by DetailTorrentViewModel.checkFreeSpace :426 (fresh DVM text). Definition TorrentDetailsInfo.java:90-93. |
| 8 | TorrentDetailsInfo.getTorrent | REACHABLE proposed | SOURCE | Called directly by DetailTorrentFragment :431-432 (local copy) and by DetailTorrentViewModel :207, :270, :432, :479, :542 (fresh DVM text). Definition TorrentDetailsInfo.java:42-45. |
| 9 | TorrentDetailsInfo.getTorrentInfo | REACHABLE proposed | SOURCE | Called directly by DetailTorrentFragment :431-432 (local copy) and by DetailTorrentViewModel :480, :543 (fresh DVM text). Definition TorrentDetailsInfo.java:54-57. |
| 10 | TorrentDetailsInfo.setAdvancedInfo | REACHABLE proposed | SOURCE | Called directly by DetailTorrentViewModel.updateInfo(AdvancedTorrentInfo) :219 (fresh DVM text). Definition TorrentDetailsInfo.java:71-74. |
| 11 | TorrentDetailsInfo.setDirName | REACHABLE proposed | SOURCE | Called directly by DetailTorrentViewModel mutableParamsCallback :454 (fresh DVM text). Definition TorrentDetailsInfo.java:83-86. |
| 12 | TorrentDetailsInfo.setMetaInfo | REACHABLE proposed | SOURCE | Called directly by DetailTorrentViewModel.updateInfo(TorrentMetaInfo) :200 (fresh DVM text). Definition TorrentDetailsInfo.java:107-110. |
| 13 | TorrentDetailsInfo.setStorageFreeSpace | REACHABLE proposed | SOURCE | Called directly by DetailTorrentViewModel mutableParamsCallback :453 (inside the fromRunnable, fresh DVM text). Definition TorrentDetailsInfo.java:95-98. |
| 14 | TorrentDetailsInfo.setTorrent | REACHABLE proposed | SOURCE | Called directly by DetailTorrentViewModel.updateInfo(Torrent,TorrentInfo) :208 (fresh DVM text). Definition TorrentDetailsInfo.java:47-50. |
| 15 | TorrentDetailsInfo.setTorrentInfo | REACHABLE proposed | SOURCE | Called directly by DetailTorrentViewModel.updateInfo(Torrent,TorrentInfo) :209 (fresh DVM text). Definition TorrentDetailsInfo.java:59-62. |
| 16 | TorrentDetailsInfo.toString | OPEN | INFERRED | Definition TorrentDetailsInfo.java:115-125. No printed caller in any file printed in this session or the prior session. NOT UNREACHABLE: toString is a common logging/concat route; needs a saved full-repo grep before any flip. Highest-priority grep target for this batch. |
| 17 | TorrentDetailsMutableParams.<init> | REACHABLE proposed | SOURCE | Constructed with `new TorrentDetailsMutableParams()` in DetailTorrentViewModel field initialiser :92 and in clearData() :137 (fresh DVM text). Implicit default constructor. |
| 18 | TorrentDetailsMutableParams.getDirPath | REACHABLE proposed | SOURCE | Called directly by DetailTorrentViewModel mutableParamsCallback :447 and checkParamsChanged :492 (fresh DVM text). Definition TorrentDetailsMutableParams.java:62-65. |
| 19 | TorrentDetailsMutableParams.getName | REACHABLE proposed | SOURCE | Called directly by DetailTorrentViewModel checkParamsChanged :486 (fresh DVM text), by DetailTorrentInfoFragment.initEditNameDialog :305, and by DetailTorrentFragment :541 (local copy). Definition TorrentDetailsMutableParams.java:38-41. |
| 20 | TorrentDetailsMutableParams.isFirstLastPiecePriority | REACHABLE proposed | SOURCE | Called directly by DetailTorrentViewModel checkParamsChanged :513 (fresh DVM text). Definition TorrentDetailsMutableParams.java:86-89. |
| 21 | TorrentDetailsMutableParams.isPrioritiesChanged | REACHABLE proposed | SOURCE | Called directly by DetailTorrentViewModel checkParamsChanged :504 (fresh DVM text). Definition TorrentDetailsMutableParams.java:74-77. |
| 22 | TorrentDetailsMutableParams.isSequentialDownload | REACHABLE proposed | SOURCE | Called directly by DetailTorrentViewModel checkParamsChanged :498 (fresh DVM text). Definition TorrentDetailsMutableParams.java:50-53. |
| 23 | TorrentDetailsMutableParams.setDirPath | REACHABLE proposed | SOURCE | Called directly by DetailTorrentViewModel initMutableParams :438 (fresh DVM text) and by DetailTorrentInfoFragment chooseDir ActivityResult callback :129. Definition TorrentDetailsMutableParams.java:67-70. |
| 24 | TorrentDetailsMutableParams.setFirstLastPiecePriority | REACHABLE proposed | SOURCE | Called directly by DetailTorrentViewModel initMutableParams :440 (fresh DVM text). Definition TorrentDetailsMutableParams.java:91-94. |
| 25 | TorrentDetailsMutableParams.setName | REACHABLE proposed | SOURCE | Called directly by DetailTorrentViewModel initMutableParams :437 (fresh DVM text) and by DetailTorrentInfoFragment subscribeAlertDialog :227. Definition TorrentDetailsMutableParams.java:43-46. |
| 26 | TorrentDetailsMutableParams.setPrioritiesChanged | REACHABLE proposed | SOURCE | Called directly in the applyPriority subscribe lambda, DetailTorrentViewModel :334 (fresh DVM text). Definition TorrentDetailsMutableParams.java:79-82. |
| 27 | TorrentDetailsMutableParams.setSequentialDownload | REACHABLE proposed | SOURCE | Called directly by DetailTorrentViewModel initMutableParams :439 (fresh DVM text). Definition TorrentDetailsMutableParams.java:55-58. |
| 28 | TorrentDetailsMutableParams.toString | OPEN | INFERRED | Definition TorrentDetailsMutableParams.java:99-109. No printed caller in any file printed in this session or the prior session. NOT UNREACHABLE for the same reason as row 16; needs a saved full-repo grep. Highest-priority grep target for this batch, jointly with row 16. |
| 29 | DetailTorrentInfoFragment.<clinit> | REACHABLE proposed | INFERRED | Class initialisation on first use (static TAG and dialog-tag constants); fragment first constructed by newInstance, called from DetailPagerAdapter :59-60 (prior fresh copy). JVM class-init dispatch INFERRED. |
| 30 | DetailTorrentInfoFragment.<init> | REACHABLE proposed | SOURCE | Constructed with `new DetailTorrentInfoFragment()` in newInstance, DetailTorrentInfoFragment.java:81-88, called by DetailPagerAdapter.createFragment :59-60 (prior fresh copy). Implicit default constructor. |
| 31 | DetailTorrentInfoFragment.checkNameField | REACHABLE proposed | SOURCE | Called directly in subscribeAlertDialog :226 and in the TextWatcher afterTextChanged in initEditNameDialog :320. Definition :259-272. |
| 32 | DetailTorrentInfoFragment.initEditNameDialog | REACHABLE proposed | SOURCE | Called directly in subscribeAlertDialog DIALOG_SHOWN branch :218. Definition :294-323. |
| 33 | DetailTorrentInfoFragment.lambda$new$2 | REACHABLE proposed | INFERRED | chooseDir ActivityResult callback, field :117-131 (RESULT_OK check, setDirPath call, error dialog). Invoked only by ActivityResult dispatch, not printed from androidx. |
| 34 | DetailTorrentInfoFragment.lambda$new$3 | REACHABLE proposed | INFERRED | selectTag ActivityResult callback, field :132-145 (reads selected TagInfo, subscribes viewModel.addTag). ActivityResult dispatch INFERRED. |
| 35 | DetailTorrentInfoFragment.lambda$onCreateView$0 | REACHABLE proposed | INFERRED | folderChooserButton click lambda, onCreateView :110 (`showChooseDirDialog()`). View click dispatch INFERRED. |
| 36 | DetailTorrentInfoFragment.lambda$onCreateView$1 | REACHABLE proposed | INFERRED | editNameButton click lambda, onCreateView :111 (`showEditNameDialog()`). View click dispatch INFERRED. |
| 37 | DetailTorrentInfoFragment.lambda$subscribeAlertDialog$4 | REACHABLE proposed | INFERRED | Dialog-event lambda in subscribeAlertDialog, :211-242 (DIALOG_SHOWN / POSITIVE / NEGATIVE branches). Invoked only via Rx subscription to dialogViewModel.observeEvents. |
| 38 | DetailTorrentInfoFragment.newInstance | REACHABLE proposed | SOURCE | Called directly by DetailPagerAdapter.createFragment at INFO_FRAG_POS (prior fresh copy). Definition DetailTorrentInfoFragment.java:81-88. |
| 39 | DetailTorrentInfoFragment.onAttach | REACHABLE proposed | INFERRED | Definition :91-97 (stores activity). Invoked only by framework fragment lifecycle dispatch. |
| 40 | DetailTorrentInfoFragment.onCreateView | REACHABLE proposed | INFERRED | Definition :99-115 (inflate, provider.get, setViewModel :105, click listeners, tags listener). Invoked only by framework fragment lifecycle dispatch. |

## Still owed before merge

- Saved full-repo grep for the two OPEN toString rows (rows 16, 28) before any UNREACHABLE flip.
- Printed fragment_detail_torrent_info.xml to confirm row 5's binding basis (getDirName).
- Printed launcher → DetailTorrentActivity → DetailTorrentFragment step (strict-entry caveat).
- Fresh re-verification of local-copy line numbers (DetailTorrentFragment, Trackers/Files
  fragments, DetailPagerAdapter) against a fresh fetch, and of the four b89-90-src files
  whose local hash-object values differ from the prior connector SHAs.
- Bytecode confirmation of lambda $ numbering.
- Main-agent spot-check (1 in 5), py_compile, build, Mac build/C1 — all not run.
- Build, sampler, C1 on a full checkout (git clone still unavailable in this VM for the
  private repo — named missing check, not passed).
