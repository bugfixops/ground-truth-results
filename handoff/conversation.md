# Claude Code session: Android trigger-graph task (2026-10-24)

_Readable export: user messages and assistant replies only. Tool calls, command output and file contents are left out._


---

### User

These are the papers I'm working on. APEX, GAPS and TraceDroid. Also attach current draft(lack so many stuffs).
If you has time, you can also see the Goal explorer and ADGE (It's fine if you have time).

And here are the all 13 apps (not 19, only 13 java only app).final_java_only.zip

Here are the example of the graph I showed you. 2 MD file is the prompt to generate it. share.zip

If you find any error/ bug or question. Just reach me thought whats app or discord.

what does this mean, this folder has everything check now


---

### Claude

Now the two prompt files and the draft.

Now let me look inside one app folder and the top-level CSVs.

The message is a handoff. It gives you the background papers, the current paper draft, the 13 test apps, and a worked example of the "trigger graph" plus the prompts used to make it. I unzipped both archives and checked them. Everything the message mentions is in the folder, but I found a few mismatches worth asking them about.

## What each part of the message means

| They said | File | What it is |
|---|---|---|
| "papers I'm working on: APEX, GAPS, TraceDroid" | the 3 PDFs | The three tools the study compares. Each one tries to drive an Android app until a chosen method runs. |
| "current draft (lacks so many stuffs)" | [icst-2027-draft.pdf](icst-2027-draft.pdf) | A study for ICST 2027. It only describes the plan: every results table is empty dashes and there are about 10 TODOs. |
| "Goal Explorer and ADGE, if you have time" | 2 PDFs | Related tools the draft mentions but doesn't run. Optional reading. |
| "13 Java-only apps" | `final_java_only.zip` | For each app: the APK with coverage measurement built in, its source, the compiled classes, and coverage reports from 1-hour runs of two automated testers (APE and Monkey). |
| "example of the graph" + "2 MD files" | `share.zip`, [GRAPH_PROMPT.md](GRAPH_PROMPT.md), [GENERIC_PROMPT.md](GENERIC_PROMPT.md) | A worked example for the Currency app: for each method, which screen and which user action make it run. The two files are the prompts you give a coding agent to build such a graph. GRAPH_PROMPT works from source only. GENERIC_PROMPT adds checking on an emulator. |

**How it fits together.** This is my inference; the message never says what your task is.
1. Build a trigger graph for each app.
2. Use it to write GUI scenarios.
3. Run those scenarios on an emulator and record which methods actually ran. That gives the "known reachable" set.
4. Remove the methods Monkey already hit. What's left are the targets.
5. Run GAPS, APEX and TraceDroid on those targets.

Steps 1–3 are the draft's open `TODO [GT-REGISTRY]`. So your job is probably to make graphs for the 13 apps, but confirm that with them.

## What checks out
- All 13 apps have an APK, source, class files, and APE, Monkey and combined coverage reports.
- None of the apps contains a Kotlin (`.kt`) file.
- All 26 runs used the settings the draft states: API 27, 3600 s, seed 20261016, 500 ms throttle.

## Problems to raise with them
1. **The example graph is for a different Currency version.** `share/README.md` says v1.33 (commit `72e7dcd`), but the dataset's Currency is v1.58 (commit `fb95913`). The graph only shows the format; it can't serve as ground truth for this APK.
2. **41 apps or 13?** The draft says 41 apps throughout, and its Table I lists OpenCalc, Wikipedia and TranslateYou, which aren't among the 13.
3. **Which tool is the baseline?** The draft takes Monkey's misses as the targets, but `tool_run_set_38.csv` lists **APE** as the baseline for all 10 apps.
4. **The `Documents` fixture folder is missing.** `MANIFEST.csv` says Markor and AmazeFileManager need `fixtures/Documents`, but `_fixtures/` only has `Download`, `Music` and `Pictures`.
5. **Aegis and MMEX setup.** The draft says their setup is done, but in these runs coverage is about 4% for MMEX and 15–21% for Aegis, which suggests the setup wasn't in place. The README says they need manual setup, while `MANIFEST.csv` says MMEX needs none. Also, Aegis, AnkiDroid and MMEX aren't in the tool run set at all.

Written for: the person who sent you the files, to paste into WhatsApp or Discord.

> Checked the folder, everything's there. A few questions:
> 1. The Currency graph in share.zip is v1.33, but the dataset APK is v1.58. Is it just a format example, or should I regenerate it for v1.58?
> 2. Is the study now 13 Java-only apps, or still 41 like the draft says?
> 3. The draft uses Monkey's misses as targets, but tool_run_set_38.csv lists APE as the baseline. Which is right?
> 4. MANIFEST mentions fixtures/Documents (Markor, Amaze), but _fixtures has no Documents folder.
> 5. MMEX and Aegis coverage is very low (about 4% and 15–21%). Was the vault/database setup done for these runs?
> 6. What exactly should I do first? Run the graph prompt on all 13 apps?

I haven't read the five tool papers in depth yet. The extracted files are in `/private/tmp/claude-501/-Users-darshan-Desktop-yang/d045584d-1ca6-4e30-988a-f2f0a8d6b500/scratchpad/apps_x/final_java_only` and `/private/tmp/claude-501/-Users-darshan-Desktop-yang/d045584d-1ca6-4e30-988a-f2f0a8d6b500/scratchpad/share_x/share`. If you want, I can summarise the APEX, GAPS and TraceDroid papers next, or try GRAPH_PROMPT.md on Diary (the smallest app, 11 Java files) to see how the process works.


---

### User

For now we only work with JAVA related apps, they should be 14 on the list.


---

### Claude

The zip contains only 13 apps. I searched the whole archive and there's no 14th app anywhere in it. The folder's own README probably explains the gap:

> near miss, NOT included: Vinyl-Music-Player (4 .kt files among 268 .java)

The selection rule kept only apps with zero Kotlin files. Vinyl-Music-Player is almost all Java but has 4 Kotlin files, so it was dropped. That's most likely your 14th app.

The sender's own message also says "only 13 java only app", so you and they may be counting differently. Ask them:

- Should Vinyl-Music-Player be included? It's mostly Java with 4 Kotlin files.
- If so, can they send its folder? It should have the APK, source and classes, plus the APE and Monkey coverage runs, like the other 13.
- If not, which app is the 14th?

I've saved the Java-only scope (14 expected, 13 delivered) to memory so I'll remember it next session.


---

### User

Okay just wirh 13, so what do we do with these?


---

### Claude

Treat the 13 apps as the study's benchmark. The draft lays out the steps, and the files they sent cover the first ones.

## The pipeline

1. **Build a trigger graph for each app** using [GRAPH_PROMPT.md](GRAPH_PROMPT.md). For every method, the graph records which screen and which user action make it run, or marks it as dead code. This step needs only the app's source, no device. The Currency graph in `share.zip` is the example of what this produces.
2. **Confirm on an emulator.** Turn the graph's paths into scripted user actions and run them on an API 27 emulator with the instrumented APK. Then collect coverage (JaCoCo). The methods that actually ran become the "proven GUI-reachable" set.
3. **Pick the targets:** the proven-reachable methods that Monkey did *not* hit. Split them into "APE hit it" and "APE missed it" (Table III in the draft).
4. **Run GAPS, APEX and TraceDroid** on those targets and fill in Tables II–IV.

Steps 1–2 are almost certainly what they want from you, since they sent the graph example and the prompts. They match the draft's open `TODO [GT-REGISTRY]`.

## How big the job is

I counted methods from the coverage reports in the zip, leaving out the coverage helper classes:

| App | Methods | Missed by Monkey | …APE hit | …missed by both |
|---|---:|---:|---:|---:|
| Currency | 145 | 77 | 35 | 42 |
| Diary | 287 | 122 | 23 | 99 |
| hash-checker | 525 | 170 | 49 | 121 |
| openlauncher | 901 | 550 | 169 | 381 |
| Omni-Notes | 1,426 | 991 | 413 | 578 |
| Vanilla-Music | 1,468 | 566 | 199 | 367 |
| AnyMemo | 2,192 | 1,522 | 601 | 921 |
| Markor | 2,855 | 1,760 | 516 | 1,244 |
| Aegis | 2,957 | 2,250 | 44 | 2,206 |
| AmazeFileManager | 2,982 | 2,221 | 372 | 1,849 |
| AnkiDroid | 4,178 | 3,953 | 1,787 | 2,166 |
| MMEX | 4,269 | 4,007 | 10 | 3,997 |
| LibreTorrent | 4,728 | 3,168 | 520 | 2,648 |
| **Total** | **28,913** | **21,357** | **4,738** | **16,619** |

The "missed by Monkey" column only marks candidate targets. Many of those methods won't be reachable through the GUI, and steps 1–2 are what sort them out. Aegis and MMEX barely got past their first screen in these runs, so both need their setup (a test vault for Aegis, a database with an account for MMEX) before step 2 is meaningful for them.

## Recommended order
- **Start with Currency** (145 methods). It's the smallest, and the v1.33 example graph is a reference to compare against, even though the dataset ships v1.58.
- **Then Diary, hash-checker and openlauncher** (small).
- **Leave LibreTorrent, MMEX and AnkiDroid for last** (about 4,000+ methods each).

The prompt also expects a viewer template, which isn't in the folder. It can be recovered from the example page `currency_trigger_graph.html`, which stores its data in a `<script id="data">` block that can be swapped for `/*DATA*/`.

I can start step 1 on Currency v1.58 now. Step 2 needs an API 27 emulator: do you have one set up on this machine?

I've updated memory to say the study uses these 13 apps.


---

### User

what needs to be done, give me what we do then we will start, I will ask yang first if its right then we start


---

### Claude

Written for: Yang, to confirm the plan before you start.

I wrote the plan as a page: https://claude.ai/artifact/BujgpkPwLUT8zXeskVNEwn

It's private for now. Yang can't open it until you share it from the page's Share menu. It has the steps, the order to work through the 13 apps (with method counts and the setup each one needs), and the open questions. If you'd rather just send text, here's a short version to paste into WhatsApp:

> Hi Yang, before we start, can you check that this is the right plan for the 13 Java apps?
>
> **Steps**
> 0. Setup: rebuild the viewer template from the Currency HTML, get the Android 8.1 framework source, and set up an API 27 emulator that matches the baseline runs.
> 1. Build a trigger graph for each app with GRAPH_PROMPT.md (source only, no device).
> 2. Verify on the emulator: turn the graph paths into GUI scenarios, run them on the instrumented APK, and keep only methods with positive JaCoCo coverage. That's the proven-reachable set R_a.
> 3. Targets: T_a = R_a minus what the baseline hit, split by whether APE hit them.
> 4. Run GAPS, APEX and TraceDroid on T_a and fill Tables II–IV.
>
> Order: small apps first (Currency, Diary, hash-checker, openlauncher), then medium ones, then the large or setup-heavy ones (Aegis, AnkiDroid, MMEX, LibreTorrent).
>
> **Questions**
> 1. Is my part steps 1–3? Who runs the tools in step 4?
> 2. GRAPH_PROMPT for step 1 plus GENERIC_PROMPT for step 2, or GENERIC_PROMPT for everything?
> 3. Baseline: the draft says Monkey, but tool_run_set_38.csv says APE. Which is it?
> 4. The Currency example graph is v1.33, but the APK is v1.58. Should I build a new graph?
> 5. fixtures/Documents is missing (Markor and Amaze need it).
> 6. Aegis and MMEX coverage is very low (about 15–21% and 4%). Is there a setup recipe or a newer run?
> 7. Which emulator image did you use, and how do I trigger the coverage dump and reset?
> 8. Should the draft change from 41 apps to these 13?

Once Yang confirms, I'd start with step 1 on Currency.


---

### User

is the task for all of thrr 13 apps to make it like what we have in share for currency app?


---

### Claude

I think so, but nobody has said it outright. The message only says "here's an example of the graph" and "the 2 MD files are the prompts to generate it". It never says "do this for all 13 apps". It's the most likely reading, for three reasons:

- They sent the finished Currency example together with the two prompts that produce it. You don't send the recipe unless someone is meant to use it again.
- The prompts are written for any app, with blanks like `{APP_SRC_DIR}` and `{PACKAGE}`. GENERIC_PROMPT.md even says it "has not yet been run on a second app".
- The draft's missing ground-truth step (`TODO [GT-REGISTRY]`) is exactly what these graphs feed into.

## What "like share" means for each app
- **`<app>_trigger_graph.html`**: the interactive viewer (screen map, what each screen leads to, how each method gets triggered)
- **`methods.csv`**: one row per method, with its verdict and shortest path from app launch
- **`<app>_trigger_graph.json`**: the same data in machine-readable form
- **`README.md`**: counts, how far the graph can be trusted, and its limits

## Two catches
1. **The Currency example was also checked on an emulator.** Its README says it ran 77 scenarios on API 27 and compared the result with coverage. GRAPH_PROMPT.md alone gives you the graph without that check. The draft needs the coverage proof, so "like share" probably means graph plus emulator verification (GENERIC_PROMPT.md).
2. **The other apps are much bigger.** The Currency graph has 123 methods and 298 edges. LibreTorrent, MMEX and AnkiDroid each have about 4,000–4,700 methods, roughly 30 to 40 times as many. Expect far more work per app, and the viewer may get crowded.

I've added the deliverable question to the top of the plan page so Yang can answer it directly.

The plan page now has this as question 1: https://claude.ai/artifact/BujgpkPwLUT8zXeskVNEwn

If you're sending the WhatsApp text instead, add this line at the top of the questions:

> 0. Is the task to make a share/-style folder (HTML viewer, methods.csv, JSON, README) for each of the 13 apps, like the Currency one? And should each one also be checked on the emulator, like Currency was with 77 scenarios?


---

### User

write in short for the message to ask


---

### Claude

Written for: Yang, on WhatsApp.

> Hi Yang, quick check before I start:
> 1. Is the task to make a share/-style output (HTML viewer, methods.csv, JSON, README) for each of the 13 apps, like Currency?
> 2. Should each one also be checked on the emulator with JaCoCo, like Currency was (77 scenarios)?
> 3. Currency in the zip is v1.58 but the example graph is v1.33. Should I redo it for v1.58?
> 4. Which is the baseline, Monkey or APE? The draft says Monkey, tool_run_set_38.csv says APE.
> 5. fixtures/Documents is missing (Markor and Amaze need it).
> 6. Is there a setup recipe for Aegis and MMEX? Their coverage is very low.


---

### User

Is the task to make a share/-style output (HTML viewer, methods.csv, JSON, README) for each of the 13 apps, like Currency?

this is the task , now lets start what do we need to do now?


---

### Claude

I'll check what's installed on this machine first, then do the setup.


---

### User (sent while Claude was working)

does this need emualtor?


---

### User (sent while Claude was working)

But the page is not necessary
The important part is the data


---

### Claude

The method list matches JaCoCo exactly: 145 methods for Currency v1.58, against 123 in the v1.33 example. Now the files to read:

Now the viewer's path logic, so the CSV I generate matches theirs:

The BFS is simple and I'll copy it exactly. Let me look at some edges from the example to match their style and level of detail:


---

### User (sent while Claude was working)

what do we need to do now tell me in simple term? do we need to crea5te files like json and csv like share folder has for remaining 13 apps?


---

### Claude

Yes. For each of the 13 apps we make the same data files the share folder has for Currency:

- **`<app>_trigger_graph.json`**: the main data. It lists every screen, every method, and every link between them, such as "tapping this button calls this method".
- **`methods.csv`**: one row per method, giving whether it can be reached and the shortest list of taps from app launch to it.
- **`README.md`**: a short note with the counts and the limits.

That's 13 apps, not 13 plus Currency. Currency is one of the 13, and it needs to be redone because the example graph is for an older version of the app. The HTML page is optional, as you said.

**How each app gets done, in simple terms:**
1. Read all of the app's code.
2. List its screens and what you can tap on each one.
3. Record which method each tap or system event runs, and what that method calls next.
4. A script checks that every method is covered and works out the shortest path to each one.
5. Save the JSON, CSV and README.

No emulator is needed for this.

**Done so far:** the work folder is ready at `/Users/darshan/Desktop/yang/work/`, and I've built the tool that lists each app's methods. I've also studied how the example files are built, so ours will have the same format.

**Next:** build the Currency files first (145 methods, the smallest app), so you can compare them with the share example before we do the other 12. Should I start?


---

### User

how do we create those? is there scripts he provided or we need to do it?


---

### Claude

He didn't send any scripts. He sent three things:

1. **Two prompts** ([GRAPH_PROMPT.md](GRAPH_PROMPT.md) and [GENERIC_PROMPT.md](GENERIC_PROMPT.md)). These are instructions you give an AI coding agent like me. They aren't programs you can run.
2. **The finished Currency example** (`share.zip`), to show what the result should look like.
3. **The HTML viewer**, which is built into that example.

So the files are made like this:

| Part | Who does it |
|---|---|
| Reading the code and working out "this tap runs this method, which calls that one" | **The AI agent (me)**, following the prompt. No script can do this, because it takes understanding of the code and of how Android behaves. This is most of the work. |
| Listing all methods in an app | A small script. **I already wrote it** (`work/tools/list_methods.py`). |
| Checking the graph, finding each method's shortest path, writing `methods.csv` and the README | A script. The prompt says the agent should write it, so **I'll write it once** and reuse it for all 13 apps. |

That's almost certainly how he made the Currency example too: he gave the prompt to an AI agent (the draft mentions Claude Code and Codex). The prompt itself says it was "distilled from one worked example."

In practice: I read each app's code and write the graph data, then the script checks it and produces the CSV. Small apps like Currency are manageable in one session. The big ones (around 4,000 methods each) will need to be split into parts.

Want me to start with Currency?


---

### User

does this take time to generate, if he was able to do 1 then why give others to me to perform?


---

### Claude

Yes, it takes time, and the time grows with app size.

**Why it's slow**
- The agent has to read every file and reason about each method: what calls it, what the user taps to get there, and under what conditions.
- Currency is tiny: 145 methods, about 5,000 lines. The big apps (LibreTorrent, MMEX, AnkiDroid) have 4,000+ methods each, roughly 30 times as much.
- The output has to be checked. AI agents get some edges wrong. Even the Currency example, after an emulator check, had one wrong prediction that had to be fixed. Someone needs to review each graph, and verifying on an emulator takes even longer.

Rough guess: the small apps take a session each, and the big ones take many sessions split into parts.

**Why he handed it to you**
I can't know his reasons, but the usual ones apply:
- **He set up the method; you scale it.** Doing one small app proves the idea and fixes the format. Doing 13 is the labor part, which is normal to hand to a student or collaborator.
- **The method itself still needs testing.** GENERIC_PROMPT.md says it "has not yet been run on a second app." Running it on the other 12 shows whether it works on bigger, messier apps, and that's useful for the paper.
- **He has other work.** The draft is mostly TODOs, and three tools (GAPS, APEX, TraceDroid) still need to be run.

Your job is partly to run the prompt and partly to catch where it breaks or gives wrong results. His message ends with "if you find any error/bug or question, reach me," which fits that reading.

If you want to know how long he took on Currency, or whether he expects the emulator check on every app, ask him. That tells you how much time to plan for.


---

### User

what all do we need to perform all 13 apps now? do we need compute heavy? do we need emulators? what all do we need? how do we validate


---

### Claude

You don't need heavy compute, and you don't need an emulator to make the files. The emulator only comes in for the strongest kind of checking. Here's the full picture.

## 1. Making the files (JSON, CSV, README)

| Need | Status |
|---|---|
| Source code, class files, APKs for all 13 apps | ✅ Have it (the zip) |
| The prompts and the example output | ✅ Have it |
| Method-list tool | ✅ Built |
| Script that checks the graph and writes the CSV and README | ⏳ I write it once and reuse it for all 13 |
| **AI agent time** | This is the real cost. It's not CPU or GPU but agent usage: the agent reads the code and writes the graph. Small apps fit in a session; the big ones will use a lot of your Claude usage and need several sessions. |
| Android 8.1 framework source (optional) | A few files downloaded when needed, to back up claims about how Android behaves. Small. |

Your laptop (M1, 8 GB RAM) is fine for this. No GPU needed.

## 2. Validating (from cheapest to strongest)

1. **Script checks** (free, automatic): every method is accounted for, every screen is reachable, and nothing points to a method that doesn't exist. This only shows the graph is complete, not that it's correct.
2. **Compare with the coverage you already have** (free, no emulator): the zip has APE and Monkey coverage reports showing which methods really ran. If the graph calls a method dead but APE ran it, the graph is wrong. This catches mistakes at no cost, and I'd do it for every app.
3. **Read the paths** (you or me): pick about 15 methods per app and check that the "tap this, then this" path makes sense, as the prompt asks.
4. **Emulator check** (strongest, like the 77 scenarios behind the Currency example): run each path on a real emulator and confirm the predicted methods actually run.

## 3. What option 4 needs (none of it is installed now)
- Java (JDK), about 300 MB
- Android SDK, adb, emulator, and an **Android 8.1 (API 27) image**, about 3–5 GB
- `jacococli.jar`, to read the coverage dumps

Your Mac has 20 GB free, so it fits but is getting tight. 8 GB RAM is enough for one emulator. One open question: the API 27 image has to run on an M1 chip, and I'd need to check that.

**Alternative:** the APE and Monkey runs were done on another computer (the run logs show `/Users/poyu/...` and `emulator-5560`). Someone on the team already has a working setup. Ask Yang whether you can use it rather than building one on your laptop.

## Recommendation
Start with steps 1–3 for all 13 apps, which need no installs. Ask Yang whether step 4 is required for every app. If it is, set it up after Currency is done.


---

### User

I still dont get what the goal is for this task


---

### Claude

## The paper in one sentence
Some tools (GAPS, APEX, TraceDroid) claim they can steer an app until a specific piece of code runs. The paper tests how well they actually do that, and why they fail when they fail.

## The problem
To test a tool fairly, you have to know the answer yourself. If you tell APEX "make method X run" and it fails, there are two possibilities:
- the tool is bad, or
- method X can't be reached at all, for example because it's dead code or needs a server that doesn't exist.

You can't tell which unless you already know how X can be reached.

## What your task does
For each app, the graph is a map that says, for every method, how a normal user can make it run. A real row from the Currency example's `methods.csv`:

> **AboutPreference.onBindDialogView**: tap the Currency icon → tap the Settings menu item → tap the About row

That is the answer key for that method. Or the map says it's **unreachable** (dead code), so nobody should be blamed for missing it.

## How the paper then uses your map
1. **Your map** shows which methods are reachable and how.
2. **Remove the easy ones**, the methods random tapping (Monkey) already hit. The rest are the hard targets.
3. **Give the hard targets to GAPS, APEX and TraceDroid** and see which ones each tool reaches.
4. **When a tool fails**, compare what it did with the path on your map: "it never opened Settings", "it didn't long-press the row", and so on. That explains why it failed, which is research question 2 in the draft.

**In short:** you're building the answer key the paper grades the tools against. The paper's results tables are empty right now because this answer key doesn't exist yet for the 13 apps.


---

### User

is there any table for these for what reached? comparision table


---

### Claude

There are comparison tables, but only for the two random-style testers, **APE vs Monkey**. There are **no results yet for GAPS, APEX or TraceDroid**; those tables in the draft are empty.

## What exists: APE vs Monkey (1-hour runs, API 27)

This combines the zip's CSVs (line coverage) with the method counts I took from the coverage reports:

| App | Methods | Monkey reached | APE reached | Either | Line cov. Monkey | Line cov. APE |
|---|---:|---:|---:|---:|---:|---:|
| Currency | 145 | 68 | 103 | 103 | 39.2% | 57.5% |
| Diary | 287 | 165 | 187 | 188 | 46.4% | 53.9% |
| hash-checker | 525 | 355 | 404 | 404 | 54.8% | 64.1% |
| openlauncher | 901 | 351 | 485 | 520 | 35.1% | 51.8% |
| Omni-Notes | 1,426 | 435 | 847 | 848 | 27.1% | 54.0% |
| Vanilla-Music | 1,468 | 902 | 1,057 | 1,101 | 54.3% | 64.9% |
| AnyMemo | 2,192 | 670 | 1,227 | 1,271 | 26.8% | 54.1% |
| Markor | 2,855 | 1,095 | 1,565 | 1,611 | 34.1% | 50.5% |
| Aegis | 2,957 | 707 | 542 | 751 | 20.7% | 15.0% |
| AmazeFileManager | 2,982 | 761 | 1,124 | 1,133 | 21.1% | 32.5% |
| AnkiDroid | 4,178 | 225 | 2,004 | 2,012 | 3.3% | 39.9% |
| MMEX | 4,269 | 262 | 262 | 272 | 4.2% | 4.2% |
| LibreTorrent | 4,728 | 1,560 | 2,063 | 2,080 | 29.8% | 41.4% |
| **Total** | **28,913** | **7,556** | **11,870** | **12,294** | | |

Takeaways:
- APE beats Monkey on almost every app. The exception is Aegis, where both struggle.
- Even together they reach only 12,294 of 28,913 methods (43%). The other 16,600 are either hard to reach or unreachable. Your graphs are what tells those two cases apart.
- MMEX (about 4%) and Aegis are stuck near the start, probably because their setup wasn't done.

The source files are in `work/final_java_only/`: `comparison_ape_vs_monkey_api27.csv`, `combined_ape_monkey_api27.csv` and `summary_ape_api27.csv`.

## What's missing: the main comparison
This is the draft's Table II, still empty:

| Tool | Hits / targets | Rate |
|---|---|---|
| APE | – | – |
| GAPS | – | – |
| APEX (paper / plus) | – | – |
| TraceDroid (paper / plus) | – | – |

It can't be filled until the targets exist, and the targets come from your graphs: methods the graph proves reachable, minus the ones Monkey already hit.

The zip's README mentions a "38-app tool run set", so some GAPS, APEX or TraceDroid runs may exist on Yang's side. Worth asking whether there are any early results you can look at.


---

### User

if this is all calculated why are we working on this?


---

### Claude

The table answers a different question. It shows **what random testing happened to reach**. It doesn't say what **could** be reached, or **how**.

## What the table tells you
"In one hour, Monkey ran these methods and didn't run those."

## What it can't tell you
Take Currency: 145 methods, 103 reached by APE or Monkey, **42 reached by neither**. For each of those 42, the table can't say:
- Is it reachable at all, or is it dead code?
- If it's reachable, what does a user have to do? Which screen, which taps, what data has to exist first?

Multiply that by all 13 apps and you get **16,600 methods that nothing reached**, with no explanation for any of them.

## Why the paper needs that answer
- **Choosing targets.** Asking GAPS or APEX to reach a dead method isn't fair, because nobody can reach it. The paper needs a list of methods that are **proven reachable**, and the coverage table doesn't give that.
- **Explaining failures.** When APEX misses a method, the paper has to say why. You can only say "it never long-pressed the row" if you know the correct path is "long-press the row, then tap Chart." That path comes from the graph.

## An analogy
The coverage table is a record of which rooms visitors walked into during one hour. The graph is the **floor plan**: every room, which door leads where, and which rooms are locked for good. To judge a guide who claims "I can take you to any room," you need the floor plan, not the visitor log.

So the work isn't redoing what's calculated. It fills in the half the coverage table can't answer.


---

### User

start working on by one and explain each steps we work on I am still confused, the first work we need to do is making html json and csv files for each of these provided 13 JAVA apps right?


---

### Claude

Yes. For each of the 13 apps the first job is to make the JSON, CSV and HTML files. I'll start with **Currency** and explain each step as I go.

**The steps for one app:**
1. **Inventory**: list what's in the app (screens, buttons, menus, settings, methods).
2. **Read the code**: every Java file.
3. **Define the pages**: the distinct screens and modes a user can be in.
4. **Write the links**: "on this page, this tap runs this method, which calls that one…"
5. **Check**: a script verifies the graph, and we compare it with the APE/Monkey coverage.
6. **Output**: JSON, CSV, HTML, README.

---

## Step 1: Inventory (Currency)

First the **manifest**. It's the app's "table of contents" and lists every screen (Activity) and every way the app can be started from outside. Then the **menus**, **layouts** (screen designs) and **settings** XML, which say which buttons exist.

Still 0 errors. Here's a second sample: the fixed methods plus ones I haven't read yet:

Before I report, let me double-check the environment numbers I put in the README against the actual CSV:

Currency is done. Let me save the progress and how you like to work, so the next session picks up correctly:

**Currency is done (app 1 of 13).** Its files are in [work/graphs/Currency/out/](work/graphs/Currency/out/), in the same format as the share folder:

| File | What it is |
|---|---|
| `currency_trigger_graph.json` | The main data: 22 pages, 145 methods, 391 links |
| `methods.csv` | One row per method, with its shortest list of taps |
| `currency_trigger_graph.html` | The optional viewer |
| `README.md` | Counts, how far to trust it, and limits |

One real row from the CSV:
> **Main.onCopyClick**: open the app → long-press any row → tap Copy

## What we found
- **140 methods can be reached, 2 are dead code, 3 only Android itself could call.**
- **The coverage contradicted none of the verdicts.** Nothing I marked as dead ever ran in the APE or Monkey runs.
- **35 methods are reachable but neither tool ever ran them.** Of those:
  - 13 need the exchange-rate download to work, and it never did on the test emulator.
  - 3 only run when the network is off.
  - 19 the tools simply missed. Most of these are widget code, which you can only reach from the home screen, where APE and Monkey can't go.

  Those 19 are good targets for the paper.
- **Two likely crashes, found by reading the code:** picking "New chart" while the chart is still loading, and tapping the widget's refresh button while offline.

## How it was checked
- The script checks found no errors.
- I read 36 of the shortest paths by hand. That caught 4 mistakes, and all are fixed.
- The comparison with real coverage showed one of my Android-behaviour assumptions was wrong, and I corrected it.

**Not done yet: checking it on an emulator,** which the share example had (77 scenarios). 74 of the links rely on how I remember Android behaving, and those are the most likely to be wrong.

## What you can reuse
The scripts in [work/tools/](work/tools/) work for all 13 apps. For each new app, only the reading and writing of the links has to be redone.

## Next
- **Send Yang the Currency files** and ask whether this matches what they expect, before we do the other 12.
- Then do **Diary** (287 methods), the next smallest app.


---

### User

do we have script for this whole other remaining or we do it manually how did you do this for currency?


---

### Claude

It's half and half. Some parts are scripts, which are done and reusable for all 13 apps. The main part is not a script: I (the AI) read the code and wrote the links. Here's exactly what happened for Currency:

| Step | How it was done | Reusable for the other 12? |
|---|---|---|
| 1. List all methods | **Script** (`list_methods.py`) reads the compiled class files | ✅ Yes, run as is |
| 2. Get APE/Monkey coverage per method | **Script** (`coverage_methods.py`) | ✅ Yes, run as is |
| 3. Read the code (manifest, menus, layouts, all 17 Java files) | **Me, by hand** | ❌ No, every app is different |
| 4. Decide the pages (screens and modes) | **Me, by hand** | ❌ No |
| 5. Write every link ("this tap → this method → calls that one") into `graph_def.py` | **Me, by hand**: 391 links for Currency | ❌ No, this is most of the work |
| 6. Check it, find shortest paths, compare with coverage, write the JSON, CSV and HTML | **Script** (`build_graph.py`) | ✅ Yes, run as is |
| 7. Read sample paths and fix shortcuts | **Me, by hand** | ❌ No |
| 8. Write the README | **Me**, from the script's numbers | Partly |

So for each remaining app, steps 1, 2 and 6 are automatic, and steps 3–5 and 7 have to be done by reading that app's code. There's no way around this: understanding "long-press a row puts the screen into selection mode, which changes the menu" takes reading the code, and no simple script can work that out.

## Making the other 12 faster
Many of the links are mechanical and could be **extracted by a script**:
- **Direct calls** (method A calls method B). These can be read straight from the compiled code. For Currency they were 113 of the 391 links.
- **Screens and entry points** from the manifest, **menu items** from the menu XML, and **listener registrations** (`setOnClickListener`, and so on).

That would leave the manual work as the parts that need understanding: pages and modes, which tap triggers what, conditions, and Android's own callbacks. For the big apps (LibreTorrent, MMEX and AnkiDroid have around 4,000+ methods each) this matters a lot. Writing every direct call by hand there isn't realistic.

**My recommendation:** before Diary, let me write that call-extractor script. It takes about one session, and it pays off on every app after that, especially the big ones. Then:
- **Small apps** (Diary, hash-checker, openlauncher): one app per session, with the script doing the mechanical part.
- **Big apps**: split by feature (for example "settings", "editor", "file list"), possibly with several agents working on different parts in parallel. If you want that, say "use a workflow" and I'll plan it. It uses a lot more of your Claude usage, so it's your call.

Should I write the call extractor now, or go straight to Diary the same way I did Currency?


---

### User

compare the result of this with what he shared in share folder, we used the same app right currency app, what is his result and what is ours?


---

### Claude

It's the same app but **not the same version**: his graph is for Currency **v1.33**, ours is for **v1.58** (the APK in the dataset). So some differences are because the app itself changed. Let me compare them properly:

Let me also compare by **user taps** rather than internal steps, since the two graphs model internal detail differently:

Yes, it's the same app (Currency), but **not the same version**. His graph is **v1.33**; ours is **v1.58**, the version actually in the 13-app dataset. Between those versions the developer added a home-screen widget, moved Settings/Help behind a ☰ button, and rewrote the download code. So some differences come from the app itself, not from either analysis.

## Side by side

| | His (v1.33) | Ours (v1.58) |
|---|---:|---:|
| Methods | 123 | 145 |
| Pages | 16 | 22 |
| Links (edges) | 298 | 391 |
| Reachable | 119 | 140 |
| Dead code | 2 | 2 (**the same two**) |
| Called only by Android | 2 | 3 (**the same two**, plus the widget service's `onBind`) |
| Evidence label on each link | No | Yes |
| Checked on an emulator | **Yes**: 77 scenarios, 76 matched | **No, not yet** |

## Where they agree
- **106 methods exist in both versions, and we gave the same verdict for every one of them** (reachable, dead or Android-only).
- We found the same two dead methods for the same reasons (`ChartParser.startParser(Context,int)` and `Singleton.getList`).

That agreement isn't a fully blind test: I had read his README, which names those methods, before building ours. I did confirm them myself by searching every caller.

## Differences because the app changed
- **17 of his methods no longer exist.** v1.58 replaced the old background-download classes (`ParseTask`).
- **39 methods are new in v1.58**: the widget (19), the new download code, and the ☰ popup.
- **6 new pages**: widget home, widget setup, the ☰ popup, two settings dialogs, and a background state.
- **Settings and Help are one tap deeper** (☰ → Settings) than in his version.

## Differences in how we each modelled it
- **"Steps from launch" isn't comparable between the two.** It counts internal method hops, not taps. His model jumps from "Settings tapped" straight to the Settings page; ours goes through the screen's start-up methods. So the About dialog is 9 steps in his and 15 in ours, but only **one extra tap** for the user (the ☰). Counted by user taps, 77 of the 102 comparable methods are identical.
- **His CSV lists alternatives as steps** ("Press Home ; or Back ; or rotate"). Ours shows only the first option.

## A bug in his CSV (worth telling him)
His **graph is correct, but 4 rows in his `methods.csv` drop the last tap.** When the path ends at a menu handler, the final tap disappears:

| Method | His CSV says | Actually needs |
|---|---|---|
| `HelpActivity.onOptionsItemSelected` | tap icon ; tap Help | …; **tap the Up arrow** |
| `SettingsActivity.onOptionsItemSelected` | tap icon ; tap Settings | …; **tap the Up arrow** |
| `ChartActivity.onOptionsItemSelected` | tap icon ; long-press ; tap Chart | …; **tap a Chart menu item** |
| `Main.onOptionsItemSelected` | tap icon | …; **tap a menu item** |

His own graph has the right link (for example edge E275, "Tap the Up arrow"), so the problem is in whatever script turned the graph into the CSV. Our CSV includes those taps.

## Bottom line
On the methods both versions share, our result matches his. The main gap is that **his was checked on an emulator and ours hasn't been yet**. Here's a short message you could send him about the bug:

> In share/methods.csv, 4 rows drop the last tap when the shortest path ends at an onOptionsItemSelected (HelpActivity, SettingsActivity, ChartActivity, Main). E.g. HelpActivity.onOptionsItemSelected shows "tap icon ; tap Help" but needs "tap the Up arrow" too. The graph edge (E275) is right, so it looks like a CSV-generation bug. Also: the dataset's Currency is v1.58, so I rebuilt the graph for v1.58. It agrees with yours on all 106 methods both versions share.


---

### User

where do you have this chat history, I want to share this with kiro session


---

### Claude

Your messages sent while I was working are stored as a separate record type, so the export needs to include those too. Writing the export script:
