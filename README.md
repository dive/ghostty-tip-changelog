> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: July 5, 2026 at 02:38 UTC.

## July 5, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/28725807699)  
Summary: 1 runs • 2 commits • 2 authors

### Changes

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

## June 30, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/28454269522)  
Summary: 1 runs • 2 commits • 2 authors

### Changes

- [`5d47602`](https://github.com/ghostty-org/ghostty/commit/5d476024b4e9960802dd5772aa5f77bab5df2a76) build(deps): bump namespacelabs/nscloud-cache-action from 1.4.3 to 1.5.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [namespacelabs/nscloud-cache-action](https://github.com/namespacelabs/nscloud-cache-action) from 1.4.3 to 1.5.0.
  - [Release notes](https://github.com/namespacelabs/nscloud-cache-action/releases)
  - [Commits](https://github.com/namespacelabs/nscloud-cache-action/compare/15799a6b54e5765f85b2aac25b3f0df43ed571c0...d6b68aa38adace8976c09629021052d57bb1ce9c)
  
  ---
  updated-dependencies:
  - dependency-name: namespacelabs/nscloud-cache-action
    dependency-version: 1.5.0
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`0a50617`](https://github.com/ghostty-org/ghostty/commit/0a5061743d608a1b0349a3305a4136ff67600921) build(deps): bump namespacelabs/nscloud-cache-action from 1.4.3 to 1.5.0 ([#13120](https://github.com/ghostty-org/ghostty/issues/13120)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [namespacelabs/nscloud-cache-action](https://github.com/namespacelabs/nscloud-cache-action)
  from 1.4.3 to 1.5.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/namespacelabs/nscloud-cache-action/releases">namespacelabs/nscloud-cache-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v1.5.0</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>Bump pnpm/action-setup from 5.0.0 to 6.0.3 in the
  major-actions-dependencies group across 1 directory by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/127">namespacelabs/nscloud-cache-action#127</a></li>
  <li>Bump the minor-npm-dependencies group across 1 directory with 8
  updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/130">namespacelabs/nscloud-cache-action#130</a></li>
  <li>ci: add --verbose to cargo invocations by <a
  href="https://github.com/annervisser"><code>@​annervisser</code></a> in
  <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/117">namespacelabs/nscloud-cache-action#117</a></li>
  <li>Bump the minor-actions-dependencies group with 5 updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/133">namespacelabs/nscloud-cache-action#133</a></li>
  <li>Bump eslint-plugin-n from 17.24.0 to 18.0.1 by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/132">namespacelabs/nscloud-cache-action#132</a></li>
  <li>fix(ci): pin astral-sh/setup-uv to a valid v7 SHA by <a
  href="https://github.com/rcrowe"><code>@​rcrowe</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/134">namespacelabs/nscloud-cache-action#134</a></li>
  <li>ci: matrix pnpm versions to cover v11 by <a
  href="https://github.com/rcrowe"><code>@​rcrowe</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/131">namespacelabs/nscloud-cache-action#131</a></li>
  <li>Bump the major-actions-dependencies group across 1 directory with 2
  updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/142">namespacelabs/nscloud-cache-action#142</a></li>
  <li>Bump the minor-actions-dependencies group across 1 directory with 7
  updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/145">namespacelabs/nscloud-cache-action#145</a></li>
  <li>Bump the minor-npm-dependencies group across 1 directory with 9
  updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/144">namespacelabs/nscloud-cache-action#144</a></li>
  <li>Pass spacectl binPath explicitly instead of relying on PATH by <a
  href="https://github.com/rcrowe"><code>@​rcrowe</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/146">namespacelabs/nscloud-cache-action#146</a></li>
  <li>ci: add tuist cache mode test by <a
  href="https://github.com/rcrowe"><code>@​rcrowe</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/147">namespacelabs/nscloud-cache-action#147</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/namespacelabs/nscloud-cache-action/compare/v1...v1.5.0">https://github.com/namespacelabs/nscloud-cache-action/compare/v1...v1.5.0</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/d6b68aa38adace8976c09629021052d57bb1ce9c"><code>d6b68aa</code></a>
  ci: add tuist cache mode test (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/147">#147</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/aee11c4fe2689420e2ba4128c27a6e297217997c"><code>aee11c4</code></a>
  Pass spacectl binPath explicitly instead of relying on PATH (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/146">#146</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/4cfea58f960c4e6cbab9f11ce754c4933274642d"><code>4cfea58</code></a>
  Bump the minor-npm-dependencies group across 1 directory with 9 updates
  (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/144">#144</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/2d59ae229313b90908155bbad0758681ad61a0d8"><code>2d59ae2</code></a>
  Bump the minor-actions-dependencies group across 1 directory with 7
  updates (...</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/18c2caf2ae15a55cd922b6430072bf4dcb42653c"><code>18c2caf</code></a>
  Bump the major-actions-dependencies group across 1 directory with 2
  updates (...</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/709f7233c082f4e6834932395fe47810bc3bbc52"><code>709f723</code></a>
  ci: matrix pnpm versions to cover v11 (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/131">#131</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/34b9206dd6befcd25156541c21ecae4dd706db56"><code>34b9206</code></a>
  Bump eslint-plugin-n from 17.24.0 to 18.0.1 (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/132">#132</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/8004c8e3d292e880d4d2dd8b79e96a531b6466be"><code>8004c8e</code></a>
  fix(ci): pin astral-sh/setup-uv to valid v7.6.0 SHA (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/134">#134</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/0a5f069ee9873caaecdd04aa15a9b358c16b35bc"><code>0a5f069</code></a>
  Bump the minor-actions-dependencies group with 5 updates (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/133">#133</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/064bb70e4ad00eaf0b1384a443a76315612db876"><code>064bb70</code></a>
  ci: add --verbose to cargo invocations (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/117">#117</a>)</li>
  <li>Additional commits viewable in <a
  href="https://github.com/namespacelabs/nscloud-cache-action/compare/15799a6b54e5765f85b2aac25b3f0df43ed571c0...d6b68aa38adace8976c09629021052d57bb1ce9c">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=namespacelabs/nscloud-cache-action&package-manager=github_actions&previous-version=1.4.3&new-version=1.5.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## June 29, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/28395795571)  
Summary: 1 runs • 1 commits • 1 authors

### Changes

- [`28f9367`](https://github.com/ghostty-org/ghostty/commit/28f9367bee11ad42f40f8aa589eb8c6db62d34be) Update VOUCHED list ([#13119](https://github.com/ghostty-org/ghostty/issues/13119)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13118#discussioncomment-17475451)
  from @mitchellh.
  
  Vouch: @quinnypig
  ```

