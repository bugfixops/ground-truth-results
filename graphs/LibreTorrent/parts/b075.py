# Citation-form rework 2026-11-01: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Batch 75 part (AddFeedDialog, AddFeedDialog$1/$2, AddFeedMutableParams).
# Hand-written edges only; no UNREACHABLE rows; no SUPPRESS entries.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b075_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# Authoritative batch source: clone
# graphs/LibreTorrent/scratch/merge-ready/batch75-merge-ready.md (40 REACHABLE /
# 0 UNREACHABLE / 0 OPEN, counted from the table labels).
# Rows covered by an existing graph_def edge are named in the .md Dependencies
# line instead of being re-edged here. One exception: initAlertDialog is
# hand-edged from initLayoutView (its batch-cited caller) because the existing
# graph edge onCreateDialog -> initAlertDialog does not match the printed
# call structure (onCreateDialog calls initLayoutView:205, which calls
# initAlertDialog:255); the suspect existing edge is flagged in REPORT.md.
# Button-lambda mapping is bytecode-verified (javap -c -p): $4 calls
# updateChannel, $5 calls deleteFeedDialog, $6 calls addChannel, $7 calls
# finish, $8 is the onShow listener that installs them.

# initAlertDialog is called from initLayoutView, not directly from
# onCreateDialog (see header note).
e('AddFeedDialog.initLayoutView', 'AddFeedDialog.initAlertDialog', 'CALL', 'Layout setup builds the alert dialog',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedDialog.java:255; SRC ui/addfeed/AddFeedDialog.java:258-288')

# Button / onShow / layout / focus / key / Rx dispatch edges.
e('AddFeedDialog.lambda$initAlertDialog$8', 'AddFeedDialog.lambda$initAlertDialog$4', 'FRAMEWORK', 'Edit-button click dispatches to the edit lambda',
  cls='non_standard', via='Dialog button click dispatch installed by the onShow listener',
  evidence='INFERRED click dispatch; SRC ui/addfeed/AddFeedDialog.java:275-280')
e('AddFeedDialog.lambda$initAlertDialog$8', 'AddFeedDialog.lambda$initAlertDialog$5', 'FRAMEWORK', 'Delete-button click dispatches to the delete lambda',
  cls='non_standard', via='Dialog button click dispatch installed by the onShow listener',
  evidence='INFERRED click dispatch; SRC ui/addfeed/AddFeedDialog.java:275-280')
e('AddFeedDialog.lambda$initAlertDialog$8', 'AddFeedDialog.lambda$initAlertDialog$6', 'FRAMEWORK', 'Add-button click dispatches to the add lambda',
  cls='non_standard', via='Dialog button click dispatch installed by the onShow listener',
  evidence='INFERRED click dispatch; SRC ui/addfeed/AddFeedDialog.java:275-284')
e('AddFeedDialog.lambda$initAlertDialog$8', 'AddFeedDialog.lambda$initAlertDialog$7', 'FRAMEWORK', 'Cancel-button click dispatches to the cancel lambda',
  cls='non_standard', via='Dialog button click dispatch installed by the onShow listener',
  evidence='INFERRED click dispatch; SRC ui/addfeed/AddFeedDialog.java:275-288')
e('AddFeedDialog.initAlertDialog', 'AddFeedDialog.lambda$initAlertDialog$8', 'FRAMEWORK', 'Dialog shown dispatches to the onShow listener',
  cls='non_standard', via='Dialog onShow dispatch',
  evidence='INFERRED onShow dispatch; SRC ui/addfeed/AddFeedDialog.java:275-288')
e('AddFeedDialog.initLayoutView', 'AddFeedDialog.lambda$initLayoutView$2', 'FRAMEWORK', 'End-icon click toggles the expandable layout',
  cls='non_standard', via='View click dispatch',
  evidence='INFERRED click dispatch; SRC ui/addfeed/AddFeedDialog.java:250')
e('AddFeedDialog.initLayoutView', 'AddFeedDialog.lambda$initLayoutView$3', 'FRAMEWORK', 'Clipboard-button click shows the clipboard dialog',
  cls='non_standard', via='View click dispatch',
  evidence='INFERRED click dispatch; SRC ui/addfeed/AddFeedDialog.java:252')
e('AddFeedDialog.onCreateDialog', 'AddFeedDialog.lambda$new$0', 'FRAMEWORK', 'Window focus change dispatches to the focus listener',
  cls='non_standard', via='ViewTreeObserver focus-change dispatch',
  evidence='INFERRED focus dispatch; SRC ui/addfeed/AddFeedDialog.java:112-113,207')
e('AddFeedDialog.onResume', 'AddFeedDialog.lambda$onResume$1', 'FRAMEWORK', 'Dialog key event dispatches to the key listener',
  cls='non_standard', via='Dialog key dispatch',
  evidence='INFERRED key dispatch; SRC ui/addfeed/AddFeedDialog.java:141-157')
e('AddFeedDialog.subscribeAlertDialog', 'AddFeedDialog.lambda$subscribeAlertDialog$10', 'CALL', 'Clipboard-item subscription runs its item lambda',
  cls='non_standard', via='Rx subscribe dispatch inside subscribeAlertDialog',
  evidence='INFERRED Rx dispatch; SRC ui/addfeed/AddFeedDialog.java:325-328')
e('AddFeedDialog.subscribeAlertDialog', 'AddFeedDialog.lambda$subscribeAlertDialog$9', 'CALL', 'Alert-event subscription runs its event lambda',
  cls='non_standard', via='Rx subscribe dispatch inside subscribeAlertDialog',
  evidence='INFERRED Rx dispatch; SRC ui/addfeed/AddFeedDialog.java:303-326')

# Dialog lifecycle chain (onAttach / onCreateDialog covered by Dependencies).
e('AddFeedDialog.onCreateDialog', 'AddFeedDialog.onStart', 'LIFECYCLE', 'Start the dialog after creation',
  evidence='SRC ui/addfeed/AddFeedDialog.java:180-209; SRC ui/addfeed/AddFeedDialog.java:170-176')
e('AddFeedDialog.onStart', 'AddFeedDialog.onResume', 'LIFECYCLE', 'Resume the dialog after start',
  evidence='SRC ui/addfeed/AddFeedDialog.java:170-176; SRC ui/addfeed/AddFeedDialog.java:141-158')
e('AddFeedDialog.onResume', 'AddFeedDialog.onStop', 'LIFECYCLE', 'Stop the dialog after resume',
  evidence='SRC ui/addfeed/AddFeedDialog.java:141-158; SRC ui/addfeed/AddFeedDialog.java:161-167')
e('AddFeedDialog.onStop', 'AddFeedDialog.onDestroyView', 'LIFECYCLE', 'Destroy the dialog view after stop',
  evidence='SRC ui/addfeed/AddFeedDialog.java:161-167; SRC ui/addfeed/AddFeedDialog.java:213-218')

# Clipboard dialog, TextWatchers, and the params getters.
e('AddFeedDialog.lambda$initLayoutView$3', 'AddFeedDialog.showClipboardDialog', 'CALL', 'Clipboard-button click shows the clipboard dialog',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedDialog.java:252; SRC ui/addfeed/AddFeedDialog.java:291-301')
e('AddFeedDialog.initLayoutView', 'AddFeedDialog$1.<init>', 'CALL', 'Layout setup registers the URL TextWatcher',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedDialog.java:222-235')
e('AddFeedDialog.initLayoutView', 'AddFeedDialog$1.afterTextChanged', 'FRAMEWORK', 'URL text change dispatches to the watcher callback',
  cls='non_standard', via='TextWatcher dispatch',
  evidence='INFERRED TextWatcher dispatch; SRC ui/addfeed/AddFeedDialog.java:222-235')
e('AddFeedDialog.initLayoutView', 'AddFeedDialog$1.beforeTextChanged', 'FRAMEWORK', 'URL text change dispatches to the watcher callback',
  cls='non_standard', via='TextWatcher dispatch',
  evidence='INFERRED TextWatcher dispatch; SRC ui/addfeed/AddFeedDialog.java:222-235')
e('AddFeedDialog.initLayoutView', 'AddFeedDialog$1.onTextChanged', 'FRAMEWORK', 'URL text change dispatches to the watcher callback',
  cls='non_standard', via='TextWatcher dispatch',
  evidence='INFERRED TextWatcher dispatch; SRC ui/addfeed/AddFeedDialog.java:222-235')
e('AddFeedDialog.initLayoutView', 'AddFeedDialog$2.<init>', 'CALL', 'Layout setup registers the filter TextWatcher',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedDialog.java:236-249')
e('AddFeedDialog.initLayoutView', 'AddFeedDialog$2.afterTextChanged', 'FRAMEWORK', 'Filter text change dispatches to the watcher callback',
  cls='non_standard', via='TextWatcher dispatch',
  evidence='INFERRED TextWatcher dispatch; SRC ui/addfeed/AddFeedDialog.java:236-249')
e('AddFeedDialog.initLayoutView', 'AddFeedDialog$2.beforeTextChanged', 'FRAMEWORK', 'Filter text change dispatches to the watcher callback',
  cls='non_standard', via='TextWatcher dispatch',
  evidence='INFERRED TextWatcher dispatch; SRC ui/addfeed/AddFeedDialog.java:236-249')
e('AddFeedDialog.initLayoutView', 'AddFeedDialog$2.onTextChanged', 'FRAMEWORK', 'Filter text change dispatches to the watcher callback',
  cls='non_standard', via='TextWatcher dispatch',
  evidence='INFERRED TextWatcher dispatch; SRC ui/addfeed/AddFeedDialog.java:236-249')
e('AddFeedDialog.initLayoutView', 'AddFeedDialog.switchClipboardButton', 'CALL', 'Layout setup refreshes the clipboard button',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedDialog.java:253; SRC ui/addfeed/AddFeedDialog.java:115-119')
e('AddFeedDialog.onStop', 'AddFeedDialog.unsubscribeClipboardManager', 'CALL', 'Dialog stop unsubscribes the clipboard manager',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedDialog.java:161-167; SRC ui/addfeed/AddFeedDialog.java:105-108')
e('AddFeedDialog.lambda$initAlertDialog$4', 'AddFeedDialog.updateChannel', 'CALL', 'Edit-button click updates the channel',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedDialog.java:279; SRC ui/addfeed/AddFeedDialog.java:395-409')
e('AddFeedViewModel.<init>', 'AddFeedMutableParams.<init>', 'CALL', 'ViewModel field initialiser constructs the mutable params',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedViewModel.java:48; SRC ui/addfeed/AddFeedMutableParams.java:27-35')
e('AddFeedViewModel.fetchParams', 'AddFeedMutableParams.getFeedId', 'CALL', 'fetchParams reads the feed id',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedViewModel.java:145-148; SRC ui/addfeed/AddFeedMutableParams.java:37-40')
e('AddFeedViewModel.applyParams', 'AddFeedMutableParams.getFilter', 'CALL', 'applyParams reads the filter for the channel record',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedViewModel.java:164-179; SRC ui/addfeed/AddFeedMutableParams.java:96-99')

# No UNREACHABLE rows in this batch; nothing to list here.
UNREACHABLE.update({})

# No part edge points at a method that is UNREACHABLE in any batch, and this
# batch has no UNREACHABLE methods of its own, so no SUPPRESS entries apply.
SUPPRESS.update(set())
