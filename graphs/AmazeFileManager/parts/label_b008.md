STATUS: RUNNING 21:24

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| CloudIconModelFactory.<init> | REACHABLE | EXPLICIT | Called from GlideApp registration code | SRC CloudIconModelFactory.java:18-20 |
| CloudIconModelFactory.build | REACHABLE | EXPLICIT | Called by Glide when loading cloud images | SRC CloudIconModelFactory.java:23-26 |
| CloudIconModelFactory.teardown | REACHABLE | EXPLICIT | Called by Glide lifecycle | SRC CloudIconModelFactory.java:29-31 |
| CloudIconModelLoader.<init> | REACHABLE | EXPLICIT | Called from CloudIconModelFactory.build | SRC CloudIconModelLoader.java:19-21 |
| CloudIconModelLoader.buildLoadData | REACHABLE | EXPLICIT | Called by Glide for image loading | SRC CloudIconModelLoader.java:25-31 |
| CloudIconModelLoader.handles | REACHABLE | EXPLICIT | Called by Glide to check if loader handles URI | SRC CloudIconModelLoader.java:33-40 |
| CloudPluginException.<init> | REACHABLE | EXPLICIT | Thrown from CloudHandler and CloudUtil methods | SRC CloudHandler.java:85-86, CloudPluginException.java:7-9 |
| CloudSheetFragment.<init> | REACHABLE | EXPLICIT | Instantiated in MainActivity | SRC MainActivity.java:1953 |
| CloudSheetFragment.onCreate | REACHABLE | LIFECYCLE | Called by Android framework on fragment creation | SRC CloudSheetFragment.java:40-41 |
| CloudSheetFragment.setupDialog | REACHABLE | LIFECYCLE | Called by Android framework during dialog setup | SRC CloudSheetFragment.java:45-87 |
| CloudSheetFragment.onClick | REACHABLE | EXPLICIT | Set as click listener in setupDialog | SRC CloudSheetFragment.java:101-146 |
| CloudSheetFragment.isCloudProviderAvailable | REACHABLE | EXPLICIT | Called from CloudSheetFragment.setupDialog and other cloud-related code | SRC CloudSheetFragment.java:89-97, Drawer.java:308, CloudHandler.java:85 |
| CloudStreamServer.<clinit> | REACHABLE | SYSTEM | Static initializer always runs on class load | SRC CloudStreamServer.java:70-75 |
| CloudStreamServer.<init> | REACHABLE | EXPLICIT | Called from CloudStreamer.<init> | SRC CloudStreamer.java:31, CloudStreamServer.java:199-225 |
| CloudStreamServer.<init> | REACHABLE | EXPLICIT | Called from CloudStreamer.<init> (overload) | SRC CloudStreamer.java:31, CloudStreamServer.java:226-245 |
| CloudStreamServer.encodeUri | REACHABLE | EXPLICIT | Called from HTTPSession.handleResponse | SRC CloudStreamServer.java:1 |
| CloudStreamServer.lambda$new$0 | REACHABLE | SYSTEM | Created in CloudStreamServer constructor for server thread | SRC CloudStreamServer.java:204-220 |
| CloudStreamServer.lambda$new$1 | REACHABLE | SYSTEM | Created in CloudStreamServer constructor for server thread | SRC CloudStreamServer.java:228-244 |
| CloudStreamServer.stop | REACHABLE | EXPLICIT | Called from CloudStreamer.stop and StreamServer.tryBind | SRC CloudStreamer.java:52-55, StreamServer.java:212 |
| CloudStreamServer.tryBind | REACHABLE | EXPLICIT | Called from CloudStreamServer constructor | SRC CloudStreamServer.java:199-201, 226-228 |
| CloudStreamServer$HTTPSession.<init> | REACHABLE | EXPLICIT | Instantiated in server loop when client connects | SRC CloudStreamServer.java:217-218 |
| CloudStreamServer$HTTPSession.decodeHeader | REACHABLE | EXPLICIT | Called from handleResponse to parse HTTP headers | SRC CloudStreamServer.java:385, 518-570 |
| CloudStreamServer$HTTPSession.decodeMultipartData | REACHABLE | EXPLICIT | Called from handleResponse when processing multipart form data | SRC CloudStreamServer.java:480-481, 574-651 |
| CloudStreamServer$HTTPSession.decodeParms | REACHABLE | EXPLICIT | Called from handleResponse and decodeMultipartData | SRC CloudStreamServer.java:473-475, 772-791 |
| CloudStreamServer$HTTPSession.decodePercent | REACHABLE | EXPLICIT | Called from decodeHeader to decode URI | SRC CloudStreamServer.java:508, 734-770 |
| CloudStreamServer$HTTPSession.getBoundaryPositions | REACHABLE | EXPLICIT | Called from decodeMultipartData to find boundary markers | SRC CloudStreamServer.java:598, 656-693 |
| CloudStreamServer$HTTPSession.handleResponse | REACHABLE | EXPLICIT | Called from HTTPSession.run | SRC CloudStreamServer.java:358-361, 363-816 |
| CloudStreamServer$HTTPSession.run | REACHABLE | LIFECYCLE | Thread entry point, called by thread start | SRC CloudStreamServer.java:342-361 |
| CloudStreamServer$HTTPSession.saveTmpFile | REACHABLE | EXPLICIT | Called from decodeMultipartData to save uploaded file | SRC CloudStreamServer.java:608, 695-717 |
| CloudStreamServer$HTTPSession.sendError | REACHABLE | EXPLICIT | Called from handleResponse and decodeHeader on errors | SRC CloudStreamServer.java:389, 398, 402, 479-480, 484, 597, 601, 605, 793-800 |
| CloudStreamServer$HTTPSession.sendResponse | REACHABLE | EXPLICIT | Called from handleResponse to send HTTP response | SRC CloudStreamServer.java:512-514, 802-833 |
| CloudStreamServer$HTTPSession.stripMultipartHeaders | REACHABLE | EXPLICIT | Called from decodeMultipartData to process multipart headers | SRC CloudStreamServer.java:607, 719-732 |
| CloudStreamServer$Response.<init> | REACHABLE | EXPLICIT | Instantiated in CloudStreamer.serve method | SRC CloudStreamer.java:65, 93, 106, 111, CloudStreamServer.java:103-107 |
| CloudStreamServer$Response.<init> | REACHABLE | EXPLICIT | Instantiated in CloudStreamer.serve method (overload with 3 params) | SRC CloudStreamer.java:65, 93, 106, 111, CloudStreamServer.java:111-118 |
| CloudStreamServer$Response.addHeader | REACHABLE | EXPLICIT | Called from CloudStreamer.serve to set response headers | SRC CloudStreamer.java:97, 107, 112, 114, CloudStreamServer.java:139-144 |

STATUS: DONE 21:24
