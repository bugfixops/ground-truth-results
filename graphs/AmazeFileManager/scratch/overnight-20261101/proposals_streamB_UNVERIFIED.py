# AmazeFileManager — stream B proposals, UNVERIFIED, NOT MERGED, NOT PUSHED
# Merger (full local checkout only, branch work-2026-10-31): print the CURRENT
# graph_def.py line for every delete / UNREACHABLE removal below and confirm the
# edge / entry still exists at that line. Snapshot line numbers from prior work
# (edge_lines.json, unreach_lines.json) are POINTERS ONLY, never proof.
# Rebuild, re-print every route touched, re-draw the sample, run all eight
# checks before any merge. Nothing here has passed build / sampler / grep / C1.
# Corrections vs the prior helper-4 fold (made tonight from re-read source):
#   - AppsAdapterPreloadModel clone line is :45, not :44 (grep-verified).
#   - Sftp lambda$null$5 descriptor-order claim softened: elimination only
#     (see route_checks_consolidated.md A1); the fix itself is unchanged.

# 1. SftpConnectDialog — delete E89e2cedd (confirm on checkout), add:
e('SftpConnectDialog.lambda$null$5', 'GetSshHostFingerprintTask.execute', 'CALL',
  'removeConnection callback creates and executes fingerprint task',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:178,199')
# Guard: !isEmpty(sshHostKey) (SftpConnectDialog.java:175).
# Sftp $2 vs $6 stays OPEN pending bytecode/class-file order — do not assign.

# 2. CompressedExplorerFragment — delete Ee1aeff93 ONLY if the checkout confirms
#    it exists (prior snapshot: absent); in either case add:
e('CompressedExplorerFragment$1.onActionItemClicked', 'Decompressor.decompress(String,String[])', 'CALL',
  'extract menu item decompresses checked entries',
  evidence='SRC fragments/CompressedExplorerFragment.java:329')
# Guard: item.getItemId() == R.id.ex (:307, :321); decompressor assigned :215 / :243.

# 3. GlideRequest.listener — remove its UNREACHABLE entry (confirm on checkout), add:
e('RecyclerAdapter.showThumbnailWithBackground', 'GlideRequest.listener', 'CALL',
  'thumbnail builder listener, receiver is GlideRequest via preload provider',
  evidence='SRC adapters/RecyclerAdapter.java:899')
e('RecyclerAdapter.showRoundedThumbnail', 'GlideRequest.listener', 'CALL',
  'rounded thumbnail builder listener, receiver is GlideRequest via preload provider',
  evidence='SRC adapters/RecyclerAdapter.java:945')

# 4. GlideRequest.clone — remove its UNREACHABLE entry ONLY if the checkout
#    confirms its current label is UNREACHABLE; in either case add/confirm:
e('AppsAdapterPreloadModel.getPreloadRequestBuilder', 'GlideRequest.clone', 'CALL',
  'preload builder clones the GlideRequest before loading',
  evidence='SRC adapters/glide/AppsAdapterPreloadModel.java:45')
# Do NOT flip GlideOptions.clone on this evidence — different method.

# 5. IconDataParcelable.setImageBroken — remove its UNREACHABLE entry, add:
e('RecyclerAdapter.showThumbnailWithBackground', 'IconDataParcelable.setImageBroken', 'CALL',
  'thumbnail callback invokes setImageBroken via OnImageProcessed',
  evidence='SRC adapters/RecyclerAdapter.java:596,599,609,864,883,895')
e('RecyclerAdapter.showRoundedThumbnail', 'IconDataParcelable.setImageBroken', 'CALL',
  'rounded thumbnail callback invokes setImageBroken via OnImageProcessed',
  evidence='SRC adapters/RecyclerAdapter.java:724,733,912,930,941')
# NOTE: :912, :930, :941 are prior-report citations, NOT re-read tonight;
# the merger must confirm them on checkout before applying this edge.

# 6. GlideRequests.as — INFERRED delegation step ONLY. Add only with the
#    INFERRED basis recorded; HOLD if the merger requires SOURCE-only edges
#    until build-generated GlideRequests.java is printed confirming
#    asDrawable() { return as(Drawable.class); }.
e('GlideRequests.asDrawable', 'GlideRequests.as', 'CALL',
  'generated asDrawable delegates to as(Class)',
  evidence='INFERRED generated GlideRequests.java; anchors SRC adapters/glide/RecyclerPreloadModelProvider.java:30, adapters/glide/AppsAdapterPreloadModel.java:28')

# Section B (prior WP2 proposals, carried unchanged except as noted; the merger
# must print each cited line on checkout — none was re-read tonight):
#  - LayoutElementParcelable.writeToParcel: remove UNREACHABLE; add
#    MainFragment.onSaveInstanceState -> writeToParcel (FRAMEWORK; marshalling
#    INFERRED), evidence SRC fragments/MainFragment.java:397,402,415.
#  - RoundedImageView.setBackgroundColor: remove UNREACHABLE; add
#    onBindViewHolder -> setBackgroundColor (:716, :742, :744) and
#    showRoundedThumbnail -> setBackgroundColor (:905, :908, :916, :925, :940),
#    grid branch + PREFERENCE_USE_CIRCULAR_IMAGES only.
#  - SimpleTextWatcher.beforeTextChanged / onTextChanged: remove UNREACHABLE;
#    add RenameBookmark.onCreateDialog -> beforeTextChanged / onTextChanged
#    (FRAMEWORK; TextView dispatch INFERRED),
#    evidence SRC ui/dialogs/RenameBookmark.java:86-93,112-119.
#  - OPEN (no fix): 13 Glide methods (see consolidated report A7),
#    SimpleTextWatcher.afterTextChanged, TextEditorActivity.<init> (ENV gate),
#    Sftp $2 vs $6 assignment.
