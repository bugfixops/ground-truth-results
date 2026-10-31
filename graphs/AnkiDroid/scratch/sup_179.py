
# ---- sup for part 129 (2026-10-29): on API 27 CompatHelper picks CompatV21 (CompatHelper.java:35-36), and CompatV21 inherits each Compat method from a later override (CompatV16 for disableDatabaseWriteAheadLogging and updateWidgetDimensions, CompatV12 for enableCookiesForFileSchemePages, CompatV21 for prepareWebViewCookies). The CompatV10 and CompatV11 bodies and the Nook class are shadowed on API 27; their automatic CHA CALL edges are suppressed here. CompatHelper.<init> reaches the Nook constructor only when getSdkVersion() == 15 (CompatHelper.java:34).
sup(
    ('CompatHelper.<init>', 'CompatV15NookHdOrHdPlus.<init>'),
    ('AnkiDroidWidgetSmall$UpdateService.buildUpdate', 'CompatV10.updateWidgetDimensions'),
    ('AnkiDroidWidgetSmall.onReceive', 'CompatV10.updateWidgetDimensions'),
    ('AnkiDroidApp.onCreate', 'CompatV10.prepareWebViewCookies'),
    ('AnkiDroidApp.onCreate', 'CompatV10.enableCookiesForFileSchemePages'),
    ('Collection.close(boolean)', 'CompatV15NookHdOrHdPlus.disableDatabaseWriteAheadLogging'),
    ('Collection.close(boolean)', 'CompatV11.disableDatabaseWriteAheadLogging'),
    ('Collection.close(boolean)', 'CompatV10.disableDatabaseWriteAheadLogging'),
    ('DB.<init>', 'CompatV15NookHdOrHdPlus.disableDatabaseWriteAheadLogging'),
    ('DB.<init>', 'CompatV11.disableDatabaseWriteAheadLogging'),
    ('DB.<init>', 'CompatV10.disableDatabaseWriteAheadLogging'),
)
