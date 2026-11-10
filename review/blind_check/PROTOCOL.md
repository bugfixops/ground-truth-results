# Blind check of the class labels: protocol (for the worker, not for the readers)

Purpose: measure how often our class labels are wrong, with readers who never see the labels, and fix the causes. A reader is a
model agent that gets only `INSTRUCTIONS.md` and a chunk file (id, app, jvm_class, method, desc) and classifies each method
from the source. The worker (you) may start as many readers as needed and should use the strongest model available.

## Draw (per pass; record the seed in the report)
- Population: never-run methods = rows of graphs/<App>/out/sanity_check.csv with monkey_hit 0 and ape_hit 0. Class of a method
  from graphs/<App>/out/methods.csv by the class rule of review/TASK_NOTE.md (dead/config if UNREACHABLE; env_kinds other than
  permission; state_kinds; explicit_standard_route = no is library; else gui). Same function as tools_dev/reaudit_shares.py.
- GUI draw: 8 random methods per app (40) that are labelled gui, not drawn in an earlier pass.
- Changed draw: 5 random methods per app (25; LibreTorrent has only about 10, take what exists) among never-run methods
  whose class differs between the previous head and the current build (pass 1: against f5eb13ac, the round-2 CI head).
- Shuffle the rows of each app, give them ids `<App>-F01...`, write a chunk file per app (about 13 rows) WITHOUT any label, and
  keep a key file (id, method, category gui_draw or changed, old class, new class) outside the readers' reach.

## Readers
- One reader per app chunk gives the first classification. Readers get nothing else: no labels, no old results, no paths to
  graphs/, out/, scratch/, review/, device/, handoff/, run_result/, tools/, tools_dev/, any clone, ~/Documents, ~/Downloads.
- Miss = the reader's class_found differs from our class, EXCEPT: class_found = state with dialog_dependent = yes and our class
  = gui counts as agree (Jin's own checked cases Aegis-38 and Aegis-39 rule a dialog that one GUI sequence opens and closes as
  GUI; the written rule says state, so the readers apply it literally; the practice wins).
- Every miss is read by a SECOND blind reader (same instructions, only the missed rows). It counts as a confirmed miss only if
  the second reader's class_found equals the first reader's (still excluding the dialog exception). If the two readers differ,
  read the source yourself and decide; list those rows in the report.
- Precision = 1 - confirmed misses / rows, separately for the GUI draw and the changed draw.

## Loop
1. First fix the two named defects of the message (CloudIcon env; VaultEntryIcon env) and the general rule they show: a state
   gate that in-app actions can create only after an env action is env. Apply the rule as a screen over all STATE rows judged in
   graphs/<App>/scratch/reaudit/r2_judged.csv and r3_judged.csv (and the hand-written state gates of the five apps), judge the
   hits from the source, fix them.
2. Rebuild (handoff/ci/rebuild.sh for the five apps). PASS 1: draw, read, confirm.
3. Group the confirmed misses by cause (a missing guard kind, a wrong edge class, a wrong gate kind). Fix the CAUSES with
   general rules or screens, not method by method; judge the flagged steps from the source; apply as in rounds 2 and 3
   (r4_judged.csv and a round4 rules block, or extend the round 3 files). Do not tune on the rows of review/sample_tune beyond what
   a general cause needs: measure.py must stay at 84.6% (115 of 136) or higher.
4. Rebuild. PASS 2: a NEW seed, a fresh draw (nothing from pass 1), read, confirm. This is the final estimate.
5. Stop after pass 2, or after pass 1 when both precisions are 90% or higher (then no cause fix is needed beyond step 1).
   Do not start a pass 3.

## Where to keep results (not in review/)
graphs/<App>/scratch/reaudit/blind_r3b/pass<k>/: the chunk file, each reader's output CSV, the key file (with our labels) and the
second readers' output; plus graphs/<App>/scratch/reaudit/blind_r3b/SUMMARY.txt with per pass: seed, rows, misses, confirmed
misses by cause, precision for both draws.

## Constraints (as in round 3)
- Route changes: each changed sampled route re-verified from the source, path row rewritten, ROUTES.csv marked, listed in
  round3b_route_changes.txt. Limit 10 changed sampled routes. STOP and report only if the limit is exceeded, the final CI fails,
  an error survives two fix attempts, or check_cases drops below 23 of 23.
- Errors 0 and warnings 0 in all 13 apps (CI), check_unchanged_apps ALL UNCHANGED, none_check --covered 0, check_terms clean.
- Never open the full sample or any held-out row; never push to main or PUBLISH_REQUEST.txt; never edit review/ or
  tools/results_templates/root_readme.md (the reviewer does); no real device run.
- Keep R2_DIALOG_RULE = False.
- ONE push, then handoff/REBUILD_REQUEST.txt for all 13 apps, wait for the CI.

## Report once
Head; errors/warnings per app; check_cases; route_diff and changed sampled routes; measure.py before and after; per named
defect the new class; per pass: seed, rows, misses, confirmed misses by cause, precision (GUI draw, changed draw); which rules
changed; other methods changed per app and class pair; judged and unjudged steps; the routes changed.
