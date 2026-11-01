**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 117 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED merge-ready part only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to `graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**

**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push, so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1 check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).

- Scope: batch 117 only, 40 methods, no other batch, no other app, no device replay, no Aegis.

- Source: existing proposal `~/workspace/libretorrent-batch117-proposal.md` used as an INPUT, not a result. Membership was re-verified in this pass against the local plan copy `~/workspace/agent27-plan.tsv` (4,733 lines incl. header; plan blob SHA `0104806dd666c840049b3db52823d4b384fa1c92`): all 40 plan methods match the table below in plan order, all TODO_CANDIDATE_REACHABLE.

- Printed source: prior-session connector prints saved in `~/workspace/batch117-118-src/` (Limitations, Network, Proxy, Scheduling, Storage, Streaming, SettingsFragment, SelectTagActivity, SelectTagDialog, TorrentTagsList, AddTagButton — one file at a time in that pass). In this pass the table citations were spot-checked against those saved copies (see Spot-checks below), and one file was freshly re-fetched from branch `work-2026-10-31` with a 30 s pause and found byte-identical: `ui/settings/SettingsFragment.java` (10,437 bytes, no diff vs the saved copy). No fresh HTTP 429 was hit in this pass. Remaining files were NOT freshly re-fetched in this pass — the merger must still confirm the trunk line numbers against a fresh branch print if it requires fresh evidence for every row, but no row below rests on a search_code result or on an unprinted caller.

- Counts (mechanically verified): **40 REACHABLE proposed / 0 UNREACHABLE proposed / 0 OPEN**, 40/40 rows judged, sequence 1–40 intact. confirmed_by: 14 SOURCE / 26 INFERRED, never DYN, FW-MEMORY, or UNVERIFIED.

- OPEN/disputed rows: NONE. There were no OPEN rows in the batch 117 proposal to re-derive, and no disputed row was left by the prior pass. No row is claimed UNREACHABLE in this batch: no saved full-repo grep was run, and absence of a printed caller was never treated as proof of absence. No search_code 0-result was used as evidence of absence.


## Per-row judgements (carried from the proposal table, membership and citations spot-checked in this pass)

| # | Method | Label proposed | confirmed_by | Printed citation / route |
|---|---|---|---|---|
| 1 | LimitationsSettingsFragment.newInstance | REACHABLE | SOURCE | Def `:44-49` (`new LimitationsSettingsFragment()`). Called by SettingsFragment.java:177 (large-screen branch). |
| 2 | LimitationsSettingsFragment.onCreate | REACHABLE | INFERRED | Def `:53-167` (loads repo, binds every preference). Fragment lifecycle after row 1; dispatch unprinted. |
| 3 | LimitationsSettingsFragment.onCreatePreferences | REACHABLE | INFERRED | Def `:169-171` (`setPreferencesFromResource(R.xml.pref_limitations, rootKey)`). Framework calls it; dispatch unprinted. |
| 4 | LimitationsSettingsFragment.onPreferenceChange | REACHABLE | INFERRED | Registered via `bindOnPreferenceChangeListener` (`:174-176`, `setOnPreferenceChangeListener(this)`), called in onCreate at `:80,:91,:102,:109,:120,:131,:142,:153,:164`. Def `:180-245`. Dispatch unprinted. |
| 5 | LimitationsSettingsFragment.parseMaxConnectionValue | REACHABLE | SOURCE | Def `:247-256`. Called from onPreferenceChange at `:183` (max connections) and `:188` (max connections per torrent). |
| 6 | NetworkSettingsFragment.<clinit> | REACHABLE | INFERRED | Static `TAG = NetworkSettingsFragment.class.getSimpleName()` (`:70`) — non-constant, so class initialisation runs on first use via row 17. No <clinit> body is written in source. |
| 7 | NetworkSettingsFragment.<init> | REACHABLE | SOURCE | Implicit default ctor, called by `newInstance` `:78` (`new NetworkSettingsFragment()`). |
| 8 | NetworkSettingsFragment.bindOnPreferenceChangeListener | REACHABLE | SOURCE | Def `:299-301` (`setOnPreferenceChangeListener(this)`). Called in onCreate at `:115,:122,:129,:136,:143,:154,:166,:176,:184,:192,:199,:224,:268,:275`. |
| 9 | NetworkSettingsFragment.fileChooseDialog | REACHABLE | SOURCE | Def `:284-297` (Intent to FileManagerDialog, `fileChoose.launch(i)` `:296`). Called by the ip-filter click lambda `:214` (row 14). |
| 10 | NetworkSettingsFragment.lambda$new$5 | REACHABLE | INFERRED | `fileChoose` ActivityResult callback body `:381-403` (RESULT_OK → `pref.ipFilteringFile`, summary update). Launched via row 9; result dispatch unprinted. Field-declaration order after the onCreate lambdas gives $5; confirm against bytecode. |
| 11 | NetworkSettingsFragment.lambda$new$6 | REACHABLE | INFERRED | `anonymousModeActivity` ActivityResult callback body `:405-413` (refreshes anonymous-mode summary). Launched from the anonymous-mode click branch (row 16); dispatch unprinted. |
| 12 | NetworkSettingsFragment.lambda$onCreate$0 | REACHABLE | INFERRED | Port-start bind lambda `:163` (`editText.setFilters(portFilter)`), registered by `setOnBindEditTextListener`. Dialog-binding dispatch unprinted. |
| 13 | NetworkSettingsFragment.lambda$onCreate$1 | REACHABLE | INFERRED | Port-end bind lambda `:173`, same pattern as row 12. |
| 14 | NetworkSettingsFragment.lambda$onCreate$2 | REACHABLE | INFERRED | IP-filter-file click lambda `:212-216` (calls row 9, returns true). Signature `(Preference)Z` matches. Click dispatch unprinted. |
| 15 | NetworkSettingsFragment.lambda$onCreate$3 | REACHABLE | INFERRED | Proxy click lambda `:229-237` (large → row 23 + Proxy row 33; small → row 24). Click dispatch unprinted. |
| 16 | NetworkSettingsFragment.lambda$onCreate$4 | REACHABLE | INFERRED | Anonymous-mode click lambda `:246-262` (large → `setFragment(AnonymousModeSettingsFragment.newInstance())` `:248`; small → PreferenceActivity Intent + `anonymousModeActivity.launch(i)`). Click dispatch unprinted. |
| 17 | NetworkSettingsFragment.newInstance | REACHABLE | SOURCE | Def `:77-82`. Called by SettingsFragment.java:159 (large-screen branch). |
| 18 | NetworkSettingsFragment.onAttach | REACHABLE | INFERRED | Def `:86-91` (captures AppCompatActivity). Framework lifecycle; dispatch unprinted. |
| 19 | NetworkSettingsFragment.onCreate | REACHABLE | INFERRED | Def `:104-278` (loads repo/fs, finds and binds all network preferences). Lifecycle after row 17. |
| 20 | NetworkSettingsFragment.onCreatePreferences | REACHABLE | INFERRED | Def `:280-282` (`setPreferencesFromResource(R.xml.pref_network, rootKey)`). |
| 21 | NetworkSettingsFragment.onPreferenceChange | REACHABLE | INFERRED | Registered via row 8. Def `:304-359` (port range, DHT/LSD/uTP/UPnP/NAT-PMP, encryption modes, IP filtering, seeding, tracker validation). Dispatch unprinted. |
| 22 | NetworkSettingsFragment.onViewCreated | REACHABLE | INFERRED | Def `:94-101` (`new ViewModelProvider(activity).get(SettingsViewModel.class)`). Lifecycle; dispatch unprinted. |
| 23 | NetworkSettingsFragment.setFragment | REACHABLE | SOURCE | Def `:361-369` (transaction replace of detail container, large-screen guard). Called at `:231` (Proxy) and `:248` (anonymous mode). |
| 24 | NetworkSettingsFragment.startActivity | REACHABLE | SOURCE | Def `:371-378` (Intent to PreferenceActivity + config, `startActivity(i)` `:378`). Called at `:234` (Proxy, small screen). |
| 25 | ProxySettingsFragment.<clinit> | REACHABLE | INFERRED | Static `TAG = ProxySettingsFragment.class.getSimpleName()` (`:49`); class initialisation on first use via row 33. |
| 26 | ProxySettingsFragment.<init> | REACHABLE | SOURCE | Implicit default ctor, called by `newInstance` `:57` (`new ProxySettingsFragment()`). |
| 27 | ProxySettingsFragment.bindOnPreferenceChangeListener | REACHABLE | SOURCE | Def `:177-179`. Called in onCreate at `:109` (type), `:118` (address), `:131` (port), `:139` (peers too), `:147` (requires auth), `:157` (login), `:167` (password). |
| 28 | ProxySettingsFragment.enableOrDisablePreferences | REACHABLE | SOURCE | Def `:182-204` (enables/disables address, port, peers-too, requires-auth). Called from onPreferenceChange `:213` when proxy type changes. |
| 29 | ProxySettingsFragment.lambda$onCreate$1 | REACHABLE | INFERRED | Port bind lambda `:129-131` (`editText.setFilters(portFilter)`). $ numbering: $0 is the onViewCreated save-button click (row 32, first lambda in file order), so the first onCreate lambda is $1; confirm against bytecode. |
| 30 | ProxySettingsFragment.lambda$onCreate$2 | REACHABLE | INFERRED | Password bind lambda `:165-167` (`setTransformationMethod(PasswordTransformationMethod.getInstance())`). |
| 31 | ProxySettingsFragment.lambda$onPreferenceChange$3 | REACHABLE | INFERRED | Password-branch bind lambda `:232-234` (summary from the transformation of the new value), registered inside onPreferenceChange. |
| 32 | ProxySettingsFragment.lambda$onViewCreated$0 | REACHABLE | INFERRED | Save-button click lambda `:74-78` (`pref.applyProxy(true)`, `proxyChanged = false`). First lambda in file order, hence $0. Click dispatch unprinted. |
| 33 | ProxySettingsFragment.newInstance | REACHABLE | SOURCE | Def `:56-61`. Called by NetworkSettingsFragment.java:231 (large-screen proxy branch). |
| 34 | ProxySettingsFragment.onCreate | REACHABLE | INFERRED | Def `:95-170` (loads repo, proxy type/address/port/peers/auth/login/password, binds listeners). Lifecycle after row 33. |
| 35 | ProxySettingsFragment.onCreatePreferences | REACHABLE | INFERRED | Def `:172-174` (`setPreferencesFromResource(R.xml.pref_proxy, rootKey)`). |
| 36 | ProxySettingsFragment.onDestroy | REACHABLE | INFERRED | Def `:82-93` (shows "apply after reboot" toast if `proxyChanged`). Lifecycle; dispatch unprinted. |
| 37 | ProxySettingsFragment.onPreferenceChange | REACHABLE | INFERRED | Registered via row 27. Def `:206-245` (writes every proxy setting, calls row 28 on type change, sets `proxyChanged = true`). Dispatch unprinted. |
| 38 | ProxySettingsFragment.onViewCreated | REACHABLE | INFERRED | Def `:66-79` (finds coordinator layout + save button, shows it, registers row 32). Lifecycle; dispatch unprinted. |
| 39 | SchedulingSettingsFragment.<init> | REACHABLE | SOURCE | Implicit default ctor, called by `newInstance` `:54` (`new SchedulingSettingsFragment()`). File printed in full in this pass. |
| 40 | SchedulingSettingsFragment.bindOnPreferenceChangeListener | REACHABLE | SOURCE | Def `:169-171`. Called in onCreate at `:73` (enable start), `:80` (enable stop), `:87` (start time), `:94` (stop time), `:101` (run only once), `:108` (switch WiFi). |

## Spot-checks done in this pass (against ~/workspace/batch117-118-src/ saved copies)
- SettingsFragment trunk: `openPreference` branches confirmed — Network newInstance :159 / startActivity :162, Storage :168/:171, Limitations :177/:180, Scheduling :186/:189, Streaming :204/:207; click listeners register via `prefClickListener` calling `openPreference(preference.getKey())` (:132); `setFragment` :220-229, `startActivity` :232-240.
- Limitations: `newInstance` :44, `bindOnPreferenceChangeListener` registrations :80,:91,:102,:109,:120,:131,:142,:153,:164, `parseMaxConnectionValue` called :183 and :188, defined :247.
- Network: Proxy branch `setFragment(ProxySettingsFragment.newInstance())` :231, small-screen `startActivity(ProxySettingsFragment.class)` :234, `setFragment` :361-369, `startActivity` :371-378.
- Proxy: `newInstance` :56, `enableOrDisablePreferences` defined :182, called :213.
- Scheduling (rows 39–40 only in this batch): `newInstance` :54 is the ctor call site for row 39; row 40's bind method is defined in the Scheduling file (see batch 118 for its onCreate call sites).

## Caveats the merger must see (undecided conventions recorded, not decided)
1. **Strict-entry caveat (all rows):** the launcher → SettingsActivity → SettingsFragment step was NOT printed in the prior pass and was not freshly printed in this pass. Under a strict launcher-entry rule all section rows (117 rows 1–40; 118 rows 1–33) revert to OPEN. They are judged REACHABLE on the printed settings trunk, the same convention as sibling settings batches 115–116. The merger must pick one entry convention for all settings batches.
2. **Small-screen dispatch:** `PreferenceActivity.getFragment` dispatch was NOT freshly printed; the large-screen `newInstance()` call sites are printed direct call sites and are sufficient for the SOURCE marks. If the merger requires the small-screen dispatch printed, those rows weaken to INFERRED, not to OPEN/UNREACHABLE.
3. **Lambda numbering:** `$n` numbering is source-order sequential, NOT bytecode-verified — confirm at merge; a swap within a group does not change any label, but the cited body must be re-matched (notably Network $5/$6 ActivityResult callbacks and Proxy $0/$1/$2/$3).
4. **Proxy trunk:** Proxy is reached via the Network fragment's proxy click (:227-237), not via a SettingsFragment entry — do not re-route it through SettingsFragment.
4. **confirmed_by convention:** SOURCE = a printed direct in-app call site naming the method (or a printed registration/call in the same file for a private helper); INFERRED = reached only through unprinted framework/library dispatch (fragment lifecycle, preference-change/click/bind-text listeners, ActivityResult callbacks, class initialisation) where definition + registration are printed but dispatch itself is not printed from fw_src. This is the per-row convention, not a whole-route convention; labels are unaffected, only confirmed_by would change at merge if the merger adopts the whole-route convention.
5. **Not claimed:** no build, sampler, full-repo grep, or C1 — no full local checkout (git clone of the private repo still fails in this VM with no credential device, named missing check, not passed). Main-agent spot-check (1 in 5), py_compile, build, and Mac build/C1 are still owed before merging. **0 rows verified for merge.**
