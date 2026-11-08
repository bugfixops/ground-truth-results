# Stream A Phase 3 — Group L4 summary (mappers, gates, misc)

Scope: LibreTorrent only, branch work-2026-10-31, repo bugfixops/ground-truth-results.
No device work, no pushes, no branch edits, no tick marker written. Nothing outside
`phase3/verdicts/L4/` (verdict files) and `phase3/greps/L4/` (saved greps) was written.
No 429 was hit; the single connector fetch (AndroidManifest.xml) succeeded. All greps
below are over the local complete corpus (281 app Java files + res layouts) unless noted.

## 1. D13 mapper rows — 2 flips, 4 stays

- **FLIP 1/1** (baseAdapters.BR.<init>): OPEN → UNREACHABLE no_trigger_in_app INFERRED.
  5 files import androidx.databinding.library.baseAdapters.BR and use only BR.<field> reads
  (grep_D13_BRimports.txt, grep_D13_BRreads.txt); zero `new BR(` in the complete corpus
  (grep_D13_newBR.txt, 0 lines); no printed construction path.
- **FLIP 2/37** (libretorrent.BR.<init>): OPEN → UNREACHABLE no_trigger_in_app INFERRED.
  6 files import org.proninyaroslav.libretorrent.BR, field reads only; same zero-`new BR(` grep.
- **2/38, 2/39 stay OPEN — premise FAILED.** D13's static-only premise is unprinted: no
  generated InnerBrLookup/InnerLayoutIdLookup source exists in the corpus
  (grep_D13_mapper.txt, 0 hits for mapper/lookup/trigger names), and the batch-2
  conditional table records the competing possibility that mapper-generated code constructs
  the lookups. Batch-18 <clinit> REACHABLE does not imply <init> (D8). Resolver: a printed
  generated mapper body showing static-only members with no instantiation (→ UNREACHABLE),
  or a printed lookup-construction site (→ REACHABLE).
- **2/40 stays OPEN — premise FAILED.** No DataBindingTriggerClass source printed
  (same 0-hit grep); empty-marker/no-instance-members unprinted; zero sites of any kind.
  Resolver: a printed generated body showing an empty marker, or a construction/dispatch site.
- **12/1 stays OPEN — link MISSING.** Zero `extends`/`super(` lines in the batch-12 and
  batch-17 files and no generated mapper source for either class, so no printed evidence that
  the libretorrent mapper extends the databinding mapper. Batch-17 <init> REACHABLE (D8)
  does not transfer across packages (D8 no-transfer rule). Resolver: a printed superclass
  relation (→ REACHABLE INFERRED via super() from the REACHABLE libretorrent mapper <init>)
  or a printed databinding-mapper dispatch site.
- **17/36 (collectDependencies), 17/37 (convertBrIdToString) stay OPEN.** Zero hits in app
  Java (grep_D13_1736.txt, 0 lines); runtime-API methods with no printed caller, outside
  D8's inflate-path coverage. Resolver: a printed generated dispatch or app caller.

## 2. D23 test-scope — both stay UNREACHABLE, both checks pass

- **3/16 (Logger.getEntry) stays UNREACHABLE.** (a) Only callers are in src/test LoggerTest
  (grep_D23_testcallers.txt); (b) zero main-tree callers — grep_D23_getEntry.txt is the
  definition (Logger.java:301) only, grep_D23_getEntry_callers.txt is empty.
- **3/21 (TorrentInfoProvider.getInstance, Engine overload) stays UNREACHABLE.** (a) Only
  callers are in src/androidTest — AbstractTest.java:72 and TorrentEngineTest.java:181
  (line numbers confirmed, grep_D23_testcallers.txt); (b) zero main-tree callers of the
  Engine overload — all 5 main-tree getInstance sites use the Context overload
  (grep_D23_provider_getInstance.txt). Neither check failed, so nothing was flipped on
  this item (both rows were already UNREACHABLE INFERRED; verdicts are no-change).

## 3. D24 3-arg ctors — enumeration complete, no label flips

3-arg (Context, AttributeSet, defStyleAttr) rows found by scanning all 120 batch files
plus the corpus ctor definitions (grep_D24_3arg_defs.txt):

| Row | Class | 2-arg body (printed) | Outcome |
|---|---|---|---|
| 85/31 | EmptyRecyclerView | super only (:59-62), no this(...) | UNREACHABLE stands |
| 85/40 | ExpansionHeader | super + init (:63-68), no this(...) | UNREACHABLE stands |
| 86/12 | FixHintTextInputEditText | super only (:39-41), no this(...) | UNREACHABLE stands |
| 86/17 | SwitchBar | super(ContextThemeWrapper) + init (:44-48), no this(...) | UNREACHABLE stands |
| 86/21 | ThemedSpeedDialView | super only (:40-44), no this(...) | UNREACHABLE stands |
| 94/31 | PiecesView | super + create (:57-62), no this(...) | UNREACHABLE stands (label); confirmed_by SOURCE → INFERRED under D28, see §7 |
| 11/6 | AddTagButton | super + init (:43-48), no this(...) | UNREACHABLE stands |
| 115/4 | SummaryPreference | this(context, attrs, R.attr.preferenceStyle) (:44-48) | REACHABLE stands (D24 clause ii) |
| 115/10 | SwitchBarPreference | this(context, attrs, R.attr.preferenceStyle) (:45-49) | REACHABLE stands (D24 clause ii) |
| 115/16 | TimePreference | this(context, attrs, R.attr.preferenceStyle) (:38-42) | REACHABLE stands (D24 clause ii) |

Supporting greps: grep_D24_newctors.txt (zero 3-arg construction sites; sole `new AddTagButton(`
site is the 1-arg form, TorrentTagsList.java:79), grep_D24_extends.txt (zero subclass
extensions, 0 lines). No other batch holds a 3-arg ctor row (ColorView has only a 2-arg ctor;
TorrentTagsList 119/36 is 2-arg only; 115/5, 115/11, 115/17 are 4-arg ctors, REACHABLE via
printed delegation, not D24 rows). LayoutInflater 2-arg-only dispatch is the printed fw_src
fact cited in the batch files.

## 4. D25 (D10 on batches 45/46/118) — confirmation, no flips

- **45/15, 45/16, 45/20, 45/21** already UNREACHABLE closed_by_api_level INFERRED and stand:
  gate prints re-verified from corpus — AppearanceSettingsFragment.java:118
  (`SDK_INT < O` → initLegacyNotifySettings) and TorrentNotifier.java:276
  (`SDK_INT >= O` early return in applyLegacyNotifySettings), saved in grep_D25_gates.txt.
  45/16's sole site (Appearance :213, ringtonePicker result handler) and 45/21's sole site
  (:241, onPreferenceChange branch bound only inside gated initLegacyNotifySettings :134)
  are both inside the gated region. No other batch-45 row turns on the Appearance/
  TorrentNotifier gates (remaining rows are ungated getters/setters or the 46/33-34
  torrentFinishNotify rows with ungated onCreate callers).
- **46/21, 46/22** already UNREACHABLE closed_by_api_level INFERRED and stand: gate print
  re-verified — Utils.java:704-707 (`SDK_INT < R || ...` early return; at API 27 the first
  disjunct is TRUE so :706 is never evaluated) and :711 (after the always-taken return),
  saved in grep_D25_gates.txt.
- **Batch 118: zero SDK hits verified** — grep_D25_batch118_SDK.txt, 0 lines across all six
  batch-118 source files (Scheduling/Storage/Streaming fragments, AddTagButton,
  SelectTagActivity, SelectTagDialog). No batch-118 row is API-gated on its own file and no
  Appearance/TorrentNotifier coupling reaches it. No row changes.

## 5. D26 (D12 on batches 26/27) — confirmation, no flips

All batch-26/27 rows were already REACHABLE; D12 confirms them. Subscription + handler
prints (grep_D26_subscriptions.txt, corpus TorrentInfoProvider.java):

- **27/21 (flagged) stands REACHABLE INFERRED.** Interval error consumer printed at
  :373-374 (`(Throwable t) -> Log.e(TAG, "Getting trackers info for torrent " + id +
  " error: " + ...)`); subscription printed — `Observable.interval(...).subscribe(tick,
  error)` inside `Flowable.create` (:357-375) via observeTrackersInfo :110-111 →
  DetailTorrentViewModel.observeTrackers :180. Under D12 the error occurrence is a runtime
  condition, not a blocker.
- Same pattern verified for 26/33 (advanced-info error consumer :337-338), 27/9 (peers
  :406-407), 27/13 (pieces :439-440), and the tick consumers 26/32 and 27/20. No row had
  a missing subscription, so no row goes to OPEN on its own evidence.

## 6. D27 — FLIP 72/21

- **FLIP 72/21** (TorrentService.onBind): OPEN → UNREACHABLE no_trigger_in_app INFERRED.
  All three D27 elements verified: (i) zero bindService/unbindService/ServiceConnection in
  the complete corpus (grep_D27_bind.txt, 0 lines); (ii) manifest declares TorrentService
  with no android:exported attribute and no intent filter — self-closed element at
  AndroidManifest.xml:252-254, connector fetch SHA 875a8aa7de97caac5d9457836b0ea30f1c3d51ea
  (grep_D27_manifest.txt); (iii) no system binding path printed — only startService sites
  (TorrentEngine :152/:158/:285 via Utils.startServiceBackground → startService at
  Utils.java:432; NotificationReceiver :58/:69/:74/:79, grep_D27_startservice.txt), and
  onBind itself returns null (TorrentService.java:100-103).

## 7. D28 sweep (all 120 batches, read-only) — 23 confirmed_by flips, labels unchanged

Sweep totals: OPEN 257, all confirmed_by `—` (no OPEN-INFERRED or OPEN-SOURCE exceptions);
UNREACHABLE 575, of which 541 already INFERRED. Exceptions verdict as SOURCE → INFERRED
(label unchanged, one kind + reason + source reference preserved in the batch files):

- 39/3, 39/4 (branch_never_taken); 40/3 (branch_never_taken)
- 42/28, 42/29, 42/31 (closed_by_api_level)
- 56/2, 56/3, 56/13, 56/14, 56/15, 56/16, 56/17 (branch_never_taken)
- 57/5 (closed_by_api_level)
- 94/7, 94/8, 94/31 (no_trigger_in_app)
- 96/40, 97/1, 102/13 (no_trigger_in_app)
- 115/38, 115/39, 115/40 (closed_by_api_level)

Non-exceptions noted: batches 17/18 hold 11 UNREACHABLE rows (17/1, 17/4, 17/5, 17/13, 17/18,
17/21, 17/22, 17/27, 17/31, 18/26, 18/27) whose kind cell already states
`no_trigger_in_app / INFERRED` with no separate confirmed_by column — these satisfy D28 in
substance and were NOT verdict as changes. REACHABLE confirmed_by values were NOT touched,
per instructions (65 REACHABLE rows filed with `—` and 135 with no confirmed_by cell are
documented variance outside this sweep's scope).

## 8. D29 tension identification (NO flips — recorded for morning review)

Exact `bind` overload rows for the two `<include>`-child bindings, all in batch 5, all
currently UNREACHABLE no_trigger_in_app INFERRED:

- **AddTorrentInfoBinding.bind: 5/19** (bind(View)) and **5/20** (bind(View,Object))
- **DetailTorrentAppbarBinding.bind: 5/25** (bind(View)) and **5/26** (bind(View,Object))

Include facts verified from layouts: fragment_add_torrent_info.xml:16-19 includes
`@layout/add_torrent_info` with id `info` and `app:viewModel="@{viewModel}"`;
fragment_detail_torrent.xml:10-12 includes `@layout/detail_torrent_appbar` with id `appbar`.
Parent bind rows for reference: FragmentAddTorrentInfoBinding.bind 7/23, 7/24 (also
UNREACHABLE). Tension, verbatim from D29: under D4d parent-include logic, generated
parent-Impl code arguably calls the child `bind()` (a parent must hold the child binding
to pass variables, cf. 59/32); if the user accepts that argument, 5/19, 5/20, 5/25, 5/26
flip to REACHABLE INFERRED; otherwise they stand UNREACHABLE per the user's 2026-11-01
statement that batches 5-9 are UNREACHABLE. NOT flipped tonight — the user's explicit
statement governs until the user revises it. (The `inflate` overloads 5/21-24, 5/27-30 are
not part of this tension.)

## 9. Misc identification

- **115/7** — SummaryPreference.setSummary(int), override, currently OPEN. No decided rule
  covers a Preference setSummary override (not D14 getter, not D15/D16, not D10/D12).
  Evidence: no printed caller on a SummaryPreference receiver (grep_misc_115_setSummary.txt;
  the Appearance setSummary sites at :141/:209 are on a plain `Preference` notifySound);
  XML android:summary is handled by the Preference base class during construction, and the
  override dereferences summaryView (null until onBindViewHolder). **Stays OPEN.**
  Resolver: a printed caller on a SummaryPreference receiver, or a printed androidx
  Preference dispatch showing the override is invoked.
- **115/8** — SummaryPreference.setSummary(CharSequence), override, currently OPEN. Same
  as 115/7 (definition :79-85). **Stays OPEN** with the same resolver.
- **58/32** — ActivityAddTorrentBindingImpl.hasPendingBindings, override, currently OPEN.
  Fitting decided rule is D17, but its outcome turns on one print not obtained in this leaf:
  the version-noted androidx ViewDataBinding rebind body showing whether the rebind path
  queries hasPendingBindings(). App-tree callers are zero (grep_misc_58_hasPendingBindings.txt,
  0 lines). D17 also requires ALL open hasPendingBindings rows to flip together, so this
  row is not flipped alone. LEAD ONLY (not evidence): a secondary databinding write-up
  renders generated executeBindingsInternal as querying hasPendingBindings() — generated-Impl
  code in a blog rendering, not the versioned androidx base-class print D17 names.
  **Stays OPEN.** Resolver: the D17 print (→ all open hasPendingBindings rows flip together,
  REACHABLE INFERRED if queried, UNREACHABLE no_trigger_in_app INFERRED if not queried and
  app-tree callers are zero).
- **22/1** — AddTorrentParams.writeToParcel, Parcelable trio member, currently OPEN.
  Fitting decided rule is D33: no printed marshalling site naming AddTorrentParams
  (grep_misc_22_parcel.txt, 0 lines; batch file agrees — zero marshalling sites in the saved
  252-file grep); definition only at AddTorrentParams.java:96-107; CREATOR alone does not
  flip a row (D33). Not a $1 row (D22 no), not a binding row (D14/D15/D16 no), not D10/D12.
  **Stays OPEN.** Resolver: a printed marshalling site naming AddTorrentParams
  (putExtra/getParcelableExtra/Bundle parcel path) → REACHABLE under D5a/D33.

## Flips (total: label flips 3, confirmed_by flips 23)

Label flips: 1/1, 2/37 (→ UNREACHABLE no_trigger_in_app INFERRED), 72/21 (→ UNREACHABLE
no_trigger_in_app INFERRED).
Confirmed_by-only flips (label unchanged, SOURCE → INFERRED): 39/3, 39/4, 40/3, 42/28,
42/29, 42/31, 56/2, 56/3, 56/13, 56/14, 56/15, 56/16, 56/17, 57/5, 94/7, 94/8, 94/31, 96/40,
97/1, 102/13, 115/38, 115/39, 115/40.

## OPEN remainders with resolvers (this leaf's scope)

2/38, 2/39 (generated mapper body), 2/40 (generated trigger-class body), 12/1 (superclass
relation or databinding-mapper dispatch), 17/36, 17/37 (printed caller/dispatch), 115/7,
115/8 (SummaryPreference-receiver caller or Preference dispatch print), 58/32 (D17
ViewDataBinding rebind-body print, together-flip), 22/1 (AddTorrentParams marshalling site).
D29 tension rows 5/19, 5/20, 5/25, 5/26 are UNREACHABLE by the user's statement, pending the
user's morning decision on the D4d parent-include argument — not OPEN, not flipped.

## Blockers / premises that failed

- No generated databinding source (mapper, InnerBrLookup/InnerLayoutIdLookup,
  DataBindingTriggerClass, Impl bodies) is printed anywhere in the corpus or the batch
  files — this blocks D13 for 2/38, 2/39, 2/40 and D17's print for 58/32, and is why those
  rows stay OPEN rather than flipping on absence.
- No superclass relation between the libretorrent and databinding DataBinderMapperImpl
  classes is printed — blocks 12/1.
- No 429 was encountered; no check was skipped for rate-limit reasons. The one connector
  fetch (manifest) succeeded and its SHA matches the batch-72 record.
- Scope note for the D13 zero-`new BR(` grep: it covers the local complete corpus (app
  Java + res layouts); library sources in final_java_only beyond the printed corpus were
  not re-grepped in this leaf, and the verdict evidence says so. The D13 flip test as
  ordered in the task (static-only constants class + zero `new BR(` + no printed
  construction path) is met on the printed evidence cited.
