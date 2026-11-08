# AnyMemo device routes — notes (D1/D3, finish run 2026-11-01)

Sources: graphs/AnyMemo/verification.csv path rows (30, final sample),
graphs/AnyMemo/out/methods.csv (env/state kinds), the app manifest
(final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main/AndroidManifest.xml),
work-emulator ci/apps.csv (package org.liberty.android.fantastischmemopro,
no setup), work-emulator/fixtures/ (verified on disk), and the printed
route files in graphs/AnyMemo/scratch/route_print/.

## Verification performed (merger, this session)

- ROUTES.csv checked against the verification.csv path rows and
  out/methods.csv: 30 rows in path-row order, every method, edges string,
  and source exact; env/state kinds exact for all 30; every listed
  permission declared in the manifest; every listed fixture exists under
  work-emulator/fixtures/. All checks pass.
- Each of the 27 scripts was merger-verified and then independently
  audited: py_compile OK, edge ids exactly equal to the ROUTES.csv row,
  no permission grants, no fixture pushes, and a per-helper drycheck PASS
  (see helper REPORT.md files and the audit reports under
  audit/d3-h12/, audit/d3-h34/, audit/d3-h56/, audit/d3-h1-rework/,
  audit/d3-h34-rework/, audit/d3-h34-rework-cellfix/,
  audit/d3-h56-rework/). H1/H5/H6 scripts ship ONLY in their reworked
  (stage-fallback-stripped) form; route_18 ships ONLY in its reworked
  (TTF_ROW_TEXT set) form; route_17 ships no script (unscriptable).
- Full assembled drycheck (all 30 rows + all 27 scripts, stage drycheck.py
  --load-scripts): AnyMemo: 30 PASS, 0 FAIL with a staged wemu (27
  scripted + 3 unscriptable). Against the real unprovisioned fixture
  store the single FAIL is route_18's missing .ttf fixture (see below)
  — a provisioning signal, not a bundle defect.
- All D3 audits and re-audits have PASSED at push time. The notes below
  are the merger's findings as updated by those audits; audit verdicts
  govern where they differ from the merger's provisional notes.

## Status: 27 scripted, 3 unscriptable (10.0%, exactly at the 10% cap)

- Unscriptable: route_02 UploadDropboxActivity.onDestroy and route_08
  DropboxApiHelper$4.call. Reason (both): a Dropbox account and saved
  access token cannot be created by adb on an AOSP emulator (no token
  fixture exists; OAuth login in an external browser/Custom Tab and
  api.dropboxapi.com reachability are required; methods.csv states the
  token gate explicitly). The attempt cannot start.
- Unscriptable (added at D3 push time, superseding the provisional
  scripted status below): route_17 Card.toString. Reason: Card.toString
  fires only in the RuntimeException message at
  LearnQueueManager.java:267 (cardDao.update returns 0); this chain's
  flush is the build-time flush with an empty dirtyCache, and deleting
  the card trips the earlier :263 LearningData check first, so no UI,
  fixture, or harness path populates dirtyCache with a nonexistent
  card. This is the D1 audit's recorded revert condition firing on the
  H34 auditor's judgment (a script that cannot reach its target must be
  unscriptable). Full reason, printed evidence, and edge ids are in
  ROUTE_UNSCRIPTABLE_17.md; the route_17.py script is EXCLUDED from the
  push bundle (not modified). D7 consequence: a not-reached route_17
  run maps to a DEVICE row of unclear, never wrong; the method's
  verification.csv label is untouched by this reclassification.
- All other routes are scripted. "Scripted" means a script exists and
  passes drycheck; it does not guarantee reached=yes on a real run.
  A route whose target does not fire reports reached=no (DEVICE row
  unclear), which is the system's designed behavior for hard routes.

## Fixtures

- ROUTES.csv lists Download/sample_deck.apkg on routes 02, 04, 07, 09, 10,
  15, 18, 20 (the generic STATE file listing gate). In practice the
  listing gate is satisfied by first-run state in every case: the
  first-run sample db (french-body-parts.db in the app root) for
  09/10/15, the ".." row for 20, directories for the browsers. The
  pushed .apkg (verified: an Anki archive containing collection.anki2,
  no cards.xml) is never the row actually tapped, because every browser
  involved filters by extension (.db for 04/15/20, .ttf for 07/18) and
  opens at the app root, not at /sdcard/Download/. The listing is
  harmless (run_app.sh pushes it; unused) and is kept as verified.
- REAL-RUN FIXTURE NEEDS (flagged to the coordinator/device lead; none
  exists in work-emulator/fixtures today, and none is listed here):
  - A .ttf FILE placed so it lands in the picker root
    (AMEnv.DEFAULT_ROOT_PATH = external files dir + "/anymemo/") for
    routes 07 and 18. UPDATE AT D3 PUSH TIME: the ROUTES.csv rows for
    07 and 18 are now amended (fixtures cell =
    Download/sample_deck.apkg;Android/data/org.liberty.android.fantastischmemo/files/anymemo/DejaVuSans.ttf,
    the .apkg retained), and route_18's script is fixed
    (TTF_ROW_TEXT = "DejaVuSans.ttf", verified as a real font on the
    build machine); route_07's script is unchanged (H2 PASS — it was
    already the right shape for the provisioned case). What remains is
    ONLY the file provisioning itself (device-lead/D9 item, outside
    this push): until DejaVuSans.ttf is provisioned into the fixture
    store at that picker-root path, routes 07/18 fail at the picker tap
    (unclear, never wrong). Both pickers pass EXTRA_FILE_EXTENSIONS
    ".ttf" (SettingsScreen.java:715/:726) and FileBrowserFragment lists
    only matching files (FileBrowserFragment.java:252-257); a fresh
    install has no .ttf in that root, so no file row exists to tap
    until provisioning lands.
  - A genuine Mnemosyne2 cards archive (a zip containing cards.xml)
    for route_04. The converter throws unless cards.xml is present
    (Mnemosyne2CardsImporter.java:184) before ValueType is first used,
    and the export-converter browser filters to ".db", so the .apkg
    row may not even be listed. Re-routing the target is NOT an
    option for a ticked app; only fixture provisioning fixes route_04.
- No setup.py is shipped: the AnyMemo setup column in ci/apps.csv is
  empty, and every script builds needed deck/card state through the app
  UI (first launch auto-creates the sample db; routes 13/14/21 create a
  second db through the Open tab / Merge UI where two distinct paths
  are required).

## Route decisions and real-run caveats (all routes stay scripted)

- Merger-splice family (printed chain splices a Misc-tab DatabaseMerger
  launch onto a PreviewEditActivity result tail; a Misc launch returns
  to AnyMemo, not PreviewEdit, by startActivityForResult semantics, and
  with empty target/source fields the merge throws): routes 01, 06, 11,
  12, 13, 14, 19, 22, 23. Scripts follow the printed edge order (some
  re-enter PreviewEdit/StudyActivity via Recent/Open tab and log the
  return edges as comments). Real-run outcome likely unclear where the
  return cannot fire. NOT unscriptable: the attempt can start; the
  target may not be reached. The auditor is asked to judge the
  comment-logging and re-entry treatment on the routes it samples.
- Route_03 guard deviation (auditor to re-read): the printed launcher
  guard says both category and range radios are unchecked, but that
  branch takes refill(startOrd, quizSize), which never calls
  getCardsByCategory; only the category branch (refill(Category),
  QuizQueueManager.java:199-202) reaches the target. The script takes
  the category path. Edges over prose: the chain is validated by
  drycheck, and the category path is the only source path to the
  target. Also note the trigger graph's "study" gui text on the
  open-actions edge is wrong for this route (the quiz item creates the
  launcher dialog).
- Route_05: fixed-coordinate taps (540, 400) with why strings for the
  live download list rows (no stable selector exists); re-check
  against the actual emulator resolution before a real run. Needs live
  anymemo.org reachability (emulator has network).
- Route_09: the accept target fires only after the system
  ACTION_CREATE_DOCUMENT picker completes (ExportAnyMemoDbFragment
  .java:47) — out-of-app UI with no route edge. The script comments
  the picker steps; if the picker is not completed, the run reports
  reached=no (unclear).
- Route_16 drawer gap (auditor to judge): the script taps the drawer
  "Options" entry without opening the drawer first; the harness has no
  drawer-open gesture, and the Misc tab's Options button (same
  OptionScreen) is documented but not scripted. On a real run the
  drawer-entry tap may not resolve unless the drawer is opened first.
- Route_17 Card.toString (SUPERSEDED AT D3 PUSH TIME — now
  unscriptable, see Status above): the target fires only on a
  DAO-update-failure exception (LearnQueueManager.java:267). The D3
  helper found no deterministic UI-reachable induction: this chain's
  flush is the build-time flush with an empty dirtyCache (only
  LearnQueueManager.update, after grading at StudyActivity.java:608,
  populates it); a UI-graded card's row exists; a UI-deleted card
  trips the earlier :263 LearningData check first (CardDaoImpl.delete
  cascade-deletes learning data, CardDaoImpl.java:187-195). The H34
  auditor judged that a script that cannot reach its target must be
  unscriptable, firing the D1 revert condition; the former script
  (which walked through queue-load and commented the final edge
  without claiming reach) is EXCLUDED from the push bundle.
- Route_19 gesture uncertainty: no third-party dictionary app is needed
  (DictApp.parse runs inside getDictApp before the ColorDict intent
  fires). But the gesture tail is uncertain: gestures default off
  (the script enables them via the Gestures dialog), the harness has
  no stroke API (the script long-presses gesture_overlay), and a press
  without movement is unlikely to score as an O-shape over 3.0.
  Fallback noted but not scripted (the route's edge IS the gesture):
  StudyActivity's menu_context_lookup item calls lookupDictionary()
  directly. Also the script enters StudyActivity directly (a gesture
  in CardPlayerActivity would hit QACardActivity's no-op, not
  StudyActivity's override) and logs the PreviewEdit menu_card_player
  tap as a comment.
- Route_21: two distinct merge paths, both through the Merge UI
  (target = files-dir empty.db, source = app-root french-body-parts.db
  with 28 cards); merging copies each card through create, which calls
  setCreationDate. No blocking caveat.
- Route_20: completable without any fixture (".." always exists).
- Routes 24-30 are process-start routes (launch + comments only). The
  API 27 storage-permission dialog (AnyMemo.java:124-129) fires after
  all three of routes 28-30's targets (Dagger build at onCreate:117;
  channels in AMApplication.onCreate), so it cannot block them.
- Route_04 chain note: the printed chain splices an export-converter
  head (MnemosyneXMLExporter, "xml" destination, create-document
  branch) onto an import-service tail (Mnemosyne2CardsImporter, "db"
  destination). The script follows the printed edges; the "Yes"
  dialog tap may find no dialog from the export head in a real run.

## Decisions (Muse's own, for user/Yang review)

- D2 stands: storage permission is a startup-trunk ENV gate only;
  current modelling stands.
- Route_17: SUPERSEDED AT D3 PUSH TIME. The revert condition fired:
  the H34 auditor judged that a script that cannot reach its target
  must be unscriptable, so route_17 is now unscriptable (3/30, exactly
  at the 10% cap). Its script is excluded from the push bundle; its
  verification.csv label is untouched; D7 maps a not-reached run to
  unclear, never wrong. (The earlier "stays scripted" entry above is
  retained for history and is superseded by this entry.)
- Routes 07/18 stay scripted with their fixtures cells amended at D3
  push time (see Fixtures above); only the .ttf FILE provisioning
  remains open (device-lead/D9). Route_04 stays scripted despite its
  Mnemosyne-archive gap (see above): the gap is a provisionable
  input, not an adb-uncreatable condition, and flipping it would spend
  the cap on a gap the coordinator can close by provisioning.
