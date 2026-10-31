STATUS: RUNNING 23:09

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| FtpService.<clinit> | REACHABLE | | Loaded when FtpReceiver constructs Intent referencing FtpService class | SRC FtpReceiver.java:20 |
| FtpService.<init> | REACHABLE | | Framework constructs Service when startService called | SRC FtpReceiver.java:24 |
| FtpService.byteOfInt | REACHABLE | | Called by intToInet to extract byte from int | SRC FtpService.java:351 |
| FtpService.callIsWifiApEnabled | REACHABLE | | Called by isEnabledWifiHotspot to check hotspot state via reflection | SRC FtpService.java:302 |
| FtpService.getLocalInetAddress | REACHABLE | | Called by FtpNotification to display server IP address | SRC FtpNotification.java:77 |
| FtpService.getPort | REACHABLE | | Called by run to get port from preferences for FTP server | SRC FtpService.java:220 |
| FtpService.intToInet | REACHABLE | | Called by getLocalInetAddress to convert int IP to InetAddress | SRC FtpService.java:316 |
| FtpService.isConnectedToLocalNetwork | REACHABLE | | Called by FtpTileService.onClick and getLocalInetAddress to check network | SRC FtpTileService.java:51, FtpService.java:307 |
| FtpService.isConnectedToWifi | REACHABLE | | Called by FtpTileService.onClick and getLocalInetAddress to check wifi | SRC FtpTileService.java:50, FtpService.java:311 |
| FtpService.isEnabledWifiHotspot | REACHABLE | | Called by FtpTileService.onClick and getLocalInetAddress to check hotspot | SRC FtpTileService.java:52, FtpService.java:307, 328 |
| FtpService.isRunning | REACHABLE | | Called by FtpTileService, FtpReceiver to check if server thread running | SRC FtpTileService.java:47, 65, FtpReceiver.java:23 |
| FtpService.onBind | REACHABLE | | Service lifecycle method, framework calls even though returns null | SRC FtpService.java:148-151 |
| FtpService.onDestroy | REACHABLE | | Service lifecycle method, called when stopService invoked | SRC FtpService.java:234-247, FtpReceiver.java:26 |
| FtpService.onStartCommand | REACHABLE | | Service lifecycle method, framework calls after startService | SRC FtpService.java:119-142, FtpReceiver.java:24 |
| FtpService.onTaskRemoved | REACHABLE | | Service lifecycle method, framework calls when task removed from recents | SRC FtpService.java:251-262 |
| FtpService.run | REACHABLE | | Runnable.run called when serverThread.start invoked in onStartCommand | SRC FtpService.java:131-132, 153-233 |
| FtpService$FtpReceiverActions.<clinit> | REACHABLE | | Enum class loaded when referenced in EventBus.post calls | SRC FtpService.java:228, 230 |
| FtpTileService.<init> | REACHABLE | | Framework constructs TileService when QS tile added | SRC AndroidManifest.xml:195-201 |
| FtpTileService.lambda$onClick$0 | REACHABLE | | Lambda body from onClick's unlockAndRun parameter | SRC FtpTileService.java:46-57 |
| FtpTileService.onClick | REACHABLE | | TileService lifecycle method, framework calls when user taps tile | SRC FtpTileService.java:41-58 |
| FtpTileService.onFtpReceiverActions | REACHABLE | | EventBus @Subscribe method invoked when FtpReceiverActions posted | SRC FtpTileService.java:23-25, 30 |
| FtpTileService.onStartListening | REACHABLE | | TileService lifecycle method, framework calls when tile visible | SRC FtpTileService.java:28-32 |
| FtpTileService.onStopListening | REACHABLE | | TileService lifecycle method, framework calls when tile not visible | SRC FtpTileService.java:35-38 |
| FtpTileService.updateTileState | REACHABLE | | Called by onStartListening and onFtpReceiverActions to update tile UI | SRC FtpTileService.java:31, 24, 61-71 |

STATUS: DONE 23:11
