# Ground-truth (schema 2) progress. Read by tools/resume_after_reset.sh: a line that starts with "- [ ]" means work remains.
# "- [x]" = converted and checked (strict build 0/0, verification.csv, readme_notes.md, out/README.md, all checkers pass).
# Order = the order to work in (smallest first). Recipe: handoff/CONVERSION_RECIPE.md. Rules of Yang: memory file ground-truth-requirements.md.
- [x] Currency
- [x] Diary
- [x] hash-checker
- [x] Omni-Notes
- [x] openlauncher
- [x] Vanilla-Music
# 2026-10-26 23:15 EDT: AnyMemo moved to the end and paused (not finished). Resume it from graphs/AnyMemo/AGENT_NOTES.md, section PAUSE POINT.
- [x] Markor
- [ ] Aegis
# 2026-10-27: the four apps below are assigned to Kiro (handoff/KIRO_CONVERT_APPS.md). "- [K]" = not ticked: the run must not take them.
# 2026-10-29 23:25: the user moved AmazeFileManager, AnkiDroid and MMEX into the overnight run, labelling only, in this order.
- [L] AmazeFileManager (labelled overnight 2026-10-30: UNRESOLVED 0, errors 0, warnings 0; route checks not started)
# 2026-10-27 21:20: these three are for the overnight convert run (handoff/RESUME_PROMPT_CONVERT.md, tools/resume_convert.sh). "- [C]" = run queue, not ticked.
- [L] AnkiDroid (labelled overnight 2026-10-30: UNRESOLVED 0, errors 0, warnings 0; route checks not started)
- [L] MMEX (labelled overnight 2026-10-31: UNRESOLVED 0, errors 0, warnings 0; route checks not started)
# 2026-10-28: "- [H]" = handed to ChatGPT (brief: handoff/CHATGPT_BRIEF_LIBRETORRENT.md). Not in the Claude queue; not ticked.
- [H] LibreTorrent (handed to ChatGPT 2026-10-28; removed from the overnight queue)
# 2026-10-29: "- [N]" = NEXT step, not started (device replay of sampled routes on API 27 emulators in GitHub Actions, repo bugfixops/test-13). Plan: handoff/NEXT_DEVICE_REPLAY.md. Start only after all apps finish and the user says go.
- [N] Device replay on GitHub Actions (bugfixops/test-13): not started
# 2026-10-27: AnyMemo round 3 finished by Kiro (handoff/KIRO_FIX_ANYMEMO.md); "- [K]" until the user decides to tick it.
- [x] AnyMemo (round 3 by Kiro 2026-10-27; checked by the orchestrator 2026-10-27 18:50: build 0/0, PENDING 0, citations and bytecode checks pass, 30 path rows; see graphs/AnyMemo/AGENT_NOTES.md)
