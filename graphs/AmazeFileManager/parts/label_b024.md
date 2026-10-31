STATUS: RUNNING 22:59

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| ExtractService.<clinit> | UNREACHABLE | no_trigger_in_app | Only static final String constants; compile-time initialization, no runtime <clinit> needed | SRC ExtractService.java:69,85-88 |
| ExtractService.<init> | UNREACHABLE | framework_never_calls | Service instantiated by framework via no-arg constructor only; explicit constructor not in source | SRC ExtractService.java:65 (no explicit constructor defined) |
| ExtractService.getDataPackages | REACHABLE | | Called by parent AbstractProgressiveService and ProcessViewerFragment | SRC ExtractService.java:191-193, AbstractProgressiveService.java (parent) |
| ExtractService.getNotificationBuilder | REACHABLE | | Called by parent AbstractProgressiveService.publishResults | SRC ExtractService.java:155-157, AbstractProgressiveService.java |
| ExtractService.getNotificationCustomViewBig | REACHABLE | | Called by parent AbstractProgressiveService.publishResults | SRC ExtractService.java:174-176, AbstractProgressiveService.java |
| ExtractService.getNotificationCustomViewSmall | REACHABLE | | Called by parent AbstractProgressiveService.publishResults | SRC ExtractService.java:170-172, AbstractProgressiveService.java |
| ExtractService.getNotificationId | REACHABLE | | Called by parent AbstractProgressiveService | SRC ExtractService.java:159-161, AbstractProgressiveService.java |
| ExtractService.getNotificationManager | REACHABLE | | Called by parent AbstractProgressiveService.publishResults | SRC ExtractService.java:151-153, AbstractProgressiveService.java |
| ExtractService.getProgressHandler | REACHABLE | | Called by parent AbstractProgressiveService | SRC ExtractService.java:195-197, AbstractProgressiveService.java |
| ExtractService.getProgressListener | REACHABLE | | Called by ProcessViewerFragment when bound | SRC ExtractService.java:178-180, ProcessViewerFragment.java:161 |
| ExtractService.getTitle | REACHABLE | | Called by parent AbstractProgressiveService.publishResults | SRC ExtractService.java:163-167, AbstractProgressiveService.java:94 |
| ExtractService.getTotalSize | REACHABLE | | Called from onStartCommand | SRC ExtractService.java:207-209, ExtractService.java:138 |
| ExtractService.lambda$onStartCommand$0 | REACHABLE | | Lambda set as progress listener in onStartCommand | SRC ExtractService.java:142-143 |
| ExtractService.onBind | REACHABLE | | ProcessViewerFragment binds to ExtractService | SRC ExtractService.java:387-389, ProcessViewerFragment.java:161 |
| ExtractService.onCreate | REACHABLE | | Service lifecycle callback | SRC ExtractService.java:89-92 |
| ExtractService.onDestroy | REACHABLE | | Service lifecycle callback | SRC ExtractService.java:199-201 |
| ExtractService.onStartCommand | REACHABLE | | Service started via Decompressor.decompress -> ServiceWatcherUtil.runService -> startService | SRC ExtractService.java:94-147, Decompressor.java:44-48, ServiceWatcherUtil.java:163 |
| ExtractService.setProgressListener | REACHABLE | | Called from onStartCommand and ProcessViewerFragment | SRC ExtractService.java:182-185, ExtractService.java:142, ProcessViewerFragment.java:161 |
| ExtractService$1.<init> | REACHABLE | | BroadcastReceiver constructed in field initializer | SRC ExtractService.java:383-389 |
| ExtractService$1.onReceive | REACHABLE | | BroadcastReceiver callback for TAG_BROADCAST_EXTRACT_CANCEL | SRC ExtractService.java:384-387, ExtractService.java:90 |
| ExtractService$DoWork.<init> | REACHABLE | | Constructed in onStartCommand | SRC ExtractService.java:222-230, ExtractService.java:146 |
| ExtractService$DoWork.doInBackground | REACHABLE | | AsyncTask execution from onStartCommand | SRC ExtractService.java:232-320, ExtractService.java:146 |
| ExtractService$DoWork.lambda$onProgressUpdate$0 | REACHABLE | | Positive button lambda in password dialog | SRC ExtractService.java:333-338, ExtractService.java:332 |
| ExtractService$DoWork.lambda$onProgressUpdate$1 | REACHABLE | | Negative button lambda in password dialog | SRC ExtractService.java:341-348, ExtractService.java:341 |
| ExtractService$DoWork.onPostExecute | REACHABLE | | AsyncTask lifecycle callback after doInBackground | SRC ExtractService.java:350-361, ExtractService.java:146 |
| ExtractService$DoWork.onProgressUpdate | REACHABLE | | AsyncTask progress callback from publishProgress | SRC ExtractService.java:323-349, ExtractService.java:255,318 |
| ExtractService$DoWork.toastOnParseError | REACHABLE | | Called from lambda$onProgressUpdate$1 | SRC ExtractService.java:363-367, ExtractService.java:343 |
| ExtractService$DoWork$1.<init> | REACHABLE | | Anonymous OnUpdate callback constructed in doInBackground | SRC ExtractService.java:257-291, ExtractService.java:257 |
| ExtractService$DoWork$1.isCancelled | REACHABLE | | Extractor callback | SRC ExtractService.java:290-292, ExtractService.java:257 |
| ExtractService$DoWork$1.onFinish | REACHABLE | | Extractor callback | SRC ExtractService.java:279-283, ExtractService.java:257 |
| ExtractService$DoWork$1.onStart | REACHABLE | | Extractor callback | SRC ExtractService.java:261-271, ExtractService.java:257 |
| ExtractService$DoWork$1.onUpdate | REACHABLE | | Extractor callback | SRC ExtractService.java:273-278, ExtractService.java:257 |
| EncryptedEntry.<init> | REACHABLE | | No-arg constructor called from CryptHandler.findEntry and getAllEntries | SRC EncryptedEntry.java:12, CryptHandler.java:93,117 |
| EncryptedEntry.<init> | REACHABLE | | Two-arg constructor called from EncryptDecryptUtils.startEncryption | SRC EncryptedEntry.java:14-17, EncryptDecryptUtils.java:54 |
| EncryptedEntry.getId | REACHABLE | | Called from CryptHandler.updateEntry | SRC EncryptedEntry.java:20-22, CryptHandler.java:79,85 |
| EncryptedEntry.getPassword | REACHABLE | | Called from CryptHandler.addEntry and updateEntry | SRC EncryptedEntry.java:32-34, CryptHandler.java:60-61,82 |
| EncryptedEntry.getPath | REACHABLE | | Called from CryptHandler.addEntry and updateEntry | SRC EncryptedEntry.java:28-30, CryptHandler.java:59,80 |
| EncryptedEntry.setId | REACHABLE | | Called from CryptHandler.findEntry and getAllEntries | SRC EncryptedEntry.java:16-18, CryptHandler.java:95,118 |
| EncryptedEntry.setPassword | REACHABLE | | Called from CryptHandler.findEntry and getAllEntries | SRC EncryptedEntry.java:24-26, CryptHandler.java:97,120-121 |
| EncryptedEntry.setPath | REACHABLE | | Called from CryptHandler.findEntry and getAllEntries | SRC EncryptedEntry.java:20-22, CryptHandler.java:96,119 |

STATUS: DONE 23:04
