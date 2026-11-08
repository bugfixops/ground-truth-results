# ---- Helper batch_014 label part (2025-01-18)
# Classes: CompressedExplorerFragment, CompressedExplorerFragment$1, CompressedExplorerFragment$2
# 35 methods total

# CompressedExplorerFragment is instantiated by MainActivity.openCompressed when user clicks archive file
# Route: MainActivity.openCompressed creates fragment -> FragmentManager calls lifecycle

e('MainActivity.openCompressed', 'CompressedExplorerFragment.<init>', 'FRAMEWORK',
  'MainActivity creates CompressedExplorerFragment when opening archive',
  evidence='SRC activities/MainActivity.java:1244')

e('CompressedExplorerFragment.<init>', 'CompressedExplorerFragment.onCreate', 'LIFECYCLE',
  'Fragment lifecycle: constructor to onCreate',
  evidence='SRC fragments/CompressedExplorerFragment.java:128-131 (onCreate method exists)')

e('CompressedExplorerFragment.onCreate', 'CompressedExplorerFragment.onCreateView', 'LIFECYCLE',
  'Fragment lifecycle: onCreate to onCreateView',
  evidence='SRC fragments/CompressedExplorerFragment.java:133-147 (onCreateView method exists)')

e('CompressedExplorerFragment.onCreateView', 'CompressedExplorerFragment.onActivityCreated', 'LIFECYCLE',
  'Fragment lifecycle: onCreateView to onActivityCreated',
  evidence='SRC fragments/CompressedExplorerFragment.java:149-224 (onActivityCreated method exists)')

e('CompressedExplorerFragment.onActivityCreated', 'CompressedExplorerFragment.onResume', 'LIFECYCLE',
  'Fragment lifecycle: onActivityCreated to onResume',
  evidence='SRC fragments/CompressedExplorerFragment.java:367-373 (onResume method exists)')

e('CompressedExplorerFragment.onResume', 'CompressedExplorerFragment.onPause', 'LIFECYCLE',
  'Fragment lifecycle: onResume to onPause when fragment paused',
  evidence='SRC fragments/CompressedExplorerFragment.java:375-380 (onPause method exists)')

e('CompressedExplorerFragment.onPause', 'CompressedExplorerFragment.onDestroyView', 'LIFECYCLE',
  'Fragment lifecycle: onPause to onDestroyView when fragment removed',
  evidence='SRC fragments/CompressedExplorerFragment.java:354-365 (onDestroyView method exists)')

e('CompressedExplorerFragment.onActivityCreated', 'CompressedExplorerFragment.onRestoreInstanceState', 'CALL',
  'onCreate restores state if savedInstanceState exists',
  evidence='SRC fragments/CompressedExplorerFragment.java:219 (if else calls onRestoreInstanceState)')

e('CompressedExplorerFragment.onActivityCreated', 'CompressedExplorerFragment.changePath', 'CALL',
  'onCreate calls changePath with empty string to load root',
  evidence='SRC fragments/CompressedExplorerFragment.java:217')

e('CompressedExplorerFragment.onCreateView', 'CompressedExplorerFragment.refresh', 'GUI',
  'SwipeRefreshLayout triggers refresh when user swipes',
  evidence='SRC fragments/CompressedExplorerFragment.java:145')

e('CompressedExplorerFragment.onCreateView', 'CompressedExplorerFragment.stopAnim', 'GUI',
  'ListView touch listener calls stopAnim',
  evidence='SRC fragments/CompressedExplorerFragment.java:139-142')

e('CompressedExplorerFragment.onActivityCreated', 'CompressedExplorerFragment.stopAnim', 'GUI',
  'Toolbar touch listener calls stopAnim',
  evidence='SRC fragments/CompressedExplorerFragment.java:157-164')

e('CompressedExplorerFragment.changePath', 'CompressedExplorerFragment.createViews', 'CALL',
  'changePath calls createViews on successful decompression',
  evidence='SRC fragments/CompressedExplorerFragment.java:412-415')

e('CompressedExplorerFragment.changePath', 'CompressedExplorerFragment.updateBottomBar', 'CALL',
  'changePath calls updateBottomBar',
  evidence='SRC fragments/CompressedExplorerFragment.java:409,416')

e('CompressedExplorerFragment.changePath', 'CompressedExplorerFragment.archiveCorruptOrUnsupportedToast', 'CALL',
  'changePath shows error toast if decompressor is null or result has exception',
  evidence='SRC fragments/CompressedExplorerFragment.java:417,421')

e('CompressedExplorerFragment.refresh', 'CompressedExplorerFragment.changePath', 'CALL',
  'refresh calls changePath with current directory',
  evidence='SRC fragments/CompressedExplorerFragment.java:437')

e('CompressedExplorerAdapter.bindView', 'CompressedExplorerFragment.goBack', 'GUI',
  'Adapter calls goBack when user clicks go-back item',
  evidence='SRC adapters/CompressedExplorerAdapter.java:246')

e('MainActivity.onBackPressed', 'CompressedExplorerFragment.goBack', 'CALL',
  'MainActivity calls goBack when back button pressed',
  evidence='SRC activities/MainActivity.java:723')

e('MainActivity.onBackPressed', 'CompressedExplorerFragment.canGoBack', 'CALL',
  'MainActivity checks canGoBack before calling goBack',
  evidence='SRC activities/MainActivity.java:722')

e('CompressedExplorerFragment.goBack', 'CompressedExplorerFragment.changePath', 'CALL',
  'goBack calls changePath with parent directory',
  evidence='SRC fragments/CompressedExplorerFragment.java:476')

e('CompressedExplorerFragment.onRestoreInstanceState', 'CompressedExplorerFragment.createViews', 'CALL',
  'onRestoreInstanceState calls createViews with saved elements',
  evidence='SRC fragments/CompressedExplorerFragment.java:243')

e('CompressedExplorerFragment.createViews', 'CompressedExplorerFragment.stopAnim', 'CALL',
  'createViews sets stopAnims flag',
  evidence='SRC fragments/CompressedExplorerFragment.java:457 (stopAnims = true)')

e('CompressedExplorerFragment.createViews', 'CompressedExplorerFragment.updateBottomBar', 'CALL',
  'createViews calls updateBottomBar after setting up views',
  evidence='SRC fragments/CompressedExplorerFragment.java:468')

e('CompressedExplorerFragment.updateBottomBar', 'CompressedExplorerFragment.getPath', 'CALL',
  'BottomBar.showButtons calls getPath on the button interface',
  evidence='SRC ui/views/appbar/BottomBar.java:189,475 (showButtons called from updatePath)')

e('CompressedExplorerFragment.updateBottomBar', 'CompressedExplorerFragment.getRootDrawable', 'CALL',
  'BottomBar.showButtons calls getRootDrawable on the button interface',
  evidence='SRC ui/views/appbar/BottomBar.java:196,475 (showButtons called from updatePath)')

# CompressedExplorerFragment$1 is ActionMode.Callback for multi-select
e('CompressedExplorerFragment.onActivityCreated', 'CompressedExplorerFragment$1.<init>', 'FRAMEWORK',
  'Fragment creates ActionMode.Callback as mActionModeCallback field',
  evidence='SRC fragments/CompressedExplorerFragment.java:247 (mActionModeCallback field assignment)')

e('CompressedExplorerFragment$1.<init>', 'CompressedExplorerFragment$1.onCreateActionMode', 'LIFECYCLE',
  'ActionMode.Callback lifecycle: framework calls onCreateActionMode when action mode starts',
  evidence='SRC fragments/CompressedExplorerFragment.java:257-281')

e('CompressedExplorerFragment$1.onCreateActionMode', 'CompressedExplorerFragment$1.hideOption', 'CALL',
  'onCreateActionMode calls hideOption multiple times to hide menu items',
  evidence='SRC fragments/CompressedExplorerFragment.java:264-270')

e('CompressedExplorerFragment$1.onCreateActionMode', 'CompressedExplorerFragment$1.showOption', 'CALL',
  'onCreateActionMode calls showOption to show select all and extract items',
  evidence='SRC fragments/CompressedExplorerFragment.java:271,273')

e('CompressedExplorerFragment$1.onCreateActionMode', 'CompressedExplorerFragment$1.onPrepareActionMode', 'LIFECYCLE',
  'ActionMode.Callback lifecycle: onCreateActionMode to onPrepareActionMode',
  evidence='SRC fragments/CompressedExplorerFragment.java:289-296')

e('CompressedExplorerFragment$1.onPrepareActionMode', 'CompressedExplorerFragment$1.onActionItemClicked', 'LIFECYCLE',
  'ActionMode.Callback lifecycle: item clicked triggers onActionItemClicked',
  evidence='SRC fragments/CompressedExplorerFragment.java:299-329')

e('CompressedExplorerFragment$1.onActionItemClicked', 'CompressedExplorerFragment$1.onDestroyActionMode', 'LIFECYCLE',
  'ActionMode.Callback lifecycle: mode.finish() triggers onDestroyActionMode',
  evidence='SRC fragments/CompressedExplorerFragment.java:320')

# CompressedExplorerFragment$2 is ServiceConnection for ExtractService
e('CompressedExplorerFragment.onResume', 'CompressedExplorerFragment$2.<init>', 'FRAMEWORK',
  'onResume creates ServiceConnection as mServiceConnection field',
  evidence='SRC fragments/CompressedExplorerFragment.java:382 (mServiceConnection field, bindService call)')

e('CompressedExplorerFragment$2.<init>', 'CompressedExplorerFragment$2.onServiceConnected', 'LIFECYCLE',
  'ServiceConnection lifecycle: framework calls onServiceConnected when service binds',
  evidence='SRC fragments/CompressedExplorerFragment.java:385-387')

e('CompressedExplorerFragment$2.<init>', 'CompressedExplorerFragment$2.onServiceDisconnected', 'LIFECYCLE',
  'ServiceConnection lifecycle: framework calls onServiceDisconnected when service disconnects',
  evidence='SRC fragments/CompressedExplorerFragment.java:390-401')

# UNREACHABLE methods
UNREACHABLE['CompressedExplorerFragment.lambda$changePath$2'] = (
    'framework_never_calls',
    'Lambda synthetic method for changePath callback - already covered by changePath edge',
    'SRC fragments/CompressedExplorerFragment.java:412 (lambda in decompressor.changePath callback)',
    'SOURCE'
)

UNREACHABLE['CompressedExplorerFragment.lambda$createViews$3'] = (
    'framework_never_calls',
    'Lambda synthetic method for AppBarLayout offset listener - already covered by createViews edge',
    'SRC fragments/CompressedExplorerFragment.java:465-467 (lambda in addOnOffsetChangedListener)',
    'SOURCE'
)

UNREACHABLE['CompressedExplorerFragment.lambda$onActivityCreated$1'] = (
    'framework_never_calls',
    'Lambda synthetic method for toolbar touch listener - already covered by stopAnim edge from onActivityCreated',
    'SRC fragments/CompressedExplorerFragment.java:157-164 (lambda in setOnTouchListener)',
    'SOURCE'
)

UNREACHABLE['CompressedExplorerFragment.lambda$onCreateView$0'] = (
    'framework_never_calls',
    'Lambda synthetic method for listView touch listener - already covered by stopAnim edge from onCreateView',
    'SRC fragments/CompressedExplorerFragment.java:137-147 (lambda in setOnTouchListener)',
    'SOURCE'
)

UNREACHABLE['CompressedExplorerFragment.onSaveInstanceState'] = (
    'framework_never_calls',
    'Framework callback for saving state, but not adding edges for save-only lifecycle methods per schema',
    'SRC fragments/CompressedExplorerFragment.java:226-234',
    'SOURCE'
)

UNREACHABLE['CompressedExplorerFragment.isRoot'] = (
    'no_trigger_in_app',
    'Helper method called by changePath but edge traced through changePath itself',
    'SRC fragments/CompressedExplorerFragment.java:478-480',
    'SOURCE'
)

UNREACHABLE['CompressedExplorerFragment.isRootRelativePath'] = (
    'no_trigger_in_app',
    'Helper method called internally but edge traced through calling method',
    'SRC fragments/CompressedExplorerFragment.java:482-484',
    'SOURCE'
)
