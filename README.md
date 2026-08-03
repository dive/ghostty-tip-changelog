> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: August 3, 2026 at 19:24 UTC.

## August 3, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/30840279326), [2](https://github.com/ghostty-org/ghostty/actions/runs/30834015563), [3](https://github.com/ghostty-org/ghostty/actions/runs/30829026722), [4](https://github.com/ghostty-org/ghostty/actions/runs/30823354937), [5](https://github.com/ghostty-org/ghostty/actions/runs/30782256667)  
Summary: 5 runs • 21 commits • 5 authors

### Changes

- [`c11fe54`](https://github.com/ghostty-org/ghostty/commit/c11fe5486f7c1f0aa346b8f0a23ea0fcedf79433) core: avoid copying OSC 52 clipboard responses ([@jparise](https://github.com/jparise))
  ```text
  OSC 52 clipboard reads built their response in an allocated buffer and
  then passed it through Message.writeReq, which allocated a second copy
  for large responses.
  
  Instead, transfer the allocated response directly using .write_alloc.
  
  Small responses now retain their initial allocation until the IO thread
  consumes them instead of being copied inline and freed immediately.
  Their allocation count is unchanged, while large responses improve from
  two allocations to one. Both cases avoid the additional copy.
  ```
- [`ac04fc2`](https://github.com/ghostty-org/ghostty/commit/ac04fc276169c70d31aa6fcfc5b43fc160d6fe6e) core: avoid copying OSC 52 clipboard responses ([#13577](https://github.com/ghostty-org/ghostty/issues/13577)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  OSC 52 clipboard reads built their response in an allocated buffer and
  then passed it through Message.writeReq, which allocated a second copy
  for large responses.
  
  Instead, transfer the allocated response directly using .write_alloc.
  
  Small responses now retain their initial allocation until the IO thread
  consumes them instead of being copied inline and freed immediately.
  Their allocation count is unchanged, while large responses improve from
  two allocations to one. Both cases avoid the additional copy.
  ```
- [`90da3ab`](https://github.com/ghostty-org/ghostty/commit/90da3aba58a8c5f44d97bd9ec54eaa1696591256) gtk: fix split sizing to eliminate flickering ([@dkinzler](https://github.com/dkinzler))
  ```text
  For widget resizes the split ratio is now synced directly from the
  propMaxPosition callback in the SplitTreeSplit widget, instead of an
  idle callback. With this change all surfaces will be sized correctly
  from the start, in a single round of size allocation in GTK. Previously,
  surfaces would initially be shown with the wrong size for a few frames
  until the idle callback ran, resulting in visible flickering. This was
  especially visible when resizing a split quickly by holding down the
  resize keybind.
  
  Moved logic to sync split ratio between gtk.Paned widget and split tree
  into new syncSplitRatio function in the SplitTreeSplit widget. Added
  debug assertions and log warnings to syncSplitRatio where we look up
  the split tree.
  ```
- [`957ed21`](https://github.com/ghostty-org/ghostty/commit/957ed21d5c6241f81526581db78520d3c3196421) core: free allocated writes in read-only mode ([@jparise](https://github.com/jparise))
  ```text
  Read-only filtering happens in Surface.queueIo after callers construct
  the message. This early return leaked write_alloc payloads because the
  IO thread never receives them and therefore does not perform its normal
  cleanup.
  ```
- [`7d74809`](https://github.com/ghostty-org/ghostty/commit/7d748097a069768e12fa9bf63d598215a3e8f7a3) core: free allocated writes in read-only mode ([#13574](https://github.com/ghostty-org/ghostty/issues/13574)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Read-only filtering happens in Surface.queueIo after callers construct
  the message. This early return leaked write_alloc payloads because the
  IO thread never receives them and therefore does not perform its normal
  cleanup.
  ```
- [`da581e0`](https://github.com/ghostty-org/ghostty/commit/da581e0fb7a49af38b59a91ef59e1677ff06435a) gtk: improve split sizing ([#13414](https://github.com/ghostty-org/ghostty/issues/13414)) ([@jcollie](https://github.com/jcollie))
  ```text
  This PR improves the way splits/surfaces are sized in the GTK app, which
  eliminates flickering and slightly improves performance.
  
  Fixes #13328, #12709, #11187.
  Related #8208 (closed) but some later comments mention flickering issues
  persisting.
  Builds on top of the changes in #12698.
  
  Previously an idle callback was used to sync the split ratio between the
  GTK widget tree and the split tree data structure that represents the
  split layout. The widget tree contains a `SplitTreeSplit` widget, which
  wraps a `GtkPaned` widget, for every split. During size allocation a
  `GtkPaned` widget first computes the initial position of the divider and
  thereby the size for its two children. We get notified of that position
  (and the max possible position) via the `propPosition/propMaxPosition`
  callbacks in `SplitTreeSplit` and set up an idle callback (the `onIdle`
  function) to update the position if it does not match the desired split
  ratio. Since the initial position is often not correct, especially in
  nested layouts or if the ratio is not 0.5, a surface will first be shown
  with the wrong size for a few frames until the idle callback runs and
  corrects the sizing. In nested layouts it might take multiple rounds of
  size allocation and idle callbacks until every surface gets the correct
  size. This causes flickering as widgets eventually snap to another size,
  which is especially noticeable if the layout changes quickly e.g. when
  resizing a split using keybinds.
  
  To fix this, the divider position will now be corrected directly from
  the `propMaxPosition` callback, which runs during GTK size allocation,
  right after a `GtkPaned` computes the initial position and right before
  it uses the position to allocate sizes for its two children. With this
  change every surface will be sized correctly during the first round of
  size allocation.
  The idle callback is still used to update the ratio in the split tree
  when a split is resized by manually dragging the divider in the UI. The
  logic to sync the split ratio was moved to the new `syncSplitRatio`
  function which is called from both `propMaxPosition` and `onIdle`.
  
  This is kind of hacky, but I reviewed the GTK source code in detail to
  verify that this is safe (see the various code comments for more
  details). I also tested extensively on both Hyprland and KDE Plasma:
  creating deeply nested layouts, resizing with both keybinds and dragging
  dividers by hand, with multiple tabs, resizing the entire window,
  resizing entire subtrees to 0 and back. Everything seems to work fine.
  
  For performance testing I used sysprof which can also collect GTK stats.
  When creating/deleting/resizing splits I can measure a slight but
  consistent increase in GTK FPS (+5 to 10) on my system. Other than that
  CPU usage and FPS seem to be the same before and after. I guess this
  makes sense, while we added a bit of work to the GTK loop during size
  allocation, we avoid surfaces being resized.
  
  For the flickering, here's a side-by-side comparison. Left is before the
  changes, right is after.
  
  
  https://github.com/user-attachments/assets/2a4f0b4b-e113-49b5-b0d7-d9e507a5a4ff
  
  AI Disclosure: no AI was used.
  ```
- [`15c50c1`](https://github.com/ghostty-org/ghostty/commit/15c50c1db1983961c9aa37a2fc0f51327ad26608) crash: do not use global state ([@vancluever](https://github.com/vancluever))
  ```text
  This removes use of global state from the crash reporting functionality
  (everything in src/crash).
  
  This particularly ensures that there are no races on the system
  environment during the execution of the initialization thread that would
  possibly cause crashes, particularly in any (albeit unsupported) 3rd
  party integrations of libghostty-internal.
  
  Ultimately, this pushes any coupling of I/O and environment to places
  that would more correctly interface with global state, such as the
  same-thread global.init, and the crash report CLI.
  
  Note that similar de-coupling actions have been taken on XDG and home
  directory functionality, pushing their coupling points up the stack in a
  similar way.
  ```
- [`b5290e7`](https://github.com/ghostty-org/ghostty/commit/b5290e74c42c2fc5f891eb20f08d0ac0c7c634f8) terminal/snapshot: release decoded hyperlink table refs ([@mitchellh](https://github.com/mitchellh))
  ```text
  Decoded hyperlink table entries retained their insertion reference after
  the grid added its per-cell references. Overwriting all linked cells could
  therefore leave unused entries alive indefinitely.
  
  Release each accepted wire table entry after grid decoding, including
  duplicate values that map to one native ID. Regression coverage verifies
  exact cell ownership and reaping after overwrite.
  ```
- [`f99896b`](https://github.com/ghostty-org/ghostty/commit/f99896bf8c2438e2edbc2a5779a1f2fafa9bcc6d) terminal/snapshot: preserve style reader errors ([@mitchellh](https://github.com/mitchellh))
  ```text
  Lenient style decoding previously caught every error, so PAGE and SCREEN
  could treat truncation or an I/O failure as an invalid semantic style and
  continue from a corrupted stream position.
  
  Add a nullable decoder that discards only invalid style contents while
  propagating reader failures. Update snapshot callers and cover both semantic
  fallback and structural failure behavior.
  ```
- [`cafe7d5`](https://github.com/ghostty-org/ghostty/commit/cafe7d5da43fb19020117e1ab5cca06751f8d0c7) terminal/snapshot: clamp decoded saved cursors ([@mitchellh](https://github.com/mitchellh))
  ```text
  SCREEN decoding restored saved cursor coordinates directly from the wire
  even when they exceeded the current terminal dimensions, unlike the live
  cursor restoration path.
  ```
- [`7d9aaa2`](https://github.com/ghostty-org/ghostty/commit/7d9aaa29703750c4f129790314a54c9a6cd5c7c5) terminal/snapshot: clarify incremental history errors ([@mitchellh](https://github.com/mitchellh))
  ```text
  Document why incremental history decoding exposes native page finalization
  errors and intentionally bypasses the one-shot ExistingHistory guard after READY.
  ```
- [`5c65304`](https://github.com/ghostty-org/ghostty/commit/5c65304a27402f64a7d7356a92b08973e99bc911) crash: do not use global state ([#13567](https://github.com/ghostty-org/ghostty/issues/13567)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This removes use of global state from the crash reporting functionality
  (everything in `src/crash`).
  
  This particularly ensures that there are no races on the system
  environment during the execution of the initialization thread that would
  possibly cause crashes, particularly in any (albeit unsupported) 3rd
  party integrations of libghostty-internal.
  
  Ultimately, this pushes any coupling of I/O and environment to places
  that would more correctly interface with global state, such as the
  same-thread `global.init`, and the crash report CLI.
  
  Note that similar de-coupling actions have been taken on XDG and home
  directory functionality, pushing their coupling points up the stack in a
  similar way.
  ```
- [`863fc95`](https://github.com/ghostty-org/ghostty/commit/863fc9531ae0b8e09b7103a9089dfc00319a7d9c) terminal/snapshot: more misc bugs ([#13573](https://github.com/ghostty-org/ghostty/issues/13573)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Again nothing critical, just some polish around the edges.
  ```
- [`d148471`](https://github.com/ghostty-org/ghostty/commit/d14847183844e84fb8282ebe5a6c9061f40530e3) terminal/snapshot: preserve mixed-width pending wrap ([@mitchellh](https://github.com/mitchellh))
  ```text
  SCREEN decode clamped the cursor x coordinate to the physical page
  width, but validated pending wrap against the terminal-wide column
  count. A lazily reflowed page narrower than the current terminal could
  therefore lose a valid pending-wrap state at its last physical column.
  The next write would continue on the same row instead of wrapping.
  
  Validate pending wrap against the cursor page width, matching the clamp
  and the page-local cursor pin. Add a mixed-width decode regression that
  places the cursor at the narrow page boundary.
  ```
- [`cbc9f36`](https://github.com/ghostty-org/ghostty/commit/cbc9f360b1d6be9305f25cd6e68c49884fa24187) terminal/snapshot: report invalid decoder states ([@mitchellh](https://github.com/mitchellh))
  ```text
  Decoder.next treated calls before READY and calls after any prior decode
  error as unreachable. Network or mux glue that retried after a truncated
  history record, or invoked next before setup completed, could therefore
  turn a recoverable protocol misuse into a process panic.
  
  Add DecoderNotReady and DecoderFailed to NextError and return them for
  the start and failed states. Keep finished calls idempotent, and cover
  both an early call and a retry after FINISH truncation.
  ```
- [`e89ff37`](https://github.com/ghostty-org/ghostty/commit/e89ff37aa8a551369a8f5ae9022cc43410b6d59e) terminal/snapshot: encode screen pages safely ([@mitchellh](https://github.com/mitchellh))
  ```text
  SCREEN encoding assumed every page from the active boundary onward was
  resident. A debug assertion guarded that PageList policy invariant, but
  release builds immediately used pageAssumeResident. If compression policy
  ever allowed a SCREEN suffix page to remain compressed, the encoder would
  read an inactive union field, causing undefined behavior and potentially
  a crash or corrupt snapshot.
  
  Use pagePreservingState for every SCREEN suffix page, as HISTORY already
  does, and include allocation failure in EncodeError. Resident pages remain
  a zero-allocation borrow while compressed pages decode into temporary
  read-only storage without changing the source representation. Exercise the
  path with an explicitly compressed active suffix page.
  ```
- [`9a5279d`](https://github.com/ghostty-org/ghostty/commit/9a5279db682832274442ba2471d277b2ca9b4fa4) terminal/snapshot: release decoded style table refs ([@mitchellh](https://github.com/mitchellh))
  ```text
  PAGE decoding inserted every valid style table entry into the native
  ref-counted set before decoding cells. That insertion contributed one
  reference in addition to every cell reference, unlike organically built
  pages where the initial add belongs to the first cell. An unused encoded
  style therefore remained live with refcount one and was emitted again on
  every re-encode; used styles were also permanently over-counted.
  
  After the grid has installed all cell references, release the temporary
  table-owned reference once per distinct live style. Unused styles become
  dead immediately and used styles retain exactly their cell count. Cover
  used reference counts, unordered sparse IDs, and canonical first
  re-encoding of an unused entry.
  ```
- [`418b5d1`](https://github.com/ghostty-org/ghostty/commit/418b5d18054a015f25efc30592a412a0ac5c6c68) terminal/snapshot: harden grapheme suffix decode ([@mitchellh](https://github.com/mitchellh))
  ```text
  Grapheme suffix decoding accepted U+0000 even though zero is the native
  empty-cell sentinel. It also appended codepoints one at a time and, when
  page capacity failed after a prefix had been stored, left that truncated
  prefix attached to the cell. Hostile snapshots could therefore introduce
  invalid cluster data or render a partial cluster depending on allocator
  capacity.
  
  Ignore NUL alongside invalid scalar values. If any append runs out of
  native capacity, remove the prefix already attached and consume the rest
  of the declared suffix without applying it, making delivery atomic at the
  cluster level. Cover NUL input and a failure after 128 accepted suffix
  codepoints.
  ```
- [`0b940ed`](https://github.com/ghostty-org/ghostty/commit/0b940ed58925cdf5b27e9c10855694f0f83c0d57) terminal/snapshot: misc bugs ([#13572](https://github.com/ghostty-org/ghostty/issues/13572)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Misc bugs related to snapshotting. Nothing critical. Each backed by a
  failed test w/o the change that passes with it.
  ```
- [`e37865b`](https://github.com/ghostty-org/ghostty/commit/e37865bedc2e1b4884f728f41f0d4a179418387f) terminal/snapshot: add incremental decoder ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds a new `terminal.snapshot.Decoder` that allows for incremental
  decoding of a snapshot stream. There are two methods: `ready` builds up
  the entire terminal up to READY. Then `next` acts like a Zig iterator
  and applies incremental history as it becomes available. In between
  calls to `ready` and `next` the caller can do whatever.
  ```
- [`b4592ee`](https://github.com/ghostty-org/ghostty/commit/b4592eefd27290457852ad7d4f16799ecc00b983) terminal/snapshot: add incremental decoder ([#13569](https://github.com/ghostty-org/ghostty/issues/13569)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds a new `terminal.snapshot.Decoder` that allows for incremental
  decoding of a snapshot stream. There are two methods: `ready` builds up
  the entire terminal up to READY. Then `next` acts like a Zig iterator
  and applies incremental history as it becomes available. In between
  calls to `ready` and `next` the caller can do whatever.
  
  The use case for this: with a 1MB ascii stream, the time to decode to
  READY is ~40us on my machine, versus 1.5ms for the entire history. This
  means that a terminal could be rendered and visible after 40us rather
  than waiting for the full terminal. This isn't a large terminal, but
  that READY time should be pretty standard since screens don't get that
  big, but history is unbounded.
  ```

## August 2, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/30770277131), [2](https://github.com/ghostty-org/ghostty/actions/runs/30769052845), [3](https://github.com/ghostty-org/ghostty/actions/runs/30765748163), [4](https://github.com/ghostty-org/ghostty/actions/runs/30752310032), [5](https://github.com/ghostty-org/ghostty/actions/runs/30743972710)  
Summary: 5 runs • 25 commits • 7 authors

### Changes

- [`7031c89`](https://github.com/ghostty-org/ghostty/commit/7031c892b2d1309d4463a56654b90bd0501f3970) synthetic: line length options for the ascii generator ([@mitchellh](https://github.com/mitchellh))
  ```text
  The ascii generator emits an unbroken stream of printable bytes, which
  exercises terminal wrapping but produces only full-width rows. Add
  line-min and line-max options that emit CR LF-terminated lines with a
  uniformly distributed printable length so generated corpora can also
  model shell-like output where most rows end well before the last
  column. The default behavior is unchanged.
  ```
- [`0b5e124`](https://github.com/ghostty-org/ghostty/commit/0b5e12453b639af3f904ad57123cb075a97a82f8) benchmark: add terminal-snapshot benchmark ([@mitchellh](https://github.com/mitchellh))
  ```text
  Measures the terminal binary snapshot codecs in both directions
  against the same terminal state. Setup feeds a pre-generated VT
  stream (for example from ghostty-gen ascii) to a terminal outside
  the timed region.
  
  Baseline measurements at this commit (M-series, ReleaseFast, 80x24,
  unlimited scrollback, 1 MB corpora, per-loop time with setup
  subtracted):
  
    ascii lines 1-70:  34.16 MB  encode  92.8 ms  decode 119.8 ms
    ascii full-wrap:   16.01 MB  encode  43.6 ms  decode  56.2 ms
    utf8:               4.33 MB  encode  12.4 ms  decode  19.0 ms
  ```
- [`ed0f54f`](https://github.com/ghostty-org/ghostty/commit/ed0f54fb8ccf45fc502de25f2c0f1e60967fc2a4) terminal/snapshot: 8-byte grid cells with blank elision ([@mitchellh](https://github.com/mitchellh))
  ```text
  Rework the PAGE grid encoding for codec speed and size. This is a
  breaking change to the work-in-progress version 1 wire format.
  
  Cells were previously a fixed 16-byte header plus inline grapheme
  suffixes: one byte each for content kind, width, and flags, a
  reserved byte, 16-bit style and hyperlink IDs, a 32-bit value, and an
  always-present 32-bit suffix count that was almost always zero. Cells
  are now one 64-bit little-endian word with a documented bit registry
  that carries the hyperlink ID in its high bits. The layout
  deliberately coincides with the native cell so clean rows encode as a
  straight copy of page memory and decode as one bulk read plus an
  in-place normalization pass; a comptime check falls back to a
  portable field-by-field codec if the native layout ever diverges.
  
  Each row header also gains an encoded cell count so trailing default
  cells are elided instead of spending 16 bytes apiece encoding
  nothing: on typical shell output most of every row is blank, and
  measurement showed 97% of encoded snapshot bytes were zero. Grapheme
  suffixes move out of the cell stream into a per-grid section of
  (row, column, codepoints) entries, which keeps row decoding
  fixed-stride and bulk-copyable.
  
  Decode ID remapping switches from hash maps to direct-indexed tables
  sized by the 16-bit encoded ID space, removing per-styled-cell hash
  lookups.
  
  Benchmark deltas at this commit (terminal-snapshot, M-series,
  ReleaseFast, 1 MB corpora):
  
    ascii lines 1-70:  34.16 MB -> 7.66 MB (4.5x)
                       encode 92.8 -> 18.2 ms, decode 119.8 -> 28.0 ms
    ascii full-wrap:   16.01 MB -> 8.04 MB (2.0x)
                       encode 43.6 -> 18.4 ms, decode  56.2 -> 25.6 ms
    utf8:               4.33 MB -> 1.90 MB (2.3x)
                       encode 12.4 ->  4.9 ms, decode  19.0 ->  9.6 ms
  ```
- [`9cc061c`](https://github.com/ghostty-org/ghostty/commit/9cc061c28cc79f5c11eae1299fe06fe486ada157) terminal/snapshot: hardware-accelerated CRC32C ([@mitchellh](https://github.com/mitchellh))
- [`9f66563`](https://github.com/ghostty-org/ghostty/commit/9f66563479df3b12e08d28fca2bb7bbe4ce65e16) terminal/snapshot: gate page verification on slow runtime safety ([@mitchellh](https://github.com/mitchellh))
  ```text
  PAGE decoding verified the complete native integrity of every decoded
  page unconditionally, building per-cell reference maps that accounted
  for roughly a fifth of decode time. The decoder normalizes every
  semantic value while decoding, so a completed decode upholds page
  invariants by construction and the verification only defends against
  decoder bugs. Follow the native page policy instead: assertIntegrity
  and friends run full verification only when slow runtime safety is
  enabled, which keeps the check in debug and test builds where those
  bugs are caught.
  
  Benchmark deltas at this commit (terminal-snapshot, 1 MB corpora):
  
    ascii lines 1-70:  decode 15.5 -> 12.2 ms (encode unchanged)
  ```
- [`3e5d128`](https://github.com/ghostty-org/ghostty/commit/3e5d128353171df595a9535e595f18a4406db0c2) terminal/snapshot: stage PAGE payloads while decoding ([@mitchellh](https://github.com/mitchellh))
  ```text
  PAGE payloads were decoded through a stack of stream adapters:
  a CRC32C-hashing reader over a length-limited reader over the
  BLAKE3-hashing snapshot reader. Every row paid several adapter
  crossings and both hashes were fed row-sized chunks, which kept
  BLAKE3 out of its efficient many-block path and made adapter
  overhead about a quarter of decode time.
  
  Decode now reads the remaining payload into a scratch buffer with
  one bulk read, so each hash sees the payload as a single update, and
  then parses the tables and grid from a flat in-memory reader. Row
  headers are also read as one three-byte read instead of two calls.
  Staging is capped at 8 MiB, far above any standard-capacity page
  payload, so a hostile declared length cannot force a large
  allocation; larger payloads fall back to the streaming path. CRC
  validation and exact-exhaustion checks are unchanged, with the
  staged reader checked for leftover bytes to preserve
  PayloadNotExhausted semantics.
  
  Benchmark deltas at this commit (terminal-snapshot, 1 MB corpora):
  
    ascii lines 1-70:  decode 12.2 -> 8.1 ms (encode unchanged)
    ascii full-wrap:   decode 11.1 -> 7.2 ms
    utf8:              decode  3.1 -> 2.1 ms
  
  Relative to the previous wire format and codecs, the series is a
  16.0x encode and 14.8x decode improvement on line-shaped scrollback
  at 4.5x smaller wire size.
  ```
- [`9e3019f`](https://github.com/ghostty-org/ghostty/commit/9e3019f1905496970e90eb9169fac4ebc0804321) terminal/snapshot: variable-width grid cell encoding ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a per-row encoded cell width to the PAGE grid format. Rows
  previously always spent eight bytes per cell, but a plain text cell
  carries only a codepoint: on line-shaped scrollback most encoded
  bytes were predictable zeros that still had to pass through CRC32C,
  BLAKE3, both codecs, and any transport compression the caller
  applies.
  
  Each row now declares one of four widths in previously reserved row
  flag bits, chosen canonically as the smallest width admitted by the
  bitwise OR of the row cell words: one or two bytes transport a bare
  codepoint, four bytes transport the low word half (any content kind,
  style IDs up to sixty-three, no wide or flag or hyperlink bits), and
  eight bytes remain the full word. Every width is a truncation on
  encode and a zero-extension on decode, so narrow rows encode and
  decode as vectorizable integer loops, one and two byte rows need at
  most surrogate replacement and skip cell normalization entirely, and
  full-width rows keep the existing bulk copy. Decoders use the
  declared width for framing and accept rows encoded wider than
  necessary. Rows containing wide characters, hyperlinks, semantic
  content, or large style IDs still use the full width, which leaves
  CJK-heavy content unchanged.
  
  Benchmark deltas at this commit (terminal-snapshot, M-series,
  ReleaseFast, 1 MB corpora):
  
    ascii lines 1-70:  7.66 MB -> 1.03 MB (7.4x)
                       encode 5.8 -> 2.0 ms, decode 8.1 -> 2.7 ms
    ascii full-wrap:   8.04 MB -> 1.04 MB (7.7x)
                       encode 5.4 -> 1.3 ms, decode 7.2 -> 1.8 ms
    utf8:              unchanged (wide cells keep rows at full width)
  
  For a caller compressing the stream, the lines snapshot end to end
  with zstd -1: encode plus compress 18.5 -> 2.8 ms, decompress plus
  decode 15.8 -> 3.6 ms, and the compressed size itself drops from
  1.35 MB to 0.86 MB because the packed stream is denser for the
  entropy coder.
  ```
- [`d351d9c`](https://github.com/ghostty-org/ghostty/commit/d351d9ce07d53c9bee9db4bf28a95c17c0a9d448) terminal/snapshot: more efficient binary form, optimize wire size + encode/decode speeds ([#13566](https://github.com/ghostty-org/ghostty/issues/13566)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Reworks the terminal PAGE grid wire format and optimize both
  encode/decode. Example improvements for 1MB of VT input w/ full
  scrollback: ~30x smaller wire size, ~45x faster encoding and decoding.
  
  > [!IMPORTANT]
  >
  > **Snapshot version 1 is still explicitly a work-in-progress format, so
  this breaks wire compatibility**.
  
  The original snapshot version I merged favored simplicity over
  optimization. This was the format used a proof-of-concept in my own
  projects, but I knew it wasn't what I wanted to ship. This PR looks at
  the record formats and trades simplicity for performance, a fair trade
  for a performance-sensitive binary format.
  
  Overview of changes:
  
  - **8-byte grid cells.** Cells are now one 64-bit word whose layout
  deliberately coincides with the native cell. Previously, cells were 16
  bytes each and in our 1MB corpus 97% of the data was `0`. Lol.
  - **Blank trailing cells are not written.** Rows declare an encoded cell
  count so trailing blank cells cost nothing.
  - **Hardware CRC32C.** Added `src/crc32c.zig` that uses inline-asm on
  aarch64/x86_64 to get hardware speeds for CRC32. Zig's stdlib is 0.56
  GB/s, aarch64 hardware is 10 GB/s on my computer.
  - **Variable-width cells.** Each row declares how many bytes transport
  each cell word: 1, 2, 4, or 8 depending on the widest row cell.
  
  ## Format
  
  Grid layout, per PAGE record:
  
  ```
     old                                new
     +--------------------------+      +--------------------------+
     | row 0                    |      | row 0                    |
     |   flags (1)              |      |   flags + width (1)      |
     |   cols * 16B cells with  |      |   encoded cell count (2) |
     |   inline suffixes        |      |   count * width cells    |
     +--------------------------+      +--------------------------+
     | ...                      |      | ...                      |
     +--------------------------+      +--------------------------+
     | row (rows - 1)           |      | row (rows - 1)           |
     +--------------------------+      +--------------------------+
                                       | grapheme suffix section  |
                                       +--------------------------+
  ```
  
  Every row previously carried exactly `cols` cells; now it carries cells
  only through its last non-default cell, and the cells past the count are
  implicitly zero. The row flag byte gains the encoded cell width in its
  previously reserved bits:
  
  ```
     bit 0 wrap                 bit 2-3 semantic prompt
     bit 1 wrap continuation    bit 4-5 encoded cell width (log2 bytes)
  ```
  
  The cell itself, old fixed 16-byte header versus the new single word:
  
  ```
     old (16 bytes + inline suffixes)     new (one u64 word)
     +--------+---------+--------+        bit  0 +------------------+
     | kind 1 | width 1 | flags 1|               | content kind  2b |
     +--------+---------+--------+        bit  2 +------------------+
     | zero 1 | style id 2       |               | content      24b |
     +--------+------------------+        bit 26 +------------------+
     | hyperlink id 2            |               | style ID     16b |
     +---------------------------+        bit 42 +------------------+
     | value 4                   |               | width kind    2b |
     +---------------------------+        bit 44 +------------------+
     | grapheme count 4          |               | protected     1b |
     +---------------------------+        bit 45 +------------------+
     | grapheme cps 4 * count    |               | hyperlink     1b |
     +---------------------------+        bit 46 +------------------+
                                                 | semantic      2b |
                                          bit 48 +------------------+
                                                 | hyperlink ID 16b |
                                          bit 64 +------------------+
  ```
  
  The word's bit layout intentionally matches the native cell (with the
  wire hyperlink ID in the native padding), so full-width rows are a
  straight copy of page memory. The row's encoded width then transports
  each word truncated, and decode is the matching zero-extension:
  
  ```
     width | bytes | admitted cells
     ------+-------+------------------------------------------------
       0   |   1   | codepoint <= U+00FF, nothing else set
       1   |   2   | codepoint <= U+FFFF, nothing else set
       2   |   4   | any content kind/codepoint, style IDs 1-63,
           |       | narrow, no flags, no hyperlink
       3   |   8   | everything
  ```
  
  Grapheme suffixes were inline after each cell, which forced per-cell
  framing decisions; they are now one section after the rows, so a
  grapheme-free page (the overwhelming case) pays 4 bytes total:
  
  ```
     old: ... | cell | cp cp | cell | ...      (inline, per cell)
  
     new: +----------------+----------------------------------+
          | entry count 4  | entries: row 2, col 2, count 2,  |
          |                |          count * codepoint 4     |
          +----------------+----------------------------------+
  ```
  
  ## Performance
  
  Setup: `ghostty-bench +terminal-snapshot`, 80x24 terminal with unlimited
  scrollback fed 1 MB of VT input.
  
  Per-commit improvements:
  
  | change                        | wire size | encode  | decode   |
  |-------------------------------|-----------|---------|----------|
  | baseline (v1 before this PR)  | 34.16 MB  | 92.8 ms | 119.8 ms |
  | 8-byte cells + blank elision  | 7.66 MB   | 18.2 ms | 28.0 ms  |
  | hardware CRC32C               | 7.66 MB   | 5.8 ms  | 15.5 ms  |
  | gate page verification        | 7.66 MB   | 5.8 ms  | 12.2 ms  |
  | staged PAGE payload decoding  | 7.66 MB   | 5.8 ms  | 8.1 ms   |
  | variable-width cells          | 1.03 MB   | 2.0 ms  | 2.7 ms   |
  
  Final result across various inputs:
  
  | corpus | wire size | encode | decode |
  
  |----------------------------|------------------------|----------------------|-----------------------|
  | ascii lines 1-70 | 34.16 -> 1.03 MB (33x) | 92.8 -> 2.0 ms (46x) |
  119.8 -> 2.7 ms (44x) |
  | ascii full-width wrap | 16.01 -> 1.04 MB (15x) | 43.6 -> 1.3 ms (34x)
  | 56.2 -> 1.8 ms (31x) |
  | utf8 (wide/grapheme heavy) | 4.33 -> 1.89 MB (2.3x) | 12.4 -> 1.7 ms
  (7x) | 19.0 -> 2.2 ms (9x) |
  
  ### Relationship with Compression
  
  I expect that users of this will wrap everything in compression, so I
  also benchmarked all my changes against a caller-owned zstd compressor
  to ensure we're making the write tradeoffs. Less bytes means less time
  in a compressor, even if a ton of 0s compresses really well.
  
  My results: `zstd -1` over the `lines` snapshot drops from 12.7 ms to
  0.8 ms, and the compressed artifact shrinks from 1.35 MB to 0.86 MB. So
  the end state is a win-win.
  ````
- [`3a606c6`](https://github.com/ghostty-org/ghostty/commit/3a606c6c41b83996d5f23860062548a63a08546c) macOS: install update with same code path ([@bo2themax](https://github.com/bo2themax))
- [`c992658`](https://github.com/ghostty-org/ghostty/commit/c992658b2994a560b052f79b241e4cd02df843c5) terminal/osc: decode OSC 52 base64 with the SIMD decoder ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  OSC 52 clipboard writes decoded their base64 payload with the scalar
  std implementation while Kitty graphics payloads already used the SIMD
  decoder in src/simd.
  
  Move clipboard path to use the same SIMD decoder. The encode side
  of the read reply stays scalar since the codebase has no SIMD
  encoder. 3.3x faster on a 4KB-payload decode micro-benchmark.
  ```
- [`39799a6`](https://github.com/ghostty-org/ghostty/commit/39799a61ce116a4f85e5f98582017383bd73ebc8) terminal/osc: decode OSC 52 base64 with the SIMD decoder ([#13565](https://github.com/ghostty-org/ghostty/issues/13565)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  use simd decoder for OSC 52 clipboard instead of the scalar impl.
  ```
- [`f424b20`](https://github.com/ghostty-org/ghostty/commit/f424b20589e3cd286a7ec3c49836849150c1bcf5) macOS: install update with same code path ([#13562](https://github.com/ghostty-org/ghostty/issues/13562)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously if you select "**Install and Relaunch**" in the update pill,
  there's still a confirmation alert about killing active process, but it
  will just relaunch regardlessly(which is the intended behaviour) when
  you do it in the command palette.
  
  Using UpdateState to check so Ghostty will relaunch immediately when
  user chooses "Install and Relaunch".
  
  > For the auto update case, this will be handled a bit differently in
  the future. If an update is already installed and waiting for relaunch
  (that the user is not aware of), quitting Ghostty will still remind them
  if there's active processes.
  ```
- [`a4f9b9c`](https://github.com/ghostty-org/ghostty/commit/a4f9b9cea23e84873f785c77eaa3475689354e43) Update VOUCHED list ([#13564](https://github.com/ghostty-org/ghostty/issues/13564)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/13563#issuecomment-5160200376)
  from @trag1c.
  
  Denounce: @guysoft
  ```
- [`aa74971`](https://github.com/ghostty-org/ghostty/commit/aa7497128252d8e4ba67b48a0d3908d91afa469f) build: lower iOS deployment target version ([@elias8](https://github.com/elias8))
- [`f024d21`](https://github.com/ghostty-org/ghostty/commit/f024d21fc46ab2110ef6573f7f5ea5263330cad7) Fix superfluous newline in html formatting ([@RoniJacobson](https://github.com/RoniJacobson))
  ```text
  Every page is formatted in a div, and when the div closes it creates a newline in the html rendering.
  In order to fix this a newline is now removed whenever the div is closed (if there are any newlines waiting to be rendered).
  ```
- [`75302fe`](https://github.com/ghostty-org/ghostty/commit/75302feda446d8340dd8a065fb706f72248658e9) Add test for superfluous newline in html formatting ([@RoniJacobson](https://github.com/RoniJacobson))
- [`f5911d6`](https://github.com/ghostty-org/ghostty/commit/f5911d6964c9ccf95b26a25882ea4620c7280f46) comment: fix grammar and acronym casing in message.zig doc comments ([@12ya](https://github.com/12ya))
  ```text
  - "the number of messages we send to the IO thread are also very few"
    had a subject-verb agreement issue; reworded to "is also very small"
  - Capitalized "pty" -> "PTY"
  ```
- [`a7cfa6f`](https://github.com/ghostty-org/ghostty/commit/a7cfa6fc238635af1ad8e4e5cc39980bbb3dc3b0) config: update scrollbar doc per current implementation ([@bo2themax](https://github.com/bo2themax))
- [`70e41e9`](https://github.com/ghostty-org/ghostty/commit/70e41e96d334d02668f8fda139fea3c020cf11bf) terminal/snapshot: pty continuation ([@mitchellh](https://github.com/mitchellh))
  ```text
  Builds on #13544
  
  This adds a new CONTINUATION record type that is sent before READY.
  CONTINUATION contains the bytes (if any) that will bring a ground-state
  VT state machine up to the same state.
  
  This allows snapshotting a terminal instance that is, for example,
  blocked waiting for a caller to complet an in-flight Kitty graphics
  protocol send. In practice, I think this will be rare. But in theory, it
  avoids a DoS-type attack.
  
  The continuation state must be the MINIMAL set of bytes that will move
  the virtual terminal state from a ground to non-ground state. The reason
  it must be minimal is because any extra bytes can duplicate work into the
  terminal that might already exist.
  ```
- [`e85bf9f`](https://github.com/ghostty-org/ghostty/commit/e85bf9fb2d36ad9cfb6dd879716ad9300c2e8ea6) terminal/snapshot: pty continuation record ([#13556](https://github.com/ghostty-org/ghostty/issues/13556)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Builds on #13544
  
  This adds a new CONTINUATION record type that is sent before READY.
  CONTINUATION contains the bytes (if any) that will bring a ground-state
  VT state machine up to the same state.
  
  This allows snapshotting a terminal instance that is, for example,
  blocked waiting for a caller to complet an in-flight Kitty graphics
  protocol send. In practice, I think this will be rare. But in theory, it
  avoids a DoS-type attack.
  
  The continuation state must be the MINIMAL set of bytes that will move
  the virtual terminal state from a ground to non-ground state. The reason
  it must be minimal is because any extra bytes can duplicate work into
  the terminal that might already exist.
  ```
- [`322636b`](https://github.com/ghostty-org/ghostty/commit/322636bfb0f467b179b7b59383956149759fb525) config: update scrollbar doc per current implementation ([#13553](https://github.com/ghostty-org/ghostty/issues/13553)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  We should also update the doc after #9865, which is discussed in
  https://github.com/ghostty-org/ghostty/discussions/9610
  ```
- [`f683042`](https://github.com/ghostty-org/ghostty/commit/f6830420cefb3b06552dad2e29f09f6f302dd57b) termio: fix doc comment grammar and PTY casing in message.zig ([#13549](https://github.com/ghostty-org/ghostty/issues/13549)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ### What
  Comment-only cleanup in `src/termio/message.zig`:
  
  - Fixes a subject-verb agreement error in the `Message` union's doc
    comment: "the number of messages ... are also very few" -> "is also
    very small"
  - Capitalizes "pty" to "PTY" in several doc comments
  
  ### Why
  Caught while reading through `message.zig`. No functional changes,
  doc comments only.
  ```
- [`915496c`](https://github.com/ghostty-org/ghostty/commit/915496c22104b621a70c29557dede737f9398f3c) libghostty(formatter): fix superfluous newline in html formatting ([#13543](https://github.com/ghostty-org/ghostty/issues/13543)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  In the html formatter every page is formatted in a div. When the div
  closes it causes a newline in the html rendering. In order to fix this a
  newline is now removed whenever the div is closed (if there are any
  newlines waiting to be rendered - as far as I could see in my testing
  there was always one).
  
  I thought of trying to add a test but could not think of a way to do so
  without adding a massive blob of html into the file.
  
  Before (orange was added by me to show where the div ends):
  <img width="1278" height="586" alt="image"
  src="https://github.com/user-attachments/assets/473ba28d-bec0-481f-9a89-a6a72c9a3657"
  />
  
  After:
  <img width="959" height="439" alt="image"
  src="https://github.com/user-attachments/assets/27bae0d3-cc82-4dc8-aa72-c4a8b0f7d424"
  />
  
  No AI was used in this pr.
  ```
- [`bab076c`](https://github.com/ghostty-org/ghostty/commit/bab076c1a2dfbf7fd288d4221fc1feb830e45b82) build: lower iOS deployment target version ([#13539](https://github.com/ghostty-org/ghostty/issues/13539)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Reopening #13535.
  ```
- [`6837d70`](https://github.com/ghostty-org/ghostty/commit/6837d7027f226355db661e8215a3ad24ffaf4eb5) Update VOUCHED list ([#13550](https://github.com/ghostty-org/ghostty/issues/13550)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/13549#issuecomment-5157211534)
  from @trag1c.
  
  Vouch: @12ya
  ```

## August 1, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/30719797621), [2](https://github.com/ghostty-org/ghostty/actions/runs/30710337334), [3](https://github.com/ghostty-org/ghostty/actions/runs/30708032098), [4](https://github.com/ghostty-org/ghostty/actions/runs/30707014679), [5](https://github.com/ghostty-org/ghostty/actions/runs/30702183255), [6](https://github.com/ghostty-org/ghostty/actions/runs/30682038661), [7](https://github.com/ghostty-org/ghostty/actions/runs/30681000128)  
Summary: 7 runs • 65 commits • 10 authors

### Changes

- [`cc1d262`](https://github.com/ghostty-org/ghostty/commit/cc1d262105b31dc3f2607fd34ff036a004347fec) macOS: fix update error pill is not showing properly ([@bo2themax](https://github.com/bo2themax))
- [`68beeeb`](https://github.com/ghostty-org/ghostty/commit/68beeeb3f6c9d296d99d821b17a477623d98b035) terminal: add stream continuation tracking for replay ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds opt-in continuation tracking to `terminal.Stream` that allows
  any caller to call `writeContinuation` in order to get the minimum bytes
  necessary from a grounded parser state to the identical state.
  
  This enables reliable stream restart across serialization states, which
  could be used for local restart, networked terminals, etc. For me, this
  is used for multiplexers. :)
  
  ## Implementation
  
  The implementation of this was really carefully done to avoid any
  negative performance impact particularly when continuation tracking is
  _off_.
  
  The way this work is simple:
  
    1. ESC is the only char that leaves the ground state and most
       ESC sequences are short. So if we're in a non-ground state, we
       do a backwards vectorized search to find the last `ESC` in the
       input slice. If one doesn't exist, we assume we found it previously
       and store the whole slice (rare, since ESC sequences are usually
       short like I said).
  
    2. If we're in the ground state that means we only have a potential
       incomplete UTF-8 codepoint, so we find the lead UTF-8 byte.
  
    3. When writing, we normalize the suffix to drop things like BEL
       commands that would've already been handled to avoid
       double-calling.
  
  ## Performance
  
  Via `ghostty-bench +terminal-stream`
  
    Corpus                     main      tracking off  tracking on
    plain ASCII (256 MiB)      175.4ms   175.8ms       175.5ms
    UTF-8 (32 MiB)             268.4ms   270.0ms       269.9ms
    5% invalid UTF-8 (32 MiB)  316.4ms   317.8ms       320.2ms
    CSI-heavy (32 MiB)         145.0ms   146.3ms       145.9ms
    OSC (32 MiB)               1621.0ms  1627.5ms      1638.3ms
    Kitty APC (128 MiB)        95.5ms    96.9ms        96.3ms
    mixed traffic (32 MiB)     172.4ms   172.0ms       172.3ms
    giant APC (128 MiB)        38.3ms    38.3ms        40.8ms
  ```
- [`f588078`](https://github.com/ghostty-org/ghostty/commit/f5880782fe34faccd30bb0c903055987171b6370) terminal: add stream continuation tracking for replay ([#13544](https://github.com/ghostty-org/ghostty/issues/13544)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds opt-in continuation tracking to `terminal.Stream` that allows
  any caller to call `writeContinuation` in order to get the minimum bytes
  necessary from a grounded parser state to the identical state.
  
  This enables reliable stream restart across serialization states, which
  could be used for local restart, networked terminals, etc. For me, this
  is used for multiplexers. :)
  
  **LLM usage:** I wrote the continuation tracker myself, used a mix of
  5.6+Fable to review it for me, applied their feedback directly. Only
  place with predominantly AI code are tests, which I reviewed. Commit and
  PR message written myself.
  
  ## Implementation
  
  The implementation of this was really carefully done to avoid any
  negative performance impact particularly when continuation tracking is
  _off_.
  
  The way this work is simple:
  
  1. ESC is the only char that leaves the ground state and most ESC
  sequences are short. So if we're in a non-ground state, we do a
  backwards vectorized search to find the last `ESC` in the input slice.
  If one doesn't exist, we assume we found it previously and store the
  whole slice (rare, since ESC sequences are usually short like I said).
  
  2. If we're in the ground state that means we only have a potential
  incomplete UTF-8 codepoint, so we find the lead UTF-8 byte.
  
  3. When writing, we normalize the suffix to drop things like BEL
  commands that would've already been handled to avoid double-calling.
  
  ## Performance
  
  No real impact.
  
  Via `ghostty-bench +terminal-stream`.
  
  Corpus | Main | PR w/ Tracking Off | PR w/ Tracking On
  -- | -- | -- | --
  Plain ASCII (256 MiB) | 175.4 ms | 175.8 ms | 175.5 ms
  UTF-8 (32 MiB) | 268.4 ms | 270.0 ms | 269.9 ms
  5% invalid UTF-8 (32 MiB) | 316.4 ms | 317.8 ms | 320.2 ms
  CSI-heavy (32 MiB) | 145.0 ms | 146.3 ms | 145.9 ms
  OSC (32 MiB) | 1621.0 ms | 1627.5 ms | 1638.3 ms
  Kitty APC (128 MiB) | 95.5 ms | 96.9 ms | 96.3 ms
  Mixed traffic (32 MiB) | 172.4 ms | 172.0 ms | 172.3 ms
  Giant APC (128 MiB) | 38.3 ms | 38.3 ms | 40.8 ms
  ```
- [`46edeee`](https://github.com/ghostty-org/ghostty/commit/46edeee407ff1cd15fb7db3837025386b2f3a327) macOS: fix update error pill is not showing properly ([#13540](https://github.com/ghostty-org/ghostty/issues/13540)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `acknowledgement` will call `dismissUpdateInstallation` so the error
  state will never happen.
  ```
- [`60b4a35`](https://github.com/ghostty-org/ghostty/commit/60b4a358548a658bbb9810688e0cf7ba617edc9e) Fix CircBuf metadata after shrinking ([@fallintoplace](https://github.com/fallintoplace))
- [`7a512c3`](https://github.com/ghostty-org/ghostty/commit/7a512c31252e32751e0d2691dd6ce48c68fc9798) gtk: fix capitalization of banner title ([@jcollie](https://github.com/jcollie))
- [`e9e7864`](https://github.com/ghostty-org/ghostty/commit/e9e7864b43c7ce8bc520f95f964f7409f2d12dfe) remove fuzze entries in *.po files ([@jcollie](https://github.com/jcollie))
- [`b2d4462`](https://github.com/ghostty-org/ghostty/commit/b2d44625908eb56aee299d8511d803bc11ab79fc) gtk: fix capitalization of banner title ([#10642](https://github.com/ghostty-org/ghostty/issues/10642)) ([@trag1c](https://github.com/trag1c))
- [`2ee42ad`](https://github.com/ghostty-org/ghostty/commit/2ee42adc76bd9270d754ae38415cfc7d5018654c) datastruct/circ_buf: fix metadata after shrinking ([#13515](https://github.com/ghostty-org/ghostty/issues/13515)) ([@jcollie](https://github.com/jcollie))
  ```text
  ## Summary
  
  - normalize circular-buffer metadata after every resize
  - retain the oldest values when shrinking below the current length
  - cover partial shrink, exact-length shrink, and empty-to-zero
  boundaries
  
  ## Root cause
  
  `resize` rotated live values to index zero before reallocating, but only
  repaired `head` and `full` when capacity grew. Shrinking a partially
  filled buffer could therefore leave `head` beyond the new allocation and
  report a length greater than capacity. A later append could index
  outside the resized storage.
  
  ## Validation
  
  - `zig fmt --check src/datastruct/circ_buf.zig`
  - `zig test src/circ_buf_test.zig --test-filter 'CircBuf resize'` using
  a temporary import harness: 8 tests passed
  ```
- [`74ad15c`](https://github.com/ghostty-org/ghostty/commit/74ad15c104fda80da15ced0863c0d4b1673be37f) Update VOUCHED list ([#13542](https://github.com/ghostty-org/ghostty/issues/13542)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/13527#issuecomment-5152299257)
  from @jcollie.
  
  Vouch: @gadgetman6
  ```
- [`e40a547`](https://github.com/ghostty-org/ghostty/commit/e40a5475dbca846f80d18314337b797efd1e4ff4) Rewrite localization teams docs for clarity and permit reviewer bias. ([@00-kat](https://github.com/00-kat))
- [`ad96613`](https://github.com/ghostty-org/ghostty/commit/ad96613a8c04093b94ab05107fc9fc22d802c380) inspector: add copy and export for terminal IO events ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  Adds "Copy" and "Export to file" buttons to the Terminal IO inspector
  so recorded VT events can be saved outside the app for sharing or
  analysis.
  
  Export is wired up through a new export_terminal_io apprt action,
  handled with a native save dialog on both macOS and GTK.
  ```
- [`31f4931`](https://github.com/ghostty-org/ghostty/commit/31f4931f8b053abc72fdf17aa3173aa0ed85f27c) i18n: add missing strings ([@Uzaaft](https://github.com/Uzaaft))
- [`2c0d258`](https://github.com/ghostty-org/ghostty/commit/2c0d2588a746e75240273986977c93fb604bfa73) inspector: make `FileChooser` cast type-safe ([@Uzaaft](https://github.com/Uzaaft))
- [`57ad6c7`](https://github.com/ghostty-org/ghostty/commit/57ad6c77a5121fa920a938450c722b22385f2cdd) Rewrite the localization teams docs to improve legibility, and explicitly permit members who know each other ([#12720](https://github.com/ghostty-org/ghostty/issues/12720)) ([@pluiedev](https://github.com/pluiedev))
  ```text
  ~~Maybe I have too many exclamation marks, let me know if I should
  metaphorically calm down.~~ Fixed now.
  
  My wording is intentionally biased toward languages spoken less
  (**edit**: not nearly as much anymore), but I specifically do not
  disallow members who know each other regardless of language popularity.
  Quoting myself from Discord[^convo]:
  
  > people who know each other are more likely to have more similar tastes
  or quirks in their language use by virtue of (perhaps subconsciously)
  stealing off each other, and there's also the whole “eh it's good enough
  i trust that you thought it through” thing that's more likely if you
  know the other translators already
  
  I don't believe it's *necessarily worse*, and if you have more than two
  members then the issue greatly diminishes too, but I don't want people
  to see this and go “oh no I need to get my translations in before
  Ghostty 1.4 that releases while I'm sleeping tomorrow so I should ask my
  bestie to help”, and to instead be willing to be more patient, at least
  for a reasonable amount of time (which I consider to be ≤ 2 months).
  
  [^convo]: @trag1c and I chatted about this prior to this PR in
  `#maintainers` on the Ghostty Discord server. If you have access to that
  channel, check out these links:
  [1](https://discord.com/channels/1005603569187160125/1337443701403815999/1504241367357063188),
  [2](https://discord.com/channels/1005603569187160125/1337443701403815999/1504465642361979021),
  [3](https://discord.com/channels/1005603569187160125/1337443701403815999/1505255908676993135).
  ```
- [`631c71e`](https://github.com/ghostty-org/ghostty/commit/631c71e41c4d5e305ff826dbb5d7864e702b60ca) inspector: add copy and export for terminal IO events ([#13519](https://github.com/ghostty-org/ghostty/issues/13519)) ([@jcollie](https://github.com/jcollie))
  ```text
  Adds "Copy" and "Export to file" buttons to the Terminal IO inspector so
  recorded VT events can be saved outside the app for sharing or analysis.
  
  Found myself needing/wishing for this while I was debugging my tmux fork
  with libghostty-vt.
  
  
  Disclaimer: I haven't considered performance at all, so please lmk if
  there are anything here you would like me to optimize.
  ```
- [`dc52c24`](https://github.com/ghostty-org/ghostty/commit/dc52c248e73386fef496c3bbe8643d6276b7fbfc) benchmark: terminal-resize ([@mitchellh](https://github.com/mitchellh))
- [`4a88cc5`](https://github.com/ghostty-org/ghostty/commit/4a88cc5948295019d85f09ad77bcc303b7aba69a) terminal: skip reflow pin scans for rows without pins ([@mitchellh](https://github.com/mitchellh))
  ```text
  Reflow scanned the full tracked pin list for every source cell it
  copied, twice per cell in the wide-character case, even though pins
  are rare and at most a handful exist. Each check also went through
  node.page(), which can restore a compressed page just to compare
  pointers.
  
  reflowRow now determines once per row whether any tracked pin is on
  the source row and skips the per-cell pin scans entirely when there
  is none, which is the overwhelmingly common case. The comparisons
  use node identity instead of pages: a node owns exactly one page, so
  they are equivalent, and this avoids the restore hazard.
  
  1.09x faster on ghostty-bench +terminal-resize --mode=cols (120x80
  terminal, 10k-line scrollback, shrink/grow column reflow cycles).
  ```
- [`c5ca2db`](https://github.com/ghostty-org/ghostty/commit/c5ca2db1b6ef2d8a160767cb0c13ec2d2061e83f) terminal: memoize style id mapping during reflow ([@mitchellh](https://github.com/mitchellh))
  ```text
  Memoize the most recent style mapping and when there is a reuse
  bump the ref with `use()`. This avoids a lookup (`addWithId`) on
  every single styled cell.
  
  1.25x faster on ghostty-bench +terminal-resize --mode=cols (120x80
  terminal, 10k-line scrollback, shrink/grow column reflow cycles).
  ```
- [`c249b9d`](https://github.com/ghostty-org/ghostty/commit/c249b9de3496bc3e8c4128686ba64553e17409a8) terminal: bulk-copy runs of simple cells during reflow ([@mitchellh](https://github.com/mitchellh))
  ```text
  Reflow copied every cell through a per-cell state machine
  (writeCell) that dispatches on content tag, wide property, grapheme,
  hyperlink, and style handling, and advances the destination cursor
  one cell at a time. The vast majority of cells in practice are
  narrow text or bg-color cells with no managed memory that share a
  single style across long runs.
  
  reflowRow now scans ahead for the run of such cells bounded by the
  remaining space in the destination row, copies the run with a single
  memcpy, and adjusts the style ref count once for the whole run via
  useMultiple. Wide characters, spacers, graphemes, hyperlinks, Kitty
  placeholders, and rows containing tracked pins all take the original
  per-cell path, and a style set failure falls back to writeCell which
  handles growing page capacity.
  
  2.19x faster on ghostty-bench +terminal-resize --mode=cols (120x80
  terminal, 10k-line scrollback, shrink/grow column reflow cycles).
  ```
- [`179161c`](https://github.com/ghostty-org/ghostty/commit/179161c081199d49c6b1238418b0a8712855e2f3) terminal: memoize reflow new-page capacity adjustment ([@mitchellh](https://github.com/mitchellh))
  ```text
  reflowRow computed the capacity for prospective destination pages on
  every source row via Capacity.adjust, which performs a full page
  layout calculation to find the available grid space.
  
  The result only depends on the source page, and reflow visits source pages
  sequentially and never revisits one, so memoize the adjustment per
  source page so we only do this once.
  
  1.06x faster on ghostty-bench +terminal-resize --mode=cols (120x80
  terminal, 10k-line scrollback, shrink/grow column reflow cycles).
  ```
- [`46276d0`](https://github.com/ghostty-org/ghostty/commit/46276d046ced8930501c8a7a056d96fecf9aa789) terminal: recycle pages within a column reflow ([@mitchellh](https://github.com/mitchellh))
  ```text
  In `resizeCols`, stash the most recently finished source node
  instead of destroying it, so we can recycle it without a bunch of
  syscalls.
  
  1.30x faster on ghostty-bench +terminal-resize --mode=cols (120x80
  terminal, 10k-line scrollback, shrink/grow column reflow cycles),
  with system time dropping from 34ms to 8ms per run.
  ```
- [`0fb3565`](https://github.com/ghostty-org/ghostty/commit/0fb3565c768ea6a07cfa5d3d71d106a126af667a) terminal: support nested field paths and eqlAny in Mask ([@mitchellh](https://github.com/mitchellh))
  ```text
  Two small extensions to the Mask helper, both motivated by the
  reflow bulk run scan in the next commits.
  
  fieldMask now accepts dot-separated field paths so a mask can cover
  a nested field of a packed struct or packed union member, e.g.
  "content.codepoint.data" covers exactly the codepoint bits of a cell
  without its padding. Packed union members all share bit offset zero.
  
  Mask gains eqlAny, the "any" counterpart to eql: it returns whether
  any value in a group has masked fields equal to the expected
  pattern. This supports run scans that must stop when a sentinel
  value appears anywhere in a group, such as the Kitty virtual
  placeholder codepoint which requires slow-path handling.
  ```
- [`d4e446c`](https://github.com/ghostty-org/ghostty/commit/d4e446c4803d2ad6dd3a3eb40a1dd9ad6037fc21) terminal: reduce reflow run scan to masked compares ([@mitchellh](https://github.com/mitchellh))
  ```text
  Finding the length of a bulk-copyable cell run evaluated the
  field-wise bulkCopyable predicate plus a style compare per cell,
  which compiles to a chain of extracts and branches and had become
  the hottest loop in a column reflow.
  
  Once the first cell passes the full predicate, a cell continues the
  run iff it matches the first cell in content tag, style id, wide
  property, and hyperlink flag, so the continuation test is now a
  masked compare of the raw cell bits via the Mask helper, plus a
  masked equality test against the Kitty virtual placeholder codepoint
  for text runs (placeholders must set a row flag so they take the
  slow path). This is slightly stricter than the predicate (a bg-color
  cell no longer extends an unstyled text run), which only splits a
  copy into multiple runs and remains correct.
  
  1.21x faster on ghostty-bench +terminal-resize --mode=cols (120x80
  terminal, 10k-line scrollback, shrink/grow column reflow cycles).
  ```
- [`ec5b369`](https://github.com/ghostty-org/ghostty/commit/ec5b369611ae59675d7c78168dd25600b85d105f) terminal: vectorize reflow run scan ([@mitchellh](https://github.com/mitchellh))
  ```text
  The masked-compare scan that finds bulk-copyable cell runs still
  processed one cell per iteration and remained the largest single
  cost in a column reflow.
  
  Scan whole groups of cells at a time using the group variants of the
  Mask helper: a group that fully matches the run pattern (and, for
  text runs, contains no Kitty virtual placeholder, via eqlAny)
  extends the run by the whole group, and any mismatch falls through
  to the scalar loop which finds the exact end of the run within it.
  The group length comes from the shared simd.lanes helper where the
  target has SIMD support and falls back to a plain unrolled group
  elsewhere.
  
  1.19x faster on ghostty-bench +terminal-resize --mode=cols (120x80
  terminal, 10k-line scrollback, shrink/grow column reflow cycles).
  Combined with the preceding reflow optimizations, resize with reflow
  is 5.8x faster than before the series.
  ```
- [`aa21cae`](https://github.com/ghostty-org/ghostty/commit/aa21caeaa3a2feb6ef1251d20bd81b52f1da0940) terminal: improve resize with reflow performance (~6x faster) ([#13537](https://github.com/ghostty-org/ghostty/issues/13537)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Improves the time to resize mixed content w/ wrapping 120x80, 10k lines
  of scrollback by about ~6x.
  
  I'm working on deferred resize in another branch, but it still follows
  roughly the same logic so I instead decided to shift course and look at
  the existing full-pagelist resize+reflow and found many places to
  improve while keeping understanding.
  
  The optimizations here match the general patterns of other recent
  optimizations: cache some stuff, reuse some pages, bring in our
  `page.Mask` helper and add vectorized ops. Nothing exotic we haven't
  been doing recently.
  
  Also note the Neovim project brought this up as a noticeable issue and I
  believe this will help mitigate their issues until we get proper
  deferred reflow in.
  
  **LLM notes:** The optimizations were produced with Fable 5 using a
  profile-driven approach (macOS `sample` plus disassembly-level
  attribution of the hot loops at each step). I then requested each be
  split into its own measurable commit, reviewed each in isolation, and
  modified most of the commit messages. This PR message is hand-written.
  ```
- [`8fca649`](https://github.com/ghostty-org/ghostty/commit/8fca64957b8e5fc7348378f116179af56df3151d) cli: report ssh terminfo cache failures ([@jparise](https://github.com/jparise))
  ```text
  A state directory with the wrong permissions left the terminfo cache
  failing with errors that named no path, so there was nothing to act on:
  
      $ ghostty +ssh-cache --add=user@host
      Error: Unable to add 'user@host' to cache. Error: error.AccessDenied
  
  Every +ssh-cache failure now names its cache file, and +ssh no longer
  swallows cache-related errors.
  
  Error messages in these actions are also lowercased after the "Error: "
  prefix and append the error with ": {t}" rather than a second "Error: ".
  
  Ref: https://github.com/ghostty-org/ghostty/issues/9393#issuecomment-5145799368
  ```
- [`ca3dc9e`](https://github.com/ghostty-org/ghostty/commit/ca3dc9eeac7893d6ac4507d60761226cb16fd09f) cli: classify ssh cache errors in DiskCache ([@jparise](https://github.com/jparise))
- [`08f039f`](https://github.com/ghostty-org/ghostty/commit/08f039fbb3dea9c6b1cdb5ff4550666598122346) cli: report ssh terminfo cache failures ([#13533](https://github.com/ghostty-org/ghostty/issues/13533)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A state directory with the wrong permissions left the terminfo cache
  failing with errors that named no path, so there was nothing to act on:
  
      $ ghostty +ssh-cache --add=user@host
      Error: Unable to add 'user@host' to cache. Error: error.AccessDenied
  
  Every +ssh-cache failure now names its cache file, and +ssh no longer
  swallows cache-related errors.
  
  Error messages in these actions are also lowercased after the "Error: "
  prefix and append the error with ": {t}" rather than a second "Error: ".
  
  Ref:
  https://github.com/ghostty-org/ghostty/issues/9393#issuecomment-5145799368
  ```
- [`fdf8dfd`](https://github.com/ghostty-org/ghostty/commit/fdf8dfd7b17410751d9ec7e082665b07ec9d31b5) terminal/snapshot: define v0 record framing ([@mitchellh](https://github.com/mitchellh))
- [`b4fd26f`](https://github.com/ghostty-org/ghostty/commit/b4fd26f0d934809f12333f1bf81c38f7ab6beeec) terminal/snapshot: hyperlink and style encoding ([@mitchellh](https://github.com/mitchellh))
- [`805c3b0`](https://github.com/ghostty-org/ghostty/commit/805c3b0bafc28bc063d3fe9b8e73261075a0525a) terminal/snapshot: start page encoding ([@mitchellh](https://github.com/mitchellh))
- [`d44baa9`](https://github.com/ghostty-org/ghostty/commit/d44baa91476ad3747271a52575ff147193102b14) terminal/snapshot: setup the snapshot main ([@mitchellh](https://github.com/mitchellh))
- [`2fc238e`](https://github.com/ghostty-org/ghostty/commit/2fc238ed01bca7c3bc46a8a728ac35356fb4b4a8) terminal/snapshot: decode directly into pages ([@mitchellh](https://github.com/mitchellh))
- [`406f5e7`](https://github.com/ghostty-org/ghostty/commit/406f5e7d82466e4bee0a3b1289df9905053b1968) terminal/snapshot: encode sparse page grids ([@mitchellh](https://github.com/mitchellh))
- [`83ffa74`](https://github.com/ghostty-org/ghostty/commit/83ffa74e2b9057614a1f204747faa4d54a742012) terminal/snapshot: page records ([@mitchellh](https://github.com/mitchellh))
- [`e8e56e7`](https://github.com/ghostty-org/ghostty/commit/e8e56e782c7cfa277839b489d5b13396f8bbe24b) terminal/snapshot: small edits ([@mitchellh](https://github.com/mitchellh))
- [`6508cbb`](https://github.com/ghostty-org/ghostty/commit/6508cbbb49616a1b12f80f225f87240e10c2db49) terminal/snapshot: screen record ([@mitchellh](https://github.com/mitchellh))
- [`f50bdfa`](https://github.com/ghostty-org/ghostty/commit/f50bdfab200b97142f4cf97feb3b7a456552f389) terminal/snapshot: screen plus active encoding ([@mitchellh](https://github.com/mitchellh))
- [`d34fd05`](https://github.com/ghostty-org/ghostty/commit/d34fd0593eb241b7f76e7ab9e01cb079e4bc92c0) terminal/snapshot: screen decoding ([@mitchellh](https://github.com/mitchellh))
- [`7d91b87`](https://github.com/ghostty-org/ghostty/commit/7d91b8776664208a1582846f1286396edbce04da) terminal/snapshot: history record ([@mitchellh](https://github.com/mitchellh))
- [`0288bec`](https://github.com/ghostty-org/ghostty/commit/0288bec3cf314af00fb1b8425b32fc578fb23019) terminal/snapshot: terminal record ([@mitchellh](https://github.com/mitchellh))
- [`83e4827`](https://github.com/ghostty-org/ghostty/commit/83e482700b7e647bc9c6da985493f7b2ae991e92) terminal/snapshot: ready/finish checkpoints ([@mitchellh](https://github.com/mitchellh))
- [`86ec146`](https://github.com/ghostty-org/ghostty/commit/86ec1463348441fa0b914dbde8b657eb96148775) terminal/snapshot: full encode/decode ([@mitchellh](https://github.com/mitchellh))
- [`b867a0f`](https://github.com/ghostty-org/ghostty/commit/b867a0f59e3ceee335828cc79e2c7bdb2a69c467) terminal/snapshot: use lib.Enum enums where possible ([@mitchellh](https://github.com/mitchellh))
- [`43ec9b3`](https://github.com/ghostty-org/ghostty/commit/43ec9b373b76a8c0e86a093f63aee643e01c69ff) terminal/snapshot: harden hyperlink decoding, allow invalid hyperlinks for page ([@mitchellh](https://github.com/mitchellh))
- [`92c8dfd`](https://github.com/ghostty-org/ghostty/commit/92c8dfd5084d8e9b88397dab1cb61ad0d38b1d4b) terminal/snapshot: clean up tests ([@mitchellh](https://github.com/mitchellh))
- [`32f11a4`](https://github.com/ghostty-org/ghostty/commit/32f11a4663c897366f91876b5dda7fdc715e6ac0) terminal/snapshot: test fixtures ([@mitchellh](https://github.com/mitchellh))
- [`627f343`](https://github.com/ghostty-org/ghostty/commit/627f3430975db22582b88a7f528518d58bdff188) build: helpgen needs terminal options ([@mitchellh](https://github.com/mitchellh))
- [`13bc78b`](https://github.com/ghostty-org/ghostty/commit/13bc78b7f33536351fef16b2e37992b845215679) terminal/snapshot: grid tests ([@mitchellh](https://github.com/mitchellh))
- [`38d92c5`](https://github.com/ghostty-org/ghostty/commit/38d92c50c9c8c19f543a13c126aa8710f9f6e856) terminal/snapshot: kaitai verification ([@mitchellh](https://github.com/mitchellh))
  ```text
  Describe the complete version 1 snapshot format with a Kaitai schema and make every golden fixture self-describing for automatic discovery. Add a verifier that compiles the schema, parses all fixtures, and checks record checksums, checkpoint digests, and cross-record invariants.
  
  Preserve Kaitai metadata when generating fixture candidates and provide the compiler and Python runtime dependencies through the development shell. Keep the mode registry portable to Kaitai JavaScript targets so the complete fixture also works in the web IDE.
  ```
- [`66ea61d`](https://github.com/ghostty-org/ghostty/commit/66ea61dd9d6f62995451ad92a3f499839ab7db7a) ci: verify snapshot kaitai ([@mitchellh](https://github.com/mitchellh))
  ```text
  Run the snapshot Kaitai verifier in its own required xsm job. This gives schema, fixture, checksum, and cross-record validation a distinct CI result without coupling it to the libghostty-vt test suite.
  ```
- [`f8ac0ca`](https://github.com/ghostty-org/ghostty/commit/f8ac0ca98fcc12c1970560dd40f7bb2e39dc3ba4) terminal/snapshot: accept kitty placeholder cells, track rows ([@mitchellh](https://github.com/mitchellh))
  ```text
  Treat Kitty virtual placeholder codepoints as ordinary valid grid content during snapshot restore and derive the native row lookup hint from decoded cells. Image and placement registries remain intentionally omitted.
  
  Cover the behavior with a complete snapshot round trip containing a real virtual placement and its grapheme diacritics.
  ```
- [`a508720`](https://github.com/ghostty-org/ghostty/commit/a508720a89c5e899e6bc8883e1cc23851ea4ddb8) terminal/snapshot: grid decode robustness principle ([@mitchellh](https://github.com/mitchellh))
  ```text
  Keep snapshot grid encoding strict by rejecting malformed wide-cell relationships before they can produce invalid wire data.
  
  Decode untrusted grids liberally while preserving record alignment. Unknown semantic values and content kinds degrade to safe defaults, optional graphemes and hyperlinks are dropped when invalid or over capacity, and malformed wide-cell markers normalize to narrow cells.
  ```
- [`465488d`](https://github.com/ghostty-org/ghostty/commit/465488d6b4f7a0eb7fac09e37aff8078f28b472a) terminal/snapshot: screen robustness ([@mitchellh](https://github.com/mitchellh))
  ```text
  Keep SCREEN encoding strict while allowing decoding to recover from unknown or noncanonical semantic state. Cursor positions now clamp to the restored active area, and invalid enum values, reserved bits, and optional state degrade to native defaults.
  ```
- [`a44eb83`](https://github.com/ghostty-org/ghostty/commit/a44eb8335884b104f2d44c4a613161db595e457f) terminal/snapshot: style/hyperlink robustness in page and screen ([@mitchellh](https://github.com/mitchellh))
  ```text
  Keep the standalone style and hyperlink codecs strict while allowing PAGE and SCREEN decoders to discard invalid optional data at boundaries they own. Normalize invalid styles to defaults, ignore unrepresentable hyperlinks, reuse duplicate entries, and validate hyperlink values before encoding.
  ```
- [`7c64181`](https://github.com/ghostty-org/ghostty/commit/7c64181b69df1ac6e7c1883aa939cfc2bfccde41) terminal/snapshot: history robustness ([@mitchellh](https://github.com/mitchellh))
  ```text
  Treat HISTORY row counts as canonical metadata rather than a reason to reject otherwise usable history. Restore topology from the declared PAGE sequence while keeping record framing, routing keys, and sequence boundaries strict.
  ```
- [`9d1c6a9`](https://github.com/ghostty-org/ghostty/commit/9d1c6a9217bc79e9598bacdf3c8160bfaddf6be7) terminal/snapshot: terminal robustness ([@mitchellh](https://github.com/mitchellh))
  ```text
  Normalize unknown terminal-wide semantic fields during restore while keeping dimensions and screen count structural. Preserve canonical encoding, ignore reserved mode and tab-stop bits, reset invalid color and scrolling state, and clamp finite scrollback policies to the native range.
  ```
- [`58e9209`](https://github.com/ghostty-org/ghostty/commit/58e92098a209a137ff6af376086ae965124ec5f1) terminal/snapshot: snapshot robustness ([@mitchellh](https://github.com/mitchellh))
  ```text
  Route HISTORY sequences by their encoded screen key so both keyed sequence groups can arrive in either order. Keep undeclared and duplicate routing strict, separate HISTORY manifest parsing from page restoration, and clear decoder-only generation state before returning the terminal.
  ```
- [`f0fe788`](https://github.com/ghostty-org/ghostty/commit/f0fe788fcc7ef47f7e59745e7884c9bcff295f17) terminal/snapshot: less buffering, better stream writing ([@mitchellh](https://github.com/mitchellh))
  ```text
  Stream complete snapshot records to any std.Io.Writer while retaining one reusable payload buffer for length and CRC calculation. Update BLAKE3 incrementally so checkpoints no longer require rehashing an allocating destination.
  
  Wrap decode hashing in StreamReader to enforce exact checkpoint boundaries. Preserve v1 bytes while allowing snapshots to begin at the current writer position and retaining only valid prefixes on failures.
  ```
- [`d37e1fe`](https://github.com/ghostty-org/ghostty/commit/d37e1fe184f0486e155d61b1cee1c6d82c8d199f) terminal/snapshot: format doesn't require EOF ([@mitchellh](https://github.com/mitchellh))
  ```text
  Treat FINISH as the self-delimiting snapshot boundary instead of peeking for end-of-file. Normal decoding now leaves continuation bytes unread, allowing snapshots and live protocol data to share a stream without waiting for closure.
  
  Add decodeExact for bounded files that still require strict exhaustion, and update the Kaitai schema, documentation, and tests for continuation and sequential snapshot decoding.
  ```
- [`e2e74fe`](https://github.com/ghostty-org/ghostty/commit/e2e74fecbe08cd545dc748435ab20cec424756d5) terminal/snapshot: move history size hints to screen record ([@mitchellh](https://github.com/mitchellh))
  ```text
  Publish each screen's logical history extent before READY so clients can size scrollbars while older pages are still arriving. Keep the value advisory and continue deriving native PageList totals from decoded pages.
  
  Reduce HISTORY to its structural screen key and page count, and update the format documentation, Kaitai schema, verifier, and versioned fixtures.
  ```
- [`05d4934`](https://github.com/ghostty-org/ghostty/commit/05d4934848307cb3025702d480a3bde20d901250) terminal/snapshot: better root export ([@mitchellh](https://github.com/mitchellh))
  ```text
  Expose complete encode and decode entry points directly from terminal.snapshot instead of requiring terminal.snapshot.snapshot. Reorder the decode APIs to accept the allocator and I/O context before the reader.
  ```
- [`6b09bb3`](https://github.com/ghostty-org/ghostty/commit/6b09bb3fcaad6805c56ed51528dd86df33d13030) terminal/snapshot: ignore hex files in typos ([@mitchellh](https://github.com/mitchellh))
  ```text
  Exclude annotated snapshot fixture hex files from typo checking. Their arbitrary binary byte sequences can otherwise be misidentified as misspelled words.
  ```
- [`154ddc2`](https://github.com/ghostty-org/ghostty/commit/154ddc2a2f071585ae5b64dfdb6565b3061e8604) terminal/snapshot: binary snapshot format ([#13534](https://github.com/ghostty-org/ghostty/issues/13534)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This adds the first version of a binary snapshot format for terminal
  state.
  
  Use cases: replay software (like asciinema), multiplexers (like zmx),
  scrollback-saving on disk, etc.
  
  The intention of the binary snapshot format is to be able to fully
  encode and decode terminal state across mediums such as network and
  disk. You can also encode partial terminal state (e.g. only one screen
  or even one page of contents). Long term, the intention is to also
  support streaming state while a live terminal is running, but this
  initial PR focuses on the full snapshot first (with some design choices
  to get to the streaming state in the future).
  
  The format is documented in the Zig code, but I also did a
  [Kaitai](https://kaitai.io/) descriptor and both the Zig and Kaitai spec
  verify they can parse committed fixtures. This helps identify drift in
  the format or encoder/decoders in any way since this must ultimately be
  a fixed format.
  
  > [!NOTE]
  >
  > **On reviewability:** this is a massive PR that I don't expect anyone
  to reasonably review. I'm going through it line-by-line (again) but I
  purposely extracted any changes that affect other parts of Ghostty out
  to other already-merged PRs. This one is isolated purely to a package
  that isn't called by any client software. **So the plan is if this rough
  shape looks good I'll merge it and we'll iterate from there.**
  
  > [!WARNING]
  >
  > **Experimental.** The format can and will change. And we may also
  decide that binary snapshotting in this way isn't the right direction
  altogether (although, I'm pretty confident it is). It'd be impossible to
  get a single large perfect PR because it'd be even larger than this by
  multiples. So instead, we'll iterate on main so long as this work is not
  touching any production code, which it isn't!
  
  ## Example
  
  Encode:
  
  ```zig
  const terminal = @import("terminal/main.zig");
  
  var file_buffer: [16 * 1024]u8 = undefined;
  var file_writer = file.writer(io, &file_buffer);
  try terminal.snapshot.encode(alloc, &file_writer.interface, &t);
  try file_writer.interface.flush();
  ```
  
  Decode a full terminal:
  
  ```zig
  var t = try terminal.snapshot.decode(&reader, io, alloc);
  defer t.deinit(alloc);
  ```
  
  ## Future
  
  This PR purposely only supports a synchronous encode/decode. I wanted to
  get the large groundwork in before iterating further. Some iterations in
  the future:
  
  * Kitty graphics
  * Live terminal snapshotting
  * PTY stream continuation records (so VT state machines can stay in
  sync)
  * Performance work (encoding and decoding, maybe size)
  * Configurable limits to prevent DoS
  * C API
  * etc...
  
  ## Wire format
  
  The "robustness principle" is a guiding principle: "be conservative in
  what you do, be liberal in what you accept from others." Our encoders
  have a lot of extra validation, our decoders massage invalid data into
  reasonable defaults (e.g. invalid styles become unstyled text).
  
  > [!IMPORTANT]
  >
  > **Version 1 has no compatibility promise.** We use version 1 in the
  envelope header. We will absolutely break this format as needed as we
  iterate and improve on it...
  
  ### Envelope
  
  Every snapshot starts with a fixed ten-byte envelope:
  
  | Offset | Size | Field |
  | ---: | ---: | :--- |
  | 0 | 8 | Magic: `GHOSTSNP` |
  | 8 | 2 | Snapshot version: `1` |
  
  ### Record framing
  
  After the envelope, records are concatenated back-to-back. Every record
  has a fixed header:
  
  | Offset | Size | Field |
  | ---: | ---: | :--- |
  | 0 | 2 | Record tag |
  | 2 | 4 | Payload length |
  | 6 | 4 | CRC32C |
  | 10 | variable | Payload |
  
  CRC32C covers the encoded tag, payload length, and payload. The
  payload-length boundary prevents a malformed record decoder from
  consuming bytes belonging to the next record.
  
  The registered record tags are:
  
  | Value | Tag | Purpose |
  | ---: | :--- | :--- |
  | 1 | `TERMINAL` | Terminal-wide state and declared screens |
  | 2 | `SCREEN` | One screen's live state and active page manifest |
  | 3 | `PAGE` | One self-contained set of rows and cells |
  | 4 | `HISTORY` | One screen's historical page manifest |
  | 5 | `READY` | Digest of the renderable prefix |
  | 6 | `FINISH` | Digest of the complete snapshot |
  
  To view the format of each record, read its corresponding
  `terminal/snapshot/<type>.zig` file.
  
  ### Complete record sequence
  
  ```text
  +----------------------------------------+
  | Envelope                               |
  +----------------------------------------+
  | TERMINAL                               |
  +----------------------------------------+
  | SCREEN * terminal.screen_count         |
  | PAGE   * each screen.page_count        |
  +----------------------------------------+
  | READY                                  |
  +----------------------------------------+
  | HISTORY * terminal.screen_count        |
  | PAGE    * each history.page_count       |
  +----------------------------------------+
  | FINISH                                 |
  +----------------------------------------+
  | Optional containing-transport bytes    |
  +----------------------------------------+
  ```
  
  `SCREEN` and `HISTORY` groups are routed by their encoded screen key and
  may arrive in either key order.
  
  ## Checkpoints and validation
  
  Each record has an independent CRC32C, but per-record checksums cannot
  detect a valid record being reordered, omitted, or duplicated. `READY`
  and `FINISH` therefore contain BLAKE3-256 digests over exact snapshot
  prefixes:
  
  - `READY` covers the envelope, `TERMINAL`, and all live `SCREEN`/`PAGE`
  sequences. It does not include itself.
  - `FINISH` covers that same prefix, the complete `READY` record, and all
  `HISTORY`/`PAGE` sequences. It does not include itself.
  
  This gives the format two useful integrity boundaries:
  
  ```text
  envelope ... active pages | READY | history pages | FINISH
  <------ renderable ------->
  <------------- complete snapshot --------------->
  ```
  
  ## Performance
  
  ### Size, Compression Recommended
  
  We intentionally use a simple grid over something like RLE (run-length
  encoding). So every row contains exactly `columns` cells and each is
  16-bytes! This is large! A 80x24, 10,000 line scrollback terminal
  uncompressed would be ~13MB. However, with zstd level 1 compression that
  goes down to 260K.
  
  ### Speed
  
  We haven't benchmarked encoding or decoding speed yet. This PR focused
  on getting a format in place. This will be heavily optimized later. I
  suspect its probably pretty darn slow, actually.
  
  ## Kaitai Struct
  
  I added a `snapshot.ksy` Kaita Struct spec that independently describes
  the complete format. This is used by us for format validation but it can
  also be used to programmatically generate parsers. For example, our test
  fixture in the Kaita Struct web IDE decodes to:
  
  <img width="523" height="779" alt="image"
  src="https://github.com/user-attachments/assets/cd199c73-b6d6-4b35-8957-0cfe3d1a18f2"
  />
  
  **AI Usage:** This work was done in concert with various models and
  agents. Writing full encoders/decoders is tedious so it took a lot of
  that way. A lot of review was done by AI (trying to find holes, issues,
  inconsistencies). The actual binary protocol design and iteration was
  done by me. This PR message was written by me.
  ````

## July 30, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/30572539376), [2](https://github.com/ghostty-org/ghostty/actions/runs/30565278840), [3](https://github.com/ghostty-org/ghostty/actions/runs/30528378351), [4](https://github.com/ghostty-org/ghostty/actions/runs/30510818052)  
Summary: 4 runs • 10 commits • 2 authors

### Changes

- [`b61fd5f`](https://github.com/ghostty-org/ghostty/commit/b61fd5fbb6830b2546cfcaab0e17e6df010e4075) terminal: add iterator to ref counted set ([@mitchellh](https://github.com/mitchellh))
- [`fc1bd06`](https://github.com/ghostty-org/ghostty/commit/fc1bd06a1a090d0ebe59a6b04b021440fbae5b57) terminal: PageList builder to build from raw pages ([@mitchellh](https://github.com/mitchellh))
- [`35db320`](https://github.com/ghostty-org/ghostty/commit/35db32078bc97a54334895bd32a83fce8fc0ef4c) terminal: PageList allocatePage ([@mitchellh](https://github.com/mitchellh))
- [`e77c261`](https://github.com/ghostty-org/ghostty/commit/e77c2612e51af6489cb60043af31aef2da3a5fa5) lib: Zig enums have stable values ([@mitchellh](https://github.com/mitchellh))
- [`457c5a0`](https://github.com/ghostty-org/ghostty/commit/457c5a0a64632282f7f8c2833013b38dc2c312ed) terminal: PageList align Builder/PageAllocation APIs better ([@mitchellh](https://github.com/mitchellh))
  ```text
  Rename Builder.addPage and PageAllocation.cancel to their consistent allocatePage and deinit forms. Track successful ownership transfers so both builder APIs can use unconditional deferred cleanup without releasing pages transferred to a PageList.
  ```
- [`4d605bf`](https://github.com/ghostty-org/ghostty/commit/4d605bf0d819df901a0332bbb320dc849fdd82e4) Misc improvements for future binary snapshot API ([#13525](https://github.com/ghostty-org/ghostty/issues/13525)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Extracted out the raw `src/terminal` changes needed for the future
  snapshot work, 4 separate changes. These are uncontroversial and
  relatively simple, summarized below. Tests AI assisted but the rest
  including commit messages, this PR message, etc. all organic.
  
  * **Add iterator to ref counted set.** Iterate over live entries and
  their IDs. Const, doesn't mutate the set.
  * **lib.Enum produces stable enums for Zig.** Basically the same as C
  except it uses the smallest fitting integer including the holes.
  * **PageList: a couple helpers for manually creating pages.** There is
  `PageList.Builder` for creating a new pagelist and
  `PageList.allocatePage` for modifying an existing one. This allows
  PageList construction from raw pages.
  ```
- [`d5c7e54`](https://github.com/ghostty-org/ghostty/commit/d5c7e54ae465895fe849de3f35a1440a434db983) terminal: fix string capacity check in hyperlink reflow ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13522
  
  Fixes unreachable when reflow dupes a hyperlink into a destination page
  whose string allocator is nearly full.
  
  The capacity precondition in ReflowCursor.writeCell performed a single
  test allocation of `uri.len + id.len` bytes before duping a hyperlink
  into the destination page. But PageEntry.dupe allocates the URI and
  the explicit ID as two separate allocations, and the string allocator
  rounds every allocation up to its 32-byte chunk size independently, so
  the two separate allocations can require one more chunk than the
  single combined test allocation.
  
  Write a new helper to make sure we get the right amount of space
  using the same allocation pattern of dupe.
  ```
- [`506de85`](https://github.com/ghostty-org/ghostty/commit/506de8517a6579926d35a7b9ae388f32afb8fe42) terminal: fix string capacity check in hyperlink reflow ([#13524](https://github.com/ghostty-org/ghostty/issues/13524)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13522
  
  Fixes unreachable when reflow dupes a hyperlink into a destination page
  whose string allocator is nearly full.
  
  The capacity precondition in ReflowCursor.writeCell performed a single
  test allocation of `uri.len + id.len` bytes before duping a hyperlink
  into the destination page. But PageEntry.dupe allocates the URI and the
  explicit ID as two separate allocations, and the string allocator rounds
  every allocation up to its 32-byte chunk size independently, so the two
  separate allocations can require one more chunk than the single combined
  test allocation.
  
  Write a new helper to make sure we get the right amount of space using
  the same allocation pattern of dupe.
  
  **AI note:** Verified upstream via Fable. I told it to ignore any
  conclusions and do its own validation and fix suggestion. It did
  validate it with a failing test which I studied. It implement a fix, I
  rewrote it to be more idiomatic.
  ```
- [`70c498a`](https://github.com/ghostty-org/ghostty/commit/70c498ac3273661aebf6cce9904c0d42b2e5d299) Update VOUCHED list ([#13521](https://github.com/ghostty-org/ghostty/issues/13521)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13520#discussioncomment-17837792)
  from @pluiedev.
  
  Vouch: @carlvillads
  ```
- [`96e39f8`](https://github.com/ghostty-org/ghostty/commit/96e39f82355d6bbc09f777c775bf01e667f3803e) Update VOUCHED list ([#13518](https://github.com/ghostty-org/ghostty/issues/13518)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13516#discussioncomment-17834904)
  from @jcollie.
  
  Vouch: @fallintoplace
  ```

## July 29, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/30467033163), [2](https://github.com/ghostty-org/ghostty/actions/runs/30460185353), [3](https://github.com/ghostty-org/ghostty/actions/runs/30419843281)  
Summary: 3 runs • 9 commits • 6 authors

### Changes

- [`9fc2a30`](https://github.com/ghostty-org/ghostty/commit/9fc2a3085201f8b51095ff509ef8ebf2b7ed2c55) url: exclude trailing spaces from path matches ([@ruseel](https://github.com/ruseel))
  ```text
  #13491
  #9921
  
  Path matching previously included end-of-line spaces. Pi redraws can
  leave blank cells after a path, causing cmd-click to open a pathname
  that includes those cells. Do not include trailing whitespace in path
  matches.
  
  AI disclosure: Pi using GPT-5.6 Terra High was used to investigate
  and write this change. I reviewed it personally.
  ```
- [`c3b5cab`](https://github.com/ghostty-org/ghostty/commit/c3b5cab94165ea253b8e33683d5fd76fdddb025a) wayland/Hotkeys: polish & simplify ([@pluiedev](https://github.com/pluiedev))
  ```text
  I've come up with a way to avoid manually allocating each entry which
  honestly makes the code flow much more smoothly. Basically you collect
  all the applicable keybinds first, then try to bind them with their
  stable memory addresses.
  ```
- [`adfef29`](https://github.com/ghostty-org/ghostty/commit/adfef29776abcafad57fa17c973a8651ab95b3b9) wayland/Hotkeys: polish & simplify ([#13512](https://github.com/ghostty-org/ghostty/issues/13512)) ([@jcollie](https://github.com/jcollie))
  ```text
  I've come up with a way to avoid manually allocating each entry which
  honestly makes the code flow much more smoothly. Basically you collect
  all the applicable keybinds first, then try to bind them with their
  stable memory addresses.
  ```
- [`6ad1fe7`](https://github.com/ghostty-org/ghostty/commit/6ad1fe7d8cbda36c77b337a96c9bea8a77883699) url: exclude trailing spaces from path matches ([#13505](https://github.com/ghostty-org/ghostty/issues/13505)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This change improves the user experience for Pi TUI users on macOS.
  
  As a user of Ghostty 1.3.1, Pi 0.80.7, and macOS 26.5, I noticed that
  Command-click was not working.
  
  With Pi's help (GPT-5.6 Terra High), I narrowed the cause down to Pi's
  redraw
  behavior and `src/config/url.zig`'s regular expression. More details are
  in
  [Vouch Request
  #13491](https://github.com/ghostty-org/ghostty/discussions/13491).
  
  The `trailing_spaces_at_eol` behavior in `src/config/url.zig` was
  introduced in
  [PR #9921](https://github.com/ghostty-org/ghostty/pull/9921) while
  improving
  Command-click handling for relative and local paths. The concern about
  matching
  trailing whitespace was also noted in [a review
  comment](https://github.com/ghostty-org/ghostty/pull/9921#issuecomment-3661107609).
  
  However, supporting file paths with trailing spaces does not seem like a
  good
  trade-off because it blocks Command-click for file paths displayed by Pi
  TUI.
  
  This PR removes that behavior.
  
  I tested this on my Mac with a patched Ghostty build, and Command-click
  worked
  correctly for file paths in Pi TUI.
  
  AI disclosure: I used Pi with GPT-5.6 Terra High to investigate and
  implement this change.
  I reviewed the code and tested the result myself.
  ```
- [`a34bf0d`](https://github.com/ghostty-org/ghostty/commit/a34bf0dce717fe29c209b77e58f0d6e372bb3747) Update VOUCHED list ([#13511](https://github.com/ghostty-org/ghostty/issues/13511)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13508#discussioncomment-17828581)
  from @jcollie.
  
  Vouch: @simonbcn
  ```
- [`4b58623`](https://github.com/ghostty-org/ghostty/commit/4b586231af5aa8c1f4221704ef452782715022ef) docs: clarify macOS dependencies ([@vegerot](https://github.com/vegerot))
  ```text
  reword: The doc said "macOS doesn't need any dependencies" and then immediately listed things you needed to install for macOS 😁.  This is just rewording the doc to be more consistent.
  ```
- [`1cc5e7b`](https://github.com/ghostty-org/ghostty/commit/1cc5e7bec1eb81c05bb79cc3af22c98cabdbe7cd) update zig-gobject to 0.3.2 ([@jcollie](https://github.com/jcollie))
  ```text
  Includes better ZIg 0.16 compat and updates for Gnome 50.
  ```
- [`6bbbf59`](https://github.com/ghostty-org/ghostty/commit/6bbbf59e9fb08b769539899f27034c50b4ac8de2) update zig-gobject to 0.3.2 ([#13502](https://github.com/ghostty-org/ghostty/issues/13502)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Includes better ZIg 0.16 compat and updates for Gnome 50.
  ```
- [`ae87274`](https://github.com/ghostty-org/ghostty/commit/ae8727401d8c549671c36cdc326a94f47c94b635) docs: clarify macOS dependencies ([#13498](https://github.com/ghostty-org/ghostty/issues/13498)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  reword: The doc said "macOS doesn't need any dependencies" and then
  immediately listed things you needed to install for macOS 😁. This is
  just rewording the doc to be more consistent.
  ```

## July 28, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/30394987951), [2](https://github.com/ghostty-org/ghostty/actions/runs/30393463354), [3](https://github.com/ghostty-org/ghostty/actions/runs/30380212926), [4](https://github.com/ghostty-org/ghostty/actions/runs/30372308941), [5](https://github.com/ghostty-org/ghostty/actions/runs/30370584052), [6](https://github.com/ghostty-org/ghostty/actions/runs/30325837845)  
Summary: 6 runs • 14 commits • 7 authors

### Changes

- [`232d40c`](https://github.com/ghostty-org/ghostty/commit/232d40c062e2fb6fedc24276843afae7a315a664) Update VOUCHED list ([#13499](https://github.com/ghostty-org/ghostty/issues/13499)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/13498#issuecomment-5109104876)
  from @mitchellh.
  
  Vouch: @vegerot
  ```
- [`7bea975`](https://github.com/ghostty-org/ghostty/commit/7bea975bd34f8da977674246b36ae80c6df57d09) Update VOUCHED list ([#13497](https://github.com/ghostty-org/ghostty/issues/13497)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13458#discussioncomment-17817388)
  from @jcollie.
  
  Vouch: @RoniJacobson
  ```
- [`2f3814c`](https://github.com/ghostty-org/ghostty/commit/2f3814ca5e6cfcbd504ff86b8120f7e6b7266f56) gtk: honor suspended window state ([@rockorager](https://github.com/rockorager))
  ```text
  GTK exposes the Wayland xdg_toplevel suspended state when the
  compositor knows a window is not visible. Ghostty previously only used
  widget map state, so it could continue rendering a mapped surface on an
  inactive workspace or behind other windows.
  
  Combine the mapped and suspended states for surface occlusion and update
  all displayed surfaces whenever the toplevel suspension state changes.
  
  Amp-Thread-ID: https://ampcode.com/threads/T-019fa965-aa5f-7099-85b4-a9679d2c8bd3
  ```
- [`6c8c079`](https://github.com/ghostty-org/ghostty/commit/6c8c07981d7b4d7c6509323ffb1fe19f45e8af1c) terminal: add visibility reports ([@rockorager](https://github.com/rockorager))
  ```text
  Applications cannot infer whether an unfocused terminal remains visible, so
  focus reports are insufficient for avoiding expensive rendering while a
  view is hidden.
  
  Implement private mode 2033 and the visibility query/report sequences.
  Track conservative per-surface visibility, report every effective change
  while enabled, and always answer explicit queries and mode enables. Keep
  view visibility across terminal resets because it is owned by the host,
  not terminal state.
  
  Amp-Thread-ID: https://ampcode.com/threads/T-019fa965-aa5f-7099-85b4-a9679d2c8bd3
  ```
- [`03eaa01`](https://github.com/ghostty-org/ghostty/commit/03eaa01d484b8c6a098bc94c948e474f33879677) terminal: add visibility reports with GTK suspension tracking ([#13494](https://github.com/ghostty-org/ghostty/issues/13494)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Summary
  
  Applications cannot reliably determine whether an unfocused terminal is
  still
  visible, so focus reports alone are insufficient for avoiding
  unnecessary
  rendering.
  
  This adds terminal visibility reporting by:
  
  - implementing private mode 2033
  - supporting `CSI ? 998 n` visibility queries and `CSI ? 999 ; Ps n`
  responses
  - reporting effective visibility changes while mode 2033 is enabled
  - preserving host-owned visibility state across terminal resets
  - treating unknown visibility conservatively as potentially visible
  
  On GTK 4.12 and newer, surface visibility now combines widget mapping
  with the
  toplevel `suspended` state. This allows Ghostty to recognize windows
  hidden on
  another workspace or otherwise known by the compositor to be
  non-visible.
  Older GTK versions retain the existing conservative behavior.
  
  ## Testing
  
  Added coverage for:
  
  - mode 2033 support and enable/disable behavior
  - explicit visibility queries
  - immediate reports when enabling the mode
  - visible and non-visible responses
  - visibility persistence across terminal resets
  - suppression of visibility queries in read-only mode
  
  ## AI disclosure
  
  Amp assisted with the implementation, tests, commit messages, and this
  pull
  request description. I reviewed the resulting changes and understand how
  they
  interact with the terminal, termio, surface, and GTK visibility paths.
  
  Implements: #13451
  Reference: https://rockorager.dev/misc/visibility-reports/
  ```
- [`07f6c6b`](https://github.com/ghostty-org/ghostty/commit/07f6c6bb07afe0f1d44e5b05fc50b543b6ee878c) mirror deps ([@mitchellh](https://github.com/mitchellh))
- [`4133c6e`](https://github.com/ghostty-org/ghostty/commit/4133c6e48c4b99d19f5885478a19db4868994d07) mirror deps ([#13496](https://github.com/ghostty-org/ghostty/issues/13496)) ([@mitchellh](https://github.com/mitchellh))
- [`95befb3`](https://github.com/ghostty-org/ghostty/commit/95befb33775a4d292732b5d2605d3e95dec05c81) Update VOUCHED list ([#13495](https://github.com/ghostty-org/ghostty/issues/13495)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13491#discussioncomment-17814823)
  from @tristan957.
  
  Vouch: @ruseel
  ```
- [`d716955`](https://github.com/ghostty-org/ghostty/commit/d71695550d4f4aba8b28ce700eeb4b95365ca0e9) config: update info about global keybinds on Linux ([@pluiedev](https://github.com/pluiedev))
- [`d320cd7`](https://github.com/ghostty-org/ghostty/commit/d320cd7df28e4abf6483e021402c65f2ca3f53a2) cli: fix list-themes preview lifecycle ([@jparise](https://github.com/jparise))
  ```text
  Start the vaxis event loop so the theme preview can receive terminal
  input, and retain its environment map for as long as vaxis may access
  it.
  ```
- [`74f45b3`](https://github.com/ghostty-org/ghostty/commit/74f45b321982546e182885a06051c2aab62ce01d) config: update info about global keybinds on Linux ([#13492](https://github.com/ghostty-org/ghostty/issues/13492)) ([@mitchellh](https://github.com/mitchellh))
- [`6e21f41`](https://github.com/ghostty-org/ghostty/commit/6e21f41c0cc6bd09b19e0cc6b8267c7c29ac6159) cli: fix list-themes preview lifecycle ([#13466](https://github.com/ghostty-org/ghostty/issues/13466)) ([@jcollie](https://github.com/jcollie))
  ```text
  Start the vaxis event loop so the theme preview can receive terminal
  input, and retain its environment map for as long as vaxis may access
  it.
  ```
- [`4a22eed`](https://github.com/ghostty-org/ghostty/commit/4a22eed6d9e054fc162a1fb8d4b2899f144da174) renderer/metal: fix 2x sizeof over-allocation in Buffer.sync ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  Buffer.sync and Buffer.syncFromArrayLists computed the new buffer size
  in bytes (req_bytes * 2) and then multiplied by @sizeOf(T) again when
  passing it to newBufferWithLength:, allocating data.len * sizeOf(T)^2 * 2
  bytes. For the 32-byte CellText buffers this is a 64x over-allocation
  and for the 4-byte CellBg buffers 8x, per swap-chain frame (e.g. ~9.4MB
  instead of ~300KB per frame for a full 120x40 screen of text).
  
  Match the OpenGL buffer implementation: track the new length in units
  of T and multiply by @sizeOf(T) exactly once.
  ```
- [`a60cd15`](https://github.com/ghostty-org/ghostty/commit/a60cd15bb5a197d8e2596e86442031cbece06bcc) renderer/metal: fix 2x sizeof over-allocation in Buffer.sync ([#13490](https://github.com/ghostty-org/ghostty/issues/13490)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Seems to me the grow path in `Buffer.sync` (and `syncFromArrayLists`)
  multiplies by `@sizeOf(T)` twice: `req_bytes` is already a byte count,
  it gets doubled into size, and then the `newBufferWithLength:` call does
  `size * @sizeOf(T)` on top of that. So every reallocation ends up being
  `data.len` × `@sizeOf(T)`^2 × 2 bytes instead of the intended `data.len`
  × `@sizeOf(T)` × 2.
  
  The OpenGL version of this same helper does it what seems to be the
  intended way, so this looks like a mixup rather than a deliberate safety
  margin.
  
  This makes the Metal implementation match the OpenGL one: track the new
  length in units of T (which also fixes self.len going stale after a
  grow. It's documented as the allocated element count but was never
  updated here)
  ```

