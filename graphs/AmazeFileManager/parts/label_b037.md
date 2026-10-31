STATUS: RUNNING 23:28

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| GlideRequests.<init> | UNREACHABLE | no_trigger_in_app | Generated Glide class constructor, not directly instantiated by app code. GlideApp.with() is the entry point | INFERRED: GlideRequests is generated class, grep shows no direct instantiation |
| GlideRequests.addDefaultRequestListener | UNREACHABLE | no_trigger_in_app | Generated method not called by app | INFERRED: grep shows no usage in app code |
| GlideRequests.applyDefaultRequestOptions | UNREACHABLE | no_trigger_in_app | Generated method not called by app | INFERRED: grep shows no usage in app code |
| GlideRequests.as | UNREACHABLE | no_trigger_in_app | Generated method not called by app | INFERRED: grep shows no usage in app code |
| GlideRequests.asBitmap | UNREACHABLE | no_trigger_in_app | Generated method not called by app | INFERRED: grep shows no usage in app code |
| GlideRequests.asDrawable | UNREACHABLE | no_trigger_in_app | Generated method not called by app. App uses GlideApp.with().asDrawable() which calls GlideRequests.asDrawable() but through GlideApp wrapper | INFERRED: GlideApp.with() returns GlideRequests but calls go through GlideApp generated code |
| GlideRequests.asFile | UNREACHABLE | no_trigger_in_app | Generated method not called by app | INFERRED: grep shows no usage in app code |
| GlideRequests.asGif | UNREACHABLE | no_trigger_in_app | Generated method not called by app | INFERRED: grep shows no usage in app code |
| GlideRequests.download | UNREACHABLE | no_trigger_in_app | Generated method not called by app | INFERRED: grep shows no usage in app code |
| GlideRequests.downloadOnly | UNREACHABLE | no_trigger_in_app | Generated method not called by app | INFERRED: grep shows no usage in app code |
| GlideRequests.load(various) | UNREACHABLE | no_trigger_in_app | Generated method not called by app. App uses GlideApp.with().load() which may internally delegate to GlideRequests but not directly | INFERRED: all .load() calls are on GlideApp not GlideRequests |
| GlideRequests.setDefaultRequestOptions | UNREACHABLE | no_trigger_in_app | Generated method not called by app | INFERRED: grep shows no usage in app code |
| GlideRequests.setRequestOptions | UNREACHABLE | no_trigger_in_app | Generated method not called by app | INFERRED: grep shows no usage in app code |
| GzipDecompressor.<init> | REACHABLE | | Called from CompressedHelper.getCompressorInstance when file type is gzipped tar | SRC filesystem/compressed/CompressedHelper.java:118 |
| GzipDecompressor.changePath | REACHABLE | | Creates GzipHelperTask to load compressed file contents | SRC filesystem/compressed/showcontents/helpers/GzipDecompressor.java:46 |
| GzipExtractor.<init> | REACHABLE | | Called from CompressedHelper.getExtractorInstance when extracting gzipped tar files | SRC filesystem/compressed/CompressedHelper.java:88 |
| GzipExtractor.extractEntry | REACHABLE | | Called from GzipExtractor.extractWithFilter to extract individual tar entries | SRC filesystem/compressed/extractcontents/helpers/GzipExtractor.java:81,89 |
| GzipExtractor.extractWithFilter | REACHABLE | | Overrides Extractor.extractWithFilter, called by extraction framework | SRC filesystem/compressed/extractcontents/helpers/GzipExtractor.java:52 |
| GzipHelperTask.<init> | REACHABLE | | Instantiated by GzipDecompressor.changePath | SRC filesystem/compressed/showcontents/helpers/GzipDecompressor.java:46 |
| GzipHelperTask.addElements | REACHABLE | | Called from parent CompressedHelperTask.doInBackground | SRC asynchronous/asynctasks/compress/GzipHelperTask.java:61 |
| HiddenAdapter.<init> | REACHABLE | | Instantiated in GeneralDialogCreation.showHistoryDialog and showHiddenDialog | SRC ui/dialogs/GeneralDialogCreation.java:1097,1119 |
| HiddenAdapter.getItemCount | REACHABLE | | RecyclerView.Adapter lifecycle method | SRC adapters/HiddenAdapter.java:133 |
| HiddenAdapter.getItemId | REACHABLE | | RecyclerView.Adapter lifecycle method | SRC adapters/HiddenAdapter.java:128 |
| HiddenAdapter.lambda$null$1 | REACHABLE | | Nested lambda in row click handler | SRC adapters/HiddenAdapter.java:101-116 |
| HiddenAdapter.lambda$null$2 | REACHABLE | | Nested lambda in row click handler | SRC adapters/HiddenAdapter.java:101-116 |
| HiddenAdapter.lambda$null$3 | REACHABLE | | Nested lambda in row click handler | SRC adapters/HiddenAdapter.java:101-116 |
| HiddenAdapter.lambda$onBindViewHolder$0 | REACHABLE | | Lambda for deleteButton click listener | SRC adapters/HiddenAdapter.java:78 |
| HiddenAdapter.lambda$onBindViewHolder$4 | REACHABLE | | Lambda for row click listener | SRC adapters/HiddenAdapter.java:99 |
| HiddenAdapter.onBindViewHolder | REACHABLE | | RecyclerView.Adapter lifecycle method | SRC adapters/HiddenAdapter.java:69 |
| HiddenAdapter.onCreateViewHolder | REACHABLE | | RecyclerView.Adapter lifecycle method | SRC adapters/HiddenAdapter.java:59 |
| HiddenAdapter.updateDialog | REACHABLE | | Called after adapter creation in GeneralDialogCreation | SRC adapters/HiddenAdapter.java:123 |
| HiddenViewHolder.<init> | REACHABLE | | Instantiated by HiddenAdapter.onCreateViewHolder | SRC adapters/holders/HiddenViewHolder.java:25 |

STATUS: DONE 23:32
