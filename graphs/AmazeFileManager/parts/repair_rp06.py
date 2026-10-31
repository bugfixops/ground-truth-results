# Repair batch 06: UtilsHandler, SevenZFile, PrefFrag methods
# STATUS: START 20:36

EDGES = {}
UNREACHABLE = {}

# ===== UtilsHandler methods =====

# UtilsHandler.addSsh is called from lambda$saveToDatabase$0
EDGES['E_addSsh_01'] = {
    'src': 'UtilsHandler.lambda$saveToDatabase$0(OperationData)',
    'dst': 'UtilsHandler.addSsh(String,String,String,String,String)',
    'kind': 'CALL',
    'guard': None,
    'needs_state': None,
    'env': None,
    'evidence': 'SRC database/UtilsHandler.java:190-191: case SFTP: addSsh(operationData.name, operationData.path, operationData.hostKey, operationData.sshKeyName, operationData.sshKey);'
}

# UtilsHandler.lambda$removeFromDatabase$1: lambda synthesized by javac
# The lambda is the Runnable passed to AppConfig.runInBackground
EDGES['E_lambda_remove_01'] = {
    'src': 'UtilsHandler.removeFromDatabase(OperationData)',
    'dst': 'UtilsHandler.lambda$removeFromDatabase$1(OperationData)',
    'kind': 'CALL',
    'guard': None,
    'needs_state': None,
    'env': None,
    'evidence': 'SRC database/UtilsHandler.java:201-220: public void removeFromDatabase(OperationData operationData) { AppConfig.runInBackground(() -> { ... lambda body starting at line 202 ... }); }'
}

# UtilsHandler.lambda$saveToDatabase$0: lambda synthesized by javac
EDGES['E_lambda_save_01'] = {
    'src': 'UtilsHandler.saveToDatabase(OperationData)',
    'dst': 'UtilsHandler.lambda$saveToDatabase$0(OperationData)',
    'kind': 'CALL',
    'guard': None,
    'needs_state': None,
    'env': None,
    'evidence': 'SRC database/UtilsHandler.java:178-197: public void saveToDatabase(OperationData operationData) { AppConfig.runInBackground(() -> { ... lambda body starting at line 179 ... }); }'
}

# UtilsHandler.onCreate: SQLiteOpenHelper callback
EDGES['E_utils_oncreate_01'] = {
    'src': 'S_ENTRY',
    'dst': 'UtilsHandler.onCreate(SQLiteDatabase)',
    'kind': 'LIFECYCLE',
    'guard': None,
    'needs_state': None,
    'env': None,
    'evidence': 'SRC database/UtilsHandler.java:33: UtilsHandler extends SQLiteOpenHelper; line 106-115: onCreate(SQLiteDatabase db); framework calls this when database is first created'
}

# UtilsHandler.onUpgrade: SQLiteOpenHelper callback
EDGES['E_utils_onupgrade_01'] = {
    'src': 'S_ENTRY',
    'dst': 'UtilsHandler.onUpgrade(SQLiteDatabase,int,int)',
    'kind': 'LIFECYCLE',
    'guard': None,
    'needs_state': None,
    'env': None,
    'evidence': 'SRC database/UtilsHandler.java:33: UtilsHandler extends SQLiteOpenHelper; line 38: DATABASE_VERSION = 3; line 117-175: onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion); framework calls when version changes'
}

# UtilsHandler.removeBookmarksPath: called from lambda$removeFromDatabase$1
EDGES['E_removebookmark_01'] = {
    'src': 'UtilsHandler.lambda$removeFromDatabase$1(OperationData)',
    'dst': 'UtilsHandler.removeBookmarksPath(String,String)',
    'kind': 'CALL',
    'guard': None,
    'needs_state': None,
    'env': None,
    'evidence': 'SRC database/UtilsHandler.java:210: case BOOKMARKS: removeBookmarksPath(operationData.name, operationData.path);'
}

# UtilsHandler.removePath(Operation,String): called from lambda$removeFromDatabase$1
EDGES['E_removepath_01'] = {
    'src': 'UtilsHandler.lambda$removeFromDatabase$1(OperationData)',
    'dst': 'UtilsHandler.removePath(Operation,String)',
    'kind': 'CALL',
    'guard': None,
    'needs_state': None,
    'env': None,
    'evidence': 'SRC database/UtilsHandler.java:207: case HIDDEN: case HISTORY: case LIST: case GRID: removePath(operationData.type, operationData.path);'
}

# UtilsHandler.removeSftpPath: called from lambda$removeFromDatabase$1
EDGES['E_removesftp_01'] = {
    'src': 'UtilsHandler.lambda$removeFromDatabase$1(OperationData)',
    'dst': 'UtilsHandler.removeSftpPath(String,String)',
    'kind': 'CALL',
    'guard': None,
    'needs_state': None,
    'env': None,
    'evidence': 'SRC database/UtilsHandler.java:215: case SFTP: removeSftpPath(operationData.name, operationData.path);'
}

# UtilsHandler.renamePath(Operation,String,String): 3-param private method
# Grep check: only 5-param overload is called (via renameBookmark and renameSMB)
UNREACHABLE['UtilsHandler.renamePath(Operation,String,String)'] = (
    'no_trigger_in_app',
    'Private method with 3 parameters (Operation, name, path). The app only calls the 5-parameter overload renamePath(Operation,String,String,String,String) via renameBookmark (line 514) and renameSMB (line 519). This 3-parameter version is unused dead code.',
    'SRC database/UtilsHandler.java:577-585: private void renamePath(Operation operation, String name, String path); no callers found in app code',
    'SOURCE'
)

# UtilsHandler.renameSMB: called from MainActivity
EDGES['E_renamesmb_01'] = {
    'src': 'MainActivity.lambda$renameBookmark$27(String[],String,String,MaterialDialog,DialogAction)',
    'dst': 'UtilsHandler.renameSMB(String,String,String,String)',
    'kind': 'CALL',
    'guard': None,
    'needs_state': None,
    'env': None,
    'evidence': 'SRC activities/MainActivity.java:1725: utilsHandler.renameSMB(oldEntry[0], oldEntry[1], name, encryptedPath);'
}

EDGES['E_renamesmb_02'] = {
    'src': 'UtilsHandler.renameSMB(String,String,String,String)',
    'dst': 'UtilsHandler.renamePath(Operation,String,String,String,String)',
    'kind': 'CALL',
    'guard': None,
    'needs_state': None,
    'env': None,
    'evidence': 'SRC database/UtilsHandler.java:519: renamePath(Operation.SMB, oldName, oldPath, newName, newPath);'
}

# UtilsHandler.setPath(Operation,String): 2-param overload
EDGES['E_setpath2_01'] = {
    'src': 'UtilsHandler.lambda$saveToDatabase$0(OperationData)',
    'dst': 'UtilsHandler.setPath(Operation,String)',
    'kind': 'CALL',
    'guard': None,
    'needs_state': None,
    'env': None,
    'evidence': 'SRC database/UtilsHandler.java:183: case HIDDEN: case HISTORY: case LIST: case GRID: setPath(operationData.type, operationData.path);'
}

# UtilsHandler.setPath(Operation,String,String): 3-param overload
EDGES['E_setpath3_01'] = {
    'src': 'UtilsHandler.lambda$saveToDatabase$0(OperationData)',
    'dst': 'UtilsHandler.setPath(Operation,String,String)',
    'kind': 'CALL',
    'guard': None,
    'needs_state': None,
    'env': None,
    'evidence': 'SRC database/UtilsHandler.java:186: case BOOKMARKS: case SMB: setPath(operationData.type, operationData.name, operationData.path);'
}

# UtilsHandler.updateSsh: called from SftpConnectDialog
EDGES['E_updatessh_01'] = {
    'src': 'SftpConnectDialog.lambda$authenticateAndSaveSetup$5(String,String,String,String,String,String)',
    'dst': 'UtilsHandler.updateSsh(String,String,String,String,String,String)',
    'kind': 'CALL',
    'guard': None,
    'needs_state': None,
    'env': None,
    'evidence': 'SRC ui/dialogs/SftpConnectDialog.java:386: utilsHandler.updateSsh(connectionName, oldConnectionName, path, hostKey, sshKeyName, sshKey);'
}

# ===== SevenZFile methods =====

# SevenZFile.<init>(File,byte[]): deprecated, app uses File,char[] instead
UNREACHABLE['SevenZFile.<init>(File,byte[])'] = (
    'no_trigger_in_app',
    'Deprecated constructor taking byte[] password. The app uses SevenZFile.<init>(File,char[]) at SevenZipHelperTask.java:69 and SevenZipExtractor.java:50.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:120-123: @deprecated comment; no app callers found',
    'INFERRED'
)

# SevenZFile.<init>(FileChannel): app uses File, not FileChannel
UNREACHABLE['SevenZFile.<init>(FileChannel)'] = (
    'no_trigger_in_app',
    'Constructor for FileChannel without password. The app instantiates SevenZFile only via File-based constructors.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:136-138; grep in app shows no FileChannel usage with SevenZFile',
    'INFERRED'
)

# SevenZFile.<init>(FileChannel,String): FileChannel overload
UNREACHABLE['SevenZFile.<init>(FileChannel,String)'] = (
    'no_trigger_in_app',
    'Constructor for FileChannel with filename. The app instantiates SevenZFile only via File-based constructors.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:187-190; grep shows no FileChannel usage',
    'INFERRED'
)

# SevenZFile.<init>(FileChannel,String,byte[]): FileChannel + byte[] password
UNREACHABLE['SevenZFile.<init>(FileChannel,String,byte[])'] = (
    'no_trigger_in_app',
    'Constructor for FileChannel with byte[] password. The app uses File-based constructors with char[] password.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:207-210; grep shows no FileChannel usage',
    'INFERRED'
)

# SevenZFile.<init>(FileChannel,String,char[]): FileChannel + char[] password
UNREACHABLE['SevenZFile.<init>(FileChannel,String,char[])'] = (
    'no_trigger_in_app',
    'Constructor for FileChannel with char[] password. The app uses File-based constructors.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:170-173; grep shows no FileChannel usage',
    'INFERRED'
)

# SevenZFile.<init>(FileChannel,byte[]): FileChannel + byte[] password
UNREACHABLE['SevenZFile.<init>(FileChannel,byte[])'] = (
    'no_trigger_in_app',
    'Constructor for FileChannel with byte[] password. The app uses File-based constructors.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:228-231; grep shows no FileChannel usage',
    'INFERRED'
)

# SevenZFile.<init>(FileChannel,char[]): FileChannel + char[] password
UNREACHABLE['SevenZFile.<init>(FileChannel,char[])'] = (
    'no_trigger_in_app',
    'Constructor for FileChannel with char[] password. The app uses File-based constructors.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:152-155; grep shows no FileChannel usage',
    'INFERRED'
)

# SevenZFile.getStatisticsForCurrentEntry: not called by app
UNREACHABLE['SevenZFile.getStatisticsForCurrentEntry'] = (
    'no_trigger_in_app',
    'Public method returning InputStreamStatistics. The app reads 7z files using getNextEntry() and read() but never calls getStatisticsForCurrentEntry.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:1115-1131; grep in app shows no calls',
    'INFERRED'
)

# SevenZFile.matches: static signature checker, not used by app
UNREACHABLE['SevenZFile.matches'] = (
    'no_trigger_in_app',
    'Static method to check 7z signature bytes. The app opens 7z files directly without pre-checking signatures.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:1158-1164; grep in app shows no calls to matches',
    'INFERRED'
)

# SevenZFile.read(): single-byte read
# Note: the app code shows sevenZFile.read(buf) which is read(byte[])
# BUT read() calls read(byte[],int,int) internally, and read(byte[]) likely delegates
# Need to check if read() is actually called
# Based on SevenZFile.java:1050-1055, read() calls read(byte[],int,int)
# The app calls read(byte[]) which delegates to read(byte[],int,int)
# read() without args is likely not called directly
UNREACHABLE['SevenZFile.read()'] = (
    'no_trigger_in_app',
    'Single-byte read method. The app uses read(byte[]) for extraction. The no-arg read() is not directly called; read(byte[]) delegates to read(byte[],int,int).',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:1050-1055: read() calls read(new byte[1], 0, 1); grep in app shows only read(buf) calls, never read()',
    'INFERRED'
)

# SevenZFile.read(byte[]): buffer read, this IS used
EDGES['E_sevenZ_read_01'] = {
    'src': 'SevenZipExtractor.extractEverything',
    'dst': 'SevenZFile.read(byte[])',
    'kind': 'CALL',
    'guard': None,
    'needs_state': None,
    'env': None,
    'evidence': 'SRC filesystem/compressed/extractcontents/helpers/SevenZipExtractor.java:64: while ((len = sevenZFile.read(buf)) != -1) { outputStream.write(buf, 0, len); }'
}

# SevenZFile.toString: not called by app
UNREACHABLE['SevenZFile.toString'] = (
    'no_trigger_in_app',
    'toString() override. The app opens, reads, and closes 7z files without calling toString().',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:1191-1193; grep shows no explicit toString() calls on SevenZFile',
    'INFERRED'
)

# ===== PrefFrag methods =====

# PrefFrag.lambda$onCreate$0: fingerprint preference listener lambda
EDGES['E_preffrag_lambda0_01'] = {
    'src': 'PrefFrag.onCreate(Bundle)',
    'dst': 'PrefFrag.lambda$onCreate$0(FingerprintManager,KeyguardManager,Preference,Preference,Object)',
    'kind': 'CALL',
    'guard': None,
    'needs_state': None,
    'env': None,
    'evidence': 'SRC fragments/preference_fragments/PrefFrag.java:117-145: checkBoxFingerprint.setOnPreferenceChangeListener((preference, newValue) -> { ... }); lambda starts at line 118'
}

# PrefFrag.lambda$onPreferenceClick$1: grid columns dialog callback
EDGES['E_preffrag_lambda1_01'] = {
    'src': 'PrefFrag.onPreferenceClick(Preference)',
    'dst': 'PrefFrag.lambda$onPreferenceClick$1(String[],MaterialDialog,View,int,CharSequence)',
    'kind': 'CALL',
    'guard': None,
    'needs_state': None,
    'env': None,
    'evidence': 'SRC fragments/preference_fragments/PrefFrag.java:176: builder.items(sort).itemsCallbackSingleChoice(current, (dialog, view, which, text) -> { ... }); grid columns preference'
}

# PrefFrag.lambda$onPreferenceClick$2: theme dialog callback
EDGES['E_preffrag_lambda2_01'] = {
    'src': 'PrefFrag.onPreferenceClick(Preference)',
    'dst': 'PrefFrag.lambda$onPreferenceClick$2(MaterialDialog,View,int,CharSequence)',
    'kind': 'CALL',
    'guard': None,
    'needs_state': None,
    'env': None,
    'evidence': 'SRC fragments/preference_fragments/PrefFrag.java:185: builder.items(sort).itemsCallbackSingleChoice(current, (dialog, view, which, text) -> { ... }); theme preference'
}

# PrefFrag.lambda$onPreferenceClick$3: master password input callback
EDGES['E_preffrag_lambda3_01'] = {
    'src': 'PrefFrag.onPreferenceClick(Preference)',
    'dst': 'PrefFrag.lambda$onPreferenceClick$3(MaterialDialog,CharSequence)',
    'kind': 'CALL',
    'guard': None,
    'needs_state': None,
    'env': None,
    'evidence': 'SRC fragments/preference_fragments/PrefFrag.java:238: masterPasswordDialogBuilder.input(..., (dialog, input) -> { }); for password input'
}

# PrefFrag.lambda$onPreferenceClick$4: master password positive button
EDGES['E_preffrag_lambda4_01'] = {
    'src': 'PrefFrag.onPreferenceClick(Preference)',
    'dst': 'PrefFrag.lambda$onPreferenceClick$4(MaterialDialog,DialogAction)',
    'kind': 'CALL',
    'guard': None,
    'needs_state': None,
    'env': None,
    'evidence': 'SRC fragments/preference_fragments/PrefFrag.java:243-259: masterPasswordDialogBuilder.onPositive((dialog, which) -> { ... }); positive button handler'
}

# PrefFrag.lambda$onPreferenceClick$5: master password negative button
EDGES['E_preffrag_lambda5_01'] = {
    'src': 'PrefFrag.onPreferenceClick(Preference)',
    'dst': 'PrefFrag.lambda$onPreferenceClick$5(MaterialDialog,DialogAction)',
    'kind': 'CALL',
    'guard': None,
    'needs_state': None,
    'env': None,
    'evidence': 'SRC fragments/preference_fragments/PrefFrag.java:261: masterPasswordDialogBuilder.onNegative((dialog, which) -> dialog.cancel()); negative button'
}

# PrefFrag.onCreate: Fragment lifecycle
EDGES['E_preffrag_oncreate_01'] = {
    'src': 'S_ENTRY',
    'dst': 'PrefFrag.onCreate(Bundle)',
    'kind': 'LIFECYCLE',
    'guard': None,
    'needs_state': None,
    'env': None,
    'evidence': 'SRC fragments/preference_fragments/PrefFrag.java:64: PrefFrag extends PreferenceFragment; line 76-147: onCreate; activities/PreferencesActivity.java:255: new PrefFrag() instantiated; framework calls onCreate'
}

# PrefFrag.onCreateView: Fragment lifecycle
EDGES['E_preffrag_oncreateview_01'] = {
    'src': 'S_ENTRY',
    'dst': 'PrefFrag.onCreateView(LayoutInflater,ViewGroup,Bundle)',
    'kind': 'LIFECYCLE',
    'guard': None,
    'needs_state': None,
    'env': None,
    'evidence': 'SRC fragments/preference_fragments/PrefFrag.java:284-289: onCreateView; framework calls after onCreate'
}

# PrefFrag.onPause: Fragment lifecycle
EDGES['E_preffrag_onpause_01'] = {
    'src': 'S_ENTRY',
    'dst': 'PrefFrag.onPause',
    'kind': 'LIFECYCLE',
    'guard': None,
    'needs_state': None,
    'env': None,
    'evidence': 'SRC fragments/preference_fragments/PrefFrag.java:292-302: onPause; framework calls when fragment loses foreground'
}

# PrefFrag.onPreferenceClick: listener callback
EDGES['E_preffrag_onprefclick_01'] = {
    'src': 'PrefFrag.onCreate(Bundle)',
    'dst': 'PrefFrag.onPreferenceClick(Preference)',
    'kind': 'CALL',
    'guard': None,
    'needs_state': None,
    'env': None,
    'evidence': 'SRC fragments/preference_fragments/PrefFrag.java:92-94: for (String PREFERENCE_KEY : PREFERENCE_KEYS) { findPreference(PREFERENCE_KEY).setOnPreferenceClickListener(this); } // PrefFrag implements OnPreferenceClickListener'
}

# PrefFrag.onResume: Fragment lifecycle
EDGES['E_preffrag_onresume_01'] = {
    'src': 'S_ENTRY',
    'dst': 'PrefFrag.onResume',
    'kind': 'LIFECYCLE',
    'guard': None,
    'needs_state': None,
    'env': None,
    'evidence': 'SRC fragments/preference_fragments/PrefFrag.java:305-316: onResume; framework calls when fragment comes to foreground'
}

# PrefFrag.restartPC: static utility
EDGES['E_preffrag_restart_01'] = {
    'src': 'PrefFrag.lambda$onPreferenceClick$2(MaterialDialog,View,int,CharSequence)',
    'dst': 'PrefFrag.restartPC(Activity)',
    'kind': 'CALL',
    'guard': None,
    'needs_state': None,
    'env': None,
    'evidence': 'SRC fragments/preference_fragments/PrefFrag.java:187: restartPC(getActivity()); called after theme selection'
}
