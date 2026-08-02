> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: August 2, 2026 at 15:56 UTC.

## August 2, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/30752310032), [2](https://github.com/ghostty-org/ghostty/actions/runs/30743972710)  
Summary: 2 runs • 12 commits • 6 authors

### Changes

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

## July 27, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/30304357049), [2](https://github.com/ghostty-org/ghostty/actions/runs/30295137203), [3](https://github.com/ghostty-org/ghostty/actions/runs/30286163644), [4](https://github.com/ghostty-org/ghostty/actions/runs/30281549818), [5](https://github.com/ghostty-org/ghostty/actions/runs/30270547633)  
Summary: 5 runs • 22 commits • 6 authors

### Changes

- [`c3655ba`](https://github.com/ghostty-org/ghostty/commit/c3655ba258d930b1eceae05a91a226a8f3720cb9) terminal: expose desktop notification effect ([@pearkes](https://github.com/pearkes))
- [`47d602c`](https://github.com/ghostty-org/ghostty/commit/47d602c422d180eb08627dd29f3386719fac7dcb) terminal: expose progress report effect ([@pearkes](https://github.com/pearkes))
- [`628adaf`](https://github.com/ghostty-org/ghostty/commit/628adaf30f54b7310a163fed164d72ea4391ed3c) terminal: share progress state enum ([@pearkes](https://github.com/pearkes))
- [`2729996`](https://github.com/ghostty-org/ghostty/commit/2729996eab608d19847f4d0c37508442bb3a2096) terminal: update event tests for constructor API ([@pearkes](https://github.com/pearkes))
- [`d0e72a3`](https://github.com/ghostty-org/ghostty/commit/d0e72a3ab654326bc1e5de07199cee229066ee19) font/sprite: update to z2d 0.12.1, use native path insetting ([@vancluever](https://github.com/vancluever))
  ```text
  This change updates z2d to 0.12.1 and changes the sprite font path
  insetting functionality to use the new path offset abilities released in
  the update.
  
  In addition, there has been a slight change to the drawing of E0B5 and
  its respective reflection; we now add a 1-pixel horizontal line segment
  to each end to force them to be perpendicular. This is because
  offsetting pre-expands the curves and ultimately causes the end segments
  of the curve itself to have slight non-horizontal angles, which produce
  small artifacts at the ends without the forced horizontal ends.
  ```
- [`eb9faed`](https://github.com/ghostty-org/ghostty/commit/eb9faed28beac3a0736dc4b6d3327ece78266c03) font/sprite: update to z2d 0.12.1, use native path insetting ([#13489](https://github.com/ghostty-org/ghostty/issues/13489)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This change updates z2d to 0.12.1 and changes the sprite font path
  insetting functionality to use the new path offset abilities released in
  the update.
  
  In addition, there has been a slight change to the drawing of E0B5 and
  its respective reflection; we now add a 1-pixel horizontal line segment
  to each end to force them to be perpendicular. This is because
  offsetting pre-expands the curves and ultimately causes the end segments
  of the curve itself to have slight non-horizontal angles, which produce
  small artifacts at the ends without the forced horizontal ends.
  ```
- [`2dd79f3`](https://github.com/ghostty-org/ghostty/commit/2dd79f3bc6af649e68422b08e21ad0300fd8b391) Expose additional events: desktop and progress ([#13483](https://github.com/ghostty-org/ghostty/issues/13483)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This exposes libghostty-vt callbacks for additional terminal events.
  
  * Desktop notifications from OSC 9/777
  * Progress reports from OSC 9;4, including state and optional percentage
  * Uses the `lib.Enum` progress state
  * Exposes both through the existing terminal option/effect API
  
  AI disclosure: Sol-5.6 was used extensively to write the code, I
  reviewed it personally.
  ```
- [`10e6ace`](https://github.com/ghostty-org/ghostty/commit/10e6ace6b66bddcee1a746c8d5fffb414209cf2a) GhosttyI18n: fix build on freebsd with zig 0.16 ([@svmhdvn](https://github.com/svmhdvn))
- [`c14cb51`](https://github.com/ghostty-org/ghostty/commit/c14cb5196adf4350e6b86f81c871502281016701) GhosttyI18n: fix build on freebsd with zig 0.16 ([#13485](https://github.com/ghostty-org/ghostty/issues/13485)) ([@jcollie](https://github.com/jcollie))
- [`28f02ac`](https://github.com/ghostty-org/ghostty/commit/28f02ac3ce1656f41134f53dc8bf8e3882e14507) Update VOUCHED list ([#13487](https://github.com/ghostty-org/ghostty/issues/13487)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/13485#issuecomment-5094118020)
  from @jcollie.
  
  Vouch: @svmhdvn
  ```
- [`f4c68d6`](https://github.com/ghostty-org/ghostty/commit/f4c68d65e5008b950c9a2aac9fa928b244dc3b99) terminal: support runtime scrollback limits ([@mitchellh](https://github.com/mitchellh))
  ```text
  Scrollback limits were fixed when a terminal screen was initialized.
  Move byte and line state and enforcement into a shared Limits type so
  PageList can update both constraints after initialization and resize.
  
  Add runtime setters to PageList and Terminal. Lowering a limit prunes
  eligible history immediately, while zero bytes switches the primary
  screen to no-scrollback behavior and clears retained history. Keep
  alternate screens unchanged.
  ```
- [`03d5fa2`](https://github.com/ghostty-org/ghostty/commit/03d5fa268902d609b2872178a1d5a4d9ff351ee7) lib-vt: move scrollback limits to terminal_set ([@mitchellh](https://github.com/mitchellh))
  ```text
  Terminal construction previously accepted GhosttyTerminalOptions with
  dimensions and one scrollback byte limit. Remove the options struct from
  the ABI and make ghostty_terminal_new accept columns and rows directly.
  
  Add byte and line limit options to ghostty_terminal_set and forward them
  to the runtime Terminal setters. NULL removes a limit, while zero bytes
  disables scrollback. Update type metadata, tests, and all API examples.
  ```
- [`a27e04e`](https://github.com/ghostty-org/ghostty/commit/a27e04e8f938be5a6b4c1831d78fea57fae5813f) lib-vt: readers for configured scrollback limits ([@mitchellh](https://github.com/mitchellh))
  ```text
  C API callers could configure runtime scrollback limits but could not
  read them back. Add terminal data keys for the primary screen byte and
  line configurations.
  
  Return GHOSTTY_NO_VALUE for unlimited limits and keep reads stable while
  an alternate screen is active. Document the configured-value semantics
  and add focused coverage for defaults, updates, and unlimited values.
  ```
- [`5fd2973`](https://github.com/ghostty-org/ghostty/commit/5fd2973b9a53ca639e82f1db178587f553dc6e0a) lib-vt: better docs for C options ([@mitchellh](https://github.com/mitchellh))
- [`5a35415`](https://github.com/ghostty-org/ghostty/commit/5a35415a5d59a117e654735ca5a01f876dec5841) libghostty: scrollback limits can be changed at runtime ([#13481](https://github.com/ghostty-org/ghostty/issues/13481)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  **This is an ABI breaking change for C libs.**
  
  Fixes https://github.com/ghostty-org/ghostty/issues/13268
  
  You can now change scrollback limits (bytes and lines) at runtime.
  
  This breaks the ABI but makes for a much more long-term pattern:
  `ghostty_terminal_new` now only takes viewport size, and you set
  scrollback configurations with the generic `ghostty_terminal_set`. The
  `GhosttyTerminalOptions` struct is fully removed. I think this will
  serve us much better over the long term.
  ```
- [`5b2d3b7`](https://github.com/ghostty-org/ghostty/commit/5b2d3b7df184b8395519baa235ee9539e2fb1a9b) terminal: limit scrollback by physical lines ([@mitchellh](https://github.com/mitchellh))
- [`86f81fb`](https://github.com/ghostty-org/ghostty/commit/86f81fb5b1e45a14281a23e556f916096093e3a3) terminal: expose scrollback line limit ([@mitchellh](https://github.com/mitchellh))
- [`10bc434`](https://github.com/ghostty-org/ghostty/commit/10bc43420cef8b5c8f1a4ac28b5a917d5c12b9cb) terminal: make scrollback byte limit optional ([@mitchellh](https://github.com/mitchellh))
- [`65c4821`](https://github.com/ghostty-org/ghostty/commit/65c48213b6ebbc7c8382d86ccf429101969040c4) config: expose scrollback line limit ([@mitchellh](https://github.com/mitchellh))
- [`1092204`](https://github.com/ghostty-org/ghostty/commit/1092204df19bf56eb5b983dcc44394a1855f111e) config: support unlimited scrollback limits ([@mitchellh](https://github.com/mitchellh))
- [`659a60a`](https://github.com/ghostty-org/ghostty/commit/659a60ae53e96e6303e50180fa68587b7cacc911) terminal/search: fix tests ([@mitchellh](https://github.com/mitchellh))
- [`739603b`](https://github.com/ghostty-org/ghostty/commit/739603b8a2b643b167031a99718127cc0ca311a5) Introduce `scrollback-limit-lines` to limit scrollback by lines instead of bytes ([#13473](https://github.com/ghostty-org/ghostty/issues/13473)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds a new config `scrollback-limit-lines` to limit scrollback by
  lines instead of bytes. This also renames `scrollback-limit` to
  `scrollback-limit-bytes` to make it clear what it does but we have a
  compatibility entry so old configurations will continue to work, so its
  not breaking.
  
  **This is NOT exclusive to `scrollback-limit-bytes`**. When both are
  set, then the _first limit reached_ is used. Since lines is affected by
  viewport size and bytes are affected by entries (more styles, more
  graphemes, etc.), they serve somewhat different purposes and it might be
  useful to set both.
  
  The default remains 50MB of bytes, unlimited lines.
  
  This is not exposed to libghostty yet. I have that coming as a follow up
  change.
  ```

