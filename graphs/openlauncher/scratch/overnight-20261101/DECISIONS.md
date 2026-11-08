# openlauncher — decisions made by Muse (Stream D leaf, 2026-11-01), for user/Yang review

None of these decides anything about another app or about Yang's open items. Each is recorded here as Muse's
own decision, not in Yang's name.

## D1 — check_citations: 2 residual "file not held" problems are a cache blocker, not a graph failure
Decision: report check (2) as NOT fully passing locally, rather than passed or failed on the merits.
Reasoning: the only 2 of 64 distinct citations that do not resolve locally point at
fw_src/android-8.1.0_r1/services/core/java/com/android/server/am/ActivityManagerService.java (1,086,106 B) and
.../pm/PackageManagerService.java (1,190,171 B), which exceed the GitHub connector's get_file_contents display
limit. The connector's suggested download URLs carry a token, which this project's hard constraints forbid
using. All other 62 citations resolve with 0 line-range problems and FW-MEMORY/DYN/UNVERIFIED = 0, and the
earlier session read both oversize files in full from a checkout with 0 errors. Inventing a pass would hide a
real gap; calling the graph wrong would misdescribe a tooling limit as a citation error.

## D2 — the single PENDING grep hit is legitimate source terminology, not an unfinished marker
Decision: treat grep check (7) as explained, not failed.
Reasoning: the only `PENDING` hit in graph_def.py is `taskList.getStatus() == PENDING` (AsyncTask.Status.PENDING)
in a guard at line 942, matching HideAppsFragment.java:66 exactly. It is not a PENDING label, status, or TODO.

## D3 — the sample is 27 routes, not 30, and the error rate is computed over 27
Decision: report "verify_sample.py openlauncher 30 20261025 -> 27 methods" and error rate 1/27 = 0.037.
Reasoning: the tool's strata quotas cap below 30 for this app (fewer members than quota in several strata);
27 is the tool's reproducible output for seed 20261025, identical before and after the rebuild. Dividing by 30
would understate the rate; inventing 3 more routes would break reproducibility.

## D4 — no graph change from this re-verification; the DialogUtils "fixed" row stays "fixed"
Decision: make no edit to graph_def.py and keep verification.csv byte-identical to the branch file.
Reasoning: the one fixed route (DialogUtils.copy) was already fixed in the fetched graph_def (no
ENV_STORAGE_FAIL on the copy edge; guards "item is Backup"/"item is Restore"), independently re-confirmed
against DialogUtils.java:146-182. The regenerated verification.csv matches the branch file byte for byte, so
there is nothing new to merge; the "fixed" verdicts in verification.csv record history (errors found and
fixed by the earlier session), not errors in the current graph.
