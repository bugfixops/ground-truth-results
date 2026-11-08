# Citation-form rework 2026-11-02: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# C12 converter delivery (2026-11-01): audited A3 base copied unchanged except this header.
# No UNREACHABLE rows: stronger-evidence rule (b) is vacuous; no grade changes.
# Merger note recorded in REPORT-b078.md, NOT applied: rows 3/4 $n mapping stands as marked with the batch caveat carried (edges follow confirmed graph_def onShow routes 1282/1286/1288). Delivered printed evidence: parts/b078_printed.txt (fresh, from clone tree).
# Batch 78 part (AddTag dialog, AddTag state/ViewModel, and AddTorrentActivity core). Hand-written edges only.
# Each evidence string cites lines printed in
# helper/a3-g16/scratch/b078_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/
# Rows whose route already exists in merger-tree graph_def.py are
# listed in the .md Dependencies line and are NOT repeated here.

e('AddTagDialog.initLayoutView', 'AddTagDialog$1.<init>', 'CALL', 'Construct the anonymous TextWatcher registered on the name field',
  cls='explicit', evidence='SRC ui/addtag/AddTagDialog.java:138-152')
e('AddTagDialog.initLayoutView', 'AddTagDialog$1.beforeTextChanged', 'FRAMEWORK', 'TextWatcher beforeTextChanged dispatched on name-field text change',
  cls='non_standard', via='TextWatcher dispatch', evidence='INFERRED TextWatcher dispatch; SRC ui/addtag/AddTagDialog.java:138-141')
e('AddTagDialog.initLayoutView', 'AddTagDialog$1.onTextChanged', 'FRAMEWORK', 'TextWatcher onTextChanged dispatched on name-field text change',
  cls='non_standard', via='TextWatcher dispatch', evidence='INFERRED TextWatcher dispatch; SRC ui/addtag/AddTagDialog.java:138-145')
e('AddTagViewModel.<init>', 'AddTagState.<init>', 'CALL', 'ViewModel constructor creates its state object',
  cls='explicit', evidence='SRC ui/addtag/AddTagViewModel.java:41')
e('AddTagDialog.onCreateDialog', 'AddTagState.getColor', 'CALL', 'Create-dialog colour check reads the state colour',
  cls='explicit', evidence='SRC ui/addtag/AddTagDialog.java:123; SRC ui/addtag/AddTagState.java:53-55')
e('AddTagViewModel.saveTag', 'AddTagState.getExistsTagId', 'CALL', 'Save-tag reads the existing-tag id',
  cls='explicit', evidence='SRC ui/addtag/AddTagViewModel.java:57; SRC ui/addtag/AddTagState.java:33-35')
e('AddTagViewModel.saveTag', 'AddTagState.getName', 'CALL', 'Save-tag reads the state name for the new TagInfo',
  cls='explicit', evidence='SRC ui/addtag/AddTagViewModel.java:59; SRC ui/addtag/AddTagState.java:43-45')
e('AddTagViewModel.setInitValues', 'AddTagState.setExistsTagId', 'CALL', 'Init-values writes the existing-tag id into state',
  cls='explicit', evidence='SRC ui/addtag/AddTagViewModel.java:46; SRC ui/addtag/AddTagState.java:37-40')
e('AddTagViewModel.setInitValues', 'AddTagState.setName', 'CALL', 'Init-values writes the name into state',
  cls='explicit', evidence='SRC ui/addtag/AddTagViewModel.java:47; SRC ui/addtag/AddTagState.java:47-50')
e('AddTagDialog.onCreateDialog', 'AddTagViewModel.<init>', 'CALL', 'Create-dialog obtains the ViewModel from the provider',
  cls='explicit', evidence='SRC ui/addtag/AddTagDialog.java:117-118; SRC ui/addtag/AddTagViewModel.java:38-43')
e('AddTagViewModel.saveTag', 'AddTagViewModel.lambda$saveTag$0', 'CALL', 'Save-tag fromCallable body runs on subscribe',
  cls='non_standard', via='Rx Completable.fromCallable dispatch', evidence='INFERRED Rx dispatch; SRC ui/addtag/AddTagViewModel.java:63-74')
e('AddTagViewModel.lambda$saveTag$0', 'AddTagViewModel$TagAlreadyExistsException.<init>', 'CALL', 'Save-tag lambda throws the already-exists exception on a name clash',
  cls='explicit', evidence='SRC ui/addtag/AddTagViewModel.java:67; SRC ui/addtag/AddTagViewModel.java:77')

# No UNREACHABLE rows in this batch; nothing to list here.
UNREACHABLE.update({})

# No UNREACHABLE rows in this batch and no REACHABLE method of this
# group calls an UNREACHABLE method in bytecode (see REPORT.md),
# so no SUPPRESS entries apply.
SUPPRESS.update(set())
