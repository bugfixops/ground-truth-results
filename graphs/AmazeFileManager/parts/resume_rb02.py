# ---- resume batch rb_02 (2024-01-19)

# CloudEntry methods - called from CloudHandler and CloudLoaderAsyncTask
# Note: CloudEntry.<init>(OpenMode,String) already labeled in graph_def.py line 7071 as CloudEntry.<init>

e('CloudHandler.updateEntry', 'CloudEntry.getId', 'CALL',
  'Gets entry ID to update database record',
  evidence='SRC database/CloudHandler.java:122')

e('CloudHandler.addEntry', 'CloudEntry.getPersistData', 'CALL',
  'Gets persist data to store in database',
  evidence='SRC database/CloudHandler.java:92,98')

e('CloudHandler.updateEntry', 'CloudEntry.getPersistData', 'CALL',
  'Gets persist data to update database record',
  evidence='SRC database/CloudHandler.java:127,133')

e('CloudHandler.addEntry', 'CloudEntry.getServiceType', 'CALL',
  'Gets service type ordinal to store in database',
  evidence='SRC database/CloudHandler.java:90')

e('CloudHandler.updateEntry', 'CloudEntry.getServiceType', 'CALL',
  'Gets service type ordinal to update database record',
  evidence='SRC database/CloudHandler.java:123')

# CloudIconDataFetcher lifecycle methods - called by Glide framework
e('CloudIconDataFetcher.loadData', 'CloudIconDataFetcher.cleanup', 'LIFECYCLE',
  'Glide framework calls cleanup after loadData completes or fails',
  evidence='INFERRED Glide DataFetcher lifecycle; SRC utils/glide/CloudIconDataFetcher.java:48-55')

e('CloudIconModelLoader.buildLoadData', 'CloudIconDataFetcher.getDataClass', 'CALL',
  'Glide queries data class for type information',
  evidence='INFERRED Glide framework queries fetcher type; SRC utils/glide/CloudIconDataFetcher.java:63-66')

e('CloudIconModelLoader.buildLoadData', 'CloudIconDataFetcher.getDataSource', 'CALL',
  'Glide queries data source for caching strategy',
  evidence='INFERRED Glide framework queries data source; SRC utils/glide/CloudIconDataFetcher.java:69-73')

e('CloudIconDataFetcher.<init>', 'CloudIconDataFetcher.loadData', 'LIFECYCLE',
  'Glide framework calls loadData to fetch image data',
  evidence='INFERRED Glide DataFetcher lifecycle; SRC utils/glide/CloudIconDataFetcher.java:35-43')

# CloudStreamServer$Response default constructor - UNREACHABLE
UNREACHABLE['CloudStreamServer$Response.<init>(CloudStreamServer)'] = (
    'no_trigger_in_app',
    'Default constructor is never called; app only uses parameterized constructor Response(status, mimeType, data)',
    'SRC utils/cloud/CloudStreamer.java:65,93,106,111 shows only new Response(status, mimeType, data) calls',
    'SOURCE'
)
