# Spot-check — batch 31 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json, plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). Rows 1 and 6 are in both sets; checked once, under Changed. Verdicts D1–D36/R1–R5 are NOT re-decided. No work file edited.

## Changed rows (12)

All twelve labels/kinds/confirmed_by are correct — L2 D20 (FeedChannelItem storage site FeedFragment.java:142 + Parcel.java:2894), L2 D19 (array greps 0), L1 (hashCode/toString full-scope greps). Every one FAILs on stale prose only.

- 31/1 FeedChannel.hashCode — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "Stays OPEN". (L1: definition FeedChannel.java:121-124; no printed hash-collection use of a FeedChannel.)
- 31/2 FeedChannel.toString — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "Stays OPEN". (L1 full-scope greps zero.)
- 31/3 FeedChannel.writeToParcel — REACHABLE INFERRED — FAIL-prose. Stale: "Parcelable-trio policy: stays OPEN". (D20: FeedChannelItem storage site + Parcel.java:2894.)
- 31/5 FeedChannel$1.createFromParcel — REACHABLE INFERRED — FAIL-prose. Stale: "Stays OPEN". (D20; CREATOR body FeedChannel.java:108-111.)
- 31/6 FeedChannel$1.newArray — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "Stays OPEN". (D19; array_fields shows only the newArray return type at FeedChannel.java:114, no field; storage site is not an array site, D5d.)
- 31/13 FeedItem.hashCode — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "Stays OPEN". (L1 full-scope greps zero.)
- 31/14 FeedItem.toString — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "Stays OPEN". (L1 full-scope greps zero.)
- 31/18 FeedItem$1.newArray — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "Stays OPEN". (D19; array_fields shows only the newArray return type at FeedItem.java:124, no field.)
- 31/25 TagInfo.toString — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "Stays OPEN". (L1: the only `+ tags` sites are inside the 30/9 and 21/40 bodies, both UNREACHABLE; the only `info` concats are the 10/40 and 11/8 bodies, both UNREACHABLE — dependency consistency verified in L1_SUMMARY.)
- 31/29 TagInfo$1.newArray — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "Stays OPEN". (D19; array_fields shows only the newArray return type at TagInfo.java:76-78, no field; the TagInfo round trip parcels single objects only, never an array.)
- 31/37 Torrent.hashCode — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "Stays OPEN". (L1 full-scope greps zero.)
- 31/40 Torrent.toString — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "Stays OPEN". (L1 full-scope greps zero; follows host 90/16's UNREACHABLE status as a dependent, with no independent trigger.)

## Sample rows (6 sample-only)

- 31/11 FeedItem.describeContents — OPEN — PASS. Definition FeedItem.java:96-99; framework marshalling only, no printed parcel site. OPEN confirmed_by is —, as required.
- 31/16 FeedItem$1.\<init\> — REACHABLE INFERRED — PASS. Anonymous Creator at FeedItem.java:114-128; field initializer runs at class init on first use (row 8 route); row flags the correction vs the prior proposal (which left this OPEN) under the same Creator-$1.\<init\> convention as row 4.
- 31/21 TagInfo.\<init\>(Parcel) — REACHABLE SOURCE — PASS. Definition TagInfo.java:51-55; the cell's final substantive statement is the GREPFAMILY FLIP 2026-11-01 (unparcel sites now printed: DetailTorrentInfoFragment getParcelableExtra(TAG_RESULT_SELECTED_TAG) and AddTorrentInfoFragment same), which supersedes the earlier "Stays OPEN" history sentence in the same cell. Contrast Phase 3 flips, where only a bare "verdict applied" note was appended.
- 31/26 TagInfo.writeToParcel — REACHABLE INFERRED — PASS. Definition TagInfo.java:63-67; the cell's final substantive statement is the GREPFAMILY FLIP 2026-11-01 (parcel sites printed: SelectTagDialog putExtra item.info, etc.), superseding the earlier "Stays OPEN" history sentence in the same cell.
- 31/31 Torrent.\<init\>(Parcel) — OPEN — PASS. Definition Torrent.java:104-117; only printed caller is its own CREATOR.createFromParcel:160-163, itself OPEN (32/3) — dependency premise unchanged by Phase 3. OPEN confirmed_by is —, as required.
- 31/36 Torrent.getMagnet — REACHABLE SOURCE — PASS. TorrentSessionImpl restore path :413-415 (loadTask.putMagnet(torrent.getMagnet(), …)); definition Torrent.java:124-127.

Totals: checked 18 (12 changed + 6 sample-only) — PASS 6, FAIL-prose 12, FAIL-label 0.
