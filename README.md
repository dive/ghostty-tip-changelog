> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: September 25, 2026 at 10:59 UTC.

## September 25, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/36090632632)  
Summary: 1 runs • 13 commits • 5 authors

### Changes

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
Summary: 3 runs • 4 commits • 2 authors

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
- [`7c40388`](https://github.com/ghostty-org/ghostty/commit/7c40388b2c63b7dcc5d6c9b9804e40fb2574444f) Update VOUCHED list ([#14373](https://github.com/ghostty-org/ghostty/issues/14373)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14372#discussioncomment-18573897)
  from @jcollie.
  
  Vouch: @shreeve
  ```

## September 23, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/35889579093), [2](https://github.com/ghostty-org/ghostty/actions/runs/35865209242)  
Summary: 2 runs • 2 commits • 1 authors

### Changes

- [`622b4ee`](https://github.com/ghostty-org/ghostty/commit/622b4eecd7d2ce1a10930537c17f0d61abdba817) Update VOUCHED list ([#14367](https://github.com/ghostty-org/ghostty/issues/14367)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14365#discussioncomment-18569751)
  from @jcollie.
  
  Vouch: @toppk
  ```
- [`7fb75b3`](https://github.com/ghostty-org/ghostty/commit/7fb75b3c508ce8dfccfe796d9bec3cba75843d84) Update VOUCHED list ([#14363](https://github.com/ghostty-org/ghostty/issues/14363)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14209#discussioncomment-18567131)
  from @jcollie.
  
  Vouch: @nicolaair
  ```

## September 22, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/35755595241), [2](https://github.com/ghostty-org/ghostty/actions/runs/35702865383), [3](https://github.com/ghostty-org/ghostty/actions/runs/35684211276)  
Summary: 3 runs • 7 commits • 5 authors

### Changes

- [`9d2d9ac`](https://github.com/ghostty-org/ghostty/commit/9d2d9acac740dda166cc41c77f5886eb8773809d) agents: drop CLAUDE.md ([@trag1c](https://github.com/trag1c))
- [`4ae9f1a`](https://github.com/ghostty-org/ghostty/commit/4ae9f1a2de5484de3d6a13fe03676b8853b9c41c) agents: drop CLAUDE.md ([#14348](https://github.com/ghostty-org/ghostty/issues/14348)) ([@trag1c](https://github.com/trag1c))
  ```text
  Claude Code finally supports AGENTS.md since
  [v2.1.277](https://code.claude.com/docs/en/changelog#2-1-277), so the
  symlink can be yeeted.
  ```
- [`bd1c82b`](https://github.com/ghostty-org/ghostty/commit/bd1c82bc5306da32b16b5055ceff023d7ebc9edc) Update VOUCHED list ([#14341](https://github.com/ghostty-org/ghostty/issues/14341)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14337#discussioncomment-18549787)
  from @pluiedev.
  
  Denounce: @zorzysty
  ```
- [`8619bec`](https://github.com/ghostty-org/ghostty/commit/8619becb23a8f577694cd50321bdf7adb8473364) opengl: validate exported DMA-BUF planes ([@EriksRemess](https://github.com/EriksRemess))
  ```text
  Maximizing the window could crash the app when EGL returned an invalid DMA-BUF plane descriptor.
  GDK later hit a fatal assertion while downloading the texture.
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

## September 21, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/35621789148), [2](https://github.com/ghostty-org/ghostty/actions/runs/35614571074), [3](https://github.com/ghostty-org/ghostty/actions/runs/35546322398)  
Summary: 3 runs • 5 commits • 5 authors

### Changes

- [`a925a97`](https://github.com/ghostty-org/ghostty/commit/a925a97e37c4d3598d263ec55682ef4f20b2009a) renderer/opengl: fix missing gl.finish() between present request and sharing presented frame ([@AnthonyZhOon](https://github.com/AnthonyZhOon))
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
- [`3c47ca1`](https://github.com/ghostty-org/ghostty/commit/3c47ca159368eb4a860ffe5333abdf4a85b2767b) Sync CODEOWNERS vouch list ([#14327](https://github.com/ghostty-org/ghostty/issues/14327)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Sync CODEOWNERS owners with vouch list.
  
  ## Added Users
  
  - @dungdm93
  ```

## September 20, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/35492892512), [2](https://github.com/ghostty-org/ghostty/actions/runs/35490141243), [3](https://github.com/ghostty-org/ghostty/actions/runs/35487007432)  
Summary: 3 runs • 8 commits • 3 authors

### Changes

- [`27e8b3f`](https://github.com/ghostty-org/ghostty/commit/27e8b3fa85d9cf8c7cd5ae2ced348bcb0a4fba9c) Update VOUCHED list ([#14320](https://github.com/ghostty-org/ghostty/issues/14320)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14319#issuecomment-5747979152)
  from @pluiedev.
  
  Vouch: @RadicalTray
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
- [`12542b3`](https://github.com/ghostty-org/ghostty/commit/12542b3923106fd13e4f5d0f9b7c8b65843a1836) deps: Update uucode for Unicode 18 ([@jacobsandlund](https://github.com/jacobsandlund))
- [`aef7aae`](https://github.com/ghostty-org/ghostty/commit/aef7aaeb88423d7b483e857042a4135d8d5143f1) check-zig-hash --update ([@jacobsandlund](https://github.com/jacobsandlund))
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

## September 19, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/35468004060), [2](https://github.com/ghostty-org/ghostty/actions/runs/35466266073)  
Summary: 2 runs • 3 commits • 3 authors

### Changes

- [`790c6b6`](https://github.com/ghostty-org/ghostty/commit/790c6b60f730a17fef267ffde0817c55fa7d62d3) Update VOUCHED list ([@github-actions[bot]](https://github.com/apps/github-actions))
  ```text
  https://github.com/ghostty-org/ghostty/discussions/14305#discussioncomment-DC_kwDOHFhdAs4BGpVY
  ```
- [`a301054`](https://github.com/ghostty-org/ghostty/commit/a3010543b0c39b98a81ace9f50b1910ae641c8c1) Update VOUCHED list ([#14307](https://github.com/ghostty-org/ghostty/issues/14307)) ([@jcollie](https://github.com/jcollie))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14305#discussioncomment-18519384)
  from @jcollie.
  
  Vouch: @thomasfedb
  ```
- [`ca9b038`](https://github.com/ghostty-org/ghostty/commit/ca9b0384f22fc018d81b9f69cada01677f565126) Update VOUCHED list ([#14308](https://github.com/ghostty-org/ghostty/issues/14308)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14305#discussioncomment-18519384)
  from @jcollie.
  
  Vouch: @thomasfedb
  ```

