# Repair Batch 29 - AmazeFileManager

STATUS: START 22:11
STATUS: DONE 22:17

## Methods Analyzed

| Method | Status | Evidence Lines |
|--------|--------|----------------|
| MainFragment.addSearchResult | REACHABLE | Already routed in graph_def.py line 9163 |
| MainFragment.addShortcut | REACHABLE | Already routed in graph_def.py line 9211 |
| MainFragment.addTo | REACHABLE | Already routed in graph_def.py lines 7892, 9167, 9183 |
| MainFragment.hide | REACHABLE | Already routed in graph_def.py lines 9147, 9696 |
| MainFragment.onSearchCompleted | REACHABLE | Already routed in graph_def.py line 9197 |
| MainFragment$1.onGlobalLayout | REACHABLE | Framework ViewTreeObserver callback, registered at MainFragment.java:310 |
| MainFragment$2.getSpanSize | REACHABLE | Already routed in graph_def.py |
| MainFragment$3.hideOption | REACHABLE | Internal helper called from onCreateActionMode (line 494) and onPrepareActionMode |
| MainFragment$3.initMenu | REACHABLE | Called from onCreateActionMode at MainFragment.java:492 |
| MainFragment$3.onActionItemClicked | REACHABLE | Already routed in graph_def.py |
| MainFragment$3.onCreateActionMode | REACHABLE | Already routed in graph_def.py |
| MainFragment$3.onDestroyActionMode | REACHABLE | Already routed in graph_def.py |
| MainFragment$3.onPrepareActionMode | REACHABLE | Already routed in graph_def.py |
| MainFragment$3.showOption | REACHABLE | Internal helper called from onCreateActionMode and onPrepareActionMode |
| MainFragment$4.onReceive | REACHABLE | Already routed in graph_def.py |
| MainFragment$4$1.<init> | REACHABLE | Already routed in graph_def.py |
| MainFragment$4$1.onMediaScannerConnected | REACHABLE | Framework MediaScannerConnection callback, MainFragment.java:797-800 |
| MainFragment$4$1.onScanCompleted | REACHABLE | Framework MediaScannerConnection callback, MainFragment.java:802-806 |
| MainFragment$5.onReceive | REACHABLE | BroadcastReceiver for DECRYPT_BROADCAST, registered at MainFragment.java:1427 |
| MainFragment$6.<init> | REACHABLE | Already routed in graph_def.py |
| MainFragment$7.run | REACHABLE | Already routed in graph_def.py |
| ObtainableServiceBinder.getService | REACHABLE | Already routed in graph_def.py |
| OperationData.<init>(Operation,String,String,String,String,String) | REACHABLE | Called from SftpConnectDialog at lines 250, 352 |
| OperationData.toString | UNREACHABLE | Library-style: Object.toString override, no app callers found |
| Operations.<init> | UNREACHABLE | Library-style: only static methods, no instantiation found |
| PasteHelper.<init>(Parcel) | REACHABLE | Called from PasteHelper$1.createFromParcel (Parcelable pattern) |
| PasteHelper.describeContents | UNREACHABLE | Library-style: Parcelable boilerplate, framework callback, no app calls |
| PasteHelper.writeToParcel | UNREACHABLE | Library-style: Parcelable boilerplate, framework callback, no app calls |
| PasteHelper$1.createFromParcel | REACHABLE | Already routed in graph_def.py |
| PasteHelper$1.newArray | UNREACHABLE | Library-style: Parcelable.Creator boilerplate, framework callback, no app calls |
| PathSwitchPreference.lambda$setListener$0 | REACHABLE | Lambda from setListener, routes to FoldersPref.onPreferenceClick |
| PathSwitchPreference.onBindView | REACHABLE | Already routed in graph_def.py |
| PathSwitchPreference.onCreateView | REACHABLE | Already routed in graph_def.py line 15176 |
| PathSwitchPreference.setListener | REACHABLE | Already routed in graph_def.py |

## Summary

- **REACHABLE**: 29 methods
- **UNREACHABLE**: 5 methods
- **INCOMPLETE**: 0 methods

## New Edges Added

1. MainFragment.onCreateView -> MainFragment$1.<init>
2. MainFragment$1.<init> -> MainFragment$1.onGlobalLayout
3. MainFragment$3.onCreateActionMode -> MainFragment$3.hideOption
4. MainFragment$3.onPrepareActionMode -> MainFragment$3.hideOption
5. MainFragment$3.onCreateActionMode -> MainFragment$3.initMenu
6. MainFragment$3.onCreateActionMode -> MainFragment$3.showOption
7. MainFragment$3.onPrepareActionMode -> MainFragment$3.showOption
8. MainFragment$4$1.<init> -> MainFragment$4$1.onMediaScannerConnected
9. MainFragment$4$1.<init> -> MainFragment$4$1.onScanCompleted
10. MainFragment.onStart -> MainFragment$5.<init>
11. MainFragment$5.<init> -> MainFragment$5.onReceive
12. SftpConnectDialog$2.onClick -> OperationData.<init>(Operation,String,String,String,String,String)
13. SftpConnectDialog$4.onClick -> OperationData.<init>(Operation,String,String,String,String,String)
14. PasteHelper$1.createFromParcel -> PasteHelper.<init>(Parcel)
15. PathSwitchPreference.setListener -> PathSwitchPreference.lambda$setListener$0
16. PathSwitchPreference.lambda$setListener$0 -> PathSwitchPreference.getOnPreferenceClickListener
17. PathSwitchPreference.lambda$setListener$0 -> FoldersPref.onPreferenceClick

## Unreachable Methods

### OperationData.toString
- Object.toString override
- No app callers found (grep: cd app/src/main/java && grep -rn "OperationData.*toString")
- OperationData.java:75-86

### Operations.<init>
- Class with only static methods (mkdir, mkfile, rename, etc.)
- No instantiation found (grep: cd app/src/main/java && grep -rn "new Operations()")
- Operations.java implicit constructor

### PasteHelper.describeContents
- Parcelable.describeContents boilerplate
- Framework callback, no app calls
- PasteHelper.java:31-34

### PasteHelper.writeToParcel
- Parcelable.writeToParcel boilerplate
- Framework callback, no app calls
- PasteHelper.java:36-40

### PasteHelper$1.newArray
- Parcelable.Creator.newArray boilerplate
- Framework callback for array allocation, no app calls
- PasteHelper.java:47-49
