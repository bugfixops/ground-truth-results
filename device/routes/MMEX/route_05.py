"""MMEX route_05: Passcode.savePasscode.

Method: Passcode.savePasscode
Edge ids (in route order):
    E71c76102 E2e074fc1 E5d5a9c2f Eff22f7d2 Ed2488d54 E025b8cae
    E02874fba Ec35ca2a7 E3a7e070b Eb967ab5b E124f2c64 E2a1c6fc4
    Ef2276126 E52f14c8f E532edcea Eb6c06d72 E9ac9395c E117d8069
    E8ff3567a E15135c45 Ec3713848 Edbef50b3 E0044db82 Ea8845013
    Eed2c3bb1 E53b01cac E28b9ac6c Edc77ed75 Ea63a9050
Printed route source:
    graphs/MMEX/scratch/route_print_final2/Passcode.savePasscode.txt
    (29 steps; edge list verified identical to the verification.csv
    path row for Passcode.savePasscode, result unclear -- the route
    verdict is unclear in verification.csv, but the script below
    still implements the printed steps as written).
Launch component: com.money.manager.ex/.home.MainActivity, the
    MAIN/LAUNCHER activity (AndroidManifest.xml:136-143, package
    com.money.manager.ex at AndroidManifest.xml:19).
Permissions: none. The print header has env=-, so no ENV permission
    gate applies.
Fixtures: none (no STATE file gate in the print header).
Setup: none (apps.csv MMEX setup cell is effectively none).
State preconditions (read before judging the real run): a valid
    database must be present and the first-run tutorial already
    dismissed (home/MainActivity.java:184, 1478-1490); the printed
    route assumes both. The active-passcode preference is enabled
    only while no passcode exists
    (settings/SecuritySettingsFragment.java:161), which the
    pm-clear state satisfies, and MainActivity's own passcode
    authentication on start (home/MainActivity.java:252-260) does
    not divert while no passcode is set. The passcode entered here
    is 12345, entered twice; the second entry must match the first
    for the REINSERT branch to call setPasscode
    (settings/SecuritySettingsFragment.java:112, 117-118).
Run (from the repo root, once merged to device/routes/MMEX/):
    python3 -I device/routes/MMEX/route_05.py --package
    com.money.manager.ex --log steps/route_05.log
    --outdir <outdir> [--dry-run] [--adb adb]
Draft location: finish/work/MMEX/device-draft/g1/route_05.py; the
    import below resolves once the file sits under device/routes/MMEX/
    as in the Currency template scripts.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))

from device.harness import Runner

EDGE_IDS = [
    "E71c76102", "E2e074fc1", "E5d5a9c2f", "Eff22f7d2", "Ed2488d54",
    "E025b8cae", "E02874fba", "Ec35ca2a7", "E3a7e070b", "Eb967ab5b",
    "E124f2c64", "E2a1c6fc4", "Ef2276126", "E52f14c8f", "E532edcea",
    "Eb6c06d72", "E9ac9395c", "E117d8069", "E8ff3567a", "E15135c45",
    "Ec3713848", "Edbef50b3", "E0044db82", "Ea8845013", "Eed2c3bb1",
    "E53b01cac", "E28b9ac6c", "Edc77ed75", "Ea63a9050",
]

PASSCODE_DIGITS = ["1", "2", "3", "4", "5"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--log", required=True)
    parser.add_argument("--outdir", default=".")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--adb", default="adb")
    args = parser.parse_args()
    r = Runner(package=args.package, route="route_05", edge_ids=EDGE_IDS,
               log_path=args.log, dry_run=args.dry_run, adb=args.adb,
               outdir=args.outdir)
    try:
        # E71c76102: Tap the MMEX icon in the launcher
        # (MAIN/LAUNCHER intent filter, AndroidManifest.xml:136-143).
        r.launch("com.money.manager.ex/.home.MainActivity",
                 edge="E71c76102")
        # E2e074fc1: The system instantiates MainActivity, then
        # calls onCreate.
        r.comment("system instantiates MainActivity, then onCreate",
                  edge="E2e074fc1")
        # E5d5a9c2f: onCreate calls initHomeFragment
        # (home/MainActivity.java:238).
        r.comment("MainActivity.onCreate calls initHomeFragment",
                  edge="E5d5a9c2f")
        # Eff22f7d2: initHomeFragment commits HomeFragment; the home
        # screen is shown.
        r.comment("initHomeFragment commits HomeFragment (home shown)",
                  edge="Eff22f7d2")
        # Ed2488d54: Open the drawer, then tap a top-level drawer
        # item with no sub-items. The Menu key toggles the drawer
        # (home/MainActivity.java:407-419, KEYCODE_MENU branch), and
        # the Settings group item text is @string/settings =
        # "Settings" (res/values/strings.xml:189; item built at
        # home/MainActivity.java:1107, case at 664-665).
        r.key("MENU", edge="Ed2488d54")
        r.tap(text="Settings", edge="Ed2488d54")
        # E025b8cae: The tap posts the drawer-item Runnable with a
        # 200 ms delay; the framework runs run().
        r.comment("drawer Runnable posted (200 ms delay), framework "
                  "runs run()", edge="E025b8cae")
        # E02874fba: run() calls onDrawerMenuAndOptionMenuSelected
        # with the tapped group item.
        r.comment("run() calls onDrawerMenuAndOptionMenuSelected "
                  "with the group item", edge="E02874fba")
        # Ec35ca2a7: case R.id.menu_settings starts SettingsActivity.
        r.comment("case menu_settings starts SettingsActivity",
                  edge="Ec35ca2a7")
        # E3a7e070b: The system instantiates SettingsActivity, then
        # onCreate (settings/SettingsActivity.java:40-46).
        r.comment("system instantiates SettingsActivity, then "
                  "onCreate", edge="E3a7e070b")
        # Eb967ab5b: onCreate shows the default SettingsFragment
        # (settings/SettingsActivity.java:67-69); the settings list
        # is shown.
        r.comment("SettingsActivity shows the settings list",
                  edge="Eb967ab5b")
        # E124f2c64: Tap the security preference. Its title is
        # @string/preferences_security = "Security"
        # (res/values/strings.xml:281; res/xml/preferences.xml:49-50),
        # and its click listener is set at
        # settings/SettingsFragment.java:126.
        r.tap(text="Security", edge="E124f2c64")
        # E2a1c6fc4: The listener starts SecuritySettingsActivity
        # (settings/SettingsFragment.java:129).
        r.comment("security preference starts SecuritySettingsActivity",
                  edge="E2a1c6fc4")
        # Ef2276126: The system instantiates SecuritySettingsActivity,
        # then onCreate (settings/SecuritySettingsActivity.java:25-29).
        r.comment("system instantiates SecuritySettingsActivity, then "
                  "onCreate", edge="Ef2276126")
        # E52f14c8f: onCreate sets SecuritySettingsFragment; the
        # security settings screen is shown.
        r.comment("SecuritySettingsActivity shows SecuritySettingsFragment",
                  edge="E52f14c8f")
        # E532edcea: Tap the active-passcode preference. Its title
        # is @string/preferences_active_passcode = "Activate Passcode"
        # (res/values/strings.xml:282;
        # res/xml/preferences_security.xml:22-23), and its click
        # listener is set at
        # settings/SecuritySettingsFragment.java:55.
        r.tap(text="Activate Passcode", edge="E532edcea")
        # Eb6c06d72: The listener calls startActivityPasscode
        # (settings/SecuritySettingsFragment.java:60).
        r.comment("preference click calls startActivityPasscode",
                  edge="Eb6c06d72")
        # E9ac9395c: startActivityPasscode starts PasscodeActivity
        # for result (settings/SecuritySettingsFragment.java:168-175).
        r.comment("startActivityPasscode starts PasscodeActivity",
                  edge="E9ac9395c")
        # E117d8069: The system instantiates PasscodeActivity, then
        # onCreate (PasscodeActivity.java:82).
        r.comment("system instantiates PasscodeActivity, then onCreate",
                  edge="E117d8069")
        # E8ff3567a: onCreate sets the passcode layout
        # (PasscodeActivity.java:92, R.layout.passcode_activity) and
        # wires the digit keys; the passcode screen is shown.
        r.comment("PasscodeActivity shows the passcode screen",
                  edge="E8ff3567a")
        # E15135c45: Tap the digit keys. The buttons carry literal
        # texts "0" to "9" (res/layout/passcode_activity.xml:161-264
        # for 1-9, 285 for 0); the shared listener fills the focused
        # field and advances focus, and the fifth digit triggers
        # setResult(RESULT_OK) and finish
        # (PasscodeActivity.java:101-131). Entered passcode: 12345.
        for digit in PASSCODE_DIGITS:
            r.tap(text=digit, edge="E15135c45")
        # Ec3713848: PasscodeActivity sets RESULT_OK with the entered
        # passcode and the framework delivers the result to the
        # fragment that called startActivityForResult.
        r.comment("first passcode entry returns RESULT_OK",
                  edge="Ec3713848")
        # Edbef50b3: The INSERT branch of onActivityResult stores
        # the entered passcode and starts a second PasscodeActivity
        # for re-entry (settings/SecuritySettingsFragment.java:103-107).
        r.comment("INSERT branch starts the re-entry PasscodeActivity",
                  edge="Edbef50b3")
        # E0044db82: startActivityPasscode with
        # REQUEST_REINSERT_PASSCODE starts the second PasscodeActivity
        # (settings/SecuritySettingsFragment.java:168-175).
        r.comment("second PasscodeActivity started for re-entry",
                  edge="E0044db82")
        # Ea8845013: The system instantiates PasscodeActivity again,
        # then onCreate.
        r.comment("system instantiates PasscodeActivity again, then "
                  "onCreate", edge="Ea8845013")
        # Eed2c3bb1: The passcode screen is shown a second time.
        r.comment("passcode screen shown a second time",
                  edge="Eed2c3bb1")
        # E53b01cac: Re-enter the same passcode, 12345, on the
        # second passcode screen (same digit buttons and listener
        # as the first entry).
        for digit in PASSCODE_DIGITS:
            r.tap(text=digit, edge="E53b01cac")
        # E28b9ac6c: The second entry returns RESULT_OK and the
        # framework delivers it to onActivityResult.
        r.comment("second passcode entry returns RESULT_OK",
                  edge="E28b9ac6c")
        # Edc77ed75: The REINSERT branch calls setPasscode once the
        # re-entered passcode matches the stored one
        # (settings/SecuritySettingsFragment.java:112, 117-118).
        r.comment("REINSERT branch calls Passcode.setPasscode",
                  edge="Edc77ed75")
        # Ea63a9050: setPasscode calls savePasscode
        # (Passcode.java:80). TARGET REACHED.
        r.comment("setPasscode calls savePasscode (target)",
                  edge="Ea63a9050")
    finally:
        r.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
