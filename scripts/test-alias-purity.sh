#!/usr/bin/env bash
# Prove the semantic alias gate rejects implementation and version drift.
set -euo pipefail

cd "$(dirname "$0")/.."

alias_name="citygml"
alias_lib="$alias_name/src/lib.rs"
alias_manifest="$alias_name/Cargo.toml"
checker="scripts/check-alias-purity.sh"
tmp="$(mktemp -d "${TMPDIR:-/tmp}/citygml-alias-mutations.XXXXXX")"
cp "$alias_lib" "$tmp/lib.rs"
cp "$alias_manifest" "$tmp/Cargo.toml"

restore() {
    cp "$tmp/lib.rs" "$alias_lib"
    cp "$tmp/Cargo.toml" "$alias_manifest"
    rm -rf "$tmp"
}
trap restore EXIT HUP INT TERM

expect_rejection() {
    local mutation="$1"
    if "$checker" >"$tmp/$mutation.log" 2>&1; then
        printf 'alias mutation was not rejected: %s
' "$mutation" >&2
        return 1
    fi
    printf '%s: killed
' "$mutation"
}

"$checker"
printf '
pub struct DivergentAliasType;
' >> "$alias_lib"
expect_rejection independent-type
cp "$tmp/lib.rs" "$alias_lib"

python3 -c 'from pathlib import Path; import sys; p=Path(sys.argv[1]); s=p.read_text(); old="version = \"=0.1.0\""; assert s.count(old)==1; p.write_text(s.replace(old, "version = \"0.1.0\""))' "$alias_manifest"
expect_rejection loose-version

cp "$tmp/lib.rs" "$alias_lib"
cp "$tmp/Cargo.toml" "$alias_manifest"
"$checker"
cmp -s "$tmp/lib.rs" "$alias_lib"
cmp -s "$tmp/Cargo.toml" "$alias_manifest"

trap - EXIT HUP INT TERM
rm -rf "$tmp"
printf 'alias mutation probes: 2/2 killed; sources restored
'
