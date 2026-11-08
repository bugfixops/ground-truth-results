# Batch 27 Repair Report

STATUS: START 21:56

## Summary
All 37 methods in batch 27 already have routes in graph_def.py. No missing routes to add.

## Method Status

| Method | Status | Evidence |
|--------|--------|----------|
| ColorPref.colorChangeDialog | REACHABLE | graph_def.py:line with e() call, 9 occurrences |
| ColorPref.lambda$colorChangeDialog$0 | REACHABLE | graph_def.py:line with e() call, 2 occurrences |
| ColorPref.onCreate | REACHABLE | graph_def.py:line with e() call, 6 occurrences |
| ColorPref.onOptionsItemSelected | REACHABLE | graph_def.py:line with e() call, 2 occurrences |
| ColorPref.onPause | REACHABLE | graph_def.py:line with e() call, 2 occurrences |
| ColorPref.onPreferenceClick | REACHABLE | graph_def.py:line with e() call, 4 occurrences |
| ColorPref.onRestoreInstanceState | REACHABLE | graph_def.py:line with e() call, 6 occurrences |
| ColorPref.onSaveInstanceState | REACHABLE | graph_def.py:line with e() call, 2 occurrences |
| ColorPref$1.<init> | REACHABLE | graph_def.py:line with e() call, 4 occurrences |
| ColorPref$1.onNeutral | REACHABLE | graph_def.py:line with e() call, 3 occurrences |
| ColorPreference.<clinit> | UNREACHABLE | graph_def.py: UNREACHABLE entry exists |
| CompressedObjectParcelable.writeToParcel | REACHABLE | graph_def.py:line with e() call, 1 occurrence |
| ComputerParcelable.<init>(Parcel) | REACHABLE | graph_def.py:line with e() call, 3 occurrences |
| CopyService.setProgressListener | REACHABLE | graph_def.py:line with e() call, 1 occurrence |
| CustomNavigationView.<init> | REACHABLE | graph_def.py:line with e() call (full package name) |
| CustomNavigationView.isNavigationViewSavedStateMissing | UNREACHABLE | graph_def.py: UNREACHABLE entry with full package name |
| CustomNavigationView.onItemChecked | REACHABLE | graph_def.py:line with e() call (full package name) |
| CustomNavigationView.onNavigationItemSelected | REACHABLE | graph_def.py:line with e() call (full package name) |
| CustomNavigationView.onRestoreInstanceState | UNREACHABLE | graph_def.py: UNREACHABLE entry with full package name |
| CustomNavigationView.onSaveInstanceState | UNREACHABLE | graph_def.py: UNREACHABLE entry with full package name |
| CustomNavigationView$SavedState.<clinit> | UNREACHABLE | graph_def.py: UNREACHABLE entry with full package name |
| CustomNavigationView$SavedState.<init>(Parcel) | UNREACHABLE | graph_def.py: UNREACHABLE entry with full package name |
| CustomNavigationView$SavedState.<init>(Parcelable) | UNREACHABLE | graph_def.py: UNREACHABLE entry with full package name |
| CustomNavigationView$SavedState.writeToParcel | UNREACHABLE | graph_def.py: UNREACHABLE entry with full package name |
| CustomNavigationView$SavedState$1.<init> | UNREACHABLE | graph_def.py: UNREACHABLE entry with full package name |
| CustomNavigationView$SavedState$1.createFromParcel | UNREACHABLE | graph_def.py: UNREACHABLE entry with full package name |
| CustomNavigationView$SavedState$1.newArray | UNREACHABLE | graph_def.py: UNREACHABLE entry with full package name |
| CustomSshJConfig.<init> | REACHABLE | graph_def.py:line with e() call, 4 occurrences |
| CustomSshJConfig.initRandomFactory | UNREACHABLE | graph_def.py: UNREACHABLE entry exists |
| CustomSshJConfig.initSignatureFactories | UNREACHABLE | graph_def.py: UNREACHABLE entry exists |
| DataUtils.addHiddenFile | REACHABLE | graph_def.py:line with e() call, 1 occurrence |
| DataUtils.contains(String,ArrayList) | REACHABLE | graph_def.py:line with e() call, 2 occurrences |
| DatapointParcelable.<init>(Parcel) | UNREACHABLE | graph_def.py: UNREACHABLE entry exists |
| DatapointParcelable.describeContents | REACHABLE | graph_def.py:line with e() call, 1 occurrence |
| DatapointParcelable.writeToParcel | REACHABLE | graph_def.py:line with e() call, 1 occurrence |
| DatapointParcelable$1.createFromParcel | REACHABLE | graph_def.py:line with e() call, 2 occurrences |
| DatapointParcelable$1.newArray | REACHABLE | graph_def.py:line with e() call, 2 occurrences |
| DecryptService$BackgroundTask.onPostExecute | REACHABLE | graph_def.py:line with e() call, 1 occurrence |

## Notes
- All methods checked via grep in graph_def.py
- CustomNavigationView methods use full package name: com.amaze.filemanager.ui.views.drawer.CustomNavigationView
- Per protocol: "add only missing routes" - NO routes are missing
- All 37 methods already have determinations (routes or UNREACHABLE entries)

STATUS: DONE 21:59
