#!/usr/bin/env python3
"""MMEX per-route setup for route_21 (DefinedDateRange$1.<init>) -- bootstrap (audit §3.2).

Bootstrap only: no seed rows are needed, because route_20's chain needs
nothing but a reachable home screen (drawer -> About -> Logcat button).

What this setup does, in run_app.sh order (after `pm clear`, before the
route script), using only host-side adb (no UI driving is needed here):

1. Pushes an EMPTY file to /sdcard/MoneyManagerEx/mmex.mmb. An empty
   file is not a fake database: on first open the app's own
   MmxOpenHelper.onCreate runs the app's own schema script
   (R.raw.tables_v1) plus initDatabase (base currency, date format)
   -- database/MmxOpenHelper.java:96-103, 227-236. A hand-filled
   plaintext sqlite3 .mmb is deliberately NOT used: the app opens
   every database through the SQLCipher SupportFactory
   (MmxOpenHelper.java:132-154), so a plaintext file with a SQLite
   header would be rejected as not-a-database, while a 0-byte file
   is treated as a new database and initialised by the app itself.
2. Writes the app's default SharedPreferences file
   (com.money.manager.ex_preferences.xml, the PreferenceManager
   default; provided by MmxModule.provideSharedPreferences,
   core/ioc/MmxModule.java:60-64) via `run-as` (the replay APKs are
   instrumented debug builds), setting:
     - prefshowtutorial = false (BehaviourSettings.getShowTutorial
       default true, settings/BehaviourSettings.java:86-88; tutorial
       is the first showPrerequisite gate, home/MainActivity.java:
       1478-1489);
     - databasepath = /sdcard/MoneyManagerEx/mmex.mmb
       (DatabaseSettings.getDatabasePath/setDatabasePath; the path
       key string is res/values/prefids.xml:34 "databasepath").
   With those two set, MainActivity.isDatabaseAvailable()
   (home/MainActivity.java:1338-1348: path non-empty, not an
   unpassworded .emb, file exists) passes and showPrerequisite()
   returns false, so MainActivity proceeds to initHomeFragment.
3. Launches MainActivity and waits until it is the resumed activity,
   so the schema creation in step 1 has actually happened before the
   route script runs.

Failure mode: any step failing exits 1, which run_app.sh records as
failed_at_step_0 (setup_failed). Nothing is faked: if the schema is
not created, the route script's home taps fail honestly.

This file is written for device/routes/MMEX/setup_route_21.py (the
run_app.sh per-route setup contract: invoked with --package --log
--outdir --gen-dir). It is NOT executed by drycheck: drycheck only
py_compiles setup scripts (for gen: fixtures) and dry-loads route
scripts, so this bootstrap is validated on the live run, not by
dry-run. The route script itself is dry-safe.

Route note: bootstrap-sufficient.

Usage (invoked by run_app.sh):
    setup_route_21.py --package <pkg> --log <log> --outdir <dir> \
        --gen-dir <dir>
"""

import argparse
import os
import subprocess
import sys
import time

PKG = "com.money.manager.ex"
MAIN = "com.money.manager.ex/.home.MainActivity"
DB_DEVICE_PATH = "/sdcard/MoneyManagerEx/mmex.mmb"
PREFS_NAME = "com.money.manager.ex_preferences.xml"

PREFS_XML = """<?xml version='1.0' encoding='utf-8' standalone='yes' ?>
<map>
    <string name="databasepath">/sdcard/MoneyManagerEx/mmex.mmb</string>
    <boolean name="prefshowtutorial" value="false" />
</map>
"""


def _fail(msg):
    print("setup FAILED: " + msg, file=sys.stderr)
    sys.exit(1)


def _adb(adb, args, timeout=60):
    try:
        proc = subprocess.run([adb] + args, capture_output=True,
                              text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        _fail("adb %s timed out" % " ".join(args))
    if proc.returncode != 0:
        _fail("adb %s failed (%s): %s" % (
            " ".join(args), proc.returncode, proc.stderr.strip()[:300]))
    return proc.stdout


def _shell(adb, command, timeout=60):
    return _adb(adb, ["shell"] + command, timeout=timeout)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="MMEX route_21 setup: bootstrap an app-created database")
    parser.add_argument("--package", default=PKG)
    parser.add_argument("--log", default=None)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--gen-dir", default=None)
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args(argv)
    adb = args.adb
    pkg = args.package or PKG
    gen_dir = args.gen_dir or os.environ.get("GEN_DIR", "") or os.getcwd()
    os.makedirs(gen_dir, exist_ok=True)

    def log(msg):
        line = msg + "\n"
        if args.log:
            with open(args.log, "a", encoding="utf-8") as f:
                f.write(line)
        sys.stdout.write(line)

    # 1. Empty database file on shared storage (app-created schema).
    mmb_local = os.path.join(gen_dir, "mmex.mmb")
    with open(mmb_local, "wb") as f:
        pass  # 0 bytes, deliberately: the app initialises it itself.
    _shell(adb, ["mkdir", "-p", "/sdcard/MoneyManagerEx"])
    _adb(adb, ["push", mmb_local, DB_DEVICE_PATH])
    log("pushed empty %s (0 bytes) to %s" % (mmb_local, DB_DEVICE_PATH))

    # 2. SharedPreferences via run-as (debug build): tutorial off,
    # database path set. The app is not running (pm clear just ran),
    # so no in-memory preference cache can overwrite this file.
    prefs_local = os.path.join(gen_dir, "mmex_prefs.xml")
    with open(prefs_local, "w", encoding="utf-8") as f:
        f.write(PREFS_XML)
    _adb(adb, ["push", prefs_local, "/sdcard/mmex_prefs.xml"])
    # Storage grant (audit §2.6, option (a)): run_app.sh grants ROUTES
    # permissions only AFTER setup, and the bootstrap DB lives on shared
    # /sdcard, so setup grants storage itself before the run-as copy
    # and the warm launch.
    _shell(adb, ["pm", "grant", pkg, "android.permission.READ_EXTERNAL_STORAGE"])
    _shell(adb, ["pm", "grant", pkg, "android.permission.WRITE_EXTERNAL_STORAGE"])
    _shell(adb, ["run-as", pkg, "mkdir", "-p",
                 "/data/data/%s/shared_prefs" % pkg])
    _shell(adb, ["run-as", pkg, "cp", "/sdcard/mmex_prefs.xml",
                 "/data/data/%s/shared_prefs/%s" % (pkg, PREFS_NAME)])
    back = _shell(adb, ["run-as", pkg, "cat",
                        "/data/data/%s/shared_prefs/%s" % (pkg, PREFS_NAME)])
    if "databasepath" not in back or "prefshowtutorial" not in back:
        _fail("preferences read-back does not contain the bootstrap keys")
    log("wrote shared prefs %s (tutorial off, databasepath set)" % PREFS_NAME)

    # 3. Warm launch: MainActivity onCreate opens the database, which
    # runs MmxOpenHelper.onCreate (tables_v1 + initDatabase).
    _shell(adb, ["am", "start", "-W", "-n", MAIN])
    deadline = time.time() + 60
    while time.time() < deadline:
        dump = _shell(adb, ["dumpsys", "activity", "activities"])
        if "mResumedActivity" in dump and "MainActivity" in dump:
            break
        time.sleep(2)
    else:
        _fail("MainActivity did not become the resumed activity in 60s")
    log("MainActivity resumed; app-created database schema is live")
    return 0


if __name__ == "__main__":
    sys.exit(main())
