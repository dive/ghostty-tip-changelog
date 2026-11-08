> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: November 8, 2026 at 12:38 UTC.

## November 8, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/42453768003), [2](https://github.com/ghostty-org/ghostty/actions/runs/42448097492)  
Summary: 2 runs • 8 commits • 4 authors

### Changes

- [`e356223`](https://github.com/ghostty-org/ghostty/commit/e356223d3c1a894aa9cbb479bec30988bcaebb5a) add NSColorExtension test for distance ([@francislata](https://github.com/francislata))
- [`3119f12`](https://github.com/ghostty-org/ghostty/commit/3119f12b6e4fece3a081a0374454dcfd307a75b0) update test case name ([@francislata](https://github.com/francislata))
- [`e035beb`](https://github.com/ghostty-org/ghostty/commit/e035beb9437118b803830a5864ea2f4dd7094354) Add NSColorTests for NSColor+Extension ([#15139](https://github.com/ghostty-org/ghostty/issues/15139)) ([@bo2themax](https://github.com/bo2themax))
  ```text
  # Overview
  This PR adds some tests to the `distance(to:)` extension of
  `NSColor+Extension.swift`.
  
  This increased the coverage from `0.0%` to `35.5%`.
  
  # Details
  In this PR, I only added tests to `distance(to:)` as it is the main
  function exposed within the extension.
  
  I'm adding these tests to further increase the macOS test coverage
  (#7879).
  ```
- [`b543fbe`](https://github.com/ghostty-org/ghostty/commit/b543fbed1a83da7918a7de65ad8ac733c57ceef8) terminal: add render OOM regression test ([@Uzaaft](https://github.com/Uzaaft))
- [`3e29fcd`](https://github.com/ghostty-org/ghostty/commit/3e29fcd628a50757ad24988c721340e56f392485) terminal: retry dirty rows after failed render updates ([@Uzaaft](https://github.com/Uzaaft))
- [`3a69a97`](https://github.com/ghostty-org/ghostty/commit/3a69a97b6070c1789cad760a1bd646620fe3ae01) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`e33e4cf`](https://github.com/ghostty-org/ghostty/commit/e33e4cf83006b541a73074029189e7f9a499fd99) Update iTerm2 colorschemes ([#15140](https://github.com/ghostty-org/ghostty/issues/15140)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20261102-150615-3d8a6a1
  ```
- [`59044f5`](https://github.com/ghostty-org/ghostty/commit/59044f5c5ee5764b69cc8153d307507cb1f400f5) terminal: retry dirty rows after failed render updates ([#15127](https://github.com/ghostty-org/ghostty/issues/15127)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  So tl;dr: a failed update marks unfinished work as finished
  
  Test pushed first to prove that this causes a crash before I push the
  patch a patch, that instead leaves failed rows marked as dirty, so the
  next update rebuilds them instead of using incomplete data. But I'm not
  sure of this is *sound* in a terminal.
  ```

## November 7, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/42398288749), [2](https://github.com/ghostty-org/ghostty/actions/runs/42387649303), [3](https://github.com/ghostty-org/ghostty/actions/runs/42384512829), [4](https://github.com/ghostty-org/ghostty/actions/runs/42346179212), [5](https://github.com/ghostty-org/ghostty/actions/runs/42325700870)  
Summary: 5 runs • 12 commits • 4 authors

### Changes

- [`5ed7747`](https://github.com/ghostty-org/ghostty/commit/5ed7747e8db1414ab07ec814ec2c4cd242281396) terminal: enumFromC no longer scans every enum field ([@mitchellh](https://github.com/mitchellh))
- [`1b8b3f5`](https://github.com/ghostty-org/ghostty/commit/1b8b3f55bcc93d2685f7771948516af1222dcc46) terminal: remap pins when the column growth backfill stops early ([@mitchellh](https://github.com/mitchellh))
- [`358818e`](https://github.com/ghostty-org/ghostty/commit/358818ebddb9e4d0bcfb16fb2d3f559cb7c70257) terminfo: use a multi-word description field ([@jparise](https://github.com/jparise))
  ```text
  The last field of a terminfo name line is the entry's description, and
  ours was the single word "Ghostty". ncurses' tic warns about that on
  every compile because older tic versions may treat a description with
  no spaces as another alias:
  
      "<stdin>", line 1, col 31, terminal 'xterm-ghostty': older tic
      versions may treat the description field as an alias
  
  That warning shows up in `+ssh --verbose` and in manual installs.
  
  Use "Ghostty terminal emulator", which matches the description in
  ncurses' own ghostty entry:
  
  https://github.com/ThomasDickey/ncurses-snapshots/blob/26ceb3cbd343/misc/terminfo.src#L8870
  ```
- [`0aa2292`](https://github.com/ghostty-org/ghostty/commit/0aa22921cad37022529a56e064df24a009f01500) terminal: fix dangling pins on column growth resize, faster C enum validation ([#15134](https://github.com/ghostty-org/ghostty/issues/15134)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Two fixes from the libghostty 1.0 upgrade I found in Rex:
  
  - Dangling pins when growing columns without reflow.
  - A performance regression and fix: `enumFromC` no longer scans every
  field.
  
  **AI usage: Opus for tests.**
  ```
- [`27ffca0`](https://github.com/ghostty-org/ghostty/commit/27ffca0dd67177d1f069ea7f910362e5d871613d) terminfo: use a multi-word description field ([#15135](https://github.com/ghostty-org/ghostty/issues/15135)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The last field of a terminfo name line is the entry's description, and
  ours was the single word "Ghostty". ncurses' tic warns about that on
  every compile because older tic versions may treat a description with no
  spaces as another alias:
  
      "<stdin>", line 1, col 31, terminal 'xterm-ghostty': older tic
      versions may treat the description field as an alias
  
  That warning shows up in `+ssh --verbose` and in manual installs.
  
  Use "Ghostty terminal emulator", which matches the description in
  ncurses' own ghostty entry:
  
  
  https://github.com/ThomasDickey/ncurses-snapshots/blob/26ceb3cbd343/misc/terminfo.src#L8870
  ```
- [`3c3f331`](https://github.com/ghostty-org/ghostty/commit/3c3f33121a9be2389584db716248dbf0fa0439a6) cli: run the ssh terminfo install under sh ([@jparise](https://github.com/jparise))
  ```text
  ssh passes the remote command to the user's login shell, and the
  install script assumed POSIX syntax. Under tcsh, nushell, or elvish it
  failed to parse, so the install never succeeded, the host was never
  cached, and every connection retried it and printed a parse error
  before falling back to xterm-256color.
  
  The `command -v tic` check is gone too. It only kept fish from printing
  its own unknown-command error, and fish no longer runs the script.
  
  We also no longer need explicit error codes and can instead rely on `sh
  -c` exiting with the status of the last command.
  ```
- [`8265e74`](https://github.com/ghostty-org/ghostty/commit/8265e74cd3945c56d59aba3917ff01af33ba3e78) cli: run the ssh terminfo install under sh ([#15112](https://github.com/ghostty-org/ghostty/issues/15112)) ([@jcollie](https://github.com/jcollie))
  ```text
  ssh passes the remote command to the user's login shell, and the install
  script assumed POSIX syntax. Under tcsh, nushell, or elvish it failed to
  parse, so the install never succeeded, the host was never cached, and
  every connection retried it and printed a parse error before falling
  back to xterm-256color.
  
  The `command -v tic` check is gone too. It only kept fish from printing
  its own unknown-command error, and fish no longer runs the script.
  
  We also no longer need explicit error codes and can instead rely on `sh
  -c` exiting with the status of the last command.
  ```
- [`ac5374b`](https://github.com/ghostty-org/ghostty/commit/ac5374bd16829d556f7f3636a9a19ff7f506062a) Update VOUCHED list ([#15133](https://github.com/ghostty-org/ghostty/issues/15133)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/15132#discussioncomment-19460089)
  from @bo2themax.
  
  Vouch: @Inv1x
  ```
- [`b57d75f`](https://github.com/ghostty-org/ghostty/commit/b57d75f4e2f4e017f52ce2458a91b63922dac1d9) libghostty: doxygen site works better on mobile ([@mitchellh](https://github.com/mitchellh))
  ```text
  Just brute forcing various CSS things to make the site look better on mobile.
  ```
- [`5813c94`](https://github.com/ghostty-org/ghostty/commit/5813c9461d5af78b6307a1254d00b1bc190eaccd) libghostty: doxygen site works better on mobile ([#15129](https://github.com/ghostty-org/ghostty/issues/15129)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Just brute forcing various CSS things to make the site look better on
  mobile.
  ```
- [`ea67530`](https://github.com/ghostty-org/ghostty/commit/ea675302b71a2413b16c77bb12659605bf736be2) libghostty-vt: start 1.1.0-dev, add the ABI baseline and version gate ([@mitchellh](https://github.com/mitchellh))
  ```text
  Housekeeping to move dev to 1.1.0 for libghostty. This also commits the
  ABI golden for future CI runs.
  
  This also fixes an issue where our tests didn't run properly on the 1.0
  tag, and we want it to run for the ABI golden upload.
  ```
- [`5acdbf1`](https://github.com/ghostty-org/ghostty/commit/5acdbf154369928eb228d2263cbe612d165f7569) libghostty-vt: start 1.1.0-dev, add the ABI baseline and version gate ([#15128](https://github.com/ghostty-org/ghostty/issues/15128)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Housekeeping to move dev to 1.1.0 for libghostty. This also commits the
  ABI golden for future CI runs.
  
  This also fixes an issue where our tests didn't run properly on the 1.0
  tag, and we want it to run for the ABI golden upload.
  ```

## November 6, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/42306115040), [2](https://github.com/ghostty-org/ghostty/actions/runs/42286095862), [3](https://github.com/ghostty-org/ghostty/actions/runs/42284650139), [4](https://github.com/ghostty-org/ghostty/actions/runs/42274738908), [5](https://github.com/ghostty-org/ghostty/actions/runs/42265534130), [6](https://github.com/ghostty-org/ghostty/actions/runs/42237235647), [7](https://github.com/ghostty-org/ghostty/actions/runs/42225715062), [8](https://github.com/ghostty-org/ghostty/actions/runs/42201296689), [9](https://github.com/ghostty-org/ghostty/actions/runs/42199593118), [10](https://github.com/ghostty-org/ghostty/actions/runs/42195208227), [11](https://github.com/ghostty-org/ghostty/actions/runs/42162681903)  
Summary: 11 runs • 48 commits • 9 authors

### Changes

- [`0b7f9c1`](https://github.com/ghostty-org/ghostty/commit/0b7f9c156fd9daeb4361c234884c6afc68611566) libghostty-vt: some final C ABI cleanups ([@mitchellh](https://github.com/mitchellh))
  ```text
  Changes to the C API:
  
  - `ghostty_terminal_select_output` takes `const GhosttyGridRef*` rather
    than a struct by value.
  - `GHOSTTY_TERMINAL_DATA_CURSOR_STYLE` is now
    `GHOSTTY_TERMINAL_DATA_CURSOR_SGR_STYLE` with the same value, since
    `GhosttyCursorStyle` means the cursor shape.
  - The allocator vtable functions have named typedefs so the parity test
    can compare their signatures. The ABI is the same, but the Zig side
    moves to `anyopaque` to match the header's `void*`.
  - Render state keys that have no value to report return
    `GHOSTTY_NO_VALUE` rather than `GHOSTTY_INVALID_VALUE`.
  - NULL handles and output pointers no longer crash. Functions that
    return a `GhosttyResult` return `GHOSTTY_INVALID_VALUE`. Functions that
    can't report an error do nothing, or return false, 0, or NULL. The
    headers and the conventions page now document this.
  - `GHOSTTY_TERMINAL_OPT_GLYPH_PROTOCOL` is disabled by default, and a
    NULL value disables it again. Embedders opt in.
  - `ghostty_color_x11_names` returned a garbage pointer without the color
    feature. It now returns an empty table.
  - The Windows DLL exported the two CRT section markers, 211 exports
    against the 209 in `symbols.txt`. They now have hidden visibility.
  ```
- [`e852b90`](https://github.com/ghostty-org/ghostty/commit/e852b903f439e552b9debddd684d89fea1d433b6) libghostty-vt: some final C ABI cleanups ([#15125](https://github.com/ghostty-org/ghostty/issues/15125)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Changes to the C API:
  
  - `ghostty_terminal_select_output` takes `const GhosttyGridRef*` rather
  than a struct by value.
  - `GHOSTTY_TERMINAL_DATA_CURSOR_STYLE` is now
  `GHOSTTY_TERMINAL_DATA_CURSOR_SGR_STYLE` with the same value, since
  `GhosttyCursorStyle` means the cursor shape.
  - The allocator vtable functions have named typedefs so the parity test
  can compare their signatures. The ABI is the same, but the Zig side
  moves to `anyopaque` to match the header's `void*`.
  - Render state keys that have no value to report return
  `GHOSTTY_NO_VALUE` rather than `GHOSTTY_INVALID_VALUE`.
  - NULL handles and output pointers no longer crash. Functions that
  return a `GhosttyResult` return `GHOSTTY_INVALID_VALUE`. Functions that
  can't report an error do nothing, or return false, 0, or NULL. The
  headers and the conventions page now document this.
  - `GHOSTTY_TERMINAL_OPT_GLYPH_PROTOCOL` is disabled by default, and a
  NULL value disables it again. Embedders opt in.
  - `ghostty_color_x11_names` returned a garbage pointer without the color
  feature. It now returns an empty table.
  - The Windows DLL exported the two CRT section markers, 211 exports
  against the 209 in `symbols.txt`. They now have hidden visibility.
  
  **AI usage:** Some of these found by a Fable reviewer that I ran in
  parallel to me hand-reviewing every single header and signature. I wrote
  all the docs and this PR message.
  ```
- [`a859f49`](https://github.com/ghostty-org/ghostty/commit/a859f491075226a883506434aaefb8c552ceba61) libghostty-vt: prepare for 1.0.0 ([@mitchellh](https://github.com/mitchellh))
  ```text
  This prepares libghostty-vt for its first release. The first tag will be
  `vt-1.0.0`. We're skipping 0.1.0 entirely, so it is never released and
  the docs no longer mention it or any pre-1.0 policy.
  
  This doesn't change the C API. The ABI goldens are untouched. The only
  binary differences are the version metadata below.
  ```
- [`0fa3d57`](https://github.com/ghostty-org/ghostty/commit/0fa3d577a5614150ff8e2c152de5fb9d5c6d2dec) libghostty-vt: prepare for 1.0.0 ([#15126](https://github.com/ghostty-org/ghostty/issues/15126)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This prepares libghostty-vt for its first release. The first tag will be
  `vt-1.0.0`. We're skipping 0.1.0 entirely, so it is never released and
  the docs no longer mention it or any pre-1.0 policy.
  
  This is mostly a mechanical change of changing where 0.1 is mentioned to
  1.0. I used AI assistance to help me find all the places and also to run
  a swath of verification across multiple operating systems,in parallel to
  me doing the same.
  
  This doesn't change the C API. The ABI goldens are untouched. The only
  binary differences are the version metadata below.
  ```
- [`660a0a2`](https://github.com/ghostty-org/ghostty/commit/660a0a2bb1ed76f95a549601764ba62b36881e64) libghostty: add a test to ensure terminal modes are defined ([@jcollie](https://github.com/jcollie))
  ```text
  Adds a test to make sure that all terminal modes defined in Zig have a
  corresponding definition in `ghostty/vt.h`.
  
  - add `ghostty/vt.h` aliases so that every Zig mode name has a matching
    GHOSTTY_MODE_* macro
  - move the translate-c setup out of build.zig into src/build/c_deps.zig,
    which translates `ghostty.h` and `ghostty/vt.h` once per target and
    optimize mode and imports them as the `ghostty-h` and `ghostty-vt-h`
    modules
  - generalize checkGhosttyHEnum into checkEnum, used by both it and the
    new checkGhosttyVtHMacroExists; the macro check only tests that each
    macro exists, since a mode macro's value is not a plain integer
  - vendor EnumSet and EnumIndexer from the Zig 0.17.0 std library with
    an n^2 eval branch quota in EnumIndexer, since its sort falls back to
    insertion sort on short ranges and the mode table exceeds the n log n
    quota std uses
  ```
- [`9c77332`](https://github.com/ghostty-org/ghostty/commit/9c773327e23b1ef88fd6a1a8abe1323d20054e41) libghostty: translate ghostty/vt.h for the ABI tests through c_deps ([@jcollie](https://github.com/jcollie))
  ```text
  The C ABI tests translated `ghostty/vt.h` themselves in
  `GhosttyZig.initVtCTest`, so the C API test binary ended up with two
  translations of the same header. Have `c_deps` provide the one import,
  `ghostty-vt-h`, to both the mode test and the ABI tests.
  
  - only `ghostty.h` is skipped on wasm and Windows, since it includes
    `<sys/types.h>`; `ghostty/vt.h` needs only compiler-provided headers
    and now translates for every target, linking libc only if the module
    already does
  - translate for the module's own target and optimize mode by default,
    so that layout comparisons are made against the same target
  - include `link_libc` in the cache key
  - drop the wasm and Windows skip from `checkGhosttyVtHMacroExists`
  ```
- [`f80e4d5`](https://github.com/ghostty-org/ghostty/commit/f80e4d5c6bfc8f03a17af4bd1d6f0eeb211332b3) libghostty: rename the mode macros to match the Zig mode names ([@jcollie](https://github.com/jcollie))
  ```text
  Rather than carrying a second spelling of each mode macro as an alias,
  rename the GHOSTTY_MODE_* macros in `ghostty/vt/modes.h` so that each
  one matches the name of the mode in Zig, and drop the aliases. The docs
  and header comments that referred to the old names are updated to
  match.
  ```
- [`f6cb4cf`](https://github.com/ghostty-org/ghostty/commit/f6cb4cf1276c3cb1a027468ddeb1a976a822ccfa) libghostty: add a test to ensure terminal modes are defined ([#12230](https://github.com/ghostty-org/ghostty/issues/12230)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Adds a test to make sure that all terminal modes defined in Zig have a
  corresponding definition in `ghostty/vt.h`.
  
  AI disclosure: Claude Code was used to make some of the mechanical
  renames/cleanups.
  ```
- [`d03983f`](https://github.com/ghostty-org/ghostty/commit/d03983f02cbffc51b2d661facadab50dc2a209be) terminal: RefCountedSet reuses dead IDs instead of rehashing ([@mitchellh](https://github.com/mitchellh))
  ```text
  Once every ID in a `RefCountedSet` has been handed out, `add` now reuses
  the ID of a dead item (zero references) as long as at least 10% of IDs
  are dead. Previously, `add` returned `NeedsRehash` here and every caller
  responded by cloning the entire page at the same capacity just to
  compact the IDs.
  
  `ghostty-bench +terminal-stream` at 120x80, 8MiB inputs:
  
  | Input           | Scrollback | main (ms)   | set-reuse (ms) | Speedup |
  | --------------- | ---------- | ----------- | -------------- | ------- |
  | links.vt        | 0          | 87.6 ± 1.0  | 65.0 ± 0.4     | 1.35x   |
  | styled-heavy.vt | 0          | 49.2 ± 0.4  | 42.1 ± 0.2     | 1.17x   |
  | styled-mixed.vt | 0          | 87.2 ± 0.3  | 81.6 ± 1.3     | 1.07x   |
  | ascii.vt        | 0          | 9.7 ± 0.1   | 9.7 ± 0.1      | 1.01x   |
  | styled-plain.vt | 0          | 12.4 ± 0.1  | 12.3 ± 0.1     | 1.01x   |
  | osc.vt          | 0          | 157.8 ± 1.3 | 157.5 ± 0.3    | 1.00x   |
  | links.vt        | 10KB       | 38.2 ± 0.5  | 37.7 ± 0.4     | 1.01x   |
  | styled-heavy.vt | 10KB       | 29.8 ± 0.4  | 29.6 ± 0.2     | 1.01x   |
  | styled-mixed.vt | 10KB       | 64.2 ± 0.2  | 64.0 ± 0.2     | 1.00x   |
  | out.txt (2.6GB) | 0          | 4949 ± 7    | 4918 ± 6       | 1.01x   |
  | out.txt (2.6GB) | 50MB       | 5135 ± 7    | 5070 ± 7       | 1.01x   |
  
  Real programs hit this too. I recorded about 25 seconds of each of 17
  programs in a pty and replayed them through `ghostty-bench
  +terminal-stream` at 160x48 with the app's 50MB scrollback. These three
  measurably rehash on main (instructions retired for the whole replay,
  including startup):
  
  | Workload                       | Rehashes (main) | Page copies | Instructions |
  | ------------------------------ | --------------- | ----------- | ------------ |
  | `rg --hyperlink-format` + less | 6               | 12 -> 6     | -14.2%       |
  | chafa playing an animated GIF  | 148             | 150 -> 2    | -10.9%       |
  | `eza --hyperlink -R` + less    | 2               | 8 -> 6      | -3.6%        |
  ```
- [`636c1d7`](https://github.com/ghostty-org/ghostty/commit/636c1d780568db5c5fe299b7105fcf6b4c74c068) terminal: RefCountedSet only reaps dead items it may displace ([@mitchellh](https://github.com/mitchellh))
  ```text
  Only reap a dead item whose PSL is at most the held item's. The bucket
  then never ends up with a shorter PSL than it had, so every probe
  sequence through it stays intact. Otherwise the dead item is probed
  past like any other.
  ```
- [`738d8f7`](https://github.com/ghostty-org/ghostty/commit/738d8f7f5b574b2348e0ba635a0f00a0d51c35fe) terminal: RefCountedSet checks table membership, not a sentinel bucket ([@mitchellh](https://github.com/mitchellh))
- [`38f4a71`](https://github.com/ghostty-org/ghostty/commit/38f4a710e3e6a218342915bf9d29eab10281a702) terminal: RefCountedSet.releaseMultiple asserts n > 0 ([@mitchellh](https://github.com/mitchellh))
- [`31a5299`](https://github.com/ghostty-org/ghostty/commit/31a52992f12710f0382661a481fce46a966a7ea1) terminal: RefCountedSet reclaims the dead ID insert passed over ([@mitchellh](https://github.com/mitchellh))
  ```text
  When `add` reclaims a dead ID, `insert` may still reuse a smaller dead
  ID that it reaps on its probe path. The reclaimed ID then stays dead
  and out of the table, but `free_cursor` had already moved past it, so
  the next reclaims scanned the rest of the set first and only found it
  again after wrapping around.
  
  Point `free_cursor` back at it in that case so it is the next ID
  reclaimed. Harmless before, since it was found eventually, but it is
  the cheapest dead ID to reuse.
  ```
- [`aef8b7b`](https://github.com/ghostty-org/ghostty/commit/aef8b7b38d281784108f1ab1f03d6ecb9c5246d3) terminal: tighten the RefCountedSet dead ID reuse tests ([@mitchellh](https://github.com/mitchellh))
- [`5d3f653`](https://github.com/ghostty-org/ghostty/commit/5d3f653329fc62f04625f1952d88282d93df8b29) terminal: update RefCountedSet docs for dead ID reuse ([@mitchellh](https://github.com/mitchellh))
- [`4d6fb32`](https://github.com/ghostty-org/ghostty/commit/4d6fb32631d20fbd2203be0fdd5ba8109a00519b) libghostty-vt: deploy docs from GHA, move to Vercel, prep release site ([@mitchellh](https://github.com/mitchellh))
  ```text
  This sets up automation so that our libghostty-vt docs go out
  automatically and support a separate tip vs release site.  The build
  happens in GHA so we can remove the Docker builder.
  
  This also moves to Vercel, which we already used for our main web
  domain, so all our web stuff is centralized in one place. I should note
  a bias here because I am a board member of Vercel but that wasn't the
  driving reason and Ghostty has been using Vercel since years before that.
  ```
- [`8b3b025`](https://github.com/ghostty-org/ghostty/commit/8b3b025bdbbeac42fe066d2235af5ae5e6744e44) libghostty-vt: deploy docs from GHA, move to Vercel, prep release site ([#15123](https://github.com/ghostty-org/ghostty/issues/15123)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This sets up automation so that our libghostty-vt docs go out
  automatically and support a separate tip vs release site. The build
  happens in GHA so we can remove the Docker builder.
  
  This also moves to Vercel, which we already used for our main web
  domain, so all our web stuff is centralized in one place. I should note
  a bias here because I am a board member of Vercel but that wasn't the
  driving reason and Ghostty has been using Vercel since years before
  that.
  
  **AI usage:** Opus wrote all the release automation, I reviewed it and
  wrote the commit/PR/etc.
  ```
- [`b5d9c93`](https://github.com/ghostty-org/ghostty/commit/b5d9c93da1b045593a88c846ac8fed0f3835f2f3) terminal: RefCountedSet reuses dead IDs instead of rehashing ([#15121](https://github.com/ghostty-org/ghostty/issues/15121)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Once every ID in a `RefCountedSet` has been handed out, `add` now reuses
  the ID of a dead item in place.
  
  Previously it returned `NeedsRehash`, and every caller responded by
  cloning the entire page at the same capacity, copying every row, cell,
  style, grapheme and string just to free up IDs. This caused quite a lot
  of allocation and throughput churn.
  
  This has a huge impact on alt-screen apps (TUIs) in particular, because
  they don't generally ever allocate new pages and have a fixed size and
  usage pattern (usually) and constantly overwrite styles, links, etc. You
  can see below how this plays out with benchmarks.
  
  `ghostty-bench +terminal-stream` at 120x80, 8 MiB inputs:
  
  | Input | Scrollback | main (ms) | set-reuse (ms) | Speedup |
  | --------------- | ---------- | ----------- | -------------- | -------
  |
  | links.vt | 0 | 90.2 ± 0.7 | 67.3 ± 0.6 | 1.34x |
  | styled-heavy.vt | 0 | 50.7 ± 0.4 | 44.5 ± 0.3 | 1.14x |
  | styled-mixed.vt | 0 | 90.4 ± 1.2 | 83.6 ± 0.3 | 1.08x |
  | ascii.vt | 0 | 10.2 ± 0.1 | 10.2 ± 0.2 | 1.00x |
  | styled-plain.vt | 0 | 13.2 ± 0.3 | 12.9 ± 0.1 | 1.02x |
  | osc.vt | 0 | 161.6 ± 2.0 | 163.3 ± 4.6 | 0.99x |
  | links.vt | 10KB | 39.8 ± 1.1 | 39.5 ± 0.4 | 1.01x |
  | styled-heavy.vt | 10KB | 30.9 ± 0.7 | 30.5 ± 0.2 | 1.01x |
  | styled-mixed.vt | 10KB | 66.5 ± 0.5 | 66.3 ± 0.5 | 1.00x |
  
  I also wanted to know whether real programs hit this, so I recorded
  about 25 seconds of them:
  
  | Workload | Rehashes (main) | Page copies | Instructions |
  | ------------------------------ | --------------- | ----------- |
  ------------ |
  | `rg --hyperlink-format` + less | 6 | 12 -> 6 | -14.2% |
  | chafa playing an animated GIF | 148 | 150 -> 2 | -8.4% |
  | `eza --hyperlink -R` + less | 2 | 8 -> 6 | -3.1% |
  
  And then there are a bunch I tested that didn't move much (but all moved
  towards faster): nvim, helix, btop, htop, tmux.
  
  `NeedsRehash` can now only happen if the living count is wrong. Safe
  builds assert there, and release builds still fall back to the clone. In
  a future PR we can probably remove this entirely.
  
  **AI usage:** I did all the RCS changes, I had Fable adversarially
  review which did pull up a few issues that I verified, I had Opus
  implement the benchmark changes and run them. I wrote this message of
  course.
  ```
- [`3c3a887`](https://github.com/ghostty-org/ghostty/commit/3c3a8873ef0ea7843f1712a40b37c671f565f2a9) doxygen: fix the configuration and keep the build free of warnings ([@mitchellh](https://github.com/mitchellh))
- [`56919d3`](https://github.com/ghostty-org/ghostty/commit/56919d3ffd0981d52110b8d036dc3743b23ef6bb) doxygen: register every C example and rename c-vt to c-vt-osc ([@mitchellh](https://github.com/mitchellh))
- [`f21f400`](https://github.com/ghostty-org/ghostty/commit/f21f40018791bd30fe0ecfc7d104dd556226faf7) doxygen: nest the API reference and describe every topic ([@mitchellh](https://github.com/mitchellh))
- [`5acbc10`](https://github.com/ghostty-org/ghostty/commit/5acbc10ebf84ccb7a9b2d7daf1784f2b3262d74d) doxygen: move the API conventions out of the main page ([@mitchellh](https://github.com/mitchellh))
- [`6f41fba`](https://github.com/ghostty-org/ghostty/commit/6f41fbaad44e8356abfef9881d10ef0d820ecd7d) doxygen: write the Examples page and fix example names and READMEs ([@mitchellh](https://github.com/mitchellh))
- [`3a73ef5`](https://github.com/ghostty-org/ghostty/commit/3a73ef54201efa01760013c8bc6ece70075dfed7) doxygen: move the terminal guides out of the reference pages ([@mitchellh](https://github.com/mitchellh))
- [`2bc37a0`](https://github.com/ghostty-org/ghostty/commit/2bc37a0eea6a2e5da08367e62e0f2b2a2e385938) doxygen: write the main page and Getting Started ([@mitchellh](https://github.com/mitchellh))
- [`7341454`](https://github.com/ghostty-org/ghostty/commit/7341454308f2b8a564a7540ffa6de2d7cd0d6c85) doxygen: move the rendering and image guides out of the reference pages ([@mitchellh](https://github.com/mitchellh))
- [`51bff35`](https://github.com/ghostty-org/ghostty/commit/51bff35a73097f105078f9566604c265b773ee1c) doxygen: move the input, grid, selection, search and snapshot guides out of the reference pages ([@mitchellh](https://github.com/mitchellh))
- [`9a0cb21`](https://github.com/ghostty-org/ghostty/commit/9a0cb21428205711aa4982089109e919704b1aee) doxygen: give every topic page the same short intro ([@mitchellh](https://github.com/mitchellh))
- [`ba66391`](https://github.com/ghostty-org/ghostty/commit/ba66391955118c3bddee80bccb08348f0fe149d9) doxygen: wrap the markdown pages at 80 columns ([@mitchellh](https://github.com/mitchellh))
- [`d2ce23a`](https://github.com/ghostty-org/ghostty/commit/d2ce23a87c9521931851219885e1ac3ab5733fa5) doxgyen: update some docs ([@mitchellh](https://github.com/mitchellh))
- [`2f8d9e1`](https://github.com/ghostty-org/ghostty/commit/2f8d9e1f99b18c80bfebbeb1e44ca647db46dec0) doxygen: update concepts ([@mitchellh](https://github.com/mitchellh))
- [`477bfd2`](https://github.com/ghostty-org/ghostty/commit/477bfd2941c73b8eef96395ee898b0c21f069f18) libghostty-vt: rewritten Doxygen docs ([#15120](https://github.com/ghostty-org/ghostty/issues/15120)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This is a full rewrite of the libghostty docs.
  
  **AI usage:** I hand-write all the english content, I used Opus to
  handle the build scripts and CI.
  ```
- [`020a0a0`](https://github.com/ghostty-org/ghostty/commit/020a0a0998e084d457cf3d1604fb62de4647525f) terminal: find style runs with one scan in RowBuilder.scan ([@arc-source-coder](https://github.com/arc-source-coder))
  ```text
  `RowBuilder.scan` previously handled each kind of special cell separately,
  each with its own run scan. Rows with frequent style changes paid for failed
  group comparisons of plain cells and styled runs every one or two cells.
  
  Use `Mask.eqlEnd` to find both plain and styled runs. It checks the next
  cell individually before comparing whole groups. Rows with graphemes
  get a separate scan specialization, while the common version is inlined.
  
  Background color cells no longer produce style runs: their color is
  stored in the cell, and `RenderState.Cell.style` is undefined for cells
  with the default style ID. This also removes the need for `Mask.eqlExact`.
  
  `Mask.eql` now ORs the differences together and checks the masked bits
  once to avoid emulated 64-bit lane comparisons on baseline x86-64.
  
  ## Benchmarks
  
  `ghostty-bench +screen-clone` on Windows x86-64:
  
  | Input         | Size   | Mode          | main (ms)     | This PR (ms) | Speedup |
  | ------------- | ------ | ------------- | ------------- | ------------ | ------- |
  | DOOM-fire-zig | 160x50 | render-locked | 1314.9 ± 48.0 | 434.9 ± 23.6 | 3.02x   |
  | DOOM-fire-zig | 160x50 | render        | 1622.0 ± 44.2 | 743.4 ± 18.9 | 2.18x   |
  | dense_cells   | 160x50 | render-locked | 1593.7 ± 13.5 | 467.8 ± 7.5  | 3.41x   |
  | dense_cells   | 160x50 | render        | 1969.7 ± 27.4 | 858.4 ± 15.1 | 2.29x   |
  | styled-heavy  | 120x80 | render        | 245.5 ± 5.6   | 211.1 ± 4.5  | 1.16x   |
  | styled-heavy  | 120x80 | render-scroll | 361.4 ± 8.9   | 333.6 ± 9.7  | 1.08x   |
  ```
- [`d1ce0c4`](https://github.com/ghostty-org/ghostty/commit/d1ce0c46573472d6f961d8b04a03868640c4af93) terminal: fix performance regression, apply some fixes ([@mitchellh](https://github.com/mitchellh))
- [`171a4e0`](https://github.com/ghostty-org/ghostty/commit/171a4e0444959e1938084b5db803dd83c16591b6) terminal: find style runs with one scan in RowBuilder.scan ([#15111](https://github.com/ghostty-org/ghostty/issues/15111)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `RowBuilder.scan` previously handled each kind of special cell
  separately, each with its own run scan. Rows with frequent style changes
  paid for failed group comparisons of plain cells and styled runs every
  one or two cells.
  
  This finds each run with a new `Mask.eqlEnd`, which returns the index
  where the run ends and checks the next cell on its own before checking
  groups. Rows with graphemes get a separate scan specialization, while
  the common version is inlined.
  
  Background color cells no longer produce style runs: their color is
  stored in the cell, and `RenderState.Cell.style` is already undefined
  for them. This also removes the only use of `Mask.eqlExact`.
  
  `Mask.eql` now ORs the differences and checks the masked bits once,
  which avoids emulated 64-bit lane comparisons on baseline x86-64.
  
  ## Benchmarks
  
  `ghostty-bench +screen-clone` on Windows x86-64:
  
  | Input | Size | Mode | main (ms) | This PR (ms) | Speedup |
  | ------------- | ------ | ------------- | ------------- | ------------
  | ------- |
  | DOOM-fire-zig | 160x50 | render-locked | 1314.9 ± 48.0 | 434.9 ± 23.6
  | 3.02x |
  | DOOM-fire-zig | 160x50 | render | 1622.0 ± 44.2 | 743.4 ± 18.9 | 2.18x
  |
  | dense_cells | 160x50 | render-locked | 1593.7 ± 13.5 | 467.8 ± 7.5 |
  3.41x |
  | dense_cells | 160x50 | render | 1969.7 ± 27.4 | 858.4 ± 15.1 | 2.29x |
  | styled-heavy | 120x80 | render | 245.5 ± 5.6 | 211.1 ± 4.5 | 1.16x |
  | styled-heavy | 120x80 | render-scroll | 361.4 ± 8.9 | 333.6 ± 9.7 |
  1.08x |
  | medium_cells | 139x68 | render-locked | 142.2 ± 4.8 | 132.6 ± 4.4 |
  1.07x |
  | medium_cells | 139x68 | render | 149.7 ± 5.5 | 139.3 ± 3.6 | 1.07x |
  | styled-light | 120x80 | render-locked | 149.5 ± 3.8 | 140.3 ± 3.5 |
  1.07x |
  | styled-light | 120x80 | render | 158.8 ± 5.5 | 148.0 ± 4.7 | 1.07x |
  
  AI disclosure: Developed with Claude Code (Opus 5.5) and OpenCode (GPT
  6.1 Sol), including benchmarking and codegen experiments.
  ```
- [`4441aab`](https://github.com/ghostty-org/ghostty/commit/4441aabcafd673314b0667177905726680d9f8ba) terminal/kitty: evict the oldest image by transmission ([@fornwall](https://github.com/fornwall))
  ```text
  Eviction ranked images by generation, which changes whenever an
  animation shows another frame, so a playing animation outlived images
  transmitted after it. Images advanced in the same tick were also ordered
  by hash map iteration. Rank by the transmission stamp instead.
  ```
- [`de202be`](https://github.com/ghostty-org/ghostty/commit/de202be94a418b56136d8075eb4b768672ad9f18) terminal: keep triple-click selection over blank lines ([@arc-source-coder](https://github.com/arc-source-coder))
  ```text
  Dragging a triple-click selection over a blank row clears the
  selection until the pointer reaches another row with content.
  
  Fall back to the untrimmed line at the drag point, matching the
  existing behavior at the click point.
  ```
- [`1fa19fa`](https://github.com/ghostty-org/ghostty/commit/1fa19fa3e9f73e49bd231de4995a1ecfecda7afd) terminal/kitty: evict the oldest image by transmission ([#15103](https://github.com/ghostty-org/ghostty/issues/15103)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  The [Kitty graphics
  protocol](https://sw.kovidgoyal.net/kitty/graphics-protocol/) has a
  [storage
  quota](https://sw.kovidgoyal.net/kitty/graphics-protocol/#image-persistence-and-storage-quotas):
  older images are evicted to make space for newer images.
  
  Image eviction treated an
  [animation](https://sw.kovidgoyal.net/kitty/graphics-protocol/#animation)
  as new again each time it showed another frame, so a playing animation
  outlived images transmitted after it.
  
  #15094 fixed the same problem for image numbers - this PR fixes it for
  eviction.
  
  To reproduce, start with `ghostty --image-storage-limit=12` and run the
  below script:
  
  ```sh
  # Start a green animation:
  printf '\e_Ga=T,q=2,i=1,f=24,s=1,v=1,c=8,r=4;/wAA\e\\'
  printf '\e_Ga=f,q=2,i=1,f=24,s=1,v=1,z=100;AP8A\e\\'
  printf '\e_Ga=a,q=2,i=1,s=3\e\\'
  # Show a blue image:
  printf '\e_Ga=T,q=2,i=2,f=24,s=1,v=1,c=8,r=4;AAD/\e\\'
  # Let the animation advance:
  sleep 1
  # Show a yellow image, going over the quota:
  printf '\e_Ga=T,q=2,i=3,f=24,s=1,v=1,c=8,r=4;//8A\e\\'
  ```
  
  - Before this PR: the newer blue image disappears, leaving the older
  green animation.
  - After this PR: the older green animation disappears, as in Kitty
  (checked using larger images to hit kitty fixed quota).
  
  AI disclosure: Initially created using Opus 5.5 through Claude Code.
  ````
- [`53e5514`](https://github.com/ghostty-org/ghostty/commit/53e55147bbbb0157672dac0228aa7744e881f1fa) terminal: keep triple-click selection over blank lines ([#15113](https://github.com/ghostty-org/ghostty/issues/15113)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Dragging a triple-click selection over a blank row currently clears the
  selection until the pointer reaches another row with content.
  
  This falls back to selecting the untrimmed line when the drag point is
  on a blank row, matching the existing behavior at the click point.
  
  To reproduce, run `printf 'alpha beta\n\nthree four\n'`, triple-click
  `alpha`, and drag down over the blank line. The selection should extend
  through it instead of disappearing.
  
  AI disclosure: Developed with Claude Code (Opus 5.5).
  ```
- [`9b4a007`](https://github.com/ghostty-org/ghostty/commit/9b4a0076d246cdb36d589be7dd3f14a6079e7d7f) cli: explicitly install terminfo to ~/.terminfo on ssh remote host ([@database64128](https://github.com/database64128))
  ```text
  By default tic installs terminfo into /usr/share/terminfo, which can
  cause file conflicts with the system package manager.
  
  To fix that, explicitly specify the output directory we just created
  to avoid modifying /usr/share/terminfo/.
  
  For #15031
  ```
- [`6283611`](https://github.com/ghostty-org/ghostty/commit/6283611ddf8d6d4a55c323b897428bd83b6ad5cc) cli: verify xterm-ghostty resolves after ssh install ([@jparise](https://github.com/jparise))
  ```text
  Installing to ~/.terminfo doesn't guarantee the entry is usable. ncurses
  skips $HOME/.terminfo for root when built with --disable-root-environ,
  as Arch's package is. Previously, tic installed into the system terminfo
  directory as root, so that case worked by overwriting package-owned
  files. With an explicit output directory, the install would succeed but
  xterm-ghostty wouldn't resolve, and the host would be cached as set up.
  
  Check the entry with infocmp after installing. If it doesn't resolve,
  the install fails and the session falls back to xterm-256color without
  caching the host.
  
  Also drop the mkdir. tic creates its output directory itself.
  
  See #15031, #15061
  ```
- [`2c76f29`](https://github.com/ghostty-org/ghostty/commit/2c76f29972dad21d3f2cc0efde2517a6fa8fed56) cli: explicitly install terminfo to ~/.terminfo on ssh remote host ([#15061](https://github.com/ghostty-org/ghostty/issues/15061)) ([@jparise](https://github.com/jparise))
  ```text
  By default `tic` installs terminfo into `/usr/share/terminfo`, which can
  cause file conflicts with the system package manager.
  
  To fix that, explicitly specify the output directory we just created to
  avoid modifying `/usr/share/terminfo/`.
  
  For #15031
  ```
- [`16f5674`](https://github.com/ghostty-org/ghostty/commit/16f5674dc3eaeee9575d2b729255f2fe0993ece3) Update VOUCHED list ([#15107](https://github.com/ghostty-org/ghostty/issues/15107)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/15007#discussioncomment-19437535)
  from @bo2themax.
  
  Vouch: @jin-eden
  ```
- [`db663e0`](https://github.com/ghostty-org/ghostty/commit/db663e0755ef2efcc8dd4ba5c8b7f3f25b5914b0) Update VOUCHED list ([#15106](https://github.com/ghostty-org/ghostty/issues/15106)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/15064#discussioncomment-19437280)
  from @bo2themax.
  
  Vouch: @sm010422
  ```
- [`de4bc49`](https://github.com/ghostty-org/ghostty/commit/de4bc494a5d7bb5747bf8cc76b4a31bd033628e2) i18n: updated Latvian translations ([@EriksRemess](https://github.com/EriksRemess))
  ```text
  Translations for the command palette's Focus and Untitled labels, new appearance commands and descriptions.
  ```
- [`8a5d14b`](https://github.com/ghostty-org/ghostty/commit/8a5d14bd05f8eab80e00ff24a304092c549c9f9b) i18n: updated Latvian translations ([#15100](https://github.com/ghostty-org/ghostty/issues/15100)) ([@trag1c](https://github.com/trag1c))
  ```text
  Translations for the command palette's Focus and Untitled labels, new
  appearance commands and descriptions.
  ```
- [`6095e27`](https://github.com/ghostty-org/ghostty/commit/6095e277a52fb98286a4660520fa189c51a87ec9) pkg: build simdutf, highway, and wuffs with hidden visibility ([@mitchellh](https://github.com/mitchellh))
  ```text
  When we build them, these are only ever statically linked into our
  binaries. We should not be exporting their symbols ever.
  ```
- [`c445f44`](https://github.com/ghostty-org/ghostty/commit/c445f448a7b0e409e71264ca10b302305a62f696) pkg: build simdutf, highway, and wuffs with hidden visibility ([#15102](https://github.com/ghostty-org/ghostty/issues/15102)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  When we build them, these are only ever statically linked into our
  binaries. We should not be exporting their symbols ever.
  ```

## November 5, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/42129106932), [2](https://github.com/ghostty-org/ghostty/actions/runs/42114400380), [3](https://github.com/ghostty-org/ghostty/actions/runs/42102045218), [4](https://github.com/ghostty-org/ghostty/actions/runs/42091032406), [5](https://github.com/ghostty-org/ghostty/actions/runs/42085053732), [6](https://github.com/ghostty-org/ghostty/actions/runs/42069194696)  
Summary: 6 runs • 38 commits • 5 authors

### Changes

- [`1da2e16`](https://github.com/ghostty-org/ghostty/commit/1da2e165bfc677cb3bd1cc32540941a6b0f8beb6) ci: check the libghostty-vt ABI with abidiff ([@mitchellh](https://github.com/mitchellh))
- [`c757567`](https://github.com/ghostty-org/ghostty/commit/c757567e433fb51263afa2903ef67ae9f2acf9d2) ci: build a Zig dependent with the macOS SDK and test the Windows install layout ([@mitchellh](https://github.com/mitchellh))
- [`e607b9e`](https://github.com/ghostty-org/ghostty/commit/e607b9e9726d66a46f521f7a33f524b469501f9d) ci: strip symbol versions in the ABI export list ([@mitchellh](https://github.com/mitchellh))
- [`6ba2c2b`](https://github.com/ghostty-org/ghostty/commit/6ba2c2b27065e2825745bbb78e7ad5f0b68e1690) app: add window theme switching action ([@jparise](https://github.com/jparise))
  ```text
  Add an app-scoped set_window_theme action with system, light, and dark
  values so appearance can be changed from keybindings and generated
  command palette entries. Previously these controls had no shared action
  and were unavailable across application runtimes.
  
  Apply the action as a session override through NSAppearance on macOS and
  AdwStyleManager on GTK. Keep overrides across config reloads, matching
  the existing window-decoration override behavior, without persisting
  configuration.
  
  GTK now also applies window-theme on config reload, so changes take
  effect live instead of only at startup. While an override is active,
  the window-theme=ghostty runtime CSS is omitted so terminal colors don't
  stay pinned over the selected appearance.
  
  See #7221
  ```
- [`4a59fd2`](https://github.com/ghostty-org/ghostty/commit/4a59fd20afed05f3a4799c8d3d70aac4b431de01) i18n: update window theme action catalogs ([@jparise](https://github.com/jparise))
  ```text
  Regenerate the translation template and catalogs after adding command
  palette labels and descriptions for set_window_theme. Previously these
  messages were absent, preventing translators from localizing the new
  appearance commands.
  ```
- [`dce5a94`](https://github.com/ghostty-org/ghostty/commit/dce5a9464a25b946cc945ebd99c93441cd7a1e9c) app: add config value to set_window_theme ([@jparise](https://github.com/jparise))
  ```text
  An override from set_window_theme could only be replaced by another
  override. The existing system value isn't an undo because it differs
  from a configured dark, light, auto, or ghostty window-theme, so the
  only way back to the configured appearance was to restart.
  
  Add a config value that clears the override and returns to the
  configured window-theme, along with a matching command palette entry.
  On macOS this clears the appearance override. On GTK the override now
  defaults to config and syncStyleManager resolves it, so the action and
  config changes share one path.
  
  Overrides still persist across config reloads rather than being cleared
  by them. A theme change triggers a soft reload, and hard reloads also
  come from SIGUSR2 and the config errors dialog, so a reload is a poor
  way to undo an override. This also matches how font size adjustments
  and window decoration overrides behave.
  
  See #7221
  ```
- [`8b27b66`](https://github.com/ghostty-org/ghostty/commit/8b27b66f3b20f353743895be28f521eb72137c6f) gtk: follow the system for conditional themes ([@jparise](https://github.com/jparise))
  ```text
  Applying window-theme on config changes made it possible to recurse
  without bound. With window-theme=ghostty and light and dark themes whose
  backgrounds are the opposite of their slots, on a system with no color
  scheme preference, each scheme change triggers a soft reload that swaps
  the background, which selects the other scheme again. window-theme=auto
  avoids this because it already becomes system when the themes differ.
  
  Skipping setColorScheme for an unchanged scheme wouldn't help because
  libadwaita already does that and the computed scheme alternates on every
  pass. Instead, auto and ghostty now follow the system when a conditional
  theme is in use rather than deriving the scheme from a background color
  that depends on it.
  
  See #14208
  ```
- [`27eb594`](https://github.com/ghostty-org/ghostty/commit/27eb594d2aaaa6755a688a5a23f83e2b4342e196) libghostty: test ABI in CI ([#15096](https://github.com/ghostty-org/ghostty/issues/15096)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This PR adds automated ABI checking using
  [libabigail](https://sourceware.org/libabigail/) to CI. This doesn't
  actually compare anything yet because I haven't frozen the ABI, but
  soon!
  
  **AI usage:** Opus wrote the YAML and the ABI check script. I wrote the
  markdown and the idea/policy.
  ```
- [`64c83cc`](https://github.com/ghostty-org/ghostty/commit/64c83cc2e1aadde92ddea0afdc8cdc87905e3e25) libghostty-vt: freeze the callback payload structs ([@mitchellh](https://github.com/mitchellh))
- [`de2dfde`](https://github.com/ghostty-org/ghostty/commit/de2dfded37eb3dbf84e1aece3ac4062bfc542cf9) libghostty-vt: type the keys and callbacks in the type manifest ([@mitchellh](https://github.com/mitchellh))
- [`6b6d0ee`](https://github.com/ghostty-org/ghostty/commit/6b6d0eec6cdbe10c095079f93fc63a73931a09cc) libghostty-vt: type the remaining key enums in the type manifest ([@mitchellh](https://github.com/mitchellh))
- [`b54f31f`](https://github.com/ghostty-org/ghostty/commit/b54f31f825a2988841e0593c03f03e708dbb31be) libghostty-vt: document threads and output buffers ([@mitchellh](https://github.com/mitchellh))
- [`12206bf`](https://github.com/ghostty-org/ghostty/commit/12206bfb8dd18aa76f563c613b52c3cc89f182c3) libghostty-vt: remove the selection format functions ([@mitchellh](https://github.com/mitchellh))
- [`fdedeba`](https://github.com/ghostty-org/ghostty/commit/fdedebade075d8189b7a68946eddf35dfb171e6d) libghostty-vt: fail CI on ABI changes that aren't additions ([@mitchellh](https://github.com/mitchellh))
- [`bbccbb5`](https://github.com/ghostty-org/ghostty/commit/bbccbb5465d99d1b7441cd7ca1f6bee76e7c88bc) app: add window theme switching action ([#14208](https://github.com/ghostty-org/ghostty/issues/14208)) ([@jparise](https://github.com/jparise))
  ```text
  Add an app-scoped set_window_theme action with dark, light, and system
  values so appearance can be changed from keybindings and generated
  command palette entries. Previously these controls had no shared action
  and were unavailable across application runtimes.
  
  Apply the action as a session override through NSAppearance on macOS and
  AdwStyleManager on GTK. Keep overrides across config reloads, matching
  the existing window-decoration override behavior, without persisting
  configuration.
  
  See #7221
  ```
- [`66af4c7`](https://github.com/ghostty-org/ghostty/commit/66af4c7458db7e19ae7adb44aa7054879be58b6b) libghostty-vt: freeze callback payloads, type the manifest, gate more of the ABI in CI ([#15098](https://github.com/ghostty-org/ghostty/issues/15098)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  **This breaks the C ABI. This is all on purpose to stabilize the ABI to
  prep for a 1.0 stable libghostty-vt release.**
  
  This is the last planned round of breaking changes. After this, the
  headers are in their 1.0 shape and the remaining work only adds to them.
  
  Breaking changes:
  
  - The six structs the library passes to callbacks no longer start with a
  `size` field and are now frozen: `GhosttyClipboardWrite`,
  `GhosttyClipboardRead`, `GhosttyTerminalDesktopNotification`,
  `GhosttyTerminalProgressReport`, `GhosttyTerminalProgramStatus` and
  `GhosttyTerminalSemanticPrompt`. A size on a struct the library produces
  leaves the version check to the app. New data will arrive through a new
  option with a new struct. The clipboard reply structs are inputs and
  stay sized.
  - `ghostty_terminal_selection_format_buf`,
  `ghostty_terminal_selection_format_alloc` and
  `GhosttyTerminalSelectionFormatOptions` are removed. They duplicated the
  formatter. Use a `GhosttyFormatter` with
  `GHOSTTY_FORMATTER_OPT_SELECTION`, and read the active selection with
  `GHOSTTY_TERMINAL_DATA_SELECTION`.
  - Six internal `ghostty_simd_*` and `ghostty_hwy_*` symbols are no
  longer exported. No header ever declared them.
  
  Additions:
  
  - `ghostty_type_json` now gives every key of every key enum a direction
  and the type its `void *` points at, and describes every callback
  typedef with its parameters and return type. That covers 27 key enums,
  287 keys and 27 callbacks.
  - `vt.h` documents the output buffer convention and the thread model.
  - `zig build test-lib-vt-abi` compares the built library to goldens in
  `src/terminal/c/abi/`: a type manifest per target and the list of public
  functions. It fails on anything that isn't an addition. CI runs it for
  Linux, macOS and WebAssembly, which covers the targets the `abi-check`
  job can't. `zig build update-lib-vt-abi` records an intentional
  addition.
  - `search` joins the feature matrix in CI.
  
  | Struct | 64-bit | wasm32 |
  | --- | --- | --- |
  | `GhosttyClipboardWrite` | 72 → 64 | 36 → 32 |
  | `GhosttyClipboardRead` | 80 → 72 | 40 → 36 |
  | `GhosttyTerminalDesktopNotification` | 40 → 32 | 20 → 16 |
  | `GhosttyTerminalProgressReport` | 16 → 8 | 12 → 8 |
  | `GhosttyTerminalProgramStatus` | 88 → 80 | 48 → 44 |
  | `GhosttyTerminalSemanticPrompt` | 56 → 48 | 36 → 32 |
  
  **AI usage:** Fable planned, Opus did the YAML and scripting, I did the
  Zig stuff and markdown and review.
  ```
- [`44385f0`](https://github.com/ghostty-org/ghostty/commit/44385f07c33972e75087bf2343ec287a79d5ce7b) terminal/kitty: only target virtual placements from placeholders ([@fornwall](https://github.com/fornwall))
  ```text
  A Unicode placeholder naming a placement by ID matched any placement
  with that ID, so a pinned placement was drawn a second time at the
  placeholder cells. Kitty only accepts a virtual placement here.
  ```
- [`383a6f6`](https://github.com/ghostty-org/ghostty/commit/383a6f6ae344998bc637025330ffab69aed0c0fe) terminal/kitty: find the newest numbered image by transmission ([@fornwall](https://github.com/fornwall))
  ```text
  Number lookups ranked images by generation, which changes whenever an
  animation shows another frame, so a playing animation could take over
  the number from a newer image. Rank by the transmission stamp instead.
  ```
- [`8474e94`](https://github.com/ghostty-org/ghostty/commit/8474e9421ed3d5ee10bc98d5b910f1b483cb24bf) build: load only the packages libghostty-vt compiles ([@mitchellh](https://github.com/mitchellh))
- [`fd5e90e`](https://github.com/ghostty-org/ghostty/commit/fd5e90e8c5de3821a8b99558941dc790de5b817a) libghostty: publish a dependency tarball for offline builds ([@mitchellh](https://github.com/mitchellh))
- [`34afe11`](https://github.com/ghostty-org/ghostty/commit/34afe119fcf41989c9dce939894974a7551c16bb) mirror deps ([@mitchellh](https://github.com/mitchellh))
- [`5255e48`](https://github.com/ghostty-org/ghostty/commit/5255e48b6ad831800fad495ec0f2879ed8c89ef0) libghostty: publish a dependency tarball with each libghostty-vt release ([#15095](https://github.com/ghostty-org/ghostty/issues/15095)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This continues the work toward tagged libghostty-vt releases. This PR:
  
  - Library builds now only load the Zig packages the library compiles.
  Previously a `-Demit-lib-vt` build also fetched zlib, pixels,
  iterm2_themes and zigimg, which are app-only. The library dependency
  list goes from 9 packages to 5.
  - vaxis is bumped so zigimg can be lazy again (the commit vaxis pinned
  was no longer reachable upstream).
  - uucode moves to the commit vaxis pins so there is one copy.
  - Each release now publishes `libghostty-vt-X.Y.Z-deps.tar.gz` next to
  the source tarball. It contains the five packages already unpacked, so a
  packager builds with no network and no Zig fetch step:
  
  ```
  tar -xzf libghostty-vt-0.1.0.tar.gz
  tar -xzf libghostty-vt-0.1.0-deps.tar.gz
  cd libghostty-vt-0.1.0
  zig build --system ../libghostty-vt-0.1.0-deps
  ```
  
  - `zig build dist-deps -Demit-lib-vt` builds that tarball reproducibly
  and verifies its contents against the hashes in `deps/packages.json`.
  - The release workflow builds, signs and publishes the deps tarball,
  lists it in `SHA256SUMS`, and `verify-offline` now builds from the two
  release tarballs alone, which is the exact procedure the packaging guide
  documents.
  - All dependencies this touches are mirrored on
  `deps.files.ghostty.org`.
  
  **AI usage:** Opus did the build plumbing, the workflow changes and the
  dependency gating stuff. I reviewed, directed the dependency approach
  and wrote the markdown.
  ````
- [`97f422f`](https://github.com/ghostty-org/ghostty/commit/97f422fa2464c4770d1d4919d39cfb33da571b79) terminal/kitty: find the newest numbered image by transmission ([#15094](https://github.com/ghostty-org/ghostty/issues/15094)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  In the [Kitty graphics
  protocol](https://sw.kovidgoyal.net/kitty/graphics-protocol/), clients
  can refer to images by a non-unique [image
  number](https://sw.kovidgoyal.net/kitty/graphics-protocol/#requesting-image-ids-from-the-terminal),
  and commands using a number act on the newest image with that number.
  
  Image lookup treated an
  [animation](https://sw.kovidgoyal.net/kitty/graphics-protocol/#animation)
  as new again each time it showed another frame, so a playing animation
  could take over the number from an image transmitted after it.
  
  Run the below script to reproduce:
  
  ```sh
  # Start an animation using number 7:
  printf '\e_Ga=T,q=2,I=7,f=24,s=1,v=1,c=8,r=4;/wAA\e\\'
  printf '\e_Ga=f,q=2,I=7,f=24,s=1,v=1,z=100;AP8A\e\\'
  printf '\e_Ga=a,q=2,I=7,s=3\e\\'
  # Transmit (but do not display) a blue image with number 7:
  printf '\e_Ga=t,q=2,I=7,f=24,s=1,v=1;AAD/\e\\'
  # Let the animation advance:
  sleep 1
  # Display the last transmitted image with number 7:
  printf '\e_Ga=p,q=2,I=7,c=8,r=4\e\\'
  ```
  
  - Before this PR: a second green square appears, showing the animation
  again.
  - After this PR: a blue square appears next to the green one, as in
  Kitty.
  
  AI disclosure: Initially created using Opus 5.5 through Claude Code.
  ````
- [`c412a31`](https://github.com/ghostty-org/ghostty/commit/c412a31994e55e05c58c5c540dd2adf4b71f7f96) terminal/kitty: only target virtual placements from placeholders ([#15086](https://github.com/ghostty-org/ghostty/issues/15086)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  In the [Kitty graphics
  protocol](https://sw.kovidgoyal.net/kitty/graphics-protocol/), showing
  an image on screen creates a placement, which can be given a placement
  ID.
  
  A normal placement is drawn at the cursor. A virtual placement (`U=1`)
  draws nothing by itself. Instead, the image appears wherever the
  application prints [Unicode
  placeholders](https://sw.kovidgoyal.net/kitty/graphics-protocol/#unicode-placeholders),
  which are text cells that name an image and optionally a placement.
  
  A placeholder that names a placement ID matched any placement with that
  ID, not only virtual ones. [Kitty requires a virtual placement
  here](https://github.com/kovidgoyal/kitty/blob/3e4ffc10989170c9c57eacba15ba084e6d14893b/kitty/graphics.c#L1272-L1280),
  which the spec implies but does not state outright.
  
  To reproduce, run this. The first line displays a red square using a
  normal placement, and the second references that placement from Unicode
  placeholders:
  
  ```sh
  printf '\e_Gq=2,a=T,f=24,s=1,v=1,i=1,p=1,c=2,r=1;/wAA\e\\\n\n'
  printf '\e[38;5;1;58;5;1m\xf4\x8e\xbb\xae\xf4\x8e\xbb\xae\e[m\n'
  ```
  
  - Before this PR: a second red square appears two rows below the first,
  since the normal placement was successfully referenced from the Unicode
  placeholders.
  - After this PR: only the first square appears, since normal placements
  can no longer be referenced from Unicode placeholders, as in Kitty.
  
  AFAIK very unlikely to actually hit this behaviour difference in
  practice (unless deliberately targeting this), so this is more of a
  small conformance fix rather than a bug fix affecting users. But IMHO
  these small inconstencies adds up, and it would be nice if kitty
  graphics evolves into a standard stable protocol implemented identically
  in multiple terminals.
  
  AI disclosure: Initially created using Opus 5.5 through Claude Code.
  ````
- [`3eb5af7`](https://github.com/ghostty-org/ghostty/commit/3eb5af718b6ca4abf805006336c92e6d1f9a49a4) i18n: Update Dutch translations ([@mtak](https://github.com/mtak))
- [`081a587`](https://github.com/ghostty-org/ghostty/commit/081a5871ee93952a973005f10124d3105d4947cd) i18n: Update Dutch translations ([#15037](https://github.com/ghostty-org/ghostty/issues/15037)) ([@trag1c](https://github.com/trag1c))
  ```text
  Add missing Dutch translations for command palette strings.
  ```
- [`5ce2325`](https://github.com/ghostty-org/ghostty/commit/5ce2325ec623dfa192826521ca85f0dc0cf649b3) terminal: clear cursor pin garbage flag after resize ([@fornwall](https://github.com/fornwall))
  ```text
  Shrinking a screen without scrollback can erase the cursor's row, which
  marks the cursor pin as garbage. The pin moves to the active top-left but
  keeps the flag, so a Kitty image placed at the cursor copies it and is
  never drawn.
  ```
- [`76329e5`](https://github.com/ghostty-org/ghostty/commit/76329e5ad9731a74587bc6536ea308d33ad09149) terminal: clear cursor pin garbage flag after resize ([#15085](https://github.com/ghostty-org/ghostty/issues/15085)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Shrinking a screen without scrollback can erase the cursor's row, which
  marks the cursor pin as garbage.
  
  A Kitty image then placed at the cursor copies that flag and is never
  drawn. The flag is now cleared after resize. Seems to be a regression
  from #14838.
  
  To reproduce, run this and shrink the window when prompted:
  
  ```sh
  # Enter the alt screen and print an 'x' on the bottom row, so that
  # shrinking the window pushes rows off the top. Then move home; the
  # echo below leaves the cursor on row 2.
  printf '\e[?1049h\e[999;1Hx\e[H'
  echo 'Alt screen ready. Shrink the window by at least 2 rows within 5 seconds.'
  sleep 5
  # Transmit a red Kitty image, 1 cell high and 8 cells wide:
  printf '\e_Ga=T,f=24,s=1,v=1,c=8,r=1,q=2;/wAA\e\\'
  echo 'Image sent: expect a red bar to the left. Exiting in 5 seconds.'
  sleep 5
  printf '\e[?1049l'
  echo 'Back on the normal screen. Reproducer finished.'
  ```
  
  - Before this PR: no image appears.
  - After this PR: a red bar appears at the top-left.
  
  AI disclosure: Initially created using Opus 5.5 through Claude Code.
  ````
- [`e9b6108`](https://github.com/ghostty-org/ghostty/commit/e9b6108f3895543d24625630593b7987e794a48e) libghostty-vt: version the ELF exports, add GHOSTTY_DEPRECATED ([@mitchellh](https://github.com/mitchellh))
- [`18365c6`](https://github.com/ghostty-org/ghostty/commit/18365c6fefd43ec6337b0e71c83d20c62b48c494) libghostty-vt: key and mouse event accessors report NULL ([@mitchellh](https://github.com/mitchellh))
- [`5af2876`](https://github.com/ghostty-org/ghostty/commit/5af2876e9a73c9422fed52f905ec5913fa417fb7) libghostty-vt: export every symbol in every build ([@mitchellh](https://github.com/mitchellh))
- [`ad89e75`](https://github.com/ghostty-org/ghostty/commit/ad89e75cc5278da9a7594eb3d2d58687397c00a8) example: set the unshifted codepoint in c-vt-encode-key ([@mitchellh](https://github.com/mitchellh))
- [`ee5d0f6`](https://github.com/ghostty-org/ghostty/commit/ee5d0f668c8f7410bdba56fa20b379e080fba68f) libghostty-vt: version the ELF exports, one symbol set for every build ([#15091](https://github.com/ghostty-org/ghostty/issues/15091)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  **This breaks the C ABI. This is all on purpose to stabilize the ABI to
  prep for a 1.0 stable libghostty-vt release.**
  
  - Linux and FreeBSD shared libraries now export only `ghostty_*`, under
  a `GHOSTTY_VT_0` version node, via `src/terminal/c/ghostty-vt.map`.
  - `GHOSTTY_DEPRECATED(msg)` in types.h, so we can mark functions
  deprecated after 1.0 with the replacement named in the warning. Nothing
  uses it yet.
  - Headers compile under `-Wpedantic -Werror` as C11, C23 and C++17.
  - Every symbol is exported in every build. Unsupported functions now
  return `GHOSTTY_UNSUPPORTED`. Features can now be queried from build
  info APIs.
  - Key and mouse event accessors ABI changes: the remaining void setters,
  both `_set_from_terminal` functions and `ghostty_mouse_encoder_reset`
  return `GhosttyResult`; `ghostty_key_event_set_utf8` takes a
  `GhosttyString`; `ghostty_mouse_event_get_button` returns
  `GhosttyResult` with `GHOSTTY_NO_VALUE` when no button is set; and no
  accessor dereferences a NULL event any more (it was UB in ReleaseFast).
  ```
- [`657e82d`](https://github.com/ghostty-org/ghostty/commit/657e82d1a34b3d01d53b04e4c040af364786cf53) libghostty-vt: INVALID=0 key enums, one cursor style and image layer enum ([@mitchellh](https://github.com/mitchellh))
  ````text
  Every key enum used with a `*_get` or `*_set` function now starts with
  `*_INVALID = 0`, and the existing keys shift up by one. A zeroed or
  uninitialized variable is never a real key, and passing INVALID returns
  `GHOSTTY_INVALID_VALUE`. This changes the number of every option in 13
  enums, including all of `GhosttyTerminalOption`, so bindings that
  hardcode option numbers must update. Every enumerator also has an
  explicit value now, so inserting one can't silently renumber the rest.
  
  Duplicate enums for the same concept are merged into `types.h`:
  
  - `GhosttyTerminalCursorStyle` and `GhosttyRenderStateCursorVisualStyle`
    become `GhosttyCursorStyle`.
  - `GhosttyRenderStateImageLayer` and `GhosttyKittyPlacementLayer` become
    `GhosttyImageLayer`. The placement iterator's layer option is now a
    bitmask so it can select more than one layer, and 0 or NULL means no
    filter:
  
  ```c
  uint32_t mask = GHOSTTY_IMAGE_LAYER_MASK_BELOW_TEXT |
                  GHOSTTY_IMAGE_LAYER_MASK_ABOVE_TEXT;
  ghostty_kitty_graphics_placement_iterator_set(
      iterator, GHOSTTY_KITTY_GRAPHICS_PLACEMENT_ITERATOR_OPT_LAYER, &mask);
  ```
  
  A few enumerators are renamed to match their type: the `_OPTION_` keys
  become `_OPT_` like every other key enum, `GHOSTTY_SCROLL_VIEWPORT_*`
  becomes `GHOSTTY_TERMINAL_SCROLL_VIEWPORT_*`, and
  `GHOSTTY_KITTY_IMAGE_DATA_*` becomes `GHOSTTY_KITTY_GRAPHICS_IMAGE_DATA_*`.
  ````
- [`796f09a`](https://github.com/ghostty-org/ghostty/commit/796f09a6f4bb1505e3b417c6d1db16cf74a14768) libghostty-vt: consistent setter names, results, and NULL defaults ([@mitchellh](https://github.com/mitchellh))
- [`9f09a05`](https://github.com/ghostty-org/ghostty/commit/9f09a053dbf2d3f533adfd5d812f08d70978bc51) libghostty-vt: one shape for every function that fills a caller buffer ([@mitchellh](https://github.com/mitchellh))
- [`6dc6cd9`](https://github.com/ghostty-org/ghostty/commit/6dc6cd92752b905e5d466bb319181319d2f38ee8) libghostty-vt: continuation size query succeeds when nothing is pending ([@mitchellh](https://github.com/mitchellh))
- [`03bd7e7`](https://github.com/ghostty-org/ghostty/commit/03bd7e76a0ea68fb2d5856b1bc3153135ebda91b) libghostty-vt: consistent key enums, signatures, and buffer shapes ([#15089](https://github.com/ghostty-org/ghostty/issues/15089)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  **This breaks the C ABI. This is a BIG ABI breaking PR. This is all on
  purpose to stabilize the ABI to prep for a 1.0 stable libghostty-vt
  release.**
  
  This is the last batch of signature and naming changes from the ABI
  review. After this, every key enum, setter, and buffer-filling function
  in libghostty-vt follows the same rules... so we'll have less churn.
  
  The rules this PR enforces:
  
  - Every key enum starts at `_INVALID = 0` and every enumerator has an
  explicit value. A zeroed struct never names a real key.
  - Option keys use `_OPT_`. There is one `GhosttyCursorStyle` and one
  `GhosttyImageLayer`, in types.h.
  - Setters are `_set`, never `_setopt`. NULL as the value resets the
  option to its documented default.
  - Anything that can fail returns `GhosttyResult`. String outputs are
  `GhosttyString`.
  - Every function that fills a caller buffer takes `uint8_t* buf, size_t
  buf_len, size_t* out_written` and returns `GhosttyResult`:
  `OUT_OF_SPACE` with the needed size when too small, NULL with 0 as a
  size query, `SUCCESS` with 0 when there is nothing to write.
  
  What changed for callers:
  
  | Before | After |
  | --- | --- |
  | Thirteen key enums without `_INVALID = 0` | `_INVALID = 0` inserted,
  every value shifted up by one |
  | `ghostty_{key,mouse}_encoder_setopt[_from_terminal]` |
  `ghostty_{key,mouse}_encoder_set[_from_terminal]` |
  | `GHOSTTY_SEARCH_OPT_SELECT_NEXT` and `_PREV` option keys |
  `ghostty_search_select_next()` and `_prev()` |
  | `bool ghostty_osc_command_data`, title as `const char**` |
  `GhosttyResult`, title as `GhosttyString*` |
  | `void ghostty_terminal_scroll_viewport` | `GhosttyResult`,
  `INVALID_VALUE` leaves the viewport alone |
  | `ghostty_sgr_attribute_tag(GhosttySgrAttribute)` | takes `const
  GhosttySgrAttribute*`, `UNSET` for NULL |
  | `const char* ghostty_key_event_get_utf8` | returns `GhosttyString` |
  | `char* buf` in the five `*_encode` functions | `uint8_t* buf` |
  | `ghostty_{key,mouse}_encoder_encode(…, char* out_buf, size_t
  out_buf_size, size_t* out_len)` | `(…, uint8_t* buf, size_t buf_len,
  size_t* out_written)` |
  | `size_t* out_len` in `ghostty_grid_ref_graphemes` and `_hyperlink_uri`
  | `size_t* out_written` |
  | `GRAPHEMES_BUF` key takes a bare `uint32_t*` | takes
  `GhosttyCodepointBuffer {ptr, cap, len}` |
  | Kitty `IMAGE_DATA_DATA_PTR` and `_DATA_LEN` | `IMAGE_DATA_PIXELS`
  (`GhosttyString`) and `_EXPECTED_LEN` |
  | Placement iterator `LAYER` filter takes an enum | takes a `uint32_t`
  mask of `GHOSTTY_IMAGE_LAYER_MASK_*` |
  | `ghostty_terminal_paste(…, bool* out_written)` | `bool* out_pasted` |
  | Scrollback limit NULL rejected | NULL is the 10 KB default, `SIZE_MAX`
  is unlimited |
  | Scroll-viewport tags `GHOSTTY_SCROLL_VIEWPORT_*` |
  `GHOSTTY_TERMINAL_SCROLL_VIEWPORT_*` |
  ```

## November 4, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/41923292341), [2](https://github.com/ghostty-org/ghostty/actions/runs/41911262211), [3](https://github.com/ghostty-org/ghostty/actions/runs/41887613577)  
Summary: 3 runs • 32 commits • 3 authors

### Changes

- [`def58d3`](https://github.com/ghostty-org/ghostty/commit/def58d386bb1c626acd338f75ad2959b13d738b6) cli: flush plain color list output ([@12ya](https://github.com/12ya))
  ```text
  Flush stdout before returning so plain and piped color listings include all entries instead of ending mid-line
  ```
- [`02cf8a6`](https://github.com/ghostty-org/ghostty/commit/02cf8a6a2fbac49a7cf661b5eebfe57b98f21b4b) libghostty-vt: zero and freeze the structs used for callbacks ([@mitchellh](https://github.com/mitchellh))
  ```text
  **This breaks the C ABI. This is all on purpose to stabilize the ABI to
  prep for a 1.0 stable libghostty-vt release.**
  
  Make sure that all structs sent via a callback are zeroed and that their
  size is frozen. If we change structs we can introduce new callback types
  instead of changing the prior callback signatures.
  ```
- [`9e0d83c`](https://github.com/ghostty-org/ghostty/commit/9e0d83ceea1a268bbe6c8abefa584782e8e5d321) libghostty-vt: drop the size field from GridRef and Selection ([@mitchellh](https://github.com/mitchellh))
  ````text
  **This breaks the C ABI. This is all on purpose to stabilize the ABI to
  prep for a 1.0 stable libghostty-vt release.**
  
  `GhosttyGridRef` and `GhosttySelection` are now unsized/frozen structs.
  The size was never used and they're embedded types so its really a
  parent type concern.
  
  If either type ever needs to hold more, that will be a new type rather
  than a change to these. Callers now zero-initialize them instead of
  using `GHOSTTY_INIT_SIZED`:
  
  ```c
  GhosttySelection selection = {0};
  ```
  
  The header docs for both types were rewritten. They now explain where a
  grid reference comes from, how long it stays valid, that `x` and `y` are
  not screen coordinates, and how selection direction works, with a usage
  example for each. The examples drop `GHOSTTY_INIT_SIZED` for these
  types.
  ````
- [`a447ff7`](https://github.com/ghostty-org/ghostty/commit/a447ff7d86ecf6c2e52779c0768e476d15d9e914) libghostty-vt: make GhosttyStyle a frozen 16-byte struct ([@mitchellh](https://github.com/mitchellh))
- [`49fbdaf`](https://github.com/ghostty-org/ghostty/commit/49fbdafd1df45dfc7e5e8034be03f3d0b89e50a2) libghostty-vt: set formatter options by key ([@mitchellh](https://github.com/mitchellh))
- [`742fc2f`](https://github.com/ghostty-org/ghostty/commit/742fc2f2e20f2a6f1a8db43b1268db3d85161360) libghostty-vt: one sized-struct rule for every sized struct ([@mitchellh](https://github.com/mitchellh))
- [`29bf7aa`](https://github.com/ghostty-org/ghostty/commit/29bf7aa9b4d5f8f464d9eb5d1809f9433759829d) cli: flush plain color list output ([#15073](https://github.com/ghostty-org/ghostty/issues/15073)) ([@jcollie](https://github.com/jcollie))
  ```text
  Flush stdout before returning so plain and piped color listings include
  all entries instead of ending mid-line
  
  `ghostty +list-colors --plain`
  
  <img width="1615" height="419" alt="image"
  src="https://github.com/user-attachments/assets/7d25e9b7-f22f-43df-9caa-bf343f909d14"
  />
  ```
- [`86aef72`](https://github.com/ghostty-org/ghostty/commit/86aef72a2c8e67c780867de2378b2fc4d6dcd9ca) libghostty-vt: zero and freeze the structs used for callbacks ([#15074](https://github.com/ghostty-org/ghostty/issues/15074)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  **This breaks the C ABI. This is all on purpose to stabilize the ABI to
  prep for a 1.0 stable libghostty-vt release.**
  
  A minor chage. Make sure that all structs sent via a callback are zeroed
  and that their size is frozen. If we change structs we can introduce new
  callback types instead of changing the prior callback signatures.
  ```
- [`f5a1a0f`](https://github.com/ghostty-org/ghostty/commit/f5a1a0fedd8762d490bc2951dc4b63a0f1b030e0) libghostty-vt: frozen value structs and one sized-struct rule ([#15075](https://github.com/ghostty-org/ghostty/issues/15075)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  **This breaks the C ABI. This is all on purpose to stabilize the ABI to
  prep for a 1.0 stable libghostty-vt release.**
  
  This adds a bunch of helpers and unifies our handling of sized structs
  throughout the libghostty C API. Previously, we had ~20 types with sized
  structs but only actually checked 2 of them! This PR also freezes a
  couple sized structs that didn't need a size.
  
  Along the way, the formatter's three option structs are gone.
  `ghostty_formatter_terminal_new` takes no options and we now use
  `ghostty_formatter_set` and `_get` like others.
  
  Also updated docs: a new "Sized Structs" section in vt.h explains the
  rule, and every sized struct links to it.
  
  **AI usage:** I implemented the helpers and had Opus mechanically verify
  and update all our call sites.
  ```
- [`6581a59`](https://github.com/ghostty-org/ghostty/commit/6581a593c68798cdd2c2cb77b7558747c65a0987) ci: add a release workflow for libghostty-vt ([@mitchellh](https://github.com/mitchellh))
- [`1a2cf06`](https://github.com/ghostty-org/ghostty/commit/1a2cf06dd1284f84bb28d87dbc3a055e97c93f42) docs: add a packaging guide for libghostty-vt ([@mitchellh](https://github.com/mitchellh))
  ```text
  libghostty-vt is about to get its own tagged releases, and distros
  need to be able to package it from the docs alone. PACKAGING.md only
  covered the app, with a short WebAssembly section for the library.
  
  PACKAGING-LIBGHOSTTY.md is a new, self-contained guide for packaging
  the library. It has its own accuracy warning, Zig version and minisign
  key so someone reading the library tarball never needs PACKAGING.md.
  It covers the release files on release.files.ghostty.org, the offline
  build with deps/libghostty-vt.txt, the installed files, the build
  options that matter for the library (including the only two -fsys
  options it uses, simdutf and highway), the 0.x rebuild rule and
  SONAME, package naming, pkg-config and CMake use, the third-party
  manifest and licenses, a smoke test, platform tiers, and the
  WebAssembly notes moved over from PACKAGING.md.
  
  It also calls out that the archive GitHub generates for a vt- tag is
  not a source tarball. It has no LIB_VERSION file, so `zig build` in it
  builds the app, not the library.
  
  PACKAGING.md stays the app's guide. It points library packagers at
  the new file, and its Zig version section now points at
  minimum_zig_version in build.zig.zon instead of a required_zig
  constant that no longer exists (and an example of Zig 0.14.0).
  
  The library tarball ships PACKAGING-LIBGHOSTTY.md and drops
  PACKAGING.md. dist/cmake/README.md now fetches the release tarball
  instead of main and links to the new guide instead of repeating it.
  vt.h replaces its "work in progress" warnings with the actual
  stability policy and an example runtime version check.
  ```
- [`281d341`](https://github.com/ghostty-org/ghostty/commit/281d34115fc300b4be121c01487550464d0eed9f) build: don't install the man page placeholder for libghostty-vt ([@mitchellh](https://github.com/mitchellh))
- [`e95bed6`](https://github.com/ghostty-org/ghostty/commit/e95bed63330cc921f3cf2fe3d14e024396b09d43) libghostty: release workflow and packaging guide for libghostty-vt ([#15076](https://github.com/ghostty-org/ghostty/issues/15076)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds:
  
  - Release workflow for libghostty-vt via GitHub actions triggerd by a
  `vt-X.Y.Z` tag.
  - `PACKAGING-LIBGHOSTTY.md`, a packaging guide for libghostty-vt, copy
  and pasted and reworked for libghostty from PACKAGING.md
  
  **AI usage:** Opus wrote the YAML, I did the markdown.
  ```
- [`8f7fc00`](https://github.com/ghostty-org/ghostty/commit/8f7fc00c3da2ac410d73256fc34ecce81ea49344) libghostty-vt: test that the C headers match the Zig types ([@mitchellh](https://github.com/mitchellh))
  ```text
  This continues/completes the work @jcollie started.
  
  All our C headers for libghostty and our Zig extern types are maintained
  by hand. This commit adds automated tests to verify that they are always
  matching.
  
  The test translates `ghostty/vt.h` with translate-c and walks the type
  registry in `src/terminal/c/types.zig` (the same list that produces the
  `ghostty_type_json()` manifest). For every registered type it checks:
  
    - Structs and unions: size, alignment, and every field's name,
      position, offset, and size.
    - Enums: every Zig value is a C enumerator with the same number,
      every C enumerator maps back to a Zig value, and the `_MAX_VALUE`
      sentinel is present and equal to `INT_MAX`.
    - Packed types and aliases: the same integer type.
    - Opaque handles: a pointer to an incomplete C struct.
  
  A second test runs the other way and checks that every struct, union,
  enum, and opaque handle in the headers is in the registry. A new header
  type that isn't registered fails the build, so coverage stays complete
  without any manual work.
  
  This did find a couple small mismatches that were fixed:
  `GhosttyModeReportState` (u8) and `GhosttySgrUnderline` (u3). Neither
  is an ABI bug since both cross the C API as a C int but the metadata
  didn't match.
  ```
- [`942e353`](https://github.com/ghostty-org/ghostty/commit/942e353465eb80b0bdb63bfb116d95fcb0d8edbf) libghostty-vt: test that the C headers match the Zig types ([#15071](https://github.com/ghostty-org/ghostty/issues/15071)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This continues/completes the work @jcollie started.
  
  All our C headers for libghostty and our Zig extern types are maintained
  by hand. This commit adds automated tests to verify that they are always
  matching.
  
  The test translates `ghostty/vt.h` with translate-c and walks the type
  registry in `src/terminal/c/types.zig` (the same list that produces the
  `ghostty_type_json()` manifest). For every registered type it checks:
  
  - Structs and unions: size, alignment, and every field's name, position,
  offset, and size.
  - Enums: every Zig value is a C enumerator with the same number, every C
  enumerator maps back to a Zig value, and the `_MAX_VALUE` sentinel is
  present and equal to `INT_MAX`.
    - Packed types and aliases: the same integer type.
    - Opaque handles: a pointer to an incomplete C struct.
  
  A second test runs the other way and checks that every struct, union,
  enum, and opaque handle in the headers is in the registry. A new header
  type that isn't registered fails the build, so coverage stays complete
  without any manual work.
  
  This did find a couple small mismatches that were fixed:
  `GhosttyModeReportState` (u8) and `GhosttySgrUnderline` (u3). Neither is
  an ABI bug since both cross the C API as a C int but the metadata didn't
  match.
  
  **AI usage:** Fable planned, Opus written (code only), I reviewed and
  modified the code rather significantly and wrote all the english myself.
  ```
- [`1830cd2`](https://github.com/ghostty-org/ghostty/commit/1830cd2502274a2ba0a1c03341cde3e063f57019) libghostty: derive shared library version metadata from lib_version ([@mitchellh](https://github.com/mitchellh))
  ```text
  Zig already names the shared library from `lib_version` on Linux, the
  BSDs and Windows. For 0.1.0 that is libghostty-vt.so.0.1.0 with SONAME
  libghostty-vt.so.0, plus .so.0 and .so symlinks, and ghostty-vt.dll.
  
  macOS metadata didn't follow this though. The Apple ld path hardcoded the
  install name `@rpath/libghostty-vt.dylib` and compatibility version
  1.0.0, and CMake had 0.1.0 baked into every library name.
  
  All of the version metadata is now derived from `SharedVersion` in
  GhosttyLibVt.zig, which also documents the policy.
  
  For 0.1.0 a dylib gets:
  
    - install name @rpath/libghostty-vt.0.dylib
    - compatibility version 0.1.0 (0.<minor>.0 before 1.0, <major>.0.0
      after)
    - current version 0.1.0
  
  Before 1.0 there is no ABI promise. Any minor release may break the
  ABI, and packagers handle that by rebuilding dependents on a minor bump.
  That is documentation, not build logic, so the file names stay Zig's.
  
  dyld doesn't actually enforce the compatibility version. On macOS 27 a
  client linked against a 0.1.0 dylib happily loads one marked 0.2.0 and
  the other way around, even with an old deployment target.
  
  CMake now reads the version from LIB_VERSION or build.zig instead of
  hardcoding 0.1.0, and derives the real name and SONAME from it. This
  also fixes the installed CMake package config on macOS, which said
  `IMPORTED_SONAME "GHOSTTY_VT_SONAME@"` because configure_file read
  "@rpath/@" as a variable named "rpath/".
  
  CI now checks the names against lib_version instead of a literal.
  test.yml checks the SONAME and symlinks, check-apple-libghostty-vt.nu
  checks the install name and both versions, release-tip runs that check
  on the dylib it builds, and the nix shared-link test checks the library
  name the test program records.
  ```
- [`8edb49e`](https://github.com/ghostty-org/ghostty/commit/8edb49e386acbcaa2ab6141a8e5285c2a03f4f57) libghostty: version the lib-vt tarball and vt- tags from lib_version ([@mitchellh](https://github.com/mitchellh))
  ```text
  `zig build dist -Demit-lib-vt` now names the tarball after the library
  version instead of the app version, for example
  libghostty-vt-0.1.0-dev.tar.gz, and writes a LIB_VERSION file into it in
  place of VERSION. The app tarball is unchanged.
  ```
- [`184b01a`](https://github.com/ghostty-org/ghostty/commit/184b01ab32c67b6accea14aa22ce8ed2c0ed7733) libghostty: install a CMake package config and fix lib-vt packaging defaults ([@mitchellh](https://github.com/mitchellh))
- [`7b06c05`](https://github.com/ghostty-org/ghostty/commit/7b06c054155d26f789d79a6e3ee0dc4b6e76f924) libghostty: record the final install paths in the lib-vt .pc and CMake files ([@mitchellh](https://github.com/mitchellh))
  ```text
  Distros install with `DESTDIR=/stage zig build --prefix /usr`, often
  with `--prefix-lib-dir lib64`. Zig 0.17 joins DESTDIR into every install
  path it gives the build, so both .pc files said `prefix=/stage/usr`.
  They also hardcoded `libdir=${prefix}/lib` and `includedir=${prefix}/include`,
  the CMake config hardcoded lib/, include/ and bin/, and all four files
  were installed under lib/ even when the libraries went to lib64/.
  
  For that install the .pc files now start with:
  
      prefix=/usr
      includedir=${prefix}/include
      libdir=${prefix}/lib64
  
  and the .pc and CMake files are installed to lib64/pkgconfig/ and
  lib64/cmake/ghostty-vt/. The default layout is unchanged.
  ```
- [`3a1457c`](https://github.com/ghostty-org/ghostty/commit/3a1457c34e41d98cac86582c2cbb5360b3ced2ff) ci: make the lib-vt leak checks able to fail ([@mitchellh](https://github.com/mitchellh))
- [`f5dcef0`](https://github.com/ghostty-org/ghostty/commit/f5dcef0453e1dd65f080577e07c6d9163dab218f) libghostty: add a version header and ghostty_version() ([@mitchellh](https://github.com/mitchellh))
  ```text
  libghostty-vt had no way to check its version from C at compile time,
  and the only runtime answer was ghostty_build_info(), which returns a
  string that isn't null-terminated. Consumers like Neovim's
  FindGhostty.cmake and distro packaging want both.
  
  `include/ghostty/vt/version.h` is a new committed header with
  GHOSTTY_VT_VERSION_MAJOR, _MINOR, _PATCH, a GHOSTTY_VT_VERSION string
  and GHOSTTY_VT_VERSION_AT_LEAST(maj, min, pat). vt.h includes it. It
  contains only macros and includes nothing, so build systems can read it
  as plain text. It is committed rather than generated so the tarball,
  Doxygen and anyone reading the headers all see the same file.
  
  The header only carries the release number, "0.1.0", never "-dev".
  A build from a vt- tag or a LIB_VERSION tarball drops the pre-release
  part, so a header with "-dev" in it would be wrong on exactly the
  builds we release.
  
  `ghostty_version()` returns the full version of the loaded library as
  a static null-terminated string, for example "0.1.0-dev+9a018f5cc". It
  is the same text as GHOSTTY_BUILD_INFO_VERSION_STRING. There is no
  separate function for the numbers since ghostty_build_info() already
  returns them.
  
  A new test, ghostty-vt-version-h-test, runs as part of test-lib-vt and
  fails if the header's numbers disagree with the version the library is
  built with, so a release bump has to update both. It reads the header
  as text the same way CMake would.
  
  The Version docs explain the 0.x ABI policy and why a runtime check
  matters before 1.0: every 0.x release shares the libghostty-vt.0
  library name, so the system happily loads a 0.2 library for a program
  compiled against 0.1. The c-vt-build-info example now shows both a
  compile-time check and a runtime compatibility check.
  ```
- [`ac1feec`](https://github.com/ghostty-org/ghostty/commit/ac1feec8338c4ef0ae8cd596fd43130577f3edf2) libghostty: link the lib-vt dylib with Zig when Ghostty is a dependency ([@mitchellh](https://github.com/mitchellh))
  ```text
  Zig projects that depend on Ghostty and link `dep.artifact("ghostty-vt")`
  panicked at configure time on macOS with `unable to find artifact
  "ghostty-vt"`. Every shared-library `c-vt-*` example hit this. Linux
  was unaffected.
  
  On a macOS host with the SDK, `initShared` links the dylib with Apple's
  linker in a Run step and installs it with `addInstallFileWithDir`, so
  there is no Compile step for `dep.artifact` to find.
  
  When Ghostty is a dependency, the shared library is now an ordinary
  Compile step installed with `addInstallArtifact`. The dependent links
  it into its own build, so the compatibility version and Apple
  distribution load commands from the native link don't matter there.
  The install name is still `@rpath/libghostty-vt.0.dylib`.
  
  Packaging builds (`-Demit-lib-vt`) keep the native link.
  ```
- [`97a5653`](https://github.com/ghostty-org/ghostty/commit/97a5653d323a730e4816936ed62520205f1007ae) pkg/wuffs: give the tests their own module ([@mitchellh](https://github.com/mitchellh))
  ```text
  The wuffs tests embed sample images from the pixels package. They added
  those imports to the `wuffs` module itself, which is also the module
  Ghostty imports, so every build that used wuffs carried eight test
  images in its module graph. Nothing compiled them in, but anything that
  reads the graph, such as a report of which packages end up in
  libghostty-vt, counted pixels as part of the library.
  
  The tests now build from a separate module with the same root file and
  the same `wuffs_c` import, plus the images.
  ```
- [`5b500d1`](https://github.com/ghostty-org/ghostty/commit/5b500d1433b61bc612409f82d6c8e35110ede62c) libghostty: generate the lib-vt dependency list and third-party manifest ([@mitchellh](https://github.com/mitchellh))
  ```text
  Packagers building libghostty-vt offline had to fetch all 37 Ghostty
  dependencies, including GTK and font packages the library never touches,
  and had no list of the third-party code inside the library or its
  licenses.
  
  check-zig-cache.sh now also generates two files:
  
    - build.zig.zon.lib-vt.txt, the 9 packages a `-Demit-lib-vt` build
      needs, in the same format as build.zig.zon.txt.
    - build.zig.zon.lib-vt.third-party.json, every third-party project in
      that build with its version, commit, URL, license, and whether its
      code is linked into the library or only used by the build.
  
  Neither file is written by hand. gen-lib-vt-deps.sh starts from an empty
  package directory and runs `zig build lib-vt-packages --system` for each
  supported target, fetching whatever Zig reports missing until the build
  runs. That keeps packages Zig requires even though the library doesn't
  use them, and leaves out lazy packages the library never asks for.
  
  The new `lib-vt-packages` step, defined only with `-Demit-lib-vt`, finds
  what is linked by walking the library's module graph: imports, C
  sources, include directories and linked libraries. It also reads every
  package's build.zig.zon for its version. The walk caught translate_c,
  whose helper modules are imported by every translated header.
  
  Licenses can't be derived, so each build.zig.zon in this repository now
  describes the third-party code it brings in, next to its URLs:
  
      .third_party = .{
          .{ .name = "wuffs", .license = "Apache-2.0 OR MIT", .version = "0.4.0-alpha.10" },
      },
  
  Zig and zon2nix ignore unknown top-level fields, so this changes neither
  the build nor the other generated files. Generation fails with a message
  saying what to fix when a package has no entry, an entry names a removed
  package, a linked package has no version, or vendored code is linked
  without an entry.
  
  fetch-zig-cache.sh takes an optional list, so packagers can fetch only
  what the library needs:
  
      ZIG_GLOBAL_CACHE_DIR=/tmp/offline-cache \
        ./nix/build-support/fetch-zig-cache.sh build.zig.zon.lib-vt.txt
  
  It also no longer uses `zig fetch`. In Zig 0.17, `zig fetch <url>` only
  stores p/<hash>.tar.gz, which `--system` can't read, so the script was
  broken for offline builds. It now writes a throwaway package that
  depends on each URL and runs `zig build --fetch` on it, which unpacks
  every package into p/<hash>.
  
  The offline build needs a fresh global cache too. Zig 0.17 hits
  "reached unreachable code" when a lazy package is missing from the
  `--system` directory but its tarball is in the global cache.
  ```
- [`4f2139a`](https://github.com/ghostty-org/ghostty/commit/4f2139ab4d769e37bab77ea767e398782ac19021) ci: build and test libghostty-vt offline from its dependency list ([@mitchellh](https://github.com/mitchellh))
  ```text
  The new test-lib-vt-offline job fetches only build.zig.zon.lib-vt.txt
  into an empty directory, then builds libghostty-vt and runs test-lib-vt
  with `--system` pointed at it and an empty global cache. If the list is
  missing a package, the job fails instead of the build quietly finding or
  downloading it somewhere else.
  ```
- [`2eda578`](https://github.com/ghostty-org/ghostty/commit/2eda578e784d2c46fd682f5fee55d4b3206448bf) libghostty: ship simdutf's license texts and take its version from pkg/simdutf ([@mitchellh](https://github.com/mitchellh))
  ```text
  The simdutf sources vendored in pkg/simdutf/vendor are compiled into
  libghostty-vt, but the repository had no copy of simdutf's licenses, so
  neither the source tarball nor anything built from it did either. Both of
  simdutf's licenses require shipping their text. LICENSE-APACHE and
  LICENSE-MIT from simdutf v9.0.0 now sit next to the sources. simdutf can
  be used under either one, matching the "Apache-2.0 OR MIT" in the
  third-party manifest.
  
  pkg/simdutf/build.zig.zon still said 5.2.8, though the vendored
  simdutf.h says 9.0.0. It now says 9.0.0, and vendored code takes its
  version from the build.zig.zon that holds it, so the .third_party entry
  no longer repeats it. As with fetched packages, gen-lib-vt-deps.sh
  rejects an entry that sets a second version. The generated files are
  unchanged.
  ```
- [`3de7129`](https://github.com/ghostty-org/ghostty/commit/3de71293034969aaa09ad6f19ee53a9d23087403) build: move the generated dependency files into deps/ ([@mitchellh](https://github.com/mitchellh))
- [`9fc62a9`](https://github.com/ghostty-org/ghostty/commit/9fc62a98cc765f2c341d317f2ee684ebb9584237) libghostty: prepare libghostty-vt for tagged releases ([#15069](https://github.com/ghostty-org/ghostty/issues/15069)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This is the first batch of work toward tagged libghostty-vt releases.
  This PR:
  
  - Library gets its own version via `lib_version` in `build.zig`.
  - Tags are processed as `vt-X.Y.Z`, and builds read this.
  - Tarball builds are named `libghostty-vt-X.Y.Z.tar.gz`
  - Tarball contains a `LIB_VERSION` file so a plain `zig build` uses that
  (similar to our app's `VERSION` file in the tarball)
  - The shared libraries SONAME is set properly
  - The macOS dylib install name and version metadata are set properly
  - CMake derives version from `lib_version`, the version is no longer
  hardcoded
  - The install layout is now more appropriate for packages:
    * `.pc` files under `lib/pkgconfig`
    * Cmake under `lib/cmake/ghostty-vt`
  - A new `version.h` header with macros and functions to help embedders
  - Generated dependency list including licensing information packagers
  need
  - CI verification for a lot of this so it doesn't drift/fail
  
  **AI usage:** A huge mix of me and Fable going back and forth. I wrote
  all the english. There's just a lot of glue in here that is not pleasant
  and does not spark joy to write, so I used more AI assistance than
  normal for this task and will continue to for packaging.
  ```
- [`8c0c45c`](https://github.com/ghostty-org/ghostty/commit/8c0c45c18a17fe8dc270b4c80ff31053c6f52a89) libghostty-vt: return GHOSTTY_UNSUPPORTED for unknown keys ([@mitchellh](https://github.com/mitchellh))
  ````text
  **This breaks the C ABI. This is all on purpose to stabilize the ABI to prep for a 1.0 stable libghostty-vt release.**
  
  All our enum-keyed APIs `*_{get,set,setopt,getopt}` now return a new
  result `GHOSTTY_UNSUPPORTED` for a key the library doesn't know. This
  lets a program compiled against newer headers but linked against an
  older build detect this case.
  
  Previously, unknown keys were undefined behavior. lol.
  
  Example usage:
  
  ```c
  bool blinking = false;
  switch (ghostty_render_state_get(state,
      GHOSTTY_RENDER_STATE_DATA_CURSOR_BLINKING, &blinking)) {
  case GHOSTTY_SUCCESS:
    break;
  case GHOSTTY_UNSUPPORTED:
    // Older library that doesn't know this key. Use a default.
    blinking = true;
    break;
  default:
    // A real error, such as a NULL state.
    return;
  }
  ```
  ````
- [`40066da`](https://github.com/ghostty-org/ghostty/commit/40066da055311c991b5c45be67313ef2b3661539) libghostty-vt: return GHOSTTY_UNSUPPORTED for unknown keys ([#15070](https://github.com/ghostty-org/ghostty/issues/15070)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  **This breaks the C ABI. This is all on purpose to stabilize the ABI to
  prep for a 1.0 stable libghostty-vt release.**
  
  All our enum-keyed APIs `*_{get,set,setopt,getopt}` now return a new
  result `GHOSTTY_UNSUPPORTED` for a key the library doesn't know. This
  lets a program compiled against newer headers but linked against an
  older build detect this case.
  
  Previously, unknown keys were undefined behavior. lol.
  
  Example usage:
  
  ```c
  bool blinking = false;
  switch (ghostty_render_state_get(state,
      GHOSTTY_RENDER_STATE_DATA_CURSOR_BLINKING, &blinking)) {
  case GHOSTTY_SUCCESS:
    break;
  case GHOSTTY_UNSUPPORTED:
    // Older library that doesn't know this key. Use a default.
    blinking = true;
    break;
  default:
    // A real error, such as a NULL state.
    return;
  }
  ```
  
  **AI usage:** My idea, I wrote the new docs and the main result return.
  Then the "repeatedly draw the owl" refactoring was done by Opus.
  Validated by Fable.
  ````
- [`5db83d7`](https://github.com/ghostty-org/ghostty/commit/5db83d7689bd7eaaaeb27198c9f870b04794cc8c) libghostty-vt: reserved allocator vtable slots, revamp allocator docs ([@mitchellh](https://github.com/mitchellh))
  ````text
  **This breaks the C ABI. This is all on purpose to stabilize the ABI to
  prep for a 1.0 stable libghostty-vt release.**
  
  Added four reserved `void*` slots to the end of `GhosttyAllocatorVtable`
  so we have room to add more function pointers if we ever want to.
  
  This also makes `resize` and `remap` optional. A NULL `resize` acts
  like it returned false and a NULL `remap` acts like it returned NULL,
  so the library falls back to alloc, copy, free. An allocator built on
  plain malloc and free now only needs `alloc` and `free`:
  
  ```c
  static const GhosttyAllocatorVtable vtable = {
      .alloc = my_alloc,
      .free = my_free,
  };
  ```
  
  The allocator docs in allocator.h were rewritten. They now cover the
  default allocator per platform, how to write an allocator, alignment
  (an exponent, not a byte count, which trips people up) and buffer
  ownership.
  
  The new example/c-vt-allocator is an alloc and free only allocator.
  ````
- [`ee02d01`](https://github.com/ghostty-org/ghostty/commit/ee02d019e8459ed4d09fac55753ad2363c5a8b01) libghostty-vt: reserved allocator vtable slots, revamp allocator docs ([#15068](https://github.com/ghostty-org/ghostty/issues/15068)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  **This breaks the C ABI. This is all on purpose to stabilize the ABI to
  prep for a 1.0 stable libghostty-vt release.**
  
  Added four reserved `void*` slots to the end of `GhosttyAllocatorVtable`
  so we have room to add more function pointers if we ever want to.
  
  This also makes `resize` and `remap` optional. A NULL `resize` acts like
  it returned false and a NULL `remap` acts like it returned NULL, so the
  library falls back to alloc, copy, free. An allocator built on plain
  malloc and free now only needs `alloc` and `free`:
  
  ```c
  static const GhosttyAllocatorVtable vtable = {
      .alloc = my_alloc,
      .free = my_free,
  };
  ```
  
  The allocator docs in allocator.h were rewritten. They now cover the
  default allocator per platform, how to write an allocator, alignment (an
  exponent, not a byte count, which trips people up) and buffer ownership.
  
  The new example/c-vt-allocator is an alloc and free only allocator.
  
  **AI usage:** Reviewed by Opus, primarily written by me, tests+example
  written by Opus.
  ````

## November 3, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/41704148845), [2](https://github.com/ghostty-org/ghostty/actions/runs/41657405741), [3](https://github.com/ghostty-org/ghostty/actions/runs/41640921915), [4](https://github.com/ghostty-org/ghostty/actions/runs/41612522728), [5](https://github.com/ghostty-org/ghostty/actions/runs/41588034700), [6](https://github.com/ghostty-org/ghostty/actions/runs/41578816344), [7](https://github.com/ghostty-org/ghostty/actions/runs/41569815273), [8](https://github.com/ghostty-org/ghostty/actions/runs/41558315898)  
Summary: 8 runs • 18 commits • 8 authors

### Changes

- [`0edfc65`](https://github.com/ghostty-org/ghostty/commit/0edfc656fa3d55d2bbf4519420666b19e5b19dba) macOS: fix tab bar frame on macOS 27 when it first appears. ([@bo2themax](https://github.com/bo2themax))
  ```text
  On macOS 27.2 (Probably already like this in early versions), the new tab button appears later than other views.
  The previous guard will skip the following layout, causing issues when the tab bar first appears on a window without tabs:
  1. "Show Tab Bar" the first time for a window without tabs.
  2. "Merge All Windows" from a window without tabs. The tab bar remains clipped until the next `becomeMain` or other functions trigger the setup.
  ```
- [`2d1f9cf`](https://github.com/ghostty-org/ghostty/commit/2d1f9cf1095ea4d5c0888ddbc62e03bd14e11597) os: reserve space for executable path terminator ([@12ya](https://github.com/12ya))
  ```text
  Return error.PathTooLong when a candidate path fills the buffer,
  leaving no room for the null terminator. Add a regression test for
  the boundary that previously caused an out-of-bounds write.
  ```
- [`fef7af4`](https://github.com/ghostty-org/ghostty/commit/fef7af4e19f6d8b0361c49e6190b81f3a64a999b) os: reserve space for executable path terminator ([#15058](https://github.com/ghostty-org/ghostty/issues/15058)) ([@jcollie](https://github.com/jcollie))
  ```text
  Return error.PathTooLong when a candidate path fills the buffer, leaving
  no room for the null terminator. Add a regression test for the boundary
  that previously caused an out-of-bounds write.
  
  AI disclosure: used OpenAI Codex
  ```
- [`c7f68a7`](https://github.com/ghostty-org/ghostty/commit/c7f68a7f48c6a5b357689eb8c2328bc2dab5d8ed) macOS: fix tab bar frame on macOS 27 when it first appears. ([#15029](https://github.com/ghostty-org/ghostty/issues/15029)) ([@bo2themax](https://github.com/bo2themax))
  ```text
  On macOS 27.2 (Probably already like this in early versions), the new
  tab button appears later than other views. The previous guard will skip
  the following layout, causing issues when the tab bar first appears on a
  window without tabs:
  1. "Show Tab Bar" the first time for a window without tabs.
  2. "Merge All Windows" from a window without tabs. The tab bar remains
  clipped until the next `becomeMain` or other functions trigger the
  setup.
  
  > New tab doesn't have the issue because it will trigger the setup
  multiple times (at least 3: addTitlebarAccessoryViewController,
  becomeMain and syncAppearance).
  
  ### AI Disclosure
  
  I check the RC myself and asked Claude to rephrase my scattered
  comments.
  ```
- [`fad1133`](https://github.com/ghostty-org/ghostty/commit/fad1133619a98a1bb60e99baac2d5460dfb33985) terminal: pass the style to fillStyles as a vector ([@arc-source-coder](https://github.com/arc-source-coder))
  ```text
  Without explicit `inline`, LLVM still inlines `fillStyles`, but
  writes each style as two 64-bit stores on x86-64. Passing the style
  as a vector restores one 16-byte vector store per style.
  
  ## Benchmarks
  
  `ghostty-bench +screen-clone` at 120x80 with 1 MiB of styled-heavy
  output, on Windows x86-64:
  
  | Mode          | main (ms)    | vector (ms)  | Speedup |
  | ------------- | ------------ | ------------ | ------- |
  | render-scroll | 441.4 ± 20.1 | 414.7 ± 14.6 | 1.06x   |
  ```
- [`4a2d77e`](https://github.com/ghostty-org/ghostty/commit/4a2d77ebb2d8d6973e1808bff1ca3e4f13b0a67b) terminal: reserve style runs once per row in RowBuilder.scan ([@arc-source-coder](https://github.com/arc-source-coder))
  ```text
  `RowBuilder.scan`, which runs during `beginUpdate`, previously called
  `ArrayList.append` for each style run.
  
  A cell starts at most one run, so reserve a row's worth of runs before
  the scan and use `appendAssumeCapacity`. Unlike `append`, which LLVM
  does not inline into the function, this compiles to inline stores.
  
  ## Benchmarks
  
  `ghostty-bench +screen-clone` on Windows x86-64:
  
  | Input         | Size   | Mode          | main (ms)     | reserve (ms)  | Speedup |
  | ------------- | ------ | ------------- | ------------- | ------------- | ------- |
  | DOOM-fire-zig | 160x50 | render-locked | 2480.6 ± 37.0 | 1285.0 ± 25.6 | 1.93x   |
  | DOOM-fire-zig | 160x50 | render        | 2759.3 ± 36.6 | 1571.1 ± 29.2 | 1.76x   |
  | styled-heavy  | 120x80 | render        | 297.1 ± 6.4   | 236.9 ± 6.4   | 1.25x   |
  | styled-heavy  | 120x80 | render-scroll | 414.5 ± 8.5   | 366.4 ± 9.0   | 1.13x   |
  ```
- [`7ea52a2`](https://github.com/ghostty-org/ghostty/commit/7ea52a29c5a91fa9a832aa6205add0a4311862da) terminal: pass the style to fillStyles as a vector ([#15053](https://github.com/ghostty-org/ghostty/issues/15053)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Follow-up to #15023.
  
  Without explicit `inline`, LLVM still inlines `fillStyles`, but lowers
  the fill to two 64-bit stores per style on x86-64. Passing the style as
  `@Vector(2, u64)` restores one `movdqu` 128-bit store.
  
  I also asked Sol to check ARM codegen: both versions already store the
  style in one instruction.
  
  ## Benchmarks
  
  `ghostty-bench +screen-clone` at 120x80 with 1 MiB of styled-heavy
  output, on Windows x86-64:
  
  | Mode          | main (ms)    | This PR (ms)  | Speedup |
  | ------------- | ------------ | ------------ | ------- |
  | render-scroll | 441.4 ± 20.1 | 414.7 ± 14.6 | 1.06x   |
  
  AI disclosure: Developed with OpenCode (GPT 6.1 Sol)
  ```
- [`6fba087`](https://github.com/ghostty-org/ghostty/commit/6fba0873efb7765e9d0f79de449063f3214b3d75) terminal: reserve style runs once per row in RowBuilder.scan ([#15054](https://github.com/ghostty-org/ghostty/issues/15054)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `RowBuilder.scan`, which runs during `beginUpdate`, previously appended
  each style run with `ArrayList.append`, which isn't inlined there. This
  reserves a row's worth of runs before the scan (a cell starts at most
  one run) and uses `appendAssumeCapacity`, which compiles to inline
  stores.
  
  ## Benchmarks
  
  `ghostty-bench +screen-clone` on Windows x86-64:
  
  | Input | Size | Mode | main (ms) | This PR (ms) | Speedup |
  | ------------- | ------ | ------------- | ------------- | -------------
  | ------- |
  | DOOM-fire-zig | 160x50 | render-locked | 2480.6 ± 37.0 | 1285.0 ± 25.6
  | 1.93x |
  | DOOM-fire-zig | 160x50 | render | 2759.3 ± 36.6 | 1571.1 ± 29.2 |
  1.76x |
  | styled-heavy | 120x80 | render | 297.1 ± 6.4 | 236.9 ± 6.4 | 1.25x |
  | styled-heavy | 120x80 | render-scroll | 414.5 ± 8.5 | 366.4 ± 9.0 |
  1.13x |
  
  AI disclosure: Developed with Claude Code (Opus 5.5) and OpenCode (GPT
  6.1 Sol), including benchmarking and codegen analysis.
  ```
- [`060ff6b`](https://github.com/ghostty-org/ghostty/commit/060ff6b52dcfde52112a8376c6cf3e26f4161edf) i18n: update Japanese translation ([#15025](https://github.com/ghostty-org/ghostty/issues/15025)) ([@clavinjune](https://github.com/clavinjune))
- [`b148bf7`](https://github.com/ghostty-org/ghostty/commit/b148bf728524ac17daec66692a8265d351c9c702) macos: allow quitting with a clipboard confirmation open ([@jparise](https://github.com/jparise))
  ```text
  The clipboard confirmation is a plain window presented as a sheet, and
  windows prevent application termination while modal by default. AppKit
  therefore dropped quit requests before reaching applicationShouldTerminate
  for as long as the modal was open. NSAlert sheets don't have this behavior.
  
  Verified with an active confirmation window using Cmd-Q, the quit action
  and Apple Event, and a quit event with the logout reason.
  ```
- [`0d1d5e8`](https://github.com/ghostty-org/ghostty/commit/0d1d5e884b88a711f1ccf47387ab41e8fa28a755) macos: allow quitting with a clipboard confirmation open ([#15040](https://github.com/ghostty-org/ghostty/issues/15040)) ([@bo2themax](https://github.com/bo2themax))
- [`c12d42e`](https://github.com/ghostty-org/ghostty/commit/c12d42eaf877b996cc798f9dd54b2a79ba630db9) terminal: print ASCII runs as u8 slices from input instead of u32 ([@mitchellh](https://github.com/mitchellh))
  ```text
  The stream now finds runs of plain ASCII (non-control) and passes that
  through to the terminal directly from the input pointer rather than widening
  it to u32 and doing a copy.
  
  This is implemented as a specialization on stream handlers, which both
  the Ghostty GUI and libghostty-vt handlers implement. If the specialized
  callback isn't implemented, the old `print_slice` (u32 slice) is used.
  
  Non-ASCII input takes the same path as before. utf8.vt and the CJK
  inputs are unchanged.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream` on Apple Silicon:
  
  | Input            | Size   | main (ms)    | print-u8 (ms) | Speedup |
  | ---------------- | ------ | ------------ | ------------- | ------- |
  | ascii.vt         | 120x80 | 43.2 ± 0.5   | 29.2 ± 0.5    | 1.48x   |
  | ascii-lines.vt   | 120x80 | 67.2 ± 0.5   | 51.3 ± 0.4    | 1.31x   |
  | styled-plain.vt  | 120x80 | 65.7 ± 0.3   | 48.9 ± 0.6    | 1.34x   |
  | light_cells.vt   | 120x80 | 39.3 ± 0.6   | 31.8 ± 0.3    | 1.24x   |
  | cursor_motion.vt | 120x80 | 147.2 ± 0.9  | 128.6 ± 1.1   | 1.14x   |
  | scrolling.vt     | 120x80 | 736.5 ± 6.4  | 648.7 ± 6.0   | 1.14x   |
  | dense_cells.vt   | 120x80 | 101.0 ± 0.7  | 94.8 ± 1.2    | 1.07x   |
  | utf8.vt          | 120x80 | 315.3 ± 2.6  | 314.6 ± 0.4   | 1.00x   |
  | osc.vt           | 120x80 | 951.5 ± 3.4  | 944.6 ± 2.7   | 1.01x   |
  | out.txt (2.6GB)  | 120x80 | 5177.6 ± 9.8 | 4892.7 ± 1.9  | 1.06x   |
  
  `ghostty-bench +terminal-stream` on x86-64 (Haswell, KVM guest):
  
  | Input            | Size   | main (ms) | print-u8 (ms) | Speedup |
  | ---------------- | ------ | --------- | ------------- | ------- |
  | ascii.vt         | 120x80 | 122.5     | 95.5          | 1.28x   |
  | ascii-lines.vt   | 120x80 | 234.5     | 175.9         | 1.33x   |
  | styled-plain.vt  | 120x80 | 231.8     | 174.4         | 1.33x   |
  | light_cells.vt   | 120x80 | 83.4      | 64.5          | 1.29x   |
  | cursor_motion.vt | 120x80 | 564.0     | 459.4         | 1.23x   |
  | scrolling.vt     | 120x80 | 3918.0    | 3577.6        | 1.10x   |
  | styled-heavy.vt  | 120x80 | 574.7     | 520.4         | 1.10x   |
  | dense_cells.vt   | 120x80 | 382.1     | 350.2         | 1.09x   |
  | medium_cells.vt  | 120x80 | 651.8     | 607.0         | 1.07x   |
  | utf8.vt          | 120x80 | 895.4     | 881.5         | 1.02x   |
  | cjk-prose.vt     | 120x80 | 274.9     | 280.8         | 0.98x   |
  | hyperlinks.vt    | 120x80 | 135.0     | 128.2         | 1.05x   |
  ```
- [`a227276`](https://github.com/ghostty-org/ghostty/commit/a227276b770c450ab0e5704a42a773c952e4991b) terminal: clear the blank hint where a snapshot test writes cells ([@mitchellh](https://github.com/mitchellh))
- [`091beb9`](https://github.com/ghostty-org/ghostty/commit/091beb99250bc4c1a255d3617b54630c115d0f27) terminal: print ASCII runs as u8 slices from input instead of u32 ([#15046](https://github.com/ghostty-org/ghostty/issues/15046)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The stream now finds runs of plain ASCII (non-control) and passes that
  through to the terminal directly from the input pointer rather than
  widening it to u32 and doing a copy.
  
  This is implemented as a specialization on stream handlers, which both
  the Ghostty GUI and libghostty-vt handlers implement. If the specialized
  callback isn't implemented, the old `print_slice` (u32 slice) is used.
  
  Non-ASCII input takes the same path as before. utf8.vt and the CJK
  inputs are unchanged.
  
  **Note: this does not speed up pure-ASCII `cat` times.** The speedups
  below are based on raw bytes pumping through libghostty's core. Our
  `cat` times in the shell are bound by the _kernel_, we're already within
  5% of the speed of a full 100% CPU busy loop pumping bytes out of a pty
  as fast as it can (and the last 5% is because we don't spin the CPU at
  100%).
  
  Edit: I edited the above to say "pure ASCII" because it does measurably
  speed up `cat`-ing the asciinema 2.6GB dump. That's because we now
  process the ASCII runs at full speed while slower sequences can't
  process at pty-read-speeds.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream` on Apple Silicon:
  
  | Input            | Size   | main (ms)    | print-u8 (ms) | Speedup |
  | ---------------- | ------ | ------------ | ------------- | ------- |
  | ascii.vt         | 120x80 | 43.2 ± 0.5   | 29.2 ± 0.5    | 1.48x   |
  | ascii-lines.vt   | 120x80 | 67.2 ± 0.5   | 51.3 ± 0.4    | 1.31x   |
  | styled-plain.vt  | 120x80 | 65.7 ± 0.3   | 48.9 ± 0.6    | 1.34x   |
  | light_cells.vt   | 120x80 | 39.3 ± 0.6   | 31.8 ± 0.3    | 1.24x   |
  | cursor_motion.vt | 120x80 | 147.2 ± 0.9  | 128.6 ± 1.1   | 1.14x   |
  | scrolling.vt     | 120x80 | 736.5 ± 6.4  | 648.7 ± 6.0   | 1.14x   |
  | dense_cells.vt   | 120x80 | 101.0 ± 0.7  | 94.8 ± 1.2    | 1.07x   |
  | utf8.vt          | 120x80 | 315.3 ± 2.6  | 314.6 ± 0.4   | 1.00x   |
  | osc.vt           | 120x80 | 951.5 ± 3.4  | 944.6 ± 2.7   | 1.01x   |
  | out.txt (2.6GB)  | 120x80 | 5177.6 ± 9.8 | 4892.7 ± 1.9  | 1.06x   |
  
  `ghostty-bench +terminal-stream` on x86-64 (Haswell, KVM guest):
  
  | Input            | Size   | main (ms) | print-u8 (ms) | Speedup |
  | ---------------- | ------ | --------- | ------------- | ------- |
  | ascii.vt         | 120x80 | 122.5     | 95.5          | 1.28x   |
  | ascii-lines.vt   | 120x80 | 234.5     | 175.9         | 1.33x   |
  | styled-plain.vt  | 120x80 | 231.8     | 174.4         | 1.33x   |
  | light_cells.vt   | 120x80 | 83.4      | 64.5          | 1.29x   |
  | cursor_motion.vt | 120x80 | 564.0     | 459.4         | 1.23x   |
  | scrolling.vt     | 120x80 | 3918.0    | 3577.6        | 1.10x   |
  | styled-heavy.vt  | 120x80 | 574.7     | 520.4         | 1.10x   |
  | dense_cells.vt   | 120x80 | 382.1     | 350.2         | 1.09x   |
  | medium_cells.vt  | 120x80 | 651.8     | 607.0         | 1.07x   |
  | utf8.vt          | 120x80 | 895.4     | 881.5         | 1.02x   |
  | cjk-prose.vt     | 120x80 | 274.9     | 280.8         | 0.98x   |
  | hyperlinks.vt    | 120x80 | 135.0     | 128.2         | 1.05x   |
  ```
- [`6676bba`](https://github.com/ghostty-org/ghostty/commit/6676bbaec73a2a30eced56003dd7248e931de6fa) Update VOUCHED list ([#15045](https://github.com/ghostty-org/ghostty/issues/15045)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/15044#discussioncomment-19366333)
  from @jcollie.
  
  Vouch: @ghdtjdwn
  ```
- [`25de649`](https://github.com/ghostty-org/ghostty/commit/25de649dde19bb96c7ad8ec4f7d28441a865da09) terminal: write the blank row once when scrolling a region up ([@mitchellh](https://github.com/mitchellh))
  ```text
  Scrolling up inside a scroll region (`cursorScrollRegionUp`) now builds
  the erased row's reset header in a register and writes it straight into
  the row's new slot at the bottom of the region. Previously it reset the
  row in place and then rotated it there.
  
  On x86-64 this improves scroll region vtebench results by 6-8%. This
  was actually a regress from #14997 so this just gets that back.
  
  Apple Silicon was never affected and still isn't. It now runs one fewer
  instruction per scrolled row with no measurable change in time. Other
  inputs stay within 0.06% of main in instructions retired.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream` on x86-64 (Haswell, KVM guest).
  
  | Input                         | Size   | main (ms) | x86-scroll (ms) | Speedup |
  | ----------------------------- | ------ | --------- | --------------- | ------- |
  | scrolling_top_small_region.vt | 120x80 | 2837.3    | 2582.3          | 1.11x   |
  | scrolling_bottom_region.vt    | 120x80 | 2775.0    | 2659.7          | 1.02x   |
  | scrolling.vt                  | 120x80 | 3855.1    | 3818.0          | 1.01x   |
  
  ## Why?
  
  `Row.blank` took a bit from the row's padding, and that changed how LLVM
  lowers the unchanged `row.reset()`. It now emits a 4-byte store of only
  the header's high half. `rotateOnce` does an 8-byte load of that same
  header a few instructions later. x86 can't forward a narrow store into
  a wider load, so every scrolled line waited for the store to reach
  cache. A profile put 62% of `cursorScrollRegionUp`'s samples right
  after that load.
  
  `fastmem.rotateIn` shifts the region and writes the new header after
  the memmove, so the header never makes the round trip through memory.
  With the change, the function's samples are back at their level from
  before #14997.
  ```
- [`18e645e`](https://github.com/ghostty-org/ghostty/commit/18e645ea22a5ef4793a2008275eb6f98e5d039bb) terminal: write the blank row once when scrolling a region up ([#15042](https://github.com/ghostty-org/ghostty/issues/15042)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Scrolling up inside a scroll region (`cursorScrollRegionUp`) now builds
  the erased row's reset header in a register and writes it straight into
  the row's new slot at the bottom of the region. Previously it reset the
  row in place and then rotated it there.
  
  On x86-64 this improves scroll region vtebench results by 6-8%. This was
  actually a regress from #14997 so this just gets that back.
  
  Apple Silicon was never affected and still isn't. It now runs one fewer
  instruction per scrolled row with no measurable change in time. Other
  inputs stay within 0.06% of main in instructions retired.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream` on x86-64 (Haswell, KVM guest).
  
  | Input | Size | main (ms) | x86-scroll (ms) | Speedup |
  | ----------------------------- | ------ | --------- | --------------- |
  ------- |
  | scrolling_top_small_region.vt | 120x80 | 2837.3 | 2582.3 | 1.11x |
  | scrolling_bottom_region.vt | 120x80 | 2775.0 | 2659.7 | 1.02x |
  | scrolling.vt | 120x80 | 3855.1 | 3818.0 | 1.01x |
  
  ## Why?
  
  `Row.blank` took a bit from the row's padding, and that changed how LLVM
  lowers the unchanged `row.reset()`. It now emits a 4-byte store of only
  the header's high half. `rotateOnce` does an 8-byte load of that same
  header a few instructions later. x86 can't forward a narrow store into a
  wider load, so every scrolled line waited for the store to reach cache.
  A profile put 62% of `cursorScrollRegionUp`'s samples right after that
  load.
  
  `fastmem.rotateIn` shifts the region and writes the new header after the
  memmove, so the header never makes the round trip through memory. With
  the change, the function's samples are back at their level from before
  #14997.
  
  **AI usage:** Fable figured this out. I had no idea, but I looked at its
  analysis and agree with its conclusions. I pushed it in bunch of
  different ways and couldn't find any holes. I wrote the prose.
  ```
- [`fa3b435`](https://github.com/ghostty-org/ghostty/commit/fa3b435cbfdc70c4e41ace87e1cde401f62e2aa5) Update VOUCHED list ([#15041](https://github.com/ghostty-org/ghostty/issues/15041)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14147#discussioncomment-19363823)
  from @jcollie.
  
  Vouch: @danudey
  ```

## November 2, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/41546831074), [2](https://github.com/ghostty-org/ghostty/actions/runs/41520563485), [3](https://github.com/ghostty-org/ghostty/actions/runs/41511614122), [4](https://github.com/ghostty-org/ghostty/actions/runs/41506747057), [5](https://github.com/ghostty-org/ghostty/actions/runs/41502755506), [6](https://github.com/ghostty-org/ghostty/actions/runs/41491697673), [7](https://github.com/ghostty-org/ghostty/actions/runs/41485839464), [8](https://github.com/ghostty-org/ghostty/actions/runs/41478021093), [9](https://github.com/ghostty-org/ghostty/actions/runs/41466669618), [10](https://github.com/ghostty-org/ghostty/actions/runs/41459038808), [11](https://github.com/ghostty-org/ghostty/actions/runs/41388327846), [12](https://github.com/ghostty-org/ghostty/actions/runs/41364959727)  
Summary: 12 runs • 39 commits • 5 authors

### Changes

- [`0e067de`](https://github.com/ghostty-org/ghostty/commit/0e067ded703c4212248daf996f97c62f2f13114a) core: declare pointer nullability in ghostty.h ([@jparise](https://github.com/jparise))
  ```text
  Pointers in ghostty.h declared no nullability information, so Swift
  imported them all as implicitly unwrapped optionals. This lack of
  enforcement made it possible to miss a guard and pass NULL to a non-null
  Zig parameter.
  
  Make non-null the header's default using Clang's `assume_nonnull` and
  explicitly annotate the other nullable pointers based on their Zig
  declarations.
  
  This exposed a few existing calls that had the wrong expectations:
  
  - The ghostty_set_window_background_blur callers, readSelection, and
    Config.backgroundColor could pass NULL and now guard their optional
    values.
  - Clearing the preedit passes NULL, so ghostty_surface_preedit now
    accepts a nullable pointer on the Zig side too.
  
  This change is source-breaking for Swift embedders because optional
  handling of newly non-optional values will no longer compile.
  ```
- [`a455842`](https://github.com/ghostty-org/ghostty/commit/a455842c28d587cd2ee2b75cc21fa021b1a47d09) core: declare pointer nullability in ghostty.h ([#15039](https://github.com/ghostty-org/ghostty/issues/15039)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Pointers in ghostty.h declared no nullability information, so Swift
  imported them all as implicitly unwrapped optionals. This lack of
  enforcement made it possible to miss a guard and pass NULL to a non-null
  Zig parameter.
  
  Make non-null the header's default using Clang's `assume_nonnull` and
  explicitly annotate the other nullable pointers based on their Zig
  declarations.
  
  This exposed a few existing calls that had the wrong expectations:
  
  - The ghostty_set_window_background_blur callers, readSelection, and
  Config.backgroundColor could pass NULL and now guard their optional
  values.
  - Clearing the preedit passes NULL, so ghostty_surface_preedit now
  accepts a nullable pointer on the Zig side too.
  
  This change is source-breaking for Swift embedders because optional
  handling of newly non-optional values will no longer compile.
  ```
- [`4c92f80`](https://github.com/ghostty-org/ghostty/commit/4c92f80954b1d563c148d77a051394fd2d39de60) terminal: print fast stays active while a hyperlink is open ([@mitchellh](https://github.com/mitchellh))
  ```text
  `printSlice` previously bailed out of its fast path whenever an OSC 8
  hyperlink was open and printed every codepoint through the scalar
  `print`. It now writes linked text with the same batched fills as
  unlinked text.
  
  The batched path is specialized at comptime on whether a link is open,
  decided once per `printSlice` call. We don't inline the link open part
  because it is rarer.
  
  The hyperlink map has a fixed capacity, so the fills only write as many
  cells as it has room for and never grow the page themselves (that would
  replace the page under their cached pointers). When it is full, `print`
  writes the next codepoint and grows the page through
  `cursorSetHyperlink` exactly as before.
  
  Overwriting cells that are already linked still falls back to `print`.
  That's something we can maybe optimize in the future.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream`:
  
  | Input              | Size    | main (ms)     | print-hyperlink (ms) | Speedup |
  | ------------------ | ------- | ------------- | -------------------- | ------- |
  | hyperlinks-long.vt | 120x80  | 94.0 ± 1.2    | 54.4 ± 1.0           | 1.73x   |
  | hyperlinks-long.vt | 215x215 | 99.3 ± 1.2    | 60.4 ± 1.5           | 1.64x   |
  | alternating.vt     | 120x80  | 154.4 ± 1.5   | 125.8 ± 0.5          | 1.23x   |
  | alternating.vt     | 215x215 | 150.2 ± 0.8   | 122.7 ± 1.8          | 1.22x   |
  | styled-mixed.vt    | 120x80  | 499.1 ± 3.5   | 454.6 ± 3.5          | 1.10x   |
  | styled-mixed.vt    | 215x215 | 460.6 ± 1.4   | 420.9 ± 5.1          | 1.09x   |
  | hyperlinks.vt      | 120x80  | 43.9 ± 0.5    | 39.9 ± 0.2           | 1.10x   |
  | hyperlinks.vt      | 215x215 | 44.9 ± 0.4    | 42.5 ± 0.8           | 1.06x   |
  | osc.vt             | 120x80  | 990.5 ± 15.8  | 944.8 ± 3.9          | 1.05x   |
  | osc.vt             | 215x215 | 1004.9 ± 9.6  | 963.2 ± 6.8          | 1.04x   |
  | ascii.vt           | 120x80  | 41.8 ± 0.3    | 41.7 ± 0.2           | 1.00x   |
  ```
- [`91973f2`](https://github.com/ghostty-org/ghostty/commit/91973f2b29be42a2a8713406e18c56238b5f6c19) terminal: print fast stays active while a hyperlink is open ([#15034](https://github.com/ghostty-org/ghostty/issues/15034)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `printSlice` previously bailed out of its fast path whenever an OSC 8
  hyperlink was open and printed every codepoint through the scalar
  `print`. It now writes linked text with the same batched fills as
  unlinked text.
  
  The batched path is specialized at comptime on whether a link is open,
  decided once per `printSlice` call. We don't inline the link open part
  because it is rarer.
  
  The hyperlink map has a fixed capacity, so the fills only write as many
  cells as it has room for and never grow the page themselves (that would
  replace the page under their cached pointers). When it is full, `print`
  writes the next codepoint and grows the page through
  `cursorSetHyperlink` exactly as before.
  
  Overwriting cells that are already linked still falls back to `print`.
  That's something we can maybe optimize in the future.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream`:
  
  | Input | Size | main (ms) | print-hyperlink (ms) | Speedup |
  | ------------------ | ------- | ------------- | -------------------- |
  ------- |
  | hyperlinks-long.vt | 120x80 | 94.0 ± 1.2 | 54.4 ± 1.0 | 1.73x |
  | hyperlinks-long.vt | 215x215 | 99.3 ± 1.2 | 60.4 ± 1.5 | 1.64x |
  | alternating.vt | 120x80 | 154.4 ± 1.5 | 125.8 ± 0.5 | 1.23x |
  | alternating.vt | 215x215 | 150.2 ± 0.8 | 122.7 ± 1.8 | 1.22x |
  | styled-mixed.vt | 120x80 | 499.1 ± 3.5 | 454.6 ± 3.5 | 1.10x |
  | styled-mixed.vt | 215x215 | 460.6 ± 1.4 | 420.9 ± 5.1 | 1.09x |
  | hyperlinks.vt | 120x80 | 43.9 ± 0.5 | 39.9 ± 0.2 | 1.10x |
  | hyperlinks.vt | 215x215 | 44.9 ± 0.4 | 42.5 ± 0.8 | 1.06x |
  | osc.vt | 120x80 | 990.5 ± 15.8 | 944.8 ± 3.9 | 1.05x |
  | osc.vt | 215x215 | 1004.9 ± 9.6 | 963.2 ± 6.8 | 1.04x |
  | ascii.vt | 120x80 | 41.8 ± 0.3 | 41.7 ± 0.2 | 1.00x |
  
  **AI usage:** Idea/impl by me, Fable review and benchmark.
  ```
- [`8484146`](https://github.com/ghostty-org/ghostty/commit/8484146c74ef4b075b68c9cf8767019b2b3c738c) terminal: skip erasing and scanning rows that are already blank ([@mitchellh](https://github.com/mitchellh))
  ```text
  Erase line (EL, `CSI K`) and erase character (ECH, `CSI X`) now do
  nothing to the cells of a row that is already blank. Scrolling the
  screen into history before a clear (`CSI 22 J`, or `CSI 2 J` at a
  prompt) no longer reads the cells of blank rows, and scans the other
  rows several cells at a time.
  
  This extends the `Row.blank` hint from #14997, which only covered whole
  rows cleared by erase display:
  https://github.com/ghostty-org/ghostty/pull/14997
  
  This doesn't impact any other workloads, and was identified in the
  asciinema dump as a relatively common command (see 2% speedup).
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream`:
  
  | Input           | Size    | main (ms)   | erase-opt-2 (ms) | Speedup |
  | --------------- | ------- | ----------- | ---------------- | ------- |
  | erase-scroll.vt | 120x80  | 241.9 ± 0.6 | 107.7 ± 0.2      | 2.24x   |
  | erase-scroll.vt | 120x12  | 50.5 ± 0.2  | 46.2 ± 0.4       | 1.09x   |
  | erase-scroll.vt | 300x100 | 797.6 ± 1.7 | 259.9 ± 0.5      | 3.07x   |
  | erase-lines.vt  | 120x80  | 43.9 ± 0.4  | 25.7 ± 0.3       | 1.71x   |
  | erase-lines.vt  | 120x12  | 41.6 ± 0.3  | 24.1 ± 0.5       | 1.73x   |
  | erase-lines.vt  | 300x100 | 80.3 ± 0.4  | 29.1 ± 0.2       | 2.76x   |
  | erase.vt        | 120x80  | 51.4 ± 0.4  | 51.5 ± 0.3       | 1.00x   |
  | ascii.vt        | 120x80  | 42.6 ± 0.8  | 42.2 ± 0.4       | 1.01x   |
  | styled-plain.vt | 120x80  | 66.5 ± 0.8  | 64.9 ± 0.5       | 1.02x   |
  | utf8.vt         | 120x80  | 316.2 ± 1.8 | 315.8 ± 1.4      | 1.00x   |
  | osc.vt          | 120x80  | 991 ± 21    | 979 ± 6          | 1.01x   |
  | scrolling.vt    | 120x80  | 736.2 ± 6.4 | 736.8 ± 6.1      | 1.00x   |
  | scrolling_fs.vt | 120x80  | 53.1 ± 0.2  | 53.1 ± 0.3       | 1.00x   |
  | out.txt (2.6GB) | 120x80  | 5315 ± 22   | 5231 ± 13        | 1.02x   |
  ```
- [`a0c0928`](https://github.com/ghostty-org/ghostty/commit/a0c092868ded132033c85104e9ab3a266c52f2d4) terminal: skip erasing and scanning rows that are already blank ([#15035](https://github.com/ghostty-org/ghostty/issues/15035)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Erase line (EL, `CSI K`) and erase character (ECH, `CSI X`) now do
  nothing to the cells of a row that is already blank. Scrolling the
  screen into history before a clear (`CSI 22 J`, or `CSI 2 J` at a
  prompt) no longer reads the cells of blank rows, and scans the other
  rows several cells at a time.
  
  This extends the `Row.blank` hint from #14997, which only covered whole
  rows cleared by erase display:
  https://github.com/ghostty-org/ghostty/pull/14997
  
  This doesn't impact any other workloads, and was identified in the
  asciinema dump as a relatively common command (see 2% speedup).
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream`:
  
  | Input           | Size    | main (ms)   | erase-opt-2 (ms) | Speedup |
  | --------------- | ------- | ----------- | ---------------- | ------- |
  | erase-scroll.vt | 120x80  | 241.9 ± 0.6 | 107.7 ± 0.2      | 2.24x   |
  | erase-scroll.vt | 120x12  | 50.5 ± 0.2  | 46.2 ± 0.4       | 1.09x   |
  | erase-scroll.vt | 300x100 | 797.6 ± 1.7 | 259.9 ± 0.5      | 3.07x   |
  | erase-lines.vt  | 120x80  | 43.9 ± 0.4  | 25.7 ± 0.3       | 1.71x   |
  | erase-lines.vt  | 120x12  | 41.6 ± 0.3  | 24.1 ± 0.5       | 1.73x   |
  | erase-lines.vt  | 300x100 | 80.3 ± 0.4  | 29.1 ± 0.2       | 2.76x   |
  | erase.vt        | 120x80  | 51.4 ± 0.4  | 51.5 ± 0.3       | 1.00x   |
  | ascii.vt        | 120x80  | 42.6 ± 0.8  | 42.2 ± 0.4       | 1.01x   |
  | styled-plain.vt | 120x80  | 66.5 ± 0.8  | 64.9 ± 0.5       | 1.02x   |
  | utf8.vt         | 120x80  | 316.2 ± 1.8 | 315.8 ± 1.4      | 1.00x   |
  | osc.vt          | 120x80  | 991 ± 21    | 979 ± 6          | 1.01x   |
  | scrolling.vt    | 120x80  | 736.2 ± 6.4 | 736.8 ± 6.1      | 1.00x   |
  | scrolling_fs.vt | 120x80  | 53.1 ± 0.2  | 53.1 ± 0.3       | 1.00x   |
  | out.txt (2.6GB) | 120x80  | 5315 ± 22   | 5231 ± 13        | 1.02x   |
  
  **AI usage:** I did the impl after #14997, Opus/Fable reviewed and
  benchmarked. Note: a lot of these are coming in fast now cause I was
  doing a lot of it in parallel over the weekend, the benchmarks and
  review took time.
  ```
- [`0b1729e`](https://github.com/ghostty-org/ghostty/commit/0b1729e945978fca4bcd6165d8ac408bf675a7f2) Update VOUCHED list ([#15036](https://github.com/ghostty-org/ghostty/issues/15036)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/15033#discussioncomment-19359609)
  from @jcollie.
  
  Vouch: @database64128
  ```
- [`22b8451`](https://github.com/ghostty-org/ghostty/commit/22b84514411aab13ce71c09052a10c76380eaf4b) terminal: re-read the style per row in the mixed-width print fast path ([@mitchellh](https://github.com/mitchellh))
  ```text
  `printSliceMixed` now reads the cursor's style ID for every row it
  fills, instead of building its cell template once at the start of the
  slice.
  
  This is a bug from the mixed narrow/wide fast path in #15021:
  https://github.com/ghostty-org/ghostty/pull/15021
  ```
- [`e0acea2`](https://github.com/ghostty-org/ghostty/commit/e0acea2753f84ec31c26cdc1c8837fad99cd83b9) terminal: re-read the style per row in the mixed-width print fast path ([#15032](https://github.com/ghostty-org/ghostty/issues/15032)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `printSliceMixed` now reads the cursor's style ID for every row it
  fills, instead of building its cell template once at the start of the
  slice.
  
  This is a bug from the mixed narrow/wide fast path in #15021:
  https://github.com/ghostty-org/ghostty/pull/15021
  ```
- [`faa346b`](https://github.com/ghostty-org/ghostty/commit/faa346b068361c47826b653af5e4a526e5a4e957) terminal: print uses the right margin after wrapping ([@mitchellh](https://github.com/mitchellh))
  ```text
  With left/right margins set and the cursor right of the right margin,
  `print` kept using the screen edge as its limit even after wrapping
  to the left margin. A wide char after the wrap could leave the cursor
  outside the margins. `printSlice` already handled this correctly.
  
  This matches xterm, which recomputes the right edge after every wrap
  (`dotext` in charproc.c).
  
  The fix resets the limit to the right margin after each wrap.
  ```
- [`77f85cd`](https://github.com/ghostty-org/ghostty/commit/77f85cd67c4c434acc714bb1d1248107a3782a68) terminal: print uses the right margin after wrapping ([#15030](https://github.com/ghostty-org/ghostty/issues/15030)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  With left/right margins set and the cursor right of the right margin,
  `print` kept using the screen edge as its limit even after wrapping to
  the left margin. A wide char after the wrap could leave the cursor
  outside the margins. `printSlice` already handled this correctly.
  
  This matches xterm, which recomputes the right edge after every wrap
  (`dotext` in charproc.c).
  
  The fix resets the limit to the right margin after each wrap.
  ```
- [`41557e2`](https://github.com/ghostty-org/ghostty/commit/41557e2ccf7f27b7ed6665b163bd467d4fa8691e) terminal: store Style as a packed u128 ([@arc-source-coder](https://github.com/arc-source-coder))
  ```text
  Style is now a `packed struct(u128)`. Equality compares the bits
  directly, hashing no longer builds a separate `PackedStyle`, and
  the style is all zero bits.
  
  `Style.Color` now uses an 8-bit tag and 24-bit payload. The constructors
  zero unused bits, and value() provides a tagged-union view for switching
  on a color. This also removes the wasm-specific equality and default
  checks.
  
  A u128 is 16-byte aligned, which increases the alignment of the style
  set. The page capacity calculation now accounts for padding before the
  metadata.
  
  `ghostty-bench +terminal-stream` at 120x80, on Windows x86-64:
  
  | Input           | main (ms)    | packed (ms)  | Speedup |
  | --------------- | ------------ | ------------ | ------- |
  | styled-heavy.vt | 377.8 ± 7.5  | 330.0 ± 9.1  | 1.14x   |
  | styled-multi.vt | 443.5 ± 17.2 | 401.9 ± 12.4 | 1.10x   |
  | ascii.vt        | 73.6 ± 2.0   | 72.3 ± 1.9   | 1.02x   |
  | utf8.vt         | 580.9 ± 20.3 | 573.7 ± 14.6 | 1.01x   |
  | styled-mixed.vt | 1088 ± 8     | 1085 ± 16    | 1.00x   |
  | styled-plain.vt | 112.6 ± 2.6  | 112.5 ± 3.0  | 1.00x   |
  | osc.vt          | 2256 ± 31    | 2256 ± 64    | 1.00x   |
  
  `ghostty-bench +screen-clone` at 120x80 on 1 MiB of styled-heavy.vt:
  
  | Mode          | main (ms)    | packed (ms)  | Speedup |
  | ------------- | ------------ | ------------ | ------- |
  | render-scroll | 561.3 ± 21.0 | 453.9 ± 22.3 | 1.24x   |
  | render        | 342.3 ± 9.7  | 310.8 ± 6.1  | 1.10x   |
  ```
- [`73a2a1d`](https://github.com/ghostty-org/ghostty/commit/73a2a1d06e9269b67257f4ab810f1a489f0d5b19) terminal: move SGR attribute handling to Style ([@arc-source-coder](https://github.com/arc-source-coder))
  ```text
  Move the SGR attribute switch from `Screen.applyAttribute` into
  `Style.withAttribute(attr)`, which returns the updated style.
  
  Performance is neutral to slightly faster (2-3%) on sequences with
  several attributes. With `withAttribute` inlined, LLVM keeps the running
  style and cursor pointer in registers across attributes instead of
  reloading them from the stack. On x86-64, a bold attribute goes from
  34 to 28 instructions per loop iteration, and `38;5;N` from 66 to 47.
  ```
- [`72bc97a`](https://github.com/ghostty-org/ghostty/commit/72bc97a9edf5df1080fa68fc8b38c45dc692c8ea) terminal: simplify fillStyles to one vector store ([@arc-source-coder](https://github.com/arc-source-coder))
  ```text
  Now that Style is exactly 16 bytes, `fillStyles` writes each style with
  one vector store. The old version used two overlapping 16-byte stores
  to handle styles of 16-32 bytes. With a 16-byte Style, both write to the
  same address, and LLVM lowered the old loop to two 64-bit stores per style.
  
  `ghostty-bench +screen-clone` at 120x80 on 1 MiB of styled-heavy.vt:
  
  | Mode          | before (ms)   | after (ms)   | Speedup |
  | ------------- | ------------- | ------------ | ------- |
  | render-scroll | 457.2 ± 25.7  | 424.9 ± 23.3 | 1.08x   |
  | render        | 314.4 ± 7.0   | 312.4 ± 6.0  | 1.01x   |
  ```
- [`de16f08`](https://github.com/ghostty-org/ghostty/commit/de16f08dcf7f3f4104e8722cb39a632a6a8a19f9) terminal: assert canonical Style.Color bits, test hash and constructors ([@mitchellh](https://github.com/mitchellh))
  ```text
  Review follow-ups for the packed Style:
  
  * `Color.value()` now asserts that the unused payload bits of `.none`
    and `.palette` colors are zero. Equality and hashing compare raw bits,
    so a non-canonical color would compare unequal to its canonical twin
    while reading back as the same value. The assert is `unreachable` in
    release builds and costs nothing there.
  
  * Drop the `hasUniqueRepresentation` assert. For a packed struct it
    reduces to `@sizeOf * 8 == @bitSizeOf`, which the two asserts above
    it already state.
  
  * Add tests that the three constructors leave unused bits zero and that
    the hash fold separates the same value in different fields (fg vs bg
    vs underline, palette vs flags), which is what the odd multiplier on
    the upper half exists for.
  
  * `fillStyles` has one call site; drop `inline`.
  ```
- [`d20d208`](https://github.com/ghostty-org/ghostty/commit/d20d208c514661ca14b9935576d66655fa2a8be8) terminal: size the hyperlink map independently of the hyperlink set ([@mitchellh](https://github.com/mitchellh))
  ```text
  A page's hyperlink map is now sized by its own capacity field,
  `hyperlink_cells`, instead of being derived from the hyperlink
  set's byte capacity. We previously derived it from bytes and were
  usually wasting bytes.
  
  The point of this change is primarily MEMORY DENSITY. We now get more
  rows/MB since our page structure isn't wasting as much. See benchmarks below.
  
  The snapshot format is unchanged. The PAGE header's single hyperlink
  capacity hint now covers both tables (the larger of the set bytes and
  the map's equivalent in set items), so old snapshots decode to the same
  layout as before and new snapshots stay readable by current readers.
  I made that as a choice to avoid breaking snapshots. Snapshots don't
  need perfect decode and its not super important for performance there.
  
  `ghostty-bench +terminal-stream`:
  
  | Input           | Size    | main (ms)    | hyperlink-map-size (ms) | Speedup |
  | --------------- | ------- | ------------ | ----------------------- | ------- |
  | hyperlinks.vt   | 215x215 | 61.8 ± 1.3   | 44.7 ± 0.5              | 1.38x   |
  | hyperlinks.vt   | 120x80  | 53.7 ± 0.3   | 43.5 ± 0.3              | 1.23x   |
  | osc.vt          | 120x80  | 1129.0 ± 2.2 | 978.8 ± 4.2             | 1.15x   |
  | osc.vt          | 215x215 | 1097.4 ± 6.7 | 1012.8 ± 4.0            | 1.08x   |
  | alternating.vt  | 120x80  | 163.8 ± 3.3  | 151.8 ± 0.9             | 1.08x   |
  | burst.vt        | 120x80  | 73.8 ± 0.6   | 68.9 ± 0.4              | 1.07x   |
  | styled-mixed.vt | 120x80  | 575.0 ± 2.1  | 580.1 ± 4.6             | 0.99x   |
  | styled-heavy.vt | 120x80  | 230.5 ± 0.2  | 230.5 ± 0.6             | 1.00x   |
  | ascii.vt        | 120x80  | 40.4 ± 0.3   | 40.5 ± 0.1              | 1.00x   |
  | utf8.vt         | 120x80  | 382.0 ± 0.9  | 386.0 ± 5.0             | 0.99x   |
  | erase.vt        | 120x80  | 50.1 ± 0.1   | 50.8 ± 0.1              | 0.99x   |
  
  The speedups come from fewer page clones (osc.vt at 120x80 went from
  232 capacity growths to 62) and from pages staying in the pool instead
  of being allocated on the heap. So this helps in general.
  
  Now memory. At a 10 MB scrollback limit at 120x80:
  
  | Input          | Heap pages   | History rows | Rows/MiB   |
  | -------------- | ------------ | ------------ | ---------- |
  | osc.vt         | 2157 -> 328  | 5625 -> 6507 | 624 -> 694 |
  | hyperlinks.vt  | 520 -> 6     | 6125 -> 7262 | 681 -> 775 |
  | alternating.vt | 1088 -> 266  | 9002 -> 9032 | 948 -> 963 |
  | ascii.vt       | 0 -> 0       | 9117 -> 9117 | 972 -> 972 |
  ```
- [`687f37a`](https://github.com/ghostty-org/ghostty/commit/687f37acd90462d451acd5f79042822d5d0255fb) terminal: pack Style into 128 bits and simplify style updates ([#15023](https://github.com/ghostty-org/ghostty/issues/15023)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously, style comparisons checked flags and colors field by field,
  and hashing created a `PackedStyle` each time. This stores `Style`
  directly as a `packed struct(u128)`, so equality becomes a single
  integer comparison and hashing no longer needs the packing step. It also
  removes the wasm-specific equality and default-style checks.
  
  This also moves SGR attribute application from `Screen` into
  `Style.withAttribute`, which allows LLVM to keep the running style in
  registers across attributes. The render-state style fill now uses one
  16-byte vector store per cell.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream` at 120x80, on Windows x86-64:
  
  | Input           | main (ms)    | This PR (ms)   | Speedup |
  | --------------- | ------------ | ------------ | ------- |
  | styled-heavy.vt | 377.8 ± 7.5  | 325.9 ± 5.9  | 1.16x   |
  | styled-multi.vt | 443.5 ± 17.2 | 390.9 ± 12.6 | 1.13x   |
  | ascii.vt        | 73.6 ± 2.0   | 72.9 ± 2.2   | 1.01x   |
  | styled-mixed.vt | 1088 ± 8     | 1084 ± 9     | 1.00x   |
  | utf8.vt         | 580.9 ± 20.3 | 579.0 ± 26.1 | 1.00x   |
  | styled-plain.vt | 112.6 ± 2.6  | 112.4 ± 3.6  | 1.00x   |
  | osc.vt          | 2256 ± 31    | 2258 ± 32    | 1.00x   |
  
  `ghostty-bench +screen-clone` at 120x80, with 1 MiB of styled-heavy
  output:
  
  | Mode          | main (ms)    | This PR (ms)   | Speedup |
  | ------------- | ------------ | ------------ | ------- |
  | render-scroll | 561.3 ± 21.0 | 424.9 ± 23.3 | 1.32x   |
  | render        | 342.3 ± 9.7  | 312.4 ± 6.0  | 1.10x   |
  
  AI disclosure: Developed with Claude Code (Opus 5.5) and OpenCode (GPT
  6.1 Sol), including profiling and codegen experiments.
  ```
- [`298f8ec`](https://github.com/ghostty-org/ghostty/commit/298f8ecb9cd30471da7bca9933335e496a5882d1) terminal: size the hyperlink map independently of the hyperlink set ([#15028](https://github.com/ghostty-org/ghostty/issues/15028)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A page's hyperlink map is now sized by its own capacity field,
  `hyperlink_cells`, instead of being derived from the hyperlink set's
  byte capacity. We previously derived it from bytes and were usually
  wasting bytes.
  
  The point of this change is primarily MEMORY DENSITY. We now get more
  rows/MB since our page structure isn't wasting as much. And more rows/MB
  means less page growths! See benchmarks below.
  
  The snapshot format is unchanged. The PAGE header's single hyperlink
  capacity hint now covers both tables (the larger of the set bytes and
  the map's equivalent in set items), so old snapshots decode to the same
  layout as before and new snapshots stay readable by current readers. I
  made that as a choice to avoid breaking snapshots. Snapshots don't need
  perfect decode and its not super important for performance there.
  
  `ghostty-bench +terminal-stream`:
  
  | Input | Size | main (ms) | hyperlink-map-size (ms) | Speedup |
  | --------------- | ------- | ------------ | ----------------------- |
  ------- |
  | hyperlinks.vt | 215x215 | 61.8 ± 1.3 | 44.7 ± 0.5 | 1.38x |
  | hyperlinks.vt | 120x80 | 53.7 ± 0.3 | 43.5 ± 0.3 | 1.23x |
  | osc.vt | 120x80 | 1129.0 ± 2.2 | 978.8 ± 4.2 | 1.15x |
  | osc.vt | 215x215 | 1097.4 ± 6.7 | 1012.8 ± 4.0 | 1.08x |
  | alternating.vt | 120x80 | 163.8 ± 3.3 | 151.8 ± 0.9 | 1.08x |
  | burst.vt | 120x80 | 73.8 ± 0.6 | 68.9 ± 0.4 | 1.07x |
  | styled-mixed.vt | 120x80 | 575.0 ± 2.1 | 580.1 ± 4.6 | 0.99x |
  | styled-heavy.vt | 120x80 | 230.5 ± 0.2 | 230.5 ± 0.6 | 1.00x |
  | ascii.vt | 120x80 | 40.4 ± 0.3 | 40.5 ± 0.1 | 1.00x |
  | utf8.vt | 120x80 | 382.0 ± 0.9 | 386.0 ± 5.0 | 0.99x |
  | erase.vt | 120x80 | 50.1 ± 0.1 | 50.8 ± 0.1 | 0.99x |
  
  The speedups come from fewer page clones (osc.vt at 120x80 went from 232
  capacity growths to 62) and from pages staying in the pool instead of
  being allocated on the heap. So this helps in general.
  
  Now memory. At a 10 MB scrollback limit at 120x80:
  
  | Input          | Heap pages   | History rows | Rows/MiB   |
  | -------------- | ------------ | ------------ | ---------- |
  | osc.vt         | 2157 -> 328  | 5625 -> 6507 | 624 -> 694 |
  | hyperlinks.vt  | 520 -> 6     | 6125 -> 7262 | 681 -> 775 |
  | alternating.vt | 1088 -> 266  | 9002 -> 9032 | 948 -> 963 |
  | ascii.vt       | 0 -> 0       | 9117 -> 9117 | 972 -> 972 |
  
  **AI usage:** Tests written by Opus, main impl by me, PR desc by me.
  ```
- [`a74bd24`](https://github.com/ghostty-org/ghostty/commit/a74bd243c03301a00a480035734aa1febbab2ea1) Fix broken tests using old syntax ([@mitchellh](https://github.com/mitchellh))
- [`68750a1`](https://github.com/ghostty-org/ghostty/commit/68750a1be2b99227328a6b185ae72719dea0428f) terminal: support mixed narrow/wide in print fast path ([@mitchellh](https://github.com/mitchellh))
  ```text
  `printSlice` previously bailed out of its fast path when there was a
  width class change. It can now continue going in various circumstances,
  which is realistic since before even things like CJK/emoji + a space
  would drop out of fast path!
  
  This still has limits: zero-width codepoints, grapheme continuations,
  hyperlinked cells, insert mode and DECAWM off still fall back to the
  per-codepoint `print` path as before.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream` at 120x80:
  
  | Input           | 2027 | main (ms)   | print-mixed (ms) | Speedup |
  | --------------- | ---- | ----------- | ---------------- | ------- |
  | cjk-prose.vt    | off  | 171.9 ± 0.4 | 83.7 ± 0.3       | 2.05x   |
  | cjk-prose.vt    | on   | 178.5 ± 0.5 | 89.1 ± 0.2       | 2.00x   |
  | cjk-spaces.vt   | off  | 25.5 ± 0.1  | 15.4 ± 0.1       | 1.65x   |
  | cjk-spaces.vt   | on   | 26.3 ± 0.3  | 16.2 ± 0.1       | 1.63x   |
  | styled-uni.vt   | off  | 330.4 ± 0.8 | 219.9 ± 0.7      | 1.50x   |
  | styled-uni.vt   | on   | 367.5 ± 0.7 | 259.1 ± 0.7      | 1.42x   |
  | utf8.vt         | off  | 382.4 ± 1.0 | 313.6 ± 0.5      | 1.22x   |
  | utf8.vt         | on   | 398.8 ± 0.8 | 329.4 ± 0.4      | 1.21x   |
  | styled-mixed.vt | off  | 572.3 ± 1.6 | 504.5 ± 2.1      | 1.13x   |
  | styled-mixed.vt | on   | 599.5 ± 1.4 | 529.2 ± 0.9      | 1.13x   |
  | ascii.vt        | off  | 40.5 ± 0.1  | 40.6 ± 0.1       | 1.00x   |
  | styled-plain.vt | off  | 63.8 ± 0.5  | 63.3 ± 0.3       | 1.01x   |
  | osc.vt          | off  | 1125 ± 4    | 1122 ± 2         | 1.00x   |
  | out.txt (2.6GB) | off  | 5455 ± 177  | 5375 ± 8         | 1.01x   |
  | out.txt (2.6GB) | on   | 5399 ± 7    | 5413 ± 6         | 1.00x   |
  
  - cjk-spaces.vt is `+utf8` with only CJK ideographs and a space after 30%
    of them.
  - cjk-prose.vt mixes them with printable ASCII at a 1:0.3 weight.
  - styled-uni.vt is `+styled` with multibyte weights
  ```
- [`e2a3ba0`](https://github.com/ghostty-org/ghostty/commit/e2a3ba004d01ca1d0251c891544b97784a072c20) terminal: support mixed narrow/wide in print fast path ([#15021](https://github.com/ghostty-org/ghostty/issues/15021)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `printSlice` previously bailed out of its fast path when there was a
  width class change. It can now continue going in various circumstances,
  which is realistic since before even things like CJK/emoji + a space
  would drop out of fast path!
  
  This still has limits: zero-width codepoints, grapheme continuations,
  hyperlinked cells, insert mode and DECAWM off still fall back to the
  per-codepoint `print` path as before.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream` at 120x80:
  
  | Input           | 2027 | main (ms)   | print-mixed (ms) | Speedup |
  | --------------- | ---- | ----------- | ---------------- | ------- |
  | cjk-prose.vt    | off  | 171.9 ± 0.4 | 83.7 ± 0.3       | 2.05x   |
  | cjk-prose.vt    | on   | 178.5 ± 0.5 | 89.1 ± 0.2       | 2.00x   |
  | cjk-spaces.vt   | off  | 25.5 ± 0.1  | 15.4 ± 0.1       | 1.65x   |
  | cjk-spaces.vt   | on   | 26.3 ± 0.3  | 16.2 ± 0.1       | 1.63x   |
  | styled-uni.vt   | off  | 330.4 ± 0.8 | 219.9 ± 0.7      | 1.50x   |
  | styled-uni.vt   | on   | 367.5 ± 0.7 | 259.1 ± 0.7      | 1.42x   |
  | utf8.vt         | off  | 382.4 ± 1.0 | 313.6 ± 0.5      | 1.22x   |
  | utf8.vt         | on   | 398.8 ± 0.8 | 329.4 ± 0.4      | 1.21x   |
  | styled-mixed.vt | off  | 572.3 ± 1.6 | 504.5 ± 2.1      | 1.13x   |
  | styled-mixed.vt | on   | 599.5 ± 1.4 | 529.2 ± 0.9      | 1.13x   |
  | ascii.vt        | off  | 40.5 ± 0.1  | 40.6 ± 0.1       | 1.00x   |
  | styled-plain.vt | off  | 63.8 ± 0.5  | 63.3 ± 0.3       | 1.01x   |
  | osc.vt          | off  | 1125 ± 4    | 1122 ± 2         | 1.00x   |
  | out.txt (2.6GB) | off  | 5455 ± 177  | 5375 ± 8         | 1.01x   |
  | out.txt (2.6GB) | on   | 5399 ± 7    | 5413 ± 6         | 1.00x   |
  
  - cjk-spaces.vt is `+utf8` with only CJK ideographs and a space after
  30% of them.
  - cjk-prose.vt mixes them with printable ASCII at a 1:0.3 weight.
  - styled-uni.vt is `+styled` with multibyte weights
  
  **AI usage:** I had the initial idea, but my work gained a 30% speedup.
  Upon an adversarial review with Fable, it identified some register
  spilling and branch mispredicts that were eating huge cost and reworked
  it (to the mixed row loop now), which I understood/reviewed and accept.
  I wrote all the human language.
  ```
- [`825f31c`](https://github.com/ghostty-org/ghostty/commit/825f31c5201e5f6144ac9267d459e64740e4c456) Update VOUCHED list ([#15022](https://github.com/ghostty-org/ghostty/issues/15022)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/15020#discussioncomment-19356061)
  from @jcollie.
  
  Vouch: @yinxiangshi
  ```
- [`379bdfa`](https://github.com/ghostty-org/ghostty/commit/379bdfabffe16b6a326c4289ad2bf9d712cce80a) Update VOUCHED list ([#15016](https://github.com/ghostty-org/ghostty/issues/15016)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/15015#discussioncomment-19355011)
  from @jcollie.
  
  Vouch: @arc-source-coder
  ```
- [`9113da0`](https://github.com/ghostty-org/ghostty/commit/9113da029815076cefbbc1ea7b1f63e8082e09ea) terminal: project hyperlink and string capacity when growing a page ([@mitchellh](https://github.com/mitchellh))
  ```text
  `PageList.increaseCapacity` now projects hyperlink and string capacity
  from the page's current usage, the same way it has for styles and
  graphemes since #13826. A page that runs out of hyperlink or string
  space grows once to about what the whole page will need, instead of
  doubling over and over.
  
  Previously, hyperlinks and strings always doubled. Hyperlink capacity
  starts at only 4 links, so a page with a unique link on every row (such
  as `ls --hyperlink`) grew its hyperlink capacity 8 times. Every growth
  is a full page allocation and copy.
  
  `ghostty-bench +terminal-stream` at 120x80:
  
  | Input              | main (ms)    | grow-hyperlink (ms) | Speedup |
  | ------------------ | ------------ | ------------------- | ------- |
  | alternating.vt     | 471.5 ± 5.5  | 410.2 ± 1.3         | 1.15x   |
  | osc.vt             | 1177 ± 47    | 1126 ± 29           | 1.04x   |
  | burst.vt           | 125.2 ± 0.4  | 123.3 ± 0.4         | 1.02x   |
  | styled-mixed.vt    | 577.3 ± 3.0  | 575.2 ± 3.1         | 1.00x   |
  | erase.vt           | 359.7        | 357.9               | 1.01x   |
  | ascii.vt           | 41.5         | 41.4                | 1.00x   |
  | styled-heavy.vt    | 246.5 ± 1.4  | 246.7 ± 0.9         | 1.00x   |
  | utf8.vt            | 408.7 ± 1.7  | 408.0 ± 1.2         | 1.00x   |
  | out.txt (2.6GB)    | 5734 ± 49    | 5553 ± 173          | 1.03x   |
  
  In the real world, this is a small win. A unique link per row is what
  `ls --hyperlink` and some compilers produce, but most output doesn't
  look like that. Its important it doesn't regress other workoads.
  ```
- [`f0d8cb7`](https://github.com/ghostty-org/ghostty/commit/f0d8cb776254f5dec58b353811398c60fff2fd86) terminal: carried pages compare usage per row ([@mitchellh](https://github.com/mitchellh))
  ```text
  When a carried page has fewer rows than the standard so that it fits in
  a pool item, `grow` now scales its usage up to the standard row count
  before deciding what capacity the next page keeps.
  
  Previously, a trimmed page looked emptier than it really was, so the next
  page shrank its jcapacity, ran out of room, and had to grow by copying itself.
  
  This is a follow-up fix to carried pages from #14985:
  https://github.com/ghostty-org/ghostty/pull/14985
  
  In the real world I think this would be a pretty edge case scenario but
  it was something I saw that bothered me.
  
  `ghostty-bench +terminal-stream`:
  
  | Input           | Size   | main (ms)    | fix (ms)     | Speedup |
  | --------------- | ------ | ------------ | ------------ | ------- |
  | cycle.vt        | 80x24  | 234.2 ± 4.9  | 144.1 ± 4.6  | 1.63x   |
  | styled-mixed.vt | 120x80 | 583.4 ± 3.2  | 582.4 ± 2.1  | 1.00x   |
  | styled-mixed.vt | 30x24  | 630.2 ± 2.3  | 631.6 ± 3.1  | 1.00x   |
  | osc.vt          | 120x80 | 1152.2 ± 9.7 | 1158.2 ± 5.1 | 0.99x   |
  | burst.vt        | 120x80 | 76.4 ± 1.0   | 76.5 ± 0.7   | 1.00x   |
  | alternating.vt  | 120x80 | 177.8 ± 2.5  | 178.8 ± 2.4  | 0.99x   |
  | styled-heavy.vt | 120x80 | 240.8 ± 0.9  | 241.6 ± 2.1  | 1.00x   |
  | utf8.vt         | 120x80 | 384.2 ± 0.8  | 384.0 ± 1.0  | 1.00x   |
  | ascii.vt        | 120x80 | 41.9 ± 0.1   | 41.8 ± 0.3   | 1.00x   |
  ```
- [`431d003`](https://github.com/ghostty-org/ghostty/commit/431d003c44e857f7ce273e3e209c9daac8eee85e) terminal: project hyperlink and string capacity when growing a page ([#15012](https://github.com/ghostty-org/ghostty/issues/15012)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `PageList.increaseCapacity` now projects hyperlink and string capacity
  from the page's current usage, the same way it has for styles and
  graphemes since #13826. A page that runs out of hyperlink or string
  space grows once to about what the whole page will need, instead of
  doubling over and over.
  
  Previously, hyperlinks and strings always doubled. Hyperlink capacity
  starts at only 4 links, so a page with a unique link on every row (such
  as `ls --hyperlink`) grew its hyperlink capacity 8 times. Every growth
  is a full page allocation and copy.
  
  `ghostty-bench +terminal-stream` at 120x80:
  
  | Input              | main (ms)    | grow-hyperlink (ms) | Speedup |
  | ------------------ | ------------ | ------------------- | ------- |
  | alternating.vt     | 471.5 ± 5.5  | 410.2 ± 1.3         | 1.15x   |
  | osc.vt             | 1177 ± 47    | 1126 ± 29           | 1.04x   |
  | burst.vt           | 125.2 ± 0.4  | 123.3 ± 0.4         | 1.02x   |
  | styled-mixed.vt    | 577.3 ± 3.0  | 575.2 ± 3.1         | 1.00x   |
  | erase.vt           | 359.7        | 357.9               | 1.01x   |
  | ascii.vt           | 41.5         | 41.4                | 1.00x   |
  | styled-heavy.vt    | 246.5 ± 1.4  | 246.7 ± 0.9         | 1.00x   |
  | utf8.vt            | 408.7 ± 1.7  | 408.0 ± 1.2         | 1.00x   |
  | out.txt (2.6GB)    | 5734 ± 49    | 5553 ± 173          | 1.03x   |
  
  In the real world, this is a small win. A unique link per row is what
  `ls --hyperlink` and some compilers produce, but most output doesn't
  look like that. Its important it doesn't regress other workoads.
  
  **AI usage:** Opus for tests, benchmarking, validation. Meat brain for
  impl and this PR desc.
  ```
- [`7b267cd`](https://github.com/ghostty-org/ghostty/commit/7b267cd9ac7863b0bd72e808daa021381e72dc21) terminal: carried pages compare usage per row ([#15013](https://github.com/ghostty-org/ghostty/issues/15013)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  When a carried page has fewer rows than the standard so that it fits in
  a pool item, `grow` now scales its usage up to the standard row count
  before deciding what capacity the next page keeps.
  
  Previously, a trimmed page looked emptier than it really was, so the
  next page shrank its jcapacity, ran out of room, and had to grow by
  copying itself.
  
  This is a follow-up fix to carried pages from #14985:
  https://github.com/ghostty-org/ghostty/pull/14985
  
  In the real world I think this would be a pretty edge case scenario but
  it was something I saw that bothered me.
  
  `ghostty-bench +terminal-stream`:
  
  | Input           | Size   | main (ms)    | fix (ms)     | Speedup |
  | --------------- | ------ | ------------ | ------------ | ------- |
  | cycle.vt        | 80x24  | 234.2 ± 4.9  | 144.1 ± 4.6  | 1.63x   |
  | styled-mixed.vt | 120x80 | 583.4 ± 3.2  | 582.4 ± 2.1  | 1.00x   |
  | styled-mixed.vt | 30x24  | 630.2 ± 2.3  | 631.6 ± 3.1  | 1.00x   |
  | osc.vt          | 120x80 | 1152.2 ± 9.7 | 1158.2 ± 5.1 | 0.99x   |
  | burst.vt        | 120x80 | 76.4 ± 1.0   | 76.5 ± 0.7   | 1.00x   |
  | alternating.vt  | 120x80 | 177.8 ± 2.5  | 178.8 ± 2.4  | 0.99x   |
  | styled-heavy.vt | 120x80 | 240.8 ± 0.9  | 241.6 ± 2.1  | 1.00x   |
  | utf8.vt         | 120x80 | 384.2 ± 0.8  | 384.0 ± 1.0  | 1.00x   |
  | ascii.vt        | 120x80 | 41.9 ± 0.1   | 41.8 ± 0.3   | 1.00x   |
  
  EDIT: The `cycle.vt` input shape was one chosen particularly to exercise
  the grow/shrink issue I saw. Its not representative of real world data.
  
  **AI usage:** I saw the problem and came up with the idea to resolve it,
  deferred to Opus for impl, testing, validation. I reviewed.
  ```
- [`0d4418a`](https://github.com/ghostty-org/ghostty/commit/0d4418ac20922475ebb40ef23a666898bbc91b67) terminal: fix edge cases in carried page capacity ([@mitchellh](https://github.com/mitchellh))
  ```text
  Found a few bugs from #14985:
  
    - The rows per byte check that decides whether a carried page may
      trim rows to fit in the pool overflowed on 32-bit targets (i.e. wasm32)
      for terminals narrower than about 37 columns.
    - `grow_hint` was updated before the new page was allocated. If
      allocation failed this caused problems.
    - On tall terminals at the minimum scrollback size, pages with
      trimmed rows hold less of the active area, so the page list could
      go over the byte limit during a burst of styled output.
  
  These are all correctness fixes with no performance impact.
  ```
- [`4747d7f`](https://github.com/ghostty-org/ghostty/commit/4747d7ff427480f75736dc207d14251b8eabd3c9) terminal: fix edge cases in carried page capacity ([#15005](https://github.com/ghostty-org/ghostty/issues/15005)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Found a few bugs from #14985:
  
  - The rows per byte check that decides whether a carried page may trim
  rows to fit in the pool overflowed on 32-bit targets (i.e. wasm32) for
  terminals narrower than about 37 columns.
  - `grow_hint` was updated before the new page was allocated. If
  allocation failed this caused problems.
  - On tall terminals at the minimum scrollback size, pages with trimmed
  rows hold less of the active area, so the page list could go over the
  byte limit during a burst of styled output.
  
  These are all correctness fixes with no performance impact.
  
  **AI stuff:** I found the first two issues, Fable found the last, Opus
  did the bug fixes and I reviewed.
  ```
- [`f7b25c8`](https://github.com/ghostty-org/ghostty/commit/f7b25c8129d84d53cf0cda4ffa024a692aca019e) termio: don't require RFC 1123 hostnames in OSC 7 ([@jcollie](https://github.com/jcollie))
  ```text
  The Zig 0.17 port switched reportPwd from `uri.getHost` to
  `std.Io.net.HostName.fromUri`, which also validates the host as an
  RFC 1123 hostname. Local hostnames often aren't: macOS allows names
  like "Foo's MacBook Pro", some systems use underscores, and our URI
  parser deliberately accepts MAC addresses. Any OSC 7 report from such
  a machine was dropped, so new tabs, splits and windows stopped
  inheriting the working directory.
  
  The host only has to match the local hostname, which `isLocal` already
  checks, so extract it without validating it, as 1.3 did.
  
  Fixes: #14970
  Ref: https://github.com/ghostty-org/ghostty/discussions/14952
  ```
- [`881fc68`](https://github.com/ghostty-org/ghostty/commit/881fc68902a5d819fdac96bcb597a2d99feb9729) terminal: skip clearing rows that are already blank ([@mitchellh](https://github.com/mitchellh))
  ```text
  Erase display (ED, `CSI J`) now skips rows that are already blank instead
  of clearing them again. On a mostly empty screen, full-screen erases are
  now 2x to 14x faster depending on screen size. Plain text and scrolling
  are unaffected.
  
  Programs that redraw by clearing (shells redrawing prompts, `clear`,
  `watch`, TUIs) usually erase a screen that is mostly empty already.
  Previously, every erase cleared every row cell by cell anyway, even
  when the cells were already zero.
  
  ## How
  
  Rows get a new `blank` bit, taken from the row's padding. It is set when
  a whole row is cleared with a zero blank cell and cleared by anything
  that writes cells. `clearRows` sees the bit and only resets the row's
  metadata, leaving the cells alone. Skipped rows aren't marked dirty
  because nothing about how they look changed.
  
  The bit is a hint that can be false for a blank row but never true for
  a row with content. We verify this with integrity checks.
  
  The tricky part was not slowing down printing. My first attempt cleared
  the bit whenever a row was marked dirty, which happens on every cursor
  move, and made scrolling about 3% slower. Now `writeCell` clears it,
  which also covers the spacer head a wide char writes before it wraps.
  `Row.markWritten` sets dirty and clears blank in one load and store,
  because doing them separately was measurable on the print path.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream`:
  
  | Input           | Size    | main (ms)    | blank-track (ms) | Speedup |
  | --------------- | ------- | ------------ | ---------------- | ------- |
  | erase.vt        | 120x80  | 362.6 ± 1.1  | 49.9 ± 0.1       | 7.27x   |
  | erase.vt        | 120x12  | 89.0 ± 0.3   | 49.0 ± 0.3       | 1.82x   |
  | erase.vt        | 300x100 | 1149 ± 16    | 82.6 ± 0.2       | 13.91x  |
  | ascii.vt        | 120x80  | 40.6 ± 0.2   | 40.5 ± 0.2       | 1.00x   |
  | styled-plain.vt | 120x80  | 64.1 ± 0.5   | 63.5 ± 0.5       | 1.01x   |
  | styled-mixed.vt | 120x80  | 576.0 ± 1.6  | 579.7 ± 5.9      | 0.99x   |
  | utf8.vt         | 120x80  | 380.5 ± 2.3  | 386.5 ± 6.5      | 0.98x   |
  | osc.vt          | 120x80  | 1142 ± 5     | 1140 ± 3         | 1.00x   |
  | out.txt (2.6GB) | 120x80  | 5911         | 5589             | 1.06x   |
  
  `out.txt` is the asciinema data dump, a real world workload. It gets
  faster because real sessions erase a lot! The vtebench vim inputs are
  1 to 2% faster for the same reason. The vtebench scrolling inputs are
  unchanged. utf8.vt looks 2% slower but it is noisy, and it executes
  only 0.3% more instructions, so this is probably noise.
  ```
- [`fd29936`](https://github.com/ghostty-org/ghostty/commit/fd29936f0914f5a303e1d67fd09201f981b7eff1) macos: make Surface main actor-isolated ([@jparise](https://github.com/jparise))
  ```text
  Calls into libghostty must happen on the main actor, and nearly every
  Surface function was already annotated with `@MainActor`.
  
  Main actor isolation makes the class implicitly Sendable, so the
  explicit conformance goes away. `deinit` remains `nonisolated`, so the
  surface handle stays `nonisolated(unsafe)` for it to read the value and
  hand it to the main actor to be freed.
  ```
- [`6573de6`](https://github.com/ghostty-org/ghostty/commit/6573de67e9990ebf0308f5cb07e4e40895d748ec) Replace std.ArrayListUnmanaged and std.ArrayListAligned ([@jcollie](https://github.com/jcollie))
  ```text
  Both are deprecated aliases in Zig 0.17: std.ArrayListUnmanaged is
  std.ArrayList, which has been unmanaged since 0.15, and
  std.ArrayListAligned is std.array_list.Aligned. Zig 0.18 removes them,
  so use the names they alias. No behavior change.
  ```
- [`2178e63`](https://github.com/ghostty-org/ghostty/commit/2178e635dffc71e0c679b143680665bf09857bb8) terminal: mark reset rows blank and test the blank bit bookkeeping ([@mitchellh](https://github.com/mitchellh))
- [`59093e3`](https://github.com/ghostty-org/ghostty/commit/59093e3aadb1478e6642061059b1882cfa1b6cf3) terminal: skip clearing rows that are already blank ([#14997](https://github.com/ghostty-org/ghostty/issues/14997)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Erase display (ED, `CSI J`) now skips rows that are already blank
  instead of clearing them again. On a mostly empty screen, full-screen
  erases are now 2x to 14x faster depending on screen size. Plain text and
  scrolling are unaffected.
  
  Programs that redraw by clearing (shells redrawing prompts, `clear`,
  `watch`, TUIs) usually erase a screen that is mostly empty already.
  Previously, every erase cleared every row cell by cell anyway, even when
  the cells were already zero.
  
  ## How
  
  Rows get a new `blank` bit, taken from the row's padding. It is set when
  a whole row is cleared with a zero blank cell and cleared by anything
  that writes cells. `clearRows` sees the bit and only resets the row's
  metadata, leaving the cells alone. Skipped rows aren't marked dirty
  because nothing about how they look changed.
  
  The bit is a hint that can be false for a blank row but never true for a
  row with content. We verify this with integrity checks.
  
  The tricky part was not slowing down printing. My first attempt cleared
  the bit whenever a row was marked dirty, which happens on every cursor
  move, and made scrolling about 3% slower. Now `writeCell` clears it,
  which also covers the spacer head a wide char writes before it wraps.
  `Row.markWritten` sets dirty and clears blank in one load and store,
  because doing them separately was measurable on the print path.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream`:
  
  | Input | Size | main (ms) | blank-track (ms) | Speedup |
  | --------------- | ------- | ------------ | ---------------- | -------
  |
  | erase.vt | 120x80 | 362.6 ± 1.1 | 49.9 ± 0.1 | 7.27x |
  | erase.vt | 120x12 | 89.0 ± 0.3 | 49.0 ± 0.3 | 1.82x |
  | erase.vt | 300x100 | 1149 ± 16 | 82.6 ± 0.2 | 13.91x |
  | ascii.vt | 120x80 | 40.6 ± 0.2 | 40.5 ± 0.2 | 1.00x |
  | styled-plain.vt | 120x80 | 64.1 ± 0.5 | 63.5 ± 0.5 | 1.01x |
  | styled-mixed.vt | 120x80 | 576.0 ± 1.6 | 579.7 ± 5.9 | 0.99x |
  | utf8.vt | 120x80 | 380.5 ± 2.3 | 386.5 ± 6.5 | 0.98x |
  | osc.vt | 120x80 | 1142 ± 5 | 1140 ± 3 | 1.00x |
  | out.txt (2.6GB) | 120x80 | 5911 | 5589 | 1.06x |
  
  `out.txt` is the asciinema data dump, a real world workload. It gets
  faster because real sessions erase a lot! The vtebench vim inputs are 1
  to 2% faster for the same reason. The vtebench scrolling inputs are
  unchanged. utf8.vt looks 2% slower but it is noisy, and it executes only
  0.3% more instructions, so this is probably noise.
  
  **AI usage:** I came up with the change, Opus helped with benchmarking
  and validating, I wrote the text. Fable helped come up with an alternate
  idea for my original design which had the 3% slowdown :(
  ```
- [`ada6e3d`](https://github.com/ghostty-org/ghostty/commit/ada6e3d722fde00e7171e2d4e93c7392052f2720) Replace std.ArrayListUnmanaged and std.ArrayListAligned ([#15001](https://github.com/ghostty-org/ghostty/issues/15001)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Both are deprecated aliases in Zig 0.17: std.ArrayListUnmanaged is
  std.ArrayList, which has been unmanaged since 0.15, and
  std.ArrayListAligned is std.array_list.Aligned. Zig 0.18 removes them,
  so use the names they alias. No behavior change.
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`5c6d43e`](https://github.com/ghostty-org/ghostty/commit/5c6d43eeecaf4eff506a96d0f5310b5682c80c88) macos: make Surface main actor-isolated ([#14999](https://github.com/ghostty-org/ghostty/issues/14999)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Calls into libghostty must happen on the main actor, and nearly every
  Surface function was already annotated with `@MainActor`.
  
  Main actor isolation makes the class implicitly Sendable, so the
  explicit conformance goes away. `deinit` remains `nonisolated`, so the
  surface handle stays `nonisolated(unsafe)` for it to read the value and
  hand it to the main actor to be freed.
  ```
- [`042b16b`](https://github.com/ghostty-org/ghostty/commit/042b16b6146ada29877dfeeea9f286889e4adeb1) termio: don't require RFC 1123 hostnames in OSC 7 ([#14971](https://github.com/ghostty-org/ghostty/issues/14971)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The Zig 0.17 port switched reportPwd from `uri.getHost` to
  `std.Io.net.HostName.fromUri`, which also validates the host as an RFC
  1123 hostname. Local hostnames often aren't: macOS allows names like
  "Foo's MacBook Pro", some systems use underscores, and our URI parser
  deliberately accepts MAC addresses. Any OSC 7 report from such a machine
  was dropped, so new tabs, splits and windows stopped inheriting the
  working directory.
  
  The host only has to match the local hostname, which `isLocal` already
  checks, so extract it without validating it, as 1.3 did.
  
  Fixes: #14970
  Ref: https://github.com/ghostty-org/ghostty/discussions/14952
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`7cd6fa0`](https://github.com/ghostty-org/ghostty/commit/7cd6fa0215a1299c69c27fe543f48ecab45b775f) Sync CODEOWNERS vouch list ([#15002](https://github.com/ghostty-org/ghostty/issues/15002)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Sync CODEOWNERS owners with vouch list.
  
  ## Added Users
  
  - @mangkoran
  ```

