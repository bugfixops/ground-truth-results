STATUS: RUNNING 23:36

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| MainActivity$2.<init> | REACHABLE | | Called from MainActivity.onResume to create receiver2 instance | SRC MainActivity.java:1610 (receiver2 = new BroadcastReceiver), 1120 (registerReceiver) |
| MainActivity$2.onReceive | REACHABLE | | Framework calls when broadcast with TAG_INTENT_FILTER_GENERAL received | SRC MainActivity.java:1612-1618 (onReceive method showing intent handling) |
| MainActivity$3.<init> | REACHABLE | | Called from MainActivity.updateUsbInformation to create mOtgReceiver | SRC MainActivity.java:1171 (BroadcastReceiver mOtgReceiver = new), 1165 (registerReceiver) |
| MainActivity$3.onReceive | REACHABLE | | Framework calls when USB device attached/detached | SRC MainActivity.java:1172-1186 (onReceive method with USB actions) |
| MainActivity$FabActionListener.<init> | REACHABLE | | Called from MainActivity.initialiseFab to create FAB listener | SRC MainActivity.java:1508 (new FabActionListener(this)), 1935 (constructor) |
| MainActivity$FabActionListener.onActionSelected | REACHABLE | | GUI callback when user selects FAB menu item | SRC MainActivity.java:1940-1959 (onActionSelected with switch on actionItem.getId()) |
| MainActivityHelper.<init> | REACHABLE | | Called from MainActivity.onCreate to instantiate helper | SRC MainActivityHelper.java:82-85 (constructor), MainActivity.java:184 (field), onCreate instantiates |
| MainActivityHelper.addSearchFragment | REACHABLE | | Static method called from search to add SearchWorkerFragment | SRC MainActivityHelper.java:607 (addSearchFragment call), 624-642 (method definition) |
| MainActivityHelper.checkFolder | REACHABLE | | Called from MainActivity.onActivityResult for SAF checks | SRC MainActivityHelper.java:338-373 (method), MainActivity.java:565,573 (calls) |
| MainActivityHelper.compressFiles | REACHABLE | | Called from MainActivity.onActivityResult after SAF permission | SRC MainActivityHelper.java:375-388 (method), MainActivity.java:1386 (call) |
| MainActivityHelper.deleteFiles | REACHABLE | | Called from GeneralDialogCreation.showDeleteDialog | SRC MainActivityHelper.java:507-520 (method), GeneralDialogCreation.java:201 (call) |
| MainActivityHelper.extractFile | REACHABLE | | Called from MainActivity.onOptionsItemSelected and onActivityResult | SRC MainActivityHelper.java:522-531 (method), MainActivity.java:1037,1383 (calls) |
| MainActivityHelper.getIntegralNames | REACHABLE | | Called from BottomBar.updatePath for localized names | SRC MainActivityHelper.java:206-232 (method), BottomBar.java:314 (call) |
| MainActivityHelper.guideDialogForLEXA | REACHABLE | | Called from rename/mkFile/mkDir/checkFolder when SAF needed | SRC MainActivityHelper.java:234-254 (method), 249,288,413,470,349 (lambda/calls) |
| MainActivityHelper.isNewDirectoryRecursive | UNREACHABLE | no_trigger_in_app | Static utility method never called in app source | SRC MainActivityHelper.java:644-646 (method definition); grep shows no call sites |
| MainActivityHelper.lambda$guideDialogForLEXA$4 | REACHABLE | | Lambda for LEXA dialog positive button callback | SRC MainActivityHelper.java:249 (onPositive lambda) |
| MainActivityHelper.lambda$guideDialogForLEXA$5 | REACHABLE | | Lambda for LEXA dialog negative button callback | SRC MainActivityHelper.java:250 (onNegative lambda) |
| MainActivityHelper.lambda$mkdir$0 | REACHABLE | | Lambda callback when folder creation dialog confirmed | SRC MainActivityHelper.java:137-140 (dialog callback lambda in mkdir) |
| MainActivityHelper.lambda$mkdir$1 | REACHABLE | | Lambda validator for folder name input | SRC MainActivityHelper.java:141-151 (validator lambda in mkdir) |
| MainActivityHelper.lambda$mkfile$2 | REACHABLE | | Lambda callback when file creation dialog confirmed | SRC MainActivityHelper.java:163-166 (dialog callback lambda in mkfile) |
| MainActivityHelper.lambda$mkfile$3 | REACHABLE | | Lambda validator for file name input | SRC MainActivityHelper.java:167-187 (validator lambda in mkfile) |
| MainActivityHelper.mk | REACHABLE | | Private helper called from mkdir and mkfile to show input dialog | SRC MainActivityHelper.java:194-204 (method), 137,163 (calls from mkdir/mkfile) |
| MainActivityHelper.mkDir | REACHABLE | | Called from lambda$mkdir$0 and MainActivity.onActivityResult | SRC MainActivityHelper.java:449-505 (method), 139,1370-1371 (calls) |
| MainActivityHelper.mkFile | REACHABLE | | Called from lambda$mkfile$2 and MainActivity.onActivityResult | SRC MainActivityHelper.java:390-447 (method), 165,1380,1559 (calls) |
| MainActivityHelper.mkdir | REACHABLE | | Called from MainActivity$FabActionListener.onActionSelected | SRC MainActivityHelper.java:136-160 (method), MainActivity.java:1947 (call from FAB) |
| MainActivityHelper.mkfile | REACHABLE | | Called from MainActivity$FabActionListener.onActionSelected | SRC MainActivityHelper.java:162-192 (method), MainActivity.java:1950 (call from FAB) |
| MainActivityHelper.parseCloudPath | REACHABLE | | Called from BottomBar.updatePath for cloud path parsing | SRC MainActivityHelper.java:555-583 (method), BottomBar.java:320 (call) |
| MainActivityHelper.parseOTGPath | REACHABLE | | Called from BottomBar.updatePath for OTG path parsing | SRC MainActivityHelper.java:549-553 (method), BottomBar.java:311 (call) |
| MainActivityHelper.parseSftpPath | REACHABLE | | Called from BottomBar.updatePath for SFTP path parsing | SRC MainActivityHelper.java:533-537 (method), BottomBar.java:305 (call) |
| MainActivityHelper.parseSmbPath | REACHABLE | | Called from BottomBar.updatePath for SMB path parsing | SRC MainActivityHelper.java:539-543 (method), BottomBar.java:308 (call) |
| MainActivityHelper.rename | REACHABLE | | Called from MainActivity.onActivityResult and MainFragment | SRC MainActivityHelper.java:260-336 (method), MainActivity.java:1375-1376,MainFragment.java:1225 (calls) |
| MainActivityHelper.search | REACHABLE | | Called from AppBar search callback in MainActivity.onCreate | SRC MainActivityHelper.java:585-622 (method), MainActivity.java:292 (call from AppBar lambda) |
| MainActivityHelper.showFailedOperationDialog | REACHABLE | | Called from MainActivity$2.onReceive and MainActivity.onActivityResult | SRC MainActivityHelper.java:88-100 (method), MainActivity.java:315,1583,1616 (calls) |
| MainActivityHelper.triggerStorageAccessFramework | REACHABLE | | Called from guideDialogForLEXA and lambda$guideDialogForLEXA$4 | SRC MainActivityHelper.java:255-258 (method), 249 (call from lambda) |
| MainActivityHelper$1.<init> | REACHABLE | | mNotificationReceiver field initialized in MainActivityHelper | SRC MainActivityHelper.java:102 (field initializer new BroadcastReceiver()) |
| MainActivityHelper$1.onReceive | REACHABLE | | Framework calls when media mounted/unmounted broadcast received | SRC MainActivityHelper.java:103-120 (onReceive method), MainActivity.java:1119 (registerReceiver) |

STATUS: DONE 23:50
