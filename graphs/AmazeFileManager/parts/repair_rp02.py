# Repair batch 02: SftpConnectDialog methods
# Generated for AmazeFileManager graph repair

# onCreate - already has edges in graph_def.py, REACHABLE via LIFECYCLE
# Lines 93-98: DialogFragment.onCreate called by framework
# The framework calls onCreate when the fragment is created

# onCreateDialog - already has one edge in graph_def.py, adding more edges
# Lines 101-294: DialogFragment.onCreateDialog called by framework
# This method sets up the dialog and registers several lambdas

e('SftpConnectDialog.onCreateDialog', 'SftpConnectDialog.lambda$onCreateDialog$9', 'GUI',
  'portET.setOnFocusChangeListener registers lambda$onCreateDialog$9',
  evidence='SRC SftpConnectDialog.java:131 portET.setOnFocusChangeListener((v, hasFocus) -> {...')

e('SftpConnectDialog.onCreateDialog', 'SftpConnectDialog.lambda$onCreateDialog$1', 'GUI',
  'selectPemBTN.setOnClickListener registers lambda$onCreateDialog$1',
  evidence='SRC SftpConnectDialog.java:139 selectPemBTN.setOnClickListener(v -> {...')

e('SftpConnectDialog.onCreateDialog', 'SftpConnectDialog.lambda$onCreateDialog$0', 'GUI',
  'dialogBuilder.onPositive registers lambda$onCreateDialog$0 for positive button',
  evidence='SRC SftpConnectDialog.java:157 dialogBuilder.onPositive((dialog, which) -> {...')

e('SftpConnectDialog.onCreateDialog', 'SftpConnectDialog.lambda$onCreateDialog$13', 'GUI',
  'dialogBuilder.onNegative registers lambda$onCreateDialog$13 for negative button',
  evidence='SRC SftpConnectDialog.java:232 }).onNegative((dialog, which) -> dialog.dismiss());')

e('SftpConnectDialog.onCreateDialog', 'SftpConnectDialog.lambda$onCreateDialog$12', 'GUI',
  'edit mode: dialogBuilder.negativeText onNegative registers lambda$onCreateDialog$12',
  evidence='SRC SftpConnectDialog.java:236 if(edit) { dialogBuilder.negativeText(R.string.delete).onNegative((dialog, which) -> {...')

e('SftpConnectDialog.onCreateDialog', 'SftpConnectDialog.lambda$onCreateDialog$10', 'GUI',
  'edit mode: dialogBuilder.onNeutral registers lambda$onCreateDialog$10',
  evidence='SRC SftpConnectDialog.java:253 }).neutralText(R.string.cancel).onNeutral((dialog, which) -> dialog.dismiss());')

e('SftpConnectDialog.onCreateDialog', 'MaterialDialog.Builder.<init>', 'CALL',
  'onCreateDialog instantiates MaterialDialog.Builder',
  evidence='SRC SftpConnectDialog.java:148 final MaterialDialog.Builder dialogBuilder = new MaterialDialog.Builder(context);')

e('SftpConnectDialog.onCreateDialog', 'MaterialDialog.Builder.build', 'CALL',
  'onCreateDialog builds MaterialDialog',
  evidence='SRC SftpConnectDialog.java:255 MaterialDialog dialog = dialogBuilder.build();')

e('SftpConnectDialog.onCreateDialog', 'SimpleTextWatcher.<init>', 'CALL',
  'onCreateDialog creates SimpleTextWatcher anonymous subclass for validator',
  evidence='SRC SftpConnectDialog.java:264 TextWatcher validator = new SimpleTextWatcher() {...')

# lambda$onCreateDialog$9 - focus change listener for port EditText
# Lines 131-134
e('SftpConnectDialog.lambda$onCreateDialog$9', 'EditText.selectAll', 'CALL',
  'lambda calls selectAll when port field gains focus',
  evidence='SRC SftpConnectDialog.java:131-133 portET.setOnFocusChangeListener((v, hasFocus) -> { if(hasFocus) portET.selectAll(); });')

# lambda$onCreateDialog$1 - click listener for select PEM button
# Lines 139-144
e('SftpConnectDialog.lambda$onCreateDialog$1', 'Intent.<init>', 'CALL',
  'lambda creates Intent for file selection',
  evidence='SRC SftpConnectDialog.java:140 Intent intent = new Intent()')

e('SftpConnectDialog.lambda$onCreateDialog$1', 'SftpConnectDialog.startActivityForResult', 'CALL',
  'lambda calls startActivityForResult to launch file picker',
  evidence='SRC SftpConnectDialog.java:144 startActivityForResult(intent, SELECT_PEM_INTENT);')

# lambda$onCreateDialog$0 - main positive button handler
# Lines 157-231
e('SftpConnectDialog.lambda$onCreateDialog$0', 'EditText.getText', 'CALL',
  'lambda reads text from edit fields',
  evidence='SRC SftpConnectDialog.java:159-163 final String connectionName = connectionET.getText().toString();')

e('SftpConnectDialog.lambda$onCreateDialog$0', 'UtilsHandler.getSshHostKey', 'CALL',
  'lambda retrieves existing SSH host key',
  evidence='SRC SftpConnectDialog.java:169 String sshHostKey = utilsHandler.getSshHostKey(deriveSftpPathFrom(...));')

e('SftpConnectDialog.lambda$onCreateDialog$0', 'SshConnectionPool.getInstance', 'CALL',
  'lambda gets SshConnectionPool singleton',
  evidence='SRC SftpConnectDialog.java:176 SshConnectionPool.getInstance().removeConnection(...);')

e('SftpConnectDialog.lambda$onCreateDialog$0', 'SshConnectionPool.removeConnection', 'CALL',
  'lambda removes existing connection before reconnecting',
  evidence='SRC SftpConnectDialog.java:176-177 SshConnectionPool.getInstance().removeConnection(SshClientUtils.deriveSftpPathFrom(...), () -> {...')

e('SftpConnectDialog.lambda$onCreateDialog$0', 'SftpConnectDialog.lambda$null$2', 'ASYNC',
  'removeConnection callback registers lambda$null$2',
  evidence='SRC SftpConnectDialog.java:177 removeConnection(..., () -> {...')

e('SftpConnectDialog.lambda$onCreateDialog$0', 'GetSshHostFingerprintTask.<init>', 'CALL',
  'lambda creates GetSshHostFingerprintTask for new connection (no existing key)',
  evidence='SRC SftpConnectDialog.java:203 new GetSshHostFingerprintTask(hostname, port, taskResult -> {...')

e('SftpConnectDialog.lambda$onCreateDialog$0', 'GetSshHostFingerprintTask.execute', 'CALL',
  'lambda executes GetSshHostFingerprintTask',
  evidence='SRC SftpConnectDialog.java:230 }).execute();')

e('SftpConnectDialog.lambda$onCreateDialog$0', 'SftpConnectDialog.lambda$null$6', 'ASYNC',
  'GetSshHostFingerprintTask callback registers lambda$null$6',
  evidence='SRC SftpConnectDialog.java:203 new GetSshHostFingerprintTask(hostname, port, taskResult -> {...')

e('SftpConnectDialog.lambda$onCreateDialog$0', 'AlertDialog.Builder.<init>', 'CALL',
  'lambda creates AlertDialog.Builder for host key verification',
  evidence='SRC SftpConnectDialog.java:213 new AlertDialog.Builder(context).setTitle(...)')

# lambda$null$2 - callback from removeConnection
# Lines 177-199
e('SftpConnectDialog.lambda$null$2', 'GetSshHostFingerprintTask.<init>', 'CALL',
  'lambda creates GetSshHostFingerprintTask after connection removed',
  evidence='SRC SftpConnectDialog.java:178 new GetSshHostFingerprintTask(hostname, port, taskResult -> {...')

e('SftpConnectDialog.lambda$null$2', 'GetSshHostFingerprintTask.execute', 'CALL',
  'lambda executes GetSshHostFingerprintTask',
  evidence='SRC SftpConnectDialog.java:198 }).execute();')

e('SftpConnectDialog.lambda$null$2', 'SftpConnectDialog.lambda$null$3', 'ASYNC',
  'GetSshHostFingerprintTask callback registers lambda$null$3',
  evidence='SRC SftpConnectDialog.java:178 new GetSshHostFingerprintTask(hostname, port, taskResult -> {...')

# lambda$null$3 - callback from GetSshHostFingerprintTask (edit mode with existing key)
# Lines 178-198
e('SftpConnectDialog.lambda$null$3', 'SecurityUtils.getFingerprint', 'CALL',
  'lambda gets host key fingerprint',
  evidence='SRC SftpConnectDialog.java:181 final String hostKeyFingerprint = SecurityUtils.getFingerprint(hostKey);')

e('SftpConnectDialog.lambda$null$3', 'SftpConnectDialog.authenticateAndSaveSetup', 'CALL',
  'lambda calls authenticateAndSaveSetup when key matches',
  evidence='SRC SftpConnectDialog.java:183-185 authenticateAndSaveSetup(connectionName, hostname, port, sshHostKey, username, password, selectedParsedKeyPairName, selectedParsedKeyPair, edit);')

e('SftpConnectDialog.lambda$null$3', 'AlertDialog.Builder.<init>', 'CALL',
  'lambda creates AlertDialog.Builder when host key changed',
  evidence='SRC SftpConnectDialog.java:187 new AlertDialog.Builder(context).setTitle(...)')

e('SftpConnectDialog.lambda$null$3', 'SftpConnectDialog.lambda$null$4', 'GUI',
  'setPositiveButton registers lambda$null$4',
  evidence='SRC SftpConnectDialog.java:191 .setPositiveButton(R.string.update_host_key, (dialog1, which1) -> {...')

e('SftpConnectDialog.lambda$null$3', 'SftpConnectDialog.lambda$null$5', 'GUI',
  'setNegativeButton registers lambda$null$5',
  evidence='SRC SftpConnectDialog.java:196 .setNegativeButton(R.string.cancel_recommended, (dialog1, which1) -> dialog1.dismiss())')

e('SftpConnectDialog.lambda$null$3', 'AlertDialog.Builder.show', 'CALL',
  'lambda shows the alert dialog',
  evidence='SRC SftpConnectDialog.java:197 .show();')

# lambda$null$4 - positive button in host key changed dialog
# Lines 191-195
e('SftpConnectDialog.lambda$null$4', 'SftpConnectDialog.authenticateAndSaveSetup', 'CALL',
  'lambda calls authenticateAndSaveSetup with new host key',
  evidence='SRC SftpConnectDialog.java:192-194 authenticateAndSaveSetup(connectionName, hostname, port, hostKeyFingerprint, username, password, selectedParsedKeyPairName, selectedParsedKeyPair, edit);')

# lambda$null$5 - negative button in host key changed dialog
# Lines 196
e('SftpConnectDialog.lambda$null$5', 'AlertDialog.dismiss', 'CALL',
  'lambda dismisses the alert dialog',
  evidence='SRC SftpConnectDialog.java:196 .setNegativeButton(R.string.cancel_recommended, (dialog1, which1) -> dialog1.dismiss())')

# lambda$null$6 - callback from GetSshHostFingerprintTask (new connection)
# Lines 203-230
e('SftpConnectDialog.lambda$null$6', 'SecurityUtils.getFingerprint', 'CALL',
  'lambda gets host key fingerprint',
  evidence='SRC SftpConnectDialog.java:206 final String hostKeyFingerprint = SecurityUtils.getFingerprint(hostKey);')

e('SftpConnectDialog.lambda$null$6', 'StringBuilder.<init>', 'CALL',
  'lambda creates StringBuilder for host:port display',
  evidence='SRC SftpConnectDialog.java:207 StringBuilder sb = new StringBuilder(hostname);')

e('SftpConnectDialog.lambda$null$6', 'AlertDialog.Builder.<init>', 'CALL',
  'lambda creates AlertDialog.Builder for verification',
  evidence='SRC SftpConnectDialog.java:213 new AlertDialog.Builder(context).setTitle(...)')

e('SftpConnectDialog.lambda$null$6', 'SftpConnectDialog.lambda$null$7', 'GUI',
  'setPositiveButton registers lambda$null$7',
  evidence='SRC SftpConnectDialog.java:217 .setPositiveButton(R.string.yes, (dialog1, which1) -> {...')

e('SftpConnectDialog.lambda$null$6', 'SftpConnectDialog.lambda$null$8', 'GUI',
  'setNegativeButton registers lambda$null$8',
  evidence='SRC SftpConnectDialog.java:229 .setNegativeButton(R.string.no, (dialog1, which1) -> dialog1.dismiss()).show();')

e('SftpConnectDialog.lambda$null$6', 'AlertDialog.Builder.show', 'CALL',
  'lambda shows the verification dialog',
  evidence='SRC SftpConnectDialog.java:229 .show();')

# lambda$null$7 - positive button in host key verification dialog
# Lines 217-228
e('SftpConnectDialog.lambda$null$7', 'AlertDialog.dismiss', 'CALL',
  'lambda dismisses verification dialog',
  evidence='SRC SftpConnectDialog.java:219 dialog1.dismiss();')

e('SftpConnectDialog.lambda$null$7', 'SftpConnectDialog.authenticateAndSaveSetup', 'CALL',
  'lambda calls authenticateAndSaveSetup after user accepts key',
  evidence='SRC SftpConnectDialog.java:220-222 authenticateAndSaveSetup(connectionName, hostname, port, hostKeyFingerprint, username, password, selectedParsedKeyPairName, selectedParsedKeyPair, edit)')

e('SftpConnectDialog.lambda$null$7', 'Log.d', 'CALL',
  'lambda logs successful setup',
  evidence='SRC SftpConnectDialog.java:224 Log.d(TAG, "Saved setup");')

e('SftpConnectDialog.lambda$null$7', 'SftpConnectDialog.dismiss', 'CALL',
  'lambda dismisses the SftpConnectDialog',
  evidence='SRC SftpConnectDialog.java:225 dismiss();')

# lambda$null$8 - negative button in host key verification dialog
# Lines 229
e('SftpConnectDialog.lambda$null$8', 'AlertDialog.dismiss', 'CALL',
  'lambda dismisses verification dialog when user declines',
  evidence='SRC SftpConnectDialog.java:229 .setNegativeButton(R.string.no, (dialog1, which1) -> dialog1.dismiss())')

# lambda$onCreateDialog$13 - negative button handler (non-edit mode)
# Line 232
e('SftpConnectDialog.lambda$onCreateDialog$13', 'MaterialDialog.dismiss', 'CALL',
  'lambda dismisses the dialog',
  evidence='SRC SftpConnectDialog.java:232 }).onNegative((dialog, which) -> dialog.dismiss());')

# lambda$onCreateDialog$12 - negative button handler (edit mode - delete)
# Lines 236-252
e('SftpConnectDialog.lambda$onCreateDialog$12', 'EditText.getText', 'CALL',
  'lambda reads connection parameters',
  evidence='SRC SftpConnectDialog.java:237-240 final String connectionName = connectionET.getText().toString();')

e('SftpConnectDialog.lambda$onCreateDialog$12', 'DataUtils.getInstance', 'CALL',
  'lambda gets DataUtils singleton',
  evidence='SRC SftpConnectDialog.java:243 int i = DataUtils.getInstance().containsServer(...);')

e('SftpConnectDialog.lambda$onCreateDialog$12', 'DataUtils.containsServer', 'CALL',
  'lambda checks if server exists',
  evidence='SRC SftpConnectDialog.java:243 int i = DataUtils.getInstance().containsServer(new String[]{connectionName, path});')

e('SftpConnectDialog.lambda$onCreateDialog$12', 'DataUtils.removeServer', 'CALL',
  'lambda removes server from DataUtils',
  evidence='SRC SftpConnectDialog.java:246 DataUtils.getInstance().removeServer(i);')

e('SftpConnectDialog.lambda$onCreateDialog$12', 'AppConfig.runInBackground', 'CALL',
  'lambda runs database removal in background',
  evidence='SRC SftpConnectDialog.java:247 AppConfig.runInBackground(() -> {...')

e('SftpConnectDialog.lambda$onCreateDialog$12', 'SftpConnectDialog.lambda$null$11', 'ASYNC',
  'runInBackground callback registers lambda$null$11',
  evidence='SRC SftpConnectDialog.java:247-249 AppConfig.runInBackground(() -> { utilsHandler.removeFromDatabase(...); });')

e('SftpConnectDialog.lambda$onCreateDialog$12', 'MainActivity.getDrawer', 'CALL',
  'lambda gets drawer to refresh it',
  evidence='SRC SftpConnectDialog.java:251 ((MainActivity) getActivity()).getDrawer().refreshDrawer();')

e('SftpConnectDialog.lambda$onCreateDialog$12', 'MaterialDialog.dismiss', 'CALL',
  'lambda dismisses the dialog',
  evidence='SRC SftpConnectDialog.java:252 dialog.dismiss();')

# lambda$null$11 - background task for database removal
# Lines 247-249
e('SftpConnectDialog.lambda$null$11', 'UtilsHandler.removeFromDatabase', 'CALL',
  'lambda removes SFTP connection from database',
  evidence='SRC SftpConnectDialog.java:248-249 utilsHandler.removeFromDatabase(new OperationData(UtilsHandler.Operation.SFTP, path, connectionName, null, null, null));')

e('SftpConnectDialog.lambda$null$11', 'OperationData.<init>', 'CALL',
  'lambda creates OperationData for removal',
  evidence='SRC SftpConnectDialog.java:248 new OperationData(UtilsHandler.Operation.SFTP, path, connectionName, null, null, null)')

# lambda$onCreateDialog$10 - neutral button handler (edit mode - cancel)
# Line 253
e('SftpConnectDialog.lambda$onCreateDialog$10', 'MaterialDialog.dismiss', 'CALL',
  'lambda dismisses the dialog',
  evidence='SRC SftpConnectDialog.java:253 }).neutralText(R.string.cancel).onNeutral((dialog, which) -> dialog.dismiss());')

# onActivityResult - LIFECYCLE method
# Lines 298-327
e('SftpConnectDialog.onActivityResult', 'Intent.getData', 'CALL',
  'onActivityResult gets selected file URI',
  evidence='SRC SftpConnectDialog.java:306 selectedPem = data.getData();')

e('SftpConnectDialog.onActivityResult', 'ContentResolver.openInputStream', 'CALL',
  'onActivityResult opens input stream for PEM file',
  evidence='SRC SftpConnectDialog.java:309 InputStream selectedKeyContent = context.getContentResolver().openInputStream(selectedPem);')

e('SftpConnectDialog.onActivityResult', 'PemToKeyPairTask.<init>', 'CALL',
  'onActivityResult creates PemToKeyPairTask',
  evidence='SRC SftpConnectDialog.java:311 new PemToKeyPairTask(selectedKeyContent, result -> {...')

e('SftpConnectDialog.onActivityResult', 'PemToKeyPairTask.execute', 'CALL',
  'onActivityResult executes PemToKeyPairTask',
  evidence='SRC SftpConnectDialog.java:321 }).execute();')

e('SftpConnectDialog.onActivityResult', 'SftpConnectDialog.lambda$onActivityResult$14', 'ASYNC',
  'PemToKeyPairTask callback registers lambda$onActivityResult$14',
  evidence='SRC SftpConnectDialog.java:311 new PemToKeyPairTask(selectedKeyContent, result -> {...')

e('SftpConnectDialog.onActivityResult', 'Log.e', 'CALL',
  'onActivityResult logs FileNotFoundException',
  evidence='SRC SftpConnectDialog.java:323 Log.e(TAG, "File not found", e);')

# lambda$onActivityResult$14 - callback from PemToKeyPairTask
# Lines 311-321
e('SftpConnectDialog.lambda$onActivityResult$14', 'Uri.getLastPathSegment', 'CALL',
  'lambda gets filename from URI',
  evidence='SRC SftpConnectDialog.java:313 selectedParsedKeyPairName = selectedPem.getLastPathSegment().substring(...);')

e('SftpConnectDialog.lambda$onActivityResult$14', 'SftpConnectDialog.getDialog', 'CALL',
  'lambda gets the MaterialDialog',
  evidence='SRC SftpConnectDialog.java:314 MDButton okBTN = ((MaterialDialog)getDialog()).getActionButton(DialogAction.POSITIVE);')

e('SftpConnectDialog.lambda$onActivityResult$14', 'MaterialDialog.getActionButton', 'CALL',
  'lambda gets positive button',
  evidence='SRC SftpConnectDialog.java:315 .getActionButton(DialogAction.POSITIVE);')

e('SftpConnectDialog.lambda$onActivityResult$14', 'MDButton.setEnabled', 'CALL',
  'lambda enables positive button',
  evidence='SRC SftpConnectDialog.java:316 okBTN.setEnabled(okBTN.isEnabled() || true);')

e('SftpConnectDialog.lambda$onActivityResult$14', 'Dialog.findViewById', 'CALL',
  'lambda finds select PEM button',
  evidence='SRC SftpConnectDialog.java:318 Button selectPemBTN = getDialog().findViewById(R.id.selectPemBTN);')

e('SftpConnectDialog.lambda$onActivityResult$14', 'Button.setText', 'CALL',
  'lambda sets button text to filename',
  evidence='SRC SftpConnectDialog.java:319 selectPemBTN.setText(selectedParsedKeyPairName);')

# authenticateAndSaveSetup - called from multiple lambdas
# Lines 327-394
e('SftpConnectDialog.authenticateAndSaveSetup', 'SshClientUtils.encryptSshPathAsNecessary', 'CALL',
  'authenticateAndSaveSetup encrypts path',
  evidence='SRC SftpConnectDialog.java:336 final String encryptedPath = SshClientUtils.encryptSshPathAsNecessary(path);')

e('SftpConnectDialog.authenticateAndSaveSetup', 'SshConnectionPool.getInstance', 'CALL',
  'authenticateAndSaveSetup gets connection pool',
  evidence='SRC SftpConnectDialog.java:340 SSHClient result = SshConnectionPool.getInstance().getConnection(...);')

e('SftpConnectDialog.authenticateAndSaveSetup', 'SshConnectionPool.getConnection', 'CALL',
  'authenticateAndSaveSetup establishes SSH connection',
  evidence='SRC SftpConnectDialog.java:340-341 SshConnectionPool.getInstance().getConnection(hostname, port, hostKeyFingerprint, username, password, selectedParsedKeyPair);')

e('SftpConnectDialog.authenticateAndSaveSetup', 'DataUtils.getInstance', 'CALL',
  'authenticateAndSaveSetup gets DataUtils singleton',
  evidence='SRC SftpConnectDialog.java:344 if(DataUtils.getInstance().containsServer(path) == -1) {...')

e('SftpConnectDialog.authenticateAndSaveSetup', 'DataUtils.containsServer', 'CALL',
  'authenticateAndSaveSetup checks if server already exists',
  evidence='SRC SftpConnectDialog.java:344 if(DataUtils.getInstance().containsServer(path) == -1) {')

e('SftpConnectDialog.authenticateAndSaveSetup', 'DataUtils.addServer', 'CALL',
  'authenticateAndSaveSetup adds server for new connection',
  evidence='SRC SftpConnectDialog.java:345 DataUtils.getInstance().addServer(new String[]{connectionName, path});')

e('SftpConnectDialog.authenticateAndSaveSetup', 'MainActivity.getDrawer', 'CALL',
  'authenticateAndSaveSetup gets drawer',
  evidence='SRC SftpConnectDialog.java:346 ((MainActivity) getActivity()).getDrawer().refreshDrawer();')

e('SftpConnectDialog.authenticateAndSaveSetup', 'UtilsHandler.saveToDatabase', 'CALL',
  'authenticateAndSaveSetup saves connection to database',
  evidence='SRC SftpConnectDialog.java:348 utilsHandler.saveToDatabase(new OperationData(...));')

e('SftpConnectDialog.authenticateAndSaveSetup', 'OperationData.<init>', 'CALL',
  'authenticateAndSaveSetup creates OperationData',
  evidence='SRC SftpConnectDialog.java:348-350 new OperationData(UtilsHandler.Operation.SFTP, encryptedPath, connectionName, hostKeyFingerprint, selectedParsedKeyPairName, getPemContents())')

e('SftpConnectDialog.authenticateAndSaveSetup', 'SftpConnectDialog.getPemContents', 'CALL',
  'authenticateAndSaveSetup calls getPemContents for database',
  evidence='SRC SftpConnectDialog.java:350 getPemContents())')

e('SftpConnectDialog.authenticateAndSaveSetup', 'MainActivity.getCurrentMainFragment', 'CALL',
  'authenticateAndSaveSetup gets main fragment',
  evidence='SRC SftpConnectDialog.java:352 MainFragment ma = ((MainActivity)getActivity()).getCurrentMainFragment();')

e('SftpConnectDialog.authenticateAndSaveSetup', 'MainFragment.loadlist', 'CALL',
  'authenticateAndSaveSetup loads SFTP directory in fragment',
  evidence='SRC SftpConnectDialog.java:353 ma.loadlist(path, false, OpenMode.SFTP);')

e('SftpConnectDialog.authenticateAndSaveSetup', 'SftpConnectDialog.dismiss', 'CALL',
  'authenticateAndSaveSetup dismisses dialog on success',
  evidence='SRC SftpConnectDialog.java:354 dismiss();')

e('SftpConnectDialog.authenticateAndSaveSetup', 'Snackbar.make', 'CALL',
  'authenticateAndSaveSetup shows snackbar if connection exists',
  evidence='SRC SftpConnectDialog.java:357 Snackbar.make(getActivity().findViewById(R.id.content_frame), getString(R.string.connection_exists), Snackbar.LENGTH_SHORT).show();')

e('SftpConnectDialog.authenticateAndSaveSetup', 'DataUtils.removeServer', 'CALL',
  'authenticateAndSaveSetup removes old server in edit mode',
  evidence='SRC SftpConnectDialog.java:379 DataUtils.getInstance().removeServer(DataUtils.getInstance().containsServer(originalPath));')

e('SftpConnectDialog.authenticateAndSaveSetup', 'Collections.sort', 'CALL',
  'authenticateAndSaveSetup sorts server list',
  evidence='SRC SftpConnectDialog.java:381 Collections.sort(DataUtils.getInstance().getServers(), new BookSorter());')

e('SftpConnectDialog.authenticateAndSaveSetup', 'BookSorter.<init>', 'CALL',
  'authenticateAndSaveSetup creates BookSorter comparator',
  evidence='SRC SftpConnectDialog.java:381 new BookSorter()')

e('SftpConnectDialog.authenticateAndSaveSetup', 'AppConfig.runInBackground', 'CALL',
  'authenticateAndSaveSetup runs database update in background for edit mode',
  evidence='SRC SftpConnectDialog.java:384 AppConfig.runInBackground(() -> {...')

e('SftpConnectDialog.authenticateAndSaveSetup', 'SftpConnectDialog.lambda$authenticateAndSaveSetup$15', 'ASYNC',
  'runInBackground callback registers lambda$authenticateAndSaveSetup$15',
  evidence='SRC SftpConnectDialog.java:385-389 utilsHandler.updateSsh(...);')

# lambda$authenticateAndSaveSetup$15 - background task for database update
# Lines 385-389
e('SftpConnectDialog.lambda$authenticateAndSaveSetup$15', 'UtilsHandler.updateSsh', 'CALL',
  'lambda updates SSH connection in database',
  evidence='SRC SftpConnectDialog.java:385-388 utilsHandler.updateSsh(connectionName, getArguments().getString("name"), encryptedPath, hostKeyFingerprint, selectedParsedKeyPairName, getPemContents());')

e('SftpConnectDialog.lambda$authenticateAndSaveSetup$15', 'SftpConnectDialog.getPemContents', 'CALL',
  'lambda calls getPemContents for database update',
  evidence='SRC SftpConnectDialog.java:388 getPemContents());')

# getPemContents - reads PEM file content
# Lines 397-413
e('SftpConnectDialog.getPemContents', 'BufferedReader.<init>', 'CALL',
  'getPemContents creates BufferedReader',
  evidence='SRC SftpConnectDialog.java:402 BufferedReader reader = new BufferedReader(new InputStreamReader(context.getContentResolver().openInputStream(selectedPem)));')

e('SftpConnectDialog.getPemContents', 'InputStreamReader.<init>', 'CALL',
  'getPemContents creates InputStreamReader',
  evidence='SRC SftpConnectDialog.java:402 new InputStreamReader(context.getContentResolver().openInputStream(selectedPem))')

e('SftpConnectDialog.getPemContents', 'ContentResolver.openInputStream', 'CALL',
  'getPemContents opens PEM file stream',
  evidence='SRC SftpConnectDialog.java:402 context.getContentResolver().openInputStream(selectedPem)')

e('SftpConnectDialog.getPemContents', 'StringBuilder.<init>', 'CALL',
  'getPemContents creates StringBuilder',
  evidence='SRC SftpConnectDialog.java:403 StringBuilder sb = new StringBuilder();')

e('SftpConnectDialog.getPemContents', 'BufferedReader.readLine', 'CALL',
  'getPemContents reads lines from file',
  evidence='SRC SftpConnectDialog.java:404 for (String line = reader.readLine(); line != null; line = reader.readLine()) {')
