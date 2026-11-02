# ---- Stream A combined build (user order 2026-11-02 ~00:25 EST): DeckTask split + dialog/hook variants + best-route Set G ----
# Fragments (audited designs, applied in one build): apply-decktask/02-decktask.py, apply-dialog/02-dialog.py, apply-bestroute/02-bestroute.py.
# The DeckTask EDIT clause is appended to graphs/AnkiDroid/graph_def.py AFTER the B6 wrapper (never in this mod file).
# Hand deletions applied with this build (see fix_log): 01.py Edf6d8bd0, 01.py three base-onCreate Reviewer edges, graph_def.py Eefecf867 clinit edge, graph_def.py Eb9d6a916 generic RESULT edge.

# ---- DeckTask / Connection variant split (helper apply-decktask, design-decktask DESIGN.md second rework) ----
# READ BEFORE APPENDING: this fragment supplies e() edges only. It defines no EDIT, no sup(),
# no SCREENS entry, and no builder edit. The EDIT clause lives in the companion file
# EDIT-wrapper-decktask.py and MUST be appended to graphs/AnkiDroid/graph_def.py AFTER the
# current final EDIT definition (the B6 wrapper, graph_def.py:7162 in this tree), never inside
# graph_def_mod/02.py: the mod loader in graph_def.py runs before the B3/B6 EDIT definitions,
# so an EDIT written in a mod file would be replaced by them and never applied.
# This edge fragment itself may be appended as graphs/AnkiDroid/graph_def_mod/02.py content
# (it runs in the same namespace as graph_def.py, so e() is available), or appended to
# graph_def.py after the EDIT wrapper; either placement is fine for edges, because the builder
# applies EDIT to all edges only after the whole graph definition has been executed.
# Conventions (graph_def.py top, builder build_graph.py:304): e(src, dst, kind, trigger,
# guard=None, evidence=None, env=None). Variant edges carry the type condition as guard TEXT
# only: env and needs_state are never set on a variant edge, so variant chains keep the same
# BFS cost as the shared chains and win only on steps (design section 1.2, section 5.5).
# Evidence rule (design section 1.3): entry edges use plain SRC, never a bytecode citation,
# because a launch-site line contains launchDeckTask, not doInBackground. Body edges use plain
# SRC over the case/return lines (design allows plain SRC; it passes check 2). No edge
# evidence, guard, trigger, or comment in this file uses the literal counted by check 5.
# Counts in this file: 50 entry edges for 51 launch call lines (AbstractFlashcardViewer.
# onActivityResult ANSWER covers two lines, :1076 and :1092, in one (method, type) entry);
# 34 body edges; post chains for all 34 types; progress chains for 8 types (see section 4).
# No post/progress chain is written for a type whose design listener set is empty, and no
# shared edge is deleted by this file: suppression of the shared body/listener edges is done
# by the hand-covering rule (build_graph.py:216-228) plus the EDIT clause, not by sup().

# ================================================================== 1. Entry edges (design section 2.3 item 1) =====
# One e() call per (launching method, type). Kind ASYNC. Guard text verbatim:
# mType == TASK_TYPE_<T>. Evidence template verbatim from design section 2.3 item 1:
# SRC <launch file>:<launch line>; SRC com/ichi2/async/DeckTask.java:129-134, 203-204;
# FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651. These edges bypass the shared
# DeckTask.launchDeckTask node, so a variant chain is one step shorter than the shared chain.
# Receiver-variant launch records (AbstractFlashcardViewer.onActivityResult@Previewer /
# @Reviewer in auto_calls.json) get NO separate entry edge: design section 2.2 counts
# AbstractFlashcardViewer.onActivityResult as two entries (ANSWER, UPDATE), not three, and the
# receiver records are duplicates of the same :1092 call, not separate launch methods.
# LOAD_DECK_COUNTS: DeckPicker.updateDeckList (DeckPicker.java:1823) listener DeckPicker$22 -- anonymous, DeckPicker.java:1823-1846
e('DeckPicker.updateDeckList', 'DeckTask.doInBackground@LOAD_DECK_COUNTS', 'ASYNC',
  "this launch call creates the task instance whose type is LOAD_DECK_COUNTS; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_LOAD_DECK_COUNTS', env=None,
  evidence='SRC DeckPicker.java:1823; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# SAVE_COLLECTION: UIUtils.saveCollectionInBackground (UIUtils.java:115) listener UIUtils$1 -- anonymous
e('UIUtils.saveCollectionInBackground', 'DeckTask.doInBackground@SAVE_COLLECTION', 'ASYNC',
  "this launch call creates the task instance whose type is SAVE_COLLECTION; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_SAVE_COLLECTION', env=None,
  evidence='SRC UIUtils.java:115; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# ANSWER_CARD: AbstractFlashcardViewer.answerCard (AbstractFlashcardViewer.java:1320) listener AbstractFlashcardViewer$10 -- mAnswerCardHandler, field AbstractFlashcardViewer.java:578
e('AbstractFlashcardViewer.answerCard', 'DeckTask.doInBackground@ANSWER_CARD', 'ASYNC',
  "this launch call creates the task instance whose type is ANSWER_CARD; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_ANSWER_CARD', env=None,
  evidence='SRC AbstractFlashcardViewer.java:1320; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# ANSWER_CARD: AbstractFlashcardViewer.onActivityResult (AbstractFlashcardViewer.java:1076, 1092) listener AbstractFlashcardViewer$10 -- mAnswerCardHandler; two lines, one (method, type) entry
e('AbstractFlashcardViewer.onActivityResult', 'DeckTask.doInBackground@ANSWER_CARD', 'ASYNC',
  "this launch call creates the task instance whose type is ANSWER_CARD; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_ANSWER_CARD', env=None,
  evidence='SRC AbstractFlashcardViewer.java:1076; SRC AbstractFlashcardViewer.java:1092; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# ANSWER_CARD: Reviewer.onCollectionLoaded (Reviewer.java:110) listener AbstractFlashcardViewer$10 -- mAnswerCardHandler
e('Reviewer.onCollectionLoaded', 'DeckTask.doInBackground@ANSWER_CARD', 'ASYNC',
  "this launch call creates the task instance whose type is ANSWER_CARD; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_ANSWER_CARD', env=None,
  evidence='SRC Reviewer.java:110; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# ADD_FACT: NoteEditor.saveNote (NoteEditor.java:681) listener NoteEditor$1 -- mSaveFactHandler
e('NoteEditor.saveNote', 'DeckTask.doInBackground@ADD_FACT', 'ASYNC',
  "this launch call creates the task instance whose type is ADD_FACT; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_ADD_FACT', env=None,
  evidence='SRC NoteEditor.java:681; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# UPDATE_FACT: AbstractFlashcardViewer.onActivityResult (AbstractFlashcardViewer.java:1084) listener AbstractFlashcardViewer$9 -- mUpdateCardHandler, field AbstractFlashcardViewer.java:511
e('AbstractFlashcardViewer.onActivityResult', 'DeckTask.doInBackground@UPDATE_FACT', 'ASYNC',
  "this launch call creates the task instance whose type is UPDATE_FACT; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_UPDATE_FACT', env=None,
  evidence='SRC AbstractFlashcardViewer.java:1084; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# UPDATE_FACT: CardBrowser.onActivityResult (CardBrowser.java:697) listener CardBrowser$13 -- mUpdateCardHandler (CardBrowser)
e('CardBrowser.onActivityResult', 'DeckTask.doInBackground@UPDATE_FACT', 'ASYNC',
  "this launch call creates the task instance whose type is UPDATE_FACT; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_UPDATE_FACT', env=None,
  evidence='SRC CardBrowser.java:697; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# UNDO: AbstractFlashcardViewer.undo (AbstractFlashcardViewer.java:1172) listener AbstractFlashcardViewer$10 -- mAnswerCardHandler, NOT DeckPicker$13
e('AbstractFlashcardViewer.undo', 'DeckTask.doInBackground@UNDO', 'ASYNC',
  "this launch call creates the task instance whose type is UNDO; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_UNDO', env=None,
  evidence='SRC AbstractFlashcardViewer.java:1172; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# UNDO: DeckPicker.undo (DeckPicker.java:999) listener DeckPicker$13 -- undo listener
e('DeckPicker.undo', 'DeckTask.doInBackground@UNDO', 'ASYNC',
  "this launch call creates the task instance whose type is UNDO; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_UNDO', env=None,
  evidence='SRC DeckPicker.java:999; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# SEARCH_CARDS: CardBrowser.searchCards (CardBrowser.java:812) listener CardBrowser$16 -- mSearchCardsHandler
e('CardBrowser.searchCards', 'DeckTask.doInBackground@SEARCH_CARDS', 'ASYNC',
  "this launch call creates the task instance whose type is SEARCH_CARDS; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_SEARCH_CARDS', env=None,
  evidence='SRC CardBrowser.java:812; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# DISMISS: AbstractFlashcardViewer.dismiss (AbstractFlashcardViewer.java:2825) listener AbstractFlashcardViewer$8 -- mDismissCardHandler, field AbstractFlashcardViewer.java:484
e('AbstractFlashcardViewer.dismiss', 'DeckTask.doInBackground@DISMISS', 'ASYNC',
  "this launch call creates the task instance whose type is DISMISS; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_DISMISS', env=None,
  evidence='SRC AbstractFlashcardViewer.java:2825; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# DISMISS: CardBrowser$1.onSelection (CardBrowser.java:179) listener CardBrowser$14 -- mSuspendCardHandler
e('CardBrowser$1.onSelection', 'DeckTask.doInBackground@DISMISS', 'ASYNC',
  "this launch call creates the task instance whose type is DISMISS; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_DISMISS', env=None,
  evidence='SRC CardBrowser.java:179; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# DISMISS: CardBrowser$1$1.onClick (CardBrowser.java:198) listener CardBrowser$15 -- mDeleteNoteHandler, NOT $8
e('CardBrowser$1$1.onClick', 'DeckTask.doInBackground@DISMISS', 'ASYNC',
  "this launch call creates the task instance whose type is DISMISS; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_DISMISS', env=None,
  evidence='SRC CardBrowser.java:198; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# CHECK_DATABASE: DeckPicker.integrityCheck (DeckPicker.java:1147) listener DeckPicker$15 -- per route-08 note
e('DeckPicker.integrityCheck', 'DeckTask.doInBackground@CHECK_DATABASE', 'ASYNC',
  "this launch call creates the task instance whose type is CHECK_DATABASE; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_CHECK_DATABASE', env=None,
  evidence='SRC DeckPicker.java:1147; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# REPAIR_DECK: DeckPicker.repairDeck (DeckPicker.java:1112) listener DeckPicker$14 -- confirmed by body matching
e('DeckPicker.repairDeck', 'DeckTask.doInBackground@REPAIR_DECK', 'ASYNC',
  "this launch call creates the task instance whose type is REPAIR_DECK; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_REPAIR_DECK', env=None,
  evidence='SRC DeckPicker.java:1112; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# UPDATE_VALUES_FROM_DECK: StudyOptionsFragment.refreshInterface(boolean,boolean) (StudyOptionsFragment.java:492) listener StudyOptionsFragment$3 -- getDeckTaskListener listener
e('StudyOptionsFragment.refreshInterface(boolean,boolean)', 'DeckTask.doInBackground@UPDATE_VALUES_FROM_DECK', 'ASYNC',
  "this launch call creates the task instance whose type is UPDATE_VALUES_FROM_DECK; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_UPDATE_VALUES_FROM_DECK', env=None,
  evidence='SRC StudyOptionsFragment.java:492; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# DELETE_DECK: DeckPicker.deleteDeck (DeckPicker.java:2017) listener DeckPicker$24 -- confirmed by body matching
e('DeckPicker.deleteDeck', 'DeckTask.doInBackground@DELETE_DECK', 'ASYNC',
  "this launch call creates the task instance whose type is DELETE_DECK; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_DELETE_DECK', env=None,
  evidence='SRC DeckPicker.java:2017; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# REBUILD_CRAM: DeckPicker.rebuildFiltered (DeckPicker.java:2102) listener DeckPicker$25 -- mSimpleProgressListener
e('DeckPicker.rebuildFiltered', 'DeckTask.doInBackground@REBUILD_CRAM', 'ASYNC',
  "this launch call creates the task instance whose type is REBUILD_CRAM; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_REBUILD_CRAM', env=None,
  evidence='SRC DeckPicker.java:2102; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# REBUILD_CRAM: StudyOptionsFragment.onMenuItemClick (StudyOptionsFragment.java:318) listener StudyOptionsFragment$3 -- getDeckTaskListener(true); same method also launches EMPTY_CRAM at :325
e('StudyOptionsFragment.onMenuItemClick', 'DeckTask.doInBackground@REBUILD_CRAM', 'ASYNC',
  "this launch call creates the task instance whose type is REBUILD_CRAM; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_REBUILD_CRAM', env=None,
  evidence='SRC StudyOptionsFragment.java:318; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# REBUILD_CRAM: StudyOptionsFragment.onActivityResult (StudyOptionsFragment.java:427) listener StudyOptionsFragment$3 -- getDeckTaskListener(true)
e('StudyOptionsFragment.onActivityResult', 'DeckTask.doInBackground@REBUILD_CRAM', 'ASYNC',
  "this launch call creates the task instance whose type is REBUILD_CRAM; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_REBUILD_CRAM', env=None,
  evidence='SRC StudyOptionsFragment.java:427; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# REBUILD_CRAM: CustomStudyDialog.createCustomStudySession (CustomStudyDialog.java:454) listener CustomStudyDialog$4
e('CustomStudyDialog.createCustomStudySession', 'DeckTask.doInBackground@REBUILD_CRAM', 'ASYNC',
  "this launch call creates the task instance whose type is REBUILD_CRAM; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_REBUILD_CRAM', env=None,
  evidence='SRC CustomStudyDialog.java:454; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# EMPTY_CRAM: DeckPicker.emptyFiltered (DeckPicker.java:2108) listener DeckPicker$25 -- mSimpleProgressListener
e('DeckPicker.emptyFiltered', 'DeckTask.doInBackground@EMPTY_CRAM', 'ASYNC',
  "this launch call creates the task instance whose type is EMPTY_CRAM; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_EMPTY_CRAM', env=None,
  evidence='SRC DeckPicker.java:2108; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# EMPTY_CRAM: StudyOptionsFragment.onMenuItemClick (StudyOptionsFragment.java:325) listener StudyOptionsFragment$3 -- getDeckTaskListener(true)
e('StudyOptionsFragment.onMenuItemClick', 'DeckTask.doInBackground@EMPTY_CRAM', 'ASYNC',
  "this launch call creates the task instance whose type is EMPTY_CRAM; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_EMPTY_CRAM', env=None,
  evidence='SRC StudyOptionsFragment.java:325; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# IMPORT: DeckPicker.importAdd (DeckPicker.java:1580) listener DeckPicker$5 -- mImportAddListener
e('DeckPicker.importAdd', 'DeckTask.doInBackground@IMPORT', 'ASYNC',
  "this launch call creates the task instance whose type is IMPORT; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_IMPORT', env=None,
  evidence='SRC DeckPicker.java:1580; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# IMPORT_REPLACE: DeckPicker.importReplace (DeckPicker.java:1588) listener DeckPicker$6 -- mImportReplaceListener
e('DeckPicker.importReplace', 'DeckTask.doInBackground@IMPORT_REPLACE', 'ASYNC',
  "this launch call creates the task instance whose type is IMPORT_REPLACE; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_IMPORT_REPLACE', env=None,
  evidence='SRC DeckPicker.java:1588; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# EXPORT_APKG: DeckPicker.exportApkg (DeckPicker.java:1623) listener DeckPicker$7 -- mExportListener
e('DeckPicker.exportApkg', 'DeckTask.doInBackground@EXPORT_APKG', 'ASYNC',
  "this launch call creates the task instance whose type is EXPORT_APKG; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_EXPORT_APKG', env=None,
  evidence='SRC DeckPicker.java:1623; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# REORDER: DeckOptions$DeckPreferenceHack$Editor.commit (DeckOptions.java:170) listener DeckOptions$DeckPreferenceHack$Editor$2 -- mConfChangeHandler; graph src is commit, not plain DeckOptions
e('DeckOptions$DeckPreferenceHack$Editor.commit', 'DeckTask.doInBackground@REORDER', 'ASYNC',
  "this launch call creates the task instance whose type is REORDER; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_REORDER', env=None,
  evidence='SRC DeckOptions.java:170; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# CONF_CHANGE: DeckOptions$DeckPreferenceHack$Editor.commit (DeckOptions.java:223) listener DeckOptions$DeckPreferenceHack$Editor$2 -- mConfChangeHandler
e('DeckOptions$DeckPreferenceHack$Editor.commit', 'DeckTask.doInBackground@CONF_CHANGE', 'ASYNC',
  "this launch call creates the task instance whose type is CONF_CHANGE; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_CONF_CHANGE', env=None,
  evidence='SRC DeckOptions.java:223; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# CONF_RESET: DeckOptions$DeckPreferenceHack$Editor.commit (DeckOptions.java:232) listener DeckOptions$DeckPreferenceHack$Editor$2 -- mConfChangeHandler
e('DeckOptions$DeckPreferenceHack$Editor.commit', 'DeckTask.doInBackground@CONF_RESET', 'ASYNC',
  "this launch call creates the task instance whose type is CONF_RESET; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_CONF_RESET', env=None,
  evidence='SRC DeckOptions.java:232; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# CONF_REMOVE: DeckOptions$DeckPreferenceHack$Editor.remConf (DeckOptions.java:404) listener DeckOptions$DeckPreferenceHack$Editor$2 -- mConfChangeHandler
e('DeckOptions$DeckPreferenceHack$Editor.remConf', 'DeckTask.doInBackground@CONF_REMOVE', 'ASYNC',
  "this launch call creates the task instance whose type is CONF_REMOVE; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_CONF_REMOVE', env=None,
  evidence='SRC DeckOptions.java:404; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# CONF_SET_SUBDECKS: DeckOptions$DeckPreferenceHack$Editor.commit (DeckOptions.java:276) listener DeckOptions$DeckPreferenceHack$Editor$2 -- mConfChangeHandler
e('DeckOptions$DeckPreferenceHack$Editor.commit', 'DeckTask.doInBackground@CONF_SET_SUBDECKS', 'ASYNC',
  "this launch call creates the task instance whose type is CONF_SET_SUBDECKS; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_CONF_SET_SUBDECKS', env=None,
  evidence='SRC DeckOptions.java:276; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# RENDER_BROWSER_QA: CardBrowser$RenderOnScroll.onScroll (CardBrowser.java:1156) listener CardBrowser$17 -- mRenderQAHandler
e('CardBrowser$RenderOnScroll.onScroll', 'DeckTask.doInBackground@RENDER_BROWSER_QA', 'ASYNC',
  "this launch call creates the task instance whose type is RENDER_BROWSER_QA; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_RENDER_BROWSER_QA', env=None,
  evidence='SRC CardBrowser.java:1156; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# RENDER_BROWSER_QA: CardBrowser$RenderOnScroll.onScrollStateChanged (CardBrowser.java:1170) listener CardBrowser$17 -- mRenderQAHandler
e('CardBrowser$RenderOnScroll.onScrollStateChanged', 'DeckTask.doInBackground@RENDER_BROWSER_QA', 'ASYNC',
  "this launch call creates the task instance whose type is RENDER_BROWSER_QA; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_RENDER_BROWSER_QA', env=None,
  evidence='SRC CardBrowser.java:1170; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# CHECK_MEDIA: DeckPicker.mediaCheck (DeckPicker.java:1191) listener DeckPicker$16 -- per route-08 note
e('DeckPicker.mediaCheck', 'DeckTask.doInBackground@CHECK_MEDIA', 'ASYNC',
  "this launch call creates the task instance whose type is CHECK_MEDIA; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_CHECK_MEDIA', env=None,
  evidence='SRC DeckPicker.java:1191; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# ADD_TEMPLATE: CardTemplateEditor$CardTemplateFragment.addNewTemplate (CardTemplateEditor.java:718) listener CardTemplateEditor$1 -- mUpdateTemplateHandler, shared with REMOVE_TEMPLATE
e('CardTemplateEditor$CardTemplateFragment.addNewTemplate', 'DeckTask.doInBackground@ADD_TEMPLATE', 'ASYNC',
  "this launch call creates the task instance whose type is ADD_TEMPLATE; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_ADD_TEMPLATE', env=None,
  evidence='SRC CardTemplateEditor.java:718; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# REMOVE_TEMPLATE: CardTemplateEditor$CardTemplateFragment.deleteTemplate (CardTemplateEditor.java:664) listener CardTemplateEditor$1 -- mUpdateTemplateHandler, shared with ADD_TEMPLATE
e('CardTemplateEditor$CardTemplateFragment.deleteTemplate', 'DeckTask.doInBackground@REMOVE_TEMPLATE', 'ASYNC',
  "this launch call creates the task instance whose type is REMOVE_TEMPLATE; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_REMOVE_TEMPLATE', env=None,
  evidence='SRC CardTemplateEditor.java:664; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# COUNT_MODELS: ModelBrowser.onCollectionLoaded (ModelBrowser.java:240) listener ModelBrowser$1 -- mLoadingModelsHandler
e('ModelBrowser.onCollectionLoaded', 'DeckTask.doInBackground@COUNT_MODELS', 'ASYNC',
  "this launch call creates the task instance whose type is COUNT_MODELS; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_COUNT_MODELS', env=None,
  evidence='SRC ModelBrowser.java:240; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# COUNT_MODELS: ModelBrowser.fullRefresh (ModelBrowser.java:572) listener ModelBrowser$1 -- mLoadingModelsHandler
e('ModelBrowser.fullRefresh', 'DeckTask.doInBackground@COUNT_MODELS', 'ASYNC',
  "this launch call creates the task instance whose type is COUNT_MODELS; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_COUNT_MODELS', env=None,
  evidence='SRC ModelBrowser.java:572; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# COUNT_MODELS: ModelBrowser.onActivityResult (ModelBrowser.java:680) listener ModelBrowser$1 -- mLoadingModelsHandler
e('ModelBrowser.onActivityResult', 'DeckTask.doInBackground@COUNT_MODELS', 'ASYNC',
  "this launch call creates the task instance whose type is COUNT_MODELS; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_COUNT_MODELS', env=None,
  evidence='SRC ModelBrowser.java:680; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# DELETE_MODEL: ModelBrowser.deleteModel (ModelBrowser.java:579) listener ModelBrowser$2 -- mDeleteModelHandler
e('ModelBrowser.deleteModel', 'DeckTask.doInBackground@DELETE_MODEL', 'ASYNC',
  "this launch call creates the task instance whose type is DELETE_MODEL; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_DELETE_MODEL', env=None,
  evidence='SRC ModelBrowser.java:579; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# DELETE_FIELD: ModelFieldEditor.deleteField (ModelFieldEditor.java:281) listener ModelFieldEditor$8 -- mChangeFieldHandler
e('ModelFieldEditor.deleteField', 'DeckTask.doInBackground@DELETE_FIELD', 'ASYNC',
  "this launch call creates the task instance whose type is DELETE_FIELD; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_DELETE_FIELD', env=None,
  evidence='SRC ModelFieldEditor.java:281; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# REPOSITION_FIELD: ModelFieldEditor$6.onPositive (ModelFieldEditor.java:376) listener ModelFieldEditor$8 -- mChangeFieldHandler
e('ModelFieldEditor$6.onPositive', 'DeckTask.doInBackground@REPOSITION_FIELD', 'ASYNC',
  "this launch call creates the task instance whose type is REPOSITION_FIELD; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_REPOSITION_FIELD', env=None,
  evidence='SRC ModelFieldEditor.java:376; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# REPOSITION_FIELD: ModelFieldEditor$6$1.confirm (ModelFieldEditor.java:388) listener ModelFieldEditor$8 -- mChangeFieldHandler
e('ModelFieldEditor$6$1.confirm', 'DeckTask.doInBackground@REPOSITION_FIELD', 'ASYNC',
  "this launch call creates the task instance whose type is REPOSITION_FIELD; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_REPOSITION_FIELD', env=None,
  evidence='SRC ModelFieldEditor.java:388; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# ADD_FIELD: ModelFieldEditor$2.onPositive (ModelFieldEditor.java:198) listener ModelFieldEditor$8 -- mChangeFieldHandler
e('ModelFieldEditor$2.onPositive', 'DeckTask.doInBackground@ADD_FIELD', 'ASYNC',
  "this launch call creates the task instance whose type is ADD_FIELD; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_ADD_FIELD', env=None,
  evidence='SRC ModelFieldEditor.java:198; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# ADD_FIELD: ModelFieldEditor$2$1.confirm (ModelFieldEditor.java:208) listener ModelFieldEditor$8 -- mChangeFieldHandler
e('ModelFieldEditor$2$1.confirm', 'DeckTask.doInBackground@ADD_FIELD', 'ASYNC',
  "this launch call creates the task instance whose type is ADD_FIELD; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_ADD_FIELD', env=None,
  evidence='SRC ModelFieldEditor.java:208; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# CHANGE_SORT_FIELD: ModelFieldEditor.sortByField (ModelFieldEditor.java:461) listener ModelFieldEditor$8 -- mChangeFieldHandler
e('ModelFieldEditor.sortByField', 'DeckTask.doInBackground@CHANGE_SORT_FIELD', 'ASYNC',
  "this launch call creates the task instance whose type is CHANGE_SORT_FIELD; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_CHANGE_SORT_FIELD', env=None,
  evidence='SRC ModelFieldEditor.java:461; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# CHANGE_SORT_FIELD: ModelFieldEditor$7.confirm (ModelFieldEditor.java:468) listener ModelFieldEditor$8 -- mChangeFieldHandler
e('ModelFieldEditor$7.confirm', 'DeckTask.doInBackground@CHANGE_SORT_FIELD', 'ASYNC',
  "this launch call creates the task instance whose type is CHANGE_SORT_FIELD; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_CHANGE_SORT_FIELD', env=None,
  evidence='SRC ModelFieldEditor.java:468; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# SAVE_MODEL: CardTemplateEditor$CardTemplateFragment.onOptionsItemSelected (CardTemplateEditor.java:512) listener CardTemplateEditor$CardTemplateFragment$2 -- mSaveModelAndExitHandler
e('CardTemplateEditor$CardTemplateFragment.onOptionsItemSelected', 'DeckTask.doInBackground@SAVE_MODEL', 'ASYNC',
  "this launch call creates the task instance whose type is SAVE_MODEL; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_SAVE_MODEL', env=None,
  evidence='SRC CardTemplateEditor.java:512; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# FIND_EMPTY_CARDS: DeckPicker.handleEmptyCards (DeckPicker.java:2172) listener DeckPicker$27 -- DeckTask.Listener, NOT TaskListener; direct dispatch
e('DeckPicker.handleEmptyCards', 'DeckTask.doInBackground@FIND_EMPTY_CARDS', 'ASYNC',
  "this launch call creates the task instance whose type is FIND_EMPTY_CARDS; AsyncTask.execute runs that instance's doInBackground",
  guard='mType == TASK_TYPE_FIND_EMPTY_CARDS', env=None,
  evidence='SRC DeckPicker.java:2172; SRC com/ichi2/async/DeckTask.java:129-134, 203-204; FW-SRC core/java/android/os/AsyncTask.java:594-596, 632-651')

# ================================================================== 2. Body edges (design section 2.3 item 2) =====
# One e() call per variant. Kind CALL. Trigger verbatim: 'switch case for this type only'.
# Evidence: plain SRC over the case line and its return line in DeckTask.java:234-341; the
# return line contains the body name, including the capital-G spellings doInBackGround*.
# Each hand body edge is what suppresses the base auto edge for that body (build_graph.py:
# 216-228), so after all 34 are present the shared DeckTask.doInBackground node has no body
# edges left. The shared node itself is NOT deleted: its onPostExecute hand edge and its
# non-dispatch auto calls stay.
# LOAD_DECK_COUNTS: case DeckTask.java:234, return DeckTask.java:235
e('DeckTask.doInBackground@LOAD_DECK_COUNTS', 'DeckTask.doInBackgroundLoadDeckCounts', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:234-235')

# SAVE_COLLECTION: case DeckTask.java:237, return DeckTask.java:238
e('DeckTask.doInBackground@SAVE_COLLECTION', 'DeckTask.doInBackgroundSaveCollection', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:237-238')

# ANSWER_CARD: case DeckTask.java:240, return DeckTask.java:241
e('DeckTask.doInBackground@ANSWER_CARD', 'DeckTask.doInBackgroundAnswerCard', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:240-241')

# ADD_FACT: case DeckTask.java:243, return DeckTask.java:244
e('DeckTask.doInBackground@ADD_FACT', 'DeckTask.doInBackgroundAddNote', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:243-244')

# UPDATE_FACT: case DeckTask.java:246, return DeckTask.java:247
e('DeckTask.doInBackground@UPDATE_FACT', 'DeckTask.doInBackgroundUpdateNote', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:246-247')

# UNDO: case DeckTask.java:249, return DeckTask.java:250
e('DeckTask.doInBackground@UNDO', 'DeckTask.doInBackgroundUndo', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:249-250')

# SEARCH_CARDS: case DeckTask.java:252, return DeckTask.java:253
e('DeckTask.doInBackground@SEARCH_CARDS', 'DeckTask.doInBackgroundSearchCards', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:252-253')

# DISMISS: case DeckTask.java:255, return DeckTask.java:256
e('DeckTask.doInBackground@DISMISS', 'DeckTask.doInBackgroundDismissNote', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:255-256')

# CHECK_DATABASE: case DeckTask.java:258, return DeckTask.java:259
e('DeckTask.doInBackground@CHECK_DATABASE', 'DeckTask.doInBackgroundCheckDatabase', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:258-259')

# REPAIR_DECK: case DeckTask.java:261, return DeckTask.java:262
e('DeckTask.doInBackground@REPAIR_DECK', 'DeckTask.doInBackgroundRepairDeck', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:261-262')

# UPDATE_VALUES_FROM_DECK: case DeckTask.java:264, return DeckTask.java:265
e('DeckTask.doInBackground@UPDATE_VALUES_FROM_DECK', 'DeckTask.doInBackgroundUpdateValuesFromDeck', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:264-265')

# DELETE_DECK: case DeckTask.java:267, return DeckTask.java:268
e('DeckTask.doInBackground@DELETE_DECK', 'DeckTask.doInBackgroundDeleteDeck', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:267-268')

# REBUILD_CRAM: case DeckTask.java:270, return DeckTask.java:271
e('DeckTask.doInBackground@REBUILD_CRAM', 'DeckTask.doInBackgroundRebuildCram', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:270-271')

# EMPTY_CRAM: case DeckTask.java:273, return DeckTask.java:274
e('DeckTask.doInBackground@EMPTY_CRAM', 'DeckTask.doInBackgroundEmptyCram', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:273-274')

# IMPORT: case DeckTask.java:276, return DeckTask.java:277
e('DeckTask.doInBackground@IMPORT', 'DeckTask.doInBackgroundImportAdd', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:276-277')

# IMPORT_REPLACE: case DeckTask.java:279, return DeckTask.java:280
e('DeckTask.doInBackground@IMPORT_REPLACE', 'DeckTask.doInBackgroundImportReplace', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:279-280')

# EXPORT_APKG: case DeckTask.java:282, return DeckTask.java:283
e('DeckTask.doInBackground@EXPORT_APKG', 'DeckTask.doInBackgroundExportApkg', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:282-283')

# REORDER: case DeckTask.java:285, return DeckTask.java:286
e('DeckTask.doInBackground@REORDER', 'DeckTask.doInBackgroundReorder', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:285-286')

# CONF_CHANGE: case DeckTask.java:288, return DeckTask.java:289
e('DeckTask.doInBackground@CONF_CHANGE', 'DeckTask.doInBackgroundConfChange', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:288-289')

# CONF_RESET: case DeckTask.java:291, return DeckTask.java:292
e('DeckTask.doInBackground@CONF_RESET', 'DeckTask.doInBackgroundConfReset', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:291-292')

# CONF_REMOVE: case DeckTask.java:294, return DeckTask.java:295
e('DeckTask.doInBackground@CONF_REMOVE', 'DeckTask.doInBackgroundConfRemove', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:294-295')

# CONF_SET_SUBDECKS: case DeckTask.java:297, return DeckTask.java:298
e('DeckTask.doInBackground@CONF_SET_SUBDECKS', 'DeckTask.doInBackgroundConfSetSubdecks', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:297-298')

# RENDER_BROWSER_QA: case DeckTask.java:300, return DeckTask.java:301
e('DeckTask.doInBackground@RENDER_BROWSER_QA', 'DeckTask.doInBackgroundRenderBrowserQA', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:300-301')

# CHECK_MEDIA: case DeckTask.java:303, return DeckTask.java:304
e('DeckTask.doInBackground@CHECK_MEDIA', 'DeckTask.doInBackgroundCheckMedia', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:303-304')

# ADD_TEMPLATE: case DeckTask.java:306, return DeckTask.java:307
e('DeckTask.doInBackground@ADD_TEMPLATE', 'DeckTask.doInBackgroundAddTemplate', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:306-307')

# REMOVE_TEMPLATE: case DeckTask.java:309, return DeckTask.java:310
e('DeckTask.doInBackground@REMOVE_TEMPLATE', 'DeckTask.doInBackgroundRemoveTemplate', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:309-310')

# COUNT_MODELS: case DeckTask.java:312, return DeckTask.java:313
e('DeckTask.doInBackground@COUNT_MODELS', 'DeckTask.doInBackgroundCountModels', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:312-313')

# DELETE_MODEL: case DeckTask.java:315, return DeckTask.java:316
e('DeckTask.doInBackground@DELETE_MODEL', 'DeckTask.doInBackGroundDeleteModel', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:315-316')

# DELETE_FIELD: case DeckTask.java:318, return DeckTask.java:319
e('DeckTask.doInBackground@DELETE_FIELD', 'DeckTask.doInBackGroundDeleteField', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:318-319')

# REPOSITION_FIELD: case DeckTask.java:321, return DeckTask.java:322
e('DeckTask.doInBackground@REPOSITION_FIELD', 'DeckTask.doInBackGroundRepositionField', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:321-322')

# ADD_FIELD: case DeckTask.java:324, return DeckTask.java:325
e('DeckTask.doInBackground@ADD_FIELD', 'DeckTask.doInBackGroundAddField', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:324-325')

# CHANGE_SORT_FIELD: case DeckTask.java:327, return DeckTask.java:328
e('DeckTask.doInBackground@CHANGE_SORT_FIELD', 'DeckTask.doInBackgroundChangeSortField', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:327-328')

# SAVE_MODEL: case DeckTask.java:330, return DeckTask.java:331
e('DeckTask.doInBackground@SAVE_MODEL', 'DeckTask.doInBackgroundSaveModel', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:330-331')

# FIND_EMPTY_CARDS: case DeckTask.java:332, return DeckTask.java:333
e('DeckTask.doInBackground@FIND_EMPTY_CARDS', 'DeckTask.doInBackGroundFindEmptyCards', 'CALL', 'switch case for this type only',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:332-333')

# ================================================================== 3. Post chains (design section 2.3 item 3) =====
# Design section 2.3 item 3 requires the post chain for LOAD_DECK_COUNTS in scope and permits
# other types as their routes require. This file supplies the post chain for ALL 34 types from
# the design's own _POST_LISTENERS table (section 2.3 item 5), so no type's post delivery is
# left on the shared chain after the split: listener sets are unions over all sites of the type
# (design section 2.6), never per-site. Trimming to LOAD-only does not change any section 3
# verdict except that it leaves other types' post routes on the shared chain; it must not be
# done silently -- the merger must record a trim in its report. Evidence per design section
# 2.3 item 3: variant -> onPostExecute@T ASYNC, DeckTask.java:360-362 plus AsyncTask finish
# lines 691-695; onPostExecute@T -> TaskListener@T CALL, DeckTask.java:362, 1305-1306;
# TaskListener@T -> listener CALL, DeckTask.java:1306. FIND_EMPTY_CARDS is the exception: its
# listener DeckPicker$27 is a DeckTask.Listener, not a TaskListener, and is dispatched directly
# (design section 2.1, edge Ed329ba67), so its chain ends with a direct onPostExecute@T -> $27
# edge and no TaskListener@T hop. No post chain is written for a type with an empty set; every
# type in the design table has a non-empty post set, so all 34 appear here.
# Post chain LOAD_DECK_COUNTS
e('DeckTask.doInBackground@LOAD_DECK_COUNTS', 'DeckTask.onPostExecute@LOAD_DECK_COUNTS', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@LOAD_DECK_COUNTS', 'DeckTask$TaskListener.onPostExecute@LOAD_DECK_COUNTS', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@LOAD_DECK_COUNTS', 'DeckPicker$22.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain SAVE_COLLECTION
e('DeckTask.doInBackground@SAVE_COLLECTION', 'DeckTask.onPostExecute@SAVE_COLLECTION', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@SAVE_COLLECTION', 'DeckTask$TaskListener.onPostExecute@SAVE_COLLECTION', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@SAVE_COLLECTION', 'UIUtils$1.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain ANSWER_CARD
e('DeckTask.doInBackground@ANSWER_CARD', 'DeckTask.onPostExecute@ANSWER_CARD', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@ANSWER_CARD', 'DeckTask$TaskListener.onPostExecute@ANSWER_CARD', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@ANSWER_CARD', 'AbstractFlashcardViewer$10.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain ADD_FACT
e('DeckTask.doInBackground@ADD_FACT', 'DeckTask.onPostExecute@ADD_FACT', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@ADD_FACT', 'DeckTask$TaskListener.onPostExecute@ADD_FACT', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@ADD_FACT', 'NoteEditor$1.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain UPDATE_FACT
e('DeckTask.doInBackground@UPDATE_FACT', 'DeckTask.onPostExecute@UPDATE_FACT', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@UPDATE_FACT', 'DeckTask$TaskListener.onPostExecute@UPDATE_FACT', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@UPDATE_FACT', 'AbstractFlashcardViewer$9.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')
e('DeckTask$TaskListener.onPostExecute@UPDATE_FACT', 'CardBrowser$13.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain UNDO
e('DeckTask.doInBackground@UNDO', 'DeckTask.onPostExecute@UNDO', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@UNDO', 'DeckTask$TaskListener.onPostExecute@UNDO', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@UNDO', 'DeckPicker$13.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')
e('DeckTask$TaskListener.onPostExecute@UNDO', 'AbstractFlashcardViewer$10.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain SEARCH_CARDS
e('DeckTask.doInBackground@SEARCH_CARDS', 'DeckTask.onPostExecute@SEARCH_CARDS', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@SEARCH_CARDS', 'DeckTask$TaskListener.onPostExecute@SEARCH_CARDS', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@SEARCH_CARDS', 'CardBrowser$16.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain DISMISS
e('DeckTask.doInBackground@DISMISS', 'DeckTask.onPostExecute@DISMISS', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@DISMISS', 'DeckTask$TaskListener.onPostExecute@DISMISS', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@DISMISS', 'AbstractFlashcardViewer$8.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')
e('DeckTask$TaskListener.onPostExecute@DISMISS', 'CardBrowser$14.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')
e('DeckTask$TaskListener.onPostExecute@DISMISS', 'CardBrowser$15.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain CHECK_DATABASE
e('DeckTask.doInBackground@CHECK_DATABASE', 'DeckTask.onPostExecute@CHECK_DATABASE', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@CHECK_DATABASE', 'DeckTask$TaskListener.onPostExecute@CHECK_DATABASE', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@CHECK_DATABASE', 'DeckPicker$15.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain REPAIR_DECK
e('DeckTask.doInBackground@REPAIR_DECK', 'DeckTask.onPostExecute@REPAIR_DECK', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@REPAIR_DECK', 'DeckTask$TaskListener.onPostExecute@REPAIR_DECK', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@REPAIR_DECK', 'DeckPicker$14.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain UPDATE_VALUES_FROM_DECK
e('DeckTask.doInBackground@UPDATE_VALUES_FROM_DECK', 'DeckTask.onPostExecute@UPDATE_VALUES_FROM_DECK', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@UPDATE_VALUES_FROM_DECK', 'DeckTask$TaskListener.onPostExecute@UPDATE_VALUES_FROM_DECK', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@UPDATE_VALUES_FROM_DECK', 'StudyOptionsFragment$3.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain DELETE_DECK
e('DeckTask.doInBackground@DELETE_DECK', 'DeckTask.onPostExecute@DELETE_DECK', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@DELETE_DECK', 'DeckTask$TaskListener.onPostExecute@DELETE_DECK', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@DELETE_DECK', 'DeckPicker$24.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain REBUILD_CRAM
e('DeckTask.doInBackground@REBUILD_CRAM', 'DeckTask.onPostExecute@REBUILD_CRAM', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@REBUILD_CRAM', 'DeckTask$TaskListener.onPostExecute@REBUILD_CRAM', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@REBUILD_CRAM', 'DeckPicker$25.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')
e('DeckTask$TaskListener.onPostExecute@REBUILD_CRAM', 'StudyOptionsFragment$3.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')
e('DeckTask$TaskListener.onPostExecute@REBUILD_CRAM', 'CustomStudyDialog$4.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain EMPTY_CRAM
e('DeckTask.doInBackground@EMPTY_CRAM', 'DeckTask.onPostExecute@EMPTY_CRAM', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@EMPTY_CRAM', 'DeckTask$TaskListener.onPostExecute@EMPTY_CRAM', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@EMPTY_CRAM', 'DeckPicker$25.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')
e('DeckTask$TaskListener.onPostExecute@EMPTY_CRAM', 'StudyOptionsFragment$3.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain IMPORT
e('DeckTask.doInBackground@IMPORT', 'DeckTask.onPostExecute@IMPORT', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@IMPORT', 'DeckTask$TaskListener.onPostExecute@IMPORT', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@IMPORT', 'DeckPicker$5.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain IMPORT_REPLACE
e('DeckTask.doInBackground@IMPORT_REPLACE', 'DeckTask.onPostExecute@IMPORT_REPLACE', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@IMPORT_REPLACE', 'DeckTask$TaskListener.onPostExecute@IMPORT_REPLACE', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@IMPORT_REPLACE', 'DeckPicker$6.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain EXPORT_APKG
e('DeckTask.doInBackground@EXPORT_APKG', 'DeckTask.onPostExecute@EXPORT_APKG', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@EXPORT_APKG', 'DeckTask$TaskListener.onPostExecute@EXPORT_APKG', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@EXPORT_APKG', 'DeckPicker$7.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain REORDER
e('DeckTask.doInBackground@REORDER', 'DeckTask.onPostExecute@REORDER', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@REORDER', 'DeckTask$TaskListener.onPostExecute@REORDER', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@REORDER', 'DeckOptions$DeckPreferenceHack$Editor$2.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain CONF_CHANGE
e('DeckTask.doInBackground@CONF_CHANGE', 'DeckTask.onPostExecute@CONF_CHANGE', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@CONF_CHANGE', 'DeckTask$TaskListener.onPostExecute@CONF_CHANGE', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@CONF_CHANGE', 'DeckOptions$DeckPreferenceHack$Editor$2.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain CONF_RESET
e('DeckTask.doInBackground@CONF_RESET', 'DeckTask.onPostExecute@CONF_RESET', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@CONF_RESET', 'DeckTask$TaskListener.onPostExecute@CONF_RESET', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@CONF_RESET', 'DeckOptions$DeckPreferenceHack$Editor$2.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain CONF_REMOVE
e('DeckTask.doInBackground@CONF_REMOVE', 'DeckTask.onPostExecute@CONF_REMOVE', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@CONF_REMOVE', 'DeckTask$TaskListener.onPostExecute@CONF_REMOVE', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@CONF_REMOVE', 'DeckOptions$DeckPreferenceHack$Editor$2.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain CONF_SET_SUBDECKS
e('DeckTask.doInBackground@CONF_SET_SUBDECKS', 'DeckTask.onPostExecute@CONF_SET_SUBDECKS', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@CONF_SET_SUBDECKS', 'DeckTask$TaskListener.onPostExecute@CONF_SET_SUBDECKS', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@CONF_SET_SUBDECKS', 'DeckOptions$DeckPreferenceHack$Editor$2.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain RENDER_BROWSER_QA
e('DeckTask.doInBackground@RENDER_BROWSER_QA', 'DeckTask.onPostExecute@RENDER_BROWSER_QA', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@RENDER_BROWSER_QA', 'DeckTask$TaskListener.onPostExecute@RENDER_BROWSER_QA', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@RENDER_BROWSER_QA', 'CardBrowser$17.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain CHECK_MEDIA
e('DeckTask.doInBackground@CHECK_MEDIA', 'DeckTask.onPostExecute@CHECK_MEDIA', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@CHECK_MEDIA', 'DeckTask$TaskListener.onPostExecute@CHECK_MEDIA', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@CHECK_MEDIA', 'DeckPicker$16.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain ADD_TEMPLATE
e('DeckTask.doInBackground@ADD_TEMPLATE', 'DeckTask.onPostExecute@ADD_TEMPLATE', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@ADD_TEMPLATE', 'DeckTask$TaskListener.onPostExecute@ADD_TEMPLATE', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@ADD_TEMPLATE', 'CardTemplateEditor$1.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain REMOVE_TEMPLATE
e('DeckTask.doInBackground@REMOVE_TEMPLATE', 'DeckTask.onPostExecute@REMOVE_TEMPLATE', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@REMOVE_TEMPLATE', 'DeckTask$TaskListener.onPostExecute@REMOVE_TEMPLATE', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@REMOVE_TEMPLATE', 'CardTemplateEditor$1.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain COUNT_MODELS
e('DeckTask.doInBackground@COUNT_MODELS', 'DeckTask.onPostExecute@COUNT_MODELS', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@COUNT_MODELS', 'DeckTask$TaskListener.onPostExecute@COUNT_MODELS', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@COUNT_MODELS', 'ModelBrowser$1.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain DELETE_MODEL
e('DeckTask.doInBackground@DELETE_MODEL', 'DeckTask.onPostExecute@DELETE_MODEL', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@DELETE_MODEL', 'DeckTask$TaskListener.onPostExecute@DELETE_MODEL', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@DELETE_MODEL', 'ModelBrowser$2.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain DELETE_FIELD
e('DeckTask.doInBackground@DELETE_FIELD', 'DeckTask.onPostExecute@DELETE_FIELD', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@DELETE_FIELD', 'DeckTask$TaskListener.onPostExecute@DELETE_FIELD', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@DELETE_FIELD', 'ModelFieldEditor$8.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain REPOSITION_FIELD
e('DeckTask.doInBackground@REPOSITION_FIELD', 'DeckTask.onPostExecute@REPOSITION_FIELD', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@REPOSITION_FIELD', 'DeckTask$TaskListener.onPostExecute@REPOSITION_FIELD', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@REPOSITION_FIELD', 'ModelFieldEditor$8.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain ADD_FIELD
e('DeckTask.doInBackground@ADD_FIELD', 'DeckTask.onPostExecute@ADD_FIELD', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@ADD_FIELD', 'DeckTask$TaskListener.onPostExecute@ADD_FIELD', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@ADD_FIELD', 'ModelFieldEditor$8.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain CHANGE_SORT_FIELD
e('DeckTask.doInBackground@CHANGE_SORT_FIELD', 'DeckTask.onPostExecute@CHANGE_SORT_FIELD', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@CHANGE_SORT_FIELD', 'DeckTask$TaskListener.onPostExecute@CHANGE_SORT_FIELD', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@CHANGE_SORT_FIELD', 'ModelFieldEditor$8.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain SAVE_MODEL
e('DeckTask.doInBackground@SAVE_MODEL', 'DeckTask.onPostExecute@SAVE_MODEL', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@SAVE_MODEL', 'DeckTask$TaskListener.onPostExecute@SAVE_MODEL', 'CALL',
  'onPostExecute forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362, 1305-1306')
e('DeckTask$TaskListener.onPostExecute@SAVE_MODEL', 'CardTemplateEditor$CardTemplateFragment$2.onPostExecute', 'CALL',
  'the TaskListener adapter forwards to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1306')

# Post chain FIND_EMPTY_CARDS
e('DeckTask.doInBackground@FIND_EMPTY_CARDS', 'DeckTask.onPostExecute@FIND_EMPTY_CARDS', 'ASYNC',
  'the worker result is delivered to onPostExecute on the UI thread (AsyncTask finish)',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695')
e('DeckTask.onPostExecute@FIND_EMPTY_CARDS', 'DeckPicker$27.onPostExecute', 'CALL',
  'onPostExecute forwards directly to the DeckTask.Listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:362')

# ================================================================== 4. Progress chains (design section 2.3 item 4) ===
# Required by design section 2.3 item 4: ANSWER_CARD, UPDATE_FACT, DISMISS, RENDER_BROWSER_QA.
# Additional chains in this section (ADD_FACT, UNDO, SEARCH_CARDS, IMPORT_REPLACE) are NOT
# design section 2.3 item 4 scope; they are included because their publishProgress evidence is
# already in the tree (graph_def_mod/01.py, part 069) and their _PROG_LISTENERS sets in the
# design are non-empty. The merger may drop the additional four without affecting any section 3
# verdict; dropping any of the required four breaks routes 12 / 20 / 30 as designed.
# Structure per type: body -> onProgressUpdate@T (ASYNC, existing body evidence with the dst
# variant), onProgressUpdate@T -> TaskListener@T (CALL, DeckTask.java:352-355, 1311-1312),
# TaskListener@T -> listener (CALL, DeckTask.java:1312). Types with an empty design progress
# set get NO progress chain here: LOAD_DECK_COUNTS (body at DeckTask.java:480-491 publishes
# nothing), SAVE_COLLECTION, CHECK_DATABASE, REPAIR_DECK, UPDATE_VALUES_FROM_DECK, DELETE_DECK,
# REBUILD_CRAM, EMPTY_CRAM, EXPORT_APKG, REORDER, CONF_CHANGE, CONF_RESET, CONF_REMOVE,
# CONF_SET_SUBDECKS, CHECK_MEDIA, ADD_TEMPLATE, REMOVE_TEMPLATE, COUNT_MODELS, DELETE_MODEL,
# DELETE_FIELD, REPOSITION_FIELD, ADD_FIELD, CHANGE_SORT_FIELD, SAVE_MODEL, FIND_EMPTY_CARDS.
# IMPORT gets no body progress chain: its progress goes through doProgress (DeckTask.java:1348-
# 1350, callback created in doInBackgroundImportAdd at :750), not through a direct body ->
# onProgressUpdate edge, so a direct body edge here would be a false edge. Its $5 progress
# fan-out is still pruned by the EDIT clause to the IMPORT set.
# Progress chain ANSWER_CARD (REQUIRED; publishProgress at DeckTask.java:457)
e('DeckTask.doInBackgroundAnswerCard', 'DeckTask.onProgressUpdate@ANSWER_CARD', 'ASYNC',
  'publishProgress posts progress to onProgressUpdate on the UI thread',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:455-458, 352-355')
e('DeckTask.onProgressUpdate@ANSWER_CARD', 'DeckTask$TaskListener.onProgressUpdate@ANSWER_CARD', 'CALL',
  'onProgressUpdate forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:352-355, 1311-1312')
e('DeckTask$TaskListener.onProgressUpdate@ANSWER_CARD', 'AbstractFlashcardViewer$10.onProgressUpdate', 'CALL',
  'the TaskListener adapter forwards progress to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1312')

# Progress chain UPDATE_FACT (REQUIRED; publishProgress at DeckTask.java:420 and 422)
e('DeckTask.doInBackgroundUpdateNote', 'DeckTask.onProgressUpdate@UPDATE_FACT', 'ASYNC',
  'publishProgress posts progress to onProgressUpdate on the UI thread',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:418-423, 352-355')
e('DeckTask.onProgressUpdate@UPDATE_FACT', 'DeckTask$TaskListener.onProgressUpdate@UPDATE_FACT', 'CALL',
  'onProgressUpdate forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:352-355, 1311-1312')
e('DeckTask$TaskListener.onProgressUpdate@UPDATE_FACT', 'AbstractFlashcardViewer$9.onProgressUpdate', 'CALL',
  'the TaskListener adapter forwards progress to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1312')
e('DeckTask$TaskListener.onProgressUpdate@UPDATE_FACT', 'CardBrowser$13.onProgressUpdate', 'CALL',
  'the TaskListener adapter forwards progress to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1312')

# Progress chain DISMISS (REQUIRED; publishProgress at DeckTask.java:565)
e('DeckTask.doInBackgroundDismissNote', 'DeckTask.onProgressUpdate@DISMISS', 'ASYNC',
  'publishProgress posts progress to onProgressUpdate on the UI thread',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:563-566, 352-355')
e('DeckTask.onProgressUpdate@DISMISS', 'DeckTask$TaskListener.onProgressUpdate@DISMISS', 'CALL',
  'onProgressUpdate forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:352-355, 1311-1312')
e('DeckTask$TaskListener.onProgressUpdate@DISMISS', 'AbstractFlashcardViewer$8.onProgressUpdate', 'CALL',
  'the TaskListener adapter forwards progress to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1312')
e('DeckTask$TaskListener.onProgressUpdate@DISMISS', 'CardBrowser$14.onProgressUpdate', 'CALL',
  'the TaskListener adapter forwards progress to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1312')
e('DeckTask$TaskListener.onProgressUpdate@DISMISS', 'CardBrowser$15.onProgressUpdate', 'CALL',
  'the TaskListener adapter forwards progress to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1312')

# Progress chain RENDER_BROWSER_QA (REQUIRED; publishProgress at DeckTask.java:659)
e('DeckTask.doInBackgroundRenderBrowserQA', 'DeckTask.onProgressUpdate@RENDER_BROWSER_QA', 'ASYNC',
  'publishProgress posts progress to onProgressUpdate on the UI thread',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:657-660, 352-355')
e('DeckTask.onProgressUpdate@RENDER_BROWSER_QA', 'DeckTask$TaskListener.onProgressUpdate@RENDER_BROWSER_QA', 'CALL',
  'onProgressUpdate forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:352-355, 1311-1312')
e('DeckTask$TaskListener.onProgressUpdate@RENDER_BROWSER_QA', 'CardBrowser$17.onProgressUpdate', 'CALL',
  'the TaskListener adapter forwards progress to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1312')

# Progress chain ADD_FACT (ADDITIONAL, tree-verified; publishProgress at DeckTask.java:380)
e('DeckTask.doInBackgroundAddNote', 'DeckTask.onProgressUpdate@ADD_FACT', 'ASYNC',
  'publishProgress posts progress to onProgressUpdate on the UI thread',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:378-381, 352-355')
e('DeckTask.onProgressUpdate@ADD_FACT', 'DeckTask$TaskListener.onProgressUpdate@ADD_FACT', 'CALL',
  'onProgressUpdate forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:352-355, 1311-1312')
e('DeckTask$TaskListener.onProgressUpdate@ADD_FACT', 'NoteEditor$1.onProgressUpdate', 'CALL',
  'the TaskListener adapter forwards progress to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1312')

# Progress chain UNDO (ADDITIONAL, tree-verified; publishProgress at DeckTask.java:601)
e('DeckTask.doInBackgroundUndo', 'DeckTask.onProgressUpdate@UNDO', 'ASYNC',
  'publishProgress posts progress to onProgressUpdate on the UI thread',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:599-602, 352-355')
e('DeckTask.onProgressUpdate@UNDO', 'DeckTask$TaskListener.onProgressUpdate@UNDO', 'CALL',
  'onProgressUpdate forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:352-355, 1311-1312')
e('DeckTask$TaskListener.onProgressUpdate@UNDO', 'DeckPicker$13.onProgressUpdate', 'CALL',
  'the TaskListener adapter forwards progress to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1312')
e('DeckTask$TaskListener.onProgressUpdate@UNDO', 'AbstractFlashcardViewer$10.onProgressUpdate', 'CALL',
  'the TaskListener adapter forwards progress to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1312')

# Progress chain SEARCH_CARDS (ADDITIONAL, tree-verified; publishProgress at DeckTask.java:633)
e('DeckTask.doInBackgroundSearchCards', 'DeckTask.onProgressUpdate@SEARCH_CARDS', 'ASYNC',
  'publishProgress posts progress to onProgressUpdate on the UI thread',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:629-634, 352-355')
e('DeckTask.onProgressUpdate@SEARCH_CARDS', 'DeckTask$TaskListener.onProgressUpdate@SEARCH_CARDS', 'CALL',
  'onProgressUpdate forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:352-355, 1311-1312')
e('DeckTask$TaskListener.onProgressUpdate@SEARCH_CARDS', 'CardBrowser$16.onProgressUpdate', 'CALL',
  'the TaskListener adapter forwards progress to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1312')

# Progress chain IMPORT_REPLACE (ADDITIONAL, tree-verified; publishProgress at DeckTask.java:809 and 859)
e('DeckTask.doInBackgroundImportReplace', 'DeckTask.onProgressUpdate@IMPORT_REPLACE', 'ASYNC',
  'publishProgress posts progress to onProgressUpdate on the UI thread',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:805-810, 855-860, 352-355')
e('DeckTask.onProgressUpdate@IMPORT_REPLACE', 'DeckTask$TaskListener.onProgressUpdate@IMPORT_REPLACE', 'CALL',
  'onProgressUpdate forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:352-355, 1311-1312')
e('DeckTask$TaskListener.onProgressUpdate@IMPORT_REPLACE', 'DeckPicker$6.onProgressUpdate', 'CALL',
  'the TaskListener adapter forwards progress to the registered listener for this type',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:1312')

# ================================================================== 5. Connection split (design section 3.7) ======
# Exactly two branches. Single SYNC entry, from Connection.sync (NOT from DeckPicker.
# sync(String): the withdrawn second SYNC specification in the old design must not be used,
# because it would break the section 3.7(d) tie argument). Single LOGIN entry, from the login
# call site MyAccount.login (graph name has no parentheses; design section 3.7 writes it as
# MyAccount.login() in prose). Both entries bypass launchConnectionTask only, not their own
# callers. No Connection post/progress variant chain is needed for route 02: EasyX509 is
# reached through the SYNC body's callees (Syncer.sync -> meta -> req chain), before any
# onPostExecute listener. Guard texts for Connection entries are DERIVED, not design-verbatim:
# the design gives no Connection guard string; Connection stores the branch in
# Payload.taskType (Connection.java:161 for LOGIN, :167 for SYNC, field at :504), so the
# guard text mirrors the DeckTask form with that field. The merger/auditor must confirm the
# derived guard wording before building; it is guard text only, never a costed gate.
# SYNC entry (section 3.7(c)):
e('Connection.sync', 'Connection.doInBackground@SYNC', 'ASYNC',
  "this sync call creates the Connection task instance whose type is SYNC; AsyncTask.execute runs that instance's doInBackground",
  guard='data.taskType == TASK_TYPE_SYNC', env=None,
  evidence='SRC com/ichi2/async/Connection.java:166-168; SRC com/ichi2/async/Connection.java:83-100, 173-179')

# LOGIN entry (section 3.7(c); call at MyAccount.java:140, inside MyAccount.java:125-143,
# non-empty username/password branch at :139-140; the :135 call is commented out):
e('MyAccount.login', 'Connection.doInBackground@LOGIN', 'ASYNC',
  "this login call creates the Connection task instance whose type is LOGIN; AsyncTask.execute runs that instance's doInBackground",
  guard='data.taskType == TASK_TYPE_LOGIN', env=None,
  evidence='SRC com/ichi2/anki/MyAccount.java:140; SRC com/ichi2/async/Connection.java:160-162, 83-100, 173-179')

# Middle hops (Connection.java:178):
e('Connection.doInBackground@SYNC', 'Connection.doOneInBackground@SYNC', 'CALL',
  'doInBackground delegates to doOneInBackground', env=None,
  evidence='SRC com/ichi2/async/Connection.java:178')
e('Connection.doInBackground@LOGIN', 'Connection.doOneInBackground@LOGIN', 'CALL',
  'doInBackground delegates to doOneInBackground', env=None,
  evidence='SRC com/ichi2/async/Connection.java:178')

# Body edges, hand-covered so the base auto edges E2d0c2ced (SYNC) and E9250c2b8 (LOGIN) are
# suppressed for the shared node as well (build_graph.py:216-228):
e('Connection.doOneInBackground@SYNC', 'Connection.doInBackgroundSync', 'CALL', 'switch case for this branch only',
  env=None, evidence='SRC com/ichi2/async/Connection.java:187-188')
e('Connection.doOneInBackground@LOGIN', 'Connection.doInBackgroundLogin', 'CALL', 'switch case for this branch only',
  env=None, evidence='SRC com/ichi2/async/Connection.java:184-185')

# ================================================================== 6. Route 12 hand edge (design section 3.3(c)) ==
# NEW edge, not an existing edge: AbstractFlashcardViewer$8.onProgressUpdate currently has only
# the skipped self-loop E093d8ba2 in the graph. The self-loop is left in place (harmless,
# skipped by cheapest because src == dst); it is NOT deleted. Evidence is plain SRC, never a
# bytecode citation (design section 3.3(c)). Trigger verbatim from design section 3.3(c).
# Without this edge the DISMISS progress chain ends at $8 and DISMISS cannot compete for
# route 12 at all; with it, DISMISS reaches $10 in one extra hop and ANSWER wins by that hop.
e('AbstractFlashcardViewer$8.onProgressUpdate', 'AbstractFlashcardViewer$10.onProgressUpdate', 'CALL',
  '`$8` forwards progress to the registered answer-card handler',
  env=None, evidence='SRC AbstractFlashcardViewer.java:491-492')

# End of DeckTask / Connection variant fragment. Companion file EDIT-wrapper-decktask.py must be
# appended to graph_def.py after the current final EDIT; without it, fan-out copies of unsplit
# bodies/listeners survive as live splices (design section 0 point 1, section 2.3 item 5).
# ---- Dialog/hook variants (routes 05, 07, 19) ----
# Dialog-id and hook-name variant edges for AnkiDroid routes 05, 07, 19.
#
# Source design (read-only, applied by the merger after independent audit):
#   helper/design-dialog-hook/DESIGN.md (revised version, revision note D1-D6)
#   helper/design-dialog-hook/REAUDIT.md (overall PASS, defect list empty)
# Baseline in the design: methods 4186, edges 9183, REACHABLE 3275,
# UNREACHABLE 911, errors 0, warnings 0.
#
# HOW TO APPLY THIS FILE
#   Append the e() calls below, in this order, as part of
#   graphs/AnkiDroid/graph_def_mod/02.py. The file is executed in the
#   graph_def.py namespace, so e() (and SCREENS, if it were needed) are
#   already defined; nothing is imported or defined here.
#   Do NOT add a second EDIT definition (the single chained EDIT in
#   graph_def.py already applies to every edge).
#
# WHAT IS DELIBERATELY NOT IN THIS FILE
#   - No sup() calls. Design section 0 and section 4 item 1: hand-edge
#     suppression already fires for every pair below, so sup() for these
#     pairs would be redundant. Suppression of the old auto edges is
#     automatic once the hand edges below exist.
#   - No SCREENS additions. No new page node is required for BFS for any
#     of the three routes (design sections 1(c), 2(c), 3(c)).
#   - No generic newInstance(int,long) -> newInstance(int,long,boolean)
#     restoration. That restoration is DROPPED by design decision D5
#     (see section 1 restorations below); do not re-add it.
#   - No deletion of the existing direct hand edge
#     Stats.calculateDue(Context,AxisType) -> AdvancedStatistics.runFilter
#     (Edf6d8bd0, graph_def_mod/01.py, part 100). A 02.py fragment cannot
#     delete an edge: the builder's edge list is not exposed to mod files
#     (only e() is), and mod files are executed in sorted order after
#     01.py. The merger MUST delete that one e() block from 01.py as a
#     separate edit, or route 19 will still take the direct edge and the
#     design's 34-step route (and the 9244 edge count) will not hold.
#     See CHECKLIST.md for the exact block to delete.
#   - No generic restorations for route 19. Every route-19 moved edge is
#     suppressed with no restoration by design (section 3 below).
#   - No change to the generic lifecycle edge E90f59cc0
#     (CustomStudyDialog.<init> -> CustomStudyDialog.onCreateDialog).
#     Its androidx wording is LEFT ALONE by design decision D2; the new
#     @0/@101 lifecycle edges below deliberately use the correct
#     support-v4 wording verbatim instead of copying the generic wording.
#   - No new edge ids are predicted here. Variant edges get new ids from
#     the builder at build time; restoration edges keep the auto edge
#     ids noted in their comments only because they are written
#     byte-identically to the auto edges they replace (same trigger,
#     guard, evidence, env, needs_state, and no guard/env/state gate).
#
# ORDER NOTE (tie, design section 1(d))
#   Within each route section below, variant edges come first, then
#   generic restoration edges, following the order of the tables in
#   design sections 1(c), 2(c), 3(c). Do NOT reorder these calls without
#   re-auditing: CustomStudyDialog.getText1 / buildInputDialog (and,
#   through them, getText2, getDefaultValue, $2.<init>, $3.<init>) TIE
#   between the generic-restoration chain and the @101 chain at equal
#   cost, so the winner depends on hand-edge order. Either outcome is
#   acceptable and route 05's target is reached only through
#   getText1@101 regardless, but the merger MUST report which chain won
#   on the real build. The audit simulation, in which restorations were
#   listed first and the generic chain won, does NOT predict the winner
#   for this file's variant-first order; neither outcome is presented
#   here as guaranteed.
#
# TRIGGER WORDING (not specified in the design tables)
#   The design tables specify kind, guard, and evidence for each edge,
#   but not the trigger string. Triggers below copy the corresponding
#   auto edge's trigger where one exists: 'Direct call' for direct
#   bytecode calls, 'Virtual/interface call that can dispatch to this
#   implementation' for interface/registry dispatch (the auto cha
#   trigger), and 'lifecycle callback of <Class> (DialogFragment)' for
#   the lifecycle edges (copied from the generic lifecycle edges).
#   No cls/via is set on any edge below, so CALL edges take the default
#   class 'explicit', exactly as the auto edges they replace or mirror
#   (design section 0). See CHECKLIST.md for the full mapping.

# ======================================================================
# Section 1 (design 1(c)): Route 05 - Sched.totalRevForCurrentDeck
# Variant edges, @0 (first instance, id 0) and @101 (second instance,
# CUSTOM_STUDY_REV = 101). New ids are assigned by the builder.
# ======================================================================

# 1-V01: first-instance entry from the study-options context menu.
e('StudyOptionsFragment.showCustomStudyContextMenu',
  'CustomStudyDialog.newInstance(int,long)@0', 'CALL', 'Direct call',
  guard='id == CONTEXT_MENU_STANDARD (0)',
  evidence='SRC StudyOptionsFragment.java:273 (bytecode)')

# 1-V02: first-instance entry from the deck-picker context menu.
e('DeckPickerContextMenu$1.onSelection',
  'CustomStudyDialog.newInstance(int,long)@0', 'CALL', 'Direct call',
  guard='id == CONTEXT_MENU_STANDARD (0)',
  evidence='SRC dialogs/DeckPickerContextMenu.java:135 (bytecode)')

# 1-V03: @0 chain, 2-arg newInstance delegates to the 3-arg overload.
e('CustomStudyDialog.newInstance(int,long)@0',
  'CustomStudyDialog.newInstance(int,long,boolean)@0', 'CALL', 'Direct call',
  guard='id == 0, passed through',
  evidence='SRC CustomStudyDialog.java:79 (bytecode)')

# 1-V04: @0 chain, 3-arg newInstance constructs the dialog.
e('CustomStudyDialog.newInstance(int,long,boolean)@0',
  'CustomStudyDialog.<init>@0', 'CALL', 'Direct call',
  guard='id == 0, passed through',
  evidence='SRC CustomStudyDialog.java:83 (bytecode)')

# 1-V05: @0 lifecycle. Evidence VERBATIM as INFERRED support-v4 text
# (NOT plain SRC, and NOT the generic E90f59cc0 androidx wording, which
# is left alone by design decision D2).
e('CustomStudyDialog.<init>@0',
  'CustomStudyDialog.onCreateDialog@0', 'LIFECYCLE',
  'lifecycle callback of CustomStudyDialog (DialogFragment)',
  evidence='INFERRED support-v4 Fragment/DialogFragment lifecycle order (support-v4 source not read; CustomStudyDialog imports android.support.v4.app.DialogFragment); SRC com/ichi2/anki/dialogs/CustomStudyDialog.java:94')

# 1-V06: @0 chain, id 0 takes the context-menu branch (< 100).
e('CustomStudyDialog.onCreateDialog@0',
  'CustomStudyDialog.buildContextMenu', 'CALL', 'Direct call',
  guard='dialogId == 0 (< 100)',
  evidence='SRC CustomStudyDialog.java:100 (bytecode)')

# 1-V07: second-instance entry, context-menu pick CUSTOM_STUDY_REV.
e('CustomStudyDialog$1.onSelection',
  'CustomStudyDialog.newInstance(int,long,boolean)@101', 'CALL', 'Direct call',
  guard='user picks CUSTOM_STUDY_REV (101) from the context menu',
  evidence='SRC CustomStudyDialog.java:184 (bytecode)')

# 1-V08: @101 chain, 3-arg newInstance constructs the dialog.
e('CustomStudyDialog.newInstance(int,long,boolean)@101',
  'CustomStudyDialog.<init>@101', 'CALL', 'Direct call',
  guard='id == 101, passed through',
  evidence='SRC CustomStudyDialog.java:83 (bytecode)')

# 1-V09: @101 lifecycle. Evidence VERBATIM as INFERRED support-v4 text
# (same string as 1-V05; NOT plain SRC; NOT the generic androidx wording).
e('CustomStudyDialog.<init>@101',
  'CustomStudyDialog.onCreateDialog@101', 'LIFECYCLE',
  'lifecycle callback of CustomStudyDialog (DialogFragment)',
  evidence='INFERRED support-v4 Fragment/DialogFragment lifecycle order (support-v4 source not read; CustomStudyDialog imports android.support.v4.app.DialogFragment); SRC com/ichi2/anki/dialogs/CustomStudyDialog.java:94')

# 1-V10: @101 chain, id 101 takes the input-dialog branch (>= 100).
e('CustomStudyDialog.onCreateDialog@101',
  'CustomStudyDialog.buildInputDialog@101', 'CALL', 'Direct call',
  guard='dialogId == 101 (>= 100)',
  evidence='SRC CustomStudyDialog.java:102 (bytecode)')

# 1-V11: @101 chain, buildInputDialog always calls getText1.
e('CustomStudyDialog.buildInputDialog@101',
  'CustomStudyDialog.getText1@101', 'CALL', 'Direct call',
  guard='dialogId == 101, passed through',
  evidence='SRC CustomStudyDialog.java:211 (bytecode)')

# 1-V12: @101 chain, getText1 case CUSTOM_STUDY_REV reaches the target.
# This hand edge suppresses the generic auto edge E0ca39dd5
# (getText1 -> totalRev); E0ca39dd5 is NOT restored, so after the edit
# this is the ONLY incoming edge to Sched.totalRevForCurrentDeck.
e('CustomStudyDialog.getText1@101',
  'Sched.totalRevForCurrentDeck', 'CALL', 'Direct call',
  guard='dialogId == CUSTOM_STUDY_REV (101)',
  evidence='SRC CustomStudyDialog.java:363 (bytecode)')

# --- Section 1 generic restorations (design 1(c)) ---
# Each edge below is byte-identical to the auto edge it replaces
# (trigger 'Direct call', guard None, evidence as shown, env None,
# needs_state None), so it keeps that auto edge's id. These keep other
# dialog ids working after the @ edges above suppress the auto edges
# globally. Restoration edges must NOT acquire a variant guard: that
# would change their ids and misdescribe the generic call.
# Checked against graph_def.py at translation time: none of these
# (src, dst) pairs is a B6_GUARD / B6FIX_GUARD key and none matches a
# B3_FIX / B6FIX_EVIDENCE / B6_EVIDENCE (src, dst, old-evidence) key,
# so the single chained EDIT does not alter them; the merger must
# re-check this at merge time (design section 0).

# 1-R01: restores auto E2c327703 (CustomStudyDialog.java:83).
e('CustomStudyDialog.newInstance(int,long,boolean)',
  'CustomStudyDialog.<init>', 'CALL', 'Direct call',
  guard=None, env=None,
  evidence='SRC CustomStudyDialog.java:83 (bytecode)')

# 1-R02: restores auto Ec6b33a80 (CustomStudyDialog.java:100).
e('CustomStudyDialog.onCreateDialog',
  'CustomStudyDialog.buildContextMenu', 'CALL', 'Direct call',
  guard=None, env=None,
  evidence='SRC CustomStudyDialog.java:100 (bytecode)')

# 1-R03: restores auto Eab9aa442 (CustomStudyDialog.java:102).
e('CustomStudyDialog.onCreateDialog',
  'CustomStudyDialog.buildInputDialog', 'CALL', 'Direct call',
  guard=None, env=None,
  evidence='SRC CustomStudyDialog.java:102 (bytecode)')

# 1-R04: restores auto Eb7b12863 (CustomStudyDialog.java:211).
e('CustomStudyDialog.buildInputDialog',
  'CustomStudyDialog.getText1', 'CALL', 'Direct call',
  guard=None, env=None,
  evidence='SRC CustomStudyDialog.java:211 (bytecode)')

# 1-R05 (implicit in design 1(c), counted in the re-audit's 5 route-05
# restorations): restores auto Eda5cc9ae (CustomStudyDialog.java:184),
# so default-branch picks other than 101 (100, 102-106) still flow
# generically. The @101 hand edge 1-V07 suppresses the auto edge; this
# restoration is what keeps those other picks working.
e('CustomStudyDialog$1.onSelection',
  'CustomStudyDialog.newInstance(int,long,boolean)', 'CALL', 'Direct call',
  guard=None, env=None,
  evidence='SRC CustomStudyDialog.java:184 (bytecode)')

# D5 DROP (design 1(c), revision note D5): the generic restoration
# CustomStudyDialog.newInstance(int,long) ->
# CustomStudyDialog.newInstance(int,long,boolean) (auto Ecf5cf491,
# CustomStudyDialog.java:79) is DROPPED and is NOT written here.
# Both generic 2-arg callers are retargeted to @0 by 1-V01 and 1-V02,
# so no generic 2-arg caller remains; the edge would be a dead
# placeholder. The base method stays REACHABLE through its @0 variant.
# Counting effect: hand +33, not +34; net +61, edges 9244, not +62/9245.

# ======================================================================
# Section 2 (design 2(c)): Route 07 - libanki.Utils$1.<init>
# Variant edges, @SELECT (DIALOG_IMPORT_SELECT = 1). New ids are
# assigned by the builder.
# ======================================================================

# 2-V01: HINT dialog positive button asks for the SELECT dialog.
# Trigger copies the auto edge's interface-dispatch trigger
# (auto E2821c117, ImportDialog.java:76).
e('ImportDialog$1.onPositive',
  'DeckPicker.showImportDialog(int)@SELECT', 'CALL',
  'Virtual/interface call that can dispatch to this implementation',
  guard='HINT dialog positive: showImportDialog(DIALOG_IMPORT_SELECT)',
  evidence='SRC ImportDialog.java:76 (bytecode)')

# 2-V02: @SELECT chain, 1-arg showImportDialog delegates to 2-arg.
e('DeckPicker.showImportDialog(int)@SELECT',
  'DeckPicker.showImportDialog(int,String)@SELECT', 'CALL', 'Direct call',
  guard='id == DIALOG_IMPORT_SELECT, passed through',
  evidence='SRC DeckPicker.java:1089 (bytecode)')

# 2-V03: @SELECT chain, 2-arg showImportDialog creates the dialog.
e('DeckPicker.showImportDialog(int,String)@SELECT',
  'ImportDialog.newInstance@SELECT', 'CALL', 'Direct call',
  guard='id == DIALOG_IMPORT_SELECT, passed through',
  evidence='SRC DeckPicker.java:1095 (bytecode)')

# 2-V04: @SELECT chain, newInstance constructs the dialog.
e('ImportDialog.newInstance@SELECT',
  'ImportDialog.<init>@SELECT', 'CALL', 'Direct call',
  guard='dialogType == DIALOG_IMPORT_SELECT, passed through',
  evidence='SRC ImportDialog.java:49 (bytecode)')

# 2-V05: @SELECT lifecycle. Evidence VERBATIM as the generic E88404d0f
# string (INFERRED, not plain SRC).
e('ImportDialog.<init>@SELECT',
  'ImportDialog.onCreateDialog@SELECT', 'LIFECYCLE',
  'lifecycle callback of ImportDialog (DialogFragment)',
  evidence='INFERRED support-v4 Fragment/DialogFragment lifecycle order (support-v4 source not read; ImportDialog imports android.support.v4.app.DialogFragment); SRC com/ichi2/anki/dialogs/ImportDialog.java:59')

# 2-V06: @SELECT chain, SELECT case reaches the target's caller.
# This hand edge suppresses the generic auto edge Ee61e1dd8
# (onCreateDialog -> getImportableDecks); Ee61e1dd8 is NOT restored, so
# after the edit this is the ONLY incoming edge to
# libanki.Utils.getImportableDecks. The existing target edge
# Ecb463f10 (getImportableDecks -> libanki.Utils$1.<init>) is unchanged.
e('ImportDialog.onCreateDialog@SELECT',
  'libanki.Utils.getImportableDecks', 'CALL', 'Direct call',
  guard='mType == DIALOG_IMPORT_SELECT',
  evidence='SRC ImportDialog.java:88 (bytecode)')

# --- Section 2 generic restorations (design 2(c)) ---
# Byte-identical to the auto edges they replace (same rules as section
# 1 restorations); EDIT-key check as in section 1: none of these
# (src, dst) pairs is a B6_GUARD / B6FIX_GUARD key or a B3_FIX /
# B6FIX_EVIDENCE / B6_EVIDENCE key at translation time; re-check at
# merge time. Note the B6_GUARD entry for
# (ImportDialog.onCreateDialog, libanki.Utils.getImportableDecks) does
# NOT touch any restoration below, because that pair is suppressed
# without restoration, not restored.

# 2-R01: restores auto E0ca886ae (DeckPicker.java:1089).
e('DeckPicker.showImportDialog(int)',
  'DeckPicker.showImportDialog(int,String)', 'CALL', 'Direct call',
  guard=None, env=None,
  evidence='SRC DeckPicker.java:1089 (bytecode)')

# 2-R02: restores auto Eb7dfd04d (DeckPicker.java:1095).
e('DeckPicker.showImportDialog(int,String)',
  'ImportDialog.newInstance', 'CALL', 'Direct call',
  guard=None, env=None,
  evidence='SRC DeckPicker.java:1095 (bytecode)')

# 2-R03: restores auto E2da7107c (ImportDialog.java:49).
e('ImportDialog.newInstance',
  'ImportDialog.<init>', 'CALL', 'Direct call',
  guard=None, env=None,
  evidence='SRC ImportDialog.java:49 (bytecode)')

# ======================================================================
# Section 3 (design 3(c)): Route 19 - AdvancedStatistics$Card.setIvl
# Variant edges, @ + hook-name string. New ids are assigned by the
# builder. There are NO generic restorations in this section: every
# moved auto edge below is suppressed with no restoration.
# ======================================================================

# 3-V01: Statistics call site, hook name advancedStatistics.
# Suppresses auto Ea34eba66 (Stats.calculateDue -> Hooks.runFilter);
# no generic restoration for this source (its only runFilter call is
# Stats.java:311, with "advancedStatistics").
e('Stats.calculateDue(Context,AxisType)',
  'Hooks.runFilter@advancedStatistics', 'CALL', 'Direct call',
  guard='hook name == "advancedStatistics"',
  evidence='SRC Stats.java:311 (bytecode)')

# 3-V02: _renderQA call site, hook name mungeQA.
# Together with 3-V03, suppresses auto Ed1de7fa0
# (_renderQA -> Hooks.runFilter); no generic restoration for this
# source (its runFilter calls are only :1008 mungeFields and :1010
# mungeQA). auto_calls.json holds only ONE (_renderQA, Hooks.runFilter)
# record, at line 1010; the :1008 call has no auto record of its own,
# so in net effect 3-V03 suppresses nothing beyond what 3-V02 already
# suppresses (design 3(c), audit D5 rewording).
e('Collection._renderQA(Object[],String,String)',
  'Hooks.runFilter@mungeQA', 'CALL', 'Direct call',
  guard='hook name == "mungeQA"',
  evidence='SRC Collection.java:1010 (bytecode)')

# 3-V03: _renderQA call site, hook name mungeFields.
e('Collection._renderQA(Object[],String,String)',
  'Hooks.runFilter@mungeFields', 'CALL', 'Direct call',
  guard='hook name == "mungeFields"',
  evidence='SRC Collection.java:1008 (bytecode)')

# 3-V04: @advancedStatistics dispatch to the sole installer.
# Suppresses auto E70b0401a (Hooks.runFilter ->
# AdvancedStatistics.runFilter); no generic restoration. Guard carries
# the MG943 precondition text VERBATIM from deleted Edf6d8bd0's note
# (design 3(c), audit D3), after the registry-list guard. Evidence is
# PLAIN SRC, NOT (bytecode): the install lines do not contain a
# runFilter call, so a (bytecode) citation here would create a
# check-4 problem (design 3(d)).
e('Hooks.runFilter@advancedStatistics',
  'AdvancedStatistics.runFilter', 'CALL',
  'Virtual/interface call that can dispatch to this implementation',
  guard='registry list for key "advancedStatistics" (sole installer AdvancedStatistics.install); MISSING GATE MG943: the preference advanced_statistics_enabled (default false, Hooks.java:61) must be true for AdvancedStatistics to be installed. Without it, calculateDue(AxisType) at Stats.java:331 runs instead.',
  evidence='SRC com/ichi2/libanki/hooks/AdvancedStatistics.java:147-148; SRC com/ichi2/libanki/hooks/Hooks.java:138-150')

# 3-V05: @mungeQA dispatch to ChessFilter.
# Suppresses auto E6e2b0570 (Hooks.runFilter -> ChessFilter.runFilter);
# no generic restoration. Plain SRC evidence, as in 3-V04.
e('Hooks.runFilter@mungeQA',
  'ChessFilter.runFilter', 'CALL',
  'Virtual/interface call that can dispatch to this implementation',
  guard='registry list for key "mungeQA"',
  evidence='SRC com/ichi2/libanki/hooks/ChessFilter.java:65; SRC com/ichi2/libanki/hooks/Hooks.java:138-150')

# 3-V06: @mungeQA dispatch to HebrewFixFilter.
# Suppresses auto E556f3436 (Hooks.runFilter -> HebrewFixFilter.runFilter);
# no generic restoration. Plain SRC evidence, as in 3-V04.
e('Hooks.runFilter@mungeQA',
  'HebrewFixFilter.runFilter', 'CALL',
  'Virtual/interface call that can dispatch to this implementation',
  guard='registry list for key "mungeQA"',
  evidence='SRC com/ichi2/libanki/hooks/HebrewFixFilter.java:32; SRC com/ichi2/libanki/hooks/Hooks.java:138-150')

# 3-V07: @mungeQA dispatch to LaTeX$LaTeXFilter.
# Suppresses auto E96397a0b (Hooks.runFilter -> LaTeX$LaTeXFilter.runFilter);
# no generic restoration. Plain SRC evidence, as in 3-V04. Note the
# LaTeX path is com/ichi2/libanki/LaTeX.java, not hooks/.
e('Hooks.runFilter@mungeQA',
  'LaTeX$LaTeXFilter.runFilter', 'CALL',
  'Virtual/interface call that can dispatch to this implementation',
  guard='registry list for key "mungeQA"',
  evidence='SRC com/ichi2/libanki/LaTeX.java:115; SRC com/ichi2/libanki/hooks/Hooks.java:138-150')

# Hooks.runFilter@mungeFields gets NO outgoing hand edge, deliberately
# (design 3(c)): no addHook("mungeFields", ...) exists anywhere in the
# app sources, so the registry list for that key is empty and dispatch
# returns the argument unchanged. The dead-end variant node is faithful,
# not an error: it is not a method in method_list.json (its base is),
# so the builder's unknown-node checks do not apply to it.
#
# Unchanged by this file (design 3(c), "edges that STAY"): the generic
# Template.render_unescaped -> Hooks.runFilter edge (Ee203e69a,
# Template.java:274, dynamic "fmod_" + mod), the generic Hooks.runFilter
# -> FuriganaFilters / HintFilter / Hook.runFilter auto edges, the
# Hooks.getInstance -> Hooks.<init> -> AdvancedStatistics.install chain,
# and the whole AdvancedStatistics.runFilter tail (including
# E66c764f8 and the 7-edge tail). The generic Hooks.runFilter node
# itself stays REACHABLE through Template.
#
# End of dialog/hook variant fragment: 25 variant/dispatch edges
# (12 route 05 + 6 route 07 + 7 route 19) + 8 generic restorations
# (5 route 05 + 3 route 07) = 33 hand edges in this file.
# Combined with the separate Edf6d8bd0 deletion in graph_def_mod/01.py,
# the design's expectation for this design's portion alone is:
# hand +33, removed 21 (20 suppressed autos + 1 deleted hand edge),
# replicated autos +49, net +61, edges 9183 -> 9244. The real combined
# build count will differ because the other two designs also change
# edges; do not force the build to 9244 (design section 4 item 2).

# ---- Best-route Set G (routes 03, 13, 14, 18, 21, 26, 28) ----
# ============================================================================
# AnkiDroid Stream A — Set G best-route edits (DESIGN.md reworked version,
# as re-audited PASS in REAUDIT.md with apply-time defect D1 fixed below).
#
# HOW TO USE THIS FILE (merger read this first):
# - This is a code FRAGMENT, ready to append as part of
#   graphs/AnkiDroid/graph_def_mod/02.py. It is NOT a standalone graph
#   definition: it assumes the builder namespace already provides e(),
#   sup() and SCREENS, exactly as graph_def_mod/01.py uses them.
# - It NEVER touches the merger tree, NEVER pushes, and contains NO edit
#   to the single EDIT definition. There is no EDIT code in this file at
#   all: no EDIT assignment, no EDIT call, no EDIT override.
# - NEW-* placeholder ids from the design are NOT real ids and are NEVER
#   used here. Every new edge below is added by (src, dst, kind,
#   evidence, guard) only; real edge ids are content hashes assigned on
#   rebuild. Re-printed routes must be matched by node sequence and
#   costs, not by placeholder ids (design section 0.4).
# - ATOMICITY (design sections 0.6 and 8): apply each group WHOLE, in a
#   single rebuild, with the merger actions in the MERGER-ACTION blocks.
#   Do NOT push a partially applied set. In particular:
#     * Group 1 suppressions without the six NEW producer edges strand
#       six listeners; Group 2 deletions without the variant entry flip
#       Reviewer; Group 3 section 2c without section 4c leaves route
#       18's generic-page RESULT shortcut intact, and 4c without 2c
#       leaves its CardBrowser shortcut intact.
#     * The family components (Group 1, Group 2, Group 3) are jointly
#       atomic for the seven-route outcome (REAUDIT section 9
#       clarification): applying one alone is label-safe but does not
#       achieve the claimed routes.
#     * Route 21's summary edge is genuinely independent (no removal).
#     * Route 14 Option A (section 6 below) is SEPARABLE and
#       ACCEPTANCE-GATED: apply it only with explicit coordinator
#       acceptance (see section 6 and CHECKLIST.md). Omitting it does
#       not break the other groups; route 14 then stays WRONG.
# - HAND DELETIONS CANNOT BE DONE BY THIS FRAGMENT ALONE. Adding code
#   cannot remove an earlier e() call. The three MERGER-ACTION blocks
#   below state the exact lines the merger must DELETE from their
#   source files. sup() is NOT used for those deletions: sup() only
#   removes auto (bytecode) edges, and the deleted edges are
#   hand-written (design sections 0.1C, 2c, 4c). If the merger applies
#   only this fragment without those deletions, the hand edges remain
#   and the claimed routes will NOT result. Do not dress a MERGER-ACTION
#   deletion up as a sup() call.
# - CONSTRAINTS honoured in this file (design section 0.2):
#     * single EDIT untouched; no tools/ edit; no out/ or .github/ write.
#     * no second route-11 call-site edge; no route-08 edge of any kind
#       (the CardBrowser$16 edge in Group 1 is the SEARCH_CARDS
#       producer edge from design section 0.1A.2, not a route-08 edge).
#     * no suppression of any of the 16 confirm + 8 cancel dispatch
#       edges (in particular Eb104f8cb and E5bc5ca78 are untouched).
#     * Ecba7dfd7 stays ENV_NETWORK (untouched here).
#     * route-26 step-5 guard stays :958-only (untouched here).
#     * Eba94fbde (DeckTask switch arm to RenderBrowserQA) is NOT
#       suppressed (see Group 3).
# ============================================================================


# ============================================================================
# GROUP 1 — TaskListener family (design sections 0.1A, 0.1B, 0.5).
# Atomic group: 28 base suppressions + 28 D1 @-variant suppressions
# + six NEW producer edges + $24 suppression + $24 summary edge.
# ============================================================================

# --- 1A. Suppress all 28 DeckTask$TaskListener.onPostExecute interface
# pairs (design section 0.5). Verified against
# graphs/AnkiDroid/out/ankidroid_trigger_graph.json before transcription:
# all 28 base ids below match (src, dst) exactly, 0 mismatches.
# src for every row is DeckTask$TaskListener.onPostExecute, evidence
# DeckTask.java:1306 (bytecode) for all. Printed reason (design
# section 0.5, record verbatim in the graph comment and AGENT_NOTES.md):
# each auto edge is the bytecode extractor's unguarded interface
# dispatch (DeckTask.java:1306 is the mListener.onPostExecute call
# site, DeckTask.java:362); the implementation is registered only by
# the producer(s) in the section 0.5 table, each of which already has
# (or, for the six NEW rows, is given here) a direct ASYNC delivery
# edge. A task launched by any other producer registers a different
# listener. The interface node itself stays REACHABLE (via
# DeckTask.onPostExecute, Eee369b5f); only its fan-out is removed.
# A pair-suppression below suppresses ONE (src, dst) pair only, never
# the interface node itself. The $13 / $8 / $1 pairs in sections 1c /
# 6c / 7c of the design are the SAME pairs as in this list: do not
# add them a second time (design section 8, step 1).
sup(('DeckTask$TaskListener.onPostExecute', 'AbstractFlashcardViewer$10.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute', 'AbstractFlashcardViewer$8.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute', 'AbstractFlashcardViewer$9.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute', 'CardBrowser$13.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute', 'CardBrowser$14.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute', 'CardBrowser$15.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute', 'CardBrowser$16.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute', 'CardBrowser$17.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute', 'CardTemplateEditor$1.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute', 'CardTemplateEditor$CardTemplateFragment$2.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute', 'CustomStudyDialog$4.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute', 'DeckOptions$DeckPreferenceHack$Editor$2.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute', 'DeckPicker$13.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute', 'DeckPicker$14.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute', 'DeckPicker$15.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute', 'DeckPicker$16.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute', 'DeckPicker$22.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute', 'DeckPicker$24.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute', 'DeckPicker$25.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute', 'DeckPicker$5.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute', 'DeckPicker$6.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute', 'DeckPicker$7.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute', 'ModelBrowser$1.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute', 'ModelBrowser$2.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute', 'ModelFieldEditor$8.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute', 'NoteEditor$1.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute', 'StudyOptionsFragment$3.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute', 'UIUtils$1.onPostExecute'))

# --- 1A-D1. APPLY-TIME FIX for REAUDIT defect D1 (read this before
# believing the design's section 0.1A / 0.4 mechanism sentence).
# The design claims sup() on a base TaskListener pair kills the 28
# variant copies too. That claim is FALSE: the 28 variant edges are
# separate auto_calls.json entries, not products of the add_auto_edges
# duplication loop, and the suppression check compares the auto call's
# own (src, dst) pair, so a base pair does not match an @-suffixed
# pair. The graph's own precedent proves the authors knew this:
# graph_def.py lines 437-442 and 3626-3627 list BOTH the base and the
# @ pairs for onProgressUpdate suppressions, in exactly the form used
# below (src 'DeckTask$TaskListener.onPostExecute@<Listener>',
# dst '<Listener>.onPostExecute').
# Fix implemented here (REAUDIT D1, first branch): add the 28 @ pairs
# to the sup() list explicitly, so the variant copies are removed too.
# Count consequence (see CHECKLIST.md): a base-only build would
# remove 35 edges, not 63; WITH the @ pairs below, the removal count
# is 63, as the design's tables state (58 sup() removals + 5 hand
# deletions). Verified against out JSON: all 28 @-variant edges exist
# as separate CALL entries (e.g. DeckPicker$13 variant E4581eb48), and
# all 28 variant source nodes have ZERO incoming edges, so they are
# inert and removing them cannot change any best route (REAUDIT
# section 1: real-build approximation differs from the design
# simulation in 0 best routes).
sup(('DeckTask$TaskListener.onPostExecute@AbstractFlashcardViewer$10', 'AbstractFlashcardViewer$10.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute@AbstractFlashcardViewer$8', 'AbstractFlashcardViewer$8.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute@AbstractFlashcardViewer$9', 'AbstractFlashcardViewer$9.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute@CardBrowser$13', 'CardBrowser$13.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute@CardBrowser$14', 'CardBrowser$14.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute@CardBrowser$15', 'CardBrowser$15.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute@CardBrowser$16', 'CardBrowser$16.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute@CardBrowser$17', 'CardBrowser$17.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute@CardTemplateEditor$1', 'CardTemplateEditor$1.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute@CardTemplateEditor$CardTemplateFragment$2', 'CardTemplateEditor$CardTemplateFragment$2.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute@CustomStudyDialog$4', 'CustomStudyDialog$4.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute@DeckOptions$DeckPreferenceHack$Editor$2', 'DeckOptions$DeckPreferenceHack$Editor$2.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute@DeckPicker$13', 'DeckPicker$13.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute@DeckPicker$14', 'DeckPicker$14.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute@DeckPicker$15', 'DeckPicker$15.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute@DeckPicker$16', 'DeckPicker$16.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute@DeckPicker$22', 'DeckPicker$22.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute@DeckPicker$24', 'DeckPicker$24.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute@DeckPicker$25', 'DeckPicker$25.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute@DeckPicker$5', 'DeckPicker$5.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute@DeckPicker$6', 'DeckPicker$6.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute@DeckPicker$7', 'DeckPicker$7.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute@ModelBrowser$1', 'ModelBrowser$1.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute@ModelBrowser$2', 'ModelBrowser$2.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute@ModelFieldEditor$8', 'ModelFieldEditor$8.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute@NoteEditor$1', 'NoteEditor$1.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute@StudyOptionsFragment$3', 'StudyOptionsFragment$3.onPostExecute'),
    ('DeckTask$TaskListener.onPostExecute@UIUtils$1', 'UIUtils$1.onPostExecute'))

# --- 1A.2. Six NEW producer ASYNC edges (design section 0.1A.2).
# Atomic with the suppressions above: suppressing all 28 without
# these would flip these six REACHABLE listeners to no-route, because
# each has ZERO non-interface direct incoming edges in the baseline
# JSON (verified). Each edge is a direct ASYNC summary of a printed
# launch site, in the exact form of the existing direct edges.
# $13 is mUpdateCardHandler (field at CardBrowser.java:900, body
# :915-924); launched with mUpdateCardHandler at :697 (EDIT_CARD
# result branch).
e('CardBrowser.onActivityResult', 'CardBrowser$13.onPostExecute', 'ASYNC',
  'the UPDATE_FACT task finishes and calls its listener',
  evidence='SRC com/ichi2/anki/CardBrowser.java:697')
# $14 is mSuspendCardHandler (field at :1000, body :1012-1022);
# launched at :181 (CONTEXT_MENU_SUSPEND, TASK_TYPE_DISMISS +
# SUSPEND_CARD).
e('CardBrowser$1.onSelection', 'CardBrowser$14.onPostExecute', 'ASYNC',
  'the DISMISS (suspend) task finishes and calls its listener',
  evidence='SRC com/ichi2/anki/CardBrowser.java:181')
# $15 is mDeleteNoteHandler (field at :1028, body :1040-1048);
# launched at :199 (delete-confirm positive button,
# TASK_TYPE_DISMISS + DELETE_NOTE).
e('CardBrowser$1$1.onClick', 'CardBrowser$15.onPostExecute', 'ASYNC',
  'the DISMISS (delete) task finishes and calls its listener',
  evidence='SRC com/ichi2/anki/CardBrowser.java:199')
# $16 is mSearchCardsHandler (field at :1051, body :1067-1079).
# Launched with mSearchCardsHandler inside searchCards() at :812-813
# (TASK_TYPE_SEARCH_CARDS); searchCards() itself is called from
# onActivityResult and the search UI, so the listener's other callers
# reach it through searchCards, not through the interface.
e('CardBrowser.searchCards', 'CardBrowser$16.onPostExecute', 'ASYNC',
  'the SEARCH_CARDS task finishes and calls its listener',
  evidence='SRC com/ichi2/anki/CardBrowser.java:812-813')
# $14 is the anonymous listener created inside repairDeck()
# (TASK_TYPE_REPAIR_DECK at :1112, onPostExecute dismissing the
# progress dialog and calling onCollectionLoadError on failure).
# Its siblings $15 (integrityCheck, E748990b0) and $16 (mediaCheck,
# Ecf295e7b) already have direct edges; $14 was the only one missing.
e('DeckPicker.repairDeck', 'DeckPicker$14.onPostExecute', 'ASYNC',
  'the REPAIR_DECK task finishes and calls its listener',
  evidence='SRC com/ichi2/anki/DeckPicker.java:1112')
# $2 is mSaveModelAndExitHandler (field at :563, body :576-589:
# setResult + finishWithAnimation on success).
# Launched with it at :512 (action_confirm, modelHasChanged(),
# TASK_TYPE_SAVE_MODEL).
e('CardTemplateEditor$CardTemplateFragment.onOptionsItemSelected',
  'CardTemplateEditor$CardTemplateFragment$2.onPostExecute', 'ASYNC',
  'the SAVE_MODEL task finishes and calls its listener',
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:512')

# --- 1B. $24 layout flip (design section 0.1B). Atomic pair:
# suppression + summary edge together.
# Suppress the auto pair DeckPicker$24.onPostExecute ->
# DeckPicker.openStudyOptions (E931f7818, auto CALL, evidence
# DeckPicker.java:2042). The $24 call sits inside
# if (mFragmented && removingCurrent) (DeckPicker.java:2040-2042),
# and openStudyOptions itself branches on the same flag (:1695-1703:
# fragmented -> loadStudyOptionsFragment (:1698); phone ->
# StudyOptionsActivity (:1699-1703)). BFS ignores both guards and
# composes the fragmented head with the phone continuation, which
# cannot hold on one run. $24's genuine direct edge
# (DeckPicker.deleteDeck -> $24, E57dce628) and its updateDeckList
# branch (E41dfe9a6) are UNAFFECTED by this suppression.
sup(('DeckPicker$24.onPostExecute', 'DeckPicker.openStudyOptions'))
# Summary edge for the ONLY continuation that call can actually take.
# This is a genuine summary of an existing delegation
# ($24 -> openStudyOptions -> loadStudyOptionsFragment under
# mFragmented and removingCurrent). It is NOT dressed up as a direct
# call: $24 does not call loadStudyOptionsFragment directly; the edge
# summarises the delegation, exactly as the route-21 summary-edge
# mechanism does (design section 5). It preserves $24's genuine
# continuation; it is not a shortcut: in simulation it is used by
# 0 best routes, because $24's best route ends at $24 itself and its
# downstream routes take the updateDeckList branch E41dfe9a6, which
# is unaffected. Other openStudyOptions callers (handleDeckSelection,
# onCreateCustomStudySession, $12.onPositive, S_DECKPICKER GUI) are
# layout-agnostic and are not touched: they still reach both branches
# through the base node, exactly as before.
e('DeckPicker$24.onPostExecute', 'DeckPicker.loadStudyOptionsFragment', 'ASYNC',
  'in fragmented mode, $24 openStudyOptions reloads the study options fragment',
  guard='mFragmented and removingCurrent, DeckPicker.java:2040-2042',
  evidence='SRC com/ichi2/anki/DeckPicker.java:2040-2042; SRC com/ichi2/anki/DeckPicker.java:1695-1698')


# ============================================================================
# GROUP 2 — Reviewer receiver (design section 0.1C).
# Atomic group: delete three base-onCreate hand edges + add the
# receiver-variant entry chain. Deletion alone would flip Reviewer.
# ============================================================================

# --- 2-MERGER-ACTION (NOT executable code — do NOT convert to sup()).
# DELETE the following three hand-written edges from
# graphs/AnkiDroid/graph_def_mod/01.py, part 137 (lines about 4188-4217
# in the merger tree read for this task). The design specifies DELETION
# of these hand edges; it does NOT specify sup() for them, and sup()
# must NOT be used: sup() only removes auto edges, and these are hand
# edges. Deletion mechanism, exactly as designed: remove the three e()
# statements from part 137.
#   (a) AbstractFlashcardViewer.onCreate -> Reviewer.onCollectionLoaded
#       (Ee2fb37d3, hand ASYNC). Its own note says it was written
#       from the base node because AnkiActivity.onLoadFinished@Reviewer
#       has no inbound edge. Receiver-inconsistent: the base onCreate
#       node is shared by Reviewer's own onCreate (Reviewer does not
#       override onCreate) and by Previewer.onCreate calling
#       super.onCreate (Previewer.java:39, auto E9bb6dca5), so a
#       Previewer chain could traverse it into Reviewer's loader
#       callback, while Previewer's own callback is
#       Previewer.onCollectionLoaded (Ecb6f2b21).
#   (b) AbstractFlashcardViewer.onCreate -> Reviewer.restorePreferences
#       (E3e5784f2, hand CALL; Reviewer.java:396-397 overrides it).
#   (c) AbstractFlashcardViewer.onCreate -> Reviewer.getContentViewAttr
#       (Ea1ef11ff, hand CALL; Reviewer.java:82 overrides it).
# Nothing is lost by these deletions: restorePreferences and
# getContentViewAttr stay reachable via the variant's own auto edges
# (see below), and onCollectionLoaded stays reachable via the new
# ASYNC edge below. Previewer chains can no longer reach any of the
# three, because Previewer never enters onCreate@Reviewer (its chain
# is Previewer.<init> -> Previewer.onCreate ->
# Previewer.onCollectionLoaded).
# --- END 2-MERGER-ACTION ---

# --- 2-ADD. Entry into the EXISTING receiver-variant node
# AbstractFlashcardViewer.onCreate@Reviewer (design section 0.1C).
# This node is a declared receiver variant in auto_calls.json, with
# zero incoming edges in the baseline JSON and existing auto outgoing
# edges to Reviewer.restorePreferences, Reviewer.getContentViewAttr,
# AnkiActivity.startLoadingCollection, and others. Receiver variants
# are EXCLUDED from the hand-variant duplication set in add_auto_edges
# (variants are built only from @ nodes not in receiver), so entering
# it does not duplicate base onCreate edges onto it or onto Previewer.
# Consequence, disclosed plainly (design section 0.1C): the variant
# entry shortens the Reviewer chain by one step (it bypasses the
# AFV.<init> node, whose listener-creation edges remain reachable
# through the retained Reviewer.<init> -> AFV.<init> edge).
# Simulated: Reviewer.onCollectionLoaded 12 steps via these two edges
# (env none, state data); restorePreferences and getContentViewAttr
# 12 steps via the entry edge + their existing variant auto edges.
e('Reviewer.<init>', 'AbstractFlashcardViewer.onCreate@Reviewer', 'LIFECYCLE',
  'the framework calls the base onCreate implementation with a Reviewer receiver',
  evidence='SRC com/ichi2/anki/Reviewer.java:56; SRC com/ichi2/anki/AbstractFlashcardViewer.java:849-859')
e('AbstractFlashcardViewer.onCreate@Reviewer', 'Reviewer.onCollectionLoaded', 'ASYNC',
  'the collection finishes loading and the loader calls onCollectionLoaded on the Reviewer (AnkiActivity.onLoadFinished dispatch)',
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:859; SRC com/ichi2/anki/AnkiActivity.java:255-262, 283-290; SRC com/ichi2/anki/Reviewer.java:96-98')


# ============================================================================
# GROUP 3 — Route-13 <clinit> deletion + route-18 Previewer for-result
# split TOGETHER (design sections 2c + 4c). Atomic group: section 2c
# without 4c leaves route 18's generic-page RESULT shortcut intact;
# 4c without 2c leaves route 18's CardBrowser shortcut intact.
# ============================================================================

# --- 3-MERGER-ACTION (NOT executable code — do NOT convert to sup()).
# DELETE the following hand-written edge from graphs/AnkiDroid/
# graph_def.py, part 009 block (lines about 1502-1510 in the merger
# tree read for this task). The design specifies DELETION; it states
# explicitly "do not sup() it — sup() only removes auto edges; this
# edge is hand-written, so deletion is the mechanism".
#   CardBrowser.<clinit> -> CardBrowser.<init> (Eefecf867, hand
#   FRAMEWORK, 'newInstance constructs the instance after the class
#   is initialized', evidence FW-SRC Instrumentation.java:1170-1174;
#   SRC CardBrowser.java:121, 134-135).
# Printed reason for the deletion (record in the graph comment
# replacing it, and in AGENT_NOTES.md): a static method call
# (CardBrowser.updateSearchItemQA at DeckTask.java:652) triggers
# <clinit> but never constructs an Activity instance; the framework
# newInstance path this edge's evidence cites runs when an activity
# is LAUNCHED, and that launch is already represented by the INTENT
# edges DeckPicker.openCardBrowser -> CardBrowser.<init> (E0e89f361),
# Reviewer.openCardBrowser -> CardBrowser.<init> (E5285c072), and
# NavigationDrawerActivity.openCardBrowser -> CardBrowser.<init>
# (Efa2a7c95). The <clinit> node itself stays reachable (from
# S_DECKPICKER -> CardBrowser.<clinit>, E58e7e755, and from
# RenderBrowserQA's static call), so CardBrowser.<clinit>'s label
# does not change; only the <clinit>-as-instantiation traversal
# disappears. This deletion is Eefecf867 ONLY.
# --- 3-NOT-SUPPRESSED. Eba94fbde (DeckTask.doInBackground ->
# DeckTask.doInBackgroundRenderBrowserQA, switch arm) is NOT
# suppressed, and E3f1b0491 (static-call <clinit> edge) is NOT
# suppressed either. The switch arm is genuine when launched from
# CardBrowser, and no replacement chain exists for its downstream
# routes; after the <clinit> deletion above it dead-ends for
# instantiation (its only route to CardBrowser.<init> was
# E3f1b0491 -> Eefecf867). There is deliberately NO sup() call for
# either pair anywhere in this file. Suppressing either would
# additionally break genuine RenderBrowserQA / class-init
# reachability. Eba94fbde appears in no simulated Set G route for
# the seven methods.
# --- END 3-MERGER-ACTION ---

# --- 3-ADD (design section 4c, Part B). Previewer for-result page
# split. New SCREENS entry and edges in the B6-fix section; no EDIT
# change, no suppression of any dispatch edge.
# Why @FORRESULT variant nodes (rather than splitting only the page):
# the page a Previewer enters is decided by Previewer.onCollectionLoaded,
# a single shared method node. If only a new page were added with an
# ENTERS edge from the generic onCollectionLoaded, both launchers
# would enter both pages and the shortcut would survive. The variant
# chain makes entry into S_PREVIEWER_FORRESULT reachable ONLY from
# the fragment's for-result launch. The variant nodes are not methods
# in method_list.json; base() strips @FORRESULT, so they do not
# create labels, and the build's "page not reachable" check passes
# because S_PREVIEWER_FORRESULT is reachable from
# S_CARDTEMPLATEEDITOR, which is reachable. Note on duplication:
# @FORRESULT nodes are not receiver variants, so the builder will
# duplicate Previewer auto edges onto the @FORRESULT sources; those
# duplicates land on Previewer-owned destinations only and cannot
# reach either RESULT edge — the merger must confirm this on
# re-print (design section 0.4).
SCREENS['S_PREVIEWER_FORRESULT'] = 'Previewer: card preview launched for-result by CardTemplateEditor$CardTemplateFragment (startActivityForResult, REQUEST_PREVIEWER)'

# Variant lifecycle chain, entered ONLY from the template editor's
# for-result launch. Evidence: CardTemplateEditor.java:478-504
# (action_preview, startActivityForResult at :503-504).
e('CardTemplateEditor$CardTemplateFragment.onOptionsItemSelected',
  'Previewer.<init>@FORRESULT', 'INTENT',
  'preview a card from the template editor, for-result',
  guard='menu item action_preview selected and a card id exists (real card or dummy card), CardTemplateEditor.java:478-504',
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:478-504')
e('Previewer.<init>@FORRESULT', 'Previewer.onCreate@FORRESULT', 'LIFECYCLE',
  'framework activity launch',
  evidence='SRC com/ichi2/anki/Previewer.java:32; FW-SRC core/java/android/app/Activity.java:989')
e('Previewer.onCreate@FORRESULT', 'Previewer.onCollectionLoaded@FORRESULT', 'ASYNC',
  'card id != -1, so the early finish at Previewer.java:35-38 does not apply',
  evidence='SRC com/ichi2/anki/Previewer.java:32-39, 46-51')
# Dual entry: the for-result Previewer can do everything a generic
# Previewer can (GUI edges stay on S_PREVIEWER), but its RESULT
# edge lives only on the for-result page.
e('Previewer.onCollectionLoaded@FORRESULT', 'S_PREVIEWER', 'ENTERS',
  'for-result previewer reaches the previewer screen',
  evidence='SRC com/ichi2/anki/Previewer.java:45-51')
e('Previewer.onCollectionLoaded@FORRESULT', 'S_PREVIEWER_FORRESULT', 'ENTERS',
  'for-result previewer reaches the for-result previewer screen',
  evidence='SRC com/ichi2/anki/Previewer.java:45-51')
# MOVE (not copy) of Eb9d6a916: the for-result-page edge below is
# added here, and the generic-page edge is DELETED by the
# merger action that follows. The generic page must lose its RESULT
# edge, or the CardBrowser shortcut survives.
e('S_PREVIEWER_FORRESULT',
  'CardTemplateEditor$CardTemplateFragment.onActivityResult', 'RESULT',
  'previewer launched for-result by this fragment returns its result to it',
  guard='this Previewer instance was launched for-result by this fragment (CardTemplateEditor.java:503-504)',
  evidence='SRC com/ichi2/anki/CardTemplateEditor.java:503-504, 557-560')

# --- 3-MERGER-ACTION-RESULT (NOT executable code — do NOT convert to
# sup()). DELETE the existing hand edge from graphs/AnkiDroid/
# graph_def.py (lines about 5693-5700 in the merger tree read for
# this task):
#   S_PREVIEWER -> CardTemplateEditor$CardTemplateFragment.onActivityResult
#   (Eb9d6a916, hand RESULT, evidence CardTemplateEditor.java:503-504,
#   557-560).
# This is a MOVE, not a copy: the edge above on S_PREVIEWER_FORRESULT
# replaces it. The generic page must lose its RESULT edge, or the
# CardBrowser shortcut survives (a Previewer launched by CardBrowser
# via startActivityWithoutAnimation, AnkiActivity.java:158-161 as
# plain startActivity, could otherwise still deliver a result to the
# fragment). Eb9d6a916 appears in only 4 methods' current best
# routes (fragment.deleteDummyCards, fragment.onActivityResult,
# Collection.findNotes, Finder.findNotes); in Set G simulation the
# for-result RESULT edge is used by exactly 4 best routes, matching
# this set.
# --- END 3-MERGER-ACTION-RESULT ---


# ============================================================================
# SECTION 4 — Route-21 summary edge (design section 5c).
# Genuinely independent (no removal). File location in the merger
# tree: graphs/AnkiDroid/graph_def.py, B6 route-21 section, alongside
# E81c3cc95 / E2e661eb4.
# ============================================================================

# Summary ENTERS edge (mechanism (S) in design section 0; precedent:
# the existing direct variant-page edge E2e661eb4 itself bypasses the
# $1.onPositive callback, with the graph note "both routes exist").
# This edge is a SUMMARY of the existing 3-step delegation chain
# (sync(String) -> showSyncErrorDialog(int) ->
# showSyncErrorDialog(int,String) -> S_DLG_SYNC_ERROR_NOT_LOGGED_IN),
# not a new call: the 2-arg method IS invoked with id 0 from
# sync(String) via the 1-arg delegation, so the summary does not
# invent a call. It lands DIRECTLY on the variant page, so it creates
# no media shortcut (unlike a summary edge to the shared
# showSyncErrorDialog(int,String) node, which BFS could then route
# into the MEDIA page — do NOT add that form).
# Guard: hkey empty, DeckPicker.java:1280-1282
# (showSyncErrorDialog(DIALOG_USER_NOT_LOGGED_IN_SYNC) at :1282).
# The $17 chain is UNTOUCHED: DeckPicker$17.onPostExecute ->
# showSyncErrorDialog(int,String) (E5509de9d) is genuine for the
# media branch (:1493-1495) and the sanity branch (:1488) and is NOT
# suppressed here. MEDIA routing is preserved: DeckPicker.mediaCheck
# still routes through the MEDIA page (E6b094d43, E12ec6751 family),
# not through this edge; if any re-print shows mediaCheck (or any
# media-dialog method) routed through the NOT_LOGGED_IN page, back
# this edge out. The corrected chain already exists in the graph but
# is exactly tied with the $17 chain (both 16 edges); this edge
# replaces the 3-step delegation with 1 step, saving 2, so BFS takes
# the 14-edge direct-dialog route deterministically, not on a tie.
e('DeckPicker.sync(String)', 'S_DLG_SYNC_ERROR_NOT_LOGGED_IN', 'ENTERS',
  'hkey is empty, so sync(String) shows the not-logged-in dialog directly, without launching Connection.sync',
  guard='hkey empty, com/ichi2/anki/DeckPicker.java:1280-1282 (showSyncErrorDialog(DIALOG_USER_NOT_LOGGED_IN_SYNC) at :1282)',
  evidence='SRC com/ichi2/anki/DeckPicker.java:1280-1282; SRC com/ichi2/anki/DeckPicker.java:1058-1062')


# ============================================================================
# SECTION 5 — Route-26 target (design section 6c).
# NO new code in this section, deliberately. The route-26 suppression
# is ALREADY in Group 1: DeckTask$TaskListener.onPostExecute ->
# ModelFieldEditor$8.onPostExecute (E60efa3a0, auto CALL, evidence
# DeckTask.java:1306). Do NOT add it a second time (design section 8,
# step 1). $8 is registered only by ModelFieldEditor's own launchers,
# each with a direct ASYNC edge into $8 already in the graph:
# $6.onPositive (Ec428313c), $6$1.confirm (E1b9527dd), $7.confirm
# (Ef1429c4c), $2.onPositive (Ea1d11c47), $2$1.confirm (Eaf9fd4f0),
# deleteField (E6cf1352b), sortByField (E364727b6). A
# LOAD_DECK_COUNTS task from DeckPicker's updateDeckList registers
# $22, not $8. Genuine delivery is preserved by those seven direct
# edges, so $8 stays REACHABLE.
# CONSTRAINTS for route 26, stated here so the merger does not
# "complete" this section by adding a forbidden edge:
# - Eb104f8cb (ConfirmationDialog$1.onPositive ->
#   ModelFieldEditor$5$1.confirm, one of the 16 confirm dispatch
#   edges) is NOT suppressed. $5$1.confirm's BFS therefore stays
#   unchanged: 13 edges via the generic page
#   (deleteModelDialog -> S_DLG_CONFIRMATION -> onPositive ->
#   $5$1.confirm, ending E844468b9 E1f54d2af Eb104f8cb). Under the
#   no-suppression constraint, $5$1.confirm's BFS route cannot be
#   made the rename route; route B remains a valid, audited,
#   non-best derivation. Lifting the constraint for this single pair
#   is a coordinator decision, not something this file smuggles in.
# - Route-26 step-5 guard stays :958-only (auto_calls has exactly one
#   record for that pair; :858 has none and is not modelled here).
#   Nothing in this file touches that guard.
# - Route-17 step-6 edge Ec31ec494 is not disturbed.
# ============================================================================


# ============================================================================
# SECTION 6 — Route-14 Option A (design section 3c). ACCEPTANCE-GATED.
# This block is SEPARABLE (design sections 0.6.5 and 8, step 1): the
# merger applies it ONLY with explicit coordinator acceptance of the
# key-context argument AND the init-route expectation below. If the
# coordinator does not accept it, OMIT this whole block (and only
# this block) from 02.py; the other groups still apply, and route 14
# stays WRONG with design section 3a as its non-best derivation.
# No tools/ edit may be made to rescue route 14 instead (design
# section 3c ruling; B6 step 7).
# ============================================================================

# Option A — suppress ONE auto pair:
# Preferences$SettingsFragment.onResume -> Preferences.updatePreference
# (E8743f2b1, auto CALL, evidence Preferences.java:801 (bytecode)).
# COMMENT STATING THE TRUTH ABOUT THIS EDGE (record verbatim):
# This suppression suppresses a TRUE call edge to encode key context.
# onResume REALLY does call updatePreference at Preferences.java:799-801
# (syncAccount at :799, custom_sync_server_link at :800,
# advanced_statistics_link at :801). This is NOT a false-edge
# suppression like Group 1 / sections 4-5. All three keys are plain
# Preference elements (syncAccount in preferences_general.xml:29-33,
# custom_sync_server_link in preferences_advanced.xml:38-40,
# advanced_statistics_link in preferences_advanced.xml:131-133), so
# all three hit the else-return at Preferences.java:621 in
# updateSummary (line 622 is the closing brace) before replaceString
# (:636) or replaceStringIfNumeric (:634) can run. The edge is
# therefore the sole carrier of a key-inconsistent composition into
# replaceString. updatePreference stays reachable via
# onSharedPreferenceChanged (E249f9a1a, :812, and E1ff1f154, :225)
# and updateSummary stays reachable via initPreference (E0817366c,
# :445), so no method loses its only route.
# EXPECTED BFS ROUTE (corrected expectation): the 10-edge
# initPreference route (2 env kinds hardware+permission, 0 state
# kinds), NOT the 9-edge page-GUI backupMax-change route. The
# page-GUI route carries 1 state kind (settings) vs 0 for the init
# route, so it loses on state kinds before steps. Do NOT record the
# 9-edge page-GUI route as BFS under any outcome. Guard-text-only
# fixes on E8743f2b1 / Ec779c0bd document the fault but do not change
# BFS (the cost model ignores guard text) and are NOT a substitute
# for this block. Option B (@-variant split) and Option C
# (guard-text-only) are REJECTED in the design and are not coded here.
# ACCEPTANCE OF OPTION A IS A COORDINATOR DECISION, STATED HERE AND
# NOT RESOLVED BY THIS FILE. See CHECKLIST.md, open question 2.
sup(('Preferences$SettingsFragment.onResume', 'Preferences.updatePreference'))


# ============================================================================
# SECTION 7 — What this file deliberately does NOT contain (design
# section 9). The merger must not add any of these while applying it:
# - No sup() for Eba94fbde, E3f1b0491, any confirm/cancel dispatch
#   edge (including Eb104f8cb, E5bc5ca78), E5509de9d ($17 genuine
#   media/sanity edge), or any genuine caller edge.
# - No producer-specific DeckTask variant chains for the TaskListener
#   family (rejected in design section 0.1A.3); variant chains are
#   used only for the Reviewer receiver (Group 2) and the Previewer
#   for-result page (Group 3), where the shared node is a lifecycle
#   method.
# - No guard-text-only "fix" presented as a BFS fix for routes 14,
#   26-intermediate, or 28 (guard text is never read by either BFS
#   stage; design section 0).
# - No tools/build_graph.py change of any kind.
# - No second route-11 edge, no route-08 edge, no change to
#   Ecba7dfd7 (stays ENV_NETWORK), no change to the route-26
#   :958-only guard, no change to the single EDIT definition.
# Expected Set G outcomes (design section 0.3 + REAUDIT section 5;
# all subject to the merger's real rebuild and re-print, and to the
# three coordinator acceptances in CHECKLIST.md):
#   route 03 = 12 edges, filtered-deck route (0 env, data);
#   route 13 = 37 edges, Reviewer-head route (network, data);
#   route 14 = 10 edges, initPreference route (hardware+permission,
#     none) — ONLY with Option A acceptance, else stays WRONG;
#   route 18 = 34 edges, Reviewer head + for-result tail (none, data);
#   route 21 = 14 edges, direct-dialog route (none, none);
#   route 26 target = 12 edges, route A (permission, file+data);
#   route 28 = 23 edges, onActivityResult route (none, data) —
#     ruling (ii) stated explicitly; the $1 route at 25 edges, same
#     kinds, stays non-best; FIXED only if the coordinator
#     explicitly accepts the onActivityResult route, otherwise
#     stays WRONG.
# Aggregate (design section 0.4, re-proved in REAUDIT section 6):
#   0 of 3,275 REACHABLE methods lose a route; 0 of 911 UNREACHABLE
#   gain one; 1,274 best routes change (1,063 via the Reviewer
#   variant entry). Any label move on rebuild = stop, back out the
#   last edit, report — it is not "explained away".
# ============================================================================

# ---- Stream A merger fix: IMPORT progress chain (restores DeckPicker$5.onProgressUpdate) ----
# Root cause found on the first Stream A build: the variant progress hand edges
# (onProgressUpdate@T -> TaskListener@T) suppress, by the builder's base-pair hand-covering
# rule, the auto edge DeckTask.onProgressUpdate -> DeckTask$TaskListener.onProgressUpdate
# (Eb7581a2a), which was the base TaskListener's only entry. The DeckTask fragment wrote no
# IMPORT progress chain ("its progress goes via doProgress"), so DeckPicker$5.onProgressUpdate
# (the IMPORT listener, graph_def.py:7489) stranded: REACHABLE fell 3275 -> 3274, errors 1.
# The EDIT wrapper already allows IMPORT progress to DeckPicker$5.onProgressUpdate
# (_PROG_LISTENERS['IMPORT']), so this chain needs only the two hand edges below; the
# TaskListener@IMPORT -> $5 edge arrives by auto fan-out and stays CALL under the EDIT clause.
# Genuine path (printed source): doInBackgroundImportAdd builds the only ProgressCallback in
# the source root (DeckTask.java:750); ProgressCallback.publishProgress calls task.doProgress
# (DeckTask.java:1340-1342); doProgress calls publishProgress (DeckTask.java:1348-1349);
# AsyncTask dispatches onProgressUpdate (DeckTask.java:352-355) to the registered listener
# (DeckTask.java:1311-1312). No other task builds a ProgressCallback, so routing doProgress
# to @IMPORT is type-correct. Correction (audit note): the base doProgress ->
# onProgressUpdate edge (Ec953edeb) is a HAND edge from graph_def_mod/01.py, so hand-covering
# does NOT suppress it and it persists; this is harmless because base onProgressUpdate's
# only remaining outgoing is the BaseAsyncTask super-call and base TaskListener still has
# no incoming edge — the @IMPORT chain, not the base chain, carries $5.
# This does NOT restore the base TaskListener fan-out: base TaskListener.onProgressUpdate
# still has no entry, so progress for other types stays on its variant chain only.
e('DeckTask.doProgress', 'DeckTask.onProgressUpdate@IMPORT', 'ASYNC',
  'the import progress callback forwards through doProgress, which publishes progress to onProgressUpdate on the UI thread',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:750, 1320-1350, 1348-1349, 352-355')
e('DeckTask.onProgressUpdate@IMPORT', 'DeckTask$TaskListener.onProgressUpdate@IMPORT', 'CALL',
  'onProgressUpdate forwards to the registered TaskListener',
  env=None, evidence='SRC com/ichi2/async/DeckTask.java:352-355, 1311-1312')
