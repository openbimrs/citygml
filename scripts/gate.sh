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
./scripts/test-alias-purity.sh
cargo package -p openbim-citygml
cargo package -p citygml
