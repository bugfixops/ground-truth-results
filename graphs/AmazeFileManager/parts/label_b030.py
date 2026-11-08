# ---- Helper batch_030 label part (2024)
# FtpServerFragment and FtpServerFragment$1

# FtpServerFragment.<init> - constructor
e('Drawer.lambda$populateDrawer$5', 'FtpServerFragment.<init>', 'CALL', 'Drawer creates FtpServerFragment via lambda',
  evidence='SRC Drawer.java:405')

# FtpServerFragment.onCreate - Fragment lifecycle
e('FtpServerFragment.<init>', 'FtpServerFragment.onCreate', 'LIFECYCLE', 'Fragment lifecycle onCreate after construction',
  evidence='SRC FtpServerFragment.java:93-98 shows onCreate implementation')

# FtpServerFragment.onCreateView - Fragment lifecycle
e('FtpServerFragment.onCreate', 'FtpServerFragment.onCreateView', 'LIFECYCLE', 'Fragment lifecycle onCreateView after onCreate',
  evidence='SRC FtpServerFragment.java:100-104 shows onCreateView implementation')

# FtpServerFragment.onActivityCreated - Fragment lifecycle
e('FtpServerFragment.onCreateView', 'FtpServerFragment.onActivityCreated', 'LIFECYCLE', 'Fragment lifecycle onActivityCreated after onCreateView',
  evidence='SRC FtpServerFragment.java:143-157 shows onActivityCreated implementation')

# FtpServerFragment.onResume - Fragment lifecycle
e('FtpServerFragment.onActivityCreated', 'FtpServerFragment.onResume', 'LIFECYCLE', 'Fragment lifecycle onResume after onActivityCreated',
  evidence='SRC FtpServerFragment.java:391-398 shows onResume implementation')

# FtpServerFragment.onPause - Fragment lifecycle
e('FtpServerFragment.onResume', 'FtpServerFragment.onPause', 'LIFECYCLE', 'Fragment lifecycle onPause when leaving',
  evidence='SRC FtpServerFragment.java:400-405 shows onPause implementation')

# FtpServerFragment.onCreateOptionsMenu - Framework callback
e('FtpServerFragment.onCreate', 'FtpServerFragment.onCreateOptionsMenu', 'FRAMEWORK', 'Framework calls onCreateOptionsMenu after setHasOptionsMenu(true)',
  evidence='SRC FtpServerFragment.java:96 sets setHasOptionsMenu; FtpServerFragment.java:365-367 shows onCreateOptionsMenu')

# FtpServerFragment.updateSpans called from onCreateView and onFtpReceiveActions
e('FtpServerFragment.onCreateView', 'FtpServerFragment.updateSpans', 'CALL', 'onCreateView calls updateSpans to initialize status text',
  evidence='SRC FtpServerFragment.java:119')

# FtpServerFragment.updateStatus called from onCreateView
e('FtpServerFragment.onCreateView', 'FtpServerFragment.updateStatus', 'CALL', 'onCreateView calls updateStatus to initialize UI',
  evidence='SRC FtpServerFragment.java:120')

# FtpServerFragment.startServer called from button click
e('FtpServerFragment.lambda$onCreateView$0', 'FtpServerFragment.startServer', 'CALL', 'Button click lambda calls startServer',
  evidence='SRC FtpServerFragment.java:132')

# FtpServerFragment.stopServer called from button click
e('FtpServerFragment.lambda$onCreateView$0', 'FtpServerFragment.stopServer', 'CALL', 'Button click lambda calls stopServer',
  evidence='SRC FtpServerFragment.java:139')

# FtpServerFragment.lambda$onCreateView$0 - button click handler
e('FtpServerFragment.onCreateView', 'FtpServerFragment.lambda$onCreateView$0', 'GUI', 'ftpBtn setOnClickListener registers lambda',
  evidence='SRC FtpServerFragment.java:127')

# FtpServerFragment.onOptionsItemSelected - menu item selection
e('FtpServerFragment.onCreateOptionsMenu', 'FtpServerFragment.onOptionsItemSelected', 'FRAMEWORK', 'Framework calls onOptionsItemSelected when menu item selected',
  evidence='SRC FtpServerFragment.java:159-360 shows handler')

# FtpServerFragment.getDefaultPortFromPreferences called from onOptionsItemSelected
e('FtpServerFragment.onOptionsItemSelected', 'FtpServerFragment.getDefaultPortFromPreferences', 'CALL', 'onOptionsItemSelected gets current port',
  evidence='SRC FtpServerFragment.java:162')

# FtpServerFragment.changeFTPServerPort called from lambda in onOptionsItemSelected
e('FtpServerFragment.lambda$onOptionsItemSelected$1', 'FtpServerFragment.changeFTPServerPort', 'CALL', 'Lambda calls changeFTPServerPort after dialog',
  evidence='SRC FtpServerFragment.java:172')

# FtpServerFragment.lambda$onOptionsItemSelected$1 - port dialog callback
e('FtpServerFragment.onOptionsItemSelected', 'FtpServerFragment.lambda$onOptionsItemSelected$1', 'GUI', 'MaterialDialog onPositive callback',
  evidence='SRC FtpServerFragment.java:167')

# FtpServerFragment.getDefaultPathFromPreferences called from onOptionsItemSelected
e('FtpServerFragment.onOptionsItemSelected', 'FtpServerFragment.getDefaultPathFromPreferences', 'CALL', 'onOptionsItemSelected gets current path',
  evidence='SRC FtpServerFragment.java:186')

# FtpServerFragment.changeFTPServerPath called from lambda in onOptionsItemSelected
e('FtpServerFragment.lambda$onOptionsItemSelected$2', 'FtpServerFragment.changeFTPServerPath', 'CALL', 'Lambda calls changeFTPServerPath after dialog',
  evidence='SRC FtpServerFragment.java:197')

# FtpServerFragment.lambda$onOptionsItemSelected$2 - path dialog callback
e('FtpServerFragment.onOptionsItemSelected', 'FtpServerFragment.lambda$onOptionsItemSelected$2', 'GUI', 'MaterialDialog onPositive callback',
  evidence='SRC FtpServerFragment.java:188')

# FtpServerFragment.lambda$onOptionsItemSelected$3 - path dialog else branch callback
e('FtpServerFragment.onOptionsItemSelected', 'FtpServerFragment.lambda$onOptionsItemSelected$3', 'GUI', 'MaterialDialog input callback',
  evidence='SRC FtpServerFragment.java:185')

# FtpServerFragment.initLoginDialogViews called from onOptionsItemSelected
e('FtpServerFragment.onOptionsItemSelected', 'FtpServerFragment.initLoginDialogViews', 'CALL', 'onOptionsItemSelected initializes login dialog',
  evidence='SRC FtpServerFragment.java:226')

# FtpServerFragment.setFTPUsername called from lambda in onOptionsItemSelected
e('FtpServerFragment.lambda$onOptionsItemSelected$4', 'FtpServerFragment.setFTPUsername', 'CALL', 'Lambda calls setFTPUsername',
  evidence='SRC FtpServerFragment.java:234')

# FtpServerFragment.setFTPPassword called from lambda in onOptionsItemSelected
e('FtpServerFragment.lambda$onOptionsItemSelected$4', 'FtpServerFragment.setFTPPassword', 'CALL', 'Lambda calls setFTPPassword',
  evidence='SRC FtpServerFragment.java:245')

# FtpServerFragment.lambda$onOptionsItemSelected$4 - login dialog callback
e('FtpServerFragment.onOptionsItemSelected', 'FtpServerFragment.lambda$onOptionsItemSelected$4', 'GUI', 'MaterialDialog onPositive callback for login',
  evidence='SRC FtpServerFragment.java:230')

# FtpServerFragment.setSecurePreference called from lambda in onOptionsItemSelected
e('FtpServerFragment.lambda$onOptionsItemSelected$4', 'FtpServerFragment.setSecurePreference', 'CALL', 'Lambda calls setSecurePreference',
  evidence='SRC FtpServerFragment.java:250')

# FtpServerFragment.getFTPTimeout called from onOptionsItemSelected
e('FtpServerFragment.onOptionsItemSelected', 'FtpServerFragment.getFTPTimeout', 'CALL', 'onOptionsItemSelected gets current timeout',
  evidence='SRC FtpServerFragment.java:262')

# FtpServerFragment.setFTPTimeout called from lambda in onOptionsItemSelected
e('FtpServerFragment.lambda$onOptionsItemSelected$5', 'FtpServerFragment.setFTPTimeout', 'CALL', 'Lambda calls setFTPTimeout',
  evidence='SRC FtpServerFragment.java:278')

# FtpServerFragment.lambda$onOptionsItemSelected$5 - timeout dialog callback
e('FtpServerFragment.onOptionsItemSelected', 'FtpServerFragment.lambda$onOptionsItemSelected$5', 'GUI', 'MaterialDialog input callback for timeout',
  evidence='SRC FtpServerFragment.java:263')

# FtpServerFragment.lambda$onOptionsItemSelected$6 - another branch in timeout callback
e('FtpServerFragment.onOptionsItemSelected', 'FtpServerFragment.lambda$onOptionsItemSelected$6', 'GUI', 'MaterialDialog input callback alternate branch',
  evidence='SRC FtpServerFragment.java:263')

# FtpServerFragment.onFtpReceiveActions - EventBus callback
e('FtpServerFragment.onResume', 'FtpServerFragment.onFtpReceiveActions', 'ASYNC', 'EventBus delivers FtpReceiverActions after registration',
  evidence='SRC FtpServerFragment.java:397 registers; FtpServerFragment.java:334-361 shows @Subscribe handler')

# FtpServerFragment.getUsernameFromPreferences called from initLoginDialogViews
e('FtpServerFragment.initLoginDialogViews', 'FtpServerFragment.getUsernameFromPreferences', 'CALL', 'initLoginDialogViews gets username',
  evidence='SRC FtpServerFragment.java:528')

# FtpServerFragment.getPasswordFromPreferences called from initLoginDialogViews and updateStatus
e('FtpServerFragment.initLoginDialogViews', 'FtpServerFragment.getPasswordFromPreferences', 'CALL', 'initLoginDialogViews gets password',
  evidence='SRC FtpServerFragment.java:532')

# FtpServerFragment.getSecurePreference called from initLoginDialogViews
e('FtpServerFragment.initLoginDialogViews', 'FtpServerFragment.getSecurePreference', 'CALL', 'initLoginDialogViews gets secure preference',
  evidence='SRC FtpServerFragment.java:535')

# FtpServerFragment.lambda$initLoginDialogViews$8 - anonymous checkbox listener
e('FtpServerFragment.initLoginDialogViews', 'FtpServerFragment.lambda$initLoginDialogViews$8', 'GUI', 'Anonymous checkbox setOnCheckedChangeListener',
  evidence='SRC FtpServerFragment.java:516')

# FtpServerFragment.getFTPAddressString called from updateSpans
e('FtpServerFragment.updateSpans', 'FtpServerFragment.getFTPAddressString', 'CALL', 'updateSpans gets FTP address for display',
  evidence='SRC FtpServerFragment.java:486')

# FtpServerFragment.lambda$updateStatus$7 - password visibility toggle
e('FtpServerFragment.updateStatus', 'FtpServerFragment.lambda$updateStatus$7', 'GUI', 'ftpPasswordVisibleButton setOnClickListener',
  evidence='SRC FtpServerFragment.java:457')

# FtpServerFragment$1.<init> - BroadcastReceiver constructor
e('FtpServerFragment.<init>', 'FtpServerFragment$1.<init>', 'CALL', 'FtpServerFragment initializes mWifiReceiver field',
  evidence='SRC FtpServerFragment.java:369 shows field declaration')

# FtpServerFragment$1.onReceive - BroadcastReceiver callback
e('FtpServerFragment.onResume', 'FtpServerFragment$1.onReceive', 'SYSTEM', 'System delivers CONNECTIVITY_ACTION broadcast after registration',
  evidence='SRC FtpServerFragment.java:395 registers mWifiReceiver; FtpServerFragment.java:372-387 shows onReceive')

# UNREACHABLE methods from this batch
UNREACHABLE_BATCH_030 = {
}
