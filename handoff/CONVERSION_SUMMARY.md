# Conversion summary: labelling run, 2026-10-30

Scope: labelling only. An app counts as labelled when its build shows UNRESOLVED 0, errors 0, warnings 0. Route checks, route tables and deliverables were not part of this run. Nothing was committed, pushed, installed or downloaded, and no adb, emulator, gradle or network access was used.

## Results

| App | Progress line | Build | UNRESOLVED | Errors | Warnings | Where the blocker is recorded |
|---|---|---|---|---|---|---|
| AmazeFileManager | [B] | 21 | 17 | 69 | 105 | handoff/HANDOFF_V2.md "## Blocked" and "## Convert run decisions" |
| AnkiDroid | [B] | 184 | 672 | 694 | 0 | graphs/AnkiDroid/AGENT_NOTES.md "## Blocked" |
| MMEX | [B] | r1 | 1939 | 1950 | 8 | graphs/MMEX/AGENT_NOTES.md "## Blocked" |

No app was labelled in this run. All three are blocked, and the run moved on past each one.

## AmazeFileManager

- Builds 17 to 21 applied the decision files in graphs/AmazeFileManager/scratch/fix14/decisions/. Build 20 deleted two spurious Statvfs edges. Build 21 applied N1 and N2 (minus nine GUI rows that broke the page-source rule, which were reverted). Errors went from 132 (build 20) to 69 (build 21). No error category rose.
- The three faults the user listed are resolved. The two ENV texts are registered, RoundedImageView.onDraw has a route, and the PasteHelper$1 and UserColorPreferences$1 citations were checked by a grep that was actually run.
- Open items that block the gate:
  - 104 "UNREACHABLE but has incoming edges" warnings and 1 REVIEW warning. Conservative choice: keep the entries and edges.
  - 52 unknown-node errors (38 unknown source, 14 unknown destination), including the nine GUI rows reverted in build 21.
  - 8 no-path methods outside AboutActivity (listed in the decisions section).
  - commons_compress_7z sources outside the method universe, not added.
  - Glide C5: the 24-method list is missing from scratch/conflicts.md, so Glide is undecided.
- Open item that does not block: the nine AboutActivity methods with no path stay unlabelled, as the run rule says.
- Full decision list with the conservative choices: handoff/HANDOFF_V2.md "## Convert run decisions (AmazeFileManager labelling run, 2026-10-30)".

## AnkiDroid

- Build 184 made no graph change. The 672 UNRESOLVED methods in 212 classes need source-verified graph edges or source-verified UNREACHABLE entries.

## MMEX

- Build r1 made no graph change. Batch 085 is not merged, and the 1939 UNRESOLVED methods need source-verified graph edges.

## Next step

Resume AmazeFileManager from the open items above. AnkiDroid and MMEX resume from their notes files.
