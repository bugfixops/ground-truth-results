# LibreTorrent batch 57 helper report

Membership source: `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, filtered to batch 57 only. Exact count: 40.

Summary: 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. The inspected code contains utility implementations and local algorithmic calls, but this pass did not establish complete routes from an app entry point for any row. Uncertainty remains OPEN.

| Plan row | JVM method | Descriptor | Status | Evidence / limitation |
|---:|---|---|---|---|
| 1 | `DateUtils.startOfYesterday` | `(J)J` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 2 | `TorrentContentFileTreeUtils.buildFileTree` | `(Ljava/util/List;)Landroidx/core/util/Pair;` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 3 | `TorrentContentFileTreeUtils.makeObject` | `(ILjava/lang/String;JLorg/proninyaroslav/libretorrent/core/model/filetree/TorrentContentFileTree;Z)Lorg/proninyaroslav/libretorrent/core/model/filetree/TorrentContentFileTree;` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 4 | `Utils.<clinit>` | `()V` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 5 | `Utils.buildExactAlarmPermissionRequest` | `(Landroid/content/Context;)Landroid/content/Intent;` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 6 | `Utils.checkConnectivity` | `(Landroid/content/Context;)Z` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 7 | `Utils.colorizeProgressBar` | `(Landroid/content/Context;Landroid/widget/ProgressBar;)V` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 8 | `Utils.dpToPx` | `(Landroid/content/Context;F)I` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 9 | `Utils.enableBootReceiver` | `(Landroid/content/Context;Z)V` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 10 | `Utils.enableBootReceiverIfNeeded` | `(Landroid/content/Context;)V` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 11 | `Utils.fetchHttpUrl` | `(Landroid/content/Context;Ljava/lang/String;)[B` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 12 | `Utils.getAppTheme` | `(Landroid/content/Context;)I` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 13 | `Utils.getAppVersionNumber` | `(Ljava/lang/String;)Ljava/lang/String;` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 14 | `Utils.getAttributeColor` | `(Landroid/content/Context;I)I` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 15 | `Utils.getBatteryLevel` | `(Landroid/content/Context;)F` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 16 | `Utils.getClipData` | `(Landroid/content/Context;)Landroid/content/ClipData;` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 17 | `Utils.getClipboardText` | `(Landroid/content/Context;)Ljava/util/List;` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 18 | `Utils.getDefaultBatteryLowLevel` | `()I` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 19 | `Utils.getDrawerGroupDateAddedFilter` | `(Landroid/content/Context;J)Lorg/proninyaroslav/libretorrent/core/filter/TorrentFilter;` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 20 | `Utils.getDrawerGroupItemSorting` | `(Landroid/content/Context;J)Lorg/proninyaroslav/libretorrent/core/sorting/TorrentSortingComparator;` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 21 | `Utils.getDrawerGroupStatusFilter` | `(Landroid/content/Context;J)Lorg/proninyaroslav/libretorrent/core/filter/TorrentFilter;` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 22 | `Utils.getFileList` | `(Lorg/libtorrent4j/FileStorage;)Ljava/util/ArrayList;` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 23 | `Utils.getForegroundNotifyFilter` | `(Landroid/content/Context;Lorg/proninyaroslav/libretorrent/core/settings/SettingsRepository;)Lorg/proninyaroslav/libretorrent/core/filter/TorrentFilter;` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 24 | `Utils.getForegroundNotifySorting` | `(Landroid/content/Context;Lorg/proninyaroslav/libretorrent/core/settings/SettingsRepository;)Lorg/proninyaroslav/libretorrent/core/sorting/TorrentSortingComparator;` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 25 | `Utils.getLineSeparator` | `()Ljava/lang/String;` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 26 | `Utils.getNavigationDrawerItems` | `(Landroid/content/Context;Landroid/content/SharedPreferences;)Ljava/util/List;` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 27 | `Utils.getRandomColor` | `()I` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 28 | `Utils.getSSLContext` | `()Ljavax/net/ssl/SSLContext;` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 29 | `Utils.getSettingsTheme` | `(Landroid/content/Context;)I` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 30 | `Utils.getThemePreference` | `(Landroid/content/Context;)I` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 31 | `Utils.getTorrentDownloadPath` | `(Landroid/content/Context;)Landroid/net/Uri;` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 32 | `Utils.getTranslucentAppTheme` | `(Landroid/content/Context;)I` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 33 | `Utils.getVersionComponents` | `(Ljava/lang/String;)[I` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 34 | `Utils.hasManageExternalStoragePermission` | `(Landroid/content/Context;)Z` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 35 | `Utils.isBatteryBelowThreshold` | `(Landroid/content/Context;I)Z` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 36 | `Utils.isBatteryCharging` | `(Landroid/content/Context;)Z` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 37 | `Utils.isBatteryLow` | `(Landroid/content/Context;)Z` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 38 | `Utils.isFileSystemPath` | `(Landroid/net/Uri;)Z` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 39 | `Utils.isHash` | `(Ljava/lang/String;)Z` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |
| 40 | `Utils.isLargeScreenDevice` | `(Landroid/content/Context;)Z` | OPEN | Source definition is present; full hand-authored route from app entry not established in this bounded audit. |

## Source evidence
- `DateUtils.java:135`: `startOfYesterday(long)`.
- `TorrentContentFileTreeUtils.java:46,101,119`: `buildFileTree` invokes `makeObject`.
- `Utils.java`: method definitions for the listed utility methods were signature-scanned at the line numbers recorded in `batch_057_helper_printed.txt`.
- Source-local definition/call evidence is insufficient to prove entry-to-method reachability or absence of a route.

