> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: September 12, 2026 at 12:34 UTC.

## September 12, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/34674371812)  
Summary: 1 runs • 2 commits • 2 authors

### Changes

- [`c0c5473`](https://github.com/ghostty-org/ghostty/commit/c0c5473daf5b0ebc78ce0c8d1854f6221574ab3c) build: refactoring our use of translate-c ([@vancluever](https://github.com/vancluever))
  ```text
  This commit refactors our use of translate-c, in preparation for larger
  removal of cImport and better co-ordination between building of C
  dependencies and translation of headers.
  
  The major update is the creation of an internal helper package that
  wraps our use of the external translate-c library. This allows us to not
  only have better shorthand and a data-driven, declarative approach to C
  translation (versus the otherwise more imperative approach), it also
  funnels the external dependency into a single package instead of
  spreading it out among what will be an increasingly larger amount of
  places as dependencies in "pkg/" get updated.
  
  It also includes some refactors, namely to the harfbuzz package, which
  has had its individual settings refactored into helpers to allow for the
  settings to be better shared between translation and the build of the
  c-based static library.
  
  Wuffs has also had a bit of a refactor too so that we don't generate a
  file with all of the macro defines in it - we just send these in as "-D"
  flags now.
  ```
- [`e2e53f8`](https://github.com/ghostty-org/ghostty/commit/e2e53f861482e080bf45054ba49ef471f9849937) build: refactoring our use of translate-c ([#14203](https://github.com/ghostty-org/ghostty/issues/14203)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This commit refactors our use of translate-c, in preparation for larger
  removal of `cImport` and better co-ordination between building of C
  dependencies and translation of headers.
  
  The major update is the creation of an internal helper package that
  wraps our use of the external translate-c library. This allows us to not
  only have better shorthand and a data-driven, declarative approach to C
  translation (versus the otherwise more imperative approach), it also
  funnels the external dependency into a single package instead of
  spreading it out among what will be an increasingly larger amount of
  places as dependencies in `pkg/` get updated.
  
  It also includes some refactors, namely to the harfbuzz package, which
  has had its individual settings refactored into helpers to allow for the
  settings to be better shared between translation and the build of the
  c-based static library.
  
  Wuffs has also had a bit of a refactor too so that we don't generate a
  file with all of the macro defines in it - we just send these in as `-D`
  flags now.
  ```

## September 10, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/34467384606), [2](https://github.com/ghostty-org/ghostty/actions/runs/34461061903), [3](https://github.com/ghostty-org/ghostty/actions/runs/34447229683)  
Summary: 3 runs • 7 commits • 5 authors

### Changes

- [`53ae1dd`](https://github.com/ghostty-org/ghostty/commit/53ae1dd8bc318fcd139b1a51216a9355a642bd91) update translation ([@anhthang](https://github.com/anhthang))
- [`d13d439`](https://github.com/ghostty-org/ghostty/commit/d13d4399557dbbd81dc462aa1a314d5dba531db8) update ([@anhthang](https://github.com/anhthang))
- [`44f2a44`](https://github.com/ghostty-org/ghostty/commit/44f2a44df7e8c4a0c6df3f7d872ef3d7ead88e51) i18n: update `vi` translation for 1.4 ([#13783](https://github.com/ghostty-org/ghostty/issues/13783)) ([@00-kat](https://github.com/00-kat))
- [`8a3dbc8`](https://github.com/ghostty-org/ghostty/commit/8a3dbc8ce6f450f810e3b05be72690c103e1827b) i18n(hr): spiffy up the translation ([@neoto](https://github.com/neoto))
  ```text
  Adds some linguistic polish mentioned in [my
  review](https://github.com/ghostty-org/ghostty/pull/14019#pullrequestreview-5146552587)
  and throughout the comments.
  
  Contributes to #13766
  ```
- [`6d8f8b9`](https://github.com/ghostty-org/ghostty/commit/6d8f8b9aa739e84a7cbaab2880dfdb5601e1c42e) chore: make event reporting explicit ([@neoto](https://github.com/neoto))
- [`ea624f5`](https://github.com/ghostty-org/ghostty/commit/ea624f5a8cdab0ca353be76a7b5416b76fd58ce2) i18n(hr): spiffy up the translation ([#14194](https://github.com/ghostty-org/ghostty/issues/14194)) ([@trag1c](https://github.com/trag1c))
  ```text
  Adds some linguistic polish mentioned in [my
  
  review](https://github.com/ghostty-org/ghostty/pull/14019#pullrequestreview-5146552587)
  and throughout the comments.
  
  Contributes to #13766
  
  CC: @Filip7 @kristina8888
  ```
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

