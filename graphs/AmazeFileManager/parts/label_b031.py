# ---- Helper batch_031 label part (2025-01-18)

# FtpService - REACHABLE methods via FtpReceiver broadcast and FtpTileService

# FtpService.<clinit> - REACHABLE via class load when FtpReceiver.onReceive creates Intent
e('FtpReceiver.onReceive', 'FtpService.<clinit>', 'FRAMEWORK',
  'Framework loads FtpService class when Intent constructed at line 20',
  evidence='SRC FtpReceiver.java:20')

# FtpService.<init> - REACHABLE via startService
e('FtpReceiver.onReceive', 'FtpService.<init>', 'FRAMEWORK',
  'Framework calls constructor when context.startService invoked',
  evidence='SRC FtpReceiver.java:24')

# FtpService.onStartCommand - REACHABLE via Service lifecycle
e('FtpService.<init>', 'FtpService.onStartCommand', 'LIFECYCLE',
  'Framework calls onStartCommand after service started',
  evidence='SRC FtpService.java:119-142, FtpReceiver.java:24')

# FtpService.run - REACHABLE via Thread.start
e('FtpService.onStartCommand', 'FtpService.run', 'ASYNC',
  'onStartCommand creates Thread with this Runnable and calls start',
  evidence='SRC FtpService.java:131-132')

# FtpService.getPort - REACHABLE via run
e('FtpService.run', 'FtpService.getPort', 'CALL',
  'run calls getPort to configure listener factory',
  evidence='SRC FtpService.java:220')

# FtpService.onDestroy - REACHABLE via Service lifecycle
e('FtpService.<init>', 'FtpService.onDestroy', 'LIFECYCLE',
  'Framework calls onDestroy when service stopped',
  evidence='SRC FtpService.java:234-247, FtpReceiver.java:26')

# FtpService.onTaskRemoved - REACHABLE via Service lifecycle
e('FtpService.<init>', 'FtpService.onTaskRemoved', 'LIFECYCLE',
  'Framework calls onTaskRemoved when task removed from recents',
  evidence='SRC FtpService.java:251-262')

# FtpService.onBind - REACHABLE via Service lifecycle
e('FtpService.<init>', 'FtpService.onBind', 'LIFECYCLE',
  'Framework calls onBind for Service even though returns null',
  evidence='SRC FtpService.java:148-151')

# FtpService.isRunning - REACHABLE via static calls from FtpTileService and FtpReceiver
e('FtpTileService.onClick', 'FtpService.isRunning', 'CALL',
  'FtpTileService.onClick calls isRunning to check state',
  evidence='SRC FtpTileService.java:47')

e('FtpTileService.updateTileState', 'FtpService.isRunning', 'CALL',
  'updateTileState calls isRunning to update tile',
  evidence='SRC FtpTileService.java:65')

e('FtpReceiver.onReceive', 'FtpService.isRunning', 'CALL',
  'FtpReceiver checks isRunning before starting service',
  evidence='SRC FtpReceiver.java:23')

# FtpService.isConnectedToLocalNetwork - REACHABLE via static calls
e('FtpTileService.onClick', 'FtpService.isConnectedToLocalNetwork', 'CALL',
  'onClick checks network connection before starting service',
  evidence='SRC FtpTileService.java:51')

e('FtpService.getLocalInetAddress', 'FtpService.isConnectedToLocalNetwork', 'CALL',
  'getLocalInetAddress calls isConnectedToLocalNetwork',
  evidence='SRC FtpService.java:307')

# FtpService.isConnectedToWifi - REACHABLE via static calls
e('FtpTileService.onClick', 'FtpService.isConnectedToWifi', 'CALL',
  'onClick checks wifi connection before starting service',
  evidence='SRC FtpTileService.java:50')

e('FtpService.getLocalInetAddress', 'FtpService.isConnectedToWifi', 'CALL',
  'getLocalInetAddress calls isConnectedToWifi',
  evidence='SRC FtpService.java:311')

# FtpService.isEnabledWifiHotspot - REACHABLE via static calls
e('FtpTileService.onClick', 'FtpService.isEnabledWifiHotspot', 'CALL',
  'onClick checks wifi hotspot before starting service',
  evidence='SRC FtpTileService.java:52')

e('FtpService.getLocalInetAddress', 'FtpService.isEnabledWifiHotspot', 'CALL',
  'getLocalInetAddress calls isEnabledWifiHotspot',
  evidence='SRC FtpService.java:307, 328')

# FtpService.getLocalInetAddress - REACHABLE via FtpNotification
e('FtpNotification.startNotification', 'FtpService.getLocalInetAddress', 'CALL',
  'FtpNotification calls getLocalInetAddress to show IP in notification',
  evidence='SRC FtpNotification.java:77')

# FtpService.intToInet - REACHABLE via getLocalInetAddress
e('FtpService.getLocalInetAddress', 'FtpService.intToInet', 'CALL',
  'getLocalInetAddress calls intToInet to convert IP address',
  evidence='SRC FtpService.java:316')

# FtpService.byteOfInt - REACHABLE via intToInet
e('FtpService.intToInet', 'FtpService.byteOfInt', 'CALL',
  'intToInet calls byteOfInt in loop to extract bytes',
  evidence='SRC FtpService.java:351')

# FtpService.callIsWifiApEnabled - REACHABLE via isEnabledWifiHotspot
e('FtpService.isEnabledWifiHotspot', 'FtpService.callIsWifiApEnabled', 'CALL',
  'isEnabledWifiHotspot calls callIsWifiApEnabled',
  evidence='SRC FtpService.java:302')

# FtpService$FtpReceiverActions.<clinit> - REACHABLE via EventBus.post
e('FtpService.run', 'FtpService$FtpReceiverActions.<clinit>', 'FRAMEWORK',
  'Framework loads enum when referenced in EventBus.post',
  evidence='SRC FtpService.java:228, 230')

# FtpTileService - REACHABLE via Quick Settings Tile

# FtpTileService.<init> - REACHABLE via TileService lifecycle
e('ENTRY_POINT.QS_TILE', 'FtpTileService.<init>', 'FRAMEWORK',
  'Framework constructs TileService when user adds QS tile',
  evidence='SRC AndroidManifest.xml:195-201')

# FtpTileService.onStartListening - REACHABLE via TileService lifecycle
e('FtpTileService.<init>', 'FtpTileService.onStartListening', 'LIFECYCLE',
  'Framework calls onStartListening when tile becomes visible',
  evidence='SRC FtpTileService.java:28-32')

# FtpTileService.onStopListening - REACHABLE via TileService lifecycle
e('FtpTileService.<init>', 'FtpTileService.onStopListening', 'LIFECYCLE',
  'Framework calls onStopListening when tile no longer visible',
  evidence='SRC FtpTileService.java:35-38')

# FtpTileService.onClick - REACHABLE via TileService lifecycle
e('FtpTileService.<init>', 'FtpTileService.onClick', 'LIFECYCLE',
  'Framework calls onClick when user taps the tile',
  evidence='SRC FtpTileService.java:41-58')

# FtpTileService.lambda$onClick$0 - REACHABLE via onClick's lambda
e('FtpTileService.onClick', 'FtpTileService.lambda$onClick$0', 'CALL',
  'onClick calls unlockAndRun with lambda body compiled as this method',
  evidence='SRC FtpTileService.java:46-57')

# FtpTileService.updateTileState - REACHABLE via onStartListening and EventBus callback
e('FtpTileService.onStartListening', 'FtpTileService.updateTileState', 'CALL',
  'onStartListening calls updateTileState to initialize',
  evidence='SRC FtpTileService.java:31')

e('FtpTileService.onFtpReceiverActions', 'FtpTileService.updateTileState', 'CALL',
  'onFtpReceiverActions calls updateTileState on EventBus event',
  evidence='SRC FtpTileService.java:24')

# FtpTileService.onFtpReceiverActions - REACHABLE via EventBus
e('EventBus.register', 'FtpTileService.onFtpReceiverActions', 'SYSTEM',
  'EventBus invokes @Subscribe method when registered and event posted',
  evidence='SRC FtpTileService.java:23-25, 30')

# UNREACHABLE methods
UNREACHABLE_PART_B031 = {
}
