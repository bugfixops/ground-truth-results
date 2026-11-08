# UNVERIFIED PROPOSAL — has NOT passed build, sampler, full-repo grep, or C1 checks; re-check from printed source before relying/merging.

# WP2 AmazeFileManager — merge-ready fix fragments, UNVERIFIED, DO NOT APPLY BLINDLY
# Merger (full checkout only): print current graph_def.py lines for each
# item below, confirm the edge/UNREACHABLE entry still exists at that line,
# apply, rebuild, re-print the routes, run all eight checks, then draw the
# sampler again. Nothing here has passed build/sampler/grep/C1.
# Sources: first set (WP2_AmazeFileManager_first_set_route_checks.md) +
# second set (WP2_Amaze_second_set_my_routes.md). Glide / non-Glide helper
# reports, when delivered, are separate files and are NOT yet folded in here.

# 1. SftpConnectDialog — delete E89e2cedd (snapshot line 11617 in
#    scratch/edge_lines.json; confirm on checkout), add the correct edge:
e('SftpConnectDialog.lambda$null$5', 'GetSshHostFingerprintTask.execute', 'CALL',
  'removeConnection callback creates and executes fingerprint task',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:178,199')
# Guard for the above, per graph_def.py guard syntax in use for this app:
#   guard '!isEmpty(sshHostKey)' (SftpConnectDialog.java:175)
# Sftp $2 vs $6 (dialog-button handlers :190-194 vs :217-227) stays OPEN
# pending bytecode/class-file order — do NOT assign by guess.

# 2. CompressedExplorerFragment — confirm Ee1aeff93 presence first.
#    If absent from current graph_def.py, skip the delete and only add:
e('CompressedExplorerFragment$1.onActionItemClicked', 'Decompressor.decompress(String,String[])', 'CALL',
  'extract menu item decompresses checked entries',
  evidence='SRC fragments/CompressedExplorerFragment.java:329')
# Guard: item.getItemId() == R.id.ex (:307,:321), decompressor assigned
# (:215 onActivityCreated / :243 onRestoreInstanceState).

# 3. GlideRequest.listener — remove its UNREACHABLE entry (snapshot line
#    11004 in scratch/unreach_lines.json; confirm on checkout), add:
e('RecyclerAdapter.showThumbnailWithBackground', 'GlideRequest.listener', 'CALL',
  'thumbnail builder listener, receiver is GlideRequest via preload provider',
  evidence='SRC adapters/RecyclerAdapter.java:899')
e('RecyclerAdapter.showRoundedThumbnail', 'GlideRequest.listener', 'CALL',
  'rounded thumbnail builder listener, receiver is GlideRequest via preload provider',
  evidence='SRC adapters/RecyclerAdapter.java:945')
# Guards: PREFERENCE_SHOW_THUMB at the callers (:593,:607,:719,:732).

# 4. GlideRequest.clone — remove its UNREACHABLE entry ONLY if the current
#    label on checkout is UNREACHABLE (it is absent from the 363-entry
#    unreach snapshot, which covers only 363/472 UNREACHABLE, so absence
#    proves nothing), otherwise only add/confirm the edge below:
e('AppsAdapterPreloadModel.getPreloadRequestBuilder', 'GlideRequest.clone', 'CALL',
  'preload builder clones the GlideRequest before loading',
  evidence='SRC adapters/glide/AppsAdapterPreloadModel.java:44')
# Do NOT flip GlideOptions.clone on this evidence — different method.

# 5. IconDataParcelable.setImageBroken — remove its UNREACHABLE entry
#    (confirm label/line on checkout first), add:
e('RecyclerAdapter.showThumbnailWithBackground', 'IconDataParcelable.setImageBroken', 'CALL',
  'thumbnail callback invokes setImageBroken via OnImageProcessed',
  evidence='SRC adapters/RecyclerAdapter.java:596,599,609,864,883,895')
e('RecyclerAdapter.showRoundedThumbnail', 'IconDataParcelable.setImageBroken', 'CALL',
  'rounded thumbnail callback invokes setImageBroken via OnImageProcessed',
  evidence='SRC adapters/RecyclerAdapter.java:724,733,912,930,941')
