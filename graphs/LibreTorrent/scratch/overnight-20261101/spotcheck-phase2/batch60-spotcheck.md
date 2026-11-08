# Batch 60 — Phase 2 spot-check (UNVERIFIED proposal check only; nothing merged, nothing pushed)

- Source file checked: `~/workspace/overnight/stream-A/work/batch60-merge-ready.md`
- Evidence base: already-fetched files only (`~/workspace/b596061-openclose-src/`, `~/workspace/b596061-openclose2-src/`).
  No connector fetch was needed; no 429; no missing file.
- Rows checked (16): sample 1, 6, 11, 16, 21, 26, 31, 36 + Phase 1c flips 10, 12, 18, 19, 20, 27, 28, 40
  (rows 11, 12, 26, 36 are both sample and flips; row 21 is the Sw600dpLand <clinit> sample row).
- Batch Counts verified mechanically from the label column AND against the Counts section: 28 REACHABLE / 6 UNREACHABLE / 6 OPEN
  (Phase 1c arithmetic holds: before 25/0/15; D4c 6 OPEN→UNREACHABLE, D4e 4 OPEN→REACHABLE, D4d 1 REACHABLE→OPEN = 28/6/6).
- Build/sampler/C1: not run (not this task).

## Per-row verdicts

| Row | Label in file | Verdict | Evidence (printed source) |
|-----|---------------|---------|---------------------------|
| 1 `AddTorrentInfoBindingImpl$4.onChange()V` | REACHABLE proposed INFERRED | PASS | Same count correspondence as batch-59 row 36, re-verified: add_torrent_info.xml has exactly 5 two-way `@{viewModel.mutableParams...}` bindings (:43, :101, :109, :116, :123) for plan $1-$5; route AddTorrentInfoFragment :93 inflate + :103 setViewModel, framework dispatch INFERRED. Revert condition (merger rejects inverse-listener identification → 59-61 $N flips revert together) recorded, not decided here. |
| 6 `DetailTorrentAppbarBindingImpl.<init>(DataBindingComponent,View)` | REACHABLE proposed INFERRED | PASS | DetailTorrentFragment.java:150 `DataBindingUtil.inflate(inflater, R.layout.fragment_detail_torrent, ...)` (verified); binding.appbar use at :171 `binding.appbar.toolbar.inflateMenu(...)` (verified); fragment_detail_torrent.xml:10-12 `<include layout="@layout/detail_torrent_appbar"/>` (verified). Generated mapper/included-binding creation unprinted, so INFERRED is correct. |
| 10 `DetailTorrentAppbarBindingImpl.invalidateAll()V` | REACHABLE proposed INFERRED | PASS* | Label matches Phase 1c D4e (base Impl created via row 6's path). *Conditional on D4e standing. Pre-flip "stays OPEN" sentence remains alongside the [APPLIED D4e] tag — text cleanup only. |
| 11 `DetailTorrentAppbarBindingImpl.onFieldChange(int,Object,int)Z` | UNREACHABLE proposed INFERRED `no_trigger_in_app` | PASS* | Label matches Phase 1c D4c option U. Evidence verified: base detail_torrent_appbar.xml has NO `<data>` block and NO `@{...}` expressions (grep count 0; Toolbar + TabLayout with static attributes only); git blob SHA verified exactly as 15c7cf4fd1ff1b26ec48c0c760936453cc58ab00; saved binding-callbacks grep reports setVariable 0 / onFieldChange 0 hits in the 252-file tree; parent include passes no variable (fragment_detail_torrent.xml:10-12 has no bind: attribute). *Conditional on D4c standing. (Line-count nit: the file says "29 lines", wc counts 28 newlines — the file's last line has no trailing newline, so 29 editor lines; content verified, not a failure.) |
| 12 `DetailTorrentAppbarBindingImpl.setVariable(int,Object)Z` | UNREACHABLE proposed INFERRED `no_trigger_in_app` | PASS* | Same D4c evidence as row 11: no variable declared, so the generated outer Impl has no variable to propagate to this included binding via setVariable. *Conditional on D4c standing. |
| 16 `DetailTorrentAppbarBindingLargeLandNotouchImpl.executeBindings()V` | REACHABLE proposed INFERRED | PASS* | Variant layout exists (res/layout-large-land-notouch/detail_torrent_appbar.xml, blob SHA be659cb60ff9d3b2df954eed6c1eb05a3415fa41 — verified exactly, byte-identical to the sw600dp variant); fragment include + :150 inflate verified (row 6). On a matching device the qualifier selection (framework dispatch, INFERRED) creates this variant Impl. *Conditional on convention (iv) (all-configurations reading); under a single fixed portrait-phone config this row reverts to OPEN per the file's own recorded revert condition — not decided here. |
| 18 `DetailTorrentAppbarBindingLargeLandNotouchImpl.invalidateAll()V` | REACHABLE proposed INFERRED | PASS* | D4e applied together with D4b (variant creation) as the Phase 1c note states; variant Impl creation path per row 16. *Conditional on D4e + convention (iv). Same stale "stays OPEN" text note. |
| 19 `DetailTorrentAppbarBindingLargeLandNotouchImpl.onFieldChange(int,Object,int)Z` | UNREACHABLE proposed INFERRED `no_trigger_in_app` | PASS* | Same D4c evidence as row 11, applied to the variant layout: variant file also has NO `<data>`/no `@{...}` (grep count 0) and the same blob SHA be659cb... (verified), so even on a matching device there is no observable for onFieldChange to fire on. *Conditional on D4c standing. (Same 36-vs-35 line-count note as row 11: trailing-newline counting; content verified.) |
| 20 `DetailTorrentAppbarBindingLargeLandNotouchImpl.setVariable(int,Object)Z` | UNREACHABLE proposed INFERRED `no_trigger_in_app` | PASS* | Same D4c evidence as row 19. *Conditional on D4c standing. |
| 21 `DetailTorrentAppbarBindingSw600dpLandImpl.<clinit>()V` | REACHABLE proposed INFERRED | PASS* | Variant layout exists (res/layout-sw600dp-land/detail_torrent_appbar.xml, blob SHA be659cb... verified exactly); fragment include + :150 inflate verified. Class initialisation on first active use of the variant Impl (generated, INFERRED). *Conditional on convention (iv), same revert condition as row 16. |
| 26 `DetailTorrentAppbarBindingSw600dpLandImpl.invalidateAll()V` | REACHABLE proposed INFERRED | PASS* | D4e + D4b as row 18, for the sw600dp variant. *Conditional on D4e + convention (iv). Same stale "stays OPEN" text note. |
| 27 `DetailTorrentAppbarBindingSw600dpLandImpl.onFieldChange(int,Object,int)Z` | UNREACHABLE proposed INFERRED `no_trigger_in_app` | PASS* | Same D4c evidence as row 19, for the sw600dp variant (same blob SHA, no `<data>`/no `@{...}`). *Conditional on D4c standing. |
| 28 `DetailTorrentAppbarBindingSw600dpLandImpl.setVariable(int,Object)Z` | UNREACHABLE proposed INFERRED `no_trigger_in_app` | PASS* | Same D4c evidence as row 27. *Conditional on D4c standing. |
| 31 `DialogAddFeedChannelBindingImpl.<clinit>()V` | REACHABLE proposed INFERRED | PASS | AddFeedDialog.java:202 `DataBindingUtil.inflate(i, R.layout.dialog_add_feed_channel, null, false)` (verified) — first use of the binding class; class-init timing unprinted, so INFERRED is correct. |
| 36 `DialogAddFeedChannelBindingImpl.invalidateAll()V` | REACHABLE proposed INFERRED | PASS* | D4e on the AddFeedDialog :202 creation path (verified). *Conditional on D4e standing. Same stale "stays OPEN" text note. |
| 40 `DialogAddFeedChannelBindingImpl.setVariable(int,Object)Z` | OPEN | PASS* | Label matches Phase 1c D4d: AddFeedDialog.java:203 `binding.setViewModel(viewModel)` (verified) is the typed-setter call, and generated setVariable CALLS the typed setter, so the printed call is zero evidence setVariable ran. *Conditional on D4d standing. (Impl setViewModel itself is batch-61 row 1, as the row notes.) |

## Totals

- PASS: 16, FAIL: 0 (of 16 checked).
- Proposed corrections: none to any label. Text cleanups only: superseded "stays OPEN" sentences in rows 10, 18, 26, 36.
- Note for the coordinator: rows 13-16 and 21-24 (variant creation/lifecycle REACHABLE) and the D4c UNREACHABLE rows both
  depend on conventions the file records but does not decide — (iv) all-configurations vs single-config for variants
  (must be applied to batches 60 and 65 together) and D4c option U. Within those decisions, the flips are mechanically
  correct: the D4c flip list (11, 12, 19, 20, 27, 28) matches the table exactly, and no batch-58 row was touched.
