# ---- Helper batch_017 label part (2025-01-18)

# CryptHandler edges
e('MainActivity.onDestroy', 'CryptHandler.<init>(Context)', 'CALL', 'MainActivity closes database handlers on destroy',
  evidence='SRC MainActivity.java:1214')

e('MainFragment.findEncryptedEntry', 'CryptHandler.<init>(Context)', 'CALL', 'Creates handler to query encrypted entries',
  evidence='SRC MainFragment.java:952')

e('EncryptDecryptUtils.startEncryption', 'CryptHandler.<init>(Context)', 'CALL', 'Creates handler to add encrypted entry',
  evidence='SRC EncryptDecryptUtils.java:48')

e('DeleteTask.doInBackground', 'CryptHandler.<init>(Context)', 'CALL', 'Creates handler to delete encrypted entry',
  evidence='SRC DeleteTask.java:163')

e('MoveFiles.doInBackground', 'CryptHandler.<init>(Context)', 'CALL', 'Creates handler to update encrypted entry path',
  evidence='SRC MoveFiles.java:188')

e('CopyService.onStartCommand', 'CryptHandler.<init>(Context)', 'CALL', 'Creates handler in copy service',
  evidence='SRC CopyService.java:305')

e('CryptHandler.<init>(Context)', 'SQLiteOpenHelper.<init>', 'FRAMEWORK', 'Extends SQLiteOpenHelper',
  evidence='SRC CryptHandler.java:21 extends SQLiteOpenHelper, FW-SRC android/database/sqlite/SQLiteOpenHelper.java:132-164')

e('SQLiteOpenHelper.getWritableDatabase', 'CryptHandler.onCreate', 'LIFECYCLE', 'Framework calls onCreate when database created',
  evidence='SRC CryptHandler.java:37 onCreate signature, FW-SRC android/database/sqlite/SQLiteOpenHelper.java:256-294')

e('SQLiteOpenHelper.getWritableDatabase', 'CryptHandler.onUpgrade', 'LIFECYCLE', 'Framework calls onUpgrade on version change',
  evidence='SRC CryptHandler.java:47 onUpgrade signature, FW-SRC android/database/sqlite/SQLiteOpenHelper.java:256-294')

e('EncryptDecryptUtils.startEncryption', 'CryptHandler.addEntry', 'CALL', 'Adds encrypted file entry to database',
  evidence='SRC EncryptDecryptUtils.java:54')

e('DeleteTask.doInBackground', 'CryptHandler.clear', 'CALL', 'Removes encrypted entry when file deleted',
  evidence='SRC DeleteTask.java:165')

e('MainFragment.findEncryptedEntry', 'CryptHandler.findEntry', 'CALL', 'Queries encrypted entry by path',
  evidence='SRC MainFragment.java:956')

e('MoveFiles.doInBackground', 'CryptHandler.findEntry', 'CALL', 'Finds encrypted entry before updating path',
  evidence='SRC MoveFiles.java:189')

e('MainFragment.findEncryptedEntry', 'CryptHandler.getAllEntries', 'CALL', 'Retrieves all encrypted entries to find match',
  evidence='SRC MainFragment.java:956')

e('MoveFiles.doInBackground', 'CryptHandler.updateEntry', 'CALL', 'Updates encrypted file path after move',
  evidence='SRC MoveFiles.java:194')

e('CryptHandler.addEntry', 'CryptUtil.encryptPassword', 'CALL', 'Encrypts password before storing',
  evidence='SRC CryptHandler.java:60')

e('CryptHandler.updateEntry', 'CryptUtil.encryptPassword', 'CALL', 'Encrypts password before updating',
  evidence='SRC CryptHandler.java:81')

e('CryptHandler.findEntry', 'CryptUtil.decryptPassword', 'CALL', 'Decrypts password from database',
  evidence='SRC CryptHandler.java:97')

e('CryptHandler.getAllEntries', 'CryptUtil.decryptPassword', 'CALL', 'Decrypts password for each entry',
  evidence='SRC CryptHandler.java:120')

# CryptUtil edges
e('EncryptService.onStartCommand', 'CryptUtil.<init>(Context,HybridFileParcelable,ProgressHandler,ArrayList,String)', 'CALL', 'Constructor starts encryption process',
  evidence='SRC EncryptService.java:191')

e('DecryptService.onStartCommand', 'CryptUtil.<init>(Context,HybridFileParcelable,String,ProgressHandler,ArrayList)', 'CALL', 'Constructor starts decryption process',
  evidence='SRC DecryptService.java:149')

e('CryptUtil.<init>(Context,HybridFileParcelable,ProgressHandler,ArrayList,String)', 'CryptUtil.encrypt', 'CALL', 'Encryption constructor calls encrypt',
  evidence='SRC CryptUtil.java:124')

e('CryptUtil.<init>(Context,HybridFileParcelable,String,ProgressHandler,ArrayList)', 'CryptUtil.decrypt', 'CALL', 'Decryption constructor calls decrypt',
  evidence='SRC CryptUtil.java:152')

e('CryptUtil.encrypt', 'CryptUtil.aesEncrypt', 'CALL', 'Encrypts file using AES on API 23+',
  evidence='SRC CryptUtil.java:225')

e('CryptUtil.encrypt', 'CryptUtil.rsaEncrypt', 'CALL', 'Encrypts file using RSA on API 18-22',
  evidence='SRC CryptUtil.java:227')

e('CryptUtil.decrypt', 'CryptUtil.aesDecrypt', 'CALL', 'Decrypts file using AES on API 23+',
  evidence='SRC CryptUtil.java:206')

e('CryptUtil.decrypt', 'CryptUtil.rsaDecrypt', 'CALL', 'Decrypts file using RSA on API 18-22',
  evidence='SRC CryptUtil.java:208')

e('CloudHandler.addEntry', 'CryptUtil.encryptPassword', 'CALL', 'Encrypts cloud service password',
  evidence='SRC CloudHandler.java:94')

e('CloudHandler.updateEntry', 'CryptUtil.encryptPassword', 'CALL', 'Encrypts cloud service password',
  evidence='SRC CloudHandler.java:129')

e('FtpServerFragment.onPreferenceChange', 'CryptUtil.encryptPassword', 'CALL', 'Encrypts FTP password',
  evidence='SRC FtpServerFragment.java:595')

e('SmbUtil.getSmbEncryptedPath', 'CryptUtil.encryptPassword', 'CALL', 'Encrypts SMB password',
  evidence='SRC SmbUtil.java:56')

e('PrefFrag.updatePreferencesMasterPassword', 'CryptUtil.encryptPassword', 'CALL', 'Encrypts master password',
  evidence='SRC PrefFrag.java:258')

e('CloudHandler.findEntry', 'CryptUtil.decryptPassword', 'CALL', 'Decrypts cloud service password',
  evidence='SRC CloudHandler.java:155')

e('CloudHandler.getAllEntries', 'CryptUtil.decryptPassword', 'CALL', 'Decrypts cloud service passwords',
  evidence='SRC CloudHandler.java:190')

e('FtpService.onStartCommand', 'CryptUtil.decryptPassword', 'CALL', 'Decrypts FTP password',
  evidence='SRC FtpService.java:167')

e('FtpServerFragment.getPasswordFromPreferences', 'CryptUtil.decryptPassword', 'CALL', 'Decrypts FTP password',
  evidence='SRC FtpServerFragment.java:552')

e('SmbUtil.getSmbDecryptedPath', 'CryptUtil.decryptPassword', 'CALL', 'Decrypts SMB password',
  evidence='SRC SmbUtil.java:34')

e('PrefFrag.showMasterPasswordDialog', 'CryptUtil.decryptPassword', 'CALL', 'Decrypts master password',
  evidence='SRC PrefFrag.java:234')

e('EncryptDecryptUtils.decryptFile', 'CryptUtil.decryptPassword', 'CALL', 'Decrypts file password',
  evidence='SRC EncryptDecryptUtils.java:122')

e('CryptUtil.encryptPassword', 'CryptUtil.aesEncryptPassword', 'CALL', 'Uses AES password encryption on API 23+',
  evidence='SRC CryptUtil.java:526')

e('CryptUtil.encryptPassword', 'CryptUtil.rsaEncryptPassword', 'CALL', 'Uses RSA password encryption on API 18-22',
  evidence='SRC CryptUtil.java:528')

e('CryptUtil.decryptPassword', 'CryptUtil.aesDecryptPassword', 'CALL', 'Uses AES password decryption on API 23+',
  evidence='SRC CryptUtil.java:528')

e('CryptUtil.decryptPassword', 'CryptUtil.rsaDecryptPassword', 'CALL', 'Uses RSA password decryption on API 18-22',
  evidence='SRC CryptUtil.java:530')

e('CryptUtil.aesEncrypt', 'CryptUtil.getSecretKey', 'CALL', 'Gets AES key for encryption',
  evidence='SRC CryptUtil.java:278')

e('CryptUtil.aesDecrypt', 'CryptUtil.getSecretKey', 'CALL', 'Gets AES key for decryption',
  evidence='SRC CryptUtil.java:315')

e('CryptUtil.aesEncryptPassword', 'CryptUtil.getSecretKey', 'CALL', 'Gets AES key for password encryption',
  evidence='SRC CryptUtil.java:349')

e('CryptUtil.aesDecryptPassword', 'CryptUtil.getSecretKey', 'CALL', 'Gets AES key for password decryption',
  evidence='SRC CryptUtil.java:370')

e('GeneralDialogCreation.showAuthenticationDialog', 'CryptUtil.initCipher', 'CALL', 'Initializes cipher for fingerprint authentication',
  evidence='SRC GeneralDialogCreation.java:833')

e('CryptUtil.encrypt', 'CryptUtil.lambda$encrypt$1', 'ASYNC', 'Lambda callback for recursive directory encryption',
  evidence='SRC CryptUtil.java:243')

e('CryptUtil.decrypt', 'CryptUtil.lambda$decrypt$0', 'ASYNC', 'Lambda callback for recursive directory decryption',
  evidence='SRC CryptUtil.java:178')

# CustomFileObserver edges
e('MainFragment.updateList', 'CustomFileObserver.<init>', 'CALL', 'Creates file observer for current directory',
  evidence='SRC MainFragment.java:1194')

e('MainFragment.updateList', 'CustomFileObserver.startWatching', 'CALL', 'Starts watching after observer creation',
  evidence='SRC MainFragment.java:1196')

e('MainFragment.updateList', 'CustomFileObserver.stopWatching', 'CALL', 'Stops previous observer before creating new one',
  evidence='SRC MainFragment.java:1192')

e('CustomFileObserver.startWatching', 'CustomFileObserver.startPollingSystem', 'CALL', 'Uses polling on API 23 due to framework bug',
  evidence='SRC CustomFileObserver.java:67')

e('CustomFileObserver.startWatching', 'FileObserver.startWatching', 'FRAMEWORK', 'Calls super on other API levels',
  evidence='SRC CustomFileObserver.java:69')

e('CustomFileObserver.stopWatching', 'CustomFileObserver.stopPollingSystem', 'CALL', 'Stops polling on API 23',
  evidence='SRC CustomFileObserver.java:77')

e('CustomFileObserver.stopWatching', 'FileObserver.startWatching', 'FRAMEWORK', 'Calls super on other API levels',
  evidence='SRC CustomFileObserver.java:79')

e('FileObserver.inotify', 'CustomFileObserver.onEvent', 'FRAMEWORK', 'Framework delivers file system events',
  evidence='SRC CustomFileObserver.java:83 overrides FileObserver.onEvent, FW-SRC android/os/FileObserver.java:239-249')

e('CustomFileObserver.onEvent', 'CustomFileObserver.sendMessages', 'CALL', 'Sends buffered messages after defer period',
  evidence='SRC CustomFileObserver.java:114,117')

e('CustomFileObserver.onEvent', 'CustomFileObserver$1.<init>', 'CALL', 'Creates TimerTask to defer message sending',
  evidence='SRC CustomFileObserver.java:108')

e('Timer.schedule', 'CustomFileObserver$1.run', 'FRAMEWORK', 'Timer executes TimerTask',
  evidence='SRC CustomFileObserver.java:109,110')

e('CustomFileObserver$1.run', 'CustomFileObserver.sendMessages', 'CALL', 'Deferred call to send buffered messages',
  evidence='SRC CustomFileObserver.java:113')

e('CustomFileObserver.startPollingSystem', 'CustomFileObserver$FileTimerTask.<init>', 'CALL', 'Creates polling task for API 23',
  evidence='SRC CustomFileObserver.java:155')

e('ScheduledExecutorService.scheduleWithFixedDelay', 'CustomFileObserver$FileTimerTask.run', 'FRAMEWORK', 'Executor runs polling task periodically',
  evidence='SRC CustomFileObserver.java:156')

e('CustomFileObserver$FileTimerTask.run', 'CustomFileObserver$FileTimerTask.compare', 'CALL', 'Compares file lists to detect changes',
  evidence='SRC CustomFileObserver.java:173,176')

e('CustomFileObserver$FileTimerTask.run', 'CustomFileObserver.onEvent', 'CALL', 'Reports detected changes as events',
  evidence='SRC CustomFileObserver.java:173,176')
