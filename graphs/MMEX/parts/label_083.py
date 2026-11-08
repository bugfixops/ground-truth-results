# ================================================================== batch 083 (label_083): 6 classes, 38 methods
# (graphs/MMEX/scratch/batches/batch_083.txt): MainActivity_MembersInjector (4, Dagger-generated),
# MyActionBarDrawerToggle (4), RecentDatabaseEntryComparator (2), RecentDatabasesProvider (18, including $1.<init>),
# RecentDatabasesProvider_Factory (3, Dagger-generated), SelectDatabaseActivity (7).
# Rows, printed lines and counts: graphs/MMEX/parts/label_083.md (32 REACHABLE, 6 UNREACHABLE, 0 INCOMPLETE).
# Grep and class-file evidence: graphs/MMEX/parts/label_083.grep.txt (sections 1-4).
# This file writes:
#   - 1 SCREENS key: S_SELECT_DATABASE (new; no S_SELECT* key exists in graph_def.py or other parts; see Open points in label_083.md);
#   - 8 e() edges: 1 INTENT, 1 LIFECYCLE, 1 ENTERS, 3 FRAMEWORK (two picker results, one permission request),
#     and 2 non_standard CALL edges for the Dagger Lazy<RecentDatabasesProvider>.get hop into
#     RecentDatabasesProvider_Factory.get (from MainActivity.getDatabases and MainActivity.changeDatabase);
#   - 4 gui() edges: S_SELECT_DATABASE to the two @OnClick handlers, S_HOME to the two drawer-toggle callbacks;
#   - 3 sup() pairs (D14a): auto CALL records whose caller is UNREACHABLE (create -> <init>, injectMembers -> injectMDatabases,
#     compare -> DatabaseMetadata.isSynchronised);
#   - 6 UNREACHABLE entries (no_trigger_in_app).
# No other CALL edges: the other REACHABLE rows rest on auto_calls.json records (D7).
# Edges whose destination is owned by another batch (PasswordActivity INTENT edges, MainActivity.onCreate and similar) are not written here (D1).

SCREENS.update({'S_SELECT_DATABASE': 'The database chooser (SelectDatabaseActivity): the create-database button (createDatabaseButton) and the open-database button (openDatabaseButton); shown when no valid database is set (MainActivity.showPrerequisite) or when a database change fails (MainActivity.changeDatabase)'})

# ---- INTENT / LIFECYCLE / ENTERS: the chooser page
e('MainActivity.showSelectDatabaseActivity', 'SelectDatabaseActivity.<init>', 'INTENT',
  'new Intent(this, SelectDatabaseActivity.class) with FLAG_ACTIVITY_CLEAR_TOP, then startActivity (MainActivity.java:1503-1506)',
  evidence='MainActivity.java:1486-1487 (showPrerequisite, branch taken when isDatabaseAvailable is false), 1503-1506; auto CALL changeDatabase -> showSelectDatabaseActivity at MainActivity.java:554; AndroidManifest.xml:368 (no intent-filter, explicit intent only); label_083.grep.txt sections 1, 4')

e('SelectDatabaseActivity.<init>', 'SelectDatabaseActivity.onCreate', 'LIFECYCLE',
  'Framework creates the activity (implicit constructor) and calls onCreate (SelectDatabaseActivity.java:54)',
  evidence='SelectDatabaseActivity.java:46-54; LIFECYCLE from the implicit constructor to onCreate (framework activity lifecycle, INFERRED; the framework source is not read)')

e('SelectDatabaseActivity.onCreate', 'S_SELECT_DATABASE', 'ENTERS',
  'setContentView(R.layout.activity_select_database) shows the chooser (SelectDatabaseActivity.java:56)',
  evidence='SelectDatabaseActivity.java:56; res/layout/activity_select_database.xml:62 and 80 (the two buttons)')

# ---- FRAMEWORK: picker results and permission result
e('SelectDatabaseActivity.onOpenDatabaseClick', 'SelectDatabaseActivity.onActivityResult', 'FRAMEWORK',
  'FileStorageHelper.showStorageFilePicker starts the document picker with startActivityForResult (request code RequestCodes.SELECT_DOCUMENT); the framework returns the result to onActivityResult',
  evidence='SelectDatabaseActivity.java:106-111 (showStorageFilePicker at 110); core/docstorage/FileStorageHelper.java:56-65 (startActivityForResult at 65, SELECT_DOCUMENT at 58) under final_java_only/MMEX/app/MMEX-#v2024.06.14/app/src/main/java/com/money/manager/ex/')

e('SelectDatabaseActivity.onCreateDatabaseClick', 'SelectDatabaseActivity.onActivityResult', 'FRAMEWORK',
  'FileStorageHelper.showCreateFilePicker starts the create-document picker with startActivityForResult (request code RequestCodes.CREATE_DOCUMENT); the framework returns the result to onActivityResult',
  evidence='SelectDatabaseActivity.java:99-104 (showCreateFilePicker at 103); core/docstorage/FileStorageHelper.java:74-83 (startActivityForResult at 83, CREATE_DOCUMENT at 76)')

e('SelectDatabaseActivity.onCreate', 'SelectDatabaseActivity.onRequestPermissionsResult', 'FRAMEWORK',
  'requestExternalStoragePermissions(this) (SelectDatabaseActivity.java:64) asks for the storage permissions when not yet granted; the framework returns the answer to onRequestPermissionsResult',
  evidence='SelectDatabaseActivity.java:63-64; utils/MmxFileUtils.java:140-154 (requestExternalStoragePermissions), 156-165 (ActivityCompat.requestPermissions at 162, only when the permission is not granted, line 160)')

# ---- non_standard CALL: Dagger Lazy<RecentDatabasesProvider>.get runs RecentDatabasesProvider_Factory.get (label_036 pattern)
e('MainActivity.getDatabases', 'RecentDatabasesProvider_Factory.get', 'CALL',
  'mDatabases.get() (Dagger Lazy<RecentDatabasesProvider> injected into the field at MainActivity.java:157) runs the factory provider RecentDatabasesProvider_Factory.get on first use',
  cls='non_standard',
  via='dagger.Lazy.get: DoubleCheck calls the Provider (javax.inject.Provider.get bridge get()Object, flags 0x1041, then get()RecentDatabasesProvider). Library behaviour, INFERRED; library code not read',
  evidence='INFERRED MainActivity.java:157 (field), 1043 (mDatabases.get()); label_083.grep.txt section 3 (Factory class parse: appProvider field and get methods); label_036 pattern')

e('MainActivity.changeDatabase', 'RecentDatabasesProvider_Factory.get', 'CALL',
  'mDatabases.get().get(database.localPath) (MainActivity.java:538) calls the same Lazy, which runs RecentDatabasesProvider_Factory.get on first use',
  cls='non_standard',
  via='dagger.Lazy.get as in the getDatabases edge above (library behaviour, INFERRED)',
  evidence='INFERRED MainActivity.java:157, 538; label_083.grep.txt section 3')

# ---- GUI: page to method (S_SELECT_DATABASE and S_HOME are the pages)
gui('S_SELECT_DATABASE', 'SelectDatabaseActivity.onCreateDatabaseClick',
    'Tap the create-database button (createDatabaseButton, activity_select_database.xml:62); ButterKnife binds it through SelectDatabaseActivity_ViewBinding$1.doClick (generated, auto_calls record SelectDatabaseActivity_ViewBinding.java:38)',
    evidence='SelectDatabaseActivity.java:99-100 (@OnClick(R.id.createDatabaseButton)); res/layout/activity_select_database.xml:62; label_083.grep.txt section 4')

gui('S_SELECT_DATABASE', 'SelectDatabaseActivity.onOpenDatabaseClick',
    'Tap the open-database button (openDatabaseButton, activity_select_database.xml:80); bound through SelectDatabaseActivity_ViewBinding$2.doClick (generated, auto_calls record SelectDatabaseActivity_ViewBinding.java:46)',
    evidence='SelectDatabaseActivity.java:106-107 (@OnClick(R.id.openDatabaseButton)); res/layout/activity_select_database.xml:80; label_083.grep.txt section 4')

gui('S_HOME', 'MyActionBarDrawerToggle.onDrawerOpened',
    'The navigation drawer opens: the home icon (MainActivity.onOptionsItemSelected, openDrawer at MainActivity.java:395, batch 081) or MainActivity.onKeyDown (openDrawer at MainActivity.java:413, batch 081). The DrawerLayout calls the listener, which initializeDrawer adds at MainActivity.java:1297 (batch 080)',
    evidence='MyActionBarDrawerToggle.java:42-45; MainActivity.java:395, 413 (batch 081); MainActivity.java:1296-1297 (batch 080); S_HOME is the page the drawer is shown on (graph_def.py SCREENS)')

gui('S_HOME', 'MyActionBarDrawerToggle.onDrawerClosed',
    'The navigation drawer closes: back press (MainActivity.onBackPressed, closeDrawer at MainActivity.java:442, batch 080), a drawer item tap (closeDrawer at MainActivity.java:948 and 970, batch 080), or MainActivity.onKeyDown (closeDrawer at MainActivity.java:411, batch 081)',
    evidence='MyActionBarDrawerToggle.java:47-50; MainActivity.java:442, 948, 970 (batch 080); MainActivity.java:411 (batch 081); listener added at MainActivity.java:1297')

# ---- sup(): auto CALL records whose caller is UNREACHABLE (D14a)
sup(('MainActivity_MembersInjector.create', 'MainActivity_MembersInjector.<init>'))
sup(('MainActivity_MembersInjector.injectMembers', 'MainActivity_MembersInjector.injectMDatabases'))
sup(('RecentDatabaseEntryComparator.compare', 'DatabaseMetadata.isSynchronised'))

# ================================================================== UNREACHABLE (batch 083). Tuple: (kind, reason, evidence, confirmed_by)

UNREACHABLE['MainActivity_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (javax.inject.Provider argument, class-file flags 0x0001). Its only caller record is create (auto_calls.json, MainActivity_MembersInjector.java:22), and create has no caller: no app source names the injector, and DaggerMmxComponent.class references only injectMDatabases of the injector (label_083.grep.txt sections 1, 3)',
  'python-printed auto_calls record MainActivity_MembersInjector.java:22 (label_083.grep.txt section 4); class-file parse of MainActivity_MembersInjector.class and DaggerMmxComponent.class (section 3)',
  'INFERRED')

UNREACHABLE['MainActivity_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory (class-file flags 0x0009). No caller: DaggerMmxComponent.class references injectMDatabases (DaggerMmxComponent.java:403 in the auto_calls record), not create; no app source reference (label_083.grep.txt sections 1, 3)',
  'class-file parse (label_083.grep.txt section 3); section 2 (only MainActivity_MembersInjector.class and DaggerMmxComponent.class name the injector); no auto_calls record with create as dst',
  'INFERRED')

UNREACHABLE['MainActivity_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance injector, typed to MainActivity (class-file flags 0x0001). No caller: no class file calls injectMembers(MainActivity); the component refers only to injectMDatabases. Its only outgoing record is injectMembers -> injectMDatabases (MainActivity_MembersInjector.java:27), cut by sup()',
  'python-printed auto_calls record MainActivity_MembersInjector.java:27 (section 4); class-file parse (section 3); the synthetic bridge injectMembers(Object)V (flags 0x1041) is an open point, not a row',
  'INFERRED')

UNREACHABLE['MyActionBarDrawerToggle.<init>(AppCompatActivity,DrawerLayout,Toolbar,int,int)'] = ('no_trigger_in_app',
  'Second constructor (with Toolbar). The only app construction is the 4-argument form at MainActivity.java:1296; no other "new MyActionBarDrawerToggle" in app source (grep section 1); no auto_calls record names this constructor (section 4)',
  'MyActionBarDrawerToggle.java:37-40 (declaration); MainActivity.java:1296 (the only app construction, 4-argument form); label_083.grep.txt sections 1, 3, 4',
  'SOURCE')

UNREACHABLE['RecentDatabaseEntryComparator.<init>'] = ('no_trigger_in_app',
  'Implicit default constructor (class-file <init>()V, flags 0x0001). The class is never instantiated: source grep finds only its declaration (RecentDatabaseEntryComparator.java:24), and no class file except its own names it (grep section 2)',
  'RecentDatabaseEntryComparator.java:24-25 (declaration); label_083.grep.txt sections 1, 2, 3',
  'SOURCE')

UNREACHABLE['RecentDatabaseEntryComparator.compare'] = ('no_trigger_in_app',
  'Comparator body (RecentDatabaseEntryComparator.java:48-58). Runs only as a Comparator of DatabaseMetadata, and the comparator is never instantiated (row above). Its auto_calls record compare -> DatabaseMetadata.isSynchronised (line 49) is cut by sup()',
  'RecentDatabaseEntryComparator.java:47-59; python-printed auto_calls record line 49 (section 4); class-file parse (section 3); the synthetic bridge compare(Object,Object)I (flags 0x1041) is an open point',
  'SOURCE')
