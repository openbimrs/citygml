# Contributing

Thank you for helping build OpenBIM.rs CityGML support.

## Before changing code

Read the root and nearest nested `AGENTS.md`. Version 0.1.0 is a reserved
scaffold; proposals for parsing, writing, models, or validation must include a
reviewable scope and executable evidence before capability documentation changes.

Do not copy OGC standard text, schemas, or example corpora into the repository
without an explicit, verified redistribution grant.

## Local verification

Use Rust 1.85 or newer and run:

```bash
./scripts/gate.sh
```

Keep `citygml/src/lib.rs` a pure re-export and keep its canonical dependency
pinned with an exact `=` version. Add entries to `CHANGELOG.md` for user-visible
changes.
