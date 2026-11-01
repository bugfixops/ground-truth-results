# Spot-check — batch 32 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json, plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). Verdicts D1–D36/R1–R5 are NOT re-decided. No work file edited.

## Changed rows (11)

All eleven PASS: label, kind, confirmed_by match the verdict, and the work prose contains no stays-OPEN / NOT-UNREACHABLE sentence (the Phase 3 note is appended; the prose states the definition and the no-caller / no-invocation position, which is consistent with the verdict basis, not a contradiction of it).

- 32/2 Torrent$1.\<init\> — REACHABLE INFERRED — PASS. L2 D22: TorrentEngine.java:351 and :412 → session.addTorrent → TorrentSessionImpl.java:263 `new Torrent` (corpus lines verified: TorrentSessionImpl:263 `Torrent torrent = new Torrent(`); class init runs the CREATOR field initializer (Torrent.java:157). Dependency rows 32/29 and 32/30 are REACHABLE in current work, as the D22 premise requires for the sibling rows.
- 32/4 Torrent$1.newArray — UNREACHABLE no_trigger_in_app INFERRED — PASS. L2 D19 (array greps 0; array_fields shows only the newArray return type at Torrent.java:166, no field).
- 32/7 TorrentTagInfo.hashCode — UNREACHABLE no_trigger_in_app INFERRED — PASS. L1 (definition TorrentTagInfo.java:74; no printed caller; full-scope greps zero).
- 32/8 TorrentTagInfo.toString — UNREACHABLE no_trigger_in_app INFERRED — PASS. L1 (definition TorrentTagInfo.java:82; no printed caller; full-scope greps zero).
- 32/20 BencodeFileItem.toString — UNREACHABLE no_trigger_in_app INFERRED — PASS. L1 (definition BencodeFileItem.java:119; no printed caller; full-scope greps zero).
- 32/22 BencodeFileItem$1.\<init\> — REACHABLE INFERRED — PASS. L2 D22: Utils.getFileList constructs `new BencodeFileItem(...)` at Utils.java:145 (verified in corpus), called from the TorrentMetaInfo(TorrentInfo) ctor at TorrentMetaInfo.java:108, itself REACHABLE in current work (32/29); class init runs the CREATOR field initializer (BencodeFileItem.java:95).
- 32/24 BencodeFileItem$1.newArray — UNREACHABLE no_trigger_in_app INFERRED — PASS. L2 D19 (array_fields shows only the newArray return type at BencodeFileItem.java:105, no field; the TorrentMetaInfo readTypedList path is a list path, not an array path, and never calls newArray).
- 32/34 TorrentMetaInfo.hashCode — UNREACHABLE no_trigger_in_app INFERRED — PASS. L1 (definition TorrentMetaInfo.java:166; no printed caller; full-scope greps zero).
- 32/35 TorrentMetaInfo.toString — UNREACHABLE no_trigger_in_app INFERRED — PASS. L1 (definition TorrentMetaInfo.java:195; no printed caller; full-scope greps zero).
- 32/37 TorrentMetaInfo$1.\<init\> — REACHABLE INFERRED — PASS. L2 D22: TorrentDownloadImpl.java:406 and :1194 `new TorrentMetaInfo(ti)` (verified in corpus) and TorrentEngine.java:464 `new TorrentMetaInfo(bencode)` (verified in corpus); class init runs the CREATOR field initializer (TorrentMetaInfo.java:149).
- 32/39 TorrentMetaInfo$1.newArray — UNREACHABLE no_trigger_in_app INFERRED — PASS. L2 D19 (array_fields shows only the newArray return type at TorrentMetaInfo.java:159, no field).

## Sample rows (8)

- 32/1 Torrent.writeToParcel — OPEN — PASS. Torrent.java:142; no printed marshalling site for Torrent; premise unchanged by Phase 3 (the D20 storage sites name TorrentListItem/TrackerItem/FeedChannelItem, not Torrent). OPEN confirmed_by is —, as required.
- 32/6 TorrentTagInfo.equals — OPEN — PASS. TorrentTagInfo.java:63; no printed caller.
- 32/11 BencodeFileItem.\<init\>(String,int,long) — REACHABLE SOURCE — PASS. Utils.java:145 in getFileList():142.
- 32/16 BencodeFileItem.getSize — REACHABLE SOURCE — PASS. BencodeFileTreeUtils.java buildFileTree loop: file.getSize() (:102-103, fresh fetch).
- 32/21 BencodeFileItem.writeToParcel — OPEN — PASS. BencodeFileItem.java:88; only reachable via TorrentMetaInfo.writeToParcel, itself OPEN (32/36) — dependency premise unchanged by Phase 3. OPEN confirmed_by is —, as required.
- 32/26 TorrentMetaInfo.\<init\>(Parcel) — OPEN — PASS. TorrentMetaInfo.java:113; called only from CREATOR :153, not printed as invoked (32/38 OPEN). OPEN confirmed_by is —, as required.
- 32/31 TorrentMetaInfo.describeContents — OPEN — PASS. TorrentMetaInfo.java:129; no printed caller.
- 32/36 TorrentMetaInfo.writeToParcel — OPEN — PASS. TorrentMetaInfo.java:135; no printed marshalling site for TorrentMetaInfo. OPEN confirmed_by is —, as required.

Totals: checked 19 (11 changed + 8 sample-only) — PASS 19, FAIL-prose 0, FAIL-label 0.
