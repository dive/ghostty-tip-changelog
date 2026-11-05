> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: November 5, 2026 at 10:14 UTC.

## November 4, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/41923292341), [2](https://github.com/ghostty-org/ghostty/actions/runs/41911262211), [3](https://github.com/ghostty-org/ghostty/actions/runs/41887613577)  
Summary: 3 runs • 32 commits • 3 authors

### Changes

- [`def58d3`](https://github.com/ghostty-org/ghostty/commit/def58d386bb1c626acd338f75ad2959b13d738b6) cli: flush plain color list output ([@12ya](https://github.com/12ya))
  ```text
  Flush stdout before returning so plain and piped color listings include all entries instead of ending mid-line
  ```
- [`02cf8a6`](https://github.com/ghostty-org/ghostty/commit/02cf8a6a2fbac49a7cf661b5eebfe57b98f21b4b) libghostty-vt: zero and freeze the structs used for callbacks ([@mitchellh](https://github.com/mitchellh))
  ```text
  **This breaks the C ABI. This is all on purpose to stabilize the ABI to
  prep for a 1.0 stable libghostty-vt release.**
  
  Make sure that all structs sent via a callback are zeroed and that their
  size is frozen. If we change structs we can introduce new callback types
  instead of changing the prior callback signatures.
  ```
- [`9e0d83c`](https://github.com/ghostty-org/ghostty/commit/9e0d83ceea1a268bbe6c8abefa584782e8e5d321) libghostty-vt: drop the size field from GridRef and Selection ([@mitchellh](https://github.com/mitchellh))
  ````text
  **This breaks the C ABI. This is all on purpose to stabilize the ABI to
  prep for a 1.0 stable libghostty-vt release.**
  
  `GhosttyGridRef` and `GhosttySelection` are now unsized/frozen structs.
  The size was never used and they're embedded types so its really a
  parent type concern.
  
  If either type ever needs to hold more, that will be a new type rather
  than a change to these. Callers now zero-initialize them instead of
  using `GHOSTTY_INIT_SIZED`:
  
  ```c
  GhosttySelection selection = {0};
  ```
  
  The header docs for both types were rewritten. They now explain where a
  grid reference comes from, how long it stays valid, that `x` and `y` are
  not screen coordinates, and how selection direction works, with a usage
  example for each. The examples drop `GHOSTTY_INIT_SIZED` for these
  types.
  ````
- [`a447ff7`](https://github.com/ghostty-org/ghostty/commit/a447ff7d86ecf6c2e52779c0768e476d15d9e914) libghostty-vt: make GhosttyStyle a frozen 16-byte struct ([@mitchellh](https://github.com/mitchellh))
- [`49fbdaf`](https://github.com/ghostty-org/ghostty/commit/49fbdafd1df45dfc7e5e8034be03f3d0b89e50a2) libghostty-vt: set formatter options by key ([@mitchellh](https://github.com/mitchellh))
- [`742fc2f`](https://github.com/ghostty-org/ghostty/commit/742fc2f2e20f2a6f1a8db43b1268db3d85161360) libghostty-vt: one sized-struct rule for every sized struct ([@mitchellh](https://github.com/mitchellh))
- [`29bf7aa`](https://github.com/ghostty-org/ghostty/commit/29bf7aa9b4d5f8f464d9eb5d1809f9433759829d) cli: flush plain color list output ([#15073](https://github.com/ghostty-org/ghostty/issues/15073)) ([@jcollie](https://github.com/jcollie))
  ```text
  Flush stdout before returning so plain and piped color listings include
  all entries instead of ending mid-line
  
  `ghostty +list-colors --plain`
  
  <img width="1615" height="419" alt="image"
  src="https://github.com/user-attachments/assets/7d25e9b7-f22f-43df-9caa-bf343f909d14"
  />
  ```
- [`86aef72`](https://github.com/ghostty-org/ghostty/commit/86aef72a2c8e67c780867de2378b2fc4d6dcd9ca) libghostty-vt: zero and freeze the structs used for callbacks ([#15074](https://github.com/ghostty-org/ghostty/issues/15074)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  **This breaks the C ABI. This is all on purpose to stabilize the ABI to
  prep for a 1.0 stable libghostty-vt release.**
  
  A minor chage. Make sure that all structs sent via a callback are zeroed
  and that their size is frozen. If we change structs we can introduce new
  callback types instead of changing the prior callback signatures.
  ```
- [`f5a1a0f`](https://github.com/ghostty-org/ghostty/commit/f5a1a0fedd8762d490bc2951dc4b63a0f1b030e0) libghostty-vt: frozen value structs and one sized-struct rule ([#15075](https://github.com/ghostty-org/ghostty/issues/15075)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  **This breaks the C ABI. This is all on purpose to stabilize the ABI to
  prep for a 1.0 stable libghostty-vt release.**
  
  This adds a bunch of helpers and unifies our handling of sized structs
  throughout the libghostty C API. Previously, we had ~20 types with sized
  structs but only actually checked 2 of them! This PR also freezes a
  couple sized structs that didn't need a size.
  
  Along the way, the formatter's three option structs are gone.
  `ghostty_formatter_terminal_new` takes no options and we now use
  `ghostty_formatter_set` and `_get` like others.
  
  Also updated docs: a new "Sized Structs" section in vt.h explains the
  rule, and every sized struct links to it.
  
  **AI usage:** I implemented the helpers and had Opus mechanically verify
  and update all our call sites.
  ```
- [`6581a59`](https://github.com/ghostty-org/ghostty/commit/6581a593c68798cdd2c2cb77b7558747c65a0987) ci: add a release workflow for libghostty-vt ([@mitchellh](https://github.com/mitchellh))
- [`1a2cf06`](https://github.com/ghostty-org/ghostty/commit/1a2cf06dd1284f84bb28d87dbc3a055e97c93f42) docs: add a packaging guide for libghostty-vt ([@mitchellh](https://github.com/mitchellh))
  ```text
  libghostty-vt is about to get its own tagged releases, and distros
  need to be able to package it from the docs alone. PACKAGING.md only
  covered the app, with a short WebAssembly section for the library.
  
  PACKAGING-LIBGHOSTTY.md is a new, self-contained guide for packaging
  the library. It has its own accuracy warning, Zig version and minisign
  key so someone reading the library tarball never needs PACKAGING.md.
  It covers the release files on release.files.ghostty.org, the offline
  build with deps/libghostty-vt.txt, the installed files, the build
  options that matter for the library (including the only two -fsys
  options it uses, simdutf and highway), the 0.x rebuild rule and
  SONAME, package naming, pkg-config and CMake use, the third-party
  manifest and licenses, a smoke test, platform tiers, and the
  WebAssembly notes moved over from PACKAGING.md.
  
  It also calls out that the archive GitHub generates for a vt- tag is
  not a source tarball. It has no LIB_VERSION file, so `zig build` in it
  builds the app, not the library.
  
  PACKAGING.md stays the app's guide. It points library packagers at
  the new file, and its Zig version section now points at
  minimum_zig_version in build.zig.zon instead of a required_zig
  constant that no longer exists (and an example of Zig 0.14.0).
  
  The library tarball ships PACKAGING-LIBGHOSTTY.md and drops
  PACKAGING.md. dist/cmake/README.md now fetches the release tarball
  instead of main and links to the new guide instead of repeating it.
  vt.h replaces its "work in progress" warnings with the actual
  stability policy and an example runtime version check.
  ```
- [`281d341`](https://github.com/ghostty-org/ghostty/commit/281d34115fc300b4be121c01487550464d0eed9f) build: don't install the man page placeholder for libghostty-vt ([@mitchellh](https://github.com/mitchellh))
- [`e95bed6`](https://github.com/ghostty-org/ghostty/commit/e95bed63330cc921f3cf2fe3d14e024396b09d43) libghostty: release workflow and packaging guide for libghostty-vt ([#15076](https://github.com/ghostty-org/ghostty/issues/15076)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds:
  
  - Release workflow for libghostty-vt via GitHub actions triggerd by a
  `vt-X.Y.Z` tag.
  - `PACKAGING-LIBGHOSTTY.md`, a packaging guide for libghostty-vt, copy
  and pasted and reworked for libghostty from PACKAGING.md
  
  **AI usage:** Opus wrote the YAML, I did the markdown.
  ```
- [`8f7fc00`](https://github.com/ghostty-org/ghostty/commit/8f7fc00c3da2ac410d73256fc34ecce81ea49344) libghostty-vt: test that the C headers match the Zig types ([@mitchellh](https://github.com/mitchellh))
  ```text
  This continues/completes the work @jcollie started.
  
  All our C headers for libghostty and our Zig extern types are maintained
  by hand. This commit adds automated tests to verify that they are always
  matching.
  
  The test translates `ghostty/vt.h` with translate-c and walks the type
  registry in `src/terminal/c/types.zig` (the same list that produces the
  `ghostty_type_json()` manifest). For every registered type it checks:
  
    - Structs and unions: size, alignment, and every field's name,
      position, offset, and size.
    - Enums: every Zig value is a C enumerator with the same number,
      every C enumerator maps back to a Zig value, and the `_MAX_VALUE`
      sentinel is present and equal to `INT_MAX`.
    - Packed types and aliases: the same integer type.
    - Opaque handles: a pointer to an incomplete C struct.
  
  A second test runs the other way and checks that every struct, union,
  enum, and opaque handle in the headers is in the registry. A new header
  type that isn't registered fails the build, so coverage stays complete
  without any manual work.
  
  This did find a couple small mismatches that were fixed:
  `GhosttyModeReportState` (u8) and `GhosttySgrUnderline` (u3). Neither
  is an ABI bug since both cross the C API as a C int but the metadata
  didn't match.
  ```
- [`942e353`](https://github.com/ghostty-org/ghostty/commit/942e353465eb80b0bdb63bfb116d95fcb0d8edbf) libghostty-vt: test that the C headers match the Zig types ([#15071](https://github.com/ghostty-org/ghostty/issues/15071)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This continues/completes the work @jcollie started.
  
  All our C headers for libghostty and our Zig extern types are maintained
  by hand. This commit adds automated tests to verify that they are always
  matching.
  
  The test translates `ghostty/vt.h` with translate-c and walks the type
  registry in `src/terminal/c/types.zig` (the same list that produces the
  `ghostty_type_json()` manifest). For every registered type it checks:
  
  - Structs and unions: size, alignment, and every field's name, position,
  offset, and size.
  - Enums: every Zig value is a C enumerator with the same number, every C
  enumerator maps back to a Zig value, and the `_MAX_VALUE` sentinel is
  present and equal to `INT_MAX`.
    - Packed types and aliases: the same integer type.
    - Opaque handles: a pointer to an incomplete C struct.
  
  A second test runs the other way and checks that every struct, union,
  enum, and opaque handle in the headers is in the registry. A new header
  type that isn't registered fails the build, so coverage stays complete
  without any manual work.
  
  This did find a couple small mismatches that were fixed:
  `GhosttyModeReportState` (u8) and `GhosttySgrUnderline` (u3). Neither is
  an ABI bug since both cross the C API as a C int but the metadata didn't
  match.
  
  **AI usage:** Fable planned, Opus written (code only), I reviewed and
  modified the code rather significantly and wrote all the english myself.
  ```
- [`1830cd2`](https://github.com/ghostty-org/ghostty/commit/1830cd2502274a2ba0a1c03341cde3e063f57019) libghostty: derive shared library version metadata from lib_version ([@mitchellh](https://github.com/mitchellh))
  ```text
  Zig already names the shared library from `lib_version` on Linux, the
  BSDs and Windows. For 0.1.0 that is libghostty-vt.so.0.1.0 with SONAME
  libghostty-vt.so.0, plus .so.0 and .so symlinks, and ghostty-vt.dll.
  
  macOS metadata didn't follow this though. The Apple ld path hardcoded the
  install name `@rpath/libghostty-vt.dylib` and compatibility version
  1.0.0, and CMake had 0.1.0 baked into every library name.
  
  All of the version metadata is now derived from `SharedVersion` in
  GhosttyLibVt.zig, which also documents the policy.
  
  For 0.1.0 a dylib gets:
  
    - install name @rpath/libghostty-vt.0.dylib
    - compatibility version 0.1.0 (0.<minor>.0 before 1.0, <major>.0.0
      after)
    - current version 0.1.0
  
  Before 1.0 there is no ABI promise. Any minor release may break the
  ABI, and packagers handle that by rebuilding dependents on a minor bump.
  That is documentation, not build logic, so the file names stay Zig's.
  
  dyld doesn't actually enforce the compatibility version. On macOS 27 a
  client linked against a 0.1.0 dylib happily loads one marked 0.2.0 and
  the other way around, even with an old deployment target.
  
  CMake now reads the version from LIB_VERSION or build.zig instead of
  hardcoding 0.1.0, and derives the real name and SONAME from it. This
  also fixes the installed CMake package config on macOS, which said
  `IMPORTED_SONAME "GHOSTTY_VT_SONAME@"` because configure_file read
  "@rpath/@" as a variable named "rpath/".
  
  CI now checks the names against lib_version instead of a literal.
  test.yml checks the SONAME and symlinks, check-apple-libghostty-vt.nu
  checks the install name and both versions, release-tip runs that check
  on the dylib it builds, and the nix shared-link test checks the library
  name the test program records.
  ```
- [`8edb49e`](https://github.com/ghostty-org/ghostty/commit/8edb49e386acbcaa2ab6141a8e5285c2a03f4f57) libghostty: version the lib-vt tarball and vt- tags from lib_version ([@mitchellh](https://github.com/mitchellh))
  ```text
  `zig build dist -Demit-lib-vt` now names the tarball after the library
  version instead of the app version, for example
  libghostty-vt-0.1.0-dev.tar.gz, and writes a LIB_VERSION file into it in
  place of VERSION. The app tarball is unchanged.
  ```
- [`184b01a`](https://github.com/ghostty-org/ghostty/commit/184b01ab32c67b6accea14aa22ce8ed2c0ed7733) libghostty: install a CMake package config and fix lib-vt packaging defaults ([@mitchellh](https://github.com/mitchellh))
- [`7b06c05`](https://github.com/ghostty-org/ghostty/commit/7b06c054155d26f789d79a6e3ee0dc4b6e76f924) libghostty: record the final install paths in the lib-vt .pc and CMake files ([@mitchellh](https://github.com/mitchellh))
  ```text
  Distros install with `DESTDIR=/stage zig build --prefix /usr`, often
  with `--prefix-lib-dir lib64`. Zig 0.17 joins DESTDIR into every install
  path it gives the build, so both .pc files said `prefix=/stage/usr`.
  They also hardcoded `libdir=${prefix}/lib` and `includedir=${prefix}/include`,
  the CMake config hardcoded lib/, include/ and bin/, and all four files
  were installed under lib/ even when the libraries went to lib64/.
  
  For that install the .pc files now start with:
  
      prefix=/usr
      includedir=${prefix}/include
      libdir=${prefix}/lib64
  
  and the .pc and CMake files are installed to lib64/pkgconfig/ and
  lib64/cmake/ghostty-vt/. The default layout is unchanged.
  ```
- [`3a1457c`](https://github.com/ghostty-org/ghostty/commit/3a1457c34e41d98cac86582c2cbb5360b3ced2ff) ci: make the lib-vt leak checks able to fail ([@mitchellh](https://github.com/mitchellh))
- [`f5dcef0`](https://github.com/ghostty-org/ghostty/commit/f5dcef0453e1dd65f080577e07c6d9163dab218f) libghostty: add a version header and ghostty_version() ([@mitchellh](https://github.com/mitchellh))
  ```text
  libghostty-vt had no way to check its version from C at compile time,
  and the only runtime answer was ghostty_build_info(), which returns a
  string that isn't null-terminated. Consumers like Neovim's
  FindGhostty.cmake and distro packaging want both.
  
  `include/ghostty/vt/version.h` is a new committed header with
  GHOSTTY_VT_VERSION_MAJOR, _MINOR, _PATCH, a GHOSTTY_VT_VERSION string
  and GHOSTTY_VT_VERSION_AT_LEAST(maj, min, pat). vt.h includes it. It
  contains only macros and includes nothing, so build systems can read it
  as plain text. It is committed rather than generated so the tarball,
  Doxygen and anyone reading the headers all see the same file.
  
  The header only carries the release number, "0.1.0", never "-dev".
  A build from a vt- tag or a LIB_VERSION tarball drops the pre-release
  part, so a header with "-dev" in it would be wrong on exactly the
  builds we release.
  
  `ghostty_version()` returns the full version of the loaded library as
  a static null-terminated string, for example "0.1.0-dev+9a018f5cc". It
  is the same text as GHOSTTY_BUILD_INFO_VERSION_STRING. There is no
  separate function for the numbers since ghostty_build_info() already
  returns them.
  
  A new test, ghostty-vt-version-h-test, runs as part of test-lib-vt and
  fails if the header's numbers disagree with the version the library is
  built with, so a release bump has to update both. It reads the header
  as text the same way CMake would.
  
  The Version docs explain the 0.x ABI policy and why a runtime check
  matters before 1.0: every 0.x release shares the libghostty-vt.0
  library name, so the system happily loads a 0.2 library for a program
  compiled against 0.1. The c-vt-build-info example now shows both a
  compile-time check and a runtime compatibility check.
  ```
- [`ac1feec`](https://github.com/ghostty-org/ghostty/commit/ac1feec8338c4ef0ae8cd596fd43130577f3edf2) libghostty: link the lib-vt dylib with Zig when Ghostty is a dependency ([@mitchellh](https://github.com/mitchellh))
  ```text
  Zig projects that depend on Ghostty and link `dep.artifact("ghostty-vt")`
  panicked at configure time on macOS with `unable to find artifact
  "ghostty-vt"`. Every shared-library `c-vt-*` example hit this. Linux
  was unaffected.
  
  On a macOS host with the SDK, `initShared` links the dylib with Apple's
  linker in a Run step and installs it with `addInstallFileWithDir`, so
  there is no Compile step for `dep.artifact` to find.
  
  When Ghostty is a dependency, the shared library is now an ordinary
  Compile step installed with `addInstallArtifact`. The dependent links
  it into its own build, so the compatibility version and Apple
  distribution load commands from the native link don't matter there.
  The install name is still `@rpath/libghostty-vt.0.dylib`.
  
  Packaging builds (`-Demit-lib-vt`) keep the native link.
  ```
- [`97a5653`](https://github.com/ghostty-org/ghostty/commit/97a5653d323a730e4816936ed62520205f1007ae) pkg/wuffs: give the tests their own module ([@mitchellh](https://github.com/mitchellh))
  ```text
  The wuffs tests embed sample images from the pixels package. They added
  those imports to the `wuffs` module itself, which is also the module
  Ghostty imports, so every build that used wuffs carried eight test
  images in its module graph. Nothing compiled them in, but anything that
  reads the graph, such as a report of which packages end up in
  libghostty-vt, counted pixels as part of the library.
  
  The tests now build from a separate module with the same root file and
  the same `wuffs_c` import, plus the images.
  ```
- [`5b500d1`](https://github.com/ghostty-org/ghostty/commit/5b500d1433b61bc612409f82d6c8e35110ede62c) libghostty: generate the lib-vt dependency list and third-party manifest ([@mitchellh](https://github.com/mitchellh))
  ```text
  Packagers building libghostty-vt offline had to fetch all 37 Ghostty
  dependencies, including GTK and font packages the library never touches,
  and had no list of the third-party code inside the library or its
  licenses.
  
  check-zig-cache.sh now also generates two files:
  
    - build.zig.zon.lib-vt.txt, the 9 packages a `-Demit-lib-vt` build
      needs, in the same format as build.zig.zon.txt.
    - build.zig.zon.lib-vt.third-party.json, every third-party project in
      that build with its version, commit, URL, license, and whether its
      code is linked into the library or only used by the build.
  
  Neither file is written by hand. gen-lib-vt-deps.sh starts from an empty
  package directory and runs `zig build lib-vt-packages --system` for each
  supported target, fetching whatever Zig reports missing until the build
  runs. That keeps packages Zig requires even though the library doesn't
  use them, and leaves out lazy packages the library never asks for.
  
  The new `lib-vt-packages` step, defined only with `-Demit-lib-vt`, finds
  what is linked by walking the library's module graph: imports, C
  sources, include directories and linked libraries. It also reads every
  package's build.zig.zon for its version. The walk caught translate_c,
  whose helper modules are imported by every translated header.
  
  Licenses can't be derived, so each build.zig.zon in this repository now
  describes the third-party code it brings in, next to its URLs:
  
      .third_party = .{
          .{ .name = "wuffs", .license = "Apache-2.0 OR MIT", .version = "0.4.0-alpha.10" },
      },
  
  Zig and zon2nix ignore unknown top-level fields, so this changes neither
  the build nor the other generated files. Generation fails with a message
  saying what to fix when a package has no entry, an entry names a removed
  package, a linked package has no version, or vendored code is linked
  without an entry.
  
  fetch-zig-cache.sh takes an optional list, so packagers can fetch only
  what the library needs:
  
      ZIG_GLOBAL_CACHE_DIR=/tmp/offline-cache \
        ./nix/build-support/fetch-zig-cache.sh build.zig.zon.lib-vt.txt
  
  It also no longer uses `zig fetch`. In Zig 0.17, `zig fetch <url>` only
  stores p/<hash>.tar.gz, which `--system` can't read, so the script was
  broken for offline builds. It now writes a throwaway package that
  depends on each URL and runs `zig build --fetch` on it, which unpacks
  every package into p/<hash>.
  
  The offline build needs a fresh global cache too. Zig 0.17 hits
  "reached unreachable code" when a lazy package is missing from the
  `--system` directory but its tarball is in the global cache.
  ```
- [`4f2139a`](https://github.com/ghostty-org/ghostty/commit/4f2139ab4d769e37bab77ea767e398782ac19021) ci: build and test libghostty-vt offline from its dependency list ([@mitchellh](https://github.com/mitchellh))
  ```text
  The new test-lib-vt-offline job fetches only build.zig.zon.lib-vt.txt
  into an empty directory, then builds libghostty-vt and runs test-lib-vt
  with `--system` pointed at it and an empty global cache. If the list is
  missing a package, the job fails instead of the build quietly finding or
  downloading it somewhere else.
  ```
- [`2eda578`](https://github.com/ghostty-org/ghostty/commit/2eda578e784d2c46fd682f5fee55d4b3206448bf) libghostty: ship simdutf's license texts and take its version from pkg/simdutf ([@mitchellh](https://github.com/mitchellh))
  ```text
  The simdutf sources vendored in pkg/simdutf/vendor are compiled into
  libghostty-vt, but the repository had no copy of simdutf's licenses, so
  neither the source tarball nor anything built from it did either. Both of
  simdutf's licenses require shipping their text. LICENSE-APACHE and
  LICENSE-MIT from simdutf v9.0.0 now sit next to the sources. simdutf can
  be used under either one, matching the "Apache-2.0 OR MIT" in the
  third-party manifest.
  
  pkg/simdutf/build.zig.zon still said 5.2.8, though the vendored
  simdutf.h says 9.0.0. It now says 9.0.0, and vendored code takes its
  version from the build.zig.zon that holds it, so the .third_party entry
  no longer repeats it. As with fetched packages, gen-lib-vt-deps.sh
  rejects an entry that sets a second version. The generated files are
  unchanged.
  ```
- [`3de7129`](https://github.com/ghostty-org/ghostty/commit/3de71293034969aaa09ad6f19ee53a9d23087403) build: move the generated dependency files into deps/ ([@mitchellh](https://github.com/mitchellh))
- [`9fc62a9`](https://github.com/ghostty-org/ghostty/commit/9fc62a98cc765f2c341d317f2ee684ebb9584237) libghostty: prepare libghostty-vt for tagged releases ([#15069](https://github.com/ghostty-org/ghostty/issues/15069)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This is the first batch of work toward tagged libghostty-vt releases.
  This PR:
  
  - Library gets its own version via `lib_version` in `build.zig`.
  - Tags are processed as `vt-X.Y.Z`, and builds read this.
  - Tarball builds are named `libghostty-vt-X.Y.Z.tar.gz`
  - Tarball contains a `LIB_VERSION` file so a plain `zig build` uses that
  (similar to our app's `VERSION` file in the tarball)
  - The shared libraries SONAME is set properly
  - The macOS dylib install name and version metadata are set properly
  - CMake derives version from `lib_version`, the version is no longer
  hardcoded
  - The install layout is now more appropriate for packages:
    * `.pc` files under `lib/pkgconfig`
    * Cmake under `lib/cmake/ghostty-vt`
  - A new `version.h` header with macros and functions to help embedders
  - Generated dependency list including licensing information packagers
  need
  - CI verification for a lot of this so it doesn't drift/fail
  
  **AI usage:** A huge mix of me and Fable going back and forth. I wrote
  all the english. There's just a lot of glue in here that is not pleasant
  and does not spark joy to write, so I used more AI assistance than
  normal for this task and will continue to for packaging.
  ```
- [`8c0c45c`](https://github.com/ghostty-org/ghostty/commit/8c0c45c18a17fe8dc270b4c80ff31053c6f52a89) libghostty-vt: return GHOSTTY_UNSUPPORTED for unknown keys ([@mitchellh](https://github.com/mitchellh))
  ````text
  **This breaks the C ABI. This is all on purpose to stabilize the ABI to prep for a 1.0 stable libghostty-vt release.**
  
  All our enum-keyed APIs `*_{get,set,setopt,getopt}` now return a new
  result `GHOSTTY_UNSUPPORTED` for a key the library doesn't know. This
  lets a program compiled against newer headers but linked against an
  older build detect this case.
  
  Previously, unknown keys were undefined behavior. lol.
  
  Example usage:
  
  ```c
  bool blinking = false;
  switch (ghostty_render_state_get(state,
      GHOSTTY_RENDER_STATE_DATA_CURSOR_BLINKING, &blinking)) {
  case GHOSTTY_SUCCESS:
    break;
  case GHOSTTY_UNSUPPORTED:
    // Older library that doesn't know this key. Use a default.
    blinking = true;
    break;
  default:
    // A real error, such as a NULL state.
    return;
  }
  ```
  ````
- [`40066da`](https://github.com/ghostty-org/ghostty/commit/40066da055311c991b5c45be67313ef2b3661539) libghostty-vt: return GHOSTTY_UNSUPPORTED for unknown keys ([#15070](https://github.com/ghostty-org/ghostty/issues/15070)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  **This breaks the C ABI. This is all on purpose to stabilize the ABI to
  prep for a 1.0 stable libghostty-vt release.**
  
  All our enum-keyed APIs `*_{get,set,setopt,getopt}` now return a new
  result `GHOSTTY_UNSUPPORTED` for a key the library doesn't know. This
  lets a program compiled against newer headers but linked against an
  older build detect this case.
  
  Previously, unknown keys were undefined behavior. lol.
  
  Example usage:
  
  ```c
  bool blinking = false;
  switch (ghostty_render_state_get(state,
      GHOSTTY_RENDER_STATE_DATA_CURSOR_BLINKING, &blinking)) {
  case GHOSTTY_SUCCESS:
    break;
  case GHOSTTY_UNSUPPORTED:
    // Older library that doesn't know this key. Use a default.
    blinking = true;
    break;
  default:
    // A real error, such as a NULL state.
    return;
  }
  ```
  
  **AI usage:** My idea, I wrote the new docs and the main result return.
  Then the "repeatedly draw the owl" refactoring was done by Opus.
  Validated by Fable.
  ````
- [`5db83d7`](https://github.com/ghostty-org/ghostty/commit/5db83d7689bd7eaaaeb27198c9f870b04794cc8c) libghostty-vt: reserved allocator vtable slots, revamp allocator docs ([@mitchellh](https://github.com/mitchellh))
  ````text
  **This breaks the C ABI. This is all on purpose to stabilize the ABI to
  prep for a 1.0 stable libghostty-vt release.**
  
  Added four reserved `void*` slots to the end of `GhosttyAllocatorVtable`
  so we have room to add more function pointers if we ever want to.
  
  This also makes `resize` and `remap` optional. A NULL `resize` acts
  like it returned false and a NULL `remap` acts like it returned NULL,
  so the library falls back to alloc, copy, free. An allocator built on
  plain malloc and free now only needs `alloc` and `free`:
  
  ```c
  static const GhosttyAllocatorVtable vtable = {
      .alloc = my_alloc,
      .free = my_free,
  };
  ```
  
  The allocator docs in allocator.h were rewritten. They now cover the
  default allocator per platform, how to write an allocator, alignment
  (an exponent, not a byte count, which trips people up) and buffer
  ownership.
  
  The new example/c-vt-allocator is an alloc and free only allocator.
  ````
- [`ee02d01`](https://github.com/ghostty-org/ghostty/commit/ee02d019e8459ed4d09fac55753ad2363c5a8b01) libghostty-vt: reserved allocator vtable slots, revamp allocator docs ([#15068](https://github.com/ghostty-org/ghostty/issues/15068)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  **This breaks the C ABI. This is all on purpose to stabilize the ABI to
  prep for a 1.0 stable libghostty-vt release.**
  
  Added four reserved `void*` slots to the end of `GhosttyAllocatorVtable`
  so we have room to add more function pointers if we ever want to.
  
  This also makes `resize` and `remap` optional. A NULL `resize` acts like
  it returned false and a NULL `remap` acts like it returned NULL, so the
  library falls back to alloc, copy, free. An allocator built on plain
  malloc and free now only needs `alloc` and `free`:
  
  ```c
  static const GhosttyAllocatorVtable vtable = {
      .alloc = my_alloc,
      .free = my_free,
  };
  ```
  
  The allocator docs in allocator.h were rewritten. They now cover the
  default allocator per platform, how to write an allocator, alignment (an
  exponent, not a byte count, which trips people up) and buffer ownership.
  
  The new example/c-vt-allocator is an alloc and free only allocator.
  
  **AI usage:** Reviewed by Opus, primarily written by me, tests+example
  written by Opus.
  ````

## November 3, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/41704148845), [2](https://github.com/ghostty-org/ghostty/actions/runs/41657405741), [3](https://github.com/ghostty-org/ghostty/actions/runs/41640921915), [4](https://github.com/ghostty-org/ghostty/actions/runs/41612522728), [5](https://github.com/ghostty-org/ghostty/actions/runs/41588034700), [6](https://github.com/ghostty-org/ghostty/actions/runs/41578816344), [7](https://github.com/ghostty-org/ghostty/actions/runs/41569815273), [8](https://github.com/ghostty-org/ghostty/actions/runs/41558315898)  
Summary: 8 runs • 18 commits • 8 authors

### Changes

- [`0edfc65`](https://github.com/ghostty-org/ghostty/commit/0edfc656fa3d55d2bbf4519420666b19e5b19dba) macOS: fix tab bar frame on macOS 27 when it first appears. ([@bo2themax](https://github.com/bo2themax))
  ```text
  On macOS 27.2 (Probably already like this in early versions), the new tab button appears later than other views.
  The previous guard will skip the following layout, causing issues when the tab bar first appears on a window without tabs:
  1. "Show Tab Bar" the first time for a window without tabs.
  2. "Merge All Windows" from a window without tabs. The tab bar remains clipped until the next `becomeMain` or other functions trigger the setup.
  ```
- [`2d1f9cf`](https://github.com/ghostty-org/ghostty/commit/2d1f9cf1095ea4d5c0888ddbc62e03bd14e11597) os: reserve space for executable path terminator ([@12ya](https://github.com/12ya))
  ```text
  Return error.PathTooLong when a candidate path fills the buffer,
  leaving no room for the null terminator. Add a regression test for
  the boundary that previously caused an out-of-bounds write.
  ```
- [`fef7af4`](https://github.com/ghostty-org/ghostty/commit/fef7af4e19f6d8b0361c49e6190b81f3a64a999b) os: reserve space for executable path terminator ([#15058](https://github.com/ghostty-org/ghostty/issues/15058)) ([@jcollie](https://github.com/jcollie))
  ```text
  Return error.PathTooLong when a candidate path fills the buffer, leaving
  no room for the null terminator. Add a regression test for the boundary
  that previously caused an out-of-bounds write.
  
  AI disclosure: used OpenAI Codex
  ```
- [`c7f68a7`](https://github.com/ghostty-org/ghostty/commit/c7f68a7f48c6a5b357689eb8c2328bc2dab5d8ed) macOS: fix tab bar frame on macOS 27 when it first appears. ([#15029](https://github.com/ghostty-org/ghostty/issues/15029)) ([@bo2themax](https://github.com/bo2themax))
  ```text
  On macOS 27.2 (Probably already like this in early versions), the new
  tab button appears later than other views. The previous guard will skip
  the following layout, causing issues when the tab bar first appears on a
  window without tabs:
  1. "Show Tab Bar" the first time for a window without tabs.
  2. "Merge All Windows" from a window without tabs. The tab bar remains
  clipped until the next `becomeMain` or other functions trigger the
  setup.
  
  > New tab doesn't have the issue because it will trigger the setup
  multiple times (at least 3: addTitlebarAccessoryViewController,
  becomeMain and syncAppearance).
  
  ### AI Disclosure
  
  I check the RC myself and asked Claude to rephrase my scattered
  comments.
  ```
- [`fad1133`](https://github.com/ghostty-org/ghostty/commit/fad1133619a98a1bb60e99baac2d5460dfb33985) terminal: pass the style to fillStyles as a vector ([@arc-source-coder](https://github.com/arc-source-coder))
  ```text
  Without explicit `inline`, LLVM still inlines `fillStyles`, but
  writes each style as two 64-bit stores on x86-64. Passing the style
  as a vector restores one 16-byte vector store per style.
  
  ## Benchmarks
  
  `ghostty-bench +screen-clone` at 120x80 with 1 MiB of styled-heavy
  output, on Windows x86-64:
  
  | Mode          | main (ms)    | vector (ms)  | Speedup |
  | ------------- | ------------ | ------------ | ------- |
  | render-scroll | 441.4 ± 20.1 | 414.7 ± 14.6 | 1.06x   |
  ```
- [`4a2d77e`](https://github.com/ghostty-org/ghostty/commit/4a2d77ebb2d8d6973e1808bff1ca3e4f13b0a67b) terminal: reserve style runs once per row in RowBuilder.scan ([@arc-source-coder](https://github.com/arc-source-coder))
  ```text
  `RowBuilder.scan`, which runs during `beginUpdate`, previously called
  `ArrayList.append` for each style run.
  
  A cell starts at most one run, so reserve a row's worth of runs before
  the scan and use `appendAssumeCapacity`. Unlike `append`, which LLVM
  does not inline into the function, this compiles to inline stores.
  
  ## Benchmarks
  
  `ghostty-bench +screen-clone` on Windows x86-64:
  
  | Input         | Size   | Mode          | main (ms)     | reserve (ms)  | Speedup |
  | ------------- | ------ | ------------- | ------------- | ------------- | ------- |
  | DOOM-fire-zig | 160x50 | render-locked | 2480.6 ± 37.0 | 1285.0 ± 25.6 | 1.93x   |
  | DOOM-fire-zig | 160x50 | render        | 2759.3 ± 36.6 | 1571.1 ± 29.2 | 1.76x   |
  | styled-heavy  | 120x80 | render        | 297.1 ± 6.4   | 236.9 ± 6.4   | 1.25x   |
  | styled-heavy  | 120x80 | render-scroll | 414.5 ± 8.5   | 366.4 ± 9.0   | 1.13x   |
  ```
- [`7ea52a2`](https://github.com/ghostty-org/ghostty/commit/7ea52a29c5a91fa9a832aa6205add0a4311862da) terminal: pass the style to fillStyles as a vector ([#15053](https://github.com/ghostty-org/ghostty/issues/15053)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Follow-up to #15023.
  
  Without explicit `inline`, LLVM still inlines `fillStyles`, but lowers
  the fill to two 64-bit stores per style on x86-64. Passing the style as
  `@Vector(2, u64)` restores one `movdqu` 128-bit store.
  
  I also asked Sol to check ARM codegen: both versions already store the
  style in one instruction.
  
  ## Benchmarks
  
  `ghostty-bench +screen-clone` at 120x80 with 1 MiB of styled-heavy
  output, on Windows x86-64:
  
  | Mode          | main (ms)    | This PR (ms)  | Speedup |
  | ------------- | ------------ | ------------ | ------- |
  | render-scroll | 441.4 ± 20.1 | 414.7 ± 14.6 | 1.06x   |
  
  AI disclosure: Developed with OpenCode (GPT 6.1 Sol)
  ```
- [`6fba087`](https://github.com/ghostty-org/ghostty/commit/6fba0873efb7765e9d0f79de449063f3214b3d75) terminal: reserve style runs once per row in RowBuilder.scan ([#15054](https://github.com/ghostty-org/ghostty/issues/15054)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `RowBuilder.scan`, which runs during `beginUpdate`, previously appended
  each style run with `ArrayList.append`, which isn't inlined there. This
  reserves a row's worth of runs before the scan (a cell starts at most
  one run) and uses `appendAssumeCapacity`, which compiles to inline
  stores.
  
  ## Benchmarks
  
  `ghostty-bench +screen-clone` on Windows x86-64:
  
  | Input | Size | Mode | main (ms) | This PR (ms) | Speedup |
  | ------------- | ------ | ------------- | ------------- | -------------
  | ------- |
  | DOOM-fire-zig | 160x50 | render-locked | 2480.6 ± 37.0 | 1285.0 ± 25.6
  | 1.93x |
  | DOOM-fire-zig | 160x50 | render | 2759.3 ± 36.6 | 1571.1 ± 29.2 |
  1.76x |
  | styled-heavy | 120x80 | render | 297.1 ± 6.4 | 236.9 ± 6.4 | 1.25x |
  | styled-heavy | 120x80 | render-scroll | 414.5 ± 8.5 | 366.4 ± 9.0 |
  1.13x |
  
  AI disclosure: Developed with Claude Code (Opus 5.5) and OpenCode (GPT
  6.1 Sol), including benchmarking and codegen analysis.
  ```
- [`060ff6b`](https://github.com/ghostty-org/ghostty/commit/060ff6b52dcfde52112a8376c6cf3e26f4161edf) i18n: update Japanese translation ([#15025](https://github.com/ghostty-org/ghostty/issues/15025)) ([@clavinjune](https://github.com/clavinjune))
- [`b148bf7`](https://github.com/ghostty-org/ghostty/commit/b148bf728524ac17daec66692a8265d351c9c702) macos: allow quitting with a clipboard confirmation open ([@jparise](https://github.com/jparise))
  ```text
  The clipboard confirmation is a plain window presented as a sheet, and
  windows prevent application termination while modal by default. AppKit
  therefore dropped quit requests before reaching applicationShouldTerminate
  for as long as the modal was open. NSAlert sheets don't have this behavior.
  
  Verified with an active confirmation window using Cmd-Q, the quit action
  and Apple Event, and a quit event with the logout reason.
  ```
- [`0d1d5e8`](https://github.com/ghostty-org/ghostty/commit/0d1d5e884b88a711f1ccf47387ab41e8fa28a755) macos: allow quitting with a clipboard confirmation open ([#15040](https://github.com/ghostty-org/ghostty/issues/15040)) ([@bo2themax](https://github.com/bo2themax))
- [`c12d42e`](https://github.com/ghostty-org/ghostty/commit/c12d42eaf877b996cc798f9dd54b2a79ba630db9) terminal: print ASCII runs as u8 slices from input instead of u32 ([@mitchellh](https://github.com/mitchellh))
  ```text
  The stream now finds runs of plain ASCII (non-control) and passes that
  through to the terminal directly from the input pointer rather than widening
  it to u32 and doing a copy.
  
  This is implemented as a specialization on stream handlers, which both
  the Ghostty GUI and libghostty-vt handlers implement. If the specialized
  callback isn't implemented, the old `print_slice` (u32 slice) is used.
  
  Non-ASCII input takes the same path as before. utf8.vt and the CJK
  inputs are unchanged.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream` on Apple Silicon:
  
  | Input            | Size   | main (ms)    | print-u8 (ms) | Speedup |
  | ---------------- | ------ | ------------ | ------------- | ------- |
  | ascii.vt         | 120x80 | 43.2 ± 0.5   | 29.2 ± 0.5    | 1.48x   |
  | ascii-lines.vt   | 120x80 | 67.2 ± 0.5   | 51.3 ± 0.4    | 1.31x   |
  | styled-plain.vt  | 120x80 | 65.7 ± 0.3   | 48.9 ± 0.6    | 1.34x   |
  | light_cells.vt   | 120x80 | 39.3 ± 0.6   | 31.8 ± 0.3    | 1.24x   |
  | cursor_motion.vt | 120x80 | 147.2 ± 0.9  | 128.6 ± 1.1   | 1.14x   |
  | scrolling.vt     | 120x80 | 736.5 ± 6.4  | 648.7 ± 6.0   | 1.14x   |
  | dense_cells.vt   | 120x80 | 101.0 ± 0.7  | 94.8 ± 1.2    | 1.07x   |
  | utf8.vt          | 120x80 | 315.3 ± 2.6  | 314.6 ± 0.4   | 1.00x   |
  | osc.vt           | 120x80 | 951.5 ± 3.4  | 944.6 ± 2.7   | 1.01x   |
  | out.txt (2.6GB)  | 120x80 | 5177.6 ± 9.8 | 4892.7 ± 1.9  | 1.06x   |
  
  `ghostty-bench +terminal-stream` on x86-64 (Haswell, KVM guest):
  
  | Input            | Size   | main (ms) | print-u8 (ms) | Speedup |
  | ---------------- | ------ | --------- | ------------- | ------- |
  | ascii.vt         | 120x80 | 122.5     | 95.5          | 1.28x   |
  | ascii-lines.vt   | 120x80 | 234.5     | 175.9         | 1.33x   |
  | styled-plain.vt  | 120x80 | 231.8     | 174.4         | 1.33x   |
  | light_cells.vt   | 120x80 | 83.4      | 64.5          | 1.29x   |
  | cursor_motion.vt | 120x80 | 564.0     | 459.4         | 1.23x   |
  | scrolling.vt     | 120x80 | 3918.0    | 3577.6        | 1.10x   |
  | styled-heavy.vt  | 120x80 | 574.7     | 520.4         | 1.10x   |
  | dense_cells.vt   | 120x80 | 382.1     | 350.2         | 1.09x   |
  | medium_cells.vt  | 120x80 | 651.8     | 607.0         | 1.07x   |
  | utf8.vt          | 120x80 | 895.4     | 881.5         | 1.02x   |
  | cjk-prose.vt     | 120x80 | 274.9     | 280.8         | 0.98x   |
  | hyperlinks.vt    | 120x80 | 135.0     | 128.2         | 1.05x   |
  ```
- [`a227276`](https://github.com/ghostty-org/ghostty/commit/a227276b770c450ab0e5704a42a773c952e4991b) terminal: clear the blank hint where a snapshot test writes cells ([@mitchellh](https://github.com/mitchellh))
- [`091beb9`](https://github.com/ghostty-org/ghostty/commit/091beb99250bc4c1a255d3617b54630c115d0f27) terminal: print ASCII runs as u8 slices from input instead of u32 ([#15046](https://github.com/ghostty-org/ghostty/issues/15046)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The stream now finds runs of plain ASCII (non-control) and passes that
  through to the terminal directly from the input pointer rather than
  widening it to u32 and doing a copy.
  
  This is implemented as a specialization on stream handlers, which both
  the Ghostty GUI and libghostty-vt handlers implement. If the specialized
  callback isn't implemented, the old `print_slice` (u32 slice) is used.
  
  Non-ASCII input takes the same path as before. utf8.vt and the CJK
  inputs are unchanged.
  
  **Note: this does not speed up pure-ASCII `cat` times.** The speedups
  below are based on raw bytes pumping through libghostty's core. Our
  `cat` times in the shell are bound by the _kernel_, we're already within
  5% of the speed of a full 100% CPU busy loop pumping bytes out of a pty
  as fast as it can (and the last 5% is because we don't spin the CPU at
  100%).
  
  Edit: I edited the above to say "pure ASCII" because it does measurably
  speed up `cat`-ing the asciinema 2.6GB dump. That's because we now
  process the ASCII runs at full speed while slower sequences can't
  process at pty-read-speeds.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream` on Apple Silicon:
  
  | Input            | Size   | main (ms)    | print-u8 (ms) | Speedup |
  | ---------------- | ------ | ------------ | ------------- | ------- |
  | ascii.vt         | 120x80 | 43.2 ± 0.5   | 29.2 ± 0.5    | 1.48x   |
  | ascii-lines.vt   | 120x80 | 67.2 ± 0.5   | 51.3 ± 0.4    | 1.31x   |
  | styled-plain.vt  | 120x80 | 65.7 ± 0.3   | 48.9 ± 0.6    | 1.34x   |
  | light_cells.vt   | 120x80 | 39.3 ± 0.6   | 31.8 ± 0.3    | 1.24x   |
  | cursor_motion.vt | 120x80 | 147.2 ± 0.9  | 128.6 ± 1.1   | 1.14x   |
  | scrolling.vt     | 120x80 | 736.5 ± 6.4  | 648.7 ± 6.0   | 1.14x   |
  | dense_cells.vt   | 120x80 | 101.0 ± 0.7  | 94.8 ± 1.2    | 1.07x   |
  | utf8.vt          | 120x80 | 315.3 ± 2.6  | 314.6 ± 0.4   | 1.00x   |
  | osc.vt           | 120x80 | 951.5 ± 3.4  | 944.6 ± 2.7   | 1.01x   |
  | out.txt (2.6GB)  | 120x80 | 5177.6 ± 9.8 | 4892.7 ± 1.9  | 1.06x   |
  
  `ghostty-bench +terminal-stream` on x86-64 (Haswell, KVM guest):
  
  | Input            | Size   | main (ms) | print-u8 (ms) | Speedup |
  | ---------------- | ------ | --------- | ------------- | ------- |
  | ascii.vt         | 120x80 | 122.5     | 95.5          | 1.28x   |
  | ascii-lines.vt   | 120x80 | 234.5     | 175.9         | 1.33x   |
  | styled-plain.vt  | 120x80 | 231.8     | 174.4         | 1.33x   |
  | light_cells.vt   | 120x80 | 83.4      | 64.5          | 1.29x   |
  | cursor_motion.vt | 120x80 | 564.0     | 459.4         | 1.23x   |
  | scrolling.vt     | 120x80 | 3918.0    | 3577.6        | 1.10x   |
  | styled-heavy.vt  | 120x80 | 574.7     | 520.4         | 1.10x   |
  | dense_cells.vt   | 120x80 | 382.1     | 350.2         | 1.09x   |
  | medium_cells.vt  | 120x80 | 651.8     | 607.0         | 1.07x   |
  | utf8.vt          | 120x80 | 895.4     | 881.5         | 1.02x   |
  | cjk-prose.vt     | 120x80 | 274.9     | 280.8         | 0.98x   |
  | hyperlinks.vt    | 120x80 | 135.0     | 128.2         | 1.05x   |
  ```
- [`6676bba`](https://github.com/ghostty-org/ghostty/commit/6676bbaec73a2a30eced56003dd7248e931de6fa) Update VOUCHED list ([#15045](https://github.com/ghostty-org/ghostty/issues/15045)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/15044#discussioncomment-19366333)
  from @jcollie.
  
  Vouch: @ghdtjdwn
  ```
- [`25de649`](https://github.com/ghostty-org/ghostty/commit/25de649dde19bb96c7ad8ec4f7d28441a865da09) terminal: write the blank row once when scrolling a region up ([@mitchellh](https://github.com/mitchellh))
  ```text
  Scrolling up inside a scroll region (`cursorScrollRegionUp`) now builds
  the erased row's reset header in a register and writes it straight into
  the row's new slot at the bottom of the region. Previously it reset the
  row in place and then rotated it there.
  
  On x86-64 this improves scroll region vtebench results by 6-8%. This
  was actually a regress from #14997 so this just gets that back.
  
  Apple Silicon was never affected and still isn't. It now runs one fewer
  instruction per scrolled row with no measurable change in time. Other
  inputs stay within 0.06% of main in instructions retired.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream` on x86-64 (Haswell, KVM guest).
  
  | Input                         | Size   | main (ms) | x86-scroll (ms) | Speedup |
  | ----------------------------- | ------ | --------- | --------------- | ------- |
  | scrolling_top_small_region.vt | 120x80 | 2837.3    | 2582.3          | 1.11x   |
  | scrolling_bottom_region.vt    | 120x80 | 2775.0    | 2659.7          | 1.02x   |
  | scrolling.vt                  | 120x80 | 3855.1    | 3818.0          | 1.01x   |
  
  ## Why?
  
  `Row.blank` took a bit from the row's padding, and that changed how LLVM
  lowers the unchanged `row.reset()`. It now emits a 4-byte store of only
  the header's high half. `rotateOnce` does an 8-byte load of that same
  header a few instructions later. x86 can't forward a narrow store into
  a wider load, so every scrolled line waited for the store to reach
  cache. A profile put 62% of `cursorScrollRegionUp`'s samples right
  after that load.
  
  `fastmem.rotateIn` shifts the region and writes the new header after
  the memmove, so the header never makes the round trip through memory.
  With the change, the function's samples are back at their level from
  before #14997.
  ```
- [`18e645e`](https://github.com/ghostty-org/ghostty/commit/18e645ea22a5ef4793a2008275eb6f98e5d039bb) terminal: write the blank row once when scrolling a region up ([#15042](https://github.com/ghostty-org/ghostty/issues/15042)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Scrolling up inside a scroll region (`cursorScrollRegionUp`) now builds
  the erased row's reset header in a register and writes it straight into
  the row's new slot at the bottom of the region. Previously it reset the
  row in place and then rotated it there.
  
  On x86-64 this improves scroll region vtebench results by 6-8%. This was
  actually a regress from #14997 so this just gets that back.
  
  Apple Silicon was never affected and still isn't. It now runs one fewer
  instruction per scrolled row with no measurable change in time. Other
  inputs stay within 0.06% of main in instructions retired.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream` on x86-64 (Haswell, KVM guest).
  
  | Input | Size | main (ms) | x86-scroll (ms) | Speedup |
  | ----------------------------- | ------ | --------- | --------------- |
  ------- |
  | scrolling_top_small_region.vt | 120x80 | 2837.3 | 2582.3 | 1.11x |
  | scrolling_bottom_region.vt | 120x80 | 2775.0 | 2659.7 | 1.02x |
  | scrolling.vt | 120x80 | 3855.1 | 3818.0 | 1.01x |
  
  ## Why?
  
  `Row.blank` took a bit from the row's padding, and that changed how LLVM
  lowers the unchanged `row.reset()`. It now emits a 4-byte store of only
  the header's high half. `rotateOnce` does an 8-byte load of that same
  header a few instructions later. x86 can't forward a narrow store into a
  wider load, so every scrolled line waited for the store to reach cache.
  A profile put 62% of `cursorScrollRegionUp`'s samples right after that
  load.
  
  `fastmem.rotateIn` shifts the region and writes the new header after the
  memmove, so the header never makes the round trip through memory. With
  the change, the function's samples are back at their level from before
  #14997.
  
  **AI usage:** Fable figured this out. I had no idea, but I looked at its
  analysis and agree with its conclusions. I pushed it in bunch of
  different ways and couldn't find any holes. I wrote the prose.
  ```
- [`fa3b435`](https://github.com/ghostty-org/ghostty/commit/fa3b435cbfdc70c4e41ace87e1cde401f62e2aa5) Update VOUCHED list ([#15041](https://github.com/ghostty-org/ghostty/issues/15041)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14147#discussioncomment-19363823)
  from @jcollie.
  
  Vouch: @danudey
  ```

## November 2, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/41546831074), [2](https://github.com/ghostty-org/ghostty/actions/runs/41520563485), [3](https://github.com/ghostty-org/ghostty/actions/runs/41511614122), [4](https://github.com/ghostty-org/ghostty/actions/runs/41506747057), [5](https://github.com/ghostty-org/ghostty/actions/runs/41502755506), [6](https://github.com/ghostty-org/ghostty/actions/runs/41491697673), [7](https://github.com/ghostty-org/ghostty/actions/runs/41485839464), [8](https://github.com/ghostty-org/ghostty/actions/runs/41478021093), [9](https://github.com/ghostty-org/ghostty/actions/runs/41466669618), [10](https://github.com/ghostty-org/ghostty/actions/runs/41459038808), [11](https://github.com/ghostty-org/ghostty/actions/runs/41388327846), [12](https://github.com/ghostty-org/ghostty/actions/runs/41364959727)  
Summary: 12 runs • 39 commits • 5 authors

### Changes

- [`0e067de`](https://github.com/ghostty-org/ghostty/commit/0e067ded703c4212248daf996f97c62f2f13114a) core: declare pointer nullability in ghostty.h ([@jparise](https://github.com/jparise))
  ```text
  Pointers in ghostty.h declared no nullability information, so Swift
  imported them all as implicitly unwrapped optionals. This lack of
  enforcement made it possible to miss a guard and pass NULL to a non-null
  Zig parameter.
  
  Make non-null the header's default using Clang's `assume_nonnull` and
  explicitly annotate the other nullable pointers based on their Zig
  declarations.
  
  This exposed a few existing calls that had the wrong expectations:
  
  - The ghostty_set_window_background_blur callers, readSelection, and
    Config.backgroundColor could pass NULL and now guard their optional
    values.
  - Clearing the preedit passes NULL, so ghostty_surface_preedit now
    accepts a nullable pointer on the Zig side too.
  
  This change is source-breaking for Swift embedders because optional
  handling of newly non-optional values will no longer compile.
  ```
- [`a455842`](https://github.com/ghostty-org/ghostty/commit/a455842c28d587cd2ee2b75cc21fa021b1a47d09) core: declare pointer nullability in ghostty.h ([#15039](https://github.com/ghostty-org/ghostty/issues/15039)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Pointers in ghostty.h declared no nullability information, so Swift
  imported them all as implicitly unwrapped optionals. This lack of
  enforcement made it possible to miss a guard and pass NULL to a non-null
  Zig parameter.
  
  Make non-null the header's default using Clang's `assume_nonnull` and
  explicitly annotate the other nullable pointers based on their Zig
  declarations.
  
  This exposed a few existing calls that had the wrong expectations:
  
  - The ghostty_set_window_background_blur callers, readSelection, and
  Config.backgroundColor could pass NULL and now guard their optional
  values.
  - Clearing the preedit passes NULL, so ghostty_surface_preedit now
  accepts a nullable pointer on the Zig side too.
  
  This change is source-breaking for Swift embedders because optional
  handling of newly non-optional values will no longer compile.
  ```
- [`4c92f80`](https://github.com/ghostty-org/ghostty/commit/4c92f80954b1d563c148d77a051394fd2d39de60) terminal: print fast stays active while a hyperlink is open ([@mitchellh](https://github.com/mitchellh))
  ```text
  `printSlice` previously bailed out of its fast path whenever an OSC 8
  hyperlink was open and printed every codepoint through the scalar
  `print`. It now writes linked text with the same batched fills as
  unlinked text.
  
  The batched path is specialized at comptime on whether a link is open,
  decided once per `printSlice` call. We don't inline the link open part
  because it is rarer.
  
  The hyperlink map has a fixed capacity, so the fills only write as many
  cells as it has room for and never grow the page themselves (that would
  replace the page under their cached pointers). When it is full, `print`
  writes the next codepoint and grows the page through
  `cursorSetHyperlink` exactly as before.
  
  Overwriting cells that are already linked still falls back to `print`.
  That's something we can maybe optimize in the future.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream`:
  
  | Input              | Size    | main (ms)     | print-hyperlink (ms) | Speedup |
  | ------------------ | ------- | ------------- | -------------------- | ------- |
  | hyperlinks-long.vt | 120x80  | 94.0 ± 1.2    | 54.4 ± 1.0           | 1.73x   |
  | hyperlinks-long.vt | 215x215 | 99.3 ± 1.2    | 60.4 ± 1.5           | 1.64x   |
  | alternating.vt     | 120x80  | 154.4 ± 1.5   | 125.8 ± 0.5          | 1.23x   |
  | alternating.vt     | 215x215 | 150.2 ± 0.8   | 122.7 ± 1.8          | 1.22x   |
  | styled-mixed.vt    | 120x80  | 499.1 ± 3.5   | 454.6 ± 3.5          | 1.10x   |
  | styled-mixed.vt    | 215x215 | 460.6 ± 1.4   | 420.9 ± 5.1          | 1.09x   |
  | hyperlinks.vt      | 120x80  | 43.9 ± 0.5    | 39.9 ± 0.2           | 1.10x   |
  | hyperlinks.vt      | 215x215 | 44.9 ± 0.4    | 42.5 ± 0.8           | 1.06x   |
  | osc.vt             | 120x80  | 990.5 ± 15.8  | 944.8 ± 3.9          | 1.05x   |
  | osc.vt             | 215x215 | 1004.9 ± 9.6  | 963.2 ± 6.8          | 1.04x   |
  | ascii.vt           | 120x80  | 41.8 ± 0.3    | 41.7 ± 0.2           | 1.00x   |
  ```
- [`91973f2`](https://github.com/ghostty-org/ghostty/commit/91973f2b29be42a2a8713406e18c56238b5f6c19) terminal: print fast stays active while a hyperlink is open ([#15034](https://github.com/ghostty-org/ghostty/issues/15034)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `printSlice` previously bailed out of its fast path whenever an OSC 8
  hyperlink was open and printed every codepoint through the scalar
  `print`. It now writes linked text with the same batched fills as
  unlinked text.
  
  The batched path is specialized at comptime on whether a link is open,
  decided once per `printSlice` call. We don't inline the link open part
  because it is rarer.
  
  The hyperlink map has a fixed capacity, so the fills only write as many
  cells as it has room for and never grow the page themselves (that would
  replace the page under their cached pointers). When it is full, `print`
  writes the next codepoint and grows the page through
  `cursorSetHyperlink` exactly as before.
  
  Overwriting cells that are already linked still falls back to `print`.
  That's something we can maybe optimize in the future.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream`:
  
  | Input | Size | main (ms) | print-hyperlink (ms) | Speedup |
  | ------------------ | ------- | ------------- | -------------------- |
  ------- |
  | hyperlinks-long.vt | 120x80 | 94.0 ± 1.2 | 54.4 ± 1.0 | 1.73x |
  | hyperlinks-long.vt | 215x215 | 99.3 ± 1.2 | 60.4 ± 1.5 | 1.64x |
  | alternating.vt | 120x80 | 154.4 ± 1.5 | 125.8 ± 0.5 | 1.23x |
  | alternating.vt | 215x215 | 150.2 ± 0.8 | 122.7 ± 1.8 | 1.22x |
  | styled-mixed.vt | 120x80 | 499.1 ± 3.5 | 454.6 ± 3.5 | 1.10x |
  | styled-mixed.vt | 215x215 | 460.6 ± 1.4 | 420.9 ± 5.1 | 1.09x |
  | hyperlinks.vt | 120x80 | 43.9 ± 0.5 | 39.9 ± 0.2 | 1.10x |
  | hyperlinks.vt | 215x215 | 44.9 ± 0.4 | 42.5 ± 0.8 | 1.06x |
  | osc.vt | 120x80 | 990.5 ± 15.8 | 944.8 ± 3.9 | 1.05x |
  | osc.vt | 215x215 | 1004.9 ± 9.6 | 963.2 ± 6.8 | 1.04x |
  | ascii.vt | 120x80 | 41.8 ± 0.3 | 41.7 ± 0.2 | 1.00x |
  
  **AI usage:** Idea/impl by me, Fable review and benchmark.
  ```
- [`8484146`](https://github.com/ghostty-org/ghostty/commit/8484146c74ef4b075b68c9cf8767019b2b3c738c) terminal: skip erasing and scanning rows that are already blank ([@mitchellh](https://github.com/mitchellh))
  ```text
  Erase line (EL, `CSI K`) and erase character (ECH, `CSI X`) now do
  nothing to the cells of a row that is already blank. Scrolling the
  screen into history before a clear (`CSI 22 J`, or `CSI 2 J` at a
  prompt) no longer reads the cells of blank rows, and scans the other
  rows several cells at a time.
  
  This extends the `Row.blank` hint from #14997, which only covered whole
  rows cleared by erase display:
  https://github.com/ghostty-org/ghostty/pull/14997
  
  This doesn't impact any other workloads, and was identified in the
  asciinema dump as a relatively common command (see 2% speedup).
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream`:
  
  | Input           | Size    | main (ms)   | erase-opt-2 (ms) | Speedup |
  | --------------- | ------- | ----------- | ---------------- | ------- |
  | erase-scroll.vt | 120x80  | 241.9 ± 0.6 | 107.7 ± 0.2      | 2.24x   |
  | erase-scroll.vt | 120x12  | 50.5 ± 0.2  | 46.2 ± 0.4       | 1.09x   |
  | erase-scroll.vt | 300x100 | 797.6 ± 1.7 | 259.9 ± 0.5      | 3.07x   |
  | erase-lines.vt  | 120x80  | 43.9 ± 0.4  | 25.7 ± 0.3       | 1.71x   |
  | erase-lines.vt  | 120x12  | 41.6 ± 0.3  | 24.1 ± 0.5       | 1.73x   |
  | erase-lines.vt  | 300x100 | 80.3 ± 0.4  | 29.1 ± 0.2       | 2.76x   |
  | erase.vt        | 120x80  | 51.4 ± 0.4  | 51.5 ± 0.3       | 1.00x   |
  | ascii.vt        | 120x80  | 42.6 ± 0.8  | 42.2 ± 0.4       | 1.01x   |
  | styled-plain.vt | 120x80  | 66.5 ± 0.8  | 64.9 ± 0.5       | 1.02x   |
  | utf8.vt         | 120x80  | 316.2 ± 1.8 | 315.8 ± 1.4      | 1.00x   |
  | osc.vt          | 120x80  | 991 ± 21    | 979 ± 6          | 1.01x   |
  | scrolling.vt    | 120x80  | 736.2 ± 6.4 | 736.8 ± 6.1      | 1.00x   |
  | scrolling_fs.vt | 120x80  | 53.1 ± 0.2  | 53.1 ± 0.3       | 1.00x   |
  | out.txt (2.6GB) | 120x80  | 5315 ± 22   | 5231 ± 13        | 1.02x   |
  ```
- [`a0c0928`](https://github.com/ghostty-org/ghostty/commit/a0c092868ded132033c85104e9ab3a266c52f2d4) terminal: skip erasing and scanning rows that are already blank ([#15035](https://github.com/ghostty-org/ghostty/issues/15035)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Erase line (EL, `CSI K`) and erase character (ECH, `CSI X`) now do
  nothing to the cells of a row that is already blank. Scrolling the
  screen into history before a clear (`CSI 22 J`, or `CSI 2 J` at a
  prompt) no longer reads the cells of blank rows, and scans the other
  rows several cells at a time.
  
  This extends the `Row.blank` hint from #14997, which only covered whole
  rows cleared by erase display:
  https://github.com/ghostty-org/ghostty/pull/14997
  
  This doesn't impact any other workloads, and was identified in the
  asciinema dump as a relatively common command (see 2% speedup).
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream`:
  
  | Input           | Size    | main (ms)   | erase-opt-2 (ms) | Speedup |
  | --------------- | ------- | ----------- | ---------------- | ------- |
  | erase-scroll.vt | 120x80  | 241.9 ± 0.6 | 107.7 ± 0.2      | 2.24x   |
  | erase-scroll.vt | 120x12  | 50.5 ± 0.2  | 46.2 ± 0.4       | 1.09x   |
  | erase-scroll.vt | 300x100 | 797.6 ± 1.7 | 259.9 ± 0.5      | 3.07x   |
  | erase-lines.vt  | 120x80  | 43.9 ± 0.4  | 25.7 ± 0.3       | 1.71x   |
  | erase-lines.vt  | 120x12  | 41.6 ± 0.3  | 24.1 ± 0.5       | 1.73x   |
  | erase-lines.vt  | 300x100 | 80.3 ± 0.4  | 29.1 ± 0.2       | 2.76x   |
  | erase.vt        | 120x80  | 51.4 ± 0.4  | 51.5 ± 0.3       | 1.00x   |
  | ascii.vt        | 120x80  | 42.6 ± 0.8  | 42.2 ± 0.4       | 1.01x   |
  | styled-plain.vt | 120x80  | 66.5 ± 0.8  | 64.9 ± 0.5       | 1.02x   |
  | utf8.vt         | 120x80  | 316.2 ± 1.8 | 315.8 ± 1.4      | 1.00x   |
  | osc.vt          | 120x80  | 991 ± 21    | 979 ± 6          | 1.01x   |
  | scrolling.vt    | 120x80  | 736.2 ± 6.4 | 736.8 ± 6.1      | 1.00x   |
  | scrolling_fs.vt | 120x80  | 53.1 ± 0.2  | 53.1 ± 0.3       | 1.00x   |
  | out.txt (2.6GB) | 120x80  | 5315 ± 22   | 5231 ± 13        | 1.02x   |
  
  **AI usage:** I did the impl after #14997, Opus/Fable reviewed and
  benchmarked. Note: a lot of these are coming in fast now cause I was
  doing a lot of it in parallel over the weekend, the benchmarks and
  review took time.
  ```
- [`0b1729e`](https://github.com/ghostty-org/ghostty/commit/0b1729e945978fca4bcd6165d8ac408bf675a7f2) Update VOUCHED list ([#15036](https://github.com/ghostty-org/ghostty/issues/15036)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/15033#discussioncomment-19359609)
  from @jcollie.
  
  Vouch: @database64128
  ```
- [`22b8451`](https://github.com/ghostty-org/ghostty/commit/22b84514411aab13ce71c09052a10c76380eaf4b) terminal: re-read the style per row in the mixed-width print fast path ([@mitchellh](https://github.com/mitchellh))
  ```text
  `printSliceMixed` now reads the cursor's style ID for every row it
  fills, instead of building its cell template once at the start of the
  slice.
  
  This is a bug from the mixed narrow/wide fast path in #15021:
  https://github.com/ghostty-org/ghostty/pull/15021
  ```
- [`e0acea2`](https://github.com/ghostty-org/ghostty/commit/e0acea2753f84ec31c26cdc1c8837fad99cd83b9) terminal: re-read the style per row in the mixed-width print fast path ([#15032](https://github.com/ghostty-org/ghostty/issues/15032)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `printSliceMixed` now reads the cursor's style ID for every row it
  fills, instead of building its cell template once at the start of the
  slice.
  
  This is a bug from the mixed narrow/wide fast path in #15021:
  https://github.com/ghostty-org/ghostty/pull/15021
  ```
- [`faa346b`](https://github.com/ghostty-org/ghostty/commit/faa346b068361c47826b653af5e4a526e5a4e957) terminal: print uses the right margin after wrapping ([@mitchellh](https://github.com/mitchellh))
  ```text
  With left/right margins set and the cursor right of the right margin,
  `print` kept using the screen edge as its limit even after wrapping
  to the left margin. A wide char after the wrap could leave the cursor
  outside the margins. `printSlice` already handled this correctly.
  
  This matches xterm, which recomputes the right edge after every wrap
  (`dotext` in charproc.c).
  
  The fix resets the limit to the right margin after each wrap.
  ```
- [`77f85cd`](https://github.com/ghostty-org/ghostty/commit/77f85cd67c4c434acc714bb1d1248107a3782a68) terminal: print uses the right margin after wrapping ([#15030](https://github.com/ghostty-org/ghostty/issues/15030)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  With left/right margins set and the cursor right of the right margin,
  `print` kept using the screen edge as its limit even after wrapping to
  the left margin. A wide char after the wrap could leave the cursor
  outside the margins. `printSlice` already handled this correctly.
  
  This matches xterm, which recomputes the right edge after every wrap
  (`dotext` in charproc.c).
  
  The fix resets the limit to the right margin after each wrap.
  ```
- [`41557e2`](https://github.com/ghostty-org/ghostty/commit/41557e2ccf7f27b7ed6665b163bd467d4fa8691e) terminal: store Style as a packed u128 ([@arc-source-coder](https://github.com/arc-source-coder))
  ```text
  Style is now a `packed struct(u128)`. Equality compares the bits
  directly, hashing no longer builds a separate `PackedStyle`, and
  the style is all zero bits.
  
  `Style.Color` now uses an 8-bit tag and 24-bit payload. The constructors
  zero unused bits, and value() provides a tagged-union view for switching
  on a color. This also removes the wasm-specific equality and default
  checks.
  
  A u128 is 16-byte aligned, which increases the alignment of the style
  set. The page capacity calculation now accounts for padding before the
  metadata.
  
  `ghostty-bench +terminal-stream` at 120x80, on Windows x86-64:
  
  | Input           | main (ms)    | packed (ms)  | Speedup |
  | --------------- | ------------ | ------------ | ------- |
  | styled-heavy.vt | 377.8 ± 7.5  | 330.0 ± 9.1  | 1.14x   |
  | styled-multi.vt | 443.5 ± 17.2 | 401.9 ± 12.4 | 1.10x   |
  | ascii.vt        | 73.6 ± 2.0   | 72.3 ± 1.9   | 1.02x   |
  | utf8.vt         | 580.9 ± 20.3 | 573.7 ± 14.6 | 1.01x   |
  | styled-mixed.vt | 1088 ± 8     | 1085 ± 16    | 1.00x   |
  | styled-plain.vt | 112.6 ± 2.6  | 112.5 ± 3.0  | 1.00x   |
  | osc.vt          | 2256 ± 31    | 2256 ± 64    | 1.00x   |
  
  `ghostty-bench +screen-clone` at 120x80 on 1 MiB of styled-heavy.vt:
  
  | Mode          | main (ms)    | packed (ms)  | Speedup |
  | ------------- | ------------ | ------------ | ------- |
  | render-scroll | 561.3 ± 21.0 | 453.9 ± 22.3 | 1.24x   |
  | render        | 342.3 ± 9.7  | 310.8 ± 6.1  | 1.10x   |
  ```
- [`73a2a1d`](https://github.com/ghostty-org/ghostty/commit/73a2a1d06e9269b67257f4ab810f1a489f0d5b19) terminal: move SGR attribute handling to Style ([@arc-source-coder](https://github.com/arc-source-coder))
  ```text
  Move the SGR attribute switch from `Screen.applyAttribute` into
  `Style.withAttribute(attr)`, which returns the updated style.
  
  Performance is neutral to slightly faster (2-3%) on sequences with
  several attributes. With `withAttribute` inlined, LLVM keeps the running
  style and cursor pointer in registers across attributes instead of
  reloading them from the stack. On x86-64, a bold attribute goes from
  34 to 28 instructions per loop iteration, and `38;5;N` from 66 to 47.
  ```
- [`72bc97a`](https://github.com/ghostty-org/ghostty/commit/72bc97a9edf5df1080fa68fc8b38c45dc692c8ea) terminal: simplify fillStyles to one vector store ([@arc-source-coder](https://github.com/arc-source-coder))
  ```text
  Now that Style is exactly 16 bytes, `fillStyles` writes each style with
  one vector store. The old version used two overlapping 16-byte stores
  to handle styles of 16-32 bytes. With a 16-byte Style, both write to the
  same address, and LLVM lowered the old loop to two 64-bit stores per style.
  
  `ghostty-bench +screen-clone` at 120x80 on 1 MiB of styled-heavy.vt:
  
  | Mode          | before (ms)   | after (ms)   | Speedup |
  | ------------- | ------------- | ------------ | ------- |
  | render-scroll | 457.2 ± 25.7  | 424.9 ± 23.3 | 1.08x   |
  | render        | 314.4 ± 7.0   | 312.4 ± 6.0  | 1.01x   |
  ```
- [`de16f08`](https://github.com/ghostty-org/ghostty/commit/de16f08dcf7f3f4104e8722cb39a632a6a8a19f9) terminal: assert canonical Style.Color bits, test hash and constructors ([@mitchellh](https://github.com/mitchellh))
  ```text
  Review follow-ups for the packed Style:
  
  * `Color.value()` now asserts that the unused payload bits of `.none`
    and `.palette` colors are zero. Equality and hashing compare raw bits,
    so a non-canonical color would compare unequal to its canonical twin
    while reading back as the same value. The assert is `unreachable` in
    release builds and costs nothing there.
  
  * Drop the `hasUniqueRepresentation` assert. For a packed struct it
    reduces to `@sizeOf * 8 == @bitSizeOf`, which the two asserts above
    it already state.
  
  * Add tests that the three constructors leave unused bits zero and that
    the hash fold separates the same value in different fields (fg vs bg
    vs underline, palette vs flags), which is what the odd multiplier on
    the upper half exists for.
  
  * `fillStyles` has one call site; drop `inline`.
  ```
- [`d20d208`](https://github.com/ghostty-org/ghostty/commit/d20d208c514661ca14b9935576d66655fa2a8be8) terminal: size the hyperlink map independently of the hyperlink set ([@mitchellh](https://github.com/mitchellh))
  ```text
  A page's hyperlink map is now sized by its own capacity field,
  `hyperlink_cells`, instead of being derived from the hyperlink
  set's byte capacity. We previously derived it from bytes and were
  usually wasting bytes.
  
  The point of this change is primarily MEMORY DENSITY. We now get more
  rows/MB since our page structure isn't wasting as much. See benchmarks below.
  
  The snapshot format is unchanged. The PAGE header's single hyperlink
  capacity hint now covers both tables (the larger of the set bytes and
  the map's equivalent in set items), so old snapshots decode to the same
  layout as before and new snapshots stay readable by current readers.
  I made that as a choice to avoid breaking snapshots. Snapshots don't
  need perfect decode and its not super important for performance there.
  
  `ghostty-bench +terminal-stream`:
  
  | Input           | Size    | main (ms)    | hyperlink-map-size (ms) | Speedup |
  | --------------- | ------- | ------------ | ----------------------- | ------- |
  | hyperlinks.vt   | 215x215 | 61.8 ± 1.3   | 44.7 ± 0.5              | 1.38x   |
  | hyperlinks.vt   | 120x80  | 53.7 ± 0.3   | 43.5 ± 0.3              | 1.23x   |
  | osc.vt          | 120x80  | 1129.0 ± 2.2 | 978.8 ± 4.2             | 1.15x   |
  | osc.vt          | 215x215 | 1097.4 ± 6.7 | 1012.8 ± 4.0            | 1.08x   |
  | alternating.vt  | 120x80  | 163.8 ± 3.3  | 151.8 ± 0.9             | 1.08x   |
  | burst.vt        | 120x80  | 73.8 ± 0.6   | 68.9 ± 0.4              | 1.07x   |
  | styled-mixed.vt | 120x80  | 575.0 ± 2.1  | 580.1 ± 4.6             | 0.99x   |
  | styled-heavy.vt | 120x80  | 230.5 ± 0.2  | 230.5 ± 0.6             | 1.00x   |
  | ascii.vt        | 120x80  | 40.4 ± 0.3   | 40.5 ± 0.1              | 1.00x   |
  | utf8.vt         | 120x80  | 382.0 ± 0.9  | 386.0 ± 5.0             | 0.99x   |
  | erase.vt        | 120x80  | 50.1 ± 0.1   | 50.8 ± 0.1              | 0.99x   |
  
  The speedups come from fewer page clones (osc.vt at 120x80 went from
  232 capacity growths to 62) and from pages staying in the pool instead
  of being allocated on the heap. So this helps in general.
  
  Now memory. At a 10 MB scrollback limit at 120x80:
  
  | Input          | Heap pages   | History rows | Rows/MiB   |
  | -------------- | ------------ | ------------ | ---------- |
  | osc.vt         | 2157 -> 328  | 5625 -> 6507 | 624 -> 694 |
  | hyperlinks.vt  | 520 -> 6     | 6125 -> 7262 | 681 -> 775 |
  | alternating.vt | 1088 -> 266  | 9002 -> 9032 | 948 -> 963 |
  | ascii.vt       | 0 -> 0       | 9117 -> 9117 | 972 -> 972 |
  ```
- [`687f37a`](https://github.com/ghostty-org/ghostty/commit/687f37acd90462d451acd5f79042822d5d0255fb) terminal: pack Style into 128 bits and simplify style updates ([#15023](https://github.com/ghostty-org/ghostty/issues/15023)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously, style comparisons checked flags and colors field by field,
  and hashing created a `PackedStyle` each time. This stores `Style`
  directly as a `packed struct(u128)`, so equality becomes a single
  integer comparison and hashing no longer needs the packing step. It also
  removes the wasm-specific equality and default-style checks.
  
  This also moves SGR attribute application from `Screen` into
  `Style.withAttribute`, which allows LLVM to keep the running style in
  registers across attributes. The render-state style fill now uses one
  16-byte vector store per cell.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream` at 120x80, on Windows x86-64:
  
  | Input           | main (ms)    | This PR (ms)   | Speedup |
  | --------------- | ------------ | ------------ | ------- |
  | styled-heavy.vt | 377.8 ± 7.5  | 325.9 ± 5.9  | 1.16x   |
  | styled-multi.vt | 443.5 ± 17.2 | 390.9 ± 12.6 | 1.13x   |
  | ascii.vt        | 73.6 ± 2.0   | 72.9 ± 2.2   | 1.01x   |
  | styled-mixed.vt | 1088 ± 8     | 1084 ± 9     | 1.00x   |
  | utf8.vt         | 580.9 ± 20.3 | 579.0 ± 26.1 | 1.00x   |
  | styled-plain.vt | 112.6 ± 2.6  | 112.4 ± 3.6  | 1.00x   |
  | osc.vt          | 2256 ± 31    | 2258 ± 32    | 1.00x   |
  
  `ghostty-bench +screen-clone` at 120x80, with 1 MiB of styled-heavy
  output:
  
  | Mode          | main (ms)    | This PR (ms)   | Speedup |
  | ------------- | ------------ | ------------ | ------- |
  | render-scroll | 561.3 ± 21.0 | 424.9 ± 23.3 | 1.32x   |
  | render        | 342.3 ± 9.7  | 312.4 ± 6.0  | 1.10x   |
  
  AI disclosure: Developed with Claude Code (Opus 5.5) and OpenCode (GPT
  6.1 Sol), including profiling and codegen experiments.
  ```
- [`298f8ec`](https://github.com/ghostty-org/ghostty/commit/298f8ecb9cd30471da7bca9933335e496a5882d1) terminal: size the hyperlink map independently of the hyperlink set ([#15028](https://github.com/ghostty-org/ghostty/issues/15028)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A page's hyperlink map is now sized by its own capacity field,
  `hyperlink_cells`, instead of being derived from the hyperlink set's
  byte capacity. We previously derived it from bytes and were usually
  wasting bytes.
  
  The point of this change is primarily MEMORY DENSITY. We now get more
  rows/MB since our page structure isn't wasting as much. And more rows/MB
  means less page growths! See benchmarks below.
  
  The snapshot format is unchanged. The PAGE header's single hyperlink
  capacity hint now covers both tables (the larger of the set bytes and
  the map's equivalent in set items), so old snapshots decode to the same
  layout as before and new snapshots stay readable by current readers. I
  made that as a choice to avoid breaking snapshots. Snapshots don't need
  perfect decode and its not super important for performance there.
  
  `ghostty-bench +terminal-stream`:
  
  | Input | Size | main (ms) | hyperlink-map-size (ms) | Speedup |
  | --------------- | ------- | ------------ | ----------------------- |
  ------- |
  | hyperlinks.vt | 215x215 | 61.8 ± 1.3 | 44.7 ± 0.5 | 1.38x |
  | hyperlinks.vt | 120x80 | 53.7 ± 0.3 | 43.5 ± 0.3 | 1.23x |
  | osc.vt | 120x80 | 1129.0 ± 2.2 | 978.8 ± 4.2 | 1.15x |
  | osc.vt | 215x215 | 1097.4 ± 6.7 | 1012.8 ± 4.0 | 1.08x |
  | alternating.vt | 120x80 | 163.8 ± 3.3 | 151.8 ± 0.9 | 1.08x |
  | burst.vt | 120x80 | 73.8 ± 0.6 | 68.9 ± 0.4 | 1.07x |
  | styled-mixed.vt | 120x80 | 575.0 ± 2.1 | 580.1 ± 4.6 | 0.99x |
  | styled-heavy.vt | 120x80 | 230.5 ± 0.2 | 230.5 ± 0.6 | 1.00x |
  | ascii.vt | 120x80 | 40.4 ± 0.3 | 40.5 ± 0.1 | 1.00x |
  | utf8.vt | 120x80 | 382.0 ± 0.9 | 386.0 ± 5.0 | 0.99x |
  | erase.vt | 120x80 | 50.1 ± 0.1 | 50.8 ± 0.1 | 0.99x |
  
  The speedups come from fewer page clones (osc.vt at 120x80 went from 232
  capacity growths to 62) and from pages staying in the pool instead of
  being allocated on the heap. So this helps in general.
  
  Now memory. At a 10 MB scrollback limit at 120x80:
  
  | Input          | Heap pages   | History rows | Rows/MiB   |
  | -------------- | ------------ | ------------ | ---------- |
  | osc.vt         | 2157 -> 328  | 5625 -> 6507 | 624 -> 694 |
  | hyperlinks.vt  | 520 -> 6     | 6125 -> 7262 | 681 -> 775 |
  | alternating.vt | 1088 -> 266  | 9002 -> 9032 | 948 -> 963 |
  | ascii.vt       | 0 -> 0       | 9117 -> 9117 | 972 -> 972 |
  
  **AI usage:** Tests written by Opus, main impl by me, PR desc by me.
  ```
- [`a74bd24`](https://github.com/ghostty-org/ghostty/commit/a74bd243c03301a00a480035734aa1febbab2ea1) Fix broken tests using old syntax ([@mitchellh](https://github.com/mitchellh))
- [`68750a1`](https://github.com/ghostty-org/ghostty/commit/68750a1be2b99227328a6b185ae72719dea0428f) terminal: support mixed narrow/wide in print fast path ([@mitchellh](https://github.com/mitchellh))
  ```text
  `printSlice` previously bailed out of its fast path when there was a
  width class change. It can now continue going in various circumstances,
  which is realistic since before even things like CJK/emoji + a space
  would drop out of fast path!
  
  This still has limits: zero-width codepoints, grapheme continuations,
  hyperlinked cells, insert mode and DECAWM off still fall back to the
  per-codepoint `print` path as before.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream` at 120x80:
  
  | Input           | 2027 | main (ms)   | print-mixed (ms) | Speedup |
  | --------------- | ---- | ----------- | ---------------- | ------- |
  | cjk-prose.vt    | off  | 171.9 ± 0.4 | 83.7 ± 0.3       | 2.05x   |
  | cjk-prose.vt    | on   | 178.5 ± 0.5 | 89.1 ± 0.2       | 2.00x   |
  | cjk-spaces.vt   | off  | 25.5 ± 0.1  | 15.4 ± 0.1       | 1.65x   |
  | cjk-spaces.vt   | on   | 26.3 ± 0.3  | 16.2 ± 0.1       | 1.63x   |
  | styled-uni.vt   | off  | 330.4 ± 0.8 | 219.9 ± 0.7      | 1.50x   |
  | styled-uni.vt   | on   | 367.5 ± 0.7 | 259.1 ± 0.7      | 1.42x   |
  | utf8.vt         | off  | 382.4 ± 1.0 | 313.6 ± 0.5      | 1.22x   |
  | utf8.vt         | on   | 398.8 ± 0.8 | 329.4 ± 0.4      | 1.21x   |
  | styled-mixed.vt | off  | 572.3 ± 1.6 | 504.5 ± 2.1      | 1.13x   |
  | styled-mixed.vt | on   | 599.5 ± 1.4 | 529.2 ± 0.9      | 1.13x   |
  | ascii.vt        | off  | 40.5 ± 0.1  | 40.6 ± 0.1       | 1.00x   |
  | styled-plain.vt | off  | 63.8 ± 0.5  | 63.3 ± 0.3       | 1.01x   |
  | osc.vt          | off  | 1125 ± 4    | 1122 ± 2         | 1.00x   |
  | out.txt (2.6GB) | off  | 5455 ± 177  | 5375 ± 8         | 1.01x   |
  | out.txt (2.6GB) | on   | 5399 ± 7    | 5413 ± 6         | 1.00x   |
  
  - cjk-spaces.vt is `+utf8` with only CJK ideographs and a space after 30%
    of them.
  - cjk-prose.vt mixes them with printable ASCII at a 1:0.3 weight.
  - styled-uni.vt is `+styled` with multibyte weights
  ```
- [`e2a3ba0`](https://github.com/ghostty-org/ghostty/commit/e2a3ba004d01ca1d0251c891544b97784a072c20) terminal: support mixed narrow/wide in print fast path ([#15021](https://github.com/ghostty-org/ghostty/issues/15021)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `printSlice` previously bailed out of its fast path when there was a
  width class change. It can now continue going in various circumstances,
  which is realistic since before even things like CJK/emoji + a space
  would drop out of fast path!
  
  This still has limits: zero-width codepoints, grapheme continuations,
  hyperlinked cells, insert mode and DECAWM off still fall back to the
  per-codepoint `print` path as before.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream` at 120x80:
  
  | Input           | 2027 | main (ms)   | print-mixed (ms) | Speedup |
  | --------------- | ---- | ----------- | ---------------- | ------- |
  | cjk-prose.vt    | off  | 171.9 ± 0.4 | 83.7 ± 0.3       | 2.05x   |
  | cjk-prose.vt    | on   | 178.5 ± 0.5 | 89.1 ± 0.2       | 2.00x   |
  | cjk-spaces.vt   | off  | 25.5 ± 0.1  | 15.4 ± 0.1       | 1.65x   |
  | cjk-spaces.vt   | on   | 26.3 ± 0.3  | 16.2 ± 0.1       | 1.63x   |
  | styled-uni.vt   | off  | 330.4 ± 0.8 | 219.9 ± 0.7      | 1.50x   |
  | styled-uni.vt   | on   | 367.5 ± 0.7 | 259.1 ± 0.7      | 1.42x   |
  | utf8.vt         | off  | 382.4 ± 1.0 | 313.6 ± 0.5      | 1.22x   |
  | utf8.vt         | on   | 398.8 ± 0.8 | 329.4 ± 0.4      | 1.21x   |
  | styled-mixed.vt | off  | 572.3 ± 1.6 | 504.5 ± 2.1      | 1.13x   |
  | styled-mixed.vt | on   | 599.5 ± 1.4 | 529.2 ± 0.9      | 1.13x   |
  | ascii.vt        | off  | 40.5 ± 0.1  | 40.6 ± 0.1       | 1.00x   |
  | styled-plain.vt | off  | 63.8 ± 0.5  | 63.3 ± 0.3       | 1.01x   |
  | osc.vt          | off  | 1125 ± 4    | 1122 ± 2         | 1.00x   |
  | out.txt (2.6GB) | off  | 5455 ± 177  | 5375 ± 8         | 1.01x   |
  | out.txt (2.6GB) | on   | 5399 ± 7    | 5413 ± 6         | 1.00x   |
  
  - cjk-spaces.vt is `+utf8` with only CJK ideographs and a space after
  30% of them.
  - cjk-prose.vt mixes them with printable ASCII at a 1:0.3 weight.
  - styled-uni.vt is `+styled` with multibyte weights
  
  **AI usage:** I had the initial idea, but my work gained a 30% speedup.
  Upon an adversarial review with Fable, it identified some register
  spilling and branch mispredicts that were eating huge cost and reworked
  it (to the mixed row loop now), which I understood/reviewed and accept.
  I wrote all the human language.
  ```
- [`825f31c`](https://github.com/ghostty-org/ghostty/commit/825f31c5201e5f6144ac9267d459e64740e4c456) Update VOUCHED list ([#15022](https://github.com/ghostty-org/ghostty/issues/15022)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/15020#discussioncomment-19356061)
  from @jcollie.
  
  Vouch: @yinxiangshi
  ```
- [`379bdfa`](https://github.com/ghostty-org/ghostty/commit/379bdfabffe16b6a326c4289ad2bf9d712cce80a) Update VOUCHED list ([#15016](https://github.com/ghostty-org/ghostty/issues/15016)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/15015#discussioncomment-19355011)
  from @jcollie.
  
  Vouch: @arc-source-coder
  ```
- [`9113da0`](https://github.com/ghostty-org/ghostty/commit/9113da029815076cefbbc1ea7b1f63e8082e09ea) terminal: project hyperlink and string capacity when growing a page ([@mitchellh](https://github.com/mitchellh))
  ```text
  `PageList.increaseCapacity` now projects hyperlink and string capacity
  from the page's current usage, the same way it has for styles and
  graphemes since #13826. A page that runs out of hyperlink or string
  space grows once to about what the whole page will need, instead of
  doubling over and over.
  
  Previously, hyperlinks and strings always doubled. Hyperlink capacity
  starts at only 4 links, so a page with a unique link on every row (such
  as `ls --hyperlink`) grew its hyperlink capacity 8 times. Every growth
  is a full page allocation and copy.
  
  `ghostty-bench +terminal-stream` at 120x80:
  
  | Input              | main (ms)    | grow-hyperlink (ms) | Speedup |
  | ------------------ | ------------ | ------------------- | ------- |
  | alternating.vt     | 471.5 ± 5.5  | 410.2 ± 1.3         | 1.15x   |
  | osc.vt             | 1177 ± 47    | 1126 ± 29           | 1.04x   |
  | burst.vt           | 125.2 ± 0.4  | 123.3 ± 0.4         | 1.02x   |
  | styled-mixed.vt    | 577.3 ± 3.0  | 575.2 ± 3.1         | 1.00x   |
  | erase.vt           | 359.7        | 357.9               | 1.01x   |
  | ascii.vt           | 41.5         | 41.4                | 1.00x   |
  | styled-heavy.vt    | 246.5 ± 1.4  | 246.7 ± 0.9         | 1.00x   |
  | utf8.vt            | 408.7 ± 1.7  | 408.0 ± 1.2         | 1.00x   |
  | out.txt (2.6GB)    | 5734 ± 49    | 5553 ± 173          | 1.03x   |
  
  In the real world, this is a small win. A unique link per row is what
  `ls --hyperlink` and some compilers produce, but most output doesn't
  look like that. Its important it doesn't regress other workoads.
  ```
- [`f0d8cb7`](https://github.com/ghostty-org/ghostty/commit/f0d8cb776254f5dec58b353811398c60fff2fd86) terminal: carried pages compare usage per row ([@mitchellh](https://github.com/mitchellh))
  ```text
  When a carried page has fewer rows than the standard so that it fits in
  a pool item, `grow` now scales its usage up to the standard row count
  before deciding what capacity the next page keeps.
  
  Previously, a trimmed page looked emptier than it really was, so the next
  page shrank its jcapacity, ran out of room, and had to grow by copying itself.
  
  This is a follow-up fix to carried pages from #14985:
  https://github.com/ghostty-org/ghostty/pull/14985
  
  In the real world I think this would be a pretty edge case scenario but
  it was something I saw that bothered me.
  
  `ghostty-bench +terminal-stream`:
  
  | Input           | Size   | main (ms)    | fix (ms)     | Speedup |
  | --------------- | ------ | ------------ | ------------ | ------- |
  | cycle.vt        | 80x24  | 234.2 ± 4.9  | 144.1 ± 4.6  | 1.63x   |
  | styled-mixed.vt | 120x80 | 583.4 ± 3.2  | 582.4 ± 2.1  | 1.00x   |
  | styled-mixed.vt | 30x24  | 630.2 ± 2.3  | 631.6 ± 3.1  | 1.00x   |
  | osc.vt          | 120x80 | 1152.2 ± 9.7 | 1158.2 ± 5.1 | 0.99x   |
  | burst.vt        | 120x80 | 76.4 ± 1.0   | 76.5 ± 0.7   | 1.00x   |
  | alternating.vt  | 120x80 | 177.8 ± 2.5  | 178.8 ± 2.4  | 0.99x   |
  | styled-heavy.vt | 120x80 | 240.8 ± 0.9  | 241.6 ± 2.1  | 1.00x   |
  | utf8.vt         | 120x80 | 384.2 ± 0.8  | 384.0 ± 1.0  | 1.00x   |
  | ascii.vt        | 120x80 | 41.9 ± 0.1   | 41.8 ± 0.3   | 1.00x   |
  ```
- [`431d003`](https://github.com/ghostty-org/ghostty/commit/431d003c44e857f7ce273e3e209c9daac8eee85e) terminal: project hyperlink and string capacity when growing a page ([#15012](https://github.com/ghostty-org/ghostty/issues/15012)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `PageList.increaseCapacity` now projects hyperlink and string capacity
  from the page's current usage, the same way it has for styles and
  graphemes since #13826. A page that runs out of hyperlink or string
  space grows once to about what the whole page will need, instead of
  doubling over and over.
  
  Previously, hyperlinks and strings always doubled. Hyperlink capacity
  starts at only 4 links, so a page with a unique link on every row (such
  as `ls --hyperlink`) grew its hyperlink capacity 8 times. Every growth
  is a full page allocation and copy.
  
  `ghostty-bench +terminal-stream` at 120x80:
  
  | Input              | main (ms)    | grow-hyperlink (ms) | Speedup |
  | ------------------ | ------------ | ------------------- | ------- |
  | alternating.vt     | 471.5 ± 5.5  | 410.2 ± 1.3         | 1.15x   |
  | osc.vt             | 1177 ± 47    | 1126 ± 29           | 1.04x   |
  | burst.vt           | 125.2 ± 0.4  | 123.3 ± 0.4         | 1.02x   |
  | styled-mixed.vt    | 577.3 ± 3.0  | 575.2 ± 3.1         | 1.00x   |
  | erase.vt           | 359.7        | 357.9               | 1.01x   |
  | ascii.vt           | 41.5         | 41.4                | 1.00x   |
  | styled-heavy.vt    | 246.5 ± 1.4  | 246.7 ± 0.9         | 1.00x   |
  | utf8.vt            | 408.7 ± 1.7  | 408.0 ± 1.2         | 1.00x   |
  | out.txt (2.6GB)    | 5734 ± 49    | 5553 ± 173          | 1.03x   |
  
  In the real world, this is a small win. A unique link per row is what
  `ls --hyperlink` and some compilers produce, but most output doesn't
  look like that. Its important it doesn't regress other workoads.
  
  **AI usage:** Opus for tests, benchmarking, validation. Meat brain for
  impl and this PR desc.
  ```
- [`7b267cd`](https://github.com/ghostty-org/ghostty/commit/7b267cd9ac7863b0bd72e808daa021381e72dc21) terminal: carried pages compare usage per row ([#15013](https://github.com/ghostty-org/ghostty/issues/15013)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  When a carried page has fewer rows than the standard so that it fits in
  a pool item, `grow` now scales its usage up to the standard row count
  before deciding what capacity the next page keeps.
  
  Previously, a trimmed page looked emptier than it really was, so the
  next page shrank its jcapacity, ran out of room, and had to grow by
  copying itself.
  
  This is a follow-up fix to carried pages from #14985:
  https://github.com/ghostty-org/ghostty/pull/14985
  
  In the real world I think this would be a pretty edge case scenario but
  it was something I saw that bothered me.
  
  `ghostty-bench +terminal-stream`:
  
  | Input           | Size   | main (ms)    | fix (ms)     | Speedup |
  | --------------- | ------ | ------------ | ------------ | ------- |
  | cycle.vt        | 80x24  | 234.2 ± 4.9  | 144.1 ± 4.6  | 1.63x   |
  | styled-mixed.vt | 120x80 | 583.4 ± 3.2  | 582.4 ± 2.1  | 1.00x   |
  | styled-mixed.vt | 30x24  | 630.2 ± 2.3  | 631.6 ± 3.1  | 1.00x   |
  | osc.vt          | 120x80 | 1152.2 ± 9.7 | 1158.2 ± 5.1 | 0.99x   |
  | burst.vt        | 120x80 | 76.4 ± 1.0   | 76.5 ± 0.7   | 1.00x   |
  | alternating.vt  | 120x80 | 177.8 ± 2.5  | 178.8 ± 2.4  | 0.99x   |
  | styled-heavy.vt | 120x80 | 240.8 ± 0.9  | 241.6 ± 2.1  | 1.00x   |
  | utf8.vt         | 120x80 | 384.2 ± 0.8  | 384.0 ± 1.0  | 1.00x   |
  | ascii.vt        | 120x80 | 41.9 ± 0.1   | 41.8 ± 0.3   | 1.00x   |
  
  EDIT: The `cycle.vt` input shape was one chosen particularly to exercise
  the grow/shrink issue I saw. Its not representative of real world data.
  
  **AI usage:** I saw the problem and came up with the idea to resolve it,
  deferred to Opus for impl, testing, validation. I reviewed.
  ```
- [`0d4418a`](https://github.com/ghostty-org/ghostty/commit/0d4418ac20922475ebb40ef23a666898bbc91b67) terminal: fix edge cases in carried page capacity ([@mitchellh](https://github.com/mitchellh))
  ```text
  Found a few bugs from #14985:
  
    - The rows per byte check that decides whether a carried page may
      trim rows to fit in the pool overflowed on 32-bit targets (i.e. wasm32)
      for terminals narrower than about 37 columns.
    - `grow_hint` was updated before the new page was allocated. If
      allocation failed this caused problems.
    - On tall terminals at the minimum scrollback size, pages with
      trimmed rows hold less of the active area, so the page list could
      go over the byte limit during a burst of styled output.
  
  These are all correctness fixes with no performance impact.
  ```
- [`4747d7f`](https://github.com/ghostty-org/ghostty/commit/4747d7ff427480f75736dc207d14251b8eabd3c9) terminal: fix edge cases in carried page capacity ([#15005](https://github.com/ghostty-org/ghostty/issues/15005)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Found a few bugs from #14985:
  
  - The rows per byte check that decides whether a carried page may trim
  rows to fit in the pool overflowed on 32-bit targets (i.e. wasm32) for
  terminals narrower than about 37 columns.
  - `grow_hint` was updated before the new page was allocated. If
  allocation failed this caused problems.
  - On tall terminals at the minimum scrollback size, pages with trimmed
  rows hold less of the active area, so the page list could go over the
  byte limit during a burst of styled output.
  
  These are all correctness fixes with no performance impact.
  
  **AI stuff:** I found the first two issues, Fable found the last, Opus
  did the bug fixes and I reviewed.
  ```
- [`f7b25c8`](https://github.com/ghostty-org/ghostty/commit/f7b25c8129d84d53cf0cda4ffa024a692aca019e) termio: don't require RFC 1123 hostnames in OSC 7 ([@jcollie](https://github.com/jcollie))
  ```text
  The Zig 0.17 port switched reportPwd from `uri.getHost` to
  `std.Io.net.HostName.fromUri`, which also validates the host as an
  RFC 1123 hostname. Local hostnames often aren't: macOS allows names
  like "Foo's MacBook Pro", some systems use underscores, and our URI
  parser deliberately accepts MAC addresses. Any OSC 7 report from such
  a machine was dropped, so new tabs, splits and windows stopped
  inheriting the working directory.
  
  The host only has to match the local hostname, which `isLocal` already
  checks, so extract it without validating it, as 1.3 did.
  
  Fixes: #14970
  Ref: https://github.com/ghostty-org/ghostty/discussions/14952
  ```
- [`881fc68`](https://github.com/ghostty-org/ghostty/commit/881fc68902a5d819fdac96bcb597a2d99feb9729) terminal: skip clearing rows that are already blank ([@mitchellh](https://github.com/mitchellh))
  ```text
  Erase display (ED, `CSI J`) now skips rows that are already blank instead
  of clearing them again. On a mostly empty screen, full-screen erases are
  now 2x to 14x faster depending on screen size. Plain text and scrolling
  are unaffected.
  
  Programs that redraw by clearing (shells redrawing prompts, `clear`,
  `watch`, TUIs) usually erase a screen that is mostly empty already.
  Previously, every erase cleared every row cell by cell anyway, even
  when the cells were already zero.
  
  ## How
  
  Rows get a new `blank` bit, taken from the row's padding. It is set when
  a whole row is cleared with a zero blank cell and cleared by anything
  that writes cells. `clearRows` sees the bit and only resets the row's
  metadata, leaving the cells alone. Skipped rows aren't marked dirty
  because nothing about how they look changed.
  
  The bit is a hint that can be false for a blank row but never true for
  a row with content. We verify this with integrity checks.
  
  The tricky part was not slowing down printing. My first attempt cleared
  the bit whenever a row was marked dirty, which happens on every cursor
  move, and made scrolling about 3% slower. Now `writeCell` clears it,
  which also covers the spacer head a wide char writes before it wraps.
  `Row.markWritten` sets dirty and clears blank in one load and store,
  because doing them separately was measurable on the print path.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream`:
  
  | Input           | Size    | main (ms)    | blank-track (ms) | Speedup |
  | --------------- | ------- | ------------ | ---------------- | ------- |
  | erase.vt        | 120x80  | 362.6 ± 1.1  | 49.9 ± 0.1       | 7.27x   |
  | erase.vt        | 120x12  | 89.0 ± 0.3   | 49.0 ± 0.3       | 1.82x   |
  | erase.vt        | 300x100 | 1149 ± 16    | 82.6 ± 0.2       | 13.91x  |
  | ascii.vt        | 120x80  | 40.6 ± 0.2   | 40.5 ± 0.2       | 1.00x   |
  | styled-plain.vt | 120x80  | 64.1 ± 0.5   | 63.5 ± 0.5       | 1.01x   |
  | styled-mixed.vt | 120x80  | 576.0 ± 1.6  | 579.7 ± 5.9      | 0.99x   |
  | utf8.vt         | 120x80  | 380.5 ± 2.3  | 386.5 ± 6.5      | 0.98x   |
  | osc.vt          | 120x80  | 1142 ± 5     | 1140 ± 3         | 1.00x   |
  | out.txt (2.6GB) | 120x80  | 5911         | 5589             | 1.06x   |
  
  `out.txt` is the asciinema data dump, a real world workload. It gets
  faster because real sessions erase a lot! The vtebench vim inputs are
  1 to 2% faster for the same reason. The vtebench scrolling inputs are
  unchanged. utf8.vt looks 2% slower but it is noisy, and it executes
  only 0.3% more instructions, so this is probably noise.
  ```
- [`fd29936`](https://github.com/ghostty-org/ghostty/commit/fd29936f0914f5a303e1d67fd09201f981b7eff1) macos: make Surface main actor-isolated ([@jparise](https://github.com/jparise))
  ```text
  Calls into libghostty must happen on the main actor, and nearly every
  Surface function was already annotated with `@MainActor`.
  
  Main actor isolation makes the class implicitly Sendable, so the
  explicit conformance goes away. `deinit` remains `nonisolated`, so the
  surface handle stays `nonisolated(unsafe)` for it to read the value and
  hand it to the main actor to be freed.
  ```
- [`6573de6`](https://github.com/ghostty-org/ghostty/commit/6573de67e9990ebf0308f5cb07e4e40895d748ec) Replace std.ArrayListUnmanaged and std.ArrayListAligned ([@jcollie](https://github.com/jcollie))
  ```text
  Both are deprecated aliases in Zig 0.17: std.ArrayListUnmanaged is
  std.ArrayList, which has been unmanaged since 0.15, and
  std.ArrayListAligned is std.array_list.Aligned. Zig 0.18 removes them,
  so use the names they alias. No behavior change.
  ```
- [`2178e63`](https://github.com/ghostty-org/ghostty/commit/2178e635dffc71e0c679b143680665bf09857bb8) terminal: mark reset rows blank and test the blank bit bookkeeping ([@mitchellh](https://github.com/mitchellh))
- [`59093e3`](https://github.com/ghostty-org/ghostty/commit/59093e3aadb1478e6642061059b1882cfa1b6cf3) terminal: skip clearing rows that are already blank ([#14997](https://github.com/ghostty-org/ghostty/issues/14997)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Erase display (ED, `CSI J`) now skips rows that are already blank
  instead of clearing them again. On a mostly empty screen, full-screen
  erases are now 2x to 14x faster depending on screen size. Plain text and
  scrolling are unaffected.
  
  Programs that redraw by clearing (shells redrawing prompts, `clear`,
  `watch`, TUIs) usually erase a screen that is mostly empty already.
  Previously, every erase cleared every row cell by cell anyway, even when
  the cells were already zero.
  
  ## How
  
  Rows get a new `blank` bit, taken from the row's padding. It is set when
  a whole row is cleared with a zero blank cell and cleared by anything
  that writes cells. `clearRows` sees the bit and only resets the row's
  metadata, leaving the cells alone. Skipped rows aren't marked dirty
  because nothing about how they look changed.
  
  The bit is a hint that can be false for a blank row but never true for a
  row with content. We verify this with integrity checks.
  
  The tricky part was not slowing down printing. My first attempt cleared
  the bit whenever a row was marked dirty, which happens on every cursor
  move, and made scrolling about 3% slower. Now `writeCell` clears it,
  which also covers the spacer head a wide char writes before it wraps.
  `Row.markWritten` sets dirty and clears blank in one load and store,
  because doing them separately was measurable on the print path.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream`:
  
  | Input | Size | main (ms) | blank-track (ms) | Speedup |
  | --------------- | ------- | ------------ | ---------------- | -------
  |
  | erase.vt | 120x80 | 362.6 ± 1.1 | 49.9 ± 0.1 | 7.27x |
  | erase.vt | 120x12 | 89.0 ± 0.3 | 49.0 ± 0.3 | 1.82x |
  | erase.vt | 300x100 | 1149 ± 16 | 82.6 ± 0.2 | 13.91x |
  | ascii.vt | 120x80 | 40.6 ± 0.2 | 40.5 ± 0.2 | 1.00x |
  | styled-plain.vt | 120x80 | 64.1 ± 0.5 | 63.5 ± 0.5 | 1.01x |
  | styled-mixed.vt | 120x80 | 576.0 ± 1.6 | 579.7 ± 5.9 | 0.99x |
  | utf8.vt | 120x80 | 380.5 ± 2.3 | 386.5 ± 6.5 | 0.98x |
  | osc.vt | 120x80 | 1142 ± 5 | 1140 ± 3 | 1.00x |
  | out.txt (2.6GB) | 120x80 | 5911 | 5589 | 1.06x |
  
  `out.txt` is the asciinema data dump, a real world workload. It gets
  faster because real sessions erase a lot! The vtebench vim inputs are 1
  to 2% faster for the same reason. The vtebench scrolling inputs are
  unchanged. utf8.vt looks 2% slower but it is noisy, and it executes only
  0.3% more instructions, so this is probably noise.
  
  **AI usage:** I came up with the change, Opus helped with benchmarking
  and validating, I wrote the text. Fable helped come up with an alternate
  idea for my original design which had the 3% slowdown :(
  ```
- [`ada6e3d`](https://github.com/ghostty-org/ghostty/commit/ada6e3d722fde00e7171e2d4e93c7392052f2720) Replace std.ArrayListUnmanaged and std.ArrayListAligned ([#15001](https://github.com/ghostty-org/ghostty/issues/15001)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Both are deprecated aliases in Zig 0.17: std.ArrayListUnmanaged is
  std.ArrayList, which has been unmanaged since 0.15, and
  std.ArrayListAligned is std.array_list.Aligned. Zig 0.18 removes them,
  so use the names they alias. No behavior change.
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`5c6d43e`](https://github.com/ghostty-org/ghostty/commit/5c6d43eeecaf4eff506a96d0f5310b5682c80c88) macos: make Surface main actor-isolated ([#14999](https://github.com/ghostty-org/ghostty/issues/14999)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Calls into libghostty must happen on the main actor, and nearly every
  Surface function was already annotated with `@MainActor`.
  
  Main actor isolation makes the class implicitly Sendable, so the
  explicit conformance goes away. `deinit` remains `nonisolated`, so the
  surface handle stays `nonisolated(unsafe)` for it to read the value and
  hand it to the main actor to be freed.
  ```
- [`042b16b`](https://github.com/ghostty-org/ghostty/commit/042b16b6146ada29877dfeeea9f286889e4adeb1) termio: don't require RFC 1123 hostnames in OSC 7 ([#14971](https://github.com/ghostty-org/ghostty/issues/14971)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The Zig 0.17 port switched reportPwd from `uri.getHost` to
  `std.Io.net.HostName.fromUri`, which also validates the host as an RFC
  1123 hostname. Local hostnames often aren't: macOS allows names like
  "Foo's MacBook Pro", some systems use underscores, and our URI parser
  deliberately accepts MAC addresses. Any OSC 7 report from such a machine
  was dropped, so new tabs, splits and windows stopped inheriting the
  working directory.
  
  The host only has to match the local hostname, which `isLocal` already
  checks, so extract it without validating it, as 1.3 did.
  
  Fixes: #14970
  Ref: https://github.com/ghostty-org/ghostty/discussions/14952
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`7cd6fa0`](https://github.com/ghostty-org/ghostty/commit/7cd6fa0215a1299c69c27fe543f48ecab45b775f) Sync CODEOWNERS vouch list ([#15002](https://github.com/ghostty-org/ghostty/issues/15002)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Sync CODEOWNERS owners with vouch list.
  
  ## Added Users
  
  - @mangkoran
  ```

## November 1, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/41334104825), [2](https://github.com/ghostty-org/ghostty/actions/runs/41316706444), [3](https://github.com/ghostty-org/ghostty/actions/runs/41315316132), [4](https://github.com/ghostty-org/ghostty/actions/runs/41300698848), [5](https://github.com/ghostty-org/ghostty/actions/runs/41270777866), [6](https://github.com/ghostty-org/ghostty/actions/runs/41265367781), [7](https://github.com/ghostty-org/ghostty/actions/runs/41262969399)  
Summary: 7 runs • 13 commits • 5 authors

### Changes

- [`5e7714e`](https://github.com/ghostty-org/ghostty/commit/5e7714e71cd41ac0095aefa2120838842dfeca48) datastruct: prevent overflow in circular buffer arithmetic ([@12ya](https://github.com/12ya))
  ```text
  Check capacity growth and slice bounds before addition. Calculate
  wrapped indexes without overflowing intermediate sums and reuse the
  index calculation in the iterator.
  
  Add regression tests for capacity requests and index operations near
  the usize limit.
  ```
- [`0aa2f7c`](https://github.com/ghostty-org/ghostty/commit/0aa2f7caf52988bbfa42290cd3afbfbf550c0ef6) datastruct: use checked addition for buffer capacity ([@12ya](https://github.com/12ya))
  ```text
  #14987
  
  Use std.math.add to reject overflowing capacity requests while preserving the OutOfMemory error.
  ```
- [`c7eb3e8`](https://github.com/ghostty-org/ghostty/commit/c7eb3e8b96288e47e12f045056d270f8ba7f45f0) datastruct: restore circular buffer explanations ([@12ya](https://github.com/12ya))
  ```text
  #14987
  
  Restore iterator and head/tail explanations removed during overflow hardening. Describe saturating seeks and wrapping arithmetic accurately.
  ```
- [`a7e8e4d`](https://github.com/ghostty-org/ghostty/commit/a7e8e4d15bd0f12ad2a1123bf157b338e526c23e) datastruct: prevent overflow in circular buffer arithmetic ([#14987](https://github.com/ghostty-org/ghostty/issues/14987)) ([@jcollie](https://github.com/jcollie))
  ```text
  Check capacity growth and slice bounds before addition. Calculate
  wrapped indexes without overflowing intermediate sums and reuse the
  index calculation in the iterator.
  
  Add regression tests for capacity requests and index operations near the
  usize limit.
  
  AI disclosure: OpenAI Codex
  ```
- [`54d162d`](https://github.com/ghostty-org/ghostty/commit/54d162da5bea1d95399574495bde4ddb91df0784) terminal: apply every attribute of an SGR sequence at once ([@mitchellh](https://github.com/mitchellh))
  ```text
  An SGR sequence with several attributes, such as `CSI 0;1;38;5;100 m`,
  now updates the cursor style once after all of its attributes are
  applied.
  
  Previously, we applied per-attribute: 0, then 1, then 38, etc. Each forced
  a lookup, a hash, etc.
  
  Multi-attribute SGRs are common. Programs like Neovim, ncurses programs,
  btop, etc. In the 2.6 GB asciinema dump, about 9% of all SGR sequences
  are multi-attribute.
  
  ## How
  
  The action carries the whole sequence rather than keeping per-attribute
  actions and adding a trailing "end of sequence" marker. A handler that
  wants the old per-attribute view iterates `value.parser()`, and a
  handler that wants to batch gets the sequence boundary for free, with
  no state carried between actions.
  
  Unknown attributes are ignored silently in the app handler now, the
  same as libghostty-vt already did.
  
  There are no behavioral changes here.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream` at 120x80:
  
  | Input           | main (ms)   | sgr-multi (ms) | Speedup |
  | --------------- | ----------- | -------------- | ------- |
  | styled-multi.vt | 367.7 ± 0.8 | 233.7 ± 0.6    | 1.57x   |
  | out.txt (2.6GB) | 5929 ± 26   | 5679 ± 8       | 1.04x   |
  | styled-heavy.vt | 238.7 ± 0.8 | 231.5 ± 0.8    | 1.03x   |
  | styled-mixed.vt | 573.9 ± 1.9 | 571.3 ± 2.3    | 1.00x   |
  | osc.vt          | 1124 ± 7    | 1119 ± 3       | 1.00x   |
  | utf8.vt         | 379.1 ± 1.5 | 378.5 ± 1.2    | 1.00x   |
  | styled-plain.vt | 64.2 ± 0.4  | 64.2 ± 0.4     | 1.00x   |
  | ascii.vt        | 40.3 ± 0.2  | 40.3 ± 0.2     | 1.00x   |
  
  Importantly: normal non-SGR workloads are unaffected.
  ```
- [`2f967e3`](https://github.com/ghostty-org/ghostty/commit/2f967e3a6ab231188c29a97fb422e479a254e97c) terminal: apply every attribute of an SGR sequence at once ([#14995](https://github.com/ghostty-org/ghostty/issues/14995)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  An SGR sequence with several attributes, such as `CSI 0;1;38;5;100 m`,
  now updates the cursor style once after all of its attributes are
  applied.
  
  Previously, we applied per-attribute: 0, then 1, then 38, etc. Each
  forced a lookup, a hash, etc.
  
  Multi-attribute SGRs are common. Programs like Neovim, ncurses programs,
  btop, etc. In the 2.6 GB asciinema dump, about 9% of all SGR sequences
  are multi-attribute.
  
  ## How
  
  The action carries the whole sequence rather than keeping per-attribute
  actions and adding a trailing "end of sequence" marker. A handler that
  wants the old per-attribute view iterates `value.parser()`, and a
  handler that wants to batch gets the sequence boundary for free, with no
  state carried between actions.
  
  Unknown attributes are ignored silently in the app handler now, the same
  as libghostty-vt already did.
  
  There are no behavioral changes here.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream` at 120x80:
  
  | Input           | main (ms)   | sgr-multi (ms) | Speedup |
  | --------------- | ----------- | -------------- | ------- |
  | styled-multi.vt | 367.7 ± 0.8 | 233.7 ± 0.6    | 1.57x   |
  | out.txt (2.6GB) | 5929 ± 26   | 5679 ± 8       | 1.04x   |
  | styled-heavy.vt | 238.7 ± 0.8 | 231.5 ± 0.8    | 1.03x   |
  | styled-mixed.vt | 573.9 ± 1.9 | 571.3 ± 2.3    | 1.00x   |
  | osc.vt          | 1124 ± 7    | 1119 ± 3       | 1.00x   |
  | utf8.vt         | 379.1 ± 1.5 | 378.5 ± 1.2    | 1.00x   |
  | styled-plain.vt | 64.2 ± 0.4  | 64.2 ± 0.4     | 1.00x   |
  | ascii.vt        | 40.3 ± 0.2  | 40.3 ± 0.2     | 1.00x   |
  
  Importantly: normal non-SGR workloads are unaffected.
  
  **AI usage:** My normal: I came up with the change, Opus helped with
  benchmarking and validating, I wrote the text.
  ```
- [`a3e349f`](https://github.com/ghostty-org/ghostty/commit/a3e349f7a02709130d4cb83b24bac56a5d334d52) i18n: update Bahasa Indonesia translation ([#14991](https://github.com/ghostty-org/ghostty/issues/14991)) ([@clavinjune](https://github.com/clavinjune))
- [`a5b4403`](https://github.com/ghostty-org/ghostty/commit/a5b44039d10f25d2d0a5992137cd6517f49e72aa) Update VOUCHED list ([#14992](https://github.com/ghostty-org/ghostty/issues/14992)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14991#issuecomment-6557130969)
  from @trag1c.
  
  Vouch: @clavinjune
  ```
- [`a3b5946`](https://github.com/ghostty-org/ghostty/commit/a3b5946a59b94bf097da1aac889cf95f9c704675) terminal: new pages keep the capacity recent pages needed ([@mitchellh](https://github.com/mitchellh))
  ```text
  **Headline performance number:** all data shapes other than plain-text
  is anywhere from 20% to 380% faster. Plain text is unaffected.
  
  `PageList.grow` now gives a new page the style, grapheme, string, and
  hyperlink capacity that the last two full pages needed, instead of
  always starting over from the standard capacity.
  
  Previously, every `grow` would allocate a new standard sized page and
  force the caller to call repeat `increaseCapacity` calls as needed. For
  similar data shapes, this would force a LOT of page copies and
  allocations.
  
  ## How
  
  So, I've tried this a few times before! And I've failed multiple times
  to get the right mix of logic to make this speedup the benchmarks but
  NOT regress standard workloads.
  
  I think I've got it this time though. Well, I know I have something
  because the benchmarks show it.
  
  The way it works: when we need to grow a new page, we keep the capacity
  of any managed dimension (style, grapheme, etc.) so long as 1/3rd of it
  is actually utilized. Otherwise, we shrink it back to standard size or
  1.5x what was used, whichever is BIGGER (so, it leans towards similar
  data). After that, we raise all dimensions to what the page _before_
  used, so that it takes _two full pages_ of low utilization to start
  shrinking.
  
  **We call these "carried pages," since the usage is carried forward.**
  
  If a carried page is larger than a pooled memory size, we shrink rows so
  that it fits in the pool. If we can't do this reasonably, we heap
  allocate but we try very hard to avoid this.
  ## Benchmarks
  
  `ghostty-bench +terminal-stream` at 120x80:
  
  | Input           | main (ms)     | page-grow (ms) | Speedup |
  | --------------- | ------------- | -------------- | ------- |
  | styled-mixed.vt | 2284.1 ± 43.6 | 611.3 ± 1.3    | 3.74x   |
  | osc.vt          | 2616.3 ± 25.6 | 1173.7 ± 4.8   | 2.23x   |
  | burst.vt        | 250.3 ± 12.8  | 90.6 ± 0.7     | 2.76x   |
  | alternating.vt  | 443.9 ± 11.2  | 123.4 ± 4.4    | 3.60x   |
  | hyperlinks.vt   | 211.1 ± 5.6   | 55.1 ± 1.7     | 3.83x   |
  | styled-heavy.vt | 301.7 ± 1.4   | 246.0 ± 1.1    | 1.23x   |
  | utf8.vt         | 439.1 ± 2.0   | 385.6 ± 0.8    | 1.14x   |
  | ascii.vt        | 42.5 ± 0.6    | 42.0 ± 0.2     | 1.01x   |
  | styled-plain.vt | 65.7 ± 0.4    | 65.7 ± 0.4     | 1.00x   |
  | erase.vt        | 362.9 ± 4.2   | 372.4 ± 4.4    | 0.97x   |
  | out.txt (2.6GB) | 5857 ± 13     | 5922 ± 31      | 0.99x   |
  
  `out.txt` is the asciinema data dump. It is unaffected because diverse,
  heterogenous data (honestly, real world workloads!) don't behave this
  way. But because of that, its important to see that its all the same!
  
  It's important to note that while `out.txt` looks 1% slower, CPU metrics
  point to less instructions executed, less memory copies (2105 page
  copies instead of 2270, 1838 heap pages instead of 1934). So this is
  probably noise.
  
  Homogenous data is often used for benchmarks, and quite frankly I'm
  tired of people pointing out stuff like pure-SGR streams being very slow
  in Ghostty. So, this fixes that while not affecting normal workloads.
  ```
- [`dc8f599`](https://github.com/ghostty-org/ghostty/commit/dc8f59943ce94b75ffadc45cc4f36eca6a7ed2ae) terminal: new pages keep the capacity recent pages needed ([#14985](https://github.com/ghostty-org/ghostty/issues/14985)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  **Headline performance number:** all streams of heavily loaded
  homogeneous data shapes other than plain-text is anywhere from 20% to
  380% faster. Plain text is unaffected.
  
  `PageList.grow` now gives a new page the style, grapheme, string, and
  hyperlink capacity that the last two full pages needed, instead of
  always starting over from the standard capacity.
  
  Previously, every `grow` would allocate a new standard sized page and
  force the caller to call repeat `increaseCapacity` calls as needed. For
  similar data shapes, this would force a LOT of page copies and
  allocations.
  
  ## How
  
  So, I've tried this a few times before! And I've failed multiple times
  to get the right mix of logic to make this speedup the benchmarks but
  NOT regress standard workloads.
  
  I think I've got it this time though. Well, I know I have something
  because the benchmarks show it.
  
  The way it works: when we need to grow a new page, we keep the capacity
  of any managed dimension (style, grapheme, etc.) so long as 1/3rd of it
  is actually utilized. Otherwise, we shrink it back to standard size or
  1.5x what was used, whichever is BIGGER (so, it leans towards similar
  data). After that, we raise all dimensions to what the page _before_
  used, so that it takes _two full pages_ of low utilization to start
  shrinking.
  
  **We call these "carried pages," since the usage is carried forward.**
  
  If a carried page is larger than a pooled memory size, we shrink rows so
  that it fits in the pool. If we can't do this reasonably, we heap
  allocate but we try very hard to avoid this.
  ## Benchmarks
  
  `ghostty-bench +terminal-stream` at 120x80:
  
  | Input           | main (ms)     | page-grow (ms) | Speedup |
  | --------------- | ------------- | -------------- | ------- |
  | styled-mixed.vt | 2284.1 ± 43.6 | 611.3 ± 1.3    | 3.74x   |
  | osc.vt          | 2616.3 ± 25.6 | 1173.7 ± 4.8   | 2.23x   |
  | burst.vt        | 250.3 ± 12.8  | 90.6 ± 0.7     | 2.76x   |
  | alternating.vt  | 443.9 ± 11.2  | 123.4 ± 4.4    | 3.60x   |
  | hyperlinks.vt   | 211.1 ± 5.6   | 55.1 ± 1.7     | 3.83x   |
  | styled-heavy.vt | 301.7 ± 1.4   | 246.0 ± 1.1    | 1.23x   |
  | utf8.vt         | 439.1 ± 2.0   | 385.6 ± 0.8    | 1.14x   |
  | ascii.vt        | 42.5 ± 0.6    | 42.0 ± 0.2     | 1.01x   |
  | styled-plain.vt | 65.7 ± 0.4    | 65.7 ± 0.4     | 1.00x   |
  | erase.vt        | 362.9 ± 4.2   | 372.4 ± 4.4    | 0.97x   |
  | out.txt (2.6GB) | 5857 ± 13     | 5922 ± 31      | 0.99x   |
  
  `out.txt` is the asciinema data dump. It is unaffected because diverse,
  heterogenous data (honestly, real world workloads!) don't behave this
  way. But because of that, its important to see that its all the same!
  
  It's important to note that while `out.txt` looks 1% slower, CPU metrics
  point to less instructions executed, less memory copies (2105 page
  copies instead of 2270, 1838 heap pages instead of 1934). So this is
  probably noise.
  
  Homogenous data is often used for benchmarks, and quite frankly I'm
  tired of people pointing out stuff like pure-SGR streams being very slow
  in Ghostty. So, this fixes that while not affecting normal workloads.
  
  **AI usage:** I've done the laddering before so I did a NUMBER of messy
  passes. I had Opus running benchmarks for each of my attempts. I think I
  tried 6 or 7 different logical choices before settling on this. Fable
  chased down the alignment issue in the benchmark (cause I was seeing
  like a consistent 4% slowdown in vtebench dense cells but it didn't make
  sense to me because this codepath didn't get touched!). I wrote this
  whole PR message.
  ```
- [`845736e`](https://github.com/ghostty-org/ghostty/commit/845736e1df59e637a614aee78009217c9b480988) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`2fc8d02`](https://github.com/ghostty-org/ghostty/commit/2fc8d02c253bc09ff7456c65e7f63dd6eebaf4de) Update iTerm2 colorschemes ([#14981](https://github.com/ghostty-org/ghostty/issues/14981)) ([@jcollie](https://github.com/jcollie))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20261026-153024-27cbbb5
  ```
- [`c42f6fb`](https://github.com/ghostty-org/ghostty/commit/c42f6fb4740102b678773f4bfdd4ef7613afe818) Update VOUCHED list ([#14983](https://github.com/ghostty-org/ghostty/issues/14983)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14982#discussioncomment-19325417)
  from @jcollie.
  
  Vouch: @cammeresi
  ```

## October 31, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/41244998361), [2](https://github.com/ghostty-org/ghostty/actions/runs/41221492187), [3](https://github.com/ghostty-org/ghostty/actions/runs/41208691947), [4](https://github.com/ghostty-org/ghostty/actions/runs/41167071786), [5](https://github.com/ghostty-org/ghostty/actions/runs/41160759341), [6](https://github.com/ghostty-org/ghostty/actions/runs/41159681318)  
Summary: 6 runs • 11 commits • 5 authors

### Changes

- [`c7be56a`](https://github.com/ghostty-org/ghostty/commit/c7be56a04696249a2c33abac88586338aba7fc7a) fuzz: exercise hierarchical context in osc harness ([@paaloeye](https://github.com/paaloeye))
  ```text
  The OSC fuzzer harness previously discarded the parsed command returned
  by the OSC parser without evaluating lazily parsed metadata. **OSC 3008**
  hierarchical context sequences parse metadata fields on demand through
  readOption, leaving option parsing, type conversions, and unescaping
  unexercised by the fuzzer.
  
  When a hierarchical context command is produced, query every defined
  context field to fuzz option extraction and validation. For string
  fields with escape sequences, exercise both the streaming character
  iterator and heap-allocated decoding paths. Seed inputs for **OSC 3008** in
  the initial and minimized corpora are updated with escaped metadata.
  
  Also align the fuzzer package minimum Zig version with the root build
  and pass the target macOS deployment version and `-Wno-override-module`
  to afl-cc to silence target triple and linker version mismatch warnings.
  
  AI disclosure: AI helped to discover AFL++ args and drafted this commit message.
  
  Spec: https://github.com/uapi-group/specifications/blob/5e61460b42b91bb1e402b50a6149774d78fc0d8e/specs/osc_context.md
  Assited-By: Gemini 4 Argon (Medium)
  Assited-By: Antigravity CLI 1.3.5
  Agent-Session: 0c644e81-47c4-4768-95ee-5660020523dd
  ```
- [`83b57ac`](https://github.com/ghostty-org/ghostty/commit/83b57ac5ead868e133adb509f7ef0a4ffa3ffe01) fuzz: exercise hierarchical context in osc harness ([#14977](https://github.com/ghostty-org/ghostty/issues/14977)) ([@jcollie](https://github.com/jcollie))
  ```text
  The OSC fuzzer harness previously discarded the parsed command returned
  by the OSC parser without evaluating lazily parsed metadata. **OSC
  3008** hierarchical context sequences parse metadata fields on demand
  through `readOption`, leaving option parsing, type conversions, and
  unescaping unexercised by the fuzzer.
  
  When a hierarchical context command is produced, query every defined
  context field to fuzz option extraction and validation. Seed inputs for
  **OSC 3008** in the initial and minimized corpora are updated with
  escaped metadata.
  
  Also align the fuzzer package minimum Zig version with the root build
  and pass the target macOS deployment version and `-Wno-override-module`
  to `afl-cc` to silence target triple and linker version mismatch
  warnings.
  
  AI disclosure: AI helped to discover AFL++ args and drafted this commit
  message.
  
  Spec:
  https://github.com/uapi-group/specifications/blob/5e61460b42b91bb1e402b50a6149774d78fc0d8e/specs/osc_context.md
  ```
- [`b01ca00`](https://github.com/ghostty-org/ghostty/commit/b01ca003ca76687072b1cac6f1e3dd1bd0e27fa5) benchmark: add shaper-rows benchmark ([@AryanHamedani](https://github.com/AryanHamedani))
  ```text
  Measures turning terminal rows into text runs (`--mode=runs`) and
  shaping them (`--mode=shape`), which the renderer does for every dirty
  row on every frame. Shaped runs are cached by the renderer but run
  iteration is not, so `runs` isolates the per-frame cost a cache can't
  hide. The data file fills a screen during setup, which is not timed.
  ```
- [`1461f06`](https://github.com/ghostty-org/ghostty/commit/1461f068745a4b9524e197a38a876072a9a220f0) benchmark: end a shaper frame after each shaper-rows pass ([@AryanHamedani](https://github.com/AryanHamedani))
  ```text
  CoreText shapers keep CoreFoundation objects in a release pool until
  endFrame(). The renderer calls it once per frame, so do the same once
  per pass instead of letting every pass accumulate in the pool.
  ```
- [`3bd54e0`](https://github.com/ghostty-org/ghostty/commit/3bd54e025cc3349ee76ab1af7ec1ff8f7353632b) benchmark: add shaper-rows benchmark ([#14965](https://github.com/ghostty-org/ghostty/issues/14965)) ([@jcollie](https://github.com/jcollie))
  ```text
  Adds `ghostty-bench +shaper-rows`, as suggested in
  https://github.com/ghostty-org/ghostty/pull/11079#issuecomment-6524841018.
  
  None of the existing benchmarks cover the font shaper. This one fills a
  screen from `--data` during setup, which isn't timed, and then makes
  `--iterations` passes (default 200) over every row:
  
  - `--mode=runs` only splits rows into text runs. The renderer does this
  for every dirty row on every frame, and unlike shaping it isn't cached,
  so this shows the per-frame cost.
  - `--mode=shape` also shapes each run.
  
  It uses the embedded Inconsolata face with the embedded Arabic face as
  fallback, so RTL input gets shaped by a real font. Terminal size is
  `--terminal-rows`/`--terminal-cols` (80x120), same as `screen-clone`.
  
  On main (Linux, HarfBuzz, ReleaseFast), with hyperfine, 10 runs each:
  
  | data | runs | shape |
  |---|---|---|
  | 2000 lines of `src/terminal/Terminal.zig` | 34.7 ms ±1.0 | 84.3 ms
  ±2.0 |
  | 2000 lines of Persian prose | 58.2 ms ±3.2 | 246.7 ms ±12.7 |
  
  On #11079 it picked up a 2x slowdown in `runs` on plain ASCII.
  
  *AI disclosure: I used Claude Code to write and port this benchmark and
  to draft this description. I've read the code and can explain it, and I
  ran the numbers above myself.*
  ```
- [`ce92029`](https://github.com/ghostty-org/ghostty/commit/ce920296c891d0f9e266cfb908057716304182ab) terminal: skip the ED2 prompt scan when OSC 133 was never seen ([@mitchellh](https://github.com/mitchellh))
  ```text
  Full-screen `eraseDisplay` now skips finding the last prompt line when
  we haven't seen semantic prompts. For screens without OSC133,
  full-screen erases are now ~2x faster.
  
  Programs that redraw by clearing the screen (TUIs, `watch`, etc.)
  would hit this unnecessary path every clear because they never emit
  OSC133.
  
  This also adds a `+erase` generator to `ghostty-gen` that produces a
  stream of full-screen clears and cursor movement to simulate
  pathological inputs that hit this optimization.
  
  `ghostty-bench +terminal-stream`:
  
  | Input           | Size    | main (ms)     | erase-opt (ms) | Speedup |
  | --------------- | ------- | ------------- | -------------- | ------- |
  | erase.vt        | 120x80  | 748.7 ± 51.6  | 421.8 ± 6.2    | 1.78x   |
  | erase.vt        | 120x12  | 114.0 ± 2.4   | 102.5 ± 1.1    | 1.11x   |
  | erase.vt        | 300x100 | 2597.1 ± 54.1 | 1227.0 ± 14.2  | 2.12x   |
  | ascii.vt        | 120x80  | 45.7 ± 0.3    | 45.8 ± 0.3     | 1.00x   |
  | styled-plain.vt | 120x80  | 70.4 ± 0.4    | 69.9 ± 0.6     | 1.01x   |
  | styled-heavy.vt | 120x80  | 311.9 ± 7.0   | 313.5 ± 6.9    | 0.99x   |
  | utf8.vt         | 120x80  | 473.1 ± 4.5   | 476.9 ± 5.3    | 0.99x   |
  | osc.vt          | 120x80  | 2770 ± 30     | 2726 ± 25      | 1.02x   |
  
  This also fixes a couple places where we wern't properly setting
  `seen`.
  ```
- [`9bfa8ee`](https://github.com/ghostty-org/ghostty/commit/9bfa8ee9a1d73f99208c1f056c4e4b5783402ead) terminal: skip the ED2 prompt scan when OSC 133 was never seen ([#14975](https://github.com/ghostty-org/ghostty/issues/14975)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Full-screen `eraseDisplay` now skips finding the last prompt line when
  we haven't seen semantic prompts. For screens without OSC133,
  full-screen erases are now ~2x faster.
  
  Programs that redraw by clearing the screen (TUIs, `watch`, etc.) would
  hit this unnecessary path every clear because they never emit OSC133.
  
  This also adds a `+erase` generator to `ghostty-gen` that produces a
  stream of full-screen clears and cursor movement to simulate
  pathological inputs that hit this optimization.
  
  This also fixes a couple places where we wern't properly setting `seen`.
  
  `ghostty-bench +terminal-stream`:
  
  | Input           | Size    | main (ms)     | erase-opt (ms) | Speedup |
  | --------------- | ------- | ------------- | -------------- | ------- |
  | erase.vt        | 120x80  | 748.7 ± 51.6  | 421.8 ± 6.2    | 1.78x   |
  | erase.vt        | 120x12  | 114.0 ± 2.4   | 102.5 ± 1.1    | 1.11x   |
  | erase.vt        | 300x100 | 2597.1 ± 54.1 | 1227.0 ± 14.2  | 2.12x   |
  | ascii.vt        | 120x80  | 45.7 ± 0.3    | 45.8 ± 0.3     | 1.00x   |
  | styled-plain.vt | 120x80  | 70.4 ± 0.4    | 69.9 ± 0.6     | 1.01x   |
  | styled-heavy.vt | 120x80  | 311.9 ± 7.0   | 313.5 ± 6.9    | 0.99x   |
  | utf8.vt         | 120x80  | 473.1 ± 4.5   | 476.9 ± 5.3    | 0.99x   |
  | osc.vt          | 120x80  | 2770 ± 30     | 2726 ± 25      | 1.02x   |
  
  The benchmarks most importantly show not just the speedup but that
  existing data shapes are unaffected.
  
  **AI disclosure:** Fable found the slowdown cause (reported by a
  libghostty user), I fixed it, Fable+Opus validated my work and found a
  couple bugs (e.g. missing setting `seen` in cursor copy and snapshot).
  Opus wrote the synthetic generator and ran the benchmarks. I wrote all
  the comments and this PR body.
  ```
- [`51e7fe5`](https://github.com/ghostty-org/ghostty/commit/51e7fe51db607773a651b161527beb10ce92a611) terminal/tmux: parse %output without a regex ([@jcollie](https://github.com/jcollie))
  ```text
  Parse `%output %<pane> <data>` by hand instead of compiling an
  Oniguruma regex for every pane write, matching how %window-close and
  %session-window-changed are already parsed.
  
  The pane id now goes through parseDecimalId, so an id that overflows
  usize is logged and dropped rather than hitting `catch unreachable`.
  Empty data is accepted rather than rejected.
  
  The data is sliced from the line directly rather than through
  std.mem.cutPrefix, which returns a const slice, so that it keeps the
  mutability of the parser buffer it points into.
  ```
- [`ae0dc1b`](https://github.com/ghostty-org/ghostty/commit/ae0dc1b7136c2baddc3e067663aa041cd555cfda) terminal/tmux: parse %output without a regex ([#14947](https://github.com/ghostty-org/ghostty/issues/14947)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Parse `%output %<pane> <data>` by hand instead of compiling an Oniguruma
  regex for every pane write, matching how %window-close and
  %session-window-changed are already parsed.
  
  The pane id now goes through parseDecimalId, so an id that overflows
  usize is logged and dropped rather than hitting `catch unreachable`.
  Empty data is accepted rather than rejected.
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`c911f96`](https://github.com/ghostty-org/ghostty/commit/c911f96ee8fedd4594b5b69f1128fcb03f560622) Update VOUCHED list ([#14969](https://github.com/ghostty-org/ghostty/issues/14969)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14963#discussioncomment-19307157)
  from @jcollie.
  
  Vouch: @hamidp
  ```
- [`0a672a9`](https://github.com/ghostty-org/ghostty/commit/0a672a914479354aa8599c75927485b22905c394) Update VOUCHED list ([#14968](https://github.com/ghostty-org/ghostty/issues/14968)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14964#discussioncomment-19306948)
  from @jcollie.
  
  Vouch: @edsarmiento
  ```

## October 30, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/41126163986), [2](https://github.com/ghostty-org/ghostty/actions/runs/41124653536), [3](https://github.com/ghostty-org/ghostty/actions/runs/41119470525), [4](https://github.com/ghostty-org/ghostty/actions/runs/41115877636), [5](https://github.com/ghostty-org/ghostty/actions/runs/41105956349), [6](https://github.com/ghostty-org/ghostty/actions/runs/41088392462), [7](https://github.com/ghostty-org/ghostty/actions/runs/41066122923), [8](https://github.com/ghostty-org/ghostty/actions/runs/41009687911), [9](https://github.com/ghostty-org/ghostty/actions/runs/40999068173), [10](https://github.com/ghostty-org/ghostty/actions/runs/40992707017)  
Summary: 10 runs • 30 commits • 9 authors

### Changes

- [`8bb4f45`](https://github.com/ghostty-org/ghostty/commit/8bb4f45846ecde0ab53a846ee1bca5533dca8c5f) fuzz: fix replay crash detection and add osc target ([@paaloeye](https://github.com/paaloeye))
- [`a0706b7`](https://github.com/ghostty-org/ghostty/commit/a0706b79b3d791873177b1fda4b155267769e8c5) fuzz: fix replay crash detection and add osc target ([#14896](https://github.com/ghostty-org/ghostty/issues/14896)) ([@jcollie](https://github.com/jcollie))
  ```text
  In Nushell, running an external command that exits successfully returns
  stdout as an empty string. The previous error check tested whether the
  result was not `null`, which always evaluated to `true` for clean exits.
  
  Use the `complete` command to inspect the process exit code.
  
  Additionally, add "osc" to the default list of fuzzers so OSC crashes
  are replayed by default.
  
  Ref: https://www.nushell.sh/commands/docs/complete.html
  ```
- [`fbed180`](https://github.com/ghostty-org/ghostty/commit/fbed180a5f181915c92a8f2f561903a6e4645b5a) Update VOUCHED list ([#14960](https://github.com/ghostty-org/ghostty/issues/14960)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14959#discussioncomment-19301732)
  from @jcollie.
  
  Vouch: @AryanHamedani
  ```
- [`4d7de0a`](https://github.com/ghostty-org/ghostty/commit/4d7de0a483e40e2c1dc542315b2a87be96977df2) fix(ssh): show authentication messages during terminfo setup ([@clinta](https://github.com/clinta))
  ```text
  Suppressing SSH stderr hid keyboard-interactive login instructions.
  Inherit it instead; installer output remains suppressed by default.
  ```
- [`9644c75`](https://github.com/ghostty-org/ghostty/commit/9644c7571d43f988415b3ed38f40be76e5964dd4) datastruct: fix clearing circular buffers with zero capacity ([@12ya](https://github.com/12ya))
  ```text
  Keep buffers with zero capacity marked full after clear(), so append()
  returns error.OutOfMemory instead of panicking.
  
  Add a regression test for this case.
  ```
- [`f040f0a`](https://github.com/ghostty-org/ghostty/commit/f040f0ab0ee30d77794b98d87e27fc9105ee6ab9) datastruct: fix clearing circular buffers with zero capacity ([#14958](https://github.com/ghostty-org/ghostty/issues/14958)) ([@jcollie](https://github.com/jcollie))
  ```text
  Keep buffers with zero capacity marked full after clear(), so append()
  returns error.OutOfMemory instead of panicking.
  
  Add a regression test for this case.
  
  AI disclosure: OpenAI Codex
  ```
- [`4489314`](https://github.com/ghostty-org/ghostty/commit/44893148d009bd372f5f7e8d2edbd0340fc82b65) cli: show SSH authentication messages during terminfo setup ([#14916](https://github.com/ghostty-org/ghostty/issues/14916)) ([@jcollie](https://github.com/jcollie))
  ```text
  `+ssh` suppresses stderr during terminfo setup. OpenSSH still displays
  authentication prompts through `/dev/tty`, but accompanying
  informational messages from custom SSH servers are hidden. This can make
  authentication appear to stall.
  
  Inherit SSH stderr without disabling interactive authentication.
  Installer output remains suppressed by default, and `--verbose` behavior
  is preserved. SSH warnings and login banners can now also appear during
  setup.
  
  Tested with 114 focused SSH tests and nine real OpenSSH scenarios
  covering keyboard-interactive setup and login, the Bash shell wrapper,
  installation, fallback, caching, environment forwarding, and exit-status
  propagation.
  
  Oh-My-Pi using GPT-6.1 Sol assisted with diagnosis, implementation,
  validation, and drafting this change.
  ```
- [`32da5e4`](https://github.com/ghostty-org/ghostty/commit/32da5e47b26cad0dadb36c279ae9e020a2e60959) snap: avoid trailing colon in LD_LIBRARY_PATH ([@12ya](https://github.com/12ya))
  ```text
  Add the separator only when appending a nonempty inherited path.
  A trailing colon adds the working directory to library lookup,
  which can make launcher commands load a conflicting local library
  and fail before Ghostty starts.
  ```
- [`1d23d02`](https://github.com/ghostty-org/ghostty/commit/1d23d02ae16f86d9c9a3792098cb906b94208bcc) snap: avoid trailing colon in LD_LIBRARY_PATH ([#14954](https://github.com/ghostty-org/ghostty/issues/14954)) ([@jcollie](https://github.com/jcollie))
  ```text
  Add the separator only when appending a nonempty inherited path. A
  trailing colon adds the working directory to library lookup, which can
  make launcher commands load a conflicting local library and fail before
  Ghostty starts.
  
  Verified with the extracted Ghostty 1.4.0 ARM64 Snap in Docker:
  the original launcher exits 127 with an empty libc.so.6 in the
  working directory, while the corrected launcher exits 0.
  
  I intended to open an issue documenting this investigation, but
  issue creation is restricted. I can provide the Docker commands
  used to reproduce the failure in the follow up comments instead.
  
  
  AI disclosure: OpenAI Codex assisted with investigating the issue,
  proposing the fix, running Docker reproductions, reviewing the
  change, and drafting this commit message.
  ```
- [`93404a4`](https://github.com/ghostty-org/ghostty/commit/93404a48a9a8bf265bb1671e0e6d9985322f6682) Update VOUCHED list ([#14957](https://github.com/ghostty-org/ghostty/issues/14957)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14956#discussioncomment-19300741)
  from @jcollie.
  
  Vouch: @yeager
  ```
- [`86c704a`](https://github.com/ghostty-org/ghostty/commit/86c704afdde5a8ee67300d924d1c52b4d82b4ff4) gtk: fix jumps when resizing splits via keybind ([@dkinzler](https://github.com/dkinzler))
  ```text
  `syncSplitRatio` now exits early if GTK size allocation has not yet
  computed a value for the `max-position` property of the `GtkPaned`
  widget. Initially `max-position` has the max value for a `c_int`, so
  that calculations in the function would overflow and set the split ratio
  to 0. This could happen when resizing a split multiple times by holding
  down a keybind.
  ```
- [`ca91d0a`](https://github.com/ghostty-org/ghostty/commit/ca91d0a24e67b3eecdb23c943227cd2b3908747b) gtk: fix jumps when resizing splits via keybind ([#14951](https://github.com/ghostty-org/ghostty/issues/14951)) ([@jcollie](https://github.com/jcollie))
  ```text
  `syncSplitRatio` now exits early if GTK size allocation has not yet
  computed a value for the `max-position` property of the `GtkPaned`
  widget. Initially `max-position` has the max value for a `c_int`, so
  that calculations in the function would overflow and set the split ratio
  to 0. This could happen when resizing a split multiple times by holding
  down a keybind.
  
  Fixes a regression introduced by #14476 where the split ratio sometimes
  jumps to the minimum when holding down the resize keybind. See the video
  below. When `syncSplitRatio` is called from `SplitTree.resize` it is not
  guaranteed that the `GtkPaned` widget has already been size allocated.
  This can happen with many resizes in a short time because the `GtkPaned`
  widget is rebuilt on every one.
  
  
  https://github.com/user-attachments/assets/442adf44-3a1c-41ee-bdc4-aa971848893e
  ```
- [`90ed851`](https://github.com/ghostty-org/ghostty/commit/90ed851dea8a7f328ad937adc5521c809f2cd41d) config: ignore repeated space in direct commands ([@12ya](https://github.com/12ya))
  ```text
  Repeated spaces in direct: commands produced empty arguments.
  Use tokenizeScalar to skip those empty fields and add a regression
  case for repeated spaces between arguments.
  ```
- [`e2593c1`](https://github.com/ghostty-org/ghostty/commit/e2593c1496cbf9f34f13e53d2d83b80283c8f24f) config: ignore repeated space in direct commands ([#14950](https://github.com/ghostty-org/ghostty/issues/14950)) ([@jcollie](https://github.com/jcollie))
  ```text
  Repeated spaces in direct: commands produced empty arguments. Use
  tokenizeScalar to skip those empty fields and add a regression case for
  repeated spaces between arguments.
  
  
  follow up to https://github.com/ghostty-org/ghostty/pull/14921
  ```
- [`854e514`](https://github.com/ghostty-org/ghostty/commit/854e51422732c00088ceb79b09a61e504b89800d) snap: bundle gstreamer plugins so audio bell works ([@aaron-ang](https://github.com/aaron-ang))
  ```text
  When `bell-features = audio` is enabled, GTK plays the bell through its
  GStreamer media backend. GTK links GStreamer itself, but GStreamer also
  needs playback, decode and audio sink plugins to build a pipeline, and
  the snap ships none of them, so the bell silently fails to play.
  
  Stage gstreamer1.0-plugins-base/-good/-pulseaudio for the decode and
  audio sink pipeline (typefind, playbin/decodebin, vorbis, audioconvert,
  autoaudiosink, pulsesink). In the launcher, export
  GST_PLUGIN_SYSTEM_PATH, GST_PLUGIN_SCANNER and GST_REGISTRY so
  GStreamer finds the bundled plugins and keeps a per-user registry cache
  under SNAP_USER_COMMON, and unset GST_PLUGIN_PATH plus the `_1_0`
  variants so host settings can't override the bundled paths.
  ```
- [`ff23824`](https://github.com/ghostty-org/ghostty/commit/ff23824213b8d7ab7a07dca6a7e0d68cad51b802) snap: bundle gstreamer plugins so audio bell works ([#12676](https://github.com/ghostty-org/ghostty/issues/12676)) ([@jcollie](https://github.com/jcollie))
  ```text
  ## Summary
  
  With `bell-features = audio` and a valid `bell-audio-path` configured,
  no sound plays in the snap build of Ghostty.
  
  On core26, GTK links GStreamer directly. GStreamer still needs playback,
  decode and audio-sink plugins to build a pipeline, and the snap ships
  none of them, so the bell fails silently.
  
  `bell-features = system` (the compositor sound, via
  `gdk_surface_beep()`) already works and is unchanged.
  
  ## Fix
  
  - Stage `gstreamer1.0-plugins-base`, `gstreamer1.0-plugins-good` and
  `gstreamer1.0-pulseaudio`. This gives the snap `typefind`,
  `playbin`/`decodebin`, `ogg`, `vorbis`, `audioconvert`, `autoaudiosink`,
  `pulsesink`, etc.
  - In `snap/local/launcher`, export `GST_PLUGIN_SYSTEM_PATH`,
  `GST_PLUGIN_SCANNER` and `GST_REGISTRY`. GStreamer then uses only the
  bundled plugins and keeps a per-user registry cache under
  `SNAP_USER_COMMON`.
  - Unset `GST_PLUGIN_PATH`, `GST_PLUGIN_PATH_1_0`,
  `GST_PLUGIN_SYSTEM_PATH_1_0`, `GST_PLUGIN_SCANNER_1_0` and
  `GST_REGISTRY_1_0`. GStreamer prefers the `_1_0` variants over the
  unversioned ones, so host settings could otherwise override the bundled
  paths.
  
  `gstreamer1.0-pipewire` is not included. PipeWire registers
  `pipewiresink` with rank none
  ([source](https://github.com/PipeWire/pipewire/blob/master/src/gst/gstpipewire.c)),
  so `autoaudiosink` never selects it. On PipeWire hosts the bell plays
  through `pulsesink` and pipewire-pulse. The package would also pull in
  the `pipewire` daemon package without changing behavior.
  
  ## Local build
  
  The snap CI builds from a release tarball. Building
  `snap/snapcraft.yaml` from a git checkout needs two changes that are
  *not* part of this PR:
  
  1. A `VERSION` file at the repo root, e.g. `echo 1.4.0-dev > VERSION`.
  2. `blueprint-compiler` 0.20.0 or newer on `PATH` during the build.
  Ubuntu 26.04 ships 0.19.0. I ran v0.20.0 from source and added
  `python3-gi`, `gir1.2-gtk-4.0` and `gir1.2-adw-1` to `build-packages`.
  
  ## Test plan
  
  I built the snap on core26 (arm64) and installed it on an Ubuntu 24.04
  host.
  
  - [x] The snap contains the plugins above, and `gst-plugin-scanner` sits
  at the path the launcher exports.
  - [x] I ran `playbin` on `/usr/share/sounds/freedesktop/stereo/bell.oga`
  with the snap's own GStreamer libraries and the launcher's `GST_*`
  environment:
    - It played to EOS.
    - `autoaudiosink` selected the bundled `pulsesink`.
    - Audio was captured from a null sink.
  - [x] With an empty plugin directory, the same test fails to create
  `playbin`. This shows the plugins come from the snap.
  
  ## AI Disclosure
  
  Claude Code was used throughout:
  - diagnosing the missing plugins
  - drafting the `snapcraft.yaml` and launcher changes
  - rebasing onto core26 and addressing review feedback
  - driving the core26 snap build and the GStreamer playback test
  
  I reviewed every line of the diff and understand what each change does.
  ```
- [`8c04d7c`](https://github.com/ghostty-org/ghostty/commit/8c04d7c2e8c37a4044b1af4c58e529c714c83b20) config: reject empty prefixed commands ([@12ya](https://github.com/12ya))
  ```text
  Commands containing only `direct:` or `shell:` were accepted because
  the empty-input check ran before prefix removal.
  ```
- [`cf0ab14`](https://github.com/ghostty-org/ghostty/commit/cf0ab14aed55315a53de668bc1bbcf4a13ce0ddd) config: reject empty prefixed commands ([#14921](https://github.com/ghostty-org/ghostty/issues/14921)) ([@jcollie](https://github.com/jcollie))
  ```text
  Commands containing only `direct:` or `shell:` were accepted because the
  empty-input check ran before prefix removal.
  
  AI assistance: Used OpenAI Codex
  ```
- [`7e79688`](https://github.com/ghostty-org/ghostty/commit/7e7968826f02f846e04706729cdccc4b85b85258) tmux: unescape %output and handle window-close ([@MisterTea](https://github.com/MisterTea))
  ```text
  %output payload bytes that cannot travel in the control stream are
  octal-escaped. Unescape them in place so pane data is the original
  bytes. Also parse %window-close / %unlinked-window-close and
  %session-window-changed, and emit an active_window action so callers
  can track tmux's current window.
  
  #1935
  ```
- [`c2d9362`](https://github.com/ghostty-org/ghostty/commit/c2d93620efc6364b95641fa317d428b8a4e1f9ab) tmux: do not unescape %output in the parser ([@MisterTea](https://github.com/MisterTea))
  ```text
  #1935
  
  Decoding octal escapes while parsing %output is wasted work if a
  control client never reads pane bytes. Leave the payload as tmux
  sent it; callers that need the original stream can decode later.
  Window-close, session-window-changed, and active_window are unchanged.
  ```
- [`dc6ab39`](https://github.com/ghostty-org/ghostty/commit/dc6ab39fb1f31c6e0ffe2fadfc0b3e2d4d347442) termio: handle tmux active_window action ([@MisterTea](https://github.com/MisterTea))
  ```text
  The viewer emits active_window when the current tmux window
  changes. The stream handler switch did not cover that tag, so
  the GTK build failed. Accept the action and leave GUI
  notification for a later change, matching the windows case.
  ```
- [`9a92081`](https://github.com/ghostty-org/ghostty/commit/9a920818820f0885e9302b6831cdfe5a2aab67a4) tmux: honor session id on active window changes ([@MisterTea](https://github.com/MisterTea))
  ```text
  #1935
  
  %session-window-changed is broadcast to every control client for
  every session. Emit active_window only when the notification's
  session matches the one this viewer is attached to.
  %window-pane-changed stays ignored, since an active pane change
  does not mean the current window changed. If recording the action
  runs out of memory, the viewer becomes defunct.
  ```
- [`7e4cc4f`](https://github.com/ghostty-org/ghostty/commit/7e4cc4fae011dc3a133ce625d6cf6f0d546be64a) tmux: reject oversized control ids without leaking ([@MisterTea](https://github.com/MisterTea))
  ```text
  #1935
  
  %window-close and %session-window-changed are split with prefix
  cuts instead of compiling a regex on every notification. An id
  that is not decimal digits or does not fit in usize is ignored
  rather than crashing. If a later list-windows line fails to
  parse, layout arenas from the lines that already parsed are freed.
  ```
- [`539a7f1`](https://github.com/ghostty-org/ghostty/commit/539a7f1ce770b12071ca146e9824b9d9e5a1b88f) nix: use store paths for propagated GStreamer packages ([@romen](https://github.com/romen))
  ```text
  postFixup wrote the literal attribute names (e.g.
  "gst_all_1.gstreamer") into nix-support/propagated-user-env-packages
  instead of store paths. Anything that builds an environment from that
  file fails, e.g. `nix shell github:ghostty-org/ghostty/v1.4.0`:
  
      error: not an absolute path: 'gst_all_1.gstreamer'
  
  Interpolate the packages so the file contains their store paths.
  
  
  Change-Id: I37035d027b3ec2396f7d39911fe7dc336a6a6964
  ```
- [`2ddcda8`](https://github.com/ghostty-org/ghostty/commit/2ddcda8e80fdf53d2a6fdee9d36f4986d858d477) tmux: test %exit with and without a reason ([@MisterTea](https://github.com/MisterTea))
  ```text
  #1935
  
  The parser already accepts a bare %exit and one with a reason
  such as "server exited", and drops the reason. Cover both forms.
  Use std.mem.find for the session-window split; indexOf is deprecated.
  ```
- [`0a5a6a6`](https://github.com/ghostty-org/ghostty/commit/0a5a6a6e1a20928f4b097d51ec9fcf06de353024) Merge remote-tracking branch 'origin/main' into tmux-pr4-protocol ([@MisterTea](https://github.com/MisterTea))
- [`cd00d09`](https://github.com/ghostty-org/ghostty/commit/cd00d09c64c34c3074b0b2c2f584fce6fbab2ca9) tmux: ignore active_window in raw startup tests ([@MisterTea](https://github.com/MisterTea))
  ```text
  #1935
  
  Main's raw startup viewer test switches on every viewer action.
  The active_window action added for %session-window-changed was
  unhandled, so CI failed to compile that test. This startup path
  does not change the active window, so the test ignores the action.
  ```
- [`eec45a5`](https://github.com/ghostty-org/ghostty/commit/eec45a52dda2a3080023ef45d37797a091b486bd) tmux: handle window-close and active window ([#14273](https://github.com/ghostty-org/ghostty/issues/14273)) ([@jcollie](https://github.com/jcollie))
  ```text
  ## Summary
  
  - Parse `%window-close` / `%unlinked-window-close` and
  `%session-window-changed`.
  - Emit an `active_window` viewer action so later layers can track tmux's
  current window.
  - Parse `%exit` as soon as the notification line is seen.
  
  `%output` is left escaped on purpose. A control client that is not
  reading pane bytes should not pay to decode octal sequences up front;
  callers that need the original stream can unescape later (see #12076).
  
  This is stacked on #14262. GitHub will also show that commit until it
  merges, because we cannot target another PR's branch from a fork.
  
  **Depends on:** #14262
  
  CI / compile may fail until that PR is on `main`. That is expected.
  
  ## Test plan
  
  - [ ] `zig build test-lib-vt -Dtest-filter="tmux"` after #14262 is
  merged
  - [ ] Close a tmux window and change the active window; parser emits the
  new notifications (still log-only on `main` until later PRs)
  
  ## AI disclosure
  
  This change was written with [Cursor](https://cursor.com). I directed
  the work, reviewed the diff, and am responsible for it.
  
  Related: #1935
  
  Made with [Cursor](https://cursor.com)
  ```
- [`e1e05c1`](https://github.com/ghostty-org/ghostty/commit/e1e05c1cd13efc4bc962f4a3fd8c4e310267b340) nix: use store paths for propagated GStreamer packages ([#14929](https://github.com/ghostty-org/ghostty/issues/14929)) ([@jcollie](https://github.com/jcollie))
  ````text
  `nix/package.nix` writes the GStreamer entries in
  `nix-support/propagated-user-env-packages` as plain strings
  (`gst_all_1.gstreamer`) rather than store paths. The package builds
  fine, but anything that reads that file to assemble an environment fails
  afterwards. With 1.4.0:
  
      $ nix shell github:ghostty-org/ghostty/v1.4.0
      error: not an absolute path: 'gst_all_1.gstreamer'
  
  `nix run` is unaffected since it doesn't read propagated packages.
  
  This interpolates the three packages so their store paths are written,
  matching the `$terminfo`, `$shell_integration` and `$vim` lines above.
  
  Tested on x86_64-linux:
  
  ```
  nix build .#default
  cat result/nix-support/propagated-user-env-packages   # all store paths now
  nix shell .#default -c ghostty --version
  
  # Also tested a long-running GUI session with the resulting environment and tested AV playing with `mpv -vo kitty`
  nix shell .#default
  which ghostty # points to the path of the just build derivation
  ghostty # opens a new ghostty window
  # within that new window
  mpv -vo kitty ~/Downloads/some_random_video.mp4
  # Video and Audio both play properly
  ```
  
  AI disclosure: Claude Opus 5.5, used to diagnose the issue, edit the
  commit message, and draft the initial version of this PR description.
  I (a human being) manually patched the nix file (admittedly it was a
  trivial fix), and tested the patch.
  
  
  ---
  
  **Note: I know this will be automatically closed until I am vouched, but
  I'd like to store here the PR description, while the fix is fresh,
  rather than having to craft a new one if the vouching process takes
  days.**
  ````
- [`7c6e101`](https://github.com/ghostty-org/ghostty/commit/7c6e1011c237aaac3d19d094b3c4bdada3b21bc8) Update VOUCHED list ([#14943](https://github.com/ghostty-org/ghostty/issues/14943)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14942#discussioncomment-19283760)
  from @jcollie.
  
  Vouch: @tonypapousek
  ```

