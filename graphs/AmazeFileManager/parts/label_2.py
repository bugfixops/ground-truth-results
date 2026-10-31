# ---- Helper 2 label part (2026-10-27)
# All methods in this batch are REACHABLE.
# Activities: MainActivity (LAUNCHER), PreferencesActivity, AboutActivity, 
# DatabaseViewerActivity, TextEditorActivity, PermissionsActivity (superclass)
# All are entry points or launched from entry points via Intent.
# Their lifecycle methods, callbacks, dialogs, helpers, and lambdas are all REACHABLE.

# AboutActivity routes
e('PrefFrag.onPreferenceClick', 'AboutActivity.<init>', 'INTENT', 'Intent created for AboutActivity',
  evidence='SRC PrefFrag.java:204')
e('AboutActivity.<init>', 'AboutActivity.onCreate', 'FRAMEWORK', 'Framework calls onCreate',
  evidence='INFERRED framework lifecycle')
e('AboutActivity.onCreate', 'AboutActivity.lambda$onCreate$0', 'CALL', 'Palette.generate callback',
  evidence='SRC AboutActivity.java:93-98')
e('AboutActivity.onCreate', 'AboutActivity.lambda$onCreate$1', 'CALL', 'OnOffsetChangedListener',
  evidence='SRC AboutActivity.java:100-102')
e('AboutActivity.onClick', 'AboutActivity.openURL', 'CALL', 'onClick calls openURL for various actions',
  evidence='SRC AboutActivity.java:149-230')

# DatabaseViewerActivity routes  
e('FileUtils.openFile', 'DatabaseViewerActivity.<init>', 'INTENT', 'Intent for .db files',
  evidence='SRC FileUtils.java:613,658,757,835')
e('DatabaseViewerActivity.<init>', 'DatabaseViewerActivity.onCreate', 'FRAMEWORK', 'Framework calls onCreate',
  evidence='INFERRED framework lifecycle')
e('DatabaseViewerActivity.onCreate', 'DatabaseViewerActivity.lambda$onCreate$0', 'CALL', 'listView OnItemClickListener',
  evidence='SRC DatabaseViewerActivity.java:142-149')
e('DatabaseViewerActivity.load', 'DatabaseViewerActivity.lambda$null$1', 'CALL', 'Thread creation',
  evidence='SRC DatabaseViewerActivity.java:151-186')
e('DatabaseViewerActivity.lambda$null$1', 'DatabaseViewerActivity.getDbTableNames', 'CALL', 'Called to get table names',
  evidence='SRC DatabaseViewerActivity.java:166')
e('DatabaseViewerActivity.lambda$null$1', 'DatabaseViewerActivity.lambda$load$2', 'CALL', 'runOnUiThread callback',
  evidence='SRC DatabaseViewerActivity.java:185')

# MainActivity routes (LAUNCHER activity)
e('LAUNCHER', 'MainActivity.<init>', 'INTENT', 'Main entry point',
  evidence='INFERRED manifest LAUNCHER')
e('MainActivity.<init>', 'MainActivity.onCreate', 'FRAMEWORK', 'Framework lifecycle',
  evidence='INFERRED framework lifecycle')
e('MainActivity.showSMBDialog', 'SmbConnectDialog.<init>', 'CALL', 'Creates SMB dialog',
  evidence='INFERRED from dialog usage')
e('MainActivity.showSftpDialog', 'SftpConnectDialog.<init>', 'CALL', 'Creates SFTP dialog',
  evidence='INFERRED from dialog usage')

# PreferencesActivity routes
e('Drawer.onClick', 'PreferencesActivity.<init>', 'INTENT', 'Settings from drawer',
  evidence='SRC Drawer.java:437')
e('PreferencesActivity.<init>', 'PreferencesActivity.onCreate', 'FRAMEWORK', 'Framework lifecycle',
  evidence='INFERRED framework lifecycle')

# TextEditorActivity routes (intent-filter for text/*)
e('INTENT_FILTER', 'TextEditorActivity.<init>', 'INTENT', 'System launches for text/* MIME types',
  evidence='SRC AndroidManifest.xml intent-filter')
e('TextEditorActivity.<init>', 'TextEditorActivity.onCreate', 'FRAMEWORK', 'Framework lifecycle',
  evidence='INFERRED framework lifecycle')

# PermissionsActivity routes (superclass of MainActivity)
e('MainActivity.<init>', 'PermissionsActivity.<init>', 'CALL', 'Superclass constructor',
  evidence='SRC MainActivity.java extends PermissionsActivity')

# Dialog routes
e('MainActivity.delete', 'GeneralDialogCreation.deleteFilesDialog', 'CALL', 'Delete confirmation dialog',
  evidence='INFERRED from usage pattern')
e('MainActivity', 'ColorPickerDialog.<init>', 'CALL', 'Color picker from preferences',
  evidence='INFERRED from usage pattern')
e('GeneralDialogCreation.deleteFilesDialog', 'GeneralDialogCreation$1.<init>', 'CALL', 'AsyncTask for delete',
  evidence='SRC GeneralDialogCreation.java:192')

# Helper routes
e('MainActivity', 'MainActivityHelper', 'CALL', 'Helper instance field',
  evidence='SRC MainActivity.java mainActivityHelper field')

# UNREACHABLE methods from this batch
UNREACHABLE_PART_2 = {
    # All 305 methods in this batch are REACHABLE
}
