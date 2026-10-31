# Repair Batch 35 - AmazeFileManager
# Label Helper Slot 3

STATUS: START 22:46

## Methods Analysis

| Method | Status | Evidence |
|--------|--------|----------|
| ThemedImageView.<init>(Context) | REACHABLE | Already in graph_def.py with route from AndroidLayoutInflater.inflate |
| ThemedImageView.<init>(Context,AttributeSet) | REACHABLE | Already in graph_def.py with route from AndroidLayoutInflater.inflate |
| ThemedImageView.<init>(Context,AttributeSet,int) | REACHABLE | Already in graph_def.py with routes from other constructors and calls to AndroidView.setColorFilter, getActivity |
| ThemedImageView.getActivity | REACHABLE | Already in graph_def.py with route from ThemedImageView.<init>(Context,AttributeSet,int) |
| TinyDB.putBooleanArray | REACHABLE | Already in graph_def.py as TinyDB.putBooleanArray(SharedPreferences,String,Boolean[]) with route from QuickAccessPref.onPreferenceClick |
| UserColorPreferences.<init>(Parcel) | REACHABLE | Already in graph_def.py with route from AndroidIntent.getParcelableExtra |
| UserColorPreferences.describeContents | REACHABLE | Already in graph_def.py with route from AndroidIntent.putParcelableExtra |
| UserColorPreferences.writeToParcel | REACHABLE | Already in graph_def.py with route from AndroidIntent.putParcelableExtra |
| UserColorPreferences$1.createFromParcel | REACHABLE | Already in graph_def.py with Parcelable.Creator pattern |
| UserColorPreferences$1.newArray | REACHABLE | Already in graph_def.py with Parcelable.Creator pattern |
| UtilitiesProvider.getThemeManager | REACHABLE | Already in graph_def.py with existing route |
| Utils.<init> | UNREACHABLE | Utility class constructor never instantiated; SRC utils/Utils.java:59; grep found no "new Utils()" calls |
| Utils.getViewRawY | REACHABLE | Already in graph_def.py with route from FastScroller.getRelativeTouchPosition |
| UtilsHandler.addSsh | REACHABLE | Already in graph_def.py as UtilsHandler.addSsh(String,String,String,String,String) with route from lambda$saveToDatabase$0 |
| UtilsHandler.lambda$removeFromDatabase$1 | REACHABLE | Already in graph_def.py as lambda$removeFromDatabase$1(OperationData) with route from removeFromDatabase |
| UtilsHandler.lambda$saveToDatabase$0 | REACHABLE | Already in graph_def.py as lambda$saveToDatabase$0(OperationData) with route from saveToDatabase |
| UtilsHandler.onCreate | REACHABLE | Already in graph_def.py as onCreate(SQLiteDatabase) with LIFECYCLE edge from S_ENTRY |
| UtilsHandler.onUpgrade | REACHABLE | Already in graph_def.py as onUpgrade(SQLiteDatabase,int,int) with LIFECYCLE edge from S_ENTRY |
| UtilsHandler.removeBookmarksPath | REACHABLE | Already in graph_def.py as removeBookmarksPath(String,String) with route from lambda$removeFromDatabase$1 |
| UtilsHandler.removePath | REACHABLE | Already in graph_def.py as removePath(Operation,String) with route from lambda$removeFromDatabase$1 |
| UtilsHandler.removeSftpPath | REACHABLE | Already in graph_def.py as removeSftpPath(String,String) with route from lambda$removeFromDatabase$1 |
| UtilsHandler.setPath(Operation,String) | REACHABLE | Already in graph_def.py with route from lambda$saveToDatabase$0 |
| UtilsHandler.setPath(Operation,String,String) | REACHABLE | Already in graph_def.py with route from lambda$saveToDatabase$0 |
| UtilsHandler.updateSsh | REACHABLE | Already in graph_def.py with route from SftpConnectDialog |
| ZipService.onBind | REACHABLE | Already in graph_def.py with LIFECYCLE route from ProcessViewerFragment.refreshView |
| ZipService.onDestroy | REACHABLE | Already in graph_def.py with LIFECYCLE route from ZipService.onBind |
| ZipService.setProgressListener | REACHABLE | Already in graph_def.py with route from ProcessViewerFragment$CustomServiceConnection.onServiceConnected |

## Summary

- Total methods: 27
- REACHABLE: 26 (already have routes in graph_def.py)
- UNREACHABLE: 1 (Utils.<init>)
- INCOMPLETE: 0

STATUS: DONE 22:48
