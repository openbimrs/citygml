#!/usr/bin/env bash
# Complete standalone verification gate for openbimrs/citygml.
set -euo pipefail

cd "$(dirname "$0")/.."

# Concurrent jobs must not share mutable Cargo target artifacts. Respect a
# caller-provided target directory; otherwise use the host build cache when it exists.
if [[ -z "${CARGO_TARGET_DIR:-}" && -d /mnt/backup/build-cache ]]; then
  export CARGO_TARGET_DIR=/mnt/backup/build-cache/openbim-citygml-target
fi

cargo fmt --all -- --check
cargo build --workspace --all-targets
cargo test --workspace --all-features
cargo clippy --workspace --all-targets --all-features -- -D warnings
RUSTDOCFLAGS="-D warnings" cargo doc --workspace --all-features --no-deps
./scripts/check-alias-purity.sh
cargo package --allow-dirty -p openbim-citygml
# Cargo cannot verify a registry dependency until the canonical package exists.
# Until first publication, inspect the alias archive file set after the workspace
# and semantic purity checks above have passed.
cargo package --allow-dirty --list -p citygml
