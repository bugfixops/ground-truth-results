# Aegis C3 sample-fix step — FIX_REPORT (continuation merger, 2026-11-01)

Status: fixes 1–4 applied and verified in the merger's private
tree; redrawn sample judged fresh by 9 helpers; FINAL table
built. STOP after the final table — NO PUSH made. Independent
fix audits follow this delivery; the C3 push, then C4 logs,
then D1/D3/D7, then F1-readiness come after those audits PASS.
No F1 claim, no PROGRESS line.

## 1. Fixes applied (one at a time; edit, rebuild, reprint each)

All builds in `merger/tree` (`python3 -I tools/build_graph.py
graphs/Aegis aegis`). Baseline before fixes: methods 2995,
REACHABLE 2537, UNREACHABLE 458, edges 5782, errors 0,
warnings 0. Backup of pre-fix graph_def.py:
`merger/backup-pre-samplefix/graph_def.py`.

### Fix 1 — CustomSvgIcon installer split (J1 design, extended)

Design verified against printed source, then EXTENDED: the
judging design split create/loadIcons/lambda$2 by installer,
but printed source shows two more paths it missed — the
IconPickerDialog$1 forwarder (the adapter's listener is always
the $1 instance created in create(), IconPickerDialog
.java:53–66, forwarding to the installing activity's listener
:62–64) and the search-clear path (setQuery(null) reloads with
showAddCustom false, IconAdapter.java:92–96). Both split too,
or the @ASSIGN prefix would still reach EditEntryActivity$1
through the shared forwarder / shared search reload.
Edits: create @EDIT (startIconSelection, showAddCustom true,
:594) / @ASSIGN (onAssignIconEntryClick, false, :194);
loadIcons @EDIT/@ASSIGN; popup lambdas $2/$1 @EDIT/@ASSIGN
(pack switch keeps the flag, :138); shared create machinery
replicated onto both variants (focus $0, watcher $2 ×3,
preloader, span $3, IconRecyclerView <init>/onMeasure; auto
constructor edges replicate on their own); loadIcons framework
edges replicated with onBindViewHolder split; category-header
tap $3 replicated shared from both variants; dispatch split
direct (lambda$2@EDIT → EditEntry$1, @ASSIGN → AssignIcons$1
empty dead-end) AND forwarder ($1@EDIT → EditEntry$1,
$1@ASSIGN → AssignIcons$1); search-clear sup'd and re-routed
to loadIcons@NOCUSTOM → onBindViewHolder@NOCUSTOM with NO
onCustomSelected dispatch. Base chain left unfed (both callers
use variants); its edges stay as documentation, per the
@APP/@FILE precedent. Residual (recorded, out of scope):
onIconSelected dispatch stays shared (cannot reach
CustomSvgIcon) — it later produced the selectIcon WRONG in
the redrawn sample (see §5).
First build after the edit: 2 errors / 2 flips (lambda$3 +
setIsCollapsed UNRESOLVED — the category tap had not been
replicated); fixed by replicating the $3 gui edges, rebuilt.
Build after fix 1: 2995, 2537/458, edges 5900 (+118), errors
0, warnings 0, label flips 0. Eight checks: check 2: 22
distinct, 0 problems; check 3: 0 flagged; check 4: 3915
checked, 317 skipped, 159 implicit, 0 not-show; checks 5–7:
check_v2 skips schema-2 Aegis, 0 problems; check 8 --all: 0
with no other mention; --callers: 0 of 458; STRICT line 10 =
True. Redump CustomSvgIcon.<init> (26 steps): edit page →
icon click → startIconSelection → startImageSelectionActivity
(empty icon-packs branch, :590) → chooser → SVG →
ImportFileTask@SVG_PICK → lambda$new$0 → CustomSvgIcon
.<init>; 0 AssignIcons mentions. Graph reachability check:
AssignIcons prefix reaches CustomSvgIcon = False, reaches
EditEntry$1.onCustomSelected = False, reaches AssignIcons$1
= True (dead end); EditEntry prefix reaches CustomSvgIcon
and EditEntry$1 = True.

### Fix 2 — AndOtp processImporterState @FILE split (J4 design)

Note: the helper's "@APP-variant edge" wording does not exist
as such — the dumped step 35 was the SHARED auto CHA edge
(processImporterState → AndOtp decrypt, :179), so a bare sup
would have killed the genuine @FILE path too. The fix splits
instead: startImportFile feeds processImporterState@FILE (new)
and the base node (hand replacement of the auto :134 edge,
for all other importers); the auto CHA edge to AndOtp decrypt
is sup'd; only the @FILE variant reaches AndOtp decrypt,
guarded by supportsDirect false (DatabaseImporter.java:35),
getAppPath throws (AndOtpImporter.java:59–62), and read →
EncryptedState on non-JSON (AndOtpImporter.java:76–80).
Build after fix 2: 2995, 2537/458, edges 5913 (+13), errors 0,
warnings 0, flips 0. Eight checks: check 2: 22/0; check 3: 0;
check 4: 3926 checked, 318 skipped, 159 implicit, 0 not-show;
checks 5–7: schema-2 skip, 0 problems; check 8: 0 / 0 of 458;
STRICT True. Redump decryptNewFormat: pref_import → @FILE
dialog → file picker → ImportFileTask → SIE@FILE →
onCreate@FILE → startImport@FILE → startImportFile →
processImporterState@FILE → AndOtp decrypt → @ANDOTP dialog
chain → decryptNewFormat; 0 @APP/GA mentions. Caveat: the
@FILE dialog pick step does not name the andOTP row (the
graph's existing @FILE abstraction level); the route is
genuine (pick andOTP row, pick an andOTP file) but the pick
is satisfiable, not established — h1 later graded the
redrawn route UNCLEAR partly on this step-37 gap.

### Fix 3 — Aegis decrypt@IMPORT onto @FILE variant (J8 design)

The :1291 hand edge moved from base processImporterState to
processImporterState@FILE (fed by startImportFile since fix
2); guard/evidence updated to the @FILE Aegis facts
(supportsDirect false, DatabaseImporter.java:34; getAppPath
throws, AegisImporter.java:39–42; read returns EncryptedState
for an encrypted vault file, AegisImporter.java:44–52). The
auto CHA edge to Aegis decrypt stays suppressed by this hand
edge's base pair, as before. The @APP prefix must NOT be
"fixed" for this target (Aegis is excluded from the direct
dialog).
Build after fix 3: 2995, 2537/458, edges 5913 (unchanged —
the edge moved, not added), errors 0, warnings 0, flips 0.
Eight checks: check 2: 22/0; check 3: 0; check 4: 3926/318/
159/0; checks 5–7: schema-2 skip, 0 problems; check 8: 0 / 0
of 458; STRICT True. Redump getKey: the dumped route is now
the 17-step AUTH path (MainActivity.onStart →
startAuthActivity (ENCRYPTED edge) → AuthActivity →
password-slot decrypt task → getKey), NOT the importer path
— the router prefers it once the @APP splice is gone. That
path is genuine (getKey runs on every password unlock,
AuthActivity.java:356); its only caveat is the cross-run
ENCRYPTED step-8 state, so it grades UNCLEAR at best under
the strict convention, never WRONG. The @FILE importer path
to getKey still exists (verified: startImportFile reaches
getKey) and is genuine.
Reachability audit note: a BFS still finds base
processImporterState → decrypt@IMPORT, but ONLY the long way
around (base → processDecryptedImporterState → icon
optimisation → MainActivity → Settings → file import → @FILE
chain → @FILE variant → decrypt@IMPORT). That is a genuine
two-import execution, not a surviving splice: every path to
decrypt@IMPORT now passes through a @FILE segment. The same
holds for AndOtp after fix 2.

### Fix 4 — Stratum dispatch split (J8 design, CORRECTED)

Stratum is genuinely reachable both ways in the original
design's reading (supportsDirect true, DatabaseImporter
.java:49; real getAppPath, StratumImporter.java:65–66), so
unlike AndOtp/Aegis it got its own @APP chain, not just
@FILE. Threaded: $26@STRATUM (Stratum row tap in the direct
dialog) → $27@STRATUM (OK reads Stratum) → lambda$7@STRATUM
→ SIE@STRATUM → <init>@STRATUM → onCreate@STRATUM →
startImport@STRATUM → startImportApp@STRATUM → async →
lambda$5@STRATUM → processImporterState@STRATUM → Stratum
decrypt; plus @FILE variant → Stratum decrypt; shared auto
CHA edge sup'd; base lambda$5 → processImporterState
re-written by hand (its auto edge is suppressed by the
@STRATUM variant hand edge's base pair). Warning lambdas NOT
threaded for @STRATUM (direct path only; supported-version
case suffices for REACHABLE).
FIRST ATTEMPT FAILED REDUMP (caught by the per-fix redump,
not by the checks): the first build passed everything (2995,
2537/458, edges 5956, 0/0, flips 0) but the redump still
showed the GA pick (steps 23–27 @APP) followed by
lambda$5@STRATUM dispatch — because lambda$5@STRATUM had been
fed from the SHARED onPostExecute node, which the base
startImportApp chain also reaches. Fix: the root-shell async
chain is variant-split too (doInBackground@STRATUM,
onPostExecute@STRATUM, same pattern as ImportFileTask
@SVG_PICK/@SETTINGS_IMPORT); the shared-node feed was
removed. Lesson recorded: variant dispatch must be split
end-to-end through shared async machinery, or the shared
nodes re-merge the prefixes.
Build after fix 4 (corrected): 2995, 2537/458, edges 5958
(+2 vs first attempt), errors 0, warnings 0, flips 0 (vs
pre-fix4). Eight checks: check 2: 22/0; check 3: 0; check 4:
3955 checked, 321 skipped, 160 implicit, 0 not-show; checks
5–7: schema-2 skip, 0 problems; check 8: 0 / 0 of 458; STRICT
True. Redump decrypt(SecretKey): Stratum row tap → OK →
@STRATUM page chain → @STRATUM async → @STRATUM dispatch →
Stratum decrypt → @STRATUM dialog chain → decrypt(SecretKey);
0 GA mentions.
CUMULATIVE after all four fixes: methods 2995, 2537/458,
edges 5782 → 5958 (+176), errors 0, warnings 0, label flips
0 across all four fixes.
**REFUTATION (from final judging — see §5): the fix-4 edge
`processImporterState@STRATUM → Stratum decrypt` is FALSE
(readFromApp always yields SqlState, never EncryptedState)
and must be removed before push. The @STRATUM chain up to
processImporterState is genuine and stays.**

## 2. ExitActivity.onCreate decision (Aegis-C3-Exit, Muse's own)

Decision: (a) WRONG by design, route-14 class, with proof —
NOT fixable, NOT plain WRONG, never CORRECT or UNCLEAR.
Evidence printed personally by the merger: dumped route
(`merger/scratch/route_ExitActivity_before.txt`, 10 steps)
step 7 E9dbeda39 PanicResponderActivity.onCreate →
finishApp, guard "pref_panic_trigger is on and the sender is
trusted and the action is the TRIGGER";
PanicResponderActivity.java:29 (!BuildConfig.TEST.get() →
trusted path :31–34, else getIntent() :35–36), :38–42
(TRIGGER → finishApp, else finish), :49–52 (finishApp calls
exitAppAndRemoveFromRecents); AndroidManifest.xml:91–101
(PanicResponderActivity exported, launchMode singleInstance,
TRIGGER intent-filter) and the bare ExitActivity declaration
(no intent-filter, so only explicit intents reach it);
app/build.gradle:37 (TEST = AtomicBoolean(false) in
defaultConfig, so the TEST re-scope is invalid under the
declared standard configuration); whole-app grep:
exitAppAndRemoveFromRecents is called only from
PanicResponderActivity.finishApp (:50). The "sender is
trusted" clause is unsatisfiable in standard config: entry
is a plain TRIGGER intent (not startActivityForResult) into
a singleInstance activity, so no calling package exists for
TrustedIntents.getIntentFromTrustedSender, which returns
null and onCreate falls to finish() (:46) — steps 8–10
correct in isolation, never reached. Caveat recorded
honestly: TrustedIntents.java and FW Activity.java are ABSENT
from the merger tree's fw_src (partial extraction), so the
library lines (TrustedIntents.java:104–110,120–124,131–142;
FW-SRC Activity.java:5384–5399) rest on graph_def.py's guard
text plus the route-14 audit's printed verification — both
in-tree legs (singleInstance manifest, TEST=false) were
re-printed by the merger. No graph fix exists within
standard config: dropping the trust guard would invent a
variant contradicting code, and the TEST re-scope
contradicts the declared configuration. Labels UNCHANGED
(route-14 precedent: ApkSignaturePin.getSignatures stays
REACHABLE while its route stands WRONG by design). OPEN ITEM
for coordinator/user review: on this evidence the whole
ExitActivity chain (finishApp, exitAppAndRemoveFromRecents,
ExitActivity.<init>, ExitActivity.onCreate) is
production-unreachable; if the coordinator/user rule so,
those 4 methods flip to UNREACHABLE and the sample
composition changes — that is a label decision, NOT made
silently here. Final-table effect: none on the rate (WRONG
counts as wrong under all three options). ExitActivity was
NOT redrawn, so it does not appear in the final table; its
by-design WRONG stands from the pre-fix dump.

## 3. Step-8 convention record (Aegis-C3-Step8, binding)

Coordinator decision, recorded as Muse's own for user/Yang
review in fix_log.md + AGENT_NOTES.md: the STRICT D-C3-10
reading STANDS for the final table. The 12 solely-step-8
UNCLEAR routes stay UNCLEAR, NOT CORRECT. The
relaunch-compatible reading (CORRECT 17, rate 6/23 = 0.2609)
is NOT adopted: the declared configuration is fresh install,
step 8's own guard demands a producer of the loaded vault
earlier on the route, steps 1–7 contain none, and adopting
the relaunch reading would hide the one step with no in-run
producer. This reaffirms the concordant rulings of all three
fix audits (fix-010203, fix-2014-sample, fix-040616). UNCLEAR
routes are excluded from the error-rate denominator under
either reading, so this choice hides no WRONG route — but
the final CORRECT count (4) must not be inflated by
convention. In the redrawn sample the convention is the
decisive reason for 13 of the 15 UNCLEAR routes (the other
two: injectVaultLockReceiver2 and IconPack$Icon rest on
absent generated code, with step-16 cross-run pack for the
latter).

## 4. Redrawn sample + tally + final error rate

Redraw: `python3 -I tools/verify_sample.py Aegis 30 20261025`
(same seed) on the post-fix graph → 25 routes (PLAIN pool 2
vs quota 7, as expected), 694 steps, 353 distinct edges,
saved to `merger/scratch/sample_30_final.txt` (first-draw
`sample_30.txt` untouched). Composition changed vs first
draw (strata follow routes): IN selectIcon, Stratum Legacy
decrypt, RawSlot.getType; OUT startImportFile, getKey (its
new 17-step auth route left its old stratum), ExitActivity
.onCreate. The other 3 fixed targets ARE redrawn (AndOtp 49
steps via @FILE, Stratum 45 via @STRATUM, CustomSvgIcon 26
via the empty-packs branch).
Judged fresh by 9 helpers (h1–h9, max 3 routes each, two
staggered waves) with a merger completeness check per report
(step counts match the sample; per-helper arithmetic
verified; every report holds a per-step table with
personally printed file:lines; prior verdicts withheld).
Final table: `judging-final/route_table.md` (it lives there
until push time; the first-draw table in
`judging-sample30/route_table.md` must NOT be pushed as
final).
Tally: CORRECT 4, WRONG 6, UNCLEAR 15 (25 routes). Steps:
537 correct / 31 wrong / 126 unclear (694 total).
fixed (first-draw WRONG → redrawn CORRECT, strict) = 0.
Final error rate = (0 + 6) / (4 + 0 + 6) = 6/10 = 0.6000.
First-draw rate was 6/11 = 0.5455. The rate ROSE although
two fixable WRONGs left the WRONG set, because the redrawn
sample contains 4 NEW WRONGs outside the 4-fix scope
(FreeOtp GA-splice, selectIcon onIconSelected residual,
Legacy GA-splice + @APP-impossibility, RawSlot disable-path
by-design) and lost 1 CORRECT to stricter generated-code
grading (injectVaultLockReceiver2). See the migration table
in route_table.md for the full accounting. "Fixed" is
defined strictly (WRONG→CORRECT); the two WRONG→UNCLEAR
migrations (CustomSvgIcon, AndOtp) leave both numerator and
denominator, so the rate is 0.6000 under the strict
definition and under wrong/(correct+wrong) alike.

## 5. What final judging proved (merger-verified)

- Stratum fix-4 edge REFUTED (h2, h8, merger-verified):
  `DatabaseImporter.readFromApp` passes isInternal=true
  (DatabaseImporter.java:79–87); StratumImporter.read
  (stream, true) takes readInternal (:70–72), returning
  SqlState with super(false) (:324–328); no Stratum
  readFromApp override exists. So on ANY app-import prefix
  the state is SqlState and EncryptedState.decrypt never
  fires. The fix-4 @STRATUM→decrypt edge is false; the
  @STRATUM chain up to processImporterState is genuine and
  stays; the genuine Stratum decrypt path is @FILE only.
  CORRECTION REQUIRED BEFORE PUSH (see §6). General
  caution: app-import decrypt dispatch needs per-importer
  verification of readInternal's state.
- FreeOtp WRONG (h1, merger-verified): GA-prefix route into
  FreeOTP decrypt; GA State super(false) → decrypt never
  called. Same defect class, not one of the 4 fixes.
- selectIcon WRONG (h3, merger-verified): the dumped route
  correctly follows @ASSIGN variants through step 40, but
  step 41 uses the shared onIconSelected dispatch to
  EditEntry$1 instead of AssignIcons$1 — the fix-1 residual
  recorded in §1. Follow-up: split onIconSelected direct +
  forwarder, fix-1 pattern.
- AndOtp UNCLEAR (h1): steps 8–9 (convention) + step-37 pick
  gap (the @FILE pick does not name andOTP). The splice is
  gone; what remains is pick-step precision. Follow-up:
  per-importer @FILE pick variants.
- getSignatures WRONG by design (h6, independent): step 8
  trust guard unsatisfiable; TEST=false re-verified; same
  legs as route 14. No fix.
- No other helper WRONG was overturned by the merger; all
  other verdicts stand as delivered (route verdicts
  unaffected by the helper-counting differences in Hilt
  steps 2–3 strictness, post-failure downstream counting,
  and step-8 propagation depth — all noted in
  route_table.md).

## 6. Exact C3 push manifest (audit-gated; DO NOT PUSH yet)

Push ONLY to branch work-2026-10-31 in
bugfixops/ground-truth-results, under the push-lock protocol,
after fix audits PASS. Files (all under graphs/Aegis/ only;
every file under 900 KB):

1. graphs/Aegis/graph_def.py (570,509 B at delivery —
   post-fix-4 state; see correction warning below)
2. graphs/Aegis/scratch/route_table.md (copy of
   judging-final/route_table.md AT PUSH TIME — until then
   the final table lives ONLY in judging-final/)
3. graphs/Aegis/scratch/fix_log.md (appended through this
   step, in-tree)
4. graphs/Aegis/AGENT_NOTES.md (appended through this step,
   in-tree)
5. graphs/Aegis/scratch/FIX_REPORT.md (copy of
   merger/FIX_REPORT.md AT PUSH TIME, for the audits)

CORRECTION WARNING — READ BEFORE PUSH: the push must NOT
include the fix-4 edge `processImporterState@STRATUM →
StratumImporter$EncryptedState.decrypt` as-is (refuted, §5).
The correction (remove that edge; keep the @STRATUM chain
for the decrypted branch) needs its own rebuild + redump
(Stratum decrypt route must fall back to @FILE) + audit
before push. If the correction is applied, graph_def.py
changes from the delivered bytes and the Stratum row of the
final table must be re-judged on the corrected route — the
coordinator/audits decide whether that re-judgement is a
table amendment or a new sample cycle; it is NOT done
silently in this step. Do NOT push the first-draw table
(judging-sample30/route_table.md) as final. Do NOT push
out/, ci_latest/, tools/, or any other app's folders. Never
write a tick marker; K-status lines are the coordinator's only.

## C3 push assembly note (push-assembly step, 2026-11-01)
- Stratum correction applied (see scratch/fix_log.md "Stratum correction" entry): graph_def.py now 570,664 B (was 570,509 B at section-6 delivery), edges 5957, 2995 methods, 2537/458, errors 0, warnings 0, 0 label flips.
- Independent correction audit PASS (work/Aegis/audit/c3-stratum-correction/AUDIT.md); audit section-6 notes applied verbatim to the pushed route_table.md copy (row-3 correction note + FLAG-resolved note; row-3 verdict column untouched, still WRONG; rate unchanged 6/10 = 0.6000).
- Section-7 suspect edges (Legacy Ee4fdd4f0, Totp Eda333e39) NOT changed — follow-ups with their own design + audit.
- Staged for the C3 push as: graphs/Aegis/graph_def.py, graphs/Aegis/scratch/route_table.md, graphs/Aegis/scratch/fix_log.md, graphs/Aegis/AGENT_NOTES.md, graphs/Aegis/scratch/FIX_REPORT.md (this file, with this note). Commit SHA recorded in MERGER_REPORT.md + the staging sync record after the push lands.
