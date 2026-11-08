# Repair batch 23 - Label additions for AmazeFileManager
# This file contains only e() edges and UNREACHABLE[...] assignments

# ==== ZipService$1.onReceive ====
e('ZipService.onCreate', 'ZipService$1.<init>', 'CALL', 'Anonymous BroadcastReceiver instantiated',
  evidence='SRC asynchronous/services/ZipService.java:305-310')
e('ZipService$1.<init>', 'ZipService$1.onReceive', 'FRAMEWORK', 'BroadcastReceiver.onReceive called by framework',
  evidence='SRC asynchronous/services/ZipService.java:86, 307')

# ==== HybridFile$9$1.close, HybridFile$11$1.close ====
e('HybridFile$9$1.<init>', 'HybridFile$9$1.close', 'CALL', 'InputStream.close() called when stream closed',
  evidence='SRC filesystem/HybridFile.java:909-920')
e('HybridFile$11$1.<init>', 'HybridFile$11$1.close', 'CALL', 'InputStream.close() called when stream closed',
  evidence='SRC filesystem/HybridFile.java:952-965')

# ==== Operations$1.doInBackground ====
e('Operations.mkdir', 'Operations$1.<init>', 'CALL', 'Anonymous AsyncTask instantiated',
  evidence='SRC filesystem/Operations.java:83')
e('Operations$1.<init>', 'Operations$1.doInBackground', 'ASYNC', 'AsyncTask.doInBackground called by framework',
  evidence='SRC filesystem/Operations.java:88-194')

# ==== Operations$2.doInBackground ====
e('Operations.mkfile', 'Operations$2.<init>', 'CALL', 'Anonymous AsyncTask instantiated',
  evidence='SRC filesystem/Operations.java:197')
e('Operations$2.<init>', 'Operations$2.doInBackground', 'ASYNC', 'AsyncTask.doInBackground called by framework',
  evidence='SRC filesystem/Operations.java:202-332')

# ==== Operations$3$1.<init> ====
e('Operations.rename', 'Operations$3.<init>', 'CALL', 'Anonymous AsyncTask instantiated',
  evidence='SRC filesystem/Operations.java:335')
e('Operations$3.<init>', 'Operations$3.doInBackground', 'ASYNC', 'AsyncTask.doInBackground',
  evidence='SRC filesystem/Operations.java:341')
e('Operations$3.doInBackground', 'Operations$3$1.<init>', 'CALL', 'Anonymous ErrorCallBack instantiated',
  evidence='SRC filesystem/Operations.java:369')

# ==== Library classes without source ====
UNREACHABLE['NID.<init>'] = ('no_trigger_in_app', 'Apache Commons Compress library class; no app instantiation', 'class not in app source', 'INFERRED')
UNREACHABLE['SevenZMethod.getId'] = ('no_trigger_in_app', 'Apache Commons Compress library class method', 'class not in app source', 'INFERRED')
UNREACHABLE['StreamMap.toString'] = ('no_trigger_in_app', 'Apache Commons Compress library class toString', 'class not in app source', 'INFERRED')
UNREACHABLE['RarDecompressor.realRelativeDirectory'] = ('no_trigger_in_app', 'junrar library class method', 'class not in app source', 'INFERRED')
UNREACHABLE['Statvfs.<init>'] = ('no_trigger_in_app', 'sshj library class constructor', 'class not in app source', 'INFERRED')

# ==== Constants classes ====
UNREACHABLE['PreferencesConstants.<init>'] = ('no_trigger_in_app', 'Constants class never instantiated', 'SRC fragments/preference_fragments/PreferencesConstants.java:8', 'SOURCE')
UNREACHABLE['NotificationConstants.<init>'] = ('no_trigger_in_app', 'Constants class never instantiated', 'SRC ui/notifications/NotificationConstants.java:18', 'SOURCE')

# ==== Utility class ====
UNREACHABLE['OTGUtil.<init>'] = ('no_trigger_in_app', 'Utility class with static methods only', 'SRC utils/OTGUtil.java', 'INFERRED')

# ==== Methods marked INCOMPLETE (need further analysis beyond slot capacity) ====
# SshClientTemplate.<init>(String) - single-param constructor delegates to two-param; need to verify if ever called directly
# UsbOtgRepresentation.equals - need grep to verify equals() usage
# CircleGradientDrawable.<init>(String,AppTheme,DisplayMetrics) - custom view, needs instantiation analysis
# Indicator$PendingRevealAnimator.lambda$new$0 - lambda, needs decompilation context
# ThemedTextView.<init> - custom view, likely inflated
# WarnableTextInputLayout.<init> - custom view, likely inflated
# SmbSearchDialog$ElementViewHolder.<init> - RecyclerView ViewHolder
# ComputerParcelable$1.<init> - Parcelable CREATOR anonymous class
# DataUtils$DataUtilsHolder.<init> - singleton holder pattern
# ProgressHandler.<init>(int,long) - specific overload needs verification
# ServiceWatcherUtil$1.run - Runnable anonymous class
