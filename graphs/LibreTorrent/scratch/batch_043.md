# LibreTorrent batch 43 source audit

Membership is the exact 40-row set in `scratch/batch_043_plan.txt`. I checked the SettingsRepositoryImpl definitions and app use sites in `scratch/batch_043_helper_printed.txt`. Preferences have direct UI, service and engine use, but complete hand-authored routes from registered app entries were not established. All 40 methods remain OPEN; no missing grep result is treated as proof of unreachability.

| # | Method | Label | Evidence / route note |
|---:|---|---|---|
| 1 | `SettingsRepositoryImpl.autostart()` | OPEN | Preference getter; full entry route absent. |
| 2 | `SettingsRepositoryImpl.autostart(boolean)` | OPEN | Preference setter; UI route absent. |
| 3 | `SettingsRepositoryImpl.batteryControl()` | OPEN | Preference getter; entry route absent. |
| 4 | `SettingsRepositoryImpl.batteryControl(boolean)` | OPEN | Preference setter; UI route absent. |
| 5 | `SettingsRepositoryImpl.cpuDoNotSleep()` | OPEN | Service callers; service-entry route not audited. |
| 6 | `SettingsRepositoryImpl.cpuDoNotSleep(boolean)` | OPEN | Preference setter; UI callback route absent. |
| 7 | `SettingsRepositoryImpl.customBatteryControl()` | OPEN | Engine settings callers; entry route absent. |
| 8 | `SettingsRepositoryImpl.customBatteryControl(boolean)` | OPEN | Preference setter; UI route absent. |
| 9 | `SettingsRepositoryImpl.customBatteryControlValue()` | OPEN | Engine settings caller; entry route absent. |
| 10 | `SettingsRepositoryImpl.customBatteryControlValue(int)` | OPEN | Preference setter; UI route absent. |
| 11 | `SettingsRepositoryImpl.defaultTrackersList()` | OPEN | Engine/settings UI callers; entry route absent. |
| 12 | `SettingsRepositoryImpl.defaultTrackersList(String)` | OPEN | Settings UI caller; callback route absent. |
| 13 | `SettingsRepositoryImpl.dirToWatch()` | OPEN | Engine settings caller; entry route absent. |
| 14 | `SettingsRepositoryImpl.dirToWatch(String)` | OPEN | Storage settings caller; callback route absent. |
| 15 | `SettingsRepositoryImpl.enableDht()` | OPEN | Engine settings caller; entry route absent. |
| 16 | `SettingsRepositoryImpl.enableDht(boolean)` | OPEN | Network settings caller; callback route absent. |
| 17 | `SettingsRepositoryImpl.enableIpFiltering()` | OPEN | Engine caller; entry route absent. |
| 18 | `SettingsRepositoryImpl.enableIpFiltering(boolean)` | OPEN | Network settings caller; callback route absent. |
| 19 | `SettingsRepositoryImpl.enableLsd()` | OPEN | Engine settings caller; entry route absent. |
| 20 | `SettingsRepositoryImpl.enableLsd(boolean)` | OPEN | Network settings caller; callback route absent. |
| 21 | `SettingsRepositoryImpl.enableNatPmp()` | OPEN | Engine settings caller; entry route absent. |
| 22 | `SettingsRepositoryImpl.enableNatPmp(boolean)` | OPEN | Network settings caller; callback route absent. |
| 23 | `SettingsRepositoryImpl.enableRoaming()` | OPEN | Engine/utility callers; entry route absent. |
| 24 | `SettingsRepositoryImpl.enableRoaming(boolean)` | OPEN | Behavior settings caller; callback route absent. |
| 25 | `SettingsRepositoryImpl.enableSchedulingShutdown()` | OPEN | Receiver/UI use; complete entry route absent. |
| 26 | `SettingsRepositoryImpl.enableSchedulingShutdown(boolean)` | OPEN | Receiver/UI use; complete entry route absent. |
| 27 | `SettingsRepositoryImpl.enableSchedulingStart()` | OPEN | Receiver/UI use; complete entry route absent. |
| 28 | `SettingsRepositoryImpl.enableSchedulingStart(boolean)` | OPEN | Receiver/UI use; complete entry route absent. |
| 29 | `SettingsRepositoryImpl.enableStreaming()` | OPEN | Engine/settings UI callers; entry route absent. |
| 30 | `SettingsRepositoryImpl.enableStreaming(boolean)` | OPEN | Settings UI caller; callback route absent. |
| 31 | `SettingsRepositoryImpl.enableUpnp()` | OPEN | Engine settings caller; entry route absent. |
| 32 | `SettingsRepositoryImpl.enableUpnp(boolean)` | OPEN | Network settings caller; callback route absent. |
| 33 | `SettingsRepositoryImpl.enableUtp()` | OPEN | Engine settings caller; entry route absent. |
| 34 | `SettingsRepositoryImpl.enableUtp(boolean)` | OPEN | Network settings caller; callback route absent. |
| 35 | `SettingsRepositoryImpl.encryptInConnectionsMode()` | OPEN | Engine settings caller; entry route absent. |
| 36 | `SettingsRepositoryImpl.encryptInConnectionsMode(int)` | OPEN | Network settings caller; callback route absent. |
| 37 | `SettingsRepositoryImpl.encryptOutConnectionsMode()` | OPEN | Engine settings caller; entry route absent. |
| 38 | `SettingsRepositoryImpl.encryptOutConnectionsMode(int)` | OPEN | Network settings caller; callback route absent. |
| 39 | `SettingsRepositoryImpl.feedItemKeepTime()` | OPEN | FeedFetcherWorker/settings callers; entry route absent. |
| 40 | `SettingsRepositoryImpl.feedRemoveDuplicates()` | OPEN | FeedFetcherWorker/settings callers; entry route absent. |

Totals: 40 rows = 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. No graph labels changed, so no graph build was run for this batch.
