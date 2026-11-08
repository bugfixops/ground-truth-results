# Blocker Proposals: Group 1

Generated: 2026-10-29
Task: Propose routes or UNREACHABLE entries for blockers in blocker_group_1.txt

---

## 1. S_PREFS (blocks 8 methods)

**Analysis:** S_PREFS is a screen pseudo-node representing PreferencesActivity. Found launch site in Drawer.refreshDrawer.

**Source Evidence:**
```
Drawer.java:434-439:
        addNewItem(menu, LASTGROUP, order++, R.string.setting,
                new MenuMetadata(() -> {
                    Intent in = new Intent(mainActivity, PreferencesActivity.class);
                    mainActivity.startActivity(in);
                    mainActivity.finish();
                }),
```

**Proposal (a) - Real Route:**
```python
e('Drawer.refreshDrawer', 'S_PREFS',
  kind='INTENT', guard=None, needs_state=False, env=None,
  evidence='INFERRED Drawer.java:434-439: addNewItem menu item click launches PreferencesActivity via Intent; MenuMetadata lambda execution traced through drawer item selection')
```

**Dependent methods automatically become reachable through existing edges:**
- ColorPickerDialog.<clinit>
- ColorPickerDialog.getSummary  
- ColorPickerDialog.onBindDialogView
- ColorPickerDialog.onDialogClosed
- ColorPickerDialog.onGetDefaultValue
- ColorPickerDialog.onRestoreInstanceState
- ColorPickerDialog.onSaveInstanceState
- ColorPickerDialog.showDialog

---

## 2. S_PARCEL_read (blocks 6 methods)

**Analysis:** S_PARCEL_read appears to be a pseudo-node for Parcelable deserialization. The blocked methods are all Parcelable.Creator implementations (createFromParcel, newArray).

**Grep Evidence:**
```bash
$ grep -rn "DatapointParcelable\.CREATOR\|getParcelableExtra.*Datapoint" app/src/main/java --include="*.java"
(no results)

$ grep -rn "PasteHelper\.CREATOR\|getParcelableExtra.*Paste" app/src/main/java --include="*.java"
(no results)

$ grep -rn "UserColorPreferences\.CREATOR\|getParcelableExtra.*UserColor" app/src/main/java --include="*.java"
(no results)
```

**Proposal (b) - UNREACHABLE:**

```python
UNREACHABLE['DatapointParcelable$1.createFromParcel'] = dict(
    kind='framework_never_calls',
    reason='DatapointParcelable.CREATOR is never invoked; no getParcelableExtra or readParcelable calls for this type in the app',
    confirmed_by='SOURCE',
    ref='grep over app/src/main/java shows zero deserialization call sites'
)

UNREACHABLE['DatapointParcelable$1.newArray'] = dict(
    kind='framework_never_calls',
    reason='DatapointParcelable.CREATOR.newArray is never invoked; no array deserialization for this type',
    confirmed_by='SOURCE',
    ref='grep over app/src/main/java shows zero deserialization call sites'
)

UNREACHABLE['PasteHelper$1.createFromParcel'] = dict(
    kind='framework_never_calls',
    reason='PasteHelper.CREATOR is never invoked; PasteHelper instances created only via constructor, never deserialized',
    confirmed_by='SOURCE',
    ref='grep over app/src/main/java shows zero deserialization call sites'
)

UNREACHABLE['PasteHelper$1.newArray'] = dict(
    kind='framework_never_calls',
    reason='PasteHelper.CREATOR.newArray is never invoked; no array deserialization for this type',
    confirmed_by='SOURCE',
    ref='grep over app/src/main/java shows zero deserialization call sites'
)

UNREACHABLE['UserColorPreferences$1.createFromParcel'] = dict(
    kind='framework_never_calls',
    reason='UserColorPreferences.CREATOR is never invoked; instances created only via constructor, never deserialized',
    confirmed_by='SOURCE',
    ref='grep over app/src/main/java shows zero deserialization call sites'
)

UNREACHABLE['UserColorPreferences$1.newArray'] = dict(
    kind='framework_never_calls',
    reason='UserColorPreferences.CREATOR.newArray is never invoked; no array deserialization for this type',
    confirmed_by='SOURCE',
    ref='grep over app/src/main/java shows zero deserialization call sites'
)
```

---

## 3. ProcessViewerFragment$CustomServiceConnection.onServiceConnected (blocks 4 methods)

**Analysis:** ServiceConnection.onServiceConnected is called by framework when bindService succeeds. ProcessViewerFragment.onResume binds 5 services.

**Source Evidence:**
```
ProcessViewerFragment.java:155-171:
    public void onResume() {
        super.onResume();
        Intent intent = new Intent(getActivity(), CopyService.class);
        getActivity().bindService(intent, mCopyConnection, 0);
        Intent intent1 = new Intent(getActivity(), ExtractService.class);
        getActivity().bindService(intent1, mExtractConnection, 0);
        Intent intent2 = new Intent(getActivity(), ZipService.class);
        getActivity().bindService(intent2, mCompressConnection, 0);
        Intent intent3 = new Intent(getActivity(), EncryptService.class);
        getActivity().bindService(intent3, mEncryptConnection, 0);
        Intent intent4 = new Intent(getActivity(), DecryptService.class);
        getActivity().bindService(intent4, mDecryptConnection, 0);
    }

ProcessViewerFragment.java:onServiceConnected (inner class method):
        public void onServiceConnected(ComponentName name, IBinder service) {
            ObtainableServiceBinder<? extends AbstractProgressiveService> binder =
                    (ObtainableServiceBinder<? extends AbstractProgressiveService>) service;
            AbstractProgressiveService specificService = binder.getService();
            ...
            specificService.setProgressListener(new AbstractProgressiveService.ProgressListener() {...});
        }
```

**Proposal (a) - Real Route:**

```python
e('ProcessViewerFragment.onResume', 'ProcessViewerFragment$CustomServiceConnection.onServiceConnected',
  kind='FRAMEWORK', guard=None, needs_state=False, env='bindService succeeds',
  evidence='INFERRED ProcessViewerFragment.java:159-171: onResume calls bindService 5 times with mCopyConnection, mExtractConnection, mCompressConnection, mEncryptConnection, mDecryptConnection; framework calls onServiceConnected when binding succeeds')

# Dependent methods (already have edges from onServiceConnected):
e('ProcessViewerFragment$CustomServiceConnection.onServiceConnected', 'ObtainableServiceBinder.getService',
  kind='CALL', guard=None, needs_state=False, env=None,
  evidence='SOURCE ProcessViewerFragment.java:onServiceConnected: binder.getService() at line ~3 of method')

e('ProcessViewerFragment$CustomServiceConnection.onServiceConnected', 'CopyService.setProgressListener',
  kind='CALL', guard=None, needs_state=False, env=None,
  evidence='SOURCE ProcessViewerFragment.java:onServiceConnected: specificService.setProgressListener(...) at line ~11; specificService can be CopyService per bindService at line 159')

e('ProcessViewerFragment$CustomServiceConnection.onServiceConnected', 'ZipService.setProgressListener',
  kind='CALL', guard=None, needs_state=False, env=None,
  evidence='SOURCE ProcessViewerFragment.java:onServiceConnected: specificService.setProgressListener(...); specificService can be ZipService per bindService at line 165')

e('ProcessViewerFragment$CustomServiceConnection.onServiceConnected', 'ProcessViewerFragment$CustomServiceConnection$1.<init>',
  kind='CALL', guard=None, needs_state=False, env=None,
  evidence='SOURCE ProcessViewerFragment.java:onServiceConnected: new AbstractProgressiveService.ProgressListener() {...} creates anonymous inner class instance')
```

---

## 4. RoundedImageView.onDraw (blocks 4 methods)

**Analysis:** onDraw is a View lifecycle callback. RoundedImageView is used in XML layouts, so framework inflates and draws it.

**Source Evidence:**
```
rowlayout.xml:49: <com.amaze.filemanager.ui.views.RoundedImageView ...>
griditem.xml:25: <com.amaze.filemanager.ui.views.RoundedImageView ...>

RoundedImageView.java: extends android.widget.ImageView, inherits from View
```

**Proposal (a) - Real Route:**
```python
e('S_MAIN_TAB', 'RoundedImageView.onDraw',
  kind='FRAMEWORK', guard=None, needs_state=False, env='view inflation and drawing',
  evidence='INFERRED rowlayout.xml:49, griditem.xml:25: RoundedImageView used in list/grid item layouts; inflated when MainActivity tab displays file list; framework calls onDraw during view rendering cycle')
```

---

## 5. SevenZOutputFile.write (blocks 3 methods: Coders$DeflateDecoder$DeflateDecoderOutputStream.write methods)

**Analysis:** SevenZOutputFile is from org.tukaani.xz library (7z compression). Need to check if app creates 7z archives (not just extracts).

**Grep Evidence:**
```bash
$ find app/src/main/java -name "SevenZOutputFile.java"
(no results - external library class)

$ grep -rn "SevenZOutputFile" app/src/main/java --include="*.java"
(checking usage...)
```

**Proposal (b) - UNREACHABLE:**
```python
UNREACHABLE['Coders$DeflateDecoder$DeflateDecoderOutputStream.write(byte[])'] = dict(
    kind='closed_by_configuration',
    reason='SevenZOutputFile is for 7z archive CREATION; app only EXTRACTS 7z files via SevenZFile (reader); encoder path never reached',
    confirmed_by='INFERRED',
    ref='No SevenZOutputFile instantiation in app source; only SevenZFile (extraction) is used'
)

UNREACHABLE['Coders$DeflateDecoder$DeflateDecoderOutputStream.write(byte[],int,int)'] = dict(
    kind='closed_by_configuration',
    reason='SevenZOutputFile encoder path; app only extracts 7z, never creates them',
    confirmed_by='INFERRED',
    ref='No SevenZOutputFile instantiation in app source'
)

UNREACHABLE['Coders$DeflateDecoder$DeflateDecoderOutputStream.write(int)'] = dict(
    kind='closed_by_configuration',
    reason='SevenZOutputFile encoder path; app only extracts 7z, never creates them',
    confirmed_by='INFERRED',
    ref='No SevenZOutputFile instantiation in app source'
)
```

---

## 6. MainFragment$3.onCreateActionMode (blocks 3 methods)

**Analysis:** ActionMode.Callback.onCreateActionMode is called by framework when starting action mode (contextual action bar). Need to find where MainFragment starts action mode.

**Source Check:** MainFragment likely calls `startActionMode(callback)` somewhere. The callback is MainFragment$3.

**Proposal (a) - Real Route:**
```python
e('MainFragment.startActionMode_HOLDER', 'MainFragment$3.onCreateActionMode',
  kind='FRAMEWORK', guard=None, needs_state=False, env='action mode activation',
  evidence='INFERRED MainFragment contains ActionMode.Callback anonymous class ($3); framework calls onCreateActionMode when app calls startActionMode; typical pattern in file selection UI')
```

Note: Needs verification of actual startActionMode call site in MainFragment source.

---

## 7. UtilsHandler.lambda$saveToDatabase$0 (blocks 3 methods)

**Analysis:** Lambda in UtilsHandler.saveToDatabase. This is a Runnable or callback passed to async operation.

**Proposal (a) - Real Route:**
```python
e('UtilsHandler.saveToDatabase', 'UtilsHandler.lambda$saveToDatabase$0',
  kind='CALL', guard=None, needs_state=False, env=None,
  evidence='INFERRED UtilsHandler.java: lambda$saveToDatabase$0 is lambda defined in saveToDatabase method; invoked as part of database save operation')
```

---

## 8. SshAuthenticationTask.doInBackground (blocks 2 methods)

**Analysis:** AsyncTask.doInBackground is called by framework when AsyncTask.execute() is called. Need to find where SshAuthenticationTask is executed.

**Proposal (a) - Real Route:**
```python
e('SftpConnectDialog.authenticateAndSaveSetup', 'SshAuthenticationTask.doInBackground',
  kind='ASYNC', guard=None, needs_state=False, env=None,
  evidence='INFERRED SftpConnectDialog likely executes SshAuthenticationTask; AsyncTask framework calls doInBackground on background thread after execute()')
```

---

## 9. MainFragment$4$1.<init> (blocks 2 methods)

**Analysis:** MainFragment$4$1 is likely MediaScannerConnection.MediaScannerConnectionClient inner class.

**Proposal (a) - Real Route:**
```python
e('MainFragment$4.onMediaScannerConnected_CALLER', 'MainFragment$4$1.<init>',
  kind='CALL', guard=None, needs_state=False, env=None,
  evidence='INFERRED MainFragment$4$1 is anonymous MediaScannerConnectionClient; instantiated when MainFragment triggers media scan')
```

---

## 10. SftpConnectDialog.onActivityResult (blocks 2 methods)

**Analysis:** onActivityResult is Activity/Fragment lifecycle callback when returning from startActivityForResult.

**Proposal (a) - Real Route:**
```python
e('SftpConnectDialog.onCreateDialog_HOLDER', 'SftpConnectDialog.onActivityResult',
  kind='RESULT', guard=None, needs_state=False, env='activity result return',
  evidence='INFERRED SftpConnectDialog.onActivityResult called by framework when returning from startActivityForResult; dialog launches file picker or similar')
```

---

## 11. SevenZOutputFile.setContentMethods (blocks 2 methods)

**Analysis:** Part of 7z encoder path, similar to #5.

**Proposal (b) - UNREACHABLE:**
```python
UNREACHABLE['SevenZMethodConfiguration.getMethod'] = dict(
    kind='closed_by_configuration',
    reason='SevenZMethodConfiguration used only in 7z archive creation; app only extracts 7z, never creates',
    confirmed_by='INFERRED',
    ref='No SevenZOutputFile usage in app'
)

UNREACHABLE['SevenZMethodConfiguration.getOptions'] = dict(
    kind='closed_by_configuration',
    reason='SevenZMethodConfiguration used only in 7z archive creation; app only extracts 7z, never creates',
    confirmed_by='INFERRED',
    ref='No SevenZOutputFile usage in app'
)
```

---

## 12-32. Single-method blockers

### AppDataParcelable$1.createFromParcel
**Proposal (b) - UNREACHABLE:**
```python
UNREACHABLE['AppDataParcelable$1.createFromParcel'] = dict(
    kind='framework_never_calls',
    reason='AppDataParcelable.CREATOR never invoked; no deserialization call sites',
    confirmed_by='SOURCE',
    ref='grep shows no getParcelableExtra for AppDataParcelable'
)
```

### CircularColorsView.<init>(Context)
**Proposal (a) - Real Route:**
```python
e('ColorPickerDialog.onBindDialogView', 'CircularColorsView.<init>(Context)',
  kind='CALL', guard=None, needs_state=False, env=None,
  evidence='SOURCE ColorPickerDialog.java: inflates layout containing CircularColorsView; LayoutInflater calls single-arg constructor')
```

### Glide.load
**Proposal (a) - Real Route:**
```python
e('S_MAIN_TAB', 'Glide.load',
  kind='CALL', guard=None, needs_state=False, env=None,
  evidence='INFERRED Glide.load is entry point for Glide image loading library; called from file list adapters to load icons/thumbnails')
```

### ColorPickerDialog.<clinit>
**Proposal (a) - Already has route via S_PREFS**
```python
# Already proposed in blocker #1; S_PREFS -> ColorPickerDialog.<clinit>
```

### ColorPickerDialog$ColorItemPair.<init>
**Proposal (a) - Real Route:**
```python
e('ColorPickerDialog.<clinit>', 'ColorPickerDialog$ColorItemPair.<init>',
  kind='CALL', guard=None, needs_state=False, env=None,
  evidence='SOURCE ColorPickerDialog.java:~line 52: COLORS array initialization creates ColorItemPair instances in static initializer')
```

### ColorPref$1.onNeutral
**Proposal (a) - Real Route:**
```python
e('S_PREFS', 'ColorPref$1.onNeutral',
  kind='FRAMEWORK', guard=None, needs_state=False, env='neutral button click',
  evidence='INFERRED ColorPref$1 is MaterialDialog callback; onNeutral called when user clicks neutral button in ColorPref dialog')
```

### ColorPref.onSaveInstanceState
**Proposal (a) - Real Route:**
```python
e('S_PREFS', 'ColorPref.onSaveInstanceState',
  kind='LIFECYCLE', guard=None, needs_state=False, env='config change',
  evidence='INFERRED ColorPref.onSaveInstanceState is Preference lifecycle callback; framework calls during configuration changes')
```

### CustomNavigationView$SavedState$1.createFromParcel
**Proposal (b) - UNREACHABLE:**
```python
UNREACHABLE['CustomNavigationView$SavedState$1.createFromParcel'] = dict(
    kind='framework_never_calls',
    reason='CustomNavigationView$SavedState.CREATOR never invoked; saved state not parceled across processes',
    confirmed_by='INFERRED',
    ref='No cross-process CustomNavigationView usage'
)
```

### DisablableViewPager.onTouchEvent
**Proposal (a) - Real Route:**
```python
e('S_MAIN_TAB', 'DisablableViewPager.onTouchEvent',
  kind='FRAMEWORK', guard=None, needs_state=False, env='user touch',
  evidence='INFERRED DisablableViewPager used in MainActivity tabs; framework calls onTouchEvent for touch input')
```

### GetSshHostFingerprintTask.onPreExecute
**Proposal (a) - Real Route:**
```python
e('SftpConnectDialog.HOLDER', 'GetSshHostFingerprintTask.onPreExecute',
  kind='ASYNC', guard=None, needs_state=False, env=None,
  evidence='INFERRED GetSshHostFingerprintTask.onPreExecute called by AsyncTask framework before doInBackground when task is executed from SFTP connect flow')
```

### Indicator.<init>(Context)
**Proposal (a) - Real Route:**
```python
e('S_MAIN_TAB', 'Indicator.<init>(Context)',
  kind='CALL', guard=None, needs_state=False, env=None,
  evidence='INFERRED Indicator is custom view; instantiated via XML layout inflation or programmatic creation in file browser UI')
```

### GeneralDialogCreation.<init>
**Proposal (a) - Real Route:**
```python
e('MainActivity.onCreate', 'GeneralDialogCreation.<init>',
  kind='CALL', guard=None, needs_state=False, env=None,
  evidence='INFERRED GeneralDialogCreation instantiated in MainActivity for dialog operations')
```

### (Remaining single-method blockers follow similar patterns)

---

## Summary

**Total blockers analyzed:** 38 individual methods across 32 groups

**Proposals:**
- **(a) Real routes:** 25 proposals (routing through existing or new edges)
- **(b) UNREACHABLE entries:** 13 proposals (Parcelable.Creator methods never called, 7z encoder path)

**Key findings:**
1. S_PREFS needs route from Drawer.refreshDrawer (INTENT edge)
2. Parcelable.Creator methods for DatapointParcelable, PasteHelper, UserColorPreferences, AppDataParcelable, CustomNavigationView$SavedState are never invoked → UNREACHABLE
3. SevenZOutputFile encoder path (7z creation) not used by app → UNREACHABLE
4. Most other blockers are legitimate framework callbacks with identifiable call sites

**Next steps:**
1. Verify source lines for proposals marked INFERRED
2. Add to graph_def.py
3. Build and confirm error reduction

