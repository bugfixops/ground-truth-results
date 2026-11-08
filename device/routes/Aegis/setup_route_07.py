#!/usr/bin/env python3
# STAGING — Aegis device-final, NEW final sample (post-fix redraw, seed 20261025).
# Per-route setup for new setup_route_07. Run-time generation only; nothing here is
# committed as a binary. Interface: --package --log --outdir --gen-dir (GEN_DIR
# fallback). No real emulator/adb run, no CI request, no drycheck pass claimed.

"""Aegis route_07 setup: generate authplus_backup.zip at run time.

Run-time generated fixture for ROUTES.csv gen form
gen:authplus_backup.zip -> /sdcard/Download/authplus_backup.zip.
run_app.sh pushes the generated file to /sdcard/Download/ before
route_07 runs; this script itself pushes nothing to the device and
the generated file is never committed -- it lives only under the
run's out dir.

Format (AuthenticatorPlusImporter.java): a password-protected zip
(zip4j ZipInputStream with the typed password) containing an entry
named exactly "Accounts.txt" whose lines are GoogleAuthUri lines
(otpauth:// URIs). The zip uses traditional ZipCrypto encryption
(STORED entry); Python's zipfile cannot write encrypted zips, so
the ZipCrypto stream cipher and zip structures are built here with
the standard library only. The password is "aegis-test-password",
exactly as the route script types it.

Usage (invoked by run_app.sh; all arguments optional except --gen-dir
when run standalone):
    setup_route_07.py --package <pkg> --log <log> --outdir <dir> \
        --gen-dir <dir>
"""

import argparse
import os
import sys
import struct


# ---- Traditional ZipCrypto (stream cipher), stdlib only ----
# Key schedule per the PKWARE APPNOTE: key0 starts 0x12345678,
# key1 0x23456789, key2 0x34567890; CRC32 drives key0/key2.
_ZIP_KEYS0 = 0x12345678


def _zip_crc32(crc, byte):
    crc ^= byte
    for _ in range(8):
        crc = (crc >> 1) ^ (0xedb88320 if crc & 1 else 0)
    return crc & 0xffffffff


def _zip_update_keys(keys, byte):
    k0, k1, k2 = keys
    k0 = _zip_crc32(k0, byte)
    k1 = ((k1 + (k0 & 0xff)) * 134775813 + 1) & 0xffffffff
    k2 = _zip_crc32(k2, (k1 >> 24) & 0xff)
    return (k0, k1, k2)


def _zip_decrypt_byte(k2):
    temp = (k2 | 2) & 0xffffffff
    return ((temp * (temp ^ 1)) >> 8) & 0xff


def _zip_encrypt_data(password, plaintext):
    """Encrypt plaintext (bytes) with ZipCrypto; returns encrypted bytes
    starting with the 12-byte encryption header. The header's last byte
    is the high byte of the plaintext CRC (general-purpose flag bit 3
    is clear, so readers check it against the CRC)."""
    keys = (0x12345678, 0x23456789, 0x34567890)
    for ch in password.encode("utf-8"):
        keys = _zip_update_keys(keys, ch)
    import binascii
    crc = binascii.crc32(plaintext) & 0xffffffff
    header = os.urandom(11) + bytes([(crc >> 24) & 0xff])
    out = bytearray()
    for byte in header + plaintext:
        out.append(byte ^ _zip_decrypt_byte(keys[2]))
        keys = _zip_update_keys(keys, byte)
    return bytes(out)


def _zip_stored_encrypted(filename, plaintext, password):
    """Build a minimal zip with one STORED, ZipCrypto-encrypted entry."""
    import binascii
    crc = binascii.crc32(plaintext) & 0xffffffff
    enc = _zip_encrypt_data(password, plaintext)
    name = filename.encode("utf-8")
    # MS-DOS date/time: 2020-01-01 00:00:00 (fixed; content is what matters)
    dostime = 0
    dosdate = ((2020 - 1980) << 9) | (1 << 5) | 1
    local = struct.pack("<IHHHHHIIIHH",
                        0x04034b50, 20, 0x0001, 0, dostime, dosdate,
                        crc, len(enc), len(plaintext), len(name), 0)
    local += name + enc
    central = struct.pack("<IHHHHHHIIIHHHHHII",
                          0x02014b50, 20, 20, 0x0001, 0, dostime, dosdate,
                          crc, len(enc), len(plaintext), len(name),
                          0, 0, 0, 0, 0, 0)
    central += name
    cd_offset = len(local)
    eocd = struct.pack("<IHHHHIIH",
                       0x06054b50, 0, 0, 1, 1, len(central), cd_offset, 0)
    return local + central + eocd


PASSWORD = "aegis-test-password"


def build(gen_dir):
    accounts = (
        "otpauth://totp/TestIssuer:testuser"
        "?secret=JBSWY3DPEHPK3PXP&issuer=TestIssuer"
        "&algorithm=SHA1&digits=6&period=30\n"
    ).encode("utf-8")
    blob = _zip_stored_encrypted("Accounts.txt", accounts, PASSWORD)
    out_path = os.path.join(gen_dir, "authplus_backup.zip")
    with open(out_path, "wb") as f:
        f.write(blob)
    return out_path, "Authenticator Plus, ZipCrypto zip, Accounts.txt (1 URI)"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--package", default="")
    parser.add_argument("--log", default=None)
    parser.add_argument("--outdir", default=None)
    parser.add_argument("--gen-dir", default=None)
    args = parser.parse_args(argv)
    gen_dir = args.gen_dir or os.path.join(os.getcwd(), "gen")
    os.makedirs(gen_dir, exist_ok=True)
    out_path, detail = build(gen_dir)
    size = os.path.getsize(out_path)
    line = "generated %s (%d bytes, %s)\n" % (os.path.basename(out_path), size, detail)
    if args.log:
        with open(args.log, "a", encoding="utf-8") as f:
            f.write(line)
    sys.stdout.write(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
