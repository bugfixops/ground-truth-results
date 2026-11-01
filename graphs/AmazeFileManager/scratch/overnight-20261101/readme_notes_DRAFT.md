# AmazeFileManager — readme_notes DRAFT (local mirror only, NOT generated)

Status: DRAFT. This file was written by hand as a draft for the merger.
It has NOT been processed by tools/gen_readme_v2.py (that tool needs
out/ from a successful local build, which is blocked — see Blockers in
scratch/route_checks_consolidated.md). Do NOT copy this file to the
branch as readme_notes.md until the build passes and gen_readme_v2.py
has been run on a full checkout. The five headings below are in the
required order.

## What the re-audit changed (compared with the schema 1 graph)

- Labels re-derived from printed source under schema 2: every method in
  method_list.json (2981) carries exactly one of REACHABLE / UNREACHABLE
  with, for UNREACHABLE, a kind, a reason, and a source reference;
  confirmed_by is SOURCE or INFERRED only.
- The branch build report (re-fetched 2026-11-01) records 2509 REACHABLE
  / 472 UNREACHABLE (closed_by_api_level 9, framework_never_calls 39,
  no_trigger_in_app 424), 7768 edges, errors 0, warnings 0.
- Stream B overnight proposals (UNVERIFIED, not merged): correction of
  the SftpConnectDialog lambda edge E89e2cedd (wrong lambda source,
  citation one line off), the CompressedExplorerFragment extract edge
  (wrong/missing <init> edge), and REACHABLE proposals for
  GlideRequest.listener, GlideRequest.clone,
  IconDataParcelable.setImageBroken, and (INFERRED step)
  GlideRequests.as, plus prior proposals for
  LayoutElementParcelable.writeToParcel,
  RoundedImageView.setBackgroundColor, and
  SimpleTextWatcher.beforeTextChanged / onTextChanged. See
  scratch/route_checks_consolidated.md for the full list and the two
  citation corrections made tonight (clone line :45, not :44; Sftp $5
  descriptor-order claim softened to elimination only).

## How the checked paths were chosen

- Intended: the stratified 30-route sample from
  `python3 -I tools/verify_sample.py AmazeFileManager 30 20261025`,
  judged step by step against printed source lines.
- Actual tonight: the sampler could NOT be run — out/methods.csv
  (1,179,770 bytes) exceeds the GitHub connector's display limit and
  there is no chunk/range read. The routes judged tonight are therefore
  an issue-first set (the 21 build-report contradictions and the two
  named edges E89e2cedd / Ee1aeff93), NOT the stratified sample, and no
  sample error rate is claimed. The sample must be drawn, printed, and
  judged on a full checkout before this section can be finalised.

## What waits for a device (API 27)

- Device checks have NOT started (overnight instruction: no emulator,
  adb, APKs, or new repos tonight). Everything below waits for the
  user-chosen emulator setup.
- Replay of the sampled routes on an API 27 debug build, fresh install,
  runtime permissions granted only where a route needs them, to confirm
  labels with DEVICE evidence where the source leaves a step INFERRED
  (framework dispatch: Fragment/DialogFragment lifecycle, AsyncTask
  onPostExecute, RecyclerView binding, ListPreloader, Bundle marshalling,
  TextView watcher dispatch, generated Glide delegation).
- The TextEditorActivity.<init> ENV-gate question (ENV-gated but ran in
  a tool run) needs the graph's ENV edge text plus the manifest and
  FileUtils launch path printed, and then a device replay to check
  whether the gate condition was actually satisfied.
- AboutActivity is labelled from src/fdroid under the standard
  configuration; its device behaviour in the fdroid flavor is part of
  the device-check pass, not tonight's work.

## Hazard candidates (from reading the code, not reproduced)

- None confirmed tonight. The following are reading notes only, not
  reproduced hazards, and each needs a printed source line before it
  can be listed as a hazard candidate:
  - The SftpConnectDialog host-key flow: the :175 guard
    (!isEmpty(sshHostKey)) selects between two different fingerprint
    task creations (:178 vs :203); a wrong lambda attribution (E89)
    hid which task executes after removeConnection.
  - Method-reference edges (IconDataParcelable.setImageBroken) and
    Parcelable callbacks (LayoutElementParcelable.writeToParcel) are
    invisible to a bare-name call search; any hazard or reachability
    claim that relies on "no call site found" must use a
    receiver-aware / interface-aware search instead.
  - Generated Glide code (GlideRequests / GlideRequest / GlideOptions)
    is not in final_java_only; claims about its dispatch are INFERRED
    until build-generated sources are printed.

## Limits

- No local build, sampler run, or eight-check run was possible tonight:
  graph_def.py (1,058,622 bytes), auto_calls.json (1,839,161 bytes),
  and out/methods.csv (1,179,770 bytes) all exceed the connector's
  display limit, get_file_contents has no range parameter, and the
  token-bearing download URL was not used (hard constraint). The
  branch's prior build report (0 errors / 0 warnings) is quoted as the
  branch's own output, not as a fresh local result.
- No full AmazeFileManager source tree exists on this VM; only 10 java
  files were locally printed. Whole-tree claims (notably the 13 OPEN
  Glide methods, SimpleTextWatcher.afterTextChanged, and the
  TextEditorActivity ENV gate) stay OPEN until a receiver-typed grep
  over the full tree and the generated Glide sources are printed.
- Tool coverage (Monkey / APE / JaCoCo) was used only as a pointer to
  which methods to look at, never as evidence for any label.
- No label, edge, or log in this draft has been merged or pushed.
