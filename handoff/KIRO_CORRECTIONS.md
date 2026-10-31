# KIRO CORRECTIONS: AmazeFileManager (in force from 2026-10-27 21:10)

Read this whole file before your next step. These corrections override handoff/KIRO_CONVERT_APPS.md section 11 where they set a limit. Then continue from the "Current step" in graphs/AmazeFileManager/AGENT_NOTES.md. Do not restart finished work.

## What the check found (counted from the files at 21:10)

| part | report rows | rows with a source line | rows without | status the helper claimed | edges in the .py | action |
|---|---|---|---|---|---|---|
| label_1 | 297 | 110 | 187 | DONE | 0 | reject: redo the 187 rows |
| label_2 | 305 | 60 | 245 | DONE | 24 | reject: cite or redo the 245 rows |
| label_3 | 562 | 84 | 478 | DONE | 106 | reject: cite or redo the 478 rows |
| label_4 | 30 | 28 | 2 | INCOMPLETE (batch of 989 methods) | 7 | the batch was too large: split it (C3) |
| label_c1 | 54 | 45 | 9 | INCOMPLETE (batch of 67 methods) | 10 | cite or redo the 9 rows, then check it (C1) |
| label_c2 | 0 | 0 | 0 | RUNNING | 42 | not accepted: edges with no report rows |
| label_c3 | 0 | 0 | 0 | RUNNING | 0 | nothing yet |
| label_c4 | 0 | 0 | 0 | RUNNING | 37 | not accepted: edges with no report rows |

"DONE" from label_1, label_2 and label_3 is not accepted while rows lack a source line. None of these parts has been merged into graph_def.py yet. Keep it that way until C1 is met.

Several STATUS lines carry dates that are wrong (for example 2025-01-10 and 2025-01-17). Take the time from the output of date (C4).

## C1. A part is merged only when all of these hold
a. Every e(...) edge and every UNREACHABLE entry in the .py has a matching row in the .md, and every row has a matching entry.
b. Every row's Source Lines column names a file and a line range, and you have printed those lines with sed -n and read them.
c. The .md ends with "STATUS: DONE <HH:MM>", written after (a) and (b) are true.
d. After the merge: python3 -m py_compile graphs/AmazeFileManager/graph_def.py passes, the build's errors do not rise, and the merge is recorded in AGENT_NOTES.md.
A part that fails any of these is not merged. Its status is INCOMPLETE.

## C2. Rows without a source line
Each such row is verified again: print the lines, read them, and rewrite the row with the citation. If the source does not support the label, change the label to UNRESOLVED and put the method back in the queue. Do not keep a row because its label looks right.

## C3. Batch size
- No helper gets more than 40 methods. The batches of 989 (label_4) and 67 (label_c1) are rejected.
- Split the chunks in scratch/reassign_chunks/ into batches of at most 40 methods. Record the split in AGENT_NOTES.md as a table: batch | classes | methods | helper | status.
- A helper writes each row as soon as its method is done, not in one block at the end.

## C4. STATUS lines
- First line: "STATUS: RUNNING <HH:MM>". Last line: "STATUS: DONE <HH:MM>", or "STATUS: INCOMPLETE <HH:MM> <reason>".
- Take HH:MM from the output of date. Do not write a date from memory.
- A helper with no new row for 30 minutes is stuck: mark its batch INCOMPLETE and give it to one new helper (section 12 of the rules file).

## C5. Glide
The 24 methods listed under "## Decision: REACHABLE" in scratch/conflicts.md are REACHABLE. Each needs a route in graph_def.py: an e(...) chain from an entry point to the method, where each edge cites the printed source line of the call (the GlideApp call sites are already listed in conflicts.md). The build's "method has no path" errors for these 24 must reach zero before other Glide work continues.

## C6. Route checks
Route checks (section 4 of the rules file) start only after the build reports UNRESOLVED 0 and warnings 0. Until then, do not draw the sample.

## C7. Progress record
After each build, add one line to AGENT_NOTES.md: time, REACHABLE, UNREACHABLE, UNRESOLVED, errors, warnings, and the list of merged parts. This line is the only progress record.

## C8. Parallel work
Keep up to 4 helpers at a time (section 11 of the rules file), each on one batch from C3. Parallel work does not replace C1 to C4.
