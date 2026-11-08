# UNVERIFIED PROPOSAL — has NOT passed build, sampler, full-repo grep, or C1 checks; re-check from printed source before relying/merging.

# WP2 AmazeFileManager — FOLDED merge-ready fix file, UNVERIFIED, NOT MERGED
# ============================================================================
# Status: PROPOSAL ONLY. Nothing here has been applied to graph_def.py, no
# label has been flipped, no build / sampler / grep / C1 check has been run
# on this file, and nothing here has been pushed. This file FOLDS, into one
# place, every fix fragment from:
#   - first set  : WP2_AmazeFileManager_first_set_route_checks.md
#   - second set : WP2_Amaze_second_set_my_routes.md (and the earlier
#                  WP2_Amaze_merge_ready_fixes_UNVERIFIED.py, which covered
#                  ONLY first/second-set fixes)
#   - non-Glide  : WP2_Amaze_NonGlide_contradictions.md
#   - Glide group: WP2_Amaze_Glide_group.md
# No fix has been added that is not in one of those four reports. Items
# marked OPEN below are NOT fixes: they are left exactly as the reports
# left them, with the resolver the report named.
#
# Merger rules (full local checkout only, branch work-2026-10-31):
#   1. Print the CURRENT graph_def.py line for every delete / UNREACHABLE
#      removal below and confirm the edge / entry still exists at that
#      line. Snapshot line numbers below come from scratch/edge_lines.json
#      (7,993 edges) and scratch/unreach_lines.json (363 entries vs 472
#      UNREACHABLE in build_report.txt) and are POINTERS ONLY, never proof.
#   2. Apply only the items marked "proposed" (and, for conditional items,
#      only the branch whose precondition the checkout confirms).
#   3. Rebuild (tools/build_graph.py), re-print every route touched,
#      re-draw the sample, and run all eight checks before any merge.
#   4. Never present this file, or any item in it, as verified or merged.
#
# Repo: bugfixops/ground-truth-results, branch work-2026-10-31 only.
# Baseline (re-checked in the reports, not re-derived here): 2981 methods,
# 2509 REACHABLE / 472 UNREACHABLE, errors 0, warnings 0, no verification.csv.
# Source root for every SRC citation: final_java_only/AmazeFileManager/
# app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/
# Edge syntax below is graph_def.py e(...) style, as in the earlier merge
# file. Conform node names / kind spelling to graph_def.py's actual
# convention on checkout; do not change src, dst, evidence, or guard
# while conforming.
#
# Folded totals: 10 label/edge-removal proposals (2 of them conditional:
#   Ee1aeff93 delete, GlideRequest.clone UNREACHABLE removal),
#   18 e(...) edge proposals in total (15 in FIX 1-10, of which 2 in FIX 5
#   are the onBindViewHolder -> show* supporting edges, plus 3 deduplicated
#   supporting edges in the SUPPORTING section, all "add only if missing"
#   where so marked), 15 OPEN methods with NO fix (13 Glide +
#   SimpleTextWatcher.afterTextChanged + TextEditorActivity.<init>),
#   plus 1 OPEN edge assignment (Sftp $2 vs $6).

# ---------------------------------------------------------------------------
# FIX 1. SftpConnectDialog — wrong edge E89e2cedd
# Status: proposed (delete + add). The $2 vs $6 assignment is still OPEN.
# Edge id: E89e2cedd (snapshot graph_def.py line 11617, edge_lines.json;
#   confirm on checkout; id was hash-matched against parts/repair_rp02.py
#   in the first set, so re-confirm if that edge's text was edited since).
# DELETE:
#   SftpConnectDialog.lambda$null$2 -> GetSshHostFingerprintTask.execute
#   (claimed trigger "lambda executes GetSshHostFingerprintTask", evidence
#   SRC SftpConnectDialog.java:198 — wrong source AND one line off: :198
#   is the closing brace of if (hostKey != null) {, .execute() is :199.
#   lambda$null$2's descriptor ends (DialogInterface, int): it is a dialog
#   button handler, not a Runnable / task callback.)
# ADD:
e('SftpConnectDialog.lambda$null$5', 'GetSshHostFingerprintTask.execute', 'CALL',
  'removeConnection callback creates and executes fingerprint task',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:178,199')
# Guard: !isEmpty(sshHostKey) (SftpConnectDialog.java:175). Route head:
#   onCreateDialog :160 onPositive handler (lambda$onCreateDialog$9) ->
#   :175 guard -> :176-177 SshConnectionPool.removeConnection(..., Runnable)
#   -> SshConnectionPool.java:94-95 AsyncRemoveConnection executes ->
#   :301-303 onPostExecute callback.run() if non-null (AsyncTask dispatch
#   INFERRED) -> lambda$null$5 body -> :178/:199 task execute.
#   lambda$null$5 is the only candidate whose descriptor matches the
#   removeConnection Runnable's 7 captures exactly
#   (String, String, int, String, String, String, boolean).
# STILL OPEN — do NOT guess: which of lambda$null$2 / lambda$null$6 is the
#   :190-194 handler vs the :217-227 handler. Their descriptors are
#   identical; assignment needs bytecode / class-file lambda order.
#   (Both, as a pair, go to SftpConnectDialog.authenticateAndSaveSetup
#   (:191-194 and :220-222); only the :217-227 one also dismisses/logs
#   (:219, :223-225).)
# CAUTION (first set, not a new edge): do NOT trust repair_rp02.py's other
#   lambda$null$* guesses blindly — it also swaps lambda$onCreateDialog$0
#   (port-focus listener, :132-134) with $9 (onPositive handler, :160-231).
#   Re-derive that subgraph from method_list.json descriptors on checkout.

# ---------------------------------------------------------------------------
# FIX 2. CompressedExplorerFragment — wrong / missing edge Ee1aeff93
# Status: proposed (add; delete ONLY if the edge is confirmed present).
# Edge id: Ee1aeff93 — CONFIRM EXISTENCE FIRST. Saved edge_lines.json has
#   NO entry for Ee1aeff93 (lookup returns None), while it does contain
#   E89e2cedd. If it is absent from current graph_def.py there is nothing
#   to delete: record the <init> -> decompress pair as "not present in
#   current graph", not as "deleted".
# DELETE (conditional, only if confirmed present on checkout):
#   CompressedExplorerFragment.<init> -> Decompressor.decompress
#   (wrong: the fragment has no explicit constructor — fields :82-126,
#   first method onCreate :127 — so <init> calls nothing named decompress;
#   the bare target name is also ambiguous between the two overloads.)
# ADD:
e('CompressedExplorerFragment$1.onActionItemClicked', 'Decompressor.decompress(String,String[])', 'CALL',
  'extract menu item decompresses checked entries',
  evidence='SRC fragments/CompressedExplorerFragment.java:329')
# Guard: item.getItemId() == R.id.ex (:307, :321), with decompressor
#   assigned (:215 onActivityCreated, guarded savedInstanceState == null
#   && compressedFile != null at :209; :243 onRestoreInstanceState).
#   Decompressor.java: decompress(String) :43, decompress(String,String[])
#   :55 — the :329 call matches the two-argument overload.
#   Action-mode start (mActionModeCallback :247, R.id.ex shown :277) is
#   framework/standard, INFERRED, not FW-SRC.

# ---------------------------------------------------------------------------
# FIX 3. GlideRequest.listener — wrong label UNREACHABLE -> REACHABLE
# Status: proposed (remove UNREACHABLE entry + add edges).
# Method descriptor: listener (Lcom/bumptech/glide/request/RequestListener;)
#   Lcom/amaze/filemanager/GlideRequest;
# REMOVE UNREACHABLE entry (snapshot graph_def.py line 11004, unreach_lines
#   [11004, 11004]; confirm label + line on checkout first).
# ADD:
e('RecyclerAdapter.showThumbnailWithBackground', 'GlideRequest.listener', 'CALL',
  'thumbnail builder listener, receiver is GlideRequest via preload provider',
  evidence='SRC adapters/RecyclerAdapter.java:899')
e('RecyclerAdapter.showRoundedThumbnail', 'GlideRequest.listener', 'CALL',
  'rounded thumbnail builder listener, receiver is GlideRequest via preload provider',
  evidence='SRC adapters/RecyclerAdapter.java:945')
# Guards: PREFERENCE_SHOW_THUMB at the callers (:593, :607, :719, :732).
# Receiver chain (SOURCE): RecyclerAdapter :116 modelProvider field, :388
#   modelProvider = new RecyclerPreloadModelProvider(mainFrag, uris);
#   RecyclerPreloadModelProvider :26 GlideRequest<Drawable> request field,
#   :30 request = GlideApp.with(fragment).asDrawable().centerCrop(),
#   :43-52 getPreloadRequestBuilder returns request.load(...) — so the
#   .listener() receiver at :899/:945 is a GlideRequest at runtime
#   (virtual dispatch from the RequestBuilder static type).
# SUPPORTING edges — see the deduplicated SUPPORTING section below (each
#   edge once, add ONLY if missing). The onBindViewHolder -> show* edges
#   are already given as code in FIX 5 (method-reference evidence) and are
#   NOT repeated here. onBindViewHolder dispatch itself is framework
#   dispatch, INFERRED.

# ---------------------------------------------------------------------------
# FIX 4. GlideRequest.clone — REACHABLE proposed, via AppsAdapterPreloadModel
# Status: proposed (add edge; UNREACHABLE removal CONDITIONAL — see caveat).
# Method descriptor: clone ()Lcom/amaze/filemanager/GlideRequest;
# CAVEAT (second set, binding): the saved unreach_lines.json snapshot has
#   only 363 entries vs 472 UNREACHABLE in build_report.txt, and
#   GlideRequest.clone is ABSENT from that snapshot. Absence proves
#   NOTHING about its current label. The merger MUST check its current
#   label / line on a full checkout BEFORE removing any UNREACHABLE entry
#   for it. If it is already REACHABLE, only add / confirm the edge below.
# REMOVE UNREACHABLE entry (CONDITIONAL on the checkout confirming the
#   current label is UNREACHABLE; no snapshot line number exists for it).
# ADD:
e('AppsAdapterPreloadModel.getPreloadRequestBuilder', 'GlideRequest.clone', 'CALL',
  'preload builder clones the GlideRequest before loading',
  evidence='SRC adapters/glide/AppsAdapterPreloadModel.java:44')
# Receiver proof: AppsAdapterPreloadModel :24 field GlideRequest<Drawable>
#   request, :28 request = GlideApp.with(f).asDrawable().fitCenter(),
#   :43-44 return request.clone().load(item). The .clone() receiver is
#   GlideRequest, NOT GlideOptions.
# Do NOT flip GlideOptions.clone on this evidence — different method
# (see OPEN item 13d below). ListPreloader dispatch that calls
# getPreloadRequestBuilder is library dispatch, INFERRED.

# ---------------------------------------------------------------------------
# FIX 5. IconDataParcelable.setImageBroken — wrong label -> REACHABLE
# Status: proposed (remove UNREACHABLE entry + add edges).
# Method descriptor: setImageBroken (Z)V.
# REMOVE UNREACHABLE entry (snapshot graph_def.py line 14064, unreach_lines
#   [14064, 14064]; confirm label + line on checkout first).
# ADD (method-reference resolution; non-Glide report §1 + second set §3):
e('RecyclerAdapter.showThumbnailWithBackground', 'IconDataParcelable.setImageBroken', 'CALL',
  'errorListener.onImageProcessed(...) invokes the method reference passed at the call site',
  evidence='SRC adapters/RecyclerAdapter.java:864, 883, 895')
e('RecyclerAdapter.showRoundedThumbnail', 'IconDataParcelable.setImageBroken', 'CALL',
  'errorListener.onImageProcessed(...) invokes the method reference passed at the call site',
  evidence='SRC adapters/RecyclerAdapter.java:912, 930, 941')
# SUPPORTING edges — add ONLY if missing (the method-reference call sites):
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.showThumbnailWithBackground', 'CALL',
  'list bind passes iconData::setImageBroken as OnImageProcessed',
  evidence='SRC adapters/RecyclerAdapter.java:595-596, 598-599, 608-609')
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.showRoundedThumbnail', 'CALL',
  'grid bind passes iconData::setImageBroken as OnImageProcessed',
  evidence='SRC adapters/RecyclerAdapter.java:724, 733')
# Why: OnImageProcessed is a functional interface with void
#   onImageProcessed(boolean) (:1029-1031), matching setImageBroken (Z)V
#   exactly, so rowItem.iconData::setImageBroken is invoked by the
#   errorListener.onImageProcessed(...) calls above (:864 already-broken,
#   :883 onLoadFailed, :895 onResourceReady-false; :912, :930, :941 same
#   pattern in the rounded method). Guards: PREFERENCE_SHOW_THUMB at the
#   callers; iconData.isImageBroken() checks at :858/:904 check current
#   state and do not gate callback registration. onBindViewHolder head is
#   RecyclerView dispatch, INFERRED.

# ---------------------------------------------------------------------------
# FIX 6. LayoutElementParcelable.writeToParcel — wrong label -> REACHABLE
# Status: proposed (remove UNREACHABLE entry + add edge).
# Method descriptor: writeToParcel (Landroid/os/Parcel;I)V.
# REMOVE UNREACHABLE entry (snapshot graph_def.py line 11155, unreach_lines
#   [11155, 11155]; confirm label + line on checkout first).
# ADD:
e('MainFragment.onSaveInstanceState', 'LayoutElementParcelable.writeToParcel', 'FRAMEWORK',
  'outState.putParcelableArrayList("list", LIST_ELEMENTS); Bundle marshalling calls writeToParcel on each element when the saved-state Bundle is written to a Parcel',
  evidence='SRC fragments/MainFragment.java:397, 402, 415; LIST_ELEMENTS is ArrayList<LayoutElementParcelable> at :153')
# Guard: listView != null (MainFragment.java:402); the parcel-list line is
#   :415 outState.putParcelableArrayList("list", LIST_ELEMENTS).
#   putParcelableArrayList stores the objects; writeToParcel runs when the
#   saved-state Bundle is actually written to a Parcel by the framework
#   (FragmentManager / activity state save) — that marshalling step and
#   the onSaveInstanceState lifecycle dispatch are INFERRED here (no
#   fw_src line printed). If the merger's convention uses CALL rather
#   than FRAMEWORK for Bundle-marshalling edges, keep src/dst/evidence
#   and change only the kind, still recording marshalling as INFERRED.
#   Side note, not a separate verdict: writeToParcel's writeParcelable
#   (iconData, 0) also parcels each element's IconDataParcelable.

# ---------------------------------------------------------------------------
# FIX 7. RoundedImageView.setBackgroundColor — wrong label -> REACHABLE
# Status: proposed (remove UNREACHABLE entry + add edges). GRID BRANCH ONLY.
# Method descriptor: setBackgroundColor (I)V. Override in
#   ui/views/RoundedImageView.java: recolours its own Paint field, does
#   NOT call super.setBackgroundColor(color).
# REMOVE UNREACHABLE entry (snapshot graph_def.py line 13206, unreach_lines
#   [13206, 13206]; confirm label + line on checkout first).
# ADD:
e('RecyclerAdapter.onBindViewHolder', 'RoundedImageView.setBackgroundColor', 'CALL',
  'grid branch: iconBackground is holder.genericIcon when PREFERENCE_USE_CIRCULAR_IMAGES, and genericIcon is a RoundedImageView (cast at :716); virtual dispatch reaches the override',
  evidence='SRC adapters/RecyclerAdapter.java:716, 742, 744')
e('RecyclerAdapter.showRoundedThumbnail', 'RoundedImageView.setBackgroundColor', 'CALL',
  'iconBackground is viewHolder.genericIcon when PREFERENCE_USE_CIRCULAR_IMAGES; virtual dispatch reaches the override',
  evidence='SRC adapters/RecyclerAdapter.java:905, 908, 916, 925, 940')
# Guard (BOTH edges): grid view AND PREFERENCE_USE_CIRCULAR_IMAGES true.
#   Proof: ItemViewHolder declares genericIcon as ImageView, but
#   RecyclerAdapter :716 casts ((RoundedImageView) holder.genericIcon)
#   unconditionally in the grid branch, so genericIcon IS a
#   RoundedImageView at runtime in grid layout (else every grid bind
#   would throw ClassCastException); :742 (onBindViewHolder) and :905/:916
#   (showRoundedThumbnail) select iconBackground = genericIcon when the
#   preference is on, iconLayout (RelativeLayout) when off; :744 and
#   :908/:925/:940 are the setBackgroundColor calls on that selection.
#   onBindViewHolder head is RecyclerView dispatch, INFERRED.
# DELIBERATELY NOT CITED: RecyclerAdapter :723
#   holder.imageView1.setBackgroundColor(Color.BLACK) — imageView1 is
#   statically ImageView and its runtime type cannot be determined from
#   Java source alone (layout XML is not in final_java_only); it may or
#   may not reach this override. The non-circular branch (iconLayout)
#   resolves to View.setBackgroundColor, NOT this override.

# ---------------------------------------------------------------------------
# FIX 8. SimpleTextWatcher.beforeTextChanged — wrong label -> REACHABLE
# Status: proposed (remove UNREACHABLE entry + add edge).
# Method descriptor: beforeTextChanged (Ljava/lang/CharSequence;III)V.
#   Base method in utils/SimpleTextWatcher.java is empty; that does not
#   stop it executing — dispatch resolves to the base method when no
#   override exists.
# REMOVE UNREACHABLE entry (snapshot graph_def.py lines 14477-14479,
#   unreach_lines; confirm label + lines on checkout first).
# ADD:
e('RenameBookmark.onCreateDialog', 'SimpleTextWatcher.beforeTextChanged', 'FRAMEWORK',
  'anonymous SimpleTextWatcher registered on conName/ip overrides only afterTextChanged, so TextView dispatch calls the base beforeTextChanged',
  evidence='SRC ui/dialogs/RenameBookmark.java:86-93, 112-119')
# Route: RenameBookmark :86-93 (conName) and :112-119 (ip) register
#   anonymous SimpleTextWatcher subclasses overriding ONLY afterTextChanged
#   (method_list.json: RenameBookmark$1 / $2 list only <init> and
#   afterTextChanged); TextView dispatch on text change calls all three
#   watcher callbacks (INFERRED standard dispatch, no fw_src line printed),
#   so beforeTextChanged resolves to the base method. Dialog-show head
#   (who shows RenameBookmark) was not printed — INFERRED, not a reason
#   to doubt the registration + non-override facts, which are SOURCE.

# ---------------------------------------------------------------------------
# FIX 9. SimpleTextWatcher.onTextChanged — wrong label -> REACHABLE
# Status: proposed (remove UNREACHABLE entry + add edge).
# Method descriptor: onTextChanged (Ljava/lang/CharSequence;III)V.
# REMOVE UNREACHABLE entry (snapshot graph_def.py lines 14481-14483,
#   unreach_lines; confirm label + lines on checkout first).
# ADD:
e('RenameBookmark.onCreateDialog', 'SimpleTextWatcher.onTextChanged', 'FRAMEWORK',
  'anonymous SimpleTextWatcher registered on conName/ip overrides only afterTextChanged, so TextView dispatch calls the base onTextChanged',
  evidence='SRC ui/dialogs/RenameBookmark.java:86-93, 112-119')
# Identical reasoning to FIX 8, same sites. If the merger's convention
# uses CALL rather than FRAMEWORK for TextView-dispatch edges, keep
# src/dst/evidence and change only the kind, still recording dispatch
# as INFERRED.

# ---------------------------------------------------------------------------
# FIX 10. GlideRequests.as — REACHABLE proposed, INFERRED delegation step
# Status: proposed WITH A HOLD FLAG (see below). Do not apply silently.
# Method descriptor: as (Ljava/lang/Class;)Lcom/amaze/filemanager/GlideRequest;
# REMOVE UNREACHABLE entry (snapshot graph_def.py line 11014, unreach_lines
#   [11014, 11014]; confirm label + line on checkout first).
# ADD (INFERRED delegation step — the generated file was NOT printed):
e('GlideRequests.asDrawable', 'GlideRequests.as', 'CALL',
  'INFERRED: generated asDrawable() delegates as(Drawable.class); anchored by printed asDrawable call sites below',
  evidence='SRC adapters/glide/RecyclerPreloadModelProvider.java:30, adapters/glide/AppsAdapterPreloadModel.java:28')
# Anchors (SOURCE): RecyclerPreloadModelProvider :30
#   GlideApp.with(fragment).asDrawable() and AppsAdapterPreloadModel :28
#   GlideApp.with(f).asDrawable() — receivers are the GlideRequests objects
#   returned by GlideApp.with(...). In Glide's generated API, asDrawable()
#   is implemented as as(Drawable.class).
# HOLD-FOR-SOURCE FLAG: if the merger requires SOURCE-only edges, DO NOT
#   apply this block yet. Instead run resolver R-as first: print
#   build-generated GlideRequests.java (NOT in final_java_only — generated
#   at build time, not in the app source tree) and confirm
#   asDrawable() { return as(Drawable.class); }. Until then this fix
#   stays INFERRED, and the method stays OPEN under a SOURCE-only rule.
#   The .load(...) sites are NOT claimed as as-routes: whether generated
#   load delegates through asDrawable was not printed and is not asserted.
# SUPPORTING edges — see the deduplicated SUPPORTING section below (each
#   edge once, add ONLY if missing).

# ---------------------------------------------------------------------------
# SUPPORTING EDGES — deduplicated, add ONLY if missing (not in FIX 1-10
# above, and NOT duplicated between FIX 3 and FIX 10).
# Status: proposed, add-only-if-missing. The onBindViewHolder ->
# showThumbnailWithBackground / showRoundedThumbnail edges are NOT repeated
# here: they are already given as code in FIX 5.
e('RecyclerAdapter.setItems', 'RecyclerPreloadModelProvider.<init>', 'CALL',
  'setItems constructs the preload model provider',
  evidence='SRC adapters/RecyclerAdapter.java:388')
e('RecyclerPreloadModelProvider.<init>', 'GlideRequests.asDrawable', 'CALL',
  'provider init calls GlideApp.with(fragment).asDrawable()',
  evidence='SRC adapters/glide/RecyclerPreloadModelProvider.java:30')
e('AppsAdapterPreloadModel.<init>', 'GlideRequests.asDrawable', 'CALL',
  'provider init calls GlideApp.with(f).asDrawable()',
  evidence='SRC adapters/glide/AppsAdapterPreloadModel.java:28')

# ============================================================================
# OPEN — NO FIX. Do NOT flip, do NOT add an edge for any item below.
# ============================================================================

# OPEN 1. SimpleTextWatcher.afterTextChanged (Landroid/text/Editable;)V
#   — NO label fix. Snapshot unreach lines 15928-15933 (confirm on
#   checkout if needed, but do NOT merge as verified). Reason: the two
#   printed RenameBookmark watchers override afterTextChanged WITHOUT a
#   super call (RenameBookmark.java:88-92), so dispatch on those instances
#   never reaches the base method. The base runs only for a registered
#   watcher that does not override afterTextChanged, or an override
#   elsewhere that calls super.afterTextChanged(...); no such site was
#   printed. CONDITIONAL HYGIENE NOTE (verify on checkout): IF the graph
#   contains an edge RenameBookmark$1.afterTextChanged ->
#   SimpleTextWatcher.afterTextChanged, that edge is unsupported on
#   printed source (no super call) and should be deleted — deleting it
#   does NOT settle the label; the label stays OPEN.
#   Resolver: full-repo grep (local checkout) for SimpleTextWatcher
#   registrations / extends SimpleTextWatcher + addTextChangedListener
#   sites, checking each subclass's override set and any
#   super.afterTextChanged call; or a printed plain-SimpleTextWatcher
#   registration site. Tool coverage alone must NOT flip it.

# OPEN 2. TextEditorActivity.<init> ()V
#   — NO label fix, NO gate correction. Current label per build report:
#   REACHABLE, ENV-gated but ran (not a contradiction entry; no entry in
#   unreach_lines.json, consistent with that). Reason: the activity file
#   itself (activities/TextEditorActivity.java, printed in full) declares
#   NO constructor (implicit default <init>, implicit super() to
#   ThemedActivity) and contains NO ENV gate, permission check, or
#   instantiation condition — onCreate branches only on theme, SDK_INT,
#   and Intent data. The ENV gate's text and edge live in graph_def.py,
#   which was not printed. Resolver (local checkout): (1) print the
#   graph_def.py edges into TextEditorActivity.<init> and identify the
#   ENV edge + exact ENV text; (2) print the manifest entry and the
#   FileUtils.openFile / openunknown body that builds the launch Intent
#   (MainFragment.onListItemClicked :851 -> :933 openFile is only the
#   partial printed path); (3) check whether the ENV condition was
#   actually satisfied in the tool run's environment. Until then the
#   ENV-gate question stays OPEN. Do NOT change the label on coverage.

# OPEN 3. Glide contradiction group — 13 methods, NO fix, NO edge.
#   All 13 were labelled UNREACHABLE but are OPEN (not UNREACHABLE):
#   the whole source tree was NOT printed, so no UNREACHABLE verdict is
#   licensed, and tool coverage is a pointer only, never evidence.
#   3a. GlideOptions.<init> ()V — OPEN. No new GlideOptions(), no
#       GlideOptions reference in any printed file. Plausible route only
#       via unprinted generated code.
#   3b. GlideOptions.apply (BaseRequestOptions;)GlideOptions — OPEN.
#       Zero .apply( calls on any receiver in the printed corpus.
#       label_1.md's "AppsAdapterPreloadModel :28" claim is wrong: :28
#       contains no .apply( (it is asDrawable().fitCenter()).
#   3c. GlideOptions.autoClone ()GlideOptions — OPEN. No printed call
#       site or caller; hypothesis only (generated chaining).
#   3d. GlideOptions.clone ()GlideOptions — OPEN. NOT the .clone() at
#       AppsAdapterPreloadModel.java:44 — that receiver is declared
#       GlideRequest<Drawable> (:24), so it is GlideRequest.clone
#       (FIX 4), a different method. Do NOT add any edge for
#       GlideOptions.clone from getPreloadRequestBuilder.
#   3e. GlideOptions.lock ()GlideOptions — OPEN. No printed call site;
#       hypothesis only (library locks the request's options object).
#   3f. GlideRequest.addListener (RequestListener;)GlideRequest — OPEN.
#       No .addListener( on any Glide receiver printed; RecyclerAdapter
#       uses .listener(...) (:899, :945), never .addListener(...). A
#       RequestListener implementation is not an addListener call.
#   3g. GlideRequest.apply (BaseRequestOptions;)GlideRequest — OPEN.
#       Zero .apply( calls in the printed corpus.
#   3h. GlideRequest.downsample (DownsampleStrategy;)GlideRequest — OPEN.
#       Zero .downsample( in the printed corpus.
#   3i. GlideRequest.optionalCenterInside ()GlideRequest — OPEN. Zero
#       occurrences printed; code calls centerCrop() / fitCenter()
#       (non-optional variants) only.
#   3j. GlideRequest.optionalFitCenter ()GlideRequest — OPEN. Same as 3i.
#   3k. GlideRequest.set (Option,Object;)GlideRequest — OPEN. No call
#       site identified; a bare .set( grep was deliberately NOT run
#       (non-specific). Needs a receiver-typed grep (GlideRequest
#       receiver + com.bumptech.glide.load.Option first argument).
#   3l. GlideRequest.transform (Transformation;)GlideRequest — OPEN.
#       Zero .transform( calls printed ("transform" in RecyclerAdapter
#       is only a code comment). Only the single-Transformation overload
#       is judged here; other overloads are separate methods.
#   3m. GlideRequests.setRequestOptions (RequestOptions;)V — OPEN. No
#       printed call site or caller; hypothesis only (generated
#       override wrapping non-GlideOptions arguments).
#   Resolvers (cheapest first, all need a checkout / generated source):
#   R-as / R-setRequestOptions / R-options-init: print build-generated
#     GlideRequests.java (not in final_java_only; look in build/generated
#     outputs for this app's Glide version). Settles 3a, 3b, FIX 10's
#     SOURCE status, and 3m.
#   R-request: print build-generated GlideRequest.java; check which of
#     apply / addListener / downsample / optionalCenterInside /
#     optionalFitCenter / set / transform are invoked from
#     app-reachable generated code (definition alone is not reachability).
#   R-tree: receiver-typed grep over the unprinted dirs (activities/
#     DatabaseViewerActivity, TextEditorActivity, PreferencesActivity,
#     activities/superclasses/*, fragments/preference_fragments/*,
#     ui/*, adapters/data/*, adapters/holders/*, filesystem/*,
#     asynchronous/*, database/*, exceptions/*, utils/* other than
#     GlideConstants.java and utils/glide/*) for .addListener(, .apply(,
#     .downsample(, .transform(, optionalCenterInside, optionalFitCenter,
#     GlideOptions, and .set( with a GlideRequest receiver + Option
#     argument. A bare-name grep (old glide_method_grep.txt style) must
#     NOT be used as evidence — it hits e.g. SharedPreferences.Editor
#     .apply() and URLDecoder.decode.
#   R-lib: obtain the Glide library source for the app's Glide version
#     (NOT in fw_src, which contains only android-8.1.0_r1) and check
#     whether library request-building calls lock() / clone() /
#     autoClone() on the request's options object, and whether a
#     GlideRequest's options object is a GlideOptions at runtime.
#     Needed for 3c, 3d, 3e only.
#   Also corrected (Glide report §5): label_1.md's Glide reasons do not
#   survive a receiver-typed re-check — GlideApp.with() returns
#   GlideRequests, not GlideOptions; "Glide framework calls it" is
#   INFERRED, not a printed route; and a method description ("sets
#   default options") is not a call site.

# ---------------------------------------------------------------------------
# END OF FOLDED FILE. Reminder: UNVERIFIED, NOT MERGED, NOT PUSHED.
# The merger applies NOTHING from here without a full local checkout,
# current-line prints, a rebuild, re-printed routes, and all eight checks.
