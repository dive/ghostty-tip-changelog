> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: September 30, 2026 at 09:14 UTC.

## September 30, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/36670952998), [2](https://github.com/ghostty-org/ghostty/actions/runs/36665025906), [3](https://github.com/ghostty-org/ghostty/actions/runs/36660177665), [4](https://github.com/ghostty-org/ghostty/actions/runs/36659330138), [5](https://github.com/ghostty-org/ghostty/actions/runs/36655721423), [6](https://github.com/ghostty-org/ghostty/actions/runs/36654852811)  
Summary: 6 runs • 13 commits • 5 authors

### Changes

- [`4da7523`](https://github.com/ghostty-org/ghostty/commit/4da7523faba68ccb4042ea20585817098a51c015) Update VOUCHED list ([#14471](https://github.com/ghostty-org/ghostty/issues/14471)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13769#discussioncomment-18671909)
  from @jcollie.
  
  Vouch: @HackAttack
  ```
- [`b0174d0`](https://github.com/ghostty-org/ghostty/commit/b0174d03f6b5414f8254ec7bb05fd261e8745cb8) Update VOUCHED list ([#14469](https://github.com/ghostty-org/ghostty/issues/14469)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14468#discussioncomment-18671074)
  from @jcollie.
  
  Vouch: @pressatojump
  ```
- [`f9ab34f`](https://github.com/ghostty-org/ghostty/commit/f9ab34f104855dcb67d0fc7c81c727f72778b5a6) terminal: repair live pending wrap after resize ([@fornwall](https://github.com/fornwall))
  ```text
  Resize already repairs a saved cursor whose pending wrap no longer falls
  at the right edge, but leaves the live cursor armed. The next character
  then starts a new row even when reflow left space after the last print.
  
  Apply the same adjustment to the live cursor after reloading its pin:
  clear pending wrap and advance one cell when it is no longer at the right
  edge. Preserve pending wrap when the cursor still fills the resized row.
  
  Several Screen resize tests moved the cursor with cursorAbsolute while
  testWriteString had left pending wrap set, a state Terminal never
  produces because setCursorPos clears the flag. They now clear it too.
  
  Cover live and restored cursors when widening, narrowing, changing only
  height, merging wrapped rows, and printing after a wide character, plus
  a cursor without pending wrap.
  ```
- [`26e64df`](https://github.com/ghostty-org/ghostty/commit/26e64dfb4f03c493ebbeb12c9f020fe8f1304a5f) terminal: repair live pending wrap after resize ([#14458](https://github.com/ghostty-org/ghostty/issues/14458)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Fix an extra line wrap after resizing a terminal with pending wrap set.
  
  If resizing leaves room after the last printed cell, clear pending wrap
  and advance the live cursor to the next insertion position, matching the
  existing saved-cursor handling.
  
  Several `Screen` resize tests repositioned the cursor without clearing
  pending wrap. They now clear it, matching `Terminal.setCursorPos`.
  
  ### Widening example
  Starting with a 10-column terminal:
  
  1. Output `123456789|`.
  2. Widen the terminal.
  3. Output `X`.
  
  Current buggy behaviour:
  ```
  123456789|
  X
  ```
  
  Fixed expected behaviour:
  ```
  123456789|X
  ```
  
  ### Narrowing example
  Starting with a 10-column terminal:
  
  1. Output `123456789|`.
  2. Narrow the terminal to 8 columns.
  3. Output `X`.
  
  Current buggy behaviour:
  ```
  12345678
  9|
  X
  ```
  
  Fixed expected behaviour:
  ```
  12345678
  9|X
  ```
  
  AI disclosure: Created with codex using gpt-6 astra. Iterated on,
  manually tested and reviewed by me.
  ````
- [`5170b06`](https://github.com/ghostty-org/ghostty/commit/5170b06f61171692b364717196ab015b64990f68) terminal: fix relative prompt click coordinates ([@fornwall](https://github.com/fornwall))
  ```text
  Relative prompt clicks (OSC 133;A;click_events=2) subtracted a
  page-local prompt row from a viewport row.
  
  These coordinate systems could differ when the viewport was offset
  within a storage page or the prompt and click occupied different pages.
  The saturating subtraction could then collapse distinct click rows to 1.
  
  Count rows between the prompt and click pins instead, including when the
  prompt begins above the visible viewport.
  
  Reference: https://sw.kovidgoyal.net/kitty/shell-integration/
  ```
- [`438d584`](https://github.com/ghostty-org/ghostty/commit/438d584f0669012b5db30771df8cf37f26c9408d) test: run esctest against libghostty-vt, report-only in CI ([@jcollie](https://github.com/jcollie))
  ```text
  esctest is a conformance suite for terminal emulators. Most of it fails
  today, largely for want of DECRQCRA, so the CI job reports its results
  in the step summary and a log artifact but never fails the build.
  
  Claude-Session: https://claude.ai/code/session_01EFZKUd9WPnnojj5RiDeA1z
  ```
- [`80456f0`](https://github.com/ghostty-org/ghostty/commit/80456f05732a68b3fed99eb7396eddf8b7981080) renderer: fix custom shader selection color uniform layout ([@howdeploy](https://github.com/howdeploy))
- [`75e7a18`](https://github.com/ghostty-org/ghostty/commit/75e7a180d33a7aeea2d08c1d26885e888d8bde53) renderer: fix custom shader selection color uniform layout ([#14460](https://github.com/ghostty-org/ghostty/issues/14460)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Custom shaders read the configured selection foreground and background
  colors swapped: the CPU `Uniforms` struct stores background before
  foreground, while the GLSL `Globals` block declares foreground before
  background.
  
  Reorder the two CPU fields to match GLSL. Add a regression test that
  compiles the actual shader prefix and compares both selection uniform
  offsets from SPIRV-Cross reflection with `@offsetOf(Uniforms, ...)`.
  
  Related discussion:
  https://github.com/ghostty-org/ghostty/discussions/14459
  
  Validation on Linux with Zig 0.16.0, GTK 4.22.4, libadwaita 1.9.3, and
  Blueprint 0.18.0:
  
  - `zig build test -Dtest-filter="custom shader selection uniform layout"
  -Dapp-runtime=none -Demit-macos-app=false -Demit-docs=false -j6
  --summary all`: 77/77 tests passed in the filtered run, including
  unnamed import tests.
  - Restoring only the original CPU field order makes the regression test
  fail with `expected 4480, found 4464`; the remaining 76 tests pass.
  Restoring the fix passes 77/77 again.
  - `zig build -Demit-docs=false -j6 --summary all`: GTK Debug build
  completed, 273/273 steps succeeded, with the local build workaround
  described below.
  
  The normal GTK test build initially hit an unrelated Zig linker error
  handling `R_X86_64_PC64` relocations in the system glibc 2.44 `.sframe`
  sections. For the full GTK build only, `.use_llvm = true` was
  temporarily added to `ghostty-build-data` and `gtk_blueprint_check`.
  Those local changes were removed after verification and are not part of
  this PR. The headless test results above required no source workarounds.
  The full test suite and visual checks were not run.
  
  AI disclosure: OpenAI Codex adapted the existing local fix and
  regression test to current main and drafted this description.
  ```
- [`da1afb5`](https://github.com/ghostty-org/ghostty/commit/da1afb56142b25c03ea26fcd71d755a23f048d34) test: run esctest against libghostty-vt, report-only in CI ([#14454](https://github.com/ghostty-org/ghostty/issues/14454)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  esctest is a conformance suite for terminal emulators. Most of it fails
  today, largely for want of DECRQCRA, so the CI job reports its results
  in the step summary and a log artifact but never fails the build.
  
  AI disclosure: Claude Code assisted in the development of this PR but I
  have thoroughly reviewed the code.
  ```
- [`cc2f7ee`](https://github.com/ghostty-org/ghostty/commit/cc2f7ee4def8c90dbade4bef033dd40c0f4502dd) terminal: fix relative prompt click coordinates ([#14416](https://github.com/ghostty-org/ghostty/issues/14416)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Relative prompt clicks (`OSC 133;A;click_events=2`) subtracted a
  page-local prompt row from a viewport row.
  
  These coordinate systems could differ when the viewport was offset
  within a storage page or the prompt and click occupied different pages.
  The saturating subtraction could then collapse distinct click rows to 1.
  
  Count rows between the prompt and click pins instead, including when the
  prompt begins above the visible viewport.
  
  Reference: https://sw.kovidgoyal.net/kitty/shell-integration/
  
  AI disclosure: Created with gpt-6 astra in codex, then iterated on and
  reviewed by me.
  ```
- [`5b435d5`](https://github.com/ghostty-org/ghostty/commit/5b435d548a670f10d9b87357287dcaf5281de7f0) Update VOUCHED list ([#14466](https://github.com/ghostty-org/ghostty/issues/14466)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14465#discussioncomment-18669994)
  from @jcollie.
  
  Vouch: @stepankandrushin
  ```
- [`d67ab32`](https://github.com/ghostty-org/ghostty/commit/d67ab3213ea272a51b0aecffdc1c5704d7b9b2fe) Update VOUCHED list ([#14464](https://github.com/ghostty-org/ghostty/issues/14464)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14463#discussioncomment-18669416)
  from @jcollie.
  
  Vouch: @clemg
  ```
- [`6f51f41`](https://github.com/ghostty-org/ghostty/commit/6f51f41d0492ee1125f7bf054619fc31fb21baa2) Update VOUCHED list ([#14462](https://github.com/ghostty-org/ghostty/issues/14462)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14461#discussioncomment-18669266)
  from @jcollie.
  
  Vouch: @howdeploy
  ```

## September 29, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/36646682281), [2](https://github.com/ghostty-org/ghostty/actions/runs/36621526573), [3](https://github.com/ghostty-org/ghostty/actions/runs/36570963001), [4](https://github.com/ghostty-org/ghostty/actions/runs/36564315702), [5](https://github.com/ghostty-org/ghostty/actions/runs/36560770343)  
Summary: 5 runs • 14 commits • 5 authors

### Changes

- [`0d82239`](https://github.com/ghostty-org/ghostty/commit/0d82239b5803953a18dd8dc84f99867778dd2518) fix(gtk): warn once about missing/invalid DPI values ([@xandris](https://github.com/xandris))
  ```text
  Fixes #14410
  ```
- [`4ddf1f7`](https://github.com/ghostty-org/ghostty/commit/4ddf1f79d3490c93506fc41601dcaff6d4d4f134) fix(gtk): warn once about missing/invalid DPI values ([#14434](https://github.com/ghostty-org/ghostty/issues/14434)) ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes #14410
  
  Sorry it took so long I had to learn zig :) I just added a warnings
  struct so unset DPI is warned about once and invalid DPI is warned about
  whenever the invalid value changes.
  ```
- [`a141f9b`](https://github.com/ghostty-org/ghostty/commit/a141f9bdb3afe8aaa0ae9a37741a345cc1199fac) windows: run global constructors in DLLs ([@jcollie](https://github.com/jcollie))
  ```text
  Zig's `_DllMainCRTStartup` returns without running static initializers,
  so simdutf's active-kernel pointer stays null in libghostty-vt.dll and
  the first multi-byte UTF-8 sequence crashes the process.
  
  Discussion: https://github.com/ghostty-org/ghostty/discussions/14355
  
  Claude-Session: https://claude.ai/code/session_01H2NEUyBqXoyVpDXjXkqh8p
  ```
- [`a7cf951`](https://github.com/ghostty-org/ghostty/commit/a7cf951ebe450db0298780e97c0829af5c25c6ad) ci: test the libghostty-vt DLL with c-vt-effects on Windows ([@jcollie](https://github.com/jcollie))
  ```text
  Unit tests link the terminal statically and never load the DLL, so they
  can't see this crash. Run the C example against the DLL directly.
  
  Claude-Session: https://claude.ai/code/session_01H2NEUyBqXoyVpDXjXkqh8p
  ```
- [`f9e8270`](https://github.com/ghostty-org/ghostty/commit/f9e82709360d97b2246718f774c544de0f16787b) libghostty-vt/windows: run global constructors in DLLs ([#14447](https://github.com/ghostty-org/ghostty/issues/14447)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  When libghostty-vt is linked as a DLL global constructors were not being
  initialized. This caused a crash in simdutf if a multi-byte UTF-8
  sequence was split across writes.
  
  Also added a test to drive libghostty-vt as a shared library to so that
  regressions shouldn't happen.
  
  Refs: #14355
  
  AI disclosure. Claude Code was used to diagnose and implement the patch,
  but I have thoroughly reviewed the code.
  ```
- [`520d8f5`](https://github.com/ghostty-org/ghostty/commit/520d8f55ace5186f71bb796cffc9350e4973d790) terminal: CAN and SUB cancel an in-progress OSC ([@mitchellh](https://github.com/mitchellh))
  ```text
  When a program cancels an OSC with CAN (0x18) or SUB (0x1A), we still
  ran the command as if the OSC had ended normally. For example,
  `ESC ] 2 ; title CAN` still changed the window title. xterm discards a
  cancelled OSC without acting on it, and now we do too.
  
  References:
  
  - xterm (patch 411) `charproc.c`: `CASE_CAN` and `CASE_SUB` reset the
    parser, and only `CASE_BELL` and `CASE_ST` call `do_osc`.
  - DEC ANSI parser: CAN and SUB "cancel any escape sequence, control
    sequence or control string in progress."
    https://vt100.net/emu/dec_ansi_parser
  ```
- [`0538f75`](https://github.com/ghostty-org/ghostty/commit/0538f7535be0cbca6bbe54e6fde654d5c628f1f2) terminal: CAN and SUB cancel an in-progress OSC ([#14453](https://github.com/ghostty-org/ghostty/issues/14453)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  When a program cancels an OSC with CAN (0x18) or SUB (0x1A), we still
  ran the command as if the OSC had ended normally. For example, `ESC ] 2
  ; title CAN` still changed the window title. xterm discards a cancelled
  OSC without acting on it, and now we do too.
  
  References:
  
  - xterm (patch 411) `charproc.c`: `CASE_CAN` and `CASE_SUB` reset the
  parser, and only `CASE_BELL` and `CASE_ST` call `do_osc`.
  - DEC ANSI parser: CAN and SUB "cancel any escape sequence, control
  sequence or control string in progress."
  https://vt100.net/emu/dec_ansi_parser
  ```
- [`7b11f3d`](https://github.com/ghostty-org/ghostty/commit/7b11f3dca034d8d24369ad3856afe57946d7902a) libghostty: unknown sequence callback for OSC ([@mitchellh](https://github.com/mitchellh))
  ````text
  This extends the unknown sequence support to OSC (we previously only supported
  APC). This lets a libghostty-vt (Zig or C) user handle OSC sequences that
  libghostty itself doesn't support.
  
  When there is no unknown max bytes set (the default), this has no
  measurable cost in any benchmarks. When it is set, it only impacts
  unknown sequences.
  
  ```c
  static void on_unknown(GhosttyTerminal t, void* ud,
                         const GhosttyTerminalUnknownSequence* seq) {
    if (seq->tag != GHOSTTY_TERMINAL_UNKNOWN_SEQUENCE_OSC) return;
    const GhosttyTerminalUnknownOscSequence* osc = &seq->value.osc;
    printf("OSC: %.*s\n", (int)osc->content.len,
           (const char*)osc->content.ptr);
  }
  
  size_t max = 1024;
  ghostty_terminal_set(t, GHOSTTY_TERMINAL_OPT_UNKNOWN_SEQUENCE,
                       (const void*)on_unknown);
  ghostty_terminal_set(t, GHOSTTY_TERMINAL_OPT_UNKNOWN_MAX_BYTES, &max);
  
  // Prints "OSC: 7400;hello"
  const char* seq = "\x1b]7400;hello\x07";
  ghostty_terminal_vt_write(t, (const uint8_t*)seq, strlen(seq));
  ```
  ````
- [`3a3047f`](https://github.com/ghostty-org/ghostty/commit/3a3047f6b62a791fd8b12d9f07a85b3d2160370b) libghostty: unknown sequence callback for OSC ([#14452](https://github.com/ghostty-org/ghostty/issues/14452)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This extends the unknown sequence support to OSC (we previously only
  supported APC). This lets a libghostty-vt (Zig or C) user handle OSC
  sequences that libghostty itself doesn't support.
  
  When there is no unknown max bytes set (the default), this has no
  measurable cost in any benchmarks. When it is set, it only impacts
  unknown sequences.
  
  ```c
  static void on_unknown(GhosttyTerminal t, void* ud,
                         const GhosttyTerminalUnknownSequence* seq) {
    if (seq->tag != GHOSTTY_TERMINAL_UNKNOWN_SEQUENCE_OSC) return;
    const GhosttyTerminalUnknownOscSequence* osc = &seq->value.osc;
    printf("OSC: %.*s\n", (int)osc->content.len,
           (const char*)osc->content.ptr);
  }
  
  size_t max = 1024;
  ghostty_terminal_set(t, GHOSTTY_TERMINAL_OPT_UNKNOWN_SEQUENCE,
                       (const void*)on_unknown);
  ghostty_terminal_set(t, GHOSTTY_TERMINAL_OPT_UNKNOWN_MAX_BYTES, &max);
  
  // Prints "OSC: 7400;hello"
  const char* seq = "\x1b]7400;hello\x07";
  ghostty_terminal_vt_write(t, (const uint8_t*)seq, strlen(seq));
  ```
  ````
- [`a573781`](https://github.com/ghostty-org/ghostty/commit/a573781c6c2b0c192fc82bf5b60b34b1317a384f) terminal: clear the kitty placeholder flag on full-row clears ([@fornwall](https://github.com/fornwall))
  ```text
  Erasing a row that holds a Kitty virtual placeholder (e.g. `CSI 2K`)
  left `kitty_virtual_placeholder` set. `Screen.clearCells` and
  `Page.clearCells` scanned the cells about to be erased and kept the
  flag if any was a placeholder. That is backwards, since those cells
  are blank afterwards. The flag was only cleared when it was already
  stale.
  
  Clear it unconditionally on a full-row clear, matching `moveCells`
  and the `styled`/`hyperlink`/`grapheme` flags. A stale flag made
  placement iteration scan rows with no placeholders.
  ```
- [`05392dc`](https://github.com/ghostty-org/ghostty/commit/05392dcc9b1edb3e4fbaa513646ecd08c67f0ffb) renderer: nuke stub WebGL renderer ([@pluiedev](https://github.com/pluiedev))
  ```text
  We don't really have a WebGL renderer at all. Maybe this was a holdover
  from when libghostty-internal was supposed to run on WASM? No idea.
  Anyway this is holding us back as the sole remaining renderer not using
  the generic API framework.
  ```
- [`40d5b86`](https://github.com/ghostty-org/ghostty/commit/40d5b860d26bb5683acae07c694582cbba5e4cfb) renderer: share render device state across renderers ([@pluiedev](https://github.com/pluiedev))
  ```text
  It's rather wasteful to go through EGL initialization whenever a new
  surface is created, so let's extract the device state out and store it
  at an app level.
  ```
- [`ed350cb`](https://github.com/ghostty-org/ghostty/commit/ed350cbb4be3523e66016ceecd3be92b61334755) renderer: share render device state across renderers ([#14446](https://github.com/ghostty-org/ghostty/issues/14446)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  It's rather wasteful to go through EGL initialization whenever a new
  surface is created, so let's extract the device state out and store it
  at an app level.
  
  Also removed the stub WebGL renderer. I'm not sure which purpose it
  serves but no code was ever written for it and we're not targeting WebGL
  any time soon.
  
  **AI notice**: I defined the scope and the mechanical tasks are mostly
  performed by DeepSeek v4.1 Flash.
  ```
- [`02a3a04`](https://github.com/ghostty-org/ghostty/commit/02a3a049c9da7aaba1920dcd8ea3624b1ce452f1) terminal: clear the kitty placeholder flag on full-row clears ([#14449](https://github.com/ghostty-org/ghostty/issues/14449)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Erasing a row that holds a Kitty virtual placeholder left
  `kitty_virtual_placeholder` set.
  
  `Screen.clearCells` and `Page.clearCells` scanned the cells about to be
  erased and kept the flag if any was a placeholder. That is backwards,
  since those cells are blank afterwards. The flag was only cleared when
  it was already stale.
  
  AI disclosure: Created with claude code using opus 5.5. Iterated on and
  reviewed by me.
  ```

## September 28, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/36466905637), [2](https://github.com/ghostty-org/ghostty/actions/runs/36430031707), [3](https://github.com/ghostty-org/ghostty/actions/runs/36429057423)  
Summary: 3 runs • 29 commits • 10 authors

### Changes

- [`12752b2`](https://github.com/ghostty-org/ghostty/commit/12752b2ac1bb05ce53402ed8c853ed1f96eef0b1) Update VOUCHED list ([#14445](https://github.com/ghostty-org/ghostty/issues/14445)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14443#discussioncomment-18645416)
  from @jcollie.
  
  Vouch: @francislata
  ```
- [`78494ba`](https://github.com/ghostty-org/ghostty/commit/78494bad86c51ae78a66bfea3e42b8bd8c0b7cc2) terminal/c: expose the application-requested mouse shape ([@toppk](https://github.com/toppk))
  ```text
  C frontends cannot read the pointer shape that the terminal already tracks
  for OSC 22. Expose it through ghostty_terminal_get so they can honor shape
  requests and restore the pointer after hover overrides without parsing OSC
  sequences themselves.
  ```
- [`67fb0c9`](https://github.com/ghostty-org/ghostty/commit/67fb0c9407ec0906fc157c418a7ddc343ce6f7d2) terminal/c: move mouse shapes into mouse.h ([@toppk](https://github.com/toppk))
- [`a3f3331`](https://github.com/ghostty-org/ghostty/commit/a3f3331d4df6904f11f5063127cc3d99a43dc4a0) font: store nerd-font constraints in a 3-level table ([@j-c-m](https://github.com/j-c-m))
  ```text
  getConstraint was a switch over hundreds of nerd-font ranges. Generate a
  3-level table, same shape as the symbol LUT. Empty pages return after
  the stage1 load.
  
  branch vs current main (6301810a4)
  
  cmatrix -u 0 -b 120×40 getConstraint drops from ~16.5% to 0.7%.
  
  doom-fire 120x40 FPS flat ~776->777, getConstraint ~16% to 0.7%.
  ```
- [`364f847`](https://github.com/ghostty-org/ghostty/commit/364f8472ae97820a9b2806eea510457c30092777) terminal/c: expose the application-requested mouse shape ([#14371](https://github.com/ghostty-org/ghostty/issues/14371)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This commit was generated with extensive usage of AI (openai codex and
  claude code).
  
  Adds GHOSTTY_TERMINAL_DATA_MOUSE_SHAPE to ghostty_terminal_get,
  returning a public GhosttyMouseShape enum, so C frontends can read the
  pointer shape the terminal already tracks for OSC 22 without parsing OSC
  themselves.
  I am doing this so that I can handle OSC22 requests from applications
  for my c based terminal. Without this I do not see these commands.
  
  There was some discussion on discord whether to make it lower level by
  not using the enum and just sending the string. I didn't do that because
  my usecase is a normal c based terminal, and I think the curated enum
  that libghostty provides should be used by normal users, as well as the
  fact that this is already how zig land operates.
  
  I did mention this in my vouch request:
  https://github.com/ghostty-org/ghostty/discussions/14365 but there's no
  other applicable issue or discussion on this subject on github. Although
  the discussion here:
  https://github.com/ghostty-org/ghostty/discussions/12477 proposes a more
  low level api that might be worth looking into at some point, I think
  that's complementary.
  ```
- [`b1d2b7e`](https://github.com/ghostty-org/ghostty/commit/b1d2b7ef1f1cf5cc0118298bad849870bc678298) font: store nerd-font constraints in a 3-level table ([#14420](https://github.com/ghostty-org/ghostty/issues/14420)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Re-submit and improvement of #14306 - Now use a Lookup table so it is
  the same shape and performance of isSymbol when looking up nerd font
  constraints.
  
  getConstraint was a switch over hundreds of nerd-font ranges. Generate a
  3-level table, same shape as the symbol LUT. Empty pages return after
  the stage1 load.
  
  branch vs current main (6301810a4)
  
  cmatrix -u 0 -b 120×40 getConstraint drops from ~16.5% to 0.7%.
  
  doom-fire 120x40 FPS flat ~776->777, getConstraint ~16% to 0.7%.
  ```
- [`b60eed1`](https://github.com/ghostty-org/ghostty/commit/b60eed139be3bb175beab33bd0cf6479751d33ec) font: append BMP codepoints as one UTF-16 unit ([@j-c-m](https://github.com/j-c-m))
  ```text
  CoreText would always call CFStringGetSurrogatePairForLongCharacter,
  reserve two unichars, then shrink.
  
  addCodepoint treats cp > 0xFFFF as a pair. BMP codepoints are appended
  as one unichar, and surrogate conversion runs only for pairs.
  
  This is a 50% profiled speedup in addCodepoint for the common BMP case.
  ```
- [`e8fe0a5`](https://github.com/ghostty-org/ghostty/commit/e8fe0a5e61e6a67061bcc4bb955fc2957a7ac5b3) macOS: fix duplicate new windows triggered by Shortcuts.app ([@bo2themax](https://github.com/bo2themax))
- [`b94b3a0`](https://github.com/ghostty-org/ghostty/commit/b94b3a056ef26dfed11552e344fab28c545c885b) macOS: reduce the tab bar background opacity on macOS 27 ([@bo2themax](https://github.com/bo2themax))
- [`7376891`](https://github.com/ghostty-org/ghostty/commit/73768913b47820aae4f077ecbddec111042661c3) terminal: reject digit separators in OSC integers ([@fornwall](https://github.com/fornwall))
  ```text
  OSC numeric fields currently accept Zig digit separators: `9;4;1;4_2` sets
  progress to 42 and `4;1_0;red` selects palette index 10. In `rgb:f_f/0/0`,
  the underscore also counts toward the component width, producing a red
  value of 15 instead of 255.
  
  While mostly harmless in practice, nonstandard extensions like this can
  cause terminal interoperability issues over time.
  
  Introduce a shared integer parser that rejects digit separators and
  requires unsigned fields to contain digits only. Apply it to OSC numeric
  fields and RGB hexadecimal components, preserving signed ranges and
  existing error handling. This also rejects leading signs in unsigned
  fields that previously used `parseInt`, and affects RGB colors in
  configuration and themes through the shared color parser.
  ```
- [`4b86e35`](https://github.com/ghostty-org/ghostty/commit/4b86e3594cda498c1f973d8466d33eeef526429b) terminal/kitty: use wuffs for zlib image decompression ([@AnthonyZhOon](https://github.com/AnthonyZhOon))
  ```text
  Kitty graphics previously decoded zlib payloads through Zig's streaming
  flate reader. Use the Wuffs zlib decoder instead for faster throughput
  with a single-pass approach and safer code.
  
  Add coverage for output growth, size limits, truncated streams, and
  compressed PNG images.
  ```
- [`42049f1`](https://github.com/ghostty-org/ghostty/commit/42049f1c4483f799178267ea0ba11e4b4fe63886) pkg/wuffs: align zlib decoder storage ([@AnthonyZhOon](https://github.com/AnthonyZhOon))
  ```text
  Byte allocations can return addresses that do not satisfy the opaque
  Wuffs decoder's C alignment requirement. Request 16-byte alignment to
  avoid misaligned accesses when using allocators such as a fixed buffer.
  
  Add regression coverage with an unaligned allocator buffer and verify
  that a corrupted Adler-32 checksum is rejected.
  ```
- [`1ca2858`](https://github.com/ghostty-org/ghostty/commit/1ca2858d042f9c2d06e20148dca807aa22e75fde) tmux: map pane mouse flags to the selectors tmux reports ([@jparise](https://github.com/jparise))
  ```text
  tmux reports mouse_standard_flag for mode 1000, mouse_button_flag for
  1002, and mouse_all_flag for 1003, and it clears the other two before
  setting one so at most one is ever on. It has no X10 mode 9. The viewer
  mapped each flag one selector too low, so a pane with mode 1000 enabled
  was recorded as button tracking plus X10.
  
  mouse_any_flag has never named a selector. Every tmux version defines
  it as "some tracking mode is on": standard or button before 1003
  support existed, and the union of all three since. Map each specific
  flag to its actual selector and stop requesting mouse_any_flag, since
  the specific flags already cover it.
  ```
- [`d92e340`](https://github.com/ghostty-org/ghostty/commit/d92e3400e6e9ce480efb479759b22d7491003320) terminal: parse OSC integers in a single pass ([@fornwall](https://github.com/fornwall))
- [`500040d`](https://github.com/ghostty-org/ghostty/commit/500040d3b0650ce80d6a2e7d4664175577aa5b92) lib: move parseInt to src/lib and expose it from main.zig ([@fornwall](https://github.com/fornwall))
- [`31bbb12`](https://github.com/ghostty-org/ghostty/commit/31bbb12738c05fbdc940b731a69ce03057fd6612) lib: document why parseInt does not use std.fmt.parseInt ([@fornwall](https://github.com/fornwall))
- [`3822aa0`](https://github.com/ghostty-org/ghostty/commit/3822aa01d23dc8a66f67727a85738df065fb60ab) terminal: test OSC 3008 numeric fields reject non-digits ([@fornwall](https://github.com/fornwall))
- [`b1c2641`](https://github.com/ghostty-org/ghostty/commit/b1c264163d889322dfea9c66268b06788676d8a2) vt: reject search ticks after the terminal is freed ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  ghostty_search_tick didn't check whether the search's terminal had
  been freed. A history search compares its results against a pin
  tracked in the terminal's page list, so ticking a search after freeing
  its terminal read freed memory.
  
  Return GHOSTTY_INVALID_VALUE in that case, like feed and run already do.
  ```
- [`1a174c0`](https://github.com/ghostty-org/ghostty/commit/1a174c063a69f77708bbd7ec9773504e185710e7) nix: update zon2nix to 0.8.1 ([@jcollie](https://github.com/jcollie))
  ```text
  Should be even faster both when updating the lock files
  and when building with Nix in CI.
  ```
- [`1f3d869`](https://github.com/ghostty-org/ghostty/commit/1f3d869b4fbb9a3ea707c0f324096a3c5b026341) nix: remove no-longer-necessary linkFarm override ([@jcollie](https://github.com/jcollie))
- [`659ca22`](https://github.com/ghostty-org/ghostty/commit/659ca22c01b865f6b47eea7af62295aebb51449b) update to zon2nix 0.9.0 ([@jcollie](https://github.com/jcollie))
- [`c065cd3`](https://github.com/ghostty-org/ghostty/commit/c065cd3cdf9e18e8bdf66ca2454b5f6a49befc03) vt: reject search ticks after the terminal is freed ([#14437](https://github.com/ghostty-org/ghostty/issues/14437)) ([@mitchellh](https://github.com/mitchellh))
- [`d1eb462`](https://github.com/ghostty-org/ghostty/commit/d1eb462893eb0f347e462bb272692c58b045c319) nix: update zon2nix to 0.9.0 ([#14436](https://github.com/ghostty-org/ghostty/issues/14436)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Should be even faster both when updating the lock files and when
  building with Nix in CI.
  ```
- [`a85cd2e`](https://github.com/ghostty-org/ghostty/commit/a85cd2e161c7eeee5ced9a9e0ec6a1fe8105789e) tmux: map pane mouse flags to the selectors tmux reports ([#14425](https://github.com/ghostty-org/ghostty/issues/14425)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  tmux reports `mouse_standard_flag` for mode 1000, `mouse_button_flag`
  for 1002, and `mouse_all_flag` for 1003, and it clears the other two
  before setting one so at most one is ever on. It has no X10 mode 9. The
  viewer mapped each flag one selector too low, so a pane with mode 1000
  enabled was recorded as button tracking plus X10.
  
  `mouse_any_flag` has never named a selector. Every tmux version defines
  it as "some tracking mode is on": standard or button before 1003 support
  existed, and the union of all three since. Map each specific flag to its
  actual selector and stop requesting `mouse_any_flag`, since the specific
  flags already cover it.
  ```
- [`d48c037`](https://github.com/ghostty-org/ghostty/commit/d48c0372f42f9216761c425e4d080dc1957ee900) kitty: Use wuffs for zlib decoding over the stdlib ([#14422](https://github.com/ghostty-org/ghostty/issues/14422)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Kitty graphics previously decoded zlib payloads through Zig's streaming
  flate reader. Use the Wuffs zlib decoder instead for faster throughput
  with a single-pass approach and safer code.
  
  Microbenchmarking the wuffs decoder compared to the standard library
  showed throughput improvements of 10-30% for kitty graphics protocol's
  usecases of Zlib compression (compressed image file transmission)
  
  Benchmark | Zig stdlib | Wuffs | Speedup
  -- | -- | -- | --
  Zlib decompression | 2.30 s | 1.96 s | 1.17×
  Base64 chunk decoding + zlib decompression | 2.34 s | 1.99 s | 1.18×
  > The test data was a sample of my wallpapers directory consisting of 4k
  and 1920x1080 images with various compression ratios. Some outliers with
  extreme compression ratios (nearly all 1 colour) were ignored)
  # AI Disclosure
  A mix of GPT 6 Sol and Astra were used to run the benchmarks then write
  the diff, and then requested an audit round which surfaced the unaligned
  allocation bug.
  I reviewed the code and compared the zlib wrapper with our existing
  wrappers and reference implementations for wuffs wrappers.
  ```
- [`f04a00c`](https://github.com/ghostty-org/ghostty/commit/f04a00c071cd6c58705010926b4a5e7544654e62) terminal: reject digit separators in OSC integers ([#14417](https://github.com/ghostty-org/ghostty/issues/14417)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  OSC numeric fields currently accept Zig digit separators: `9;4;1;4_2`
  sets progress to 42 and `4;1_0;red` selects palette index 10. In
  `rgb:f_f/0/0`, the underscore also counts toward the component width,
  producing a red value of 15 instead of 255.
  
  While mostly harmless in practice, nonstandard extensions like this can
  cause terminal interoperability issues over time.
  
  Introduce a shared integer parser that rejects digit separators and
  requires unsigned fields to contain digits only. Apply it to OSC numeric
  fields and RGB hexadecimal components, preserving signed ranges and
  existing error handling. This also rejects leading signs in unsigned
  fields that previously used `parseInt`, and affects RGB colors in
  configuration and themes through the shared color parser.
  
  AI disclosure: Created with gpt-6 astra in codex, then iterated on and
  reviewed by me.
  ```
- [`068e15c`](https://github.com/ghostty-org/ghostty/commit/068e15c2d1d0cb8ad823636c3dc3b3c71dd7645e) macOS: reduce the tab bar background opacity on macOS 27 ([#14414](https://github.com/ghostty-org/ghostty/issues/14414)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Golden Gate changed the style of the native tab bar; now the tab bar has
  a glassy style, but AppKit also adds the window background color to the
  background, which looks weird on some themes.
  
  Fixes https://github.com/ghostty-org/ghostty/issues/14411.
  
  Others also proposed other approaches like changing the CALayer, but I
  think that's too complicated. Changing the opacity to 0.5 should cover
  most themes without sacrificing the glass style while maintaining the
  tab title's visibility.
  
  <img width="962" height="266" alt="image"
  src="https://github.com/user-attachments/assets/698a1469-c3fa-4e03-bfdd-f61d64b8fbfd"
  />
  ```
- [`bcfae28`](https://github.com/ghostty-org/ghostty/commit/bcfae289ceca9dfc3aab59a63c534e1116a614a8) macOS: fix duplicate new windows triggered by Shortcuts.app ([#14413](https://github.com/ghostty-org/ghostty/issues/14413)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes https://github.com/ghostty-org/ghostty/issues/14107.
  
  ## AI Disclosure
  
  Claude explored the patch and implemented most of it, I don't have a
  better way to check the event. I reviewed and reapply some of it.
  ```
- [`4406075`](https://github.com/ghostty-org/ghostty/commit/4406075a09c8ca0d83f30e8aaa710b9315ec428a) font: append BMP codepoints as one UTF-16 unit ([#14406](https://github.com/ghostty-org/ghostty/issues/14406)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This is a re-submit of #14309, I made another cleanup pass to simplify
  the code. Still a good performance improvement.
  
  CoreText would always call CFStringGetSurrogatePairForLongCharacter,
  reserve two unichars, then shrink.
  
  addCodepoint treats cp > 0xFFFF as a pair. BMP codepoints are appended
  as one unichar, and surrogate conversion runs only for pairs.
  
  This is a 50% profiled speedup in addCodepoint for the common BMP case.
  ```

## September 27, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/36289889834)  
Summary: 1 runs • 2 commits • 2 authors

### Changes

- [`75166e9`](https://github.com/ghostty-org/ghostty/commit/75166e9eb0f6812b492b875bda0b49000843fe9f) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`b40acce`](https://github.com/ghostty-org/ghostty/commit/b40acce58dcf77df52231c3798ea58e924647c89) Update iTerm2 colorschemes ([#14424](https://github.com/ghostty-org/ghostty/issues/14424)) ([@jcollie](https://github.com/jcollie))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260921-150923-0b55a9e
  ```

## September 25, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/36202102188), [2](https://github.com/ghostty-org/ghostty/actions/runs/36190238862), [3](https://github.com/ghostty-org/ghostty/actions/runs/36168450666), [4](https://github.com/ghostty-org/ghostty/actions/runs/36163015294), [5](https://github.com/ghostty-org/ghostty/actions/runs/36155263131), [6](https://github.com/ghostty-org/ghostty/actions/runs/36090632632)  
Summary: 6 runs • 41 commits • 10 authors

### Changes

- [`6301810`](https://github.com/ghostty-org/ghostty/commit/6301810a48aaa3426887a4316668f18833a40138) Update VOUCHED list ([#14409](https://github.com/ghostty-org/ghostty/issues/14409)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11214#discussioncomment-18606662)
  from @jcollie.
  
  Vouch: @xandris
  ```
- [`4eb3088`](https://github.com/ghostty-org/ghostty/commit/4eb3088316b7a95af7a505aeb9a39dc8b93fcb8d) gtk: don't tell systemd we're ready before we can handle SIGUSR2 ([@jcollie](https://github.com/jcollie))
  ```text
  On a dark desktop, syncing the color scheme during startup triggers a
  config reload, which sent RELOADING=1 and READY=1 before the SIGUSR2
  handler was installed. systemd 262 refuses to start a Type=notify-reload
  service whose reload signal has no handler, so D-Bus activation fails
  intermittently and no window opens.
  
  Fixes #14398
  Discussions: #11724, #14394
  
  Claude-Session: https://claude.ai/code/session_01PQKfAq9x9wJG5Vfy31Um65
  ```
- [`47693cc`](https://github.com/ghostty-org/ghostty/commit/47693cc4bcddddae7e91b9121f6cb736d02472c8) gtk,renderer: don't export DMABUFs when apprts can't accept them ([@pluiedev](https://github.com/pluiedev))
  ```text
  Rather annoyingly there's no way to avoid DMABUF format conflicts with
  OpenGL, so we bail if GTK won't take our DMABUFs
  ```
- [`b9e07f9`](https://github.com/ghostty-org/ghostty/commit/b9e07f98f4d66c254010d5825905f8e837b88000) gtk,opengl: flip CPU rendered textures correctly ([@pluiedev](https://github.com/pluiedev))
- [`2ea1eea`](https://github.com/ghostty-org/ghostty/commit/2ea1eeae2a040c6f057d03ede3b907c73f99c272) libghostty-vt: expose RenderState overscan in the C API ([@mitchellh](https://github.com/mitchellh))
  ````text
  This exposes the `RenderState` overscan and row identity from #14400
  through the libghostty-vt C API. Example:
  
  ```c
  GhosttyRenderStateOverscan request = { .above = 0, .below = 1 };
  ghostty_render_state_set(state, GHOSTTY_RENDER_STATE_OPTION_OVERSCAN,
                           &request);
  ghostty_render_state_update(state, terminal);
  
  ghostty_render_state_get(state, GHOSTTY_RENDER_STATE_DATA_ROW_ITERATOR,
                           &rows);
  while (ghostty_render_state_row_iterator_next(rows)) {
    int32_t y;
    GhosttyRenderStateRowId id;
    ghostty_render_state_row_get(
        rows, GHOSTTY_RENDER_STATE_ROW_DATA_VIEWPORT_Y, &y);
    ghostty_render_state_row_get(
        rows, GHOSTTY_RENDER_STATE_ROW_DATA_ID, &id);
    draw_row(rows, id, y * cell_height - offset_px);
  }
  ```
  
  A change: the row iterator is now sliced to `rowDataRange()`, the rows the last
  update captured. Every existing bounds check compares against the slice
  length, so iteration, `row_get`, and `row_set` needed no other changes.
  `GHOSTTY_RENDER_STATE_ROW_DATA_VIEWPORT_Y` adds the negated overscan
  above to the iterator position.
  
  The row id is opaque to C, and only equality is documented. Internally
  the first word is the page serial and the second is the row within the
  page plus one, so an all-zero id is never valid.
  ````
- [`d0c5ba6`](https://github.com/ghostty-org/ghostty/commit/d0c5ba6cd9db9aa6e47da4526668891989e95fb9) libghostty-vt: expose RenderState overscan in the C API ([#14404](https://github.com/ghostty-org/ghostty/issues/14404)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This exposes the `RenderState` overscan and row identity from #14400
  through the libghostty-vt C API. Example:
  
  ```c
  GhosttyRenderStateOverscan request = { .above = 0, .below = 1 };
  ghostty_render_state_set(state, GHOSTTY_RENDER_STATE_OPTION_OVERSCAN,
                           &request);
  ghostty_render_state_update(state, terminal);
  
  ghostty_render_state_get(state, GHOSTTY_RENDER_STATE_DATA_ROW_ITERATOR,
                           &rows);
  while (ghostty_render_state_row_iterator_next(rows)) {
    int32_t y;
    GhosttyRenderStateRowId id;
    ghostty_render_state_row_get(
        rows, GHOSTTY_RENDER_STATE_ROW_DATA_VIEWPORT_Y, &y);
    ghostty_render_state_row_get(
        rows, GHOSTTY_RENDER_STATE_ROW_DATA_ID, &id);
    draw_row(rows, id, y * cell_height - offset_px);
  }
  ```
  
  A change: the row iterator is now sliced to `rowDataRange()`, the rows
  the last update captured. Every existing bounds check compares against
  the slice length, so iteration, `row_get`, and `row_set` needed no other
  changes. `GHOSTTY_RENDER_STATE_ROW_DATA_VIEWPORT_Y` adds the negated
  overscan above to the iterator position.
  
  The row id is opaque to C, and only equality is documented. Internally
  the first word is the page serial and the second is the row within the
  page plus one, so an all-zero id is never valid.
  ````
- [`02e51d5`](https://github.com/ghostty-org/ghostty/commit/02e51d57195bcd03f7525cdbdfb8015d934bf0b6) gtk,opengl: even more post-rendersurface fixes ([#14403](https://github.com/ghostty-org/ghostty/issues/14403)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Should work around #14395...
  ```
- [`1a9edb0`](https://github.com/ghostty-org/ghostty/commit/1a9edb0009a7e4fd87d2eca5d61386ce0c2b7e9d) gtk: don't tell systemd we're ready before we can handle SIGUSR2 ([#14399](https://github.com/ghostty-org/ghostty/issues/14399)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  On a dark desktop, syncing the color scheme during startup triggers a
  config reload, which sent RELOADING=1 and READY=1 before the SIGUSR2
  handler was installed. systemd 262 refuses to start a Type=notify-reload
  service whose reload signal has no handler, so D-Bus activation fails
  intermittently and no window opens.
  
  Fixes #14398
  Discussions: #11724, #14394, #14393
  
  AI disclosure: Claude Code was used to investigate and develop the
  patch, but the author has thoroughly reviewed the patch.
  ```
- [`ca4f719`](https://github.com/ghostty-org/ghostty/commit/ca4f719f7730a302a93230add6944a8c233060ef) terminal: add overscan support to RenderState for smooth scrolling ([@mitchellh](https://github.com/mitchellh))
  ````text
  This adds overscan to `RenderState`: an optional number of rows to
  capture above and below the viewport to enable smooth/fractional scrolling.
  This is the Zig API only.
  
  This is the first step towards smooth scrolling. A renderer that draws
  the grid at a fractional row offset needs the partially visible rows at
  the top and bottom edges, which the render state now captures. Row ids
  let a renderer keep per-row work (shaped text, cached geometry) across a
  scroll rather than rebuilding every row whenever the viewport moves.
  
  Example:
  
  ```zig
  var state: RenderState = .empty;
  defer state.deinit(alloc);
  
  // Capture one extra row above and below the viewport.
  state.overscan_request = .{ .above = 1, .below = 1 };
  try state.update(alloc, &terminal);
  
  // Only entries in rowDataRange() are populated. There may be
  // fewer overscan rows than requested, e.g. at the top of
  // scrollback. See `state.overscan` for the actual counts.
  const range = state.rowDataRange();
  const rows = state.row_data.slice();
  for (range.start..range.end) |i| {
      // Viewport-relative: -1 is the row above the viewport,
      // state.rows is the row below it.
      const y = state.viewportY(i);
  
      // Stable across updates, e.g. for per-row caches.
      const id = rows.get(i).id();
  
      // Draw rows.items(.cells)[i] at `y` minus the fractional
      // scroll offset, reusing cached work for `id` if clean.
      _ = .{ y, id };
  }
  ```
  ````
- [`c959af6`](https://github.com/ghostty-org/ghostty/commit/c959af63d11b524a84c21900372990dbc024b059) terminal: add overscan support to RenderState for smooth scrolling ([#14400](https://github.com/ghostty-org/ghostty/issues/14400)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This adds overscan to `RenderState`: an optional number of rows to
  capture above and below the viewport to enable smooth/fractional
  scrolling. This is the Zig API only.
  
  This is the first step towards smooth scrolling. A renderer that draws
  the grid at a fractional row offset needs the partially visible rows at
  the top and bottom edges, which the render state now captures. Row ids
  let a renderer keep per-row work (shaped text, cached geometry) across a
  scroll rather than rebuilding every row whenever the viewport moves.
  
  Example:
  
  ```zig
  var state: RenderState = .empty;
  defer state.deinit(alloc);
  
  // Capture one extra row above and below the viewport.
  state.overscan_request = .{ .above = 1, .below = 1 };
  try state.update(alloc, &terminal);
  
  // Only entries in rowDataRange() are populated. There may be
  // fewer overscan rows than requested, e.g. at the top of
  // scrollback. See `state.overscan` for the actual counts.
  const range = state.rowDataRange();
  const rows = state.row_data.slice();
  for (range.start..range.end) |i| {
      // Viewport-relative: -1 is the row above the viewport,
      // state.rows is the row below it.
      const y = state.viewportY(i);
  
      // Stable across updates, e.g. for per-row caches.
      const id = rows.get(i).id();
  
      // Draw rows.items(.cells)[i] at `y` minus the fractional
      // scroll offset, reusing cached work for `id` if clean.
      _ = .{ y, id };
  }
  ```
  ````
- [`45013fa`](https://github.com/ghostty-org/ghostty/commit/45013faf842464c46184a152dbc40c60278ef924) gtk: support fractional surface scaling ([@and-rs](https://github.com/and-rs))
  ```text
  Use gdk surface scale for device sizes and
  DPI, keep textures 1:1 with device pixels,
  and react to scale notify on resize/redraw.
  ```
- [`1964ed1`](https://github.com/ghostty-org/ghostty/commit/1964ed123927e233e7d19425aae7ab53e52b1120) gtk: harden fractional scale notify and DPI rounding ([@and-rs](https://github.com/and-rs))
  ```text
  Retry GdkSurface scale notify from size-allocate if realize ran
  before a native surface existed, and ref the surface so a
  replaced GdkSurface cannot leave a dangling handler.
  
  Skip snapshots when scale is non-positive to avoid dividing by zero.
  Round DPI in estimateInitialSize so the pre-present font grid
  matches the realized surface.
  ```
- [`df2186d`](https://github.com/ghostty-org/ghostty/commit/df2186dce8a3a651eceb744a6fefddacb74b20fe) gtk: drop 4.12 version checks ([@and-rs](https://github.com/and-rs))
- [`08931f4`](https://github.com/ghostty-org/ghostty/commit/08931f40510f0ab30ca7ab7ebb72fbc66ca92bb7) gtk: added logs to debug scaling values ([@and-rs](https://github.com/and-rs))
- [`9dc7408`](https://github.com/ghostty-org/ghostty/commit/9dc7408be82fbee0ff039e91d08b88e68392a77f) gtk: snap fractional texture origin to device pixels ([@and-rs](https://github.com/and-rs))
  ```text
  RenderSurface previously placed the texture at CSS origin (0,0).
  That is pixel-aligned only when the widget itself is aligned to
  the native surface. Tab bars and other chrome shift the widget
  to a fractional device coordinate, so GTK linearly samples every
  texel and fonts look blurry.
  ```
- [`0070f9d`](https://github.com/ghostty-org/ghostty/commit/0070f9d0a0218e950d8b3888c47aaf3aefb87290) gtk: snap fractional texture origin GdkSurface ([@and-rs](https://github.com/and-rs))
  ```text
  - I was originally snapping to the window widget
  - Size the buffer from the snapped span, not ceil(css × scale).
  ```
- [`70a75ce`](https://github.com/ghostty-org/ghostty/commit/70a75ceb506e08ff418ab7412f9858c01d1909b3) gtk: Layout unifies scale, origin, snapped size ([@and-rs](https://github.com/and-rs))
  ```text
  - widgetLayout replaces widgetDeviceSize
  - snapOffset guards non-positive scale
  - snappedAxis uses round span, not ceil
  ```
- [`d1da183`](https://github.com/ghostty-org/ghostty/commit/d1da18350cadc9c61ecb0eded0b47c4e86d923a1) gtk: remove widgetDeviceSize, snapshotOrigin wrappers ([@and-rs](https://github.com/and-rs))
  ```text
  - widgetLayout replaces widgetDeviceSize calls
  - snapOrigin replaces snapshotOrigin method
  - widgetLayoutForSize replaces snappedDeviceSize site
  ```
- [`e1916c1`](https://github.com/ghostty-org/ghostty/commit/e1916c1abbec98f6a8934061191a29a1ede15a75) gtk: demote log from info to debug ([@and-rs](https://github.com/and-rs))
- [`56dbc4a`](https://github.com/ghostty-org/ghostty/commit/56dbc4a768778753737a3b9cbe0a3f9b4e434553) gtk: support fractional surface scaling ([#14269](https://github.com/ghostty-org/ghostty/issues/14269)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Fix
  
  This PR aims to use gdk_surface_get_scale() over
  gtk_widget_get_scale_factor() so device sizes and DPI follow the real
  fractional scale instead of the ceiled integer. Fall back to
  get_scale_factor when there is no GdkSurface.
  
  in short: Keep textures 1:1 with device pixels and listen to GdkSurface
  notify::scale for resize/redraw.
  
  - Related to #1938 (The issue was closed, but eventually it regressed;
  fractional scaling still blurry).
  - Because the original issue was closed I created this discussion:
  #13911 (Let me know if that is enough for this PR otherwise I guess we
  would need to create a new issue although I see it as unnecessary).
  - I was waiting on #14052 to be merged.
  
  ## Considerations
  
  Ok the blurry font is in a way subtle and hard to perceive. But a very
  "easy" way to test this is by looking at box characters. Box chars are
  supposed to be rendered pixel perfect with sharp edges because they're
  just boxes I suppose (correct me if I am wrong). You can compare to
  other terminal emulators, but if you see blurry edges on them, then
  we're not rendering on fractional scaling properly.
  
  Like this image in the discussion (the box char is much sharper on kitty
  previous to the fix):
  <img width="444" height="338" alt="image"
  src="https://github.com/user-attachments/assets/ec60dae0-2c33-4d52-adb5-92ea41775bf8"
  />
  
  I mention this because I have only tested on 1440p and ultrawide 4k
  (5120x2160). on Niri Wayland at 1.3x 1.5x and 1.666x.
  
  I have NOT tested yet on X11. I would love is someone could help with
  that otherwise I will do it, it's just going to take me abit of time.
  Same for other resolutions.
  
  > [!IMPORTANT]
  > of course just let me know if I can improve or change anything here in
  the code. Thanks!
  
  ## AI Disclosure
  
  I used GPT 5.6 Terra and Grok 4.6 here & there.
  ```
- [`714fe9b`](https://github.com/ghostty-org/ghostty/commit/714fe9b90373f88300e0f6ba3c51837439164a7e) terminal,macos: support resizing the window with CSI 8 t ([@shreeve](https://github.com/shreeve))
  ```text
  #1115
  
  Previously, the xterm window manipulation sequence CSI 8 ; rows ;
  columns t (XTWINOPS) was parsed but ignored as unimplemented. This
  lets a program such as a TUI request a terminal size, instead of
  asking the user to resize the window by hand.
  
  Because any program, including one on a remote machine, could use
  this to change the window size, it is gated behind a new
  `vt-window-resize-allowed` option that is disabled by default. This
  follows the same pattern as `title-report` for CSI 21 t. Requests
  below 40 columns by 10 rows are raised to that size so a program
  can't shrink the window to hide its output.
  
  The surface checks the config and converts the grid size to a size
  in points, then performs a new `resize_window` apprt action. A zero
  or omitted parameter is passed through as zero so the apprt keeps
  that dimension exactly as is.
  
  On macOS, the window is resized by the difference between the
  requested and current surface size, so the titlebar and other views
  are accounted for, and it is clamped to the screen before resizing
  so the terminal is only resized once. The request is ignored if the
  surface is in a split, a window with multiple tabs, fullscreen, the
  quick terminal, or has the inspector open, since the resize would not
  apply to the surface alone.
  ```
- [`219cca9`](https://github.com/ghostty-org/ghostty/commit/219cca9329e0bc6bc601c87e283da3225bbbe23f) gtk: support resizing the window with CSI 8 t ([@shreeve](https://github.com/shreeve))
  ```text
  Implement the `resize_window` apprt action on GTK. A floating window
  can resize itself on both Wayland and X11 by setting its default size
  while mapped: GTK uses the new default size unless the window's size
  is fixed by the compositor, and mutter applies a size committed by
  the client. gnome-terminal handles CSI 8 t the same way on GTK 4.
  
  As on macOS, the window is resized by the difference between the
  requested and current surface size, which accounts for the headerbar
  and tab bar. The difference is computed in device pixels because the
  surface's content scale also includes the font DPI. The request is
  ignored if the surface is in a split, the window has multiple tabs,
  or the window is the quick terminal, maximized, fullscreen, or tiled,
  since the compositor owns the size in those states.
  
  The window's compute-size handler re-asserts the current size when it
  exceeds the compositor bounds, which would prevent shrinking a window
  that fills the screen, so it steps aside for a requested resize.
  ```
- [`2a987d5`](https://github.com/ghostty-org/ghostty/commit/2a987d59de766302899bc2c7360c67cdac3ea5fc) config: move vt-window-resize-allowed next to vt-kam-allowed ([@shreeve](https://github.com/shreeve))
- [`d4f45be`](https://github.com/ghostty-org/ghostty/commit/d4f45bee3fe5b7ad14f3aed41463578f109f91c7) terminal: fix reverse wrap cursor jump ([@fornwall](https://github.com/fornwall))
  ```text
  Stop when clearing pending wrap consumes the last cursor-left step.
  Otherwise, margin handling can move a restored cursor down to the top
  scrolling margin. Add a regression test that restores pending wrap at
  the left margin above the top scrolling margin.
  ```
- [`a3e80a6`](https://github.com/ghostty-org/ghostty/commit/a3e80a685ed672873aefe8bb07b8516ec3a4175a) terminal: fix word selection across wide characters ([@fornwall](https://github.com/fornwall))
  ```text
  Double-clicking a wide character selects one character or nothing,
  depending on which half is clicked. Resolve wide-character spacers to
  their character so either half selects the whole word, including
  across soft wraps.
  ```
- [`9a5fe9b`](https://github.com/ghostty-org/ghostty/commit/9a5fe9b4b9c843735da41cdbed8d64b668d07546) Support resizing the window with CSI 8 t ([#14375](https://github.com/ghostty-org/ghostty/issues/14375)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Relates to #1115, following my vouch request (#14372).
  
  This implements the xterm window manipulation sequence `CSI 8 ; rows ;
  columns t`
  (XTWINOPS), which lets a program request a terminal size in cells. My
  use case is
  a TUI that wants a sensible starting size instead of asking the user to
  resize.
  It's off by default behind a new `vt-window-resize-allowed` option,
  following
  `title-report` and `vt-kam-allowed`.
  
  **Security.** Since any program, including one over SSH, could send
  this:
  
  - it's disabled unless the user opts in;
  - requests below 40 columns × 10 rows are raised to that size, so a
  program can't
    shrink the window to hide its output (@jcollie's concern in #14372);
  - requests larger than the screen are clamped to the screen;
  - it's ignored in splits, multi-tab windows, the quick terminal, and
  when the
    window manager owns the size (fullscreen, maximized, tiled).
  
  **GNOME.** This works on GNOME Wayland and X11. A floating GTK 4 window
  can resize
  itself by calling `gtk_window_set_default_size()` while mapped: GTK uses
  the new
  default size unless the compositor has fixed the size, and mutter
  accepts a size
  committed by the client. gnome-terminal handles CSI 8 t the same way on
  GTK 4
  (`terminal_window_update_size()`), including skipping maximized,
  fullscreen, and
  tiled windows. One Ghostty-specific catch: the window's compute-size
  handler
  re-asserts the current size when it exceeds the compositor bounds, which
  blocked
  shrinking a window that fills the screen, so it steps aside for a
  requested resize.
  
  Both platforms resize the window by the difference between the requested
  and
  current surface size, so the titlebar, headerbar, and tab bar are
  accounted for.
  A zero or omitted parameter leaves that dimension untouched.
  
  **Testing.** Parser tests added; the full test suite passes on macOS and
  Linux.
  On a macOS release build and on GNOME Shell 50.1 / mutter 50.1 / GTK
  4.22
  (headless, Wayland and Xwayland), verified via `stty size`: exact grids
  for full,
  partial, minimum, and oversized requests; refusals for splits, tabs,
  maximized,
  tiled, and fullscreen, and recovery once undone; and exact sizes at
  monitor
  scales 1.25, 1.5, and 2, with 1.25 text scaling, and with window
  padding.
  
  libghostty-vt parses the sequence but ignores it; exposing it to
  embedders as an
  effect (like `title_changed`) could be a follow-up.
  
  AI disclosure: I used Claude Code to help research, write, and test this
  change.
  I've reviewed all of it and can answer questions about it.
  ```
- [`2fe073a`](https://github.com/ghostty-org/ghostty/commit/2fe073a52c9a9feb11022a61b5196094fb46af55) terminal: fix reverse wrap cursor jump ([#14390](https://github.com/ghostty-org/ghostty/issues/14390)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  With [reverse wrapping](https://ghostty.org/docs/vt/csi/cub) enabled, a
  cursor-left (CUB) or Backspace after DECRC could jump the cursor down to
  the top of the scrolling region.
  
  This happened when the restored cursor had [pending
  wrap](https://ghostty.org/docs/vt/concepts/cursor#pending-wrap-state)
  set and clearing it consumed the whole move, so the left-margin handling
  ran with nothing left to move. Stop once pending wrap is cleared and no
  move remains.
  
  Reproduce:
  
  ```sh
  printf '%b' \
    '\0033[?6;1045l\0033[?7;45;69h\0033[2J' \
    '\0033[1;2sAB\00337\0033[2;5s\0033[3;5r\00338\0033[1DX' \
    '\0033[?45;69l\0033[r\0033[6;1H'
  ```
  
  This saves pending wrap, changes the margins, restores the cursor, then
  moves left and prints `X`.
  
  - Before: `AB` on row 1; `X` at row 3, column 2.
  - After: `AX` on row 1.
  
  Tested with Kitty, which handles this correctly.
  
  AI disclaimer: Created with gpt-6 astra using codex. Iterated on,
  reviewed and manually tested by me.
  ````
- [`69bf1ac`](https://github.com/ghostty-org/ghostty/commit/69bf1ac87f4e0b1a3994fa28744606635791cc14) terminal: fix word selection across wide characters ([#14391](https://github.com/ghostty-org/ghostty/issues/14391)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Double-clicking `日本語` selects one character or nothing, depending on
  which half of a character is clicked. Resolve wide-character spacers to
  their character so either half selects the whole word, including across
  soft wraps.
  
  AI disclaimer: Created with codex and gpt-6 astra. Iterated on, reviewed
  and manually tested by me.
  ```
- [`a412480`](https://github.com/ghostty-org/ghostty/commit/a412480131945f19ce0d7e37b74047526419fd63) tmux: fix list-windows action use-after-free ([@MisterTea](https://github.com/MisterTea))
  ```text
  receivedListWindows stored Action.windows as a slice into a temporary
  ArrayList that is freed on return. Logging that action (or otherwise
  touching the slice) use-after-freed arena state and crashed Ghostty
  immediately after list-windows.
  
  Sync layouts into self.windows first, then point the action at the
  stable self.windows.items slice. Print window counts instead of
  dumping Window with {any}, which walks ArenaAllocator nodes.
  
  #1935
  ```
- [`f327613`](https://github.com/ghostty-org/ghostty/commit/f3276131f10dae0e53cc64dc52f0930ac7bd347a) font: store glyph cache keys as packed u64 ([@j-c-m](https://github.com/j-c-m))
  ```text
  This is a long time follow-up to 93dcb195 and something I originally
  missed in 8824256, as I am making another performance pass through the
  render pipeline.
  
  93dcb195 stopped using the full RenderOptions as identity but left them
  in the key, but packed them for a temporary identity and hashes. This commit
  uses the true identity as the key and stops any temporary packing, making eql
  very cheap allowing us to use a simple fast hash that (mostly) relies on
  glyph ids to distribute accross the hash table.
  
  I don't have a big headline doom-fire-zig fps number maybe 1% 766->774 FPS
  120x40 window on my hardware but it does seem limited somewhere else. However,
  when profiling doom-fire-zig runs the renderGlyph leaf drops from 22% to 1.8%.
  ```
- [`b15fe2e`](https://github.com/ghostty-org/ghostty/commit/b15fe2eea0079a867e947fdf38e281fa76cbe258) font: store CodepointKey as a packed u64 ([@j-c-m](https://github.com/j-c-m))
  ```text
  This is the same treatment to CodepointKey as #14300
  
  vs main this increases doom-fire-zig fps by 3% (749->772).
  
  In my tests these do stack, and in profiling this change moves a ~17%
  getIndex to a ~3% HashMap.
  ```
- [`cc140d4`](https://github.com/ghostty-org/ghostty/commit/cc140d478a1cf42df45ac6e31d1a584b6e601adb) opengl: explicitly initialize surfaceless display ([@RadicalTray](https://github.com/RadicalTray))
- [`9a4ba7d`](https://github.com/ghostty-org/ghostty/commit/9a4ba7d5480ff3bfa1e1b7a6586007fe13ec05c4) tmux: test list-windows action lifetime ([@MisterTea](https://github.com/MisterTea))
- [`c4f15c8`](https://github.com/ghostty-org/ghostty/commit/c4f15c884a71387c837c9d6ae027f9f8ea8a8970) terminal: stop word selection at hard line breaks ([@fornwall](https://github.com/fornwall))
  ```text
  Selecting from the last column could include the next row across a hard
  line break. Check the wrap flag of the row being left before extending
  the selection. Soft-wrapped words still span rows.
  ```
- [`a4f0d9f`](https://github.com/ghostty-org/ghostty/commit/a4f0d9f4a4cdbfbeb2fd86d59dfaad3bd60676ff) terminal: batch special graphics character writes ([@fornwall](https://github.com/fornwall))
  ```text
  Map DEC Special Graphics and British charset bytes during batched cell
  writes instead of calling print() for each character. Keep Unicode and
  single shifts on the scalar path.
  ```
- [`21773fd`](https://github.com/ghostty-org/ghostty/commit/21773fd67137aba39a23a313bceef1ed501bdc8c) opengl: fix nvidia needing `EGL_PLATFORM=surfaceless` to launch correctly ([#14319](https://github.com/ghostty-org/ghostty/issues/14319)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  After the `EGL_SURFACE_TYPE` fix in #14279, I still need to use
  `EGL_PLATFORM=surfaceless` to successfully launch with the Nvidia driver
  and not the fallback Mesa.
  
  To drop `EGL_PLATFORM=surfaceless`, just explicitly initialize a
  surfaceless display.
  
  Related
  https://github.com/ghostty-org/ghostty/discussions/14243#discussioncomment-18455741
  ```
- [`b5dbe15`](https://github.com/ghostty-org/ghostty/commit/b5dbe15813c069bedee43afef04a9bec23353a6d) font: store glyph cache keys as packed u64 ([#14300](https://github.com/ghostty-org/ghostty/issues/14300)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This is a long time follow-up to 93dcb195 and something I originally
  missed in 8824256, as I am making another performance pass through the
  render pipeline.
  
  93dcb195 stopped using the full RenderOptions as identity but left them
  in the key, but packed them for a temporary identity and hashes. This
  commit uses the true identity as the key and stops any temporary
  packing, making eql very cheap allowing us to use a simple fast hash
  that (mostly) relies on glyph ids to distribute accross the hash table.
  
  I don't have a big headline doom-fire-zig fps number maybe 1% 766->774
  FPS 120x40 window on my hardware but it does seem limited somewhere
  else. However, when profiling doom-fire-zig runs the renderGlyph leaf
  drops from 22% to 1.8%.
  
  AI: I used Grok 4.6 to build harnesses for automated testing & profiling
  utilizing ghostty-bench, `cmatrix-b`, and doom-fire-zig (120x40) (not in
  this PR). Initial profiling research and actual code produced by a dumb
  little human (so says the AI).
  ```
- [`8215dd9`](https://github.com/ghostty-org/ghostty/commit/8215dd9ee3af89665532736824afc24889b94cab) terminal: batch special graphics character writes ([#14356](https://github.com/ghostty-org/ghostty/issues/14356)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Batch DEC Special Graphics and British charset bytes in `printSlice()`
  using the existing lookup tables. Single shifts and Unicode input in
  these charsets still use `print()`.
  
  Synthetic benchmark: Repainting an 80×24 box 20,000 times: **296.6 ms →
  42.8 ms (6.9× faster)** in the local ReleaseFast benchmark (median of 10
  runs, 3 warmups).
  
  <details>
  <summary>Reproduce the benchmark</summary>
  
  ```python
  from pathlib import Path
  
  rows = [b"l" + b"q" * 78 + b"k"]
  rows += [b"x" + b" " * 78 + b"x"] * 22
  rows += [b"m" + b"q" * 78 + b"j"]
  frame = b"\x1b[H\x1b(0" + b"\r\n".join(rows) + b"\x1b(B"
  Path("/tmp/box-repaints.bin").write_bytes(frame * 20000)
  ```
  
  Run on the base and this branch:
  
  ```sh
  zig build -Demit-bench -Doptimize=ReleaseFast -Dapp-runtime=none -Demit-exe=false
  hyperfine --warmup 3 --runs 10 'zig-out/bin/ghostty-bench +terminal-stream --terminal-cols=80 --terminal-rows=24 --data=/tmp/box-repaints.bin'
  ```
  
  </details>
  
  AI disclaimer: Created with codex and gpt-6 astra. Iterated on, reviewed
  and manually tested by me.
  ````
- [`aa9ed7d`](https://github.com/ghostty-org/ghostty/commit/aa9ed7d51ca07bd6d6727abe3c3efa138484fceb) terminal: stop word selection at hard line breaks ([#14354](https://github.com/ghostty-org/ghostty/issues/14354)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Double-clicking the last column could select text across a hard newline.
  Check the wrap flag of the row being left so selection stops there.
  Soft-wrapped words still span rows.
  
  To reproduce, run this without resizing afterward, then double-click the
  rightmost `a`. Only the first row should be selected.
  
  ```sh
  python3 - <<EOF
  import os, sys
  cols = os.get_terminal_size().columns
  sys.stdout.write("\r" + "a" * cols + "\r\n" + "b" * cols + "\r\n")
  sys.stdout.flush()
  EOF
  ```
  
  AI disclaimer: Created with codex and gpt-6 astra. Iterated on, reviewed
  and manually tested by me.
  ````
- [`4c1099c`](https://github.com/ghostty-org/ghostty/commit/4c1099ce9654f8d2cb20ac9792978d3979c1ce53) font: store CodepointKey as a packed u64 ([#14301](https://github.com/ghostty-org/ghostty/issues/14301)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This is the same treatment to CodepointKey as #14300
  
  vs main this increases doom-fire-zig fps by 3% (749->772).
  
  In my tests these will stack, and in profiling this change moves a ~17%
  getIndex to a ~3% HashMap.
  ```
- [`982fe90`](https://github.com/ghostty-org/ghostty/commit/982fe90d941e4b4aab4905ffcbcfdea60bd83343) tmux: fix list-windows action use-after-free ([#14262](https://github.com/ghostty-org/ghostty/issues/14262)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Summary
  
  `receivedListWindows` stored `Action.windows` as a slice into a
  temporary ArrayList that is freed on return. Logging that action (or
  otherwise touching the slice) use-after-freed arena state and crashed
  Ghostty immediately after `list-windows`.
  
  Sync layouts into `self.windows` first, then point the action at the
  stable `self.windows.items` slice. Print window counts instead of
  dumping `Window` with `{any}`, which walks `ArenaAllocator` nodes.
  
  This is independently useful today: control mode already logs viewer
  actions.
  
  Related: #1935
  
  ## Test plan
  
  - [x] Regression test fails without the fix due to mismatched
  temporary/viewer window pointers
  - [x] `zig build test -Dtest-filter='session changed resets state'`
  - [x] `zig build test -Dtest-filter=tmux`
  
  ## AI disclosure
  
  This change was prepared with Cursor. I reviewed the slice lifetime and
  the `Action.format` change.
  
  
  Made with [Cursor](https://cursor.com)
  ```

## September 24, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/36070365403), [2](https://github.com/ghostty-org/ghostty/actions/runs/36047047879), [3](https://github.com/ghostty-org/ghostty/actions/runs/35938861377)  
Summary: 3 runs • 62 commits • 18 authors

### Changes

- [`5ca09ac`](https://github.com/ghostty-org/ghostty/commit/5ca09acf6b00a9188a177d40154e35362f7c32c5) build: trim branch name before sanitizing it for the version ([@jcollie](https://github.com/jcollie))
  ```text
  The trailing newline from git rev-parse was being replaced with a
  hyphen, producing versions like 1.3.2-main-+7c40388b2.
  ```
- [`d40bc77`](https://github.com/ghostty-org/ghostty/commit/d40bc77229aae080972af9915cf99dde9a4457b7) build: trim branch name before sanitizing it for the version ([#14386](https://github.com/ghostty-org/ghostty/issues/14386)) ([@jcollie](https://github.com/jcollie))
  ```text
  The trailing newline from git rev-parse was being replaced with a
  hyphen, producing versions like 1.3.2-main-+7c40388b2.
  
  Fixes #14385
  ```
- [`c273d6f`](https://github.com/ghostty-org/ghostty/commit/c273d6ff692f8b9ad3df595e74073d68a6341d39) Update VOUCHED list ([#14387](https://github.com/ghostty-org/ghostty/issues/14387)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14384#discussioncomment-18586072)
  from @jcollie.
  
  Vouch: @pltrz
  ```
- [`d4c88d8`](https://github.com/ghostty-org/ghostty/commit/d4c88d8069912b653d707191388ca98e24751f12) Update VOUCHED list ([#14241](https://github.com/ghostty-org/ghostty/issues/14241)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14240#discussioncomment-18444371)
  from @jcollie.
  
  Vouch: @JuaniRaggio
  ```
- [`fe9cf6a`](https://github.com/ghostty-org/ghostty/commit/fe9cf6a26691fb7dbfc260eb169a801ca4b9790f) build: fully transition away from cImport/addTranslateC ([@vancluever](https://github.com/vancluever))
  ```text
  This migrates all remaining uses of cImport (and addTranslateC for good
  measure) to using translate-c for C translation, ensuring that we are
  ready for when cImport is removed from the language, and also that all
  sources of C translation are using the same snapshot of the external
  package (when can then be updated when we need to fix something).
  
  A couple of notes:
  
  * A few options have been added to support the new translations, namely
    the ability to link libraries (passed through to linkLibrary on the
    Translator side) and whether or not to initialize default values
    (looks like cImport did this without a way to control it, but
    translate-c does not do it by default).
  
  * Using the new library linking option actually simplifies the process
    of translating a number of the C packages as we have been shipping the
    necessary headers for these packages already with the applicable
    libraries. For some of the more complex translation processes though,
    we still include the appropriate directories directly.
  ```
- [`4dfa44e`](https://github.com/ghostty-org/ghostty/commit/4dfa44ecd95a9e6c72188484c2a2871298800e8a) bash: use passed exit status in precmd ([@jparise](https://github.com/jparise))
  ```text
  The Bash 4.4+ prompt hook saves the command status before doing its own
  work and passes it to __ghostty_precmd. The function ignored that
  argument and instead read the hook invocation status, causing command
  end markers to report zero.
  
  Use the explicit argument when present while retaining the current
  status fallback required by the older bash-preexec path.
  
  See #14247
  ```
- [`ed7f046`](https://github.com/ghostty-org/ghostty/commit/ed7f046ee4dee89e5e8bbbecbc67ee14ac1f10d1) bash: recognize attributed prompt command arrays ([@jparise](https://github.com/jparise))
  ```text
  Bash includes additional variable attributes in declare output, so an
  exported indexed array is reported with an -ax prefix instead of -a.
  Match the indexed-array prefix without requiring a following space so
  these values continue through the array-preserving path.
  ```
- [`591ccac`](https://github.com/ghostty-org/ghostty/commit/591ccacbdfa59945cb4f5b015390d0b8d416a7f0) bash: preserve exit status across prompt commands ([@jparise](https://github.com/jparise))
  ```text
  Existing scalar PROMPT_COMMAND entries can overwrite the last command's
  status before Ghostty's appended hook runs. Capture and restore the
  status before those commands, then consume the saved value in the final
  hook.
  
  Keep array hooks as independent entries because Bash 5.1 and newer
  restore the original status for each entry. Preserve the existing
  PROMPT_COMMAND type and safely handle inherited prompt commands where
  Ghostty's function definitions are absent.
  
  This retains the fast Bash 4.4+ PS0 integration rather than using
  bash-preexec's DEBUG trap.
  
  See #14247
  ```
- [`8482d54`](https://github.com/ghostty-org/ghostty/commit/8482d5454e0eee8329cadf2711be78c40298b6ec) bash: fix OSC 133;D status always zero ([#14250](https://github.com/ghostty-org/ghostty/issues/14250)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The Bash 4.4+ prompt hook saves the command status before doing its own
  work and passes it to __ghostty_precmd. The function ignored that
  argument and instead read the hook invocation status, causing command
  end markers to report zero.
  
  Also, existing scalar PROMPT_COMMAND entries can overwrite the last
  command's status before Ghostty's appended hook runs. Capture and
  restore the status before those commands, then consume the saved value
  in the final hook.
  
  Fixes #14247
  ```
- [`8fff9d6`](https://github.com/ghostty-org/ghostty/commit/8fff9d6e98ccb37930629429dafdb02ff97faaea) build: fully transition away from cImport/addTranslateC ([#14246](https://github.com/ghostty-org/ghostty/issues/14246)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This migrates all remaining uses of `cImport` (and `addTranslateC` for
  good measure) to using translate-c for C translation, ensuring that we
  are ready for when `cImport` is removed from the language, and also that
  all sources of C translation are using the same snapshot of the external
  package (when can then be updated when we need to fix something).
  
  A couple of notes:
  
  * A few options have been added to support the new translations, namely
  the ability to link libraries (passed through to `linkLibrary` on the
  Translator side) and whether or not to initialize default values (looks
  like `cImport` did this without a way to control it, but translate-c
  does not do it by default).
  
  * Using the new library linking option actually simplifies the process
  of translating a number of the C packages as we have been shipping the
  necessary headers for these packages already with the applicable
  libraries. For some of the more complex translation processes though, we
  still include the appropriate directories directly.
  ```
- [`f9a3f24`](https://github.com/ghostty-org/ghostty/commit/f9a3f24a56bf05f70894e1a084809d4fffadf420) Update VOUCHED list ([#14256](https://github.com/ghostty-org/ghostty/issues/14256)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14249#discussioncomment-18467661)
  from @mitchellh.
  
  Vouch: @MisterTea
  ```
- [`494e413`](https://github.com/ghostty-org/ghostty/commit/494e41374e536f80fafa9cb30c6d1d8cb1e77110) i18n(ru): refine Russian translation ([@derVedro](https://github.com/derVedro))
- [`a4031c8`](https://github.com/ghostty-org/ghostty/commit/a4031c8e3f94f40df712de7cdf6fd4f6c17980c6) bash: detect hooks in prompt command arrays ([@jparise](https://github.com/jparise))
  ```text
  The delimiter-based guard treats PROMPT_COMMAND as a semicolon-separated
  command list. Indexed array expansion joins elements with spaces instead,
  so a hook appended after an existing element is not detected when the
  integration is sourced again.
  
  Match the full internal hook command as a substring so the guard works
  for both scalar and array values. This intentionally gives up command
  boundary matching; the private function name and redirection keep an
  incidental match unlikely.
  ```
- [`a1bf5b5`](https://github.com/ghostty-org/ghostty/commit/a1bf5b5e113b1b0c4e30c87ecbe746bd07eda3e4) embedded: route split and close C APIs through performBindingAction ([@MisterTea](https://github.com/MisterTea))
  ```text
  macOS menus call ghostty_surface_split, split_focus, and request_close
  directly, while keybinds go through Surface.performBindingAction. GTK
  already uses that path for splits and close. Route the embedded C APIs
  the same way so menus and keybinds share one hook.
  ```
- [`ab34b8b`](https://github.com/ghostty-org/ghostty/commit/ab34b8b131eb2d60e7d22838dd6d77b98fec04b3) opengl: explicitly set EGL_SURFACE_TYPE ([@pluiedev](https://github.com/pluiedev))
- [`c15e2f7`](https://github.com/ghostty-org/ghostty/commit/c15e2f79922620f8651b92bb55662b19ce9505bb) opengl: EGLattrib arrays need no explicit sentinel ([@pluiedev](https://github.com/pluiedev))
  ```text
  Array literals automagically gain the sentinel when assigned the correct
  type. Neat, huh?
  
  See https://ziglang.org/documentation/0.16.0/#Sentinel-Terminated-Arrays
  ```
- [`851cd4d`](https://github.com/ghostty-org/ghostty/commit/851cd4dc13adbd17886ab1baf46280d27a6c9fa6) gtk: disable Vulkan again, remove old version gates ([@pluiedev](https://github.com/pluiedev))
  ```text
  Vulkan is causing problems again...
  
  Also our minimum GTK version requirement is 4.18 now, so we can nuke all
  the old checks
  ```
- [`0fca3d3`](https://github.com/ghostty-org/ghostty/commit/0fca3d34a56a420da92a7cb20109e71d523f7bf6) gtk/imgui_widget: remove direct call to glClearColor ([@pluiedev](https://github.com/pluiedev))
  ```text
  Since the refactor to move our OpenGL context off-thread there is no more
  GLAD context loaded on the main thread for this widget, so calling ANY
  OpenGL function will crash the entire app.
  
  I don't think the call even worked as intended? I at least can't seem to
  tell any difference when the clear commands are simply removed.
  Maybe they were useful before.
  ```
- [`590ab15`](https://github.com/ghostty-org/ghostty/commit/590ab157f4f05286888f5838f4167fe4fcc07be2) opengl/Sampler: handle enum parameters correctly ([@pluiedev](https://github.com/pluiedev))
  ```text
  I'm so dumb like honestly, always double check if your unreachables
  are *comptime*. Whether the value being switched on is comptime or not
  does not matter
  ```
- [`f5c056d`](https://github.com/ghostty-org/ghostty/commit/f5c056d3045b4b9baf86400a95e598044a0573b5) font: import Constraint from Glyph.zig in nerd-font codegen ([@j-c-m](https://github.com/j-c-m))
  ```text
  1c0aac54b moved RenderOptions.Constraint from face.zig to Glyph.zig
  and updated nerd_font_attributes.zig. This does the matching change to
  the generator.
  ```
- [`57bdb8c`](https://github.com/ghostty-org/ghostty/commit/57bdb8c443e39c523d543f6c3f50a9370c35c314) i18n(ru): small fixes ([@derVedro](https://github.com/derVedro))
  ```text
  хорошо!
  ```
- [`5de703a`](https://github.com/ghostty-org/ghostty/commit/5de703a1b6ca0b91fcebe932b44be1df2de0a683) i18n: refine Russian translation ([#14257](https://github.com/ghostty-org/ghostty/issues/14257)) ([@00-kat](https://github.com/00-kat))
  ```text
  We had a small conversation in the last Russian translation PR #13809,
  and @korikhin made a good point about how the translation could be
  improved, something everyone had overlooked until then.
  ```
- [`cd8daf9`](https://github.com/ghostty-org/ghostty/commit/cd8daf9eb6fe85ed6ec1c4450b34fff84abf9bea) build(deps): bump docker/build-push-action from 7.3.0 to 7.4.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [docker/build-push-action](https://github.com/docker/build-push-action) from 7.3.0 to 7.4.0.
  - [Release notes](https://github.com/docker/build-push-action/releases)
  - [Commits](https://github.com/docker/build-push-action/compare/53b7df96c91f9c12dcc8a07bcb9ccacbed38856a...c3c9e263c25d99ce0380d002d59b67737d91b0dc)
  
  ---
  updated-dependencies:
  - dependency-name: docker/build-push-action
    dependency-version: 7.4.0
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`98f2e3e`](https://github.com/ghostty-org/ghostty/commit/98f2e3e6dce6f4198254c9d8ccf5de50c94b17ca) build(deps): bump namespacelabs/nscloud-cache-action from 1.6.1 to 1.7.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [namespacelabs/nscloud-cache-action](https://github.com/namespacelabs/nscloud-cache-action) from 1.6.1 to 1.7.0.
  - [Release notes](https://github.com/namespacelabs/nscloud-cache-action/releases)
  - [Commits](https://github.com/namespacelabs/nscloud-cache-action/compare/c5f8dab7560444c4bf8dbc64f1b203431873c547...1124a6f3ce44e5cf84cc22111530961f4d2a15f9)
  
  ---
  updated-dependencies:
  - dependency-name: namespacelabs/nscloud-cache-action
    dependency-version: 1.7.0
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`e842d76`](https://github.com/ghostty-org/ghostty/commit/e842d763ce2f4d7739a9b405d302dafb3ce96a25) Update VOUCHED list ([#14290](https://github.com/ghostty-org/ghostty/issues/14290)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14289#issuecomment-5728440286)
  from @trag1c.
  
  Vouch: @cristeahub
  ```
- [`87b6065`](https://github.com/ghostty-org/ghostty/commit/87b60655bffa8632bf06740291d68fb87440dfa7) Update the Norwegian translation ([@cristeahub](https://github.com/cristeahub))
  ```text
  These are mostly nitpicky changes that focuses on the following:
  
  - Consistent langauge (marker, last inn, tøm)
  - Grammatical fixes
  - Language flow improvements
  
  There are still a few things that could be changed, but I felt these
  changes are the most impactful and makes the language better.
  ```
- [`cb7db24`](https://github.com/ghostty-org/ghostty/commit/cb7db2490bb7ff3bad14a1a375c8dfb34d902e62) Update the Norwegian translation ([#14289](https://github.com/ghostty-org/ghostty/issues/14289)) ([@trag1c](https://github.com/trag1c))
  ```text
  These are mostly nitpicky changes that focuses on the following:
  
  - Consistent langauge (marker, last inn, tøm)
  - Grammatical fixes
  - Language flow improvements
  
  There are still a few things that could be changed, but I felt these
  changes are the most impactful and makes the language better.
  ```
- [`86f4490`](https://github.com/ghostty-org/ghostty/commit/86f449013ed4ca4096395de5b9798a962cce0944) Update VOUCHED list ([#14292](https://github.com/ghostty-org/ghostty/issues/14292)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14291#discussioncomment-18500537)
  from @pluiedev.
  
  Vouch: @KonstantinHudyakov
  ```
- [`12542b3`](https://github.com/ghostty-org/ghostty/commit/12542b3923106fd13e4f5d0f9b7c8b65843a1836) deps: Update uucode for Unicode 18 ([@jacobsandlund](https://github.com/jacobsandlund))
- [`aef7aae`](https://github.com/ghostty-org/ghostty/commit/aef7aaeb88423d7b483e857042a4135d8d5143f1) check-zig-hash --update ([@jacobsandlund](https://github.com/jacobsandlund))
- [`1bd494c`](https://github.com/ghostty-org/ghostty/commit/1bd494cf956e1c57267b7836eceb77e872b17f6e) build(deps): bump namespacelabs/nscloud-cache-action from 1.6.1 to 1.7.0 ([#14285](https://github.com/ghostty-org/ghostty/issues/14285)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [namespacelabs/nscloud-cache-action](https://github.com/namespacelabs/nscloud-cache-action)
  from 1.6.1 to 1.7.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/namespacelabs/nscloud-cache-action/releases">namespacelabs/nscloud-cache-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v1.7.0</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>fix: Stabilize Brew and Maven cache mode tests by <a
  href="https://github.com/sebawita"><code>@​sebawita</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/170">namespacelabs/nscloud-cache-action#170</a></li>
  <li>fix: update actions toolkit to 0.5.0 by <a
  href="https://github.com/rcrowe"><code>@​rcrowe</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/175">namespacelabs/nscloud-cache-action#175</a></li>
  <li>Add cache miss documentation hint by <a
  href="https://github.com/sebawita"><code>@​sebawita</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/169">namespacelabs/nscloud-cache-action#169</a></li>
  <li>fix: update vulnerable transitive dependencies by <a
  href="https://github.com/rcrowe"><code>@​rcrowe</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/176">namespacelabs/nscloud-cache-action#176</a></li>
  <li>test: move Vitest mocks to module scope by <a
  href="https://github.com/rcrowe"><code>@​rcrowe</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/177">namespacelabs/nscloud-cache-action#177</a></li>
  </ul>
  <h2>New Contributors</h2>
  <ul>
  <li><a href="https://github.com/sebawita"><code>@​sebawita</code></a>
  made their first contribution in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/170">namespacelabs/nscloud-cache-action#170</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/namespacelabs/nscloud-cache-action/compare/v1.6.1...v1.7.0">https://github.com/namespacelabs/nscloud-cache-action/compare/v1.6.1...v1.7.0</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/1124a6f3ce44e5cf84cc22111530961f4d2a15f9"><code>1124a6f</code></a>
  test: move Vitest mocks to module scope (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/177">#177</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/e40c60c47e26a5b911d6a0683a7294401e5f2dbe"><code>e40c60c</code></a>
  fix: update vulnerable transitive dependencies (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/176">#176</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/7db012f73e34bd0e002c17e6ada243fc8b89008f"><code>7db012f</code></a>
  Add cache miss documentation hint (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/169">#169</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/3199dcd520c302741adae1d82317e99e3db7bf94"><code>3199dcd</code></a>
  fix: update actions toolkit to 0.5.0 (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/175">#175</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/ac29750009f671e320b31cb40043262d8679ed61"><code>ac29750</code></a>
  Stabilize Brew and Maven cache mode tests (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/170">#170</a>)</li>
  <li>See full diff in <a
  href="https://github.com/namespacelabs/nscloud-cache-action/compare/c5f8dab7560444c4bf8dbc64f1b203431873c547...1124a6f3ce44e5cf84cc22111530961f4d2a15f9">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=namespacelabs/nscloud-cache-action&package-manager=github_actions&previous-version=1.6.1&new-version=1.7.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`89efb12`](https://github.com/ghostty-org/ghostty/commit/89efb129b8cc5ed6249a7afaa4ea3900396f87c0) build(deps): bump docker/build-push-action from 7.3.0 to 7.4.0 ([#14284](https://github.com/ghostty-org/ghostty/issues/14284)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [docker/build-push-action](https://github.com/docker/build-push-action)
  from 7.3.0 to 7.4.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/docker/build-push-action/releases">docker/build-push-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v7.4.0</h2>
  <ul>
  <li>Use the shared error helper for Buildx commands by <a
  href="https://github.com/crazy-max"><code>@​crazy-max</code></a> in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1620">docker/build-push-action#1620</a></li>
  <li>Prevent workflow command injection in metadata logs by <a
  href="https://github.com/crazy-max"><code>@​crazy-max</code></a> in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1617">docker/build-push-action#1617</a></li>
  <li>Bump <code>@​docker/actions-toolkit</code> from 0.92.0 to 0.100.0 in
  <a
  href="https://redirect.github.com/docker/build-push-action/pull/1614">docker/build-push-action#1614</a>
  <a
  href="https://redirect.github.com/docker/build-push-action/pull/1618">docker/build-push-action#1618</a>
  <a
  href="https://redirect.github.com/docker/build-push-action/pull/1621">docker/build-push-action#1621</a></li>
  <li>Bump <code>@​humanfs/node</code> from 0.16.7 to 0.16.8 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1609">docker/build-push-action#1609</a></li>
  <li>Bump brace-expansion from 1.1.13 to 1.1.18 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1592">docker/build-push-action#1592</a></li>
  <li>Bump csv-parse from 7.0.0 to 7.0.2 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1613">docker/build-push-action#1613</a></li>
  <li>Bump js-yaml from 4.3.0 to 4.3.2 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1605">docker/build-push-action#1605</a>
  <a
  href="https://redirect.github.com/docker/build-push-action/pull/1615">docker/build-push-action#1615</a></li>
  <li>Bump nanoid from 3.3.16 to 3.3.18 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1611">docker/build-push-action#1611</a></li>
  <li>Bump postcss from 8.5.10 to 8.5.25 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1590">docker/build-push-action#1590</a></li>
  <li>Bump postcss-selector-parser from 7.1.1 to 7.1.5 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1606">docker/build-push-action#1606</a></li>
  <li>Bump sigstore from 4.1.0 to 4.1.1 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1577">docker/build-push-action#1577</a></li>
  <li>Bump undici from 6.27.0 to 6.28.0 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1594">docker/build-push-action#1594</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/docker/build-push-action/compare/v7.3.0...v7.4.0">https://github.com/docker/build-push-action/compare/v7.3.0...v7.4.0</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/docker/build-push-action/commit/c3c9e263c25d99ce0380d002d59b67737d91b0dc"><code>c3c9e26</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1621">#1621</a>
  from docker/dependabot/npm_and_yarn/docker/actions-t...</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/459b6741834dcd35f946352017e7675bd2089d42"><code>459b674</code></a>
  [dependabot skip] chore: update generated content</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/4dedcb23c91d79c1629bf53ec2c3bcfffef5b34e"><code>4dedcb2</code></a>
  chore(deps): Bump <code>@​docker/actions-toolkit</code> from 0.99.0 to
  0.100.0</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/379bf63a979bd70751945601fa04c50674509952"><code>379bf63</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1620">#1620</a>
  from crazy-max/buildx-error-message</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/9877975c9e0b0b661592ff61049069507f9bc2f6"><code>9877975</code></a>
  chore: update generated content</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/7ed0556ffafb8eb312463411ef0a84a1dfe24d94"><code>7ed0556</code></a>
  use the shared Buildx error summary helper</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/91670ba5a4df99a24efff8637a78c83fd1b0f6b1"><code>91670ba</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1618">#1618</a>
  from docker/dependabot/npm_and_yarn/docker/actions-t...</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/80dbc8614a5c0ce4356740f69179cf829ecdc79a"><code>80dbc86</code></a>
  [dependabot skip] chore: update generated content</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/50cac3a3b6f55e6015d6483d1dd72a3ecb90d20d"><code>50cac3a</code></a>
  chore(deps): Bump <code>@​docker/actions-toolkit</code> from 0.98.0 to
  0.99.0</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/03b4d6cac0163b44733e1fa60adfd6da560ee4d1"><code>03b4d6c</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1617">#1617</a>
  from crazy-max/fix-metadata-workflow-commands</li>
  <li>Additional commits viewable in <a
  href="https://github.com/docker/build-push-action/compare/53b7df96c91f9c12dcc8a07bcb9ccacbed38856a...c3c9e263c25d99ce0380d002d59b67737d91b0dc">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=docker/build-push-action&package-manager=github_actions&previous-version=7.3.0&new-version=7.4.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`d3f5910`](https://github.com/ghostty-org/ghostty/commit/d3f5910cc45e53c5341b3e2dacde839b30434a6e) font: import Constraint from Glyph.zig in nerd-font codegen ([#14282](https://github.com/ghostty-org/ghostty/issues/14282)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  1c0aac54b moved RenderOptions.Constraint from face.zig to Glyph.zig and
  updated nerd_font_attributes.zig. This does the matching change to the
  generator.
  ```
- [`85bfc98`](https://github.com/ghostty-org/ghostty/commit/85bfc983a519890cf5bf2ee7f5b9542817043a1f) gtk,opengl: cleanup & fixes for [#14052](https://github.com/ghostty-org/ghostty/issues/14052) ([#14279](https://github.com/ghostty-org/ghostty/issues/14279)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes most issues mentioned in #14243, #14254 and elsewhere e.g. on
  Discord. Will add more fixes if they can be solidly reproduced.
  
  Please review each commit individually.
  ```
- [`0a08614`](https://github.com/ghostty-org/ghostty/commit/0a08614aaafe8aafd1891750b1644c631896c703) bash: detect hooks in prompt command arrays ([#14266](https://github.com/ghostty-org/ghostty/issues/14266)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The delimiter-based guard treats PROMPT_COMMAND as a semicolon-separated
  command list. Indexed array expansion joins elements with spaces
  instead, so a hook appended after an existing element is not detected
  when the integration is sourced again.
  
  Match the full internal hook command as a substring so the guard works
  for both scalar and array values. This intentionally gives up command
  boundary matching; the private function name and redirection keep an
  incidental match unlikely.
  ```
- [`1e3cd1a`](https://github.com/ghostty-org/ghostty/commit/1e3cd1a24673be7e352c1d1f716d262798d37f7f) embedded: route split and close C APIs through performBindingAction ([#14261](https://github.com/ghostty-org/ghostty/issues/14261)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Summary
  
  macOS menus call `ghostty_surface_split`, `split_focus`, and
  `request_close` directly, while keybinds go through
  `Surface.performBindingAction`. GTK already uses that path for splits
  and close. Route the embedded C APIs the same way so menus and keybinds
  share one hook.
  
  Behavior without any extra Surface hook is unchanged:
  `performBindingAction` still forwards splits to the app and
  `close_surface` still closes.
  
  ## Test plan
  
  - [x] `zig build test -Demit-macos-app=false` (compiles; these C exports
  have no unit test)
  
  ## AI disclosure
  
  This change was prepared with Cursor. I reviewed the C API routing and
  how it compares to GTK's existing `performBindingAction` path.
  
  
  Made with [Cursor](https://cursor.com)
  ```
- [`c55f213`](https://github.com/ghostty-org/ghostty/commit/c55f213aa2a3aa1d852f9f91cb4bd95d55982f48) terminal: add option to disable scrollback pull on resize ([@mitchellh](https://github.com/mitchellh))
  ```text
  #14294
  
  This adds a boolean flag throughout the Zig API and C API to control
  whether resizing can pull scrollback back into the active area. The
  default is true, which is the existing behavior.
  
  Ptys that keep their own screen buffer without scrollback (namely
  Windows ConPTY) can't pull rows back, so after a resize that pulls we
  disagree with the pty about what is on screen and subsequent output
  lands in the wrong place.
  
  Row growth always appends blank rows at the bottom when pulling is
  disabled.
  
  Refs:
  https://github.com/microsoft/terminal/blob/7c92ecd037476f957809d0813b14d8bc44bb071a/src/cascadia/TerminalCore/Terminal.cpp#L380-L406
  https://github.com/xtermjs/xterm.js/blob/c58ea3637f3968e0e6e79cd92cf9aace7ef89ee2/src/common/buffer/Buffer.ts#L194-L197
  https://github.com/wezterm/wezterm/blob/b09b56c29c1e367e598b60ca266e2cc9038751e0/term/src/screen.rs#L268-L288
  ```
- [`b32f20f`](https://github.com/ghostty-org/ghostty/commit/b32f20f3e8d25bb925ec545c54498e93518e7ced) terminal: add option to disable scrollback pull on resize ([#14296](https://github.com/ghostty-org/ghostty/issues/14296)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  #14294
  
  This adds a boolean flag throughout the Zig API and C API to control
  whether resizing can pull scrollback back into the active area. The
  default is true, which is the existing behavior.
  
  Ptys that keep their own screen buffer without scrollback (namely
  Windows ConPTY) can't pull rows back, so after a resize that pulls we
  disagree with the pty about what is on screen and subsequent output
  lands in the wrong place.
  
  Row growth always appends blank rows at the bottom when pulling is
  disabled.
  
  Refs:
  
  https://github.com/microsoft/terminal/blob/7c92ecd037476f957809d0813b14d8bc44bb071a/src/cascadia/TerminalCore/Terminal.cpp#L380-L406
  https://github.com/xtermjs/xterm.js/blob/c58ea3637f3968e0e6e79cd92cf9aace7ef89ee2/src/common/buffer/Buffer.ts#L194-L197
  https://github.com/wezterm/wezterm/blob/b09b56c29c1e367e598b60ca266e2cc9038751e0/term/src/screen.rs#L268-L288
  ```
- [`a925a97`](https://github.com/ghostty-org/ghostty/commit/a925a97e37c4d3598d263ec55682ef4f20b2009a) renderer/opengl: fix missing gl.finish() between present request and sharing presented frame ([@AnthonyZhOon](https://github.com/AnthonyZhOon))
- [`790c6b6`](https://github.com/ghostty-org/ghostty/commit/790c6b60f730a17fef267ffde0817c55fa7d62d3) Update VOUCHED list ([@github-actions[bot]](https://github.com/apps/github-actions))
  ```text
  https://github.com/ghostty-org/ghostty/discussions/14305#discussioncomment-DC_kwDOHFhdAs4BGpVY
  ```
- [`ca9b038`](https://github.com/ghostty-org/ghostty/commit/ca9b0384f22fc018d81b9f69cada01677f565126) Update VOUCHED list ([#14308](https://github.com/ghostty-org/ghostty/issues/14308)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14305#discussioncomment-18519384)
  from @jcollie.
  
  Vouch: @thomasfedb
  ```
- [`a301054`](https://github.com/ghostty-org/ghostty/commit/a3010543b0c39b98a81ace9f50b1910ae641c8c1) Update VOUCHED list ([#14307](https://github.com/ghostty-org/ghostty/issues/14307)) ([@jcollie](https://github.com/jcollie))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14305#discussioncomment-18519384)
  from @jcollie.
  
  Vouch: @thomasfedb
  ```
- [`9cdbf79`](https://github.com/ghostty-org/ghostty/commit/9cdbf798d904769d0b3514658f3684b24850487d) deps: Update uucode for Unicode 18 ([#14293](https://github.com/ghostty-org/ghostty/issues/14293)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This updates `uucode` for the new (as of 9/16) Unicode 18 release. See
  the [PR on uucode](https://github.com/jacobsandlund/uucode/pull/58) for
  details.
  
  In short, mostly Unicode 18 is the typical Emoji, Scripts, Blocks
  additions, but it also simplifies Grapheme Breaking for Indic Conjunct
  Break, somewhat. Also in the `uucode` PR is the results of the
  `+grapheme-break` benchmark showing this has no performance impact.
  
  Note a new `.table_len` and `.fromTableIndex` help us precompute the
  lookup table, though the slightly more complicated index calculation
  needs a bump in @setEvalBranchQuota.
  
  Testing note, I've been running this on my mac, but my linux machine has
  been collecting dust :(
  
  **AI disclaimer**: I used Astra and Fable to develop this, but closely
  reviewed and steered the code such that there is a cleaner split with
  `indic_conjunct_break_linker_extend` and
  `indic_conjunct_break_linker_other`, and arranged the new `BreakState`
  for easier manipulation while still keeping the same precomputed table
  size (the naive switch from 5 enum values to 3 enum values plus a
  boolean was going to raise the size a bit).
  ```
- [`079502e`](https://github.com/ghostty-org/ghostty/commit/079502e23e2c296d200776e03058aab81703c93d) terminal: look up modes by number with a comptime sorted set ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds `datastruct.ComptimeIntSet`, a set of comptime-known integer
  keys with a fast runtime lookup, and uses it in `modes.modeFromInt` to
  map a mode number to its mode.
  
  Previously `modesFromInt` did an inline for comparing every entry.
  In disassembly this showed up as hundreds of branches and instructions.
  
  This is admittedly a micro-optimization but it has a really practical
  reason: checking some of these modes is critical on the render path
  (e.g. synchronized rendering) and every nanosecond is something we want
  to save. Plus, the complexity of this change is pretty low.
  
    C API get mode 2026:          10.5 ns ->  3.2 ns
    C API get unknown mode:       10.5 ns ->  1.8 ns
    C API get KAM (first entry):   3.8 ns ->  3.2 ns
    stream CSI ? 2026 h/l:        20.6 ns -> 12.7 ns per sequence
    stream set/reset 3 modes:     46.0 ns -> 28.0 ns per sequence
    stream DECRQM:                57.0 ns -> 41.0 ns per sequence
  ```
- [`01a8d3a`](https://github.com/ghostty-org/ghostty/commit/01a8d3af223dbb5ba3ddbf0a8f3d7820e304880a) terminal: look up modes by number with a comptime sorted set ([#14316](https://github.com/ghostty-org/ghostty/issues/14316)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds `datastruct.ComptimeIntSet`, a set of comptime-known integer
  keys with a fast runtime lookup, and uses it in `modes.modeFromInt` to
  map a mode number to its mode.
  
  Previously `modesFromInt` did an inline for comparing every entry. In
  disassembly this showed up as hundreds of branches and instructions.
  
  This is admittedly a micro-optimization but it has a really practical
  reason: checking some of these modes is critical on the render path
  (e.g. synchronized rendering) and every nanosecond is something we want
  to save. Plus, the complexity of this change is pretty low.
  
  >   C API get mode 2026:          10.5 ns ->  3.2 ns
  >   C API get unknown mode:       10.5 ns ->  1.8 ns
  >   C API get KAM (first entry):   3.8 ns ->  3.2 ns
  >   stream CSI ? 2026 h/l:        20.6 ns -> 12.7 ns per sequence
  >   stream set/reset 3 modes:     46.0 ns -> 28.0 ns per sequence
  >   stream DECRQM:                57.0 ns -> 41.0 ns per sequence
  ```
- [`e507794`](https://github.com/ghostty-org/ghostty/commit/e5077949834c3291a9434f88b38a381d8f5fedfc) libghostty-vt: add render hold effect for synchronized output (mode 2026) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds a new callback `render_hold` to the libghostty-vt API (Zig and
  C). This callback is called whenever the embedder should snapshot the
  last rendered frame at the current terminal state (currently only for mode
  2026). The name is generic so other sources in the future might reuse it.
  
  Before this, libghostty-vt did nothing for mode 2026 beyond setting
  the mode bit, so an embedder could only check the mode before each
  draw and skip the render state update when it was set.
  
  That has two problems:
  
    1. The frame left on screen is whatever was drawn last, which
       can be older than what the program intended or even a half-drawn
       frame.
    2. If the program resets and sets the mode again between two
       draws (or within a single write), the mode never appears to turn off
       and the finished frame in between is lost, so a program that draws
       continuously can appear frozen.
  
  With the callback, an embedder updates its render state when a hold begins,
  which captures exactly the frame the program wants left on screen,
  and then skips updates until the hold ends.
  
  This actually is a more robust implementation than Ghostty GUI has so I
  plan to follow up to fix that!
  ```
- [`56a3437`](https://github.com/ghostty-org/ghostty/commit/56a3437a7f51796d7946584043229c2f15c70583) libghostty-vt: add render hold effect for synchronized output ([#14317](https://github.com/ghostty-org/ghostty/issues/14317)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds a new callback `render_hold` to the libghostty-vt API (Zig and
  C). This callback is called whenever the embedder should snapshot the
  last rendered frame at the current terminal state (currently only for
  mode 2026). The name is generic so other sources in the future might
  reuse it.
  
  Before this, libghostty-vt did nothing for mode 2026 beyond setting the
  mode bit, so an embedder could only check the mode before each draw and
  skip the render state update when it was set.
  
  That has two problems:
  
  1. The frame left on screen is whatever was drawn last, which can be
  older than what the program intended or even a half-drawn frame.
  2. If the program resets and sets the mode again between two draws (or
  within a single write), the mode never appears to turn off and the
  finished frame in between is lost, so a program that draws continuously
  can appear frozen.
  
  With the callback, an embedder updates its render state when a hold
  begins, which captures exactly the frame the program wants left on
  screen, and then skips updates until the hold ends.
  
  This actually is a more robust implementation than Ghostty GUI has so I
  plan to follow up to fix that!
  ```
- [`27e8b3f`](https://github.com/ghostty-org/ghostty/commit/27e8b3fa85d9cf8c7cd5ae2ced348bcb0a4fba9c) Update VOUCHED list ([#14320](https://github.com/ghostty-org/ghostty/issues/14320)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14319#issuecomment-5747979152)
  from @pluiedev.
  
  Vouch: @RadicalTray
  ```
- [`8619bec`](https://github.com/ghostty-org/ghostty/commit/8619becb23a8f577694cd50321bdf7adb8473364) opengl: validate exported DMA-BUF planes ([@EriksRemess](https://github.com/EriksRemess))
  ```text
  Maximizing the window could crash the app when EGL returned an invalid DMA-BUF plane descriptor.
  GDK later hit a fatal assertion while downloading the texture.
  ```
- [`3c47ca1`](https://github.com/ghostty-org/ghostty/commit/3c47ca159368eb4a860ffe5333abdf4a85b2767b) Sync CODEOWNERS vouch list ([#14327](https://github.com/ghostty-org/ghostty/issues/14327)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Sync CODEOWNERS owners with vouch list.
  
  ## Added Users
  
  - @dungdm93
  ```
- [`9fc8d9e`](https://github.com/ghostty-org/ghostty/commit/9fc8d9ebdf29305fe6782a81969440d9a523ae60) gtk: streamline surface overrides ([@neoto](https://github.com/neoto))
  ```text
  Moves code related to surface overrides to its own file to help
  with argument type redefinition in a bunch of places.
  ```
- [`a79d958`](https://github.com/ghostty-org/ghostty/commit/a79d95825229a81008c518ef10a8529e6d6efebd) gtk: streamline surface overrides ([#14332](https://github.com/ghostty-org/ghostty/issues/14332)) ([@jcollie](https://github.com/jcollie))
  ```text
  While investigating the EGL context being created twice (is this known
  and/or expected?), I noticed that the `overrides` argument was being
  repeated in a bunch of places. I couldn't help but do something about it
  so here I am.
  
  This essentially just moves things around, placing related logic in a
  nicer box. I haven't changed anything when it comes to functionality.
  
  Feel free to close if this isn't something worthwhile.
  
  CC @jcollie
  ```
- [`4ff6993`](https://github.com/ghostty-org/ghostty/commit/4ff699343ad039bc73f970ae104cbcec42cc070c) gtk,opengl: fix misplaced gl.finish() when exporting frames ([#14304](https://github.com/ghostty-org/ghostty/issues/14304)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  We must call `gl.finish()` after the present GL calls and before adding
  the exported frame handle to the readable LatestFrame slot that the
  app-thread reads.
  After the fixes in #14279 I could reliably reproduce fcitx5 with mozc
  japanese triggering out of order frame states. I tracked this down to
  the unsynchronised present logic. I believe the bug was just triggered
  by rapid redraws allowing the app to read data from unsynchronised DMA
  buffers.
  Now rendering *should* be smooth
  
  Fixes
  https://github.com/ghostty-org/ghostty/discussions/14243#discussioncomment-18459289
  ```
- [`a93a8b0`](https://github.com/ghostty-org/ghostty/commit/a93a8b03b65dce30f6bd5df6a2250bd1247e5089) gtk,imgui: Fix broken widget by allowing a GLES context to be used ([@AnthonyZhOon](https://github.com/AnthonyZhOon))
- [`de53b33`](https://github.com/ghostty-org/ghostty/commit/de53b335d0a5f0650ca7c7b10cddf4aa34e4d49c) gtk,imgui: Fix broken widget by allowing a GLES context to be used ([#14336](https://github.com/ghostty-org/ghostty/issues/14336)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  ```
  info(opengl): loaded OpenGL 4.3
  warning(gtk_ghostty_imgui_widget): GLArea for Dear ImGui widget failed to realize: Unable to create a GL context
  warning(gtk_ghostty_imgui_widget): Dear ImGui context not initialized
  ```
  Despite logs showing loaded OpenGL, api tracing ghostty showed OpenGL ES
  being used, the imgui widget was failing to initialize a context because
  we did not support GLES for the imgui widget.
  
  Still not sure what's going on with our OpenGL api selection but this
  gets the inspector working in this scenario for me.
  
  # AI Disclosure
  GPT Astra-Light in the desktop ChatGPT wrote the intial code, I deleted
  unnecessary changes and looked up the imgui function being called to
  understand the change, and tested the result.
  ````
- [`22391ed`](https://github.com/ghostty-org/ghostty/commit/22391ed6491f2924361dcad1f9a9176a390fd20f) opengl: validate exported DMA-BUF planes ([#14322](https://github.com/ghostty-org/ghostty/issues/14322)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Maximizing the window could crash the app when EGL returned an invalid
  DMA-BUF plane descriptor. GDK later hit a fatal assertion while
  downloading the texture.
  
  `
  Gdk:ERROR:../../../gdk/gdkdmabuf.c:154:gdk_dmabuf_do_download_mmap:
  assertion failed: (i > 0)
  Bail out!
  Gdk:ERROR:../../../gdk/gdkdmabuf.c:154:gdk_dmabuf_do_download_mmap:
  assertion failed: (i > 0)
  `
  
  Validate exported descriptors before passing them to GTK.
  Invalid exports now use the existing CPU-memory fallback.
  ```
- [`bd1c82b`](https://github.com/ghostty-org/ghostty/commit/bd1c82bc5306da32b16b5055ceff023d7ebc9edc) Update VOUCHED list ([#14341](https://github.com/ghostty-org/ghostty/issues/14341)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14337#discussioncomment-18549787)
  from @pluiedev.
  
  Denounce: @zorzysty
  ```
- [`9d2d9ac`](https://github.com/ghostty-org/ghostty/commit/9d2d9acac740dda166cc41c77f5886eb8773809d) agents: drop CLAUDE.md ([@trag1c](https://github.com/trag1c))
- [`4ae9f1a`](https://github.com/ghostty-org/ghostty/commit/4ae9f1a2de5484de3d6a13fe03676b8853b9c41c) agents: drop CLAUDE.md ([#14348](https://github.com/ghostty-org/ghostty/issues/14348)) ([@trag1c](https://github.com/trag1c))
  ```text
  Claude Code finally supports AGENTS.md since
  [v2.1.277](https://code.claude.com/docs/en/changelog#2-1-277), so the
  symlink can be yeeted.
  ```
- [`7fb75b3`](https://github.com/ghostty-org/ghostty/commit/7fb75b3c508ce8dfccfe796d9bec3cba75843d84) Update VOUCHED list ([#14363](https://github.com/ghostty-org/ghostty/issues/14363)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14209#discussioncomment-18567131)
  from @jcollie.
  
  Vouch: @nicolaair
  ```
- [`622b4ee`](https://github.com/ghostty-org/ghostty/commit/622b4eecd7d2ce1a10930537c17f0d61abdba817) Update VOUCHED list ([#14367](https://github.com/ghostty-org/ghostty/issues/14367)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14365#discussioncomment-18569751)
  from @jcollie.
  
  Vouch: @toppk
  ```
- [`7c40388`](https://github.com/ghostty-org/ghostty/commit/7c40388b2c63b7dcc5d6c9b9804e40fb2574444f) Update VOUCHED list ([#14373](https://github.com/ghostty-org/ghostty/issues/14373)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14372#discussioncomment-18573897)
  from @jcollie.
  
  Vouch: @shreeve
  ```

