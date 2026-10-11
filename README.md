> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: October 11, 2026 at 03:34 UTC.

## October 11, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/38104361585)  
Summary: 1 runs • 2 commits • 2 authors

### Changes

- [`6603157`](https://github.com/ghostty-org/ghostty/commit/66031576b7a8dcafa6d695c0bf23f15ae81aaf26) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`24da727`](https://github.com/ghostty-org/ghostty/commit/24da727f6857b5350b4a502bdcb30ab942b36e81) Update iTerm2 colorschemes ([#14634](https://github.com/ghostty-org/ghostty/issues/14634)) ([@jcollie](https://github.com/jcollie))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20261005-151109-31756e7
  ```

## October 10, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/38089240001), [2](https://github.com/ghostty-org/ghostty/actions/runs/38083192720), [3](https://github.com/ghostty-org/ghostty/actions/runs/38081318922), [4](https://github.com/ghostty-org/ghostty/actions/runs/38080640871), [5](https://github.com/ghostty-org/ghostty/actions/runs/38050071133)  
Summary: 5 runs • 16 commits • 8 authors

### Changes

- [`9fa2e3a`](https://github.com/ghostty-org/ghostty/commit/9fa2e3aaffdc7ae30f7cc417d1ce706957ae58a0) libghostty-vt: add prompt-based viewport scrolling ([@elias8](https://github.com/elias8))
- [`e3ac620`](https://github.com/ghostty-org/ghostty/commit/e3ac62001ef2a6c9c4b4bb4231535c1c3c3e4ae3) feat(lib-vt): expose prompt navigation through the C API ([#14618](https://github.com/ghostty-org/ghostty/issues/14618)) ([@trag1c](https://github.com/trag1c))
  ```text
  Adds `GHOSTTY_SCROLL_VIEWPORT_DELTA_PROMPT` to the existing
  `ghostty_terminal_scroll_viewport` API. This allows libghostty consumers
  to navigate between shell prompts using the same native implementation
  as Ghostty's `jump_to_prompt` action.
  
  The signed `delta_prompt` count moves backward or forward from the
  viewport top, treating multiline prompt continuations as one group. This
  also fixes two boundary cases in the shared traversal: navigating
  backward through a trimmed prompt and navigating forward when the
  current prompt continues to the last retained row.
  
  AI disclosure: I used Codex to assist with the implementation.
  ```
- [`4144f6d`](https://github.com/ghostty-org/ghostty/commit/4144f6dea4dbf9586c797e535a04f1cfd381d8a7) core: demote 'adjusting page capacity' log message to debug ([@jcollie](https://github.com/jcollie))
- [`6161591`](https://github.com/ghostty-org/ghostty/commit/61615915c8f423b1497ac2a1ae68885cad353892) core: demote 'adjusting page capacity' log message to debug ([#14631](https://github.com/ghostty-org/ghostty/issues/14631)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This can really spam the logs, and isn't really useful outside of a
  developer context anyway.
  ```
- [`b10ba7e`](https://github.com/ghostty-org/ghostty/commit/b10ba7ea26502f8e637e5f698d8d001a6256d9c4) terminal: preserve grapheme data when widening wraps ([@fornwall](https://github.com/fornwall))
  ```text
  With grapheme clustering (mode 2027) enabled, a cluster can widen
  after it has been printed. Codepoints that join a cluster without
  changing its width, such as a zero-width joiner, are stored on the
  cluster's single narrow cell. A later joining codepoint can then make
  the cluster two columns wide (for example a heart, a zero-width joiner,
  then thumbs up).
  
  When that happens in the last column and auto-wrap is enabled, the
  cluster wraps to the next line and its stored codepoints have to move
  with it. Copy them before wrapping instead of looking them up on the
  row above afterwards. That row isn't the original one when the wrap
  scrolls a single-row screen or a margin region, or doesn't scroll at
  all below the scroll region. So the codepoints were dropped, taken
  from an unrelated cell, or the lookup panicked.
  ```
- [`6dae79d`](https://github.com/ghostty-org/ghostty/commit/6dae79db927110b29970a0fbe7979949c6a3ffd4) terminal: re-attach wrapped grapheme data in one allocation ([@fornwall](https://github.com/fornwall))
  ```text
  Re-attach the grapheme codepoints copied across a widening wrap with a
  single setGraphemes call instead of appending them one at a time.
  Appending probed the grapheme map and could reallocate the chunk once
  per codepoint, which cost about 10% on input where every wrap carries
  a maximal cluster.
  
  Screen.setGraphemes mirrors appendGrapheme: on a full grapheme map or
  allocator it grows the page's grapheme capacity, reloads the cell and
  retries. Add a test that wraps onto a compacted page with no grapheme
  capacity so that path is covered.
  ```
- [`b7207b2`](https://github.com/ghostty-org/ghostty/commit/b7207b2ef6aa3e05af992a6febb9ee83ad69bb8c) libghostty-vt: update program status protocol to revision 0.4 ([@mitchellh](https://github.com/mitchellh))
  ```text
  The only change in behavior is the reply to the support query. It
  used to be a bare `?`. It now also lists the states and kinds the
  terminal accepts, computed at comptime.
  
  The rest is documentation to match revisions 0.3 and 0.4.
  
  References:
  
  - Program Status Protocol (OSC 7501) specification:
    https://www.superlogical.com/rex/docs/build/program-status
  ```
- [`9cd19b4`](https://github.com/ghostty-org/ghostty/commit/9cd19b40de63f5bd172d1fcf30b667c8186d8923) libghostty-vt: update program status protocol to revision 0.4 ([#14630](https://github.com/ghostty-org/ghostty/issues/14630)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The only change in behavior is the reply to the support query. It used
  to be a bare `?`. It now also lists the states and kinds the terminal
  accepts, computed at comptime.
  
  The rest is documentation to match revisions 0.3 and 0.4.
  
  References:
  
  - Program Status Protocol (OSC 7501) specification:
  https://www.superlogical.com/rex/docs/build/program-status
  ```
- [`2551d93`](https://github.com/ghostty-org/ghostty/commit/2551d9323505043ee6f4fcd5fc6f116bbe06f1df) terminal: preserve grapheme data when widening wraps ([#14552](https://github.com/ghostty-org/ghostty/issues/14552)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  With [grapheme
  clustering](https://mitchellh.com/writing/grapheme-clusters-in-terminals#grapheme-clustering-in-terminals)
  enabled, a cluster can widen after it has been printed. Codepoints that
  join a cluster without changing its width, such as a zero-width joiner,
  are stored on the cluster's single narrow cell. A later joining
  codepoint can then make the cluster two columns wide (for example a
  heart, a zero-width joiner, then thumbs up).
  
  When that happens in the last column and auto-wrap is enabled, the
  cluster wraps to the next line and its stored codepoints have to move
  with it. Copy them before wrapping instead of looking them up on the row
  above afterwards: that row isn't the original one when the wrap scrolls
  a single-row screen or a margin region, or doesn't scroll at all below
  the scroll region.
  
  To reproduce, open a window and run the below using a safe build:
  
  ```sh
  # \033[?2027h    Enable grapheme-cluster handling (mode 2027).
  # \033[2J        Clear the visible screen.
  # \033[1;2r      Set the scrolling region to rows 1–2 and home the cursor.
  # \033[999;999H  Move to the bottom-right corner (coordinates are clamped).
  # \u2764         Print a heart, initially one cell wide.
  # \u200d         Append a zero-width joiner to the heart.
  # \U0001f44d     Append thumbs up, widening the cluster and triggering wrapping.
  # \033[r         Restore full-screen scrolling and home the cursor.
  # \033[999;1H    Move to the first column of the bottom row (below grapheme).
  # \n             Print a newline.
  printf '\033[?2027h\033[2J\033[1;2r\033[999;999H\u2764\u200d\U0001f44d\033[r\033[999;1H\n'
  ```
  
  - Before: Panics in safe builds when the cluster widens at the
  bottom-right corner below a scroll region. In release builds it unwraps
  a missing grapheme lookup, which is undefined behavior (a ReleaseFast
  test run segfaults).
  - After: it wraps with its grapheme data intact.
  
  AI disclosure: Initially created with the help of gpt-6 astra in codex.
  Iterated on, reviewed and tested by me.
  ````
- [`b804cb8`](https://github.com/ghostty-org/ghostty/commit/b804cb8fd7f48f471b741ffeaac240b61a31d694) benchmark: measure the terminal formatter with every extra ([@robmorgan](https://github.com/robmorgan))
  ```text
  The formatter benchmark only measured ScreenFormatter with no extras,
  the path clipboard copy, write_screen_file and search use. The
  libghostty-vt C API formats a whole terminal with
  ghostty_formatter_terminal_new, a TerminalFormatter whose extras
  (palette, modes, scrolling region, tabstops, cursor, style and so on)
  describe the terminal's state as well as its contents, and nothing
  measured it.
  
  --formatter=terminal formats with a TerminalFormatter and every extra,
  for every mode and region. With --mode=roundtrip both formats use it,
  so the round trip checks that the output reconstructs that state too,
  not only the contents. The default, --formatter=screen, is unchanged.
  ```
- [`1de05f1`](https://github.com/ghostty-org/ghostty/commit/1de05f1a780b279dcbfc89d93b43b850bd50e517) core: use std.Io.Dir.max_path_bytes ([@paaloeye](https://github.com/paaloeye))
  ```text
  Replace all `std.fs.max_path_bytes` with `std.Io.Dir.max_path_bytes`.
  
  `std.fs.max_path_bytes` is deprected starting from 0.16.0.
  ```
- [`10f6eb4`](https://github.com/ghostty-org/ghostty/commit/10f6eb4603a3f154f8493593da5cfeb895680cbf) cli/list-themes: don't crash when no themes match the search ([@jcollie](https://github.com/jcollie))
  ```text
  With a search that matches nothing, the filtered list is empty, and
  three keys in normal mode assumed a selected theme existed:
  
  - Enter opened the save screen, which indexes the selected theme while
    drawing.
  - G and End set the selection to `len - 1`, which underflows.
  - c and C indexed the selected theme to copy its name or path.
  
  Enter now only opens the save screen when there is a theme to save,
  G and End saturate at zero, and c and C do nothing on an empty list.
  ```
- [`c986a09`](https://github.com/ghostty-org/ghostty/commit/c986a09dc4c04d641914995e4a8ee706d9ea4e4b) cli/list-themes: don't crash when no themes match the search ([#14612](https://github.com/ghostty-org/ghostty/issues/14612)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  With a search that matches nothing, the filtered list is empty, and
  three keys in normal mode assumed a selected theme existed:
  
  - Enter opened the save screen, which indexes the selected theme while
  drawing.
  - G and End set the selection to `len - 1`, which underflows.
  - c and C indexed the selected theme to copy its name or path.
  
  Enter now only opens the save screen when there is a theme to save, G
  and End saturate at zero, and c and C do nothing on an empty list.
  
  AI disclosure: Claude Code assisted in the development of this PR.
  ```
- [`747dd53`](https://github.com/ghostty-org/ghostty/commit/747dd538d5a71bc84e980177db3b23c082ed5781) core: use std.Io.Dir.max_path_bytes ([#14611](https://github.com/ghostty-org/ghostty/issues/14611)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Replace all `std.fs.max_path_bytes` with `std.Io.Dir.max_path_bytes`.
  
  `std.fs.max_path_bytes` is deprected starting from 0.16.0.
  ```
- [`65f2b48`](https://github.com/ghostty-org/ghostty/commit/65f2b4838f1d5946aa19080bfb84732871c7b695) benchmark: measure the terminal formatter with every extra ([#14581](https://github.com/ghostty-org/ghostty/issues/14581)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The formatter benchmark only measures `ScreenFormatter` with no extras,
  the path clipboard copy, `write_screen_file` and search use. The
  libghostty-vt C API formats a whole terminal with
  `ghostty_formatter_terminal_new`, a lovely `TerminalFormatter` whose
  extras(palette, modes, scrolling region, cursor, etc.) describe the
  terminal's state as well as its contents. As far as I'm aware, nothing
  measured that path.
  
  This PR adds `--formatter=terminal` to the benchmarks, which formats
  with a `TerminalFormatter` and every extra. It works with every mode and
  region. With `--mode=roundtrip`, both formats use it, so the round trip
  also checks that the output reconstructs the terminal state, not just
  the contents. The default, `--formatter=screen`, is unchanged.
  
  ### Numbers
  
  Here is the `ghostty-bench +terminal-formatter`, ReleaseFast on my
  Macbook Pro M1 Max with a median of 60 hyperfine runs and the `noop`
  baseline subtracted:
  
  | Input | main `screen` | this PR `screen` | this PR `terminal` |
  | --- | --- | --- | --- |
  | `ghostty-gen +styled --seed=42`, 640 KB, 80×24 | 1,687 µs | 1,688 µs |
  1,718 µs |
  | Claude Code session, 120×40, alternate screen | 7.67 µs | 7.62 µs |
  16.27 µs |
  
  **Note:** The existing path is unchanged. The extras add a fixed ~8.6 µs
  per format, mostly the 256-entry palette and modes.
  
  AI disclosure: Written with help from Claude Code using Opus 5.5. I
  reviewed, tested and ran the benchmarks myself.
  ```
- [`1da3ac4`](https://github.com/ghostty-org/ghostty/commit/1da3ac43bef626ec1155c366c1960cb0f4f74d1f) Update VOUCHED list ([#14623](https://github.com/ghostty-org/ghostty/issues/14623)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14486#issuecomment-6097215618)
  from @trag1c.
  
  Denounce: @rebecca-bell-2001
  ```

## October 9, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/37960020956), [2](https://github.com/ghostty-org/ghostty/actions/runs/37902855280), [3](https://github.com/ghostty-org/ghostty/actions/runs/37884767144)  
Summary: 3 runs • 6 commits • 4 authors

### Changes

- [`7f1219f`](https://github.com/ghostty-org/ghostty/commit/7f1219fd701449fa3e5de33b9ba9ce85f008ac33) cli/list-themes: add ctrl-d/u paging ([@davidsanchez222](https://github.com/davidsanchez222))
  ```text
  Ctrl-D and Ctrl-U move down and up 20 themes, like PgDn and PgUp.
  This helps keyboards without page keys and matches the less/vi-style
  keys that already exist (g/G).
  ```
- [`246f702`](https://github.com/ghostty-org/ghostty/commit/246f702876b924a1cb7cade1e99274d1470302fc) cli/list-themes: add ctrl-d/u paging ([#14607](https://github.com/ghostty-org/ghostty/issues/14607)) ([@jcollie](https://github.com/jcollie))
  ```text
  discussion #14604
  
  ## Ctrl-D and Ctrl-U paging
  
  `Ctrl-D` and `Ctrl-U` move down and up 20 themes. `PgDn` and `PgUp`
  already do this. `g` and `G` already exist (#13376), so vim-like paging
  fits. It also helps users who have no `PgUp` or `PgDn` key.
  ```
- [`9d479dc`](https://github.com/ghostty-org/ghostty/commit/9d479dcb1664e8dc3c66c7302ce596dc56b36d6d) Update VOUCHED list ([#14614](https://github.com/ghostty-org/ghostty/issues/14614)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14582#discussioncomment-18831499)
  from @pluiedev.
  
  Denounce: @Martzcode
  ```
- [`f473f31`](https://github.com/ghostty-org/ghostty/commit/f473f310979da7002f3c2793f39cfbeef475bb88) terminal: support DECSTR ([@jcollie](https://github.com/jcollie))
  ```text
  Programs and test suites use DECSTR (CSI ! p) to undo the modes, margins,
  and pen they may have left behind without clearing the screen. It was
  ignored, so that state leaked into whatever ran next.
  ```
- [`5169c47`](https://github.com/ghostty-org/ghostty/commit/5169c473aa996a9eff29307daad6a01501c5c245) terminal: documentation for DECSTR ([@korikhin](https://github.com/korikhin))
- [`b115e45`](https://github.com/ghostty-org/ghostty/commit/b115e456749e2820a14d3942a63159ff8d46d925) terminal: support DECSTR ([#14538](https://github.com/ghostty-org/ghostty/issues/14538)) ([@jcollie](https://github.com/jcollie))
  ```text
  Programs and test suites use DECSTR (CSI ! p) to undo the modes,
  margins, and pen they may have left behind without clearing the screen.
  It was ignored, so that state leaked into whatever ran next.
  ```

## October 8, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/37856874364), [2](https://github.com/ghostty-org/ghostty/actions/runs/37844704694), [3](https://github.com/ghostty-org/ghostty/actions/runs/37805457756), [4](https://github.com/ghostty-org/ghostty/actions/runs/37794266921), [5](https://github.com/ghostty-org/ghostty/actions/runs/37790076764), [6](https://github.com/ghostty-org/ghostty/actions/runs/37789831587), [7](https://github.com/ghostty-org/ghostty/actions/runs/37742721150)  
Summary: 7 runs • 12 commits • 7 authors

### Changes

- [`54ba7b1`](https://github.com/ghostty-org/ghostty/commit/54ba7b1dd98dfaf14ee82ae7cbf435e867986da9) cli/list-themes: fix keypad page down binding ([@davidsanchez222](https://github.com/davidsanchez222))
  ```text
  The move-down-by-20 binding listed kp_down instead of kp_page_down.
  Pressing keypad down matched both this binding and the move-down-by-1
  binding, so it moved 21 themes. The move-up-by-20 binding already uses
  kp_page_up.
  ```
- [`c770410`](https://github.com/ghostty-org/ghostty/commit/c770410dbb57909ff4f6921a6497688a957f85db) cli/list-themes: fix keypad page down binding ([#14605](https://github.com/ghostty-org/ghostty/issues/14605)) ([@jcollie](https://github.com/jcollie))
  ````text
  discussion #14604
  
  ## small bug fix
  
  In the "move down 20" binding, `vaxis.Key.kp_down` should be
  `vaxis.Key.kp_page_down`. A `kp_down` press matches both `if` statements
  and moves down 21 rows. I cannot test this because I use macOS and have
  no keypad.
  
  ```zig
  // move down
  if (key.matchesAny(&.{ 'j', '+', vaxis.Key.down, vaxis.Key.kp_down, vaxis.Key.kp_add }, .{}))
      self.down(1);
  if (key.matchesAny(&.{ vaxis.Key.page_down, vaxis.Key.kp_down }, .{}))
      self.down(20);
  
  // move up (no issue, it uses kp_page_up)
  if (key.matchesAny(&.{ 'k', '-', vaxis.Key.up, vaxis.Key.kp_up, vaxis.Key.kp_subtract }, .{}))
      self.up(1);
  if (key.matchesAny(&.{ vaxis.Key.page_up, vaxis.Key.kp_page_up }, .{}))
      self.up(20);
  ```
  ````
- [`55424c1`](https://github.com/ghostty-org/ghostty/commit/55424c1ccb34bff8f5534b5bc918ea859b3a9278) i18n: use "konfiguration" consistently in Danish (da) translation ([@kgni](https://github.com/kgni))
- [`e2ced6b`](https://github.com/ghostty-org/ghostty/commit/e2ced6b710427ea69dc6795bf00a787c81554452) i18n: update Danish (da) PO-Revision-Date ([@kgni](https://github.com/kgni))
- [`ce63fcb`](https://github.com/ghostty-org/ghostty/commit/ce63fcba60abb7e11e6435fae32855c20ef3c9cf) I18n/da konfiguration ([#14594](https://github.com/ghostty-org/ghostty/issues/14594)) ([@trag1c](https://github.com/trag1c))
  ````text
  ## Summary
  
  Small follow up to #14586  based on a suggestion from @Fjodor42.
  Two strings used "konfigurering" while the rest of the file uses
  "konfiguration".
  
  ```diff
   msgid "Open Configuration in OS Editor"
  -msgstr "Åbn konfigurering i styresystemets redigeringsprogram"
  +msgstr "Åbn konfiguration i styresystemets redigeringsprogram"
  
   msgid "Open Configuration in New Window"
  -msgstr "Åbn konfigurering i nyt vindue"
  +msgstr "Åbn konfiguration i nyt vindue"
  ```
  
  Also bumped `PO-Revision-Date`.
  ````
- [`23c7a3e`](https://github.com/ghostty-org/ghostty/commit/23c7a3e5a68aefee51b30a780e706771f80b5f97) formatter: write the cursor position relative to the margins in origin mode ([@robmorgan](https://github.com/robmorgan))
  ```text
  VT output from TerminalFormatter restores origin mode (DECOM) with the
  other modes and the scrolling region after the contents, then writes
  the cursor position with CUP. In origin mode CUP counts from the
  top-left of the scrolling region, but the position was written from the
  top-left of the screen, so replaying the output put the cursor that far
  down and to the right whenever a program had set margins and origin
  mode.
  
  When the output restores both origin mode and the scrolling region,
  the cursor position (and the cell reprinted to restore a pending wrap)
  is now written relative to the region's top-left. Without either, the
  replaying terminal counts from the screen's top-left, as before.
  ```
- [`7ec9e26`](https://github.com/ghostty-org/ghostty/commit/7ec9e26a29399b30ef78f06985fc75045b3cecb6) formatter: write the cursor position relative to the margins in origin mode ([#14588](https://github.com/ghostty-org/ghostty/issues/14588)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  When a program sets a scrolling region and origin mode (DECOM), the VT
  output from `TerminalFormatter` restores the cursor to the wrong place.
  The formatter restores origin mode and the scrolling region (along with
  the other modes) after the contents, then writes the cursor position
  with CUP. In origin mode, CUP counts from the top-left of the screen, so
  the replayed cursor lands too far down (and right with DECSLRM), by the
  size of the margins.
  
  ### Reproduce
  
  Format a terminal with a scrolling region on rows 5-20, with origin mode
  on and the cursor at row 7, column 7, then play the output back and
  print an `X` at the cursor. I made an agent write a small C program with
  `ghostty_formatter_terminal_new` (modes, scrolling region, and cursor
  extras on) against libghostty-vt built from `main` and from this branch:
  
  <img width="764" height="602" alt="formatter-side-by-side"
  src="https://github.com/user-attachments/assets/787943b4-3763-4bbc-8eb8-1924600063e1"
  />
  
  
  The only difference in the output is the cursor position:
  
  ```
  main:  …row 24\e[5;20r\e[7;7H\e[0m   → row 11 in origin mode
  fixed: …row 24\e[5;20r\e[3;7H\e[0m   → row 7
  ```
  
  **The Fix:** When the output restores both origin mode and the scrolling
  region, the cursor position is now rewritten relative to the region's
  top-left. Without either, the replaying terminal counts from the
  screen's top-left, as before. Setting origin mode moves the cursor home,
  so you must write the position relative to the margins after it, and no
  mode ordering avoids this.
  
  ### Performance
  
  The fix runs once per format, not per cell. I've used the benchmark I
  contributed in https://github.com/ghostty-org/ghostty/pull/14581 to run
  `ghostty-bench +terminal-formatter` with `TerminalFormatter` and every
  extra, ReleaseFast on my MacBook Pro M1 Max, median of 60 hyperfine
  runs:
  
  | **Input** | **main** | **this PR** |
  | --- | --- | --- |
  |  80×24 screen in origin mode, 100,000 formats | 1005.4 ms | 999.4 ms |
  | ghostty-gen +styled --seed=42, 640 KB, 20 formats | 47.4 ms | 47.3 ms
  |
  
  AI disclosure: Written with help from Claude Code using Opus 5.5. I
  reviewed, tested and ran the benchmarks myself.
  ````
- [`bad5854`](https://github.com/ghostty-org/ghostty/commit/bad5854f358332f3168b35c5052f41b45a2671b3) Update VOUCHED list ([#14603](https://github.com/ghostty-org/ghostty/issues/14603)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14595#issuecomment-6062284415)
  from @mitchellh.
  
  Vouch: @Huge
  ```
- [`0f171f6`](https://github.com/ghostty-org/ghostty/commit/0f171f650a1cbbd6df4a2573b6b0c7de57cc6d90) Update VOUCHED list ([#14600](https://github.com/ghostty-org/ghostty/issues/14600)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14597#issuecomment-6061673855)
  from @pluiedev.
  
  Denounce: @riskirills66
  ```
- [`7551c5b`](https://github.com/ghostty-org/ghostty/commit/7551c5bad4211ebf3cf20647f5b735f2dc14b1f6) Update VOUCHED list ([#14599](https://github.com/ghostty-org/ghostty/issues/14599)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14598#issuecomment-6061636878)
  from @trag1c.
  
  Vouch: @Rayzerrek
  ```
- [`7b60f9b`](https://github.com/ghostty-org/ghostty/commit/7b60f9bf5f057394038f81653eaa7cc5a55bb5df) i18n: improve Danish (da) translation ([@kgni](https://github.com/kgni))
- [`8f0dd37`](https://github.com/ghostty-org/ghostty/commit/8f0dd3709050b1026f6324368805033197d8b4a5) i18n: improve Danish (da) translation ([#14586](https://github.com/ghostty-org/ghostty/issues/14586)) ([@trag1c](https://github.com/trag1c))
  ````text
  Hi!
  
  I'm a native Danish speaker and went through the Danish translation. I
  hope it's okay that I open this.
  
  My background: Got 0 errors in all of my spelling tests from 4th to 6th
  grade
  
  Happy to adjust or drop anything the da_DK maintainers disagree with.
  
  I followed the Danish GNOME translations for some of these - e.g.
  "Afslut" instead of "Luk ned"
  
  ## Summary
  
  Review pass of `po/da.po` with grammar fixes and small consistency
  changes. No new strings; still `252/252` translated.
  
  ```diff
  - Åben i Ghostty / Åben et nyt vindue. / …og åben den.
  + Åbn i Ghostty / Åbn et nyt vindue. / …og åbn den.        (imperative of "åbne", ~20 strings)
  - Kopiér det valgte tekst …
  + Kopiér den valgte tekst …                                 ("tekst" is common gender)
  - Slå sikker input til/fra
  + Slå sikkert input til/fra                                 ("input" is neuter / intetkøn)
  - Hvis ingen terminaltitel er angivet, vil dette have ingen effekt.
  + Hvis ingen terminaltitel er angivet, har dette ingen effekt.
  - Luk ned / Luk ned for Ghostty?
  + Afslut / Afslut Ghostty?                                  (matches GNOME)
  - Eksekver en kommando… / …vil blive eksekveret.
  + Kør en kommando… / …vil blive kørt.
  - Venligst gennemse fejlene nedenfor, og derefter enten genindlæs …
  + Gennemgå fejlene nedenfor, og genindlæs derefter …
  - Tjek efter opdateringer
  + Søg efter opdateringer
  - Dialog for at skifte titlen på den nuværende terminal.
  + Angiv en ny titel for den nuværende terminal.
  - Kopiér valg som HTML …
  + Kopiér markering som HTML …                               (matches "markering" elsewhere)
  ```
  
  Smaller consistency fixes:
  - `Dette medfører en nedsat ydeevne.` → `Ydeevnen vil være nedsat.`
  - `Slå vis altid øverst til/fra` → `Slå 'altid øverst' til/fra`
  - "Kopiér skærm/markering … til midlertidig fil" titles now use the same
  wording
  - Comma before "og" in all temp-file descriptions
  
  I used Claude Code to help review the initial translation; I went
  through and chose every change myself.
  ````

## October 7, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/37630750011), [2](https://github.com/ghostty-org/ghostty/actions/runs/37569761740), [3](https://github.com/ghostty-org/ghostty/actions/runs/37551559977)  
Summary: 3 runs • 4 commits • 3 authors

### Changes

- [`a60e9e2`](https://github.com/ghostty-org/ghostty/commit/a60e9e2a57f73e1eef2bd1cf2995a467f69e7fb0) Update VOUCHED list ([#14585](https://github.com/ghostty-org/ghostty/issues/14585)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14584#discussioncomment-18795569)
  from @jcollie.
  
  Vouch: @kgni
  ```
- [`c706451`](https://github.com/ghostty-org/ghostty/commit/c706451fe8bf1a55750c3262ed323df99d717a24) terminal: apply a single shift to exactly one printed character ([@robmorgan](https://github.com/robmorgan))
  ```text
  A single shift (SS2/SS3) applies to the next character received. Only
  printCell used it up, so a combining mark or VS16, which attaches to
  the previous cell without going through printCell, left the shift in
  place for the character after it.
  
  DEC STD 070 (3.8.3.2) says that if the character after a single shift
  is not a graphic character in its range, the shift is ignored and the
  character is processed as if the shift had not been received. ISO 2022
  (8.4) likewise applies it to the immediately following character
  only. print now takes the charset, and clears the single shift, once
  for each codepoint, so a combining mark or VS16 cancels the shift and
  prints unmapped. xterm does the same (WriteNow in charproc.c).
  
  printCell maps its character with that charset and writes it with the
  new writeCell, which writes a cell as it is. Spacers and blanks use
  writeCell, and so does the grapheme path that moves a character VS16
  widened to the next row. That path printed the stored, already mapped
  character through the charset again, so a '#' became a '£' if the
  British set was selected in between.
  ```
- [`b699ea7`](https://github.com/ghostty-org/ghostty/commit/b699ea79f4b881421b4b3055abc16a0957d76beb) terminal: apply a single shift to exactly one printed character ([#14576](https://github.com/ghostty-org/ghostty/issues/14576)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  With a single shift (SS2/SS3) pending, a combining mark or VS16 did not
  use it up because only `printCell` cleared the shift and those
  characters attach to the previous cell without going through it. The
  shift then applied to the next character instead. So in `x` + SS2 + VS16
  + `#` with the British set in G2, the `#` became a `£`.
  
  ### Reproduce
  
  Run these in a current build:
  ```sh
  printf 'x\e*0\eN\u0301a\e*B\n'              # combining mark: prints x́▒, should be x́a
  printf 'x\e*A\eN\uFE0F#\e*B\n'              # VS16: prints x£, should be x#
  printf '\e[%dG#\e(A\uFE0F\e(B\n' $COLUMNS   # expect a wide # at the start of the next line
  ```
  
  **Old**
  <img width="656" height="297" alt="image"
  src="https://github.com/user-attachments/assets/7a20c734-71fd-422f-8394-106e6234d538"
  />
  
  **Fixed**
  <img width="434" height="295" alt="image"
  src="https://github.com/user-attachments/assets/1401e986-3fde-479c-aa5c-e7546861ed97"
  />
  
  DEC STD 070 (3.8.3.2) says that if the character after a single shift is
  not a graphic character in its range, the shift is ignored and the
  character is processed as if the shift had not been received. ISO 2022
  (8.4) likewise applies it to the immediately following character only.
  `print` now takes the charset, and clears the single shift, once for
  each codepoint, so a combining mark or VS16 cancels the shift and prints
  unmapped. xterm does the same (WriteNow in `charproc.c`).
  
  `printCell` maps its character with that charset and writes it with the
  new `writeCell`, which writes a cell as it is. Spacers and blanks use
  `writeCell`, and so does the grapheme path that moves a character VS16
  widened to the next row. That path printed the stored, already mapped
  character through the charset again, so a '#' became a '£' if the
  British set was selected in between (e.g: before VS16).
  
  ### Performance
  I ran `ghostty-bench +terminal-stream` with hyperfine against `main`
  (ReleaseFast, M1 Max, the same 100 MB inputs for both). ASCII, styled
  and DEC line-drawing input show no change, since they go through
  `printSlice` and never reach this code. Random UTF-8, which falls back
  to `print` for most codepoints, is about 1% slower, within this
  machine's run-to-run noise.
  
  AI disclosure: Created with help from Claude Code using Opus 5.5,
  Iterated on, manually tested and reviewed by me.
  ````
- [`34f3900`](https://github.com/ghostty-org/ghostty/commit/34f39002c6e3974b54e6a6d400bd83777c5ea558) Update VOUCHED list ([#14573](https://github.com/ghostty-org/ghostty/issues/14573)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14323#discussioncomment-18786373)
  from @jcollie.
  
  Vouch: @ekusiadadus
  ```

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

