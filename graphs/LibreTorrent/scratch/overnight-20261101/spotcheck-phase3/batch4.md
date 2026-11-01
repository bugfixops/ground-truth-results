# Spot-check — batch 4 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json, plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). Row 11 is in both sets; checked once, under Changed. Verdicts D1–D36/R1–R5 are NOT re-decided. No work file edited.

## Changed rows (1)

- 4/11 UriConverter.\<init\> — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose (label, kind, confirmed_by correct per L5 D13/D32: all methods static — UriConverter.java:27 class, static toUri :30-32, static fromUri :36-38, no explicit ctor; saved grep greps/L5/grep_4_11_uriconverter.txt shows only the import, the @TypeConverters registration, and the definition — zero `new UriConverter`). Stale prose contradicts the new label: "DISPUTED row, kept OPEN", "Do NOT merge this row as UNREACHABLE on the current evidence", "no `new UriConverter` in any printed file … so the row stays OPEN", "DECISION 2026-11-01 (D3c/D1): D3c decides this row stays OPEN". (Confirmed_by reads INFERRED from the trailing cell "INFERRED Kind: `no_trigger_in_app`. [Phase 3 completion … L5 verdict applied.]".)

## Sample rows (7 sample-only)

- 4/1 TorrentDownloadImpl.isDownloading — UNREACHABLE no_trigger_in_app INFERRED — PASS. Interface method + implementation only; no caller in the printed implementation file.
- 4/6 FeedRepositoryImpl.getSerializeFileFormat — UNREACHABLE no_trigger_in_app INFERRED — PASS. Implementation + interface declarations only; no caller in the printed implementation file.
- 4/16 FileSystemFacadeImpl.lastModified — UNREACHABLE no_trigger_in_app INFERRED — PASS. Facade method with no printed app caller; dispatcher for rows 13 and 29, which stand or fall with it.
- 4/21 SafFileSystem.openFD(Uri,String,String) — UNREACHABLE no_trigger_in_app INFERRED — PASS. Outer overload delegating to row 20; no printed caller.
- 4/26 SafFileSystem$FakePath.isFakePath — UNREACHABLE no_trigger_in_app INFERRED — PASS. Definition only; no caller in any printed file (distinct from Utils.isSafPath).
- 4/31 NormalizeUrl.\<init\> — UNREACHABLE no_trigger_in_app INFERRED — PASS. All-static utility class; no construction site printed (row itself corrects the audit's "private constructor" reason).
- 4/36 BindingAdapterUtils.\<init\> — UNREACHABLE no_trigger_in_app INFERRED — PASS. All-static utility class; no explicit ctor, no construction site printed.

Totals: checked 8 (1 changed + 7 sample-only) — PASS 7, FAIL-prose 1, FAIL-label 0.
