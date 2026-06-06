> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: June 6, 2026 at 15:28 UTC.

## June 6, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/27050927493)  
Summary: 1 runs • 2 commits • 1 authors

### Changes

- [`a979b86`](https://github.com/ghostty-org/ghostty/commit/a979b8698b2798483bcb957c5f4059cb53c8dd72) terminal: hook up glyph protocol glossary to terminal state ([@mitchellh](https://github.com/mitchellh))
  ```text
  This hooks up the glyph protocol glossary to the terminal state. This
  effectively makes us handle the APC protocol for it both in Ghostty GUI
  and libghostty, although we didn't implement the renderer yet.
  
  The Zig/C libghostty API also has a way to disable the protocol but it is
  enabled by default. The memory usage is bound by the specification.
  
  For dirty tracking for the renderer, we're going with the simple route that
  any glyph change marks a coarse grained dirty flag and we'll [in the future]
  rebuild the entire state in the renderer. I think this will be fine for
  realistic workloads, but we can reassess in the future when we have
  real workloads.
  ```
- [`f146db5`](https://github.com/ghostty-org/ghostty/commit/f146db5535a154baa74806589f12d7e27daccbbe) terminal: hook up glyph protocol glossary to terminal state ([#12937](https://github.com/ghostty-org/ghostty/issues/12937)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This hooks up the glyph protocol glossary to the terminal state. This
  effectively makes us handle the APC protocol for it both in Ghostty GUI
  and libghostty, although we didn't implement the renderer yet.
  
  The Zig/C libghostty API also has a way to disable the protocol but it
  is enabled by default. The memory usage is bound by the specification.
  
  For dirty tracking for the renderer, we're going with the simple route
  that any glyph change marks a coarse grained dirty flag and we'll [in
  the future] rebuild the entire state in the renderer. I think this will
  be fine for realistic workloads, but we can reassess in the future when
  we have real workloads.
  ```

## June 5, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/27043592302), [2](https://github.com/ghostty-org/ghostty/actions/runs/27040558144)  
Summary: 2 runs • 20 commits • 3 authors

### Changes

- [`d649454`](https://github.com/ghostty-org/ghostty/commit/d6494544cf9f6df963ae32377f3c7783545d9804) terminal: add panic test for integer overflow in selectPrev with no active matches ([@bo2themax](https://github.com/bo2themax))
- [`bd365e1`](https://github.com/ghostty-org/ghostty/commit/bd365e1aa96133b7876221aa7b58dabb3c58e040) terminal: cover selection drop when all matches disappear ([@claude](https://github.com/claude))
  ```text
  selectPrev's wrap (active_len + history_len - 1) would underflow if a
  selection were live while both result lists are empty. Add a test that
  exercises the invariant making that unreachable: overwriting the only match
  forces a reload that empties both lists and drops the selection, so the next
  select() hits the no-matches guard instead of the wrap arithmetic.
  ```
- [`1e63834`](https://github.com/ghostty-org/ghostty/commit/1e63834cdc90365fd458b34b1b02413d42972995) fix(terminal): avoid integer overflow in selectPrev with no active matches ([@bo2themax](https://github.com/bo2themax))
- [`ea37f46`](https://github.com/ghostty-org/ghostty/commit/ea37f4672c84e749f56600a53d444b2ca4b0c903) fix(terminal): avoid integer overflow in selectPrev with no active matches ([#12936](https://github.com/ghostty-org/ghostty/issues/12936)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Also found when test searching.
  
  Run Ghostty debug on macOS and follow these steps:
  
  1. Open Ghostty, `cat src/Surface.zig` and start search
  `self.startClipboardRequest`.
  2. Click up button(Press enter) 6 times and click down button (Press
  shift+enter) 6 times.
  3. You should see a panic crash.
  
  ### AI Disclosure
  Claude implemented the fix and the unit test.
  
  I reviewed it and tested it myself.
  ```
- [`2055bb6`](https://github.com/ghostty-org/ghostty/commit/2055bb6dd6a039ffd7251e644b637cac6383e4f2) terminal: glyph request glyf decode ([@mitchellh](https://github.com/mitchellh))
- [`59d2ad9`](https://github.com/ghostty-org/ghostty/commit/59d2ad9b6a2fbf46b64df9fe82f93d153219f063) terminal: glyph protocol Glossary entry starting to take shape ([@mitchellh](https://github.com/mitchellh))
- [`cf548a3`](https://github.com/ghostty-org/ghostty/commit/cf548a3aadf53f55865e270abc27db152f0002d8) terminal/apc: glyph glossary registration business logic ([@mitchellh](https://github.com/mitchellh))
- [`0cd815f`](https://github.com/ghostty-org/ghostty/commit/0cd815f94a6d9f4c9ca4dd8bbd00f372c4a3e441) terminal/apc: glyph glossary delete, contains, clear ([@mitchellh](https://github.com/mitchellh))
- [`cc91940`](https://github.com/ghostty-org/ghostty/commit/cc91940993e70e611ba5d8609ffecfcfa53ade39) terminal/glyph: register request ([@mitchellh](https://github.com/mitchellh))
- [`6f83d8a`](https://github.com/ghostty-org/ghostty/commit/6f83d8a4f14b7b095f0c6c415c01467afe395384) terminal/glyph: clear ([@mitchellh](https://github.com/mitchellh))
- [`d271b27`](https://github.com/ghostty-org/ghostty/commit/d271b271f9e519ad21f70d3b37415d508480df35) terminal/glyph: query ([@mitchellh](https://github.com/mitchellh))
- [`1c0aac5`](https://github.com/ghostty-org/ghostty/commit/1c0aac54bdd86a94ee6c3ec4ce974ae6797c85bf) font: reshuffle glyph sizing types to Glyph.zig ([@mitchellh](https://github.com/mitchellh))
- [`7837563`](https://github.com/ghostty-org/ghostty/commit/7837563ed6583d9b29565b926a0272daa251a887) fix(terminal): guard wrap count when resize pushes cursor to scrollback ([@claude](https://github.com/claude))
  ```text
  In the column-shrink (.lt) branch of PageList.resize, resizeWithoutReflow
  lowers self.rows before resizeCols runs. Because the active area is anchored
  to the bottom, shrinking rows moves the active-area top down; a cursor near
  the top of the old active area then ends up above the new active area (in
  scrollback).
  
  resizeCols counts wrap continuations from the cursor pin up to the active-area
  top via a .left_up rowIterator. When the cursor pin is above the limit, the
  range is reversed and the iterator's order assertion fires (SIGABRT in debug;
  silently iterates empty in release).
  
  Count zero wraps when the cursor pin is above the active area, mirroring the
  post-reflow preserved-cursor block which already no-ops for a non-active
  cursor. Add a regression test.
  ```
- [`05eeb43`](https://github.com/ghostty-org/ghostty/commit/05eeb439421a362e783ebead03edfa455e2bda38) font: exclude libghostty-vt from embedded font tests ([@mitchellh](https://github.com/mitchellh))
- [`f0d81f1`](https://github.com/ghostty-org/ghostty/commit/f0d81f15ee886e17e188422ec057caf4cfcdaa92) terminal/apc: reject malformed glyph clear cp ([@mitchellh](https://github.com/mitchellh))
  ```text
  Glyph clear execution previously treated an unparsable cp option the same
  as an omitted cp option. That made inputs such as c;cp=zz behave like a
  bare clear request and remove every glossary registration.
  
  Track clear option presence separately from successful decoding. A
  present but malformed cp now returns a malformed_payload clear failure
  without mutating the glossary, while an omitted cp still clears all
  registrations.
  ```
- [`e45f002`](https://github.com/ghostty-org/ghostty/commit/e45f002d1aaee91a9c17dd9293e4262ef608149e) terminal/apc: reject malformed glyph register input ([@mitchellh](https://github.com/mitchellh))
  ```text
  Register parsing now validates the full register request shape before
  constructing the parsed command. Inputs that only contain the verb
  separator, such as `r`, `r;cp=e0a0`, or `r;foo`, now fail with
  InvalidFormat instead of reaching Register invariants guarded by asserts.
  
  Valid empty-payload requests still parse when they include the payload
  separator, allowing execution to report malformed_payload through the
  normal protocol response path.
  ```
- [`b661ada`](https://github.com/ghostty-org/ghostty/commit/b661adad2ec9e32d739684b3051c733dbcd021ea) font: add exact glyph protocol constraints ([@mitchellh](https://github.com/mitchellh))
  ```text
  Extend glyph render constraints with cell-span sizing modes for height,
  width, contain, cover bounds, and stretch bounds. These preserve the
  existing face-targeted behavior for platform fonts, emoji, and Nerd Font
  rules while giving registered glyphs a target based on terminal cell
  spans.
  
  Map Glyph Protocol registration options to the new constraint modes so
  sizing follows the spec formulas based on authored advance width and line
  height. Baseline alignment now places design-space y=0 on the terminal
  text baseline instead of approximating it as start alignment.
  
  Document the placement formulas in the local protocol summary and add
  focused tests for constraint mapping, cell-span padding, line-height and
  advance scaling, contain versus cover behavior, stretch, and baseline
  placement.
  ```
- [`aab0f80`](https://github.com/ghostty-org/ghostty/commit/aab0f8079f6994be6b056a9737d46408ae0d9d82) Revert "font: add exact glyph protocol constraints" ([@mitchellh](https://github.com/mitchellh))
  ```text
  This reverts commit b661adad2ec9e32d739684b3051c733dbcd021ea.
  ```
- [`179fe57`](https://github.com/ghostty-org/ghostty/commit/179fe571d75e64f3b0cf84d2b550b10d3c4230d1) terminal: Glyph Protocol Glossary and request handler implementation ([#12930](https://github.com/ghostty-org/ghostty/issues/12930)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds the glossary and request handler logic to the glyph protocol
  package.
  
  We now have a fully spec compliant business-logic part of the glyph
  protocol.
  
  **This doesn't yet hook it up to terminal state.** So it isn't impacting
  any real-world usage yet.
  
  Code was hand-written, tests were AI-assisted and human reviewed.
  ```
- [`5a1edfb`](https://github.com/ghostty-org/ghostty/commit/5a1edfb25402f06bc11568de3fcbf4bcc4b898be) fix(terminal): guard wrap count when resize pushes cursor to scrollback ([#12935](https://github.com/ghostty-org/ghostty/issues/12935)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Found this issue when testing some search features; follow up for
  #12907.
  
  You can either reproduce using the PoC below with `libghostty-vt` or run
  Ghostty debug on macOS and follow these steps:
  
  1. Open Ghostty and start search `0`.
  2. Press `cmd+=` to increase font size.
  3. You should see a panic crash.
  
  ### AI Disclosure
  
  As the commit suggests, Claude implemented the fix, the unit test, and
  PoC file.
  
  I reviewed it(seems reasonable to me, but I’m not a Zig professional)
  and tested it myself.
  
  
  ```zig
  // PoC: resize panic when shrinking both axes with the cursor near the top
  // of a fully-populated screen.
  //
  // Build (with libghostty-vt headers + dylib on the standard search paths):
  //   zig run poc.zig -lghostty-vt
  //
  // Or point at a local build:
  //   zig run poc.zig -I <prefix>/include -L <prefix>/lib -lghostty-vt
  //
  // At runtime the dylib must be discoverable (DYLD_LIBRARY_PATH on macOS,
  // LD_LIBRARY_PATH on Linux, or an rpath baked in at link time).
  //
  // Without the fix, this aborts with
  //   reached unreachable code   (assert in PageList.Pin.pageIterator)
  // at _terminal.PageList.resizeCols on a debug/safe build. On release it
  // silently iterates an empty (reversed) range.
  
  const std = @import("std");
  const c = @cImport({
      @cInclude("ghostty/vt.h");
  });
  
  pub fn main() !void {
      var term: c.GhosttyTerminal = null;
      const opts: c.GhosttyTerminalOptions = .{
          .cols = 80,
          .rows = 24,
          .max_scrollback = 1000,
      };
      if (c.ghostty_terminal_new(null, &term, opts) != c.GHOSTTY_SUCCESS) {
          return error.InitFailed;
      }
      defer c.ghostty_terminal_free(term);
  
      // Fill every one of the 24 active rows with non-blank content. This is
      // what makes the bug reachable: when rows shrink, resizeWithoutReflow
      // can only trim *blank* trailing rows, so non-blank rows are instead
      // pushed up into scrollback and the active-area top moves down.
      {
          var buf: [256]u8 = undefined;
          var i: usize = 0;
          while (i < 24) : (i += 1) {
              // "X" on each row; CR+LF between rows but not after the last so
              // we don't scroll the top row away.
              const line = if (i + 1 < 24)
                  std.fmt.bufPrint(&buf, "X\r\n", .{}) catch unreachable
              else
                  std.fmt.bufPrint(&buf, "X", .{}) catch unreachable;
              c.ghostty_terminal_vt_write(term, line.ptr, line.len);
          }
      }
  
      // CSI 1;1H -> park the cursor on the TOP row (1-based). The active area is
      // anchored to the bottom, so once we shrink rows this row falls above the
      // new active-area top, i.e. into scrollback.
      const move = "\x1b[1;1H";
      c.ghostty_terminal_vt_write(term, move.ptr, move.len);
  
      // Shrink both axes. Columns must shrink to take resize()'s .lt branch,
      // which runs the row shrink first and then resizeCols with the original
      // (now out-of-active-area) cursor pin. Panics in
      // _terminal.PageList.resizeCols.
      _ = c.ghostty_terminal_resize(term, 79, 20, 8, 16);
  
      std.debug.print("survived resize (fix is present)\n", .{});
  }
  ```
  ````

## June 4, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26973076631), [2](https://github.com/ghostty-org/ghostty/actions/runs/26971272537)  
Summary: 2 runs • 13 commits • 5 authors

### Changes

- [`2444e4d`](https://github.com/ghostty-org/ghostty/commit/2444e4d557e47ecb1a63d8198b7f28f3a94fa8f8) libghostty: add option to set default cursor style ([@noib3](https://github.com/noib3))
  ```text
  Adds an option to `libghostty-vt` to configure the default cursor style
  that should be displayed when an app sends a DECSCUSR reset sequence
  (`CSI 0 q`).
  ```
- [`66950a4`](https://github.com/ghostty-org/ghostty/commit/66950a4a537d1c21fe63a7c53d3c254bbe83679a) libghostty: add option to set default cursor blink ([@noib3](https://github.com/noib3))
  ```text
  Adds an option to `libghostty-vt` to configure whether the default
  cursor displayed when an app sends a DECSCUSR reset sequence should
  blink.
  ```
- [`e7b506c`](https://github.com/ghostty-org/ghostty/commit/e7b506c69d2ae8f071b29b1deb3c6ff93cf73a8d) Test setting/resetting the default cursor style and blink ([@noib3](https://github.com/noib3))
- [`42fcd58`](https://github.com/ghostty-org/ghostty/commit/42fcd58dba54c2a0404c1c3d73c7d44081fac836) libghostty-vt: add options to configure default cursor's style and blink ([#12900](https://github.com/ghostty-org/ghostty/issues/12900)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This PR adds 2 options to `libghostty-vt` to configure the style and
  blink status of the default cursor. They control how the terminal
  renders the cursor when a program doesn't request any explicit style or
  when it resets it to the terminal's default state by sending a DECSCUSR
  reset sequence (`CSI 0 q`).
  ```
- [`d8f56b7`](https://github.com/ghostty-org/ghostty/commit/d8f56b790e2cce1dd42908a94655d9242a813892) font: add glyf entry decoder to outline ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add Glyf.Outline for decoding the contours and points of a Glyf.
  ```
- [`8eff74e`](https://github.com/ghostty-org/ghostty/commit/8eff74ef7680f40bbcc03d634ad1ad11417c29f3) font: add glyf rasterizer ([@mitchellh](https://github.com/mitchellh))
- [`51995a7`](https://github.com/ghostty-org/ghostty/commit/51995a7822de65adfbd1f7c3208d9522500ee58c) font: glyf rasterization png comparison ([@mitchellh](https://github.com/mitchellh))
- [`c4e1ab8`](https://github.com/ghostty-org/ghostty/commit/c4e1ab8883aca124eacbbec916f404a7f7bebf71) core: send selection_changed notification ([@jparise](https://github.com/jparise))
  ```text
  The core had no signal to the apprt when the active selection changed,
  so a consumer (e.g. a screen reader) kept reading a stale selection
  until some unrelated query refreshed it.
  
  This change adds a payload-less selection_changed action that's fired on
  a selection state transition. The apprt reads the current selection
  through the normal read path.
  
  This consolidates selection state changes so the notification fires
  consistently: all sites route through setSelection rather than calling
  screen.select directly, including the mouse paths that previously
  bypassed it for clipboard timing.
  
  The new setSelectionAndCopy extends setSelection with the additional
  'copy_on_select' behavior.
  
  On macOS, this posts .ghosttySelectionDidChange, which is debounced
  before posting a NSAccessibility .selectedTextChanged notification.
  
  GTK has no consumer yet and no-ops the action.
  ```
- [`7fa6fff`](https://github.com/ghostty-org/ghostty/commit/7fa6fffbca802897047186eed7b43faa3bcb87cf) terminal: saturate cursor subtraction in resizeCols (zongyuan.li)
  ```text
  PageList.resize takes the .lt branch when columns shrink, which calls
  resizeWithoutReflow (mutating self.rows to the new smaller value) and
  then resizeCols with the original opts.cursor.y. When both axes shrink
  in one call and the cursor sits at or past the new bottom row, the
  expression `self.rows - c.y - 1` underflows and panics in safety builds.
  
  Use saturating subtraction; "remaining rows below cursor" is 0 once the
  cursor sits at or past the new bottom.
  ```
- [`f135b95`](https://github.com/ghostty-org/ghostty/commit/f135b950989cbf404ef6dc52affc5c2f9060bba3) terminal: test shrinking both axes with cursor past new bottom (Zongyuan Li)
  ```text
  Adds a PageList regression test exercising the underflow path fixed in
  7fa6fffbc, and a libghostty-vt C API test mirroring the original repro
  through ghostty_terminal_resize.
  ```
- [`4782e59`](https://github.com/ghostty-org/ghostty/commit/4782e59eacfa3d79cf0862378a82dca1ff0476b3) terminal: saturate cursor subtraction in resizeCols ([#12907](https://github.com/ghostty-org/ghostty/issues/12907)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  PageList.resize takes the .lt branch when columns shrink, which calls
  resizeWithoutReflow (mutating self.rows to the new smaller value) and
  then resizeCols with the original opts.cursor.y. When both axes shrink
  in one call and the cursor sits at or past the new bottom row, the
  expression `self.rows - c.y - 1` underflows and panics in safety builds.
  
  Use saturating subtraction; "remaining rows below cursor" is 0 once the
  cursor sits at or past the new bottom.
  
  This problem is reported by
  [discussion#12905](https://github.com/ghostty-org/ghostty/discussions/12905)
  ```
- [`52368cb`](https://github.com/ghostty-org/ghostty/commit/52368cbcff21d52d1c1b35a95543c31683618876) core: send selection_changed notification ([#12902](https://github.com/ghostty-org/ghostty/issues/12902)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The core had no signal to the apprt when the active selection changed,
  so a consumer (e.g. a screen reader) kept reading a stale selection
  until some unrelated query refreshed it.
  
  This change adds a payload-less selection_changed action that's fired on
  a selection state transition. The apprt reads the current selection
  through the normal read path.
  
  This consolidates selection state changes so the notification fires
  consistently: all sites route through setSelection rather than calling
  screen.select directly, including the mouse paths that previously
  bypassed it for clipboard timing.
  
  The new setSelectionAndCopy extends setSelection with the additional
  'copy_on_select' behavior.
  
  On macOS, this posts .ghosttySelectionDidChange, which is debounced
  before posting a NSAccessibility .selectedTextChanged notification.
  
  GTK has no consumer yet and no-ops the action.
  
  See: #9932
  ```
- [`8fcead0`](https://github.com/ghostty-org/ghostty/commit/8fcead00e56a9c4e84af5ead9b8913824223f03e) font: glyf outline decoder and rasterizer ([#12893](https://github.com/ghostty-org/ghostty/issues/12893)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds a Glyf outline decoder and rasterizer.
  
  So it turns out that FreeType and CoreText have very shitty APIs for raw
  Glyf table rasterization. CoreText as far as I can find can't do it at
  all. In both cases you have to create a synthetic font with just this
  entry and rasterize the glyph. And the code to do all that was WAYYYYYY
  complex such that this made way more sense.
  
  We need this for the Glyph Protocol.
  
  **AI disclosure:** Hand-written parser, rasterizer. AI assisted
  validation and test writing. I read the spec myself.
  
  cc @qwerasd205
  ```

## June 3, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26908961402), [2](https://github.com/ghostty-org/ghostty/actions/runs/26869468488), [3](https://github.com/ghostty-org/ghostty/actions/runs/26864366652)  
Summary: 3 runs • 5 commits • 5 authors

### Changes

- [`5f7738a`](https://github.com/ghostty-org/ghostty/commit/5f7738a0e9fc192c2b8ccbb0da22084bde5dd191) build(deps): bump actions/checkout from 6.0.2 to 6.0.3 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [actions/checkout](https://github.com/actions/checkout) from 6.0.2 to 6.0.3.
  - [Release notes](https://github.com/actions/checkout/releases)
  - [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/actions/checkout/compare/de0fac2e4500dabe0009e67214ff5f5447ce83dd...df4cb1c069e1874edd31b4311f1884172cec0e10)
  
  ---
  updated-dependencies:
  - dependency-name: actions/checkout
    dependency-version: 6.0.3
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`bfe633a`](https://github.com/ghostty-org/ghostty/commit/bfe633a9487892ff3d27ed727db540267f22ef90) build(deps): bump actions/checkout from 6.0.2 to 6.0.3 ([#12911](https://github.com/ghostty-org/ghostty/issues/12911)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps [actions/checkout](https://github.com/actions/checkout) from 6.0.2
  to 6.0.3.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/actions/checkout/releases">actions/checkout's
  releases</a>.</em></p>
  <blockquote>
  <h2>v6.0.3</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>Update changelog by <a
  href="https://github.com/ericsciple"><code>@​ericsciple</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2357">actions/checkout#2357</a></li>
  <li>fix: expand merge commit SHA regex and add SHA-256 test cases by <a
  href="https://github.com/yaananth"><code>@​yaananth</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2414">actions/checkout#2414</a></li>
  <li>Fix checkout init for SHA-256 repositories by <a
  href="https://github.com/yaananth"><code>@​yaananth</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2439">actions/checkout#2439</a></li>
  <li>Update changelog for v6.0.3 by <a
  href="https://github.com/yaananth"><code>@​yaananth</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2446">actions/checkout#2446</a></li>
  </ul>
  <h2>New Contributors</h2>
  <ul>
  <li><a href="https://github.com/yaananth"><code>@​yaananth</code></a>
  made their first contribution in <a
  href="https://redirect.github.com/actions/checkout/pull/2414">actions/checkout#2414</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/actions/checkout/compare/v6...v6.0.3">https://github.com/actions/checkout/compare/v6...v6.0.3</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/actions/checkout/blob/main/CHANGELOG.md">actions/checkout's
  changelog</a>.</em></p>
  <blockquote>
  <h1>Changelog</h1>
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
  <h2>v4.2.0</h2>
  <ul>
  <li>Add Ref and Commit outputs by <a
  href="https://github.com/lucacome"><code>@​lucacome</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/1180">actions/checkout#1180</a></li>
  <li>Dependency updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>- <a
  href="https://redirect.github.com/actions/checkout/pull/1777">actions/checkout#1777</a>,
  <a
  href="https://redirect.github.com/actions/checkout/pull/1872">actions/checkout#1872</a></li>
  </ul>
  <h2>v4.1.7</h2>
  <ul>
  <li>Bump the minor-npm-dependencies group across 1 directory with 4
  updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/1739">actions/checkout#1739</a></li>
  <li>Bump actions/checkout from 3 to 4 by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/1697">actions/checkout#1697</a></li>
  <li>Check out other refs/* by commit by <a
  href="https://github.com/orhantoy"><code>@​orhantoy</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/1774">actions/checkout#1774</a></li>
  </ul>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/actions/checkout/commit/df4cb1c069e1874edd31b4311f1884172cec0e10"><code>df4cb1c</code></a>
  Update changelog for v6.0.3 (<a
  href="https://redirect.github.com/actions/checkout/issues/2446">#2446</a>)</li>
  <li><a
  href="https://github.com/actions/checkout/commit/1cce3390c2bfda521930d01229c073c7ff920824"><code>1cce339</code></a>
  Fix checkout init for SHA-256 repositories (<a
  href="https://redirect.github.com/actions/checkout/issues/2439">#2439</a>)</li>
  <li><a
  href="https://github.com/actions/checkout/commit/900f2210b1d28bbbd0bd22d17926b9e224e8f231"><code>900f221</code></a>
  fix: expand merge commit SHA regex and add SHA-256 test cases (<a
  href="https://redirect.github.com/actions/checkout/issues/2414">#2414</a>)</li>
  <li><a
  href="https://github.com/actions/checkout/commit/0c366fd6a839edf440554fa01a7085ccba70ac98"><code>0c366fd</code></a>
  Update changelog (<a
  href="https://redirect.github.com/actions/checkout/issues/2357">#2357</a>)</li>
  <li>See full diff in <a
  href="https://github.com/actions/checkout/compare/de0fac2e4500dabe0009e67214ff5f5447ce83dd...df4cb1c069e1874edd31b4311f1884172cec0e10">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=actions/checkout&package-manager=github_actions&previous-version=6.0.2&new-version=6.0.3)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`ef68e96`](https://github.com/ghostty-org/ghostty/commit/ef68e96400fd8811b786c2b0e9ab49692eae8bab) macos: fix GHOSTTY_QUICK_TERMINAL not set for quick terminal splits (YuWiz)
- [`4df593b`](https://github.com/ghostty-org/ghostty/commit/4df593bd24675b0f0e14add31825dc8b184cf724) macos: fix GHOSTTY_QUICK_TERMINAL not set for quick terminal splits ([#12896](https://github.com/ghostty-org/ghostty/issues/12896)) ([@bo2themax](https://github.com/bo2themax))
- [`629838b`](https://github.com/ghostty-org/ghostty/commit/629838b9bd050b4708bdd162c115b58874646b34) Update VOUCHED list ([#12906](https://github.com/ghostty-org/ghostty/issues/12906)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12905#discussioncomment-17160340)
  from @jcollie.
  
  Vouch: @c0x0o
  ```

## June 2, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26822901695)  
Summary: 1 runs • 3 commits • 2 authors

### Changes

- [`ab82b8a`](https://github.com/ghostty-org/ghostty/commit/ab82b8ab720ce46183a58a55554e4a4a7423e3f5) core: fix use-after-free in Surface.setSelection ([@jparise](https://github.com/jparise))
  ```text
  setSelection captured the previous selection, then called Screen.select
  (which deinits the previous selection's tracked pins), then compared the
  new selection against the now-freed previous pin via `sel.eql(prev)`.
  That read freed pin memory (use-after-free).
  
  The comparison was a copy-on-select optimization ("only re-copy if the
  selection changed"). Remove it rather than repair it because:
  
  - It never fired correctly. It compared against freed memory, so the
    shipped behavior was already "always copy".
  
  - It can't be repaired by copying `prev`'s pin before Screen.select.
    That fixes the use-after-free but not the logic: the call sites (e.g.
    mouse drag release) pass a selection equal to the one already set, so
    a working `eql` skip would suppress the very copy those sites exist to
    perform. A correct optimization would have to compare against the
    last-copied selection (before the mouse event mutated the live one),
    which would require extra state.
  
  - It isn't worth tracking that additional state. The copy runs once per
    selection gesture (mouse up, double-click), which isn't in a hot path,
    so skipping a redundant re-copy only saves a single clipboard write.
  
  Removing the skip eliminates the use-after-free and keeps the behavior
  consistent with what we've already been doing.
  ```
- [`76b9bdb`](https://github.com/ghostty-org/ghostty/commit/76b9bdb1999398fa1b64d000f9a77088af232b62) terminal: test Screen.select frees existing pins ([@jparise](https://github.com/jparise))
- [`6246c28`](https://github.com/ghostty-org/ghostty/commit/6246c288ae1087c8d67f75432a59da004b30bf25) core: fix use-after-free in Surface.setSelection ([#12894](https://github.com/ghostty-org/ghostty/issues/12894)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `setSelection` captured the previous selection, then called
  `Screen.select` (which deinits the previous selection's tracked pins),
  then compared the new selection against the now-freed previous pin via
  `sel.eql(prev)`. That read freed pin memory (use-after-free).
  
  The comparison was a copy-on-select optimization ("only re-copy if the
  selection changed"). Remove it rather than repair it because:
  
  - It never fired correctly. It compared against freed memory, so the
  shipped behavior was already "always copy".
  
  - It can't be repaired by copying `prev`'s pin before `Screen.select`.
  That fixes the use-after-free but not the logic: the call sites (e.g.
  mouse drag release) pass a selection equal to the one already set, so a
  working `eql` skip would suppress the very copy those sites exist to
  perform. A correct optimization would have to compare against the
  last-copied selection (before the mouse event mutated the live one),
  which would require extra state.
  
  - It isn't worth tracking that additional state. The copy runs once per
  selection gesture (mouse up, double-click), which isn't in a hot path,
  so skipping a redundant re-copy only saves a single clipboard write.
  
  Removing the skip eliminates the use-after-free and keeps the behavior
  consistent with what we've already been doing.
  
  ---
  
  _AI Disclosure_: Claude Opus 4.8 found this in a review while I was
  working on adjacent code.
  ```

## June 1, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26773386588), [2](https://github.com/ghostty-org/ghostty/actions/runs/26770642732)  
Summary: 2 runs • 13 commits • 7 authors

### Changes

- [`d3775d1`](https://github.com/ghostty-org/ghostty/commit/d3775d1ed0a2e41ee8f2ecdb325f6c016b2b3e93) terminal: glyph protocol parser and response encoder ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds the core parse/encode for the still in-development and experimental
  terminal glyph protocol: https://github.com/raphamorim/rio/pull/1542
  Up to version 1.9.
  
  The only cross-cutting change necessary was changing the APC
  identification logic which previously only looked at a single byte to
  support multi-byte identifiers since the glyph protocol uses `25a1`.
  ```
- [`5758e14`](https://github.com/ghostty-org/ghostty/commit/5758e149319d244cbf2d21d1ae8d1376adaf1f91) terminal: glyph protocol parser and response encoder ([#12352](https://github.com/ghostty-org/ghostty/issues/12352)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  **Important: this DOES NOT hook up the glyph protocol to Ghostty or
  libghostty. Its just the parser.**
  
  This adds the core parse/encode for the still in-development and
  experimental terminal glyph protocol:
  https://github.com/raphamorim/rio/pull/1542
  
  The only cross-cutting change necessary was changing the APC
  identification logic which previously only looked at a single byte to
  support multi-byte identifiers since the glyph protocol uses `25a1`.
  
  For DoS protection, the default limits any glyph-related APC command
  size to 1 megabyte.
  
  > [!WARNING]
  >
  > Since this protocol is still in development and discussion, there is
  no promise the implementation will stay within Ghostty or that any of
  the APIs exposed by this will remain stable. We're just getting ahead of
  it.
  ```
- [`024880b`](https://github.com/ghostty-org/ghostty/commit/024880b9ca40ecf8a399deff14e422dd32746f68) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`33adb58`](https://github.com/ghostty-org/ghostty/commit/33adb58bee9eeca906e29ee957140275d4903257) macos: remove unneeded initializers ([@jparise](https://github.com/jparise))
  ```text
  These will be automatically synthesized (they only do memberwise
  initialization) and do not need to be manually defined.
  ```
- [`e32d7ab`](https://github.com/ghostty-org/ghostty/commit/e32d7abe6eeae9c3aa557fef2bcfe97a212688c5) macos: fix swiftlint opening_brace issue ([@jparise](https://github.com/jparise))
- [`3e83a54`](https://github.com/ghostty-org/ghostty/commit/3e83a54d08ef4f4820b8a401910c838f4f0636e0) macos: remove unneeded initializers ([#12875](https://github.com/ghostty-org/ghostty/issues/12875)) ([@bo2themax](https://github.com/bo2themax))
  ```text
  These will be automatically synthesized (they only do memberwise
  initialization) and do not need to be manually defined.
  ```
- [`eb5c1c7`](https://github.com/ghostty-org/ghostty/commit/eb5c1c7220121c8616160e10cb1aa664166a06f3) fix(macos): mark Swift os.Logger interpolations as public ([@claude](https://github.com/claude))
- [`a181c38`](https://github.com/ghostty-org/ghostty/commit/a181c386ca938f730c6e802b7931b37ec65f3047) config: fix missing space in docs ([@masterflitzer](https://github.com/masterflitzer))
  ```text
  fixes #12873
  
  comment/docs only change:
  switched space and tab in default value of `selection-word-chars`
  so there is no space at the value boundary
  needed because markdown trims spaces at the beginning & end
  of a code snippet
  ```
- [`c4c9e94`](https://github.com/ghostty-org/ghostty/commit/c4c9e945aefbd0afbfc21a05f76d06e36e10a625) Update VOUCHED list ([#12880](https://github.com/ghostty-org/ghostty/issues/12880)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12879#issuecomment-4587359428)
  from @00-kat.
  
  Vouch: @masterflitzer
  ```
- [`16f2fdc`](https://github.com/ghostty-org/ghostty/commit/16f2fdc90c2ca59ed870c7b3355a337b1fd650b2) config: fix missing space in docs ([#12879](https://github.com/ghostty-org/ghostty/issues/12879)) ([@jcollie](https://github.com/jcollie))
  ```text
  fixes #12873
  
  comment/docs only change:
  switched space and tab in default value of `selection-word-chars` so
  there is no space at the value boundary
  needed because markdown trims spaces at the beginning & end of a code
  snippet
  ```
- [`0f7cd84`](https://github.com/ghostty-org/ghostty/commit/0f7cd84b880b203c98683e520e84b9db0c5938d8) Update VOUCHED list ([#12889](https://github.com/ghostty-org/ghostty/issues/12889)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12840#discussioncomment-17132417)
  from @bo2themax.
  
  Vouch: @52dyd
  ```
- [`b81670f`](https://github.com/ghostty-org/ghostty/commit/b81670f3f439eff8df615257ff70d9ef39e60065) macOS: mark Swift os.Logger interpolations as public ([#12877](https://github.com/ghostty-org/ghostty/issues/12877)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ### AI Disclosure
  
  Claude implemented it. I'm fully aware of and confident about the
  change; it's just chore work actually.
  ```
- [`43e0340`](https://github.com/ghostty-org/ghostty/commit/43e03401758e8e1e0d23afb3a8e2a00b43e8e8ee) Update iTerm2 colorschemes ([#12867](https://github.com/ghostty-org/ghostty/issues/12867)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260525-155808-7335c0a
  ```

