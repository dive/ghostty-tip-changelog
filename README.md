> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: June 11, 2026 at 18:59 UTC.

## June 10, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/27282569352)  
Summary: 1 runs • 1 commits • 1 authors

### Changes

- [`5659cef`](https://github.com/ghostty-org/ghostty/commit/5659cef41f4f2f7a478d0800a11836fa17e64d66) Update VOUCHED list ([#12978](https://github.com/ghostty-org/ghostty/issues/12978)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12977#discussioncomment-17251869)
  from @jcollie.
  
  Vouch: @jamesarch
  ```

## June 8, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/27142450381), [2](https://github.com/ghostty-org/ghostty/actions/runs/27113839529)  
Summary: 2 runs • 7 commits • 4 authors

### Changes

- [`3263ce5`](https://github.com/ghostty-org/ghostty/commit/3263ce5122480fe4d59a1189f67a3aac65949aa1) terminal: support click_events=2 ([@alexbathome](https://github.com/alexbathome))
- [`97777cf`](https://github.com/ghostty-org/ghostty/commit/97777cf5a32fd8943ab5c15d6ccee709a15943b4) fix: fix tests, change enum fields to lowercase ([@alexbathome](https://github.com/alexbathome))
- [`3ba5e9c`](https://github.com/ghostty-org/ghostty/commit/3ba5e9c24390412fb1dbb08c51008f1efdcff97b) Update VOUCHED list ([#12958](https://github.com/ghostty-org/ghostty/issues/12958)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12954#discussioncomment-17215965)
  from @pluiedev.
  
  Vouch: @alexbathome
  ```
- [`fd882c6`](https://github.com/ghostty-org/ghostty/commit/fd882c67cc3d95e9cc7fd837f33fbd0ef64017c4) pr review: added saturated arithmetic ([@alexbathome](https://github.com/alexbathome))
- [`69095e2`](https://github.com/ghostty-org/ghostty/commit/69095e298ab88bb0eb5ba541f4c505f2c22d07f5) terminal: support click_events=2 ([#12953](https://github.com/ghostty-org/ghostty/issues/12953)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  ## Context
  
  Implements the OSC 133 `click_events=2` such that click events on the
  terminal are sent to the shell where the y coordinate is sent relative
  to the prompt pin.
  
  See
  https://sw.kovidgoyal.net/kitty/shell-integration/#click_events=1|2:~:text=click%5Fevents,xterm
  further detailed explanation.
  
  This should close https://github.com/ghostty-org/ghostty/issues/10865
  
  ### Testing
  
  I did some basic manual testing here via the following:
  ```
  ghostty  main
  ❯ printf '\033]133;A;click_events=1\007' && cat
  ^[[<0;49;4M^[[<0;48;8M^[[<0;47;12M^C
  
  ghostty  main  5s
  ❯ printf '\033]133;A;click_events=2\007' && cat
  ^[[<0;50;1M^[[<0;49;4M^[[<0;48;9M^[[<0;48;14M^C
  ```
  
  #### Notes
  
  This is my first Ghostty PR. All code here is hand-rolled, AI was used
  to do "smart" code searches/point me in the right direction.
  
  I'm actively trying to learn Zig, Ghostty, and get more involved with
  the community here so I'm avoiding obtuse usage of AI where possible.
  
  Any feedback or tips are more than welcome! Thank you! :pray:
  ````
- [`002fd41`](https://github.com/ghostty-org/ghostty/commit/002fd41429036e973d7257174f40bc1e3106ceb7) lib-vt: add pwd_changed callback for OSC 7/9/1337 (Zongyuan Li)
  ```text
  Previously the libghostty-vt stream handler dropped .report_pwd as a
  no-op, so embedders never saw shell-reported cwd changes and the
  terminal's pwd field was never populated from escape sequences.
  
  Wire the action to setPwd and expose a pwd_changed callback analogous
  to title_changed via GHOSTTY_TERMINAL_OPT_PWD_CHANGED. The payload is
  passed through unparsed; embedders read it with ghostty_terminal_get
  and decode any URI scheme themselves.
  ```
- [`2ba5e6b`](https://github.com/ghostty-org/ghostty/commit/2ba5e6b92963c9c9470fb30338989bb38fa11857) lib-vt: add pwd_changed callback for OSC 7/9/1337 ([#12956](https://github.com/ghostty-org/ghostty/issues/12956)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously the libghostty-vt stream handler dropped .report_pwd as a
  no-op, so embedders never saw shell-reported cwd changes and the
  terminal's pwd field was never populated from escape sequences.
  
  Wire the action to setPwd and expose a pwd_changed callback analogous to
  title_changed via GHOSTTY_TERMINAL_OPT_PWD_CHANGED. The payload is
  passed through unparsed; embedders read it with ghostty_terminal_get and
  decode any URI scheme themselves.
  
  This is proposed in
  [discussion#12927](https://github.com/ghostty-org/ghostty/discussions/12927)
  ```

## June 6, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/27074213689), [2](https://github.com/ghostty-org/ghostty/actions/runs/27050927493)  
Summary: 2 runs • 7 commits • 2 authors

### Changes

- [`7777ded`](https://github.com/ghostty-org/ghostty/commit/7777dedd5f35ebbca89edf9dfdfe65b4a071d831) gtk: add "Close Split" to right-click context menu ([@cmwetherell](https://github.com/cmwetherell))
  ```text
  Add a "Close Split" option to the split submenu in the right-click
  context menu, allowing users to close the focused split pane directly
  from the context menu.
  ```
- [`4885a53`](https://github.com/ghostty-org/ghostty/commit/4885a53a98386da8b8e1c1cbff54e435d2c0dab3) gtk: rename close-pane to close-split ([@cmwetherell](https://github.com/cmwetherell))
  ```text
  Rename internal action and function from close-pane/actionClosePane
  to close-split/actionCloseSplit for consistency with the UI label.
  ```
- [`247280f`](https://github.com/ghostty-org/ghostty/commit/247280fdbd453d8fd8157ada3a0232789a391802) gtk: regenerate translations for close-split menu item ([@cmwetherell](https://github.com/cmwetherell))
- [`bcf1293`](https://github.com/ghostty-org/ghostty/commit/bcf12937d09d60ce23e46fd5a1851dfb3bb5e61c) Merge remote-tracking branch 'origin/main' into close-split-gtk ([@cmwetherell](https://github.com/cmwetherell))
  ```text
  # Conflicts:
  #	po/hu.po
  #	po/id.po
  ```
- [`7092b39`](https://github.com/ghostty-org/ghostty/commit/7092b39445bebfd3178f562eb9e5fa9a95a32332) GTK: Improve Split Close Behavior ([#11173](https://github.com/ghostty-org/ghostty/issues/11173)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Summary
  - Adds a "Close Split" option to the right-click context menu in the
  split submenu
  - Allows users to close the focused split pane directly from the context
  menu
  
  Reference discussion:
  https://github.com/ghostty-org/ghostty/discussions/10982
  ```
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

