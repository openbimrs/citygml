# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.1] - 2026-10-28

### Changed

- **Licence:** `AGPL-3.0-or-later OR LicenseRef-Commercial`; the last
  published release (0.1.0) was `MIT`. A commercial licence is available from
  the copyright holder named in `NOTICE`. See `LICENSING.md`. The crates ship
  `LICENSE`, `NOTICE` and `LICENSES/LicenseRef-Commercial.txt`.
- Raise MSRV to Rust 1.99.
- Relicensed repository-authored work from MIT to `AGPL-3.0-or-later`; historical releases remain under their published MIT terms, and third-party material retains its own terms.
- The release gate packages both crates together and checks the `citygml`
  alias against the candidate canonical package.
- Alias purity now fails closed over Cargo dependency, feature, target, build,
  and source shape, with 19 mutation probes and exact package allowlists.
- CI now pins its runner and action revisions; local fallback targets are unique
  per gate invocation.

## [0.1.0] - 2026-08-25

### Added

- Reserved canonical `openbim-citygml` scaffold with an explicit status constant.
- Exact-version, pure-re-export `citygml` alias package.
- Standalone CI, package, documentation, and mutation-verified alias-purity gates.

[0.1.1]: https://crates.io/crates/openbim-citygml/0.1.1
[0.1.0]: https://crates.io/crates/openbim-citygml/0.1.0
