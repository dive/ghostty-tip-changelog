> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: July 7, 2026 at 06:41 UTC.

## July 7, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/28841679058), [2](https://github.com/ghostty-org/ghostty/actions/runs/28840138366), [3](https://github.com/ghostty-org/ghostty/actions/runs/28839347060)  
Summary: 3 runs • 8 commits • 4 authors

### Changes

- [`6e267d3`](https://github.com/ghostty-org/ghostty/commit/6e267d336396946e2e32be68e6b6d8a1cd85b60b) macOS: use the  `getOpinionatedStringContents` same as paste ([@bo2themax](https://github.com/bo2themax))
- [`c41c6b8`](https://github.com/ghostty-org/ghostty/commit/c41c6b81a4642ccba18d47b375d9495664de72a0) macOS: use the`getOpinionatedStringContents` same as paste for dragging ([#13212](https://github.com/ghostty-org/ghostty/issues/13212)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The only difference of getting the string contents between dragging
  pasteboard and general pasteboard is the URL now. It was first
  introduced in #4962, I don't why it was added, since `public.url` often
  comes with `public.utf8-plain-text` when dragging.
  
  I also check with iTerm's
  [PTYTextView](https://github.com/gnachman/iTerm2/blob/f267f243e59855e2b1b44df3343d07174de7857b/sources/TerminalView/PTYTextView.m#L307),
  it doesn't register URL either, so I think it's safe for us to remove
  it.
  
  > I checked the iTerm's source after my changes, I hope that doesn't
  violates any licensing
  ```
- [`d8464a5`](https://github.com/ghostty-org/ghostty/commit/d8464a5f5b1755c606486ce0da80160c52a5b78b) Update VOUCHED list ([#13229](https://github.com/ghostty-org/ghostty/issues/13229)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13129#discussioncomment-17555238)
  from @tristan957.
  
  Vouch: @escalonc
  ```
- [`dac341c`](https://github.com/ghostty-org/ghostty/commit/dac341cad56fecc436750525fa7b8757a6028ffc) font/sprite: make cursor height respect adjust-cursor-height ([@qwerasd205](https://github.com/qwerasd205))
  ```text
  This was a regression caused by the sprite face rework (#7732), I'm
  surprised it went unnoticed for so long.
  ```
- [`e8f3f6c`](https://github.com/ghostty-org/ghostty/commit/e8f3f6c438ac61fbb6189d4a88a7c7716f658219) font/sprite: add regression test for cursor-height metric ([@qwerasd205](https://github.com/qwerasd205))
- [`446f80f`](https://github.com/ghostty-org/ghostty/commit/446f80f4edd16d217e8ec928664d86a529b3a223) terminal: render state update optimizations (~2.7x to ~11x less lock hold) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This optimizes `RenderState.update`, the per-frame call that snapshots
  terminal state for the renderer and is the main reason the renderer
  thread holds the terminal lock.
  
  Lock hold time is reduced ~2.7x to ~11x depending on the frame.
  
  ## The changes
  
  1. iterate page chunks instead of rows in `update`
  2. classify cells with masked vector compares.
  3. split the update into `beginUpdate`/`endUpdate` phases. There's a
     lot to be gained by accumulating data with the lock held and then
     processing it out of the lock.
  4. generalize the masked-compare scans into `page.Mask`. This is just
     a really common pattern we're doing now and it yields a ton of great
     value. Its error prone so lets make it a tested helper.
  
  ## Benchmarks
  
  Measured with the new `ghostty-bench +screen-clone` modes (`render`,
  `render-locked`, `render-clean`, `render-partial`), 120x80 terminal, M4
  Max, macOS 26, ReleaseFast, hyperfine means of 10+ runs, per-update
  times derived from fixed-count update loops with process startup
  subtracted. "Lock held" is the time the terminal lock must be held per
  update; "before" held the lock for the entire update.
  
  | scenario | before (lock held) | after (lock held) | after (total) | lock change |
  |----------|--------------------|-------------------|---------------|-------------|
  | clean frame (nothing dirty) | 202 ns | 19 ns | 19 ns | 10.9x |
  | partial frame (1 dirty row) | 290 ns | 54 ns | 54 ns | 5.4x |
  | full rebuild, lightly styled | 6.9 µs | 2.5 µs | 3.0 µs | 2.7x |
  | full rebuild, fully styled | 9.3 µs | 2.4 µs | 8.0 µs | 3.8x |
  | full rebuild, fully styled, 250x150 | 49.9 µs | 9.4 µs | 31.6 µs | 5.3x |
  | full rebuild, plain text | 1.9 µs | 1.9 µs | 1.9 µs | 1.0x (memcpy floor) |
  
  The clean and partial cases are the steady-state frame costs (cursor
  blink, mouse movement, typing). The full-rebuild cases are the contended
  ones: colored scrolling output (build logs, htop, vim) moves the
  viewport pin every frame, forcing a full rebuild exactly when the IO
  thread is busiest, so that row of the table is where lock contention
  actually hurts. Plain text was already at the memcpy floor and is
  unchanged.
  
  ## LLM Notes
  
  This work was driven by Fable 5: benchmarks, optimizations, the property
  test, and the measurements above. I reviewed every line, simplified the
  design in a few places (API naming, the Mask helper shape), and re-ran
  the verifications myself.
  ```
- [`98a7c0f`](https://github.com/ghostty-org/ghostty/commit/98a7c0f6f95f412504d6d45fba9f8acc6ed1f6da) terminal: render state update optimizations (~2.7x to ~11x lock time reduction) ([#13227](https://github.com/ghostty-org/ghostty/issues/13227)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This optimizes `RenderState.update`, the per-frame call that snapshots
  terminal state for the renderer and is the main reason the renderer
  thread holds the terminal lock.
  
  Lock hold time is reduced ~2.7x to ~11x depending on the frame. This was
  already a super fast part of Ghostty, so I don't expect any noticeable
  changes for end users or library users. But, why not be fast?
  
  ## The changes
  
  1. iterate page chunks instead of rows in `update`
  2. classify cells with masked vector compares.
  3. split the update into `beginUpdate`/`endUpdate` phases. There's a lot
  to be gained by accumulating data with the lock held and then processing
  it out of the lock.
  4. generalize the masked-compare scans into `page.Mask`. This is just a
  really common pattern we're doing now and it yields a ton of great
  value. Its error prone so lets make it a tested helper.
  
  ## Benchmarks
  
  Measured with the new `ghostty-bench +screen-clone` modes (`render`,
  `render-locked`, `render-clean`, `render-partial`), 120x80 terminal, M4
  Max, macOS 26, ReleaseFast, hyperfine means of 10+ runs, per-update
  times derived from fixed-count update loops with process startup
  subtracted. "Lock held" is the time the terminal lock must be held per
  update; "before" held the lock for the entire update.
  
  | scenario | before (lock held) | after (lock held) | after (total) |
  lock change |
  
  |----------|--------------------|-------------------|---------------|-------------|
  | clean frame (nothing dirty) | 202 ns | 19 ns | 19 ns | 10.9x |
  | partial frame (1 dirty row) | 290 ns | 54 ns | 54 ns | 5.4x |
  | full rebuild, lightly styled | 6.9 µs | 2.5 µs | 3.0 µs | 2.7x |
  | full rebuild, fully styled | 9.3 µs | 2.4 µs | 8.0 µs | 3.8x |
  | full rebuild, fully styled, 250x150 | 49.9 µs | 9.4 µs | 31.6 µs |
  5.3x |
  | full rebuild, plain text | 1.9 µs | 1.9 µs | 1.9 µs | 1.0x (memcpy
  floor) |
  
  The clean and partial cases are the steady-state frame costs (cursor
  blink, mouse movement, typing). The full-rebuild cases are the contended
  ones: colored scrolling output (build logs, htop, vim) moves the
  viewport pin every frame, forcing a full rebuild exactly when the IO
  thread is busiest, so that row of the table is where lock contention
  actually hurts. Plain text was already at the memcpy floor and is
  unchanged.
  
  ## LLM Notes
  
  This work was driven by Fable 5: benchmarks, optimizations, the property
  test, and the measurements above. I reviewed every line, simplified the
  design in a few places (API naming, the Mask helper shape), and re-ran
  the verifications myself.
  ```
- [`cabbdee`](https://github.com/ghostty-org/ghostty/commit/cabbdee32b75ac71f0e2b19b31e4c25da97b5461) Fix `adjust-cursor-height` regression ([#13225](https://github.com/ghostty-org/ghostty/issues/13225)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The `cursor-height` metric (and corresponding `adjust-`) was introduced
  by #3062 but the sprite face rework in #7732 accidentally removed the
  logic that it relied on. I've moved the logic to live inside of the
  sprite face itself (which, I think, was my plan while writing the
  rework, I just forgot to actually do it lol), and added a test for the
  height metric being respected and the re-centering being performed
  correctly.
  
  This problem came to my attention because of #13221, which didn't go
  about doing the fix the right way, but did make me realize that it was a
  problem in the first place (since I had thought that I had already
  implemented this logic when doing the rework!)
  
  ### Verification
  
  https://github.com/user-attachments/assets/4074690b-846e-442d-8ec0-91a34042f6eb
  ```

## July 6, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/28827535657), [2](https://github.com/ghostty-org/ghostty/actions/runs/28807063048), [3](https://github.com/ghostty-org/ghostty/actions/runs/28797087835)  
Summary: 3 runs • 16 commits • 1 authors

### Changes

- [`4c5b1d5`](https://github.com/ghostty-org/ghostty/commit/4c5b1d5d52a5c8a79be2db897c8fbddaad64f1d2) bench: terminal-stream reads 64KiB chunks to match the IO thread ([@mitchellh](https://github.com/mitchellh))
  ```text
  The terminal-stream benchmark fed the stream in 4KiB chunks while
  the real IO thread reads from the pty into 64KiB buffers (see
  buffer_capacity in termio/Exec.zig) and hands those to the stream
  whole. Chunk size affects measurement in two ways: it determines
  how often the stream crosses a chunk boundary (partial UTF-8
  sequences, escape sequences split mid-parse) and how many read
  syscalls the harness itself performs (a 2.6 GB corpus is ~636k
  pread calls at 4KiB versus ~40k at 64KiB).
  
  This bumps the benchmark read and dispatch buffers to 64KiB so the
  stream is exercised with realistic chunk sizes. Measured with
  ghostty-bench terminal-stream on a 2.6 GB recording of real
  terminal sessions (120x80, M4 Max, ReleaseFast, hyperfine means):
  
  | harness      | time            | throughput |
  |--------------|-----------------|------------|
  | 4KiB chunks  | 9.651 s ± 0.013 | 270 MB/s   |
  | 64KiB chunks | 9.582 s ± 0.101 | 272 MB/s   |
  
  The stream itself is barely chunk-size sensitive (most time is in
  parsing and terminal state updates), but the harness now matches
  what the IO thread actually does, and later commits are measured
  against this configuration.
  ```
- [`cb4c49f`](https://github.com/ghostty-org/ghostty/commit/cb4c49fbf206ce0c474493a1354629ebba43e2b9) terminal: scalar UTF-8 decode consumes partial sequences cut off by ESC ([@mitchellh](https://github.com/mitchellh))
  ```text
  The scalar fallback of utf8DecodeUntilControlSeq (used when SIMD is
  disabled, e.g. wasm builds) treated a valid-so-far but incomplete
  UTF-8 sequence at the end of its decode region as pending input in
  all cases: it stopped without consuming the bytes so a future chunk
  could complete the sequence. That is correct when the region ends
  at the end of the input, but the region can also be bounded by an
  ESC byte. In that case the sequence can never be completed (the
  next byte is already known to be ESC), and the SIMD implementation,
  via simdutf, replaces the ill-formed prefix with U+FFFD and
  consumes up to the ESC. The two implementations disagreed on both
  the consumed count and the decoded output for inputs like
  "\xC2\x1B[0m".
  
  The divergence is invisible at the stream level (the pending bytes
  take the scalar nextUtf8 path which also emits a replacement
  character once it sees the ESC) but it means the scalar decoder is
  not a faithful reference for the SIMD one.
  
  This makes the scalar decoder treat a partial sequence bounded by
  an ESC as a maximal subpart per Unicode 3-7: one U+FFFD, consumed
  through the end of the region. Truncation at the true end of input
  still leaves the bytes pending. Also adds a differential fuzz test
  that runs 10k random mixtures of ASCII, escapes, controls, and
  valid/invalid UTF-8 through both implementations and requires
  identical results, which is what caught this.
  ```
- [`083d970`](https://github.com/ghostty-org/ghostty/commit/083d9709be0dc19dbd2392718288d5b6b578ea1d) terminal: decode ASCII inline in the SIMD scan for ESC ([@mitchellh](https://github.com/mitchellh))
  ```text
  Profiling terminal-stream on a 2.6 GB recording of real terminal
  sessions showed ~9% of total time inside the UTF-8 decode stage,
  and most of it was not the decode itself: real streams contain an
  escape sequence every ~18 bytes, so utf8DecodeUntilControlSeq is
  called on short printable runs, and each call paid simdutf setup
  plus its scalar rewind_and_convert_with_errors tail (which handles
  the last partial SIMD block of every conversion) for only a
  handful of bytes. The scalar tail alone accounted for ~3.4% of
  total time.
  
  Terminal input is also overwhelmingly ASCII, for which UTF-8 to
  UTF-32 "decoding" is just widening each byte to 32 bits. This
  fuses the two passes: while scanning each chunk for ESC we also
  check for bytes >= 0x80 and widen pure-ASCII chunks straight into
  the output vector via PromoteTo, never touching simdutf. The first
  non-ASCII byte hands the remainder of the run (up to the next ESC)
  to the existing simdutf-based path, so non-ASCII text takes
  exactly the same code as before. Inputs shorter than one vector
  are handled by a scalar byte loop that likewise skips simdutf for
  ASCII.
  
  The widening store needs a dedicated path for the HWY_SCALAR
  fallback target (compiled on targets without guaranteed SIMD, e.g.
  arm-linux-androideabi): its single-lane vectors cannot be halved
  so the one lane is widened directly.
  
  The new differential fuzz test verifies the SIMD implementation
  still matches the scalar reference exactly. Measured with
  ghostty-bench terminal-stream (2.6 GB real-session corpus, 87%
  printable ASCII / 5.5% ESC / 5.6% UTF-8, 120x80, M4 Max,
  ReleaseFast, hyperfine means):
  
  | stream            | before          | after           | change |
  |-------------------|-----------------|-----------------|--------|
  | real 2.6 GB corpus | 9.582 s (272 MB/s) | 9.090 s (287 MB/s) | +5.4% |
  ```
- [`300f42c`](https://github.com/ghostty-org/ghostty/commit/300f42c7a970dfbbb313fd6456d4d0eb81e8efbd) terminal: handle CSI entry bytes inline in consumeUntilGround ([@mitchellh](https://github.com/mitchellh))
  ```text
  Profiling terminal-stream on a 2.6 GB recording of real terminal
  sessions showed ~7% of time in nextNonUtf8 self, and most calls
  were for the structural bytes of CSI sequences: the '[' after ESC
  and the single byte spent in the csi_entry state (a digit, private
  marker, or final byte). Real streams contain tens of millions of
  CSI sequences, and each paid two to three function calls just to
  advance the parser through those states before the bulk parameter
  loop could take over.
  
  This lifts both transitions into the consumeUntilGround loop: the
  "ESC [" prefix is matched directly, and the csi_entry byte is
  handled by a shared csiEntryByte helper that both the loop and
  nextNonUtf8 use (the logic previously lived only in nextNonUtf8).
  A typical CSI sequence now parses entirely within
  consumeUntilGround/consumeCsiParams without any per-byte calls.
  Handlers with a vtRaw hook keep the general path since csiEntryByte
  dispatches finals directly.
  
  Measured with ghostty-bench terminal-stream (120x80, M4 Max,
  ReleaseFast, hyperfine means of 5 runs). nextNonUtf8 self time
  drops from ~7% to ~3% of the profile:
  
  | stream                     | before  | after   | change |
  |----------------------------|---------|---------|--------|
  | real 2.6 GB session corpus | 9.097 s | 8.854 s | +2.7%  |
  | csi mix (SGR/CUP, 100 MB)  | 695 ms  | 674 ms  | +3.1%  |
  ```
- [`cb2d785`](https://github.com/ghostty-org/ghostty/commit/cb2d78587194d2cc451b5078412b2612ecb2371a) terminal: fill style-only cell runs in bulk in printSliceFill ([@mitchellh](https://github.com/mitchellh))
  ```text
  Profiling terminal-stream on a 2.6 GB recording of real terminal
  sessions showed printSliceFill as the single largest item (~25% of
  total time), and disassembly showed the time split across three
  scalar loops: the run-eligibility scan over codepoints, the
  simple-cell check that guards the branch-free fill, and the general
  path that fixes up style ref counts one cell at a time. The store
  loop itself was already auto-vectorized by LLVM, but the two scans
  are early-exit search loops that LLVM does not vectorize, and the
  general path turns out to be the common case in real traffic:
  styled text constantly overwrites cells holding a different style
  (TUI redraws, scrolling colored output), so every such cell failed
  the simple check and paid a release/use pair.
  
  Three changes, which only pay off together (vectorizing the scans
  without the bulk path makes mismatch-heavy rows slower because the
  wider check re-runs for every cell the general path consumes):
  
  The run-eligibility scan handles the narrow class, codepoints in
  [0x10, 0xFF], eight lanes at a time. The simple-cell check compares
  four masked cells per iteration. And a new bulk path handles runs
  of cells that differ from the expected simple cell only by style
  id: one vector scan finds the extent of the uniformly-styled run,
  the ref counts are fixed with a single releaseMultiple/useMultiple
  pair, and the cells are filled with the same branch-free store
  loop as the simple case. Cells with graphemes, hyperlinks, or wide
  content still fall back to print().
  
  Measured with ghostty-bench terminal-stream (120x80, M4 Max,
  ReleaseFast, hyperfine means of 5 runs). The redraw corpus is a
  full-screen 80-row styled repaint whose span color rotates every
  frame, so every cell is overwritten with a different style:
  
  | stream                     | before  | after   | change |
  |----------------------------|---------|---------|--------|
  | real 2.6 GB session corpus | 8.826 s | 7.955 s | +11%   |
  | TUI redraw (100 MB)        | 348 ms  | 287 ms  | +21%   |
  ```
- [`8d663a7`](https://github.com/ghostty-org/ghostty/commit/8d663a76e935d046198256698d2bd79d35f55a40) terminal: release style refs per run instead of per cell in clearCells ([@mitchellh](https://github.com/mitchellh))
  ```text
  clearCells released the style reference of every styled cell
  individually: an array index, a ref decrement, and a liveness
  check per cell. Styled cells overwhelmingly come in runs sharing
  the same style id (a colored status bar, a highlighted region, a
  full row painted in one color), so most of that work is repeated
  bookkeeping on the same style entry.
  
  This groups consecutive cells with the same style id and releases
  each run with a single releaseMultiple call. Rows with alternating
  styles degrade to the same per-cell cost as before; uniform rows,
  the common case, do one ref-count update per run. The
  releaseMultiple assertion that the ref count is at least the run
  length holds by construction since every cell in the run held a
  reference.
  
  Measured with ghostty-bench terminal-stream (120x80, M4 Max,
  ReleaseFast, hyperfine means of 5 runs). The erase corpus paints a
  full screen of styled rows and erases it with ED 2 in a loop,
  which is the pattern full-screen TUIs produce on clear/redraw:
  
  | stream                     | before  | after   | change |
  |----------------------------|---------|---------|--------|
  | real 2.6 GB session corpus | 8.055 s | 7.965 s | +1.1%  |
  | styled paint + ED 2 (100 MB) | 260 ms | 123 ms | 2.1x   |
  ```
- [`b505315`](https://github.com/ghostty-org/ghostty/commit/b5053153f40991558cccdc369761d68be17037fe) terminal: log unsupported-input messages once per distinct value ([@mitchellh](https://github.com/mitchellh))
  ```text
  Profiling terminal-stream on a 2.6 GB recording of real terminal
  sessions showed ~5% of total time under writev, all of it log
  output: the recording triggers ~120k warnings, dominated by a few
  repeated messages ("unimplemented mode: 34", "invalid device
  attributes command", "invalid C0 character") that some program in
  the recorded session re-emitted on every frame or every prompt.
  Each occurrence pays formatting plus a blocking write syscall,
  and repeats add no diagnostic value beyond the first: the message
  already includes the offending value.
  
  These messages are emitted in response to input that the terminal
  application controls, so a misbehaving or merely chatty program
  can flood the log indefinitely. This adds a logUnsupportedOnce
  helper that suppresses repeats per (call site, value): each site
  tracks the distinct keys it has logged (the mode number, final
  byte, or first parameter, depending on the site) in a small fixed
  table of 16 u32 slots, 64 bytes per site. Real streams only ever
  produce a handful of distinct unsupported values per site, so if a
  table fills, new values are suppressed too; by then the log
  already shows the problem class and unbounded distinct values
  would flood it anyway. Slots are claimed with 32-bit atomics
  (native on wasm32) and never change afterwards, so lookups are a
  lock-free scan and the worst case race is a duplicate message.
  
  The OSC 1 change-icon message moves from info to warn to match the
  other unsupported-input messages the helper covers.
  
  Measured with ghostty-bench terminal-stream (2.6 GB real-session
  corpus, 120x80, M4 Max, ReleaseFast, hyperfine means of 5 runs,
  stderr to /dev/null which undersells the cost of a real log sink):
  
  | stream                     | before  | after   | change |
  |----------------------------|---------|---------|--------|
  | real 2.6 GB session corpus | 7.916 s | 7.674 s | +3.2%  |
  
  System time drops from 0.49 s to 0.22 s from the eliminated
  writev calls.
  ```
- [`634957c`](https://github.com/ghostty-org/ghostty/commit/634957c8e67cad5040f54cef57de5502450d1f5f) terminal: VT throughput optimizations from real-world dataset (~1.2x to ~3.4x) ([#13226](https://github.com/ghostty-org/ghostty/issues/13226)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This is a series of seven commits that optimizes VT processing
  throughput. Each commit is isolated, individually benchmarked, and
  carries a detailed commit message so please read each for details about
  each change.
  
  Whereas #13220 was driven by synthetic data, this series was driven by
  profiling a 2.6 GB recording of real terminal sessions from an asciinema
  data dump. Through this, I've been able to improve throughput processing
  the full dump from 276 to 342 MB/s on my system.
  
  > [!NOTE]
  >
  > **LLM usage:** This series of work was largely driven by Fable 5 and
  the summaries below started as LLM-written. I've proofread (and mostly
  modified) every line of work and rewritten everything to be shorter and
  more in line with how I'd describe a change. Nothing here was
  unreviewed. I also threw away 3 sets of changes I didn't agree with the
  maintenance of, but did speed up things a bit.
  
  ## The changes
  
  1. **decode ASCII inline in the SIMD scan for ESC**. Real streams call
  `utf8DecodeUntilControlSeq` on short runs (an escape every ~18 bytes),
  so ~9% of total time was simdutf setup plus its scalar tail paid per
  tiny run. The ESC scan and the UTF-8 to UTF-32 "decode" (a widening for
  ASCII) are now one pass. **Result: +5.4% on the real corpus.**
  2. **handle CSI entry bytes inline in consumeUntilGround**. The `[`
  after ESC and the single `csi_entry` byte each paid a `nextNonUtf8`
  call, two to three calls for every one of the tens of millions of CSI
  sequences in the recording. Both transitions are now handled in the
  consumeUntilGround loop, so a typical CSI parses with no per-byte calls
  at all. **Result: +2.7% real corpus, +3.1% CSI-heavy stream.**
  3. **fill style-only cell runs in bulk in printSliceFill**. The largest
  single item in the profile (~25%). The print fast path's two scans (run
  eligibility, simple-cell check) are early-exit search loops LLVM won't
  vectorize, and real traffic constantly lands in the general path because
  styled text overwrites cells styled differently (TUI redraws), paying a
  per-cell release/use pair. The scans are now vectorized and
  uniformly-styled runs are consumed wholesale: one vector scan, one
  releaseMultiple/useMultiple pair, one branch-free fill. **Result: +11%
  real corpus, +21% TUI redraw.**
  4. **release style refs per run instead of per cell in clearCells**.
  Erasing styled rows released each cell's style reference one at a time
  even though styled cells overwhelmingly share one style per run (status
  bars, highlighted regions, solid rows). Runs now release with a single
  releaseMultiple. **Result: +1.1% real corpus, 2.1x on full-screen styled
  erase.**
  5. **log unsupported-input messages once per distinct value**. The
  recording triggers ~120k warnings, dominated by a few messages some
  program re-emitted every frame ("unimplemented mode: 34"), each paying
  formatting plus a blocking writev while adding nothing beyond the first
  occurrence. A logUnsupportedOnce helper suppresses repeats per (call
  site, value) using a 64-byte lock-free table per site. **Result: +3.2%
  on the real corpus, system time halved.**
  
  ## Benchmarks
  
  Measured with `ghostty-bench +terminal-stream` (full terminal handler,
  120x80 terminal, M4 Max, macOS 26, ReleaseFast, hyperfine means of 6
  runs, 64KiB read chunks). These are parser-stage numbers, not end-to-end
  app numbers.
  
  | stream | before | after | throughput | change |
  
  |-------------------------------|---------|---------|------------------|--------|
  | real 2.6 GB session recording | 9.441 s | 7.609 s | 276 → 342 MB/s |
  1.24x |
  | ascii (no escapes) | 119 ms | 84 ms | 838 → 1186 MB/s | 1.41x |
  | TUI redraw (rotating styles) | 417 ms | 293 ms | 240 → 342 MB/s |
  1.42x |
  | styled paint + ED 2 erase | 418 ms | 124 ms | 239 → 808 MB/s | 3.38x |
  | csi mix (random-color SGR/CUP)| 695 ms | 696 ms | (adversarial) |
  ~1.0x |
  
  Note the "csi mix" benchmark above was a generated adversarial input
  e.g. a worst-case input for the changes we made. It wasn't based in
  real-world data or expectations. But I asked for it to be done so we can
  verify we don't see regressions too much (and were able to verify we see
  basically none).
  ```
- [`258de36`](https://github.com/ghostty-org/ghostty/commit/258de36d152522476b9f2443e9f37aad8cc6f79b) benchmark: terminal-stream uses the full terminal handler ([@mitchellh](https://github.com/mitchellh))
  ```text
  The terminal-stream benchmark previously used a simplified handler
  that handles print actions and drops everything else. That was
  originally intended to isolate parse and print throughput, but it
  understates the cost of escape-heavy streams: no terminal state is
  updated for CSI/OSC/ESC sequences, and because actions are
  dispatched at comptime, the unhandled action arms are eliminated
  entirely, so the benchmark measures dispatch code that doesn't
  exist in the real app.
  
  This switches the benchmark to the full readonly terminal stream
  handler (terminal.TerminalStream). Every escape sequence now
  updates real terminal state (styles, cursor movement, erases,
  modes, etc.), closely mirroring the work the real IO thread does
  per byte. This is the handler used to measure the VT throughput
  changes in the following commits.
  
  Parser-in-isolation measurement remains covered by the separate
  terminal-parser and osc-parser benchmarks, and print throughput is
  identical under both handlers since printing flows into the same
  Terminal call either way.
  ```
- [`47e26df`](https://github.com/ghostty-org/ghostty/commit/47e26df60f53471f2e210b5c43a965bf195faa42) terminal: batch printed codepoint runs into direct row fills ([@mitchellh](https://github.com/mitchellh))
  ```text
  #13209
  
  After #13209 the IO pipeline delivers the parse thread's full
  measured capacity, so IO throughput is now bound by VT processing.
  Profiling `terminal-stream` on plain text showed ~85% of wall time
  inside Terminal.print: every printable codepoint paid the full
  per-character cost (right margin computation, grapheme clustering
  checks, width lookup, wrap/insert mode checks, charset mapping,
  per-cell style bookkeeping, dirty marking, cursor advance) even
  though for typical bulk output every one of those answers is the
  same for thousands of consecutive characters.
  
  This adds a new print_slice stream action carrying a run of
  printable codepoints, emitted whenever the SIMD ground-state path
  decodes multiple codepoints at once, plus Terminal.printSlice which
  processes such runs in batch. Since action dispatch is comptime,
  delivering a slice through the existing vt handler interface has
  the same codegen as a dedicated entry point; handlers that don't
  care about batching can simply loop and treat each codepoint as a
  print action.
  
  printSlice hoists all run-invariant checks (status display, insert
  and wraparound modes, charset state, hyperlink state) out of the
  loop and then fills cells row by row. A single masked u64 compare
  classifies each destination cell as "simple" (plain codepoint cell,
  narrow, no hyperlink, style already matching the cursor); runs of
  simple cells are written with a branch-free store loop, style-only
  mismatches are handled inline with the same ref-counting printCell
  does, and anything needing real cleanup (wide spacers, grapheme
  data, hyperlinks) exits the fast path with the cursor positioned on
  the offending cell so print() handles that one codepoint with full
  generality. Dirty marking, previous_char, and cursor advancement
  happen once per row instead of once per character.
  
  The fast path handles both narrow and wide codepoints (CJK/emoji are
  written as wide+spacer_tail pair fills, including spacer-head
  handling at the right edge) and stays exact under grapheme
  clustering (mode 2027): a codepoint only joins a run if it is width
  1 or 2 and is a grapheme break from the previously written
  codepoint, so print() would never have attached it to the previous
  cell. The first codepoint of a batch defers to print() whenever the
  previous cell could carry cluster state we can't cheaply reason
  about (including a pending wrap, where print attaches to the
  pending cell instead of wrapping).
  
  Correctness is verified by a new differential fuzz test that runs
  the same operations through per-codepoint print and randomly
  chunked printSlice, comparing full screen dumps, cursor state, and
  page integrity (style refcounts, grapheme maps) after every
  operation, across wraps, margins, mode toggles, hyperlinks,
  charsets, and wide/combining/ZWJ/RI/jamo codepoints.
  
  Throughput measured with ghostty-bench terminal-stream (full
  terminal handler, 100 MB deterministic corpora, 120x80, M4 Max,
  ReleaseFast, hyperfine means of 10 runs; ~15ms process startup
  included in all numbers):
  
  | stream                    | before | after  | change |
  |---------------------------|--------|--------|--------|
  | ascii (no newlines)       | 784 ms | 138 ms | 5.7x   |
  | ascii lines               | 833 ms | 198 ms | 4.2x   |
  | unicode mixed-script      | 779 ms | 320 ms | 2.4x   |
  | CJK (all wide)            | 424 ms | 126 ms | 3.4x   |
  | unicode, mode 2027 on     | 807 ms | 367 ms | 2.2x   |
  | CJK, mode 2027 on         | 495 ms | 198 ms | 2.5x   |
  ```
- [`1a88f36`](https://github.com/ghostty-org/ghostty/commit/1a88f3622b50e8d82d3d3ef6c6a56fdbddb895c9) terminal: dispatch CSI finals directly from stream fast paths ([@mitchellh](https://github.com/mitchellh))
  ```text
  Profiling escape-heavy streams showed the dominant remaining cost
  was Parser.next: every byte routed through it copies a [3]?Action
  return value that is ~240 bytes (the action union is sized by
  osc.Command). A typical CSI sequence paid this twice: once for the
  first byte after "ESC [" (csi_entry has no fast path, so even the
  first parameter digit went through the table machine) and once for
  the final byte that dispatches the sequence.
  
  This extends the existing stream fast paths to cover both. The
  csi_param fast path now handles final bytes (0x40-0x7E) by
  finalizing parameters and dispatching the CSI directly via a new
  csiDispatchFinal, which replicates the parser's csi_dispatch action
  (MAX_PARAMS overflow drop, trailing parameter finalization, and the
  colon-separator validation for non-'m' finals) without constructing
  the action array. A new csi_entry fast path handles the byte right
  after "ESC [": first parameter digit, empty first parameter,
  private markers (0x3C-0x3F), and parameterless finals. Everything
  else (C0 controls, intermediates, the csi_entry colon edge case)
  still defers to the state machine.
  
  Because these paths dispatch without going through Parser.next,
  they would bypass a handler's vtRaw hook, so they are disabled at
  comptime for handlers that declare one (the inspector). Those
  handlers keep the exact previous behavior.
  
  Throughput measured with ghostty-bench terminal-stream (full
  terminal handler, 100 MB deterministic corpora, 120x80, M4 Max,
  ReleaseFast, hyperfine means of 10 runs). The csi corpus is a
  realistic mix of SGR, cursor movement, erases, and mode changes
  with short text runs; sgr is a doom-fire-like stream of truecolor
  SGRs and cell pairs:
  
  | stream | before | after  | change |
  |--------|--------|--------|--------|
  | csi    | 618 ms | 525 ms | +18%   |
  | sgr    | 486 ms | 414 ms | +17%   |
  ```
- [`253e4f9`](https://github.com/ghostty-org/ghostty/commit/253e4f9c3c439f241e93336940fe4bd200d4a7e2) terminal: bulk-parse CSI parameter bytes at the slice level ([@mitchellh](https://github.com/mitchellh))
  ```text
  After the CSI dispatch fast paths, profiling showed the remaining
  escape-sequence cost was the per-byte plumbing itself: for every
  parameter byte of a sequence like "ESC [ 38;2;10;20;30 m" the
  stream re-entered nextNonUtf8, re-checked the parser state, and
  re-dispatched through the fast-path switch, paying call and state
  check overhead per digit.
  
  consumeUntilGround now hands whole input slices to a new
  consumeCsiParams loop whenever the parser is in the csi_param
  state. It consumes runs of digits and separators with the parser
  accumulator state held in locals, dispatches directly when it
  reaches the final byte, and returns to the general path on the
  first byte it doesn't understand (C0 controls, intermediates,
  etc.), guaranteeing byte-for-byte identical semantics with the
  per-byte fast path it hoists. Like the dispatch fast paths, this is
  disabled at comptime for handlers that declare vtRaw so the
  inspector continues to observe every action.
  
  Throughput measured with ghostty-bench terminal-stream (full
  terminal handler, 100 MB deterministic corpora, 120x80, M4 Max,
  ReleaseFast, hyperfine means of 10 runs):
  
  | stream | before | after  | change |
  |--------|--------|--------|--------|
  | csi    | 525 ms | 407 ms | +29%   |
  | sgr    | 414 ms | 294 ms | +41%   |
  
  Combined with the previous commit, CSI-heavy streams are 1.5-1.7x
  faster end to end than before this series.
  ```
- [`cee35ca`](https://github.com/ghostty-org/ghostty/commit/cee35cabf69d9cf2501c945fe6ee23811552b024) terminal: skip style map update when SGR leaves style unchanged ([@mitchellh](https://github.com/mitchellh))
  ```text
  Profiling the csi benchmark showed ~20% of time in the style
  ref-counted set (hash, probe, release/use churn) driven by
  manualStyleUpdate, which runs after every SGR attribute even when
  the attribute didn't actually change the cursor style. Real
  programs re-assert the same style constantly (per span, per line,
  or on every refresh of a mostly static screen), so a large share of
  these updates are no-ops.
  
  Screen.setAttribute already snapshots the old style to restore it
  on failure, so this compares the style after applying the attribute
  and returns early when it's unchanged: the current style ID is
  already correct and no release/lookup/use is needed.
  
  The tradeoff is one extra Style.eql on every style-changing
  attribute. Measured with ghostty-bench terminal-stream (full
  terminal handler, 100 MB deterministic corpora, 120x80, M4 Max,
  ReleaseFast, hyperfine means of 10 runs) across corpora with
  different repeated style rates (the csi/sgr corpora draw random
  colors from a palette so nearly every SGR changes the style, which
  is the worst case for this change; the redraw corpora model TUI
  refreshes that re-assert the current style for 70% / 95% of SGRs):
  
  | stream              | before | after  | change |
  |---------------------|--------|--------|--------|
  | redraw (95% same)   | 277 ms | 260 ms | +7%    |
  | redraw (70% same)   | 302 ms | 291 ms | +4%    |
  | csi (~0% same)      | 407 ms | 414 ms | -2%    |
  | sgr (~0% same)      | 295 ms | 303 ms | -3%    |
  
  Real-world SGR traffic is far closer to the redraw corpora than to
  the adversarial random-color ones, so this trades a small worst
  case regression for a solid win on the common pattern.
  ```
- [`2da015c`](https://github.com/ghostty-org/ghostty/commit/2da015cd6ac06cedc89e09756e895d2c1715205d) terminal: various VT processing optimizations (~1.5x to ~6x throughput increase) ([#13220](https://github.com/ghostty-org/ghostty/issues/13220)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This is a series of five commits that optimizes VT processing throughput
  in various ways. Each commit is isolated, individually benchmarked, and
  carries a detailed commit message so please read each for details about
  each change.
  
  After #13209 made IO fully parser-bound, these gains should translate
  directly into end-to-end IO throughput (until some other stage becomes
  the new bottleneck). Plain ASCII processing went from ~128 MB/s to ~725
  MB/s. `time cat ascii_150MB.txt` went from 1.5s before 13209 to 1.2s on
  main to 566ms on this branch.
  
  ## The changes
  
  1. **batch printed codepoint runs into direct row fills**. Profiling
  showed ~85% of plain-text time inside `Terminal.print`, re-answering the
  same questions (margins, modes, width, charset, style) for every single
  character. A new `print_slice` stream action delivers runs of decoded
  codepoints to `Terminal.printSlice`, which hoists the invariants and
  fills rows with a masked-compare + branch-free store loop, falling back
  to `print()` for anything complex. **Result: 2.2x–5.7x on ascii plus
  unicode text.**
  2. **dispatch CSI finals directly from stream fast paths**. Every byte
  through `Parser.next` copies a ~240 byte `[3]?Action` and a typical CSI
  copied it twice. New `csi_entry/final` fast paths dispatch directly
  without the action array. **Result: +17-18% on CSI streams.**
  3. **bulk-parse CSI parameter bytes at the slice level**. Parameter
  digits/separators are consumed in a tight slice loop with parser state
  in locals instead of re-entering the per-byte path. **Result: +29-41% on
  escape-heavy streams.**
  4. **skip style map update when SGR leaves style unchanged**. Skip the
  release/hash/probe/use churn when an SGR attribute is a no-op. **Result:
  +4-7% on TUI-refresh patterns, -2-3% on adversarial random-color
  streams** (tradeoff detailed in the commit message). This one is more
  questionable, but willing to measure on real workloads.
  
  ## Benchmarks
  
  Measured with `ghostty-bench +terminal-stream` (full terminal handler,
  100 MB deterministic synthetic corpora, 120x80 terminal, M4 Max, macOS
  26, ReleaseFast, hyperfine means of 10 runs, ~15 ms process startup
  included in all numbers). These are parser-stage numbers, not end-to-end
  app numbers.
  
  | stream | before | after | throughput | change |
  
  |----------------------------|--------|--------|------------------|--------|
  | ascii (no newlines) | 784 ms | 138 ms | 128 → 725 MB/s | 5.7x |
  | ascii lines | 833 ms | 198 ms | 120 → 505 MB/s | 4.2x |
  | unicode mixed-script | 779 ms | 320 ms | 128 → 313 MB/s | 2.4x |
  | CJK (all wide) | 424 ms | 126 ms | 236 → 794 MB/s | 3.4x |
  | unicode, mode 2027 on | 807 ms | 367 ms | 124 → 273 MB/s | 2.2x |
  | CJK, mode 2027 on | 495 ms | 198 ms | 202 → 505 MB/s | 2.5x |
  | csi mix (SGR/CUP/EL/modes) | 648 ms | 414 ms | 154 → 242 MB/s | 1.6x |
  | sgr fire (doom-fire-like) | 495 ms | 303 ms | 202 → 330 MB/s | 1.6x |
  | TUI redraw (repeat styles) | 642 ms | 291 ms | 156 → 344 MB/s | 2.2x |
  | osc | 8.26 s | 8.20 s | (untouched path) | ~1.0x |
  
  **End-to-end note:** #13209 measured the parse thread pegged while the
  gather thread used ~33% of a core, so parser gains of this size may make
  gather (or the renderer lock) the new bottleneck for plain text before
  the full 5.7x shows up end to end. I'll take a look at that soon...
  
  ## LLM Notes
  
  These findings were almost all found by Fable 5. I went through each
  change and simplified quite a lot, read every single line, re-ran
  verifications by hand. Fable in particular isn't good at writing elegant
  Zig code, so there's a lot of style stuff. Ultimately though, I
  understand all of this and feel comfortable with the changes.
  ```
- [`2f0e665`](https://github.com/ghostty-org/ghostty/commit/2f0e6659dd5f3fbc61d91a14389ca6bf54369564) termio: pipeline pty reads to overlap parsing with draining ([@mitchellh](https://github.com/mitchellh))
  ```text
  This replaces the single-threaded pty read loop on posix systems with
  a two-stage pipeline: a new `io-gather` thread drains the pty into a
  small ring of large buffers while the existing `io-reader` thread
  parses the previous batch concurrently.
  
  The motivating discovery was actually found by Fable, but the
  resulting code was hand-written and hand-verified (in addition to
  model-verified as an extra check): on macOS the kernel tty output queue
  caps every read on the pty master at about 1 KiB regardless of the
  read buffer size. Instrumenting a pty with a 64 KB buffer while
  streaming a 6.49 MB file produced 6,337 reads where every read was exactly
  1024 bytes.
  
  This immediately made me realize two things about the old loop that we've
  had since like 2023 which called processOutput once per read: all per-call
  overhead (terminal lock, render wakeup, cursor timestamp) was paid per
  kilobyte of bulk output, and the child could never run more than 1 KiB
  ahead of us, so while we parsed the child (e.g. `cat`) sat blocked on a full
  kernel queue instead of producing.
  
  In 2023, I justified this architecture by saying "reads are generally small"
  but I didn't understand then that reads are generally small because the
  kernel makes them small even if there is a lot of data.
  
  To preserve latency for the more typical
  small-reads-that-are-actually-small, sub-1 KB payloads deliver on the first
  EAGAIN with no added latency.
  
  End-to-end throughput was measured by timing `cat file > /dev/ttysN`
  against a fresh app instance (M4 Max, macOS 26, ReleaseFast, medians
  of repeated interleaved A/B runs):
  
  | stream                  | before       | after         | change  |
  |-------------------------|--------------|---------------|---------|
  | ascii.txt (6.5 MB)      | 91-92 MB/s   | 114-123 MB/s  | +25-30% |
  | unicode.txt (8 MB)      | 116-117 MB/s | 180-183 MB/s  | +55%    |
  | DOOM-Fire-Zig           | 530 fps      | 770 fps       | +45%    |
  
  The pipeline now delivers the parse stage's full measured capacity
  (the parse thread is pegged while gather spends ~33% of a core, so
  any IO throughput improvements are now fully parser-bound).
  
  **Linux note:** This needs to be verified on Linux. I think broadly
  architecture is better and should never be worse. But its possible
  some of the magic constants need to be tuned differently. Would love
  more testing there.
  ```
- [`0535770`](https://github.com/ghostty-org/ghostty/commit/0535770e3541ab7b4ab536d57151db65f9f8c33d) termio: pipeline pty reads to overlap parsing with draining (25 - 55% IO throughput increase) ([#13209](https://github.com/ghostty-org/ghostty/issues/13209)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This replaces the single-threaded pty read loop on posix systems with a
  two-stage pipeline: a new `io-gather` thread drains the pty into a small
  ring of large buffers while the existing `io-reader` thread parses the
  previous batch concurrently.
  
  After this, our IO throughput is now within noise (1 to 3%) of our VT
  parsing and processing throughput. This means that any VT performance
  improvements should raise IO throughput. We're completely bound by it
  now.
  
  > [!IMPORTANT]
  >
  > **Against all odds, we've found a massive (25% to 55%) performance
  improvement in Ghostty IO.** This is a subsystem we were happy to get 2%
  improvement gains in recent years. And the change is relatively simple
  and understandable, too.
  
  The motivating discovery was actually found by Fable, but the resulting
  code was hand-written and hand-verified (in addition to model-verified
  as an extra check): on macOS the kernel tty output queue caps every read
  on the pty master at about 1 KiB regardless of the read buffer size.
  Instrumenting a pty with a 64 KB buffer while streaming a 6.49 MB file
  produced 6,337 reads where every read was exactly 1024 bytes.
  
  This immediately made me realize two things about the old loop that
  we've had since like 2023 which called processOutput once per read: all
  per-call overhead (terminal lock, render wakeup, cursor timestamp) was
  paid per kilobyte of bulk output, and the child could never run more
  than 1 KiB ahead of us, so while we parsed the child (e.g. `cat`) sat
  blocked on a full kernel queue instead of producing.
  
  In 2023, I justified this architecture by saying "reads are generally
  small" but I didn't understand then that reads are generally small
  because the kernel makes them small even if there is a lot of data.
  
  To preserve latency for the more typical
  small-reads-that-are-actually-small, sub-1 KB payloads deliver on the
  first EAGAIN with no added latency.
  
  ## Benchmarks
  
  End-to-end throughput was measured by timing `cat file > /dev/ttysN`
  against a fresh app instance (M4 Max, macOS 26, ReleaseFast, medians of
  repeated interleaved A/B runs):
  
  | stream                  | before       | after         | change  |
  |-------------------------|--------------|---------------|---------|
  | ascii.txt (6.5 MB)      | 91-92 MB/s   | 114-123 MB/s  | +25-30% |
  | unicode.txt (8 MB)      | 116-117 MB/s | 180-183 MB/s  | +55%    |
  | DOOM-Fire-Zig           | 530 fps      | 770 fps       | +45%    |
  
  The pipeline now delivers the parse stage's full measured capacity (the
  parse thread is pegged while gather spends ~33% of a core, so any IO
  throughput improvements are now fully parser-bound).
  
  **Linux note:** This needs to be verified on Linux. I think broadly
  architecture is better and should never be worse. But its possible some
  of the magic constants need to be tuned differently. Would love more
  testing there.
  
  ## Some Background on LLM Usage
  
  As noted above, the original promising path was found by Fable 5. I
  decided to throw some money at analyzing our IO throughput, and went
  into it expecting minor improvements at the cost of unmaintainable
  special case optimizations (typical LLM results when given such tasks on
  an already-optimized path).
  
  I spun off a Fable 5 session (API pricing) prior to some holiday weekend
  (American, July 4th) festivities. When I came back late that night, it
  pointed this path out with some pretty questionable code/results.
  
  The frustrating thing is that _I swear I tried this years ago_ and it
  didn't deliver results. Unfortunately, it was long enough ago (probably
  2023) that I can't remember nor do I have any evidence. But, my brain
  had already clocked this possibility and blocked it out as "already
  tried and failed." The code in question that this PR ultimately touched
  has been basically unchanged for 2+ years.
  
  As a second point, this is a **great example of what I love about
  LLMs**. I was not in a performance-hunting mood and I have other tasks I
  need to get to while at the computer, so improving Ghostty performance
  wasn't my current mode and I would not have worked on it anytime soon
  while at the computer. But, I try to keep an agent running all the time,
  and before my family came over for holiday afternoon, I decided today I
  would try budgeting $100 to Fable to focus on Ghostty's IO performance.
  Why not?
  
  I came back, saw some questionable but interesting results, and decided
  it was worth some human hours to validate, understand, and work on this
  myself. It was worth it. 😄
  
  Anyways, the total API cost of this if you're curious: **$88.28**.
  
  Remember, I **hand-wrote the code** so thats basically what it cost me
  to discover this path. Fable did produce its own solution (in about 3x
  the LoC change of this diff with non-idiomatic Zig styles, overly
  defensive guards, and simultaneously poor error handling). So, I guess I
  did pay for a solution. A bad one. Haha. But the problem it found was
  real and good.
  ```

## July 5, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/28755030114), [2](https://github.com/ghostty-org/ghostty/actions/runs/28754050801), [3](https://github.com/ghostty-org/ghostty/actions/runs/28753449265), [4](https://github.com/ghostty-org/ghostty/actions/runs/28752444628), [5](https://github.com/ghostty-org/ghostty/actions/runs/28749549372), [6](https://github.com/ghostty-org/ghostty/actions/runs/28743971848), [7](https://github.com/ghostty-org/ghostty/actions/runs/28725807699)  
Summary: 7 runs • 15 commits • 6 authors

### Changes

- [`acd09c0`](https://github.com/ghostty-org/ghostty/commit/acd09c0a6cdda07a073047087388c49a76d8fd8c) macos: add tests for NSPasteboard.getOpinionatedStringContents ([@claude](https://github.com/claude))
- [`49806fc`](https://github.com/ghostty-org/ghostty/commit/49806fc4cca56b8edaef18c8ccaae6bf26ac424b) macOS: read string contents per pasteboard item in order ([@bo2themax](https://github.com/bo2themax))
  ```text
  Pasteboards mixing file URLs with other items will now be pasted as joined string.
  ```
- [`1056599`](https://github.com/ghostty-org/ghostty/commit/10565995b9453757b72e634191d73abb2a420dc3) macOS: only read file urls for new-terminal services ([@bo2themax](https://github.com/bo2themax))
  ```text
  macOS is already guarding this system, but guarding what we actually need anyway
  ```
- [`8d83849`](https://github.com/ghostty-org/ghostty/commit/8d838491326b6f75768df1fa70dba0072853e8c9) macOS: read string contents per pasteboard item ([#13170](https://github.com/ghostty-org/ghostty/issues/13170)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes: https://github.com/ghostty-org/ghostty/pull/4956, regression
  from: https://github.com/ghostty-org/ghostty/pull/4956
  
  
  ### AI Disclosure
  
  Claude wrote the tests before I changed `getOpinionatedStringContents`
  ```
- [`b213a72`](https://github.com/ghostty-org/ghostty/commit/b213a72c03b427607b43c89ff4223a7baa079fe8) macOS: only read file urls for new-terminal services ([#13169](https://github.com/ghostty-org/ghostty/issues/13169)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  macOS is already guarding this in Services settings, but guarding what
  we actually need anyway
  ```
- [`2970e9a`](https://github.com/ghostty-org/ghostty/commit/2970e9a2a81d992c8c9a90e785cb65926b8172b3) lib-vt: many more color utility APIs ([@mitchellh](https://github.com/mitchellh))
  ```text
  Embedders that render theme editors, palette pickers, or custom
  settings UI need to use the same color semantics as Ghostty.
  
  This moves the shared parsing paths into terminal/color and exposes them
  through libghostty-vt. Config color and palette parsing now delegate to
  the same helpers, so CLI/config behavior and the C ABI stay in lockstep.
  
  From C:
  
      GhosttyColorRgb rgb;
      ghostty_color_parse("ForestGreen", 11, &rgb);
  
      uint8_t index;
      ghostty_color_parse_palette_entry(
          "0x10=#282c34", 12, &index, &rgb);
  
      const GhosttyColorX11Entry* names =
          ghostty_color_x11_names();
  
  The exported color API is:
  
      ghostty_color_parse
      ghostty_color_parse_x11
      ghostty_color_parse_palette_entry
      ghostty_color_palette_default
      ghostty_color_palette_generate
      ghostty_color_luminance
      ghostty_color_perceived_luminance
      ghostty_color_contrast
      ghostty_color_x11_names
      ghostty_color_x11_name_count
  
  The X11 name table is parsed once at comptime into null-terminated
  entries in rgb.txt order. The existing case-insensitive map keeps the
  same behavior for RGB.parse and +list-colors, while bindings can walk a
  static table without allocations.
  ```
- [`63e75e8`](https://github.com/ghostty-org/ghostty/commit/63e75e86c282ca1d07de9588f0c2cfc268b2621b) lib-vt: many more color utility APIs ([#13206](https://github.com/ghostty-org/ghostty/issues/13206)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Embedders that render theme editors, palette pickers, or custom settings
  UI need to use the same color semantics as Ghostty.
  
  This moves the shared parsing paths into terminal/color and exposes them
  through libghostty-vt. Config color and palette parsing now delegate to
  the same helpers, so CLI/config behavior and the C ABI stay in lockstep.
  
  From C:
  
      GhosttyColorRgb rgb;
      ghostty_color_parse("ForestGreen", 11, &rgb);
  
      uint8_t index;
      ghostty_color_parse_palette_entry(
          "0x10=#282c34", 12, &index, &rgb);
  
      const GhosttyColorX11Entry* names =
          ghostty_color_x11_names();
  
  The exported color API is:
  
      ghostty_color_parse
      ghostty_color_parse_x11
      ghostty_color_parse_palette_entry
      ghostty_color_palette_default
      ghostty_color_palette_generate
      ghostty_color_luminance
      ghostty_color_perceived_luminance
      ghostty_color_contrast
      ghostty_color_x11_names
      ghostty_color_x11_name_count
  
  The X11 name table is parsed once at comptime into null-terminated
  entries in rgb.txt order. The existing case-insensitive map keeps the
  same behavior for RGB.parse and +list-colors, while bindings can walk a
  static table without allocations.
  
  This doesn't add any more binary size since all of this was already used
  by terminal internals.
  ```
- [`f00e906`](https://github.com/ghostty-org/ghostty/commit/f00e906949bbe46904ff7a13eeff9e8d4a292d09) lib-vt: add color scheme report encoder ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a shared encoder for CSI ? 997 ; Ps n color scheme reports and use
  it for both CSI ? 996 n replies and unsolicited Termio reports. Export the
  same encoder through the libghostty-vt C API with docs and an example.
  
  This is a really light API, arguably easy for consumers to hardcode,
  but it didn't match the rest of our style in the libghostty API so we
  should expose it.
  
  Example: GHOSTTY_COLOR_SCHEME_DARK encodes to ESC [ ? 997 ; 1 n,
  while GHOSTTY_COLOR_SCHEME_LIGHT encodes to ESC [ ? 997 ; 2 n.
  ```
- [`4a7cabc`](https://github.com/ghostty-org/ghostty/commit/4a7cabc4fe7ccc1eacd40cdb561fdbd3bf66869f) lib-vt: add color scheme report encoder ([#13192](https://github.com/ghostty-org/ghostty/issues/13192)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a shared encoder for CSI ? 997 ; Ps n color scheme reports and use
  it for both CSI ? 996 n replies and unsolicited Termio reports. Export
  the same encoder through the libghostty-vt C API with docs and an
  example.
  
  This is a really light API, arguably easy for consumers to hardcode, but
  it didn't match the rest of our style in the libghostty API so we should
  expose it.
  ```
- [`004c88e`](https://github.com/ghostty-org/ghostty/commit/004c88e41ebf02e07b55a392f984e4545c3d60c7) fix: set max window clamp to current monitor size ([@yak3d](https://github.com/yak3d))
- [`715ef6c`](https://github.com/ghostty-org/ghostty/commit/715ef6c154997160b917f0168a60b636f32f4537) fix: set max window clamp to current monitor size ([#13171](https://github.com/ghostty-org/ghostty/issues/13171)) ([@jcollie](https://github.com/jcollie))
  ```text
  This PR fixes #7984. The issue was that GTK would clamp the window
  itself based on the display it was opened on. We fix this by computing
  the size based on the current display and then implicitly setting the
  window size instead of relying on GTK to do it.
  
  Claude Code w/ Opus 4.7 was used to investigate, fix and explain some of
  the Ghostty architecture to me.
  ```
- [`243f7df`](https://github.com/ghostty-org/ghostty/commit/243f7df7c131f9cc69bed4bc4586f5bf17b9d4fa) Update VOUCHED list ([#13202](https://github.com/ghostty-org/ghostty/issues/13202)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/13191#issuecomment-4887029233)
  from @mitchellh.
  
  Vouch: @tasselx
  ```
- [`131ca6d`](https://github.com/ghostty-org/ghostty/commit/131ca6d9eb80b816488a342dfa3a9f4f7381bd73) Update VOUCHED list ([#13199](https://github.com/ghostty-org/ghostty/issues/13199)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13196#discussioncomment-17538577)
  from @bo2themax.
  
  Vouch: @Nagato-Yuzuru
  ```
- [`02504bc`](https://github.com/ghostty-org/ghostty/commit/02504bcce1012f3341d8a011657e8d62ecb8528a) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`8642142`](https://github.com/ghostty-org/ghostty/commit/8642142a3d62beda7b1a9733c23bf11b80c720eb) Update iTerm2 colorschemes ([#13190](https://github.com/ghostty-org/ghostty/issues/13190)) ([@jcollie](https://github.com/jcollie))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260629-161812-8c97c3c
  ```

## July 4, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/28720244698), [2](https://github.com/ghostty-org/ghostty/actions/runs/28711497350), [3](https://github.com/ghostty-org/ghostty/actions/runs/28699453517), [4](https://github.com/ghostty-org/ghostty/actions/runs/28695359537)  
Summary: 4 runs • 12 commits • 4 authors

### Changes

- [`65e6128`](https://github.com/ghostty-org/ghostty/commit/65e61282a60afe36c6e9fabcd23c514fa683e9e9) lib-vt: add unicode grapheme width API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Embedders that render text outside the terminal grid need to predict
  how many cells text will occupy once it is written to the terminal.
  The existing codepoint width API exposes the table used by print, but
  that is not enough for mode 2027 grapheme clustering: VS15/VS16, ZWJ
  sequences, skin tone modifiers, and other continuation codepoints can
  change the width of the whole cluster.
  
  This exposes a single segment-and-measure API so callers use Ghostty
  segmentation and width folding together:
  
      uint8_t width;
      size_t n = ghostty_unicode_grapheme_width(cps, len, &width);
  
  From the Zig module:
  
      const vt = @import("ghostty-vt");
      const result = vt.unicode.graphemeWidth(u21, cps);
  
  Callers loop until their string is consumed. The API is intentionally
  not streaming: input must contain a complete first cluster or the
  logical string end, so chunked readers should keep buffering when the
  function consumes all available codepoints and more may arrive.
  
  The terminal hot path now shares the width-decision func with the
  API, the helper is inline and preserves the old branch structure. So
  this doesn't change codegen at all.
  ```
- [`98df7ef`](https://github.com/ghostty-org/ghostty/commit/98df7efc831b4d181bd472a4c508425d0fe399b7) lib-vt: add unicode grapheme width API ([#13186](https://github.com/ghostty-org/ghostty/issues/13186)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Embedders that render text outside the terminal grid need to predict how
  many cells text will occupy once it is written to the terminal. The
  existing codepoint width API exposes the table used by print, but that
  is not enough for mode 2027 grapheme clustering: VS15/VS16, ZWJ
  sequences, skin tone modifiers, and other continuation codepoints can
  change the width of the whole cluster.
  
  This exposes a single segment-and-measure API so callers use Ghostty
  segmentation and width folding together:
  
      uint8_t width;
      size_t n = ghostty_unicode_grapheme_width(cps, len, &width);
  
  From the Zig module:
  
      const vt = @import("ghostty-vt");
      const result = vt.unicode.graphemeWidth(u21, cps);
  
  Callers loop until their string is consumed. The API is intentionally
  not streaming: input must contain a complete first cluster or the
  logical string end, so chunked readers should keep buffering when the
  function consumes all available codepoints and more may arrive.
  
  The terminal hot path now shares the width-decision func with the API,
  the helper is inline and preserves the old branch structure. So this
  doesn't change codegen at all.
  ```
- [`61ce641`](https://github.com/ghostty-org/ghostty/commit/61ce641fcaf6900303a80ea6d9354a819033c8f7) Update VOUCHED list ([#13183](https://github.com/ghostty-org/ghostty/issues/13183)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/13182#issuecomment-4882909658)
  from @trag1c.
  
  Vouch: @pearkes
  ```
- [`91c87e2`](https://github.com/ghostty-org/ghostty/commit/91c87e2cf324e113dbf4d6ff37f630210626092c) terminal: parse kitty drag and drop protocol (OSC 72) ([@ajr-khll](https://github.com/ajr-khll))
  ```text
  Adds an OSC 72 parser following the kitty drag and drop protocol
  specification. Parses metadata and payload into a Command.kitty_dnd_protocol
  variant. Reassembly of chunked transfers and any action handling are
  intentionally out of scope here; stream.zig logs the command as
  unimplemented for now.
  
  Includes a walkthrough document covering the design and each touched file.
  ```
- [`dd6c09b`](https://github.com/ghostty-org/ghostty/commit/dd6c09bcf8b3e60d49883c55e042332a0bea4074) terminal: clean up OSC 72 parser comments and add tests ([@ajr-khll](https://github.com/ajr-khll))
  ```text
  Trims over-commented fields and enum variants to match the repo
  baseline (kitty_clipboard_protocol style). Adds 11 tests covering
  metadata/payload parsing, all EventType values, integer keys,
  negative sentinels, case-sensitive key matching, and BEL terminator
  recording. Removes the development walkthrough document.
  ```
- [`a6132c1`](https://github.com/ghostty-org/ghostty/commit/a6132c18bf4245b9ecead8095da8e637d4e2f0b8) terminal: add doc comments to OSC 72 EventType and Option enums ([@ajr-khll](https://github.com/ajr-khll))
- [`c488ccd`](https://github.com/ghostty-org/ghostty/commit/c488ccda667afbad5e6bfc4815d3aa7abbde5fc8) terminal: correct OSC 72 doc comments for m, i, o, y, X, Y keys ([@ajr-khll](https://github.com/ajr-khll))
- [`6887509`](https://github.com/ghostty-org/ghostty/commit/6887509035d379e728f1eafd7df4ead57e27ecce) Kitty dnd parser ([#13029](https://github.com/ghostty-org/ghostty/issues/13029)) ([@jcollie](https://github.com/jcollie))
  ```text
  (#12852)
  I opened a discussion to work on the new kitty dnd protocol and
  implementing it for Ghostty. I was told to work on the parser but not to
  hook up any actions to it yet. So, that's what I did! Largely based the
  format on kitty_clipboard_protocol.zig, and used Claude Opus 4.8 (Claude
  Code) for writing tests and some structural guidance early on. Would
  love to get started on adding actions as well!
  ```
- [`fc5a727`](https://github.com/ghostty-org/ghostty/commit/fc5a7277297f7098d1d53e4ad972d51a8fc4da4c) lib-vt: add unicode codepoint width API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Embedders that render text outside the terminal grid need to predict
  how many cells a codepoint will occupy once it is written to the
  terminal. The immediate motivation is IME preedit overlay rendering:
  measuring preedit text with font APIs (e.g. CoreText advances) can
  disagree with the terminal's unicode table on ambiguous-width CJK and
  emoji, causing the overlay to visibly jump when the composed text
  commits and reflows through the real grid layout.
  
  This exposes the exact width table the terminal print path already
  uses, so overlays are column-accurate by construction. From C:
  
      uint8_t w = ghostty_unicode_codepoint_width(0x4E00); // 2
  
  And from the Zig module:
  
      const vt = @import("ghostty-vt");
      const w = vt.unicode.codepointWidth(0x4E00); // 2
  
  The function is total over its input: 0 for zero-width codepoints
  (controls, combining marks, default-ignorables, surrogates), 2 for
  wide codepoints (East Asian Wide/Fullwidth, regional indicators,
  clamped at 2), and 1 for everything else, including invalid values
  beyond U+10FFFF.
  
  Perf: uses the LUT lookup we use for the main core terminal
  
  Binary size: the width table was already linked into libghostty-vt
  via the print path, so this adds only the exported wrapper.
  ```
- [`3a2e283`](https://github.com/ghostty-org/ghostty/commit/3a2e28329ce4a1fb7d06b9e17402298e9e84aca2) lib-vt: add scroll-to-row viewport scrolling ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds a GHOSTTY_SCROLL_VIEWPORT_ROW tag with a `size_t row` member
  in the value union. The row is an absolute offset from the top of the
  scrollable area, clamped to the active area, in the same row space as
  the scrollbar offset so thumb positions round-trip cleanly:
  
      ghostty_terminal_scroll_viewport(term,
          (GhosttyTerminalScrollViewport){
              .tag = GHOSTTY_SCROLL_VIEWPORT_ROW,
              .value = {.row = 42},
          });
  
  The tag is appended to the existing enum and the union fits within the
  reserved padding, so this is ABI compatible.
  
  This also corrects the docs on GHOSTTY_TERMINAL_DATA_SCROLLBAR: the
  getter is amortized O(1) (total is maintained incrementally, the offset
  is cached), not "expensive". Since there is intentionally no change
  callback, the docs now bless polling per frame or per write batch and
  diffing, which is what Ghostty's own renderer does.
  
  Motivation: Embedders building native scrollbars can already read scroll state via
  GHOSTTY_TERMINAL_DATA_SCROLLBAR, but the write side only exposed
  top/bottom/delta scrolling. Mapping a scrollbar thumb drag to an
  absolute position required reading the current offset and computing a
  delta, which is two calls that must be sequenced atomically by the
  caller.
  
  The core already supports absolute positioning and the macOS
  app uses it for scroller drags via the scroll_to_row keybinding; this
  exposes the same operation through the libghostty C API.
  ```
- [`8ef9193`](https://github.com/ghostty-org/ghostty/commit/8ef91934592e6cbc5d11919739438a8f8d43ea4e) lib-vt: add unicode codepoint width API ([#13178](https://github.com/ghostty-org/ghostty/issues/13178)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Embedders that render text outside the terminal grid need to predict how
  many cells a codepoint will occupy once it is written to the terminal.
  The immediate motivation is IME preedit overlay rendering: measuring
  preedit text with font APIs (e.g. CoreText advances) can disagree with
  the terminal's unicode table on ambiguous-width CJK and emoji, causing
  the overlay to visibly jump when the composed text commits and reflows
  through the real grid layout.
  
  This exposes the exact width table the terminal print path already uses,
  so overlays are column-accurate by construction. From C:
  
      uint8_t w = ghostty_unicode_codepoint_width(0x4E00); // 2
  
  And from the Zig module:
  
      const vt = @import("ghostty-vt");
      const w = vt.unicode.codepointWidth(0x4E00); // 2
  
  The function is total over its input: 0 for zero-width codepoints
  (controls, combining marks, default-ignorables, surrogates), 2 for wide
  codepoints (East Asian Wide/Fullwidth, regional indicators, clamped at
  2), and 1 for everything else, including invalid values beyond U+10FFFF.
  
  Perf: uses the LUT lookup we use for the main core terminal
  
  Binary size: the width table was already linked into libghostty-vt via
  the print path, so this adds only the exported wrapper.
  ```
- [`cca5172`](https://github.com/ghostty-org/ghostty/commit/cca51729a1b6c095621bead1fec5daf3a21e3f50) lib-vt: add scroll-to-row viewport scrolling ([#13179](https://github.com/ghostty-org/ghostty/issues/13179)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds a GHOSTTY_SCROLL_VIEWPORT_ROW tag with a `size_t row` member
  in the value union. The row is an absolute offset from the top of the
  scrollable area, clamped to the active area, in the same row space as
  the scrollbar offset so thumb positions round-trip cleanly:
  
      ghostty_terminal_scroll_viewport(term,
          (GhosttyTerminalScrollViewport){
              .tag = GHOSTTY_SCROLL_VIEWPORT_ROW,
              .value = {.row = 42},
          });
  
  The tag is appended to the existing enum and the union fits within the
  reserved padding, so this is ABI compatible.
  
  This also corrects the docs on GHOSTTY_TERMINAL_DATA_SCROLLBAR: the
  getter is amortized O(1) (total is maintained incrementally, the offset
  is cached), not "expensive". Since there is intentionally no change
  callback, the docs now bless polling per frame or per write batch and
  diffing, which is what Ghostty's own renderer does.
  
  Motivation: Embedders building native scrollbars can already read scroll
  state via GHOSTTY_TERMINAL_DATA_SCROLLBAR, but the write side only
  exposed top/bottom/delta scrolling. Mapping a scrollbar thumb drag to an
  absolute position required reading the current offset and computing a
  delta, which is two calls that must be sequenced atomically by the
  caller.
  
  The core already supports absolute positioning and the macOS app uses it
  for scroller drags via the scroll_to_row keybinding; this exposes the
  same operation through the libghostty C API.
  ```

## July 3, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/28679695704), [2](https://github.com/ghostty-org/ghostty/actions/runs/28677170266), [3](https://github.com/ghostty-org/ghostty/actions/runs/28640624400), [4](https://github.com/ghostty-org/ghostty/actions/runs/28640398405), [5](https://github.com/ghostty-org/ghostty/actions/runs/28636844086)  
Summary: 5 runs • 11 commits • 5 authors

### Changes

- [`8fe5913`](https://github.com/ghostty-org/ghostty/commit/8fe5913f7ee3eb1ea9da1b8fb1803fbe143dc069) kitty/gfx: fix build on targets without 64-bit atomics ([@mitchellh](https://github.com/mitchellh))
  ```text
  The generation counter added in bdc0b6c19 is a process-global
  std.atomic.Value(u64). The Zig compiler rejects 64-bit atomic
  operations on targets whose largest supported atomic size is 32 bits
  (e.g. arm-linux-androideabi), which broke the libghostty-vt Android
  build. This slipped past other CI targets because they're either
  64-bit or compile kitty graphics out entirely (wasm32-freestanding).
  
  The counter backing nextGeneration is now comptime-selected: 64-bit
  targets keep the lock-free atomic counter, while 32-bit targets fall
  back to a mutex-protected u64. This preserves the process-wide
  uniqueness and monotonicity guarantees of generation stamps
  everywhere. The mutex cost is irrelevant since this is a cold path,
  only invoked on content mutations.
  ```
- [`d560c64`](https://github.com/ghostty-org/ghostty/commit/d560c645488d158c3e554e13025c0eaad68d1f43) kitty/gfx: fix build on targets without 64-bit atomics ([#13174](https://github.com/ghostty-org/ghostty/issues/13174)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The generation counter added in bdc0b6c19 is a process-global
  std.atomic.Value(u64). The Zig compiler rejects 64-bit atomic operations
  on targets whose largest supported atomic size is 32 bits (e.g.
  arm-linux-androideabi), which broke the libghostty-vt Android build.
  This slipped past other CI targets because they're either 64-bit or
  compile kitty graphics out entirely (wasm32-freestanding).
  
  The counter backing nextGeneration is now comptime-selected: 64-bit
  targets keep the lock-free atomic counter, while 32-bit targets fall
  back to a mutex-protected u64. This preserves the process-wide
  uniqueness and monotonicity guarantees of generation stamps everywhere.
  The mutex cost is irrelevant since this is a cold path, only invoked on
  content mutations.
  ```
- [`bdc0b6c`](https://github.com/ghostty-org/ghostty/commit/bdc0b6c19c95300e1ab57c36c69e8fb4da1a0c88) kitty/gfx: add generation stamps, delete transmit time ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a generation counter to the kitty graphics image storage. Every
  content mutation (image transmit/replace, placement add, delete)
  assigns the storage a fresh stamp, and every image is stamped when
  it is added or replaced.
  
  This solves two problems:
  
  First, a retransmission of the same image ID with identical dimensions
  was previously undetectable by anything comparing width, height, format,
  and data length; the per-image stamp changes on every add/replace, so caches
  keyed on it always see the change. Second, the dirty flag was the only
  storage-wide signal, and it is also set by scrolling and resizing, which move
  placements without changing contents. The generation is only bumped by content
  mutations, so an unchanged value means the placement set and all
  image data are identical and consumers can skip re-reading them,
  recomputing only placement geometry.
  
  The generation replaces Image.transmit_time entirely: newest-image
  lookup by number, eviction ordering, and the renderer's texture
  staleness checks all key on it now. A monotonic counter strictly
  orders transmissions where Instant-based times could collide within
  clock resolution (the renderer previously assumed equal timestamps
  meant identical images), and this removes a syscall and an error
  path per transmission.
  
  Delete commands now only mark a mutation (dirty flag and
  generation) when they actually remove something. A delete-all runs
  on every screen clear, so previously every ESC [ 2 J dirtied the
  image state even with no images stored. Eviction via setLimit also
  now marks the state dirty, which it previously did not.
  
  Both generations are exposed through libghostty-vt as
  GHOSTTY_KITTY_GRAPHICS_DATA_GENERATION and
  GHOSTTY_KITTY_IMAGE_DATA_GENERATION (uint64_t), and the headers now
  document that stored image data is always post-inflate/post-decode:
  COMPRESSION always reports NONE, FORMAT is never PNG, and DATA_PTR
  is raw pixels ready for GPU upload.
  
      uint64_t gen = 0;
      ghostty_kitty_graphics_get(
          graphics, GHOSTTY_KITTY_GRAPHICS_DATA_GENERATION, &gen);
      if (gen == last_gen) return; // nothing changed, skip re-reads
  ```
- [`4812fcd`](https://github.com/ghostty-org/ghostty/commit/4812fcdc7d1baa2f8d25f885f93f073b32e31a09) kitty/gfx: add generation stamps, delete transmit time ([#13173](https://github.com/ghostty-org/ghostty/issues/13173)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a generation counter to the kitty graphics image storage. Every
  content mutation (image transmit/replace, placement add, delete) assigns
  the storage a fresh stamp, and every image is stamped when it is added
  or replaced.
  
  This solves two problems:
  
  First, a retransmission of the same image ID with identical dimensions
  was previously undetectable by anything comparing width, height, format,
  and data length; the per-image stamp changes on every add/replace, so
  caches keyed on it always see the change. Second, the dirty flag was the
  only storage-wide signal, and it is also set by scrolling and resizing,
  which move placements without changing contents. The generation is only
  bumped by content mutations, so an unchanged value means the placement
  set and all image data are identical and consumers can skip re-reading
  them, recomputing only placement geometry.
  
  The generation replaces Image.transmit_time entirely: newest-image
  lookup by number, eviction ordering, and the renderer's texture
  staleness checks all key on it now. A monotonic counter strictly orders
  transmissions where Instant-based times could collide within clock
  resolution (the renderer previously assumed equal timestamps meant
  identical images), and this removes a syscall and an error path per
  transmission.
  
  Delete commands now only mark a mutation (dirty flag and generation)
  when they actually remove something. A delete-all runs on every screen
  clear, so previously every ESC [ 2 J dirtied the image state even with
  no images stored. Eviction via setLimit also now marks the state dirty,
  which it previously did not.
  ```
- [`3b63c6d`](https://github.com/ghostty-org/ghostty/commit/3b63c6dc651396c3b74e6a5bc510306df13cdb4c) Manually vouch `eunos-1128` & denounce `VectorPeak` ([@pluiedev](https://github.com/pluiedev))
  ```text
  See #13163
  
  The `!denounce` command should ideally not ban the OP when a manual
  target has been specified...
  ```
- [`bb7cd85`](https://github.com/ghostty-org/ghostty/commit/bb7cd85b2eeb5c298c0808401c80f714dfc98ff3) Manually vouch `eunos-1128` & denounce `VectorPeak` ([#13166](https://github.com/ghostty-org/ghostty/issues/13166)) ([@pluiedev](https://github.com/pluiedev))
  ```text
  See #13163
  
  The `!denounce` command should ideally not ban the OP when a manual
  target has been specified...
  ```
- [`9314b2c`](https://github.com/ghostty-org/ghostty/commit/9314b2c559ab6272b906584a4aabde354b7e9e05) Update VOUCHED list ([#13165](https://github.com/ghostty-org/ghostty/issues/13165)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13163#discussioncomment-17519109)
  from @pluiedev.
  
  Denounce: @eunos-1128
  ```
- [`5a69903`](https://github.com/ghostty-org/ghostty/commit/5a699032ffa6fc1a314abd9993b3e5d7e2f102f5) build(deps): bump docker/build-push-action from 7.2.0 to 7.3.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [docker/build-push-action](https://github.com/docker/build-push-action) from 7.2.0 to 7.3.0.
  - [Release notes](https://github.com/docker/build-push-action/releases)
  - [Commits](https://github.com/docker/build-push-action/compare/f9f3042f7e2789586610d6e8b85c8f03e5195baf...53b7df96c91f9c12dcc8a07bcb9ccacbed38856a)
  
  ---
  updated-dependencies:
  - dependency-name: docker/build-push-action
    dependency-version: 7.3.0
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`7873341`](https://github.com/ghostty-org/ghostty/commit/78733419a13a2b16317b2f82d7e58c1844d6aa24) build(deps): bump dorny/paths-filter from 4.0.1 to 4.0.2 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [dorny/paths-filter](https://github.com/dorny/paths-filter) from 4.0.1 to 4.0.2.
  - [Release notes](https://github.com/dorny/paths-filter/releases)
  - [Changelog](https://github.com/dorny/paths-filter/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/dorny/paths-filter/compare/fbd0ab8f3e69293af611ebaee6363fc25e6d187d...7b450fff21473bca461d4b92ce414b9d0420d706)
  
  ---
  updated-dependencies:
  - dependency-name: dorny/paths-filter
    dependency-version: 4.0.2
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`8a4d63c`](https://github.com/ghostty-org/ghostty/commit/8a4d63c4ce66373eb694b13349b4367c3fbe31cb) build(deps): bump dorny/paths-filter from 4.0.1 to 4.0.2 ([#13159](https://github.com/ghostty-org/ghostty/issues/13159)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps [dorny/paths-filter](https://github.com/dorny/paths-filter) from
  4.0.1 to 4.0.2.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/dorny/paths-filter/releases">dorny/paths-filter's
  releases</a>.</em></p>
  <blockquote>
  <h2>v4.0.2</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>fix warning message by <a
  href="https://github.com/cgundy"><code>@​cgundy</code></a> in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/282">dorny/paths-filter#282</a></li>
  <li>chore: fix GitHub spelling in logs by <a
  href="https://github.com/squat"><code>@​squat</code></a> in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/278">dorny/paths-filter#278</a></li>
  <li>fix: use rev-parse instead of branch --show-current for older git
  compat by <a
  href="https://github.com/saschabratton"><code>@​saschabratton</code></a>
  in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/303">dorny/paths-filter#303</a></li>
  <li>fix: work around git dubious ownership errors in container jobs by
  <a
  href="https://github.com/saschabratton"><code>@​saschabratton</code></a>
  in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/317">dorny/paths-filter#317</a></li>
  <li>docs: update changelog for v4.0.2 by <a
  href="https://github.com/saschabratton"><code>@​saschabratton</code></a>
  in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/318">dorny/paths-filter#318</a></li>
  </ul>
  <h2>New Contributors</h2>
  <ul>
  <li><a href="https://github.com/cgundy"><code>@​cgundy</code></a> made
  their first contribution in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/282">dorny/paths-filter#282</a></li>
  <li><a href="https://github.com/squat"><code>@​squat</code></a> made
  their first contribution in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/278">dorny/paths-filter#278</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/dorny/paths-filter/compare/v4.0.1...v4.0.2">https://github.com/dorny/paths-filter/compare/v4.0.1...v4.0.2</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/dorny/paths-filter/blob/master/CHANGELOG.md">dorny/paths-filter's
  changelog</a>.</em></p>
  <blockquote>
  <h1>Changelog</h1>
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
  <ul>
  <li><a href="https://redirect.github.com/dorny/paths-filter/pull/91">Fix
  getLocalRef() returns wrong ref</a></li>
  </ul>
  <h2>v2.10.1</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/85">Improve
  robustness of change detection</a></li>
  </ul>
  <h2>v2.10.0</h2>
  <ul>
  <li><a href="https://redirect.github.com/dorny/paths-filter/pull/82">Add
  ref input parameter</a></li>
  <li><a href="https://redirect.github.com/dorny/paths-filter/pull/83">Fix
  change detection in PR when pullRequest.changed_files is
  incorrect</a></li>
  </ul>
  <h2>v2.9.3</h2>
  <ul>
  <li><a href="https://redirect.github.com/dorny/paths-filter/pull/78">Fix
  change detection when base is a tag</a></li>
  </ul>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/7b450fff21473bca461d4b92ce414b9d0420d706"><code>7b450ff</code></a>
  docs: update changelog for v4.0.2 (<a
  href="https://redirect.github.com/dorny/paths-filter/issues/318">#318</a>)</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/928037783a71f24983ea250c6e55290c1b2de54f"><code>9280377</code></a>
  fix: work around git dubious ownership errors in container jobs (<a
  href="https://redirect.github.com/dorny/paths-filter/issues/317">#317</a>)</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/f3ceefdc7ef57bc2d8560787d4b6c33e44044cec"><code>f3ceefd</code></a>
  fix: use rev-parse instead of branch --show-current for older git compat
  (<a
  href="https://redirect.github.com/dorny/paths-filter/issues/303">#303</a>)</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/61f87a10cd2c304679af17bb73ef192addf33c1c"><code>61f87a1</code></a>
  chore: fix GitHub spelling in logs (<a
  href="https://redirect.github.com/dorny/paths-filter/issues/278">#278</a>)</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/b82ff81ffbe6fb4b636bb5b47e37fd8d12b32632"><code>b82ff81</code></a>
  fix warning message (<a
  href="https://redirect.github.com/dorny/paths-filter/issues/282">#282</a>)</li>
  <li>See full diff in <a
  href="https://github.com/dorny/paths-filter/compare/fbd0ab8f3e69293af611ebaee6363fc25e6d187d...7b450fff21473bca461d4b92ce414b9d0420d706">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=dorny/paths-filter&package-manager=github_actions&previous-version=4.0.1&new-version=4.0.2)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`8252871`](https://github.com/ghostty-org/ghostty/commit/8252871b2b5550ef9649c823530a688ea5175bc9) build(deps): bump docker/build-push-action from 7.2.0 to 7.3.0 ([#13143](https://github.com/ghostty-org/ghostty/issues/13143)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [docker/build-push-action](https://github.com/docker/build-push-action)
  from 7.2.0 to 7.3.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/docker/build-push-action/releases">docker/build-push-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v7.3.0</h2>
  <ul>
  <li>Preserve names in esbuild bundle by <a
  href="https://github.com/crazy-max"><code>@​crazy-max</code></a> in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1567">docker/build-push-action#1567</a></li>
  <li>Bump <code>@​docker/actions-toolkit</code> from 0.90.0 to 0.92.0 in
  <a
  href="https://redirect.github.com/docker/build-push-action/pull/1545">docker/build-push-action#1545</a>
  <a
  href="https://redirect.github.com/docker/build-push-action/pull/1572">docker/build-push-action#1572</a></li>
  <li>Bump <code>@​sigstore/core</code> from 3.1.0 to 3.2.1 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1568">docker/build-push-action#1568</a></li>
  <li>Bump js-yaml from 4.1.1 to 4.3.0 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1566">docker/build-push-action#1566</a></li>
  <li>Bump tmp from 0.2.5 to 0.2.7 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1547">docker/build-push-action#1547</a></li>
  <li>Bump undici from 6.24.1 to 6.27.0 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1564">docker/build-push-action#1564</a></li>
  <li>Bump vite from 7.3.2 to 7.3.6 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1563">docker/build-push-action#1563</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/docker/build-push-action/compare/v7.2.0...v7.3.0">https://github.com/docker/build-push-action/compare/v7.2.0...v7.3.0</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/docker/build-push-action/commit/53b7df96c91f9c12dcc8a07bcb9ccacbed38856a"><code>53b7df9</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1572">#1572</a>
  from docker/dependabot/npm_and_yarn/docker/actions-t...</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/154298c1ca89be1c0e019084f0611ddca621aafc"><code>154298c</code></a>
  [dependabot skip] chore: update generated content</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/cb1238b9c9eb453d106b4e4142a5bd9cde710040"><code>cb1238b</code></a>
  chore(deps): Bump <code>@​docker/actions-toolkit</code> from 0.91.0 to
  0.92.0</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/24f845d5cbe75d2d350a984fd0e18cb7a3f29c1c"><code>24f845d</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1566">#1566</a>
  from docker/dependabot/npm_and_yarn/js-yaml-4.2.0</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/9c6973007b52c322651c38915d5e8824cea95c50"><code>9c69730</code></a>
  [dependabot skip] chore: update generated content</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/bc3a3a5f72a6dca16c2c2468d1dfc55ee66d2193"><code>bc3a3a5</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1574">#1574</a>
  from docker/dependabot/github_actions/aws-actions/co...</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/a82c504a2387bb8bedc50072f9c554ae2a7dab5d"><code>a82c504</code></a>
  chore(deps): Bump js-yaml from 4.1.1 to 4.3.0</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/0285a75190c039d6dac52b7711abcef3f5d8f6f6"><code>0285a75</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1573">#1573</a>
  from docker/dependabot/github_actions/actions/cache-...</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/c6ad2a3f9644680619de938b97c8a10a87b2a88d"><code>c6ad2a3</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1575">#1575</a>
  from docker/dependabot/github_actions/actions/checko...</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/d37484fb9737c5442a257e2f0ae5a8d756ed7d92"><code>d37484f</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1564">#1564</a>
  from docker/dependabot/npm_and_yarn/undici-6.27.0</li>
  <li>Additional commits viewable in <a
  href="https://github.com/docker/build-push-action/compare/f9f3042f7e2789586610d6e8b85c8f03e5195baf...53b7df96c91f9c12dcc8a07bcb9ccacbed38856a">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=docker/build-push-action&package-manager=github_actions&previous-version=7.2.0&new-version=7.3.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## July 2, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/28622708104), [2](https://github.com/ghostty-org/ghostty/actions/runs/28563110896)  
Summary: 2 runs • 4 commits • 2 authors

### Changes

- [`f245cdc`](https://github.com/ghostty-org/ghostty/commit/f245cdc66721c3cea7551fca715f1ea04cd6bdc2) lib-vt: expose selection gesture to Zig ([@rockorager](https://github.com/rockorager))
  ```text
  Selection gestures are already part of the libghostty-vt C API, but the
  native Zig module did not re-export the underlying terminal type. Zig
  consumers that implement mouse selection had to reach into terminal
  internals instead of using @import("ghostty-vt").
  
  Re-export SelectionGesture from lib_vt alongside the other terminal
  selection and screen types.
  ```
- [`842badc`](https://github.com/ghostty-org/ghostty/commit/842badca5f1fc8e8bca1521bf7c619d26561aaa5) lib-vt: expose selection gesture to Zig ([#13156](https://github.com/ghostty-org/ghostty/issues/13156)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Selection gestures are already part of the libghostty-vt C API, but the
  native Zig module did not re-export the underlying terminal type. Zig
  consumers that implement mouse selection had to reach into terminal
  internals instead of using @import("ghostty-vt").
  
  Re-export SelectionGesture from lib_vt alongside the other terminal
  selection and screen types.
  
  AI Disclosure: I used AI. Yes, for +1
  ```
- [`aea63d7`](https://github.com/ghostty-org/ghostty/commit/aea63d71fe6630ae940b8ecf07d35851c0c11fba) libghostty: fix utf-8 grapheme length overflow ([@mitchellh](https://github.com/mitchellh))
  ```text
  The GRAPHEMES_UTF8 row-cells getter inferred its required byte
  accumulator from utf8CodepointSequenceLength, which stores the
  value in u3. Multi-scalar clusters longer than seven UTF-8 bytes
  could overflow that accumulator before the capacity check, causing
  wrong probe sizes and allowing optimized builds to write past a
  caller-provided buffer.
  
  Use usize for the required byte count so probing and capacity
  checks match the later encode loop. Extend the render C API test
  to cover the short combining cluster, an eight-byte flag cluster,
  a longer family emoji, exact-size success, and the
  cap == needed - 1 no-write boundary.
  ```
- [`c22df09`](https://github.com/ghostty-org/ghostty/commit/c22df09da10b27dd248b21b7be8b26dcbddeb8ef) libghostty: fix utf-8 grapheme length overflow ([#13145](https://github.com/ghostty-org/ghostty/issues/13145)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The GRAPHEMES_UTF8 row-cells getter inferred its required byte
  accumulator from utf8CodepointSequenceLength, which stores the value in
  u3. Multi-scalar clusters longer than seven UTF-8 bytes could overflow
  that accumulator before the capacity check, causing wrong probe sizes
  and allowing optimized builds to write past a caller-provided buffer.
  
  Use usize for the required byte count so probing and capacity checks
  match the later encode loop. Extend the render C API test to cover the
  short combining cluster, an eight-byte flag cluster, a longer family
  emoji, exact-size success, and the cap == needed - 1 no-write boundary.
  ```

## July 1, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/28551941025), [2](https://github.com/ghostty-org/ghostty/actions/runs/28537629892), [3](https://github.com/ghostty-org/ghostty/actions/runs/28485879059)  
Summary: 3 runs • 5 commits • 4 authors

### Changes

- [`df5cee2`](https://github.com/ghostty-org/ghostty/commit/df5cee23829e14074d546c63baca839c47326d6f) Update VOUCHED list ([#13141](https://github.com/ghostty-org/ghostty/issues/13141)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13121#discussioncomment-17502740)
  from @jcollie.
  
  Vouch: @yak3d
  ```
- [`480edb4`](https://github.com/ghostty-org/ghostty/commit/480edb45e323daf21993c32d386a457ee8c23e96) ci: skip tip release when only non-artifact files change ([@claude](https://github.com/claude))
  ```text
  Detect changes since the last tip with dorny/paths-filter (base: tip)
  and skip the build when a push touches only files that never reach the
  built artifact: all of .github (except release-tip.yml, which defines the
  build/tag/publish jobs) plus docs and repo/lint/editor metadata.
  ```
- [`8b71d7a`](https://github.com/ghostty-org/ghostty/commit/8b71d7a03cf345b6430171e480fa6e5135953095) ci: skip tip release when only non-artifact files change ([#13130](https://github.com/ghostty-org/ghostty/issues/13130)) ([@jcollie](https://github.com/jcollie))
  ```text
  Ignore more files when releasing tip. Moved release-tip run to a
  separate script so we can test against it.
  
  ### AI Disclosure
  
  Claude did this, I reviewed the changes and asked it run the tests
  locally before creating the pr.
  ```
- [`c6b0c0d`](https://github.com/ghostty-org/ghostty/commit/c6b0c0dcb45f4fa8dfb1d74604568ced30f8c48d) build(deps): bump namespacelabs/nscloud-cache-action from 1.5.0 to 1.6.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [namespacelabs/nscloud-cache-action](https://github.com/namespacelabs/nscloud-cache-action) from 1.5.0 to 1.6.0.
  - [Release notes](https://github.com/namespacelabs/nscloud-cache-action/releases)
  - [Commits](https://github.com/namespacelabs/nscloud-cache-action/compare/d6b68aa38adace8976c09629021052d57bb1ce9c...58bf6e08898e88803c098e2b522668541cd3b2e3)
  
  ---
  updated-dependencies:
  - dependency-name: namespacelabs/nscloud-cache-action
    dependency-version: 1.6.0
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`e1d31de`](https://github.com/ghostty-org/ghostty/commit/e1d31deaaed21aa9225afca78d778fb373c95852) build(deps): bump namespacelabs/nscloud-cache-action from 1.5.0 to 1.6.0 ([#13126](https://github.com/ghostty-org/ghostty/issues/13126)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [namespacelabs/nscloud-cache-action](https://github.com/namespacelabs/nscloud-cache-action)
  from 1.5.0 to 1.6.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/namespacelabs/nscloud-cache-action/releases">namespacelabs/nscloud-cache-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v1.6.0</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>Remove unused Unix-only helpers from utils by <a
  href="https://github.com/rcrowe"><code>@​rcrowe</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/148">namespacelabs/nscloud-cache-action#148</a></li>
  <li>Validate cache links on Windows runners by <a
  href="https://github.com/rcrowe"><code>@​rcrowe</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/149">namespacelabs/nscloud-cache-action#149</a></li>
  <li>Early Windows support -&gt; Bump actions-toolkit to v0.4.0, fix
  Dependabot &amp; patch security advisories by <a
  href="https://github.com/rcrowe"><code>@​rcrowe</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/150">namespacelabs/nscloud-cache-action#150</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/namespacelabs/nscloud-cache-action/compare/v1...v1.6.0">https://github.com/namespacelabs/nscloud-cache-action/compare/v1...v1.6.0</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/58bf6e08898e88803c098e2b522668541cd3b2e3"><code>58bf6e0</code></a>
  Bump actions-toolkit to v0.4.0; fix Dependabot and patch security
  advisories ...</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/07c62f87b6a9734917f8944b3afce3181492e327"><code>07c62f8</code></a>
  Validate cache links on Windows runners (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/149">#149</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/148be15ff18531cb436517206569f053ce7bf8d1"><code>148be15</code></a>
  Remove unused Unix-only helpers from utils (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/148">#148</a>)</li>
  <li>See full diff in <a
  href="https://github.com/namespacelabs/nscloud-cache-action/compare/d6b68aa38adace8976c09629021052d57bb1ce9c...58bf6e08898e88803c098e2b522668541cd3b2e3">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=namespacelabs/nscloud-cache-action&package-manager=github_actions&previous-version=1.5.0&new-version=1.6.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

