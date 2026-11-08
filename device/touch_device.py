#!/usr/bin/env python3
"""Find the touchscreen event node from `adb shell getevent -i` output.

Usage: adb shell getevent -i | python3 -I device/touch_device.py
Prints the first /dev/input/eventN device whose ABS set includes
both ABS_MT_POSITION_X (0x35) and ABS_MT_POSITION_Y (0x36) — the
touchscreen — and exits 0. Exits 1 (printing nothing) when no such
device is found, so the caller falls back to its default node and
logs a warning instead of silently using a wrong node.

getevent -i output shape (per device):
    add device 1: /dev/input/event0
      bus:      ...
      name:     "Power Button"
      events:
        EV_KEY (0001): ...
        EV_ABS (0003): 0030 0031 ...
A device section starts at an "add device" line; the ABS line lists
the supported absolute axes as hex codes. Only stdlib is used.
"""

import re
import sys

DEVICE_RE = re.compile(r"^add device \d+: (/dev/input/event\d+)\s*$")
ABS_RE = re.compile(r"^\s+EV_ABS \(0003\):\s*(.*)$")


def find_touchscreen(lines):
    """First event node whose ABS set has 0035 and 0036, else None."""
    device = None
    for line in lines:
        m = DEVICE_RE.match(line)
        if m:
            device = m.group(1)
            continue
        m = ABS_RE.match(line)
        if m and device is not None:
            codes = set(m.group(1).split())
            if "0035" in codes and "0036" in codes:
                return device
            device = None  # this device is not a touchscreen; keep scanning
    return None


def main(argv=None):
    node = find_touchscreen(sys.stdin.read().splitlines())
    if node is None:
        return 1
    sys.stdout.write(node + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
