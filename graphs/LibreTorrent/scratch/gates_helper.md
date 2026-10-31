# LibreTorrent session 2 gate review helper

Reviewed `out/build_report.txt` and the source named below. The report has 201 `WARN TO CLASSIFY` rows, but only 54 are gate-kind warnings; the remaining 147 say `no route found, labelled UNREACHABLE by AUTO_DEAD` and are method-label warnings, not gates. The 54 gate rows reduce to four distinct texts.

## Distinct gate text and recommendation

### 1. `outside package: the device reboots (BOOT_COMPLETED) or another system broadcast arrives`

Affected edges: `Ecc50358b`, `E41682652`, `Ecf4b18b9`.

- `Ecc50358b` (`S_ENTRY -> S_SYS_BootReceiver`): ENV `system_event`. The manifest filter names boot and quick-boot broadcasts, and `BootReceiver.isBootCompleted` checks those actions. Printed source: `app/src/main/AndroidManifest.xml:265-273`; `app/src/main/java/org/proninyaroslav/libretorrent/receiver/BootReceiver.java:43-58`.
- `E41682652` (`S_ENTRY -> S_SYS_NotificationReceiver`): remove this generic gate from this edge. The receiver is explicitly not exported and the listed notification actions are app-defined; `TorrentService` creates explicit PendingIntents targeting it. Printed source: `app/src/main/AndroidManifest.xml:256-263`; `app/src/main/java/org/proninyaroslav/libretorrent/service/TorrentService.java:497-502`.
- `Ecf4b18b9` (`S_ENTRY -> S_SYS_SchedulerReceiver`): ENV `time` if this edge represents the scheduled alarm firing. `SchedulerReceiver` has no manifest filter, while `Scheduler.setStartStopAppAlarm` sets an alarm for a configured wall-clock time. The reboot/system-broadcast wording is wrong for this edge. Printed source: `app/src/main/AndroidManifest.xml:276-277`; `app/src/main/java/org/proninyaroslav/libretorrent/service/Scheduler.java:80-105`.

### 2. `outside package: another app, the system or adb sends the intent / broadcast / content call`

Affected edges: `Eff9ed769`, `E4987a154`, `Ea1aa384c`, `E1ec0a247`. Recommendation: ENV `other_app` for these exported activity entry points. The manifest exposes `SendTextToClipboard`, `AddFeedActivity`, and `AddTorrentActivity` for SEND/VIEW actions and `SettingsActivity` for APPLICATION_PREFERENCES. Printed source: `app/src/main/AndroidManifest.xml:62-100`, `141-162`, `178-205`.

### 3. `The list / adapter shows at least one row (some user data exists: add an item first)`

Affected edges (42): `E5addfafe`, `E71271699`, `E62b78a7c`, `E6f29c666`, `Ee907c8e2`, `Efb30ef3a`, `E16685fdf`, `E1b07f1cf`, `E46820032`, `E78433568`, `Ee64196d8`, `E1fbbffda`, `Ef9609fca`, `E3eb184d9`, `E63fbebcf`, `Edd0fb769`, `E1e75b01e`, `E670b1893`, `E02fa4390`, `E7c7bfdd7`, `E3aa8e0df`, `E88455f06`, `Eaad49900`, `E1a96f7c4`, `E343acb52`, `Edc880d2d`, `Ea27a2285`, `E0686b8bf`, `Ea4b1cb4b`, `E41ff908d`, `E41f32163`, `E16ab1d1e`, `Eeaca07e3`, `E280240fc`, `Ebc0da7c1`, `Eb0f81ff6`, `Ea5dc3a67`, `Eda8fbc9f`, `E56660e23`, `Eace6a920`, `E48ae04d4`, `Ed60883c3`.

Recommendation: STATE `data`; these edges describe row-backed adapter callbacks. Source example: `app/src/main/java/org/proninyaroslav/libretorrent/ui/customviews/EmptyRecyclerView.java:69-76` checks `getAdapter().getItemCount() == 0` to switch between empty and populated views. `DownloadableFilesAdapter` binds the supplied row item at `app/src/main/java/org/proninyaroslav/libretorrent/ui/addtorrent/DownloadableFilesAdapter.java:102-110`. The prose in the gate is a graph description, not a literal code string; preserve the exact report text here for matching, and use a source-derived predicate if the graph schema requires literal code text.

Printed callback declarations covering the grouped edges: `ui/addtorrent/DownloadableFilesAdapter.java:57,69`; `ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:366,384,394,408`; `ui/detailtorrent/pages/files/TorrentContentFilesAdapter.java:73,85`; `ui/detailtorrent/pages/peers/PeerListAdapter.java:59,71`; `ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:298,304,314,330`; `ui/detailtorrent/pages/trackers/TrackerListAdapter.java:70,82`; `ui/feeditems/FeedItemsAdapter.java:64,76`; `ui/feeds/FeedChannelListAdapter.java:79,91`; `ui/feeds/FeedFragment.java:356,371,380,405`; `ui/filemanager/FileManagerAdapter.java:74,82`; `ui/filemanager/FileManagerSpinnerAdapter.java:128,134`; `ui/log/LogAdapter.java:48,60`; `ui/main/MainFragment.java:460,466,475,494`; `ui/main/TorrentListAdapter.java:76,88`; `ui/main/drawer/TagsAdapter.java:60,96,104`; `ui/tag/TagsAdapter.java:46,58`. These callback bodies take the row/index supplied by the adapter/framework; none contains an app-authored “at least one row” branch at these callback declarations.

### 4. `outside package: the notification shade, an alarm, a launcher widget or shortcut starts it`

Affected edges: `Ee75ec53e`, `Eeb44303f`, `E41cc7170`, `Ebb1ee4a5`, `E47742ff4`.

- `Ee75ec53e` (`TorrentNotifier.makeTorrentFinishedNotify -> DetailTorrentActivity.<init>`) and `Eeb44303f` (`TorrentService.initPendingIntents -> S_SYS_NotificationReceiver`): ENV `system_event` for a user activating a notification from system UI. The app creates explicit PendingIntents; the external step is the notification interaction. Printed source: `app/src/main/java/org/proninyaroslav/libretorrent/ui/TorrentNotifier.java:212-238`; `app/src/main/java/org/proninyaroslav/libretorrent/service/TorrentService.java:497-522`.
- `E41cc7170` and `Ebb1ee4a5` (the `Scheduler.cancel*AppAlarm -> S_SYS_SchedulerReceiver` edges): remove the gate/edges as receiver-trigger claims. These methods construct PendingIntents and cancel alarms; cancellation does not dispatch the receiver. Printed source: `app/src/main/java/org/proninyaroslav/libretorrent/service/Scheduler.java:60-78`.
- `E47742ff4` (`Scheduler.setStartStopAppAlarm -> S_SYS_SchedulerReceiver`): ENV `time`; this sets a one-shot alarm for a scheduled wall-clock time. Printed source: `app/src/main/java/org/proninyaroslav/libretorrent/service/Scheduler.java:80-105`.

No coverage files or coverage results were used.
