# Alias package instructions

This package is a compatibility alias only.

- `src/lib.rs` may contain comments and exactly
  `pub use openbim_citygml::*;`; nothing else.
- Keep the dependency version exactly equal to this package version with `=`.
- Define no types, traits, functions, constants, modules, macros, features, or
  behavior here.
- Keep `AGENTS.md` and `PLAN.md` outside the package archive.

Run `../scripts/check-alias-purity.sh` after every change.
