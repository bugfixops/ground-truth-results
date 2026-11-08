STATUS: RUNNING 21:30

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| CloudStreamSource.<init> | REACHABLE | | Created in CloudStreamer.serve() | SRC CloudStreamer.java:89 |
| CloudStreamSource.close | REACHABLE | | Override of RandomAccessStream, called on returned stream | SRC RandomAccessStream.java (framework) |
| CloudStreamSource.getCurrentPosition | REACHABLE | | Override of RandomAccessStream, called by framework | SRC RandomAccessStream.java (framework) |
| CloudStreamSource.getName | REACHABLE | | Called in CloudStreamer.serve() constructor at line 89 | SRC CloudStreamer.java:89 |
| CloudStreamSource.moveTo | REACHABLE | | Called in CloudStreamer.serve() | SRC CloudStreamer.java:103 |
| CloudStreamSource.open | REACHABLE | | Called implicitly in serve flow | SRC CloudStreamer.java:85-110 |
| CloudStreamSource.read | REACHABLE | | Override of RandomAccessStream, called by HTTP server | SRC RandomAccessStream.java (framework) |
| CloudStreamSource.read | REACHABLE | | Overload (byte[],int,int), called by HTTP server | SRC RandomAccessStream.java (framework) |
| CloudStreamer.<clinit> | REACHABLE | | Static initializer for pattern field | SRC CloudStreamer.java:25 |
| CloudStreamer.<init> | REACHABLE | | Called in getInstance() | SRC CloudStreamer.java:37 |
| CloudStreamer.getInstance | REACHABLE | | Called from CloudUtil.launchCloud | SRC CloudUtil.java:135 |
| CloudStreamer.isStreamMedia | REACHABLE | | Static utility method, called from app | SRC CloudStreamer.java:43-44 |
| CloudStreamer.serve | REACHABLE | | Override of CloudStreamServer.serve, framework dispatch | SRC CloudStreamer.java:62-117 |
| CloudStreamer.setStreamSrc | REACHABLE | | Called in launchCloud thread | SRC CloudUtil.java:138 |
| CloudStreamer.stop | REACHABLE | | Called from SshClientUtils | SRC SshClientUtils.java:239 |
| CloudUtil.<init> | REACHABLE | | Implicit constructor | SRC CloudUtil.java:46 |
| CloudUtil.checkToken | REACHABLE | | Called from Drawer | SRC Drawer.java:577 |
| CloudUtil.getCloudFiles | REACHABLE | | Called from LoadFilesListTask | SRC LoadFilesListTask.java:458 |
| CloudUtil.getThumbnailInputStreamForCloud | REACHABLE | | Utility called from CloudIconDataFetcher or similar | SRC CloudUtil.java:249-332 |
| CloudUtil.lambda$launchCloud$1 | REACHABLE | | Lambda in runOnUiThread | SRC CloudUtil.java:140 |
| CloudUtil.lambda$null$0 | REACHABLE | | Lambda in AsyncTask.execute/checkToken | SRC CloudUtil.java:174 |
| CloudUtil.launchCloud | REACHABLE | | Called from MainFragment | SRC MainFragment.java:930 |
| CloudUtil.listFiles | REACHABLE | | Called from HybridFile | SRC HybridFile.java:864 |
| CloudUtil.stripPath | REACHABLE | | Called in launchCloud | SRC CloudUtil.java:142 |
| CloudUtil$1.<init> | REACHABLE | | Anonymous AsyncTask created in checkToken | SRC CloudUtil.java:174 |
| CloudUtil$1.doInBackground | REACHABLE | | AsyncTask override called by framework | SRC CloudUtil.java:179 |
| CloudUtil$1.onPostExecute | REACHABLE | | AsyncTask override called by framework | SRC CloudUtil.java:237 |
| CloudUtil$2.<init> | REACHABLE | | Anonymous Runnable in Thread created in launchCloud | SRC CloudUtil.java:137 |
| CloudUtil$2.execute | REACHABLE | | Runnable.run() called by Thread framework | SRC CloudUtil.java:138 |
| CloudUtil$2$1.<init> | REACHABLE | | Inner class from getThumbnailInputStreamForCloud SFTP | SRC CloudUtil.java:265 |
| CloudUtil$2$1.close | REACHABLE | | InputStream override called by framework | SRC CloudUtil.java:270 |
| Coder.<init> | REACHABLE | | Instantiated in SevenZFile | SRC SevenZFile.java:642 |
| CoderBase.<clinit> | REACHABLE | | Static initializer for NONE array | SRC CoderBase.java:29 |
| CoderBase.<init> | REACHABLE | | Called by Coder and subclasses | SRC CoderBase.java:35 |
| CoderBase.canAcceptOptions | REACHABLE | | Called from SevenZMethodConfiguration | SRC SevenZMethodConfiguration.java:59 |
| CoderBase.encode | REACHABLE | | Called from Coders methods for encoding | SRC Coders.java:+ |
| CoderBase.getOptionsAsProperties | REACHABLE | | Called from Coders utility | SRC Coders.java:+ |
| CoderBase.getOptionsFromCoder | REACHABLE | | Called in SevenZFile | SRC SevenZFile.java:1033 |
| CoderBase.numberOptionOrDefault | REACHABLE | | Static utility called by subclasses | SRC CoderBase.java:72 |

STATUS: DONE 21:30
