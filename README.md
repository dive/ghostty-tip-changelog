> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: October 2, 2026 at 09:16 UTC.

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

