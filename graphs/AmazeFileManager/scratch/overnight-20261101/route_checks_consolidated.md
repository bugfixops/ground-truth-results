# AmazeFileManager — route-check consolidation, stream B overnight (LOCAL ONLY, NOT MERGED, NOT PUSHED)

Branch: work-2026-10-31, repo bugfixops/ground-truth-results.
Standard configuration: debug build (com.amaze.filemanager.debug, DATASET.txt),
fresh install, API 27, runtime permissions only where a route needs them.
AboutActivity comes from src/fdroid (task instruction; not re-checked here).

## What this file is, and is not

- This is NOT the 30-route sampler table. The sampler
  (`python3 -I tools/verify_sample.py AmazeFileManager 30 20261025`) reads
  `graphs/AmazeFileManager/out/methods.csv` (1,179,770 bytes), which the
  GitHub connector refuses ("too large to display"), and there is no
  chunk/range parameter in get_file_contents. No sample_30.txt, no sample
  error rate, and no verification.csv row is claimed in this file.
- Section A = items I re-derived MYSELF tonight from locally printed
  source files (the 10 java files already on this VM under
  ~/workspace/wp2-amaze/scratch/) plus the branch-verified method_list.json.
  Line numbers below were re-checked with grep/sed tonight, not copied.
- Section B = prior WP2 proposals (first set, second set, Glide group,
  non-Glide group, helper-4 fold) carried as INPUT ONLY. Their defining or
  caller files were NOT locally printed tonight, so I do not re-verify
  them here; the merger must still print them on a full checkout.
- No tool coverage, old generated graph, or build REACHABLE count was used
  as evidence for any verdict. confirmed_by is SOURCE only where lines
  were printed tonight (section A), otherwise as stated in the prior
  report (section B). Never DYN / FW-MEMORY / UNVERIFIED.
- No framework claim here rests on a printed fw_src/android-8.1.0_r1/
  line (none printed tonight). Framework dispatch steps (DialogFragment
  lifecycle, AsyncTask onPostExecute, RecyclerView binding, ListPreloader)
  are standard/INFERRED wherever a route depends on them.

## Baseline, verified from the branch tonight (not from the handover)

- `graphs/AmazeFileManager/out/build_report.txt` fetched via connector:
  methods 2981, pages 12, edges 7768; REACHABLE 2509, UNREACHABLE 472
  (closed_by_api_level 9, framework_never_calls 39, no_trigger_in_app 424);
  errors 0, warnings 0; path status UNCHECKED 2509; 21 UNREACHABLE-but-ran
  contradictions; 1 ENV-gated-but-ran (TextEditorActivity.<init>).
  Identical (diff-clean) to the local prior copy.
- `graphs/AmazeFileManager/scratch/build_finish_30.txt` fetched via
  connector: same blob SHA as out/build_report.txt, same counts.
- `graphs/AmazeFileManager/method_list.json` fetched via connector:
  673,134 bytes, md5-identical to the local copy, 2981 entries.
- `tools/build_graph.py` local copy: git blob hash matches the branch
  listing SHA, so it is branch-identical. verify_sample.py (2373 bytes)
  and show_route.py (5314 bytes) match branch sizes only (hash not
  verified). check_citations.py, check_routes.py, check_bytecode_lines.py,
  scan_unreachable.py, gen_readme_v2.py were NOT fetched tonight; the
  eight checks are not run (see Blockers), so their tool copies do not
  change any outcome tonight.
- Branch root listing confirms: NO verification.csv, NO readme_notes.md,
  NO LESSONS.md, NO make_verification.py under graphs/AmazeFileManager/.
  So verification.csv cannot be produced "via make_verification.py"
  tonight even apart from the build blocker: that script must first be
  authored (on the examples pattern) on a full checkout.

## Section A — re-derived tonight from printed source

### A1. SftpConnectDialog edge E89e2cedd — WRONG, fix proposed (not applied)

Claimed edge (hash-matched by prior work against parts/repair_rp02.py;
current graph_def.py line NOT printed tonight — merger must confirm):
`SftpConnectDialog.lambda$null$2 -> GetSshHostFingerprintTask.execute`,
evidence `SRC SftpConnectDialog.java:198 }).execute();`.

Re-checked lines (SftpConnectDialog.java, local printed copy):
- :160 `dialogBuilder.onPositive((dialog, which) -> {`
- :175 `if (!isEmpty(sshHostKey)) {`
- :176-177 `SshConnectionPool.getInstance().removeConnection(..., () -> {`
- :178 `new GetSshHostFingerprintTask(hostname, port, taskResult -> {`
- :199 `}).execute();`  — :198 is the closing brace of
  `if (hostKey != null) {`, so the cited :198 is one line off.
- The else branch at :202-229 creates a second, different task
  (`:203 new GetSshHostFingerprintTask`, `:229 }).execute();`).

Descriptors (branch-verified method_list.json):
- lambda$null$2 and lambda$null$6 both end `(DialogInterface, int)`:
  dialog-button handlers, not a Runnable, not a task callback.
- lambda$null$3 / lambda$null$7 are static `(DialogInterface, int)`:
  dismiss handlers.
- lambda$null$4 / lambda$null$8 end in `AsyncTaskResult`: task callbacks.
- lambda$null$5 is `(String, int, String, String, String, String,
  boolean)`: 7 captures, no trailing interface parameter — the only
  lambda$null$ candidate for the :176-177 Runnable by elimination.

CORRECTION to the prior second-set claim: the second set said the
$5 descriptor matches the Runnable's captures "EXACTLY in count and
types". Count (7) and type multiset match, but the descriptor order
(String, int, String, String, String, String, boolean) is NOT the
source-textual capture order (connectionName String, hostname String,
port int, sshHostKey String, username String, password String,
edit boolean). The elimination argument stands; the exact-order claim
does not, and I do not repeat it. The $2-vs-$6 assignment (handlers at
:190-194 vs :217-227) stays OPEN pending bytecode/class-file order;
do not guess it.

Upstream steps that check out (AsyncTask dispatch INFERRED):
SshConnectionPool.java:94 `public void removeConnection(... Runnable
callback)`, :95 `new AsyncRemoveConnection(url, callback).execute();`,
:301 `onPostExecute`, :303 `callback.run()` (guarded by non-null at :302).

Proposed fix (for the merger, not applied): delete E89e2cedd; add
`SftpConnectDialog.lambda$null$5 -> GetSshHostFingerprintTask.execute`,
CALL, evidence `SRC ui/dialogs/SftpConnectDialog.java:178,199`,
guard `!isEmpty(sshHostKey)` (:175).

### A2. CompressedExplorerFragment edge Ee1aeff93 — WRONG / MISSING, fix proposed

Claimed pair: `CompressedExplorerFragment.<init> ->
Decompressor.decompress`. Prior work found NO entry for Ee1aeff93 in
the saved edge_lines.json snapshot; I did not re-verify that snapshot
claim tonight (graph_def.py unprinted), so the merger must confirm
presence on a checkout. If absent, the fix is purely an ADD.

Re-checked lines:
- CompressedExplorerFragment.java has no explicit constructor in the
  printed file; `<init>` calls nothing named decompress.
- :215 `decompressor = CompressedHelper.getCompressorInstance(...)`
  in onActivityCreated, guarded at :209 by
  `savedInstanceState == null && compressedFile != null`.
- :243 same assignment in onRestoreInstanceState.
- :306 `onActionItemClicked`, :321 `case R.id.ex:`, :329
  `decompressor.decompress(compressedFile.getPath(), dirs);`,
  :331 `mode.finish()`.
- Decompressor.java: :43 `decompress(String)`, :55
  `decompress(String, String[])`. The :329 call matches the
  two-argument overload; a bare `Decompressor.decompress` target is
  ambiguous.

Proposed fix: add `CompressedExplorerFragment$1.onActionItemClicked ->
Decompressor.decompress(String,String[])`, CALL, evidence
`SRC fragments/CompressedExplorerFragment.java:329`, guard
`item.getItemId() == R.id.ex` (:307, :321) with decompressor assigned
(:215 / :243). Delete Ee1aeff93 only if the checkout confirms it exists.

### A3. GlideRequest.listener — WRONG LABEL, REACHABLE proposed

Build-report pointer only (UNREACHABLE but ran; coverage is not evidence).
Re-checked lines:
- RecyclerPreloadModelProvider.java: :26 field
  `GlideRequest<Drawable> request;`, :30
  `request = GlideApp.with(fragment).asDrawable().centerCrop();`,
  :43-52 `getPreloadRequestBuilder` returns `request.load(...)`.
  The stored object IS a GlideRequest<Drawable>.
- RecyclerAdapter.java: :899 and :945
  `modelProvider.getPreloadRequestBuilder(iconData).listener(requestListener).into(view);`
  in showThumbnailWithBackground (:856) and showRoundedThumbnail (:902).
  The `.listener(...)` receiver at runtime is GlideRequest by virtual
  dispatch from the static RequestBuilder type. Callers of those two
  methods are guarded by PREFERENCE_SHOW_THUMB (prior report cites
  :593, :607, :719, :732; not re-grepped tonight — merger to confirm
  the guard lines on checkout).
- The full launcher-to-adapter head was not printed step-by-step
  tonight, so this is a label verdict (UNREACHABLE is false) plus the
  printed receiver chain, not a claimed full route.

Proposed fix: remove the UNREACHABLE entry for GlideRequest.listener;
add the :899 / :945 route edges.

### A4. GlideRequest.clone — REACHABLE proposed (NOT GlideOptions.clone)

Re-checked lines (AppsAdapterPreloadModel.java):
- :24 field `GlideRequest<Drawable> request;`
- :28 `request = GlideApp.with(f).asDrawable().fitCenter();`
- :45 `return request.clone().load(item);` in getPreloadRequestBuilder.

CORRECTION to all prior files: the clone line is :45, not :44, in the
locally printed copy (grep-verified tonight). Fix fragments citing :44
must be corrected to :45 before merge. The :44 citation in the prior
folded file is wrong by one line; the verdict is unaffected.

The receiver is GlideRequest, so this resolves GlideRequest.clone
only. GlideOptions.clone is a DIFFERENT method and is NOT resolved by
this site. Whether GlideRequest.clone is currently UNREACHABLE in the
branch graph is NOT established tonight (it is absent from the
363-entry unreach snapshot, which covers only 363 of 472 UNREACHABLE
entries — absence proves nothing). Merger: confirm its current label
on checkout; if already REACHABLE, add/confirm only the edge.

### A5. IconDataParcelable.setImageBroken — REACHABLE proposed

Re-checked lines (RecyclerAdapter.java):
- Method-reference sites: :596, :599, :609 (list branches) and
  :724, :733 (grid branches), each passing
  `rowItem.iconData::setImageBroken` as the OnImageProcessed argument
  to showThumbnailWithBackground / showRoundedThumbnail.
- showThumbnailWithBackground (:856): the errorListener parameter is
  invoked at :864 (`onImageProcessed(true)`, already-broken early
  return), :883 (onLoadFailed), :895 (`onImageProcessed(false)`,
  onResourceReady) — verified by sed tonight for the :856-899 block.
  The :912 / :930 / :941 invocations in showRoundedThumbnail were
  NOT re-read tonight (prior report's citation; merger to confirm).
- OnImageProcessed is a single-method interface with
  `void onImageProcessed(boolean)`, matching setImageBroken's
  descriptor `(Z)V` (prior report cites RecyclerAdapter.java:1029-1031;
  not re-read tonight).

A method reference is a real call site even though no
`setImageBroken(...)` call text appears. The onBindViewHolder head is
RecyclerView dispatch (INFERRED).

Proposed fix: remove the UNREACHABLE entry for
IconDataParcelable.setImageBroken; add the thumbnail-callback route
edges (evidence :596, :599, :609, :724, :733 for the references and
:864, :883, :895 for the invocations; :912, :930, :941 to confirm).

### A6. GlideRequests.as — REACHABLE proposed, INFERRED delegation step only

Re-checked anchor sites (SOURCE):
- RecyclerPreloadModelProvider.java:30 `GlideApp.with(fragment).asDrawable()`
- AppsAdapterPreloadModel.java:28 `GlideApp.with(f).asDrawable()`
  In both, the `.asDrawable()` receiver is the GlideRequests object
  returned by `GlideApp.with(...)`.
- The step `asDrawable() -> as(Drawable.class)` is generated-code
  delegation: generated GlideRequests.java is NOT in final_java_only
  and was not printed tonight. So this verdict is INFERRED for that
  step, SOURCE for the anchors. A merger requiring SOURCE-only edges
  must HOLD this fix and first print build-generated GlideRequests.java
  to confirm `asDrawable() { return as(Drawable.class); }`.

### A7. GlideOptions group — OPEN (13 methods, not flipped)

No `GlideOptions` reference and no `.apply(`, `.addListener(`,
`.downsample(`, `.transform(`, `optionalCenterInside`,
`optionalFitCenter`, or `new GlideOptions` call appears in any file
printed tonight (Sftp, SshConnectionPool, CompressedExplorer,
Decompressor, both glide providers, RecyclerAdapter). That is absence
in 7 files, not a whole-tree grep, so it proves no UNREACHABLE label.
The 13 OPEN methods: GlideOptions.<init>, .apply, .autoClone, .clone,
.lock; GlideRequest.addListener, .apply, .downsample,
.optionalCenterInside, .optionalFitCenter, .set,
.transform(Transformation); GlideRequests.setRequestOptions.
Resolvers (from prior Glide report, adopted): print build-generated
GlideRequests.java / GlideRequest.java; receiver-typed grep over the
unprinted remainder of the tree; Glide library source for the app's
Glide version (not in fw_src) for lock/clone/autoClone dispatch.
In particular, do NOT add any edge for GlideOptions.clone from
AppsAdapterPreloadModel.getPreloadRequestBuilder — that site is
GlideRequest.clone (A4).

## Section B — prior WP2 proposals carried as INPUT ONLY (not re-verified tonight)

| Item | Prior verdict | Why not re-verified tonight |
|---|---|---|
| LayoutElementParcelable.writeToParcel | REACHABLE proposed (MainFragment.onSaveInstanceState :397, :402, :415 putParcelableArrayList; Bundle marshalling INFERRED) | MainFragment.java, IconDataParcelable.java, LayoutElementParcelable.java not locally printed tonight |
| RoundedImageView.setBackgroundColor | REACHABLE proposed (grid branch + PREFERENCE_USE_CIRCULAR_IMAGES; :716 cast, :742 selection, :744+ calls; :723 imageView1 deliberately NOT cited) | RoundedImageView.java, ItemViewHolder.java not locally printed tonight; RecyclerAdapter lines :716/:742/:744 re-confirmed tonight, but the override definition itself was not re-read |
| SimpleTextWatcher.beforeTextChanged / onTextChanged | REACHABLE proposed (RenameBookmark :86-93, :112-119 register anonymous watchers overriding only afterTextChanged; TextView dispatch INFERRED) | SimpleTextWatcher.java, RenameBookmark.java not locally printed tonight |
| SimpleTextWatcher.afterTextChanged | OPEN (RenameBookmark overrides do not call super; needs whole-folder registration hunt) | Same as above |
| TextEditorActivity.<init> | OPEN (ENV-gate question unanswered; gate text lives in unprinted graph_def.py) | TextEditorActivity.java, manifest, FileUtils launch path not printed tonight |
| Sftp $2 vs $6 assignment | OPEN (needs bytecode/class-file lambda order) | Same as A1 |
| 13 Glide OPEN methods | OPEN | See A7 |

Note on section B line citations: where a prior citation conflicts
with a line I re-read tonight, tonight's reading wins (clone :45, not
:44). All other section B citations are as the prior reports state
them and are the merger's to confirm on checkout.

## Counts on judged items tonight (NOT the app sample error rate)

- Section A verdicts with a proposed fix: A1 (wrong edge), A2
  (wrong/missing edge), A3 (wrong label), A4 (proposed REACHABLE),
  A5 (proposed REACHABLE), A6 (proposed REACHABLE, INFERRED step) = 6.
- Section A OPEN: A7 group (13 methods, counted as one group item).
- No item was judged "correct" tonight, because no sampled route was
  available to judge correct: the sampler is blocked (see Blockers).
  Therefore NO sample error rate is computed here. Quoting
  (fixed+wrong)/(correct+fixed+wrong) over this issue-first set would
  be 6/6 = 1.00, which is the error rate of a deliberately
  issue-first selection, NOT the app's error rate, and it must not be
  quoted as such.

## Proposed fix fragments (UNVERIFIED, for the merger on a full checkout only)

Full text with corrected :45 citation is in
scratch/proposals_streamB_UNVERIFIED.py in this local mirror. Summary:
delete E89e2cedd (confirm line on checkout); add lambda$null$5 ->
GetSshHostFingerprintTask.execute (:178, :199, guard :175); add
onActionItemClicked -> Decompressor.decompress(String,String[]) (:329,
guard R.id.ex); remove UNREACHABLE for GlideRequest.listener,
GlideRequest.clone (conditional on checkout label),
IconDataParcelable.setImageBroken; add their routes; add
GlideRequests.asDrawable -> GlideRequests.as ONLY with the INFERRED
flag noted (hold if SOURCE-only required). Section B fixes are as in
the prior helper-4 fold, unchanged except the :44 -> :45 correction
for the clone edge.

## Blockers (exact)

1. GRAPH RECONSTRUCTION BLOCKED. `graphs/AmazeFileManager/graph_def.py`
   (1,058,622 bytes) — connector fetch attempted tonight, reply:
   "too large to display (1058622 bytes)". `auto_calls.json`
   (1,839,161 bytes) and `out/methods.csv` (1,179,770 bytes) exceed the
   same limit (methods.csv barrier confirmed by helper 4; auto_calls
   size confirmed by branch directory listing tonight). get_file_contents
   has no chunk/range/offset parameter (schema verified via list-tools
   tonight). The download URL the connector offers carries a token
   that is redacted in tool output; per the hard constraints it was
   NOT unwrapped, NOT used, and NOT recorded. No git clone exists on
   this VM (clone fails without auth; not attempted tonight because
   the task forbids waiting for / using a token and directs connector
   use instead).
2. PARTS ASSEMBLY FALLBACK FAILS. Branch `merge_parts.py` (fetched
   tonight, 5353 bytes) is NOT a general assembler: it appends
   UNREACHABLE entries from 4 specific label parts (b041, b042, b043,
   b045) to an existing graph_def.py. The parts/ fragments do not
   contain the base graph (entries, SCREENS, hand edges, SUPPRESS,
   ENV_KINDS_OF, CLASSIFY/EDIT hooks), so no faithful current
   graph_def.py can be assembled from parts/ alone. Substituting an
   older under-1MB scratch copy (e.g. graph_def_before_rb12.py,
   746,302 bytes) was REJECTED: it is an intermediate state, not the
   current graph, and building it would not reproduce 2509/472.
3. CONSEQUENTLY NOT RUN: the build (needs graph_def.py + auto_calls.json),
   the sampler (needs methods.csv), show_route printing of sampled
   routes, all eight checks, make_verification.py / verification.csv,
   gen_readme_v2.py / out/README.md. No check is marked passed without
   its printed output. The branch build report's 0 errors / 0 warnings
   are the branch's own prior output, re-fetched and diff-verified
   tonight — they are NOT a fresh local build result.
4. SOURCE TREE GAP. No full AmazeFileManager source tree exists on this
   VM (only 10 java files under ~/workspace/wp2-amaze/scratch/);
   final_java_only/ is not present locally. Further route judging
   needs connector fetches of individual source files (one at a time,
   ~30 s apart) or a full checkout arranged by the parent.
