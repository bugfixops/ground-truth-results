# Spot-check — batch 30 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json, plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). Rows 6 and 16 are in both sets; checked once, under Changed. Verdicts D1–D36/R1–R5 are NOT re-decided. No work file edited.

## Changed rows (18)

All eighteen labels/kinds/confirmed_by are correct — L2 D20 (storage sites MainFragment.java:162 TorrentListItem, DetailTorrentTrackersFragment.java:183 TrackerItem, FeedFragment.java:142 FeedChannelItem, plus Parcel.java:2894 `getField("CREATOR")` in greps/L2/Parcel_8.1_readParcelableCreator_excerpt.txt), L2 D19 (array greps 0), L1 (hashCode/toString full-scope greps), and R5 (TorrentInfo.java:125 inside 30/2; TorrentInfo.java:155 inside 30/10; TorrentStateCode.java:71 inside 30/16 — all verified in corpus). Every one FAILs on stale prose only; each work row's evidence cell still carries its pre-flip operative conclusion, quoted below.

- 30/2 TorrentInfo.\<init\>(Parcel) — REACHABLE SOURCE — FAIL-prose. Stale: "Stays OPEN". (D20 + D5b: caller TorrentInfo$1.createFromParcel (30/12) REACHABLE on the TorrentListItem storage site; ctor call site printed in the CREATOR body TorrentInfo.java:175-177.)
- 30/6 TorrentInfo.describeContents — REACHABLE INFERRED — FAIL-prose. Stale: "Stays OPEN". (D20: TorrentListItem storage site + Parcel.java:2894.)
- 30/8 TorrentInfo.hashCode — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "Stays OPEN". (L1 full-scope greps zero.)
- 30/9 TorrentInfo.toString — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "Stays OPEN". (L1 full-scope greps zero.)
- 30/10 TorrentInfo.writeToParcel — REACHABLE INFERRED — FAIL-prose. Stale: "Stays OPEN". (D20, same site and framework print as 30/6.)
- 30/12 TorrentInfo$1.createFromParcel — REACHABLE INFERRED — FAIL-prose. Stale: "Stays OPEN". (D20; CREATOR body TorrentInfo.java:175-177.)
- 30/13 TorrentInfo$1.newArray — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "Stays OPEN". (D19; array_fields shows only the newArray return type at TorrentInfo.java:180, no field; storage site is not an array site, D5d.)
- 30/16 TorrentStateCode.fromValue — REACHABLE SOURCE — FAIL-prose. Stale: "Dependency rule: stays OPEN". (R5: caller TorrentInfo.java:125 inside now-REACHABLE Parcel ctor 30/2, verified in corpus. The row's own text adds "**It flips to REACHABLE if and only if the Parcel-ctor route is ever resolved" — that condition is now met.)
- 30/17 TorrentStateCode.value — REACHABLE SOURCE — FAIL-prose. Stale: "Dependency rule: stays OPEN, standing/falling with rows 10 and 16". (R5: callers TorrentInfo.java:155 inside now-REACHABLE writeToParcel 30/10 and TorrentStateCode.java:71 inside now-REACHABLE 30/16, both verified in corpus.)
- 30/19 TrackerInfo.\<init\>(Parcel) — REACHABLE SOURCE — FAIL-prose. Stale: "Stays OPEN". (D20 + D5b: caller TrackerInfo$1.createFromParcel (30/32) REACHABLE on the TrackerItem storage site; CREATOR body TrackerInfo.java:196-198.)
- 30/24 TrackerInfo.describeContents — REACHABLE INFERRED — FAIL-prose. Stale: "Stays OPEN". (D20: TrackerItem storage site + Parcel.java:2894.)
- 30/27 TrackerInfo.hashCode — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "Stays OPEN". (L1 full-scope greps zero.)
- 30/29 TrackerInfo.toString — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "Stays OPEN". (L1 full-scope greps zero.)
- 30/30 TrackerInfo.writeToParcel — REACHABLE INFERRED — FAIL-prose. Stale: "Stays OPEN". (D20, same site and framework print as 30/24.)
- 30/32 TrackerInfo$1.createFromParcel — REACHABLE INFERRED — FAIL-prose. Stale: "Stays OPEN". (D20; CREATOR body TrackerInfo.java:196-198.)
- 30/33 TrackerInfo$1.newArray — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "Stays OPEN". (D19; array_fields shows only the newArray return type at TrackerInfo.java:201, no field.)
- 30/37 FeedChannel.\<init\>(Parcel) — REACHABLE SOURCE — FAIL-prose. Stale: "Stays OPEN". (D20 + D5b: caller FeedChannel$1.createFromParcel (31/5) REACHABLE on the FeedChannelItem storage site; CREATOR body FeedChannel.java:108-111.)
- 30/39 FeedChannel.describeContents — REACHABLE INFERRED — FAIL-prose. Stale: "Stays OPEN". (D20: FeedChannelItem storage site + Parcel.java:2894.)

## Sample rows (6 sample-only)

- 30/1 TorrentInfo.\<clinit\> — REACHABLE INFERRED — PASS. Class init precedes first use: TorrentEngine.makeInfo:779/787 `new TorrentInfo(...)`; CREATOR field at TorrentInfo.java:173-183 runs at class init; JVM timing unprinted, hence INFERRED.
- 30/11 TorrentInfo$1.\<init\> — REACHABLE INFERRED — PASS. Anonymous Creator at TorrentInfo.java:173-183; field initializer runs at class init on first use (rows 3-4 route); same convention as batch 29 row 5.
- 30/21 TrackerInfo.\<init\>(AnnounceEntry) — REACHABLE SOURCE — PASS. TorrentDownloadImpl.getTrackerInfoList:904-905, reached via TorrentEngine.makeTrackerInfoList.
- 30/26 TrackerInfo.getMessageAndStatus — REACHABLE SOURCE — PASS. Called from the AnnounceEntry ctor itself, TrackerInfo.java:74; definition :88-145 (private).
- 30/31 TrackerInfo$1.\<init\> — REACHABLE INFERRED — PASS. Anonymous Creator at TrackerInfo.java:193-204; field initializer runs at class init on first use (row 21 route); same convention as row 11.
- 30/36 FeedChannel.\<clinit\> — REACHABLE INFERRED — PASS. Class init precedes first use: AddFeedViewModel.applyParams:173 `new FeedChannel(...)`; JVM timing unprinted, hence INFERRED.

Totals: checked 24 (18 changed + 6 sample-only) — PASS 6, FAIL-prose 18, FAIL-label 0.
