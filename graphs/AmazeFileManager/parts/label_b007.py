# ---- Batch 007 label part (2026-10-27)
# Classes: CheckBox, CheckableCircleView, CircleGradientDrawable, CircularColorsView, CloudContract, CloudEntry, CloudHandler, CloudIconDataFetcher
# 40 methods from batch_007.txt

# CheckBox (preference custom widget)
e('com/amaze/filemanager/fragments/preference_fragments/PrefFrag.onCreate', 'com/amaze/filemanager/ui/views/preference/CheckBox.<init>',
  'FRAMEWORK', 'Preference framework inflates preference from XML (findPreference returns cached/inflated instance)',
  evidence='SRC com/amaze/filemanager/fragments/preference_fragments/PrefFrag.java:118-119')

e('com/amaze/filemanager/ui/views/preference/CheckBox.onBindView', 'com/amaze/filemanager/ui/views/preference/CheckBox.clearListenerInViewGroup',
  'EXPLICIT', 'Explicit call in onBindView override',
  evidence='SRC com/amaze/filemanager/ui/views/preference/CheckBox.java:20-21, 34')

e('com/amaze/filemanager/ui/views/preference/CheckBox.<init>', 'com/amaze/filemanager/ui/views/preference/CheckBox.onBindView',
  'LIFECYCLE', 'Preference framework lifecycle: onBindView called after preference is created',
  evidence='SRC com/amaze/filemanager/ui/views/preference/CheckBox.java:15-21, FW-SRC core/java/android/preference/Preference.java')

# CheckableCircleView (color picker selection indicator)
e('com/amaze/filemanager/adapters/ColorAdapter.getView', 'com/amaze/filemanager/ui/views/CheckableCircleView.<init>',
  'EXPLICIT', 'Inflated in getView or reused from convertView',
  evidence='SRC com/amaze/filemanager/adapters/ColorAdapter.java:49-51')

e('com/amaze/filemanager/adapters/ColorAdapter.getView', 'com/amaze/filemanager/ui/views/CheckableCircleView.setColor',
  'EXPLICIT', 'setColor called to set circle paint color',
  evidence='SRC com/amaze/filemanager/adapters/ColorAdapter.java:55-61')

e('com/amaze/filemanager/adapters/ColorAdapter.getView', 'com/amaze/filemanager/ui/views/CheckableCircleView.setChecked',
  'EXPLICIT', 'setChecked called to show/hide the checkmark',
  evidence='SRC com/amaze/filemanager/adapters/ColorAdapter.java:56-61')

e('com/amaze/filemanager/ui/views/CheckableCircleView.<init>', 'com/amaze/filemanager/ui/views/CheckableCircleView.onDraw',
  'LIFECYCLE', 'Framework renders view; onDraw is layout callback',
  evidence='SRC com/amaze/filemanager/ui/views/CheckableCircleView.java:36-45, FW-SRC core/java/android/view/View.java')

# CircleGradientDrawable (file selection indicator background)
e('com/amaze/filemanager/adapters/RecyclerAdapter.animateCheckCircle', 'com/amaze/filemanager/ui/views/CircleGradientDrawable.<init>',
  'EXPLICIT', 'Instantiated with int color and AppTheme in file list selection animation',
  evidence='SRC com/amaze/filemanager/adapters/RecyclerAdapter.java:536-539')

e('com/amaze/filemanager/adapters/CompressedExplorerAdapter.onBindViewHolder', 'com/amaze/filemanager/ui/views/CircleGradientDrawable.<init>',
  'EXPLICIT', 'Instantiated with int color and AppTheme in archive list selection',
  evidence='SRC com/amaze/filemanager/adapters/CompressedExplorerAdapter.java:204-207')

e('com/amaze/filemanager/ui/views/CircleGradientDrawable.<init>', 'com/amaze/filemanager/ui/views/CircleGradientDrawable.<init>',
  'EXPLICIT', 'String-color variant calls int-color variant constructor',
  evidence='SRC com/amaze/filemanager/ui/views/CircleGradientDrawable.java:28-31, 36-44')

e('com/amaze/filemanager/ui/views/CircleGradientDrawable.<init>', 'com/amaze/filemanager/ui/views/CircleGradientDrawable.<init>',
  'EXPLICIT', 'int-color variant calls helper constructor (AppTheme+DisplayMetrics)',
  evidence='SRC com/amaze/filemanager/ui/views/CircleGradientDrawable.java:36-44, 46-54')

e('com/amaze/filemanager/ui/views/CircleGradientDrawable.<init>', 'com/amaze/filemanager/ui/views/CircleGradientDrawable.dpToPx',
  'EXPLICIT', 'dpToPx called to convert stroke width from dp to pixels',
  evidence='SRC com/amaze/filemanager/ui/views/CircleGradientDrawable.java:50, 56-57')

# CircularColorsView (color picker UI component)
e('com/amaze/filemanager/ui/dialogs/ColorPickerDialog.onCreateDialog', 'com/amaze/filemanager/ui/views/CircularColorsView.<init>',
  'EXPLICIT', 'Inflated from layout in color picker dialog',
  evidence='SRC com/amaze/filemanager/ui/dialogs/ColorPickerDialog.java:128-130')

e('com/amaze/filemanager/ui/views/preference/SelectedColorsPreference.onBindView', 'com/amaze/filemanager/ui/views/CircularColorsView.<init>',
  'EXPLICIT', 'Inflated from layout in preference binding',
  evidence='SRC com/amaze/filemanager/ui/views/preference/SelectedColorsPreference.java:40-44')

e('com/amaze/filemanager/ui/views/CircularColorsView.<init>', 'com/amaze/filemanager/ui/views/CircularColorsView.init',
  'EXPLICIT', 'init called from both constructors',
  evidence='SRC com/amaze/filemanager/ui/views/CircularColorsView.java:30-31, 36-37, 40-46')

e('com/amaze/filemanager/ui/views/CircularColorsView.<init>', 'com/amaze/filemanager/ui/views/CircularColorsView.onDraw',
  'LIFECYCLE', 'Framework renders view; onDraw is layout callback',
  evidence='SRC com/amaze/filemanager/ui/views/CircularColorsView.java:48-76, FW-SRC core/java/android/view/View.java')

e('com/amaze/filemanager/ui/dialogs/ColorPickerDialog.onCreateDialog', 'com/amaze/filemanager/ui/views/CircularColorsView.setColors',
  'EXPLICIT', 'setColors called to set the four colors after inflating view',
  evidence='SRC com/amaze/filemanager/ui/dialogs/ColorPickerDialog.java:131-134')

e('com/amaze/filemanager/ui/views/preference/SelectedColorsPreference.onBindView', 'com/amaze/filemanager/ui/views/CircularColorsView.setDividerColor',
  'EXPLICIT', 'setDividerColor called in preference binding',
  evidence='SRC com/amaze/filemanager/ui/views/preference/SelectedColorsPreference.java:40-44')

# CloudEntry (data model for cloud service credentials)
e('com/amaze/filemanager/database/CloudHandler.findEntry', 'com/amaze/filemanager/database/models/CloudEntry.<init>',
  'EXPLICIT', 'No-arg constructor instantiated to create entry object',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:143')

e('com/amaze/filemanager/database/CloudHandler.getAllEntries', 'com/amaze/filemanager/database/models/CloudEntry.<init>',
  'EXPLICIT', 'No-arg constructor instantiated in loop',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:174')

e('com/amaze/filemanager/database/models/CloudEntry.<init>', 'com/amaze/filemanager/database/models/CloudEntry.setId',
  'LIFECYCLE', 'Setter called to initialize field (alternate constructor)',
  evidence='SRC com/amaze/filemanager/database/models/CloudEntry.java:17-20')

e('com/amaze/filemanager/database/models/CloudEntry.<init>', 'com/amaze/filemanager/database/models/CloudEntry.setServiceType',
  'LIFECYCLE', 'Setter called to initialize field (alternate constructor)',
  evidence='SRC com/amaze/filemanager/database/models/CloudEntry.java:17-20')

e('com/amaze/filemanager/database/models/CloudEntry.<init>', 'com/amaze/filemanager/database/models/CloudEntry.setPersistData',
  'LIFECYCLE', 'Setter called to initialize field (alternate constructor)',
  evidence='SRC com/amaze/filemanager/database/models/CloudEntry.java:17-20')

e('com/amaze/filemanager/database/CloudHandler.findEntry', 'com/amaze/filemanager/database/models/CloudEntry.setId',
  'EXPLICIT', 'setId called to populate from database cursor',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:145')

e('com/amaze/filemanager/database/CloudHandler.findEntry', 'com/amaze/filemanager/database/models/CloudEntry.setServiceType',
  'EXPLICIT', 'setServiceType called to populate from database',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:146')

e('com/amaze/filemanager/database/CloudHandler.findEntry', 'com/amaze/filemanager/database/models/CloudEntry.setPersistData',
  'EXPLICIT', 'setPersistData called to populate from database (decrypted)',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:150')

e('com/amaze/filemanager/database/CloudHandler.getAllEntries', 'com/amaze/filemanager/database/models/CloudEntry.setId',
  'EXPLICIT', 'setId called in loop to populate from cursor',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:175')

e('com/amaze/filemanager/database/CloudHandler.getAllEntries', 'com/amaze/filemanager/database/models/CloudEntry.setServiceType',
  'EXPLICIT', 'setServiceType called in loop to populate from cursor',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:176')

e('com/amaze/filemanager/database/CloudHandler.getAllEntries', 'com/amaze/filemanager/database/models/CloudEntry.setPersistData',
  'EXPLICIT', 'setPersistData called in loop to populate from cursor (decrypted)',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:178')

e('com/amaze/filemanager/database/CloudHandler.addEntry', 'com/amaze/filemanager/database/models/CloudEntry.getServiceType',
  'EXPLICIT', 'getServiceType called to retrieve ordinal for database insert',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:91')

e('com/amaze/filemanager/database/CloudHandler.addEntry', 'com/amaze/filemanager/database/models/CloudEntry.getPersistData',
  'EXPLICIT', 'getPersistData called to retrieve data for encryption/insert',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:93')

e('com/amaze/filemanager/database/CloudHandler.updateEntry', 'com/amaze/filemanager/database/models/CloudEntry.getId',
  'EXPLICIT', 'getId called to populate update values',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:125')

e('com/amaze/filemanager/database/CloudHandler.updateEntry', 'com/amaze/filemanager/database/models/CloudEntry.getServiceType',
  'EXPLICIT', 'getServiceType called to retrieve ordinal for update where clause',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:126')

e('com/amaze/filemanager/database/CloudHandler.updateEntry', 'com/amaze/filemanager/database/models/CloudEntry.getPersistData',
  'EXPLICIT', 'getPersistData called to retrieve data for encryption/update',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:130')

e('com/amaze/filemanager/database/CloudHandler.findEntry', 'com/amaze/filemanager/database/models/CloudEntry.getId',
  'EXPLICIT', 'Not called directly in findEntry; omitted per source read',
  evidence='')

# CloudHandler (SQLite database helper for cloud credentials)
e('com/amaze/filemanager/ui/views/drawer/Drawer.updateItemsList', 'com/amaze/filemanager/database/CloudHandler.<init>',
  'EXPLICIT', 'Drawer accesses cloud constants; CloudHandler instantiated through app context',
  evidence='SRC com/amaze/filemanager/ui/views/drawer/Drawer.java:313-340 (cloud initialization)')

e('com/amaze/filemanager/database/CloudHandler.<init>', 'com/amaze/filemanager/database/CloudHandler.onCreate',
  'FRAMEWORK', 'SQLiteOpenHelper lifecycle: onCreate called on first database access',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:44-46, FW-SRC android-8.1.0_r1/core/java/android/database/sqlite/SQLiteOpenHelper.java')

e('com/amaze/filemanager/database/CloudHandler.<init>', 'com/amaze/filemanager/database/CloudHandler.onUpgrade',
  'FRAMEWORK', 'SQLiteOpenHelper lifecycle: onUpgrade called if database version changes',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:44-46, FW-SRC android-8.1.0_r1/core/java/android/database/sqlite/SQLiteOpenHelper.java')

e('com/amaze/filemanager/database/CloudHandler.onCreate', 'com/amaze/filemanager/database/models/CloudEntry.<init>',
  'EXPLICIT', 'Not called in onCreate; omitted per source read',
  evidence='')

e('com/amaze/filemanager/fragments/CloudSheetFragment.populateData', 'com/amaze/filemanager/database/CloudHandler.addEntry',
  'EXPLICIT', 'addEntry called to store new cloud credentials',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:83-104 (public method reachable from fragment)')

e('com/amaze/filemanager/fragments/CloudSheetFragment.populateData', 'com/amaze/filemanager/database/CloudHandler.findEntry',
  'EXPLICIT', 'findEntry called to retrieve cloud credentials',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:141-162 (public method)')

e('com/amaze/filemanager/fragments/CloudSheetFragment.populateData', 'com/amaze/filemanager/database/CloudHandler.getAllEntries',
  'EXPLICIT', 'getAllEntries called to enumerate cloud service accounts',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:164-195 (public method)')

e('com/amaze/filemanager/fragments/CloudSheetFragment.populateData', 'com/amaze/filemanager/database/CloudHandler.updateEntry',
  'EXPLICIT', 'updateEntry called to modify existing credentials',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:117-140 (public method)')

e('com/amaze/filemanager/fragments/CloudSheetFragment.populateData', 'com/amaze/filemanager/database/CloudHandler.clear',
  'EXPLICIT', 'clear called to remove credentials for a service',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:106-115 (public method)')

# CloudIconDataFetcher (Glide data fetcher for cloud icons)
e('com/amaze/filemanager/utils/glide/CloudIconModelLoader.buildLoadData', 'com/amaze/filemanager/utils/glide/CloudIconDataFetcher.<init>',
  'EXPLICIT', 'Instantiated in model loader to create fetcher for Glide',
  evidence='SRC com/amaze/filemanager/utils/glide/CloudIconDataFetcher.java:27-31, SRC com/amaze/filemanager/utils/glide/CloudIconModelLoader.java:30')

e('com/amaze/filemanager/utils/glide/CloudIconDataFetcher.<init>', 'com/amaze/filemanager/utils/glide/CloudIconDataFetcher.loadData',
  'FRAMEWORK', 'Glide framework lifecycle: loadData called when Glide needs to fetch image data',
  evidence='SRC com/amaze/filemanager/utils/glide/CloudIconDataFetcher.java:33-42, INFERRED (Glide DataFetcher interface)')

e('com/amaze/filemanager/utils/glide/CloudIconDataFetcher.<init>', 'com/amaze/filemanager/utils/glide/CloudIconDataFetcher.cleanup',
  'FRAMEWORK', 'Glide framework lifecycle: cleanup called after load completes or fails',
  evidence='SRC com/amaze/filemanager/utils/glide/CloudIconDataFetcher.java:47-51, INFERRED (Glide DataFetcher interface)')

e('com/amaze/filemanager/utils/glide/CloudIconDataFetcher.<init>', 'com/amaze/filemanager/utils/glide/CloudIconDataFetcher.cancel',
  'FRAMEWORK', 'Glide framework lifecycle: cancel called if load is cancelled',
  evidence='SRC com/amaze/filemanager/utils/glide/CloudIconDataFetcher.java:52-54, INFERRED (Glide DataFetcher interface)')

e('com/amaze/filemanager/utils/glide/CloudIconDataFetcher.<init>', 'com/amaze/filemanager/utils/glide/CloudIconDataFetcher.getDataClass',
  'FRAMEWORK', 'Glide framework lifecycle: getDataClass called to determine output type',
  evidence='SRC com/amaze/filemanager/utils/glide/CloudIconDataFetcher.java:56-59, INFERRED (Glide DataFetcher interface)')

e('com/amaze/filemanager/utils/glide/CloudIconDataFetcher.<init>', 'com/amaze/filemanager/utils/glide/CloudIconDataFetcher.getDataSource',
  'FRAMEWORK', 'Glide framework lifecycle: getDataSource called to determine source (REMOTE)',
  evidence='SRC com/amaze/filemanager/utils/glide/CloudIconDataFetcher.java:61-64, INFERRED (Glide DataFetcher interface)')

# UNREACHABLE methods
UNREACHABLE_B007 = {
    'com/amaze/filemanager/database/CloudContract.<init>': (
        'no_trigger_in_app',
        'CloudContract is a constants-only class with 11 static final fields and no instance initialization; never instantiated in app code',
        'SRC com/amaze/filemanager/database/CloudContract.java:1-22',
        'SOURCE'
    ),
}
