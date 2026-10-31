STATUS: RUNNING 18:33

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| CloudStreamServer.<clinit> | REACHABLE | | Static initializer creates SimpleDateFormat for HTTP headers | SRC CloudStreamServer.java:1127-1131 |
| CloudStreamServer.<init>(File) | REACHABLE | | Constructor called by CloudStreamer.<init> | SRC CloudStreamServer.java:227-250 |
| CloudStreamServer.<init>(int,File) | REACHABLE | | Constructor called by CloudStreamer.<init> via super | SRC CloudStreamServer.java:199-226 |
| CloudStreamServer.encodeUri | UNREACHABLE | no_trigger_in_app | Private method only called in commented-out serveFile code (line 974 is commented) | SRC CloudStreamServer.java:866-885 shows method body; grep -rn "encodeUri" shows only the definition and commented usage at line 974 |
| CloudStreamServer.lambda$new$0 | REACHABLE | | Lambda in first constructor for Thread execution | SRC CloudStreamServer.java:203-218 |
| CloudStreamServer.lambda$new$1 | REACHABLE | | Lambda in second constructor for Thread execution | SRC CloudStreamServer.java:231-246 |
| CloudStreamServer.stop | REACHABLE | | Called by CloudStreamer.stop | SRC CloudStreamServer.java:254-263 |
| CloudStreamServer.tryBind | REACHABLE | | Called from both constructors | SRC CloudStreamServer.java:271-280 |
| CloudStreamSource.<init> | REACHABLE | | Already labeled in graph_def.py batch 009 | SRC CloudStreamSource.java:18-24 |
| CloudStreamSource.close | REACHABLE | | Called by CloudStreamServer.sendResponse | SRC CloudStreamSource.java:77-82 |
| CloudStreamSource.getCurrentPosition | REACHABLE | | Called by RandomAccessStream (parent class) | SRC CloudStreamSource.java:96-98 |
| CloudStreamSource.getName | REACHABLE | | Used by server response handling | SRC CloudStreamSource.java:84-86 |
| CloudStreamSource.moveTo | REACHABLE | | Already labeled in graph_def.py batch 009 | SRC CloudStreamSource.java:88-94 |
| CloudStreamSource.open | REACHABLE | | Already labeled in graph_def.py batch 009 | SRC CloudStreamSource.java:53-62 |
| CloudStreamSource.read() | REACHABLE | | Called by CloudStreamServer.sendResponse | SRC CloudStreamSource.java:64-69 |
| CloudStreamSource.read(byte[],int,int) | REACHABLE | | Called by CloudStreamServer.sendResponse | SRC CloudStreamSource.java:71-75 |
| CloudStreamer.<clinit> | REACHABLE | | Static initializer creates Pattern for media file matching | SRC CloudStreamer.java:25 |
| CloudStreamer.<init> | REACHABLE | | Already labeled in graph_def.py batch 009 | SRC CloudStreamer.java:30-32 |
| CloudStreamer.getInstance | REACHABLE | | Already labeled in graph_def.py batch 009 | SRC CloudStreamer.java:34-41 |
| CloudStreamer.isStreamMedia | REACHABLE | | Public static method checks if file is streamable media | SRC CloudStreamer.java:43-45 |
| CloudStreamer.serve | REACHABLE | | Already labeled in graph_def.py batch 009 | SRC CloudStreamer.java:58-115 |
| CloudStreamer.setStreamSrc | REACHABLE | | Already labeled in graph_def.py batch 009 | SRC CloudStreamer.java:47-51 |
| CloudStreamer.stop | REACHABLE | | Already labeled in graph_def.py batch 009 | SRC CloudStreamer.java:53-57 |
| CloudUtil$1.doInBackground | REACHABLE | | Already labeled in graph_def.py batch 009 | SRC CloudUtil.java:179-228 |
| CloudUtil$1.onPostExecute | REACHABLE | | Already labeled in graph_def.py batch 009 | SRC CloudUtil.java:230-239 |
| CloudUtil$2$1.close | REACHABLE | | Anonymous RemoteFileInputStream.close override in getThumbnailInputStreamForCloud | SRC CloudUtil.java:268-277 |
| CloudUtil$2.<init> | REACHABLE | | Constructor for SFtpClientTemplate anonymous class in getThumbnailInputStreamForCloud | SRC CloudUtil.java:264-278 |
| CloudUtil.<init> | UNREACHABLE | no_trigger_in_app | CloudUtil has only static methods; no constructor calls found | SRC CloudUtil.java:52 (implicit constructor); grep -rn "new CloudUtil" shows no instantiation |
| CloudUtil.getThumbnailInputStreamForCloud | REACHABLE | | Public static method for getting cloud file thumbnails | SRC CloudUtil.java:248-307 |
| CloudUtil.lambda$launchCloud$1 | REACHABLE | | Lambda in launchCloud for UI thread execution | SRC CloudUtil.java:139-155 |
| CloudUtil.lambda$null$0 | REACHABLE | | Lambda in launchCloud for background thread | SRC CloudUtil.java:136-157 |
| CloudUtil.launchCloud | REACHABLE | | Already labeled in graph_def.py batch 009 | SRC CloudUtil.java:135-158 |
| CloudUtil.listFiles | REACHABLE | | Already labeled in graph_def.py batch 009 | SRC CloudUtil.java:59-64 |
| CoderBase.encode | REACHABLE | | Abstract method called by Coders.addEncoder via virtual dispatch | INFERRED commons_compress_7z library source not in src/main |
| CoderBase.getOptionsAsProperties | REACHABLE | | Called by SevenZ library when writing archive | INFERRED commons_compress_7z library source not in src/main |
| Coders$BCJDecoder.encode | REACHABLE | | Already labeled in graph_def.py batch 010 | SRC Coders.java (library code) |
| Coders$BZIP2Decoder.encode | REACHABLE | | Already labeled in graph_def.py batch 010 | SRC Coders.java (library code) |
| Coders$CopyDecoder.encode | REACHABLE | | Already labeled in graph_def.py batch 010 | SRC Coders.java (library code) |

STATUS: DONE 18:40
