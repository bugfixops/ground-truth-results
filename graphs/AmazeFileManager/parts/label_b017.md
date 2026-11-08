STATUS: RUNNING 22:51

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| CryptHandler.<init> | REACHABLE | | Called from MainActivity.onDestroy, MainFragment.findEncryptedEntry, EncryptDecryptUtils.startEncryption, DeleteTask, MoveFiles, CopyService | SRC MainActivity.java:1214, MainFragment.java:952, EncryptDecryptUtils.java:48, DeleteTask.java:163, MoveFiles.java:188, CopyService.java:305 |
| CryptHandler.onCreate | REACHABLE | | Framework SQLiteOpenHelper lifecycle callback | SRC CryptHandler.java:37-44 extends SQLiteOpenHelper |
| CryptHandler.onUpgrade | REACHABLE | | Framework SQLiteOpenHelper lifecycle callback | SRC CryptHandler.java:47-52 extends SQLiteOpenHelper |
| CryptHandler.addEntry | REACHABLE | | Called from EncryptDecryptUtils.startEncryption | SRC EncryptDecryptUtils.java:48,54 |
| CryptHandler.clear | REACHABLE | | Called from DeleteTask to remove encrypted file entries | SRC DeleteTask.java:163-165 |
| CryptHandler.findEntry | REACHABLE | | Called from MainFragment.findEncryptedEntry and MoveFiles | SRC MainFragment.java:952-956, MoveFiles.java:188-189 |
| CryptHandler.getAllEntries | REACHABLE | | Called from MainFragment.findEncryptedEntry | SRC MainFragment.java:956 |
| CryptHandler.updateEntry | REACHABLE | | Called from MoveFiles to update encrypted file paths after move | SRC MoveFiles.java:194 |
| CryptUtil.<init>(Context,HybridFileParcelable,ProgressHandler,ArrayList,String) | REACHABLE | | Encryption constructor called from EncryptService | SRC EncryptService.java:191 |
| CryptUtil.<init>(Context,HybridFileParcelable,String,ProgressHandler,ArrayList) | REACHABLE | | Decryption constructor called from DecryptService | SRC DecryptService.java:149 |
| CryptUtil.encrypt | REACHABLE | | Called from encryption constructor | SRC CryptUtil.java:124 |
| CryptUtil.decrypt | REACHABLE | | Called from decryption constructor | SRC CryptUtil.java:152 |
| CryptUtil.aesEncrypt | REACHABLE | | Called from encrypt method on API 23+ | SRC CryptUtil.java:225 |
| CryptUtil.aesDecrypt | REACHABLE | | Called from decrypt method on API 23+ | SRC CryptUtil.java:206 |
| CryptUtil.rsaEncrypt | REACHABLE | | Called from encrypt method on API 18-22 | SRC CryptUtil.java:227 |
| CryptUtil.rsaDecrypt | REACHABLE | | Called from decrypt method on API 18-22 | SRC CryptUtil.java:208 |
| CryptUtil.encryptPassword | REACHABLE | | Called from CryptHandler.addEntry, CryptHandler.updateEntry, CloudHandler, FtpServerFragment, SmbUtil, PrefFrag | SRC CryptHandler.java:60,81, CloudHandler.java:94,129, FtpServerFragment.java:595, SmbUtil.java:56, PrefFrag.java:258 |
| CryptUtil.decryptPassword | REACHABLE | | Called from CryptHandler.findEntry, CryptHandler.getAllEntries, CloudHandler, FtpService, FtpServerFragment, SmbUtil, PrefFrag, EncryptDecryptUtils | SRC CryptHandler.java:97,120, CloudHandler.java:155,190, FtpService.java:167, FtpServerFragment.java:552, SmbUtil.java:34, PrefFrag.java:234, EncryptDecryptUtils.java:122 |
| CryptUtil.aesEncryptPassword | REACHABLE | | Called from encryptPassword on API 23+ | SRC CryptUtil.java:526 |
| CryptUtil.aesDecryptPassword | REACHABLE | | Called from decryptPassword on API 23+ | SRC CryptUtil.java:528 |
| CryptUtil.rsaEncryptPassword | REACHABLE | | Called from encryptPassword on API 18-22 | SRC CryptUtil.java:528 |
| CryptUtil.rsaDecryptPassword | REACHABLE | | Called from decryptPassword on API 18-22 | SRC CryptUtil.java:530 |
| CryptUtil.getSecretKey | REACHABLE | | Called from aesEncrypt, aesDecrypt, aesEncryptPassword, aesDecryptPassword on API 23+ | SRC CryptUtil.java:278,315,349,370 |
| CryptUtil.initCipher | REACHABLE | | Called from PrefFrag for fingerprint authentication | SRC PrefFrag.java:260 (checked via grep) |
| CryptUtil.lambda$decrypt$0 | REACHABLE | | Lambda generated for decrypt method | SRC CryptUtil.java:178 forEachChildrenFile callback |
| CryptUtil.lambda$encrypt$1 | REACHABLE | | Lambda generated for encrypt method | SRC CryptUtil.java:243 forEachChildrenFile callback |
| CustomFileObserver.<init> | REACHABLE | | Called from MainFragment to watch directory changes | SRC MainFragment.java:1194 |
| CustomFileObserver.startWatching | REACHABLE | | Called from MainFragment after observer creation | SRC MainFragment.java:1196 |
| CustomFileObserver.stopWatching | REACHABLE | | Called from MainFragment before creating new observer | SRC MainFragment.java:1192 |
| CustomFileObserver.onEvent | REACHABLE | | Framework FileObserver callback for file system events | SRC CustomFileObserver.java:83-119 overrides FileObserver.onEvent |
| CustomFileObserver.sendMessages | REACHABLE | | Called from onEvent to send buffered file change notifications | SRC CustomFileObserver.java:114,117 |
| CustomFileObserver.startPollingSystem | REACHABLE | | Called from startWatching on API 23 (Marshmallow workaround) | SRC CustomFileObserver.java:67 |
| CustomFileObserver.stopPollingSystem | REACHABLE | | Called from stopWatching on API 23 | SRC CustomFileObserver.java:77 |
| CustomFileObserver.getPath | REACHABLE | | Getter method for observer path | SRC CustomFileObserver.java:60 |
| CustomFileObserver.wasStopped | REACHABLE | | Status checker for observer state | SRC CustomFileObserver.java:56 |
| CustomFileObserver$1.<init> | REACHABLE | | Anonymous class constructor created by Timer in onEvent | SRC CustomFileObserver.java:108 new TimerTask() |
| CustomFileObserver$1.run | REACHABLE | | TimerTask callback to defer sendMessages call | SRC CustomFileObserver.java:110-114 |
| CustomFileObserver$FileTimerTask.<init> | REACHABLE | | Created by startPollingSystem for API 23 polling | SRC CustomFileObserver.java:155 |
| CustomFileObserver$FileTimerTask.run | REACHABLE | | Runnable executed periodically by scheduled executor | SRC CustomFileObserver.java:165-181 |
| CustomFileObserver$FileTimerTask.compare | REACHABLE | | Called from run to find directory changes | SRC CustomFileObserver$FileTimerTask.java:173,176 |

STATUS: DONE 22:53
