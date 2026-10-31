# ---- resume_rb03 part (2026-10-28 18:34)
# Batch rb_03: NEW labels for CloudStreamServer, CloudStreamSource, CloudStreamer, CloudUtil, CoderBase methods
# Note: method_list.json uses signatures like <init>(File), but graph_def.py uses short names like <init>

# CloudStreamServer.<init> creates lambda$new$1 (from second constructor)
e('CloudStreamServer.<init>', 'CloudStreamServer.lambda$new$1', 'ASYNC', 'Constructor creates Thread with lambda',
  evidence='SRC CloudStreamServer.java:231-246 (second constructor)')

# Static initializers
e('CloudStreamServer', 'CloudStreamServer.<clinit>', 'LIFECYCLE', 'Static block initializes gmtFrmt when class loads',
  evidence='SRC CloudStreamServer.java:1127-1131')

e('CloudStreamer', 'CloudStreamer.<clinit>', 'LIFECYCLE', 'Static block initializes pattern when class loads',
  evidence='SRC CloudStreamer.java:25')

# CloudStreamSource methods
e('CloudStreamServer.sendResponse', 'CloudStreamSource.close', 'CALL', 'sendResponse closes stream',
  evidence='SRC CloudStreamServer.java:849')

e('CloudStreamServer.sendResponse', 'CloudStreamSource.read', 'CALL', 'sendResponse reads from stream',
  evidence='SRC CloudStreamServer.java:841')

e('CloudStreamSource.read', 'CloudStreamSource.getCurrentPosition', 'CALL', 'read tracks position',
  evidence='SRC CloudStreamSource.java:73, 96-98')

e('CloudStreamSource.<init>', 'CloudStreamSource.getName', 'CALL', 'constructor sets name',
  evidence='SRC CloudStreamSource.java:23, 84-86')

# CloudStreamer.isStreamMedia
e('SmbFile', 'CloudStreamer.isStreamMedia', 'CALL', 'checks if file is streamable',
  evidence='SRC CloudStreamer.java:43-45')

# CloudUtil methods
e('CloudIconDataFetcher.loadData', 'CloudUtil.getThumbnailInputStreamForCloud', 'CALL', 'Glide data fetcher loads cloud thumbnails',
  evidence='SRC CloudIconDataFetcher.java:37')

e('CloudUtil.getThumbnailInputStreamForCloud', 'CloudUtil$2$1.close', 'CALL', 'creates anonymous RemoteFileInputStream with close override',
  evidence='SRC CloudUtil.java:268-277')

e('CloudUtil.launchCloud', 'CloudUtil.lambda$null$0', 'ASYNC', 'creates background thread',
  evidence='SRC CloudUtil.java:136')

e('CloudUtil.launchCloud', 'CloudUtil.lambda$launchCloud$1', 'ASYNC', 'creates UI thread lambda',
  evidence='SRC CloudUtil.java:139')

# CoderBase - library methods
e('Coders.addEncoder', 'CoderBase.encode', 'CALL', 'calls encode via virtual dispatch',
  evidence='INFERRED commons_compress_7z library')

e('Coders.addEncoder', 'CoderBase.getOptionsAsProperties', 'CALL', 'gets encoder options',
  evidence='INFERRED commons_compress_7z library')

# UNREACHABLE entries
UNREACHABLE['CloudStreamServer.encodeUri'] = ('no_trigger_in_app', 'Private method only in commented code', 'SRC CloudStreamServer.java:866-885, line 974 commented', 'SOURCE')

UNREACHABLE['CloudUtil.<init>'] = ('no_trigger_in_app', 'CloudUtil has only static methods', 'SRC CloudUtil.java:52', 'SOURCE')
