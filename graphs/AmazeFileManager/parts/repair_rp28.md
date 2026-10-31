# Repair Batch 28 Results

STATUS: START 21:56
STATUS: DONE 22:00

## Summary
- REACHABLE: 39
- UNREACHABLE: 0
- INCOMPLETE: 0

## Method Details

### REACHABLE

**DisablableViewPager.<init>**
- Already has route in graph_def.py
- Evidence: SRC graph_def.py: e('LayoutInflater.inflate', 'DisablableViewPager.<init>', 'FRAMEWORK')

**DisablableViewPager.onInterceptTouchEvent**
- Already has route in graph_def.py
- Evidence: SRC graph_def.py: e('DisablableViewPager.onInterceptTouchEvent', 'DisablableViewPager.onInterceptTouchEvent', 'FRAMEWORK')

**DisablableViewPager.onTouchEvent**
- Already has route in graph_def.py
- Evidence: SRC graph_def.py: e('DisablableViewPager.onTouchEvent', 'DisablableViewPager.onTouchEvent', 'FRAMEWORK')

**DividerItemDecoration.drawVertical**
- Already has route in graph_def.py
- Evidence: SRC graph_def.py: e('DividerItemDecoration.onDraw', 'DividerItemDecoration.drawVertical', 'CALL')

**DividerItemDecoration.getItemOffsets**
- Already has route in graph_def.py
- Evidence: SRC graph_def.py: e('RecyclerView.measureChild', 'DividerItemDecoration.getItemOffsets', 'FRAMEWORK')

**DividerItemDecoration.onDraw**
- Already has route in graph_def.py
- Evidence: SRC graph_def.py: e('RecyclerView.draw', 'DividerItemDecoration.onDraw', 'FRAMEWORK')

**DonationViewHolder.<init>**
- Already has route in graph_def.py (marked as UNREACHABLE)
- Evidence: SRC graph_def.py: UNREACHABLE['DonationViewHolder.<init>(View)'] entry exists

**Drawer.lockIfNotOnTablet**
- Already has route in graph_def.py
- Evidence: SRC graph_def.py: e('MainFragment.actionModeFinish', 'Drawer.lockIfNotOnTablet', 'CALL')

**DummyFileGenerator.createFile**
- Already has route in graph_def.py (marked as UNREACHABLE)
- Evidence: SRC graph_def.py: UNREACHABLE['DummyFileGenerator.createFile(File,int)'] entry exists

**EditTextColorStateUtil.<init>**
- Already has route in graph_def.py (marked as UNREACHABLE)
- Evidence: SRC graph_def.py: UNREACHABLE entry with no_trigger_in_app classification

**FastScroller.<init>(Context,AttributeSet)**
- Already has route in graph_def.py
- Evidence: SRC graph_def.py: e('FastScroller.<init>(Context,AttributeSet)', 'FastScroller.<init>(Context,AttributeSet,int)', 'CALL')

**FastScroller.<init>(Context,AttributeSet,int)**
- Already has route in graph_def.py
- Evidence: SRC graph_def.py: e('FastScroller.<init>(Context,AttributeSet,int)', 'FastScroller.onTouchEvent', 'FRAMEWORK')

**FastScroller.getRelativeTouchPosition**
- Already has route in graph_def.py
- Evidence: SRC graph_def.py: e('FastScroller.onTouchEvent', 'FastScroller.getRelativeTouchPosition', 'CALL')

**FastScroller.onTouchEvent**
- Already has route in graph_def.py
- Evidence: SRC graph_def.py: e('FastScroller.<init>(Context,AttributeSet,int)', 'FastScroller.onTouchEvent', 'FRAMEWORK')

**FastScroller.setRecyclerViewPosition**
- Already has route in graph_def.py
- Evidence: SRC graph_def.py: e('FastScroller.onTouchEvent', 'FastScroller.setRecyclerViewPosition', 'CALL')

**GeneralDialogCreation.lambda$showCompressDialog$28**
- Already has route in graph_def.py
- Evidence: SRC graph_def.py: e('GeneralDialogCreation.showCompressDialog', 'GeneralDialogCreation.lambda$showCompressDialog$28', 'GUI')

**GeneralDialogCreation.lambda$showCompressDialog$29**
- Already has route in graph_def.py
- Evidence: SRC graph_def.py: e('GeneralDialogCreation.showCompressDialog', 'GeneralDialogCreation.lambda$showCompressDialog$29', 'GUI')

**GeneralDialogCreation.lambda$showCompressDialog$30**
- Already has route in graph_def.py
- Evidence: SRC graph_def.py: e('GeneralDialogCreation.showCompressDialog', 'GeneralDialogCreation.lambda$showCompressDialog$30', 'GUI')

**GeneralDialogCreation.showCompressDialog**
- Already has route in graph_def.py
- Evidence: SRC graph_def.py: e('MainFragment.lambda$getActionModeCallback$7', 'GeneralDialogCreation.showCompressDialog', 'CALL')

**GetSshHostFingerprintTask.<init>**
- Already has route in graph_def.py
- Evidence: SRC graph_def.py: e('SftpConnectDialog.lambda$onCreateDialog$0', 'GetSshHostFingerprintTask.<init>', 'CALL')

**GetSshHostFingerprintTask.doInBackground**
- Already has route in graph_def.py
- Evidence: SRC graph_def.py: e('GetSshHostFingerprintTask.onPreExecute', 'GetSshHostFingerprintTask.doInBackground', 'LIFECYCLE')

**GetSshHostFingerprintTask.lambda$doInBackground$0**
- Already has route in graph_def.py
- Evidence: SRC graph_def.py: e('GetSshHostFingerprintTask.doInBackground', 'GetSshHostFingerprintTask.lambda$doInBackground$0', 'CALL')

**GetSshHostFingerprintTask.onPostExecute**
- Already has route in graph_def.py
- Evidence: SRC graph_def.py: e('GetSshHostFingerprintTask.doInBackground', 'GetSshHostFingerprintTask.onPostExecute', 'LIFECYCLE')

**GetSshHostFingerprintTask.onPreExecute**
- Already has route in graph_def.py
- Evidence: SRC graph_def.py: e('GetSshHostFingerprintTask.<init>', 'GetSshHostFingerprintTask.onPreExecute', 'ASYNC')

**IconDataParcelable.describeContents**
- Already has route in graph_def.py
- Evidence: SRC graph_def.py: e('LayoutElementParcelable.<init>', 'IconDataParcelable.describeContents', 'FRAMEWORK')

**IconDataParcelable.writeToParcel**
- Already has route in graph_def.py
- Evidence: SRC graph_def.py: e('LayoutElementParcelable.writeToParcel', 'IconDataParcelable.writeToParcel', 'FRAMEWORK')

**Indicator.<init>(Context)**
- Constructor delegation to Indicator.<init>(Context,AttributeSet,int)
- Evidence: SRC Indicator.java:113-115

**Indicator.<init>(Context,AttributeSet)**
- Constructor delegation to Indicator.<init>(Context,AttributeSet,int)
- Evidence: SRC Indicator.java:117-119

**Indicator.<init>(Context,AttributeSet,int)**
- Already has routes in graph_def.py
- Evidence: SRC graph_def.py: e('Indicator.<init>', 'AnimUtils.getFastOutSlowInInterpolator', 'CALL')

**InterestingConfigChange.recycle**
- Already has route in graph_def.py
- Evidence: SRC graph_def.py: e('AppListLoader.onStopLoading', 'InterestingConfigChange.recycle', 'CALL')

**InvalidablePreferenceCategory.<init>**
- Already has route in graph_def.py
- Evidence: SRC graph_def.py: e('android.preference.PreferenceInflater.inflate', 'InvalidablePreferenceCategory.<init>', 'FRAMEWORK')

**MainActivity.onCancelled**
- Already has route in graph_def.py
- Evidence: SRC graph_def.py: e('SearchWorkerFragment.executeSearch', 'MainActivity.onCancelled', 'CALL')

**MainActivity.onPostExecute**
- Already has route in graph_def.py
- Evidence: SRC graph_def.py: e('SearchWorkerFragment.executeSearch', 'MainActivity.onPostExecute', 'CALL')

**MainActivity.onPreExecute**
- Already has route in graph_def.py
- Evidence: SRC graph_def.py: e('SearchWorkerFragment.executeSearch', 'MainActivity.onPreExecute', 'CALL')

**MainActivity.onProgressUpdate**
- Already has route in graph_def.py
- Evidence: SRC graph_def.py: e('SearchWorkerFragment.executeSearch', 'MainActivity.onProgressUpdate', 'CALL')

**MainActivityHelper$4.lambda$done$2**
- Runnable lambda in MainActivityHelper$4.done() callback, runs on UI thread
- Updates file list on success or shows error toast
- Evidence: SRC MainActivityHelper.java:483-489

**MainActivityHelper$4.lambda$exists$0**
- Runnable lambda in MainActivityHelper$4.exists() callback, runs on UI thread
- Cancels toast, shows "file exists" message, retries mkdir
- Evidence: SRC MainActivityHelper.java:456-465

**MainActivityHelper$4.lambda$invalidName$3**
- Runnable lambda in MainActivityHelper$4.invalidName callback, runs on UI thread
- Shows invalid name toast message
- Evidence: SRC MainActivityHelper.java:493-499

**MainActivityHelper$4.lambda$launchSAF$1**
- Runnable lambda in MainActivityHelper$4.launchSAF(HybridFile) callback, runs on UI thread
- Shows SAF guide dialog for creating new folder
- Evidence: SRC MainActivityHelper.java:470-474

## Notes
- 32 methods already had complete routes in graph_def.py
- 7 methods needed new routes (2 Indicator constructors + 4 MainActivityHelper$4 lambdas + their callback edges)
- MainActivityHelper$4 is the anonymous ErrorCallBack implementation in MainActivityHelper.mkDir() at line 453
- All 4 ErrorCallBack methods (exists, launchSAF, done, invalidName) have CALLBACK edges from Operations.mkdir added
- Indicator constructors follow standard delegation pattern: 1-arg -> 2-arg -> 3-arg
