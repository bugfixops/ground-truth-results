# LABEL Helper Instructions

You are a read-only helper for the AmazeFileManager graph conversion. Your job is to label methods from your assigned classes.

## Your Task

1. Read the class list from your assignment file (helper_N_methods.json)
2. For each method in each class:
   - Read the source code from `final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/`
   - Determine if it's REACHABLE (has a trigger from an entry point) or UNREACHABLE
   - If UNREACHABLE: determine the kind and reason with printed source lines
3. Write your output to TWO files:
   - `parts/label_N.py`: Python code with e(...) edges and UNREACHABLE[...] entries only (same style as graph_def.py, NO new constants)
   - `parts/label_N.md`: Markdown table with columns: method | label | kind | reason | printed file:lines

## Rules (from KIRO_CONVERT_APPS.md sections 3, 5, 11)

### Section 3: Labels
- Every method gets exactly one label: REACHABLE or UNREACHABLE
- UNREACHABLE needs: kind (no_trigger_in_app, branch_never_taken, framework_never_calls, closed_by_configuration, closed_by_api_level), reason, and source reference
- confirmed_by is SOURCE or INFERRED. Never DYN, FW-MEMORY, or UNVERIFIED
- Tool coverage is never evidence - do not use it to decide labels
- Library/generated classes (Glide*, Dagger, Hilt, Room *_Impl, protobuf): label INFERRED
- For library classes, UNREACHABLE requires grep -rn output showing no call sites
- If the app calls a library class, its methods are REACHABLE through those calls

### Section 5: Framework and Library Claims
- Cite framework from fw_src/android-8.1.0_r1/ with FW-SRC path:lines
- If framework file not in fw_src/, claim is INFERRED with "source not read"
- Libraries not in dataset (androidx, material, Glide, etc.) are INFERRED
- Do not write framework claims from memory

### Section 11: Helper Rules
- You are READ-ONLY: never edit graph_def.py, out/, verification.csv, make_verification.py, readme_notes.md, PROGRESS_V2.md, AGENT_NOTES.md, tools/, or another helper's files
- You NEVER run tools/build_graph.py and NEVER apply a fix
- Every claim you write MUST carry printed source lines
- A claim without printed source lines will be rejected

## Output Format

### parts/label_N.py
```python
# ---- Helper N label part (YYYY-MM-DD)

# ClassName methods
e('SourceMethod', 'TargetMethod', 'KIND', 'description',
  evidence='SRC SourceFile.java:123-456')

# More edges...

# UNREACHABLE methods from this batch
UNREACHABLE_PART_N = {
    'ClassName.methodName': ('kind', 'reason with source evidence', 'SRC SourceFile.java:lines', 'SOURCE or INFERRED'),
}
```

### parts/label_N.md
```markdown
| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| ClassName.method1 | REACHABLE | | Called from entry via path | SRC SourceFile.java:123 |
| ClassName.method2 | UNREACHABLE | no_trigger_in_app | No reachable caller | SRC SourceFile.java:456 shows only dead code calls it |
```

## Status Updates

Write to the TOP of your parts/label_N.md:
- First line: `STATUS: RUNNING <timestamp>`
- Last line when done: `STATUS: DONE` or `STATUS: INCOMPLETE <reason>`

## Important

- Print source lines with sed -n for every claim
- For Glide/library methods: grep -rn to show all call sites
- If you cannot determine a label from source, mark it STATUS: INCOMPLETE with the specific method and why
- Work from /Users/darshan/Desktop/yang/work
- App source root: final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/
- Never guess - if source doesn't show it clearly, report it as incomplete
