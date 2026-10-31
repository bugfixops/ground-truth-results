# Next step (NOT STARTED): replay the routes on API 27 emulators in GitHub Actions

Status: planned. Start only when the user says go, and only after all app conversions have finished (the overnight convert run, Aegis, AmazeFileManager and LibreTorrent).

Repo: https://github.com/bugfixops/test-13 (public).

## Why
Yang's rules need DEVICE confirmation for labels and routes. Right now the eight ticked apps have 0 DEVICE rows. Only 215 of 8,583 reachable methods have a route that was read against the source. The earlier repo, bugfixops/work-emulator, runs Monkey only, and Monkey cannot decide labels.

## Before any push or run (in this order)
1. Check the environment variables and secrets the workflow needs. List them in this file. Secrets go in the GitHub repo settings only, never in a file. The repo is public, so never print or commit a secret.
2. Decide what to push. Only what runs the emulator: the workflow file, the route scripts, the APK list and the fixtures they need. No graph notes, no email address, no personal data, no tokens.
3. Commit with the neutral identity bugfixops <bugfixops@users.noreply.github.com>. Never use the global git identity.
4. Get the user's go-ahead for the push and for each run.

## Method (when started)
- Write one route script per sampled route. Each script follows the printed steps of that route (taps, text entries, the permission answer). Monkey is not used for route checks.
- Run each app on an API 27 x86_64 emulator. Record, per route: reached (yes or no), the screens and steps seen, and the logs.
- Pull the results into work/emulator_runs/. Compare with the graphs (tools/emu_compare.py).
- Add DEVICE rows to verification.csv only for routes that were actually reached. A route that was not reached is "unclear" until the script is checked. A failed script is not evidence that the route is wrong.
- No label changes from one device run without reading the source again.

## Scope (decide when started)
- Routes per app: start with 30 per app. Increase for Omni-Notes, Vanilla-Music, Markor, hash-checker, and AnyMemo's edges (the first-draft error rates are high there).
- Storage permission for gated routes: grant it per route, as the standard configuration says, or pre-grant it. Yang decides.
- Order of apps.
- Whether to delete the repo afterwards.

## Pipeline marker
work/handoff/PROGRESS_V2.md has the line "[N]" for this step. No script reads it. It is not ticked.

## Open decisions for the user
- Go or no-go, and when.
- Routes per app.
- Permission grant rule (Yang).
- Delete the repo afterwards, or keep it.
