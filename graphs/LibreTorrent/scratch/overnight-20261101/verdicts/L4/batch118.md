# L4 verdicts — batch 118 (D25 confirmation, no flips, no row changes)

D25 check performed as a negative sweep, not a per-row flip: zero `SDK_INT` / `Build.VERSION` hits
in all six batch-118 source files in the complete local corpus (SchedulingSettingsFragment,
StorageSettingsFragment, StreamingSettingsFragment, AddTagButton, SelectTagActivity,
SelectTagDialog) — saved grep grep_D25_batch118_SDK.txt, 0 lines. No batch-118 row is
API-gated on its own file, and no Appearance/TorrentNotifier gate coupling reaches any
batch-118 row. No row changes under D25.

| batch/row | method | old label | NEW label | confirmed_by | evidence | revert condition |
| 118/all | (D25 SDK sweep — no row changed) | — | — | — | verified, no change — grep_D25_batch118_SDK.txt, 0 lines across the six batch-118 source files | A printed SDK-gated call site for a batch-118 row |
