# Repository instructions

This is the standalone canonical repository for OpenBIM.rs CityGML packages.
Version 0.1.0 is a reserved scaffold, not an implementation.

## Directories

- `openbim-citygml/` — canonical scaffold package.
- `citygml/` — exact-version pure-re-export alias package.
- `docs/` — architectural boundaries and contributor context.
- `scripts/` — the authoritative gate and alias-purity checks.

## Invariants

1. Rust edition is 2021 and MSRV is 1.85.
2. The canonical crate makes no parser, writer, model, validation, or conformance claim.
3. The alias source contains only `pub use openbim_citygml::*;` apart from comments.
4. The alias dependency is pinned to exactly the canonical package version.
5. Normative standards, schemas, and official examples stay out of the repository.
6. `./scripts/gate.sh` must pass before committing.
