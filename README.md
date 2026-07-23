> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: July 23, 2026 at 13:45 UTC.

## July 23, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/30010810985)  
Summary: 1 runs • 4 commits • 3 authors

### Changes

- [`960c2cc`](https://github.com/ghostty-org/ghostty/commit/960c2cca5d57ca6e293efd2d7b7a0f590412cfa8) fix: fix kitty temp directory copy length mismatch ([@elias8](https://github.com/elias8))
- [`e663d54`](https://github.com/ghostty-org/ghostty/commit/e663d54051d3af9103d1d889d3d7eac7d7176931) os/hostname: switch to std.Io.net.HostName.validate ([@jparise](https://github.com/jparise))
  ```text
  Zig 0.16's hostname validation routine is RFC 1123-compliant, so we can
  use it directly rather than rolling our own.
  
  Ref: https://codeberg.org/ziglang/zig/commit/efe649b13e582be855376944bac1346426e238d6
  Ref: https://github.com/ziglang/zig/pull/25710
  ```
- [`4154185`](https://github.com/ghostty-org/ghostty/commit/4154185e23707870a118767afa1dc074828a3b2f) os/hostname: switch to std.Io.net.HostName.validate ([#13428](https://github.com/ghostty-org/ghostty/issues/13428)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Zig 0.16's hostname validation routine is RFC 1123-compliant, so we can
  use it directly rather than rolling our own.
  
  Ref:
  https://codeberg.org/ziglang/zig/commit/efe649b13e582be855376944bac1346426e238d6
  Ref: https://github.com/ziglang/zig/pull/25710
  ```
- [`30de782`](https://github.com/ghostty-org/ghostty/commit/30de782e8edb5658e6539f5ccebcdcfa6582f102) fix(terminal): fix kitty temp directory copy length mismatch ([#13424](https://github.com/ghostty-org/ghostty/issues/13424)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  EDIT:
  [exposed](https://github.com/elias8/libghostty/actions/runs/29996356691/job/89171182671?pr=113#step:12:447)
  while syncing libghostty dart bindings to latest main.
  ```

## July 22, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/29956921809), [2](https://github.com/ghostty-org/ghostty/actions/runs/29949317476), [3](https://github.com/ghostty-org/ghostty/actions/runs/29936126378)  
Summary: 3 runs • 14 commits • 2 authors

### Changes

- [`1c861e3`](https://github.com/ghostty-org/ghostty/commit/1c861e3c476f2489008c12fc0b75af72c1b8484d) pkg/apple-sdk: support Xcode 27 SDK headers ([@mitchellh](https://github.com/mitchellh))
  ```text
  Xcode 27's math.h uses the __need_infinity_nan protocol provided by
  matching Clang resource headers. Zig 0.16's bundled float.h predates
  that protocol, causing the bundled libc++ compilation to fail.
  
  Overlay the SDK math.h through the Apple SDK libc include path and
  provide the missing infinity and NaN definitions. The compatibility
  header can be removed once Zig's bundled Clang headers support the
  protocol.
  ```
- [`d97a574`](https://github.com/ghostty-org/ghostty/commit/d97a5742423551e8847f2c81f6c10feeb6f5a66e) ci: test with Xcode 27 ([@mitchellh](https://github.com/mitchellh))
- [`ab0b9da`](https://github.com/ghostty-org/ghostty/commit/ab0b9da9e88fcb4b0533a1854e84628f663930af) pkg/apple-sdk: support Xcode 27 SDK headers ([#13419](https://github.com/ghostty-org/ghostty/issues/13419)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Xcode 27's math.h uses the __need_infinity_nan protocol provided by
  matching Clang resource headers. Zig 0.16's bundled float.h predates
  that protocol, causing the bundled libc++ compilation to fail.
  
  Overlay the SDK math.h through the Apple SDK libc include path and
  provide the missing infinity and NaN definitions. The compatibility
  header can be removed once Zig's bundled Clang headers support the
  protocol.
  ```
- [`dac134d`](https://github.com/ghostty-org/ghostty/commit/dac134d254bab15209e494413973e4f902b654c6) pkg/apple-sdk: enable libc++ availability annotations ([@mitchellh](https://github.com/mitchellh))
  ```text
  #13417
  
  The bundled upstream libc++ headers in Zig 0.16 skip the Apple-configured
  availability setting. This causes the headers to assume every LLVM 21
  ABI symbol is present in the target system libc++, producing binaries
  that fail at launch on macOS versions without `std::__hash_memory`.
  
  Enable the Apple vendor availability table for compile steps configured
  by the Apple SDK helper. libc++ now selects its inline compatibility
  implementation when the target system dylib does not provide the symbol.
  
  References in the mega comment
  ```
- [`49a76f2`](https://github.com/ghostty-org/ghostty/commit/49a76f244d6db48115ec48b4d9b5d40593386099) pkg/apple-sdk: enable libc++ availability annotations ([#13418](https://github.com/ghostty-org/ghostty/issues/13418)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  #13417
  
  The bundled upstream libc++ headers in Zig 0.16 skip the
  Apple-configured availability setting. This causes the headers to assume
  every LLVM 21 ABI symbol is present in the target system libc++,
  producing binaries that fail at launch on macOS versions without
  `std::__hash_memory`.
  
  Enable the Apple vendor availability table for compile steps configured
  by the Apple SDK helper. libc++ now selects its inline compatibility
  implementation when the target system dylib does not provide the symbol.
  
  References in the mega comment
  ```
- [`e8525c0`](https://github.com/ghostty-org/ghostty/commit/e8525c0fd907a6bfa91286984c767894b2b8fa65) Update to Zig 0.16.0 ([@vancluever](https://github.com/vancluever))
  ```text
  This commit represents the majority of the work necessary to upgrade
  Ghostty to use Zig 0.16.0.
  
  Key parts:
  
  * In addition to its previous responsibilities, the global state now
    houses state for global I/O implementations and the process
    environment. It is now also utilized in the main application along
    with the C library. Where necessary, global state is isolated from key
    parts of the implementation (e.g., in libghostty subsystems), and it's
    expected that this list will grow.
  
  * We currently manage our own C translation layer where necessary. In
    these cases, cImport has been removed in favor of the new external
    translate-c package. Due to fixes that have needed be made to properly
    translate the dependencies that were swapped out, as mentioned, we
    have had to backport fixes from the current translate-c package (and
    the upstream Arocc dependency). We will host this ourselves until Zig
    0.17.0 is released with these fixes.
  
  * Where necessary (only a small number of cases), some stdlib code from
    0.15.2 (and even from 0.17.0) has been taken, adopted, and vendored in
    lib/compat.
  ```
- [`f2a7652`](https://github.com/ghostty-org/ghostty/commit/f2a7652abab5d03f846f3150f9cc1b2dc23bb3dd) mitchell's touchups ([@mitchellh](https://github.com/mitchellh))
  ```text
  - benchmark: avoid buffers to avoid a memcpy
  - build: keep frame pointers on macOS. There was some debug changes from
    Zig 0.15 and this helps. Also, Apple actually requires/expects x29 to
    always be a frame pointer.
  - build/macos: force libSystem symbols instead of compiler-rt
  - global: add InitOpts.tool so that ghostty-gen/bench can parse their
    own actions in `+action`
  - quirks: provide our own vectorized memset. see the comment for more
    details why.
  - synthetic: fix UB by accessing global.io before it was initialized
  - terminal/hash_map: force inline for unique repr types. Zig 0.15
    inlined and 0.16 doesn't, measured a huge slowdown in hyperlink
    benchmarks.
  - terminal: add explicit `@Vector` usage for storing a run of identical cells
    as well as for scanning printable cells. This auto-vectorized in Zig
    0.15 but not in Zig 0.16. This produces the same assembly.
  - unicode: properties and LUT need power-of-two backing integer to avoid
    bad LLVM codegen
  ```
- [`da04b65`](https://github.com/ghostty-org/ghostty/commit/da04b65d4c3e590aa37a431ec6e25efc6900224d) terminal: init_single_threaded for C API ([@vancluever](https://github.com/vancluever))
  ```text
  The C API is assumed to be single-threaded per VT instance.
  Additionally, using fully-threaded I/O instances registers signal
  handlers, and would do a pair of registrations once per instance, which
  could easily get out of hand (and is not really what we intend anyway).
  
  init_single_threaded does not register signal handlers, so it does not
  have this issue, and matches the execution model of the C VT API
  (single-threaded/not thread-safe within a single VT instance).
  
  This also fixes an initialization issue with the threaded I/O instance
  in general (needs allocation as the memory location would have gone out
  of scope before).
  ```
- [`048619a`](https://github.com/ghostty-org/ghostty/commit/048619a6bf548684ec6af3a3b0d3cc45dd9f189e) global: take minimal instead of juicy main ([@vancluever](https://github.com/vancluever))
  ```text
  The early-stage main Zig wrapper recognizes if main only needs the
  minimal state (args and lower-level environment) and skips a bunch of
  unneeded initialization (allocator, arena, threaded I/O, and the
  higher-level environment map). Particularly, the fact that it does not
  set up an I/O instance means that we won't have any unneeded signal
  handlers set up for the unused threaded I/O implementation, which is
  similar in spirit to the fixes we applied for the C VT implementation,
  with the notable difference that we do actually set a threaded I/O up in
  global state - hence, again, we don't want the duplicate unused one.
  ```
- [`4956668`](https://github.com/ghostty-org/ghostty/commit/4956668702f3e029b615a5600531eadc40170f9b) vt: get rid of log spam on tests ([@vancluever](https://github.com/vancluever))
  ```text
  Zig 0.16.0 made the criteria for reporting "failed command" stricter (or
  looser, depending on your perspective I guess...) - now, tests that
  print anything to stderr cause the message to appear.
  
  Note that in this instance tests still pass and you get a return code of
  0, but nonetheless, it can be confusing.
  
  Additionally, having spammy passing tests in general is not necessarily
  a great experience, so this should help with that.
  
  Note that this change was already done to the main tests. We can add a
  build argument to control this if need be.
  ```
- [`7121ab6`](https://github.com/ghostty-org/ghostty/commit/7121ab6c3f0e868d3383c59a2e4d5a564f96aa9f) global: state should default to null ([@vancluever](https://github.com/vancluever))
- [`a77c706`](https://github.com/ghostty-org/ghostty/commit/a77c706a180528f8197771abd51436d98ccd854a) fix process and global error handling ([@mitchellh](https://github.com/mitchellh))
  ```text
  Restore the error handling that the removed std.posix fork and waitpid
  wrappers previously provided. Raw fork failures now propagate, waitpid
  retries interruptions before reading status, and edit-config constructs the
  sentinel-terminated argv required by execve.
  
  Let global initialization own cleanup through its existing errdefer so
  temporary paths are freed once. Report initialization failures with the
  static synchronous I/O provider because global I/O has already been torn
  down by that point.
  ```
- [`b988efc`](https://github.com/ghostty-org/ghostty/commit/b988efcfe584e88a3d0330e2c17c386ffa419d72) fix some 0.16 translation regressions ([@mitchellh](https://github.com/mitchellh))
- [`7aa9591`](https://github.com/ghostty-org/ghostty/commit/7aa9591746ffa4d2eee458960c76554352832595) Update to Zig 0.16.0 ([#12726](https://github.com/ghostty-org/ghostty/issues/12726)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Closes #12228
  Supersedes #12388
  
  **UPDATED** - Also check comments for additional details!
  
  This commit represents the majority of the work necessary to upgrade
  Ghostty to use Zig 0.16.0.
  
  At this point, all tests pass under Linux, but more work may be
  necessary to get them to build and function on other platforms.
  
  There are some parts of this update that deserve commentary, so that
  follows below:
  
  ## Expanded use of global state (IO/environment related)
  
  Global state, once generally only used by the C library, has now been
  expanded to be used across the project at large. The static local
  variable that holds the state has been moved private in its source
  container with all attributes that need to be accessed globally gated
  behind accessors, most of which guard on testing and send test copies
  instead. Use of the global state in non-testing scenarios asserts that
  the state has been initialized through `init` naturally through the
  optional assertion process.
  
  The rationale for this change is to have a location to store a
  general-purpose I/O implementation and environment variables, both of
  which are now provided through [Juicy
  Main](https://ziglang.org/download/0.16.0/release-notes.html#Juicy-Main)
  and hence can no longer be accessed or mutated through stdlib without
  use of lower-level system calls and hacks (some of which are employed,
  but sparingly).
  
  As the code matures, dependence on global state should naturally slim
  down.
  
  We do not allow global state to be used in libghostty-vt. There are
  comptime guards that prevent this should compilation of libghostty-vt
  end up pulling `global.zig`. This means that as per the last paragraph,
  work has already begun to de-couple the codebase from global state where
  necessary. Additionally, in some places where environment needs to be
  updated and where it can be done in an isolated fashion, environment
  maps are used - system-level injection of environment through the use of
  `setenv` or `unsetenv` now only happens during early initialization (and
  hopefully we can remove these in the future too, especially since they
  require re-synchronization of the higher-level environment primitives
  after this is done).
  
  ## The `lib/compat` Tree
  
  Some stdlib features that have been removed but still either seem they
  would be valuable to us or outright complex to move away from
  (particularly `SegmentedList`) have been extracted from 0.15.2, updated
  as needed, and placed in `src/lib/compat`. The intention again is to
  allow for piecemeal migration to more modern implementations or possibly
  straight local versions.
  
  This paradigm has also allowed us to add `std.Io.Condition.waitTimeout`,
  which incidentally was missed in the 0.16.0 shuffle and has been
  re-added for 0.17.0. We can remove this in favor of the upstream when we
  eventually migrate to that, obviously.
  
  Note that there was a lot more of this extracted code when this work was
  started, but a lot of said code has been removed (namely environment or
  process/fd-related functionality).
  
  ## translate-c Issues (functional on Linux, Darwin WIP)
  
  There have been a number of C translation issues that we have been
  working through through submitted patches and the great help from folks
  on the Arocc and Zig side. This is ongoing, with the remaining work to
  getting things fixed mainly focused on the MacOS side. Stay tuned for
  further developments.
  
  As mentioned at the top, follow comments for more details!
  ```

## July 21, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/29798507621), [2](https://github.com/ghostty-org/ghostty/actions/runs/29794463583), [3](https://github.com/ghostty-org/ghostty/actions/runs/29790117224)  
Summary: 3 runs • 4 commits • 4 authors

### Changes

- [`88b4cd0`](https://github.com/ghostty-org/ghostty/commit/88b4cd047fa627cdca6781bc7e7dc8b75a2cecb9) gitignore: add zig-pkg so switching between branches doesn't produce noise ([@mitchellh](https://github.com/mitchellh))
- [`f547745`](https://github.com/ghostty-org/ghostty/commit/f5477459ea23fe09bb047ed9e89a5ae53a3269bd) build(deps): bump actions/checkout from 7.0.0 to 7.0.1 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [actions/checkout](https://github.com/actions/checkout) from 7.0.0 to 7.0.1.
  - [Release notes](https://github.com/actions/checkout/releases)
  - [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/actions/checkout/compare/9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0...3d3c42e5aac5ba805825da76410c181273ba90b1)
  
  ---
  updated-dependencies:
  - dependency-name: actions/checkout
    dependency-version: 7.0.1
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`0a71d57`](https://github.com/ghostty-org/ghostty/commit/0a71d573d6bf12b31ccf8456a06fff951bc5fbc4) build(deps): bump actions/checkout from 7.0.0 to 7.0.1 ([#13403](https://github.com/ghostty-org/ghostty/issues/13403)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps [actions/checkout](https://github.com/actions/checkout) from 7.0.0
  to 7.0.1.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/actions/checkout/releases">actions/checkout's
  releases</a>.</em></p>
  <blockquote>
  <h2>v7.0.1</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>skip running unsafe pr check if input is default by <a
  href="https://github.com/aiqiaoy"><code>@​aiqiaoy</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2518">actions/checkout#2518</a></li>
  <li>trim only ascii whitespace for branch by <a
  href="https://github.com/aiqiaoy"><code>@​aiqiaoy</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2521">actions/checkout#2521</a></li>
  <li>escape values passed to --unset by <a
  href="https://github.com/aiqiaoy"><code>@​aiqiaoy</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2530">actions/checkout#2530</a></li>
  <li>Various dependency updates</li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/actions/checkout/compare/v7...v7.0.1">https://github.com/actions/checkout/compare/v7...v7.0.1</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/actions/checkout/blob/main/CHANGELOG.md">actions/checkout's
  changelog</a>.</em></p>
  <blockquote>
  <h1>Changelog</h1>
  <h2>v7.0.1</h2>
  <ul>
  <li>Skip running unsafe pr check if input is default by <a
  href="https://github.com/aiqiaoy"><code>@​aiqiaoy</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2518">actions/checkout#2518</a></li>
  <li>Trim only ascii whitespace for branch by <a
  href="https://github.com/aiqiaoy"><code>@​aiqiaoy</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2521">actions/checkout#2521</a></li>
  <li>Escape values passed to --unset by <a
  href="https://github.com/aiqiaoy"><code>@​aiqiaoy</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2530">actions/checkout#2530</a></li>
  <li>Various dependency updates</li>
  </ul>
  <h2>v7.0.0</h2>
  <ul>
  <li>Block checking out fork PR for pull_request_target and workflow_run
  by <a href="https://github.com/aiqiaoy"><code>@​aiqiaoy</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2454">actions/checkout#2454</a></li>
  <li>Various dependency updates</li>
  </ul>
  <h2>v6.0.3</h2>
  <ul>
  <li>Fix checkout init for SHA-256 repositories by <a
  href="https://github.com/yaananth"><code>@​yaananth</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2439">actions/checkout#2439</a></li>
  <li>fix: expand merge commit SHA regex and add SHA-256 test cases by <a
  href="https://github.com/yaananth"><code>@​yaananth</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2414">actions/checkout#2414</a></li>
  </ul>
  <h2>v6.0.2</h2>
  <ul>
  <li>Fix tag handling: preserve annotations and explicit fetch-tags by <a
  href="https://github.com/ericsciple"><code>@​ericsciple</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2356">actions/checkout#2356</a></li>
  </ul>
  <h2>v6.0.1</h2>
  <ul>
  <li>Add worktree support for persist-credentials includeIf by <a
  href="https://github.com/ericsciple"><code>@​ericsciple</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2327">actions/checkout#2327</a></li>
  </ul>
  <h2>v6.0.0</h2>
  <ul>
  <li>Persist creds to a separate file by <a
  href="https://github.com/ericsciple"><code>@​ericsciple</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2286">actions/checkout#2286</a></li>
  <li>Update README to include Node.js 24 support details and requirements
  by <a href="https://github.com/salmanmkc"><code>@​salmanmkc</code></a>
  in <a
  href="https://redirect.github.com/actions/checkout/pull/2248">actions/checkout#2248</a></li>
  </ul>
  <h2>v5.0.1</h2>
  <ul>
  <li>Port v6 cleanup to v5 by <a
  href="https://github.com/ericsciple"><code>@​ericsciple</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2301">actions/checkout#2301</a></li>
  </ul>
  <h2>v5.0.0</h2>
  <ul>
  <li>Update actions checkout to use node 24 by <a
  href="https://github.com/salmanmkc"><code>@​salmanmkc</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2226">actions/checkout#2226</a></li>
  </ul>
  <h2>v4.3.1</h2>
  <ul>
  <li>Port v6 cleanup to v4 by <a
  href="https://github.com/ericsciple"><code>@​ericsciple</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2305">actions/checkout#2305</a></li>
  </ul>
  <h2>v4.3.0</h2>
  <ul>
  <li>docs: update README.md by <a
  href="https://github.com/motss"><code>@​motss</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/1971">actions/checkout#1971</a></li>
  <li>Add internal repos for checking out multiple repositories by <a
  href="https://github.com/mouismail"><code>@​mouismail</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/1977">actions/checkout#1977</a></li>
  <li>Documentation update - add recommended permissions to Readme by <a
  href="https://github.com/benwells"><code>@​benwells</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2043">actions/checkout#2043</a></li>
  <li>Adjust positioning of user email note and permissions heading by <a
  href="https://github.com/joshmgross"><code>@​joshmgross</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2044">actions/checkout#2044</a></li>
  <li>Update README.md by <a
  href="https://github.com/nebuk89"><code>@​nebuk89</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2194">actions/checkout#2194</a></li>
  <li>Update CODEOWNERS for actions by <a
  href="https://github.com/TingluoHuang"><code>@​TingluoHuang</code></a>
  in <a
  href="https://redirect.github.com/actions/checkout/pull/2224">actions/checkout#2224</a></li>
  <li>Update package dependencies by <a
  href="https://github.com/salmanmkc"><code>@​salmanmkc</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2236">actions/checkout#2236</a></li>
  </ul>
  <h2>v4.2.2</h2>
  <ul>
  <li><code>url-helper.ts</code> now leverages well-known environment
  variables by <a href="https://github.com/jww3"><code>@​jww3</code></a>
  in <a
  href="https://redirect.github.com/actions/checkout/pull/1941">actions/checkout#1941</a></li>
  <li>Expand unit test coverage for <code>isGhes</code> by <a
  href="https://github.com/jww3"><code>@​jww3</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/1946">actions/checkout#1946</a></li>
  </ul>
  <h2>v4.2.1</h2>
  <ul>
  <li>Check out other refs/* by commit if provided, fall back to ref by <a
  href="https://github.com/orhantoy"><code>@​orhantoy</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/1924">actions/checkout#1924</a></li>
  </ul>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/actions/checkout/commit/3d3c42e5aac5ba805825da76410c181273ba90b1"><code>3d3c42e</code></a>
  prep v7.0.1 release (<a
  href="https://redirect.github.com/actions/checkout/issues/2531">#2531</a>)</li>
  <li><a
  href="https://github.com/actions/checkout/commit/28802689a136bfcdb721715abd713740beecbe07"><code>2880268</code></a>
  escape values passed to --unset (<a
  href="https://redirect.github.com/actions/checkout/issues/2530">#2530</a>)</li>
  <li><a
  href="https://github.com/actions/checkout/commit/12cd2235efa0937479335606d7c3ac9f6c0973b1"><code>12cd223</code></a>
  trim only ascii whitespace for branch (<a
  href="https://redirect.github.com/actions/checkout/issues/2521">#2521</a>)</li>
  <li><a
  href="https://github.com/actions/checkout/commit/62661c4e71a304b2823ed026347b8d34c3eac541"><code>62661c4</code></a>
  skip running unsafe pr check if input is default (<a
  href="https://redirect.github.com/actions/checkout/issues/2518">#2518</a>)</li>
  <li><a
  href="https://github.com/actions/checkout/commit/e8d4307400f9427dba7cb98e488d6ab85f1cec5f"><code>e8d4307</code></a>
  Bump the minor-actions-dependencies group with 2 updates (<a
  href="https://redirect.github.com/actions/checkout/issues/2499">#2499</a>)</li>
  <li><a
  href="https://github.com/actions/checkout/commit/631c942040754b6e095e929c1677c07e10ed4f87"><code>631c942</code></a>
  eslint 9 (<a
  href="https://redirect.github.com/actions/checkout/issues/2474">#2474</a>)</li>
  <li><a
  href="https://github.com/actions/checkout/commit/4f1f4aec02e41874fa0262ea8ff5172d7978ad1e"><code>4f1f4ae</code></a>
  Bump actions/upload-artifact from 4 to 7 (<a
  href="https://redirect.github.com/actions/checkout/issues/2476">#2476</a>)</li>
  <li><a
  href="https://github.com/actions/checkout/commit/ba097532fb203f7e88c9c3c0b899b49469908a92"><code>ba09753</code></a>
  Bump actions/checkout from 6 to 7 (<a
  href="https://redirect.github.com/actions/checkout/issues/2488">#2488</a>)</li>
  <li><a
  href="https://github.com/actions/checkout/commit/b9e0990d219a03df7633c93f6f005a8fecbcab22"><code>b9e0990</code></a>
  Bump docker/login-action from 3.3.0 to 4.2.0 (<a
  href="https://redirect.github.com/actions/checkout/issues/2479">#2479</a>)</li>
  <li><a
  href="https://github.com/actions/checkout/commit/e8cb398be4a550817e382abf69e4c12c76fce1f2"><code>e8cb398</code></a>
  Bump docker/build-push-action from 6.5.0 to 7.2.0 (<a
  href="https://redirect.github.com/actions/checkout/issues/2478">#2478</a>)</li>
  <li>Additional commits viewable in <a
  href="https://github.com/actions/checkout/compare/9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0...3d3c42e5aac5ba805825da76410c181273ba90b1">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=actions/checkout&package-manager=github_actions&previous-version=7.0.0&new-version=7.0.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
  Dependabot will resolve any conflicts with this PR as long as you don't
  alter it yourself. You can also trigger a rebase manually by commenting
  `@dependabot rebase`.
  
  [//]: # (dependabot-automerge-start)
  [//]: # (dependabot-automerge-end)
  
  ---
  
  <details>
  <summary>Dependabot commands and options</summary>
  <br />
  
  You can trigger Dependabot actions by commenting on this PR:
  - `@dependabot rebase` will rebase this PR
  - `@dependabot recreate` will recreate this PR, overwriting any edits
  that have been made to it
  - `@dependabot show <dependency name> ignore conditions` will show all
  of the ignore conditions of the specified dependency
  - `@dependabot ignore this major version` will close this PR and stop
  Dependabot creating any more for this major version (unless you reopen
  the PR or upgrade to it yourself)
  - `@dependabot ignore this minor version` will close this PR and stop
  Dependabot creating any more for this minor version (unless you reopen
  the PR or upgrade to it yourself)
  - `@dependabot ignore this dependency` will close this PR and stop
  Dependabot creating any more for this dependency (unless you reopen the
  PR or upgrade to it yourself)
  
  
  </details>
  ```
- [`30e1f3b`](https://github.com/ghostty-org/ghostty/commit/30e1f3bb8c3d2949e9ae4aefc1c2b76142569cfb) Update VOUCHED list ([#13404](https://github.com/ghostty-org/ghostty/issues/13404)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13402#discussioncomment-17707616)
  from @jcollie.
  
  Vouch: @carldaws
  ```

## July 20, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/29778065680), [2](https://github.com/ghostty-org/ghostty/actions/runs/29761838058), [3](https://github.com/ghostty-org/ghostty/actions/runs/29756162299)  
Summary: 3 runs • 9 commits • 4 authors

### Changes

- [`74d0c72`](https://github.com/ghostty-org/ghostty/commit/74d0c72fd9318ad3ab95bfb56f6c2d995e267e2e) Update VOUCHED list ([#13401](https://github.com/ghostty-org/ghostty/issues/13401)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13400#discussioncomment-17706483)
  from @jcollie.
  
  Vouch: @Ragnoroct
  ```
- [`ee9d5b3`](https://github.com/ghostty-org/ghostty/commit/ee9d5b352f1ba4b87c36ff7cab7708ccfcb2f4c9) terminal: handle page capacity errors in eraseRow ([@mitchellh](https://github.com/mitchellh))
  ```text
  Re: #13160 (related but not that issue)
  
  PageList eraseRow and eraseRowBounded have the same issue previously
  fixed for cursorScrollAbove: when shifting rows up across a page boundary,
  the top row of the next page is cloned into the last row of the
  previous page, and that clone can fail if the destination page lacks
  capacity for the row's managed memory.
  
  Handle the errors the same way the other cross-page copies do:
  increase the destination page capacity for the dimension that ran
  out and retry the row copy.
  
  This type of logic was repeated EVERYWHERE so I extracted this into a
  helper in PageList and Screen. They're slightly different due to the extra
  accounting that Screen has to do for the cursor.
  
  Don't know of any scenario this actually happened in the real world but
  it was trivially reproducible with tests.
  ```
- [`ea7dc5c`](https://github.com/ghostty-org/ghostty/commit/ea7dc5c000c31c44ff2cdc5bd23dea4c090bf800) terminal: handle page capacity errors in eraseRow ([#13397](https://github.com/ghostty-org/ghostty/issues/13397)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Re: #13160 (related but not that issue)
  
  PageList eraseRow and eraseRowBounded have the same issue previously
  fixed for cursorScrollAbove: when shifting rows up across a page
  boundary, the top row of the next page is cloned into the last row of
  the previous page, and that clone can fail if the destination page lacks
  capacity for the row's managed memory.
  
  Handle the errors the same way the other cross-page copies do: increase
  the destination page capacity for the dimension that ran out and retry
  the row copy.
  
  This type of logic was repeated EVERYWHERE so I extracted this into a
  helper in PageList and Screen. They're slightly different due to the
  extra accounting that Screen has to do for the cursor.
  
  Don't know of any scenario this actually happened in the real world but
  it was trivially reproducible with tests.
  ```
- [`a65e11c`](https://github.com/ghostty-org/ghostty/commit/a65e11cc928f1ecf4d4a1d640d28a37c06e3d20f) kitty images: add support for transient usage hints ([@jcollie](https://github.com/jcollie))
  ```text
  Kitty 0.48 added support for usage hints in the image protocol,
  specifically for marking images as "transient", meaning that they
  should be prioritized for eviction if there is memory pressure.
  
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#image-usage-hints
  
  Also changed the eviction algorithm to use an allocated array for
  organizing the images to be evicted rather than using an ArrayList to
  minimize the number of allocations made (no real memory savings though).
  ```
- [`2104e07`](https://github.com/ghostty-org/ghostty/commit/2104e0749c6da413b173bce375d77975fd41f4be) macOS: hide visible NSScrollPocket for hidden title bar ([@bo2themax](https://github.com/bo2themax))
  ```text
  Fixes https://github.com/ghostty-org/ghostty/issues/13390
  ```
- [`0433262`](https://github.com/ghostty-org/ghostty/commit/043326249387b36a2655c7f24bb856bbc1aca4ea) terminal: handle page capacity errors in cursorScrollAbove ([@mitchellh](https://github.com/mitchellh))
  ```text
  Re: #13160
  
  When cursorScrollAbove rotates rows across a page boundary, the last
  row of the previous page is cloned into the destination page. That can
  cause capacity failures we didn't previously handle.
  
  The error propagated out of the operation after rows had already been rotated,
  leaving the page list half-mutated. Subsequent operations on the corrupted state
  can cause crashes since the state was incoherent.
  
  Handle these errors the same way insertLines and deleteLines already
  do for their cross-page copies: increase the destination page capacity
  for the dimension that ran out and retry the row copy.
  ```
- [`56b086b`](https://github.com/ghostty-org/ghostty/commit/56b086bd93b69884263a8a4a4a10f4bc1b9b4539) terminal: handle page capacity errors in cursorScrollAbove ([#13394](https://github.com/ghostty-org/ghostty/issues/13394)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Re: #13160
  
  When cursorScrollAbove rotates rows across a page boundary, the last row
  of the previous page is cloned into the destination page. That can cause
  capacity failures we didn't previously handle.
  
  The error propagated out of the operation after rows had already been
  rotated, leaving the page list half-mutated. Subsequent operations on
  the corrupted state can cause crashes since the state was incoherent.
  
  Handle these errors the same way insertLines and deleteLines already do
  for their cross-page copies: increase the destination page capacity for
  the dimension that ran out and retry the row copy.
  ```
- [`18d8303`](https://github.com/ghostty-org/ghostty/commit/18d8303972b1f68b865add30c700f821332de554) kitty images: add support for transient usage hints ([#13389](https://github.com/ghostty-org/ghostty/issues/13389)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Kitty 0.48 added support for usage hints in the image protocol,
  specifically for marking images as "transient", meaning that they should
  be prioritized for eviction if there is memory pressure.
  
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#image-usage-hints
  
  Also changed the eviction algorithm to use an allocated array for
  organizing the images to be evicted rather than using an ArrayList to
  minimize the number of allocations made (no real memory savings though).
  ```
- [`ff8457b`](https://github.com/ghostty-org/ghostty/commit/ff8457b70fd44b6b0d29906098134716c16287d0) macOS: hide visible NSScrollPocket for hidden title bar ([#13393](https://github.com/ghostty-org/ghostty/issues/13393)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes https://github.com/ghostty-org/ghostty/issues/13390
  
  Technically it would be safe to remove `#available(macOS 27, *)` check,
  but I haven't tested all the os versions, so I kept it there.
  
  ### AI Disclosure
  
  No AI is used for this one.
  ```

## July 19, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/29697007776), [2](https://github.com/ghostty-org/ghostty/actions/runs/29693133907), [3](https://github.com/ghostty-org/ghostty/actions/runs/29689282072)  
Summary: 3 runs • 5 commits • 3 authors

### Changes

- [`2da02f4`](https://github.com/ghostty-org/ghostty/commit/2da02f4d289d917538c907b362e69878e064c36e) config: update `background-blur` to reflect growing adoption ([@pluiedev](https://github.com/pluiedev))
  ```text
  `ext-background-effect-v1` is finally seeing major adoption throughout
  KWin, Mutter, cosmic-comp, Niri, etc. and we should update our comments
  on that.
  ```
- [`2511abe`](https://github.com/ghostty-org/ghostty/commit/2511abe3dd864013ef9a20c14c50e432f901f703) config: update `background-blur` to reflect growing adoption ([#13384](https://github.com/ghostty-org/ghostty/issues/13384)) ([@pluiedev](https://github.com/pluiedev))
  ```text
  `ext-background-effect-v1` is finally seeing major adoption throughout
  KWin, Mutter, cosmic-comp, Niri, etc. and we should update our comments
  on that.
  ```
- [`c9c017e`](https://github.com/ghostty-org/ghostty/commit/c9c017e8e5dd3c2a03fad48d365154b15df173ac) Update VOUCHED list ([#13383](https://github.com/ghostty-org/ghostty/issues/13383)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13376#discussioncomment-17684953)
  from @jcollie.
  
  Vouch: @bousii
  ```
- [`b513f1b`](https://github.com/ghostty-org/ghostty/commit/b513f1b2093e4d71613ed0584b1ae9ff57afe0fe) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`77c65cb`](https://github.com/ghostty-org/ghostty/commit/77c65cb5fecee8568d080aa235fde20afa5ba803) Update iTerm2 colorschemes ([#13377](https://github.com/ghostty-org/ghostty/issues/13377)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260713-155359-c3968b3
  ```

## July 18, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/29629221748)  
Summary: 1 runs • 2 commits • 1 authors

### Changes

- [`c594031`](https://github.com/ghostty-org/ghostty/commit/c594031d5085527182e608a6100cbfa75cfd022f) terminal: move cursor defaults into terminal state ([@mitchellh](https://github.com/mitchellh))
  ```text
  Cursor defaults were duplicated across stream handlers and it was a
  pretty significant amount of simple and yet non-trivial logic to
  understand.
  
  Store these on Terminal itself and have methods to route things like
  DECSCUSR through for consistent behaviors.
  ```
- [`f3c9a2b`](https://github.com/ghostty-org/ghostty/commit/f3c9a2b7262a989ba7e9408d00471fda8f788d16) terminal: move cursor defaults into terminal state ([#13370](https://github.com/ghostty-org/ghostty/issues/13370)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Cursor defaults were duplicated across stream handlers and it was a
  pretty significant amount of simple and yet non-trivial logic to
  understand.
  
  Store these on Terminal itself and have methods to route things like
  DECSCUSR through for consistent behaviors.
  
  No AI usage here.
  ```

## July 17, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/29610434744), [2](https://github.com/ghostty-org/ghostty/actions/runs/29602269436), [3](https://github.com/ghostty-org/ghostty/actions/runs/29600718239), [4](https://github.com/ghostty-org/ghostty/actions/runs/29586962822)  
Summary: 4 runs • 9 commits • 3 authors

### Changes

- [`439d35e`](https://github.com/ghostty-org/ghostty/commit/439d35e27ca2ef7ae62af5d3a386dad4f7ad0bdf) libghostty: mark semantic stream failures ([@mitchellh](https://github.com/mitchellh))
  ```text
  The libghostty-vt stream is made to be infallible: in the case of any error
  it just logs and moves on. That's because a terminal can't really... stop,
  under normal operations. But, under special operations (fuzzing, replays,
  etc.) it can and should stop!
  
  Rather than make the operation fallible, its simply enough for me at least
  to know that something went wrong. This is a simple change that adds a simple
  flag that is flagged to true when such a scenario happens.
  
  For normal Ghostty GUI operations, this isn't used at all. For libghostty
  consumers they can choose to read it if they want, but don't have to.
  
  This also adds a C API to read it.
  ```
- [`6711672`](https://github.com/ghostty-org/ghostty/commit/6711672dec655b620ae64cde1e1ff6cee2e95b18) libghostty: mark semantic stream failures ([#13369](https://github.com/ghostty-org/ghostty/issues/13369)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The libghostty-vt stream is made to be infallible: in the case of any
  error it just logs and moves on. That's because a terminal can't
  really... stop, under normal operations. But, under special operations
  (fuzzing, replays, etc.) it can and should stop!
  
  Rather than make the operation fallible, its simply enough for me at
  least to know that something went wrong. This is a simple change that
  adds a simple flag that is flagged to true when such a scenario happens.
  
  For normal Ghostty GUI operations, this isn't used at all. For
  libghostty consumers they can choose to read it if they want, but don't
  have to.
  
  This also adds a C API to read it.
  ```
- [`89b103d`](https://github.com/ghostty-org/ghostty/commit/89b103dd5ec669318de53fa361195d155b9e7155) terminal: more full featured resize (cell geo, sync rendering, etc.) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This makes the Terminal.resize handle more of the common elements that
  a core terminal emulator should: cell geoemtry handling (if exists),
  updates synchronized output modes.
  
  This adds a new TerminalStream.resize that also handles the side effects
  for more easy integration into downstream libghostty-vt consumers, namely
  mode 2048 in-band signaling handling.
  ```
- [`dde3d4d`](https://github.com/ghostty-org/ghostty/commit/dde3d4d6b05338e1860a7c45fd17990a6d634e8b) terminal: screen resize failures are now safe ([@mitchellh](https://github.com/mitchellh))
- [`a3c1cab`](https://github.com/ghostty-org/ghostty/commit/a3c1caba545e7894b21fa359701d245b82b82083) terminal: resize failures are now almost fully safe ([@mitchellh](https://github.com/mitchellh))
  ```text
  Terminal resize could leave tab stops, pixel geometry, synchronized output,
  or screen dimensions partially updated when a later allocation failed. This
  is now safe. There is one exception, see the code comments.
  ```
- [`d7e9773`](https://github.com/ghostty-org/ghostty/commit/d7e9773329ae86e6117c9ab5b6531367ac8c530a) terminal: make resize handling error-safe, handle more logic ([#13367](https://github.com/ghostty-org/ghostty/issues/13367)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This makes error returns in `Screen.resize` and `Terminal.resize` safe:
  they leave the terminal/screen in its prior state (with one exception,
  noted below). Previously, both were documented as leaving the terminal
  in a garbage stage on error.
  
  Unit tests with tripwire added to verify errdefer behaviors.
  
  This also includes a refactor: the common behaviors that resize needs
  such as updating cell size in pixels, disabling synchronized output,
  handling mode 2048, are now pulled into libghostty-vt. This will make it
  easier for downstream libghostty users to make proper terminals.
  
  **The one perfect undo exception:** If the primary screen can resize but
  the alt screen cannot, then we try our best to do something reasonable,
  in order:
  
  1. If we're on the primary screen, we just deallocate the alt screen.
  It'll be reallocated lazily (and may fail) in the future. Worst case
  here is we lose screen data if the future TUI doesn't expect a clear on
  enter/exit.
  
  2. If we're on the alt screen, we deallocate to try recover memory, then
  reinitialize eagerly at the new size hoping to at least have a blank alt
  screen. Similar to 1, we lose screen data here, but its likely screen
  data that mattered since we were actively on the alt screen.
  
  3. If the eager reinit fails, we switch to the primary screen. This is
  the biggest issue, cause the TUI program won't know this happened and
  probably do some crazy stuff on the primary screen. But, its also a
  super exceptional situation.
  
  In every case though, the terminal is consistent and safe to use.
  
  **LLM notes:** Only used as a judge and to assist with test writing, not
  used at all for commit messages, PR, or non-test logic.
  ```
- [`f21d376`](https://github.com/ghostty-org/ghostty/commit/f21d37688368be95b0ee57674f30e9af9376f40b) Update VOUCHED list ([#13368](https://github.com/ghostty-org/ghostty/issues/13368)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13366#discussioncomment-17675218)
  from @jcollie.
  
  Vouch: @AprilNEA
  ```
- [`0f0ede8`](https://github.com/ghostty-org/ghostty/commit/0f0ede81d5950f7889dccde07a450d162ffd6e7c) build(deps): bump namespacelabs/nscloud-cache-action from 1.6.0 to 1.6.1 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [namespacelabs/nscloud-cache-action](https://github.com/namespacelabs/nscloud-cache-action) from 1.6.0 to 1.6.1.
  - [Release notes](https://github.com/namespacelabs/nscloud-cache-action/releases)
  - [Commits](https://github.com/namespacelabs/nscloud-cache-action/compare/58bf6e08898e88803c098e2b522668541cd3b2e3...c5f8dab7560444c4bf8dbc64f1b203431873c547)
  
  ---
  updated-dependencies:
  - dependency-name: namespacelabs/nscloud-cache-action
    dependency-version: 1.6.1
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`e9ffb25`](https://github.com/ghostty-org/ghostty/commit/e9ffb2579d71185ad25926fb6122e5f388454dcf) build(deps): bump namespacelabs/nscloud-cache-action from 1.6.0 to 1.6.1 ([#13361](https://github.com/ghostty-org/ghostty/issues/13361)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [namespacelabs/nscloud-cache-action](https://github.com/namespacelabs/nscloud-cache-action)
  from 1.6.0 to 1.6.1.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/namespacelabs/nscloud-cache-action/releases">namespacelabs/nscloud-cache-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v1.6.1</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>Bump the minor-actions-dependencies group across 1 directory with 6
  updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/154">namespacelabs/nscloud-cache-action#154</a></li>
  <li>Remove Tuist cache mode test by <a
  href="https://github.com/rcrowe"><code>@​rcrowe</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/156">namespacelabs/nscloud-cache-action#156</a></li>
  <li>Bump the minor-npm-dependencies group across 1 directory with 9
  updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/155">namespacelabs/nscloud-cache-action#155</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/namespacelabs/nscloud-cache-action/compare/v1...v1.6.1">https://github.com/namespacelabs/nscloud-cache-action/compare/v1...v1.6.1</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/c5f8dab7560444c4bf8dbc64f1b203431873c547"><code>c5f8dab</code></a>
  Bump the minor-npm-dependencies group across 1 directory with 9 updates
  (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/155">#155</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/0820eca039c654baff6026b49fe635a167913044"><code>0820eca</code></a>
  ci: remove tuist cache mode test (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/156">#156</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/fa75731ea70ffa2e55a1e66dd0cb4383c9b2b716"><code>fa75731</code></a>
  Bump the minor-actions-dependencies group across 1 directory with 6
  updates (...</li>
  <li>See full diff in <a
  href="https://github.com/namespacelabs/nscloud-cache-action/compare/58bf6e08898e88803c098e2b522668541cd3b2e3...c5f8dab7560444c4bf8dbc64f1b203431873c547">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=namespacelabs/nscloud-cache-action&package-manager=github_actions&previous-version=1.6.0&new-version=1.6.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
  Dependabot will resolve any conflicts with this PR as long as you don't
  alter it yourself. You can also trigger a rebase manually by commenting
  `@dependabot rebase`.
  
  [//]: # (dependabot-automerge-start)
  [//]: # (dependabot-automerge-end)
  
  ---
  
  <details>
  <summary>Dependabot commands and options</summary>
  <br />
  
  You can trigger Dependabot actions by commenting on this PR:
  - `@dependabot rebase` will rebase this PR
  - `@dependabot recreate` will recreate this PR, overwriting any edits
  that have been made to it
  - `@dependabot show <dependency name> ignore conditions` will show all
  of the ignore conditions of the specified dependency
  - `@dependabot ignore this major version` will close this PR and stop
  Dependabot creating any more for this major version (unless you reopen
  the PR or upgrade to it yourself)
  - `@dependabot ignore this minor version` will close this PR and stop
  Dependabot creating any more for this minor version (unless you reopen
  the PR or upgrade to it yourself)
  - `@dependabot ignore this dependency` will close this PR and stop
  Dependabot creating any more for this dependency (unless you reopen the
  PR or upgrade to it yourself)
  
  
  </details>
  ```

