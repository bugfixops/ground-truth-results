# LibreTorrent batch 103 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 103 only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. The prior Agent 41 proposal
  (`~/workspace/libretorrent-batch103-proposal.md`) was used as an INPUT / lead list only;
  every row below was re-checked against source freshly printed in this pass (see
  "Freshly printed source" below). No verdict was copied as a result without that check.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 103 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/agent27-plan.tsv` (4,733 lines incl. header; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy), all
`TODO_CANDIDATE_REACHABLE` (candidates, not evidence), in plan order:
FileManagerDialog rows 1-15, FileManagerDialog$1 rows 16-19, $2 rows 20-22, $3 rows 23-24,
$MediaReceiver rows 25-26, FileManagerNode rows 27-37, FileManagerSpinnerAdapter rows 38-40.

## Counts — mechanically verified from the table below

- **40 rows, sequence 1-40 intact, in plan order.**
- **REACHABLE proposed: 35 / 40 (SOURCE 26, INFERRED 9)**
- **UNREACHABLE proposed: 0**
- **OPEN: 5 / 40** (rows 34, 35, 36, 37, 40)
- **Verified for merge: 0.** Verification still requires the main agent's 1-in-5 spot-check,
  `py_compile` + build on a full checkout, and the Mac build/C1 return — all **not run** here.

## Freshly printed source used in this pass

All files freshly connector-fetched from branch `work-2026-10-31` in this pass, one file
at a time with ~20 s pauses, saved in `~/workspace/b103104-src/`, all under
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`:
- `ui/filemanager/FileManagerNode.java` — 117 lines. Definitions verified: `<init>` :39-44,
  `getName` :47-50, `setName` :53-56, `getType` :59-62, `setType` :65-68, `isEnabled` :70-73,
  `setEnabled` :75-78, `isDirectory` :80-83, `compareTo` :86-89, `equals` :92-105,
  `toString` :109-116. (Prior proposal said 118 lines; the fresh fetch is 117 lines and
  every citation below was re-checked by grep against the fresh copy, so the 1-line
  difference does not move any cited line.)
- `ui/filemanager/FileManagerSpinnerAdapter.java` — 186 lines (prior proposal said 187;
  citations re-checked by grep). Definitions: `StorageSpinnerItem.<init>` :57-62,
  `<init>` :95-98, `clear` :100-103, `addItem` :105-108, `addItems` :110-113,
  `getCount` :116-119, `getItem` :122-125, `getItemId` :128-131, `getDropDownView` :134-154,
  `getView` :157-169, `getStorageItem` :172-175, `getTitle` :177-180, `setTitle` :182-186.
  `TAG` at :42, so `<clinit>` timing is the unprinted JVM rule (INFERRED).
- `ui/filemanager/FileManagerViewModel.java` — 392 lines (prior proposal said 393;
  citations re-checked by grep). `getChildItems` :113-145 constructs `FileManagerNode`
  at :127 (parent dir), :134 (directory), :136-137 (file); no `setEnabled`/`setName`/
  `setType`/`toString` call on a `FileManagerNode` and no `addItem` call anywhere in it.
- `ui/filemanager/FileManagerDialog.java` — 691 lines (prior proposal said 692;
  citations re-checked by grep). Key call sites all confirmed fresh: factory
  :135-140, `new FileManagerSpinnerAdapter` :208, `setTitle` :209, `addItems` :210,
  adapter set :211, `$2` listener :214-238, `registerMediaReceiver` call :240,
  `showInputNameDialog` call :172, `subscribeAlertDialog` :276, `subscribeAdapter` :277,
  `$3` callback field :311-317, `onOptionsItemSelected` :499-516, `goToDirectoryDialog`
  :548-555, `reloadSpinner` :636-650, `addItems` again :645, `MediaReceiver` field :111,
  `onReceive` -> `reloadSpinner` :687-690. No `setEnabled`/`setName`/`setType` call on a
  `FileManagerNode` and no `addItem` call anywhere in it; the `toString()` calls in it
  (:329 `nameField.getText().toString()`, :354 `e.toString()`, :575 `editable.toString()`)
  are on other objects, not on a `FileManagerNode`.
- `ui/filemanager/FileManagerAdapter.java` — 175 lines (prior proposal said 176;
  citations re-checked by grep). Comparator :57-61 (`compareTo` :58, `isDirectory` :59),
  `submitList` sort :88-94 (sort at :91), diffCallback :96-111 (`equals` at :102 and :109),
  `bind` :126-... (`setEnabled(item.isEnabled())` :135, `isEnabled` branch :137,
  `getName` :138/:154/:157, `isDirectory` :156). It only *reads* `isEnabled`; it never
  calls `setEnabled`, `setName`, `setType`, or a `FileManagerNode.toString()`.
- `ui/filemanager/FileManagerViewModelFactory.java` and `ui/filemanager/GoToFolderDialog.java`
  were also freshly fetched in this pass (52 and 166 lines); their rows are batch 104
  (see `batch104-merge-ready.md`), and they contain no `FileManagerNode` setter or
  `addItem` call either.

No fresh HTTP 429 was hit in this pass. No connector `search_code` result was used as
evidence of absence. No saved full-repo grep was run (no full local checkout — git clone
fails in this VM with no credential device, named missing check, not passed).

## Shared routes (printed steps, cited once here and reused by row)

Shorthand: FD = FileManagerDialog.java, FN = FileManagerNode.java,
VM = FileManagerViewModel.java, AD = FileManagerAdapter.java, SA = FileManagerSpinnerAdapter.java.

**R1 — FileManagerDialog activity, dialog-anchored (NOT launcher-anchored).**
Who starts FileManagerDialog (startActivity site / manifest entry) was NOT printed in this
session, so every route below is anchored at FileManagerDialog's own lifecycle/menu/click
handlers, not at the launcher. Inside the dialog, all steps are printed app code:
`FD:120 onCreate` -> factory `FD:135-140` -> `FD:199` swipe listener, `FD:201` storage list,
`FD:208-214` spinner adapter + selection listener, `FD:240 registerMediaReceiver`;
`FD:273-279 onStart` -> subscribeAlertDialog / subscribeAdapter / curDir callback registration;
`FD:499-516 onOptionsItemSelected` (menu dispatch itself is framework, the calls inside are
printed app code); `FD:430-457 onItemClicked` (adapter click callback, calls inside printed).

**R2 — Node list flow.**
`FD:302-309 subscribeAdapter` subscribes `viewModel.childNodes` to `adapter::submitList`
-> `VM:96-99 refreshCurDirectory` / `VM:101-107 updateCurDir` -> `VM:113-145 getChildItems`
-> `AD:88-94 submitList` sorts with `AD:57-61 directoryFirstCmp` and ListAdapter/DiffUtil
-> `AD:96-111 diffCallback`, `AD:126-157 ViewHolder.bind`. The Rx/ListAdapter dispatch steps
are library code, not printed; the calls inside the printed callback bodies are SOURCE.

**R3 — Anonymous-class mapping (by signature, not order alone).**
$1 = the TextWatcher created at FD:176 (methods before/on/afterTextChanged match the plan
signatures exactly, fresh-verified at FD:176-190); $2 = the AdapterView.OnItemSelectedListener
created at FD:214 (onItemSelected/onNothingSelected, fresh-verified at FD:214-238);
$3 = the Observable.OnPropertyChangedCallback created at FD:311-317 (onPropertyChanged,
fresh-verified). Lambda bodies do not create $ classes, so no lambda interferes with this
numbering, but bytecode was not checked — merger must confirm $ indices.

**confirmed_by convention used here (recorded, not decided as a project convention):**
SOURCE = a direct app-to-app call site naming the method is printed in app source
(including a printed listener body that calls it); INFERRED = the method is reached only
through unprinted framework/library dispatch (DialogFragment/activity lifecycle, view-click
dispatch, Rx/ViewModelProvider dispatch, JVM class initialisation, Spinner/BaseAdapter
dispatch) where the registration or show site is printed. This is the per-row convention,
not the whole-route convention used in some earlier batches; labels are unaffected, only
`confirmed_by` would change at merge if the merger adopts the whole-route convention.

## Per-method table (all 40 rows, in plan order)

| # | Method (plan) | Proposed label | confirmed_by | Route / printed citations |
|---|---|---|---|---|
| 1 | FileManagerDialog.openHomeDirectory | REACHABLE proposed | SOURCE | R1: FD:503-504 onOptionsItemSelected home menu -> openHomeDirectory() :518-522 -> goToDirectory(path). |
| 2 | FileManagerDialog.permissionDeniedToast | REACHABLE proposed | SOURCE | R1: called FD:231 ($2 catch), :338 (handleAlertDialogEvent), :436/:446 (onItemClicked), :530 (goToDirectory), :563 (returnDirectoryUri), :586 (createFile), :598 (returnFileUri). Definition FD:382-387. |
| 3 | FileManagerDialog.refreshDir | REACHABLE proposed | INFERRED | R1: registered as the swipe-refresh listener at FD:199 (`setOnRefreshListener(this::refreshDir)`); definition FD:459-462 -> viewModel.refreshCurDirectory(). The SwipeRefreshLayout dispatch into it is framework, not printed, hence INFERRED. |
| 4 | FileManagerDialog.registerMediaReceiver | REACHABLE proposed | SOURCE | R1: FD:240 onCreate -> registerMediaReceiver() :281-287 (filter MEDIA_MOUNTED/UNMOUNTED, file scheme, registerReceiver). |
| 5 | FileManagerDialog.reloadSpinner | REACHABLE proposed | SOURCE | Called explicitly from MediaReceiver.onReceive, FD:689 (`dialog.get().reloadSpinner()`); definition FD:636-650 (clear/addItems/setTitle/refreshCurDirectory). |
| 6 | FileManagerDialog.returnDirectoryUri | REACHABLE proposed | SOURCE | R1: FD:505-510 onOptionsItemSelected ok menu (non-SAVE mode) -> returnDirectoryUri() :557-568 (getCurDirectoryUri, setResult, finish). |
| 7 | FileManagerDialog.returnFileUri | REACHABLE proposed | SOURCE | R1: FD:452-455 onItemClicked FILE + FILE_CHOOSER_MODE -> saveCurDirectoryPath + returnFileUri(name) :593-604 (getFileUri, setResult, finish). |
| 8 | FileManagerDialog.saveCurDirectoryPath | REACHABLE proposed | SOURCE | R1: FD:454 (onItemClicked), :506 (onOptionsItemSelected); definition FD:464-472 (pref last-dir write). |
| 9 | FileManagerDialog.showCreateFolderErrDialog | REACHABLE proposed | SOURCE | R1: FD:331-332 handleAlertDialogEvent (createDirectory false) -> showCreateFolderErrDialog() :389-402. |
| 10 | FileManagerDialog.showInputNameDialog | REACHABLE proposed | SOURCE | R1: FD:172 addFab click lambda body -> showInputNameDialog() :243-256. |
| 11 | FileManagerDialog.showReplaceFileDialog | REACHABLE proposed | SOURCE | FD:577 Dialog.createFile (file exists, not replace) -> showReplaceFileDialog() :606-619. |
| 12 | FileManagerDialog.showSendErrorDialog | REACHABLE proposed | SOURCE | FD:341 (handleAlertDialogEvent IOException), :449 (onItemClicked IOException); definition FD:370-380. |
| 13 | FileManagerDialog.subscribeAdapter | REACHABLE proposed | SOURCE | R1: FD:277 onStart -> subscribeAdapter() :302-309 (childNodes -> adapter::submitList). |
| 14 | FileManagerDialog.subscribeAlertDialog | REACHABLE proposed | SOURCE | R1: FD:276 onStart -> subscribeAlertDialog() :297-300 (dialogViewModel events -> handleAlertDialogEvent). |
| 15 | FileManagerDialog.unregisterMediaReceiver | REACHABLE proposed | SOURCE | R1: FD:262 onDestroy -> unregisterMediaReceiver() :289-295 (try unregisterReceiver, ignore IllegalArgumentException). |
| 16 | FileManagerDialog$1.<init> | REACHABLE proposed | SOURCE | R3: the anonymous TextWatcher is instantiated by the printed expression at FD:176 (`binding.fileName.addTextChangedListener(new TextWatcher() {...})`). |
| 17 | FileManagerDialog$1.afterTextChanged | REACHABLE proposed | INFERRED | R3: registered at FD:176; definition FD:186-189 (clears layoutFileName error). TextWatcher dispatch is framework, not printed, hence INFERRED. |
| 18 | FileManagerDialog$1.beforeTextChanged | REACHABLE proposed | INFERRED | R3: registered at FD:176; definition FD:178-179 (empty body). Framework dispatch, hence INFERRED; an empty body does not make it unreachable — the callback slot is registered. |
| 19 | FileManagerDialog$1.onTextChanged | REACHABLE proposed | INFERRED | R3: registered at FD:176; definition FD:182-183 (empty body). Same reasoning as row 18. |
| 20 | FileManagerDialog$2.<init> | REACHABLE proposed | SOURCE | R3: the anonymous OnItemSelectedListener is instantiated by the printed expression at FD:214 (`setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {...})`). |
| 21 | FileManagerDialog$2.onItemSelected | REACHABLE proposed | INFERRED | R3: registered at FD:214; definition FD:216-233 (getItem, isDirectoryExists, jumpToDirectory, permissionDeniedToast on SecurityException). Spinner framework dispatch, hence INFERRED. |
| 22 | FileManagerDialog$2.onNothingSelected | REACHABLE proposed | INFERRED | R3: registered at FD:214; definition FD:236-237 (empty body). Framework dispatch, hence INFERRED; same empty-body reasoning as row 18. |
| 23 | FileManagerDialog$3.<init> | REACHABLE proposed | SOURCE | R3: the anonymous OnPropertyChangedCallback is instantiated by the printed field initialiser at FD:311-317. |
| 24 | FileManagerDialog$3.onPropertyChanged | REACHABLE proposed | INFERRED | R3: registered at FD:278 (`curDir.addOnPropertyChangedCallback(currentDirCallback)`); definition FD:314-316 (storageAdapter.setTitle). Observable dispatch is library code, not printed, hence INFERRED. |
| 25 | FileManagerDialog$MediaReceiver.<init> | REACHABLE proposed | SOURCE | Field initialiser FD:111 (`new MediaReceiver(this)`); definition FD:682-684. |
| 26 | FileManagerDialog$MediaReceiver.onReceive | REACHABLE proposed | INFERRED | Registered at FD:286 (`registerReceiver(mediaReceiver, filter)`, filter FD:282-285 MEDIA_MOUNTED/UNMOUNTED + file scheme); definition FD:687-690 -> reloadSpinner(). System broadcast dispatch, hence INFERRED. |
| 27 | FileManagerNode.<init> | REACHABLE proposed | SOURCE | R2: VM:127 (parent dir), :134 (directory), :136-137 (file) in getChildItems. Definition FN:39-44. |
| 28 | FileManagerNode.compareTo | REACHABLE proposed | SOURCE | R2: AD:57-61 comparator lambda `n1.compareTo(n2)`, used by AD:91 `list.sort(directoryFirstCmp)` in submitList. Definition FN:86-89 (itself calls another.getName()). |
| 29 | FileManagerNode.equals | REACHABLE proposed | SOURCE | R2: AD:102 and :109 diffCallback areContentsTheSame/areItemsTheSame both call `oldItem.equals(newItem)`. Definition FN:92-105. |
| 30 | FileManagerNode.getName | REACHABLE proposed | SOURCE | FD:431 (PARENT_DIR check), AD:138 (extension check), AD:154/:157 (bind). Definition FN:47-50. |
| 31 | FileManagerNode.getType | REACHABLE proposed | SOURCE | FD:441 (DIR check), :452 (FILE check) in onItemClicked. Definition FN:59-62. |
| 32 | FileManagerNode.isDirectory | REACHABLE proposed | SOURCE | AD:59 (comparator directory-first) and AD:156 (bind icon branch). Definition FN:80-83. |
| 33 | FileManagerNode.isEnabled | REACHABLE proposed | SOURCE | AD:135 (`itemView.setEnabled(item.isEnabled())`) and AD:137 (enabled branch) in bind. Definition FN:70-73. |
| 34 | FileManagerNode.setEnabled | OPEN | — | Definition FN:75-78. Fresh grep across all 7 files printed in this pass (FD, VM, AD, FN, SA, FAC, GD) found NO call to `setEnabled` on a `FileManagerNode` (AD only reads `isEnabled`). Resolves with: a printed setEnabled call site, or a saved full-repo grep. NOT flipped to UNREACHABLE on this printed subset. |
| 35 | FileManagerNode.setName | OPEN | — | Definition FN:53-56. Fresh grep across all 7 files printed in this pass found NO `setName` call on a `FileManagerNode`. Resolves with: a printed setName call site, or a saved full-repo grep. NOT flipped to UNREACHABLE on this printed subset. |
| 36 | FileManagerNode.setType | OPEN | — | Definition FN:65-68. Fresh grep across all 7 files printed in this pass found NO `setType` call on a `FileManagerNode`. Resolves with: a printed setType call site, or a saved full-repo grep. NOT flipped to UNREACHABLE on this printed subset. |
| 37 | FileManagerNode.toString | OPEN | — | Definition FN:109-116. Fresh grep across all 7 files printed in this pass found NO `toString()` call on a `FileManagerNode` (the `toString()` calls in FD are on `Editable`/`Exception` objects, not on a node). Resolves with: a printed caller, or a saved full-repo grep. NOT flipped to UNREACHABLE on this printed subset. Note: `setName`/`setType` are also `FileNode` interface methods, but no interface-dispatch caller was printed either; that is a lead for the grep, not a route. |
| 38 | FileManagerSpinnerAdapter.<clinit> | REACHABLE proposed | INFERRED | First printed use is FD:208 (`new FileManagerSpinnerAdapter(this)`); static TAG at SA:42. Class-init timing is the unprinted JVM rule, hence INFERRED. |
| 39 | FileManagerSpinnerAdapter.<init> | REACHABLE proposed | SOURCE | FD:208 in onCreate. Definition SA:95-98. |
| 40 | FileManagerSpinnerAdapter.addItem | OPEN | — | Definition SA:105-108. Fresh grep across all 7 files printed in this pass found NO `addItem(...)` call: FD uses `addItems` at FD:210 and FD:645, never `addItem` (singular); VM returns a list via `getStorageList`, it does not call the adapter. Resolves with: a printed `addItem(...)` call site (distinct from `addItems`), or a saved full-repo grep. NOT flipped to UNREACHABLE on this printed subset. |

## OPEN rows and what would resolve them (5 rows)

- setEnabled / setName / setType / toString (rows 34-37): a printed caller in any file, or a saved full-repo grep over the source tree (not run — no full local checkout).
- addItem (row 40): a printed `addItem(...)` call site (distinct from addItems), or a saved full-repo grep.

## Caveats restated

1. Strict-entry caveat: no launcher -> FileManagerDialog step was printed. Under a strict
   entry-route rule, the 35 REACHABLE rows revert to OPEN. The routes above are dialog-anchored.
   (This is the undecided strict-entry convention, recorded here, not decided.)
2. Anonymous $ numbering (R3) is by signature match, not bytecode-confirmed; merger must confirm.
3. No row is verified for merge: no build, sampler, full-repo grep, or C1 check was run.
   A merge step must re-derive every row from a full checkout and close the 5 OPEN rows.
4. FileManagerViewModel, FileManagerViewModelFactory, and GoToFolderDialog rows are NOT in
   batch 103 and are judged only in batch 104; their citations here are route context only.
5. Line-count drift vs the prior proposal (FD 691 vs 692, VM 392 vs 393, AD 175 vs 176,
   SA 186 vs 187, FN 117 vs 118) does not move any cited line: every citation above was
   re-checked by grep against the fresh copies in this pass.
