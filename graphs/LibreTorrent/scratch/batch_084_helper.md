# LibreTorrent batch 84 source audit

Membership is exactly the 40 batch 84 rows in batch_084_helper_printed.txt. Source excerpts cover the dialog listener registration and callbacks, mutable parameter model, view-model initialization/build/validation/download code, and the activity caller search. All 40 remain OPEN: local calls and callback bodies do not establish the complete app-entry path or framework/library dispatch chain required for a REACHABLE label. No missing search result is treated as proof of unreachability.

| # | Method | Finding | Printed source / unresolved route |
|---:|---|---|---|
| 1 | CreateTorrentDialog$2.onTextChanged | OPEN | CreateTorrentDialog.java:65-270 printed; Dialog/listener registration and complete activity-to-dialog entry route not fully traced. |
| 2 | CreateTorrentDialog$3.<init> | OPEN | CreateTorrentDialog.java:65-270 printed; Dialog/listener registration and complete activity-to-dialog entry route not fully traced. |
| 3 | CreateTorrentDialog$3.onItemSelected | OPEN | CreateTorrentDialog.java:65-270 printed; Dialog/listener registration and complete activity-to-dialog entry route not fully traced. |
| 4 | CreateTorrentDialog$3.onNothingSelected | OPEN | CreateTorrentDialog.java:65-270 printed; Dialog/listener registration and complete activity-to-dialog entry route not fully traced. |
| 5 | CreateTorrentDialog$4.<init> | OPEN | CreateTorrentDialog.java:65-270 printed; Dialog/listener registration and complete activity-to-dialog entry route not fully traced. |
| 6 | CreateTorrentDialog$4.onItemSelected | OPEN | CreateTorrentDialog.java:65-270 printed; Dialog/listener registration and complete activity-to-dialog entry route not fully traced. |
| 7 | CreateTorrentDialog$4.onNothingSelected | OPEN | CreateTorrentDialog.java:65-270 printed; Dialog/listener registration and complete activity-to-dialog entry route not fully traced. |
| 8 | CreateTorrentMutableParams.<init> | OPEN | CreateTorrentMutableParams.java:1-190 printed; Accessor/mutator body printed; complete binding/UI data dispatch and entry route not established. |
| 9 | CreateTorrentMutableParams.getComments | OPEN | CreateTorrentMutableParams.java:1-190 printed; Accessor/mutator body printed; complete binding/UI data dispatch and entry route not established. |
| 10 | CreateTorrentMutableParams.getPieceSizeIndex | OPEN | CreateTorrentMutableParams.java:1-190 printed; Accessor/mutator body printed; complete binding/UI data dispatch and entry route not established. |
| 11 | CreateTorrentMutableParams.getSavePath | OPEN | CreateTorrentMutableParams.java:1-190 printed; Accessor/mutator body printed; complete binding/UI data dispatch and entry route not established. |
| 12 | CreateTorrentMutableParams.getSeedPath | OPEN | CreateTorrentMutableParams.java:1-190 printed; Accessor/mutator body printed; complete binding/UI data dispatch and entry route not established. |
| 13 | CreateTorrentMutableParams.getSeedPathName | OPEN | CreateTorrentMutableParams.java:1-190 printed; Accessor/mutator body printed; complete binding/UI data dispatch and entry route not established. |
| 14 | CreateTorrentMutableParams.getSkipFiles | OPEN | CreateTorrentMutableParams.java:1-190 printed; Accessor/mutator body printed; complete binding/UI data dispatch and entry route not established. |
| 15 | CreateTorrentMutableParams.getTorrentVersionIndex | OPEN | CreateTorrentMutableParams.java:1-190 printed; Accessor/mutator body printed; complete binding/UI data dispatch and entry route not established. |
| 16 | CreateTorrentMutableParams.getTrackerUrls | OPEN | CreateTorrentMutableParams.java:1-190 printed; Accessor/mutator body printed; complete binding/UI data dispatch and entry route not established. |
| 17 | CreateTorrentMutableParams.getWebSeedUrls | OPEN | CreateTorrentMutableParams.java:1-190 printed; Accessor/mutator body printed; complete binding/UI data dispatch and entry route not established. |
| 18 | CreateTorrentMutableParams.isPrivateTorrent | OPEN | CreateTorrentMutableParams.java:1-190 printed; Accessor/mutator body printed; complete binding/UI data dispatch and entry route not established. |
| 19 | CreateTorrentMutableParams.isStartSeeding | OPEN | CreateTorrentMutableParams.java:1-190 printed; Accessor/mutator body printed; complete binding/UI data dispatch and entry route not established. |
| 20 | CreateTorrentMutableParams.setComments | OPEN | CreateTorrentMutableParams.java:1-190 printed; Accessor/mutator body printed; complete binding/UI data dispatch and entry route not established. |
| 21 | CreateTorrentMutableParams.setPieceSizeIndex | OPEN | CreateTorrentMutableParams.java:1-190 printed; Accessor/mutator body printed; complete binding/UI data dispatch and entry route not established. |
| 22 | CreateTorrentMutableParams.setPrivateTorrent | OPEN | CreateTorrentMutableParams.java:1-190 printed; Accessor/mutator body printed; complete binding/UI data dispatch and entry route not established. |
| 23 | CreateTorrentMutableParams.setSavePath | OPEN | CreateTorrentMutableParams.java:1-190 printed; Accessor/mutator body printed; complete binding/UI data dispatch and entry route not established. |
| 24 | CreateTorrentMutableParams.setSeedPathName | OPEN | CreateTorrentMutableParams.java:1-190 printed; Accessor/mutator body printed; complete binding/UI data dispatch and entry route not established. |
| 25 | CreateTorrentMutableParams.setSkipFiles | OPEN | CreateTorrentMutableParams.java:1-190 printed; Accessor/mutator body printed; complete binding/UI data dispatch and entry route not established. |
| 26 | CreateTorrentMutableParams.setStartSeeding | OPEN | CreateTorrentMutableParams.java:1-190 printed; Accessor/mutator body printed; complete binding/UI data dispatch and entry route not established. |
| 27 | CreateTorrentMutableParams.setTorrentVersionIndex | OPEN | CreateTorrentMutableParams.java:1-190 printed; Accessor/mutator body printed; complete binding/UI data dispatch and entry route not established. |
| 28 | CreateTorrentMutableParams.setTrackerUrls | OPEN | CreateTorrentMutableParams.java:1-190 printed; Accessor/mutator body printed; complete binding/UI data dispatch and entry route not established. |
| 29 | CreateTorrentMutableParams.setWebSeedUrls | OPEN | CreateTorrentMutableParams.java:1-190 printed; Accessor/mutator body printed; complete binding/UI data dispatch and entry route not established. |
| 30 | CreateTorrentMutableParams.toString | OPEN | CreateTorrentMutableParams.java:1-190 printed; Accessor/mutator body printed; complete binding/UI data dispatch and entry route not established. |
| 31 | CreateTorrentViewModel.<clinit> | OPEN | CreateTorrentViewModel.java:50-406 printed; Model/build/validation/download body printed; complete activity/dialog route and callback dispatch not established. |
| 32 | CreateTorrentViewModel.<init> | OPEN | CreateTorrentViewModel.java:50-406 printed; Model/build/validation/download body printed; complete activity/dialog route and callback dispatch not established. |
| 33 | CreateTorrentViewModel.buildTorrent | OPEN | CreateTorrentViewModel.java:50-406 printed; Model/build/validation/download body printed; complete activity/dialog route and callback dispatch not established. |
| 34 | CreateTorrentViewModel.decodeSkipFilesList | OPEN | CreateTorrentViewModel.java:50-406 printed; Model/build/validation/download body printed; complete activity/dialog route and callback dispatch not established. |
| 35 | CreateTorrentViewModel.decodeUrls | OPEN | CreateTorrentViewModel.java:50-406 printed; Model/build/validation/download body printed; complete activity/dialog route and callback dispatch not established. |
| 36 | CreateTorrentViewModel.downloadTorrent | OPEN | CreateTorrentViewModel.java:50-406 printed; Model/build/validation/download body printed; complete activity/dialog route and callback dispatch not established. |
| 37 | CreateTorrentViewModel.finish | OPEN | CreateTorrentViewModel.java:50-406 printed; Model/build/validation/download body printed; complete activity/dialog route and callback dispatch not established. |
| 38 | CreateTorrentViewModel.getAndValidateTrackers | OPEN | CreateTorrentViewModel.java:50-406 printed; Model/build/validation/download body printed; complete activity/dialog route and callback dispatch not established. |
| 39 | CreateTorrentViewModel.getAndValidateWebSeeds | OPEN | CreateTorrentViewModel.java:50-406 printed; Model/build/validation/download body printed; complete activity/dialog route and callback dispatch not established. |
| 40 | CreateTorrentViewModel.getBuildProgress | OPEN | CreateTorrentViewModel.java:50-406 printed; Model/build/validation/download body printed; complete activity/dialog route and callback dispatch not established. |

Count: 40 plan rows = 40 OPEN, 0 REACHABLE labels, 0 UNREACHABLE labels. No graph edits or coverage evidence were used.
