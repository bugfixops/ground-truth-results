# AmazeFileManager — DECISIONS (Muse's own decisions, for user/Yang review; never in Yang's name)

## D1. Do NOT use the token-bearing download URL (2026-11-01, stream B)
Reasoning: the task's hard constraint forbids waiting for, using, or
recording any token, and the connector redacts the token in its own
output. The URL was therefore not unwrapped, not fetched, and not
recorded anywhere. Consequence: large branch files stay unfetched and
the gate is blocked (see STEP_LOG). This decision follows the task
constraint, not a user instruction about this app.

## D2. Do NOT substitute an older under-1MB graph copy for the current graph_def.py
Reasoning: scratch copies under 1 MB (e.g. graph_def_before_rb12.py,
746,302 bytes) are intermediate states, not the current graph
(1,058,622 bytes, build 28/29/30 state, 2509/472). Building one would
produce different counts and would misrepresent the branch graph.
A faithful reconstruction from parts/ is also impossible because
merge_parts.py only appends UNREACHABLE entries from 4 parts and the
parts lack the base graph (entries, SCREENS, hand edges, SUPPRESS,
ENV_KINDS_OF, CLASSIFY/EDIT hooks). Consequence: no local build is
claimed tonight.

## D3. Do NOT flip any of the 21 contradictions on tool coverage alone
Reasoning: KIRO section 3 and the task both forbid it; coverage is a
pointer only. Tonight's flips are proposals from printed source only
(section A of route_checks_consolidated.md), and the 13 Glide methods
with no printed call site stay OPEN rather than being confirmed
UNREACHABLE.

## D4. GlideRequests.as is INFERRED, and held if SOURCE-only is required
Reasoning: the two asDrawable() anchor sites are printed SOURCE, but
the asDrawable() -> as(Class) step is generated-code delegation and
generated GlideRequests.java is not in final_java_only and was not
printed. Presenting the whole route as SOURCE would overstate the
evidence. The merger must either record the INFERRED step or print
the generated file first.

## D5. No sample error rate is reported tonight
Reasoning: the sampler could not run (methods.csv blocked), so the
only judged items are an issue-first selection. Reporting 6/6 = 1.00
as "the error rate" would mislead; the consolidated report states
the 6/6 figure only as the issue-first set's fraction and forbids
quoting it as the app's error rate.

## D6. Citation corrections adopted tonight (supersede prior files)
Reasoning: grep-verified against locally printed source tonight.
(a) AppsAdapterPreloadModel clone line is :45, not :44 — all fix
fragments citing :44 must be corrected before merge.
(b) Sftp lambda$null$5 matches the removeConnection Runnable by
elimination (only 7-capture, non-static, no-trailing-interface-param
lambda$null$ candidate), NOT by exact descriptor order — the
descriptor order (String, int, String, ...) differs from the
source-textual capture order, so the prior "exact order" claim is
withdrawn. Neither correction changes any verdict.

## D7. verification.csv is NOT hand-written tonight
Reasoning: the rules require verification.csv to be produced by
make_verification.py with assertions against the graph, and no
make_verification.py exists for AmazeFileManager on the branch.
Hand-writing it would violate the rule and could not be asserted
without a build. It stays unwritten until a checkout exists and the
generator is authored.

## D8. Draft logs are kept as drafts, not as branch logs
Reasoning: readme_notes_DRAFT.md and LESSONS_DRAFT.md in this local
mirror are hand drafts. They must not be copied to the branch as
readme_notes.md / LESSONS.md until the build passes and
gen_readme_v2.py has run on a full checkout. The filenames carry
_DRAFT to prevent accidental promotion.
