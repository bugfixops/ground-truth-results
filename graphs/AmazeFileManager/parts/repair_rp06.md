# Repair batch 06: Method labeling results

STATUS: START 20:36
STATUS: DONE 20:41

## Summary

- Total methods: 37
- REACHABLE: 25
- UNREACHABLE: 12
- INCOMPLETE: 0

## Method details

### REACHABLE (25 methods)

| Method | Evidence lines |
|--------|---------------|
| UtilsHandler.addSsh(String,String,String,String,String) | SRC database/UtilsHandler.java:190-191, 241-254 |
| UtilsHandler.lambda$removeFromDatabase$1(OperationData) | SRC database/UtilsHandler.java:201-220 |
| UtilsHandler.lambda$saveToDatabase$0(OperationData) | SRC database/UtilsHandler.java:178-197 |
| UtilsHandler.onCreate(SQLiteDatabase) | SRC database/UtilsHandler.java:33, 106-115; SQLiteOpenHelper lifecycle |
| UtilsHandler.onUpgrade(SQLiteDatabase,int,int) | SRC database/UtilsHandler.java:33, 38, 117-175; SQLiteOpenHelper lifecycle |
| UtilsHandler.removeBookmarksPath(String,String) | SRC database/UtilsHandler.java:210, 456-462 |
| UtilsHandler.removePath(Operation,String) | SRC database/UtilsHandler.java:207, 565-572 |
| UtilsHandler.removeSftpPath(String,String) | SRC database/UtilsHandler.java:215, 490-515 |
| UtilsHandler.renameSMB(String,String,String,String) | SRC activities/MainActivity.java:1725; SRC database/UtilsHandler.java:518-520 |
| UtilsHandler.setPath(Operation,String) | SRC database/UtilsHandler.java:183, 522-531 |
| UtilsHandler.setPath(Operation,String,String) | SRC database/UtilsHandler.java:186, 533-541 |
| UtilsHandler.updateSsh(String,String,String,String,String,String) | SRC ui/dialogs/SftpConnectDialog.java:386; SRC database/UtilsHandler.java:256-272 |
| SevenZFile.read(byte[]) | SRC filesystem/compressed/extractcontents/helpers/SevenZipExtractor.java:64 |
| PrefFrag.lambda$onCreate$0(FingerprintManager,KeyguardManager,Preference,Preference,Object) | SRC fragments/preference_fragments/PrefFrag.java:117-145 |
| PrefFrag.lambda$onPreferenceClick$1(String[],MaterialDialog,View,int,CharSequence) | SRC fragments/preference_fragments/PrefFrag.java:176 |
| PrefFrag.lambda$onPreferenceClick$2(MaterialDialog,View,int,CharSequence) | SRC fragments/preference_fragments/PrefFrag.java:185, 187 |
| PrefFrag.lambda$onPreferenceClick$3(MaterialDialog,CharSequence) | SRC fragments/preference_fragments/PrefFrag.java:238 |
| PrefFrag.lambda$onPreferenceClick$4(MaterialDialog,DialogAction) | SRC fragments/preference_fragments/PrefFrag.java:243-259 |
| PrefFrag.lambda$onPreferenceClick$5(MaterialDialog,DialogAction) | SRC fragments/preference_fragments/PrefFrag.java:261 |
| PrefFrag.onCreate(Bundle) | SRC fragments/preference_fragments/PrefFrag.java:64, 76-147; SRC activities/PreferencesActivity.java:255 |
| PrefFrag.onCreateView(LayoutInflater,ViewGroup,Bundle) | SRC fragments/preference_fragments/PrefFrag.java:284-289; Fragment lifecycle |
| PrefFrag.onPause | SRC fragments/preference_fragments/PrefFrag.java:292-302; Fragment lifecycle |
| PrefFrag.onPreferenceClick(Preference) | SRC fragments/preference_fragments/PrefFrag.java:92-94, 149-263 |
| PrefFrag.onResume | SRC fragments/preference_fragments/PrefFrag.java:305-316; Fragment lifecycle |
| PrefFrag.restartPC(Activity) | SRC fragments/preference_fragments/PrefFrag.java:187, 268-277 |

### UNREACHABLE (12 methods)

| Method | Kind | Evidence lines |
|--------|------|---------------|
| UtilsHandler.renamePath(Operation,String,String) | no_trigger_in_app | SRC database/UtilsHandler.java:577-585; unused 3-param overload |
| SevenZFile.<init>(File,byte[]) | no_trigger_in_app | SRC SevenZFile.java:120-123; deprecated, app uses File,char[] |
| SevenZFile.<init>(FileChannel) | no_trigger_in_app | SRC SevenZFile.java:136-138; app uses File not FileChannel |
| SevenZFile.<init>(FileChannel,String) | no_trigger_in_app | SRC SevenZFile.java:187-190; app uses File not FileChannel |
| SevenZFile.<init>(FileChannel,String,byte[]) | no_trigger_in_app | SRC SevenZFile.java:207-210; app uses File not FileChannel |
| SevenZFile.<init>(FileChannel,String,char[]) | no_trigger_in_app | SRC SevenZFile.java:170-173; app uses File not FileChannel |
| SevenZFile.<init>(FileChannel,byte[]) | no_trigger_in_app | SRC SevenZFile.java:228-231; app uses File not FileChannel |
| SevenZFile.<init>(FileChannel,char[]) | no_trigger_in_app | SRC SevenZFile.java:152-155; app uses File not FileChannel |
| SevenZFile.getStatisticsForCurrentEntry | no_trigger_in_app | SRC SevenZFile.java:1115-1131; app doesn't query statistics |
| SevenZFile.matches | no_trigger_in_app | SRC SevenZFile.java:1158-1164; app doesn't pre-check signatures |
| SevenZFile.read() | no_trigger_in_app | SRC SevenZFile.java:1050-1055; app uses read(byte[]), not read() |
| SevenZFile.toString | no_trigger_in_app | SRC SevenZFile.java:1191-1193; not explicitly called |

### INCOMPLETE (0 methods)

None
