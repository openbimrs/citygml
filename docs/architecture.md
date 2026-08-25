# Architecture

## Repository role

This repository is an independently buildable home for two CityGML package
names. Release 0.1.0 establishes metadata and package boundaries only; it does
not implement CityGML.

## Dependency direction

```text
citygml  --->  openbim-citygml
(alias)         (canonical scaffold)
```

`openbim-citygml` owns any future public API. In 0.1.0 that API is limited to
`PACKAGE_STATUS`. `citygml` is a compatibility name and must never define its
own type, function, constant, module, trait, macro, or behavior. Its dependency
uses `version = "=0.1.0"` so canonical and alias APIs cannot drift.

The semantic checker strips Rust comments, tokenizes the remaining alias source,
and requires precisely the canonical glob re-export. It also verifies the exact
manifest dependency. The shell wrapper makes that check convenient for CI and
the full gate.

## Capability boundary

No data model, parser, writer, serializer, validator, schema binding, version
recognizer, profile implementation, or conformance suite exists. Those are
future design decisions, not latent capabilities of this scaffold.

Any future implementation should begin with an explicit design covering:

- supported CityGML standard part and version;
- conceptual-model versus encoding responsibilities;
- preservation and resource-limit behavior;
- validation and conformance terminology;
- licensed provenance for test inputs.

## Standards artifacts

The repository links to official OGC pages but contains no normative text,
schemas, generated bindings, or official example corpus. The root `.gitignore`
keeps a local `references/` directory untracked. Redistribution rights and
provenance must be verified before any external artifact is committed or packed.

## Packaging order

The canonical package must be packaged and, if separately authorized, published
before the alias because Cargo verifies registry dependencies while packaging.
Before the canonical 0.1.0 exists on crates.io, the gate fully packages
`openbim-citygml` and runs `cargo package --list` for `citygml`. Workspace build,
test, Clippy, rustdoc, and alias-purity checks still cover both crates locally.

Publication and pushing are intentionally outside the gate.
