> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: July 10, 2026 at 11:46 UTC.

## July 10, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/29066195131), [2](https://github.com/ghostty-org/ghostty/actions/runs/29065831060)  
Summary: 2 runs • 10 commits • 3 authors

### Changes

- [`035ae8d`](https://github.com/ghostty-org/ghostty/commit/035ae8ddb683e7147f8ecd8878ad43e201a26ac3) build(deps): bump cachix/install-nix-action from 31.10.6 to 31.10.7 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [cachix/install-nix-action](https://github.com/cachix/install-nix-action) from 31.10.6 to 31.10.7.
  - [Release notes](https://github.com/cachix/install-nix-action/releases)
  - [Changelog](https://github.com/cachix/install-nix-action/blob/master/RELEASE.md)
  - [Commits](https://github.com/cachix/install-nix-action/compare/8aa03977d8d733052d78f4e008a241fd1dbf36b3...a49548c11d9846ad46ecc0115273879b045f001c)
  
  ---
  updated-dependencies:
  - dependency-name: cachix/install-nix-action
    dependency-version: 31.10.7
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`5bc6588`](https://github.com/ghostty-org/ghostty/commit/5bc6588e43e280b32049a18835414688a46bdb26) terminal/search: ignore empty search needles ([@mitchellh](https://github.com/mitchellh))
  ```text
  Low-level search state accepted an empty needle even though the search
  thread normally filters it out. SlidingWindow treated the empty string
  as a zero-length match and underflowed while calculating its inclusive
  end offset. Active and viewport overlap calculations could also
  underflow while loading adjacent pages.
  
  Treat an empty needle as an inactive search with no matches or history,
  and saturate the viewport overlap length.
  ```
- [`0ff4e41`](https://github.com/ghostty-org/ghostty/commit/0ff4e41b22b4da6e5603dd69570eabf4083c8ede) terminal: fix pin wrapping at row boundaries ([@mitchellh](https://github.com/mitchellh))
  ```text
  Pin.leftWrap and rightWrap calculated the destination using the
  remainder after consuming the current row. When that remainder was an
  exact multiple of the column count, rightWrap subtracted one from zero
  and leftWrap produced a column equal to the width. Dereferencing either
  pin could panic. A maximum usize offset on a one-column page also
  overflowed the row count.
  
  Base the row and column calculations on the remainder minus one. This
  maps exact multiples to the final cell of the correct row and keeps the
  maximum offset calculation in range so traversal reports overflow
  normally.
  ```
- [`0aaedf4`](https://github.com/ghostty-org/ghostty/commit/0aaedf4360ff3db1d724e148acc6f1c69d196c76) terminal: saturate origin cursor offsets ([@mitchellh](https://github.com/mitchellh))
  ```text
  setCursorPos added origin-mode margins to requested row and column
  values before clamping them to the scrolling region. A request near
  maxInt(usize) overflowed during that addition and crashed instead of
  landing on the region boundary.
  
  Use saturating addition for the origin offsets. The existing clamp then
  places oversized requests on the bottom-right margin without changing
  normal cursor positioning.
  ```
- [`6236d38`](https://github.com/ghostty-org/ghostty/commit/6236d3859c3687cbc25537d5ceabf1c6b56749bb) Misc runtime safety fixes ([#13275](https://github.com/ghostty-org/ghostty/issues/13275)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Runtime safety violating scenarios found by GPT 5.6. Verified each one
  manually. See each commit.
  
  I'm going to keep searching so not going to merge this yet.
  ```
- [`35e1a01`](https://github.com/ghostty-org/ghostty/commit/35e1a0160c4f6797e1bb1ef8e7a2b8c6b114ab58) build(deps): bump cachix/install-nix-action from 31.10.6 to 31.10.7 ([#13271](https://github.com/ghostty-org/ghostty/issues/13271)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [cachix/install-nix-action](https://github.com/cachix/install-nix-action)
  from 31.10.6 to 31.10.7.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/cachix/install-nix-action/releases">cachix/install-nix-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v31.10.7</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>nix: 2.34.7 -&gt; 2.34.8 by <a
  href="https://github.com/github-actions"><code>@​github-actions</code></a>[bot]
  in <a
  href="https://redirect.github.com/cachix/install-nix-action/pull/278">cachix/install-nix-action#278</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/cachix/install-nix-action/compare/v31.10.6...v31.10.7">https://github.com/cachix/install-nix-action/compare/v31.10.6...v31.10.7</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/a49548c11d9846ad46ecc0115273879b045f001c"><code>a49548c</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/install-nix-action/issues/278">#278</a>
  from cachix/create-pull-request/patch</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/147e749b5f8b678f21493ce9aa9cbecb5df69d6f"><code>147e749</code></a>
  nix: 2.34.7 -&gt; 2.34.8</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/23cf0fec1d55e0b1f2631aedd2a610c21ef8b077"><code>23cf0fe</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/install-nix-action/issues/276">#276</a>
  from cachix/dependabot/github_actions/actions/checkout-7</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/8bdfc70a3e5c0e108d7943e2bfe3d74fa0a4d095"><code>8bdfc70</code></a>
  chore(deps): bump actions/checkout from 6 to 7</li>
  <li>See full diff in <a
  href="https://github.com/cachix/install-nix-action/compare/8aa03977d8d733052d78f4e008a241fd1dbf36b3...a49548c11d9846ad46ecc0115273879b045f001c">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=cachix/install-nix-action&package-manager=github_actions&previous-version=31.10.6&new-version=31.10.7)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`f6f79ac`](https://github.com/ghostty-org/ghostty/commit/f6f79acce6c2805baeaa1b3a6bc4ab918b096c25) terminal: dispatch APC string bytes in bulk slices ([@rockorager](https://github.com/rockorager))
  ```text
  APC payloads such as Kitty graphics images can be megabytes of base64
  data, but every byte was dispatched individually: through the VT state
  machine table, an apc_put action, the stream handler, the APC protocol
  handler, and finally a per-byte ArrayList append in the Kitty command
  parser. Five layers of dispatch per byte made large image transfers
  far slower than they needed to be.
  
  Add a bulk fast path alongside the existing CSI fast paths in
  consumeUntilGround: scan the longest run of apc_put bytes (stopping
  at any byte the parse table doesn't treat as APC payload: CAN, SUB,
  ESC, and most C1 bytes exit or abort the string state, and 0xA0-0xFF
  are ignored by it) and dispatch the run as a single new apc_put_slice
  action. The APC handler identifies the protocol from the first few
  bytes as before, then passes the remainder of each slice to the
  protocol parser in bulk; the Kitty parser appends payload data with a
  single appendSlice. Ignored/unknown APC sequences now drop each slice
  in O(1) instead of per-byte dispatch.
  
  The fast path is guarded the same way as the CSI fast paths: handlers
  with a vtRaw hook (the inspector) keep receiving per-byte apc_put
  actions, and the scalar next() path is unchanged.
  
  Also add benchmark support: a `ghostty-gen +kitty` synthetic generator
  emitting well-formed Kitty graphics transmit commands with 4 KiB
  random base64 payloads (not valid image data; the corpus exercises
  the parsing paths, not image decoding), and a `ghostty-bench
  +apc-parser` benchmark that measures the stream -> APC -> Kitty parse
  path without image decode/storage.
  
  Benchmarks on a 64 MiB corpus (hyperfine, ReleaseFast, x86_64 Linux,
  baseline is identical source with only the fast path disabled):
  
    apc-parser:               1.061 s -> 43 ms  (~25x)
    terminal-stream (kitty):  1.163 s -> 72 ms  (~16x)
    terminal-stream (ascii):  no change
  
  The ascii case was verified with retired instruction counts (perf
  stat, pinned to one core) since wall time on the test machine has
  4-7 ms of noise: 988,030,458 vs 988,045,833 instructions (+0.0016%),
  a fixed startup-size delta; the ground-state hot loop never reaches
  the new branch.
  ```
- [`6275184`](https://github.com/ghostty-org/ghostty/commit/627518447395c9ff328e6ef8222f3a9409e4c40d) terminal/search: reset cached results after resize ([@mitchellh](https://github.com/mitchellh))
  ```text
  Screen searches only reset cached dimensions while feeding more
  history. Selecting or reloading a result immediately after a resize
  left flattened highlights pointing at page nodes freed by reflow. The
  next selection operation could dereference those stale pointers and
  crash.
  
  Centralize dimension invalidation and run it before feed, reload, and
  selection paths inspect cached state. Add regression coverage for
  selecting a cached active match after a column resize.
  ```
- [`7f073c4`](https://github.com/ghostty-org/ghostty/commit/7f073c4cf2cd892441f7b9ab401823435567cbd1) terminal: dispatch APC string bytes in bulk slices ([#13270](https://github.com/ghostty-org/ghostty/issues/13270)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  APC payloads such as Kitty graphics images can be megabytes of base64
  data, but every byte was dispatched individually: through the VT state
  machine table, an apc_put action, the stream handler, the APC protocol
  handler, and finally a per-byte ArrayList append in the Kitty command
  parser. Five layers of dispatch per byte made large image transfers far
  slower than they needed to be.
  
  Add a bulk fast path alongside the existing CSI fast paths in
  consumeUntilGround: scan the longest run of apc_put bytes (stopping at
  any byte the parse table doesn't treat as APC payload: CAN, SUB, ESC,
  and most C1 bytes exit or abort the string state, and 0xA0-0xFF are
  ignored by it) and dispatch the run as a single new apc_put_slice
  action. The APC handler identifies the protocol from the first few bytes
  as before, then passes the remainder of each slice to the protocol
  parser in bulk; the Kitty parser appends payload data with a single
  appendSlice. Ignored/unknown APC sequences now drop each slice in O(1)
  instead of per-byte dispatch.
  
  The fast path is guarded the same way as the CSI fast paths: handlers
  with a vtRaw hook (the inspector) keep receiving per-byte apc_put
  actions, and the scalar next() path is unchanged.
  
  Also add benchmark support: a `ghostty-gen +kitty` synthetic generator
  emitting well-formed Kitty graphics transmit commands with 4 KiB random
  base64 payloads (not valid image data; the corpus exercises the parsing
  paths, not image decoding), and a `ghostty-bench +apc-parser` benchmark
  that measures the stream -> APC -> Kitty parse path without image
  decode/storage.
  
  Benchmarks on a 64 MiB corpus (hyperfine, ReleaseFast, x86_64 Linux,
  baseline is identical source with only the fast path disabled):
  
    apc-parser:               1.061 s -> 43 ms  (~25x)
    terminal-stream (kitty):  1.163 s -> 72 ms  (~16x)
    terminal-stream (ascii):  no change
  
  The ascii case was verified with retired instruction counts (perf stat,
  pinned to one core) since wall time on the test machine has 4-7 ms of
  noise: 988,030,458 vs 988,045,833 instructions (+0.0016%), a fixed
  startup-size delta; the ground-state hot loop never reaches the new
  branch.
  
  AI Disclosure: This code was written with the assistance of Fable 5 via
  Amp.
  ```
- [`a23d90c`](https://github.com/ghostty-org/ghostty/commit/a23d90c89afa00fd5563a3db89d8a1cfab3e7573) terminal/search: reset cached results after resize ([#13274](https://github.com/ghostty-org/ghostty/issues/13274)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Screen searches only reset cached dimensions while feeding more history.
  Selecting or reloading a result immediately after a resize left
  flattened highlights pointing at page nodes freed by reflow. The next
  selection operation could dereference those stale pointers and crash.
  
  Centralize dimension invalidation and run it before feed, reload, and
  selection paths inspect cached state. Add regression coverage for
  selecting a cached active match after a column resize.
  ```

## July 9, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/29048787966), [2](https://github.com/ghostty-org/ghostty/actions/runs/29046999434), [3](https://github.com/ghostty-org/ghostty/actions/runs/29034451943)  
Summary: 3 runs • 26 commits • 4 authors

### Changes

- [`c62c159`](https://github.com/ghostty-org/ghostty/commit/c62c1598413fdf6b72a4b64aafa25e44b71a1915) terminal: add standalone LZ4 block codec ([@mitchellh](https://github.com/mitchellh))
  ```text
  Scrollback compression needs a codec that can be used from libghostty-vt
  without pulling in libc, and we need to measure it before integrating it
  with terminal page ownership.
  
  This adds an allocation-free raw LZ4 block codec in scalar Zig.  Callers
  provide the input, output, and fixed-size scratch table. The decoder
  uses an exact-size output contract so page metadata mismatches fail
  cleanly. Compatibility vectors, boundary cases, random round trips, and
  fuzz coverage exercise the block format.
  
  Also adds a page-compression benchmark that operates on reusable raw
  page corpora. Compression and decompression have separate modes with
  setup outside the timed region, plus a ratio report and no-op baseline.
  Nothing uses compression in the terminal yet; this is the isolated codec
  and measurement groundwork.
  ```
- [`ebc3ffd`](https://github.com/ghostty-org/ghostty/commit/ebc3ffd222f65765261cd30cfc2273643133ef89) terminal: add compressed page representation ([@mitchellh](https://github.com/mitchellh))
  ```text
  The standalone LZ4 codec had no representation for terminal page
  ownership or metadata, so PageList integration would otherwise need to
  reconstruct every Page field independently.
  
  Add compress.Page, which embeds the complete terminal Page while
  retaining its original virtual mapping and owns only an exact-sized
  encoded block. Compression is kept only when the encoded state is
  strictly smaller, and scratch output is capped at that profitability
  boundary so a future PageList caller can borrow a standard pool item.
  
  Extend the page-compression benchmark with a store mode that measures
  the encoded copy, allocation, bounded retention, and eviction path.
  Nothing uses compression from PageList yet; this remains isolated
  groundwork.
  ```
- [`f6fd4cb`](https://github.com/ghostty-org/ghostty/commit/f6fd4cb0878a04a96b67fc46be674f19f5883a13) terminal: generalize page memory reclamation ([@mitchellh](https://github.com/mitchellh))
  ```text
  PageList's virtual-memory helpers were tied to pool items even though
  the underlying decommit and recommit operations also apply to retained
  page mappings.
  
  Move the helpers into terminal/mem.zig and express their different
  failure contracts as generic modes. Zero mode preserves the existing
  pool invariant and fallbacks, while strict mode only succeeds when the
  operating system accepts reclamation and avoids touching memory that
  will be restored.
  
  PageList now uses the shared zero mode for its page pool. The strict
  path is tested in isolation and remains unused, so this does not enable
  page compression yet.
  ```
- [`421fe8d`](https://github.com/ghostty-org/ghostty/commit/421fe8dabe585aee5131e3960e492d29bd373043) terminal: integrate compressed pages into PageList ([@mitchellh](https://github.com/mitchellh))
  ```text
  PageList nodes previously exposed Page directly, so introducing a
  compressed representation would require every consumer to understand its
  state and ownership.
  
  Add resident and compressed node states behind a page access boundary.
  Content access transparently recommits and restores retained mappings,
  while metadata traversal stays compressed and lifecycle paths can
  discard encoded contents without decoding. Compression borrows pool
  memory for standard scratch and uses temporary aligned storage for
  oversized pages.
  
  Migrate terminal, rendering, search, formatting, and C API consumers to
  the new boundary. Hot grow, scroll, and print paths reuse resolved
  pages, with an explicit resident-only accessor where live cursor
  pointers prove that the page cannot be compressed.
  
  The compression entry point remains private with no production callers,
  so normal terminal behavior and scrollback accounting are unchanged.
  ReleaseFast terminal-stream comparisons across bulk output, scrolling,
  redraw, and erase workloads remain within 2% of the parent revision.
  ```
- [`9156ada`](https://github.com/ghostty-org/ghostty/commit/9156ada1692c7b6ac8408463639e3836af51f432) terminal: add cold-history compression pass ([@mitchellh](https://github.com/mitchellh))
  ```text
  PageList could compress individual nodes but had no policy-level
  operation for selecting pages that are safe to reclaim. The compressed
  state therefore remained reachable only from tests.
  
  Add a stateless pass that considers only complete history pages while
  the viewport follows the active area. It gates work on supported
  retained-mapping reclamation, reports attempts and retained bytes, and
  leaves restoration lazy when a resize pulls compressed history back into
  the active area.
  
  Add a live scrollback-compression benchmark for measuring complete
  PageList compression and restoration against saved VT corpora. The pass
  still has no production callers, and ReleaseFast terminal-stream
  comparisons remain within the existing throughput guardrail.
  ```
- [`70e788f`](https://github.com/ghostty-org/ghostty/commit/70e788f06677e36d1f0e8c1f21c3751531ac3246) terminal: add incremental scrollback compression ([@mitchellh](https://github.com/mitchellh))
  ```text
  Cold-history compression previously required scanning every eligible
  page in one call, which makes it unsuitable for an idle-time scheduler.
  The inspector also restored compressed pages while traversing collapsed
  entries, hiding the representation and undoing reclamation.
  
  Add caller-owned serial state that resumes compression without retaining
  node pointers. Each invocation inspects at most eight candidates and
  attempts one resident page. List mutations restart safely, while
  unsupported or historical viewports stop work. Keep a stateless
  whole-history operation for measurement.
  
  Expose metadata-only storage and memory accounting for diagnostics,
  update the inspector to restore only expanded pages, and add an
  incremental live scrollback benchmark. This remains disconnected from
  production scheduling.
  ```
- [`e7969ed`](https://github.com/ghostty-org/ghostty/commit/e7969ed43658b1330e282254cc1f0fe3805379f7) terminal: make PageList compression self-contained ([@mitchellh](https://github.com/mitchellh))
  ```text
  Incremental compression previously exposed its traversal state to
  callers, requiring them to coordinate the cursor with PageList lifetime
  and topology changes. Read-only consumers also had to restore compressed
  nodes to inspect their contents.
  
  Move the continuation state into PageList and expose a single mode-based
  compression entry point. Incremental passes restart safely across
  mutations and verify a no-work pass before becoming idle, while full
  passes leave incremental state fresh.
  
  Add preserved page reads which decode compressed nodes into caller-owned
  storage without changing their representation, and migrate the
  scrollback compression benchmark to the new API.
  ```
- [`0d015b2`](https://github.com/ghostty-org/ghostty/commit/0d015b2fcea547b698ef66c084d5946ec9c8f662) terminal: preserve compressed pages during search ([@mitchellh](https://github.com/mitchellh))
  ```text
  Search previously used the normal page access boundary while formatting
  history and checking soft-wrap boundaries. Inspecting compressed history
  therefore restored its retained mapping and undid the memory
  reclamation.
  
  Format through preserved page snapshots and copy row counts and wrap
  state into the sliding window's owned metadata. Overlap decisions reuse
  the same snapshot, so compressed pages are decoded at most once per
  append and remain compressed after matching.
  
  Add a cross-page regression which searches compressed history and
  verifies both source nodes retain their compressed representation.
  ```
- [`f8c217e`](https://github.com/ghostty-org/ghostty/commit/f8c217e557e5aee4275e29ba4fedc559d1c730f5) terminal: track pending scrollback compression ([@mitchellh](https://github.com/mitchellh))
  ```text
  PageList previously kept only traversal position, so callers had no
  central signal for deciding when an incremental compression pass should
  run. Scheduling policy had to infer work from output and UI activity.
  
  Track compression dirtiness alongside the PageList continuation state.
  Growth preserves valid progress while marking work pending, and resize
  or viewport transitions restart from the oldest page. A no-work
  verification pass clears the state.
  
  Expose Terminal helpers which report whether compression is required and
  run compression against primary scrollback even while the alternate
  screen is active. Unsupported retained-memory targets report no work.
  ```
- [`461562c`](https://github.com/ghostty-org/ghostty/commit/461562ca4ffe344dd1a6f7f24ab1f32fbb0fd448) terminal: enable idle scrollback compression ([@mitchellh](https://github.com/mitchellh))
  ```text
  Scrollback compression was available only through explicit PageList
  calls, so normal renderer-backed surfaces never reclaimed cold history.
  
  Debounce renderer wakeups with a one-shot timer and run bounded
  compression steps only when the terminal lock is immediately available.
  Timer state is isolated in the renderer and becomes idle once PageList
  reports that the pass is complete.
  
  Keep inspector reads representation-preserving by decoding compressed
  pages into temporary copies. Update the scrollback configuration and
  benchmark documentation to describe the production behavior and its
  memory accounting.
  ```
- [`b9bb50c`](https://github.com/ghostty-org/ghostty/commit/b9bb50c832378bf1a7f45538b4d117f3e4137ebf) terminal: optimize page compression codec ([@mitchellh](https://github.com/mitchellh))
  ```text
  The raw LZ4 codec previously kept one match candidate and extended and
  copied matches byte by byte. This limited compression quality and made
  page restoration substantially more expensive than the reference
  decoder.
  
  Pack two candidates into the existing 16 KiB table, accelerate long
  literal searches, and compare matching runs a word at a time. Decode
  short literals and common repeated patterns with fixed-width copies
  while retaining exact bounds checks for malformed blocks.
  
  This keeps the public API, workspace size, block format, and
  allocation-free dependency model unchanged.
  ```
- [`181254d`](https://github.com/ghostty-org/ghostty/commit/181254d36a14e563cf81690b31b275ada841171c) terminal: debounce compression by page activity ([@mitchellh](https://github.com/mitchellh))
  ```text
  Compression scheduling previously postponed its idle timer after every
  renderer wake. The inspector redraw loop wakes the renderer
  continuously, so opening it could prevent pending scrollback compression
  from ever starting.
  
  Track compression-relevant PageList activity with a wrapping 48-bit
  token and restart the timer only when the composite Terminal token
  changes. This removes the separate dirty bit while reserving 16 bits for
  future Terminal-owned compression triggers.
  
  Expose target availability through the terminal package and leave
  renderer compression state undefined on unsupported targets so its timer
  is never initialized.
  ```
- [`95685af`](https://github.com/ghostty-org/ghostty/commit/95685afd26813b5ad93c912199f39e6295a919a3) terminal: compress offscreen scrollback history ([@mitchellh](https://github.com/mitchellh))
  ```text
  Compression previously stopped whenever the viewport left the active
  area, leaving all scrollback resident while a user viewed history.
  
  Traverse complete historical pages through a metadata-only iterator
  which skips the contiguous visible range. Restart incremental traversal
  after every viewport movement so pages become eligible once they leave
  view, while visible pages remain resident for immediate redraw.
  
  Add a PageList-only drain mode for tests and benchmarks, and update
  scrollback documentation to describe the offscreen eligibility rule.
  ```
- [`0fb89f4`](https://github.com/ghostty-org/ghostty/commit/0fb89f4ffebabd7ea868f75a93f14a41ff65764a) terminal: configure scrollback compression ([@mitchellh](https://github.com/mitchellh))
  ```text
  Idle compression was always enabled on supported renderer-backed
  surfaces and the default logical scrollback limit remained sized for
  fully resident history.
  
  Add a default-on scrollback-compression option and make renderer
  scheduling honor it across config reloads. Existing compressed pages
  remain encoded when the option is disabled, while reenabling it starts a
  fresh idle pass.
  
  Raise the default logical scrollback limit from 10 MB to 50 MB and
  document typical physical-memory savings, content-dependent behavior,
  and retained virtual address usage.
  ```
- [`6d5dda4`](https://github.com/ghostty-org/ghostty/commit/6d5dda40db6e6fbde98064e0bd6ec3d2de29c928) inspector: clarify page compression memory ([@mitchellh](https://github.com/mitchellh))
  ```text
  The PageList overview mixed structural state with a long list of exact
  byte counters, making the compression result difficult to interpret.
  
  Keep the overview focused on grid and scrollback structure, and add a
  dedicated compression section before scrollbar details. Present page
  states, uncompressed size, encoded ratio, resident estimate, and savings
  using readable units and scoped help text.
  ```
- [`172f15d`](https://github.com/ghostty-org/ghostty/commit/172f15da3b904633f798d99cb6e43acd78cbdc79) terminal: expose compression through libghostty-vt ([@mitchellh](https://github.com/mitchellh))
  ```text
  Scrollback compression scheduling was only available to Zig callers that
  used Terminal directly, leaving C embedders unable to drive the same idle
  compression policy.
  
  Define ABI-aware mode and result enums on Terminal and export activity
  and compression operations through the C API. Keep scheduling
  caller-owned, validate C inputs, and document the incremental contract
  with a complete example.
  
  Report unsupported reclamation consistently for full passes so callers
  can disable compression on targets that cannot retain decommitted
  mappings.
  ```
- [`25e6245`](https://github.com/ghostty-org/ghostty/commit/25e62456914392344bc6d7e3bbd9fb5a3a50fbc5) renderer: avoid starving scrollback compression ([@mitchellh](https://github.com/mitchellh))
  ```text
  Inspector rendering can hold the terminal mutex while waking the
  renderer. When the compression scheduler failed to acquire that mutex,
  it treated every wake as possible terminal activity and restarted the
  idle timer. Frequent inspector frames could therefore postpone
  compression indefinitely until another interaction changed the timing.
  
  Keep an existing compression deadline when a wake encounters lock
  contention. The timer callback already rechecks both terminal activity
  and lock availability, while the first contended wake still arms a
  timer when none is active.
  ```
- [`9a4bd21`](https://github.com/ghostty-org/ghostty/commit/9a4bd2120a56073435c45c5249144817b400019a) terminal: optimize LZ4 decoding and add differential tests ([@mitchellh](https://github.com/mitchellh))
  ```text
  The block decoder previously copied literals through variable-length
  memcpy calls and expanded every match with word loops that carried an
  overcopy fallback in each branch. Real page blocks decode as millions
  of tiny sequences, so per-sequence overhead dominated restore time.
  
  Decode short literal runs and in-token matches with blind fixed-width
  copies whose margin checks subsume the exact bounds checks they
  replace. Expand small repeating periods into pattern-word stores,
  copy distant long matches with one exact memcpy, and propagate the
  rare non-power-of-two short offsets bytewise. Page corpora restore
  13% to 19% faster and text around twice as fast, while compressor
  output stays byte-for-byte unchanged.
  
  Replace the fuzz test with a differential property suite which
  round-trips generated inputs, validates blocks with an independent
  format walker, rejects wrong-size outputs, and decodes corrupted and
  truncated blocks. A light version runs as a normal unit test; the
  exhaustive version runs when GHOSTTY_LZ4_SLOW is set. An AGENTS.md
  records the benchmarking, testing, and verification workflow for
  this directory.
  ```
- [`7e02af8`](https://github.com/ghostty-org/ghostty/commit/7e02af87980bfdaad6d393b985d35c917476878e) terminal: scrollback page compression (70 to 90% memory savings) ([#13264](https://github.com/ghostty-org/ghostty/issues/13264)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds transparent compression for non-active/non-viewport scrollback
  pages, reducing physical memory for compressed pages by anywhere from
  70% to 90%. Compression is obviously highly dependent on the shape of
  the data, but these are the numbers I got for normal scrollback.
  
  Due to compression being available, I bumped the default scrollback
  limit from 10MB to 50MB. On average, a full scrollback still uses less
  memory than the prior limit due to the compression ratios.
  
  ## Demo
  
  Here is a demo video showing me filling my scrollback and using the
  inspector so you can see the live compression/decompression activity and
  results:
  
  
  https://github.com/user-attachments/assets/7b9d0383-42f7-47bf-8b3f-853e3f89549c
  
  ## Resident vs. Virtual Memory
  
  This PR works by lowering _resident/physicalmemory, but doesn't touch
  _virtual_ memory.
  
  Practically what this means is that users need to make sure they're
  looking at resident memory to see the change.
  
  We use OS primitives like `MADV_DONTNEED` on Linux or
  `MADV_FREE_REUSABLE` on Darwin to discard our physical memory, but
  retain our virtual memory allocations. This is awesome because it means
  our decompression is infallible: the OS has already given us the memory,
  but it just remaps it at that point.
  
  This is baked into the core implementation, so compression only works on
  systems that support an OS primitive to retain virtual mappings while
  discarding physical. Today, that is macOS and 64-bit Linux. Other
  operating systems have support we just haven't coded it up yet.
  
  ## Implementation
  
  A major refactor had to happen to PageList to represent nodes as either
  resident or compressed. Pins typically accessed node content directly so
  we had to add a bunch of helpers to read metadata without decompression
  (but some access requires it).
  
  Compression is relatively slow and its important we don't impact IO
  performance. So we support incremental compression passes and they only
  run when the terminal is idle (250ms timer on the render thread that
  resets on any activity). Benchmarks show zero regression in IO
  throughput on this change.
  
  In order to maintain the no-libc invariant for libghostty-vt, we use a
  hand-written (an AI assisted optimization) LZ4 compression
  implementation. The performance and compression ratio is _okay_. Its a
  good first step for this. I think in the future I want to look at other
  implementations we can bring in based on build configuration.
  
  ## Performance
  
  Measured with a saved 7.3 MB corpus made by repeating `gh --help` output
  into a 120x80 terminal with a 50 MB scrollback limit on my machine:
  
  | compression measurement | result |
  |-------------------------|--------|
  | pages compressed | 121 |
  | raw page backing | 49.56 MB |
  | encoded storage | 3.03 MB (6.11% of raw) |
  | estimated physical memory savings | 46.53 MB (93.89%) |
  | full compression | 30.3 ms total, 12.2 ms over the 18.1 ms no-op
  baseline (~101 µs/page) |
  | incremental drain | 29.7 ms total, 11.6 ms over baseline (~96 µs/page)
  |
  | compress and restore | 33.5 ms total, 3.2 ms over full compression
  (~26 µs/page to restore) |
  
  The workload above is especially repetitive, so its 6.11% encoded ratio
  is better than the 10% to 30% expected for text-heavy terminal history
  in general. Steady-state throughput is unchanged within noise
  (`terminal-stream` benchmarks and manual `cat` timings).
  
  ## libghostty-vt
  
  The same caller-driven compression controls are exposed to Zig and C.
  
  Note that compression _is not automatic_ for libghostty users. Callers
  must determine their own definition of "idle" and when to compress and
  call our incremental callback APIs to perform the compression.
  Decompression is automatic and as-needed (and will trigger
  recompression-required flags so callers are aware).
  
  ## LLM Notes
  
  This work was done in concert with Codex. I reviewed and
  rewrote/reshaped pretty much every change extensively, particularly
  PageList/Terminal. This PR message is written by hand, commit messages
  are LLM written but reviewed.
  ```
- [`d34b54e`](https://github.com/ghostty-org/ghostty/commit/d34b54e9b4ecdf17f5c161cc7fe5164a69be586e) renderer: hand off state mutex to avoid starving frames ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  The renderer state mutex is unfair on all platforms (os_unfair_lock
  on macOS, a futex based lock elsewhere). A thread that unlocks and
  right away locks again wins over a sleeping waiter, because the
  waiter first has to be woken up and scheduled. The termio parse
  thread does exactly this under heavy pty output: it relocks the
  mutex for every batch and never sleeps in between, so the renderer
  can starve in updateFrame for as long as the output lasts.
  
  Fix this by letting the parse thread stay off the lock until the
  renderer had its turn. `renderer.State` gets two atomics: a waiter
  count (`demand`) and a generation counter (`handoff_gen`). The renderer
  takes the mutex through lockDemand/unlockDemand which update these,
  and the parse thread calls yieldToDemand between batches. If a
  waiter exists it sleeps on a futex until the renderer took and
  released the lock, with a 1ms timeout so a lost wake can not stall
  IO forever.
  
  All the atomics are monotonic on purpose: they are only a hint for
  scheduling, the mutex still protects the terminal state itself.
  When the renderer is not waiting the cost for the parse loop is a
  single relaxed atomic load per batch.
  ```
- [`4f53b84`](https://github.com/ghostty-org/ghostty/commit/4f53b846bc19a47752cad946b842972abfc8e7aa) renderer: move State declaration to top of file ([@Uzaaft](https://github.com/Uzaaft))
- [`11b9a6e`](https://github.com/ghostty-org/ghostty/commit/11b9a6ef17e21b89e2ef14dd786992cc5577b69b) renderer: hand off state mutex to avoid starving frames ([#13265](https://github.com/ghostty-org/ghostty/issues/13265)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The mutex is unfair. From my understanding (after a brief convo with
  @rockorager), it's a race between the parse thread and the renderer
  thread.
  
  The parse thread is unlocking it then locking it faster than the
  renderer thread can get a lock/unlock. Under sustained pty output the
  parse thread never sleeps between batches, so the renderer's frame
  snapshot can starve for as long as the output lasts.
  
  The fix here makes the parse thread voluntarily stay off the lock until
  the renderer has had one turn by introducing two atomics:
  
  - `demand`: a waiter count. The renderer increments it before locking
  and decrements it after acquiring, so demand > 0 means "the renderer is
  queued on the lock or about to be."
  - `handoff_gen`: a generation counter. The renderer bumps it (with a
  futex wake) after unlocking, meaning "a waiter completed one full turn."
  
  At each batch boundary the parse thread checks demand (a single relaxed
  load in the common case, so this **should** cost nothing when the
  renderer isn't waiting). If a waiter exists, it futex-waits on
  handoff_gen until the renderer has taken and released the lock, bounded
  by a 1ms timeout, trying to ensure a lost wake can't stall IO.
  
  This is inspired from `parking_lot` form rust land, which has eventual
  fairness, but applied only at the one site that misbehaves.
  
  ## LLM Note
  
  I used Fable 5 in Amp to write the code, but only after I identified the
  problem myself from previous experience with mutex fairness (and the
  convo above with rockorager).
  
  The diagnosis — the parse thread barging the unfair mutex and starving
  the renderer — came first.Fable then traced the exact loop in
  `Exec.zig/generic.zig` and implemented the handoff protocol.
  
  I've reviewed the changes.
  ```
- [`60121a0`](https://github.com/ghostty-org/ghostty/commit/60121a039941ba79a7076a58fd6a0f75af695a76) Revert "termio: bound POSIX read-ahead on non-Darwin" ([@rockorager](https://github.com/rockorager))
  ```text
  This reverts commit bed47168ca7f34fe0a27e9f13c46b8df97cb77ca.
  ```
- [`b14d923`](https://github.com/ghostty-org/ghostty/commit/b14d9238366f87e1792a4363d60523ced10e310f) Revert "termio: bound POSIX read-ahead on non-Darwin" ([#13253](https://github.com/ghostty-org/ghostty/issues/13253)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This reverts commit bed47168ca7f34fe0a27e9f13c46b8df97cb77ca.
  
  This commit reduced the buffer size and count on non-Darwin. This
  introduced a ~20% perf loss on linux for high throughput loads on a
  questionable claim. Producers of bytes should not be pacing frames based
  on how fast they can write to the terminal.
  ```
- [`9c9cf3e`](https://github.com/ghostty-org/ghostty/commit/9c9cf3e8217471169563a29e6f0c3fd33a90f050) renderer: avoid allocating when there are no active links ([@jparise](https://github.com/jparise))
  ```text
  Determine if any links are active before building the string and
  byte-to-cell map. Those buffers scale with viewport size, and this
  function runs during frame updates, so avoid allocating them when the
  current mouse/modifier state can't highlight any regex links.
  
  This adds an additional `self.links` iteration, but that list is usually
  small, the "active" check is cheap, and it breaks on the first hit.
  ```
- [`7cb44fe`](https://github.com/ghostty-org/ghostty/commit/7cb44fea332efa74e3843e531fd1aa4e764a8e4d) renderer: avoid allocating when there are no active links ([#13258](https://github.com/ghostty-org/ghostty/issues/13258)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Determine if any links are active before building the string and
  byte-to-cell map. Those buffers scale with viewport size, and this
  function runs during frame updates, so avoid allocating them when the
  current mouse/modifier state can't highlight any regex links.
  
  This adds an additional `self.links` iteration, but that list is usually
  small, the "active" check is cheap, and it breaks on the first hit.
  
  ---
  
  GPT 5.5 spotted this and wrote the test case. I came up with the
  tradeoffs myself and wrote the runtime code.
  ```

## July 8, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/28965283998), [2](https://github.com/ghostty-org/ghostty/actions/runs/28919853743), [3](https://github.com/ghostty-org/ghostty/actions/runs/28916631760)  
Summary: 3 runs • 10 commits • 4 authors

### Changes

- [`0274e7a`](https://github.com/ghostty-org/ghostty/commit/0274e7ad843627aa097f77c531f4baf399247c5d) macos: fix quick terminal restoring stale size after display reconnect ([@quinnypig](https://github.com/quinnypig))
  ```text
  The quick terminal caches its last-closed window frame per display so it
  can restore the user's size when reopened. The cache entry was considered
  valid whenever the current screen was the same size *or larger* than when
  the frame was saved ("persist when screens grow"). This has led to a pattern
  that was simply maddening. To wit:
  
  That rule breaks across display changes. When an external display is
  disconnected and later reconnected at a different resolution (common
  after traveling with a laptop) the same display can come back larger
  than when the frame was cached. The stale frame is still treated as valid
  and restored, so the quick terminal no longer fills the screen (it appears
  at a partial width/height). Because the cache is persisted, restarting
  Ghostty does not clear it, and the user is slowly driven mad.
  
  Only treat a cached frame as valid when the screen geometry matches
  exactly (both backing scale factor and frame size). On any mismatch we
  drop the entry and fall back to the configured quick-terminal-size. Manual
  resizes are still remembered across toggles within a stable display
  configuration.
  
  Fixes the regression reported in #12348.
  ```
- [`f815f84`](https://github.com/ghostty-org/ghostty/commit/f815f8459421e4b53e6c4b9ba559a74e9dc62798) macos: fix quick terminal restoring stale size after display reconnect ([#13250](https://github.com/ghostty-org/ghostty/issues/13250)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  "Why is my quick terminal not taking up the entire top of my docked Mac
  screen after I reconnect?" Boy howdy are you in the right PR.
  
  It turns out that the quick terminal caches its last-closed window frame
  per display so it can restore the user's size when reopened. The cache
  entry was considered valid whenever the current screen was the same size
  *or larger* than when the frame was saved ("persist when screens grow").
  This has led to a pattern that was simply maddening. To wit: that rule
  breaks across display changes.
  
  When an external display is disconnected and later reconnected at a
  different resolution (common after traveling with a laptop, do not even
  get me started on projectors) the same display can come back larger than
  when the frame was cached. The stale frame is still treated as valid and
  restored, so the quick terminal no longer fills the screen (it appears
  at a partial width/height). Because the cache is persisted, restarting
  Ghostty does not clear it, and the user is slowly driven mad. Welcome to
  madness; we have snacks.
  
  This PR addresses this by treating a cached frame as valid when the
  screen geometry matches exactly (both backing scale factor and frame
  size). On any mismatch we drop the entry and fall back to the configured
  quick-terminal-size. Manual resizes are still remembered across toggles
  within a stable display configuration.
  
  Fixes the regression reported in #12348.
  
  AI disclaimer: I used AI for this. Of course I used AI for this, my code
  is terrible on a good day. Specifically, Claude Code, as well as a
  custom harness that has the curious tendency to write commit messages
  containing conspiracy theories about the code because I am history's
  greatest monster.
  
  Fight me!
  ```
- [`751a60d`](https://github.com/ghostty-org/ghostty/commit/751a60df61526ab71e32838f321ada374b3c1a43) macos: route IME preedit commits through key events ([@qappell](https://github.com/qappell))
- [`91f66da`](https://github.com/ghostty-org/ghostty/commit/91f66da24527fa02d92b5fd0b41cd020f553a64c) macos: route IME preedit commits through key events ([#13222](https://github.com/ghostty-org/ghostty/issues/13222)) ([@bo2themax](https://github.com/bo2themax))
- [`8307349`](https://github.com/ghostty-org/ghostty/commit/8307349ec5ff1502fc033869643b36f5173bf0a2) terminal: fix increaseCapacity growth from zero-capacity dimensions ([@mitchellh](https://github.com/mitchellh))
  ```text
  PageList.increaseCapacity grows a capacity dimension by doubling it.
  If the dimension is zero, doubling "succeeds" without growing: the
  page is reallocated and recloned with an identical capacity, violating
  the documented guarantee that we always increase by at least one unit.
  Every unbounded retry site (startHyperlink, cursorSetHyperlink, the
  reflow probes, insertLines/deleteLines) then loops forever reallocating
  a page per iteration, and the single-retry sites (styles, graphemes)
  fail their retry and silently drop data.
  
  No production page has a zero dimension today, which is why this has
  never fired: standard capacities are nonzero and doubling keeps them
  nonzero. But exactRowCapacity legitimately returns zero for dimensions
  with no content (a compacted plain text page has zero styles, grapheme,
  string, and hyperlink capacity), so any compaction work makes this
  reachable.
  
  Growth from zero now jumps straight to the standard default for the
  dimension rather than doubling. The default is what every standard
  page starts with, so single-retry callers are guaranteed enough room
  for their pending allocation, whereas doubling from a minimum unit
  could still come up short (a single grapheme can need multiple chunks,
  and a style set below capacity 3 cannot store anything).
  ```
- [`e44f5cb`](https://github.com/ghostty-org/ghostty/commit/e44f5cb0fa1aa02158e29b295833e1c3c024570e) terminal: guard RefCountedSet lookups against zero-capacity sets ([@mitchellh](https://github.com/mitchellh))
  ```text
  Layout.init(0) is an explicitly supported special case that produces a
  valid zero-capacity set with a zero-size table. But lookupContext had
  no guard for it: probing computes `table[hash & 0]` and reads whatever
  memory follows the set in its backing buffer, treating those bytes as
  an item ID which is then used to index the (also zero-size) items
  array, an out-of-bounds read reaching arbitrarily far past the set.
  
  This has never fired in practice because no production page carries a
  zero-capacity set today, and where one could occur the adjacent bytes
  happen to be zero (which reads as an empty bucket and returns null).
  Page.exactRowCapacity legitimately produces zero capacities for pages
  without styled or hyperlinked cells though, so any page compaction
  work makes this reachable with nonzero adjacent memory: in a Page
  layout the styles set can be followed by the grapheme bitmap, which
  is initialized to all ones.
  
  Lookups on a zero-capacity set now return null without touching the
  table. This also covers add, which looks up before inserting and
  already handles the zero capacity correctly after that point by
  returning OutOfMemory. All other entry points assert on valid IDs,
  which a zero-capacity set cannot have.
  ```
- [`c442eb4`](https://github.com/ghostty-org/ghostty/commit/c442eb4b308381aeabfbdbedc092e42eba806b66) terminal: document the pool reuse zeroing invariant ([@mitchellh](https://github.com/mitchellh))
  ```text
  PageList skips zeroing pooled page buffers in release builds, relying
  on the OS page allocator handing out zeroed pages and destroyNodeExt
  zeroing buffers before returning them to the pool. There is a hidden
  exception: std.heap.MemoryPool writes its free list node into the
  first pointer-size bytes of a free-listed buffer, so a reused buffer
  is not fully zero. This is only safe because the page rows array is
  laid out at offset 0, a page always has at least one row, and initBuf
  fully rewrites every row, overwriting the stale free list pointer.
  
  None of that was written down or checked anywhere, so a future layout
  reorder (or a zero-row page) would corrupt pages in release builds
  only, in a way that depends on pool reuse patterns. This adds a
  comptime assert that a Row covers at least a pointer, a runtime assert
  that pages always have at least one row, and comments tying the
  invariant together at the layout, initBuf, and pool reuse sites.
  
  Also fixes stale doc comments: deinit referenced a clonePool function
  that no longer exists, and Screen tests referenced increaseCapacity by
  its old adjustCapacity name.
  ```
- [`d3f4476`](https://github.com/ghostty-org/ghostty/commit/d3f4476dbfb770694aa8b53195b7a7337965b1fe) terminal: various PageList hardening for capacity edge cases ([#13244](https://github.com/ghostty-org/ghostty/issues/13244)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Each commit is standalone. This contains various unoffensive hardening
  of edge cases in PageList layout stuff. None of this is reachable today,
  but I'm just buttoning this up to experiment with compaction/compression
  of pages in various scenarios.
  ```
- [`896aca4`](https://github.com/ghostty-org/ghostty/commit/896aca499001f42e132f456ebc9cdfed616cf1fb) terminal: return free-listed page memory to the OS ([@mitchellh](https://github.com/mitchellh))
  ```text
  The PageList page pool never returns memory to the OS: destroyed pages
  are zeroed and free-listed until the surface exits. Any operation that
  shrinks the page count (clearing scrollback, pruning churn, resets,
  reflow) therefore retains its high-water RSS forever.
  
  Clearing a full scrollback keeps all of it resident, which at the default 10MB
  scrollback-limit is 10MB per terminal of memory that can never be
  used again for anything else.
  
  Lots of memes on the internet about this, and it turns out operating
  systems give us an answer for this (both Linux and macOS at least),
  so let's do it kids.
  
  Pool items can't be individually freed since they live inside arena
  chunks, but they are page-aligned and page-multiple sized, so we can
  decommit them while they sit in the free list. Our page-aligned
  allocation pays off, again!
  
  On Linux, madvise(MADV_DONTNEED) reclaims the pages immediately and
  guarantees zero-fill on the next touch, which also lets us skip the
  zeroing memset entirely, making destroy cheaper.
  
  On macOS, we zero in place and mark the item MADV_FREE_REUSABLE, which
  removes it from the process footprint immediately. Reuse is paired
  with MADV_FREE_REUSE when the pool hands a buffer back out so that
  footprint accounting stays correct. The zero invariant required by
  page reuse holds either way: reusable page contents are either
  preserved (our zeroes) or reclaimed and zero-filled by the kernel.
  
  Other platforms and test builds keep the existing memset behavior.
  
  ## LLM Notes
  
  Fable 5 found the retention behavior while re-analyzing scrollback
  memory, wrote the change and tests, and verified the madvise semantics
  empirically with memory probes on macOS and a real Linux kernel, plus
  before/after throughput benchmarks on both. I reviewed the analysis,
  the diff, rewrote the code to be more idiomatic Zig, and wrote this
  commit message you're reading.
  ```
- [`ad692f1`](https://github.com/ghostty-org/ghostty/commit/ad692f1e858b8c6475aec4539934526a8d783e6d) terminal: return free-listed page memory to the OS ([#13245](https://github.com/ghostty-org/ghostty/issues/13245)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This uses `madvise` flags on both macOS and Linux to mark our unused
  pool items as free memory and not show up in RSS (until they're actually
  used). We can do this since we do page-aligned/page-multiple
  allocations, heyo!
  
  Background: The PageList page pool never returns memory to the OS:
  destroyed pages are zeroed and free-listed until the surface exits. Any
  operation that shrinks the page count (clearing scrollback, pruning
  churn, resets, reflow) therefore retains its high-water RSS forever.
  Clearing a full scrollback keeps all of it resident, which at the
  default 10MB scrollback-limit is 10MB per terminal of memory that can
  never be used again for anything else.
  
  Lots of memes on the internet about this, and it turns out operating
  systems give us an answer for this (both Linux and macOS at least), so
  let's do it kids.
  
  On Linux, madvise(MADV_DONTNEED) reclaims the pages immediately and
  guarantees zero-fill on the next touch, which also lets us skip the
  zeroing memset entirely, making destroy cheaper.
  
  On macOS, we zero in place and mark the item MADV_FREE_REUSABLE, which
  removes it from the process footprint immediately. Reuse is paired with
  MADV_FREE_REUSE when the pool hands a buffer back out so that footprint
  accounting stays correct. The zero invariant required by page reuse
  holds either way: reusable page contents are either preserved (our
  zeroes) or reclaimed and zero-filled by the kernel.
  
  Other platforms and test builds keep the existing memset behavior.
  
  ## LLM Notes
  
  Fable 5 found the retention behavior while re-analyzing scrollback
  memory, wrote the change and tests, and verified the madvise semantics
  empirically with memory probes on macOS and a real Linux kernel, plus
  before/after throughput benchmarks on both. I reviewed the analysis, the
  diff, rewrote the code to be more idiomatic Zig, and wrote this commit
  message you're reading.
  ```

## July 7, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/28904916842), [2](https://github.com/ghostty-org/ghostty/actions/runs/28899078944), [3](https://github.com/ghostty-org/ghostty/actions/runs/28896482651), [4](https://github.com/ghostty-org/ghostty/actions/runs/28891474273), [5](https://github.com/ghostty-org/ghostty/actions/runs/28887370183), [6](https://github.com/ghostty-org/ghostty/actions/runs/28872066911), [7](https://github.com/ghostty-org/ghostty/actions/runs/28841679058), [8](https://github.com/ghostty-org/ghostty/actions/runs/28840138366), [9](https://github.com/ghostty-org/ghostty/actions/runs/28839347060)  
Summary: 9 runs • 22 commits • 6 authors

### Changes

- [`16e4b5e`](https://github.com/ghostty-org/ghostty/commit/16e4b5e98f10f255bdda934a61ff41e9b3a849c7) terminal: track page ownership explicitly on pagelist nodes ([@mitchellh](https://github.com/mitchellh))
  ```text
  PageList decided whether a page's backing memory belongs to the memory
  pool or the heap by comparing its length against std_size. This was super
  error-prone and the source of many bugs historically. We locked it down
  but its bothered me and has gotten in the way of another feature I've
  wanted to do: memory compaction.
  
  First, this commit records the ownership explicitly on each node and uses it
  everywhere ownership was previously inferred from size.
  
  Second, createPage gains an exact_size option that forces an exact-size
  heap allocation even when the layout would fit a pool item.
  
  Third, compact() now uses it to shrink any page to its minimum size,
  including standard pages. Nothing calls compact [YET!] but this is going
  to be the key to compressing scrollback history.
  
  This is groundwork for a ton of memory savings. Coming soon.
  ```
- [`39b3c47`](https://github.com/ghostty-org/ghostty/commit/39b3c4771701cf7b97b9d027fcd8416b7f59976e) terminal: track page ownership explicitly on pagelist nodes ([#13241](https://github.com/ghostty-org/ghostty/issues/13241)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  PageList decided whether a page's backing memory belongs to the memory
  pool or the heap by comparing its length against std_size. This was
  super error-prone and the source of many bugs historically. We locked it
  down but its bothered me and has gotten in the way of another feature
  I've wanted to do: memory compaction.
  
  First, this commit records the ownership explicitly on each node and
  uses it everywhere ownership was previously inferred from size.
  
  Second, createPage gains an exact_size option that forces an exact-size
  heap allocation even when the layout would fit a pool item.
  
  Third, compact() now uses it to shrink any page to its minimum size,
  including standard pages. Nothing calls compact [YET!] but this is going
  to be the key to compressing scrollback history.
  
  This is groundwork for a ton of memory savings. Coming soon.
  ```
- [`b953bb3`](https://github.com/ghostty-org/ghostty/commit/b953bb34630cbae71c6088d58e37745ae9b23119) terminal: fix bitmap allocator chunk region sizing ([@mitchellh](https://github.com/mitchellh))
  ```text
  BitmapAllocator.layout takes a capacity in bytes, but sized its chunk
  region as `aligned_cap * chunk_size`, reserving chunk_size times more
  memory than the bitmaps can ever address. As a result, the grapheme
  region of every standard page reserved 128 KiB with only 8 KiB
  reachable, and the string region 64 KiB with only 2 KiB reachable.
  About ~180 KiB of waste in every 576 KiB page.
  
  Results for a standard page:
  
  | region | before | after |
  |---|---|---|
  | grapheme allocator | 131,136 B | 8,256 B |
  | string allocator | 65,544 B | 2,056 B |
  | page total | 589,824 B (576 KiB) | 409,600 B (400 KiB) |
  
  30% less memory for every standard page in every terminal,
  including the preheated pages in the PageList pool.
  ```
- [`bc6ca3f`](https://github.com/ghostty-org/ghostty/commit/bc6ca3ff53bbb9c7f256ef235e67e22f95ea7ff7) terminal: fix bitmap allocator chunk region sizing ([#13240](https://github.com/ghostty-org/ghostty/issues/13240)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  BitmapAllocator.layout takes a capacity in bytes, but sized its chunk
  region as `aligned_cap * chunk_size`, reserving chunk_size times more
  memory than the bitmaps can ever address. As a result, the grapheme
  region of every standard page reserved 128 KiB with only 8 KiB
  reachable, and the string region 64 KiB with only 2 KiB reachable. About
  ~180 KiB of waste in every 576 KiB page.
  
  Results for a standard page:
  
  | region | before | after |
  |---|---|---|
  | grapheme allocator | 131,136 B | 8,256 B |
  | string allocator | 65,544 B | 2,056 B |
  | page total | 589,824 B (576 KiB) | 409,600 B (400 KiB) |
  
  30% less memory for every standard page in every terminal, including the
  preheated pages in the PageList pool.
  ```
- [`20a1bfa`](https://github.com/ghostty-org/ghostty/commit/20a1bfa5fd11c54a982d44566a843df0734cfb18) fix: pass RGB color inputs by pointer ([@elias8](https://github.com/elias8))
- [`14c8298`](https://github.com/ghostty-org/ghostty/commit/14c82988309b7bffb590d47ca0d05aabb093da42) terminal: report OSC color queries in lib-vt ([@mitchellh](https://github.com/mitchellh))
  ```text
  libghostty-vt already tracked OSC color state but ignored color queries in the standalone stream handler. This meant embedders that installed write_pty still received no response for OSC 4/10/11/12 or Kitty OSC 21 queries.
  
  Resolve the current terminal colors through shared Terminal helpers and encode replies through the write_pty effect. Xterm queries use the fixed 16-bit rgb form, preserve the request terminator, and fall back from cursor to foreground when no cursor color is set. Kitty color queries now report supported terminal-backed keys and return empty values for unset dynamic colors.
  
  Add RGB wire encoders and tests covering the stream handler and C API. The OSC parser now releases color operation request lists during reset, fixing an allocation leak exposed by multi-query OSC color tests.
  ```
- [`5a4f810`](https://github.com/ghostty-org/ghostty/commit/5a4f8106a3ce03be7eb9946e666eeead83c4729b) fix(lib-vt): pass RGB color inputs by pointer ([#13238](https://github.com/ghostty-org/ghostty/issues/13238)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes C ABI compatibility issue on arm64 macOS by passing color by
  reference instead of by value. I ran into an
  [issue](https://github.com/elias8/libghostty/actions/runs/28889437162/job/85698207979?pr=93)
  while working on the Dart bindings, where tests passed on Linux and
  x86_64 macOS locally, but failed on arm64 macOS. The Dart FFI appears to
  lower the argument (3 byte struct) differently on arm64 macOS. So the
  change addresses that by changing the arguments to by reference and
  aligns with the preexisting APIs.
  
  _AI disclosure: I used codex 5.5 to assist with debugging and making the
  changes. However, I have reviewed all changes manually and verified by
  running the tests both locally and on CI with the fix applied._
  ```
- [`3ff6d08`](https://github.com/ghostty-org/ghostty/commit/3ff6d08fad56f2d6b81420a27bdc56ee707b453e) lib-vt: report OSC and Kitty color queries ([#13239](https://github.com/ghostty-org/ghostty/issues/13239)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Hooks up responses to OSC and Kitty color queries if `write_pty` is set
  for libghostty.
  
  Also found a memory leak: the OSC parser now releases color operation
  request lists during reset.
  ```
- [`bb0ac4c`](https://github.com/ghostty-org/ghostty/commit/bb0ac4c723ec8b79a4d82e8a6c7fbbf8cd59794f) termio: don't bridge pty reads while the parser is idle ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes a frame time regression reported with fortio's `fps -fire`
  benchmark (fortio.org/terminal/fps): frame times nearly doubled at
  typical grid sizes after #13209 (the pipelined pty reader), and were
  more than 5x worse at small grids.
  
  ## The problem
  
  The `fps -fire` program follows a request/response pattern: write a
  frame, end it with a cursor position query (CSI 6n), and block until
  the reply arrives before starting the next frame.
  
  The gather stage treats any burst of 1 KiB or more as a saturated
  stream. When its spin retries come up dry, it sleeps in a 1ms poll
  expecting the writer's next refill so it can publish fewer, larger
  batches. But a frame-synced writer will never refill here: it is
  blocked waiting for a reply to a query that is sitting inside the
  very batch the gather stage is holding back. The poll always sleeps
  its full timeout, adding ~1.2ms to every round trip. Ouch!
  
  ## The fix
  
  Sleeping for a refill gap is only free while the parse stage is busy,
  since the wait hides behind parse time. Once the parser is idle,
  every additional microsecond spent bridging is added straight to
  output latency. So:
  
  1. When the spin retries exhaust and the parse stage is idle,
     deliver the batch immediately instead of polling.
  
  2. When the parse stage is busy, use a `pipe2` pipe to allow the parser
     to notify the gather thread it is idle. In the middle of the `poll`
     loop and sleep, we can get interrupted immediately and deliver
     the batch.
  
  The pipe is only written while the gather stage is actively polling, so an
  interactive terminal never pays the syscalls, and a saturated stream
  never idles the parser, preserving full batching and throughput for
  bulk output. Win, win, win!
  
  ## Benchmarks
  
  | workload | pre-#13209 | before | after |
  |---|---|---|---|
  | fps -fire 80x24 | 0.262 ms / 3674 fps | 1.435 ms / 694 fps | 0.234 ms / 4106 fps |
  | fps -fire 160x45 | 1.012 ms / 975 fps | 1.823 ms / 545 fps | 0.701 ms / 1405 fps |
  | fps -fire 284x68 | 2.443 ms / 407 fps | 2.391 ms / 414 fps | 1.351 ms / 732 fps |
  | cat 19.3 MB | 0.204 s (95 MB/s) | 0.086 s (224 MB/s) | 0.082 s (236 MB/s) |
  
  ## LLM Notes
  
  Bisect script written by hand and found the offending commit. Fable 5
  found the likely cause. I manually came up with the proposed solution and
  wrote it out. Fable helped benchmark for me to verify my assumptions
  conceptually and in the real world.
  ```
- [`e7a3a1f`](https://github.com/ghostty-org/ghostty/commit/e7a3a1fc8c7dd7d5c117c12fc66641ebc148ea16) termio: don't bridge pty reads while the parser is idle ([#13237](https://github.com/ghostty-org/ghostty/issues/13237)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes a frame time regression reported with fortio's `fps -fire`
  benchmark (fortio.org/terminal/fps): frame times nearly doubled at
  typical grid sizes after #13209 (the pipelined pty reader), and were
  more than 5x worse at small grids.
  
  ## The problem
  
  The `fps -fire` program follows a request/response pattern: write a
  frame, end it with a cursor position query (CSI 6n), and block until the
  reply arrives before starting the next frame.
  
  The gather stage treats any burst of 1 KiB or more as a saturated
  stream. When its spin retries come up dry, it sleeps in a 1ms poll
  expecting the writer's next refill so it can publish fewer, larger
  batches. But a frame-synced writer will never refill here: it is blocked
  waiting for a reply to a query that is sitting inside the very batch the
  gather stage is holding back. The poll always sleeps its full timeout,
  adding ~1.2ms to every round trip. Ouch!
  
  ## The fix
  
  Sleeping for a refill gap is only free while the parse stage is busy,
  since the wait hides behind parse time. Once the parser is idle, every
  additional microsecond spent bridging is added straight to output
  latency. So:
  
  1. When the spin retries exhaust and the parse stage is idle, deliver
  the batch immediately instead of polling.
  
  2. When the parse stage is busy, use a `pipe2` pipe to allow the parser
  to notify the gather thread it is idle. In the middle of the `poll` loop
  and sleep, we can get interrupted immediately and deliver the batch.
  
  The pipe is only written while the gather stage is actively polling, so
  an interactive terminal never pays the syscalls, and a saturated stream
  never idles the parser, preserving full batching and throughput for bulk
  output. Win, win, win!
  
  ## Benchmarks
  
  | workload | pre-#13209 | main | this PR |
  |---|---|---|---|
  | fps -fire 80x24 | 0.262 ms / 3674 fps | 1.435 ms / 694 fps | 0.234 ms
  / 4106 fps |
  | fps -fire 160x45 | 1.012 ms / 975 fps | 1.823 ms / 545 fps | 0.701 ms
  / 1405 fps |
  | fps -fire 284x68 | 2.443 ms / 407 fps | 2.391 ms / 414 fps | 1.351 ms
  / 732 fps |
  | cat 19.3 MB | 0.204 s (95 MB/s) | 0.086 s (224 MB/s) | 0.082 s (236
  MB/s) |
  
  ## LLM Notes
  
  Bisect script written by hand and found the offending commit. Fable 5
  found the likely cause. I manually came up with the proposed solution
  and wrote it out. Fable helped benchmark for me to verify my assumptions
  conceptually and in the real world. Commit message written by hand
  except for the benchmark results.
  ```
- [`bed4716`](https://github.com/ghostty-org/ghostty/commit/bed47168ca7f34fe0a27e9f13c46b8df97cb77ca) termio: bound POSIX read-ahead on non-Darwin ([@EriksRemess](https://github.com/EriksRemess))
  ```text
  The pipelined POSIX pty reader uses multiple large gather buffers to avoid
  stalling on Darwin, where pty reads are capped around 1KiB. On Linux this can
  let bulk terminal producers run too far ahead of terminal parsing/rendering.
  
  Frame-style terminal apps such as DOOM-fire can then report very high producer
  FPS while Ghostty displays stale frames from the buffered stream.
  
  Keep the Darwin-tuned 4 x 64KiB pipeline, but reduce non-Darwin read-ahead to
  2 x 8KiB so the pty can apply backpressure before multiple frames are queued.
  ```
- [`15a2edc`](https://github.com/ghostty-org/ghostty/commit/15a2edcbb93aa03a512cfe92b7bdca49ac1a9e98) termio: bound POSIX read-ahead on non-Darwin ([#13236](https://github.com/ghostty-org/ghostty/issues/13236)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The pipelined POSIX pty reader uses multiple large gather buffers to
  avoid stalling on Darwin, where pty reads are capped around 1KiB. On
  Linux this can let bulk terminal producers run too far ahead of terminal
  parsing/rendering.
  
  Frame-style terminal apps such as DOOM-fire can then report very high
  producer FPS while Ghostty displays stale frames from the buffered
  stream.
  
  Keep the Darwin-tuned 4 x 64KiB pipeline, but reduce non-Darwin
  read-ahead to 2 x 8KiB so the pty can apply backpressure before multiple
  frames are queued.
  
  AI disclosure: Codex gpt-5.5 xhigh helped.
  ```
- [`77190bd`](https://github.com/ghostty-org/ghostty/commit/77190bd02301e2666adf926a1b7a891dc2189353) terminal: handful of scroll region optimizations ([@mitchellh](https://github.com/mitchellh))
  ```text
  This optimizes scrolling inside a scroll region (DECSTBM).
  
  ## The changes
  
  1. **Stop creating scrollback for top-anchored regions on screens that don't
    retain scrollback.** `index()` routed any full-width region with `top == 0`
    through `cursorScrollAbove()`, which pushes the scrolled-out row into
    scrollback. Every scroll paid `PageList.grow()` plus amortized page pruning,
    which includes a 512 KB `memset` each time a page is recycled. These now
    use the in-place region scroll instead. CSI S gets the same routing fix.
    **Result: 1.05x-1.49x on the bottom-anchored region workloads, 1.25x on
    alt-screen full-screen scrolling.**
  
  2. **Add a specialized `Screen.cursorScrollRegionUp()` for the region scroll
     hot path.** The previous fast path (`PageList.eraseRowBounded`) paid
     per-scroll bookkeeping that exceeded the actual row work.
     The new function is built around the invariant that the cursor sits on the
     bottom row of a full-width region.
     **Result: 1.23x-1.24x on the top-anchored region workloads.**
  
  ## Benchmarks
  
  | workload | region (80 rows) | before | after | change |
  |---|---|---|---|---|
  | scrolling (control) | primary screen, no region | 237 ms | 235 ms | 1.0x |
  | scrolling_bottom_region | alt, rows 1-79 | 243 ms | 231 ms | 1.05x |
  | scrolling_bottom_small_region | alt, rows 1-40 | 311 ms | 208 ms | 1.49x |
  | scrolling_top_region | alt, rows 2-80 | 283 ms | 229 ms | 1.23x |
  | scrolling_top_small_region | alt, rows 40-80 | 258 ms | 208 ms | 1.24x |
  | alt screen full-screen scrolling | alt, no region | 288 ms | 230 ms | 1.25x |
  
  ## LLM Notes
  
  Assisted by Fable 5: it diagnosed the vtebench gap, wrote the benchmark
  harness payloads, profiled, and proposed hot paths. I manually wrote the
  hot path replacements and had it judge my work.
  ```
- [`160c3c6`](https://github.com/ghostty-org/ghostty/commit/160c3c69ea9a47961dfd973a8190b774048c20a1) terminal: handful of scroll region optimizations (minor) ([#13231](https://github.com/ghostty-org/ghostty/issues/13231)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This optimizes scrolling inside a scroll region (DECSTBM).
  
  We're squeezing blood out of a rock here. There just isn't much
  improvement to be had given our architecture for this case, but there
  were a couple things found that result in modest gains.
  
  ## Vtebench
  
  You can see the modest gains here. Still behind Alacritty (very very
  close).
  
  <img width="3558" height="2410" alt="CleanShot 2026-07-06 at 21 18
  39@2x"
  src="https://github.com/user-attachments/assets/3c800089-3510-4887-9872-e9926d686955"
  />
  
  
  ## The changes
  
  1. **Stop creating scrollback for top-anchored regions on screens that
  don't retain scrollback.** `index()` routed any full-width region with
  `top == 0` through `cursorScrollAbove()`, which pushes the scrolled-out
  row into scrollback. Every scroll paid `PageList.grow()` plus amortized
  page pruning, which includes a 512 KB `memset` each time a page is
  recycled. These now use the in-place region scroll instead. CSI S gets
  the same routing fix. **Result: 1.05x-1.49x on the bottom-anchored
  region workloads, 1.25x on alt-screen full-screen scrolling.**
  
  2. **Add a specialized `Screen.cursorScrollRegionUp()` for the region
  scroll hot path.** The previous fast path (`PageList.eraseRowBounded`)
  paid per-scroll bookkeeping that exceeded the actual row work. The new
  function is built around the invariant that the cursor sits on the
  bottom row of a full-width region. **Result: 1.23x-1.24x on the
  top-anchored region workloads.**
  
  ## Benchmarks
  
  | workload | region (80 rows) | before | after | change |
   |---|---|---|---|---|
  | scrolling (control) | primary screen, no region | 237 ms | 235 ms |
  1.0x |
  | scrolling_bottom_region | alt, rows 1-79 | 243 ms | 231 ms | 1.05x |
  | scrolling_bottom_small_region | alt, rows 1-40 | 311 ms | 208 ms |
  1.49x |
   | scrolling_top_region | alt, rows 2-80 | 283 ms | 229 ms | 1.23x |
  | scrolling_top_small_region | alt, rows 40-80 | 258 ms | 208 ms | 1.24x
  |
  | alt screen full-screen scrolling | alt, no region | 288 ms | 230 ms |
  1.25x |
  
  ## LLM Notes
  
  Assisted by Fable 5: it diagnosed the vtebench gap, wrote the benchmark
  harness payloads, profiled, and proposed hot paths. I manually wrote the
  hot path replacements and had it judge my work.
  ```
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

