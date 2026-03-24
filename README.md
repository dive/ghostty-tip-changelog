> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: March 24, 2026 at 12:16 UTC.

## March 24, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23472855296), [2](https://github.com/ghostty-org/ghostty/actions/runs/23469421167), [3](https://github.com/ghostty-org/ghostty/actions/runs/23468473879)  
Summary: 3 runs • 5 commits • 5 authors

### Changes

- [`7d31d9b`](https://github.com/ghostty-org/ghostty/commit/7d31d9b57f7064f74cd8a098189d2f9248ef4dd5) cmake: add import library to custom command OUTPUT ([@deblasis](https://github.com/deblasis))
  ```text
  Ninja requires all produced files to be listed as explicit outputs of
  custom commands. The zig build produces a .lib import library alongside
  the DLL, but it was not listed in the OUTPUT directive. This causes
  Ninja to fail with "missing and no known rule to make it" when
  IMPORTED_IMPLIB references the .lib file.
  ```
- [`d4a38c8`](https://github.com/ghostty-org/ghostty/commit/d4a38c8661453026bd1b1bb022ba2c37b347adce) cmake: add import library to custom command OUTPUT ([#11794](https://github.com/ghostty-org/ghostty/issues/11794)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  # What
  
  PR #11756 added IMPORTED_IMPLIB pointing to the .lib import library, but
  the
  import library is not listed in the OUTPUT directive of the
  `add_custom_command`
  that runs zig build. The file is produced as a side-effect of the build.
  
  This works with the Visual Studio generator (which is lenient about
  undeclared outputs) but fails with Ninja:
  
  ninja: error: 'zig-out/lib/ghostty-vt.lib', needed by 'ghostling',
  missing and no known rule to make it
  
  The fix adds "${ZIG_OUT_DIR}/lib/${GHOSTTY_VT_IMPLIB}" to the OUTPUT
  list. No
  behavioral change. The file was already being built, Ninja just needs to
  know
  about it.
  
  ## but_why.gif
  
  I am cleaning up https://github.com/ghostty-org/ghostling/pull/6 and I
  realise that in order to get rid of the CMake workarounds we had before
  #11756, this change is necessary.
  
  # POC
  
  I set up a branch pointing at my fork with a POC and it builds, this is
  the cleaned up CMakeList
  https://github.com/deblasis/winghostling/blob/test/cmake-implib-no-workaround/CMakeLists.txt
  ```
- [`147596d`](https://github.com/ghostty-org/ghostty/commit/147596d5608e3274e4b77fcdc201560f46fdb7c1) build(deps): bump cachix/install-nix-action from 31.10.1 to 31.10.2 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [cachix/install-nix-action](https://github.com/cachix/install-nix-action) from 31.10.1 to 31.10.2.
  - [Release notes](https://github.com/cachix/install-nix-action/releases)
  - [Changelog](https://github.com/cachix/install-nix-action/blob/master/RELEASE.md)
  - [Commits](https://github.com/cachix/install-nix-action/compare/1ca7d21a94afc7c957383a2d217460d980de4934...51f3067b56fe8ae331890c77d4e454f6d60615ff)
  
  ---
  updated-dependencies:
  - dependency-name: cachix/install-nix-action
    dependency-version: 31.10.2
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`c584f87`](https://github.com/ghostty-org/ghostty/commit/c584f87b9037455e38bd96808089f8740efb3e6c) build(deps): bump cachix/install-nix-action from 31.10.1 to 31.10.2 ([#11790](https://github.com/ghostty-org/ghostty/issues/11790)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [cachix/install-nix-action](https://github.com/cachix/install-nix-action)
  from 31.10.1 to 31.10.2.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/cachix/install-nix-action/releases">cachix/install-nix-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v31.10.2</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>nix: 2.34.1 -&gt; 2.34.2 by <a
  href="https://github.com/github-actions"><code>@​github-actions</code></a>[bot]
  in <a
  href="https://redirect.github.com/cachix/install-nix-action/pull/270">cachix/install-nix-action#270</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/cachix/install-nix-action/compare/v31...v31.10.2">https://github.com/cachix/install-nix-action/compare/v31...v31.10.2</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/51f3067b56fe8ae331890c77d4e454f6d60615ff"><code>51f3067</code></a>
  Revert &quot;ci: use 25.11 for channel tests&quot;</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/15118c17f94ae94b32a2a51839986d18c508f12f"><code>15118c1</code></a>
  ci: use 25.11 for channel tests</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/e1ac057965e5be579300ea6beb1f0e9a8a607344"><code>e1ac057</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/install-nix-action/issues/270">#270</a>
  from cachix/create-pull-request/patch</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/d181b9642fe3b3f85724b0337c37dca054cb4ef8"><code>d181b96</code></a>
  nix: 2.34.1 -&gt; 2.34.2</li>
  <li>See full diff in <a
  href="https://github.com/cachix/install-nix-action/compare/1ca7d21a94afc7c957383a2d217460d980de4934...51f3067b56fe8ae331890c77d4e454f6d60615ff">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=cachix/install-nix-action&package-manager=github_actions&previous-version=31.10.1&new-version=31.10.2)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`846599b`](https://github.com/ghostty-org/ghostty/commit/846599b97ef17a99cab699927b480e75aa36c5ac) Update VOUCHED list ([#11791](https://github.com/ghostty-org/ghostty/issues/11791)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11460#discussioncomment-16285158)
  from @00-kat.
  
  Vouch: @viruslobster
  ```

## March 23, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23465479473), [2](https://github.com/ghostty-org/ghostty/actions/runs/23463779213), [3](https://github.com/ghostty-org/ghostty/actions/runs/23461217695), [4](https://github.com/ghostty-org/ghostty/actions/runs/23458735124), [5](https://github.com/ghostty-org/ghostty/actions/runs/23457617226), [6](https://github.com/ghostty-org/ghostty/actions/runs/23451621230), [7](https://github.com/ghostty-org/ghostty/actions/runs/23449313767), [8](https://github.com/ghostty-org/ghostty/actions/runs/23447242926), [9](https://github.com/ghostty-org/ghostty/actions/runs/23443898888), [10](https://github.com/ghostty-org/ghostty/actions/runs/23443121106), [11](https://github.com/ghostty-org/ghostty/actions/runs/23442314075)  
Summary: 11 runs • 64 commits • 6 authors

### Changes

- [`c1e616c`](https://github.com/ghostty-org/ghostty/commit/c1e616c6cda402c6823d97dba89dde690808f2b7) libghostty: add ghostty_free for cross-runtime memory safety ([@deblasis](https://github.com/deblasis))
  ```text
  On Windows, Zig's built-in libc and MSVC's CRT maintain separate
  heaps, so calling free() on memory allocated by the library causes
  undefined behavior. Add ghostty_free() that frees through the same
  allocator that performed the allocation, making it safe on all
  platforms.
  
  Update format_alloc docs and all examples to use ghostty_free()
  instead of free().
  ```
- [`7039f56`](https://github.com/ghostty-org/ghostty/commit/7039f566bb5db987707a9a4fd8637575b595ffaa) vt: move free_alloc to dedicated allocator.zig ([@mitchellh](https://github.com/mitchellh))
  ```text
  Extract the inline free_alloc function from main.zig into a new
  allocator.zig module in the C API layer. The function is renamed
  to alloc_free in main.zig (and free in allocator.zig) for
  consistency with the other C API naming conventions. Add tests
  for null pointer, allocated memory, and null allocator fallback.
  ```
- [`b819ce0`](https://github.com/ghostty-org/ghostty/commit/b819ce0e20c14d649613c8fb39705b5893960b9c) vt: add ghostty_alloc for buffer allocation ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a ghostty_alloc function that pairs with the existing
  ghostty_free, giving embedders a symmetric malloc/free-style
  API for buffer allocation through the libghostty allocator
  interface. Returns NULL on allocation failure.
  ```
- [`67db6b8`](https://github.com/ghostty-org/ghostty/commit/67db6b896079a14f14d8e18492870e9b33443d4a) libghostty: add ghostty_free for cross-runtime memory safety ([#11785](https://github.com/ghostty-org/ghostty/issues/11785)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## What
  
  On Windows, calling `free()` on memory allocated by libghostty crashes
  because Zig and MSVC use separate heaps.
  
  This adds `ghostty_free()` so consumers can free library-allocated
  memory safely on all platforms.
  
  ## Why
  
  When Zig builds a DLL on Windows with `link_libc = true`, it does not
  link the Windows C runtime (`ucrtbase.dll`). Instead it uses its own
  libc built on top of `KERNEL32.dll`. So `builtin.link_libc` is true and
  `c_allocator` is selected, but Zig's `malloc` and MSVC's `malloc` are
  different implementations with different heaps. 💥
  
  On Linux/macOS this is not a problem because Zig links the system libc
  and everyone shares the same heap. On Windows, `free(buf)` from MSVC
  tries to free memory from Zig's heap and you get a debug assertion
  failure or undefined behavior.
  
  The `format_alloc` docs said "the buffer can be freed with `free()`" but
  that is only true when the library and consumer share the same C
  runtime, which is not the case on Windows.
  
  ## How
  
  - Add `ghostty_free(allocator, ptr, len)` that frees through the same
  allocator that did the allocation
  - Update `format_alloc` docs to point to `ghostty_free()` instead of
  `free()`
  - Update all 3 examples to use `ghostty_free(NULL, buf, len)`
  
  The signature takes an allocator because raw buffers (unlike objects
  like terminals or formatters) do not store their allocator internally.
  The caller already has all three values: the allocator they passed, the
  pointer, and the length they got back.
  
  I went back and forth on the naming. Other options I considered:
  `ghostty_alloc_free(allocator, ptr, len)` or returning a `GhosttyBuffer`
  wrapper with its own `_free`. Happy to change the naming if there is a
  preference.
  
  No impact on Linux/macOS. `ghostty_free()` works correctly there too, it
  just happens to call the same `free()` the consumer would have called
  anyway.
  
  ## Verified
  
  - `zig build test-lib-vt` passes on Windows, macOS arm64, Linux x86_64
  (exit 0)
  - `zig build test` passes on Windows (2575/2619 passed, 1 pre-existing
  font sprite failure) and macOS (exit 0)
  - cmake shared example builds, links, and runs correctly on Windows with
  `ghostty_free()` (no more heap crash)
  
  ## What I Learnt
  
  - What I wrote in Why
  - Zig allocators require the length to free (no hidden metadata headers
  like C's malloc). This is a deliberate design choice for explicit
  control.
  - The standard pattern for C libraries on Windows is "whoever allocates,
  frees" (like `curl_free()`, `SDL_free()`). This avoids cross-runtime
  heap issues entirely.
  ```
- [`07272ae`](https://github.com/ghostty-org/ghostty/commit/07272ae88f4e15608383f0cc786586ec84d66e41) stream: add bell effect callback support ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add an Effects struct to the readonly stream Handler that allows
  callers to provide optional callbacks for side effects like bell.
  Previously, the bell action was silently ignored along with other
  query/response actions. Now it is handled separately and dispatched
  through the effects callback if one is provided.
  
  Add a test that verifies bell with a null callback (default readonly
  behavior) does not crash, and that a provided callback is invoked
  the correct number of times.
  ```
- [`67d8d86`](https://github.com/ghostty-org/ghostty/commit/67d8d86efd8d180df43b35978648c59f2cabd477) terminal: rename ReadonlyStream to TerminalStream ([@mitchellh](https://github.com/mitchellh))
  ```text
  Rename stream_readonly.zig to stream_terminal.zig and its exported
  types from ReadonlyStream/ReadonlyHandler to TerminalStream. The
  "readonly" name is now wrong since the handler now supports
  settable effects callbacks. The new name better reflects that this
  is a stream handler for updating terminal state.
  ```
- [`e24cc1b`](https://github.com/ghostty-org/ghostty/commit/e24cc1b53bb8012d83fdb4e55fbedf6602611596) terminal: add write_pty effect and implement DECRQM ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a generic write_pty effect callback to the stream terminal
  handler, allowing callers to receive pty response data. Use it to
  implement request_mode and request_mode_unknown (DECRQM), which
  encode the mode state as a DECRPM response and write it back
  through the callback. Previously these were silently ignored.
  
  The write_pty data is stack-allocated and only valid for the
  duration of the call.
  ```
- [`6366ce9`](https://github.com/ghostty-org/ghostty/commit/6366ce9a220e6a445d0632c3b75e9b336b3d424e) terminal: add set_window_title effect to stream handler ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously the window_title action was silently ignored in the
  readonly stream handler. Add a set_window_title callback to the
  Effects struct so callers can be notified when a window title is
  set via OSC 2. Follows the same pattern as bell and write_pty
  where the callback is optional and defaults to null in readonly
  mode.
  ```
- [`08a44d7`](https://github.com/ghostty-org/ghostty/commit/08a44d7e696428737e2330fb275f94ea18f41b4b) terminal: store title set by escape sequences ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a title field to Terminal, mirroring the existing pwd field.
  The title is set via setTitle/getTitle and tracks the most recent
  value written by OSC 0/2 sequences. The stream handler now persists
  the title in terminal state in addition to forwarding it to the
  surface. The field is cleared on full reset.
  ```
- [`22c7edf`](https://github.com/ghostty-org/ghostty/commit/22c7edf3f8d17a189504323dc1a6267e43281c9b) terminal: rename set_window_title effect to title_changed ([@mitchellh](https://github.com/mitchellh))
  ```text
  The effect callback no longer receives the title string directly.
  Instead, the handler stores the title in terminal state via setTitle
  before invoking the callback, so consumers query it through
  handler.terminal.getTitle(). This removes the redundant parameter
  and keeps the effect signature consistent with the new terminal
  title field. Tests now verify terminal state directly rather than
  tracking the title through the callback.
  ```
- [`1345163`](https://github.com/ghostty-org/ghostty/commit/134516310d3b73d828c67de1eb107d0b754e111a) terminal: implement kitty_keyboard_query in stream_terminal ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously kitty_keyboard_query was listed as a no-op in the
  readonly stream handler. This implements it using the write_pty
  effect callback so that the current kitty keyboard flags are
  reported back via the pty, matching the behavior in the full
  stream handler.
  ```
- [`26c81b4`](https://github.com/ghostty-org/ghostty/commit/26c81b4b0e2f7e0c70ac7face8f33cff5f68c7f1) terminal: add xtversion effect to stream_terminal ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add an xtversion callback to the Effects struct so that
  stream_terminal can respond to XTVERSION queries. The callback
  returns the version string to embed in the DCS response. If the
  callback is unset or returns an empty string, the response defaults
  to "libghostty". The response is formatted and written back via the
  existing write_pty effect.
  ```
- [`6083e9f`](https://github.com/ghostty-org/ghostty/commit/6083e9f80bc06de4b734e736cf07ed6f0575953a) terminal: expose size_report via stream_terminal effects ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a `size` callback to the stream_terminal Effects struct that
  returns a size_report.Size geometry snapshot for XTWINOPS size
  queries (CSI 14/16/18 t). The handler owns all protocol encoding
  using the existing size_report.encode, keeping VT knowledge out
  of effect consumers. This follows the same pattern as the xtversion
  effect: the callback supplies data, the handler formats the reply
  and calls write_pty.
  
  CSI 21 t (title report) is handled internally from terminal state
  since the title is already available via terminal.getTitle() and
  does not require an external callback.
  ```
- [`b9669e1`](https://github.com/ghostty-org/ghostty/commit/b9669e10c40a0f3390f5d573656f25ba5e154716) fuzz: update stream fuzzer to use TerminalStream ([@mitchellh](https://github.com/mitchellh))
  ```text
  ReadonlyStream was removed from the public API. Update the stream
  fuzzer to use TerminalStream, which is the type now returned by
  Terminal.vtStream().
  ```
- [`165e036`](https://github.com/ghostty-org/ghostty/commit/165e03669ce53263b1763e42e9beaf39b0911fd6) terminal: port enquiry to Effects ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously the ENQ (0x05) action was ignored in stream_terminal,
  listed in the no-op group alongside other unhandled queries. The
  real implementation in termio/stream_handler writes a configurable
  response string back to the pty.
  
  Add an enquiry callback to Effects following the same query-style
  pattern as xtversion: the callback returns the raw response bytes
  and the handler owns writing them to the pty via writePty. When no
  callback is set (readonly mode), ENQ is silently ignored. Empty
  responses are also ignored. The response is capped at 256 bytes
  using a stack buffer with sentinel conversion for writePty.
  ```
- [`2e7aa04`](https://github.com/ghostty-org/ghostty/commit/2e7aa047af3692ff6c6fa003f078d772c6db697d) terminal: port device_status to stream_terminal Effects ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously device_status was in the ignored "no terminal-modifying
  effect" group in stream_terminal.zig. This ports it to use the
  Effects pattern, handling all three DSR request types.
  
  Operating status and cursor position are handled entirely within
  stream_terminal since they only need terminal state and write_pty.
  Cursor position respects origin mode and scrolling region offsets.
  
  Color scheme adds a new color_scheme effect callback that returns
  a ColorScheme enum (light/dark). The handler encodes the response
  internally, keeping protocol knowledge in the terminal layer. A
  new ColorScheme type is added to device_status.zig so the terminal
  layer does not depend on apprt.
  ```
- [`b31dcf9`](https://github.com/ghostty-org/ghostty/commit/b31dcf9a4cc0e00652d8fa62c4abb0364ad0263a) terminal: add device_attributes module ([@mitchellh](https://github.com/mitchellh))
  ```text
  Introduce a dedicated device_attributes.zig module that consolidates
  all device attribute types and encoding logic. This moves
  DeviceAttributeReq out of ansi.zig and adds structured response
  types for DA1 (primary), DA2 (secondary), and DA3 (tertiary) with
  self-encoding methods.
  
  Primary DA uses a ConformanceLevel enum covering VT100-series
  per-model values and VT200+ conformance levels, plus a Feature
  enum with all known xterm DA1 attribute codes (132-col, printer,
  sixel, color, clipboard, etc.) as a simple slice. Secondary DA
  uses a DeviceType enum matching the xterm decTerminalID values.
  Tertiary DA encodes the DECRPTUI unit ID as a u32 formatted to
  8 hex digits.
  
  This is preparatory work for exposing device attributes through
  the stream_terminal Effects callback system.
  ```
- [`ba3f9bb`](https://github.com/ghostty-org/ghostty/commit/ba3f9bb400d2dd95ae99017f3f3ed8756a3eaf91) terminal: port device_attributes to stream_terminal Effects ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a device_attributes effect callback to the stream_terminal
  Handler. The callback returns a device_attributes.Attributes
  struct which the handler encodes and writes back to the pty.
  
  Add Attributes.encode which dispatches to the correct sub-type
  encoder based on the request type (primary, secondary, tertiary).
  
  In readonly mode the callback is null so all DA queries are
  silently ignored, matching the previous behavior where
  device_attributes was in the ignored actions list.
  
  Tests cover all three DA types with default attributes, custom
  attributes, and readonly mode.
  ```
- [`701d1d5`](https://github.com/ghostty-org/ghostty/commit/701d1d55d23ae199785b56db05c92d74f157a2f3) terminal: fix secondary DA test to match default firmware version ([@mitchellh](https://github.com/mitchellh))
  ```text
  The default firmware_version for Secondary device attributes is 0,
  but the test expected a value of 10. Update the test expectation to
  match the actual default.
  ```
- [`69104fb`](https://github.com/ghostty-org/ghostty/commit/69104fb1f02a3daa8b41bf6d3ca32f71b86f5ac0) libghostty: introduce optional "effects" to handle queries and side effects for terminals ([#11787](https://github.com/ghostty-org/ghostty/issues/11787)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Renames `ReadonlyStream` to `TerminalStream` and introduces an
  effects-based callback system so that the stream handler can optionally
  respond to queries and side effects (bell, title changes, device
  attributes, device status, size reports, XTVERSION, ENQ, DECRQM, kitty
  keyboard queries).
  
  The default behavior is still read-only, callers have to opt-in to
  setting callbacks to function pointers.
  
  This doesn't handle every possible side effect yet, e.g. this doesn't
  include clipboards, pwd reporting, and others. But this covers the
  important ones.
  
  This PR is Zig only, the C version of this will come later.
  ```
- [`5ef2da8`](https://github.com/ghostty-org/ghostty/commit/5ef2da8127501083abdeb623df45674b7439ea45) windows: fix XDG-related test failures on Windows ([@deblasis](https://github.com/deblasis))
  ```text
  Make the "cache directory paths" test cross-platform by using
  std.fs.path.join for expected values and a platform-appropriate
  mock home path, since the function under test uses native path
  separators.
  
  Skip the two shell integration XDG_DATA_DIRS tests on Windows.
  These tests use hardcoded Unix path separators (:) and Unix default
  paths (/usr/local/share:/usr/share) which are not applicable on
  Windows where the path delimiter is ; and XDG_DATA_DIRS is not a
  standard concept.
  ```
- [`2fe89c3`](https://github.com/ghostty-org/ghostty/commit/2fe89c340a4680a36ded8a517266770f2dc42a4b) windows: fix XDG-related test failures on Windows ([#11783](https://github.com/ghostty-org/ghostty/issues/11783)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## What
  
  Two fixes for tests that fail on Windows due to Unix-specific
  assumptions.
  
  1. The "cache directory paths" test in xdg.zig hardcodes Unix paths like
  `/Users/test/.cache` in expected values. The function under test uses
  `std.fs.path.join` which produces native separators, so the expectations
  need to match. Fixed by using `std.fs.path.join` for expected values
  too, with a platform-appropriate mock home path.
  
  2. Two shell integration tests for `setupXdgDataDirs` hardcode Unix path
  separators (`:`) and Unix default paths (`/usr/local/share:/usr/share`).
  These are not applicable on Windows where the delimiter is `;` and
  `XDG_DATA_DIRS` is not a standard concept. Skipped on Windows with
  `SkipZigTest`.
  
  
  ## Why skip instead of fix for the shell integration tests?
  
  `setupXdgDataDirs` is used by fish, elvish, and nushell. On Windows,
  `XDG_DATA_DIRS` is not standard. The equivalent would be `%ProgramData%`
  (what Go's `adrg/xdg`, Python's `platformdirs`, and others map to).
  Fixing this properly means adding a Windows-appropriate default, which
  is a separate change. (How do you guys deal with these situations? Do
  you create issues on the spot as reminders or do you wait for the
  requirement to emerge by itself when the time comes?
  
  Worth noting: the production code on line 664 of `shell_integration.zig`
  hardcodes the fallback to `"/usr/local/share:/usr/share"` with `:`
  separators, while `prependEnv` correctly uses `std.fs.path.delimiter`
  (`;` on Windows). If a shell that uses this runs on Windows, you would
  get mixed separators. Tracked separately.
  
  ## Verified
  
  - `zig build test-lib-vt` passes on Windows (exit 0)
  - No behavior change on Linux/macOS (xdg.zig fix produces same paths,
  shell_integration skip only triggers on Windows)
  
  ## What I Learnt
  
  - `std.fs.path.join` uses the native path separator, so tests that
  hardcode `/` in expected paths will fail on Windows even if the
  production code is correct. Better to use `path.join` in test
  expectations too.
  - The XDG Base Directory spec is Unix-only but cross-platform libraries
  have converged on mappings. Ghostty maps to `%LOCALAPPDATA%` which
  matches common conventions. The missing piece is `XDG_DATA_DIRS` which
  has no Windows default and falls through to Unix paths.
  ```
- [`f2773d4`](https://github.com/ghostty-org/ghostty/commit/f2773d42c1c4cc8750bfe6298397f2aa4a93340d) windows: skip expandHomeUnix test on Windows ([@deblasis](https://github.com/deblasis))
  ```text
  expandHomeUnix is a Unix-internal function that is never called on
  Windows. The public expandHome function returns the path unchanged
  on Windows since ~/ is not a standard Windows idiom. The test calls
  expandHomeUnix directly, which invokes home() and expects Unix-style
  forward-slash separators.
  ```
- [`fd49716`](https://github.com/ghostty-org/ghostty/commit/fd49716ea2084108aa098db390931c007495a1ab) windows: skip expandHomeUnix test on Windows ([#11784](https://github.com/ghostty-org/ghostty/issues/11784)) ([@jcollie](https://github.com/jcollie))
  ````text
  ## What
  
  Skip the `expandHomeUnix` test on Windows with `SkipZigTest`.
  
  `expandHomeUnix` is a Unix-internal function that is never called on
  Windows. The public `expandHome` already returns the path unchanged on
  Windows (added upstream in cccdb0d2a). But the unit test calls
  `expandHomeUnix` directly, which invokes `home()` and expects Unix-style
  forward-slash separators, so it fails on Windows.
  
  ## How
  
  Two lines:
  
  ```zig
  if (builtin.os.tag == .windows) return error.SkipZigTest;
  
  ```
  
  ## Verified
  
  - `zig build test-lib-vt` passes on Windows (exit 0)
  - No behavior change on Linux/macOS
  
  ## What I Learnt
  
  - When upstream adds a platform dispatch for production code (like
  `expandHome` returning unchanged on Windows), the unit tests for
  internal platform-specific functions (like `expandHomeUnix`) may still
  need a skip guard.
  - Zig doesn't have something like Go's `//go:build` but damn... comptime
  is insane, like supercharged C# `#if`
  ````
- [`5a46e61`](https://github.com/ghostty-org/ghostty/commit/5a46e61bee58e9170f00b3c1404f6ca78aabcf82) cmake: fix Windows build support ([@mitchellh](https://github.com/mitchellh))
  ```text
  On Windows, shared libraries (DLLs) require an import library (.lib)
  for linking, and the DLL itself is placed in bin/ rather than lib/ by
  the Zig build. The CMake wrapper was missing IMPORTED_IMPLIB on the
  shared imported target, causing link failures, and assumed the shared
  library was always in lib/.
  
  Add GHOSTTY_VT_IMPLIB for the import library name, set IMPORTED_IMPLIB
  on the ghostty-vt target, and fix the shared library path to use bin/
  on Windows. Install the DLL and PDB to bin/ and the import library to
  lib/ following standard Windows conventions. Apply the same fixes to
  ghostty-vt-config.cmake.in for the find_package path.
  ```
- [`f4998c6`](https://github.com/ghostty-org/ghostty/commit/f4998c6abbce862448d68fb2b4c3b17ba16d7b16) build: fix Windows build failures in helpgen and framegen ([@mitchellh](https://github.com/mitchellh))
  ```text
  Use writerStreaming() instead of writer() for stdout in helpgen and
  main_build_data. The positional writer calls setEndPos/ftruncate in
  end(), which fails on Windows when stdout is redirected via
  captureStdOut() because ftruncate maps INVALID_PARAMETER to
  FileTooBig. Streaming mode skips truncation entirely since stdout
  is inherently a sequential stream.
  
  Replace scandir with opendir/readdir plus qsort in framegen since
  scandir is a POSIX extension not available on Windows.
  ```
- [`48cf3f3`](https://github.com/ghostty-org/ghostty/commit/48cf3f36cde2c28ba2f321636bf8612873bd274a) ci: run Windows CMake examples after building ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a "Run Example" step to the build-examples-cmake-windows job
  so that each CMake example is executed after it is built, verifying
  the resulting binaries actually work. The executable name is derived
  from the matrix directory name by replacing hyphens with underscores,
  matching the project convention.
  ```
- [`0fdddd5`](https://github.com/ghostty-org/ghostty/commit/0fdddd5bc2efe1cd8952ac4e248c84ff91c95cdf) Revert "build: fix Windows build failures in helpgen and framegen" ([@mitchellh](https://github.com/mitchellh))
  ```text
  This reverts commit 704511465b8b04d6839fbaaf3323d9349693f04a.
  ```
- [`6ccc01a`](https://github.com/ghostty-org/ghostty/commit/6ccc01a85258634eb09d48fd906e6311b395a956) revert the build-windows ([@mitchellh](https://github.com/mitchellh))
- [`2afadfc`](https://github.com/ghostty-org/ghostty/commit/2afadfc104ee4b0385afe19e9560da8afb58e7f1) build: fix Windows cmake example failures ([@mitchellh](https://github.com/mitchellh))
  ```text
  The cmake examples were failing at runtime on Windows CI for two
  reasons.
  
  The static library was installed as "libghostty-vt.a" on all
  platforms, but on Windows the DLL import library is also placed in
  zig-out/lib/ as "ghostty-vt.lib". The CMakeLists.txt expected the
  platform-native name "ghostty-vt.lib" for the static lib, so it
  picked up the tiny DLL import lib instead, silently producing a
  dynamically-linked executable. That executable then failed at
  runtime because the DLL was not on PATH.
  
  Fix this by installing the static library as "ghostty-vt-static.lib"
  on Windows to avoid the name collision, and updating CMakeLists.txt
  to match. For the shared (DLL) example, add zig-out/bin to PATH in
  the CI run step so the DLL can be found at runtime.
  ```
- [`31285e1`](https://github.com/ghostty-org/ghostty/commit/31285e1ac34d8a2dcd46ec682fba767d05ebd21e) build: disable bundled compiler_rt and ubsan_rt for MSVC targets ([@mitchellh](https://github.com/mitchellh))
  ```text
  Zig's bundled compiler_rt and ubsan_rt produce object files with
  ELF-style linker directives (/exclude-symbols) and COMDAT sections
  that are incompatible with the MSVC linker, causing LNK1143 and
  LNK4229 errors when linking the static library.
  
  MSVC provides its own compiler runtime so bundling Zig's versions
  is unnecessary. Skip bundling both runtimes when the target ABI is
  MSVC.
  ```
- [`1ce057f`](https://github.com/ghostty-org/ghostty/commit/1ce057f0535f3a0a57cb5c9ed34d3b7fecfb967c) build: disable ubsan and bundled runtimes for MSVC targets ([@mitchellh](https://github.com/mitchellh))
  ```text
  Zig's ubsan instrumentation emits ELF-style /exclude-symbols linker
  directives into the compiled object files, causing LNK4229 warnings
  with the MSVC linker. The bundled compiler_rt also produces COMDAT
  sections that are incompatible with MSVC, causing fatal LNK1143.
  
  Disable sanitize_c entirely on the root module for MSVC targets and
  skip bundling both compiler_rt and ubsan_rt since MSVC provides its
  own runtime.
  ```
- [`69f82ec`](https://github.com/ghostty-org/ghostty/commit/69f82ec7511950eef3d5f52c738d5da6bcac9b0c) build: disable bundled ubsan runtime on Windows ([@mitchellh](https://github.com/mitchellh))
  ```text
  Zig's ubsan runtime emits /exclude-symbols linker directives that
  are incompatible with the MSVC linker, causing LNK4229 warnings and
  LNK1143 errors. Disable bundling ubsan_rt on Windows while keeping
  compiler_rt which provides essential symbols like memcpy, memset,
  memmove, and ___chkstk_ms.
  
  The previous check used target.result.abi == .msvc which never
  matched because Zig defaults to the gnu ABI on Windows.
  ```
- [`2c89bef`](https://github.com/ghostty-org/ghostty/commit/2c89bef860efbd5518375edcce6f1f210a923c59) build: skip bundled compiler_rt and ubsan_rt in Windows static lib ([@mitchellh](https://github.com/mitchellh))
  ```text
  Zig's compiler_rt produces COFF objects with invalid COMDAT
  sections that the MSVC linker rejects (LNK1143), and its ubsan_rt
  emits /exclude-symbols directives that MSVC does not understand
  (LNK4229). Skip bundling both in the static library on Windows
  since the MSVC CRT provides the needed builtins (memcpy, memset,
  etc.). The shared library continues to bundle compiler_rt as it
  needs to be self-contained.
  ```
- [`01401ef`](https://github.com/ghostty-org/ghostty/commit/01401ef6756c0876b775e0bcdd06064abc68697e) build: fix Windows static lib linking with MSVC ([@mitchellh](https://github.com/mitchellh))
  ```text
  Three issues when linking the static library with the MSVC linker:
  
  Use the LLVM backend on Windows to produce valid COFF objects.
  The self-hosted backend generates compiler_rt objects with invalid
  COMDAT sections that the MSVC linker rejects (LNK1143).
  
  Disable bundling ubsan_rt on Windows. Zig's ubsan runtime emits
  /exclude-symbols linker directives that MSVC does not understand
  (LNK4229).
  
  Add ntdll and kernel32 as transitive link dependencies for the
  static library on Windows. The Zig standard library uses NT API
  functions (NtClose, NtCreateSection, etc.) that consumers must
  link.
  ```
- [`1eed35d`](https://github.com/ghostty-org/ghostty/commit/1eed35dddccbcb3a47ffddf999df43ecd1f217ea) build: default to MSVC ABI on Windows ([@mitchellh](https://github.com/mitchellh))
  ```text
  Zig defaults to the GNU ABI on Windows, which produces COFF objects
  with invalid COMDAT sections in compiler_rt that the MSVC linker
  rejects (LNK1143), and uses GNU conventions like ___chkstk_ms that
  are unavailable in the MSVC CRT.
  
  Default to the MSVC ABI when no explicit ABI is requested, following
  the same pattern as the existing macOS target override. This ensures
  compiler_rt produces valid COFF and the generated code uses
  MSVC-compatible symbols. Users can still explicitly request the GNU
  ABI via -Dtarget.
  
  Also disable bundling ubsan_rt on Windows (its /exclude-symbols
  directives are MSVC-incompatible) and add ntdll and kernel32 as
  transitive link dependencies for the static library.
  ```
- [`afa8f05`](https://github.com/ghostty-org/ghostty/commit/afa8f059e5faeb6198ca64edb89762fb821df9e5) build: skip linkLibCpp on MSVC targets ([@mitchellh](https://github.com/mitchellh))
  ```text
  Zig's bundled libc++/libc++abi conflicts with the MSVC C++ runtime
  headers (vcruntime_typeinfo.h, vcruntime_exception.h, etc.) when
  targeting native-native-msvc. This caused compilation failures in
  the SIMD C++ code due to -nostdinc++ suppressing MSVC headers and
  libc++ types clashing with MSVC runtime types.
  
  Skip linkLibCpp() for MSVC targets across all packages (highway,
  simdutf, utfcpp) and the main build (SharedDeps, GhosttyZig) since
  MSVC provides its own C++ standard library natively. Also add
  missing <iterator> and <cstddef> includes that were previously
  pulled in transitively through libc++ headers but are not
  guaranteed by MSVC's headers.
  ```
- [`3d581eb`](https://github.com/ghostty-org/ghostty/commit/3d581eb92eade74bce9becdda50c0bf2877df366) build: use linkLibC instead of linkLibCpp on MSVC targets ([@mitchellh](https://github.com/mitchellh))
  ```text
  When compiling C++ files, Zig unconditionally passes -nostdinc++ and,
  if link_libcpp is set, adds its bundled libc++/libc++abi include paths
  as replacements (see Compilation.zig). On MSVC targets this conflicts
  with the MSVC C++ runtime headers (vcruntime_typeinfo.h,
  vcruntime_exception.h, etc.), causing compilation failures in SIMD
  C++ code.
  
  The fix is to use linkLibC instead of linkLibCpp on MSVC. Zig always
  passes -nostdinc to strip default search paths, but LibCDirs.detect
  re-adds the MSVC SDK include directories, which contain both C and
  C++ standard library headers. This gives us proper access to MSVC's
  own <optional>, <iterator>, <cstddef>, etc. without the libc++
  conflicts.
  
  For the package builds (highway, simdutf, utfcpp) this means
  switching from linkLibCpp to linkLibC on MSVC. For SharedDeps and
  GhosttyZig, linkLibC is already called separately, so we just skip
  linkLibCpp.
  ```
- [`b4c529a`](https://github.com/ghostty-org/ghostty/commit/b4c529a82722cb6f9425de531888ff3424be4732) build: add -std=c++17 for SIMD C++ files on MSVC ([@mitchellh](https://github.com/mitchellh))
  ```text
  The SIMD C++ files use C++17 features (std::optional, std::size).
  With Zig's bundled libc++ these are available implicitly, but MSVC
  headers guard C++17 features behind the standard version
  (_HAS_CXX17). Without an explicit -std=c++17 flag, clang defaults
  to a lower standard and the MSVC <optional> header does not define
  std::optional.
  ```
- [`63260ec`](https://github.com/ghostty-org/ghostty/commit/63260ec7221741fb0c0a0e2f1018da094b116af9) build: disable ubsan for SIMD C++ files on MSVC ([@mitchellh](https://github.com/mitchellh))
  ```text
  The SIMD C++ files reference __ubsan_handle_* symbols when compiled
  in debug mode, but we do not link or bundle the ubsan runtime on
  MSVC. This matches what the highway and simdutf packages already do
  in their own build files.
  ```
- [`b723f2a`](https://github.com/ghostty-org/ghostty/commit/b723f2a4377a196eaa594e42bc0a7ba0ad1ba09c) ci: remove run step from Windows cmake examples ([@mitchellh](https://github.com/mitchellh))
  ```text
  The "Run Example" step in the build-examples-cmake-windows job
  hangs, so remove it entirely. The build step is still run so
  compilation is verified, but the examples are no longer executed
  on Windows.
  ```
- [`1213dac`](https://github.com/ghostty-org/ghostty/commit/1213dacd5be631a896b9618a0bfebd8efa2e5c79) cmake: fix Windows libghostty build support ([#11756](https://github.com/ghostty-org/ghostty/issues/11756)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  On Windows, shared libraries (DLLs) require an import library (.lib) for
  linking, and the DLL itself is placed in bin/ rather than lib/ by the
  Zig build. The CMake wrapper was missing IMPORTED_IMPLIB on the shared
  imported target, causing link failures, and assumed the shared library
  was always in lib/.
  
  Add GHOSTTY_VT_IMPLIB for the import library name, set IMPORTED_IMPLIB
  on the ghostty-vt target, and fix the shared library path to use bin/ on
  Windows. Install the DLL and PDB to bin/ and the import library to lib/
  following standard Windows conventions. Apply the same fixes to
  ghostty-vt-config.cmake.in for the find_package path.
  ```
- [`aa969df`](https://github.com/ghostty-org/ghostty/commit/aa969df6794ed5018342920b20c65c5f74c6fb7a) ci: clean up Windows build job ([@mitchellh](https://github.com/mitchellh))
  ```text
  Rename build-windows to build-libghostty-vt-windows to reflect that
  it only builds and tests libghostty-vt for now, and move it next to
  the other build-libghostty-vt jobs.
  
  Replace the manual PowerShell zig download/install with mlugg/setup-zig,
  which auto-detects the version from build.zig.zon and handles caching.
  Upgrade the runner from windows-2022 to windows-2025. Remove the
  generated-script-to-swallow-errors pattern in favor of direct zig
  build commands.
  ```
- [`d568ce9`](https://github.com/ghostty-org/ghostty/commit/d568ce9cc838d97a5e323054e72f19e47c6cc0a9) terminal: support VirtualAlloc for page allocation on windows ([@mitchellh](https://github.com/mitchellh))
  ```text
  Extract the platform-specific page backing memory allocation into
  AllocPosix and AllocWindows structs behind a PageAlloc comptime
  switch. Previously, POSIX mmap calls were inlined at each call
  site. This adds a Windows VirtualAlloc implementation and routes
  all allocation through PageAlloc.alloc/free, making the backing
  memory strategy consistent and easier to extend.
  ```
- [`e95fdd2`](https://github.com/ghostty-org/ghostty/commit/e95fdd2f21bda187c3a521417243d7280110f6a1) terminal: handle CRLF line endings in rgb.txt parsing ([@mitchellh](https://github.com/mitchellh))
  ```text
  The X11 color map parser in x11_color.zig uses @embedFile to load
  rgb.txt at comptime, then splits on \n. On Windows, git may check
  out rgb.txt with CRLF line endings, leaving a trailing \r on each
  line. This caused color names to be stored as e.g. "white\r" instead
  of "white", so all X11 color lookups failed at runtime.
  
  Strip trailing \r from each line before parsing. Also mark rgb.txt
  as -text in .gitattributes to prevent line ending conversion in
  future checkouts.
  ```
- [`fa10237`](https://github.com/ghostty-org/ghostty/commit/fa10237fb0cb952dcc5760339890e50f25818111) build: fix windows build to properly run tests and build of libghostty-vt ([#11781](https://github.com/ghostty-org/ghostty/issues/11781)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Our Windows build has been broken for a _long_ time. It hasn't actually
  worked and our CI was falsely passing when it was actually failing to
  build/test. This PR fixes that and fixes the issues it found so
  `libghostty-vt` can build and pass tests.
  
  **This is only for libghostty!** I'd still like to expand our _test_
  coverage to all of Ghostty for Windows but libghostty is more important
  for that platform in the short term and it's an incremental piece of
  work.
  
  A couple windows compatibility issues fixed:
  
  - `terminal.Page` uses `VirtualAlloc` on Windows (thanks @deblasis)
  - Our rgb.txt loading was not resilient to CRLF endings
  ```
- [`04b5dc7`](https://github.com/ghostty-org/ghostty/commit/04b5dc733243d85f0bbaa3aea25d65a19649cd64) terminal: guard ghostty.h checks on building the app ([@mitchellh](https://github.com/mitchellh))
- [`7253668`](https://github.com/ghostty-org/ghostty/commit/7253668ec20b0a79e41930ec4ba9e189d605cc7e) config: move file formatter to dedicated file to prevent import bloat ([@mitchellh](https://github.com/mitchellh))
- [`f60587f`](https://github.com/ghostty-org/ghostty/commit/f60587ffcc15886ee0dd2f24764da4e69f83a9d2) renderer/size: move PaddingBalance enum out of Config ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously WindowPaddingBalance was defined inside Config.zig, which
  meant tests for renderer sizing had to pull in the full config
  dependency. Move the enum into renderer/size.zig as PaddingBalance
  and re-export it from Config so the public API is unchanged. This
  lets size.zig tests run without depending on Config.
  ```
- [`51f8784`](https://github.com/ghostty-org/ghostty/commit/51f878417fede56716a3931b8a55fa4b0cbe15aa) reenable tests ([@mitchellh](https://github.com/mitchellh))
- [`409f05c`](https://github.com/ghostty-org/ghostty/commit/409f05c92750e94c376b0c42ae7c70b2d9fbd62c) typos ([@mitchellh](https://github.com/mitchellh))
- [`5828352`](https://github.com/ghostty-org/ghostty/commit/58283528c79de8f9d17bc5f4e280e43835696c67) vt: handle invalid enum before pointer cast in getters ([@mitchellh](https://github.com/mitchellh))
  ```text
  The inline else switch in each C API getter expands the .invalid
  case, which has OutType void. When called with .invalid and a null
  out pointer, the @ptrCast(@alignCast(out)) panics before getTyped
  can return early.
  
  Handle .invalid explicitly in the outer switch of every getter to
  short-circuit before the pointer cast. This affects build_info,
  cell, row, terminal, osc, and render (three getters).
  ```
- [`f92bb74`](https://github.com/ghostty-org/ghostty/commit/f92bb7419692bfce765aa6571ec1d72ac5095a2c) ci: add test-lib-vt job ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a new CI job that runs `zig build test-lib-vt` to test the
  lib-vt build step. The job mirrors the existing test job structure
  with the same nix/cachix setup and skip conditions. It is also
  added to the required checks list.
  ```
- [`3c8d0a9`](https://github.com/ghostty-org/ghostty/commit/3c8d0a9c25493091b82bed88f2c6c7c171a51c11) vt: fix test failures in render and key_encode ([@mitchellh](https://github.com/mitchellh))
  ```text
  The colors_get function used structSizedFieldFits to guard the
  palette copy, which required the entire palette array to fit in the
  provided size. This prevented partial palette writes when the caller
  passed a truncated sized struct, since the guard failed even though
  the inner code already handled partial copies correctly. Remove the
  outer guard so the existing partial-copy logic applies.
  
  The setopt_from_terminal test expected alt_esc_prefix to be false on
  a fresh terminal, but the mode definition in modes.zig sets its
  default to true. Update the test expectation to match.
  ```
- [`206f989`](https://github.com/ghostty-org/ghostty/commit/206f9894f7978f894a29d1a6d686284b489504ae) Fix `zig build test-lib-vt`  ([#11778](https://github.com/ghostty-org/ghostty/issues/11778)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  - Our `checkGhosttyH` calls need to be guarded on building Ghostty app
  which has it
  - Move FileFormatter to its own file to avoid poisoning test refs with
  Config.zig which pulls in the world
  - Move WindowPaddingBalance to renderer to avoid pulling in Config.zig
  - Add a `zig build test-lib-vt` CI job
  ```
- [`d67f65e`](https://github.com/ghostty-org/ghostty/commit/d67f65e38c8362c066dbfc70f2425808833e7049) also build static libghostty-vt for wasm ([@turbolent](https://github.com/turbolent))
- [`9b3f7a9`](https://github.com/ghostty-org/ghostty/commit/9b3f7a9287bcb0524d8ddfc78dc7ae35c641d187) vt: also build static libghostty-vt for wasm ([#11757](https://github.com/ghostty-org/ghostty/issues/11757)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A static libghostty-vt is also useful for wasm targets, as that allows
  linking with an application into a larger wasm module.
  
  See
  https://github.com/ghostty-org/ghostty/pull/11729#issuecomment-4106589379
  ```
- [`855a6b0`](https://github.com/ghostty-org/ghostty/commit/855a6b01fcb52a85434d13d4c554f8b551248541) gtk: Open urls with openuri portal ([@tdgroot](https://github.com/tdgroot))
- [`37d297c`](https://github.com/ghostty-org/ghostty/commit/37d297c03c5494de34d37d77439f73cb0d953137) gtk/portal: General improvements ([@tdgroot](https://github.com/tdgroot))
  ```text
  - Token is formatted without allocation
  - Reusable function for formatToken
  - Tests in portal.zig are actuall included now
  ```
- [`919e586`](https://github.com/ghostty-org/ghostty/commit/919e586c516442b899f1f925f4aa37a100dee833) gtk/portal: Improve OpenURI lifecycle ([@tdgroot](https://github.com/tdgroot))
- [`8bc7590`](https://github.com/ghostty-org/ghostty/commit/8bc75907b541673deba24d3075fa0818c8f7b633) gtk: Fix casing for openUri ([@tdgroot](https://github.com/tdgroot))
- [`374ed27`](https://github.com/ghostty-org/ghostty/commit/374ed2721462ba2a9aaa8c6872a8c56eb4568b90) gtk: Open URIs with portals ([#11754](https://github.com/ghostty-org/ghostty/issues/11754)) ([@jcollie](https://github.com/jcollie))
  ```text
  This is a continuation of the solid work done by @jcollie in PR #7864. I
  checked with him if I could take over to continue the implementation.
  
  His changes of last year have been adapted to be compatible with the
  current GTK implementation. Aside from just "making it work", I also
  dived into the portals and OpenURI implementation and made some
  improvements there.
  
  Notable improvements were:
  - Improved lifecycle management of glib resources in the OpenURI
  implementation
  - More forgiving error handling in OpenURI implementation by adding more
  fallbacks
  - Fixed some memory leaks
  - Less memory allocations in Portals implementation
  - Added tests for building the Portals request path
  
  Fixes #5991
  ```
- [`f0d59c2`](https://github.com/ghostty-org/ghostty/commit/f0d59c22b201d79ccc8fe2a326b5a2f2dbcb37b3) Update VOUCHED list ([#11775](https://github.com/ghostty-org/ghostty/issues/11775)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11768#issuecomment-4111147332)
  from @jcollie.
  
  Vouch: @lynicis
  ```
- [`f6cf978`](https://github.com/ghostty-org/ghostty/commit/f6cf978b32c4c1f947aeb779694e8e48a008ae32) Update VOUCHED list ([#11773](https://github.com/ghostty-org/ghostty/issues/11773)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11771#issuecomment-4111016256)
  from @jcollie.
  
  Vouch: @deblasis
  ```

## March 22, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23411835341), [2](https://github.com/ghostty-org/ghostty/actions/runs/23405966563), [3](https://github.com/ghostty-org/ghostty/actions/runs/23404576910), [4](https://github.com/ghostty-org/ghostty/actions/runs/23399074980), [5](https://github.com/ghostty-org/ghostty/actions/runs/23394861871)  
Summary: 5 runs • 10 commits • 2 authors

### Changes

- [`1d54a94`](https://github.com/ghostty-org/ghostty/commit/1d54a94cedd4405584d2dcdde948262a33110018) Update VOUCHED list ([#11755](https://github.com/ghostty-org/ghostty/issues/11755)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11754#issuecomment-4106929553)
  from @mitchellh.
  
  Vouch: @tdgroot
  ```
- [`1f2a3b8`](https://github.com/ghostty-org/ghostty/commit/1f2a3b8a830aad15a72fec41e386fa4db4ab6804) update README ([@mitchellh](https://github.com/mitchellh))
  ```text
  The README hasn't been updated in years basically!
  
  This updates the README to make libghostty a first class citizen of the
  project and to update our roadmap and goals for the project to more
  accurately reflect our current state and future plans.
  ```
- [`7d816f8`](https://github.com/ghostty-org/ghostty/commit/7d816f8e81e6cd05fd846b0ec7e02ea706efde41) Update README ([#11748](https://github.com/ghostty-org/ghostty/issues/11748)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The README hasn't been updated in years basically!
  
  This updates the README to make libghostty a first class citizen of the
  project and to update our roadmap and goals for the project to more
  accurately reflect our current state and future plans.
  
  I notably updated our roadmap to be more accurate to our state, e.g.
  we're stable now. I removed Windows because it's not a short term focus
  and I think libghostty is more important and enables that ecosystem a
  lot more (libghostty itself being already compatible with Windows). I
  also expanded on "fancy features" and clarified its to make
  Ghostty-specific sequences.
  ```
- [`8bd3a49`](https://github.com/ghostty-org/ghostty/commit/8bd3a493be648aa7df12e45c531a7f30cffa6eb1) libghostty: add resolved bg_color and fg_color to cells API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11705
  
  Add bg_color and fg_color options to GhosttyRenderStateRowCellsData
  that resolve the final RGB color for a cell, flattening the multiple
  possible sources. For background, this handles content-tag bg_color_rgb,
  content-tag bg_color_palette (looked up in the palette), and the
  style bg_color. For foreground, this resolves palette indices through
  the palette; bold color handling is not applied and is left to the
  caller.
  
  Both return GHOSTTY_INVALID_VALUE when no explicit color is set, in
  which case the caller should fall back to whatever default color it
  wants (e.g. the terminal background/foreground).
  ```
- [`ecc55b9`](https://github.com/ghostty-org/ghostty/commit/ecc55b94c803789762682065ab68f227447909c5) libghostty: add resolved bg_color and fg_color to cells API ([#11735](https://github.com/ghostty-org/ghostty/issues/11735)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11705
  
  Add bg_color and fg_color options to GhosttyRenderStateRowCellsData that
  resolve the final RGB color for a cell, flattening the multiple possible
  sources. For background, this handles content-tag bg_color_rgb,
  content-tag bg_color_palette (looked up in the palette), and the style
  bg_color. For foreground, this resolves palette indices through the
  palette; bold color handling is not applied and is left to the caller.
  
  Both return GHOSTTY_INVALID_VALUE when no explicit color is set, in
  which case the caller should fall back to whatever default color it
  wants (e.g. the terminal background/foreground).
  ```
- [`8a788a3`](https://github.com/ghostty-org/ghostty/commit/8a788a350e105398b1c32df74a4a962e3d723032) Update VOUCHED list ([#11741](https://github.com/ghostty-org/ghostty/issues/11741)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11737#discussioncomment-16252675)
  from @pluiedev.
  
  Denounce: @kody-w
  ```
- [`47bfde3`](https://github.com/ghostty-org/ghostty/commit/47bfde328658ede90f2d1a98e0d7bc8fb99fda12) libghostty: expose mouse_tracking terminal data option ([@mitchellh](https://github.com/mitchellh))
  ```text
  #11706
  
  Add a new GHOSTTY_TERMINAL_DATA_MOUSE_TRACKING option to the
  ghostty_terminal_get API. This returns true if any mouse tracking
  mode is active (X10, normal, button, or any-event), replacing the
  need for consumers to loop over four separate mode queries.
  ```
- [`0c2bafc`](https://github.com/ghostty-org/ghostty/commit/0c2bafcc2a63a49f0f747adf8ca454bd85336167) libghostty: expose mouse_tracking terminal data option ([#11734](https://github.com/ghostty-org/ghostty/issues/11734)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11706
  
  Add a new GHOSTTY_TERMINAL_DATA_MOUSE_TRACKING option to the
  ghostty_terminal_get API. This returns true if any mouse tracking mode
  is active (X10, normal, button, or any-event), replacing the need for
  consumers to loop over four separate mode queries.
  ```
- [`32c97a0`](https://github.com/ghostty-org/ghostty/commit/32c97a019f3f30d379436ec1a636c3d1d0472fbd) terminal: default render state foreground to white ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11704
  
  The RenderState empty initializer set both background and foreground
  to the default RGB value of black (0, 0, 0), making text unreadable
  when a caller has not explicitly configured terminal colors via
  DynamicRGB. This is the common case for libghostty consumers.
  
  Default the foreground to white so that the initial render state
  provides readable white-on-black text out of the box.
  
  Long term we also need to expose setting the default colors for a
  Terminal instance but this is a workable fix in the mean time.
  ```
- [`ad5e967`](https://github.com/ghostty-org/ghostty/commit/ad5e9679c882fac5ca68e734834d88da18f585d8) terminal: default render state foreground to white ([#11736](https://github.com/ghostty-org/ghostty/issues/11736)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11704
  
  The RenderState empty initializer set both background and foreground to
  the default RGB value of black (0, 0, 0), making text unreadable when a
  caller has not explicitly configured terminal colors via DynamicRGB.
  This is the common case for libghostty consumers.
  
  Default the foreground to white so that the initial render state
  provides readable white-on-black text out of the box.
  
  Long term we also need to expose setting the default colors for a
  Terminal instance but this is a workable fix in the mean time.
  ```

## March 21, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23390298154), [2](https://github.com/ghostty-org/ghostty/actions/runs/23388647037), [3](https://github.com/ghostty-org/ghostty/actions/runs/23386078903), [4](https://github.com/ghostty-org/ghostty/actions/runs/23385209490), [5](https://github.com/ghostty-org/ghostty/actions/runs/23381920473), [6](https://github.com/ghostty-org/ghostty/actions/runs/23381687422), [7](https://github.com/ghostty-org/ghostty/actions/runs/23372156958)  
Summary: 7 runs • 18 commits • 3 authors

### Changes

- [`8d6be5a`](https://github.com/ghostty-org/ghostty/commit/8d6be5a3dd7e7a88670deb953b03532b22106758) build: add static library target for libghostty-vt ([@mitchellh](https://github.com/mitchellh))
  ```text
  Refactor GhosttyLibVt to support both shared and static library
  builds via a shared initLib helper that accepts a LinkMode. The
  shared and static entry points (initShared, initStatic) delegate
  to this common path.
  
  For static builds, compiler_rt and ubsan_rt are bundled to avoid
  undefined symbol errors. Debug symbols (dsymutil) are skipped for
  static libs since they are not linked. The install artifact uses
  a "-static" suffix internally but installs as "libghostty-vt.a"
  via a new installLib method. Wasm is excluded from static builds
  since it has no meaningful static vs shared distinction.
  ```
- [`555bf7e`](https://github.com/ghostty-org/ghostty/commit/555bf7e92292b40b3d5b6b450bf8b92c99fd174c) build: add cmake static library support ([@mitchellh](https://github.com/mitchellh))
  ```text
  Expose both shared and static libraries as separate CMake imported
  targets (ghostty-vt and ghostty-vt-static) rather than toggling
  between them with BUILD_SHARED_LIBS. The zig build already produces
  both in a single invocation, so both are always available.
  
  The find_package config template is updated to export both targets
  as ghostty-vt::ghostty-vt and ghostty-vt::ghostty-vt-static.
  
  Add a c-vt-cmake-static example that demonstrates linking the static
  library via FetchContent with -Dsimd=false to avoid C++ runtime
  dependencies.
  ```
- [`5fd36ea`](https://github.com/ghostty-org/ghostty/commit/5fd36ea69e1d69f0ae15424d736a30df7b07fc81) build: enable PIC for static libghostty-vt ([@mitchellh](https://github.com/mitchellh))
  ```text
  The static library was built without position-independent code,
  which caused linker errors when consumers tried to link it into
  PIE executables (the default on most Linux distributions). The
  linker would fail with "relocation R_X86_64_32 against symbol
  cannot be used when making a PIE object."
  
  Enable PIC on the static library root module so it can be linked
  into both PIE and non-PIE executables.
  ```
- [`1775c31`](https://github.com/ghostty-org/ghostty/commit/1775c312ae6e99f8c499997faa6c084c3a758931) libghostty: add static library support ([#11732](https://github.com/ghostty-org/ghostty/issues/11732)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Multiple changes:
  
  * `zig build -Demit-lib-vt` now produces both shared and static
  libraries by default
  * Ghosty as a zig build dependency exports the static lib as
  `dep.artifact("ghostty-vt-static")`
  * CMake exports the static lib as `ghostty-vt-static`
  
  Note that the static library is _not fat_. **If you enable SIMD you have
  dependencies** and you need to manually link those: libc++, simdutf, and
  highway. The `c-cmake-static` example disables SIMD.
  ```
- [`1438a2f`](https://github.com/ghostty-org/ghostty/commit/1438a2fe4bea11e31d36f106e6191f2796595121) Update VOUCHED list ([#11731](https://github.com/ghostty-org/ghostty/issues/11731)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11729#issuecomment-4104386360)
  from @mitchellh.
  
  Vouch: @turbolent
  ```
- [`918840c`](https://github.com/ghostty-org/ghostty/commit/918840cf1d1d617d1c8bb63f738a56ca7c6f165d) vt: persist VT stream state across vt_write calls ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously, every call to vt_write created a fresh ReadonlyStream with
  new Parser and UTF8Decoder state. This meant escape sequences split
  across write boundaries (e.g. ESC in one write, [27m in the next)
  would lose parser state, causing the second write to start in ground
  state and print the CSI parameters as literal text.
  
  The C API now stores a persistent ReadonlyStream in the TerminalWrapper
  struct, which is created when the Terminal is initialized. The vt_write
  function feeds bytes through this stored stream, allowing it to maintain
  parser state across calls. This change ensures that escape sequences
  split across write boundaries are correctly parsed and rendered.
  ```
- [`ed13978`](https://github.com/ghostty-org/ghostty/commit/ed1397826b03fc91eb07337d070290045bad0365) vt: persist VT stream state across vt_write calls ([#11728](https://github.com/ghostty-org/ghostty/issues/11728)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously, every call to vt_write created a fresh ReadonlyStream with
  new Parser and UTF8Decoder state. This meant escape sequences split
  across write boundaries (e.g. ESC in one write, [27m in the next) would
  lose parser state, causing the second write to start in ground state and
  print the CSI parameters as literal text.
  
  The C API now stores a persistent ReadonlyStream in the TerminalWrapper
  struct, which is created when the Terminal is initialized. The vt_write
  function feeds bytes through this stored stream, allowing it to maintain
  parser state across calls. This change ensures that escape sequences
  split across write boundaries are correctly parsed and rendered.
  ```
- [`50113ab`](https://github.com/ghostty-org/ghostty/commit/50113ab67860893969bbfe568261a293d91bf92f) macOS: add mouse state tests for [#11276](https://github.com/ghostty-org/ghostty/issues/11276) ([@bo2themax](https://github.com/bo2themax))
  ```text
  It will fail on 4e24adf71 and success after #11276
  ```
- [`ac3893d`](https://github.com/ghostty-org/ghostty/commit/ac3893d0b9c91b3d3b023556e30783fabaf3f082) macOS: Add command palette tests ([@bo2themax](https://github.com/bo2themax))
- [`d80d848`](https://github.com/ghostty-org/ghostty/commit/d80d84862e3b10bf97cfcda67b241152db2fe4e8) macOS: fix mouse not working correctly in CommandPaletteView ([#11658](https://github.com/ghostty-org/ghostty/issues/11658)) ([@bo2themax](https://github.com/bo2themax))
- [`3da7fb9`](https://github.com/ghostty-org/ghostty/commit/3da7fb9fdee4eeab067a27bb4b368702a68f0533) macOS: fix mouse not working correctly in CommandPaletteView ([#11658](https://github.com/ghostty-org/ghostty/issues/11658)) ([#11665](https://github.com/ghostty-org/ghostty/issues/11665)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Also added a test case for
  https://github.com/ghostty-org/ghostty/pull/11276, which will fail right
  before that commit.
  
  ## AI Disclosure
  
  Claude helped me to write some dummy texts for testing
  ```
- [`c3b7fd8`](https://github.com/ghostty-org/ghostty/commit/c3b7fd8477ebbff36a379c6cc782f76cf3a5441f) vt: add ghostty_build_info API for querying build configuration ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a new C API function ghostty_build_info() that exposes compile-time
  build options to library consumers. This allows callers to query whether
  SIMD, Kitty graphics protocol, and tmux control mode support were
  enabled at build time.
  ```
- [`abefe5b`](https://github.com/ghostty-org/ghostty/commit/abefe5b40cfa7d627998b6fc91cc213260d18825) vt: add ghostty_build_info API for querying build configuration ([#11725](https://github.com/ghostty-org/ghostty/issues/11725)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a new C API function ghostty_build_info() that exposes compile-time
  build options to library consumers. This allows callers to query whether
  SIMD, Kitty graphics protocol, and tmux control mode support were
  enabled at build time.
  ```
- [`155bd3a`](https://github.com/ghostty-org/ghostty/commit/155bd3a58e6d18d01162614a1ac237f9b74e4a61) vt: expose optimize mode in build info API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add GHOSTTY_BUILD_INFO_OPTIMIZE to query the Zig optimization mode
  (debug, release safe/small/fast) the library was compiled with. This
  reads directly from builtin.mode at comptime so it requires no build
  system plumbing.
  ```
- [`3fc04fd`](https://github.com/ghostty-org/ghostty/commit/3fc04fd4ae9bab243e6023acdf024abf78270e88) build: replace lib-vt step with -Demit-lib-vt option ([@mitchellh](https://github.com/mitchellh))
  ```text
  Remove the dedicated `zig build lib-vt` step and replace it with a
  `-Demit-lib-vt` build option. This fixes two problems:
  
  1. We can default XCFramework, app, etc. steps to false if emit-lib-vt
     is true, so that the lib-vt build doesn't pull in unrelated
     artifacts. **Most importantly, lib-vt alone can be build without
     full Xcode installations.**
  
  2. We can build lib-vt as part of a bundle with other artifacts if we
     really want.
  ```
- [`a49747d`](https://github.com/ghostty-org/ghostty/commit/a49747df52ad3a411b3019141a144678f59a3495) build: replace lib-vt step with -Demit-lib-vt option ([#11716](https://github.com/ghostty-org/ghostty/issues/11716)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Remove the dedicated `zig build lib-vt` step and replace it with a
  `-Demit-lib-vt` build option. This fixes two problems:
  
  1. We can default XCFramework, app, etc. steps to false if emit-lib-vt
  is true, so that the lib-vt build doesn't pull in unrelated artifacts.
  **Most importantly, lib-vt alone can be build without full Xcode
  installations.**
  
  2. We can build lib-vt as part of a bundle with other artifacts if we
  really want.
  ```
- [`b66120d`](https://github.com/ghostty-org/ghostty/commit/b66120d37d3001b3901f62d869266ba9dba0f60d) vt: add color_palette and color_rgb cell data types ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add two new CellData variants to extract background color values
  directly from cells. color_palette (10) returns the palette index
  as a GhosttyColorPaletteIndex and color_rgb (11) returns the RGB
  components as a GhosttyColorRgb. Both reuse the existing color
  types from color.h rather than introducing new ones.
  
  These are only valid when the cell content_tag is
  bg_color_palette or bg_color_rgb respectively; querying them
  with a mismatched tag reads from the wrong union member.
  ```
- [`efb3523`](https://github.com/ghostty-org/ghostty/commit/efb35235919a38bb04ac8b8ef06537f0317b7045) vt: add color_palette and color_rgb cell data types ([#11717](https://github.com/ghostty-org/ghostty/issues/11717)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add two new CellData variants to extract background color values
  directly from cells. color_palette (10) returns the palette index as a
  GhosttyColorPaletteIndex and color_rgb (11) returns the RGB components
  as a GhosttyColorRgb. Both reuse the existing color types from color.h
  rather than introducing new ones.
  
  These are only valid when the cell content_tag is
  bg_color_palette or bg_color_rgb respectively; querying them with a
  mismatched tag reads from the wrong union member.
  
  Found via Ghostling.
  ```

## March 20, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23365823171), [2](https://github.com/ghostty-org/ghostty/actions/runs/23359486964), [3](https://github.com/ghostty-org/ghostty/actions/runs/23358549711), [4](https://github.com/ghostty-org/ghostty/actions/runs/23353940580), [5](https://github.com/ghostty-org/ghostty/actions/runs/23352929301), [6](https://github.com/ghostty-org/ghostty/actions/runs/23350746193), [7](https://github.com/ghostty-org/ghostty/actions/runs/23349031592), [8](https://github.com/ghostty-org/ghostty/actions/runs/23347190522), [9](https://github.com/ghostty-org/ghostty/actions/runs/23345798479), [10](https://github.com/ghostty-org/ghostty/actions/runs/23327743605), [11](https://github.com/ghostty-org/ghostty/actions/runs/23326999168)  
Summary: 11 runs • 63 commits • 8 authors

### Changes

- [`0e0db10`](https://github.com/ghostty-org/ghostty/commit/0e0db1074b3d4e4c6470215ea5226c636cbaafa4) build: set zig optimize flag for CMake release builds ([@mitchellh](https://github.com/mitchellh))
  ```text
  Map CMake release build types (Release, MinSizeRel, RelWithDebInfo)
  to -Doptimize=ReleaseFast so that zig build automatically produces
  optimized builds when CMake is configured for a release variant.
  Debug builds remain unaffected, letting Zig use its default Debug
  optimization level.
  ```
- [`e8fb7ea`](https://github.com/ghostty-org/ghostty/commit/e8fb7eabad8bd4bebb64ca7fcad80442763dcb84) build: set zig optimize flag for CMake release builds ([#11707](https://github.com/ghostty-org/ghostty/issues/11707)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Map CMake release build types (Release, MinSizeRel, RelWithDebInfo) to
  -Doptimize=ReleaseFast so that zig build automatically produces
  optimized builds when CMake is configured for a release variant. Debug
  builds remain unaffected, letting Zig use its default Debug optimization
  level.
  ```
- [`89ae0ea`](https://github.com/ghostty-org/ghostty/commit/89ae0ea6ef089389aec0011e53c9b00e380c4e65) core: add function to get process info from the surface ([@jcollie](https://github.com/jcollie))
  ```text
  This adds a function to the core surface to get process information
  about the process(es) running in the terminal. Currently supported is
  the PID of the foreground process and the name of the slave PTY.
  
  If there is an error retrieving the information, or the platform does
  not support retieving that information `null` is returned.
  
  This will be useful in exposing the foreground PID and slave PTY name to
  AppleScript or other APIs.
  ```
- [`64de418`](https://github.com/ghostty-org/ghostty/commit/64de418f38f8739ba2259b5e8cc6ba51a74cdc30) core: add macos system include path ([@jcollie](https://github.com/jcollie))
- [`264a1a7`](https://github.com/ghostty-org/ghostty/commit/264a1a7cddee96b978c40ba538af3444d7a6c550) core: fix target for macos libc search ([@jcollie](https://github.com/jcollie))
- [`2ea6029`](https://github.com/ghostty-org/ghostty/commit/2ea6029c7adc08f245ef243a77915ec40c7566b4) core: address getProcessInfo feedback ([@jcollie](https://github.com/jcollie))
  ```text
  * consolidate *.c files into a single file
  * consolidate ProcessInfo enums into a single enum
  ```
- [`b0789af`](https://github.com/ghostty-org/ghostty/commit/b0789af583c9aac555bdc384041d02123dbbd2e7) core: fix c macro comparisons ([@jcollie](https://github.com/jcollie))
- [`d5ce05f`](https://github.com/ghostty-org/ghostty/commit/d5ce05fd37d8f9c94025e71cfd0b7c9ec290a5ce) core: simplify pty.c macro usage ([@jcollie](https://github.com/jcollie))
- [`7b9e49a`](https://github.com/ghostty-org/ghostty/commit/7b9e49a47fbacd2c776aab47470f1b769a6de58f) core: build pty.c only on certain platforms (avoids building os iOS) ([@jcollie](https://github.com/jcollie))
- [`fa84b87`](https://github.com/ghostty-org/ghostty/commit/fa84b8709c7e42be1588da97c9cf957e1be66a98) ci: add build-cmake job to test cmake build of libghostty-vt ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a new CI job that builds the root CMakeLists.txt to ensure the
  cmake wrapper for libghostty-vt works.
  
  This isn't the recommend way to build libghostty-vt, but its how
  downstream CMake projects would consume it so we gotta keep it
  working.
  ```
- [`0066dfa`](https://github.com/ghostty-org/ghostty/commit/0066dfa9f672e04451d6433db684d496c407422f) core: add function to get process info from the surface ([#11639](https://github.com/ghostty-org/ghostty/issues/11639)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds a function to the core surface to get process information
  about the process(es) running in the terminal. Currently supported is
  the PID of the foreground process and the name of the slave PTY.
  
  If there is an error retrieving the information, or the platform does
  not support retieving that information `null` is returned.
  
  This will be useful in exposing the foreground PID and slave PTY name to
  AppleScript or other APIs.
  ```
- [`72fea09`](https://github.com/ghostty-org/ghostty/commit/72fea098dccc8b9a7b71b69f54975c698587a8ba) ci: add build-cmake job to test cmake build of libghostty-vt ([#11703](https://github.com/ghostty-org/ghostty/issues/11703)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a new CI job that builds the root CMakeLists.txt to ensure the cmake
  wrapper for libghostty-vt works.
  
  This isn't the recommend way to build libghostty-vt, but its how
  downstream CMake projects would consume it so we gotta keep it working.
  ```
- [`3dee62f`](https://github.com/ghostty-org/ghostty/commit/3dee62f9046e0fcbc9841ccfe4a96d7f78fd90c4) build: add CMake support for libghostty-vt ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a top-level CMakeLists.txt that wraps `zig build lib-vt` so that
  CMake-based downstream projects can consume libghostty-vt without
  needing to interact with the Zig build system directly. A custom
  command triggers the zig build during `cmake --build`, and the
  resulting shared library is exposed as an IMPORTED target.
  
  Downstream projects can pull in the library via FetchContent, which
  fetches the source and builds it as part of their own CMake build, or
  via find_package after a manual install step. The package config
  template in dist/cmake/ sets up the ghostty-vt::ghostty-vt target
  with proper include paths and macOS rpath handling.
  
  A c-vt-cmake example demonstrates the FetchContent workflow, creating
  a terminal, writing VT sequences, and formatting the output as plain
  text. CI is updated to auto-discover and build CMake-based examples
  alongside the existing Zig-based ones.
  ```
- [`9ba2614`](https://github.com/ghostty-org/ghostty/commit/9ba2614ac1926b64c884923f4be233daeec98643) build: add CMake support for libghostty-vt ([#11700](https://github.com/ghostty-org/ghostty/issues/11700)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Add a top-level CMakeLists.txt that wraps `zig build lib-vt` so that
  CMake-based downstream projects can consume libghostty-vt without
  needing to interact with the Zig build system directly. A custom command
  triggers the zig build during `cmake --build`, and the resulting shared
  library is exposed as an IMPORTED target.
  
  Downstream projects can pull in the library via FetchContent, which
  fetches the source and builds it as part of their own CMake build, or
  via find_package after a manual install step. The package config
  template in dist/cmake/ sets up the ghostty-vt::ghostty-vt target with
  proper include paths and macOS rpath handling.
  
  A c-vt-cmake example demonstrates the FetchContent workflow, creating a
  terminal, writing VT sequences, and formatting the output as plain text.
  CI is updated to auto-discover and build CMake-based examples alongside
  the existing Zig-based ones.
  
  > [!WARNING]
  >
  > I am **very much not a CMake expert.** I leaned on LLMs heavily for
  this. I did read the docs for what was chosen here and understand what's
  going on, but if there is a better or more idiomatic way to do this I'm
  all ears!
  
  ## Example CMake File
  
  ```cmake
  cmake_minimum_required(VERSION 3.19)
  project(c-vt-cmake LANGUAGES C)
  
  include(FetchContent)
  FetchContent_Declare(ghostty
      GIT_REPOSITORY https://github.com/ghostty-org/ghostty.git
      GIT_TAG main
  )
  FetchContent_MakeAvailable(ghostty)
  
  add_executable(c_vt_cmake src/main.c)
  target_link_libraries(c_vt_cmake PRIVATE ghostty-vt)
  ```
  ````
- [`542d6aa`](https://github.com/ghostty-org/ghostty/commit/542d6aa14d2f9a4d522f3ca614dbcc6264191740) windows: avoid fontconfig and ensure build compiles ([@marler8997](https://github.com/marler8997))
- [`aac4916`](https://github.com/ghostty-org/ghostty/commit/aac491657be1c17f214a32c6ee0b1a221bf99bd1) windows: avoid fontconfig and ensure build compiles ([#11698](https://github.com/ghostty-org/ghostty/issues/11698)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This changes allows me to use ghostty as a zon dependency when building
  on windows (for windows). Fixes
  https://github.com/ghostty-org/ghostty/discussions/11697
  ```
- [`a0d7386`](https://github.com/ghostty-org/ghostty/commit/a0d738697e37046b77f3a391b39340a86235a4c0) vt: add c render state api and example ([@mitchellh](https://github.com/mitchellh))
  ```text
  Introduce the first public C render-state surface for libghostty-vt.
  Before this change, the render-state path was only available in Zig,
  so C embedders had no direct way to create and update that cache.
  
  Add an opaque GhosttyRenderState type with new, update, and free
  entry points, then wire those symbols through the C API bridge and
  library exports. Keep the surface intentionally minimal for now so
  ownership and update behavior are established before adding read
  accessors.
  ```
- [`2876fb7`](https://github.com/ghostty-org/ghostty/commit/2876fb7a555708e8ac6884e4c4d5e251e5ab026a) vt: expose dirty state in C API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Switch RenderState.Dirty to lib.Enum so it uses C-compatible enum
  backing when building the C ABI target. Add GhosttyRenderStateDirty and
  new ghostty_render_state_dirty_get/set declarations to the render header,
  then wire both functions through src/terminal/c/main.zig and the lib_vt
  export table.
  ```
- [`b830a0e`](https://github.com/ghostty-org/ghostty/commit/b830a0ee1d2d14f559a08191aa46ecb0ea1b524e) vt: add size getter for render state ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add ghostty_render_state_size_get() to return cols and rows from the
  current render state using out pointers. The C wrapper validates null
  inputs, the symbol is wired through the C API export layers, and tests
  cover success and invalid-value paths.
  ```
- [`b35f8ed`](https://github.com/ghostty-org/ghostty/commit/b35f8ed16eeeb401045e139d8c658214aefd3248) vt: expose render state colors in C API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a C-facing GhosttyRenderStateColors sized struct and a
  ghostty_render_state_colors_get accessor so renderers can read
  background, foreground, cursor color state, and palette data directly
  from the render state.
  ```
- [`ad0e47e`](https://github.com/ghostty-org/ghostty/commit/ad0e47ebac90e4b1b1d4a816c3c7be4ae744688b) vt: cover c row iterator new/free ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a C ABI row-iterator handle for render state with
  ghostty_render_state_row_iterator_new and
  ghostty_render_state_row_iterator_free, and wire them through
  src/terminal/c/main.zig, src/lib_vt.zig, and
  include/ghostty/vt/render.h. The header now documents only the
  currently exported iterator API.
  ```
- [`f610d7e`](https://github.com/ghostty-org/ghostty/commit/f610d7e00fed12d00c2731781ddabe9f4ef9e39a) vt: add render_row_iterator_next ([@mitchellh](https://github.com/mitchellh))
- [`2147b9d`](https://github.com/ghostty-org/ghostty/commit/2147b9d65c6f5b04ef784c4c624709ff5c401dba) vt: row dirty tracking ([@mitchellh](https://github.com/mitchellh))
- [`900afa7`](https://github.com/ghostty-org/ghostty/commit/900afa7b80e68dde673761e58bebf4b494eaae87) fix types ([@mitchellh](https://github.com/mitchellh))
- [`459583a`](https://github.com/ghostty-org/ghostty/commit/459583a6c396f04d303d24dd635bc947b9204e90) vt: use get/set pattern for render state data access ([@mitchellh](https://github.com/mitchellh))
  ```text
  Replace the individual ghostty_render_state_size_get,
  ghostty_render_state_dirty_get, and ghostty_render_state_dirty_set
  functions with generic ghostty_render_state_get and
  ghostty_render_state_set functions that use enum-dispatched data
  kinds and option kinds, following the same InType/OutType pattern
  used by the terminal and mouse encoder C APIs.
  ```
- [`33e81ff`](https://github.com/ghostty-org/ghostty/commit/33e81ffb7546dbe79bab074e3982ef5d74be4bb4) vt: use get/set pattern for row iterator data access ([@mitchellh](https://github.com/mitchellh))
  ```text
  Replace ghostty_render_state_row_dirty_get and
  ghostty_render_state_row_dirty_set with generic
  ghostty_render_state_row_get and ghostty_render_state_row_set
  functions using enum-dispatched data/option kinds.
  ```
- [`75b4905`](https://github.com/ghostty-org/ghostty/commit/75b49051a3bb2cd8da564e0a72ef8b0abacf8dc2) vt: add GhosttyRenderStateRowCells opaque type ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a new opaque RowCells type that wraps per-row cell data
  (raw cells, graphemes, styles) for the C API. The caller
  allocates a RowCells handle via row_cells_new, then populates
  it by passing it to row_get with the new .cells data kind.
  This queries the current row from the iterator and slices the
  underlying MultiArrayList into the RowCellsWrapper fields.
  
  The new type and functions are wired through main.zig,
  lib_vt.zig, and the render.h C header.
  ```
- [`ecd1d0d`](https://github.com/ghostty-org/ghostty/commit/ecd1d0d1e1a6337af31400c50bd9767f16636823) vt: decouple row iterator allocation from population ([@mitchellh](https://github.com/mitchellh))
  ```text
  Change row_iterator_new to only allocate with undefined fields,
  matching the pattern used by row_cells_new. The iterator is now
  populated via the render state get API with a new .row_iterator
  data kind, which slices the row data and resets y to null.
  
  This separates the lifetime of the opaque handle from the render
  state it iterates, letting callers allocate once and re-populate
  from different states without reallocating.
  ```
- [`6ae17a0`](https://github.com/ghostty-org/ghostty/commit/6ae17a02af8e831c6a798acdcdd81d6c82f2bea8) vt: add cell-level iteration and data access to render state row cells ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add next, select, and get functions to the render state row cells
  API, mirroring the row iterator pattern. row_cells_next advances to
  the next cell sequentially, row_cells_select jumps to a specific
  column index with bounds validation, and row_cells_get queries data
  for the current cell position.
  
  The get function supports querying raw cell values (GhosttyCell),
  resolved styles (GhosttyStyle), grapheme codepoint counts, and
  writing grapheme codepoints into a caller-provided buffer.
  
  Also add Cell.C and Cell.cval() to page.zig, matching the existing
  Row.C/Row.cval() pattern, so the render state can convert cells to
  the C ABI type without a raw bitCast.
  ```
- [`60ea2d7`](https://github.com/ghostty-org/ghostty/commit/60ea2d76d46b6333357cece7e14a8ad841f6521a) vt: add color data getters to render state ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add individual color data kinds to GhosttyRenderStateData so callers
  can query background, foreground, cursor color, cursor-color presence,
  and the full 256-color palette through ghostty_render_state_get()
  without using the sized-struct colors API.
  
  COLOR_CURSOR returns GHOSTTY_INVALID_VALUE when no explicit cursor
  color is set; callers can check COLOR_CURSOR_HAS_VALUE first.
  ```
- [`d9df415`](https://github.com/ghostty-org/ghostty/commit/d9df4154dbe6a21e43c96cc1537b3724a0c784ba) vt: add cursor field data getters to render state API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Expose the cursor fields from RenderState.Cursor through the C API
  via new GhosttyRenderStateData enum values. This adds getters for
  visual style, visibility, blink state, password input detection,
  and viewport position (x, y, wide tail).
  
  A new GhosttyRenderStateCursorVisualStyle enum maps the Zig
  cursor.Style values (bar, block, underline, block_hollow) to
  stable C integer constants. Viewport position getters return
  GHOSTTY_INVALID_VALUE when the cursor is not visible within
  the viewport.
  ```
- [`e7a18ea`](https://github.com/ghostty-org/ghostty/commit/e7a18ea5b358afe2490fe61ef7cbd3321825f2f1) vt: fix render state cell style and graphemes_buf APIs ([@mitchellh](https://github.com/mitchellh))
  ```text
  The GRAPHEMES_BUF data kind previously required a double pointer
  (pointer to a uint32_t*) because the OutType was [*]u32, making the
  typed out parameter *[*]u32. Change OutType to u32 so that callers
  pass a plain uint32_t* buffer directly, which is the natural C
  calling convention. The implementation casts the out pointer to
  [*]u32 internally to write into the buffer.
  
  The STYLE data kind read directly from the render state style array
  without checking whether the cell actually had non-default styling.
  The style data is undefined for unstyled cells, so this caused a
  panic on a corrupt enum value when the caller read the style of an
  unstyled cell. Now check cell.hasStyling() first and return the
  default style for unstyled cells.
  
  Expand the c-vt-render example to exercise dirty tracking, color
  retrieval, cursor state, row/cell iteration with style resolution,
  and dirty state reset. Break the example into six doxygen snippet
  regions and reference them from render.h.
  ```
- [`00ffc22`](https://github.com/ghostty-org/ghostty/commit/00ffc22ecbd769c62a597423540aea8ebf6afe54) libghostty: starting render state API in C ([#11664](https://github.com/ghostty-org/ghostty/issues/11664)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This adds the `terminal.RenderState` API for C.
  
  The render state API is the API that should be used to create a high
  performance renderer. It limits access to a terminal instance to a very
  optimized `update` call so that terminal IO is blocked for a tiny amount
  of time. After that, all read access on the RenderState is safe to build
  frame data.
  
  ## Example
  
  ```c
  int main(void) {
    GhosttyResult result;
  
    GhosttyTerminal terminal = NULL;
    GhosttyTerminalOptions terminal_opts = {
        .cols = 80,
        .rows = 24,
        .max_scrollback = 10000,
    };
    result = ghostty_terminal_new(NULL, &terminal, terminal_opts);
    assert(result == GHOSTTY_SUCCESS);
  
    GhosttyRenderState render_state = NULL;
    result = ghostty_render_state_new(NULL, &render_state);
    assert(result == GHOSTTY_SUCCESS);
  
    const char* first_frame = "first frame\r\n";
    ghostty_terminal_vt_write(
        terminal,
        (const uint8_t*)first_frame,
        strlen(first_frame));
    result = ghostty_render_state_update(render_state, terminal);
    assert(result == GHOSTTY_SUCCESS);
  
    const char* second_frame = "second frame\r\n";
    ghostty_terminal_vt_write(
        terminal,
        (const uint8_t*)second_frame,
        strlen(second_frame));
    result = ghostty_render_state_update(render_state, terminal);
    assert(result == GHOSTTY_SUCCESS);
  
    printf("Render state was updated successfully.\n");
  
    ghostty_render_state_free(render_state);
    ghostty_terminal_free(terminal);
    return 0;
  }
  ```
  
  ## API Changes
  
  New `GhosttyRenderState` C API (`include/ghostty/vt/render.h`):
  
  | Function | Description |
  |---|---|
  | `ghostty_render_state_new` | Allocate an empty render state. |
  | `ghostty_render_state_free` | Destroy a render state. |
  | `ghostty_render_state_update` | Snapshot a terminal instance into the
  render state. |
  | `ghostty_render_state_get` | Type-tagged read of dimensions, dirty
  state, colors, cursor, palette. |
  | `ghostty_render_state_set` | Type-tagged write (currently: dirty
  state). |
  | `ghostty_render_state_colors_get` | Bulk color read via sized-struct
  for forward compatibility. |
  | `ghostty_render_state_row_iterator_new` | Allocate a reusable row
  iterator. |
  | `ghostty_render_state_row_iterator_next` | Advance the row iterator. |
  | `ghostty_render_state_row_iterator_free` | Destroy a row iterator. |
  | `ghostty_render_state_row_get` | Read per-row data (dirty flag, raw
  row, cells). |
  | `ghostty_render_state_row_set` | Write per-row data (dirty flag). |
  | `ghostty_render_state_row_cells_new` | Allocate a reusable cell
  iterator. |
  | `ghostty_render_state_row_cells_next` | Advance the cell iterator. |
  | `ghostty_render_state_row_cells_select` | Jump the cell iterator to a
  specific column. |
  | `ghostty_render_state_row_cells_get` | Read per-cell data (raw cell,
  style, graphemes). |
  | `ghostty_render_state_row_cells_free` | Destroy a cell iterator. |
  
  `GhosttyRenderStateData` keys (for `_get`):
  
  | Key | Type | Description |
  |---|---|---|
  | `COLS` | `uint16_t` | Viewport width in cells. |
  | `ROWS` | `uint16_t` | Viewport height in cells. |
  | `DIRTY` | `GhosttyRenderStateDirty` | Global dirty state. |
  | `ROW_ITERATOR` | `GhosttyRenderStateRowIterator` | Populate a
  pre-allocated row iterator. |
  | `COLOR_BACKGROUND` | `GhosttyColorRgb` | Default background color. |
  | `COLOR_FOREGROUND` | `GhosttyColorRgb` | Default foreground color. |
  | `COLOR_CURSOR` | `GhosttyColorRgb` | Explicit cursor color (invalid if
  not set). |
  | `COLOR_CURSOR_HAS_VALUE` | `bool` | Whether an explicit cursor color
  is set. |
  | `COLOR_PALETTE` | `GhosttyColorRgb[256]` | Active 256-color palette. |
  | `CURSOR_VISUAL_STYLE` | `GhosttyRenderStateCursorVisualStyle` | Bar,
  block, underline, or hollow block. |
  | `CURSOR_VISIBLE` | `bool` | Cursor visibility from terminal modes. |
  | `CURSOR_BLINKING` | `bool` | Cursor blink state from terminal modes. |
  | `CURSOR_PASSWORD_INPUT` | `bool` | Whether cursor is at a password
  field. |
  | `CURSOR_VIEWPORT_HAS_VALUE` | `bool` | Whether cursor is in the
  viewport. |
  | `CURSOR_VIEWPORT_X` | `uint16_t` | Cursor viewport column. |
  | `CURSOR_VIEWPORT_Y` | `uint16_t` | Cursor viewport row. |
  | `CURSOR_VIEWPORT_WIDE_TAIL` | `bool` | Cursor on wide-char tail cell.
  |
  
  `GhosttyRenderStateOption` keys (for `_set`):
  
  | Key | Type | Description |
  |---|---|---|
  | `DIRTY` | `GhosttyRenderStateDirty` | Reset global dirty state. |
  
  `GhosttyRenderStateRowData` keys (for `_row_get`):
  
  | Key | Type | Description |
  |---|---|---|
  | `DIRTY` | `bool` | Whether this row is dirty. |
  | `RAW` | `GhosttyRow` | Raw row value. |
  | `CELLS` | `GhosttyRenderStateRowCells` | Populate a pre-allocated cell
  iterator. |
  
  `GhosttyRenderStateRowOption` keys (for `_row_set`):
  
  | Key | Type | Description |
  |---|---|---|
  | `DIRTY` | `bool` | Clear/set dirty flag for this row. |
  
  `GhosttyRenderStateRowCellsData` keys (for `_row_cells_get`):
  
  | Key | Type | Description |
  |---|---|---|
  | `RAW` | `GhosttyCell` | Raw cell value. |
  | `STYLE` | `GhosttyStyle` | Resolved style for this cell. |
  | `GRAPHEMES_LEN` | `uint32_t` | Total codepoints including base (0 if
  empty). |
  | `GRAPHEMES_BUF` | `uint32_t*` | Write codepoints into caller buffer. |
  ````
- [`e680cf9`](https://github.com/ghostty-org/ghostty/commit/e680cf9f358ce37a4e91d6025f567dff3e4c1f19) Update VOUCHED list ([#11699](https://github.com/ghostty-org/ghostty/issues/11699)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11698#issuecomment-4099492496)
  from @mitchellh.
  
  Vouch: @marler8997
  ```
- [`220d6fd`](https://github.com/ghostty-org/ghostty/commit/220d6fd43d1199b160fca3f95a62b4a8c295b4d3) nix: add systems input and fix zig follows ([@luisnquin](https://github.com/luisnquin))
- [`a888db9`](https://github.com/ghostty-org/ghostty/commit/a888db94b050bd267877ccdf0737f34efb6df7ea) nix: add systems input and fix zig follows ([#11686](https://github.com/ghostty-org/ghostty/issues/11686)) ([@jcollie](https://github.com/jcollie))
  ```text
  Currently I have to use [this unusual
  syntax](https://github.com/luisnquin/nixos-config/blob/6e1c9f32e0f35bc3423af3b895c10a8fe97e7e18/flake.nix#L137)
  in my flake inputs to ensure that I don't have systems repeated in my
  flake.lock file. This will make more obvious the fact that you have to
  do follows to that hidden input.
  ```
- [`9e2e99c`](https://github.com/ghostty-org/ghostty/commit/9e2e99c55fb5f2c0709938eb590b62112f3d7446) gtk/wayland: replace KDE blur with ext-background-effect-v1 ([@pluiedev](https://github.com/pluiedev))
  ```text
  The venerable KDE blur protocol has been replaced with the compositor-
  agnostic ext-background-effect-v1 protocol, to be implemented by Niri and
  others. The new protocol is much easier to use overall, though we do need
  to calculate the blur region manually like X11.
  ```
- [`5abf21c`](https://github.com/ghostty-org/ghostty/commit/5abf21c1e229266749fcc711b2b7a07e366a4542) gtk/wayland: complete blur region calculation ([@pluiedev](https://github.com/pluiedev))
  ```text
  It took me a while and with lots of trial and error to arrive here,
  but the end result looks pretty good.
  ```
- [`80ab5d9`](https://github.com/ghostty-org/ghostty/commit/80ab5d92eab280296bab23067d257b87d1244fab) gtk/x11: use BlurRegion ([@pluiedev](https://github.com/pluiedev))
- [`27fd1c7`](https://github.com/ghostty-org/ghostty/commit/27fd1c7788a3ebdf347b54c5bc9c1c329f175397) gtk/winproto: fix memleak & other tweaks ([@pluiedev](https://github.com/pluiedev))
- [`9c30bfa`](https://github.com/ghostty-org/ghostty/commit/9c30bfadc5d8e7ebf7ea6a7d7b45bf02c3b4ca7b) gtk: various blur-related fixes  ([#10727](https://github.com/ghostty-org/ghostty/issues/10727)) ([@pluiedev](https://github.com/pluiedev))
- [`46ece22`](https://github.com/ghostty-org/ghostty/commit/46ece224ba4e7a4e3243a27a29d7aafaf1273436) Update VOUCHED list ([#11694](https://github.com/ghostty-org/ghostty/issues/11694)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11420#discussioncomment-16227199)
  from @mitchellh.
  
  Vouch: @hlcfan
  ```
- [`4b9324f`](https://github.com/ghostty-org/ghostty/commit/4b9324f48a3499ec2329ce2e39ab58d368d871e8) bash: suppress __ghostty_hook errors in inherited PROMPT_COMMAND ([@jparise](https://github.com/jparise))
  ```text
  When some tools spawn subshells, PROMPT_COMMAND may be inherited as an
  environment variable while the __ghostty_hook function is not (bash
  doesn't export functions by default). This causes "command not found"
  errors on every prompt in the subshell.
  
  Add 2>/dev/null to the __ghostty_hook entry in PROMPT_COMMAND so that it
  silently no-ops in subshells where the function isn't defined. This also
  silences any errors from inside __ghostty_hook itself, but those are all
  terminal escape sequences and non-actionable.
  
  See: #11245
  ```
- [`e2399de`](https://github.com/ghostty-org/ghostty/commit/e2399de38c3bb5edb222660448e10e143ac9fba6) bash: suppress __ghostty_hook errors in inherited PROMPT_COMMAND ([#11690](https://github.com/ghostty-org/ghostty/issues/11690)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  When some tools spawn subshells, PROMPT_COMMAND may be inherited as an
  environment variable while the __ghostty_hook function is not (bash
  doesn't export functions by default). This causes "command not found"
  errors on every prompt in the subshell.
  
  Add 2>/dev/null to the __ghostty_hook entry in PROMPT_COMMAND so that it
  silently no-ops in subshells where the function isn't defined. This also
  silences any errors from inside __ghostty_hook itself, but those are all
  terminal escape sequences and non-actionable.
  
  See: #11245
  ```
- [`ff0ee36`](https://github.com/ghostty-org/ghostty/commit/ff0ee364bb04bdd554a81c80c43027a1f4f20edf) Update VOUCHED list ([#11691](https://github.com/ghostty-org/ghostty/issues/11691)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11686#issuecomment-4098087863)
  from @mitchellh.
  
  Vouch: @luisnquin
  ```
- [`f168b3c`](https://github.com/ghostty-org/ghostty/commit/f168b3c098eae1db30811173ac7cc5d5ac4da3c2) vt: add ghostty_terminal_get for reading terminal state ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a typed data query API to the terminal C interface, following
  the same OutType pattern used by the OSC command data API. The new
  ghostty_terminal_get function takes a GhosttyTerminalData tag and
  an output pointer, returning GhosttyResult.
  
  Currently exposes cols, rows, cursor x/y position, and cursor
  pending wrap state. The GhosttyTerminalData enum is placed with the
  other types in the header (before functions) per the ordering
  convention.
  ```
- [`7f36e8b`](https://github.com/ghostty-org/ghostty/commit/7f36e8bd43bdc52aa3398125ce8c42e5211adceb) vt: add style C API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Expose the terminal Style struct to the C API as GhosttyStyle, a
  sized struct with foreground, background, and underline colors
  (as tagged unions) plus boolean text decoration flags.
  
  Add ghostty_style_default() to obtain the default style and
  ghostty_style_is_default() to check whether a style has all
  default values. Wire both through c/style.zig, main.zig, and
  lib_vt.zig with the corresponding header in vt/style.h.
  ```
- [`d62f6df`](https://github.com/ghostty-org/ghostty/commit/d62f6df1d5370b6ec7a5de80dd15718a424e727e) vt: expose cursor_style via terminal_get ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add cursor_style to TerminalData, returning the current SGR style
  of the cursor (the style applied to newly printed characters) as a
  GhosttyStyle.
  
  Refactor the C style conversion helpers: replace the standalone
  convertStyle and convertColor functions with fromStyle and fromColor
  initializers on the Style and Color extern structs respectively.
  ```
- [`d827225`](https://github.com/ghostty-org/ghostty/commit/d827225573b673bc5c1756f2d14971638a472d53) vt: expand padding for color union to 64-bit to allow for a pointer ([@mitchellh](https://github.com/mitchellh))
- [`5c8b9f3`](https://github.com/ghostty-org/ghostty/commit/5c8b9f3f434abee1e70f454ec00301010ea01edf) vt: add GhosttyCell and GhosttyRow C API with data getters ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add opaque GhosttyCell (uint64_t) and GhosttyRow (uint64_t) types that
  bitcast to the internal packed Cell and Row structs from page.zig. Each
  type has a corresponding data enum and getter function following the
  same pattern as ghostty_terminal_get.
  
  ghostty_cell_get supports extracting codepoint, content tag, wide
  property, has_text, has_styling, style_id, has_hyperlink, protected,
  and semantic_content. ghostty_row_get supports wrap, wrap_continuation,
  grapheme, styled, hyperlink, semantic_prompt, kitty_virtual_placeholder,
  and dirty.
  
  The cell and row types and functions live in a new screen.h header,
  separate from terminal.h, with terminal.h including screen.h for
  convenience.
  ```
- [`057f227`](https://github.com/ghostty-org/ghostty/commit/057f227145fcce8d92678c16591d936f54f202b8) terminal: convert Point to lib.Enum/lib.TaggedUnion with C header ([@mitchellh](https://github.com/mitchellh))
- [`0400de2`](https://github.com/ghostty-org/ghostty/commit/0400de28b40bc47b0fcd0f5a78a908413cb86be6) vt: add ghostty_terminal_cell for point-based cell lookup ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a new C API function ghostty_terminal_cell that retrieves the
  opaque cell and row values at a given point in the terminal grid.
  The point is a tagged union supporting active, viewport, screen, and
  history coordinate systems.
  ```
- [`2a952b4`](https://github.com/ghostty-org/ghostty/commit/2a952b4dfeac0acda22e67779dabdc415757a0a7) bash: move __ghostty_preexec_hook into __ghostty_hook ([@jparise](https://github.com/jparise))
  ```text
  We previously used a readonly variable (__ghostty_ps0) to define the
  best __ghostty_preexec_hook expansion for the current bash version.
  
  This works pretty well, but it had the downside of managing another
  variable (#11258).
  
  We can instead simplify this a bit by moving this into __ghostty_hook. I
  didn't take that approach originally because I wanted to avoid the bash
  version check on each command, but slightly loosening our guard check to
  just look for "__ghostty_preexec_hook" (rather than the full expansion
  expression) means we can bury the bash version check to the cold path.
  
  One small gap here is that we may not update PS0 to the correct syntax
  if we start switching between significantly different bash versions in
  interactive subshells, but that seems like a pretty rare case to handle
  given the benefits of this approach.
  ```
- [`df8813b`](https://github.com/ghostty-org/ghostty/commit/df8813bf1b0a0526ee5da340b4398f85f0852c52) vt: replace ghostty_terminal_cell with GhosttyGridRef API ([@mitchellh](https://github.com/mitchellh))
- [`5498248`](https://github.com/ghostty-org/ghostty/commit/549824842dd72b2e77caf0d443a3b3951480c764) vt: add style and grapheme accessors ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add ghostty_grid_ref_style and ghostty_grid_ref_graphemes to the grid
  ref C API, allowing callers to extract the full style and grapheme
  cluster directly from a grid reference without manually resolving
  the page internals.
  ```
- [`93c597c`](https://github.com/ghostty-org/ghostty/commit/93c597ce6bb36179065d93a465d6ee679f7472f7) example: add grid reference traversal example ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a c-vt-grid-ref example that demonstrates the terminal and grid
  reference APIs end-to-end. The example creates a small 10x3 terminal,
  writes text with mixed styles via VT sequences, then iterates over
  every cell in the active area using ghostty_terminal_grid_ref. For
  each cell it extracts the codepoint, and for each row it inspects
  the wrap flag and the style bold attribute.
  
  The grid_ref.h defgroup gains a @snippet reference to the new example,
  and vt.h gets the corresponding @example entry and @ref listing.
  ```
- [`d2a29de`](https://github.com/ghostty-org/ghostty/commit/d2a29de95989d739d2b2dfcf2df8762fbbb9b1c8) libghostty: terminal data, grid point and cell inspection APIs ([#11676](https://github.com/ghostty-org/ghostty/issues/11676)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This adds a complete set of APIs for inspecting individual cells and
  rows in the terminal grid from C. Callers can now resolve any point in
  the grid to a reference, then extract codepoints, grapheme clusters,
  styles, wide-character state, semantic prompt tags, and row-level
  metadata like wrap and dirty flags.
  
  This also adds a robust `ghostty_terminal_get` API for extracting
  information like rows, cols, active screen, cursor information, etc.
  from the terminal.
  
  ## Example
  
  ```c
  // Write bold red text via SGR sequences
  const char *text = "\033[1;31mHello\033[0m";
  ghostty_terminal_vt_write(terminal, (const uint8_t *)text, strlen(text));
  
  // Resolve cell (0,0) to a grid reference
  GhosttyGridRef ref = GHOSTTY_INIT_SIZED(GhosttyGridRef);
  GhosttyPoint pt = {
    .tag = GHOSTTY_POINT_TAG_ACTIVE,
    .value = { .coordinate = { .x = 0, .y = 0 } },
  };
  ghostty_terminal_grid_ref(terminal, pt, &ref);
  
  // Read the codepoint ('H')
  GhosttyCell cell;
  ghostty_grid_ref_cell(&ref, &cell);
  uint32_t codepoint = 0;
  ghostty_cell_get(cell, GHOSTTY_CELL_DATA_CODEPOINT, &codepoint);
  
  // Read the resolved style (bold=true, fg=red)
  GhosttyStyle style = GHOSTTY_INIT_SIZED(GhosttyStyle);
  ghostty_grid_ref_style(&ref, &style);
  assert(style.bold);
  ```
  
  ## API Changes
  
  ### New Types
  
  | Type | Description |
  |------|-------------|
  | `GhosttyCell` | Opaque 64-bit cell value |
  | `GhosttyRow` | Opaque 64-bit row value |
  | `GhosttyCellData` | Enum for `ghostty_cell_get` data kinds (codepoint,
  content tag, wide, has_text, etc.) |
  | `GhosttyCellContentTag` | Cell content kind (codepoint, grapheme, bg
  color palette/RGB) |
  | `GhosttyCellWide` | Cell width (narrow, wide, spacer tail/head) |
  | `GhosttyCellSemanticContent` | Semantic content type (output, input,
  prompt) |
  | `GhosttyRowData` | Enum for `ghostty_row_get` data kinds (wrap,
  grapheme, styled, dirty, etc.) |
  | `GhosttyRowSemanticPrompt` | Row-level semantic prompt state |
  | `GhosttyGridRef` | Sized struct — resolved reference to a cell
  position in the page structure |
  | `GhosttyPoint` | Tagged union specifying a grid position in a given
  coordinate system |
  | `GhosttyPointTag` | Coordinate system tag: `ACTIVE`, `VIEWPORT`,
  `SCREEN`, `HISTORY` |
  | `GhosttyPointCoordinate` | x/y coordinate pair |
  | `GhosttyStyleId` | Style identifier type (uint16) |
  
  ### New Functions
  
  | Function | Description |
  |----------|-------------|
  | `ghostty_cell_get` | Extract typed data from a cell (codepoint, wide,
  style ID, etc.) |
  | `ghostty_row_get` | Extract typed data from a row (wrap, dirty,
  semantic prompt, etc.) |
  | `ghostty_terminal_grid_ref` | Resolve a `GhosttyPoint` to a
  `GhosttyGridRef` |
  | `ghostty_grid_ref_cell` | Extract the `GhosttyCell` from a grid ref |
  | `ghostty_grid_ref_row` | Extract the `GhosttyRow` from a grid ref |
  | `ghostty_grid_ref_graphemes` | Get the full grapheme cluster
  (codepoints) for the cell |
  | `ghostty_grid_ref_style` | Get the resolved `GhosttyStyle` for the
  cell |
  ````
- [`7966740`](https://github.com/ghostty-org/ghostty/commit/7966740b48b287f1ed1aa2a355afde3b81197933) bash: move __ghostty_preexec_hook into __ghostty_hook ([#11674](https://github.com/ghostty-org/ghostty/issues/11674)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  We previously used a readonly variable (__ghostty_ps0) to define the
  best __ghostty_preexec_hook expansion for the current bash version.
  
  This worked pretty well, but it had the downside of managing another
  variable (#11258).
  
  We can instead simplify this a bit by moving this into __ghostty_hook. I
  didn't take that approach originally because I wanted to avoid the bash
  version check on each command, but slightly loosening our guard check to
  just look for "__ghostty_preexec_hook" (rather than the full expansion
  expression) means we can bury the bash version check to the cold path.
  
  One small gap here is that we may not update PS0 to the correct syntax
  if we start switching between significantly different bash versions in
  interactive subshells, but that seems like a pretty rare case to handle
  given the benefits of this approach.
  ```
- [`10e6938`](https://github.com/ghostty-org/ghostty/commit/10e69384d7e6a59253dda2cc00482210f6e63ee7) build(deps): bump namespacelabs/nscloud-setup from 0.0.11 to 0.0.12 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [namespacelabs/nscloud-setup](https://github.com/namespacelabs/nscloud-setup) from 0.0.11 to 0.0.12.
  - [Release notes](https://github.com/namespacelabs/nscloud-setup/releases)
  - [Commits](https://github.com/namespacelabs/nscloud-setup/compare/f378676225212387f1283f4da878712af2c4cd60...df198f982fcecfb8264bea3f1274b56a61b6dfdc)
  
  ---
  updated-dependencies:
  - dependency-name: namespacelabs/nscloud-setup
    dependency-version: 0.0.12
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`7c14aec`](https://github.com/ghostty-org/ghostty/commit/7c14aecd3fb96cbc6c9c2035ebe830a38f1693e1) build(deps): bump namespacelabs/nscloud-setup-buildx-action ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [namespacelabs/nscloud-setup-buildx-action](https://github.com/namespacelabs/nscloud-setup-buildx-action) from 0.0.22 to 0.0.23.
  - [Release notes](https://github.com/namespacelabs/nscloud-setup-buildx-action/releases)
  - [Commits](https://github.com/namespacelabs/nscloud-setup-buildx-action/compare/f5814dcf37a16cce0624d5bec2ab879654294aa0...d059ed7184f0bc7c8b27e8810cea153d02bcc6dd)
  
  ---
  updated-dependencies:
  - dependency-name: namespacelabs/nscloud-setup-buildx-action
    dependency-version: 0.0.23
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`4531594`](https://github.com/ghostty-org/ghostty/commit/4531594d51f76b4350f6ec23d8916b59ae261ddc) build(deps): bump namespacelabs/nscloud-setup-buildx-action from 0.0.22 to 0.0.23 ([#11673](https://github.com/ghostty-org/ghostty/issues/11673)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [namespacelabs/nscloud-setup-buildx-action](https://github.com/namespacelabs/nscloud-setup-buildx-action)
  from 0.0.22 to 0.0.23.
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/namespacelabs/nscloud-setup-buildx-action/commit/d059ed7184f0bc7c8b27e8810cea153d02bcc6dd"><code>d059ed7</code></a>
  Update to node24 (<a
  href="https://redirect.github.com/namespacelabs/nscloud-setup-buildx-action/issues/15">#15</a>)</li>
  <li>See full diff in <a
  href="https://github.com/namespacelabs/nscloud-setup-buildx-action/compare/f5814dcf37a16cce0624d5bec2ab879654294aa0...d059ed7184f0bc7c8b27e8810cea153d02bcc6dd">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=namespacelabs/nscloud-setup-buildx-action&package-manager=github_actions&previous-version=0.0.22&new-version=0.0.23)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`e9eac7d`](https://github.com/ghostty-org/ghostty/commit/e9eac7d4758c5b7692c59e4dda89b2184ad18960) build(deps): bump namespacelabs/nscloud-setup from 0.0.11 to 0.0.12 ([#11672](https://github.com/ghostty-org/ghostty/issues/11672)) ([@jcollie](https://github.com/jcollie))
  ```text
  [//]: # (dependabot-start)
  ⚠️  **Dependabot is rebasing this PR** ⚠️
  
  Rebasing might not happen immediately, so don't worry if this takes some
  time.
  
  Note: if you make any changes to this PR yourself, they will take
  precedence over the rebase.
  
  ---
  
  [//]: # (dependabot-end)
  
  Bumps
  [namespacelabs/nscloud-setup](https://github.com/namespacelabs/nscloud-setup)
  from 0.0.11 to 0.0.12.
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/namespacelabs/nscloud-setup/commit/df198f982fcecfb8264bea3f1274b56a61b6dfdc"><code>df198f9</code></a>
  Update to node24 (<a
  href="https://redirect.github.com/namespacelabs/nscloud-setup/issues/10">#10</a>)</li>
  <li>See full diff in <a
  href="https://github.com/namespacelabs/nscloud-setup/compare/f378676225212387f1283f4da878712af2c4cd60...df198f982fcecfb8264bea3f1274b56a61b6dfdc">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=namespacelabs/nscloud-setup&package-manager=github_actions&previous-version=0.0.11&new-version=0.0.12)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`1f89ce9`](https://github.com/ghostty-org/ghostty/commit/1f89ce91d97065f04c196b84c391c7212bd50de0) Update VOUCHED list ([#11675](https://github.com/ghostty-org/ghostty/issues/11675)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11671#discussioncomment-16218675)
  from @jcollie.
  
  Vouch: @unphased
  ```

## March 19, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23303726826), [2](https://github.com/ghostty-org/ghostty/actions/runs/23294986782)  
Summary: 2 runs • 6 commits • 4 authors

### Changes

- [`c08a211`](https://github.com/ghostty-org/ghostty/commit/c08a21180aa98ee813bc97bf04e1d0c31ec2f65d) build(deps): bump cachix/cachix-action from 16 to 17 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [cachix/cachix-action](https://github.com/cachix/cachix-action) from 16 to 17.
  - [Release notes](https://github.com/cachix/cachix-action/releases)
  - [Commits](https://github.com/cachix/cachix-action/compare/3ba601ff5bbb07c7220846facfa2cd81eeee15a1...1eb2ef646ac0255473d23a5907ad7b04ce94065c)
  
  ---
  updated-dependencies:
  - dependency-name: cachix/cachix-action
    dependency-version: '17'
    dependency-type: direct:production
    update-type: version-update:semver-major
  ...
  ```
- [`b1ad24e`](https://github.com/ghostty-org/ghostty/commit/b1ad24e24f3c04d854ed2c516fd0b947cf800420) bash: emit 133;P (instead of 133;A) under ble.sh ([@jparise](https://github.com/jparise))
  ```text
  ble.sh performs its own cursor positioning so we get multiple newlines
  with 133;A's fresh-line behavior. ble.sh is a large enough project to
  justify this additional, unambiguous conditional.
  
  See: akinomyoga/ble.sh#684
  See: wezterm/wezterm#5072
  ```
- [`2bbbca3`](https://github.com/ghostty-org/ghostty/commit/2bbbca369d5fc67da8f2084f0b8973ef4619ba78) bash: emit 133;P (instead of 133;A) under ble.sh ([#11644](https://github.com/ghostty-org/ghostty/issues/11644)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ble.sh performs its own cursor positioning so we get multiple newlines
  with 133;A's fresh-line behavior. ble.sh is a large enough project to
  justify this additional, unambiguous conditional.
  
  See: akinomyoga/ble.sh#684
  See: wezterm/wezterm#5072
  ```
- [`c2e9de2`](https://github.com/ghostty-org/ghostty/commit/c2e9de224eaf09a2ce3e7cb2f6c26d6d577ed8f0) build(deps): bump cachix/cachix-action from 16 to 17 ([#11643](https://github.com/ghostty-org/ghostty/issues/11643)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps [cachix/cachix-action](https://github.com/cachix/cachix-action)
  from 16 to 17.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/cachix/cachix-action/releases">cachix/cachix-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v17</h2>
  <h2>What's Changed</h2>
  <h3>Breaking changes</h3>
  <ul>
  <li>Upgrade action to use Node 24 by <a
  href="https://github.com/sandydoo"><code>@​sandydoo</code></a> in <a
  href="https://redirect.github.com/cachix/cachix-action/pull/212">cachix/cachix-action#212</a>
  <a
  href="https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/">https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/cachix/cachix-action/compare/v16...v17">https://github.com/cachix/cachix-action/compare/v16...v17</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/1eb2ef646ac0255473d23a5907ad7b04ce94065c"><code>1eb2ef6</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/cachix-action/issues/212">#212</a>
  from cachix/upgrade-node-24</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/75ce400143912180b47fa504676215ca47e1634f"><code>75ce400</code></a>
  dist: re-build using esbuild targeting node24</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/2b33705a8232e51ac94414b3b8c203d0a5e42ca3"><code>2b33705</code></a>
  deps: update devenv inputs</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/04937db281cae63d98e660f990648ab4eef1cec1"><code>04937db</code></a>
  breaking: update action to Node 24</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/ca2e51995f0edefbb31bc858102abd109580c99c"><code>ca2e519</code></a>
  ci: use 25.11 for tests</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/e7c5c1add25228c774d40ae0adbd520ea7c919c0"><code>e7c5c1a</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/cachix-action/issues/208">#208</a>
  from cachix/dependabot/github_actions/actions/checkout-6</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/bea8a506457e59a062336709ee10a5677fd9a59e"><code>bea8a50</code></a>
  ci: allow running tests manually and with a custom nix version</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/2e35755955435b7976b76834528c38a0fcf725c0"><code>2e35755</code></a>
  chore(deps): bump actions/checkout from 5 to 6</li>
  <li>See full diff in <a
  href="https://github.com/cachix/cachix-action/compare/3ba601ff5bbb07c7220846facfa2cd81eeee15a1...1eb2ef646ac0255473d23a5907ad7b04ce94065c">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=cachix/cachix-action&package-manager=github_actions&previous-version=16&new-version=17)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`c9729fb`](https://github.com/ghostty-org/ghostty/commit/c9729fbd269d72a20eb4a53846dd3cd7ae1dfc4a) ci: use local git commands for path-filter action ([@jparise](https://github.com/jparise))
  ```text
  Passing a `token` value causes this action to use the GitHub REST API,
  which is subject to rate limits. We can chew through that allowance
  quickly (1,000 requests/hour) given that we run two of these actions per
  workflow run.
  
  `token` defaults to the workflow's token, but by setting it explicitly
  to an empty string, the action will instead use `git diff` to determine
  the modified paths. This works fine for our case because we're already
  running the checkout action, so we have an up-to-date repository view.
  
  This also has the advantage of working around the 300 files GitHub REST
  API limit for listing changed files.
  
  Ref: https://github.com/dorny/paths-filter
  ```
- [`69e0673`](https://github.com/ghostty-org/ghostty/commit/69e0673478b4e92d1a5f0a1e1c41091218f853af) ci: use local git commands for path-filter action ([#11652](https://github.com/ghostty-org/ghostty/issues/11652)) ([@jcollie](https://github.com/jcollie))
  ```text
  Passing a `token` value causes this action to use the GitHub REST API,
  which is subject to rate limits. We can chew through that allowance
  quickly (1,000 requests/hour) given that we run two of these actions per
  workflow run.
  
  `token` defaults to the workflow's token, but by setting it explicitly
  to an empty string, the action will instead use `git diff` to determine
  the modified paths. This works fine for our case because we're already
  running the checkout action, so we have an up-to-date repository view.
  
  This also has the advantage of working around the 300 files GitHub REST
  API limit for listing changed files.
  
  Ref: https://github.com/dorny/paths-filter
  ```

## March 18, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23257063138), [2](https://github.com/ghostty-org/ghostty/actions/runs/23255200023), [3](https://github.com/ghostty-org/ghostty/actions/runs/23253545237), [4](https://github.com/ghostty-org/ghostty/actions/runs/23248995028), [5](https://github.com/ghostty-org/ghostty/actions/runs/23222237491)  
Summary: 5 runs • 17 commits • 5 authors

### Changes

- [`2d51401`](https://github.com/ghostty-org/ghostty/commit/2d514013d51e9805305b5e93c5bd9eb9ada774a4) fix "open terminal here" action on Plasma ([@heddxh](https://github.com/heddxh))
- [`4b1e48b`](https://github.com/ghostty-org/ghostty/commit/4b1e48b71e7e7b0317651a8c3173defff9ffffaa) swap arguments ([@heddxh](https://github.com/heddxh))
- [`c9e1006`](https://github.com/ghostty-org/ghostty/commit/c9e1006213eb9234209924c91285d6863e59ce4c) Fix: correct "Open Ghostty Here" Dolphin action for Plasma ([#11614](https://github.com/ghostty-org/ghostty/issues/11614)) ([@jcollie](https://github.com/jcollie))
  ```text
  See #11594
  
  The change allows "Open Ghostty Here" Dolphin action to launch new
  ghostty window with gtk single instance.
  ```
- [`1f3a3b4`](https://github.com/ghostty-org/ghostty/commit/1f3a3b41f785d10906678394d13c180657d35210) bash: handle PROMPT_COMMAND ending in a newline ([@jparise](https://github.com/jparise))
  ```text
  We need to handle on more case: when an existing PROMPT_COMMAND ends in
  a newline, we don't want to append a ; because that already counts as a
  command separator.
  
  We now handle all of these PROMPT_COMMAND cases:
  
  - Ends with ; — no ; added
  - Ends with \n or other whitespace — no ; added
  - Ends with a command name — ; added as separator
  
  See: #11245
  ```
- [`3dc6998`](https://github.com/ghostty-org/ghostty/commit/3dc69981d2abf7e66eeb973229b86c6bb847c734) bash: handle PROMPT_COMMAND ending in a newline ([#11621](https://github.com/ghostty-org/ghostty/issues/11621)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  We need to handle on more case: when an existing PROMPT_COMMAND ends in
  a newline, we don't want to append a ; because that already counts as a
  command separator.
  
  We now handle all of these PROMPT_COMMAND cases:
  
  - Ends with ; — no ; added
  - Ends with \n or other whitespace — no ; added
  - Ends with a command name — ; added as separator
  
  See: #11245
  ```
- [`e01046a`](https://github.com/ghostty-org/ghostty/commit/e01046af158cef2e324ae153e73381d544ed3cc6) docs: extract focus encoding example into standalone project ([@mitchellh](https://github.com/mitchellh))
  ```text
  Extract the inline code example from focus.h into a standalone
  buildable example at example/c-vt-encode-focus. The header now
  uses a Doxygen @snippet tag to include the code from the example
  source file, so the documentation stays in sync with code that
  is verified to compile and run.
  ```
- [`bb3b3ba`](https://github.com/ghostty-org/ghostty/commit/bb3b3ba6150b55c251e05fd205a1da5b8c34ec5f) ci: dynamically discover example directories for build-examples ([@mitchellh](https://github.com/mitchellh))
  ```text
  Replace the hardcoded matrix list in the build-examples job with a
  dynamic list-examples job that discovers all subdirectories under
  example/ at runtime. This uses ls/jq to produce a JSON array and
  fromJSON() to feed it into the matrix, so new examples are picked
  up automatically without updating the workflow.
  ```
- [`15b8976`](https://github.com/ghostty-org/ghostty/commit/15b8976d643de69df2168aa99320557e6b95bc02) docs: extract inline code examples into standalone projects ([@mitchellh](https://github.com/mitchellh))
  ```text
  Extract inline @code blocks from vt headers (size_report.h, modes.h,
  sgr.h, paste.h, mouse.h, key.h) into standalone buildable examples
  under example/. Each header now uses Doxygen @snippet tags to include
  code from the example source files, keeping documentation in sync
  with code that is verified to compile and run.
  
  New example projects: c-vt-size-report and c-vt-modes. Existing
  examples (c-vt-sgr, c-vt-paste, c-vt-mouse-encode, c-vt-key-encode)
  gain snippet markers so their code can be referenced from the headers.
  Conceptual snippets in key.h, mouse.h, and key/encoder.h that show
  terminal-state usage patterns remain inline since they cannot be
  compiled standalone.
  ```
- [`ceef806`](https://github.com/ghostty-org/ghostty/commit/ceef8065b02a8cf007e7a6ed3f6e71965fa20ad6) ci: filter build-examples to directories with build.zig.zon ([@mitchellh](https://github.com/mitchellh))
  ```text
  The dynamic example directory discovery added in bb3b3ba included
  all subdirectories under example/, but some (wasm-key-encode,
  wasm-sgr) are pure HTML examples with no build.zig.zon. Running
  zig build in those directories falls back to the root build.zig
  and attempts a full GTK binary build, which fails on CI.
  
  Filter the listing to only include directories that contain a
  build.zig.zon file so non-Zig examples are excluded from the
  build matrix.
  ```
- [`f037f41`](https://github.com/ghostty-org/ghostty/commit/f037f41f78fd96a98b4f612f40e117f80af6ca31) Add example AGENTS file ([@mitchellh](https://github.com/mitchellh))
- [`383a7e1`](https://github.com/ghostty-org/ghostty/commit/383a7e14a7e4043dbfbd45aaa19781bba442952b) example: add README ([@mitchellh](https://github.com/mitchellh))
- [`996ce03`](https://github.com/ghostty-org/ghostty/commit/996ce03f0b9e9407c0164e4a3c4f341ed91cc817) example: rename some examples ([@mitchellh](https://github.com/mitchellh))
- [`9e6c875`](https://github.com/ghostty-org/ghostty/commit/9e6c875f334c43f1b1ea4cb8d23c1ec07c6d9f9c) Ensure all examples in libghostty C docs build and run in CI ([#11609](https://github.com/ghostty-org/ghostty/issues/11609)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This moves all our examples away from embedded source to `@snippet` and
  files so that we can use our CI to actually run the builds and keep them
  working.
  
  Note: I used AI to extract the examples, and it did some weird merging
  stuff. It all works but I want to make sure all these examples are still
  human friendly so I need to go back and review all that. I clicked
  through the web docs and they look good, just need to verify the GitHub
  flow.
  ```
- [`a74f437`](https://github.com/ghostty-org/ghostty/commit/a74f43760edce5a4b51d73c44cc39066cb24539e) Update VOUCHED list ([#11623](https://github.com/ghostty-org/ghostty/issues/11623)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11622#issuecomment-4082875090)
  from @00-kat.
  
  Vouch: @EkaterinePapava
  ```
- [`a1d7ad9`](https://github.com/ghostty-org/ghostty/commit/a1d7ad92434a6c1c5b5a2b436a15e0573790b6cc) terminal: extract size report encoder ([@mitchellh](https://github.com/mitchellh))
  ```text
  Size report escape sequences were previously formatted inline in
  Termio.sizeReportLocked, and termio.Message carried a duplicate enum for
  report styles. That made the encoding logic harder to reuse and kept
  the style type scoped to termio.
  
  Move the encoding into terminal.size_report and export it through
  terminal.main. The encoder now takes renderer.Size directly and derives
  grid and pixel dimensions from one source of truth. termio.Message now
  aliases terminal.size_report.Style, and Termio writes reports via the
  shared encoder.
  ```
- [`7bf8974`](https://github.com/ghostty-org/ghostty/commit/7bf89740dd86c28f40c2d5ab9cd001cbf41b864a) vt: expose size_report encoding in the C API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add ghostty_size_report_encode() to libghostty-vt, following the
  same pattern as focus encoding: a single stateless function that
  writes a terminal size report escape sequence into a caller-provided
  buffer.
  
  The size_report.zig Style enum and Size struct now use lib.Enum and
  lib.Struct so the types are automatically C-compatible when building
  with c_abi, eliminating the need for duplicate type definitions in
  the C wrapper. The C wrapper in c/size_report.zig re-exports these
  types directly and provides the callconv(.c) encode entry point.
  
  Supports mode 2048 in-band reports and XTWINOPS responses (CSI 14 t,
  CSI 16 t, CSI 18 t).
  ```
- [`d3bd224`](https://github.com/ghostty-org/ghostty/commit/d3bd224081d3c7c5ee54df6815e44f0b5d25357b) terminal/vt: extract size report encoding to its own file ([#11607](https://github.com/ghostty-org/ghostty/issues/11607)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Extract size report encoding into a reusable module and expose it
  through the libghostty-vt C API as `ghostty_size_report_encode()`.
  
  Size report escape sequences (mode 2048 in-band reports, XTWINOPS CSI
  14/16/18 t responses) were formatted inline in
  `Termio.sizeReportLocked`, and `termio.Message` carried its own
  duplicate enum for report styles. This made the encoding logic
  impossible to reuse from the C library and kept the style type
  unnecessarily scoped to termio.
  
  ## Example
  
  ```c
  GhosttySizeReportSize size = {
      .rows = 24, .columns = 80,
      .cell_width = 9, .cell_height = 18,
  };
  
  char buf[64];
  size_t written = 0;
  ghostty_size_report_encode(
      GHOSTTY_SIZE_REPORT_MODE_2048, size,
      buf, sizeof(buf), &written);
  // buf contains: "\x1b[48;24;80;432;720t"
  ```
  ````

