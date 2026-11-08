# repair_rp30.py - Batch 30 repairs

def edge(src, dst, kind, summary='', evidence=''):
    """Schema-2 edge format"""
    return {'src': src, 'dst': dst, 'kind': kind, 'summary': summary, 'evidence': evidence}

EDGES = []

# ===== PemToKeyPairTask methods =====

# PemToKeyPairTask.<init>(InputStream,Callback)
# Called from SftpConnectDialog when user selects PEM key file
# SRC SftpConnectDialog.java:~195 (grep shows this location)
# SRC PemToKeyPairTask.java:95-97
EDGES.append(edge(
    'SftpConnectDialog.lambda$onActivityResult$1',
    'PemToKeyPairTask.<init>(InputStream,Callback)',
    'CALL',
    'SftpConnectDialog instantiates PemToKeyPairTask with selected PEM key file InputStream',
    'SRC PemToKeyPairTask.java:95-97: public PemToKeyPairTask(@NonNull InputStream pemFile, AsyncTaskResult.Callback<KeyPair> callback) throws IOException { this(IOUtils.readFully(pemFile).toByteArray(), callback); }; caller site found via grep'
))

EDGES.append(edge(
    'PemToKeyPairTask.<init>(InputStream,Callback)',
    'PemToKeyPairTask.<init>(byte[],Callback)',
    'CALL',
    'Constructor delegates to private byte array constructor after reading InputStream',
    'SRC PemToKeyPairTask.java:95-97: public PemToKeyPairTask(@NonNull InputStream pemFile, AsyncTaskResult.Callback<KeyPair> callback) throws IOException { this(IOUtils.readFully(pemFile).toByteArray(), callback); }'
))

# PemToKeyPairTask.doInBackground
# AsyncTask framework calls this after .execute()
# SRC PemToKeyPairTask.java:108-131
EDGES.append(edge(
    'AndroidAsyncTask.execute',
    'PemToKeyPairTask.doInBackground',
    'ASYNC',
    'AsyncTask framework calls doInBackground on background thread',
    'SRC PemToKeyPairTask.java:108-131: @Override protected KeyPair doInBackground(Void... voids) { while(true) { if (isCancelled()) return null; if (paused) continue; for (PemToKeyPairConverter converter : converters) { KeyPair keyPair = converter.convert(new String(pemFile)); if (keyPair != null) { paused = false; return keyPair; } } ... publishProgress(new IOException(...)); } }'
))

EDGES.append(edge(
    'PemToKeyPairTask.doInBackground',
    'PemToKeyPairTask$PemToKeyPairConverter.convert',
    'CALL',
    'doInBackground tries each converter to parse PEM key',
    'SRC PemToKeyPairTask.java:115: KeyPair keyPair = converter.convert(new String(pemFile));'
))

EDGES.append(edge(
    'PemToKeyPairTask.doInBackground',
    'AndroidAsyncTask.publishProgress',
    'CALL',
    'doInBackground publishes progress when no converter can parse the key',
    'SRC PemToKeyPairTask.java:125: publishProgress(new IOException("No converter available to parse selected PEM"));'
))

# PemToKeyPairTask.onProgressUpdate
# AsyncTask framework calls this on UI thread after publishProgress
# SRC PemToKeyPairTask.java:133-175
EDGES.append(edge(
    'AndroidAsyncTask.publishProgress',
    'PemToKeyPairTask.onProgressUpdate',
    'ASYNC',
    'AsyncTask framework delivers progress update to onProgressUpdate on UI thread',
    'SRC PemToKeyPairTask.java:133-175: @Override protected void onProgressUpdate(IOException... values) { ... MaterialDialog.Builder builder = new MaterialDialog.Builder(...); ... builder.onPositive(((dialog, which) -> { ... })).onNegative(((dialog, which) -> { ... toastOnParseError(result); ... })); ... }'
))

# Lambdas inside onProgressUpdate
# lambda$onProgressUpdate$0 - the onPositive listener lambda
# SRC PemToKeyPairTask.java:147-157
EDGES.append(edge(
    'PemToKeyPairTask.onProgressUpdate',
    'PemToKeyPairTask.lambda$onProgressUpdate$0',
    'GUI',
    'onProgressUpdate registers lambda as positive button listener in MaterialDialog',
    'SRC PemToKeyPairTask.java:147-157: builder.onPositive(((dialog, which) -> { this.passwordFinder = new PasswordFinder() { @Override public char[] reqPassword(Resource<?> resource) { return textfield.getText().toString().toCharArray(); } @Override public boolean shouldRetry(Resource<?> resource) { return false; } }; this.paused = false; dialog.dismiss(); }))'
))

EDGES.append(edge(
    'PemToKeyPairTask.lambda$onProgressUpdate$0',
    'PemToKeyPairTask$1.<init>',
    'CALL',
    'Lambda creates anonymous PasswordFinder implementation',
    'SRC PemToKeyPairTask.java:148-156: this.passwordFinder = new PasswordFinder() { @Override public char[] reqPassword(Resource<?> resource) { return textfield.getText().toString().toCharArray(); } @Override public boolean shouldRetry(Resource<?> resource) { return false; } };'
))

# lambda$onProgressUpdate$1 - the onNegative listener lambda
# SRC PemToKeyPairTask.java:159-163
EDGES.append(edge(
    'PemToKeyPairTask.onProgressUpdate',
    'PemToKeyPairTask.lambda$onProgressUpdate$1',
    'GUI',
    'onProgressUpdate registers lambda as negative button listener in MaterialDialog',
    'SRC PemToKeyPairTask.java:159-163: .onNegative(((dialog, which) -> { dialog.dismiss(); toastOnParseError(result); cancel(true); }))'
))

EDGES.append(edge(
    'PemToKeyPairTask.lambda$onProgressUpdate$1',
    'PemToKeyPairTask.toastOnParseError',
    'CALL',
    'Negative button lambda calls toastOnParseError to show error message',
    'SRC PemToKeyPairTask.java:161: toastOnParseError(result);'
))

EDGES.append(edge(
    'PemToKeyPairTask.lambda$onProgressUpdate$1',
    'AndroidAsyncTask.cancel',
    'CALL',
    'Negative button lambda cancels the AsyncTask',
    'SRC PemToKeyPairTask.java:162: cancel(true);'
))

# lambda$onProgressUpdate$2 - the WarnableTextInputValidator lambda
# SRC PemToKeyPairTask.java:167-172
EDGES.append(edge(
    'PemToKeyPairTask.onProgressUpdate',
    'PemToKeyPairTask.lambda$onProgressUpdate$2',
    'GUI',
    'onProgressUpdate registers lambda as text validation callback',
    'SRC PemToKeyPairTask.java:167-172: new WarnableTextInputValidator(AppConfig.getInstance().getMainActivityContext(), textfield, wilTextfield, dialog.getActionButton(DialogAction.POSITIVE), (text) -> { if (text.length() < 1) { return new WarnableTextInputValidator.ReturnState(...); } return new WarnableTextInputValidator.ReturnState(); })'
))

# PemToKeyPairTask.onPostExecute
# AsyncTask framework calls this on UI thread when doInBackground completes
# SRC PemToKeyPairTask.java:177-181
EDGES.append(edge(
    'AndroidAsyncTask.doInBackground',
    'PemToKeyPairTask.onPostExecute',
    'ASYNC',
    'AsyncTask framework calls onPostExecute on UI thread with result from doInBackground',
    'SRC PemToKeyPairTask.java:177-181: @Override protected void onPostExecute(KeyPair result) { if(callback != null) { callback.onResult(result); } }'
))

EDGES.append(edge(
    'PemToKeyPairTask.onPostExecute',
    'AsyncTaskResult$Callback.onResult',
    'CALL',
    'onPostExecute delivers KeyPair result to callback',
    'SRC PemToKeyPairTask.java:179: callback.onResult(result);'
))

# PemToKeyPairTask.toastOnParseError
# SRC PemToKeyPairTask.java:183-186
EDGES.append(edge(
    'PemToKeyPairTask.toastOnParseError',
    'Toast.makeText',
    'CALL',
    'toastOnParseError shows error toast with parse error message',
    'SRC PemToKeyPairTask.java:183-186: Toast.makeText(AppConfig.getInstance().getMainActivityContext(), AppConfig.getInstance().getResources().getString(R.string.ssh_pem_key_parse_error, result.getLocalizedMessage()), Toast.LENGTH_LONG).show();'
))

# PemToKeyPairTask$1 methods (anonymous PasswordFinder implementation)
# PemToKeyPairTask$1.<init>
# Created by lambda$onProgressUpdate$0
EDGES.append(edge(
    'PemToKeyPairTask$1.<init>',
    'Object.<init>',
    'CALL',
    'Anonymous PasswordFinder constructor chains to Object constructor',
    'SRC PemToKeyPairTask.java:148: new PasswordFinder() (implicit super() call)'
))

# PemToKeyPairTask$1.reqPassword
# Called by sshj library converters when password is needed
# SRC PemToKeyPairTask.java:150-152
UNREACHABLE['PemToKeyPairTask$1.reqPassword'] = (
    'framework_never_calls',
    'reqPassword is called by sshj library (OpenSSHKeyFile, OpenSSHKeyV1KeyFile, PuTTYKeyFile) when password is needed for encrypted keys. However, this PasswordFinder instance is only created when user clicks the positive button after entering password (PemToKeyPairTask.java:148-156). The doInBackground loop (lines 110-126) runs converters before the dialog is shown, so the first iteration always uses passwordFinder=null. After dialog interaction, passwordFinder is set, doInBackground resumes and converters.init() calls reqPassword. This IS reachable when user has encrypted PEM key.',
    'SRC PemToKeyPairTask.java:150-152: @Override public char[] reqPassword(Resource<?> resource) { return textfield.getText().toString().toCharArray(); }; called from sshj library converters',
    'INFERRED'
)

# Wait, I need to reconsider. Let me check if this is actually reachable...
# Looking at the code flow:
# 1. doInBackground starts, tries converters with passwordFinder=null
# 2. If key is encrypted, converters fail
# 3. publishProgress is called
# 4. onProgressUpdate shows dialog
# 5. User enters password and clicks OK
# 6. lambda sets passwordFinder and paused=false
# 7. doInBackground loop continues
# 8. Converter.convert calls converter.init(reader, passwordFinder)
# 9. init() eventually calls passwordFinder.reqPassword()

# Actually this IS REACHABLE! Let me create the edge instead.

# Remove UNREACHABLE and add edges
EDGES.append(edge(
    'PemToKeyPairTask$OpenSshPemToKeyPairConverter.throwingConvert',
    'PemToKeyPairTask$1.reqPassword',
    'CALL',
    'OpenSSH converter calls reqPassword when password-protected key needs decryption',
    'SRC PemToKeyPairTask.java:213: converter.init(new StringReader(source), passwordFinder); sshj library OpenSSHKeyFile.init will call passwordFinder.reqPassword if key is encrypted'
))

EDGES.append(edge(
    'PemToKeyPairTask$OpenSshV1PemToKeyPairConverter.throwingConvert',
    'PemToKeyPairTask$1.reqPassword',
    'CALL',
    'OpenSSH v1 converter calls reqPassword when password-protected key needs decryption',
    'SRC PemToKeyPairTask.java:220: converter.init(new StringReader(source), passwordFinder); sshj library OpenSSHKeyV1KeyFile.init will call passwordFinder.reqPassword if key is encrypted'
))

EDGES.append(edge(
    'PemToKeyPairTask$PuttyPrivateKeyToKeyPairConverter.throwingConvert',
    'PemToKeyPairTask$1.reqPassword',
    'CALL',
    'PuTTY converter calls reqPassword when password-protected key needs decryption',
    'SRC PemToKeyPairTask.java:227: converter.init(new StringReader(source), passwordFinder); sshj library PuTTYKeyFile.init will call passwordFinder.reqPassword if key is encrypted'
))

# PemToKeyPairTask$1.shouldRetry
# Called by sshj library after reqPassword
# SRC PemToKeyPairTask.java:154-156
EDGES.append(edge(
    'PemToKeyPairTask$OpenSshPemToKeyPairConverter.throwingConvert',
    'PemToKeyPairTask$1.shouldRetry',
    'CALL',
    'OpenSSH converter calls shouldRetry to check if password retry is allowed',
    'SRC PemToKeyPairTask.java:154-156: @Override public boolean shouldRetry(Resource<?> resource) { return false; }; called by sshj library after password attempt'
))

EDGES.append(edge(
    'PemToKeyPairTask$OpenSshV1PemToKeyPairConverter.throwingConvert',
    'PemToKeyPairTask$1.shouldRetry',
    'CALL',
    'OpenSSH v1 converter calls shouldRetry to check if password retry is allowed',
    'SRC PemToKeyPairTask.java:154-156: @Override public boolean shouldRetry(Resource<?> resource) { return false; }; called by sshj library after password attempt'
))

EDGES.append(edge(
    'PemToKeyPairTask$PuttyPrivateKeyToKeyPairConverter.throwingConvert',
    'PemToKeyPairTask$1.shouldRetry',
    'CALL',
    'PuTTY converter calls shouldRetry to check if password retry is allowed',
    'SRC PemToKeyPairTask.java:154-156: @Override public boolean shouldRetry(Resource<?> resource) { return false; }; called by sshj library after password attempt'
))

# ===== PrefFrag methods =====

# PrefFrag.onCreate
# Framework calls onCreate when fragment is created
# SRC PrefFrag.java:69-121
EDGES.append(edge(
    'AndroidFragment.onCreate',
    'PrefFrag.onCreate',
    'FRAMEWORK',
    'Android framework calls onCreate when fragment is created',
    'SRC PrefFrag.java:69-121: @Override public void onCreate(Bundle savedInstanceState) { super.onCreate(savedInstanceState); utilsProvider = ((BasicActivity) getActivity()).getUtilsProvider(); addPreferencesFromResource(R.xml.preferences); ... }'
))

EDGES.append(edge(
    'PrefFrag.onCreate',
    'PrefFrag.lambda$onCreate$0',
    'GUI',
    'onCreate registers lambda as onPreferenceChangeListener for fingerprint checkbox',
    'SRC PrefFrag.java:94-111: checkBoxFingerprint.setOnPreferenceChangeListener((preference, newValue) -> { ... });'
))

# PrefFrag.lambda$onCreate$0
# The fingerprint checkbox change listener
# SRC PrefFrag.java:94-111
EDGES.append(edge(
    'PrefFrag.lambda$onCreate$0',
    'Toast.makeText',
    'CALL',
    'Lambda shows toast when fingerprint permission checks fail',
    'SRC PrefFrag.java:97-99, 103-105, 108-110: Toast.makeText calls for various fingerprint setup failures'
))

# PrefFrag.onCreateView
# Framework calls onCreateView to create the fragment view
# SRC PrefFrag.java:268-274
EDGES.append(edge(
    'AndroidFragment.onCreateView',
    'PrefFrag.onCreateView',
    'FRAMEWORK',
    'Android framework calls onCreateView to inflate fragment layout',
    'SRC PrefFrag.java:268-274: @Override public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) { View v = super.onCreateView(inflater, container, savedInstanceState); listView = v.findViewById(android.R.id.list); return v; }'
))

# PrefFrag.onPreferenceClick
# Called when user clicks a preference
# SRC PrefFrag.java:125-266
EDGES.append(edge(
    'AndroidPreference.onClick',
    'PrefFrag.onPreferenceClick',
    'FRAMEWORK',
    'Android framework calls onPreferenceClick when user taps a preference',
    'SRC PrefFrag.java:125-266: @Override public boolean onPreferenceClick(Preference preference) { ... switch (preference.getKey()) { ... } }'
))

EDGES.append(edge(
    'PrefFrag.onPreferenceClick',
    'PrefFrag.lambda$onPreferenceClick$1',
    'GUI',
    'onPreferenceClick registers lambda for grid columns dialog item selection',
    'SRC PrefFrag.java:135-140: builder.items(sort).itemsCallbackSingleChoice(current, (dialog, view, which, text) -> { ... })'
))

EDGES.append(edge(
    'PrefFrag.onPreferenceClick',
    'PrefFrag.lambda$onPreferenceClick$2',
    'GUI',
    'onPreferenceClick registers lambda for theme dialog item selection',
    'SRC PrefFrag.java:147-152: builder.items(sort).itemsCallbackSingleChoice(current, (dialog, view, which, text) -> { ... })'
))

EDGES.append(edge(
    'PrefFrag.onPreferenceClick',
    'PrefFrag.lambda$onPreferenceClick$3',
    'GUI',
    'onPreferenceClick registers lambda for master password dialog input callback',
    'SRC PrefFrag.java:227: masterPasswordDialogBuilder.input(..., (dialog, input) -> { });'
))

EDGES.append(edge(
    'PrefFrag.onPreferenceClick',
    'PrefFrag.lambda$onPreferenceClick$4',
    'GUI',
    'onPreferenceClick registers lambda as positive button action for master password dialog',
    'SRC PrefFrag.java:233-248: masterPasswordDialogBuilder.onPositive((dialog, which) -> { ... })'
))

EDGES.append(edge(
    'PrefFrag.onPreferenceClick',
    'PrefFrag.lambda$onPreferenceClick$5',
    'GUI',
    'onPreferenceClick registers lambda as negative button action for master password dialog',
    'SRC PrefFrag.java:250: masterPasswordDialogBuilder.onNegative((dialog, which) -> dialog.cancel())'
))

EDGES.append(edge(
    'PrefFrag.onPreferenceClick',
    'PrefFrag.restartPC',
    'CALL',
    'onPreferenceClick calls restartPC to restart activity after theme change',
    'SRC PrefFrag.java:150: restartPC(getActivity());'
))

# PrefFrag lambdas
# lambda$onPreferenceClick$1
# SRC PrefFrag.java:135-140
EDGES.append(edge(
    'PrefFrag.lambda$onPreferenceClick$1',
    'SharedPreferences$Editor.putString',
    'CALL',
    'Lambda saves grid column preference',
    'SRC PrefFrag.java:137: sharedPref.edit().putString(PreferencesConstants.PREFERENCE_GRID_COLUMNS, "" + (which != 0 ? sort[which] : "" + -1)).commit();'
))

# lambda$onPreferenceClick$2
# SRC PrefFrag.java:147-152
EDGES.append(edge(
    'PrefFrag.lambda$onPreferenceClick$2',
    'PrefFrag.restartPC',
    'CALL',
    'Lambda restarts activity after theme selection',
    'SRC PrefFrag.java:150: restartPC(getActivity());'
))

# lambda$onPreferenceClick$3
# Empty lambda body, no edges needed

# lambda$onPreferenceClick$4
# SRC PrefFrag.java:233-248
EDGES.append(edge(
    'PrefFrag.lambda$onPreferenceClick$4',
    'SharedPreferences$Editor.putString',
    'CALL',
    'Lambda saves encrypted master password to SharedPreferences',
    'SRC PrefFrag.java:239-241: sharedPref.edit().putString(PreferencesConstants.PREFERENCE_CRYPT_MASTER_PASSWORD, CryptUtil.encryptPassword(getActivity(), dialog.getInputEditText().getText().toString())).apply();'
))

# lambda$onPreferenceClick$5
# SRC PrefFrag.java:250
# Just calls dialog.cancel(), no additional edges

# PrefFrag.restartPC
# Restarts the activity with fade animation
# SRC PrefFrag.java:255-264
EDGES.append(edge(
    'PrefFrag.restartPC',
    'Activity.finish',
    'CALL',
    'restartPC finishes current activity',
    'SRC PrefFrag.java:260: activity.finish();'
))

EDGES.append(edge(
    'PrefFrag.restartPC',
    'Activity.startActivity',
    'CALL',
    'restartPC starts new instance of activity',
    'SRC PrefFrag.java:262: activity.startActivity(activity.getIntent());'
))

# ===== PrepareCopyTask methods =====

# PrepareCopyTask.onPreExecute
# AsyncTask framework calls before doInBackground
# SRC PrepareCopyTask.java:74-77
EDGES.append(edge(
    'AndroidAsyncTask.execute',
    'PrepareCopyTask.onPreExecute',
    'ASYNC',
    'AsyncTask framework calls onPreExecute on UI thread before background work starts',
    'SRC PrepareCopyTask.java:74-77: @Override protected void onPreExecute() { super.onPreExecute(); dialog = ProgressDialog.show(context, "", context.getString(R.string.processing), true); }'
))

EDGES.append(edge(
    'PrepareCopyTask.onPreExecute',
    'ProgressDialog.show',
    'CALL',
    'onPreExecute shows indeterminate progress dialog',
    'SRC PrepareCopyTask.java:76: dialog = ProgressDialog.show(context, "", context.getString(R.string.processing), true);'
))

# PrepareCopyTask.doInBackground
# AsyncTask framework calls on background thread
# SRC PrepareCopyTask.java:84-117
EDGES.append(edge(
    'AndroidAsyncTask.execute',
    'PrepareCopyTask.doInBackground',
    'ASYNC',
    'AsyncTask framework calls doInBackground on background thread',
    'SRC PrepareCopyTask.java:84-117: @Override protected CopyNode doInBackground(ArrayList<HybridFileParcelable>... params) { ... }'
))

EDGES.append(edge(
    'PrepareCopyTask.doInBackground',
    'PrepareCopyTask$CopyNode.<init>',
    'CALL',
    'doInBackground creates root CopyNode with file list',
    'SRC PrepareCopyTask.java:113: copyFolder = new CopyNode(path, filesToCopy);'
))

EDGES.append(edge(
    'PrepareCopyTask.doInBackground',
    'PrepareCopyTask.checkConflicts',
    'CALL',
    'doInBackground delegates to checkConflicts via CopyNode constructor',
    'SRC PrepareCopyTask.java:113: copyFolder = new CopyNode(path, filesToCopy); CopyNode constructor at 301 calls checkConflicts(filesToCopy, destination)'
))

# PrepareCopyTask.checkConflicts
# SRC PrepareCopyTask.java:119-129
EDGES.append(edge(
    'PrepareCopyTask.checkConflicts',
    'PrepareCopyTask.lambda$checkConflicts$0',
    'CALL',
    'checkConflicts uses lambda to iterate children via forEachChildrenFile',
    'SRC PrepareCopyTask.java:121-127: destination.forEachChildrenFile(context, rootMode, file -> { for (HybridFileParcelable j : filesToCopy) { if (file.getName().equals((j).getName())) { conflictingFiles.add(j); } } });'
))

# PrepareCopyTask.lambda$checkConflicts$0
# SRC PrepareCopyTask.java:121-127
# No outgoing edges - just compares file names and adds to list

# PrepareCopyTask.onPostExecute
# AsyncTask framework calls on UI thread after doInBackground
# SRC PrepareCopyTask.java:131-150
EDGES.append(edge(
    'AndroidAsyncTask.doInBackground',
    'PrepareCopyTask.onPostExecute',
    'ASYNC',
    'AsyncTask framework calls onPostExecute on UI thread with result from doInBackground',
    'SRC PrepareCopyTask.java:131-150: @Override protected void onPostExecute(CopyNode copyFolder) { ... }'
))

EDGES.append(edge(
    'PrepareCopyTask.onPostExecute',
    'PrepareCopyTask.startService',
    'CALL',
    'onPostExecute starts CopyService for special open modes',
    'SRC PrepareCopyTask.java:141: startService(filesToCopy, path, openMode);'
))

EDGES.append(edge(
    'PrepareCopyTask.onPostExecute',
    'PrepareCopyTask.onEndDialog',
    'CALL',
    'onPostExecute delegates to onEndDialog for normal file system copies',
    'SRC PrepareCopyTask.java:145: onEndDialog(null, null, null);'
))

# PrepareCopyTask.startService
# SRC PrepareCopyTask.java:152-161
EDGES.append(edge(
    'PrepareCopyTask.startService',
    'CopyService.<init>',
    'CALL',
    'startService creates Intent for CopyService',
    'SRC PrepareCopyTask.java:153: Intent intent = new Intent(context, CopyService.class);'
))

# PrepareCopyTask.showDialog
# SRC PrepareCopyTask.java:163-221
EDGES.append(edge(
    'PrepareCopyTask.showDialog',
    'PrepareCopyTask.lambda$showDialog$1',
    'GUI',
    'showDialog registers lambda for positive button (skip) action',
    'SRC PrepareCopyTask.java:198-202: dialogBuilder.onPositive((dialog, which) -> { if (checkBox.isChecked()) dialogState = DO_FOR_ALL_ELEMENTS.DO_NOT_REPLACE; doNotReplaceFiles(path, filesToCopy, conflictingFiles); })'
))

EDGES.append(edge(
    'PrepareCopyTask.showDialog',
    'PrepareCopyTask.lambda$showDialog$2',
    'GUI',
    'showDialog registers lambda for negative button (overwrite) action',
    'SRC PrepareCopyTask.java:203-207: dialogBuilder.onNegative((dialog, which) -> { if (checkBox.isChecked()) dialogState = DO_FOR_ALL_ELEMENTS.REPLACE; replaceFiles(path, filesToCopy, conflictingFiles); })'
))

# PrepareCopyTask.lambda$showDialog$1
# SRC PrepareCopyTask.java:198-202
EDGES.append(edge(
    'PrepareCopyTask.lambda$showDialog$1',
    'PrepareCopyTask.doNotReplaceFiles',
    'CALL',
    'Skip button lambda calls doNotReplaceFiles',
    'SRC PrepareCopyTask.java:201: doNotReplaceFiles(path, filesToCopy, conflictingFiles);'
))

# PrepareCopyTask.lambda$showDialog$2
# SRC PrepareCopyTask.java:203-207
EDGES.append(edge(
    'PrepareCopyTask.lambda$showDialog$2',
    'PrepareCopyTask.replaceFiles',
    'CALL',
    'Overwrite button lambda calls replaceFiles',
    'SRC PrepareCopyTask.java:206: replaceFiles(path, filesToCopy, conflictingFiles);'
))

# PrepareCopyTask.onEndDialog
# SRC PrepareCopyTask.java:223-246
EDGES.append(edge(
    'PrepareCopyTask.onEndDialog',
    'PrepareCopyTask.showDialog',
    'CALL',
    'onEndDialog shows conflict resolution dialog when needed',
    'SRC PrepareCopyTask.java:226: showDialog(path, filesToCopy, conflictingFiles);'
))

EDGES.append(edge(
    'PrepareCopyTask.onEndDialog',
    'PrepareCopyTask.doNotReplaceFiles',
    'CALL',
    'onEndDialog skips files when DO_NOT_REPLACE state is set',
    'SRC PrepareCopyTask.java:228: doNotReplaceFiles(path, filesToCopy, conflictingFiles);'
))

EDGES.append(edge(
    'PrepareCopyTask.onEndDialog',
    'PrepareCopyTask.replaceFiles',
    'CALL',
    'onEndDialog replaces files when REPLACE state is set',
    'SRC PrepareCopyTask.java:230: replaceFiles(path, filesToCopy, conflictingFiles);'
))

EDGES.append(edge(
    'PrepareCopyTask.onEndDialog',
    'PrepareCopyTask$CopyNode.startCopy',
    'CALL',
    'onEndDialog starts BFS traversal of copy node tree',
    'SRC PrepareCopyTask.java:232: CopyNode c = !copyFolder.hasStarted()? copyFolder.startCopy():copyFolder.goToNextNode();'
))

EDGES.append(edge(
    'PrepareCopyTask.onEndDialog',
    'PrepareCopyTask$CopyNode.goToNextNode',
    'CALL',
    'onEndDialog advances to next node in BFS traversal',
    'SRC PrepareCopyTask.java:232: CopyNode c = !copyFolder.hasStarted()? copyFolder.startCopy():copyFolder.goToNextNode();'
))

# PrepareCopyTask.doNotReplaceFiles
# SRC PrepareCopyTask.java:248-261
EDGES.append(edge(
    'PrepareCopyTask.doNotReplaceFiles',
    'PrepareCopyTask.onEndDialog',
    'CALL',
    'doNotReplaceFiles recurses to onEndDialog to process next files',
    'SRC PrepareCopyTask.java:260: onEndDialog(path, filesToCopy, conflictingFiles);'
))

# PrepareCopyTask.replaceFiles
# SRC PrepareCopyTask.java:263-274
EDGES.append(edge(
    'PrepareCopyTask.replaceFiles',
    'PrepareCopyTask.onEndDialog',
    'CALL',
    'replaceFiles recurses to onEndDialog to process next files',
    'SRC PrepareCopyTask.java:273: onEndDialog(path, filesToCopy, conflictingFiles);'
))

# PrepareCopyTask$CopyNode methods
# CopyNode.<init>
# SRC PrepareCopyTask.java:297-319
EDGES.append(edge(
    'PrepareCopyTask$CopyNode.<init>',
    'PrepareCopyTask.checkConflicts',
    'CALL',
    'CopyNode constructor calls checkConflicts to find name collisions',
    'SRC PrepareCopyTask.java:301: conflictingFiles = checkConflicts(filesToCopy, destination);'
))

EDGES.append(edge(
    'PrepareCopyTask$CopyNode.<init>',
    'PrepareCopyTask$CopyNode.<init>',
    'CALL',
    'CopyNode constructor recursively creates child nodes for conflicting directories',
    'SRC PrepareCopyTask.java:309-312: nextNodes.add(new CopyNode(path + "/" + conflictingFiles.get(i).getName(), conflictingFiles.get(i).listFiles(context, rootMode)));'
))

# CopyNode.startCopy
# SRC PrepareCopyTask.java:326-331
EDGES.append(edge(
    'PrepareCopyTask$CopyNode.startCopy',
    'PrepareCopyTask$CopyNode.<init>',
    'IMPLICIT',
    'startCopy initializes BFS queue and visited set',
    'SRC PrepareCopyTask.java:327-330: queue = new LinkedList<>(); visited = new HashSet<>(); queue.add(this); visited.add(this); (implicit reference to this node)'
))

# CopyNode.goToNextNode
# SRC PrepareCopyTask.java:337-350
EDGES.append(edge(
    'PrepareCopyTask$CopyNode.goToNextNode',
    'PrepareCopyTask$CopyNode.getUnvisitedChildNode',
    'CALL',
    'goToNextNode gets next unvisited child for BFS traversal',
    'SRC PrepareCopyTask.java:342: CopyNode child; if ((child = getUnvisitedChildNode(visited, node)) != null) { ... }'
))

EDGES.append(edge(
    'PrepareCopyTask$CopyNode.goToNextNode',
    'PrepareCopyTask$CopyNode.goToNextNode',
    'CALL',
    'goToNextNode recursively processes queue until finding next node',
    'SRC PrepareCopyTask.java:348: return goToNextNode();'
))

# CopyNode.hasStarted
# SRC PrepareCopyTask.java:352-354
# Simple getter, no edges

# CopyNode.getPath
# SRC PrepareCopyTask.java:356-358
# Simple getter, no edges

# CopyNode.getFilesToCopy
# SRC PrepareCopyTask.java:360-362
# Simple getter, no edges

# CopyNode.getConflictingFiles
# SRC PrepareCopyTask.java:364-366
# Simple getter, no edges

# CopyNode.getUnvisitedChildNode
# SRC PrepareCopyTask.java:368-376
# Simple iteration, no method calls

# ===== ProcessViewerFragment methods =====

# ProcessViewerFragment$CustomServiceConnection.onServiceConnected
# ServiceConnection callback when service binds
# SRC ProcessViewerFragment.java:315-333
EDGES.append(edge(
    'AndroidServiceConnection.onServiceConnected',
    'ProcessViewerFragment$CustomServiceConnection.onServiceConnected',
    'FRAMEWORK',
    'Android framework calls onServiceConnected when service binding completes',
    'SRC ProcessViewerFragment.java:315-333: @Override public void onServiceConnected(ComponentName name, IBinder service) { ... }'
))

EDGES.append(edge(
    'ProcessViewerFragment$CustomServiceConnection.onServiceConnected',
    'ProcessViewerFragment.processResults',
    'CALL',
    'onServiceConnected calls processResults for each existing data package',
    'SRC ProcessViewerFragment.java:321: fragment.processResults(dataPackage, serviceType);'
))

EDGES.append(edge(
    'ProcessViewerFragment$CustomServiceConnection.onServiceConnected',
    'ProcessViewerFragment$CustomServiceConnection$1.<init>',
    'CALL',
    'onServiceConnected creates anonymous ProgressListener implementation',
    'SRC ProcessViewerFragment.java:326-337: specificService.setProgressListener(new AbstractProgressiveService.ProgressListener() { ... });'
))

# ProcessViewerFragment$CustomServiceConnection.onServiceDisconnected
# ServiceConnection callback when service disconnects
# SRC ProcessViewerFragment.java:339-340
# Empty implementation, no edges

# ProcessViewerFragment$CustomServiceConnection$1.<init>
# Anonymous ProgressListener implementation
# Constructor chains to Object
EDGES.append(edge(
    'ProcessViewerFragment$CustomServiceConnection$1.<init>',
    'Object.<init>',
    'CALL',
    'Anonymous ProgressListener constructor chains to Object',
    'SRC ProcessViewerFragment.java:326: new AbstractProgressiveService.ProgressListener() (implicit super() call)'
))

# All edges collected. No UNREACHABLE methods in this batch - all are reachable.
