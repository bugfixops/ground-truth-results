# L2 verdicts — batch 21 (AddTorrentParams)

Scope: OPEN Parcelable-trio rows only. No marshalling site naming AddTorrentParams exists in the complete local corpus (greps/L2/grep_all_parcel_sites.txt, 80 parcel sites: the only putExtra/getParcelableExtra sites name FileManagerConfig, Uri, TagInfo, PreferenceActivityConfig, or primitive/String values).

| batch/row | method | old label | NEW label | confirmed_by | evidence (file:line or grep path) | revert condition |
| 21/36 | AddTorrentParams.<init>(Parcel) | OPEN | OPEN | — | verified, no change. Only printed caller is AddTorrentParams$1.createFromParcel (AddTorrentParams.java:112), i.e. batch 22/3, which stays OPEN (no marshalling site) — D5b dependency rule. | A printed marshalling site naming AddTorrentParams flips 22/3 to REACHABLE, and 21/36 then follows to REACHABLE SOURCE via the :112 call site. |
| 21/38 | AddTorrentParams.describeContents | OPEN | OPEN | — | verified, no change. Definition AddTorrentParams.java:91-93 only; zero marshalling sites naming this class in greps/L2/grep_all_parcel_sites.txt. CREATOR definition alone is not a caller (D5a). | A printed marshalling site naming AddTorrentParams. |
