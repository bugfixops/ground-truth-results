# LibreTorrent batch 104 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 104 only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, re-derived from printed source. The prior Agent 41 proposal
  (`~/workspace/libretorrent-batch104-proposal.md`) was used as an INPUT / lead list only;
  every row below was re-checked against source freshly printed in this pass (see
  "Freshly printed source" below). No verdict was copied as a result without that check.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 104 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/agent27-plan.tsv` (4,733 lines incl. header; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy), all
`TODO_CANDIDATE_REACHABLE` (candidates, not evidence), in plan order:
FileManagerSpinnerAdapter rows 1-10, $StorageSpinnerItem rows 11-12,
FileManagerViewModel rows 13-34, FileManagerViewModelFactory rows 35-36,
GoToFolderDialog rows 37-40.

## Counts — mechanically verified from the table below

- **40 rows, sequence 1-40 intact, in plan order.**
- **REACHABLE proposed: 40 / 40 (SOURCE 32, INFERRED 8)**
- **UNREACHABLE proposed: 0**
- **OPEN: 0 / 40**
- **Verified for merge: 0.** Verification still requires the main agent's 1-in-5 spot-check,
  `py_compile` + build on a full checkout, and the Mac build/C1 return — all **not run** here.

## Freshly printed source used in this pass

All files freshly connector-fetched from branch `work-2026-10-31` in this pass, one file
at a time with ~20 s pauses, saved in `~/workspace/b103104-src/`, all under
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`:
- `ui/filemanager/FileManagerSpinnerAdapter.java` — 186 lines. Definitions verified by grep:
  `clear` :100-103, `addItem` :105-108, `addItems` :110-113, `getCount` :116-119,
  `getItem` :122-125 (delegates to `getStoragePath`), `getItemId` :128-131,
  `getDropDownView` :134-154 (calls `getStorageItem` :146, `getStoragePath` via item at :150),
  `getView` :157-169 (calls `getTitle` :166), `getStorageItem` :172-175, `getTitle` :177-180,
  `setTitle` :182-186, `StorageSpinnerItem.<init>` :57-62, `getStoragePath` :75-77.
- `ui/filemanager/FileManagerViewModel.java` — 392 lines. Definitions/callers verified by grep:
  `<init>` :61-94 (calls `checkPermissions` :80, `updateCurDir` :89), `refreshCurDirectory`
  :96-99, `updateCurDir` :101-107, `getChildItems` :113-145, `filterDirectories` :147-161,
  `createDirectory` :163-171, `openDirectory` :173-184, `jumpToDirectory` :186-195,
  `isDirectoryExists` :197-200, `upToParentDirectory` :206-217, `fileExists` :219-227,
  `appendExtension` :229-246, `createFile` :248-270, `getCurDirectoryUri` :272-283,
  `getFileUri` :285-296, `getExtSdCardPaths` :298-318, `getBaseSdCardPath` :320-327,
  `getSdCardDataPath` :329-336, `tryGetCanonicalPath` :338-345, `checkPermissions` :347-358,
  `getStorageList` :360-392 (constructs `StorageSpinnerItem` at :367 and :380).
  `TAG` at :51, so `<clinit>` timing is the unprinted JVM rule (INFERRED).
- `ui/filemanager/FileManagerDialog.java` — 691 lines. Dialog-side callers verified by grep:
  factory construction :135-140, `ViewModelProvider.get` :140, `getStorageList` :201 and :640,
  `setTitle` :209/:315/:646, `addItems` :210/:645, `clear` :644, `getItem` :223,
  `isDirectoryExists` :224, `jumpToDirectory` :225/:227/:527, `createDirectory` :331,
  `openDirectory` :335/:443, `upToParentDirectory` :433, `refreshCurDirectory` :461/:649,
  `getCurDirectoryUri` :560, `fileExists` :576, `createFile` :583, `getFileUri` :596,
  `getSpinnerPos` :652-661 (calls `getStoragePath` at :655), `goToDirectoryDialog` :548-555
  (calls `GoToFolderDialog.newInstance()` at :552), `onFragmentFinished` :664-673.
- `ui/filemanager/FileManagerViewModelFactory.java` — 52 lines. `<init>` :34-41,
  `create` :45-51 (constructs `new FileManagerViewModel(...)` at :48).
- `ui/filemanager/GoToFolderDialog.java` — 166 lines. `TAG` at :48, `newInstance` :55-62
  (constructs `new GoToFolderDialog()` at :56), `onCreateDialog` :91-105,
  `initLayoutView` :107-126, `initAlertDialog` :128-145 (positive-button lambda
  `goToDir()` at :139, cancel lambda `finish(..., CANCEL)` at :142-143),
  `goToDir` :147-156 (calls `finish` at :155), `onBackPressed` :158-159 (calls `finish`
  at :159), `finish` :162-165 (dismiss + `FragmentCallback.onFragmentFinished`).
  No explicit constructor declaration appears in the fresh file; `<init>` is the implicit
  default constructor reached via `newInstance` — merger must confirm no explicit ctor
  exists in a version other than the printed file.
- `ui/filemanager/FileManagerNode.java` and `ui/filemanager/FileManagerAdapter.java`
  were also freshly fetched in this pass; their rows are batch 103, and they contain
  no batch-104 row.

No fresh HTTP 429 was hit in this pass. No connector `search_code` result was used as
evidence of absence. No saved full-repo grep was run (no full local checkout — git clone
fails in this VM with no credential device, named missing check, not passed).

## Shared routes (printed steps, cited once here and reused by row)

Shorthand: FD = FileManagerDialog.java, SA = FileManagerSpinnerAdapter.java,
VM = FileManagerViewModel.java, FAC = FileManagerViewModelFactory.java,
GD = GoToFolderDialog.java.

**R1 — FileManagerDialog activity, dialog-anchored (NOT launcher-anchored).**
As in batch 103, who starts FileManagerDialog was NOT printed, so routes are anchored at
FileManagerDialog's own handlers: `FD:120 onCreate` (factory :135-140, spinner :208-214),
`FD:273-279 onStart`, `FD:499-516 onOptionsItemSelected`, `FD:430-457 onItemClicked`,
`FD:636-650 reloadSpinner`, plus the $2 spinner callback at FD:214-238 and the $3
curDir callback at FD:311-317. The ViewModel is obtained through the AndroidX
ViewModelProvider library (FD:140); that dispatch step is INFERRED, the factory and
constructor bodies it reaches are printed.

**R2 — Spinner rendering (framework dispatch).**
FD:211 sets the spinner adapter (`binding.storageSpinner.setAdapter(storageAdapter)`).
Android's Spinner/BaseAdapter framework then calls getCount/getView/getDropDownView/
getItemId; that framework code was not printed, so those four rows are INFERRED, while
calls made inside their printed bodies (getStorageItem, getTitle, getStoragePath) are SOURCE.

**R3 — GoToFolderDialog show flow.**
FD:548-555 goToDirectoryDialog() -> GD:55-62 newInstance() (new GoToFolderDialog + Bundle)
-> `show(fm, ...)` (fragment-manager dispatch, INFERRED for the fragment lifecycle itself)
-> GD:91-105 onCreateDialog -> GD:107-126 initLayoutView -> GD:128-145 initAlertDialog,
whose OnShowListener lambda at GD:137-139 wires the positive button to goToDir().

**confirmed_by convention used here (recorded, not decided as a project convention):**
SOURCE = a direct app-to-app call site naming the method is printed in app source
(including a printed listener body that calls it, and an internal call site printed in the
definition file itself where the calling method is itself SOURCE-anchored); INFERRED = the
method is reached only through unprinted framework/library dispatch (activity/fragment
lifecycle, ActivityResult/Spinner/BaseAdapter dispatch, ViewModelProvider/Rx dispatch, JVM
class initialisation) where the registration or entry is printed. This is the per-row
convention, not the whole-route convention used in some earlier batches; labels are
unaffected, only `confirmed_by` would change at merge if the merger adopts the
whole-route convention.

## Per-method table (all 40 rows, in plan order)

| # | Method (plan) | Proposed label | confirmed_by | Route / printed citations |
|---|---|---|---|---|
| 1 | FileManagerSpinnerAdapter.addItems | REACHABLE proposed | SOURCE | R1: FD:210 (onCreate, spinnerItems) and FD:645 (reloadSpinner). Definition SA:110-113. |
| 2 | FileManagerSpinnerAdapter.clear | REACHABLE proposed | SOURCE | R1: FD:644 (reloadSpinner, before re-adding items). Definition SA:100-103. |
| 3 | FileManagerSpinnerAdapter.getCount | REACHABLE proposed | INFERRED | R2: adapter set at FD:211; Spinner framework calls getCount to size the list. Definition SA:116-119. Framework code not printed, hence INFERRED. |
| 4 | FileManagerSpinnerAdapter.getDropDownView | REACHABLE proposed | INFERRED | R2: adapter set at FD:211; Spinner framework calls it when the dropdown opens. Definition SA:134-154 (itself calls getStorageItem :146 and getStoragePath :150). Hence INFERRED. |
| 5 | FileManagerSpinnerAdapter.getItem | REACHABLE proposed | SOURCE | R1: FD:223 ($2.onItemSelected body: `storageAdapter.getItem(i)`). Definition SA:122-125 (delegates to getStoragePath). |
| 6 | FileManagerSpinnerAdapter.getItemId | REACHABLE proposed | INFERRED | R2: adapter set at FD:211; Spinner framework calls getItemId for the selected position. Definition SA:128-131. Hence INFERRED. |
| 7 | FileManagerSpinnerAdapter.getStorageItem | REACHABLE proposed | SOURCE | Called from getDropDownView at SA:146. Definition SA:172-175 (bounds-checked items.get). |
| 8 | FileManagerSpinnerAdapter.getTitle | REACHABLE proposed | SOURCE | Called from getView at SA:166. Definition SA:177-180. Also set via setTitle (row 10). |
| 9 | FileManagerSpinnerAdapter.getView | REACHABLE proposed | INFERRED | R2: adapter set at FD:211; Spinner framework calls getView to render the closed spinner. Definition SA:157-169 (itself calls getTitle :166). Hence INFERRED. |
| 10 | FileManagerSpinnerAdapter.setTitle | REACHABLE proposed | SOURCE | R1: FD:209 (onCreate), FD:315 ($3.onPropertyChanged body), FD:646 (reloadSpinner). Definition SA:182-186 (sets curPath + notifyDataSetChanged). |
| 11 | FileManagerSpinnerAdapter$StorageSpinnerItem.<init> | REACHABLE proposed | SOURCE | VM:367-371 (internal storage item) and VM:380-384 (external storage items, loop) in getStorageList. Definition SA:57-62. |
| 12 | FileManagerSpinnerAdapter$StorageSpinnerItem.getStoragePath | REACHABLE proposed | SOURCE | SA:124 (getItem), SA:150 (getDropDownView), FD:655 (Dialog.getSpinnerPos). Definition SA:75-77. |
| 13 | FileManagerViewModel.<clinit> | REACHABLE proposed | INFERRED | First printed use is FD:135-140 (factory creation + ViewModelProvider.get); static TAG at VM:51. Class-init timing is the unprinted JVM rule, hence INFERRED. |
| 14 | FileManagerViewModel.<init> | REACHABLE proposed | INFERRED | FAC:47-48 (`new FileManagerViewModel(application, config, startDir)` in create), reached from FD:140 via the ViewModelProvider library, whose dispatch code was not printed — hence INFERRED, not SOURCE. Definition VM:61-94 (itself calls checkPermissions :80 and updateCurDir :89). |
| 15 | FileManagerViewModel.appendExtension | REACHABLE proposed | SOURCE | VM:224 (fileExists) and VM:253 (createFile). Definition VM:229-246 (private). |
| 16 | FileManagerViewModel.checkPermissions | REACHABLE proposed | SOURCE | VM:80 (ctor), :180 (openDirectory), :190 (jumpToDirectory), :213 (upToParentDirectory), :257 (createFile), :279 (getCurDirectoryUri), :292 (getFileUri), :306/:308 (getExtSdCardPaths). Definition VM:347-358 (private). |
| 17 | FileManagerViewModel.createDirectory | REACHABLE proposed | SOURCE | FD:331 (handleAlertDialogEvent, new-folder dialog positive click). Definition VM:163-171. |
| 18 | FileManagerViewModel.createFile | REACHABLE proposed | SOURCE | FD:583 (Dialog.createFile body: `viewModel.createFile(fileName)`). Definition VM:248-270 (itself calls appendExtension :253 and checkPermissions :257). |
| 19 | FileManagerViewModel.fileExists | REACHABLE proposed | SOURCE | FD:576 (Dialog.createFile body). Definition VM:219-227 (itself calls appendExtension :224). |
| 20 | FileManagerViewModel.filterDirectories | REACHABLE proposed | SOURCE | VM:132 (getChildItems loop). Definition VM:147-161 (API-R / FILE_CHOOSER_MODE branch :148-150). |
| 21 | FileManagerViewModel.getBaseSdCardPath | REACHABLE proposed | SOURCE | VM:305 (getExtSdCardPaths). Definition VM:320-327 (itself calls tryGetCanonicalPath :323). |
| 22 | FileManagerViewModel.getChildItems | REACHABLE proposed | SOURCE | VM:98 (refreshCurDirectory) and VM:106 (updateCurDir). Definition VM:113-145 (itself calls filterDirectories :132 and constructs FileManagerNode :127/:134/:136). |
| 23 | FileManagerViewModel.getCurDirectoryUri | REACHABLE proposed | SOURCE | FD:560 (Dialog.returnDirectoryUri body). Definition VM:272-283 (itself calls checkPermissions :279). |
| 24 | FileManagerViewModel.getExtSdCardPaths | REACHABLE proposed | SOURCE | VM:363 (getStorageList). Definition VM:298-318 (itself calls getBaseSdCardPath :305, getSdCardDataPath :307, checkPermissions :306/:308). |
| 25 | FileManagerViewModel.getFileUri | REACHABLE proposed | SOURCE | FD:596 (Dialog.returnFileUri body). Definition VM:285-296 (itself calls checkPermissions :292). |
| 26 | FileManagerViewModel.getSdCardDataPath | REACHABLE proposed | SOURCE | VM:307 (getExtSdCardPaths fallback). Definition VM:329-336 (itself calls tryGetCanonicalPath :332). |
| 27 | FileManagerViewModel.getStorageList | REACHABLE proposed | SOURCE | FD:201 (onCreate) and FD:640 (reloadSpinner). Definition VM:360-392 (itself calls getExtSdCardPaths :363 and constructs StorageSpinnerItem :367/:380). |
| 28 | FileManagerViewModel.isDirectoryExists | REACHABLE proposed | SOURCE | FD:224 ($2.onItemSelected body). Definition VM:197-200. |
| 29 | FileManagerViewModel.jumpToDirectory | REACHABLE proposed | SOURCE | FD:225/:227 ($2.onItemSelected body) and FD:527 (Dialog.goToDirectory body). Definition VM:186-195 (itself calls checkPermissions :190 and updateCurDir :194). |
| 30 | FileManagerViewModel.openDirectory | REACHABLE proposed | SOURCE | FD:335 (handleAlertDialogEvent) and FD:443 (onItemClicked DIR branch). Definition VM:173-184 (itself calls checkPermissions :180 and updateCurDir :183). |
| 31 | FileManagerViewModel.refreshCurDirectory | REACHABLE proposed | SOURCE | FD:461 (Dialog.refreshDir body) and FD:649 (reloadSpinner). Definition VM:96-99 (childNodes.onNext(getChildItems())). |
| 32 | FileManagerViewModel.tryGetCanonicalPath | REACHABLE proposed | SOURCE | VM:323 (getBaseSdCardPath) and VM:332 (getSdCardDataPath). Definition VM:338-345 (private, IOException fallback returns input). |
| 33 | FileManagerViewModel.upToParentDirectory | REACHABLE proposed | SOURCE | FD:433 (onItemClicked PARENT_DIR branch). Definition VM:206-217 (itself calls checkPermissions :213 and updateCurDir :216). |
| 34 | FileManagerViewModel.updateCurDir | REACHABLE proposed | SOURCE | VM:89 (ctor), :183 (openDirectory), :194 (jumpToDirectory), :216 (upToParentDirectory). Definition VM:101-107 (curDir.set + childNodes.onNext(getChildItems())). |
| 35 | FileManagerViewModelFactory.<init> | REACHABLE proposed | SOURCE | FD:135-139 (onCreate: `new FileManagerViewModelFactory(this.getApplication(), intent.getParcelableExtra(TAG_CONFIG), startDir)`). Definition FAC:34-41. |
| 36 | FileManagerViewModelFactory.create | REACHABLE proposed | INFERRED | Reached from FD:140 (`new ViewModelProvider(this, factory).get(FileManagerViewModel.class)`) via the ViewModelProvider library, whose dispatch code was not printed — hence INFERRED. Definition FAC:45-51 (itself constructs the ViewModel at :48). |
| 37 | GoToFolderDialog.<clinit> | REACHABLE proposed | INFERRED | First printed use is FD:552 (goToDirectoryDialog -> GoToFolderDialog.newInstance()); static TAG at GD:48. Class-init timing is the unprinted JVM rule, hence INFERRED. |
| 38 | GoToFolderDialog.<init> | REACHABLE proposed | SOURCE | GD:56 (newInstance body: `new GoToFolderDialog()`), called from FD:552. Default (implicit) constructor; no explicit ctor is printed in the fresh file, which is consistent with newInstance being the only construction site printed. |
| 39 | GoToFolderDialog.finish | REACHABLE proposed | SOURCE | GD:155 (goToDir), GD:159 (onBackPressed), GD:142-143 (cancel-button lambda). Definition GD:162-165 (dismiss + FragmentCallback.onFragmentFinished, which lands in FD:664-673 onFragmentFinished). |
| 40 | GoToFolderDialog.goToDir | REACHABLE proposed | SOURCE | R3: GD:139 (positive-button click lambda body in initAlertDialog: `addButton.setOnClickListener((v) -> goToDir())`). Definition GD:147-156 (putExtra TAG_URI + finish OK). |

## OPEN rows

None. No row is left OPEN, and no UNREACHABLE label is claimed: every row above has a
printed caller, a printed registration + framework/library dispatch, or a printed
construction site, as cited per row.

## Caveats restated

1. Strict-entry caveat: no launcher -> FileManagerDialog step was printed. Under a strict
   entry-route rule, the 40 REACHABLE rows revert to OPEN. The routes above are dialog-anchored.
   (This is the undecided strict-entry convention, recorded here, not decided.)
2. INFERRED rows (3, 4, 6, 9, 13, 14, 36, 37) rest on framework/library dispatch
   (Spinner/BaseAdapter, ViewModelProvider, JVM class-init) whose code was not printed from
   fw_src or the library; the registrations/construction sites that trigger them are printed.
3. GoToFolderDialog.<init> has no explicit constructor in the printed file; it is the
   implicit default constructor reached via newInstance. Merger must confirm no explicit
   ctor exists in a version other than the printed file (fresh fetch, 166 lines).
4. No row is verified for merge: no build, sampler, full-repo grep, or C1 check was run.
   A merge step must re-derive every row from a full checkout.
5. Line-count drift vs the prior proposal (FD 691 vs 692, VM 392 vs 393, AD 175 vs 176,
   SA 186 vs 187, FAC 52 vs 53, GD 166 vs 167) does not move any cited line: every citation
   above was re-checked by grep against the fresh copies in this pass.
