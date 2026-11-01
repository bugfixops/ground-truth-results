# Aegis 3.4.2: method-level trigger graph (schema 2)

How every method of **Aegis** is triggered, in the standard configuration: the instrumented debug build (`beemdevelopment/Aegis@v3.4.2`, commit `619c1ab13cdd`, APK sha256 `0855ee49...`), an API 27 emulator, permissions and fixtures as in `final_java_only`. Labels follow `handoff/SCHEMA_V2.md`: REACHABLE or UNREACHABLE, ENV and STATE gates, edge classes (explicit, standard, non-standard), and how each label was confirmed.

## What is in this folder

| File | What it is |
|---|---|
| `aegis_trigger_graph.json` | pages, methods, `verdict`, `labels` (per-method fields), `edges` (with `edge_class`, `env_kinds`, `state_kinds`, stable ids), `paths` (verified paths only), `verification` (counts) |
| `methods.csv` | one row per method: verdict, UNREACHABLE reason, ENV and STATE kinds and texts, edge classes on the best route, whether an explicit/standard-only route exists, how the label was confirmed, path status, and the derived best route (`shortest_path`, `route_edge_ids`) |
| `../verification.csv` | the audit log: one row per label, edge or path that was checked, with result, how, and where (file:line) |
| `sanity_check.csv` | tool coverage (Monkey / APE, API 27) next to the labels; a one-way check only, it never sets a label |
| `aegis_trigger_graph.html`, `build_report.txt` | the viewer and the validation report |

## Numbers

- **2995 methods**, **12 pages** (including pseudo pages), **5483 edges**. Verdicts: **2537 REACHABLE**, **458 UNREACHABLE**.
- UNREACHABLE by reason: branch_never_taken 1, framework_never_calls 31, no_trigger_in_app 426.
- ENV gates (methods): hardware 41, other 1, other_app 121, permission 10, system_event 18, time 5. STATE gates (methods): data 136, file 1678, session 546, settings 24. Methods with no gate: 484.
- Edge classes: explicit 4456, non_standard 165, page 20, standard 842. Non-standard edges: 165 (Dagger / Hilt dependency injection: the library makes the link to the generated component; DialogInterface.OnClickListener.onClick (interface call; Dialogs.java:391-393; the listener is the lambda at AuthActivity.java:124-126); DialogInterface.OnClickListener.onClick (interface call; Dialogs.java:39).
- 1620 reachable methods have a non-standard edge on their best route; 765 have no explicit-or-standard-only route at all.
- Labels confirmed by: INFERRED 2719, SOURCE 276 (SOURCE: every edge of the best route cites a source line, in the app or in the Android 8.1 / library source; INFERRED: some edge rests on inference or on another app).

## How much to trust it

No verification log yet: every label is `UNCHECKED` and nothing is claimed beyond what the evidence column says.

Edges whose evidence is not a source line (804 of 5483): E5b266140 (AegisApplication.<init> -> Hilt_AegisApplication.onCreate); Ed430de74 (Hilt_AegisApplication.generatedComponent -> Hilt_AegisApplication$1.get); E1e4b62ae (AegisActivity.onCreate -> Hilt_AegisActivity$1.onContextAvailable); Ed3b2fc19 (Hilt_AegisActivity.generatedComponent -> DaggerAegisApplication_HiltComponents_SingletonC$SingletonCImpl.retainedComponentBuilder); E1c3ead1c (Hilt_AegisActivity.generatedComponent -> DaggerAegisApplication_HiltComponents_SingletonC$ActivityRetainedCBuilder.build); E9eaaba0b (Hilt_AegisActivity.generatedComponent -> DaggerAegisApplication_HiltComponents_SingletonC$ActivityRetainedCImpl.activityComponentBuilder); E9e40d82d (Hilt_AegisActivity.generatedComponent -> DaggerAegisApplication_HiltComponents_SingletonC$ActivityCBuilder.activity); E3c923e18 (Hilt_AegisActivity.generatedComponent -> DaggerAegisApplication_HiltComponents_SingletonC$ActivityCBuilder.build); E983da919 (AegisApplicationBase.onCreate -> AegisApplicationBase$AppLifecycleObserver.onStateChanged); E313f4f87 (S_PROCESS -> VaultLockReceiver.onReceive); Ed3c98a2a (S_PROCESS -> QsTileRefreshReceiver.onReceive); E436827e4 (MainActivity.onStart -> AegisActivity.onResume) ...

Sanity check against tool coverage (never used to set a label): 751 methods ran in the 1-hour Monkey / APE runs on API 27; **0** of them are labelled UNREACHABLE.

## What the re-audit changed (compared with the schema 1 graph)
Pending: this section is written when the Aegis graph reaches 0 errors.

## How the checked paths were chosen
Pending: this section is written when the Aegis graph reaches 0 errors.

## What waits for a device (API 27)
Pending: this section is written when the Aegis graph reaches 0 errors.

## Hazard candidates (from reading the code, not reproduced)
Pending: this section is written when the Aegis graph reaches 0 errors.

## Limits
- Warnings after the batch-36 build (96 errors, 68 warnings; batches 33 to 36 added none): 67 are UNREACHABLE consistency flags (the 62 listed below from batch 22, plus the two TextDrawable$Builder flags, the two Dialogs flags and the batch-30 flag at the end of this list), and one is the REVIEW line. Each flagged method is UNREACHABLE, and every incoming edge comes from a caller that is also UNREACHABLE. None has a REACHABLE or UNRESOLVED caller, so no edge contradicts a verdict. The reasons:
  - GlideOptions (26 methods): generated Glide option class. The app source has no reference to GlideApp, GlideRequest or GlideOptions (grep of src/main/java, 0 hits). The instance methods are reached only from the static xxxOf and xxxTransform factories, which are UNREACHABLE. The GlideRequest and GlideRequests clusters are labelled in batch 22 (see the bullets below).
  - GlideRequest.apply and GlideRequest.<init>(Class,RequestBuilder) (2): UNREACHABLE in batch 22. Their only in-universe caller is GlideRequest.getDownloadOnlyRequest (auto_calls.json rows), which is also UNREACHABLE: the download paths (download, downloadOnly) are never called by the app (grep of the Glide-importing app files). Same consistency flag as the rest of this list.
  - Glide library path (batch 22, INFERRED; the Glide library source is not read): into(ImageView) at ui/glide/GlideHelper.java:41 and :54 reaches GlideRequest.clone, autoClone, optionalCenterCrop, optionalCenterInside and optionalFitCenter only when the ImageView scale type maps to them. These five are ENV-dependent on the view's scale type and were not tested on a device. GlideRequest.lock and GlideRequests.clearOnStop are UNREACHABLE INFERRED because the library may call them internally.
  - GoogleAuthProtos MigrationPayload (13) and OtpParameters (17): generated protobuf accessors. The app reads the payload through getOtpParametersList, getBatchId, getBatchIndex and getBatchSize (GoogleAuthInfo.java:204-271), none of which is flagged. The flagged methods (singular getOtpParameters, hasBatchIndex, clear*, set*Value, *Bytes, addOtpParameters(int,...), setOtpParameters, removeOtpParameters) have no caller outside the generated file. The protobuf cluster is not finished (its other methods are still errors).
  - ApkSignaturePin (2: getFingerprint, getSHA256Fingerprint): vendored library (info.guardianproject.trustedintents). The callers are getMD5Fingerprint, getSHA1Fingerprint, getSHA256Fingerprint and doFingerprintsMatchCertificates, all UNREACHABLE; the app source does not call any of them.
  - TrustedIntents.isIntentSane (1): private method of the same library. Its callers isReceiverTrusted(Intent) and startActivity are UNREACHABLE; the app source does not call isReceiverTrusted.
  - EntryAdapter.onItemDismiss (1): the only caller is SimpleItemTouchHelperCallback.onSwiped (SimpleItemTouchHelperCallback.java:98), which is UNREACHABLE because the touch helper enables only UP and DOWN drag, so no swipe starts (batch 18).
- One REVIEW line (not a method warning): the NONSTD_HINT regex at tools/build_graph.py:61 flags 7 edges (Ed430de74, Ed3b2fc19, E1c3ead1c, E9eaaba0b, E9e40d82d, E3c923e18, Ebdc15ea3) whose evidence contains the words dagger, library or reflect. Their edges are plain FRAMEWORK edges, so they are false positives. Not fixed; tools/ is not edited.
- TextDrawable$Builder.rect and TextDrawable$Builder.roundRect (batch 28, 2 flags): each has one incoming CALL edge, from buildRect and buildRoundRect. Both callers are UNREACHABLE (no app code calls them; grep of the app tree). No REACHABLE or UNRESOLVED caller exists, so no edge contradicts a verdict.
- Dialogs (batch 29, 2 flags): Dialogs.showErrorDialog(Context,String,Exception,OnClickListener) has one incoming CALL edge from the UNREACHABLE 3-argument String overload (Dialogs.java:360), and Dialogs.showTextInputDialog(Context,int,int,TextInputListener,boolean) has one incoming CALL edge from the UNREACHABLE 2-argument showPasswordInputDialog (Dialogs.java:255). Both callers have no app call sites (bytecode call rows), so the flags are the same kind as the batch-22 list.
- NotificationService.serviceMethod (batch 30, 1 flag): its one incoming CALL edge is from onStartCommand, which is UNREACHABLE because nothing starts the service. The start call in VaultManager.startNotificationService is inside a comment (VaultManager.java:280-283, issue #1047), and the manifest entry is not exported (AndroidManifest.xml:105). Same kind as the flags above.
- Batch 30 open items for a device check (not tested): (a) SwitchPreference.setChecked(boolean) ignores its argument and always sets the switch on; the stored value is set through the androidx initial-value path (INFERRED, androidx source not read). Hazard candidate for the security page. (b) With android:fullBackupOnly="true" (AndroidManifest.xml:24), onBackup, onRestore and onQuotaExceeded are UNREACHABLE (INFERRED: the BackupAgent source is not in fw_src). A full-backup run on API 27 should show only onFullBackup and onRestoreFile running.
- DropdownCheckBoxes filter (batch 28, INFERRED): the framework runs the group filter (getFilter, performFiltering, publishResults, and the predicate lambda) even though typing is closed by app:allow_filtering="false" (dialog_export.xml:98, input type 0). The app source gives no trigger for that framework run, and the AutoCompleteTextView source is not held. A tool run recorded the filter running, so these four routes are REACHABLE. Open item for a device check: open the export dialog's groups field and see whether the popup filters the rows as the tap or the dialog opening triggers it.
- ENV-gated methods (on the best route, not tested on a device): MainActivity.handleIncomingIntent (ENV_VIEW, ENV_SEND); MainActivity.lambda$new$7 (ENV_PICK_IMAGE); ScannerActivity.<init> and onCreate (ENV_CAMERA); WelcomeSlide lambdas (ENV_PICKER); ImportExportPreferencesFragment.lambda$new$0 and IconPacksManagerFragment.lambda$new$0 (ENV_PICKER); BackupsPreferencesFragment.lambda$new$0 (ENV_BACKUP_RESULT); export RESULT lambdas (ENV_EXPORT_RESULT); BiometricSlotInitializer.onAuthenticationSucceeded (ENV_BIOMETRIC).

## JSON shape (short)

```
{ "schema": 2, "title", "screens": {page: description}, "methods": [...], "verdict": {method: REACHABLE|UNREACHABLE},
  "labels": {method: {unreachable: {kind, text}, env: [{kinds, text}], state: [{kinds, text}], route_edge_classes, explicit_standard_route,
                      confirmed_by, source_ref, path_status}},
  "edges": [ {id, src, dst, kind, edge_class, via, trigger, gui[], guard, reads[], writes[], note, needs_state, state_kinds, env, env_kinds, evidence, class_basis} ],
  "paths": [ {method, edges[], edge_classes, explicit_standard_only, env, state, verified_by, ref} ], "verification": {...} }
```

`src`/`dst` are methods (`Class.method`, overloads as `Class.method(Type,Type)`) or pages (`S_...`). A suffix `@CONTEXT` is the same method or page in a specific context. Edge ids are a hash of the edge content, so they stay stable when other edges change.
