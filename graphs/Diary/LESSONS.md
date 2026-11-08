# Diary — lessons

- A "file not held" result from check_citations.py is a missing-cache result, not a citation error: the overnight run's 81 Diary problems were all missing files, with 0 line-range problems; with the full fw_src tree present, the local run shows 81 distinct citations and 0 problems.
- A scan over an empty source tree proves nothing: scan_unreachable.py printed "no other mention" for all 21 UNREACHABLE methods only because no source files were present to search.
- When a redrawn route sample reproduces the stored verification rows edge-for-edge (30/30 here), the stored judgments transfer to the current build — but the transfer itself must be checked and printed, not assumed.
- Unclear path rows are not errors: Diary's 5 unclear routes are unclear only because their final step rests on picker-app, libcore, or java.io behaviour that was not read; their app-internal steps check out against printed source.
- A missing generator tool must be reported, not worked around: no make_verification.py existed on the branch, so verification.csv was kept exactly as fetched until a portable writer was written and proven byte-identical.
- Small discrepancies deserve recording, not silent fixing: DATASET.txt says target_sdk 28 while the graph baseline is API 27 (android-8.1.0_r1).
- A name-only unreachable scan overstates callers: overloads and same-name methods in other classes must be triaged by signature and declaring class before any label is questioned.
