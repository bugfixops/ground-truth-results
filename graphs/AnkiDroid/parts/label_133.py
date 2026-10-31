# AnkiDroid batch 133 (LABEL helper). Models part: 39 methods, all labelled REACHABLE.
# The full row list (label, kind, reason, source) is in graphs/AnkiDroid/parts/label_133.md.
#
# No e() edges and no UNREACHABLE entries are written here:
# - Every caller of these methods is an automatic CALL edge in graphs/AnkiDroid/auto_calls.json. Each row names
#   the caller and its call line.
# - The page-owned edges (S_*) that reach these methods belong to other batches.
#
# Recorded in the rows, not as edges:
# - Gate STATE_NOTE: the Models$TransformFieldAdd, Delete and Move transform bodies run only inside the per-note
#   loop of Models._transformFields (Models.java:722-726), so the model needs at least one note.
# - Over-approximation: auto_calls.json maps Models._transformFields (Models.java:726) to all three transform bodies
#   (dispatch cha). Each call site passes one visitor, so no pair is suppressed.
