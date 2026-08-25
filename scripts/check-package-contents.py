#!/usr/bin/env python3
"""Require exact Cargo package payloads; fail on additions and omissions."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXPECTED = {'openbim-citygml': ['.cargo_vcs_info.json', 'Cargo.lock', 'Cargo.toml', 'Cargo.toml.orig', 'LICENSE', 'README.md', 'src/lib.rs'], 'citygml': ['.cargo_vcs_info.json', 'Cargo.lock', 'Cargo.toml', 'Cargo.toml.orig', 'LICENSE', 'README.md', 'src/lib.rs']}

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
if errors:
    for error in errors:
        print(f"package contents error: {error}", file=sys.stderr)
    raise SystemExit(1)
print("package contents: exact allowlists verified")
