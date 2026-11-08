# Gating review — AnyMemo schema 2 conversion (round 2)

Reviewer: gating reviewer. Verified against the app Java source and the built graph, not the implementer's
narrative. Binding spec: handoff/KIRO_SESSION_ANYMEMO.md. Working dir: /Users/darshan/Desktop/yang/work.
All spot-checks below were run read-only (sed -n on source ranges, grep -c on graph_def.py, one show_route,
json.load on the trigger graph). The full build/tool battery was NOT re-run; recorded outputs were read.

Verdict: **CHANGES_REQUESTED** — one explicit, literal gate stated in items (a) and (e) fails
(`grep -c "PENDING" graphs/AnyMemo/graph_def.py` == 7, the brief requires 0). All other substance verified and holds.

---

## Item (a): the six STEP 1 placeholders

STEP 1 region of graph_def.py (lines ~1812–1840) now carries real, source-cited verdicts for all six; the
round-1 placeholder markers are gone (`grep -c "PENDING (round 1)"` = 0, `grep -c "round 1 PENDING"` = 0).

Spot-checks against source (all confirmed):
- **1e CardEditor.onConfigurationChanged** — graph_def.py:~1841 adds `S_CARD_EDITOR -> CardEditor.onConfigurationChanged`
  SYSTEM "rotate the device", evidence `SRC ui/CardEditor.java:415-418`. sed -n 415,418p ui/CardEditor.java shows
  `@Override / public void onConfigurationChanged(Configuration newConfig) { / super.onConfigurationChanged(...)`.
  The class DOES declare the method. **Confirmed.** (confirmed)
- **1f SettingsScreen.onConfigurationChanged** — edge cites `SRC ui/SettingsScreen.java:154-157`; sed -n 154,157p
  shows the `@Override onConfigurationChanged` declaration. **Confirmed.** (confirmed)
- **1c QuizLauncherDialogFragment.onDestroy** — edge `S_DLG_QUIZ_LAUNCHER -> ...onDestroy` FRAMEWORK, cites
  `ui/QuizLauncherDialogFragment.java:55 (extends BaseDialogFragment), 133-134 (onDestroy); no dismiss()/setCancelable
  in the file; INFERRED androidx DialogFragment`. sed -n 133,134p shows `public void onDestroy() { super.onDestroy();`
  and grep for dismiss/setCancelable/setCanceledOnTouchOutside on the file returns nothing (exit 1). The INFERRED
  androidx cancel→destroy order is labelled INFERRED in the evidence. **Confirmed.** (confirmed)
- **1a CategoryEditorFragment.onDestroy** — edge `CategoryEditorFragment$1.onClick -> ...onDestroy` LIFECYCLE,
  guard `v == okButton`, cites `ui/CategoryEditorFragment.java:94-108 (dismiss at 108); INFERRED androidx`. sed -n
  94,108p shows the OK-path handler ending in `dismiss();`. Fragment-destroy is INFERRED. **Confirmed.** (confirmed)
- 1b (PreviewEditActivity, restartActivity finish at :462 + Back) and 1d (CardListActivity, Back only, restartActivity
  UNREACHABLE) read as sound from the cited evidence strings and the fix log; not line-reprinted beyond the two
  required spot-checks, but consistent with the surrounding LIFECYCLE pattern. (likely)

Fragment-destroy entries (1a, 1c) are labelled INFERRED; onConfigurationChanged edges (1e, 1f) exist only because
the class declares the method (verified in source). All correct.

**BLOCKING sub-requirement FAILS**: item (a) states "grep -c \"PENDING\" graph_def.py == 0". Actual = **7**
(confirmed by `grep -c "PENDING" graphs/AnyMemo/graph_def.py`). The 7 hits are the pre-existing `C3_LIB_PENDING`
constant (graph_def.py:2080) and its six evidence uses (:2246, :2248, :2264, :2266, :2282, :2284), the androidx
ViewDataBinding "pending-bindings pass" text. Confirmed pre-existing: scratch/graph_def_before_round2.py has 9
PENDING (these 7 + the 2 round-1 markers that STEP 1 correctly removed). (confirmed)

The implementer's fix log and a prior orchestrator "waived" this gate as unsatisfiable without a forbidden rename
of C3_LIB_PENDING. That reasoning is defensible, but the binding spec I must verify against states the gate
literally as `== 0`, with no waiver clause. The spec's instruction is explicit that the implementer's narrative is
not the standard. The gate does not hold as written, so item (a) does not pass. A fix must either (i) obtain an
explicit relaxation of this gate recorded in the binding spec itself, or (ii) rename `C3_LIB_PENDING`
(graph_def.py:2080) and reword its six uses (:2246, :2248, :2264, :2266, :2282, :2284) if that edit is authorized.

## Item (b): the ten STEP 2 automatic-edge pairs

All ten are classified "present" in scratch/fix_round2.md, with per-host @AM/@DBX variants where applicable. No hand
edges were added, so there is no CALL-dedup reconciliation to check (build_graph.py:223 is not triggered).

Spot-checks against out/anymemo_trigger_graph.json (json.load) and source:
- **Item 5 onViewCreated -> refreshList**: edges E553e8d3a (@AM) and E2fbadfb0 (@DBX), both CALL,
  `AbstractDownloaderFragment.onViewCreated@* -> AbstractDownloaderFragment.refreshList@*`. Source
  downloader/common/AbstractDownloaderFragment.java:172 is `refreshList();` inside onViewCreated. auto_calls.json
  has exactly one onViewCreated→refreshList call row. **Present, confirmed.** (confirmed)
- **Item 10 DropboxOauth2AccountActivity.onCreate -> Oauth2AccountActivity.onCreate**: edge Eba2af780 CALL.
  Source downloader/dropbox/DropboxOauth2AccountActivity.java:21 is `super.onCreate(savedInstanceState);`.
  **Present, confirmed.** (confirmed)
- **Item 9 DropboxListActivity.refreshList -> AbstractDownloaderFragment.refreshList**: edge E7bad5c55 CALL
  (-> refreshList@DBX). Source downloader/dropbox/DropboxListActivity.java:95 is `fragment.refreshList();`.
  **Present, confirmed.** (confirmed)
- **Item 1 showFetchDatabaseDialog**: edges E30961aed (@AM), E72ef4f0f (@DBX), both CALL. **Present, confirmed.** (confirmed)

Each spot-checked pair yields exactly the CALL edge(s) claimed. Item (b) holds.

## Item (c): the final 30-route sample

Final draw scratch/kiro_sample_30_final.txt has 30 methods; count logged correct 30 / fixed 0 / wrong 0 / unclear 0
(error rate 0.0).

- **Comma-citation route (required)**: the FileBrowser adapter edge cites `ui/FileBrowserFragment.java:594, 480`
  (the show_route.py comma-truncation bug). Printed each range by hand: :594 is `public void setItems(List<String>
  items) {`, :480 is `public void onBindViewHolder(ViewHolder holder, final int position) {`. The RecyclerView
  rebinds rows when the adapter data is set; judgment "correct, INFERRED androidx" holds. (confirmed)
- LearnQueueManager.java:267 is `throw new RuntimeException("...: " + card);` — the `+ card` is the Card.toString
  site (Card.toString declared at entity/Card.java:153). Route judgment holds. (confirmed)
- show_route BaseActivity.onResume: traces S_ENTRY → AnyMemo.<init> (MAIN/LAUNCHER, AndroidManifest.xml:23-46) →
  onCreate → ... lifecycle, every step source-cited. "correct" holds. (confirmed)

Item (c) holds for the spot-checked routes.

## Item (d): verification.csv

- Header is EXACT: `type,item,result,confirmed_by,ref,edges,note`. (confirmed)
- Row counts: 30 path, 271 label, 45 edge. Of the 271 label rows, **241** correspond to the graph's UNREACHABLE
  methods and 30 to the sampled reachable methods. (confirmed)
- make_verification.py uses only paths under graphs/AnyMemo/ or tools/ (grep for /private/tmp, /tmp/, session,
  /Users/ finds only two comment lines, no real path). (confirmed)
- Self-check / STALE: the final build (scratch/kiro_build_final.txt) shows `verification label checked 271 errors 0`,
  `verification edge checked 45 errors 7` (the 7 STEP-1 "fixed" edges, by design), `verification path checked 30
  errors 0`, and no STALE/WARN line (only "warnings: 0"). (confirmed)

**Discrepancy vs the brief text**: item (d) says "247 'label' rows for UNREACHABLE methods". Actual = **241**.
This is source-correct, not an error: STEP 1 moved the six placeholders from UNREACHABLE to REACHABLE
(247 − 6 = 241), and the build confirms UNREACHABLE 241. The "247" in the brief is the pre-STEP-1 count, and item
(a) (resolving the six) and item (d) (keeping 247) cannot both be satisfied literally — resolving six placeholders
to REACHABLE necessarily drops UNREACHABLE to 241. The implementer chose the source-correct 241 and the label set is
verified set-equal to the graph's UNREACHABLE set. I treat this as NON-BLOCKING (the brief is internally
inconsistent here and 241 is the source-grounded answer), but flag it so the decision-maker can confirm the intent. (confirmed)

## Item (e): STEP 8 checks

From the recorded outputs:
- build: errors 0, warnings 0 (kiro_build_final.txt). PASS. (confirmed)
- check_citations: "33 distinct, 0 problems; ... FW-MEMORY / DYN / UNVERIFIED: 0" (kiro_check_citations.txt). PASS. (confirmed)
- check_routes: **1 route flagged** (FileBrowserFragment$3.<init>) (kiro_check_routes.txt). The brief's item (e)
  allows a flagged route if "explained in readme_notes.md" — it is, under "## Limits" (false positive of the
  `result` heuristic: the picker edge's ENV text mentions RESULT_CANCELED for the device-less baseline while the
  next guard needs RESULT_OK; on a real API 27 device these do not contradict). Satisfies the escape clause. PASS. (confirmed)
- check_bytecode_lines: "0 where the cited line does not show the callee" (kiro_check_bytecode.txt). PASS. (confirmed)
- check_v2: "apps with problems: 0"; AnyMemo (and Markor) are schema-2 hand-written and skipped by the old tool
  (kiro_check_v2.txt). As expected. (confirmed)
- `grep -c "DEAD\|FRAMEWORK_ONLY"` = 0. PASS. (confirmed)
- `grep -c "PENDING"` = **7**, gate requires 0. **FAIL** (same blocking finding as item (a)). (confirmed)

## Item (f): final build

methods 2207, pages 77, edges 4492, REACHABLE 1966, UNREACHABLE 241 (branch_never_taken 7, framework_never_calls 18,
no_trigger_in_app 216), errors 0, warnings 0 (kiro_build_final.txt). Build is clean. Item (f) holds. (confirmed)

## NEVER / STOP / file-set compliance

- **Allowed-edit set only**: graph_def.py, make_verification.py, verification.csv, readme_notes.md, LESSONS.md all
  carry round-2 mtimes (2026-10-27 17:51–18:25); AGENT_NOTES.md updated. tools/ has NO file modified after
  2026-10-27 17:30 (round-2 window); graphs/Aegis and graphs/Markor were not touched by this agent within the
  window (Aegis/graph_def.py at 18:01 is the concurrent Aegis agent's work, isolated from graphs/AnyMemo/).
  handoff/ changes are logs/briefs outside this agent's edits. **Compliant.** (confirmed)
- **readme_notes.md headings**: exactly the five required headings, in order (re-audit changed / how paths chosen /
  waits for a device / hazard candidates / limits). Hazard list is short and source-printed. **Compliant.** (confirmed)
- **AGENT_NOTES.md**: STEP 9 permits one appended line; the tail shows exactly one new 2026-10-27 round-2 line
  ("DONE. ... see scratch/fix_round2.md"); older text untouched. **Compliant.** (confirmed)
- **No coverage cited as a round-2 label**: one UNREACHABLE entry, DataBindingTriggerClass.<init>
  (graph_def.py:2938), ends its reason with "coverage_baseline monkey and ape both false", and that phrase is echoed
  into verification.csv. This is PRE-EXISTING (present verbatim in scratch/graph_def_before_round2.py:2925 and the
  round-1 baseline) and is the ONLY such citation. The round-2 agent added no coverage-cited label. The label's
  primary reason is source-grounded (no invoke site of the ctor in the app bytecode). Out of round-2 scope;
  INFORMATIONAL, not blocking. Worth noting for a future pass that the trailing coverage phrase technically violates
  the NEVER rule and could be trimmed if/when that line is ever in scope. (confirmed)

---

## Findings

1. **PENDING gate fails (BLOCKING, items a + e / STEP 8 item 7)** — `grep -c "PENDING" graphs/AnyMemo/graph_def.py`
   == 7, the brief requires 0. All 7 are the pre-existing `C3_LIB_PENDING` constant (graph_def.py:2080) and its six
   evidence uses (:2246, :2248, :2264, :2266, :2282, :2284). STEP 1's own placeholder markers are gone
   (`PENDING (round 1)` / `round 1 PENDING` both 0), so the gate's intent is met, but the literal gate the spec
   states is not. Fix: either record an explicit relaxation of the `grep == 0` gate for the pre-existing
   C3_LIB_PENDING token in the binding spec, or (if authorized) rename C3_LIB_PENDING at graph_def.py:2080 and
   reword its six uses so the literal count reaches 0, then rebuild (expect errors 0/warnings 0) and re-run STEP 8.

2. **UNREACHABLE label count 241 vs brief's 247 (NON-BLOCKING, item d)** — verification.csv has 241 UNREACHABLE
   label rows, not 247, because STEP 1 resolved six placeholders to REACHABLE (247−6=241) and the graph's
   UNREACHABLE set is 241. Source-correct; the brief's 247 is the pre-STEP-1 figure and conflicts with item (a).
   Confirm the decision-maker accepts 241 as the intended count.

3. **Pre-existing coverage phrase in one label's evidence (INFORMATIONAL, out of round-2 scope)** —
   DataBindingTriggerClass.<init> (graph_def.py:2938) ends with "coverage_baseline monkey and ape both false",
   echoed into verification.csv. Pre-existing and not added this round; the label is otherwise source-grounded.
   Could be trimmed when that line is next in scope.
