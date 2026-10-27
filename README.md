> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: October 27, 2026 at 21:44 UTC.

## October 27, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/40584098988), [2](https://github.com/ghostty-org/ghostty/actions/runs/40568497398), [3](https://github.com/ghostty-org/ghostty/actions/runs/40546649739), [4](https://github.com/ghostty-org/ghostty/actions/runs/40541589904), [5](https://github.com/ghostty-org/ghostty/actions/runs/40535055733), [6](https://github.com/ghostty-org/ghostty/actions/runs/40526449383), [7](https://github.com/ghostty-org/ghostty/actions/runs/40450332918)  
Summary: 7 runs • 19 commits • 6 authors

### Changes

- [`5c1d15f`](https://github.com/ghostty-org/ghostty/commit/5c1d15f9b571982afe4376e8cb38b6f3fbb52bc0) config: prevent panic on truncated UTF-8 ([@12ya](https://github.com/12ya))
  ```text
  #14879
  
  Check that the full UTF-8 sequence is available before slicing it so
  truncated configuration strings return InvalidString instead of panicking.
  Cover incomplete two-, three-, and four-byte sequences and verify that
  SelectionWordChars.parseCLI reports InvalidValue.
  ```
- [`46e9dc9`](https://github.com/ghostty-org/ghostty/commit/46e9dc9a927b2e7e7cba79e6902c176127dbdf2c) config: prevent panic on truncated UTF-8 ([#14879](https://github.com/ghostty-org/ghostty/issues/14879)) ([@jcollie](https://github.com/jcollie))
  ```text
  `CodepointIterator` could panic on incomplete UTF-8, such as a lone 0xC2
  byte, when slicing beyond the available input.
  
  Check the remaining byte count before slicing and return `InvalidString`
  for truncated sequences. Test incomplete two-, three-, and four-byte
  sequences in the iterator and `SelectionWordChars.parseCLI`.
  
  Validation:
  - `zig build test -Dtest-filter=SelectionWordChars
  -Dtest-filter=codepointIterator -Demit-macos-app=false`: 91 tests
  passed.
  - Standalone string helper tests: 13 passed.
  - Formatting and whitespace checks passed.
  
  AI disclosure: OpenAI Codex assisted with the code, tests, and PR
  description.
  ```
- [`241a7bc`](https://github.com/ghostty-org/ghostty/commit/241a7bca3b14fa3a136dfb9860eb0d9d183bb3f4) cli: fix Unicode escape validation ([@12ya](https://github.com/12ya))
  ```text
  #14876
  
  Interpret hexadecimal letters as 10 through 15 when checking Unicode
  escapes so oversized values are rejected.
  
  Cover lowercase and uppercase letters in quoted and unquoted escapes.
  Run quoted cases on every platform.
  ```
- [`b84594f`](https://github.com/ghostty-org/ghostty/commit/b84594f9783e9ca924ba7c703ab7d633b38c4bbe) build: fix the snap and flatpak builds ([@mitchellh](https://github.com/mitchellh))
  ```text
  These have been broken since Zig 0.17, I think snap since before that.
  
  The snap moves to core26 (Ubuntu 26.04), which ships new enough GTK,
  libadwaita, and harfbuzz. It also uses the system gtk4-layer-shell now
  that Ubuntu packages it, and redirects `-lbzip2` to `libbz2.so` with a
  one-line linker script, the same way the flatpak already does.
  ```
- [`b840b24`](https://github.com/ghostty-org/ghostty/commit/b840b2457cc0f5ee63cb324b3af9bb8e753e512c) cli: fix Unicode escape validation ([#14876](https://github.com/ghostty-org/ghostty/issues/14876)) ([@jcollie](https://github.com/jcollie))
  ```text
  Fix hexadecimal letter conversion in CommaSplitter's Unicode escape
  validation. Letters a-f and A-F were interpreted as 0-5 instead of
  10-15, allowing oversized escapes such as \u{aaaaaa} to pass validation.
  
  Add regression tests for lowercase and uppercase escapes.
  
  Validation:
  - Standalone tests: 27 passed, 3 Windows tests skipped.
  - Formatting: passed.
  
  AI assistance: Used OpenAI Codex for diagnosis, explanations, code/test
  suggestions, validation, and PR wording.
  ```
- [`919dca5`](https://github.com/ghostty-org/ghostty/commit/919dca5c848d43a489a4cb2e1feade016f0fa2db) build: fix the snap and flatpak builds ([#14881](https://github.com/ghostty-org/ghostty/issues/14881)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  These have been broken since Zig 0.17, I think snap since before that.
  
  The snap moves to core26 (Ubuntu 26.04), which ships new enough GTK,
  libadwaita, and harfbuzz. It also uses the system gtk4-layer-shell now
  that Ubuntu packages it, and redirects `-lbzip2` to `libbz2.so` with a
  one-line linker script, the same way the flatpak already does.
  ```
- [`4a4fc01`](https://github.com/ghostty-org/ghostty/commit/4a4fc017940bec38c93b278c10c6a18c591f3e63) up to 1.4.1-dev ([@mitchellh](https://github.com/mitchellh))
- [`83fb956`](https://github.com/ghostty-org/ghostty/commit/83fb95624b0439ee660c2679b43b38c8b63769cd) Bump version to 1.4.0 ([@mitchellh](https://github.com/mitchellh))
- [`155bbbe`](https://github.com/ghostty-org/ghostty/commit/155bbbe5343d6579a20121673702937cee96572f) i18n: polish the Polish ([@Rayzerrek](https://github.com/Rayzerrek))
- [`d87c497`](https://github.com/ghostty-org/ghostty/commit/d87c497aff312f8bfcaeffbb53813dcccea4492b) i18n: polish the Polish ([#14874](https://github.com/ghostty-org/ghostty/issues/14874)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Picked from #14598
  ```
- [`c46e292`](https://github.com/ghostty-org/ghostty/commit/c46e292eda4fb217fbbc2763a7ed6f73f04db4de) Update VOUCHED list ([#14878](https://github.com/ghostty-org/ghostty/issues/14878)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14877#discussioncomment-19221073)
  from @jcollie.
  
  Vouch: @rtgibbons
  ```
- [`f9c3b20`](https://github.com/ghostty-org/ghostty/commit/f9c3b20f7ecb8fe145e595469b62841c8fe5cb7d) macOS: increase test coverage for NSPasteboard ([@francislata](https://github.com/francislata))
- [`a732580`](https://github.com/ghostty-org/ghostty/commit/a7325808ad17249b356824102c4c0e917352b686) macOS: increase test coverage for NSPasteboard ([#14870](https://github.com/ghostty-org/ghostty/issues/14870)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Picked and amended from #14868
  ```
- [`99dae4d`](https://github.com/ghostty-org/ghostty/commit/99dae4d8700a63040b4131a5b43bf7f50d5d13d8) ci: add freebsd builds for libghostty-vt ([@mitchellh](https://github.com/mitchellh))
- [`445e234`](https://github.com/ghostty-org/ghostty/commit/445e23496414d870a0407d145b285381fc031bc1) some freebsd fixes ([@mitchellh](https://github.com/mitchellh))
- [`f13b528`](https://github.com/ghostty-org/ghostty/commit/f13b52851a744f14cb22101dc29d78babdc6e656) terminal: memory decommit/recommit for FreeBSD ([@mitchellh](https://github.com/mitchellh))
- [`4d429ec`](https://github.com/ghostty-org/ghostty/commit/4d429ecfdeed4e08473602a3071fda897cd18a39) ci: run libghostty-vt tests in CI ([@mitchellh](https://github.com/mitchellh))
- [`1b9bb3a`](https://github.com/ghostty-org/ghostty/commit/1b9bb3aeb1236e2151539c695fbb03e171fe1e4c) build: -Demit-test-exe only emits the libghostty c tests for libghostty ([@mitchellh](https://github.com/mitchellh))
- [`68640f3`](https://github.com/ghostty-org/ghostty/commit/68640f3049d5ae76d7d5eebb5bbdf713a3a98713) libghostty-vt: support FreeBSD, test in CI ([#14867](https://github.com/ghostty-org/ghostty/issues/14867)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds support for FreeBSD to libghostty-vt and validates it in CI.
  
  There were only a few places we really need to make compatibility fixes:
  
  - The memory decommit/recommit stuff, which is very OS specific.
  - Kitty graphics shared memory paths
  - TinyIO, one method
  ```

## October 26, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/40396684066), [2](https://github.com/ghostty-org/ghostty/actions/runs/40393630080), [3](https://github.com/ghostty-org/ghostty/actions/runs/40389935061), [4](https://github.com/ghostty-org/ghostty/actions/runs/40364482308), [5](https://github.com/ghostty-org/ghostty/actions/runs/40361578719), [6](https://github.com/ghostty-org/ghostty/actions/runs/40359380687), [7](https://github.com/ghostty-org/ghostty/actions/runs/40330121151), [8](https://github.com/ghostty-org/ghostty/actions/runs/40267247680), [9](https://github.com/ghostty-org/ghostty/actions/runs/40259139232)  
Summary: 9 runs • 38 commits • 9 authors

### Changes

- [`9ee02ae`](https://github.com/ghostty-org/ghostty/commit/9ee02ae601d3eec567723287e1c20bd0e9f1489c) i18n: Irish translation for Ghostty 1.4 ([#13837](https://github.com/ghostty-org/ghostty/issues/13837)) ([@aindriu80](https://github.com/aindriu80))
- [`afbbbe1`](https://github.com/ghostty-org/ghostty/commit/afbbbe15887c8a83db9c3f1df30411bbfff87bd0) macos/applescript: add AppleScript name override property ([@paaloeye](https://github.com/paaloeye))
  ````text
  - expose read-write `name override` property on tab and terminal classes in Ghostty.sdef
  - implement `titleOverride` accessors in `ScriptTab` and `ScriptTerminal`
  - add `titleOverride` property to `SurfaceView` to manage manual terminal title overrides
  - fix minor inconsistencies in comments
  
  AppleScript API usage:
  
  ```applescript
  -- Setting and clearing a tab name override via AppleScript
  tell application "Ghostty"
      -- Target the selected tab of the front window
      set targetTab to selected tab of front window
  
      -- Set name override
      set name override of targetTab to "My Custom Tab Title"
      log "Tab title: " & (name of targetTab)
      log "Tab override: " & (name override of targetTab)
      delay 2.0 -- delay is here only for illustrative purposes
  
      -- Clear override
      set name override of targetTab to ""
  end tell
  ```
  
  AI disclosure: Antigravity CLI was used for the first draft. Iterated, minimised, reviewed, and tested by me.
  
  Closes: https://github.com/ghostty-org/ghostty/issues/12048
  Discussion: https://github.com/ghostty-org/ghostty/discussions/12047
  Agent-Session: cdd11bbe-928a-4a00-a085-c8f87a57966f
  ````
- [`b279b2c`](https://github.com/ghostty-org/ghostty/commit/b279b2ccb8f6d7bb86afa44bd5bf5529c29fdce0) macos: clear split zoom indicator when tree is not split ([@paaloeye](https://github.com/paaloeye))
  ```text
  When closing sibling splits down to a single terminal leaf while
  zoomed via AppleScript, `SplitTree` retained its zoomed node
  reference because the target being removed was not the zoomed node itself.
  
  Because the tree was no longer split but the zoomed property remained non-nil,
  the window's zoom state stayed active and the reset zoom indicator remained visible.
  
  `SplitTree` now validates that a tree can only have a zoomed node if
  it actually contains splits and the zoomed node exists in root. In
  addition, `SplitTree` exposes an `isZoomed` property, and the terminal
  controller and window reactively update the zoom state and accessory
  controls accordingly.
  
  AI disclosure: Antigravity CLI wrote the tests initially. Iterated, reviewed, and tested by me.
  ```
- [`91d198c`](https://github.com/ghostty-org/ghostty/commit/91d198cc32b6056fede5625e0c60302d01bbb846) macos/applescript: add AppleScript name override property ([#14733](https://github.com/ghostty-org/ghostty/issues/14733)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  - expose read-write `name override` property on tab and terminal classes
  in Ghostty.sdef
  - implement `titleOverride` accessors in `ScriptTab` and
  `ScriptTerminal`
  - add `titleOverride` property to `SurfaceView` to manage manual
  terminal title overrides
  - fix minor inconsistencies in comments
  
  AppleScript API usage:
  
  ```applescript
  -- Setting and clearing a tab name override via AppleScript
  tell application "Ghostty"
      -- Target the selected tab of the front window
      set targetTab to selected tab of front window
  
      -- Set name override
      set name override of targetTab to "My Custom Tab Title"
      log "Tab title: " & (name of targetTab)
      log "Tab override: " & (name override of targetTab)
      delay 2.0 -- delay is here only for illustrative purposes
  
      -- Clear override
      set name override of targetTab to ""
  end tell
  ```
  
  AI disclosure: Antigravity CLI was used for the first draft. Iterated,
  minimised, reviewed, and tested by me.
  
  Closes: https://github.com/ghostty-org/ghostty/issues/12048
  Discussion: https://github.com/ghostty-org/ghostty/discussions/12047
  ````
- [`18f0963`](https://github.com/ghostty-org/ghostty/commit/18f09635d9e2e27df1d332f49a82d27cdcc03a48) macos: clear split zoom indicator when tree is not split ([#14703](https://github.com/ghostty-org/ghostty/issues/14703)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  When closing sibling splits down to a single terminal leaf while zoomed
  via AppleScript, `SplitTree` retained its zoomed node reference because
  the target being removed was not the zoomed node itself.
  
  Because the tree was no longer split but the zoomed property remained
  non-nil, the window's zoom state stayed active and the reset zoom
  indicator remained visible.
  
  `SplitTree` now validates that a tree can only have a zoomed node if it
  actually contains splits and the zoomed node exists in root. In
  addition, `SplitTree` exposes an `isZoomed` property, and the terminal
  controller and window reactively update the zoom state and accessory
  controls accordingly.
  
  AI disclosure: Antigravity CLI wrote the tests initially. Iterated,
  reviewed, and tested by me.
  
  <details>
  <summary>UX before:</summary>
  <video
  src="https://github.com/user-attachments/assets/263557d1-1be8-41ca-9070-85075c659afb"
  width="100%"></video>
  </details>
  
  <details>
  <summary>UX after:</summary>
  <video
  src="https://github.com/user-attachments/assets/55ba6778-0901-4722-aa51-8ea0b0c83a1c"
  width="100%"></video>
  </details>
  
  Minimal reproducible example (MRE) using `AppleScript`:
  ```applescript
  tell application id "com.mitchellh.ghostty"
      activate
  
      -- Get the current focused terminal
      set t1 to focused terminal of selected tab of front window
  
      -- Create 4 splits (2x2 grid)
      --   [ t1 | t2 ]
      --   [ t3 | t4 ]
      set t2 to split t1 direction right
      delay 0.5
  
      set t3 to split t1 direction down
      delay 0.5
  
      set t4 to split t2 direction down
      delay 0.5
  
      -- Zoom one of the splits (t1)
      perform action "toggle_split_zoom" on t1
      delay 0.5
  
      -- Close other splits
      try
          close t4
      on error
          perform action "close_surface" on t4
      end try
      delay 0.2
  
      try
          close t3
      on error
          perform action "close_surface" on t3
      end try
      delay 0.2
  
      try
          close t2
      on error
          perform action "close_surface" on t2
      end try
  end tell
  ```
  ````
- [`6ce1e60`](https://github.com/ghostty-org/ghostty/commit/6ce1e605819a9db6f62efb6e1eb98fe1327c3a50) mirror deps ([@mitchellh](https://github.com/mitchellh))
- [`efc5105`](https://github.com/ghostty-org/ghostty/commit/efc51050badfff9a444e5f7750bca9d2ff379bf9) ci: use macOS Golden Gate with Xcode 27.1 ([@mitchellh](https://github.com/mitchellh))
- [`de956a2`](https://github.com/ghostty-org/ghostty/commit/de956a2c2f1c03efb314668e33db9a809097e5de) mirror deps ([#14861](https://github.com/ghostty-org/ghostty/issues/14861)) ([@mitchellh](https://github.com/mitchellh))
- [`da5936c`](https://github.com/ghostty-org/ghostty/commit/da5936c2287cd7f466acdad3cc000de5ce35ccaa) ci: use macOS Golden Gate with Xcode 27.1 ([#14862](https://github.com/ghostty-org/ghostty/issues/14862)) ([@mitchellh](https://github.com/mitchellh))
- [`6eb24a0`](https://github.com/ghostty-org/ghostty/commit/6eb24a0f0f38cabd24457b31c44d6b6bde5540f5) shell-integration: don't let directory names inject escape sequences ([@mitchellh](https://github.com/mitchellh))
  ```text
  The zsh integration reported the working directory with `print`, which
  expands backslash escapes in every argument, including `$PWD`. A
  directory named `x\a\e]52;c;SGVsbG8=\a` ended our OSC 7 early and sent
  a real OSC 52 sequence. A directory name containing a raw ESC or BEL
  byte did the same thing in both zsh and bash.
  
  zsh now uses `print -r` so backslashes in the path are printed as-is,
  and writes the ESC and BEL framing bytes with `$'...'` quoting. Both
  zsh and bash strip control bytes from the hostname and directory
  before sending them, the same way the zsh title code already does.
  Fish was already safe because it percent-encodes the path.
  ```
- [`ebd4499`](https://github.com/ghostty-org/ghostty/commit/ebd449995d321e90d6c73be3decb15558512b2ed) shell-integration: don't let directory names inject escape sequences ([#14859](https://github.com/ghostty-org/ghostty/issues/14859)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The zsh integration reported the working directory with `print`, which
  expands backslash escapes in every argument, including `$PWD`. A
  directory named `x\a\e]52;c;SGVsbG8=\a` ended our OSC 7 early and sent a
  real OSC 52 sequence. A directory name containing a raw ESC or BEL byte
  did the same thing in both zsh and bash.
  
  zsh now uses `print -r` so backslashes in the path are printed as-is,
  and writes the ESC and BEL framing bytes with `$'...'` quoting. Both zsh
  and bash strip control bytes from the hostname and directory before
  sending them, the same way the zsh title code already does. Fish was
  already safe because it percent-encodes the path.
  ```
- [`1851e12`](https://github.com/ghostty-org/ghostty/commit/1851e121baec1f02b31065a8c4ae3ee845bbc4d1) terminal/tmux: reject zero-sized and oversized panes in layouts ([@mitchellh](https://github.com/mitchellh))
  ```text
  A program running in the terminal can enter tmux control mode with
  `ESC P 1000 p` and then send its own `%layout-change` notifications or
  `list-windows` output. The layout parser accepted nodes with a width or
  height of zero, and the viewer cast pane sizes to `u16` without checking
  them.
  
  A bad layout now makes the tmux viewer defunct with a logged warning,
  the same as any other layout error, instead of crashing Ghostty. Real
  tmux never sends zero-sized panes, so normal sessions are unaffected.
  ```
- [`bf14ea1`](https://github.com/ghostty-org/ghostty/commit/bf14ea1fbda2d069112003b80ec3b9186b7688f6) terminal/tmux: reject zero-sized and oversized panes in layouts ([#14858](https://github.com/ghostty-org/ghostty/issues/14858)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A program running in the terminal can enter tmux control mode with `ESC
  P 1000 p` and then send its own `%layout-change` notifications or
  `list-windows` output. The layout parser accepted nodes with a width or
  height of zero, and the viewer cast pane sizes to `u16` without checking
  them.
  
  A bad layout now makes the tmux viewer defunct with a logged warning,
  the same as any other layout error, instead of crashing Ghostty. Real
  tmux never sends zero-sized panes, so normal sessions are unaffected.
  ```
- [`297ff52`](https://github.com/ghostty-org/ghostty/commit/297ff52922127fd7a2b7f8fe856d39f2b48ace07) gtk: implement the Kitty clipboard protocol (OSC 5522) ([@jcollie](https://github.com/jcollie))
  ```text
  Implement the kitty_read, kitty_write, and list (paste event) requests
  in the GTK apprt on top of the existing core protocol support, and wire
  the confirmation dialog up to Kitty requests, including session-grant
  remember support.
  
  Also fix two adjacent issues found while testing: the clipboard-write
  signal now carries a "cleared" flag so image-only writes toast as
  copies instead of clears, and a failed OSC 52 text read now answers
  with an empty reply instead of leaving the client waiting forever.
  
  TODO: the new remember-row strings in the confirmation dialog are
  deliberately not marked for translation; wrap them in i18n._() and
  regenerate the translation files once they should be translated.
  ```
- [`54b6544`](https://github.com/ghostty-org/ghostty/commit/54b65443e0247280ce2d4826c02870f887166578) gtk: show an image preview in the clipboard confirmation dialog ([@jcollie](https://github.com/jcollie))
  ```text
  Decode the first image/* representation of a Kitty clipboard request
  with gdk_texture_new_from_bytes and show it in the dialog in place of
  the text preview, falling back to the text preview when there is no
  decodable image. The picture's paintable and the visible preview page
  are bound declaratively to the clipboard-image property.
  ```
- [`3ea78b0`](https://github.com/ghostty-org/ghostty/commit/3ea78b066715891e9855d56644c9fd9b04335227) gtk: fix crash denying an OSC 52 read with "remember" checked ([@jcollie](https://github.com/jcollie))
  ```text
  Remembering the denial set clipboard-read to deny before the request was
  answered, and the OSC 52 reply is written by the same path that serves an
  allowed read, which asserts reads aren't denied.
  ```
- [`1ebbfe9`](https://github.com/ghostty-org/ghostty/commit/1ebbfe9a1996b29d4c4561be7ae977d2fddc7a30) gtk: preview every representation of a clipboard request ([@jcollie](https://github.com/jcollie))
  ```text
  A multipart payload was reduced to one preview — the first decodable
  image, else the first text, else a bare list of MIME types — so the user
  authorized data they were never shown. The dialog now gives each
  representation its own page, named by MIME type.
  ```
- [`1306fab`](https://github.com/ghostty-org/ghostty/commit/1306fab94d15f1b01ddfba5644f695610697bde6) test: wait for the clipboard status reply ([@jcollie](https://github.com/jcollie))
  ```text
  The script exited as soon as it had written the transaction, so the
  terminal's status packet arrived with nothing left to read it and
  printed itself on the next shell prompt. It also carries a name and a
  session password now, so a run exercises the permission prompt.
  ```
- [`7169fea`](https://github.com/ghostty-org/ghostty/commit/7169fea55bfd58a57e4139fd90300cc93f8d187f) gtk: reword the Kitty clipboard remember subtitle ([@jcollie](https://github.com/jcollie))
- [`a6a1a46`](https://github.com/ghostty-org/ghostty/commit/a6a1a4664237841dc171da28686be256ef92cf3e) terminal: mark pins on erased history rows as garbage ([@noib3](https://github.com/noib3))
- [`b97e426`](https://github.com/ghostty-org/ghostty/commit/b97e42691c44bc0e35eb7750b06273145f89c4dc) set TERM for +ssh without clobbering the user's SetEnv ([@mitchellh](https://github.com/mitchellh))
  ```text
  `+ssh` passed `-o SetEnv=TERM=...` to ssh. ssh only uses the first
  SetEnv it finds, so the one on the command line replaced every SetEnv
  entry in the user's ssh config. This brings back the bug that #11518
  fixed in the old shell integration wrapper, now in `+ssh` (#12582).
  
  `TERM` was also only set with `--forward-env`, so `--forward-env=false`
  (what `ssh-terminfo`-only users get) left the inherited
  `TERM=xterm-ghostty` in place even when the terminfo install failed.
  
  ssh sends the SetEnv entries in the user's ssh config again, and
  a failed terminfo install falls back to `xterm-256color` like it
  did in 1.3.1, no matter which `ssh-*` features are enabled.
  
  `TERM` is now set in the environment of the ssh process instead of
  with SetEnv, the same way the 1.3.1 wrapper did. ssh sends `TERM` on
  its own when it opens a remote terminal, so the server doesn't need
  `AcceptEnv TERM`. This happens whenever `--forward-env` or
  `--terminfo` is enabled. With both disabled, ssh runs with the user's
  environment unchanged. The `+ssh` help is updated to explain how
  `TERM` is chosen.
  
  Docs: https://man.openbsd.org/ssh_config#SetEnv
  ```
- [`9438bd3`](https://github.com/ghostty-org/ghostty/commit/9438bd3e54931b1aceefc6037dc0674f4b844bf6) terminal: mark pins on erased history rows as garbage ([#14838](https://github.com/ghostty-org/ghostty/issues/14838)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This PR makes tracked grid refs report no value when the history row
  they point to is erased (e.g. by `CSI 3 J`), the same way they already
  do when the row is pruned.
  
  That's what the
  [docs](https://github.com/ghostty-org/ghostty/blob/cec8b92/include/ghostty/vt/grid_ref.h#L52-L58)
  describe, but erased refs were silently moved to the top-left of the
  remaining rows instead, so callers couldn't tell their row was gone.
  
  AI disclosure: I used Claude to investigate the issue, write the change
  and add/update tests. I understand what it did, and I wrote this PR
  description.
  ```
- [`1607438`](https://github.com/ghostty-org/ghostty/commit/16074385fa98fdbf54fb09182bb93635ceb97ee4) deps: update z2d to v0.13.0 ([@vancluever](https://github.com/vancluever))
  ```text
  Release notes at:
   https://github.com/vancluever/z2d/blob/v0.13.0/CHANGELOG.md
  
  A few bug fixes that will ultimately pertain to Ghostty's use of z2d,
  but there is a bunch more utility now for text shaping and path
  serialization that could prove useful in a pinch. :) This release also
  now puts Zig 0.17.0 support at a stable tag.
  
  The tarball commit hash here is the tag's corresponding commit.
  ```
- [`37b7101`](https://github.com/ghostty-org/ghostty/commit/37b71016bffab818bcda8be60efe808882c7b947) set TERM for +ssh without clobbering the user's SetEnv ([#14854](https://github.com/ghostty-org/ghostty/issues/14854)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `+ssh` passed `-o SetEnv=TERM=...` to ssh. ssh only uses the first
  SetEnv it finds, so the one on the command line replaced every SetEnv
  entry in the user's ssh config. This brings back the bug that #11518
  fixed in the old shell integration wrapper, now in `+ssh` (#12582).
  
  `TERM` was also only set with `--forward-env`, so `--forward-env=false`
  (what `ssh-terminfo`-only users get) left the inherited
  `TERM=xterm-ghostty` in place even when the terminfo install failed.
  
  ssh sends the SetEnv entries in the user's ssh config again, and a
  failed terminfo install falls back to `xterm-256color` like it did in
  1.3.1, no matter which `ssh-*` features are enabled.
  
  `TERM` is now set in the environment of the ssh process instead of with
  SetEnv, the same way the 1.3.1 wrapper did. ssh sends `TERM` on its own
  when it opens a remote terminal, so the server doesn't need `AcceptEnv
  TERM`. This happens whenever `--forward-env` or `--terminfo` is enabled.
  With both disabled, ssh runs with the user's environment unchanged. The
  `+ssh` help is updated to explain how `TERM` is chosen.
  
  Docs: https://man.openbsd.org/ssh_config#SetEnv
  ```
- [`79bd880`](https://github.com/ghostty-org/ghostty/commit/79bd880d6b0dfbad5a9505fa88ab2b3c598efefe) gtk: implement kitty clipboard protocol ([#14061](https://github.com/ghostty-org/ghostty/issues/14061)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This PR wires up the kitty clipboard protocol in the GTK apprt after all
  of the work to implement the protocol in the core and the macOS apprt.
  Adds an image preview to the confirmation dialog.
  
  Since we are in string freeze for 1.4, two new strings added for the
  confirmation dialog were not marked for translation. Once 1.4 is
  released they can be marked for translation for 1.5.
  
  Fixes #10549
  
  AI disclosure: Claude Fable 5 was used to develop this PR but the author
  has thoroughly reviewed the code and has rewritten sections.
  ```
- [`4bcd00d`](https://github.com/ghostty-org/ghostty/commit/4bcd00d636e2a8156135dfaebdd99f900664aa39) deps: update z2d to v0.13.0 ([#14855](https://github.com/ghostty-org/ghostty/issues/14855)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Release notes at:
   https://github.com/vancluever/z2d/blob/v0.13.0/CHANGELOG.md
  
  A few bug fixes that will ultimately pertain to Ghostty's use of z2d,
  but there is a bunch more utility now for text shaping and path
  serialization that could prove useful in a pinch.
  :slightly_smiling_face: This release also now puts Zig 0.17.0 support at
  a stable tag.
  
  The tarball commit hash here is the tag's corresponding commit.
  ```
- [`84983d0`](https://github.com/ghostty-org/ghostty/commit/84983d060db826a07501c4fc4b7165233ba0df6d) terminal: cap the rows computed by Capacity.adjust ([@mitchellh](https://github.com/mitchellh))
  ```text
  `Capacity.adjust` computed how many rows fit in the page's memory at
  the new column count and stored that number in a 16-bit row count
  without checking it. Narrowing a very wide page can free room for
  more than 65535 rows.
  
  `adjust` now caps the row count at the largest value a page can hold
  before fitting rows to the memory size. This matches the cap that
  `maxCols` already applies to columns. U
  ```
- [`e257bb4`](https://github.com/ghostty-org/ghostty/commit/e257bb45e6d4d61c14eacdc717be89c6110f99ff) terminal: keep cursor style and hyperlink valid after scrollClear prunes ([@mitchellh](https://github.com/mitchellh))
  ```text
  `scrollClear` now checks whether the cursor pin changed pages. If it
  did, it clears the pin's garbage flag and calls `cursorPageReplaced`,
  which registers the style and hyperlink on the new page without
  touching the freed one. This matches how `cursorDownScroll` already
  handles the single row case. The doc comment for `scrollClear` is also
  rewritten to describe where the cursor ends up.
  ```
- [`0af5c9e`](https://github.com/ghostty-org/ghostty/commit/0af5c9e55c5b790de15aa7c7fcd90472b41c53cd) terminal: cap the rows computed by Capacity.adjust ([#14856](https://github.com/ghostty-org/ghostty/issues/14856)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `Capacity.adjust` computed how many rows fit in the page's memory at the
  new column count and stored that number in a 16-bit row count without
  checking it. Narrowing a very wide page can free room for more than
  65535 rows.
  
  `adjust` now caps the row count at the largest value a page can hold
  before fitting rows to the memory size. This matches the cap that
  `maxCols` already applies to columns. U
  ```
- [`1c2ea72`](https://github.com/ghostty-org/ghostty/commit/1c2ea72225e4c4f64dee4411f52035ecf23f336b) terminal: keep cursor style and hyperlink valid after scrollClear prunes ([#14857](https://github.com/ghostty-org/ghostty/issues/14857)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `scrollClear` now checks whether the cursor pin changed pages. If it
  did, it clears the pin's garbage flag and calls `cursorPageReplaced`,
  which registers the style and hyperlink on the new page without touching
  the freed one. This matches how `cursorDownScroll` already handles the
  single row case. The doc comment for `scrollClear` is also rewritten to
  describe where the cursor ends up.
  ```
- [`f63124c`](https://github.com/ghostty-org/ghostty/commit/f63124ca3a8d28d63d1e12d8a93d8932037174da) fontconfig: handle when lang is string and not langset ([@pluiedev](https://github.com/pluiedev))
  ```text
  Fontconfig accepts strings when a langset is expected. This by itself is
  not a problem. But for some ungodly reason it can also *return* a string
  in place of a langset, for example when a `FcPattern` doesn't match any
  language and it falls back to `"en"`. Just why would you do this? What
  reason can there ever be to do this??????
  ```
- [`8112f76`](https://github.com/ghostty-org/ghostty/commit/8112f7676007b7823798f8a1259ab274058e8bf6) fontconfig: handle when lang is string and not langset ([#14853](https://github.com/ghostty-org/ghostty/issues/14853)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fontconfig accepts strings when a langset is expected. This by itself is
  not a problem. But for some ungodly reason it can also *return* a string
  in place of a langset, for example when a `FcPattern` doesn't match any
  language and it [falls
  back](https://github.com/fontconfig/fontconfig/blob/b25ffeabd15b76f86c0c6736f6df2f1b89858010/src/fccfg.c#L2062-L2065)
  to `"en"`. Just why would you do this? What reason can there ever be to
  do this??????
  ```
- [`297507f`](https://github.com/ghostty-org/ghostty/commit/297507f498ef6fd33b7514e143e2d641144457a4) termio: send the config change color scheme report directly ([@jcollie](https://github.com/jcollie))
  ```text
  StreamHandler.changeConfig queued a color_scheme_report message into the
  termio mailbox. changeConfig runs on the io thread, which is the only
  reader of that mailbox, so when the mailbox was full (for example, from
  a burst of query replies queued by the reader thread) the io thread
  blocked forever pushing to itself. Every other thread then blocked on
  its next send to the same mailbox, freezing Ghostty on a config reload.
  
  Write the report from Termio.changeConfig instead, using the same
  colorSchemeReportLocked the message handler uses. The report still
  follows the config update in order with other output.
  
  Fixes: #14833
  ```
- [`509e5fb`](https://github.com/ghostty-org/ghostty/commit/509e5fbec4ddf78f884b4cd21a8a4d7346636d44) macos: fix flash of neighbor tab when moving titlebar tabs ([@lehni](https://github.com/lehni))
  ```text
  With titlebar tabs on macOS 26, move_tab removed the selected tab from its group and added it back at the new position. Removing the selected tab makes AppKit select and draw a neighbor until the tab is made key again, which showed up as a flash of the other tab's content. Instead, move the tabs being passed over to the other side of the selected tab, so the selected tab never leaves the group.
  ```
- [`87b6596`](https://github.com/ghostty-org/ghostty/commit/87b65966dfadc42dacd8d55b99ebc430e6a52455) termio: send the config change color scheme report directly ([#14834](https://github.com/ghostty-org/ghostty/issues/14834)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  StreamHandler.changeConfig queued a color_scheme_report message into the
  termio mailbox. changeConfig runs on the io thread, which is the only
  reader of that mailbox, so when the mailbox was full (for example, from
  a burst of query replies queued by the reader thread) the io thread
  blocked forever pushing to itself. Every other thread then blocked on
  its next send to the same mailbox, freezing Ghostty on a config reload.
  
  Write the report from Termio.changeConfig instead, using the same
  colorSchemeReportLocked the message handler uses. The report still
  follows the config update in order with other output.
  
  Fixes: #14833
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`0fe113a`](https://github.com/ghostty-org/ghostty/commit/0fe113a35370667d8c4d6970ee5c1704825dce6b) macos: fix flash of neighbor tab when moving titlebar tabs ([#14847](https://github.com/ghostty-org/ghostty/issues/14847)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  With `macos-titlebar-style = tabs` on macOS 26, `move_tab` briefly shows
  the content of the neighboring tab before the moved tab is shown again.
  
  The macOS 26 workaround from 09246780b removes the selected tab from its
  tab group and adds it back at the new position, then makes it key on the
  next run loop turn. Removing the selected tab makes AppKit select and
  draw a neighbor in the meantime, which is the flash.
  
  This instead moves the tabs that are passed over to the other side of
  the selected tab. The selected tab never leaves the group and stays
  selected throughout, so nothing else is drawn. The resulting order is
  the same as before, and the titlebar glitches the workaround was added
  for don't come back in my testing.
  
  Only the macOS 26 titlebar tabs path changes. The path for the other
  window styles is untouched.
  
  ## Before
  
  
  https://github.com/user-attachments/assets/2de82693-98bb-4c48-b05d-6abd87935584
  
  ## After
  
  
  https://github.com/user-attachments/assets/e4d829a3-71de-46cd-a1fd-2b46cb6e7e4d
  
  ## AI disclosure
  
  Diagnosed and written with Claude Code. I reviewed the change and tested
  it by hand on macOS 26 with titlebar tabs.
  ```
- [`d773509`](https://github.com/ghostty-org/ghostty/commit/d7735095de636a7014651e23e94620f498979233) build(deps): bump cachix/install-nix-action from 31.11.2 to 31.11.3 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [cachix/install-nix-action](https://github.com/cachix/install-nix-action) from 31.11.2 to 31.11.3.
  - [Release notes](https://github.com/cachix/install-nix-action/releases)
  - [Changelog](https://github.com/cachix/install-nix-action/blob/master/RELEASE.md)
  - [Commits](https://github.com/cachix/install-nix-action/compare/448cde739abec1eaf0646249e3d25bb8d9bc7702...75c75c31ebece974e48ebc36b4ad125bd97bd97b)
  
  ---
  updated-dependencies:
  - dependency-name: cachix/install-nix-action
    dependency-version: 31.11.3
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`3aec944`](https://github.com/ghostty-org/ghostty/commit/3aec9443422758d2cadb90d50ede788a599d633f) build(deps): bump cachix/install-nix-action from 31.11.2 to 31.11.3 ([#14851](https://github.com/ghostty-org/ghostty/issues/14851)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [cachix/install-nix-action](https://github.com/cachix/install-nix-action)
  from 31.11.2 to 31.11.3.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/cachix/install-nix-action/releases">cachix/install-nix-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>31.11.3</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>nix: 2.35.3 -&gt; 2.35.4 by <a
  href="https://github.com/xokdvium"><code>@​xokdvium</code></a> in <a
  href="https://redirect.github.com/cachix/install-nix-action/pull/283">cachix/install-nix-action#283</a>
  <strong>Security</strong>: Updates the bundled certificates shipped with
  the installer to remove the compromised eMudhra certificates.</li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/cachix/install-nix-action/compare/v31.11.2...31.11.3">https://github.com/cachix/install-nix-action/compare/v31.11.2...31.11.3</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/75c75c31ebece974e48ebc36b4ad125bd97bd97b"><code>75c75c3</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/install-nix-action/issues/283">#283</a>
  from xokdvium/cacert-bump</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/37360376014064afef043dd1cddb9f6710a05e63"><code>3736037</code></a>
  nix: 2.35.3 -&gt; 2.35.4</li>
  <li>See full diff in <a
  href="https://github.com/cachix/install-nix-action/compare/448cde739abec1eaf0646249e3d25bb8d9bc7702...75c75c31ebece974e48ebc36b4ad125bd97bd97b">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=cachix/install-nix-action&package-manager=github_actions&previous-version=31.11.2&new-version=31.11.3)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## October 25, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/40229290745), [2](https://github.com/ghostty-org/ghostty/actions/runs/40225977480), [3](https://github.com/ghostty-org/ghostty/actions/runs/40157524465)  
Summary: 3 runs • 9 commits • 4 authors

### Changes

- [`f63508e`](https://github.com/ghostty-org/ghostty/commit/f63508e5a1e0b3a5ce2f6cff591339e5b871aea0) Update VOUCHED list ([#14848](https://github.com/ghostty-org/ghostty/issues/14848)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14846#discussioncomment-19183173)
  from @jcollie.
  
  Vouch: @lehni
  ```
- [`fb13fa9`](https://github.com/ghostty-org/ghostty/commit/fb13fa9602f47590ccfaaea4cd8e178fac2ec8cc) Update VOUCHED list ([#14845](https://github.com/ghostty-org/ghostty/issues/14845)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14844#discussioncomment-19182684)
  from @jcollie.
  
  Denounce: @ifmael
  ```
- [`17001b8`](https://github.com/ghostty-org/ghostty/commit/17001b8f23ea548276c55df84bba720f82561c07) gtk: never resize a split smaller than one cell ([@thomasfedb](https://github.com/thomasfedb))
  ```text
  Also clamp keyboard split resizes to the split size, which fixed an
  assertion failure when resize_split moved past the edge of a split.
  ```
- [`cc84a42`](https://github.com/ghostty-org/ghostty/commit/cc84a42f9c6d0e7b7281d8fe2e7bb79872000b8d) gtk: clamp the split position and keep the ratio in sync ([@thomasfedb](https://github.com/thomasfedb))
- [`859f06f`](https://github.com/ghostty-org/ghostty/commit/859f06fc99c8f01d78ba1c1fced0079dd533ab92) gtk: update the split minimum when the config changes ([@thomasfedb](https://github.com/thomasfedb))
- [`79fecfa`](https://github.com/ghostty-org/ghostty/commit/79fecfa62d3d84da8a68ca68683f52f401e42669) gtk: keep split ratios on window resize and sync on min-position ([@thomasfedb](https://github.com/thomasfedb))
- [`59e565e`](https://github.com/ghostty-org/ghostty/commit/59e565ea0be6f133763540e33300effea40266e8) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`1ee9b25`](https://github.com/ghostty-org/ghostty/commit/1ee9b25636335521deca003e582fb3ea28fd31b8) Update iTerm2 colorschemes ([#14835](https://github.com/ghostty-org/ghostty/issues/14835)) ([@jcollie](https://github.com/jcollie))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20261019-151001-86a776d
  ```
- [`cec8b92`](https://github.com/ghostty-org/ghostty/commit/cec8b92f1ecd176a20a56aa405021e7ae991b996) gtk: never resize a split smaller than one cell ([#14476](https://github.com/ghostty-org/ghostty/issues/14476)) ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes a regression of #1297 on GTK.
  
  **Issue**
  Splits can be dragged or resized down to 0px, which just looks like a
  thick divider. The 10px minimum from #1323 was lost in the GTK rewrite.
  
  **Fix**
  Splits are now at least one cell plus padding in size, and the divider
  can't be dragged past that. This also clamps keyboard resizes.
  
  Tested on Fedora 44. Dragging and `resize_split` stop at one column or
  line. I believe that macOS already has its own minimum and is unchanged.
  
  First pass written with Claude Code (Claude Opus 5.5), reviewed and
  reprompted by me.
  ```

## October 24, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/40135767958), [2](https://github.com/ghostty-org/ghostty/actions/runs/40048552838)  
Summary: 2 runs • 3 commits • 3 authors

### Changes

- [`9cac2bd`](https://github.com/ghostty-org/ghostty/commit/9cac2bd0cf5a4de233e05851d1aaa1347f5baf7f) terminal/kitty: remove placements in erased history ([@jcollie](https://github.com/jcollie))
  ```text
  Erasing scrollback (ED3) moved Kitty image placements anchored in the
  erased rows onto the top-left of the active area, where they became
  visible again until the next screen clear. PageList.eraseRows moves
  tracked pins in erased rows to the top-left of the retained rows
  without marking them garbage, so the image storage never noticed the
  placement had lost its row.
  
  Remove pin-backed placements in the erased history range (and any
  relative placements orphaned by that) before erasing the rows, while
  their pins still identify them. The PageList pin semantics are left
  unchanged since search relies on erased pins not being garbage.
  
  Fixes: #14831
  ```
- [`bcfe577`](https://github.com/ghostty-org/ghostty/commit/bcfe5775454aebe2103e4dde906177b54fe61a94) terminal/kitty: remove placements in erased history ([#14832](https://github.com/ghostty-org/ghostty/issues/14832)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Erasing scrollback (ED3) moved Kitty image placements anchored in the
  erased rows onto the top-left of the active area, where they became
  visible again until the next screen clear. PageList.eraseRows moves
  tracked pins in erased rows to the top-left of the retained rows without
  marking them garbage, so the image storage never noticed the placement
  had lost its row.
  
  Remove pin-backed placements in the erased history range (and any
  relative placements orphaned by that) before erasing the rows, while
  their pins still identify them. The PageList pin semantics are left
  unchanged since search relies on erased pins not being garbage.
  
  Fixes: #14831
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`8ef0ec1`](https://github.com/ghostty-org/ghostty/commit/8ef0ec1238220a5a714be452ed2844f0691fcf83) Update VOUCHED list ([#14824](https://github.com/ghostty-org/ghostty/issues/14824)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14822#discussioncomment-19157195)
  from @jcollie.
  
  Vouch: @AlJohri
  ```

## October 23, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/40003456956)  
Summary: 1 runs • 2 commits • 2 authors

### Changes

- [`a743c4e`](https://github.com/ghostty-org/ghostty/commit/a743c4e53ed62ff7ebca286200d251c4999f398e) docs: replace stale function name. `ghostty_vt_osc_free()` should be `ghostty_osc_free` ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  Change-Id: I4efdf6a51f568b4bc2678ef4a6aa1c106a6a6964
  ```
- [`22f100c`](https://github.com/ghostty-org/ghostty/commit/22f100c6367045bb5fc86172f837047dee2f7670) docs: replace stale function name. `ghostty_vt_osc_free()` should be `ghostty_osc_free` ([#14818](https://github.com/ghostty-org/ghostty/issues/14818)) ([@jcollie](https://github.com/jcollie))

## October 22, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/39847564398)  
Summary: 1 runs • 9 commits • 2 authors

### Changes

- [`432612c`](https://github.com/ghostty-org/ghostty/commit/432612cc3ffd76ef2ced5c6b966908a80eb71e7e) build: add -Dinstalled-exe-path for the Linux launcher files ([@jcollie](https://github.com/jcollie))
  ```text
  The Zig 0.17 port replaced the absolute path to the executable in the
  desktop file, D-Bus services and systemd user service with a bare
  `ghostty`, since the install prefix is no longer known while the build
  is configured. systemd resolves a bare ExecStart= name against a fixed
  search path rather than PATH: /usr/bin and /usr/local/bin on most
  systems, and only systemd's own directory on NixOS. So the service
  failed to start for any install outside those directories, including
  every Nix one.
  
  -Dinstalled-exe-path gives the absolute path to write into those files.
  Without it they still name the executable alone, which is right for
  packages installing to /usr. The Nix package passes its output path, and
  the Flatpak manifests pass /app/bin/ghostty, which is what they produced
  before the port.
  ```
- [`390e607`](https://github.com/ghostty-org/ghostty/commit/390e607550c2cfef322c761c7e4a40424be53eec) nix: check that the launcher files name the installed executable ([@jcollie](https://github.com/jcollie))
  ```text
  Run `systemd-analyze verify` on the systemd user service, and check that
  every Exec= and TryExec= in the D-Bus service and desktop file is an
  absolute path to an executable, so a build that stops passing
  -Dinstalled-exe-path fails instead of shipping a service systemd can't
  start.
  
  The verifier starts a user manager, which needs a writable runtime
  directory that the sandbox doesn't have, so it gets one under $TMPDIR.
  ```
- [`3079a43`](https://github.com/ghostty-org/ghostty/commit/3079a4396693c6cd76a3d5adc0e6d756a55bb290) kitty graphics: non-chunk continuations end the chunked transmission ([@mitchellh](https://github.com/mitchellh))
  ```text
  While a chunked Kitty graphics load was in progress, every transmit
  or animation frame command was treated as its next chunk, regardless
  of its transmission medium. A file (`t=f`), temporary file (`t=t`), or
  shared memory (`t=s`) command arriving mid-load had its encoded path
  appended to the partial image as pixel data.
  
  This diverged from Kitty. The spec only defines chunking for direct
  data, and continuation chunks must carry only the `m` and `q` keys, so
  a command with another medium can never be a continuation. Kitty
  abandons the in-progress load and handles the command as a new
  transmission, for both image and animation frame loads. A client that
  interrupts a load this way now gets the image or frame it asked for
  instead of a corrupted or failed one.
  
  `execute` now destroys the in-progress load before dispatching any
  non-direct transmit or frame command, so the command is handled as a
  fresh transmission, including its own `q` setting.
  ```
- [`75a7606`](https://github.com/ghostty-org/ghostty/commit/75a7606c3f19d08eb00dfdbd0b919abb6545ee0e) terminal: discard cancelled or aborted APC commands ([@mitchellh](https://github.com/mitchellh))
  ```text
  ECMA-48 says a control string that is cancelled or aborted is thrown
  away. xterm only dispatches a control string on ST, and Kitty only
  ends an APC on ST or BEL, so neither runs the command.
  
  https://ecma-international.org/publications-and-standards/standards/ecma-48/
  ```
- [`bbbd749`](https://github.com/ghostty-org/ghostty/commit/bbbd749064737297dabb1d32e78da4f47e23001d) kitty graphics: non-chunk continuations end the chunked transmission ([#14811](https://github.com/ghostty-org/ghostty/issues/14811)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  While a chunked Kitty graphics load was in progress, every transmit or
  animation frame command was treated as its next chunk, regardless of its
  transmission medium. A file (`t=f`), temporary file (`t=t`), or shared
  memory (`t=s`) command arriving mid-load had its encoded path appended
  to the partial image as pixel data.
  
  This diverged from Kitty. The spec only defines chunking for direct
  data, and continuation chunks must carry only the `m` and `q` keys, so a
  command with another medium can never be a continuation. Kitty abandons
  the in-progress load and handles the command as a new transmission, for
  both image and animation frame loads. A client that interrupts a load
  this way now gets the image or frame it asked for instead of a corrupted
  or failed one.
  
  `execute` now destroys the in-progress load before dispatching any
  non-direct transmit or frame command, so the command is handled as a
  fresh transmission, including its own `q` setting.
  ```
- [`8026651`](https://github.com/ghostty-org/ghostty/commit/80266510281cd209361a7e8283b3de82bcd90f53) terminal: discard cancelled or aborted APC commands ([#14812](https://github.com/ghostty-org/ghostty/issues/14812)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ECMA-48 says a control string that is cancelled or aborted is thrown
  away. xterm only dispatches a control string on ST, and Kitty only ends
  an APC on ST or BEL, so neither runs the command.
  
  
  https://ecma-international.org/publications-and-standards/standards/ecma-48/
  ```
- [`e07a6f0`](https://github.com/ghostty-org/ghostty/commit/e07a6f0eba66a07b7f893e1d814018c57b0d1d6e) terminal: continuations must restart at C1 sequence introducers ([@mitchellh](https://github.com/mitchellh))
  ```text
  A stream continuation that ended after an 8-bit C1 introducer had
  aborted an APC could not be exported. For example, `ESC _ data 0x9B`
  ends the APC and starts a CSI, but the tracker only treats ESC as the
  start of a new sequence, so it kept the aborted APC. Replaying that
  would end the APC a second time, and validation rejected it.
  
  Export now starts at the last C1 introducer that moved the parser into
  a new sequence and writes it in its 7-bit ESC form.
  ```
- [`d278256`](https://github.com/ghostty-org/ghostty/commit/d278256dbf0783340d64bc40b8523dd977b30c21) build: add -Dinstalled-exe-path for the Linux launcher files ([#14806](https://github.com/ghostty-org/ghostty/issues/14806)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The Zig 0.17 port replaced the absolute path to the executable in the
  desktop file, D-Bus services and systemd user service with a bare
  `ghostty`, since the install prefix is no longer known while the build
  is configured. systemd resolves a bare ExecStart= name against a fixed
  search path rather than PATH: /usr/bin and /usr/local/bin on most
  systems, and only systemd's own directory on NixOS. So the service
  failed to start for any install outside those directories, including
  every Nix one.
  
  -Dinstalled-exe-path gives the absolute path to write into those files.
  Without it they still name the executable alone, which is right for
  packages installing to /usr. The Nix package passes its output path, and
  the Flatpak manifests pass /app/bin/ghostty, which is what they produced
  before the port.
  
  Fixes #14805
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`08a9518`](https://github.com/ghostty-org/ghostty/commit/08a9518340e19487bd5fdf96963583fb32f0c41f) terminal: continuations must restart at C1 sequence introducers ([#14814](https://github.com/ghostty-org/ghostty/issues/14814)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A stream continuation that ended after an 8-bit C1 introducer had
  aborted an APC could not be exported. For example, `ESC _ data 0x9B`
  ends the APC and starts a CSI, but the tracker only treats ESC as the
  start of a new sequence, so it kept the aborted APC. Replaying that
  would end the APC a second time, and validation rejected it.
  
  Export now starts at the last C1 introducer that moved the parser into a
  new sequence and writes it in its 7-bit ESC form.
  ```

## October 21, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/39676795925), [2](https://github.com/ghostty-org/ghostty/actions/runs/39620313939), [3](https://github.com/ghostty-org/ghostty/actions/runs/39562349268), [4](https://github.com/ghostty-org/ghostty/actions/runs/39536529900), [5](https://github.com/ghostty-org/ghostty/actions/runs/39533979636)  
Summary: 5 runs • 37 commits • 6 authors

### Changes

- [`eea7bea`](https://github.com/ghostty-org/ghostty/commit/eea7beaf7857eb416f0934c9899cf68425104b26) terminal: pending Kitty animation frames and a stable image transmission ([@mitchellh](https://github.com/mitchellh))
- [`781c58e`](https://github.com/ghostty-org/ghostty/commit/781c58e9665ae6409f98d29fe8372e9cad7fd078) terminal: skip snapshot records with unknown tags ([@mitchellh](https://github.com/mitchellh))
- [`5a31f46`](https://github.com/ghostty-org/ghostty/commit/5a31f469b641d2b2107d5f147464417502134f54) terminal: decode snapshot records from a header the caller reads ([@mitchellh](https://github.com/mitchellh))
- [`f48c260`](https://github.com/ghostty-org/ghostty/commit/f48c2606ce951c2d90af6c88bdf9853bd4d33efc) terminal: snapshot Kitty graphics images and placements ([@mitchellh](https://github.com/mitchellh))
- [`04f20eb`](https://github.com/ghostty-org/ghostty/commit/04f20eb161288d3bb9980533a3acc7180b7ea0c0) terminal: snapshot Kitty graphics pixel payloads ([@mitchellh](https://github.com/mitchellh))
- [`aa4e425`](https://github.com/ghostty-org/ghostty/commit/aa4e425f0eab71c0fd7c243872459d436bc81782) terminal: expose snapshot Kitty graphics through the C API ([@mitchellh](https://github.com/mitchellh))
- [`9f0285f`](https://github.com/ghostty-org/ghostty/commit/9f0285f329c3e1a78e10ff735cde98b085eb39dd) terminal: replace nextSliceUntilGround with nextSliceUntil and Boundary stops ([@mitchellh](https://github.com/mitchellh))
- [`4d3487e`](https://github.com/ghostty-org/ghostty/commit/4d3487ef579136c66fc629e7f1853a55a41b3914) libghostty-vt: replace vt_write_until_ground with vt_write_until ([@mitchellh](https://github.com/mitchellh))
- [`7fdd2df`](https://github.com/ghostty-org/ghostty/commit/7fdd2df67ac61762912468d3fe9676fd766c20be) terminal: stage snapshot Kitty pixel payloads by need and store them raw ([@mitchellh](https://github.com/mitchellh))
- [`2e28d3a`](https://github.com/ghostty-org/ghostty/commit/2e28d3ae28bffb6024e24a0510fa728351b09ada) terminal: add DCS and OSC boundaries to nextSliceUntil and vt_write_until ([@mitchellh](https://github.com/mitchellh))
- [`1092370`](https://github.com/ghostty-org/ghostty/commit/109237025c09a2d899d7c2c6c594feece89d6b92) libghostty: add Kitty graphics images, placements, and pixels to binary snapshot format ([#14801](https://github.com/ghostty-org/ghostty/issues/14801)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This adds Kitty graphics to the terminal snapshot format. A restored
  terminal now shows the same images in the same places, including
  scrollback, animations, virtual placements, and a chunked transmission
  that was still in progress when the snapshot was taken.
  
  The records are optional. A decoder without Kitty graphics support or by
  choice can skip them.
  
  Images and placements are restored before READY, so the terminal handed
  to the caller at READY already has its full layout. But the image _data_
  (pixel data) is sent _after READY_. This is done to optimize a
  time-to-render: a renderer can render the terminal and all cells in the
  proper layout by READY, but lacks the image data still.
  
  Image pixels arrive after READY as their own records, one per image or
  animation frame. The encoder orders payloads by need: images visible in
  the shown viewport first, then each scrollback image right after the
  history page that first shows it, then everything else.
  
  Pixels are stored raw. Snapshots are normally compressed in transit, and
  on real images that compressor does at least as well on raw pixels as on
  pre-compressed ones, so compressing here would only add encoder time.
  Pointless.
  
  ## C Example
  
  The incremental decoder reports each image's pixels as a progress event
  alongside history pages, and the C API exposes this, plus image counts
  and pending bytes per screen for progress UI:
  
  ```c
  uint64_t pending = 0;
  ghostty_snapshot_decoder_get(
      decoder, GHOSTTY_SNAPSHOT_DECODER_DATA_KITTY_PENDING_BYTES_PRIMARY,
      &pending);
  
  while (ghostty_snapshot_decoder_next(decoder) == GHOSTTY_SUCCESS) {
    GhosttySnapshotDecoderProgressKind kind;
    ghostty_snapshot_decoder_get(
        decoder, GHOSTTY_SNAPSHOT_DECODER_DATA_PROGRESS_KIND, &kind);
    if (kind == GHOSTTY_SNAPSHOT_DECODER_PROGRESS_KIND_IMAGE) {
      size_t bytes = 0;
      ghostty_snapshot_decoder_get(
          decoder, GHOSTTY_SNAPSHOT_DECODER_DATA_PROGRESS_IMAGE_BYTES, &bytes);
      // Advance a progress bar, redraw the image, etc.
    }
  }
  ```
  
  **AI usage:** I designed the binary layout and big decisions, I had
  Fable+Opus do most of the implementation plus review (in addition to my
  human review). I wrote the docs myself after it had done that. The
  encoding implementation (kitty.zig) is _fine_, there's a bunch of places
  I think I'd reorder or do things slightly differently but at this stage
  I was far more interested in getting the binary layout, fixtures, etc.
  right over the raw how it works.
  ````
- [`f54340a`](https://github.com/ghostty-org/ghostty/commit/f54340ad77814fe319d136e5e915d6a48de8dd23) libghostty-vt: add `vt_write_until` to process vt until user-specified boundaries ([#14802](https://github.com/ghostty-org/ghostty/issues/14802)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This adds `ghostty_terminal_vt_write_until`, which writes VT data like
  `ghostty_terminal_vt_write` but stops right after the first byte that
  reaches a caller-provided boundary: ground plus start and end of APC,
  DCS and OSC strings.
  
  The use case for this is that it allows downstreams to create a
  high-performance proxy that sits between the pty and the terminal
  emulator in order to implement custom handlers, filter things out, etc.
  
  The main constraint I had was that plain `nextSlice` must not move.
  Normal, mainline, unproxied IO must not have ANY impact from this API.
  And this achieves that.
  
  **ABI breaking change:** I decided to remove the old
  `ghostty_terminal_vt_write_until_ground` instead of having a shim
  because its not a commonly used API and
  `ghostty_terminal_vt_write_until` replaces it.
  
  ## C Example
  
  ```c
  uint32_t want = GHOSTTY_TERMINAL_BOUNDARY_APC_START |
                  GHOSTTY_TERMINAL_BOUNDARY_APC_END;
  size_t off = 0;
  while (off < len) {
    GhosttyTerminalWriteStop stop = GHOSTTY_INIT_SIZED(GhosttyTerminalWriteStop);
    if (ghostty_terminal_vt_write_until(terminal, data + off, len - off,
                                        want, &stop) == GHOSTTY_NO_VALUE) {
      break; // No boundary in the rest of the chunk.
    }
    off += stop.consumed;
    if (stop.reached & GHOSTTY_TERMINAL_BOUNDARY_APC_START) {
      // Content starts at data + off.
    }
    if (stop.reached & GHOSTTY_TERMINAL_BOUNDARY_APC_END) {
      // The ending byte is at data + off - 1.
    }
  }
  ```
  
  **AI usage:** I implemented most of the Zig, AI did most of the C
  changes, the tests, and the benchmark tooling under my direction. I
  reviewed the design, the parser state audit. I wrote the docs and this
  PR message.
  ````
- [`521cf2c`](https://github.com/ghostty-org/ghostty/commit/521cf2c5d30bd48028ca61546c64e7913764073d) Update VOUCHED list ([#14798](https://github.com/ghostty-org/ghostty/issues/14798)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14774#discussioncomment-19100005)
  from @jcollie.
  
  Vouch: @olrtg
  ```
- [`9603143`](https://github.com/ghostty-org/ghostty/commit/9603143989e302937878c1b43f4083d2ca0f04fd) gtk: fix focus and drop result when moving a split between split trees ([@thomasfedb](https://github.com/thomasfedb))
  ```text
  Moving a split out of a split tree now moves focus in that tree to
  another split, as closing it does. Previously the old window kept the
  moved split's title and didn't receive keyboard input.
  
  The split drop handler now returns whether the split was moved, since
  GTK expects a result from it.
  ```
- [`67edd20`](https://github.com/ghostty-org/ghostty/commit/67edd20a0292629da7e01b64973de19d356df487) gtk: fix focus and drop result when moving a split between split trees ([#14475](https://github.com/ghostty-org/ghostty/issues/14475)) ([@jcollie](https://github.com/jcollie))
  ```text
  **Issue**
  Dragging a split onto a split in another window removed it from its
  split tree without moving focus to another split, as closing a split
  does. The old window kept showing the moved split's title.
  
  To reproduce: split a window (A | B), open a second window, and drag B's
  handle onto the second window's split. The first window's title still
  reads B's title, and typing does nothing.
  
  **Fix**
  This reuses the close path's "remove and focus a neighbour" logic for
  moves.
  Tested on Fedora 44 against current `main`, before and after the change.
  
  First pass written with Claude Code (Claude Opus 5.5), reviewed and
  reprompted by me.
  ```
- [`1152bc9`](https://github.com/ghostty-org/ghostty/commit/1152bc991ce9ff95323c25566dc7fe6b3d2d4648) termio: free the exec env once when Surface.init fails ([@Pyre909](https://github.com/Pyre909))
- [`d7ea628`](https://github.com/ghostty-org/ghostty/commit/d7ea6284a620e94ea8c2725d9ce967f806dfdea3) core: free the termio derived config when Termio.init fails ([@Pyre909](https://github.com/Pyre909))
- [`05b4692`](https://github.com/ghostty-org/ghostty/commit/05b46924ea4de8bda3b14f60e1accea9b98e20b4) termio: fail every allocation in the exec env test ([@Pyre909](https://github.com/Pyre909))
- [`1e9b06f`](https://github.com/ghostty-org/ghostty/commit/1e9b06f601d6956d3ea80a57bcde03370d51e48e) core: free the renderer config when Renderer.init fails ([@Pyre909](https://github.com/Pyre909))
- [`0bda7c3`](https://github.com/ghostty-org/ghostty/commit/0bda7c34c54b5bee0e5d7d44ded5f94e873f00fd) core: release the font grid when Surface.init fails ([@Pyre909](https://github.com/Pyre909))
- [`88fb0f8`](https://github.com/ghostty-org/ghostty/commit/88fb0f8f677676e8563f66db547eacbb72d9e438) terminal: make Kitty image storage dirty a change counter ([@mitchellh](https://github.com/mitchellh))
- [`4501fe7`](https://github.com/ghostty-org/ghostty/commit/4501fe72ecf98f325d68a34815ff1a631de0a5f9) terminal: add a fixed Kitty placement kind to the render state ([@mitchellh](https://github.com/mitchellh))
- [`b1260a0`](https://github.com/ghostty-org/ghostty/commit/b1260a050cc7ccae43dd503984cd98d6ee9996e1) terminal: report fixed Kitty placements from the render state ([@mitchellh](https://github.com/mitchellh))
- [`59a68e1`](https://github.com/ghostty-org/ghostty/commit/59a68e16628485057303eff98ee9d91d844d666b) terminal: tell render state consumers when the image list changed ([@mitchellh](https://github.com/mitchellh))
- [`d22c3aa`](https://github.com/ghostty-org/ghostty/commit/d22c3aa030b9e38fc6a0d60eccb2918d5aeda4df) terminal: expose the image placements generation to C embedders ([@mitchellh](https://github.com/mitchellh))
- [`7bd9798`](https://github.com/ghostty-org/ghostty/commit/7bd979836f96976632e9bfa4534229d73cecf0eb) renderer: draw every Kitty placement from the render state ([@mitchellh](https://github.com/mitchellh))
- [`9fc5ec6`](https://github.com/ghostty-org/ghostty/commit/9fc5ec6bbc1fdde5c0aa2b6853f057c37f144729) docs: describe drawing Kitty images from the render state ([@mitchellh](https://github.com/mitchellh))
- [`606012e`](https://github.com/ghostty-org/ghostty/commit/606012ecb9686d8eb36c041bca69d648cdc87410) terminal: fix render state compile on 32-bit targets ([@mitchellh](https://github.com/mitchellh))
- [`dcaf698`](https://github.com/ghostty-org/ghostty/commit/dcaf6984ed542ddb297be6acc9d757504dfa8e0b) terminal: reject OSC 7501 reports with malformed ids ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #14790
  
  OSC 7501 validation iterated id values with a ValueIterator that
  filtered by the value alphabet, which silently skips any value
  containing a disallowed byte.
  
  Validation now iterates the raw values so invalid ids discard the
  whole report as documented. The app, title, and msg length checks
  had the same filtering, so an over-limit value with a disallowed
  byte also escaped its limit. Those now check raw values too.
  ```
- [`8c425a7`](https://github.com/ghostty-org/ghostty/commit/8c425a7bd57de848aa83cb9b003b1ecd6037c56a) terminal: reject OSC 7501 reports with malformed ids ([#14793](https://github.com/ghostty-org/ghostty/issues/14793)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #14790
  
  OSC 7501 validation iterated id values with a ValueIterator that
  filtered by the value alphabet, which silently skips any value
  containing a disallowed byte.
  
  Validation now iterates the raw values so invalid ids discard the whole
  report as documented. The app, title, and msg length checks had the same
  filtering, so an over-limit value with a disallowed byte also escaped
  its limit. Those now check raw values too.
  ```
- [`5799392`](https://github.com/ghostty-org/ghostty/commit/5799392844848cab33b2be217b0963e44fec5026) termio: free the exec env once when Surface.init fails ([#14715](https://github.com/ghostty-org/ghostty/issues/14715)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fix for the double free described in #14708.
  
  `Surface.init` passes the termio env map to `termio.Exec.init` by value,
  and the subprocess frees it in `Exec.deinit`. Though the surface's
  `errdefer env.deinit()` stays armed after that handoff, so if a later
  step fails (the mailbox, `Termio.DerivedConfig.init`, or `Termio.init`),
  the env is freed twice: once by `io_exec.deinit()` and again by
  `env.deinit()`. If `Exec.init` itself fails after adding entries, the
  surface frees its stale copy of the map instead.
  
  The fix:
  - `Exec.init` owns the env from the call on and frees it if it fails.
  Only its copy is current once it has modified the map, so the caller
  can't free it safely.
  - `Surface.init` builds the env in its own block, so its errdefer ends
  before the handoff.
  - A test fails an allocation inside `Exec.init` and relies on the
  testing allocator to catch a leaked env. Without the fix it reports 317
  bytes allocated and 0 freed.
  - Fixes the term config leak, renderer config leak, and the font grid
  reference. For which all are on the same failure path.
  
  **Testing**
  - Was able to Reproduce on macOS(Upstream), Linux (GTK) (Upstream), and
  Windows (ran under my forked build) by forcing an allocation failure
  just before `Termio.init`. Each crashed in `Environ.Map.deinit` at
  `0xaaaaaaaaaaaaaaaa` (freed memory) without the fix and reported a clean
  `error.OutOfMemory` with it.
  - `zig build test` on macOS: all tests pass.
  
  **AI disclosure:** I used Claude Code to help find the bug, write the
  fix and test, and run the reproductions. I reviewed the changes and
  understand all the code being submitted for implementation.
  ```
- [`48dde97`](https://github.com/ghostty-org/ghostty/commit/48dde97e0413a27064e4c6182db3df6ee999db7d) Move all Kitty placements to RenderState, update renderer ([#14789](https://github.com/ghostty-org/ghostty/issues/14789)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This finishes moving Kitty image placements into `RenderState`, which
  #14780 started with virtual placements.
  
  The render state now reports every Kitty placement on screen: virtual,
  fixed (placed at a cell), and relative placements, including ones
  chained to a fixed placement. Ghostty's renderer now draws only from the
  render state's image placement iterator, so Ghostty and libghostty-vt
  embedders share one source of truth for what images are on screen and
  where.
  
  Benchmark highlights (image work per frame, main => this PR):
  
  - Scrolling with images and 100k lines of scrollback: 3.3µs to 70ns.
  Main's cost grew with scrollback because `pointFromPin` walks the page
  list, but the new render state doesn't do that.
  - New output lines with images on screen: 672–919ns to ~115ns.
  - A dirty row with placeholder images elsewhere on screen: 281ns to
  14ns. Main rebuilt every frame, but the render state is smarter.
  
  **AI usage:** I drove the overall Zig code changes and wrote most of it,
  AI helped with the C API changes since they're mostly mechanical, plus
  testing, validation. I wrote all the comment/docs and this PR message.
  ```
- [`57ad578`](https://github.com/ghostty-org/ghostty/commit/57ad5787a34f38c8bf505d3defa576c551c8620d) gtk: pass an activation token to the OpenURI portal (Dylan Kenney)
  ```text
  Opening a link through the portal sent no activation_token, so the app
  the portal launched had no proof the user asked for it and couldn't
  raise its window on compositors that check. Ask GDK for a token tied to
  the input that opened the link, as GTK's own URI launcher does, and
  pass it in the OpenURI options.
  ```
- [`ab77366`](https://github.com/ghostty-org/ghostty/commit/ab773665b99f35d0877f02c5438ff36423d82207) nix: update zon2nix ([@jcollie](https://github.com/jcollie))
  ```text
  Eliminates extraneous flake inputs.
  Better caching behavior.
  ```
- [`df246d0`](https://github.com/ghostty-org/ghostty/commit/df246d0105e13dfd4a6a54754a9c6555325644ec) nix: update zon2nix ([#14788](https://github.com/ghostty-org/ghostty/issues/14788)) ([@jcollie](https://github.com/jcollie))
  ```text
  Eliminates extraneous flake inputs.
  Better caching behavior.
  ```
- [`47bd203`](https://github.com/ghostty-org/ghostty/commit/47bd2033cd01a84fe45f1256606224a6891da5cb) gtk: pass an activation token to the OpenURI portal ([#14787](https://github.com/ghostty-org/ghostty/issues/14787)) ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes #14785
  
  Opening a link through the portal sent no activation_token, so the app
  the portal launched had no proof the user asked for it and couldn't
  raise its window on compositors that check. Ask GDK for a token tied to
  the input that opened the link, as GTK's own URI launcher does, and pass
  it in the OpenURI options.
  
  Rebased on main (Zig 0.17), 3994 tests passed, 0 failed, and a
  Ctrl+click's token showed up in the OpenURI call and Brave used it.
  
  Claude Code wrote the change and ran the build and test suite. I
  reviewed the code and did the real-click tests myself.
  ```
- [`90dcd00`](https://github.com/ghostty-org/ghostty/commit/90dcd00b508c86e79402e8d06a5afd16af6b6059) Update VOUCHED list ([#14794](https://github.com/ghostty-org/ghostty/issues/14794)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14792#discussioncomment-19086968)
  from @jcollie.
  
  Vouch: @binaryfire
  ```

