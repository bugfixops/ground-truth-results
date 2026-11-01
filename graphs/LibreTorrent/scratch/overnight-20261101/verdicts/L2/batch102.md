# L2 verdicts — batch 102 (FileManagerConfig newArray)

Scope: OPEN Parcelable-trio rows only. The rest of the FileManagerConfig trio (102/10 Parcel ctor, 102/12 describeContents, 102/14 writeToParcel, 102/16 createFromParcel) is already REACHABLE on the printed putExtra + getParcelableExtra round trip (CreateTorrentDialog:258-263/:268-273/:327-334 + FileManagerDialog:137) and is not re-verdicted here; 102/15 ($1.<init>) stands as in the file.

| batch/row | method | old label | NEW label | confirmed_by | evidence (file:line or grep path) | revert condition |
| 102/17 | FileManagerConfig$1.newArray | OPEN | UNREACHABLE | INFERRED | Kind: `no_trigger_in_app`. D19 all three tests pass (greps/L2/grep_array_apis.txt 0; grep_array_apis2.txt 0; grep_parcelable_array_type.txt 0; grep_array_fields.txt shows only the newArray return type at FileManagerConfig.java:102, no field). The FileManagerConfig round trip parcels single objects only, never an array. | A printed array site naming FileManagerConfig, or a printed Parcelable[] field/state for this class. |
