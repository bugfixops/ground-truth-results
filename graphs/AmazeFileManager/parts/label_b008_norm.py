# ---- Batch 008 label part (2026-10-27)

# CloudIconModelFactory methods
e('CloudIconModelFactory.<init>', 'CloudIconModelLoader.<init>', 'EXPLICIT', 'Glide factory creates loader',
  evidence='SRC CloudIconModelFactory.java:18-20')
e('CloudIconModelFactory.build', 'CloudIconModelLoader.<init>', 'EXPLICIT', 'Factory builds CloudIconModelLoader',
  evidence='SRC CloudIconModelFactory.java:23-26')

# CloudIconModelLoader methods
e('CloudIconModelLoader.buildLoadData', 'CloudIconDataFetcher.<init>', 'EXPLICIT', 'Creates fetcher for image loading',
  evidence='SRC CloudIconModelLoader.java:25-31')

# CloudPluginException - thrown from multiple call sites
e('CloudHandler.addEntry', 'CloudPluginException.<init>', 'EXPLICIT', 'Throws when cloud provider unavailable',
  evidence='SRC CloudHandler.java:85-86')
e('CloudHandler.updateEntry', 'CloudPluginException.<init>', 'EXPLICIT', 'Throws when cloud provider unavailable',
  evidence='SRC CloudHandler.java:118-121')
e('CloudHandler.findEntry', 'CloudPluginException.<init>', 'EXPLICIT', 'Throws when cloud provider unavailable',
  evidence='SRC CloudHandler.java:141-144')
e('CloudHandler.getAllEntries', 'CloudPluginException.<init>', 'EXPLICIT', 'Throws when cloud provider unavailable',
  evidence='SRC CloudHandler.java:169-172')
e('CloudUtil.listFiles', 'CloudPluginException.<init>', 'EXPLICIT', 'Throws when cloud provider unavailable',
  evidence='SRC CloudUtil.java:59-82')
e('LoadFilesListTask.loadCloudFiles', 'CloudPluginException.<init>', 'EXPLICIT', 'Throws when cloud provider unavailable',
  evidence='SRC LoadFilesListTask.java:453-455')

# CloudSheetFragment - shown from MainActivity
e('MainActivity.onOptionsItemSelected', 'CloudSheetFragment.<init>', 'EXPLICIT', 'Creates cloud sheet dialog fragment',
  evidence='SRC MainActivity.java:1953')
e('CloudSheetFragment.<init>', 'CloudSheetFragment.onCreate', 'LIFECYCLE', 'Android framework calls onCreate on fragment creation',
  evidence='SRC CloudSheetFragment.java:40-41')
e('CloudSheetFragment.<init>', 'CloudSheetFragment.setupDialog', 'LIFECYCLE', 'Android framework calls setupDialog during dialog setup',
  evidence='SRC CloudSheetFragment.java:45-87')
e('CloudSheetFragment.setupDialog', 'CloudSheetFragment.onClick', 'EXPLICIT', 'Sets onClick listener on layouts',
  evidence='SRC CloudSheetFragment.java:70-76')
e('CloudSheetFragment.setupDialog', 'CloudSheetFragment.isCloudProviderAvailable', 'EXPLICIT', 'Checks cloud provider availability',
  evidence='SRC CloudSheetFragment.java:69')

# CloudStreamServer - instantiated via CloudStreamer.getInstance()
e('CloudUtil.playStream', 'CloudStreamer.getInstance', 'EXPLICIT', 'Gets streamer instance',
  evidence='SRC CloudUtil.java:135')
e('SshClientUtils.playStream', 'CloudStreamer.getInstance', 'EXPLICIT', 'Gets streamer instance',
  evidence='SRC SshClientUtils.java:238')
e('StreamServer.tryBind', 'CloudStreamer.getInstance', 'EXPLICIT', 'Stops conflicting streamer',
  evidence='SRC StreamServer.java:212')
e('CloudStreamer.getInstance', 'CloudStreamServer.<init>', 'EXPLICIT', 'Creates new CloudStreamer (extends CloudStreamServer)',
  evidence='SRC CloudStreamer.java:34-39')
e('CloudStreamServer.<init>', 'CloudStreamServer.lambda$new$0', 'SYSTEM', 'Creates server thread with lambda',
  evidence='SRC CloudStreamServer.java:204-220')
e('CloudStreamServer.lambda$new$0', 'CloudStreamServer$HTTPSession.<init>', 'EXPLICIT', 'Accepts client socket and creates HTTPSession',
  evidence='SRC CloudStreamServer.java:217-218')
e('CloudStreamer.__init__', 'CloudStreamServer.<init>', 'EXPLICIT', 'Calls super constructor with port and file',
  evidence='SRC CloudStreamer.java:31, CloudStreamServer.java:199-201')

# HTTPSession - created per client connection
e('CloudStreamServer$HTTPSession.<init>', 'CloudStreamServer$HTTPSession.run', 'LIFECYCLE', 'Creates thread and calls run',
  evidence='SRC CloudStreamServer.java:330-338')
e('CloudStreamServer$HTTPSession.run', 'CloudStreamServer$HTTPSession.handleResponse', 'EXPLICIT', 'HTTPSession.run calls handleResponse',
  evidence='SRC CloudStreamServer.java:358-361')
e('CloudStreamServer$HTTPSession.handleResponse', 'CloudStreamServer$HTTPSession.decodeHeader', 'EXPLICIT', 'Parses HTTP headers',
  evidence='SRC CloudStreamServer.java:385')
e('CloudStreamServer$HTTPSession.handleResponse', 'CloudStreamServer$HTTPSession.sendError', 'EXPLICIT', 'Sends error on invalid request',
  evidence='SRC CloudStreamServer.java:389, 398, 402')
e('CloudStreamServer$HTTPSession.handleResponse', 'CloudStreamServer$HTTPSession.decodeParms', 'EXPLICIT', 'Decodes URI parameters',
  evidence='SRC CloudStreamServer.java:473-475')
e('CloudStreamServer$HTTPSession.handleResponse', 'CloudStreamServer$HTTPSession.decodeMultipartData', 'EXPLICIT', 'Processes multipart form data',
  evidence='SRC CloudStreamServer.java:480-481')
e('CloudStreamServer$HTTPSession.handleResponse', 'CloudStreamServer$HTTPSession.sendResponse', 'EXPLICIT', 'Sends HTTP response',
  evidence='SRC CloudStreamServer.java:512-514')
e('CloudStreamServer$HTTPSession.decodeHeader', 'CloudStreamServer$HTTPSession.decodePercent', 'EXPLICIT', 'Decodes URI percent encoding',
  evidence='SRC CloudStreamServer.java:508')
e('CloudStreamServer$HTTPSession.decodeMultipartData', 'CloudStreamServer$HTTPSession.getBoundaryPositions', 'EXPLICIT', 'Finds multipart boundaries',
  evidence='SRC CloudStreamServer.java:598')
e('CloudStreamServer$HTTPSession.decodeMultipartData', 'CloudStreamServer$HTTPSession.saveTmpFile', 'EXPLICIT', 'Saves uploaded file',
  evidence='SRC CloudStreamServer.java:608')
e('CloudStreamServer$HTTPSession.decodeMultipartData', 'CloudStreamServer$HTTPSession.stripMultipartHeaders', 'EXPLICIT', 'Processes multipart headers',
  evidence='SRC CloudStreamServer.java:607')
e('CloudStreamServer$HTTPSession.decodeMultipartData', 'CloudStreamServer$HTTPSession.sendError', 'EXPLICIT', 'Sends error on parse failure',
  evidence='SRC CloudStreamServer.java:597, 601, 605')
e('CloudStreamServer$HTTPSession.handleResponse', 'CloudStreamServer.serve', 'EXPLICIT', 'Calls abstract serve method (overridden in CloudStreamer)',
  evidence='SRC CloudStreamServer.java:511')

# Response - created and returned by serve methods
e('CloudStreamer.serve', 'CloudStreamServer$Response.<init>', 'EXPLICIT', 'Creates response with error status',
  evidence='SRC CloudStreamer.java:65')
e('CloudStreamer.serve', 'CloudStreamServer$Response.<init>', 'EXPLICIT', 'Creates response with range not satisfiable',
  evidence='SRC CloudStreamer.java:93')
e('CloudStreamer.serve', 'CloudStreamServer$Response.<init>', 'EXPLICIT', 'Creates response with partial content',
  evidence='SRC CloudStreamer.java:106')
e('CloudStreamer.serve', 'CloudStreamServer$Response.<init>', 'EXPLICIT', 'Creates response with OK status',
  evidence='SRC CloudStreamer.java:111')
e('CloudStreamServer$Response.<init>', 'CloudStreamServer$Response.addHeader', 'EXPLICIT', 'Response constructor allows adding headers',
  evidence='SRC CloudStreamer.java:97, 107, 112, 114')

# CloudStreamServer stop
e('CloudStreamer.stop', 'CloudStreamServer.stop', 'EXPLICIT', 'Calls parent stop method',
  evidence='SRC CloudStreamer.java:52-55')
e('CloudStreamServer.stop', 'CloudStreamServer.tryBind', 'EXPLICIT', 'tryBind stops Streamer if port occupied',
  evidence='SRC CloudStreamServer.java:199-201, 226-228')

# No UNREACHABLE entries for this batch - all methods are reachable
