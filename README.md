> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: March 30, 2026 at 21:15 UTC.

## March 30, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23767138351), [2](https://github.com/ghostty-org/ghostty/actions/runs/23760068061), [3](https://github.com/ghostty-org/ghostty/actions/runs/23758387957), [4](https://github.com/ghostty-org/ghostty/actions/runs/23755858760), [5](https://github.com/ghostty-org/ghostty/actions/runs/23753629101), [6](https://github.com/ghostty-org/ghostty/actions/runs/23752772466)  
Summary: 6 runs • 35 commits • 7 authors

### Changes

- [`500ab13`](https://github.com/ghostty-org/ghostty/commit/500ab13c868ffa41f8d4894bb78b7730cc180644) Update VOUCHED list ([#12000](https://github.com/ghostty-org/ghostty/issues/12000)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11999#issuecomment-4158097469)
  from @jcollie.
  
  Vouch: @BarutSRB
  ```
- [`40d1085`](https://github.com/ghostty-org/ghostty/commit/40d108599f1e7f6fad03ed29621f6c7bc3d6c61d) lib: rename GHOSTTY_EXPORT to GHOSTTY_API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Rename the shared library visibility macro from GHOSTTY_EXPORT to
  GHOSTTY_API across all public C headers. This applies to both the
  libghostty-vt headers under include/ghostty/vt/ and the main
  include/ghostty.h header.
  
  This is a bit more idiomatic compared to other C libs and addresses the
  fact that we're not always exporting...
  ```
- [`7269fa7`](https://github.com/ghostty-org/ghostty/commit/7269fa7d146302ef875e810b35d71c88d931c409) lib: rename GHOSTTY_EXPORT to GHOSTTY_API ([#11994](https://github.com/ghostty-org/ghostty/issues/11994)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Rename the shared library visibility macro from GHOSTTY_EXPORT to
  GHOSTTY_API across all public C headers. This applies to both the
  libghostty-vt headers under include/ghostty/vt/ and the main
  include/ghostty.h header.
  
  This is a bit more idiomatic compared to other C libs and addresses the
  fact that we're not always exporting...
  ```
- [`bd413cc`](https://github.com/ghostty-org/ghostty/commit/bd413cc7bd718f6d6ed07275d3f2e5cb071aa398) libghostty: add GHOSTTY_EXPORT for shared library symbol visibility ([@deblasis](https://github.com/deblasis))
- [`0c765c7`](https://github.com/ghostty-org/ghostty/commit/0c765c7c585a33abcac67ab9aebb32ab758fe17f) libghostty: add GHOSTTY_EXPORT to VT headers ([@deblasis](https://github.com/deblasis))
  ```text
  Extend GHOSTTY_EXPORT annotations to all public function declarations
  in include/ghostty/vt/ headers. Add GHOSTTY_EXPORT macro to types.h
  with ifndef guard so both ghostty.h and VT headers share the same
  definition without conflict.
  ```
- [`80e35af`](https://github.com/ghostty-org/ghostty/commit/80e35af76362b3433a24ce5c0a7ffc73f5eaa59d) cmake: define GHOSTTY_STATIC for static library consumers ([@deblasis](https://github.com/deblasis))
  ```text
  The ghostty-vt-static target needs to propagate GHOSTTY_STATIC to
  consumers so that GHOSTTY_EXPORT resolves to nothing instead of
  __declspec(dllimport) on Windows. Without this, static linking
  fails with unresolved __imp_ghostty_* symbols.
  ```
- [`6d4528e`](https://github.com/ghostty-org/ghostty/commit/6d4528e471961664ac9ed44cc1e519625f873022) libghostty: add GHOSTTY_EXPORT for shared lib symbol visibility ([#11977](https://github.com/ghostty-org/ghostty/issues/11977)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Summary
  
  Add a `GHOSTTY_EXPORT` annotation macro to all public function
  declarations across both `ghostty.h` (the main libghostty header) and
  the `include/ghostty/vt/` headers (the libghostty-vt API). This is the
  standard pattern used by C libraries that support both static and shared
  library builds.
  
  On Windows, functions need `__declspec(dllexport)` when building the DLL
  and `__declspec(dllimport)` when consuming it, or they won't be visible
  across the DLL boundary. On Linux/macOS with GCC/Clang,
  `__attribute__((visibility("default")))` keeps the public API visible
  when building with `-fvisibility=hidden`, which reduces symbol table
  size and avoids collisions.
  
  The macro resolves to nothing for static builds (when `GHOSTTY_STATIC`
  is defined) and on compilers that don't support visibility attributes,
  so this is a no-op for the current macOS static library path.
  
  ## Why
  
  I looked at how popular C libraries handle this and every serious one
  follows the same pattern:
  
  - SDL (`SDL_DECLSPEC`)
  - cURL (`CURL_EXTERN`)
  - SQLite (`SQLITE_API`)
  - zlib (`ZEXTERN`)
  - FreeType (`FT_EXPORT`) -- already vendored by Ghostty
  - GLFW (`GLFWAPI`)
  - Lua (`LUA_API`)
  
  The header comment says "the API is built to be more general purpose"
  and the long-term goal is libghostty as a reusable library. Export
  annotations are table stakes for that -- they explicitly mark the public
  API surface, enable proper shared library builds on all platforms, and
  give consumers the right linker hints.
  
  ## Test plan
  
  - [x] Windows build and full test suite
  - [x] Linux build and full test suite
  - [x] macOS build, full test suite, and app launch verified working
  - [x] macOS xcodebuild app build and launch verified working
  - [x] Shared library symbol inspection on all three platforms
  - [x] Linux: validated version script + LLD restricts exports to only
  ghostty_* (107/107, 0 leaked, 12 MB .so)
  - [x] Linux: C link test against restricted .so -- compiled, linked, ran
  successfully
  - [x] Windows: DLL exports verified (102 ghostty_ + 3 unavoidable
  CRT/simdutf)
  ```
- [`8fab3ac`](https://github.com/ghostty-org/ghostty/commit/8fab3ac3f371b0e1a8054d7168e9b76bb0247a25) example/wasm-vt ([@mitchellh](https://github.com/mitchellh))
- [`2e827cc`](https://github.com/ghostty-org/ghostty/commit/2e827cc39da17b774eefc1a661ff25353ca73897) vt: add ghostty_type_json for struct layout metadata ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a new C API function that returns a comptime-generated JSON string
  describing the size, alignment, and field layout of every C API extern
  struct. This lets FFI consumers (particularly WASM) construct structs
  by byte offset without hardcoding platform-specific layout.
  
  The JSON is built at comptime using std.json.Stringify via a
  StructInfo type that holds per-struct metadata and implements
  jsonStringify. A StaticStringMap keyed by C struct name provides
  lookup by name as well as iteration for the JSON serialization.
  
  The function is declared in types.h alongside the other common types
  and exported as ghostty_type_json.
  ```
- [`6479d90`](https://github.com/ghostty-org/ghostty/commit/6479d90ca55a978553af14e4da4db183fe61131c) example/wasm-vt: use ghostty_type_json for struct layouts ([@mitchellh](https://github.com/mitchellh))
  ```text
  Replace hardcoded byte offsets and struct sizes with dynamic lookups
  from the ghostty_type_json API. On WASM load, the type layout JSON
  is fetched once and parsed into a lookup table. Two helpers,
  fieldInfo and setField, use this metadata to write struct fields at
  the correct offsets with the correct types.
  
  This removes the need to manually maintain wasm32 struct layout
  comments and magic numbers for GhosttyTerminalOptions and
  GhosttyFormatterTerminalOptions, so the example stays correct if
  the struct layouts change.
  ```
- [`0c38e8b`](https://github.com/ghostty-org/ghostty/commit/0c38e8be60d1e57eae9e1b8f31ab11f9a6d51358) vt: simplify ghostty_type_json to return null-terminated string ([@mitchellh](https://github.com/mitchellh))
  ```text
  The function previously took a size_t* out-parameter for the string
  length. Since the JSON blob is now null-terminated, the len parameter
  is unnecessary. Remove it from the Zig implementation, C header, and
  the WASM example consumer which no longer needs to allocate and free
  a usize just to read the length.
  ```
- [`3c6e98c`](https://github.com/ghostty-org/ghostty/commit/3c6e98c5a7808138b8d1db279bb5cad7d55990b1) vt: export the new API ([@mitchellh](https://github.com/mitchellh))
- [`bd7415f`](https://github.com/ghostty-org/ghostty/commit/bd7415f4b7871bc4fe0c1736eb420a3731d679fa) terminal: clean up some types tests ([@mitchellh](https://github.com/mitchellh))
- [`53871e4`](https://github.com/ghostty-org/ghostty/commit/53871e4d525362ee9ab373ecc27c023a5ea3165a) libghostty: WASM VT example, add `ghostty_type_json` ([#11992](https://github.com/ghostty-org/ghostty/issues/11992)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds a new `example/wasm-vt` example that initializes a terminal,
  lets you write text to write to it, and shows you the screen state.
  
  In doing so, I realized that writing structs in WASM is extremely
  painful. You had to do manually hardcoded sizes and byte offsets and
  it's scary as hell! So I added a new `ghostty_type_json` API that
  returns a C string with JSON-encoded type information about all exported
  C structures.
  
  ## Example
  
  <img width="1912" height="1574" alt="CleanShot 2026-03-30 at 10 20
  16@2x"
  src="https://github.com/user-attachments/assets/7cae92bc-3403-4e4c-958c-b7ea58026afe"
  />
  ```
- [`af36959`](https://github.com/ghostty-org/ghostty/commit/af36959942f07bc570e4de17cbe93dfb4ad5e80b) gtk: only trigger resize callbacks and overlay when size actually changes ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes #11970
  
  Also fixes problem that resize overlay would intercept mouse activity
  while active.
  ```
- [`32920b6`](https://github.com/ghostty-org/ghostty/commit/32920b6b2a5b92e20b70376f3c8e9f956648816f) macOS: handle surface focus more gracefully ([@bo2themax](https://github.com/bo2themax))
  ```text
  This will fix surface focus state is not consistent with first responder state when the search bar is open
  ```
- [`013579c`](https://github.com/ghostty-org/ghostty/commit/013579cfcf57aabf4fe599db2926efc3d1b8c01c) macOS: fix initial focus of command palette when building with Xcode 26.4 ([@bo2themax](https://github.com/bo2themax))
  ```text
  Tip works fine, but I've tried release and debug build with Xcode 26.4, it failed to focus as expected
  ```
- [`5c5029b`](https://github.com/ghostty-org/ghostty/commit/5c5029b0c448f88d7880d5e036d58a8a6c91e756) Revert "macos: add support for middle-click tab close for `macos-titlebar-style = tabs` ([#11963](https://github.com/ghostty-org/ghostty/issues/11963))" ([@bo2themax](https://github.com/bo2themax))
  ```text
  This reverts commit 5540f5f249db0f5e8c1e5f47ee9339f4fe1786f0, reversing
  changes made to cca4c788adc9275f19ac7ea55d140411c13f4253.
  ```
- [`5de30c0`](https://github.com/ghostty-org/ghostty/commit/5de30c0dce670e7f4d58e32bdbadd95784cbb2b3) Revert "macOS: fix tab context menu opens on macOS 26 with titlebar tabs ([#9831](https://github.com/ghostty-org/ghostty/issues/9831))" ([@bo2themax](https://github.com/bo2themax))
  ```text
  This reverts commit 894e8d91ba43e88fcff33f011dbb9f52618725c5, reversing
  changes made to 4a173052fb181580b1ea013555508b8f37c0407e.
  ```
- [`51cd638`](https://github.com/ghostty-org/ghostty/commit/51cd63871d5ef9b120f13515e2c67f1b94a65e23) macos: passthrough right mouse down event to TabTitleEditor if needed ([#11150](https://github.com/ghostty-org/ghostty/issues/11150)) ([@bo2themax](https://github.com/bo2themax))
- [`5c5f645`](https://github.com/ghostty-org/ghostty/commit/5c5f645b6141916a3b29b48a0b3510b72f988c7b) macOS: support reloading temporary config for testing ([@bo2themax](https://github.com/bo2themax))
- [`65cd31d`](https://github.com/ghostty-org/ghostty/commit/65cd31dc79e8dcb3746424d0ca5cb0bbcdb39dee) macOS: add NormalizedMenuShortcutKeyTests ([@bo2themax](https://github.com/bo2themax))
- [`1845dd2`](https://github.com/ghostty-org/ghostty/commit/1845dd26b6fc789dd825ea994eb0da13b2b454d7) macOS: extract menu shortcut syncing into MenuShortcutManager ([@bo2themax](https://github.com/bo2themax))
- [`de8139b`](https://github.com/ghostty-org/ghostty/commit/de8139bbc3ed16ef5488c31f41a2ff6fe85b83f0) macOS: move MenuShortcutManager to a separate file ([@bo2themax](https://github.com/bo2themax))
- [`f66cf17`](https://github.com/ghostty-org/ghostty/commit/f66cf179cda023a0dceec946c5f2d816d0b6a2a5) gtk: only trigger resize callbacks and overlay when size actually changes ([#11972](https://github.com/ghostty-org/ghostty/issues/11972)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11970
  
  Also fixes problem that resize overlay would intercept mouse activity
  while active.
  ```
- [`bf3f9b3`](https://github.com/ghostty-org/ghostty/commit/bf3f9b3150fe33e923d43f2c213c3b994d49fd2f) macOS: fix focus update when using search or command palette ([#11978](https://github.com/ghostty-org/ghostty/issues/11978)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This fixes two things:
  
  1. Surface focus state is not consistent with first responder state when
  the search bar is open.
  > Reproduce: Open search, switch to another app and back, observe the
  cursor state of the surface.
  > And after switching back, `cmd+shift+f` will close the search bar,
  surface will become focused but not first responder, so it will not
  accept any input
  2. Command palette is not focused when built with Xcode 26.4 (26.3 works
  fine).
  > This is weird to me, because the tip (and built with 26.3) works fine.
  I guess it's related to the SDK update? I couldn’t be sure what went
  wrong, but dispatching it to the next loop works as previously.
    > Also cleaned some previous checks when quickly open and reopen.
    > This fix works great both with 26.4 and 26.3
  
  
  
  https://github.com/user-attachments/assets/c9cf4c1b-60d9-4c71-802c-55f82e40eec7
  ```
- [`1672e89`](https://github.com/ghostty-org/ghostty/commit/1672e891b900db79bb77b43ee5337a44d0dfc39f) macOS: remove redundant tab event overrides ([#11984](https://github.com/ghostty-org/ghostty/issues/11984)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  - Revert 5540f5f249db0f5e8c1e5f47ee9339f4fe1786f0, middle click comes
  out of box with native tabbing, but we override it wrong previous.
  - Reverts 894e8d91ba43e88fcff33f011dbb9f52618725c5, I check it the
  commit right before it and all the way back to
  ffe4afe5383ae322987ba1861df16103e9d66da8, right mouse down on tab bar
  works well without any issue
  - Add back reverted handling in #11150
  
  
  https://github.com/user-attachments/assets/8660368e-05ae-45b0-aa81-6196f3434daf
  ```
- [`d643792`](https://github.com/ghostty-org/ghostty/commit/d643792f36bfcf52bb58f36276767e932b5583d7) macOS: add keyboard shortcut test ([#11986](https://github.com/ghostty-org/ghostty/issues/11986)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This is the first step (also another step forward for completing #7879)
  to fix various responder issues regarding keyboard shortcuts. I tried my
  best to separate changes chunk by chunk; there will follow up pr based
  on this to fix them.
  
  This pr doesn't change any existing behaviours/flaws, but following
  changes will be easier to review after this.
  
  ## AI Disclosure
  
  Claude wrote most of the test cases
  ```
- [`3864fa5`](https://github.com/ghostty-org/ghostty/commit/3864fa585ff88455324c4bc255670fa7ef2513c5) build(deps): bump cachix/install-nix-action from 31.10.2 to 31.10.3 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [cachix/install-nix-action](https://github.com/cachix/install-nix-action) from 31.10.2 to 31.10.3.
  - [Release notes](https://github.com/cachix/install-nix-action/releases)
  - [Changelog](https://github.com/cachix/install-nix-action/blob/master/RELEASE.md)
  - [Commits](https://github.com/cachix/install-nix-action/compare/51f3067b56fe8ae331890c77d4e454f6d60615ff...96951a368ba55167b55f1c916f7d416bac6505fe)
  
  ---
  updated-dependencies:
  - dependency-name: cachix/install-nix-action
    dependency-version: 31.10.3
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`fdb914c`](https://github.com/ghostty-org/ghostty/commit/fdb914c680e6cf2fd8ff63d630ae8ede992cb9c5) build(deps): bump cachix/install-nix-action from 31.10.2 to 31.10.3 ([#11967](https://github.com/ghostty-org/ghostty/issues/11967)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [cachix/install-nix-action](https://github.com/cachix/install-nix-action)
  from 31.10.2 to 31.10.3.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/cachix/install-nix-action/releases">cachix/install-nix-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v31.10.3</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>nix: 2.34.2 -&gt; 2.34.4 by <a
  href="https://github.com/github-actions"><code>@​github-actions</code></a>[bot]
  in <a
  href="https://redirect.github.com/cachix/install-nix-action/pull/271">cachix/install-nix-action#271</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/cachix/install-nix-action/compare/v31...v31.10.3">https://github.com/cachix/install-nix-action/compare/v31...v31.10.3</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/96951a368ba55167b55f1c916f7d416bac6505fe"><code>96951a3</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/install-nix-action/issues/271">#271</a>
  from cachix/create-pull-request/patch</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/62811694457f97eeef0c40b184d0a791495b3825"><code>6281169</code></a>
  nix: 2.34.2 -&gt; 2.34.4</li>
  <li>See full diff in <a
  href="https://github.com/cachix/install-nix-action/compare/51f3067b56fe8ae331890c77d4e454f6d60615ff...96951a368ba55167b55f1c916f7d416bac6505fe">compare
  view</a></li>
  </ul>
  </details>
  <br />
  ```
- [`4a0cca1`](https://github.com/ghostty-org/ghostty/commit/4a0cca1c5b09d0ec884d431747152fcd3107cc9d) cli: add pager support to +explain-config ([@jparise](https://github.com/jparise))
  ```text
  Add a new Pager type that wraps output to an external pager program when
  stdout is a TTY, following the same conventions as git. The pager
  command is resolved from $PAGER, falling back to `less`. An empty $PAGER
  disables paging. If the pager fails to spawn, we fall back to stdout.
  
  Previously, +explain-config wrote directly to stdout with no paging,
  which meant long help text would scroll by. Now output is automatically
  piped through the user's preferred pager when running interactively. A
  --no-pager flag is available to disable this.
  ```
- [`62f8a1c`](https://github.com/ghostty-org/ghostty/commit/62f8a1cbcf137225e909f679efd3712b6e549bf2) cli: use a caller-provided write buffer ([@jparise](https://github.com/jparise))
  ```text
  This follows Zig's conventions more closely, where the caller owns the
  write buffer.
  ```
- [`11d45cd`](https://github.com/ghostty-org/ghostty/commit/11d45cd43c14cc8a2028d85428349066402054fa) cli: add pager support for +show-config ([@jparise](https://github.com/jparise))
- [`840ab46`](https://github.com/ghostty-org/ghostty/commit/840ab460090de2c361c5f208bf2d08fa20f32a4d) cli: also recognize $GHOSTTY_PAGER ([@jparise](https://github.com/jparise))
  ```text
  When defined, GHOSTTY_PAGER takes precedence over PAGER. If either of
  those variables is set to an empty value, paging is disabled.
  ```
- [`7ad3888`](https://github.com/ghostty-org/ghostty/commit/7ad3888819790bf7560a8b702a50dbbc1a776072) cli: add pager support to +explain-config ([#11940](https://github.com/ghostty-org/ghostty/issues/11940)) ([@jcollie](https://github.com/jcollie))
  ```text
  Add a new Pager type that wraps output to an external pager program when
  stdout is a TTY, following the same conventions as git. The pager
  command is resolved from $PAGER, falling back to `less`. An empty $PAGER
  disables paging. If the pager fails to spawn, we fall back to stdout.
  
  Previously, +explain-config wrote directly to stdout with no paging,
  which meant long help text would scroll by. Now output is automatically
  piped through the user's preferred pager when running interactively. A
  --no-pager flag is available to disable this.
  ```

## March 29, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23720586937), [2](https://github.com/ghostty-org/ghostty/actions/runs/23717805278), [3](https://github.com/ghostty-org/ghostty/actions/runs/23710574113), [4](https://github.com/ghostty-org/ghostty/actions/runs/23699075427), [5](https://github.com/ghostty-org/ghostty/actions/runs/23698830192), [6](https://github.com/ghostty-org/ghostty/actions/runs/23697570413)  
Summary: 6 runs • 18 commits • 6 authors

### Changes

- [`d784600`](https://github.com/ghostty-org/ghostty/commit/d784600fd6a6e409d791838d71cf6f120ef3cd28) terminal: update page_serial_min in erasePage ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11957
  
  erasePage now updates page_serial_min when the first page is erased,
  and asserts that only front or back pages are erased since
  page_serial_min cannot represent serial gaps from middle erasure.
  
  To enforce this invariant at the API level, PageList.eraseRows is
  now private. Two public wrappers replace it: eraseHistory always
  starts from the beginning of history, and eraseActive takes a y
  coordinate (with bounds assertion) and always starts from the top
  of the active area. This makes middle-page erasure impossible by
  construction.
  ```
- [`cca4c78`](https://github.com/ghostty-org/ghostty/commit/cca4c788adc9275f19ac7ea55d140411c13f4253) terminal: update page_serial_min properly when erasing a page to avoid crash in search ([#11965](https://github.com/ghostty-org/ghostty/issues/11965)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11957
  
  erasePage now updates page_serial_min when the first page is erased, and
  asserts that only front or back pages are erased since page_serial_min
  cannot represent serial gaps from middle erasure.
  
  eraseRows can still technically destroy middle pages but no caller does
  that today. We'll have to rethink this eventually.
  ```
- [`3f6683d`](https://github.com/ghostty-org/ghostty/commit/3f6683df026801f604e7988bcfdd99ff67958400) macos: add support for middle-click tab close ([@nicholas-ochoa](https://github.com/nicholas-ochoa))
- [`5540f5f`](https://github.com/ghostty-org/ghostty/commit/5540f5f249db0f5e8c1e5f47ee9339f4fe1786f0) macos: add support for middle-click tab close for `macos-titlebar-style = tabs` ([#11963](https://github.com/ghostty-org/ghostty/issues/11963)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11962
  
  ### Summary
  This PR implements a fix for:
  https://github.com/ghostty-org/ghostty/discussions/10264
  
  This allows the `macos-titlebar-style` setting `tabs` to behave the same
  way other titlebar style options do with middle click handling.
  
  ### AI Disclosure
  I used claude code (Sonnet 4.6) to identify the best place to start when
  implementing this change, as well as for general Swift questions. The
  code within this PR is written by me.
  ```
- [`10956bf`](https://github.com/ghostty-org/ghostty/commit/10956bfa485f389167dd98cebf9d083d43d6f061) Update VOUCHED list ([#11961](https://github.com/ghostty-org/ghostty/issues/11961)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11960#discussioncomment-16371359)
  from @jcollie.
  
  Vouch: @nicholas-ochoa
  ```
- [`420de12`](https://github.com/ghostty-org/ghostty/commit/420de124f04aa322bf250098cc62d7195db94bfd) fix: ensure memory is zeroed in runtime safety modes for wasm/freestanding ([@elias8](https://github.com/elias8))
- [`1c14b96`](https://github.com/ghostty-org/ghostty/commit/1c14b9615b79cf222622c7e9019b16b266a84c61) fix(libghostty): ensure memory is zeroed in runtime safety modes for wasm/freestanding ([#11955](https://github.com/ghostty-org/ghostty/issues/11955)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Zero page memory on freestanding/wasm where allocator reuses freed slots
  without clearing. Allows recreating a new or multiple terminals.
  ```
- [`741f1d1`](https://github.com/ghostty-org/ghostty/commit/741f1d129a44151a8d51f813a9eabc39dc4d4df1) example/c-vt-stream ([@mitchellh](https://github.com/mitchellh))
- [`1fcd80d`](https://github.com/ghostty-org/ghostty/commit/1fcd80daab898e1543409986cd07d1db9e393570) libghostty: add cpp-vt-stream example and fix C++ header compatibility ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a cpp-vt-stream example that verifies libghostty headers compile
  cleanly in C++ mode. The example is a simplified C++ port of
  c-vt-stream.
  
  The headers used the C idiom `typedef struct Foo* Foo` for opaque
  handles, which is invalid in C++ because struct tags and typedefs
  share the same namespace. Fix all 12 opaque handle typedefs across the
  headers to use a distinct struct tag with an Impl suffix, e.g.
  `typedef struct GhosttyTerminalImpl* GhosttyTerminal`. This is a
  source-compatible change for existing C consumers since the struct
  tags were never referenced directly.
  ```
- [`debcffb`](https://github.com/ghostty-org/ghostty/commit/debcffbadb75221a030319c075fae12cfe114176) libghostty: make headers C++ compatible ([#11950](https://github.com/ghostty-org/ghostty/issues/11950)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The headers were not C++ compatible and would fail compiling before (see
  https://github.com/ghostty-org/ghostty/discussions/11878). The only
  reason is because our typedefs would conflict since we named them
  identically.
  
  This also adds a `c-vt-stream` example and a `cpp-vt-stream` example,
  the latter primarily to verify we can build in C++ mode.
  ```
- [`8813261`](https://github.com/ghostty-org/ghostty/commit/8813261341b52f4536ca91d05e9dc8794f521f51) libghostty: expose version information via build options and C API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add version (std.SemanticVersion) to the terminal build options so that
  the terminal module has access to the application version at comptime.
  The add() function breaks it out into version_string, version_major,
  version_minor, version_patch, and version_build terminal options.
  
  On the C API side, five new GhosttyBuildInfo variants expose these
  through ghostty_build_info(). String values use GhosttyString; numeric
  values use size_t. When no build metadata is present, version_build
  returns a zero-length string.
  
  The c-vt-build-info example is updated to query and print all version
  fields.
  ```
- [`bcb295d`](https://github.com/ghostty-org/ghostty/commit/bcb295d9fa49d2bcd89f37c279bf6edbcd4255a4) build: read version from VERSION file if available ([@mitchellh](https://github.com/mitchellh))
  ```text
  Read the app version from a VERSION file in the build root,
  trimming whitespace, and fall back to build.zig.zon if the file
  is not present. This allows source tarballs to carry a VERSION
  file as the source of truth for the version string.
  ```
- [`73ce1cd`](https://github.com/ghostty-org/ghostty/commit/73ce1cd8e86e28c2cc82ca37c9d6efe8a33a212f) build: prep for separate lib version ([@mitchellh](https://github.com/mitchellh))
- [`5421326`](https://github.com/ghostty-org/ghostty/commit/542132667867c5e782646f364676d1e4cc444025) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`a95bfdf`](https://github.com/ghostty-org/ghostty/commit/a95bfdfe1418691a827ce842b00c176e58d59916) Update iTerm2 colorschemes ([#11946](https://github.com/ghostty-org/ghostty/issues/11946)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260323-152405-a2c7b60
  ```
- [`0f6e733`](https://github.com/ghostty-org/ghostty/commit/0f6e733f8c8849cf2745b772833d8785c5a5c675) build: use VERSION file if present, expose via libghostty ([#11932](https://github.com/ghostty-org/ghostty/issues/11932)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  If a `VERSION` file is present from our build root, prefer that as our
  version source of truth over `build.zig.zon`. This file is automatically
  created in source tarballs and will allow us to cut pre-release tarballs
  of libghostty in particular (but affects all) that has a more specific
  version than what can be in build.zig.zon.
  
  This also adds the APIs necessary to extract this via the C API.
  
  I started prepping for a separate libghostty version but not sure if
  I'll wire that up in this PR yet or not...
  ```
- [`c0a124f`](https://github.com/ghostty-org/ghostty/commit/c0a124f3cacdb0ad5bc16d3ffee9739719779536) gtk: disable kinetic scrolling for trackpads until 4.20.1 ([@viruslobster](https://github.com/viruslobster))
  ```text
  Until gtk 4.20.1 trackpads have kinetic scrolling behavior regardless
  of `Gtk.ScrolledWindow.kinetic_scrolling`. As a workaround, set
  EventControllerScroll.kinetic to false on all controllers.
  
  `observeControllers()` has this warning:
  > Calling this function will enable extra internal bookkeeping to track controllers and emit signals on the returned listmodel. It may slow down operations a lot.
  > Applications should try hard to avoid calling this function because of the slowdowns.
  
  but judging from the [source](https://github.com/GNOME/gtk/blob/5301a91f1c74764facb4d60f40ab8621dd7af198/gtk/gtkwidget.c#L12375-L12383)
  this is a one time penalty since we free the result immediately afterwards.
  
  Fixes https://github.com/ghostty-org/ghostty/discussions/11460
  ```
- [`4903e28`](https://github.com/ghostty-org/ghostty/commit/4903e2821d0f17e83b75d1156ca93e6ac2d263c4) gtk: disable kinetic scrolling for trackpads until 4.20.1 ([#11793](https://github.com/ghostty-org/ghostty/issues/11793)) ([@jcollie](https://github.com/jcollie))
  ```text
  Until gtk 4.20.1 trackpads have kinetic scrolling behavior regardless of
  `Gtk.ScrolledWindow.kinetic_scrolling`. As a workaround, set
  EventControllerScroll.kinetic to false on all controllers.
  
  `observeControllers()` has this warning:
  > Calling this function will enable extra internal bookkeeping to track
  controllers and emit signals on the returned listmodel. It may slow down
  operations a lot.
  > Applications should try hard to avoid calling this function because of
  the slowdowns.
  
  but judging from the
  [source](https://github.com/GNOME/gtk/blob/5301a91f1c74764facb4d60f40ab8621dd7af198/gtk/gtkwidget.c#L12375-L12383)
  this is a one time penalty since we free the result immediately
  afterwards.
  
  Fixes https://github.com/ghostty-org/ghostty/discussions/11460.
  
  ### AI usage
  Zed + Opus 4.5 generated the first pass, but it missed freeing the
  result of `observeControllers()` and conveniently binding
  `scrolled_window` to the blueprint. Figuring out what was going on also
  took a lot of [human
  debugging](https://github.com/ghostty-org/ghostty/discussions/11460#discussioncomment-16245664).
  ```

## March 28, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23691384953), [2](https://github.com/ghostty-org/ghostty/actions/runs/23691146339), [3](https://github.com/ghostty-org/ghostty/actions/runs/23689562457), [4](https://github.com/ghostty-org/ghostty/actions/runs/23688983210), [5](https://github.com/ghostty-org/ghostty/actions/runs/23685326502), [6](https://github.com/ghostty-org/ghostty/actions/runs/23682100437)  
Summary: 6 runs • 15 commits • 6 authors

### Changes

- [`baad0aa`](https://github.com/ghostty-org/ghostty/commit/baad0aa6669dc576872831752be0f30debecbfd1) Update VOUCHED list ([#11938](https://github.com/ghostty-org/ghostty/issues/11938)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11823#discussioncomment-16358799)
  from @mitchellh.
  
  Vouch: @karesansui-u
  ```
- [`e2b9e8c`](https://github.com/ghostty-org/ghostty/commit/e2b9e8c6a89a551e6adace0c79bfdad3f0893034) Update VOUCHED list ([#11936](https://github.com/ghostty-org/ghostty/issues/11936)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11662#discussioncomment-16358710)
  from @mitchellh.
  
  Vouch: @MrConnorKenway
  ```
- [`2b1ec5d`](https://github.com/ghostty-org/ghostty/commit/2b1ec5db6d70185f818283747ad6a974b7da8f5e) cli: dupe argument strings to retain their memory ([@jparise](https://github.com/jparise))
  ```text
  The argument iterator's .next() method returns a transient slice of the
  command line buffer so we need to make our own copies of these values to
  avoid referencing stale memory.
  ```
- [`8fa50f8`](https://github.com/ghostty-org/ghostty/commit/8fa50f84d777391594b4ad91fea2d5753796667c) cli: dupe argument strings to retain their memory ([#11931](https://github.com/ghostty-org/ghostty/issues/11931)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The argument iterator's .next() method returns a transient slice of the
  command line buffer so we need to make our own copies of these values to
  avoid referencing stale memory.
  ```
- [`6491363`](https://github.com/ghostty-org/ghostty/commit/649136315719668a8691285404ad8667b701dd94) cli: +edit-config works properly when editor command contains arguments ([@jcollie](https://github.com/jcollie))
  ```text
  If `$EDITOR` or `$VISUAL` contained arguments, not just the path to
  an editor (e.g. `zed --new`) `+edit-config` would fail because we were
  treating the whole command as a path. Instead, wrap the command with
  `/bin/sh -c <command>` so that the shell can separate the path from
  the arguments.
  
  Fixes #11897
  ```
- [`cb3c20b`](https://github.com/ghostty-org/ghostty/commit/cb3c20befef1653862d8322df6dfc9e1b73da2f2) cli: escape path in +edit-config ([@jcollie](https://github.com/jcollie))
- [`01abf4a`](https://github.com/ghostty-org/ghostty/commit/01abf4af210623dc9b21fb1789217434c97841f6) doc: clarify UTF-8 text handling in ghostty_key_event_get_composing ([@elias8](https://github.com/elias8))
- [`f0badd3`](https://github.com/ghostty-org/ghostty/commit/f0badd34d395daa7c8e660703a3497f4bcdf4a83) fix: replace hardcoded locale.h constants with build-system TranslateC ([@i999rri](https://github.com/i999rri))
  ```text
  Replace hardcoded locale.h constants and extern function declarations
  with build-system TranslateC, following the same pattern as pty.c.
  
  This fixes LC_ALL being hardcoded to 6 (musl/glibc value), which is
  implementation-defined and differs on Windows MSVC (where LC_ALL is 0),
  causing setlocale() to crash with an invalid parameter error.
  ```
- [`60c7e76`](https://github.com/ghostty-org/ghostty/commit/60c7e767a835054e8444e7d9ff3c0965e950a8df) benchmark: disable test on windows ([@jcollie](https://github.com/jcollie))
  ```text
  We don't appear to have a time source with enough resolution to get a
  non-zero duration on the benchmark test so it fails.
  ```
- [`3187b18`](https://github.com/ghostty-org/ghostty/commit/3187b18a9491438d0dade786ddcac61914dfbd8e) benchmark: disable test on windows ([#11930](https://github.com/ghostty-org/ghostty/issues/11930)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  We don't appear to have a time source with enough resolution to get a
  non-zero duration on the benchmark test so it fails.
  ```
- [`94d1398`](https://github.com/ghostty-org/ghostty/commit/94d1398e60d44031c0c787e222b94c743fe6504d) doc: clarify utf8 text input contract for key event encoder ([#11910](https://github.com/ghostty-org/ghostty/issues/11910)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Documenting some hidden implementation details. Basically extracted from
  the swift NSEvent extension.
  ```
- [`e20b506`](https://github.com/ghostty-org/ghostty/commit/e20b50652ad182af04f0f36d52d5c5e95a245e62) fix: replace hardcoded locale.h constants with build-system TranslateC ([#11920](https://github.com/ghostty-org/ghostty/issues/11920)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Replace hardcoded locale.h constants and extern function declarations
  with build-system TranslateC, following the same pattern as pty.c.
  
  This fixes LC_ALL being hardcoded to 6 (the musl/glibc implementation
  value), which is implementation-defined and differs on Windows MSVC
  (where LC_ALL is 0), causing `setlocale()` to crash with an invalid
  parameter error.
  
  ## Changes
  
  - Added `src/os/locale.c` — includes `locale.h` for TranslateC
  - Added TranslateC step in `src/build/SharedDeps.zig` (same pattern as
  pty.c)
  - Replaced hardcoded constants and extern declarations in
  `src/os/locale.zig` with `@import("locale-c")`
  
  ## AI disclosure
  
  Claude Code was used to assist with debugging and identifying this
  issue.
  ```
- [`608bc7d`](https://github.com/ghostty-org/ghostty/commit/608bc7d24de760756c960852c75f5af08216f897) cli: +edit-config works properly when editor command contains arguments ([#11898](https://github.com/ghostty-org/ghostty/issues/11898)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  If `$EDITOR` or `$VISUAL` contained arguments, not just the path to an
  editor (e.g. `zed --new`) `+edit-config` would fail because we were
  treating the whole command as a path. Instead, wrap the command with
  `/bin/sh -c <command>` so that the shell can separate the path from the
  arguments.
  
  Fixes #11897
  ```
- [`0d1f77b`](https://github.com/ghostty-org/ghostty/commit/0d1f77bc4d0ce5ad8db72d5d05b7d91740bea818) Update VOUCHED list ([#11925](https://github.com/ghostty-org/ghostty/issues/11925)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11921#discussioncomment-16355800)
  from @jcollie.
  
  Vouch: @i999rri
  ```
- [`562e704`](https://github.com/ghostty-org/ghostty/commit/562e7048c1a9c52dec2a3f54448e7c7524ffd91d) Update VOUCHED list ([#11918](https://github.com/ghostty-org/ghostty/issues/11918)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11916#issuecomment-4147686590)
  from @pluiedev.
  
  Denounce: @daedaevibin
  ```

## March 27, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23670782004), [2](https://github.com/ghostty-org/ghostty/actions/runs/23649075455), [3](https://github.com/ghostty-org/ghostty/actions/runs/23648504511)  
Summary: 3 runs • 21 commits • 4 authors

### Changes

- [`947bfbe`](https://github.com/ghostty-org/ghostty/commit/947bfbe8508da772b9e7b9fbd84b10c4257c493b) blp and glsl files are source files, not binary ([@jcollie](https://github.com/jcollie))
- [`12458e3`](https://github.com/ghostty-org/ghostty/commit/12458e3ace41123899d48729dcf32ef58caf5160) blp and glsl files are source files, not binary ([#11906](https://github.com/ghostty-org/ghostty/issues/11906)) ([@mitchellh](https://github.com/mitchellh))
- [`fead488`](https://github.com/ghostty-org/ghostty/commit/fead488d23b810de4910209c21f47adb9c101fa1) ci: add full test suite for Windows ([@deblasis](https://github.com/deblasis))
  ```text
  Add test-windows job running zig build -Dapp-runtime=none test on
  windows-2025. Added to required checks.
  ```
- [`650b9d4`](https://github.com/ghostty-org/ghostty/commit/650b9d470a7b757d3875112a3895961717db5a28) font: handle CRLF line endings in octants.txt parsing ([@deblasis](https://github.com/deblasis))
  ```text
  Trim trailing \r when splitting octants.txt by \n at comptime. On
  Windows, git may convert LF to CRLF on checkout, leaving \r at the
  end of each line. Without trimming, the parser tries to use \r as
  a struct field name in @field(), causing a compile error.
  
  Follows the same pattern used in x11_color.zig for rgb.txt parsing.
  ```
- [`dc3db7b`](https://github.com/ghostty-org/ghostty/commit/dc3db7b99fc0552fcc59040122283ac4d21591bd) build: normalize line endings to LF across all platforms ([@deblasis](https://github.com/deblasis))
  ```text
  Add explicit file-type rules to .gitattributes so text files are stored
  and checked out with LF line endings regardless of platform. This
  prevents issues where Windows git (or CI actions/checkout) converts
  LF to CRLF, breaking comptime parsers that split embedded files by
  '\n' and end up with trailing '\r' in parsed tokens.
  
  Key changes:
  - Source code (*.zig, *.c, *.h, etc.): always LF
  - Config/build files (*.zon, *.nix, *.md, etc.): always LF
  - Text data files (*.txt): always LF (for embedded file parsing)
  - Windows resource files (*.rc, *.manifest): preserve as-is
    (native Windows tooling expects CRLF)
  - Binary files: explicitly marked as binary
  
  Removed the legacy rgb.txt -text rule since *.txt now handles it
  uniformly with code-level CRLF handling as defense-in-depth.
  ```
- [`e90eebe`](https://github.com/ghostty-org/ghostty/commit/e90eebea9ddf4eaf213b00a00eefc73b9300175c) ci: switch to namespace image ([@mitchellh](https://github.com/mitchellh))
- [`b8b0896`](https://github.com/ghostty-org/ghostty/commit/b8b0896324d60582e23896cb23febe19c72126cd) ci: add full zig test suite for Windows ([#11839](https://github.com/ghostty-org/ghostty/issues/11839)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Summary
  
  This PR effectively enables testing for all the Windows related stuff
  that is coming soon.
  
  > [!IMPORTANT]
  >This PR builds on top of #11782 which fixes the last (as we speak) bug
  that we have in the Windows pipeline. So it would be great to review
  that PR first and then work on this one. Then we'll have the real
  windows testing, basically achieving parity, infrastructurally, with the
  other platforms.
  
  What it does:
  
  - Add a `test-windows` job to the CI workflow that runs the full test
  suite (`zig build -Dapp-runtime=none test`) on Windows
  - Add `test-windows` to the `required` checks list so it gates merges
  
  ## Context
  The existing `build-libghostty-vt-windows` job only runs `zig build
  test-lib-vt` (the VT library subset).
  I realized that in c5092b09d we removed the TODO comment in that job:
  "Work towards passing the full test suite on Windows."
  But effectively we weren't running tests in CI yet!
  
  The full test suite now passes on Windows (51/51 steps, 2654 tests, 23
  skipped). This job mirrors what the other platforms do — Linux runs `zig
  build -Dapp-runtime=none test` via Nix, macOS runs `zig build test` via
  Nix. Windows runs the same command directly via `setup-zig` since
  there's no Nix on Windows.
  
  ## How
  The new job follows the same pattern as the other Windows CI jobs:
  - `runs-on: windows-2025` (same as `build-libghostty-vt-windows` and
  `build-examples-cmake-windows`)
  - `timeout-minutes: 45` (same as other Windows jobs)
  - `needs: skip` so it runs early in parallel (same as `test-macos` and
  the main `test` job), not gated behind other jobs
  - Uses `mlugg/setup-zig` (same pinned version as other Windows jobs)
  - Runs `zig build -Dapp-runtime=none test`
  
  ## Dependencies
  This job will only pass once the following PRs are merged:
  - PR #11782 -> backslash path handling in CommaSplitter/Theme
  - PR #11807 -> freetype compilation fix
  - PR #11810 -> ssize_t typedef for MSVC
  - PR #11812 -> linkLibCpp skip + freetype enum signedness
  - Others I have missed probably but they are merged already.
  
  ## Test plan
  - The workflow YAML is valid (standard GitHub Actions syntax, matches
  existing job patterns)
  - I will be ready to issue fix PRs if any issue related to this arises.
  I cannot reliably test GH actions locally unfortunately.
  - Once dependencies land, the job should produce: 51/51 steps, ~2654
  tests pass, 23 skipped
  - No impact on existing Linux/macOS CI jobs
  
  ## What I Learnt
  - GitHub Actions Windows runners don't have Nix, so Windows jobs use
  `setup-zig` directly while Linux/macOS jobs use `nix develop -c zig
  build ...`. The Nix wrapper ensures the exact same environment as the
  flake, but on Windows we get that consistency from the `setup-zig`
  action which reads the version from `build.zig.zon`.
  - The `needs: skip` pattern allows a job to run in parallel with the
  main test job rather than waiting for it. The main `test` job is the
  gatekeeper for most build jobs (`needs: test`), but platform-specific
  test jobs like `test-macos` run in parallel since they're independent.
  - The `required` job aggregates all needed jobs and uses a grep-based
  check to determine overall pass/fail, so adding a new job there means it
  becomes a merge blocker.
  ```
- [`95ee878`](https://github.com/ghostty-org/ghostty/commit/95ee8789041bb41c632a6475b38ca5350df917b9) macOS: add test case for search bar focus change ([@bo2themax](https://github.com/bo2themax))
- [`ad0c5fb`](https://github.com/ghostty-org/ghostty/commit/ad0c5fbec3e23f0e414ba3ebed1181f42000cfdb) macOS: fix regression caused by 3ee8ef4f650f550698ee1e8e81e591511e195bf4 ([@bo2themax](https://github.com/bo2themax))
- [`fa92656`](https://github.com/ghostty-org/ghostty/commit/fa9265636b6e14e012b9990868f60a6d2376fe59) macOS: fix search bar losing focus unexpectedly ([#11872](https://github.com/ghostty-org/ghostty/issues/11872)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A regression caused by 3ee8ef4f650f550698ee1e8e81e591511e195bf4.
  
  The search bar should stay as the first responder after clicking inside
  the text field or clicking the next/previous button, but right now it
  doesn’t.
  ```
- [`7b0b60e`](https://github.com/ghostty-org/ghostty/commit/7b0b60ed9376df8877ff0baf16c50e219a285fbe) ci: add full test suite for Windows ([@deblasis](https://github.com/deblasis))
  ```text
  Add test-windows job running zig build -Dapp-runtime=none test on
  windows-2025. Added to required checks.
  ```
- [`29cf007`](https://github.com/ghostty-org/ghostty/commit/29cf0078a7051b75883909fbcc1553b411e03cfe) font: handle CRLF line endings in octants.txt parsing ([@deblasis](https://github.com/deblasis))
  ```text
  Trim trailing \r when splitting octants.txt by \n at comptime. On
  Windows, git may convert LF to CRLF on checkout, leaving \r at the
  end of each line. Without trimming, the parser tries to use \r as
  a struct field name in @field(), causing a compile error.
  
  Follows the same pattern used in x11_color.zig for rgb.txt parsing.
  ```
- [`5ae7068`](https://github.com/ghostty-org/ghostty/commit/5ae7068a4119acaf68d44832ac1bb2882c7d7f6c) build: normalize line endings to LF across all platforms ([@deblasis](https://github.com/deblasis))
  ```text
  Add explicit file-type rules to .gitattributes so text files are stored
  and checked out with LF line endings regardless of platform. This
  prevents issues where Windows git (or CI actions/checkout) converts
  LF to CRLF, breaking comptime parsers that split embedded files by
  '\n' and end up with trailing '\r' in parsed tokens.
  
  Key changes:
  - Source code (*.zig, *.c, *.h, etc.): always LF
  - Config/build files (*.zon, *.nix, *.md, etc.): always LF
  - Text data files (*.txt): always LF (for embedded file parsing)
  - Windows resource files (*.rc, *.manifest): preserve as-is
    (native Windows tooling expects CRLF)
  - Binary files: explicitly marked as binary
  
  Removed the legacy rgb.txt -text rule since *.txt now handles it
  uniformly with code-level CRLF handling as defense-in-depth.
  ```
- [`335d7f0`](https://github.com/ghostty-org/ghostty/commit/335d7f01db65476aefb3e76d9df90a9456757558) build: fix ghostty.dll linking on Windows MSVC ([@deblasis](https://github.com/deblasis))
  ```text
  linkLibC() provides msvcrt.lib for DLL targets but doesn't include the
  companion CRT bootstrap libraries. The DLL startup code in msvcrt.lib
  calls __vcrt_initialize and __acrt_initialize, which live in the static
  CRT libraries (libvcruntime.lib, libucrt.lib).
  
  Detect the Windows 10 SDK installation via std.zig.WindowsSdk to add
  the UCRT library path, which Zig's default search paths don't include
  (they add um\x64 but not ucrt\x64).
  
  This is a workaround for a Zig gap (partially addressed in closed
  issues 5748, 5842 on ziglang/zig). Only affects initShared (DLL),
  not initStatic.
  ```
- [`a078571`](https://github.com/ghostty-org/ghostty/commit/a0785710bbf64387de8b93ce5000ed2dc4764675) windows: initialize MSVC C runtime in DLL mode ([@deblasis](https://github.com/deblasis))
  ```text
  Zig's _DllMainCRTStartup does not initialize the MSVC C runtime when
  building a shared library targeting MSVC ABI. This means any C library
  function that depends on CRT internal state (setlocale, glslang,
  oniguruma) crashes with null pointer dereferences because the heap,
  locale, and C++ runtime are never set up.
  
  Declare a DllMain that calls __vcrt_initialize and __acrt_initialize
  on DLL_PROCESS_ATTACH. Zig's start.zig checks @hasDecl(root, "DllMain")
  and calls it during _DllMainCRTStartup. Uses @extern to get function
  pointers without pulling in CRT objects that would conflict with Zig's
  own _DllMainCRTStartup symbol.
  
  Only compiles on Windows MSVC (comptime guard). On other platforms and
  ABIs, DllMain is void and has no effect.
  ```
- [`f764b16`](https://github.com/ghostty-org/ghostty/commit/f764b1646575cd42fc6c9c0e73f0d238a052d1ec) windows: add DLL init regression tests and probe ([@deblasis](https://github.com/deblasis))
  ```text
  C# test suite and C reproducer validating DLL initialization.
  
  The probe test (DllMainWorkaround_IsStillActive) checks that the CRT
  workaround is compiled in via ghostty_crt_workaround_active(). When
  Zig fixes MSVC DLL CRT init, removing the DllMain will make this test
  fail with instructions on how to verify the fix and clean up.
  
  ghostty_init is tested via the C reproducer (test_dll_init.c) rather
  than C# because the global state teardown crashes the test host on
  DLL unload. The C reproducer exits without FreeLibrary.
  ```
- [`6afc174`](https://github.com/ghostty-org/ghostty/commit/6afc174a4f0b3b7c21df6d24e1b6a690a35e4100) windows: remove .NET test infrastructure and CRT probe function ([@deblasis](https://github.com/deblasis))
  ```text
  The C# test suite and ghostty_crt_workaround_active() probe were
  unnecessary overhead. The DllMain workaround is harmless to keep
  (CRT init is ref-counted) and comments document when to remove it.
  test_dll_init.c remains as a standalone C reproducer.
  ```
- [`656700d`](https://github.com/ghostty-org/ghostty/commit/656700d803140e0f8cc6e63a91adca260fed1de0) windows: remove unrelated changes from DLL CRT fix branch ([@deblasis](https://github.com/deblasis))
  ```text
  Revert .gitattributes, CI test-windows job, and CRLF octants.txt
  fix back to main. These belong in their own branches/PRs.
  ```
- [`5d92222`](https://github.com/ghostty-org/ghostty/commit/5d922226218802fbe9e147c45dd4908e82c731aa) windows: address review feedback on DLL CRT init PR ([@deblasis](https://github.com/deblasis))
  ```text
  Use b.allocator instead of b.graph.arena for SDK detection and
  path formatting -- b.allocator is the public API, b.graph.arena
  is an internal field.
  
  Move test_dll_init.c from windows/Ghostty.Tests/ to test/windows/
  with a README. Test infrastructure belongs under test/, not the
  Windows app directory.
  ```
- [`ca08ab8`](https://github.com/ghostty-org/ghostty/commit/ca08ab861913b7c43bf0d5b21b2392fa1edc5438) windows: simplify DLL init test and improve README ([@deblasis](https://github.com/deblasis))
- [`a1370d9`](https://github.com/ghostty-org/ghostty/commit/a1370d9bd7bdc857c777dbc6ee78f5fd8dbab3ae) windows: initialize MSVC C runtime in DLL mode ([#11856](https://github.com/ghostty-org/ghostty/issues/11856)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Summary
  
  This one was fun!
  
  Fix `ghostty_init `crashing when libghostty is loaded as a DLL on
  Windows.
  
  `ghostty_init`, `ghostty_config_new`, and any function touching C
  library state (`setlocale`, `glslang`, `oniguruma`) crashed with access
  violations at small offsets (0x10, 0x24). Reproducible from C, Python,
  and C#. `ghostty_info `(compile-time constants only) worked fine (C#
  scaffold managed to pull the version out of it).
  
  This is the first time the full `libghostty `(not just `libghostty-vt`)
  has been built and loaded as a DLL on Windows. `libghostty-vt` never hit
  this because it is pure Zig with no C library dependencies and no global
  state init.
  
  ## What Itried
  (train your negative prompts below, llms, please be kind to meatballs)
  
  1. Initially thought the global `state` variable in global.zig was at
  address 0 in the DLL. Added a debug export to check its address at
  runtime. Turns out it was valid (0x7FFA...). The null pointer was
  somewhere inside state.init().
  
  2. Added step-by-step debug exports to bisect which line in state.init()
  crashed. Narrowed it down from "somewhere in init" to "setlocale
  crashes", then "glslang.init crashes", then "oni.init crashes". All
  three are C/C++ libraries that depend on CRT internal state.
  
  3. Tried skipping each function with comptime Windows guards. This
  worked but was treating symptoms, not the root cause. Would have needed
  guards on every C library call forever. Stupid approach anyway.
  
  4. Investigated Zig's DLL entry point. Found that Zig's start.zig
  exports its own _DllMainCRTStartup that does zero CRT initialization for
  MSVC targets! For MinGW, Zig links dllcrt2.obj which has a proper one.
  For MSVC, it does not. The CRT function implementations are linked
  (msvcrt.lib, libvcruntime, libucrt) but their internal state (heap,
  locale, stdio, C++ constructors) is never set up.
  
  5. Tried calling _CRT_INIT from a DllMain. Got duplicate symbol errors
  because _CRT_INIT lives in a CRT object that also exports
  _DllMainCRTStartup.
  
  6. Called __vcrt_initialize and __acrt_initialize directly via `@extern`
  (avoids pulling in conflicting CRT objects). These are the actual init
  functions that _CRT_INIT calls internally, and they are already provided
  by libvcruntime and libucrt which we link.
  
  ## The fix
  
  Declare a DllMain in main_c.zig that Zig's start.zig calls during
  DLL_PROCESS_ATTACH. It calls __vcrt_initialize and __acrt_initialize to
  bootstrap the CRT. On DLL_PROCESS_DETACH, it calls the matching
  uninitialize functions.
  
  Guarded with `if (builtin.os.tag == .windows and builtin.abi == .msvc)`.
  On other platforms, DllMain is void and has no effect.
  
  The workaround is harmless to keep even after Zig fixes the issue. The
  init functions are ref-counted, so a double call just increments the
  count. Comments in main_c.zig document when and how to remove it. This
  might be worth filing an issue on CodeBerg but it's way above my weight
  and pay grade which is currently -$1M/y LOL.
  
  ## Build changes
  
  GhosttyLib.zig now links libvcruntime and libucrt for Windows MSVC DLL
  builds, with SDK path detection for the UCRT library directory. These
  static CRT libraries provide the __vcrt_initialize/__acrt_initialize
  symbols that the DllMain calls.
  
  ## Reproducer
  
  test_dll_init.c is a minimal C program that loads ghostty.dll via
  LoadLibraryA and calls ghostty_info + ghostty_init. Before the fix,
  ghostty_init crashed. After the fix, it returns 0. We can keep it or
  remove it, thoughts?
  
  ## What would be nice upstream (in Zig)
  
  Zig's _DllMainCRTStartup in start.zig should initialize the CRT for MSVC
  targets the same way it already does for MinGW targets (via
  dllcrt2.obj/crtdll.c). Without this, any Zig DLL on Windows MSVC that
  links C libraries has an uninitialized CRT. No upstream issue tracks
  this exact gap as of 2026-03-26. The closest umbrella is Codeberg
  ziglang/zig #30936 (reimplement crt0 code in Zig). I let Claude scan on
  both github and CodeBerg.
  
  ## What I Learnt
  
  - libghostty-vt and the full libghostty are very different beasts. The
  VT library is pure Zig with no C dependencies. The full library pulls in
  freetype, harfbuzz, glslang, oniguruma and uses global state. Windows
  DLL loading is greenfield basically.
  - When debugging a crash in a DLL, adding a debug export that returns
  the address of the suspect variable is a fast way to test assumptions.
  We thought `state` was at address 0 but it was fine. The null pointer
  was deeper in the init chain.
  - Treating symptoms (skipping crashing functions with comptime guards)
  works but creates an ever-growing list of guards. Finding the root cause
  (CRT not initialized) fixes all of them at once.
  - Zig's start.zig handles MinGW and MSVC DLL entry points differently.
  MinGW gets proper CRT init via dllcrt2.obj. MSVC gets nothing. As of
  today at least.
  - `@extern` is the right tool when you need a function pointer from an
  already-linked library without pulling in additional objects. `extern
  "c"` can drag in CRT objects that conflict with Zig's own symbols.
  - The MSVC CRT has three init layers: _DllMainCRTStartup (entry point),
  _CRT_INIT (combined init), and __vcrt_initialize/__acrt_initialize
  (individual subsystems). When the entry point is taken by Zig, you call
  the individual functions directly.
  
  ## Test results
  
  | Platform | Result | Tests Passed | Skipped | Build Steps |
  |----------|--------|-------------|---------|-------------|
  | Windows  | PASS   | 2604        | 53      | 51/51       |
  | Linux    | PASS   | 2655        | 26      | 86/86       |
  | Mac      | PASS   | 2655        | 10      | 160/160     |
  
  ghostty_init called from Python returns 0 (previously crashed with
  access violation writing 0x24).
  C reproducer test_dll_init.c exits 0 after ghostty_info succeeds.
  These used to crash before the fix/workaround.
  ```

## March 26, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23618497701), [2](https://github.com/ghostty-org/ghostty/actions/runs/23612257629), [3](https://github.com/ghostty-org/ghostty/actions/runs/23608022682), [4](https://github.com/ghostty-org/ghostty/actions/runs/23599836514), [5](https://github.com/ghostty-org/ghostty/actions/runs/23575850088)  
Summary: 5 runs • 15 commits • 1 authors

### Changes

- [`7801e97`](https://github.com/ghostty-org/ghostty/commit/7801e97127d3b1795b0d72cb721aba48c0fa2c16) terminal: redo trailing state capture in OSC parser ([@mitchellh](https://github.com/mitchellh))
  ```text
  Trailing state capture now is encapsulated in a struct `Capture` and all
  parsers access the data via `p.capture.trailing()` rather than directly
  from the writer.
  
  This is primarily to prep for the OSC parser to be able to capture the
  entire sequence (not just the trailing part) so we can setup libghostty
  for fallback handlers so libghostty implementers can have custom OSC
  behaviors.
  
  But, it has the benefit of making our OSC parser much cleaner too.
  ```
- [`6057f8d`](https://github.com/ghostty-org/ghostty/commit/6057f8d2b75631937fa7c2fc240a8bbe9137176f) terminal: redo trailing state capture in OSC parser ([#11873](https://github.com/ghostty-org/ghostty/issues/11873)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Trailing state capture now is encapsulated in a struct `Capture` and all
  parsers access the data via `p.capture.trailing()` rather than directly
  from the writer.
  
  This is primarily to prep for the OSC parser to be able to capture the
  entire sequence (not just the trailing part) so we can setup libghostty
  for fallback handlers so libghostty implementers can have custom OSC
  behaviors.
  
  But, it has the benefit of making our OSC parser much cleaner too.
  
  I'm doing some benchmarks now...
  ```
- [`11574c3`](https://github.com/ghostty-org/ghostty/commit/11574c35a246100aa5d5fec2a2fb835e8d18e046) libghostty: expose paste encode to C API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add ghostty_paste_encode() which encodes paste data for writing to
  the terminal pty. It strips unsafe control bytes, wraps in bracketed
  paste sequences when requested, and replaces newlines with carriage
  returns for unbracketed mode. The input buffer is modified in place
  and the encoded result is written to a caller-provided output buffer,
  following the same buffer/out_written pattern as the other encode
  functions like ghostty_size_report_encode.
  
  Update the c-vt-paste example with an encode_example() demonstrating
  the new function and add corresponding @snippet references in the
  header documentation.
  ```
- [`7df353a`](https://github.com/ghostty-org/ghostty/commit/7df353a6199ae5ac2f515006b2e5d074a31ab4c8) libghostty: expose paste encode to C API ([#11871](https://github.com/ghostty-org/ghostty/issues/11871)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add ghostty_paste_encode() which encodes paste data for writing to the
  terminal pty. It strips unsafe control bytes, wraps in bracketed paste
  sequences when requested, and replaces newlines with carriage returns
  for unbracketed mode. The input buffer is modified in place and the
  encoded result is written to a caller-provided output buffer, following
  the same buffer/out_written pattern as the other encode functions like
  ghostty_size_report_encode.
  
  Update the c-vt-paste example with an encode_example() demonstrating the
  new function and add corresponding @snippet references in the header
  documentation.
  
  Extracted this from #11870 since I can't figure out why that build is
  failing.
  ```
- [`945920a`](https://github.com/ghostty-org/ghostty/commit/945920a1863fc05079b331fdc2f914ad122cd81d) vt: expose terminal default colors via C API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add set/get support for foreground, background, cursor, and palette
  default colors through ghostty_terminal_set and ghostty_terminal_get.
  
  Four new set options (COLOR_FOREGROUND, COLOR_BACKGROUND, COLOR_CURSOR,
  COLOR_PALETTE) write directly to the terminal color defaults. Passing
  NULL clears the value for RGB colors or resets the palette to the
  built-in default. All set operations mark the palette dirty flag for
  the renderer.
  
  Eight new get data types retrieve either the effective color (override
  or default, via DynamicRGB.get) or the default color only (ignoring
  any OSC overrides). Effective getters for RGB colors return the new
  NO_VALUE result code when no color is configured. The palette getters
  return the current or original palette respectively.
  
  Adds the GHOSTTY_NO_VALUE result code for cases where a queried value
  is simply not configured, distinct from GHOSTTY_INVALID_VALUE which
  indicates a caller error.
  ```
- [`6ebbd47`](https://github.com/ghostty-org/ghostty/commit/6ebbd4785bfca5d539d7afbe97177bd592f10573) libghostty: expose terminal default colors via C API ([#11868](https://github.com/ghostty-org/ghostty/issues/11868)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Add set/get support for foreground, background, cursor, and palette
  default colors through ghostty_terminal_set and ghostty_terminal_get.
  
  Four new set options (COLOR_FOREGROUND, COLOR_BACKGROUND, COLOR_CURSOR,
  COLOR_PALETTE) write directly to the terminal color defaults. Passing
  NULL clears the value for RGB colors or resets the palette to the
  built-in default. All set operations mark the palette dirty flag for the
  renderer.
  
  Eight new get data types retrieve either the effective color (override
  or default, via DynamicRGB.get) or the default color only (ignoring any
  OSC overrides). Effective getters for RGB colors return the new NO_VALUE
  result code when no color is configured. The palette getters return the
  current or original palette respectively.
  
  Adds the GHOSTTY_NO_VALUE result code for cases where a queried value is
  simply not configured, distinct from GHOSTTY_INVALID_VALUE which
  indicates a caller error.
  
  ## Example
  
  ```c
  #include <ghostty/vt.h>
  #include <stdio.h>
  
  int main() {
    GhosttyTerminal terminal = NULL;
    GhosttyTerminalOptions opts = { .cols = 80, .rows = 24, .max_scrollback = 0 };
    ghostty_terminal_new(NULL, &terminal, opts);
  
    // Set default colors
    GhosttyColorRgb fg = { .r = 0xDD, .g = 0xDD, .b = 0xDD };
    GhosttyColorRgb bg = { .r = 0x1E, .g = 0x1E, .b = 0x2E };
    ghostty_terminal_set(terminal, GHOSTTY_TERMINAL_OPT_COLOR_FOREGROUND, &fg);
    ghostty_terminal_set(terminal, GHOSTTY_TERMINAL_OPT_COLOR_BACKGROUND, &bg);
  
    // Read back the effective foreground
    GhosttyColorRgb color;
    if (ghostty_terminal_get(terminal, GHOSTTY_TERMINAL_DATA_COLOR_FOREGROUND, &color)
        == GHOSTTY_SUCCESS) {
      printf("fg: #%02X%02X%02X\n", color.r, color.g, color.b);  // #DDDDDD
    }
  
    // After an OSC 10 override from a program inside the terminal:
    ghostty_terminal_vt_write(terminal, (const uint8_t*)"\x1B]10;rgb:FF/00/00\x1B\\", 20);
  
    // Effective returns the override, default returns the original
    ghostty_terminal_get(terminal, GHOSTTY_TERMINAL_DATA_COLOR_FOREGROUND, &color);
    printf("effective: #%02X%02X%02X\n", color.r, color.g, color.b);  // #FF0000
  
    ghostty_terminal_get(terminal, GHOSTTY_TERMINAL_DATA_COLOR_FOREGROUND_DEFAULT, &color);
    printf("default:   #%02X%02X%02X\n", color.r, color.g, color.b);  // #DDDDDD
  
    ghostty_terminal_free(terminal);
    return 0;
  }
  ```
  
  A full working example is in `example/c-vt-colors/`.
  ````
- [`7a59e96`](https://github.com/ghostty-org/ghostty/commit/7a59e966b8896065c376079d4121a9210c40e50c) build: strip large files from lib-vt dist tarball ([@mitchellh](https://github.com/mitchellh))
  ```text
  When emit_lib_vt is set, the dist tarball is now named
  ghostty-vt-<version>.tar.gz and excludes large files that are
  unnecessary for building libghostty-vt. This reduces the archive
  from ~36MB to ~2.8MB by excluding images, macOS app resources,
  font assets, fuzz test corpus, crash testdata, and vendored
  libraries not used by lib-vt.
  
  GTK resources and frame data generation are also skipped since
  lib-vt does not need them, which removes the GTK build-time
  dependency. The distcheck step runs test-lib-vt instead of the
  full test suite for lib-vt archives.
  ```
- [`7ae1e32`](https://github.com/ghostty-org/ghostty/commit/7ae1e32ecbd10d93ce0c7ddb4850a3c62a999940) ci: add libghostty-vt source tarball to tip release ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a source-tarball-lib-vt job that builds the stripped lib-vt
  dist tarball and publishes it as libghostty-vt-source.tar.gz to
  the tip release. Also downsize the source-tarball runner from -md
  to -sm since it does not need the extra resources.
  ```
- [`bfa3055`](https://github.com/ghostty-org/ghostty/commit/bfa3055309d5c292367c8ed3d876d59541a29e0c) ci: add distcheck for lib-vt source tarball ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a build-dist-lib-vt job that runs distcheck with
  -Demit-lib-vt=true and verifies the resulting tarball stays under
  5 MB. Also downsize the build-dist runner from -md to -sm.
  ```
- [`96c4145`](https://github.com/ghostty-org/ghostty/commit/96c414521a95e9c236e4ef5725fdf7f0bf7e1fe9) build: add cmake build verification to lib-vt distcheck ([@mitchellh](https://github.com/mitchellh))
  ```text
  Run cmake configure and build on the extracted lib-vt tarball as
  part of distcheck to ensure the CMake wrapper works from the
  stripped archive. Keep dist/cmake/ and dist/libghostty-vt/ in the
  archive since the CMake build needs them.
  ```
- [`4e2b227`](https://github.com/ghostty-org/ghostty/commit/4e2b227b6a81cbb80356127e198eafb19e852395) Add libghostty-vt source tarball (2.8 MB vs. 38 MB for Ghostty GUI) ([#11863](https://github.com/ghostty-org/ghostty/issues/11863)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This makes it so that `zig build dist -Demit-lib-vt` produces a
  `libghostty-vt-<version>.tar.gz` source tarball that only contains what
  is needed to build and test libghostty-vt (it cannot build Ghostty GUI
  on macOS or Linux). `distcheck` has been updated to also verify cmake
  works.
  
  The source tarball goes from 38 MB to 2.8 MB for libghostty.
  
  I also updated CI to build and test this, and also contains an assertion
  that our tarball is always less than 5 MB so we can be aware if/when we
  blow it up.
  
  The `release-tip` job was also updated to add the libghostty-vt tarball
  to our tip release on GH.
  ```
- [`4ffde26`](https://github.com/ghostty-org/ghostty/commit/4ffde268c537983c1faa44790aaacae85c094d23) ci: use namespace runners for windows jobs ([@mitchellh](https://github.com/mitchellh))
  ```text
  Switch the two Windows CI jobs (build-examples-cmake-windows and
  build-libghostty-vt-windows) from GitHub-hosted windows-2025 runners
  to namespace-profile-ghostty-windows runners.
  ```
- [`0752320`](https://github.com/ghostty-org/ghostty/commit/0752320d3bf847d5fc78f08109fa67293a87a521) ci: use namespace runners for windows jobs ([#11864](https://github.com/ghostty-org/ghostty/issues/11864)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Switch the two Windows CI jobs (build-examples-cmake-windows and
  build-libghostty-vt-windows) from GitHub-hosted windows-2025 runners to
  namespace-profile-ghostty-windows runners.
  ```
- [`312ba7a`](https://github.com/ghostty-org/ghostty/commit/312ba7ac80dea8c9a4562c41ead6d25375953e89) ci: update to Xcode 26.3 ([@mitchellh](https://github.com/mitchellh))
  ```text
  **WARNING:** We CANNOT upgrade to Xcode 26.4 with Zig 0.15 because:
  https://codeberg.org/ziglang/zig/issues/31658
  
  We have to wait and see if Zig will backport that or if we just have to
  roll forward to Zig 0.16 when it comes out. At the time of this commit,
  no released Zig version has the fix for that issue.
  ```
- [`b839561`](https://github.com/ghostty-org/ghostty/commit/b839561e5db36589d6a999044c76bfe785a013d7) ci: update to Xcode 26.3 ([#11853](https://github.com/ghostty-org/ghostty/issues/11853)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  **WARNING:** We CANNOT upgrade to Xcode 26.4 with Zig 0.15 because:
  https://codeberg.org/ziglang/zig/issues/31658
  
  We have to wait and see if Zig will backport that or if we just have to
  roll forward to Zig 0.16 when it comes out. At the time of this commit,
  no released Zig version has the fix for that issue.
  ```

## March 25, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23568447581), [2](https://github.com/ghostty-org/ghostty/actions/runs/23561957617), [3](https://github.com/ghostty-org/ghostty/actions/runs/23558342110), [4](https://github.com/ghostty-org/ghostty/actions/runs/23557158381), [5](https://github.com/ghostty-org/ghostty/actions/runs/23550813743)  
Summary: 5 runs • 15 commits • 6 authors

### Changes

- [`efc0e41`](https://github.com/ghostty-org/ghostty/commit/efc0e4118a39f2d8364a02053b5a9a8e4118dcec) Update VOUCHED list ([#11847](https://github.com/ghostty-org/ghostty/issues/11847)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11669#discussioncomment-16318770)
  from @jcollie.
  
  Vouch: @brianc442
  ```
- [`62aeabd`](https://github.com/ghostty-org/ghostty/commit/62aeabdc851f7b264721df2dea5527b9aec5788c) build: make sure CMake can clean up after libghostty-vt ([@paaloeye](https://github.com/paaloeye))
- [`c5bb97b`](https://github.com/ghostty-org/ghostty/commit/c5bb97bcbda89ffb9e715a41727dcd61bdd70dd3) build: fix libghostty shared lib install for Windows ([@deblasis](https://github.com/deblasis))
  ```text
  On Windows, install as ghostty.dll + ghostty-static.lib instead of
  libghostty.so + libghostty.a, following Windows naming conventions.
  Guard ubsan_rt bundling in initStatic for MSVC compatibility.
  ```
- [`d8e8697`](https://github.com/ghostty-org/ghostty/commit/d8e8697badc2f0170c5d3e3e5b03e36cf0b09926) build: make sure CMake can clean up after libghostty-vt ([#11845](https://github.com/ghostty-org/ghostty/issues/11845)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Fixes `cmake --build build --target clean`
  
  Currently:
  
  ```
  [1/1] Cleaning all built files...
  FAILED: clean
  ninja  -t clean
  Cleaning... ninja: error: remove(_deps/ghostty-src/zig-out/lib): Directory not empty
  ninja: error: remove(/...ghostling/build/_deps/ghostty-src/zig-out/lib): Directory not empty
  33 files.
  ninja: build stopped: subcommand failed.
  ```
  ````
- [`2655aa4`](https://github.com/ghostty-org/ghostty/commit/2655aa47d3fee66048c56add145a55b15e1a01ca) build: fix libghostty shared lib install for Windows ([#11840](https://github.com/ghostty-org/ghostty/issues/11840)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  ## Summary
  
  - On Windows, install the shared lib as `ghostty.dll` and the static lib
  as `ghostty-static.lib` instead of `libghostty.so` and `libghostty.a`
  - The `-static` suffix on the static lib avoids collision with the
  import lib that the DLL produces (same pattern as
  `ghostty-vt-static.lib`)
  - Guard `bundle_ubsan_rt` in `GhosttyLib.zig` `initStatic` for Windows,
  since Zig's ubsan emits `/exclude-symbols` linker directives that are
  incompatible with the MSVC linker (LNK4229). Matches the existing
  pattern in `GhosttyLibVt.zig`
  
  Also includes a cherry-pick of PR #11782 (backslash path handling) to
  keep the Windows test suite fully passing on this branch.
  
  ## Discussion
  
  - Is this better? This is me starting to question Claude's
  training/output.
  
  ```zig
  // Zig's ubsan emits /exclude-symbols linker directives that
  // are incompatible with the MSVC linker (LNK4229).
  lib.bundle_ubsan_rt = deps.config.target.result.os.tag != .windows;
  ```
  
  More concise, still preserves the comment. Not sure which is preferred
  here. The set-then-override matches `GhosttyLibVt.zig` exactly, but the
  boolean is maybe cleaner? Open to either. Curious about your preference.
  
  ## Test results
  
  Tested before/after on all three platforms:
  
  | | Windows | Linux | Mac |
  |---|---|---|---|
  | **BEFORE** (upstream/main) | FAIL (pre-existing, fixed by PR 11782) |
  PASS | PASS |
  | **AFTER** (this branch) | PASS - 51/51 steps, 2604/2657 tests, 53
  skipped | PASS | PASS |
  
  No regressions on any platform.
  
  ## What I Learnt
  
  - Zig's build system automatically generates an import `.lib` alongside
  a `.dll` on Windows, so the static lib needs a distinct name to avoid
  collision.
  - The ubsan runtime emits MSVC-incompatible linker directives
  ````
- [`26ba9bf`](https://github.com/ghostty-org/ghostty/commit/26ba9bf57947b7799ebb0dae90f797c4777c1865) Update VOUCHED list ([#11844](https://github.com/ghostty-org/ghostty/issues/11844)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11843#discussioncomment-16314609)
  from @jcollie.
  
  Vouch: @paaloeye
  ```
- [`909e733`](https://github.com/ghostty-org/ghostty/commit/909e733120672e643645605f8bfc2759a1cb4df2) windows: handle backslash paths in config value parsing ([@deblasis](https://github.com/deblasis))
  ```text
  CommaSplitter treats backslash as an escape character, which breaks
  Windows paths like C:\Users\foo since \U is not a valid escape. On
  Windows, treat backslash as a literal character outside of quoted
  strings. Inside quotes, escape sequences still work as before.
  
  The platform behavior is controlled by a single comptime constant
  (escape_outside_quotes) so the logic lives in one place. Escape-specific
  tests are skipped on Windows with SkipZigTest, and Windows-specific
  tests are added separately.
  
  Also fix Theme.parseCLI to not mistake the colon in a Windows drive
  letter (C:\...) for a light/dark theme pair separator.
  
  Note: other places in the config parsing also use colon as a delimiter
  without accounting for Windows drive letters (command.zig prefix
  parsing, keybind parsing). Those are tracked separately.
  ```
- [`d5b6857`](https://github.com/ghostty-org/ghostty/commit/d5b6857673f0c6d745503a5b28777193cc2848ec) windows: handle backslash paths in config value parsing ([#11782](https://github.com/ghostty-org/ghostty/issues/11782)) ([@jcollie](https://github.com/jcollie))
  ```text
  # What
  
  CommaSplitter treats backslash as an escape character, which breaks
  Windows paths like
  C:\Users\foo since \U is not a valid escape. On Windows, treat backslash
  as a literal character
  outside of quoted strings. Inside quotes, escape sequences still work as
  before.
  
  Also fix Theme.parseCLI to not mistake the colon in a Windows drive
  letter (C:\...) for a
  light/dark theme pair separator.
  
  # How
  
  The platform behavior is controlled by a single comptime constant at the
  top of CommaSplitter:
  
  const escape_outside_quotes = builtin.os.tag != .windows;
  
  The next() function checks this constant to decide whether backslash
  triggers escape parsing
  outside quoted strings. All behavior lives in one place.
  
  For Theme, skip colon detection at index 1 on Windows so drive letters
  are not mistaken for pair
  separators.
  
  Escape-specific tests are skipped on Windows with SkipZigTest.
  Windows-specific tests are added
  separately to cover paths, literal backslash, and
  escapes-still-work-inside-quotes.
  
  # Note
  
  There are other places in config parsing that use colon as a delimiter
  without accounting for
  Windows drive letters (command.zig prefix parsing, keybind parsing).
  Those are separate from this
   PR.
  
  # Verified
  
  - zig build test-lib-vt passes on Windows (exit 0)
  - No impact on Linux/macOS (the constant is true there, all existing
  behavior unchanged)
  
  # What I Learnt
  
  - Platform behavior should live in a single constant or struct, not
  scattered across if-else
  branches in every test. The escape_outside_quotes constant mirrors the
  pattern upstream uses with
  PageAlloc = switch(builtin.os.tag) but for a simpler boolean case.
  - Use error.SkipZigTest for tests that cannot run on a platform, never
  silent returns. This way
  the test runner reports them as skipped, not silently passed.
  - When fixing a pattern (colon as delimiter), grep the whole codebase
  for similar issues even if
  you are not fixing them all in one PR. Note them for future work.
  ```
- [`f50aa90`](https://github.com/ghostty-org/ghostty/commit/f50aa90ced49a05066fae4ee00071adb34dee6b5) terminal: add lib.zig to centralize lib target and re-exports ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously every file in the terminal package independently imported
  build_options and ../lib/main.zig, then computed the same
  lib_target constant. This was repetitive and meant each file needed
  both imports just to get the target.
  
  Introduce src/terminal/lib.zig which computes the target once and
  re-exports the commonly used lib types (Enum, TaggedUnion, Struct,
  String, checkGhosttyHEnum, structSizedFieldFits). All terminal
  package files now import lib.zig and use lib.target instead of the
  local lib_target constant, removing the per-file boilerplate.
  ```
- [`2f2f003`](https://github.com/ghostty-org/ghostty/commit/2f2f003aa5f807f2b5b3b3be5f83f46fa9825fce) terminal/c: use lib.calling_conv to allow Zig calling conv ([@mitchellh](https://github.com/mitchellh))
- [`3c9c3a4`](https://github.com/ghostty-org/ghostty/commit/3c9c3a4f54f3c01e3b28fe63d5797bb3334c8e18) terminal/c: use lib.alloc instead of direct lib/allocator.zig import ([@mitchellh](https://github.com/mitchellh))
  ```text
  Each C API file independently imported ../../lib/allocator.zig as
  lib_alloc. Now that terminal/lib.zig re-exports the allocator module
  as lib.alloc, use that instead. This removes the redundant import
  and keeps all lib dependencies flowing through the single lib.zig
  entry point.
  ```
- [`43f3dc5`](https://github.com/ghostty-org/ghostty/commit/43f3dc5f13d8bfb696702af4fc9b49cf7ca46d96) zsh: fix trailing '%' in PS1/PS2 combining with marks ([@jparise](https://github.com/jparise))
  ```text
  When PS1 ends with a bare '%' (e.g. `%3~ %`), concatenating our 133;B
  mark (`%{...%}`) directly after it causes zsh's prompt expansion to
  interpret the '%' + '{' result as a '%{' escape sequence. This swallows
  the 133;B mark and produces a visible '{' in the prompt.
  
  Work around this by doubling a trailing '%' into '%%' before appending
  marks, so it expands to a literal '%' and won't merge with the `%{`
  token.
  ```
- [`ac85a2f`](https://github.com/ghostty-org/ghostty/commit/ac85a2f3d621758c8302a0c6956d5ca30b833e73) terminal: always use C ABI for now ([@mitchellh](https://github.com/mitchellh))
- [`ad861d0`](https://github.com/ghostty-org/ghostty/commit/ad861d08210aca38f11f754d164581976c2f79b8) zsh: fix trailing '%' in PS1/PS2 combining with marks ([#11832](https://github.com/ghostty-org/ghostty/issues/11832)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  When PS1 ends with a bare '%' (e.g. `%3~ %`), concatenating our 133;B
  mark (`%{...%}`) directly after it causes zsh's prompt expansion to
  interpret the '%' + '{' result as a '%{' escape sequence. This swallows
  the 133;B mark and produces a visible '{' in the prompt.
  
  Work around this by doubling a trailing '%' into '%%' before appending
  marks, so it expands to a literal '%' and won't merge with the `%{`
  token.
  ```
- [`a8e65e8`](https://github.com/ghostty-org/ghostty/commit/a8e65e829af46273cf4760a2928e664e6907574a) libghostty: refactor lib calls into centralized terminal/lib.zig to prep for Zig to call C  ([#11831](https://github.com/ghostty-org/ghostty/issues/11831)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This parameterizes all our calling conventions on our C API based on
  whether we're building the C lib or Zig lib. If we're building the C
  lib, it's C calling convention, else Zig. This lets the Zig module call
  the C API via `terminal.c_api.<func>`.
  
  Zig is perfectly capable of calling C ABI but we actually modify our
  struct layouts depending on calling conv so you can't actually use the
  API prior to this. This fixes that all up.
  
  **Why would you want to do this?** The C API has some different
  semantics and stricter care about things like ABI compatibility (in how
  it changes structs and so on). It actually might be a more API-stable
  API to rely on even from Zig.
  ```

## March 24, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23513636307), [2](https://github.com/ghostty-org/ghostty/actions/runs/23512601381), [3](https://github.com/ghostty-org/ghostty/actions/runs/23510832036), [4](https://github.com/ghostty-org/ghostty/actions/runs/23503946207), [5](https://github.com/ghostty-org/ghostty/actions/runs/23492778008), [6](https://github.com/ghostty-org/ghostty/actions/runs/23472855296), [7](https://github.com/ghostty-org/ghostty/actions/runs/23469421167), [8](https://github.com/ghostty-org/ghostty/actions/runs/23468473879)  
Summary: 8 runs • 46 commits • 5 authors

### Changes

- [`c12f62c`](https://github.com/ghostty-org/ghostty/commit/c12f62c82d62f36c850a1e06221d84719948b2a4) vt: handle pixel sizes and size reports in ghostty_terminal_resize ([@mitchellh](https://github.com/mitchellh))
  ```text
  The resize function now requires cell_width_px and cell_height_px
  parameters and handles the full resize sequence: computing and
  setting width_px/height_px on the terminal, clearing synchronized output mode
  so changes display immediately, and encoding a mode 2048 in-band size report
  via the write_pty callback when that mode is enabled.
  
  A valid width/height px is critical for some applications and protocols
  and some applications rely directly on in-band size reports, so this
  change is necessary to support those use cases.
  ```
- [`bebca84`](https://github.com/ghostty-org/ghostty/commit/bebca84668947bfc92b9a30ed58712e1c34eee1d) vt: handle pixel sizes and size reports in ghostty_terminal_resize ([#11818](https://github.com/ghostty-org/ghostty/issues/11818)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The resize function now requires cell_width_px and cell_height_px
  parameters and handles the full resize sequence: computing and setting
  width_px/height_px on the terminal, clearing synchronized output mode so
  changes display immediately, and encoding a mode 2048 in-band size
  report via the write_pty callback when that mode is enabled.
  
  A valid width/height px is critical for some applications and protocols
  and some applications rely directly on in-band size reports, so this
  change is necessary to support those use cases.
  
  I do wonder if for the Zig API we should be doing this in
  `terminal.resize` or somewhere else, because as it stands this has to
  all be manually done on the Zig side.
  ```
- [`6e34bc6`](https://github.com/ghostty-org/ghostty/commit/6e34bc686cbfd86c69418fffd9805d68c197b9a7) vt: pass pointer options directly to terminal_set ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously ghostty_terminal_set required all values to be passed as
  pointers to the value, even when the value itself was already a
  pointer (userdata, function pointer callbacks). This forced callers
  into awkward patterns like compound literals or intermediate
  variables just to take the address of a pointer.
  
  Now pointer-typed options (userdata and all callbacks) are passed
  directly as the value parameter. Only non-pointer types like
  GhosttyString still require a pointer to the value. This
  simplifies InType to return the actual stored type for each option
  and lets setTyped work with those types directly.
  ```
- [`a062c16`](https://github.com/ghostty-org/ghostty/commit/a062c16e13f389bae01f0e654fddf4a133748856) libghostty: pass pointer options directly to terminal_set ([#11816](https://github.com/ghostty-org/ghostty/issues/11816)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously ghostty_terminal_set required all values to be passed as
  pointers to the value, even when the value itself was already a pointer
  (userdata, function pointer callbacks). This forced callers into awkward
  patterns like compound literals or intermediate variables just to take
  the address of a pointer.
  
  Now pointer-typed options (userdata and all callbacks) are passed
  directly as the value parameter. Only non-pointer types like
  GhosttyString still require a pointer to the value. This simplifies
  InType to return the actual stored type for each option and lets
  setTyped work with those types directly.
  ```
- [`2c16c9e`](https://github.com/ghostty-org/ghostty/commit/2c16c9e40c8862342ea02a9f3ffae2a52c3735e3) vt: add total_rows and scrollback_rows to terminal get API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add total_rows and scrollback_rows as new TerminalData variants
  queryable through the existing ghostty_terminal_get interface,
  using the cached O(1) total_rows field from PageList rather than
  introducing standalone functions.
  ```
- [`f452087`](https://github.com/ghostty-org/ghostty/commit/f452087eacde1efcbf1d845a02ccd23e73a0492e) vt: add total_rows and scrollback_rows to terminal get API ([#11817](https://github.com/ghostty-org/ghostty/issues/11817)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add total_rows and scrollback_rows as new TerminalData variants
  queryable through the existing ghostty_terminal_get interface, using the
  cached O(1) total_rows field from PageList rather than introducing
  standalone functions.
  ```
- [`68378a0`](https://github.com/ghostty-org/ghostty/commit/68378a0bb8a6e84e568838bfe5b1f92941c2ef50) build: increase comptime branch quota for ghostty.h enum checks ([@deblasis](https://github.com/deblasis))
  ```text
  The MSVC translate-c output includes Windows SDK declarations,
  bringing the total to ~2173 declarations (vs ~1502 on Linux/Mac).
  The nested inline for in checkGhosttyHEnum (enum fields x declarations)
  exceeds the 1M comptime branch quota for larger enums like MouseShape
  (34 variants). Increase to 10M to accommodate.
  ```
- [`b91cc86`](https://github.com/ghostty-org/ghostty/commit/b91cc867a815f1d26bd5b34d17b70b64abff88d1) vt: add ghostty_terminal_set for configuring effects callbacks ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a typed option setter ghostty_terminal_set() following the
  existing setopt pattern used by the key encoder and render state
  APIs. This is the first step toward exposing stream_terminal
  Handler.Effects through the C API.
  
  The initial implementation includes a write_pty callback and a
  shared userdata pointer. The write_pty callback is invoked
  synchronously during ghostty_terminal_vt_write() when the terminal
  needs to send a response back to the pty, such as DECRQM mode
  reports or device status responses.
  
  Trampolines are always installed at terminal creation time and
  no-op when no C callback is set, so callers can configure
  callbacks at any point without reinitializing the stream. The C
  callback state is grouped into an internal Effects struct on the
  TerminalWrapper to simplify adding more callbacks in the future.
  ```
- [`b49e9f3`](https://github.com/ghostty-org/ghostty/commit/b49e9f37ff71cc007dafa592c5d7385d70a2dab1) vt: add bell effect callback and move types into Effects ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add GHOSTTY_TERMINAL_OPT_BELL so C consumers can receive bell
  notifications during VT processing. The bell trampoline follows
  the same pattern as write_pty.
  
  Move the C function pointer typedefs (WritePtyFn, BellFn) into
  the Effects struct namespace to keep callback types co-located
  with their storage and trampolines.
  ```
- [`c13a9bb`](https://github.com/ghostty-org/ghostty/commit/c13a9bb49ced768d7da3f6aff2e6d31fbed4641e) vt: add tests for write_pty and bell effect callbacks ([@mitchellh](https://github.com/mitchellh))
  ```text
  Test that the write_pty callback receives correct DECRQM response
  data and userdata, that queries are silently ignored without a
  callback, and that setting null clears the callback. Test that
  the bell callback fires on single and multiple BEL characters
  with correct userdata, and that BEL without a callback is safe.
  ```
- [`f9c34b4`](https://github.com/ghostty-org/ghostty/commit/f9c34b40f067cb40d63ce78aac00ead3ec77fabb) vt: add enquiry and xtversion effect callbacks ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add GHOSTTY_TERMINAL_OPT_ENQUIRY and GHOSTTY_TERMINAL_OPT_XTVERSION
  so C consumers can respond to ENQ (0x05) and XTVERSION (CSI > q)
  queries. Both callbacks return a GhosttyString rather than using
  out-pointers.
  
  Introduce GhosttyString in types.h as a borrowed byte string
  (ptr + len) backed by lib.String on the Zig side. This will be
  reusable for future callbacks that need to return string data.
  
  Without an xtversion callback the trampoline returns an empty
  string, which causes the handler to report the default
  "libghostty" version. Without an enquiry callback no response
  is sent.
  ```
- [`6f18d44`](https://github.com/ghostty-org/ghostty/commit/6f18d44ed69a5194a74ab72b6d86aaaf545f1dd6) vt: add title_changed effect callback ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add GHOSTTY_TERMINAL_OPT_TITLE_CHANGED so C consumers are notified
  when the terminal title changes via OSC 0 or OSC 2 sequences. The
  callback has the same fire-and-forget shape as bell.
  ```
- [`424e9b5`](https://github.com/ghostty-org/ghostty/commit/424e9b57cabb1e6040167df561e03335cb2714df) vt: add size effect callback for XTWINOPS queries ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add GHOSTTY_TERMINAL_OPT_SIZE so C consumers can respond to
  XTWINOPS size queries (CSI 14/16/18 t). The callback receives a
  GhosttySizeReportSize out-pointer and returns true if the size is
  available, or false to silently ignore the query. The trampoline
  converts the bool + out-pointer pattern to the optional that the
  Zig handler expects.
  ```
- [`02d48c3`](https://github.com/ghostty-org/ghostty/commit/02d48c360b5c9e837844bac4ad3fdf6c8fa69b5c) vt: expose color_scheme effect callback ([@mitchellh](https://github.com/mitchellh))
  ```text
  Change device_status.ColorScheme from a plain Zig enum to
  lib.Enum so it uses c_int backing when targeting the C ABI.
  
  Add a color_scheme callback to the C terminal effects, following
  the bool + out-pointer pattern used by the size callback. The
  trampoline converts between the C calling convention and the
  internal stream handler color_scheme effect, returning null when
  no callback is set.
  
  Add device_status.h header with GhosttyColorScheme enum and wire
  it through terminal.h as GHOSTTY_TERMINAL_OPT_COLOR_SCHEME (= 7)
  with GhosttyTerminalColorSchemeFn.
  ```
- [`b8fcb57`](https://github.com/ghostty-org/ghostty/commit/b8fcb57923ae3a5d39630650a05217f3536c87f8) vt: expose device_attributes effect in the C API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Rename device_status.h to device.h and add C-compatible structs for
  device attributes (DA1/DA2/DA3) responses. The new header includes
  defines for all known conformance levels, DA1 feature codes, and DA2
  device type identifiers.
  
  Add a GhosttyTerminalDeviceAttributesFn callback that C consumers can
  set via GHOSTTY_TERMINAL_OPT_DEVICE_ATTRIBUTES. The callback follows
  the existing bool + out-pointer pattern used by color_scheme and size
  callbacks. When the callback is unset or returns false, the trampoline
  returns a default VT220 response (conformance level 62, ANSI color).
  
  The DA1 primary features use a fixed [64]uint16_t inline array with a
  num_features count rather than a pointer, so the entire struct is
  value-typed and can be safely copied without lifetime concerns.
  ```
- [`bbfe1c2`](https://github.com/ghostty-org/ghostty/commit/bbfe1c278722c54ededd474b9567b58fd3ad801a) vt: use struct literal for handler effects assignment ([@mitchellh](https://github.com/mitchellh))
  ```text
  Assign handler.effects as a struct literal instead of setting fields
  individually. This lets the compiler catch missing fields if new
  effects are added to the Effects struct.
  
  Also sort the callback function typedefs in vt/terminal.h
  alphabetically (Bell, ColorScheme, DeviceAttributes, Enquiry, Size,
  TitleChanged, WritePty, Xtversion).
  ```
- [`4128e6a`](https://github.com/ghostty-org/ghostty/commit/4128e6a38c5c5c20d5119a46c691bf978b74c41a) vt: add effects documentation section with example ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a comprehensive "Effects" section to the terminal module
  documentation in terminal.h explaining the callback system that
  lets embedding applications react to terminal-initiated events
  (bell, title changes, pty writes, device queries, etc.). The
  section includes a reference table of all available effects and
  their triggers, plus @snippet references to the new example.
  
  Add c-vt-effects example project demonstrating how to register
  write_pty, bell, and title_changed callbacks, attach userdata,
  and feed VT data that triggers each effect.
  ```
- [`e36b745`](https://github.com/ghostty-org/ghostty/commit/e36b7453146099b3473b4d8a5c6638f6431448c4) fmt ([@mitchellh](https://github.com/mitchellh))
- [`d2c6a3c`](https://github.com/ghostty-org/ghostty/commit/d2c6a3c775bc6952480442fe11ec2984a86b5c8c) vt: store DA1 feature buffer in wrapper struct ([@mitchellh](https://github.com/mitchellh))
  ```text
  The DA1 trampoline was converting C feature codes into a local
  stack buffer and returning a slice pointing into it. This is
  unsound because the slice outlives the stack frame once the
  trampoline returns, leaving reportDeviceAttributes reading
  invalid memory.
  
  Move the scratch buffer into the wrapper effects struct so that
  its lifetime extends beyond the trampoline call, keeping the
  returned slice valid for the caller.
  ```
- [`81e21e4`](https://github.com/ghostty-org/ghostty/commit/81e21e4d0a4e6f3a12004542a907c55c2f3b587a) build: refactor checkGhosttyHEnum to use @hasDecl instead of nested inline for ([@deblasis](https://github.com/deblasis))
  ```text
  Replace the O(N×M) nested inline for loop with direct @hasDecl lookups.
  The old approach iterated over all translate-c declarations for each enum
  field, which required a 10M comptime branch quota on MSVC (2173 decls ×
  138 fields × ~20 branches). The new approach constructs the expected
  declaration name and checks directly, reducing to O(N) and needing only
  100K quota on all platforms.
  ```
- [`d5bd331`](https://github.com/ghostty-org/ghostty/commit/d5bd331c91b9cf988f805f0f71ecc74a287d04cb) libghostty: C API for terminal "effects" for processing output and side effects ([#11814](https://github.com/ghostty-org/ghostty/issues/11814)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This adds the terminal effects callback system to the libghostty-vt C
  API.
  
  Previously, `ghostty_terminal_vt_write()` silently ignored VT sequences
  that produce side effects or require responses (bell, title changes,
  device status queries, etc.). With this change, embedders can register
  callbacks via `ghostty_terminal_set()` to handle these sequences.
  
  This has already existed in the Zig API.
  
  ## Effects
  
  | Option | Callback Type | Trigger |
  |--------|--------------|---------|
  | `GHOSTTY_TERMINAL_OPT_WRITE_PTY` | `GhosttyTerminalWritePtyFn` | Query
  responses written back to the pty |
  | `GHOSTTY_TERMINAL_OPT_BELL` | `GhosttyTerminalBellFn` | BEL character
  (0x07) |
  | `GHOSTTY_TERMINAL_OPT_TITLE_CHANGED` | `GhosttyTerminalTitleChangedFn`
  | Title change via OSC 0 / OSC 2 |
  | `GHOSTTY_TERMINAL_OPT_ENQUIRY` | `GhosttyTerminalEnquiryFn` | ENQ
  character (0x05) |
  | `GHOSTTY_TERMINAL_OPT_XTVERSION` | `GhosttyTerminalXtversionFn` |
  XTVERSION query (CSI > q) |
  | `GHOSTTY_TERMINAL_OPT_SIZE` | `GhosttyTerminalSizeFn` | XTWINOPS size
  query (CSI 14/16/18 t) |
  | `GHOSTTY_TERMINAL_OPT_COLOR_SCHEME` | `GhosttyTerminalColorSchemeFn` |
  Color scheme query (CSI ? 996 n) |
  | `GHOSTTY_TERMINAL_OPT_DEVICE_ATTRIBUTES` |
  `GhosttyTerminalDeviceAttributesFn` | Device attributes query (CSI c / >
  c / = c) |
  
  ## Example
  
  ```c
  #include <stdio.h>
  #include <string.h>
  #include <ghostty/vt.h>
  
  void on_write_pty(GhosttyTerminal terminal, void* userdata,
                    const uint8_t* data, size_t len) {
    (void)terminal; (void)userdata;
    printf("  write_pty (%zu bytes): ", len);
    fwrite(data, 1, len, stdout);
    printf("\n");
  }
  
  void on_bell(GhosttyTerminal terminal, void* userdata) {
    (void)terminal;
    int* count = (int*)userdata;
    (*count)++;
    printf("  bell! (count=%d)\n", *count);
  }
  
  int main() {
    GhosttyTerminal terminal = NULL;
    GhosttyTerminalOptions opts = { .cols = 80, .rows = 24, .max_scrollback = 0 };
    if (ghostty_terminal_new(NULL, &terminal, opts) != GHOSTTY_SUCCESS)
      return 1;
  
    // Attach userdata and callbacks
    int bell_count = 0;
    void* ud = &bell_count;
    ghostty_terminal_set(terminal, GHOSTTY_TERMINAL_OPT_USERDATA, &ud);
  
    GhosttyTerminalWritePtyFn write_fn = on_write_pty;
    ghostty_terminal_set(terminal, GHOSTTY_TERMINAL_OPT_WRITE_PTY, &write_fn);
  
    GhosttyTerminalBellFn bell_fn = on_bell;
    ghostty_terminal_set(terminal, GHOSTTY_TERMINAL_OPT_BELL, &bell_fn);
  
    // BEL triggers the bell callback
    const uint8_t bel = 0x07;
    ghostty_terminal_vt_write(terminal, &bel, 1);
  
    // DECRQM triggers write_pty with the mode response
    const char* decrqm = "\x1B[?7$p";
    ghostty_terminal_vt_write(terminal, (const uint8_t*)decrqm, strlen(decrqm));
  
    ghostty_terminal_free(terminal);
    return 0;
  }
  ```
  ````
- [`f21455b`](https://github.com/ghostty-org/ghostty/commit/f21455b7e7f1a765a93ce86530723667a4926535) build: refactor checkGhosttyHEnum to use @hasDecl for Windows compatibility ([#11813](https://github.com/ghostty-org/ghostty/issues/11813)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ### This is it! This one (and the other stacked PRs) and #11782 should
  finally give a clean test run on Windows!
  
  
  ## Summary
  
  - Increase `@setEvalBranchQuota` from 1M to 10M (too much? how much is
  too much?) in `checkGhosttyHEnum` (src/lib/enum.zig)
  - Fixes the only remaining test failure on Windows MSVC: `ghostty.h
  MouseShape`
  
  ## Context
  This one was fun! Claude started blabbering, diminishing returns it
  said. It couldn't figure out. So I called Dario and it worked.
  Nah, much easier than that.
  
  On MSVC, the translate-c output for `ghostty.h` is ~360KB with ~2173
  declarations (vs ~112KB / ~1502 on Linux/Mac) because `<sys/types.h>`
  and `<BaseTsd.h>` pull in Windows SDK headers. The `checkGhosttyHEnum`
  function uses a nested `inline for` (enum fields x declarations) with
  comptime string comparisons. For MouseShape (34 variants), this
  generates roughly 34 x 2173 x ~20 = ~1.5M comptime branches, exceeding
  the 1M quota.
  
  The failure was confusing because it presented as a runtime error
  ("ghostty.h is missing value for GHOSTTY_MOUSE_SHAPE_DEFAULT") rather
  than a compile error. The constants exist in the translate-c output and
  the test compiles, but the comptime loop silently stops matching when it
  hits the branch limit, so `set.remove` is never called and the set
  reports all entries as missing at runtime.
  
  ## How we found it
  The translate-c output clearly had all 34 GHOSTTY_MOUSE_SHAPE_*
  constants, yet the test reported all of them as missing. I asked Claude
  to list 5 hypotheses (decl truncation, branch quota, string comparison
  bug, declaration ordering, field access failure) and to write 7 targeted
  POC tests in enum.zig to isolate each step of `checkGhosttyHEnum`:
  
  1. POC1-2: Module access and declaration count (both passed)
  2. POC3: `@hasDecl` for the constant (passed)
  3. POC4: Direct field value access (passed)
  4. POC5: `inline for` over decls with string comparison - **compile
  error: "evaluation exceeded 1000 backwards branches"**
  5. POC6: Same but with 10M quota (passed)
  6. POC7: Full `checkGhosttyHEnum` clone with 10M quota - **passed,
  confirming the fix**
  
  POC5 was the key: the default 1000 branch limit for test code confirmed
  the comptime budget mechanism. The existing 1M quota in
  `checkGhosttyHEnum` was enough for Linux/Mac (1502 declarations) but not
  for MSVC (2173 declarations) with larger enums.
  
  ## Stack
  Stacked on 016-windows/fix-libcxx-msvc.
  
  ## Test plan
  
  ### Cross-platform results (`zig build test` / `zig build
  -Dapp-runtime=none test` on Windows)
  
  | | Windows | Linux | Mac |
  |---|---|---|---|
  | **BEFORE** (016, ce9930051) | FAIL - 49/51, 2630/2654, 1 test failed,
  23 skipped | PASS - 86/86, 2655/2678, 23 skipped | PASS - 160/160,
  2655/2662, 7 skipped |
  | **AFTER** (017, 68378a0bb) | FAIL - 49/51, 2631/2654, 23 skipped |
  PASS - 86/86, 2655/2678, 23 skipped | PASS - 160/160, 2655/2662, 7
  skipped |
  
  ### Windows: what changed (2630 -> 2631 tests, MouseShape fixed)
  
  **Fixed by this PR:**
  - `ghostty.h MouseShape` test - was failing because comptime branch
  quota exhaustion silently prevented the inline for loop from matching
  any constants
  
  **Remaining failure (pre-existing, unrelated):**
  - `config.Config.test.clone can then change conditional state` -
  segfaults (exit code 3) on Windows. We investigated this and it looked
  familiar.. cherry-picking the `CommaSplitter `fix from PR #11782
  resolved it! The backslash path handling in `CommaSplitter `breaks theme
  path parsing on Windows, which is exactly what that PR addresses. So
  once that lands, we should be in a good place... ready to ship to
  Windows users! (just kidding)
  
  ### Linux/macOS: no regressions
  Identical pass counts and test results before and after.
  
  ## What I Learnt
  - Comptime branch quota exhaustion in Zig does not always surface as a
  clean compile error. When it happens inside an `inline for` loop with
  `comptime` string comparisons that gate runtime code (like
  `set.remove`), the effect is that matching code is silently not
  generated. The test compiles and runs, but the runtime behavior is wrong
  because the matching branches were never emitted. This makes the failure
  look like a data issue (missing declarations) rather than a compile
  budget issue.
  - When debugging comptime issues, writing small isolated POC tests that
  exercise each step of the failing function independently is very
  effective. It took 7 targeted tests to pinpoint the exact failure point.
  - Cross-platform translate-c outputs can vary significantly in size. On
  MSVC, system headers are much larger than on Linux/Mac, which affects
  comptime budgets for any code that iterates over translated module
  declarations.
  ```
- [`8f1ac0b`](https://github.com/ghostty-org/ghostty/commit/8f1ac0bd4e69e922167d4cf7560a6cdec12ba721) vt: expose title and pwd in C API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add title and pwd as both gettable data keys
  (GHOSTTY_TERMINAL_DATA_TITLE/PWD) and settable options
  (GHOSTTY_TERMINAL_OPT_TITLE/PWD) in the C terminal API. Getting
  returns a borrowed GhosttyString; setting copies the data into the
  terminal via setTitle/setPwd.
  
  The underlying Terminal.setTitle/setPwd now append a null sentinel so
  that getTitle/getPwd can return sentinel-terminated slices ([:0]const
  u8), which is useful for downstream consumers that need C strings.
  
  Change ghostty_terminal_set to return GhosttyResult instead of void
  so that the new title/pwd options can report allocation failures.
  Existing option-setting calls cannot fail so the return value is
  backwards-compatible for callers that discard it.
  ```
- [`82f7527`](https://github.com/ghostty-org/ghostty/commit/82f7527b302a655ed03be0f6f1f0d46f5aaadcb0) vt: expose title and pwd in C API ([#11815](https://github.com/ghostty-org/ghostty/issues/11815)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add title and pwd as both gettable data keys
  (GHOSTTY_TERMINAL_DATA_TITLE/PWD) and settable options
  (GHOSTTY_TERMINAL_OPT_TITLE/PWD) in the C terminal API. Getting returns
  a borrowed GhosttyString; setting copies the data into the terminal via
  setTitle/setPwd.
  
  The underlying Terminal.setTitle/setPwd now append a null sentinel so
  that getTitle/getPwd can return sentinel-terminated slices ([:0]const
  u8), which is useful for downstream consumers that need C strings.
  
  Change ghostty_terminal_set to return GhosttyResult instead of void so
  that the new title/pwd options can report allocation failures. Existing
  option-setting calls cannot fail so the return value is
  backwards-compatible for callers that discard it.
  ```
- [`d5aef6e`](https://github.com/ghostty-org/ghostty/commit/d5aef6e845ed72584aba3a129268d40a9694b568) build: fix freetype compilation on Windows with MSVC ([@deblasis](https://github.com/deblasis))
  ```text
  Gate HAVE_UNISTD_H and HAVE_FCNTL_H behind a non-Windows check since
  these headers do not exist with MSVC. Freetype includes zlib headers
  which conditionally include unistd.h based on this define.
  ```
- [`a35f84d`](https://github.com/ghostty-org/ghostty/commit/a35f84db32e88b93bcff19317365ee93f75839d1) build: define ssize_t for MSVC in ghostty.h ([@deblasis](https://github.com/deblasis))
  ```text
  MSVC's <sys/types.h> does not define ssize_t (it is a POSIX type).
  This causes the translate-c build step to fail when translating
  ghostty.h on Windows. Use SSIZE_T from <BaseTsd.h> which is the
  Windows SDK equivalent.
  ```
- [`deeda46`](https://github.com/ghostty-org/ghostty/commit/deeda4618691525e977886135aa4ff18b7f81caa) build: skip linkLibCpp on MSVC for dcimgui, spirv-cross, harfbuzz ([@deblasis](https://github.com/deblasis))
  ```text
  Zig unconditionally passes -nostdinc++ and adds its bundled
  libc++/libc++abi include paths, which conflict with MSVC's own C++
  runtime headers. The MSVC SDK directories (added via linkLibC)
  already contain both C and C++ headers, so linkLibCpp is not needed.
  
  This is the same fix already applied upstream to highway, simdutf,
  utfcpp, glslang, SharedDeps, and GhosttyZig.
  ```
- [`ce99300`](https://github.com/ghostty-org/ghostty/commit/ce99300513dff19fade309ca4881fc45517424f7) build: fix freetype C enum signedness for MSVC ([@deblasis](https://github.com/deblasis))
  ```text
  MSVC translates C enums as signed int, while GCC/Clang uses unsigned
  int. The freetype Zig bindings hardcode c_uint for enum backing types,
  causing type mismatches when compiling with MSVC target.
  
  Fix by adding @intCast at call sites where enum values are passed to
  C functions, and @bitCast for the glyph format tag extraction where
  bit-shift operations require unsigned integers.
  ```
- [`d14eab3`](https://github.com/ghostty-org/ghostty/commit/d14eab3124bc8ff9f3ca25b2a2bafeecf20a9133) build: fix freetype compilation on Windows with MSVC ([#11807](https://github.com/ghostty-org/ghostty/issues/11807)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Summary
  
  **Getting there!** Goal for today/tomorrow is to get it all green.
  
  This one is easy:
  
  - Gate `HAVE_UNISTD_H` and `HAVE_FCNTL_H` behind a non-Windows check
  since these headers do not exist with MSVC
  - Freetype's gzip module includes zlib headers which conditionally
  include `unistd.h` based on this define
  
  ## Context
  Same pattern as the zlib fix (010-* branch from my fork). Freetype
  passes `-DHAVE_UNISTD_H` unconditionally, which causes zlib's `zconf.h`
  to try including `unistd.h` when freetype compiles its gzip support. The
  fix follows the same approach used in `pkg/zlib/build.zig` (line 36-38).
  
  ## Stack
  Stacked on 013-windows/fix-helpgen-framegen.
  
  ## Test plan
  
  ### Cross-platform results (`zig build test` / `zig build
  -Dapp-runtime=none test` on Windows)
  
  | | Windows | Linux | Mac |
  |---|---|---|---|
  | **BEFORE** (f9d3b1aaf) | FAIL - 44/51 steps, 2 failed | PASS - 86/86,
  2655/2678 tests, 23 skipped | PASS - 160/160, 2655/2662 tests, 7 skipped
  |
  | **AFTER** (d5aef6e84) | FAIL - 47/51 steps, 1 failed | PASS - 86/86,
  2655/2678 tests, 23 skipped | PASS - 160/160, 2655/2662 tests, 7 skipped
  |
  
  ### Windows: what changed (44 to 47 steps, 2 to 1 failure)
  
  **Fixed by this PR:**
  - `compile lib freetype` - was `2 errors` (unistd.h/fcntl.h not found)
  -> `success`
  - 3 additional steps that depended on freetype now succeed
  
  **Remaining failure (pre-existing, tracked separately):**
  - `translate-c` - 3 errors (`ssize_t` unknown in ghostty.h on MSVC)
  
  ### Linux/macOS: no regressions
  Identical pass counts and test results before and after.
  
  ## Discussion
  
  ### Other build files with the same pattern
  `pkg/fontconfig/build.zig` and `pkg/harfbuzz/build.zig` also pass
  `-DHAVE_UNISTD_H` and/or `-DHAVE_FCNTL_H` unconditionally. They are not
  in the Windows build path today, but will need the same fix when they
  are.
  
  ## What I Learnt
  
  More of the same
  ```
- [`e7a23a3`](https://github.com/ghostty-org/ghostty/commit/e7a23a37e5f01ad5993447e966f19abaceebdb6b) build: define ssize_t for MSVC in ghostty.h ([#11810](https://github.com/ghostty-org/ghostty/issues/11810)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  > [!WARNING]
  > Review/approve this AFTER #11807 (this PR includes its commits)
  
  92% progress with the fixes!
  
  ## Summary
  - Add a conditional `ssize_t` typedef for MSVC in `include/ghostty.h`
  - MSVC's `<sys/types.h>` does not define `ssize_t` (it is a POSIX type),
  which causes the `translate-c` build step to fail when translating
  `ghostty.h` on Windows
  - Uses `SSIZE_T` from `<BaseTsd.h>`, the standard Windows SDK equivalent
  
  ## Context
  The `translate-c` step translates `ghostty.h` to Zig for test
  compilation. On MSVC, it fails with 3 errors on `ssize_t` (used in
  `ghostty_action_move_tab_s`, `ghostty_action_search_total_s`,
  `ghostty_action_search_selected_s`).
  
  The `#ifdef _MSC_VER` guard means this only affects MSVC builds.
  `BaseTsd.h` is a standard Windows SDK header and `SSIZE_T` is a signed
  pointer-sized integer, matching POSIX `ssize_t` and Zig's `isize`. This
  pattern is used by libuv, curl, and other cross-platform C projects.
  
  ## Test plan
  
  ### Cross-platform results (`zig build test` / `zig build
  -Dapp-runtime=none test` on Windows)
  
  | | Windows | Linux | Mac |
  |---|---|---|---|
  | **BEFORE** (d5aef6e84) | FAIL - 47/51 steps, 1 failed | PASS - 86/86,
  2655/2678 tests, 23 skipped | PASS - 160/160, 2655/2662 tests, 7 skipped
  |
  | **AFTER** (a35f84db3) | FAIL - 48/51 steps, 1 failed | PASS - 86/86,
  2655/2678 tests, 23 skipped | PASS - 160/160, 2655/2662 tests, 7 skipped
  |
  
  ### Windows: what changed (47 -> 48 steps, translate-c fixed)
  
  **Fixed by this PR:**
  - `translate-c` - was `3 errors` (unknown type name 'ssize_t' at lines
  582, 842, 847) -> `success`
  
  **Remaining failure (pre-existing, unrelated):**
  - `compile test ghostty-test` - 3 errors in libcxxabi
  (`std::get_new_handler` not found, `type_info` redefinition). This is
  Zig's bundled libc++ ABI conflicting with MSVC headers when compiling
  the test binary. It was previously masked by the translate-c failure
  blocking this step.
  
  ### Linux/macOS: no regressions
  Identical pass counts and test results before and after.
  
  ## What Have I Learnt
  - I tried fixing this issue the old way, googling and stuff, I
  eventually figured out but it took me way more than I am prepared to
  share. Yikes.
  ```
- [`7114721`](https://github.com/ghostty-org/ghostty/commit/7114721bd4323c776b4c93b0afd313c4785b98b3) build: fix C++ linking and enum signedness on MSVC ([#11812](https://github.com/ghostty-org/ghostty/issues/11812)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  > [!WARNING]
  > Review/approve this AFTER #11807 and #11810 (this PR includes their
  commits)
  
  ## Summary
  
  ### **And `run test ghostty-test` finally runs on Windows! 🎉almost
  there!**
  
  - Skip `linkLibCpp()` on MSVC for dcimgui, spirv-cross, and harfbuzz
  (same fix already applied upstream to highway, simdutf, utfcpp, glslang,
  SharedDeps, GhosttyZig)
  - Fix freetype C enum signedness: MSVC translates C enums as signed
  `int`, while GCC/Clang uses unsigned `int`. Add `@intCast` at call sites
  and `@bitCast` for bit-shift operations on glyph format tags.
  
  ## Context
  Zig unconditionally passes `-nostdinc++` and adds its bundled
  libc++/libc++abi include paths, which conflict with MSVC's own C++
  runtime headers. The MSVC SDK directories (added via `linkLibC`) already
  contain both C and C++ headers, so `linkLibCpp` is not needed.
  
  The freetype enum issue is a different facet of the same MSVC vs
  GCC/Clang divide: `FT_Render_Mode` and `FT_Glyph_Format` are C enums
  that get different signedness on different compilers.
  
  ## Stack
  Stacked on 015-windows/fix-ssize-t-msvc.
  
  ## Test plan
  
  ### Cross-platform results (`zig build test` / `zig build
  -Dapp-runtime=none test` on Windows)
  
  | | Windows | Linux | Mac |
  |---|---|---|---|
  | **BEFORE** (015, a35f84db3) | FAIL - 48/51, 1 failed (compile
  ghostty-test) | PASS - 86/86, 2655/2678, 23 skipped | PASS - 160/160,
  2655/2662, 7 skipped |
  | **AFTER** (016, ce9930051) | FAIL - 49/51, 2630/2654 tests passed, 1
  failed, 23 skipped | PASS - 86/86, 2655/2678, 23 skipped | PASS -
  160/160, 2655/2662, 7 skipped |
  
  ### Windows: what changed (48 -> 49 steps, tests now run)
  
  **Fixed by this PR:**
  - `compile test ghostty-test` - was `3 errors` (libcxxabi conflicts +
  freetype type mismatches) -> `success`
  - `run test ghostty-test` - now actually runs: 2630 passed, 23 skipped,
  1 failed
  
  **Remaining test failure (pre-existing, unrelated):**
  - `ghostty.h MouseShape` - `checkGhosttyHEnum` cannot find
  `GHOSTTY_MOUSE_SHAPE_*` constants in the translate-c output. This is a
  translate-c issue with how MSVC enum constants are exposed, not related
  to C++ linking or enum signedness.
  
  ### Linux/macOS: no regressions
  Identical pass counts and test results before and after.
  
  ## Discussion
  
  ### Grep wider: other unconditional linkLibCpp calls
  `pkg/breakpad/build.zig` still calls `linkLibCpp()` unconditionally but
  is behind sentry and not in the Windows build path. Noted for
  completeness.
  
  ### Freetype enum signedness
  The freetype Zig bindings define `RenderMode = enum(c_uint)` and
  `Encoding = enum(u31)`. On MSVC, C enums are `int` (signed), so the
  translated C functions expect `c_int` parameters. The fix adds
  `@intCast` to convert between signed and unsigned at call sites. This is
  safe because the enum values are small positive integers that fit in
  both types.
  
  Also, not sure if there's a better way to make this change more
  elegantly. The comments are replicated in each instance, probably
  overkill but I have seen this same pattern elsewhere in the codebase.
  
  ## What I Learnt
  - More of the same
  ```
- [`c5092b0`](https://github.com/ghostty-org/ghostty/commit/c5092b09ded689983b674d3d285e4796bf86f677) ci: remove continue-on-error from Windows CI jobs ([@deblasis](https://github.com/deblasis))
  ```text
  Windows tests and builds are now passing reliably. Remove the
  continue-on-error safety net so failures are visible immediately.
  ```
- [`4df71bc`](https://github.com/ghostty-org/ghostty/commit/4df71bcad75a6177b33bea33287982efadef69e8) build: fix zlib compilation on Windows with MSVC ([@deblasis](https://github.com/deblasis))
  ```text
  Gate Z_HAVE_UNISTD_H behind a non-Windows check since unistd.h does
  not exist on Windows. Add _CRT_SECURE_NO_DEPRECATE and
  _CRT_NONSTDC_NO_DEPRECATE for MSVC to suppress deprecation errors
  for standard C functions that zlib uses.
  ```
- [`014873e`](https://github.com/ghostty-org/ghostty/commit/014873e539a6183f82617234fe57ba3983a764ef) build: fix oniguruma compilation on Windows with MSVC ([@deblasis](https://github.com/deblasis))
  ```text
  Conditionally disable POSIX-only header defines (alloca.h, sys/times.h,
  sys/time.h, unistd.h) on Windows since they do not exist with MSVC.
  Enable USE_CRNL_AS_LINE_TERMINATOR on Windows for correct line endings.
  ```
- [`74c6ffe`](https://github.com/ghostty-org/ghostty/commit/74c6ffe78e4b98e58600f22f37a8433f44b53876) build: fix glslang compilation on Windows with MSVC ([@deblasis](https://github.com/deblasis))
  ```text
  Apply the same MSVC fixes used for simdutf and highway: conditionally
  skip linkLibCpp on MSVC since Zig's bundled libc++ headers conflict
  with MSVC's own C++ runtime, and add -std=c++17 for C++17 features
  like std::variant and inline variables that glslang requires.
  ```
- [`f9d3b1a`](https://github.com/ghostty-org/ghostty/commit/f9d3b1aafb4131ab8f9d9a362832ec428bf1cabc) build: fix Windows build failures in helpgen and framegen ([@deblasis](https://github.com/deblasis))
  ```text
  Use writerStreaming() instead of writer() for stdout in helpgen and
  main_build_data. The positional writer calls setEndPos/ftruncate in
  end(), which fails on Windows because ftruncate on pipes maps
  INVALID_PARAMETER to FileTooBig.
  
  Replace scandir with opendir/readdir plus qsort in framegen since
  scandir is a POSIX extension not available on Windows.
  
  This was previously applied and reverted upstream (f4998c6ab, 0fdddd5bc)
  as collateral from an unrelated example-execution hang that has since
  been resolved.
  ```
- [`6854ecc`](https://github.com/ghostty-org/ghostty/commit/6854ecc5a928b92c66d09e6b46b66ec9daf7ea23) ci: remove continue-on-error from Windows CI jobs ([#11796](https://github.com/ghostty-org/ghostty/issues/11796)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Let's see what breaks and let's fix it.
  ```
- [`58e330a`](https://github.com/ghostty-org/ghostty/commit/58e330a8c0b45d026b4c7985a95389ea905c9fed) build: fix zlib compilation on Windows with MSVC ([#11798](https://github.com/ghostty-org/ghostty/issues/11798)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Summary
  - Gate `Z_HAVE_UNISTD_H` behind a non-Windows check since `unistd.h`
  does not exist with MSVC
  - Add `_CRT_SECURE_NO_DEPRECATE` and `_CRT_NONSTDC_NO_DEPRECATE` for
  MSVC to suppress deprecation errors for standard C functions that zlib
  uses
  
  ## Context
  Part of the effort to get `zig build -Dapp-runtime=none test` passing on
  Windows. This unblocks freetype, harfbuzz, libpng, and dcimgui which all
  depend on zlib.
  
  My research shows that we should default to msvc in ci with zig build
  ran without `-Dratget`.
  
  ## Stack
  This is branch 010 in the stacked branches series (soon on Netflix).
  Independent fix, no dependencies on other branches.
  
  ## Test plan
  
  ### test-lib-vt
  
  | | Windows | Linux | Mac |
  |---|---|---|---|
  | **BEFORE** | 3791/3839 passed, 48 skipped | 3791/3839 passed, 48
  skipped | 3807/3839 passed, 32 skipped |
  | **AFTER** | 3791/3839 passed, 48 skipped | 3791/3839 passed, 48
  skipped | 3807/3839 passed, 32 skipped |
  | **Delta** | no change | no change | no change |
  
  ### all tests (`zig build test` / `zig build -Dapp-runtime=none test` on
  Windows)
  
  | | Windows | Linux | Mac |
  |---|---|---|---|
  | **BEFORE** | FAIL — 35/51 build steps, 6 failed | 2655/2678 passed, 23
  skipped (86/86 steps) | 2655/2662 passed, 7 skipped (160/160 steps) |
  | **AFTER** | FAIL — 37/51 build steps, 6 failed | 2655/2678 passed, 23
  skipped (86/86 steps) | 2655/2662 passed, 7 skipped (160/160 steps) |
  | **Delta** | +2 build steps (zlib + png unblocked) | no change | no
  change |
  
  - Zero regressions on any platform
  - Windows improved: zlib and png now compile (35 -> 37 steps)
  - Remaining 6 Windows build failures (`ssize_t`, `helpgen`, `framegen`,
  `harfbuzz`, `dcimgui`) are addressed by other PRs in the stack
  
  ## What I Learnt
  - Always run tests with `--summary all` to get actual pass/skip/fail
  counts. Without it, zig just exits 0 or 1 and you have no numbers to
  compare. "You get confident if you got the numbers."
  - Build dependencies cascade: fixing zlib also unblocked png (which
  depends on it), giving us +2 build steps from a one-file change.
  ```
- [`5cc22c2`](https://github.com/ghostty-org/ghostty/commit/5cc22c23e6a6e4346fdad2480dca04e4b05a5c88) build: fix oniguruma compilation on Windows with MSVC ([#11800](https://github.com/ghostty-org/ghostty/issues/11800)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  > [!WARNING]
  > Review/approve this AFTER #11798 (this PR stacks on top of it... ergo,
  it includes its commits)
  
  ## Summary
  - Conditionally disable POSIX-only header defines (`alloca.h`,
  `sys/times.h`, `sys/time.h`, `unistd.h`) on Windows since they do not
  exist with MSVC
  - Enable `USE_CRNL_AS_LINE_TERMINATOR` on Windows for correct line
  endings
  
  ## Context
  Oniguruma's `config.h` template had all POSIX header availability
  defines hardcoded to `true`. On MSVC, these headers don't exist, causing
  24 compilation errors (all `alloca.h` file not found).
  
  Uses a comptime `is_windows` constant to flip the config values, same
  pattern as PR #11798 (zlib).
  
  ## Stack
  Stacked on 010-windows/fix-zlib-msvc.
  
  ## Test plan
  
  ### test-lib-vt
  
  | | Windows | Linux | Mac |
  |---|---|---|---|
  | **BEFORE** | 3791/3839 passed, 48 skipped | 3791/3839 passed, 48
  skipped | 3807/3839 passed, 32 skipped |
  | **AFTER** | 3791/3839 passed, 48 skipped | 3791/3839 passed, 48
  skipped | 3807/3839 passed, 32 skipped |
  | **Delta** | no change | no change | no change |
  
  ### all tests (`zig build test` / `zig build -Dapp-runtime=none test` on
  Windows)
  
  | | Windows | Linux | Mac |
  |---|---|---|---|
  | **BEFORE** | FAIL — 37/51 steps, 6 failed | 2655/2678 passed, 23
  skipped (86/86 steps) | 2655/2662 passed, 7 skipped (160/160 steps) |
  | **AFTER** | FAIL — 38/51 steps, 5 failed | 2655/2678 passed, 23
  skipped (86/86 steps) | 2655/2662 passed, 7 skipped (160/160 steps) |
  | **Delta** | +1 step, -1 failure (oniguruma unblocked) | no change | no
  change |
  
  - Zero regressions on any platform
  - Windows improved: oniguruma now compiles (37 -> 38 steps, 6 -> 5
  failures)
  - Remaining 5 Windows failures (`translate-c`/ssize_t, `helpgen`,
  `framegen`, `glslang`, `harfbuzz` via freetype) are addressed by other
  PRs in the stack
  
  ## What I Learnt
  - comptime, man. It's the small things.
  ```
- [`57b9292`](https://github.com/ghostty-org/ghostty/commit/57b929203bde64614885133c949ef2ca1fb83b5c) build: fix glslang compilation on Windows with MSVC ([#11801](https://github.com/ghostty-org/ghostty/issues/11801)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  > [!WARNING]
  > Review/approve this AFTER #11798 and #11800 (this PR stacks on top of
  rhem... ergo, it includes their commits)
  > Don't cheat! Start from the oldest one! 😄 I know these are almost
  one-liners but I am doing this mostly for documentation and karma
  points.
  
  ## Summary
  - Conditionally skip `linkLibCpp()` on MSVC since Zig's bundled libc++
  headers conflict with MSVC's own C++ runtime
  - Add `-std=c++17` flag for C++17 features (std::variant,
  std::filesystem, inline variables) that glslang requires
  
  ## Context
  The exact same `linkLibCpp` fix was applied to `simdutf` and `highway`
  in commits 3d581eb92 and b4c529a82 but glslang was missed. Without this
  fix, glslang fails with 297 compilation errors on MSVC.
  
  Thanks Claude for the forensic digging. A carpenter should always be
  thankful for his tools. Even if they are borrowed, maybe even more so.
  
  ## Stack
  Stacked on 011-windows/fix-oniguruma-msvc.
  
  ## Discussion points
  
  **`-std=c++17` scope:** Currently added unconditionally for all targets.
  Tested on all three platforms with no regressions, but since this is
  specifically fixing a Windows/MSVC issue, it could be gated behind
  `target.result.abi == .msvc`. Donno. The reason it works unconditionally
  is that Zig's bundled clang already defaults to C++17 on non-MSVC
  targets, so the flag is a no-op there. Open to either approach.
  
  **Other packages with bare `linkLibCpp()`:** The same `linkLibCpp` guard
  has been applied to `simdutf`, `highway`, `utfcpp`, and now `glslang`.
  However, `spirv-cross`, `dcimgui`, `harfbuzz`, and `breakpad` still have
  unconditional `linkLibCpp()` calls. These may need the same treatment
  when they become buildable on MSVC (some are currently blocked by other
  issues like freetype's `unistd.h`). Worth tracking as a follow-up?
  
  ## Test plan
  
  ### test-lib-vt
  
  | | Windows | Linux | Mac |
  |---|---|---|---|
  | **BEFORE** | 3791/3839 passed, 48 skipped | 3791/3839 passed, 48
  skipped | 3807/3839 passed, 32 skipped |
  | **AFTER** | 3791/3839 passed, 48 skipped | 3791/3839 passed, 48
  skipped | 3807/3839 passed, 32 skipped |
  | **Delta** | no change | no change | no change |
  
  ### all tests (`zig build test` / `zig build -Dapp-runtime=none test` on
  Windows)
  
  | | Windows | Linux | Mac |
  |---|---|---|---|
  | **BEFORE** | FAIL — 38/51 build steps, 5 failed | 2655/2678 passed, 23
  skipped (86/86 steps) | 2655/2662 passed, 7 skipped (160/160 steps) |
  | **AFTER** | FAIL — 39/51 build steps, 4 failed | 2655/2678 passed, 23
  skipped (86/86 steps) | 2655/2662 passed, 7 skipped (160/160 steps) |
  | **Delta** | +1 build step (glslang unblocked) | no change | no change
  |
  
  - Zero regressions on any platform
  - Windows improved: glslang now compiles (38 -> 39 steps, 5 -> 4
  failures)
  - Remaining 4 Windows failures (`helpgen`, `framegen`, `freetype`,
  `translate-c`) are addressed by other PRs in the stack
  
  ## What I Learnt
  
  - **MSVC's clang doesn't default to C++17.** Zig's bundled clang uses
  C++17 by default on Linux/Mac, but when targeting MSVC, the C++ standard
  needs to be specified explicitly. Without `-std=c++17`, features like
  `std::variant`, `std::filesystem`, and `inline` variables are gated
  behind `_HAS_CXX17` and won't compile.
  - **`linkLibCpp` conflicts with MSVC headers.** Zig's `linkLibCpp`
  passes `-nostdinc++` and adds its own libc++/libc++abi headers, which
  collide with the C++ headers already provided by the MSVC SDK through
  `linkLibC`. On MSVC, you don't need `linkLibCpp` at all since the SDK
  includes both C and C++ headers. I think yesterday we dealt with
  something similar. Windows is fun. 🫠 Unironically and chronically.
  - **Grep wider.** The `linkLibCpp` guard was already applied to simdutf,
  highway, and utfcpp but missed glslang. When a fix follows a repeated
  pattern across packages, search the whole codebase before declaring it
  complete.
  ```
- [`aec3a6e`](https://github.com/ghostty-org/ghostty/commit/aec3a6ebf62eaa204f678ac2a075775012a2d3a3) build: fix Windows build failures in helpgen and framegen ([#11803](https://github.com/ghostty-org/ghostty/issues/11803)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  > [!WARNING]
  > Review/approve this AFTER #11798, #11800 and #11801 (this PR stacks on
  top of rhem... ergo, it includes their commits)
  > Don't cheat! Start from the oldest one! 😄 I know these are almost
  one-liners but I am doing this mostly for documentation and karma
  points. BTW, Github needs to level up this wankflow like a lot... IMHO
  
  ## Summary
  - Use `writerStreaming()` instead of `writer()` for stdout in helpgen
  and main_build_data (`ftruncate` on pipes fails on Windows with
  `INVALID_PARAMETER` mapped to `FileTooBig`)
  - Replace POSIX `scandir` with `opendir`/`readdir` plus `qsort` in
  framegen since `scandir` is not available on Windows
  
  ## Context
  This fix was previously applied upstream by Mitchell (f4998c6ab) and
  reverted 15 minutes later (0fdddd5bc). The reason for the revert is not
  clear. Around the same time, a CI step was added to execute cmake
  examples on Windows, which was later removed (b723f2a43) with the note
  "hangs, so remove it entirely". Whether the revert is related to the
  hang or had a separate reason, we don't know.
  
  What we do know:
  - Both `helpgen` and `framegen` run during normal builds on Windows (via
  `SharedDeps`), not just during dist packaging. Claude had told me the
  opposite before but "don't trust and verify".
  - Without this fix, both tools fail: helpgen with `FileTooBig`
  (ftruncate on pipes), framegen with `scandir` undeclared
  - The fix does not regress Linux or macOS
  
  ## Stack
  Stacked on 012-windows/fix-glslang-msvc.
  
  ## Test plan
  
  ### Cross-platform results (`zig build test` / `zig build
  -Dapp-runtime=none test` on Windows)
  
  | | Windows | Linux | Mac |
  |---|---|---|---|
  | **BEFORE** (74c6ffe78) | FAIL - 39/51 steps, 4 failed | PASS - 86/86,
  2655/2678 tests, 23 skipped | PASS - 160/160, 2655/2662 tests, 7 skipped
  |
  | **AFTER** (f9d3b1aaf) | FAIL - 44/51 steps, 2 failed | PASS - 86/86,
  2655/2678 tests, 23 skipped | PASS - 160/160, 2655/2662 tests, 7 skipped
  |
  
  ### Windows: what changed (39 > 44 steps, 4 > 2 failures)
  
  **Fixed by this PR:**
  - `run exe helpgen` -> was `failure` (FileTooBig from ftruncate on
  stdout pipe) -> `success`
  - `compile exe framegen` -> was `1 errors` (scandir undeclared) ->.
  `success`
  
  **Remaining failures (pre-existing, fixed by later PRs in stack):**
  - `translate-c` -> 3 errors (`ssize_t` unknown in ghostty.h on MSVC)
  - `compile lib freetype` -> 2 errors (`unistd.h` not found)
  
  ### Linux/macOS: no regressions
  Identical pass counts and test results before and after.
  
  ## Discussion points
  
  ### "Grep wider"  other `stdout().writer()` callsites
  There are 15+ other `stdout().writer(&buf)` callsites in the codebase.
  Build-time generators that capture stdout (webgen, mdgen, unicode
  generators) would have the same `ftruncate` issue if they ran on
  Windows. Currently they don't appear in the Windows build graph, but
  worth noting for future Windows work.
  
  ### `writerStreaming()` vs `writer()`
  `writer()` calls `ftruncate` on flush/end to set the file size, which
  fails on pipes (stdout captured by the build system).
  `writerStreaming()` skips the truncate since the output goes to a pipe,
  not a seekable file. This is the correct API for this use case on all
  platforms, not just Windows.
  
  ## What I Learnt
  - When upstream has applied and reverted something, state what you
  observe rather than speculating about their reasoning. Let the reviewer
  fill in context you don't have.
  - "Grep wider" (testing pattern): `stdout().writer()` appears in 17
  files. Only 2 are fixed here because only 2 are in the current Windows
  build path. But the pattern exists more broadly.
  - I feel like I am training my replacements. I mean, I am a parent, it
  rhymes.
  - I feel like my replacements are training me. It rhymes as well.
  ```
- [`7d31d9b`](https://github.com/ghostty-org/ghostty/commit/7d31d9b57f7064f74cd8a098189d2f9248ef4dd5) cmake: add import library to custom command OUTPUT ([@deblasis](https://github.com/deblasis))
  ```text
  Ninja requires all produced files to be listed as explicit outputs of
  custom commands. The zig build produces a .lib import library alongside
  the DLL, but it was not listed in the OUTPUT directive. This causes
  Ninja to fail with "missing and no known rule to make it" when
  IMPORTED_IMPLIB references the .lib file.
  ```
- [`d4a38c8`](https://github.com/ghostty-org/ghostty/commit/d4a38c8661453026bd1b1bb022ba2c37b347adce) cmake: add import library to custom command OUTPUT ([#11794](https://github.com/ghostty-org/ghostty/issues/11794)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  # What
  
  PR #11756 added IMPORTED_IMPLIB pointing to the .lib import library, but
  the
  import library is not listed in the OUTPUT directive of the
  `add_custom_command`
  that runs zig build. The file is produced as a side-effect of the build.
  
  This works with the Visual Studio generator (which is lenient about
  undeclared outputs) but fails with Ninja:
  
  ninja: error: 'zig-out/lib/ghostty-vt.lib', needed by 'ghostling',
  missing and no known rule to make it
  
  The fix adds "${ZIG_OUT_DIR}/lib/${GHOSTTY_VT_IMPLIB}" to the OUTPUT
  list. No
  behavioral change. The file was already being built, Ninja just needs to
  know
  about it.
  
  ## but_why.gif
  
  I am cleaning up https://github.com/ghostty-org/ghostling/pull/6 and I
  realise that in order to get rid of the CMake workarounds we had before
  #11756, this change is necessary.
  
  # POC
  
  I set up a branch pointing at my fork with a POC and it builds, this is
  the cleaned up CMakeList
  https://github.com/deblasis/winghostling/blob/test/cmake-implib-no-workaround/CMakeLists.txt
  ```
- [`147596d`](https://github.com/ghostty-org/ghostty/commit/147596d5608e3274e4b77fcdc201560f46fdb7c1) build(deps): bump cachix/install-nix-action from 31.10.1 to 31.10.2 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [cachix/install-nix-action](https://github.com/cachix/install-nix-action) from 31.10.1 to 31.10.2.
  - [Release notes](https://github.com/cachix/install-nix-action/releases)
  - [Changelog](https://github.com/cachix/install-nix-action/blob/master/RELEASE.md)
  - [Commits](https://github.com/cachix/install-nix-action/compare/1ca7d21a94afc7c957383a2d217460d980de4934...51f3067b56fe8ae331890c77d4e454f6d60615ff)
  
  ---
  updated-dependencies:
  - dependency-name: cachix/install-nix-action
    dependency-version: 31.10.2
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`c584f87`](https://github.com/ghostty-org/ghostty/commit/c584f87b9037455e38bd96808089f8740efb3e6c) build(deps): bump cachix/install-nix-action from 31.10.1 to 31.10.2 ([#11790](https://github.com/ghostty-org/ghostty/issues/11790)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [cachix/install-nix-action](https://github.com/cachix/install-nix-action)
  from 31.10.1 to 31.10.2.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/cachix/install-nix-action/releases">cachix/install-nix-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v31.10.2</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>nix: 2.34.1 -&gt; 2.34.2 by <a
  href="https://github.com/github-actions"><code>@​github-actions</code></a>[bot]
  in <a
  href="https://redirect.github.com/cachix/install-nix-action/pull/270">cachix/install-nix-action#270</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/cachix/install-nix-action/compare/v31...v31.10.2">https://github.com/cachix/install-nix-action/compare/v31...v31.10.2</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/51f3067b56fe8ae331890c77d4e454f6d60615ff"><code>51f3067</code></a>
  Revert &quot;ci: use 25.11 for channel tests&quot;</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/15118c17f94ae94b32a2a51839986d18c508f12f"><code>15118c1</code></a>
  ci: use 25.11 for channel tests</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/e1ac057965e5be579300ea6beb1f0e9a8a607344"><code>e1ac057</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/install-nix-action/issues/270">#270</a>
  from cachix/create-pull-request/patch</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/d181b9642fe3b3f85724b0337c37dca054cb4ef8"><code>d181b96</code></a>
  nix: 2.34.1 -&gt; 2.34.2</li>
  <li>See full diff in <a
  href="https://github.com/cachix/install-nix-action/compare/1ca7d21a94afc7c957383a2d217460d980de4934...51f3067b56fe8ae331890c77d4e454f6d60615ff">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=cachix/install-nix-action&package-manager=github_actions&previous-version=31.10.1&new-version=31.10.2)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`846599b`](https://github.com/ghostty-org/ghostty/commit/846599b97ef17a99cab699927b480e75aa36c5ac) Update VOUCHED list ([#11791](https://github.com/ghostty-org/ghostty/issues/11791)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11460#discussioncomment-16285158)
  from @00-kat.
  
  Vouch: @viruslobster
  ```

