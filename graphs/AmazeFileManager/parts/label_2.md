STATUS: RUNNING 2026-10-27 20:53:08

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| AboutActivity.<init> | REACHABLE | | Constructor called when Activity instantiated via Intent from PrefFrag | SRC PrefFrag.java:204 startActivity(new Intent(getActivity(), AboutActivity.class)) |
| AboutActivity.lambda$onCreate$0 | REACHABLE | | Lambda callback for Palette.generate() in onCreate | SRC AboutActivity.java:93-98 Palette.from(bitmap).generate(palette -> {...}) |
| AboutActivity.lambda$onCreate$1 | REACHABLE | | Lambda callback for OnOffsetChangedListener in onCreate | SRC AboutActivity.java:100-102 mAppBarLayout.addOnOffsetChangedListener((appBarLayout, verticalOffset) -> {...}) |
| AboutActivity.onClick | REACHABLE | | OnClickListener callback, registered in onCreate | SRC AboutActivity.java:149 public void onClick(View v) |
| AboutActivity.onOptionsItemSelected | REACHABLE | | Framework callback for menu item selection | SRC AboutActivity.java:128 public boolean onOptionsItemSelected(MenuItem item) |
| AboutActivity.openURL | REACHABLE | | Called from onClick for various URL buttons | SRC AboutActivity.java:231 private void openURL(String url), called from onClick cases |
| DatabaseViewerActivity.getDbTableNames | REACHABLE | | Called from load() method | SRC DatabaseViewerActivity.java:166 arrayList = getDbTableNames(c) |
| DatabaseViewerActivity.lambda$load$2 | REACHABLE | | Lambda in load() Thread runOnUiThread callback | SRC DatabaseViewerActivity.java:185 runOnUiThread(() -> { listView.setAdapter(arrayAdapter); }) |
| DatabaseViewerActivity.lambda$null$1 | REACHABLE | | Lambda in load() Thread creation | SRC DatabaseViewerActivity.java:151-186 new Thread(() -> {...}).start() |
| DatabaseViewerActivity.lambda$onCreate$0 | REACHABLE | | Lambda for listView OnItemClickListener in onCreate | SRC DatabaseViewerActivity.java:142-149 listView.setOnItemClickListener((parent, view, position, id) -> {...}) |
| DatabaseViewerActivity.onBackPressed | REACHABLE | | Framework callback | SRC DatabaseViewerActivity.java:205 public void onBackPressed() |
| DatabaseViewerActivity.onDestroy | REACHABLE | | Framework lifecycle callback | SRC DatabaseViewerActivity.java:190 protected void onDestroy() |
| DatabaseViewerActivity.onOptionsItemSelected | REACHABLE | | Framework callback for menu selection | SRC DatabaseViewerActivity.java:199 public boolean onOptionsItemSelected(MenuItem item) |
| DatabaseViewerActivity.onPrepareOptionsMenu | REACHABLE | | Framework callback | SRC DatabaseViewerActivity.java:194 public boolean onPrepareOptionsMenu(Menu menu) |
| MainActivity.addConnection(OpenMode) | REACHABLE | | Called from UI for adding cloud connections | SRC MainActivity method in LAUNCHER activity |
| MainActivity.addConnection(boolean,String,String,String,String,String) | REACHABLE | | Called for adding SMB/cloud connections | SRC MainActivity method in LAUNCHER activity |
| MainActivity.closeInteractiveShell | REACHABLE | | Called from onDestroy | SRC MainActivity method in LAUNCHER activity |
| MainActivity.copyToClipboard | REACHABLE | | Called for copy operations | SRC MainActivity method in LAUNCHER activity |
| MainActivity.delete | REACHABLE | | Called for file deletion | SRC MainActivity method in LAUNCHER activity |
| MainActivity.deleteConnection(OpenMode) | REACHABLE | | Called to remove connections | SRC MainActivity method in LAUNCHER activity |
| MainActivity.deleteConnection(String,String) | REACHABLE | | Called to remove specific connection | SRC MainActivity method in LAUNCHER activity |
| MainActivity.exit | REACHABLE | | Called from UI exit action | SRC MainActivity method in LAUNCHER activity |
| MainActivity.getFAB | REACHABLE | | Getter for FAB | SRC MainActivity method in LAUNCHER activity |
| MainActivity.getPaste | REACHABLE | | Getter for paste data | SRC MainActivity method in LAUNCHER activity |
| MainActivity.hideSmokeScreen | REACHABLE | | Called to hide overlay | SRC MainActivity method in LAUNCHER activity |
| MainActivity.killToast | REACHABLE | | Called to dismiss toast | SRC MainActivity method in LAUNCHER activity |
| MainActivity.lambda$addConnection$9 | REACHABLE | | Lambda in addConnection | SRC MainActivity lambda in LAUNCHER activity |
| MainActivity.lambda$checkForExternalPermission$1 | REACHABLE | | Lambda for permission check | SRC MainActivity lambda in LAUNCHER activity |
| MainActivity.lambda$deleteConnection$10 | REACHABLE | | Lambda in deleteConnection | SRC MainActivity lambda in LAUNCHER activity |
| MainActivity.lambda$exit$3 | REACHABLE | | Lambda in exit | SRC MainActivity lambda in LAUNCHER activity |
| MainActivity.lambda$initFabToSave$2 | REACHABLE | | Lambda in initFabToSave | SRC MainActivity lambda in LAUNCHER activity |
| MainActivity.lambda$initialiseViews$8 | REACHABLE | | Lambda in initialiseViews | SRC MainActivity lambda in LAUNCHER activity |
| MainActivity.lambda$onCreate$0 | REACHABLE | | Lambda in onCreate | SRC MainActivity lambda in LAUNCHER activity |
| MainActivity.lambda$onOptionsItemSelected$4 | REACHABLE | | Lambda in onOptionsItemSelected | SRC MainActivity lambda in LAUNCHER activity |
| MainActivity.lambda$onOptionsItemSelected$5 | REACHABLE | | Lambda in onOptionsItemSelected | SRC MainActivity lambda in LAUNCHER activity |
| MainActivity.lambda$onOptionsItemSelected$6 | REACHABLE | | Lambda in onOptionsItemSelected | SRC MainActivity lambda in LAUNCHER activity |
| MainActivity.lambda$onOptionsItemSelected$7 | REACHABLE | | Lambda in onOptionsItemSelected | SRC MainActivity lambda in LAUNCHER activity |
| MainActivity.modify | REACHABLE | | Called for file modification | SRC MainActivity method in LAUNCHER activity |
| MainActivity.onActivityResult | REACHABLE | | Framework callback | SRC MainActivity.java framework callback in LAUNCHER activity |
| MainActivity.onBackPressed | REACHABLE | | Framework callback | SRC MainActivity.java framework callback in LAUNCHER activity |
| MainActivity.onBookAdded | REACHABLE | | BookmarkCallback interface method | SRC MainActivity.java implements BookmarkCallback |
| MainActivity.onCancelled | REACHABLE | | Callback interface method | SRC MainActivity.java callback in LAUNCHER activity |
| MainActivity.onConfigurationChanged | REACHABLE | | Framework callback | SRC MainActivity.java framework callback in LAUNCHER activity |
| MainActivity.onCreateLoader | REACHABLE | | LoaderManager callback | SRC MainActivity.java implements LoaderManager.LoaderCallbacks |
| MainActivity.onDestroy | REACHABLE | | Framework lifecycle callback | SRC MainActivity.java framework callback in LAUNCHER activity |
| MainActivity.onHiddenFileAdded | REACHABLE | | DataChangeListener callback | SRC MainActivity.java implements DataChangeListener |
| MainActivity.onHiddenFileRemoved | REACHABLE | | DataChangeListener callback | SRC MainActivity.java implements DataChangeListener |
| MainActivity.onHistoryCleared | REACHABLE | | Callback interface method | SRC MainActivity.java callback in LAUNCHER activity |
| MainActivity.onKeyDown | REACHABLE | | Framework callback | SRC MainActivity.java framework callback in LAUNCHER activity |
| MainActivity.onLoadFinished | REACHABLE | | LoaderManager callback | SRC MainActivity.java implements LoaderManager.LoaderCallbacks |
| MainActivity.onLoaderReset | REACHABLE | | LoaderManager callback | SRC MainActivity.java implements LoaderManager.LoaderCallbacks |
| MainActivity.onNewIntent | REACHABLE | | Framework callback | SRC MainActivity.java framework callback in LAUNCHER activity |
| MainActivity.onPause | REACHABLE | | Framework lifecycle callback | SRC MainActivity.java framework callback in LAUNCHER activity |
| MainActivity.onPostCreate | REACHABLE | | Framework lifecycle callback | SRC MainActivity.java framework callback in LAUNCHER activity |
| MainActivity.onPostExecute | REACHABLE | | AsyncTask callback | SRC MainActivity.java AsyncTask method in LAUNCHER activity |
| MainActivity.onPreExecute | REACHABLE | | AsyncTask callback | SRC MainActivity.java AsyncTask method in LAUNCHER activity |
| MainActivity.onPrepareOptionsMenu | REACHABLE | | Framework callback | SRC MainActivity.java framework callback in LAUNCHER activity |
| MainActivity.onProgressUpdate | REACHABLE | | AsyncTask callback | SRC MainActivity.java AsyncTask method in LAUNCHER activity |
| MainActivity.onSaveInstanceState | REACHABLE | | Framework lifecycle callback | SRC MainActivity.java framework callback in LAUNCHER activity |
| MainActivity.renameBookmark | REACHABLE | | BookmarkCallback interface method | SRC MainActivity.java implements BookmarkCallback |
| MainActivity.setPagingEnabled | REACHABLE | | Setter called from fragments | SRC MainActivity method in LAUNCHER activity |
| MainActivity.setPaste | REACHABLE | | Setter for paste data | SRC MainActivity method in LAUNCHER activity |
| MainActivity.showSMBDialog | REACHABLE | | Called to show SMB dialog | SRC MainActivity method in LAUNCHER activity |
| MainActivity.showSftpDialog | REACHABLE | | Called to show SFTP dialog | SRC MainActivity method in LAUNCHER activity |
| MainActivity.showToast | REACHABLE | | Called to show toast messages | SRC MainActivity method in LAUNCHER activity |
| MainActivity.updateViews | REACHABLE | | Called to update UI | SRC MainActivity method in LAUNCHER activity |
| MainActivity$2.onReceive | REACHABLE | | BroadcastReceiver callback in MainActivity inner class | SRC MainActivity$2 extends BroadcastReceiver |
| MainActivity$3.onReceive | REACHABLE | | BroadcastReceiver callback in MainActivity inner class | SRC MainActivity$3 extends BroadcastReceiver |
| MainActivity$FabActionListener.onActionSelected | REACHABLE | | SpeedDial callback in MainActivity inner class | SRC MainActivity$FabActionListener callback |
| PreferencesActivity.getRestartActivity | REACHABLE | | Getter method | SRC PreferencesActivity.java:254 public boolean getRestartActivity() |
| PreferencesActivity.onBackPressed | REACHABLE | | Framework callback | SRC PreferencesActivity.java:110 public void onBackPressed() |
| PreferencesActivity.onOptionsItemSelected | REACHABLE | | Framework callback | SRC PreferencesActivity.java:126 public boolean onOptionsItemSelected(MenuItem item) |
| PreferencesActivity.onSaveInstanceState | REACHABLE | | Framework lifecycle callback | SRC PreferencesActivity.java:105 protected void onSaveInstanceState(Bundle outState) |
| PreferencesActivity.restartActivity | REACHABLE | | Called to restart activity | SRC PreferencesActivity.java:245 public void restartActivity(final Activity activity) |
| PreferencesActivity.restoreListViewState | REACHABLE | | Called to restore list state | SRC PreferencesActivity.java:225 public Parcelable restoreListViewState(int prefFragment) |
| PreferencesActivity.saveListViewState | REACHABLE | | Called to save list state | SRC PreferencesActivity.java:220 public void saveListViewState(int prefFragment, Parcelable listViewState) |
| PreferencesActivity.setRestartActivity | REACHABLE | | Setter method | SRC PreferencesActivity.java:250 public void setRestartActivity() |
| TextEditorActivity.afterTextChanged | REACHABLE | | TextWatcher callback | SRC TextEditorActivity.java implements TextWatcher |
| TextEditorActivity.beforeTextChanged | REACHABLE | | TextWatcher callback | SRC TextEditorActivity.java implements TextWatcher |
| TextEditorActivity.checkUnsavedChanges | REACHABLE | | Called on exit to check for unsaved content | SRC TextEditorActivity.java private method called from framework callbacks |
| TextEditorActivity.cleanSpans | REACHABLE | | Called to clean text spans | SRC TextEditorActivity.java private method |
| TextEditorActivity.hideSearchView | REACHABLE | | Called to hide search UI | SRC TextEditorActivity.java private method |
| TextEditorActivity.lambda$checkUnsavedChanges$0 | REACHABLE | | Lambda in checkUnsavedChanges dialog positive action | SRC TextEditorActivity.java lambda |
| TextEditorActivity.lambda$checkUnsavedChanges$1 | REACHABLE | | Lambda in checkUnsavedChanges dialog negative action | SRC TextEditorActivity.java lambda |
| TextEditorActivity.lambda$load$4 | REACHABLE | | Lambda in load method | SRC TextEditorActivity.java lambda |
| TextEditorActivity.lambda$null$3 | REACHABLE | | Nested lambda in load | SRC TextEditorActivity.java lambda |
| TextEditorActivity.lambda$saveFile$2 | REACHABLE | | Lambda in saveFile | SRC TextEditorActivity.java lambda |
| TextEditorActivity.onBackPressed | REACHABLE | | Framework callback | SRC TextEditorActivity.java framework callback |
| TextEditorActivity.onClick | REACHABLE | | OnClickListener callback | SRC TextEditorActivity.java implements View.OnClickListener |
| TextEditorActivity.onCreateOptionsMenu | REACHABLE | | Framework callback | SRC TextEditorActivity.java framework callback |
| TextEditorActivity.onDestroy | REACHABLE | | Framework lifecycle callback | SRC TextEditorActivity.java framework callback |
| TextEditorActivity.onOptionsItemSelected | REACHABLE | | Framework callback | SRC TextEditorActivity.java framework callback |
| TextEditorActivity.onPrepareOptionsMenu | REACHABLE | | Framework callback | SRC TextEditorActivity.java framework callback |
| TextEditorActivity.onSaveInstanceState | REACHABLE | | Framework lifecycle callback | SRC TextEditorActivity.java framework callback |
| TextEditorActivity.onTextChanged | REACHABLE | | TextWatcher callback | SRC TextEditorActivity.java implements TextWatcher |
| TextEditorActivity.revealSearchView | REACHABLE | | Called to reveal search UI | SRC TextEditorActivity.java private method |
| TextEditorActivity.saveFile | REACHABLE | | Called to save file content | SRC TextEditorActivity.java private method |
| TextEditorActivity$1.<init> | REACHABLE | | Constructor for Runnable inner class | SRC TextEditorActivity.java:408 new Runnable() |
| TextEditorActivity$1.run | REACHABLE | | Runnable run method | SRC TextEditorActivity.java:408 new Runnable() implementation |
| TextEditorActivity$2.<init> | REACHABLE | | Constructor for AnimatorListenerAdapter | SRC TextEditorActivity.java:481 new AnimatorListenerAdapter() |
| TextEditorActivity$2.onAnimationEnd | REACHABLE | | AnimatorListener callback | SRC TextEditorActivity.java:481 AnimatorListenerAdapter |
| TextEditorActivity$3.<init> | REACHABLE | | Constructor for AnimatorListenerAdapter | SRC TextEditorActivity.java:518 new AnimatorListenerAdapter() |
| TextEditorActivity$3.onAnimationEnd | REACHABLE | | AnimatorListener callback | SRC TextEditorActivity.java:518 AnimatorListenerAdapter |
| PermissionsActivity.isGranted | REACHABLE | | Private helper called from onRequestPermissionsResult | SRC PermissionsActivity.java:101 private boolean isGranted(int[] grantResults) |
| PermissionsActivity.lambda$requestInstallApkPermission$1 | REACHABLE | | Lambda in requestInstallApkPermission | SRC PermissionsActivity.java:66 materialDialog.getActionButton(...).setOnClickListener(v -> ...) |
| PermissionsActivity.lambda$requestPermission$2 | REACHABLE | | Lambda in requestPermission | SRC PermissionsActivity.java:87 rationale.getActionButton(...).setOnClickListener(v -> {...}) |
| PermissionsActivity.lambda$requestStoragePermission$0 | REACHABLE | | Lambda in requestStoragePermission | SRC PermissionsActivity.java:56 materialDialog.getActionButton(...).setOnClickListener(v -> finish()) |
| PermissionsActivity.onRequestPermissionsResult | REACHABLE | | Framework callback | SRC PermissionsActivity.java:26 @Override public void onRequestPermissionsResult |
| PermissionsActivity.requestInstallApkPermission | REACHABLE | | Called to request install permission | SRC PermissionsActivity.java:62 public void requestInstallApkPermission |
| ColorPickerDialog.<clinit> | REACHABLE | | Static initializer | SRC ColorPickerDialog.java static initialization |
| ColorPickerDialog.<init> | REACHABLE | | Constructor | SRC ColorPickerDialog.java:70 public ColorPickerDialog(Context context, AttributeSet attrs) |
| ColorPickerDialog.getColor | REACHABLE | | Helper to get color resource | SRC ColorPickerDialog.java:226 private int getColor(int i, int pos) |
| ColorPickerDialog.getSummary | REACHABLE | | Preference method override | SRC ColorPickerDialog.java:95 public CharSequence getSummary() |
| ColorPickerDialog.inflateItem | REACHABLE | | Called from onBindDialogView to create items | SRC ColorPickerDialog.java:159 private View inflateItem(...) called from onBindDialogView |
| ColorPickerDialog.lambda$inflateItem$0 | REACHABLE | | Lambda OnClickListener in inflateItem | SRC ColorPickerDialog.java:160 View.OnClickListener clickListener = v -> {...} |
| ColorPickerDialog.onBindDialogView | REACHABLE | | DialogPreference callback | SRC ColorPickerDialog.java:100 public void onBindDialogView(View view) |
| ColorPickerDialog.onDialogClosed | REACHABLE | | DialogPreference callback | SRC ColorPickerDialog.java:194 protected void onDialogClosed(boolean positiveResult) |
| ColorPickerDialog.onGetDefaultValue | REACHABLE | | Preference callback | SRC ColorPickerDialog.java:90 protected Object onGetDefaultValue(TypedArray a, int index) |
| ColorPickerDialog.onRestoreInstanceState | REACHABLE | | Preference lifecycle callback | SRC ColorPickerDialog.java:241 protected void onRestoreInstanceState(Parcelable state) |
| ColorPickerDialog.onSaveInstanceState | REACHABLE | | Preference lifecycle callback | SRC ColorPickerDialog.java:232 protected Parcelable onSaveInstanceState() |
| ColorPickerDialog.select | REACHABLE | | Helper to select radio button | SRC ColorPickerDialog.java:154 private void select(View listChild, boolean checked) called from onBindDialogView |
| ColorPickerDialog.setColorPreference | REACHABLE | | Setter called from preference fragment | SRC ColorPickerDialog.java:80 public void setColorPreference(...) |
| ColorPickerDialog.setListener | REACHABLE | | Setter for callback | SRC ColorPickerDialog.java:85 public void setListener(OnAcceptedConfig l) |
| ColorPickerDialog.showDialog | REACHABLE | | DialogPreference method | SRC ColorPickerDialog.java:183 protected void showDialog(Bundle state) |
| ColorPickerDialog$ColorItemPair.<init> | REACHABLE | | Constructor for inner class | SRC ColorPickerDialog.java:217 public ColorItemPair(Integer first, int[] second) |
| ColorPickerDialog$SavedState.<clinit> | REACHABLE | | Static initializer | SRC ColorPickerDialog.java:258 static CREATOR field |
| ColorPickerDialog$SavedState.<init>(Parcel) | REACHABLE | | Parcelable constructor | SRC ColorPickerDialog.java:249 public SavedState(Parcel source) |
| ColorPickerDialog$SavedState.<init>(Parcelable) | REACHABLE | | Constructor with superstate | SRC ColorPickerDialog.java:256 public SavedState(Parcelable superState) |
| ColorPickerDialog$SavedState.writeToParcel | REACHABLE | | Parcelable method | SRC ColorPickerDialog.java:251 public void writeToParcel(Parcel dest, int flags) |
| ColorPickerDialog$SavedState$1.<init> | REACHABLE | | Parcelable.Creator constructor | SRC ColorPickerDialog.java:259 Creator instance |
| ColorPickerDialog$SavedState$1.createFromParcel | REACHABLE | | Parcelable.Creator method | SRC ColorPickerDialog.java:260 public SavedState createFromParcel(Parcel in) |
| ColorPickerDialog$SavedState$1.newArray | REACHABLE | | Parcelable.Creator method | SRC ColorPickerDialog.java:263 public SavedState[] newArray(int size) |
| GeneralDialogCreation.<init> | REACHABLE | | Constructor | SRC GeneralDialogCreation.java constructor |
| GeneralDialogCreation.deleteFilesDialog | REACHABLE | | Static method called from MainActivity | SRC GeneralDialogCreation.java:166 public static void deleteFilesDialog |
| GeneralDialogCreation.lambda$deleteFilesDialog$0 | REACHABLE | | Lambda in deleteFilesDialog onPositive | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$null$39 | REACHABLE | | Nested lambda | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$setPermissionsDialog$40 | REACHABLE | | Lambda in setPermissionsDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showArchiveDialog$26 | REACHABLE | | Lambda in showArchiveDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showArchiveDialog$27 | REACHABLE | | Lambda in showArchiveDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showChangePathsDialog$41 | REACHABLE | | Lambda in showChangePathsDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showChangePathsDialog$42 | REACHABLE | | Lambda in showChangePathsDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showCloudDialog$8 | REACHABLE | | Lambda in showCloudDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showCloudDialog$9 | REACHABLE | | Lambda in showCloudDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showCompressDialog$28 | REACHABLE | | Lambda in showCompressDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showCompressDialog$29 | REACHABLE | | Lambda in showCompressDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showCompressDialog$30 | REACHABLE | | Lambda in showCompressDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showDecryptDialog$21 | REACHABLE | | Lambda in showDecryptDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showDecryptFingerprintDialog$20 | REACHABLE | | Lambda in showDecryptFingerprintDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showEncryptAuthenticateDialog$14 | REACHABLE | | Lambda in showEncryptAuthenticateDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showEncryptAuthenticateDialog$15 | REACHABLE | | Lambda in showEncryptAuthenticateDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showEncryptAuthenticateDialog$16 | REACHABLE | | Lambda in showEncryptAuthenticateDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showEncryptAuthenticateDialog$17 | REACHABLE | | Lambda in showEncryptAuthenticateDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showEncryptAuthenticateDialog$18 | REACHABLE | | Lambda in showEncryptAuthenticateDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showEncryptAuthenticateDialog$19 | REACHABLE | | Lambda in showEncryptAuthenticateDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showEncryptWarningDialog$10 | REACHABLE | | Lambda in showEncryptWarningDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showEncryptWarningDialog$11 | REACHABLE | | Lambda in showEncryptWarningDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showEncryptWithPresetPasswordSaveAsDialog$12 | REACHABLE | | Lambda in showEncryptWithPresetPasswordSaveAsDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showEncryptWithPresetPasswordSaveAsDialog$13 | REACHABLE | | Lambda in showEncryptWithPresetPasswordSaveAsDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showHistoryDialog$38 | REACHABLE | | Lambda in showHistoryDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showPackageDialog$24 | REACHABLE | | Lambda in showPackageDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showPackageDialog$25 | REACHABLE | | Lambda in showPackageDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showPasswordDialog$22 | REACHABLE | | Lambda in showPasswordDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showPasswordDialog$23 | REACHABLE | | Lambda in showPasswordDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showPropertiesDialog$1 | REACHABLE | | Lambda in showPropertiesDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showPropertiesDialog$2 | REACHABLE | | Lambda in showPropertiesDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showPropertiesDialog$3 | REACHABLE | | Lambda in showPropertiesDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showPropertiesDialog$4 | REACHABLE | | Lambda in showPropertiesDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showPropertiesDialog$5 | REACHABLE | | Lambda in showPropertiesDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showPropertiesDialog$6 | REACHABLE | | Lambda in showPropertiesDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showPropertiesDialog$7 | REACHABLE | | Lambda in showPropertiesDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showSortDialog$31 | REACHABLE | | Lambda in showSortDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showSortDialog$32 | REACHABLE | | Lambda in showSortDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showSortDialog$33 | REACHABLE | | Lambda in showSortDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showSortDialog$34 | REACHABLE | | Lambda in showSortDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showSortDialog$35 | REACHABLE | | Lambda in showSortDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showSortDialog$36 | REACHABLE | | Lambda in showSortDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.lambda$showSortDialog$37 | REACHABLE | | Lambda in showSortDialog | SRC GeneralDialogCreation.java lambda |
| GeneralDialogCreation.onSortTypeSelected | REACHABLE | | Callback method | SRC GeneralDialogCreation.java method |
| GeneralDialogCreation.setPermissionsDialog | REACHABLE | | Static dialog method called from MainActivity | SRC GeneralDialogCreation.java static method |
| GeneralDialogCreation.showChangePathsDialog | REACHABLE | | Static dialog method | SRC GeneralDialogCreation.java static method |
| GeneralDialogCreation.showCloudDialog | REACHABLE | | Static dialog method | SRC GeneralDialogCreation.java static method |
| GeneralDialogCreation.showCompressDialog | REACHABLE | | Static dialog method | SRC GeneralDialogCreation.java static method |
| GeneralDialogCreation.showDecryptDialog | REACHABLE | | Static dialog method | SRC GeneralDialogCreation.java static method |
| GeneralDialogCreation.showDecryptFingerprintDialog | REACHABLE | | Static dialog method | SRC GeneralDialogCreation.java static method |
| GeneralDialogCreation.showEncryptAuthenticateDialog | REACHABLE | | Static dialog method | SRC GeneralDialogCreation.java static method |
| GeneralDialogCreation.showEncryptWarningDialog | REACHABLE | | Static dialog method | SRC GeneralDialogCreation.java static method |
| GeneralDialogCreation.showEncryptWithPresetPasswordSaveAsDialog | REACHABLE | | Static dialog method | SRC GeneralDialogCreation.java static method |
| GeneralDialogCreation.showNameDialog | REACHABLE | | Static dialog method called from activities | SRC GeneralDialogCreation.java:141 public static MaterialDialog showNameDialog |
| GeneralDialogCreation.showPasswordDialog | REACHABLE | | Static dialog method | SRC GeneralDialogCreation.java static method |
| GeneralDialogCreation.showPropertiesDialog | REACHABLE | | Static dialog method | SRC GeneralDialogCreation.java static method |
| GeneralDialogCreation.showPropertiesDialogForStorage | REACHABLE | | Static dialog method | SRC GeneralDialogCreation.java static method |
| GeneralDialogCreation.showPropertiesDialogWithPermissions | REACHABLE | | Static dialog method | SRC GeneralDialogCreation.java static method |
| GeneralDialogCreation.showPropertiesDialogWithoutPermissions | REACHABLE | | Static dialog method | SRC GeneralDialogCreation.java static method |
| GeneralDialogCreation.showSMBHelpDialog | REACHABLE | | Static dialog method | SRC GeneralDialogCreation.java static method |
| GeneralDialogCreation$1.<init> | REACHABLE | | AsyncTask constructor in deleteFilesDialog | SRC GeneralDialogCreation.java:192 new AsyncTask |
| GeneralDialogCreation$1.doInBackground | REACHABLE | | AsyncTask method | SRC GeneralDialogCreation.java AsyncTask doInBackground |
| GeneralDialogCreation$1.onPostExecute | REACHABLE | | AsyncTask method | SRC GeneralDialogCreation.java AsyncTask onPostExecute |
| GeneralDialogCreation$1.onPreExecute | REACHABLE | | AsyncTask method | SRC GeneralDialogCreation.java AsyncTask onPreExecute |
| GeneralDialogCreation$1.onProgressUpdate | REACHABLE | | AsyncTask method | SRC GeneralDialogCreation.java AsyncTask onProgressUpdate |
| GeneralDialogCreation$1.updateViews | REACHABLE | | Helper method in AsyncTask | SRC GeneralDialogCreation.java:275 private void updateViews |
| GeneralDialogCreation$2.<init> | REACHABLE | | SimpleTextWatcher constructor | SRC GeneralDialogCreation.java SimpleTextWatcher instance |
| GeneralDialogCreation$2.onTextChanged | REACHABLE | | TextWatcher callback | SRC GeneralDialogCreation.java SimpleTextWatcher.onTextChanged |
| GeneralDialogCreation$SizeFormatter.<init> | REACHABLE | | Constructor for inner class | SRC GeneralDialogCreation.java SizeFormatter constructor |
| GeneralDialogCreation$SizeFormatter.getFormattedValue | REACHABLE | | IValueFormatter method | SRC GeneralDialogCreation.java implements IValueFormatter |
| SftpConnectDialog.<init> | REACHABLE | | Constructor | SRC SftpConnectDialog.java constructor |
| SftpConnectDialog.authenticateAndSaveSetup | REACHABLE | | Called to authenticate SFTP connection | SRC SftpConnectDialog.java method |
| SftpConnectDialog.getPemContents | REACHABLE | | Helper to read PEM file | SRC SftpConnectDialog.java method |
| SftpConnectDialog.lambda$authenticateAndSaveSetup$15 | REACHABLE | | Lambda in authenticateAndSaveSetup | SRC SftpConnectDialog.java lambda |
| SftpConnectDialog.lambda$null$11 | REACHABLE | | Nested lambda | SRC SftpConnectDialog.java lambda |
| SftpConnectDialog.lambda$null$2 | REACHABLE | | Nested lambda | SRC SftpConnectDialog.java lambda |
| SftpConnectDialog.lambda$null$3 | REACHABLE | | Nested lambda | SRC SftpConnectDialog.java lambda |
| SftpConnectDialog.lambda$null$4 | REACHABLE | | Nested lambda | SRC SftpConnectDialog.java lambda |
| SftpConnectDialog.lambda$null$5 | REACHABLE | | Nested lambda | SRC SftpConnectDialog.java lambda |
| SftpConnectDialog.lambda$null$6 | REACHABLE | | Nested lambda | SRC SftpConnectDialog.java lambda |
| SftpConnectDialog.lambda$null$7 | REACHABLE | | Nested lambda | SRC SftpConnectDialog.java lambda |
| SftpConnectDialog.lambda$null$8 | REACHABLE | | Nested lambda | SRC SftpConnectDialog.java lambda |
| SftpConnectDialog.lambda$onActivityResult$14 | REACHABLE | | Lambda in onActivityResult | SRC SftpConnectDialog.java lambda |
| SftpConnectDialog.lambda$onCreateDialog$0 | REACHABLE | | Lambda in onCreateDialog | SRC SftpConnectDialog.java lambda |
| SftpConnectDialog.lambda$onCreateDialog$1 | REACHABLE | | Lambda in onCreateDialog | SRC SftpConnectDialog.java lambda |
| SftpConnectDialog.lambda$onCreateDialog$10 | REACHABLE | | Lambda in onCreateDialog | SRC SftpConnectDialog.java lambda |
| SftpConnectDialog.lambda$onCreateDialog$12 | REACHABLE | | Lambda in onCreateDialog | SRC SftpConnectDialog.java lambda |
| SftpConnectDialog.lambda$onCreateDialog$13 | REACHABLE | | Lambda in onCreateDialog | SRC SftpConnectDialog.java lambda |
| SftpConnectDialog.lambda$onCreateDialog$9 | REACHABLE | | Lambda in onCreateDialog | SRC SftpConnectDialog.java lambda |
| SftpConnectDialog.onActivityResult | REACHABLE | | Framework callback | SRC SftpConnectDialog.java framework callback |
| SftpConnectDialog.onCreate | REACHABLE | | DialogFragment lifecycle callback | SRC SftpConnectDialog.java framework callback |
| SftpConnectDialog.onCreateDialog | REACHABLE | | DialogFragment callback | SRC SftpConnectDialog.java framework callback |
| SftpConnectDialog$1.<init> | REACHABLE | | TextWatcher inner class constructor | SRC SftpConnectDialog.java TextWatcher instance |
| SftpConnectDialog$1.afterTextChanged | REACHABLE | | TextWatcher callback | SRC SftpConnectDialog.java TextWatcher.afterTextChanged |
| SmbConnectDialog.<init> | REACHABLE | | Constructor | SRC SmbConnectDialog.java constructor |
| SmbConnectDialog.createEditTextColorStateList | REACHABLE | | Helper method | SRC SmbConnectDialog.java method |
| SmbConnectDialog.createSMBPath | REACHABLE | | Helper to build SMB path | SRC SmbConnectDialog.java method |
| SmbConnectDialog.lambda$onCreateDialog$0 | REACHABLE | | Lambda in onCreateDialog | SRC SmbConnectDialog.java lambda |
| SmbConnectDialog.lambda$onCreateDialog$1 | REACHABLE | | Lambda in onCreateDialog | SRC SmbConnectDialog.java lambda |
| SmbConnectDialog.lambda$onCreateDialog$2 | REACHABLE | | Lambda in onCreateDialog | SRC SmbConnectDialog.java lambda |
| SmbConnectDialog.lambda$onCreateDialog$3 | REACHABLE | | Lambda in onCreateDialog | SRC SmbConnectDialog.java lambda |
| SmbConnectDialog.lambda$onCreateDialog$4 | REACHABLE | | Lambda in onCreateDialog | SRC SmbConnectDialog.java lambda |
| SmbConnectDialog.onCreate | REACHABLE | | DialogFragment lifecycle callback | SRC SmbConnectDialog.java framework callback |
| SmbConnectDialog.onCreateDialog | REACHABLE | | DialogFragment callback | SRC SmbConnectDialog.java framework callback |
| SmbConnectDialog.setTint | REACHABLE | | Helper method | SRC SmbConnectDialog.java method |
| SmbConnectDialog$1.<init> | REACHABLE | | TextWatcher constructor | SRC SmbConnectDialog.java TextWatcher instance |
| SmbConnectDialog$1.afterTextChanged | REACHABLE | | TextWatcher callback | SRC SmbConnectDialog.java TextWatcher.afterTextChanged |
| SmbConnectDialog$2.<init> | REACHABLE | | TextWatcher constructor | SRC SmbConnectDialog.java TextWatcher instance |
| SmbConnectDialog$2.afterTextChanged | REACHABLE | | TextWatcher callback | SRC SmbConnectDialog.java TextWatcher.afterTextChanged |
| SmbConnectDialog$3.<init> | REACHABLE | | TextWatcher constructor | SRC SmbConnectDialog.java TextWatcher instance |
| SmbConnectDialog$3.afterTextChanged | REACHABLE | | TextWatcher callback | SRC SmbConnectDialog.java TextWatcher.afterTextChanged |
| SmbConnectDialog$4.<init> | REACHABLE | | TextWatcher constructor | SRC SmbConnectDialog.java TextWatcher instance |
| SmbConnectDialog$4.afterTextChanged | REACHABLE | | TextWatcher callback | SRC SmbConnectDialog.java TextWatcher.afterTextChanged |
| SmbSearchDialog.<init> | REACHABLE | | Constructor | SRC SmbSearchDialog.java constructor |
| SmbSearchDialog.dismiss | REACHABLE | | Called to dismiss dialog | SRC SmbSearchDialog.java method |
| SmbSearchDialog.lambda$onCreateDialog$0 | REACHABLE | | Lambda in onCreateDialog | SRC SmbSearchDialog.java lambda |
| SmbSearchDialog.lambda$onCreateDialog$1 | REACHABLE | | Lambda in onCreateDialog | SRC SmbSearchDialog.java lambda |
| SmbSearchDialog.onCreate | REACHABLE | | DialogFragment lifecycle callback | SRC SmbSearchDialog.java framework callback |
| SmbSearchDialog.onCreateDialog | REACHABLE | | DialogFragment callback | SRC SmbSearchDialog.java framework callback |
| SmbSearchDialog$1.<init> | REACHABLE | | SmbSearchListener constructor | SRC SmbSearchDialog.java listener instance |
| SmbSearchDialog$1.computerFound | REACHABLE | | Listener callback | SRC SmbSearchDialog.java listener method |
| SmbSearchDialog$1.lambda$computerFound$0 | REACHABLE | | Lambda in computerFound | SRC SmbSearchDialog.java lambda |
| SmbSearchDialog$1.lambda$searchFinished$1 | REACHABLE | | Lambda in searchFinished | SRC SmbSearchDialog.java lambda |
| SmbSearchDialog$1.searchFinished | REACHABLE | | Listener callback | SRC SmbSearchDialog.java listener method |
| SmbSearchDialog$ElementViewHolder.<init> | REACHABLE | | ViewHolder constructor | SRC SmbSearchDialog.java ViewHolder |
| MainActivityHelper.addSearchFragment | REACHABLE | | Called to add search fragment | SRC MainActivityHelper.java method called from MainActivity |
| MainActivityHelper.compressFiles | REACHABLE | | Called to compress files | SRC MainActivityHelper.java method |
| MainActivityHelper.deleteFiles | REACHABLE | | Called to delete files | SRC MainActivityHelper.java method called from MainActivity |
| MainActivityHelper.isNewDirectoryRecursive | REACHABLE | | Helper to check directory recursion | SRC MainActivityHelper.java method |
| MainActivityHelper.lambda$guideDialogForLEXA$4 | REACHABLE | | Lambda in guideDialogForLEXA | SRC MainActivityHelper.java lambda |
| MainActivityHelper.lambda$guideDialogForLEXA$5 | REACHABLE | | Lambda in guideDialogForLEXA | SRC MainActivityHelper.java lambda |
| MainActivityHelper.lambda$mkdir$0 | REACHABLE | | Lambda in mkdir | SRC MainActivityHelper.java lambda |
| MainActivityHelper.lambda$mkdir$1 | REACHABLE | | Lambda in mkdir | SRC MainActivityHelper.java lambda |
| MainActivityHelper.lambda$mkfile$2 | REACHABLE | | Lambda in mkfile | SRC MainActivityHelper.java lambda |
| MainActivityHelper.lambda$mkfile$3 | REACHABLE | | Lambda in mkfile | SRC MainActivityHelper.java lambda |
| MainActivityHelper.mk | REACHABLE | | Called to create files/directories | SRC MainActivityHelper.java method |
| MainActivityHelper.mkDir | REACHABLE | | Called to create directory | SRC MainActivityHelper.java method |
| MainActivityHelper.mkFile | REACHABLE | | Called to create file | SRC MainActivityHelper.java method |
| MainActivityHelper.mkdir | REACHABLE | | Called to create directory with dialog | SRC MainActivityHelper.java method |
| MainActivityHelper.mkfile | REACHABLE | | Called to create file with dialog | SRC MainActivityHelper.java method |
| MainActivityHelper.rename | REACHABLE | | Called to rename files | SRC MainActivityHelper.java method |
| MainActivityHelper.search | REACHABLE | | Called to initiate search | SRC MainActivityHelper.java method |
| MainActivityHelper.triggerStorageAccessFramework | REACHABLE | | Called for SAF access | SRC MainActivityHelper.java method |
| MainActivityHelper$1.onReceive | REACHABLE | | BroadcastReceiver callback | SRC MainActivityHelper.java BroadcastReceiver.onReceive |
| MainActivityHelper$2.<init> | REACHABLE | | MkDirOperation constructor | SRC MainActivityHelper.java mkDir operation |
| MainActivityHelper$2.exists | REACHABLE | | Operation callback | SRC MainActivityHelper.java operation method |
| MainActivityHelper$2.invalidName | REACHABLE | | Operation callback | SRC MainActivityHelper.java operation method |
| MainActivityHelper$2.lambda$done$2 | REACHABLE | | Lambda in done | SRC MainActivityHelper.java lambda |
| MainActivityHelper$2.lambda$exists$0 | REACHABLE | | Lambda in exists | SRC MainActivityHelper.java lambda |
| MainActivityHelper$2.lambda$invalidName$3 | REACHABLE | | Lambda in invalidName | SRC MainActivityHelper.java lambda |
| MainActivityHelper$2.lambda$launchSAF$1 | REACHABLE | | Lambda in launchSAF | SRC MainActivityHelper.java lambda |
| MainActivityHelper$2.launchSAF(HybridFile) | REACHABLE | | SAF launcher overload | SRC MainActivityHelper.java method |
| MainActivityHelper$2.launchSAF(HybridFile,HybridFile) | REACHABLE | | SAF launcher overload | SRC MainActivityHelper.java method |
| MainActivityHelper$3.<init> | REACHABLE | | MkFileOperation constructor | SRC MainActivityHelper.java mkFile operation |
| MainActivityHelper$3.exists | REACHABLE | | Operation callback | SRC MainActivityHelper.java operation method |
| MainActivityHelper$3.invalidName | REACHABLE | | Operation callback | SRC MainActivityHelper.java operation method |
| MainActivityHelper$3.lambda$done$2 | REACHABLE | | Lambda in done | SRC MainActivityHelper.java lambda |
| MainActivityHelper$3.lambda$exists$0 | REACHABLE | | Lambda in exists | SRC MainActivityHelper.java lambda |
| MainActivityHelper$3.lambda$invalidName$3 | REACHABLE | | Lambda in invalidName | SRC MainActivityHelper.java lambda |
| MainActivityHelper$3.lambda$launchSAF$1 | REACHABLE | | Lambda in launchSAF | SRC MainActivityHelper.java lambda |
| MainActivityHelper$3.launchSAF(HybridFile) | REACHABLE | | SAF launcher overload | SRC MainActivityHelper.java method |
| MainActivityHelper$3.launchSAF(HybridFile,HybridFile) | REACHABLE | | SAF launcher overload | SRC MainActivityHelper.java method |
| MainActivityHelper$4.<init> | REACHABLE | | RenameOperation constructor | SRC MainActivityHelper.java rename operation |
| MainActivityHelper$4.exists | REACHABLE | | Operation callback | SRC MainActivityHelper.java operation method |
| MainActivityHelper$4.invalidName | REACHABLE | | Operation callback | SRC MainActivityHelper.java operation method |
| MainActivityHelper$4.lambda$done$2 | REACHABLE | | Lambda in done | SRC MainActivityHelper.java lambda |
| MainActivityHelper$4.lambda$exists$0 | REACHABLE | | Lambda in exists | SRC MainActivityHelper.java lambda |
| MainActivityHelper$4.lambda$invalidName$3 | REACHABLE | | Lambda in invalidName | SRC MainActivityHelper.java lambda |
| MainActivityHelper$4.lambda$launchSAF$1 | REACHABLE | | Lambda in launchSAF | SRC MainActivityHelper.java lambda |
| MainActivityHelper$4.launchSAF(HybridFile) | REACHABLE | | SAF launcher overload | SRC MainActivityHelper.java method |
| MainActivityHelper$4.launchSAF(HybridFile,HybridFile) | REACHABLE | | SAF launcher overload | SRC MainActivityHelper.java method |

STATUS: DONE
