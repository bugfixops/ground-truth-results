# ---- AnkiDroid combined fix batch (merge lead, 2026-11-02) ----
# Assembled from the audited turn fragments, verbatim. The lead-owned
# section at the end (CURSOR parallel page + NEW_COLLECTION page) is the
# merger's own addition, independently audited before inclusion.
# The fragments' own 'draft / not merged' headers are stale as of this merge:
# the text below IS the merged batch. Route 24 v3 is NOT copied here:
# its V01/V02 are byte-identical to route 30 v2's and its V03 differs only
# in evidence span; route 30 v2's V01/V02/V03 are applied ONCE below.
# Route 14 v1, route 24 v1/v2, route 27 v1/v2/v3 are NOT in this file.

# ---- route 11 ----
# ---- AnkiDroid route 11 FIX-DRAFT (helper draft only; NOT merged) ----
# Producer-aware listener-dispatch variant for @REBUILD_CRAM, keyed to the
# CustomStudyDialog launch site. Route 11 target: StudyOptionsActivity.closeStudyOptions(int).
# Fiction fixed: the printed route's step 12 (shared type-union edge
# DeckTask$TaskListener.onPostExecute@REBUILD_CRAM -> CustomStudyDialog$4.onPostExecute,
# id E46c212fb) lets the StudyOptionsFragment rebuild launch reach $4, although that
# launch installs a different listener (see NOTES.md). This fragment gives the
# CustomStudyDialog launch its own variant chain whose listener set is $4 only.
#
# Placement (for the turn lead alone): append these e() edges as new
# graph_def_mod content, or to graphs/AnkiDroid/graph_def.py after the EDIT
# wrapper; either placement is fine for edges, because the builder applies EDIT
# to all edges only after the whole graph definition has executed. This file
# defines NO edit clause, NO suppression call, NO screens entry, and NO builder
# change. The companion EDIT-wrapper-draft.txt (appended to graph_def.py AFTER
# the current final EDIT definition, never here) neutralises the shared
# type-union edge; without it the fiction path survives, because BFS follows
# the shorter fragment-launch path first.
#
# Conventions (same as graph_def_mod/02.py): variant edges carry the condition
# as guard TEXT only; env and needs_state are never set on a variant edge, so
# variant chains keep the same BFS cost as the shared chains. Guards are free
# text and BFS ignores guard text, so enforcement here is topological, not
# guard-based: the producer chain's post set is $4 only, and the EDIT draft
# takes the shared fan-out edge out of BFS. Evidence uses plain SRC only.
# Node naming: the second suffix is the producer key. base() splits at the
# first '@', so these nodes share base methods with the shared @REBUILD_CRAM
# nodes and the hand-covering rule treats them the same way; no existing node
# uses a double suffix, so there is no collision.
#
# Existing edges deliberately NOT duplicated here:
# - CustomStudyDialog.createCustomStudySession -> DeckTask.doInBackground@REBUILD_CRAM
#   (shared type entry, graph_def_mod/02.py) stays: the launch genuinely creates
#   a REBUILD_CRAM task, and other launches keep their shared entries.
# - CustomStudyDialog.createCustomStudySession -> CustomStudyDialog$4.onPostExecute
#   (direct ASYNC edge, graph_def.py) stays: it is a genuine shortcut from the
#   same launch, and BFS may prefer it; it does not touch the fragment launch.
# - CustomStudyDialog$4.onPostExecute -> DeckPicker.onCreateCustomStudySession and
#   -> StudyOptionsActivity.onCreateCustomStudySession (auto virtual-dispatch
#   copies of the CustomStudyListener call) stay: they are the host dispatch
#   after $4, distinct from the listener dispatch fixed here.

# Entry: the CustomStudyDialog launch only. Guard text names both the type
# condition (as in 02.py) and the producer; it is documentation, not the filter.
e('CustomStudyDialog.createCustomStudySession', 'DeckTask.doInBackground@REBUILD_CRAM@CustomStudyDialog', 'ASYNC',
  "this launch call creates the task instance whose type is REBUILD_CRAM; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_REBUILD_CRAM and launch site is CustomStudyDialog.createCustomStudySession', env=None,
  evidence='SRC CustomStudyDialog.java:454; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# Body: producer-independent switch case, same body method as the shared variant.
e('DeckTask.doInBackground@REBUILD_CRAM@CustomStudyDialog', 'DeckTask.doInBackgroundRebuildCram', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:270-271')

# Post chain, producer variant only (mirrors the 02.py section 3 pattern).
e('DeckTask.doInBackground@REBUILD_CRAM@CustomStudyDialog', 'DeckTask.onPostExecute@REBUILD_CRAM@CustomStudyDialog', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@REBUILD_CRAM@CustomStudyDialog', 'DeckTask$TaskListener.onPostExecute@REBUILD_CRAM@CustomStudyDialog', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
# Listener set is $4 ONLY. The delegate line is the dispatch mechanism; the
# launch line is the producer binding (the anonymous listener installed at
# CustomStudyDialog.java:454 is $4, whose onPostExecute is at :467).
e('DeckTask$TaskListener.onPostExecute@REBUILD_CRAM@CustomStudyDialog', 'CustomStudyDialog$4.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306; SRC CustomStudyDialog.java:454')

# ---- route 12 ----
# ---- AnkiDroid route 12 FIX DRAFT (turn lead merges; this file is NOT merged by its author) ----
# Target: HttpFetcher.downloadFileToSdCardMethod, final-draw route 12, WRONG at step 15.
# Printed fiction: NavigationDrawerActivity.onNavigationItemSelected -> DeckPicker.openCardBrowser
# (Ea0eba485). Corrected step 15: ... -> Reviewer.openCardBrowser; corrected step 16:
# Reviewer.openCardBrowser -> CardBrowser.<init> (edge already in the graph).
# This fragment supplies e() edges ONLY. It defines no EDIT, no suppression call, no SCREENS
# entry, and no builder edit. Any EDIT clause needed to activate it lives in the companion
# file EDIT-wrapper-draft.txt and MUST be appended to graphs/AnkiDroid/graph_def.py AFTER
# the current final EDIT definition, never inside this file (the mod loader in
# graph_def.py runs before the EDIT definitions, so an EDIT written in a mod file would
# be replaced by them and never applied). This fragment itself may be appended as a new
# graphs/AnkiDroid/graph_def_mod/NN.py file (it runs in the same namespace as
# graph_def.py, so e() is available), or appended to graph_def.py after the EDIT
# wrapper; either placement is fine for edges, because the builder applies EDIT to all
# edges only after the whole graph definition has been executed.
#
# Mechanism (A1 variant conventions, graph_def_mod/02.py header): receiver-variant
# dispatch nodes. The extractor already emits receiver-variant auto call records for
# this dispatch (gtr/graphs/AnkiDroid/auto_calls.json: src
# NavigationDrawerActivity.onNavigationItemSelected@Reviewer -> Reviewer.openCardBrowser
# and src ...@DeckPicker -> DeckPicker.openCardBrowser, both at
# NavigationDrawerActivity.java:263), but no page edge enters either variant node, so
# the variant nodes are unreachable and BFS never uses them. This fragment adds exactly
# those page entries, plus hand dispatch edges mirroring the shared dispatch node's
# hand out-edges, resolved per receiver. Variant edges carry the receiver condition as
# guard TEXT only: env and needs_state are never set on a variant edge, so variant
# chains keep the same BFS cost as the shared chains.
#
# ACTIVATION WARNING (see NOTES.md section 4): this fragment alone does NOT change the
# printed route. The corrected chain and the shared chain have identical BFS cost
# (env, setup, steps), and the builder's cheapest() breaks cost ties by edge-definition
# order, where the shared page edge (graph_def.py batch 036) precedes any fragment
# edge. The companion EDIT-wrapper-draft.txt reclassifies the two receiver page edges
# to the shared node as REGISTER (BFS-invisible), which makes the variant page edges
# the only drawer entry from S_REVIEWER and S_DECKPICKER. Without that wrapper (or the
# equivalent merger deletion of those two page edges), the printed route keeps the
# shared node and the step-15 fiction. The turn lead must apply one of the two.
#
# No edge here touches the ConfirmationDialog confirm/cancel dispatch edges, and no
# edge here deletes or reclassifies any shared dispatch edge: the shared node stays
# fully intact for the StudyOptions, Statistics, and CardBrowser screens, which have
# no receiver variant in this draft.

# ================================================================== 1. Variant page edges =====
# One GUI edge per receiver page, mirroring the existing shared page edges (same gui
# text, so device/gui steps are unchanged). Evidence mirrors the shared page edges.

e('S_REVIEWER', 'NavigationDrawerActivity.onNavigationItemSelected@Reviewer', 'GUI',
  'pick an item in the navigation drawer on the reviewer',
  gui=['pick an item in the navigation drawer on the reviewer'],
  guard='the running activity is Reviewer: Reviewer extends AbstractFlashcardViewer, which extends NavigationDrawerActivity, so the drawer listener runs on a Reviewer instance',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:110; SRC com/ichi2/anki/Reviewer.java:56; SRC com/ichi2/anki/NavigationDrawerActivity.java:249-290',
  note='Receiver-variant page edge. The NavigationView dispatch is the support library, not in fw_src: INFERRED. The shared page edge to the base node is reclassified by the companion EDIT wrapper; this edge replaces it for the Reviewer receiver only.')

e('S_DECKPICKER', 'NavigationDrawerActivity.onNavigationItemSelected@DeckPicker', 'GUI',
  'pick an item in the navigation drawer on the deck list',
  gui=['pick an item in the navigation drawer on the deck list'],
  guard='the running activity is DeckPicker: DeckPicker extends NavigationDrawerActivity, so the drawer listener runs on a DeckPicker instance',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:68, 249-290; SRC com/ichi2/anki/DeckPicker.java:110',
  note='Receiver-variant page edge. The NavigationView dispatch is the support library, not in fw_src: INFERRED. The shared page edge to the base node is reclassified by the companion EDIT wrapper; this edge replaces it for the DeckPicker receiver only.')

# ================================================================== 2. Reviewer-receiver dispatch =====
# Mirrors all six hand out-edges of the shared dispatch node that apply to this
# receiver, with nav_browser resolved to the Reviewer override. The nav_help and
# nav_feedback items need no hand edge here: the extractor's auto call records from
# the @Reviewer variant node (openUrl, getManualUrl, getFeedbackUrl) already cover
# them, exactly as they do from the base node. MG302 (the chosen item must not
# already be checked, NavigationDrawerActivity.java:252) is a note only, as on the
# shared edges: env and needs_state unset.

e('NavigationDrawerActivity.onNavigationItemSelected@Reviewer', 'DeckPicker.<init>', 'INTENT',
  'choose the Decks item in the drawer on the reviewer: start DeckPicker with CLEAR_TOP and NEW_TASK',
  guard='receiver is Reviewer; this drawer item is handled by the base-class branch, identical for every receiver',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:252-260',
  note='MISSING GATE MG302: the Decks item is not already checked (NavigationDrawerActivity.java:252 returns true when it is). env and needs_state unset.')

e('NavigationDrawerActivity.onNavigationItemSelected@Reviewer', 'Statistics.<init>', 'INTENT',
  'choose the Statistics item in the drawer on the reviewer: start Statistics with the selected deck',
  guard='receiver is Reviewer; this drawer item is handled by the base-class branch, identical for every receiver',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:265-268',
  note='MISSING GATE MG302: the Statistics item is not already checked (NavigationDrawerActivity.java:252). The request code is REQUEST_STATISTICS. env and needs_state unset.')

e('NavigationDrawerActivity.onNavigationItemSelected@Reviewer', 'Preferences.<init>', 'INTENT',
  'choose the Settings item in the drawer on the reviewer: start Preferences with REQUEST_PREFERENCES_UPDATE',
  guard='receiver is Reviewer; this drawer item is handled by the base-class branch, identical for every receiver',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:273-277',
  note='MISSING GATE MG302: the Settings item is not already checked (NavigationDrawerActivity.java:252). env and needs_state unset.')

e('NavigationDrawerActivity.onNavigationItemSelected@Reviewer', 'Reviewer.openCardBrowser', 'CALL',
  'choose the Card browser item in the drawer on the reviewer (virtual dispatch to the Reviewer override)',
  guard='receiver is Reviewer: the virtual call at NavigationDrawerActivity.java:263 resolves openCardBrowser() to the Reviewer override',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:262-264; SRC com/ichi2/anki/Reviewer.java:507-518',
  note='MISSING GATE MG302: the Card browser item is not already checked (NavigationDrawerActivity.java:252). This is corrected route-12 step 15. The hand edge also covers the extractor auto record @Reviewer -> Reviewer.openCardBrowser (NavigationDrawerActivity.java:263), so that auto copy is skipped by the hand-covering rule. env and needs_state unset.')

e('NavigationDrawerActivity.onNavigationItemSelected@Reviewer', 'NavigationDrawerActivity$2.onCheckedChanged', 'FRAMEWORK',
  'choose the night-mode item in the drawer on the reviewer: performClick toggles the switch and fires its listener',
  guard='receiver is Reviewer; this drawer item is handled by the base-class branch, identical for every receiver',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:270-272, 89-105',
  note='MISSING GATE MG302: the night-mode item is not already checked (NavigationDrawerActivity.java:252). The click dispatch on SwitchCompat/CompoundButton is the support library, not in fw_src: INFERRED. env and needs_state unset.')

e('NavigationDrawerActivity.onNavigationItemSelected@Reviewer', 'NavigationDrawerActivity$3.onDrawerClosed', 'FRAMEWORK',
  'closeDrawers at line 288 calls the drawer listener, which runs onDrawerClosed (reviewer drawer)',
  guard='receiver is Reviewer; the drawer-close callback is identical for every receiver',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:288, 110-113',
  note='The DrawerLayout dispatch to the listener is the support library, not in fw_src: INFERRED.')

# ================================================================== 3. DeckPicker-receiver dispatch =====
# Mirrors all six hand out-edges of the shared dispatch node that apply to this
# receiver, with nav_browser resolved to the DeckPicker override. The DeckPicker
# receiver keeps its own dispatch: its nav_browser edge below is the genuine
# DeckPicker override, not the shared node's fan-out. nav_help / nav_feedback are
# covered by the extractor auto records from the @DeckPicker variant node, as above.
# MG302 is a note only, as on the shared edges.

e('NavigationDrawerActivity.onNavigationItemSelected@DeckPicker', 'DeckPicker.<init>', 'INTENT',
  'choose the Decks item in the drawer on the deck list: start DeckPicker with CLEAR_TOP and NEW_TASK',
  guard='receiver is DeckPicker; this drawer item is handled by the base-class branch, identical for every receiver',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:252-260',
  note='MISSING GATE MG302: the Decks item is not already checked (NavigationDrawerActivity.java:252 returns true when it is). env and needs_state unset.')

e('NavigationDrawerActivity.onNavigationItemSelected@DeckPicker', 'Statistics.<init>', 'INTENT',
  'choose the Statistics item in the drawer on the deck list: start Statistics with the selected deck',
  guard='receiver is DeckPicker; this drawer item is handled by the base-class branch, identical for every receiver',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:265-268',
  note='MISSING GATE MG302: the Statistics item is not already checked (NavigationDrawerActivity.java:252). The request code is REQUEST_STATISTICS. env and needs_state unset.')

e('NavigationDrawerActivity.onNavigationItemSelected@DeckPicker', 'Preferences.<init>', 'INTENT',
  'choose the Settings item in the drawer on the deck list: start Preferences with REQUEST_PREFERENCES_UPDATE',
  guard='receiver is DeckPicker; this drawer item is handled by the base-class branch, identical for every receiver',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:273-277',
  note='MISSING GATE MG302: the Settings item is not already checked (NavigationDrawerActivity.java:252). env and needs_state unset.')

e('NavigationDrawerActivity.onNavigationItemSelected@DeckPicker', 'DeckPicker.openCardBrowser', 'CALL',
  'choose the Card browser item in the drawer on the deck list (virtual dispatch to the DeckPicker override)',
  guard='receiver is DeckPicker: the virtual call at NavigationDrawerActivity.java:263 resolves openCardBrowser() to the DeckPicker override',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:262-264; SRC com/ichi2/anki/DeckPicker.java:1707-1713',
  note='MISSING GATE MG302: the Card browser item is not already checked (NavigationDrawerActivity.java:252). The hand edge also covers the extractor auto record @DeckPicker -> DeckPicker.openCardBrowser (NavigationDrawerActivity.java:263), so that auto copy is skipped by the hand-covering rule. env and needs_state unset.')

e('NavigationDrawerActivity.onNavigationItemSelected@DeckPicker', 'NavigationDrawerActivity$2.onCheckedChanged', 'FRAMEWORK',
  'choose the night-mode item in the drawer on the deck list: performClick toggles the switch and fires its listener',
  guard='receiver is DeckPicker; this drawer item is handled by the base-class branch, identical for every receiver',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:270-272, 89-105',
  note='MISSING GATE MG302: the night-mode item is not already checked (NavigationDrawerActivity.java:252). The click dispatch on SwitchCompat/CompoundButton is the support library, not in fw_src: INFERRED. env and needs_state unset.')

e('NavigationDrawerActivity.onNavigationItemSelected@DeckPicker', 'NavigationDrawerActivity$3.onDrawerClosed', 'FRAMEWORK',
  'closeDrawers at line 288 calls the drawer listener, which runs onDrawerClosed (deck-list drawer)',
  guard='receiver is DeckPicker; the drawer-close callback is identical for every receiver',
  env=None,
  evidence='SRC com/ichi2/anki/NavigationDrawerActivity.java:288, 110-113',
  note='The DrawerLayout dispatch to the listener is the support library, not in fw_src: INFERRED.')

# ---- route 14 v2 (v1 never merged) ----
# ---- DRAFT ONLY, AnkiDroid route 14 v2 (Models$TransformFieldDelete.<init>) ----
# Turn-lead merge only. This file is never pushed by the drafter and edits
# no graph, branch, tool, workflow, or output file.
#
# v2 SUPERSEDES v1 entirely. The merger applies THIS file plus
# v2/EDIT-wrapper-draft.txt only, never v1 + v2 together (that would
# duplicate the 10 v1 edges). The v1 files stay intact as the failed
# record; nothing here edits them.
#
# Why v2 exists (AUDIT2 FAIL on v1): v1 sealed only two of the four
# hand ENTERS edges into the shared S_DLG_CONFIRMATION page. The
# add-field entry (ModelFieldEditor$2.onPositive) stayed open, and the
# auditor's simulation showed route 14 re-printing as a NEW fiction of
# the same kind, 18 edges via $2.onPositive -> generic -> $3.confirm,
# beating the genuine 21-edge variant route. v2 closes the $2 entry as
# well, with its own variant page carrying $2$1.confirm/cancel, so no
# method loses its only route.
#
# Why the sortByField entry is NOT closed in v2 (deliberate, reasoned
# choice, see NOTES.md section 6): sortByField is the last entry keeping
# the generic page reachable. Closing it as well flips 14 labeled
# REACHABLE methods that have no variant page and no other entry into
# the generic page (NoteEditor, CardTemplate, reposition $6$1 confirms
# and the ConfirmationDialog fan-out nodes). The sort entry stays open
# in v2, and the genuine route wins over the sort prefix only by a
# BFS discovery-order tie at $3.confirm depth 16. That tie is flagged
# as fragile in NOTES.md, and the merger's rebuild re-print is the
# gate: if the rebuild prints route 14 via sort -> generic, v2 fails
# and the sort split plus a full dialog split is required.
#
# Conventions (from graph_def_mod/02.py and the A1 variant work):
# - Variant edges carry the condition as guard TEXT only. env is always
#   None on a variant edge and no needs_state argument is passed, so a
#   variant chain keeps the same BFS cost as the shared chain and wins
#   only on the node sequence, not on cost.
# - Evidence strings below are copied from the existing generic-page
#   edges for the same dialog, so no evidence claim is new except the
#   page identity itself, which the guard text states. One exception,
#   carried over from v1 and disclosed in NOTES.md section 4: R14-V06
#   is WIDENED (235-256) relative to the generic ENTERS evidence
#   (239-256), so the cited range includes the method head (:235) and
#   the guard (:236-237). It is not verbatim.
# - This file defines no chained wrapper, no deletion, and no call
#   that removes edges. It adds edges only. Adding edges alone cannot
#   remove the three existing generic ENTERS edges (a hand edge is
#   removed only by the merger deleting its line, or by the companion
#   wrapper draft changing its kind); see NOTES.md and the companion
#   wrapper draft in the same folder. The companion wrapper is
#   load-bearing: without it, BFS can still enter the generic page
#   from deleteModelDialog, deleteFieldDialog, and $2.onPositive and
#   reach $3.confirm.
# - Nothing in this file touches the ConfirmationDialog$1.onPositive /
#   onNegative dispatch fan-out, and nothing here touches any direct
#   generic-page GUI edge. Those edges stay exactly as built; they
#   become unreachable from these three show-methods only because the
#   three generic ENTERS edges are made BFS-invisible by the wrapper.
# - No edge, guard, trigger, evidence string, or comment in this file
#   uses any literal that checks 5-7 grep for.
#
# Edge inventory: 3 SCREENS entries, 3 ENTERS edges, 10 GUI dispatch
# edges (4 + 4 for the two v1 pages, 2 for the new add-field page).
# 13 e() calls total: R14-V01..V10 carried over unchanged from v1,
# R14-V11..V13 new in v2.

SCREENS['S_DLG_CONFIRMATION_MODELBROWSER_DELETEMODEL'] = 'ConfirmationDialog: ModelBrowser delete-note-type dialog (ModelBrowser$7/$8)'
SCREENS['S_DLG_CONFIRMATION_MODELFIELDEDITOR_DELETEFIELD'] = 'ConfirmationDialog: ModelFieldEditor delete-field dialog (ModelFieldEditor$3/$4)'
SCREENS['S_DLG_CONFIRMATION_MODELFIELDEDITOR_ADDFIELD'] = 'ConfirmationDialog: ModelFieldEditor add-field sync-required dialog (ModelFieldEditor$2$1)'

# ---- R14-V01: ModelBrowser delete-model dialog, variant entry ----
# Replaces, for this dialog only, the generic ENTERS edge
# ModelBrowser.deleteModelDialog -> S_DLG_CONFIRMATION.
# Source: deleteModelDialog shows a ConfirmationDialog at :466 (dialog d,
# try branch) and at :484 (dialog c, catch branch); the list-size gate
# is at :448 and the last-model toast is at :490.
e('ModelBrowser.deleteModelDialog', 'S_DLG_CONFIRMATION_MODELBROWSER_DELETEMODEL', 'ENTERS',
  'the delete note type confirmation dialog (ConfirmationDialog) is shown',
  env=None,
  guard='mModelIds.size() > 1 (ModelBrowser.java:448); with one note type only the last-model toast is shown (ModelBrowser.java:490)',
  evidence='SRC com/ichi2/anki/ModelBrowser.java:448, 466, 484, 490')

# ---- R14-V02: variant dispatch, delete-model dialog d (try branch) ----
# Anonymous confirm $7: confirm() calls deleteModel() at :455.
# Evidence copied from the existing generic-page $7.confirm edge.
e('S_DLG_CONFIRMATION_MODELBROWSER_DELETEMODEL', 'ModelBrowser$7.confirm', 'GUI',
  'press OK on the delete note type confirmation dialog',
  gui=['press OK on the delete note type confirmation dialog'],
  env=None,
  guard='shown dialog is deleteModelDialog dialog d (ModelBrowser.java:450-466; modSchema() does not throw)',
  evidence='SRC com/ichi2/anki/ModelBrowser.java:448-466, 451-460; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-44; SRC com/ichi2/libanki/Collection.java:364-382; SRC com/ichi2/libanki/Storage.java:317-319')

# ---- R14-V03: variant dispatch, delete-model dialog d, cancel ----
# Anonymous cancel $7: cancel() dismisses the context menu at :461-463.
# Evidence copied from the existing generic-page $7.cancel edge.
e('S_DLG_CONFIRMATION_MODELBROWSER_DELETEMODEL', 'ModelBrowser$7.cancel', 'GUI',
  'press Cancel on the delete note type confirmation dialog',
  gui=['press Cancel on the delete note type confirmation dialog'],
  env=None,
  guard='shown dialog is deleteModelDialog dialog d (ModelBrowser.java:450-466; modSchema() does not throw)',
  evidence='SRC com/ichi2/anki/ModelBrowser.java:461-463; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:46-49')

# ---- R14-V04: variant dispatch, delete-model dialog c (catch branch) ----
# Anonymous confirm $8: confirm() calls deleteModel() at :472.
# Evidence copied from the existing generic-page $8.confirm edge.
e('S_DLG_CONFIRMATION_MODELBROWSER_DELETEMODEL', 'ModelBrowser$8.confirm', 'GUI',
  'press OK on the full sync confirmation dialog for deleting a note type',
  gui=['press OK on the full sync confirmation dialog for deleting a note type'],
  env=None,
  guard='shown dialog is deleteModelDialog dialog c from the catch branch (ModelBrowser.java:467-484; modSchema() throws)',
  evidence='SRC com/ichi2/anki/ModelBrowser.java:467-484; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-44; SRC com/ichi2/libanki/Collection.java:364-382; SRC com/ichi2/libanki/sync/Syncer.java:423-428')

# ---- R14-V05: variant dispatch, delete-model dialog c, cancel ----
# Anonymous cancel $8: cancel() dismisses the context menu.
# Evidence copied from the existing generic-page $8.cancel edge.
e('S_DLG_CONFIRMATION_MODELBROWSER_DELETEMODEL', 'ModelBrowser$8.cancel', 'GUI',
  'press Cancel on the full sync confirmation dialog for deleting a note type',
  gui=['press Cancel on the full sync confirmation dialog for deleting a note type'],
  env=None,
  guard='shown dialog is deleteModelDialog dialog c from the catch branch (ModelBrowser.java:467-484; modSchema() throws)',
  evidence='SRC com/ichi2/anki/ModelBrowser.java:467-484; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:46-49')

# ---- R14-V06: ModelFieldEditor delete-field dialog, variant entry ----
# Replaces, for this dialog only, the generic ENTERS edge
# ModelFieldEditor.deleteFieldDialog -> S_DLG_CONFIRMATION.
# Source: deleteFieldDialog shows the warning dialog at :256 (try
# branch, dialog d) and the sync-required dialog at :274 (catch branch,
# dialog c); with fewer than 2 fields it only toasts, at :236-237.
# Evidence WIDENED, not verbatim: 235-256 vs the generic 239-256.
e('ModelFieldEditor.deleteFieldDialog', 'S_DLG_CONFIRMATION_MODELFIELDEDITOR_DELETEFIELD', 'ENTERS',
  'the field delete warning is shown from the field context menu (delete); a second sync-required dialog uses the same variant page',
  env=None,
  guard='mFieldLabels.size() >= 2 (ModelFieldEditor.java:236-237); with fewer fields only the last-field toast is shown and no dialog appears',
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:235-256, 273-274')

# ---- R14-V07: variant dispatch, delete-field warning (try branch) ----
# Anonymous confirm $3: confirm() calls deleteField() at :245.
# Evidence copied from the existing generic-page $3.confirm edge.
# This is the corrected route-14 step: deleteFieldDialog -> variant
# page -> $3.confirm -> deleteField.
e('S_DLG_CONFIRMATION_MODELFIELDEDITOR_DELETEFIELD', 'ModelFieldEditor$3.confirm', 'GUI',
  'tap OK on the field delete warning',
  gui=['tap OK on the field delete warning'],
  env=None,
  guard='shown dialog is deleteFieldDialog warning dialog d (ModelFieldEditor.java:240-256; modSchema() does not throw)',
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:241-256; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-44')

# ---- R14-V08: variant dispatch, delete-field warning, cancel ----
# Anonymous cancel $3: cancel() dismisses the context menu at :251-253.
# Evidence copied from the existing generic-page $3.cancel edge.
e('S_DLG_CONFIRMATION_MODELFIELDEDITOR_DELETEFIELD', 'ModelFieldEditor$3.cancel', 'GUI',
  'tap Cancel on the field delete warning',
  gui=['tap Cancel on the field delete warning'],
  env=None,
  guard='shown dialog is deleteFieldDialog warning dialog d (ModelFieldEditor.java:240-256; modSchema() does not throw)',
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:251-253; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:46-49')

# ---- R14-V09: variant dispatch, sync-required delete dialog (catch) ----
# Anonymous confirm $4: confirm() calls deleteField() at :262.
# Evidence copied from the existing generic-page $4.confirm edge.
# $4 must move with $3: if $4 stayed on the generic page, the fiction
# would survive one step longer, via deleteModelDialog -> generic
# page -> $4.confirm -> deleteField, instead of via $3.confirm.
e('S_DLG_CONFIRMATION_MODELFIELDEDITOR_DELETEFIELD', 'ModelFieldEditor$4.confirm', 'GUI',
  'tap OK on the sync-required field delete dialog (full sync confirmation)',
  gui=['tap OK on the sync-required field delete dialog (full sync confirmation)'],
  env=None,
  guard='shown dialog is deleteFieldDialog sync-required dialog c from the catch branch (ModelFieldEditor.java:257-274; modSchema() throws)',
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:259-267; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-44')

# ---- R14-V10: variant dispatch, sync-required delete dialog, cancel ----
# Anonymous cancel $4: cancel() dismisses the context menu at :269-271.
# Evidence copied from the existing generic-page $4.cancel edge.
e('S_DLG_CONFIRMATION_MODELFIELDEDITOR_DELETEFIELD', 'ModelFieldEditor$4.cancel', 'GUI',
  'tap Cancel on the sync-required field delete dialog',
  gui=['tap Cancel on the sync-required field delete dialog'],
  env=None,
  guard='shown dialog is deleteFieldDialog sync-required dialog c from the catch branch (ModelFieldEditor.java:257-274; modSchema() throws)',
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:269-271; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:46-49')

# ---- R14-V11 (NEW in v2): ModelFieldEditor add-field dialog, variant entry ----
# Replaces, for this dialog only, the generic ENTERS edge
# ModelFieldEditor$2.onPositive -> S_DLG_CONFIRMATION (graph_def.py:4670).
# Source, re-read for v2: addFieldDialog (ModelFieldEditor.java:175)
# builds a MaterialDialog whose OK callback is $2.onPositive (:186);
# on a valid new field name it calls mCol.modSchema() at :197, and on
# the ConfirmModSchemaException catch branch (:200) it creates
# ConfirmationDialog c (:203) and shows it at :219 via
# ModelFieldEditor.this.showDialogFragment(c). The dialog's own
# confirm is $2$1 (confirm at :204-211, ADD_FIELD relaunch at :208-209;
# cancel at :213-215). Without this split, $2.onPositive -> generic ->
# $3.confirm is the 18-edge fiction that failed v1 (AUDIT2).
# Evidence copied from the existing generic-page ENTERS edge.
e('ModelFieldEditor$2.onPositive', 'S_DLG_CONFIRMATION_MODELFIELDEDITOR_ADDFIELD', 'ENTERS',
  'the sync-required add-field dialog (full sync confirmation) is shown when the schema change needs confirmation',
  env=None,
  guard='shown dialog is the add-field sync-required dialog c (ModelFieldEditor.java:200-219; modSchema() throws at :197, catch at :200)',
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:200-219; SRC com/ichi2/libanki/Collection.java:364-374; SRC com/ichi2/libanki/Storage.java:317-319; SRC com/ichi2/libanki/sync/Syncer.java:424-429')

# ---- R14-V12 (NEW in v2): variant dispatch, add-field sync-required dialog ----
# Anonymous confirm $2$1: confirm() relaunches ADD_FIELD at :208-209.
# Evidence copied from the existing generic-page $2$1.confirm edge
# (graph_def.py:4682-4687). $2$1.confirm keeps its pre-existing
# outgoing ASYNC edge to ModelFieldEditor$8.onPostExecute; only how
# the confirm node itself is reached changes.
e('S_DLG_CONFIRMATION_MODELFIELDEDITOR_ADDFIELD', 'ModelFieldEditor$2$1.confirm', 'GUI',
  'tap OK on the sync-required add-field dialog (full sync confirmation)',
  gui=['tap OK on the sync-required add-field dialog (full sync confirmation)'],
  env=None,
  guard='shown dialog is the add-field sync-required dialog c (ModelFieldEditor.java:203-219; modSchema() throws)',
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:204-211; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-44')

# ---- R14-V13 (NEW in v2): variant dispatch, add-field dialog, cancel ----
# Anonymous cancel $2$1: cancel() dismisses the context menu at :213-215.
# Evidence copied from the existing generic-page $2$1.cancel edge
# (graph_def.py:4689-4694). $2$1.cancel moves with $2$1.confirm: a
# split that moved only the confirm would leave the cancel reachable
# only through the generic page from the wrong dialog's prefix.
e('S_DLG_CONFIRMATION_MODELFIELDEDITOR_ADDFIELD', 'ModelFieldEditor$2$1.cancel', 'GUI',
  'tap Cancel on the sync-required add-field dialog',
  gui=['tap Cancel on the sync-required add-field dialog'],
  env=None,
  guard='shown dialog is the add-field sync-required dialog c (ModelFieldEditor.java:203-219; modSchema() throws)',
  evidence='SRC com/ichi2/anki/ModelFieldEditor.java:213-215; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:46-49')

# ---- route 20 ----
# ---- AnkiDroid route 20 FIX-DRAFT (turn lead merges; auditor judges) ----
# Target: libanki.Utils.base62. Fiction fixed: printed step 19 (E62a24da3),
# Note.<init>(Collection,JSONObject,Long) -> libanki.Utils.guid64, sits in the
# id == null (new-note) branch of the constructor (Note.java:67-72) but was
# claimed on the CHECK_MEDIA prefix, where the id is an existing note id
# (Media._normalizeNoteRefs -> Collection.getNote -> Note.<init>(Collection,Long)).
#
# Mechanism (A1 variant conventions, as in graph_def_mod/02.py): branch-sensitive
# constructor variants keyed on the id argument of the 3-arg constructor.
#   Note.<init>(Collection,JSONObject,Long)@id-null  -- id == null, new note
#   Note.<init>(Collection,JSONObject,Long)@id-set   -- id != null, existing note
# Variant edges carry the branch condition as guard TEXT only; env is None and
# no needs_state is set on any edge below, so variant chains keep the same BFS
# cost as the shared chains and win only on steps.
#
# HOW TO APPLY (draft only; the turn lead merges after audit):
#   Append the e() calls below to graphs/AnkiDroid/graph_def_mod/02.py (they run
#   in the graph_def.py namespace, so e() is available), or to graph_def.py
#   after the EDIT wrapper; either placement is fine for edges, because the
#   builder applies EDIT to all edges only after the whole graph definition
#   has been executed.
#   This file supplies e() edges ONLY. It defines no EDIT, no sup() call, no
#   SCREENS entry, and no builder edit. No EDIT clause is needed for this fix:
#   every auto edge this split replaces is suppressed by the hand-covering
#   rule (build_graph.py add_auto_edges: an auto edge is skipped when a hand
#   edge shares its (src, base(dst)) or (base(src), base(dst)) pair), and the
#   variant-copy loop only re-emits UNSUPPRESSED auto edges onto variants.
#   See NOTES.md for the pair-by-pair suppression table.
#
# WHAT THIS FILE DELIBERATELY DOES NOT TOUCH:
#   - No ModelFieldEditor confirm/cancel dispatch edge is added, removed, or
#     retargeted here; this fragment touches Note constructors only.
#   - No shared edge is deleted by this file: suppression of the shared
#     constructor edges is done by the hand-covering rule, not by sup().
#   - The guid64 -> base91 -> base62 tail is NOT re-written: those calls are
#     branch-independent (guid64 always calls base91, base91 always calls
#     base62), so the existing edges stand and the tail is reachable only
#     from the @id-null variant after this split.
#   - No new head edge is written: the corrected route's head already exists
#     in the graph (CardBrowser.onOptionsItemSelected -> NoteEditor.<init>
#     INTENT edge, graph_def.py; NoteEditor.onCollectionLoaded ->
#     NoteEditor.setNote(Note) and setNote(Note) -> Note.<init>(Collection,
#     JSONObject) auto edges). This fragment only splits the constructor.
#   - The auto edge Note.<init>(Collection,JSONObject,Long) ->
#     libanki.Utils.<clinit> (Note.java:71) is intentionally left unsplit:
#     it is not a branch call, and the builder copies it onto both variants.
#     It is on no route to base62.
#
# Edge count: 9 hand edges -- 2 delegating-constructor retargets, 1 @id-set
# outgoing edge, 6 @id-null outgoing edges. No generic restoration edges:
# the 3-arg constructor has no direct caller in the tree (every construction
# goes through one of the two delegating constructors, both retargeted
# below), so no generic caller remains. The base 3-arg node stays reachable
# through its variants (build_graph.py first_variant maps variant nodes back
# to their base method for the reachability verdict).
#
# Node-name convention: the variant suffix follows the A1 '@' convention
# (DeckTask.doInBackground@CHECK_MEDIA, CustomStudyDialog.<init>@0). base()
# splits on the first '@', so the base of each variant below is the plain
# 3-arg constructor name.

# ======================================================================
# 1. Delegating-constructor retargets (incoming edges to the variants)
# ======================================================================

# 1-R1: the long delegating constructor forwards its id unchanged, so its
# target is the @id-set variant. Its only caller in the whole tree is
# Collection.getNote (Collection.java:426), which passes a primitive long;
# autoboxing a primitive long can never yield null, so the forwarded id is
# always non-null. This hand edge suppresses the auto edge
# Note.<init>(Collection,Long) -> Note.<init>(Collection,JSONObject,Long)
# (Note.java:55).
e('Note.<init>(Collection,Long)',
  'Note.<init>(Collection,JSONObject,Long)@id-set', 'CALL', 'Direct call',
  guard='id passed through unchanged (this(col, null, id)); the only caller passes a primitive long, so the boxed id is non-null',
  env=None,
  evidence='SRC com/ichi2/libanki/Note.java:55 (bytecode); SRC com/ichi2/libanki/Collection.java:426 (bytecode)')

# 1-R2: the model delegating constructor passes the literal null as the id,
# so its target is the @id-null variant, for every caller of this constructor
# (NoteEditor.setNote(Note) at NoteEditor.java:1370, Collection.newNote at
# Collection.java:506, CardContentProvider bulkInsertNotes/insert). This hand
# edge suppresses the auto edge Note.<init>(Collection,JSONObject) ->
# Note.<init>(Collection,JSONObject,Long) (Note.java:60).
e('Note.<init>(Collection,JSONObject)',
  'Note.<init>(Collection,JSONObject,Long)@id-null', 'CALL', 'Direct call',
  guard='id == null: the delegating call passes the literal null (this(col, model, null))',
  env=None,
  evidence='SRC com/ichi2/libanki/Note.java:60 (bytecode)')

# ======================================================================
# 2. @id-set variant outgoing edge (existing-note branch, Note.java:67-69)
# ======================================================================

# 2-S1: the id != null branch calls load() and nothing else branch-specific.
# This hand edge suppresses the auto edge
# Note.<init>(Collection,JSONObject,Long) -> Note.load (Note.java:69).
# The @id-set variant therefore has NO edge to guid64, timestampID, or any
# other else-branch call, so the CHECK_MEDIA prefix (which arrives here via
# 1-R1) ends at load() and cannot reach base62.
e('Note.<init>(Collection,JSONObject,Long)@id-set',
  'Note.load', 'CALL', 'Direct call',
  guard='id != null, passed through: the if branch (id != null) calls load()',
  env=None,
  evidence='SRC com/ichi2/libanki/Note.java:67-69 (bytecode)')

# ======================================================================
# 3. @id-null variant outgoing edges (new-note branch, Note.java:70-86)
# ======================================================================

# 3-N1: else-branch first statement: fresh id from timestampID.
# Suppresses the auto edge (Note.java:71).
e('Note.<init>(Collection,JSONObject,Long)@id-null',
  'libanki.Utils.timestampID', 'CALL', 'Direct call',
  guard='id == null, passed through: the else branch assigns a fresh id',
  env=None,
  evidence='SRC com/ichi2/libanki/Note.java:71 (bytecode)')

# 3-N2: the argument evaluation of 3-N1 reads the collection database.
# Suppresses the auto edge (Note.java:71).
e('Note.<init>(Collection,JSONObject,Long)@id-null',
  'Collection.getDb', 'CALL', 'Direct call',
  guard='id == null, passed through: getDb is the timestampID argument',
  env=None,
  evidence='SRC com/ichi2/libanki/Note.java:71 (bytecode)')

# 3-N3: else-branch guid assignment -- the edge the printed route claimed on
# the wrong prefix. Reachable ONLY from the @id-null variant after this
# split. Suppresses the auto edge E62a24da3 (Note.java:72).
e('Note.<init>(Collection,JSONObject,Long)@id-null',
  'libanki.Utils.guid64', 'CALL', 'Direct call',
  guard='id == null, passed through: the else branch assigns guid64()',
  env=None,
  evidence='SRC com/ichi2/libanki/Note.java:72 (bytecode)')

# 3-N4: else-branch field-map lookup via the models object.
# Suppresses the auto edge (Note.java:84).
e('Note.<init>(Collection,JSONObject,Long)@id-null',
  'Collection.getModels', 'CALL', 'Direct call',
  guard='id == null, passed through: getModels is the fieldMap receiver',
  env=None,
  evidence='SRC com/ichi2/libanki/Note.java:84 (bytecode)')

# 3-N5: else-branch field-map construction from the new note's model.
# Suppresses the auto edge (Note.java:84).
e('Note.<init>(Collection,JSONObject,Long)@id-null',
  'Models.fieldMap', 'CALL', 'Direct call',
  guard='id == null, passed through: the else branch builds the field map',
  env=None,
  evidence='SRC com/ichi2/libanki/Note.java:84 (bytecode)')

# 3-N6: else-branch schema-modification timestamp read.
# Suppresses the auto edge (Note.java:85).
e('Note.<init>(Collection,JSONObject,Long)@id-null',
  'Collection.getScm', 'CALL', 'Direct call',
  guard='id == null, passed through: the else branch reads the schema timestamp',
  env=None,
  evidence='SRC com/ichi2/libanki/Note.java:85 (bytecode)')

# End of route-20 fix draft. No EDIT, no sup(), no SCREENS entry in this file.

# ---- route 23 (V02/V03 KEPT, lead decision) ----
# ---- DRAFT ONLY: AnkiDroid route 23 (Sched.getToday) token-aware branch routing ----
# DRAFT, NOT MERGED. The turn lead alone merges, after independent audit.
# This file supplies e() edges only. It defines no EDIT, no suppression
# call, no SCREENS entry, and no change to any edge for route steps 1-16.
# It is written to be appended in the same namespace as graph_def.py
# (as graph_def_mod/02.py content is), where e() is already defined.
#
# Mechanism (A1 variant conventions, as in graph_def_mod/02.py):
# variant edges carry the condition as guard TEXT only; env is never set
# on a variant edge and needs_state is never set, so variant chains keep
# the same BFS cost as the shared chains. New variant nodes use the
# @suffix form (base() strips the suffix), so validation against the
# method list still passes on the base method name.
#
# Why hand-covering alone suppresses the fiction, with no EDIT needed:
# the builder skips an auto edge whenever a hand edge shares its
# (base(src), base(dst)) pair. Each hand edge below shares a base pair
# with exactly one auto edge, so those auto edges are skipped:
#   - R23-V01/V02/V03 share (Finder._where, Finder._findCardState) and
#     together suppress the generic auto edge Efa260a34
#     (Finder._where -> Finder._findCardState, Finder.java:324).
#   - R23-V04 shares (Finder._findCardState, Sched.getToday) and
#     suppresses the generic auto edge E594578a7
#     (Finder._findCardState -> Sched.getToday, Finder.java:466).
#   - R23-V05 shares (Finder._findCardState, Sched.getDayCutoff) and
#     suppresses that auto edge (Finder.java:467).
#   - R23-V06 shares (Finder._findCardState, Collection.getSched) and
#     suppresses that auto edge (Finder.java:467).
# Suppressing all three outgoing auto edges matters: a surviving auto
# edge out of Finder._findCardState would be fanned out by the builder
# to every variant node of that method, which would put the suspended
# and buried variants back on a path to a method they never call.
# R23-V04/V05/V06 are therefore a set: dropping any one of them
# re-opens fan-out for that destination. R23-V02/V03, by contrast, are
# modelling only and may be dropped without recreating the fiction,
# because R23-V01 alone already suppresses the generic dispatch edge.
#
# Deliberately absent from this file:
#   - No restoration of the generic Finder._where -> Finder._findCardState
#     edge and no restoration of the generic Finder._findCardState ->
#     Sched.getToday edge. Restoring either would resurrect the fiction.
#   - No outgoing edge from Finder._findCardState@suspended or
#     Finder._findCardState@buried. Both branches return a string
#     constant and call no method, so those variant nodes are terminal
#     by construction: they cannot reach Sched.getToday.
#   - No variant node for the review / new / learn branches. Those
#     branches also return string constants and call no method
#     (Finder.java:452-460), so omitting them loses no method
#     reachability.
#   - No edge for any other Finder._where dispatch target
#     (Finder._findDeck, Finder._findTag, and the rest). Their auto
#     edges survive untouched because no hand edge shares their pairs.
#   - No change to the 16 confirm + 8 cancel dispatch edges, which are
#     dialog dispatch edges unrelated to this route and untouched here.
#
# Corrected BFS route after merge (same 18-step length as printed):
# steps 1-16 exactly as printed, then
#   17  Finder._where -> Finder._findCardState@due   (R23-V01)
#   18  Finder._findCardState@due -> Sched.getToday  (R23-V04)
# Condition: the selected deck is a filtered (dyn) deck
# (StudyOptionsFragment.java:346-348, rebuild item visible) and the
# rebuilt dyn deck's first search term terms[0] contains is:due
# (Sched.java:1560-1561, wrapped and suffixed at 1565-1569).

# R23-V01: dispatch instance for the is:due token.
# _where splits token is:due into cmd "is", val "due" and calls
# _findCardState("due") (Finder.java:296-299, 323-324). The guard names
# the data condition from _fillDyn: terms[0] is the user search term
# (Sched.java:1560-1561) and the final search string is that term plus
# the fixed suffix (Sched.java:1565-1569), so is:due reaches _where
# only when terms[0] itself contains it.
e('Finder._where', 'Finder._findCardState@due', 'CALL', 'Direct call',
  guard='query token is:due present: the rebuilt dyn deck first search term terms[0] contains is:due',
  env=None,
  evidence='SRC Finder.java:324 (bytecode); SRC Sched.java:1560-1561; SRC Sched.java:1565-1569')

# R23-V02: dispatch instance for the is:suspended token.
# The fixed _fillDyn suffix always contributes this token
# (Sched.java:1568), and _where dispatches it the same way
# (Finder.java:323-324). Its branch returns a string constant
# (Finder.java:461-462) and calls no method, so this node has no
# outgoing edge in this file.
e('Finder._where', 'Finder._findCardState@suspended', 'CALL', 'Direct call',
  guard='dispatch instance for the is:suspended token',
  env=None,
  evidence='SRC Finder.java:324 (bytecode); SRC Finder.java:461-462; SRC Sched.java:1568')

# R23-V03: dispatch instance for the is:buried token.
# Same dispatch as R23-V02 (Finder.java:323-324); its branch returns a
# string constant (Finder.java:463-464) and calls no method, so this
# node has no outgoing edge in this file.
e('Finder._where', 'Finder._findCardState@buried', 'CALL', 'Direct call',
  guard='dispatch instance for the is:buried token',
  env=None,
  evidence='SRC Finder.java:324 (bytecode); SRC Finder.java:463-464; SRC Sched.java:1568')

# R23-V04: the due branch calls getToday.
# Only val "due" takes this branch (Finder.java:465-467); the
# suspended and buried branches return constants before it.
e('Finder._findCardState@due', 'Sched.getToday', 'CALL', 'Direct call',
  guard='val == "due"',
  env=None,
  evidence='SRC Finder.java:466 (bytecode)')

# R23-V05: the same due-branch expression also calls getDayCutoff.
# Included so the generic auto edge for this destination is suppressed
# with the others instead of fanning out to the suspended and buried
# variants, which never call it (Finder.java:461-464).
e('Finder._findCardState@due', 'Sched.getDayCutoff', 'CALL', 'Direct call',
  guard='val == "due"',
  env=None,
  evidence='SRC Finder.java:467 (bytecode)')

# R23-V06: the same due-branch expression obtains the scheduler object
# whose getToday and getDayCutoff are then called (Finder.java:466-467).
# Included for the same fan-out reason as R23-V05.
e('Finder._findCardState@due', 'Collection.getSched', 'CALL', 'Direct call',
  guard='val == "due"',
  env=None,
  evidence='SRC Finder.java:466-467 (bytecode)')

# ---- route 30 v2 (shared @CONFIRM subgraph, applied ONCE; also serves route 24 v3) ----
# ---- AnkiDroid route 30 fix draft v2 (DRAFT ONLY, not merged) ----
# Target: SimpleMessageDialog.<init>, final-draw route 30, WRONG at step 5 only.
# This file supersedes the v1 draft in ../fragment.py + ../NOTES.md for
# route 30. The v1 files stay intact as the failed record; nothing here
# edits them, any graph file, tools/, .github/, or out/, and nothing
# here is merged or pushed. The turn lead alone merges, after a fresh
# independent re-audit.
#
# Fiction: printed step 5, S_DLG_DATABASE_ERROR -> DeckPicker.integrityCheck
# (Ea13b2167), entered on a failed-load prefix. The entered LOAD_FAILED
# dialog's buttons go only to ERROR_HANDLING or to exit(); the cited
# lines 294-302 are the different CONFIRM dialog's onPositive, never
# shown on that prefix. See NOTES.md for every printed source line.
#
# Mechanism (dialog-id-aware variant, A1 conventions from
# graphs/AnkiDroid/graph_def_mod/02.py): split the shared page by dialog
# id with a @CONFIRM suffix, and split its CONFIRM button callback the
# same way. Variant edges carry the dialog id as guard TEXT only; no
# env and no needs_state is set on any variant edge, so the variant
# chain keeps the same BFS cost as a shared chain. The suffix is
# stripped by the builder's base() when checking known nodes, so no new
# screen entry is needed for the @CONFIRM page, and the builder's
# first-variant rule counts the @CONFIRM callback node as the base
# callback method for labelling.
#
# What this file contains: three variant edges only (V01-V03 below),
# unchanged in substance from v1 (same sources, destinations, kinds,
# triggers, and guards; V03's evidence string is widened to the full
# source path form used by V01/V02, see NOTES.md).
# What this file deliberately does NOT contain:
#   - no edge-removal calls of any kind;
#   - no second definition of the graph-wide edge-rewriting function
#     (the single definition in graph_def.py is untouched; no separate
#     rewriting draft is needed for this fix, see NOTES.md);
#   - no new screen entry;
#   - no edge to the CHECK_MEDIA listener, and no edge that changes
#     the CHECK_DATABASE listener chain (integrityCheck ->
#     DeckPicker$15.onPostExecute is an existing edge, left untouched);
#   - no change to any ConfirmationDialog dispatch edge, and no change
#     to any other S_DLG_DATABASE_ERROR outgoing edge (LOAD_FAILED
#     buttons, ERROR_HANDLING list, REPAIR, RESTORE, NEW_COLLECTION,
#     RESTORE_CONFIRMATION, FULL_SYNC buttons all stay where they are).
#
# Merger actions required with this fragment (atomic, in NOTES.md):
# delete Ea13b2167; its connection survives ONLY as the callback hop
# V02+V03. Do NOT create a direct variant-page -> integrityCheck edge.
# The variant $9 edge V03 also covers the generic callback's automatic
# call to integrityCheck by the builder's hand-covering rule (a hand
# edge with the same base pair replaces the automatic edge), so after
# V03 the generic callback node has no call to integrityCheck left,
# even before its generic page edge is moved.
#
# EXPECTED PRINTED ROUTE after fragment + merger deletions (verified
# by this draft's own simulation in the builder's namespace, see
# NOTES.md section 2; it is NOT the 13-edge menu route):
#   S_ENTRY -> IntentHandler.onCreate -> DeckPicker.<init> ->
#   DeckPicker.onCreate -> DeckPicker.showStartupScreensAndDialogs ->
#   DeckPicker.integrityCheck -> DeckPicker$15.onPostExecute ->
#   AnkiActivity.showSimpleMessageDialog(String,boolean) ->
#   SimpleMessageDialog.newInstance(String,boolean) ->
#   SimpleMessageDialog.newInstance(String,String,boolean) ->
#   SimpleMessageDialog.<init>
# (10 edges, in BOTH allow_setup modes.) That route is branch-
# conditional twice over: the showStartupScreensAndDialogs ->
# integrityCheck hop runs only on a database version upgrade
# (DeckPicker.java:921, 928-929), and the onPostExecute ->
# showSimpleMessageDialog hop runs only on a successful database
# check (DeckPicker.java:1160, 1170; else handleDbError at :1172).
# The 13-edge menu route below is a genuine AVAILABLE VARIANT PATH,
# not the printed route, while the showStartup edge stands:
#   S_ENTRY -> IntentHandler.onCreate -> DeckPicker.<init> ->
#   DeckPicker.onCreate -> S_DECKPICKER (collection open) ->
#   DeckPicker.onOptionsItemSelected -> S_DLG_DATABASE_ERROR@CONFIRM
#   -> DatabaseErrorDialog$9.onPositive@CONFIRM ->
#   DeckPicker.integrityCheck -> DeckPicker$15.onPostExecute ->
#   AnkiActivity.showSimpleMessageDialog(String,boolean) ->
#   SimpleMessageDialog.newInstance(String,boolean) ->
#   SimpleMessageDialog.newInstance(String,String,boolean) ->
#   SimpleMessageDialog.<init>

# R30-V01: collection-open menu entry, CONFIRM dialog only.
# Menu case action_check_database calls showDatabaseErrorDialog with
# DIALOG_CONFIRM_DATABASE_CHECK; the helper builds that dialog type
# and shows it. This is the only entry edge to the variant page.
e('DeckPicker.onOptionsItemSelected', 'S_DLG_DATABASE_ERROR@CONFIRM', 'ENTERS',
  'the check-database menu item is tapped and the database dialog opens (id 6)',
  guard='item.getItemId() == R.id.action_check_database; showDatabaseErrorDialog(DIALOG_CONFIRM_DATABASE_CHECK)',
  evidence='SRC com/ichi2/anki/DeckPicker.java:595-598; SRC com/ichi2/anki/DeckPicker.java:1026-1028')

# R30-V02: variant page button, CONFIRM dialog only.
# The callback object $9 is created only in the CONFIRM case: case at
# :294, callback created at :299, onPositive at :301. Its trigger
# text copies the existing generic $9 page edge verbatim.
e('S_DLG_DATABASE_ERROR@CONFIRM', 'DatabaseErrorDialog$9.onPositive@CONFIRM', 'GUI',
  'tap OK on the database-check confirmation (integrityCheck)',
  gui=['tap OK on the database-check confirmation (integrityCheck)'],
  guard='dialog variant is DIALOG_CONFIRM_DATABASE_CHECK (id 6)',
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:294-302; SRC com/ichi2/anki/DeckPicker.java:595-598')

# R30-V03: variant callback body, CONFIRM dialog only.
# The onPositive body calls integrityCheck at line 302 (callback
# created at :299, onPositive at :301, dismiss at :303). This hand
# edge has the same base pair as the automatic call from the generic
# callback, so the builder's hand-covering rule replaces that
# automatic edge: the generic callback node no longer calls
# integrityCheck, and only the @CONFIRM callback node does.
e('DatabaseErrorDialog$9.onPositive@CONFIRM', 'DeckPicker.integrityCheck', 'CALL',
  'Direct call',
  guard='dialog variant is DIALOG_CONFIRM_DATABASE_CHECK (id 6); onPositive body calls integrityCheck',
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:299-303')

# ---- route 25 (B01/B02 guard wording corrected by merger, see notes) ----
# ---- AnkiDroid route 25 DRAFT ONLY (turn fix, route 25 only) ----
# Target: BaseAsyncTask.onProgressUpdate. Printed route verdict WRONG, fiction
# at step 5 (edge Ecfd88980): the shared page S_DLG_DATABASE_ERROR let a
# LOAD_FAILED entry exit through DatabaseErrorDialog$6.onSelection, the
# RESTORE_BACKUP single-choice callback, which is never shown on that prefix.
#
# DRAFT STATUS: this file is a draft for the turn lead alone to merge. It
# pushes nothing and edits no graph file. A separate auditor judges it.
#
# WHAT THIS FILE CONTAINS: variant edges only (e() and gui() calls), plus
# the four SCREENS entries for the new variant pages. It defines no EDIT,
# and it uses no suppression calls. If an EDIT change is ever needed for
# this route, it must be drafted as a separate EDIT-wrapper-draft.txt file,
# never inside this file, because an EDIT clause must be appended to
# graph_def.py AFTER the B6 wrapper.
#
# CONVENTIONS (from graph_def_mod/02.py, A1 variant work):
# - Variant edges carry the dialog-id condition as guard TEXT only.
#   env is never set on a variant edge and needs_state is never set on
#   one either, so variant chains keep the same BFS cost as the shared
#   chains and win or lose only on steps.
# - BFS ignores guard text. The dialog-id distinction is therefore
#   carried by the NODES themselves (variant pages plus split helper
#   nodes), not by the guards alone. A guard-only change to a shared
#   page edge would not block the fiction path.
# - Hand-covering (build_graph.py add_auto_edges): a hand edge whose
#   base (src, dst) pair matches an automatic call edge suppresses that
#   automatic edge. That is how the callback -> helper variant edges
#   below replace the shared automatic callback -> showDatabaseErrorDialog
#   edges, with no suppression call and no deletion of a genuine edge.
# - The tail from DatabaseErrorDialog$6.onSelection onward is NOT
#   duplicated here: the automatic edge $6.onSelection ->
#   DeckPicker.restoreFromBackup (DatabaseErrorDialog.java:257-259),
#   DeckPicker.restoreFromBackup -> importReplace (DeckPicker.java:1249),
#   and the DeckTask IMPORT_REPLACE variant chain already in
#   graph_def_mod/02.py (entry, body, progress chain) are all pre-existing
#   and genuine. This fragment only repairs the dialog prefix.
# - No edge in this file touches S_DLG_CONFIRMATION or any
#   *.confirm / *.cancel node. Those dispatch edges are untouched.
# - Anonymous-class numbers ($1, $3, $5, $6, $7, $10) are the graph's
#   callback labels inside DatabaseErrorDialog.onCreateDialog; the
#   dialog-id constants (DIALOG_LOAD_FAILED = 0, DIALOG_ERROR_HANDLING = 2,
#   DIALOG_RESTORE_BACKUP = 4, DIALOG_CONFIRM_RESTORE_BACKUP = 7) are a
#   different numbering and are cited separately in every guard.
#
# MERGER MOVE LIST (not in this file; the turn lead applies it):
# Adding these variant edges alone does NOT remove the fiction path,
# because the shared page edges in graph_def.py batch 041 and the shared
# ENTERS edges still exist. For the fiction to close, the lead must MOVE
# (delete from the shared page, not duplicate) the following shared edges
# to the variant counterparts written here, and retarget the LOAD_FAILED
# ENTERS edges to the variant page:
#   shared S_DLG_DATABASE_ERROR -> DatabaseErrorDialog$1.onPositive
#       -> R25-B01 (S_DLG_DATABASE_ERROR@LOAD_FAILED -> $1.onPositive)
#   shared S_DLG_DATABASE_ERROR -> DatabaseErrorDialog$1.onNegative
#       -> R25-B02 (S_DLG_DATABASE_ERROR@LOAD_FAILED -> $1.onNegative)
#   shared S_DLG_DATABASE_ERROR -> DatabaseErrorDialog$3.onSelection
#       -> R25-D01 (S_DLG_DATABASE_ERROR@ERROR_HANDLING -> $3.onSelection)
#   shared S_DLG_DATABASE_ERROR -> DatabaseErrorDialog$5.onPositive
#       -> R25-F01 (S_DLG_DATABASE_ERROR@RESTORE_BACKUP -> $5.onPositive)
#   shared S_DLG_DATABASE_ERROR -> DatabaseErrorDialog$6.onSelection
#       -> R25-F02 (S_DLG_DATABASE_ERROR@RESTORE_BACKUP -> $6.onSelection)
#   shared S_DLG_DATABASE_ERROR -> DatabaseErrorDialog$7.onNegative
#       -> R25-F03 (S_DLG_DATABASE_ERROR@RESTORE_BACKUP -> $7.onNegative)
#   shared S_DLG_DATABASE_ERROR -> DatabaseErrorDialog$10.onPositive
#       -> R25-E03 (S_DLG_DATABASE_ERROR@CONFIRM_RESTORE_BACKUP -> $10.onPositive)
#   shared DeckPicker.onCreate -> S_DLG_DATABASE_ERROR (LOAD_FAILED/CURSOR
#       branch only) -> R25-A01; shared DeckPicker.handleDbError ->
#       S_DLG_DATABASE_ERROR -> R25-A02; shared
#       DeckPicker.onCollectionLoadError -> S_DLG_DATABASE_ERROR ->
#       R25-A03; shared DeckPicker.onOptionsItemSelected ->
#       S_DLG_DATABASE_ERROR (ids 6 and 7) is replaced by the split
#       helper chains R25-E01/R25-E02 (id 7, this route) and the route-24
#       counterpart (id 6, owned by the route-24 draft, not written here).
# Until that move list is applied, the shared page still offers $6 to a
# LOAD_FAILED entry and the printed fiction survives alongside this
# genuine variant chain. The auditor should judge this fragment as the
# replacement chain, and judge the move list as a separate merger step.
# The shared page's remaining callbacks (repair $4, new-collection $8,
# confirm-check $9, full-sync $11) are owned by sibling drafts (routes
# 24, 27, 30) and are deliberately not moved by this route-25 fragment.

# ---- Variant pages (SCREENS entries; the merger may instead place these
# four lines in the SCREENS dict of graph_def.py with identical text) ----
# Variant-page descriptions (NOT SCREENS entries: the builder's page check
# compares base(node) against SCREENS keys, so an '@'-suffixed key can
# never match and always errors; variant pages validate via their base
# page, as @CONFIRM already does with no SCREENS entry at all):
# S_DLG_DATABASE_ERROR@LOAD_FAILED = 'DatabaseErrorDialog type 0 (DIALOG_LOAD_FAILED): collection failed to load, error-handling options or close only'
# S_DLG_DATABASE_ERROR@ERROR_HANDLING = 'DatabaseErrorDialog type 2 (DIALOG_ERROR_HANDLING): repair-option list'
# S_DLG_DATABASE_ERROR@RESTORE_BACKUP = 'DatabaseErrorDialog type 4 (DIALOG_RESTORE_BACKUP): restore one backup, or back to the error-handling list when no backup exists'
# S_DLG_DATABASE_ERROR@CONFIRM_RESTORE_BACKUP = 'DatabaseErrorDialog type 7 (DIALOG_CONFIRM_RESTORE_BACKUP): confirm restoring from a backup'

# ======================================================================
# A. LOAD_FAILED entries (ENTERS): the only dialog this prefix shows.
# DeckPicker.onCreate shows id 0 only on the else branch after the
# storage, mount, and directory checks pass and the cursor-size check
# fails (DeckPicker.java:418, 430-433); the id-9 cursor branch at :431
# shares the $1 callback block and is NOT given a variant page here,
# because it is outside route 25's prefix (see NOTES.md).
# ======================================================================

# R25-A01: onCreate -> LOAD_FAILED variant page.
e('DeckPicker.onCreate', 'S_DLG_DATABASE_ERROR@LOAD_FAILED', 'ENTERS',
  'the collection is not open and the storage checks pass: the load-failed dialog (id 0) is shown',
  guard='dialog id == DIALOG_LOAD_FAILED (0), passed through showDatabaseErrorDialog',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:418, 430-433; SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:27-36')

# R25-A02: handleDbError -> LOAD_FAILED variant page.
e('DeckPicker.handleDbError', 'S_DLG_DATABASE_ERROR@LOAD_FAILED', 'ENTERS',
  'a database error result is reported and the load-failed dialog opens',
  guard='dialog id == DIALOG_LOAD_FAILED (0), passed through showDatabaseErrorDialog',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1243-1245')

# R25-A03: onCollectionLoadError -> LOAD_FAILED variant page (indirect
# through the DialogHandler message, as in the existing shared edge).
e('DeckPicker.onCollectionLoadError', 'S_DLG_DATABASE_ERROR@LOAD_FAILED', 'ENTERS',
  'the collection load error is reported and the load-failed dialog opens through DialogHandler (indirect)',
  guard='dialog id == DIALOG_LOAD_FAILED (0), passed through showDatabaseErrorDialog',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:835-837; SRC com/ichi2/anki/dialogs/DialogHandler.java:58-60')

# ======================================================================
# B. LOAD_FAILED callbacks (GUI): exactly two, and neither is $6.
# The LOAD_FAILED / CURSOR block (DatabaseErrorDialog.java:73-94) builds
# one dialog with a positive button (error-handling options) and a
# negative button (close). There is no restore button on this dialog.
# ======================================================================

# R25-B01: LOAD_FAILED positive -> ERROR_HANDLING (via the split helper).
gui('S_DLG_DATABASE_ERROR@LOAD_FAILED', 'DatabaseErrorDialog$1.onPositive',
    'tap error handling options on the load-failed dialog',
    guard='dialog id == DIALOG_LOAD_FAILED (0); this callback exists only on the load-failed dialog',
    evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:80-87')

# R25-B02: LOAD_FAILED negative -> close (DeckPicker.exit, automatic
# call from the callback body at DatabaseErrorDialog.java:90-92).
gui('S_DLG_DATABASE_ERROR@LOAD_FAILED', 'DatabaseErrorDialog$1.onNegative',
    'tap close on the load-failed dialog (DeckPicker.exit)',
    guard='dialog id == DIALOG_LOAD_FAILED (0); this callback exists only on the load-failed dialog',
    evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:89-92')

# ======================================================================
# C. Dialog-to-dialog transitions through split helper nodes.
# DeckPicker.showDatabaseErrorDialog(int) (DeckPicker.java:1026-1028)
# builds DatabaseErrorDialog.newInstance(id) and shows it, so the id
# argument selects the dialog. Splitting the helper by id is what keeps
# one dialog instance from bridging to another dialog's callbacks: the
# shared helper node has no page edge in the current graph, and a single
# shared helper node must never be given edges to every variant page.
# Each transition below is therefore a CALL to a split helper node plus
# an ENTERS edge from that node to exactly one variant page.
# ======================================================================

# R25-C01: $1.onPositive calls the helper with id 2.
e('DatabaseErrorDialog$1.onPositive', 'DeckPicker.showDatabaseErrorDialog@ERROR_HANDLING', 'CALL', 'Direct call',
  guard='dialog id == DIALOG_ERROR_HANDLING (2), passed through',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:84-87')

# R25-C02: split helper (id 2) shows the ERROR_HANDLING variant page.
e('DeckPicker.showDatabaseErrorDialog@ERROR_HANDLING', 'S_DLG_DATABASE_ERROR@ERROR_HANDLING', 'ENTERS',
  'the error-handling list dialog is requested: the repair-option list opens',
  guard='dialog id == DIALOG_ERROR_HANDLING (2), passed through',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1026-1028; SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:47-53, 57-59, 129')

# R25-C03: $3.onSelection, restore branch only, calls the helper
# with id 4. The list callback handles values 0-5 in one switch
# (DatabaseErrorDialog.java:172-195); only value 3 (restore) takes
# this edge. The other values' helper edges belong to sibling drafts
# and must be added by them (see NOTES.md); this edge alone does not
# claim $3 only ever picks restore.
e('DatabaseErrorDialog$3.onSelection', 'DeckPicker.showDatabaseErrorDialog@RESTORE_BACKUP', 'CALL', 'Direct call',
  guard='user picks restore, mRepairValues[which] == 3, always offered; dialog id == DIALOG_RESTORE_BACKUP (4), passed through',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:149-150, 170-172, 184-187')

# R25-C04: split helper (id 4) shows the RESTORE_BACKUP variant page.
e('DeckPicker.showDatabaseErrorDialog@RESTORE_BACKUP', 'S_DLG_DATABASE_ERROR@RESTORE_BACKUP', 'ENTERS',
  'the restore-backup dialog is requested: the backup list (or the no-backup notice) opens',
  guard='dialog id == DIALOG_RESTORE_BACKUP (4), passed through',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1026-1028; SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:47-53, 57-59, 216')

# R25-C05: $5.onPositive (no-backup branch) calls the helper with id 2,
# returning to the ERROR_HANDLING list. This reuses the R25-C02 helper
# node; it is a different source edge, not a duplicate of R25-C01.
e('DatabaseErrorDialog$5.onPositive', 'DeckPicker.showDatabaseErrorDialog@ERROR_HANDLING', 'CALL', 'Direct call',
  guard='dialog id == DIALOG_ERROR_HANDLING (2), passed through; taken only when the backup list is empty',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:224-233')

# R25-C06: $10.onPositive (confirm-restore) calls the helper with id 4.
# This reuses the R25-C04 helper node and page; it is the menu
# alternative's second hop (see section E).
e('DatabaseErrorDialog$10.onPositive', 'DeckPicker.showDatabaseErrorDialog@RESTORE_BACKUP', 'CALL', 'Direct call',
  guard='dialog id == DIALOG_RESTORE_BACKUP (4), passed through',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:315-318')

# ======================================================================
# D. ERROR_HANDLING callback (GUI): the single list callback.
# The list is built at DatabaseErrorDialog.java:129-162. Restore
# (value 3) is added unconditionally at :149-150, unlike check_db
# (value 1, only when the collection is open, :134-141) and repair
# (value 2, only when sqlite3 is installed, :144-147). That is why the
# restore branch is available on the failed-load prefix even though
# the check_db branch is not: the contradiction that blocks route 24's
# ERROR_HANDLING path does not block route 25's.
# ======================================================================

# R25-D01: ERROR_HANDLING list -> $3.onSelection.
gui('S_DLG_DATABASE_ERROR@ERROR_HANDLING', 'DatabaseErrorDialog$3.onSelection',
    'pick one repair option in the error handling list',
    guard='dialog id == DIALOG_ERROR_HANDLING (2); route 25 takes the restore branch, mRepairValues[which] == 3',
    evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:134-156, 168-196')

# ======================================================================
# E. Menu alternative (collection open): action_restore_backup.
# The deck-list page already offers DeckPicker.onOptionsItemSelected
# (gui edge S_DECKPICKER -> onOptionsItemSelected in graph_def.py).
# The menu case at DeckPicker.java:617-619 calls the helper with id 7.
# This section is the alternative prefix; it joins the main chain at
# R25-C04 / R25-C06, so no second copy of the RESTORE page is needed.
# ======================================================================

# R25-E01: menu item -> split helper (id 7).
e('DeckPicker.onOptionsItemSelected', 'DeckPicker.showDatabaseErrorDialog@CONFIRM_RESTORE_BACKUP', 'CALL', 'Direct call',
  guard='menu item == R.id.action_restore_backup; dialog id == DIALOG_CONFIRM_RESTORE_BACKUP (7), passed through',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:617-619')

# R25-E02: split helper (id 7) shows the CONFIRM_RESTORE_BACKUP page.
e('DeckPicker.showDatabaseErrorDialog@CONFIRM_RESTORE_BACKUP', 'S_DLG_DATABASE_ERROR@CONFIRM_RESTORE_BACKUP', 'ENTERS',
  'the restore-backup confirmation dialog is requested: the confirmation dialog opens',
  guard='dialog id == DIALOG_CONFIRM_RESTORE_BACKUP (7), passed through',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1026-1028; SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:47-53, 57-59, 308')

# R25-E03: CONFIRM_RESTORE_BACKUP positive -> restore dialog (via R25-C06).
gui('S_DLG_DATABASE_ERROR@CONFIRM_RESTORE_BACKUP', 'DatabaseErrorDialog$10.onPositive',
    'tap continue on the restore confirmation (the restore dialog for id 4 follows)',
    guard='dialog id == DIALOG_CONFIRM_RESTORE_BACKUP (7); this callback exists only on the confirmation dialog',
    evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:313-318')

# ======================================================================
# F. RESTORE_BACKUP callbacks (GUI): the three callbacks of the id-4
# dialog. The dialog builds its backup list from
# BackupManager.getBackups at DatabaseErrorDialog.java:218-222. When
# the list is empty it shows an OK button ($5); when it is non-empty
# it shows a date list with single-choice selection ($6) and a cancel
# button ($7, dismiss only, no onward route for this target).
# ======================================================================

# R25-F01: no-backup OK -> back to ERROR_HANDLING (via R25-C05).
gui('S_DLG_DATABASE_ERROR@RESTORE_BACKUP', 'DatabaseErrorDialog$5.onPositive',
    'tap OK on the no-backup restore dialog (back to the error handling list)',
    guard='dialog id == DIALOG_RESTORE_BACKUP (4); taken only when mBackups.length == 0',
    evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:224-234; SRC com/ichi2/anki/BackupManager.java:311-326')

# R25-F02: backup selection -> restoreFromBackup (automatic call at
# DatabaseErrorDialog.java:257-259, not duplicated in this fragment).
# This is the edge the printed fiction misused: on the variant graph
# it is reachable only from the RESTORE_BACKUP page, never from the
# LOAD_FAILED page.
gui('S_DLG_DATABASE_ERROR@RESTORE_BACKUP', 'DatabaseErrorDialog$6.onSelection',
    'pick a backup date in the restore list (restoreFromBackup)',
    guard='dialog id == DIALOG_RESTORE_BACKUP (4); taken only when the backup list is non-empty and the chosen backup has length > 0',
    evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:251-270; SRC com/ichi2/anki/BackupManager.java:311-326')

# R25-F03: restore-list cancel -> dismiss only (terminal for this route).
gui('S_DLG_DATABASE_ERROR@RESTORE_BACKUP', 'DatabaseErrorDialog$7.onNegative',
    'tap cancel on the restore list (dismiss only)',
    guard='dialog id == DIALOG_RESTORE_BACKUP (4); taken only when the backup list is non-empty',
    evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:243-248')

# ---- End of route-25 draft fragment: 18 variant edges (A 3, B 2,
# C 6, D 1, E 3, F 3) plus 4 SCREENS entries. No EDIT, no suppression
# call, no tail edge, no S_DLG_CONFIRMATION edge. ----

# ---- route 27 v4 (v1/v2/v3 never merged) ----
# ---- AnkiDroid route 27 v4 DRAFT ONLY (turn fix, route 27 only; NOT merged) ----
# Redesign after the FAIL re-audit of v3 (turn/audit/route_27/AUDIT4.md).
# The v1 files (turn/fix/route_27/fragment.py, NOTES.md), the v2 files
# (turn/fix/route_27/v2/fragment.py, NOTES.md), and the v3 files
# (turn/fix/route_27/v3/fragment.py, NOTES.md) stay intact as the failed
# record; nothing here edits them, any graph file, tools/, .github/, or
# out/, and nothing here is pushed. The turn lead alone merges; a fresh
# independent re-audit judges this draft.
#
# APPLY V4 ONLY. Never apply v1, v2, or v3 alongside v4. V4 contains
# v3's 12 edges in full (the 10 v2 edges plus V09/V10) plus the 35
# sync-resolution split edges in the final section below; applying v3
# as well would duplicate those 12 pairs as parallel edges with
# differing guard/evidence text (the builder does not dedupe same-pair
# edges) and applying v1 as well would reintroduce v1's wrong
# BackupManager 243 guard text on V07. The same hazard applies to any
# stacking of drafts: one route-27 fragment per merge, and that
# fragment is v4.
#
# Problem (judged WRONG, final-draw route 27, step 5, edge Ee8da2b4f): the
# printed route jumps from the shared page S_DLG_DATABASE_ERROR straight to
# DatabaseErrorDialog$4.onPositive. That callback belongs to the
# DIALOG_REPAIR_COLLECTION dialog (DatabaseErrorDialog.java:201-214), but the
# dialog actually entered on the printed prefix is DIALOG_LOAD_FAILED
# (DeckPicker.java:433), whose only buttons go to DIALOG_ERROR_HANDLING or
# to exit() (DatabaseErrorDialog.java:73-94). The shared page lets BFS jump
# dialog ids; these variant pages stop that jump for route 27 by carrying
# the dialog id in the page node itself.
#
# Why v2 failed, and what v3 changes (BFS follows node identity, NOT guard
# text, so separation must be carried by node topology, not guards):
# - V2 added 10 genuine variant edges and, with merger moves M1-M5, closed
#   the $4 gate (shortest path to $4.onPositive = the corrected chain
#   itself, 9 edges to $4 + 5 tail = 14 to close()). But v2's section 8
#   competition table was false on two dispatches that reach
#   Collection.close() WITHOUT $4, so they escape the $4 gate entirely:
#   (a) the $6 fiction: generic page -> $6.onSelection ->
#   restoreFromBackup -> importReplace -> @IMPORT_REPLACE ->
#   doInBackgroundImportReplace -> close() (10 edges, DeckTask.java:805
#   tmpCol.close(); v2's claim that the $6 chain "ends at
#   onProgressUpdate, not close()" is false at method level).
#   (b) the $11 fiction: generic page -> $11.onPositive (id-8 FULL_SYNC
#   dialog, call at DatabaseErrorDialog.java:330) -> sync("download") ->
#   ... -> FullSyncer.download -> close() (12 edges; v2's claim that $11
#   "neither reaches close()" is false: $11 -> close() in 7 built edges,
#   and sync("download") genuinely satisfies the download branch).
# - V3 therefore adds the $11 disposition v2 lacked: a new id-8 variant
#   page (S_DLG_DATABASE_ERROR_FULL_SYNC) with a re-provided $11 dispatch
#   (V10), entered genuinely from the ERROR_HANDLING list via value 4
#   (V09, DatabaseErrorDialog.java:188-191; value 4 is offered
#   unconditionally at :151-153), plus merger move M11 (delete the
#   generic $11 dispatch, graph_def.py:5570-5574). After M11, $11's only
#   incoming is V10, and the shortest genuine $11 path to close() is
#   16 edges (see NOTES.md section 8), which loses to the 14-edge
#   corrected chain honestly instead of beating it as a fiction.
# - The $6 disposition is NOT a v3 edge: in the combined merge, route 25
#   moves generic $6 to its @RESTORE_BACKUP page (route-25 F02), so $6's
#   only incoming becomes the genuine restore-list dispatch and its
#   shortest path to close() is the genuine 16-edge restore chain (see
#   NOTES.md section 8). V3's standalone claim is corrected accordingly:
#   v3 + M1-M5 + M11 alone is NOT a merge candidate, because the $6
#   fiction at 10 edges still prints without route 25's $6 move; the
#   merge candidate is the combined batch (v3 + route 25 + routes 24/30),
#   in which the $6 fiction is already gone. V3 must land in-batch with
#   route 25's $6 move (and with route 25's F01, for the section 10
#   label condition).
# - The 12-edge onResume sync path is method-level real but branch-false
#   (see NOTES.md section 8): sync() passes null, and the null branch
#   takes client.sync(), not FullSyncer.download. It is excluded from
#   the genuine competition on that branch analysis, not by any edge
#   deletion; the simulation in NOTES.md section 8 reports it plainly
#   as the method-level cheapest print, so the lead and the re-audit
#   can see exactly what a method-level rebuild would print and why
#   the 14-edge chain is nevertheless the cheapest branch-genuine path.
#
# Variant pages (same three keys as v1/v2, plus one new id-8 key):
#   S_DLG_DATABASE_ERROR_LOAD_FAILED (id 0)
#   S_DLG_DATABASE_ERROR_ERROR_HANDLING (id 2)
#   S_DLG_DATABASE_ERROR_REPAIR (id 3)
#   S_DLG_DATABASE_ERROR_FULL_SYNC (id 8, NEW in v3)
# The tail from DeckPicker.repairDeck onward already exists (the DeckTask
# variant edges in graph_def_mod/02.py plus the auto call edges) and is
# NOT duplicated here. Likewise the $4.onPositive -> repairDeck call edge
# (DatabaseErrorDialog.java:210) and the $11.onPositive -> sync(String)
# call edge (DatabaseErrorDialog.java:330) already exist and are NOT
# duplicated here.
#
# Conventions followed (graph_def_mod/02.py header and the A1 variant
# technique): variant edges carry the dialog-id condition as guard TEXT
# only; env and needs_state are never set on a variant edge, so variant
# chains keep the same BFS cost as shared chains and win only on
# steps/node sequence. Entry edges use plain SRC, never a bytecode
# citation. This file adds edges only: it removes, retargets, or rewrites
# nothing by itself, and it defines no chained rewrite clause (see
# NOTES.md section 11 for why none is needed: every (src, dst) pair below
# is new). The single chained rewrite clause in graph_def.py is untouched.
# No edge here touches S_DLG_CONFIRMATION or any confirm/cancel dispatch
# edge. Placement for the merger: these lines run in the graph_def.py
# namespace (e() and SCREENS are already defined there), as in
# graph_def_mod/02.py. The SCREENS lines may instead be moved into the
# SCREENS dict in graph_def.py; either placement gives the same nodes.
# The fragment alone does NOT change the printed route: until the merger
# applies moves M1-M5 + M11 in NOTES.md (and the sibling moves listed
# there), the generic edges still exist and BFS still prints a fiction.
# Judge this draft together with that move list.
#
# SCREENS entries for the four variant pages.
SCREENS['S_DLG_DATABASE_ERROR_LOAD_FAILED'] = 'DatabaseErrorDialog type 0 (DIALOG_LOAD_FAILED): collection failed to load; buttons only to error handling or exit'
SCREENS['S_DLG_DATABASE_ERROR_ERROR_HANDLING'] = 'DatabaseErrorDialog type 2 (DIALOG_ERROR_HANDLING): repair-option list, reached from the load-failed dialog positive button'
SCREENS['S_DLG_DATABASE_ERROR_REPAIR'] = 'DatabaseErrorDialog type 3 (DIALOG_REPAIR_COLLECTION): repair confirmation, reached by picking repair (value 2) in the error-handling list'
SCREENS['S_DLG_DATABASE_ERROR_FULL_SYNC'] = 'DatabaseErrorDialog type 8 (DIALOG_FULL_SYNC_FROM_SERVER): full-sync-from-server confirmation, reached by picking full sync (value 4) in the error-handling list'

# 27-V01: variant entry, onCreate final else branch (id 0). The sibling
# branch at :430-431 shows id 9 (CURSOR_SIZE_LIMIT_EXCEEDED), which shares
# the $1 callback block but gets NO variant page here (see NOTES.md
# section 9, lead decision L1); this edge is the id-0 branch only.
e('DeckPicker.onCreate', 'S_DLG_DATABASE_ERROR_LOAD_FAILED', 'ENTERS',
  'the collection is not open and the storage checks pass: the load-failed dialog (id 0) is shown',
  guard='dialogType == DIALOG_LOAD_FAILED (0), DeckPicker.java:432-433 final else branch (not the cursor-size branch at :430-431)',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:418, 430-433; SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:27-36')

# 27-V01b: variant entry, handleDbError (id 0 only). This method's only
# action is showing the load-failed dialog, so its variant entry is exact.
e('DeckPicker.handleDbError', 'S_DLG_DATABASE_ERROR_LOAD_FAILED', 'ENTERS',
  'a database error result is reported and the load-failed dialog opens',
  guard='dialogType == DIALOG_LOAD_FAILED (0), passed through showDatabaseErrorDialog',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1243-1245')

# 27-V01c: variant entry, onCollectionLoadError (id 0 only, indirect
# through the DialogHandler message, as in the existing shared edge).
e('DeckPicker.onCollectionLoadError', 'S_DLG_DATABASE_ERROR_LOAD_FAILED', 'ENTERS',
  'the collection load error is reported and the load-failed dialog opens through DialogHandler (indirect)',
  guard='dialogType == DIALOG_LOAD_FAILED (0), passed through showDatabaseErrorDialog',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:835-837; SRC com/ichi2/anki/dialogs/DialogHandler.java:58-60')

# 27-V02: LOAD_FAILED dispatch, positive button only to ERROR_HANDLING.
# The DIALOG_CURSOR_SIZE_LIMIT_EXCEEDED case falls through to this same
# case block, so the same dialog (and the same two buttons) is shown for
# id 9 as for id 0; route 27 enters with id 0.
e('S_DLG_DATABASE_ERROR_LOAD_FAILED', 'DatabaseErrorDialog$1.onPositive', 'GUI',
  'tap error handling options on the load-failed dialog',
  gui=['tap error handling options on the load-failed dialog'],
  guard='dialogType == DIALOG_LOAD_FAILED (0)',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:80-87')

# 27-V03: LOAD_FAILED dispatch, negative button only to exit. This is the
# second and last real button of the entered dialog; no repair button
# exists on this page, which is exactly what the printed step 5 got wrong.
e('S_DLG_DATABASE_ERROR_LOAD_FAILED', 'DatabaseErrorDialog$1.onNegative', 'GUI',
  'tap close on the load-failed dialog (DeckPicker.exit)',
  gui=['tap close on the load-failed dialog (DeckPicker.exit)'],
  guard='dialogType == DIALOG_LOAD_FAILED (0)',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:89-92')

# 27-V04: bridge from the LOAD_FAILED positive button to the
# ERROR_HANDLING variant page. The callback calls
# showDatabaseErrorDialog(DIALOG_ERROR_HANDLING); that helper builds the
# dialog with DatabaseErrorDialog.newInstance(id) and shows it
# (DeckPicker.java:1026-1028), so the next page shown is the
# ERROR_HANDLING dialog, not a return to the shared page. Kind ENTERS
# follows the existing callback -> page edges (for example
# ModelFieldEditor$2.onPositive -> S_DLG_CONFIRMATION in graph_def.py).
# This is the first of the two genuine ERROR_HANDLING entries (the other
# is V08); see NOTES.md section 4 for the exhaustive entry census.
e('DatabaseErrorDialog$1.onPositive', 'S_DLG_DATABASE_ERROR_ERROR_HANDLING', 'ENTERS',
  'the load-failed positive button asks for the error-handling dialog',
  guard='dialogType == DIALOG_ERROR_HANDLING (2), requested by DatabaseErrorDialog.java:85-86',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:85-86; SRC com/ichi2/anki/DeckPicker.java:1026-1028')

# 27-V08: bridge from the no-backup restore OK button to the
# ERROR_HANDLING variant page. The RESTORE_BACKUP dialog builds its backup
# list from BackupManager.getBackups (:218-222); when the list is empty it
# shows an OK button whose onPositive calls
# showDatabaseErrorDialog(DIALOG_ERROR_HANDLING) (:230-232). This is the
# second genuine ERROR_HANDLING entry, and the one v1 missed: without it,
# the no-backup return has no variant landing, and with it but without
# merger move M5, the generic page -> $5 -> this bridge path would tie
# the corrected chain at 14 edges. V08's source is the method node
# $5.onPositive, so it fires from whichever page dispatches $5 after the
# merger moves (route 25's RESTORE variant, once it lands); it adds no
# page dispatch to $5 itself, which stays route 25's edge to write.
e('DatabaseErrorDialog$5.onPositive', 'S_DLG_DATABASE_ERROR_ERROR_HANDLING', 'ENTERS',
  'the no-backup restore OK button asks for the error-handling dialog',
  guard='dialogType == DIALOG_ERROR_HANDLING (2), requested by DatabaseErrorDialog.java:231-232; taken only when the backup list is empty (mBackups.length == 0, :224)',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:224-234; SRC com/ichi2/anki/DeckPicker.java:1026-1028')

# 27-V05: ERROR_HANDLING dispatch, repair pick only. Value 2 is offered
# only when sqlite3 runs (the sqliteInstalled check); the other list
# values belong to other routes and are NOT drafted here (route 25 needs
# value 3, restore; routes 24/30 need value 1, check database, which v3
# deliberately does NOT bridge for the collection-open reason in NOTES.md
# section 9; value 4, full sync, is drafted here as V09; values 0 and 5
# have no route-27 owner).
e('S_DLG_DATABASE_ERROR_ERROR_HANDLING', 'DatabaseErrorDialog$3.onSelection', 'GUI',
  'pick repair in the error handling list',
  gui=['pick repair in the error handling list'],
  guard='selected value == 2 (repair), offered only when sqlite3 is installed (DatabaseErrorDialog.java:65-70, 144-147)',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:144-147, 180-183')

# 27-V06: bridge from the repair pick to the REPAIR variant page. The
# case-2 branch calls showDatabaseErrorDialog(DIALOG_REPAIR_COLLECTION),
# so the next page shown is the repair confirmation dialog. Note the
# source of this edge is the SHARED method node $3.onSelection: it is
# safe only because merger move M2 removes the generic page -> $3 edge,
# so $3 is reachable only from variant ERROR_HANDLING pages after the
# moves (see NOTES.md section 7).
e('DatabaseErrorDialog$3.onSelection', 'S_DLG_DATABASE_ERROR_REPAIR', 'ENTERS',
  'the repair pick asks for the repair-collection dialog',
  guard='dialogType == DIALOG_REPAIR_COLLECTION (3), requested by DatabaseErrorDialog.java:180-183',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:180-183; SRC com/ichi2/anki/DeckPicker.java:1026-1028')

# 27-V07: REPAIR dispatch, positive button to repairDeck. The call edge
# $4.onPositive -> DeckPicker.repairDeck already exists in the graph
# (DatabaseErrorDialog.java:210) and is reused, not rewritten here.
# The repair chain reaches Collection.close() only with a non-null
# collection: repairCollection dereferences col.getPath() at
# BackupManager.java:242 BEFORE the null-checked col.close() at :245
# (line 243 is only `File deckFile = new File(deckPath);`), so a null
# collection throws before close() is reached. This corrects v1's
# off-by-one citation (v1 said 243 for the dereference).
e('S_DLG_DATABASE_ERROR_REPAIR', 'DatabaseErrorDialog$4.onPositive', 'GUI',
  'tap repair on the repair dialog (repairDeck)',
  gui=['tap repair on the repair dialog (repairDeck)'],
  guard='dialogType == DIALOG_REPAIR_COLLECTION (3); collection non-null so BackupManager.repairCollection reaches col.close() (BackupManager.java:242-245)',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:207-212')

# 27-V09: bridge from the full-sync pick to the FULL_SYNC variant page.
# NEW in v3; this is the $11 disposition's genuine entry. The
# ERROR_HANDLING list offers value 4 (full sync from server)
# unconditionally (DatabaseErrorDialog.java:151-153, outside both the
# colIsOpen branch at :134-141 and the sqlite3 branch at :144-147), and
# the case-4 branch calls
# showDatabaseErrorDialog(DIALOG_FULL_SYNC_FROM_SERVER) (:188-191), so
# the next page shown is the full-sync confirmation dialog. Note the
# source of this edge is the SHARED method node $3.onSelection: it is
# safe for exactly the same reason as V06 (merger move M2 removes the
# generic page -> $3 edge, so $3 is reachable only from variant
# ERROR_HANDLING pages after the moves), and value 4, unlike value 1,
# has no collection-state gate, so the LOAD_FAILED -> ERROR_HANDLING ->
# FULL_SYNC path is genuinely available on the failed-load prefix.
# The DialogHandler force-full-sync message (DialogHandler.java:88-96)
# is NOT an entry to this page: it shows a ConfirmationDialog, a
# different dialog class, not a DatabaseErrorDialog of id 8.
e('DatabaseErrorDialog$3.onSelection', 'S_DLG_DATABASE_ERROR_FULL_SYNC', 'ENTERS',
  'the full-sync pick asks for the full-sync-from-server dialog',
  guard='dialogType == DIALOG_FULL_SYNC_FROM_SERVER (8), requested by DatabaseErrorDialog.java:188-191; value 4 offered unconditionally (:151-153)',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:151-153, 188-191; SRC com/ichi2/anki/DeckPicker.java:1026-1028')

# 27-V10: FULL_SYNC dispatch, positive button to sync("download"). The
# call edge $11.onPositive -> DeckPicker.sync(String) already exists in
# the graph (DatabaseErrorDialog.java:330) and is reused, not rewritten
# here. This is the re-provided dispatch that merger move M11 moves off
# the shared page: after M11, $11's only incoming edge is this one, so
# $11 stays reachable (no label flip) while the dialog-id fiction
# (generic page -> $11 from a LOAD_FAILED entry) is gone. The sync tail
# from here is genuine: sync("download") satisfies the download branch
# (Connection.java:334-337 -> FullSyncer.download -> mCol.close() at
# FullSyncer.java:94), and the full V09+V10 path to close() is 16 edges
# (see NOTES.md section 8), which loses to the 14-edge corrected chain.
e('S_DLG_DATABASE_ERROR_FULL_SYNC', 'DatabaseErrorDialog$11.onPositive', 'GUI',
  'tap overwrite on the full-sync confirmation (sync download)',
  gui=['tap overwrite on the full-sync confirmation (sync download)'],
  guard='dialogType == DIALOG_FULL_SYNC_FROM_SERVER (8)',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:322-334')

# ---- Sync-resolution split (NEW in v4; this is the AUDIT4 remedy item 1) ----
# Why v3 failed, in one paragraph: v3's dialog split is complete, but a
# method-level rebuild still prints the 12-edge onResume sync path, and
# AUDIT4 confirms from source that that print is branch-false: sync()
# hardcodes null (DeckPicker.java:1266-1267), sync(String) passes its
# argument straight through into the Connection payload
# (DeckPicker.java:1284-1286), and doInBackgroundSync takes client.sync()
# on null (Connection.java:284-288) and FullSyncer.download only on
# non-null "download" (Connection.java:318, :334-337). No dialog move
# changes the argument sync() passes, so the fix must split the sync
# chain itself by the resolution argument, exactly as route 20 splits
# the Note 3-arg constructor by argument null-ness (@id-null vs @id-set
# variant nodes in graph_def). The mechanism is the same A1 variant
# mechanism, and it needs no builder change: variant nodes keyed by
# resolution, with the null chain and the download chain separated so
# BFS cannot walk from a null call site to FullSyncer.download.
#
# Resolution values, exhaustively, from every caller of
# DeckPicker.sync(String) in the source root (built-graph incoming
# census agrees: exactly 7 callers):
#   null: DeckPicker.sync() only (DeckPicker.java:1267, sync(null)).
#     Every sync() caller (onResume :705, automaticSync :769, menu :558,
#     DialogHandler :105, SyncErrorDialog$2 retry :94, S_DECKPICKER GUI)
#     reaches the null variant through this one retarget, so none of
#     them needs its own edge.
#   "download": DatabaseErrorDialog$11.onPositive (:330, v3 V10's tail),
#     DeckPicker$17.onPostExecute (:1452, fullSync + empty-collection
#     branch; Syncer.sync returns "fullSync" at Syncer.java:137), and
#     SyncErrorDialog$5 (:153, keep-remote confirm) and $8 (:199,
#     sanity keep-remote confirm).
#   "upload": SyncErrorDialog$4 (:139, keep-local confirm) and $7 (:186,
#     sanity keep-local confirm). The upload branch ends at col.reopen()
#     (Connection.java:322), never close(), so the upload chain needs
#     its own variant (so its tasks do not leak into the download
#     chain) but no download edge.
# No other caller exists: Connection.sync is called only by
# DeckPicker.sync(String) (built-graph incoming census: one caller),
# and FullSyncer.download is called only by doInBackgroundSync
# (Connection.java:337; built-graph incoming census: one caller).
#
# How the split is carried through the chain (four hops per variant,
# no helper hop added, so every genuine chain keeps its step count):
#   DeckPicker.sync(String)@sync-R -> Connection.sync@sync-R
#   Connection.sync@sync-R -> Connection.doInBackground@SYNC-R
#   Connection.doInBackground@SYNC-R -> Connection.doOneInBackground@SYNC-R
#   Connection.doOneInBackground@SYNC-R -> Connection.doInBackgroundSync@sync-R
# with R in {null, download, upload}. Variant edges carry the
# resolution condition as guard TEXT only, env None, no needs_state
# parameter, exactly as the dialog variant edges above. The body
# branch edges are hand-covered per branch, not left to variant-copy
# (variant-copy would give every variant every branch's edge, which
# is exactly the error that produced the 13-edge null -> upload ->
# beforeUpload -> close() path in the first simulation of this
# draft): null-only edges (Syncer.sync, getSyncMsg, modSchemaNoCheck,
# save) go to the null body variant only; FullSyncer construction
# and reopen go to the download and upload body variants only;
# FullSyncer.upload goes to the upload body variant only; and
# FullSyncer.download goes to the download body variant only. So no
# null or upload prefix can reach FullSyncer.download at all, and no
# null or download prefix can reach FullSyncer.upload (whose
# beforeUpload calls close() at Collection.java:411) either.
# Branch-independent body edges (pre-branch setup, post-branch media
# sync, exception handling, the finally close(boolean) — a different
# node from the close() target) are left to variant-copy, which gives
# them to all three variants alike; none of their subtrees reaches
# Collection.close() (verified by search in NOTES.md section 8).
#
# Why the shared chain does not leak around the split (builder rules,
# build_graph.py add_auto_edges, lines 205-228):
# - Hand-covering: a hand edge whose base (src, dst) pair matches an
#   automatic call edge suppresses that automatic edge for every
#   variant copy. Each retarget below therefore kills the shared
#   automatic edge it replaces: sync() -> sync(String)@sync-null kills
#   sync() -> sync(String); every sync(String) caller retarget kills
#   that caller's automatic edge to plain sync(String); the three
#   sync(String)@sync-R -> Connection.sync@sync-R edges kill the
#   automatic sync(String) -> Connection.sync edge; and the single
#   doInBackgroundSync@sync-download -> FullSyncer.download edge kills
#   the automatic doInBackgroundSync -> FullSyncer.download edge, so
#   even the plain body node (still reachable through the old @SYNC
#   hand chain, which is itself unreachable once plain Connection.sync
#   loses its only incoming) can no longer take the download branch.
# - Variant-copy: an automatic edge that is NOT hand-covered is copied
#   onto every variant of its source node. That is what carries the
#   branch-independent tails onto all three variants without new
#   edges: sync(String) auto edges to Payload, showSyncErrorDialog,
#   getSharedPrefs and the class-init edges; Connection.sync auto edge
#   to launchConnectionTask (whose onward plain doInBackground hop is
#   a dead end: plain doInBackground's automatic doOne hop is already
#   hand-covered by the existing @SYNC entry, and its only surviving
#   hop is the BaseAsyncTask super-call); doInBackground auto edge to
#   BaseAsyncTask.doInBackground; and every doInBackgroundSync auto
#   edge except download (Syncer.sync, FullSyncer.<init>, FullSyncer
#   .upload, MediaSyncer.sync, Collection.reopen, Collection.close
#   (boolean) — a different node from the close() target — and the
#   rest), which land on all three body variants alike. None of those
#   copied tails reaches Collection.close(): Syncer.sync's subtree
#   ends at save/meta/finish, FullSyncer.<init> initialises fields
#   only, FullSyncer.upload ends at reopen, MediaSyncer.sync syncs
#   media. The simulation in NOTES.md verifies this by search, not by
#   assertion.
# - Hand edges are NOT copied: the two hand edges out of plain
#   sync(String) therefore need explicit variant copies, supplied
#   below for all three variants — the task-listener hop to
#   DeckPicker$17.onPostExecute (graph_def.py:532, "the sync task
#   finishes and calls its listener", true for every sync task) and
#   the summary ENTERS hop to S_DLG_SYNC_ERROR_NOT_LOGGED_IN
#   (graph_def_mod/02.py:1924, hkey-empty branch, true for every
#   resolution since the branch is taken before Connection.sync is
#   ever called). The listener copy is what makes the genuine
#   null-task -> fullSync -> download sequence printable (see NOTES
#   section 8: a genuine 14-edge tie, not a fiction).
# - Labels: a base method stays REACHABLE when any of its variants is
#   reached (build_graph.py first_variant maps a reached variant node
#   back to its base method), so plain sync(String), plain
#   Connection.sync, plain doInBackground, plain doOneInBackground
#   and plain doInBackgroundSync losing their shared edges to the
#   variants costs no label, provided every caller is retargeted —
#   which the exhaustive census above guarantees. No plain node is
#   left reachable from a non-retargeted caller.
# - No rewrite clause is needed: every pair below is new (a variant
#   source or destination that appears nowhere in the pushed graph),
#   so nothing is hand-covered that needs rewriting and the single
#   chained rewrite clause in graph_def.py is untouched. The EDIT
#   clause's Connection pruning (graph_def.py:7558) does not touch
#   these variants: its variant-type test accepts only the exact
#   suffixes SYNC and LOGIN, while the new suffixes are SYNC-null,
#   SYNC-download and SYNC-upload, so it returns no match and prunes
#   nothing here; the suppression above already removes the only
#   automatic edge that must not be copied (download).
# - The LOGIN chain is untouched: MyAccount.login ->
#   doInBackground@LOGIN -> doOne@LOGIN -> doInBackgroundLogin shares
#   no node with the sync variants (doInBackgroundLogin is a different
#   body), and no edge below mentions LOGIN, login, or MyAccount.
#
# Edge labels 27-S01..S35 (35 edges). Kinds follow the edges they
# replace: CALL for direct calls, ASYNC for the task entry and the
# task-listener hop, ENTERS for the dialog-summary hop.

# 27-S01: null retarget. sync() passes the literal null, so its only
# genuine target is the null variant. This one edge carries every
# sync() caller (onResume, automaticSync, menu, DialogHandler,
# SyncErrorDialog$2 retry, S_DECKPICKER GUI) into the null chain.
e('DeckPicker.sync()', 'DeckPicker.sync(String)@sync-null', 'CALL', 'Direct call',
  guard='syncConflictResolution == null: sync() passes the literal null (DeckPicker.java:1267)',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1266-1267')

# 27-S02: download retarget, dialog full sync. The $11 callback passes
# the literal "download"; this is v3 V10's tail, retargeted from plain
# sync(String) to the download variant so the genuine $11 chain keeps
# its step count exactly.
e('DatabaseErrorDialog$11.onPositive', 'DeckPicker.sync(String)@sync-download', 'CALL', 'Direct call',
  guard='syncConflictResolution == "download": the full-sync callback passes the literal "download" (DatabaseErrorDialog.java:330)',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:322-334')

# 27-S03: download retarget, sync listener. After a sync task finishes,
# the listener calls sync("download") when the server answer is
# fullSync and the local collection is empty (Syncer.sync returns
# "fullSync" at Syncer.java:137). This is the second genuine download
# caller AUDIT4 names; it is a download call whatever task completed,
# so it targets the download variant from the shared listener node.
e('DeckPicker$17.onPostExecute', 'DeckPicker.sync(String)@sync-download', 'CALL', 'Direct call',
  guard='syncConflictResolution == "download": listener passes the literal "download" on the fullSync + empty-collection branch (DeckPicker.java:1450-1452)',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1450-1452; SRC com/ichi2/libanki/sync/Syncer.java:137')

# 27-S04: upload retarget, conflict keep-local confirm.
e('SyncErrorDialog$4.onPositive', 'DeckPicker.sync(String)@sync-upload', 'CALL', 'Direct call',
  guard='syncConflictResolution == "upload": the keep-local confirm passes the literal "upload" (SyncErrorDialog.java:139)',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:135-142')

# 27-S05: download retarget, conflict keep-remote confirm.
e('SyncErrorDialog$5.onPositive', 'DeckPicker.sync(String)@sync-download', 'CALL', 'Direct call',
  guard='syncConflictResolution == "download": the keep-remote confirm passes the literal "download" (SyncErrorDialog.java:153)',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:149-156')

# 27-S06: upload retarget, sanity keep-local confirm.
e('SyncErrorDialog$7.onPositive', 'DeckPicker.sync(String)@sync-upload', 'CALL', 'Direct call',
  guard='syncConflictResolution == "upload": the sanity keep-local confirm passes the literal "upload" (SyncErrorDialog.java:186)',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:183-189')

# 27-S07: download retarget, sanity keep-remote confirm.
e('SyncErrorDialog$8.onPositive', 'DeckPicker.sync(String)@sync-download', 'CALL', 'Direct call',
  guard='syncConflictResolution == "download": the sanity keep-remote confirm passes the literal "download" (SyncErrorDialog.java:199)',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/SyncErrorDialog.java:196-202')

# 27-S08..S10: null chain, hop 1 of 4. sync(String) builds the payload
# [hkey, syncFetchesMedia, syncConflictResolution] and calls
# Connection.sync; the resolution travels inside the payload, so the
# null variant's Connection.sync node is the null variant.
e('DeckPicker.sync(String)@sync-null', 'Connection.sync@sync-null', 'CALL', 'Direct call',
  guard='payload carries syncConflictResolution == null through to Connection.sync (DeckPicker.java:1284-1286)',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1284-1286')
e('DeckPicker.sync(String)@sync-download', 'Connection.sync@sync-download', 'CALL', 'Direct call',
  guard='payload carries syncConflictResolution == "download" through to Connection.sync (DeckPicker.java:1284-1286)',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1284-1286')
e('DeckPicker.sync(String)@sync-upload', 'Connection.sync@sync-upload', 'CALL', 'Direct call',
  guard='payload carries syncConflictResolution == "upload" through to Connection.sync (DeckPicker.java:1284-1286)',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1284-1286')

# 27-S11..S13: chain hop 2 of 4. Connection.sync sets TASK_TYPE_SYNC
# and launches the task; the entry hop mirrors the existing
# Connection.sync -> doInBackground@SYNC entry (graph_def_mod/02.py),
# with the resolution suffix added so the SYNC family splits by
# resolution instead of sharing one chain.
e('Connection.sync@sync-null', 'Connection.doInBackground@SYNC-null', 'ASYNC',
  'this sync call creates the Connection task instance whose type is SYNC and whose payload resolution is null; AsyncTask.execute runs that instance\'s doInBackground',
  guard='data.taskType == TASK_TYPE_SYNC; payload resolution == null (Connection.java:166-168)',
  env=None,
  evidence='SRC com/ichi2/async/Connection.java:166-168; SRC com/ichi2/async/Connection.java:83-100, 173-179')
e('Connection.sync@sync-download', 'Connection.doInBackground@SYNC-download', 'ASYNC',
  'this sync call creates the Connection task instance whose type is SYNC and whose payload resolution is "download"; AsyncTask.execute runs that instance\'s doInBackground',
  guard='data.taskType == TASK_TYPE_SYNC; payload resolution == "download" (Connection.java:166-168)',
  env=None,
  evidence='SRC com/ichi2/async/Connection.java:166-168; SRC com/ichi2/async/Connection.java:83-100, 173-179')
e('Connection.sync@sync-upload', 'Connection.doInBackground@SYNC-upload', 'ASYNC',
  'this sync call creates the Connection task instance whose type is SYNC and whose payload resolution is "upload"; AsyncTask.execute runs that instance\'s doInBackground',
  guard='data.taskType == TASK_TYPE_SYNC; payload resolution == "upload" (Connection.java:166-168)',
  env=None,
  evidence='SRC com/ichi2/async/Connection.java:166-168; SRC com/ichi2/async/Connection.java:83-100, 173-179')

# 27-S14..S16: chain hop 3 of 4. doInBackground delegates to
# doOneInBackground (Connection.java:178); the variant suffix is
# carried unchanged so the null chain cannot cross into the download
# chain at this hop either.
e('Connection.doInBackground@SYNC-null', 'Connection.doOneInBackground@SYNC-null', 'CALL',
  'doInBackground delegates to doOneInBackground',
  guard='data.taskType == TASK_TYPE_SYNC; payload resolution == null',
  env=None,
  evidence='SRC com/ichi2/async/Connection.java:178')
e('Connection.doInBackground@SYNC-download', 'Connection.doOneInBackground@SYNC-download', 'CALL',
  'doInBackground delegates to doOneInBackground',
  guard='data.taskType == TASK_TYPE_SYNC; payload resolution == "download"',
  env=None,
  evidence='SRC com/ichi2/async/Connection.java:178')
e('Connection.doInBackground@SYNC-upload', 'Connection.doOneInBackground@SYNC-upload', 'CALL',
  'doInBackground delegates to doOneInBackground',
  guard='data.taskType == TASK_TYPE_SYNC; payload resolution == "upload"',
  env=None,
  evidence='SRC com/ichi2/async/Connection.java:178')

# 27-S17..S19: chain hop 4 of 4. doOneInBackground's SYNC case calls
# doInBackgroundSync (Connection.java:187-188); the body node itself
# is split by resolution, which is the hop where the branch finally
# diverges — the body variants are distinct nodes, so the download
# edge below can be given to one variant only.
e('Connection.doOneInBackground@SYNC-null', 'Connection.doInBackgroundSync@sync-null', 'CALL', 'switch case for this branch only',
  guard='data.taskType == TASK_TYPE_SYNC; payload resolution == null (Connection.java:187-188)',
  env=None,
  evidence='SRC com/ichi2/async/Connection.java:187-188')
e('Connection.doOneInBackground@SYNC-download', 'Connection.doInBackgroundSync@sync-download', 'CALL', 'switch case for this branch only',
  guard='data.taskType == TASK_TYPE_SYNC; payload resolution == "download" (Connection.java:187-188)',
  env=None,
  evidence='SRC com/ichi2/async/Connection.java:187-188')
e('Connection.doOneInBackground@SYNC-upload', 'Connection.doInBackgroundSync@sync-upload', 'CALL', 'switch case for this branch only',
  guard='data.taskType == TASK_TYPE_SYNC; payload resolution == "upload" (Connection.java:187-188)',
  env=None,
  evidence='SRC com/ichi2/async/Connection.java:187-188')

# 27-S20: the ONLY download edge in the split. doInBackgroundSync
# constructs FullSyncer and calls server.download() only in the
# non-null "download" branch (Connection.java:318, :334-337); giving
# this edge to the download body variant alone, and to no other
# variant, is the whole fix. Its base pair hand-covers the automatic
# doInBackgroundSync -> FullSyncer.download edge, so the plain body
# node loses the download branch too.
e('Connection.doInBackgroundSync@sync-download', 'FullSyncer.download', 'CALL', 'Direct call',
  guard='conflictResolution == "download": FullSyncer is constructed and server.download() is called only on this branch (Connection.java:318, 334-337)',
  env=None,
  evidence='SRC com/ichi2/async/Connection.java:318, 334-337')

# 27-S21..S23: task-listener copies (hand edges are not copied by the
# builder, so the plain sync(String) -> $17 hop needs one copy per
# variant). The listener runs when any sync task finishes, whatever
# its resolution, so all three variants get it. The null copy is the
# genuine null-task -> fullSync -> download sequence (NOTES section 8).
e('DeckPicker.sync(String)@sync-null', 'DeckPicker$17.onPostExecute', 'ASYNC',
  'the sync task finishes and calls its listener',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1284, 1291, 1404')
e('DeckPicker.sync(String)@sync-download', 'DeckPicker$17.onPostExecute', 'ASYNC',
  'the sync task finishes and calls its listener',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1284, 1291, 1404')
e('DeckPicker.sync(String)@sync-upload', 'DeckPicker$17.onPostExecute', 'ASYNC',
  'the sync task finishes and calls its listener',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1284, 1291, 1404')

# 27-S24..S26: not-logged-in summary copies (same hand-copy reason).
# When hkey is empty, sync(String) shows the not-logged-in dialog
# directly without launching Connection.sync (DeckPicker.java:1280-
# 1282); the branch is taken before the payload resolution matters,
# so all three variants get the summary hop, preserving route 30's
# sync -> sync-error -> login detour at the same hop count (with the
# variant node substituted for plain sync(String)).
e('DeckPicker.sync(String)@sync-null', 'S_DLG_SYNC_ERROR_NOT_LOGGED_IN', 'ENTERS',
  'hkey is empty, so sync(String) shows the not-logged-in dialog directly, without launching Connection.sync',
  guard='hkey empty, com/ichi2/anki/DeckPicker.java:1280-1282 (showSyncErrorDialog(DIALOG_USER_NOT_LOGGED_IN_SYNC) at :1282)',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1280-1282; SRC com/ichi2/anki/DeckPicker.java:1058-1062')
e('DeckPicker.sync(String)@sync-download', 'S_DLG_SYNC_ERROR_NOT_LOGGED_IN', 'ENTERS',
  'hkey is empty, so sync(String) shows the not-logged-in dialog directly, without launching Connection.sync',
  guard='hkey empty, com/ichi2/anki/DeckPicker.java:1280-1282 (showSyncErrorDialog(DIALOG_USER_NOT_LOGGED_IN_SYNC) at :1282)',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1280-1282; SRC com/ichi2/anki/DeckPicker.java:1058-1062')
e('DeckPicker.sync(String)@sync-upload', 'S_DLG_SYNC_ERROR_NOT_LOGGED_IN', 'ENTERS',
  'hkey is empty, so sync(String) shows the not-logged-in dialog directly, without launching Connection.sync',
  guard='hkey empty, com/ichi2/anki/DeckPicker.java:1280-1282 (showSyncErrorDialog(DIALOG_USER_NOT_LOGGED_IN_SYNC) at :1282)',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1280-1282; SRC com/ichi2/anki/DeckPicker.java:1058-1062')

# 27-S27..S30: null-only body edges. All four sit inside the
# conflictResolution == null branch of doInBackgroundSync, so they
# belong to the null body variant only. Each hand-covers its
# automatic edge, so the download and upload body variants lose it
# too (correct: neither branch ever calls client.sync() or takes the
# sanityCheckError save path).
e('Connection.doInBackgroundSync@sync-null', 'Syncer.sync(Connection)', 'CALL', 'Direct call',
  guard='conflictResolution == null: the null branch calls client.sync() (Connection.java:284-288)',
  env=None,
  evidence='SRC com/ichi2/async/Connection.java:288')
e('Connection.doInBackgroundSync@sync-null', 'Syncer.getSyncMsg', 'CALL', 'Direct call',
  guard='conflictResolution == null: the null branch reads the sync message after client.sync() (Connection.java:289)',
  env=None,
  evidence='SRC com/ichi2/async/Connection.java:289')
e('Connection.doInBackgroundSync@sync-null', 'Collection.modSchemaNoCheck', 'CALL', 'Direct call',
  guard='conflictResolution == null: the null branch forces a full sync on sanityCheckError (Connection.java:302)',
  env=None,
  evidence='SRC com/ichi2/async/Connection.java:302')
e('Connection.doInBackgroundSync@sync-null', 'Collection.save()', 'CALL', 'Direct call',
  guard='conflictResolution == null: the null branch saves after forcing a full sync on sanityCheckError (Connection.java:303)',
  env=None,
  evidence='SRC com/ichi2/async/Connection.java:303')

# 27-S31..S32: non-null body edges. FullSyncer is constructed only
# in the else (non-null) branch (Connection.java:318), so its
# construction edge goes to the download and upload body variants
# only; the null body variant never constructs a FullSyncer.
e('Connection.doInBackgroundSync@sync-download', 'FullSyncer.<init>', 'CALL', 'Direct call',
  guard='conflictResolution != null: the else branch constructs FullSyncer (Connection.java:318)',
  env=None,
  evidence='SRC com/ichi2/async/Connection.java:318')
e('Connection.doInBackgroundSync@sync-upload', 'FullSyncer.<init>', 'CALL', 'Direct call',
  guard='conflictResolution != null: the else branch constructs FullSyncer (Connection.java:318)',
  env=None,
  evidence='SRC com/ichi2/async/Connection.java:318')

# 27-S33: upload-only body edge. server.upload() is called only in
# the "upload" branch (Connection.java:322); upload's beforeUpload
# calls close() (Collection.java:411), so this edge must NOT be
# copied to the null or download variants — that copy is what made
# the first simulation print a 13-edge branch-false upload path.
e('Connection.doInBackgroundSync@sync-upload', 'FullSyncer.upload', 'CALL', 'Direct call',
  guard='conflictResolution == "upload": server.upload() is called only on this branch (Connection.java:322)',
  env=None,
  evidence='SRC com/ichi2/async/Connection.java:322')

# 27-S34..S35: non-null body edges. col.reopen() after a full sync is
# called in the upload branch (Connection.java:323) and in the
# download branch (Connection.java:345, :351), never in the null
# branch, so it goes to the download and upload body variants only.
e('Connection.doInBackgroundSync@sync-download', 'Collection.reopen', 'CALL', 'Direct call',
  guard='conflictResolution == "download": col.reopen() after a successful or failed download (Connection.java:345, 351)',
  env=None,
  evidence='SRC com/ichi2/async/Connection.java:345, 351')
e('Connection.doInBackgroundSync@sync-upload', 'Collection.reopen', 'CALL', 'Direct call',
  guard='conflictResolution == "upload": col.reopen() after upload (Connection.java:323)',
  env=None,
  evidence='SRC com/ichi2/async/Connection.java:323')

# End of route 27 v4 draft: 47 variant edges (v3's 12: 27-V01, V01b,
# V01c, V02, V03, V04, V08, V05, V06, V07, V09, V10; plus the sync
# split's 35: 27-S01..S35) + 4 SCREENS entries. No removal call, no
# chained rewrite clause, no duplicated tail edge, no
# S_DLG_CONFIRMATION edge. The generic-page deletions that make this
# fragment fix the route are merger moves M1-M5 + M11 in NOTES.md,
# not edges in this file; the $6 disposition is route 25's F02 move
# in the combined batch, not an edge in this file; and the four
# ENTERS edges are deleted/retargeted only under the pinned
# ENTERS/cursor gate in NOTES.md section 9, not as a standalone
# route-27 move.

# ---- route 28 ----
# ---- AnkiDroid route 28 DRAFT ONLY (turn fix, route 28 only; NOT merged) ----
# Target: AbstractFlashcardViewer.typeAnswer, final-draw route 28, WRONG at
# printed step 9 (Eed5b25c0, shared TaskListener.onPreExecute fan-out to a
# listener the LOAD_DECK_COUNTS launch never registered).
# This fragment supplies e() edges only. It defines no EDIT, no sup(), no
# SCREENS entry, and no builder edit. Any EDIT clause needed with it lives
# ONLY in the companion file EDIT-wrapper-draft.txt, which must be appended
# to graphs/AnkiDroid/graph_def.py AFTER the current final EDIT definition
# (the B6 wrapper), never inside this file, and must chain the previous
# EDIT rather than replace it.
# Conventions (graph_def.py top, graph_def_mod/02.py header): variant edges
# carry the type condition as guard TEXT only; env and needs_state are never
# set on a variant edge, so the variant chain keeps the same BFS cost as
# the shared chain and wins only because the shared fiction hop is gone
# (see NOTES.md, hand-covering section). Evidence uses plain SRC, never a
# bytecode citation, because a launch-site line contains launchDeckTask,
# not onPreExecute.
# Scope: route 28's corrected route only. The entry below is the Reviewer
# ANSWER_CARD launch; no other launch site is added here (see NOTES.md
# for the AFV onActivityResult and UNDO launches, which stay for a later
# fragment, and for why no DeckTask.onPreExecute@ANSWER_CARD hop is used).

# Entry: Reviewer.onCollectionLoaded launches ANSWER_CARD with
# mAnswerCardHandler. Method declared at Reviewer.java:96-98; the launch
# call itself is at Reviewer.java:110-111. The listener is the
# AbstractFlashcardViewer field mAnswerCardHandler, declared at
# AbstractFlashcardViewer.java:578; its onPreExecute body at :583-585
# calls blockControls(). DeckTask.launchDeckTask at DeckTask.java:129-134
# calls execute(), which runs onPreExecute before the background work;
# DeckTask.onPreExecute at DeckTask.java:344-347 delegates to the listener
# passed to this launch (DeckTask.java:346: mListener.onPreExecute(this)).
# Kind ASYNC, following the DeckTask entry edges in graph_def_mod/02.py
# and the direct launch-to-listener edges in graph_def.py (for example
# AbstractFlashcardViewer.answerCard -> AbstractFlashcardViewer$10.onPreExecute).
e('Reviewer.onCollectionLoaded', 'DeckTask$TaskListener.onPreExecute@ANSWER_CARD', 'ASYNC',
  "this launch call creates the task instance whose type is ANSWER_CARD with mAnswerCardHandler; AsyncTask.execute runs that instance's onPreExecute before its background work",
  guard='mType == TASK_TYPE_ANSWER_CARD', env=None,
  evidence='SRC Reviewer.java:110-111; SRC com/ichi2/async/DeckTask.java:129-134, 344-347; SRC com/ichi2/anki/AbstractFlashcardViewer.java:578-585')

# Listener hop: the TaskListener default forwards onPreExecute(task) to
# the no-argument onPreExecute that mAnswerCardHandler overrides
# (DeckTask.java:1299-1301). For ANSWER_CARD the registered listener set
# is exactly {AbstractFlashcardViewer$10}: every ANSWER_CARD launch in
# the tree passes mAnswerCardHandler (AbstractFlashcardViewer.java:1076,
# 1092, 1320; Reviewer.java:110-111). No other listener is written here.
# Kind CALL, following the onPostExecute@T -> TaskListener@T hops in
# graph_def_mod/02.py. The tail after this edge already exists as auto
# edges and is NOT re-written: AbstractFlashcardViewer$10.onPreExecute
# -> AbstractFlashcardViewer.blockControls (AbstractFlashcardViewer.java:584)
# -> AbstractFlashcardViewer.typeAnswer (AbstractFlashcardViewer.java:2449,
# predicate evaluation in blockControls).
e('DeckTask$TaskListener.onPreExecute@ANSWER_CARD', 'AbstractFlashcardViewer$10.onPreExecute', 'CALL',
  'the TaskListener adapter forwards pre-execute to the registered listener for this type',
  env=None,
  evidence='SRC com/ichi2/async/DeckTask.java:1299-1301; SRC com/ichi2/anki/AbstractFlashcardViewer.java:578-585')

# ---- Lead-owned section (merge lead, 2026-11-02; design in
# turn/merge/LEAD_PAGES_DESIGN.md, independently audit-PASS in
# turn/merge/LEAD_PAGES_AUDIT.md). Neither page is in any fragment.
# CURSOR: parallel page, NOT dual-label: the id-9 branch
# (DeckPicker.java:430-431) shares the $1 block (DatabaseErrorDialog.java:73-94)
# with id 0, so it gets its own page + B01/B02 copies; route 25's A01 stays
# id-0-only. $1's onward edges are reused, not duplicated (C01 already
# carries $1.onPositive -> helper@ERROR_HANDLING; $1.onNegative -> exit is
# the :91 auto call).
# NEW_COLLECTION: genuine 2-hop helper form for entry (N-01/N-02/N-03) and
# for the failure bridge (N-04/N-05, targeting route 25's @LOAD_FAILED page
# only, never both LOAD_FAILED pages). No 1-hop $3->page or $8->page edge.
# Auditor erratum noted: $8.onPositive's auto outgoing set also includes
# the ancillary CollectionHelper.getInstance (:283) and
# BackupManager.<clinit> (:285); neither is a page transition or
# hand-cover target, so no edge is added for them. The page-relevant
# outgoing auto calls are :283-286 + :288 as in the design.

# Variant-page descriptions (NOT SCREENS entries, same builder reason as
# the route-25 pages above):
# S_DLG_DATABASE_ERROR@CURSOR_SIZE_LIMIT_EXCEEDED = 'DatabaseErrorDialog type 9 (DIALOG_CURSOR_SIZE_LIMIT_EXCEEDED): cursor size limit exceeded, error-handling options or close only'

# C-01: cursor ENTERS (the id-9 half of the split generic onCreate edge;
# route 25 A01 is the id-0 half).
e('DeckPicker.onCreate', 'S_DLG_DATABASE_ERROR@CURSOR_SIZE_LIMIT_EXCEEDED', 'ENTERS',
  'the collection is not open and the storage checks pass: the cursor-size dialog (id 9) is shown',
  guard='dialog id == DIALOG_CURSOR_SIZE_LIMIT_EXCEEDED (9), passed through showDatabaseErrorDialog; taken only when exceededCursorSizeLimit is true',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:418, 430-431; SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:27-36')

# C-02: cursor positive dispatch (B01 copy, new source page, same $1 node).
gui('S_DLG_DATABASE_ERROR@CURSOR_SIZE_LIMIT_EXCEEDED', 'DatabaseErrorDialog$1.onPositive',
    'tap error handling options on the cursor-size dialog',
    guard='dialog id == DIALOG_CURSOR_SIZE_LIMIT_EXCEEDED (9); this callback exists only on the load-failed / cursor dialog',
    evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:80-87')

# C-03: cursor negative dispatch (B02 copy).
gui('S_DLG_DATABASE_ERROR@CURSOR_SIZE_LIMIT_EXCEEDED', 'DatabaseErrorDialog$1.onNegative',
    'tap close on the cursor-size dialog (DeckPicker.exit)',
    guard='dialog id == DIALOG_CURSOR_SIZE_LIMIT_EXCEEDED (9); this callback exists only on the load-failed / cursor dialog',
    evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:89-92')

# Variant-page description (NOT a SCREENS entry, same builder reason):
# S_DLG_DATABASE_ERROR@NEW_COLLECTION = 'DatabaseErrorDialog type 5 (DIALOG_NEW_COLLECTION): create a new empty collection, old database moves to the broken folder; create restarts, failure returns to the load-failed dialog'

# N-01: value-5 pick calls the split helper (CALL; base pair hand-covers
# the :194 auto call, as route 25 C03 does for value 3).
e('DatabaseErrorDialog$3.onSelection', 'DeckPicker.showDatabaseErrorDialog@NEW_COLLECTION', 'CALL', 'Direct call',
  guard='user picks delete-old-collection, mRepairValues[which] == 5, always offered; dialog id == DIALOG_NEW_COLLECTION (5), passed through',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:155-156, 170-172, 192-194')

# N-02: split helper (id 5) shows the NEW_COLLECTION variant page.
e('DeckPicker.showDatabaseErrorDialog@NEW_COLLECTION', 'S_DLG_DATABASE_ERROR@NEW_COLLECTION', 'ENTERS',
  'the new-collection dialog is requested: the create-new-collection dialog opens',
  guard='dialog id == DIALOG_NEW_COLLECTION (5), passed through',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1026-1028; SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:47-53, 57-59, 275')

# N-03: NEW_COLLECTION dispatch (re-provided $8 dispatch, replacing
# generic 5549-5553).
gui('S_DLG_DATABASE_ERROR@NEW_COLLECTION', 'DatabaseErrorDialog$8.onPositive',
    'tap create on the new-collection dialog (the old database moves to the broken folder)',
    guard='dialog id == DIALOG_NEW_COLLECTION (5); this callback exists only on the new-collection dialog',
    evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:280-290')

# N-04: failure bridge, first hop: $8 calls the split helper with id 0
# (CALL; base pair hand-covers the :288 auto call; else branch only).
e('DatabaseErrorDialog$8.onPositive', 'DeckPicker.showDatabaseErrorDialog@LOAD_FAILED', 'CALL', 'Direct call',
  guard='dialog id == DIALOG_LOAD_FAILED (0), passed through; taken only when moveDatabaseToBrokenFolder returns false',
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:285-288')

# N-05: failure bridge, second hop: split helper (id 0) shows route 25's
# @LOAD_FAILED variant page (only target; never both LOAD_FAILED pages).
e('DeckPicker.showDatabaseErrorDialog@LOAD_FAILED', 'S_DLG_DATABASE_ERROR@LOAD_FAILED', 'ENTERS',
  'the load-failed dialog is requested after the new-collection move fails: the load-failed dialog opens',
  guard='dialog id == DIALOG_LOAD_FAILED (0), passed through',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1026-1028; SRC com/ichi2/anki/dialogs/DatabaseErrorDialog.java:47-53, 57-59, 73-74')


