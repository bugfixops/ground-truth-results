# LibreTorrent batch 120 helper report

Membership source: `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, batch 120 only. Exact plan count: 3.

Summary: 0 REACHABLE, 0 UNREACHABLE, 3 OPEN. TorrentTagsList source shows local listener registration, list submission, and chip close-icon callback logic. The source search found two listener-registration callers, but did not establish complete host entry paths or every callback chain. Keep all OPEN.

| Plan row | JVM method | Descriptor | Status | Reason |
|---:|---|---|---|---|
| 1 | `TorrentTagsList.lambda$buildChip$0` | `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;Landroid/view/View;)V` | OPEN | Local implementation and listener setup are visible; full host-entry and callback chain was not verified for each target. |
| 2 | `TorrentTagsList.setListener` | `(Lorg/proninyaroslav/libretorrent/ui/tag/TorrentTagsList$Listener;)V` | OPEN | Local implementation and listener setup are visible; full host-entry and callback chain was not verified for each target. |
| 3 | `TorrentTagsList.submit` | `(Ljava/util/List;)V` | OPEN | Local implementation and listener setup are visible; full host-entry and callback chain was not verified for each target. |

## Evidence
- `TorrentTagsList.java:18-52`: custom ChipGroup; constructors call init; setListener and submit.
- `TorrentTagsList.java:54-86`: chip creation; close icon invokes listener when non-null; add button likewise.
- Source search found `setListener` callers in `DetailTorrentInfoFragment.java:112` and `AddTorrentInfoFragment.java:120`.

