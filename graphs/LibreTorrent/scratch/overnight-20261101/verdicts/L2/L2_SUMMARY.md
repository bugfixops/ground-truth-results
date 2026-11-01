# L2 Summary — Parcelable trios (D5/D19/D20/D21/D22/D33)

## Parcel.java print outcome (D20) — CONFIRMED, getField

Fetched via the GitHub connector (no token) from branch work-2026-10-31, repo bugfixops/ground-truth-results, path `fw_src/android-8.1.0_r1/core/java/android/os/Parcel.java` (the task's `frameworks/base/...` path does not exist in this repo; the flattened layout is `core/java/android/os/Parcel.java`). File: 3,229 lines, blob SHA fae9d5310f8ed81c2813bcf56755e853c28eed74. Exact lookup call, line 2894, inside `readParcelableCreator(ClassLoader)` (lines 2867-2911, excerpt saved at greps/L2/Parcel_8.1_readParcelableCreator_excerpt.txt):

`Field f = parcelableClass.getField("CREATOR");`

`getField` is inherited-field lookup, so a subclass storage site IS a marshalling site for the base class's parcel methods — but only where the subclass defines no own CREATOR. That condition holds for TorrentInfo (via TorrentListItem), TrackerInfo (via TrackerItem), and FeedChannel (via FeedChannelItem), and FAILS for FileItem (via TorrentContentFileItem, which defines its own CREATOR and its own describeContents override). See batch73.md for the failed premise.

## Totals

- Rows judged (OPEN trio rows in batches 21, 22, 28, 29, 30, 31, 32, 41, 42, 73, 82, 114, plus 102/17 and 92/39): **77**
- Flips: **33** — 15 to REACHABLE, 18 to UNREACHABLE
- Staying OPEN: **44**
- Batches 41 and 42 contain zero OPEN trio rows (already closed; verified, no change).

## Flips to REACHABLE (15)

- D20 inherited CREATOR (INFERRED, storage site + Parcel.java:2894): 30/6, 30/10, 30/12 (TorrentInfo, MainFragment.java:162); 30/24, 30/30, 30/32 (TrackerInfo, DetailTorrentTrackersFragment.java:183); 30/39, 31/3, 31/5 (FeedChannel, FeedFragment.java:142).
- D20 + D5b positive direction, Parcel ctor SOURCE via printed CREATOR-body call site: 30/2 (caller 30/12), 30/19 (caller 30/32), 30/37 (caller 31/5).
- D22 $1.<init> INFERRED on printed first use on a REACHABLE route: 32/2 (Torrent; TorrentEngine.java:351/:412 → session.addTorrent → TorrentSessionImpl.java:263 `new Torrent`), 32/22 (BencodeFileItem; Utils.java:145 `new BencodeFileItem` via TorrentMetaInfo.java:108 from REACHABLE-proposed 32/29), 32/37 (TorrentMetaInfo; TorrentDownloadImpl.java:406/:1194 and TorrentEngine.java:464, REACHABLE-proposed 32/29/32/30).

## Flips to UNREACHABLE, kind `no_trigger_in_app`, INFERRED (18, all D19)

22/4, 28/33, 29/7, 29/22, 29/40, 30/13, 30/33, 31/6, 31/18, 31/29, 32/4, 32/24, 32/39, 73/36, 82/17, 114/27, 102/17, 92/39. D19 evidence (saved greps, complete local corpus of 301 Java files): (i) zero array-extra APIs — greps/L2/grep_array_apis.txt 0 lines, grep_array_apis2.txt 0 lines; (ii) zero Parcelable[]-typed fields/state — grep_parcelable_array_type.txt 0 lines, grep_array_fields.txt hits are only newArray return types, never fields; (iii) no Bundle/array parcel path names any of these classes — grep_all_parcel_sites.txt (80 sites: single extras, Uri, TagInfo, FileManagerConfig, PreferenceActivityConfig, list-state Parcelables, and internal readTypedList/writeTypedList list paths, which never call newArray). Revert condition for each: a printed array site naming that class, or a printed Parcelable[] field/state for it (plus, for storage classes, a printed androidx ParcelableStorage body showing newArray dispatch).

## Staying OPEN (44) with the specific missing site each

- No marshalling site naming the class: 21/38 (AddTorrentParams describeContents); 22/1 (writeToParcel), 22/3 (createFromParcel); 28/26, 28/30 (AdvancedTorrentInfo); 28/37 (MagnetInfo describeContents); 29/4, 29/14, 29/19 (MagnetInfo/PeerInfo write/describe); 29/6, 29/21, 29/39 (createFromParcel, MagnetInfo/PeerInfo/SessionStats); 29/33, 29/37 (SessionStats); 31/11, 31/15 (FeedItem); 31/34 (Torrent describeContents); 32/1, 32/13, 32/31, 32/36 (Torrent/BencodeFileItem/TorrentMetaInfo write/describe); 82/12, 82/14 (DownloadableFileItem).
- Dependency on an OPEN createFromParcel (D5b): 21/36 (caller 22/3 OPEN); 28/19 (subclass Parcel ctors → OPEN createFromParcels); 28/21 (subclass writeToParcels OPEN); 28/23 (caller 28/32 OPEN); 28/35 (caller 29/6 OPEN); 29/9 (caller 29/21 OPEN); 29/31 (caller 29/39 OPEN); 31/9 (caller 31/17 OPEN); 31/31 (caller 32/3 OPEN); 32/10 (callers 32/23, 32/26 OPEN); 32/21 (via 32/36 OPEN); 32/26 (caller 32/38 OPEN); 82/10 (caller 82/16 OPEN); 32/3, 32/23, 32/38 (createFromParcel rows themselves, framework dispatch only, no unparcel site); 31/17 (FeedItem createFromParcel, no unparcel site).
- D20 premise failed (subclass owns its CREATOR/describeContents): 73/29, 73/35 — resolver is a printed parcel site for a plain FileItem, not a subclass instance.

## Explicit checks requested in the brief

- **22/1 is AddTorrentParams.writeToParcel, NOT a $1.<init> row** — D22 does not apply to it; it stays OPEN (no marshalling site). 22/2 ($1.<init>) is already REACHABLE INFERRED in the merge-ready file and was not re-verdicted.
- **21/36 vs 22/3 (D5b step 2)**: 22/3 stays OPEN (no marshalling site for AddTorrentParams), so 21/36 stays OPEN with it — the dependency direction held, no flip either way.
- **D21 confirmation (no flips)**: 31/20, 31/22 stand REACHABLE SOURCE on printed `new TagInfo` sites (AddTagViewModel:61/:59); 31/21 stands REACHABLE SOURCE via its REACHABLE createFromParcel caller 31/28 on the printed TagInfo round trip. Entity status was not the basis for any of the three — confirmed from the batch-31 file.
- **Out of scope, untouched**: 21/39, 21/40 (hashCode/toString); 28/18 (plain ctor); 114/22, 114/23 (plain setters); already-REACHABLE $1.<init> rows (22/2, 28/31, 29/5, 29/20, 29/38, 30/11, 30/31, 31/4, 31/16, 31/27, 73/34, 82/15); already-closed batch 41/42 trio rows.

## Premises that failed

1. D20 for FileItem: TorrentContentFileItem defines its own CREATOR (TorrentContentFileItem.java:72-85) and overrides describeContents (:57-60, no super call), so the base FileItem CREATOR/describeContents never run on the storage path. 73/29 and 73/35 stay OPEN; only 73/36 moves (D19 UNREACHABLE). Already-REACHABLE 73/27/73/33 stand on printed super-calls, unaffected.
2. The brief's `frameworks/base/...` Parcel.java path does not exist in this repo; the actual path is `fw_src/android-8.1.0_r1/core/java/android/os/Parcel.java`. The print itself was obtained and confirms getField.

## Follow-up correction received (bind:/app: namespaces) — not applicable to L2

The parent's correction (check BOTH `bind:` AND `app:` attributes, plus any other namespace prefix, in every `<include>` element) concerns databinding include pass-through greps. L2's greps contain no `<include>`/databinding checks at all (parcel sites, array APIs, storage sites only), so no L2 grep needed widening; recorded in greps/L2/note_bind_app_correction.txt. No verdict in this group depends on an include pass-through.

## Blockers

None. No 429 was hit (connector fetches one at a time with ~30 s pauses; Parcel.java fetched successfully). No pushes made, no branch edits made, no tick markers written, and no files written outside phase3/verdicts/L2/ and phase3/greps/L2/. All labels are from printed source or the saved greps cited; confirmed_by uses only SOURCE/INFERRED, OPEN rows use —; no row flips on CREATOR definition alone, on entity status alone, or on a single-extra site for newArray.
