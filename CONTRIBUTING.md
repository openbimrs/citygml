# Contributing

Thank you for helping build OpenBIM.rs CityGML support.

## Before changing code

Read the root and nearest nested `AGENTS.md`. Version 0.1.1 is a reserved
scaffold; proposals for parsing, writing, models, or validation must include a
reviewable scope and executable evidence before capability documentation changes.

Do not copy OGC standard text, schemas, or example corpora into the repository
without an explicit, verified redistribution grant.

## Local verification

Use Rust 1.99 or newer and run:

```bash
./scripts/gate.sh
```

Keep `citygml/src/lib.rs` a pure re-export and keep its canonical dependency
pinned with an exact `=` version. Add entries to `CHANGELOG.md` for user-visible
changes.

## Releasing

Releases are published by `.github/workflows/release.yml` through crates.io
trusted publishing; there is no token and no manual `cargo publish`. Bump the
version(s), date the `CHANGELOG.md` section, merge to `main`, then push an
annotated tag `v<version>` on that commit. The workflow checks that the tag is
on `main` and matches the manifest and changelog, runs `scripts/gate.sh`, then
publishes `openbim-citygml` and then its exact-version alias `citygml` in the `crates.io` environment. Already-published versions
are skipped, so a failed run can be re-run. crates.io trusts exactly the
repository, the file name `release.yml` and the environment `crates.io`; keep
all three. Run the workflow by hand with a tag name to rehearse (gate only).

## Licensing contributions

OpenBIM.rs is dual-licensed: `AGPL-3.0-or-later OR LicenseRef-Commercial`
(see [`LICENSING.md`](LICENSING.md)). To keep the commercial option
possible, every contribution is accepted on the following terms, which you
agree to by submitting it (a pull request, patch, issue attachment or any
other material intended for inclusion):

1. **Licence to the project.** Your contribution is licensed under
   `AGPL-3.0-or-later`.
2. **Licence to the copyright holder.** You also grant the copyright holder
   named in [`NOTICE`](NOTICE) a perpetual, worldwide, non-exclusive,
   royalty-free, irrevocable licence to use, reproduce, modify, distribute,
   sublicense and relicense your contribution, including under proprietary
   or commercial terms, as part of OpenBIM.rs or works derived from it.
3. **You keep your copyright.** These terms grant a licence; they do not
   transfer ownership.
4. **You have the right to grant this.** The contribution is your own work,
   or you have permission to submit it on these terms (for example from
   your employer). Identify third-party material, keep its licence,
   attribution and provenance, and do not submit third-party material whose
   licence does not allow these terms.
5. **Patents.** You grant the same parties a licence under any patent claims
   you can license that your contribution necessarily infringes, on the terms
   of section 11 of the AGPL.

If you cannot agree to these terms, say so in the issue or pull request
before submitting; the contribution can then not be merged.
