> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: August 15, 2026 at 21:15 UTC.

## August 15, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/31894663124), [2](https://github.com/ghostty-org/ghostty/actions/runs/31890031839), [3](https://github.com/ghostty-org/ghostty/actions/runs/31876969328), [4](https://github.com/ghostty-org/ghostty/actions/runs/31868500752), [5](https://github.com/ghostty-org/ghostty/actions/runs/31865684095), [6](https://github.com/ghostty-org/ghostty/actions/runs/31864664855), [7](https://github.com/ghostty-org/ghostty/actions/runs/31862777169)  
Summary: 7 runs • 13 commits • 4 authors

### Changes

- [`cecf816`](https://github.com/ghostty-org/ghostty/commit/cecf81678e47f967b0354acada67e69d229f436b) Update VOUCHED list ([#13843](https://github.com/ghostty-org/ghostty/issues/13843)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13841#discussioncomment-18031969)
  from @jcollie.
  
  Vouch: @preiter93
  ```
- [`946422d`](https://github.com/ghostty-org/ghostty/commit/946422dbc5832bb1d8e3298e339c89577da86bca) terminal: replace std.fmt.parseFloat with custom fraction parsing ([@mitchellh](https://github.com/mitchellh))
  ```text
  We have exactly two callers of `parseFloat` and they both have very
  limited expect input shapes: values 0-1, simple decimals. parseFloat
  brings in ~26KB of binary size, so replace it with a custom parser for
  our exact shape.
  ```
- [`e3939d0`](https://github.com/ghostty-org/ghostty/commit/e3939d0f6224f2d9d16d030e7c1c04f082b0f39e) terminal: replace std.fmt.parseFloat with custom fraction parsing ([#13839](https://github.com/ghostty-org/ghostty/issues/13839)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  We have exactly two callers of `parseFloat` and they both have very
  limited expect input shapes: values 0-1, simple decimals. parseFloat
  brings in ~26KB of binary size, so replace it with a custom parser for
  our exact shape.
  ```
- [`1d9fcdc`](https://github.com/ghostty-org/ghostty/commit/1d9fcdc151aedc72db1678e6e1df3425ed94939b) i18n: complete Kazakh (kk) translation for v1.4 ([@AnmiTaliDev](https://github.com/AnmiTaliDev))
  ```text
  Translates the 180 remaining strings, mainly command palette entries
  introduced for v1.4 localization.
  ```
- [`034f584`](https://github.com/ghostty-org/ghostty/commit/034f5843f21b7a3c9924d5e42ee34ee784699763) fix: apply kk translation review feedback ([@AnmiTaliDev](https://github.com/AnmiTaliDev))
- [`b5aa8e7`](https://github.com/ghostty-org/ghostty/commit/b5aa8e7a071f53dec2c203fc521e147ce6e8cce0) i18n: complete Kazakh (kk) translation for v1.4 ([#13778](https://github.com/ghostty-org/ghostty/issues/13778)) ([@trag1c](https://github.com/trag1c))
  ```text
  Translates the 180 remaining strings, mainly command palette entries
  introduced for v1.4 localization.
  ```
- [`1fdbb8c`](https://github.com/ghostty-org/ghostty/commit/1fdbb8c912231bdbe039614a70f10772a3e50d23) libghostty: -Dvt-features to compile out unused features ([@mitchellh](https://github.com/mitchellh))
  ```text
  This introduces a `-Dvt-features` build option for libghostty-vt that
  compiles out optional feature areas, primarily so size-conscious
  embedders (e.g. wasm) can significantly trim the binary.
  
  The flag is similar to `-Dcpu`, `+feature` or `feature` to enable it,
  `-feature` to disable, magic word `all` to turn all features on or off.
  Example: `-Dvt-features=-all,+render-state` builds only the render
  state API.
  
  ### Sizes
  
  | Build | Bytes | Brotli |
  |---|---|---|
  | default (all features) | 876,500 | 218,309 |
  | web interactive (`-all,+render-state,+input-encode,+selection,+color,+grid-introspection`) | 661,119 | 168,994 |
  | read-only viewer (`-all,+render-state`) | 537,441 | 132,858 |
  | bare VT core (`-all`) | 515,422 | 125,756 |
  | xterm.js browser bundle (incl. renderers) | 488,663 | 99,311 |
  | @xterm/headless | 182,672 | 39,651 |
  
  Note: xterm versions are stable as of this commit.
  ```
- [`794515b`](https://github.com/ghostty-org/ghostty/commit/794515ba60a8c6d537b5f3a427374b23b2673492) libghostty: -Dvt-features to compile out unused features ([#13834](https://github.com/ghostty-org/ghostty/issues/13834)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This introduces a `-Dvt-features` build option for libghostty-vt that
  compiles out optional feature areas, primarily so size-conscious
  embedders (e.g. wasm) can significantly trim the binary.
  
  The flag is similar to `-Dcpu`, `+feature` or `feature` to enable it,
  `-feature` to disable, magic word `all` to turn all features on or off.
  Example: `-Dvt-features=-all,+render-state` builds only the render state
  API.
  
  Added CI to verify the lib and tests _compile_ (we don't run it) for
  each individual feature.
  
  ### Sizes
  
  wasm32, ReleaseFast:
  
  | Build | Bytes | Brotli |
  |---|---|---|
  | default (all features) | 876,500 | 218,309 |
  | web interactive
  (`-all,+render-state,+input-encode,+selection,+color,+grid-introspection`)
  | 661,119 | 168,994 |
  | read-only viewer (`-all,+render-state`) | 537,441 | 132,858 |
  | bare VT core (`-all`) | 515,422 | 125,756 |
  | xterm.js browser bundle (incl. renderers) | 488,663 | 99,311 |
  | @xterm/headless | 182,672 | 39,651 |
  
  Note: xterm versions are stable as of this commit.
  
  ### C Header Note
  
  I didn't do a `vt/features.h` style header that has macros to guard
  symbols for the various features. This is something we should do in the
  future. The way it is now, the C header always declares everything, and
  its not a problem unless an unavailable function is referenced at link
  time.
  ```
- [`348f714`](https://github.com/ghostty-org/ghostty/commit/348f714ff97a4b323ee2ce195bb16387ba6a1dbe) Update VOUCHED list ([#13833](https://github.com/ghostty-org/ghostty/issues/13833)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13831#discussioncomment-18025282)
  from @jcollie.
  
  Vouch: @DiegoArmstrong
  ```
- [`d61920d`](https://github.com/ghostty-org/ghostty/commit/d61920d80e0e6d2c2a058c96d1b916c7300ddab5) lib-vt: disable logging in wasm release builds ([@mitchellh](https://github.com/mitchellh))
- [`51a4311`](https://github.com/ghostty-org/ghostty/commit/51a4311ef18b0971c112967cf24a538a2c71ea36) terminal: clean up overzealous inlining ([@mitchellh](https://github.com/mitchellh))
- [`0e0893a`](https://github.com/ghostty-org/ghostty/commit/0e0893adff219b80f8837f685bfd54f643036fc6) libghostty: attacking wasm binary size ([#13830](https://github.com/ghostty-org/ghostty/issues/13830)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This should release our ReleaseFast bundle from 1.1MB to ~800KB.
  
  The major win is disabling logging in ReleaseFast wasm builds (~200KB).
  
  The next is removing aggressive inlining in paths that don't make sense
  for performance. Verified with benchmarks on native to not affect
  anything really.
  
  The third was really dumb: `var buf: [4096]u32 = @splat(c)` in LLVM
  releasefast for wasm was lowering to 4096 separate `i32.store`...
  like... 30KB of code. Replacing this with a for loop reduced by 30KB and
  made REP (a rare sequence) 11x faster lol.
  ```
- [`e84dd30`](https://github.com/ghostty-org/ghostty/commit/e84dd3015543d695e51993e02a01283cfdab2439) Update VOUCHED list ([#13829](https://github.com/ghostty-org/ghostty/issues/13829)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13828#discussioncomment-18024891)
  from @jcollie.
  
  Vouch: @diego-moment
  ```

## August 14, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/31844397329), [2](https://github.com/ghostty-org/ghostty/actions/runs/31839586303), [3](https://github.com/ghostty-org/ghostty/actions/runs/31833203809), [4](https://github.com/ghostty-org/ghostty/actions/runs/31827610332), [5](https://github.com/ghostty-org/ghostty/actions/runs/31820574489), [6](https://github.com/ghostty-org/ghostty/actions/runs/31817549169), [7](https://github.com/ghostty-org/ghostty/actions/runs/31807124981), [8](https://github.com/ghostty-org/ghostty/actions/runs/31806196926), [9](https://github.com/ghostty-org/ghostty/actions/runs/31799751847), [10](https://github.com/ghostty-org/ghostty/actions/runs/31775512293), [11](https://github.com/ghostty-org/ghostty/actions/runs/31768389423), [12](https://github.com/ghostty-org/ghostty/actions/runs/31764190608)  
Summary: 12 runs • 28 commits • 11 authors

### Changes

- [`88ed6be`](https://github.com/ghostty-org/ghostty/commit/88ed6bebf4abfa8deb1b0cdd73dde4b07c7e0a3e) libghostty: much faster wide-character reflow on resize ([@mitchellh](https://github.com/mitchellh))
  ```text
  Resizing a terminal whose buffer is heavy with wide characters (CJK,
  emoji) is now 3-5x faster on the reflow path.
  
  This was relatively simple work. We already have a bulk fast path for
  same-style cells. We previously omitted ANY wide characters from this.
  We relaxed this by making it work with complete wide pairs (wide followed
  by spacer tail).
  
  ### Benchmarks
  
  Resize dance (13 column resizes, 80 -> 40 -> 132 and back and forth again)
  over a ~2,000-row scrollback buffer.
  
  | Workload | Before | After | Speedup |
  |---|---|---|---|
  | cjk | 0.938 | 0.296 | 3.2x |
  | emoji | 0.875 | 0.191 | 4.6x |
  | mixed build-log | 0.306 | 0.155 | 2.0x |
  | grapheme | 2.449 | 1.831 | 1.3x |
  | ascii-short | 0.115 | 0.117 | 1.0x |
  | ascii-long | 0.109 | 0.112 | 1.0x |
  | latin | 0.093 | 0.095 | 1.0x |
  | sgr-truecolor | 0.939 | 0.965 | 1.0x |
  
  **AI usage:** Profiled, implemented, benchmarked, and written by Fable.
  Plan validated by me before doing it, I wrote all the
  comments/commits/blah.
  ```
- [`d760ee9`](https://github.com/ghostty-org/ghostty/commit/d760ee96e54657416eb427b793c7e839f003df7d) terminal: much faster wide-character reflow on resize ([#13827](https://github.com/ghostty-org/ghostty/issues/13827)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Resizing a terminal whose buffer is heavy with wide characters (CJK,
  emoji) is now 3-5x faster on the reflow path.
  
  This was relatively simple work. We already have a bulk fast path for
  same-style cells. We previously omitted ANY wide characters from this.
  We relaxed this by making it work with complete wide pairs (wide
  followed by spacer tail).
  
  ### Benchmarks
  
  Resize dance (13 column resizes, 80 -> 40 -> 132 and back and forth
  again) over a ~2,000-row scrollback buffer.
  
  | Workload | Before | After | Speedup |
  |---|---|---|---|
  | cjk | 0.938 | 0.296 | 3.2x |
  | emoji | 0.875 | 0.191 | 4.6x |
  | mixed build-log | 0.306 | 0.155 | 2.0x |
  | grapheme | 2.449 | 1.831 | 1.3x |
  | ascii-short | 0.115 | 0.117 | 1.0x |
  | ascii-long | 0.109 | 0.112 | 1.0x |
  | latin | 0.093 | 0.095 | 1.0x |
  | sgr-truecolor | 0.939 | 0.965 | 1.0x |
  
  **AI usage:** Profiled, implemented, benchmarked, and written by Fable.
  Plan validated by me before doing it, I wrote all the
  comments/commits/blah.
  ```
- [`3d9b2b4`](https://github.com/ghostty-org/ghostty/commit/3d9b2b483cd807c05e72e2827559572c38bcbe66) libghostty: much faster grapheme-heavy IO throughput ([@mitchellh](https://github.com/mitchellh))
  ```text
  Processing grapheme-heavy input (ZWJ sequences, emoji modifiers, flags,
  combining marks) through is now almost 3x faster.
  
  ### Primary Change: PageList Capacity Projection
  
  This workload was heavily bound by `PageList.increaseCapacity` because
  pathological cases of single-dimensional growth cause repeated page
  capacity doublings which get increasingly expensive because each time we
  do a full allocation + clone.
  
  So the major change is that for grapheme bytes in particular, when we
  reach a capacity limit, we take the current usage for the current set of
  rows and project it out to the remaining capacity of rows. Basically, we
  assume that a similar workload will continue. So rather than doubling,
  we're _guessing_ how much you're going to need.
  
  In the real world, I'm not really sure if this matters at all. There are
  no regressions on any regular corpus streams (asciinema, wikipedia dumps, etc.).
  
  ### Other Changes
  
  There are some other changes here, all found on the path to improving
  grapheme IO throughput:
  
  * The bitmap allocator now maintains `search_start` hint we update on
    every allocation so that future free-scans are much faster. This is
    the lowest possible place we don't have a full bitmap.
  
  * For wasm32, we use an alternate hashing structure for small keys
    since Wyhash's 64bit * 64bit multiplication is very very slow because
    wasm has no widening instruction.
  
  * Terminal `printSlice` now checks the fast path compatibility once up front
    rather than on every fast-path attempt.
  
  ### Benchmarks
  
  Data: ZWJ family/profession sequences, skin-tone modifiers,
  flags, and combining marks streamed in 64 KiB chunks into an 80x24
  terminal, default modes.
  
  | Benchmark | Before | After | Speedup |
  |---|---|---|---|
  | wasm, V8, 16 MiB stream | 52 MB/s | 151 MB/s | 2.9x |
  | native, terminal-stream, 64 MiB | 894 ms | 305 ms | 2.9x |
  
  Sorry the native stuff is in ms, that's how our native `ghostty-bench`
  does things versus the custom little V8 harness.
  
  **AI usage:** Developed alongside Fable: profiling, implementation, and
  benchmarks. All human language messages written myself. Validated myself.
  ```
- [`6b22215`](https://github.com/ghostty-org/ghostty/commit/6b22215c5d46019f94b658f7665941f951d0de1e) libghostty: much faster grapheme-heavy IO throughput ([#13826](https://github.com/ghostty-org/ghostty/issues/13826)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Processing grapheme-heavy input (ZWJ sequences, emoji modifiers, flags,
  combining marks) through is now almost 3x faster.
  
  ### Primary Change: PageList Capacity Projection
  
  This workload was heavily bound by `PageList.increaseCapacity` because
  pathological cases of single-dimensional growth cause repeated page
  capacity doublings which get increasingly expensive because each time we
  do a full allocation + clone.
  
  So the major change is that for grapheme bytes in particular, when we
  reach a capacity limit, we take the current usage for the current set of
  rows and project it out to the remaining capacity of rows. Basically, we
  assume that a similar workload will continue. So rather than doubling,
  we're _guessing_ how much you're going to need.
  
  In the real world, I'm not really sure if this matters at all. There are
  no regressions on any regular corpus streams (asciinema, wikipedia
  dumps, etc.).
  
  ### Other Changes
  
  There are some other changes here, all found on the path to improving
  grapheme IO throughput:
  
  * The bitmap allocator now maintains `search_start` hint we update on
  every allocation so that future free-scans are much faster. This is the
  lowest possible place we don't have a full bitmap.
  
  * For wasm32, we use an alternate hashing structure for small keys since
  Wyhash's 64bit * 64bit multiplication is very very slow because wasm has
  no widening instruction.
  
  * Terminal `printSlice` now checks the fast path compatibility once up
  front rather than on every fast-path attempt.
  
  ### Benchmarks
  
  Data: ZWJ family/profession sequences, skin-tone modifiers, flags, and
  combining marks streamed in 64 KiB chunks into an 80x24 terminal,
  default modes.
  
  | Benchmark | Before | After | Speedup |
  |---|---|---|---|
  | wasm, V8, 16 MiB stream | 52 MB/s | 151 MB/s | 2.9x |
  | native, terminal-stream, 64 MiB | 894 ms | 305 ms | 2.9x |
  
  Sorry the native stuff is in ms, that's how our native `ghostty-bench`
  does things versus the custom little V8 harness.
  
  **AI usage:** Developed alongside Fable: profiling, implementation, and
  benchmarks. All human language messages written myself. Validated
  myself.
  ```
- [`74a233b`](https://github.com/ghostty-org/ghostty/commit/74a233b5439c6721cee8ae1f453c308e02ca9d74) libghostty: faster render state reads and updates on wasm targets ([@mitchellh](https://github.com/mitchellh))
  ```text
  This makes the `ghostty_render_state_*` C API significantly faster on
  wasm32-freestanding, measured in V8 via Node for Chrome. Also verified
  in `jsc` for Safari.
  
  The major change is a new bulk row read API that makes full-screen cell reads
  roughly 10x faster for wasm embedders. This should help any embedder with
  high FFI overhead, such as Go, Python, etc. too.
  
  Non-wasm performance is not impacted, all benchmarks were run on my mac
  too w/ no regressions (two of the changes are native wins as well).
  
  ## Changes
  
  * color: the "vectorized" palette conversion loop was silently
    scalarized by LLVM into per-byte ops because it loaded/stored through
    array-typed pointers. Zig 0.16 disables the LLVM loop vectorizer, so
    manually vectorized loops must go through vector-typed pointers.
  * C styles: major optimizations to converting Zig styles to C styles.
    This is a heavy operation for render state.
  * render: `endUpdate`'s style-run fill (`@memset` with a struct value)
    re-loaded its source every iteration and stored field by field. Now
    manually vectorized.
  * render: new `GHOSTTY_RENDER_STATE_ROW_DATA_CELLS_RAW` returns a
    borrowed `GhosttyCellsView` of the current row's raw cell values, valid
    until the next update. One call per row instead of 3-6 calls per cell.
  
  ## Benchmarks
  
  | Benchmark | Before | After | Speedup |
  |---|---|---|---|
  | colors_get | 114 ns | 35 ns | 3.3x |
  | style get, per styled cell | 7.8 ns | 6.7 ns | 1.2x |
  | raw+style read, per cell | 8.6 ns | 7.7 ns | 1.1x |
  | full-screen text read, per cell | 7.5 ns | 0.7 ns | 10.7x |
  | full-screen text+style read, per cell | 8.6 ns | 1.7 ns | 5.1x |
  | render state update, styled full frame | 3.4 us | 2.6 us | 1.3x |
  
  **AI usage:** Fable did the implementation and benchmarking and drafted
  this message. Comments were partially rewritten by me.
  ```
- [`16833f5`](https://github.com/ghostty-org/ghostty/commit/16833f5e5f58589c3d6ba876a73eb0c5f550231d) libghostty: faster render state reads and updates on wasm targets ([#13825](https://github.com/ghostty-org/ghostty/issues/13825)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This makes the `ghostty_render_state_*` C API significantly faster on
  wasm32-freestanding, measured in V8 via Node for Chrome. Also verified
  in `jsc` for Safari.
  
  The major change is a new bulk row read API that makes full-screen cell
  reads roughly 10x faster for wasm embedders. This should help any
  embedder with high FFI overhead, such as Go, Python, etc. too.
  
  Non-wasm performance is not impacted, all benchmarks were run on my mac
  too w/ no regressions (two of the changes are native wins as well).
  
  ## Changes
  
  * color: the "vectorized" palette conversion loop was silently
  scalarized by LLVM into per-byte ops because it loaded/stored through
  array-typed pointers. Zig 0.16 disables the LLVM loop vectorizer, so
  manually vectorized loops must go through vector-typed pointers.
  * C styles: major optimizations to converting Zig styles to C styles.
  This is a heavy operation for render state.
  * render: `endUpdate`'s style-run fill (`@memset` with a struct value)
  re-loaded its source every iteration and stored field by field. Now
  manually vectorized.
  * render: new `GHOSTTY_RENDER_STATE_ROW_DATA_CELLS_RAW` returns a
  borrowed `GhosttyCellsView` of the current row's raw cell values, valid
  until the next update. One call per row instead of 3-6 calls per cell.
  
  ## Benchmarks
  
  | Benchmark | Before | After | Speedup |
  |---|---|---|---|
  | colors_get | 114 ns | 35 ns | 3.3x |
  | style get, per styled cell | 7.8 ns | 6.7 ns | 1.2x |
  | raw+style read, per cell | 8.6 ns | 7.7 ns | 1.1x |
   | full-screen text read, per cell | 7.5 ns | 0.7 ns | 10.7x |
   | full-screen text+style read, per cell | 8.6 ns | 1.7 ns | 5.1x |
  | render state update, styled full frame | 3.4 us | 2.6 us | 1.3x |
  
  **AI usage:** Fable did the implementation and benchmarking and drafted
  this message. Comments were partially rewritten by me.
  ```
- [`87f69a1`](https://github.com/ghostty-org/ghostty/commit/87f69a12ee28445cd95e39060fd626ccfc27b5e0) libghostty: much faster vt_write on wasm targets ([@mitchellh](https://github.com/mitchellh))
  ```text
  This makes `ghostty_terminal_vt_write` on wasm32-freestanding anywhere
  from 1.4x to 13x faster depending on the input, measured in V8 via Node
  for Chrome as well as `jsc` for Safari.
  
  ## Changes
  
  * stream: the batched parse path (bulk UTF-8 decode, print_slice runs)
    is used even when `build_options.simd` is false. The per-byte loop
    is now debug-only.
  * simd/vt: the scalar `utf8DecodeUntilControlSeq` gets a vectorized
    ASCII bulk path that is compatible with wasm simd128.
  * style: on wasm, `Style.eql` compares canonical `PackedStyle` forms
    which is faster by like 11%. On native its slower so we only do this
    for wasm.
  * build: wasm targets now default to the `simd128` CPU feature since
    every browser engine has supported it for years. Opt out with
    `-Dcpu=generic`.
  * PACKAGING.md documents the wasm build, including `wasm-opt` notes.
  
  ## Benchmarks
  
  | Workload | Before | After | Speedup |
  |---|---|---|---|
  | ascii | 85 MB/s | 1070 MB/s | 12.5x |
  | ascii-wrap | 84 MB/s | 1103 MB/s | 13.1x |
  | clear-redraw | 85 MB/s | 913 MB/s | 10.7x |
  | scroll | 79 MB/s | 304 MB/s | 3.8x |
  | cursor | 120 MB/s | 255 MB/s | 2.1x |
  | utf8 | 99 MB/s | 169 MB/s | 1.7x |
  | sgr16 | 81 MB/s | 133 MB/s | 1.6x |
  | sgr-truecolor | 62 MB/s | 88 MB/s | 1.4x |
  
  End result: wasm at roughly 50-85% of the native ReleaseFast+SIMD build
  on the same workloads. Plain ASCII was at 6% of native before.
  
  **AI usage:** Lots of Fable help. As always, the human language stuff
  like this commit and comments were rewritten by me.
  ```
- [`2f72b04`](https://github.com/ghostty-org/ghostty/commit/2f72b041f65932867baef177e8f3be9c92b0f2ed) libghostty: much faster vt_write on wasm targets ([#13821](https://github.com/ghostty-org/ghostty/issues/13821)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This makes `ghostty_terminal_vt_write` on wasm32-freestanding anywhere
  from 1.4x to 13x faster depending on the input, measured in V8 via Node
  for Chrome as well as `jsc` for Safari.
  
  This changes the default Wasm build to default to enabling the `simd128`
  CPU feature because baseline doesn't have that and every major browser
  has supported it for years. This results in massive performance
  improvements (like, 50%+ on all streams).
  
  Non-wasm performance is not impacted, all benchmarks were run on my mac
  too w/ no regressions.
  
  ## Changes
  
  * stream: the batched parse path (bulk UTF-8 decode, print_slice runs)
  is used even when `build_options.simd` is false. The per-byte loop is
  now debug-only.
  * simd/vt: the scalar `utf8DecodeUntilControlSeq` gets a vectorized
  ASCII bulk path that is compatible with wasm simd128.
  * style: on wasm, `Style.eql` compares canonical `PackedStyle` forms
  which is faster by like 11%. On native its slower so we only do this for
  wasm.
  * build: wasm targets now default to the `simd128` CPU feature since
  every browser engine has supported it for years. Opt out with
  `-Dcpu=generic`.
  * PACKAGING.md documents the wasm build, including `wasm-opt` notes.
  
  ## Benchmarks
  
  | Workload | Before | After | Speedup |
  |---|---|---|---|
  | ascii | 85 MB/s | 1070 MB/s | 12.5x |
  | ascii-wrap | 84 MB/s | 1103 MB/s | 13.1x |
  | clear-redraw | 85 MB/s | 913 MB/s | 10.7x |
  | scroll | 79 MB/s | 304 MB/s | 3.8x |
  | cursor | 120 MB/s | 255 MB/s | 2.1x |
  | utf8 | 99 MB/s | 169 MB/s | 1.7x |
  | sgr16 | 81 MB/s | 133 MB/s | 1.6x |
  | sgr-truecolor | 62 MB/s | 88 MB/s | 1.4x |
  
  End result: wasm at roughly 50-85% of the native ReleaseFast+SIMD build
  on the same workloads. Plain ASCII was at 6% of native before.
  
  **AI usage:** Lots of Fable help. As always, the human language stuff
  like this commit and comments were rewritten by me.
  ```
- [`29a70bc`](https://github.com/ghostty-org/ghostty/commit/29a70bc3674e7a95c47a54f9660833a86c87f3b5) ci: publish wasm tip artifacts ([@mitchellh](https://github.com/mitchellh))
  ```text
  This builds and publishes `ghostty-vt.wasm` binaries into our tip
  GitHub releases. These are built with the proper optimization, `simd128`
  CPU feature set, and run through `wasm-opt`.
  
  This allows wasm consumers to use libghostty without a Zig toolkit.
  
  Published two: `ghostty-vt.wasm` and `ghostty-vt-small.wasm`. The latter
  is ReleaseSmall, but is 10 to 20% slower. Users choice.
  ```
- [`8f485a7`](https://github.com/ghostty-org/ghostty/commit/8f485a7f478fc497ec02d60f274a33af542f1819) ci: publish wasm tip artifacts ([#13822](https://github.com/ghostty-org/ghostty/issues/13822)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This builds and publishes `ghostty-vt.wasm` binaries into our tip GitHub
  releases. These are built with the proper optimization, `simd128` CPU
  feature set, and run through `wasm-opt`.
  
  This allows wasm consumers to use libghostty without a Zig toolkit.
  
  Published two: `ghostty-vt.wasm` and `ghostty-vt-small.wasm`. The latter
  is ReleaseSmall, but is 10 to 20% slower. Users choice.
  ```
- [`e305665`](https://github.com/ghostty-org/ghostty/commit/e3056658d05bdd54db9fd37a02c196bfe81cfe39) libghostty: faster render state updates and C API reads ([@mitchellh](https://github.com/mitchellh))
  ```text
  This improves the performance of render state plus C API reads. I
  specifically benchmarked the C API call and found a lot of overhead in
  the C API layer which this cleans up. The impact of these changes will be
  less visible to Zig consumers but moderately improve there.
  
  All benchmark numbers below are via the C API.
  
  Highlights:
  
  - full rebuilds are **1.71x faster (11.4µs to 6.6µs per 120x80 frame)**
  - single-dirty-row updates (e.g. the TUI/prompt steady state) are *1.44x
    faster**
  - full-frame reads through the C API are **1.2x to 1.8x faster**
  
  ## Changes
  
  * endUpdate skips unchanged style runs.
  * `GRAPHEMES_UTF8` getter gets a fast path for single ASCII codepoints (the
    overwhelming majority of cells).
  * The bg/fg color getters no longer copy the full 28-byte style. Instead,
     they switch directly on the one color field they need.
  * The `get_multi` variants validate the handle and position once per batch
    instead of per key.
  * Iterator positions are sentinel values instead of Zig optionals. The
    optional tagging overhead was showing up in benchmarks.
  * `colors_get` reads through a pointer instead of copying the ~1KB colors
    struct to the stack per call.
  * The palette conversion is vectorized. The 4-byte padded RGB to 3-byte
    was not being auto-vectorized. Explicitly vectorize it. Something like
    a 4x speedup on NEON.
  
  ## Benchmarks
  
  | Benchmark | Before | After | Speedup |
  |---|---|---|---|
  | update (forced full rebuild) | 11.4 µs/frame | 6.6 µs/frame | 1.71x |
  | update (single dirty row) | 143 ns | 99 ns | 1.44x |
  | read cell style/bg/fg/selected | 10.3 ns/cell | 8.8 ns/cell | 1.17x |
  | read cell via get_multi | 9.6 ns/cell | 6.9 ns/cell | 1.40x |
  | read cell UTF-8 text | 4.9 ns/cell | 2.7 ns/cell | 1.78x |
  | colors_get + palette | 213 ns/call | 45 ns/call | 4.58x |
  
  Clean updates (no terminal changes) and the raw cell read paths
  are unchanged.
  
  **AI usage:** Driven by Fable primarily, reviewed everything and rewrote
  all human-language (comments) since Fable in particular does really bad
  at that. This commit message too.
  ```
- [`53be7d0`](https://github.com/ghostty-org/ghostty/commit/53be7d0353640351e2d6a06725779f21a3ebe481) libghostty: faster render state updates and C API reads ([#13818](https://github.com/ghostty-org/ghostty/issues/13818)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This improves the performance of render state plus C API reads. I
  specifically benchmarked the C API call and found a lot of overhead in
  the C API layer which this cleans up. The impact of these changes will
  be less visible to Zig consumers but moderately improve there.
  
  All benchmark numbers below are via the C API.
  
  Highlights:
  
  - full rebuilds are **1.71x faster (11.4µs to 6.6µs per 120x80 frame)**
  - single-dirty-row updates (e.g. the TUI/prompt steady state) are
  **1.44x faster**
  - full-frame reads through the C API are **1.2x to 1.8x faster**
  
  ## Changes
  
  * endUpdate skips unchanged style runs.
  * `GRAPHEMES_UTF8` getter gets a fast path for single ASCII codepoints
  (the overwhelming majority of cells).
  * The bg/fg color getters no longer copy the full 28-byte style.
  Instead, they switch directly on the one color field they need.
  * The `get_multi` variants validate the handle and position once per
  batch instead of per key.
  * Iterator positions are sentinel values instead of Zig optionals. The
  optional tagging overhead was showing up in benchmarks.
  * `colors_get` reads through a pointer instead of copying the ~1KB
  colors struct to the stack per call.
  * The palette conversion is vectorized. The 4-byte padded RGB to 3-byte
  was not being auto-vectorized. Explicitly vectorize it. Something like a
  4x speedup on NEON.
  
  ## Benchmarks
  
  | Benchmark | Before | After | Speedup |
  |---|---|---|---|
  | update (forced full rebuild) | 11.4 µs/frame | 6.6 µs/frame | 1.71x |
  | update (single dirty row) | 143 ns | 99 ns | 1.44x |
  | read cell style/bg/fg/selected | 10.3 ns/cell | 8.8 ns/cell | 1.17x |
  | read cell via get_multi | 9.6 ns/cell | 6.9 ns/cell | 1.40x |
  |read cell UTF-8 text | 4.9 ns/cell | 2.7 ns/cell | 1.78x |
  | colors_get + palette | 213 ns/call | 45 ns/call | 4.58x |
  
  Clean updates (no terminal changes) and the raw cell read paths are
  unchanged.
  
  **AI usage:** Driven by Fable primarily, reviewed everything and rewrote
  all human-language (comments) since Fable in particular does really bad
  at that. This commit message too.
  ```
- [`cde7f93`](https://github.com/ghostty-org/ghostty/commit/cde7f93435eb40dfbc306e338c43418e8322220e) renderer: simplify cell row storage ([@jparise](https://github.com/jparise))
  ```text
  Cell contents used our ArrayListCollection container to manage per-row
  foreground lists. This was the only place ArrayListCollection was used.
  
  We now own the row list slice directly, initialize cursor capacity to
  exactly one cell, and reallocate the contiguous background buffer in
  place when possible. Foreground rows still use exact sizes so resizes
  (which are infrequent) do not retain the high-water mark.
  ```
- [`4a174e1`](https://github.com/ghostty-org/ghostty/commit/4a174e1c89a93853d18e47fd7553801633ba8746) renderer: simplify cell row storage ([#13599](https://github.com/ghostty-org/ghostty/issues/13599)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Cell contents used our ArrayListCollection container to manage per-row
  foreground lists. This was the only place ArrayListCollection was used.
  
  We now own the row list slice directly, initialize cursor capacity to
  exactly one cell, and reallocate the contiguous background buffer in
  place when possible. Foreground rows still use exact sizes so resizes
  (which are infrequent) do not retain the high-water mark.
  ```
- [`250a36f`](https://github.com/ghostty-org/ghostty/commit/250a36fe6f55de3d2a910deb420f35b0cf6dc350) i18n: Update es_ES translations ([@alosarjos](https://github.com/alosarjos))
  ```text
  Update the translations for the next 1.4 release
  ```
- [`f2022fe`](https://github.com/ghostty-org/ghostty/commit/f2022fe88d57f1b93913de1087ec4f3e459ef3b7) macOS: avoid holding SurfaceView when sending notifications ([@bo2themax](https://github.com/bo2themax))
- [`375ce78`](https://github.com/ghostty-org/ghostty/commit/375ce787466f7bd666f5d8b2e32182ade296dcf3) i18n: Update Norwegian translations ([@Uzaaft](https://github.com/Uzaaft))
- [`6584450`](https://github.com/ghostty-org/ghostty/commit/6584450279ae3ccd20c889c091a73b3a52d5ce09) i18n: Update Norwegian translations ([#13781](https://github.com/ghostty-org/ghostty/issues/13781)) ([@trag1c](https://github.com/trag1c))
- [`1ff3deb`](https://github.com/ghostty-org/ghostty/commit/1ff3deb1bbbf960e69edf49eb7b34fa227080b8d) i18n: Update es_ES translations ([#13800](https://github.com/ghostty-org/ghostty/issues/13800)) ([@00-kat](https://github.com/00-kat))
  ```text
  Update the translations for the next 1.4 release
  ```
- [`562f21a`](https://github.com/ghostty-org/ghostty/commit/562f21a6e72ce1710ca859b25b1562f7f7b0f76a) macOS: avoid holding SurfaceView when sending notifications ([#13810](https://github.com/ghostty-org/ghostty/issues/13810)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  We shouldn't hold a closing surface view when sending notifications and
  waiting to dismiss that notification. This happens rarely, but it's the
  right thing to do.
  
  ### AI Disclosure
  Found by Claude when judging other branches, I applied the changes
  myself.
  
  > Forgot that after force pushing, you can't reopen #13787 🫪, linking it
  here for the review history.
  ```
- [`f81dcad`](https://github.com/ghostty-org/ghostty/commit/f81dcadc82ea2afdcf2dc92929037701122f05b5) Update VOUCHED list ([#13814](https://github.com/ghostty-org/ghostty/issues/13814)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13812#discussioncomment-18018163)
  from @mitchellh.
  
  Vouch: @elitex45
  ```
- [`987ee52`](https://github.com/ghostty-org/ghostty/commit/987ee52751a7d87a7bee996cd2e249a01be2571b) Update and (hopefully) complete Hungarian translations in hu.po ([@balazs-szucs](https://github.com/balazs-szucs))
- [`fa392ba`](https://github.com/ghostty-org/ghostty/commit/fa392baf28c7343ea8f7b005fe2a3299116ee79b) i18n: add missing Hungarian translations ([#13799](https://github.com/ghostty-org/ghostty/issues/13799)) ([@00-kat](https://github.com/00-kat))
  ```text
  Part of: #13766
  ```
- [`93e7e7e`](https://github.com/ghostty-org/ghostty/commit/93e7e7e9933a339032a0499043e0f0c6d7218a7a) po/zh_CN: add missing translations ([@pluiedev](https://github.com/pluiedev))
  ```text
  Frankly the number of command palette entries is a bit ridiculous,
  but such is life
  ```
- [`485864c`](https://github.com/ghostty-org/ghostty/commit/485864cd609ebc7c0350aacbf0ef8c8a0a767c86) po/zh_CN: add missing translations ([#13608](https://github.com/ghostty-org/ghostty/issues/13608)) ([@bo2themax](https://github.com/bo2themax))
  ```text
  Frankly the number of command palette entries is a bit ridiculous, but
  such is life
  ```
- [`89a26a3`](https://github.com/ghostty-org/ghostty/commit/89a26a39eb01a7cf34a64f9329da8304bebd4d8e) Update VOUCHED list ([#13808](https://github.com/ghostty-org/ghostty/issues/13808)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12664#discussioncomment-18012616)
  from @pluiedev.
  
  Vouch: @Zlitus
  ```
- [`365e0bd`](https://github.com/ghostty-org/ghostty/commit/365e0bd0083f3d51a7b7242ad8c5a025c7848c75) i18n: Updating `es_AR` for 1.4 ([#13784](https://github.com/ghostty-org/ghostty/issues/13784)) ([@alanmoyano](https://github.com/alanmoyano))
  ```text
  This PR also updates old translations to keep better consistency.
  
  AI Disclaimer: I translated manually all strings and then used an agent
  to review consistency and legibility and applied many suggestions.
  ```
- [`710b872`](https://github.com/ghostty-org/ghostty/commit/710b8723905533d623c5e64ba0c5e6662fe79713) Update VOUCHED list ([#13805](https://github.com/ghostty-org/ghostty/issues/13805)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13804#discussioncomment-18010199)
  from @jcollie.
  
  Vouch: @pssalman
  ```

## August 13, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/31753370466), [2](https://github.com/ghostty-org/ghostty/actions/runs/31747907657), [3](https://github.com/ghostty-org/ghostty/actions/runs/31739372157), [4](https://github.com/ghostty-org/ghostty/actions/runs/31734701377), [5](https://github.com/ghostty-org/ghostty/actions/runs/31728903762), [6](https://github.com/ghostty-org/ghostty/actions/runs/31709515839), [7](https://github.com/ghostty-org/ghostty/actions/runs/31701849462), [8](https://github.com/ghostty-org/ghostty/actions/runs/31661233121), [9](https://github.com/ghostty-org/ghostty/actions/runs/31658437256)  
Summary: 9 runs • 35 commits • 13 authors

### Changes

- [`8fd2013`](https://github.com/ghostty-org/ghostty/commit/8fd2013a09c9105507a98360318ec7f5e802d50b) i18n: add missing Polish translations + minor fixes ([@trag1c](https://github.com/trag1c))
- [`0ee8a72`](https://github.com/ghostty-org/ghostty/commit/0ee8a72970734717394c1e9e988e365b650ea415) i18n: add missing Polish translations + minor fixes ([#13798](https://github.com/ghostty-org/ghostty/issues/13798)) ([@00-kat](https://github.com/00-kat))
- [`27d1642`](https://github.com/ghostty-org/ghostty/commit/27d1642879adb0da7a363cbfca67c11a102cbc48) Update Turkish translations ([@bitigchi](https://github.com/bitigchi))
- [`226a916`](https://github.com/ghostty-org/ghostty/commit/226a91658da6400140a7da3f38b825ba0395bd5d) Update Turkish translations ([#13770](https://github.com/ghostty-org/ghostty/issues/13770)) ([@00-kat](https://github.com/00-kat))
- [`dd22396`](https://github.com/ghostty-org/ghostty/commit/dd22396bd798d90445e1b365a79da061f96e5dc9) i18n: update es_BO translations for 1.4 ([@MiguelElGallo](https://github.com/MiguelElGallo))
- [`bedb6f2`](https://github.com/ghostty-org/ghostty/commit/bedb6f2ff9d2c65456a7b1e98a5a04a702b77f27) i18n: update es_BO translations for 1.4 ([#13782](https://github.com/ghostty-org/ghostty/issues/13782)) ([@trag1c](https://github.com/trag1c))
  ```text
  issue #13766
  ```
- [`51992ab`](https://github.com/ghostty-org/ghostty/commit/51992ab01ad7e6dfeced16615080b68f620bb122) libghostty: make device and point headers self-contained ([@mitchellh](https://github.com/mitchellh))
- [`e4ec4f0`](https://github.com/ghostty-org/ghostty/commit/e4ec4f0f95f44b131c256127d26c67258104be5a) libghostty: fix enum underlying type detection ([@mitchellh](https://github.com/mitchellh))
  ```text
  Use fixed int enum types for C++11, C23, Clang's fixed-enum extension,
  and GCC 13 or newer. Previously only finalized C23 mode selected an explicit
  underlying type, leaving C++ and common older C modes with
  implementation-defined enum types.
  ```
- [`309440e`](https://github.com/ghostty-org/ghostty/commit/309440e07f3ff097fb4b11ab8cc92b01e29625e8) libghostty: include all public structs in type JSON ([@mitchellh](https://github.com/mitchellh))
- [`d930c74`](https://github.com/ghostty-org/ghostty/commit/d930c74c4d8211d551d0cb99054f13338113f4f9) libghostty: make sized initialization valid C++ ([@mitchellh](https://github.com/mitchellh))
  ```text
  Use an immediately invoked lambda for GHOSTTY_INIT_SIZED in C++ so the
  macro value-initializes every field before setting the ABI size. The
  previous C compound literal and designated initializer required compiler
  extensions in C++17 and C++20.
  
  Keep the existing standard compound literal for C callers.
  ```
- [`119f4fd`](https://github.com/ghostty-org/ghostty/commit/119f4fd6063cb695d1179c5ab1b362c4d71f23d0) libghostty: minor C/C++ compatibility fixes ([#13801](https://github.com/ghostty-org/ghostty/issues/13801)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Minor things as I was just auditing the state of our headers:
  
  * Make sure all subheaders like `point.h` can be included standalone
  * Support Clang/GCC extensions for typed enums if we can detect it
  * Add missing structs to the `ghostty_type_json` function
  * Fix `GHOSTTY_INIT_SIZED` for C++ mode
  ```
- [`ac4dc12`](https://github.com/ghostty-org/ghostty/commit/ac4dc12056c137378da49152b806edc01ba730d6) terminal: size dynamic tabstops by bits ([@jparise](https://github.com/jparise))
  ```text
  Dynamic tabstop storage treated the number of columns above the inline
  capacity as a byte count even though each byte stores eight stops. This
  was wasteful, although in practice this is in the order of just bytes.
  
  Round the extra column count up to whole storage units and grow the existing
  slice with realloc, preserve existing stops.
  ```
- [`908961f`](https://github.com/ghostty-org/ghostty/commit/908961f8a95573096ab231654cccc97170da8086) terminal: size dynamic tabstops by bits ([#13600](https://github.com/ghostty-org/ghostty/issues/13600)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Dynamic tabstop storage treated the number of columns above the inline
  capacity as a byte count even though each byte stores eight stops. This
  was wasteful, although in practice this is in the order of just bytes.
  
  Round the extra column count up to whole storage units and grow the
  existing slice with realloc, preserve existing stops.
  ```
- [`43fe699`](https://github.com/ghostty-org/ghostty/commit/43fe699071c7dceb161dc3b0c04fce46ade36174) Update VOUCHED list ([#13797](https://github.com/ghostty-org/ghostty/issues/13797)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13796#discussioncomment-18006390)
  from @jcollie.
  
  Vouch: @sghng
  ```
- [`30e5eab`](https://github.com/ghostty-org/ghostty/commit/30e5eabe9b1ec1245ffe930264dd0eb3a95c18e7) Add 'da' to `CODEOWNERS` and `src/os/i18n_locales.zig` ([@carlvillads](https://github.com/carlvillads))
- [`af9ead6`](https://github.com/ghostty-org/ghostty/commit/af9ead68172ff4059930e32afc1b7d58a4234fe6) Add danish translation file ([@carlvillads](https://github.com/carlvillads))
- [`bd381c4`](https://github.com/ghostty-org/ghostty/commit/bd381c4a524934f8ada8eae6accae16a484171e9) Update po/da.po ([@carlvillads](https://github.com/carlvillads))
- [`ca5b3dc`](https://github.com/ghostty-org/ghostty/commit/ca5b3dc77bf4421f2d4784318d7431c7658468ef) Update po/da.po ([@carlvillads](https://github.com/carlvillads))
- [`004f79e`](https://github.com/ghostty-org/ghostty/commit/004f79e2737a6b4c10bcff856680802061b00aa1) Merge branch 'ghostty-org:main' into localization-da ([@carlvillads](https://github.com/carlvillads))
- [`4713668`](https://github.com/ghostty-org/ghostty/commit/47136687d725d611a5b9d7fd59a13b1c4e360617) add command palette translations ([@carlvillads](https://github.com/carlvillads))
- [`9f8550b`](https://github.com/ghostty-org/ghostty/commit/9f8550b7f4e671a4305cb63541bbce9652bce38a) Add danish translations ([#13538](https://github.com/ghostty-org/ghostty/issues/13538)) ([@00-kat](https://github.com/00-kat))
- [`4770375`](https://github.com/ghostty-org/ghostty/commit/47703753ad8f313601689d3eb6087469f5665d16) Update VOUCHED list ([#13793](https://github.com/ghostty-org/ghostty/issues/13793)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13791#discussioncomment-18005730)
  from @jcollie.
  
  Vouch: @dolzenko
  ```
- [`bb019ca`](https://github.com/ghostty-org/ghostty/commit/bb019cac272a953c6338b2ab709d6ae26725c3a5) Update VOUCHED list ([#13794](https://github.com/ghostty-org/ghostty/issues/13794)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13792#discussioncomment-18005749)
  from @jcollie.
  
  Vouch: @dmunozv04
  ```
- [`b104a3f`](https://github.com/ghostty-org/ghostty/commit/b104a3f0b3f7e021df5a773f68d5ff6130a8ce64) i18n - Latvian translation of command palette, typo fixes and more natural translations ([@EriksRemess](https://github.com/EriksRemess))
- [`b3514d5`](https://github.com/ghostty-org/ghostty/commit/b3514d56210e8a57a480fb4d0c82121e86df28e4) i18n: Latvian translation. Additional strings. ([@EriksRemess](https://github.com/EriksRemess))
- [`491806f`](https://github.com/ghostty-org/ghostty/commit/491806fbeb35b9153838085d6cf615cb977546e6) i18n(lv): last two missing translations ([@EriksRemess](https://github.com/EriksRemess))
- [`613050d`](https://github.com/ghostty-org/ghostty/commit/613050ddffbe9e15e538a355e2c6934407113793) i18n - Latvian translation of command palette, typo fixes and more natural translations ([#11663](https://github.com/ghostty-org/ghostty/issues/11663)) ([@00-kat](https://github.com/00-kat))
- [`98b828a`](https://github.com/ghostty-org/ghostty/commit/98b828a0232e411eb1e39b83de22fa3869faa51a) config: flush autogenerated config template ([@steven-tk](https://github.com/steven-tk))
  ```text
  #13774
  
  Flush the buffered writer after writing the template so newly created
  configuration files contain the expected guidance instead of being empty.
  ```
- [`dab1b10`](https://github.com/ghostty-org/ghostty/commit/dab1b105b932fecf155d2b6a66c79d8311f826ea) config: flush autogenerated config template ([#13780](https://github.com/ghostty-org/ghostty/issues/13780)) ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes #13774
  
  Simple one-line fix: added the missing flush to the function.
  
  - `zig build` passed
  - `zig build test` passed
  - Confirmed template appears after fix in `~/Library/Application
  Support/com.mitchellh.ghostty/config.ghostty`
  
  ---
  **AI Disclosure**
  
  As mentioned before - I used OpenAI Codex (Sol 5.6 high):
  a) to see if the template still exists & a function exists that tries to
  use the template
  b) find the moment in history this behavior changed.
  Additionally:
  c) reviewing my work and draft a commit message matching your preferred
  style
  
  I implemented the change, ran the build/test, manually verified the
  behavior, and understand the fix.
  ```
- [`d2c70a8`](https://github.com/ghostty-org/ghostty/commit/d2c70a8c7b9b6893c13640c02d7b6f9a1624f3f0) Update VOUCHED list ([#13775](https://github.com/ghostty-org/ghostty/issues/13775)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13773#discussioncomment-17996184)
  from @jcollie.
  
  Vouch: @steven-tk
  ```
- [`bdb5660`](https://github.com/ghostty-org/ghostty/commit/bdb566068ead29409eb5d410249f02f51d274d3d) Expose semantic prompt state through C APIs ([@figelwump](https://github.com/figelwump))
- [`c80c373`](https://github.com/ghostty-org/ghostty/commit/c80c3736275412a0cf75588fb6b7e73fd9395fcd) Remove internal surface prompt query ([@figelwump](https://github.com/figelwump))
- [`b2fa293`](https://github.com/ghostty-org/ghostty/commit/b2fa2931b6599f7e32a7c547b3f5520ac3333881) Expose semantic prompt state through libghostty-vt ([#13767](https://github.com/ghostty-org/ghostty/issues/13767)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Summary
  
  - Add `GHOSTTY_TERMINAL_DATA_CURSOR_AT_PROMPT` to expose semantic prompt
  state through `libghostty-vt`.
  - Reuse `Terminal.cursorIsAtPrompt()` rather than introducing separate
  prompt tracking.
  
  ## Motivation
  
  Ghostty already tracks whether the cursor is at a semantic prompt
  through `Terminal.cursorIsAtPrompt()`. Exposing this query through
  `libghostty-vt` lets downstream terminal consumers use Ghostty's
  existing semantic prompt state without introducing separate tracking.
  
  The query returns false when semantic prompt information is unavailable
  or the alternate screen is active.
  
  Discussed in https://github.com/ghostty-org/ghostty/discussions/13755.
  
  ## Testing
  
  - `zig build test-lib-vt`
  - `zig build test-lib-vt -Dtest-filter="get cursor_at_prompt"`
  - `zig build -Demit-lib-vt`
  
  ## AI disclosure
  
  Codex assisted with adding the `libghostty-vt` query and test,
  addressing review feedback, running validation, and drafting this
  description. I reviewed and edited the final code and description,
  reviewed the validation results, and understand how the change interacts
  with Ghostty's semantic prompt state.
  ```
- [`3650bef`](https://github.com/ghostty-org/ghostty/commit/3650bef4ec28512c1402be8ed838b2929f3aa794) Fix +new-window -e <command> inheriting forced shell integration from the running GTK application. ([@PRIHLOP](https://github.com/PRIHLOP))
  ```text
  Arguments after -e are now marked as an explicit command that requires shell detection. That marker is propagated with the existing command override to the new surface for both the current +new-window and +new-tab GTK paths. When the override is applied, forced shell integration becomes detect; an explicit none remains disabled.
  
  This is scoped to the GTK -e path. It does not change the generic forced shell-integration behavior, so configured integration continues to support shell executables with non-standard names.
  
  Fixes #12378.
  ```
- [`c54ec80`](https://github.com/ghostty-org/ghostty/commit/c54ec80c55a045312f7c97d66b32c8043526f03c) gtk: Fix +new-window -e <command> inheriting forced shell integration from the running GTK application. Fixes [#12378](https://github.com/ghostty-org/ghostty/issues/12378). ([#13741](https://github.com/ghostty-org/ghostty/issues/13741)) ([@jcollie](https://github.com/jcollie))
  ```text
  ## Summary
  Fix `+new-window -e <command>` inheriting forced shell integration from
  the running GTK application.
  
  Arguments after `-e` are now marked as an explicit command that requires
  shell detection. That marker is propagated with the existing command
  override to the new surface for both the current `+new-window` and
  `+new-tab` GTK paths. When the override is applied, forced shell
  integration becomes `detect`; an explicit `none` remains disabled.
  
  This is scoped to the GTK `-e` path. It does not change the generic
  forced shell-integration behavior, so configured integration continues
  to support shell executables with non-standard names.
  
  Fixes #12378.
  
  ## Root cause
  
  The GTK IPC path replaced `config.command` for the new surface but
  retained the running application's `shell-integration` value. `termio`
  therefore treated an arbitrary explicit command such as Vim as the
  forced shell and appended shell-specific arguments.
  
  ## AI usage
  
  I used Hermes Agent (with ChatGPT 5.6) to help inspect the codebase,
  trace the GTK command path, and draft parts of the implementation and
  test. I manually reviewed and edited the changes, validated the behavior
  and test results, and understand the affected code paths.
  ```

## August 12, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/31633700350), [2](https://github.com/ghostty-org/ghostty/actions/runs/31626263992), [3](https://github.com/ghostty-org/ghostty/actions/runs/31613624802), [4](https://github.com/ghostty-org/ghostty/actions/runs/31602893706), [5](https://github.com/ghostty-org/ghostty/actions/runs/31553289786)  
Summary: 5 runs • 21 commits • 6 authors

### Changes

- [`4a516fa`](https://github.com/ghostty-org/ghostty/commit/4a516fa393932fe263bbca8d30740d17e40484f1) github: remove the issue templates ([@trag1c](https://github.com/trag1c))
- [`d2eeb73`](https://github.com/ghostty-org/ghostty/commit/d2eeb734b0dbf80954d1b630986746a5e9e194fd) github: remove the issue templates ([#13765](https://github.com/ghostty-org/ghostty/issues/13765)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  They're not needed anymore since the "New issue" button is now
  inaccessible to non-maintainers anyway.
  ```
- [`8b7c57c`](https://github.com/ghostty-org/ghostty/commit/8b7c57c756115e519516698206b54ed80b49d1e7) gtk: add window title renaming ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes #10469 for GTK.
  ```
- [`1eaf457`](https://github.com/ghostty-org/ghostty/commit/1eaf457b184c0fd34f5ff3fb2d0241d04d7515c4) gtk: add window title renaming ([#10999](https://github.com/ghostty-org/ghostty/issues/10999)) ([@pluiedev](https://github.com/pluiedev))
  ```text
  Fixes #10469 for GTK.
  ```
- [`e523cf8`](https://github.com/ghostty-org/ghostty/commit/e523cf81040626cf240723443d9106813709e49c) terminal: move cursor home after formatting tabstops ([@mitchellh](https://github.com/mitchellh))
  ```text
  Home the cursor after serializing custom tab stops, since formatting VT
  expects it to be there for new lines.
  ```
- [`99b877a`](https://github.com/ghostty-org/ghostty/commit/99b877ad22a7c9e146d6e4c3ba118e66ea694fb7) terminal: move cursor home after formatting tabstops ([#13763](https://github.com/ghostty-org/ghostty/issues/13763)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Home the cursor after serializing custom tab stops, since formatting VT
  expects it to be there for new lines.
  ```
- [`da8b171`](https://github.com/ghostty-org/ghostty/commit/da8b171265e0f9db09287e62e70e10afa0d44e9c) macOS: fix Sendable warning for UnsafeMutablePointer ([@bo2themax](https://github.com/bo2themax))
  ```text
  Swift explicitly [marked UnsafeMutablePointer as non sendable](https://github.com/swiftlang/swift/commit/0568dbf903bbd7c1278c029d7e4eaaad6a460002). Moving from `@unchecked @retroactive` to `nonisolated(unsafe)` is safe for us as per the previous comments
  ```
- [`97ae257`](https://github.com/ghostty-org/ghostty/commit/97ae257497ae687bca7f9c711e46c6937386480e) macOS: fix warnings in showUserNotification ([@bo2themax](https://github.com/bo2themax))
- [`c78226b`](https://github.com/ghostty-org/ghostty/commit/c78226bfaea1e03107d91c4e27c836f9d8143a7b) macOS:  fix Main actor-isolated static property 'find' warnings ([@bo2themax](https://github.com/bo2themax))
- [`cb7eaa0`](https://github.com/ghostty-org/ghostty/commit/cb7eaa059dbc4be7318a6071efc14b4891c628e6) macOS: silent weak ownership difference warnings ([@bo2themax](https://github.com/bo2themax))
  ```text
  UpdateViewModel doesn't own the Task, we don't actually need it here.
  ```
- [`7e3ddc2`](https://github.com/ghostty-org/ghostty/commit/7e3ddc2c891b1076caa235de9681a9b598bc3546) macOS: fix swift warnings ([#13762](https://github.com/ghostty-org/ghostty/issues/13762)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Rework for #12764
  ```
- [`3901168`](https://github.com/ghostty-org/ghostty/commit/3901168b161783cd10b8211c08635bcf756a0751) macOS: remove iOS target ([@bo2themax](https://github.com/bo2themax))
- [`400be4c`](https://github.com/ghostty-org/ghostty/commit/400be4cc1d6c1fbec2222c02aedcef7ada4d796f) macOS: adjust file tree ([@bo2themax](https://github.com/bo2themax))
- [`daab08e`](https://github.com/ghostty-org/ghostty/commit/daab08ec0158934e646d37613f805584277a586f) macOS: drop the cross-platform check and abstraction ([@bo2themax](https://github.com/bo2themax))
- [`b112f39`](https://github.com/ghostty-org/ghostty/commit/b112f3954ce703ceb90afe5bb391b9d33321db2b) build: stop building Ghostty for iOS ([@bo2themax](https://github.com/bo2themax))
- [`4f39c50`](https://github.com/ghostty-org/ghostty/commit/4f39c506ef666887eb0ea68ee125fe1036ace31b) macOS: remove iOS target and clean up cross platform checks ([#13759](https://github.com/ghostty-org/ghostty/issues/13759)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  As discussed in Discord: Ghostty internal support for iOS is not
  important and we verify iOS compatibility for `libghostty-vt` through
  compilation.
  
  Diff is **BIG**, but it contains mostly cleanup and didn't touch macOS's
  implementation (except for some renaming).
  
  ### AI Disclosure
  
  Claude did batch removal for me, I manually reviewed them and ran
  locally for macOS.
  ```
- [`7a17189`](https://github.com/ghostty-org/ghostty/commit/7a171895ddf7088b6f24b137c394e080d967d25e) build: stop building Ghostty.xcframework for iOS ([@bo2themax](https://github.com/bo2themax))
- [`396166e`](https://github.com/ghostty-org/ghostty/commit/396166ecbeca91cb9623e993e6049053cead68bc) build: stop building Ghostty.xcframework for iOS ([#13760](https://github.com/ghostty-org/ghostty/issues/13760)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Depends on https://github.com/ghostty-org/ghostty/pull/13759.
  
  **Removing iOS for `Ghostty.xcframework` will affect other
  [awesome-libghostty](https://github.com/Uzaaft/awesome-libghostty)
  projects**, so I separated it.
  
  
  ### AI Disclosure
  
  Claude ran the check and did the changes, I reviewed it.
  ```
- [`a69a591`](https://github.com/ghostty-org/ghostty/commit/a69a591af11370453d707aa9c0b2ec6ff17ce3c3) libghostty: functions to detect and write until stream ground state ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds new functions to both C and Zig to write VT data until the
  VT parser reaches a "ground" state. The ground state is when the
  parser/stream is stateless: between all partial UTF-8, OSC, CSI, etc.
  
  This lets embedders safely interleave custom VT sequences from multiple
  sources. A practical example is a standard terminal reading from a pty
  that is then doing custom APC or something mid-stream for their emulator
  client.
  ```
- [`51ed437`](https://github.com/ghostty-org/ghostty/commit/51ed437cd1a202e625feb7fd0577354d81bcc54b) libghostty: functions to detect and write until stream ground state ([#13761](https://github.com/ghostty-org/ghostty/issues/13761)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds new functions to both C and Zig to write VT data until the VT
  parser reaches a "ground" state. The ground state is when the
  parser/stream is stateless: between all partial UTF-8, OSC, CSI, etc.
  
  This lets embedders safely interleave custom VT sequences from multiple
  sources. A practical example is a standard terminal reading from a pty
  that is then doing custom APC or something mid-stream for their emulator
  client.
  
  The new function is anywhere from 1% to 5% slower than normal VT write,
  but that should be acceptable due to its special case. Normal VT writes
  are unchanged.
  ```
- [`9f9b8d1`](https://github.com/ghostty-org/ghostty/commit/9f9b8d1d0525e63106cfc0ea19775056b205ffb5) Update VOUCHED list ([#13756](https://github.com/ghostty-org/ghostty/issues/13756)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13755#discussioncomment-17982722)
  from @jcollie.
  
  Vouch: @figelwump
  ```

## August 11, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/31535255635), [2](https://github.com/ghostty-org/ghostty/actions/runs/31523372788), [3](https://github.com/ghostty-org/ghostty/actions/runs/31513216985), [4](https://github.com/ghostty-org/ghostty/actions/runs/31505930846), [5](https://github.com/ghostty-org/ghostty/actions/runs/31501623712), [6](https://github.com/ghostty-org/ghostty/actions/runs/31453674000), [7](https://github.com/ghostty-org/ghostty/actions/runs/31450087990)  
Summary: 7 runs • 20 commits • 5 authors

### Changes

- [`fad7f85`](https://github.com/ghostty-org/ghostty/commit/fad7f854e8f976968bf4d61d408de9699cf87666) Update VOUCHED list ([#13754](https://github.com/ghostty-org/ghostty/issues/13754)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13753#discussioncomment-17980814)
  from @mitchellh.
  
  Vouch: @shorsher
  ```
- [`0c8ec22`](https://github.com/ghostty-org/ghostty/commit/0c8ec225b5a998792ddcbf626687cd3a28ec4523) macOS: remove unused menu validations ([@bo2themax](https://github.com/bo2themax))
- [`f0e3be3`](https://github.com/ghostty-org/ghostty/commit/f0e3be3eefe104eeb119562499df45f4762995f9) macOS: support decoding the surrogate pair with UnicodeHexInput ([@bo2themax](https://github.com/bo2themax))
- [`f719af0`](https://github.com/ghostty-org/ghostty/commit/f719af00c2f44ca7473219abb29dfd5fbb0fcc85) terminal/kitty: use fixed table for control keys ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  Graphics commands prev. stored parsed control fields in a hash map
  backed that used an arena.
  This added hashing and allocation to every command even though protocol
  keys are single ASCII letters.
  
  Store letter keys in a fixed array with a presence bitmap and remove the
  now-unnecessary arena. Unknown non-letter keys remain ignored and are
  covered by a regression test.
  ```
- [`5ce1fe1`](https://github.com/ghostty-org/ghostty/commit/5ce1fe1ff9d5a1069604e1cae599c2f283ec12aa) terminal/kitty: document the experiment variants that were considered ([@Uzaaft](https://github.com/Uzaaft))
- [`04d1939`](https://github.com/ghostty-org/ghostty/commit/04d1939d5f3d0120ed9a4754146883f848e65d43) issue-triage: add a documentation search checkbox ([@trag1c](https://github.com/trag1c))
- [`92cdfc7`](https://github.com/ghostty-org/ghostty/commit/92cdfc748ec42045bc23bff6c8d887de2872ccb3) issue-triage: add a documentation search checkbox ([#13752](https://github.com/ghostty-org/ghostty/issues/13752)) ([@mitchellh](https://github.com/mitchellh))
- [`8e4715b`](https://github.com/ghostty-org/ghostty/commit/8e4715b6ea65c7f5b3e476c81d111a35053d8d4a) terminal/kitty: use fixed table for control keys ([#13729](https://github.com/ghostty-org/ghostty/issues/13729)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Swap out the hash map backed by an arena with a fixed array.
  Measurements from poop:
  CPU Cycles: 173M → 171M (−1.2%)
  Instructions: 519M → 517M (−0.5%)
  Peak RSS: 11.9 → 11.8 MB
  Cache misses: 356K → 312K (−12.4%)
  ```
- [`d1937d6`](https://github.com/ghostty-org/ghostty/commit/d1937d63e45547515484e9820f9148988783ecfe) macOS: remove unused menu validations ([#13726](https://github.com/ghostty-org/ghostty/issues/13726)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  UpdateController isn't the target of any menu item, we don't need add
  menu validation here.
  ```
- [`b0b9fbc`](https://github.com/ghostty-org/ghostty/commit/b0b9fbc8d5b0faecdd79da2303811b42bd0afc67) macOS: support decoding the surrogate pair with UnicodeHexInput ([#13737](https://github.com/ghostty-org/ghostty/issues/13737)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Not yet a perfect fix for
  https://github.com/ghostty-org/ghostty/discussions/13730
  ```
- [`90154e2`](https://github.com/ghostty-org/ghostty/commit/90154e28957ae2257993a30284cce9337c3060e6) macos: ignore -e arguments as open files ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13319
  
  AppKit treats existing positional arguments as documents, causing paths
  passed to a child command after -e to open an extra terminal surface.
  
  We now process args ourselves during openFile callbacks to ignore
  file paths after `-e`. There isn't a way to avoid this I can find
  because AppKit processes argc/argv from the main entrypoint and that
  can't be overridden.
  ```
- [`a858bd4`](https://github.com/ghostty-org/ghostty/commit/a858bd4d35f4cbab142b0fd68d7179cc99de4f4a) macos: ignore -e arguments as open files ([#13748](https://github.com/ghostty-org/ghostty/issues/13748)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13319
  
  AppKit treats existing positional arguments as documents, causing paths
  passed to a child command after -e to open an extra terminal surface.
  
  We now process args ourselves during openFile callbacks to ignore file
  paths after `-e`. There isn't a way to avoid this I can find because
  AppKit processes argc/argv from the main entrypoint and that can't be
  overridden.
  ```
- [`8c9fd7a`](https://github.com/ghostty-org/ghostty/commit/8c9fd7aa79c4d6cc768293fa6e3726162d00c618) macos: normalize command paths as file URLs ([@mitchellh](https://github.com/mitchellh))
  ```text
  #13319
  #13748
  
  Normalize command-line file arguments as file URLs internally while
  keeping the AppKit and FileManager string boundaries unchanged.
  
  This handles relative paths, URL-sensitive characters, and trailing
  directory separators consistently when matching duplicate open-file
  events.
  ```
- [`426386b`](https://github.com/ghostty-org/ghostty/commit/426386b8579d5e558aa5d4cfdfb003ad06bc4fc5) Update VOUCHED list ([#13747](https://github.com/ghostty-org/ghostty/issues/13747)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13746#discussioncomment-17977627)
  from @jcollie.
  
  Vouch: @alex19EP
  ```
- [`d695fff`](https://github.com/ghostty-org/ghostty/commit/d695ffff3b268490a73fd241ea94ac8c26e99599) macos: defer OSC52 clipboard read confirmations until focused ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #10077
  
  Clipboard read confirmations would immediately show a sheet which
  grabbed focus. This could be used for a bunch of dumb reasons, including
  DoS attacks. But, it also caused focus/sheet loops for programs that did
  OSC52 on focus changes (which was seen via some Neovim configs!).
  
  Now, if a surface is unfocused, we bell the surface and show the confirmation
  request on next focus. If the surface is not focused or another request
  comes in, we cancel the prior one.
  
  This also fixes some memory management issues around clipboard requests
  that were likely small leaks (didn't verify the old bug, but verified
  the new code, and eyeballed the old).
  ```
- [`046b8fc`](https://github.com/ghostty-org/ghostty/commit/046b8fcc2a9afccd238577778752a5f86ef9968a) macos: defer OSC52 clipboard read confirmations until focused ([#13744](https://github.com/ghostty-org/ghostty/issues/13744)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #10077
  
  Clipboard read confirmations would immediately show a sheet which
  grabbed focus. This could be used for a bunch of dumb reasons, including
  DoS attacks. But, it also caused focus/sheet loops for programs that did
  OSC52 on focus changes (which was seen via some Neovim configs!).
  
  Now, if a surface is unfocused, we bell the surface and show the
  confirmation request on next focus. If the surface is not focused or
  another request comes in, we cancel the prior one.
  
  This also fixes some memory management issues around clipboard requests
  that were likely small leaks (didn't verify the old bug, but verified
  the new code, and eyeballed the old).
  
  To implement this, I decided to reorient the whole clipboard
  confirmation thing around state on SurfaceView (which simplifies memory
  management) and using Combine on BaseTerminalController to get notified.
  ```
- [`94d775f`](https://github.com/ghostty-org/ghostty/commit/94d775fefc21f74d9cc85a46b34c4e1d85318fd0) Update VOUCHED list ([#13743](https://github.com/ghostty-org/ghostty/issues/13743)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13742#discussioncomment-17970277)
  from @jcollie.
  
  Vouch: @dave92082
  ```
- [`49e4df7`](https://github.com/ghostty-org/ghostty/commit/49e4df78333ccdeb262e59d0f3c4de9d4b0bc7fd) macOS: rework for [#12712](https://github.com/ghostty-org/ghostty/issues/12712) and [#13645](https://github.com/ghostty-org/ghostty/issues/13645) ([@bo2themax](https://github.com/bo2themax))
- [`4b9d589`](https://github.com/ghostty-org/ghostty/commit/4b9d589bcb234b3fdd2160a3abf02cf9b647f328) macOS: disable text selection on macOS 15 ([@bo2themax](https://github.com/bo2themax))
- [`44f06d4`](https://github.com/ghostty-org/ghostty/commit/44f06d4e4fd098aa4b5627e0c2b2d6e704834117) macOS: rework for [#12712](https://github.com/ghostty-org/ghostty/issues/12712) and [#13645](https://github.com/ghostty-org/ghostty/issues/13645) ([#13717](https://github.com/ghostty-org/ghostty/issues/13717)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  `needleSelection` was introduced in #12712 to select all texts when
  syncing pasteboard, the crash happens most on macOS 15 in
  `readPasteboardNeedle`. It seems that `objectWillChange` fires
  differently there, and it's hard to reproduce on macOS 26/27. I think
  guaranteeing from ourside is enough, I believe SwiftUI already as its
  own when updating the binding.
  
  **Confirmed with a simple example on macOS 15, it seems a SwiftUI
  issue🫪. So I changed the minimal macOS version for text selection to
  macOS 26. I don't see an elegant way to fix it.**
  
  <img width="1352" height="849" alt="image"
  src="https://github.com/user-attachments/assets/1dfef3f5-ceaa-41dd-bb91-c23dbc5e4ad3"
  />
  
  
  ```swift
  struct ContentView: View {
      @State private var text = ""
      @State private var selection: TextSelection?
      var body: some View {
          TextField("Search", text: $text, selection: $selection)
      }
  }
  ```
  ````

## August 10, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/31439881201), [2](https://github.com/ghostty-org/ghostty/actions/runs/31436717873), [3](https://github.com/ghostty-org/ghostty/actions/runs/31414618806), [4](https://github.com/ghostty-org/ghostty/actions/runs/31400623896), [5](https://github.com/ghostty-org/ghostty/actions/runs/31367606708), [6](https://github.com/ghostty-org/ghostty/actions/runs/31354005195), [7](https://github.com/ghostty-org/ghostty/actions/runs/31347193596)  
Summary: 7 runs • 26 commits • 9 authors

### Changes

- [`09557e9`](https://github.com/ghostty-org/ghostty/commit/09557e91dc33907fb151b2791414d2c6153fd2e0) Update VOUCHED list ([#13739](https://github.com/ghostty-org/ghostty/issues/13739)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13738#discussioncomment-17968662)
  from @jcollie.
  
  Vouch: @PRIHLOP
  ```
- [`b68eb67`](https://github.com/ghostty-org/ghostty/commit/b68eb67e956b051372910cfe6b453e43121b76e3) config/edit: better handling of existing paths ([@vancluever](https://github.com/vancluever))
  ```text
  This adds some better handling of existing paths when editing
  configuration files:
  
  * If we've found an existing file we just skip any attempts to create
    files/dirs, and just return the path.
  
  * If the path (including file) does not exist, we check to see if the
    directory exists first (possibly following symlinks). Directory
    creation happens normally after this (note that any intermediary
    symlinks in this process will still cause the process to fail, this is
    to prevent infinite loops, as per the comments in
    std.Io.Threaded.dirCreateDirPath).
  ```
- [`d929e6a`](https://github.com/ghostty-org/ghostty/commit/d929e6a34a091dcfd69d45011b96cc70b5575dac) config/edit: better handling of existing paths ([#13736](https://github.com/ghostty-org/ghostty/issues/13736)) ([@jcollie](https://github.com/jcollie))
  ```text
  This adds some better handling of existing paths when editing
  configuration files:
  
  * If we've found an existing file we just skip any attempts to create
  files/dirs, and just return the path.
  
  * If the path (including file) does not exist, we check to see if the
  directory exists first (possibly following symlinks). Directory creation
  happens normally after this (note that any intermediary symlinks in this
  process will still cause the process to fail, this is to prevent
  infinite loops, as per the comments in
  std.Io.Threaded.dirCreateDirPath).
  ```
- [`1dbc8ca`](https://github.com/ghostty-org/ghostty/commit/1dbc8ca30c8ce929019c8a4d971113fc79cd4d58) apprt/gtk: add WeakRef.deinit and use it at teardown sites ([@hakonhagland](https://github.com/hakonhagland))
  ```text
  A GWeakRef must be released before the memory holding it is freed: the
  target keeps a pointer to the GWeakRef so it can clear it at finalize,
  and if that memory is gone by then the target walks into whatever now
  occupies it. inspector_window.zig already carries this warning, and
  every call site follows it — but the rule lives in a comment in one
  file, while the type itself offers only set and get, so releasing one
  looks like an ordinary assignment.
  
  Give it a name. deinit forwards to g_weak_ref_clear, which is the call
  GLib documents for a GWeakRef that is going away, and the dispose-time
  clears now use it. set(null) still works and is unchanged; the clear in
  handleReloadConfig stays a set(null) because the object is still alive
  there and the reference is reused.
  
  Zig has no destructors so this enforces nothing. It puts the
  requirement on the type someone is already looking at.
  ```
- [`951a03b`](https://github.com/ghostty-org/ghostty/commit/951a03b58bf60e73d2d361ac8848cb9423c8be26) apprt/gtk: add WeakRef.deinit and use it at teardown sites ([#13732](https://github.com/ghostty-org/ghostty/issues/13732)) ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes #13713.
  
  `WeakRef(T)` offers `set` and `get`, so releasing one is spelled
  `set(null)` — indistinguishable from an ordinary assignment. The
  requirement that it *must* happen before the owning memory is freed
  lives in a comment in `class/inspector_window.zig`, which is not where
  somebody using the type is looking.
  
  This adds `deinit`, forwarding to `g_weak_ref_clear` — the call GLib
  documents for a `GWeakRef` that is going away — and switches the
  dispose-time clears to it.
  
  ### What changed
  
  - `weak_ref.zig`: new `deinit`, with the reasoning in its doc comment.
  - `window.zig`, `split_tree.zig`, `application.zig`,
  `command_palette.zig`: the four dispose-time clears now call `deinit`.
  
  `set(null)` is unchanged and still valid. The clear in
  `Application.handleReloadConfig` deliberately stays a `set(null)`: the
  object is alive there and the reference is reused, so it is a logical
  clear rather than teardown — which is the distinction the new name is
  meant to make visible.
  
  ### Why it is worth a method
  
  Zig has no destructors, so this enforces nothing; it is documentation
  that happens to be executable. The concrete case is in #13713: I added a
  `WeakRef(Window)` in a downstream branch, did not clear it, and closing
  a window that had shown that dialog deadlocked the GTK main loop inside
  `weak_ref_data_clear_list` locking freed memory. Every upstream call
  site already gets this right — the point is only to put the rule where
  the next person will see it.
  
  ### Testing
  
  `zig build test` passes. `zig fmt --check` clean. Built and used on
  Linux/GTK; the change is behaviourally identical to what was there,
  since `g_weak_ref_clear` and `g_weak_ref_set(NULL)` both unregister.
  
  ---
  
  **AI disclosure per `AI_POLICY.md`:** I investigated the underlying
  incident with Claude Code and it drafted this change; I reviewed it.
  ```
- [`fd47b15`](https://github.com/ghostty-org/ghostty/commit/fd47b15cd4dad1152e17d13b8f79a0f1183c61f2) gtk: free hotkeys memory on app teardown ([@dkinzler](https://github.com/dkinzler))
  ```text
  Free array list memory in Hotkeys.deinit to avoid DebugAllocator
  throwing an error about leaked memory.
  ```
- [`0a183c9`](https://github.com/ghostty-org/ghostty/commit/0a183c923bfc6150e710121f481e3d03464f1b60) core/gtk: allow editing Ghostty config in a Ghostty window ([@jcollie](https://github.com/jcollie))
  ```text
  This PR extends the `open_config` keybind action to allow editing the
  Ghostty config in a new Ghostty window using the editor configured in
  `$EDITOR` or `$VISUAL`.
  ```
- [`e53b18a`](https://github.com/ghostty-org/ghostty/commit/e53b18a64726ad0ef0860d1dd77065defca8223f) gtk: free hotkeys memory on app teardown ([#13727](https://github.com/ghostty-org/ghostty/issues/13727)) ([@pluiedev](https://github.com/pluiedev))
  ```text
  In debug builds the DebugAllocator throws an error about leaked memory
  when you close Ghostty, if you have global keybinds in your config with
  a Wayland compositor that supports the vicinae-hotkey protocol. The
  cause is the `Hotkeys.entries` array list never actually being freed.
  Not really a problem because the list should be kept around until app
  teardown anyway, but not getting an error every time would be nice (even
  if you need a somewhat specific setup for this to even happen right
  now).
  
  To fix this free the array list memory in Hotkeys.deinit with
  `ArrayList.clearAndFree`. As the existing comment on `deinit` already
  mentions, we can't use `ArrayList.deinit` because it leaves the list in
  an invalid state and `Hotkeys.clear` might still get called and use it.
  ```
- [`0914c5c`](https://github.com/ghostty-org/ghostty/commit/0914c5c2f1b96cefb2277a2cb871db181fd559da) core/gtk: allow editing Ghostty config in a Ghostty window ([#11905](https://github.com/ghostty-org/ghostty/issues/11905)) ([@jcollie](https://github.com/jcollie))
  ```text
  This PR extends the `open_config` keybind action to allow editing the
  Ghostty config in a new Ghostty window using the editor configured in
  `$EDITOR` or `$VISUAL`.
  ```
- [`d6248a3`](https://github.com/ghostty-org/ghostty/commit/d6248a32dd724e1cd9c7f9b68c9360f3ad630d47) ghostty.h: mark as internal ([@pluiedev](https://github.com/pluiedev))
  ```text
  Its moniker has been `libghostty-internal` for *quite* a while now among
  maintainers but that has never really been clarified for the public aside
  from a couple comments on discussions. Judging by how many people still
  try to vibe their way into making this work for their purposes, I think
  we should clear this up once and for all.
  ```
- [`7e463bc`](https://github.com/ghostty-org/ghostty/commit/7e463bc65d430e8a8f0aa786abf83601cf2b9598) ghostty.h: mark as internal ([#13724](https://github.com/ghostty-org/ghostty/issues/13724)) ([@bo2themax](https://github.com/bo2themax))
- [`a82637b`](https://github.com/ghostty-org/ghostty/commit/a82637b53aa434fa5c8bc8360c58561d7d48a8e1) crash: resolve sentry directories on the init thread ([@mitchellh](https://github.com/mitchellh))
  ```text
  Sentry initialization already ran on a separate thread, but the cache
  and state directory resolution happened on the main thread before
  spawning it. On macOS the cache dir resolution calls NSFileManager
  URLForDirectory:inDomain:appropriateForURL:create:error: which takes
  multiple milliseconds and was the single largest cost in global.init.
  
  All directory resolution now happens on the init thread.
  
    before: 2967us-4018us
    after:    30us-70us (env map snapshot + thread spawn)
  
  global.init total drops from ~3.4-5.0ms to ~0.4-1.0ms.
  ```
- [`3225e9e`](https://github.com/ghostty-org/ghostty/commit/3225e9ebb195b1cc237c7b8d9de3d51c6863cb5e) macos: cache unified logging loggers per scope ([@mitchellh](https://github.com/mitchellh))
  ```text
  The logFn for macOS unified logging created and released an os_log_t
  logger on every single log call. Loggers are now cached per log scope for
  the process lifetime via an atomic pointer (a creation race wastes at most
  one create).
  
  Measured on macOS (Apple Silicon) with local timing instrumentation
  during app launch, the version-info logging block in global.init:
  
    before: 1070us-2629us
    after:   858us-1319us
  ```
- [`afc79b8`](https://github.com/ghostty-org/ghostty/commit/afc79b8ccf4098ba15659578d0fc666c74fb61bd) font: look up Apple Color Emoji by exact name on macOS ([@mitchellh](https://github.com/mitchellh))
  ```text
  The Apple Color Emoji fallback font was discovered with the generic
  discovery path, which builds a CTFontCollection and runs system-wide
  font matching. Since we know the exact font we want, we can look it
  up directly with CTFontCreateWithName instead.
  ```
- [`c454a3b`](https://github.com/ghostty-org/ghostty/commit/c454a3bf47cd72945b7f4db3b53f8af332e167c9) font: support warmup threads ([@mitchellh](https://github.com/mitchellh))
  ```text
  The first CoreText font query in a process initializes the system
  font database, which takes multiple milliseconds (~7ms measured in an
  isolated process; 2-4ms observed inside Ghostty startup). This cost
  was previously paid during the first surface's font grid
  initialization, on the critical path to the first window.
  
  App.create can now spawn a background thread that performs the warmup.
  ```
- [`131b293`](https://github.com/ghostty-org/ghostty/commit/131b293dbbf426acf57618bc43bef0a4fe260d12) renderer/metal: warm up the Metal device machinery at app creation ([@mitchellh](https://github.com/mitchellh))
  ```text
  The first Metal device query in a process (MTLCopyAllDevices) takes
  multiple milliseconds; once the framework is warm, subsequent queries
  are effectively free (measured ~15ms cold, ~1us warm in isolation).
  This cost was paid during the first surface's renderer
  initialization, on the critical path to the first window.
  
  Measured on macOS (Apple Silicon) with local timing instrumentation
  during app launch, first surface renderer initialization:
  
    GraphicsAPI.init before: 4227us (device query ~3.5ms)
    GraphicsAPI.init after:  ~900us (device query 20-25us)
  ```
- [`de1336f`](https://github.com/ghostty-org/ghostty/commit/de1336faddbdffc8fb4f58af3597d3f031e2b2d9) renderer/metal: warm up command queue and shader pipelines ([@mitchellh](https://github.com/mitchellh))
  ```text
  Extend the Metal portion of the startup warmup thread to also create
  (and discard) a command queue and build (and discard) the shader
  pipelines for both pixel formats we may use (which one is used
  depends on the blending config). The first command queue for a device
  and the first render pipeline state creations pay one-time driver
  setup and shader compilation costs; once warm, the real creations
  during surface initialization hit driver and OS caches.
  
  Measured on macOS (Apple Silicon) with local timing instrumentation
  during app launch, first surface renderer initialization:
  
    queue creation:  717us -> 93us
    pipeline builds: 1023us -> 347us
    renderer init total: 2777us -> 1466us
  ```
- [`db6d20d`](https://github.com/ghostty-org/ghostty/commit/db6d20dce1df0614b4903a4c5c5489a384ab8eeb) apprt/embedded: initialize the TIS keymap lazily ([@mitchellh](https://github.com/mitchellh))
  ```text
  The embedded apprt App init created the keyboard layout keymap
  eagerly, which requires talking to the text input system (TIS). The
  first TIS call in a process is slow: 6.6ms measured inside
  ghostty_app_new during app launch (up to ~30ms in a cold process).
  
  The keymap is only used for keyboard layout queries (option-as-alt
  detection, layout change reload), which happen once keyboard events
  are flowing. By then AppKit has already warmed TIS and the call is
  effectively free (~0.2us measured warm). So initialize the keymap
  lazily on first use. If the layout changes before the keymap was ever
  created, reload is a no-op since lazy init picks up the current
  layout.
  
  Measured on macOS (Apple Silicon) with local timing instrumentation
  during app launch:
  
    embedded app init before: ~6.7ms (keymap 6614us)
    embedded app init after:  ~60us (config clone only)
  ```
- [`4b1e02c`](https://github.com/ghostty-org/ghostty/commit/4b1e02c7c3cf6d6a3548a67d88d08d4962ff67ed) macos: do not load the config errors window when there are no errors ([@mitchellh](https://github.com/mitchellh))
  ```text
  Measured on macOS (Apple Silicon) during app launch, via a startup
  timeline instrumented across the Swift app and libghostty:
  
    config apply, errors step:      35.5ms -> 0.1ms
    main() -> first frame rendered: ~126ms -> ~93ms
    main() -> window visible:       ~193ms -> ~173ms
  ```
- [`da74563`](https://github.com/ghostty-org/ghostty/commit/da745630bed8689365be0ec9a0cfe283a2ed965d) macos: only check for auto-tabbing when tabbing preference is always ([@mitchellh](https://github.com/mitchellh))
  ```text
  windowDidLoad undoes macOS automatic window tabbing by inspecting
  window.tabGroup. Accessing tabGroup on a fresh window materializes
  AppKit's tab group machinery, which takes ~15-20ms and is on the
  critical path of every window creation, including the first window at
  app launch.
  
  AppKit only auto-tabs a fresh window when the system tabbing
  preference is "always": the tab bar "+" button goes through
  newWindowForTab which we intercept and route through our own tab
  logic, so it never auto-tabs. Guard the check on
  NSWindow.userTabbingPreference == .always so everyone else skips the
  tab group materialization entirely.
  
  Measured on macOS (Apple Silicon) during app launch via the startup
  timeline instrumentation:
  
    windowDidLoad tab group check: 17.8ms -> ~0ms
    main() -> window visible: median ~173ms -> ~165ms (n=7)
  ```
- [`931a538`](https://github.com/ghostty-org/ghostty/commit/931a538a3992c0f33c6647360bd15ff54f0f7a87) comments ([@mitchellh](https://github.com/mitchellh))
- [`ad08f3b`](https://github.com/ghostty-org/ghostty/commit/ad08f3b0378b119c584aa54980fc5f7fb18b45bb) macos: reduce app launch time ~15%, time to first frame ~27% ([#13722](https://github.com/ghostty-org/ghostty/issues/13722)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Startup optimizations for macOS! Highlights:
  
   * Process exec to visible window: **15% reduction, ~193ms to ~165ms.**
   * Time to first rendered frame: **27% reduction, ~126ms to ~92ms.**
  * Zig startup time goes from **20ms to ~5ms**, the remainder is
  AppKit/Swift stuff.
  
  > [!NOTE]
  >
  > "Time to first rendered frame?" I measured the time between global
  init start to the first Metal callback saying that a frame was
  completed/drawn. This is faster than when it is _presented_ because we
  can create an IOSurfaceLayer and draw to it before AppKit finishes its
  startup and shows the window. But, the good news is this means that when
  the window is shown, the frame is already drawn!
  
  See individual commits for speeds, but a summary below:
  
  1. **Resolve Sentry directories on the init thread, not startup thread
  (~3-4ms).** Sentry init already ran on a thread, but directory
  resolution happened on the main thread first, and on macOS that calls
  `NSFileManager URLForDirectory:` which is slow as shit.
  
  2. **Initialize the TIS keymap lazily (~7ms).** The keymap is only
  needed once keyboard events flow. If AppKit isn't warmed up, this is
  SLOW. Defer setup until its needed.
  
  3. **Warm up the font registry and Metal on background threads (~7ms+
  off the first surface).** The first CoreText query initializes the
  system font database (~7ms) and the first Metal device/queue/pipeline
  use pays framework init and shader compilation costs. `App.create` now
  spawns a detached warmup thread per subsystem so this overlaps config
  load, AppKit launch, and window creation. First font grid init went from
  ~4.5ms to ~1.1ms, renderer init from ~6.8ms to ~1.5ms.
  
  4. **Look up Apple Color Emoji by exact name.** We know exactly which
  font we want, so skip the system-wide `CTFontCollection` matching
  (~312us to ~13us).
  
  5. **Cache unified logging loggers per scope.** We created and released
  an `os_log_t` on every log call. I actually had a comment saying this is
  slow but probably won't matter. Well, we log a lot on startup, and this
  actually mattered.
  
  ## Warmup Threads
  
  As a note, some of the biggest speedups are by using "warmup" threads.
  These are one-time launched threads on system start that basically just
  "touch" the relevant frameworks (CoreText/Metal). The initial touching
  of these frameworks has a ton of cost associated with them (and they're
  thread-safe), so we can shave off a bunch of time by just touching them
  in the background.
  
  This sets up a race between our own startup needing it and these warmup
  threads, but in every case I measured, the warmup threads win.
  
  ## Linux
  
  All the optimizations here focused really on slow macOS APIs. I plan on
  measuring on Linux, but nothing here should slow it down.
  
  **AI usage:** Fable was used for this one to find the issues, help
  perform the measurements, and draft commit messages by splitting up my
  work. I wrote the code, then edited the commit messages. This PR message
  is fully hand-written.
  ```
- [`b8222f4`](https://github.com/ghostty-org/ghostty/commit/b8222f4a8403765050cca52c537ddd7638725457) terminal/kitty: clear placements on image retransmit ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13719
  
  The Kitty graphics protocol requires retransmitting data for a
  specific image ID to delete the previous image and all of its
  placements.
  
  Ghostty instead preserved the placement count and map when replacing image
  data. Repeated `a=T` commands therefore added one anonymous placement per
  frame and retained its tracked pin.
  
  Spec: https://sw.kovidgoyal.net/kitty/graphics-protocol/#display-images-on-screen
  ```
- [`156bc8c`](https://github.com/ghostty-org/ghostty/commit/156bc8c814292349981f3adbfb1120c3d4f02020) terminal/kitty: clear placements on image retransmit ([#13723](https://github.com/ghostty-org/ghostty/issues/13723)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13719
  
  The Kitty graphics protocol requires retransmitting data for a specific
  image ID to delete the previous image and all of its placements.
  
  Ghostty instead preserved the placement count and map when replacing
  image data. Repeated `a=T` commands therefore added one anonymous
  placement per frame and retained its tracked pin.
  
  Spec:
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#display-images-on-screen
  ```
- [`c285d3c`](https://github.com/ghostty-org/ghostty/commit/c285d3c2442f314b9b9221bc95d02108c61d8d0f) build(deps): bump dorny/paths-filter from 4.0.2 to 4.0.3 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [dorny/paths-filter](https://github.com/dorny/paths-filter) from 4.0.2 to 4.0.3.
  - [Release notes](https://github.com/dorny/paths-filter/releases)
  - [Changelog](https://github.com/dorny/paths-filter/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/dorny/paths-filter/compare/7b450fff21473bca461d4b92ce414b9d0420d706...ceb8a2b8f2d89434be7ff52d3de7ec3738c5cc9d)
  
  ---
  updated-dependencies:
  - dependency-name: dorny/paths-filter
    dependency-version: 4.0.3
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`bb876a0`](https://github.com/ghostty-org/ghostty/commit/bb876a0d286b661089b7f40dd3a6488d629beffe) build(deps): bump dorny/paths-filter from 4.0.2 to 4.0.3 ([#13718](https://github.com/ghostty-org/ghostty/issues/13718)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps [dorny/paths-filter](https://github.com/dorny/paths-filter) from
  4.0.2 to 4.0.3.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/dorny/paths-filter/releases">dorny/paths-filter's
  releases</a>.</em></p>
  <blockquote>
  <h2>v4.0.3</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>Update Outputs in readme to account for the 'every'
  predicate-quantifier by <a
  href="https://github.com/hintron"><code>@​hintron</code></a> in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/247">dorny/paths-filter#247</a></li>
  <li>fix: scope base-ignored warning to API path by <a
  href="https://github.com/saschabratton"><code>@​saschabratton</code></a>
  in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/319">dorny/paths-filter#319</a></li>
  <li>docs: add contents permission to PR example by <a
  href="https://github.com/134130"><code>@​134130</code></a> in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/248">dorny/paths-filter#248</a></li>
  <li>feat: add 'some-with-excludes' predicate quantifier by <a
  href="https://github.com/arxeiss"><code>@​arxeiss</code></a> in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/322">dorny/paths-filter#322</a></li>
  <li>Document safe handling of file list outputs in workflows by <a
  href="https://github.com/dorny"><code>@​dorny</code></a> in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/326">dorny/paths-filter#326</a></li>
  </ul>
  <h2>Security</h2>
  <ul>
  <li>Escape multi-line filenames in list-files shell and csv output] by
  <a href="https://github.com/ken-matsui"><code>@​ken-matsui</code></a>
  and <a href="https://github.com/tjswlsgg"><code>@​tjswlsgg</code></a> in
  <a
  href="https://github.com/advisories/GHSA-7hc6-8hq5-9q2m">https://github.com/advisories/GHSA-7hc6-8hq5-9q2m</a></li>
  </ul>
  <h2>New Contributors</h2>
  <ul>
  <li><a href="https://github.com/hintron"><code>@​hintron</code></a> made
  their first contribution in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/247">dorny/paths-filter#247</a></li>
  <li><a href="https://github.com/134130"><code>@​134130</code></a> made
  their first contribution in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/248">dorny/paths-filter#248</a></li>
  <li><a href="https://github.com/arxeiss"><code>@​arxeiss</code></a> made
  their first contribution in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/322">dorny/paths-filter#322</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/dorny/paths-filter/compare/v4...v4.0.3">https://github.com/dorny/paths-filter/compare/v4...v4.0.3</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/dorny/paths-filter/blob/master/CHANGELOG.md">dorny/paths-filter's
  changelog</a>.</em></p>
  <blockquote>
  <h1>Changelog</h1>
  <h2>v4.0.3</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/326">Document
  safe handling of file list outputs in workflows</a></li>
  <li><a href="https://github.com/advisories/GHSA-7hc6-8hq5-9q2m">Escape
  multi-line filenames in list-files shell and csv output</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/322">Add
  'some-with-excludes' predicate quantifier</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/248">Add
  contents permission to PR example</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/319">Scope
  base-ignored warning to API path</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/247">Update
  outputs in readme to account for the 'every'
  predicate-quantifier</a></li>
  </ul>
  <h2>v4.0.2</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/317">Work
  around git dubious ownership errors in container jobs</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/303">Use
  rev-parse instead of branch --show-current for older git compat</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/282">Fix
  warning message</a></li>
  </ul>
  <h2>v4.0.1</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/255">Support
  merge queue</a></li>
  </ul>
  <h2>v4.0.0</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/294">Update
  action runtime to node24</a></li>
  </ul>
  <h2>v3.0.4</h2>
  <ul>
  <li><a href="https://github.com/advisories/GHSA-7hc6-8hq5-9q2m">Escape
  multi-line filenames in list-files shell and csv output</a></li>
  </ul>
  <h2>v3.0.3</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/279">Add
  missing predicate-quantifier</a></li>
  </ul>
  <h2>v3.0.2</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/224">Add
  config parameter for predicate quantifier</a></li>
  </ul>
  <h2>v3.0.1</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/133">Compare
  base and ref when token is empty</a></li>
  </ul>
  <h2>v3.0.0</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/210">Update to
  Node.js 20</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/215">Update
  all dependencies</a></li>
  </ul>
  <h2>v2.11.1</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/167">Update
  @​actions/core to v1.10.0 - Fixes warning about deprecated
  set-output</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/168">Document
  need for pull-requests: read permission</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/164">Updating
  to actions/checkout@v3</a></li>
  </ul>
  <h2>v2.11.0</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/157">Set
  list-files input parameter as not required</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/161">Update
  Node.js</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/162">Fix
  incorrect handling of Unicode characters in exec()</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/163">Use
  Octokit pagination</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/160">Updates
  real world links</a></li>
  </ul>
  <h2>v2.10.2</h2>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/ceb8a2b8f2d89434be7ff52d3de7ec3738c5cc9d"><code>ceb8a2b</code></a>
  Update CHANGELOG.md for v4.0.3 and v3.0.4 (<a
  href="https://redirect.github.com/dorny/paths-filter/issues/327">#327</a>)</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/ef09b88f3eacdbec6ce135a7c9a193a6849545c1"><code>ef09b88</code></a>
  Document safe handling of file list outputs in workflows (<a
  href="https://redirect.github.com/dorny/paths-filter/issues/326">#326</a>)</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/44adc5b06dc135dba334efce9bf3cf0624512d2d"><code>44adc5b</code></a>
  Merge commit from fork</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/4711b7a31b4aa89103d8c6ffab2e3b8e7b6381c7"><code>4711b7a</code></a>
  feat: add 'some-with-excludes' predicate quantifier (<a
  href="https://redirect.github.com/dorny/paths-filter/issues/322">#322</a>)</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/93c889f9e58fca66f35a0c83d8673ac7e88bb70a"><code>93c889f</code></a>
  fix: escape multi-line filenames in list-files shell and csv output</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/b41dfa943b1939b9b646f67753bfe35cf6e4de03"><code>b41dfa9</code></a>
  docs: add contents permission to PR example (<a
  href="https://redirect.github.com/dorny/paths-filter/issues/248">#248</a>)</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/9af6e5a9d010d1ae8ec570390b3d793e2b70a402"><code>9af6e5a</code></a>
  fix: scope base-ignored warning to API path (<a
  href="https://redirect.github.com/dorny/paths-filter/issues/319">#319</a>)</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/cae9006b65a1a53044b518c68e13e835c54948a7"><code>cae9006</code></a>
  docs: update outputs in readme to account for the 'every'
  predicate-quantifie...</li>
  <li>See full diff in <a
  href="https://github.com/dorny/paths-filter/compare/7b450fff21473bca461d4b92ce414b9d0420d706...ceb8a2b8f2d89434be7ff52d3de7ec3738c5cc9d">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=dorny/paths-filter&package-manager=github_actions&previous-version=4.0.2&new-version=4.0.3)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## August 9, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/31337999494), [2](https://github.com/ghostty-org/ghostty/actions/runs/31325264351), [3](https://github.com/ghostty-org/ghostty/actions/runs/31320152152), [4](https://github.com/ghostty-org/ghostty/actions/runs/31313857575), [5](https://github.com/ghostty-org/ghostty/actions/runs/31293445585), [6](https://github.com/ghostty-org/ghostty/actions/runs/31292361837)  
Summary: 6 runs • 27 commits • 6 authors

### Changes

- [`0aa71d0`](https://github.com/ghostty-org/ghostty/commit/0aa71d02ed068a3a036721ab9e480cbdf82ac329) terminal: reduce Parser.Action log formatting code size ([@mitchellh](https://github.com/mitchellh))
  ```text
  Shrinks libghostty-vt dylib by ~2%.
  ```
- [`f368543`](https://github.com/ghostty-org/ghostty/commit/f36854345e50fe382f37a6ef5859f9013787a23b) libghostty: skip stack traces in release panic handlers ([@mitchellh](https://github.com/mitchellh))
  ```text
  The default Zig panic handler unwinds the stack and symbolicates it,
  which drags in ~160KB worth of helper machinery. For an embedded library
  this isn't great because the embedder's environment should be providing
  this as long as libghostty is compiled with symbols or has a way to
  symbolize.
  
  Change ReleaseFast/ReleaseSmall libghostty-vt builds to use a custom
  panic handler. Debug/ReleaseSafe keep the full Zig handlers.
  
  This shrinks libghostty-vt on macOS by ~160KB (~9%).
  ```
- [`579db41`](https://github.com/ghostty-org/ghostty/commit/579db418934a5990296b7fd65d1b6b586b46dfc6) libghostty: log to stderr with raw writes, not lockStderr ([@mitchellh](https://github.com/mitchellh))
  ```text
  see the prior commit, but most importantly this makes it so we can
  replace our IO impl from Threaded.
  ```
- [`82df79e`](https://github.com/ghostty-org/ghostty/commit/82df79ec8d2c61f3beb3ecfc543ed32cb4aba450) libghostty: replace Io.Threaded with custom Io impl (TinyIo) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a new Io implementation `TinyIo` that only supports the operations
  we need and doesn't support concurrency. This shrinks the binary size
  of libghostty by anywhere from ~100KB (macOS) to ~200KB (Linux) and
  runtime memory requirements by over 256KB (the thread-local storage
  `std.Io.Threaded` creates plus the 18KB threaded structure is gone).
  
  `TinyIo` is POSIX-only: Windows keeps std.Io.Threaded, and on
  freestanding targets (wasm) TinyIo degrades to std.Io.failing
  behavior just like before.
  
  It is also exported from the Zig module as `ghostty.TinyIo` so
  Zig embedders can opt into the same size win when constructing
  terminals.
  ```
- [`d524a0f`](https://github.com/ghostty-org/ghostty/commit/d524a0fe645cfd4d9ae27bd8451b934dcf2ebaef) libghostty: guard release builds against std debug Io ([@mitchellh](https://github.com/mitchellh))
  ```text
  Release libghostty-vt builds carefully avoid referencing
  std.Options.debug_io because its default implementation is
  std.Io.Threaded, and referencing that vtable keeps every operation
  Threaded supports linked into the binary: roughly 110KB of unreachable
  code. Nothing references it today, but any std.debug.print,
  std.debug.lockStderr, or std.log default-handler call added to
  release-reachable code would silently reintroduce all of it.
  
  Declare std_options_debug_io in the root module so std uses our value
  instead of constructing the Threaded default. Development builds
  (Debug, ReleaseSafe, tests) forward the std default so std.debug.print
  and friends work normally. ReleaseFast and ReleaseSmall builds declare
  it as a @compileError: since std only analyzes the declaration lazily,
  at the moment something references a debug Io code path, the error
  fires exactly at the offending reference, turning a silent size
  regression into a build failure with a message explaining the
  alternatives.
  
  Release binaries are byte-identical when the guard is not tripped.
  ```
- [`a15ddda`](https://github.com/ghostty-org/ghostty/commit/a15dddae2a497e6540feca5c6adc7e86edd59adb) TinyIo: fix failing tests in CI ([@mitchellh](https://github.com/mitchellh))
- [`fea378e`](https://github.com/ghostty-org/ghostty/commit/fea378e565c8ddb7f49808c4f2e36a4a932e35ff) libghostty: reduce binary size ~16% (macOS), ~22% (Linux) ([#13715](https://github.com/ghostty-org/ghostty/issues/13715)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This shrinks the binary size of libghostty-vt by **16% on aarch64 macOS
  and 22% on x86_64 Linux**. It also shrinks the in-memory footprint by
  ~256KB per thread + ~20KB per app. All benchmarks remain the same, no
  speedups or slowdowns.
  
  Each commit message explains an individual tactic used, but to
  summarize:
  
  1. **No stack traces in release panic handlers (~160KB).** This requires
  the Zig stack unwind and symbolication logic. I don't think this makes
  sense in an embedded library because the embedder should handle this.
  
  2. **An alternate `std.Io` implementation called `TinyIo` (~100KB to
  200KB).** See later... since this is the big one.
  
  3. **Disable recursive Parser.Action logging (~35KB).** We now only log
  the top-level fields of a Parser.Action, which lowers the amount of
  `std.fmt` codegen significantly.
  
  All sizes above are aarch64 macOS and x86_64 Linux ReleaseFast
  libghostty builds.
  
  ## TinyIo
  
  I think the main complexity introduction here is our alternate `std.Io`
  implementation `TinyIo`. This is an IO implementation that implements IO
  operations we need through direct syscalls and does not support
  concurrency or any other options like network, progress, etc.
  
  Why? Because of the way `std.Io` works through vtable dispatch, the
  linker and dead code removal can't prune ANY of the function pointers.
  So our binary has full implementations of all the networking,
  concurrency, etc. related code even though we don't use it.
  
  This has a runtime effect too: even though we put `std.Io.Threaded` in
  single-threaded mode, it still allocates ~256KB of TLS _per thread_, and
  its raw struct state is ~18KB (versus 80 _bytes_ for `TinyIo`).
  
  For future maintenance: I exhaustively implemented the vtable rather
  than use the failing vtable from Zig stdlib so any Zig changes to add
  new fields to this error so we can determine if we want to support it or
  not.
  ```
- [`034506f`](https://github.com/ghostty-org/ghostty/commit/034506f14562242c70618aaf5775366766653ffd) gtk: add +new-tab cli action ([@jcollie](https://github.com/jcollie))
- [`9d8fbd1`](https://github.com/ghostty-org/ghostty/commit/9d8fbd15b3b4e385b82c1a9e31cdbb99a74dabd6) gtk: add +new-tab action ([#11762](https://github.com/ghostty-org/ghostty/issues/11762)) ([@jcollie](https://github.com/jcollie))
  ```text
  This PR adds a `+new-tab` CLI action, useful for automation on GTK. This
  mainly re-uses machinery added for the `+new-window`, but adds in a
  unique surface ID for identifying surfaces for IPC purposes (and
  eliminates use of raw pointers for callbacks from notifications).
  ```
- [`16e13a5`](https://github.com/ghostty-org/ghostty/commit/16e13a59aeda57ccb1b9998ab989615960dbcafb) build: fix Linux Android SDK fallback path ([@fornwall](https://github.com/fornwall))
  ```text
  Use the standard ~/Android/Sdk capitalization for the Linux SDK fallback.
  
  This lets NDK discovery work when neither ANDROID_NDK_HOME nor an SDK
  environment variable is set.
  ```
- [`74f91d1`](https://github.com/ghostty-org/ghostty/commit/74f91d1b439e7b906f003e60a65bd8994c3c77a5) macOS: support `drag-handle` config ([@bo2themax](https://github.com/bo2themax))
- [`fde9e28`](https://github.com/ghostty-org/ghostty/commit/fde9e281c4a6bd9e62d87eedc66e3c3dc48e40cc) agents: remove double negative ([@jparise](https://github.com/jparise))
- [`349664f`](https://github.com/ghostty-org/ghostty/commit/349664f031852bc6cca44c96dda7bf2b779d0402) agents: remove double negative ([#13710](https://github.com/ghostty-org/ghostty/issues/13710)) ([@mitchellh](https://github.com/mitchellh))
- [`da59a2e`](https://github.com/ghostty-org/ghostty/commit/da59a2ec42744e81c4cdafbd2a3507f257c455be) macOS: support `drag-handle` config ([#13709](https://github.com/ghostty-org/ghostty/issues/13709)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Closes https://github.com/ghostty-org/ghostty/discussions/12332
  
  Also a tiny rephrasing for the documentation.
  ```
- [`2dc0883`](https://github.com/ghostty-org/ghostty/commit/2dc08839b1a1a331d9ba71ca097c5f8db2965182) build: fix Linux Android SDK fallback path ([#13705](https://github.com/ghostty-org/ghostty/issues/13705)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Use the standard `~/Android/Sdk` capitalization for the Linux SDK
  fallback.
  
  This lets NDK discovery work when neither `ANDROID_NDK_HOME` nor an
  `SDK` environment variable is set.
  ```
- [`c6e7e9e`](https://github.com/ghostty-org/ghostty/commit/c6e7e9e4e2fa27e1a5dea57e878eb1146faaf62b) config: add `drag-handle` ([@pluiedev](https://github.com/pluiedev))
- [`65a3e66`](https://github.com/ghostty-org/ghostty/commit/65a3e666efdda5191051f94a5414eb2cf516245c) gtk: drag overlay toggle ([@pluiedev](https://github.com/pluiedev))
- [`850ca8c`](https://github.com/ghostty-org/ghostty/commit/850ca8c7b1c69078621aea638bb6564d7b3d53b5) gtk: rebind is-split after moving split cross-tree ([@pluiedev](https://github.com/pluiedev))
  ```text
  It turns out we never unbound the split from its original tree after
  moving, which means `is-split` in particular is desynced and leads to
  hilarious artifacts like how `unfocused-split-*` options just stop
  working properly. I only realized this is a thing after the naïve
  drag handle config option didn't work properly. Fun!
  ```
- [`05221c1`](https://github.com/ghostty-org/ghostty/commit/05221c11c9db0715666fc6e038915128fc6a563e) core,gtk: add `drag-handle` config ([#13706](https://github.com/ghostty-org/ghostty/issues/13706)) ([@pluiedev](https://github.com/pluiedev))
  ```text
  Fixes hundreds of complaints about the fact that drag handles cannot be
  hidden, on GTK at least.
  
  I'm not sure if we ever made an issue for this? If you come across any
  discussions asking for this, please link them here :)
  ```
- [`74efadb`](https://github.com/ghostty-org/ghostty/commit/74efadb446205eb052ce10d202300b2dc8970947) lib-vt: answer XTGETTCAP queries ([@fornwall](https://github.com/fornwall))
  ```text
  Ghostty's full termio path answers XTGETTCAP from the static terminfo
  map, but terminal/stream_terminal.zig, which backs libghostty-vt,
  parses the same DCS request and then discards it. There is no XTGETTCAP
  effect either, so an embedder cannot restore the replies through the
  C API.
  
  Programs query these over SSH instead of assuming the remote host has
  the client's terminfo entry. This matters more for an embedder than for
  the desktop app, which can install its entry on the remote through
  shell integration.
  
  Answer the queries in stream_terminal the same way termio does: look
  up each requested key in the static terminfo map and write the reply
  to the pty, skipping the lookups entirely when no write_pty effect is
  set. The map now stores null-terminated responses so they can be
  handed straight to write_pty without copying. terminal/dcs.zig and the
  termio path are unchanged.
  
  "TN" is handled separately. It names the terminfo entry the terminal
  runs as, so it has to agree with TERM -- which is set in
  termio/Exec.zig, a layer libghostty-vt does not contain. The library
  never sees TERM and cannot answer on the embedder's behalf, and
  answering with Ghostty's own entry from the static map would misreport
  every embedder, so "TN" is intercepted before the map lookup. The name
  is instead configured through a new option,
  GHOSTTY_TERMINAL_OPT_TERMINFO_NAME: the string is copied into the
  terminal, names longer than 128 bytes are rejected, and while unset
  the query goes unanswered.
  
  This is the first dependency from src/terminal on src/terminfo, so
  libghostty-vt now carries Ghostty's terminfo table: +16,023 bytes
  (+1.9%) on a wasm32-freestanding ReleaseSmall build.
  ```
- [`f64f4ac`](https://github.com/ghostty-org/ghostty/commit/f64f4aca2c29b554d111b36c3d946a9bddd159ff) lib-vt: answer XTGETTCAP queries ([#13530](https://github.com/ghostty-org/ghostty/issues/13530)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Ghostty's full termio path answers XTGETTCAP from the static terminfo
  map, but `terminal/stream_terminal.zig`, which backs libghostty-vt,
  parses the same DCS request and then discards it. There is no XTGETTCAP
  effect either, so an embedder cannot restore the replies through the C
  API.
  
  Programs query these over SSH instead of assuming the remote host has
  the client's terminfo entry. This matters more for an embedder than for
  the desktop app, which can install its entry on the remote through shell
  integration.
  
  Answer the queries in `stream_terminal` the same way termio does: look
  up each requested key in the static terminfo map and write the reply to
  the pty, skipping the lookups entirely when no `write_pty` effect is
  set. The map now stores null-terminated responses so they can be handed
  straight to `write_pty` without copying. `terminal/dcs.zig` and the
  termio path are unchanged.
  
  `TN` is handled separately. It names the terminfo entry the terminal
  runs as, so it has to agree with `TERM` — which is set in
  `termio/Exec.zig`, a layer libghostty-vt does not contain. The library
  never sees `TERM` and cannot answer on the embedder's behalf, and
  answering with Ghostty's own entry from the static map would misreport
  every embedder, so `TN` is intercepted before the map lookup. The name
  is instead configured through a new option,
  `GHOSTTY_TERMINAL_OPT_TERMINFO_NAME`: the string is copied into the
  terminal, names longer than 128 bytes are rejected, and while unset the
  query goes unanswered.
  
  This is the first dependency from `src/terminal` on `src/terminfo`, so
  libghostty-vt now carries Ghostty's terminfo table: +16,023 bytes
  (+1.9%) on a `wasm32-freestanding` `ReleaseSmall` build.
  
  ---
  
  AI usage: Created with claude code and opus 5. I have reviewed the code
  and made modifications where it made sense. I have also tested this end
  to end in an application.
  ```
- [`afb351f`](https://github.com/ghostty-org/ghostty/commit/afb351f8385d8b895671cb398d13fb39e06611f4) terminal/stream: fast-path APC termination ([@mitchellh](https://github.com/mitchellh))
  ```text
  APC payload bytes are bulk consumed, but the terminating byte still passed
  through the generic parser action loop. Handle ESC and C1 ST directly after
  bulk consumption while leaving other transitions on the scalar path.
  ```
- [`b537282`](https://github.com/ghostty-org/ghostty/commit/b537282411ae731f3d49705be391320ff5f51e9e) terminal/apc: support reporting unknown APC sequences ([@mitchellh](https://github.com/mitchellh))
- [`6b990de`](https://github.com/ghostty-org/ghostty/commit/6b990de5be7fcce9ffc7bed1a713f64c8503fbff) terminal: C API for unknown sequences ([@mitchellh](https://github.com/mitchellh))
- [`7e8b4f3`](https://github.com/ghostty-org/ghostty/commit/7e8b4f360be6f9aea0bced4641e25dd564d60abc) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`94beef8`](https://github.com/ghostty-org/ghostty/commit/94beef81efad44514c328564d2e6c2fefc243712) libghostty: effect for unknown sequence (APC only this PR) ([#13702](https://github.com/ghostty-org/ghostty/issues/13702)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This introduces a new effect for Zig/C callers to detect unknown
  sequences.
  
  This PR starts only with APC, but the API shape is such that we can add
  other types (OSC next) in future PRs. The goal of this is to have zero
  overhead in the disabled/undetected (both) case, and minimal overhead in
  the detected case.
  
  This is important in particular for libghostty consumers because it
  allows them to implement their own custom protocols and/or support
  features libghostty doesn't support. It isn't possible to support them
  at the same performance libghostty does but supporting them in general
  is usually valuable.
  
  From a Zig API to enable this, users must set `unknown_max_bytes` for
  the APC handler AND update their stream handler to recognize unknown
  sequences. The built-in `stream_terminal` stream type has an exposed
  callback for this, so both must be set.
  ```
- [`163e229`](https://github.com/ghostty-org/ghostty/commit/163e229756e632e39838a9f6e26402269dda213a) Update iTerm2 colorschemes ([#13704](https://github.com/ghostty-org/ghostty/issues/13704)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260803-155300-875a82f
  ```

