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


def parse_dump(xml_text):
    """Parse uiautomator dump XML text; returns the root Element."""
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

    def wait_for(self, edge, text=None, res_id=None, timeout=10):
        if sum(v is not None for v in (text, res_id)) != 1:
            raise ValueError("wait_for needs exactly one of text, res_id")
        label = "text=%s" % text if text is not None else "res_id=%s" % res_id
        if self.dry_run:
            self._check_edge(edge)
            self.planned.append("%s wait for %s" % (self.adb, label))
            self._log_line(edge, "wait_for", label, "planned")
            return
        deadline = time.time() + timeout
        while time.time() < deadline:
            root = self._raw_dump()
            if find_node(root, text=text, res_id=res_id) is not None:
                self._log_line(edge, "wait_for", label, "ok")
                return
            time.sleep(1)
        self._log_line(edge, "wait_for", label, "failed")
        raise TimeoutError("wait_for timed out for %s" % label)

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
        self._run(["push", local, target], edge, "push_fixture", target)

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
