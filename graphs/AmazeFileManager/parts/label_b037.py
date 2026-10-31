# ---- Helper batch_037 label part (2025-01-10)

# GlideRequests - GENERATED Glide class
# All methods are UNREACHABLE unless specifically called by app code

# GzipDecompressor
e('CompressedHelper.getCompressorInstance', 'GzipDecompressor.<init>', 'CALL',
  'Instantiation when file type is gzipped tar',
  evidence='SRC filesystem/compressed/CompressedHelper.java:118')

e('GzipDecompressor.changePath', 'GzipHelperTask.<init>', 'CALL',
  'Creates GzipHelperTask to load compressed file contents',
  evidence='SRC filesystem/compressed/showcontents/helpers/GzipDecompressor.java:46')

e('GzipHelperTask.<init>', 'GzipHelperTask.addElements', 'LIFECYCLE',
  'CompressedHelperTask.doInBackground calls abstract addElements',
  evidence='SRC asynchronous/asynctasks/compress/CompressedHelperTask.java:55')

# GzipExtractor
e('CompressedHelper.getExtractorInstance', 'GzipExtractor.<init>', 'CALL',
  'Instantiation when extracting gzipped tar files',
  evidence='SRC filesystem/compressed/CompressedHelper.java:88')

e('GzipExtractor.<init>', 'GzipExtractor.extractWithFilter', 'LIFECYCLE',
  'Extractor.extractEntries or extractEverything calls abstract extractWithFilter',
  evidence='SRC filesystem/compressed/extractcontents/Extractor.java:57,73')

e('GzipExtractor.extractWithFilter', 'GzipExtractor.extractEntry', 'CALL',
  'Extracts individual tar entries from gzip stream',
  evidence='SRC filesystem/compressed/extractcontents/helpers/GzipExtractor.java:81')

# GzipHelperTask methods routed via parent

# HiddenAdapter
e('GeneralDialogCreation.showHistoryDialog', 'HiddenAdapter.<init>', 'CALL',
  'Adapter created for history dialog',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:1097')

e('GeneralDialogCreation.showHiddenDialog', 'HiddenAdapter.<init>', 'CALL',
  'Adapter created for hidden files dialog',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:1119')

# HiddenAdapter RecyclerView.Adapter lifecycle methods
e('HiddenAdapter.<init>', 'HiddenAdapter.onCreateViewHolder', 'LIFECYCLE',
  'Framework calls onCreateViewHolder when RecyclerView needs new view',
  evidence='INFERRED: RecyclerView.Adapter lifecycle callback, source not read')

e('HiddenAdapter.<init>', 'HiddenAdapter.onBindViewHolder', 'LIFECYCLE',
  'Framework calls onBindViewHolder when RecyclerView binds data to view',
  evidence='INFERRED: RecyclerView.Adapter lifecycle callback, source not read')

e('HiddenAdapter.<init>', 'HiddenAdapter.getItemCount', 'LIFECYCLE',
  'Framework calls getItemCount to determine adapter size',
  evidence='INFERRED: RecyclerView.Adapter lifecycle callback, source not read')

e('HiddenAdapter.<init>', 'HiddenAdapter.getItemId', 'LIFECYCLE',
  'Framework calls getItemId for item identification',
  evidence='INFERRED: RecyclerView.Adapter lifecycle callback, source not read')

e('HiddenAdapter.onCreateViewHolder', 'HiddenViewHolder.<init>', 'CALL',
  'ViewHolder instantiated when RecyclerView needs new view',
  evidence='SRC adapters/HiddenAdapter.java:64')

e('HiddenAdapter.onBindViewHolder', 'HiddenAdapter.lambda$onBindViewHolder$0', 'GUI',
  'Lambda for deleteButton click listener',
  evidence='SRC adapters/HiddenAdapter.java:78')

e('HiddenAdapter.onBindViewHolder', 'HiddenAdapter.lambda$onBindViewHolder$4', 'GUI',
  'Lambda for row click listener',
  evidence='SRC adapters/HiddenAdapter.java:99')

# Nested lambdas inside lambda$onBindViewHolder$4 (row click handler)
# The exact assignment of lambda$null$N to specific lines requires bytecode analysis
# But all three are called from the row handler: Thread runnable and runOnUiThread calls
e('HiddenAdapter.lambda$onBindViewHolder$4', 'HiddenAdapter.lambda$null$1', 'ASYNC',
  'Nested lambda in row handler - Thread runnable or runOnUiThread call',
  evidence='SRC adapters/HiddenAdapter.java:101-116 contains Thread and runOnUiThread lambdas')

e('HiddenAdapter.lambda$onBindViewHolder$4', 'HiddenAdapter.lambda$null$2', 'ASYNC',
  'Nested lambda in row handler - Thread runnable or runOnUiThread call',
  evidence='SRC adapters/HiddenAdapter.java:101-116 contains Thread and runOnUiThread lambdas')

e('HiddenAdapter.lambda$onBindViewHolder$4', 'HiddenAdapter.lambda$null$3', 'ASYNC',
  'Nested lambda in row handler - Thread runnable or runOnUiThread call',
  evidence='SRC adapters/HiddenAdapter.java:101-116 contains Thread and runOnUiThread lambdas')

# UNREACHABLE methods from this batch (generated Glide class - methods not called by app)
UNREACHABLE['GlideRequests.<init>'] = ('no_trigger_in_app', 'Generated Glide class constructor, not directly instantiated by app code. GlideApp.with() is the entry point', 'INFERRED: GlideRequests is generated class, grep shows no direct instantiation', 'INFERRED')
UNREACHABLE['GlideRequests.addDefaultRequestListener'] = ('no_trigger_in_app', 'Generated method not called by app', 'INFERRED: grep shows no usage in app code', 'INFERRED')
UNREACHABLE['GlideRequests.applyDefaultRequestOptions'] = ('no_trigger_in_app', 'Generated method not called by app', 'INFERRED: grep shows no usage in app code', 'INFERRED')
UNREACHABLE['GlideRequests.as'] = ('no_trigger_in_app', 'Generated method not called by app', 'INFERRED: grep shows no usage in app code', 'INFERRED')
UNREACHABLE['GlideRequests.asBitmap'] = ('no_trigger_in_app', 'Generated method not called by app', 'INFERRED: grep shows no usage in app code', 'INFERRED')
UNREACHABLE['GlideRequests.asDrawable'] = ('no_trigger_in_app', 'Generated method not called by app. App uses GlideApp.with().asDrawable() which calls GlideRequests.asDrawable() but through GlideApp wrapper', 'INFERRED: GlideApp.with() returns GlideRequests but calls go through GlideApp generated code', 'INFERRED')
UNREACHABLE['GlideRequests.asFile'] = ('no_trigger_in_app', 'Generated method not called by app', 'INFERRED: grep shows no usage in app code', 'INFERRED')
UNREACHABLE['GlideRequests.asGif'] = ('no_trigger_in_app', 'Generated method not called by app', 'INFERRED: grep shows no usage in app code', 'INFERRED')
UNREACHABLE['GlideRequests.download'] = ('no_trigger_in_app', 'Generated method not called by app', 'INFERRED: grep shows no usage in app code', 'INFERRED')
UNREACHABLE['GlideRequests.downloadOnly'] = ('no_trigger_in_app', 'Generated method not called by app', 'INFERRED: grep shows no usage in app code', 'INFERRED')
UNREACHABLE['GlideRequests.load(Landroid/graphics/Bitmap;)Lcom/amaze/filemanager/GlideRequest;'] = ('no_trigger_in_app', 'Generated method not called by app. App uses GlideApp.with().load() which may internally delegate to GlideRequests but not directly', 'INFERRED: all .load() calls are on GlideApp not GlideRequests', 'INFERRED')
UNREACHABLE['GlideRequests.load(Landroid/graphics/drawable/Drawable;)Lcom/amaze/filemanager/GlideRequest;'] = ('no_trigger_in_app', 'Generated method not called by app. App uses GlideApp.with().load() which may internally delegate to GlideRequests but not directly', 'INFERRED: all .load() calls are on GlideApp not GlideRequests', 'INFERRED')
UNREACHABLE['GlideRequests.load(Landroid/net/Uri;)Lcom/amaze/filemanager/GlideRequest;'] = ('no_trigger_in_app', 'Generated method not called by app. App uses GlideApp.with().load() which may internally delegate to GlideRequests but not directly', 'INFERRED: all .load() calls are on GlideApp not GlideRequests', 'INFERRED')
UNREACHABLE['GlideRequests.load(Ljava/io/File;)Lcom/amaze/filemanager/GlideRequest;'] = ('no_trigger_in_app', 'Generated method not called by app. App uses GlideApp.with().load() which may internally delegate to GlideRequests but not directly', 'INFERRED: all .load() calls are on GlideApp not GlideRequests', 'INFERRED')
UNREACHABLE['GlideRequests.load(Ljava/lang/Integer;)Lcom/amaze/filemanager/GlideRequest;'] = ('no_trigger_in_app', 'Generated method not called by app. App uses GlideApp.with().load() which may internally delegate to GlideRequests but not directly', 'INFERRED: all .load() calls are on GlideApp not GlideRequests', 'INFERRED')
UNREACHABLE['GlideRequests.load(Ljava/lang/Object;)Lcom/amaze/filemanager/GlideRequest;'] = ('no_trigger_in_app', 'Generated method not called by app. App uses GlideApp.with().load() which may internally delegate to GlideRequests but not directly', 'INFERRED: all .load() calls are on GlideApp not GlideRequests', 'INFERRED')
UNREACHABLE['GlideRequests.load(Ljava/lang/String;)Lcom/amaze/filemanager/GlideRequest;'] = ('no_trigger_in_app', 'Generated method not called by app. App uses GlideApp.with().load() which may internally delegate to GlideRequests but not directly', 'INFERRED: all .load() calls are on GlideApp not GlideRequests', 'INFERRED')
UNREACHABLE['GlideRequests.load(Ljava/net/URL;)Lcom/amaze/filemanager/GlideRequest;'] = ('no_trigger_in_app', 'Generated method not called by app. App uses GlideApp.with().load() which may internally delegate to GlideRequests but not directly', 'INFERRED: all .load() calls are on GlideApp not GlideRequests', 'INFERRED')
UNREACHABLE['GlideRequests.load([B)Lcom/amaze/filemanager/GlideRequest;'] = ('no_trigger_in_app', 'Generated method not called by app. App uses GlideApp.with().load() which may internally delegate to GlideRequests but not directly', 'INFERRED: all .load() calls are on GlideApp not GlideRequests', 'INFERRED')
UNREACHABLE['GlideRequests.setDefaultRequestOptions'] = ('no_trigger_in_app', 'Generated method not called by app', 'INFERRED: grep shows no usage in app code', 'INFERRED')
UNREACHABLE['GlideRequests.setRequestOptions'] = ('no_trigger_in_app', 'Generated method not called by app', 'INFERRED: grep shows no usage in app code', 'INFERRED')
