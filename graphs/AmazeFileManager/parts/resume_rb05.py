# ---- part resume_rb05 (2024-12-19)

# ColorPickerDialog.lambda$inflateItem$0
e('ColorPickerDialog.inflateItem', 'ColorPickerDialog.lambda$inflateItem$0', 'CALL',
  'Lambda click listener for color picker item',
  evidence='SRC ui/dialogs/ColorPickerDialog.java:169-176')

e('ColorPickerDialog.lambda$inflateItem$0', 'ColorPickerDialog.select', 'CALL',
  'Lambda calls select to update selection state',
  evidence='SRC ui/dialogs/ColorPickerDialog.java:170-174')

# ColorPickerDialog.setColorPreference
e('ColorPref.loadSection1', 'ColorPickerDialog.setColorPreference', 'CALL',
  'ColorPref sets color preferences on the dialog',
  evidence='SRC fragments/preference_fragments/ColorPref.java:223')

# ColorPickerDialog.setListener
e('ColorPref.loadSection1', 'ColorPickerDialog.setListener', 'CALL',
  'ColorPref sets listener on the dialog',
  evidence='SRC fragments/preference_fragments/ColorPref.java:224-232')

# ColorPref.lambda$loadSection1$1
e('ColorPickerDialog.setListener', 'ColorPref.lambda$loadSection1$1', 'CALL',
  'Lambda listener passed to setListener',
  evidence='SRC fragments/preference_fragments/ColorPref.java:224-232')

e('ColorPref.lambda$loadSection1$1', 'ColorPref.checkCustomization', 'CALL',
  'Lambda calls checkCustomization',
  evidence='SRC fragments/preference_fragments/ColorPref.java:226')

e('ColorPref.lambda$loadSection1$1', 'ColorPref.invalidateEverything', 'CALL',
  'Lambda calls invalidateEverything',
  evidence='SRC fragments/preference_fragments/ColorPref.java:227')

# ComputerParcelable.<init>(String,String)
e('SmbSearchDialog.onCreateDialog', 'ComputerParcelable.<init>(String,String)', 'CALL',
  'Creates ComputerParcelable in SMB search dialog',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:78')

e('SubnetScanner$ScanNodeTask.call', 'ComputerParcelable.<init>(String,String)', 'CALL',
  'Creates ComputerParcelable in subnet scanner',
  evidence='SRC utils/SubnetScanner.java:56,58')

e('SubnetScanner$4.run', 'ComputerParcelable.<init>(String,String)', 'CALL',
  'Creates ComputerParcelable from hostname lookup',
  evidence='SRC utils/SubnetScanner.java:157')

# ComputerParcelable.<init>(Parcel) - UNREACHABLE
# Already marked UNREACHABLE in graph_def.py:9344 - ComputerParcelable is never unparceled in app

# CopyService$1.onReceive
e('ProcessViewerFragment.cancelBroadcast', 'CopyService$1.onReceive', 'INTENT',
  'ProcessViewerFragment sends TAG_BROADCAST_COPY_CANCEL broadcast to cancel copy',
  evidence='SRC fragments/ProcessViewerFragment.java:251; asynchronous/services/CopyService.java:100 registerReceiver(receiver3, new IntentFilter(TAG_BROADCAST_COPY_CANCEL))')

e('CopyService.onStartCommand', 'CopyService$1.onReceive', 'INTENT',
  'Notification stop button sends TAG_BROADCAST_COPY_CANCEL broadcast',
  evidence='SRC asynchronous/services/CopyService.java:129 stopIntent = new Intent(TAG_BROADCAST_COPY_CANCEL), 130 stopPendingIntent = PendingIntent.getBroadcast(...), 131-132 action added to notification; 100 registerReceiver(receiver3, new IntentFilter(TAG_BROADCAST_COPY_CANCEL))')
