# ---- Helper batch_018 label part (2024-12-29)

# CustomNavigationView is inflated from main_toolbar.xml layout and used as the drawer navigation view
# Constructor called during layout inflation from MainActivity.setContentView

e('android.view.LayoutInflater.inflate', 'com.amaze.filemanager.ui.views.drawer.CustomNavigationView.<init>', 'FRAMEWORK',
  'Layout inflation of com.amaze.filemanager.ui.views.drawer.CustomNavigationView from main_toolbar.xml',
  evidence='SRC main_toolbar.xml:58 shows <com.amaze.filemanager.ui.views.drawer.CustomNavigationView android:id="@+id/navigation"')

# CustomNavigationView.<init> calls super and sets self as listener
e('com.amaze.filemanager.ui.views.drawer.CustomNavigationView.<init>', 'com.amaze.filemanager.ui.views.drawer.CustomNavigationView.setNavigationItemSelectedListener', 'CALL',
  'Constructor calls super.setNavigationItemSelectedListener(this)',
  evidence='SRC CustomNavigationView.java:24 super.setNavigationItemSelectedListener(this)')

# Drawer sets the navigation item selected listener
e('com.amaze.filemanager.ui.views.drawer.Drawer.<init>', 'com.amaze.filemanager.ui.views.drawer.CustomNavigationView.setNavigationItemSelectedListener', 'CALL',
  'Drawer constructor sets itself as listener',
  evidence='SRC Drawer.java:162 navView.setNavigationItemSelectedListener(this)')

# onNavigationItemSelected is the callback for navigation item clicks
e('com.google.android.material.navigation.NavigationView', 'com.amaze.filemanager.ui.views.drawer.CustomNavigationView.onNavigationItemSelected', 'GUI',
  'Framework callback when user selects navigation drawer item',
  evidence='SRC CustomNavigationView.java:16-17 implements NavigationView.OnNavigationItemSelectedListener; method at line 33')

# onNavigationItemSelected calls onItemChecked
e('com.amaze.filemanager.ui.views.drawer.CustomNavigationView.onNavigationItemSelected', 'com.amaze.filemanager.ui.views.drawer.CustomNavigationView.onItemChecked', 'CALL',
  'Called when item should be selected',
  evidence='SRC CustomNavigationView.java:38,42 onItemChecked(item)')

# getSelected called from Drawer.refreshDrawer
e('com.amaze.filemanager.ui.views.drawer.Drawer.refreshDrawer', 'com.amaze.filemanager.ui.views.drawer.CustomNavigationView.getSelected', 'CALL',
  'Drawer.refreshDrawer reads selected item to restore state',
  evidence='SRC Drawer.java:451 MenuItem item = navView.getSelected()')

# setCheckedItem called from Drawer.selectCorrectDrawerItemForPath
e('com.amaze.filemanager.ui.views.drawer.Drawer.selectCorrectDrawerItemForPath', 'com.amaze.filemanager.ui.views.drawer.CustomNavigationView.setCheckedItem', 'CALL',
  'Drawer.selectCorrectDrawerItemForPath marks item as checked',
  evidence='SRC Drawer.java:678 navView.setCheckedItem(item)')

# deselectItems called from Drawer.deselectEverything
e('com.amaze.filemanager.ui.views.drawer.Drawer.deselectEverything', 'com.amaze.filemanager.ui.views.drawer.CustomNavigationView.deselectItems', 'CALL',
  'Drawer.deselectEverything clears navigation selection',
  evidence='SRC Drawer.java:715 navView.deselectItems()')

# CustomSshJConfig.init is called from MainActivity.onCreate
e('com.amaze.filemanager.activities.MainActivity.onCreate', 'com.amaze.filemanager.filesystem.ssh.CustomSshJConfig.init', 'CALL',
  'MainActivity initialization calls CustomSshJConfig.init',
  evidence='SRC MainActivity.java:286 CustomSshJConfig.init()')

# CustomSshJConfig constructor called when creating SSH clients
e('com.amaze.filemanager.asynchronous.asynctasks.ssh.SshAuthenticationTask.doInBackground', 'com.amaze.filemanager.filesystem.ssh.CustomSshJConfig.<init>', 'CALL',
  'SSH authentication task creates CustomSshJConfig instance',
  evidence='SRC SshAuthenticationTask.java:119 final SSHClient sshClient = new SSHClient(new CustomSshJConfig())')

e('com.amaze.filemanager.asynchronous.asynctasks.ssh.GetSshHostFingerprintTask.doInBackground', 'com.amaze.filemanager.filesystem.ssh.CustomSshJConfig.<init>', 'CALL',
  'SSH fingerprint task creates CustomSshJConfig instance',
  evidence='SRC GetSshHostFingerprintTask.java:84 final SSHClient sshClient = new SSHClient(new CustomSshJConfig())')

# UNREACHABLE methods - SavedState not used on API 27 due to ClassNotFoundException guard
# isNavigationViewSavedStateMissing returns true on API 23-28, blocking SavedState usage

UNREACHABLE['com.amaze.filemanager.ui.views.drawer.CustomNavigationView.onSaveInstanceState'] = (
    'framework_never_calls',
    'API 27 target; isNavigationViewSavedStateMissing returns true for API 23-28, method returns super.onSaveInstanceState() without using SavedState',
    'SRC CustomNavigationView.java:67-69 if (isNavigationViewSavedStateMissing()) return super.onSaveInstanceState(); line 117 returns true for API M-P',
    'SOURCE')

UNREACHABLE['com.amaze.filemanager.ui.views.drawer.CustomNavigationView.onRestoreInstanceState'] = (
    'framework_never_calls',
    'API 27 target; isNavigationViewSavedStateMissing returns true for API 23-28, method calls super.onRestoreInstanceState() without using SavedState',
    'SRC CustomNavigationView.java:84-87 if(isNavigationViewSavedStateMissing()) super.onRestoreInstanceState(state); return; line 117 returns true for API M-P',
    'SOURCE')

UNREACHABLE['com.amaze.filemanager.ui.views.drawer.CustomNavigationView.isNavigationViewSavedStateMissing'] = (
    'no_trigger_in_app',
    'Only called from onSaveInstanceState and onRestoreInstanceState which are themselves unreachable on API 27',
    'SRC CustomNavigationView.java:67,84,117 method definition and all call sites are within unreachable SavedState code paths',
    'SOURCE')

UNREACHABLE['com.amaze.filemanager.ui.views.drawer.CustomNavigationView$SavedState.<clinit>'] = (
    'framework_never_calls',
    'Static initializer for SavedState class; class not used on API 27 due to isNavigationViewSavedStateMissing guard',
    'SRC CustomNavigationView.java:120 SavedState class; line 117 isNavigationViewSavedStateMissing blocks usage on API 23-28',
    'SOURCE')

UNREACHABLE['com.amaze.filemanager.ui.views.drawer.CustomNavigationView$SavedState.<init>'] = (
    'framework_never_calls',
    'SavedState(Parcelable) constructor not used on API 27 due to isNavigationViewSavedStateMissing guard in onSaveInstanceState',
    'SRC CustomNavigationView.java:123-125 constructor; line 67-69 guard prevents SavedState creation',
    'SOURCE')

UNREACHABLE['com.amaze.filemanager.ui.views.drawer.CustomNavigationView$SavedState.<init>'] = (
    'framework_never_calls',
    'SavedState(Parcel) constructor not used on API 27 due to isNavigationViewSavedStateMissing guard in onRestoreInstanceState',
    'SRC CustomNavigationView.java:127-130 private constructor; line 84-87 guard prevents SavedState usage',
    'SOURCE')

UNREACHABLE['com.amaze.filemanager.ui.views.drawer.CustomNavigationView$SavedState.writeToParcel'] = (
    'framework_never_calls',
    'SavedState.writeToParcel not called on API 27 because SavedState instances never created due to isNavigationViewSavedStateMissing guard',
    'SRC CustomNavigationView.java:132-135 writeToParcel method; SavedState not instantiated on API 23-28',
    'SOURCE')

UNREACHABLE['com.amaze.filemanager.ui.views.drawer.CustomNavigationView$SavedState$1.<init>'] = (
    'framework_never_calls',
    'CREATOR anonymous class constructor; CREATOR not used on API 27 because SavedState parceling skipped',
    'SRC CustomNavigationView.java:138-145 CREATOR field; SavedState not parceled on API 23-28',
    'SOURCE')

UNREACHABLE['com.amaze.filemanager.ui.views.drawer.CustomNavigationView$SavedState$1.createFromParcel'] = (
    'framework_never_calls',
    'CREATOR.createFromParcel not called on API 27 because SavedState not saved to Parcel',
    'SRC CustomNavigationView.java:139-141 createFromParcel method; SavedState parceling blocked by line 84-87 guard',
    'SOURCE')

UNREACHABLE['com.amaze.filemanager.ui.views.drawer.CustomNavigationView$SavedState$1.newArray'] = (
    'framework_never_calls',
    'CREATOR.newArray not called on API 27 because SavedState not restored from Parcel',
    'SRC CustomNavigationView.java:142-144 newArray method; SavedState unparceling blocked by isNavigationViewSavedStateMissing',
    'SOURCE')

UNREACHABLE['com.amaze.filemanager.filesystem.ssh.CustomSshJConfig.initSignatureFactories'] = (
    'framework_never_calls',
    'Protected method overridden from DefaultConfig but never called by sshj library; DefaultConfig constructor does not invoke it',
    'SRC CustomSshJConfig.java:53-55 protected void initSignatureFactories; INFERRED source not read for DefaultConfig superclass constructor flow',
    'INFERRED')

UNREACHABLE['com.amaze.filemanager.filesystem.ssh.CustomSshJConfig.initRandomFactory'] = (
    'framework_never_calls',
    'Protected method overridden from DefaultConfig but never called by sshj library; DefaultConfig constructor does not invoke it',
    'SRC CustomSshJConfig.java:57-60 protected void initRandomFactory; INFERRED source not read for DefaultConfig superclass constructor flow',
    'INFERRED')
