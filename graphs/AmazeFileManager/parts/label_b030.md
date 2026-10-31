STATUS: RUNNING 23:08

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| FtpServerFragment.<init> | REACHABLE | | Constructor called from Drawer lambda | SRC Drawer.java:405 |
| FtpServerFragment.onCreate | REACHABLE | | Fragment lifecycle after construction | SRC FtpServerFragment.java:93-98 |
| FtpServerFragment.onCreateView | REACHABLE | | Fragment lifecycle after onCreate | SRC FtpServerFragment.java:100-142 |
| FtpServerFragment.onActivityCreated | REACHABLE | | Fragment lifecycle after onCreateView | SRC FtpServerFragment.java:144-157 |
| FtpServerFragment.onResume | REACHABLE | | Fragment lifecycle after onActivityCreated | SRC FtpServerFragment.java:387-398 |
| FtpServerFragment.onPause | REACHABLE | | Fragment lifecycle when pausing | SRC FtpServerFragment.java:400-405 |
| FtpServerFragment.onCreateOptionsMenu | REACHABLE | | Framework calls after setHasOptionsMenu(true) | SRC FtpServerFragment.java:96, 317-319 |
| FtpServerFragment.onOptionsItemSelected | REACHABLE | | Framework calls on menu item selection | SRC FtpServerFragment.java:159-308 |
| FtpServerFragment.updateSpans | REACHABLE | | Called from onCreateView and onFtpReceiveActions | SRC FtpServerFragment.java:119, 345, 465-489 |
| FtpServerFragment.updateStatus | REACHABLE | | Called from onCreateView | SRC FtpServerFragment.java:120, 406-463 |
| FtpServerFragment.startServer | REACHABLE | | Called from button click lambda | SRC FtpServerFragment.java:132, 375-377 |
| FtpServerFragment.stopServer | REACHABLE | | Called from button click lambda | SRC FtpServerFragment.java:139, 333, 382-384 |
| FtpServerFragment.lambda$onCreateView$0 | REACHABLE | | Button click listener registered in onCreateView | SRC FtpServerFragment.java:127 |
| FtpServerFragment.getDefaultPortFromPreferences | REACHABLE | | Called from onOptionsItemSelected and others | SRC FtpServerFragment.java:172, 457, 534, 537-539 |
| FtpServerFragment.changeFTPServerPort | REACHABLE | | Called from dialog lambda | SRC FtpServerFragment.java:182, 570-578 |
| FtpServerFragment.lambda$onOptionsItemSelected$1 | REACHABLE | | MaterialDialog onPositive callback for port | SRC FtpServerFragment.java:176 |
| FtpServerFragment.getDefaultPathFromPreferences | REACHABLE | | Called from onOptionsItemSelected and updateStatus | SRC FtpServerFragment.java:202, 459, 564-568 |
| FtpServerFragment.changeFTPServerPath | REACHABLE | | Called from dialog lambda | SRC FtpServerFragment.java:210, 221, 580-586 |
| FtpServerFragment.lambda$onOptionsItemSelected$2 | REACHABLE | | MaterialDialog onPositive callback for path | SRC FtpServerFragment.java:204 |
| FtpServerFragment.lambda$onOptionsItemSelected$3 | REACHABLE | | MaterialDialog input callback for path | SRC FtpServerFragment.java:203 |
| FtpServerFragment.initLoginDialogViews | REACHABLE | | Called from onOptionsItemSelected | SRC FtpServerFragment.java:226, 492-527 |
| FtpServerFragment.setFTPUsername | REACHABLE | | Called from dialog lambda | SRC FtpServerFragment.java:254, 267, 588-591 |
| FtpServerFragment.setFTPPassword | REACHABLE | | Called from dialog lambda | SRC FtpServerFragment.java:255, 268, 593-602 |
| FtpServerFragment.lambda$onOptionsItemSelected$4 | REACHABLE | | MaterialDialog onPositive callback for login | SRC FtpServerFragment.java:250 |
| FtpServerFragment.setSecurePreference | REACHABLE | | Called from dialog lambda | SRC FtpServerFragment.java:273, 274, 619-621 |
| FtpServerFragment.getFTPTimeout | REACHABLE | | Called from onOptionsItemSelected | SRC FtpServerFragment.java:288, 607-609 |
| FtpServerFragment.setFTPTimeout | REACHABLE | | Called from dialog lambda | SRC FtpServerFragment.java:299, 301, 611-613 |
| FtpServerFragment.lambda$onOptionsItemSelected$5 | REACHABLE | | MaterialDialog input callback for timeout | SRC FtpServerFragment.java:289 |
| FtpServerFragment.lambda$onOptionsItemSelected$6 | REACHABLE | | MaterialDialog input callback alternate branch | SRC FtpServerFragment.java:289 |
| FtpServerFragment.onFtpReceiveActions | REACHABLE | | EventBus @Subscribe callback after registration | SRC FtpServerFragment.java:397, 343-363 |
| FtpServerFragment.getUsernameFromPreferences | REACHABLE | | Called from initLoginDialogViews and updateStatus | SRC FtpServerFragment.java:432, 512, 516, 541-543 |
| FtpServerFragment.getPasswordFromPreferences | REACHABLE | | Called from initLoginDialogViews and updateStatus | SRC FtpServerFragment.java:429, 517, 545-562 |
| FtpServerFragment.getSecurePreference | REACHABLE | | Called from initLoginDialogViews and others | SRC FtpServerFragment.java:348, 520, 533, 615-617 |
| FtpServerFragment.lambda$initLoginDialogViews$8 | REACHABLE | | Anonymous checkbox OnCheckedChangeListener | SRC FtpServerFragment.java:499 |
| FtpServerFragment.getFTPAddressString | REACHABLE | | Called from updateSpans | SRC FtpServerFragment.java:466, 529-535 |
| FtpServerFragment.lambda$updateStatus$7 | REACHABLE | | Password visibility button click listener | SRC FtpServerFragment.java:442 |
| FtpServerFragment$1.<init> | REACHABLE | | BroadcastReceiver field initialized | SRC FtpServerFragment.java:321 |
| FtpServerFragment$1.onReceive | REACHABLE | | System delivers CONNECTIVITY_ACTION broadcast | SRC FtpServerFragment.java:395, 324-340 |

STATUS: DONE 23:13
