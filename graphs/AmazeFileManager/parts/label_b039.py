# ---- Batch 039: HybridFile anonymous inner classes (2026-10-27 23:30)
# 16 anonymous inner classes (HybridFile$1..14, nested $9$1, $10$1, $11$1)
# These are SFtpClientTemplate/SshClientTemplate callbacks created in HybridFile methods

# HybridFile$1: created in lastModified() at line 194
e('HybridFile.lastModified', 'HybridFile$1.<init>', 'CALL', 'creates SFtpClientTemplate for SFTP lastModified',
  evidence='SRC HybridFile.java:194')
e('HybridFile$1.<init>', 'SshClientUtils.execute', 'CALL', 'passes template to SshClientUtils.execute',
  evidence='SRC HybridFile.java:194')
e('SshClientUtils.execute', 'HybridFile$1.execute', 'FRAMEWORK', 'framework calls template.execute',
  evidence='SRC SshClientUtils.java:134')

# HybridFile$2: created in length() at line 224
e('HybridFile.length', 'HybridFile$2.<init>', 'CALL', 'creates SFtpClientTemplate for SFTP file size',
  evidence='SRC HybridFile.java:224')
e('HybridFile$2.<init>', 'SshClientUtils.execute', 'CALL', 'passes template to SshClientUtils.execute',
  evidence='SRC HybridFile.java:224')
e('SshClientUtils.execute', 'HybridFile$2.execute', 'FRAMEWORK', 'framework calls template.execute',
  evidence='SRC SshClientUtils.java:134')

# HybridFile$4: created in isDirectory(Context) at line 485
e('HybridFile.isDirectory', 'HybridFile$4.<init>', 'CALL', 'creates SFtpClientTemplate for SFTP directory check',
  evidence='SRC HybridFile.java:485')
e('HybridFile$4.<init>', 'SshClientUtils.execute', 'CALL', 'passes template to SshClientUtils.execute',
  evidence='SRC HybridFile.java:485')
e('SshClientUtils.execute', 'HybridFile$4.execute', 'FRAMEWORK', 'framework calls template.execute',
  evidence='SRC SshClientUtils.java:134')

# HybridFile$5: created in folderSize(Context) at line 584
e('HybridFile.folderSize', 'HybridFile$5.<init>', 'CALL', 'creates SFtpClientTemplate for SFTP folder size',
  evidence='SRC HybridFile.java:584')
e('HybridFile$5.<init>', 'SshClientUtils.execute', 'CALL', 'passes template to SshClientUtils.execute',
  evidence='SRC HybridFile.java:584')
e('SshClientUtils.execute', 'HybridFile$5.execute', 'FRAMEWORK', 'framework calls template.execute',
  evidence='SRC SshClientUtils.java:134')

# HybridFile$6: created in getUsableSpace() at line 651
e('HybridFile.getUsableSpace', 'HybridFile$6.<init>', 'CALL', 'creates SFtpClientTemplate for SFTP free space',
  evidence='SRC HybridFile.java:651')
e('HybridFile$6.<init>', 'SshClientUtils.execute', 'CALL', 'passes template to SshClientUtils.execute',
  evidence='SRC HybridFile.java:651')
e('SshClientUtils.execute', 'HybridFile$6.execute', 'FRAMEWORK', 'framework calls template.execute',
  evidence='SRC SshClientUtils.java:134')

# HybridFile$7: created in getTotal(Context) at line 704
e('HybridFile.getTotal', 'HybridFile$7.<init>', 'CALL', 'creates SFtpClientTemplate for SFTP total disk size',
  evidence='SRC HybridFile.java:704')
e('HybridFile$7.<init>', 'SshClientUtils.execute', 'CALL', 'passes template to SshClientUtils.execute',
  evidence='SRC HybridFile.java:704')
e('SshClientUtils.execute', 'HybridFile$7.execute', 'FRAMEWORK', 'framework calls template.execute',
  evidence='SRC SshClientUtils.java:134')

# HybridFile$8: created in forEachChildrenFile(Context,boolean,OnFileFound) at line 737
e('HybridFile.forEachChildrenFile', 'HybridFile$8.<init>', 'CALL', 'creates SFtpClientTemplate for SFTP file listing',
  evidence='SRC HybridFile.java:737')
e('HybridFile$8.<init>', 'SshClientUtils.execute', 'CALL', 'passes template to SshClientUtils.execute',
  evidence='SRC HybridFile.java:737')
e('SshClientUtils.execute', 'HybridFile$8.execute', 'FRAMEWORK', 'framework calls template.execute',
  evidence='SRC SshClientUtils.java:134')

# HybridFile$9: created in listFiles(Context,boolean) at line 810
e('HybridFile.listFiles', 'HybridFile$9.<init>', 'CALL', 'creates SFtpClientTemplate for SFTP file listing',
  evidence='SRC HybridFile.java:810')
e('HybridFile$9.<init>', 'SshClientUtils.execute', 'CALL', 'passes template to SshClientUtils.execute',
  evidence='SRC HybridFile.java:810')
e('SshClientUtils.execute', 'HybridFile$9.execute', 'FRAMEWORK', 'framework calls template.execute',
  evidence='SRC SshClientUtils.java:134')

# HybridFile$9$1: Cannot locate creation site in source - INCOMPLETE
# Constructor signature shows (HybridFile$9, RemoteFile, RemoteFile) but no instantiation
# found in HybridFile.java lines 810-831. Marked INCOMPLETE pending source verification.

# HybridFile$10: created in getInputStream() at line 905
e('HybridFile.getInputStream', 'HybridFile$10.<init>', 'CALL', 'creates SFtpClientTemplate for SFTP input stream',
  evidence='SRC HybridFile.java:905')
e('HybridFile$10.<init>', 'SshClientUtils.execute', 'CALL', 'passes template to SshClientUtils.execute',
  evidence='SRC HybridFile.java:905')
e('SshClientUtils.execute', 'HybridFile$10.execute', 'FRAMEWORK', 'framework calls template.execute',
  evidence='SRC SshClientUtils.java:134')

# HybridFile$10$1: RemoteFileInputStream created inside HybridFile$10.execute at line 909
e('HybridFile$10.execute', 'HybridFile$10$1.<init>', 'CALL', 'creates RemoteFileInputStream with custom close',
  evidence='SRC HybridFile.java:909')

# HybridFile$11: created in getInputStream(Context) at line 948
e('HybridFile.getInputStream', 'HybridFile$11.<init>', 'CALL', 'creates SFtpClientTemplate for SFTP input stream with context',
  evidence='SRC HybridFile.java:948')
e('HybridFile$11.<init>', 'SshClientUtils.execute', 'CALL', 'passes template to SshClientUtils.execute',
  evidence='SRC HybridFile.java:948')
e('SshClientUtils.execute', 'HybridFile$11.execute', 'FRAMEWORK', 'framework calls template.execute',
  evidence='SRC SshClientUtils.java:134')

# HybridFile$11$1: RemoteFileInputStream created inside HybridFile$11.execute at line 953
e('HybridFile$11.execute', 'HybridFile$11$1.<init>', 'CALL', 'creates RemoteFileInputStream with custom close',
  evidence='SRC HybridFile.java:953')

# HybridFile$12: created in getOutputStream(Context) at line 1021
e('HybridFile.getOutputStream', 'HybridFile$12.<init>', 'CALL', 'creates SshClientTemplate for SFTP output stream',
  evidence='SRC HybridFile.java:1021')
e('HybridFile$12.<init>', 'SshClientUtils.execute', 'CALL', 'passes template to SshClientUtils.execute',
  evidence='SRC HybridFile.java:1021')
e('SshClientUtils.execute', 'HybridFile$12.execute', 'FRAMEWORK', 'framework calls template.execute',
  evidence='SRC SshClientUtils.java:74')

# HybridFile$13: created in exists() at line 1078
e('HybridFile.exists', 'HybridFile$13.<init>', 'CALL', 'creates SFtpClientTemplate for SFTP exists check',
  evidence='SRC HybridFile.java:1078')
e('HybridFile$13.<init>', 'SshClientUtils.execute', 'CALL', 'passes template to SshClientUtils.execute',
  evidence='SRC HybridFile.java:1078')
e('SshClientUtils.execute', 'HybridFile$13.execute', 'FRAMEWORK', 'framework calls template.execute',
  evidence='SRC SshClientUtils.java:134')

# HybridFile$14: created in mkdir(Context) at line 1156
e('HybridFile.mkdir', 'HybridFile$14.<init>', 'CALL', 'creates SFtpClientTemplate for SFTP mkdir',
  evidence='SRC HybridFile.java:1156')
e('HybridFile$14.<init>', 'SshClientUtils.execute', 'CALL', 'passes template to SshClientUtils.execute',
  evidence='SRC HybridFile.java:1156')
e('SshClientUtils.execute', 'HybridFile$14.execute', 'FRAMEWORK', 'framework calls template.execute',
  evidence='SRC SshClientUtils.java:134')

# Note: HybridFile$9$1 needs investigation - need to find where it's actually created
