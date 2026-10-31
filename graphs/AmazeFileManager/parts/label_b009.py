# ---- Batch 009 label part (2026-10-27)

# CloudStreamSource methods
e('CloudStreamer.serve', 'CloudStreamSource.<init>', 'CALL', 'new CloudStreamSource(...)',
  evidence='SRC CloudStreamer.java:89')
e('CloudStreamSource.<init>', 'CloudStreamSource.open', 'CALL', 'implicit via stream usage',
  evidence='SRC CloudStreamSource.java:52-63')
e('CloudStreamer.serve', 'CloudStreamSource.moveTo', 'CALL', 'source.moveTo(startFrom)',
  evidence='SRC CloudStreamer.java:106')

# CloudStreamer methods
e('CloudUtil.launchCloud', 'CloudStreamer.getInstance', 'CALL', 'final CloudStreamer streamer = CloudStreamer.getInstance()',
  evidence='SRC CloudUtil.java:135')
e('CloudStreamer.getInstance', 'CloudStreamer.<init>', 'CALL', 'new CloudStreamer(PORT)',
  evidence='SRC CloudStreamer.java:37')
e('CloudUtil.launchCloud', 'CloudStreamer.setStreamSrc', 'CALL', 'streamer.setStreamSrc(...)',
  evidence='SRC CloudUtil.java:138')
e('CloudStreamServer.serve', 'CloudStreamer.serve', 'CALL', 'override dispatched by framework',
  evidence='SRC CloudStreamer.java:62')

# CloudUtil methods
e('Drawer.onItemClick', 'CloudUtil.checkToken', 'CALL', 'CloudUtil.checkToken(meta.path, mainActivity)',
  evidence='SRC Drawer.java:577')
e('LoadFilesListTask.doInBackground', 'CloudUtil.getCloudFiles', 'CALL', 'CloudUtil.getCloudFiles(...)',
  evidence='SRC LoadFilesListTask.java:458')
e('MainFragment.onItemClick', 'CloudUtil.launchCloud', 'CALL', 'CloudUtil.launchCloud(...)',
  evidence='SRC MainFragment.java:930')
e('HybridFile.listFiles', 'CloudUtil.listFiles', 'CALL', 'CloudUtil.listFiles(...)',
  evidence='SRC HybridFile.java:864')
e('CloudUtil.launchCloud', 'CloudUtil.stripPath', 'CALL', 'CloudUtil.stripPath(serviceType, ...)',
  evidence='SRC CloudUtil.java:142')

# CloudUtil inner classes (anonymous AsyncTask and Thread)
e('CloudUtil.checkToken', 'CloudUtil$1.<init>', 'CALL', 'new AsyncTask<String, Void, Boolean>()',
  evidence='SRC CloudUtil.java:174')
e('AndroidAsyncTask.execute', 'CloudUtil$1.doInBackground', 'CALL', 'framework calls doInBackground',
  evidence='SRC CloudUtil.java:179')
e('AndroidAsyncTask.onPostExecute', 'CloudUtil$1.onPostExecute', 'CALL', 'framework calls onPostExecute',
  evidence='SRC CloudUtil.java:217')
e('CloudUtil.launchCloud', 'CloudUtil$2.<init>', 'CALL', 'new Thread(() -> {...})',
  evidence='SRC CloudUtil.java:137')
e('Thread.run', 'CloudUtil$2.execute', 'CALL', 'lambda body execution',
  evidence='SRC CloudUtil.java:138')

# Coder and CoderBase
e('SevenZFile.readHeaders', 'Coder.<init>', 'CALL', 'new Coder()',
  evidence='SRC SevenZFile.java:642')
e('SevenZMethodConfiguration.validateOptions', 'CoderBase.canAcceptOptions', 'CALL', 'Coders.findByMethod(method).canAcceptOptions(options)',
  evidence='SRC SevenZMethodConfiguration.java:59')
e('SevenZFile.readStackEncodersAsCoders', 'CoderBase.getOptionsFromCoder', 'CALL', 'Coders.findByMethod(method).getOptionsFromCoder(...)',
  evidence='SRC SevenZFile.java:1033')

# UNREACHABLE entries (all batch 009 methods are reachable, none marked unreachable)
