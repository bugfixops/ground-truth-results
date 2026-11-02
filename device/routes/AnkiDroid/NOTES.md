# AnkiDroid device NOTES — combined merge (NEW FILE)

- This file is NEW: the branch has no `device/routes/AnkiDroid/NOTES.md`
  (connector fetch failed: path does not exist). Nothing here was
  pushed; this is a helper deliverable for the merger.
- What this file is: the LIVE-RUN FLAG LIST for the 30 driven routes
  in `ROUTES_NEW.csv` (combined-merge redraw). Every entry below is
  an item that can only be verified on a live run: uiautomator
  button-text checks, layout flags, timing/rotation behaviour, and
  fixture assumptions. Each entry states: route | flag | why it
  needs a live run | status.
- Status rule (binding): every flag stays OPEN until a live run
  verifies it. Nothing in this file claims a live run, and no flag
  is marked verified. Flags gathered from each script's own mapping
  notes and preconditions; no flag is invented that the script does
  not state. Where a script says a selector is "verified in res" or
  "verified against the printed tree", it is NOT listed as a live
  flag unless the script also says to verify it live.
- Graph basis: combined-merge graph (4186 methods, 56 pages, 9815
  edges, R3275/U911); route table CORRECT 27 / WRONG 3 / UNCLEAR 0
  (WRONG = new-sample rows 09 closeStudyOptions, 18 validateBrackets,
  28 Collection.getServer — none of those three is a driven device
  row's print; driven rows keep their corrected/gate-verified
  drives per ROUTES_DELTA.md).
- No date value is written anywhere in this file. The route_25
  backup-entry rule states a FORMAT only (see route_25).

## route_01 — Phrase.<init> (38 edges)

- route_01 | "Navigate up" and "More options" content descriptions |
  Standard framework/AppCompat descriptions assumed by the script;
  only a live uiautomator dump shows the actual descriptions |
  OPEN
- route_01 | Translation language spinners default to a valid pair, or
  run setup pre-sets translatorLastLanguageFrom/To | Spinner defaults
  are runtime state; a live run shows whether translation proceeds
  or stalls on empty language selections | OPEN
- route_01 | Glosbe response arrives and the pick-translation dialog
  is shown (final Phrase construction is a Gson library consequence)
  | Network + dialog behaviour observable only on a live run; the
  construction itself has no printed Gson source in the tree |
  OPEN

## route_02 — EasyX509TrustManager.<init> (20 edges, UNSCRIPTABLE)

- route_02 | UNSCRIPTABLE (unchanged): reaching the target requires a
  logged-in AnkiWeb account (stored hkey non-empty) and a real HTTPS
  sync to the AnkiWeb server; no test account exists and a real sync
  must not be attempted; with an empty hkey the flow diverts to the
  not-logged-in dialog before any Connection.sync | No harness
  action creates a logged-in account; this is a standing reason, not
  a live-run flag to clear | OPEN (standing)

## route_03 — Stats$1.compare (26 edges)

- route_03 | "Navigate up" content description | Standard framework
  description assumed by the script; only a live dump confirms it |
  OPEN
- route_03 | Which chart tab Statistics shows by default, and whether
  the HOURLY_BREAKDOWN fragment is the one created without an extra
  tab tap | Default tab is runtime UI state; the script dwells after
  onCollectionLoaded so fragments instantiate, but only a live run
  shows which fragment actually draws | OPEN
- route_03 | Review history gives at least 2 hourly-breakdown entries
  and the HOURLY_BREAKDOWN fragment is attached, created, measured
  non-zero, and changed since creation | Collection + fragment
  runtime state; the comparator runs only then | OPEN

## route_04 — Sched._cntFnNew (15 edges)

- route_04 | Day rollover pending at deck-list load (Utils.now() >
  mDayCutoff) and launch is not sync-on-resume | Collection clock
  state at run time; without rollover _checkDay never calls reset
  and the target is not reached | OPEN

## route_05 — libanki.Utils$1.<init> (14 edges)

- route_05 | HINT dialog positive button label is "OK" | Carried from
  the old script and flagged unverified in the script itself; only a
  live dump confirms the HINT dialog's positive label | OPEN
- route_05 | "More options" content description | Standard AppCompat
  description assumed by the script; only a live dump confirms it |
  OPEN
- route_05 | AnkiDroid directory exists and is a directory, and
  collection.anki2 exists in it | Device filesystem state at run
  time (getImportableDecks guard) | OPEN

## route_06 — Sched.revDue (16 edges)

- route_06 | Finished deck: zero new, learning, and due cards, so the
  study-options fragment takes the CONGRATS branch to finishedMsg |
  Collection state at run time; any due card takes a different
  branch and revDue is never evaluated as the _nextDueMsg test |
  OPEN

## route_07 — MediaCheckDialog$3.<init> (14 edges, MENU DRIVE KEPT)

- route_07 | DRIVE NOTE (merger + live run): the device drive is the
  14-edge MENU chain (options menu -> Check media -> OK on the
  confirm dialog -> wait for the media check -> RESULTS dialog),
  kept unchanged from the old device row. The new-sample row 07
  print is a DIFFERENT 16-edge sync-error drive (launch with
  sync-on-resume -> sync-null -> $17.onPostExecute ->
  showSyncErrorDialog -> S_DLG_SYNC_ERROR_MEDIA -> mediaCheck ->
  ... -> $3.<init>), judged CORRECT on its own condition
  (media-sync-server-error + check success + logged-in hkey +
  online). The live run must confirm the MENU drive, NOT the sync
  drive: no account, no sync, and no server result are needed for
  the menu drive, and a live run that follows the sync-error print
  would not validate this row's drive | OPEN
- route_07 | "More options" content description | Standard AppCompat
  description assumed by the script; only a live dump confirms it |
  OPEN
- route_07 | Media check succeeds AND the result has ZERO unused
  files, so the RESULTS dialog takes the else branch
  (MediaCheckDialog.java:132) | Collection/media-directory state
  (clean media directory / all media referenced), observable only
  when the check actually runs | OPEN
- route_07 | SD card mounted, so the Check media menu item is enabled
  | Device mount state at run time | OPEN

## route_08 — ModelEditorContextMenu.onCreateDialog (14 edges)

- route_08 | "More options" content description | Standard AppCompat
  description assumed by the script; only a live dump confirms it |
  OPEN
- route_08 | Model list loads successfully and the tapped model/field
  are the fixture names (Basic / Front) | Run-setup fixture match +
  live list contents; if setup creates different names,
  FIXTURE_MODEL / FIXTURE_FIELD must change to match | OPEN
- route_08 | Carried table flag: the final <init> -> onCreateDialog
  step stays INFERRED (support-v4 DialogFragment source absent from
  the tree); the same method was UNCLEAR in the first draw for this
  reason. If the table auditor rules UNCLEAR, this row flips with
  no other change | OPEN (table audit, not a live-run proof)

## route_09 — Finder.findNotes (34 edges)

- route_09 | "Navigate up", "More options", and "Preview" content
  descriptions | Standard toolbar-item descriptions assumed by the
  script; only a live dump confirms them | OPEN
- route_09 | A real or dummy card id exists for Preview, so Previewer
  does not finish early (Previewer.java:35-38) | Runtime collection
  state; an early finish breaks the for-result tail | OPEN
- route_09 | A note whose template editor is reachable from the
  CardBrowser add-card flow | Fixture + UI state at run time | OPEN

## route_10 — Template$1.compare (17 edges)

- route_10 | Whether the collection-open probe's getCol open is the
  first open or a retry open (transient first-open failure followed
  by successful retry inside exceededCursorSizeLimit -> getCol ->
  Storage.Collection) | Only a live run's logcat/steps show which
  open enters the upgrade chain; a run whose collection opens by
  the ordinary firstCollectionOpen path without entering the
  upgrade chain does not reach the target | OPEN
- route_10 | Cold start with the collection not yet open; stored
  schema below SCHEMA_VERSION; saved model with non-zero id;
  non-cloze model with a template whose qfmt contains a
  multi-modifier tag (>= 2 modifiers) whose field is absent from
  the _reqForTemplate context | Collection + model runtime state;
  the comparator runs only for >= 2 modifiers | OPEN

## route_11 — StudyOptionsActivity.closeStudyOptions(int) (24 edges)

- route_11 | PHONE-LAYOUT FLAG (mFragmented tension): the fragment
  prefix needs mFragmented true (loadStudyOptionsFragment shows the
  study-options fragment in DeckPicker), while the
  StudyOptionsActivity tail needs mFragmented false (openStudyOptions
  takes the phone branch to StudyOptionsActivity, DeckPicker
  guard at the openStudyOptions step, edge Eec5d8f89). The live run
  must confirm the activity actually launches from the fragment
  layout, or the tail fails at Eec5d8f89. This tension is
  UNRESOLVED by the combined merge: the new-sample row 09 print
  (33 steps) is WRONG and is NOT this drive; this drive repairs
  the edge break with the genuine producer-variant chain but does
  NOT resolve the guard tension | OPEN
- route_11 | "More options" content description | Standard AppCompat
  overflow description assumed by the script; only a live dump
  confirms it | OPEN
- route_11 | Collection open with a non-dyn deck selected and cards
  present, so the study-options fragment shows (not the congrats
  view) | Runtime deck state | OPEN

## route_12 — HttpFetcher.downloadFileToSdCardMethod (37 edges)

- route_12 | BEOLINGUS/NETWORK FLAG: network on with the Beolingus
  page (dict.tu-chemnitz.de) reachable, so the pronunciation post
  reaches downloadFileToSdCardMethod | External network reachability
  at run time; no AnkiWeb account is needed | OPEN
- route_12 | "Navigate up" and "More options" content descriptions |
  Standard framework/AppCompat descriptions assumed by the script;
  only a live dump confirms them | OPEN
- route_12 | Note field has non-empty text with a TEXT field
  controller, so the pronounce button exists | Fixture note state
  at run time | OPEN

## route_13 — Sound.notifyConfigurationChanged (24 edges)

- route_13 | "More options" content description | Standard AppCompat
  description assumed by the script; only a live dump confirms it |
  OPEN
- route_13 | Current card's question side contains a video sound
  (video extension/MIME) with a non-null video thumbnail; TTS off
  (non-TTS replay branch) | Card-content + settings runtime state |
  OPEN
- route_13 | Rotation to landscape WHILE the video plays drives
  onConfigurationChanged -> notifyConfigurationChanged | Timing
  behaviour: rotation must land during playback, and VideoPlayer
  must declare the configChanges the route relies on | OPEN

## route_14 — Models$TransformFieldDelete.<init> (21 edges)

- route_14 | "More options" content description | Standard AppCompat
  description assumed by the script; only a live dump confirms it |
  OPEN
- route_14 | Model Basic with at least two fields (Front plus one
  more); deleteFieldDialog only toasts when fewer than two fields |
  Fixture model state at run time | OPEN

## route_15 — Anki2Importer._mediaPick (16 edges)

- route_15 | "More options" content description | Standard AppCompat
  description assumed by the script; only a live dump confirms it |
  OPEN
- route_15 | Run setup supplies a valid import.apkg (stem "import",
  NOT collection.apkg) in the AnkiDroid folder AND the media file
  it references already present in the destination media directory,
  so compareMedia runs | D9 provisioning gap (see
  D9_PROVISIONING.md section (a)): generation unproven, device
  paths to confirm live; the script pushes no file | OPEN
- route_15 | Collection open and collection.anki2 exists at launch |
  Runtime collection state after pm clear + setup | OPEN

## route_16 — Preferences.replaceString (10 edges)

- route_16 | Launch screen IS the Advanced preferences screen
  (collection NOT open, SD mounted, AnkiDroid directory NOT
  accessible) | Launch-state runtime condition; the script itself
  notes that if the launch screen is not the Advanced screen, the
  live run must navigate to it first, and that fallback has no
  graph edge | OPEN
- route_16 | Advanced screen contains backupMax (Max number of
  backups) as a qualifying SeekBarPreference with summary XXX |
  Preferences-screen runtime contents | OPEN

## route_17 — DeckPicker$5.onProgressUpdate (16 edges)

- route_17 | "More options" content description | Standard AppCompat
  description assumed by the script; only a live dump confirms it |
  OPEN
- route_17 | Run setup supplies a valid import.apkg (stem "import",
  NOT collection.apkg) in the AnkiDroid folder | D9 provisioning
  gap (see D9_PROVISIONING.md section (a)); the script pushes no
  file | OPEN
- route_17 | Import runs long enough for progress publication (the
  progress dialog shows values while importing) | Timing/size
  behaviour: a tiny package may import too fast for
  onProgressUpdate to be observed | OPEN

## route_18 — Sched.sortCards(long[],int,int,boolean,boolean) (19 edges)

- route_18 | Tablet/fragmented layout, so the fragment toolbar shows
  the export item | Layout runtime state; on a phone layout the
  fragment toolbar item may not be where the script taps | OPEN
- route_18 | "More options" content description | Standard AppCompat
  description assumed by the script; only a live dump confirms it |
  OPEN
- route_18 | Deck with cards to export, deck id non-null, so the
  export dialog defaults Include scheduling unchecked | Fixture
  deck state at run time | OPEN

## route_19 — AdvancedStatistics$Card.setIvl (35 edges)

- route_19 | "Navigate up" content description | Standard drawer-toggle
  description assumed by the script; only a live dump confirms it |
  OPEN
- route_19 | Preference advanced_statistics_enabled ON before launch
  (run setup sets it; Hooks installs AdvancedStatistics only then)
  | Settings runtime state; without it the simulation tail never
  runs | OPEN
- route_19 | Review history present, so the simulation has cards to
  simulate; Forecast tab reached and chart builds | Runtime history
  + tab state | OPEN

## route_20 — libanki.Utils.base62 (18 edges)

- route_20 | "Navigate up" and "More options" content descriptions |
  Standard framework/AppCompat descriptions assumed by the script;
  only a live dump confirms them | OPEN
- route_20 | NoteEditor opened for ADDING a note (no existing note
  id), so setNote builds a new Note with id null | Runtime mode:
  edit mode takes the id != null branch and guid64 is never
  reached; the script notes the null argument is a runtime value,
  not a graph node distinction | OPEN
- route_20 | A current model exists; collection.anki2 exists |
  Fixture collection state | OPEN

## route_21 — DiffEngine.diff_cleanupSemanticScore (24 edges)

- route_21 | Tablet/large-screen config (mFragmented true), so the
  study-options fragment loads | Layout runtime state | OPEN
- route_21 | "Study" tap text | Inherited from an old script and
  flagged for live verification in the script itself | OPEN
- route_21 | Answer field UNFOCUSED when Enter is pressed (defocus
  tap is a comment in the script, not a claimed tap: no defocus
  selector could be verified statically) | Live-run gap: if the
  field stays focused, displayCardAnswer does not run | OPEN
- route_21 | Type-answer card fixture: mShowTypeAnswerField true,
  mTypeCorrect non-null, correct answer at least 100 chars after
  trim; typed answer at least 100 chars after trim, differing from
  the fixture correct answer so diffs contain a single edit between
  equalities | Fixture answer contents + diff runtime behaviour;
  run setup must set the fixture correct answer so this holds |
  OPEN

## route_22 — MetaDB.getNotificationStatus (14 edges)

- route_22 | Notifications enabled: minimumCardsDueForNotification
  below 1000000 (its default, 1000001, disables the task), or the
  small widget enabled; run setup must set one of these | Settings
  runtime state; the script itself does not open Preferences (that
  would leave the route) | OPEN
- route_22 | Backgrounding with HOME drives onPause -> onStop, and
  the script's dwell covers the status task + NotificationService
  run (fetchDue -> getNotificationStatus) | Timing behaviour: the
  service chain runs on its own after onStop | OPEN
- route_22 | Collection open (colIsOpen() guard on the onStop step) |
  Runtime collection state | OPEN

## route_23 — Sched.getToday (18 edges)

- route_23 | Tablet/large-screen config (mFragmented true), so the
  study-options fragment loads | Layout runtime state | OPEN
- route_23 | Rebuild item placement: whether it sits directly on the
  toolbar or under overflow ("More options") | The script taps
  overflow then Rebuild under the single edge E57aebbea and states
  the placement could not be verified statically; only a live dump
  settles it | OPEN
- route_23 | Filtered (dyn) deck selected whose FIRST search term
  contains is:due | Fixture deck-search runtime state; any other
  first term takes a different _findCardState branch | OPEN

## route_24 — DB.insert (14 edges)

- route_24 | "More options" content description | Standard AppCompat
  description assumed by the script; only a live dump confirms it |
  OPEN
- route_24 | Corrupt collection with orphan notes (missing note type,
  wrong field count, or notes with no cards), so fixIntegrity's
  _remNotes branch runs with a non-empty id set and _logRem is
  reached | Collection corruption runtime state; a healthy
  collection never reaches _remNotes | OPEN
- route_24 | Integrity-check task timing: the script dwells on the
  CHECK_DATABASE edge while the task runs | Async timing behaviour
  on a live run | OPEN

## route_25 — BaseAsyncTask.onProgressUpdate (17 edges)

- route_25 | BACKUP-DATE RULE (format only, never a value):
  RESTORE_BACKUP list items are dates derived from backup
  filenames, formatted "YYYY-MM-DD (HH:MM h)" (script header cites
  DatabaseErrorDialog.java:251-270). The live entry text comes
  from run setup's GEN_DIR/backup_entry.txt (see
  D9_PROVISIONING.md section (b)); NO script, ROUTES cell, or
  note in this merge may carry a hard-coded date string for this
  entry. The script selects the backup entry by that run-time
  text, never by a fabricated date | OPEN
- route_25 | Valid, non-empty backup .apkg present in the backups
  directory, so the RESTORE_BACKUP list is non-empty | D9
  provisioning gap (see D9_PROVISIONING.md section (b)):
  generation unproven, backups-directory path to confirm live |
  OPEN
- route_25 | LOAD_FAILED launch state AND a usable collection
  context for importReplace (which dereferences col.getPath()):
  the script itself flags this tension — if the live run shows
  importReplace cannot proceed from a failed load, the fallback
  is the collection-open menu prefix (action_restore_backup ->
  CONFIRM_RESTORE_BACKUP -> RESTORE_BACKUP, same tail) | OPEN
- route_25 | Import task publishes progress only after the backup
  zip opens, unzips, contains collection.anki2, and the temp
  collection validates | Runtime import behaviour + dwell timing |
  OPEN

## route_26 — CollectionLoader.deliverResult (11 edges, UNSCRIPTABLE)

- route_26 | UNSCRIPTABLE (unchanged): the row's only entry is the
  no-space dialog, shown only when BackupManager.enoughDiscSpace
  is false (DeckPicker.java:848-850); no harness action (launch,
  tap, key, type, scroll, rotate, push_fixture) creates a
  below-threshold free-space state, the threshold is 10 MiB
  (BackupManager.java:47, 207-208), and filling storage risks
  breaking the collection load the route itself needs; other
  loader entries (for example Reviewer onCreate) are not this
  row's route and must not be substituted | Standing reason, not
  a live-run flag to clear | OPEN (standing)
- route_26 | STALE-SCRIPT WARNING: branch files route_26.py and
  route_26b.py do NOT drive this row (they drive
  ModelFieldEditor$1.<init>, a different method, from an old
  route table). They must not be run as route_26; see
  SCRIPTS_DELTA.md flag | OPEN (merger decision)

## route_27 — Collection.close() (14 edges)

- route_27 | sqlite3 installed on the device, so the ERROR_HANDLING
  "repair" option (value 2) is offered | Device provisioning state;
  without sqlite3 the repair item is not offered and the drive
  cannot proceed | OPEN
- route_27 | Non-null collection for repairCollection (which
  dereferences col.getPath() before reaching col.close()), in
  tension with the failed-load launch state | Runtime collection
  state flagged by the script itself | OPEN
- route_27 | Dialog texts are source-verified ("Options",
  "Repair database", "Repair"), but the dialog STAGES must appear
  in order (LOAD_FAILED -> ERROR_HANDLING -> REPAIR) on the
  underscore-page chain | Live dialog sequencing | OPEN

## route_28 — AbstractFlashcardViewer.typeAnswer (16 edges)

- route_28 | TABLET/LARGE-SCREEN PRECONDITION WORDING — flagged for
  merger confirmation: the old drive's "tablet/large-screen
  config" wording is carried as a precondition note, NOT as a
  verified drive requirement and NOT as a tap. The merger must
  confirm whether the 16-edge gate-verified print (Reviewer
  prefix + ANSWER_CARD launch with mAnswerCardHandler) actually
  needs a tablet/large-screen config, or drop the wording. Until
  that confirmation, the live run should use a tablet/large-screen
  config and record whether a phone config also works | OPEN
  (merger confirmation + live observation)
- route_28 | "Study" tap text | Inherited from an old script and
  flagged for live verification in the script itself | OPEN
- route_28 | Deck with cards to study, so the Start button opens
  Reviewer; ANSWER_CARD onPreExecute runs and blockControls
  evaluates typeAnswer automatically (no card interaction needed
  after Reviewer loads) | Runtime deck state + dwell timing | OPEN

## route_29 — Decks.id(String,boolean) (11 edges)

- route_29 | FIXTURE FLAG: the exact mechanism that sets the stored
  focused deck (which preference or intent extra sets mFocusedDeck)
  was not re-verified beyond the guard text on Edd7cc90a
  ("focused deck differs from current deck; result non-null") |
  The merger must confirm the fixture sets that state before a
  real run; if it cannot be set, this route needs a different
  entry, not a forced tap | OPEN
- route_29 | Nested deck whose name contains "::" (at least one
  parent); stored focused deck differs from the current deck and
  is not in the displayed deck list; launch is not sync-on-resume |
  Fixture deck + launch runtime state | OPEN

## route_30 — SimpleMessageDialog.<init> (13 edges)

- route_30 | "More options" content description | Standard AppCompat
  description assumed by the script; only a live dump confirms it |
  OPEN
- route_30 | Integrity check completes with result non-null and true
  (DeckPicker.java:1170), so showSimpleMessageDialog runs instead
  of handleDbError | Whether a healthy collection yields that
  result is flagged in the script (inherited assumption); if a
  healthy check shows no message dialog, this script diverges at
  that step | OPEN
- route_30 | SD card available, so the Check database menu item is
  enabled | Device mount state at run time | OPEN
