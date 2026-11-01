# Spot-check — batch 29 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json, plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). Row 36 is in both sets; checked once, under Changed. Verdicts D1–D36/R1–R5 are NOT re-decided. No work file edited.

## Changed rows (10)

All ten labels/kinds/confirmed_by are correct per L1 (hashCode/toString full-scope greps) and L2 (D19 parcel-array greps); every one FAILs on stale prose only. In each work row the evidence cell's operative conclusion is the single sentence quoted.

- 29/2 MagnetInfo.hashCode — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "Stays OPEN".
- 29/3 MagnetInfo.toString — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "Stays OPEN".
- 29/7 MagnetInfo$1.newArray — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "Stays OPEN". (L2 D19: array greps 0; array_fields shows only the newArray return type at MagnetInfo.java:89, no field.)
- 29/17 PeerInfo.hashCode — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "Stays OPEN".
- 29/18 PeerInfo.toString — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "Stays OPEN".
- 29/22 PeerInfo$1.newArray — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "Stays OPEN". (L2 D19: array_fields shows only the newArray return type at PeerInfo.java:176, no field.)
- 29/28 ReadPieceInfo.toString — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "Stays OPEN".
- 29/35 SessionStats.hashCode — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "Stays OPEN".
- 29/36 SessionStats.toString — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "Stays OPEN". (Definition SessionStats.java:135-147; no printed logging/concatenation caller in the L1 greps.)
- 29/40 SessionStats$1.newArray — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose. Stale: "Stays OPEN". (L2 D19: array_fields shows only the newArray return type at SessionStats.java:89, no field.)

## Sample rows (7 sample-only)

- 29/1 MagnetInfo.getUri — OPEN — PASS. Definition MagnetInfo.java:95-98; grep of fetched files finds no getUri() caller (TorrentEngine uses getSha1hash(); AddTorrentViewModel uses getName()/getSha1hash()/getFilePriorities()). Printed-subset check only, not a full-repo grep — stated in the row, consistent with OPEN. OPEN confirmed_by is —, as required.
- 29/6 MagnetInfo$1.createFromParcel — OPEN — PASS. Definition MagnetInfo.java:82-86; framework dispatch only, no printed unparcel site for a MagnetInfo. OPEN confirmed_by is —, as required.
- 29/11 PeerInfo.\<init\>(AdvancedPeerInfo,TorrentStatus) — REACHABLE SOURCE — PASS. TorrentDownloadImpl.java:924 inside getPeerInfoList:911-929, reached via TorrentEngine.makePeerInfoList:872-881.
- 29/16 PeerInfo.getConnectionType — REACHABLE SOURCE — PASS. Called from the 2-arg ctor itself, PeerInfo.java:65; definition :108-120 (private).
- 29/21 PeerInfo$1.createFromParcel — OPEN — PASS. Definition PeerInfo.java:170-172; framework dispatch only, no printed unparcel site. OPEN confirmed_by is —, as required.
- 29/26 Priority.value — REACHABLE SOURCE — PASS. PriorityConverter.java:32-39 (static initialiser), :64 and :96; definition Priority.java:65-68.
- 29/31 SessionStats.\<init\>(Parcel) — OPEN — PASS. Definition SessionStats.java:48-58 (calls super(source) at :50); only printed caller is its own CREATOR.createFromParcel:82-86, itself OPEN (row 39) — dependency premise unchanged by Phase 3. OPEN confirmed_by is —, as required.

Totals: checked 17 (10 changed + 7 sample-only) — PASS 7, FAIL-prose 10, FAIL-label 0.
