# OpenBIM.rs CityGML

Canonical repository: <https://github.com/openbimrs/citygml>

Read `AGENTS.md` and the nearest nested `AGENTS.md` before edits. This repository
contains a reserved package scaffold only. Do not describe planned CityGML
features as implemented.

## Verification

`./scripts/gate.sh` is authoritative locally and in CI. It uses command exit
codes and includes a semantic purity check for the short-name alias.

## Conventions

- Rust 2021; MSRV 1.85; AGPL-3.0-or-later; pure Rust.
- Keep `citygml` an exact-version pure re-export of `openbim-citygml`.
- Do not vendor OGC standards, schemas, or reference corpora.
- Update capability tables only when executable implementation and tests exist.
- Do not push or publish without explicit authorization.
