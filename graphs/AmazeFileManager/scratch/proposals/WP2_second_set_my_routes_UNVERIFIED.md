# UNVERIFIED PROPOSAL — has NOT passed build, sampler, full-repo grep, or C1 checks; re-check from printed source before relying/merging.

# WP2 AmazeFileManager — second set, my routes (PROPOSED, NOT MERGED, NOT VERIFIED FOR [K])

Repo: bugfixops/ground-truth-results, branch work-2026-10-31 only.
Status: UNVERIFIED proposal. No build, sampler, grep, or C1 check was run in this
session, and no such count is claimed. No graph_def.py / out/ edit was made,
nothing was pushed by this part. This is a route-judging set from printed
source only, to be merged by a merger with a full checkout after printing
current graph_def.py lines, rebuilding, and re-printing.

Baseline (re-checked, not copied): out/build_report.txt — methods 2981,
REACHABLE 2509, UNREACHABLE 472, errors 0, warnings 0, path UNCHECKED 2509.
verification.csv does not exist on work-2026-10-31 (first set, re-affirmed
here as the reason no WP2 sample table is claimed yet).
Standard configuration: debug build (com.amaze.filemanager.debug, DATASET.txt),
fresh install, API 27, permissions only where a route needs them.
No tool coverage, old generated graphs, or build REACHABLE counts were used as
evidence. confirmed_by is SOURCE only where lines were printed, otherwise
INFERRED. Never DYN / FW-MEMORY / UNVERIFIED.
Framework dispatch (Fragment/DialogFragment lifecycle, AsyncTask
onPostExecute, RecyclerView binding, Glide library internals) is
standard/INFERRED unless FW-SRC lines are printed — none were printed here.

## 1. First-set re-verification (from local printed files, lines re-read)

### 1a. E89e2cedd — WRONG, fix confirmed, with two refinements
- Edge-line index (saved scratch/edge_lines.json, snapshot — merger must
  confirm against current graph_def.py): E89e2cedd -> graph_def.py line 11617.
  That index is evidence the edge exists in the snapshot; the merger must
  print line 11617 on a full checkout before deleting.
- Refinement 1 (strengthens the first set): SftpConnectDialog.lambda$null$5
  capture signature matches the removeConnection Runnable EXACTLY in
  count and types, not just by elimination. The Runnable (SftpConnectDialog
  :176-177) directly uses: connectionName (String), hostname (String),
  port (int), sshHostKey (String), username (String), password (String),
  edit (boolean). selectedParsedKeyPair / selectedParsedKeyPairName are
  fields (:90, :92), not captures. That is String,int,String,String,
  String,String,boolean — exactly lambda$null$5's descriptor in
  method_list.json. The other $null$ lambdas do not match: $2/$6 end in
  (DialogInterface,int) = dialog-button handlers; $3/$7 are static
  (DialogInterface,int) = dismiss handlers; $4/$8 end in AsyncTaskResult =
  GetSshHostFingerprintTask callbacks.
- Refinement 2: the real task call is at :178
  (new GetSshHostFingerprintTask(hostname, port, taskResult -> {) and :199
  (}).execute();), inside the removeConnection callback. The first set's
  :198 citation is one line off (that line is the closing brace of
  if (hostKey != null) {).
- Route, printed step by step: onCreateDialog :160 onPositive handler
  (lambda$onCreateDialog$9, descriptor EditText x5, boolean, MaterialDialog,
  DialogAction — matches :160-231) -> :175 guard !isEmpty(sshHostKey) ->
  :176-177 SshConnectionPool.removeConnection(..., Runnable) ->
  SshConnectionPool.java:94-95 removeConnection creates
  AsyncRemoveConnection and executes it -> :301-303 onPostExecute runs
  callback.run() if non-null (AsyncTask dispatch INFERRED) ->
  lambda$null$5 body -> :178/:199 GetSshHostFingerprintTask.execute.
  Verdict: wrong (edge source wrong, citation off by one). Proposed fix
  unchanged from first set: delete E89e2cedd; add
  lambda$null$5 -> GetSshHostFingerprintTask.execute, CALL, evidence
  SRC SftpConnectDialog.java:178,199, guard !isEmpty(sshHostKey) (:175).
  Proposed fix fragment:
  e('SftpConnectDialog.lambda$null$5', 'GetSshHostFingerprintTask.execute', 'CALL',
    'removeConnection callback creates and executes fingerprint task',
    evidence='SRC ui/dialogs/SftpConnectDialog.java:178,199')
  $2 vs $6 assignment (which of :190-194 vs :217-227) remains OPEN pending
  bytecode/class-file order — do not guess.

### 1b. Ee1aeff93 — NOT FOUND in edge-line index, fix becomes an ADD
- Saved scratch/edge_lines.json has NO entry for Ee1aeff93 (lookup returns
  None), while it does contain E89e2cedd. The first set already caveated
  that Ee1 was not hash-matched. Consequence for the merger: print
  graph_def.py on a full checkout and confirm whether Ee1 exists at all.
  If it does not exist, there is nothing to delete — the fix is purely to
  ADD the correct edge below, and the <init> -> decompress pair should be
  recorded as "not present in current graph" rather than "deleted".
- Correct route, re-read: CompressedExplorerFragment has no explicit
  constructor (fields :82-126, first method onCreate :127), so <init>
  cannot call decompress. decompressor is assigned at :215
  (onActivityCreated, guard savedInstanceState == null &&
  compressedFile != null at :209) and at :243 (onRestoreInstanceState).
  The only decompress( call is at :329, in
  CompressedExplorerFragment$1.onActionItemClicked (:306-335), case
  R.id.ex: (:321), after building dirs from checked positions (:324-327),
  followed by mode.finish() (:331). Decompressor.java has
  decompress(String) :43 and decompress(String,String[]) :55; :329 matches
  the two-argument overload.
  Verdict: wrong as a pair (if present), otherwise missing. Proposed fix:
  add CompressedExplorerFragment$1.onActionItemClicked ->
  Decompressor.decompress(String,String[]), CALL, evidence
  SRC fragments/CompressedExplorerFragment.java:329, guard
  item.getItemId() == R.id.ex (:307,:321) with decompressor assigned
  (:215 / :243).

### 1c. GlideRequest.listener — WRONG LABEL, re-verified with fuller route
- UNREACHABLE entry index: scratch/unreach_lines.json gives
  GlideRequest.listener -> [11004, 11004] (snapshot line, merger to confirm).
- Route, re-read: RecyclerAdapter :116 field modelProvider,
  :388 modelProvider = new RecyclerPreloadModelProvider(mainFrag, uris);
  RecyclerPreloadModelProvider :26 field GlideRequest<Drawable> request,
  :30 request = GlideApp.with(fragment).asDrawable().centerCrop(),
  :43-52 getPreloadRequestBuilder returns request.load(...) (receiver type
  GlideRequest). RecyclerAdapter :899 (showThumbnailWithBackground, :856)
  and :945 (showRoundedThumbnail, :902):
  modelProvider.getPreloadRequestBuilder(iconData).listener(requestListener).into(view);
  Callers of those two methods: :595, :598, :608 (thumbnail) and :724, :733
  (rounded thumbnail), all guarded by PREFERENCE_SHOW_THUMB (:593, :607,
  :719, :732). The .listener() receiver is therefore GlideRequest at
  runtime (virtual dispatch from RequestBuilder static type).
  Verdict: wrong label. Proposed fix unchanged: remove UNREACHABLE for
  GlideRequest.listener; add the :899/:945 route with that receiver chain.

## 2. New route — GlideRequest.clone via AppsAdapterPreloadModel
- AppsAdapterPreloadModel.java: field GlideRequest<Drawable> request (:24),
  ctor :28 request = GlideApp.with(f).asDrawable().fitCenter(),
  getPreloadRequestBuilder :43-44 return request.clone().load(item).
  The .clone() receiver is GlideRequest, NOT GlideOptions — this is the
  conflation the first set warned about in label_1.md (which cited
  "request.clone()" at :44 as GlideOptions.clone).
- AppsAdapter.java:72 field AppsAdapterPreloadModel modelProvider, :81 ctor
  takes a modelProvider, :45 import — so the provider is wired into the
  apps adapter. The ListPreloader framework dispatch that calls
  getPreloadRequestBuilder is INFERRED (library, not printed FW-SRC).
- Verdict: GlideRequest.clone is REACHABLE proposed, via
  AppsAdapterPreloadModel.getPreloadRequestBuilder. GlideOptions.clone
  is a DIFFERENT method and is NOT resolved by this route — do not flip it
  on this evidence. Full GlideOptions/GlideRequest group is being judged
  by a parallel helper; this row is reported here only because it was
  found in files already printed for the first set.
- Caveat added on re-check: the saved unreach_lines.json snapshot has
  only 363 entries vs 472 UNREACHABLE in the build report, so
  GlideRequest.clone's absence from that snapshot proves NOTHING about
  its current label. The merger must check its current label/line on a
  full checkout before removing any UNREACHABLE entry for it; if it is
  already REACHABLE, only the route edge above is to be added (or
  confirmed), not a label flip.
  Proposed fix fragment:
  e('AppsAdapterPreloadModel.getPreloadRequestBuilder', 'GlideRequest.clone', 'CALL',
    'preload builder clones the GlideRequest before loading',
    evidence='SRC adapters/glide/AppsAdapterPreloadModel.java:44')
  plus removal of UNREACHABLE for GlideRequest.clone (merger to confirm
  its current label/line on a full checkout first).

## 3. New route — IconDataParcelable.setImageBroken (contradiction resolved)
- Build-report pointer only (tool coverage never evidence): setImageBroken
  is UNREACHABLE but ran in a tool run.
- Printed route, no coverage needed: RecyclerAdapter passes
  rowItem.iconData::setImageBroken as the OnImageProcessed argument at
  :596, :599, :609 (showThumbnailWithBackground callers) and :724, :733
  (showRoundedThumbnail callers). Those methods invoke
  errorListener.onImageProcessed(true) at :864, :883, :912, :930 and
  onImageProcessed(false) at :895, :941. OnImageProcessed is a functional
  interface with void onImageProcessed(boolean) (:1030), so the method
  reference is invoked on those lines. Guards: PREFERENCE_SHOW_THUMB at
  the callers above, plus iconData.isImageBroken() checks at :858/:904
  inside the thumbnail methods (those check the current broken state;
  they do not gate the callback registration).
- Verdict: IconDataParcelable.setImageBroken is REACHABLE proposed.
  Proposed fix: remove its UNREACHABLE entry; add the
  showThumbnailWithBackground / showRoundedThumbnail ->
  IconDataParcelable.setImageBroken route with evidence
  SRC adapters/RecyclerAdapter.java:596,599,609,724,733 and
  :864,883,895,912,930,941. (A parallel helper is judging the other
  non-Glide contradictions; this row is included here because it was
  found in already-printed files.)

## Counts for this second set (my routes only, not the app sample)
- Judged items: E89 (wrong, fix proposed), Ee1 (wrong/missing, fix
  proposed), GlideRequest.listener (wrong label, fix proposed),
  GlideRequest.clone (wrong label, fix proposed),
  IconDataParcelable.setImageBroken (wrong label, fix proposed) = 5 items.
- correct: 0, fixed (proposed fix, not yet merged): 5, wrong (unfixed,
  no fix): 0, unclear: 0.
- Error-rate-style fraction on judged items: (5+0)/(0+5+0) = 1.00 (5/5).
  This is an issue-first set, NOT the WP2 sample of 30 and NOT the app's
  error rate. Do not quote it as such.
- Combined with the first set, the separable proposed-fix list is now:
  delete E89e2cedd (confirm line 11617 on checkout); add lambda$null$5 ->
  GetSshHostFingerprintTask.execute; add onActionItemClicked ->
  Decompressor.decompress(String,String[]) (and confirm Ee1 presence);
  remove UNREACHABLE for GlideRequest.listener, GlideRequest.clone
  (confirm current label first — see §2 caveat), and
  IconDataParcelable.setImageBroken; add their :899/:945, :44, and
  thumbnail-callback routes respectively. Sftp $2 vs $6 remains OPEN.

## Blockers for [K] (unchanged, stated plainly)
1. Sampler: tools/verify_sample.py reads graphs/AmazeFileManager/out/methods.csv
   (1,179,770 bytes) — too large for get_file_contents, and there is no
   range/blob MCP tool. The download URL the connector returns carries a
   token that is redacted in tool output and must not be unwrapped or used.
   Without methods.csv there is no reproducible sample_30.txt, no
   verification.csv via make_verification.py, and no final WP2 table.
2. Build/C1: tools/build_graph.py needs graphs/AmazeFileManager/graph_def.py
   (1,058,622 bytes, same too-large barrier) plus auto_calls.json
   (1,839,161 bytes, same barrier). Without them no build, citation, route,
   bytecode, or scan_unreachable check can be run or claimed.
3. Full-folder Glide grep (C5) and Sftp $2/$6 bytecode order are still
   outstanding (Glide group with a parallel helper; $2/$6 needs class files).
4. Until 1-2 are resolved by a full local checkout (or an equivalent
   authorised file transfer that the parent arranges), WP2 AmazeFileManager
   cannot reach [K] (route checks DONE, awaiting user tick) honestly, even
   though the route-judging work above is complete as proposals.
   Nothing in this file should be quoted as a verified batch, a sample
   error rate, or a [K] status.
