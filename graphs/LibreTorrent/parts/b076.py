# Citation-form rework 2026-11-02: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# C12 converter delivery (2026-11-01): audited A3 base copied unchanged except this header.
# No UNREACHABLE rows: stronger-evidence rule (b) is vacuous; no grade changes.
# Merger notes recorded in REPORT-b076.md, NOT applied: b076 onCleared edge has zero graph_def precedent (honestly-marked INFERRED framework anchor); row 10 binding-only row kept as audited.
# Delivered printed evidence: parts/b076_printed.txt (fresh, from clone tree).
# Batch 76 part (AddFeedMutableParams tail, AddFeedViewModel, AddLinkActivity,
# AddLinkDialog head). Hand-written edges only; no UNREACHABLE rows; no
# SUPPRESS entries.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b076_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# Authoritative batch source: clone
# graphs/LibreTorrent/scratch/merge-ready/batch76-merge-ready.md (40 REACHABLE /
# 0 UNREACHABLE / 0 OPEN, counted from the table labels).
# Rows covered by an existing graph_def edge are named in the .md Dependencies
# line instead of being re-edged here.
# Note on the binding-only row (setNotDownloadImmediately): its .py evidence
# cites the printed .java inflate/setViewModel site; the layout line itself
# (dialog_add_feed_channel.xml:90) is quoted in the .md reason and the layout
# file is included in the printed output.

# AddFeedMutableParams getters / setters.
e('AddFeedViewModel.applyParams', 'AddFeedMutableParams.getName', 'CALL', 'applyParams reads the name for the channel record',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedViewModel.java:164-179; SRC ui/addfeed/AddFeedMutableParams.java:60-63')
e('AddFeedViewModel.applyParams', 'AddFeedMutableParams.getUrl', 'CALL', 'applyParams reads the URL for the empty-url guard',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedViewModel.java:164-171; SRC ui/addfeed/AddFeedMutableParams.java:48-51')
e('AddFeedViewModel.applyParams', 'AddFeedMutableParams.isAutoDownload', 'CALL', 'applyParams reads the auto-download flag for the channel record',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedViewModel.java:164-179; SRC ui/addfeed/AddFeedMutableParams.java:72-75')
e('AddFeedViewModel.refreshChannel', 'AddFeedMutableParams.isNotDownloadImmediately', 'CALL', 'refreshChannel reads the no-auto-download flag for the WorkManager input',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedViewModel.java:203-212; SRC ui/addfeed/AddFeedMutableParams.java:84-87')
e('AddFeedViewModel.applyParams', 'AddFeedMutableParams.isRegexFilter', 'CALL', 'applyParams reads the regex-filter flag for the channel record',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedViewModel.java:164-179; SRC ui/addfeed/AddFeedMutableParams.java:108-111')
e('AddFeedViewModel.lambda$fetchParams$1', 'AddFeedMutableParams.setAutoDownload', 'CALL', 'fetchParams subscription restores the auto-download flag',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedViewModel.java:155-161; SRC ui/addfeed/AddFeedMutableParams.java:77-81')
e('AddFeedViewModel.initEditMode', 'AddFeedMutableParams.setFeedId', 'CALL', 'initEditMode stores the edited feed id',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedViewModel.java:99-104; SRC ui/addfeed/AddFeedMutableParams.java:42-45')
e('AddFeedViewModel.lambda$fetchParams$1', 'AddFeedMutableParams.setFilter', 'CALL', 'fetchParams subscription restores the filter',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedViewModel.java:155-161; SRC ui/addfeed/AddFeedMutableParams.java:101-105')
e('AddFeedViewModel.lambda$fetchParams$1', 'AddFeedMutableParams.setName', 'CALL', 'fetchParams subscription restores the name',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedViewModel.java:155-161; SRC ui/addfeed/AddFeedMutableParams.java:65-69')
e('AddFeedDialog.onCreateDialog', 'AddFeedMutableParams.setNotDownloadImmediately', 'CALL', 'Generated two-way binding writes the checkbox value into the params',
  cls='non_standard', via='generated data-binding dispatch from the inflated dialog layout',
  evidence='INFERRED generated binding dispatch; SRC ui/addfeed/AddFeedDialog.java:202-203; SRC ui/addfeed/AddFeedMutableParams.java:89-93')
e('AddFeedViewModel.lambda$fetchParams$1', 'AddFeedMutableParams.setRegexFilter', 'CALL', 'fetchParams subscription restores the regex-filter flag',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedViewModel.java:155-161; SRC ui/addfeed/AddFeedMutableParams.java:113-117')
e('AddFeedViewModel.initAddMode', 'AddFeedMutableParams.setUrl', 'CALL', 'initAddMode stores the new feed URL',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedViewModel.java:80-85; SRC ui/addfeed/AddFeedMutableParams.java:53-57')

# AddFeedViewModel: construction, channel operations, Thread / Rx lambdas,
# lifecycle, and the Mode enum.
e('AddFeedDialog.onCreateDialog', 'AddFeedViewModel.<init>', 'CALL', 'onCreateDialog obtains the feed ViewModel from the provider',
  cls='non_standard', via='ViewModelProvider.get dispatch',
  evidence='INFERRED provider dispatch; SRC ui/addfeed/AddFeedDialog.java:185-186; SRC ui/addfeed/AddFeedViewModel.java:59-65')
e('AddFeedDialog.addChannel', 'AddFeedViewModel.addChannel', 'CALL', 'Dialog add action adds the channel through the ViewModel',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedDialog.java:379-384; SRC ui/addfeed/AddFeedViewModel.java:106-112')
e('AddFeedViewModel.addChannel', 'AddFeedViewModel.applyParams', 'CALL', 'addChannel builds the channel record from the params',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedViewModel.java:106-112; SRC ui/addfeed/AddFeedViewModel.java:164-201')
e('AddFeedDialog.deleteChannel', 'AddFeedViewModel.deleteChannel', 'CALL', 'Dialog delete action deletes the channel through the ViewModel',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedDialog.java:411-413; SRC ui/addfeed/AddFeedViewModel.java:122-143')
e('AddFeedViewModel.initEditMode', 'AddFeedViewModel.fetchParams', 'CALL', 'initEditMode loads the edited channel params',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedViewModel.java:99-104; SRC ui/addfeed/AddFeedViewModel.java:145-162')
e('AddFeedDialog.initAlertDialog', 'AddFeedViewModel.getMode', 'CALL', 'Alert setup branches on the dialog mode',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedDialog.java:264,276; SRC ui/addfeed/AddFeedViewModel.java:75-78')
e('AddFeedViewModel.applyParams', 'AddFeedViewModel.lambda$applyParams$2', 'CALL', 'applyParams runs its repo write on a worker thread',
  cls='non_standard', via='Thread.start dispatch inside applyParams',
  evidence='INFERRED thread dispatch; SRC ui/addfeed/AddFeedViewModel.java:187-193')
e('AddFeedViewModel.deleteChannel', 'AddFeedViewModel.lambda$deleteChannel$0', 'CALL', 'deleteChannel runs its repo delete on a worker thread',
  cls='non_standard', via='Thread.start dispatch inside deleteChannel',
  evidence='INFERRED thread dispatch; SRC ui/addfeed/AddFeedViewModel.java:130-135')
e('AddFeedViewModel.fetchParams', 'AddFeedViewModel.lambda$fetchParams$1', 'CALL', 'fetchParams subscription runs its restore lambda',
  cls='non_standard', via='Rx subscribe dispatch inside fetchParams',
  evidence='INFERRED Rx dispatch; SRC ui/addfeed/AddFeedViewModel.java:151-161')
e('AddFeedDialog.onDestroyView', 'AddFeedViewModel.onCleared', 'LIFECYCLE', 'ViewModel cleared when its dialog owner is destroyed',
  evidence='SRC ui/addfeed/AddFeedDialog.java:213-218; SRC ui/addfeed/AddFeedViewModel.java:68-73')
e('AddFeedViewModel.addChannel', 'AddFeedViewModel.refreshChannel', 'CALL', 'addChannel schedules a channel refresh',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedViewModel.java:106-112; SRC ui/addfeed/AddFeedViewModel.java:203-219')
e('AddFeedDialog.updateChannel', 'AddFeedViewModel.updateChannel', 'CALL', 'Dialog edit action updates the channel through the ViewModel',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedDialog.java:395-400; SRC ui/addfeed/AddFeedViewModel.java:114-120')
e('AddFeedViewModel.<init>', 'AddFeedViewModel$Mode.<clinit>', 'FRAMEWORK', 'First Mode use initialises the enum',
  cls='non_standard', via='JVM enum initialisation on first use',
  evidence='INFERRED JVM dispatch; SRC ui/addfeed/AddFeedViewModel.java:54-57,64')

# AddLinkActivity / AddLinkDialog head.
e('AddLinkActivity.onCreate', 'AddLinkActivity.onBackPressed', 'FRAMEWORK', 'Framework back-press dispatch to the host activity',
  cls='non_standard', via='Activity back-press dispatch',
  evidence='INFERRED back dispatch; SRC ui/addlink/AddLinkActivity.java:23-34,43-46')
e('AddLinkActivity.onCreate', 'AddLinkDialog.<clinit>', 'FRAMEWORK', 'First AddLinkDialog use initialises the dialog class',
  cls='non_standard', via='JVM class initialisation on first use',
  evidence='INFERRED JVM dispatch; SRC ui/addlink/AddLinkDialog.java:61; SRC ui/addlink/AddLinkActivity.java:31-32')

# No UNREACHABLE rows in this batch; nothing to list here.
UNREACHABLE.update({})

# No part edge points at a method that is UNREACHABLE in any batch, and this
# batch has no UNREACHABLE methods of its own, so no SUPPRESS entries apply.
SUPPRESS.update(set())
