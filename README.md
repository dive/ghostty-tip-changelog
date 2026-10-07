> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: October 7, 2026 at 00:18 UTC.

## October 6, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/37542529824), [2](https://github.com/ghostty-org/ghostty/actions/runs/37515317220), [3](https://github.com/ghostty-org/ghostty/actions/runs/37510349661), [4](https://github.com/ghostty-org/ghostty/actions/runs/37392894640)  
Summary: 4 runs • 8 commits • 4 authors

### Changes

- [`bae2c3c`](https://github.com/ghostty-org/ghostty/commit/bae2c3cdbf73f2ac33a67e4b0b7811165f0f62d4) libghostty-vt: program status protocol (OSC 7501) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds support for OSC 7501, the program status protocol. A program
  uses it to tell the terminal what it is doing (idle, working, done,
  blocked on the user, or failed) and why.
  
  The terminal doesn't keep records itself, the same as OSC 9;4. The
  embedder keeps one record per id and applies the spec's lifetime rules.
  A full reset reports a clear of every record. The terminal only answers
  the support query (`OSC 7501 ; ?`) while the effect is set, so programs
  don't send reports that nothing reads. The Ghostty app ignores these
  reports for now.
  
  References:
  
  - Program Status Protocol (OSC 7501) specification:
    https://www.superlogical.com/rex/docs/build/program-status
  ```
- [`a4aacd9`](https://github.com/ghostty-org/ghostty/commit/a4aacd918ba9e79929ff608034c60a4341773ef0) libghostty-vt: program status protocol (OSC 7501) ([#14560](https://github.com/ghostty-org/ghostty/issues/14560)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds support for OSC 7501, the program status protocol. A program
  uses it to tell the terminal what it is doing (idle, working, done,
  blocked on the user, or failed) and why.
  
  OSC7501 is the first net-new terminal specification to be pioneered by
  the Ghostty project. In full transparency, this work was motivated by my
  work on Superlogical, but the specification was carefully written in a
  way that doesn't bias towards that use case. The specification is
  broadly useful across a wide variety of applications. I also distributed
  the specification with a diverse group of application and terminal
  developers to solicit feedback.
  
  The terminal doesn't keep records itself, the same as OSC 9;4. The
  embedder keeps one record per id and applies the spec's lifetime rules.
  A full reset reports a clear of every record. The terminal only answers
  the support query (`OSC 7501 ; ?`) while the effect is set, so programs
  don't send reports that nothing reads. The Ghostty app ignores these
  reports for now.
  
  References:
  
  - Program Status Protocol (OSC 7501) specification:
  https://gist.github.com/mitchellh/7acae3abd8355c1c00287d67e96c913a
  ```
- [`13b5ab2`](https://github.com/ghostty-org/ghostty/commit/13b5ab2041fe866e9b448697cd8485b115c32ba2) terminal: stop line selection at prompt boundaries across blank cells ([@fornwall](https://github.com/fornwall))
  ```text
  Selecting a span of blank cells or whitespace between OSC 133 semantic
  boundaries could pull in neighboring prompt text and reverse the
  selection endpoints.
  
  The whitespace trims iterate with a `CellIterator` bounded by the end
  pin, but the iterator bounds only the row, so the trim ran past the end
  column into the next prompt.
  ```
- [`6220a36`](https://github.com/ghostty-org/ghostty/commit/6220a36172ec4558b308b317ac9a7b1e0960cb50) terminal: print codepoints above 0xFF unmapped in a charset, as xterm ([@robmorgan](https://github.com/robmorgan))
  ```text
  With a charset other than UTF-8 or ASCII designated (the DEC
  line-drawing set, say), printCell mapped every codepoint above 0xFF to
  a space. An emoji printed in that state became a blank, and since its
  width still came from the original codepoint, a two-column one, so the
  rest of the row shifted too.
  
  A designated set only applies to the range it is invoked into: G0 is
  invoked into GL (0x21-0x7E), so codepoints outside it pass through
  unchanged (DEC STD 070, following ISO 2022; xterm does the same). The
  charset tables already only remap codepoints in GL, so printCell now
  prints anything above 0xFF as is instead of replacing it with a space.
  ```
- [`4611e04`](https://github.com/ghostty-org/ghostty/commit/4611e04ff63c50f71b3e951c4015cfae416cb40d) terminal: print codepoints above 0xFF unmapped in a charset, as xterm ([#14554](https://github.com/ghostty-org/ghostty/issues/14554)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  With a charset other than UTF-8 or ASCII designated (e.g. the DEC
  line-drawing set), `printCell` mapped every codepoint above `0xFF` to a
  space. An emoji printed in that state became a blank, and since its
  width still came from the original codepoint (a two-column one), so the
  rest of the row shifted too.
  
  A designated set only applies to the range it is invoked into: G0 is
  invoked into GL (`0x21`–`0x7E`), so codepoints outside it should pass
  through unchanged (DEC STD 070, following ISO 2022 - I checked and xterm
  behaves the same way). Ghostty's charset tables already only remap
  codepoints in GL, so `printCell` now prints anything above `0xFF` as is
  instead of replacing it with a space.
  
  To reproduce, run this inside a current build:
  ```sh
  printf '\e(0`\U0001F600a\e(B\n'
  ```
  
  **Old**
  <img width="585" height="82" alt="image"
  src="https://github.com/user-attachments/assets/4df6c46f-eaf1-459a-b7c2-2e175bbca6ed"
  />
  
  **New**
  <img width="323" height="58" alt="image"
  src="https://github.com/user-attachments/assets/d618502b-e44f-4243-b4b4-8c76e079b88d"
  />
  
  AI disclosure: Created with help from Claude Code using Opus 5.5.
  Iterated on, manually tested, and reviewed by me.
  ````
- [`ca2356f`](https://github.com/ghostty-org/ghostty/commit/ca2356fa05bedefacfc30a71d93ee899aaedb998) terminal: stop line selection at prompt boundaries across blank cells ([#14553](https://github.com/ghostty-org/ghostty/issues/14553)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Selecting a span of blank cells or whitespace between [OSC 133 semantic
  boundaries](https://gitlab.freedesktop.org/Per_Bothner/specifications/-/blob/master/proposals/semantic-prompts.md)
  could pull in neighboring prompt text and reverse the selection
  endpoints. The whitespace trims iterate with a `CellIterator` bounded by
  the end pin, but the iterator bounds only the row, so the trim ran past
  the end column into the next prompt.
  
  To reproduce: Run this script and triple-click either blank cell between
  `x` and `m` on the first row. Before the fix, the selection reaches into
  the neighboring prompt text; after the fix, nothing is selected (like
  triple-clicking a blank row).
  
  ```sh
  #!/bin/sh
  # On exit:
  # \033]133;C\007  Switch back to command-output mode (OSC 133;C).
  # \033[?1049l     Leave the alternate screen and restore the original screen.
  trap 'printf "\033]133;C\007\033[?1049l"' 0
  
  # \033[?1049h     Enter the alternate screen, preserving the original screen.
  # \033]133;C\007  Mark subsequent text as command output (OSC 133;C).
  # \033[2J        Clear the visible screen, leaving unwritten output cells.
  # \033[H         Move the cursor to the top-left corner.
  printf '\033[?1049h\033]133;C\007\033[2J\033[H'
  
  # \033]133;A\007  Mark the start of a prompt (OSC 133;A).
  # x              Print a prompt cell in column 1.
  # \033[2C        Move right two columns, leaving two unwritten output cells.
  # m              Print another prompt cell in column 4.
  # \033]133;C\007  Switch back to command-output mode (OSC 133;C).
  printf '\033]133;A\007x\033[2Cm\033]133;C\007'
  
  # Wait for Enter while you test selection; the exit trap restores the screen.
  read -r _
  ```
  
  AI disclosure: Initially created with the help of gpt-6 astra in codex.
  Iterated on, reviewed and tested by me.
  ````
- [`2febd01`](https://github.com/ghostty-org/ghostty/commit/2febd0116dab28df8beb00e4a3453022fe8f3c16) Update VOUCHED list ([#14566](https://github.com/ghostty-org/ghostty/issues/14566)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14563#discussioncomment-18782495)
  from @jcollie.
  
  Vouch: @magnussp
  ```
- [`c3203ea`](https://github.com/ghostty-org/ghostty/commit/c3203ea4b169a18eb2ccfe92847e426d8afea858) Update VOUCHED list ([#14550](https://github.com/ghostty-org/ghostty/issues/14550)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14549#discussioncomment-18767762)
  from @jcollie.
  
  Vouch: @robmorgan
  ```

## October 5, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/37273745638), [2](https://github.com/ghostty-org/ghostty/actions/runs/37265526133)  
Summary: 2 runs • 4 commits • 4 authors

### Changes

- [`140feb8`](https://github.com/ghostty-org/ghostty/commit/140feb86ae4594472607859b75167889de0c13da) renderer: always release shaders when the render thread exits (Anonymous)
  ```text
  Since #14052, shaders are only freed by releaseGpuResources while the
  display is unrealized, and only the GTK apprt unrealizes. The macOS
  apprt never does, so each closed surface leaked its five render
  pipelines and shader library.
  
  threadExit now marks the display unrealized before releasing GPU
  resources. This frees the shaders and stops any later draw from
  rebuilding resources after the render thread is gone.
  ```
- [`35a81a9`](https://github.com/ghostty-org/ghostty/commit/35a81a980bb9fce09a1ea762a68b55f8eb3477ed) renderer: always release shaders  ([#14542](https://github.com/ghostty-org/ghostty/issues/14542)) ([@pluiedev](https://github.com/pluiedev))
  ```text
  shaders are only fread by releaseGpuResources while the display is
  unrealized and only the gtk apprt unrealizes. The mac apprt never does
  automatically so each closed surface leaked its five render pipelines
  and shader library. Updated so threadExit now marks the display
  unrealized before releasing GPU resources.
  ```
- [`157c44f`](https://github.com/ghostty-org/ghostty/commit/157c44f643c9209e31bb92f4c2c4bcec9c6d23d5) input: UTF-8 encode the button in 1005 mouse reports ([@fornwall](https://github.com/fornwall))
  ```text
  In UTF-8 mouse mode (DECSET 1005) the button value was written as a
  single raw byte. xterm encodes it as UTF-8 like the coordinates, so
  values from 128 (buttons 8 and 9) take two bytes. The raw byte made
  the report invalid UTF-8.
  ```
- [`b094a6b`](https://github.com/ghostty-org/ghostty/commit/b094a6ba31825aec1b2beaae54686b4a31f98a8a) input: UTF-8 encode the button in 1005 mouse reports ([#14532](https://github.com/ghostty-org/ghostty/issues/14532)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fix UTF-8 mouse reporting (DECSET 1005) to UTF-8 encode the button
  value, as required by [xterm’s
  specification](https://invisible-island.net/xterm/ctlseqs/ctlseqs.html#h3-Extended-coordinates).
  
  Previously, buttons 8 and 9 (back/forward) produced a raw byte of `0xA0`
  or `0xA1`, making the report invalid UTF-8. For example, pressing button
  8 at column 1, row 1 produced:
  
  - Before: `b'\x1b[M\xa0!!'`
  - After: `b'\x1b[M\xc2\xa0!!'`
  
  AI disclosure: Initially created with claude code using opus 5.5.
  Iterated on, reviewed and tested manually by me.
  ```

## October 4, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/37206958649), [2](https://github.com/ghostty-org/ghostty/actions/runs/37206425565), [3](https://github.com/ghostty-org/ghostty/actions/runs/37167192678)  
Summary: 3 runs • 23 commits • 5 authors

### Changes

- [`e6db5b6`](https://github.com/ghostty-org/ghostty/commit/e6db5b633a9ae820fea1620af52dbf87cc7e430c) terminal: fix crash after shrinking columns splits a wide char ([@fornwall](https://github.com/fornwall))
  ```text
  Narrowing without reflow cleared only the cells past the new width, so a
  wide char whose spacer tail was cut kept its head in the new last column.
  Every operation pairing a head with the cell after it then reached past
  the row end: insertBlanks and eraseLine(.left) panic in Screen.clearCells,
  and rowWillBeShifted writes cells[cols].
  
  Clear the orphaned head along with the cut columns.
  ```
- [`5dc28bb`](https://github.com/ghostty-org/ghostty/commit/5dc28bb8eebaf57a6c793a406bfea8c632d4fa94) terminal: fix crash after shrinking columns splits a wide char ([#14509](https://github.com/ghostty-org/ghostty/issues/14509)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Narrowing the terminal without reflow (wraparound off, or the alternate
  screen) can cut a wide char in half, leaving its head in the last column
  with no spacer tail.
  
  Later edits on that row (e.g.
  [ICH](https://ghostty.org/docs/vt/csi/ich)) then clear the missing tail
  too, reaching one cell past the row end, which leads to a bounds
  assertion failure in safe builds or an out-of-bounds write otherwise.
  
  To reproduce, run the below script inside a safe build:
  
  ```sh
  #!/bin/sh
  printf '\e[?40h\e[?3h'       # allow DECCOLM, switch to 132 columns
  printf '\e[?47h\e[1;80H一'   # alternate screen: wide char in columns 80-81
  printf '\e[?47l\e[?3l'       # back to 80 columns (alternate screen shrinks without reflow)
  printf '\e[?47h\e[1;80H\e[@' # alternate screen: insert a blank at the last column
  printf '\e[2;1Hsurvived\n'
  ```
  
  - Before: Triggers assertion in `Screen.clearCells`.
  - After: Prints `survived`, column 80 is blank.
  
  AI disclosure: Created with claude code using opus 5.5. Iterated on and
  reviewed by me.
  ````
- [`9272a2f`](https://github.com/ghostty-org/ghostty/commit/9272a2f7c24a9282541dba8a3b361ae98bde81bc) terminal: support DECRQCRA and XTCHECKSUM ([@jcollie](https://github.com/jcollie))
  ```text
  Programs such as terminal test suites use DECRQCRA to check what is on
  the screen. Since it also lets any program read the screen back, it is
  off unless vt-xt-checksum-report is set.
  ```
- [`00a19db`](https://github.com/ghostty-org/ghostty/commit/00a19db51aeee5253c83fecc5b647c0358573b5f) config: add vt-xt-checksum-extension ([@jcollie](https://github.com/jcollie))
  ```text
  RIS resets the DECRQCRA checksum calculation, so a program like
  esctest that needs xterm's other calculations had no way to keep it.
  This is the equivalent of xterm's checksumExtension resource.
  ```
- [`7e2d179`](https://github.com/ghostty-org/ghostty/commit/7e2d1793da7f3e1d00b27abe5fe03bb04a0fb474) lib-vt: add GHOSTTY_TERMINAL_OPT_XT_CHECKSUM_EXTENSION ([@jcollie](https://github.com/jcollie))
  ```text
  Embedders had no way to choose the DECRQCRA checksum calculation that
  survives RIS, which vt-xt-checksum-extension gives the app.
  ```
- [`25b04b4`](https://github.com/ghostty-org/ghostty/commit/25b04b410463b97dbc91ec4d24da500a66f4b962) lib-vt: export xt_checksum and device_attributes ([@jcollie](https://github.com/jcollie))
  ```text
  Zig users couldn't name the types needed to set a default checksum or
  answer device attribute queries.
  ```
- [`edcaf66`](https://github.com/ghostty-org/ghostty/commit/edcaf66707f1164030872c0d7a463035af9fc29a) test/esctest: enable DECRQCRA ([@jcollie](https://github.com/jcollie))
  ```text
  esctest reads the screen back with DECRQCRA, so every test that checks
  screen contents failed while the runner left it off.
  ```
- [`cc02767`](https://github.com/ghostty-org/ghostty/commit/cc02767783543f53420c0adf139b5fe6b2471a78) terminal: link to xterm's checksum implementation ([@jcollie](https://github.com/jcollie))
  ```text
  The checksum is modeled on xterm's, so point at its source for comparison.
  ```
- [`5f0d4fe`](https://github.com/ghostty-org/ghostty/commit/5f0d4febc3ac8686ac911aa4a209a4e3d8a48131) terminal: use a rectangle selection for DECRQCRA ([@jcollie](https://github.com/jcollie))
  ```text
  The checksum had its own rectangle type and row walk, duplicating what
  Selection and the pin iterators already provide.
  ```
- [`b2f557c`](https://github.com/ghostty-org/ghostty/commit/b2f557c6c142a5787774c59dd8cb88a58fabc5d0) terminal: inline the checksum test helper ([@jcollie](https://github.com/jcollie))
  ```text
  Each test now shows the selection and flags it checks directly.
  ```
- [`01b9f49`](https://github.com/ghostty-org/ghostty/commit/01b9f4958d9d952cdbbe2473c31dfc7695d3c421) terminal: link to xterm's checksumExtension source ([@jcollie](https://github.com/jcollie))
  ```text
  xterm's documentation for these bits disagrees with its code, so
  point at both to show which one the flags follow.
  ```
- [`e8b858c`](https://github.com/ghostty-org/ghostty/commit/e8b858cc66971aa55376866b149fe304e958fc3b) terminal/tmux: don't count unstored bytes against max_bytes ([@jcollie](https://github.com/jcollie))
  ```text
  A line that filled the control mode buffer exactly couldn't be
  terminated: the newline ending a notification or block, and the '%'
  starting the next notification, were rejected as exceeding the limit
  even though none of them are stored. The parser then broke and dropped
  all further control mode output.
  
  Fixes #11935
  ```
- [`e55c687`](https://github.com/ghostty-org/ghostty/commit/e55c687a4bdf46a4a7a9f51f040798fc11e62154) input: encode ctrl+alt+shift+backspace in legacy mode ([@fornwall](https://github.com/fornwall))
  ```text
  The legacy backspace table, taken from foot's keymap.h, was missing
  foot's Shift+Alt+Ctrl row. The chord fell through to the unmodified
  entry and sent a bare DEL (BS under DECBKM), dropping both the Alt
  prefix and Ctrl. Send ESC BS like Alt+Ctrl and Shift+Alt+Ctrl+Super.
  ```
- [`82ae67b`](https://github.com/ghostty-org/ghostty/commit/82ae67b9f41a009b131f4e336895cb2cce299dfd) libghostty: document allocator alignment as a bit count ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  The alloc callback's alignment was documented as a power of two between
  1 and 16, but every vtable call passes @intFromEnum of a
  std.mem.Alignment: the number of low address bits that must be zero,
  not a byte count. An allocator written to the header would align a
  16-byte request to 4 bytes. The range was also wrong: snapshot export
  asks the terminal's allocator for page-aligned memory through
  pagePreservingState.
  
  Document the encoding the implementation already uses, with examples.
  ```
- [`406f2e5`](https://github.com/ghostty-org/ghostty/commit/406f2e54401978ad0bbf312b465554465b901f4e) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`ac2ae69`](https://github.com/ghostty-org/ghostty/commit/ac2ae69e08690a6da4e92d61728da4513674bd4b) Update iTerm2 colorschemes ([#14527](https://github.com/ghostty-org/ghostty/issues/14527)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260928-151043-99d9701
  ```
- [`3425025`](https://github.com/ghostty-org/ghostty/commit/3425025e585a3403340d4dc6d65132f42e05e605) libghostty: document allocator alignment as log2 ([#14515](https://github.com/ghostty-org/ghostty/issues/14515)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The header says alignment is a power of two from 1 to 16:
  
  https://github.com/ghostty-org/ghostty/blob/83edd491e3024ae5e50393d62877b8897da1cccd/include/ghostty/vt/allocator.h#L113-L114
  
  It's actually the log2, since we pass @intFromEnum of a
  std.mem.Alignment, which stores the exponent (@"16" = 4):
  
  https://github.com/ghostty-org/ghostty/blob/83edd491e3024ae5e50393d62877b8897da1cccd/src/lib/allocator.zig#L99
  https://ziglang.org/documentation/0.16.0/std/#std.mem.Alignment
  
  So a C allocator written to the header aligns a 16-byte request to 4
  bytes.
  
  The 1–16 range is wrong too. Snapshot export asks the terminal's
  allocator for page-aligned memory:
  
  https://github.com/ghostty-org/ghostty/blob/83edd491e3024ae5e50393d62877b8897da1cccd/src/terminal/snapshot/history.zig#L182
  
  https://github.com/ghostty-org/ghostty/blob/83edd491e3024ae5e50393d62877b8897da1cccd/src/terminal/PageList.zig#L175-L178
  
  cc @pluiedev cuz i ruberducked the doc change with her.
  ```
- [`eee709f`](https://github.com/ghostty-org/ghostty/commit/eee709f5d3f1030cde981233ec75bfa940cd843f) input: encode ctrl+alt+shift+backspace in legacy mode ([#14508](https://github.com/ghostty-org/ghostty/issues/14508)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  In legacy key encoding, `Ctrl+Alt+Shift+Backspace` sent a bare DEL
  (`0x7f`), the same as plain Backspace.
  
  The backspace table in `function_keys.zig`, which [its header
  says](https://github.com/ghostty-org/ghostty/blob/33da6848d63b3bba2b4f31ab1531d618f2795192/src/input/function_keys.zig#L6-L7)
  is mostly based on foot's `keymap.h`, was missing [foot's Shift+Alt+Ctrl
  row](https://codeberg.org/dnkl/foot/src/commit/cb2771788998f6a6288e2de8273c55a8214551e0/keymap.h#L109).
  With this change it sends `ESC BS` (`\x1b\x08`), matching xterm.
  
  To reproduce, run:
  
  ```sh
  python3 -c 'import os,tty,termios;a=termios.tcgetattr(0);tty.setraw(0);b=os.read(0,16);termios.tcsetattr(0,termios.TCSADRAIN,a);print(repr(b))'
  ```
  
  Then press **Ctrl+Alt+Shift+Backspace** (Option for Alt on macOS).
  
  | | Output |
  |---|---|
  | Before | `b'\x7f'` |
  | After | `b'\x1b\x08'` |
  
  For comparison, Ctrl+Alt+Backspace prints `b'\x1b\x08'` both before and
  after.
  
  AI disclosure: Created with claude code using opus 5.5. Iterated on and
  reviewed by me.
  ````
- [`2fb0c9c`](https://github.com/ghostty-org/ghostty/commit/2fb0c9cacb3fc75dbc8aedee9b7ed4321f091d33) terminal/tmux: don't count unstored bytes against max_bytes ([#14503](https://github.com/ghostty-org/ghostty/issues/14503)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A line that filled the control mode buffer exactly couldn't be
  terminated: the newline ending a notification or block, and the '%'
  starting the next notification, were rejected as exceeding the limit
  even though none of them are stored. The parser then broke and dropped
  all further control mode output.
  
  Fixes #11935
  
  AI disclosure: Claude Code assisted in the development of this PR.
  ```
- [`04d685c`](https://github.com/ghostty-org/ghostty/commit/04d685c6aa54b27a11fd547a9ac62cd97fdd5ee6) terminal: add suport for DECRQCRA and XTCHECKSUM ([#14483](https://github.com/ghostty-org/ghostty/issues/14483)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  DECRQCRA and XTCHECKSUM are used to inspect cells on the running
  terminal. They are mainly useful in conformance tests that verify that
  other control sequences are doing the right thing. Since these control
  sequences could be used to read the entire contents of the screen, they
  are disabled by default (see the `vt-checksum-report` config).
  
  Enabling these fix many of the failing `esctest2` tests.
  
  AI disclosure: Claude Code was used to develop this PR but I have
  thoroughly reviewed the code.
  ```
- [`aca9bf0`](https://github.com/ghostty-org/ghostty/commit/aca9bf031821c1b9dedfec24e93fb609468a274f) libghostty-vt: zero the decode_png output before the callback ([@mitchellh](https://github.com/mitchellh))
  ```text
  For C embedders this was harmless but for embedders in garbage-collected
  languages like Go it isn't because it has a pointer field and in Go,
  storing a pointer into C memory requires that memory to be initialized first,
  because the collector also looks at the value being overwritten. If the
  leftover stack bytes happened to look like a Go heap address, the process
  would abort.
  
  And surprise surprise, around 1 in ~24,000 test runs on my Mac Studio at
  home was able to trigger this in my Go bindings.
  
  References:
  
  - cgo, "Passing pointers": C memory must be initialized before Go code
    stores a pointer into it.
    https://pkg.go.dev/cmd/cgo#hdr-Passing_pointers
  ```
- [`0e0ff28`](https://github.com/ghostty-org/ghostty/commit/0e0ff282f72c92d930d41f4703547d3bc9618ba2) libghostty-vt: zero the decode_png output before the callback ([#14530](https://github.com/ghostty-org/ghostty/issues/14530)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  For C embedders this was harmless but for embedders in garbage-collected
  languages like Go it isn't because it has a pointer field and in Go,
  storing a pointer into C memory requires that memory to be initialized
  first, because the collector also looks at the value being overwritten.
  If the leftover stack bytes happened to look like a Go heap address, the
  process would abort.
  
  And surprise surprise, around 1 in ~24,000 test runs on my Mac Studio at
  home was able to trigger this in my Go bindings.
  
  References:
  
  - cgo, "Passing pointers": C memory must be initialized before Go code
  stores a pointer into it.
  https://pkg.go.dev/cmd/cgo#hdr-Passing_pointers
  ```
- [`f96c971`](https://github.com/ghostty-org/ghostty/commit/f96c9711b9f72ecf75e0fd50f3434529b4dea5b6) Update VOUCHED list ([#14528](https://github.com/ghostty-org/ghostty/issues/14528)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12713#discussioncomment-18737824)
  from @jcollie.
  
  Vouch: @maddythewisp
  ```

## October 3, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/37132099399)  
Summary: 1 runs • 3 commits • 2 authors

### Changes

- [`6fbb560`](https://github.com/ghostty-org/ghostty/commit/6fbb560cd3bff42fe06af60aef320526b62a8004) cli: include the port in the ssh-terminfo cache key ([@stepankandrushin](https://github.com/stepankandrushin))
  ```text
  The ssh-terminfo cache keyed destinations as user@hostname from `ssh -G`,
  ignoring the port. Two machines behind one address on different ports
  (e.g. user@host:2221 and user@host:2218) shared a key, so once the first
  was cached the terminfo install was skipped for the second, which still
  got TERM=xterm-ghostty without the terminfo installed.
  
  The key now carries the port when it isn't 22: user@host:port, or
  user@[addr]:port for IPv6. Port 22 keeps the old user@host form, so
  existing caches stay valid.
  
  `+ssh-cache` accepts the new form: a bare `host` query matches that host
  on every port, a bare `host:port` query that port for any user, and
  `user@host:port` one exact entry.
  
  AI disclosure: the cause was found and the patch written with Claude
  Code (Claude Opus 5.5). Reviewed and tested by me.
  ```
- [`dfd7baf`](https://github.com/ghostty-org/ghostty/commit/dfd7bafcd3a0c34a0557f68c383bb56486a62eab) cli: address review feedback on the ssh-cache port ([@stepankandrushin](https://github.com/stepankandrushin))
  ```text
  - matchesQuery treats a missing port as port 22.
  - isValidPort uses std.ascii.isDigit and rejects leading zeros, so
    host:22 and host:022 can't become distinct keys.
  ```
- [`befcdfd`](https://github.com/ghostty-org/ghostty/commit/befcdfd2c3a1cb24d9ec886e93c95b2b5daa7028) cli: include the port in the ssh-terminfo cache key ([#14472](https://github.com/ghostty-org/ghostty/issues/14472)) ([@jparise](https://github.com/jparise))
  ```text
  The ssh-terminfo cache keyed destinations as user@hostname from `ssh
  -G`, ignoring the port. Two machines behind one address on different
  ports (e.g. user@host:2221 and user@host:2218) shared a key, so once the
  first was cached the terminfo install was skipped for the second, which
  still got TERM=xterm-ghostty without the terminfo installed.
  
  The key now carries the port when it isn't 22: user@host:port, or
  user@[addr]:port for IPv6. Port 22 keeps the old user@host form, so
  existing caches stay valid.
  
  `+ssh-cache` accepts the new form: a bare `host` query matches that host
  on every port, a bare `host:port` query that port for any user, and
  `user@host:port` one exact entry.
  
  AI disclosure: the cause was found and the patch written with Claude
  Code (Claude Opus 5.5). Reviewed and tested by me.
  
  Discussed in #14465.
  ```

## October 2, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/37078509089), [2](https://github.com/ghostty-org/ghostty/actions/runs/37067831678), [3](https://github.com/ghostty-org/ghostty/actions/runs/37023207104)  
Summary: 3 runs • 6 commits • 3 authors

### Changes

- [`822e842`](https://github.com/ghostty-org/ghostty/commit/822e84272f60e320526e6c2c223ccdf786d334c9) Update VOUCHED list ([#14522](https://github.com/ghostty-org/ghostty/issues/14522)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14066#discussioncomment-18724022)
  from @jcollie.
  
  Vouch: @moonward
  ```
- [`f5a7f70`](https://github.com/ghostty-org/ghostty/commit/f5a7f706f0ef8751b9f47397b1c12880572b2330) Update VOUCHED list ([#14520](https://github.com/ghostty-org/ghostty/issues/14520)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14517#discussioncomment-18722576)
  from @pluiedev.
  
  Denounce: @davidpmclaughlin
  ```
- [`1360297`](https://github.com/ghostty-org/ghostty/commit/136029788c13c8bff81506571ab0009dcc095da2) macos: honor window-save-state=never for restorable windows ([@BarutSRB](https://github.com/BarutSRB))
  ```text
  Normal terminal windows remain eligible for native AppKit restoration
  when window-save-state is never, allowing background window snapshots
  to contend with window updates.
  
  Apply the setting when creating a terminal window and assign its
  restoration class and identifier only when restoration is enabled.
  ```
- [`934ef81`](https://github.com/ghostty-org/ghostty/commit/934ef81401f0c0d27740c44810eede26011a18da) macos: update window restoration on config reload ([@BarutSRB](https://github.com/BarutSRB))
  ```text
  Existing terminal windows retained their creation-time restoration
  policy after configuration changes.
  
  Refresh that policy on global config reload and share setup with window
  creation, preserving the custom-command exclusion.
  ```
- [`0e75d01`](https://github.com/ghostty-org/ghostty/commit/0e75d015fe085772b8ecffdba672b60c04af73fe) macos: simplify window restoration setup ([@BarutSRB](https://github.com/BarutSRB))
  ```text
  Let isRestorable control preservation while assigning the restoration
  class and identifier consistently for every terminal window.
  
  Remove the restoration test fixture that creates AppKit windows and
  broadcasts configuration changes through the shared test host.
  ```
- [`f523504`](https://github.com/ghostty-org/ghostty/commit/f523504ea5c9f41d150d1eb93cc7a748b90f9361) macos: honor window-save-state=never for restorable windows ([#14506](https://github.com/ghostty-org/ghostty/issues/14506)) ([@bo2themax](https://github.com/bo2themax))
  ```text
  With `window-save-state = never`, normal terminal windows are still
  marked `isRestorable`. Ghostty disables saving through
  `NSQuitAlwaysKeepsWindows`, but AppKit continued taking persistent-UI
  window snapshots in my reproduction on macOS 27.2 (26B5091g).
  
  Make `TerminalController.windowDidLoad()` also honor `never` when
  setting `window.isRestorable`, and only assign the restoration class and
  identifier when that flag is enabled. This adds no work to move, resize,
  or rendering callbacks.
  
  For newly created windows, `default` and `always` retain the existing
  behavior, including the exclusion of windows launched with a custom
  command. The follow-up commit also covers windows that are already open:
  on config reload, each terminal window re-syncs its restoration state
  through the same path used at window creation. Windows started with a
  custom command stay excluded.
  
  ### Reproduction and measurements
  
  I reproduced intermittent roughly 500 ms stalls while repeatedly
  focusing left/right between several Ghostty windows and other
  applications in OmniWM's Niri layout. `window-save-state = never` was
  set before restarting Ghostty.
  
  The issue reproduced on 1.3.1 and an unmodified build of `76895d97b`. In
  the latter, paired process samples showed
  `NSPersistentUIWindowSnapshotter` waiting through
  `SLSConnectionSynchronizeSLSCATransaction`, alongside Ghostty's main
  thread waiting on the connection lock under
  `SLSConnectionSetLastSLSCATransaction`.
  
  Comparing unmodified and patched builds of the same commit over two
  approximately 20-second navigation captures:
  
  | Measurement | Unmodified | Patched |
  | --- | ---: | ---: |
  | Focus presses | 113 | 129 |
  | Successful Ghostty AX frame-write attempts | 2,155 | 2,995 |
  | Ghostty AX frame-write attempts around 500 ms | 5 | 0 |
  | Slowest Ghostty AX frame-write attempt | 539.8 ms | 22.5 ms |
  | Ghostty main-thread samples in the CA/SkyLight connection-lock wait |
  2,205 / 12,544 | 0 / 12,173 |
  
  The persistent-UI snapshot worker was absent from the patched sample,
  and navigation feels noticeably smoother. These are aggregate samples
  from one before/after pair with different input counts, not a controlled
  end-to-end latency benchmark. Both Ghostty builds used ReleaseLocal with
  the same ReleaseFast core, while OmniWM remained the same instrumented
  Debug process.
  
  ### Validation
  
  - `macos/build.nu --action test`: 275 passed, 1 skipped, 0 failed.
  - New `macos/Tests/Terminal/TerminalControllerRestorationTests.swift`:
  reload flips restoration on an open window between `never`, `default`
  and `always`; custom-command windows stay non-restorable across reloads;
  surface-level config changes leave it alone.
  - `macos/build.nu --configuration ReleaseLocal`: passed.
  - Strict SwiftLint on both changed files: passed.
  - Manual navigation reproduction with the patched build: noticeably
  smoother, with the results above.
  
  ### AI disclosure
  
  I used OpenAI Codex to assist with diagnosis, implement the two-line
  change, run verification, analyze the captures, and draft this
  description. I reproduced the issue and tested the patched app
  interactively.
  ```

## October 1, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/36927788656), [2](https://github.com/ghostty-org/ghostty/actions/runs/36889148457), [3](https://github.com/ghostty-org/ghostty/actions/runs/36870310878), [4](https://github.com/ghostty-org/ghostty/actions/runs/36861449987), [5](https://github.com/ghostty-org/ghostty/actions/runs/36824341438), [6](https://github.com/ghostty-org/ghostty/actions/runs/36821001995)  
Summary: 6 runs • 16 commits • 5 authors

### Changes

- [`83edd49`](https://github.com/ghostty-org/ghostty/commit/83edd491e3024ae5e50393d62877b8897da1cccd) Update VOUCHED list ([#14510](https://github.com/ghostty-org/ghostty/issues/14510)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14507#discussioncomment-18705479)
  from @jcollie.
  
  Vouch: @mlabbe
  ```
- [`36953bc`](https://github.com/ghostty-org/ghostty/commit/36953bca8e69dfb1b48b4e2275b2f216a556c7f2) terminal: route OSC 105 to the color parser ([@fornwall](https://github.com/fornwall))
  ```text
  The color parser handles `.osc_105` and the stream handler has a
  `reset_special` arm, but the OSC prefix state machine had no `105`
  state, so the sequence never reached them and was reported through the
  unknown sequence callback instead.
  
  Add the prefix state so OSC 105 is accepted the same way as OSC 5 and
  OSC 113-119. Special colors are still not stored, so this changes no
  terminal state.
  ```
- [`8834e16`](https://github.com/ghostty-org/ghostty/commit/8834e161c15fa70b13f47236ad3cd597f7529088) libghostty-vt: add memory usage query ([@mitchellh](https://github.com/mitchellh))
  ````text
  This adds GHOSTTY_TERMINAL_DATA_MEMORY_USAGE to the terminal getter that
  returns a struct with various memory metrics.
  
  Embedders previously had no real way to measure their memory usage that
  could be attributed to libghostty, measure if their compression
  timings/algorithims were effective, etc. Now they can!
  
  Example usage:
  
  ```c
  GhosttyTerminalMemoryUsage usage =
      GHOSTTY_INIT_SIZED(GhosttyTerminalMemoryUsage);
  ghostty_terminal_get(terminal, GHOSTTY_TERMINAL_DATA_MEMORY_USAGE,
                       &usage);
  uint64_t total =
      usage.primary_resident_bytes + usage.primary_image_bytes +
      usage.alternate_resident_bytes + usage.alternate_image_bytes;
  ```
  ````
- [`88e66cb`](https://github.com/ghostty-org/ghostty/commit/88e66cbc66d0c5cc4228b65af0874e783f6c8d1d) libghostty-vt: option to compress snapshot history while decoding ([@mitchellh](https://github.com/mitchellh))
  ````text
  This adds a snapshot decoder option that compresses each history page
  as soon as it is restored. This is off by default because it slows down
  snapshot restore (as you'd expect). But if you can tolerate that this is
  a great way to avoid memory spikes.
  
  ```c
  bool compress = true;
  ghostty_snapshot_decoder_set(
      decoder, GHOSTTY_SNAPSHOT_DECODER_OPT_COMPRESS_HISTORY, &compress);
  ghostty_snapshot_decoder_decode(decoder, &terminal);
  ```
  
  Some background:
  
  Previously, decoding a snapshot always left the entire scrollback
  uncompressed, even if the terminal that produced it had compressed it.
  The history stayed that size until the embedder ran a compression pass,
  so a restore could briefly use many times more memory than the original
  terminal. With this option, a decode never holds more than one
  uncompressed history page and the restored terminal starts out
  compressed. The snapshot format doesn't change, so this works with any
  snapshot.
  ````
- [`54bada3`](https://github.com/ghostty-org/ghostty/commit/54bada35da9b7fa69049b9e1f0afa0dfb5651011) libghostty-vt: add memory usage query ([#14499](https://github.com/ghostty-org/ghostty/issues/14499)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This adds GHOSTTY_TERMINAL_DATA_MEMORY_USAGE to the terminal getter that
  returns a struct with various memory metrics.
  
  Embedders previously had no real way to measure their memory usage that
  could be attributed to libghostty, measure if their compression
  timings/algorithims were effective, etc. Now they can!
  
  Example usage:
  
  ```c
  GhosttyTerminalMemoryUsage usage =
      GHOSTTY_INIT_SIZED(GhosttyTerminalMemoryUsage);
  ghostty_terminal_get(terminal, GHOSTTY_TERMINAL_DATA_MEMORY_USAGE,
                       &usage);
  uint64_t total =
      usage.primary_resident_bytes + usage.primary_image_bytes +
      usage.alternate_resident_bytes + usage.alternate_image_bytes;
  ```
  ````
- [`8628db1`](https://github.com/ghostty-org/ghostty/commit/8628db1a6135601be0dbdcb322bad1135cfde54c) libghostty-vt: option to compress snapshot history while decoding ([#14500](https://github.com/ghostty-org/ghostty/issues/14500)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This adds a snapshot decoder option that compresses each history page as
  soon as it is restored. This is off by default because it slows down
  snapshot restore (as you'd expect). But if you can tolerate that this is
  a great way to avoid memory spikes.
  
  ```c
  bool compress = true;
  ghostty_snapshot_decoder_set(
      decoder, GHOSTTY_SNAPSHOT_DECODER_OPT_COMPRESS_HISTORY, &compress);
  ghostty_snapshot_decoder_decode(decoder, &terminal);
  ```
  
  Some background:
  
  Previously, decoding a snapshot always left the entire scrollback
  uncompressed, even if the terminal that produced it had compressed it.
  The history stayed that size until the embedder ran a compression pass,
  so a restore could briefly use many times more memory than the original
  terminal. With this option, a decode never holds more than one
  uncompressed history page and the restored terminal starts out
  compressed. The snapshot format doesn't change, so this works with any
  snapshot.
  ````
- [`33da684`](https://github.com/ghostty-org/ghostty/commit/33da6848d63b3bba2b4f31ab1531d618f2795192) terminal: route OSC 105 to the color parser ([#14496](https://github.com/ghostty-org/ghostty/issues/14496)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `OSC 105` (reset special colors) is now routed to the color parser
  instead of being treated as an unknown OSC.
  
  Information: https://invisible-island.net/xterm/ctlseqs/ctlseqs.html
  
  > Ps = 1 0 5 ; c ⇒ Reset Special Color Number c. It is reset to the
  color specified by the corresponding X resource. Any number of c
  parameters may be given. These parameters correspond to the special
  colors which can be set using an OSC 5 control (or by adding the maximum
  number of colors using an OSC 4 control).
  
  The color parser already handles `.osc_105` and the stream handler
  already has a `reset_special` arm, but the OSC prefix state machine had
  no `105` state, so neither was reachable from a byte stream.
  
  With `GHOSTTY_TERMINAL_OPT_UNKNOWN_SEQUENCE` set, OSC 105 was reported
  as unknown while its counterpart OSC 5 was accepted.
  
  Special colors are still not stored, so this changes no terminal state,
  the same as OSC 5 and OSC 113-119.
  
  AI disclosure: Created with claude code using opus 5.5, minor polish up
  and review by me.
  ```
- [`d542774`](https://github.com/ghostty-org/ghostty/commit/d5427745de0b9339736627b170ddf38dd2a35241) Update VOUCHED list ([#14497](https://github.com/ghostty-org/ghostty/issues/14497)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14484#discussioncomment-18698752)
  from @trag1c.
  
  Denounce: @creatiVision
  ```
- [`fa604a1`](https://github.com/ghostty-org/ghostty/commit/fa604a17013d01646e498f18b10019a95b9578c6) terminal/c: test a paste reader ignoring a refused write ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  A MIME reader must stop after a refused write, but one that ignores it
  and returns true makes the paste succeed with the refused data missing.
  This test currently fails: the paste reports success with nothing
  written.
  ```
- [`2b0ceff`](https://github.com/ghostty-org/ghostty/commit/2b0ceff7deed209d470739c71176b760bc0fb302) terminal/c: fail a paste after any refused write ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  The paste only checked for a refused write when the reader returned
  false, so a reader that ignored one pasted the rest. Check it after
  every read instead.
  ```
- [`b1bfd1d`](https://github.com/ghostty-org/ghostty/commit/b1bfd1d9c574aed35e1d1d190ec9cb434273ec41) terminal: reset mouse shape on empty OSC 22 ([@fornwall](https://github.com/fornwall))
  ```text
  `OSC 22 ; ST` (an empty shape name) was logged as an unknown cursor
  shape and ignored, so an application had no way to give back the
  pointer shape it had set. kitty documents the empty form as "reset the
  pointer to default", and foot clears its override the same way.
  
  Dispatch a new `mouse_shape_reset` action for the empty name. The app
  runtime resolves it to the shape a mouse tracking toggle would set
  (`default` while tracking, `text` otherwise), and the libghostty-vt
  handler to `text`, its initial shape. Unknown non-empty names are
  still ignored.
  ```
- [`a806905`](https://github.com/ghostty-org/ghostty/commit/a806905ea1e3b1564b7cc4ab1c54084939ca59b3) Push xzostksrunrx ([#14494](https://github.com/ghostty-org/ghostty/issues/14494)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `io.h` says a paste fails once a write is refused.
  `ghostty_terminal_paste` only failed if the reader also returned false,
  so a reader that ignored the refusal pasted the text with the refused
  part missing. Now any refused write fails the paste with
  `GHOSTTY_OUT_OF_MEMORY`.
  
  The first commit adds a test that fails without the fix. Identified
  while ruberducking a miri test failure in libghostty-rs with fable.
  ```
- [`0081d45`](https://github.com/ghostty-org/ghostty/commit/0081d4530929317364d3bfec5309e55238e4cd90) terminal: reset mouse shape on empty OSC 22 ([#14495](https://github.com/ghostty-org/ghostty/issues/14495)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  `OSC 22 ; ST` (empty shape name) now resets the mouse pointer shape to
  the default instead of being logged as an unknown shape and ignored.
  This lets an app restore the default after setting the pointer.
  
  ## Verify
  
  Keep the mouse over the terminal while each command runs.
  
  ```sh
  printf '\e]22;pointer\e\\'; sleep 3; printf '\e]22;\e\\'
  ```
  - Before (main): stays a hand, and `unknown cursor shape: ` is logged.
  - After (this PR): hand for 3s, then I-beam.
  
  ```sh
  printf '\e[?1000h\e]22;pointer\e\\'; sleep 3; printf '\e]22;\e\\'; sleep 3; printf '\e[?1000l'
  ```
  - Before (main): hand, hand, then I-beam (only the tracking disable
  changes it).
  - After (this PR): hand, then arrow (tracking is still on), then I-beam.
  
  ## Other terminals
  
  Not tested - from checking source:
  
  - **kitty**: same as this PR, documented as "reset to default" in its
  [spec](https://sw.kovidgoyal.net/kitty/pointer-shapes/).
  [screen.c](https://github.com/kovidgoyal/kitty/blob/cbc5382bbe04be8c14e3c7a5069d53ea8257945e/kitty/screen.c#L2230)
  - **foot**: same.
  [terminal.c](https://codeberg.org/dnkl/foot/src/commit/cb2771788998f6a6288e2de8273c55a8214551e0/terminal.c#L4739-L4746)
  - **Konsole**: same.
  [Vt102Emulation.cpp](https://invent.kde.org/utilities/konsole/-/blob/d7aa606d87241d9051dff9caa7f0874546204394/src/Vt102Emulation.cpp#L1852-1856)
  - **iTerm2**: empty resets its pointer override too; its mouse-reporting
  default is an [I-beam with a
  circle](https://github.com/gnachman/iTerm2/blob/91411f53619af602bd434ab355e674c1faa831e3/sources/TerminalView/PTYTextView%2BARC.m#L752-L770).
  [PTYSession.m](https://github.com/gnachman/iTerm2/blob/91411f53619af602bd434ab355e674c1faa831e3/sources/PTYSession/PTYSession.m#L18688-L18734)
  - **Contour**: resets too, but its default depends on main vs. alternate
  screen rather than mouse tracking.
  [Screen.cpp](https://github.com/contour-terminal/contour/blob/d8ce17bc34c653a3368d45f52bd7eea67452d673/src/vtbackend/screen/Screen.cpp#L4788-L4798)
  - **xterm**: its
  [implementation](https://github.com/ThomasDickey/xterm-snapshots/blob/bccd466414dc4ecb264a3824a6f1e41bebe65214/misc.c#L4141-L4152)
  ignores the empty form, although the
  [documentation](https://invisible-island.net/xterm/ctlseqs/ctlseqs.html#h2-Operating-System-Commands)
  says it selects the default `xterm` shape. `OSC 22 ; xterm` explicitly
  selects the I-beam; it does not restore a customized
  [`pointerShape`](https://invisible-island.net/xterm/manpage/xterm.html#VT100-Widget-Resources:pointerShape)
  setting.
  - xterm does not switch pointer shapes for mouse tracking. In Ghostty,
  `OSC 22 ; xterm` also always selects the I-beam; the empty form restores
  the tracking-dependent default (arrow while tracking, I-beam otherwise).
  
  WezTerm, Alacritty, Rio, Windows Terminal and VTE do not implement OSC
  22.
  
  The [Ghostty OSC 22 docs page](https://ghostty.org/docs/vt/osc/22)
  should probably get a line about the empty form (I can do that as a
  follow up, if this PR is merged).
  
  AI disclosure: Created with claude code using opus 5.5. Reviewed,
  iterated on and manually tested by me.
  ````
- [`2e36658`](https://github.com/ghostty-org/ghostty/commit/2e36658c63bb1e3d82bbf1e3a6312a15e4cb2bd7) opengl: explain why the surfaceless display can't be created ([@jcollie](https://github.com/jcollie))
  ```text
  When no EGL driver can be loaded (for example, the system's Mesa needs
  a newer glibc than Ghostty was built against), eglGetPlatformDisplay
  fails with EGL_BAD_PARAMETER and Ghostty exits reporting only
  "BadParameter", which says nothing about the actual cause.
  ```
- [`59c2dc0`](https://github.com/ghostty-org/ghostty/commit/59c2dc032aba42aa5064bf206cc27286add3e9d8) opengl: explain why the surfaceless display can't be created ([#14490](https://github.com/ghostty-org/ghostty/issues/14490)) ([@jcollie](https://github.com/jcollie))
  ```text
  When no EGL driver can be loaded (for example, the system's Mesa needs a
  newer glibc than Ghostty was built against), eglGetPlatformDisplay fails
  with EGL_BAD_PARAMETER and Ghostty exits reporting only "BadParameter",
  which says nothing about the actual cause.
  
  (This is a companion to #14489 but doesn't depend on it)
  
  AI disclosure: Claude Code assisted in developing this PR. I have
  thoroughly reviewed and tested the code.
  ```
- [`1dc485f`](https://github.com/ghostty-org/ghostty/commit/1dc485f10fa399f394b7dd65b42ed731d61dc885) Update VOUCHED list ([#14491](https://github.com/ghostty-org/ghostty/issues/14491)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14487#discussioncomment-18692193)
  from @jcollie.
  
  Vouch: @Myleshen
  ```

