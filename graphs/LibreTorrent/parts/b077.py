# Citation-form rework 2026-11-02: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# C12 converter delivery (2026-11-01): audited A3 base copied unchanged except this header.
# No UNREACHABLE rows: stronger-evidence rule (b) is vacuous; no grade changes.
# No merger notes for this batch. Delivered printed evidence: parts/b077_printed.txt (fresh, from clone tree).
# Batch 77 part (AddLinkDialog tail, AddLinkViewModel, AddTagActivity,
# AddTagDialog head). Hand-written edges only; no UNREACHABLE rows; no
# SUPPRESS entries.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b077_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# Authoritative batch source: clone
# graphs/LibreTorrent/scratch/merge-ready/batch77-merge-ready.md (40 REACHABLE /
# 0 UNREACHABLE / 0 OPEN, counted from the table labels).
# Rows covered by an existing graph_def edge are named in the .md Dependencies
# line instead of being re-edged here. The existing graph edges into the
# AddLinkDialog lambdas are REGISTER-only and therefore do NOT confer
# reachability, so those lambdas get hand-written dispatch edges here.
# Button-lambda mapping is bytecode-verified (javap -c -p): $4 calls addLink,
# $5 calls finish, $6 is the onShow listener that installs them.

# AddLinkDialog dispatch edges (REGISTER-only existing edges not relied on).
e('AddLinkDialog.lambda$initAlertDialog$6', 'AddLinkDialog.lambda$initAlertDialog$4', 'FRAMEWORK', 'Add-button click dispatches to the add lambda',
  cls='non_standard', via='Dialog button click dispatch installed by the onShow listener',
  evidence='INFERRED click dispatch; SRC ui/addlink/AddLinkDialog.java:238-241')
e('AddLinkDialog.lambda$initAlertDialog$6', 'AddLinkDialog.lambda$initAlertDialog$5', 'FRAMEWORK', 'Cancel-button click dispatches to the cancel lambda',
  cls='non_standard', via='Dialog button click dispatch installed by the onShow listener',
  evidence='INFERRED click dispatch; SRC ui/addlink/AddLinkDialog.java:238-245')
e('AddLinkDialog.initAlertDialog', 'AddLinkDialog.lambda$initAlertDialog$6', 'FRAMEWORK', 'Dialog shown dispatches to the onShow listener',
  cls='non_standard', via='Dialog onShow dispatch',
  evidence='INFERRED onShow dispatch; SRC ui/addlink/AddLinkDialog.java:238-245')
e('AddLinkDialog.initLayoutView', 'AddLinkDialog.lambda$initLayoutView$3', 'FRAMEWORK', 'Clipboard-button click shows the clipboard dialog',
  cls='non_standard', via='View click dispatch',
  evidence='INFERRED click dispatch; SRC ui/addlink/AddLinkDialog.java:221')
e('AddLinkDialog.onCreateDialog', 'AddLinkDialog.lambda$new$2', 'FRAMEWORK', 'Window focus change dispatches to the focus listener',
  cls='non_standard', via='ViewTreeObserver focus-change dispatch',
  evidence='INFERRED focus dispatch; SRC ui/addlink/AddLinkDialog.java:160-161,189')
e('AddLinkDialog.onResume', 'AddLinkDialog.lambda$onResume$0', 'FRAMEWORK', 'Dialog key event dispatches to the key listener',
  cls='non_standard', via='Dialog key dispatch',
  evidence='INFERRED key dispatch; SRC ui/addlink/AddLinkDialog.java:93-111')
e('AddLinkDialog.subscribeAlertDialog', 'AddLinkDialog.lambda$subscribeAlertDialog$1', 'CALL', 'Clipboard-item subscription runs its item lambda',
  cls='non_standard', via='Rx subscribe dispatch inside subscribeAlertDialog',
  evidence='INFERRED Rx dispatch; SRC ui/addlink/AddLinkDialog.java:130-137')

# AddLinkDialog lifecycle chain (onAttach / onCreateDialog / onStart covered
# by Dependencies).
e('AddLinkDialog.onStart', 'AddLinkDialog.onResume', 'LIFECYCLE', 'Resume the dialog after start',
  evidence='SRC ui/addlink/AddLinkDialog.java:122-128; SRC ui/addlink/AddLinkDialog.java:93-111')
e('AddLinkDialog.onResume', 'AddLinkDialog.onStop', 'LIFECYCLE', 'Stop the dialog after resume',
  evidence='SRC ui/addlink/AddLinkDialog.java:93-111; SRC ui/addlink/AddLinkDialog.java:113-119')
e('AddLinkDialog.onStop', 'AddLinkDialog.onDestroyView', 'LIFECYCLE', 'Destroy the dialog view after stop',
  evidence='SRC ui/addlink/AddLinkDialog.java:113-119; SRC ui/addlink/AddLinkDialog.java:195-199')

# AddLinkDialog remaining calls, ViewModel, and TextWatcher.
e('AddLinkDialog.initLayoutView', 'AddLinkDialog.switchClipboardButton', 'CALL', 'Layout setup refreshes the clipboard button',
  cls='explicit', evidence='SRC ui/addlink/AddLinkDialog.java:222; SRC ui/addlink/AddLinkDialog.java:163-167')
e('AddLinkDialog.onStop', 'AddLinkDialog.unsubscribeClipboardManager', 'CALL', 'Dialog stop unsubscribes the clipboard manager',
  cls='explicit', evidence='SRC ui/addlink/AddLinkDialog.java:113-119; SRC ui/addlink/AddLinkDialog.java:153-156')
e('AddLinkDialog.initLayoutView', 'AddLinkDialog$1.<init>', 'CALL', 'Layout setup registers the link TextWatcher',
  cls='explicit', evidence='SRC ui/addlink/AddLinkDialog.java:205-219')
e('AddLinkDialog.initLayoutView', 'AddLinkDialog$1.afterTextChanged', 'FRAMEWORK', 'Link text change dispatches to the watcher callback',
  cls='non_standard', via='TextWatcher dispatch',
  evidence='INFERRED TextWatcher dispatch; SRC ui/addlink/AddLinkDialog.java:205-219')
e('AddLinkDialog.initLayoutView', 'AddLinkDialog$1.beforeTextChanged', 'FRAMEWORK', 'Link text change dispatches to the watcher callback',
  cls='non_standard', via='TextWatcher dispatch',
  evidence='INFERRED TextWatcher dispatch; SRC ui/addlink/AddLinkDialog.java:205-219')
e('AddLinkDialog.initLayoutView', 'AddLinkDialog$1.onTextChanged', 'FRAMEWORK', 'Link text change dispatches to the watcher callback',
  cls='non_standard', via='TextWatcher dispatch',
  evidence='INFERRED TextWatcher dispatch; SRC ui/addlink/AddLinkDialog.java:205-219')
e('AddLinkDialog.onCreateDialog', 'AddLinkViewModel.<init>', 'CALL', 'onCreateDialog obtains the link ViewModel from the provider',
  cls='non_standard', via='ViewModelProvider.get dispatch',
  evidence='INFERRED provider dispatch; SRC ui/addlink/AddLinkDialog.java:176-177; SRC ui/addlink/AddLinkViewModel.java:40-43')
e('AddLinkDialog.initLayoutView', 'AddLinkViewModel.initLinkFromClipboard', 'CALL', 'Layout setup seeds the link from the clipboard',
  cls='explicit', evidence='SRC ui/addlink/AddLinkDialog.java:223; SRC ui/addlink/AddLinkViewModel.java:45-59')

# AddTagActivity / AddTagDialog head.
e('AddTagActivity.onCreate', 'AddTagActivity.onBackPressed', 'FRAMEWORK', 'Framework back-press dispatch to the host activity',
  cls='non_standard', via='Activity back-press dispatch',
  evidence='INFERRED back dispatch; SRC ui/addtag/AddTagActivity.java:47-60,73-75')
e('AddTagDialog.lambda$initLayoutView$1', 'AddTagActivity.onDialogDismissed', 'FRAMEWORK', 'Color picker dismissal calls back into its listener activity',
  cls='non_standard', via='ColorPickerDialog library callback dispatch',
  evidence='INFERRED library dispatch; SRC ui/addtag/AddTagDialog.java:153-155; SRC ui/addtag/AddTagActivity.java:83-84')
e('AddTagActivity.onCreate', 'AddTagDialog.<clinit>', 'FRAMEWORK', 'First AddTagDialog use initialises the dialog class',
  cls='non_standard', via='JVM class initialisation on first use',
  evidence='INFERRED JVM dispatch; SRC ui/addtag/AddTagDialog.java:57; SRC ui/addtag/AddTagActivity.java:58-59')

# No UNREACHABLE rows in this batch; nothing to list here.
UNREACHABLE.update({})

# No part edge points at a method that is UNREACHABLE in any batch, and this
# batch has no UNREACHABLE methods of its own, so no SUPPRESS entries apply.
SUPPRESS.update(set())
