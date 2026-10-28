#!/usr/bin/env python3
"""Require exact Cargo package payloads; fail on additions and omissions."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXPECTED = {'openbim-citygml': ['.cargo_vcs_info.json', 'Cargo.lock', 'Cargo.toml', 'Cargo.toml.orig', 'LICENSE', 'LICENSES/LicenseRef-Commercial.txt', 'LICENSES/MIT.txt', 'NOTICE', 'README.md', 'src/lib.rs'], 'citygml': ['.cargo_vcs_info.json', 'Cargo.lock', 'Cargo.toml', 'Cargo.toml.orig', 'LICENSE', 'LICENSES/LicenseRef-Commercial.txt', 'LICENSES/MIT.txt', 'NOTICE', 'README.md', 'src/lib.rs']}

EXPRESSION = 'license = "AGPL-3.0-or-later OR LicenseRef-Commercial"'
SHIPPED_LICENCES = ("LICENSE", "NOTICE", "LICENSES/LicenseRef-Commercial.txt")

errors: list[str] = []
for package, expected in EXPECTED.items():
    result = subprocess.run(
        ["cargo", "package", "--locked", "--allow-dirty", "--list", "-p", package],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    actual = sorted(line for line in result.stdout.splitlines() if line)
    wanted = sorted(expected)
    missing = sorted(set(wanted) - set(actual))
    unexpected = sorted(set(actual) - set(wanted))
    if missing or unexpected or actual != wanted:
        errors.append(
            f"{package} payload mismatch: missing={missing}, unexpected={unexpected}"
        )
# Each crate ships byte-identical copies of the root licence texts and notice
# and declares the dual expression.
for package in EXPECTED:
    crate = ROOT / package
    for name in SHIPPED_LICENCES:
        shipped = crate / name
        if not shipped.is_file() or shipped.read_bytes() != (ROOT / name).read_bytes():
            errors.append(f"{package}: {name} is missing or differs from the root")
    if EXPRESSION not in (crate / "Cargo.toml").read_text(encoding="utf-8").splitlines():
        errors.append(f"{package}: unexpected license expression")
if errors:
    for error in errors:
        print(f"package contents error: {error}", file=sys.stderr)
    raise SystemExit(1)
print("package contents: exact allowlists verified")
