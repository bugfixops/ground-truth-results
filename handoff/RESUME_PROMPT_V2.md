You are continuing an unattended job for the student who helps Yang with the ICST 2027 paper on targeted Android testing tools. Nobody can answer questions while you run: choose the conservative default, record the decision in work/handoff/HANDOFF_V2.md, and keep going.

GOAL: convert every app in work/handoff/PROGRESS_V2.md that is still "- [ ]" to the schema 2 ground truth, in the order listed there, until none is left. The full procedure, the rules and the done criteria are in work/handoff/AGENT_BRIEF_V2.md: read it completely before you start, and follow it. Examples that are finished and checked: work/graphs/Omni-Notes/ and work/graphs/hash-checker/.

MODEL: the model of this run is the one named in work/handoff/MODEL_V2 (claude-haiku-5-5 at the moment). Helper agents: when you start one with the Agent tool, do NOT set its model parameter; a helper then runs on this run's model. Never use the aliases "haiku" or "sonnet" anywhere: in this Claude Code version "haiku" means Haiku 4.5, not 5.5.

DO FIRST:
1. Read the memory index (auto-loaded), then work/handoff/AGENT_BRIEF_V2.md, work/handoff/SCHEMA_V2.md, work/handoff/CONVERSION_RECIPE.md (the sections "hash-checker", "Omni-Notes" and "Added after Omni-Notes" hold the lessons that found real errors) and work/handoff/HANDOFF_V2.md.
2. Take the first "- [ ]" app in PROGRESS_V2.md. If work/graphs/<App>/ already holds a graph_def.py, AGENT_NOTES.md or verification.csv from an earlier session, continue from it; do not start again from zero.

LOCK: every bash command you run starts with `touch /Users/darshan/Desktop/yang/work/handoff/WORKING_LOCK;`. The resume watcher will not start a second session while that file was touched in the last 30 minutes.

WAITING: the run stays alive until the helper agents you start have finished, so wait for their reports before you tick anything. A helper that stops at a usage limit leaves its work in its app folder: write its state into AGENT_NOTES.md and continue from there.

WHEN AN APP IS DONE (all checks of step 9 of the brief pass, run by you on the final build): change its line in PROGRESS_V2.md from "- [ ]" to "- [x]", append a short paragraph to HANDOFF_V2.md (numbers recomputed from the final build only), then go to the next app. Never tick an app that fails a check.

WHEN NO "- [ ]" IS LEFT: touch work/handoff/STOP_RESUME_V2, write work/handoff/FINAL_SUMMARY_V2.md (per-app numbers from the READMEs, the path error rates, the open questions, what could not be verified without a device) and reply with a short summary.

If a usage limit stops you, the watcher starts you again later from these files, so keep PROGRESS_V2.md, HANDOFF_V2.md and AGENT_NOTES.md current after every big step.
Do not push to GitHub, do not commit, do not install packages, and do not use the network except raw.githubusercontent.com for Android 8.1.0_r1 framework files.
