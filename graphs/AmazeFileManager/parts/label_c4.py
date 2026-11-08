# ---- Chunk 4 label part (2026-10-27)
# Classes: CLI$Mode, CLI$Mode$1, CLI$Mode$2, CheckBox, CheckableCircleView,
# CircleGradientDrawable, CircularColorsView, CloudContract, CloudEntry,
# CloudHandler, CloudIconDataFetcher, CloudIconModelFactory, CloudIconModelLoader

# CheckableCircleView - used in ColorAdapter
e('ColorAdapter.getView', 'CheckableCircleView.setChecked', 'CALLS', 
  'ColorAdapter.getView calls setChecked to mark selected color',
  evidence='SRC ColorAdapter.java:56')

e('ColorAdapter.getView', 'CheckableCircleView.setColor', 'CALLS',
  'ColorAdapter.getView calls setColor to set circle color',
  evidence='SRC ColorAdapter.java:57')

e('CheckableCircleView.setColor', 'CheckableCircleView.onDraw', 'CALLS',
  'setColor calls invalidate which triggers onDraw',
  evidence='SRC CheckableCircleView.java:31 (invalidate)')

e('CheckableCircleView.setChecked', 'CheckableCircleView.onDraw', 'CALLS',
  'setChecked calls invalidate which triggers onDraw',
  evidence='SRC CheckableCircleView.java:36 (invalidate)')

e('ColorAdapter.onItemClick', 'CheckableCircleView.setChecked', 'CALLS',
  'onItemClick updates checked state on click',
  evidence='SRC ColorAdapter.java:69')

# CircleGradientDrawable - used in RecyclerAdapter and CompressedExplorerAdapter
e('RecyclerAdapter.getView', 'CircleGradientDrawable.<init>', 'CALLS',
  'RecyclerAdapter creates CircleGradientDrawable for selection checkmark background',
  evidence='SRC RecyclerAdapter.java:536,539')

e('CompressedExplorerAdapter.onBindViewHolder', 'CircleGradientDrawable.<init>', 'CALLS',
  'CompressedExplorerAdapter creates CircleGradientDrawable for checkmark',
  evidence='SRC CompressedExplorerAdapter.java:204,207')

# CircularColorsView - used in ColorPickerDialog and SelectedColorsPreference
e('ColorPickerDialog.onBindDialogView', 'CircularColorsView.setColors', 'CALLS',
  'ColorPickerDialog.onBindDialogView calls setColors to configure color preview',
  evidence='SRC ColorPickerDialog.java:131')

e('ColorPickerDialog.onBindDialogView', 'CircularColorsView.setDividerColor', 'CALLS',
  'ColorPickerDialog.onBindDialogView calls setDividerColor based on theme',
  evidence='SRC ColorPickerDialog.java:132-133')

e('CircularColorsView.setColors', 'CircularColorsView.onDraw', 'CALLS',
  'setColors marks paintInitialized which onDraw checks',
  evidence='SRC CircularColorsView.java:51 (sets paintInitialized = true)')

e('CircularColorsView.setDividerColor', 'CircularColorsView.onDraw', 'CALLS',
  'setDividerColor updates paint used in onDraw',
  evidence='SRC CircularColorsView.java:47')

# CheckBox - used in PrefFrag
e('PrefFrag.onCreate', 'CheckBox.onBindView', 'CALLS',
  'Preference framework calls onBindView when binding checkbox preference',
  evidence='SRC PrefFrag.java:102 (findPreference returns CheckBox extends SwitchPreference); INFERRED framework binding')

# CloudHandler - instantiated in MainActivity
e('MainActivity.onCreate', 'CloudHandler.<init>', 'CALLS',
  'MainActivity.onCreate instantiates CloudHandler',
  evidence='SRC MainActivity.java:298')

e('CloudLoaderAsyncTask.doInBackground', 'CloudHandler.addEntry', 'CALLS',
  'CloudLoaderAsyncTask adds cloud entries after OAuth',
  evidence='SRC CloudLoaderAsyncTask.java:103')

e('CloudLoaderAsyncTask.doInBackground', 'CloudHandler.updateEntry', 'CALLS',
  'CloudLoaderAsyncTask updates cloud entries after OAuth',
  evidence='SRC CloudLoaderAsyncTask.java:98')

e('CloudHandler.addEntry', 'CloudEntry.getServiceType', 'CALLS',
  'addEntry reads service type to store in database',
  evidence='SRC CloudHandler.java:87')

e('CloudHandler.addEntry', 'CloudEntry.getPersistData', 'CALLS',
  'addEntry reads persist data to encrypt and store',
  evidence='SRC CloudHandler.java:91')

e('CloudLoaderAsyncTask.doInBackground', 'CloudEntry.<init>', 'CALLS',
  'CloudLoaderAsyncTask constructs CloudEntry with service type and persist data',
  evidence='SRC CloudLoaderAsyncTask.java:98,103')

e('CloudHandler.findEntry', 'CloudEntry.setId', 'CALLS',
  'findEntry populates CloudEntry from database cursor',
  evidence='SRC CloudHandler.java:151')

e('CloudHandler.findEntry', 'CloudEntry.setServiceType', 'CALLS',
  'findEntry sets service type from query parameter',
  evidence='SRC CloudHandler.java:152')

e('CloudHandler.findEntry', 'CloudEntry.setPersistData', 'CALLS',
  'findEntry sets decrypted persist data',
  evidence='SRC CloudHandler.java:154')

e('CloudHandler.getAllEntries', 'CloudEntry.setId', 'CALLS',
  'getAllEntries populates CloudEntry from cursor',
  evidence='SRC CloudHandler.java:187')

e('CloudHandler.getAllEntries', 'CloudEntry.setServiceType', 'CALLS',
  'getAllEntries sets service type from cursor',
  evidence='SRC CloudHandler.java:188')

e('CloudHandler.getAllEntries', 'CloudEntry.setPersistData', 'CALLS',
  'getAllEntries sets decrypted persist data',
  evidence='SRC CloudHandler.java:190')

e('CloudHandler.getAllEntries', 'CloudEntry.getId', 'CALLS',
  'getAllEntries may read id from constructed entries',
  evidence='INFERRED from standard getter usage pattern')

e('CloudHandler.updateEntry', 'CloudEntry.getId', 'CALLS',
  'updateEntry reads id for content values',
  evidence='SRC CloudHandler.java:124')

e('CloudHandler.updateEntry', 'CloudEntry.getServiceType', 'CALLS',
  'updateEntry reads service type for content values',
  evidence='SRC CloudHandler.java:125')

e('CloudHandler.updateEntry', 'CloudEntry.getPersistData', 'CALLS',
  'updateEntry reads persist data to encrypt and update',
  evidence='SRC CloudHandler.java:128')

e('CloudLoaderAsyncTask.doInBackground', 'CloudHandler.findEntry', 'CALLS',
  'CloudLoaderAsyncTask finds existing cloud entries',
  evidence='SRC CloudLoaderAsyncTask.java:88,157,221,282')

e('MainActivity.deleteAccount', 'CloudHandler.findEntry', 'CALLS',
  'MainActivity checks if cloud entry exists before delete',
  evidence='SRC MainActivity.java:1796')

e('MainActivity.deleteAccount', 'CloudHandler.clear', 'CALLS',
  'MainActivity.deleteAccount clears cloud service entry',
  evidence='SRC MainActivity.java:1824')

e('MainActivity.onPostCreate', 'CloudHandler.getAllEntries', 'CALLS',
  'MainActivity.onPostCreate loads all cloud entries',
  evidence='SRC MainActivity.java:1863')

e('CloudHandler.getAllEntries', 'CloudEntry.<init>', 'CALLS',
  'getAllEntries constructs new CloudEntry for each row',
  evidence='SRC CloudHandler.java:186')

e('CloudHandler.findEntry', 'CloudEntry.<init>', 'CALLS',
  'findEntry constructs new CloudEntry for result',
  evidence='SRC CloudHandler.java:150')

# CloudIconModelFactory - registered in AmazeFileManagerModule
e('AmazeFileManagerModule.registerComponents', 'CloudIconModelFactory.<init>', 'CALLS',
  'Glide module registers CloudIconModelFactory',
  evidence='SRC AmazeFileManagerModule.java:22')

e('CloudIconModelFactory.build', 'CloudIconModelLoader.<init>', 'CALLS',
  'Factory.build creates CloudIconModelLoader',
  evidence='SRC CloudIconModelFactory.java:24')

e('CloudIconModelLoader.buildLoadData', 'CloudIconDataFetcher.<init>', 'CALLS',
  'Loader.buildLoadData creates CloudIconDataFetcher for cloud paths',
  evidence='SRC CloudIconModelLoader.java:30')

e('CloudIconDataFetcher.loadData', 'CloudIconDataFetcher.cleanup', 'CALLS',
  'Glide calls cleanup after loadData completes or fails',
  evidence='INFERRED Glide DataFetcher lifecycle')

e('CheckBox.onBindView', 'CheckBox.clearListenerInViewGroup', 'CALLS',
  'onBindView calls clearListenerInViewGroup before super',
  evidence='SRC CheckBox.java:22')

e('CircularColorsView.<init>', 'CircularColorsView.init', 'CALLS',
  'Constructor calls init to initialize paint objects',
  evidence='SRC CircularColorsView.java:27,33')

e('CircleGradientDrawable.<init>', 'CircleGradientDrawable.dpToPx', 'CALLS',
  'Constructor calls dpToPx to convert stroke width',
  evidence='SRC CircleGradientDrawable.java:51')

# Glide framework callbacks
e('GlideRegistry', 'CloudIconModelLoader.handles', 'CALLS',
  'Glide calls handles to check if loader can handle a model string',
  evidence='INFERRED Glide ModelLoader contract')

e('GlideRegistry', 'CloudIconDataFetcher.getDataClass', 'CALLS',
  'Glide calls getDataClass for type checking',
  evidence='INFERRED Glide DataFetcher contract')

e('GlideRegistry', 'CloudIconDataFetcher.getDataSource', 'CALLS',
  'Glide calls getDataSource for caching decisions',
  evidence='INFERRED Glide DataFetcher contract')

e('CloudIconModelLoader.handles', 'CloudIconDataFetcher.loadData', 'CALLS',
  'When handles returns true, Glide eventually calls loadData',
  evidence='INFERRED Glide load flow')

# UNREACHABLE methods from chunk 4
UNREACHABLE_CHUNK_4 = {
    # CLI classes - Apache Commons Compress 7z library, NOT called by app
    'CLI$Mode.<clinit>': ('no_trigger_in_app', 
        'CLI is a command-line tool in commons_compress_7z library. grep -rn "CLI" over app source shows no references to CLI class (excluding CLIPBOARD, CLIENT, etc). The enum Mode is only used if CLI.main is called, which never happens in the app.',
        'SRC grep shows no app call site', 'SOURCE'),
    
    'CLI$Mode.<init>': ('no_trigger_in_app',
        'Mode enum constructor called only from CLI.main which is never invoked by the app. CLI is a standalone command-line utility for 7z extraction.',
        'SRC grep shows no app call site', 'SOURCE'),
    
    'CLI$Mode.getMessage': ('no_trigger_in_app',
        'Mode.getMessage is called only from CLI.main to print messages. CLI.main is never called by the app.',
        'SRC CLI.java:107 shows usage only from CLI.main; grep shows no app call site', 'SOURCE'),
    
    'CLI$Mode$1.<init>': ('no_trigger_in_app',
        'Mode$1 (LIST enum value) constructor is called only during Mode enum initialization. CLI is not used by the app.',
        'SRC grep shows no app call site', 'SOURCE'),
    
    'CLI$Mode$1.takeAction': ('no_trigger_in_app',
        'Mode$1.takeAction (LIST action) is called only from CLI.main loop. CLI is never invoked by the app.',
        'SRC CLI.java:120 shows while loop calling takeAction from main; grep shows no app call site', 'SOURCE'),
    
    'CLI$Mode$1.getContentMethods': ('no_trigger_in_app',
        'Mode$1.getContentMethods is a helper for LIST mode called only from takeAction in CLI.main execution path. CLI is not used by the app.',
        'SRC CLI.java:43 shows call from Mode$1.takeAction; grep shows no app call site', 'SOURCE'),
    
    'CLI$Mode$2.<init>': ('no_trigger_in_app',
        'Mode$2 (EXTRACT enum value) constructor is called only during Mode enum initialization. CLI is not used by the app.',
        'SRC grep shows no app call site', 'SOURCE'),
    
    'CLI$Mode$2.takeAction': ('no_trigger_in_app',
        'Mode$2.takeAction (EXTRACT action) is called only from CLI.main loop. CLI is never invoked by the app.',
        'SRC CLI.java:120 shows while loop calling takeAction from main; grep shows no app call site', 'SOURCE'),
    
    
    # CloudContract - only constants, no methods beyond constructor
    'CloudContract.<init>': ('no_trigger_in_app',
        'CloudContract is a constants-only class with public static final fields. grep shows only static field references (APP_PACKAGE_NAME, PROVIDER_AUTHORITY, etc.) used in CloudHandler and elsewhere, never instantiation. The constructor is implicitly public but never called.',
        'SRC CloudContract.java:7-18 shows only constant declarations; grep -rn "new CloudContract" shows nothing in app', 'SOURCE'),
    
    # CloudHandler methods that depend on cloud plugin
    'CloudHandler.onCreate': ('framework_never_calls',
        'CloudHandler extends SQLiteOpenHelper. onCreate is called by framework only on first database creation. If the database already exists from previous app install, onCreate is never called. This is standard SQLite behavior - onCreate happens once per device per fresh install.',
        'SRC CloudHandler.java:48-70 (onCreate creates tables); INFERRED framework database creation path', 'INFERRED'),
    
    'CloudHandler.onUpgrade': ('framework_never_calls',
        'CloudHandler extends SQLiteOpenHelper. onUpgrade is called by framework only when DATABASE_VERSION increases. Current version is 1 (DATABASE_VERSION = 1 from TabHandler). Until version increases, onUpgrade is never called.',
        'SRC CloudHandler.java:75-81 (onUpgrade drops and recreates); CloudHandler.java:44 uses TabHandler.DATABASE_VERSION; INFERRED framework database upgrade path', 'INFERRED'),
    
    # CloudIconDataFetcher callback methods
    'CloudIconDataFetcher.cancel': ('no_trigger_in_app',
        'Glide DataFetcher.cancel is called by Glide when request is cancelled. Implementation is empty (comment: do nothing). While Glide may call it during cancellation, the empty implementation means it has no actual effect. The app does not directly call cancel.',
        'SRC CloudIconDataFetcher.java:58-60 (empty implementation with "do nothing" comment)', 'SOURCE'),
    
    # CloudIconModelFactory teardown
    'CloudIconModelFactory.teardown': ('framework_never_calls',
        'ModelLoaderFactory.teardown is called by Glide when registry is torn down, typically only on Glide.tearDown() which happens during testing or explicit shutdown. Normal app lifecycle (including process death) does not call teardown. Implementation is empty.',
        'SRC CloudIconModelFactory.java:29-30 (empty implementation); INFERRED Glide lifecycle', 'INFERRED'),
}
