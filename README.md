> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: March 25, 2026 at 03:49 UTC.

## March 24, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23513636307), [2](https://github.com/ghostty-org/ghostty/actions/runs/23512601381), [3](https://github.com/ghostty-org/ghostty/actions/runs/23510832036), [4](https://github.com/ghostty-org/ghostty/actions/runs/23503946207), [5](https://github.com/ghostty-org/ghostty/actions/runs/23492778008), [6](https://github.com/ghostty-org/ghostty/actions/runs/23472855296), [7](https://github.com/ghostty-org/ghostty/actions/runs/23469421167), [8](https://github.com/ghostty-org/ghostty/actions/runs/23468473879)  
Summary: 8 runs • 46 commits • 5 authors

### Changes

- [`c12f62c`](https://github.com/ghostty-org/ghostty/commit/c12f62c82d62f36c850a1e06221d84719948b2a4) vt: handle pixel sizes and size reports in ghostty_terminal_resize ([@mitchellh](https://github.com/mitchellh))
  ```text
  The resize function now requires cell_width_px and cell_height_px
  parameters and handles the full resize sequence: computing and
  setting width_px/height_px on the terminal, clearing synchronized output mode
  so changes display immediately, and encoding a mode 2048 in-band size report
  via the write_pty callback when that mode is enabled.
  
  A valid width/height px is critical for some applications and protocols
  and some applications rely directly on in-band size reports, so this
  change is necessary to support those use cases.
  ```
- [`bebca84`](https://github.com/ghostty-org/ghostty/commit/bebca84668947bfc92b9a30ed58712e1c34eee1d) vt: handle pixel sizes and size reports in ghostty_terminal_resize ([#11818](https://github.com/ghostty-org/ghostty/issues/11818)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The resize function now requires cell_width_px and cell_height_px
  parameters and handles the full resize sequence: computing and setting
  width_px/height_px on the terminal, clearing synchronized output mode so
  changes display immediately, and encoding a mode 2048 in-band size
  report via the write_pty callback when that mode is enabled.
  
  A valid width/height px is critical for some applications and protocols
  and some applications rely directly on in-band size reports, so this
  change is necessary to support those use cases.
  
  I do wonder if for the Zig API we should be doing this in
  `terminal.resize` or somewhere else, because as it stands this has to
  all be manually done on the Zig side.
  ```
- [`6e34bc6`](https://github.com/ghostty-org/ghostty/commit/6e34bc686cbfd86c69418fffd9805d68c197b9a7) vt: pass pointer options directly to terminal_set ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously ghostty_terminal_set required all values to be passed as
  pointers to the value, even when the value itself was already a
  pointer (userdata, function pointer callbacks). This forced callers
  into awkward patterns like compound literals or intermediate
  variables just to take the address of a pointer.
  
  Now pointer-typed options (userdata and all callbacks) are passed
  directly as the value parameter. Only non-pointer types like
  GhosttyString still require a pointer to the value. This
  simplifies InType to return the actual stored type for each option
  and lets setTyped work with those types directly.
  ```
- [`a062c16`](https://github.com/ghostty-org/ghostty/commit/a062c16e13f389bae01f0e654fddf4a133748856) libghostty: pass pointer options directly to terminal_set ([#11816](https://github.com/ghostty-org/ghostty/issues/11816)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously ghostty_terminal_set required all values to be passed as
  pointers to the value, even when the value itself was already a pointer
  (userdata, function pointer callbacks). This forced callers into awkward
  patterns like compound literals or intermediate variables just to take
  the address of a pointer.
  
  Now pointer-typed options (userdata and all callbacks) are passed
  directly as the value parameter. Only non-pointer types like
  GhosttyString still require a pointer to the value. This simplifies
  InType to return the actual stored type for each option and lets
  setTyped work with those types directly.
  ```
- [`2c16c9e`](https://github.com/ghostty-org/ghostty/commit/2c16c9e40c8862342ea02a9f3ffae2a52c3735e3) vt: add total_rows and scrollback_rows to terminal get API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add total_rows and scrollback_rows as new TerminalData variants
  queryable through the existing ghostty_terminal_get interface,
  using the cached O(1) total_rows field from PageList rather than
  introducing standalone functions.
  ```
- [`f452087`](https://github.com/ghostty-org/ghostty/commit/f452087eacde1efcbf1d845a02ccd23e73a0492e) vt: add total_rows and scrollback_rows to terminal get API ([#11817](https://github.com/ghostty-org/ghostty/issues/11817)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add total_rows and scrollback_rows as new TerminalData variants
  queryable through the existing ghostty_terminal_get interface, using the
  cached O(1) total_rows field from PageList rather than introducing
  standalone functions.
  ```
- [`68378a0`](https://github.com/ghostty-org/ghostty/commit/68378a0bb8a6e84e568838bfe5b1f92941c2ef50) build: increase comptime branch quota for ghostty.h enum checks ([@deblasis](https://github.com/deblasis))
  ```text
  The MSVC translate-c output includes Windows SDK declarations,
  bringing the total to ~2173 declarations (vs ~1502 on Linux/Mac).
  The nested inline for in checkGhosttyHEnum (enum fields x declarations)
  exceeds the 1M comptime branch quota for larger enums like MouseShape
  (34 variants). Increase to 10M to accommodate.
  ```
- [`b91cc86`](https://github.com/ghostty-org/ghostty/commit/b91cc867a815f1d26bd5b34d17b70b64abff88d1) vt: add ghostty_terminal_set for configuring effects callbacks ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a typed option setter ghostty_terminal_set() following the
  existing setopt pattern used by the key encoder and render state
  APIs. This is the first step toward exposing stream_terminal
  Handler.Effects through the C API.
  
  The initial implementation includes a write_pty callback and a
  shared userdata pointer. The write_pty callback is invoked
  synchronously during ghostty_terminal_vt_write() when the terminal
  needs to send a response back to the pty, such as DECRQM mode
  reports or device status responses.
  
  Trampolines are always installed at terminal creation time and
  no-op when no C callback is set, so callers can configure
  callbacks at any point without reinitializing the stream. The C
  callback state is grouped into an internal Effects struct on the
  TerminalWrapper to simplify adding more callbacks in the future.
  ```
- [`b49e9f3`](https://github.com/ghostty-org/ghostty/commit/b49e9f37ff71cc007dafa592c5d7385d70a2dab1) vt: add bell effect callback and move types into Effects ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add GHOSTTY_TERMINAL_OPT_BELL so C consumers can receive bell
  notifications during VT processing. The bell trampoline follows
  the same pattern as write_pty.
  
  Move the C function pointer typedefs (WritePtyFn, BellFn) into
  the Effects struct namespace to keep callback types co-located
  with their storage and trampolines.
  ```
- [`c13a9bb`](https://github.com/ghostty-org/ghostty/commit/c13a9bb49ced768d7da3f6aff2e6d31fbed4641e) vt: add tests for write_pty and bell effect callbacks ([@mitchellh](https://github.com/mitchellh))
  ```text
  Test that the write_pty callback receives correct DECRQM response
  data and userdata, that queries are silently ignored without a
  callback, and that setting null clears the callback. Test that
  the bell callback fires on single and multiple BEL characters
  with correct userdata, and that BEL without a callback is safe.
  ```
- [`f9c34b4`](https://github.com/ghostty-org/ghostty/commit/f9c34b40f067cb40d63ce78aac00ead3ec77fabb) vt: add enquiry and xtversion effect callbacks ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add GHOSTTY_TERMINAL_OPT_ENQUIRY and GHOSTTY_TERMINAL_OPT_XTVERSION
  so C consumers can respond to ENQ (0x05) and XTVERSION (CSI > q)
  queries. Both callbacks return a GhosttyString rather than using
  out-pointers.
  
  Introduce GhosttyString in types.h as a borrowed byte string
  (ptr + len) backed by lib.String on the Zig side. This will be
  reusable for future callbacks that need to return string data.
  
  Without an xtversion callback the trampoline returns an empty
  string, which causes the handler to report the default
  "libghostty" version. Without an enquiry callback no response
  is sent.
  ```
- [`6f18d44`](https://github.com/ghostty-org/ghostty/commit/6f18d44ed69a5194a74ab72b6d86aaaf545f1dd6) vt: add title_changed effect callback ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add GHOSTTY_TERMINAL_OPT_TITLE_CHANGED so C consumers are notified
  when the terminal title changes via OSC 0 or OSC 2 sequences. The
  callback has the same fire-and-forget shape as bell.
  ```
- [`424e9b5`](https://github.com/ghostty-org/ghostty/commit/424e9b57cabb1e6040167df561e03335cb2714df) vt: add size effect callback for XTWINOPS queries ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add GHOSTTY_TERMINAL_OPT_SIZE so C consumers can respond to
  XTWINOPS size queries (CSI 14/16/18 t). The callback receives a
  GhosttySizeReportSize out-pointer and returns true if the size is
  available, or false to silently ignore the query. The trampoline
  converts the bool + out-pointer pattern to the optional that the
  Zig handler expects.
  ```
- [`02d48c3`](https://github.com/ghostty-org/ghostty/commit/02d48c360b5c9e837844bac4ad3fdf6c8fa69b5c) vt: expose color_scheme effect callback ([@mitchellh](https://github.com/mitchellh))
  ```text
  Change device_status.ColorScheme from a plain Zig enum to
  lib.Enum so it uses c_int backing when targeting the C ABI.
  
  Add a color_scheme callback to the C terminal effects, following
  the bool + out-pointer pattern used by the size callback. The
  trampoline converts between the C calling convention and the
  internal stream handler color_scheme effect, returning null when
  no callback is set.
  
  Add device_status.h header with GhosttyColorScheme enum and wire
  it through terminal.h as GHOSTTY_TERMINAL_OPT_COLOR_SCHEME (= 7)
  with GhosttyTerminalColorSchemeFn.
  ```
- [`b8fcb57`](https://github.com/ghostty-org/ghostty/commit/b8fcb57923ae3a5d39630650a05217f3536c87f8) vt: expose device_attributes effect in the C API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Rename device_status.h to device.h and add C-compatible structs for
  device attributes (DA1/DA2/DA3) responses. The new header includes
  defines for all known conformance levels, DA1 feature codes, and DA2
  device type identifiers.
  
  Add a GhosttyTerminalDeviceAttributesFn callback that C consumers can
  set via GHOSTTY_TERMINAL_OPT_DEVICE_ATTRIBUTES. The callback follows
  the existing bool + out-pointer pattern used by color_scheme and size
  callbacks. When the callback is unset or returns false, the trampoline
  returns a default VT220 response (conformance level 62, ANSI color).
  
  The DA1 primary features use a fixed [64]uint16_t inline array with a
  num_features count rather than a pointer, so the entire struct is
  value-typed and can be safely copied without lifetime concerns.
  ```
- [`bbfe1c2`](https://github.com/ghostty-org/ghostty/commit/bbfe1c278722c54ededd474b9567b58fd3ad801a) vt: use struct literal for handler effects assignment ([@mitchellh](https://github.com/mitchellh))
  ```text
  Assign handler.effects as a struct literal instead of setting fields
  individually. This lets the compiler catch missing fields if new
  effects are added to the Effects struct.
  
  Also sort the callback function typedefs in vt/terminal.h
  alphabetically (Bell, ColorScheme, DeviceAttributes, Enquiry, Size,
  TitleChanged, WritePty, Xtversion).
  ```
- [`4128e6a`](https://github.com/ghostty-org/ghostty/commit/4128e6a38c5c5c20d5119a46c691bf978b74c41a) vt: add effects documentation section with example ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a comprehensive "Effects" section to the terminal module
  documentation in terminal.h explaining the callback system that
  lets embedding applications react to terminal-initiated events
  (bell, title changes, pty writes, device queries, etc.). The
  section includes a reference table of all available effects and
  their triggers, plus @snippet references to the new example.
  
  Add c-vt-effects example project demonstrating how to register
  write_pty, bell, and title_changed callbacks, attach userdata,
  and feed VT data that triggers each effect.
  ```
- [`e36b745`](https://github.com/ghostty-org/ghostty/commit/e36b7453146099b3473b4d8a5c6638f6431448c4) fmt ([@mitchellh](https://github.com/mitchellh))
- [`d2c6a3c`](https://github.com/ghostty-org/ghostty/commit/d2c6a3c775bc6952480442fe11ec2984a86b5c8c) vt: store DA1 feature buffer in wrapper struct ([@mitchellh](https://github.com/mitchellh))
  ```text
  The DA1 trampoline was converting C feature codes into a local
  stack buffer and returning a slice pointing into it. This is
  unsound because the slice outlives the stack frame once the
  trampoline returns, leaving reportDeviceAttributes reading
  invalid memory.
  
  Move the scratch buffer into the wrapper effects struct so that
  its lifetime extends beyond the trampoline call, keeping the
  returned slice valid for the caller.
  ```
- [`81e21e4`](https://github.com/ghostty-org/ghostty/commit/81e21e4d0a4e6f3a12004542a907c55c2f3b587a) build: refactor checkGhosttyHEnum to use @hasDecl instead of nested inline for ([@deblasis](https://github.com/deblasis))
  ```text
  Replace the O(N×M) nested inline for loop with direct @hasDecl lookups.
  The old approach iterated over all translate-c declarations for each enum
  field, which required a 10M comptime branch quota on MSVC (2173 decls ×
  138 fields × ~20 branches). The new approach constructs the expected
  declaration name and checks directly, reducing to O(N) and needing only
  100K quota on all platforms.
  ```
- [`d5bd331`](https://github.com/ghostty-org/ghostty/commit/d5bd331c91b9cf988f805f0f71ecc74a287d04cb) libghostty: C API for terminal "effects" for processing output and side effects ([#11814](https://github.com/ghostty-org/ghostty/issues/11814)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This adds the terminal effects callback system to the libghostty-vt C
  API.
  
  Previously, `ghostty_terminal_vt_write()` silently ignored VT sequences
  that produce side effects or require responses (bell, title changes,
  device status queries, etc.). With this change, embedders can register
  callbacks via `ghostty_terminal_set()` to handle these sequences.
  
  This has already existed in the Zig API.
  
  ## Effects
  
  | Option | Callback Type | Trigger |
  |--------|--------------|---------|
  | `GHOSTTY_TERMINAL_OPT_WRITE_PTY` | `GhosttyTerminalWritePtyFn` | Query
  responses written back to the pty |
  | `GHOSTTY_TERMINAL_OPT_BELL` | `GhosttyTerminalBellFn` | BEL character
  (0x07) |
  | `GHOSTTY_TERMINAL_OPT_TITLE_CHANGED` | `GhosttyTerminalTitleChangedFn`
  | Title change via OSC 0 / OSC 2 |
  | `GHOSTTY_TERMINAL_OPT_ENQUIRY` | `GhosttyTerminalEnquiryFn` | ENQ
  character (0x05) |
  | `GHOSTTY_TERMINAL_OPT_XTVERSION` | `GhosttyTerminalXtversionFn` |
  XTVERSION query (CSI > q) |
  | `GHOSTTY_TERMINAL_OPT_SIZE` | `GhosttyTerminalSizeFn` | XTWINOPS size
  query (CSI 14/16/18 t) |
  | `GHOSTTY_TERMINAL_OPT_COLOR_SCHEME` | `GhosttyTerminalColorSchemeFn` |
  Color scheme query (CSI ? 996 n) |
  | `GHOSTTY_TERMINAL_OPT_DEVICE_ATTRIBUTES` |
  `GhosttyTerminalDeviceAttributesFn` | Device attributes query (CSI c / >
  c / = c) |
  
  ## Example
  
  ```c
  #include <stdio.h>
  #include <string.h>
  #include <ghostty/vt.h>
  
  void on_write_pty(GhosttyTerminal terminal, void* userdata,
                    const uint8_t* data, size_t len) {
    (void)terminal; (void)userdata;
    printf("  write_pty (%zu bytes): ", len);
    fwrite(data, 1, len, stdout);
    printf("\n");
  }
  
  void on_bell(GhosttyTerminal terminal, void* userdata) {
    (void)terminal;
    int* count = (int*)userdata;
    (*count)++;
    printf("  bell! (count=%d)\n", *count);
  }
  
  int main() {
    GhosttyTerminal terminal = NULL;
    GhosttyTerminalOptions opts = { .cols = 80, .rows = 24, .max_scrollback = 0 };
    if (ghostty_terminal_new(NULL, &terminal, opts) != GHOSTTY_SUCCESS)
      return 1;
  
    // Attach userdata and callbacks
    int bell_count = 0;
    void* ud = &bell_count;
    ghostty_terminal_set(terminal, GHOSTTY_TERMINAL_OPT_USERDATA, &ud);
  
    GhosttyTerminalWritePtyFn write_fn = on_write_pty;
    ghostty_terminal_set(terminal, GHOSTTY_TERMINAL_OPT_WRITE_PTY, &write_fn);
  
    GhosttyTerminalBellFn bell_fn = on_bell;
    ghostty_terminal_set(terminal, GHOSTTY_TERMINAL_OPT_BELL, &bell_fn);
  
    // BEL triggers the bell callback
    const uint8_t bel = 0x07;
    ghostty_terminal_vt_write(terminal, &bel, 1);
  
    // DECRQM triggers write_pty with the mode response
    const char* decrqm = "\x1B[?7$p";
    ghostty_terminal_vt_write(terminal, (const uint8_t*)decrqm, strlen(decrqm));
  
    ghostty_terminal_free(terminal);
    return 0;
  }
  ```
  ````
- [`f21455b`](https://github.com/ghostty-org/ghostty/commit/f21455b7e7f1a765a93ce86530723667a4926535) build: refactor checkGhosttyHEnum to use @hasDecl for Windows compatibility ([#11813](https://github.com/ghostty-org/ghostty/issues/11813)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ### This is it! This one (and the other stacked PRs) and #11782 should
  finally give a clean test run on Windows!
  
  
  ## Summary
  
  - Increase `@setEvalBranchQuota` from 1M to 10M (too much? how much is
  too much?) in `checkGhosttyHEnum` (src/lib/enum.zig)
  - Fixes the only remaining test failure on Windows MSVC: `ghostty.h
  MouseShape`
  
  ## Context
  This one was fun! Claude started blabbering, diminishing returns it
  said. It couldn't figure out. So I called Dario and it worked.
  Nah, much easier than that.
  
  On MSVC, the translate-c output for `ghostty.h` is ~360KB with ~2173
  declarations (vs ~112KB / ~1502 on Linux/Mac) because `<sys/types.h>`
  and `<BaseTsd.h>` pull in Windows SDK headers. The `checkGhosttyHEnum`
  function uses a nested `inline for` (enum fields x declarations) with
  comptime string comparisons. For MouseShape (34 variants), this
  generates roughly 34 x 2173 x ~20 = ~1.5M comptime branches, exceeding
  the 1M quota.
  
  The failure was confusing because it presented as a runtime error
  ("ghostty.h is missing value for GHOSTTY_MOUSE_SHAPE_DEFAULT") rather
  than a compile error. The constants exist in the translate-c output and
  the test compiles, but the comptime loop silently stops matching when it
  hits the branch limit, so `set.remove` is never called and the set
  reports all entries as missing at runtime.
  
  ## How we found it
  The translate-c output clearly had all 34 GHOSTTY_MOUSE_SHAPE_*
  constants, yet the test reported all of them as missing. I asked Claude
  to list 5 hypotheses (decl truncation, branch quota, string comparison
  bug, declaration ordering, field access failure) and to write 7 targeted
  POC tests in enum.zig to isolate each step of `checkGhosttyHEnum`:
  
  1. POC1-2: Module access and declaration count (both passed)
  2. POC3: `@hasDecl` for the constant (passed)
  3. POC4: Direct field value access (passed)
  4. POC5: `inline for` over decls with string comparison - **compile
  error: "evaluation exceeded 1000 backwards branches"**
  5. POC6: Same but with 10M quota (passed)
  6. POC7: Full `checkGhosttyHEnum` clone with 10M quota - **passed,
  confirming the fix**
  
  POC5 was the key: the default 1000 branch limit for test code confirmed
  the comptime budget mechanism. The existing 1M quota in
  `checkGhosttyHEnum` was enough for Linux/Mac (1502 declarations) but not
  for MSVC (2173 declarations) with larger enums.
  
  ## Stack
  Stacked on 016-windows/fix-libcxx-msvc.
  
  ## Test plan
  
  ### Cross-platform results (`zig build test` / `zig build
  -Dapp-runtime=none test` on Windows)
  
  | | Windows | Linux | Mac |
  |---|---|---|---|
  | **BEFORE** (016, ce9930051) | FAIL - 49/51, 2630/2654, 1 test failed,
  23 skipped | PASS - 86/86, 2655/2678, 23 skipped | PASS - 160/160,
  2655/2662, 7 skipped |
  | **AFTER** (017, 68378a0bb) | FAIL - 49/51, 2631/2654, 23 skipped |
  PASS - 86/86, 2655/2678, 23 skipped | PASS - 160/160, 2655/2662, 7
  skipped |
  
  ### Windows: what changed (2630 -> 2631 tests, MouseShape fixed)
  
  **Fixed by this PR:**
  - `ghostty.h MouseShape` test - was failing because comptime branch
  quota exhaustion silently prevented the inline for loop from matching
  any constants
  
  **Remaining failure (pre-existing, unrelated):**
  - `config.Config.test.clone can then change conditional state` -
  segfaults (exit code 3) on Windows. We investigated this and it looked
  familiar.. cherry-picking the `CommaSplitter `fix from PR #11782
  resolved it! The backslash path handling in `CommaSplitter `breaks theme
  path parsing on Windows, which is exactly what that PR addresses. So
  once that lands, we should be in a good place... ready to ship to
  Windows users! (just kidding)
  
  ### Linux/macOS: no regressions
  Identical pass counts and test results before and after.
  
  ## What I Learnt
  - Comptime branch quota exhaustion in Zig does not always surface as a
  clean compile error. When it happens inside an `inline for` loop with
  `comptime` string comparisons that gate runtime code (like
  `set.remove`), the effect is that matching code is silently not
  generated. The test compiles and runs, but the runtime behavior is wrong
  because the matching branches were never emitted. This makes the failure
  look like a data issue (missing declarations) rather than a compile
  budget issue.
  - When debugging comptime issues, writing small isolated POC tests that
  exercise each step of the failing function independently is very
  effective. It took 7 targeted tests to pinpoint the exact failure point.
  - Cross-platform translate-c outputs can vary significantly in size. On
  MSVC, system headers are much larger than on Linux/Mac, which affects
  comptime budgets for any code that iterates over translated module
  declarations.
  ```
- [`8f1ac0b`](https://github.com/ghostty-org/ghostty/commit/8f1ac0bd4e69e922167d4cf7560a6cdec12ba721) vt: expose title and pwd in C API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add title and pwd as both gettable data keys
  (GHOSTTY_TERMINAL_DATA_TITLE/PWD) and settable options
  (GHOSTTY_TERMINAL_OPT_TITLE/PWD) in the C terminal API. Getting
  returns a borrowed GhosttyString; setting copies the data into the
  terminal via setTitle/setPwd.
  
  The underlying Terminal.setTitle/setPwd now append a null sentinel so
  that getTitle/getPwd can return sentinel-terminated slices ([:0]const
  u8), which is useful for downstream consumers that need C strings.
  
  Change ghostty_terminal_set to return GhosttyResult instead of void
  so that the new title/pwd options can report allocation failures.
  Existing option-setting calls cannot fail so the return value is
  backwards-compatible for callers that discard it.
  ```
- [`82f7527`](https://github.com/ghostty-org/ghostty/commit/82f7527b302a655ed03be0f6f1f0d46f5aaadcb0) vt: expose title and pwd in C API ([#11815](https://github.com/ghostty-org/ghostty/issues/11815)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add title and pwd as both gettable data keys
  (GHOSTTY_TERMINAL_DATA_TITLE/PWD) and settable options
  (GHOSTTY_TERMINAL_OPT_TITLE/PWD) in the C terminal API. Getting returns
  a borrowed GhosttyString; setting copies the data into the terminal via
  setTitle/setPwd.
  
  The underlying Terminal.setTitle/setPwd now append a null sentinel so
  that getTitle/getPwd can return sentinel-terminated slices ([:0]const
  u8), which is useful for downstream consumers that need C strings.
  
  Change ghostty_terminal_set to return GhosttyResult instead of void so
  that the new title/pwd options can report allocation failures. Existing
  option-setting calls cannot fail so the return value is
  backwards-compatible for callers that discard it.
  ```
- [`d5aef6e`](https://github.com/ghostty-org/ghostty/commit/d5aef6e845ed72584aba3a129268d40a9694b568) build: fix freetype compilation on Windows with MSVC ([@deblasis](https://github.com/deblasis))
  ```text
  Gate HAVE_UNISTD_H and HAVE_FCNTL_H behind a non-Windows check since
  these headers do not exist with MSVC. Freetype includes zlib headers
  which conditionally include unistd.h based on this define.
  ```
- [`a35f84d`](https://github.com/ghostty-org/ghostty/commit/a35f84db32e88b93bcff19317365ee93f75839d1) build: define ssize_t for MSVC in ghostty.h ([@deblasis](https://github.com/deblasis))
  ```text
  MSVC's <sys/types.h> does not define ssize_t (it is a POSIX type).
  This causes the translate-c build step to fail when translating
  ghostty.h on Windows. Use SSIZE_T from <BaseTsd.h> which is the
  Windows SDK equivalent.
  ```
- [`deeda46`](https://github.com/ghostty-org/ghostty/commit/deeda4618691525e977886135aa4ff18b7f81caa) build: skip linkLibCpp on MSVC for dcimgui, spirv-cross, harfbuzz ([@deblasis](https://github.com/deblasis))
  ```text
  Zig unconditionally passes -nostdinc++ and adds its bundled
  libc++/libc++abi include paths, which conflict with MSVC's own C++
  runtime headers. The MSVC SDK directories (added via linkLibC)
  already contain both C and C++ headers, so linkLibCpp is not needed.
  
  This is the same fix already applied upstream to highway, simdutf,
  utfcpp, glslang, SharedDeps, and GhosttyZig.
  ```
- [`ce99300`](https://github.com/ghostty-org/ghostty/commit/ce99300513dff19fade309ca4881fc45517424f7) build: fix freetype C enum signedness for MSVC ([@deblasis](https://github.com/deblasis))
  ```text
  MSVC translates C enums as signed int, while GCC/Clang uses unsigned
  int. The freetype Zig bindings hardcode c_uint for enum backing types,
  causing type mismatches when compiling with MSVC target.
  
  Fix by adding @intCast at call sites where enum values are passed to
  C functions, and @bitCast for the glyph format tag extraction where
  bit-shift operations require unsigned integers.
  ```
- [`d14eab3`](https://github.com/ghostty-org/ghostty/commit/d14eab3124bc8ff9f3ca25b2a2bafeecf20a9133) build: fix freetype compilation on Windows with MSVC ([#11807](https://github.com/ghostty-org/ghostty/issues/11807)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Summary
  
  **Getting there!** Goal for today/tomorrow is to get it all green.
  
  This one is easy:
  
  - Gate `HAVE_UNISTD_H` and `HAVE_FCNTL_H` behind a non-Windows check
  since these headers do not exist with MSVC
  - Freetype's gzip module includes zlib headers which conditionally
  include `unistd.h` based on this define
  
  ## Context
  Same pattern as the zlib fix (010-* branch from my fork). Freetype
  passes `-DHAVE_UNISTD_H` unconditionally, which causes zlib's `zconf.h`
  to try including `unistd.h` when freetype compiles its gzip support. The
  fix follows the same approach used in `pkg/zlib/build.zig` (line 36-38).
  
  ## Stack
  Stacked on 013-windows/fix-helpgen-framegen.
  
  ## Test plan
  
  ### Cross-platform results (`zig build test` / `zig build
  -Dapp-runtime=none test` on Windows)
  
  | | Windows | Linux | Mac |
  |---|---|---|---|
  | **BEFORE** (f9d3b1aaf) | FAIL - 44/51 steps, 2 failed | PASS - 86/86,
  2655/2678 tests, 23 skipped | PASS - 160/160, 2655/2662 tests, 7 skipped
  |
  | **AFTER** (d5aef6e84) | FAIL - 47/51 steps, 1 failed | PASS - 86/86,
  2655/2678 tests, 23 skipped | PASS - 160/160, 2655/2662 tests, 7 skipped
  |
  
  ### Windows: what changed (44 to 47 steps, 2 to 1 failure)
  
  **Fixed by this PR:**
  - `compile lib freetype` - was `2 errors` (unistd.h/fcntl.h not found)
  -> `success`
  - 3 additional steps that depended on freetype now succeed
  
  **Remaining failure (pre-existing, tracked separately):**
  - `translate-c` - 3 errors (`ssize_t` unknown in ghostty.h on MSVC)
  
  ### Linux/macOS: no regressions
  Identical pass counts and test results before and after.
  
  ## Discussion
  
  ### Other build files with the same pattern
  `pkg/fontconfig/build.zig` and `pkg/harfbuzz/build.zig` also pass
  `-DHAVE_UNISTD_H` and/or `-DHAVE_FCNTL_H` unconditionally. They are not
  in the Windows build path today, but will need the same fix when they
  are.
  
  ## What I Learnt
  
  More of the same
  ```
- [`e7a23a3`](https://github.com/ghostty-org/ghostty/commit/e7a23a37e5f01ad5993447e966f19abaceebdb6b) build: define ssize_t for MSVC in ghostty.h ([#11810](https://github.com/ghostty-org/ghostty/issues/11810)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  > [!WARNING]
  > Review/approve this AFTER #11807 (this PR includes its commits)
  
  92% progress with the fixes!
  
  ## Summary
  - Add a conditional `ssize_t` typedef for MSVC in `include/ghostty.h`
  - MSVC's `<sys/types.h>` does not define `ssize_t` (it is a POSIX type),
  which causes the `translate-c` build step to fail when translating
  `ghostty.h` on Windows
  - Uses `SSIZE_T` from `<BaseTsd.h>`, the standard Windows SDK equivalent
  
  ## Context
  The `translate-c` step translates `ghostty.h` to Zig for test
  compilation. On MSVC, it fails with 3 errors on `ssize_t` (used in
  `ghostty_action_move_tab_s`, `ghostty_action_search_total_s`,
  `ghostty_action_search_selected_s`).
  
  The `#ifdef _MSC_VER` guard means this only affects MSVC builds.
  `BaseTsd.h` is a standard Windows SDK header and `SSIZE_T` is a signed
  pointer-sized integer, matching POSIX `ssize_t` and Zig's `isize`. This
  pattern is used by libuv, curl, and other cross-platform C projects.
  
  ## Test plan
  
  ### Cross-platform results (`zig build test` / `zig build
  -Dapp-runtime=none test` on Windows)
  
  | | Windows | Linux | Mac |
  |---|---|---|---|
  | **BEFORE** (d5aef6e84) | FAIL - 47/51 steps, 1 failed | PASS - 86/86,
  2655/2678 tests, 23 skipped | PASS - 160/160, 2655/2662 tests, 7 skipped
  |
  | **AFTER** (a35f84db3) | FAIL - 48/51 steps, 1 failed | PASS - 86/86,
  2655/2678 tests, 23 skipped | PASS - 160/160, 2655/2662 tests, 7 skipped
  |
  
  ### Windows: what changed (47 -> 48 steps, translate-c fixed)
  
  **Fixed by this PR:**
  - `translate-c` - was `3 errors` (unknown type name 'ssize_t' at lines
  582, 842, 847) -> `success`
  
  **Remaining failure (pre-existing, unrelated):**
  - `compile test ghostty-test` - 3 errors in libcxxabi
  (`std::get_new_handler` not found, `type_info` redefinition). This is
  Zig's bundled libc++ ABI conflicting with MSVC headers when compiling
  the test binary. It was previously masked by the translate-c failure
  blocking this step.
  
  ### Linux/macOS: no regressions
  Identical pass counts and test results before and after.
  
  ## What Have I Learnt
  - I tried fixing this issue the old way, googling and stuff, I
  eventually figured out but it took me way more than I am prepared to
  share. Yikes.
  ```
- [`7114721`](https://github.com/ghostty-org/ghostty/commit/7114721bd4323c776b4c93b0afd313c4785b98b3) build: fix C++ linking and enum signedness on MSVC ([#11812](https://github.com/ghostty-org/ghostty/issues/11812)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  > [!WARNING]
  > Review/approve this AFTER #11807 and #11810 (this PR includes their
  commits)
  
  ## Summary
  
  ### **And `run test ghostty-test` finally runs on Windows! 🎉almost
  there!**
  
  - Skip `linkLibCpp()` on MSVC for dcimgui, spirv-cross, and harfbuzz
  (same fix already applied upstream to highway, simdutf, utfcpp, glslang,
  SharedDeps, GhosttyZig)
  - Fix freetype C enum signedness: MSVC translates C enums as signed
  `int`, while GCC/Clang uses unsigned `int`. Add `@intCast` at call sites
  and `@bitCast` for bit-shift operations on glyph format tags.
  
  ## Context
  Zig unconditionally passes `-nostdinc++` and adds its bundled
  libc++/libc++abi include paths, which conflict with MSVC's own C++
  runtime headers. The MSVC SDK directories (added via `linkLibC`) already
  contain both C and C++ headers, so `linkLibCpp` is not needed.
  
  The freetype enum issue is a different facet of the same MSVC vs
  GCC/Clang divide: `FT_Render_Mode` and `FT_Glyph_Format` are C enums
  that get different signedness on different compilers.
  
  ## Stack
  Stacked on 015-windows/fix-ssize-t-msvc.
  
  ## Test plan
  
  ### Cross-platform results (`zig build test` / `zig build
  -Dapp-runtime=none test` on Windows)
  
  | | Windows | Linux | Mac |
  |---|---|---|---|
  | **BEFORE** (015, a35f84db3) | FAIL - 48/51, 1 failed (compile
  ghostty-test) | PASS - 86/86, 2655/2678, 23 skipped | PASS - 160/160,
  2655/2662, 7 skipped |
  | **AFTER** (016, ce9930051) | FAIL - 49/51, 2630/2654 tests passed, 1
  failed, 23 skipped | PASS - 86/86, 2655/2678, 23 skipped | PASS -
  160/160, 2655/2662, 7 skipped |
  
  ### Windows: what changed (48 -> 49 steps, tests now run)
  
  **Fixed by this PR:**
  - `compile test ghostty-test` - was `3 errors` (libcxxabi conflicts +
  freetype type mismatches) -> `success`
  - `run test ghostty-test` - now actually runs: 2630 passed, 23 skipped,
  1 failed
  
  **Remaining test failure (pre-existing, unrelated):**
  - `ghostty.h MouseShape` - `checkGhosttyHEnum` cannot find
  `GHOSTTY_MOUSE_SHAPE_*` constants in the translate-c output. This is a
  translate-c issue with how MSVC enum constants are exposed, not related
  to C++ linking or enum signedness.
  
  ### Linux/macOS: no regressions
  Identical pass counts and test results before and after.
  
  ## Discussion
  
  ### Grep wider: other unconditional linkLibCpp calls
  `pkg/breakpad/build.zig` still calls `linkLibCpp()` unconditionally but
  is behind sentry and not in the Windows build path. Noted for
  completeness.
  
  ### Freetype enum signedness
  The freetype Zig bindings define `RenderMode = enum(c_uint)` and
  `Encoding = enum(u31)`. On MSVC, C enums are `int` (signed), so the
  translated C functions expect `c_int` parameters. The fix adds
  `@intCast` to convert between signed and unsigned at call sites. This is
  safe because the enum values are small positive integers that fit in
  both types.
  
  Also, not sure if there's a better way to make this change more
  elegantly. The comments are replicated in each instance, probably
  overkill but I have seen this same pattern elsewhere in the codebase.
  
  ## What I Learnt
  - More of the same
  ```
- [`c5092b0`](https://github.com/ghostty-org/ghostty/commit/c5092b09ded689983b674d3d285e4796bf86f677) ci: remove continue-on-error from Windows CI jobs ([@deblasis](https://github.com/deblasis))
  ```text
  Windows tests and builds are now passing reliably. Remove the
  continue-on-error safety net so failures are visible immediately.
  ```
- [`4df71bc`](https://github.com/ghostty-org/ghostty/commit/4df71bcad75a6177b33bea33287982efadef69e8) build: fix zlib compilation on Windows with MSVC ([@deblasis](https://github.com/deblasis))
  ```text
  Gate Z_HAVE_UNISTD_H behind a non-Windows check since unistd.h does
  not exist on Windows. Add _CRT_SECURE_NO_DEPRECATE and
  _CRT_NONSTDC_NO_DEPRECATE for MSVC to suppress deprecation errors
  for standard C functions that zlib uses.
  ```
- [`014873e`](https://github.com/ghostty-org/ghostty/commit/014873e539a6183f82617234fe57ba3983a764ef) build: fix oniguruma compilation on Windows with MSVC ([@deblasis](https://github.com/deblasis))
  ```text
  Conditionally disable POSIX-only header defines (alloca.h, sys/times.h,
  sys/time.h, unistd.h) on Windows since they do not exist with MSVC.
  Enable USE_CRNL_AS_LINE_TERMINATOR on Windows for correct line endings.
  ```
- [`74c6ffe`](https://github.com/ghostty-org/ghostty/commit/74c6ffe78e4b98e58600f22f37a8433f44b53876) build: fix glslang compilation on Windows with MSVC ([@deblasis](https://github.com/deblasis))
  ```text
  Apply the same MSVC fixes used for simdutf and highway: conditionally
  skip linkLibCpp on MSVC since Zig's bundled libc++ headers conflict
  with MSVC's own C++ runtime, and add -std=c++17 for C++17 features
  like std::variant and inline variables that glslang requires.
  ```
- [`f9d3b1a`](https://github.com/ghostty-org/ghostty/commit/f9d3b1aafb4131ab8f9d9a362832ec428bf1cabc) build: fix Windows build failures in helpgen and framegen ([@deblasis](https://github.com/deblasis))
  ```text
  Use writerStreaming() instead of writer() for stdout in helpgen and
  main_build_data. The positional writer calls setEndPos/ftruncate in
  end(), which fails on Windows because ftruncate on pipes maps
  INVALID_PARAMETER to FileTooBig.
  
  Replace scandir with opendir/readdir plus qsort in framegen since
  scandir is a POSIX extension not available on Windows.
  
  This was previously applied and reverted upstream (f4998c6ab, 0fdddd5bc)
  as collateral from an unrelated example-execution hang that has since
  been resolved.
  ```
- [`6854ecc`](https://github.com/ghostty-org/ghostty/commit/6854ecc5a928b92c66d09e6b46b66ec9daf7ea23) ci: remove continue-on-error from Windows CI jobs ([#11796](https://github.com/ghostty-org/ghostty/issues/11796)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Let's see what breaks and let's fix it.
  ```
- [`58e330a`](https://github.com/ghostty-org/ghostty/commit/58e330a8c0b45d026b4c7985a95389ea905c9fed) build: fix zlib compilation on Windows with MSVC ([#11798](https://github.com/ghostty-org/ghostty/issues/11798)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Summary
  - Gate `Z_HAVE_UNISTD_H` behind a non-Windows check since `unistd.h`
  does not exist with MSVC
  - Add `_CRT_SECURE_NO_DEPRECATE` and `_CRT_NONSTDC_NO_DEPRECATE` for
  MSVC to suppress deprecation errors for standard C functions that zlib
  uses
  
  ## Context
  Part of the effort to get `zig build -Dapp-runtime=none test` passing on
  Windows. This unblocks freetype, harfbuzz, libpng, and dcimgui which all
  depend on zlib.
  
  My research shows that we should default to msvc in ci with zig build
  ran without `-Dratget`.
  
  ## Stack
  This is branch 010 in the stacked branches series (soon on Netflix).
  Independent fix, no dependencies on other branches.
  
  ## Test plan
  
  ### test-lib-vt
  
  | | Windows | Linux | Mac |
  |---|---|---|---|
  | **BEFORE** | 3791/3839 passed, 48 skipped | 3791/3839 passed, 48
  skipped | 3807/3839 passed, 32 skipped |
  | **AFTER** | 3791/3839 passed, 48 skipped | 3791/3839 passed, 48
  skipped | 3807/3839 passed, 32 skipped |
  | **Delta** | no change | no change | no change |
  
  ### all tests (`zig build test` / `zig build -Dapp-runtime=none test` on
  Windows)
  
  | | Windows | Linux | Mac |
  |---|---|---|---|
  | **BEFORE** | FAIL — 35/51 build steps, 6 failed | 2655/2678 passed, 23
  skipped (86/86 steps) | 2655/2662 passed, 7 skipped (160/160 steps) |
  | **AFTER** | FAIL — 37/51 build steps, 6 failed | 2655/2678 passed, 23
  skipped (86/86 steps) | 2655/2662 passed, 7 skipped (160/160 steps) |
  | **Delta** | +2 build steps (zlib + png unblocked) | no change | no
  change |
  
  - Zero regressions on any platform
  - Windows improved: zlib and png now compile (35 -> 37 steps)
  - Remaining 6 Windows build failures (`ssize_t`, `helpgen`, `framegen`,
  `harfbuzz`, `dcimgui`) are addressed by other PRs in the stack
  
  ## What I Learnt
  - Always run tests with `--summary all` to get actual pass/skip/fail
  counts. Without it, zig just exits 0 or 1 and you have no numbers to
  compare. "You get confident if you got the numbers."
  - Build dependencies cascade: fixing zlib also unblocked png (which
  depends on it), giving us +2 build steps from a one-file change.
  ```
- [`5cc22c2`](https://github.com/ghostty-org/ghostty/commit/5cc22c23e6a6e4346fdad2480dca04e4b05a5c88) build: fix oniguruma compilation on Windows with MSVC ([#11800](https://github.com/ghostty-org/ghostty/issues/11800)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  > [!WARNING]
  > Review/approve this AFTER #11798 (this PR stacks on top of it... ergo,
  it includes its commits)
  
  ## Summary
  - Conditionally disable POSIX-only header defines (`alloca.h`,
  `sys/times.h`, `sys/time.h`, `unistd.h`) on Windows since they do not
  exist with MSVC
  - Enable `USE_CRNL_AS_LINE_TERMINATOR` on Windows for correct line
  endings
  
  ## Context
  Oniguruma's `config.h` template had all POSIX header availability
  defines hardcoded to `true`. On MSVC, these headers don't exist, causing
  24 compilation errors (all `alloca.h` file not found).
  
  Uses a comptime `is_windows` constant to flip the config values, same
  pattern as PR #11798 (zlib).
  
  ## Stack
  Stacked on 010-windows/fix-zlib-msvc.
  
  ## Test plan
  
  ### test-lib-vt
  
  | | Windows | Linux | Mac |
  |---|---|---|---|
  | **BEFORE** | 3791/3839 passed, 48 skipped | 3791/3839 passed, 48
  skipped | 3807/3839 passed, 32 skipped |
  | **AFTER** | 3791/3839 passed, 48 skipped | 3791/3839 passed, 48
  skipped | 3807/3839 passed, 32 skipped |
  | **Delta** | no change | no change | no change |
  
  ### all tests (`zig build test` / `zig build -Dapp-runtime=none test` on
  Windows)
  
  | | Windows | Linux | Mac |
  |---|---|---|---|
  | **BEFORE** | FAIL — 37/51 steps, 6 failed | 2655/2678 passed, 23
  skipped (86/86 steps) | 2655/2662 passed, 7 skipped (160/160 steps) |
  | **AFTER** | FAIL — 38/51 steps, 5 failed | 2655/2678 passed, 23
  skipped (86/86 steps) | 2655/2662 passed, 7 skipped (160/160 steps) |
  | **Delta** | +1 step, -1 failure (oniguruma unblocked) | no change | no
  change |
  
  - Zero regressions on any platform
  - Windows improved: oniguruma now compiles (37 -> 38 steps, 6 -> 5
  failures)
  - Remaining 5 Windows failures (`translate-c`/ssize_t, `helpgen`,
  `framegen`, `glslang`, `harfbuzz` via freetype) are addressed by other
  PRs in the stack
  
  ## What I Learnt
  - comptime, man. It's the small things.
  ```
- [`57b9292`](https://github.com/ghostty-org/ghostty/commit/57b929203bde64614885133c949ef2ca1fb83b5c) build: fix glslang compilation on Windows with MSVC ([#11801](https://github.com/ghostty-org/ghostty/issues/11801)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  > [!WARNING]
  > Review/approve this AFTER #11798 and #11800 (this PR stacks on top of
  rhem... ergo, it includes their commits)
  > Don't cheat! Start from the oldest one! 😄 I know these are almost
  one-liners but I am doing this mostly for documentation and karma
  points.
  
  ## Summary
  - Conditionally skip `linkLibCpp()` on MSVC since Zig's bundled libc++
  headers conflict with MSVC's own C++ runtime
  - Add `-std=c++17` flag for C++17 features (std::variant,
  std::filesystem, inline variables) that glslang requires
  
  ## Context
  The exact same `linkLibCpp` fix was applied to `simdutf` and `highway`
  in commits 3d581eb92 and b4c529a82 but glslang was missed. Without this
  fix, glslang fails with 297 compilation errors on MSVC.
  
  Thanks Claude for the forensic digging. A carpenter should always be
  thankful for his tools. Even if they are borrowed, maybe even more so.
  
  ## Stack
  Stacked on 011-windows/fix-oniguruma-msvc.
  
  ## Discussion points
  
  **`-std=c++17` scope:** Currently added unconditionally for all targets.
  Tested on all three platforms with no regressions, but since this is
  specifically fixing a Windows/MSVC issue, it could be gated behind
  `target.result.abi == .msvc`. Donno. The reason it works unconditionally
  is that Zig's bundled clang already defaults to C++17 on non-MSVC
  targets, so the flag is a no-op there. Open to either approach.
  
  **Other packages with bare `linkLibCpp()`:** The same `linkLibCpp` guard
  has been applied to `simdutf`, `highway`, `utfcpp`, and now `glslang`.
  However, `spirv-cross`, `dcimgui`, `harfbuzz`, and `breakpad` still have
  unconditional `linkLibCpp()` calls. These may need the same treatment
  when they become buildable on MSVC (some are currently blocked by other
  issues like freetype's `unistd.h`). Worth tracking as a follow-up?
  
  ## Test plan
  
  ### test-lib-vt
  
  | | Windows | Linux | Mac |
  |---|---|---|---|
  | **BEFORE** | 3791/3839 passed, 48 skipped | 3791/3839 passed, 48
  skipped | 3807/3839 passed, 32 skipped |
  | **AFTER** | 3791/3839 passed, 48 skipped | 3791/3839 passed, 48
  skipped | 3807/3839 passed, 32 skipped |
  | **Delta** | no change | no change | no change |
  
  ### all tests (`zig build test` / `zig build -Dapp-runtime=none test` on
  Windows)
  
  | | Windows | Linux | Mac |
  |---|---|---|---|
  | **BEFORE** | FAIL — 38/51 build steps, 5 failed | 2655/2678 passed, 23
  skipped (86/86 steps) | 2655/2662 passed, 7 skipped (160/160 steps) |
  | **AFTER** | FAIL — 39/51 build steps, 4 failed | 2655/2678 passed, 23
  skipped (86/86 steps) | 2655/2662 passed, 7 skipped (160/160 steps) |
  | **Delta** | +1 build step (glslang unblocked) | no change | no change
  |
  
  - Zero regressions on any platform
  - Windows improved: glslang now compiles (38 -> 39 steps, 5 -> 4
  failures)
  - Remaining 4 Windows failures (`helpgen`, `framegen`, `freetype`,
  `translate-c`) are addressed by other PRs in the stack
  
  ## What I Learnt
  
  - **MSVC's clang doesn't default to C++17.** Zig's bundled clang uses
  C++17 by default on Linux/Mac, but when targeting MSVC, the C++ standard
  needs to be specified explicitly. Without `-std=c++17`, features like
  `std::variant`, `std::filesystem`, and `inline` variables are gated
  behind `_HAS_CXX17` and won't compile.
  - **`linkLibCpp` conflicts with MSVC headers.** Zig's `linkLibCpp`
  passes `-nostdinc++` and adds its own libc++/libc++abi headers, which
  collide with the C++ headers already provided by the MSVC SDK through
  `linkLibC`. On MSVC, you don't need `linkLibCpp` at all since the SDK
  includes both C and C++ headers. I think yesterday we dealt with
  something similar. Windows is fun. 🫠 Unironically and chronically.
  - **Grep wider.** The `linkLibCpp` guard was already applied to simdutf,
  highway, and utfcpp but missed glslang. When a fix follows a repeated
  pattern across packages, search the whole codebase before declaring it
  complete.
  ```
- [`aec3a6e`](https://github.com/ghostty-org/ghostty/commit/aec3a6ebf62eaa204f678ac2a075775012a2d3a3) build: fix Windows build failures in helpgen and framegen ([#11803](https://github.com/ghostty-org/ghostty/issues/11803)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  > [!WARNING]
  > Review/approve this AFTER #11798, #11800 and #11801 (this PR stacks on
  top of rhem... ergo, it includes their commits)
  > Don't cheat! Start from the oldest one! 😄 I know these are almost
  one-liners but I am doing this mostly for documentation and karma
  points. BTW, Github needs to level up this wankflow like a lot... IMHO
  
  ## Summary
  - Use `writerStreaming()` instead of `writer()` for stdout in helpgen
  and main_build_data (`ftruncate` on pipes fails on Windows with
  `INVALID_PARAMETER` mapped to `FileTooBig`)
  - Replace POSIX `scandir` with `opendir`/`readdir` plus `qsort` in
  framegen since `scandir` is not available on Windows
  
  ## Context
  This fix was previously applied upstream by Mitchell (f4998c6ab) and
  reverted 15 minutes later (0fdddd5bc). The reason for the revert is not
  clear. Around the same time, a CI step was added to execute cmake
  examples on Windows, which was later removed (b723f2a43) with the note
  "hangs, so remove it entirely". Whether the revert is related to the
  hang or had a separate reason, we don't know.
  
  What we do know:
  - Both `helpgen` and `framegen` run during normal builds on Windows (via
  `SharedDeps`), not just during dist packaging. Claude had told me the
  opposite before but "don't trust and verify".
  - Without this fix, both tools fail: helpgen with `FileTooBig`
  (ftruncate on pipes), framegen with `scandir` undeclared
  - The fix does not regress Linux or macOS
  
  ## Stack
  Stacked on 012-windows/fix-glslang-msvc.
  
  ## Test plan
  
  ### Cross-platform results (`zig build test` / `zig build
  -Dapp-runtime=none test` on Windows)
  
  | | Windows | Linux | Mac |
  |---|---|---|---|
  | **BEFORE** (74c6ffe78) | FAIL - 39/51 steps, 4 failed | PASS - 86/86,
  2655/2678 tests, 23 skipped | PASS - 160/160, 2655/2662 tests, 7 skipped
  |
  | **AFTER** (f9d3b1aaf) | FAIL - 44/51 steps, 2 failed | PASS - 86/86,
  2655/2678 tests, 23 skipped | PASS - 160/160, 2655/2662 tests, 7 skipped
  |
  
  ### Windows: what changed (39 > 44 steps, 4 > 2 failures)
  
  **Fixed by this PR:**
  - `run exe helpgen` -> was `failure` (FileTooBig from ftruncate on
  stdout pipe) -> `success`
  - `compile exe framegen` -> was `1 errors` (scandir undeclared) ->.
  `success`
  
  **Remaining failures (pre-existing, fixed by later PRs in stack):**
  - `translate-c` -> 3 errors (`ssize_t` unknown in ghostty.h on MSVC)
  - `compile lib freetype` -> 2 errors (`unistd.h` not found)
  
  ### Linux/macOS: no regressions
  Identical pass counts and test results before and after.
  
  ## Discussion points
  
  ### "Grep wider"  other `stdout().writer()` callsites
  There are 15+ other `stdout().writer(&buf)` callsites in the codebase.
  Build-time generators that capture stdout (webgen, mdgen, unicode
  generators) would have the same `ftruncate` issue if they ran on
  Windows. Currently they don't appear in the Windows build graph, but
  worth noting for future Windows work.
  
  ### `writerStreaming()` vs `writer()`
  `writer()` calls `ftruncate` on flush/end to set the file size, which
  fails on pipes (stdout captured by the build system).
  `writerStreaming()` skips the truncate since the output goes to a pipe,
  not a seekable file. This is the correct API for this use case on all
  platforms, not just Windows.
  
  ## What I Learnt
  - When upstream has applied and reverted something, state what you
  observe rather than speculating about their reasoning. Let the reviewer
  fill in context you don't have.
  - "Grep wider" (testing pattern): `stdout().writer()` appears in 17
  files. Only 2 are fixed here because only 2 are in the current Windows
  build path. But the pattern exists more broadly.
  - I feel like I am training my replacements. I mean, I am a parent, it
  rhymes.
  - I feel like my replacements are training me. It rhymes as well.
  ```
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

