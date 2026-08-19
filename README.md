> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: August 19, 2026 at 15:25 UTC.

## August 19, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/32205120526)  
Summary: 1 runs • 2 commits • 2 authors

### Changes

- [`bed20eb`](https://github.com/ghostty-org/ghostty/commit/bed20eb36453c61c6aff76bdfda0c15235b8e513) terminal: clear tabstop bit on unset instead of toggling ([@fornwall](https://github.com/fornwall))
  ```text
  Tabstops.unset used XOR, so unsetting a column without a tabstop set
  one instead. This made TBC (CSI 0 g) and CTC (CSI 2 W) create a
  tabstop at the cursor column when none existed.
  ```
- [`4c6215b`](https://github.com/ghostty-org/ghostty/commit/4c6215bb8ee186b5c829457a9a9a9c936f2337bf) terminal: clear tabstop bit on unset instead of toggling ([#13900](https://github.com/ghostty-org/ghostty/issues/13900)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Make `Tabstops.unset` (backing [Tab Clear
  (TBC)](https://ghostty.org/docs/vt/csi/tbc) with `n=0`) not set a tab
  stop when clearing a column that has no tab stop.
  ```

## August 18, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/32176127114), [2](https://github.com/ghostty-org/ghostty/actions/runs/32172263374), [3](https://github.com/ghostty-org/ghostty/actions/runs/32169188975), [4](https://github.com/ghostty-org/ghostty/actions/runs/32168669864), [5](https://github.com/ghostty-org/ghostty/actions/runs/32160637749), [6](https://github.com/ghostty-org/ghostty/actions/runs/32145015115)  
Summary: 6 runs • 23 commits • 2 authors

### Changes

- [`cfc5a96`](https://github.com/ghostty-org/ghostty/commit/cfc5a96501d72d0c43a73a9ed2f74c6381ba046c) terminal/kitty: validate graphics query image data ([@mitchellh](https://github.com/mitchellh))
  ```text
  Graphics query commands previously initialized their loading state but
  returned success before completing the image load.
  
  This allowed truncated, malformed, or otherwise invalid image data to
  return OK, giving capability probes a false positive.
  
  Complete and validate queried images through the normal load path, then
  discard the result without modifying image storage. Add coverage for
  invalid data and preserving an existing image with the queried ID.
  ```
- [`86d94f1`](https://github.com/ghostty-org/ghostty/commit/86d94f150a2c3a8e83c4dcab004e1a89af07b1c6) terminal/kitty: preserve chunked response identifiers ([@mitchellh](https://github.com/mitchellh))
  ```text
  Chunked image responses used the final command even though only the
  initial chunk carries the image and placement identifiers. Successful
  replies lost image numbers and placement IDs. Final validation errors
  could also be suppressed entirely.
  
  Save the initial response identifiers with the in-progress image and use
  them when the final chunk completes. Continue replacing the response ID
  with the generated image ID after a successful load. Cover successful
  image-number replies and invalid final payloads with unit tests.
  ```
- [`306a169`](https://github.com/ghostty-org/ghostty/commit/306a169033cd945a5bcd8b5c31fdeae218006648) terminal/kitty: preserve data on unmatched delete ([@mitchellh](https://github.com/mitchellh))
  ```text
  Make uppercase Kitty graphics deletes with a nonzero placement ID
  leave the image intact when the named placement does not exist.
  
  Previously, d=I,i=...,p=... could free unreferenced image data after
  matching no placement. A later put then failed with ENOENT, diverging
  from the protocol and Kitty.
  ```
- [`72b6cd7`](https://github.com/ghostty-org/ghostty/commit/72b6cd71247086eaa8f93edcc49d6d689045b715) terminal/kitty: validate graphics query image data ([#13896](https://github.com/ghostty-org/ghostty/issues/13896)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Graphics query commands previously initialized their loading state but
  returned success before completing the image load.
  
  This allowed truncated, malformed, or otherwise invalid image data to
  return OK, giving capability probes a false positive.
  
  Complete and validate queried images through the normal load path, then
  discard the result without modifying image storage. Add coverage for
  invalid data and preserving an existing image with the queried ID.
  ```
- [`fe12e30`](https://github.com/ghostty-org/ghostty/commit/fe12e30b3468b7afb92744f96af33f4ce484f4a9) terminal/kitty: preserve chunked response identifiers ([#13897](https://github.com/ghostty-org/ghostty/issues/13897)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Chunked image responses used the final command even though only the
  initial chunk carries the image and placement identifiers. Successful
  replies lost image numbers and placement IDs. Final validation errors
  could also be suppressed entirely.
  
  Save the initial response identifiers with the in-progress image and use
  them when the final chunk completes. Continue replacing the response ID
  with the generated image ID after a successful load. Cover successful
  image-number replies and invalid final payloads with unit tests.
  ```
- [`7f62fe7`](https://github.com/ghostty-org/ghostty/commit/7f62fe70a288c5d35ebd3097e75c46017950bcc7) terminal/kitty: preserve data on unmatched delete ([#13898](https://github.com/ghostty-org/ghostty/issues/13898)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Make uppercase Kitty graphics deletes with a nonzero placement ID leave
  the image intact when the named placement does not exist.
  
  Previously, d=I,i=...,p=... could free unreferenced image data after
  matching no placement. A later put then failed with ENOENT, diverging
  from the protocol and Kitty.
  ```
- [`f8b40a0`](https://github.com/ghostty-org/ghostty/commit/f8b40a02356f5ed945d4c2fa981394776186228b) terminal/kitty: fix various graphics deletion mismatches with spec ([@mitchellh](https://github.com/mitchellh))
  ```text
  - Limit d=a/A to non-virtual placements that intersect the active screen.
  - Keep unrelated unplaced image data when processing d=A.
  - Make d=R delete matching unused images even when they have no
    placements, and default an omitted x bound to zero.
  - Give ED2 a separate clear path that preserves scrollback references
    while reclaiming every unreferenced image.
  
  References:
  - Spec:
    https://sw.kovidgoyal.net/kitty/graphics-protocol/#deleting-images
  - Delete reference implementation:
    https://github.com/kovidgoyal/kitty/blob/0ecb10d158943e971e5254c554c2a58f1fcc79fe/kitty/graphics.c#L2114-L2363
  - ED2 reference implementation:
    https://github.com/kovidgoyal/kitty/blob/0ecb10d158943e971e5254c554c2a58f1fcc79fe/kitty/screen.c#L2919-L2958
  ```
- [`2ced1e5`](https://github.com/ghostty-org/ghostty/commit/2ced1e5c8e55bdc1cd77c7ecada4d0ef1cb28226) terminal/kitty: fix various graphics deletion mismatches with spec ([#13895](https://github.com/ghostty-org/ghostty/issues/13895)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  - Limit d=a/A to non-virtual placements that intersect the active
  screen.
  - Keep unrelated unplaced image data when processing d=A.
  - Make d=R delete matching unused images even when they have no
  placements, and default an omitted x bound to zero.
  - Give ED2 a separate clear path that preserves scrollback references
  while reclaiming every unreferenced image.
  
  References:
  - Spec:
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#deleting-images
  - Delete reference implementation:
  https://github.com/kovidgoyal/kitty/blob/0ecb10d158943e971e5254c554c2a58f1fcc79fe/kitty/graphics.c#L2114-L2363
  - ED2 reference implementation:
  https://github.com/kovidgoyal/kitty/blob/0ecb10d158943e971e5254c554c2a58f1fcc79fe/kitty/screen.c#L2919-L2958
  ```
- [`e5747cf`](https://github.com/ghostty-org/ghostty/commit/e5747cf0b603e4cad0ab6642c44738c9cfb50fa5) terminal/kitty: abort incomplete graphics loads ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously, delete left partial bytes alive for the next upload, while
  failed or incomplete retransmissions kept stale placements visible.
  
  Abort incomplete chunked image uploads on delete commands and remove an
  existing image and its placements when retransmission of an explicit ID
  begins.
  ```
- [`55dac8f`](https://github.com/ghostty-org/ghostty/commit/55dac8fc47c239c54540fa30f3bea882d359d07f) terminal/kitty: abort incomplete graphics loads ([#13893](https://github.com/ghostty-org/ghostty/issues/13893)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously, delete left partial bytes alive for the next upload, while
  failed or incomplete retransmissions kept stale placements visible.
  
  Abort incomplete chunked image uploads on delete commands and remove an
  existing image and its placements when retransmission of an explicit ID
  begins.
  ```
- [`83145c0`](https://github.com/ghostty-org/ghostty/commit/83145c0a374852b6c1c2b6e7eab94b4db63c10f7) terminal/kitty: reject conflicting image identifiers ([@mitchellh](https://github.com/mitchellh))
  ```text
  Reject Kitty graphics commands that specify both an image ID and an
  image number across every protocol action.
  
  These commands previously produced no wire response for transmissions,
  while put and delete actions could proceed using one identifier and
  mutate terminal state.
  
  Retain the original command identifiers, validate them before action
  dispatch, and preserve them in the EINVAL response. Add regression
  coverage for every action, response encoding, quiet suppression, and
  pre-mutation rejection.
  
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#requesting-image-ids-from-the-terminal
  ```
- [`52190a5`](https://github.com/ghostty-org/ghostty/commit/52190a5d8da4e21e628bb01f12f32da7b06b3a54) terminal/kitty: intersect source rectangles before sizing ([@mitchellh](https://github.com/mitchellh))
  ```text
  Kitty graphics placements previously calculated pixel and grid geometry
  from requested source dimensions before intersecting them with the image.
  The renderer clamped explicit dimensions later but treated omitted
  source dimensions as the full image.
  
  This stretched clipped crops into incorrectly sized destinations and
  exposed inconsistent geometry through storage, rendering, and
  libghostty.
  
  Resolve the source rectangle once against the image bounds and reuse it
  for placement sizing, renderer preparation, and the C API. Add
  regression tests for omitted and explicit dimensions and renderer
  geometry.
  
  Spec: https://sw.kovidgoyal.net/kitty/graphics-protocol/#controlling-displayed-image-layout
  Reference: https://github.com/kovidgoyal/kitty/blob/0ecb10d158943e971e5254c554c2a58f1fcc79fe/kitty/graphics.c#L1225-L1240
  ```
- [`409e682`](https://github.com/ghostty-org/ghostty/commit/409e682c832198be782071c7b6c182c29227d3aa) terminal/kitty: reject conflicting image identifiers ([#13889](https://github.com/ghostty-org/ghostty/issues/13889)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Reject Kitty graphics commands that specify both an image ID and an
  image number across every protocol action.
  
  These commands previously produced no wire response for transmissions,
  while put and delete actions could proceed using one identifier and
  mutate terminal state.
  
  Retain the original command identifiers, validate them before action
  dispatch, and preserve them in the EINVAL response. Add regression
  coverage for every action, response encoding, quiet suppression, and
  pre-mutation rejection.
  
  
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#requesting-image-ids-from-the-terminal
  ```
- [`9848cb1`](https://github.com/ghostty-org/ghostty/commit/9848cb15fae7eb6abfc74d563ff98b24c830900f) terminal/kitty: intersect source rectangles before sizing ([#13890](https://github.com/ghostty-org/ghostty/issues/13890)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Kitty graphics placements previously calculated pixel and grid geometry
  from requested source dimensions before intersecting them with the
  image. The renderer clamped explicit dimensions later but treated
  omitted source dimensions as the full image.
  
  This stretched clipped crops into incorrectly sized destinations and
  exposed inconsistent geometry through storage, rendering, and
  libghostty.
  
  Resolve the source rectangle once against the image bounds and reuse it
  for placement sizing, renderer preparation, and the C API. Add
  regression tests for omitted and explicit dimensions and renderer
  geometry.
  
  Spec:
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#controlling-displayed-image-layout
  Reference:
  https://github.com/kovidgoyal/kitty/blob/0ecb10d158943e971e5254c554c2a58f1fcc79fe/kitty/graphics.c#L1225-L1240
  ```
- [`c5a3c7e`](https://github.com/ghostty-org/ghostty/commit/c5a3c7e2e5b4e39ce59c14cb35c55be971058575) terminal/kitty: constrain placement offsets to cell bounds ([@mitchellh](https://github.com/mitchellh))
  ```text
  Clamp X and Y offsets when a placement is created and normalize them
  again against current cell geometry when sizing and rendering. The
  protocol requires offsets to remain within the first cell and not
  enlarge explicit c/r rectangles:
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#controlling-displayed-image-layout
  
  Previously, explicit placements were sized to the full c/r rectangle
  before the offset was applied. This extended their far edge into
  neighboring cells and let unbounded offsets reach renderer geometry.
  ```
- [`7e5dfa0`](https://github.com/ghostty-org/ghostty/commit/7e5dfa09eb601fedb9bdf5816d02890108ac1f04) terminal/kitty: constrain placement offsets to cell bounds ([#13891](https://github.com/ghostty-org/ghostty/issues/13891)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Clamp X and Y offsets when a placement is created and normalize them
  again against current cell geometry when sizing and rendering. The
  protocol requires offsets to remain within the first cell and not
  enlarge explicit c/r rectangles:
  
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#controlling-displayed-image-layout
  
  Previously, explicit placements were sized to the full c/r rectangle
  before the offset was applied. This extended their far edge into
  neighboring cells and let unbounded offsets reach renderer geometry.
  ```
- [`abd7706`](https://github.com/ghostty-org/ghostty/commit/abd77067def1653692987588913b83c975ab4893) terminal/kitty: graphics `S` value is exact byte, not max ([@mitchellh](https://github.com/mitchellh))
  ```text
  File transmissions with exactly S bytes or trailing file data previously
  failed because appendRemaining reports StreamTooLong when it reaches its
  limit. This broke the protocol's partial-file transmission path.
  
  Use an exact-length allocation and read when S is nonzero, rejecting
  premature EOF and values above the image limit. Preserve the existing
  bounded read-to-EOF behavior for S=0.
  
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#local-client
  ```
- [`364f8e9`](https://github.com/ghostty-org/ghostty/commit/364f8e9ac1e6dd79233e59fd46435c54e2117caf) terminal/kitty: graphics `S` value is exact byte, not max ([#13892](https://github.com/ghostty-org/ghostty/issues/13892)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  File transmissions with exactly S bytes or trailing file data previously
  failed because appendRemaining reports StreamTooLong when it reaches its
  limit. This broke the protocol's partial-file transmission path.
  
  Use an exact-length allocation and read when S is nonzero, rejecting
  premature EOF and values above the image limit. Preserve the existing
  bounded read-to-EOF behavior for S=0.
  
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#local-client
  ```
- [`afb61e1`](https://github.com/ghostty-org/ghostty/commit/afb61e1b6292f56b863ad0fe61bcdbad47392a5e) terminal/kitty: place cursor after tall images properly ([@mitchellh](https://github.com/mitchellh))
  ```text
  Supersedes #13886
  
  This fixes an incompatibility between Ghostty and Kitty 0.47.1+.
  
  Previously, Ghostty handled `C=0` by moving down at most one terminal
  height and then clamping the horizontal destination to the screen. The
  limit protected against an image command requesting billions of rows,
  but it counted ordinary movement to the bottom as well as scrolling.
  
  Kitty defines `C=0` as leaving the cursor after the image and implements
  the movement as rows minus one, plus one row when the image reaches the
  right edge:
  
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#controlling-displayed-image-layout
  https://github.com/kovidgoyal/kitty/blob/0ecb10d158943e971e5254c554c2a58f1fcc79fe/kitty/graphics.c#L1256-L1260
  https://github.com/kovidgoyal/kitty/blob/0ecb10d158943e971e5254c554c2a58f1fcc79fe/kitty/screen.c#L1903-L1915
  
  (Had to view Kitty source to verify what the spec meant)
  
  For example, an eight-row, full-width image in a five-row terminal needs
  four moves to reach the bottom and four more to scroll. The old limit
  allowed only five moves in total, so the next image started four rows
  inside the first one. Clamping the horizontal destination also left the
  cursor at the final column instead of wrapping to column one of the next
  row. Consecutive images could therefore overlap in both directions.
  ```
- [`d4d72f3`](https://github.com/ghostty-org/ghostty/commit/d4d72f3205f7a995fa4578f4b5369937f0b17a18) terminal/kitty: place cursor after tall images properly ([#13887](https://github.com/ghostty-org/ghostty/issues/13887)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Supersedes #13886
  
  This fixes an incompatibility between Ghostty and Kitty 0.47.1+.
  
  Previously, Ghostty handled `C=0` by moving down at most one terminal
  height and then clamping the horizontal destination to the screen. The
  limit protected against an image command requesting billions of rows,
  but it counted ordinary movement to the bottom as well as scrolling.
  
  Kitty defines `C=0` as leaving the cursor after the image and implements
  the movement as rows minus one, plus one row when the image reaches the
  right edge:
  
  
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#controlling-displayed-image-layout
  https://github.com/kovidgoyal/kitty/blob/0ecb10d158943e971e5254c554c2a58f1fcc79fe/kitty/graphics.c#L1256-L1260
  https://github.com/kovidgoyal/kitty/blob/0ecb10d158943e971e5254c554c2a58f1fcc79fe/kitty/screen.c#L1903-L1915
  
  (Had to view Kitty source to verify what the spec meant)
  
  For example, an eight-row, full-width image in a five-row terminal needs
  four moves to reach the bottom and four more to scroll. The old limit
  allowed only five moves in total, so the next image started four rows
  inside the first one. Clamping the horizontal destination also left the
  cursor at the final column instead of wrapping to column one of the next
  row. Consecutive images could therefore overlap in both directions.
  ```
- [`07af461`](https://github.com/ghostty-org/ghostty/commit/07af4612ba17afe13fcba1de8d8a1258bc666a10) terminal: report size when mode 2048 is enabled ([@elias8](https://github.com/elias8))
- [`5b9a77f`](https://github.com/ghostty-org/ghostty/commit/5b9a77f203865e73de885df743afc73af96fba50) terminal: document mode 2048 size reports ([@elias8](https://github.com/elias8))
- [`0a16db3`](https://github.com/ghostty-org/ghostty/commit/0a16db3c686045fe5ac8a58d3c91dc53d108e662) fix(lib-vt): report size when mode 2048 is enabled ([#13885](https://github.com/ghostty-org/ghostty/issues/13885)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Mode 2048 requires terminals to report the current rows, columns, and
  pixel dimensions [when the mode is
  enabled](https://gist.github.com/rockorager/e695fb2924d36b2bcf1fff4a3704bd83#:~:text=When%20first%20enabled%2C%20the%20terminal%20MUST%20send%20a%20report%20of%20the%20current%20size.),
  then report updated geometry after later resizes. The native termio
  stream already queues the initial report, but the terminal stream only
  reported from `resize`, so libghostty consumers that enabled the mode
  after committing geometry received nothing until another resize.
  
  This makes the generic handler match termio by requesting current
  geometry through the existing size callback and writing the encoded
  report through `write_pty` on every enable.
  ```

## August 17, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/32070024528), [2](https://github.com/ghostty-org/ghostty/actions/runs/32065823102), [3](https://github.com/ghostty-org/ghostty/actions/runs/32056946273), [4](https://github.com/ghostty-org/ghostty/actions/runs/32047937055), [5](https://github.com/ghostty-org/ghostty/actions/runs/32034783819), [6](https://github.com/ghostty-org/ghostty/actions/runs/32007079296), [7](https://github.com/ghostty-org/ghostty/actions/runs/31995485081), [8](https://github.com/ghostty-org/ghostty/actions/runs/31992629892), [9](https://github.com/ghostty-org/ghostty/actions/runs/31984667378)  
Summary: 9 runs • 34 commits • 9 authors

### Changes

- [`9be6c2e`](https://github.com/ghostty-org/ghostty/commit/9be6c2ea2870f409f3e73337f3f5ac74db806ba3) libghostty: option to retain continuations on snapshot decode ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a snapshot decoder option that leaves continuation tracking
  enabled on decoded terminals. This lets caller access the continuation
  bytes (if any) that were applied to the terminal.
  
  This lets replay callers export an unfinished parser or UTF-8 sequence
  from the returned terminal.
  
  This defaults to off.
  ```
- [`12967b6`](https://github.com/ghostty-org/ghostty/commit/12967b68f7d46bdbfb2cfffb6768332fb9db68c0) libghostty: option to retain continuations on snapshot decode ([#13878](https://github.com/ghostty-org/ghostty/issues/13878)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a snapshot decoder option that leaves continuation tracking enabled
  on decoded terminals. This lets caller access the continuation bytes (if
  any) that were applied to the terminal.
  
  This lets replay callers export an unfinished parser or UTF-8 sequence
  from the returned terminal.
  
  This defaults to off.
  ```
- [`846d24e`](https://github.com/ghostty-org/ghostty/commit/846d24e12b3bc12c5623cabf311f3e8c13621ea4) libghostty: buffer the writer adapter used by streaming C APIs ([@mitchellh](https://github.com/mitchellh))
  ```text
  The GhosttyWriter adapter was unbuffered, so for streaming writers that
  make small writes like the formatter, it produces a crazy amount of callbacks:
  one styled HTML page invoked the callback ~50,000 times in a benchmark lol.
  
  Change WriterAdapter to have an optional buffer (initBuffered) and use
  a 4 KB buffer for all current callers. Also optimize single byte splats
  to use memset.
  
  Results: that same styled HTML example goes from ~50K callbacks to 124.
  And throughput through the C API also improved across every workload
  I tested (styled and unstyled text in every format).
  ```
- [`56e1f3a`](https://github.com/ghostty-org/ghostty/commit/56e1f3a62e26407e8c020ef5881df3e8584be20f) libghostty: buffer the writer adapter used by streaming C APIs ([#13877](https://github.com/ghostty-org/ghostty/issues/13877)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The GhosttyWriter adapter was unbuffered, so for streaming writers that
  make small writes like the formatter, it produces a crazy amount of
  callbacks: one styled HTML page invoked the callback ~50,000 times in a
  benchmark lol. This has a particularly large impact on callers who are
  supplying callbacks through an expensive FFI interface, like Go.
  
  Change WriterAdapter to have an optional buffer (initBuffered) and use a
  4 KB buffer for all current callers. Also optimize single byte splats to
  use memset.
  
  Results: that same styled HTML example goes from ~50K callbacks to 124.
  And throughput through the C API also improved across every workload I
  tested (styled and unstyled text in every format).
  ```
- [`7c4c7ad`](https://github.com/ghostty-org/ghostty/commit/7c4c7adadc8b080ab168ed0af48319185dcbd2ba) pkg/wuffs: use C-only mirror of wuffs ([@jcollie](https://github.com/jcollie))
  ```text
  This prevents us from pulling in test images that trigger some anti-virus
  scanners. It's also smaller since it only has the necessary bits that we need.
  
  This also updates to the latest release: 0.4.0-alpha.10.
  ```
- [`6cadad0`](https://github.com/ghostty-org/ghostty/commit/6cadad06f468745651a6bb53e64d31cc8fae9e24) termio: preserve UTF-8 in desktop notification truncation ([@dolzenko](https://github.com/dolzenko))
- [`ae6d97e`](https://github.com/ghostty-org/ghostty/commit/ae6d97ea71b8ad4bb0d3837cc807d6ae097d4145) termio: avoid rescanning UTF-8 prefixes ([@dolzenko](https://github.com/dolzenko))
- [`53c6fdb`](https://github.com/ghostty-org/ghostty/commit/53c6fdbe7d53eb8c61f7af5e311d04956c4fe283) apprt: own desktop notification truncation ([@dolzenko](https://github.com/dolzenko))
  ```text
  Make the fixed-size desktop notification payload a named Message type and initialize it through a constructor.
  
  Keeping UTF-8 boundary truncation with the payload owns the buffer capacities and sentinel termination at the message boundary, while stream_handler only forwards the title and body.
  ```
- [`5c952ac`](https://github.com/ghostty-org/ghostty/commit/5c952ac977b30f3e4e01417827d4d7745015f50c) macos: simplify command palette sort keys ([@jparise](https://github.com/jparise))
  ```text
  Store the Comparable ObjectIdentifier directly instead of wrapping the
  only sort key type in AnySortKey.
  
  The expected deterministic ordering of equal terminal command titles is
  also now verified by a unit test.
  ```
- [`997a2af`](https://github.com/ghostty-org/ghostty/commit/997a2aff2afce88cdf5fa7a3d5dca047c0d65254) terminal: preserve pending wrap in VT formatter ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously, formatting a cursor at the right edge emitted CUP, which
  cleared pending wrap. Replayed output then overwrote the edge cell
  instead of wrapping before the next printable character.
  
  When pending wrap is set, move to and reformat the final cell to restore
  the flag through normal VT behavior. Emit cursor pen state afterward and
  cover replay plus pin-map behavior with a regression test.
  ```
- [`0073976`](https://github.com/ghostty-org/ghostty/commit/00739762316a0ad05c7d412705b5f6111bae3288) terminal: preserve pending wrap in VT formatter ([#13876](https://github.com/ghostty-org/ghostty/issues/13876)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously, formatting a cursor at the right edge emitted CUP, which
  cleared pending wrap. Replayed output then overwrote the edge cell
  instead of wrapping before the next printable character.
  
  When pending wrap is set, move to and reformat the final cell to restore
  the flag through normal VT behavior. Emit cursor pen state afterward and
  cover replay plus pin-map behavior with a regression test.
  ```
- [`4816afc`](https://github.com/ghostty-org/ghostty/commit/4816afc74201c4a8170223fb43e7e6fdbaa34a0a) macos: simplify command palette sort keys ([#13872](https://github.com/ghostty-org/ghostty/issues/13872)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Store the Comparable ObjectIdentifier directly instead of wrapping the
  only sort key type in AnySortKey.
  
  The expected deterministic ordering of equal terminal command titles is
  also now verified by a unit test.
  ```
- [`385a378`](https://github.com/ghostty-org/ghostty/commit/385a378fe58425482eb1df8ed614433e06b891de) termio: preserve UTF-8 in desktop notification truncation ([#13811](https://github.com/ghostty-org/ghostty/issues/13811)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Summary
  
  - Prevent desktop notification title and body truncation from producing
  invalid UTF-8.
  - Truncate fixed-size buffers to the longest valid UTF-8 prefix.
  - Add regression tests for multibyte characters at the buffer boundary.
  
  Fixes #13795
  
  ## Testing
  
  - Confirmed the original reproducer produces `[Invalid UTF-8]` with the
  installed Ghostty.
  - Confirmed the patched Ghostty displays a valid, truncated
  notification.
  - Added tests covering both notification title and body truncation.
  
  ## AI Usage Disclosure
  
  I used OpenAI Codex to investigate the root cause, implement the fix and
  regression tests, run validation, and help prepare the issue and PR
  descriptions. I reviewed and understand the submitted change.
  ```
- [`159cf6d`](https://github.com/ghostty-org/ghostty/commit/159cf6d7e7fef0f477d400c3f801b9f02dbcfd19) pkg/wuffs: use C-only mirror of wuffs ([#13789](https://github.com/ghostty-org/ghostty/issues/13789)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This prevents us from pulling in test images that trigger some
  anti-virus scanners. It's also smaller since it only has the necessary
  bits that we need.
  
  This also updates to the latest release: 0.4.0-alpha.10.
  ```
- [`1eceea9`](https://github.com/ghostty-org/ghostty/commit/1eceea92dac457f95858706f946be7d6b21e5885) i18n: Update ko_KR translations ([@dobbylee](https://github.com/dobbylee))
- [`f430905`](https://github.com/ghostty-org/ghostty/commit/f4309055fbb8cfd74bf0559a054e5eb7ddc361d8) macos: don't put 0x7F as text in key event ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13869
  
  We already checked `< 0x20` but missed `0x7F` which causes similar
  problems.
  ```
- [`6c30dc1`](https://github.com/ghostty-org/ghostty/commit/6c30dc1bfff7e22a9198931411ae862a6bb6277b) i18n: Update ko_KR translations ([#13815](https://github.com/ghostty-org/ghostty/issues/13815)) ([@trag1c](https://github.com/trag1c))
  ```text
  Update all missing Korean translations for 1.4.
  
  Part of #13766
  ```
- [`2349e97`](https://github.com/ghostty-org/ghostty/commit/2349e974b866ae4d9a8c5193a885388ddd4f2b4b) inspector: remove obsolete detachable header helper ([@jparise](https://github.com/jparise))
  ```text
  Remove the unused, callback-based detachable header implementation. It
  supported the previous terminal inspector, which has since been deleted
  (fdbe4343c). The current inspector uses DetachableHeader directly.
  ```
- [`d19f8f7`](https://github.com/ghostty-org/ghostty/commit/d19f8f7f9d3204d37fd1c47f9b51f682238a8423) macos: remove unused hosting window helper ([@jparise](https://github.com/jparise))
  ```text
  Remove the unused SwiftUI environment key intended to expose a hosting
  window. Nothing sets or reads the value.
  ```
- [`c8980b8`](https://github.com/ghostty-org/ghostty/commit/c8980b853b5e822509946c7c62188fe549731376) macos: don't put 0x7F as text in key event ([#13871](https://github.com/ghostty-org/ghostty/issues/13871)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13869
  
  We already checked `< 0x20` but missed `0x7F` which causes similar
  problems.
  ```
- [`924c8a9`](https://github.com/ghostty-org/ghostty/commit/924c8a90ded98fb643def9d7b814efa55e590298) libghostty: C api to stream formatter output through a GhosttyWriter ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add `ghostty_formatter_format` which uses a streaming GhosttyWriter
  type to write. Update the example to show this.
  ```
- [`0baa0fd`](https://github.com/ghostty-org/ghostty/commit/0baa0fd545365d388922d37370c4da2412aa4ace) inspector: remove obsolete detachable header helper ([#13874](https://github.com/ghostty-org/ghostty/issues/13874)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Remove the unused, callback-based detachable header implementation. It
  supported the previous terminal inspector, which has since been deleted
  (fdbe4343c). The current inspector uses DetachableHeader directly.
  ```
- [`faaf07e`](https://github.com/ghostty-org/ghostty/commit/faaf07e7c001e24e0bd725cc1bb3cb899815d53b) macos: remove unused hosting window helper ([#13873](https://github.com/ghostty-org/ghostty/issues/13873)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Remove the unused SwiftUI environment key intended to expose a hosting
  window. Nothing sets or reads the value.
  ```
- [`ee57b94`](https://github.com/ghostty-org/ghostty/commit/ee57b94170ab5261315cb9345eb67663e8d1908c) libghostty: C api to stream formatter output through a GhosttyWriter ([#13875](https://github.com/ghostty-org/ghostty/issues/13875)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add `ghostty_formatter_format` which uses a streaming GhosttyWriter type
  to write. Update the example to show this.
  ```
- [`3924a32`](https://github.com/ghostty-org/ghostty/commit/3924a3255686b2b646d2ee8730ad5528f4542a26) Update VOUCHED list ([#13870](https://github.com/ghostty-org/ghostty/issues/13870)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13838#discussioncomment-18052745)
  from @mitchellh.
  
  Vouch: @basteez
  ```
- [`e2662d7`](https://github.com/ghostty-org/ghostty/commit/e2662d7b63d4aee02f31164c96c180ebed8ddf0b) i18n: translate v1.4 command palette and remaining strings (be) ([@iweuhi2kjrnkw](https://github.com/iweuhi2kjrnkw))
- [`820ed68`](https://github.com/ghostty-org/ghostty/commit/820ed688efa5b914c2779449f260d369caca0b2c) i18n(be): fix translation issues per review ([@iweuhi2kjrnkw](https://github.com/iweuhi2kjrnkw))
  ```text
  - Drop redundant 'было' copula with short-form participles (lines 1767, 1769)
  - Use short predicative form 'недаступна' (line 1780)
  - 'у двух фарматах:' instead of dash-construction (line 156)
  - 'Аднавіць' instead of 'Паўтарыць' for Redo (semantic pair with Undo)
  - Fix 'у' → 'ў' after 'ANSI' (7 places)
  - Align label/description wording for Split Zoom, Read-Only, Float on Top, Secure Input
  - 'усе акны' instead of 'усе вокны' (consistent with 'акно')
  - 'калі яна ёсць' instead of 'даступная' (if present ≠ available)
  - Infinitive 'Дадаць' instead of imperative 'Дадайце'
  ```
- [`b97b17f`](https://github.com/ghostty-org/ghostty/commit/b97b17f06b1ffd694f80edd3df5dd2134a0bcb9e) i18n: translate v1.4 strings (be) ([#13771](https://github.com/ghostty-org/ghostty/issues/13771)) ([@trag1c](https://github.com/trag1c))
  ```text
  Continues the Belarusian (`be`) translation for v1.4 per #13766.
  Translates the remaining 181 strings (mostly the newly-localized command
  palette), bringing `be` to 253/253.
  ```
- [`492c260`](https://github.com/ghostty-org/ghostty/commit/492c26067c9f342f46507ade392cfad2e1400360) libghostty: use custom memory pool for Wasm ([@mitchellh](https://github.com/mitchellh))
  ```text
  A custom memory pool for Wasm that grows by exactly one item size per
  growth and shares the pool across the entire Wasm-module instead of
  per-terminal.
  
  Some background on why `std.heap.MemoryPool` is considered harmful for
  WebAssembly:
  
  First, the std.heap.MemoryPool grows 1.5x at each growth point. The backing
  allocator for that is usually a GPA which is the BrkAllocator for wasm.
  This grows by power-of-two big-allocation slots. If you pair these together
  you get a massive permanent linear memory growth. On non-wasm targets,
  this doesn't matter because these are virtual memory mappings that don't
  cost physical memory, but wasm doesn't work that way.
  
  Second, we were using one pool per terminal. On wasm, this meant that
  we paid for the free list N times. On non-wasm, this makes sense because
  the synchronization overhead has so far been measurable enough under
  load to be prohibitive (although, I'm still skeptical about this and want
  to look into it). On wasm, we build single-threaded modules, so we can use
  a global free list without any extra overhead.
  
  ## Benchmarks
  
  80x24 terminal with 1000-line scrollack processing 16MB of plain ASCII.
  
  | Scenario                        |    Before |     After |
  | ------------------------------- | --------: | --------: |
  | Fresh instance                  |  0.56 MiB |  0.56 MiB |
  | First `terminal_new` (delta)    | +3.44 MiB | +0.88 MiB |
  | One filled terminal (total)     |  4.00 MiB |  1.88 MiB |
  | Each additional filled terminal | +3.00 MiB | +0.44 MiB |
  | 5 filled terminals (total)      | 16.00 MiB |  4.06 MiB |
  
  Throughput numbers are unchanged on wasm and native (to be expected in
  the latter because this is all gated on wasm).
  ```
- [`e9db8d2`](https://github.com/ghostty-org/ghostty/commit/e9db8d2b0b827be035ab75658ea9faf4f0f56d3f) libghostty: use custom memory pool for Wasm, reduce terminal memory by ~75% ([#13865](https://github.com/ghostty-org/ghostty/issues/13865)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A custom memory pool for Wasm that grows by exactly one item size per
  growth and shares the pool across the entire Wasm-module instead of
  per-terminal.
  
  Some background on why `std.heap.MemoryPool` is considered harmful for
  WebAssembly:
  
  First, the std.heap.MemoryPool grows 1.5x at each growth point. The
  backing allocator for that is usually a GPA which is the BrkAllocator
  for wasm. This grows by power-of-two big-allocation slots. If you pair
  these together you get a massive permanent linear memory growth.
  
  On non-wasm targets, the memory growth doesn't matter because these are
  virtual memory mappings that don't cost physical memory, but wasm
  doesn't work that way. Also on native targets, the syscalls to allocate
  memory are very expensive (relatively), so it makes sense to allocate
  large virtual memory chunks and avoid them. Again, wasm doesn't work
  this way.
  
  Second, we were using one pool per terminal. On wasm, this meant that we
  paid for the free list N times. On non-wasm, this makes sense because
  the synchronization overhead has so far been measurable enough under
  load to be prohibitive (although, I'm still skeptical about this and
  want to look into it). On wasm, we build single-threaded modules, so we
  can use a global free list without any extra overhead.
  
  ## Benchmarks
  
  80x24 terminal with 1000-line scrollack processing 16MB of plain ASCII.
  
  | Scenario                        |    Before |     After |
  | ------------------------------- | --------: | --------: |
  | Fresh instance                  |  0.56 MiB |  0.56 MiB |
  | First `terminal_new` (delta)    | +3.44 MiB | +0.88 MiB |
  | One filled terminal (total)     |  4.00 MiB |  1.88 MiB |
  | Each additional filled terminal | +3.00 MiB | +0.44 MiB |
  | 5 filled terminals (total)      | 16.00 MiB |  4.06 MiB |
  
  Throughput numbers are unchanged on wasm and native (to be expected in
  the latter because this is all gated on
  wasm).
  
  Note I'm still very much optimizing the above numbers! This is just my
  first big win.
  
  **AI usage:** None used except to validate and judge.
  ```
- [`5364e51`](https://github.com/ghostty-org/ghostty/commit/5364e5158f171e4d87fdfa43d0fffebc0c3775fa) libghostty: reduce Wasm stack reservation ([@mitchellh](https://github.com/mitchellh))
  ```text
  Zig default's Wasm stacks to 1MB. Change it to 128 KB instead.
  
  This removes 896 KiB from every Wasm instance's initial linear memory
  reservation. That means that simply _loading_ `ghostty-vt.wasm` is down
  this much.
  
  Through various workload benchmarks of real terminal snapshots,
  artificial worst case full ascii, full styled, full emoji, full mixed,
  etc. workloads, I wasn't able to get a stack to go above 17 KB, so 128 KB
  is VERY generous. Lets start here.
  ```
- [`8d70c5d`](https://github.com/ghostty-org/ghostty/commit/8d70c5dca0346dcba94f8812547ff325e62bc340) libghostty: reduce Wasm stack reservation ([#13864](https://github.com/ghostty-org/ghostty/issues/13864)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Zig default's Wasm stacks to 1MB. Change it to 128 KB instead.
  
  This removes 896 KiB from every Wasm instance's initial linear memory
  reservation. That means that simply _loading_ `ghostty-vt.wasm` is down
  this much.
  
  Through various workload benchmarks of real terminal snapshots,
  artificial worst case full ascii, full styled, full emoji, full mixed,
  etc. workloads, I wasn't able to get a stack to go above 17 KB, so 128
  KB is VERY generous. Lets start here.
  ```
- [`7a96643`](https://github.com/ghostty-org/ghostty/commit/7a966438fcf5b3b209bb754b67155d34ae93b217) build(deps): bump cachix/install-nix-action from 31.11.0 to 31.11.1 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [cachix/install-nix-action](https://github.com/cachix/install-nix-action) from 31.11.0 to 31.11.1.
  - [Release notes](https://github.com/cachix/install-nix-action/releases)
  - [Changelog](https://github.com/cachix/install-nix-action/blob/master/RELEASE.md)
  - [Commits](https://github.com/cachix/install-nix-action/compare/630ae543ea3a38a9a4166f03376c02c50f408342...13d8dd58da0234aa297dedd986986ccb8e7f3e24)
  
  ---
  updated-dependencies:
  - dependency-name: cachix/install-nix-action
    dependency-version: 31.11.1
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`9a770be`](https://github.com/ghostty-org/ghostty/commit/9a770be61c39757cdb1a0d7670b8265100d3b2a6) build(deps): bump cachix/install-nix-action from 31.11.0 to 31.11.1 ([#13863](https://github.com/ghostty-org/ghostty/issues/13863)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [cachix/install-nix-action](https://github.com/cachix/install-nix-action)
  from 31.11.0 to 31.11.1.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/cachix/install-nix-action/releases">cachix/install-nix-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v31.11.1</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>nix: 2.35.1 -&gt; 2.35.2 by <a
  href="https://github.com/github-actions"><code>@​github-actions</code></a>[bot]
  in <a
  href="https://redirect.github.com/cachix/install-nix-action/pull/281">cachix/install-nix-action#281</a>
  Fixes a crash (<a
  href="https://redirect.github.com/NixOS/nix/issues/16005"><code>Assertion
  '!awake.empty()' failed</code></a>) that could abort builds.</li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/cachix/install-nix-action/compare/v31.11.0...v31.11.1">https://github.com/cachix/install-nix-action/compare/v31.11.0...v31.11.1</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/13d8dd58da0234aa297dedd986986ccb8e7f3e24"><code>13d8dd5</code></a>
  fix(ci): skip latest installer on x86_64-darwin</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/875018fe555aee647c21ea81888659240cd8e27b"><code>875018f</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/install-nix-action/issues/281">#281</a>
  from cachix/create-pull-request/patch</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/6624a11f6c07674a3ff71d2431865aecf3587190"><code>6624a11</code></a>
  nix: 2.35.1 -&gt; 2.35.2</li>
  <li>See full diff in <a
  href="https://github.com/cachix/install-nix-action/compare/630ae543ea3a38a9a4166f03376c02c50f408342...13d8dd58da0234aa297dedd986986ccb8e7f3e24">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=cachix/install-nix-action&package-manager=github_actions&previous-version=31.11.0&new-version=31.11.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## August 16, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/31974789508), [2](https://github.com/ghostty-org/ghostty/actions/runs/31971580699), [3](https://github.com/ghostty-org/ghostty/actions/runs/31969954615), [4](https://github.com/ghostty-org/ghostty/actions/runs/31967572084), [5](https://github.com/ghostty-org/ghostty/actions/runs/31952071871), [6](https://github.com/ghostty-org/ghostty/actions/runs/31940439160), [7](https://github.com/ghostty-org/ghostty/actions/runs/31927071035), [8](https://github.com/ghostty-org/ghostty/actions/runs/31921652723)  
Summary: 8 runs • 27 commits • 7 authors

### Changes

- [`bd64703`](https://github.com/ghostty-org/ghostty/commit/bd647035e97da4aadfe1003877ecf64a3a655059) input: don't emit fallback text on key release ([@tsacha](https://github.com/tsacha))
  ```text
  Key events without a kitty entry fall back to writing their UTF-8 text
  directly. On GTK, keys whose unshifted keysym is a dead key or level 5
  latch have no unshifted codepoint and take this path. With event type
  reporting enabled, releases therefore emitted the same text as presses
  and duplicated characters in applications such as Neovim.
  
  Skip the raw text fallback for release events while retaining it for
  presses and repeats. Keep the guard in the shared encoder so release
  events for identified keys still retain the UTF-8 data used to derive
  alternate keys.
  
  Cover releases with and without report-all mode, and verify that repeat
  events continue to emit fallback text.
  ```
- [`29b82dd`](https://github.com/ghostty-org/ghostty/commit/29b82dd80c46de16f5aaa405e51b2148831e2061) config: preserve bytes in hex escapes ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13855
  
  Make the config string parser preserve hexadecimal escapes as bytes.
  Previously all escaped values were encoded as Unicode codepoints.
  ```
- [`f8856a7`](https://github.com/ghostty-org/ghostty/commit/f8856a78a291193fbfab081a894d16fc21f4a42e) config: preserve bytes in hex escapes ([#13862](https://github.com/ghostty-org/ghostty/issues/13862)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13855
  
  Make the config string parser preserve hexadecimal escapes as bytes.
  Previously all escaped values were encoded as Unicode codepoints.
  ```
- [`602497e`](https://github.com/ghostty-org/ghostty/commit/602497e9b96c62b05c4c6418538192ad974e4326) input: skip text fallback for kitty key releases ([#13861](https://github.com/ghostty-org/ghostty/issues/13861)) ([@jcollie](https://github.com/jcollie))
  ```text
  Key events without a kitty entry fall back to writing their UTF-8 text
  directly. On GTK, keys whose unshifted keysym is a dead key or level 5
  latch have no unshifted codepoint and take this path. With event type
  reporting enabled, releases therefore emitted the same text as presses
  and duplicated characters in applications such as Neovim.
  
  Skip the raw text fallback for release events while retaining it for
  presses and repeats. Keep the guard in the shared encoder so release
  events for identified keys still retain the UTF-8 data used to derive
  alternate keys.
  
  Cover releases with and without report-all mode, and verify that repeat
  events continue to emit fallback text.
  
    - https://github.com/ghostty-org/ghostty/discussions/12192
    - https://github.com/ghostty-org/ghostty/discussions/12084
    - https://github.com/ghostty-org/ghostty/discussions/12433
    - https://github.com/ghostty-org/ghostty/discussions/13816
  
  ## Testing
  
    - `zig build test-lib-vt -Dtarget=x86_64-linux-gnu`
    - `zig build -Demit-lib-vt -Dtarget=x86_64-linux-gnu`
    - `zig build`
    - Verified the regression test fails without the release guard
  - Manually tested the GTK backend under Wayland/Sway and X11/XWayland,
  with the GTK simple input context and ibus 1.5.34:
      - Ergo-L `!` and `'`
      - Spanish `[`, `{`, `]`, and `}`
  - Presses, repeats, and both modifier-release orders in `nvim --clean`
      - Dead-key composition and cancellation
      - Unicode hexadecimal input
  - Full kitty keyboard mode with `kitty +kitten show_key -m kitty`,
  including composed text
  
  ## AI disclosure
  
  OpenAI Codex assisted with investigating the reports, reviewing the GTK
  and kitty input paths, extending the regression tests, running
  validation, and drafting this description. I reviewed the final code,
  edited this description, manually performed the tests listed above, and
  understand how the change interacts with the input encoder.
  ```
- [`f748b17`](https://github.com/ghostty-org/ghostty/commit/f748b17e27f5ee089494044179dea1c493ce63cc) feat: expand tildes in config theme path to HOME ([@preiter93](https://github.com/preiter93))
  ````text
  When loading a theme from a path that includes a tilde:
  ```
  theme="~/.cache/wal/colors-ghostty"
  ```
  currently fails with the following error:
  ```
  cannot include path separators unless it is an absolute path
  ```
  
  This PR tries to expand the ~ of the path. If there is no ~
  or expansion fails, it falls back to the unexpanded value.
  ````
- [`c121734`](https://github.com/ghostty-org/ghostty/commit/c1217342958b90ed3a25413c1616dfd2dd8cd1bf) move shell expand of theme from theme.zig to config.zig ([@preiter93](https://github.com/preiter93))
- [`37174c7`](https://github.com/ghostty-org/ghostty/commit/37174c73b0600cc3b2d8579fa7a210086ee3bbed) add helper and expand also if light/dark is specified ([@preiter93](https://github.com/preiter93))
- [`68a2008`](https://github.com/ghostty-org/ghostty/commit/68a2008b340959b2a94f27f37ca98257109f6396) fix: format ([@preiter93](https://github.com/preiter93))
- [`7557944`](https://github.com/ghostty-org/ghostty/commit/7557944b4f1fb9eebe451c636227a04e7a4a2704) feat: expand tildes in config theme path to HOME ([#13840](https://github.com/ghostty-org/ghostty/issues/13840)) ([@jcollie](https://github.com/jcollie))
  ````text
  When loading a theme from a path that includes a tilde:
  ```
  theme="~/.cache/wal/colors-ghostty"
  ```
  ghostty currently fails with the following error:
  ```
  cannot include path separators unless it is an absolute path
  ```
  
  This PR tries to expand the ~ of the path. If there is no ~ or expansion
  fails, it falls back to the unexpanded value.
  ````
- [`a8e9b41`](https://github.com/ghostty-org/ghostty/commit/a8e9b413f13cfeec77efd95c3ba9b4750fcbfada) libghostty: simplify Wasm allocation API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Replace a bunch of type-specific Wasm allocation functions with a generic
  byte allocator and reusable opaque out-parameters for pointers. This
  makes it a lot more ergonomic (relatively) to use the Wasm interface
  and removes a dozen or so exports.
  
  This also updates the `ghostty_type_json` `abi` field with a maximum
  alignment value that host sides can use to keep every allocation aligned
  properly, easily, without hardcoding numbers.
  
  This adds a test to verify this all works as intended and runs in CI.
  ```
- [`3790fb7`](https://github.com/ghostty-org/ghostty/commit/3790fb78fecb3577dee30c40efe1ced3e3f0d9a1) libghostty: simplify Wasm allocation API ([#13860](https://github.com/ghostty-org/ghostty/issues/13860)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Replace a bunch of type-specific Wasm allocation functions with a
  generic byte allocator and reusable opaque out-parameters for pointers.
  This makes it a lot more ergonomic (relatively) to use the Wasm
  interface and removes a dozen or so exports.
  
  This also updates the `ghostty_type_json` `abi` field with a maximum
  alignment value that host sides can use to keep every allocation aligned
  properly, easily, without hardcoding numbers.
  
  This adds a test to verify this all works as intended and runs in CI.
  ```
- [`7b57c0a`](https://github.com/ghostty-org/ghostty/commit/7b57c0a02942beb3217a751e6d26955e3c3c1d72) Update VOUCHED list ([#13859](https://github.com/ghostty-org/ghostty/issues/13859)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13858#discussioncomment-18043290)
  from @jcollie.
  
  Vouch: @tsacha
  ```
- [`9673a22`](https://github.com/ghostty-org/ghostty/commit/9673a22b01317ac6493240694a2451c8287253d1) libghostty: expand ABI type metadata ([@mitchellh](https://github.com/mitchellh))
  ```text
  The type metadata export only described extern struct layouts, leaving embedders to mirror enum values and tagged union relationships.
  
  Describe every public C type in a versioned manifest with target and build metadata. Keep union field renames alongside their source tagged unions so the manifest uses public C names without changing Zig value layouts.
  ```
- [`c755595`](https://github.com/ghostty-org/ghostty/commit/c75559589e41721ab5a3de8e336d8476f4290535) libghostty: add ABI manifest schema ([@mitchellh](https://github.com/mitchellh))
  ```text
  The ABI manifest previously had no machine-readable grammar or test that
  the public export conformed to it.
  
  Define a Draft 2020-12 schema and add a build check that executes
  ghostty_type_json for native and wasm libraries before validation. Run
  both forms in CI and publish the schema with the generated API docs.
  ```
- [`0e8b7be`](https://github.com/ghostty-org/ghostty/commit/0e8b7bea63ccf8b89d15a82bdaf6a9bb3fc8c43d) vt: expose packed cell layout ([@mitchellh](https://github.com/mitchellh))
  ```text
  GhosttyCell was exposed as a raw integer while its manifest entry was only an alias, forcing bulk-read consumers to duplicate the internal cell bit layout.\n\nAdd reflection helpers for packed structs and tagged unions, and keep the C-facing layout metadata next to Cell itself. Extend the ABI manifest and schema with recursive bit descriptors so every content arm, including palette and RGB backgrounds, can be decoded without hardcoded masks.\n\nDocument manifest-driven cell decoding and test the metadata against Zig reflection and real cell values.
  ```
- [`0ba6250`](https://github.com/ghostty-org/ghostty/commit/0ba6250388641f52135414b38c4259aa682c489b) libghostty: `ghostty_type_json` expanded with more metadata, every enum member, packed layouts, etc. ([#13856](https://github.com/ghostty-org/ghostty/issues/13856)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This PR makes `ghostty_type_json` contain more metadata necessary for
  FFI without access to the C header to produce safe, ABI compliant field
  access.
  
  The existing `ghostty_type_json` didn't expose enough information:
  embedders still had to hardcode enum values, tagged union values, and
  packed bit layouts. For wasm this meant copying offsets and masks from
  Zig internals and hoping they didn't drift. This isn't an ABI I want to
  promise.
  
  This also includes a formal JSON schema included in Doxygen docs and
  used in CI to continuously validate our output structure. I'd like to
  expand in the future comparing to actual C headers too.
  
  ## Examples
  
  ### Named References, Arrays
  
  ```json
  "GhosttyRenderStateColors": {
    "kind": "struct",
    "size": 792,
    "align": 8,
    "fields": {
      "background": {
        "offset": 8,
        "size": 3,
        "type": "GhosttyColorRgb"
      },
      "palette": {
        "offset": 18,
        "size": 768,
        "type": "array",
        "elem": "GhosttyColorRgb",
        "count": 256
      }
    }
  }
  ```
  
  ### Pointers
  
  ```json
  "GhosttyCellsView": {
    "kind": "struct",
    "size": 16,
    "align": 8,
    "fields": {
      "ptr": {
        "offset": 0,
        "size": 8,
        "type": "pointer",
        "elem": "GhosttyCell",
        "const": true,
        "nullable": true
      },
      "len": {
        "offset": 8,
        "size": 8,
        "type": "u64"
      }
    }
  }
  ```
  
  ### Enums
  
  ```json
  "GhosttyStyleColorTag": {
    "kind": "enum",
    "size": 4,
    "align": 4,
    "underlying": "i32",
    "prefix": "GHOSTTY_STYLE_COLOR_",
    "values": {
      "NONE": 0,
      "PALETTE": 1,
      "RGB": 2,
      "TAG_MAX_VALUE": 2147483647
    }
  }
  ```
  
  ### Packed Struct
  
  ```json
  "GhosttyCell": {
    "kind": "packed",
    "size": 8,
    "align": 8,
    "underlying": "u64",
    "bits": {
      "content_tag": {
        "lsb": 0,
        "width": 2,
        "type": "GhosttyCellContentTag"
      },
      "content": {
        "lsb": 2,
        "width": 24,
        "kind": "union",
        "tag": "content_tag",
        "arms": {
          "BG_COLOR_RGB": {
            "kind": "packed",
            "width": 24,
            "bits": {
              "r": {"lsb": 0, "width": 8, "type": "u8"},
              "g": {"lsb": 8, "width": 8, "type": "u8"},
              "b": {"lsb": 16, "width": 8, "type": "u8"}
            }
          }
        }
      }
    }
  }
  ```
  ````
- [`aa25679`](https://github.com/ghostty-org/ghostty/commit/aa25679da8c87b47e9b45410435bded87e283031) i18n: update Hebrew translations for v1.4 ([@slsrepo](https://github.com/slsrepo))
- [`d7f782d`](https://github.com/ghostty-org/ghostty/commit/d7f782dbcc4471eb697cce0ce888c83787ca38f0) i18n: update Hebrew translations for v1.4 ([@slsrepo](https://github.com/slsrepo))
- [`7c1d0d4`](https://github.com/ghostty-org/ghostty/commit/7c1d0d414c4bfd976c6ae422f170a4b6249716d5) i18n: update Hebrew translations for v1.4 ([@slsrepo](https://github.com/slsrepo))
  ```text
  Removed translation for opening config file with default editor.
  ```
- [`06b63c4`](https://github.com/ghostty-org/ghostty/commit/06b63c48594ea04d2a68dd8249250d1477722296) i18n: update Hebrew translations for v1.4 ([@slsrepo](https://github.com/slsrepo))
- [`26df373`](https://github.com/ghostty-org/ghostty/commit/26df373ec83fb1cebb4fee0a8394144ae984a9b8) i18n: update Hebrew translations for v1.4 ([#13785](https://github.com/ghostty-org/ghostty/issues/13785)) ([@trag1c](https://github.com/trag1c))
  ```text
  Update the Hebrew translations in po/he.po with the 181 new strings for
  v1.4, as requested in issue #13766 :)
  ```
- [`b4079f0`](https://github.com/ghostty-org/ghostty/commit/b4079f00c8946207e4db8571e3209f2de7ac4a27) libghostty: add render state structured cursor read ([@mitchellh](https://github.com/mitchellh))
  ```text
  A normal renderer would have to call `ghostty_render_state_get`
  _eight times_ to reconstruct the cursor. In languages where FFI is
  expensive (Go, wasm, etc.), this showed up in profiles of every frame.
  
  Add a sized cursor snapshot and expose it. Also expose the existing color
  snapshot through ghostty_render_state_get and remove the older
  dedicated color getter.
  ```
- [`0d37f2d`](https://github.com/ghostty-org/ghostty/commit/0d37f2d34dabd6bc6f7cf094e0d6466186b8c783) libghostty: add dedicated dirty row iteration + clear functions ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add render state C APIs for iterating only rows that require a redraw
  and for marking a completed frame clean in one call.
  
  A one-row update in a 24-row viewport reduces dirty-row discovery from
  50 calls to two, while cleanup becomes one call instead of O(N) of rows.
  
  This lower call count is massive for environments where FFI is expensive
  (Go, wasm).
  
  The dirty next API outputs the viewport y because it jumps, unlike the
  normal sequential next where its trivial for a caller to keep track.
  ```
- [`16c833c`](https://github.com/ghostty-org/ghostty/commit/16c833c5f1ffa9511909199ef1fab389493be1ef) libghostty: add render state structured cursor read ([#13851](https://github.com/ghostty-org/ghostty/issues/13851)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A normal renderer would have to call `ghostty_render_state_get` _eight
  times_ to reconstruct the cursor. In languages where FFI is expensive
  (Go, wasm, etc.), this showed up in profiles of every frame.
  
  Add a sized cursor snapshot and expose it. Also expose the existing
  color snapshot through ghostty_render_state_get and remove the older
  dedicated color getter.
  
  Found during my normal Go/wasm adventures.
  ```
- [`ad6e72d`](https://github.com/ghostty-org/ghostty/commit/ad6e72ddc4e9e259c9b70bff6e2b389e0ce91949) libghostty: add dedicated dirty row iteration + clear functions ([#13852](https://github.com/ghostty-org/ghostty/issues/13852)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add render state C APIs for iterating only rows that require a redraw
  and for marking a completed frame clean in one call.
  
  A one-row update in a 24-row viewport reduces dirty-row discovery from
  50 calls to two, while cleanup becomes one call instead of O(N) of rows.
  
  This lower call count is massive for environments where FFI is expensive
  (Go, wasm).
  
  The dirty next API outputs the viewport y because it jumps, unlike the
  normal sequential next where its trivial for a caller to keep track.
  ```
- [`f2897f3`](https://github.com/ghostty-org/ghostty/commit/f2897f31dec839352302369b3cb8009c4cec180b) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`02436fd`](https://github.com/ghostty-org/ghostty/commit/02436fd4eb0fca179f6d58717e9bc7a0ce106272) Update iTerm2 colorschemes ([#13850](https://github.com/ghostty-org/ghostty/issues/13850)) ([@jcollie](https://github.com/jcollie))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260810-152212-0173c3c
  ```

## August 15, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/31910656085), [2](https://github.com/ghostty-org/ghostty/actions/runs/31894663124), [3](https://github.com/ghostty-org/ghostty/actions/runs/31890031839), [4](https://github.com/ghostty-org/ghostty/actions/runs/31876969328), [5](https://github.com/ghostty-org/ghostty/actions/runs/31868500752), [6](https://github.com/ghostty-org/ghostty/actions/runs/31865684095), [7](https://github.com/ghostty-org/ghostty/actions/runs/31864664855), [8](https://github.com/ghostty-org/ghostty/actions/runs/31862777169)  
Summary: 8 runs • 30 commits • 6 authors

### Changes

- [`ecbeb60`](https://github.com/ghostty-org/ghostty/commit/ecbeb60ca5327186301900ccef208143ff46ef22) macos: send all insertText commits as key events ([@sghng](https://github.com/sghng))
  ```text
  Previously, insertText commits without marked text were delivered via
  sendText, which applies paste semantics and wraps the text in bracketed
  paste when the program enables it. macOS dictation and other input
  methods often commit without marked text, so programs treated dictated
  text as a paste and applied paste-specific handling.
  
  insertText is only invoked by input methods (IME, dictation, emoji
  picker, character viewer); real paste operations use a separate path.
  Send every non-empty commit through the key event path so programs
  interpret input method text as typed input. Typing is unaffected (the
  accumulator path returns earlier) and Cmd+V pastes are unaffected.
  
  The helper is renamed from committedPreeditTextAction to
  committedTextAction since it no longer only handles preedit commits.
  ```
- [`fff9f62`](https://github.com/ghostty-org/ghostty/commit/fff9f62f38cfef56ada5239ea22555b35c1e063c) cli: always install embedded SSH terminfo ([@jparise](https://github.com/jparise))
  ```text
  Remove the remote infocmp short-circuit from +ssh setup. The command
  already sends Ghostty's embedded terminfo source to tic, so accepting
  any existing entry leaves the payload unused and can preserve stale
  data.
  ```
- [`69b9abf`](https://github.com/ghostty-org/ghostty/commit/69b9abf09ebad2b11a6850a28271676f6bfeb108) cli: version SSH terminfo cache entries ([@jparise](https://github.com/jparise))
  ```text
  Derive a version from the encoded Ghostty terminfo and require callers
  to pass it explicitly when reading or writing the SSH cache. Cache
  entries created for older or different payloads no longer suppress a
  required installation.
  ```
- [`36d8e3f`](https://github.com/ghostty-org/ghostty/commit/36d8e3f77779939a4413ddcd72c05ab08aeae57d) terminal/snapshot: slicing-by-16 software CRC32C ([@mitchellh](https://github.com/mitchellh))
  ```text
  The software CRC32C fallback (WebAssembly and any other target without a
  dedicated instruction) was the std byte-at-a-time table walk, which
  profiled at ~65% of snapshot encode and ~70% of decode self-time in V8.
  Replace it with slicing-by-16: sixteen bytes fold per iteration through
  comptime per-position tables, so the serial dependency advances one block
  at a time instead of one byte.
  
  The hardware backends (aarch64 CRC, x86_64 SSE4.2) are unchanged, so
  native is expected to be unaffected; its deltas below are run-to-run
  noise.
  
  Benchmarks: wasm is V8 (node 25), ReleaseFast + wasm-opt -O3, 80x24
  terminal, 2 MiB VT corpus per workload, complete snapshot including
  scrollback, best-of-5. Native is aarch64 macOS, hyperfine mean,
  ghostty-bench +terminal-snapshot --loops=20. "base" is the parent commit.
  
  | wasm      | encode base | encode   | decode base | decode   |
  |-----------|------------:|---------:|------------:|---------:|
  | ascii     |     7.07 ms |  3.43 ms |     6.45 ms |  2.81 ms |
  | styled    |    10.54 ms |  3.14 ms |    14.37 ms |  7.12 ms |
  | truecolor |    15.23 ms |  5.33 ms |    21.76 ms | 12.11 ms |
  | cjk       |    25.41 ms |  5.95 ms |    30.83 ms | 12.04 ms |
  | grapheme  |    27.67 ms | 14.18 ms |    27.00 ms | 13.16 ms |
  
  | native | mode   | base    | this    |
  |--------|--------|--------:|--------:|
  | ascii  | encode | 40.6 ms | 41.7 ms |
  | ascii  | decode | 51.2 ms | 53.2 ms |
  | utf8   | encode | 45.2 ms | 47.2 ms |
  | utf8   | decode | 59.8 ms | 61.6 ms |
  ```
- [`c1a61fd`](https://github.com/ghostty-org/ghostty/commit/c1a61fddda00e907c7e66bd3609d6c558cccd26d) terminal/snapshot: borrow fully buffered record payloads ([@mitchellh](https://github.com/mitchellh))
  ```text
  When the record source already has the complete payload buffered — always
  the case for in-memory snapshots such as ghostty_snapshot_decoder_new_buf
  — the record reader now borrows the payload straight out of the source
  buffer instead of streaming it through the limited and hashing reader
  adapters. Payload decoders parse a fixed reader over the borrowed bytes,
  `finish` validates the CRC with a single bulk update, and the source
  advances only after validation.
  
  The page decoder takes a matching fast path: a fully buffered payload is
  parsed in place, skipping the staging allocation and copy it previously
  made per PAGE record. Streaming sources are unchanged.
  
  This is a modest win on its own; it is also the foundation for later
  commits whose buffered fast paths rely on the payload being contiguous.
  
  Benchmarks (see the first commit in this series for methodology; "prev"
  is the parent commit):
  
  | wasm      | encode prev | encode   | decode prev | decode   |
  |-----------|------------:|---------:|------------:|---------:|
  | ascii     |     3.43 ms |  3.50 ms |     2.81 ms |  2.68 ms |
  | styled    |     3.14 ms |  3.15 ms |     7.12 ms |  7.04 ms |
  | truecolor |     5.33 ms |  5.27 ms |    12.11 ms | 12.04 ms |
  | cjk       |     5.95 ms |  5.92 ms |    12.04 ms | 11.89 ms |
  | grapheme  |    14.18 ms | 14.33 ms |    13.16 ms | 13.14 ms |
  
  | native | mode   | prev    | this    |
  |--------|--------|--------:|--------:|
  | ascii  | encode | 41.7 ms | 41.8 ms |
  | ascii  | decode | 53.2 ms | 52.4 ms |
  | utf8   | encode | 47.2 ms | 47.4 ms |
  | utf8   | decode | 61.6 ms | 61.2 ms |
  ```
- [`973f619`](https://github.com/ghostty-org/ghostty/commit/973f619a2371c50fffb2062bd59a0c5134c783b1) terminal/snapshot: vectorize grid row encoding ([@mitchellh](https://github.com/mitchellh))
  ```text
  Row encoding previously made two scalar passes over every row (a backward
  scan for the encoded cell count and a validation pass accumulating the
  width-selection OR), then wrote a 3-byte header and per-width chunked
  cells through separate writer calls.
  
  Three changes, all bulk-codec only with the portable path unchanged:
  
    - scanRow computes the count and word-OR in @Vector(4, u64) strides.
      Trailing default cells are all-zero words, so the OR over the whole
      row equals the OR over the encoded prefix.
    - The per-cell wide-pair validation loop is skipped entirely when the
      OR carries no wide bits, which is every row of plain text.
    - Rows are emitted with a single reservation in the destination's spare
      buffer capacity (header plus cells, no writer calls), using explicit
      i8x16.shuffle truncation for the 1/2/4-byte cell widths. Zig 0.16
      disables loop auto-vectorization, so the previous "vectorizable"
      truncating loop was actually scalar. Destinations without buffered
      capacity (counting writers, a still-growing scratch) fall through to
      the streaming path.
  
  Benchmarks ("prev" is the parent commit):
  
  | wasm      | encode prev | encode   | decode prev | decode   |
  |-----------|------------:|---------:|------------:|---------:|
  | ascii     |     3.50 ms |  2.09 ms |     2.68 ms |  2.67 ms |
  | styled    |     3.15 ms |  2.23 ms |     7.04 ms |  7.00 ms |
  | truecolor |     5.27 ms |  4.95 ms |    12.04 ms | 11.85 ms |
  | cjk       |     5.92 ms |  6.03 ms |    11.89 ms | 11.67 ms |
  | grapheme  |    14.33 ms | 13.08 ms |    13.14 ms | 13.28 ms |
  
  | native | mode   | prev    | this    |
  |--------|--------|--------:|--------:|
  | ascii  | encode | 41.8 ms | 24.5 ms |
  | ascii  | decode | 52.4 ms | 53.4 ms |
  | utf8   | encode | 47.4 ms | 47.6 ms |
  | utf8   | decode | 61.2 ms | 60.9 ms |
  ```
- [`593762c`](https://github.com/ghostty-org/ghostty/commit/593762cfa11afdd3eaefc9e0bdd9d979d85ab39f) terminal/snapshot: batch grapheme suffix codec ([@mitchellh](https://github.com/mitchellh))
  ```text
  Grapheme suffix encoding made two full passes over the grid (a counting
  pass, then an emit pass) and issued three writer calls per entry plus one
  per codepoint. Every grapheme cell owns exactly one entry in the page's
  grapheme map, so the section count now comes straight from
  page.graphemeCount() with no counting pass, and entries are batched
  through a 4 KB buffer with one writer call per flush. The per-entry size
  check moved into the emit loop; an error still cancels the whole record
  before any of it is emitted, so error behavior is unchanged.
  
  Decoding similarly parsed entry headers and codepoints with one reader
  call per integer. Fully buffered payloads (the common case after the
  borrowed-payload commit) now parse entry headers and codepoint runs
  directly from the buffered bytes, and entries whose target cell cannot
  carry a suffix discard their codepoints in bulk.
  
  Benchmarks ("prev" is the parent commit):
  
  | wasm      | encode prev | encode   | decode prev | decode   |
  |-----------|------------:|---------:|------------:|---------:|
  | ascii     |     2.09 ms |  2.07 ms |     2.67 ms |  2.69 ms |
  | styled    |     2.23 ms |  2.29 ms |     7.00 ms |  7.06 ms |
  | truecolor |     4.95 ms |  4.91 ms |    11.85 ms | 11.99 ms |
  | cjk       |     6.03 ms |  6.14 ms |    11.67 ms | 11.83 ms |
  | grapheme  |    13.08 ms |  8.26 ms |    13.28 ms | 11.18 ms |
  
  | native | mode   | prev    | this    |
  |--------|--------|--------:|--------:|
  | ascii  | encode | 24.5 ms | 24.3 ms |
  | ascii  | decode | 53.4 ms | 50.9 ms |
  | utf8   | encode | 47.6 ms | 41.2 ms |
  | utf8   | decode | 60.9 ms | 59.5 ms |
  ```
- [`2aaad3c`](https://github.com/ghostty-org/ghostty/commit/2aaad3ca99a27d36eff57d6e59e2044005ef2ba4) terminal/snapshot: vectorize grid cell decoding ([@mitchellh](https://github.com/mitchellh))
  ```text
  Decoding one- and two-byte cells widened them to their 8-byte words one
  scalar store at a time. The bulk codec now widens sixteen transported
  bytes per step with byte shuffles against a zero vector, degrading
  width-two surrogate lanes to U+FFFD with a vector select, exactly
  matching the scalar path. Short row tails reprocess the final full
  window with overlapping stores that rewrite identical bytes.
  
  This is a native win: the shuffles lower to NEON and take ascii decode
  from 38.9 ms to 34.0 ms (measured by toggling this path at the tip of
  this series). On wasm, V8 runs the scalar fallback at the same speed as
  the shuffle version — the loop is store-bound either way — so the wasm
  deltas below are flat.
  
  Row decoding also drops per-field packed-struct read-modify-writes in
  favor of one load and one store per row header, and rows that are fully
  default (zero header byte, zero encoded cells) skip all work: decoded
  pages start zeroed, which is exactly the default row and cell state.
  
  Benchmarks ("prev" is the parent commit):
  
  | wasm      | encode prev | encode   | decode prev | decode   |
  |-----------|------------:|---------:|------------:|---------:|
  | ascii     |     2.07 ms |  2.18 ms |     2.69 ms |  2.68 ms |
  | styled    |     2.29 ms |  2.28 ms |     7.06 ms |  6.93 ms |
  | truecolor |     4.91 ms |  4.93 ms |    11.99 ms | 11.91 ms |
  | cjk       |     6.14 ms |  6.11 ms |    11.83 ms | 11.72 ms |
  | grapheme  |     8.26 ms |  8.28 ms |    11.18 ms | 11.38 ms |
  
  | native | mode   | prev    | this    |
  |--------|--------|--------:|--------:|
  | ascii  | encode | 24.3 ms | 24.3 ms |
  | ascii  | decode | 50.9 ms | 46.7 ms |
  | utf8   | encode | 41.2 ms | 41.0 ms |
  | utf8   | decode | 59.5 ms | 59.5 ms |
  ```
- [`7c1014e`](https://github.com/ghostty-org/ghostty/commit/7c1014ef662cd4e9b968b5bac6ca062fa17a3b56) terminal/snapshot: resolve wide pairs in a per-row pass ([@mitchellh](https://github.com/mitchellh))
  ```text
  Cell decoding ran wide-pair normalization inline for every decoded cell:
  two neighbor loads and a switch per cell, even though the overwhelming
  majority of rows contain no wide cells at all. Normalization is defined
  against already-stored predecessors, so running it as an ordered pass
  over the stored row afterward is exactly equivalent to interleaving it.
  
  The word-cell decoders now accumulate the bitwise OR of the row's wire
  words as they apply cells, and the pass is gated on it: rows without
  wide bits are already normalized (every cell narrow), and width-four and
  narrower transports cannot encode wide bits at all, so their rows skip
  the check at comptime. That removes the per-cell neighbor traffic from
  all styled text, which decodes through the four-byte width.
  
  Benchmarks ("prev" is the parent commit):
  
  | wasm      | encode prev | encode   | decode prev | decode   |
  |-----------|------------:|---------:|------------:|---------:|
  | ascii     |     2.18 ms |  2.06 ms |     2.68 ms |  2.70 ms |
  | styled    |     2.28 ms |  2.41 ms |     6.93 ms |  6.56 ms |
  | truecolor |     4.93 ms |  5.02 ms |    11.91 ms | 11.86 ms |
  | cjk       |     6.11 ms |  6.03 ms |    11.72 ms | 11.60 ms |
  | grapheme  |     8.28 ms |  8.36 ms |    11.38 ms | 11.39 ms |
  
  | native | mode   | prev    | this    |
  |--------|--------|--------:|--------:|
  | ascii  | encode | 24.3 ms | 25.6 ms |
  | ascii  | decode | 46.7 ms | 48.1 ms |
  | utf8   | encode | 41.0 ms | 41.7 ms |
  | utf8   | decode | 59.5 ms | 58.5 ms |
  ```
- [`47a5182`](https://github.com/ghostty-org/ghostty/commit/47a5182621e324f3351683ca2cc422562b3ff792) terminal/snapshot: skip remap tables for pages without styles ([@mitchellh](https://github.com/mitchellh))
  ```text
  Decoding a page allocated and zeroed two full remap tables (a 128 KB
  entries array plus an 8 KB seen bitmap each for styles and hyperlinks)
  even when the page declared no table entries at all, which is every page
  of plain scrollback. Empty tables now use a shared `.empty` remap that
  allocates nothing; `get` reads it as all-unmapped through a length check.
  Pages that do declare entries are unchanged.
  
  (Leaving the entries array unzeroed behind a seen-bitmap-gated `get` was
  also tried and measured no better than the plain memset, so the table
  keeps its simple zero-means-unmapped representation.)
  
  Benchmarks ("prev" is the parent commit):
  
  | wasm      | encode prev | encode   | decode prev | decode   |
  |-----------|------------:|---------:|------------:|---------:|
  | ascii     |     2.06 ms |  2.13 ms |     2.70 ms |  2.54 ms |
  | styled    |     2.41 ms |  2.29 ms |     6.56 ms |  6.75 ms |
  | truecolor |     5.02 ms |  4.95 ms |    11.86 ms | 12.05 ms |
  | cjk       |     6.03 ms |  6.23 ms |    11.60 ms | 11.39 ms |
  | grapheme  |     8.36 ms |  8.72 ms |    11.39 ms | 11.27 ms |
  
  | native | mode   | prev    | this    |
  |--------|--------|--------:|--------:|
  | ascii  | encode | 25.6 ms | 24.4 ms |
  | ascii  | decode | 48.1 ms | 45.1 ms |
  | utf8   | encode | 41.7 ms | 41.9 ms |
  | utf8   | decode | 58.5 ms | 58.6 ms |
  ```
- [`1359973`](https://github.com/ghostty-org/ghostty/commit/1359973aefb37a9beaa2ec3e8f79df78290ea6f5) terminal/snapshot: single-pass style entry codec ([@mitchellh](https://github.com/mitchellh))
  ```text
  Style entries went through roughly five writer or reader vtable calls
  each: encode wrote three 4-byte colors and two u16s separately, and
  decode read 16 bytes into a stack buffer only to re-parse it through a
  nested fixed reader, one small read per field. Style-heavy pages carry
  hundreds of entries per page, so encode now assembles each entry in a
  16-byte buffer with a single write, and decode parses the fixed-size
  entry directly from a byte array. Entries additionally parse straight
  from the buffered payload (ID and value together) when it is contiguous.
  
  Inserting a decoded style also hashed twice: an explicit `lookup` before
  `add`, even though `add` already returns the existing entry for repeated
  values. Insert with `add` alone, taking one reference per accepted table
  entry, and surrender those references through the encoded-ID remap after
  grid decoding, the same scheme hyperlink entries already use. Refcount
  outcomes are identical: each distinct style nets its cell references.
  
  Benchmarks ("prev" is the parent commit):
  
  | wasm      | encode prev | encode   | decode prev | decode   |
  |-----------|------------:|---------:|------------:|---------:|
  | ascii     |     2.13 ms |  2.12 ms |     2.54 ms |  2.59 ms |
  | styled    |     2.29 ms |  2.23 ms |     6.75 ms |  6.43 ms |
  | truecolor |     4.95 ms |  3.44 ms |    12.05 ms |  8.35 ms |
  | cjk       |     6.23 ms |  5.99 ms |    11.39 ms | 11.39 ms |
  | grapheme  |     8.72 ms |  8.33 ms |    11.27 ms | 10.89 ms |
  
  | native | mode   | prev    | this    |
  |--------|--------|--------:|--------:|
  | ascii  | encode | 24.4 ms | 24.7 ms |
  | ascii  | decode | 45.1 ms | 47.5 ms |
  | utf8   | encode | 41.9 ms | 41.9 ms |
  | utf8   | decode | 58.6 ms | 58.8 ms |
  ```
- [`eb09bf8`](https://github.com/ghostty-org/ghostty/commit/eb09bf82918de51f22b805dc705ed67b2968b984) terminal/snapshot: interleave software CRC32C streams ([@mitchellh](https://github.com/mitchellh))
  ```text
  Slicing tables removed the byte-at-a-time dependency chain, but each
  16-byte fold still depends serially on the previous one, leaving the
  software CRC latency-bound at roughly 2.5-3 GB/s in V8 while snapshot
  payloads run through it once per direction. wasm has no carry-less
  multiply, so wider tables are the only classic escape — and measuring
  slicing-by-32 against interleaving showed the extra 16 KB of tables buys
  nothing once the chain is hidden.
  
  Instead, inputs of 4 KiB and up split into thirds processed as three
  independent fold chains in one loop, then merge with the GF(2) zero-shift
  operator: crc(A ++ B, s) = crc(B, 0) XOR zeroShift(crc(A, s), |B|). The
  shift matrices are comptime, storing only even powers of two (an odd
  power applies the preceding matrix twice), 4 KB total. Software CRC
  throughput roughly doubles; hardware backends are untouched, so native
  is unaffected (tables below are noise).
  
  Benchmarks ("prev" is the parent commit):
  
  | wasm      | encode prev | encode   | decode prev | decode   |
  |-----------|------------:|---------:|------------:|---------:|
  | ascii     |     2.12 ms |  1.73 ms |     2.59 ms |  2.17 ms |
  | styled    |     2.23 ms |  1.47 ms |     6.43 ms |  5.38 ms |
  | truecolor |     3.44 ms |  2.30 ms |     8.35 ms |  7.17 ms |
  | cjk       |     5.99 ms |  3.89 ms |    11.39 ms |  9.50 ms |
  | grapheme  |     8.33 ms |  6.94 ms |    10.89 ms |  9.24 ms |
  
  | native | mode   | prev    | this    |
  |--------|--------|--------:|--------:|
  | ascii  | encode | 24.7 ms | 24.8 ms |
  | ascii  | decode | 47.5 ms | 49.2 ms |
  | utf8   | encode | 41.9 ms | 42.4 ms |
  | utf8   | decode | 58.8 ms | 59.5 ms |
  ```
- [`433b16b`](https://github.com/ghostty-org/ghostty/commit/433b16bcb1226a5d840318f88a1fb59e089b0649) terminal/apc: limit glyf decode allocations ([@mitchellh](https://github.com/mitchellh))
  ```text
  Limit individual allocations made while decoding registered glyf
  outlines to 64 KB.
  
  Carefully crafted glyf outlines could expand into ~768KB of memory per
  glossary entry, which adds up to hundreds of MB per terminal surface.
  Across many terminals this could cause issues.
  
  The 64KB number was chosen by inspecting every glyph across Apple
  symbols and Noto emoji and the largest single glyph found was 40KB. So,
  64KB is generous while limiting each terminal to ~68MB of RAM for max
  glyph glossaries.
  ```
- [`746a11c`](https://github.com/ghostty-org/ghostty/commit/746a11c721a1cf31d2691008340c719bb0a84b03) libghostty: much faster terminal snapshot encode and decode for wasm ([#13848](https://github.com/ghostty-org/ghostty/issues/13848)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Snapshot encode is now 4-7x faster, decode is 3x faster for wasm builds.
  
  Snapshot decode is particularly important for wasm builds because
  libghostty is mainly used on web as a terminal _viewer_ and snapshots
  are the best, most efficient way to ship down full terminal state.
  
  The biggest change here is a totally custom software CRC32
  implementation, which accounted for ~70% of total decode time. Native
  builds on aarch64/x86_64 use dedicated hardware instructions that wasm
  doesn't have. We've written a custom CRC32 impl (verified against Zig
  stdlib through randomized unit tests) that goes from 0.3 GB/s to 5 GB/s
  throughput in V8.
  
  ## Benchmarks
  
  Wasm on V8:
  
  | Workload | Encode Before | Encode After | Speedup | Decode Before |
  Decode After | Speedup |
  |---|---|---|---|---|---|---|
  | ascii | 290 MB/s | 1182 MB/s | 4.1x | 318 MB/s | 946 MB/s | 3.0x |
  | styled (sgr16) | 387 MB/s | 2771 MB/s | 7.2x | 284 MB/s | 758 MB/s |
  2.7x |
  | sgr-truecolor | 361 MB/s | 2382 MB/s | 6.6x | 252 MB/s | 766 MB/s |
  3.0x |
  | cjk | 411 MB/s | 2686 MB/s | 6.5x | 339 MB/s | 1100 MB/s | 3.2x |
  | grapheme | 280 MB/s | 1117 MB/s | 4.0x | 287 MB/s | 839 MB/s | 2.9x |
  
  Native on aarch64:
  
  | Corpus | Mode | Before | After |
  |---|---|---|---|
  | ascii | encode | 40.6 ms | 24.8 ms |
  | ascii | decode | 51.2 ms | 49.2 ms |
  | utf8 | encode | 45.2 ms | 42.4 ms |
  | utf8 | decode | 59.8 ms | 59.5 ms |
  
  **AI usage:** Fable did everything here except write this PR and the
  comments. It also wrote the commit messages in this case. I reviewed
  everything.
  ```
- [`e524df6`](https://github.com/ghostty-org/ghostty/commit/e524df6c829ec11eccc88d1a01e1a7a0416d5454) terminal/apc: limit glyf decode allocations ([#13849](https://github.com/ghostty-org/ghostty/issues/13849)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Limit individual allocations made while decoding registered glyf
  outlines to 64 KB.
  
  Carefully crafted glyf outlines could expand into ~768KB of memory per
  glossary entry, which adds up to hundreds of MB per terminal surface.
  Across many terminals this could cause issues.
  
  The 64KB number was chosen by inspecting every glyph across Apple
  symbols and Noto emoji and the largest single glyph found was 40KB. So,
  64KB is generous while limiting each terminal to ~68MB of RAM for max
  glyph glossaries.
  
  AI was used only to write initial tests, I rewrote em.
  ```
- [`cbe8a0e`](https://github.com/ghostty-org/ghostty/commit/cbe8a0ed4eb27e1530bc8132e52a6c45c135332c) cli: keep cached SSH terminfo installs current ([#13844](https://github.com/ghostty-org/ghostty/issues/13844)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  On a local cache miss, always send our embedded terminfo source to the
  remote `tic` instead of accepting any existing entry reported by
  `infocmp`.
  
  We also version cache entries using a content-derived hash of our
  embedded terminfo. Non-matching entries produce a cache miss and trigger
  (re)installation.
  ```
- [`9009122`](https://github.com/ghostty-org/ghostty/commit/9009122953f59d4900143aad587202a70c2136f4) macos: send all `insertText` commits as key events ([#13817](https://github.com/ghostty-org/ghostty/issues/13817)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Partially addresses #13796. Extends #13222.
  
  Previously, `insertText` commits without marked text were delivered via
  `sendText`, which applies paste semantics and wraps the text in
  bracketed
  paste when the program enables it. macOS dictation and other input
  methods often commit without marked text, so programs treated dictated
  text as a paste: opencode collapsed it into a `"[Pasted ~N lines]"` chip
  and Neovim applied paste-mode handling.
  
  `insertText` is only invoked by input methods (IME, dictation, emoji
  picker, character viewer); real paste operations use a separate path.
  Every non-empty commit is now sent as a key event — the same path
  already used for preedit commits since #13222 — so input method text
  always arrives as typed input.
  
  Typing is unaffected (the accumulator path returns earlier) and Cmd+V
  pastes are unaffected. `committedPreeditTextAction` is renamed to
  `committedTextAction` since it no longer only handles preedit commits.
  
  Testing:
  
  - 311 macOS unit tests pass.
  - Manually verified on macOS 26: dictation into Opencode and Neovim
    arrives inline with no paste handling; emoji picker inserts inline;
    Chinese IME composition unchanged; dictation in Neovim normal mode now
    behaves as keystrokes, matching Terminal.app.
  
  Notes:
  
  - Dictated "new line" now matches Terminal.app behavior (no newline
    with typed-text semantics). The previous behavior came from the paste
    path preserving the newline; a follow-up could deliver it as an
    Enter keypress if desired.
  
  AI usage: drafted with OMO + OpenCode + DeepSeek V4 Pro assistance;
  reviewed, edited, and manually tested by the author.
  ```
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
Summary: 9 runs • 280 commits • 27 authors

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
- [`e69dc2b`](https://github.com/ghostty-org/ghostty/commit/e69dc2bee8ac57f853ee07590548590a35aab89b) renderer: reset terminal state cleanup counter ([#13585](https://github.com/ghostty-org/ghostty/issues/13585)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Reset the frame counter whenever retained render state is cleared.
  Otherwise, every subsequent frame will be deinitialized and rebuilt.
  ```
- [`b9d8829`](https://github.com/ghostty-org/ghostty/commit/b9d88292be587388a336a2e59c08c4e993c04109) terminal: speed up formatting anywhere from ~1.5x to ~8x ([#13587](https://github.com/ghostty-org/ghostty/issues/13587)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This PR speeds up our formatting (plain text, html, and VT) by anywhere
  from ~1.5x to ~8x.
  
  The formatter is the hot path behind multiple features in Ghostty GUI:
  clipboard copy (plain/VT/HTML), `write_screen_file`, `selectionString`,
  and terminal search sliding window. It's also the hot path for
  libghostty users, namely people like
  [zmx](https://github.com/neurosnap/zmx) which utilize the VT formatter
  to restore a terminal.
  
  This PR also adds the benchmarking infrastructure for the formatter.
  
  ## How
  
  - **Fast cell-run optimization.** For simple cells (single codepoint, no
  style/hyperlink) we encode them as a single run rather than one at a
  time.
  - **Make some arguments comptime.** Generates more code but benchmarks
  show it improves things, specifically for per-format switches that we do
  a LOT.
  - **Interned style id fast path.** Styles are interned per page, so id
  equality implies style equality. We track the id of the active style and
  skip the per-cell `Style` copy + `eql` when it matches.
  - **Fast printing.** Avoid `std.fmt` where possible and assemble
  integers, RGB colors, codepoints in fixed-width buffers with a single
  memcpy. This was extracted partially to `fastprint.zig` so we can reuse
  it.
  - **Avoid double-formatting for tracked pins.** Previously we formatted
  twice (once through a `Discarding` writer to count bytes) for pin maps.
  Now I'm smarter about it and do a single pass.
  
  ## Performance
  
  All on my machine, 80x24 terminal, 10K lines of scrollback.
  
  | workload              | main     | this PR  | speedup | throughput |
  | --------------------- | -------- | -------- | ------- | ---------- |
  | plain / plain         | 5.74 ms  | 1.67 ms  | 3.4x    | 364 MB/s   |
  | plain / vt            | 6.46 ms  | 1.04 ms  | 6.2x    | 596 MB/s   |
  | plain / html          | 7.39 ms  | 2.32 ms  | 3.2x    | 308 MB/s   |
  | unicode / plain       | 9.74 ms  | 5.42 ms  | 1.8x    | 276 MB/s   |
  | unicode / vt          | 10.42 ms | 5.53 ms  | 1.9x    | 275 MB/s   |
  | unicode / html        | 12.53 ms | 7.35 ms  | 1.7x    | 509 MB/s   |
  | styled / plain        | 5.65 ms  | 1.69 ms  | 3.4x    | 360 MB/s   |
  | styled / vt           | 9.07 ms  | 4.20 ms  | 2.2x    | 409 MB/s   |
  | styled / html         | 10.78 ms | 6.64 ms  | 1.6x    | 740 MB/s   |
  | mixed / plain         | 8.59 ms  | 4.81 ms  | 1.8x    | 226 MB/s   |
  | mixed / vt            | 11.25 ms | 6.65 ms  | 1.7x    | 250 MB/s   |
  | mixed / html          | 14.47 ms | 10.52 ms | 1.4x    | 414 MB/s   |
  | wrapped / plain       | 7.30 ms  | 1.11 ms  | 6.6x    | 733 MB/s   |
  | wrapped / vt          | 8.14 ms  | 1.04 ms  | 7.8x    | 789 MB/s   |
  | wrapped / html        | 9.00 ms  | 2.12 ms  | 4.2x    | 465 MB/s   |
  | pin-map / plain       | 12.51 ms | 3.80 ms  | 3.3x    |            |
  | pin-map / vt          | 13.12 ms | 2.99 ms  | 4.4x    |            |
  | active screen / plain | 12.5 µs  | 2.7 µs   | 4.6x    |            |
  | active screen / vt    | 18.4 µs  | 6.8 µs   | 2.7x    |            |
  
  Workloads:
  - `plain` is ASCII lines
  - `unicode` is 2/3/4-byte codepoints with 10% grapheme clusters
  - `styled` is heavy SGR churn
  - `mixed` is styles + Unicode + hyperlinks
  -  `wrapped` is a continuous soft-wrapped stream
  - `pin-map`/`active screen` are the selectionString/search-style and
  visible-screen-only cases respectively.
  ```
- [`6687d60`](https://github.com/ghostty-org/ghostty/commit/6687d6089dc254b14b1cdb22ca310f8394c3290f) macos: avoid leaking ports while awaiting accessibility ([#13590](https://github.com/ghostty-org/ghostty/issues/13590)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  #11799
  
  Creating a CGEventTap without Accessibility permission leaks a Mach port
  inside CoreGraphics on every failed attempt. The global keybind listener
  retried this once per second while waiting for permission, so Ghostty
  eventually exhausted the process port limit.
  
  Request Accessibility access once, poll AXIsProcessTrusted while access
  is denied, and create the event tap only after access is granted. Stop
  polling before creation so an unrelated tap failure cannot restart the
  leaking retry loop.
  
  Tested this with various settings and global keys working fine.
  ```
- [`df23bef`](https://github.com/ghostty-org/ghostty/commit/df23bef0e91d602ab4b95e33ef9a4c213a1058da) i18n: translation support for command palete and Latvian translation for it ([@EriksRemess](https://github.com/EriksRemess))
- [`1125fa2`](https://github.com/ghostty-org/ghostty/commit/1125fa26df6387131295fb4433ffcab411f0bcfc) i18n: note about i18n.N_ usage and @inComptime() return msgid for i18n._ ([@EriksRemess](https://github.com/EriksRemess))
- [`e0744dd`](https://github.com/ghostty-org/ghostty/commit/e0744dde62c53555aa6b9457e2bb9fd8c74a1dc2) i18n - command palette - empty translations ([@EriksRemess](https://github.com/EriksRemess))
- [`f5419b9`](https://github.com/ghostty-org/ghostty/commit/f5419b9b151e85c027f481f045f586e10ddf1d01) gtk: do not set bell ringing if already focused ([@lotheac](https://github.com/lotheac))
- [`bdd849f`](https://github.com/ghostty-org/ghostty/commit/bdd849fc2feff762612c2d057db7e013c118e390) Update VOUCHED list ([#13596](https://github.com/ghostty-org/ghostty/issues/13596)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/13589#issuecomment-5178660481)
  from @jparise.
  
  Vouch: @lotheac
  ```
- [`85083d2`](https://github.com/ghostty-org/ghostty/commit/85083d23cd12e2959f11dd247916c43a51f5f10e) config: clarify cursor-click-to-move's relation to shell-integration ([@lotheac](https://github.com/lotheac))
  ```text
  the original wording is a bit confusing; I thought cursor-click-to-move
  required shell-integration to be enabled, and was confused when the
  mouse was still moving my cursor in fish even with
  shell-integration=none.
  ```
- [`1f6e266`](https://github.com/ghostty-org/ghostty/commit/1f6e26642e540ddf01803858772909c4fab33428) config: clarify cursor-click-to-move's relation to shell-integration ([#13589](https://github.com/ghostty-org/ghostty/issues/13589)) ([@jparise](https://github.com/jparise))
- [`cfa0ca7`](https://github.com/ghostty-org/ghostty/commit/cfa0ca710659175d3ae21b2c136dcf1024fd5d91) macos: defer transparent titlebar KVO rebinding ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13386
  
  Defer transparent-titlebar KVO rebinding to the next main-queue turn.
  Track the observed tab group so unchanged bindings are preserved.
  
  Previously, a tab-group callback could invalidate and recreate its own
  observation before returning, leaving closed terminal windows registered
  with AppKit after the undo timeout. These windows accumulated titlebar and
  layer state, increasing memory use and WindowServer CPU with tab churn.
  
  Validated with an AppDelegate change that sat and created/closed tabs
  in a loop, then counted weak controllers/windows/nsapp window.
  ```
- [`363e6e6`](https://github.com/ghostty-org/ghostty/commit/363e6e6b427c1f3a6647b14692f1953746d83045) i18n: translation support for command palete ([#11641](https://github.com/ghostty-org/ghostty/issues/11641)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Most obvious next step in translating Ghostty is the command palette.
  Added support for i18n.N_ (https://docs.gtk.org/glib/i18n.html#macros).
  Made a Latvian translation for the command palette to test. Codex did
  bulk of the translations but I verified them.
  ```
- [`594ee21`](https://github.com/ghostty-org/ghostty/commit/594ee212bc3c048ffa06ba90623eaf207a4d145c) macos: defer transparent titlebar KVO rebinding ([#13601](https://github.com/ghostty-org/ghostty/issues/13601)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13386, based on
  https://github.com/mustafa0x/ghostty/commit/a8c090
  
  Defer transparent-titlebar KVO rebinding to the next main-queue turn.
  Track the observed tab group so unchanged bindings are preserved.
  
  Previously, a tab-group callback could invalidate and recreate its own
  observation before returning, leaving closed terminal windows registered
  with AppKit after the undo timeout. These windows accumulated titlebar
  and layer state, increasing memory use and WindowServer CPU with tab
  churn.
  
  Validated with an AppDelegate change that sat and created/closed tabs in
  a loop, then counted weak controllers/windows/nsapp window.
  ```
- [`08342c9`](https://github.com/ghostty-org/ghostty/commit/08342c92446ceda22b49f42ce39e8c4714054a6e) Update VOUCHED list ([#13603](https://github.com/ghostty-org/ghostty/issues/13603)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13602#discussioncomment-17895866)
  from @jcollie.
  
  Vouch: @UnsaltedScholar
  ```
- [`ca56412`](https://github.com/ghostty-org/ghostty/commit/ca56412bf28ae4de7e323d4b30b39844501be05b) gtk: forward middle click to TUIs with mouse reporting ([#13108](https://github.com/ghostty-org/ghostty/issues/13108)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fix for Issue #12940
  I actually do not know if this has already been resolved and the issue
  is just still open. Either way, here's a fix. Now we run a check to see
  if the current program is accepting mouse events before discarding the
  middle click.
  ```
- [`48d85ea`](https://github.com/ghostty-org/ghostty/commit/48d85eaeb06ac9fc49073815bda5bac97de655ca) core: fix mouse reporting mutex lock ([@mitchellh](https://github.com/mitchellh))
- [`02f3483`](https://github.com/ghostty-org/ghostty/commit/02f34835ea48b9daee0abdcc09fca02702def688) datastruct: remove unused LRU implementation ([@Uzaaft](https://github.com/Uzaaft))
- [`8cfbaf5`](https://github.com/ghostty-org/ghostty/commit/8cfbaf545ab4215ccc9820ba905f502387d1de1f) config: formatted action should be parsable into the original ([@bo2themax](https://github.com/bo2themax))
- [`b67f8ef`](https://github.com/ghostty-org/ghostty/commit/b67f8ef51d8092ff3aaf52574a89c98f9f46b0ca) config: don't escape Binding.Action.String ([@bo2themax](https://github.com/bo2themax))
- [`066a0b7`](https://github.com/ghostty-org/ghostty/commit/066a0b7c45e50694df0c3c3892961523162a55ad) macOS: show description when subtitle missing in CommandPalette ([@bo2themax](https://github.com/bo2themax))
- [`51cf099`](https://github.com/ghostty-org/ghostty/commit/51cf099678d90775b3c587e5e34427531396d75e) datastruct: remove unused LRU implementation ([#13607](https://github.com/ghostty-org/ghostty/issues/13607)) ([@jcollie](https://github.com/jcollie))
- [`760a250`](https://github.com/ghostty-org/ghostty/commit/760a2500291df56c42cccd4d34efeeceaf8bd6ae) config: formatted action should be parsable into the original  ([#13609](https://github.com/ghostty-org/ghostty/issues/13609)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This fixes the issue where an action with string as it's parameter is
  not working correctly in CommandPalette, found in #9671. For example:
  
  ```
  command-palette-entry = title:"Set Ghostty Title",description:test sending text.,action:set_tab_title:👻
  keybind=cmd+r=set_tab_title:👻
  ```
  
  Keybind works perfectly, but the title is escaped when triggering in
  CommandPalette.
  
  > Introduced in
  [#8873](https://github.com/ghostty-org/ghostty/pull/8873/changes#diff-9e7936787320bcf70e332c868125039d8c0a7f96c4a88f2af0af21d952c6830dR1216),
  I tested the fixed issue as well, the following config still parses
  correctly, mentioned in
  https://github.com/ghostty-org/ghostty/issues/8849#issuecomment-3322018212.
  
  ```
  command-palette-entry = title:Focus Split: Next,description:"Focus the next split, if any.",action:goto_split:next
  ```
  
  Also `ghostty +show-config` now will also output the readable strings as
  well.
  <img width="1078" height="428" alt="image"
  src="https://github.com/user-attachments/assets/f9dc1447-7b4e-44f4-8362-b54f4d805c7a"
  />
  ````
- [`b8ab2ff`](https://github.com/ghostty-org/ghostty/commit/b8ab2ff16847b73afd2ea99498e44ab6694e930f) macOS: show/search description when subtitle missing in CommandPalette ([#13610](https://github.com/ghostty-org/ghostty/issues/13610)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  <img width="1125" height="552" alt="image"
  src="https://github.com/user-attachments/assets/09866c9b-d5c4-422f-860b-de4de4cca055"
  />
  ```
- [`63d08c0`](https://github.com/ghostty-org/ghostty/commit/63d08c0342ba4b5132de7b3098797a80eba8b757) macOS: show cancel update option when its actually cancellable ([@bo2themax](https://github.com/bo2themax))
  ```text
  `extracting` and `installing` state aren't cancellable by us
  ```
- [`a86c49d`](https://github.com/ghostty-org/ghostty/commit/a86c49d7af2a92e945487f52e821ee478e276fad) macOS: rename UpdateState.isIdle to isHidden ([@bo2themax](https://github.com/bo2themax))
- [`ccb08f3`](https://github.com/ghostty-org/ghostty/commit/ccb08f35f683d6087786dda8e793e911ef1a2f8a) macOS: show cancel update option when its actually cancellable ([#13612](https://github.com/ghostty-org/ghostty/issues/13612)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `extracting` and `installing` state aren't cancellable by us.
  
  > Recommend reviewing with whitespace hidden
  ```
- [`a00d155`](https://github.com/ghostty-org/ghostty/commit/a00d155e9cb31829a27c3342653e30c6220e93ca) config: limit command translations to GTK ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13614
  
  Only translate the shared default commands when building the GTK runtime.
  macOS now use the source strings until we do broader localization.
  ```
- [`d2f08f1`](https://github.com/ghostty-org/ghostty/commit/d2f08f1589cbe73e1f7cbedc2db9c5e1ae5a1ca6) config: limit command translations to GTK ([#13615](https://github.com/ghostty-org/ghostty/issues/13615)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13614
  
  Only translate the shared default commands when building the GTK
  runtime. macOS now use the source strings until we do broader
  localization.
  ```
- [`d7f7a4e`](https://github.com/ghostty-org/ghostty/commit/d7f7a4e736d47bb3501d22cc9118b23dd398a764) macOS: rename UpdateState.isIdle to isHidden ([#13613](https://github.com/ghostty-org/ghostty/issues/13613)) ([@mitchellh](https://github.com/mitchellh))
- [`2346c4f`](https://github.com/ghostty-org/ghostty/commit/2346c4fe4767373cda50b5977d95191f714b1cca) Update VOUCHED list ([#13617](https://github.com/ghostty-org/ghostty/issues/13617)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12984#issuecomment-5187316604)
  from @mitchellh.
  
  Denounce: @jamesarch
  ```
- [`9e30f70`](https://github.com/ghostty-org/ghostty/commit/9e30f70f23418fecbdca1088673000417527c4e4) gtk: do not set bell ringing if already focused ([#13597](https://github.com/ghostty-org/ghostty/issues/13597)) ([@pluiedev](https://github.com/pluiedev))
- [`f17b425`](https://github.com/ghostty-org/ghostty/commit/f17b425aac518acd7cb7cbc500b862656631a4a8) surface: use id instead of intFromPtr ([@pluiedev](https://github.com/pluiedev))
  ```text
  intFromPtr was always a hack that we had to use before we had stable
  surface IDs, and it was always slightly unsafe. Let's do it properly
  this time.
  ```
- [`1d053bd`](https://github.com/ghostty-org/ghostty/commit/1d053bd6ea28d9109fa352862588e421c2f2767f) gtk: implement drag-to-move for splits ([@pluiedev](https://github.com/pluiedev))
  ```text
  One major todo is moving splits across different split trees (i.e.
  moving across tabs and windows), but that would involve a lot more logic.
  This MVP version works for now.
  
  GTK version of #10090
  
  Closes #10224
  ```
- [`98fae16`](https://github.com/ghostty-org/ghostty/commit/98fae16a0503548b894e4bbed84f645a79ab5210) gtk: support cross-tree surface drag and drop ([@pluiedev](https://github.com/pluiedev))
- [`261848c`](https://github.com/ghostty-org/ghostty/commit/261848c2fbd34ddb5fb74dcc8327c5ded980d691) gtk: reformat blueprints ([@pluiedev](https://github.com/pluiedev))
- [`25b2d8a`](https://github.com/ghostty-org/ghostty/commit/25b2d8a38568eab31283786f6a1f1501411863b5) input,apprt: add new_tab_to_new_window action ([@pluiedev](https://github.com/pluiedev))
- [`c93752a`](https://github.com/ghostty-org/ghostty/commit/c93752a008b5a9a9a717c9e2bea4742d7efb4c00) macOS: suppress restart tips for auto update ([@bo2themax](https://github.com/bo2themax))
- [`5b70f20`](https://github.com/ghostty-org/ghostty/commit/5b70f208bc6870bb32f13720376840edc3c5ed31) terminal: print repeated characters through printSlice ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  While doing some work on my tmux fork I noticed multiple parts of
  libghostty-vt was slower than tmux equivalents(isolated). Turns out they
  do some smart stuff there.
  
  printRepeat called print() once per repeat, so something like \x1b[2000b
  ran grapheme checks, width lookups, wrap handling, etc etc 2000 times.
  
  printSlice is already documented as semantically identical to
  calling print per codepoint, so this just feeds the repeated
  codepoint through it in 4096-entry stack chunks. Simple runs take
  the batched fast path, and anything that needs care falls back to the
  previous behaviour.
  ```
- [`19e9f49`](https://github.com/ghostty-org/ghostty/commit/19e9f49089606310bb717a6a8e49174ffdd0e90a) surface: use id instead of intFromPtr ([#13620](https://github.com/ghostty-org/ghostty/issues/13620)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  intFromPtr was always a hack that we had to use before we had stable
  surface IDs, and it was always slightly unsafe. Let's do it properly
  this time.
  ```
- [`3f8b99b`](https://github.com/ghostty-org/ghostty/commit/3f8b99bb68cb46381924f33496b7e6a25d3859a8) terminal: print repeated characters through printSlice ([#13625](https://github.com/ghostty-org/ghostty/issues/13625)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  `printRepeat` (CSI `b`, repeat the previous character N times) calls
  `print()` once per repeat, so something like `\x1b[2000b` ran grapheme
  checks, width lookups, wrap handling, and the integrity assert 2000
  times for what is usually the same character on the same row.
  
  `Terminal.print` was 24% of samples on a REP-heavy micro benchmark.
  
  This PR just aims to add a fast path by introducing a chunking
  mechanism. anything that needs care (insert mode, grapheme clustering,
  hyperlinks) still falls back to per-codepoint print() inside printSlice,
  so behavior *should* stay unchanged.
  
  Some profiling data:
  
  Generated with some plain stupid logic:
  
  ```py
  D = "benchdata"
  parts, total = [], 0
  while total < 40_000_000:
      line = "x" + "\x1b[80b" + "y" + "\x1b[35b" + "\r\n"
      parts.append(line); total += len(line)
  open(f"{D}/rep.bin", "wb").write("".join(parts).encode())
  ```
  **macOS (hyperfine, 15 runs, warmup 3):**
  
  | | mean |
  |---|---|
  | before | 2.360 s |
  | after | 1.166 s |
  
  
  And now the really interesting and promising stuff
  
  **Linux, 24-core NixOS x86_64 (poop, 6s sampling):**
  
  | | wall_time | instructions | branch_misses | peak_rss |
  |---|---|---|---|---|
  | before | 1.51 s | 50.9 G | 9.41 M | 6.82 MB |
  | after | 562 ms | 9.07 G | 114 K | 6.74 MB |
  ````
- [`5944ab2`](https://github.com/ghostty-org/ghostty/commit/5944ab286d825b48b68d0e99088273cf435d6870) macOS: suppress restart tips for auto update ([#13623](https://github.com/ghostty-org/ghostty/issues/13623)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  With this, users will not be prompted to restart the app when an
  automatic update is ready. Relaunching with this state will have no
  visible difference to users.
  
  If the user checks for updates manually, either by menu, command
  palette, or keybind, a restart alert will be prompted.
  
  Closes #13478
  
  Auto updates:
  
  
  https://github.com/user-attachments/assets/f77f65a1-6e2f-4002-961c-fee4b73d447e
  
  Manual Updates:
  
  
  https://github.com/user-attachments/assets/8a52a5a0-2022-413f-97c5-6f9a2eb26e7a
  ```
- [`d02ad96`](https://github.com/ghostty-org/ghostty/commit/d02ad967b62af94d7ffaca3bbac9029966ff8824) macOS: update command options match order ([@claude](https://github.com/claude))
  ```text
  Matches are sorted in the following order:
  leadingColor > title > subtitle > description.
  
  Ranking is lexicographic on (colorScore, textScore)
  ```
- [`d866fa4`](https://github.com/ghostty-org/ghostty/commit/d866fa4553850050ec54eefa9daf2c63a9f4f4e5) terminal/kitty: fix graphics range deletion ([@mitchellh](https://github.com/mitchellh))
  ```text
  Use inclusive image ID bounds for the Kitty graphics protocol range
  delete operation.
  
  Range deletion previously joined the lower and upper bound checks with or,
  which matched every placement for any valid range. A targeted delete could
  therefore remove every graphics placement.
  
  Join the bounds with and and update the lowercase and uppercase range tests
  to keep placements below and above the selected interval.
  ```
- [`af2faa3`](https://github.com/ghostty-org/ghostty/commit/af2faa311a5a16b40afff8410a28da077b8ced57) terminal/kitty: restrict temporary image file paths ([@mitchellh](https://github.com/mitchellh))
  ```text
  Require temporary image file paths to match complete directory
  components when checking /tmp, /dev/shm, the configured temporary
  directory, and its resolved path.
  
  The previous byte-prefix checks accepted similarly named sibling
  directories such as /tmpX. A temporary-file transmission could read
  and unlink a file outside the permitted temporary directories.
  
  Add a component-boundary helper and regression coverage for built-in
  and configured directory prefixes. An integration test also verifies
  that a rejected file remains on disk.
  ```
- [`e5840bb`](https://github.com/ghostty-org/ghostty/commit/e5840bb9bacdaae78c42baa4b276f52eaa91fdbe) terminal/kitty: harden placement geometry ([@mitchellh](https://github.com/mitchellh))
  ```text
  Treat Kitty placement dimensions and offsets as untrusted values when
  calculating pixel, grid, and rectangle geometry. Saturate results that
  do not fit and return no rectangle when missing pixel metrics produces
  an empty grid.
  
  Unchecked u32 arithmetic previously panicked in safe builds and wrapped
  in fast builds. A zero row count could underflow into a maximum-size
  page traversal, while maximum dimensions could spin cursor movement or
  overflow render visibility calculations.
  
  Use checked integer scaling instead of floating-point casts, saturating
  arithmetic for extents and cursor columns, and bound off-screen cursor
  work to the terminal row count. Compute C API visibility in i64 and
  cover maximum protocol values in storage, execution, and render-info
  tests.
  ```
- [`fb4c561`](https://github.com/ghostty-org/ghostty/commit/fb4c56159fe8c6c19fa84c2a6691a44098c65e78) core: transfer long key encoding buffer ([@jparise](https://github.com/jparise))
  ```text
  The long-preedit fallback introduced in e95b1707c intentionally allocated
  twice. The encoder wrote into an oversized caller-owned buffer and returned
  only the written subslice, so transferring it required manually shrinking
  the allocation or tracking its original capacity. The copy kept that rare
  path simple.
  
  The key encoder moved to std.Io.Writer.Allocating in 44496df899. Its
  toOwnedSlice method handles shrinking and ownership transfer, remapping when
  the allocator supports it and falling back to an allocation and copy when it
  does not. Use it directly for WriteReq.alloc to remove the guaranteed second
  allocation while preserving cleanup on failure.
  ```
- [`ec04900`](https://github.com/ghostty-org/ghostty/commit/ec04900ab957c7637584e2002aeb6f24c985bd70) terminal/kitty: validate opened image file paths ([@mitchellh](https://github.com/mitchellh))
  ```text
  Validate Kitty file transmissions against a canonical path derived from
  the open file handle. Keep temporary file policy and cleanup keyed to
  that handle path.
  
  Path validation previously ran before opening, so a local cooperating
  process could replace a symlink or directory entry and make Ghostty
  read a blocklisted file.
  
  Open the submitted path once, derive its canonical path from the handle,
  and use the same handle for stat and reads. Add a regression test that
  replaces a blocked symlink after open and verifies the pinned target is
  still rejected.
  ```
- [`f6fca9a`](https://github.com/ghostty-org/ghostty/commit/f6fca9aabffc4f0576f9c427672b1972ed813dec) gtk: implement `move_tab_to_new_window` ([@pluiedev](https://github.com/pluiedev))
- [`f03d71d`](https://github.com/ghostty-org/ghostty/commit/f03d71d970a65aa6f58b6a836469258fbf2d52f4) po: update template ([@pluiedev](https://github.com/pluiedev))
- [`f766f30`](https://github.com/ghostty-org/ghostty/commit/f766f303a7d39b9f41fdda1b6d71b329f410d45f) terminal/kitty: validate shared memory ranges ([@mitchellh](https://github.com/mitchellh))
  ```text
  Validate Kitty shared memory byte ranges before mapping and copying
  image data. Interpret S as a byte count from O and preserve default
  raw-image sizing.
  
  Shared memory transmissions previously multiplied untrusted u32
  dimensions before the limit check and sliced mappings with an unchecked
  offset. Malformed commands could panic in safe builds or request a
  wrapped allocation in fast builds.
  
  Reject oversized dimensions before widening size arithmetic, derive
  bounded ranges from the stat size, and enforce max_size before
  constructing a slice. Add regression tests for explicit and implicit
  offsets, out-of-bounds offsets, and maximum dimensions.
  ```
- [`590d669`](https://github.com/ghostty-org/ghostty/commit/590d669c4a72eb9cb990bf0162071c2b9eb0f7ad) terminal/kitty: limit png decoder allocations ([@mitchellh](https://github.com/mitchellh))
  ```text
  Limit individual allocator requests made by PNG decoders to the Kitty
  graphics protocol's 400 MiB image ceiling. Add a reusable allocator
  wrapper for callers that need per-request bounds.
  
  PNG decoding previously used Wuffs' 4 GiB package limit and checked
  the result only after allocation. A tiny PNG with oversized dimensions
  could cause a multi-gigabyte RSS spike before being rejected.
  
  Wrap decoder allocators with LimitedAllocator and translate limit
  rejections to invalid image data while preserving genuine out-of-memory
  errors. Add allocator boundary tests and regression coverage for a
  crafted PNG below Wuffs' limit.
  ```
- [`d0c516f`](https://github.com/ghostty-org/ghostty/commit/d0c516f8f384ee4cc3304c4eef3dabc07c432de4) terminal/kitty: release replaced placement pins ([@mitchellh](https://github.com/mitchellh))
  ```text
  Release a Kitty graphics placement's tracked pin before replacement.
  
  Repeated updates to an external placement previously leaked tracked pins.
  
  Pass the owning screen to storage and deinitialize the old placement.
  ```
- [`402b922`](https://github.com/ghostty-org/ghostty/commit/402b9227de1efab24de981ce0d71b4d378417490) terminal/kitty: reclaim pruned placements ([@mitchellh](https://github.com/mitchellh))
  ```text
  Reclaim pin-backed Kitty graphics placements after their tracked screen
  content is pruned. Treat garbage pins as non-renderable until the next
  placement command sweeps them.
  
  Placements that scrolled beyond retained history previously remained in
  the placement map and tracked-pin set. Long-running graphics output could
  accumulate stale state, and remapped garbage pins could appear at an
  unrelated fallback location.
  
  Sweep garbage placements before growing the placement map, releasing each
  tracked pin while preserving virtual placements. Return no geometry or
  visible render position for garbage pins and cover both storage and C API
  behavior with regression tests.
  ```
- [`e206558`](https://github.com/ghostty-org/ghostty/commit/e2065583a41e576cd94927832d8e8b72f0cae1f1) core: transfer long key encoding buffer ([#13628](https://github.com/ghostty-org/ghostty/issues/13628)) ([@jcollie](https://github.com/jcollie))
  ```text
  The long-preedit fallback introduced in e95b1707c intentionally
  allocated twice. The encoder wrote into an oversized caller-owned buffer
  and returned only the written subslice, so transferring it required
  manually shrinking the allocation or tracking its original capacity. The
  copy kept that rare path simple.
  
  The key encoder moved to std.Io.Writer.Allocating in 44496df899. Its
  toOwnedSlice method handles shrinking and ownership transfer, remapping
  when the allocator supports it and falling back to an allocation and
  copy when it does not. Use it directly for WriteReq.alloc to remove the
  guaranteed second allocation while preserving cleanup on failure.
  ```
- [`dd03528`](https://github.com/ghostty-org/ghostty/commit/dd035284c2c548c139e4b312751f7b9ef628d251) Kitty graphics protocol bugs ([#13630](https://github.com/ghostty-org/ghostty/issues/13630)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Specifics in each commit message. This will be part of a security
  advisory in 1.4.0 since these patches issues related to overflows, DoS,
  unbounded memory allocation, etc.
  ```
- [`33d34cf`](https://github.com/ghostty-org/ghostty/commit/33d34cf5ce7bece9e108aaab069584c0628300be) terminal: avoid VS15 cursor underflow ([@mitchellh](https://github.com/mitchellh))
  ```text
  Handle VS15 width changes when the wide grapheme base is directly under
  the cursor. Cover both disabled wraparound and restored pending-wrap
  cursor states.
  
  A zero cursor distance previously underflowed while locating the spacer
  tail. Debug builds panicked and ReleaseFast computed an out-of-bounds
  cell pointer before updating it.
  
  Find the spacer from the wide base instead of subtracting from the
  cursor distance. Reposition the cursor from the base column and clamp it
  to the active right margin.
  ```
- [`fe98aef`](https://github.com/ghostty-org/ghostty/commit/fe98aef21cf29e06555a3c76527923eb0256af2b) terminal: report DECECM as permanently reset ([#12660](https://github.com/ghostty-org/ghostty/issues/12660)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Closes #12505
  
  This PR allows Ghostty to respond to DECRQM queries for DECECM with the
  "permanently reset".
  
  AI disclosure: I used Codex to help inspect the relevant code path and
  explain the issue, but I reviewed and made the code changes myself.
  ```
- [`bd21ff1`](https://github.com/ghostty-org/ghostty/commit/bd21ff153e047f2480086aa4eb88c88fa8368823) terminal: avoid VS15 cursor underflow ([#13631](https://github.com/ghostty-org/ghostty/issues/13631)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Handle VS15 width changes when the wide grapheme base is directly under
  the cursor.
  
  A zero cursor distance previously underflowed while locating the spacer
  tail. Debug builds panicked and ReleaseFast computed an out-of-bounds
  cell pointer before updating it.
  ```
- [`38e891e`](https://github.com/ghostty-org/ghostty/commit/38e891e6c0bbaa50661b529424fc9fdd866ae252) terminal: require opt-in for title reports ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add an explicit libghostty-vt title-report option and keep CSI 21 t
  disabled unless an embedder enables it.
  
  Previously, registering the general PTY write callback also caused the
  terminal to echo attacker-controlled window titles. This exposed
  embedders to command injection after user interaction.
  
  Gate the response in the shared terminal stream, append the C API
  option without renumbering existing values, and cover the default,
  opt-in, and reset behavior in Zig and C API tests.
  ```
- [`727b8a0`](https://github.com/ghostty-org/ghostty/commit/727b8a02f8734840de664c060678dd66f01931f6) terminal: bound OSC and grapheme allocations ([@mitchellh](https://github.com/mitchellh))
  ```text
  Cap allocating OSC payloads at 8 MiB and retain at most 64 grapheme
  suffix codepoints per cell. Our limits are generous compared to other
  terminals and this prevents an easy DoS.
  
  When the grapheme codepoint max is hit we just ignore any remainders.
  This can result in real broken graphemes because Unicode spec is really
  unbounded on them but for all practical use cases its reasonable.
  
  Compared to other terminals:
  
  | Terminal | OSC capture limit | Cell codepoints |
  | --- | ---: | ---: |
  | Ghostty | 8 MiB | 65 |
  | kitty | ~256 KiB ordinary | 24 |
  | VTE | 4,096 scalars | 11 |
  | xterm | 20 or 600 KB | 3 default, 6 max |
  | Alacritty | unbounded | unbounded |
  | WezTerm | unbounded | no explicit limit |
  ```
- [`ad27c98`](https://github.com/ghostty-org/ghostty/commit/ad27c989a4cc59b9e9f906cd4e07cdc8c30b332b) libghostty-vt: require opt-in for title reports ([#13632](https://github.com/ghostty-org/ghostty/issues/13632)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add an explicit libghostty-vt title-report option and keep CSI 21 t
  disabled unless an embedder enables it.
  
  Previously, registering the general PTY write callback also caused the
  terminal to echo attacker-controlled window titles. This exposed
  embedders to command injection after user interaction. Ghostty fixed
  this a long time ago by making CSI 21 t an opt-in in the config. Do the
  same but with our C/Zig API.
  ```
- [`46767b5`](https://github.com/ghostty-org/ghostty/commit/46767b521358200bfe3f268f365ccd2f218db558) terminal: bound OSC and grapheme allocations ([#13633](https://github.com/ghostty-org/ghostty/issues/13633)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Cap allocating OSC payloads at 8 MiB and retain at most 64 grapheme
  suffix codepoints per cell. Our limits are generous compared to other
  terminals and this prevents an easy DoS.
  
  When the grapheme codepoint max is hit we just ignore any remainders.
  This can result in real broken graphemes because Unicode spec is really
  unbounded on them but for all practical use cases its reasonable.
  
  Compared to other terminals:
  
  | Terminal | OSC capture limit | Cell codepoints |
  | --- | ---: | ---: |
  | Ghostty | 8 MiB | 65 |
  | kitty | ~256 KiB ordinary | 24 |
  | VTE | 4,096 scalars | 11 |
  | xterm | 20 or 600 KB | 3 default, 6 max |
  | Alacritty | unbounded | unbounded |
  | WezTerm | unbounded | no explicit limit |
  ```
- [`4371871`](https://github.com/ghostty-org/ghostty/commit/4371871bc2074c8b615583bd4a7ebc1957480d58) terminal/kitty: evict without scratch allocation ([@jparise](https://github.com/jparise))
  ```text
  Track each image's placement count in its existing metadata. This lets
  us use constant-time usage checks (rather than scans) during eviction.
  
  Select the best candidate directly from storage on each eviction, preserving
  the existing priority order: unused status, transient hint, generation, then
  ID.
  
  Since eviction no longer allocates, it can't fail, so callers no longer
  need to handle out-of-memory conditions.
  ```
- [`77537c8`](https://github.com/ghostty-org/ghostty/commit/77537c8065f3055d214144caab7d137543a6e133) macos: handled untrusted OSC8 hyperlinks more carefully ([@mitchellh](https://github.com/mitchellh))
  ```text
  OSC8 hyperlinks previously executed directly via the NSWorkspace opener
  so a malicious application can just do whatever it wanted and trick the
  user into opening something through Launch Services.
  
  This PR notifies apprt of OSC8 hyperlinks so they can be handled
  specially. In this PR, I added macOS-specific handling of OSC8 through a
  variety of improvements:
  
    - Preview text is sanitized, so invisible Unicode characters now show.
    - Questionable-looking URLs require confirmation to open, but a user
      can confirm to open.
    - Very questionable or definitely unsafe URLs are blocked with an
      alert that only allows the user to copy the link. The alert also
      notifies the user why.
  ```
- [`54fe8e1`](https://github.com/ghostty-org/ghostty/commit/54fe8e188552977249a084db687e75aee6bf12e9) macos: handled untrusted OSC8 hyperlinks more carefully ([#13634](https://github.com/ghostty-org/ghostty/issues/13634)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  OSC8 hyperlinks previously executed directly via the NSWorkspace opener
  so a malicious application can just do whatever it wanted and trick the
  user into opening something through Launch Services.
  
  This PR notifies apprt of OSC8 hyperlinks so they can be handled
  specially. In this PR, I added macOS-specific handling of OSC8 through a
  variety of improvements:
  
    - Preview text is sanitized, so invisible Unicode characters now show.
  - Questionable-looking URLs require confirmation to open, but a user can
  confirm to open.
  - Very questionable or definitely unsafe URLs are blocked with an alert
  that only allows the user to copy the link. The alert also notifies the
  user why.
  
  This PR also adds an explicit `link-osc8` config (default true) that
  users can use to disable osc8 completely.
  
  ## Demos
  
  ### Custom URL Schemes (Confirm)
  
  <img width="1432" height="1110" alt="CleanShot 2026-08-05 at 10 25
  57@2x"
  src="https://github.com/user-attachments/assets/f7773ca2-3389-4749-a5c9-393ae097c044"
  />
  
  ### Invisible Characters (Block)
  
  <img width="1432" height="1110" alt="CleanShot 2026-08-05 at 10 26
  44@2x"
  src="https://github.com/user-attachments/assets/bd2d0f33-f128-46e8-9bdb-227afecbb942"
  />
  
  ### Executable Target (Block)
  
  <img width="1432" height="1110" alt="CleanShot 2026-08-05 at 10 27
  31@2x"
  src="https://github.com/user-attachments/assets/080c0524-2c8e-4931-892f-d2643a5d0d4e"
  />
  ```
- [`0060d89`](https://github.com/ghostty-org/ghostty/commit/0060d89b5be3a8b07d43599ea88fc7c5893bf36e) core: fix encoded key request cleanup ([@jparise](https://github.com/jparise))
  ```text
  Encoded key requests are owned by the caller until they are added to a
  key sequence or queued for IO. The child_exited path and failed queue
  append returned without freeing the allocated request.
  
  The existing errdefer was also too broad: after queueIo took ownership, a
  later setSelection or queueRender error could free the queued request.
  
  We now free requests in the return paths that still own them, and the
  errdefer has been removed.
  
  Also, activate a sequence only after encoding and queue append succeed
  so failure preserves the previous sequence state.
  ```
- [`8696bef`](https://github.com/ghostty-org/ghostty/commit/8696bef64486a51bb3b637c74d93a6f6079a900b) macos: guard fullscreen tab presentation ([@mitchellh](https://github.com/mitchellh))
  ```text
  #13611
  
  Route new-tab window presentation through an Objective-C exception catcher.
  
  AppKit can raise an NSInternalInconsistencyException while selecting a
  new tab in native fullscreen.
  
  Catch the presentation exception, report it through the existing error
  logging path, and leave Ghostty running when AppKit’s fullscreen window
  stack is inconsistent.
  
  This was pretty hard to reproduce but I was able to reproduce it about
  1/3rd of the time via AppleScript automation...
  ```
- [`bfd40c8`](https://github.com/ghostty-org/ghostty/commit/bfd40c84bd56965ab1a0e5112a4f3e380a31b18a) terminal: reset wrap state for CSI 2 K ([@mitchellh](https://github.com/mitchellh))
  ```text
  #13616
  
  Reset the soft-wrap state when CSI 2 K erases the complete cursor
  row. Previously, erase-to-end reset the flag while complete-line erase
  left it set.
  
  WezTerm, kitty, Alacritty, VTE, and xterm.js clear the wrap state for
  complete-line erase. xterm preserves it, but xterm copies physical rows
  during resize instead of reflowing them. Diverge from xterm so reflow in
  Ghostty does not treat erased rows as one logical line, and cover the
  behavior with a resize regression test.
  ```
- [`c247e45`](https://github.com/ghostty-org/ghostty/commit/c247e455c2b5f742ba837602ac31e85908dd1292) config: refill after ignored line boundaries ([@mitchellh](https://github.com/mitchellh))
  ```text
  Refill the line iterator when an ignored comment or blank line
  consumes the remaining buffered data.
  
  Configuration parsing previously stopped silently at these boundaries
  and left every subsequent setting unapplied.
  
  Request more data before continuing the loop and cover both comment
  and blank line boundaries with buffered-reader regression tests.
  ```
- [`713ad0e`](https://github.com/ghostty-org/ghostty/commit/713ad0eb18dc28c735c1c24f2d9a628fe5fd461f) config: refill after ignored line boundaries ([#13638](https://github.com/ghostty-org/ghostty/issues/13638)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes https://github.com/ghostty-org/ghostty/discussions/13441
  
  Refill the line iterator when an ignored comment or blank line consumes
  the remaining buffered data.
  
  Configuration parsing previously stopped silently at these boundaries
  and left every subsequent setting unapplied.
  
  Request more data before continuing the loop and cover both comment and
  blank line boundaries with buffered-reader regression tests.
  ```
- [`b1887bd`](https://github.com/ghostty-org/ghostty/commit/b1887bd71601b699a9678c92000969cac16874f6) terminal: reset wrap state for CSI 2 K ([#13637](https://github.com/ghostty-org/ghostty/issues/13637)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  #13616
  
  Reset the soft-wrap state when CSI 2 K erases the complete cursor row.
  Previously, erase-to-end reset the flag while complete-line erase left
  it set.
  
  WezTerm, kitty, Alacritty, VTE, and xterm.js clear the wrap state for
  complete-line erase. xterm preserves it, but xterm copies physical rows
  during resize instead of reflowing them. Diverge from xterm so reflow in
  Ghostty does not treat erased rows as one logical line, and cover the
  behavior with a resize regression test.
  ```
- [`d0659ba`](https://github.com/ghostty-org/ghostty/commit/d0659ba52192b1dc40c3cc671ba71aeb7780568f) macos: guard fullscreen tab presentation with objc catcher ([#13636](https://github.com/ghostty-org/ghostty/issues/13636)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  #13611
  
  Route new-tab window presentation through an Objective-C exception
  catcher.
  
  AppKit can raise an NSInternalInconsistencyException while selecting a
  new tab in native fullscreen.
  
  Catch the presentation exception, report it through the existing error
  logging path, and leave Ghostty running when AppKit’s fullscreen window
  stack is inconsistent.
  
  This was pretty hard to reproduce but I was able to reproduce it about
  1/3rd of the time via AppleScript automation...
  ```
- [`168c7b9`](https://github.com/ghostty-org/ghostty/commit/168c7b94672d91cded4b506143cb0ebebc5d1ceb) core: fix encoded key request cleanup ([#13635](https://github.com/ghostty-org/ghostty/issues/13635)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Encoded key requests are owned by the caller until they are added to a
  key sequence or queued for IO. The child_exited path and failed queue
  append returned without freeing the allocated request.
  
  The existing errdefer was also too broad: after queueIo took ownership,
  a later setSelection or queueRender error could free the queued request.
  
  We now free requests in the return paths that still own them, and the
  errdefer has been removed.
  
  Also, activate a sequence only after encoding and queue append succeed
  so failure preserves the previous sequence state.
  ```
- [`7a04755`](https://github.com/ghostty-org/ghostty/commit/7a047553c7ab35863a0bc10ea4bc029c9a4f1993) macos: avoid IOSurface leak on automated surface creation ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13444
  
  A close while AppKit temporarily cleared/changed a surface's window would
  leak the surface in the controller's pslit tree. This retained surface kept
  a bunch of resources around, particularly large IOSurfaces.
  
  This seems to only be reproducible under scripted load: rapid terminal
  creation/destruction so that destruction happens just while there is a nil
  window on a surface view.
  
  Track surface ownership in a weak controller map updated alongside the split
  tree, with validated fallbacks for existing attachment state. Resolve
  scripted and App Intent operations through that ownership, and route
  non-confirming root closes directly through the immediate tab or window close
  path so teardown always reaches the renderer.
  ```
- [`4b4a5b2`](https://github.com/ghostty-org/ghostty/commit/4b4a5b2411091ccda2cd6373631ec7ccd184c577) renderer/metal: clear callback before layer release ([@mitchellh](https://github.com/mitchellh))
  ```text
  Clear the IOSurfaceLayer display callback when releasing the wrapper.
  The host view can retain the backing layer beyond renderer teardown.
  This prevents a later Core Animation display pass from invoking the
  callback with a freed renderer context.
  ```
- [`a177ba9`](https://github.com/ghostty-org/ghostty/commit/a177ba90af18d5df91b2b5cb8dddc0a55905c37f) macos: tolerate display link creation failures ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13293
  
  Treat Core Video display link creation as optional when macOS has no
  active displays. The previous error path reported every creation
  failure as out of memory and aborted renderer initialization.
  
  This also resyncs the display link on any display change so when
  a display becomes available it re-adds itself.
  
  Tabs created while the session is locked now initialize normally and
  fall back to event-driven rendering without vsync.
  ```
- [`15ac61d`](https://github.com/ghostty-org/ghostty/commit/15ac61db164fd6b6fdef0163ebddf3e07db4842a) gtk: implement drag-to-move for splits ([#10423](https://github.com/ghostty-org/ghostty/issues/10423)) ([@jcollie](https://github.com/jcollie))
  ```text
  One major todo is moving splits across different split trees (i.e.
  moving across tabs and windows), but that would involve a lot more
  logic. This MVP version works for now.
  
  Video demo (somehow the encode quality is terrible - I'll fix this
  later):
  
  
  https://github.com/user-attachments/assets/a5029451-9641-4680-bff6-38f52ebded4b
  
  
  GTK version of #10090
  
  Closes #10224
  ```
- [`d166c05`](https://github.com/ghostty-org/ghostty/commit/d166c05edd5732b4eb2db907d18f14a2faff77a2) font: handle missing CoreText display names ([@mitchellh](https://github.com/mitchellh))
  ```text
  CTFontCopyDisplayName can return null.
  ```
- [`74f01cf`](https://github.com/ghostty-org/ghostty/commit/74f01cf5df5c3426c37951015500c92a20afdfa9) macos: prevent stale search selection crash ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13266
  
  Keep search text and its selection range synchronized as a single
  state transition.
  
  Deleting or replacing a search term could leave a String.Index range
  from the old value attached to the text field. Applying that range
  could crash the app.
  
  Clear selection before publishing new text.
  ```
- [`7a9c369`](https://github.com/ghostty-org/ghostty/commit/7a9c369cf5da72d41946f683c48b0466a210cb7e) terminal: preserve cursor when formatting tabstops ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13269
  
  Move VT tabstop serialization ahead of screen formatting so cursor-moving
  CHA and HTS sequences run before screen state is restored.
  
  Tabstop-enabled snapshots previously finished at the final configured
  tabstop instead of the serialized cursor position. Replaying a snapshot
  could resume input in the wrong column.
  
  Keep tabstop bytes in their original pin-map accounting and extend the
  round-trip test to verify tabstops, cursor position, and map length.
  ```
- [`2b32b5b`](https://github.com/ghostty-org/ghostty/commit/2b32b5b75cfe7a31a6043a82d111065b0279b875) core: close retained temp directory handles ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13219
  
  Screen file actions intentionally retain their temporary directory so
  the generated path remains valid after dispatch. The directory and
  parent handles were retained with it, while TempDir.deinit also left the
  parent handle open.
  
  Each successful action leaked two descriptors. Repeated screen,
  scrollback, or selection writes could exhaust the process descriptor
  limit and prevent new PTYs, tabs, and windows from opening.
  
  Give TempDir an exhaustive close mode that either deletes or retains its
  contents while always releasing both handles. Defer screen-file cleanup,
  retaining only after successful dispatch, and cover both lifecycle paths
  with descriptor tests.
  ```
- [`880eded`](https://github.com/ghostty-org/ghostty/commit/880eded1586d7414874025863bbd9ebede1027e5) macos: avoid IOSurface leak on automated surface creation ([#13640](https://github.com/ghostty-org/ghostty/issues/13640)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13444
  
  A close while AppKit temporarily cleared/changed a surface's window
  would leak the surface in the controller's pslit tree. This retained
  surface kept a bunch of resources around, particularly large IOSurfaces.
  
  This seems to only be reproducible under scripted load: rapid terminal
  creation/destruction so that destruction happens just while there is a
  nil window on a surface view.
  
  Track surface ownership in a weak controller map updated alongside the
  split tree, with validated fallbacks for existing attachment state.
  Resolve scripted and App Intent operations through that ownership, and
  route non-confirming root closes directly through the immediate tab or
  window close path so teardown always reaches the renderer.
  ```
- [`d28bc12`](https://github.com/ghostty-org/ghostty/commit/d28bc121a88def99cbc5ec8be1e18bc40f789325) macos: synchronize cached value access ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13276
  
  Make CachedValue safe for concurrent terminal content reads and expiry.
  
  The expiry task could previously release cached Swift String storage
  while another thread retained it, aborting the process during otherwise
  normal terminal use.
  
  Protect cached values and task handles with an NSLock, and exercise
  concurrent reads across repeated expiration in a regression test.
  ```
- [`57c1baf`](https://github.com/ghostty-org/ghostty/commit/57c1baf43ae5b576644879212ec6e9cc46284ff3) macos: defer overlapping clipboard completion ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #/13074
  
  Overlapping clipboard confirmations now defer denial until the next
  main queue turn rather than completing inside the confirmation callback.
  
  This prevents the native request state from being invalidated while its
  callback is still active, avoiding the OSC 52 crash reported in #13074.
  
  The deferred closure retains the originating surface view and completes
  the ignored request with empty data, preserving the existing deny
  behavior.
  ```
- [`bb1f590`](https://github.com/ghostty-org/ghostty/commit/bb1f5908f8ba737d0bccdc777b99aec2099f7d5f) terminfo: advertise overline support ([@mitchellh](https://github.com/mitchellh))
  ```text
  #12885
  
  Ghostty already implements SGR 53 and 55, but its terminfo description
  does not expose the corresponding Smol and Rmol capabilities. Add both
  entries so the advertised capabilities match the renderer.
  ```
- [`7cd2f65`](https://github.com/ghostty-org/ghostty/commit/7cd2f65f5cb3578d2751ae31bcbcf44189879430) terminal: color reset should set override to null, not default ([@mitchellh](https://github.com/mitchellh))
  ```text
  #12755
  
  Reset previously copied the active default into the override. This is
  wrong, a reset should unset the override and defer back to the default.
  
  Reset foreground, background, and cursor colors now resolve through the
  current default while explicit OSC overrides remain unchanged across
  configuration updates.
  
  Set a configured background in the OSC 11 regression, assert OSC 111
  clears its override, then change the default to verify the reset color
  follows it.
  ```
- [`e205647`](https://github.com/ghostty-org/ghostty/commit/e20564791e538249c99b65bf8457d3a29df9c981) libghostty-vt: spacer-tail handling needs to respect slow runtime safety ([@mitchellh](https://github.com/mitchellh))
  ```text
  Debug libghostty-vt dependencies embedded in ReleaseFast or ReleaseSmall
  binaries no longer panic when narrow text overwrites the tail of a wide
  glyph.
  
  Replace the root module's std.debug.runtime_safety gate with
  build_options.slow_runtime_safety so mixed optimization modes use the
  dependency's safety configuration consistently.
  ```
- [`b30387a`](https://github.com/ghostty-org/ghostty/commit/b30387a80f6a0aede4986251583fe1569c9819da) renderer/metal: clear callback before layer release ([#13641](https://github.com/ghostty-org/ghostty/issues/13641)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes https://github.com/ghostty-org/ghostty/discussions/13242
  
  Clear the IOSurfaceLayer display callback when releasing the wrapper.
  The host view can retain the backing layer beyond renderer teardown.
  This prevents a later Core Animation display pass from invoking the
  callback with a freed renderer context.
  
  This doesn't happen the way Ghostty GUI uses our renderer, but it is
  possible for folks using ghostty-internal and its straightforward and
  easy for us to fix it.
  ```
- [`71c2d68`](https://github.com/ghostty-org/ghostty/commit/71c2d68eb40d4e51d30d94e46e7b0c305aa4407f) macos: tolerate display link creation failures ([#13639](https://github.com/ghostty-org/ghostty/issues/13639)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13293
  
  Treat Core Video display link creation as optional when macOS has no
  active displays. The previous error path reported every creation failure
  as out of memory and aborted renderer initialization.
  
  Tabs created while the session is locked now initialize normally and
  fall back to event-driven rendering without vsync.
  ```
- [`b60970c`](https://github.com/ghostty-org/ghostty/commit/b60970ce250e9000f48e013ba9d1f9efb0316f49) macos: handle missing CoreText display names ([#13642](https://github.com/ghostty-org/ghostty/issues/13642)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes https://github.com/ghostty-org/ghostty/discussions/13262
  
  CTFontCopyDisplayName can return null.
  ```
- [`5033ea8`](https://github.com/ghostty-org/ghostty/commit/5033ea83d83c243b2eddc8a38745a791a52ee177) terminal: preserve cursor when formatting tabstops ([#13643](https://github.com/ghostty-org/ghostty/issues/13643)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13269
  
  Move VT tabstop serialization ahead of screen formatting so
  cursor-moving CHA and HTS sequences run before screen state is restored.
  
  Tabstop-enabled snapshots previously finished at the final configured
  tabstop instead of the serialized cursor position. Replaying a snapshot
  could resume input in the wrong column.
  
  Keep tabstop bytes in their original pin-map accounting and extend the
  round-trip test to verify tabstops, cursor position, and map length.
  ```
- [`0dcb411`](https://github.com/ghostty-org/ghostty/commit/0dcb41168123068d7f9a7e49b561789dcba870df) fix screen action fd leak from tempdir ([#13644](https://github.com/ghostty-org/ghostty/issues/13644)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13219
  
  Screen file actions intentionally retain their temporary directory so
  the generated path remains valid after dispatch. The directory and
  parent handles were retained with it, while TempDir.deinit also left the
  parent handle open.
  
  Each successful action leaked two descriptors. Repeated screen,
  scrollback, or selection writes could exhaust the process descriptor
  limit and prevent new PTYs, tabs, and windows from opening.
  
  Give TempDir an exhaustive close mode that either deletes or retains its
  contents while always releasing both handles. Defer screen-file cleanup,
  retaining only after successful dispatch, and cover both lifecycle paths
  with descriptor tests.
  ```
- [`78dec34`](https://github.com/ghostty-org/ghostty/commit/78dec345b25dfd9e4dbbcc4ba1d5ac040aae2204) terminfo: advertise overline support ([#13649](https://github.com/ghostty-org/ghostty/issues/13649)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  #12885
  
  Ghostty already implements SGR 53 and 55, but its terminfo description
  does not expose the corresponding Smol and Rmol capabilities. Add both
  entries so the advertised capabilities match the renderer. Tmux uses
  this to gate overline.
  ```
- [`1aeca67`](https://github.com/ghostty-org/ghostty/commit/1aeca6705eab280e12352e3866e3162002b242a0) terminal: color reset should set override to null, not default ([#13650](https://github.com/ghostty-org/ghostty/issues/13650)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  #12755
  
  Reset previously copied the active default into the override. This is
  wrong, a reset should unset the override and defer back to the default.
  
  Reset foreground, background, and cursor colors now resolve through the
  current default while explicit OSC overrides remain unchanged across
  configuration updates.
  
  Set a configured background in the OSC 11 regression, assert OSC 111
  clears its override, then change the default to verify the reset color
  follows it.
  ```
- [`9ed6142`](https://github.com/ghostty-org/ghostty/commit/9ed61428daa9f15b2dc89e73f9fe0d16d3a6bb71) libghostty-vt: spacer-tail handling needs to respect slow runtime safety ([#13651](https://github.com/ghostty-org/ghostty/issues/13651)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Debug libghostty-vt dependencies embedded in ReleaseFast or ReleaseSmall
  binaries no longer panic when narrow text overwrites the tail of a wide
  glyph.
  
  Replace the root module's std.debug.runtime_safety gate with
  build_options.slow_runtime_safety so mixed optimization modes use the
  dependency's safety configuration consistently.
  ```
- [`947e839`](https://github.com/ghostty-org/ghostty/commit/947e839930718fb1d4903f75aba5b314bb5fc1e4) macos: prevent stale search selection crash ([#13645](https://github.com/ghostty-org/ghostty/issues/13645)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13266
  
  Keep search text and its selection range synchronized as a single state
  transition.
  
  Deleting or replacing a search term could leave a String.Index range
  from the old value attached to the text field. Applying that range could
  crash the app.
  
  Clear selection before publishing new text.
  ```
- [`8524cb5`](https://github.com/ghostty-org/ghostty/commit/8524cb593c5fa542f017744c7879c22c66a5e377) terminal/kitty: fix point deletion calculations (d=p, d=c) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fix d=p and d=c point deletion so only placements intersecting the
  target cell are removed.
  
  Previously, placements spanning multiple rows could be deleted from
  columns outside the target because the page-order comparison flattened
  row and column coordinates.
  
  Check the rectangle's column independently and use page order only for
  its row span, matching Kitty's implementation:
  https://github.com/kovidgoyal/kitty/blob/master/kitty/graphics.c
  
  NOTE: I did not look at Kitty's source prior to fixing this. I only
  referenced it after the fix to verify that the behavior matches.
  
  Spec:
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#deleting-images
  ```
- [`f973bd5`](https://github.com/ghostty-org/ghostty/commit/f973bd53ba90f161c7629d01b195b0a7f2ed88a5) terminal: report overline in DECRQSS SGR response ([@mitchellh](https://github.com/mitchellh))
  ```text
  #11638
  
  Report SGR 53 when the active cursor style has overline enabled.
  ```
- [`c9ef382`](https://github.com/ghostty-org/ghostty/commit/c9ef382fc97d8256b9c5af3e8f13841896b0db15) macos: synchronize cached value access ([#13646](https://github.com/ghostty-org/ghostty/issues/13646)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13276
  
  Make CachedValue safe for concurrent terminal content reads and expiry.
  
  The expiry task could previously release cached Swift String storage
  while another thread retained it, aborting the process during otherwise
  normal terminal use.
  
  Protect cached values and task handles with an NSLock, and exercise
  concurrent reads across repeated expiration in a regression test.
  ```
- [`ae0ff51`](https://github.com/ghostty-org/ghostty/commit/ae0ff51c42f859b483b4a5a073b7fb4941f78273) macos: defer overlapping clipboard completion ([#13648](https://github.com/ghostty-org/ghostty/issues/13648)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13074
  
  Overlapping clipboard confirmations now defer denial until the next main
  queue turn rather than completing inside the confirmation callback.
  
  This prevents the native request state from being invalidated while its
  callback is still active, avoiding the OSC 52 crash reported in #13074.
  
  The deferred closure retains the originating surface view and completes
  the ignored request with empty data, preserving the existing deny
  behavior.
  ```
- [`a61e15e`](https://github.com/ghostty-org/ghostty/commit/a61e15efd563f7b21098561e8d282999b5634985) terminal/kitty: fix point deletion calculations (d=p, d=c) ([#13652](https://github.com/ghostty-org/ghostty/issues/13652)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes https://github.com/ghostty-org/ghostty/discussions/12346
  
  Fix d=p and d=c point deletion so only placements intersecting the
  target cell are removed.
  
  Previously, placements spanning multiple rows could be deleted from
  columns outside the target because the page-order comparison flattened
  row and column coordinates.
  
  Check the rectangle's column independently and use page order only for
  its row span, matching Kitty's implementation:
  https://github.com/kovidgoyal/kitty/blob/master/kitty/graphics.c
  
  NOTE: I did not look at Kitty's source prior to fixing this. I only
  referenced it after the fix to verify that the behavior matches.
  
  Spec:
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#deleting-images
  ```
- [`090d161`](https://github.com/ghostty-org/ghostty/commit/090d161b2855a0235771954c88059399dae6e058) terminal: report overline in DECRQSS SGR response ([#13653](https://github.com/ghostty-org/ghostty/issues/13653)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  #11638
  
  Report SGR 53 when the active cursor style has overline enabled.
  ```
- [`9cb2147`](https://github.com/ghostty-org/ghostty/commit/9cb21476411cba36844d3dd67373b11a9328f5e8) terminal/kitty: evict without scratch allocation ([#13627](https://github.com/ghostty-org/ghostty/issues/13627)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Track each image's placement count in its existing metadata. This lets
  us use constant-time usage checks (rather than scans) during eviction.
  
  Select the best candidate directly from storage on each eviction,
  preserving the existing priority order: unused status, transient hint,
  generation, then ID.
  
  Since eviction no longer allocates, it can't fail, so callers no longer
  need to handle out-of-memory conditions.
  ```
- [`e886012`](https://github.com/ghostty-org/ghostty/commit/e88601239d9ea8c4f93ad123e031f789c64eca3f) macOS: update command options match order ([#13624](https://github.com/ghostty-org/ghostty/issues/13624)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Matches are sorted in the following order:
  leadingColor > title > subtitle > description.
  
  Ranking is lexicographic on (colorScore, textScore)
  
  <img height="300" alt="image"
  src="https://github.com/user-attachments/assets/1ec99e67-537e-4fc6-b595-d7eec8cbf31d"
  />
  
  
  ### AI Disclosure
  
  Claude reviewed and added unit tests, also did some refactoring of my
  original implementation.
  ```
- [`f1d2250`](https://github.com/ghostty-org/ghostty/commit/f1d225020ae68b789b663b7b0637ac52c0a38a05) core: avoid allocating for small pwd change actions ([@jparise](https://github.com/jparise))
  ```text
  Surface.handleMessage allocated a null-terminated copy for every working
  directory update.
  
  Use a small 256-byte stack-fallback buffer for common working directory
  lengths without adding significant pressure to this deep call stack. Longer
  paths retain the existing heap behavior, and performAction continues to borrow
  the value only for the duration of the call.
  ```
- [`b5e86a4`](https://github.com/ghostty-org/ghostty/commit/b5e86a42844e8be67af67c7d612a058ed8cd340c) terminal/kitty: release evicted placement pins ([@ampagent](https://github.com/ampagent))
  ```text
  Image eviction removed associated placements from storage without
  deinitializing them. Pin-backed placements therefore remained registered
  with the screen after eviction, allowing graphics-heavy output to
  accumulate stale tracked pins.
  
  Pass the owning screen through image insertion and eviction, and
  deinitialize each placement before removing it. Cover both the released
  pin and a retained image's live pin in the eviction regression test.
  ```
- [`ea21a2f`](https://github.com/ghostty-org/ghostty/commit/ea21a2f141e309fffc549d8639479622d504051b) core: avoid allocating for pwd change actions ([#13654](https://github.com/ghostty-org/ghostty/issues/13654)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Surface.handleMessage allocated a null-terminated copy for every working
  directory update. OSC 7 values fit within the parser's 2 KiB fixed
  buffer, so use stack-fallback storage sized for that bound and its
  terminator.
  
  The message type does not enforce the OSC bound, so an oversized future
  producer still falls back to the heap. performAction already borrows the
  value only for the duration of the call, preserving its existing
  lifetime.
  ```
- [`8eecb8f`](https://github.com/ghostty-org/ghostty/commit/8eecb8fdbfcc21bfda31ee759ff3ef23216d80fb) terminal: release Kitty placement pins on eviction ([#13656](https://github.com/ghostty-org/ghostty/issues/13656)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Image eviction removed associated placements from storage without
  deinitializing them. Pin-backed placements therefore remained registered
  with the screen after eviction, allowing graphics-heavy output to
  accumulate stale tracked pins.
  
  Pass the owning screen through image insertion and eviction, and
  deinitialize each placement before removing it. Cover both the released
  pin and a retained image's live pin in the eviction regression test.
  ```
- [`f0f3f4d`](https://github.com/ghostty-org/ghostty/commit/f0f3f4d8d816836e8e527dc1938841462913a1fa) GTK: move audio bell processing to the application ([@jcollie](https://github.com/jcollie))
  ```text
  This fixes #13647 by using at most one GStreamer thread per application.
  This was previously addressed in #12815 which used at most one GStreamer
  thread per surface. Originally discussed in #12808.
  ```
- [`1d6bc68`](https://github.com/ghostty-org/ghostty/commit/1d6bc6829812a448ac6148e7e86e36dff30d19fb) lib: remove cutPrefix implementation ([@jparise](https://github.com/jparise))
  ```text
  We can use std.mem.cutPrefix directly now that we're on Zig 0.16.
  ```
- [`e1fc390`](https://github.com/ghostty-org/ghostty/commit/e1fc390c192ca2ebba6b61403bb335f0d03b4d2b) GTK: move audio bell processing to the application ([#13657](https://github.com/ghostty-org/ghostty/issues/13657)) ([@jcollie](https://github.com/jcollie))
  ```text
  This fixes #13647 by using at most one GStreamer thread per application.
  This was previously addressed in #12815 which used at most one GStreamer
  thread per surface. Originally discussed in #12808.
  ```
- [`63da4e8`](https://github.com/ghostty-org/ghostty/commit/63da4e84d49d34a026ff7771699db237de65c044) lib: remove backported cutPrefix implementation ([#13658](https://github.com/ghostty-org/ghostty/issues/13658)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  We can use std.mem.cutPrefix directly now that we're on Zig 0.16.
  ```
- [`e0ef934`](https://github.com/ghostty-org/ghostty/commit/e0ef934f736089efc60288caff1061a2ba82c2fc) termio: replace SegmentedPool with std.MemoryPool ([@mitchellh](https://github.com/mitchellh))
  ```text
  The purpose of SegmentedPool was pointer-stable values for the pty write
  path, and the std.MemoryPool provides that.
  
  SegmentedPool is actually so old it predates a stdlib memory pool!
  Just noting why I did it in the first place. I also wrote it when I was
  pretty fucking bad at Zig, so I'm shocked its lasted this long.
  
  The write path is hot , so the replacement was benchmarked against the old
  SegmentedPool plus a rewrite simple Pool I did before realizing...
  wait... why not just a MemoryPool. Benchmarked using the real 240-byte xev
  write request.
  
    workload                    old                     std.MemoryPool
    depth-1 (keystroke echo)    3.93 ns/op              0.96 ns/op
    burst (1MiB paste, d=256)   4.27 ns/op              1.00 ns/op
    cold growth (32 -> 16k)     4.54 ns/op              6.48 ns/op
    malloc create/destroy       15.9 ns/op              (baseline)
  
  Cold growth is slower but this is only a cost when the pool grows.
  
  Note this also gets rid of the preallocation, which didn't show any
  measurable performance benefit at all. This has the benefit of shrinking
  our ThreadData by ~10KB.
  ```
- [`f948d42`](https://github.com/ghostty-org/ghostty/commit/f948d4207655f31ae9b95fa039e73524df43cd13) termio: replace SegmentedPool with std.MemoryPool ([#13659](https://github.com/ghostty-org/ghostty/issues/13659)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  The purpose of SegmentedPool was pointer-stable values for the pty write
  path, and the std.MemoryPool provides that.
  
  SegmentedPool is actually so old it predates a stdlib memory pool! Just
  noting why I did it in the first place. I also wrote it when I was
  pretty fucking bad at Zig, so I'm shocked its lasted this long.
  
  The write path is hot , so the replacement was benchmarked against the
  old SegmentedPool plus a rewrite simple Pool I did before realizing...
  wait... why not just a MemoryPool. Benchmarked using the real 240-byte
  xev write request.
  
  ```
    workload                    old                     std.MemoryPool
    depth-1 (keystroke echo)    3.93 ns/op              0.96 ns/op
    burst (1MiB paste, d=256)   4.27 ns/op              1.00 ns/op
    cold growth (32 -> 16k)     4.54 ns/op              6.48 ns/op
    malloc create/destroy       15.9 ns/op              (baseline)
  ```
  
  Cold growth is slower but this is only a cost when the pool grows.
  
  Note this also gets rid of the preallocation, which didn't show any
  measurable performance benefit at all. This has the benefit of shrinking
  our ThreadData by ~10KB.
  
  This was motivated by #13655
  ````
- [`49fd1ae`](https://github.com/ghostty-org/ghostty/commit/49fd1ae654c97fbc4e6f7ba94b3ee8b563378e2c) build: default dependencies to lib-vt mode ([@mitchellh](https://github.com/mitchellh))
  ```text
  Related to #10651
  
  Default Ghostty dependency builds to libghostty-vt-only mode and
  avoid initializing anything that would trigger broader dependency
  requirements.
  
  The impact of this is that Zig consumers can import ghostty-vt without
  requiring Xcode on macOS.
  ```
- [`cfc19e8`](https://github.com/ghostty-org/ghostty/commit/cfc19e8053b96dbc9a7d7994b84ec6eef7eb17de) libghostty: add configurable mode defaults, remove mode_set/get ([@mitchellh](https://github.com/mitchellh))
  ```text
  ABI BREAKING: This removes `ghostty_terminal_mode_get` and `_mode_set`.
  We can now represent these operations completely with standard
  `ghostty_terminal_get` and `ghostty_terminal_set`, which makes it much
  more flexible to preserve ABI in the future.
  
  This is all centered around a new `GhosttyTerminalModeConfig` structure
  that is an in or out parameter depending on use case.
  
  This also adds a new `GHOSTTY_TERMINAL_OPT_MODE_DEFAULT` option that
  can be used to set the _default_ value of mode that happens when a RIS
  event (full reset) is sent.
  ```
- [`ec58fbc`](https://github.com/ghostty-org/ghostty/commit/ec58fbc6a2da89f6d17381d56ef316f29dbf789b) build: default dependencies to lib-vt mode to avoid Xcode requirements ([#13660](https://github.com/ghostty-org/ghostty/issues/13660)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Related to #10651
  
  Default Ghostty dependency builds to libghostty-vt-only mode and avoid
  initializing anything that would trigger broader dependency
  requirements.
  
  The impact of this is that Zig consumers can import ghostty-vt without
  requiring Xcode on macOS.
  ```
- [`301bd6f`](https://github.com/ghostty-org/ghostty/commit/301bd6f8b0251301f25f0943f85264fd8f6845e3) macOS: hide settings menu icon on macOS 27 ([@bo2themax](https://github.com/bo2themax))
  ```text
  Settings appears to be somehow special and it's not hidden previously.
  ```
- [`76907d8`](https://github.com/ghostty-org/ghostty/commit/76907d8de8c78f51d3c44a941772759da24cbc5f) macOS: remove flaky color match tests ([@bo2themax](https://github.com/bo2themax))
- [`33bdeed`](https://github.com/ghostty-org/ghostty/commit/33bdeed1cbc69196c10466d0c9d881c0a7a7ac9c) macOS: remove flaky color match tests ([#13667](https://github.com/ghostty-org/ghostty/issues/13667)) ([@mitchellh](https://github.com/mitchellh))
- [`99c483f`](https://github.com/ghostty-org/ghostty/commit/99c483f477dcf3d6523a976772dcac71ab9466d3) macOS: hide settings menu icon on macOS 27 ([#13664](https://github.com/ghostty-org/ghostty/issues/13664)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Settings appears to be somehow special and it's not hidden previously.
  
  This would require building with Xcode 27 tho.
  
  <img width="704" height="364" alt="image"
  src="https://github.com/user-attachments/assets/2cb23a01-6840-40a2-b794-6a8e914aaa7d"
  />
  ```
- [`afa9e4f`](https://github.com/ghostty-org/ghostty/commit/afa9e4fad065653a87e89e9ea75c54ee7fb3f94a) libghostty: add configurable mode defaults, remove mode_set/get ([#13661](https://github.com/ghostty-org/ghostty/issues/13661)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ABI BREAKING: This removes `ghostty_terminal_mode_get` and `_mode_set`.
  We can now represent these operations completely with standard
  `ghostty_terminal_get` and `ghostty_terminal_set`, which makes it much
  more flexible to preserve ABI in the future.
  
  This is all centered around a new `GhosttyTerminalModeConfig` structure
  that is an in or out parameter depending on use case.
  
  This also adds a new `GHOSTTY_TERMINAL_OPT_MODE_DEFAULT` option that can
  be used to set the _default_ value of mode that happens when a RIS event
  (full reset) is sent. Note that not all modes are configurable because
  some are set based on live terminal state and aren't modes in and of
  themselves.
  
  ## Why Delete Functions? Why Not Add?
  
  Once tagged, the goal of `libghostty-vt` is to remain HIGHLY ABI
  compatible. We are striving for top tier ABI compatibility similar to
  legendary C libraries. That means we need to be highly confident in our
  API shapes: functions, structs, etc. and using shapes that we can retain
  ABI compatibility even as we add features. Every function is a risk. By
  pushing stuff into our `_get/_set` patterns, its easier to maintain ABI
  compatibility.
  ```
- [`18f06ef`](https://github.com/ghostty-org/ghostty/commit/18f06ef03c8827cb2f794741c469b7091a2da112) macOS: fix unsupported action falls through wrong handling ([@bo2themax](https://github.com/bo2themax))
- [`1118773`](https://github.com/ghostty-org/ghostty/commit/111877354edd2c29a78f35c2023492d699454026) core,gtk: add move_tab_to_new_window action ([#13621](https://github.com/ghostty-org/ghostty/issues/13621)) ([@pluiedev](https://github.com/pluiedev))
  ```text
  Implements most of #2630
  
  This is in reality a really simple change and ideally we can get this
  out before the 1.4 string freeze
  ```
- [`22d1317`](https://github.com/ghostty-org/ghostty/commit/22d13172cde98a0a4dda05d3d6a3fcb0dd8ed018) macOS: fix unsupported action falls through wrong handling ([#13668](https://github.com/ghostty-org/ghostty/issues/13668)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  There're won't be any visible errors, but
  `keybind=cmd+r=toggle_tab_overview/toggle_window_decorations/size_limit/quit_time`
  shouldn't go to `showChildExited`
  
  ## AI Disclosure
  
  Found by Claude during another quest, but I changed on myself.
  ```
- [`a14eba7`](https://github.com/ghostty-org/ghostty/commit/a14eba7478fc1af4e6e0cf4a793728d308f3278f) input: update toggle_maximize documentation ([@claude](https://github.com/claude))
- [`c011ad8`](https://github.com/ghostty-org/ghostty/commit/c011ad87070a742b39eaffee800a006f3c977988) Update wording ([@bo2themax](https://github.com/bo2themax))
- [`e11bfb5`](https://github.com/ghostty-org/ghostty/commit/e11bfb513919c51d3f842a367c787ab026d8d868) macos: sync appearance when new windows are created ([#13324](https://github.com/ghostty-org/ghostty/issues/13324)) ([@zenangst](https://github.com/zenangst))
  ```text
  call `syncAppearance` after `super.showWindow` has been called to
  ensure that the window is visible.
  ```
- [`44a05a8`](https://github.com/ghostty-org/ghostty/commit/44a05a88aad347916fd2447bf29b637d553238b7) macos: discard debounced selection notification ([@mitchellh](https://github.com/mitchellh))
  ```text
  Discard the selection notification payload before debouncing
  accessibility changes.
  
  The debouncer previously retained the notification and its surface
  object, keeping a closed tab's view and PTY alive after the undo
  timeout.
  ```
- [`b9113d2`](https://github.com/ghostty-org/ghostty/commit/b9113d2e7f0a978003a82b9a2deb8b27e2f1bb80) build: fix flatpak/snap, restore rpath opt, fix local gtk4-layer-shell ([@vancluever](https://github.com/vancluever))
  ```text
  This fixes regressions in the flatpak/snap builds, and knock-on stuff
  that was discovered as as a result:
  
  * Update the Zig versions in the flatpak/snap build configuration files.
  * Restore the classic -Dpatch-rpath option, and add a new -Dpatch-interp
    option. This ensures that the snap can still use -Dpatch-rpath
    correctly.
  * There seems to be an issue in Zig when parsing IPv6 addresses that
    leads to issues loading resolv.conf files; when trying to load a
    nameserver that has an IPv6 address with a numeric interface index as
    the scoped zone ID, Zig will try to resolve the interface as a name
    rather than just use the index. This is coming up in snap builds
    because the build process seems to, by default, use the exhaustive
    /run/systemd/resolve/resolv.conf file, versus the simpler stub
    (stub-resolv.conf) file. We work around this for the time being by
    linking the stub at the end of the Zig part, overwriting the link to
    the non-stub file.
  * Fixed gtk4-layer-shell packaging - the migration to external
    translate-c meant that non-system builds of the dependency were not
    handing the local gtk4-layer-shell headers over for translation. Now,
    instead, we've extracted the management of the gtk4-layer-shell source
    and wayland-protocols generation to a locally-cached object so that
    the source can be shared by both C translation and the library build
    in a way that is not coupled to any particular step.
  ```
- [`f9b2ad8`](https://github.com/ghostty-org/ghostty/commit/f9b2ad8dbed93e0b8cdd6320d8f5a46ba15c5bc8) input: update toggle_maximize documentation ([#13673](https://github.com/ghostty-org/ghostty/issues/13673)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## AI Closure
  
  Claude found and changed it
  ```
- [`daeed25`](https://github.com/ghostty-org/ghostty/commit/daeed25b378d219268ad023e9a18b933a74b3250) font/coretext: creation functions can return null, handle OOM ([@mitchellh](https://github.com/mitchellh))
  ```text
  Catch NULL results from CoreFoundation/CoreText creation functions and
  return error.OOM rather than null derefs later. I verified that this is
  possible but didn't verify the behavior when it happens, this is just
  defensive based on the report here: #13671 because it costs us nothing
  really.
  ```
- [`219173a`](https://github.com/ghostty-org/ghostty/commit/219173ab370839889a191d3fd6855e53cb82e95d) terminal/snapshot: remove BLAKE3 digests ([@mitchellh](https://github.com/mitchellh))
  ```text
  Remove BLAKE3 prefix digests. Keep READY/FINISH as empty records since
  they're semantically important markers.
  
  Our existing format (CRC32 per-record, declared counts, strict tag ordering
  requirements, etc.) already detect: accidental corruption, truncation,
  data omission, and duplication.
  
  BLAKE3 only protects against valid records being swapped or removed entirely.
  It is heavy for just that, and callers can solve that anyways via their
  own transport (like, just use TCP). For more adversarial protection,
  callers can also add layers like TLS or their own alternate signing
  methods depending on their own threat models.
  
  Removing the hash improves encode times by ~1.4x, decode times by ~1.3x.
  Time-to-READY decoding is effectively unchanged because it was such a
  small package to begin with.
  ```
- [`987f442`](https://github.com/ghostty-org/ghostty/commit/987f44260d10a9f685d06f0ff638457aee64f2f2) cli: add g/G as vi-style aliases for Home/End in list-themes ([@bousii](https://github.com/bousii))
- [`7e567c3`](https://github.com/ghostty-org/ghostty/commit/7e567c3f03e914140f0b6beb8b03c20efcc03188) cli: add g/G as vi-style aliases for Home/End in list-themes ([#13681](https://github.com/ghostty-org/ghostty/issues/13681)) ([@jcollie](https://github.com/jcollie))
  ```text
  I was messing around with this tool the other day on a 60% keyboard so I
  thought this would be a nice addition for situations like that. Keeps in
  line with the vi/less j and k inputs that this tool has as well.
  ```
- [`9682685`](https://github.com/ghostty-org/ghostty/commit/96826853bde13bad0825cd0afe35584a0760d17a) macOS: fix window sizing after dragging a split into a window ([@bo2themax](https://github.com/bo2themax))
- [`fcee198`](https://github.com/ghostty-org/ghostty/commit/fcee19819e0a0fa6656ca8f3a946d193edf63cc9) macos: discard debounced selection notification ([#13676](https://github.com/ghostty-org/ghostty/issues/13676)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Discard the selection notification payload before debouncing
  accessibility changes.
  
  The debouncer previously retained the notification and its surface
  object, keeping a closed tab's view and PTY alive after the undo
  timeout.
  ```
- [`7f96e0b`](https://github.com/ghostty-org/ghostty/commit/7f96e0bdab175deb7205ec54e0c8a084283bf015) Update VOUCHED list ([#13683](https://github.com/ghostty-org/ghostty/issues/13683)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/13675#issuecomment-5218250080)
  from @jcollie.
  
  Vouch: @zenangst
  ```
- [`571c62d`](https://github.com/ghostty-org/ghostty/commit/571c62dada5da79f68d12d376957cc1d02d846b1) font/coretext: creation functions can return null, handle OOM ([#13679](https://github.com/ghostty-org/ghostty/issues/13679)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Catch NULL results from CoreFoundation/CoreText creation functions and
  return error.OOM rather than null derefs later. I verified that this is
  possible but didn't verify the behavior when it happens, this is just
  defensive based on the report here: #13671 because it costs us nothing
  really.
  ```
- [`faeac91`](https://github.com/ghostty-org/ghostty/commit/faeac91fa5ea91d855d623c551c18036dbaa0209) macOS: fix window sizing after dragging a split into a window ([#13682](https://github.com/ghostty-org/ghostty/issues/13682)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Regression from
  [#13601](https://github.com/ghostty-org/ghostty/issues/13601), but I
  don't see why it matters. But the surface's bounds changes after
  window's created.
  ```
- [`fd98370`](https://github.com/ghostty-org/ghostty/commit/fd98370211d5e1657a3430dde5ca1c59cb5f92ab) macOS: fix swiftlint ([@bo2themax](https://github.com/bo2themax))
- [`0a78672`](https://github.com/ghostty-org/ghostty/commit/0a78672e7cd4303588aada1d7bf2a6a28129cb65) build: fix flatpak/snap, restore rpath opt, fix local gtk4-layer-shell ([#13677](https://github.com/ghostty-org/ghostty/issues/13677)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This fixes regressions in the flatpak/snap builds, and knock-on stuff
  that was discovered as as a result:
  
  * Update the Zig versions in the flatpak/snap build configuration files.
  * Restore the classic `-Dpatch-rpath` option, and add a new
  `-Dpatch-interp` option. This ensures that the snap can still use
  `-Dpatch-rpath` correctly.
  * There seems to be an issue in Zig when parsing IPv6 addresses that
  leads to issues loading `resolv.conf` files; when trying to load a
  nameserver that has an IPv6 address with a numeric interface index as
  the scoped zone ID, Zig will try to resolve the interface as a name
  rather than just use the index. This is coming up in snap builds because
  the build process seems to, by default, use the exhaustive
  `/run/systemd/resolve/resolv.conf` file, versus the simpler stub
  (`stub-resolv.conf`) file. We work around this for the time being by
  linking the stub at the end of the Zig part, overwriting the link to the
  non-stub file.
  * Fixed `gtk4-layer-shell` packaging - the migration to external
  translate-c meant that non-system builds of the dependency were not
  handing the local `gtk4-layer-shell` headers over for translation. Now,
  instead, we've extracted the management of the `gtk4-layer-shell` source
  and `wayland-protocols` generation to a locally-cached object so that
  the source can be shared by both C translation and the library build in
  a way that is not coupled to any particular step.
  ```
- [`204989a`](https://github.com/ghostty-org/ghostty/commit/204989ad90e3ca104eb76e55a77afb185f2ed074) terminal/snapshot: remove BLAKE3 digests ([#13680](https://github.com/ghostty-org/ghostty/issues/13680)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Remove BLAKE3 prefix digests. Keep READY/FINISH as empty records since
  they're semantically important markers.
  
  Our existing format (CRC32 per-record, declared counts, strict tag
  ordering requirements, etc.) already detect: accidental corruption,
  truncation, data omission, and duplication.
  
  BLAKE3 only protects against valid records being swapped or removed
  entirely. It is heavy for just that, and callers can solve that anyways
  via their own transport (like, just use TCP). For more adversarial
  protection, callers can also add layers like TLS or their own alternate
  signing methods depending on their own threat models.
  
  Removing the hash improves encode times by ~1.4x, decode times by ~1.3x.
  Time-to-READY decoding is effectively unchanged because it was such a
  small package to begin with.
  
  **AI usage:** I had it clean up the comments and the tests, but I did
  the blake3 removal and marker changes, and wrote the commit message
  myself. All reviewed.
  ```
- [`34282fc`](https://github.com/ghostty-org/ghostty/commit/34282fc7b3ba3e7f42281db73647a83768710f89) macOS: fix swiftlint ([#13684](https://github.com/ghostty-org/ghostty/issues/13684)) ([@mitchellh](https://github.com/mitchellh))
- [`4693e1b`](https://github.com/ghostty-org/ghostty/commit/4693e1b546dfc00128d5fe83533def5a92c69ab0) macos: sync appearance when new windows are created ([#13675](https://github.com/ghostty-org/ghostty/issues/13675)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  For new windows to get their appearance synced, we need to call
  `syncAppearance` after `super.showWindow(sender)`. All previous calls to
  `syncAppearance` on `TerminalWindow` will be ignored because the window
  needs to have `isVisible` set to `true`.
  
  This regression was introduced by:
  5368adcd29754939e6c283198ef6b1c122293815
  
  It added `.dropFirst()` to the `focusedSurface` appearance publishers in
  `TerminalController.swift` which removes the initial call of the
  subscription.
  
  Fixes https://github.com/ghostty-org/ghostty/issues/13324
  
  (landed on the same fix as @rasitakyol found here:
  https://github.com/ghostty-org/ghostty/pull/13341)
  ```
- [`e83cf0b`](https://github.com/ghostty-org/ghostty/commit/e83cf0b06f504be8917292b180ac65b0de685ac0) macOS: fix quit alert missing when hidden ([@bo2themax](https://github.com/bo2themax))
- [`2602886`](https://github.com/ghostty-org/ghostty/commit/2602886144c7e95099c9e2ba07f181c69e7276f3) macOS: fix quit alert missing when hidden ([#13686](https://github.com/ghostty-org/ghostty/issues/13686)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes https://github.com/ghostty-org/ghostty/discussions/13685.
  
  Removed presumably deprecated check introduced in
  8f1a014afd9c6724b767b2fbf65d27d26b3c01e5 for update pill
  > I checked for auto update as well, it works as before this, and for
  manual updates we're not confirming anyway, so I think its safe to
  remove it now.
  
  Each BaseTerminalController already has quit check and confirming code
  added in that review windows pr. It didn't cover QT before, overriding
  it to animate in for showing alert.
  
  [#5450](https://github.com/ghostty-org/ghostty/issues/5450) stays fixed.
  
  
  
  
  https://github.com/user-attachments/assets/dbf36f16-e3ce-4f6a-bc25-367fe48739b9
  ```
- [`4714732`](https://github.com/ghostty-org/ghostty/commit/47147324cee9d12b537f0ea204bf16449d706b3a) Update VOUCHED list ([#13691](https://github.com/ghostty-org/ghostty/issues/13691)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/13690#issuecomment-5224579870)
  from @00-kat.
  
  Vouch: @a-lang
  ```
- [`034506f`](https://github.com/ghostty-org/ghostty/commit/034506f14562242c70618aaf5775366766653ffd) gtk: add +new-tab cli action ([@jcollie](https://github.com/jcollie))
- [`afb351f`](https://github.com/ghostty-org/ghostty/commit/afb351f8385d8b895671cb398d13fb39e06611f4) terminal/stream: fast-path APC termination ([@mitchellh](https://github.com/mitchellh))
  ```text
  APC payload bytes are bulk consumed, but the terminating byte still passed
  through the generic parser action loop. Handle ESC and C1 ST directly after
  bulk consumption while leaving other transitions on the scalar path.
  ```
- [`b537282`](https://github.com/ghostty-org/ghostty/commit/b537282411ae731f3d49705be391320ff5f51e9e) terminal/apc: support reporting unknown APC sequences ([@mitchellh](https://github.com/mitchellh))
- [`6e647a1`](https://github.com/ghostty-org/ghostty/commit/6e647a1cbd96175fee710a34c7116c06f0bf14b3) Update VOUCHED list ([#13697](https://github.com/ghostty-org/ghostty/issues/13697)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/13693#issuecomment-5227046478)
  from @tristan957.
  
  Vouch: @gotenksIN
  ```
- [`a6fc3e0`](https://github.com/ghostty-org/ghostty/commit/a6fc3e0e2e78aeb4219ce4ef6b866cc06b1b0e09) gtk/wayland: clean up blur regions ([@gotenksIN](https://github.com/gotenksIN))
  ```text
  Destroy temporary Wayland regions after each blur update and release
  the previous cached blur region before replacing it. This prevents
  resources from leaking while the blur region changes.
  ```
- [`136f436`](https://github.com/ghostty-org/ghostty/commit/136f436a3bbb14fd48d18e927a83fc6585d5a63c) gtk/wayland: clean up blur regions ([#13699](https://github.com/ghostty-org/ghostty/issues/13699)) ([@pluiedev](https://github.com/pluiedev))
  ```text
  Fix two resource leaks when the Wayland background blur region changes.
  
  Temporary `wl_region` objects were destroyed only after an error. They
  are now always destroyed after the blur request. The previous cached
  blur region is also released before its replacement.
  
  This change does not alter protocol selection or add new Wayland
  protocols.
  
  Testing:
  
  - Verified blur on KDE Plasma 6.7.4 with GTK 4.22.4.
  - Verified with `zig build -Doptimize=ReleaseFast`.
  
  This code was written with assistance from GPT 5.6 Sol and manually
  reviewed.
  ```
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
- [`16e13a5`](https://github.com/ghostty-org/ghostty/commit/16e13a59aeda57ccb1b9998ab989615960dbcafb) build: fix Linux Android SDK fallback path ([@fornwall](https://github.com/fornwall))
  ```text
  Use the standard ~/Android/Sdk capitalization for the Linux SDK fallback.
  
  This lets NDK discovery work when neither ANDROID_NDK_HOME nor an SDK
  environment variable is set.
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
- [`9d8fbd1`](https://github.com/ghostty-org/ghostty/commit/9d8fbd15b3b4e385b82c1a9e31cdbb99a74dabd6) gtk: add +new-tab action ([#11762](https://github.com/ghostty-org/ghostty/issues/11762)) ([@jcollie](https://github.com/jcollie))
  ```text
  This PR adds a `+new-tab` CLI action, useful for automation on GTK. This
  mainly re-uses machinery added for the `+new-window`, but adds in a
  unique surface ID for identifying surfaces for IPC purposes (and
  eliminates use of raw pointers for callbacks from notifications).
  ```
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
- [`49e4df7`](https://github.com/ghostty-org/ghostty/commit/49e4df78333ccdeb262e59d0f3c4de9d4b0bc7fd) macOS: rework for [#12712](https://github.com/ghostty-org/ghostty/issues/12712) and [#13645](https://github.com/ghostty-org/ghostty/issues/13645) ([@bo2themax](https://github.com/bo2themax))
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
- [`d6248a3`](https://github.com/ghostty-org/ghostty/commit/d6248a32dd724e1cd9c7f9b68c9360f3ad630d47) ghostty.h: mark as internal ([@pluiedev](https://github.com/pluiedev))
  ```text
  Its moniker has been `libghostty-internal` for *quite* a while now among
  maintainers but that has never really been clarified for the public aside
  from a couple comments on discussions. Judging by how many people still
  try to vibe their way into making this work for their purposes, I think
  we should clear this up once and for all.
  ```
- [`7e463bc`](https://github.com/ghostty-org/ghostty/commit/7e463bc65d430e8a8f0aa786abf83601cf2b9598) ghostty.h: mark as internal ([#13724](https://github.com/ghostty-org/ghostty/issues/13724)) ([@bo2themax](https://github.com/bo2themax))
- [`4b9d589`](https://github.com/ghostty-org/ghostty/commit/4b9d589bcb234b3fdd2160a3abf02cf9b647f328) macOS: disable text selection on macOS 15 ([@bo2themax](https://github.com/bo2themax))
- [`0c8ec22`](https://github.com/ghostty-org/ghostty/commit/0c8ec225b5a998792ddcbf626687cd3a28ec4523) macOS: remove unused menu validations ([@bo2themax](https://github.com/bo2themax))
- [`fd47b15`](https://github.com/ghostty-org/ghostty/commit/fd47b15cd4dad1152e17d13b8f79a0f1183c61f2) gtk: free hotkeys memory on app teardown ([@dkinzler](https://github.com/dkinzler))
  ```text
  Free array list memory in Hotkeys.deinit to avoid DebugAllocator
  throwing an error about leaked memory.
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
- [`8b7c57c`](https://github.com/ghostty-org/ghostty/commit/8b7c57c756115e519516698206b54ed80b49d1e7) gtk: add window title renaming ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes #10469 for GTK.
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
- [`f0e3be3`](https://github.com/ghostty-org/ghostty/commit/f0e3be3eefe104eeb119562499df45f4762995f9) macOS: support decoding the surrogate pair with UnicodeHexInput ([@bo2themax](https://github.com/bo2themax))
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
- [`09557e9`](https://github.com/ghostty-org/ghostty/commit/09557e91dc33907fb151b2791414d2c6153fd2e0) Update VOUCHED list ([#13739](https://github.com/ghostty-org/ghostty/issues/13739)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13738#discussioncomment-17968662)
  from @jcollie.
  
  Vouch: @PRIHLOP
  ```
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
- [`94d775f`](https://github.com/ghostty-org/ghostty/commit/94d775fefc21f74d9cc85a46b34c4e1d85318fd0) Update VOUCHED list ([#13743](https://github.com/ghostty-org/ghostty/issues/13743)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13742#discussioncomment-17970277)
  from @jcollie.
  
  Vouch: @dave92082
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
- [`426386b`](https://github.com/ghostty-org/ghostty/commit/426386b8579d5e558aa5d4cfdfb003ad06bc4fc5) Update VOUCHED list ([#13747](https://github.com/ghostty-org/ghostty/issues/13747)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13746#discussioncomment-17977627)
  from @jcollie.
  
  Vouch: @alex19EP
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
- [`fad7f85`](https://github.com/ghostty-org/ghostty/commit/fad7f854e8f976968bf4d61d408de9699cf87666) Update VOUCHED list ([#13754](https://github.com/ghostty-org/ghostty/issues/13754)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13753#discussioncomment-17980814)
  from @mitchellh.
  
  Vouch: @shorsher
  ```
- [`9f9b8d1`](https://github.com/ghostty-org/ghostty/commit/9f9b8d1d0525e63106cfc0ea19775056b205ffb5) Update VOUCHED list ([#13756](https://github.com/ghostty-org/ghostty/issues/13756)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13755#discussioncomment-17982722)
  from @jcollie.
  
  Vouch: @figelwump
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
- [`da8b171`](https://github.com/ghostty-org/ghostty/commit/da8b171265e0f9db09287e62e70e10afa0d44e9c) macOS: fix Sendable warning for UnsafeMutablePointer ([@bo2themax](https://github.com/bo2themax))
  ```text
  Swift explicitly [marked UnsafeMutablePointer as non sendable](https://github.com/swiftlang/swift/commit/0568dbf903bbd7c1278c029d7e4eaaad6a460002). Moving from `@unchecked @retroactive` to `nonisolated(unsafe)` is safe for us as per the previous comments
  ```
- [`97ae257`](https://github.com/ghostty-org/ghostty/commit/97ae257497ae687bca7f9c711e46c6937386480e) macOS: fix warnings in showUserNotification ([@bo2themax](https://github.com/bo2themax))
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
- [`c78226b`](https://github.com/ghostty-org/ghostty/commit/c78226bfaea1e03107d91c4e27c836f9d8143a7b) macOS:  fix Main actor-isolated static property 'find' warnings ([@bo2themax](https://github.com/bo2themax))
- [`cb7eaa0`](https://github.com/ghostty-org/ghostty/commit/cb7eaa059dbc4be7318a6071efc14b4891c628e6) macOS: silent weak ownership difference warnings ([@bo2themax](https://github.com/bo2themax))
  ```text
  UpdateViewModel doesn't own the Task, we don't actually need it here.
  ```
- [`7e3ddc2`](https://github.com/ghostty-org/ghostty/commit/7e3ddc2c891b1076caa235de9681a9b598bc3546) macOS: fix swift warnings ([#13762](https://github.com/ghostty-org/ghostty/issues/13762)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Rework for #12764
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
- [`4a516fa`](https://github.com/ghostty-org/ghostty/commit/4a516fa393932fe263bbca8d30740d17e40484f1) github: remove the issue templates ([@trag1c](https://github.com/trag1c))
- [`d2eeb73`](https://github.com/ghostty-org/ghostty/commit/d2eeb734b0dbf80954d1b630986746a5e9e194fd) github: remove the issue templates ([#13765](https://github.com/ghostty-org/ghostty/issues/13765)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  They're not needed anymore since the "New issue" button is now
  inaccessible to non-maintainers anyway.
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

