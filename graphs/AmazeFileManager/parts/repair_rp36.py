# Repair batch 36: Missing routes for SftpConnectDialog lifecycle methods
# All other methods in this batch already have routes in graph_def.py

# SftpConnectDialog lifecycle: framework calls onCreate -> onCreateDialog
e('SftpConnectDialog.<init>', 'SftpConnectDialog.onCreate', 'FRAMEWORK',
  'DialogFragment framework calls onCreate after construction',
  evidence='SRC SftpConnectDialog.java:92-98 extends DialogFragment at line 75')

e('SftpConnectDialog.onCreate', 'SftpConnectDialog.onCreateDialog', 'FRAMEWORK',
  'DialogFragment framework calls onCreateDialog to build the dialog',
  evidence='SRC SftpConnectDialog.java:101-321 DialogFragment lifecycle')

# onActivityResult called by framework after startActivityForResult
e('SftpConnectDialog.lambda$onCreateDialog$1', 'SftpConnectDialog.onActivityResult', 'RESULT',
  'Framework delivers result from file picker intent started at line 147',
  evidence='SRC SftpConnectDialog.java:147 startActivityForResult(intent, SELECT_PEM_INTENT); SftpConnectDialog.java:325-360 onActivityResult checks requestCode==SELECT_PEM_INTENT')

# Two INCOMPLETE methods that don't exist in source
# SftpConnectDialog.lambda$authenticateAndSaveSetup$15 - authenticateAndSaveSetup has no lambdas in source
# SearchAsyncTask.lambda$search$1 - only one lambda in search method
