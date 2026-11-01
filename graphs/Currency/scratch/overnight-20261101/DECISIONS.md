# Currency — decisions by Muse (own decisions, for user/Yang review; never in Yang's name)

No open question from the user or from Yang arose during this re-check. The
following are Muse's own decisions on issues that came up while working, each
with reasoning. Nothing here changes a label, a route, or a branch file.

## D1 — verification.csv is NOT hand-edited for the two newly judged path rows

Reasoning: the task rule is that verification.csv is produced ONLY via
tools/make_verification.py, and that tool does not exist anywhere in tools/
on branch work-2026-10-31 (verified by directory listing). Hand-appending
rows would break the audit provenance the file exists to provide. The two
new judgements (Parser$Handler.<init> correct, Main.onDateResult correct)
are therefore recorded in scratch/route_judgements.md only, and the local
verification.csv is an unchanged copy of the branch file (98 rows, header
type,item,result,confirmed_by,ref,edges,note). Morning action for the user:
either supply/confirm the intended verification.csv producer, or accept
carrying these two rows forward in the judgements file.

## D2 — check_citations' 2 remaining problems are a reconstruction blocker, not graph errors

Reasoning: after reconstructing the cited AOSP files locally, 39 of 41
distinct citations resolve with all cited line ranges in range and 0
unbacked-evidence claims (no FW-MEMORY/DYN/UNVERIFIED). The 2 remaining
problems are both the same file, am/ActivityManagerService.java, which the
connector refuses to display at 1,086,106 B ("too large to display"). The
citations themselves (ActivityManagerService.java:19199-19224 and the
ActiveServices-adjacent edge) are unchanged from the branch graph, and the
raw download URL the connector offered contains a token, which the standing
connector-only rule forbids using. So the check is reported as partial, not
failed on the graph, and no token URL was fetched.

## D3 — the 27-method sample is accepted as the complete sample

Reasoning: verify_sample.py's quotas sum to 30 but its pools exhaust at 27
for Currency (deterministic, seed 20261025; redraw identical). Reporting
"30 routes checked" would be false. Error rate is computed over judged
routes only, excluding unclear, following the build's own formula:
(0 fixed + 0 wrong) / (23 correct + 0 + 0) = 0.0.

## D4 — the 4 unclear routes stay unclear

Reasoning: Main.onEditorAction (IME step INFERRED), CurrencyWidgetUpdate
.onDestroy, CurrencyWidgetUpdate.onDateResult and CurrencyWidgetProvider
.onDeleted (launcher steps INFERRED) all have fully printed app-side chains,
but their blocking steps are in code that was not read (launcher, IME).
Upgrading them to correct would overstate what was checked. This matches
the branch verification.csv, where the same 4 rows are already unclear.

## D5 — scan_unreachable --callers hit on Singleton.getList does not change its label

Reasoning: the hit is ChartActivity.onCreate -> Singleton.getList at
ChartActivity.java:176, which is the else-branch of "instance == null"
(:163). Re-reading ChartActivity.java:163-177 confirms instance is an
instance field, null whenever onCreate starts, so the else-branch never
runs — exactly what the branch_never_taken reason text already says. The
same-name overload hits (ChartParser.startParser, getItem) are likewise
explained in the reasons, not new callers.

## D6 — readme_notes history kept, re-check appended rather than rewritten

Reasoning: the branch notes' 28-method / 391-edge figures describe the
first audit against the schema 1 graph; rewriting them would erase the
audit trail. The 2026-11-01 re-check (27 methods, 107 edges, 23/0/0/4) is
added as a dated paragraph in the same section, and the generated README
shows the current build numbers (145 methods, 393 edges) from the build
itself. The five headings stay in their original order.
