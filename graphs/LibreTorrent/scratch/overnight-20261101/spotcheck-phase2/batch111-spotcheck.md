# Stream A Phase 2 spot-check — batch 111

Source re-derived from already-fetched local copies only
(`~/workspace/b111112-src/`); no connector fetch was needed, no 429 hit.
The merge-ready file was NOT edited; no label was changed here.
Phase 1 label changes in this file's revision notes: none (labels
unchanged 40/0/0 vs the input proposal), so the checked set is the
sample rows 1, 6, 11, 16, 21, 26, 31, 36 only.

## Per-row verdicts

| Row | Method | Filed label / confirmed_by | Verdict | Printed evidence |
|---|---|---|---|---|
| 1 | MainFragment$3.\<init\> | REACHABLE / INFERRED | PASS | Field `actionModeCallback` declared MainFragment.java:457; callback registered via `startSupportActionMode(actionModeCallback)` at MainFragment.java:173 and :191. Framework creation of the anonymous callback is unprinted, hence INFERRED. |
| 6 | MainViewModel.\<init\> | REACHABLE / INFERRED | PASS | Constructor body MainViewModel.java:69-76; instantiation only via `provider.get(MainViewModel.class)` at MainFragment.java:132 (library dispatch, unprinted). |
| 11 | MainViewModel.getAllTorrentsInfoSingle | REACHABLE / SOURCE | PASS | MainFragment.java:335 `viewModel.getAllTorrentsInfoSingle()`. |
| 16 | MainViewModel.lambda$new$0 | REACHABLE / INFERRED | PASS | Search-filter field lambda MainViewModel.java:60-67; invoked as `searchFilter.test(state)` inside the row-15 lambda at MainViewModel.java:121, downstream of the Rx `.filter(...)` at MainFragment.java:291/:339 (Rx dispatch unprinted). |
| 21 | MainViewModel.observeTorrentsDeleted | REACHABLE / SOURCE | PASS | MainFragment.java:352 and MainActivity.java:446. |
| 26 | MainViewModel.restartForegroundNotification | REACHABLE / SOURCE | PASS | MainActivity.java:170 `viewModel.restartForegroundNotification()` inside the printed permission-grant callback body. |
| 31 | MainViewModel.setStatusFilter | REACHABLE / SOURCE | PASS | MainActivity.java:590 and :615. |
| 36 | MsgMainViewModel.observeTorrentDetailsClosed | REACHABLE / SOURCE | PASS | MainFragment.java:370 and MainActivity.java:442. |

## Totals

- Checked: 8 rows. PASS: 8. FAIL: 0.
- Proposed corrections: none.

## Notes

- Strict-entry caveat is as filed: MainActivity :182 `setContentView`
  and :184-185 `findFragmentById` are printed; only the
  `activity_main.xml` layout declaration is unprinted. Labels stand
  under the sibling-batch container convention; no convention was
  decided here.
- Build/sampler/C1: not run (not this task).
