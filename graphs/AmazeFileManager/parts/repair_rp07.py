# Repair batch 07: StreamServer$HTTPSession, ProcessViewerFragment, SmbConnectDialog

# StreamServer$HTTPSession - private inner class, created when socket accepts connection
# StreamServer is abstract, extended by Streamer which is accessed via Streamer.getInstance()
# MainFragment.launchSMB calls Streamer.getInstance() -> creates server -> server thread accepts socket -> new HTTPSession(socket)

e('MainFragment.launchSMB', 'Streamer.getInstance', 'CALL', 'final Streamer s = Streamer.getInstance(); SmbStreamer/Streamer.java:57 line 1657',
  'MainFragment.java:1657')

e('Streamer.getInstance', 'Streamer.<init>', 'CALL', 'instance = new Streamer(PORT); SmbStreamer/Streamer.java:39',
  'Streamer.java:39')

e('Streamer.<init>', 'StreamServer.<init>', 'CALL', 'super(port, new File(".")); Streamer.java:34',
  'Streamer.java:34')

e('StreamServer.<init>', 'StreamServer$HTTPSession.<init>', 'ASYNC', 'new HTTPSession(accept); lambda in StreamServer constructor starts thread that accepts sockets and creates HTTPSession instances. SmbStreamer/StreamServer.java:179',
  'StreamServer.java:179')

e('StreamServer$HTTPSession.<init>', 'StreamServer$HTTPSession.run', 'ASYNC', 'Thread t = new Thread(this); t.start(); HTTPSession implements Runnable, started as new thread. SmbStreamer/StreamServer.java:222-224',
  'StreamServer.java:222-224')

e('StreamServer$HTTPSession.run', 'StreamServer$HTTPSession.handleResponse', 'CALL', 'handleResponse(socket); SmbStreamer/StreamServer.java:229',
  'StreamServer.java:229')

e('StreamServer$HTTPSession.handleResponse', 'StreamServer$HTTPSession.decodeHeader', 'CALL', 'decodeHeader(hin, pre, parms, header); SmbStreamer/StreamServer.java:266',
  'StreamServer.java:266')

e('StreamServer$HTTPSession.handleResponse', 'StreamServer$HTTPSession.decodeParms', 'CALL', 'decodeParms(postLine, parms); for POST requests with application/x-www-form-urlencoded. SmbStreamer/StreamServer.java:323',
  'StreamServer.java:323')

e('StreamServer$HTTPSession.handleResponse', 'StreamServer$HTTPSession.decodeMultipartData', 'CALL', 'decodeMultipartData(boundary, fbuf, in, parms, files); for POST with multipart/form-data. SmbStreamer/StreamServer.java:320',
  'StreamServer.java:320')

e('StreamServer$HTTPSession.handleResponse', 'StreamServer$HTTPSession.sendError', 'CALL', 'sendError(socket, HTTP_INTERNALERROR, ...); called if serve() returns null. SmbStreamer/StreamServer.java:330',
  'StreamServer.java:330')

e('StreamServer$HTTPSession.handleResponse', 'StreamServer$HTTPSession.sendResponse', 'CALL', 'sendResponse(socket, r.status, r.mimeType, r.header, r.data); sends HTTP response. SmbStreamer/StreamServer.java:332',
  'StreamServer.java:332')

e('StreamServer$HTTPSession.handleResponse', 'StreamServer.serve', 'CALL', 'Response r = serve(uri, method, header, parms, files); abstract method implemented by Streamer. SmbStreamer/StreamServer.java:327',
  'StreamServer.java:327')

e('StreamServer$HTTPSession.decodeHeader', 'StreamServer$HTTPSession.decodeParms', 'CALL', 'decodeParms(uri.substring(qmi + 1), parms); decodes query parameters from URI. SmbStreamer/StreamServer.java:363',
  'StreamServer.java:363')

e('StreamServer$HTTPSession.decodeHeader', 'StreamServer$HTTPSession.decodePercent', 'CALL', 'uri = decodePercent(uri.substring(0, qmi)); percent-decodes URI. SmbStreamer/StreamServer.java:364',
  'StreamServer.java:364')

e('StreamServer$HTTPSession.decodeHeader', 'StreamServer$HTTPSession.sendError', 'CALL', 'sendError(socket, HTTP_BADREQUEST, ...); on parse error. SmbStreamer/StreamServer.java:349, 353, 357',
  'StreamServer.java:349,353,357')

e('StreamServer$HTTPSession.decodeMultipartData', 'StreamServer$HTTPSession.getBoundaryPositions', 'CALL', 'int[] bpositions = getBoundaryPositions(fbuf, boundary.getBytes()); SmbStreamer/StreamServer.java:391',
  'StreamServer.java:391')

e('StreamServer$HTTPSession.decodeMultipartData', 'StreamServer$HTTPSession.stripMultipartHeaders', 'CALL', 'int offset = stripMultipartHeaders(fbuf, bpositions[boundarycount - 2]); SmbStreamer/StreamServer.java:435',
  'StreamServer.java:435')

e('StreamServer$HTTPSession.decodeMultipartData', 'StreamServer$HTTPSession.saveTmpFile', 'CALL', 'String path = saveTmpFile(fbuf, offset, bpositions[boundarycount - 1] - offset - 4); SmbStreamer/StreamServer.java:436',
  'StreamServer.java:436')

e('StreamServer$HTTPSession.decodeMultipartData', 'StreamServer$HTTPSession.sendError', 'CALL', 'sendError(socket, HTTP_BADREQUEST, ...); various parse errors. SmbStreamer/StreamServer.java:395, 400, 425, 449',
  'StreamServer.java:395,400,425,449')

e('StreamServer$HTTPSession.decodeParms', 'StreamServer$HTTPSession.decodePercent', 'CALL', 'p.put(decodePercent(e.substring(0, sep)).trim(), decodePercent(e.substring(sep + 1))); SmbStreamer/StreamServer.java:526-527',
  'StreamServer.java:526-527')

e('StreamServer$HTTPSession.decodePercent', 'StreamServer$HTTPSession.sendError', 'CALL', 'sendError(socket, HTTP_BADREQUEST, ...); on decode error. SmbStreamer/StreamServer.java:508',
  'StreamServer.java:508')

e('StreamServer$HTTPSession.sendError', 'StreamServer$HTTPSession.sendResponse', 'CALL', 'sendResponse(socket, status, MIME_PLAINTEXT, null, null); SmbStreamer/StreamServer.java:516',
  'StreamServer.java:516')

# ProcessViewerFragment - standard Fragment, created by MainActivity

e('MainActivity.onCreate', 'ProcessViewerFragment.<init>', 'CALL', 'transaction.replace(R.id.content_frame, new ProcessViewerFragment(), KEY_INTENT_PROCESS_VIEWER); when intent has KEY_INTENT_PROCESS_VIEWER. MainActivity.java:390',
  'MainActivity.java:390')

e('MainActivity.onServiceIntent', 'ProcessViewerFragment.<init>', 'CALL', 'transaction.replace(R.id.content_frame, new ProcessViewerFragment(), KEY_INTENT_PROCESS_VIEWER); when service starts. MainActivity.java:1590',
  'MainActivity.java:1590')

e('ProcessViewerFragment.<init>', 'ProcessViewerFragment.onCreateView', 'LIFECYCLE', 'Fragment lifecycle',
  'FW-SRC')

e('ProcessViewerFragment.onCreateView', 'ProcessViewerFragment.onActivityCreated', 'LIFECYCLE', 'Fragment lifecycle',
  'FW-SRC')

e('ProcessViewerFragment.onActivityCreated', 'ProcessViewerFragment.onResume', 'LIFECYCLE', 'Fragment lifecycle',
  'FW-SRC')

e('ProcessViewerFragment.onResume', 'ProcessViewerFragment.onPause', 'LIFECYCLE', 'Fragment lifecycle',
  'FW-SRC')

e('ProcessViewerFragment.onResume', 'ProcessViewerFragment.processResults', 'CALL', 'Called by CustomServiceConnection.onServiceConnected via serviceInstance.setProgressListener(callback). ProcessViewerFragment.java:180-215, indirect through service binding.',
  'ProcessViewerFragment.java:180-215')

e('ProcessViewerFragment.processResults', 'ProcessViewerFragment.chartInit', 'CALL', 'chartInit(total); called if !isInitialized. ProcessViewerFragment.java:192',
  'ProcessViewerFragment.java:192')

e('ProcessViewerFragment.processResults', 'ProcessViewerFragment.setupDrawables', 'CALL', 'setupDrawables(serviceType, move); called if !isInitialized. ProcessViewerFragment.java:195',
  'ProcessViewerFragment.java:195')

e('ProcessViewerFragment.processResults', 'ProcessViewerFragment.addEntry', 'CALL', 'addEntry(FileUtils.readableFileSizeFloat(doneBytes), FileUtils.readableFileSizeFloat(dataPackage.speedRaw)); ProcessViewerFragment.java:199-200',
  'ProcessViewerFragment.java:199-200')

e('ProcessViewerFragment.processResults', 'FileUtils.readableFileSizeFloat', 'CALL', 'FileUtils.readableFileSizeFloat(doneBytes) and FileUtils.readableFileSizeFloat(dataPackage.speedRaw); ProcessViewerFragment.java:199-200',
  'ProcessViewerFragment.java:199-200')

e('ProcessViewerFragment.setupDrawables', 'ProcessViewerFragment.cancelBroadcast', 'CALL', 'cancelBroadcast(new Intent(CopyService.TAG_BROADCAST_COPY_CANCEL)); and similar for other services. ProcessViewerFragment.java:248, 260, 272, 284, 296',
  'ProcessViewerFragment.java:248,260,272,284,296')

e('ProcessViewerFragment.cancelBroadcast', 'ProcessViewerFragment.lambda$cancelBroadcast$0', 'GUI', 'mCancelButton.setOnClickListener(v -> {...}); ProcessViewerFragment.java:306',
  'ProcessViewerFragment.java:306')

e('ProcessViewerFragment.addEntry', 'ProcessViewerFragment.createDataSet', 'CALL', 'dataSet = createDataSet(); if dataSet is null. ProcessViewerFragment.java:331',
  'ProcessViewerFragment.java:331')

# SmbConnectDialog - DialogFragment created by MainActivity

e('MainActivity.showSmbDialog', 'SmbConnectDialog.<init>', 'CALL', 'SmbConnectDialog smbConnectDialog = new SmbConnectDialog(); MainActivity.java:1628',
  'MainActivity.java:1628')

e('SmbConnectDialog.<init>', 'SmbConnectDialog.onCreate', 'LIFECYCLE', 'DialogFragment lifecycle',
  'FW-SRC')

e('SmbConnectDialog.onCreate', 'SmbConnectDialog.onCreateDialog', 'LIFECYCLE', 'DialogFragment lifecycle',
  'FW-SRC')

e('SmbConnectDialog.onCreate', 'EditTextColorStateUtil.setTint', 'CALL', 'EditTextColorStateUtil.setTint(context, conName, accentColor); and similar for user, pass. Note: this is in onCreateDialog, not onCreate (grep shows onCreate calls it from the already-labeled edges). SmbConnectDialog.java:164-166',
  'SmbConnectDialog.java:164-166')

e('SmbConnectDialog.onCreateDialog', 'SmbConnectDialog.lambda$onCreateDialog$0', 'GUI', 'help.setOnClickListener(v -> {...}); SmbConnectDialog.java:168',
  'SmbConnectDialog.java:168')

e('SmbConnectDialog.onCreateDialog', 'SmbConnectDialog.lambda$onCreateDialog$1', 'GUI', 'ch.setOnClickListener(view -> {...}); checkbox click listener. SmbConnectDialog.java:173',
  'SmbConnectDialog.java:173')

e('SmbConnectDialog.onCreateDialog', 'SmbConnectDialog.lambda$onCreateDialog$2', 'GUI', 'ba3.onPositive((dialog, which) -> {...}); positive button click. SmbConnectDialog.java:235',
  'SmbConnectDialog.java:235')

e('SmbConnectDialog.onCreateDialog', 'SmbConnectDialog.lambda$onCreateDialog$3', 'GUI', 'ba3.onNegative((dialog, which) -> {...}); negative button click. SmbConnectDialog.java:279',
  'SmbConnectDialog.java:279')

e('SmbConnectDialog.onCreateDialog', 'SmbConnectDialog.lambda$onCreateDialog$4', 'GUI', 'ba3.onNeutral((dialog, which) -> {...}); neutral button click. SmbConnectDialog.java:286',
  'SmbConnectDialog.java:286')

e('SmbConnectDialog.lambda$onCreateDialog$0', 'GeneralDialogCreation.showSMBHelpDialog', 'CALL', 'GeneralDialogCreation.showSMBHelpDialog(context, accentColor1); SmbConnectDialog.java:170',
  'SmbConnectDialog.java:170')

e('SmbConnectDialog.lambda$onCreateDialog$2', 'SmbConnectDialog.createSMBPath', 'CALL', 'createSMBPath(new String[]{ipa, "", "",domaind}, true) or createSMBPath(new String[]{ipa, useru, passp,domaind}, false); SmbConnectDialog.java:267, 272',
  'SmbConnectDialog.java:267,272')

e('SmbConnectDialog.lambda$onCreateDialog$2', 'SmbConnectDialog.createEditTextColorStateList', 'CALL', 'Called indirectly through setTint which is in the class but the grep shows it is already tracked through EditTextColorStateUtil.setTint from onCreate edge. Actually, looking at the source more carefully: the static setTint method at line 323 calls createEditTextColorStateList at line 318. But this is only called on API < 21. SmbConnectDialog.java:318',
  'SmbConnectDialog.java:318')

e('SmbConnectDialog.setTint', 'SmbConnectDialog.createEditTextColorStateList', 'CALL', 'ColorStateList editTextColorStateList = createEditTextColorStateList(color); SmbConnectDialog.java:318',
  'SmbConnectDialog.java:318')
