#!/usr/bin/env bash
# Complete standalone verification gate for openbimrs/citygml.
set -euo pipefail

cd "$(dirname "$0")/.."

# Concurrent jobs must not share mutable Cargo target artifacts. Respect a
# caller-provided target directory; otherwise allocate a unique host cache.
if [[ -z "${CARGO_TARGET_DIR:-}" && -d /mnt/backup/build-cache ]]; then
  export CARGO_TARGET_DIR="$(mktemp -d /mnt/backup/build-cache/openbim-citygml-target.XXXXXX)"
  trap 'rm -rf "$CARGO_TARGET_DIR"' EXIT
fi

cargo fmt --all -- --check
cargo build --workspace --all-targets
cargo test --workspace --all-features
cargo clippy --workspace --all-targets --all-features -- -D warnings
RUSTDOCFLAGS="-D warnings" cargo doc --workspace --all-features --no-deps
./scripts/check-alias-purity.sh
./scripts/test-alias-purity.sh
python3 scripts/check-package-contents.py
cargo package --locked -p openbim-citygml
cargo package --locked -p citygml
