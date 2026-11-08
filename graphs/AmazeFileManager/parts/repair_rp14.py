# Repair batch 14: SmbSearchDialog$1, FastScroller, ThemedImageButton, Utils, AboutActivity, CloudIconDataFetcher, ColorAdapter, SearchTextTask
# Methods already in graph_def.py are excluded from this file

# ==== SmbSearchDialog$1 (anonymous inner class for SubnetScanner.ScanObserver)

# SmbSearchDialog$1.<init> - Anonymous class constructor
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog$1.<init>', 'CALL',
  'SmbSearchDialog creates anonymous ScanObserver instance',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:81 subnetScanner.setObserver(new SubnetScanner.ScanObserver() {...})')

# SmbSearchDialog$1.computerFound - Callback when SMB server is discovered
e('SubnetScanner.notifyComputerFound', 'SmbSearchDialog$1.computerFound', 'FRAMEWORK',
  'SubnetScanner calls computerFound callback when SMB server is discovered',
  evidence='INFERRED SubnetScanner notifies observer.computerFound(computer); SRC ui/dialogs/SmbSearchDialog.java:82-90 overrides computerFound')

# SmbSearchDialog$1.lambda$computerFound$0 - Lambda for runOnUiThread in computerFound
e('SmbSearchDialog$1.computerFound', 'SmbSearchDialog$1.lambda$computerFound$0', 'CALL',
  'computerFound posts lambda to UI thread',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:84-89 getActivity().runOnUiThread(() -> {...})')

# SmbSearchDialog$1.searchFinished - Callback when SMB search completes
e('SubnetScanner.notifySearchFinished', 'SmbSearchDialog$1.searchFinished', 'FRAMEWORK',
  'SubnetScanner calls searchFinished callback when scan completes',
  evidence='INFERRED SubnetScanner notifies observer.searchFinished(); SRC ui/dialogs/SmbSearchDialog.java:91-106 overrides searchFinished')

# SmbSearchDialog$1.lambda$searchFinished$1 - Lambda for runOnUiThread in searchFinished
e('SmbSearchDialog$1.searchFinished', 'SmbSearchDialog$1.lambda$searchFinished$1', 'CALL',
  'searchFinished posts lambda to UI thread',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:93-105 getActivity().runOnUiThread(() -> {...})')

# ==== ThemedImageButton (custom view inflated from XML)

# ThemedImageButton.<init>(Context) - Single-arg constructor
e('ThemedImageButton.<init>(Context,AttributeSet)', 'ThemedImageButton.<init>(Context)', 'LIFECYCLE',
  'ThemedImageButton(Context,AttributeSet) calls this(Context)',
  evidence='SRC ui/views/ThemedImageButton.java:13-15 ThemedImageButton(Context context) calls super(context)')

# ThemedImageButton.<init>(Context,AttributeSet) - Two-arg constructor (XML inflation)
e('S_MAIN', 'ThemedImageButton.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'ThemedImageButton inflated from XML layout',
  evidence='SRC res/layout/namepathswitch_preference.xml contains <com.amaze.filemanager.ui.views.ThemedImageButton>; INFERRED framework LayoutInflater calls two-arg constructor for XML views',
  env='ENV_LAUNCHER')

# ThemedImageButton.<init>(Context,AttributeSet,int) - Three-arg constructor
UNREACHABLE['ThemedImageButton.<init>(Context,AttributeSet,int)'] = ('framework_never_calls', 'Three-arg constructor not used - XML inflation uses two-arg constructor, no programmatic instantiation with style', 'SRC ui/views/ThemedImageButton.java:19-22 defines constructor; no app code calls new ThemedImageButton with three args', 'SOURCE')

# ThemedImageButton.onSetAlpha - Override of View method
e('ThemedImageButton.<init>(Context,AttributeSet)', 'ThemedImageButton.onSetAlpha', 'FRAMEWORK',
  'Framework may call onSetAlpha for view alpha animation',
  evidence='SRC ui/views/ThemedImageButton.java:24-27 overrides onSetAlpha; INFERRED framework View animation system calls onSetAlpha')

# ThemedImageButton.getAccessibilityClassName - Override for accessibility
e('ThemedImageButton.<init>(Context,AttributeSet)', 'ThemedImageButton.getAccessibilityClassName', 'FRAMEWORK',
  'Framework calls getAccessibilityClassName for accessibility services',
  evidence='SRC ui/views/ThemedImageButton.java:29-32 overrides getAccessibilityClassName; INFERRED framework accessibility system calls this method')

# ==== Utils (utility methods called from various locations)

# Utils.dpToPx - Convert dp to pixels
e('MainFragment.onActivityCreated', 'Utils.dpToPx', 'CALL',
  'MainFragment calls dpToPx for dimension conversion',
  evidence='SRC fragments/MainFragment.java:315 int dptopx = Utils.dpToPx(getContext(), 115)')

# Utils.getViewRawY - Get view's raw Y position
e('FastScroller.getRelativeTouchPosition', 'Utils.getViewRawY', 'CALL',
  'FastScroller uses getViewRawY for touch position calculation',
  evidence='SRC ui/views/FastScroller.java:147 float yInParent = event.getRawY() - Utils.getViewRawY(handle)')

# Utils.isDeviceInLandScape - Check orientation
UNREACHABLE['Utils.isDeviceInLandScape'] = ('no_trigger_in_app', 'isDeviceInLandScape is defined but only found commented out in app code', 'SRC utils/Utils.java:161-163 defines method; SRC ui/views/drawer/Drawer.java:161 only usage is commented: /*if(!Utils.isDeviceInLandScape(mainActivity)){', 'SOURCE')

# Utils.setTint - Set tint color for checkbox
e('SmbConnectDialog.onCreateDialog', 'Utils.setTint', 'CALL',
  'SmbConnectDialog calls setTint for checkbox color',
  evidence='SRC ui/dialogs/SmbConnectDialog.java:161 Utils.setTint(context, ch, accentColor)')

e('PrepareCopyTask.onPostExecute', 'Utils.setTint', 'CALL',
  'PrepareCopyTask calls setTint for checkbox color',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:193 Utils.setTint(context, checkBox, accentColor)')

# ==== AboutActivity (flavor-only - all methods marked INCOMPLETE per resume_rules.md)

# AboutActivity methods are in src/fdroid and src/play only, not in src/main
# Per resume_rules.md: "source only in flavor folder(s); DATASET.txt names no flavor (section 2.3)"
# These must be marked INCOMPLETE, not REACHABLE or UNREACHABLE

