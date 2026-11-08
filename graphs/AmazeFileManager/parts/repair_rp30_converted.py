# Converted from repair_rp30.py
# Original: 68 edges, Duplicates removed: 5, New: 63

e('SftpConnectDialog.lambda$onActivityResult$1', 'PemToKeyPairTask.<init>(InputStream,Callback)', 'CALL',
  'SftpConnectDialog instantiates PemToKeyPairTask with selected PEM key file InputStream',
  evidence='SRC PemToKeyPairTask.java:95-97: public PemToKeyPairTask(@NonNull InputStream pemFile, AsyncTaskResult.Callback<KeyPair> callback) throws IOException { this(IOUtils.readFully(pemFile).toByteArray(), callback); }; caller site found via grep')

e('PemToKeyPairTask.<init>(InputStream,Callback)', 'PemToKeyPairTask.<init>(byte[],Callback)', 'CALL',
  'Constructor delegates to private byte array constructor after reading InputStream',
  evidence='SRC PemToKeyPairTask.java:95-97: public PemToKeyPairTask(@NonNull InputStream pemFile, AsyncTaskResult.Callback<KeyPair> callback) throws IOException { this(IOUtils.readFully(pemFile).toByteArray(), callback); }')

e('AndroidAsyncTask.execute', 'PemToKeyPairTask.doInBackground', 'ASYNC',
  'AsyncTask framework calls doInBackground on background thread',
  evidence='SRC PemToKeyPairTask.java:108-131: @Override protected KeyPair doInBackground(Void... voids) { while(true) { if (isCancelled()) return null; if (paused) continue; for (PemToKeyPairConverter converter : converters) { KeyPair keyPair = converter.convert(new String(pemFile)); if (keyPair != null) { paused = false; return keyPair; } } ... publishProgress(new IOException(...)); } }')

e('PemToKeyPairTask.doInBackground', 'PemToKeyPairTask$PemToKeyPairConverter.convert', 'CALL',
  'doInBackground tries each converter to parse PEM key',
  evidence='SRC PemToKeyPairTask.java:115: KeyPair keyPair = converter.convert(new String(pemFile));')

e('PemToKeyPairTask.doInBackground', 'AndroidAsyncTask.publishProgress', 'CALL',
  'doInBackground publishes progress when no converter can parse the key',
  evidence='SRC PemToKeyPairTask.java:125: publishProgress(new IOException("No converter available to parse selected PEM"));')

e('AndroidAsyncTask.publishProgress', 'PemToKeyPairTask.onProgressUpdate', 'ASYNC',
  'AsyncTask framework delivers progress update to onProgressUpdate on UI thread',
  evidence='SRC PemToKeyPairTask.java:133-175: @Override protected void onProgressUpdate(IOException... values) { ... MaterialDialog.Builder builder = new MaterialDialog.Builder(...); ... builder.onPositive(((dialog, which) -> { ... })).onNegative(((dialog, which) -> { ... toastOnParseError(result); ... })); ... }')

e('PemToKeyPairTask.lambda$onProgressUpdate$0', 'PemToKeyPairTask$1.<init>', 'CALL',
  'Lambda creates anonymous PasswordFinder implementation',
  evidence='SRC PemToKeyPairTask.java:148-156: this.passwordFinder = new PasswordFinder() { @Override public char[] reqPassword(Resource<?> resource) { return textfield.getText().toString().toCharArray(); } @Override public boolean shouldRetry(Resource<?> resource) { return false; } };')

e('PemToKeyPairTask.lambda$onProgressUpdate$1', 'AndroidAsyncTask.cancel', 'CALL',
  'Negative button lambda cancels the AsyncTask',
  evidence='SRC PemToKeyPairTask.java:162: cancel(true);')

e('PemToKeyPairTask.onProgressUpdate', 'PemToKeyPairTask.lambda$onProgressUpdate$2', 'GUI',
  'onProgressUpdate registers lambda as text validation callback',
  evidence='SRC PemToKeyPairTask.java:167-172: new WarnableTextInputValidator(AppConfig.getInstance().getMainActivityContext(), textfield, wilTextfield, dialog.getActionButton(DialogAction.POSITIVE), (text) -> { if (text.length() < 1) { return new WarnableTextInputValidator.ReturnState(...); } return new WarnableTextInputValidator.ReturnState(); })')

e('AndroidAsyncTask.doInBackground', 'PemToKeyPairTask.onPostExecute', 'ASYNC',
  'AsyncTask framework calls onPostExecute on UI thread with result from doInBackground',
  evidence='SRC PemToKeyPairTask.java:177-181: @Override protected void onPostExecute(KeyPair result) { if(callback != null) { callback.onResult(result); } }')

e('PemToKeyPairTask.onPostExecute', 'AsyncTaskResult$Callback.onResult', 'CALL',
  'onPostExecute delivers KeyPair result to callback',
  evidence='SRC PemToKeyPairTask.java:179: callback.onResult(result);')

e('PemToKeyPairTask.toastOnParseError', 'Toast.makeText', 'CALL',
  'toastOnParseError shows error toast with parse error message',
  evidence='SRC PemToKeyPairTask.java:183-186: Toast.makeText(AppConfig.getInstance().getMainActivityContext(), AppConfig.getInstance().getResources().getString(R.string.ssh_pem_key_parse_error, result.getLocalizedMessage()), Toast.LENGTH_LONG).show();')

e('PemToKeyPairTask$1.<init>', 'Object.<init>', 'CALL',
  'Anonymous PasswordFinder constructor chains to Object constructor',
  evidence='SRC PemToKeyPairTask.java:148: new PasswordFinder() (implicit super() call)')

e('PemToKeyPairTask$OpenSshPemToKeyPairConverter.throwingConvert', 'PemToKeyPairTask$1.reqPassword', 'CALL',
  'OpenSSH converter calls reqPassword when password-protected key needs decryption',
  evidence='SRC PemToKeyPairTask.java:213: converter.init(new StringReader(source), passwordFinder); sshj library OpenSSHKeyFile.init will call passwordFinder.reqPassword if key is encrypted')

e('PemToKeyPairTask$OpenSshV1PemToKeyPairConverter.throwingConvert', 'PemToKeyPairTask$1.reqPassword', 'CALL',
  'OpenSSH v1 converter calls reqPassword when password-protected key needs decryption',
  evidence='SRC PemToKeyPairTask.java:220: converter.init(new StringReader(source), passwordFinder); sshj library OpenSSHKeyV1KeyFile.init will call passwordFinder.reqPassword if key is encrypted')

e('PemToKeyPairTask$PuttyPrivateKeyToKeyPairConverter.throwingConvert', 'PemToKeyPairTask$1.reqPassword', 'CALL',
  'PuTTY converter calls reqPassword when password-protected key needs decryption',
  evidence='SRC PemToKeyPairTask.java:227: converter.init(new StringReader(source), passwordFinder); sshj library PuTTYKeyFile.init will call passwordFinder.reqPassword if key is encrypted')

e('PemToKeyPairTask$OpenSshPemToKeyPairConverter.throwingConvert', 'PemToKeyPairTask$1.shouldRetry', 'CALL',
  'OpenSSH converter calls shouldRetry to check if password retry is allowed',
  evidence='SRC PemToKeyPairTask.java:154-156: @Override public boolean shouldRetry(Resource<?> resource) { return false; }; called by sshj library after password attempt')

e('PemToKeyPairTask$OpenSshV1PemToKeyPairConverter.throwingConvert', 'PemToKeyPairTask$1.shouldRetry', 'CALL',
  'OpenSSH v1 converter calls shouldRetry to check if password retry is allowed',
  evidence='SRC PemToKeyPairTask.java:154-156: @Override public boolean shouldRetry(Resource<?> resource) { return false; }; called by sshj library after password attempt')

e('PemToKeyPairTask$PuttyPrivateKeyToKeyPairConverter.throwingConvert', 'PemToKeyPairTask$1.shouldRetry', 'CALL',
  'PuTTY converter calls shouldRetry to check if password retry is allowed',
  evidence='SRC PemToKeyPairTask.java:154-156: @Override public boolean shouldRetry(Resource<?> resource) { return false; }; called by sshj library after password attempt')

e('AndroidFragment.onCreate', 'PrefFrag.onCreate', 'FRAMEWORK',
  'Android framework calls onCreate when fragment is created',
  evidence='SRC PrefFrag.java:69-121: @Override public void onCreate(Bundle savedInstanceState) { super.onCreate(savedInstanceState); utilsProvider = ((BasicActivity) getActivity()).getUtilsProvider(); addPreferencesFromResource(R.xml.preferences); ... }')

e('PrefFrag.onCreate', 'PrefFrag.lambda$onCreate$0', 'GUI',
  'onCreate registers lambda as onPreferenceChangeListener for fingerprint checkbox',
  evidence='SRC PrefFrag.java:94-111: checkBoxFingerprint.setOnPreferenceChangeListener((preference, newValue) -> { ... });')

e('PrefFrag.lambda$onCreate$0', 'Toast.makeText', 'CALL',
  'Lambda shows toast when fingerprint permission checks fail',
  evidence='SRC PrefFrag.java:97-99, 103-105, 108-110: Toast.makeText calls for various fingerprint setup failures')

e('AndroidFragment.onCreateView', 'PrefFrag.onCreateView', 'FRAMEWORK',
  'Android framework calls onCreateView to inflate fragment layout',
  evidence='SRC PrefFrag.java:268-274: @Override public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) { View v = super.onCreateView(inflater, container, savedInstanceState); listView = v.findViewById(android.R.id.list); return v; }')

e('AndroidPreference.onClick', 'PrefFrag.onPreferenceClick', 'FRAMEWORK',
  'Android framework calls onPreferenceClick when user taps a preference',
  evidence='SRC PrefFrag.java:125-266: @Override public boolean onPreferenceClick(Preference preference) { ... switch (preference.getKey()) { ... } }')

e('PrefFrag.onPreferenceClick', 'PrefFrag.lambda$onPreferenceClick$1', 'GUI',
  'onPreferenceClick registers lambda for grid columns dialog item selection',
  evidence='SRC PrefFrag.java:135-140: builder.items(sort).itemsCallbackSingleChoice(current, (dialog, view, which, text) -> { ... })')

e('PrefFrag.onPreferenceClick', 'PrefFrag.lambda$onPreferenceClick$2', 'GUI',
  'onPreferenceClick registers lambda for theme dialog item selection',
  evidence='SRC PrefFrag.java:147-152: builder.items(sort).itemsCallbackSingleChoice(current, (dialog, view, which, text) -> { ... })')

e('PrefFrag.onPreferenceClick', 'PrefFrag.lambda$onPreferenceClick$3', 'GUI',
  'onPreferenceClick registers lambda for master password dialog input callback',
  evidence='SRC PrefFrag.java:227: masterPasswordDialogBuilder.input(..., (dialog, input) -> { });')

e('PrefFrag.onPreferenceClick', 'PrefFrag.lambda$onPreferenceClick$4', 'GUI',
  'onPreferenceClick registers lambda as positive button action for master password dialog',
  evidence='SRC PrefFrag.java:233-248: masterPasswordDialogBuilder.onPositive((dialog, which) -> { ... })')

e('PrefFrag.onPreferenceClick', 'PrefFrag.lambda$onPreferenceClick$5', 'GUI',
  'onPreferenceClick registers lambda as negative button action for master password dialog',
  evidence='SRC PrefFrag.java:250: masterPasswordDialogBuilder.onNegative((dialog, which) -> dialog.cancel())')

e('PrefFrag.onPreferenceClick', 'PrefFrag.restartPC', 'CALL',
  'onPreferenceClick calls restartPC to restart activity after theme change',
  evidence='SRC PrefFrag.java:150: restartPC(getActivity());')

e('PrefFrag.lambda$onPreferenceClick$1', 'SharedPreferences$Editor.putString', 'CALL',
  'Lambda saves grid column preference',
  evidence='SRC PrefFrag.java:137: sharedPref.edit().putString(PreferencesConstants.PREFERENCE_GRID_COLUMNS, "" + (which != 0 ? sort[which] : "" + -1)).commit();')

e('PrefFrag.lambda$onPreferenceClick$2', 'PrefFrag.restartPC', 'CALL',
  'Lambda restarts activity after theme selection',
  evidence='SRC PrefFrag.java:150: restartPC(getActivity());')

e('PrefFrag.lambda$onPreferenceClick$4', 'SharedPreferences$Editor.putString', 'CALL',
  'Lambda saves encrypted master password to SharedPreferences',
  evidence='SRC PrefFrag.java:239-241: sharedPref.edit().putString(PreferencesConstants.PREFERENCE_CRYPT_MASTER_PASSWORD, CryptUtil.encryptPassword(getActivity(), dialog.getInputEditText().getText().toString())).apply();')

e('PrefFrag.restartPC', 'Activity.finish', 'CALL',
  'restartPC finishes current activity',
  evidence='SRC PrefFrag.java:260: activity.finish();')

e('PrefFrag.restartPC', 'Activity.startActivity', 'CALL',
  'restartPC starts new instance of activity',
  evidence='SRC PrefFrag.java:262: activity.startActivity(activity.getIntent());')

e('AndroidAsyncTask.execute', 'PrepareCopyTask.onPreExecute', 'ASYNC',
  'AsyncTask framework calls onPreExecute on UI thread before background work starts',
  evidence='SRC PrepareCopyTask.java:74-77: @Override protected void onPreExecute() { super.onPreExecute(); dialog = ProgressDialog.show(context, "", context.getString(R.string.processing), true); }')

e('PrepareCopyTask.onPreExecute', 'ProgressDialog.show', 'CALL',
  'onPreExecute shows indeterminate progress dialog',
  evidence='SRC PrepareCopyTask.java:76: dialog = ProgressDialog.show(context, "", context.getString(R.string.processing), true);')

e('AndroidAsyncTask.execute', 'PrepareCopyTask.doInBackground', 'ASYNC',
  'AsyncTask framework calls doInBackground on background thread',
  evidence='SRC PrepareCopyTask.java:84-117: @Override protected CopyNode doInBackground(ArrayList<HybridFileParcelable>... params) { ... }')

e('PrepareCopyTask.doInBackground', 'PrepareCopyTask$CopyNode.<init>', 'CALL',
  'doInBackground creates root CopyNode with file list',
  evidence='SRC PrepareCopyTask.java:113: copyFolder = new CopyNode(path, filesToCopy);')

e('PrepareCopyTask.checkConflicts', 'PrepareCopyTask.lambda$checkConflicts$0', 'CALL',
  'checkConflicts uses lambda to iterate children via forEachChildrenFile',
  evidence='SRC PrepareCopyTask.java:121-127: destination.forEachChildrenFile(context, rootMode, file -> { for (HybridFileParcelable j : filesToCopy) { if (file.getName().equals((j).getName())) { conflictingFiles.add(j); } } });')

e('AndroidAsyncTask.doInBackground', 'PrepareCopyTask.onPostExecute', 'ASYNC',
  'AsyncTask framework calls onPostExecute on UI thread with result from doInBackground',
  evidence='SRC PrepareCopyTask.java:131-150: @Override protected void onPostExecute(CopyNode copyFolder) { ... }')

e('PrepareCopyTask.onPostExecute', 'PrepareCopyTask.startService', 'CALL',
  'onPostExecute starts CopyService for special open modes',
  evidence='SRC PrepareCopyTask.java:141: startService(filesToCopy, path, openMode);')

e('PrepareCopyTask.onPostExecute', 'PrepareCopyTask.onEndDialog', 'CALL',
  'onPostExecute delegates to onEndDialog for normal file system copies',
  evidence='SRC PrepareCopyTask.java:145: onEndDialog(null, null, null);')

e('PrepareCopyTask.startService', 'CopyService.<init>', 'CALL',
  'startService creates Intent for CopyService',
  evidence='SRC PrepareCopyTask.java:153: Intent intent = new Intent(context, CopyService.class);')

e('PrepareCopyTask.showDialog', 'PrepareCopyTask.lambda$showDialog$1', 'GUI',
  'showDialog registers lambda for positive button (skip) action',
  evidence='SRC PrepareCopyTask.java:198-202: dialogBuilder.onPositive((dialog, which) -> { if (checkBox.isChecked()) dialogState = DO_FOR_ALL_ELEMENTS.DO_NOT_REPLACE; doNotReplaceFiles(path, filesToCopy, conflictingFiles); })')

e('PrepareCopyTask.showDialog', 'PrepareCopyTask.lambda$showDialog$2', 'GUI',
  'showDialog registers lambda for negative button (overwrite) action',
  evidence='SRC PrepareCopyTask.java:203-207: dialogBuilder.onNegative((dialog, which) -> { if (checkBox.isChecked()) dialogState = DO_FOR_ALL_ELEMENTS.REPLACE; replaceFiles(path, filesToCopy, conflictingFiles); })')

e('PrepareCopyTask.lambda$showDialog$1', 'PrepareCopyTask.doNotReplaceFiles', 'CALL',
  'Skip button lambda calls doNotReplaceFiles',
  evidence='SRC PrepareCopyTask.java:201: doNotReplaceFiles(path, filesToCopy, conflictingFiles);')

e('PrepareCopyTask.lambda$showDialog$2', 'PrepareCopyTask.replaceFiles', 'CALL',
  'Overwrite button lambda calls replaceFiles',
  evidence='SRC PrepareCopyTask.java:206: replaceFiles(path, filesToCopy, conflictingFiles);')

e('PrepareCopyTask.onEndDialog', 'PrepareCopyTask.showDialog', 'CALL',
  'onEndDialog shows conflict resolution dialog when needed',
  evidence='SRC PrepareCopyTask.java:226: showDialog(path, filesToCopy, conflictingFiles);')

e('PrepareCopyTask.onEndDialog', 'PrepareCopyTask.doNotReplaceFiles', 'CALL',
  'onEndDialog skips files when DO_NOT_REPLACE state is set',
  evidence='SRC PrepareCopyTask.java:228: doNotReplaceFiles(path, filesToCopy, conflictingFiles);')

e('PrepareCopyTask.onEndDialog', 'PrepareCopyTask.replaceFiles', 'CALL',
  'onEndDialog replaces files when REPLACE state is set',
  evidence='SRC PrepareCopyTask.java:230: replaceFiles(path, filesToCopy, conflictingFiles);')

e('PrepareCopyTask.onEndDialog', 'PrepareCopyTask$CopyNode.startCopy', 'CALL',
  'onEndDialog starts BFS traversal of copy node tree',
  evidence='SRC PrepareCopyTask.java:232: CopyNode c = !copyFolder.hasStarted()? copyFolder.startCopy():copyFolder.goToNextNode();')

e('PrepareCopyTask.onEndDialog', 'PrepareCopyTask$CopyNode.goToNextNode', 'CALL',
  'onEndDialog advances to next node in BFS traversal',
  evidence='SRC PrepareCopyTask.java:232: CopyNode c = !copyFolder.hasStarted()? copyFolder.startCopy():copyFolder.goToNextNode();')

e('PrepareCopyTask.doNotReplaceFiles', 'PrepareCopyTask.onEndDialog', 'CALL',
  'doNotReplaceFiles recurses to onEndDialog to process next files',
  evidence='SRC PrepareCopyTask.java:260: onEndDialog(path, filesToCopy, conflictingFiles);')

e('PrepareCopyTask.replaceFiles', 'PrepareCopyTask.onEndDialog', 'CALL',
  'replaceFiles recurses to onEndDialog to process next files',
  evidence='SRC PrepareCopyTask.java:273: onEndDialog(path, filesToCopy, conflictingFiles);')

e('PrepareCopyTask$CopyNode.<init>', 'PrepareCopyTask.checkConflicts', 'CALL',
  'CopyNode constructor calls checkConflicts to find name collisions',
  evidence='SRC PrepareCopyTask.java:301: conflictingFiles = checkConflicts(filesToCopy, destination);')

e('PrepareCopyTask$CopyNode.<init>', 'PrepareCopyTask$CopyNode.<init>', 'CALL',
  'CopyNode constructor recursively creates child nodes for conflicting directories',
  evidence='SRC PrepareCopyTask.java:309-312: nextNodes.add(new CopyNode(path + "/" + conflictingFiles.get(i).getName(), conflictingFiles.get(i).listFiles(context, rootMode)));')

e('PrepareCopyTask$CopyNode.startCopy', 'PrepareCopyTask$CopyNode.<init>', 'FRAMEWORK',
  'startCopy initializes BFS queue and visited set',
  evidence='SRC PrepareCopyTask.java:327-330: queue = new LinkedList<>(); visited = new HashSet<>(); queue.add(this); visited.add(this); (implicit reference to this node)')

e('PrepareCopyTask$CopyNode.goToNextNode', 'PrepareCopyTask$CopyNode.getUnvisitedChildNode', 'CALL',
  'goToNextNode gets next unvisited child for BFS traversal',
  evidence='SRC PrepareCopyTask.java:342: CopyNode child; if ((child = getUnvisitedChildNode(visited, node)) != null) { ... }')

e('PrepareCopyTask$CopyNode.goToNextNode', 'PrepareCopyTask$CopyNode.goToNextNode', 'CALL',
  'goToNextNode recursively processes queue until finding next node',
  evidence='SRC PrepareCopyTask.java:348: return goToNextNode();')

e('AndroidServiceConnection.onServiceConnected', 'ProcessViewerFragment$CustomServiceConnection.onServiceConnected', 'FRAMEWORK',
  'Android framework calls onServiceConnected when service binding completes',
  evidence='SRC ProcessViewerFragment.java:315-333: @Override public void onServiceConnected(ComponentName name, IBinder service) { ... }')

e('ProcessViewerFragment$CustomServiceConnection.onServiceConnected', 'ProcessViewerFragment.processResults', 'CALL',
  'onServiceConnected calls processResults for each existing data package',
  evidence='SRC ProcessViewerFragment.java:321: fragment.processResults(dataPackage, serviceType);')

e('ProcessViewerFragment$CustomServiceConnection$1.<init>', 'Object.<init>', 'CALL',
  'Anonymous ProgressListener constructor chains to Object',
  evidence='SRC ProcessViewerFragment.java:326: new AbstractProgressiveService.ProgressListener() (implicit super() call)')

# UNREACHABLE entries

UNREACHABLE['PemToKeyPairTask$1.reqPassword'] = ('framework_never_calls', 'reqPassword is called by sshj library (OpenSSHKeyFile, OpenSSHKeyV1KeyFile, PuTTYKeyFile) when password is needed for encrypted keys. However, this PasswordFinder instance is only created when user clicks the positive button after entering password (PemToKeyPairTask.java:148-156). The doInBackground loop (lines 110-126) runs converters before the dialog is shown, so the first iteration always uses passwordFinder=null. After dialog interaction, passwordFinder is set, doInBackground resumes and converters.init() calls reqPassword. This IS reachable when user has encrypted PEM key.', 'SRC PemToKeyPairTask.java:150-152: @Override public char[] reqPassword(Resource<?> resource) { return textfield.getText().toString().toCharArray(); }; called from sshj library converters', 'INFERRED')
