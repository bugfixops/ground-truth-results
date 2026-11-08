# UNVERIFIED PROPOSAL — DO NOT RELY ON, MERGE, OR USE AS EVIDENCE YET

**Status: UNVERIFIED.** This is a coordinator first part from 2026-10-31, saved here so it is not lost. It has NOT passed a build, sampler, full-repo grep, or C1 checks on a full local checkout, and must be re-checked from printed source before any label, route, or graph change is relied on or merged.

**Branch rule:** work in progress is on work-2026-10-31 only, never main, and the 'result' branch is not used for work in progress unless the user says so.

---

# WP2 AmazeFileManager — first-set route checks (PROPOSED, NOT MERGED, NOT PUSHED)

Status: **PENDING — not verified for push.** This part was checked by a helper
that must not edit `graph_def.py`, `out/`, `progress/notes`, `tools/` or another
helper's files, and must not push. No file in `bugfixops/ground-truth-results`
was edited by this check. Nothing here is merged to branch `result`,
`work-2026-10-31`, or `main`.

## Sampler limitation (stated, not worked around)

- WP2 target is 30 sampled routes, seed 20261025, via
  `python3 -I tools/verify_sample.py AmazeFileManager 30 20261025`.
  That sampler reads `graphs/AmazeFileManager/out/methods.csv`.
- Via the GitHub connector alone, `out/methods.csv` (1,179,770 bytes) and
  `graphs/AmazeFileManager/graph_def.py` (1,058,622 bytes) are both too large
  for `get_file_contents` ("too large to display"), and `search_code` for this
  repo returned 0 results for `GlideOptions`, `SftpConnectDialog`, `E89e2cedd`
  and `Ee1aeff93`. There is no local clone on this VM.
- **Therefore no `sample_30.txt` output is claimed, no verification.csv row is
  written, and no C1 check (build / citations / routes / bytecode lines /
  scan_unreachable) was run.** The counts below cover only the routes/edges
  actually judged in this first set. WP2 for AmazeFileManager is NOT done.

## Re-checked baseline (from `out/`, not copied from the handover)

- `graphs/AmazeFileManager/out/build_report.txt` (read via connector):
  methods 2981; REACHABLE 2509; UNREACHABLE 472; errors 0; warnings 0;
  `path status: UNCHECKED 2509`.
- `graphs/AmazeFileManager/verification.csv` does **not** exist on
  `work-2026-10-31` (connector: "file does not exist"). That agrees with
  "0 route checks", independently of the handover's table.
- Standard configuration used for judging: debug build
  (`com.amaze.filemanager.debug`, DATASET.txt), fresh install, API 27,
  permissions only where a route needs them. AboutActivity is labelled from
  `src/fdroid` per the handover decision — not re-checked here.
- No tool coverage (Monkey, APE, `coverage_baseline.json`,
  `sanity_check.csv`, JaCoCo) was used as evidence for any verdict below.
  The build report's contradiction list was used only as a pointer to which
  methods to look at in source. `confirmed_by` below is only SOURCE or
  INFERRED, never DYN / FW-MEMORY / UNVERIFIED.
- No framework claim below rests on a printed `fw_src/android-8.1.0_r1/`
  line, because none was printed in this check. Framework dispatch steps
  (DialogFragment/Fragment lifecycle, AsyncTask `onPostExecute`, RecyclerView
  binding, ListPreloader) are therefore treated as standard/INFERRED, not
  FW-SRC, wherever a route depends on them.

## Routes / edges actually judged

### 1. E89e2cedd — WRONG (proposed fix, not merged)

Claimed edge (identified by hash reconstruction, see caveat below):
`SftpConnectDialog.lambda$null$2 -> GetSshHostFingerprintTask.execute`,
kind CALL, trigger "lambda executes GetSshHostFingerprintTask",
evidence `SRC SftpConnectDialog.java:198 }).execute();`
— from `graphs/AmazeFileManager/parts/repair_rp02.py`, which AGENT_NOTES
records as merged (build 016, "64 edges SftpConnectDialog lambdas").
Recomputing the build's edge id
(`tools/build_graph.py:assign_ids`: `E` + sha1 of
`src|dst|kind|trigger|guard|evidence|env|needs_state`, first 8 hex) over
that exact `repair_rp02.py` edge gives exactly `E89e2cedd`.

Why it is wrong, step by step against printed source:

- `method_list.json` gives `SftpConnectDialog.lambda$null$2` the descriptor
  `(String, String, int, String, String, String, boolean,
  DialogInterface, int)` — i.e. its functional-interface parameters are
  `(DialogInterface, int)`. That is a `DialogInterface.OnClickListener`,
  not a `Runnable` and not an AsyncTask callback. The same descriptor is
  shared by `lambda$null$6`; the two no-capture dismiss lambdas are the
  static `(DialogInterface, int)` entries `lambda$null$3` / `lambda$null$7`.
- The only `OnClickListener` lambdas in `SftpConnectDialog.java` are the
  dialog-button handlers at :190-194 (host-key-changed, positive) and
  :217-227 (host-key-verification, positive), plus the dismiss handlers at
  :195 and :227. None of them creates or executes a
  `GetSshHostFingerprintTask`.
- The task creation/execution that `repair_rp02.py` attributes to
  `lambda$null$2` is in fact at :178
  (`new GetSshHostFingerprintTask(hostname, port, taskResult -> {`) and
  :199 (`}).execute();`), inside the `removeConnection` callback passed at
  :176-177. That callback is a `Runnable` (no functional-interface
  parameters); the only remaining candidate in `method_list.json` is
  `lambda$null$5` (7 captured parameters, no trailing interface parameter).
- The cited line is also one line off even for the real call: :198 is the
  closing brace of `if (hostKey != null) {`, the `.execute()` is at :199.
  (This is the AGENT_BRIEF_V2 §5 "line number one line off" mistake, but
  here the source method itself is also wrong, so it is not a citation-only
  fix.)
- Upstream steps that DO check out on printed source (they do not save E89):
  `onCreateDialog` :160 `dialogBuilder.onPositive((dialog, which) -> {`;
  :175 `if (!isEmpty(sshHostKey)) {` (guard: this branch only runs for an
  existing stored host key; the `else` branch at :202 is a different task
  creation); :176-177 `SshConnectionPool.getInstance().removeConnection(...,
  () -> {`; `SshConnectionPool.java:94-95` `removeConnection` executes
  `AsyncRemoveConnection`; `SshConnectionPool.java:301-303`
  `onPostExecute` runs `callback.run()` if non-null. The AsyncTask
  dispatch itself was not FW-SRC-printed, so that link is standard/INFERRED.

Proposed fix (for the merger, not applied here):
1. Delete edge `E89e2cedd`.
2. Add `SftpConnectDialog.lambda$null$5 -> GetSshHostFingerprintTask.execute`,
   CALL, evidence `SRC SftpConnectDialog.java:178, 199`, guard
   `!isEmpty(sshHostKey)` (SftpConnectDialog.java:175).
3. Re-derive the whole `lambda$null$*` subgraph from `method_list.json`
   descriptors instead of `repair_rp02.py`'s guesses: `repair_rp02.py`
   also swaps `lambda$onCreateDialog$0` and `$9`
   (`$0` is the port-focus listener — descriptor `(EditText, View, boolean)`,
   matching :132-134; `$9` is the onPositive handler — descriptor
   `(EditText x5, boolean, MaterialDialog, DialogAction)`, matching
   :160-231), and it assigns the task callbacks (`lambda$null$4` /
   `lambda$null$8`, descriptors ending in `AsyncTaskResult`) to dialog
   buttons. Do not guess which of `lambda$null$2` / `lambda$null$6` is the
   :190 handler vs the :217 handler — their descriptors are identical;
   that assignment needs bytecode/class-file order, and is left open.
   Both, as a pair, go to `SftpConnectDialog.authenticateAndSaveSetup`
   (:191-194 and :220-222); only the :217-227 one also dismisses/logs
   (:219, :223-225).
- Verdict for this route: **wrong** (edge source wrong; citation also off
  by one). It counts in the error-rate numerator if the merger counts
  "proposed fix" as "fixed".

Caveat: the current `graph_def.py` line for E89 was not directly printed
(file too large for the connector). The identification rests on the exact
sha1 match against the merged `repair_rp02.py` edge. If the merger edited
that edge's trigger/evidence after the merge, its id would have changed
and this identification must be re-checked from a local checkout.

### 2. Ee1aeff93 — WRONG (proposed fix, not merged)

Claimed edge (as named in the task/handover):
`CompressedExplorerFragment.<init> -> Decompressor.decompress`.

Why it is wrong, step by step against printed source:

- `CompressedExplorerFragment.java` has no explicit constructor in the
  printed file: lines 82-126 are field declarations (including
  `private Decompressor decompressor;` at :116, declared but not assigned),
  and the first method is `onCreate` at :127. The implicit `<init>` therefore
  only runs field initialisers; it calls nothing named `decompress`.
- The only `decompress(` call in the printed file is at :329:
  `decompressor.decompress(compressedFile.getPath(), dirs);`, inside
  `CompressedExplorerFragment$1.onActionItemClicked` (:306-335),
  `case R.id.ex:` (:321), after building `dirs` from checked positions
  (:324-327), and followed by `mode.finish()` at :331.
- `Decompressor.java` has two overloads: `decompress(String)` at :43 and
  `decompress(String, String[])` at :55. The :329 call matches the
  two-argument overload. A bare target name `Decompressor.decompress` is
  therefore ambiguous and, per the `method_names` rule in
  `tools/build_graph.py`, should be qualified.
- `decompressor` itself is only assigned at :215
  (`CompressedHelper.getCompressorInstance(...)` in `onActivityCreated`,
  guarded by `savedInstanceState == null && compressedFile != null` at
  :209) and at :243 (in `onRestoreInstanceState`). An `<init>`-to-`decompress`
  edge skips both assignments and the action-mode guard.
- `parts/label_b014.py` (the CompressedExplorerFragment part) contains no
  `onActionItemClicked -> Decompressor.decompress` edge at all; it only has
  `onActionItemClicked -> onDestroyActionMode` (citing :320, which is in the
  `R.id.all` branch, not the `R.id.ex` branch — secondary observation,
  not counted below).

Proposed fix (for the merger, not applied here):
1. Delete edge `Ee1aeff93` (`<init> -> Decompressor.decompress`).
2. Add `CompressedExplorerFragment$1.onActionItemClicked ->
   Decompressor.decompress(String,String[])`, CALL,
   evidence `SRC fragments/CompressedExplorerFragment.java:329`,
   guard `item.getItemId() == R.id.ex` (:307, :321) with `decompressor`
   assigned (onActivityCreated :215 / onRestoreInstanceState :243).
   The action-mode start itself (`mActionModeCallback` field at :247,
   `onCreateActionMode` showing `R.id.ex` at :277) is framework/standard
   and was not FW-SRC-printed.
- Verdict for this route: **wrong**. It counts in the error-rate numerator
  if the merger counts "proposed fix" as "fixed".

Caveat: Ee1 was not hash-matched (its exact trigger/evidence/kind text
in the current graph could not be printed — `graph_def.py` too large,
`auto_calls.json` 1,839,161 bytes also too large for the connector).
The verdict judges the source→target pair as named in the task; the
merger must confirm the exact edge text from a local checkout before
deleting.

### 3. GlideRequest.listener — WRONG LABEL (proposed fix: REACHABLE, not merged)

Current label (per `out/build_report.txt` contradiction pointer, judged
from source only): UNREACHABLE. That label is wrong on printed source:

- `RecyclerAdapter.java:116` `private RecyclerPreloadModelProvider modelProvider;`
  and :388 `modelProvider = new RecyclerPreloadModelProvider(mainFrag, uris);`
- `RecyclerPreloadModelProvider.java:26` field `GlideRequest<Drawable> request;`
  :30 `request = GlideApp.with(fragment).asDrawable().centerCrop();`
  (`GlideApp.with` returns `GlideRequests` per `method_list.json`;
  `GlideRequests.asDrawable()` returns `GlideRequest`, so `.centerCrop()`
  here is `GlideRequest.centerCrop`, not `GlideOptions.centerCrop`.)
- `RecyclerPreloadModelProvider.java:43-52` `getPreloadRequestBuilder`
  returns `request.load(...)` — runtime receiver type `GlideRequest`.
- `RecyclerAdapter.java:899` (in `showThumbnailWithBackground`, :856) and
  :945 (in `showRoundedThumbnail`, :902):
  `modelProvider.getPreloadRequestBuilder(iconData).listener(requestListener).into(view);`
  The `.listener(...)` call on that `GlideRequest` receiver is therefore
  `GlideRequest.listener` at runtime (virtual dispatch from the
  `RequestBuilder` static type), in two reachable adapter methods called
  from the list binding at :595, :598, :608 (thumbnail) and :724, :733
  (rounded thumbnail, guarded by `PREFERENCE_SHOW_THUMB` at :732).
- This is a label verdict, not a full printed route: the launcher→
  MainFragment→RecyclerAdapter steps were not printed step-by-step in
  this check, so the complete route is **not** claimed correct — only that
  UNREACHABLE is false and the method needs a route.

Proposed fix (for the merger, not applied here): remove the UNREACHABLE
entry for `GlideRequest.listener`; add/keep the route
`RecyclerAdapter.showThumbnailWithBackground / showRoundedThumbnail ->
GlideRequest.listener` with evidence `SRC adapters/RecyclerAdapter.java:899, 945`
and the receiver chain above. Confirm the same reasoning for the other
`GlideRequest.*` contradiction names only after printing their call sites;
do not generalise from `listener` alone.
- Verdict for this item: **wrong** (label). Counts in the error-rate
  numerator if counted as "fixed" once the route is added.

### 4. GlideOptions.* / GlideRequest.* contradictions as a group — UNCLEAR (not resolved)

- The saved `graphs/AmazeFileManager/scratch/glide_method_grep.txt` does
  **not** satisfy KIRO §3 rule C5. It greps bare method names, so its
  "YES" hits are mostly unrelated methods: e.g. `GlideOptions.apply`
  "found" via `SharedPreferences.Editor.apply()` (ColorPreferenceHelper,
  ColorPickerDialog, GeneralDialogCreation, …) and `GlideOptions.decode`
  "found" via `URLDecoder.decode` / `Uri.decode` / `Base64.decode`.
  It never greps the class name `GlideOptions` over the source folder.
- `parts/label_1.md`'s Glide reasons are demonstrably wrong on printed
  source and are superseded history, not the current graph: it claims
  `GlideOptions.apply` from "AppsAdapterPreloadModel.java:28 …fitCenter()
  chain" (line 28 shows `fitCenter()` on a `GlideRequest`, not `apply()`
  on a `GlideOptions`) and `GlideOptions.clone` from
  "AppsAdapterPreloadModel.java:44 …request.clone()" (line 24 types
  `request` as `GlideRequest<Drawable>`, so that is `GlideRequest.clone`).
  Likewise `GlideRequests.as` from "asDrawable() calls" conflates `as(Class)`
  with `asDrawable()`.
- Files actually printed in this check (the two glide providers,
  `RecyclerAdapter.java`, `AppsAdapter.java`, `AppsListFragment.java`
  excerpts) contain **no** `GlideOptions` reference and no call to
  `GlideOptions.<init> / apply / autoClone / clone / lock`,
  `GlideRequest.addListener / apply / downsample / optionalCenterInside /
  optionalFitCenter / set / transform(Transformation)`, or
  `GlideRequests.as / setRequestOptions`. That is absence in 4-5 files,
  not a whole-app grep, so it does not prove the UNREACHABLE labels.
- What is needed (decision/blocker below): a real
  `grep -rn "GlideOptions" / "GlideRequest\."` over
  `final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java`
  from a local checkout, plus printing every distinct Glide call site and
  resolving each receiver's class (GlideRequest vs GlideOptions vs
  library RequestBuilder) before any Glide label is called correct.
- Verdict for the Glide contradiction group: **unclear** (excluded from
  the error-rate denominator, per the route-check rule).

## Error-rate-style counts (only routes actually judged)

Judged items: E89 edge, Ee1 edge, GlideRequest.listener label = 3 items
with a verdict (2 wrong edges + 1 wrong label). GlideOptions group = 1
unclear item, excluded.

- correct: 0
- proposed fix (= "fixed" for error-rate purposes, if the merger applies them): 3
  (E89, Ee1, GlideRequest.listener)
- wrong (unfixed, as delivered): 0 — every wrong item above carries a
  concrete proposed fix; none is left as bare "wrong" without a fix.
- unclear: 1 (Glide group)
- Error rate on judged, non-unclear items = (fixed + wrong) / (correct + fixed + wrong)
  = (3 + 0) / (0 + 3 + 0) = **1.00 (3/3)**. This is the error rate of this
  deliberately issue-first set, NOT of AmazeFileManager as a whole and NOT
  of the WP2 sample of 30. Do not quote it as the app's error rate.
- If "proposed fix" is counted strictly as "not yet fixed" (because this
  helper merged nothing), then: fixed = 0, wrong = 3, correct = 0, and the
  same 3/3 fraction applies with the label "wrong, fix proposed".

## Proposed fixes summary (separable set for the merger, branch `result` only)

1. Delete `E89e2cedd`; add `SftpConnectDialog.lambda$null$5 ->
   GetSshHostFingerprintTask.execute` (evidence :178, :199; guard :175).
2. Re-derive SftpConnectDialog `lambda$null$*` edges from
   `method_list.json` descriptors (swap `$0`/`$9` back; `$2`/`$6` are
   dialog-button handlers, `$3`/`$7` dismiss handlers, `$4`/`$8` task
   callbacks). Leave the `$2` vs `$6` assignment open pending bytecode order.
3. Delete `Ee1aeff93`; add `CompressedExplorerFragment$1.onActionItemClicked
   -> Decompressor.decompress(String,String[])` (evidence :329; guard
   `R.id.ex`).
4. Remove UNREACHABLE for `GlideRequest.listener`; add the RecyclerAdapter
   :899/:945 route (receiver chain via RecyclerPreloadModelProvider :26,
   :30, :43-52).
5. Do NOT flip any GlideOptions.* label on the basis of
   `glide_method_grep.txt` or `label_1.md` — both are shown above to
   conflate GlideRequest calls with GlideOptions calls.

## Blockers / decisions needed (for the parent / merger)

1. **Local checkout required.** A merger with a full checkout must:
   print the current `graph_def.py` lines for E89/Ee1, confirm the hash
   identification, apply fixes 1-4, rebuild, re-print the routes, and run
   all eight §2 checks. This connector-only check cannot do any of that.
2. **Sampler still outstanding.** Run `tools/verify_sample.py AmazeFileManager
   30 20261025` on a full checkout, print every sampled route step, judge
   each step, and only then write `verification.csv` (via
   `make_verification.py`, never by hand) and the WP2 table. Until then
   this part is **pending, not pushable** under the updated push rule.
3. **Glide full-folder grep (C5).** Run a class-name grep for `GlideOptions`
   and `GlideRequest.` over the app source folder and print every distinct
   call site with its receiver class. Until then the Glide contradiction
   group stays **unclear**.
4. **Sftp `$2` vs `$6` assignment.** Needs bytecode/class-file lambda order;
   do not guess it from source order (source order ≠ `$null$` numbering
   for nested lambdas).
5. **Framework lines.** Any route that depends on Fragment/DialogFragment
   lifecycle, AsyncTask dispatch, or ListPreloader callbacks needs printed
   `FW-SRC` lines from `fw_src/android-8.1.0_r1/` to be SOURCE; otherwise
   its `confirmed_by` is INFERRED. None was printed here.
6. **Push routing.** When (and only when) items 1-2 are done and the fixes
   are verified by re-printing, this part may be merged and pushed as a
   separate commit to branch `result` in `bugfixops/ground-truth-results`
   only, naming AmazeFileManager and this part — never to
   `work-2026-10-31` or `main`, and never by this helper directly (to
   avoid conflicts with parallel helpers on shared files).

## Files read (connector, branch work-2026-10-31 unless noted)

- `handoff/MUSE_HANDOVER.md` (§2, WP2), `handoff/KIRO_CONVERT_APPS.md`
  (§§3-4), `handoff/AGENT_BRIEF_V2.md` (§5), `handoff/SCHEMA_V2.md` (full),
  `graphs/AmazeFileManager/AGENT_NOTES.md` (full).
- `graphs/AmazeFileManager/out/build_report.txt`, `out/README.md`;
  `graphs/AmazeFileManager/scratch/conflicts.md`, `items_D_glide.tsv`,
  `items_E_structural.tsv`, `glide_method_grep.txt`,
  `glide_unreachable_entries_to_add.txt`, `unreachable_glide_list.txt`,
  `edge_lines.json`, `unreach_lines.json`, `unreachable_analysis.txt`.
- `graphs/AmazeFileManager/parts/repair_rp02.py`, `label_b014.py`,
  `label_b014.md`, `label_1.md`, `label_1.py`.
- `graphs/AmazeFileManager/method_list.json` (2981 rows).
- `tools/build_graph.py` (`assign_ids`), `tools/verify_sample.py`,
  `tools/show_route.py`.
- App source (all via connector, branch work-2026-10-31):
  `final_java_only/AmazeFileManager/app/DATASET.txt`,
  `.../ui/dialogs/SftpConnectDialog.java`,
  `.../filesystem/ssh/SshConnectionPool.java`,
  `.../fragments/CompressedExplorerFragment.java`,
  `.../filesystem/compressed/showcontents/Decompressor.java`,
  `.../adapters/glide/RecyclerPreloadModelProvider.java`,
  `.../adapters/glide/AppsAdapterPreloadModel.java`,
  `.../adapters/RecyclerAdapter.java`, `.../adapters/AppsAdapter.java`,
  `.../fragments/AppsListFragment.java` (excerpts).
- Not read, deliberately: `coverage_baseline.json`, `sanity_check.csv`
  (tool coverage, never evidence); `graph_def.py` and `out/methods.csv`
  in full (too large for the connector — see limitation above).
