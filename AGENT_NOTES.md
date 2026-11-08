> **Old file (2026-10-31 upload).** These are early AmazeFileManager conversion notes left at the top level. The current notes are `graphs/AmazeFileManager/AGENT_NOTES.md`; the final results are in `run_result/`.

# Agent Notes - AmazeFileManager

## C7 Build Log

| Build | REACHABLE | UNREACHABLE | UNRESOLVED | TOTAL | Errors | Warnings | Notes |
|-------|-----------|-------------|------------|-------|--------|----------|-------|
| repair_baseline | 1826 | 297 | 858 | 2981 | 2272 | 96 | Baseline before Phase 2b |
| build_repair_02 | 1828 | 297 | 856 | 2981 | 1922 | 101 | Applied 161 full pkg→canonical renames (Proposal 1) |
| build_repair_03 | 1827 | 299 | 855 | 2981 | 1903 | 101 | Fixed 11 JVM signature UNREACHABLE entries |
| build_repair_04 | 1827 | 299 | 855 | 2981 | 1816 | 101 | Applied Proposal 3 (FRAMEWORK→S_ENTRY, DialogPreference→S_PREFS) + Proposal 4 resolved overloads |
| build_repair_06 | 1827 | 272 | 882 | 2981 | 1816 | 101 | Deleted 27 Glide UNREACHABLE entries that have incoming bytecode edges |
| build_repair_09 | 1827 | 272 | 882 | 2981 | 1694 | 101 | Fixed 139 'bad confirmed_by CALL' → INFERRED/SOURCE |

## Current Status (build_repair_09)
- Errors breakdown: 692 "unknown node" (to be contracted), 77 GUI, 5 bad-kind, 4 missing-evidence, 6 UNREACHABLE unknown-method, 11 page unreachable, 882 method-has-no-path (expected)
- **Next step**: See `graphs/AmazeFileManager/scratch/repair_handoff.md` for complete handoff to next repair iteration
- Classified: 225 FRAMEWORK-HOP nodes (to contract), 51 APP-AMBIGUOUS nodes (to resolve)

