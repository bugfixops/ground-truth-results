"""Harness implementation: adb actions, uiautomator dump parsing, logging.

Design notes (see device/README.md for the full contract):
- Views are found by parsing `uiautomator dump` output: resource-id,
  text, or content-desc. The centre of the node's bounds is tapped.
  Fixed coordinates are allowed only when the caller passes x/y AND a
  `why` string saying why no id, text, or desc exists.
- Every action logs one line: UTC time, edge id, action, target, result.
- Dry-run mode never executes adb: it records the planned commands and
  validates edge ids. Node resolution is skipped in dry mode (there is
  no device to dump); tap/scroll/wait/assert calls record their
  selector as the planned target.
- All adb calls go through one helper so dry mode cannot leak a real
  call: _run() returns immediately in dry mode.
- System UI needs no special primitive: _raw_dump() has no package
  filter, so dump_ui/tap/wait_for/scroll_to/assert_text operate on
  whatever is foreground — the system file picker, permission
  dialogs, and the launcher are driven with the same primitives as
  app UI. A route that needs the picker or the launcher documents
  that in its header; the harness does not filter by package.
"""

import os
import re
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

BOUNDS_RE = re.compile(r"\[(\d+),(\d+)\]\[(\d+),(\d+)\]")

KEY_ALIASES = {
    "BACK": "KEYCODE_BACK",
    "HOME": "KEYCODE_HOME",
    "APP_SWITCH": "KEYCODE_APP_SWITCH",
    "ENTER": "KEYCODE_ENTER",
    "DEL": "KEYCODE_DEL",
    "DPAD_UP": "KEYCODE_DPAD_UP",
    "DPAD_DOWN": "KEYCODE_DPAD_DOWN",
    "DPAD_LEFT": "KEYCODE_DPAD_LEFT",
    "DPAD_RIGHT": "KEYCODE_DPAD_RIGHT",
    "DPAD_CENTER": "KEYCODE_DPAD_CENTER",
    "MENU": "KEYCODE_MENU",
    "SEARCH": "KEYCODE_SEARCH",
    "VOLUME_UP": "KEYCODE_VOLUME_UP",
    "VOLUME_DOWN": "KEYCODE_VOLUME_DOWN",
}


def utc_now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_bounds(bounds):
    """'[x1,y1][x2,y2]' -> (x1, y1, x2, y2). Raises ValueError if malformed."""
    m = BOUNDS_RE.fullmatch((bounds or "").strip())
    if not m:
        raise ValueError("malformed bounds %r" % (bounds,))
    return tuple(int(v) for v in m.groups())


def node_center(node):
    """Centre (x, y) of a uiautomator node's bounds attribute."""
    x1, y1, x2, y2 = parse_bounds(node.get("bounds", ""))
    return (x1 + x2) // 2, (y1 + y2) // 2


def _node_matches(node, text=None, res_id=None, desc=None):
    rid = node.get("resource-id", "")
    if res_id is not None:
        if rid == res_id or rid.endswith("/" + res_id) or \
                ("/" in rid and rid.split("/")[-1] == res_id.split("/")[-1]):
            return True
        return False
    if text is not None:
        return node.get("text", "") == text
    if desc is not None:
        return node.get("content-desc", "") == desc
    return False


def find_node(root, text=None, res_id=None, desc=None):
    """First matching node in document order, clickable nodes first.

    Exactly one of text, res_id, desc must be given. Returns the
    Element, or None when nothing matches.
    """
    if sum(v is not None for v in (text, res_id, desc)) != 1:
        raise ValueError("find_node needs exactly one of text, res_id, desc")
    matches = [n for n in root.iter("node")
               if _node_matches(n, text=text, res_id=res_id, desc=desc)]
    if not matches:
        return None
    matches.sort(key=lambda n: 0 if n.get("clickable") == "true" else 1)
    return matches[0]


def find_row_action(root, row_text, res_id):
    """Node with res_id on the same row as the text node.

    Returns the res_id node whose centre-y is closest to the
    row text node's centre-y, provided it is within 100 px
    (one drawer-row height); otherwise None. Also None when
    the row text or the res_id has no node at all. Pure
    function over a parsed dump, so it is unit-testable
    without a device.
    """
    row = find_node(root, text=row_text)
    if row is None:
        return None
    _, row_y = node_center(row)
    cands = [n for n in root.iter("node")
             if _node_matches(n, res_id=res_id)]
    if not cands:
        return None
    best = min(cands, key=lambda n: abs(node_center(n)[1] - row_y))
    if abs(node_center(best)[1] - row_y) > 100:
        return None
    return best


def parse_dump(xml_text):
    """Parse uiautomator dump XML text; returns the root Element.

    `uiautomator dump /dev/tty` prints a status line ("UI hierchary dumped to: /dev/tty") right after the XML
    on the same stream, which ElementTree rejects as "junk after document element" (real run 41580858995,
    Kiro 2026-11-03). Parse only the <hierarchy> element itself.
    """
    start = xml_text.find("<hierarchy")
    end = xml_text.rfind("</hierarchy>")
    if start != -1 and end != -1:
        xml_text = xml_text[start:end + len("</hierarchy>")]
    return ET.fromstring(xml_text)


def _shell_quote(arg):
    """Quote one argument for the device shell (single-quote style)."""
    return "'" + arg.replace("'", "'\"'\"'") + "'"


def _input_text_arg(s):
    """Encode text for `adb shell input text`: spaces become %s."""
    return s.replace(" ", "%s")


class Runner:
    """One route's (or one setup's) action runner with step logging."""

    def __init__(self, package, route, edge_ids, log_path, dry_run=False,
                 adb="adb", outdir=None):
        self.package = package
        self.route = route
        self.edge_ids = set(edge_ids) if edge_ids is not None else None
        self.dry_run = bool(dry_run)
        self.adb = adb
        self.outdir = outdir
        self.planned = []  # dry mode: planned adb command strings
        self._log_dir = os.path.dirname(os.path.abspath(log_path))
        os.makedirs(self._log_dir, exist_ok=True)
        self._log = open(log_path, "a", encoding="utf-8")
        self._closed = False

    # -- internals -----------------------------------------------------

    def _check_edge(self, edge):
        if edge is None:
            raise ValueError("every action needs an edge id")
        if self.edge_ids is not None and edge not in self.edge_ids:
            raise ValueError("edge %s is not in this route" % (edge,))

    def _log_line(self, edge, action, target, result):
        line = "%s %s %s %s %s\n" % (utc_now(), edge or "-", action,
                                     target.replace(" ", "_"), result)
        self._log.write(line)
        self._log.flush()
        return line

    def _run(self, args, edge, action, target, input_data=None):
        """Run one adb command (or record it in dry mode)."""
        self._check_edge(edge)
        cmd = [self.adb] + args
        if self.dry_run:
            self.planned.append(" ".join(cmd))
            self._log_line(edge, action, target, "planned")
            return ""
        proc = subprocess.run(cmd, input=input_data, capture_output=True,
                              timeout=120)
        out = proc.stdout
        if isinstance(out, bytes):
            out = out.decode("utf-8", "replace")
        if proc.returncode != 0:
            err = proc.stderr.decode("utf-8", "replace") if isinstance(
                proc.stderr, bytes) else (proc.stderr or "")
            self._log_line(edge, action, target, "failed")
            raise RuntimeError("adb %s failed (%s): %s" % (
                " ".join(args), proc.returncode, err.strip()[:300]))
        self._log_line(edge, action, target, "ok")
        return out

    def _shell(self, shell_args, edge, action, target):
        """Run `adb shell <args>` (each arg device-shell-quoted as needed)."""
        quoted = " ".join(_shell_quote(a) if (" " in a or "'" in a or '"' in a)
                          else a for a in shell_args)
        return self._run(["shell", quoted], edge, action, target)

    # -- device state --------------------------------------------------

    def launch(self, component, edge):
        """Start an activity: `am start -W -n <component>`."""
        self._check_edge(edge)
        self._shell(["am", "start", "-W", "-n", component], edge, "launch",
                    "component=%s" % component)

    def key(self, name, edge):
        code = KEY_ALIASES.get(name, name)
        self._shell(["input", "keyevent", code], edge, "key", code)

    def back(self, edge):
        self.key("KEYCODE_BACK", edge)

    def rotate(self, edge, orientation="landscape"):
        """Rotate the display: disable auto-rotation, force orientation.

        orientation is 'portrait' (user_rotation 0) or 'landscape'
        (user_rotation 1). Two shell settings, so two log lines for
        the one rotation edge. Anything else raises ValueError.
        """
        if orientation == "portrait":
            rot = "0"
        elif orientation == "landscape":
            rot = "1"
        else:
            raise ValueError(
                "rotate orientation must be 'portrait' or 'landscape'")
        self._shell(["settings", "put", "system", "accelerometer_rotation",
                     "0"], edge, "rotate", "orientation=%s" % orientation)
        self._shell(["settings", "put", "system", "user_rotation", rot],
                    edge, "rotate", "orientation=%s" % orientation)

    # -- background, kill, restore --------------------------------------

    def kill_app(self, edge):
        """Background the app (HOME) and kill its processes (`am kill`).

        `am kill` only kills BACKGROUND processes, so HOME first is
        enforced inside this method (scripts must not call `am kill`
        directly). Two log lines (key + kill) for the one edge.
        Note: a foreground-service process may survive `am kill`;
        scripts that need a service dead must verify via the
        coverage result, not assume the kill.
        """
        self.key("HOME", edge)
        self._shell(["am", "kill", self.package], edge, "kill_app",
                    "package=%s" % self.package)

    def relaunch(self, edge, component):
        """Start an activity again after kill_app (`am start -W -n`).

        NOTE: this starts a fresh task stack — it does NOT restore
        the pre-kill activity stack. Use restore_from_recents when
        the route needs the stack (and its savedInstanceState)
        restored; use relaunch when the route's target is reached
        on a fresh launch after the kill (e.g. a restarted service).
        """
        self._shell(["am", "start", "-W", "-n", component], edge,
                    "relaunch", "component=%s" % component)

    def restore_from_recents(self, edge, text):
        """Restore the app's task from the recents screen.

        Opens recents (APP_SWITCH), waits 1 s in real mode for the
        recents UI to appear (settle delay, not a logged step), then
        taps the recents card with the given text (usually the app
        label). The system restores the task's activity stack with
        savedInstanceState. If the card is not found, tap raises
        LookupError loudly — a missing card is never silently
        treated as a restore.
        """
        self.key("APP_SWITCH", edge)
        if not self.dry_run:
            time.sleep(1)
        self.tap(edge, text=text)

    def set_always_finish(self, edge, enabled):
        """Set global always_finish_activities (1/0).

        When enabled, the system destroys every activity as soon as
        the user leaves it — a route can then test recreation
        (onCreate with savedInstanceState) without a kill. WARNING:
        this is a GLOBAL setting and `pm clear` does NOT reset it,
        so any script that enables it MUST disable it again before
        done(), or the setting leaks into every later route in the
        run. `enabled` must be a bool.
        """
        if not isinstance(enabled, bool):
            raise ValueError("set_always_finish enabled must be a bool")
        self._shell(["settings", "put", "global",
                     "always_finish_activities", "1" if enabled else "0"],
                    edge, "always_finish", "enabled=%s" % enabled)

    def set_locale(self, edge, locale):
        """Set the system locale (global system_locales, API 27+).

        `locale` is a BCP-47 tag such as "ja-JP" or "zh-TW" (also
        accepted with an underscore, "ja_JP", normalized to a dash).
        The setting alone does not re-localize a running app: the
        script must kill_app + relaunch afterwards so the app
        launches under the new locale. WARNING: this is a GLOBAL
        setting and `pm clear` does NOT reset it, so any script
        that changes it MUST restore the previous locale before
        done() (the next route's fresh launch then uses the
        restored locale). A malformed tag raises ValueError.
        """
        if not isinstance(locale, str):
            raise ValueError("set_locale locale must be a string")
        tag = locale.replace("_", "-")
        if not re.fullmatch(r"[a-z]{2,3}(-[A-Z]{2})?", tag):
            raise ValueError("set_locale locale must look like ja-JP, "
                             "zh-CN, or zh-TW (got %r)" % locale)
        self._shell(["settings", "put", "global", "system_locales", tag],
                    edge, "set_locale", "locale=%s" % tag)

    # -- taps, text, scrolling ------------------------------------------

    def _find_for_tap(self, edge, action, text=None, res_id=None, desc=None):
        if self.dry_run:
            target = "text=%s" % text if text is not None else (
                "res_id=%s" % res_id if res_id is not None else "desc=%s" % desc)
            self._check_edge(edge)
            self.planned.append("%s shell input tap <%s>" % (self.adb, target))
            self._log_line(edge, action, target, "planned")
            return None
        root = self._raw_dump()
        node = find_node(root, text=text, res_id=res_id, desc=desc)
        if node is None:
            self._log_line(edge, action,
                           "text=%s" % text if text is not None else (
                               "res_id=%s" % res_id if res_id is not None
                               else "desc=%s" % desc), "failed")
            raise LookupError("no UI node for tap target")
        return node

    def _raw_dump(self):
        """UI dump XML root, via exec-out (no step line of its own)."""
        proc = subprocess.run(
            [self.adb, "exec-out", "uiautomator", "dump", "/dev/tty"],
            capture_output=True, timeout=120)
        out = proc.stdout.decode("utf-8", "replace") if isinstance(
            proc.stdout, bytes) else proc.stdout
        if proc.returncode != 0 or "<hierarchy" not in out:
            # Fallback: dump to a file on device, then pull it.
            subprocess.run([self.adb, "shell", "uiautomator", "dump",
                            "/sdcard/window_dump.xml"],
                           capture_output=True, timeout=120)
            proc2 = subprocess.run(
                [self.adb, "pull", "/sdcard/window_dump.xml", "-"],
                capture_output=True, timeout=120)
            out = proc2.stdout.decode("utf-8", "replace") if isinstance(
                proc2.stdout, bytes) else proc2.stdout
        return parse_dump(out)

    def tap(self, edge, text=None, res_id=None, desc=None, x=None, y=None,
            why=None):
        """Tap a view found by text, res_id, or desc; or fixed x/y with why."""
        if x is not None or y is not None:
            if x is None or y is None or not why:
                raise ValueError(
                    "fixed-coordinate tap needs both x and y and a why string")
            self._shell(["input", "tap", str(x), str(y)], edge, "tap",
                        "xy=%d,%d" % (x, y))
            return
        if sum(v is not None for v in (text, res_id, desc)) != 1:
            raise ValueError("tap needs exactly one of text, res_id, desc")
        node = self._find_for_tap(edge, "tap", text=text, res_id=res_id,
                                  desc=desc)
        if node is None:
            return  # dry mode already logged
        cx, cy = node_center(node)
        label = "text=%s" % text if text is not None else (
            "res_id=%s" % res_id if res_id is not None else "desc=%s" % desc)
        self._shell(["input", "tap", str(cx), str(cy)], edge, "tap", label)

    def long_tap(self, edge, text=None, res_id=None, desc=None, duration_ms=1000):
        if sum(v is not None for v in (text, res_id, desc)) != 1:
            raise ValueError("long_tap needs exactly one of text, res_id, desc")
        node = self._find_for_tap(edge, "long_tap", text=text, res_id=res_id,
                                  desc=desc)
        if node is None:
            return  # dry mode already logged
        cx, cy = node_center(node)
        label = "text=%s" % text if text is not None else (
            "res_id=%s" % res_id if res_id is not None else "desc=%s" % desc)
        self._shell(["input", "swipe", str(cx), str(cy), str(cx), str(cy),
                     str(duration_ms)], edge, "long_tap", label)

    def drag(self, edge, x1, y1, x2, y2, duration_ms=1500, why=None):
        """Long-press drag: `input swipe` from (x1, y1) to (x2, y2).

        A swipe whose duration covers the long-press threshold
        (~500 ms) registers as a press first and then a drag — this
        is how launcher widget placement is driven (long-press the
        widget, drag it onto the home screen). duration_ms must be
        >= 500 (below that the gesture is a fling, not a drag) and
        a `why` string is required, as for fixed-coordinate taps:
        the endpoints have no node to resolve. If a launcher
        rejects swipe-drags (it needs a true stationary hold before
        the move), use the sendevent multi-touch primitives, which
        can hold one contact stationary while moving another.
        """
        for v in (x1, y1, x2, y2):
            if not isinstance(v, int) or isinstance(v, bool):
                raise ValueError("drag coordinates must be ints")
        if duration_ms < 500:
            raise ValueError("drag duration_ms must be >= 500 "
                             "(long-press threshold)")
        if not why:
            raise ValueError("drag needs a why string for its fixed "
                             "coordinates")
        self._shell(["input", "swipe", str(x1), str(y1), str(x2), str(y2),
                     str(duration_ms)], edge, "drag",
                    "xy=%d,%d->%d,%d" % (x1, y1, x2, y2))

    def drag_from(self, edge, x2, y2, text=None, res_id=None, desc=None,
                  duration_ms=1500, why=None):
        """Long-press drag starting on a resolved node, to (x2, y2).

        The start node is found by text, res_id, or desc (exactly
        one); the drop point is fixed coordinates, so a `why`
        string is required for it. In dry mode one planned drag
        line is recorded (no tap plan: this is a drag, not a tap).
        """
        if sum(v is not None for v in (text, res_id, desc)) != 1:
            raise ValueError("drag_from needs exactly one of text, res_id, desc")
        if not isinstance(x2, int) or not isinstance(y2, int) or \
                isinstance(x2, bool) or isinstance(y2, bool):
            raise ValueError("drag_from drop coordinates must be ints")
        if duration_ms < 500:
            raise ValueError("drag_from duration_ms must be >= 500 "
                             "(long-press threshold)")
        if not why:
            raise ValueError("drag_from needs a why string for its fixed "
                             "drop coordinates")
        label = "text=%s" % text if text is not None else (
            "res_id=%s" % res_id if res_id is not None else "desc=%s" % desc)
        if self.dry_run:
            self._check_edge(edge)
            self.planned.append(
                "%s shell input swipe (drag from %s to %d,%d)"
                % (self.adb, label, x2, y2))
            self._log_line(edge, "drag_from",
                           "%s->%d,%d" % (label, x2, y2), "planned")
            return
        root = self._raw_dump()
        node = find_node(root, text=text, res_id=res_id, desc=desc)
        if node is None:
            self._log_line(edge, "drag_from", label, "failed")
            raise LookupError("no UI node for drag start")
        cx, cy = node_center(node)
        self._shell(["input", "swipe", str(cx), str(cy), str(x2), str(y2),
                     str(duration_ms)], edge, "drag_from",
                    "%s->%d,%d" % (label, x2, y2))

    def tap_row_action(self, edge, row_text, res_id):
        """Tap the res_id action node on the row labelled row_text.

        Drawer rows with an action view share one res_id across
        rows (Amaze: every server/storage row's trailing icon is
        id/imageButton), so tap(res_id) would pick the first
        row's icon. This resolves the row by text first, then
        taps that row's action node via find_row_action; a
        missing row, missing action, or action on another row
        raises LookupError (fail loudly, never tap the wrong
        row). In dry mode one planned line is recorded.
        """
        if not row_text or not res_id:
            raise ValueError("tap_row_action needs row_text and res_id")
        if self.dry_run:
            self._check_edge(edge)
            self.planned.append(
                "%s shell input tap <row text=%s action res_id=%s>"
                % (self.adb, row_text, res_id))
            self._log_line(edge, "tap_row_action",
                           "row_text=%s res_id=%s" % (row_text, res_id),
                           "planned")
            return
        root = self._raw_dump()
        node = find_row_action(root, row_text, res_id)
        if node is None:
            self._log_line(edge, "tap_row_action",
                           "row_text=%s res_id=%s" % (row_text, res_id),
                           "failed")
            raise LookupError("no action node on the row of %s" % row_text)
        cx, cy = node_center(node)
        self._shell(["input", "tap", str(cx), str(cy)], edge,
                    "tap_row_action",
                    "row_text=%s res_id=%s" % (row_text, res_id))

    # -- multi-touch (sendevent) -----------------------------------------
    # Linux input event constants for the touchscreen MT protocol
    # (slot-based, protocol B). The event node varies per emulator
    # (discover it with `adb shell getevent -i` / `getevent -p` and
    # pass it as `device`); a wrong node silently does nothing, so
    # a gesture on a wrong node yields unclear, never wrong — the
    # JaCoCo result decides whether the target fired.

    # -- row action (drawer action views) --------------------------------
    # Drawer rows with an action view (e.g. Amaze server rows: the
    # row body navigates, the trailing edit icon opens the edit
    # dialog) share one res_id across rows, so tap(res_id) would
    # pick the first row's icon — the wrong row. tap_row_action
    # finds the row by its text, then taps the res_id node on
    # that row (closest centre-y, within 100 px); anything else
    # fails loudly instead of tapping the wrong row.

    # Linux input event types/codes for the touchscreen MT protocol.
    EV_SYN, EV_KEY, EV_ABS = 0, 1, 3
    SYN_REPORT = 0
    BTN_TOUCH = 330
    ABS_MT_SLOT, ABS_MT_POSITION_X, ABS_MT_POSITION_Y = 47, 53, 54
    ABS_MT_TRACKING_ID = 57

    def _send_events(self, edge, device, events, action, target):
        """Send one compound `sendevent` shell command (one log line).

        events is a list of (type, code, value) int tuples. All
        values are validated as ints, so the built command string
        cannot inject shell syntax. In dry mode the full command is
        recorded as one planned line.
        """
        if not re.fullmatch(r"/dev/input/event\d+", device or ""):
            raise ValueError("sendevent device must be /dev/input/eventN")
        parts = []
        for (t, c, v) in events:
            if not all(isinstance(x, int) and not isinstance(x, bool)
                       for x in (t, c, v)):
                raise ValueError("sendevent events must be int tuples")
            parts.append("sendevent %s %d %d %d" % (device, t, c, v))
        self._run(["shell", "; ".join(parts)], edge, action, target)

    def two_finger_swipe(self, edge, device, start1, start2, end1, end2,
                         steps=10):
        """Two contacts moving together: DOWN, interpolated MOVEs, UP.

        start1/start2/end1/end2 are (x, y) int pairs; the two start
        points must differ (otherwise this is not multi-touch).
        steps interpolations run from the starts to the ends
        (steps >= 1). The whole gesture is one adb shell command
        and one log line. This is the primitive for routes that
        need getPointerCount() > 1 (e.g. a fling handler that
        returns early for a single finger): two contacts moving
        together report pointer count 2 throughout the move.
        """
        for pt in (start1, start2, end1, end2):
            if len(pt) != 2 or not all(
                    isinstance(v, int) and not isinstance(v, bool)
                    for v in pt):
                raise ValueError("two_finger_swipe points must be (x, y) ints")
        if start1 == start2:
            raise ValueError("two_finger_swipe start points must differ")
        if steps < 1:
            raise ValueError("two_finger_swipe steps must be >= 1")
        E = self  # event constants live on the class
        ev = []
        # DOWN: slot 0 first contact (+ BTN_TOUCH), then slot 1.
        ev += [(E.EV_ABS, E.ABS_MT_SLOT, 0),
               (E.EV_ABS, E.ABS_MT_TRACKING_ID, 0),
               (E.EV_ABS, E.ABS_MT_POSITION_X, start1[0]),
               (E.EV_ABS, E.ABS_MT_POSITION_Y, start1[1]),
               (E.EV_KEY, E.BTN_TOUCH, 1),
               (E.EV_SYN, E.SYN_REPORT, 0)]
        ev += [(E.EV_ABS, E.ABS_MT_SLOT, 1),
               (E.EV_ABS, E.ABS_MT_TRACKING_ID, 1),
               (E.EV_ABS, E.ABS_MT_POSITION_X, start2[0]),
               (E.EV_ABS, E.ABS_MT_POSITION_Y, start2[1]),
               (E.EV_SYN, E.SYN_REPORT, 0)]
        # MOVEs: linear interpolation, both slots per step + SYN.
        for i in range(1, steps + 1):
            for slot, a, b in ((0, start1, end1), (1, start2, end2)):
                x = round(a[0] + (b[0] - a[0]) * i / steps)
                y = round(a[1] + (b[1] - a[1]) * i / steps)
                ev += [(E.EV_ABS, E.ABS_MT_SLOT, slot),
                       (E.EV_ABS, E.ABS_MT_POSITION_X, x),
                       (E.EV_ABS, E.ABS_MT_POSITION_Y, y)]
            ev += [(E.EV_SYN, E.SYN_REPORT, 0)]
        # UP: both tracking ids released, BTN_TOUCH off, SYN.
        ev += [(E.EV_ABS, E.ABS_MT_SLOT, 0),
               (E.EV_ABS, E.ABS_MT_TRACKING_ID, -1),
               (E.EV_ABS, E.ABS_MT_SLOT, 1),
               (E.EV_ABS, E.ABS_MT_TRACKING_ID, -1),
               (E.EV_KEY, E.BTN_TOUCH, 0),
               (E.EV_SYN, E.SYN_REPORT, 0)]
        self._send_events(edge, device, ev, "two_finger_swipe",
                          "device=%s steps=%d" % (device, steps))

    def two_finger_tap(self, edge, device, point1, point2):
        """Two contacts down together, then up together (no move)."""
        for pt in (point1, point2):
            if len(pt) != 2 or not all(
                    isinstance(v, int) and not isinstance(v, bool)
                    for v in pt):
                raise ValueError("two_finger_tap points must be (x, y) ints")
        if point1 == point2:
            raise ValueError("two_finger_tap points must differ")
        E = self
        ev = [(E.EV_ABS, E.ABS_MT_SLOT, 0),
              (E.EV_ABS, E.ABS_MT_TRACKING_ID, 0),
              (E.EV_ABS, E.ABS_MT_POSITION_X, point1[0]),
              (E.EV_ABS, E.ABS_MT_POSITION_Y, point1[1]),
              (E.EV_KEY, E.BTN_TOUCH, 1),
              (E.EV_SYN, E.SYN_REPORT, 0),
              (E.EV_ABS, E.ABS_MT_SLOT, 1),
              (E.EV_ABS, E.ABS_MT_TRACKING_ID, 1),
              (E.EV_ABS, E.ABS_MT_POSITION_X, point2[0]),
              (E.EV_ABS, E.ABS_MT_POSITION_Y, point2[1]),
              (E.EV_SYN, E.SYN_REPORT, 0),
              (E.EV_ABS, E.ABS_MT_SLOT, 0),
              (E.EV_ABS, E.ABS_MT_TRACKING_ID, -1),
              (E.EV_ABS, E.ABS_MT_SLOT, 1),
              (E.EV_ABS, E.ABS_MT_TRACKING_ID, -1),
              (E.EV_KEY, E.BTN_TOUCH, 0),
              (E.EV_SYN, E.SYN_REPORT, 0)]
        self._send_events(edge, device, ev, "two_finger_tap",
                          "device=%s" % device)

    def type_text(self, s, edge):
        self._shell(["input", "text", _input_text_arg(s)], edge, "type_text",
                    "len=%d" % len(s))

    def scroll_to(self, edge, text=None, res_id=None):
        if sum(v is not None for v in (text, res_id)) != 1:
            raise ValueError("scroll_to needs exactly one of text, res_id")
        label = "text=%s" % text if text is not None else "res_id=%s" % res_id
        if self.dry_run:
            self._check_edge(edge)
            self.planned.append("%s shell input swipe (scroll to %s)"
                                % (self.adb, label))
            self._log_line(edge, "scroll_to", label, "planned")
            return
        for _ in range(10):
            root = self._raw_dump()
            if find_node(root, text=text, res_id=res_id) is not None:
                self._log_line(edge, "scroll_to", label, "ok")
                return
            self._shell(["input", "swipe", "500", "1500", "500", "500", "300"],
                        edge, "scroll_to", label)
        self._log_line(edge, "scroll_to", label, "failed")
        raise LookupError("scroll_to did not find %s" % label)

    def wait_for(self, edge, text=None, res_id=None, desc=None, timeout=10):
        if sum(v is not None for v in (text, res_id, desc)) != 1:
            raise ValueError(
                "wait_for needs exactly one of text, res_id, desc")
        label = "text=%s" % text if text is not None else (
            "res_id=%s" % res_id if res_id is not None else "desc=%s" % desc)
        if self.dry_run:
            self._check_edge(edge)
            self.planned.append("%s wait for %s" % (self.adb, label))
            self._log_line(edge, "wait_for", label, "planned")
            return
        deadline = time.time() + timeout
        while time.time() < deadline:
            root = self._raw_dump()
            if find_node(root, text=text, res_id=res_id,
                         desc=desc) is not None:
                self._log_line(edge, "wait_for", label, "ok")
                return
            time.sleep(1)
        self._log_line(edge, "wait_for", label, "failed")
        raise TimeoutError("wait_for timed out for %s" % label)

    def dwell(self, edge, seconds):
        """Host-side wait: sleep `seconds`, one log line, no adb call.

        For timed routes (e.g. a clear that only fires after 60 s
        of inactivity): the script dwells, then acts. In dry mode
        no time passes — one planned line is recorded. seconds
        must satisfy 0 < seconds <= 600 (the route script's own
        10-minute timeout bounds any dwell plus the other steps).
        """
        if not isinstance(seconds, (int, float)) or isinstance(seconds, bool) \
                or seconds <= 0 or seconds > 600:
            raise ValueError("dwell seconds must satisfy 0 < seconds <= 600")
        if self.dry_run:
            self._check_edge(edge)
            self.planned.append("sleep %ss (dwell)" % seconds)
            self._log_line(edge, "dwell", "seconds=%s" % seconds, "planned")
            return
        time.sleep(seconds)
        self._log_line(edge, "dwell", "seconds=%s" % seconds, "ok")

    # -- intents, permissions, fixtures ---------------------------------

    def start_intent(self, edge, action=None, data=None, mime=None,
                     extras=None, extras_args=None, component=None):
        args = ["am", "start"]
        if action:
            args += ["-a", action]
        if data:
            args += ["-d", data]
        if mime:
            args += ["-t", mime]
        for k, v in (extras or {}).items():
            args += ["--es", k, v]
        args += list(extras_args or [])
        if component:
            args += ["-n", component]
        label = "action=%s" % (action or "-")
        if component:
            label += " component=%s" % component
        self._shell(args, edge, "start_intent", label)

    def broadcast(self, edge, action=None, extras=None, extras_args=None,
                  component=None):
        args = ["am", "broadcast"]
        if action:
            args += ["-a", action]
        for k, v in (extras or {}).items():
            args += ["--es", k, v]
        args += list(extras_args or [])
        if component:
            args += ["-n", component]
        self._shell(args, edge, "broadcast",
                    "action=%s" % (action or "-"))

    def grant(self, perm, edge):
        self._shell(["pm", "grant", self.package, perm], edge, "grant", perm)

    def deny(self, perm, edge):
        self._shell(["pm", "revoke", self.package, perm], edge, "deny", perm)

    def push_fixture(self, local, edge, dest=None):
        target = dest or ("/sdcard/" + os.path.basename(local))
        # Log target carries the local path too ("<local> -> <dest>"):
        # drycheck's fixture-coverage check reads the dry-run steps
        # log and verifies every pushed file is named in the route's
        # ROUTES.csv fixtures cell (item 12(b)).
        self._run(["push", local, target], edge, "push_fixture",
                  "%s -> %s" % (local, target))

    # -- evidence, assertions, comments ----------------------------------

    def screenshot(self, name, edge):
        if not name.endswith(".png"):
            name += ".png"
        if self.outdir:
            path = os.path.join(self.outdir, "screens", self.route, name)
            os.makedirs(os.path.dirname(path), exist_ok=True)
        else:
            path = os.path.join("screens", self.route, name)
            os.makedirs(os.path.dirname(path), exist_ok=True)
        if self.dry_run:
            self._check_edge(edge)
            self.planned.append("%s exec-out screencap -p > %s"
                                % (self.adb, path))
            self._log_line(edge, "screenshot", path, "planned")
            return
        proc = subprocess.run([self.adb, "exec-out", "screencap", "-p"],
                              capture_output=True, timeout=120)
        if proc.returncode != 0:
            self._log_line(edge, "screenshot", path, "failed")
            raise RuntimeError("screencap failed")
        with open(path, "wb") as f:
            f.write(proc.stdout)
        self._log_line(edge, "screenshot", path, "ok")

    def dump_ui(self, name, edge):
        if not name.endswith(".xml"):
            name += ".xml"
        if self.outdir:
            path = os.path.join(self.outdir, "dumps", self.route, name)
            os.makedirs(os.path.dirname(path), exist_ok=True)
        else:
            path = os.path.join("dumps", self.route, name)
            os.makedirs(os.path.dirname(path), exist_ok=True)
        if self.dry_run:
            self._check_edge(edge)
            self.planned.append("%s exec-out uiautomator dump > %s"
                                % (self.adb, path))
            self._log_line(edge, "dump_ui", path, "planned")
            return
        root = self._raw_dump()
        ET.ElementTree(root).write(path, encoding="utf-8", xml_declaration=True)
        self._log_line(edge, "dump_ui", path, "ok")

    def assert_text(self, text, edge):
        if self.dry_run:
            self._check_edge(edge)
            self.planned.append("%s assert text=%s" % (self.adb, text))
            self._log_line(edge, "assert_text", "text=%s" % text, "planned")
            return
        root = self._raw_dump()
        found = any(text in (n.get("text", "") or "") or
                    text in (n.get("content-desc", "") or "")
                    for n in root.iter("node"))
        if not found:
            self._log_line(edge, "assert_text", "text=%s" % text, "failed")
            raise AssertionError("text not on screen: %r" % (text,))
        self._log_line(edge, "assert_text", "text=%s" % text, "ok")

    def comment(self, text, edge):
        """Log a no-action edge (lifecycle/framework edge with no UI step)."""
        self._check_edge(edge)
        self._log_line(edge, "comment", text, "ok")

    def done(self):
        if not self._closed:
            self._log.flush()
            self._log.close()
            self._closed = True


def main(argv):
    sys.stderr.write("harness.py is a library; run device/harness/test_harness.py\n")
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
