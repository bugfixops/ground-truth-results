# Emulator test plan: redroid on EC2, ground truth for the 13 trigger graphs

> **UPDATE 2026-10-25 (evening) - on hold.** Yang's ground-truth requirements and audit (memory `ground-truth-requirements`) replace the premises of this plan:
> tool coverage (Monkey/APE) cannot decide labels, only serve as a one-way sanity check; the 1,057 targets below were drawn from the old graphs, whose generated
> part (8 apps) Yang found unreliable (paths 10/25 fine) and which will be rebuilt by hand; the five hand-written graphs get new labels and fields.
> The 60-minute Monkey run on GitHub Actions (run 40211765388) was cancelled. Still valid: the API 27 emulator set-up on GitHub Actions (section 8) and the rule that the
> emulator is used for DEVICE confirmation and path replays on the *verified* graphs. Regenerate the targets from the new graphs before using any of this.

Written for Darshan (and Yang) to set up and run the tests. Nothing here has been run yet; every number comes from files in `work/`, every estimate is marked as an estimate.

## 1. What the emulator has to settle

The graphs are static. The emulator is the oracle: the instrumented APKs write JaCoCo method coverage, so for any scenario we can say which methods ran. A *hit* proves a method is reachable under the test conditions. A *miss* proves nothing by itself.

| # | Question | Graph claim tested | How | Pass criterion |
|---|---|---|---|---|
| Q1 | Is dead code really dead? | 2,891 methods marked DEAD / FRAMEWORK_ONLY | passive check in every run + 245 targeted attempts (`DEAD_SAMPLE`) | 0 hits (any hit is a contradiction and a generator bug) |
| Q2 | Is `REACHABLE` right? | the shortest paths of the never-run methods | follow the path of 125 frontier nodes (in front of about 1,900 never-run methods) and 238 random clean samples | share of targets hit along the predicted path; every miss classified |
| Q3 | Are the gates right? | `needs_state` on 111 samples | run with the setup (expect hit); run without it (expect miss) | gate confirmed / refuted per target |
| Q4 | Does the outside world work as modelled? | `env` edges that adb can inject (81 `ENV_ENTRY`) | `am start`, `am broadcast` with the action and data | hit when injected |
| Q5 | Is redroid equivalent to the baseline? | 130 `CONTROL_HIT` methods the baseline ran + a second 1-hour baseline | same paths; same tools, flags and seed | at least 90% of the controls hit; coverage of the new run close to Yang's |

Interpretation rules: a hit on a DEAD method refutes the graph; a miss on a REACHABLE target is classified (wrong step, needs state, needs environment, UI mismatch, crash, harness problem) and is not automatically a graph error; methods that need telephony, sensors, camera, GPS, Bluetooth, NFC, biometrics or Google services are recorded as `NOT_TESTABLE`, not as refuted.

## 2. Environment

**Image and API level.** The baseline used API 27. redroid publishes `redroid/redroid:8.1.0-latest` (Android 8.1 = API 27). Android 9 and older need the `ashmem_linux` kernel module (removed in kernel 5.18) unless `androidboot.use_memfd=true` works for 8.1 (not documented, so unverified). **Phase 0 must settle this.** Fallback: `11.0.0-latest` (API 30), clearly labelled, with the Q5 comparison against the API 27 baseline.

**Instance (estimate, to be measured in Phase 0).** One 32-vCPU / 128 GB instance (for example a Graviton `m7g.8xlarge`, or an x86 `m7i.8xlarge`) holds the 13 containers at once: about 2.5 vCPU and 9 GB each. Both CPU architectures work for our APKs: the four with native code (Aegis, LibreTorrent, MMEX, openlauncher) ship `arm64-v8a` and `x86_64`; the other nine have none. Running Monkey and APE for every app at the same time (26 containers) needs about twice that, so either two such instances or two waves.

**Host setup (Ubuntu 22.04 with a 5.15 kernel, where ashmem can still exist; check with `modprobe`):**
```
sudo apt install docker.io linux-modules-extra-$(uname -r)
sudo modprobe binder_linux devices="binder,hwbinder,vndbinder"
sudo modprobe ashmem_linux          # needed for Android 8.1 unless memfd works
```
**One container per app** (own host port and data directory; the adb port bound to localhost only):
```
docker run -itd --rm --privileged --name rd-<App> -v ~/data/<App>:/data -p 127.0.0.1:<5555+i>:5555 \
    redroid/redroid:8.1.0-latest androidboot.redroid_width=720 androidboot.redroid_height=1280 androidboot.redroid_dpi=320
adb connect localhost:<5555+i>
```
**Security:** security group open for SSH from your IP only; never publish the adb port (the redroid README warns that the host can be compromised through it); copy the APKs and fixtures with `scp` or a private S3 bucket (no public GitHub needed); terminate the instance when done.

**Coverage probe (from the dataset, verified in its source):** `am broadcast -a edu.gatech.m3.emma.COLLECT_COVERAGE -n <applicationId>/<receiver class>` (receiver class = the `receiver` column of `final_java_only/MANIFEST.csv`). The receiver writes `/data/data/<applicationId>/files/coverage.ec` (overwritten each time) and **resets the counters after every dump** (`getExecutionData(true)`), so each dump is the coverage since the previous one. Pull it with `adb pull` (root) or `run-as`, convert with `jacococli report --classfiles ... --xml`, and map to our method names with `tools/coverage_methods.py`.

**Baseline commands to reuse (from the `status.json` files):**
- Monkey: `timeout -s INT 3600 monkey -p <pkg> -s 20261016 --throttle 500 --ignore-crashes --ignore-timeouts --ignore-security-exceptions -v -v 100000000`
- APE: `CLASSPATH=/data/local/tmp/ape.jar app_process /system/bin com.android.commands.monkey.Monkey -p <pkg> -s 20261016 --throttle 500 ... --ape sata --running-minutes 60` (needs `ape.jar`, which is not in our folders)
- Coverage pulled about every 30 s (about 120 segments per hour).

## 3. Phases

| Phase | What | All at once? | Time (estimate) |
|---|---|---|---|
| 0. Feasibility | one container with Android 8.1 boots; `ro.build.version.sdk` = 27; install + `-g` permissions; fixtures pushed; probe broadcast + pull + jacococli work and the second dump is empty (reset); Currency network and certificate; 13 containers up together (measure RAM and CPU); 60 s Monkey sanity run | one, then 13 | 0.5 to 1 day (kernel modules are the unknown) |
| 1. Tool runs | 60 min Monkey and 60 min APE per app, same seed and flags; compare with Yang's coverage; every dead method checked | yes: 13 containers per wave | about 3 h for both waves including setup |
| 2. Injection | `am start` / `am broadcast` for the 81 `ENV_ENTRY` targets (incoming VIEW / SEND intents, exported components, receivers) | yes: per app in parallel | 0.5 day to write, minutes to run |
| 3. Guided scenarios | scripted paths for `FRONTIER`, `CLEAN_SAMPLE`, `SETUP_SAMPLE`, `CONTROL_HIT`, `DEAD_SAMPLE`, `ENV_SAMPLE`; each scenario: restore base state, reset coverage (one discarded dump), run steps, dump, compare | yes: one container per app, scenarios in sequence | 2 to 3 days to author, about half a day to run |
| 4. Analysis | per-app `VERIFY.md` (predicted vs observed, refuted predictions with evidence), `DYN` evidence and corrected verdicts in the graphs, generator fixes, final precision numbers | | 0.5 day |

Total: about 4 to 6 working days (estimate) and 25 to 40 instance-hours, roughly $30 to $60 on demand plus storage (check current EC2 prices).

## 4. What is tested for each app

Targets are generated (seed 20261025) into `emulator_tests/<App>/targets.csv` with expected outcome, taps, setup and environment notes; counts in `emulator_tests/SUMMARY.md`.

| Category | Targets | Expected |
|---|---:|---|
| `CONTROL_HIT` | 130 | HIT (harness check) |
| `FRONTIER` | 125 | HIT after crossing the frontier |
| `CLEAN_SAMPLE` | 238 | HIT along the path |
| `SETUP_SAMPLE` | 111 | HIT with setup, MISS without |
| `ENV_ENTRY` | 81 | HIT when injected |
| `ENV_SAMPLE` | 127 | UNKNOWN: record |
| `DEAD_SAMPLE` | 245 | MISS (a hit is a contradiction) |
| **Total** | **1,057** | |

Scenario format: a small YAML per target (`tap id=`, `tap text=`, `menu`, `type`, `swipe`, `key BACK`, `am start`, `am broadcast`, `push`, `wait`), driven by UI Automator (`uiautomator dump` + `input`). Steps that name `R.id.x` map to resource ids automatically; steps with only a variable name or label need a person (or me) to read the screen once. At run time nothing needs an LLM.

## 5. Per-app base state and extra fixtures

| App | Base state before scenarios | Extra fixtures for gated targets |
|---|---|---|
| Currency | network up (ECB); certificate problem on API 27 and below | none |
| Diary | none | none |
| hash-checker | a file as input (Download fixtures) | none |
| openlauncher | none known; check the default launcher in Phase 0 | none |
| Omni-Notes | Pictures pushed; a few notes, a category, a password, an archived and a trashed note, a reminder | audio file |
| Vanilla-Music | Music pushed and scanned | one ogg, flac, opus and m4a file |
| AnyMemo | a deck created or imported | Mnemosyne, SuperMemo, QA-text files |
| Markor | **`Documents` folder is missing in the fixtures** (create it); finish the first-run tutorial | `.jenc`, Wikitext, AsciiDoc and KaTeX samples |
| Aegis | create the vault (first run), then add entries by hand | other authenticator apps' export files |
| AmazeFileManager | fixtures pushed | 7z, gz, bz2, tar, an `.apk`, a `.db`, an encrypted file |
| AnkiDroid | import `sample_deck.apkg` (VIEW intent, tap ADD) | none |
| MMEX | finish the tutorial, create a database with accounts and transactions | none |
| LibreTorrent | none at first, then add a torrent | a tiny `.torrent` and its data |

Fixtures already on hand (`final_java_only/_fixtures`, 4.7 MB): Download (19 files: `archive.zip`, `table.csv`, `todo.txt`, `tasks.org`, `notes.md`, `journal.md`, `page.html`, `sample.pdf`, `sample_deck.apkg`, `config.xml`, `data.json`, `events.ics`, `contacts.vcf`, six images), Music (12 mp3 + 3 wav), Pictures (6 jpg), `contacts.json`.

## 6. Risks and limits

- **Kernel modules on EC2** (binder, ashmem): decided in Phase 0; the fallback changes the API level.
- **redroid is a container on the host kernel, not the baseline emulator:** no telephony, SMS, sensors, camera, GPS, Bluetooth or NFC, and probably no real launcher widgets. Those targets become `NOT_TESTABLE`.
- **Random tools are not reproducible:** the same seed on another host gives another trace, so Q5 compares coverage levels, not hit sets.
- **State restore:** first-run flows (tutorial, vault, database) must be rebuilt for every scenario; keep a tarball of each app's data directory per base state.
- **Crashes lose coverage** between dumps: dump before and after every scenario.
- A scenario can prove reachability only; a miss is evidence, not proof.

## 7. Decisions needed

1. AWS account, region and instance size (one 32-vCPU instance for 13 apps at once, or two smaller ones).
2. Whether the Android 11 fallback is acceptable if 8.1 does not run on the instance kernel.
3. Whether to include APE (needs `ape.jar`) or run Monkey only in Phase 1.
4. Who writes the scenarios: I can draft all of them from `targets.csv`; the steps without a resource id need one look at the screen.

## 8. Phase 1 on GitHub Actions (set up 2026-10-25, instead of EC2/redroid for the first runs)

The Monkey runs of Phase 1 do not need redroid: GitHub's hosted runners run a normal Android emulator with hardware acceleration (KVM).
Repository `bugfixops/work-emulator` (public, to be deleted once the results are downloaded), local copy `yang/work-emulator/`.

- **What a job does:** one job per app, all in parallel (13 jobs). It boots an API 27 x86_64 AOSP emulator (`default` target; the `google_apis` image has no x86_64 for API 27), installs `apks/<App>.apk`, pushes `fixtures/` to `/sdcard`, then runs the baseline Monkey command (`-s 20261016 --throttle 500 --ignore-crashes --ignore-timeouts --ignore-security-exceptions -v -v`) for N minutes under `timeout -s INT`, with the coverage broadcast every 30 s (about 118 dumps per hour, like the baseline). The dumps are merged and reported with JaCoCo 0.8.8 (the version of the baseline reports) and the staged class directories, which reproduce Yang's baseline `report.xml` method for method for all 13 apps (checked locally).
- **Start a run:** Actions tab, "Emulator run", "Run workflow"; or change `ci/run.conf` (APPS, MINUTES, TOOL, SEED) and push to `main`.
- **Results:** artifact `results-<App>` (7 days) and, without any login, the branch `results`: `git clone --branch results --depth 1 https://github.com/bugfixops/work-emulator.git`, folder `runs/<run id>-<attempt>/` with `SUMMARY.md`, `summary.csv` and per app `meta.json`, `methods_hit.csv` (class, method, desc, hit), `merged.ec`, `report.csv`, `report.xml.gz`, `segments.csv`, `segments.tar.gz`, `tool.log.gz`, `logcat_crash.txt`.
- **Compare with the graphs:** `python3 -I tools/emu_compare.py <run folder>` (from `work/`) writes `analysis/SUMMARY.md` and per app CSVs: coverage overlap with the baseline Monkey run (Q5), hits on DEAD / FRAMEWORK_ONLY methods (Q1; any hit refutes the graph), and methods that neither baseline run reached (new dynamic evidence).
- **Pilot (run 40211173286):** Currency and hash-checker, 3 minutes each, finished green in 5 minutes: 7 and 8 valid dumps, 41 of 145 and 147 of 525 methods hit, 0 contradictions.
- **Not done in this phase:** the guided scenarios (Phases 2 and 3), APE (needs a built `ape.jar`), first-run setups (Aegis vault, AnkiDroid import, Markor tutorial, MMEX database). `fixtures/Documents` is our reconstruction from the Download text files.
