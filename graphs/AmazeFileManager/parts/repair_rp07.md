STATUS: START 20:37

| Method | Label | Kind | Reason | Evidence |
|--------|-------|------|--------|----------|
| StreamServer$HTTPSession.<init> | REACHABLE | | | MainFragment.launchSMB -> Streamer.getInstance -> Streamer.<init> -> StreamServer.<init> creates thread that accepts sockets and constructs HTTPSession at line 179. StreamServer.java:179 |
| StreamServer$HTTPSession.decodeHeader | REACHABLE | | | HTTPSession.handleResponse calls decodeHeader(hin, pre, parms, header) at line 266. StreamServer.java:266 |
| StreamServer$HTTPSession.decodeMultipartData | REACHABLE | | | HTTPSession.handleResponse calls decodeMultipartData for POST multipart/form-data at line 320. StreamServer.java:320 |
| StreamServer$HTTPSession.decodeParms | REACHABLE | | | HTTPSession.handleResponse calls decodeParms for POST application/x-www-form-urlencoded at line 323; also called from decodeHeader for query parameters at line 363. StreamServer.java:323, 363 |
| StreamServer$HTTPSession.decodePercent | REACHABLE | | | Called from decodeHeader line 364 and decodeParms lines 526-527. StreamServer.java:364, 526-527 |
| StreamServer$HTTPSession.getBoundaryPositions | REACHABLE | | | Called from decodeMultipartData line 391. StreamServer.java:391 |
| StreamServer$HTTPSession.handleResponse | REACHABLE | | | HTTPSession.run calls handleResponse(socket) at line 229. StreamServer.java:229 |
| StreamServer$HTTPSession.run | REACHABLE | | | HTTPSession.<init> creates new Thread(this) and starts it at lines 222-224. StreamServer.java:222-224 |
| StreamServer$HTTPSession.saveTmpFile | REACHABLE | | | Called from decodeMultipartData line 436. StreamServer.java:436 |
| StreamServer$HTTPSession.sendError | REACHABLE | | | Called from handleResponse line 330, decodeHeader lines 349/353/357, decodeMultipartData lines 395/400/425/449, decodePercent line 508. StreamServer.java:330, 349, 353, 357, 395, 400, 425, 449, 508 |
| StreamServer$HTTPSession.sendResponse | REACHABLE | | | Called from handleResponse line 332 and sendError line 516. StreamServer.java:332, 516 |
| StreamServer$HTTPSession.stripMultipartHeaders | REACHABLE | | | Called from decodeMultipartData line 435. StreamServer.java:435 |
| ProcessViewerFragment.addEntry | REACHABLE | | | processResults calls addEntry at lines 199-200. ProcessViewerFragment.java:199-200 |
| ProcessViewerFragment.cancelBroadcast | REACHABLE | | | setupDrawables calls cancelBroadcast at lines 248, 260, 272, 284, 296. ProcessViewerFragment.java:248, 260, 272, 284, 296 |
| ProcessViewerFragment.chartInit | REACHABLE | | | processResults calls chartInit at line 192 when !isInitialized. ProcessViewerFragment.java:192 |
| ProcessViewerFragment.createDataSet | REACHABLE | | | addEntry calls createDataSet at line 331 if dataSet is null. ProcessViewerFragment.java:331 |
| ProcessViewerFragment.lambda$cancelBroadcast$0 | REACHABLE | | | cancelBroadcast sets mCancelButton.setOnClickListener at line 306. ProcessViewerFragment.java:306 |
| ProcessViewerFragment.onActivityCreated | REACHABLE | | | Fragment lifecycle after onCreateView. Framework calls this. ProcessViewerFragment.java:141 |
| ProcessViewerFragment.onCreateView | REACHABLE | | | Fragment lifecycle after <init>. Framework calls this. ProcessViewerFragment.java:97 |
| ProcessViewerFragment.onPause | REACHABLE | | | Fragment lifecycle. Framework calls this. ProcessViewerFragment.java:182 |
| ProcessViewerFragment.onResume | REACHABLE | | | Fragment lifecycle after onActivityCreated. Framework calls this. ProcessViewerFragment.java:165 |
| ProcessViewerFragment.processResults | REACHABLE | | | Called by CustomServiceConnection when service binding delivers progress updates. ProcessViewerFragment.java:180-215 indirect callback |
| ProcessViewerFragment.setupDrawables | REACHABLE | | | processResults calls setupDrawables at line 195 when !isInitialized. ProcessViewerFragment.java:195 |
| SmbConnectDialog.createEditTextColorStateList | REACHABLE | | | Static method setTint calls createEditTextColorStateList at line 318. SmbConnectDialog.java:318 |
| SmbConnectDialog.createSMBPath | REACHABLE | | | lambda$onCreateDialog$2 (positive button handler) calls createSMBPath at lines 267, 272. SmbConnectDialog.java:267, 272 |
| SmbConnectDialog.lambda$onCreateDialog$0 | REACHABLE | | | onCreateDialog sets help.setOnClickListener at line 168. SmbConnectDialog.java:168 |
| SmbConnectDialog.lambda$onCreateDialog$1 | REACHABLE | | | onCreateDialog sets ch.setOnClickListener at line 173. SmbConnectDialog.java:173 |
| SmbConnectDialog.lambda$onCreateDialog$2 | REACHABLE | | | onCreateDialog sets ba3.onPositive callback at line 235. SmbConnectDialog.java:235 |
| SmbConnectDialog.lambda$onCreateDialog$3 | REACHABLE | | | onCreateDialog sets ba3.onNegative callback at line 279. SmbConnectDialog.java:279 |
| SmbConnectDialog.lambda$onCreateDialog$4 | REACHABLE | | | onCreateDialog sets ba3.onNeutral callback at line 286. SmbConnectDialog.java:286 |
| SmbConnectDialog.onCreate | REACHABLE | | | DialogFragment lifecycle after <init>. Framework calls this. SmbConnectDialog.java:92 |
| SmbConnectDialog.onCreateDialog | REACHABLE | | | DialogFragment lifecycle after onCreate. Framework calls this. SmbConnectDialog.java:97 |
| SmbConnectDialog.setTint | REACHABLE | | | Static method, but onCreate already has edge to EditTextColorStateUtil.setTint which is the actual method called. The static setTint in this class (line 323) is only for API < 21 and calls createEditTextColorStateList. This is called when EditTextColorStateUtil delegates to it. SmbConnectDialog.java:323 |

STATUS: DONE 20:38
