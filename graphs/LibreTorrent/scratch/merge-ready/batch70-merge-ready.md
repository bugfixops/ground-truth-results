**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 70 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 70 only, LibreTorrent labels only, no other batch, no other app, no device replay, no Aegis.
- Membership: exactly the 40 rows for batch 70 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`,
  local copy `~/workspace/agent27-plan.tsv` (plan blob SHA
  `0104806dd666c840049b3db52823d4b384fa1c92`), all TODO_CANDIDATE_REACHABLE
  (generator candidates, not evidence), in plan order. Method names in the table were
  generated from that plan copy, not hand-typed.
- Prior proposal (`~/workspace/libretorrent-batch70-proposal.md`) was used as an INPUT / lead
  list only; every row below was re-judged against source printed in this pass.

## Counts — mechanically verified
- **40 rows, sequence 1-40 intact, in plan order.**
- **29 REACHABLE proposed / 0 UNREACHABLE proposed / 11 OPEN**
  (REACHABLE: SOURCE 6 / INFERRED 23).
- **0 rows verified for merge.** Verification still requires the main agent's 1-in-5
  spot-check, `py_compile` + build on a full checkout, and the Mac build/C1 return — all
  **not run** here, never claimed passed.

## HEADLINE CHANGE vs the prior batch-70 proposal (23/0/17 -> 29/0/11)
The prior proposal left all 9 TagsListItem rows OPEN because "NO inflate site printed in
this session" — its ui-directory listing attempt returned no usable listing, and it
excluded the drawer TagsAdapter and TorrentTagsList with reasons (both exclusions stand:
those are different classes/layouts). This pass CLOSES that gap with a fresh branch fetch:
- `ui/tag/TagsAdapter.java` (fresh, branch work-2026-10-31, saved in
  ~/workspace/b6870-src/, 111 lines) imports TagsListItemBinding (:32) and inflates
  `R.layout.tags_list_item` at :48-52 in onCreateViewHolder (:46-54). This is a DIFFERENT
  adapter from the drawer TagsAdapter (ui/main/drawer/TagsAdapter) — do not conflate them.
- `res/layout/tags_list_item.xml` (fresh, 1,099 bytes) matches the plan descriptor exactly:
  ColorView `color` + TextView `name`, and — importantly — it declares NO `<data>` variable.
- The global search_code result that pointed at this file was used ONLY as a locator lead
  and then disregarded; every verdict below rests on the fresh branch fetches above, not
  on search_code (which returns global non-repo results).
Consequence, under the batches 67-69 convention (Impl <clinit>/both <init>/base <init>/
executeBindings/invalidateAll REACHABLE INFERRED on a printed inflate):
rows 21, 22, 23, 24, 25, 27 flip OPEN -> REACHABLE INFERRED (6 rows).
Rows 26 (hasPendingBindings), 28 (onFieldChange), 29 (setVariable) STAY OPEN:
TagsAdapter's ViewHolder uses only `binding.name.setText`, `binding.color.setColor`, and
`binding.getRoot().setOnClickListener` (:100-108) — no setVariable call anywhere in the
freshly printed corpus — and the layout binds no variable, so no observable registration
is printed. That strengthens OPEN (a variable route is implausible from this layout) but
does NOT prove no other caller exists, so per the task rule they are not flipped to
UNREACHABLE without printed generated source or a saved full-repo grep.

## Judging conventions (stated so the merger can overturn them)
- Databinding rows: same as batches 67-69 — generated Impl bodies and DataBinderMapperImpl
  are NOT in final_java_only, so every databinding REACHABLE row is INFERRED (mapper step +
  base-to-Impl dispatch are generated, not printed). Impl <clinit> / both <init> overloads /
  base <init> / executeBindings / invalidateAll are REACHABLE INFERRED on a printed
  inflate; hasPendingBindings / onFieldChange / setVariable are OPEN where no printed
  caller, setter, or observable registration exists — NOT UNREACHABLE without a saved
  full-repo grep. Under a strict entry-route rule the databinding REACHABLE rows revert
  to OPEN (host-fragment/activity creation steps not printed in this session; the
  SelectTagDialog -> TagsAdapter route printed in batch 119 is a LEAD only here, not
  fresh evidence for batch 70).
- Receivers: SOURCE = a printed app-code call site naming the method; INFERRED = framework
  dispatch (manifest registration, registerReceiver, BroadcastReceiver instantiation)
  whose dispatch body was not printed from fw_src.
- confirmed_by is SOURCE or INFERRED only, never DYN, FW-MEMORY, or UNVERIFIED.
  OPEN rows carry "—" (no confirmed_by claim).

## Printed source used in this pass (fresh, branch work-2026-10-31, saved in ~/workspace/b6870-src/)
- ui/addtorrent/DownloadableFilesAdapter.java — inflate item_torrent_downloadable_file :60-61.
- ui/main/TorrentListAdapter.java — inflate item_torrent_list :79-80.
- ui/detailtorrent/pages/trackers/TrackerListAdapter.java — inflate item_trackers_list :73-74.
- ui/tag/TagsAdapter.java — inflate tags_list_item :48-52 (NEW, see headline change).
- res/layout/tags_list_item.xml — ColorView color + TextView name, no <data> variable.
- receiver/BootReceiver.java (74 lines), ConnectionReceiver.java (50), NotificationReceiver.java (83),
  PowerReceiver.java (76) — bodies and filter definitions as cited in the table.
- AndroidManifest.xml (295 lines) — NotificationReceiver :257-261, BootReceiver :266-276;
  ConnectionReceiver and PowerReceiver have NO manifest entry (dynamically registered).
- core/model/TorrentEngine.java (1,658 lines) — fields :108-109, doStart :238-239
  (comment: "Only calls from TorrentService"), switchPowerReceiver :989-1007
  (getCustomFilter :1001 under customBatteryControl, getFilter :1005 under
  batteryControl || onlyCharging), switchConnectionReceiver :1009-1021 (getFilter :1020
  under unmeteredOnly || roaming).
- Grep over all fresh adapter/fragment files: zero hits for `setVariable` or `setViewModel`.
  That grep is over the printed corpus only, NOT a full-repo grep.

## Still owed before merge
1. A printed inflate-site-independent check is no longer owed for TagsListItem rows 21-27
   (site printed above); still owed: a saved full-repo grep for all 11 OPEN rows before
   any OPEN -> UNREACHABLE flip; none is flipped on absence here. Connector search_code
   returned global results and was disregarded throughout except as the locator lead above.
2. Printed TorrentEngine entry step (TorrentService -> doStart) if the merger requires a
   launcher-anchored route for Connection/Power rows 34-36, 39-40; under that rule those
   rows revert to OPEN. Boot/Notification rows 30-33, 37-38 are manifest-anchored.
   (TorrentEngine.doStart's own comment says "Only calls from TorrentService" — a lead,
   not a printed TorrentService call site in this pass.)
3. Generated Impl bodies / DataBinderMapperImpl / layout XML beyond tags_list_item —
   not in final_java_only — plus build, sampler, and C1 on a full checkout (git clone
   still fails without login in this VM). Nothing here is verified for merge.


## ROUND-2 REVISION 2026-11-01 (G17) — 0 flips; counts unchanged (29 REACHABLE / 0 UNREACHABLE / 11 OPEN)

**This revision flips no row and decides no convention.** It completes the
round-1 <include> check for this group, re-runs the rule-F grep, and records
CONDITIONAL outcomes for the 11 OPEN rows. All labels, confirmed_by values,
row order, and REACHABLE rows are exactly as before; only this section and a
short ROUND2 note per OPEN row were added. Original backed up to
`~/workspace/libretorrent-merge-backup-pre-openclose2/batch70-merge-ready.md`.
Build: not run. C1: not run. Nothing pushed.

### 1. The round-1 <include> check is now COMPLETE — result: negative
Full record in `~/workspace/b686970-openclose2-src/include_check_686970.txt`:
- All 69 files of `res/layout/` (round-1 fetch, verified byte-identical to the
  round-1 top-level 13-layout fetches, 13/13): the only `<include>` targets
  anywhere are `toolbar`, `main_drawer_content`, `add_torrent_info`, and
  `detail_torrent_appbar`. Zero `@layout/` references to any of the 13 group
  layouts, and zero `bind:` attributes in any file — so no layout passes a
  variable to an included child anywhere in `res/layout/`.
- Fresh connector listings this pass: `res/` holds exactly three layout dirs
  (`layout`, `layout-large-land-notouch`, `layout-sw600dp-land`). Each qualified
  dir holds only `detail_torrent_appbar.xml` (SHA
  `be659cb60ff9d3b2df954eed6c1eb05a3415fa41`, 36 lines, 0 `<include>`, no
  `<data>`) and `fragment_add_torrent_info.xml` (SHA
  `8e7ec93e56e894c3305b7a620ac540702c6a1f74`, 38 lines, single `<include>` to
  `add_torrent_info`). No qualified variant of any of the 13 exists.
- None of the 13 layouts declares a `<data>` variable, `<import>`, or
  `<include>`; the only `@{...}` expressions in the set are three static dimen
  sums referencing no variable and no Observable, so no observable registration
  and no onFieldChange route arises from them. TagsListItem's layout
  (`tags_list_item.xml`) has no `@{...}` expression at all.
- Conclusion: the generated parent-to-child setVariable route is CLOSED for all
  13 bindings on layout evidence. What this does NOT close: generated Impl
  bodies and the databinding-library rebind body are still unprinted, so the
  verdicts below stay convention-dependent.

### 2. Rule-F grep re-run reproduces round 1 exactly
`~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt` (252 app Java
files, branch work-2026-10-31, count verified): `setVariable` 0 hits,
`onFieldChange` 0 hits, `hasPendingBindings` 0 hits, all 13 group Impl class
names 0 hits, `executePendingBindings` 0 hits. `setViewModel` 14 hits, none on
a batch 68/69/70 binding host. No connector 429 was hit in this pass (7 read
calls, ~30 s pauses); no search_code result was used.

### 3. CONDITIONAL table — the 11 OPEN rows (no option applied)
The setVariable-direction contradiction (batches 63-64 OPEN on zero hits vs
batch 65 REACHABLE via dispatch behind setViewModel, mechanically backwards
since setVariable CALLS the typed setter) and the generic-framework-callback
question (rule xv: onFieldChange/setVariable REACHABLE only where a variable
is actually set) are both UNDECIDED at project level. This pass applies none
of the options below. A printed generated Impl body or printed
databinding-library dispatch body would supersede this table.

| Option | setVariable rows 2, 11, 20, 29 | onFieldChange rows 1, 10, 19, 28 | hasPendingBindings rows 8, 17, 26 |
|---|---|---|---|
| S — status quo (this file) | stay OPEN | stay OPEN | stay OPEN |
| U — merger accepts combined evidence as trigger-absence (zero tree hits + no variable + no include parent + no typed-setter call on these bindings) | flip to UNREACHABLE no_trigger_in_app INFERRED | flip to UNREACHABLE no_trigger_in_app INFERRED | stay OPEN (variable-freedom does not close a library state query; rebind body still unprinted) |
| R — generic-framework-callback rule (framework/generated dispatch always runs these callbacks) | flip to REACHABLE INFERRED — but conflicts with rule (xv) for these no-variable bindings; merger must reconcile R with (xv) explicitly | flip to REACHABLE INFERRED — same (xv) conflict | stay OPEN (needs the printed rebind body either way) |

Named resolver for hasPendingBindings rows 8, 17, 26 under every option: a
printed generated Impl body or printed databinding-library rebind body showing
whether the rebind path calls this override, or that it never does.

### 4. Cross-batch linkage (judge consistently, never separately)
Rows 1-2 (ItemTorrentDownloadableFile Impl onFieldChange/setVariable) complete
the Downloadable binding whose head rows are batch 69 rows 34-40; they follow
batch 69's option U/R/S outcomes for that binding, while batch 69 row 39
(hasPendingBindings) stays OPEN under every option. Receiver rows 30-40 are
unaffected by this revision.

## Per-method table (plan order)

| # | Method | Label | confirmed_by | Printed route / citation |
|---|---|---|---|---|
| 1 | ItemTorrentDownloadableFileBindingImpl.onFieldChange | OPEN | — | Companion to batch 69 rows 34-40. No variable set / observable registration printed for this binding (DownloadableFilesAdapter uses the binding as a ViewHolder field only). NOT UNREACHABLE without a saved full-repo grep. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); <include> check completed (include_check_686970.txt, same dir): no layout in any layout dir includes this binding's layout, layout declares no variable. Still OPEN: no generated/library body printed, and the generic-framework-callback / setVariable-direction conventions are undecided — see the CONDITIONAL table above. This pass decides no convention. |
| 2 | ItemTorrentDownloadableFileBindingImpl.setVariable | OPEN | — | No printed setVariable call on this binding. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); <include> check completed (include_check_686970.txt, same dir): no layout in any layout dir includes this binding's layout, layout declares no variable. Still OPEN: no generated/library body printed, and the generic-framework-callback / setVariable-direction conventions are undecided — see the CONDITIONAL table above. This pass decides no convention. |
| 3 | ItemTorrentListBinding.<init> | REACHABLE | INFERRED | Called by ItemTorrentList Impl <init> (rows 5-6) in generated code; layout inflated at TorrentListAdapter:79-80 (fresh). |
| 4 | ItemTorrentListBindingImpl.<clinit> | REACHABLE | INFERRED | First reference via TorrentListAdapter:79 inflate (fresh). |
| 5 | ItemTorrentListBindingImpl.<init>(DataBindingComponent,View) | REACHABLE | INFERRED | Mapper result of TorrentListAdapter:79 inflate (fresh, generated, not printed). |
| 6 | ItemTorrentListBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE | INFERRED | Called by row 5 in generated code (pattern, body not printed). |
| 7 | ItemTorrentListBindingImpl.executeBindings | REACHABLE | INFERRED | Framework rebind after generated invalidateAll on the row-5 construction. |
| 8 | ItemTorrentListBindingImpl.hasPendingBindings | OPEN | — | No printed caller in the printed corpus. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method and for executePendingBindings); <include> check completed (include_check_686970.txt, same dir). Still OPEN under every option in the CONDITIONAL table above: named resolver is a printed generated Impl body or printed databinding-library rebind body showing whether the rebind path calls this override. This pass decides no convention. |
| 9 | ItemTorrentListBindingImpl.invalidateAll | REACHABLE | INFERRED | Called by the generated Impl constructor on the row-5 construction. |
| 10 | ItemTorrentListBindingImpl.onFieldChange | OPEN | — | No variable set / observable registration printed for this binding. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); <include> check completed (include_check_686970.txt, same dir): no layout in any layout dir includes this binding's layout, layout declares no variable. Still OPEN: no generated/library body printed, and the generic-framework-callback / setVariable-direction conventions are undecided — see the CONDITIONAL table above. This pass decides no convention. |
| 11 | ItemTorrentListBindingImpl.setVariable | OPEN | — | No printed setVariable call on this binding. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); <include> check completed (include_check_686970.txt, same dir): no layout in any layout dir includes this binding's layout, layout declares no variable. Still OPEN: no generated/library body printed, and the generic-framework-callback / setVariable-direction conventions are undecided — see the CONDITIONAL table above. This pass decides no convention. |
| 12 | ItemTrackersListBinding.<init> | REACHABLE | INFERRED | Called by ItemTrackersList Impl <init> (rows 14-15) in generated code; layout inflated at TrackerListAdapter:73-74 (fresh). |
| 13 | ItemTrackersListBindingImpl.<clinit> | REACHABLE | INFERRED | First reference via TrackerListAdapter:73 inflate (fresh). |
| 14 | ItemTrackersListBindingImpl.<init>(DataBindingComponent,View) | REACHABLE | INFERRED | Mapper result of TrackerListAdapter:73 inflate (fresh, generated, not printed). |
| 15 | ItemTrackersListBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE | INFERRED | Called by row 14 in generated code (pattern, body not printed). |
| 16 | ItemTrackersListBindingImpl.executeBindings | REACHABLE | INFERRED | Framework rebind after generated invalidateAll on the row-14 construction. |
| 17 | ItemTrackersListBindingImpl.hasPendingBindings | OPEN | — | No printed caller in the printed corpus. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method and for executePendingBindings); <include> check completed (include_check_686970.txt, same dir). Still OPEN under every option in the CONDITIONAL table above: named resolver is a printed generated Impl body or printed databinding-library rebind body showing whether the rebind path calls this override. This pass decides no convention. |
| 18 | ItemTrackersListBindingImpl.invalidateAll | REACHABLE | INFERRED | Called by the generated Impl constructor on the row-14 construction. |
| 19 | ItemTrackersListBindingImpl.onFieldChange | OPEN | — | No variable set / observable registration printed for this binding. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); <include> check completed (include_check_686970.txt, same dir): no layout in any layout dir includes this binding's layout, layout declares no variable. Still OPEN: no generated/library body printed, and the generic-framework-callback / setVariable-direction conventions are undecided — see the CONDITIONAL table above. This pass decides no convention. |
| 20 | ItemTrackersListBindingImpl.setVariable | OPEN | — | No printed setVariable call on this binding. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); <include> check completed (include_check_686970.txt, same dir): no layout in any layout dir includes this binding's layout, layout declares no variable. Still OPEN: no generated/library body printed, and the generic-framework-callback / setVariable-direction conventions are undecided — see the CONDITIONAL table above. This pass decides no convention. |
| 21 | TagsListItemBinding.<init> | REACHABLE | INFERRED | Called by TagsListItem Impl <init> (rows 23-24) in generated code; layout inflated at TagsAdapter (ui/tag):48-52 (fresh, NEW vs prior proposal — see header). |
| 22 | TagsListItemBindingImpl.<clinit> | REACHABLE | INFERRED | First reference via TagsAdapter (ui/tag):48 inflate (fresh). |
| 23 | TagsListItemBindingImpl.<init>(DataBindingComponent,View) | REACHABLE | INFERRED | Mapper result of TagsAdapter (ui/tag):48 inflate (fresh, generated, not printed). |
| 24 | TagsListItemBindingImpl.<init>(DataBindingComponent,View,Object[]) | REACHABLE | INFERRED | Called by row 23 in generated code (pattern, body not printed). |
| 25 | TagsListItemBindingImpl.executeBindings | REACHABLE | INFERRED | Framework rebind after generated invalidateAll on the row-23 construction. |
| 26 | TagsListItemBindingImpl.hasPendingBindings | OPEN | — | No printed caller in the printed corpus. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method and for executePendingBindings); <include> check completed (include_check_686970.txt, same dir). Still OPEN under every option in the CONDITIONAL table above: named resolver is a printed generated Impl body or printed databinding-library rebind body showing whether the rebind path calls this override. This pass decides no convention. |
| 27 | TagsListItemBindingImpl.invalidateAll | REACHABLE | INFERRED | Called by the generated Impl constructor on the row-23 construction. |
| 28 | TagsListItemBindingImpl.onFieldChange | OPEN | — | No variable set / observable registration printed for this binding. Layout tags_list_item.xml declares NO <data> variable (fresh), so no observable is bound from this layout — strengthens OPEN, does not close it to UNREACHABLE without generated source or a saved full-repo grep. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); <include> check completed (include_check_686970.txt, same dir): no layout in any layout dir includes this binding's layout, layout declares no variable. Still OPEN: no generated/library body printed, and the generic-framework-callback / setVariable-direction conventions are undecided — see the CONDITIONAL table above. This pass decides no convention. |
| 29 | TagsListItemBindingImpl.setVariable | OPEN | — | No printed setVariable call on this binding (TagsAdapter ViewHolder uses only binding.name / binding.color / getRoot(), :100-108). Layout declares no variable. See row 28. ROUND2 2026-11-01 (G17): re-run grep ~/workspace/b686970-openclose2-src/ruleF_grep_686970_rerun.txt (252 app Java files) reproduces round 1 exactly (zero hits for this method); <include> check completed (include_check_686970.txt, same dir): no layout in any layout dir includes this binding's layout, layout declares no variable. Still OPEN: no generated/library body printed, and the generic-framework-callback / setVariable-direction conventions are undecided — see the CONDITIONAL table above. This pass decides no convention. |
| 30 | BootReceiver.<init> | REACHABLE | INFERRED | Implicit ctor; framework instantiates the manifest-registered receiver (manifest fresh: BootReceiver :266-276). No explicit ctor body exists in BootReceiver.java to print. |
| 31 | BootReceiver.initScheduling | REACHABLE | SOURCE | Called from BootReceiver.onReceive (starts :39) in both branches; definition :60-73 (fresh). |
| 32 | BootReceiver.isBootCompleted | REACHABLE | SOURCE | Called from BootReceiver.onReceive (starts :39); definition :54-57 (fresh). |
| 33 | BootReceiver.onReceive | REACHABLE | INFERRED | Manifest-registered entry (BOOT_COMPLETED / QUICKBOOT_POWERON / SCHEDULE_EXACT_ALARM_PERMISSION_STATE_CHANGED, manifest :266-276 fresh); framework dispatch INFERRED (fw_src dispatch not printed). Body :39-53. Gate: system_event BOOT_COMPLETED (and the two quickboot actions). |
| 34 | ConnectionReceiver.<init> | REACHABLE | SOURCE | TorrentEngine.java:109 `private ConnectionReceiver connectionReceiver = new ConnectionReceiver();` (fresh). |
| 35 | ConnectionReceiver.getFilter | REACHABLE | SOURCE | TorrentEngine.java:1020 `appContext.registerReceiver(connectionReceiver, ConnectionReceiver.getFilter());` (fresh) under STATE settings gate unmeteredOnly || roaming (:1019); definition ConnectionReceiver.java:46-48 (fresh). |
| 36 | ConnectionReceiver.onReceive | REACHABLE | INFERRED | Dynamically registered at TorrentEngine.java:1020 (fresh); framework broadcast dispatch INFERRED. Body ConnectionReceiver.java:37-44 gates on CONNECTIVITY_ACTION. Engine-anchored: under a strict entry-route rule reverts to OPEN (TorrentEngine entry step not freshly printed). |
| 37 | NotificationReceiver.<init> | REACHABLE | INFERRED | Implicit ctor; framework instantiates the manifest-registered receiver (manifest fresh: NotificationReceiver :257-261). No explicit ctor body exists in NotificationReceiver.java to print. |
| 38 | NotificationReceiver.onReceive | REACHABLE | INFERRED | Manifest-registered entry for NOTIFY_ACTION_SHUTDOWN_APP / NOTIFY_ACTION_ADD_TORRENT (manifest :257-261 fresh); framework dispatch INFERRED. Body NotificationReceiver.java:42-83. |
| 39 | PowerReceiver.<init> | REACHABLE | SOURCE | TorrentEngine.java:108 `private PowerReceiver powerReceiver = new PowerReceiver();` (fresh). |
| 40 | PowerReceiver.getCustomFilter | REACHABLE | SOURCE | TorrentEngine.java:1001 `appContext.registerReceiver(powerReceiver, PowerReceiver.getCustomFilter());` (fresh) under STATE settings gate customBatteryControl (:1000); definition PowerReceiver.java:66-74 (fresh). Cross-note (NOT a batch 70 row): PowerReceiver.getFilter is likewise SOURCE via TorrentEngine.java:1005 under batteryControl || onlyCharging (:1004). |
