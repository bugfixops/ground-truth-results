# Aegis device routes — ROUTES notes

This package is placed in `device/routes/Aegis/` in this push (V3-corrected graph 6430 edges, final sample seed 20261025). No emulator/adb/device run was started, and no CI request was sent. This file explains the staging choices so the merger and the independent auditor can check them without re-deriving them.

## Row set and edge lists (verified, not claimed)

- 25 rows, sampler order, from the NEW final sample only (post-fix redraw,
  seed 20261025, V3-corrected graph 6430 edges, 2995 methods, 2537/458).
- Edge lists are taken EXACTLY from the regenerated verification.csv at
  `graphs/Aegis/verification.csv`
  (SHA 83c527cad5a03ec8c5e002e2b5177ceee79572e0ec8885133635139cb4074321),
  path rows in file order. Verification performed in staging:
  ROUTES.csv vs verification.csv path rows: 25 rows, same order, same
  methods, 1093 steps, 446 distinct edges, 0 mismatches.
- Dropped old row CustomSvgIcon is NOT in this package: no route_17 script
  for it exists here, and no edge list from it was carried. No SVG-pick generator exists for the dropped row: no new row picks an SVG file, and the SVG files generated at run time by setup_route_15.py (device-icon.svg) and setup_route_20.py (icon.svg) are icon-pack fixtures for rows 15 and 20, not picked files and not coverage for the dropped row. New row 17 is
  AuthActivity.lambda$onCreate$3, a different method, judged fresh.
- The old device drafts at `turn/device/` (ROUTES_DRAFT.csv, D1_NOTES.md,
  D7_PLAN.md) were used as reference only and were NEVER renamed into
  place: every row number, step count, and breakdown below was re-derived
  from the new sample.

## Renumbering map (old draft/sample numbering -> new final-sample numbering)

Old 01 AndOtp -> new 01. Old 02 FreeOTP -> new 02. Old 03 Stratum -> new 03.
Old 04 TwoFAS -> new 04. Old 05 Totp -> new 06. Old 06 AuthenticatorPlus ->
new 07. Old 07 Authy -> new 08. Old 08 RawSlot (49 steps, NONE-intro) ->
new 05 RawSlot (42 steps, @IMP import prefix; fresh script, old script
superseded). Old 09 IconAdapter -> new 09. Old 10 EntryAdapter -> new 10.
Old 11 GroupAdapter -> new 11. Old 12 AegisImporter -> new 14. Old 13
Scanner -> new 12. Old 14 Export -> new 13. Old 15 IconPackExists ->
new 15. Old 16 parser -> new 16. Old 17 CustomSvgIcon -> DROPPED (no new
row). Old 18 Audit -> new 18. Old 19 SlotIntegrity -> new 19. Old 20
IconPack Icon -> new 20. Old 21 Salsa -> new 21. Old 22 deleteAndFinish ->
new 22. Old 23 DigitCountVerifier -> new 23. Old 24 Hilt -> new 24. Old 25
AegisApplication -> new 25. New 17 AuthActivity has no old row.

## Verdict classes in this staging package

ROUTES.csv `status` uses the shipped two-value form only (`scripted` or
`unscriptable: reason`), because that is what run_app.sh and drycheck
consume. The D1 distinction between firm and draft scripted rows lives
here, in each script's staging banner, and in D1D3D7_REPORT.md — NOT in
the status column. A `scripted` row in this package therefore means "a
draft script is staged and dry-loads", never "proven on device".

- SCRIPTABLE, firm (8): rows 10, 11, 19, 21, 22, 23, 24, 25. Ordinary
  in-app UI with in-run inputs only; no fixture, picker, camera, or
  account dependency. Each still needs coordinator drycheck plus a real
  run before anything is claimed.
- DRAFT scripted, TO-ASSESS (14): rows 01, 03, 04, 05, 06, 07, 08, 12, 13,
  14, 15, 16, 18, 20. A draft script plus (where applicable) a run-time
  generator is staged, but a capability or app-side acceptance is still
  unproven (see D1D3D7_REPORT.md TO-VERIFY list). These rows are the
  retry set under the extended-harness user order.
- UNSCRIPTABLE (3): rows 02, 09, 17, each with an audited reason in
  ROUTES.csv and in the report. No script is staged for these rows: a
  script present for an unscriptable row would be a D1 inconsistency.
  Cap: 3/25 = 12.0%, over the 10% cap; the per-route cap-acceptance
  proposal is in D1D3D7_REPORT.md and belongs to the coordinator/user,
  not to this staging package.

## What changed versus the staging-D1 old-sample package (read, not copied)

- Carried scripts (20): action bodies carried from staging-D1 with
  renumbering, and edge lists REPLACED by the new verification.csv lists.
  The staging check asserted old edge list equals new edge list for every
  carried row (0 mismatches); the table's edge-identical claim for the 23
  common rows other than RawSlot is therefore confirmed by this package's
  own check, not assumed.
- New row 05 (RawSlot): fresh script from the new dump (Welcome import
  picker, assign-groups dialog OK, save chain). The old 49-step script
  was not reused.
- New row 17 (AuthActivity): no script (unscriptable as drawn). The old
  route_17 (CustomSvgIcon) was not reused for anything.
- New row 18 (Audit): rewritten as a two-phase DRAFT script (Phase A
  prepares the guards in-run, Phase B kills and relaunches), retrying the
  staging-D1 unscriptable judgement under the extended-harness order.
  The old partial script was not reused as a script.
- New row 19 keeps the staging-D1 scripted judgement: the in-script
  enable-encryption visit cures the table's pref-visibility ground, and
  the wrong-PIN digits mechanism (digits check passes, decrypt fails the
  padding check, Slot.getKey throws SlotIntegrityException, Slot.java:57
  BadPadding branch) is the stated trigger — source-derived, still
  device-unproven (see report).

## Setup decision proposal (merger must confirm)

- No UI-driving shared setup.py is shipped. `routes/setup.py` is an
  intentional no-op (logs only). Reason: the runner invokes shared
  setup.py once per route with no route argument, so it cannot know
  which route it is setting up; any intro-driving shared setup would
  corrupt intro/import prefixes and fight the two-phase scripts.
  Provisioning therefore lives per route (script intro prefix, in-script
  seeding, two-phase preparation, setup_route_NN.py generators).
- Row 14 (old row 12) decision, as proposed: per-route
  `setup_route_14.py` generates the encrypted Aegis vault fixture ONLY;
  the route script's own Welcome-import prefix IS the vault creation.
  Shared setup.py does not create a vault for this row. The merger must
  confirm this choice (or replace it with a shared setup that is provably
  safe for all 25 rows) before placement. The same pattern holds for
  every import/intro-prefix row.
- Per-route setup files are invoked by the runner as
  `setup_<route>.py` with `--gen-dir`; the ROUTES.csv `setup` cell names
  both the setup file and the generated file, as drycheck requires for
  `gen:` entries. All fixtures are `gen:` (run-time generated, never
  committed); no committed fixture file is used by this package.

## D7 re-audit O1 tightening, re-verified on the NEW sample

- New row 16 (GoogleAuthProtos$MigrationPayload.parser) IS the
  picker-gated scan-image route: dump steps 32-33 are
  `fireIntentLauncher(...)@QR_SCAN` and "the picker of another app
  returns the chosen image or file". Its methods.csv/dump ENV kind is
  other_app (the D7 plan's ENV_PICK_IMAGE wording for this route).
- New row 23 (DigitCountVerifier) carries NO system-picker env on its
  drawn chain: its steps contain no picker, scan-image, or camera step
  (the only "picker" steps are the in-app intro security picker at steps
  13-15); it is an export-side chain (TransferEntriesActivity generateQR
  to getUri to the protobuf verifier). It is therefore SCRIPTABLE with
  in-run entry seeding, not picker-gated.
- Row numbers for these two rows are UNCHANGED from the old numbering
  (16 and 23 in both draws); this was verified against the new dump, not
  assumed — the ENV order changes in the redraw were Scanner/AegisImporter
  only (new 12/14), which do not touch rows 16 or 23.

## Permissions, launch, and harness facts used

- Package com.beemdevelopment.aegis.debug; launch component
  com.beemdevelopment.aegis.debug/com.beemdevelopment.aegis.ui.MainActivity;
  receiver com.beemdevelopment.aegis.JacocoInstrument.SMSInstrumentedReceiver;
  APK apks/Aegis.apk; classes classes/Aegis/0 (from D7 plan, verified
  against the tree manifest there; not re-derived here).
- Permissions column: ONLY new row 12 (Scanner) lists
  android.permission.CAMERA, the already-granted variant
  (edge E4c53d66d, MainActivity.startScanActivity -> ScannerActivity).
  No other row lists a permission. CAMERA is the only dangerous runtime
  permission declared in the tree manifest (plus USE_BIOMETRIC/VIBRATE/
  RECEIVE_BOOT_COMPLETED, none of which is a runtime grant for these rows).
- No row's method is onRequestPermissionsResult, so the runner's
  pre-grant skip for that method literally never fires for Aegis.
- Harness primitives used by staged scripts: launch, tap, long_tap,
  type_text, scroll_to, wait_for, rotate, kill_app, relaunch, dwell,
  comment, done (phase-2 harness). No script uses fixed-coordinate taps
  without a `why` note except where the staging banner says the selector
  must be confirmed from a live dump. Long-press drag, multi-touch,
  background/kill/restore beyond kill_app/relaunch, and system-UI driving
  beyond picker/permission dialogs are NOT needed by any staged script;
  where a route needs rotation (row 18 preparation) or kill/relaunch
  (rows 18, 20), the script says so explicitly.
- Locale: no locale need is evidenced for any Aegis path row; no
  set_locale step is staged. If the coordinator's D9 gate requires one,
  that is a coordinator decision, not something this package invents.

## What this package deliberately does NOT contain

- No DEVICE rows, no verification.csv rewrite, no make_verification.py
  change (D7 verification plus synthetic test remain merger work; see
  COLLECT_COMPARE.md).
- No drycheck run against the branch graph (coordinator-dispatched).
  The staging self-checks actually run are listed in D1D3D7_REPORT.md:
  edge-list verification, py_compile, dry-mode script loads with the
  phase-2 harness, and generator runs into temp dirs. None of those is a
  D9 drycheck pass.
- No APK, zip, binary, secret, or token is committed in this package.
  Generated fixture files exist only in temp dirs from the staging test
  runs, never under turn/device-final/. Test passwords in scripts and
  generators are documented test-only values (notably "testpassword"
  for the generated Aegis vaults), never real credentials.
