## Revision 2026-11-01 — Stream A Phase 1c, DECISIONS.md applied (UNVERIFIED, 0 label flips)

Applied mechanically from ~/workspace/overnight/stream-A/DECISIONS.md (Muse's own decisions, for user/Yang review). Counts unchanged: 37 REACHABLE proposed / 0 UNREACHABLE / 3 OPEN (40 rows).
- D5c Option B (newArray requires a printed Parcelable-array site): row 27 (PreferenceActivityConfig$1.newArray) stays OPEN — it was already OPEN; NOT flipped to REACHABLE. Single-extra sites (SF:239 / PA:69) do not call newArray.
- Rows 22, 23 (PreferenceActivityConfig setters) stay OPEN — DECISIONS.md orders no flip for them.
- D1: OPEN rows' confirmed_by already "—"; no change.
- Build/C1: not run. No push. Nothing verified for merge.

## Revision 2026-11-01 — OPEN-closing round 2, group G16 (UNVERIFIED, 0 flips)

0 of 3 OPEN rows closed in this pass; counts unchanged (37 REACHABLE / 0 UNREACHABLE / 3 OPEN).
New evidence this pass: fresh greps over the already-fetched 252-file app Java tree
(~/workspace/ruleF-src), saved in ~/workspace/b103106112114115-openclose2-src/grep_rest.txt and grep_extra.txt. No GitHub
connector fetch was needed; no fresh 429. Res/layout, res/xml, generated code and
library/framework code are NOT in that tree, so it is NOT a full-repo grep.
- Rows 22-23 PreferenceActivityConfig.setFragment/setTitle: PreferenceActivityConfig is
  referenced tree-wide only at PreferenceActivity.java:69 (getParcelableExtra), SettingsFragment
  :235 (2-arg ctor) and NetworkSettingsFragment.java:252 and :373 (both 2-arg ctor + putExtra
  at :256 and :377) — NEITHER Network site calls a setter, and neither does SettingsFragment
  or PreferenceActivity. Every other setFragment/setTitle hit in the tree is another receiver
  (toolbar.setTitle, actionMode.setTitle, storageAdapter.setTitle, dialog setTitle). No
  Bundle/setArguments site carries a PreferenceActivityConfig. Stay OPEN; named target: a
  printed setter call site, or a saved full-repo grep.
- Row 27 PreferenceActivityConfig$1.newArray: tree-wide ZERO array-extra sites
  (getParcelableArrayExtra, putParcelableArrayListExtra, getParcelableArrayListExtra all zero).
  The only PreferenceActivityConfig parcel sites are single extras (SettingsFragment:239 /
  PreferenceActivity:69, plus NetworkSettingsFragment :256/:377). A single extra never calls
  newArray. Stay OPEN; named target: a printed array-extra site, or a saved full-repo grep.
CONDITIONAL TABLE — the 102/114 newArray INCONSISTENCY (FLAGGED, NEVER DECIDED): batch 102
marks FileManagerConfig$1.newArray (row 17) REACHABLE INFERRED on single-extra dispatch alone
(CreateTorrentDialog putExtra :263/:273/:334 + FileManagerDialog.java:137 getParcelableExtra;
this pass re-verified tree-wide zero array sites for FileManagerConfig too), while batch 114
keeps PreferenceActivityConfig$1.newArray (row 27) OPEN on identical-shaped evidence
(single-extra dispatch only). Applying ONE rule to both:
| Rule | 102/17 FileManagerConfig newArray | 114/27 PAC newArray |
| Option A: single-extra framework dispatch suffices for the whole trio, newArray included | stays REACHABLE INFERRED | flips to REACHABLE INFERRED |
| Option B: newArray requires a printed Parcelable-array site | REVERTS to OPEN | stays OPEN |
Under BOTH options the trio companions (Parcel ctor, createFromParcel, describeContents,
writeToParcel) stay REACHABLE on the single extra; only newArray differs. Spillover flagged,
not decided (outside G16): under Option B, any other newArray marked REACHABLE on a
non-array site (e.g. batch 92 row 39 via a storage site) would be at risk on the same logic;
the merger must apply one rule project-wide. No label changed in this file on this table.
Build: not run. C1: not run.

**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 114 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to `graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** Build and C1 run on the user's Mac after a push, so they are marked "not run" here, never passed. No sampler or full-repo grep was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 114 only, max 40 methods, no other batch, no other app, no device replay, no Aegis.
- Task: labels only, from printed source. The prior batch-114 proposal (`~/workspace/libretorrent-batch114-proposal.md`) was used as an INPUT, not a result; every row below was checked against printed source in this pass. No label changed from that proposal; the 3 OPEN rows were re-checked against the printed files and stay OPEN (see below).

## Membership — verified, not guessed

Exactly the 40 rows for batch 114 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the local plan copy `~/workspace/agent27-plan.tsv` (4,733 lines incl. header; plan blob SHA `0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy). All 40 rows are `TODO_CANDIDATE_REACHABLE` in the plan (candidates, not evidence), in plan order:
drawer.TagsAdapter$ItemViewHolder rows 1-5, drawer.TagsAdapter$NoTagsItemViewHolder rows 6-9, PreferenceActivity rows 10-15, PreferenceActivityConfig (+ $1) rows 16-27, SettingsActivity rows 28-32, SettingsFragment rows 33-40.
Membership was re-checked mechanically in this pass against the plan copy: 40 rows, sequence 1-40 intact, method names identical to the plan list. Batch 113 (separate file) covers the rest of TagsAdapter and the tag items.

## Printed source used in this pass

Path prefix for all: `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`
Prior-session printed copies, re-read in full in this pass, saved under `~/workspace/b113-114-src/`:
- `ui/main/drawer/TagsAdapter.java` (316 lines; same copy as batch 113)
- `ui/main/MainActivity.java` (811 lines; same copy as batch 113)
- `ui/settings/PreferenceActivity.java` (132 lines)
- `ui/settings/PreferenceActivityConfig.java` (94 lines)
- `ui/settings/SettingsActivity.java` (73 lines)
- `ui/settings/SettingsFragment.java` (242 lines)

Re-checks performed in this pass against those printed files (not just carried forward):
- `config.setFragment` / `config.setTitle`: no such call in SettingsFragment.java or PreferenceActivity.java. The `setFragment(...)` hits in those files are SettingsFragment.setFragment (SF:94-95, :141-204, :220) and PreferenceActivity.setFragment (PA:82, :85) — different methods, different classes — and `toolbar.setTitle(title)` (PA:76) is not PreferenceActivityConfig.setTitle. Hence rows 22-23 stay OPEN.
- Parcelable array site: no `getParcelableArrayExtra` in any printed file, and the only PreferenceActivityConfig parcel sites are the single extra SF:239 / PA:69. Hence row 27 stays OPEN.
- TagsAdapter holder binds, MainActivity tags/settings anchors, and PreferenceActivity config round-trip were all re-grepped in this pass (see citations in the table).

## Shared routes (printed steps, cited once and reused by row)

All file references below are to the prefix above unless stated otherwise. TA = `ui/main/drawer/TagsAdapter.java`, MA = `ui/main/MainActivity.java`, PA = `ui/settings/PreferenceActivity.java`, PAC = `ui/settings/PreferenceActivityConfig.java`, SA = `ui/settings/SettingsActivity.java`, SF = `ui/settings/SettingsFragment.java`.

**R-TAGS — as batch 113.** MA.initDrawer :270-272 (`tagsAdapter = new TagsAdapter(...)` :271, tagsList.setAdapter(tagsAdapter) :272); MA.subscribeTags :470-486 (submitList :485). RecyclerView/ListAdapter dispatch to TA callbacks is library dispatch, INFERRED.

**R-SETTINGS — MainActivity menu -> SettingsActivity -> SettingsFragment.** MA.onOptionsItemSelected :742-743: `else if (itemId == R.id.settings_menu) startActivity(new Intent(this, SettingsActivity.class));` Framework activity instantiation/lifecycle (unprinted) then runs SA.onCreate :42-62 (setContentView :49, detailTitle observer registered :58-61). SettingsFragment is the settings host fragment: SF.onViewCreated :82-129 registers prefClickListener on every section preference, SF.setFragment :220-230 writes viewModel.detailTitleChanged (:222), which SA observes (:58). The layout/transaction step that attaches SettingsFragment to SettingsActivity was NOT printed (activity_settings layout not printed, no fragment transaction for SettingsFragment in SA) — see Caveats: under a strict rule the SettingsFragment rows (33-40) revert to OPEN until that attachment is printed.

**R-PREF — SettingsFragment small-screen path -> PreferenceActivity (+ Config parcel).** SF.openPreference :136-212, small-screen branch (Utils.isLargeScreenDevice false): SF.startActivity :232-241: `Intent i = new Intent(activity, PreferenceActivity.class);` `PreferenceActivityConfig config = new PreferenceActivityConfig(fragment.getSimpleName(), title);` :235-237, `i.putExtra(PreferenceActivity.TAG_CONFIG, config);` :239, `startActivity(i);` :240. Framework marshalling on putExtra/startActivity calls PAC.writeToParcel/describeContents (INFERRED); framework activity instantiation/lifecycle then runs PA.onCreate :52-83, which reads the parcel back at :68-71: `intent.hasExtra(TAG_CONFIG)` :68, `intent.getParcelableExtra(TAG_CONFIG)` :69 (framework unparcel -> PAC$1.createFromParcel -> PAC Parcel ctor, INFERRED), `config.getFragment()` :70, `config.getTitle()` :71, then PA.setFragment(getFragment(fragment)) :82 (large-screen guard :58-61 finishes the activity in two-pane mode instead — so the PreferenceActivity fragment route runs only on small screens; the large-screen route is SF.setFragment, row 40).

**Confirmed_by convention used here (same as batch 113).** SOURCE = the method's own call site is printed in app code (explicit `new`, method call, or `super(...)` in a printed constructor, or a printed call inside the same file). INFERRED = the only step into the method is a framework/library dispatch (activity/fragment lifecycle, View/PopupMenu click, LiveData observer, Parcelable marshalling, JVM class initialisation) from a printed registration/start site. A row whose upstream dispatch is INFERRED but whose own call site is a printed explicit call is marked SOURCE, with the upstream caveat noted. Under a whole-route INFERRED convention, those SOURCE rows would flip to INFERRED; labels are unaffected, only confirmed_by would change at merge.

## Counts — proposed, not verified (mechanically verified: 40 rows, sequence 1-40 intact)

- REACHABLE proposed: 37 / 40 (SOURCE 12, INFERRED 25)
- UNREACHABLE proposed: 0
- OPEN: 3 / 40 (rows 22, 23, 27)
- Verified for merge: 0

## Per-method table (all 40 rows, in plan order)

| # | Method (plan) | Proposed label | confirmed_by | Route / printed citations |
|---|---|---|---|---|
| 1 | drawer.TagsAdapter$ItemViewHolder.bind(AbstractTagItem,OnClickListener) | REACHABLE proposed | SOURCE | Explicit printed call TA:99 `holder.bind(item, listener);` in onBindViewHolder (batch 113 row 29); body TA:177-184 checks `instanceof TagItem` then calls row 2 at :182. |
| 2 | drawer.TagsAdapter$ItemViewHolder.bind(TagItem,OnClickListener) | REACHABLE proposed | SOURCE | Explicit printed call TA:182 `bind((TagItem) item, listener);` inside row 1's method. Definition TA:186-222 (:190-191 name/colour, :192 root click, :198 menu click, :216 item.isSame(selectedItem) — batch 113 row 24's SOURCE route). Note: TagItem here is drawer.TagItem (ui/main/drawer), not ui/tag/TagItem. |
| 3 | drawer.TagsAdapter$ItemViewHolder.lambda$bind$0 | REACHABLE proposed | INFERRED | Root click-listener lambda TA:192-197 (`binding.getRoot().setOnClickListener((v) -> {...})`, body :193 setSelectedItem, :195 listener.onTagSelected). Registered in printed code, invoked by framework View click dispatch (unprinted), hence INFERRED. Numbering by source order (first lambda in ItemViewHolder.bind), NOT bytecode-verified. |
| 4 | drawer.TagsAdapter$ItemViewHolder.lambda$bind$1 | REACHABLE proposed | INFERRED | Menu-item click lambda TA:201-206 (`popup.setOnMenuItemClickListener((MenuItem menuItem) -> {...})`, body :203 listener.onTagMenuClicked). Invoked by framework PopupMenu dispatch (unprinted), hence INFERRED. Numbering by source order (second lambda in bind), NOT bytecode-verified. |
| 5 | drawer.TagsAdapter$ItemViewHolder.lambda$bind$2 | REACHABLE proposed | INFERRED | Menu-button click lambda TA:198-208 (`binding.menu.setOnClickListener((v) -> {...})`, body creates/shows the PopupMenu :199-207). Invoked by framework View click dispatch, hence INFERRED. Numbering by source order (third lambda in bind — note it encloses row 4's lambda), NOT bytecode-verified. |
| 6 | drawer.TagsAdapter$NoTagsItemViewHolder.<init> | REACHABLE proposed | SOURCE | Explicit printed construction TA:88 `return new NoTagsItemViewHolder(binding);` inside onCreateViewHolder (batch 113 row 30, upstream INFERRED). Definition TA:275-279 (super(binding.getRoot()) :276 — batch 113 row 35's route). |
| 7 | drawer.TagsAdapter$NoTagsItemViewHolder.bind(AbstractTagItem,OnClickListener) | REACHABLE proposed | SOURCE | Explicit printed call TA:99 `holder.bind(item, listener);` in onBindViewHolder; body TA:282-289 checks `instanceof NoTagsItem` then calls row 8 at :287. |
| 8 | drawer.TagsAdapter$NoTagsItemViewHolder.bind(NoTagsItem,OnClickListener) | REACHABLE proposed | SOURCE | Explicit printed call TA:287 `bind((NoTagsItem) item, listener);` inside row 7's method. Definition TA:291-314 (:295 click listener, :308 item.isSame(selectedItem) — batch 113 row 21's SOURCE route). |
| 9 | drawer.TagsAdapter$NoTagsItemViewHolder.lambda$bind$0 | REACHABLE proposed | INFERRED | Click-listener lambda TA:295-300 (`binding.getRoot().setOnClickListener((v) -> {...})`, body :296 setSelectedItem, :298 listener.onTagSelected). Framework View click dispatch, hence INFERRED. Numbering by source order (only lambda in this bind), NOT bytecode-verified. |
| 10 | PreferenceActivity.<clinit> | REACHABLE proposed | INFERRED | Static fields PA:45 (TAG, getSimpleName()) and :47 (TAG_CONFIG constant). First printed use of the class is SF:234 `new Intent(activity, PreferenceActivity.class)`. Class-init timing is the unprinted JVM rule, hence INFERRED. |
| 11 | PreferenceActivity.<init> | REACHABLE proposed | INFERRED | Implicit default ctor (none declared in PA). Framework activity instantiation on SF.startActivity :240 (R-PREF); no printed `new PreferenceActivity(...)` site exists, hence INFERRED. |
| 12 | PreferenceActivity.getFragment | REACHABLE proposed | SOURCE | Explicit printed call PA:82 `setFragment(getFragment(fragment));` inside onCreate (row 13). Definition PA:94-122 (name -> newInstance chain for all 10 section fragments, :97-116). Small-screen only (see two-pane gate below). |
| 13 | PreferenceActivity.onCreate | REACHABLE proposed | INFERRED | Framework activity lifecycle on SF.startActivity :240 (R-PREF); body PA:52-83 printed (theme :54, large-screen finish :58-61, config read :68-71, setFragment :82). Dispatch is framework, hence INFERRED. |
| 14 | PreferenceActivity.onOptionsItemSelected | REACHABLE proposed | INFERRED | Framework menu dispatch (home button :127-128 finish()); body PA:125-131 printed, always returns true. Dispatch unprinted, hence INFERRED. |
| 15 | PreferenceActivity.setFragment | REACHABLE proposed | SOURCE | Explicit printed call PA:82 `setFragment(getFragment(fragment));` inside onCreate (guarded by `fragment != null && savedInstanceState == null` :81). Definition PA:85-92 (fragment transaction, replace :90-91). Small-screen only. |
| 16 | PreferenceActivityConfig.<clinit> | REACHABLE proposed | INFERRED | Static CREATOR field PAC:79-93 is initialised at class initialisation; first printed use is SF:235 `new PreferenceActivityConfig(...)`. Timing is the unprinted JVM rule, hence INFERRED. |
| 17 | PreferenceActivityConfig.<init>(Parcel) | REACHABLE proposed | INFERRED | Called by row 26's createFromParcel (PAC:85) on framework unparcel at PA:69 getParcelableExtra (R-PREF). Definition PAC:40-44 (readString x2). Unparcel dispatch is framework, hence INFERRED. |
| 18 | PreferenceActivityConfig.<init>(String,String) | REACHABLE proposed | SOURCE | Explicit printed construction SF:235-237 `new PreferenceActivityConfig(fragment.getSimpleName(), title)` inside SF.startActivity. Definition PAC:34-38. |
| 19 | PreferenceActivityConfig.describeContents | REACHABLE proposed | INFERRED | Framework Parcel marshalling on SF:239 putExtra + :240 startActivity (R-PREF); framework calls describeContents during marshalling. Definition PAC:67-70 (return 0). Dispatch unprinted, hence INFERRED. |
| 20 | PreferenceActivityConfig.getFragment | REACHABLE proposed | SOURCE | Explicit printed call PA:70 `fragment = config.getFragment();` inside PA.onCreate. Definition PAC:51-54. |
| 21 | PreferenceActivityConfig.getTitle | REACHABLE proposed | SOURCE | Explicit printed call PA:71 `title = config.getTitle();` inside PA.onCreate. Definition PAC:61-64. |
| 22 | PreferenceActivityConfig.setFragment | UNREACHABLE no_trigger_in_app | INFERRED | A1 2026-11-01 (merger direct, helper A1-R5-b evidence cross-checked): saved full-tree grep: 16 setFragment hits, all other methods (PreferenceActivity.java:85, SettingsFragment.java:220, NetworkSettingsFragment.java:361, Fragment-typed args); configs built only via 2-arg ctor + putExtra (SettingsFragment.java:235-239, NetworkSettingsFragment.java:252-256,373-377) and read only via getters (PreferenceActivity.java:70-71). auto_calls.json: exact dst PreferenceActivityConfig.setFragment 0 edges. Def PreferenceActivityConfig.java:46-49. Definition PAC:46-49. No printed caller in the files printed (SF uses the 2-arg ctor :235-237, PA uses only the getters :70-71). Re-checked in this pass: no `config.setFragment` site exists in the printed files. Resolves with: a printed setFragment call site, or a saved full-repo grep. NOT UNREACHABLE on this evidence (a plain setter on a Parcelable config). |
| 23 | PreferenceActivityConfig.setTitle | UNREACHABLE no_trigger_in_app | INFERRED | A1 2026-11-01 (merger direct, helper A1-R5-b evidence cross-checked): saved full-tree grep: 40 setTitle hits, every other hit a different receiver (toolbar, dialog builder, menu item, spinner adapter own setTitle at FileManagerSpinnerAdapter.java:182); receiver reads only getTitle() (PreferenceActivity.java:71). auto_calls.json: exact dst PreferenceActivityConfig.setTitle 0 edges. Def PreferenceActivityConfig.java:56-59. Definition PAC:56-59. No printed caller in the files printed, same as row 22 (re-checked: no `config.setTitle` site; `toolbar.setTitle(title)` PA:76 is a different method). Resolves with: a printed setTitle call site, or a saved full-repo grep. NOT UNREACHABLE on this evidence. |
| 24 | PreferenceActivityConfig.writeToParcel | REACHABLE proposed | INFERRED | Framework Parcel marshalling on SF:239 putExtra + :240 startActivity (R-PREF). Definition PAC:73-77 (writeString fragment, writeString title). Dispatch unprinted, hence INFERRED. |
| 25 | PreferenceActivityConfig$1.<init> | REACHABLE proposed | INFERRED | Anonymous Parcelable.Creator subclass PAC:79-93, created by the CREATOR static-field initializer (:79-80); it is the only anonymous class in PAC, so $1 = this Creator (numbering by source order, NOT bytecode-verified). Instantiation timing is class initialisation (row 16), hence INFERRED. |
| 26 | PreferenceActivityConfig$1.createFromParcel | REACHABLE proposed | INFERRED | Framework unparcel dispatch on PA:69 getParcelableExtra (R-PREF); body PAC:83-86 `return new PreferenceActivityConfig(source);` (row 17). Dispatch unprinted, hence INFERRED. |
| 27 | PreferenceActivityConfig$1.newArray | UNREACHABLE | INFERRED | Definition PAC:89-92 (`return new PreferenceActivityConfig[size];`). Framework calls newArray only when unmarshalling a Parcelable ARRAY; the only printed parcel sites are the single extra SF:239 / PA:69. Re-checked in this pass: no `getParcelableArrayExtra` site in any printed file. Resolves with: a printed array-extra site, or a saved full-repo grep. NOT UNREACHABLE on this evidence (the standard Parcelable array entry point). Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L2 verdict applied.] |
| 28 | SettingsActivity.<clinit> | REACHABLE proposed | INFERRED | Static field SA:35 (TAG, getSimpleName()). First printed use is MA:743 `new Intent(this, SettingsActivity.class)` in the settings menu handler. Class-init timing is the unprinted JVM rule, hence INFERRED. |
| 29 | SettingsActivity.<init> | REACHABLE proposed | INFERRED | Implicit default ctor (none declared in SA). Framework activity instantiation on MA:743 startActivity (R-SETTINGS); no printed `new SettingsActivity(...)` site exists, hence INFERRED. |
| 30 | SettingsActivity.lambda$onCreate$0 | REACHABLE proposed | INFERRED | LiveData observer lambda SA:58-61 (`viewModel.detailTitleChanged.observe(this, title -> {...})`, body :59-60 setText). Registered in printed onCreate, invoked by LiveData dispatch when SF.setFragment writes detailTitleChanged (SF:222) — library dispatch, unprinted, hence INFERRED. Numbering by source order (only lambda in onCreate), NOT bytecode-verified. |
| 31 | SettingsActivity.onCreate | REACHABLE proposed | INFERRED | Framework activity lifecycle on MA:743 startActivity (R-SETTINGS); body SA:42-62 printed (ViewModel :47, setContentView :49, toolbar :51-55, observer :58-61). Dispatch is framework, hence INFERRED. |
| 32 | SettingsActivity.onOptionsItemSelected | REACHABLE proposed | INFERRED | Framework menu dispatch (home button :67-68 finish()); body SA:65-72 printed, always returns true. Dispatch unprinted, hence INFERRED. |
| 33 | SettingsFragment.<clinit> | REACHABLE proposed | INFERRED | Static fields SF:49 (TAG) and :51-58 (section-name constants). First printed use in this route is the SettingsActivity settings UI (R-SETTINGS; SF is the host fragment whose onViewCreated registers the section preferences). Class-init timing is the unprinted JVM rule, hence INFERRED. Strict-entry caveat: see Caveats (attachment step unprinted). |
| 34 | SettingsFragment.<init> | REACHABLE proposed | INFERRED | Implicit default ctor (none declared in SF). Printed construction site SF:65 `new SettingsFragment()` inside newInstance :63-70, but newInstance itself has no printed caller in the files printed; fragment instantiation is otherwise framework (layout/transaction, unprinted). Hence INFERRED overall. Strict-entry caveat: see Caveats. |
| 35 | SettingsFragment.lambda$new$0 | REACHABLE proposed | INFERRED | Preference click-listener lambda SF:131-134 (`prefClickListener = (preference) -> { openPreference(preference.getKey()); return true; }`), an instance field initializer — hence the compiler name lambda$new$0 by the field-initializer convention, NOT bytecode-verified. Registered on every section preference in onViewCreated :100,104,108,112,116,120,124,128; invoked by framework Preference click dispatch (unprinted), hence INFERRED. |
| 36 | SettingsFragment.onAttach | REACHABLE proposed | INFERRED | Framework fragment lifecycle; body SF:73-79 printed (super.onAttach :75, activity capture :77-78). Dispatch unprinted, hence INFERRED. Strict-entry caveat: see Caveats. |
| 37 | SettingsFragment.onCreatePreferences | REACHABLE proposed | INFERRED | Framework fragment lifecycle; body SF:215-218 printed (setPreferencesFromResource(R.xml.pref_headers) :217 — this is what creates the preferences that row 35's listener is registered on). Dispatch unprinted, hence INFERRED. Strict-entry caveat: see Caveats. |
| 38 | SettingsFragment.onViewCreated | REACHABLE proposed | INFERRED | Framework fragment lifecycle; body SF:82-129 printed (ViewModel :88, two-pane default fragment :90-95, all eight setOnPreferenceClickListener registrations :100-128). Dispatch unprinted, hence INFERRED. Strict-entry caveat: see Caveats. |
| 39 | SettingsFragment.openPreference | REACHABLE proposed | SOURCE | Explicit printed call SF:132 `openPreference(preference.getKey());` inside row 35's listener. Definition SF:136-212 (switch over the 8 section names; small-screen branches call startActivity :144,153,162,171,180,189,198,207 — R-PREF — large-screen branches call row 40). |
| 40 | SettingsFragment.setFragment | REACHABLE proposed | SOURCE | Explicit printed calls SF:94-95 (two-pane default, onViewCreated) and SF:141,150,159,168,177,186,195,204 (large-screen branches of openPreference). Definition SF:220-230 (:222 detailTitleChanged.setValue — the trigger for SA row 30 — :224-228 fragment transaction, itself gated on isLargeScreenDevice :224). |

## OPEN rows and what would resolve them (3 rows, unchanged from prior proposal, re-checked)

- **PreferenceActivityConfig setters (rows 22, 23):** a printed setFragment/setTitle call site (neither SF nor PA calls them on the config object), or a saved full-repo grep. They are plain setters on a config object that IS constructed and parcelled on a printed route, so they stay OPEN, not UNREACHABLE.
- **PreferenceActivityConfig$1.newArray (row 27):** a printed site unmarshalling a PreferenceActivityConfig array (e.g. getParcelableArrayExtra), or a saved full-repo grep. The single-extra route (SF:239 / PA:69) never calls newArray, but that alone is not proof no array site exists.
- **General resolver:** a saved full-repo grep (not available in this pass — connector search_code was not used as absence evidence, per prior batches' lesson that it returns 0 even for existing strings).

## Caveats restated (merger must see)

1. Strict-entry caveat: (a) the LAUNCHER -> MainActivity step (AndroidManifest) was NOT freshly re-printed in this pass, so under a strict rule the TagsAdapter holder rows (1-9) and the whole settings trunk (MA:743 -> SA -> SF) revert to OPEN until the manifest + MainActivity.onCreate chain is re-printed at merge; (b) the step attaching SettingsFragment to SettingsActivity (layout or transaction) was NOT printed, so under a strict rule SF rows 33-40 revert to OPEN until activity_settings layout (or a transaction site) is printed. The PreferenceActivity route (R-PREF) does NOT depend on (b): it is anchored at SF.startActivity, which is printed, but it does depend on (a) via MA:743.
2. Two-pane gate: PA.onCreate finishes immediately on large-screen devices (PA:58-61), so the PreferenceActivity fragment route (rows 12, 15, 17, 26) runs only on small screens; on large screens the equivalent route is SF.setFragment (row 40). Both branches are printed, so this is a configuration branch, not an OPEN row — but a device check on a large-screen config would not exercise rows 12/15/17/26.
3. No row is verified for merge: no build, sampler, grep, or C1 check was run (no local checkout). A merge step must re-derive every row from a full checkout, run the C1 checks, print the manifest + activity_settings attachment, confirm lambda/anonymous numbering (rows 3-5, 9, 25, 30, 35) against bytecode, run a saved full-repo grep for rows 22/23/27, and spot-check at least 1 in 5 citations. Build/C1: not run (Mac after push).
4. SettingsFragment.newInstance (SF:63-70) and SettingsViewModel are NOT batch rows and are not judged here; newInstance is cited only as the internal construction site for row 34.
5. Undecided conventions recorded, not decided: per-row SOURCE vs whole-route INFERRED (see convention note above); strict-entry rule (caveat 1); two-pane gate treatment (caveat 2). Labels are unaffected by the confirmed_by choice.
6. No connector search_code result was used as evidence of absence. No fresh HTTP 429 was hit in this pass (the single fresh fetch this session was Utils.java for batch 113, which succeeded; no fresh fetch was needed for batch 114 beyond the re-reads above).
