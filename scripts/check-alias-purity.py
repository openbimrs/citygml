#!/usr/bin/env python3
"""Semantically verify the citygml alias source and exact dependency pin."""

from __future__ import annotations

import pathlib
import re
import sys
import tomllib

ROOT = pathlib.Path(__file__).resolve().parent.parent
ALIAS_SOURCE = ROOT / "citygml" / "src" / "lib.rs"
ALIAS_MANIFEST = ROOT / "citygml" / "Cargo.toml"
CANONICAL_PACKAGE = "openbim-citygml"
CANONICAL_CRATE = "openbim_citygml"
EXPECTED_TOKENS = ["pub", "use", CANONICAL_CRATE, "::", "*", ";"]


def without_comments(source: str) -> str:
    """Remove nested Rust line/block comments while preserving other text."""
    output: list[str] = []
    index = 0
    block_depth = 0
    while index < len(source):
        pair = source[index : index + 2]
        if block_depth:
            if pair == "/*":
                block_depth += 1
                index += 2
            elif pair == "*/":
                block_depth -= 1
                index += 2
            else:
                index += 1
            continue
        if pair == "//":
            newline = source.find("\n", index + 2)
            if newline == -1:
                break
            output.append("\n")
            index = newline + 1
        elif pair == "/*":
            block_depth = 1
            index += 2
        elif pair == "*/":
            raise ValueError("unmatched block-comment terminator")
        else:
            output.append(source[index])
            index += 1
    if block_depth:
        raise ValueError("unterminated block comment")
    return "".join(output)


def rust_tokens(source: str) -> list[str]:
    """Tokenize the intentionally tiny accepted Rust grammar, rejecting residue."""
    token_pattern = re.compile(r"\s+|::|[A-Za-z_][A-Za-z0-9_]*|[*!;]")
    tokens: list[str] = []
    position = 0
    while position < len(source):
        match = token_pattern.match(source, position)
        if match is None:
            excerpt = source[position : position + 20]
            raise ValueError(f"unexpected source near {excerpt!r}")
        token = match.group(0)
        if not token.isspace():
            tokens.append(token)
        position = match.end()
    return tokens


def main() -> int:
    errors: list[str] = []
    try:
        tokens = rust_tokens(without_comments(ALIAS_SOURCE.read_text(encoding="utf-8")))
        if tokens != EXPECTED_TOKENS:
            errors.append(
                "alias source tokens must be exactly "
                f"{EXPECTED_TOKENS!r}; found {tokens!r}"
            )
    except (OSError, ValueError) as error:
        errors.append(f"cannot verify alias source: {error}")

    try:
        manifest = tomllib.loads(ALIAS_MANIFEST.read_text(encoding="utf-8"))
        package = manifest.get("package", {})
        dependency = manifest.get("dependencies", {}).get(CANONICAL_PACKAGE)
        if package.get("name") != "citygml":
            errors.append("alias package name must be 'citygml'")
        if package.get("version") != "0.1.0":
            errors.append("alias package version must be '0.1.0'")
        if not isinstance(dependency, dict):
            errors.append(f"missing table dependency on {CANONICAL_PACKAGE}")
        else:
            if dependency.get("version") != "=0.1.0":
                errors.append("canonical dependency must use version '=0.1.0'")
            if dependency.get("path") != "../openbim-citygml":
                errors.append("canonical dependency path must be '../openbim-citygml'")
            unexpected = set(dependency) - {"version", "path"}
            if unexpected:
                errors.append(f"canonical dependency has unexpected keys: {sorted(unexpected)}")
    except (OSError, tomllib.TOMLDecodeError) as error:
        errors.append(f"cannot verify alias manifest: {error}")

    if errors:
        for error in errors:
            print(f"alias purity error: {error}", file=sys.stderr)
        return 1
    print("alias purity: citygml is an exact-version pure re-export")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
