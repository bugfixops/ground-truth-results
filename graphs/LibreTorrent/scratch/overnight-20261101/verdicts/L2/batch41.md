# L2 verdicts — batch 41 (TorrentStream trio rows)

Checked: batch 41 contains NO OPEN Parcelable-trio rows. TorrentStream trio rows are already closed in the merge-ready file and are verified, no change: 41/31 <init>(Parcel) UNREACHABLE INFERRED, 41/34 describeContents UNREACHABLE INFERRED, 41/38 writeToParcel UNREACHABLE INFERRED, 41/40 $1.createFromParcel UNREACHABLE INFERRED, 41/39 $1.<init> REACHABLE INFERRED (class-init row, not an OPEN row). No verdict lines, no flips in this batch.

| batch/row | method | old label | NEW label | confirmed_by | evidence (file:line or grep path) | revert condition |
| — | (no OPEN trio rows in batch 41) | — | — | — | verified, no change | — |
