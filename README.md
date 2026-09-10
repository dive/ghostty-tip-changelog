> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: September 10, 2026 at 07:48 UTC.

## September 10, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/34447229683)  
Summary: 1 runs • 1 commits • 1 authors

### Changes

- [`466439b`](https://github.com/ghostty-org/ghostty/commit/466439bdfc868da880d7abefbe698df35d05f9aa) Update VOUCHED list ([#14205](https://github.com/ghostty-org/ghostty/issues/14205)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14179#discussioncomment-18381789)
  from @jcollie.
  
  Vouch: @korikhin
  ```

## September 9, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/34400808728), [2](https://github.com/ghostty-org/ghostty/actions/runs/34396884567), [3](https://github.com/ghostty-org/ghostty/actions/runs/34375231118), [4](https://github.com/ghostty-org/ghostty/actions/runs/34370911324)  
Summary: 4 runs • 10 commits • 3 authors

### Changes

- [`8c17235`](https://github.com/ghostty-org/ghostty/commit/8c17235f8d1447ae3b5109d1c3a7d1256a9b2de4) Update VOUCHED list ([#14195](https://github.com/ghostty-org/ghostty/issues/14195)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14194#issuecomment-5608205535)
  from @trag1c.
  
  Vouch: @neoto
  ```
- [`f6cb831`](https://github.com/ghostty-org/ghostty/commit/f6cb8312b38088e4038296ecc5dde3f23c83fd94) tinyio: implement a Windows version and use it in the C API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Implements TinyIO for Windows which is used to save binary and runtime
  costs. As a reminder, binary costs are saved because `std.Io` uses a
  vtable so compilers can't prune any unused functions, so you pay for the
  full cost. We can noop unused functions to save. Runtime is saved
  because there is less state to carry for unused functionality like
  concurrency primitives.
  
  The impl itself is mostly taken from Zig directly. I ran tests on
  Windows (arm64) and verified everything works as expected so far!
  
  Binary size measurements before/after:
  
    | Mode         | Io owner        | ghostty-vt.dll | vs. Threaded |
    |--------------|-----------------|---------------:|-------------:|
    | ReleaseFast  | std.Io.Threaded |      2,209,280 |              |
    | ReleaseFast  | std.Io.failing  |      1,815,552 |     -393,728 |
    | ReleaseFast  | TinyIo          |      1,826,816 |     -382,464 |
    | ReleaseSmall | std.Io.Threaded |      1,541,632 |              |
    | ReleaseSmall | std.Io.failing  |      1,190,912 |     -350,720 |
    | ReleaseSmall | TinyIo          |      1,199,616 |     -342,016 |
  
  The runtime savings are relatively small, but 1KB per terminal ain't nothing:
  
    | Io owner        | Private, +100 terminals | Private, startup |
    |-----------------|------------------------:|-----------------:|
    | std.Io.Threaded |            +161,845,248 |          782,336 |
    | TinyIo          |            +161,742,848 |          729,088 |
  ```
- [`fde3449`](https://github.com/ghostty-org/ghostty/commit/fde3449b348d8e36c0d52fd39bb33ea66744b958) tinyio: implement a Windows version and use it in the C API ([#14193](https://github.com/ghostty-org/ghostty/issues/14193)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Implements TinyIO for Windows which is used to save binary and runtime
  costs. As a reminder, binary costs are saved because `std.Io` uses a
  vtable so compilers can't prune any unused functions, so you pay for the
  full cost. We can noop unused functions to save. Runtime is saved
  because there is less state to carry for unused functionality like
  concurrency primitives.
  
  The impl itself is mostly taken from Zig directly. I ran tests on
  Windows (arm64) and verified everything works as expected so far!
  
  Binary size measurements before/after:
  
    | Mode         | Io owner        | ghostty-vt.dll | vs. Threaded |
    |--------------|-----------------|---------------:|-------------:|
    | ReleaseFast  | std.Io.Threaded |      2,209,280 |              |
    | ReleaseFast  | TinyIo          |      1,826,816 |     -382,464 |
    | ReleaseSmall | std.Io.Threaded |      1,541,632 |              |
    | ReleaseSmall | TinyIo          |      1,199,616 |     -342,016 |
  
  The runtime savings are relatively small, but 1KB per terminal ain't
  nothing:
  
    | Io owner        | Private, +100 terminals | Private, startup |
    |-----------------|------------------------:|-----------------:|
    | std.Io.Threaded |            +161,845,248 |          782,336 |
    | TinyIo          |            +161,742,848 |          729,088 |
  ```
- [`7adbb51`](https://github.com/ghostty-org/ghostty/commit/7adbb5160d24bde9a65b5999d1ccd6ea4ec053b5) build/libghostty-vt: export uucode so that it can be re-used ([@jcollie](https://github.com/jcollie))
- [`60b4306`](https://github.com/ghostty-org/ghostty/commit/60b43068c5fc74c2117877b8ac4ecf9321bb8f24) terminal: reclaim pooled and compressed page memory on Windows ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds memory decommit/recommit support to Windows via
  DiscardVirtualMemory. This allows unused page memory to be reclaimed
  the same way it is already today on Linux and macOS.
  
  DiscardVirtualMemory releases the physical pages behind a committed
  range but leaves it committed, so a later access finds a zero page or
  the old contents rather than faulting, and nothing has to be committed
  again before reuse. That keeps recommit a no-op and, more importantly,
  keeps restoring a compressed page infallible.
  
  Windows has an alternative `VirtualFree(MEM_DECOMMIT)` followed by
  `VirtualAlloc(MEM_COMMIT)` which releases the commit charge as well, but
  Windows has no overcommit, so the commit can be refused on restore and our
  restore path doesn't support OOM.
  
  https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-discardvirtualmemory
  ```
- [`7644e6d`](https://github.com/ghostty-org/ghostty/commit/7644e6d627ede8042db16d264ed3d118d8832923) build/linghostty-vt: fix libvaxis access to uucode tables ([@jcollie](https://github.com/jcollie))
- [`95cfbbb`](https://github.com/ghostty-org/ghostty/commit/95cfbbb055c659f57da3650cfb733dbb5072f6a5) terminal: reclaim pooled and compressed page memory on Windows ([#14190](https://github.com/ghostty-org/ghostty/issues/14190)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds memory decommit/recommit support to Windows via
  DiscardVirtualMemory. This allows unused page memory to be reclaimed the
  same way it is already today on Linux and macOS.
  
  DiscardVirtualMemory releases the physical pages behind a committed
  range but leaves it committed, so a later access finds a zero page or
  the old contents rather than faulting, and nothing has to be committed
  again before reuse. That keeps recommit a no-op and, more importantly,
  keeps restoring a compressed page infallible.
  
  Windows has an alternative `VirtualFree(MEM_DECOMMIT)` followed by
  `VirtualAlloc(MEM_COMMIT)` which releases the commit charge as well, but
  Windows has no overcommit, so the commit can be refused on restore and
  our restore path doesn't support OOM.
  
  
  https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-discardvirtualmemory
  ```
- [`4a70ee4`](https://github.com/ghostty-org/ghostty/commit/4a70ee4718ba0967bcfd72f43adb715bf65a860d) build/libghostty-vt: fixed to the build system for programs that embed libghostty-vt and libvaxis ([#14191](https://github.com/ghostty-org/ghostty/issues/14191)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Two small patches that don't directly affect Ghostty, but do affect
  programs that embed `libghostty-vt` and `libvaxis`, or
  any other combination that also uses `uucode`.
  
  AI disclosure: these bugs were discovered/fixed by Claude, but I've
  rewritten parts of the patches and the comments.
  
  CC @rockorager
  ```
- [`0b54463`](https://github.com/ghostty-org/ghostty/commit/0b54463649eee14c0628cc7ab95065f8a299e73c) terminal/kitty: reject unsafe Windows paths for image file mediums ([@mitchellh](https://github.com/mitchellh))
  ```text
  The Kitty graphics file and temporary file mediums open a
  client-supplied path and the Kitty specification only specifies the
  blocklist for Unix-style machines.
  
  Windows has various unsafe paths as well that we should very obviously
  block. This diverges from the Kitty specification for now (I plan
  on reporting this upstream and asking for feedback) but I think its the
  right move for security.
  
  Windows dangerous namespaces:
  
    - A UNC path (`\\server\share\x`, also `//server/share/x`) makes the
      process resolve the host and authenticate to it over SMB.
    - The device namespaces (`\\.\`, `\\?\`, `\??\`) reach raw volumes and
      named pipes, where the open connects to something or blocks.
    - Reserved DOS device names (CON, NUL, COM1, ...) resolve to devices
      from inside any directory.
  
  These are now blocked.
  
  This commit also heap allocates the path buffer because max path on
  windows is around 100KB. :)
  ```
- [`cf4de79`](https://github.com/ghostty-org/ghostty/commit/cf4de795be50ec5bfe6675803a3371d4055f2beb) kitty: reject unsafe Windows paths for image file mediums ([#14189](https://github.com/ghostty-org/ghostty/issues/14189)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The Kitty graphics file and temporary file mediums open a
  client-supplied path and the Kitty specification only specifies the
  blocklist for Unix-style machines.
  
  Windows has various unsafe paths as well that we should very obviously
  block. This diverges from the Kitty specification for now (I plan on
  reporting this upstream and asking for feedback) but I think its the
  right move for security.
  
  Windows dangerous namespaces:
  
  - A UNC path (`\\server\share\x`, also `//server/share/x`) makes the
  process resolve the host and authenticate to it over SMB.
  - The device namespaces (`\\.\`, `\\?\`, `\??\`) reach raw volumes and
  named pipes, where the open connects to something or blocks.
  - Reserved DOS device names (CON, NUL, COM1, ...) resolve to devices
  from inside any directory.
  
  These are now blocked.
  
  This commit also heap allocates the path buffer because max path on
  windows is around 100KB. :)\
  
  **AI usage:** Fable and Astra both helped with validation, edge cases.
  ```

## September 8, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/34254983862), [2](https://github.com/ghostty-org/ghostty/actions/runs/34187628915)  
Summary: 2 runs • 9 commits • 4 authors

### Changes

- [`1ff027c`](https://github.com/ghostty-org/ghostty/commit/1ff027c3322864c3c28e701496c8e9d5c14cd4ee) i18n(hr): started updating hr translation ([@Filip7](https://github.com/Filip7))
  ```text
  Related issue #13766
  ```
- [`437dce2`](https://github.com/ghostty-org/ghostty/commit/437dce21bc4853b89af56daa88a5fd5af2911d75) Update hr.po ([@kristina8888](https://github.com/kristina8888))
  ```text
  added new translations for croatian language
  ```
- [`edf3aa0`](https://github.com/ghostty-org/ghostty/commit/edf3aa01bb4d4ce2544f58213eb98c0b90c99911) i18n(hr): added more translations and fixes ([@Filip7](https://github.com/Filip7))
- [`c01c683`](https://github.com/ghostty-org/ghostty/commit/c01c683eb0564b741de6f535e95c3ffc43aff59b) i18n(hr): "toggle" string translations ([@Filip7](https://github.com/Filip7))
  ```text
  i18n(hr): add missing translations and correct some others
  ```
- [`d1ed60d`](https://github.com/ghostty-org/ghostty/commit/d1ed60d569292c249ddfba42a91d452865c34762) Update hr.po ([@kristina8888](https://github.com/kristina8888))
- [`68852fc`](https://github.com/ghostty-org/ghostty/commit/68852fc008e0d14391fb284d3bbfb2276efd4033) i18n(hr): unify translation ([@Filip7](https://github.com/Filip7))
  ```text
  Use "zaslon" instead of "ekran"
  ```
- [`4480625`](https://github.com/ghostty-org/ghostty/commit/448062571c5edf010b7490d06869b88b5ebf8f80) i18n: Started updating hr translation ([#14019](https://github.com/ghostty-org/ghostty/issues/14019)) ([@trag1c](https://github.com/trag1c))
  ```text
  Related issue #13766
  ```
- [`dd2edd7`](https://github.com/ghostty-org/ghostty/commit/dd2edd760da6b90b01ef88f75e1bea8a71b31e3f) libvt: return safe pointers for empty output ([@mitchellh](https://github.com/mitchellh))
  ```text
  Normalize empty buffers and borrowed strings at the libghostty-vt C
  boundary to null pointers.
  
  Zig can use sentinel addresses such as 0x1 for empty slices. Returning
  these pointers to Go can cause a fatal invalid-pointer error when the
  runtime relocates a goroutine's stack, even though the length is zero.
  ```
- [`b0c421f`](https://github.com/ghostty-org/ghostty/commit/b0c421fcd2e290629d4285c181b52fe2f2095f06) libghostty: return safe pointers for empty output ([#14177](https://github.com/ghostty-org/ghostty/issues/14177)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Normalize empty buffers and borrowed strings at the libghostty-vt C
  boundary to null pointers.
  
  Zig can use sentinel addresses such as 0x1 for empty slices. Returning
  these pointers to Go can cause a fatal invalid-pointer error when the
  runtime relocates a goroutine's stack, even though the length is zero.
  ```

## September 7, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/34145900617), [2](https://github.com/ghostty-org/ghostty/actions/runs/34143207969), [3](https://github.com/ghostty-org/ghostty/actions/runs/34075296265), [4](https://github.com/ghostty-org/ghostty/actions/runs/34068510483)  
Summary: 4 runs • 11 commits • 5 authors

### Changes

- [`5909690`](https://github.com/ghostty-org/ghostty/commit/5909690de1d942c8b846dfd51c8a26e510436ade) config: rebuild RepeatableCommand's C mirror on clone ([@i999rri](https://github.com/i999rri))
  ```text
  Cloning value_c copied Command.C structs whose string pointers
  still referenced the source config's memory; once the source was
  freed, an embedded host reading the command list after a config
  replace (ghostty_config_clone + ghostty_config_free of the old
  one) hit use-after-free, caught by ASan. Rebuild the mirror from
  the cloned commands with the same cval path parseCLI uses, and add
  a regression test asserting the clone's C strings do not alias the
  source's.
  ```
- [`72cf508`](https://github.com/ghostty-org/ghostty/commit/72cf508551cb1c559c9ca32330e9647399031ebb) renderer: never stop the display link while holding the draw mutex ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #14150
  
  drawFrame called syncDisplayLink from its no-redraw path while still
  holding draw_mutex, and syncDisplayLink stops the CVDisplayLink when
  there is no work left. CVDisplayLinkStop is a blocking join on
  CoreVideo's IO thread. On macOS the apprt also calls drawFrame from the
  CoreAnimation layer display callback on the main thread, which takes
  the same mutex, so any CoreVideo stall inside that stop deadlocked.
  ```
- [`623106c`](https://github.com/ghostty-org/ghostty/commit/623106cc4ea9ad5b8cc070e5e5c5260eb6eeaa7b) config: rebuild RepeatableCommand's C mirror on clone ([#14170](https://github.com/ghostty-org/ghostty/issues/14170)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Why
  
  `RepeatableCommand.clone` copies `value_c` shallowly: the cloned
  `Command.C` structs keep string pointers into the *source* config's
  memory, so the clone only stays valid as long as its source lives. Every
  other field of a config clone is a deep copy — this is the one spot
  where the clone silently borrows.
  
  The macOS app never notices because of how it rotates configs: its
  clone's source is the core-owned live config, and both are replaced
  together on the next reload, so a clone never outlives its source. An
  embedder that clones a config and then frees the source — a legal
  sequence, e.g. promoting the clone to be the new active config — reads
  freed memory the next time it fetches `command-palette-entry` through
  the C API. Caught by AddressSanitizer.
  
  History: the shallow copy is as old as the C exposure itself.
  `dbe6035da` introduced `RepeatableCommand` with a correct deep `clone`
  (zig-side `value` only); `017021787` added the `value_c` mirror for
  `ghostty_config_get`, maintaining it carefully in `init`/`parseCLI` but
  extending `clone` with only the mechanical `ArrayList.clone` — the
  struct array copies, the string ownership doesn't. Nothing in-tree
  exercises clone-then-free-source, so it stayed latent.
  
  ## What
  
  Rebuild the C mirror from the cloned commands using the same
  `Command.cval` path `parseCLI` uses, so the clone's C strings live in
  the clone's own allocation. A regression test asserts the clone's C
  strings do not alias the source's while staying equal in content.
  
  ## AI disclosure
  
  Developed with AI assistance (Claude Code). The bug was found by
  AddressSanitizer while testing the Windows embedding host; the
  root-cause analysis, the fix, and the regression test were produced in
  an AI-assisted session, then reviewed and verified by the submitter
  (ASan clean after the fix, `RepeatableCommand` tests passing).
  ```
- [`82232ec`](https://github.com/ghostty-org/ghostty/commit/82232ecde55405559dec29c5466cb9e39938cb41) renderer: never stop the display link while holding the draw mutex ([#14171](https://github.com/ghostty-org/ghostty/issues/14171)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #14150
  
  drawFrame called syncDisplayLink from its no-redraw path while still
  holding draw_mutex, and syncDisplayLink stops the CVDisplayLink when
  there is no work left. CVDisplayLinkStop is a blocking join on
  CoreVideo's IO thread. On macOS the apprt also calls drawFrame from the
  CoreAnimation layer display callback on the main thread, which takes the
  same mutex, so any CoreVideo stall inside that stop deadlocked.
  ```
- [`258c057`](https://github.com/ghostty-org/ghostty/commit/258c057c0ac7d23b8a908fc1f4c5636670ccdcd1) build(deps): bump ryand56/r2-upload-action from 1.4 to 1.5 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [ryand56/r2-upload-action](https://github.com/ryand56/r2-upload-action) from 1.4 to 1.5.
  - [Release notes](https://github.com/ryand56/r2-upload-action/releases)
  - [Commits](https://github.com/ryand56/r2-upload-action/compare/b801a390acbdeb034c5e684ff5e1361c06639e7c...33ebb7a494b3a8a3c5ed2ea6bbdc72e707090317)
  
  ---
  updated-dependencies:
  - dependency-name: ryand56/r2-upload-action
    dependency-version: '1.5'
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`e9283ba`](https://github.com/ghostty-org/ghostty/commit/e9283ba872bfb2135dbaadea68d08980dbae5f88) build(deps): bump c-hive/gha-remove-artifacts from 1.4.0 to 1.8.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [c-hive/gha-remove-artifacts](https://github.com/c-hive/gha-remove-artifacts) from 1.4.0 to 1.8.0.
  - [Release notes](https://github.com/c-hive/gha-remove-artifacts/releases)
  - [Commits](https://github.com/c-hive/gha-remove-artifacts/compare/44fc7acaf1b3d0987da0e8d4707a989d80e9554b...62c2fbea931baa7dd4a6b73ea5a799984a818f61)
  
  ---
  updated-dependencies:
  - dependency-name: c-hive/gha-remove-artifacts
    dependency-version: 1.8.0
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`ccaf7c7`](https://github.com/ghostty-org/ghostty/commit/ccaf7c776144cb5200fa0de605159cb90788a286) build(deps): bump ryand56/r2-upload-action from 1.4 to 1.5 ([#14164](https://github.com/ghostty-org/ghostty/issues/14164)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [ryand56/r2-upload-action](https://github.com/ryand56/r2-upload-action)
  from 1.4 to 1.5.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/ryand56/r2-upload-action/releases">ryand56/r2-upload-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v1.5</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>chore(deps): update dependency <code>@​types/node</code> to v22.9.0
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/524">ryand56/r2-upload-action#524</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.686.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/526">ryand56/r2-upload-action#526</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.687.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/527">ryand56/r2-upload-action#527</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.688.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/528">ryand56/r2-upload-action#528</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.689.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/529">ryand56/r2-upload-action#529</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.691.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/530">ryand56/r2-upload-action#530</a></li>
  <li>chore(deps): update determinatesystems/nix-installer-action action
  to v16 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/531">ryand56/r2-upload-action#531</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.693.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/532">ryand56/r2-upload-action#532</a></li>
  <li>chore(deps): update dependency <code>@​vercel/ncc</code> to v0.38.3
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/534">ryand56/r2-upload-action#534</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.693.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/533">ryand56/r2-upload-action#533</a></li>
  <li>chore(deps): update dependency typescript to v5.7.2 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/537">ryand56/r2-upload-action#537</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.700.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/536">ryand56/r2-upload-action#536</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.701.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/538">ryand56/r2-upload-action#538</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.703.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/539">ryand56/r2-upload-action#539</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to v22.10.1
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/535">ryand56/r2-upload-action#535</a></li>
  <li>chore(deps): update dependency dotenv to v16.4.6 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/540">ryand56/r2-upload-action#540</a></li>
  <li>chore(deps): update dependency dotenv to v16.4.7 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/541">ryand56/r2-upload-action#541</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.705.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/542">ryand56/r2-upload-action#542</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.709.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/543">ryand56/r2-upload-action#543</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to v22.10.2
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/544">ryand56/r2-upload-action#544</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.712.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/545">ryand56/r2-upload-action#545</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.713.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/546">ryand56/r2-upload-action#546</a></li>
  <li>fix(deps): update dependency mime to v4.0.6 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/548">ryand56/r2-upload-action#548</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.715.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/547">ryand56/r2-upload-action#547</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.717.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/549">ryand56/r2-upload-action#549</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to v22.10.3
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/550">ryand56/r2-upload-action#550</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to v22.10.5
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/551">ryand56/r2-upload-action#551</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.722.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/552">ryand56/r2-upload-action#552</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.723.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/553">ryand56/r2-upload-action#553</a></li>
  <li>chore(deps): update dependency typescript to v5.7.3 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/554">ryand56/r2-upload-action#554</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.726.1 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/555">ryand56/r2-upload-action#555</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to v22.10.6
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/556">ryand56/r2-upload-action#556</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.731.1 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/557">ryand56/r2-upload-action#557</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to v22.10.7
  by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/558">ryand56/r2-upload-action#558</a></li>
  <li>chore(deps): update determinatesystems/magic-nix-cache-action action
  to v9 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/560">ryand56/r2-upload-action#560</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to
  v22.10.10 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/561">ryand56/r2-upload-action#561</a></li>
  <li>chore(deps): update dependency typescript to v5.8.2 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/564">ryand56/r2-upload-action#564</a></li>
  <li>ci(test-nix): replace magic nix cache with flakehub cache by <a
  href="https://github.com/ryand56"><code>@​ryand56</code></a> in <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/567">ryand56/r2-upload-action#567</a></li>
  <li>chore(deps): update dependency typescript to v5.8.3 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/566">ryand56/r2-upload-action#566</a></li>
  <li>fix(deps): update dependency mime to v4.0.7 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/565">ryand56/r2-upload-action#565</a></li>
  <li>chore(deps): update determinatesystems/nix-installer-action action
  to v17 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/569">ryand56/r2-upload-action#569</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.810.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/559">ryand56/r2-upload-action#559</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to
  v22.15.19 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/572">ryand56/r2-upload-action#572</a></li>
  <li>chore(deps): update stefanzweifel/git-auto-commit-action action to
  v6 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/576">ryand56/r2-upload-action#576</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.832.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/571">ryand56/r2-upload-action#571</a></li>
  <li>chore(deps): update dependency <code>@​types/node</code> to
  v22.15.33 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/573">ryand56/r2-upload-action#573</a></li>
  <li>fix(deps): update aws-sdk-js-v3 monorepo to v3.837.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/577">ryand56/r2-upload-action#577</a></li>
  <li>chore(deps): update dependency dotenv to v16.6.0 by <a
  href="https://github.com/renovate"><code>@​renovate</code></a>[bot] in
  <a
  href="https://redirect.github.com/ryand56/r2-upload-action/pull/578">ryand56/r2-upload-action#578</a></li>
  </ul>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/33ebb7a494b3a8a3c5ed2ea6bbdc72e707090317"><code>33ebb7a</code></a>
  chore: update to nodejs 24</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/61474c8f6a21b0dd8fc877a0b93c2c2078c88f60"><code>61474c8</code></a>
  chore: update mappings [skip ci]</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/7d9e7c27f8702296342da8daf84e76b24e43622d"><code>7d9e7c2</code></a>
  chore(deps): update typescript to v6</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/6e86c77f4ab91d5b532f6156c15509ef35fd905a"><code>6e86c77</code></a>
  fix(renovate): increase minimumReleaseAge and add packageRules for
  ts</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/fd3d3d4ccdcea99f8e7cc84bbb0a468147e9235e"><code>fd3d3d4</code></a>
  chore(deps): update dependency jest to v30.5.1</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/0b5990b910991eb1c068df9f99384b66e0b49e41"><code>0b5990b</code></a>
  chore(deps): update dependency github-action-ts-run-api to v3.1.0</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/4196309eee620f2cd556648b16b4b45fd959cee9"><code>4196309</code></a>
  chore(deps): update dependency dotenv to v17.4.2</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/d62fd1388703f08312d5f62fdef74f4b363a2802"><code>d62fd13</code></a>
  chore(deps): update dependency <code>@​vercel/ncc</code> to ^0.45.0</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/5124bb99384f12af4f3947f0c6a8f6509d580079"><code>5124bb9</code></a>
  chore(deps): update dependency ts-jest to v29.4.12</li>
  <li><a
  href="https://github.com/ryand56/r2-upload-action/commit/820995a4f185d5c18d4c60e6e371494e3046b336"><code>820995a</code></a>
  chore(deps): update dependency <code>@​actions/core</code> to
  v3.0.1</li>
  <li>Additional commits viewable in <a
  href="https://github.com/ryand56/r2-upload-action/compare/b801a390acbdeb034c5e684ff5e1361c06639e7c...33ebb7a494b3a8a3c5ed2ea6bbdc72e707090317">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=ryand56/r2-upload-action&package-manager=github_actions&previous-version=1.4&new-version=1.5)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`da9e216`](https://github.com/ghostty-org/ghostty/commit/da9e21602f918d47a46399c458937eff7c7a74ac) build(deps): bump c-hive/gha-remove-artifacts from 1.4.0 to 1.8.0 ([#14165](https://github.com/ghostty-org/ghostty/issues/14165)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [c-hive/gha-remove-artifacts](https://github.com/c-hive/gha-remove-artifacts)
  from 1.4.0 to 1.8.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/c-hive/gha-remove-artifacts/releases">c-hive/gha-remove-artifacts's
  releases</a>.</em></p>
  <blockquote>
  <h2>v1.8.0</h2>
  <p>Enhancements:</p>
  <ul>
  <li>New <code>skip-recent-commits</code> input keeps every artifact of
  the N most recent commits, regardless of how many artifacts each commit
  produced. Applied before <code>skip-recent</code>, so the two can be
  combined. Fixes <a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/28">#28</a></li>
  <li><code>GITHUB_TOKEN</code> can now be set on both <code>env:</code>
  and <code>with:</code> (for example when it is exported for all steps)
  without the action failing. The input takes precedence. Fixes <a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/48">#48</a></li>
  </ul>
  <h2>v1.7.0</h2>
  <p>Enhancements:</p>
  <ul>
  <li>New <code>dry-run</code> input: logs which artifacts would be
  removed without deleting anything.</li>
  <li>Stricter input validation. <code>age</code> now rejects fractional
  amounts and units that are not durations (for example <code>30 D</code>,
  which moment silently treated as zero); <code>skip-recent</code> and
  <code>max-retries</code> must be non-negative integers. Previously such
  values could make every artifact eligible for deletion.</li>
  <li>Artifacts without commit information are reported separately from
  tagged ones when <code>skip-tags</code> is on.</li>
  </ul>
  <p>Maintenance:</p>
  <ul>
  <li>Rewritten in TypeScript under <code>src/</code>, bundled with
  esbuild</li>
  <li>Unit tests for input parsing and the cleanup plan, plus end-to-end
  tests against a mock GitHub API covering deletion, rate limit retries
  and failure handling</li>
  <li>CI split into lint, typecheck, test, build and run jobs</li>
  <li>Dropped dependencies: yn, dotenv-safe, cross-env,
  eslint-plugin-import</li>
  </ul>
  <h2>v1.6.0</h2>
  <p>Enhancements:</p>
  <ul>
  <li>Artifacts are now listed repo-wide instead of per workflow run. This
  cuts API requests by roughly two orders of magnitude and removes the
  hardcoded 90-day window, so artifacts on repositories with longer
  retention are now cleaned up too. Fixes <a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/62">#62</a></li>
  <li>A failed deletion no longer aborts the run: remaining artifacts are
  still processed and the action fails at the end with a count.</li>
  <li>With <code>skip-tags</code>, artifacts without commit information
  are kept rather than deleted.</li>
  <li>The log ends with a summary of removed and skipped artifacts. Fixes
  <a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/21">#21</a></li>
  </ul>
  <p>Maintenance:</p>
  <ul>
  <li>CI checks that <code>dist/</code> matches the source instead of
  auto-committing it</li>
  <li>Removed CodeQL workflow, pre-commit hooks and
  eslint-plugin-import</li>
  <li>Dependency purposes documented in <code>package.json</code></li>
  </ul>
  <h2>v1.5.0</h2>
  <p>Enhancements:</p>
  <ul>
  <li>New <code>max-retries</code> input caps how often a rate-limited
  request is retried before the action fails. <strong>Default: 5.</strong>
  Previously requests were retried indefinitely; set a larger value to
  keep the old behaviour. Fixes <a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/36">#36</a>,
  <a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/49">#49</a>,
  <a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/51">#51</a></li>
  <li>Action runtime updated to Node 24 (<a
  href="https://redirect.github.com/c-hive/gha-remove-artifacts/issues/63">#63</a>)</li>
  </ul>
  <p>Maintenance:</p>
  <ul>
  <li>All dependencies upgraded (<code>@actions/core</code> 3,
  <code>@octokit/action</code> 8, <code>@octokit/plugin-throttling</code>
  11, moment 2.30). <code>pnpm audit</code> reports no known
  vulnerabilities.</li>
  <li>Source converted to ESM, bundled with <code>@vercel/ncc</code></li>
  <li>Tooling: pnpm, ESLint 10, Prettier 3, CI on Node 24</li>
  <li>Docs: <code>action.yml</code> description, updated retention docs
  link</li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/62c2fbea931baa7dd4a6b73ea5a799984a818f61"><code>62c2fbe</code></a>
  Bump version to 1.8.0</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/449a616233a48dbdd28ba5e08f4c2fb62913afa8"><code>449a616</code></a>
  Add skip-recent-commits input and accept GITHUB_TOKEN from env and
  input</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/4bff15786ba0b91dd8ed7c32459eb72441ac1b6c"><code>4bff157</code></a>
  Bump version to 1.7.0</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/a52e55eb4fd2dd1ce50f4e125d7e5855873bb38a"><code>a52e55e</code></a>
  Add end-to-end tests against a mock GitHub API</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/03f14e2351077f8bc463a7887eba3d4c062347b1"><code>03f14e2</code></a>
  Simplify config parsing, logging and tsconfig</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/04de7b0694b817261c05361cebc55090c8be4fb8"><code>04de7b0</code></a>
  Address review findings on the TypeScript rewrite</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/8b74b1b6fcb2881415de6d93701d4f4de6b170b1"><code>8b74b1b</code></a>
  Rewrite in TypeScript, add tests, merge CI workflows</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/73aaf4a5bf7a8fc25eca958284e770e44493029a"><code>73aaf4a</code></a>
  Bump version to 1.6.0</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/c4da97c8ee1e02b19ba57ae62c3fafd4b618e06d"><code>c4da97c</code></a>
  Ignore CLAUDE.local.md</li>
  <li><a
  href="https://github.com/c-hive/gha-remove-artifacts/commit/614c11c542a610a4eec69c8e2faa27904004155f"><code>614c11c</code></a>
  Describe each dependency in package.json</li>
  <li>Additional commits viewable in <a
  href="https://github.com/c-hive/gha-remove-artifacts/compare/44fc7acaf1b3d0987da0e8d4707a989d80e9554b...62c2fbea931baa7dd4a6b73ea5a799984a818f61">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=c-hive/gha-remove-artifacts&package-manager=github_actions&previous-version=1.4.0&new-version=1.8.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`2b3b893`](https://github.com/ghostty-org/ghostty/commit/2b3b893919e0bee74b567598e741a735777c9687) deps: update translate-c backport ([@vancluever](https://github.com/vancluever))
- [`82938b6`](https://github.com/ghostty-org/ghostty/commit/82938b633ba646db38591d969c3c526332bd7e65) deps: update translate-c backport ([#14126](https://github.com/ghostty-org/ghostty/issues/14126)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This is just a monthly refresh, things have been pretty quiet on both
  the Aro and translate-c sides.
  
  https://github.com/vancluever/arocc/compare/ecbc5c7...f97cdfc
  
  https://codeberg.org/vancluever/translate-c/compare/05e7b9dd87...4e879eb8ab
  ```
- [`97f2ddb`](https://github.com/ghostty-org/ghostty/commit/97f2ddb06e43ed73948385944cd1b0c19c282807) Sync CODEOWNERS vouch list ([#14163](https://github.com/ghostty-org/ghostty/issues/14163)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Sync CODEOWNERS owners with vouch list.
  
  ## Added Users
  
  - @slowdub
  ```

## September 6, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/34063395508)  
Summary: 1 runs • 4 commits • 3 authors

### Changes

- [`501e7b5`](https://github.com/ghostty-org/ghostty/commit/501e7b5c1cf04162305c56e85204d2b1ac9427fb) pkg/fontconfig: update to 2.18.3 ([@vancluever](https://github.com/vancluever))
  ```text
  This updates our own bundled fontconfig (for static builds) to 2.18.3.
  
  Note that fontconfig has changed their build process a bit since this
  has been updated last; they are leaning on the Autoconf (and Meson as
  they are now deprecating use of Autoconf) toolchain(s) to now generate a
  number of headers that are a part of the build process.
  
  Since servicing this dependency in an effort to keep the build pure Zig
  is starting to get more complex, I've added some documentation on how to
  actually get a snapshot of the fontconfig repository in a state where
  files can be looked for and copied over as needed. Otherwise, we might
  want to in the future consider removing this altogether and just rely on
  system integrations.
  ```
- [`11d1cc4`](https://github.com/ghostty-org/ghostty/commit/11d1cc4fc8decc84048bde1b746f3a013493e36f) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`955d902`](https://github.com/ghostty-org/ghostty/commit/955d902fa6abb3aaf71cac60d6b81bd83fa7fc69) pkg/fontconfig: update to 2.18.3 ([#14113](https://github.com/ghostty-org/ghostty/issues/14113)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Supersedes #14071 (just additional review and local re-generation/re-org
  of needed headers).
  
  This updates our own bundled fontconfig (for static builds) to 2.18.3.
  
  Note that fontconfig has changed their build process a bit since this
  has been updated last; they are leaning on the Autoconf (and Meson as
  they are now deprecating use of Autoconf) toolchain(s) to now generate a
  number of headers that are a part of the build process.
  
  Since servicing this dependency in an effort to keep the build pure Zig
  is starting to get more complex, I've added some documentation on how to
  actually get a snapshot of the fontconfig repository in a state where
  files can be looked for and copied over as needed. Otherwise, we might
  want to in the future consider removing this altogether and just rely on
  system integrations.
  ```
- [`f426f6f`](https://github.com/ghostty-org/ghostty/commit/f426f6f181ba95f45d33f683fb754b6359d9e04f) Update iTerm2 colorschemes ([#14159](https://github.com/ghostty-org/ghostty/issues/14159)) ([@jcollie](https://github.com/jcollie))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260831-151010-752a9c0
  ```

## September 4, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/33902692149), [2](https://github.com/ghostty-org/ghostty/actions/runs/33895939538)  
Summary: 2 runs • 257 commits • 24 authors

### Changes

- [`636a2f3`](https://github.com/ghostty-org/ghostty/commit/636a2f35b4a37fbb1b58dd801ae14513d355e95e) input: preserve numeric keypad output with MOK2 ([@mitchellh](https://github.com/mitchellh))
- [`e7bdda9`](https://github.com/ghostty-org/ghostty/commit/e7bdda9918a87f74178e15132c2894e29a8bf271) input: encode F13 through F25 ([@mitchellh](https://github.com/mitchellh))
- [`37e3cdd`](https://github.com/ghostty-org/ghostty/commit/37e3cdd2d281feb2bb403600974289406f891461) input: encode alt+escape with MOK2 ([@mitchellh](https://github.com/mitchellh))
- [`cc3fd8a`](https://github.com/ghostty-org/ghostty/commit/cc3fd8a773300371e2d1f41265128a7bf10adfa2) input: encode help and context menu keys ([@mitchellh](https://github.com/mitchellh))
- [`b97654f`](https://github.com/ghostty-org/ghostty/commit/b97654fe76a8badbbb0c51c0c0e2156fd12f0731) input: improve xterm modifyOtherKeys 2 compatibility ([#14145](https://github.com/ghostty-org/ghostty/issues/14145)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Follow-up to #14144
  
  I wrote a harness that created all possible US-layout keyboard input
  combinations with xterm patch 411 and Ghostty main and compared their
  full encoding sequence. There are various miscompatibilities on purpose
  but these were definitely bugs I wanted to address first.
  
  - Normal-mode numeric keypad keys now preserve their numeric output
  instead of falling through to generic MOK2 encoding. Application keypad
  behavior is unchanged.
  - F13 through F25 now emit their xterm-compatible function-key
  sequences, including modifier parameters.
  - Help and Context Menu now emit editing-key codes 28 and 29.
  - Alt+Escape now emits `CSI 27;3;27~` under MOK2 while retaining the
  traditional `ESC ESC` encoding otherwise.
  
  After these changes, 2,081 of 2,096 cases match xterm exactly. The
  remaining 15 differences are intentional.
  ```
- [`587e08f`](https://github.com/ghostty-org/ghostty/commit/587e08f3f70d29c7bc196e2cd919bd4b11f9b5bb) input: encode non-ASCII alt prefixes as UTF-8 ([@mitchellh](https://github.com/mitchellh))
  ```text
  Legacy Alt-as-Escape now prefixes the complete UTF-8 sequence for
  non-ASCII input. When text is unavailable, the encoder falls back to
  the UTF-8 encoding of the unshifted codepoint.
  
  This fixes 16 xterm legacy cases and eight fixterms cases without changing
  MOK2. The cases I'm talking about are in my comparison harness...
  
  The helper now writes Escape and the selected payload directly. It
  preserves macOS Option-as-Alt translation and shifted ASCII behavior.
  ```
- [`492300c`](https://github.com/ghostty-org/ghostty/commit/492300cad104195411d12217dd22f1cd05f31376) input: encode non-ASCII alt prefixes as UTF-8 ([#14146](https://github.com/ghostty-org/ghostty/issues/14146)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Legacy Alt-as-Escape now prefixes the complete UTF-8 sequence for
  non-ASCII input. When text is unavailable, the encoder falls back to the
  UTF-8 encoding of the unshifted codepoint.
  
  This fixes 16 xterm legacy cases and eight fixterms cases without
  changing MOK2. The cases I'm talking about are in my comparison
  harness...
  
  The helper now writes Escape and the selected payload directly. It
  preserves macOS Option-as-Alt translation and shifted ASCII behavior.
  ```
- [`7c845e8`](https://github.com/ghostty-org/ghostty/commit/7c845e8af5b2e0dc508f3f64c08383985bb536ed) terminal/kitty: drag and drop command decoding ([@mitchellh](https://github.com/mitchellh))
- [`38746b8`](https://github.com/ghostty-org/ghostty/commit/38746b8c14321004edaed584c2bf3d61b1cfd676) terminal/kitty: drag and drop response encoding ([@mitchellh](https://github.com/mitchellh))
- [`50f69b8`](https://github.com/ghostty-org/ghostty/commit/50f69b883cc75061441deadcbcbee9ecf6fc81b7) terminal/kitty: drag and drop drop state machine ([@mitchellh](https://github.com/mitchellh))
- [`af8d28a`](https://github.com/ghostty-org/ghostty/commit/af8d28a940beb3dd41d16a885c1f92c729aede37) terminal/kitty: drag and drop stream handler ([@mitchellh](https://github.com/mitchellh))
- [`db2f8be`](https://github.com/ghostty-org/ghostty/commit/db2f8be59011b09e4943cade3299e83686dc68d0) terminal/kitty: dnd docs ([@mitchellh](https://github.com/mitchellh))
- [`da5ddcb`](https://github.com/ghostty-org/ghostty/commit/da5ddcb0857c0e4ddb32f7a089911e9038d040f3) terminal: Kitty drag and drop protocol drop-only core logic and state machine ([#13973](https://github.com/ghostty-org/ghostty/issues/13973)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This builds out the core logic and state machine for the Kitty drag and
  drop protocol for _drops only_. This hooks it into libghostty-vt's Zig
  API but it isn't available to the C API and it isn't hooked up to any
  Ghostty GUI. It isn't really recommended that Zig consumers integrate
  this yet because I'm sure the API will continue to change dramatically
  as I address the missing features: drag source, remote drops, etc.
  
  The major thing this does it the core `src/terminal/kitty/dnd.zig` stuff
  with e2e tests extracted from Kitty's own `kitty_tets/dnd.py`. So this
  verifies that what we have so far is working properly.
  ```
- [`a5bb22e`](https://github.com/ghostty-org/ghostty/commit/a5bb22e235e6297b05f07b08ef1fecff7f2a8c5d) terminal: add shared paste core with Kitty clipboard paste events ([@mitchellh](https://github.com/mitchellh))
- [`8760323`](https://github.com/ghostty-org/ghostty/commit/87603231658a0e0c6a8b4be0be684b7f08778255) terminal: add stream handler paste operation and enable mode 5522 in libghostty ([@mitchellh](https://github.com/mitchellh))
- [`dda8e6f`](https://github.com/ghostty-org/ghostty/commit/dda8e6f3146fc3cd2bcff0049cfc8867b3e7b58a) sys: add secure random override option with a platform default ([@mitchellh](https://github.com/mitchellh))
- [`60a1ae2`](https://github.com/ghostty-org/ghostty/commit/60a1ae2df755629dc7aa7d7aac38569ca46d43a5) libghostty: add ghostty_terminal_paste C API with paste events example ([@mitchellh](https://github.com/mitchellh))
- [`da00936`](https://github.com/ghostty-org/ghostty/commit/da0093671a12cdbdbe62b70099113cca454cd997) Update VOUCHED list ([#13975](https://github.com/ghostty-org/ghostty/issues/13975)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13899#discussioncomment-18120807)
  from @jcollie.
  
  Vouch: @j-c-m
  ```
- [`5834a0e`](https://github.com/ghostty-org/ghostty/commit/5834a0e3df621802e9578e4562d88b0c2ad4ada8) Update VOUCHED list ([#13977](https://github.com/ghostty-org/ghostty/issues/13977)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13976#discussioncomment-18121426)
  from @pluiedev.
  
  Denounce: @tangivis
  ```
- [`6758251`](https://github.com/ghostty-org/ghostty/commit/675825163b3aa975fe66f577e99b75982b15d45b) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`e424060`](https://github.com/ghostty-org/ghostty/commit/e4240606752e5e4eb480b69104d75db0054f71c8) libghostty: centralize pasting to `ghostty_terminal_paste`, enable mode 5522 ([#13978](https://github.com/ghostty-org/ghostty/issues/13978)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  **Note: this has no changes for Ghostty GUI yet.** This only impacts
  libghostty-vt.
  
  This introduces a new `ghostty_terminal_paste` C API along with a
  central `terminal.paste.paste` function that handles (1) mode 5522
  (Kitty clipboard) (2) bracketed paste (3) normal paste all in one place,
  combined with unsafe value detection and proper xterm-style newline
  handling.
  
  Terminal pasting is now stateful because for the Kitty clipboard
  protocol in particular, it must mint "grants" that stay with the
  terminal. Previously, paste encoding was stateless.
  
  To start, this is only exposed/used by libghostty to enable Kitty
  clipboard handling.
  
  Other changes:
  
  - **IO: randomSecure.** This also adds the `io.randomSecure`
  implementation to `TinyIo` and a global sys override for it because
  Kitty clipboard requires the ability to create one-time passwords and
  the implementation (following Kitty) requires a crypto random source.
  The sys model is for libghostty embedders.
  
  - **New C result value: rejected.** This introduces a new C result enum
  value "rejected" for values that are valid but rejected for some reason.
  Its very possible that prior "invalid value" users will have to update
  to this, and I recognize that its close to both but it fills an
  important semantic difference.
  
  Also note this still _eagerly_ requires all clipboard contents. I want
  to move to a callback based model but it made the PR much more
  complicated. I plan on playing with that before converting apprt's to
  this.
  ```
- [`9f0e171`](https://github.com/ghostty-org/ghostty/commit/9f0e1719dc918368367d368bfe300f59bb68b5a4) i18n: update bg_BG translations ([#13802](https://github.com/ghostty-org/ghostty/issues/13802)) ([@trag1c](https://github.com/trag1c))
- [`3f87b2e`](https://github.com/ghostty-org/ghostty/commit/3f87b2e5817429fd123af2c980cf6798017b75a1) i18n(ru): second part of Russian translation ([@derVedro](https://github.com/derVedro))
- [`a36dc24`](https://github.com/ghostty-org/ghostty/commit/a36dc245b0a8111b86b8cecdd0abf1c8d8c4dff9) Sync CODEOWNERS vouch list ([#13981](https://github.com/ghostty-org/ghostty/issues/13981)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Sync CODEOWNERS owners with vouch list.
  
  ## Added Users
  
  - @ollioddi
  - @rkoten
  - @tuananh
  - @vasilmytsyk
  ```
- [`da27e6c`](https://github.com/ghostty-org/ghostty/commit/da27e6c9082705f62a9ebbeae1753e17d2a88088) libghostty: paste reads clipboard contents on demand, streams to pty ([@mitchellh](https://github.com/mitchellh))
  ```text
  Follow up to #13978
  
  `ghostty_terminal_paste` no longer takes the clipboard's data up front.
  The request now carries only the list of available MIME types plus a
  a callback that writes one representation's bytes into a `GhosttyWriter`.
  
  Previously an embedder had to load every representation for every MIME
  type into memory before pasting. For a clipboard holding a large image
  or video next to some text that could be hundreds of megabytes that
  were never used.
  
  I also took care to make sure that the data is only read once, to avoid
  any time-of-check/time-of-use (TOCTOU) issues.
  
  There is only one case where data might be fully buffered in memory now:
  unsafe text data that needs to be checked. This is true for how Ghostty
  GUI works today too.
  ```
- [`e77b230`](https://github.com/ghostty-org/ghostty/commit/e77b2309fca3a27db1123a4f904b7fb432ee7162) libghostty: paste reads clipboard contents on demand, streams to pty ([#13983](https://github.com/ghostty-org/ghostty/issues/13983)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Follow up to #13978
  
  `ghostty_terminal_paste` no longer takes the clipboard's data up front.
  The request now carries only the list of available MIME types plus a a
  callback that writes one representation's bytes into a `GhosttyWriter`.
  
  Previously an embedder had to load every representation for every MIME
  type into memory before pasting. For a clipboard holding a large image
  or video next to some text that could be hundreds of megabytes that were
  never used.
  
  I also took care to make sure that the data is only read once, to avoid
  any time-of-check/time-of-use (TOCTOU) issues.
  
  There is only one case where data might be fully buffered in memory now:
  unsafe text data that needs to be checked. This is true for how Ghostty
  GUI works today too.
  ```
- [`32159b6`](https://github.com/ghostty-org/ghostty/commit/32159b6fe6714a8401d5ad21ce8487ac0266afd8) i18n(ru): small fix in Russian translation ([@derVedro](https://github.com/derVedro))
- [`768bc2e`](https://github.com/ghostty-org/ghostty/commit/768bc2ed475ede520dbe0695184a9e2c4aec9128) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`6a508fd`](https://github.com/ghostty-org/ghostty/commit/6a508fd5e34c7e222c052a6d00bb3891ff3feace) macos: translate physical menu shortcuts ([#13888](https://github.com/ghostty-org/ghostty/issues/13888)) ([@bo2themax](https://github.com/bo2themax))
  ```text
  Translate printable physical keybindings through the current macOS
  keyboard layout before assigning menu key equivalents. Previously these
  bindings could not be represented because SwiftUI shortcuts are
  character-based, so actions such as `super+backquote` had no native menu
  shortcut.
  
  Keep native keycodes as dispatch identity so translated display
  characters do not change physical semantics or precedence over Unicode
  bindings. Refresh shortcuts when the input source changes, and prevent
  AppKit from transforming equivalents that are already localized.
  
  **AI Usage:** The approach was suggested by GPT 5.6 Sol, but I wrote
  most of the code and understand it all.
  ```
- [`169213c`](https://github.com/ghostty-org/ghostty/commit/169213cd292417ae25cb8df78d0a77243c134c81) renderer/image: Fuse copy to owned data and pixel format conversion in prepImage ([@AnthonyZhOon](https://github.com/AnthonyZhOon))
- [`6cf7e0c`](https://github.com/ghostty-org/ghostty/commit/6cf7e0cc544e7aa505713f40b58502bfc0ee8beb) macOS: fix swiftlint warnings ([@bo2themax](https://github.com/bo2themax))
  ```text
  swiftlint 0.63.3 introduced a new rule called [`legacy_swiftui_aspect_ratio`](https://github.com/realm/SwiftLint/blob/76363aa4d733934ece226f5bce8e27c43b986a63/CHANGELOG.md?plain=1#L314)
  ```
- [`1d24eec`](https://github.com/ghostty-org/ghostty/commit/1d24eecb207e8d9188d84b607b1de0e38eb999f6) macOS: fix responsiveness for repeated new tab action ([@bo2themax](https://github.com/bo2themax))
- [`b17abd9`](https://github.com/ghostty-org/ghostty/commit/b17abd96df2ef19a9df8e346d54a56db56f76221) refactor(image): Restrict prepForUpload to Image.Pending ([@AnthonyZhOon](https://github.com/AnthonyZhOon))
- [`4c696b9`](https://github.com/ghostty-org/ghostty/commit/4c696b90c5c2db61fd0929f102e9701bbcdfb809) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`2303bcf`](https://github.com/ghostty-org/ghostty/commit/2303bcf08df639a27ff949fb172a2b1e3feea0cd) ci: update actions/upload-artifact pinned tag comment ([@jparise](https://github.com/jparise))
- [`874735a`](https://github.com/ghostty-org/ghostty/commit/874735a9af41ec6aea0017b56836a3d3746f44b7) ci: update actions/upload-artifact pinned tag comment ([#13989](https://github.com/ghostty-org/ghostty/issues/13989)) ([@mitchellh](https://github.com/mitchellh))
- [`f9206be`](https://github.com/ghostty-org/ghostty/commit/f9206be827271b6765c966f85f6a68a1e44176b6) macOS: fix swiftlint warnings ([#13986](https://github.com/ghostty-org/ghostty/issues/13986)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  swiftlint 0.63.3 introduced a new rule called
  [`legacy_swiftui_aspect_ratio`](https://github.com/realm/SwiftLint/blob/76363aa4d733934ece226f5bce8e27c43b986a63/CHANGELOG.md?plain=1#L314)
  
  <img width="509" height="451" alt="image"
  src="https://github.com/user-attachments/assets/1ff6f593-ce8a-493e-a241-e9ae418746ee"
  />
  ```
- [`7a9bca6`](https://github.com/ghostty-org/ghostty/commit/7a9bca6a6e675ab71d6a2228237fd27b8f9f6345) macOS: fix responsiveness for repeated new tab action ([#13985](https://github.com/ghostty-org/ghostty/issues/13985)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13725
  ```
- [`94b6dae`](https://github.com/ghostty-org/ghostty/commit/94b6dae423a29d965dbf613307634fcb2ec6b112) libghostty: gate mode 5522 reports on clipboard read callback ([@mitchellh](https://github.com/mitchellh))
  ```text
  Report Kitty paste event mode 5522 as unrecognized when the stream
  handler has no clipboard_read effect.
  
  Previously libghostty-vt advertised Kitty paste events
  unconditionally but Kitty clipboard reads can't work without a clipboard
  read effect set.
  ```
- [`a53771a`](https://github.com/ghostty-org/ghostty/commit/a53771af0165c34a7bd753ddbcbc5dd7126ee87f) libghostty: gate mode 5522 reports on clipboard read callback ([#13990](https://github.com/ghostty-org/ghostty/issues/13990)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Report Kitty paste event mode 5522 as unrecognized when the stream
  handler has no clipboard_read effect.
  
  Previously libghostty-vt advertised Kitty paste events unconditionally
  but Kitty clipboard reads can't work without a clipboard read effect
  set.
  ```
- [`0ce9054`](https://github.com/ghostty-org/ghostty/commit/0ce9054bf9ff5c4107bbe8a460076012861f9a3a) macos: implement Kitty clipboard protocol reads (OSC 5522) ([@mitchellh](https://github.com/mitchellh))
- [`8c7a34d`](https://github.com/ghostty-org/ghostty/commit/8c7a34d4c9c6a1afcb7a96dcc9aa4665e05d883e) macos: Kitty clipboard reads serve all clipboard content types ([@mitchellh](https://github.com/mitchellh))
- [`af9470b`](https://github.com/ghostty-org/ghostty/commit/af9470b19b40b2829653130b6b491c9ecbe6bbee) macos: Kitty clipboard reads support pw/name session grants ([@mitchellh](https://github.com/mitchellh))
- [`c1f0ef7`](https://github.com/ghostty-org/ghostty/commit/c1f0ef73a9f3a80673d8be3e9ced5e50afaf65ac) macos: serve copied files as text/uri-list in Kitty clipboard reads ([@mitchellh](https://github.com/mitchellh))
- [`df14efa`](https://github.com/ghostty-org/ghostty/commit/df14efaf332ab66c2838bed6c3d15ff41f2fd31e) macos: preview images in the clipboard read confirmation dialog ([@mitchellh](https://github.com/mitchellh))
- [`7ae9b11`](https://github.com/ghostty-org/ghostty/commit/7ae9b11138e6c63888cc02ceefb92c6c1b3d4e9e) libghostty: Kitty clipboard write permission prompts and grants ([@mitchellh](https://github.com/mitchellh))
  ```text
  The `clipboard_write` effect now is similar to read: it must response
  to a "reply" callback synchronously. This lets the embedder ask for write
  permission, too.
  
  We also now pass through program name and grant information from Kitty
  clipboard protocol so that embedders can use that if they want.
  
  This is a breaking ABI change.
  ```
- [`1bc1887`](https://github.com/ghostty-org/ghostty/commit/1bc188739d62f05df33a7bbc9c8db93a1b9f5a13) typos ([@mitchellh](https://github.com/mitchellh))
- [`9f2aa93`](https://github.com/ghostty-org/ghostty/commit/9f2aa93e825735220c44159a2f4856af3ea6e79c) libghostty: Kitty clipboard write permission prompts and grants ([#13992](https://github.com/ghostty-org/ghostty/issues/13992)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The `clipboard_write` effect now is similar to read: it must response to
  a "reply" callback synchronously. This lets the embedder ask for write
  permission, too.
  
  We also now pass through program name and grant information from Kitty
  clipboard protocol so that embedders can use that if they want.
  
  This is a breaking ABI change.
  ```
- [`75d6577`](https://github.com/ghostty-org/ghostty/commit/75d657788a63d1593e5fff22c766bd7e162f255c) macOS: Kitty clipboard read support ([#13993](https://github.com/ghostty-org/ghostty/issues/13993)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds Kitty clipboard protocol _read_ support to macOS. In the
  process, this also does most of the core termio, apprt, and Surface work
  so GTK is likely very easy to do, I just didn't have the machine on hand
  to test at the given moment. I will create an issue to follow up with
  that.
  
  This fully supports:
  
  - Non-text data, like images! For this, we show an image preview.
  - Per-program "remember"
  - Showing the program name if given instead of generic "An application"
  
  <img width="1848" height="996" alt="CleanShot 2026-08-24 at 08 37 45@2x"
  src="https://github.com/user-attachments/assets/549d9031-2e98-46bf-90d4-94171b255c42"
  />
  ```
- [`88dc6f9`](https://github.com/ghostty-org/ghostty/commit/88dc6f9723e7a0371cffba0b32ecb945ad126770) docs: reformatting for help book support ([@bo2themax](https://github.com/bo2themax))
- [`53d1b28`](https://github.com/ghostty-org/ghostty/commit/53d1b28ad32dcf2e10e01177ef97863c1ba69f0d) docs: reformatting for help book support ([#13994](https://github.com/ghostty-org/ghostty/issues/13994)) ([@mitchellh](https://github.com/mitchellh))
- [`c2c0db6`](https://github.com/ghostty-org/ghostty/commit/c2c0db68aa3b33f996a0426f00cd5972dc691ef3) macOS: enable mode 5522 paste events ([@mitchellh](https://github.com/mitchellh))
  ```text
  Advertise Kitty clipboard protocol mode 5522 on macOS and route
  clipboard paste requests through the protocol when it is enabled.
  ```
- [`1dcf4eb`](https://github.com/ghostty-org/ghostty/commit/1dcf4eb2dff0e61cac22d2a6c0700fe2dade9011) renderer/image: Fuse copying data and converting pixel format ([#13987](https://github.com/ghostty-org/ghostty/issues/13987)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Profiling `mpv --vo=kitty --vo-kitty-use-shm <video>` shows up a copy
  and then swizzle in `prepImage`
  This comes from the renderer copying the raw image data for ownership,
  then doing an rgb to rgba conversion to replace the copied data.
  This change optimize this case by letting the format conversion read
  from the data source instead of a copy of it.
  
  <img width="3825" height="1579" alt="image"
  src="https://github.com/user-attachments/assets/25851c04-b582-4bad-8f8d-930448d89fa2"
  />
  <img width="3825" height="1579" alt="image"
  src="https://github.com/user-attachments/assets/fbb1ca73-a86f-421b-992d-a764ce08c83e"
  />
  > Above-Before: prepImage profiles a memcpy + swizzle
  > Below-After: prepImage profiles just a swizzle
  
  
  The existing data path for kitty images is:
  ```
  
  Read tty for Kitty image transmission (srgb, srgba, or PNG bytes)
  -> copy into Kitty graphics ImageStorage (cpu-owned)
  
  Renderer updateFrame creates Image.Pending in renderer-owned CPU storage
  -> sync Kitty ImageStorage with renderer-owned ImageMap
  -> copy bytes into renderer.ImageMap (renderer-owned)
  -> convert ImageMap bytes to preferred GPU upload format
  
  Renderer drawFrame uploads image data to the GPU
  -> iterate through renderer.ImageMap
    -> for Pending image uploads
      -> convert the pixel format (no-op if already done), create the GPU-side texture and upload the data
  ```
  
  # Note
  Kitty graphics only supports RGB and RGBA data
  The image file decode path uses a wuffs png and jpeg decode function
  configured to return RGBA 8-bit, so I think in practice we only ever
  upload RGB8 or RGBA8. And the gray-alpha and gray pixel formats aren't
  ever used.
  
  
  # AI Disclosure
  I didn't use any LLM assistance for this.
  ````
- [`c8554f2`](https://github.com/ghostty-org/ghostty/commit/c8554f28e0efe2f5595f32020371c34b25ec628f) macOS: enable mode 5522 paste events ([#13995](https://github.com/ghostty-org/ghostty/issues/13995)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Advertise Kitty clipboard protocol mode 5522 on macOS and route
  clipboard paste requests through the protocol when it is enabled.
  ```
- [`0a396b4`](https://github.com/ghostty-org/ghostty/commit/0a396b43dccee62e61e2f17643262b800fd7699b) i18n(ru): context menu fix in Russian translation ([@derVedro](https://github.com/derVedro))
- [`9313d58`](https://github.com/ghostty-org/ghostty/commit/9313d580c6b0aff578160c79fc99fff341cf4aa3) terminal: fix stale cursor style/hyperlink state after scroll clear ([@mitchellh](https://github.com/mitchellh))
  ```text
  Clearing the screen into scrollback and then printing could crash debug
  builds with a page integrity violation, or silently corrupt style/hyperlink
  reference counts in release builds. Found in #13991 via fuzzing.
  
  The cursor's style and hyperlink IDs are only valid on the page the
  cursor is on. When the scroll clear moved the start of the fresh
  screen onto a new page, the reset path in cursorReload updated the
  cursor's position directly instead of going through cursorChangePin,
  so the cursor kept IDs from its old page. On the new page those IDs
  pointed at entries that were dead or belonged to something else, and
  the next print used them.
  
  Fix this by making the reset path go through `cursorChangePin` like
  every other cross-page cursor move, which releases the style and
  hyperlink from the old page and recreates them on the new one.
  ```
- [`7c49e72`](https://github.com/ghostty-org/ghostty/commit/7c49e723a3f2448d3224624b054d74983c4143ca) terminal: fix stale cursor style/hyperlink state after scroll clear ([#13997](https://github.com/ghostty-org/ghostty/issues/13997)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Clearing the screen into scrollback and then printing could crash debug
  builds with a page integrity violation, or silently corrupt
  style/hyperlink reference counts in release builds. Found in #13991 via
  fuzzing.
  
  The cursor's style and hyperlink IDs are only valid on the page the
  cursor is on. When the scroll clear moved the start of the fresh screen
  onto a new page, the reset path in cursorReload updated the cursor's
  position directly instead of going through cursorChangePin, so the
  cursor kept IDs from its old page. On the new page those IDs pointed at
  entries that were dead or belonged to something else, and the next print
  used them.
  
  Fix this by making the reset path go through `cursorChangePin` like
  every other cross-page cursor move, which releases the style and
  hyperlink from the old page and recreates them on the new one.
  ```
- [`25c61e8`](https://github.com/ghostty-org/ghostty/commit/25c61e852ff8de428a207a89a824bbba94a27da4) macos: implement Kitty clipboard protocol writes ([@mitchellh](https://github.com/mitchellh))
  ```text
  Programs can now write the system clipboard through the Kitty
  clipboard protocol in the macOS app. This also does all the hard work
  plumbing through core termio/apprt so GTK should be an easy follow.
  
  This functionality lets clients copy arbitrary representations (images,
  HTML, etc.) into the clipboard. Writes honor `clipboard-write`: allow
  applies silently, deny answers EPERM up front before any data is used,
  and ask shows the standard confirmation prompt.
  ```
- [`89d17b3`](https://github.com/ghostty-org/ghostty/commit/89d17b378ed9c9d68a82ab2359cfa8030f8ff4f9) macos: implement Kitty clipboard protocol writes ([#13998](https://github.com/ghostty-org/ghostty/issues/13998)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Programs can now write the system clipboard through the Kitty clipboard
  protocol in the macOS app. This also does all the hard work plumbing
  through core termio/apprt so GTK should be an easy follow.
  
  This functionality lets clients copy arbitrary representations (images,
  HTML, etc.) into the clipboard. Writes honor `clipboard-write`: allow
  applies silently, deny answers EPERM up front before any data is used,
  and ask shows the standard confirmation prompt.
  
  After this, I believe the core and macOS have 100% Kitty clipboard
  implementation but I'll double check after this.
  
  ## Demo
  
  
  
  https://github.com/user-attachments/assets/71234fa0-f539-48eb-a633-8dea3addddd5
  ```
- [`5501518`](https://github.com/ghostty-org/ghostty/commit/550151882a93b9272d381df29ab10b2041981359) macos: restore paste semantics for dropped text ([@mitchellh](https://github.com/mitchellh))
  ```text
  Discussion #13979
  
  Dropped paths and text once again honor bracketed paste mode.
  IME, dictation, emoji picker, and character viewer commits remain typed input.
  
  sendText calls ghostty_surface_text, which applies the clipboard paste
  pipeline and bracketed paste framing when enabled. Separating the
  paths at the drag-and-drop caller preserves the input-method behavior
  introduced by #13817.
  ```
- [`1334cc2`](https://github.com/ghostty-org/ghostty/commit/1334cc213e6db4be3f2fc695a06c13d49362a570) macos: answer ENOSYS for Kitty clipboard writes to primary ([@mitchellh](https://github.com/mitchellh))
  ```text
  A Kitty clipboard protocol (OSC 5522) write transaction targeting
  `loc=primary` replied `type=write:status=DONE` in the macOS app even
  though macOS has no primary selection and the data was silently
  discarded.
  
  The spec requires ENOSYS when the requested location is not
  available on the system, which the read path already answers correctly:
  https://sw.kovidgoyal.net/kitty/clipboard/
  ```
- [`928c7f0`](https://github.com/ghostty-org/ghostty/commit/928c7f0e796a96bdee53de0ba4e3469c3e7d84a9) terminal: exempt Kitty clipboard listing reads from permission prompts ([@mitchellh](https://github.com/mitchellh))
  ```text
  A Kitty clipboard protocol (OSC 5522) read that only requests the
  targets type ('.') is now served without a permission prompt and never
  consults (or consumes) session password grants.
  
  The spec requires this so that a client listing the available data types
  before reading one doesn't present the user with a double permission prompt.
  ```
- [`4f4da76`](https://github.com/ghostty-org/ghostty/commit/4f4da7657ba9c551f6110d38b73e72d3c504fd54) macos: answer ENOSYS for Kitty clipboard writes to primary ([#14000](https://github.com/ghostty-org/ghostty/issues/14000)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A Kitty clipboard protocol (OSC 5522) write transaction targeting
  `loc=primary` replied `type=write:status=DONE` in the macOS app even
  though macOS has no primary selection and the data was silently
  discarded.
  
  The spec requires ENOSYS when the requested location is not available on
  the system, which the read path already answers correctly:
  https://sw.kovidgoyal.net/kitty/clipboard/
  ```
- [`13b9857`](https://github.com/ghostty-org/ghostty/commit/13b9857a25e7befc9ae95ecaf8f3563a13757350) macos: restore paste semantics for dropped text ([#13999](https://github.com/ghostty-org/ghostty/issues/13999)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Discussion #13979
  
  Dropped paths and text once again honor bracketed paste mode. IME,
  dictation, emoji picker, and character viewer commits remain typed
  input.
  
  sendText calls ghostty_surface_text, which applies the clipboard paste
  pipeline and bracketed paste framing when enabled. Separating the paths
  at the drag-and-drop caller preserves the input-method behavior
  introduced by #13817.
  ```
- [`5350d4a`](https://github.com/ghostty-org/ghostty/commit/5350d4a5f5971da9ef4ea32566bd5d7b011dc29c) terminal: make Kitty clipboard write limit configurable ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a new `clipboard-write-limit-bytes` option (similar to
  `scrollback-limit-bytes`) to limit the maximum OSC 5522 write size.
  Defaults to 32 MB.
  
  This also adds a new `GHOSTTY_TERMINAL_OPT_CLIPBOARD_WRITE_MAX_BYTES`
  option for libghostty-vt embedders to control the same.
  
  Kitty has a limit too and it works by truncating all data. I decided on
  purpose to diverge from this because I don't think truncated binary data
  is useful. Instead, we reject it so the application knows the write
  didn't work.
  
  We truncate text data, and we try to do it at the nearest complete UTF-8
  sequence (if possible).
  ```
- [`75606a6`](https://github.com/ghostty-org/ghostty/commit/75606a6900124a1c9774d97968f69a5f7bb9c080) terminal: exempt Kitty clipboard listing reads from permission prompts ([#14001](https://github.com/ghostty-org/ghostty/issues/14001)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A Kitty clipboard protocol (OSC 5522) read that only requests the
  targets type ('.') is now served without a permission prompt and never
  consults (or consumes) session password grants.
  
  The spec requires this so that a client listing the available data types
  before reading one doesn't present the user with a double permission
  prompt.
  ```
- [`600a86d`](https://github.com/ghostty-org/ghostty/commit/600a86dcfd70ac6a16db199367ee6aad337b99cc) terminal: make Kitty clipboard write limit configurable ([#14002](https://github.com/ghostty-org/ghostty/issues/14002)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a new `clipboard-write-limit-bytes` option (similar to
  `scrollback-limit-bytes`) to limit the maximum OSC 5522 write size.
  Defaults to 32 MB.
  
  This also adds a new `GHOSTTY_TERMINAL_OPT_CLIPBOARD_WRITE_MAX_BYTES`
  option for libghostty-vt embedders to control the same.
  
  Kitty has a limit too and it works by truncating all data. I decided on
  purpose to diverge from this because I don't think truncated binary data
  is useful. Instead, we reject it so the application knows the write
  didn't work.
  
  We truncate text data, and we try to do it at the nearest complete UTF-8
  sequence (if possible).
  
  For the future: Kitty spools any write data more than some size (can't
  remember) to a temp file on disk. We might want to consider doing
  something similar since we're all in-memory at the moment. This PR
  doesn't change that.
  ```
- [`70f0065`](https://github.com/ghostty-org/ghostty/commit/70f0065759428c0594c7c5befcb20104ff7ab615) terminal: reject oversized Kitty clipboard writes ([@mitchellh](https://github.com/mitchellh))
  ```text
  Update OSC 5522 writes to reject every transaction that exceeds the
  configured decoded-data limit. The previous behavior truncated text
  while rejecting only non-text data.
  
  Programs now receive EFBIG as soon as a write crosses the limit. The
  clipboard remains untouched, and remaining write packets are ignored
  until a new transaction begins. Raise the default to the protocol
  minimum of 64 MiB.
  
  This applies the latest spec change:
  https://github.com/kovidgoyal/kitty/commit/32ea1041921607836e37815e0ab3692264a6cc81
  ```
- [`e8d8945`](https://github.com/ghostty-org/ghostty/commit/e8d8945b536189366e227b157aa0b8202b94890a) terminal: update Kitty clipboard text input validation to spec ([@mitchellh](https://github.com/mitchellh))
  ```text
  Validate decoded OSC 5522 metadata, read MIME lists, and alias
  lists as UTF-8. Treat an alias without a target MIME type as an
  invalid write packet.
  
  Malformed write packets now return EINVAL and terminate the in-flight
  transaction instead of leaving it active. Malformed reads are dropped
  without disturbing an active write.
  
  Latest changes upstream to spec:
  https://github.com/kovidgoyal/kitty/commit/458421af4656a8f90beca7d95e4c1ff7093cf269
  ```
- [`4888c0a`](https://github.com/ghostty-org/ghostty/commit/4888c0a02c2e36b5146900195e344a8ac307660f) terminal: reject oversized Kitty clipboard writes ([#14004](https://github.com/ghostty-org/ghostty/issues/14004)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Update OSC 5522 writes to reject every transaction that exceeds the
  configured decoded-data limit. The previous behavior truncated text
  while rejecting only non-text data.
  
  Programs now receive EFBIG as soon as a write crosses the limit. The
  clipboard remains untouched, and remaining write packets are ignored
  until a new transaction begins. Raise the default to the protocol
  minimum of 64 MiB.
  
  This applies the latest spec change:
  
  https://github.com/kovidgoyal/kitty/commit/32ea1041921607836e37815e0ab3692264a6cc81
  ```
- [`8867c37`](https://github.com/ghostty-org/ghostty/commit/8867c37c55b578b9eb4cfaba41cb9023e557176d) terminal: update Kitty clipboard text input validation to spec ([#14005](https://github.com/ghostty-org/ghostty/issues/14005)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Validate decoded OSC 5522 metadata, read MIME lists, and alias lists as
  UTF-8. Treat an alias without a target MIME type as an invalid write
  packet.
  
  Malformed write packets now return EINVAL and terminate the in-flight
  transaction instead of leaving it active. Malformed reads are dropped
  without disturbing an active write.
  
  Latest changes upstream to spec:
  
  https://github.com/kovidgoyal/kitty/commit/458421af4656a8f90beca7d95e4c1ff7093cf269
  ```
- [`a2212a5`](https://github.com/ghostty-org/ghostty/commit/a2212a5b1229d580ceb25d67cf3353b679eddf3b) macos: replace legacy aspectRatio with scaledToFit in clipboard preview ([@bo2themax](https://github.com/bo2themax))
- [`d7f5ba3`](https://github.com/ghostty-org/ghostty/commit/d7f5ba3b4f4745660dbb5ada6fde6f841aba07af) macOS: add test cases for ScriptKeyEventCommand ([@bo2themax](https://github.com/bo2themax))
- [`f1b9efe`](https://github.com/ghostty-org/ghostty/commit/f1b9efed802650ffaccc0b53da026314909bae53) macOS: update default behaviour of KeyboardLayout.character(for:modifiers:) ([@bo2themax](https://github.com/bo2themax))
- [`719def7`](https://github.com/ghostty-org/ghostty/commit/719def70f3df246695881f571f0edde28b95f0a3) macOS: update default behaviour of KeyboardLayout.character(for:modifiers:) ([#14009](https://github.com/ghostty-org/ghostty/issues/14009)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Follow up for #13888, and prepare for #13205.
  
  The comments are copied from the history commit.
  
  ## AI Disclosure
  
  The tests are updated by Claude, I cherrypicked them.
  ```
- [`1c73935`](https://github.com/ghostty-org/ghostty/commit/1c739350c31a8340fdbf56cd7e703f860f69bed4) macOS: add test cases for ScriptKeyEventCommand ([#14008](https://github.com/ghostty-org/ghostty/issues/14008)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Partial changes for #13205, known issues are marked as warnings.
  
  ### AI Disclosure
  
  Claude generated these tests from linked pr, I cherrypicked and reviewed
  myself.
  ```
- [`6d2b436`](https://github.com/ghostty-org/ghostty/commit/6d2b43652950b417431145147dd445d32e04119c) macos: replace legacy aspectRatio with scaledToFit in clipboard preview ([#14006](https://github.com/ghostty-org/ghostty/issues/14006)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes the swiftlint legacy_swiftui_aspect_ratio violation.
  
  ### AI Disclosure
  
  By Claude, but it's really simple.
  ```
- [`b31fbc8`](https://github.com/ghostty-org/ghostty/commit/b31fbc846474bf6082f1a3f13290e17f2d984a25) terminal: fully reset row metadata when recycling row storage ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13940
  
  Various operations like scroll, line insert, erase, etc. operations
  would clear cells but remain row metadata such as wrap flags and
  semantic prompt state.
  
  When we had fast paths in `grow` and other places like resize
  we would adopt that without knowing it because we didn't properly clear.
  
  Fix this by properly clearing row metadata too at the points where we
  erase a row that might be reused.
  
  Benchmarked with terminal-stream workloads for each affected path.
  The added cost is 2-4 instructions per recycled row next to the existing
  full-row cell clear. There was no measurable wall-clock change on any
  workload.
  
  AI helped run the benchmarks for me and analyze for missing places (it found
  some!) but otherwise this was hand-designed.
  ```
- [`046a45a`](https://github.com/ghostty-org/ghostty/commit/046a45a5fcacf427573b81de6e03de37fe01bb16) terminal: fully reset row metadata when recycling row storage ([#14010](https://github.com/ghostty-org/ghostty/issues/14010)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13940
  
  Various operations like scroll, line insert, erase, etc. operations
  would clear cells but remain row metadata such as wrap flags and
  semantic prompt state.
  
  When we had fast paths in `grow` and other places like resize we would
  adopt that without knowing it because we didn't properly clear.
  
  Fix this by properly clearing row metadata too at the points where we
  erase a row that might be reused.
  
  Benchmarked with terminal-stream workloads for each affected path. The
  added cost is 2-4 instructions per recycled row next to the existing
  full-row cell clear. There was no measurable wall-clock change on any
  workload.
  
  AI helped run the benchmarks for me and analyze for missing places (it
  found some!) but otherwise this was hand-designed.
  ```
- [`8c5bc3d`](https://github.com/ghostty-org/ghostty/commit/8c5bc3d29f17ebc42b81d4b61ec1fe86886332d4) terminal: optimize OSC string reading with SIMD ([@mitchellh](https://github.com/mitchellh))
  ```text
  We now have large OSCs (e.g. Kitty clipboard protocol) on the order
  of megabytes. OSC was still byte-at-a-time. This adds a vector-optimized
  plus bulk storing path to OSC, similar to APC.
  
  Throughput measured with the terminal-stream benchmark:
  
  | Corpus                   | Before | After | Speedup |
  |--------------------------|--------|-------|---------|
  | OSC 52, 1MiB payloads    | 446ms  | 14ms  | 32x     |
  | OSC 5522, 1MiB payloads  | 446ms  | 15ms  | 30x     |
  | OSC 5522, 64KiB payloads | 448ms  | 14ms  | 32x     |
  | OSC 5522, 4KiB payloads  | 448ms  | 16ms  | 29x     |
  | Tiny titles (~24B each)  | 450ms  | 73ms  | 6.2x    |
  | Mixed OSCs (16MiB)       | 595ms  | 531ms | 1.13x   |
  
  Used Fable to help validate this with a barrage of differential tests.
  The actual implementation was AI-written but was guided to basically
  mimic the APC path and then I hand verified everything too.
  ```
- [`8144ef4`](https://github.com/ghostty-org/ghostty/commit/8144ef4e73e70a4e9942fceb319819005f07fd37) terminal: optimize OSC string reading with SIMD ([#14011](https://github.com/ghostty-org/ghostty/issues/14011)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  We now have large OSCs (e.g. Kitty clipboard protocol) on the order of
  megabytes. OSC was still byte-at-a-time. This adds a vector-optimized
  plus bulk storing path to OSC, similar to APC.
  
  Throughput measured with the terminal-stream benchmark:
  
  | Corpus                   | Before | After | Speedup |
  |--------------------------|--------|-------|---------|
  | OSC 52, 1MiB payloads    | 446ms  | 14ms  | 32x     |
  | OSC 5522, 1MiB payloads  | 446ms  | 15ms  | 30x     |
  | OSC 5522, 64KiB payloads | 448ms  | 14ms  | 32x     |
  | OSC 5522, 4KiB payloads  | 448ms  | 16ms  | 29x     |
  | Tiny titles (~24B each)  | 450ms  | 73ms  | 6.2x    |
  | Mixed OSCs (16MiB)       | 595ms  | 531ms | 1.13x   |
  
  Used Fable to help validate this with a barrage of differential tests.
  The actual implementation was AI-written but was guided to basically
  mimic the APC path and then I hand verified everything too.
  ```
- [`48a9e29`](https://github.com/ghostty-org/ghostty/commit/48a9e29f79e918d4f73a13c1ce27646d029811e4) nix: update nixpkgs-unstable ([@jcollie](https://github.com/jcollie))
  ```text
  Update nixpkgs-unstable to pick up fontconfig 2.18. Currently we are linking against 2.17 and you get errors
  like this on standard error when using config files meant for fontconfig 2.18:
  
    Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 20: invalid constant used :
    Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 23: invalid constant used : monospace
    Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 42: invalid attribute 'xsi:nil'
    Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 43: invalid constant used :
    Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 46: invalid constant used : sans-serif
    Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 68: invalid attribute 'xsi:nil'
    Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 69: invalid constant used :
  
  This also removes an override for libfyaml on Darwin that was merged upstream into nixpkgs.
  ```
- [`d9857ea`](https://github.com/ghostty-org/ghostty/commit/d9857eabae06baebc9685121bfe78c49090643af) cli: update list-themes preview sample to valid Zig 0.16 syntax ([@tacheraSasi](https://github.com/tacheraSasi))
- [`bb00a5c`](https://github.com/ghostty-org/ghostty/commit/bb00a5c988245a10f7d96dfdadcbfbd03f977dc4) Update VOUCHED list ([#14013](https://github.com/ghostty-org/ghostty/issues/14013)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14012#issuecomment-5412366760)
  from @jcollie.
  
  Vouch: @tacheraSasi
  ```
- [`ba35746`](https://github.com/ghostty-org/ghostty/commit/ba35746377788b8953a895559a91c6e1733c18da) i18n(ru): improve Russian translation ([@derVedro](https://github.com/derVedro))
- [`bc2f7d7`](https://github.com/ghostty-org/ghostty/commit/bc2f7d7d2fa589a3abf9e4f6696e0a7f7c204e4f) terminal: update Kitty clipboard base64 handling to spec ([@mitchellh](https://github.com/mitchellh))
  ```text
  The Kitty clipboard protocol now specifies base64 handling:
  All OSC 5522 payloads and the base64 metadata values (mime, name, pw)
  use strict RFC 4648 with the standard alphabet. Characters outside
  the alphabet (including whitespace) and incorrect padding must be
  rejected, never silently skipped.
  
  For wdata payloads for one MIME type, the base64 stream can be split
  at arbitrary packet boundaries and only the concatenation must be
  correctly padded.
  
  Simdutf has a strict mode for base64 so we got this for free.
  Benchmarks to be safe:
  
  | Decoder                       | Time  | Throughput |
  |-------------------------------|-------|------------|
  | permissive (previous)         | 99ms  | 10.8 GB/s  |
  | strict                        | 97ms  | 11.1 GB/s  |
  | strict, streaming 4KiB chunks | 102ms | 10.5 GB/s  |
  | strict w/ separate scan pass  | 143ms | 7.5 GB/s   |
  | std.base64 scalar             | 234ms | 4.6 GB/s   |
  
  Spec changes upstream:
  https://github.com/kovidgoyal/kitty/commit/479872838f7536ab87b8133471eb49d06804951b
  https://sw.kovidgoyal.net/kitty/clipboard/#encoding-of-payloads
  ```
- [`82ccf12`](https://github.com/ghostty-org/ghostty/commit/82ccf12ca22131d2c845387806b6a924f86abe5f) nix: update nixpkgs-unstable ([#13678](https://github.com/ghostty-org/ghostty/issues/13678)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Update nixpkgs-unstable to pick up fontconfig 2.18. Currently we are
  linking against 2.17 and you get errors like this on standard error when
  using config files meant for fontconfig 2.18:
  
  Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 20:
  invalid constant used :
  Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 23:
  invalid constant used : monospace
  Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 42:
  invalid attribute 'xsi:nil'
  Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 43:
  invalid constant used :
  Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 46:
  invalid constant used : sans-serif
  Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 68:
  invalid attribute 'xsi:nil'
  Fontconfig warning: "/etc/fonts/conf.d/48-guessfamily.conf", line 69:
  invalid constant used :
  ```
- [`557253d`](https://github.com/ghostty-org/ghostty/commit/557253d8f64f8b08da33f5a7f3cb33a75960b09d) terminal: update Kitty clipboard base64 handling to spec ([#14015](https://github.com/ghostty-org/ghostty/issues/14015)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The Kitty clipboard protocol now specifies base64 handling: All OSC 5522
  payloads and the base64 metadata values (mime, name, pw) use strict RFC
  4648 with the standard alphabet. Characters outside the alphabet
  (including whitespace) and incorrect padding must be rejected, never
  silently skipped.
  
  For wdata payloads for one MIME type, the base64 stream can be split at
  arbitrary packet boundaries and only the concatenation must be correctly
  padded.
  
  Simdutf has a strict mode for base64 so we got this for free. Benchmarks
  to be safe:
  
  | Decoder                       | Time  | Throughput |
  |-------------------------------|-------|------------|
  | permissive (previous)         | 99ms  | 10.8 GB/s  |
  | strict                        | 97ms  | 11.1 GB/s  |
  | strict, streaming 4KiB chunks | 102ms | 10.5 GB/s  |
  | strict w/ separate scan pass  | 143ms | 7.5 GB/s   |
  | std.base64 scalar             | 234ms | 4.6 GB/s   |
  
  Spec changes upstream:
  
  https://github.com/kovidgoyal/kitty/commit/479872838f7536ab87b8133471eb49d06804951b
  https://sw.kovidgoyal.net/kitty/clipboard/#encoding-of-payloads
  ```
- [`4e817e7`](https://github.com/ghostty-org/ghostty/commit/4e817e79a1d7e3fe7393297e3c8f1269abb6523a) terminal: treat high bytes in DCS strings as payload data ([@mitchellh](https://github.com/mitchellh))
  ```text
  Refs #11216
  
  The dcs_passthrough state only forwarded bytes 0x00-0x7E to the DCS
  handler. Bytes 0x80-0x9F hit the "anywhere" C1 transitions and exited
  the string, while 0xA0-0xFF fell through to the default transition and
  were silently dropped. **This breaks any DCS payload carrying UTF-8. **
  
  A continuation byte in the C1 range terminates or corrupts the string:
  "Ü" is 0xC3 0x9C, so the 0xC3 is dropped and the 0x9C acts as 8-bit ST,
  ending the DCS mid-character.
  
  Also, a payload byte such as 0x9B (second byte of "Û") transitions to
  csi_entry, so the remainder of the payload executes as a live control sequence.
  This is a prerequisite for tmux control mode (#1935), whose %output
  notifications carry raw UTF-8 pane content.
  
  Fix this in the parse table only: override 0x80-0xFF in
  dcs_passthrough to put and in dcs_ignore to ignore, exactly how
  osc_string already claims 0x20-0xFF (including 0x9C) as data. This
  deviates from the vt100.net state machine
  (https://vt100.net/emu/dec_ansi_parser) deliberately and includes
  0x9C: a raw 0x9C is indistinguishable from a UTF-8 continuation byte,
  and we don't honor 8-bit C1 controls in the ground state either.
  ```
- [`b260da2`](https://github.com/ghostty-org/ghostty/commit/b260da24f8f10bebc92539eef640dbfd26c5a854) cli: update list-themes preview sample to valid Zig 0.16 syntax ([#14012](https://github.com/ghostty-org/ghostty/issues/14012)) ([@jcollie](https://github.com/jcollie))
  ````text
  The demo code shown in the `+list-themes` theme preview was stale from
  before the Zig 0.16 migration (context: #12228). It referenced
  `std.Io.getStdOut().writer()`, which never existed in any Zig release,
  and `pub fn main() !void`. This rewrites the rendered sample to valid
  Zig 0.16 idioms:
  
  ```zig
  const std = @import("std");
  
  pub fn main(init: std.process.Init) !void {
      var buf: [1024]u8 = undefined;
      var stdout = std.Io.File.stdout().writer(init.io, &buf);
      const w = &stdout.interface;
  
      var i: usize = 1;
      while (i <= 16) : (i += 1) {
          if (i % 15 == 0) {
              try w.writeAll("ZiggZagg\n");
          } else if (i % 3 == 0) {
              try w.writeAll("Zigg\n");
          } else if (i % 5 == 0) {
              try w.writeAll("Zagg\n");
          } else {
              try w.print("{d}\n", .{i});
          }
      }
      try w.flush();
  }
  ```
  
  The gutter line numbers, row offsets, and child window height were
  renumbered to match, and the zig version shown in the demo prompt line
  was updated from v0.13.0 to v0.16.0.
  ````
- [`9c3ec93`](https://github.com/ghostty-org/ghostty/commit/9c3ec931d64561a8407dde7ac984ce156ae91539) terminal: treat high bytes in DCS strings as payload data ([#14016](https://github.com/ghostty-org/ghostty/issues/14016)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Refs #11216
  
  The dcs_passthrough state only forwarded bytes 0x00-0x7E to the DCS
  handler. Bytes 0x80-0x9F hit the "anywhere" C1 transitions and exited
  the string, while 0xA0-0xFF fell through to the default transition and
  were silently dropped. **This breaks any DCS payload carrying UTF-8. **
  
  A continuation byte in the C1 range terminates or corrupts the string:
  "Ü" is 0xC3 0x9C, so the 0xC3 is dropped and the 0x9C acts as 8-bit ST,
  ending the DCS mid-character.
  
  Also, a payload byte such as 0x9B (second byte of "Û") transitions to
  csi_entry, so the remainder of the payload executes as a live control
  sequence. This is a prerequisite for tmux control mode (#1935), whose
  %output notifications carry raw UTF-8 pane content.
  
  Fix this in the parse table only: override 0x80-0xFF in dcs_passthrough
  to put and in dcs_ignore to ignore, exactly how osc_string already
  claims 0x20-0xFF (including 0x9C) as data. This deviates from the
  vt100.net state machine
  (https://vt100.net/emu/dec_ansi_parser) deliberately and includes 0x9C:
  a raw 0x9C is indistinguishable from a UTF-8 continuation byte, and we
  don't honor 8-bit C1 controls in the ground state either.
  ```
- [`6229d4e`](https://github.com/ghostty-org/ghostty/commit/6229d4eb62f9e2483b3ea00c11fcde70590d2d84) macOS: fix AppleScript send key for non-control keys ([@bo2themax](https://github.com/bo2themax))
- [`c4e1697`](https://github.com/ghostty-org/ghostty/commit/c4e16970a803b170e352432424f44192cb59f3ac) renderer: release GPU resources for hidden surfaces (macOS) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Ref #12034
  
  This commit releases many GPU resources when a surface becomes invisible and
  rebuilds it on the next draw. I don't say "all" because there are still
  some things we can improve on (Kitty images).
  
  We previously held onto all GPU resources for the lifetime of the surface
  regardless of its visibility state. This is 3x (for triple-buffering):
  screen render targets, uniform/cell/custom shader buffers, font textures,
  and more.
  
  Measured on macOS (Metal):
  
  | Measurement (1 visible + 20 hidden tabs)    | Before    | After   |
  |---------------------------------------------|-----------|---------|
  | Tracked GPU allocations (steady state)      | 384.6 MiB | 18.3 MiB |
  | `MTLDevice.currentAllocatedSize`            | 393.3 MiB | 19.7 MiB |
  | `footprint` IOSurface (dirty)               | 309 MB    | 15 MB   |
  | Swap chain rebuild on unhide (42 switches)  | n/a       | avg 0.43 ms, max 0.55 ms |
  
  As you can see, importantly, swap chain rebuild is fast: 0.43ms average.
  That means that the rebuild is imperceptible and happens well within
  a frame draw time.
  
  This is macOS only, but most of the work was in the generic renderer.
  GTK only needs to call `releaseGpuResources` when it becomes invisible
  to get the same benefits. I didn't have my VM handy to test this yet so
  I didn't include it.
  ```
- [`683d8db`](https://github.com/ghostty-org/ghostty/commit/683d8db643b95cf229bfb5fe9fab9ae677920343) renderer: release GPU resources for hidden surfaces (macOS) ([#14017](https://github.com/ghostty-org/ghostty/issues/14017)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Ref #12034
  
  This commit releases many GPU resources when a surface becomes invisible
  and rebuilds it on the next draw. I don't say "all" because there are
  still some things we can improve on (Kitty images).
  
  We previously held onto all GPU resources for the lifetime of the
  surface regardless of its visibility state. This is 3x (for
  triple-buffering): screen render targets, uniform/cell/custom shader
  buffers, font textures, and more.
  
  Measured on macOS (Metal):
  
  | Measurement (1 visible + 20 hidden tabs)    | Before    | After   |
  |---------------------------------------------|-----------|---------|
  | Tracked GPU allocations (steady state)      | 384.6 MiB | 18.3 MiB |
  | `MTLDevice.currentAllocatedSize`            | 393.3 MiB | 19.7 MiB |
  | `footprint` IOSurface (dirty)               | 309 MB    | 15 MB   |
  | Swap chain rebuild on unhide (42 tab switches) | n/a | avg 0.43 ms,
  max 0.55 ms |
  
  As you can see, importantly, swap chain rebuild is fast: 0.43ms average.
  That means that the rebuild is imperceptible and happens well within a
  frame draw time.
  
  This is macOS only, but most of the work was in the generic renderer.
  GTK only needs to call `releaseGpuResources` when it becomes invisible
  to get the same benefits. I didn't have my VM handy to test this yet so
  I didn't include it.
  ```
- [`ee8095d`](https://github.com/ghostty-org/ghostty/commit/ee8095d37d9813669688cf2f666756e607b84713) terminal/snapshot: use stack fallback for record scratch ([@jparise](https://github.com/jparise))
  ```text
  Use a bounded 512-byte stack fallback for complete-snapshot record
  scratch. Small records avoid heap growth while larger records continue
  through the heap allocator.
  ```
- [`73e53ce`](https://github.com/ghostty-org/ghostty/commit/73e53ceeac4d81b59d228db32de933d8114d42cd) i18n: update fr_FR translations ([@flou](https://github.com/flou))
- [`0f35043`](https://github.com/ghostty-org/ghostty/commit/0f35043c9ac588811f22c732ac5392850f22381e) terminal: execute C0 controls 0x10-0x1F in the ground state ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #14021
  
  The ground state UTF-8 fast paths only classified 0x00-0x0F plus 0x1B (escape)
  as C0 controls. The remaining C0 bytes (0x10-0x1A, 0x1C-0x1F) were decoded
  as ordinary codepoints and routed to print as if they were text.
  
  This resulted in incorrect grids but also very weird font fallback, e.g.
  U+0014 would find CJK fonts.
  
  This commit fixes this by routing every ground state C0 byte except ESC to
  execute as it should be.
  ```
- [`6dcf68f`](https://github.com/ghostty-org/ghostty/commit/6dcf68fc0b12e8caebbfc43770d66edac124b4f8) terminal: execute C0 controls 0x10-0x1F in the ground state ([#14022](https://github.com/ghostty-org/ghostty/issues/14022)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #14021
  
  The ground state UTF-8 fast paths only classified 0x00-0x0F plus 0x1B
  (escape) as C0 controls. The remaining C0 bytes (0x10-0x1A, 0x1C-0x1F)
  were decoded as ordinary codepoints and routed to print as if they were
  text.
  
  This resulted in incorrect grids but also very weird font fallback, e.g.
  U+0014 would find CJK fonts.
  
  This commit fixes this by routing every ground state C0 byte except ESC
  to execute as it should be.
  ```
- [`40a40f8`](https://github.com/ghostty-org/ghostty/commit/40a40f848dfca8c5edbc0098dd828aec03ae8e64) terminal: ignore UTF-8-decoded C1 controls in the ground state ([@mitchellh](https://github.com/mitchellh))
  ```text
  Drop UTF-8 decoded C1 controls entirely. This matches xterm's default
  behavior which is our standard policy (but note it diverges from libvte
  which executes them). There isn't really any standard I could find
  around this.
  
  The ground state UTF-8 fast paths (both the scalar decoder and the
  batched SIMD path) previously treated decoded codepoints C1 control
  codepoints as normal UTF-8 text and routed them to print.
  ```
- [`88f57ee`](https://github.com/ghostty-org/ghostty/commit/88f57ee66eeaad4da77b414b245f7b6693348985) terminal: ignore UTF-8-decoded C1 controls in the ground state ([#14023](https://github.com/ghostty-org/ghostty/issues/14023)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Drop UTF-8 decoded C1 controls entirely. This matches xterm's default
  behavior which is our standard policy (but note it diverges from libvte
  which executes them). There isn't really any standard I could find
  around this.
  
  The ground state UTF-8 fast paths (both the scalar decoder and the
  batched SIMD path) previously treated decoded codepoints C1 control
  codepoints as normal UTF-8 text and routed them to print.
  ```
- [`851751a`](https://github.com/ghostty-org/ghostty/commit/851751a1167a05d83f08c010a7b1e92f435f783f) macOS: clean up deprecated toolbar button ([@bo2themax](https://github.com/bo2themax))
- [`5f5b988`](https://github.com/ghostty-org/ghostty/commit/5f5b988c5236facfe8d2439203d9ee9d5b636cf8) i18n: update fr_FR translations ([#13971](https://github.com/ghostty-org/ghostty/issues/13971)) ([@trag1c](https://github.com/trag1c))
  ```text
  Update missing french translations for Ghostty 1.4
  (https://github.com/ghostty-org/ghostty/issues/13766)
  ```
- [`7a15898`](https://github.com/ghostty-org/ghostty/commit/7a15898bc813558a25c4beffd7391dad14cbb20c) macOS: use same ResetZoomAccessoryView ([@bo2themax](https://github.com/bo2themax))
- [`1abd53e`](https://github.com/ghostty-org/ghostty/commit/1abd53ee537a93bb33107a415fe4f4131bcf0f5b) macOS: clean up deprecated toolbar button ([#14027](https://github.com/ghostty-org/ghostty/issues/14027)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This button is a leftover from cf6017e777cda0e0c131b616f408c9a81644b5d7,
  we're now using tab's and titlebar's accessory view to display unzoom
  buttons, no need to keep them.
  ```
- [`15ff186`](https://github.com/ghostty-org/ghostty/commit/15ff186f65ca0bdbd1fa397ab03908d59de16463) macOS: use same ResetZoomAccessoryView ([#14028](https://github.com/ghostty-org/ghostty/issues/14028)) ([@mitchellh](https://github.com/mitchellh))
- [`6244458`](https://github.com/ghostty-org/ghostty/commit/6244458a11f7c83c9c8774d2f5d27aba027c00fc) Update po/ru.po ([@derVedro](https://github.com/derVedro))
- [`84dff76`](https://github.com/ghostty-org/ghostty/commit/84dff76b1383f0535657902b64cb614a34bd48e8) Update po/ru.po ([@derVedro](https://github.com/derVedro))
- [`6688aa0`](https://github.com/ghostty-org/ghostty/commit/6688aa072f87dcb169fa1a49dcf5eadc9ed87956) renderer: park DisplayLink while idle ([@mitchellh](https://github.com/mitchellh))
  ```text
  #14033
  
  Pause the CVDisplayLink when there isn't any real work to do.
  
  Start the link after updateFrame rebuilds cells, keep it running while
  cell changes or animations remain pending, and resync it from the
  no-redraw path to sleep it again.
  
  I also did some benchmark to measure the cost of starting/stopping the
  display link since this includes a lot more of that and I found that
  a continuously running link used 29 to 35 us of CPU per callback, while
  starting and stopping it for every frame used 103 to 121 us. So, in some
  pathological case this can be worse, but its still microseconds, and in
  the normal case this helps Ghostty sleep a lot more.
  ```
- [`d9840f3`](https://github.com/ghostty-org/ghostty/commit/d9840f3c8fc230c7768ae760c412974e9fc923bb) renderer: park DisplayLink while idle ([#14035](https://github.com/ghostty-org/ghostty/issues/14035)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  #14033
  
  Pause the CVDisplayLink when there isn't any real work to do.
  
  Start the link after updateFrame rebuilds cells, keep it running while
  cell changes or animations remain pending, and resync it from the
  no-redraw path to sleep it again.
  
  I also did some benchmark to measure the cost of starting/stopping the
  display link since this includes a lot more of that and I found that a
  continuously running link used 29 to 35 us of CPU per callback, while
  starting and stopping it for every frame used 103 to 121 us. So, in some
  pathological case this can be worse, but its still microseconds, and in
  the normal case this helps Ghostty sleep a lot more.
  ```
- [`b6ac6e1`](https://github.com/ghostty-org/ghostty/commit/b6ac6e1d479f29fb8194f86ec24b72901aa94c21) Revert "macOS: use same ResetZoomAccessoryView ([#14028](https://github.com/ghostty-org/ghostty/issues/14028))" ([@bo2themax](https://github.com/bo2themax))
  ```text
  This reverts commit 15ff186f65ca0bdbd1fa397ab03908d59de16463, reversing
  changes made to 1abd53ee537a93bb33107a415fe4f4131bcf0f5b.
  ```
- [`0a9f47c`](https://github.com/ghostty-org/ghostty/commit/0a9f47cae0bc3cb653ea52fbd4e1d632b79dd91a) macOS: update note about tab accessory view ([@bo2themax](https://github.com/bo2themax))
- [`b69f612`](https://github.com/ghostty-org/ghostty/commit/b69f612672f4e31e20dec2ee2684d295aec149f1) macOS: update note about tab accessory view ([#14038](https://github.com/ghostty-org/ghostty/issues/14038)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Reverts: #14028
  ```
- [`915977a`](https://github.com/ghostty-org/ghostty/commit/915977a484da9d9b93b3a30ac80ff068c5c3c6a8) i18n(ru): equalize splits ([@derVedro](https://github.com/derVedro))
- [`522ebdd`](https://github.com/ghostty-org/ghostty/commit/522ebdd0a313ef366d3567694e3588b780fae8ee) build(deps): bump hustcer/milestone-action from 3.1 to 3.2 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [hustcer/milestone-action](https://github.com/hustcer/milestone-action) from 3.1 to 3.2.
  - [Release notes](https://github.com/hustcer/milestone-action/releases)
  - [Changelog](https://github.com/hustcer/milestone-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/hustcer/milestone-action/compare/ebed8d5daafd855a600d7e665c1b130f06d24130...2f38355153344ccaaa44b5b5fcff9f604dff1b45)
  
  ---
  updated-dependencies:
  - dependency-name: hustcer/milestone-action
    dependency-version: '3.2'
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`f349d10`](https://github.com/ghostty-org/ghostty/commit/f349d108431007dac0d908af33301e3cc460b2f3) build(deps): bump hustcer/milestone-action from 3.1 to 3.2 ([#14040](https://github.com/ghostty-org/ghostty/issues/14040)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [hustcer/milestone-action](https://github.com/hustcer/milestone-action)
  from 3.1 to 3.2.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/hustcer/milestone-action/releases">hustcer/milestone-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v3.2</h2>
  <h2>[3.2] - 2026-08-25</h2>
  <h3>Bug Fixes</h3>
  <ul>
  <li>Harden action inputs and make GraphQL file lookup path-independent
  (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/168">#168</a>)</li>
  <li>Look up milestones by title across all states with pagination (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/170">#170</a>)</li>
  <li>Guard GITHUB_OUTPUT, surface GraphQL errors and tighten is-int (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/172">#172</a>)</li>
  <li>Require title for create action and sync stale docs (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/174">#174</a>)</li>
  <li>Send milestone fields as raw strings and harden action inputs (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/176">#176</a>)</li>
  </ul>
  <h3>Deps</h3>
  <ul>
  <li>Upgrade hustcer/setup-nu to v3.25 &amp; Nu to 0.113.1</li>
  <li>Upgrade hustcer/setup-nu to v3.27 and Nu to 0.115</li>
  <li>Upgrade Nu to 0.115.1</li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/hustcer/milestone-action/blob/main/CHANGELOG.md">hustcer/milestone-action's
  changelog</a>.</em></p>
  <blockquote>
  <h1>Changelog</h1>
  <p>All notable changes to this project will be documented in this
  file.</p>
  <h2>[3.2] - 2026-08-25</h2>
  <h3>Bug Fixes</h3>
  <ul>
  <li>Harden action inputs and make GraphQL file lookup path-independent
  (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/168">#168</a>)</li>
  <li>Look up milestones by title across all states with pagination (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/170">#170</a>)</li>
  <li>Guard GITHUB_OUTPUT, surface GraphQL errors and tighten is-int (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/172">#172</a>)</li>
  <li>Require title for create action and sync stale docs (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/174">#174</a>)</li>
  <li>Send milestone fields as raw strings and harden action inputs (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/176">#176</a>)</li>
  </ul>
  <h3>Deps</h3>
  <ul>
  <li>Upgrade hustcer/setup-nu to v3.25 &amp; Nu to 0.113.1</li>
  <li>Upgrade hustcer/setup-nu to v3.27 and Nu to 0.115</li>
  <li>Upgrade Nu to 0.115.1</li>
  </ul>
  <h2>[3.1] - 2026-01-23</h2>
  <h3>Documentation</h3>
  <ul>
  <li>Update milestone-action version in README (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/162">#162</a>)</li>
  </ul>
  <h3>Features</h3>
  <ul>
  <li>Break before sleep when milestone found</li>
  </ul>
  <h3>Miscellaneous Tasks</h3>
  <ul>
  <li>Update README.md (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/166">#166</a>)</li>
  </ul>
  <h3>Deps</h3>
  <ul>
  <li>Update Nu to 0.109.1</li>
  <li>Update Nushell to 0.110.0 (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/167">#167</a>)</li>
  <li>Upgrade hustcer/setup-nu to v3.22</li>
  </ul>
  <h1>Changelog</h1>
  <p>All notable changes to this project will be documented in this
  file.</p>
  <h2>[3.0] - 2025-10-26</h2>
  <p>This release introduces changes that may impact some users. If the
  action fails due to insufficient permissions, please add the
  <code>issues: write</code> and <code>pull-requests: write</code>
  permissions to your workflow. Additionally, the API for binding
  milestones has been modified. Due to these changes, the major version
  has been incremented to 3.</p>
  <h3>Bug Fixes</h3>
  <ul>
  <li>Try to fix GitHub Projects (classic) deprecation warning by using
  REST API instead of GraphQL (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/157">#157</a>)</li>
  <li>Fix &quot;Resource not accessible by integration&quot; error for
  issue milestone binding by adding <code>issues: write</code>
  permission</li>
  </ul>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/2f38355153344ccaaa44b5b5fcff9f604dff1b45"><code>2f38355</code></a>
  Bump to v3.2</li>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/90d61222172fcab928f4097d7ac0f9b777f8c6a6"><code>90d6122</code></a>
  deps: Upgrade Nu to 0.115.1</li>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/e587063f374a27424be13284709902ef21d0e7e2"><code>e587063</code></a>
  fix: Send milestone fields as raw strings and harden action inputs (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/176">#176</a>)</li>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/cc2b756fd4aa0c6296b7268f41108dc88bfb8228"><code>cc2b756</code></a>
  fix: Require title for create action and sync stale docs (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/174">#174</a>)</li>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/f8cedae0c15efb735341ecea49835c86190dee13"><code>f8cedae</code></a>
  fix: Guard GITHUB_OUTPUT, surface GraphQL errors and tighten is-int (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/172">#172</a>)</li>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/b57a2e26d7ae416cd8f283c8ddcf0022639b0a99"><code>b57a2e2</code></a>
  fix: Look up milestones by title across all states with pagination (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/170">#170</a>)</li>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/3ba8f40c9539a0d3b5ac92732bd3a26f3a9e80df"><code>3ba8f40</code></a>
  fix: Harden action inputs and make GraphQL file lookup path-independent
  (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/168">#168</a>)</li>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/1e6a3fcc554f6c07ada4feabb0b1935aa60243d3"><code>1e6a3fc</code></a>
  deps: Upgrade hustcer/setup-nu to v3.27 and Nu to 0.115</li>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/913159549289b377b4d0c9c830101da8d4c82387"><code>9131595</code></a>
  deps: Upgrade hustcer/setup-nu to v3.25 &amp; Nu to 0.113.1</li>
  <li>See full diff in <a
  href="https://github.com/hustcer/milestone-action/compare/ebed8d5daafd855a600d7e665c1b130f06d24130...2f38355153344ccaaa44b5b5fcff9f604dff1b45">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=hustcer/milestone-action&package-manager=github_actions&previous-version=3.1&new-version=3.2)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`f2d5758`](https://github.com/ghostty-org/ghostty/commit/f2d5758f6305867dc36b36293c6165d8152b853e) terminal/snapshot: use stack fallback for record scratch ([#14018](https://github.com/ghostty-org/ghostty/issues/14018)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Use a bounded 512-byte stack fallback for complete-snapshot record
  scratch. Small records avoid heap growth while larger records continue
  through the heap allocator.
  
  This usually means 2 fewer allocations per encode, resulting in a small
  performance improvement in a local benchmark:
  
  | Workload | `main` median | Branch median | Change |
  |---|---:|---:|---:|
  | Empty, 50k encodes | 135.06 ms | 130.76 ms | **3.2% faster** |
  | 1 MiB ASCII, 500 encodes | 280.75 ms | 281.25 ms | **0.2% slower**,
  within noise |
  | 1 MiB styled, 200 encodes | 1,023.02 ms | 996.32 ms | **2.6% faster**
  |
  ```
- [`278b4e2`](https://github.com/ghostty-org/ghostty/commit/278b4e2fc7aab0c5073afdfe2570f27a5a4b9142) i18n(ru): refine Russian translation ([@derVedro](https://github.com/derVedro))
- [`e9ad4b1`](https://github.com/ghostty-org/ghostty/commit/e9ad4b1d631ec91c8cad401700fee1754612ef33) macOS: fix non control keys are not working for AppleScript ([#13205](https://github.com/ghostty-org/ghostty/issues/13205)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `send key` only works for control keys like `enter` currently; this adds
  (fixes) the support for other keys listed as available. Found by
  @paaloeye in #13180
  
  The core of this fix is relying on `UCKeyTranslate` to get the
  corresponding character and code point from a key code using
  `KeyboardLayout.character(for:modifiers:)`.
  
  ScriptKeyEventCommand now respects `macos-option-as-alt`, and attach
  `text`, `unshifted_codepoint` and `consumed_mods` under the same
  condition as a manual input events like in `performKeyEquivalent` and
  `localEventKeyDown`.
  
  ## AI Disclosure
  
  Claude did the heavy lifting, I reviewed and rephrased some of the
  comments it generated. And ofc reviewed and tested myself.
  ```
- [`28b5bf9`](https://github.com/ghostty-org/ghostty/commit/28b5bf905986f9e795466b7995640d80c44c16bc) font: update embedded Noto emoji fonts ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #14046
  
  Update Noto Color Emoji from v2.034 to v2.051 and Noto Emoji
  Regular from v1.002 to v3.005.
  
  The old assets predate Unicode 15.0 and decompose newer ZWJ sequences
  into separate glyphs. This causes sequences such as the Emoji 15.1
  head-shaking faces to overlap neighboring terminal cells. The new
  assets provide the missing sequence glyphs through Unicode 17.0.
  
  New supported glyphs too:
  
  | Codepoint | Glyph | Name |
  |-----------|-------|------|
  | U+1F6D8 | 🛘 | LANDSLIDE |
  | U+1F6DC | 🛜 | WIRELESS |
  | U+1FA75 | 🩵 | LIGHT BLUE HEART |
  | U+1FA76 | 🩶 | GREY HEART |
  | U+1FA77 | 🩷 | PINK HEART |
  | U+1FA87 | 🪇 | MARACAS |
  | U+1FA88 | 🪈 | FLUTE |
  | U+1FA89 | 🪉 | HARP |
  | U+1FA8A | 🪊 | TROMBONE |
  | U+1FA8E | 🪎 | TREASURE CHEST |
  | U+1FA8F | 🪏 | SHOVEL |
  | U+1FAAD | 🪭 | FOLDING HAND FAN |
  | U+1FAAE | 🪮 | HAIR PICK |
  | U+1FAAF | 🪯 | KHANDA |
  | U+1FABB | 🪻 | HYACINTH |
  | U+1FABC | 🪼 | JELLYFISH |
  | U+1FABD | 🪽 | WING |
  | U+1FABE | 🪾 | LEAFLESS TREE |
  | U+1FABF | 🪿 | GOOSE |
  | U+1FAC6 | 🫆 | FINGERPRINT |
  | U+1FAC8 | 🫈 | HAIRY CREATURE |
  | U+1FACD | 🫍 | ORCA |
  | U+1FACE | 🫎 | MOOSE |
  | U+1FACF | 🫏 | DONKEY |
  | U+1FADA | 🫚 | GINGER ROOT |
  | U+1FADB | 🫛 | PEA POD |
  | U+1FADC | 🫜 | ROOT VEGETABLE |
  | U+1FADF | 🫟 | SPLATTER |
  | U+1FAE8 | 🫨 | SHAKING FACE |
  | U+1FAE9 | 🫩 | FACE WITH BAGS UNDER EYES |
  | U+1FAEA | 🫪 | DISTORTED FACE |
  | U+1FAEF | 🫯 | FIGHT CLOUD |
  | U+1FAF7 | 🫷 | LEFTWARDS PUSHING HAND |
  | U+1FAF8 | 🫸 | RIGHTWARDS PUSHING HAND |
  ```
- [`890aa63`](https://github.com/ghostty-org/ghostty/commit/890aa63dbbd586c6687a60b3736109203649d8dc) font: update embedded Noto emoji fonts ([#14047](https://github.com/ghostty-org/ghostty/issues/14047)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #14046
  
  Update Noto Color Emoji from v2.034 to v2.051 and Noto Emoji Regular
  from v1.002 to v3.005.
  
  The old assets predate Unicode 15.0 and decompose newer ZWJ sequences
  into separate glyphs. This causes sequences such as the Emoji 15.1
  head-shaking faces to overlap neighboring terminal cells. The new assets
  provide the missing sequence glyphs through Unicode 17.0.
  
  New supported glyphs too:
  
  | Codepoint | Glyph | Name |
  |-----------|-------|------|
  | U+1F6D8 | 🛘 | LANDSLIDE |
  | U+1F6DC | 🛜 | WIRELESS |
  | U+1FA75 | 🩵 | LIGHT BLUE HEART |
  | U+1FA76 | 🩶 | GREY HEART |
  | U+1FA77 | 🩷 | PINK HEART |
  | U+1FA87 | 🪇 | MARACAS |
  | U+1FA88 | 🪈 | FLUTE |
  | U+1FA89 | 🪉 | HARP |
  | U+1FA8A | 🪊 | TROMBONE |
  | U+1FA8E | 🪎 | TREASURE CHEST |
  | U+1FA8F | 🪏 | SHOVEL |
  | U+1FAAD | 🪭 | FOLDING HAND FAN |
  | U+1FAAE | 🪮 | HAIR PICK |
  | U+1FAAF | 🪯 | KHANDA |
  | U+1FABB | 🪻 | HYACINTH |
  | U+1FABC | 🪼 | JELLYFISH |
  | U+1FABD | 🪽 | WING |
  | U+1FABE | 🪾 | LEAFLESS TREE |
  | U+1FABF | 🪿 | GOOSE |
  | U+1FAC6 | 🫆 | FINGERPRINT |
  | U+1FAC8 | 🫈 | HAIRY CREATURE |
  | U+1FACD | 🫍 | ORCA |
  | U+1FACE | 🫎 | MOOSE |
  | U+1FACF | 🫏 | DONKEY |
  | U+1FADA | 🫚 | GINGER ROOT |
  | U+1FADB | 🫛 | PEA POD |
  | U+1FADC | 🫜 | ROOT VEGETABLE |
  | U+1FADF | 🫟 | SPLATTER |
  | U+1FAE8 | 🫨 | SHAKING FACE |
  | U+1FAE9 | 🫩 | FACE WITH BAGS UNDER EYES |
  | U+1FAEA | 🫪 | DISTORTED FACE |
  | U+1FAEF | 🫯 | FIGHT CLOUD |
  | U+1FAF7 | 🫷 | LEFTWARDS PUSHING HAND |
  | U+1FAF8 | 🫸 | RIGHTWARDS PUSHING HAND |
  ```
- [`572fd58`](https://github.com/ghostty-org/ghostty/commit/572fd5837728da2363168f035743597767b5b237) macOS: use the same default BellFeatures as config ([@bo2themax](https://github.com/bo2themax))
- [`4f4589f`](https://github.com/ghostty-org/ghostty/commit/4f4589f31f2ca196fc88731dfcdc77e1cbde9852) macOS: use the same default BellFeatures as config ([#14049](https://github.com/ghostty-org/ghostty/issues/14049)) ([@mitchellh](https://github.com/mitchellh))
- [`2de1596`](https://github.com/ghostty-org/ghostty/commit/2de15961157343ff7dbeacc1281df97a3af6c624) macos: normalize action working directory paths ([@mitchellh](https://github.com/mitchellh))
  ```text
  Discussion #14048
  
  Directory URLs no longer export a trailing slash through PWD, which
  keeps zsh's %1~ prompt expansion from resolving to an empty string.
  
  A shared URL helper removes trailing separators while preserving the
  filesystem root and percent-decoding behavior. Tests cover normal,
  repeated, encoded, and root paths.
  ```
- [`07abbd1`](https://github.com/ghostty-org/ghostty/commit/07abbd1e7ee1f98d40cffacf537577e0bcb3522b) Update macos/Sources/Helpers/Extensions/URL+Extension.swift ([@mitchellh](https://github.com/mitchellh))
- [`1c3a4a8`](https://github.com/ghostty-org/ghostty/commit/1c3a4a8314669a97177e4b39cd5d6451f4c257f3) Update macos/Sources/Helpers/Extensions/URL+Extension.swift ([@mitchellh](https://github.com/mitchellh))
- [`fac595c`](https://github.com/ghostty-org/ghostty/commit/fac595c741aaec126d1cf0085dacfa63019a02c4) macos: normalize action working directory paths ([#14051](https://github.com/ghostty-org/ghostty/issues/14051)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Discussion #14048
  
  Directory URLs no longer export a trailing slash through PWD, which
  keeps zsh's %1~ prompt expansion from resolving to an empty string.
  
  A shared URL helper removes trailing separators while preserving the
  filesystem root and percent-decoding behavior. Tests cover normal,
  repeated, encoded, and root paths.
  ```
- [`5aeb693`](https://github.com/ghostty-org/ghostty/commit/5aeb693b7727b0dc6fcc9193bc1d2453af3bcb9a) i18n: Russian translation for 1.4 ([#13809](https://github.com/ghostty-org/ghostty/issues/13809)) ([@trag1c](https://github.com/trag1c))
- [`9af9348`](https://github.com/ghostty-org/ghostty/commit/9af934813a32262ab525673840ccd76ed7df2f52) Merge from upstream ([@mohshami](https://github.com/mohshami))
- [`eb722cb`](https://github.com/ghostty-org/ghostty/commit/eb722cb26dfe3fb5dc481181ae463940492cd742) terminal: mark the previous row dirty when clearing its spacer head ([@fornwall](https://github.com/fornwall))
  ```text
  Erasing a wrapped wide character at the start of a row (ECH or DCH)
  also clears the spacer head it left at the end of the previous row,
  but that row was never marked dirty. With both rows visible, an
  incremental render kept the stale spacer head on screen until
  something unrelated redrew that row.
  
  The clearing happens in the row-start branch of splitCellBoundary.
  clearCells doesn't do dirty tracking, and both callers only mark
  the cursor row, so mark the previous row at the point it's mutated.
  
  The added dirty assertions fail without the fix.
  ```
- [`76e568b`](https://github.com/ghostty-org/ghostty/commit/76e568b475fe88f5506be33ad1a684f3c1eae85e) terminal: mark the previous row dirty when clearing its spacer head ([#14054](https://github.com/ghostty-org/ghostty/issues/14054)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Erasing a wrapped wide character at the start of a row (`ECH` or `DCH`)
  also clears the spacer head it left at the end of the previous row, but
  that row was never marked dirty. With both rows visible, an incremental
  render kept the stale spacer head on screen until something unrelated
  redrew that row.
  
  The clearing happens in the row-start branch of `splitCellBoundary`.
  `clearCells` doesn't do dirty tracking, and both callers only mark the
  cursor row, so mark the previous row at the point it's mutated.
  
  The added dirty assertions fail without the fix.
  
  ## AI Disclaimer
  Claude did the heavy lifting - identifying the root cause, generating
  code and description. I reviewed and iterated on it to move around and
  tweak tests, comments and reduce verboseness. Verified the end user
  visible behaviour improvement with a script that coloured the wide
  character, which made the stale rendering visible until a switch to the
  alt screen and back cleared it it.
  ```
- [`58f43d5`](https://github.com/ghostty-org/ghostty/commit/58f43d56289d234271e1e829712e2f043c88278f) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`777929a`](https://github.com/ghostty-org/ghostty/commit/777929a8fe603574474f6e1c9c0a35c08af1a2d9) macOS: review windows when closing multiple tabs ([@bo2themax](https://github.com/bo2themax))
- [`4540d49`](https://github.com/ghostty-org/ghostty/commit/4540d499ae463ad7b90f28f6f852f64f844c160f) macOS: review windows when closing multiple tabs ([#14062](https://github.com/ghostty-org/ghostty/issues/14062)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  We can also make close undoable when quitting, i'll add it as a follow
  up pr.
  
  <img width="573" height="450" alt="Xnip2026-08-28_19-25-02"
  src="https://github.com/user-attachments/assets/3b4f34f4-9ee6-4180-beb7-f90e98c8aa40"
  />
  ```
- [`c8c4526`](https://github.com/ghostty-org/ghostty/commit/c8c4526e43e6f832ab5d88759cde98a7b2129886) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`300a0df`](https://github.com/ghostty-org/ghostty/commit/300a0dfcb6a6081ea2ead620445965d036f2ae74) Add the Serbian and Serbian Latin translations ([@kostich](https://github.com/kostich))
- [`74e0bfd`](https://github.com/ghostty-org/ghostty/commit/74e0bfdf24dc02d9cc43d5e9356b7887467abe21) Register code ownership ([@kostich](https://github.com/kostich))
- [`7aa4767`](https://github.com/ghostty-org/ghostty/commit/7aa47671482a29875664f112dd503235d8c421ff) Add new translations to locales file ([@kostich](https://github.com/kostich))
- [`635abb7`](https://github.com/ghostty-org/ghostty/commit/635abb7ee81c8f3f4969255d24e0c24bb47f56cc) Update po/sr.po ([@kostich](https://github.com/kostich))
- [`6cd684d`](https://github.com/ghostty-org/ghostty/commit/6cd684d5d3b2a83c9966b6c5ba239d36fbd937a9) gtk: fix stale pointers to property bindings ([@dkinzler](https://github.com/dkinzler))
  ```text
  Previously, the property binding created in `Surface.bindIsSplit` would
  get freed automatically when the source object (the SplitTree widget)
  got finalized. A subsequent call to `bindIsSplit` could then cause a
  crash by using the stale pointer to the binding. This bug could e.g. be
  triggered by dragging the surface from a single-surface tab to another
  tab.
  
  We now create an extra reference to the binding object so that Surface
  essentially owns the binding and is responsible for freeing it.
  
  Updated the binding in `SurfaceScrolledWindow` to use the same pattern.
  That one was probably fine, because the binding is only created once,
  but let's be safe.
  ```
- [`e8ba5d2`](https://github.com/ghostty-org/ghostty/commit/e8ba5d2c2749e3ac85a280a6f854d9cf3e1646cc) Standardize how config/setting/preference is translated ([@kostich](https://github.com/kostich))
- [`1ae448c`](https://github.com/ghostty-org/ghostty/commit/1ae448c23b42a14b209f50e2b2de4415bfed37c9) Fix translation of sequences ([@kostich](https://github.com/kostich))
- [`2a0371b`](https://github.com/ghostty-org/ghostty/commit/2a0371b28f2077b5553a72d8f1cb5ff878634855) Apply batched suggestions from code review ([@kostich](https://github.com/kostich))
- [`17a2474`](https://github.com/ghostty-org/ghostty/commit/17a24746c4785c24bb3ff6f6758cdccf4bcb38c1) Use the correct accusative form for inanimata ([@kostich](https://github.com/kostich))
- [`e3969ab`](https://github.com/ghostty-org/ghostty/commit/e3969ab494e62bf5a66270e6bae56665faf8fce3) Align translations for current and to left/right ([@kostich](https://github.com/kostich))
- [`84c8e7d`](https://github.com/ghostty-org/ghostty/commit/84c8e7d829ce67f7c079e40cff646e0784986e9b) Align translation for Focus ([@kostich](https://github.com/kostich))
- [`97f57ed`](https://github.com/ghostty-org/ghostty/commit/97f57edccc10cb5ccef34d9d4c94276748bbd953) renderer: vsync unfocused surfaces while dirty ([@j-c-m](https://github.com/j-c-m))
  ```text
  6ae1784f4
  
  Unfocused surfaces stopped the CVDisplayLink and encoded a GPU
  frame on every PTY wakeup. A burst of close writes became that many
  Metal submits instead of one vsync.
  
  Keep the link running while the surface is visible and dirty or
  animating, whether or not it is focused. Idle surfaces still park.
  Focus continues to gate cursor blink, custom-shader animation, and
  QoS.
  ```
- [`caf48a4`](https://github.com/ghostty-org/ghostty/commit/caf48a41ee5c3861c786270d64bac950f2513012) main: fix inverted allow_stack_tracing condition ([@jcollie](https://github.com/jcollie))
  ```text
  The Zig 0.16.0 update dropped the negation from the std default
  (!strip_debug_info), disabling stack traces in every unstripped build.
  
  AI disclosure: Claude Fable was used to diagnose the problem and find the
  fix. Commit message was written by me.
  
  Claude-Session: https://claude.ai/code/session_01QfzQME46DQXwMWa43bQaa3
  ```
- [`069497e`](https://github.com/ghostty-org/ghostty/commit/069497e0ca7d02c073d69e80003c1e0f0b067ee6) gtk: fix stale pointers to property bindings ([#14065](https://github.com/ghostty-org/ghostty/issues/14065)) ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes #14037 where dragging the surface from a tab with just a single
  surface to another tab causes a crash.
  
  The cause of the crash is a stale pointer to the property binding
  created in `Surface.bindIsSplit`. When the surface is moved,
  `SplitTree.moveSplit` first updates the two split tree data structures
  of the source/target tab and then calls `bindIsSplit` to bind the
  `is-split` property of the moved surface to the `SplitTree` widget in
  the target tab. When `bindIsSplit` is called, the `SplitTree` widget in
  the source tab has already been destroyed (because the source tab is now
  empty) which causes the old binding to be freed automatically and the
  pointer `Surface.is_split_binding` becomes stale. `bindIsSplit` then
  tries to run `is_split_binding.unbind()` which causes the crash.
  
  When you create a binding with `bindProperty`, the binding itself owns
  the initially created reference and it gets freed when the source or
  target object of the binding is finalized. To prevent this, we now
  create an extra reference to the binding object so that the Surface
  widget owns it and is responsible for freeing it. The binding can still
  get severed automatically, but the binding object itself will not be
  destroyed. This is the solution mentioned in the [GObject
  docs](https://docs.gtk.org/gobject/method.Object.bind_property.html).
  Alternatively, using a WeakRef for the pointer would have also worked.
  
  Updated the binding in `SurfaceScrolledWindow` to use the same pattern.
  That one was probably fine, because the binding should only be created
  once, but it doesn't hurt to be safe.
  
  I reproduced the crash on KDE, on Hyprland I just got a glib critical
  error message about the invalid pointer. That probably has to do with
  what exactly happens to the freed memory, or maybe differing versions.
  
  #### AI Disclosure
  
  Code and comments were written by myself, used GPT5.6 in researching
  gobject binding lifecycles.
  ```
- [`3baff3a`](https://github.com/ghostty-org/ghostty/commit/3baff3a069cb64a9d3739c2ff25423524b3b80ee) main: fix inverted allow_stack_tracing condition ([#14069](https://github.com/ghostty-org/ghostty/issues/14069)) ([@jcollie](https://github.com/jcollie))
  ```text
  The Zig 0.16.0 update dropped the negation from the std default
  (!strip_debug_info), disabling stack traces in every unstripped build.
  
  AI disclosure: Claude Fable was used to diagnose the problem and find
  the fix. Commit message was written by me.
  
  
  Claude-Session: https://claude.ai/code/session_01QfzQME46DQXwMWa43bQaa3
  ```
- [`166d2fe`](https://github.com/ghostty-org/ghostty/commit/166d2fe34d65bd1fa393fd8a213c57bc6119dfb9) build: update Sparkle to 2.9.4 ([@Svector-anu](https://github.com/Svector-anu))
- [`7b47213`](https://github.com/ghostty-org/ghostty/commit/7b47213f94058c3715205ce8fa73f7ae581a652c) Update VOUCHED list ([#14074](https://github.com/ghostty-org/ghostty/issues/14074)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14072#issuecomment-5463405035)
  from @bo2themax.
  
  Vouch: @Svector-anu
  ```
- [`a542359`](https://github.com/ghostty-org/ghostty/commit/a5423592cde24222c0d1719f780c54434b5b5d34) libghostty: use caller allocation on native freestanding ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  Native freestanding targets have neither an OS page allocator nor a usable default SMP allocator. Use the allocator supplied through libghostty for terminal page storage and make a missing C allocator fail with out-of-memory instead of instantiating hosted allocation machinery. Document that native freestanding C callers must supply an allocator for allocating operations.
  ```
- [`3376153`](https://github.com/ghostty-org/ghostty/commit/3376153a44e5269b9aee5e6d2524954c171e717b) build: support native freestanding libghostty-vt ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  Native freestanding targets cannot emit shared libraries and do not provide an OS page size, stack unwinder, hosted SIMD dependencies, or filesystem-backed Kitty graphics. Build only the static artifact for those targets, define the minimum alignment used for terminal pages, disable hosted-only defaults, and install the public headers with the archive.
  ```
- [`094d175`](https://github.com/ghostty-org/ghostty/commit/094d175efa506f87c296fd8a51371c68eea191b9) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`0a76c31`](https://github.com/ghostty-org/ghostty/commit/0a76c311527a20727764e3281eb4efa8c350058a) Update iTerm2 colorschemes ([#14077](https://github.com/ghostty-org/ghostty/issues/14077)) ([@jcollie](https://github.com/jcollie))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260824-153547-75c93ee
  ```
- [`98cd670`](https://github.com/ghostty-org/ghostty/commit/98cd670c0c2ccdd3f22c40c65a3306e933643ada) Update VOUCHED list ([#14079](https://github.com/ghostty-org/ghostty/issues/14079)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14078#discussioncomment-18203195)
  from @jcollie.
  
  Vouch: @and-rs
  ```
- [`81d28be`](https://github.com/ghostty-org/ghostty/commit/81d28beaa2e3c507299d0c1a5271c2af718212e3) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`090fca4`](https://github.com/ghostty-org/ghostty/commit/090fca451d2c63bc2a5ccec23ea54cedce62c6a6) terminal/kitty: validate POSIX shared memory names ([@mitchellh](https://github.com/mitchellh))
  ```text
  Update shared memory name validation according to the new spec:
  
  https://github.com/kovidgoyal/kitty/commit/22042970cf3a4668d02a1a7bcccca778ec864c21
  ```
- [`7035647`](https://github.com/ghostty-org/ghostty/commit/70356472faa9768eb37577430602fa30495eca81) build: update Sparkle to 2.9.4 ([#14072](https://github.com/ghostty-org/ghostty/issues/14072)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Update the macOS Sparkle dependency from 2.9.0 to 2.9.4.
  
  This keeps the Swift package resolution and all tag/tip release workflow
  downloads aligned on the same version. Sparkle 2.9.2 included fixes for
  GHSA-g3hp-f6mg-559v and GHSA-hg88-v3cw-3qrh; 2.9.4 is the current stable
  release.
  
  Validation:
  - verified the 2.9.4 release contains
  `Sparkle-for-Swift-Package-Manager.zip`
  - verified the lockfile revision matches the 2.9.4 tag
  - `jq empty` on `Package.resolved`
  - `git diff --check`
  
  I could not run Xcode package resolution locally because the active
  developer directory is Command Line Tools rather than a full Xcode
  installation.
  ```
- [`5f54958`](https://github.com/ghostty-org/ghostty/commit/5f5495826c7ad143c113c25f40cf2ef39d55e459) terminal: fix living item over-count in RefCountedSet.addWithId ([@mitchellh](https://github.com/mitchellh))
  ```text
  Reported in https://github.com/ghostty-org/ghostty/discussions/14064
  
  I validated this myself manually. The zero-ref branch of `addWithIdContext`
  incremented `living` unconditionally even if `upsert` resolved the value
  to an item that was already alive under a different ID.
  
  This would cause `living` to be invalid for each time this happened and
  the downstream effect was that `count()` drifted. I couldn't find any
  crashing or invalid effect except that this caused requested style memory
  to be over-provisioned.
  ```
- [`ec7929c`](https://github.com/ghostty-org/ghostty/commit/ec7929c9c2fffb1c46096f94cc9bdd6d57c85b72) terminal/kitty: validate POSIX shared memory names ([#14080](https://github.com/ghostty-org/ghostty/issues/14080)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Update shared memory name validation according to the new spec:
  
  
  https://github.com/kovidgoyal/kitty/commit/22042970cf3a4668d02a1a7bcccca778ec864c21
  ```
- [`83c5671`](https://github.com/ghostty-org/ghostty/commit/83c56715773d2b5f0e8b1d5bee68424514bb43e3) renderer: vsync unfocused surfaces while dirty ([#14068](https://github.com/ghostty-org/ghostty/issues/14068)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A follow on for #14035, we can now fix a long standing
  effiency/performance bug now that we park the display link while idle.
  This actually could cause "animated" un-focused windows to use more GPU
  than their focused counterparts. (AI Agent interfaces seem to love
  animation).
  
  6ae1784f4
  
  Unfocused surfaces stopped the CVDisplayLink and encoded a GPU frame on
  every PTY wakeup. A burst of close writes became that many Metal submits
  instead of one vsync.
  
  Keep the link running while the surface is visible and dirty or
  animating, whether or not it is focused. Idle surfaces still park.
  ```
- [`c181983`](https://github.com/ghostty-org/ghostty/commit/c181983253129f2803891a2d801951244ae5313c) build: update Sparkle to 2.9.6 and pin SPM ([@bo2themax](https://github.com/bo2themax))
- [`6d850fe`](https://github.com/ghostty-org/ghostty/commit/6d850fef7780f3461ee526eba16077ea9d7df8a6) Update VOUCHED list ([#14084](https://github.com/ghostty-org/ghostty/issues/14084)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14083#discussioncomment-18204946)
  from @jcollie.
  
  Vouch: @mgsloan
  ```
- [`3e2c0fa`](https://github.com/ghostty-org/ghostty/commit/3e2c0fa2db39215ee3b8098181baca7feb04ec27) gtk: do not warn when gtk-xft-dpi is -1 ([@mgsloan](https://github.com/mgsloan))
  ````text
  Before this change, ghostty frequently logs the following warning, even though a `gtk-xft-dpi` value of `-1` is valid and indicates default scaling.
  
  ```
  warning(gtk_ghostty_surface): gtk-xft-dpi has invalid value (-1), using default
  ```
  
  From [the gtk docs](https://docs.gtk.org/gtk4/property.Settings.gtk-xft-dpi.html):
  
  > The font resolution, in 1024 * dots/inch.
  >
  > -1 to use the default value.
  ````
- [`860cfb1`](https://github.com/ghostty-org/ghostty/commit/860cfb1d7958d0c5af09ff23488cfa6ea6665b46) Address review feedback ([@mgsloan](https://github.com/mgsloan))
- [`8af6897`](https://github.com/ghostty-org/ghostty/commit/8af6897c0afc63037a8a3efee4162a380e3a4572) gtk: do not warn when gtk-xft-dpi is -1 ([#14085](https://github.com/ghostty-org/ghostty/issues/14085)) ([@jcollie](https://github.com/jcollie))
  ````text
  Before this change, ghostty frequently logs the following warning, even
  though a `gtk-xft-dpi` value of `-1` is valid and indicates default
  scaling.
  
  ```
  warning(gtk_ghostty_surface): gtk-xft-dpi has invalid value (-1), using default
  ```
  
  From [the gtk
  docs](https://docs.gtk.org/gtk4/property.Settings.gtk-xft-dpi.html):
  
  > The font resolution, in 1024 * dots/inch.
  >
  > -1 to use the default value.
  ````
- [`807a51e`](https://github.com/ghostty-org/ghostty/commit/807a51e3e238b7ae81fdcb03f93e2e3e7d990716) updated localization file (andrejd-magix)
- [`36015c9`](https://github.com/ghostty-org/ghostty/commit/36015c99d06d671ba961c83b74d01d7ef45dc8d3) updated revision date (andrejd-magix)
- [`ee10453`](https://github.com/ghostty-org/ghostty/commit/ee10453a26dfc8ec5d7b612f5e4a5763da7cfa82) fix unclosed quote (andrejd-magix)
- [`abac4c2`](https://github.com/ghostty-org/ghostty/commit/abac4c2cb8122540d99f30645581918022a31fc8) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`10b7158`](https://github.com/ghostty-org/ghostty/commit/10b7158e8cd57f21f7327c73a6b2cdb2f498fdae) ci: cross-compile freestanding libghostty-vt ([@Uzaaft](https://github.com/Uzaaft))
- [`7fd93e0`](https://github.com/ghostty-org/ghostty/commit/7fd93e09ca6cbca7c4c4c0dbf2817ca49a82a2a4) build: update Sparkle to 2.9.6 and pin SPM ([#14082](https://github.com/ghostty-org/ghostty/issues/14082)) ([@mitchellh](https://github.com/mitchellh))
- [`0dc2032`](https://github.com/ghostty-org/ghostty/commit/0dc2032e6ab5f197f1d93f8eb1f1735a2b5091e1) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`ec3e384`](https://github.com/ghostty-org/ghostty/commit/ec3e384d2d7d86206fc3c71aa23a76b7bdb5eae9) Sync CODEOWNERS vouch list ([#14090](https://github.com/ghostty-org/ghostty/issues/14090)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Sync CODEOWNERS owners with vouch list.
  
  ## Added Users
  
  - @jakeriksen
  - @Kleshzz
  ```
- [`e8aa098`](https://github.com/ghostty-org/ghostty/commit/e8aa098674a42e2b4ed1b8c42f4224564ad9fc1e) Update VOUCHED list ([#14092](https://github.com/ghostty-org/ghostty/issues/14092)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14091#discussioncomment-18212381)
  from @pluiedev.
  
  Denounce: @thomas-trijindev
  ```
- [`0254a7f`](https://github.com/ghostty-org/ghostty/commit/0254a7f06f8b955f9107090581b22ad14f010fe8) Merge branch 'ghostty-org:main' into main ([@mohshami](https://github.com/mohshami))
- [`dfccdb2`](https://github.com/ghostty-org/ghostty/commit/dfccdb2d4dfdfa9da14664ae06f56f3db923d1e2) Implement needed modifications for issue [#12600](https://github.com/ghostty-org/ghostty/issues/12600) ([@mohshami](https://github.com/mohshami))
  ```text
  For middle-click-action
  * Kept the option "primary-paste" instead of "paste-primary" to keep
  backwards compatibility
  * Added the option "clipboard-paste"
  
  For copy-on-select
  * Added the both, none and primary options
  
  Updated config documentation
  
  Run zig fmt
  
  Move true/false options for copy-on-select to the compatibility handler
  
  Update src/config/Config.zig
  
  
  Update src/config/Config.zig
  
  
  Update src/config/Config.zig
  
  
  Update src/config/Config.zig
  
  
  Update src/config/Config.zig
  
  
  Update src/config/Config.zig
  
  
  Update src/Surface.zig
  
  
  Update src/Surface.zig
  
  
  Update src/config/Config.zig
  
  
  Update src/config/Config.zig
  
  
  Update src/config/Config.zig
  
  
  Update src/config/Config.zig
  
  
  Update src/config/Config.zig
  
  
  Update src/Surface.zig
  
  
  Update src/Surface.zig
  
  
  Reorder switch items
  
  Apply comment from kat
  
  Remove redundent code
  ```
- [`e80ce2e`](https://github.com/ghostty-org/ghostty/commit/e80ce2ed4cc603c0b52f9cb344f39c64048478e0) Fix build error ([@mohshami](https://github.com/mohshami))
- [`d4d8f62`](https://github.com/ghostty-org/ghostty/commit/d4d8f62262cb1a974a7d2470d5f79f811fab15e4) i18n: adjust and extend Ukrainian translation ([#13854](https://github.com/ghostty-org/ghostty/issues/13854)) ([@trag1c](https://github.com/trag1c))
- [`59141ad`](https://github.com/ghostty-org/ghostty/commit/59141ad21d7e86e48eec8ab8cbfe0095cb814303) add eu translation ([@erral](https://github.com/erral))
- [`fc7bfa6`](https://github.com/ghostty-org/ghostty/commit/fc7bfa60b4b5b40183387e52b782612f417812f3) ci: move freestanding build into test workflow ([@Uzaaft](https://github.com/Uzaaft))
- [`028af92`](https://github.com/ghostty-org/ghostty/commit/028af92ce3876ce1627163ce777f516b8218b410) terminal: clarify page allocator fallback ([@Uzaaft](https://github.com/Uzaaft))
- [`f6113ea`](https://github.com/ghostty-org/ghostty/commit/f6113ea2f5da697351ffe9dd91653427c4d27f90) Implement needed modifications for issue [#12600](https://github.com/ghostty-org/ghostty/issues/12600), more flexible copy-on-select and middle-click-action ([#12604](https://github.com/ghostty-org/ghostty/issues/12604)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  For middle-click-action
  * Kept the option "primary-paste" instead of "paste-primary" to keep
  backwards compatibility
  * Added the option "clipboard-paste"
  
  For copy-on-select
  * Added the both, none and primary options
  
  Updated config documentation
  
  Note: No AI was used, Even though I don't know Zig, I looked at the code
  and the modifications seemed easy enough
  
  Closes #12600
  ```
- [`c290639`](https://github.com/ghostty-org/ghostty/commit/c2906398be63f7eed567eee294ec09f291844b95) terminal: fix living item over-count in RefCountedSet.addWithId ([#14081](https://github.com/ghostty-org/ghostty/issues/14081)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Reported in https://github.com/ghostty-org/ghostty/discussions/14064
  
  I validated this myself manually. The zero-ref branch of
  `addWithIdContext` incremented `living` unconditionally even if `upsert`
  resolved the value to an item that was already alive under a different
  ID.
  
  This would cause `living` to be invalid for each time this happened and
  the downstream effect was that `count()` drifted. I couldn't find any
  crashing or invalid effect except that this caused requested style
  memory to be over-provisioned.
  
  cc @qwerasd205 since its ref counted set, but I did this work manually
  ❤️
  ```
- [`e8709b1`](https://github.com/ghostty-org/ghostty/commit/e8709b1f9ee1a1275c8ca2b3c22f40a4e4663137) Merge remote-tracking branch 'upstream/main' into add-serbian-translation ([@kostich](https://github.com/kostich))
- [`90f7759`](https://github.com/ghostty-org/ghostty/commit/90f775976328cd90b8cf12637b776f0689f2f4f8) Fix HTML/URL acronyms as agreed ([@kostich](https://github.com/kostich))
- [`8bf7e51`](https://github.com/ghostty-org/ghostty/commit/8bf7e517f0571c605a206aae00977c2e8e0cc7ce) Regenerate sr@latin.po from sr.po ([@kostich](https://github.com/kostich))
- [`5e02d00`](https://github.com/ghostty-org/ghostty/commit/5e02d0014de36ab776ac947e60ae5641c9674ca4) ci: require freestanding libghostty-vt builds ([@Uzaaft](https://github.com/Uzaaft))
- [`458f079`](https://github.com/ghostty-org/ghostty/commit/458f079f176632bf98d503bef1726472be505f07) Use the informal form ([@kostich](https://github.com/kostich))
- [`2c854a1`](https://github.com/ghostty-org/ghostty/commit/2c854a1aa42c96ec484f136fdd38d060bd6a7683) freestanding support ([#14076](https://github.com/ghostty-org/ghostty/issues/14076)) ([@mitchellh](https://github.com/mitchellh))
- [`149c9f5`](https://github.com/ghostty-org/ghostty/commit/149c9f562af3933493eb7dd275259eee9ce26f79) terminal: extract whole-terminal search orchestration from the search thread ([@mitchellh](https://github.com/mitchellh))
- [`32601cd`](https://github.com/ghostty-org/ghostty/commit/32601cd79a23618d0e64fd0c73bfd47e713be1ef) terminal/c: add search wrapper implementing the whole-terminal search API ([@mitchellh](https://github.com/mitchellh))
- [`cdef14a`](https://github.com/ghostty-org/ghostty/commit/cdef14a1fddd223b63fec60a8f59832a7e2a4db9) Remove X-Generator from the sr.po file ([@kostich](https://github.com/kostich))
- [`f0c918f`](https://github.com/ghostty-org/ghostty/commit/f0c918fc4b72c6c7e746db68f753d102a02bb206) terminal/c: allow freeing a search and its terminal in any order ([@mitchellh](https://github.com/mitchellh))
- [`f920291`](https://github.com/ghostty-org/ghostty/commit/f9202919f71951e7b5af2837afc30f181ad2168c) libghostty: add ghostty_search_* terminal search C API ([@mitchellh](https://github.com/mitchellh))
- [`674abd8`](https://github.com/ghostty-org/ghostty/commit/674abd8a1940c928d3a0fb0ca27d6ed6dfc5e3c0) example: add c-vt-search demonstrating the terminal search C API ([@mitchellh](https://github.com/mitchellh))
- [`76d9fce`](https://github.com/ghostty-org/ghostty/commit/76d9fcefef592617360577c9208490dc44d04a65) libghostty: set the search needle via ghostty_search_set, drop GhosttySearchOptions ([@mitchellh](https://github.com/mitchellh))
- [`4b51f52`](https://github.com/ghostty-org/ghostty/commit/4b51f521d4080f1bbdb113180f1b109404b6ad7f) libghostty: add terminal search API ([#14097](https://github.com/ghostty-org/ghostty/issues/14097)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This exposes the terminal search API through libghostty C and Zig APIs.
  
  This was previously available through the Zig APIs but forced our
  threading model. I've now extracted the full terminal search state to a
  new `terminal.search.TerminalSearch` structure so threading isn't
  forced. The C API is completely new.
  
  ## Example (C)
  
  ```c
  GhosttySearch search;
  ghostty_search_new(NULL, &search, terminal);
  
  GhosttyString needle = { (const uint8_t *)"error", 5 };
  ghostty_search_set(search, GHOSTTY_SEARCH_OPT_NEEDLE, &needle);
  ghostty_search_run(search);
  
  // Find bar chrome: "k of n"
  size_t total, idx;
  ghostty_search_get(search, GHOSTTY_SEARCH_DATA_TOTAL_MATCHES, &total);
  
  // Enter: select the next match (wraps, scrolls the viewport if needed)
  ghostty_search_set(search, GHOSTTY_SEARCH_OPT_SELECT_NEXT, NULL);
  ghostty_search_get(search, GHOSTTY_SEARCH_DATA_SELECTED_INDEX, &idx);
  
  ghostty_search_free(search);
  ```
  ````
- [`8168115`](https://github.com/ghostty-org/ghostty/commit/81681158b1f04b9900c3e58ba6db790384f5b6f5) Add Serbian translation ([#13842](https://github.com/ghostty-org/ghostty/issues/13842)) ([@00-kat](https://github.com/00-kat))
  ```text
  ## Summary
  - Adds Serbian translations for both Cyrillic (`sr`) and Latin
  (`sr@latin`) scripts, registered in `src/os/i18n_locales.zig` and
  `CODEOWNERS`.
  - `po/sr@latin.po` is generated from `po/sr.po` with `msgfilter
  recode-sr-latin` and should not be translated by hand.
  - Replaces the closed #13030; strings are rebased onto current `main`.
  
  Cc @slowdub for a review.
  
  EDIT: AI disclosure: I used Cursor (Grok 4.6) for mechanical repo work
  only, not for writing the Serbian translations. The agent fetched
  ghostty-org/ghostty, branched from current main, ran msgmerge on
  po/sr.po against the template, generated po/sr@latin.po with msgfilter
  recode-sr-latin, registered sr / sr@latin in src/os/i18n_locales.zig and
  CODEOWNERS, rebased my three commits onto later main, pushed the branch,
  and opened this PR (I had intended to open the PR myself, s***** thing
  ignored my instructions). I translated and reviewed sr.po and the Latin
  file is a recode of that catalog, not a separate translation since
  Serbian Cyrillic can be perfectly transcoded to the Latin script via
  [recode-sr-latin](https://linux.die.net/man/1/recode-sr-latin).
  ```
- [`38c984e`](https://github.com/ghostty-org/ghostty/commit/38c984e6760f59a634b6538f5e8669ec829019f1) build(deps): bump softprops/action-gh-release from 3.0.2 to 3.0.3 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [softprops/action-gh-release](https://github.com/softprops/action-gh-release) from 3.0.2 to 3.0.3.
  - [Release notes](https://github.com/softprops/action-gh-release/releases)
  - [Changelog](https://github.com/softprops/action-gh-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/softprops/action-gh-release/compare/3d0d9888cb7fd7b750713d6e236d1fcb99157228...efb35369e0ad2afab669f228072c1b0d510eae64)
  
  ---
  updated-dependencies:
  - dependency-name: softprops/action-gh-release
    dependency-version: 3.0.3
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`20abdb5`](https://github.com/ghostty-org/ghostty/commit/20abdb50a6216c450d6d4d010c41c7edf5ab15b2) Update VOUCHED list ([#14101](https://github.com/ghostty-org/ghostty/issues/14101)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14100#discussioncomment-18229353)
  from @jcollie.
  
  Vouch: @jzillmann
  ```
- [`d4a5ff5`](https://github.com/ghostty-org/ghostty/commit/d4a5ff58b6bc4a1fcc79a69f5cff94a678d97f42) macOS: fix window cascading ([@bo2themax](https://github.com/bo2themax))
- [`d2e2488`](https://github.com/ghostty-org/ghostty/commit/d2e2488ef7539124122d346399a5e5cca152f259) build(deps): bump softprops/action-gh-release from 3.0.2 to 3.0.3 ([#14098](https://github.com/ghostty-org/ghostty/issues/14098)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [softprops/action-gh-release](https://github.com/softprops/action-gh-release)
  from 3.0.2 to 3.0.3.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/softprops/action-gh-release/releases">softprops/action-gh-release's
  releases</a>.</em></p>
  <blockquote>
  <h2>v3.0.3</h2>
  <p><code>3.0.3</code> is a maintenance release with updated
  dependencies. It also safely
  classifies malformed GitHub API errors to avoid secondary failures (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/822">#822</a>).</p>
  <h2>What's Changed</h2>
  <h3>Bug fixes 🐛</h3>
  <ul>
  <li>fix: safely classify GitHub API errors by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/822">softprops/action-gh-release#822</a></li>
  </ul>
  <h3>Other Changes 🔄</h3>
  <ul>
  <li>dependency updates</li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/softprops/action-gh-release/blob/master/CHANGELOG.md">softprops/action-gh-release's
  changelog</a>.</em></p>
  <blockquote>
  <h2>3.0.3</h2>
  <p><code>3.0.3</code> is a maintenance release with updated
  dependencies. It also safely
  classifies malformed GitHub API errors to avoid secondary failures (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/822">#822</a>).</p>
  <h2>What's Changed</h2>
  <h3>Bug fixes 🐛</h3>
  <ul>
  <li>fix: safely classify GitHub API errors by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/822">softprops/action-gh-release#822</a></li>
  </ul>
  <h3>Other Changes 🔄</h3>
  <ul>
  <li>dependency updates</li>
  </ul>
  <h2>3.0.2</h2>
  <p><code>3.0.2</code> is a patch release focused on release reliability
  and compatibility. It
  reuses existing draft releases when publishing prereleases, supports
  replacing
  release assets on Gitea, hardens streamed asset uploads, and provides
  clearer
  release-creation diagnostics. It also includes TypeScript, coverage, and
  tooling
  maintenance merged since <code>3.0.1</code>.</p>
  <p>This release fixes <a
  href="https://redirect.github.com/softprops/action-gh-release/issues/795">#795</a>,
  <a
  href="https://redirect.github.com/softprops/action-gh-release/issues/438">#438</a>,
  and <a
  href="https://redirect.github.com/softprops/action-gh-release/issues/803">#803</a>.
  The upload transport hardening covers the
  historical failure reported in <a
  href="https://redirect.github.com/softprops/action-gh-release/issues/790">#790</a>,
  although current hosted Node 24 runners did
  not reproduce it naturally. The diagnostics work is related to <a
  href="https://redirect.github.com/softprops/action-gh-release/issues/786">#786</a>
  and does not
  claim a reproducible release-creation fix.</p>
  <h2>What's Changed</h2>
  <h3>Exciting New Features 🎉</h3>
  <ul>
  <li>feat: improve release error reporting and test coverage by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/813">softprops/action-gh-release#813</a></li>
  </ul>
  <h3>Bug fixes 🐛</h3>
  <ul>
  <li>fix: publish existing draft releases as prereleases by <a
  href="https://github.com/godfengliang"><code>@​godfengliang</code></a>
  in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/801">softprops/action-gh-release#801</a></li>
  <li>fix: upload small checksum assets reliably by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/815">softprops/action-gh-release#815</a></li>
  <li>fix: replace existing release assets on Gitea by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/816">softprops/action-gh-release#816</a></li>
  <li>fix: clarify release creation 404 errors by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/817">softprops/action-gh-release#817</a></li>
  </ul>
  <h3>Other Changes 🔄</h3>
  <ul>
  <li>chore(deps): upgrade TypeScript to 7 by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/812">softprops/action-gh-release#812</a></li>
  <li>chore(deps): remove unused TypeScript tooling by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/814">softprops/action-gh-release#814</a></li>
  <li>dependency, Node 24 pin, and CI maintenance merged since
  <code>3.0.1</code></li>
  </ul>
  <h2>3.0.1</h2>
  <ul>
  <li>maintenance release with updated dependencies</li>
  </ul>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/efb35369e0ad2afab669f228072c1b0d510eae64"><code>efb3536</code></a>
  release 3.0.3 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/840">#840</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/6441963a7597ab67f36fea0287a7ae58a9bfd8fe"><code>6441963</code></a>
  chore(deps): bump the npm group with 2 updates (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/839">#839</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/e5ee6bc58a36b838b92fc1217f2e4b414b5abcc8"><code>e5ee6bc</code></a>
  chore(deps): bump esbuild from 0.28.1 to 0.28.2 in the npm group (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/837">#837</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/d1e66170d32c9ec7bbcb7fae044d3d686ce304d3"><code>d1e6617</code></a>
  chore(deps): bump undici from 6.27.0 to 6.28.0 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/831">#831</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/64037519ba20f54c01bc1dc90342c929aac5a2fa"><code>6403751</code></a>
  chore(deps): bump the npm group with 2 updates (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/835">#835</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/7c7184b6876126a5df15adc5b679dc450a393725"><code>7c7184b</code></a>
  chore(deps): bump postcss from 8.5.19 to 8.5.25 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/833">#833</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/0f3f0d2943676d58f9698b3ab590c2056023d77d"><code>0f3f0d2</code></a>
  chore(deps): bump brace-expansion from 5.0.8 to 5.0.9 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/832">#832</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/77fb938f2f95e717ce6705d2909af527263360a0"><code>77fb938</code></a>
  chore(deps): bump prettier from 3.9.5 to 3.9.6 in the npm group (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/830">#830</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/5a6f51711ce2ba103b78f5e9550f810679f11e0e"><code>5a6f517</code></a>
  chore(deps): bump brace-expansion from 5.0.7 to 5.0.8 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/828">#828</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/a3c91c98f80000f5b06c7fc0327c54f51c6ab7d8"><code>a3c91c9</code></a>
  chore(deps): bump the github-actions group with 2 updates (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/825">#825</a>)</li>
  <li>Additional commits viewable in <a
  href="https://github.com/softprops/action-gh-release/compare/3d0d9888cb7fd7b750713d6e236d1fcb99157228...efb35369e0ad2afab669f228072c1b0d510eae64">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=softprops/action-gh-release&package-manager=github_actions&previous-version=3.0.2&new-version=3.0.3)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`b7a680b`](https://github.com/ghostty-org/ghostty/commit/b7a680bc40b76cf7ed6b21044ac3f291ea0056be) macOS: fix window cascading ([#14106](https://github.com/ghostty-org/ghostty/issues/14106)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Regression from https://github.com/ghostty-org/ghostty/pull/13722
  ```
- [`451e224`](https://github.com/ghostty-org/ghostty/commit/451e224c64ddd0a9d9e9df045cdfb27c38fa8ff2) macOS: clean up for [#14106](https://github.com/ghostty-org/ghostty/issues/14106) ([@bo2themax](https://github.com/bo2themax))
- [`3c1ef5b`](https://github.com/ghostty-org/ghostty/commit/3c1ef5b32fc5ea6b93d28493fabf193f595139cf) macOS: clean up for [#14106](https://github.com/ghostty-org/ghostty/issues/14106) ([#14111](https://github.com/ghostty-org/ghostty/issues/14111)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  I don't know what happened to me, but I didn't notice that I should
  delete this🫪
  ```
- [`2ba7576`](https://github.com/ghostty-org/ghostty/commit/2ba75764f6002baab9cb439dfff7ec37ac7704e8) build(deps): bump flatpak/flatpak-github-actions/flatpak-builder ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [flatpak/flatpak-github-actions/flatpak-builder](https://github.com/flatpak/flatpak-github-actions) from 6.7 to 6.8.
  - [Release notes](https://github.com/flatpak/flatpak-github-actions/releases)
  - [Commits](https://github.com/flatpak/flatpak-github-actions/compare/401fe28a8384095fc1531b9d320b292f0ee45adb...79327416609af08178ad73b352877e51450790b3)
  
  ---
  updated-dependencies:
  - dependency-name: flatpak/flatpak-github-actions/flatpak-builder
    dependency-version: '6.8'
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`7358067`](https://github.com/ghostty-org/ghostty/commit/7358067d1a014e0dc36545046f2df41255f2ea26) build(deps): bump cachix/cachix-action ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [cachix/cachix-action](https://github.com/cachix/cachix-action) from 5f2d7c5294214f71b873db4b969586b980625e71 to 38b082610b782e7e93e209c35fd730d399dee866.
  - [Release notes](https://github.com/cachix/cachix-action/releases)
  - [Changelog](https://github.com/cachix/cachix-action/blob/master/RELEASE.md)
  - [Commits](https://github.com/cachix/cachix-action/compare/5f2d7c5294214f71b873db4b969586b980625e71...38b082610b782e7e93e209c35fd730d399dee866)
  
  ---
  updated-dependencies:
  - dependency-name: cachix/cachix-action
    dependency-version: 38b082610b782e7e93e209c35fd730d399dee866
    dependency-type: direct:production
  ...
  ```
- [`310797d`](https://github.com/ghostty-org/ghostty/commit/310797df1d912bccd63ef624395a2458e99f6cf7) macOS: fix cascading without affecting other new-window behaviours ([@bo2themax](https://github.com/bo2themax))
- [`a8b0855`](https://github.com/ghostty-org/ghostty/commit/a8b0855b630022db2933f402d9c964a111c8751c) macOS: fix cascading for HiddenTitlebarTerminalWindow ([@bo2themax](https://github.com/bo2themax))
- [`58aa59d`](https://github.com/ghostty-org/ghostty/commit/58aa59d0e176b57d27e685dee86d3e9b7e165ef9) Update po/eu.po ([@erral](https://github.com/erral))
- [`6a51526`](https://github.com/ghostty-org/ghostty/commit/6a5152651c8744bf5058d49ee45fdb6aee63d570) Update po/eu.po ([@erral](https://github.com/erral))
- [`4c731b5`](https://github.com/ghostty-org/ghostty/commit/4c731b5d89708ae742d4809ef1ce6a81c5c551da) Update po/eu.po ([@erral](https://github.com/erral))
- [`4ffec4b`](https://github.com/ghostty-org/ghostty/commit/4ffec4bda7ed603be297564a7b23c1d21707106e) Update po/eu.po ([@erral](https://github.com/erral))
- [`f407316`](https://github.com/ghostty-org/ghostty/commit/f407316c84a313a7f9694a2d6f3e1acabc19a416) Update po/eu.po ([@erral](https://github.com/erral))
  ```text
  applying but both eskuma and eskuina are OK.
  ```
- [`63039a6`](https://github.com/ghostty-org/ghostty/commit/63039a688e765c448ca7cc80b77d83d2177e6f51) update ([@erral](https://github.com/erral))
- [`f184d3c`](https://github.com/ghostty-org/ghostty/commit/f184d3ceb5eaee08f92f6302ac2a499bcd7dc015) update ([@erral](https://github.com/erral))
- [`4da902b`](https://github.com/ghostty-org/ghostty/commit/4da902b3c9929333f7cf78147ec714f34d5619c0) update ([@erral](https://github.com/erral))
- [`9801423`](https://github.com/ghostty-org/ghostty/commit/9801423d01e0e883c32f95a210afd98919520562) update ([@erral](https://github.com/erral))
- [`5d6615f`](https://github.com/ghostty-org/ghostty/commit/5d6615fc43ce5bc7ba9981e0c925d4e3d9dfb0d7) bash: upgrade to bash-preexec 0.7.0 ([@jparise](https://github.com/jparise))
  ```text
  https://github.com/rcaloras/bash-preexec/releases/tag/0.7.0
  
  We only source bash-preexec for bash < 4.4, so most of this release is
  inert for us: the PS0 function-substitution hook (bash >= 5.3) and the
  array PROMPT_COMMAND handling (bash >= 5.1) are never reached. What we
  do pick up is the simpler install string, per-prompt re-adjustment of
  PROMPT_COMMAND when something else modifies it, preservation of $? and
  $_ on early returns, and the first-command preexec fix.
  
  We continue to carry one local modification: __bp_adjust_histcontrol
  stays disabled in the DEBUG trap hook so the user's HISTCONTROL is
  respected (#2269). The original justification was that we didn't use
  the preexec command argument, which is no longer true because we use it
  for the window title. The comment now explains the current reasoning:
  our bash >= 4.4 integration also uses `history 1` without adjusting
  HISTCONTROL and accepts the same inaccuracy for space-prefixed commands,
  so the legacy path is kept consistent with it.
  ```
- [`7520175`](https://github.com/ghostty-org/ghostty/commit/75201750213200fba1537cf724fac5ba3dec4318) more fixes ([@erral](https://github.com/erral))
- [`aafacb1`](https://github.com/ghostty-org/ghostty/commit/aafacb1cb940e3599cb4ec2c4f9cb975532a12a4) macOS: fix flickering when creating new tab with glass style ([@bo2themax](https://github.com/bo2themax))
- [`fec89f2`](https://github.com/ghostty-org/ghostty/commit/fec89f2541e412b1a2556e56742c7612118f1b72) macOS: fix flickering when creating new tab with glass style ([#14121](https://github.com/ghostty-org/ghostty/issues/14121)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A regression from #13985.
  
  
  https://github.com/user-attachments/assets/cc7d76d7-7d86-4566-921c-a6531ce4087d
  
  
  
  
  ### AI Disclosure
  
  Used Claude to investigate, I reviewed and tested.
  ```
- [`0c1909d`](https://github.com/ghostty-org/ghostty/commit/0c1909d09a0db148913b79c684db1cef58e214ee) bash: upgrade to bash-preexec 0.7.0 ([#14120](https://github.com/ghostty-org/ghostty/issues/14120)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  https://github.com/rcaloras/bash-preexec/releases/tag/0.7.0
  
  We only source bash-preexec for bash < 4.4, so most of this release is
  inert for us: the PS0 function-substitution hook (bash >= 5.3) and the
  array PROMPT_COMMAND handling (bash >= 5.1) are never reached. What we
  do pick up is the simpler install string, per-prompt re-adjustment of
  PROMPT_COMMAND when something else modifies it, preservation of $? and
  $_ on early returns, and the first-command preexec fix.
  
  We continue to carry one local modification: __bp_adjust_histcontrol
  stays disabled in the DEBUG trap hook so the user's HISTCONTROL is
  respected (#2269). The original justification was that we didn't use the
  preexec command argument, which is no longer true because we use it for
  the window title. The comment now explains the current reasoning: our
  bash >= 4.4 integration also uses `history 1` without adjusting
  HISTCONTROL and accepts the same inaccuracy for space-prefixed commands,
  so the legacy path is kept consistent with it.
  
  *AI Usage:* I asked Fable 5.1 to run a verification pass after my manual
  upgrade, and it confirmed the expected behavior.
  ```
- [`084316a`](https://github.com/ghostty-org/ghostty/commit/084316aa825a210dedc9c2fce07772cf36ade3cb) macOS: fix cascading without affecting other new-window behaviours ([#14118](https://github.com/ghostty-org/ghostty/issues/14118)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Found another regression when investigating #14107 after the last fix.
  This regression appears on macOS 15 and 26 as well: **New window by
  Shortcuts.app or service menu while a window is visible would create a
  tab**.
  
  It appears that for `new-window` triggered by Shortcuts/Service, a small
  delay is needed to avoid automatic tabbing. It's either removing
  `NSWindow.userTabbingPreference == .always` completely or adding another
  "delay" for cascading. The latter should be better.
  
  Also fixes another cascading for `macos-titlebar-style = hidden`
  previously missed.
  ```
- [`41004c6`](https://github.com/ghostty-org/ghostty/commit/41004c6e2204494a2cbc0b4b78dd3b9c671d7488) build(deps): bump cachix/cachix-action from 5f2d7c5294214f71b873db4b969586b980625e71 to 38b082610b782e7e93e209c35fd730d399dee866 ([#14116](https://github.com/ghostty-org/ghostty/issues/14116)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps [cachix/cachix-action](https://github.com/cachix/cachix-action)
  from 5f2d7c5294214f71b873db4b969586b980625e71 to
  38b082610b782e7e93e209c35fd730d399dee866.
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/cachix/cachix-action/blob/master/RELEASE.md">cachix/cachix-action's
  changelog</a>.</em></p>
  <blockquote>
  <h1>Release</h1>
  <ol>
  <li>
  <p>Create and push a new tag:</p>
  <pre lang="console"><code>git tag v17
  git push origin v17
  </code></pre>
  </li>
  <li>
  <p>Wait for CI to pass.</p>
  </li>
  <li>
  <p><a href="https://github.com/cachix/cachix-action/releases/new">Create
  a release</a> for the new tag.</p>
  </li>
  <li>
  <p>Move the major version tag to the latest release:</p>
  <pre lang="console"><code>git tag -fa v17
  git push origin v17 --force
  </code></pre>
  </li>
  </ol>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/38b082610b782e7e93e209c35fd730d399dee866"><code>38b0826</code></a>
  dev: cleanup tests and dev files</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/0fe030c2864be690428363af3bc7016b7b1925d8"><code>0fe030c</code></a>
  dist</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/792dafcfd01b48d3df8424b641db396602252fc3"><code>792dafc</code></a>
  deps: bump dependencies</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/b690244fb5c76a5486c33b0fbbc6fd55c857d1fe"><code>b690244</code></a>
  ci: improve Nix compatibility test coverage</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/f495f3ffa2f3810a92e5cc0abc2c5d6a2a07ec82"><code>f495f3f</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/cachix-action/issues/217">#217</a>
  from cachix/dependabot/github_actions/actions/checkout-7</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/9ee3c77d45d24a8b7557d22cbba3454f2a4f8a7b"><code>9ee3c77</code></a>
  chore(deps): bump actions/checkout from 6 to 7</li>
  <li>See full diff in <a
  href="https://github.com/cachix/cachix-action/compare/5f2d7c5294214f71b873db4b969586b980625e71...38b082610b782e7e93e209c35fd730d399dee866">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
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
- [`dd167cc`](https://github.com/ghostty-org/ghostty/commit/dd167cc464f8f8b30cc561fb07e09e9fb2986c14) build(deps): bump flatpak/flatpak-github-actions/flatpak-builder from 6.7 to 6.8 ([#14115](https://github.com/ghostty-org/ghostty/issues/14115)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [flatpak/flatpak-github-actions/flatpak-builder](https://github.com/flatpak/flatpak-github-actions)
  from 6.7 to 6.8.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/flatpak/flatpak-github-actions/releases">flatpak/flatpak-github-actions/flatpak-builder's
  releases</a>.</em></p>
  <blockquote>
  <h2>v6.8</h2>
  <ul>
  <li>Add saveCache flag</li>
  <li>Add ability to override artifact name</li>
  <li>Add buildDebugBundle flag</li>
  <li>Update tests, documentation and dependencies</li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/79327416609af08178ad73b352877e51450790b3"><code>7932741</code></a>
  Update all dependencies and regenerate dist</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/09e3d61868ecd92a1c5b298a31bcc4bae17ae217"><code>09e3d61</code></a>
  readme: Don't specify setting cache key to github.sha (<a
  href="https://redirect.github.com/flatpak/flatpak-github-actions/issues/261">#261</a>)</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/23e622281a14ba5350ce2ab1ae700ac7d08cc841"><code>23e6222</code></a>
  Update runtime versions and docker images to latest</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/a3ab43f58191aa8dc105e572c0a62eaac0a7555a"><code>a3ab43f</code></a>
  flatpak-builder: Add saveCache flag</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/8e357b1556f526e3642244bdf1a6d585be36de54"><code>8e357b1</code></a>
  ci: Remove unnecessary 'needs' from debug bundle job</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/26e19caa3a954b1d36898a0e239a67d8e856f99c"><code>26e19ca</code></a>
  ci: Add test for artifact-name</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/06d246b4d5459d93c166243236f8a086d5578746"><code>06d246b</code></a>
  flatpak-builder: Add ability to override artifact name</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/a2622647717d8185d0f8cf01bb1ea2341e357ae0"><code>a262264</code></a>
  ci: Add job that uses build-debug-bundle</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/f7362292df659c06960a8c0dc309ab5990454a29"><code>f736229</code></a>
  flatpak-builder: Add buildDebugBundle flag</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/3b10954431df173eb3b564bb9adfddf3842ff91c"><code>3b10954</code></a>
  ci: Update actions to versions using Node 24</li>
  <li>See full diff in <a
  href="https://github.com/flatpak/flatpak-github-actions/compare/401fe28a8384095fc1531b9d320b292f0ee45adb...79327416609af08178ad73b352877e51450790b3">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=flatpak/flatpak-github-actions/flatpak-builder&package-manager=github_actions&previous-version=6.7&new-version=6.8)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`06178ee`](https://github.com/ghostty-org/ghostty/commit/06178eeaad7648216a0da5eb73537e9dba2266cb) terminal/search: resume a complete search when history is prepended ([@mitchellh](https://github.com/mitchellh))
  ```text
  A search that had already exhausted a screen's PageList never picked up
  history pages prepended afterwards by incremental snapshot restore.
  
  The lower level PageListSearch and so on could already handle this, we
  just needed to let it know that more history existed to search. This
  fixes that.
  ```
- [`b0481f5`](https://github.com/ghostty-org/ghostty/commit/b0481f5aa76a97e652bb842937ae4fa0eda68f3c) terminal/search: resume a complete search when history is prepended ([#14123](https://github.com/ghostty-org/ghostty/issues/14123)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A search that had already exhausted a screen's PageList never picked up
  history pages prepended afterwards by incremental snapshot restore.
  
  The lower level PageListSearch and so on could already handle this, we
  just needed to let it know that more history existed to search. This
  fixes that.
  ```
- [`3b8141f`](https://github.com/ghostty-org/ghostty/commit/3b8141fbd8e2f5770809d3df2fe0077849866dde) os/open: consume the newline when draining opener stderr ([@jzillmann](https://github.com/jzillmann))
  ```text
  takeDelimiterExclusive never consumes the delimiter: it tosses only the
  exclusive length, so the '\n' stays buffered. Once the spawned opener
  writes a single line to stderr, every subsequent call returns an empty
  slice without advancing the stream, and openThread's loop spins forever
  - one pinned core per affected open(), logging empty
  "open stderr=" warnings at tens of thousands of messages per second for
  the lifetime of the process. The thread also never reaches exe.wait(),
  so the child is never reaped.
  
  Read inclusively instead (which does consume the delimiter) and trim
  the '\n' for logging.
  
  Repro: open a link whose handler writes to stderr, e.g. an OSC 8 link
  with an unknown scheme; watch a core disappear and the unified log
  flood with "os-open: open stderr=".
  
  See discussion #14100.
  ```
- [`372d691`](https://github.com/ghostty-org/ghostty/commit/372d6914b8615610e290f8e8446d75cf4b53efeb) i18n: complete eu translation ([#14095](https://github.com/ghostty-org/ghostty/issues/14095)) ([@trag1c](https://github.com/trag1c))
- [`e212b73`](https://github.com/ghostty-org/ghostty/commit/e212b73cdaf381f2d57edc11307b06c1f520df4b) Update mk localization for v1.4 ([#14088](https://github.com/ghostty-org/ghostty/issues/14088)) ([@trag1c](https://github.com/trag1c))
  ```text
  Addressing #13766 for mk.
  ```
- [`349f026`](https://github.com/ghostty-org/ghostty/commit/349f026087d948f8f898dca3231ff91438f83ab8) os/open: consume the newline when draining opener stderr ([#14125](https://github.com/ghostty-org/ghostty/issues/14125)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes the runaway-thread bug reported in #14100 (vouched there).
  
  `openThread` drains the spawned opener's stderr with
  `takeDelimiterExclusive('\n')`. That function tosses only the exclusive
  length, so the `'\n'` is never consumed. Once the child writes one line
  to stderr, every subsequent call returns an empty slice without
  advancing the stream: the `while (true)` loop spins forever — one pinned
  core per affected `open()`, logging empty `os-open: open stderr=`
  warnings at tens of thousands of messages per second for the lifetime of
  the process — and `exe.wait()` is never reached, so the child is never
  reaped.
  
  This change reads inclusively (`takeDelimiterInclusive`, which does
  consume the delimiter) and trims the `'\n'` for logging.
  
  Observed in the wild embedding libghostty on macOS: several days of
  uptime accumulated six leaked opener threads at ~70% of a core each
  (~4.4 cores), from six link clicks whose `/usr/bin/open` wrote to
  stderr. After the fix, the same workload shows zero `os-open` log
  traffic and no leaked threads.
  
  Repro without the fix: open a link whose handler writes to stderr (e.g.
  an OSC 8 link with an unknown scheme), then watch a core pin and `log
  stream --predicate 'subsystem == "com.mitchellh.ghostty"'` flood.
  
  **AI disclosure** (per `AI_POLICY.md`): the bug was diagnosed and this
  patch drafted with Claude Code (thread sampling, log analysis, and
  reading the Zig 0.16 `std.Io.Reader` source to confirm
  `takeDelimiterExclusive`/`takeDelimiterInclusive` toss semantics). I
  reviewed the analysis and the change, understand both, and verified the
  fix in a production build of the embedding app.
  ```
- [`5dfb672`](https://github.com/ghostty-org/ghostty/commit/5dfb672986b57b6246d0c5d2c3c9a8fd3d138543) surface: restore mouse_shape when modifier overrides end ([@j-c-m](https://github.com/j-c-m))
  ```text
  hard-coded .default & .text overrode a previously set OSC22 pointer
  shape, this was a regression introduced in 6e8ed4e8b.
  ```
- [`6674aa3`](https://github.com/ghostty-org/ghostty/commit/6674aa3ba88e4e316af4106746e4b2091868df79) surface: update keyToMouseShape tests to expect mouse_shape ([@j-c-m](https://github.com/j-c-m))
  ```text
  Update the tests to expect the mouse_shape back, not the hardcoded
  .default or .text
  ```
- [`3a766cc`](https://github.com/ghostty-org/ghostty/commit/3a766ccf501c669298e5b648a47d217e99bff618) surface: show .text (i-beam) while shift is held without mouse tracking ([@j-c-m](https://github.com/j-c-m))
  ```text
  I think this is the expected behavoir when a custom OSC22 pointer is set. Once
  shift is released it will return to mouse_shape (whatever the pointer
  was before shit held).
  ```
- [`0fb6d29`](https://github.com/ghostty-org/ghostty/commit/0fb6d29404aab9c54c6fbce3cebd630960938117) SurfaceMouse: simplify keyToMouseShape ([@vancluever](https://github.com/vancluever))
  ```text
  keyToMouseShape was initially designed with more of a transition table
  model in mind to handle key presses/overrides based on very specific
  cursor states. This never materialized, so I think it's safe to just
  simply the process of handling overrides and/or passing along the
  current cursor state from the terminal in the event of key presses.
  
  Also removed a test that is essentially a duplicate of one before it now
  (returning current surface shape in the event of no overrides).
  ```
- [`6000034`](https://github.com/ghostty-org/ghostty/commit/600003455a9b6e7cf06b3127a490d6ab3c1b05df) surface: restore application mouse shape after modifier overrides ([#14128](https://github.com/ghostty-org/ghostty/issues/14128)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This fixes a regression of 9a6469743 introduced in 6e8ed4e8b.
  
  With this fix the mouse pointer will be restored to the previous (which
  could have be set to something else via OSC22), not a hardcoded .text or
  .default.
  
  It also will change the cursor to a text selection if shift is held even
  without mouse tracking, I think this is the expected behavior when a
  cursor is set via OSC22. (Kitty additionaly, once you start selecting
  changes to text (I-beam), this would be a follow-up if we desire to
  behave like kitty with OSC22 pointers).
  ```
- [`e01e75b`](https://github.com/ghostty-org/ghostty/commit/e01e75bbb228cfbb5fc08cdd53316928761c020b) terminal: don't touch me! keep the page pool free list unobtrusive ([@mitchellh](https://github.com/mitchellh))
  ```text
  This replaces the `std.heap.MemoryPool` used for page buffers with
  a custom pool called `UntouchedPool`. This keeps its free list in a side
  array and never reads/writes items until `create()`. This means that
  demand-driven allocations (like mmaped pages) don't incur physical costs
  until they're actually used.
  
  The standard `std.heap.MemoryPool` uses an intrusive linked list for
  its items which causes every item to be touched, which forces a full
  page-in of memory.
  
  It turns out we also had a lot of assertions and logic to work around
  this in various ways (size of rows, asserting we overwrite the free
  list entry, etc.) that we can now remove because of this.
  
  For an 80x24 terminal on macOS (16 KB pages):
  
  | Per terminal                 | Before   | After    |
  |------------------------------|----------|----------|
  | Page-list memory dirty       | 128 KiB  | 48 KiB   |
  | Process phys_footprint delta | 143 KiB  | 62 KiB   |
  | Page-list virtual size       | 2208 KiB | 1600 KiB |
  
  The remaining 48 KB is the active page, because we sprinkle metadata
  around the page which forces every page to be paged in. I'm going to
  follow this up with some work trying to move all our metadata to the
  front of the page so we only page one in until the rest is needed,
  but not sure if its achievable.
  
  Micro-benchmarks on the pool show that its twice the speed (slower) to
  create/free due to the side list, but in an actual `+terminal-stream`
  benchmark churning through pages, there is no measurable difference. I
  think its a good trade.
  ```
- [`31bdcd5`](https://github.com/ghostty-org/ghostty/commit/31bdcd5a79639bbac97c1a94e0f41d0f5ff84ca2) terminal: don't touch me! keep the page pool free list unobtrusive ([#14130](https://github.com/ghostty-org/ghostty/issues/14130)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This replaces the `std.heap.MemoryPool` used for page buffers with a
  custom pool called `UntouchedPool`. This keeps its free list in a side
  array and never reads/writes items until `create()`. This means that
  demand-driven allocations (like mmaped pages) don't incur physical costs
  until they're actually used.
  
  The standard `std.heap.MemoryPool` uses an intrusive linked list for its
  items which causes every item to be touched, which forces a full page-in
  of memory.
  
  It turns out we also had a lot of assertions and logic to work around
  this in various ways (size of rows, asserting we overwrite the free list
  entry, etc.) that we can now remove because of this.
  
  For an 80x24 terminal on macOS (16 KB pages):
  
  | Per terminal                 | Before   | After    |
  |------------------------------|----------|----------|
  | Page-list memory dirty       | 128 KiB  | 48 KiB   |
  | Process phys_footprint delta | 143 KiB  | 62 KiB   |
  | Page-list virtual size       | 2208 KiB | 1600 KiB |
  
  The remaining 48 KB is the active page, because we sprinkle metadata
  around the page which forces every page to be paged in. I'm going to
  follow this up with some work trying to move all our metadata to the
  front of the page so we only page one in until the rest is needed, but
  not sure if its achievable.
  
  Micro-benchmarks on the pool show that its twice the speed (slower) to
  create/free due to the side list, but in an actual `+terminal-stream`
  benchmark churning through pages, there is no measurable difference. I
  think its a good trade.
  ```
- [`e347482`](https://github.com/ghostty-org/ghostty/commit/e347482fba62fd905fab2d4c8ec6a8c6f3664385) macOS: fix find previous action when search is focused ([@bo2themax](https://github.com/bo2themax))
- [`e8936b8`](https://github.com/ghostty-org/ghostty/commit/e8936b8969e78e07d9a8bf2b6a22ce59a38f5dfb) macOS: follow up cascading fix for [#14118](https://github.com/ghostty-org/ghostty/issues/14118) ([@bo2themax](https://github.com/bo2themax))
  ```text
  Didn't respect the comment above before when reverting and testing hidden title 🫪
  ```
- [`3cca3e0`](https://github.com/ghostty-org/ghostty/commit/3cca3e0b956f07e008a4c66bb5f1a8ce266259a3) macOS: follow up cascading fix for [#14118](https://github.com/ghostty-org/ghostty/issues/14118) ([#14132](https://github.com/ghostty-org/ghostty/issues/14132)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Didn't respect the comment above. Sorry for the back&forth changes 🫪
  ```
- [`09ff85b`](https://github.com/ghostty-org/ghostty/commit/09ff85b2ac7b4204bbc48b5c7010adf0bdfb36d8) macOS: fix find previous action when search is focused ([#14131](https://github.com/ghostty-org/ghostty/issues/14131)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Typo found by @lrytz.
  ```
- [`ffe015e`](https://github.com/ghostty-org/ghostty/commit/ffe015ee55d1ab39cbf1525823ff18092433eab9) terminal: bitmap allocator marks free chunks with zero bits ([@mitchellh](https://github.com/mitchellh))
- [`c0a4f80`](https://github.com/ghostty-org/ghostty/commit/c0a4f80d80d75f7d3250d12554501fd7197e9bb0) terminal: hash map and ref counted set can initialize from zeroed memory ([@mitchellh](https://github.com/mitchellh))
- [`6112935`](https://github.com/ghostty-org/ghostty/commit/6112935a2fe9b7f5fd6c7595225c53406bee3bb1) terminal: hash map keeps its capacity and entry pointers in the struct ([@mitchellh](https://github.com/mitchellh))
- [`d2ff6d7`](https://github.com/ghostty-org/ghostty/commit/d2ff6d77a05d9e9b247684fad6bcb7979d0b2aca) terminal: pages initialize from zeroed memory and cache-line align their cells ([@mitchellh](https://github.com/mitchellh))
- [`07bccf7`](https://github.com/ghostty-org/ghostty/commit/07bccf7a311acdfa6afc77f2016160d49b1f1982) terminal: make all page data structures treat zero as empty to avoid eagerly paging in mmap pages ([#14137](https://github.com/ghostty-org/ghostty/issues/14137)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This updates all our page data structures so that the `0` value
  (literally `@memset(0)`) means empty. This way, when we initialize a new
  page via mmap (OS-guaranteed zeroed), we don't need to write to it, and
  don't trigger the kernel to physically map the memory.
  
  From Ghostty 1.3.1, our empty terminal physical memory usage goes from
  128 KB to 48 KB (#14130) to 16 KB (this PR). And even with an empty
  prompt written on my machine, it holds at 16KB, only increasing to two
  pages (32 KB) with 24 rows written.
  
  Here are some measurements.
  
  | Per terminal | Before (macOS) | After (macOS) | Before (Linux) | After
  (Linux) |
  
  |-------------------------------------------------------|----------------|---------------|----------------|---------------|
  | Page-list memory dirty, fresh | 48 KiB | 16 KiB | 24 KiB | 8 KiB |
  | Page-list memory dirty, 24 visible rows written | 64 KiB | 32 KiB | 36
  KiB | 20 KiB |
  
  Note macOS uses 16KB pages and Linux generally uses 4 KB pages.
  
  I ran `ghostty-bench +terminal-stream` main vs this branch and with
  every normal workload the results are within noise (sometimes faster
  sometimes slower).
  
  **AI usage:** It was used as a judge/validator. The actual changes were
  me, commit messages and PR messages all me.
  ```
- [`efa3c66`](https://github.com/ghostty-org/ghostty/commit/efa3c66ed16ea9251d5b2a74b606aabc248d2c00) terminal: PageList nodes are pooled individually from the gpa instead of an arena ([@mitchellh](https://github.com/mitchellh))
- [`35a6fb7`](https://github.com/ghostty-org/ghostty/commit/35a6fb747f5d60ee6d92a7f5667474914a47cf21) terminal: PageList preheats only the viewport and cursor pins ([@mitchellh](https://github.com/mitchellh))
- [`105d0a5`](https://github.com/ghostty-org/ghostty/commit/105d0a5453654f15cbe9e902df9e72ed62fa5474) terminal: C terminal wrapper allocates the kitty temp dir path only when it is set ([@mitchellh](https://github.com/mitchellh))
- [`d1cd56a`](https://github.com/ghostty-org/ghostty/commit/d1cd56a56c4244d9d9fadae028cbffc23a1d3d1a) terminal: dynamic palette shares the built-in default instead of copying it per terminal ([@mitchellh](https://github.com/mitchellh))
- [`c81f0b2`](https://github.com/ghostty-org/ghostty/commit/c81f0b26871c7fbbe2fc35549fdad1f64ed29094) terminal: cut the fixed heap cost of a new terminal nearly in half ([#14138](https://github.com/ghostty-org/ghostty/issues/14138)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This focuses explicitly on the non-mmap allocations for a
  `ghostty_terminal_new` result. The result is that we lower this portion
  of the memory by almost half. The total benefit is smaller since 70% of
  a terminal is mmap'd allocations, but this still yields an absolute ~5KB
  savings on macOS on every new terminal (not just empty, but also with a
  normal prompt and so on).
  
  Four changes to make it happy, broken down into individual commits.
  Nothing crazy:
  
  - **Page list nodes are pooled individually.** The node pool was a
  `std.heap.MemoryPool`, which sits on an arena that preheats and grows
  1.5x, so we paid for wasted space. Nodes now come from `UntouchedPool`
  (the same pool as page buffers) with a preheat of one, so the cost is
  exactlyone node (well, exactly one bucket element size in whatever
  allocator).
  - **Pin pool and tracked pin set are sized for two pins.** Every screen
  tracks exactly a viewport pin and a cursor pin at creation, but we
  preheated eight pins and let the tracked pin map grow to 17 slots on the
  first insert via doubling.
  - **The kitty temp dir path is allocated only when set.** The C wrapper
  embedded a 1 KiB `max_path_bytes` buffer that only embedders that set
  `kitty_image_medium_temp_file` ever wrote to.
  - **The default palette is shared instead of copied.** `DynamicPalette`
  carried two full 1 KiB palettes, `current` and `original`, and
  `original` was almost always the built-in default. It is now a pointer
  to the shared built-in default, or to an allocator-owned copy when a
  custom default is set. This introduces a new OOM path but we gracefully
  handle it by either ignoring or resetting.
  
  Memory measurements:
  
  | Per terminal                                | Before   | After    |
  |---------------------------------------------|----------|----------|
  | phys_footprint delta, fresh                 | 30,066 B | 25,069 B |
  | phys_footprint delta, styled prompt written | 47,023 B | 41,944 B |
  | malloc zone bytes dirtied, fresh            | 12,698 B | 7,782 B  |
  | malloc blocks live after `terminal_new`     | 11,904 B | 6,688 B  |
  | malloc blocks live after the prompt         | 12,320 B | 7,104 B  |
  
  I ran `ghostty-bench +terminal-stream` on a 500 MB ascii corpus, main vs
  this branch interleaved, and there is no noticeable change.
  
  **AI usage:** Fable did validation of the work, I did the
  implementations, commit messages, and PR notes.
  ```
- [`4406cea`](https://github.com/ghostty-org/ghostty/commit/4406cea3e9fde88876551cedfef10d3b245b75b6) input: encode ctrl keys with modifyOtherKeys 2 ([@mitchellh](https://github.com/mitchellh))
  ```text
  #7425
  
  Control-modified characters use xterm's MOK2 encoding.
  
  I incorrectly believed previously that MOK2 ctrl chars were still encoded
  as C0 bytes. This is wrong. I'm going to do a more in depth audit if
  possible with every possible key combination against xterm to see where
  we diverge but this fixes this for now without regressing any tests.
  
  Background: https://invisible-island.net/xterm/modified-keys.html
  ```
- [`1f5bb57`](https://github.com/ghostty-org/ghostty/commit/1f5bb5769fbb5e717546073d33d3985604a315b2) input: encode ctrl keys with modifyOtherKeys 2 ([#14144](https://github.com/ghostty-org/ghostty/issues/14144)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  #7425
  
  Control-modified characters use xterm's MOK2 encoding.
  
  I incorrectly believed previously that MOK2 ctrl chars were still
  encoded as C0 bytes. This is wrong. I'm going to do a more in depth
  audit if possible with every possible key combination against xterm to
  see where we diverge but this fixes this for now without regressing any
  tests.
  
  Background: https://invisible-island.net/xterm/modified-keys.html
  ```

