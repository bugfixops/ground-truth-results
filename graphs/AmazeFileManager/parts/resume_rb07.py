# ---- resume batch rb_07 (2025-01-18)

# DatabaseViewerActivity lifecycle methods
e('DatabaseViewerActivity.onCreate', 'DatabaseViewerActivity.onPrepareOptionsMenu', 'LIFECYCLE',
  'Activity menu lifecycle callback',
  evidence='INFERRED Activity options menu callbacks (framework source not read); SRC DatabaseViewerActivity.java:198-201')

e('DatabaseViewerActivity.onCreate', 'DatabaseViewerActivity.onDestroy', 'LIFECYCLE',
  'Activity lifecycle onDestroy',
  evidence='INFERRED Activity onDestroy called when activity finishes (framework source not read); SRC DatabaseViewerActivity.java:189-195')

e('DatabaseViewerActivity.onOptionsItemSelected', 'DatabaseViewerActivity.onBackPressed', 'CALL',
  'Home button in options menu calls onBackPressed',
  evidence='SRC DatabaseViewerActivity.java:206-207')

# Drawer.resetPendingPath
e('Drawer.onDrawerClosed', 'Drawer.resetPendingPath', 'CALL',
  'resetPendingPath clears pending navigation path if pendingPath is not null',
  evidence='SRC Drawer.java:557 pendingPath assigned when menu item selected; Drawer.java:563 called to clear after navigation; resetPendingPath at line 719-721')

# Drawer.lambda$addNewItem$5 - this is a menu item onClick lambda
# The exact lambda is determined by compiler; it's one of the lambdas in addNewItem calls for menu items
# All these lambdas are REACHABLE from Drawer.onNavigationItemSelected via MenuMetadata.onClickListener.onClick()
e('Drawer.refreshDrawer', 'Drawer.lambda$addNewItem$5', 'CALL',
  'refreshDrawer creates menu items with lambdas via addNewItem; lambda $5 is one of the menu item onClick handlers',
  evidence='SRC Drawer.java:402-439 addNewItem calls create MenuMetadata with lambda Runnables for FTP/Apps/Settings menu items; Drawer.java:597 meta.onClickListener.onClick() calls the lambda')

# UNREACHABLE methods
UNREACHABLE['DatapointParcelable.<init>(Landroid/os/Parcel;)V'] = ('no_trigger_in_app', 'Parcel constructor only called from createFromParcel which is UNREACHABLE (no getParcelable calls for DatapointParcelable)', 'SRC DatapointParcelable.java:120-127 constructor reads from Parcel; createFromParcel at line 129-131 is only caller', 'SOURCE')

UNREACHABLE['DatapointParcelable.<init>(Ljava/lang/String;IIJJJZ)V'] = ('no_trigger_in_app', '7-parameter constructor never called; publishResults uses 8-param constructor, addFirstDatapoint uses 4-param constructor', 'SRC DatapointParcelable.java:78-88 constructor definition; AbstractProgressiveService.java:157-158 uses 8-param (String,int,int,long,long,long,boolean,boolean), line 178 uses 4-param (String,int,long,boolean); no 7-param calls found', 'SOURCE')
