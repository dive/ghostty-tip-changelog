> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: March 15, 2026 at 03:58 UTC.

## March 14, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23098143300), [2](https://github.com/ghostty-org/ghostty/actions/runs/23090671545), [3](https://github.com/ghostty-org/ghostty/actions/runs/23088656823)  
Summary: 3 runs • 20 commits • 2 authors

### Changes

- [`302e68f`](https://github.com/ghostty-org/ghostty/commit/302e68fd3d9891919a3b6f32f47ee7f954bef848) vt: expose ghostty_terminal_new/free ([@mitchellh](https://github.com/mitchellh))
- [`18fdc15`](https://github.com/ghostty-org/ghostty/commit/18fdc15357a2f519d93987d09a2957b9369340cb) vt: ghostty_terminal_vt_write ([@mitchellh](https://github.com/mitchellh))
- [`8b9afe3`](https://github.com/ghostty-org/ghostty/commit/8b9afe35a706ea230473c81637c3f43f07d736b7) vt: ghostty_terminal_scroll_viewport ([@mitchellh](https://github.com/mitchellh))
- [`fe6e7fb`](https://github.com/ghostty-org/ghostty/commit/fe6e7fbc6b54c835f9a5229f0b19ee9f96ec5a92) vt: ghostty_terminal_resize ([@mitchellh](https://github.com/mitchellh))
- [`aa3e6e2`](https://github.com/ghostty-org/ghostty/commit/aa3e6e23a227cfe4ba0026d844b54e7a89ea880b) vt: ghostty_terminal_reset ([@mitchellh](https://github.com/mitchellh))
- [`34acdfc`](https://github.com/ghostty-org/ghostty/commit/34acdfcc4eca388d3d4fa1a5ce03525384db8e3e) vt: update terminal.h docs ([@mitchellh](https://github.com/mitchellh))
- [`8e6bf82`](https://github.com/ghostty-org/ghostty/commit/8e6bf829a746be199bd30d4670fe855035562433) terminal/osc: don't export context/semantic prompts to libvt yet ([@mitchellh](https://github.com/mitchellh))
- [`b5fb7ec`](https://github.com/ghostty-org/ghostty/commit/b5fb7ecaaaa2d788093809614d88b6294baaf672) vt: wip formatter api ([@mitchellh](https://github.com/mitchellh))
- [`4e494cc`](https://github.com/ghostty-org/ghostty/commit/4e494ccd688cd44f92d010cdd6fa46412339f69e) lib: lib.Struct can convert packed structs to extern structs ([@mitchellh](https://github.com/mitchellh))
- [`09d3ebd`](https://github.com/ghostty-org/ghostty/commit/09d3ebd80df2988dd48cc94a4826a226a7c2d269) vt: use explicit options structs ([@mitchellh](https://github.com/mitchellh))
- [`a2d570b`](https://github.com/ghostty-org/ghostty/commit/a2d570b51e059fc9fc572dcb155e81215a9c51bc) vt: add sized struct pattern and types.h ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a size field as the first member of formatter option structs
  (TerminalOptions, TerminalOptions.Extra, ScreenOptions.Extra) for ABI
  compatibility. This allows adding new fields without breaking callers
  compiled against older versions of the struct.
  
  Introduce include/ghostty/vt/types.h as the foundational header
  containing GhosttyResult and the GHOSTTY_INIT_SIZED macro for
  zero-initializing sized structs. Remove the separate result.h header,
  moving its contents into types.h.
  ```
- [`7c12d6e`](https://github.com/ghostty-org/ghostty/commit/7c12d6e35d9e1cc28f71877559c17b4088f32532) agents: skill for writing commit messages ([@mitchellh](https://github.com/mitchellh))
- [`3c8feda`](https://github.com/ghostty-org/ghostty/commit/3c8feda118cc4bd51cadc5f4c98e54158716a2c0) vt: add format_alloc to C API formatter ([@mitchellh](https://github.com/mitchellh))
  ```text
  Rename the existing format function to format_buf to clarify that it
  writes into a caller-provided buffer. Add a new format_alloc variant
  that allocates the output buffer internally using the provided
  allocator (or the default if NULL). The caller receives the allocated
  pointer and length and is responsible for freeing it.
  
  This is useful for consumers that do not know the required buffer size
  ahead of time and want to avoid the two-pass query-then-format pattern
  needed with format_buf.
  ```
- [`1e21ac1`](https://github.com/ghostty-org/ghostty/commit/1e21ac119079bf7bc4d965666ce1f691ce4d84c5) example: add c-vt-formatter example ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add an example showing how to use the ghostty-vt terminal and
  formatter APIs from C. The example creates a terminal, writes
  VT-encoded content with cursor movement and styling sequences,
  then formats the screen contents as plain text using the formatter
  API.
  ```
- [`4ad7d03`](https://github.com/ghostty-org/ghostty/commit/4ad7d03c56de3216f2a82c8790d0c8edb216db07) terminal/formatter: safely cast discarding.count to usize ([@mitchellh](https://github.com/mitchellh))
  ```text
  The Discarding writer count field is u64, but appendNTimes expects
  usize which is u32 on 32-bit targets like arm-linux-androideabi.
  Use std.math.cast instead of @intCast to safely handle the
  conversion, returning WriteFailed on overflow rather than risking
  undefined behavior.
  ```
- [`647f5ad`](https://github.com/ghostty-org/ghostty/commit/647f5adf556e13abcbe4b38c185fb81458aa5711) terminal/formatter: safely cast discarding.count to usize ([@mitchellh](https://github.com/mitchellh))
  ```text
  The Discarding writer count field is u64, but several call sites
  pass it where a usize is expected. On wasm32-freestanding, usize is
  32-bit, so this caused compilation errors.
  
  Use std.math.cast instead of a bare @intCast so that overflow is
  handled gracefully, returning WriteFailed rather than triggering
  safety-checked undefined behavior at runtime.
  ```
- [`f730eed`](https://github.com/ghostty-org/ghostty/commit/f730eed213143db6e3082311f54afbf0c87bdd2d) vt: fix missing formatter docs in doxygen ([@mitchellh](https://github.com/mitchellh))
- [`952fbce`](https://github.com/ghostty-org/ghostty/commit/952fbce0e50ded8fd8e6ee5f64e9650af962cd19) libghostty: add initial C API for terminal, formatter ([#11506](https://github.com/ghostty-org/ghostty/issues/11506)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This adds an initial C API for terminals and formatting. There is a new
  example that shows how to use this.
  
  With these APIs in place, users of the C API can now create a terminal,
  pass raw VT streams to it, and dump the terminal viewport to various
  formats. As noted in the docs, **the formatter API is not a rendering
  API**, it isn't high performance enough for that. But it's a simpler API
  to implement than the render state API so I started with that.
  
  Both APIs are purposely fairly minimal, we're just setting the stage for
  future functionality.
  
  ## Example
  
  ```c
  #include <ghostty/vt.h>
  #include <stdio.h>
  #include <stdlib.h>
  #include <string.h>
  
  int main() {
    GhosttyTerminal term;
    GhosttyTerminalOptions opts = { .cols = 80, .rows = 24, .max_scrollback = 0 };
    ghostty_terminal_new(NULL, &term, opts);
  
    const char *input = "Hello, \033[1mBold\033[0m World!\r\nLine 2\r\n";
    ghostty_terminal_vt_write(term, (const uint8_t *)input, strlen(input));
  
    GhosttyFormatterTerminalOptions fmt = GHOSTTY_INIT_SIZED(GhosttyFormatterTerminalOptions);
    fmt.emit = GHOSTTY_FORMATTER_FORMAT_PLAIN;
    fmt.trim = true;
  
    GhosttyFormatter fmtr;
    ghostty_formatter_terminal_new(NULL, &fmtr, term, fmt);
  
    uint8_t *buf;
    size_t len;
    ghostty_formatter_format_alloc(fmtr, NULL, &buf, &len);
    fwrite(buf, 1, len, stdout);
  
    free(buf);
    ghostty_formatter_free(fmtr);
    ghostty_terminal_free(term);
  }
  ```
  
  ## New APIs
  
  | Function | Description |
  |----------|-------------|
  | `ghostty_terminal_new` | Create a new terminal instance |
  | `ghostty_terminal_free` | Free a terminal instance |
  | `ghostty_terminal_reset` | Full reset of the terminal (RIS) |
  | `ghostty_terminal_resize` | Resize the terminal to given dimensions |
  | `ghostty_terminal_vt_write` | Write VT-encoded data to the terminal |
  | `ghostty_terminal_scroll_viewport` | Scroll the terminal viewport |
  | `ghostty_formatter_terminal_new` | Create a formatter for a terminal's
  active screen |
  | `ghostty_formatter_format_buf` | Format into a caller-provided buffer
  |
  | `ghostty_formatter_format_alloc` | Format into an allocated buffer |
  | `ghostty_formatter_free` | Free a formatter instance |
  
  ## Future
  
  - Obviously need to expose a lot more from the terminal:
    * Read current set modes
    * Read cursor information
    * Read screen information
    * etc...
  - Need an optional callback system so that `vt_write` can invoke
  callbacks for side effect sequences like clipboards, title setting,
  responses, etc.
  - `terminal.RenderState` C API so that people can build high performance
  renderers on top of libghostty-vt
  
  And so on...
  ````
- [`1844a5f`](https://github.com/ghostty-org/ghostty/commit/1844a5f7bafbade1305e95d515eedcb010aae104) Update VOUCHED list ([#11492](https://github.com/ghostty-org/ghostty/issues/11492)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11491#issuecomment-4060704311)
  from @mitchellh.
  
  Vouch: @devsunb
  ```
- [`6368b00`](https://github.com/ghostty-org/ghostty/commit/6368b00604e4543088eda552a8aa3f6776500332) Update VOUCHED list ([#11488](https://github.com/ghostty-org/ghostty/issues/11488)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11485#discussioncomment-16130186)
  from @mitchellh.
  
  Vouch: @jesusvazquez
  ```

## March 13, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23070991378), [2](https://github.com/ghostty-org/ghostty/actions/runs/23062813936), [3](https://github.com/ghostty-org/ghostty/actions/runs/23060730419), [4](https://github.com/ghostty-org/ghostty/actions/runs/23059512011), [5](https://github.com/ghostty-org/ghostty/actions/runs/23030892705)  
Summary: 5 runs • 11 commits • 4 authors

### Changes

- [`2044e50`](https://github.com/ghostty-org/ghostty/commit/2044e5030ffaadf0361a2f4fca040b77408db0b5) terminal: make stream processing infallible ([@mitchellh](https://github.com/mitchellh))
  ```text
  The terminal.Stream next/nextSlice functions can now no longer fail.
  All prior failure modes were fully isolated in the handler `vt`
  callbacks. As such, vt callbacks are now required to not return an error
  and handle their own errors somehow.
  
  Allowing streams to be fallible before was an incorrect design. It
  caused problematic scenarios like in `nextSlice` early terminating
  processing due to handler errors. This should not be possible.
  
  There is no safe way to bubble up vt errors through the stream because
  if nextSlice is called and multiple errors are returned, we can't
  coalesce them. We could modify that to return a partial result but its
  just more work for stream that is unnecessary. The handler can do all of
  this.
  
  This work was discovered due to cleanups to prepare for more C APIs.
  Less errors make C APIs easier to implement! And, it helps clean up our
  Zig, too.
  ```
- [`e75f895`](https://github.com/ghostty-org/ghostty/commit/e75f8956c576ea8acf6ee4e70d45f918738e7512) terminal: make stream processing infallible ([#11468](https://github.com/ghostty-org/ghostty/issues/11468)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The terminal.Stream next/nextSlice functions can now no longer fail. All
  prior failure modes were fully isolated in the handler `vt` callbacks.
  As such, vt callbacks are now required to not return an error and handle
  their own errors somehow.
  
  Allowing streams to be fallible before was an incorrect design. It
  caused problematic scenarios like in `nextSlice` early terminating
  processing due to handler errors. This should not be possible.
  
  There is no safe way to bubble up vt errors through the stream because
  if nextSlice is called and multiple errors are returned, we can't
  coalesce them. We could modify that to return a partial result but its
  just more work for stream that is unnecessary. The handler can do all of
  this.
  
  This work was discovered due to cleanups to prepare for more C APIs.
  Less errors make C APIs easier to implement! And, it helps clean up our
  Zig, too.
  ```
- [`6f8ffec`](https://github.com/ghostty-org/ghostty/commit/6f8ffecb89a4484a2fc587e0217263d28a7612e5) working basic search wrapping ([@rhodes-b](https://github.com/rhodes-b))
- [`af84fdb`](https://github.com/ghostty-org/ghostty/commit/af84fdbea8fbb1f9418f000151f99d880051a3ba) fix tests ([@rhodes-b](https://github.com/rhodes-b))
- [`04fa71e`](https://github.com/ghostty-org/ghostty/commit/04fa71e2377a386224cf6cf7af2ed0fbf757a9fd) Search wrap behavior ([#11449](https://github.com/ghostty-org/ghostty/issues/11449)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Search wrapping has been highly requested.
  
  some examples
  https://github.com/ghostty-org/ghostty/discussions/11080
  https://github.com/ghostty-org/ghostty/discussions/11440
  https://github.com/ghostty-org/ghostty/discussions/11441
  https://github.com/ghostty-org/ghostty/discussions/9762
  https://github.com/ghostty-org/ghostty/discussions/9790
  
  I also think it makes sense as its the default behavior in browsers (and
  I assume other apps)
  
  I tested where nothing is outputting and a loop where active was going
  into history not anything where pages would start to get reused though
  
  the following comment seems to me it should be safe to have wrap around
  behavior but maybe there was something else I missed about the active +
  history buffer on why that isn't true, testing basic cases it worked
  just fine for me
  
  
  https://github.com/ghostty-org/ghostty/blob/main/src/terminal/highlight.zig#L107-L111
  ```
- [`5fa1a99`](https://github.com/ghostty-org/ghostty/commit/5fa1a991d0838d7bd08a1130de16b05b99efb445) up to 1.3.2-dev ([@mitchellh](https://github.com/mitchellh))
- [`4c4e837`](https://github.com/ghostty-org/ghostty/commit/4c4e83784c5b8986d6d0a22c3f1e4fe79a4a3f03) macos: new tab applescript command should not activate application ([@mitchellh](https://github.com/mitchellh))
  ```text
  Related to #11457
  ```
- [`f3ac604`](https://github.com/ghostty-org/ghostty/commit/f3ac604fff76e29e6d827dae5f06e3eeebf7ebea) macos: select tab applescript command should not activate application ([#11459](https://github.com/ghostty-org/ghostty/issues/11459)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Related to #11457
  ```
- [`332b2ae`](https://github.com/ghostty-org/ghostty/commit/332b2aefc6e72d363aa93ab6ecfc86eeeeb5ed28) 1.3.1 ([@mitchellh](https://github.com/mitchellh))
- [`eccf960`](https://github.com/ghostty-org/ghostty/commit/eccf960def6f15dc33abaeff6f9b7ad3894db5dd) build(deps): bump dorny/paths-filter from 3.0.2 to 4.0.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [dorny/paths-filter](https://github.com/dorny/paths-filter) from 3.0.2 to 4.0.0.
  - [Release notes](https://github.com/dorny/paths-filter/releases)
  - [Changelog](https://github.com/dorny/paths-filter/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/dorny/paths-filter/compare/de90cc6fb38fc0963ad72b210f1f284cd68cea36...9d7afb8d214ad99e78fbd4247752c4caed2b6e4c)
  
  ---
  updated-dependencies:
  - dependency-name: dorny/paths-filter
    dependency-version: 4.0.0
    dependency-type: direct:production
    update-type: version-update:semver-major
  ...
  ```
- [`d4019fa`](https://github.com/ghostty-org/ghostty/commit/d4019fa484c821b8d3a1ef73d42357ae8d86f2b7) build(deps): bump dorny/paths-filter from 3.0.2 to 4.0.0 ([#11436](https://github.com/ghostty-org/ghostty/issues/11436)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps [dorny/paths-filter](https://github.com/dorny/paths-filter) from
  3.0.2 to 4.0.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/dorny/paths-filter/releases">dorny/paths-filter's
  releases</a>.</em></p>
  <blockquote>
  <h2>v4.0.0</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>feat: update action runtime to node24 by <a
  href="https://github.com/saschabratton"><code>@​saschabratton</code></a>
  in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/294">dorny/paths-filter#294</a></li>
  </ul>
  <h2>New Contributors</h2>
  <ul>
  <li><a
  href="https://github.com/saschabratton"><code>@​saschabratton</code></a>
  made their first contribution in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/294">dorny/paths-filter#294</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/dorny/paths-filter/compare/v3.0.3...v4.0.0">https://github.com/dorny/paths-filter/compare/v3.0.3...v4.0.0</a></p>
  <h2>v3.0.3</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>Add missing predicate-quantifier by <a
  href="https://github.com/wardpeet"><code>@​wardpeet</code></a> in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/279">dorny/paths-filter#279</a></li>
  </ul>
  <h2>New Contributors</h2>
  <ul>
  <li><a href="https://github.com/wardpeet"><code>@​wardpeet</code></a>
  made their first contribution in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/279">dorny/paths-filter#279</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/dorny/paths-filter/compare/v3...v3.0.3">https://github.com/dorny/paths-filter/compare/v3...v3.0.3</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/dorny/paths-filter/blob/master/CHANGELOG.md">dorny/paths-filter's
  changelog</a>.</em></p>
  <blockquote>
  <h1>Changelog</h1>
  <h2>v4.0.0</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/294">Update
  action runtime to node24</a></li>
  </ul>
  <h2>v3.0.3</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/279">Add
  missing predicate-quantifier</a></li>
  </ul>
  <h2>v3.0.2</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/224">Add
  config parameter for predicate quantifier</a></li>
  </ul>
  <h2>v3.0.1</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/133">Compare
  base and ref when token is empty</a></li>
  </ul>
  <h2>v3.0.0</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/210">Update to
  Node.js 20</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/215">Update
  all dependencies</a></li>
  </ul>
  <h2>v2.11.1</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/167">Update
  <code>@​actions/core</code> to v1.10.0 - Fixes warning about deprecated
  set-output</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/168">Document
  need for pull-requests: read permission</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/164">Updating
  to actions/checkout@v3</a></li>
  </ul>
  <h2>v2.11.0</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/157">Set
  list-files input parameter as not required</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/161">Update
  Node.js</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/162">Fix
  incorrect handling of Unicode characters in exec()</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/163">Use
  Octokit pagination</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/160">Updates
  real world links</a></li>
  </ul>
  <h2>v2.10.2</h2>
  <ul>
  <li><a href="https://redirect.github.com/dorny/paths-filter/pull/91">Fix
  getLocalRef() returns wrong ref</a></li>
  </ul>
  <h2>v2.10.1</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/85">Improve
  robustness of change detection</a></li>
  </ul>
  <h2>v2.10.0</h2>
  <ul>
  <li><a href="https://redirect.github.com/dorny/paths-filter/pull/82">Add
  ref input parameter</a></li>
  <li><a href="https://redirect.github.com/dorny/paths-filter/pull/83">Fix
  change detection in PR when pullRequest.changed_files is
  incorrect</a></li>
  </ul>
  <h2>v2.9.3</h2>
  <ul>
  <li><a href="https://redirect.github.com/dorny/paths-filter/pull/78">Fix
  change detection when base is a tag</a></li>
  </ul>
  <h2>v2.9.2</h2>
  <ul>
  <li><a href="https://redirect.github.com/dorny/paths-filter/pull/75">Fix
  fetching git history</a></li>
  </ul>
  <h2>v2.9.1</h2>
  <ul>
  <li><a href="https://redirect.github.com/dorny/paths-filter/pull/74">Fix
  fetching git history + fallback to unshallow repo</a></li>
  </ul>
  <h2>v2.9.0</h2>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/9d7afb8d214ad99e78fbd4247752c4caed2b6e4c"><code>9d7afb8</code></a>
  Update CHANGELOG for v4.0.0</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/782470c5d953cae2693d643172b14e01bacb71f3"><code>782470c</code></a>
  Merge branch 'releases/v3'</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/d1c1ffe0248fe513906c8e24db8ea791d46f8590"><code>d1c1ffe</code></a>
  Update CHANGELOG for v3.0.3</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/ce10459c8b92cd8901166c0a222fbb033ef39365"><code>ce10459</code></a>
  Merge pull request <a
  href="https://redirect.github.com/dorny/paths-filter/issues/294">#294</a>
  from saschabratton/master</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/5f40380c5482e806c81cec080f5192e7234d8fe9"><code>5f40380</code></a>
  feat: update action runtime to node24</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/668c092af3649c4b664c54e4b704aa46782f6f7c"><code>668c092</code></a>
  Merge pull request <a
  href="https://redirect.github.com/dorny/paths-filter/issues/279">#279</a>
  from wardpeet/patch-1</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/209e61402dbca8aa44f967535da6666b284025ed"><code>209e614</code></a>
  Add missing predicate-quantifier</li>
  <li>See full diff in <a
  href="https://github.com/dorny/paths-filter/compare/de90cc6fb38fc0963ad72b210f1f284cd68cea36...9d7afb8d214ad99e78fbd4247752c4caed2b6e4c">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=dorny/paths-filter&package-manager=github_actions&previous-version=3.0.2&new-version=4.0.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## March 12, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23023692641), [2](https://github.com/ghostty-org/ghostty/actions/runs/23020014641), [3](https://github.com/ghostty-org/ghostty/actions/runs/23016405050), [4](https://github.com/ghostty-org/ghostty/actions/runs/23012255263), [5](https://github.com/ghostty-org/ghostty/actions/runs/23006959585), [6](https://github.com/ghostty-org/ghostty/actions/runs/22985944795), [7](https://github.com/ghostty-org/ghostty/actions/runs/22984951308)  
Summary: 7 runs • 23 commits • 5 authors

### Changes

- [`64331b8`](https://github.com/ghostty-org/ghostty/commit/64331b8c35e2a39a9296594f9e6b096c54a8b49f) snap: Don't leak LD_LIBRARY_PATH set by the snap launcher ([@kenvandine](https://github.com/kenvandine))
- [`174aae3`](https://github.com/ghostty-org/ghostty/commit/174aae359d86c71be7bbe75f6c93166214fc4b1f) snap: Don't leak LD_LIBRARY_PATH set by the snap launcher ([#11431](https://github.com/ghostty-org/ghostty/issues/11431)) ([@kenvandine](https://github.com/kenvandine))
  ```text
  LD_LIBRARY_PATH was being leaked which could break some apps launched
  from ghostty, such as opening configuration in a text editor.
  ```
- [`d6d6fe4`](https://github.com/ghostty-org/ghostty/commit/d6d6fe4e5800f48846815a6cb2401c495e9ca57c) macOS: update window cascading ([@bo2themax](https://github.com/bo2themax))
  ```text
  Make it smaller and add comparisons between y values
  ```
- [`3022aa0`](https://github.com/ghostty-org/ghostty/commit/3022aa05ea82296adb598d340735f8339f5bf753) macOS: add test cases for drag-split ([@bo2themax](https://github.com/bo2themax))
- [`07bc888`](https://github.com/ghostty-org/ghostty/commit/07bc8886822bdc19932efea54e6d01bd230078cc) macOS: fix window position when dragging split into a new window ([@bo2themax](https://github.com/bo2themax))
- [`5c51603`](https://github.com/ghostty-org/ghostty/commit/5c51603b0b82a33c7461384e27ee67edbf3818fd) chore: make ci happy ([@bo2themax](https://github.com/bo2themax))
- [`597e8cf`](https://github.com/ghostty-org/ghostty/commit/597e8cf1c592d23fa8e69f64d1f43a20c44726ef) macOS: fix window position when dragging split into a new window ([#11429](https://github.com/ghostty-org/ghostty/issues/11429)) ([@mitchellh](https://github.com/mitchellh))
- [`77c2acf`](https://github.com/ghostty-org/ghostty/commit/77c2acf843e49c9566128fd2381a667077e4f2f8) macOS: add test case for window cascading without moving the window ([@bo2themax](https://github.com/bo2themax))
- [`ea262cd`](https://github.com/ghostty-org/ghostty/commit/ea262cdd34c36ac848ddd417cdf29a4dc93d7fb6) macOS: fix window cascading for 3rd+ window ([@bo2themax](https://github.com/bo2themax))
- [`5e38663`](https://github.com/ghostty-org/ghostty/commit/5e3866381b321bbc936f5de18e9f2b9622e0af4c) macOS: fix window cascading for the second window ([@bo2themax](https://github.com/bo2themax))
- [`a91e747`](https://github.com/ghostty-org/ghostty/commit/a91e747cb187dc143054b5c17ed2451d19422ef1) macOS: fix window cascading ([#11426](https://github.com/ghostty-org/ghostty/issues/11426)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Added test case for cascading **without moving previous window**, #11161
  will follow up for more accurate cascading after this.
  
  Fixed window cascading after last pr, now we should perform cascading
  **after** showing the window.
  ```
- [`c399812`](https://github.com/ghostty-org/ghostty/commit/c399812036a3161a7c2cf3b7dc63f4240949c607) macOS: add test case for positioning the very first window ([@bo2themax](https://github.com/bo2themax))
- [`4f849a1`](https://github.com/ghostty-org/ghostty/commit/4f849a15124b64dab955a489b77a80388b595523) macOS: fix window position for the very first window ([@bo2themax](https://github.com/bo2themax))
- [`08107d3`](https://github.com/ghostty-org/ghostty/commit/08107d342a1404ea095e48b0ee7fcc5299c2024f) macOS: we don't need initialFrame anymore ([@bo2themax](https://github.com/bo2themax))
- [`7068573`](https://github.com/ghostty-org/ghostty/commit/70685733c5947bdef9c8c7074419d0b15be86812) macOS: fix window position for the very first window ([#11421](https://github.com/ghostty-org/ghostty/issues/11421)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Depends on https://github.com/ghostty-org/ghostty/pull/11417
  
  Moved positioning part from `windowDidLoad` to `showWindow` to make new
  users happy. Also deleted `initialFrame`, since we don't need it
  anymore.
  ```
- [`d6dfaf2`](https://github.com/ghostty-org/ghostty/commit/d6dfaf28feb8e30834f18f987d1b909a3452e9fc) macOS: support injecting temporary defaults when testing ([@bo2themax](https://github.com/bo2themax))
- [`8dde340`](https://github.com/ghostty-org/ghostty/commit/8dde340f88d87bf1fa83cbbd312cf7962eaf284b) macOS: support injecting temporary defaults when testing ([#11417](https://github.com/ghostty-org/ghostty/issues/11417)) ([@mitchellh](https://github.com/mitchellh))
- [`84d48d1`](https://github.com/ghostty-org/ghostty/commit/84d48d1c6a9d4fb93eccd31cf0a731adbe174d02) config: add progress-style option ([@MOlechowski](https://github.com/MOlechowski))
  ```text
  Add option to disable OSC 9;4 ConEmu progress bars via config.
  
  Fixes #11241
  ```
- [`ab269e2`](https://github.com/ghostty-org/ghostty/commit/ab269e2c79d1540cd6d5aea74562ea4634c0104a) config: add progress-style option ([#11289](https://github.com/ghostty-org/ghostty/issues/11289)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Adds progress-style config to control OSC 9;4 progress bar visibility.
  Defaults to true, set false to hide.
  
  Fixes #11241
  
  AI Disclosure: Claude Code (Opus 4.6) used for codebase exploration,
  code review, and testing assistance. All code written and reviewed by
  hand.
  ```
- [`16ca952`](https://github.com/ghostty-org/ghostty/commit/16ca9527e95ea857a5cc6a30685bfcf58705af08) build(deps): bump actions/download-artifact from 8.0.0 to 8.0.1 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [actions/download-artifact](https://github.com/actions/download-artifact) from 8.0.0 to 8.0.1.
  - [Release notes](https://github.com/actions/download-artifact/releases)
  - [Commits](https://github.com/actions/download-artifact/compare/70fc10c6e5e1ce46ad2ea6f2b72d43f7d47b13c3...3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c)
  
  ---
  updated-dependencies:
  - dependency-name: actions/download-artifact
    dependency-version: 8.0.1
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`8093695`](https://github.com/ghostty-org/ghostty/commit/809369505534b40c83560f9cd0cbee8e7ecb7516) macos: only run key equivalents for Ghostty-owned menu items ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11396
  
  Track menu items populated from Ghostty keybind actions and only trigger
  those from SurfaceView performKeyEquivalent. This avoids app-default
  shortcuts such as Hide from pre-empting explicit keybinds.
  ```
- [`8392255`](https://github.com/ghostty-org/ghostty/commit/8392255fd6ed12dd5aad87eae0357ab6e69ec4a0) build(deps): bump actions/download-artifact from 8.0.0 to 8.0.1 ([#11399](https://github.com/ghostty-org/ghostty/issues/11399)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [actions/download-artifact](https://github.com/actions/download-artifact)
  from 8.0.0 to 8.0.1.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/actions/download-artifact/releases">actions/download-artifact's
  releases</a>.</em></p>
  <blockquote>
  <h2>v8.0.1</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>Support for CJK characters in the artifact name by <a
  href="https://github.com/danwkennedy"><code>@​danwkennedy</code></a> in
  <a
  href="https://redirect.github.com/actions/download-artifact/pull/471">actions/download-artifact#471</a></li>
  <li>Add a regression test for artifact name + content-type mismatches by
  <a href="https://github.com/danwkennedy"><code>@​danwkennedy</code></a>
  in <a
  href="https://redirect.github.com/actions/download-artifact/pull/472">actions/download-artifact#472</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/actions/download-artifact/compare/v8...v8.0.1">https://github.com/actions/download-artifact/compare/v8...v8.0.1</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/actions/download-artifact/commit/3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c"><code>3e5f45b</code></a>
  Add regression tests for CJK characters (<a
  href="https://redirect.github.com/actions/download-artifact/issues/471">#471</a>)</li>
  <li><a
  href="https://github.com/actions/download-artifact/commit/e6d03f67377d4412c7aa56a8e2e4988e6ec479dd"><code>e6d03f6</code></a>
  Add a regression test for artifact name + content-type mismatches (<a
  href="https://redirect.github.com/actions/download-artifact/issues/472">#472</a>)</li>
  <li>See full diff in <a
  href="https://github.com/actions/download-artifact/compare/70fc10c6e5e1ce46ad2ea6f2b72d43f7d47b13c3...3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=actions/download-artifact&package-manager=github_actions&previous-version=8.0.0&new-version=8.0.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`35f4d18`](https://github.com/ghostty-org/ghostty/commit/35f4d1880290d7f882f6f00fbafb46a49196e014) macos: only run key equivalents for Ghostty-owned menu items ([#11403](https://github.com/ghostty-org/ghostty/issues/11403)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11396
  
  Track menu items populated from Ghostty keybind actions and only trigger
  those from SurfaceView performKeyEquivalent. This avoids app-default
  shortcuts such as Hide from pre-empting explicit keybinds.
  ```

## March 11, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22970467471), [2](https://github.com/ghostty-org/ghostty/actions/runs/22967683770), [3](https://github.com/ghostty-org/ghostty/actions/runs/22964898207), [4](https://github.com/ghostty-org/ghostty/actions/runs/22964025677), [5](https://github.com/ghostty-org/ghostty/actions/runs/22963156248), [6](https://github.com/ghostty-org/ghostty/actions/runs/22961429369), [7](https://github.com/ghostty-org/ghostty/actions/runs/22957941413), [8](https://github.com/ghostty-org/ghostty/actions/runs/22945785511), [9](https://github.com/ghostty-org/ghostty/actions/runs/22945215801), [10](https://github.com/ghostty-org/ghostty/actions/runs/22942691693), [11](https://github.com/ghostty-org/ghostty/actions/runs/22934741901), [12](https://github.com/ghostty-org/ghostty/actions/runs/22934034203)  
Summary: 12 runs • 38 commits • 10 authors

### Changes

- [`0f745b5`](https://github.com/ghostty-org/ghostty/commit/0f745b56730ae0eff4de2e40e959d432cbdcb004) Update VOUCHED list ([#11389](https://github.com/ghostty-org/ghostty/issues/11389)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11388#discussioncomment-16087905)
  from @jcollie.
  
  Vouch: @wyounas
  ```
- [`fe98f38`](https://github.com/ghostty-org/ghostty/commit/fe98f3884d7dd72f0988949ab661beb018a191b4) macos: only show split grab handle when the mouse is near it ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11379
  
  For this pass, I made it a very simple "within 20%" (height-wise) of the
  split handle. There is no horizontal component. I want to find the right
  balance between always visible (today mostly) to only visible on direct
  hover, because I think it'll be too hard to discover on that far right
  side.
  ```
- [`a0d3566`](https://github.com/ghostty-org/ghostty/commit/a0d3566872c3bca4a139be3a49aaa9944040f95c) macos: only show split grab handle when the mouse is near it ([#11383](https://github.com/ghostty-org/ghostty/issues/11383)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11379
  
  For this pass, I made it a very simple "within 20%" (height-wise) of the
  split handle down. There is no horizontal component. I want to find the
  right balance between always visible (today mostly) to only visible on
  direct hover, because I think it'll be too hard to discover on that far
  right side.
  ```
- [`9503fa0`](https://github.com/ghostty-org/ghostty/commit/9503fa0786d3e79a5862361ae59db6d5972b4eae) nix: bump zig-overlay version ([@faukah](https://github.com/faukah))
- [`0af9938`](https://github.com/ghostty-org/ghostty/commit/0af9938ad2f2fb84d8e00501716933029bc0ba65) macos: add UI test for window position restore across titlebar styles ([@bo2themax](https://github.com/bo2themax))
  ```text
  Tests that window position and size are correctly restored after
  reopen for all four macos-titlebar-style variants.
  ```
- [`e8c82ca`](https://github.com/ghostty-org/ghostty/commit/e8c82ca1af29a8e911f328abe89bcc2650ec1705) macOS: save frame only if the window is visible ([@bo2themax](https://github.com/bo2themax))
- [`45d360d`](https://github.com/ghostty-org/ghostty/commit/45d360dc6879a80ca55f6f01ea36d9161732e099) macOS: set the initial window position after window is loaded ([@bo2themax](https://github.com/bo2themax))
- [`596d502`](https://github.com/ghostty-org/ghostty/commit/596d502a756ce6454093b5d0782bc17d700804ab) macOS: restore window frame under certain conditions ([@bo2themax](https://github.com/bo2themax))
- [`e31615d`](https://github.com/ghostty-org/ghostty/commit/e31615d00bf3811bdba4ae697c80fcb1ede3817a) bash: fix extra newlines with readline vi mode indicator ([@jparise](https://github.com/jparise))
  ```text
  Use OSC 133;P (prompt mark) instead of 133;A (fresh line + prompt mark)
  inside PS1 and PS2. Readline redraws the prompt on vi mode switches,
  Ctrl-L, and other events, and 133;A's fresh-line behavior would emit a
  CR+LF whenever the cursor wasn't at column 0, causing visible extra
  newlines.
  
  The one-time 133;A is now emitted via printf in __ghostty_precmd, which
  only runs once per prompt cycle via PROMPT_COMMAND. On SIGWINCH, bash
  redraws PS1 (firing the 133;P marks) but doesn't re-run PROMPT_COMMAND,
  so there's no unwanted fresh-line on resize either. The redraw=last flag
  persists from the initial printf.
  
  This is a little less optimal than our previous approach, in terms of
  number of prompt marks we emit, but it produces an overall more correct
  result, which is the important thing.
  
  Because readline prints its output outside the scope of PS1, those
  characters "inherit" the surrounded prompt scope. This is usually fine,
  but it can sometimes get out of sync (especially during redraws). This
  is inherently a limitation of the fact that it's a separate output
  channel, so we just have to accept that can happen.
  
  See: #11267
  ```
- [`7aff470`](https://github.com/ghostty-org/ghostty/commit/7aff470ceb220fbf58fd7e76cc7e342c7011d629) bash: fix extra newlines with readline vi mode indicator ([#11377](https://github.com/ghostty-org/ghostty/issues/11377)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Use OSC 133;P (prompt mark) instead of 133;A (fresh line + prompt mark)
  inside PS1 and PS2. Readline redraws the prompt on vi mode switches,
  Ctrl-L, and other events, and 133;A's fresh-line behavior would emit a
  CR+LF whenever the cursor wasn't at column 0, causing visible extra
  newlines.
  
  The one-time 133;A is now emitted via printf in __ghostty_precmd, which
  only runs once per prompt cycle via PROMPT_COMMAND. On SIGWINCH, bash
  redraws PS1 (firing the 133;P marks) but doesn't re-run PROMPT_COMMAND,
  so there's no unwanted fresh-line on resize either. The redraw=last flag
  persists from the initial printf.
  
  This is a little less optimal than our previous approach, in terms of
  number of prompt marks we emit, but it produces an overall more correct
  result, which is the important thing.
  
  Because readline prints its output outside the scope of PS1, those
  characters "inherit" the surrounded prompt scope. This is usually fine,
  but it can sometimes get out of sync (especially during redraws). This
  is inherently a limitation of the fact that it's a separate output
  channel, so we just have to accept that can happen.
  
  Fixes: #10953
  See: #11267
  ```
- [`12bc1e7`](https://github.com/ghostty-org/ghostty/commit/12bc1e786052a31d6f50cdbb0a703b45371a182d) macos: only show the grab handle in fullscreen if there are splits ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11376
  ```
- [`2296a82`](https://github.com/ghostty-org/ghostty/commit/2296a82c13f3621f25c2a5bb78280a80ac6c56b8) macOS: fix window frame when (re)opening new window ([#11380](https://github.com/ghostty-org/ghostty/issues/11380)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Claude wrote the fail path in the UI tests, or you can easily reproduce
  this manually. This is kinda a regression after #11322, since we are not
  delaying the frame update anymore, which exposes some of the "flaws" of
  the previous implementation.
  
  The following three commits fix this step by step:
  - We shouldn't save intermediate frames when the window is loading,
  which is triggered by `windowDidResize` and `windowDidMove` during the
  process.
  - We should set the initial position (from the config) after the window
  is loaded.
  - A small refactor on `LastWindowPosition` to support restoring the
  window frame under certain conditions.
  
  
  https://github.com/user-attachments/assets/6f90f9a5-653d-4146-95c6-8e5c69bda656
  
  
  
  ### AI Disclosure
  
  Claude helped me write the UI tests.
  ```
- [`19e5053`](https://github.com/ghostty-org/ghostty/commit/19e5053b28c524317c77d482a65b68f56fe372a4) macos: only show the grab handle in fullscreen if there are splits ([#11381](https://github.com/ghostty-org/ghostty/issues/11381)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11376
  ```
- [`36c1450`](https://github.com/ghostty-org/ghostty/commit/36c1450dc950c67e9acb008dd778d4ad813835df) nix: bump zig-overlay version ([#11375](https://github.com/ghostty-org/ghostty/issues/11375)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bump of `zig-overlay`, allowing us to drop flake-utils from the flake
  inputs. :)
  ```
- [`86c2a2e`](https://github.com/ghostty-org/ghostty/commit/86c2a2e87faa5996ac856c65718c0765be3fa3d0) input: add direct set_surface_title and set_tab_title actions ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11316
  
  This mirrors the `prompt` actions (hence why there is no window action
  here) and enables setting titles via keybind actions which importantly
  lets this work via command palettes, App Intents, AppleScript, etc.
  ```
- [`8ad9ec8`](https://github.com/ghostty-org/ghostty/commit/8ad9ec8e8806af12534080a38decc73322c877fe) add direct set_surface_title and set_tab_title actions ([#11373](https://github.com/ghostty-org/ghostty/issues/11373)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11316
  
  This mirrors the `prompt` actions (hence why there is no window action
  here) and enables setting titles via keybind actions which importantly
  lets this work via command palettes, App Intents, AppleScript, etc.
  ```
- [`f571c80`](https://github.com/ghostty-org/ghostty/commit/f571c806fec71a7de5b5ca0afc35eed92fa3cf9f) ci: skip vouched PRs for milestone attachment ([@mitchellh](https://github.com/mitchellh))
- [`d48b6ba`](https://github.com/ghostty-org/ghostty/commit/d48b6ba085eb96d2253e8a7f00c12e942a362a54) ci: skip vouched PRs for milestone attachment ([#11371](https://github.com/ghostty-org/ghostty/issues/11371)) ([@mitchellh](https://github.com/mitchellh))
- [`a8d38fe`](https://github.com/ghostty-org/ghostty/commit/a8d38fe5d807e8cf18f99dcef117355d02048d7c) Update VOUCHED list ([#11374](https://github.com/ghostty-org/ghostty/issues/11374)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11372#discussioncomment-16086042)
  from @mitchellh.
  
  Vouch: @faukah
  ```
- [`26d8bd9`](https://github.com/ghostty-org/ghostty/commit/26d8bd9e71c27f1f7f31a1079bee3ca79e79b205) bash: fix multiline PS1 with command substitutions ([@jparise](https://github.com/jparise))
  ```text
  Only replace the \n prompt escape when inserting secondary prompt marks,
  not literal newlines ($'\n'). Literal newlines may appear inside $(...)
  or `...` command substitutions, and inserting escape sequences there
  breaks the shell syntax. For example:
  
        PS1='$(if [ $? -eq 0 ]; then echo -e "P";
                      else echo -e "F";
                      fi) $ '
  
  The literal newlines between the if/else/fi are part of the shell syntax
  inside the command substitution. The previous code replaced all literal
  newlines in PS1 with newline + OSC 133 escape sequences, which injected
  terminal escapes into the middle of the command substitution and caused
  bash to report a syntax error when evaluating it.
  
  The \n prompt escape is PS1-specific and safe to replace globally. This
  means prompts using literal newlines for line breaks (rather than \n)
  won't get per-line secondary marks, but this is the conventional form
  and avoids the need for complex shell parsing.
  
  Fixes: #11267
  ```
- [`660767c`](https://github.com/ghostty-org/ghostty/commit/660767c77d077c1b7cef441fc2fa44f7dd666b08) bash: fix multiline PS1 with command substitutions ([#11369](https://github.com/ghostty-org/ghostty/issues/11369)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Only replace the \n prompt escape when inserting secondary prompt marks,
  not literal newlines `($'\n')`. Literal newlines may appear inside
  `$(...)` or `...` command substitutions, and inserting escape sequences
  there breaks the shell syntax. For example:
  
        PS1='$(if [ $? -eq 0 ]; then echo -e "P";
                      else echo -e "F";
                      fi) $ '
  
  The literal newlines between the if/else/fi are part of the shell syntax
  inside the command substitution. The previous code replaced all literal
  newlines in PS1 with newline + OSC 133 escape sequences, which injected
  terminal escapes into the middle of the command substitution and caused
  bash to report a syntax error when evaluating it.
  
  The \n prompt escape is PS1-specific and safe to replace globally. This
  means prompts using literal newlines for line breaks (rather than \n)
  won't get per-line secondary marks, but this is the conventional form
  and avoids the need for complex shell parsing.
  
  Fixes: #11267
  ```
- [`23f3cd5`](https://github.com/ghostty-org/ghostty/commit/23f3cd5f101fedcff6350648f8ba3993e6c55d90) zsh: improve prompt marking with dynamic themes ([@jparise](https://github.com/jparise))
  ```text
  Replace the strip-in-preexec / re-add-in-precmd pattern for OSC 133
  marks with a save/restore approach. Instead of pattern-matching marks
  out of PS1 (which exposes PS1 in intermediate states to other hooks), we
  save the original PS1/PS2 before adding marks and then restore them.
  
  This also adds dynamic theme detection: if PS1 changed between cycles
  (e.g., a theme rebuilt it), we skip injecting continuation marks into
  newlines. This prevents breaking plugins like Pure that use pattern
  matching to strip/rebuild the prompt.
  
  Additionally, move _ghostty_precmd to the end of precmd_functions in
  _ghostty_deferred_init (instead of substituting in-place) so that the
  first prompt is properly marked even when other hooks were appended
  after our auto-injection.
  
  There's one scenario that we still don't complete cover:
  
      precmd_functions+=(_test_overwrite_ps1)
      _test_overwrite_ps1() {
          PS1="test> "
      }
  
  ... which results in the first prompt not printing its prompt marks
  because _test_overwrite_ps1 becomes the last thing to run, overwriting
  our marks, but this will be fixed for subsequent prompts when we move
  our handler back to the last index.
  
  Fixes: #11282
  ```
- [`87e496b`](https://github.com/ghostty-org/ghostty/commit/87e496b30ff62a08e6dbdea651d86ea18b50493a) Update VOUCHED list ([#11368](https://github.com/ghostty-org/ghostty/issues/11368)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11365#issuecomment-4039534706)
  from @mitchellh.
  
  Vouch: @ydah
  ```
- [`c220654`](https://github.com/ghostty-org/ghostty/commit/c2206542d3bcb1b88eb4196620e553dad0717ca4) macos: fix tab title rename hit testing and focus handling in fullscreen mode ([@ydah](https://github.com/ydah))
- [`048a2d0`](https://github.com/ghostty-org/ghostty/commit/048a2d043a84eca4e67345eab2cdacb1a6390a70) Merge fix-fullscreen-tab-title-rename-hit into main ([@mitchellh](https://github.com/mitchellh))
- [`61865bc`](https://github.com/ghostty-org/ghostty/commit/61865bc37facf68056c4d0545a1dc4829550a8c1) zsh: improve prompt marking with dynamic themes ([#11367](https://github.com/ghostty-org/ghostty/issues/11367)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Replace the strip-in-preexec / re-add-in-precmd pattern for OSC 133
  marks with a save/restore approach. Instead of pattern-matching marks
  out of PS1 (which exposes PS1 in intermediate states to other hooks), we
  save the original PS1/PS2 before adding marks and then restore them.
  
  This also adds dynamic theme detection: if PS1 changed between cycles
  (e.g., a theme rebuilt it), we skip injecting continuation marks into
  newlines. This prevents breaking plugins like Pure that use pattern
  matching to strip/rebuild the prompt.
  
  Additionally, move _ghostty_precmd to the end of precmd_functions in
  _ghostty_deferred_init (instead of substituting in-place) so that the
  first prompt is properly marked even when other hooks were appended
  after our auto-injection.
  
  There's one scenario that we still don't complete cover:
  
      precmd_functions+=(_test_overwrite_ps1)
      _test_overwrite_ps1() {
          PS1="test> "
      }
  
  ... which results in the first prompt not printing its prompt marks
  because _test_overwrite_ps1 becomes the last thing to run, overwriting
  our marks, but this will be fixed for subsequent prompts when we move
  our handler back to the last index.
  
  Fixes: #11282
  ```
- [`ad6d366`](https://github.com/ghostty-org/ghostty/commit/ad6d3665c29b7e2db4da7e2a5fe67239d0f3df32) gtk: fix +new-window `--working-directory` inferrence. ([@jcollie](https://github.com/jcollie))
  ```text
  If the CLI argument `--working-directory` is not used with
  `+new-window`, the current working directory that `ghostty +new-window`
  is run from will be appended to the list of configuration data sent
  to the main Ghostty process. If `-e` _was_ used on the CLI, the
  `--working-directory` that was appended will be interpreted as part of
  the command to be executed, likely causing it to fail.
  
  Instead, insert `--working-directory` at the beginning of the list of
  configuration that it sent to the main Ghostty process.
  
  Fixes #11356
  ```
- [`76e9ee7`](https://github.com/ghostty-org/ghostty/commit/76e9ee7d376445a04421a7a78f5cc3e4787bcad4) gtk: fix +new-window `--working-directory` inferrence. ([#11357](https://github.com/ghostty-org/ghostty/issues/11357)) ([@pluiedev](https://github.com/pluiedev))
- [`82a8052`](https://github.com/ghostty-org/ghostty/commit/82a805296c3b45235571ecfa3b75821d9ca264b5) docs: fix backtick rendering in selection-word-chars default value ([@puzza007](https://github.com/puzza007))
  ```text
  The default value contains a literal backtick which broke inline code
  rendering on the website. Use double backtick delimiters to properly
  contain it.
  ```
- [`b992b66`](https://github.com/ghostty-org/ghostty/commit/b992b6605033d888c1c1afcf8015a6bf8cb9e7a5) docs: fix backtick rendering in selection-word-chars default value ([#11361](https://github.com/ghostty-org/ghostty/issues/11361)) ([@pluiedev](https://github.com/pluiedev))
- [`a644fca`](https://github.com/ghostty-org/ghostty/commit/a644fca5c5e74850312f13ed69f9677556abcd27) Update VOUCHED list ([#11360](https://github.com/ghostty-org/ghostty/issues/11360)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11358#discussioncomment-16080010)
  from @jcollie.
  
  Vouch: @puzza007
  ```
- [`6dd5b85`](https://github.com/ghostty-org/ghostty/commit/6dd5b856b05fbcb76f415ad18fbdfac600c3abde) macos: disable Tahoe one-time codes ([@mitchellh](https://github.com/mitchellh))
  ```text
  This disables all the automatic one-time code inputs in Ghostty.
  It'd be really neat to actually dynamically change this (not sure if its
  possible with NSTextContext or how often thats cached) but for now we
  should just fully disable it.
  ```
- [`dc18b25`](https://github.com/ghostty-org/ghostty/commit/dc18b25f86f59c79055ece87e158a5b27f625b05) macos: disable Tahoe one-time codes ([#11351](https://github.com/ghostty-org/ghostty/issues/11351)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This disables all the automatic one-time code inputs in Ghostty. It'd be
  really neat to actually dynamically change this (not sure if it's
  possible with NSTextContext or how often thats cached) but for now we
  should just fully disable it.
  
  Thanks to Ricky Mondello for the heads up on this.
  ```
- [`3293444`](https://github.com/ghostty-org/ghostty/commit/32934445cfb60e387013f4a7c4293352ac3aae44) macos: add TemporaryConfig for AI to write test cases ([@bo2themax](https://github.com/bo2themax))
- [`90dc431`](https://github.com/ghostty-org/ghostty/commit/90dc4315e2632faeb9771536cf526c46d33fc539) macos: add test cases for Ghostty.Config properties ([@bo2themax](https://github.com/bo2themax))
  ```text
  Test boolean, string, enum, and numeric config properties using
  TemporaryConfig to verify defaults and parsed values.
  ```
- [`85bec80`](https://github.com/ghostty-org/ghostty/commit/85bec8033474438182fbb33ded8dfcdcb009ea6a) build(deps): bump cachix/install-nix-action from 31.10.0 to 31.10.1 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [cachix/install-nix-action](https://github.com/cachix/install-nix-action) from 31.10.0 to 31.10.1.
  - [Release notes](https://github.com/cachix/install-nix-action/releases)
  - [Changelog](https://github.com/cachix/install-nix-action/blob/master/RELEASE.md)
  - [Commits](https://github.com/cachix/install-nix-action/compare/19effe9fe722874e6d46dd7182e4b8b7a43c4a99...1ca7d21a94afc7c957383a2d217460d980de4934)
  
  ---
  updated-dependencies:
  - dependency-name: cachix/install-nix-action
    dependency-version: 31.10.1
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`d5dab55`](https://github.com/ghostty-org/ghostty/commit/d5dab554aae398cc4b83c24d93bec20eaccbc5d9) build(deps): bump cachix/install-nix-action from 31.10.0 to 31.10.1 ([#11347](https://github.com/ghostty-org/ghostty/issues/11347)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [cachix/install-nix-action](https://github.com/cachix/install-nix-action)
  from 31.10.0 to 31.10.1.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/cachix/install-nix-action/releases">cachix/install-nix-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v31.10.1</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>nix: 2.34.0 -&gt; 2.34.1 by <a
  href="https://github.com/github-actions"><code>@​github-actions</code></a>[bot]
  in <a
  href="https://redirect.github.com/cachix/install-nix-action/pull/269">cachix/install-nix-action#269</a>
  Fixes a bug introduced in 2.34.0 that made the Nix daemon fail to load
  authentication keys configured by <code>cachix-action</code>.</li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/cachix/install-nix-action/compare/v31.10.0...v31.10.1">https://github.com/cachix/install-nix-action/compare/v31.10.0...v31.10.1</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/1ca7d21a94afc7c957383a2d217460d980de4934"><code>1ca7d21</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/install-nix-action/issues/269">#269</a>
  from cachix/create-pull-request/patch</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/b6137343272cafad497671822066f2a10ded6fef"><code>b613734</code></a>
  nix: 2.34.0 -&gt; 2.34.1</li>
  <li>See full diff in <a
  href="https://github.com/cachix/install-nix-action/compare/19effe9fe722874e6d46dd7182e4b8b7a43c4a99...1ca7d21a94afc7c957383a2d217460d980de4934">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=cachix/install-nix-action&package-manager=github_actions&previous-version=31.10.0&new-version=31.10.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`2a170b5`](https://github.com/ghostty-org/ghostty/commit/2a170b50c3ec088910645894f2d2e958ec381b42) macos: add test cases for Ghostty.Config properties ([#11263](https://github.com/ghostty-org/ghostty/issues/11263)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ### AI Disclosure
  
  Test cases is written using the Claude Agent in Xcode
  ```

## March 10, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22929804807), [2](https://github.com/ghostty-org/ghostty/actions/runs/22928895181), [3](https://github.com/ghostty-org/ghostty/actions/runs/22926107536), [4](https://github.com/ghostty-org/ghostty/actions/runs/22919665780), [5](https://github.com/ghostty-org/ghostty/actions/runs/22918391292), [6](https://github.com/ghostty-org/ghostty/actions/runs/22917096976), [7](https://github.com/ghostty-org/ghostty/actions/runs/22916232794), [8](https://github.com/ghostty-org/ghostty/actions/runs/22914796222), [9](https://github.com/ghostty-org/ghostty/actions/runs/22913587645), [10](https://github.com/ghostty-org/ghostty/actions/runs/22911767766), [11](https://github.com/ghostty-org/ghostty/actions/runs/22906920447), [12](https://github.com/ghostty-org/ghostty/actions/runs/22906644160), [13](https://github.com/ghostty-org/ghostty/actions/runs/22906186474)  
Summary: 13 runs • 33 commits • 7 authors

### Changes

- [`f9862cd`](https://github.com/ghostty-org/ghostty/commit/f9862cd4e27daf72e8e983646451a0954a47258b) GTK does support scrollbars ([@hulet](https://github.com/hulet))
- [`818e170`](https://github.com/ghostty-org/ghostty/commit/818e170ec0a16b501a78adc5ea9e197e142e877b) GTK does support scrollbars ([#11345](https://github.com/ghostty-org/ghostty/issues/11345)) ([@jcollie](https://github.com/jcollie))
  ```text
  Native GTK scrollbars are supported in 1.3.0:
  https://ghostty.org/docs/install/release-notes/1-3-0#scrollbars
  ```
- [`615af97`](https://github.com/ghostty-org/ghostty/commit/615af975f3365ea85594be7ebbc6ae90cac9558c) Update VOUCHED list ([#11344](https://github.com/ghostty-org/ghostty/issues/11344)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11343#discussioncomment-16075282)
  from @jcollie.
  
  Vouch: @hulet
  ```
- [`04d5efc`](https://github.com/ghostty-org/ghostty/commit/04d5efc8eb7b5f660bf44c0b63b9366c881e9635) config: working-directory expands ~/ prefix ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11336
  
  Introduce a proper WorkingDirectory tagged union type with home, inherit,
  and path variants. The field is now an optional (?WorkingDirectory) where
  null represents "use platform default" which is resolved during Config.finalize
  to .inherit (CLI) or .home (desktop launcher).
  ```
- [`0cb189b`](https://github.com/ghostty-org/ghostty/commit/0cb189bfbba4515797dee666e107d9b73b861ab0) config: working-directory expands ~/ prefix ([#11337](https://github.com/ghostty-org/ghostty/issues/11337)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11336
  
  Introduce a proper WorkingDirectory tagged union type with home,
  inherit, and path variants. The field is now an optional
  (?WorkingDirectory) where null represents "use platform default" which
  is resolved during Config.finalize to .inherit (CLI) or .home (desktop
  launcher).
  ```
- [`96f9772`](https://github.com/ghostty-org/ghostty/commit/96f9772cd838fa9d562ed369ea6fa8e657f870e3) tests: disable tests that fail if you have locally installed fonts ([@jcollie](https://github.com/jcollie))
  ```text
  If you have "Noto Sans Tai Tham" and/or "Noto Sans Javanese" installed
  locally on Linux, three tests fail. This PR disables those tests until a
  more permanent solution can be found.
  ```
- [`c131329`](https://github.com/ghostty-org/ghostty/commit/c1313294cd765e41c02e0b8e048fbad1beb5f740) add comments about why tests are disabled ([@jcollie](https://github.com/jcollie))
- [`a4cc37d`](https://github.com/ghostty-org/ghostty/commit/a4cc37db72bd345a7cdd90855e80339ed1caddd1) tests: disable tests that fail if you have locally installed fonts ([#11285](https://github.com/ghostty-org/ghostty/issues/11285)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  If you have "Noto Sans Tai Tham" and/or "Noto Sans Javanese" installed
  locally on Linux, three tests fail. This PR disables those tests until a
  more permanent solution can be found.
  ```
- [`71f8152`](https://github.com/ghostty-org/ghostty/commit/71f81527ad8d3393609d1e9134987653249473d4) macos: remove IntrinsicSizeTimingTests temporarily ([@mitchellh](https://github.com/mitchellh))
  ```text
  These were too flaky.
  ```
- [`8784636`](https://github.com/ghostty-org/ghostty/commit/8784636547520dc94d1b6ed2d58db00ed80eadfb) macos: remove IntrinsicSizeTimingTests temporarily ([#11332](https://github.com/ghostty-org/ghostty/issues/11332)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  These were too flaky.
  
  cc @bo2themax
  ```
- [`de0f2ab`](https://github.com/ghostty-org/ghostty/commit/de0f2ab22d941e270a4ba259ef2522f71bb84247) macos:  add enum type for macos-titlebar-style ([@bo2themax](https://github.com/bo2themax))
- [`53637ec`](https://github.com/ghostty-org/ghostty/commit/53637ec7b2b91da8e19b79cd755874b3fc2cf0db) fix jump_to_prompt forward behavior for multiline prompts ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11330.
  
  When jumping forward from prompt content, skip prompt continuation rows so a
  multiline prompt is treated as a single prompt block.
  ```
- [`7fb8e0a`](https://github.com/ghostty-org/ghostty/commit/7fb8e0ac90eeba0413736dee5b5b451d1a79ae20) fix jump_to_prompt forward behavior for multiline prompts ([#11331](https://github.com/ghostty-org/ghostty/issues/11331)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11330.
  
  When jumping forward from prompt content, skip prompt continuation rows
  so a multiline prompt is treated as a single prompt block.
  ```
- [`f88b42a`](https://github.com/ghostty-org/ghostty/commit/f88b42ad3968779168666eb03866f70e9a7568e4) macos: add enum type for macos-titlebar-style ([#11262](https://github.com/ghostty-org/ghostty/issues/11262)) ([@mitchellh](https://github.com/mitchellh))
- [`aaad43c`](https://github.com/ghostty-org/ghostty/commit/aaad43c23569e75929d611a13483e96cec6b1060) macos: make paste_from_clipboard performable on macos ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #10751
  ```
- [`c06ede5`](https://github.com/ghostty-org/ghostty/commit/c06ede584939979947336094c35b5a4c9a5ba267) macos: make paste_from_clipboard performable on macos ([#11328](https://github.com/ghostty-org/ghostty/issues/11328)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #10751
  ```
- [`f8d7876`](https://github.com/ghostty-org/ghostty/commit/f8d7876203ad65572cd085ff89afb758252217cb) Update VOUCHED list ([#11329](https://github.com/ghostty-org/ghostty/issues/11329)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11313#issuecomment-4033213188)
  from @mitchellh.
  
  Vouch: @VaughanAndrews
  ```
- [`6092c29`](https://github.com/ghostty-org/ghostty/commit/6092c299d55cd24ec72d3d5d2365279645c30ff3) macos: reset mouse state on focus loss to prevent phantom drag ([@seruman](https://github.com/seruman))
  ```text
  Fixes phantom mouse drag/selection when switching splits or apps.
  The suppressNextLeftMouseUp flag and core mouse click_state were not
  being reset on focus transitions, causing stale state that led to
  unexpected drag behavior.
  
  - Reset suppressNextLeftMouseUp in focusDidChange when losing focus
  - Defensively reset the flag when processing normal clicks
  - Reset core mouse.click_state and left_click_count on focus loss
  ```
- [`119ce0b`](https://github.com/ghostty-org/ghostty/commit/119ce0bc1df37be42cd65c57b4a3e8c39013b6c5) macos: reset mouse state on focus loss to prevent phantom drag ([#11276](https://github.com/ghostty-org/ghostty/issues/11276)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes https://github.com/ghostty-org/ghostty/discussions/11203
  
  The `suppressNextLeftMouseUp` flag from #11167 wasn't being reset on
  focus loss, causing stale state that led to phantom drags/selections and
  scrolls if you're lucky enough.
  
  I've followed the #11167 's path and made it reset on focus loss.
  
  As I stated in the [vouch
  request](https://github.com/ghostty-org/ghostty/discussions/11274); I'm
  not experienced in Swift, just following the prior PR's steps to reset
  the state. I've been using this patch for couple days and the change
  looks trivial to me tho not 100% sure if I'm missing anything.
  
  > [!NOTE]
  > Used Claude Code -Opus 4.6- for navigating the codebase and reviewing
  the change.
  ```
- [`d9039eb`](https://github.com/ghostty-org/ghostty/commit/d9039eb85a6f12ff7de205c116d978482c80bdab) config: don't double load app support path on macOS ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11323
  ```
- [`9759787`](https://github.com/ghostty-org/ghostty/commit/9759787847a0c6ed6983d1a8fe2b9c1d615b6010) config: don't double load app support path on macOS ([#11326](https://github.com/ghostty-org/ghostty/issues/11326)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11323
  ```
- [`4e24adf`](https://github.com/ghostty-org/ghostty/commit/4e24adf7177946af7f3d0e367d94fc8e2dead133) ci: skip xcode tests for freetype build ([@mitchellh](https://github.com/mitchellh))
- [`cfedda1`](https://github.com/ghostty-org/ghostty/commit/cfedda1a0e9197dfa7463a3a3aeb90ad980ab86f) macOS: add regression tests for intrinsicContentSize race ([#11256](https://github.com/ghostty-org/ghostty/issues/11256)) ([@bo2themax](https://github.com/bo2themax))
  ```text
  Tests that validate intrinsicContentSize returns a correct value when
  TerminalController.windowDidLoad() reads it. Currently fail, proving
  the race condition where @FocusedValue hasn't propagated
  lastFocusedSurface before the 40ms timer fires.
  ```
- [`a6cd1b0`](https://github.com/ghostty-org/ghostty/commit/a6cd1b08af240e7be0b07163d78dac5efa6b1752) macOS: fix intrinsicContentSize race in windowDidLoad ([#11256](https://github.com/ghostty-org/ghostty/issues/11256)) ([@bo2themax](https://github.com/bo2themax))
  ```text
  Add initialContentSize fallback on TerminalViewContainer so
  intrinsicContentSize returns the correct value immediately,
  without waiting for @FocusedValue to propagate. This removes
  the need for the DispatchQueue.main.asyncAfter 40ms delay.
  ```
- [`1592caf`](https://github.com/ghostty-org/ghostty/commit/1592cafa32e99119cee0b074fde3f50070ac3dac) Update AGENTS.md ([@mitchellh](https://github.com/mitchellh))
- [`7629130`](https://github.com/ghostty-org/ghostty/commit/7629130fb4f66262684d4b75d549b522d5943f59) macOS: restore keyboard focus after inline tab title edit ([@chronologos](https://github.com/chronologos))
  ```text
  After finishing an inline tab title edit (via keybind or double-click),
  `TabTitleEditor.finishEditing()` calls `makeFirstResponder(nil)` to
  clear focus from the text field, leaving the window itself as first
  responder. No code path restores focus to the terminal surface, so all
  keyboard input is lost until the user clicks into a pane.
  
  Add a `tabTitleEditorDidFinishEditing` delegate callback that fires
  after every edit (commit or cancel). TerminalWindow implements it by
  calling `makeFirstResponder(focusedSurface)` to hand focus back to the
  terminal.
  
  Fixes https://github.com/ghostty-org/ghostty/discussions/11315
  ```
- [`85f0972`](https://github.com/ghostty-org/ghostty/commit/85f0972b395c045fb91488399aeb6597c6be94ec) macOS: fix intrinsicContentSize race in windowDidLoad ([#11322](https://github.com/ghostty-org/ghostty/issues/11322)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This should fix #11256 and #11271.
  
  Tested manually with various combination of `window-width/height` and
  `macos-titlebar-style`.
  
  
  https://github.com/user-attachments/assets/90c12728-b195-47bf-abfd-8a4034b1e7a2
  
  
  ### AI Disclosure
  
  All the commits are generated by Claude, but orchestrated and manually
  tested by myself.
  ```
- [`3782d11`](https://github.com/ghostty-org/ghostty/commit/3782d118e1123c839eaff139bceb268ba5892bc7) macOS: restore keyboard focus after inline tab title edit ([#11320](https://github.com/ghostty-org/ghostty/issues/11320)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Summary
  
  - After finishing an inline tab title edit (via keybind or
  double-click), all keyboard input is lost because
  `TabTitleEditor.finishEditing()` sets `makeFirstResponder(nil)`, leaving
  the window itself as first responder with no path back to the terminal
  surface.
  - Adds a `tabTitleEditorDidFinishEditing` delegate callback to
  `TabTitleEditorDelegate` that fires after every edit (commit or cancel).
  - `TerminalWindow` implements it by calling
  `makeFirstResponder(focusedSurface)` to restore keyboard focus to the
  terminal.
  
  Fixes https://github.com/ghostty-org/ghostty/discussions/11315
  
  ## Testing
  
  - [x] Bind `prompt_tab_title` to a keybind (e.g. `keybind =
  cmd+shift+i=prompt_tab_title`)
  - [x] Trigger inline tab title edit via keybind, press Enter — verify
  keyboard input works immediately
  - [x] Trigger inline tab title edit via keybind, press Escape — verify
  keyboard input works immediately
  - [x] Double-click a tab title, press Enter — verify keyboard input
  works immediately
  - [x] Double-click a tab title, press Escape — verify keyboard input
  works immediately
  - [x] Verify Cmd+number tab switching works after all of the above
  - [x] Verify split pane focus is correct after editing tab title with
  splits open
  
  AI disclosure: Codebase exploration and review via [Claude
  Code](https://claude.com/claude-code)
  ```
- [`f8f431b`](https://github.com/ghostty-org/ghostty/commit/f8f431ba67e32b7fa0d63c54bc736d55cf27532f) docs: update bell-features docs for macOS ([@jcollie](https://github.com/jcollie))
  ```text
  PR #11154 didn't fully update the docs regarding `bell-features=audio`
  on macOS.
  ```
- [`e11f350`](https://github.com/ghostty-org/ghostty/commit/e11f350e8eb81ceda33a8267b6181c50e5be2789) docs: update bell-features docs for macOS ([#11279](https://github.com/ghostty-org/ghostty/issues/11279)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  PR #11154 didn't fully update the docs regarding `bell-features=audio`
  on macOS.
  ```
- [`6c73091`](https://github.com/ghostty-org/ghostty/commit/6c7309196fef805e1d0fbb0ce82944aab8edda7d) Update VOUCHED list ([#11321](https://github.com/ghostty-org/ghostty/issues/11321)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11320#issuecomment-4031703556)
  from @mitchellh.
  
  Vouch: @chronologos
  ```
- [`c83dea4`](https://github.com/ghostty-org/ghostty/commit/c83dea49fd1c4b89eee2956f8638b80122596bdc) Update VOUCHED list ([#11318](https://github.com/ghostty-org/ghostty/issues/11318)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11309#discussioncomment-16069391)
  from @mitchellh.
  
  Vouch: @dzhlobo
  ```
- [`327783f`](https://github.com/ghostty-org/ghostty/commit/327783ff6c86c5843eedaab20c7f394e4396daa4) Update VOUCHED list ([#11314](https://github.com/ghostty-org/ghostty/issues/11314)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11287#discussioncomment-16069141)
  from @mitchellh.
  
  Vouch: @ocean6954
  ```

## March 9, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22870694331), [2](https://github.com/ghostty-org/ghostty/actions/runs/22862195455), [3](https://github.com/ghostty-org/ghostty/actions/runs/22861709161), [4](https://github.com/ghostty-org/ghostty/actions/runs/22861225605), [5](https://github.com/ghostty-org/ghostty/actions/runs/22860218660), [6](https://github.com/ghostty-org/ghostty/actions/runs/22856309252), [7](https://github.com/ghostty-org/ghostty/actions/runs/22839029556), [8](https://github.com/ghostty-org/ghostty/actions/runs/22837001539), [9](https://github.com/ghostty-org/ghostty/actions/runs/22833175636)  
Summary: 9 runs • 21 commits • 6 authors

### Changes

- [`f8a0a45`](https://github.com/ghostty-org/ghostty/commit/f8a0a45963010e5cb3baa8069dbcc07a60c5d26d) Update VOUCHED list ([#11275](https://github.com/ghostty-org/ghostty/issues/11275)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11274#discussioncomment-16057271)
  from @jcollie.
  
  Vouch: @seruman
  ```
- [`703d11c`](https://github.com/ghostty-org/ghostty/commit/703d11c642a96af9e54b55b04f131bf3888948a9) Bump version to 1.3.0 ([@mitchellh](https://github.com/mitchellh))
- [`a6ee1fb`](https://github.com/ghostty-org/ghostty/commit/a6ee1fb292d2361bd3fca7998d1d86f6509b3272) macos: increase window-width/height apply delay from 10ms to 40ms ([@mitchellh](https://github.com/mitchellh))
  ```text
  Band-aid for #10304
  
  We don't have a robust fix yet but this should help mitigate more
  scenarios.
  ```
- [`8dde269`](https://github.com/ghostty-org/ghostty/commit/8dde2693bcd55e72a48c1b771f3e685e9bdfcfb6) macos: increase window-width/height apply delay from 10ms to 40ms ([#11265](https://github.com/ghostty-org/ghostty/issues/11265)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Band-aid for #10304
  
  We don't have a robust fix yet but this should help mitigate more
  scenarios.
  ```
- [`3c93c35`](https://github.com/ghostty-org/ghostty/commit/3c93c35869f40bd95db3e729549f05f48a371089) macOS: filter proper intrinsicContentSize when opening new window ([@bo2themax](https://github.com/bo2themax))
  ```text
  Fixes #11256
  ```
- [`3445c9a`](https://github.com/ghostty-org/ghostty/commit/3445c9afdad7d459ba42e0c66e25e0c09dda7eff) macOS: filter proper intrinsicContentSize when opening new window ([#11257](https://github.com/ghostty-org/ghostty/issues/11257)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11256, which is rather hard to reproduce on macOS 26, but after
  adding breaking points on size update, we can see that it happens when
  the `intrinsicContentSize` is not properly updated.
  
  <img width="998" height="556" alt="Xnip2026-03-09_11-38-40"
  src="https://github.com/user-attachments/assets/8ac1de91-5895-45fc-a443-002eb016a1ce"
  />
  ```
- [`dd3d72c`](https://github.com/ghostty-org/ghostty/commit/dd3d72c3de474c10da7e1576e39c7e2e7ad7617f) Revert "macOS: filter proper intrinsicContentSize when opening new window ([#11257](https://github.com/ghostty-org/ghostty/issues/11257))" ([@mitchellh](https://github.com/mitchellh))
  ```text
  This reverts commit 3445c9afdad7d459ba42e0c66e25e0c09dda7eff, reversing
  changes made to 1e981f858a4833ae63e7e53f9f0c84c516b4241e.
  ```
- [`3ba49a7`](https://github.com/ghostty-org/ghostty/commit/3ba49a784f4313e301efb68362158e8e338662da) terminal: fix grapheme edge-wrap hyperlink integrity panic ([@mitchellh](https://github.com/mitchellh))
  ```text
  When a grapheme expands to width 2 at the screen edge, this path can write
  spacer_head before printWrap() sets row.wrap. With an active hyperlink,
  printCell triggers hyperlink bookkeeping and page integrity checks in that
  intermediate state, causing UnwrappedSpacerHead.
  
  Mark row.wrap before writing spacer_head in this grapheme-wrap path to keep
  the intermediate state valid.
  ```
- [`1e981f8`](https://github.com/ghostty-org/ghostty/commit/1e981f858a4833ae63e7e53f9f0c84c516b4241e) terminal: fix grapheme edge-wrap hyperlink integrity panic ([#11264](https://github.com/ghostty-org/ghostty/issues/11264)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  When a grapheme expands to width 2 at the screen edge, this path can
  write spacer_head before printWrap() sets row.wrap. With an active
  hyperlink, printCell triggers hyperlink bookkeeping and page integrity
  checks in that intermediate state, causing UnwrappedSpacerHead.
  
  Mark row.wrap before writing spacer_head in this grapheme-wrap path to
  keep the intermediate state valid.
  ```
- [`fd557e8`](https://github.com/ghostty-org/ghostty/commit/fd557e83474e23b42d0f5133df319a79eda66653) bash: only define $__ghostty_ps0 when unset ([@jparise](https://github.com/jparise))
  ```text
  This fixes an error if the script was sourced a second time:
  
      bash: __ghostty_ps0: readonly variable
  
  Because this is a non-exported variable, this would only happen if the
  script was sourced multiple times in the same bash session.
  ```
- [`0a659af`](https://github.com/ghostty-org/ghostty/commit/0a659af55ff214c781347def6f41d7aaed63b84a) bash: handle existing ; in PROMPT_COMMAND ([@jparise](https://github.com/jparise))
  ```text
  If an existing PROMPT_COMMAND was a string ending in ; (and maybe some
  spaces), we'd add a redundant ;, resulting in a syntax error. Now we
  strip any trailing `;[[:space:]]*` characters from the original string
  before add ours.
  ```
- [`308b713`](https://github.com/ghostty-org/ghostty/commit/308b713e5828a3e1b07238f3ab56d75914389e3b) bash: handle existing ; in PROMPT_COMMAND ([#11260](https://github.com/ghostty-org/ghostty/issues/11260)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  If an existing PROMPT_COMMAND was a string ending in ; (and maybe some
  spaces), we'd add a redundant ;, resulting in a syntax error. Now we
  strip any trailing `;[[:space:]]*` characters from the original string
  before add ours.
  
  Fixes #11259
  ```
- [`f4c40c7`](https://github.com/ghostty-org/ghostty/commit/f4c40c7d53c1de1fcc97413fd6d543a561924e89) bash: only define $__ghostty_ps0 when unset ([#11258](https://github.com/ghostty-org/ghostty/issues/11258)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This fixes an error if the script was sourced a second time:
  
      bash: __ghostty_ps0: readonly variable
  
  Because this is a non-exported variable, this would only happen if the
  script was sourced multiple times in the same bash session.
  ```
- [`aee9361`](https://github.com/ghostty-org/ghostty/commit/aee9361fa3fdd95177823fe1ffa2b8ff19e7e413) Update es_AR.po ([@dariogriffo](https://github.com/dariogriffo))
  ```text
  Minor updates
  ```
- [`2cb8f61`](https://github.com/ghostty-org/ghostty/commit/2cb8f61bcfafeae1382edd23a1c105ab25c7a8c8) Update es_AR.po ([@dariogriffo](https://github.com/dariogriffo))
- [`c570d53`](https://github.com/ghostty-org/ghostty/commit/c570d53d45218aae294c52fa81d48220755fe692) Update es_AR.po ([@dariogriffo](https://github.com/dariogriffo))
- [`4969b0c`](https://github.com/ghostty-org/ghostty/commit/4969b0c56ecf65e0639e978a6bb9e7f076273afe) Update es_AR.po ([@dariogriffo](https://github.com/dariogriffo))
- [`9dc6f67`](https://github.com/ghostty-org/ghostty/commit/9dc6f6763f12d056e286ca62e02f960b19a8fb9e) Update es_AR.po translation for "Unable to acquire an OpenGL context for rendering." ([#11227](https://github.com/ghostty-org/ghostty/issues/11227)) ([@00-kat](https://github.com/00-kat))
  ```text
  - "Unable to acquire an OpenGL context for rendering."
  This could be translated to "No se puede" or "No se pudo", depends on
  the context of the message.
  If the message is showing a current intent the translation should be "No
  se puede", if the message is communicating that Ghostty failed to
  acquire the OpenGL then the translation should be "No se pudo", here I
  need more context.
  Either case the wording "No se puedo" is incorrect.
  ```
- [`233fb12`](https://github.com/ghostty-org/ghostty/commit/233fb12081009fee649295d323c93716655fc671) macos: add AppleScript front window and focused terminal properties ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds two new propeties to make it easy to get the frontmost (main)
  window and the focused terminal within a tab. We already had a property
  to get the selected tab of a tab group.
  ```
- [`b82d452`](https://github.com/ghostty-org/ghostty/commit/b82d452f486bbff6977ee4e5472e3cf9163e9b7a) macos: add AppleScript front window and focused terminal properties ([#11251](https://github.com/ghostty-org/ghostty/issues/11251)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This adds two new propeties to make it easy to get the frontmost (main)
  window and the focused terminal within a tab. We already had a property
  to get the selected tab of a tab group.
  
  ## Examples
  
  ### Send Input to Focused Terminal
  
  ```AppleScript
  tell application "Ghostty"
    set term to focused terminal of selected tab of front window
    input text "pwd\n" to term
  end tell
  ```
  
  ### Split the Focused Terminal
  
  ```applescript
  tell application "Ghostty"
    set currentTerm to focused terminal of selected tab of front window
    set newTerm to split currentTerm direction right
    input text "echo split-ready\n" to newTerm
  end tell
  ```
  ````
- [`ec1ca4c`](https://github.com/ghostty-org/ghostty/commit/ec1ca4c0c903d13a15452c18b1df11b3cabddaf7) Update VOUCHED list ([#11247](https://github.com/ghostty-org/ghostty/issues/11247)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11246#discussioncomment-16045992)
  from @jcollie.
  
  Vouch: @jmcgover
  ```

