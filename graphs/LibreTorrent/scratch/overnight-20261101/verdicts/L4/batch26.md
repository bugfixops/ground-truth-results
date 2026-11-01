# L4 verdicts — batch 26 (D12 confirmation, no flips)

| batch/row | method | old label | NEW label | confirmed_by | evidence | revert condition |
| 26/32 | TorrentInfoProvider.lambda$makeAdvancedInfoFlowable$12 | REACHABLE | REACHABLE | INFERRED | verified, no change — D12: Observable.interval tick consumer printed (TorrentInfoProvider.java:327-338); subscription route printed via observeAdvancedInfo → DetailTorrentViewModel → DetailTorrentFragment (batch file); Rx dispatch INFERRED | N/A |
| 26/33 | TorrentInfoProvider.lambda$makeAdvancedInfoFlowable$13 | REACHABLE | REACHABLE | INFERRED | verified, no change — D12: interval error consumer printed (TorrentInfoProvider.java:337-338, Log.e on error); subscription printed (grep_D26_subscriptions.txt); error occurrence is a runtime condition, not a blocker, under D12 | A user rule requiring a shown error occurrence would return this row to OPEN (per D12), not UNREACHABLE |
