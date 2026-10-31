# Repair batch 02 - SftpConnectDialog methods

STATUS: START 20:22

| Method | Label | Kind | Reason | Evidence |
|--------|-------|------|--------|----------|
| SftpConnectDialog.onCreate | REACHABLE | LIFECYCLE | Framework calls onCreate when DialogFragment is created | SftpConnectDialog.java:93-98, already has edges in graph_def.py |
| SftpConnectDialog.onCreateDialog | REACHABLE | LIFECYCLE | Framework calls onCreateDialog to build dialog UI | SftpConnectDialog.java:101-294, added edges for lambda registrations |
| SftpConnectDialog.lambda$onCreateDialog$9 | REACHABLE | GUI | Registered by portET.setOnFocusChangeListener in onCreateDialog | SftpConnectDialog.java:131-134 |
| SftpConnectDialog.lambda$onCreateDialog$1 | REACHABLE | GUI | Registered by selectPemBTN.setOnClickListener in onCreateDialog | SftpConnectDialog.java:139-144 |
| SftpConnectDialog.lambda$onCreateDialog$0 | REACHABLE | GUI | Registered by dialogBuilder.onPositive in onCreateDialog | SftpConnectDialog.java:157-231 |
| SftpConnectDialog.lambda$null$2 | REACHABLE | ASYNC | Callback registered by removeConnection in lambda$onCreateDialog$0 | SftpConnectDialog.java:177-199 |
| SftpConnectDialog.lambda$null$3 | REACHABLE | ASYNC | Callback registered by GetSshHostFingerprintTask in lambda$null$2 | SftpConnectDialog.java:178-198 |
| SftpConnectDialog.lambda$null$4 | REACHABLE | GUI | Registered by setPositiveButton in lambda$null$3 | SftpConnectDialog.java:191-195 |
| SftpConnectDialog.lambda$null$5 | REACHABLE | GUI | Registered by setNegativeButton in lambda$null$3 | SftpConnectDialog.java:196 |
| SftpConnectDialog.lambda$null$6 | REACHABLE | ASYNC | Callback registered by GetSshHostFingerprintTask in lambda$onCreateDialog$0 | SftpConnectDialog.java:203-230 |
| SftpConnectDialog.lambda$null$7 | REACHABLE | GUI | Registered by setPositiveButton in lambda$null$6 | SftpConnectDialog.java:217-228 |
| SftpConnectDialog.lambda$null$8 | REACHABLE | GUI | Registered by setNegativeButton in lambda$null$6 | SftpConnectDialog.java:229 |
| SftpConnectDialog.lambda$onCreateDialog$13 | REACHABLE | GUI | Registered by dialogBuilder.onNegative in onCreateDialog | SftpConnectDialog.java:232 |
| SftpConnectDialog.lambda$onCreateDialog$12 | REACHABLE | GUI | Registered by dialogBuilder.onNegative in edit mode | SftpConnectDialog.java:236-252 |
| SftpConnectDialog.lambda$null$11 | REACHABLE | ASYNC | Callback registered by AppConfig.runInBackground in lambda$onCreateDialog$12 | SftpConnectDialog.java:247-249 |
| SftpConnectDialog.lambda$onCreateDialog$10 | REACHABLE | GUI | Registered by dialogBuilder.onNeutral in edit mode | SftpConnectDialog.java:253 |
| SftpConnectDialog.onActivityResult | REACHABLE | LIFECYCLE | Framework calls onActivityResult when file picker returns | SftpConnectDialog.java:298-327 |
| SftpConnectDialog.lambda$onActivityResult$14 | REACHABLE | ASYNC | Callback registered by PemToKeyPairTask in onActivityResult | SftpConnectDialog.java:311-321 |
| SftpConnectDialog.authenticateAndSaveSetup | REACHABLE | CALL | Called from lambda$null$3, lambda$null$4, lambda$null$7 | SftpConnectDialog.java:327-394 |
| SftpConnectDialog.lambda$authenticateAndSaveSetup$15 | REACHABLE | ASYNC | Callback registered by AppConfig.runInBackground in authenticateAndSaveSetup | SftpConnectDialog.java:385-389 |
| SftpConnectDialog.getPemContents | REACHABLE | CALL | Called from authenticateAndSaveSetup and lambda$authenticateAndSaveSetup$15 | SftpConnectDialog.java:397-413 |

STATUS: DONE 20:22
