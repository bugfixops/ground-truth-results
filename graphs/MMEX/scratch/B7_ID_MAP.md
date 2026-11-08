# MMEX B7 ID map — old to new, complete

Scope: every retired edge id from the B6 fixes and the five
post-B6 implementations (routes 8+18, showPrerequisite guard,
§9 getContext repair, Sync re-feed v2, route 14 loader-id
partition), mapped to its successor id(s) in the final build —
or recorded honestly as having no direct replacement where the
edge was deleted without a 1:1 successor. No id was predicted:
every new id below was read from the final private build's
`mmex_trigger_graph.json` (build in `B7_RUN_LOG.md` section 2:
4270 methods, 3430 REACHABLE / 840 UNREACHABLE, 8441 edges),
and every retired id was confirmed absent from that JSON.

Method (mechanical): id-diff between the private stage-B6
rebuild's JSON (8256 edges; `B7_RUN_LOG.md` section 11) and
the final JSON (8441 edges), saved as
`helper/b7-run-scratch/id_diff.txt` (33 retired, 218 added),
plus a methods.csv diff, cross-checked against the audited
implementation verifications. "Retired" below means: present
in the stage-B6 JSON, absent from the final JSON — except
section 1 (retired before stage-B6) and the intermediate id
in section 3 (created after stage-B6, retired before final).

Landing order (decides every overlap; never silently union):

- stage-B6 (8256) -> routes 8+18 (+105) -> showPrerequisite
  guard (net 0: one retired, one added) -> §9 getContext
  (+2: -11 +13) -> Sync re-feed v2 (+48: -13 +22 hand +39
  auto) -> route 14 (+30: -2 +6 hand +26 auto) -> final
  (8441). Net: 8256 + 105 + 0 + 2 + 48 + 30 = 8441.
- Consequence: the §9 mirror id Eafb31232 is a retired id,
  not a final new id — §9 created it, Sync retired it (see
  section 3). Any list that unions "all new ids ever created"
  would wrongly resurrect it.

## 1. B6 set of 10 (FIX_REPORT section 8; KNOWN)

All 10 old ids are absent from the stage-B6 JSON and from the
final JSON (they were retired by the B6 fixes, before the
stage-B6 baseline). Their successors were established by the
B6 report and are all present in the final JSON (verified by
the grep in section 8 returning 0 for the old ids; the new
ids below were confirmed present in the final edge set).

| old_id | new_id | source |
|---|---|---|
| E1eb134bb | E0044db82 | FIX_REPORT §1 (D-G2 citation :45 to :43) |
| Ea42ef2c5 | Ecf182680 | FIX_REPORT §2 (D-G3 citation range) |
| E6ec96bae | E2732f4b0 | FIX_REPORT §4 (D-G7 auto to hand replacement) |
| E09ef97e5 | Eb1cc3582 | FIX_REPORT §5 (D-G8-1 basename citation) |
| E20641651 | Eab5e2ab6 | FIX_REPORT §5 (D-G8-1, R1-A) |
| E622960f9 | E10ea56a2 | FIX_REPORT §5 (D-G8-1, R1-B) |
| Edc464f1e | E57e26427 | FIX_REPORT §5 (D-G8-1) |
| E2e040e89 | Ee6b626ff | FIX_REPORT §5 (D-G8-1) |
| E68cc20fc | E06eb6eae | FIX_REPORT §5 (D-G8-1) |
| Ed981979e | E8c18509f | FIX_REPORT §5 (D-G8-1) |

B6 "unchanged" note (FIX_REPORT §8) does NOT carry past the
later implementations: E64d793d3 and Ed4e987ec, listed there
as unchanged by B6 alone, were retired by Sync (section 3).
The map applies the LATEST retirement for each id.

## 2. showPrerequisite guard (1 retired, 1 added)

| old_id | new_id | source |
|---|---|---|
| Ec1f84c25 | E00ecbc65 | `MainActivity.onCreate -> MainActivity.populateScheduledTransactions`, CALL; the hand replacement adds the `!showPrerequisite()` guard (MainActivity.java:184-187). Verified in the final JSON: same src/dst, guard as stated, evidence `SRC MainActivity.java:244 (bytecode)`. |

Blast check, measured on this run's two builds (not copied):
145 `methods.csv` rows contain Ec1f84c25 at stage-B6 and
145 contain E00ecbc65 at final, at the same position in each
route — exactly the design's figure. Final rows containing
Ec1f84c25: 0.

## 3. Sync re-feed v2 (13 retired, 22 hand added + 39 auto)

Retired set (Sync verification §3a, exact set, confirmed by
this run's id-diff):

| old_id | successor new id(s) | what it was |
|---|---|---|
| E29548d9f (D1) | Eb9acff04, E6d90f981, E6d4ca81c | `SyncService.enqueueWork -> SyncService.onHandleWork`, FRAMEWORK — replaced by the three variant FRAMEWORK edges (`enqueueWork@X -> onHandleWork@X`, X = SYNC/DOWNLOAD/UPLOAD) |
| Efb03dd01 (D2) | Ea16c654e | `SyncService.onHandleWork -> SyncService.triggerSync`, CALL — replaced by `onHandleWork@SYNC -> triggerSync` (only the SYNC variant feeds triggerSync; DOWNLOAD/UPLOAD go to sendMessage) |
| Ed4e987ec (D3) | Ef9b85498 | `SyncService.onHandleWork -> SyncService.sendMessage@DOWNLOAD`, CALL — replaced by `onHandleWork@DOWNLOAD -> sendMessage@DOWNLOAD` |
| E6b4ee715 (D4) | E6a4e9a81, Ecec101c7, E551eda55, Ecc770873 | `SyncService.onHandleWork -> SyncService.sendMessage@OTHER`, CALL — replaced by the four `@X -> sendMessage@OTHER` edges (verification A12 + A13; two distinct @UPLOAD texts exist, both listed) |
| E64d793d3 (D5) | Eced2f70b (plain branch) | `SyncManager.triggerSynchronization -> SyncManager.invokeSyncService`, CALL — replaced on the plain branch by `triggerSynchronization -> invokeSyncService@SYNC` (A1). The @MAIN branch's successor is R-S9a (next row), not D5's. |
| E0ec4b5c3 (D6) | E296a2f5e, Ea52c89b2, Efe7fefbc | `SyncManager.invokeSyncService -> SyncService.enqueueWork`, CALL — replaced by `invokeSyncService@X -> enqueueWork@X` (A4/A5/A6) |
| E41632c6b (D7) | E008a5c72 | `SyncService.enqueueWork -> SyncService.<init>`, FRAMEWORK — replaced by `enqueueWork@SYNC -> <init>` (A14; only the SYNC variant feeds `<init>`) |
| Eea45ec5e (D8) | E01ef8374, Eb135968e, E7d5c0349 | `SyncService.onHandleWork -> SyncService.onDestroy`, LIFECYCLE — replaced by `onHandleWork@X -> onDestroy` (A14, all three variants) |
| E47e8402f (F1) | E75720ed3 | `SyncServiceMessageHandler.handleMessage@DOWNLOAD -> SyncPreferenceFragment.onEvent`, ASYNC — rewritten delivery edge (guard/ENV/needs_state rewritten) |
| Ed79be682 (F2) | E81de3799 | `SyncServiceMessageHandler.handleMessage@DOWNLOAD -> MainActivity.onEvent(DbFileDownloadedEvent)`, ASYNC — rewritten. This resolves B7_PREP's conditional: F2 WAS rewritten, so Ed79be682 IS retired (it is in the stage-to-final retired set, and 0 hits in the CSV). |
| E0370fe54 (S1) | Eeda1de7b | `SyncManager.triggerDownload -> SyncManager.invokeSyncService`, auto CALL — replaced by `triggerDownload -> invokeSyncService@DOWNLOAD` (A2) |
| E11f48e0e (S2) | Efa2497dd | `SyncManager.triggerUpload -> SyncManager.invokeSyncService`, auto CALL — replaced by `triggerUpload -> invokeSyncService@UPLOAD` (A3) |
| Eafb31232 (R-S9a) | E0a520fac | §9 mirror `SyncManager.triggerSynchronization@MAIN -> SyncManager.invokeSyncService` (design-literal id, §9 verification §2) — retired by Sync's reconciliation and replaced by `triggerSynchronization@MAIN -> invokeSyncService@SYNC`. The final JSON's E0a520fac evidence states this verbatim: "reconciled Sync v2: dst retargeted to @SYNC (was plain invokeSyncService)". Eafb31232 is absent from both the stage-B6 JSON (created later) and the final JSON (retired later): the intermediate id. |

Full Sync hand-new list (22, all present in the final JSON):
A1 Eced2f70b, A2 Eeda1de7b, A3 Efa2497dd, A4 E296a2f5e,
A5 Ea52c89b2, A6 Efe7fefbc, A7 Eb9acff04, A8 E6d90f981,
A9 E6d4ca81c, A10 Ea16c654e, A11 Ef9b85498, A12 E6a4e9a81,
A13 Ecec101c7 (@SYNC) / E551eda55 (@DOWNLOAD) / Ecc770873
(@UPLOAD), A14 E008a5c72 (@SYNC to `<init>`) / E01ef8374
(@SYNC to onDestroy) / Eb135968e (@DOWNLOAD to onDestroy) /
E7d5c0349 (@UPLOAD to onDestroy), F1 E75720ed3, F2 E81de3799,
R-S9a E0a520fac. The 39 new auto fan-out ids (6 plain
`invokeSyncService` auto outs x 3 variants = 18, plus 7 plain
`onHandleWork` auto outs x 3 variants = 21) are additions
without a retired counterpart; they are in the measured added
set (`id_diff.txt`), not listed one by one here because no
retired id maps to them.

## 4. §9 getContext repair (11 retired, 13 added: 4 hand + 9 auto)

Retired set (§9 verification §2, exact set, confirmed by
this run's id-diff):

| old_id | successor | note |
|---|---|---|
| Edff47499 | — (no direct replacement) | Dead-end auto `MainActivity.showCurrentDatabasePath -> DatabaseManager.getDatabasePath`, suppressed. The caller keeps its other outs (3 to 2); getDatabasePath is now reached via the @MAIN segment (steps 4 to 7) and the plain re-assert below. |
| E66f6c096 | — (no direct replacement) | Dead-end auto `MmexApplication.createDbInstance -> getDatabasePath`, suppressed (caller 3 to 2). Same routing note as above. |
| Eeb18bb1a | — (no direct replacement) | Dead-end auto `MainActivity.onOpenDatabaseClick -> getDatabasePath`, suppressed (caller 3 to 2). |
| E48b9fe4d | — (no direct replacement) | Dead-end auto `DatabaseMetadataFactory.createDefaultEntry -> getDatabasePath`, suppressed (caller 12 to 11). |
| E86e7bbb2 | — (no direct replacement) | Dead-end auto `HomeFragment.createWelcomeView -> getDatabasePath`, suppressed (caller 4 to 3). |
| Ead13af17 | — (no direct replacement) | Dead-end auto `SyncManager.useDownloadedDatabase -> getDatabasePath`, suppressed (caller 11 to 10). |
| E930866bd | Efec640e8 | Auto `SyncManager.triggerSynchronization -> getDatabasePath`, suppressed and re-asserted as a plain-only hand edge with the same src/dst (present in the final JSON). |
| E3656f98a | E9af7d91f | Hand `MainActivity.initializeSync -> SyncManager.triggerSynchronization`, retargeted to `triggerSynchronization@MAIN` (trigger, guard, evidence otherwise character-identical, per §9 verification §8). |
| E9f9ccccc | — (no direct replacement) | Plain drawer-feeder auto `MainActivity.onDrawerMenuAndOptionMenuSelected -> triggerSynchronization`, suppressed by the @GROUP feeder's base pair. The @MAIN segment is fed only by the @GROUP feeder and initializeSync (verified: exactly 2 edges into `triggerSynchronization@MAIN` in the final JSON). |
| E1bb8c5b5 | Eaad801ab | @GROUP drawer-feeder auto `...@GROUP -> triggerSynchronization`, replaced by the @GROUP feeder to @MAIN. |
| E72da98f2 | — (no direct replacement) | @RECURRING drawer-feeder auto, suppressed as above (same base-pair side effect). |

Added set (13, §9 verification §2):

- Hand (4): E9af7d91f (edit, initializeSync to @MAIN),
  Eaad801ab (@GROUP feeder to @MAIN), Efec640e8 (plain
  re-assert to getDatabasePath), Eafb31232 (mirror @MAIN to
  plain invokeSyncService — INTERMEDIATE, retired by Sync;
  see section 3, R-S9a).
- Auto-mirrored @MAIN outs (9, all present in the final
  JSON): Ec88e7940 (to MmexApplication.<clinit>),
  E9f91fb2b (to SyncManager$1.<init>), Eb178e505 (to
  MmexApplication.getAmplitude), E531e5a96 (to
  SyncManager.getContext), E6dc2721a (to
  SyncManager.getRemotePath), E9e5d96b7 (to
  UIHelper.showToast(int)), E0016430a (to UIHelper.<init>),
  E2d998b18 (to DatabaseManager.<init>), Ec089d3dc (to
  SyncManager.isActive).

Of the 13, exactly 12 are present in the final JSON;
Eafb31232 is absent for the landing-order reason above.

## 5. Routes 8 + 18 (7 retired, 24 new variant-chain edges)

Retired:

| old_id | successor | note |
|---|---|---|
| E992e5393 | — (no direct replacement) | Repair 8 deletion: `FixerService.onContentDownloaded -> WatchlistFragment.onEvent(PriceDownloadedEvent)@RETURNED`, ASYNC (no subscriber on any Fixer prefix). The surviving route uses the untouched plain edges (Fixer to CurrencyListFragment Ed39837ab; Yahoo/Yql to Watchlist) — those are pre-existing edges, not replacements. |
| E887d2bcd | Ef2a5a02c (surviving plain edge, NOT a re-issue) | Repair 8 consequence: `@RETURNED -> WatchlistFragment.onPriceDownloaded` auto fan-out disappears with the @RETURNED node. The plain edge `WatchlistFragment.onEvent(PriceDownloadedEvent) -> onPriceDownloaded` (Ef2a5a02c) is present in BOTH the stage-B6 and final JSONs — it is the surviving route, not a new id. Recorded here so the retired id is not mistaken for still-live, and the plain id is not mistaken for its re-issue. |
| E282384e2 (D18-5) | E3693b7b2, Ea84ca658, Edf1db545, E4923a252 | Repair 18 deletion: plain RESULT `CalculatorActivity.returnResult -> InvestmentTransactionEditActivity.onActivityResult` (visit-agnostic edge), replaced by the four variant RESULT edges (one per launcher, see chain table). |
| Eb5fb7cfc (D18-1) | E9ab6a99b | Plain INTENT `InvestmentTransactionEditActivity.onNumSharesClick -> CalculatorActivity.<init>` (design graph_def.py:2197-2199), extracted from the stage-B6 JSON by (src, dst, INTENT) match — the design names the location but not the id. Replaced by the NUM_SHARES feeder. |
| Ea57d372e (D18-2) | E6fa886d0 | Plain INTENT `...onPurchasePriceClick -> CalculatorActivity.<init>` (design :2201-2204), same extraction. Replaced by the PURCHASE_PRICE feeder. |
| Ef5c42e03 (D18-3) | E221227c4 | Plain INTENT `...onCommissionClick -> CalculatorActivity.<init>` (design :2206-2208), same extraction. Replaced by the COMMISSION feeder. |
| E8e2b2862 (D18-4) | E8cacd7e4 | Plain INTENT `...onCurrentPriceClick -> CalculatorActivity.<init>` (design :2210-2212), same extraction. Replaced by the CURRENT_PRICE feeder. |

New variant chains (24, all present in the final JSON, all
in the measured added set; RESULT ids match the routes 8+18
verification §3):

| variant | feeder (click to `<init>@X`, INTENT) | `<init>@X` to `onCreate@X` (LIFECYCLE) | `onCreate@X` to `S_CALCULATOR@X` (ENTERS) | `S_CALCULATOR@X` to `onEqualsClicked@X` (GUI) | `onEqualsClicked@X` to `returnResult@X` (CALL) | `returnResult@X` to `onActivityResult@X` (RESULT) |
|---|---|---|---|---|---|---|
| NUM_SHARES | E9ab6a99b | E527238f3 | E2fc98a0a | E47180ee9 | E4398d20a | E3693b7b2 |
| PURCHASE_PRICE | E6fa886d0 | E77a022e3 | E80cc6efc | Efa1cd0b5 | Ee9bdfa0a | Ea84ca658 |
| COMMISSION | E221227c4 | E3266122b | Edc2150de | E0e8cd4a3 | E2695f7ee | Edf1db545 |
| CURRENT_PRICE | E8cacd7e4 | Edcfd73ae | Ebdca339a | E7d3e6434 | Ecc865121 | E4923a252 |

## 6. Route 14 loader-id partition (2 retired, 6 hand + 26 auto)

| old_id | successor | note |
|---|---|---|
| Ef9d523dd | Ef27e0542 (plus the full 6-edge chain below) | Deleted plain hand FRAMEWORK `IncomeVsExpensesListFragment.onLoadFinished -> IncomeVsExpensesListFragment$1.run`. Its functional successor is the chain's final edge `onLoadFinished@REPORT -> $1.run` (Ef27e0542), the sole incoming edge of `$1.run` in the final JSON. |
| E3a19df72 | E428631c7 | Suppressed plain auto CALL `onLoadFinished -> startLoader` (suppression via R14-3's base pair; no separate `sup()` call). Its functional successor is `onLoadFinished@YEARS -> startLoader@YEARS` (E428631c7), the sole incoming edge of `startLoader@YEARS`. |

Full new hand chain (6, all present in the final JSON,
route-14 verification §4):

| edge | id | kind |
|---|---|---|
| R14-1 `onActivityCreated -> onCreateLoader@YEARS` | Ebfbf7e82 | FRAMEWORK |
| R14-2 `onCreateLoader@YEARS -> onLoadFinished@YEARS` | E6df1962a | FRAMEWORK |
| R14-3 `onLoadFinished@YEARS -> startLoader@YEARS` | E428631c7 | CALL |
| R14-4 `startLoader@YEARS -> onCreateLoader@REPORT` | Ed2e1013e | FRAMEWORK |
| R14-5 `onCreateLoader@REPORT -> onLoadFinished@REPORT` | E645f3932 | FRAMEWORK |
| R14-6 `onLoadFinished@REPORT -> $1.run` | Ef27e0542 | FRAMEWORK |

The 26 new auto fan-out ids (11 each from
`onCreateLoader@YEARS` and `onCreateLoader@REPORT`, 2 each
from `onLoadFinished@YEARS` and `onLoadFinished@REPORT`)
are additions without a retired counterpart; they are in the
measured added set (`id_diff.txt`).

## 7. Metadata shifts in the combined stage-to-final methods diff

Full diff: 4270 methods, same set, 0 verdict flips, 291
methods with any column diff, 255 with a `route_edge_ids`
diff (including the 145 showPrerequisite swap rows), 41
with a `steps_from_launch` diff, 69 with an `incoming_edges` count
diff. Saved in full as
`helper/b7-run-scratch/methods_diff.txt`
(`incoming_edges` is a COUNT column; figures below are
count values).

- `confirmed_by` diffs (6 total): the §9 M3 five,
  SOURCE to INFERRED — DatabaseManager.getContext,
  getDbExternalStorageDirectory, getDefaultDatabaseDirectory,
  getExternalFilesDirectory, getPackageDirectory (the
  FileStorageHelper-prefix tail; build totals move SOURCE
  1499 to 1495 and INFERRED 2771 to 2775 across the whole
  run, with the sixth change below explaining the remaining
  step: 1499 + 1 (8+18) - 5 (§9) = 1495) — plus
  Calculator.getAmountFromResult, INFERRED to SOURCE (the
  8+18 variant chain gives it a source-evidenced route).
  No other `confirmed_by` change exists.
- §9 incoming counts (12 in §9's own accounting, relative
  to its 8361-edge baseline): the 10 @MAIN-out dsts each gain
  one (9 auto outs + the hand-mirror dst invokeSyncService)
  + getDatabasePath 8 to 2 + triggerSynchronization 5 to 3.
  In the combined diff the same dsts show aggregated deltas
  (e.g. SyncManager.getContext 10 to 14 = §9 +1 and Sync +3;
  SyncManager.getRemotePath 7 to 11 likewise; MmexApplication
  .<clinit> 59 to 64 = +4 from 8+18 fan-out and +1 from §9,
  against §9's own 63 to 64).
- Sync's 6 count-only rows (+3 each, relative to Sync's
  8363-edge baseline): NetworkUtils.<init>,
  NetworkUtils.isOnline(), RecentDatabasesProvider.get,
  RecentDatabasesProvider.getCurrent (all four appear
  count-only +3 in the combined diff too),
  SyncManager.getContext, SyncManager.getRemotePath (both
  appear in the combined diff at +4 with a route change,
  because §9 also touched them — see above).
- Route 14's 15 count-only rows (+2 each, relative to its
  8411-edge baseline): the 11 onCreateLoader auto targets
  (MmxCursorLoader.<init>(Context,Uri,Select),
  Dataset.getSource, Dataset.getUri,
  QueryReportIncomeVsExpenses.<init>,
  QueryReportIncomeVsExpenses.getAllColumns,
  SQLDataSet.<init>, ViewMobileData.<init>,
  Select.<init>(), Select.<init>(String[]),
  Select.orderBy, Select.where(String)) + 4 fragment rows
  (IncomeVsExpensesListFragment.onCreateLoader,
  onLoadFinished, updateListViewFooter, $1.<init>). In the
  combined diff, 14 of the 15 appear count-only +2;
  Dataset.getUri keeps its +2 count but its route also
  carries the showPrerequisite swap (Ec1f84c25 to
  E00ecbc65) — a different implementation's change on the
  same row, not a route-14 change.
- Step-count diffs (41) are all explained by the five
  implementations (route-14 $1.run 11 to 14; 8+18
  onActivityResult 15 to 25 and the show/set methods +3/+2;
  §9 getContext 8 to 12 and the tail +4; Sync onEvent rows
  10 to 11; showPrereq AppSettings.getPreferences 7 to 8,
  matching final-table route 29's 8 steps). No step change
  is unexplained, and no step change implies a label change
  (0 flips).

Rule for the reader: per-package figures are relative to
each package's landing baseline and must NOT be added
together; the combined stage-to-final diff is the
authoritative B7 record, and the per-package figures are
cited only to explain it.

## 8. Grep evidence: every retired id in verification.csv = 0 hits

44 ids grepped (10 B6 + 33 stage-to-final + 1
intermediate), `grep -F -c` per id over
`helper/b7-run/verification.csv` (900 rows), verbatim
output (exit status 1 on the last id is grep's "no lines
selected" for a zero count, not an error — every count
printed 0):

```
E1eb134bb: 0
Ea42ef2c5: 0
E6ec96bae: 0
E09ef97e5: 0
E20641651: 0
E622960f9: 0
Edc464f1e: 0
E2e040e89: 0
E68cc20fc: 0
Ed981979e: 0
E0370fe54: 0
E0ec4b5c3: 0
E11f48e0e: 0
E1bb8c5b5: 0
E282384e2: 0
E29548d9f: 0
E3656f98a: 0
E3a19df72: 0
E41632c6b: 0
E47e8402f: 0
E48b9fe4d: 0
E64d793d3: 0
E66f6c096: 0
E6b4ee715: 0
E72da98f2: 0
E86e7bbb2: 0
E887d2bcd: 0
E8e2b2862: 0
E930866bd: 0
E992e5393: 0
E9f9ccccc: 0
Ea57d372e: 0
Ead13af17: 0
Eb5fb7cfc: 0
Ec1f84c25: 0
Ed4e987ec: 0
Ed79be682: 0
Edff47499: 0
Eea45ec5e: 0
Eeb18bb1a: 0
Ef5c42e03: 0
Ef9d523dd: 0
Efb03dd01: 0
Eafb31232: 0
```

Cross-checks on the JSONs (mechanical, same run): all 33
stage-to-final retired ids are present in the stage-B6 JSON
(33/33) and absent from the final JSON (0/33); all 10 B6
ids are absent from both JSONs; Eafb31232 is absent from
both JSONs (intermediate, as stated). Total hits in the
CSV: 0. No stale-row bug exists in this output.

## 9. Reconciliation arithmetic (closes exactly)

- Edge counts: stage-B6 8256 -> final 8441 = +185 net.
- Per-implementation net deltas: 8+18 +105, showPrerequisite
  0, §9 +2, Sync +48, route 14 +30. Sum: 185.
- Per-implementation gross retired: 7 + 1 + 11 + 13 + 2 = 34.
  Measured stage-to-final retired: 33. Difference: 1 =
  Eafb31232, which is in both §9's added set and Sync's
  retired set but in neither the stage-B6 nor the final
  JSON.
- Per-implementation gross added: 112 + 1 + 13 + 61 + 32 =
  219. Measured stage-to-final added: 218. Difference: 1 =
  the same Eafb31232.
- 8256 - 33 + 218 = 8441. The id-diff closes exactly; no
  edge appears or disappears unexplained.

Sources: FIX_REPORT.md §8; B7_PREP.md §2 (skeleton this map
completes); routes8-18-design/DESIGN.md (D18-1 to D18-5) and
routes8-18-verify/VERIFICATION.md; showprereq-verify/
VERIFICATION.md; getcontext32-verify/VERIFICATION.md (§2,
§7 M3); sync-v2-verify/VERIFICATION.md (§3a, §3b, §3f);
route14-verify/VERIFICATION.md (§3, §4, §6); merger
AGENT_NOTES.md (Sync re-feed v2 and route-14 sections).
