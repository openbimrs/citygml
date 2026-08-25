# OpenBIM.rs CityGML

[![CI](https://github.com/openbimrs/citygml/actions/workflows/ci.yml/badge.svg)](https://github.com/openbimrs/citygml/actions/workflows/ci.yml)
[![openbim-citygml](https://img.shields.io/crates/v/openbim-citygml.svg)](https://crates.io/crates/openbim-citygml)
[![citygml](https://img.shields.io/crates/v/citygml.svg)](https://crates.io/crates/citygml)
[![docs.rs](https://docs.rs/openbim-citygml/badge.svg)](https://docs.rs/openbim-citygml)
[![MSRV](https://img.shields.io/badge/MSRV-1.85-blue)](https://www.rust-lang.org)

This repository reserves package architecture for future OpenBIM.rs CityGML
work. Version 0.1.0 is deliberately a **reserved scaffold**, not a CityGML
implementation.

## Capability status

| Capability | Status in 0.1.0 |
| --- | --- |
| Canonical package and status constant | Available |
| Short-name package as an exact-version pure re-export | Available |
| CityGML conceptual data model | Not implemented |
| GML/XML parsing | Not implemented |
| GML/XML writing | Not implemented |
| Schema or business-rule validation | Not implemented |
| CityGML version/profile support | Not implemented |
| OGC conformance claims | None |

`PACKAGE_STATUS` is metadata describing this scaffold. Its presence must not be
interpreted as parser, writer, validation, schema-coverage, or conformance
functionality.

## Package architecture

| Package | Role |
| --- | --- |
| [`openbim-citygml`](openbim-citygml/) | Canonical package; currently only the reserved scaffold status |
| [`citygml`](citygml/) | Short-name compatibility package that purely re-exports the exact canonical version |

Dependency direction is one way:

```text
citygml  --->  openbim-citygml
  alias          canonical scaffold
```

The alias defines no independent API. Do not depend on both packages directly.

## Install

Choose one package name:

```bash
cargo add openbim-citygml
# or
cargo add citygml
```

Version 0.1.0 reserves both package names as an explicit scaffold.

## Official references

The authoritative entry point is the
[OGC CityGML standard page](https://www.ogc.org/standards/citygml/). The approved
CityGML 3.0 GML encoding is
[OGC 21-006r2, Part 2](https://docs.ogc.org/is/21-006r2/21-006r2.html).
These links are references only. No OGC standard text, schema, example corpus, or
other standards artifact is copied or vendored in this repository.

## Development

Rust 1.85 or newer is required. Run the same gate as CI:

```bash
./scripts/gate.sh
```

The gate checks formatting, build, tests, Clippy, documentation, alias purity,
and complete package archives for both crates. See
[`docs/architecture.md`](docs/architecture.md) for the boundary and release
ordering.

## License

MIT — see [`LICENSE`](LICENSE).
