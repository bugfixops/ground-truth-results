# Stream C leaf A — Aegis baseline build reconstruction report

Repo: bugfixops/ground-truth-results, branch work-2026-10-31, AEGIS ONLY.
No pushes, no branch edits, no device work (no emulator/adb/APKs/new repos).
No token used anywhere: every branch read went through the GitHub connector
(`get_file_contents`, one file at a time, ~30 s pauses). No 429 was hit.
Nothing below is marked passed without its own output.

## Command run (from the workdir root)

```
cd ~/workspace/overnight/stream-C/work
python3 -I tools/build_graph.py graphs/Aegis aegis > ~/workspace/overnight/stream-C/scratch/build_baseline.txt 2>&1
```

Invocation source (not guessed): `tools/build_all.sh` runs
`python3 -I tools/build_graph.py graphs/$a $p` from the work root, and
`graphs/Aegis/AGENT_NOTES.md` records the Aegis form as
`python3 -I tools/build_graph.py graphs/Aegis aegis` (prefix `aegis`).
`build_graph.py` usage line itself is
`python3 -I build_graph.py <graph_dir> <file_prefix>`.

## Saved output

- Full printed output (verbatim, stdout + stderr):
  `~/workspace/overnight/stream-C/scratch/build_baseline.txt`
- This report:
  `~/workspace/overnight/stream-C/scratch/baseline_build_report.md`
- Reconstructed workdir: `~/workspace/overnight/stream-C/work/`
  (`tools/` + `graphs/Aegis/`)

## Build result: FAILED — no printed counts exist

Exit code: 1. The build printed NO `methods …` line, NO `verdicts:` line,
NO `errors:` / `warnings:` lines, NO `build_report.txt`, and NO
`methods.csv` / trigger-graph JSON. `graphs/Aegis/out/` in the workdir is
empty. Therefore, honestly reported:

- UNRESOLVED: not printed (build died before the report section)
- errors: not printed (build died before the report section)
- warnings: not printed (build died before the report section)
- REACHABLE / UNREACHABLE totals: not printed
- STALE presence: no STALE lines in the output (there is no output to
  contain any; this is NOT a claim of "no STALE")
- STRICT value: not printed by the build. For reference only, the
  reconstructed source sets `STRICT = True` at `graph_def.py` line 10
  (and `USE_AUTO = True` at line 9) — that is a source fact, not a
  build-printed value.

Verbatim failure (full text is in `build_baseline.txt`):

```
Traceback (most recent call last):
  File ".../tools/build_graph.py", line 731, in <module>
    sys.exit(main(sys.argv))
  File ".../tools/build_graph.py", line 334, in main
    exec(compile(open(src_path, encoding='utf-8').read(), src_path, 'exec'), ns)
  File "graphs/Aegis/graph_def.py", line 1582, in <module>
    _UNIV_SHORT = [_r['short'] for _r in _json.load(open('/Users/darshan/Desktop/yang/work/graphs/Aegis/method_list.json'))]
FileNotFoundError: [Errno 2] No such file or directory: '/Users/darshan/Desktop/yang/work/graphs/Aegis/method_list.json'
```

## Blocker 1 (reached, fatal): hardcoded author-machine path

`graphs/Aegis/graph_def.py` line 1582, top-level code executed during the
build's `exec`, opens the absolute path
`/Users/darshan/Desktop/yang/work/graphs/Aegis/method_list.json`.
It is the ONLY `/Users/` reference in `graph_def.py`. That path does not
exist on this VM, and it is outside the permitted write scope, so it was
not created and the reconstructed file was not edited to work around it
(editing it would no longer be a faithful baseline copy and would break
the SHA verification below). Context of the line: the batch-7 block reads
the method universe so every method of the generated Glide classes
(GlideApp / GlideOptions) is covered by an UNREACHABLE entry.

Fix needed before any baseline build can print counts (decision for the
parent, not taken here): either run on a machine where that path exists,
or authorise a change to that line (e.g. a relative `GDIR`-based path)
as a deliberate, recorded deviation from the branch copy — not as a
silent baseline.

## Blocker 2 (not yet reached, will be fatal next): auto_calls.json too large for the connector

`graphs/Aegis/auto_calls.json` (1,625,494 B on the branch) could NOT be
fetched. The connector returned:

> File graphs/Aegis/auto_calls.json is too large to display (1625494
> bytes). Use the download URL to fetch the content: …

The suggested download URL was NOT used: it carries a token, and this
task forbids tokens in URLs/files/logs/messages. `get_file_contents`
takes no range/chunk parameters (verified from its live input schema:
only owner/repo/path/ref/sha/fields), so there is no connector-native
chunked fetch. Its content was NOT invented or reconstructed.

Why it matters: with `USE_AUTO = True`, `build_graph.py` `add_auto_edges`
opens `graphs/Aegis/auto_calls.json` unconditionally, so once Blocker 1
is resolved the build will fail again at that open unless this file is
obtained by another authorised route. Its SHA below comes from the
branch directory listing / the connector's too-large message only — it
is NOT verified against a local copy, because no local copy exists.

## py_compile (separate check, passed on its own output)

```
python3 -m py_compile graphs/Aegis/graph_def.py   -> OK
python3 -m py_compile tools/build_graph.py        -> OK
```

py_compile passing does not imply the build passes; the build failure
above is a runtime path lookup, not a syntax error.

## Step 1 — tools/ directory listing (connector, branch work-2026-10-31)

53 entries (52 files + 1 directory `tests/`). Named tools from the task:

| file | size (B) | connector SHA (from listing) | present? |
|---|---|---|---|
| build_graph.py | 38050 | b0589d32fa0f159210895da529554fd42501b3a1 | yes, fetched + SHA-verified |
| build_all.sh | 435 | de935ac6e456145673efd58570cc6d127c934ad6 | yes, fetched + SHA-verified |
| check_citations.py | 4680 | 81f52dec7ed9435cfa6da9ba001a6ff44095d1da | yes, listed only (not fetched) |
| check_routes.py | 2747 | 1e14cdfeb85ceb2f08a1aaa53252f8d7190e19ac | yes, listed only (not fetched) |
| check_bytecode_lines.py | 5020 | f16d37ba77cafc01bfd1fa1c314c3c66df97fc4b | yes, listed only (not fetched) |
| scan_unreachable.py | 5716 | ec3329fc6cffe6a7a1f639873067b0dffa595dc0 | yes, listed only (not fetched) |
| verify_sample.py | 2373 | 9edb841a1dd5b7c1732ef839c926b79d0603d420 | yes, listed only (not fetched) |
| show_route.py | 5314 | 141e53a379cdeeebcb02cfbe424114b6033b3a36 | yes, listed only (not fetched) |
| gen_readme_v2.py | 9223 | 15337a8675cde3a08fe8722b238764a577e8303c | yes, listed only (not fetched) |
| make_verification.py | — | — | NO — absent from tools/ (no such entry; do not assume it exists) |

Other tools/ entries (listed, not fetched): build_graph_v1–v8_backup.py,
calibrate.py, cases.py, check_gen.sh, compare_graphs.py, contra.py,
coverage_methods.py, dead_by_class.py, emu_compare.py, extract_calls.py
(+ v1–v3 backups), gen_edges.py, gen_readme.py, hubs.py,
keyword_clusters.py, list_methods.py (+ v1 backup),
make_test_manifest.py, make_worklist.py, new_graph_def.sh, prep_app.sh,
publish_graphs.py, rd.sh, resume_convert.sh, resume_v5.sh, run_models.py,
sample_paths.py, show_frontier.py, show_paths.py, summary_table.py,
unhit_by_class.py, viewer_template.html (+ v1 backup),
write_summaries.py, and directory tests/.

## Step 2 — files fetched, with connector SHAs (git-blob SHA-1 recomputed locally, all matched)

| local path | bytes | connector SHA | local recomputation |
|---|---|---|---|
| work/tools/build_graph.py | 38050 | b0589d32fa0f159210895da529554fd42501b3a1 | match |
| work/tools/build_all.sh | 435 | de935ac6e456145673efd58570cc6d127c934ad6 | match |
| work/graphs/Aegis/graph_def.py | 487286 | 13db434fc5caee17c3f63e1efd0f9034e6425eb6 | match, 4983 lines |
| work/graphs/Aegis/method_list.json | 695547 | 897bd208430bf85dfb497594d52ebd376034ce75 | match, valid JSON list of 2995 entries |
| work/graphs/Aegis/AGENT_NOTES.md | 199341 | ff62d457ca067aa0153295821a2e985eb471a3e4 | match, 670 lines |

NOT fetched (see Blocker 2): `graphs/Aegis/auto_calls.json`,
1,625,494 B, SHA e60247617dac7d8a1eed0d2d399d533c386259b6 (from branch
listing only, unverified locally). NOT fetched and not needed to diagnose
the failure: `coverage_baseline.json` (optional sanity check only),
`verification.csv` (optional; branch graphs/Aegis/ listing shows no
`verification.csv` at top level), `viewer_template.html` (HTML output is
skipped if absent; the build never reached that step).

Branch `graphs/Aegis/` listing (11 entries): `.list_methods.log`,
`AGENT_NOTES.md`, `auto_calls.json`, `coverage_baseline.json`,
`generated_draft_graph_def.py.txt`, `graph_def.py`,
`method_list.json`, `readme_notes.md`, `review_notes.md`, plus
directories `out/` and `scratch/`.

## What was NOT done (per the task's hard rules)

- No push, no branch edit, no file written outside
  `~/workspace/overnight/stream-C/work/**`,
  `~/workspace/overnight/stream-C/scratch/build_baseline.txt`, and this
  report. No other app touched; Aegis only.
- No token waited for, used, or written anywhere.
- No label, count, or check marked passed without its own printed
  output. In particular: no REACHABLE/UNREACHABLE totals, no error /
  warning counts, and no STALE verdict are claimed for this build.
- No tool-coverage, old generated graph, or old build count was used as
  label evidence, and no `search_code` 0 was treated as absence
  evidence (no search_code call was needed).
- `confirmed_by` values were not assigned to anything here (no labels
  were produced).

## Bottom line for the parent

Baseline build NOT established. Two blockers, in order:
1. `graph_def.py:1582` hardcodes
   `/Users/darshan/Desktop/yang/work/graphs/Aegis/method_list.json` —
   missing on this VM (FileNotFoundError, exit 1, no counts printed).
2. `graphs/Aegis/auto_calls.json` (1,625,494 B) exceeds the connector's
   display limit and cannot be chunk-fetched through `get_file_contents`
   — it will block the next step once (1) is resolved.
Reconstruction itself is complete and SHA-verified for every file the
connector could deliver; py_compile passes for `graph_def.py` and
`build_graph.py`.
