> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: October 1, 2026 at 12:17 UTC.

## October 1, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/36824341438), [2](https://github.com/ghostty-org/ghostty/actions/runs/36821001995)  
Summary: 2 runs • 3 commits • 2 authors

### Changes

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

## September 30, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/36730069010), [2](https://github.com/ghostty-org/ghostty/actions/runs/36722471142), [3](https://github.com/ghostty-org/ghostty/actions/runs/36710304157), [4](https://github.com/ghostty-org/ghostty/actions/runs/36670952998), [5](https://github.com/ghostty-org/ghostty/actions/runs/36665025906), [6](https://github.com/ghostty-org/ghostty/actions/runs/36660177665), [7](https://github.com/ghostty-org/ghostty/actions/runs/36659330138), [8](https://github.com/ghostty-org/ghostty/actions/runs/36655721423), [9](https://github.com/ghostty-org/ghostty/actions/runs/36654852811)  
Summary: 9 runs • 29 commits • 9 authors

### Changes

- [`02c51de`](https://github.com/ghostty-org/ghostty/commit/02c51decf54a40513189a07c0d96b7d170c902e0) terminal/c: test osc command data with a NULL command ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  ghostty_osc_end returns NULL for an invalid or cancelled sequence, and
  ghostty_osc_command_data is documented to accept a NULL command. It
  unwraps the command instead, so this test currently crashes.
  ```
- [`51d3ca1`](https://github.com/ghostty-org/ghostty/commit/51d3ca1689d6ab9cc64ed394825a8417353473eb) terminal/c: return false from osc command data on NULL ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  ghostty_osc_command_data panicked on a NULL command in safe builds,
  and was undefined behavior in release builds, even though the header
  says NULL is accepted. Return false instead, like
  ghostty_osc_command_type reports NULL as an invalid command.
  ```
- [`9a4787d`](https://github.com/ghostty-org/ghostty/commit/9a4787d90c03db611d26f811aa8a794e20b44b8f) vt: don't call a same-size terminal resize a no-op ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  A resize to the current dimensions still updates pixel geometry,
  synchronized output and size reports. Only the grid is left as is.
  ```
- [`daff2d8`](https://github.com/ghostty-org/ghostty/commit/daff2d8e11f6946c499302758705aa061658ecfc) vt: test osc command data with a NULL command ([#14481](https://github.com/ghostty-org/ghostty/issues/14481)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `ghostty_osc_command_data` is documented in `osc.h` to accept a NULL
  command, but in the code it unwraps it (`command_.?` in
  `commandDataTyped`).
  A NULL command panics in safe builds and is UB in release builds.
  
  It' easy to hit this: `ghostty_osc_end` returns `NULL` for any invalid
  or cancelled sequence.
  
  This makes the function follow the docs and return false for a `NULL`
  command, just like `ghostty_osc_command_type`.
  
  AI disclosure: Claude Code was used to find the bug and write the test
  while working on libghostty-rs . The one-liner is mine.
  ```
- [`76895d9`](https://github.com/ghostty-org/ghostty/commit/76895d97b74ff6b24c2b1543bcd69ccc18048a4d) vt: don't call a same-size terminal resize a no-op ([#14482](https://github.com/ghostty-org/ghostty/issues/14482)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A resize to the current dimensions still updates pixel geometry,
  synchronized output and size reports. Only the grid is left as is.
  
  For reference:
  
  https://github.com/ghostty-org/ghostty/blob/acf1209ee9e12ddf7bafb18044979d266106ed68/src/terminal/Terminal.zig#L4056-L4057
  ```
- [`bb20f8e`](https://github.com/ghostty-org/ghostty/commit/bb20f8e45cd4035d00375358d5acd6b3c68c2e1d) terminal: reset the palette on RIS ([@korikhin](https://github.com/korikhin))
- [`2b1edde`](https://github.com/ghostty-org/ghostty/commit/2b1edded2842a405da9266dc9e0085e1849d918f) terminal: cosmetic changes in `fullReset` ([@korikhin](https://github.com/korikhin))
- [`acf1209`](https://github.com/ghostty-org/ghostty/commit/acf1209ee9e12ddf7bafb18044979d266106ed68) terminal: reset the palette on RIS ([#14480](https://github.com/ghostty-org/ghostty/issues/14480)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This happens on RIS and DECSTR in xterm
  ([charproc.c#L14402-L14407](https://github.com/ThomasDickey/xterm-snapshots/blob/9489b2056ee51fa9dd6a7087483b9b8f85d6a0c4/charproc.c#L14402-L14407)).
  
  - The first commit is the change and the typo fix.
  - The second commit is purely cosmetic. Drop it if it's meh. Flags are
  okay (checked with an assertion just in case).
  
  Now this comment tells the truth. But for what it is worth, when the
  mailbox is drained, the modes are already reset.
  
  
  https://github.com/ghostty-org/ghostty/blob/6467b1dab0be087fa8f0a7ccc7b3c5b88b9be7a5/src/termio/stream_handler.zig#L893-L894
  
  #### Reproduction
  
  Launch xterm and Ghostty with a user setting (green replaced with
  purple):
  
  ```sh
  xterm -xrm 'XTerm*color2: #ff00ff'
  ```
  
  ```sh
  ghostty --palette=2=#ff00ff
  ```
  
  Print some "green" text:
  
  ```sh
  printf '\e[32mSOME TEXT\e[0m\n'    # Shows purple as intended
  ```
  
  Change green to yellow via OSC:
  
  ```sh
  printf '\e]4;2;#ffff00\e\\'        # Text shows yellow now
  ```
  
  Reset the terminal and print some "green" text:
  
  ```sh
  printf '\ec'
  printf '\e[32mSOME TEXT\e[0m\n'    # Shows purple as intended (back to the user setting)
  ```
  
  #### AI Disclosure
  
  Claude wrote the reproduction for me.
  ````
- [`e2721d0`](https://github.com/ghostty-org/ghostty/commit/e2721d0932bffc883d39e979cd632eb721b7c2fb) macos: don't show Kitty clipboard program name in prompts ([@ajr-khll](https://github.com/ajr-khll))
  ```text
  The Kitty clipboard protocol lets a program send a "human friendly
  name" with clipboard read and write requests. The name is
  attacker-controlled and unverifiable, and showing it in the clipboard
  confirmation prompt lets a program put arbitrary text in a trusted
  dialog, which could be used for social engineering.
  
  Always show "An application" instead, matching the GTK implementation.
  ```
- [`be595d8`](https://github.com/ghostty-org/ghostty/commit/be595d8f01b58bc3dc9125fb53b825df76b6d0f5) macOS: remove compiler check for Shortcut and Tab bar fix ([@bo2themax](https://github.com/bo2themax))
- [`afded91`](https://github.com/ghostty-org/ghostty/commit/afded91dfaed30031deb033f74c444fb38204c09) terminal: preserve saved cursor position during repeated widening ([@fornwall](https://github.com/fornwall))
  ````text
  Fix saved cursors moving backward during repeated widening. Reflow now accounts for deferred line breaks and pending wrap when clamping tracked positions in trailing blanks.
  
  Starting with a 4-column terminal:
  
  1. Output `abc`, then start a new line and output `AAA|`.
  2. Save the cursor while in pending wrap (`ESC 7`).
  3. Widen to 5 columns, then to 6 columns.
  4. Restore the cursor (`ESC 8`) and output `X`.
  
  Current buggy behaviour:
  ```
  abc
  AAX|
  ```
  
  Fixed expected behaviour:
  ```
  abc
  AAA|X
  ```
  ````
- [`6467b1d`](https://github.com/ghostty-org/ghostty/commit/6467b1dab0be087fa8f0a7ccc7b3c5b88b9be7a5) macOS: remove compiler check for Shortcut and Tab bar fix ([#14473](https://github.com/ghostty-org/ghostty/issues/14473)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Follow up for #14413 and #14414
  ```
- [`7bb45ba`](https://github.com/ghostty-org/ghostty/commit/7bb45ba34eed168dae5de24b088aa4602fbee75c) libghostty: add semantic prompt and reset effects ([@mitchellh](https://github.com/mitchellh))
  ````text
  This adds two new effects to libghostty-vt. The semantic prompt effect
  reports shell integration events: a prompt starts, input starts, output
  starts, or a command ends. The reset effect reports a full reset (RIS,
  `ESC c`).
  
  Embedders previously had no way to observe either of these. The
  terminal applied OSC 133 to the grid and a full reset to its state, but
  nothing was reported outside the library. This lets an embedder track
  per-command state such as the running command line and its exit code,
  and throw that state away when a new prompt starts or the terminal is
  reset.
  
  ```c
  static void on_semantic_prompt(
      GhosttyTerminal terminal,
      void* userdata,
      const GhosttyTerminalSemanticPrompt* event) {
    if (event->kind != GHOSTTY_SEMANTIC_PROMPT_COMMAND_END) return;
    if (event->has_exit_code) {
      printf("exited with %d\n", event->exit_code);
    }
  }
  
  ghostty_terminal_set(terminal, GHOSTTY_TERMINAL_OPT_SEMANTIC_PROMPT,
                       (const void*)on_semantic_prompt);
  ```
  ````
- [`36ec90a`](https://github.com/ghostty-org/ghostty/commit/36ec90a07fcb58e3033296c06c82438bf30d2e42) libghostty: add semantic prompt and reset effects ([#14479](https://github.com/ghostty-org/ghostty/issues/14479)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This adds two new effects to libghostty-vt. The semantic prompt effect
  reports shell integration events: a prompt starts, input starts, output
  starts, or a command ends. The reset effect reports a full reset (RIS,
  `ESC c`).
  
  Embedders previously had no way to observe either of these. The terminal
  applied OSC 133 to the grid and a full reset to its state, but nothing
  was reported outside the library. This lets an embedder track
  per-command state such as the running command line and its exit code,
  and throw that state away when a new prompt starts or the terminal is
  reset.
  
  ```c
  static void on_semantic_prompt(
      GhosttyTerminal terminal,
      void* userdata,
      const GhosttyTerminalSemanticPrompt* event) {
    if (event->kind != GHOSTTY_SEMANTIC_PROMPT_COMMAND_END) return;
    if (event->has_exit_code) {
      printf("exited with %d\n", event->exit_code);
    }
  }
  
  ghostty_terminal_set(terminal, GHOSTTY_TERMINAL_OPT_SEMANTIC_PROMPT,
                       (const void*)on_semantic_prompt);
  ```
  ````
- [`dc3f73a`](https://github.com/ghostty-org/ghostty/commit/dc3f73a69e18e895a8217ec50eb3ad32a03be3ee) terminal: preserve saved cursor position during repeated widening ([#14478](https://github.com/ghostty-org/ghostty/issues/14478)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Fix saved cursors moving backward during repeated widening. Reflow now
  accounts for deferred line breaks and pending wrap when clamping tracked
  positions in trailing blanks.
  
  Starting with a 4-column terminal:
  
  1. Output `abc`, then start a new line and output `AAA|`.
  2. Save the cursor while in pending wrap (`ESC 7`).
  3. Widen to 5 columns, then to 6 columns.
  4. Restore the cursor (`ESC 8`) and output `X`.
  
  Current buggy behaviour:
  ```
  abc
  AAX|
  ```
  
  Fixed expected behaviour:
  ```
  abc
  AAA|X
  ```
  
  AI disclosure: Created with codex using gpt-6 astra. Iterated on,
  reviewed and tested by me.
  ````
- [`62fa23b`](https://github.com/ghostty-org/ghostty/commit/62fa23bfa9c1c8f908792ba3281253d776b953c7) macos: don't show Kitty clipboard program name in prompts [#14326](https://github.com/ghostty-org/ghostty/issues/14326) ([#14470](https://github.com/ghostty-org/ghostty/issues/14470)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Following up on #14325
  This simply removes the "human friendly name" field from the Kitty
  clipboard protocol from reaching the User, due to the social engineering
  concerns raised in the issue. Now, the message will always show "An
  application", which matches the GTK implementation.
  
  Used Opus 5.5 with Claude Code to find all the relevant files to change
  and check my work.
  ```
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
Summary: 6 runs • 278 commits • 36 authors

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
- [`d4d8f62`](https://github.com/ghostty-org/ghostty/commit/d4d8f62262cb1a974a7d2470d5f79f811fab15e4) i18n: adjust and extend Ukrainian translation ([#13854](https://github.com/ghostty-org/ghostty/issues/13854)) ([@trag1c](https://github.com/trag1c))
- [`59141ad`](https://github.com/ghostty-org/ghostty/commit/59141ad21d7e86e48eec8ab8cbfe0095cb814303) add eu translation ([@erral](https://github.com/erral))
- [`fc7bfa6`](https://github.com/ghostty-org/ghostty/commit/fc7bfa60b4b5b40183387e52b782612f417812f3) ci: move freestanding build into test workflow ([@Uzaaft](https://github.com/Uzaaft))
- [`028af92`](https://github.com/ghostty-org/ghostty/commit/028af92ce3876ce1627163ce777f516b8218b410) terminal: clarify page allocator fallback ([@Uzaaft](https://github.com/Uzaaft))
- [`f6113ea`](https://github.com/ghostty-org/ghostty/commit/f6113ea2f5da697351ffe9dd91653427c4d27f90) Implement needed modifications for issue [#12600](https://github.com/ghostty-org/ghostty/issues/12600), more flexible copy-on-select and middle-click-action ([#12604](https://github.com/ghostty-org/ghostty/issues/12604)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  For middle-click-action
  * Kept the option "primary-paste" instead of "paste-primary" to keep
  backwards compatibility
  * Added the option "clipboard-paste"
  
  For copy-on-select
  * Added the both, none and primary options
  
  Updated config documentation
  
  Note: No AI was used, Even though I don't know Zig, I looked at the code
  and the modifications seemed easy enough
  
  Closes #12600
  ```
- [`c290639`](https://github.com/ghostty-org/ghostty/commit/c2906398be63f7eed567eee294ec09f291844b95) terminal: fix living item over-count in RefCountedSet.addWithId ([#14081](https://github.com/ghostty-org/ghostty/issues/14081)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Reported in https://github.com/ghostty-org/ghostty/discussions/14064
  
  I validated this myself manually. The zero-ref branch of
  `addWithIdContext` incremented `living` unconditionally even if `upsert`
  resolved the value to an item that was already alive under a different
  ID.
  
  This would cause `living` to be invalid for each time this happened and
  the downstream effect was that `count()` drifted. I couldn't find any
  crashing or invalid effect except that this caused requested style
  memory to be over-provisioned.
  
  cc @qwerasd205 since its ref counted set, but I did this work manually
  ❤️
  ```
- [`e8709b1`](https://github.com/ghostty-org/ghostty/commit/e8709b1f9ee1a1275c8ca2b3c22f40a4e4663137) Merge remote-tracking branch 'upstream/main' into add-serbian-translation ([@kostich](https://github.com/kostich))
- [`90f7759`](https://github.com/ghostty-org/ghostty/commit/90f775976328cd90b8cf12637b776f0689f2f4f8) Fix HTML/URL acronyms as agreed ([@kostich](https://github.com/kostich))
- [`8bf7e51`](https://github.com/ghostty-org/ghostty/commit/8bf7e517f0571c605a206aae00977c2e8e0cc7ce) Regenerate sr@latin.po from sr.po ([@kostich](https://github.com/kostich))
- [`5e02d00`](https://github.com/ghostty-org/ghostty/commit/5e02d0014de36ab776ac947e60ae5641c9674ca4) ci: require freestanding libghostty-vt builds ([@Uzaaft](https://github.com/Uzaaft))
- [`458f079`](https://github.com/ghostty-org/ghostty/commit/458f079f176632bf98d503bef1726472be505f07) Use the informal form ([@kostich](https://github.com/kostich))
- [`2c854a1`](https://github.com/ghostty-org/ghostty/commit/2c854a1aa42c96ec484f136fdd38d060bd6a7683) freestanding support ([#14076](https://github.com/ghostty-org/ghostty/issues/14076)) ([@mitchellh](https://github.com/mitchellh))
- [`149c9f5`](https://github.com/ghostty-org/ghostty/commit/149c9f562af3933493eb7dd275259eee9ce26f79) terminal: extract whole-terminal search orchestration from the search thread ([@mitchellh](https://github.com/mitchellh))
- [`32601cd`](https://github.com/ghostty-org/ghostty/commit/32601cd79a23618d0e64fd0c73bfd47e713be1ef) terminal/c: add search wrapper implementing the whole-terminal search API ([@mitchellh](https://github.com/mitchellh))
- [`cdef14a`](https://github.com/ghostty-org/ghostty/commit/cdef14a1fddd223b63fec60a8f59832a7e2a4db9) Remove X-Generator from the sr.po file ([@kostich](https://github.com/kostich))
- [`f0c918f`](https://github.com/ghostty-org/ghostty/commit/f0c918fc4b72c6c7e746db68f753d102a02bb206) terminal/c: allow freeing a search and its terminal in any order ([@mitchellh](https://github.com/mitchellh))
- [`f920291`](https://github.com/ghostty-org/ghostty/commit/f9202919f71951e7b5af2837afc30f181ad2168c) libghostty: add ghostty_search_* terminal search C API ([@mitchellh](https://github.com/mitchellh))
- [`674abd8`](https://github.com/ghostty-org/ghostty/commit/674abd8a1940c928d3a0fb0ca27d6ed6dfc5e3c0) example: add c-vt-search demonstrating the terminal search C API ([@mitchellh](https://github.com/mitchellh))
- [`76d9fce`](https://github.com/ghostty-org/ghostty/commit/76d9fcefef592617360577c9208490dc44d04a65) libghostty: set the search needle via ghostty_search_set, drop GhosttySearchOptions ([@mitchellh](https://github.com/mitchellh))
- [`4b51f52`](https://github.com/ghostty-org/ghostty/commit/4b51f521d4080f1bbdb113180f1b109404b6ad7f) libghostty: add terminal search API ([#14097](https://github.com/ghostty-org/ghostty/issues/14097)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This exposes the terminal search API through libghostty C and Zig APIs.
  
  This was previously available through the Zig APIs but forced our
  threading model. I've now extracted the full terminal search state to a
  new `terminal.search.TerminalSearch` structure so threading isn't
  forced. The C API is completely new.
  
  ## Example (C)
  
  ```c
  GhosttySearch search;
  ghostty_search_new(NULL, &search, terminal);
  
  GhosttyString needle = { (const uint8_t *)"error", 5 };
  ghostty_search_set(search, GHOSTTY_SEARCH_OPT_NEEDLE, &needle);
  ghostty_search_run(search);
  
  // Find bar chrome: "k of n"
  size_t total, idx;
  ghostty_search_get(search, GHOSTTY_SEARCH_DATA_TOTAL_MATCHES, &total);
  
  // Enter: select the next match (wraps, scrolls the viewport if needed)
  ghostty_search_set(search, GHOSTTY_SEARCH_OPT_SELECT_NEXT, NULL);
  ghostty_search_get(search, GHOSTTY_SEARCH_DATA_SELECTED_INDEX, &idx);
  
  ghostty_search_free(search);
  ```
  ````
- [`8168115`](https://github.com/ghostty-org/ghostty/commit/81681158b1f04b9900c3e58ba6db790384f5b6f5) Add Serbian translation ([#13842](https://github.com/ghostty-org/ghostty/issues/13842)) ([@00-kat](https://github.com/00-kat))
  ```text
  ## Summary
  - Adds Serbian translations for both Cyrillic (`sr`) and Latin
  (`sr@latin`) scripts, registered in `src/os/i18n_locales.zig` and
  `CODEOWNERS`.
  - `po/sr@latin.po` is generated from `po/sr.po` with `msgfilter
  recode-sr-latin` and should not be translated by hand.
  - Replaces the closed #13030; strings are rebased onto current `main`.
  
  Cc @slowdub for a review.
  
  EDIT: AI disclosure: I used Cursor (Grok 4.6) for mechanical repo work
  only, not for writing the Serbian translations. The agent fetched
  ghostty-org/ghostty, branched from current main, ran msgmerge on
  po/sr.po against the template, generated po/sr@latin.po with msgfilter
  recode-sr-latin, registered sr / sr@latin in src/os/i18n_locales.zig and
  CODEOWNERS, rebased my three commits onto later main, pushed the branch,
  and opened this PR (I had intended to open the PR myself, s***** thing
  ignored my instructions). I translated and reviewed sr.po and the Latin
  file is a recode of that catalog, not a separate translation since
  Serbian Cyrillic can be perfectly transcoded to the Latin script via
  [recode-sr-latin](https://linux.die.net/man/1/recode-sr-latin).
  ```
- [`38c984e`](https://github.com/ghostty-org/ghostty/commit/38c984e6760f59a634b6538f5e8669ec829019f1) build(deps): bump softprops/action-gh-release from 3.0.2 to 3.0.3 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [softprops/action-gh-release](https://github.com/softprops/action-gh-release) from 3.0.2 to 3.0.3.
  - [Release notes](https://github.com/softprops/action-gh-release/releases)
  - [Changelog](https://github.com/softprops/action-gh-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/softprops/action-gh-release/compare/3d0d9888cb7fd7b750713d6e236d1fcb99157228...efb35369e0ad2afab669f228072c1b0d510eae64)
  
  ---
  updated-dependencies:
  - dependency-name: softprops/action-gh-release
    dependency-version: 3.0.3
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`20abdb5`](https://github.com/ghostty-org/ghostty/commit/20abdb50a6216c450d6d4d010c41c7edf5ab15b2) Update VOUCHED list ([#14101](https://github.com/ghostty-org/ghostty/issues/14101)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14100#discussioncomment-18229353)
  from @jcollie.
  
  Vouch: @jzillmann
  ```
- [`d4a5ff5`](https://github.com/ghostty-org/ghostty/commit/d4a5ff58b6bc4a1fcc79a69f5cff94a678d97f42) macOS: fix window cascading ([@bo2themax](https://github.com/bo2themax))
- [`d2e2488`](https://github.com/ghostty-org/ghostty/commit/d2e2488ef7539124122d346399a5e5cca152f259) build(deps): bump softprops/action-gh-release from 3.0.2 to 3.0.3 ([#14098](https://github.com/ghostty-org/ghostty/issues/14098)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [softprops/action-gh-release](https://github.com/softprops/action-gh-release)
  from 3.0.2 to 3.0.3.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/softprops/action-gh-release/releases">softprops/action-gh-release's
  releases</a>.</em></p>
  <blockquote>
  <h2>v3.0.3</h2>
  <p><code>3.0.3</code> is a maintenance release with updated
  dependencies. It also safely
  classifies malformed GitHub API errors to avoid secondary failures (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/822">#822</a>).</p>
  <h2>What's Changed</h2>
  <h3>Bug fixes 🐛</h3>
  <ul>
  <li>fix: safely classify GitHub API errors by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/822">softprops/action-gh-release#822</a></li>
  </ul>
  <h3>Other Changes 🔄</h3>
  <ul>
  <li>dependency updates</li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/softprops/action-gh-release/blob/master/CHANGELOG.md">softprops/action-gh-release's
  changelog</a>.</em></p>
  <blockquote>
  <h2>3.0.3</h2>
  <p><code>3.0.3</code> is a maintenance release with updated
  dependencies. It also safely
  classifies malformed GitHub API errors to avoid secondary failures (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/822">#822</a>).</p>
  <h2>What's Changed</h2>
  <h3>Bug fixes 🐛</h3>
  <ul>
  <li>fix: safely classify GitHub API errors by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/822">softprops/action-gh-release#822</a></li>
  </ul>
  <h3>Other Changes 🔄</h3>
  <ul>
  <li>dependency updates</li>
  </ul>
  <h2>3.0.2</h2>
  <p><code>3.0.2</code> is a patch release focused on release reliability
  and compatibility. It
  reuses existing draft releases when publishing prereleases, supports
  replacing
  release assets on Gitea, hardens streamed asset uploads, and provides
  clearer
  release-creation diagnostics. It also includes TypeScript, coverage, and
  tooling
  maintenance merged since <code>3.0.1</code>.</p>
  <p>This release fixes <a
  href="https://redirect.github.com/softprops/action-gh-release/issues/795">#795</a>,
  <a
  href="https://redirect.github.com/softprops/action-gh-release/issues/438">#438</a>,
  and <a
  href="https://redirect.github.com/softprops/action-gh-release/issues/803">#803</a>.
  The upload transport hardening covers the
  historical failure reported in <a
  href="https://redirect.github.com/softprops/action-gh-release/issues/790">#790</a>,
  although current hosted Node 24 runners did
  not reproduce it naturally. The diagnostics work is related to <a
  href="https://redirect.github.com/softprops/action-gh-release/issues/786">#786</a>
  and does not
  claim a reproducible release-creation fix.</p>
  <h2>What's Changed</h2>
  <h3>Exciting New Features 🎉</h3>
  <ul>
  <li>feat: improve release error reporting and test coverage by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/813">softprops/action-gh-release#813</a></li>
  </ul>
  <h3>Bug fixes 🐛</h3>
  <ul>
  <li>fix: publish existing draft releases as prereleases by <a
  href="https://github.com/godfengliang"><code>@​godfengliang</code></a>
  in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/801">softprops/action-gh-release#801</a></li>
  <li>fix: upload small checksum assets reliably by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/815">softprops/action-gh-release#815</a></li>
  <li>fix: replace existing release assets on Gitea by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/816">softprops/action-gh-release#816</a></li>
  <li>fix: clarify release creation 404 errors by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/817">softprops/action-gh-release#817</a></li>
  </ul>
  <h3>Other Changes 🔄</h3>
  <ul>
  <li>chore(deps): upgrade TypeScript to 7 by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/812">softprops/action-gh-release#812</a></li>
  <li>chore(deps): remove unused TypeScript tooling by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/814">softprops/action-gh-release#814</a></li>
  <li>dependency, Node 24 pin, and CI maintenance merged since
  <code>3.0.1</code></li>
  </ul>
  <h2>3.0.1</h2>
  <ul>
  <li>maintenance release with updated dependencies</li>
  </ul>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/efb35369e0ad2afab669f228072c1b0d510eae64"><code>efb3536</code></a>
  release 3.0.3 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/840">#840</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/6441963a7597ab67f36fea0287a7ae58a9bfd8fe"><code>6441963</code></a>
  chore(deps): bump the npm group with 2 updates (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/839">#839</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/e5ee6bc58a36b838b92fc1217f2e4b414b5abcc8"><code>e5ee6bc</code></a>
  chore(deps): bump esbuild from 0.28.1 to 0.28.2 in the npm group (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/837">#837</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/d1e66170d32c9ec7bbcb7fae044d3d686ce304d3"><code>d1e6617</code></a>
  chore(deps): bump undici from 6.27.0 to 6.28.0 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/831">#831</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/64037519ba20f54c01bc1dc90342c929aac5a2fa"><code>6403751</code></a>
  chore(deps): bump the npm group with 2 updates (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/835">#835</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/7c7184b6876126a5df15adc5b679dc450a393725"><code>7c7184b</code></a>
  chore(deps): bump postcss from 8.5.19 to 8.5.25 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/833">#833</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/0f3f0d2943676d58f9698b3ab590c2056023d77d"><code>0f3f0d2</code></a>
  chore(deps): bump brace-expansion from 5.0.8 to 5.0.9 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/832">#832</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/77fb938f2f95e717ce6705d2909af527263360a0"><code>77fb938</code></a>
  chore(deps): bump prettier from 3.9.5 to 3.9.6 in the npm group (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/830">#830</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/5a6f51711ce2ba103b78f5e9550f810679f11e0e"><code>5a6f517</code></a>
  chore(deps): bump brace-expansion from 5.0.7 to 5.0.8 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/828">#828</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/a3c91c98f80000f5b06c7fc0327c54f51c6ab7d8"><code>a3c91c9</code></a>
  chore(deps): bump the github-actions group with 2 updates (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/825">#825</a>)</li>
  <li>Additional commits viewable in <a
  href="https://github.com/softprops/action-gh-release/compare/3d0d9888cb7fd7b750713d6e236d1fcb99157228...efb35369e0ad2afab669f228072c1b0d510eae64">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=softprops/action-gh-release&package-manager=github_actions&previous-version=3.0.2&new-version=3.0.3)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`b7a680b`](https://github.com/ghostty-org/ghostty/commit/b7a680bc40b76cf7ed6b21044ac3f291ea0056be) macOS: fix window cascading ([#14106](https://github.com/ghostty-org/ghostty/issues/14106)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Regression from https://github.com/ghostty-org/ghostty/pull/13722
  ```
- [`451e224`](https://github.com/ghostty-org/ghostty/commit/451e224c64ddd0a9d9e9df045cdfb27c38fa8ff2) macOS: clean up for [#14106](https://github.com/ghostty-org/ghostty/issues/14106) ([@bo2themax](https://github.com/bo2themax))
- [`3c1ef5b`](https://github.com/ghostty-org/ghostty/commit/3c1ef5b32fc5ea6b93d28493fabf193f595139cf) macOS: clean up for [#14106](https://github.com/ghostty-org/ghostty/issues/14106) ([#14111](https://github.com/ghostty-org/ghostty/issues/14111)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  I don't know what happened to me, but I didn't notice that I should
  delete this🫪
  ```
- [`501e7b5`](https://github.com/ghostty-org/ghostty/commit/501e7b5c1cf04162305c56e85204d2b1ac9427fb) pkg/fontconfig: update to 2.18.3 ([@vancluever](https://github.com/vancluever))
  ```text
  This updates our own bundled fontconfig (for static builds) to 2.18.3.
  
  Note that fontconfig has changed their build process a bit since this
  has been updated last; they are leaning on the Autoconf (and Meson as
  they are now deprecating use of Autoconf) toolchain(s) to now generate a
  number of headers that are a part of the build process.
  
  Since servicing this dependency in an effort to keep the build pure Zig
  is starting to get more complex, I've added some documentation on how to
  actually get a snapshot of the fontconfig repository in a state where
  files can be looked for and copied over as needed. Otherwise, we might
  want to in the future consider removing this altogether and just rely on
  system integrations.
  ```
- [`2ba7576`](https://github.com/ghostty-org/ghostty/commit/2ba75764f6002baab9cb439dfff7ec37ac7704e8) build(deps): bump flatpak/flatpak-github-actions/flatpak-builder ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [flatpak/flatpak-github-actions/flatpak-builder](https://github.com/flatpak/flatpak-github-actions) from 6.7 to 6.8.
  - [Release notes](https://github.com/flatpak/flatpak-github-actions/releases)
  - [Commits](https://github.com/flatpak/flatpak-github-actions/compare/401fe28a8384095fc1531b9d320b292f0ee45adb...79327416609af08178ad73b352877e51450790b3)
  
  ---
  updated-dependencies:
  - dependency-name: flatpak/flatpak-github-actions/flatpak-builder
    dependency-version: '6.8'
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`7358067`](https://github.com/ghostty-org/ghostty/commit/7358067d1a014e0dc36545046f2df41255f2ea26) build(deps): bump cachix/cachix-action ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [cachix/cachix-action](https://github.com/cachix/cachix-action) from 5f2d7c5294214f71b873db4b969586b980625e71 to 38b082610b782e7e93e209c35fd730d399dee866.
  - [Release notes](https://github.com/cachix/cachix-action/releases)
  - [Changelog](https://github.com/cachix/cachix-action/blob/master/RELEASE.md)
  - [Commits](https://github.com/cachix/cachix-action/compare/5f2d7c5294214f71b873db4b969586b980625e71...38b082610b782e7e93e209c35fd730d399dee866)
  
  ---
  updated-dependencies:
  - dependency-name: cachix/cachix-action
    dependency-version: 38b082610b782e7e93e209c35fd730d399dee866
    dependency-type: direct:production
  ...
  ```
- [`310797d`](https://github.com/ghostty-org/ghostty/commit/310797df1d912bccd63ef624395a2458e99f6cf7) macOS: fix cascading without affecting other new-window behaviours ([@bo2themax](https://github.com/bo2themax))
- [`a8b0855`](https://github.com/ghostty-org/ghostty/commit/a8b0855b630022db2933f402d9c964a111c8751c) macOS: fix cascading for HiddenTitlebarTerminalWindow ([@bo2themax](https://github.com/bo2themax))
- [`58aa59d`](https://github.com/ghostty-org/ghostty/commit/58aa59d0e176b57d27e685dee86d3e9b7e165ef9) Update po/eu.po ([@erral](https://github.com/erral))
- [`6a51526`](https://github.com/ghostty-org/ghostty/commit/6a5152651c8744bf5058d49ee45fdb6aee63d570) Update po/eu.po ([@erral](https://github.com/erral))
- [`4c731b5`](https://github.com/ghostty-org/ghostty/commit/4c731b5d89708ae742d4809ef1ce6a81c5c551da) Update po/eu.po ([@erral](https://github.com/erral))
- [`4ffec4b`](https://github.com/ghostty-org/ghostty/commit/4ffec4bda7ed603be297564a7b23c1d21707106e) Update po/eu.po ([@erral](https://github.com/erral))
- [`f407316`](https://github.com/ghostty-org/ghostty/commit/f407316c84a313a7f9694a2d6f3e1acabc19a416) Update po/eu.po ([@erral](https://github.com/erral))
  ```text
  applying but both eskuma and eskuina are OK.
  ```
- [`63039a6`](https://github.com/ghostty-org/ghostty/commit/63039a688e765c448ca7cc80b77d83d2177e6f51) update ([@erral](https://github.com/erral))
- [`f184d3c`](https://github.com/ghostty-org/ghostty/commit/f184d3ceb5eaee08f92f6302ac2a499bcd7dc015) update ([@erral](https://github.com/erral))
- [`4da902b`](https://github.com/ghostty-org/ghostty/commit/4da902b3c9929333f7cf78147ec714f34d5619c0) update ([@erral](https://github.com/erral))
- [`9801423`](https://github.com/ghostty-org/ghostty/commit/9801423d01e0e883c32f95a210afd98919520562) update ([@erral](https://github.com/erral))
- [`5d6615f`](https://github.com/ghostty-org/ghostty/commit/5d6615fc43ce5bc7ba9981e0c925d4e3d9dfb0d7) bash: upgrade to bash-preexec 0.7.0 ([@jparise](https://github.com/jparise))
  ```text
  https://github.com/rcaloras/bash-preexec/releases/tag/0.7.0
  
  We only source bash-preexec for bash < 4.4, so most of this release is
  inert for us: the PS0 function-substitution hook (bash >= 5.3) and the
  array PROMPT_COMMAND handling (bash >= 5.1) are never reached. What we
  do pick up is the simpler install string, per-prompt re-adjustment of
  PROMPT_COMMAND when something else modifies it, preservation of $? and
  $_ on early returns, and the first-command preexec fix.
  
  We continue to carry one local modification: __bp_adjust_histcontrol
  stays disabled in the DEBUG trap hook so the user's HISTCONTROL is
  respected (#2269). The original justification was that we didn't use
  the preexec command argument, which is no longer true because we use it
  for the window title. The comment now explains the current reasoning:
  our bash >= 4.4 integration also uses `history 1` without adjusting
  HISTCONTROL and accepts the same inaccuracy for space-prefixed commands,
  so the legacy path is kept consistent with it.
  ```
- [`7520175`](https://github.com/ghostty-org/ghostty/commit/75201750213200fba1537cf724fac5ba3dec4318) more fixes ([@erral](https://github.com/erral))
- [`aafacb1`](https://github.com/ghostty-org/ghostty/commit/aafacb1cb940e3599cb4ec2c4f9cb975532a12a4) macOS: fix flickering when creating new tab with glass style ([@bo2themax](https://github.com/bo2themax))
- [`fec89f2`](https://github.com/ghostty-org/ghostty/commit/fec89f2541e412b1a2556e56742c7612118f1b72) macOS: fix flickering when creating new tab with glass style ([#14121](https://github.com/ghostty-org/ghostty/issues/14121)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A regression from #13985.
  
  
  https://github.com/user-attachments/assets/cc7d76d7-7d86-4566-921c-a6531ce4087d
  
  
  
  
  ### AI Disclosure
  
  Used Claude to investigate, I reviewed and tested.
  ```
- [`0c1909d`](https://github.com/ghostty-org/ghostty/commit/0c1909d09a0db148913b79c684db1cef58e214ee) bash: upgrade to bash-preexec 0.7.0 ([#14120](https://github.com/ghostty-org/ghostty/issues/14120)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  https://github.com/rcaloras/bash-preexec/releases/tag/0.7.0
  
  We only source bash-preexec for bash < 4.4, so most of this release is
  inert for us: the PS0 function-substitution hook (bash >= 5.3) and the
  array PROMPT_COMMAND handling (bash >= 5.1) are never reached. What we
  do pick up is the simpler install string, per-prompt re-adjustment of
  PROMPT_COMMAND when something else modifies it, preservation of $? and
  $_ on early returns, and the first-command preexec fix.
  
  We continue to carry one local modification: __bp_adjust_histcontrol
  stays disabled in the DEBUG trap hook so the user's HISTCONTROL is
  respected (#2269). The original justification was that we didn't use the
  preexec command argument, which is no longer true because we use it for
  the window title. The comment now explains the current reasoning: our
  bash >= 4.4 integration also uses `history 1` without adjusting
  HISTCONTROL and accepts the same inaccuracy for space-prefixed commands,
  so the legacy path is kept consistent with it.
  
  *AI Usage:* I asked Fable 5.1 to run a verification pass after my manual
  upgrade, and it confirmed the expected behavior.
  ```
- [`084316a`](https://github.com/ghostty-org/ghostty/commit/084316aa825a210dedc9c2fce07772cf36ade3cb) macOS: fix cascading without affecting other new-window behaviours ([#14118](https://github.com/ghostty-org/ghostty/issues/14118)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Found another regression when investigating #14107 after the last fix.
  This regression appears on macOS 15 and 26 as well: **New window by
  Shortcuts.app or service menu while a window is visible would create a
  tab**.
  
  It appears that for `new-window` triggered by Shortcuts/Service, a small
  delay is needed to avoid automatic tabbing. It's either removing
  `NSWindow.userTabbingPreference == .always` completely or adding another
  "delay" for cascading. The latter should be better.
  
  Also fixes another cascading for `macos-titlebar-style = hidden`
  previously missed.
  ```
- [`41004c6`](https://github.com/ghostty-org/ghostty/commit/41004c6e2204494a2cbc0b4b78dd3b9c671d7488) build(deps): bump cachix/cachix-action from 5f2d7c5294214f71b873db4b969586b980625e71 to 38b082610b782e7e93e209c35fd730d399dee866 ([#14116](https://github.com/ghostty-org/ghostty/issues/14116)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps [cachix/cachix-action](https://github.com/cachix/cachix-action)
  from 5f2d7c5294214f71b873db4b969586b980625e71 to
  38b082610b782e7e93e209c35fd730d399dee866.
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/cachix/cachix-action/blob/master/RELEASE.md">cachix/cachix-action's
  changelog</a>.</em></p>
  <blockquote>
  <h1>Release</h1>
  <ol>
  <li>
  <p>Create and push a new tag:</p>
  <pre lang="console"><code>git tag v17
  git push origin v17
  </code></pre>
  </li>
  <li>
  <p>Wait for CI to pass.</p>
  </li>
  <li>
  <p><a href="https://github.com/cachix/cachix-action/releases/new">Create
  a release</a> for the new tag.</p>
  </li>
  <li>
  <p>Move the major version tag to the latest release:</p>
  <pre lang="console"><code>git tag -fa v17
  git push origin v17 --force
  </code></pre>
  </li>
  </ol>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/38b082610b782e7e93e209c35fd730d399dee866"><code>38b0826</code></a>
  dev: cleanup tests and dev files</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/0fe030c2864be690428363af3bc7016b7b1925d8"><code>0fe030c</code></a>
  dist</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/792dafcfd01b48d3df8424b641db396602252fc3"><code>792dafc</code></a>
  deps: bump dependencies</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/b690244fb5c76a5486c33b0fbbc6fd55c857d1fe"><code>b690244</code></a>
  ci: improve Nix compatibility test coverage</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/f495f3ffa2f3810a92e5cc0abc2c5d6a2a07ec82"><code>f495f3f</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/cachix-action/issues/217">#217</a>
  from cachix/dependabot/github_actions/actions/checkout-7</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/9ee3c77d45d24a8b7557d22cbba3454f2a4f8a7b"><code>9ee3c77</code></a>
  chore(deps): bump actions/checkout from 6 to 7</li>
  <li>See full diff in <a
  href="https://github.com/cachix/cachix-action/compare/5f2d7c5294214f71b873db4b969586b980625e71...38b082610b782e7e93e209c35fd730d399dee866">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
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
- [`dd167cc`](https://github.com/ghostty-org/ghostty/commit/dd167cc464f8f8b30cc561fb07e09e9fb2986c14) build(deps): bump flatpak/flatpak-github-actions/flatpak-builder from 6.7 to 6.8 ([#14115](https://github.com/ghostty-org/ghostty/issues/14115)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [flatpak/flatpak-github-actions/flatpak-builder](https://github.com/flatpak/flatpak-github-actions)
  from 6.7 to 6.8.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/flatpak/flatpak-github-actions/releases">flatpak/flatpak-github-actions/flatpak-builder's
  releases</a>.</em></p>
  <blockquote>
  <h2>v6.8</h2>
  <ul>
  <li>Add saveCache flag</li>
  <li>Add ability to override artifact name</li>
  <li>Add buildDebugBundle flag</li>
  <li>Update tests, documentation and dependencies</li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/79327416609af08178ad73b352877e51450790b3"><code>7932741</code></a>
  Update all dependencies and regenerate dist</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/09e3d61868ecd92a1c5b298a31bcc4bae17ae217"><code>09e3d61</code></a>
  readme: Don't specify setting cache key to github.sha (<a
  href="https://redirect.github.com/flatpak/flatpak-github-actions/issues/261">#261</a>)</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/23e622281a14ba5350ce2ab1ae700ac7d08cc841"><code>23e6222</code></a>
  Update runtime versions and docker images to latest</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/a3ab43f58191aa8dc105e572c0a62eaac0a7555a"><code>a3ab43f</code></a>
  flatpak-builder: Add saveCache flag</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/8e357b1556f526e3642244bdf1a6d585be36de54"><code>8e357b1</code></a>
  ci: Remove unnecessary 'needs' from debug bundle job</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/26e19caa3a954b1d36898a0e239a67d8e856f99c"><code>26e19ca</code></a>
  ci: Add test for artifact-name</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/06d246b4d5459d93c166243236f8a086d5578746"><code>06d246b</code></a>
  flatpak-builder: Add ability to override artifact name</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/a2622647717d8185d0f8cf01bb1ea2341e357ae0"><code>a262264</code></a>
  ci: Add job that uses build-debug-bundle</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/f7362292df659c06960a8c0dc309ab5990454a29"><code>f736229</code></a>
  flatpak-builder: Add buildDebugBundle flag</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/3b10954431df173eb3b564bb9adfddf3842ff91c"><code>3b10954</code></a>
  ci: Update actions to versions using Node 24</li>
  <li>See full diff in <a
  href="https://github.com/flatpak/flatpak-github-actions/compare/401fe28a8384095fc1531b9d320b292f0ee45adb...79327416609af08178ad73b352877e51450790b3">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=flatpak/flatpak-github-actions/flatpak-builder&package-manager=github_actions&previous-version=6.7&new-version=6.8)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`06178ee`](https://github.com/ghostty-org/ghostty/commit/06178eeaad7648216a0da5eb73537e9dba2266cb) terminal/search: resume a complete search when history is prepended ([@mitchellh](https://github.com/mitchellh))
  ```text
  A search that had already exhausted a screen's PageList never picked up
  history pages prepended afterwards by incremental snapshot restore.
  
  The lower level PageListSearch and so on could already handle this, we
  just needed to let it know that more history existed to search. This
  fixes that.
  ```
- [`b0481f5`](https://github.com/ghostty-org/ghostty/commit/b0481f5aa76a97e652bb842937ae4fa0eda68f3c) terminal/search: resume a complete search when history is prepended ([#14123](https://github.com/ghostty-org/ghostty/issues/14123)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A search that had already exhausted a screen's PageList never picked up
  history pages prepended afterwards by incremental snapshot restore.
  
  The lower level PageListSearch and so on could already handle this, we
  just needed to let it know that more history existed to search. This
  fixes that.
  ```
- [`3b8141f`](https://github.com/ghostty-org/ghostty/commit/3b8141fbd8e2f5770809d3df2fe0077849866dde) os/open: consume the newline when draining opener stderr ([@jzillmann](https://github.com/jzillmann))
  ```text
  takeDelimiterExclusive never consumes the delimiter: it tosses only the
  exclusive length, so the '\n' stays buffered. Once the spawned opener
  writes a single line to stderr, every subsequent call returns an empty
  slice without advancing the stream, and openThread's loop spins forever
  - one pinned core per affected open(), logging empty
  "open stderr=" warnings at tens of thousands of messages per second for
  the lifetime of the process. The thread also never reaches exe.wait(),
  so the child is never reaped.
  
  Read inclusively instead (which does consume the delimiter) and trim
  the '\n' for logging.
  
  Repro: open a link whose handler writes to stderr, e.g. an OSC 8 link
  with an unknown scheme; watch a core disappear and the unified log
  flood with "os-open: open stderr=".
  
  See discussion #14100.
  ```
- [`372d691`](https://github.com/ghostty-org/ghostty/commit/372d6914b8615610e290f8e8446d75cf4b53efeb) i18n: complete eu translation ([#14095](https://github.com/ghostty-org/ghostty/issues/14095)) ([@trag1c](https://github.com/trag1c))
- [`e212b73`](https://github.com/ghostty-org/ghostty/commit/e212b73cdaf381f2d57edc11307b06c1f520df4b) Update mk localization for v1.4 ([#14088](https://github.com/ghostty-org/ghostty/issues/14088)) ([@trag1c](https://github.com/trag1c))
  ```text
  Addressing #13766 for mk.
  ```
- [`349f026`](https://github.com/ghostty-org/ghostty/commit/349f026087d948f8f898dca3231ff91438f83ab8) os/open: consume the newline when draining opener stderr ([#14125](https://github.com/ghostty-org/ghostty/issues/14125)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes the runaway-thread bug reported in #14100 (vouched there).
  
  `openThread` drains the spawned opener's stderr with
  `takeDelimiterExclusive('\n')`. That function tosses only the exclusive
  length, so the `'\n'` is never consumed. Once the child writes one line
  to stderr, every subsequent call returns an empty slice without
  advancing the stream: the `while (true)` loop spins forever — one pinned
  core per affected `open()`, logging empty `os-open: open stderr=`
  warnings at tens of thousands of messages per second for the lifetime of
  the process — and `exe.wait()` is never reached, so the child is never
  reaped.
  
  This change reads inclusively (`takeDelimiterInclusive`, which does
  consume the delimiter) and trims the `'\n'` for logging.
  
  Observed in the wild embedding libghostty on macOS: several days of
  uptime accumulated six leaked opener threads at ~70% of a core each
  (~4.4 cores), from six link clicks whose `/usr/bin/open` wrote to
  stderr. After the fix, the same workload shows zero `os-open` log
  traffic and no leaked threads.
  
  Repro without the fix: open a link whose handler writes to stderr (e.g.
  an OSC 8 link with an unknown scheme), then watch a core pin and `log
  stream --predicate 'subsystem == "com.mitchellh.ghostty"'` flood.
  
  **AI disclosure** (per `AI_POLICY.md`): the bug was diagnosed and this
  patch drafted with Claude Code (thread sampling, log analysis, and
  reading the Zig 0.16 `std.Io.Reader` source to confirm
  `takeDelimiterExclusive`/`takeDelimiterInclusive` toss semantics). I
  reviewed the analysis and the change, understand both, and verified the
  fix in a production build of the embedding app.
  ```
- [`5dfb672`](https://github.com/ghostty-org/ghostty/commit/5dfb672986b57b6246d0c5d2c3c9a8fd3d138543) surface: restore mouse_shape when modifier overrides end ([@j-c-m](https://github.com/j-c-m))
  ```text
  hard-coded .default & .text overrode a previously set OSC22 pointer
  shape, this was a regression introduced in 6e8ed4e8b.
  ```
- [`6674aa3`](https://github.com/ghostty-org/ghostty/commit/6674aa3ba88e4e316af4106746e4b2091868df79) surface: update keyToMouseShape tests to expect mouse_shape ([@j-c-m](https://github.com/j-c-m))
  ```text
  Update the tests to expect the mouse_shape back, not the hardcoded
  .default or .text
  ```
- [`3a766cc`](https://github.com/ghostty-org/ghostty/commit/3a766ccf501c669298e5b648a47d217e99bff618) surface: show .text (i-beam) while shift is held without mouse tracking ([@j-c-m](https://github.com/j-c-m))
  ```text
  I think this is the expected behavoir when a custom OSC22 pointer is set. Once
  shift is released it will return to mouse_shape (whatever the pointer
  was before shit held).
  ```
- [`0fb6d29`](https://github.com/ghostty-org/ghostty/commit/0fb6d29404aab9c54c6fbce3cebd630960938117) SurfaceMouse: simplify keyToMouseShape ([@vancluever](https://github.com/vancluever))
  ```text
  keyToMouseShape was initially designed with more of a transition table
  model in mind to handle key presses/overrides based on very specific
  cursor states. This never materialized, so I think it's safe to just
  simply the process of handling overrides and/or passing along the
  current cursor state from the terminal in the event of key presses.
  
  Also removed a test that is essentially a duplicate of one before it now
  (returning current surface shape in the event of no overrides).
  ```
- [`6000034`](https://github.com/ghostty-org/ghostty/commit/600003455a9b6e7cf06b3127a490d6ab3c1b05df) surface: restore application mouse shape after modifier overrides ([#14128](https://github.com/ghostty-org/ghostty/issues/14128)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This fixes a regression of 9a6469743 introduced in 6e8ed4e8b.
  
  With this fix the mouse pointer will be restored to the previous (which
  could have be set to something else via OSC22), not a hardcoded .text or
  .default.
  
  It also will change the cursor to a text selection if shift is held even
  without mouse tracking, I think this is the expected behavior when a
  cursor is set via OSC22. (Kitty additionaly, once you start selecting
  changes to text (I-beam), this would be a follow-up if we desire to
  behave like kitty with OSC22 pointers).
  ```
- [`e01e75b`](https://github.com/ghostty-org/ghostty/commit/e01e75bbb228cfbb5fc08cdd53316928761c020b) terminal: don't touch me! keep the page pool free list unobtrusive ([@mitchellh](https://github.com/mitchellh))
  ```text
  This replaces the `std.heap.MemoryPool` used for page buffers with
  a custom pool called `UntouchedPool`. This keeps its free list in a side
  array and never reads/writes items until `create()`. This means that
  demand-driven allocations (like mmaped pages) don't incur physical costs
  until they're actually used.
  
  The standard `std.heap.MemoryPool` uses an intrusive linked list for
  its items which causes every item to be touched, which forces a full
  page-in of memory.
  
  It turns out we also had a lot of assertions and logic to work around
  this in various ways (size of rows, asserting we overwrite the free
  list entry, etc.) that we can now remove because of this.
  
  For an 80x24 terminal on macOS (16 KB pages):
  
  | Per terminal                 | Before   | After    |
  |------------------------------|----------|----------|
  | Page-list memory dirty       | 128 KiB  | 48 KiB   |
  | Process phys_footprint delta | 143 KiB  | 62 KiB   |
  | Page-list virtual size       | 2208 KiB | 1600 KiB |
  
  The remaining 48 KB is the active page, because we sprinkle metadata
  around the page which forces every page to be paged in. I'm going to
  follow this up with some work trying to move all our metadata to the
  front of the page so we only page one in until the rest is needed,
  but not sure if its achievable.
  
  Micro-benchmarks on the pool show that its twice the speed (slower) to
  create/free due to the side list, but in an actual `+terminal-stream`
  benchmark churning through pages, there is no measurable difference. I
  think its a good trade.
  ```
- [`31bdcd5`](https://github.com/ghostty-org/ghostty/commit/31bdcd5a79639bbac97c1a94e0f41d0f5ff84ca2) terminal: don't touch me! keep the page pool free list unobtrusive ([#14130](https://github.com/ghostty-org/ghostty/issues/14130)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This replaces the `std.heap.MemoryPool` used for page buffers with a
  custom pool called `UntouchedPool`. This keeps its free list in a side
  array and never reads/writes items until `create()`. This means that
  demand-driven allocations (like mmaped pages) don't incur physical costs
  until they're actually used.
  
  The standard `std.heap.MemoryPool` uses an intrusive linked list for its
  items which causes every item to be touched, which forces a full page-in
  of memory.
  
  It turns out we also had a lot of assertions and logic to work around
  this in various ways (size of rows, asserting we overwrite the free list
  entry, etc.) that we can now remove because of this.
  
  For an 80x24 terminal on macOS (16 KB pages):
  
  | Per terminal                 | Before   | After    |
  |------------------------------|----------|----------|
  | Page-list memory dirty       | 128 KiB  | 48 KiB   |
  | Process phys_footprint delta | 143 KiB  | 62 KiB   |
  | Page-list virtual size       | 2208 KiB | 1600 KiB |
  
  The remaining 48 KB is the active page, because we sprinkle metadata
  around the page which forces every page to be paged in. I'm going to
  follow this up with some work trying to move all our metadata to the
  front of the page so we only page one in until the rest is needed, but
  not sure if its achievable.
  
  Micro-benchmarks on the pool show that its twice the speed (slower) to
  create/free due to the side list, but in an actual `+terminal-stream`
  benchmark churning through pages, there is no measurable difference. I
  think its a good trade.
  ```
- [`e347482`](https://github.com/ghostty-org/ghostty/commit/e347482fba62fd905fab2d4c8ec6a8c6f3664385) macOS: fix find previous action when search is focused ([@bo2themax](https://github.com/bo2themax))
- [`e8936b8`](https://github.com/ghostty-org/ghostty/commit/e8936b8969e78e07d9a8bf2b6a22ce59a38f5dfb) macOS: follow up cascading fix for [#14118](https://github.com/ghostty-org/ghostty/issues/14118) ([@bo2themax](https://github.com/bo2themax))
  ```text
  Didn't respect the comment above before when reverting and testing hidden title 🫪
  ```
- [`3cca3e0`](https://github.com/ghostty-org/ghostty/commit/3cca3e0b956f07e008a4c66bb5f1a8ce266259a3) macOS: follow up cascading fix for [#14118](https://github.com/ghostty-org/ghostty/issues/14118) ([#14132](https://github.com/ghostty-org/ghostty/issues/14132)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Didn't respect the comment above. Sorry for the back&forth changes 🫪
  ```
- [`09ff85b`](https://github.com/ghostty-org/ghostty/commit/09ff85b2ac7b4204bbc48b5c7010adf0bdfb36d8) macOS: fix find previous action when search is focused ([#14131](https://github.com/ghostty-org/ghostty/issues/14131)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Typo found by @lrytz.
  ```
- [`ffe015e`](https://github.com/ghostty-org/ghostty/commit/ffe015ee55d1ab39cbf1525823ff18092433eab9) terminal: bitmap allocator marks free chunks with zero bits ([@mitchellh](https://github.com/mitchellh))
- [`c0a4f80`](https://github.com/ghostty-org/ghostty/commit/c0a4f80d80d75f7d3250d12554501fd7197e9bb0) terminal: hash map and ref counted set can initialize from zeroed memory ([@mitchellh](https://github.com/mitchellh))
- [`6112935`](https://github.com/ghostty-org/ghostty/commit/6112935a2fe9b7f5fd6c7595225c53406bee3bb1) terminal: hash map keeps its capacity and entry pointers in the struct ([@mitchellh](https://github.com/mitchellh))
- [`d2ff6d7`](https://github.com/ghostty-org/ghostty/commit/d2ff6d77a05d9e9b247684fad6bcb7979d0b2aca) terminal: pages initialize from zeroed memory and cache-line align their cells ([@mitchellh](https://github.com/mitchellh))
- [`07bccf7`](https://github.com/ghostty-org/ghostty/commit/07bccf7a311acdfa6afc77f2016160d49b1f1982) terminal: make all page data structures treat zero as empty to avoid eagerly paging in mmap pages ([#14137](https://github.com/ghostty-org/ghostty/issues/14137)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This updates all our page data structures so that the `0` value
  (literally `@memset(0)`) means empty. This way, when we initialize a new
  page via mmap (OS-guaranteed zeroed), we don't need to write to it, and
  don't trigger the kernel to physically map the memory.
  
  From Ghostty 1.3.1, our empty terminal physical memory usage goes from
  128 KB to 48 KB (#14130) to 16 KB (this PR). And even with an empty
  prompt written on my machine, it holds at 16KB, only increasing to two
  pages (32 KB) with 24 rows written.
  
  Here are some measurements.
  
  | Per terminal | Before (macOS) | After (macOS) | Before (Linux) | After
  (Linux) |
  
  |-------------------------------------------------------|----------------|---------------|----------------|---------------|
  | Page-list memory dirty, fresh | 48 KiB | 16 KiB | 24 KiB | 8 KiB |
  | Page-list memory dirty, 24 visible rows written | 64 KiB | 32 KiB | 36
  KiB | 20 KiB |
  
  Note macOS uses 16KB pages and Linux generally uses 4 KB pages.
  
  I ran `ghostty-bench +terminal-stream` main vs this branch and with
  every normal workload the results are within noise (sometimes faster
  sometimes slower).
  
  **AI usage:** It was used as a judge/validator. The actual changes were
  me, commit messages and PR messages all me.
  ```
- [`efa3c66`](https://github.com/ghostty-org/ghostty/commit/efa3c66ed16ea9251d5b2a74b606aabc248d2c00) terminal: PageList nodes are pooled individually from the gpa instead of an arena ([@mitchellh](https://github.com/mitchellh))
- [`35a6fb7`](https://github.com/ghostty-org/ghostty/commit/35a6fb747f5d60ee6d92a7f5667474914a47cf21) terminal: PageList preheats only the viewport and cursor pins ([@mitchellh](https://github.com/mitchellh))
- [`105d0a5`](https://github.com/ghostty-org/ghostty/commit/105d0a5453654f15cbe9e902df9e72ed62fa5474) terminal: C terminal wrapper allocates the kitty temp dir path only when it is set ([@mitchellh](https://github.com/mitchellh))
- [`d1cd56a`](https://github.com/ghostty-org/ghostty/commit/d1cd56a56c4244d9d9fadae028cbffc23a1d3d1a) terminal: dynamic palette shares the built-in default instead of copying it per terminal ([@mitchellh](https://github.com/mitchellh))
- [`c81f0b2`](https://github.com/ghostty-org/ghostty/commit/c81f0b26871c7fbbe2fc35549fdad1f64ed29094) terminal: cut the fixed heap cost of a new terminal nearly in half ([#14138](https://github.com/ghostty-org/ghostty/issues/14138)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This focuses explicitly on the non-mmap allocations for a
  `ghostty_terminal_new` result. The result is that we lower this portion
  of the memory by almost half. The total benefit is smaller since 70% of
  a terminal is mmap'd allocations, but this still yields an absolute ~5KB
  savings on macOS on every new terminal (not just empty, but also with a
  normal prompt and so on).
  
  Four changes to make it happy, broken down into individual commits.
  Nothing crazy:
  
  - **Page list nodes are pooled individually.** The node pool was a
  `std.heap.MemoryPool`, which sits on an arena that preheats and grows
  1.5x, so we paid for wasted space. Nodes now come from `UntouchedPool`
  (the same pool as page buffers) with a preheat of one, so the cost is
  exactlyone node (well, exactly one bucket element size in whatever
  allocator).
  - **Pin pool and tracked pin set are sized for two pins.** Every screen
  tracks exactly a viewport pin and a cursor pin at creation, but we
  preheated eight pins and let the tracked pin map grow to 17 slots on the
  first insert via doubling.
  - **The kitty temp dir path is allocated only when set.** The C wrapper
  embedded a 1 KiB `max_path_bytes` buffer that only embedders that set
  `kitty_image_medium_temp_file` ever wrote to.
  - **The default palette is shared instead of copied.** `DynamicPalette`
  carried two full 1 KiB palettes, `current` and `original`, and
  `original` was almost always the built-in default. It is now a pointer
  to the shared built-in default, or to an allocator-owned copy when a
  custom default is set. This introduces a new OOM path but we gracefully
  handle it by either ignoring or resetting.
  
  Memory measurements:
  
  | Per terminal                                | Before   | After    |
  |---------------------------------------------|----------|----------|
  | phys_footprint delta, fresh                 | 30,066 B | 25,069 B |
  | phys_footprint delta, styled prompt written | 47,023 B | 41,944 B |
  | malloc zone bytes dirtied, fresh            | 12,698 B | 7,782 B  |
  | malloc blocks live after `terminal_new`     | 11,904 B | 6,688 B  |
  | malloc blocks live after the prompt         | 12,320 B | 7,104 B  |
  
  I ran `ghostty-bench +terminal-stream` on a 500 MB ascii corpus, main vs
  this branch interleaved, and there is no noticeable change.
  
  **AI usage:** Fable did validation of the work, I did the
  implementations, commit messages, and PR notes.
  ```
- [`4406cea`](https://github.com/ghostty-org/ghostty/commit/4406cea3e9fde88876551cedfef10d3b245b75b6) input: encode ctrl keys with modifyOtherKeys 2 ([@mitchellh](https://github.com/mitchellh))
  ```text
  #7425
  
  Control-modified characters use xterm's MOK2 encoding.
  
  I incorrectly believed previously that MOK2 ctrl chars were still encoded
  as C0 bytes. This is wrong. I'm going to do a more in depth audit if
  possible with every possible key combination against xterm to see where
  we diverge but this fixes this for now without regressing any tests.
  
  Background: https://invisible-island.net/xterm/modified-keys.html
  ```
- [`1f5bb57`](https://github.com/ghostty-org/ghostty/commit/1f5bb5769fbb5e717546073d33d3985604a315b2) input: encode ctrl keys with modifyOtherKeys 2 ([#14144](https://github.com/ghostty-org/ghostty/issues/14144)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  #7425
  
  Control-modified characters use xterm's MOK2 encoding.
  
  I incorrectly believed previously that MOK2 ctrl chars were still
  encoded as C0 bytes. This is wrong. I'm going to do a more in depth
  audit if possible with every possible key combination against xterm to
  see where we diverge but this fixes this for now without regressing any
  tests.
  
  Background: https://invisible-island.net/xterm/modified-keys.html
  ```
- [`636a2f3`](https://github.com/ghostty-org/ghostty/commit/636a2f35b4a37fbb1b58dd801ae14513d355e95e) input: preserve numeric keypad output with MOK2 ([@mitchellh](https://github.com/mitchellh))
- [`e7bdda9`](https://github.com/ghostty-org/ghostty/commit/e7bdda9918a87f74178e15132c2894e29a8bf271) input: encode F13 through F25 ([@mitchellh](https://github.com/mitchellh))
- [`37e3cdd`](https://github.com/ghostty-org/ghostty/commit/37e3cdd2d281feb2bb403600974289406f891461) input: encode alt+escape with MOK2 ([@mitchellh](https://github.com/mitchellh))
- [`cc3fd8a`](https://github.com/ghostty-org/ghostty/commit/cc3fd8a773300371e2d1f41265128a7bf10adfa2) input: encode help and context menu keys ([@mitchellh](https://github.com/mitchellh))
- [`b97654f`](https://github.com/ghostty-org/ghostty/commit/b97654fe76a8badbbb0c51c0c0e2156fd12f0731) input: improve xterm modifyOtherKeys 2 compatibility ([#14145](https://github.com/ghostty-org/ghostty/issues/14145)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Follow-up to #14144
  
  I wrote a harness that created all possible US-layout keyboard input
  combinations with xterm patch 411 and Ghostty main and compared their
  full encoding sequence. There are various miscompatibilities on purpose
  but these were definitely bugs I wanted to address first.
  
  - Normal-mode numeric keypad keys now preserve their numeric output
  instead of falling through to generic MOK2 encoding. Application keypad
  behavior is unchanged.
  - F13 through F25 now emit their xterm-compatible function-key
  sequences, including modifier parameters.
  - Help and Context Menu now emit editing-key codes 28 and 29.
  - Alt+Escape now emits `CSI 27;3;27~` under MOK2 while retaining the
  traditional `ESC ESC` encoding otherwise.
  
  After these changes, 2,081 of 2,096 cases match xterm exactly. The
  remaining 15 differences are intentional.
  ```
- [`587e08f`](https://github.com/ghostty-org/ghostty/commit/587e08f3f70d29c7bc196e2cd919bd4b11f9b5bb) input: encode non-ASCII alt prefixes as UTF-8 ([@mitchellh](https://github.com/mitchellh))
  ```text
  Legacy Alt-as-Escape now prefixes the complete UTF-8 sequence for
  non-ASCII input. When text is unavailable, the encoder falls back to
  the UTF-8 encoding of the unshifted codepoint.
  
  This fixes 16 xterm legacy cases and eight fixterms cases without changing
  MOK2. The cases I'm talking about are in my comparison harness...
  
  The helper now writes Escape and the selected payload directly. It
  preserves macOS Option-as-Alt translation and shifted ASCII behavior.
  ```
- [`492300c`](https://github.com/ghostty-org/ghostty/commit/492300cad104195411d12217dd22f1cd05f31376) input: encode non-ASCII alt prefixes as UTF-8 ([#14146](https://github.com/ghostty-org/ghostty/issues/14146)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Legacy Alt-as-Escape now prefixes the complete UTF-8 sequence for
  non-ASCII input. When text is unavailable, the encoder falls back to the
  UTF-8 encoding of the unshifted codepoint.
  
  This fixes 16 xterm legacy cases and eight fixterms cases without
  changing MOK2. The cases I'm talking about are in my comparison
  harness...
  
  The helper now writes Escape and the selected payload directly. It
  preserves macOS Option-as-Alt translation and shifted ASCII behavior.
  ```
- [`11d1cc4`](https://github.com/ghostty-org/ghostty/commit/11d1cc4fc8decc84048bde1b746f3a013493e36f) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`50f757d`](https://github.com/ghostty-org/ghostty/commit/50f757dc84c1179fe55ee396fb00268ae8dab0b9) i18n(de): adjust floating state description ([@rpfaeffle](https://github.com/rpfaeffle))
- [`5909690`](https://github.com/ghostty-org/ghostty/commit/5909690de1d942c8b846dfd51c8a26e510436ade) config: rebuild RepeatableCommand's C mirror on clone ([@i999rri](https://github.com/i999rri))
  ```text
  Cloning value_c copied Command.C structs whose string pointers
  still referenced the source config's memory; once the source was
  freed, an embedded host reading the command list after a config
  replace (ghostty_config_clone + ghostty_config_free of the old
  one) hit use-after-free, caught by ASan. Rebuild the mirror from
  the cloned commands with the same cval path parseCLI uses, and add
  a regression test asserting the clone's C strings do not alias the
  source's.
  ```
- [`955d902`](https://github.com/ghostty-org/ghostty/commit/955d902fa6abb3aaf71cac60d6b81bd83fa7fc69) pkg/fontconfig: update to 2.18.3 ([#14113](https://github.com/ghostty-org/ghostty/issues/14113)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Supersedes #14071 (just additional review and local re-generation/re-org
  of needed headers).
  
  This updates our own bundled fontconfig (for static builds) to 2.18.3.
  
  Note that fontconfig has changed their build process a bit since this
  has been updated last; they are leaning on the Autoconf (and Meson as
  they are now deprecating use of Autoconf) toolchain(s) to now generate a
  number of headers that are a part of the build process.
  
  Since servicing this dependency in an effort to keep the build pure Zig
  is starting to get more complex, I've added some documentation on how to
  actually get a snapshot of the fontconfig repository in a state where
  files can be looked for and copied over as needed. Otherwise, we might
  want to in the future consider removing this altogether and just rely on
  system integrations.
  ```
- [`f426f6f`](https://github.com/ghostty-org/ghostty/commit/f426f6f181ba95f45d33f683fb754b6359d9e04f) Update iTerm2 colorschemes ([#14159](https://github.com/ghostty-org/ghostty/issues/14159)) ([@jcollie](https://github.com/jcollie))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260831-151010-752a9c0
  ```
- [`97f2ddb`](https://github.com/ghostty-org/ghostty/commit/97f2ddb06e43ed73948385944cd1b0c19c282807) Sync CODEOWNERS vouch list ([#14163](https://github.com/ghostty-org/ghostty/issues/14163)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Sync CODEOWNERS owners with vouch list.
  
  ## Added Users
  
  - @slowdub
  ```
- [`258c057`](https://github.com/ghostty-org/ghostty/commit/258c057c0ac7d23b8a908fc1f4c5636670ccdcd1) build(deps): bump ryand56/r2-upload-action from 1.4 to 1.5 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [ryand56/r2-upload-action](https://github.com/ryand56/r2-upload-action) from 1.4 to 1.5.
  - [Release notes](https://github.com/ryand56/r2-upload-action/releases)
  - [Commits](https://github.com/ryand56/r2-upload-action/compare/b801a390acbdeb034c5e684ff5e1361c06639e7c...33ebb7a494b3a8a3c5ed2ea6bbdc72e707090317)
  
  ---
  updated-dependencies:
  - dependency-name: ryand56/r2-upload-action
    dependency-version: '1.5'
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`e9283ba`](https://github.com/ghostty-org/ghostty/commit/e9283ba872bfb2135dbaadea68d08980dbae5f88) build(deps): bump c-hive/gha-remove-artifacts from 1.4.0 to 1.8.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [c-hive/gha-remove-artifacts](https://github.com/c-hive/gha-remove-artifacts) from 1.4.0 to 1.8.0.
  - [Release notes](https://github.com/c-hive/gha-remove-artifacts/releases)
  - [Commits](https://github.com/c-hive/gha-remove-artifacts/compare/44fc7acaf1b3d0987da0e8d4707a989d80e9554b...62c2fbea931baa7dd4a6b73ea5a799984a818f61)
  
  ---
  updated-dependencies:
  - dependency-name: c-hive/gha-remove-artifacts
    dependency-version: 1.8.0
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`2b3b893`](https://github.com/ghostty-org/ghostty/commit/2b3b893919e0bee74b567598e741a735777c9687) deps: update translate-c backport ([@vancluever](https://github.com/vancluever))
- [`82938b6`](https://github.com/ghostty-org/ghostty/commit/82938b633ba646db38591d969c3c526332bd7e65) deps: update translate-c backport ([#14126](https://github.com/ghostty-org/ghostty/issues/14126)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This is just a monthly refresh, things have been pretty quiet on both
  the Aro and translate-c sides.
  
  https://github.com/vancluever/arocc/compare/ecbc5c7...f97cdfc
  
  https://codeberg.org/vancluever/translate-c/compare/05e7b9dd87...4e879eb8ab
  ```
- [`ccaf7c7`](https://github.com/ghostty-org/ghostty/commit/ccaf7c776144cb5200fa0de605159cb90788a286) build(deps): bump ryand56/r2-upload-action from 1.4 to 1.5 ([#14164](https://github.com/ghostty-org/ghostty/issues/14164)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [ryand56/r2-upload-action](https://github.com/ryand56/r2-upload-action)
  from 1.4 to 1.5.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/ryand56/r2-upload-action/releases">ryand56/r2-upload-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v1.5</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>chore(deps): update dependency <code>@​types/node</code> to v22.9.0
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/524">ryand56/r2-upload-action#524</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.686.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/526">ryand56/r2-upload-action#526</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.687.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/527">ryand56/r2-upload-action#527</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.688.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/528">ryand56/r2-upload-action#528</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.689.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/529">ryand56/r2-upload-action#529</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.691.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/530">ryand56/r2-upload-action#530</a></li>
  <li>chore(deps): update determinatesystems/nix-installer-action action
  to v16 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/531">ryand56/r2-upload-action#531</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.693.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/532">ryand56/r2-upload-action#532</a></li>
  <li>chore(deps): update dependency <code>@​vercel/ncc</code> to v0.38.3
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/534">ryand56/r2-upload-action#534</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.693.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/533">ryand56/r2-upload-action#533</a></li>
  <li>chore(deps): update dependency typescript to v5.7.2 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/537">ryand56/r2-upload-action#537</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.700.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/536">ryand56/r2-upload-action#536</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.701.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/538">ryand56/r2-upload-action#538</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.703.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/539">ryand56/r2-upload-action#539</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to v22.10.1
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/535">ryand56/r2-upload-action#535</a></li>
  <li>chore(deps): update dependency dotenv to v16.4.6 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/540">ryand56/r2-upload-action#540</a></li>
  <li>chore(deps): update dependency dotenv to v16.4.7 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/541">ryand56/r2-upload-action#541</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.705.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/542">ryand56/r2-upload-action#542</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.709.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/543">ryand56/r2-upload-action#543</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to v22.10.2
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/544">ryand56/r2-upload-action#544</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.712.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/545">ryand56/r2-upload-action#545</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.713.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/546">ryand56/r2-upload-action#546</a></li>
  <li>fix(deps): update dependency mime to v4.0.6 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/548">ryand56/r2-upload-action#548</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.715.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/547">ryand56/r2-upload-action#547</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.717.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/549">ryand56/r2-upload-action#549</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to v22.10.3
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/550">ryand56/r2-upload-action#550</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to v22.10.5
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/551">ryand56/r2-upload-action#551</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.722.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/552">ryand56/r2-upload-action#552</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.723.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/553">ryand56/r2-upload-action#553</a></li>
  <li>chore(deps): update dependency typescript to v5.7.3 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/554">ryand56/r2-upload-action#554</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.726.1 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/555">ryand56/r2-upload-action#555</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to v22.10.6
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/556">ryand56/r2-upload-action#556</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.731.1 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/557">ryand56/r2-upload-action#557</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to v22.10.7
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/558">ryand56/r2-upload-action#558</a></li>
  <li>chore(deps): update determinatesystems/magic-nix-cache-action action
  to v9 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/560">ryand56/r2-upload-action#560</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to
  v22.10.10 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/561">ryand56/r2-upload-action#561</a></li>
  <li>chore(deps): update dependency typescript to v5.8.2 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/564">ryand56/r2-upload-action#564</a></li>
  <li>ci(test-nix): replace magic nix cache with flakehub cache by <a
  href="https://github.com/ryand56"><code>@​ryand56</code></a> in <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/567">ryand56/r2-upload-action#567</a></li>
  <li>chore(deps): update dependency typescript to v5.8.3 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/566">ryand56/r2-upload-action#566</a></li>
  <li>fix(deps): update dependency mime to v4.0.7 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/565">ryand56/r2-upload-action#565</a></li>
  <li>chore(deps): update determinatesystems/nix-installer-action action
  to v17 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/569">ryand56/r2-upload-action#569</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.810.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/559">ryand56/r2-upload-action#559</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to
  v22.15.19 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/572">ryand56/r2-upload-action#572</a></li>
  <li>chore(deps): update stefanzweifel/git-auto-commit-action action to
  v6 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/576">ryand56/r2-upload-action#576</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.832.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/571">ryand56/r2-upload-action#571</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to
  v22.15.33 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/573">ryand56/r2-upload-action#573</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.837.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/577">ryand56/r2-upload-action#577</a></li>
  <li>chore(deps): update dependency dotenv to v16.6.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/578">ryand56/r2-upload-action#578</a></li>
  </ul>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/33ebb7a494b3a8a3c5ed2ea6bbdc72e707090317"><code>33ebb7a</code></a>
  chore: update to nodejs 24</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/61474c8f6a21b0dd8fc877a0b93c2c2078c88f60"><code>61474c8</code></a>
  chore: update mappings [skip ci]</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/7d9e7c27f8702296342da8daf84e76b24e43622d"><code>7d9e7c2</code></a>
  chore(deps): update typescript to v6</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/6e86c77f4ab91d5b532f6156c15509ef35fd905a"><code>6e86c77</code></a>
  fix(renovate): increase minimumReleaseAge and add packageRules for
  ts</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/fd3d3d4ccdcea99f8e7cc84bbb0a468147e9235e"><code>fd3d3d4</code></a>
  chore(deps): update dependency jest to v30.5.1</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/0b5990b910991eb1c068df9f99384b66e0b49e41"><code>0b5990b</code></a>
  chore(deps): update dependency github-action-ts-run-api to v3.1.0</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/4196309eee620f2cd556648b16b4b45fd959cee9"><code>4196309</code></a>
  chore(deps): update dependency dotenv to v17.4.2</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/d62fd1388703f08312d5f62fdef74f4b363a2802"><code>d62fd13</code></a>
  chore(deps): update dependency <code>@​vercel/ncc</code> to ^0.45.0</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/5124bb99384f12af4f3947f0c6a8f6509d580079"><code>5124bb9</code></a>
  chore(deps): update dependency ts-jest to v29.4.12</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/820995a4f185d5c18d4c60e6e371494e3046b336"><code>820995a</code></a>
  chore(deps): update dependency <code>@​actions/core</code> to
  v3.0.1</li>
  <li>Additional commits viewable in <a
  href="https://github.com/ryand56/r2-upload-action/compare/b801a390acbdeb034c5e684ff5e1361c06639e7c...33ebb7a494b3a8a3c5ed2ea6bbdc72e707090317">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=ryand56/r2-upload-action&package-manager=github_actions&previous-version=1.4&new-version=1.5)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`da9e216`](https://github.com/ghostty-org/ghostty/commit/da9e21602f918d47a46399c458937eff7c7a74ac) build(deps): bump c-hive/gha-remove-artifacts from 1.4.0 to 1.8.0 ([#14165](https://github.com/ghostty-org/ghostty/issues/14165)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [c-hive/gha-remove-artifacts](https://github.com/c-hive/gha-remove-artifacts)
  from 1.4.0 to 1.8.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/c-hive/gha-remove-artifacts/releases">c-hive/gha-remove-artifacts's
  releases</a>.</em></p>
  <blockquote>
  <h2>v1.8.0</h2>
  <p>Enhancements:</p>
  <ul>
  <li>New <code>skip-recent-commits</code> input keeps every artifact of
  the N most recent commits, regardless of how many artifacts each commit
  produced. Applied before <code>skip-recent</code>, so the two can be
  combined. Fixes <a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/28">#28</a></li>
  <li><code>GITHUB_TOKEN</code> can now be set on both <code>env:</code>
  and <code>with:</code> (for example when it is exported for all steps)
  without the action failing. The input takes precedence. Fixes <a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/48">#48</a></li>
  </ul>
  <h2>v1.7.0</h2>
  <p>Enhancements:</p>
  <ul>
  <li>New <code>dry-run</code> input: logs which artifacts would be
  removed without deleting anything.</li>
  <li>Stricter input validation. <code>age</code> now rejects fractional
  amounts and units that are not durations (for example <code>30 D</code>,
  which moment silently treated as zero); <code>skip-recent</code> and
  <code>max-retries</code> must be non-negative integers. Previously such
  values could make every artifact eligible for deletion.</li>
  <li>Artifacts without commit information are reported separately from
  tagged ones when <code>skip-tags</code> is on.</li>
  </ul>
  <p>Maintenance:</p>
  <ul>
  <li>Rewritten in TypeScript under <code>src/</code>, bundled with
  esbuild</li>
  <li>Unit tests for input parsing and the cleanup plan, plus end-to-end
  tests against a mock GitHub API covering deletion, rate limit retries
  and failure handling</li>
  <li>CI split into lint, typecheck, test, build and run jobs</li>
  <li>Dropped dependencies: yn, dotenv-safe, cross-env,
  eslint-plugin-import</li>
  </ul>
  <h2>v1.6.0</h2>
  <p>Enhancements:</p>
  <ul>
  <li>Artifacts are now listed repo-wide instead of per workflow run. This
  cuts API requests by roughly two orders of magnitude and removes the
  hardcoded 90-day window, so artifacts on repositories with longer
  retention are now cleaned up too. Fixes <a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/62">#62</a></li>
  <li>A failed deletion no longer aborts the run: remaining artifacts are
  still processed and the action fails at the end with a count.</li>
  <li>With <code>skip-tags</code>, artifacts without commit information
  are kept rather than deleted.</li>
  <li>The log ends with a summary of removed and skipped artifacts. Fixes
  <a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/21">#21</a></li>
  </ul>
  <p>Maintenance:</p>
  <ul>
  <li>CI checks that <code>dist/</code> matches the source instead of
  auto-committing it</li>
  <li>Removed CodeQL workflow, pre-commit hooks and
  eslint-plugin-import</li>
  <li>Dependency purposes documented in <code>package.json</code></li>
  </ul>
  <h2>v1.5.0</h2>
  <p>Enhancements:</p>
  <ul>
  <li>New <code>max-retries</code> input caps how often a rate-limited
  request is retried before the action fails. <strong>Default: 5.</strong>
  Previously requests were retried indefinitely; set a larger value to
  keep the old behaviour. Fixes <a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/36">#36</a>,
  <a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/49">#49</a>,
  <a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/51">#51</a></li>
  <li>Action runtime updated to Node 24 (<a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/63">#63</a>)</li>
  </ul>
  <p>Maintenance:</p>
  <ul>
  <li>All dependencies upgraded (<code>@actions/core</code> 3,
  <code>@octokit/action</code> 8, <code>@octokit/plugin-throttling</code>
  11, moment 2.30). <code>pnpm audit</code> reports no known
  vulnerabilities.</li>
  <li>Source converted to ESM, bundled with <code>@vercel/ncc</code></li>
  <li>Tooling: pnpm, ESLint 10, Prettier 3, CI on Node 24</li>
  <li>Docs: <code>action.yml</code> description, updated retention docs
  link</li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/62c2fbea931baa7dd4a6b73ea5a799984a818f61"><code>62c2fbe</code></a>
  Bump version to 1.8.0</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/449a616233a48dbdd28ba5e08f4c2fb62913afa8"><code>449a616</code></a>
  Add skip-recent-commits input and accept GITHUB_TOKEN from env and
  input</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/4bff15786ba0b91dd8ed7c32459eb72441ac1b6c"><code>4bff157</code></a>
  Bump version to 1.7.0</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/a52e55eb4fd2dd1ce50f4e125d7e5855873bb38a"><code>a52e55e</code></a>
  Add end-to-end tests against a mock GitHub API</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/03f14e2351077f8bc463a7887eba3d4c062347b1"><code>03f14e2</code></a>
  Simplify config parsing, logging and tsconfig</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/04de7b0694b817261c05361cebc55090c8be4fb8"><code>04de7b0</code></a>
  Address review findings on the TypeScript rewrite</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/8b74b1b6fcb2881415de6d93701d4f4de6b170b1"><code>8b74b1b</code></a>
  Rewrite in TypeScript, add tests, merge CI workflows</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/73aaf4a5bf7a8fc25eca958284e770e44493029a"><code>73aaf4a</code></a>
  Bump version to 1.6.0</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/c4da97c8ee1e02b19ba57ae62c3fafd4b618e06d"><code>c4da97c</code></a>
  Ignore CLAUDE.local.md</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/614c11c542a610a4eec69c8e2faa27904004155f"><code>614c11c</code></a>
  Describe each dependency in package.json</li>
  <li>Additional commits viewable in <a
  href="https://github.com/c-hive/gha-remove-artifacts/compare/44fc7acaf1b3d0987da0e8d4707a989d80e9554b...62c2fbea931baa7dd4a6b73ea5a799984a818f61">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=c-hive/gha-remove-artifacts&package-manager=github_actions&previous-version=1.4.0&new-version=1.8.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`6f6da70`](https://github.com/ghostty-org/ghostty/commit/6f6da700ede0289ecb534a726b0b13c584a23f8e) Merge branch 'ghostty-org:main' into i18n-update-translation-lt-for-v1.4 ([@tdslot](https://github.com/tdslot))
- [`72cf508`](https://github.com/ghostty-org/ghostty/commit/72cf508551cb1c559c9ca32330e9647399031ebb) renderer: never stop the display link while holding the draw mutex ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #14150
  
  drawFrame called syncDisplayLink from its no-redraw path while still
  holding draw_mutex, and syncDisplayLink stops the CVDisplayLink when
  there is no work left. CVDisplayLinkStop is a blocking join on
  CoreVideo's IO thread. On macOS the apprt also calls drawFrame from the
  CoreAnimation layer display callback on the main thread, which takes
  the same mutex, so any CoreVideo stall inside that stop deadlocked.
  ```
- [`623106c`](https://github.com/ghostty-org/ghostty/commit/623106cc4ea9ad5b8cc070e5e5c5260eb6eeaa7b) config: rebuild RepeatableCommand's C mirror on clone ([#14170](https://github.com/ghostty-org/ghostty/issues/14170)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Why
  
  `RepeatableCommand.clone` copies `value_c` shallowly: the cloned
  `Command.C` structs keep string pointers into the *source* config's
  memory, so the clone only stays valid as long as its source lives. Every
  other field of a config clone is a deep copy — this is the one spot
  where the clone silently borrows.
  
  The macOS app never notices because of how it rotates configs: its
  clone's source is the core-owned live config, and both are replaced
  together on the next reload, so a clone never outlives its source. An
  embedder that clones a config and then frees the source — a legal
  sequence, e.g. promoting the clone to be the new active config — reads
  freed memory the next time it fetches `command-palette-entry` through
  the C API. Caught by AddressSanitizer.
  
  History: the shallow copy is as old as the C exposure itself.
  `dbe6035da` introduced `RepeatableCommand` with a correct deep `clone`
  (zig-side `value` only); `017021787` added the `value_c` mirror for
  `ghostty_config_get`, maintaining it carefully in `init`/`parseCLI` but
  extending `clone` with only the mechanical `ArrayList.clone` — the
  struct array copies, the string ownership doesn't. Nothing in-tree
  exercises clone-then-free-source, so it stayed latent.
  
  ## What
  
  Rebuild the C mirror from the cloned commands using the same
  `Command.cval` path `parseCLI` uses, so the clone's C strings live in
  the clone's own allocation. A regression test asserts the clone's C
  strings do not alias the source's while staying equal in content.
  
  ## AI disclosure
  
  Developed with AI assistance (Claude Code). The bug was found by
  AddressSanitizer while testing the Windows embedding host; the
  root-cause analysis, the fix, and the regression test were produced in
  an AI-assisted session, then reviewed and verified by the submitter
  (ASan clean after the fix, `RepeatableCommand` tests passing).
  ```
- [`82232ec`](https://github.com/ghostty-org/ghostty/commit/82232ecde55405559dec29c5466cb9e39938cb41) renderer: never stop the display link while holding the draw mutex ([#14171](https://github.com/ghostty-org/ghostty/issues/14171)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #14150
  
  drawFrame called syncDisplayLink from its no-redraw path while still
  holding draw_mutex, and syncDisplayLink stops the CVDisplayLink when
  there is no work left. CVDisplayLinkStop is a blocking join on
  CoreVideo's IO thread. On macOS the apprt also calls drawFrame from the
  CoreAnimation layer display callback on the main thread, which takes the
  same mutex, so any CoreVideo stall inside that stop deadlocked.
  ```
- [`ff5b87e`](https://github.com/ghostty-org/ghostty/commit/ff5b87e4dbef56cd6b54174520ed151b88c47368) i18n: re-apply remaining lt.po review suggestions ([@tdslot](https://github.com/tdslot))
  ```text
  Eleven review suggestions from the PR were accepted but never made it
  into the pushed commit. Re-apply them and rewrap the affected entries to
  the canonical 79-column gettext width.
  
  Claude-Session: https://claude.ai/code/session_019aW9GqQj7USLWhmzNhuE34
  ```
- [`607d59b`](https://github.com/ghostty-org/ghostty/commit/607d59b0e8ef46da6e6e6e490ef8e82f961ffb25) i18n: fix Lithuanian grammar and terminology consistency in lt.po ([@tdslot](https://github.com/tdslot))
  ```text
  The wording follows the consultation bank of the VLKK (State Commission
  of the Lithuanian Language) rather than personal preference; the
  relevant entries are cited per change.
  
  - "padalinti" -> "padalyti" (9 strings). VLKK treats "dalyti" and
    "dalinti" as equal variants of the norm, prefixed derivatives
    explicitly included ("padalyti ir padalinti"), but advises picking one
    per text: "Viename tekste patartina pasirinkti vieną kurį variantą ir
    nuosekliai jį vartoti. Nereikėtų kaitalioti ir iš veiksmažodžio dalyti
    ir jo formų padarytų įsigalėjusių terminų."
    https://vlkk.lt/konsultacijos/4607-dalyti-dalinti
    The file was mixing them: the verb was "padalinti" while the noun
    everywhere was "padalijimas", which is formed from "dalyti". Unified
    on the "dalyti" line, since the established noun already commits the
    file to it, and it is also the primary variant in "Kalbos patarimai"
    (Vilnius, 2002, p. 69).
  
  - "atstatyti" -> "atkurti" / "nustatyti iš naujo" (7 strings). VLKK:
    "Veiksmažodis atstatyti reikšme 'grąžinti kokį dalyką į buvusią
    (nesusijusią su stovėjimu) padėtį' [...] vertinamas kaip verstinis ir
    vengtinas vartoti. Vartotini junginiai su veiksmažodžiais grąžinti,
    atkurti ar pan."
    https://vlkk.lt/konsultacijos/12800-atstatyti
    https://vlkk.lt/konsultacijos/235-atstatyti
    Restoring a default font or window size is exactly that sense, so
    "Reset Font Size" / "Reset Window Size" are now "Atkurti...". The file
    already used "atkurti" in "Išdidinti arba atkurti langą". Plain
    "Reset" and "Reset Terminal" re-initialise rather than restore a
    previous value, so those became "Nustatyti (terminalą) iš naujo".
  
  - "selection" is now consistently "pažymėtas tekstas" / "pažymėjimas"
    (26 strings). It had been split between that and "pasirinkimas",
    which means "a choice" -- the sense the file already uses it in for
    "Remember choice for this split".
  
  - "Toggle Fullscreen" now uses the same "Įjungti arba išjungti" pattern
    as the other on/off toggles.
  
  - "Equalize Splits" is plural, agreeing with its own description.
  
  - Unify the HTML "paste path" description with its plain/ANSI siblings,
    and minor wording fixes to the tagline and the $EDITOR description.
  
  Claude-Session: https://claude.ai/code/session_019aW9GqQj7USLWhmzNhuE34
  ```
- [`dd2edd7`](https://github.com/ghostty-org/ghostty/commit/dd2edd760da6b90b01ef88f75e1bea8a71b31e3f) libvt: return safe pointers for empty output ([@mitchellh](https://github.com/mitchellh))
  ```text
  Normalize empty buffers and borrowed strings at the libghostty-vt C
  boundary to null pointers.
  
  Zig can use sentinel addresses such as 0x1 for empty slices. Returning
  these pointers to Go can cause a fatal invalid-pointer error when the
  runtime relocates a goroutine's stack, even though the length is zero.
  ```
- [`b0c421f`](https://github.com/ghostty-org/ghostty/commit/b0c421fcd2e290629d4285c181b52fe2f2095f06) libghostty: return safe pointers for empty output ([#14177](https://github.com/ghostty-org/ghostty/issues/14177)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Normalize empty buffers and borrowed strings at the libghostty-vt C
  boundary to null pointers.
  
  Zig can use sentinel addresses such as 0x1 for empty slices. Returning
  these pointers to Go can cause a fatal invalid-pointer error when the
  runtime relocates a goroutine's stack, even though the length is zero.
  ```
- [`1ff027c`](https://github.com/ghostty-org/ghostty/commit/1ff027c3322864c3c28e701496c8e9d5c14cd4ee) i18n(hr): started updating hr translation ([@Filip7](https://github.com/Filip7))
  ```text
  Related issue #13766
  ```
- [`437dce2`](https://github.com/ghostty-org/ghostty/commit/437dce21bc4853b89af56daa88a5fd5af2911d75) Update hr.po ([@kristina8888](https://github.com/kristina8888))
  ```text
  added new translations for croatian language
  ```
- [`edf3aa0`](https://github.com/ghostty-org/ghostty/commit/edf3aa01bb4d4ce2544f58213eb98c0b90c99911) i18n(hr): added more translations and fixes ([@Filip7](https://github.com/Filip7))
- [`c01c683`](https://github.com/ghostty-org/ghostty/commit/c01c683eb0564b741de6f535e95c3ffc43aff59b) i18n(hr): "toggle" string translations ([@Filip7](https://github.com/Filip7))
  ```text
  i18n(hr): add missing translations and correct some others
  ```
- [`d1ed60d`](https://github.com/ghostty-org/ghostty/commit/d1ed60d569292c249ddfba42a91d452865c34762) Update hr.po ([@kristina8888](https://github.com/kristina8888))
- [`68852fc`](https://github.com/ghostty-org/ghostty/commit/68852fc008e0d14391fb284d3bbfb2276efd4033) i18n(hr): unify translation ([@Filip7](https://github.com/Filip7))
  ```text
  Use "zaslon" instead of "ekran"
  ```
- [`4480625`](https://github.com/ghostty-org/ghostty/commit/448062571c5edf010b7490d06869b88b5ebf8f80) i18n: Started updating hr translation ([#14019](https://github.com/ghostty-org/ghostty/issues/14019)) ([@trag1c](https://github.com/trag1c))
  ```text
  Related issue #13766
  ```
- [`0b54463`](https://github.com/ghostty-org/ghostty/commit/0b54463649eee14c0628cc7ab95065f8a299e73c) terminal/kitty: reject unsafe Windows paths for image file mediums ([@mitchellh](https://github.com/mitchellh))
  ```text
  The Kitty graphics file and temporary file mediums open a
  client-supplied path and the Kitty specification only specifies the
  blocklist for Unix-style machines.
  
  Windows has various unsafe paths as well that we should very obviously
  block. This diverges from the Kitty specification for now (I plan
  on reporting this upstream and asking for feedback) but I think its the
  right move for security.
  
  Windows dangerous namespaces:
  
    - A UNC path (`\\server\share\x`, also `//server/share/x`) makes the
      process resolve the host and authenticate to it over SMB.
    - The device namespaces (`\\.\`, `\\?\`, `\??\`) reach raw volumes and
      named pipes, where the open connects to something or blocks.
    - Reserved DOS device names (CON, NUL, COM1, ...) resolve to devices
      from inside any directory.
  
  These are now blocked.
  
  This commit also heap allocates the path buffer because max path on
  windows is around 100KB. :)
  ```
- [`7adbb51`](https://github.com/ghostty-org/ghostty/commit/7adbb5160d24bde9a65b5999d1ccd6ea4ec053b5) build/libghostty-vt: export uucode so that it can be re-used ([@jcollie](https://github.com/jcollie))
- [`cf4de79`](https://github.com/ghostty-org/ghostty/commit/cf4de795be50ec5bfe6675803a3371d4055f2beb) kitty: reject unsafe Windows paths for image file mediums ([#14189](https://github.com/ghostty-org/ghostty/issues/14189)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The Kitty graphics file and temporary file mediums open a
  client-supplied path and the Kitty specification only specifies the
  blocklist for Unix-style machines.
  
  Windows has various unsafe paths as well that we should very obviously
  block. This diverges from the Kitty specification for now (I plan on
  reporting this upstream and asking for feedback) but I think its the
  right move for security.
  
  Windows dangerous namespaces:
  
  - A UNC path (`\\server\share\x`, also `//server/share/x`) makes the
  process resolve the host and authenticate to it over SMB.
  - The device namespaces (`\\.\`, `\\?\`, `\??\`) reach raw volumes and
  named pipes, where the open connects to something or blocks.
  - Reserved DOS device names (CON, NUL, COM1, ...) resolve to devices
  from inside any directory.
  
  These are now blocked.
  
  This commit also heap allocates the path buffer because max path on
  windows is around 100KB. :)\
  
  **AI usage:** Fable and Astra both helped with validation, edge cases.
  ```
- [`60b4306`](https://github.com/ghostty-org/ghostty/commit/60b43068c5fc74c2117877b8ac4ecf9321bb8f24) terminal: reclaim pooled and compressed page memory on Windows ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds memory decommit/recommit support to Windows via
  DiscardVirtualMemory. This allows unused page memory to be reclaimed
  the same way it is already today on Linux and macOS.
  
  DiscardVirtualMemory releases the physical pages behind a committed
  range but leaves it committed, so a later access finds a zero page or
  the old contents rather than faulting, and nothing has to be committed
  again before reuse. That keeps recommit a no-op and, more importantly,
  keeps restoring a compressed page infallible.
  
  Windows has an alternative `VirtualFree(MEM_DECOMMIT)` followed by
  `VirtualAlloc(MEM_COMMIT)` which releases the commit charge as well, but
  Windows has no overcommit, so the commit can be refused on restore and our
  restore path doesn't support OOM.
  
  https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-discardvirtualmemory
  ```
- [`c488a41`](https://github.com/ghostty-org/ghostty/commit/c488a41b0673ec45e2dab28d0c8b6072b7da709f) nix: add libglvnd to devShell for EGL ([@pluiedev](https://github.com/pluiedev))
- [`fa2ec3a`](https://github.com/ghostty-org/ghostty/commit/fa2ec3a6a890c0d4e4d550564a8e37dc83d047ef) pkg/opengl: add EGL headers and bindings ([@pluiedev](https://github.com/pluiedev))
  ```text
  We need this for exporting DMABUFs and creating our own GL context
  independent of GTK.
  ```
- [`7581009`](https://github.com/ghostty-org/ghostty/commit/75810091686f5ee28d37550c4a7bb07eedaa51da) build: link against libEGL ([@pluiedev](https://github.com/pluiedev))
- [`2f0b653`](https://github.com/ghostty-org/ghostty/commit/2f0b65346918047518e7b32f9bbfa1240c15b62e) gtk,opengl: free us from the clutches of GtkGLArea ([@pluiedev](https://github.com/pluiedev))
  ```text
  GtkGLArea had numerous downsides that forced us to invent unsightly hacks
  in our renderer to work around them, most chiefly the fact that it holds
  its own GdkGLContext on the main thread (GL contexts are not at all
  thread-safe), forcing us to keep our GL calls on the main thread.
  It also does not interact well with triple-buffering and initialization
  is forced to be this sort of deferred song-and-dance since we need to
  wait for the GLArea to initialize its GL context before we can initialize
  the renderer, the core surface, and then most things in the GTK surface.
  
  We instead invent our own custom widget named RenderSurface that takes
  simple DMABUFs and displays them. The task of obtaining a GL context
  falls to manual EGL bindings, since we also need EGL to export OpenGL
  textures into DMABUFs. We keep the EGL context solely on the render
  thread meaning that the main thread never concerns itself with rendering
  except when being notified that the renderer has pushed a new frame.
  
  What makes this extra significant is that now the entire GTK apprt no
  longer depends on OpenGL in any way, shape or form. As long as it is
  being fed DMABUFs, it can render from whichever graphics API you want.
  This means we can add more backends based on OpenGL ES or more likely
  Vulkan rather painlessly in the future.
  
  **AI disclosure**: I came up with the idea and let Pi implement most of
  the nitty-gritty details around EGL, as well as replumbing the renderer
  and cleaning up all the GTK-specific workarounds there. I then carefully
  vetted every line of code and spent roughly as much time reviewing as
  coding. Most of the documentation and all commit messages are in my
  own words.
  ```
- [`380778e`](https://github.com/ghostty-org/ghostty/commit/380778e3ca8bd4083c76ce721f28417e0eacf396) ci: drop libghostty-internal builds on Windows ([@pluiedev](https://github.com/pluiedev))
  ```text
  libghostty-internal isn't really supposed to be used in Windows anyway,
  so why bother testing it?
  ```
- [`a5f604d`](https://github.com/ghostty-org/ghostty/commit/a5f604da718f600088504a37083ae1d160121af0) renderer: make LatestFrame methods no-ops when ExportedFrame is void ([@pluiedev](https://github.com/pluiedev))
- [`4c89835`](https://github.com/ghostty-org/ghostty/commit/4c8983586c4fcdeb0a13bc36a1820e5617c3877f) gtk: initialize core surface on first resize ([@pluiedev](https://github.com/pluiedev))
  ```text
  Now that our core surface does not depend on any GTK-sided OpenGL
  initialization, we can initialize it a lot earlier than before, during
  the first resize event right after GTK allocates the size for the widget.
  ```
- [`b87af86`](https://github.com/ghostty-org/ghostty/commit/b87af8646f71de1398e665c361fe659b0707a72e) pkg/opengl: replace cImport with translate-c ([@pluiedev](https://github.com/pluiedev))
  ```text
  General Zig 0.16+ futureproofing
  ```
- [`adf1614`](https://github.com/ghostty-org/ghostty/commit/adf161473d983986f48c9650152f707bd285d931) pkg/opengl: polish API ([@pluiedev](https://github.com/pluiedev))
- [`45aa963`](https://github.com/ghostty-org/ghostty/commit/45aa963d6b634f8d3e4e9a9ecdd272bf8ad751dd) opengl: delay opengl flush ([@pluiedev](https://github.com/pluiedev))
  ```text
  See https://github.com/ghostty-org/ghostty/pull/14052#issuecomment-5521325497
  ```
- [`ce5d51f`](https://github.com/ghostty-org/ghostty/commit/ce5d51f46f97e5321267abab488ff5d0fdabb2f6) gtk/render_surface: report dmabuf build errors ([@pluiedev](https://github.com/pluiedev))
- [`202fa8e`](https://github.com/ghostty-org/ghostty/commit/202fa8e39007ccbcc267173f1217422d1ac72736) gtk: do not disable OpenGL ES and Vulkan ([@pluiedev](https://github.com/pluiedev))
  ```text
  Apparently either OpenGL ES or Vulkan is required to present our DMABUFs
  for jcollie
  ```
- [`7644e6d`](https://github.com/ghostty-org/ghostty/commit/7644e6d627ede8042db16d264ed3d118d8832923) build/linghostty-vt: fix libvaxis access to uucode tables ([@jcollie](https://github.com/jcollie))
- [`95cfbbb`](https://github.com/ghostty-org/ghostty/commit/95cfbbb055c659f57da3650cfb733dbb5072f6a5) terminal: reclaim pooled and compressed page memory on Windows ([#14190](https://github.com/ghostty-org/ghostty/issues/14190)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds memory decommit/recommit support to Windows via
  DiscardVirtualMemory. This allows unused page memory to be reclaimed the
  same way it is already today on Linux and macOS.
  
  DiscardVirtualMemory releases the physical pages behind a committed
  range but leaves it committed, so a later access finds a zero page or
  the old contents rather than faulting, and nothing has to be committed
  again before reuse. That keeps recommit a no-op and, more importantly,
  keeps restoring a compressed page infallible.
  
  Windows has an alternative `VirtualFree(MEM_DECOMMIT)` followed by
  `VirtualAlloc(MEM_COMMIT)` which releases the commit charge as well, but
  Windows has no overcommit, so the commit can be refused on restore and
  our restore path doesn't support OOM.
  
  
  https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-discardvirtualmemory
  ```
- [`4a70ee4`](https://github.com/ghostty-org/ghostty/commit/4a70ee4718ba0967bcfd72f43adb715bf65a860d) build/libghostty-vt: fixed to the build system for programs that embed libghostty-vt and libvaxis ([#14191](https://github.com/ghostty-org/ghostty/issues/14191)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Two small patches that don't directly affect Ghostty, but do affect
  programs that embed `libghostty-vt` and `libvaxis`, or
  any other combination that also uses `uucode`.
  
  AI disclosure: these bugs were discovered/fixed by Claude, but I've
  rewritten parts of the patches and the comments.
  
  CC @rockorager
  ```
- [`5728672`](https://github.com/ghostty-org/ghostty/commit/57286723d0529dbe10890b84e05baa682f7e9d56) nix: update zon2nix to 0.7.0 ([@jcollie](https://github.com/jcollie))
  ```text
  1. Speeds up runs by ~3x for projects with a large number of
  dependencies by downloading in parallel (~55s → 16s on my workstation).
  
  2. Adds some workarounds for Zig 0.16's package management. The changes
  don't affect Ghostty itself, but do affect downstream projects that
  embed libghostty-vt and want to create Nix packages of their own.
  ```
- [`f5efbae`](https://github.com/ghostty-org/ghostty/commit/f5efbaee5f3bec4de688ba188b51f5bd5b5059a3) nix: use hardlinks ([@jcollie](https://github.com/jcollie))
  ```text
  Zig doesn't like symlinks in some situations.
  ```
- [`13a21fc`](https://github.com/ghostty-org/ghostty/commit/13a21fc047d26827ee324268de427f0862289ab6) nix: use --reflink=auto instead of --link ([@jcollie](https://github.com/jcollie))
  ```text
  Another Zig build system quirk worked around.
  ```
- [`f6cb831`](https://github.com/ghostty-org/ghostty/commit/f6cb8312b38088e4038296ecc5dde3f23c83fd94) tinyio: implement a Windows version and use it in the C API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Implements TinyIO for Windows which is used to save binary and runtime
  costs. As a reminder, binary costs are saved because `std.Io` uses a
  vtable so compilers can't prune any unused functions, so you pay for the
  full cost. We can noop unused functions to save. Runtime is saved
  because there is less state to carry for unused functionality like
  concurrency primitives.
  
  The impl itself is mostly taken from Zig directly. I ran tests on
  Windows (arm64) and verified everything works as expected so far!
  
  Binary size measurements before/after:
  
    | Mode         | Io owner        | ghostty-vt.dll | vs. Threaded |
    |--------------|-----------------|---------------:|-------------:|
    | ReleaseFast  | std.Io.Threaded |      2,209,280 |              |
    | ReleaseFast  | std.Io.failing  |      1,815,552 |     -393,728 |
    | ReleaseFast  | TinyIo          |      1,826,816 |     -382,464 |
    | ReleaseSmall | std.Io.Threaded |      1,541,632 |              |
    | ReleaseSmall | std.Io.failing  |      1,190,912 |     -350,720 |
    | ReleaseSmall | TinyIo          |      1,199,616 |     -342,016 |
  
  The runtime savings are relatively small, but 1KB per terminal ain't nothing:
  
    | Io owner        | Private, +100 terminals | Private, startup |
    |-----------------|------------------------:|-----------------:|
    | std.Io.Threaded |            +161,845,248 |          782,336 |
    | TinyIo          |            +161,742,848 |          729,088 |
  ```
- [`fde3449`](https://github.com/ghostty-org/ghostty/commit/fde3449b348d8e36c0d52fd39bb33ea66744b958) tinyio: implement a Windows version and use it in the C API ([#14193](https://github.com/ghostty-org/ghostty/issues/14193)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Implements TinyIO for Windows which is used to save binary and runtime
  costs. As a reminder, binary costs are saved because `std.Io` uses a
  vtable so compilers can't prune any unused functions, so you pay for the
  full cost. We can noop unused functions to save. Runtime is saved
  because there is less state to carry for unused functionality like
  concurrency primitives.
  
  The impl itself is mostly taken from Zig directly. I ran tests on
  Windows (arm64) and verified everything works as expected so far!
  
  Binary size measurements before/after:
  
    | Mode         | Io owner        | ghostty-vt.dll | vs. Threaded |
    |--------------|-----------------|---------------:|-------------:|
    | ReleaseFast  | std.Io.Threaded |      2,209,280 |              |
    | ReleaseFast  | TinyIo          |      1,826,816 |     -382,464 |
    | ReleaseSmall | std.Io.Threaded |      1,541,632 |              |
    | ReleaseSmall | TinyIo          |      1,199,616 |     -342,016 |
  
  The runtime savings are relatively small, but 1KB per terminal ain't
  nothing:
  
    | Io owner        | Private, +100 terminals | Private, startup |
    |-----------------|------------------------:|-----------------:|
    | std.Io.Threaded |            +161,845,248 |          782,336 |
    | TinyIo          |            +161,742,848 |          729,088 |
  ```
- [`8a3dbc8`](https://github.com/ghostty-org/ghostty/commit/8a3dbc8ce6f450f810e3b05be72690c103e1827b) i18n(hr): spiffy up the translation ([@neoto](https://github.com/neoto))
  ```text
  Adds some linguistic polish mentioned in [my
  review](https://github.com/ghostty-org/ghostty/pull/14019#pullrequestreview-5146552587)
  and throughout the comments.
  
  Contributes to #13766
  ```
- [`8c17235`](https://github.com/ghostty-org/ghostty/commit/8c17235f8d1447ae3b5109d1c3a7d1256a9b2de4) Update VOUCHED list ([#14195](https://github.com/ghostty-org/ghostty/issues/14195)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14194#issuecomment-5608205535)
  from @trag1c.
  
  Vouch: @neoto
  ```
- [`d08ebcc`](https://github.com/ghostty-org/ghostty/commit/d08ebcc867285a3c320144a6d10517b4c40d0790) Keep working on italian translation on 1.4 ([@Misairuzame](https://github.com/Misairuzame))
- [`69f42c1`](https://github.com/ghostty-org/ghostty/commit/69f42c1a30593bdeb7588c8e66586f8bb9e2ca06) Use 'riquadro' instead of 'divisione' for 'Split' ([@Misairuzame](https://github.com/Misairuzame))
- [`466439b`](https://github.com/ghostty-org/ghostty/commit/466439bdfc868da880d7abefbe698df35d05f9aa) Update VOUCHED list ([#14205](https://github.com/ghostty-org/ghostty/issues/14205)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14179#discussioncomment-18381789)
  from @jcollie.
  
  Vouch: @korikhin
  ```
- [`6d8f8b9`](https://github.com/ghostty-org/ghostty/commit/6d8f8b9aa739e84a7cbaab2880dfdb5601e1c42e) chore: make event reporting explicit ([@neoto](https://github.com/neoto))
- [`ea624f5`](https://github.com/ghostty-org/ghostty/commit/ea624f5a8cdab0ca353be76a7b5416b76fd58ce2) i18n(hr): spiffy up the translation ([#14194](https://github.com/ghostty-org/ghostty/issues/14194)) ([@trag1c](https://github.com/trag1c))
  ```text
  Adds some linguistic polish mentioned in [my
  
  review](https://github.com/ghostty-org/ghostty/pull/14019#pullrequestreview-5146552587)
  and throughout the comments.
  
  Contributes to #13766
  
  CC: @Filip7 @kristina8888
  ```
- [`44f2a44`](https://github.com/ghostty-org/ghostty/commit/44f2a44df7e8c4a0c6df3f7d872ef3d7ead88e51) i18n: update `vi` translation for 1.4 ([#13783](https://github.com/ghostty-org/ghostty/issues/13783)) ([@00-kat](https://github.com/00-kat))
- [`c0c5473`](https://github.com/ghostty-org/ghostty/commit/c0c5473daf5b0ebc78ce0c8d1854f6221574ab3c) build: refactoring our use of translate-c ([@vancluever](https://github.com/vancluever))
  ```text
  This commit refactors our use of translate-c, in preparation for larger
  removal of cImport and better co-ordination between building of C
  dependencies and translation of headers.
  
  The major update is the creation of an internal helper package that
  wraps our use of the external translate-c library. This allows us to not
  only have better shorthand and a data-driven, declarative approach to C
  translation (versus the otherwise more imperative approach), it also
  funnels the external dependency into a single package instead of
  spreading it out among what will be an increasingly larger amount of
  places as dependencies in "pkg/" get updated.
  
  It also includes some refactors, namely to the harfbuzz package, which
  has had its individual settings refactored into helpers to allow for the
  settings to be better shared between translation and the build of the
  c-based static library.
  
  Wuffs has also had a bit of a refactor too so that we don't generate a
  file with all of the macro defines in it - we just send these in as "-D"
  flags now.
  ```
- [`d00a498`](https://github.com/ghostty-org/ghostty/commit/d00a498274f321b8808ba89d63c4e23d93a7d8e0) opengl: flip Y axis during framebuffer blit ([@pluiedev](https://github.com/pluiedev))
- [`1a8f331`](https://github.com/ghostty-org/ghostty/commit/1a8f331f16b36717f457306753352f260c2ccdb5) macOS: implement move_tab_to_new_window ([@pedronaugusto](https://github.com/pedronaugusto))
  ```text
  The action and its keybind exist, and GTK implements them, but macOS had no
  handler so the binding did nothing there. AppKit already has the command for
  window tabs, so this forwards to it.
  
  A window that isn't in a tab group, or is alone in one, is already a window of
  its own, so there is nothing to move and the action reports it did nothing.
  
  Implements the remaining macOS half of #2630.
  ```
- [`e2e53f8`](https://github.com/ghostty-org/ghostty/commit/e2e53f861482e080bf45054ba49ef471f9849937) build: refactoring our use of translate-c ([#14203](https://github.com/ghostty-org/ghostty/issues/14203)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This commit refactors our use of translate-c, in preparation for larger
  removal of `cImport` and better co-ordination between building of C
  dependencies and translation of headers.
  
  The major update is the creation of an internal helper package that
  wraps our use of the external translate-c library. This allows us to not
  only have better shorthand and a data-driven, declarative approach to C
  translation (versus the otherwise more imperative approach), it also
  funnels the external dependency into a single package instead of
  spreading it out among what will be an increasingly larger amount of
  places as dependencies in `pkg/` get updated.
  
  It also includes some refactors, namely to the harfbuzz package, which
  has had its individual settings refactored into helpers to allow for the
  settings to be better shared between translation and the build of the
  c-based static library.
  
  Wuffs has also had a bit of a refactor too so that we don't generate a
  file with all of the macro defines in it - we just send these in as `-D`
  flags now.
  ```
- [`9bbb9b2`](https://github.com/ghostty-org/ghostty/commit/9bbb9b24680358c939846b79a519ce10f7638d1f) Update VOUCHED list ([#14215](https://github.com/ghostty-org/ghostty/issues/14215)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14166#discussioncomment-18413557)
  from @jcollie.
  
  Vouch: @pedronaugusto
  ```
- [`4dac203`](https://github.com/ghostty-org/ghostty/commit/4dac203c3f6da1c3ec884e71b1cdc6a428b7a8e5) Finish italian translation for 1.4 ([@Misairuzame](https://github.com/Misairuzame))
- [`74e47a7`](https://github.com/ghostty-org/ghostty/commit/74e47a706f95f7fabaa4ea7c7a0cf25ffae21bd2) macOS: fix title bar clipping custom font ([@bo2themax](https://github.com/bo2themax))
  ```text
  The #9168 fix is no longer needed, since the frame is now higher than the actual glyph.
  ```
- [`6a64b1c`](https://github.com/ghostty-org/ghostty/commit/6a64b1c86a969bfd6e3a51f1a5c757f980657a3b) po/zh_CN: add missing translations ([@bo2themax](https://github.com/bo2themax))
- [`5252b19`](https://github.com/ghostty-org/ghostty/commit/5252b193cfd52b4bcd868135e21e4563f2f326ec) po/zh_CN: add missing translations ([#14218](https://github.com/ghostty-org/ghostty/issues/14218)) ([@pluiedev](https://github.com/pluiedev))
- [`ef7edc4`](https://github.com/ghostty-org/ghostty/commit/ef7edc4a24cf3ef0d6862276602e09f7b4b11b40) gtk/build: speed up repeated builds by letting the Zig build cache work ([@jcollie](https://github.com/jcollie))
  ```text
  Repeated builds were penalized for three reasons:
  
  1. The gresource XML embedded the absolute cache paths of the compiled
  .ui files. It now uses relative paths, resolved against a `--sourcedir`
  passed to glib-compile-resources.
  
  2. Blueprints were compiled through a small Zig wrapper, and a Run step
  hashes the bytes of the executable it runs. A Zig binary does not relink
  to the same bytes, so after a branch switch that touched the wrapper
  every .ui moved, the gresource compiler re-ran and the whole app
  recompiled for identical output. blueprint-compiler is now run directly
  and the wrapper is reduced to a single version check whose output
  nothing reads.
  
  3. The gresource pipeline was built once per artifact. It is now
  memoized on the *std.Build.
  
  Cold builds and builds after real blueprint changes are unaffected. A
  build after the wrapper relinks goes from ~43s to ~7s on my system.
  
  AI disclosure: Claude Opus 5 was used to pinpoint the source of the
  cache poisoning and to prepare a patch. Claude Fable 5.1 measured it,
  traced the remaining churn to the wrapper's relinks, and replaced a
  custom build step with stock ones. The commit message is human-written
  based on the author's understanding of the changes.
  
  Claude-Session: https://claude.ai/code/session_01RsfB3eoSTLfnKa6zi25teN
  ```
- [`09a2724`](https://github.com/ghostty-org/ghostty/commit/09a2724c23fd13f7cd24c093c568a4b6792a66a2) Update VOUCHED list ([#14223](https://github.com/ghostty-org/ghostty/issues/14223)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14221#discussioncomment-18420862)
  from @jcollie.
  
  Vouch: @helium777
  ```
- [`7aab0a0`](https://github.com/ghostty-org/ghostty/commit/7aab0a0392369613472bd5dcfd66bef58e78c3ec) macOS: implement move_tab_to_new_window ([#14216](https://github.com/ghostty-org/ghostty/issues/14216)) ([@bo2themax](https://github.com/bo2themax))
  ```text
  Closes #2630 for macOS. #13621 added the `move_tab_to_new_window` action
  and the GTK side; this does the same on macOS with AppKit.
  
  With native tabs a tab is already a window, so the action forwards to
  AppKit's own `moveTabToNewWindow:`. It's a no-op when the window is
  alone in its tab group, same as the Window menu item. The "only
  implemented on Linux" note comes off the doc comment in `Binding.zig`.
  Tested on macOS 26, from a keybind and from the command palette. I have
  no macOS 13-15 machine.
  
  Full disclosure, written with Claude Code, I directed it, read every
  line, and tested the result.
  ```
- [`55c3e8c`](https://github.com/ghostty-org/ghostty/commit/55c3e8cc0da32921aded5bda5f4de70e69bc0888) First review feedback ([@Misairuzame](https://github.com/Misairuzame))
- [`0c2a290`](https://github.com/ghostty-org/ghostty/commit/0c2a290d3a3e2a599be3a43435d778a5896667ee) Sync CODEOWNERS vouch list ([#14229](https://github.com/ghostty-org/ghostty/issues/14229)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Sync CODEOWNERS owners with vouch list.
  
  ## Added Users
  
  - @ibaios
  ```
- [`5beb94c`](https://github.com/ghostty-org/ghostty/commit/5beb94c1620e5f9e880db002d84b95f84cbf25de) renderer: apply font-thicken to IME preedit text ([@helium777](https://github.com/helium777))
  ```text
  IME preedit text was rendered with unthickened glyphs because
  addPreeditCell omitted font_thicken options when calling
  renderCodepoint, leaving them at their default false values.
  
  Fixes #13758
  ```
- [`d5eba8d`](https://github.com/ghostty-org/ghostty/commit/d5eba8d169545cc29d5ee9796ba37ff29759f4db) i18n: update `de_DE` translations ([#13846](https://github.com/ghostty-org/ghostty/issues/13846)) ([@00-kat](https://github.com/00-kat))
  ```text
  Part of #13766.
  ```
- [`45058d7`](https://github.com/ghostty-org/ghostty/commit/45058d768991e49d74dd699e012fb0610bc8ae6f) Review feedback ([@Misairuzame](https://github.com/Misairuzame))
- [`962a060`](https://github.com/ghostty-org/ghostty/commit/962a060c86ec518baaf3f54ea51337e8259803ff) macOS: fix title bar clipping custom font ([#14217](https://github.com/ghostty-org/ghostty/issues/14217)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes https://github.com/ghostty-org/ghostty/issues/14135.
  
  <img width="1398" height="652" alt="image"
  src="https://github.com/user-attachments/assets/6901a05e-9d23-4e25-89a7-c16c1694a0f9"
  />
  
  
  > The #9168 fix is no longer needed, since the frame is now higher than
  the actual glyph.
  
  The frame change observation only affects those who have a custom window
  title font set in their config. I asked Claude to run some main thread
  benchmarking compared to `main`; it will gain some delays for rapid
  title changes and window resizing. The additional cost is brought by the
  frequent frame updates which are done by AppKit. But that's necessary
  for updating the title to the correct style.
  
  > I tried to do some diffing and removing duplicates, but it will add
  too many changes too, and I didn't think it's worth doing so.
  
  The amount looks ok to me.
  
  ### `window-title-font-family = PT Mono`
  
  | Phase | Metric | base | branch | Δ | ratio |
  |---|---|---:|---:|---:|---:|
  | Idle, 3 s | main-thread CPU | 2.8 ms | 2.8 ms | -0.0 | 1.00 |
  |  | process CPU | 11.3 ms | 11.2 ms | -0.1 | 0.99 |
  | Paced title updates, 150 × 100 ms | main-thread CPU | 878.5 ms |
  **946.7 ms** | **+68.3** | **1.08** |
  |  | process CPU | 1219.9 ms | 1335.0 ms | +115.1 | 1.09 |
  |  | wall | 17.24 s | 17.34 s | +0.1 | 1.01 |
  | Title burst, 5000 back-to-back | main-thread CPU | 180.7 ms | 181.4 ms
  | +0.7 | 1.00 |
  |  | process CPU | 254.2 ms | 254.8 ms | +0.6 | 1.00 |
  |  | wall | 2.31 s | 2.32 s | +0.0 | 1.00 |
  | `toggle_maximize` × 16 (animated resize) | main-thread CPU | 1947.8 ms
  | **2178.0 ms** | **+230.2** | **1.12** |
  |  | process CPU | 4166.8 ms | 4403.2 ms | +236.4 | 1.06 |
  |  | wall | 16.68 s | 16.72 s | +0.0 | 1.00 |
  | Native fullscreen enter/exit × 2 | main-thread CPU | 196.8 ms | 195.9
  ms | -0.9 | 1.00 |
  |  | process CPU | 360.8 ms | 361.5 ms | +0.7 | 1.00 |
  |  | wall | 8.47 s | 8.47 s | +0.0 | 1.00 |
  
  ### AI Disclosure
  
  Asked Claude to generate the harness to run the benchmark and review my
  changes. I did the changes myself.
  ```
- [`1ab2501`](https://github.com/ghostty-org/ghostty/commit/1ab2501e79b7f1b204896a1009cd6566c93f4e46) gtk/build: speed up repeated builds by letting the Zig build cache work ([#14212](https://github.com/ghostty-org/ghostty/issues/14212)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Repeated builds were penalized for three reasons:
  
  1. The gresource XML embedded the absolute cache paths of the compiled
  .ui files. It now uses relative paths, resolved against a `--sourcedir`
  passed to glib-compile-resources.
  
  2. Blueprints were compiled through a small Zig wrapper, and a Run step
  hashes the bytes of the executable it runs. A Zig binary does not relink
  to the same bytes, so after a branch switch that touched the wrapper
  every .ui moved, the gresource compiler re-ran and the whole app
  recompiled for identical output. blueprint-compiler is now run directly
  and the wrapper is reduced to a single version check whose output
  nothing reads.
  
  3. The gresource pipeline was built once per artifact. It is now
  memoized on the *std.Build.
  
  Cold builds and builds after real blueprint changes are unaffected. A
  build after the wrapper relinks goes from ~43s to ~7s on my system.
  
  AI disclosure: Claude Opus 5 was used to pinpoint the source of the
  cache poisoning and to prepare a patch. Claude Fable 5.1 measured it,
  traced the remaining churn to the wrapper's relinks, and replaced a
  custom build step with stock ones. The commit message is human-written
  based on the author's understanding of the changes.
  ```
- [`d30379c`](https://github.com/ghostty-org/ghostty/commit/d30379c5b9e3dad0963a0c6881896b9b38963801) nix: update zon2nix to 0.7.0 ([#14192](https://github.com/ghostty-org/ghostty/issues/14192)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  1. Speeds up runs by ~3x for projects with a large number of
  dependencies by downloading in parallel (~55s → 16s on my workstation).
  
  2. Adds some workarounds for Zig 0.16's package management. The changes
  don't affect Ghostty itself, but do affect downstream projects that
  embed libghostty-vt and want to create Nix packages of their own.
  
  AI disclosure: Claude was used to diagnose CI failures and suggest
  fixes.
  ```
- [`49b95d8`](https://github.com/ghostty-org/ghostty/commit/49b95d846621469ebc5950fd005fa57bcc160d85) gtk,opengl: free us from the clutches of GtkGLArea ([#14052](https://github.com/ghostty-org/ghostty/issues/14052)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  GtkGLArea had numerous downsides that forced us to invent unsightly
  hacks in our renderer to work around them, most chiefly the fact that it
  holds its own GdkGLContext on the main thread (GL contexts are not at
  all thread-safe), forcing us to keep our GL calls on the main thread. It
  also does not interact well with triple-buffering and initialization is
  forced to be this sort of deferred song-and-dance since we need to wait
  for the GLArea to initialize its GL context before we can initialize the
  renderer, the core surface, and then most things in the GTK surface.
  
  We instead invent our own custom widget named RenderSurface that takes
  simple DMABUFs and displays them. The task of obtaining a GL context
  falls to manual EGL bindings, since we also need EGL to export OpenGL
  textures into DMABUFs. We keep the EGL context solely on the render
  thread meaning that the main thread never concerns itself with rendering
  except when being notified that the renderer has pushed a new frame.
  
  What makes this extra significant is that now the entire GTK apprt no
  longer depends on OpenGL in any way, shape or form. As long as it is
  being fed DMABUFs, it can render from whichever graphics API you want.
  This means we can add more backends based on OpenGL ES or more likely
  Vulkan rather painlessly in the future.
  
  **AI disclosure**: I came up with the idea and let Pi implement most of
  the nitty-gritty details around EGL, as well as replumbing the renderer
  and cleaning up all the GTK-specific workarounds there. I then carefully
  vetted every line of code and spent roughly as much time reviewing as
  coding. Most of the documentation and all commit messages are in my own
  words.
  ```
- [`b38394a`](https://github.com/ghostty-org/ghostty/commit/b38394ae3407a4c4c27102517c03384bec89a560) i18n: it_IT translations for 1.4 ([#13996](https://github.com/ghostty-org/ghostty/issues/13996)) ([@00-kat](https://github.com/00-kat))
- [`6ab34ca`](https://github.com/ghostty-org/ghostty/commit/6ab34cad2d1a91a6282c088e448256248aadda0c) gtk: remove unused blueprint using statement ([@tristan957](https://github.com/tristan957))
- [`9dc0d97`](https://github.com/ghostty-org/ghostty/commit/9dc0d974e62d4a98f55680a58fa574949f4bf134) terminal: answer ANSI DECRQM queries ([@mitchellh](https://github.com/mitchellh))
  ```text
  #14225
  
  Handle the ANSI form of DECRQM (`CSI Ps $ p`), as specified by the
  VT510 reference [1] and xterm [2]. Previously, only the DEC private
  form reached the mode query handler.
  
  [1] https://vt100.net/docs/vt510-rm/DECRQM.html
  [2] https://invisible-island.net/xterm/ctlseqs/ctlseqs.txt
  ```
- [`ec98864`](https://github.com/ghostty-org/ghostty/commit/ec98864737dbf1ccbb6c44b7f72096479b847565) gtk: remove unused blueprint using statement ([#14235](https://github.com/ghostty-org/ghostty/issues/14235)) ([@mitchellh](https://github.com/mitchellh))
- [`3beb6d7`](https://github.com/ghostty-org/ghostty/commit/3beb6d717ac305e6a3c7b152103a6f7e81d8e3cf) terminal: decrqm don't truncate 16-bit mode requests ([@mitchellh](https://github.com/mitchellh))
  ```text
  DECRQM requests can use a full 16-bit number but we truncated to 15-bits
  for the reply (cause thats all we know about). Preserve, the full
  16-bits for requests so we give the proper response.
  ```
- [`88abb77`](https://github.com/ghostty-org/ghostty/commit/88abb77b17ba0028d41d6731a1521f318d31f777) renderer: apply font-thicken to IME preedit text ([#14230](https://github.com/ghostty-org/ghostty/issues/14230)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Fixes #13758
  
  ### Problem
  
  With `font-thicken = true` on macOS, IME preedit (composing) text
  renders noticeably thinner than committed text.
  
  ### Cause & Fix
  Committed and preedit text diverge in `src/renderer/generic.zig`:
  
  ```text
  Committed: Shaper -> addGlyph -> renderGlyph(..., { .thicken = config.font_thicken, ... })
  Preedit: State -> addPreeditCell -> renderCodepoint(..., { .grid_metrics })
  ```
  
  Fix: Pass `self.config.font_thicken` and
  `self.config.font_thicken_strength` in `addPreeditCell`.
  
  ### Testing
  
  - Verified on macOS with `font-thicken = true`.
  - Verified with `zig fmt --check`.
  
  ### AI Disclosure
  
  AI (gemini-3.8-flash) assisted in tracing the call path; manually
  verified and tested.
  ````
- [`1f225eb`](https://github.com/ghostty-org/ghostty/commit/1f225ebb5894189aa9e12cf3a371f787e574c5f4) terminal: answer ANSI DECRQM queries ([#14236](https://github.com/ghostty-org/ghostty/issues/14236)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  #14225
  
  Handle the ANSI form of DECRQM (`CSI Ps $ p`), as specified by the VT510
  reference [1] and xterm [2]. Previously, only the DEC private form
  reached the mode query handler.
  
  [1] https://vt100.net/docs/vt510-rm/DECRQM.html
  [2] https://invisible-island.net/xterm/ctlseqs/ctlseqs.txt
  ```
- [`148681e`](https://github.com/ghostty-org/ghostty/commit/148681e0aab45ea84386a7839a26db3e5015cfcd) terminal: decrqm don't truncate 16-bit mode requests ([#14237](https://github.com/ghostty-org/ghostty/issues/14237)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  DECRQM requests can use a full 16-bit number but we truncated to 15-bits
  for the reply (cause thats all we know about). Preserve, the full
  16-bits for requests so we give the proper response.
  ```
- [`661e1e7`](https://github.com/ghostty-org/ghostty/commit/661e1e77f445057312666a74d9f5002e82f81764) i18n: update Lithuanian translation for v1.4 ([#13777](https://github.com/ghostty-org/ghostty/issues/13777)) ([@trag1c](https://github.com/trag1c))
  ```text
  Updates the Lithuanian translation for v1.4 and fills all 181 missing
  strings, including the command palette entries.
  
  Related to #13766.
  
  Validation:
  - Manually reviewed all translated strings
  - `msgfmt --check --check-compatibility --check-accelerators` passes
  - `msgcmp` against the translation template passes
  
  AI usage: I used Pi with OpenAI Codex (gpt-5.6-sol) to draft the
  translations and run gettext checks. I manually reviewed all
  translations before submitting.
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
- [`cc140d4`](https://github.com/ghostty-org/ghostty/commit/cc140d478a1cf42df45ac6e31d1a584b6e601adb) opengl: explicitly initialize surfaceless display ([@RadicalTray](https://github.com/RadicalTray))
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
- [`9a4ba7d`](https://github.com/ghostty-org/ghostty/commit/9a4ba7d5480ff3bfa1e1b7a6586007fe13ec05c4) tmux: test list-windows action lifetime ([@MisterTea](https://github.com/MisterTea))
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
- [`c273d6f`](https://github.com/ghostty-org/ghostty/commit/c273d6ff692f8b9ad3df595e74073d68a6341d39) Update VOUCHED list ([#14387](https://github.com/ghostty-org/ghostty/issues/14387)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14384#discussioncomment-18586072)
  from @jcollie.
  
  Vouch: @pltrz
  ```
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

