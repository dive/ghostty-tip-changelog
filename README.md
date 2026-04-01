> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: April 1, 2026 at 00:27 UTC.

## March 31, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23818463910), [2](https://github.com/ghostty-org/ghostty/actions/runs/23817714567), [3](https://github.com/ghostty-org/ghostty/actions/runs/23816973665), [4](https://github.com/ghostty-org/ghostty/actions/runs/23809776760), [5](https://github.com/ghostty-org/ghostty/actions/runs/23804057267), [6](https://github.com/ghostty-org/ghostty/actions/runs/23800973809), [7](https://github.com/ghostty-org/ghostty/actions/runs/23799245747), [8](https://github.com/ghostty-org/ghostty/actions/runs/23778163434)  
Summary: 8 runs • 24 commits • 7 authors

### Changes

- [`4b5f2d6`](https://github.com/ghostty-org/ghostty/commit/4b5f2d60e7bc347c502ea9c13a59ba1f3f0546ff) core/gtk: ensure that first surface gets marked as focused surface by app ([@jcollie](https://github.com/jcollie))
- [`c2dd757`](https://github.com/ghostty-org/ghostty/commit/c2dd7579e28ff1fecb4a68f32ae8cacda576550c) core/gtk: ensure that first surface gets marked as focused surface by app ([#12029](https://github.com/ghostty-org/ghostty/issues/12029)) ([@jcollie](https://github.com/jcollie))
- [`dee8598`](https://github.com/ghostty-org/ghostty/commit/dee8598dc040962e9dbf5a050e2e65456b3da9d1) gtk: use surface id for notifications instead of pointer ([@jcollie](https://github.com/jcollie))
- [`0f6836c`](https://github.com/ghostty-org/ghostty/commit/0f6836c69fdc480ea84f983dfe4c0bb18edb4f61) gtk: use surface id for notifications instead of pointer ([#12028](https://github.com/ghostty-org/ghostty/issues/12028)) ([@jcollie](https://github.com/jcollie))
- [`ff02ed1`](https://github.com/ghostty-org/ghostty/commit/ff02ed1b3458f88e3d3eb31d59027e374aba2ecd) core: add 64 bit unique ID to every core surface ([@jcollie](https://github.com/jcollie))
  ```text
  - Expose that ID as the environment variable GHOSTTY_SURFACE_ID to
    processes running in Ghostty surfaces.
  - Add a function to the core app to search for surfaces by ID.
  - ID is randomly generated, it has no other meaning other than as a
    unique identifier for the surface. The ID also cannot be zero as that
    is used to indicate a null ID in some situations.
  ```
- [`f90180f`](https://github.com/ghostty-org/ghostty/commit/f90180f91f1e28d474f458e7ebe3d10f4d7bd3cd) core: add 64 bit unique ID to every core surface ([#12027](https://github.com/ghostty-org/ghostty/issues/12027)) ([@jcollie](https://github.com/jcollie))
  ```text
  - Expose that ID as the environment variable GHOSTTY_SURFACE_ID to
  processes running in Ghostty surfaces.
  - Add a function to the core app to search for surfaces by ID.
  - ID is randomly generated, it has no other meaning other than as a
  unique identifier for the surface. The ID also cannot be zero as that is
  used to indicate a null ID in some situations.
  ```
- [`4803d58`](https://github.com/ghostty-org/ghostty/commit/4803d58bb4ea8d2a71ebc1e5239f09a060e9e7c3) apprt/embedded: fix ghostty_surface_free_text parameter mismatch ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #12020
  
  The C header declared ghostty_surface_free_text with both a
  ghostty_surface_t and ghostty_text_s* parameter, but the Zig
  implementation only accepted a *Text parameter. This caused the
  surface pointer to be interpreted as the text pointer, so the
  actual text allocation was never freed.
  ```
- [`f16d354`](https://github.com/ghostty-org/ghostty/commit/f16d35489b1809657bb2675ab6bdc7eabefb59f9) apprt/embedded: fix ghostty_surface_free_text parameter mismatch ([#12025](https://github.com/ghostty-org/ghostty/issues/12025)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #12020
  
  The C header declared ghostty_surface_free_text with both a
  ghostty_surface_t and ghostty_text_s* parameter, but the Zig
  implementation only accepted a *Text parameter. This caused the surface
  pointer to be interpreted as the text pointer, so the actual text
  allocation was never freed.
  
  I opted to keep the surface parameter to minimize the diff here. I'm not
  sure why I thought I would need access to that surface pointer but just
  want to fix the leak first.
  ```
- [`b288063`](https://github.com/ghostty-org/ghostty/commit/b2880636af477287436e01e8a86238bfa198b0e1) Update VOUCHED list ([#12022](https://github.com/ghostty-org/ghostty/issues/12022)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12019#discussioncomment-16396278)
  from @jcollie.
  
  Vouch: @danneu
  ```
- [`e993ded`](https://github.com/ghostty-org/ghostty/commit/e993ded7c8a8078d28d4d4d3d2ba93cb9edce71f) ghostty.h: guard sys/types.h include for MSVC ([@deblasis](https://github.com/deblasis))
  ```text
  sys/types.h is a POSIX header that does not exist on MSVC. Move it
  into the #else branch of the existing _MSC_VER guard that already
  provides ssize_t via BaseTsd.h.
  ```
- [`ed6f058`](https://github.com/ghostty-org/ghostty/commit/ed6f0588a31ea76b027724ec4127cedbe5c3bdbf) feat: make version clickable depending on type ([@louisunlimited](https://github.com/louisunlimited))
- [`b29f261`](https://github.com/ghostty-org/ghostty/commit/b29f261dc89b6c9ed1b37d700ec3f815dcf00462) chore: clean up versionConfig to be init-able ([@louisunlimited](https://github.com/louisunlimited))
- [`90d71dd`](https://github.com/ghostty-org/ghostty/commit/90d71dd2f62b33ddb44ba8cb647e24b3eb76e131) chore: clean up comments ([@louisunlimited](https://github.com/louisunlimited))
- [`183e2ce`](https://github.com/ghostty-org/ghostty/commit/183e2cef2f17c6b43427635ac124edc13cbd1425) chore: clean up switch statement ([@louisunlimited](https://github.com/louisunlimited))
- [`010880a`](https://github.com/ghostty-org/ghostty/commit/010880a90ae5988335a6174493a6f2d2644be08b) chore: make url computed property & rework enum signature ([@louisunlimited](https://github.com/louisunlimited))
- [`591dbd5`](https://github.com/ghostty-org/ghostty/commit/591dbd511265efcf24b3a60ca31b6ce5716c68c6) macOS: fix incorrect delete symbol mapping ([@bo2themax](https://github.com/bo2themax))
- [`f140b14`](https://github.com/ghostty-org/ghostty/commit/f140b1463fc7f0d5a3d84d09663d90ea31c2ea85) macOS: fix incorrect delete symbol mapping ([#12011](https://github.com/ghostty-org/ghostty/issues/12011)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  `GHOSTTY_KEY_DELETE` should be mapped to `KeyEquivalent.deleteForward`.
  This fixes the correct symbol showing in the menu. Previously, both
  `GHOSTTY_KEY_DELETE` and `GHOSTTY_KEY_BACKSPACE` were showing `⌫`, but
  `GHOSTTY_KEY_DELETE` only worked for `fn+delete`.
  
  Add the following keybind and observe the symbol in the menu:
  ```
  keybind=delete=new_tab
  ```
  
  <img width="535" height="318" alt="image"
  src="https://github.com/user-attachments/assets/67ed7b5d-f848-42ee-a382-fe364d86cb2c"
  />
  ````
- [`5fe876c`](https://github.com/ghostty-org/ghostty/commit/5fe876cfa05d86b06da7a7fc31c363a4fc54661a) ghostty.h: guard sys/types.h include for MSVC ([#12010](https://github.com/ghostty-org/ghostty/issues/12010)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Summary
  
  - Move `sys/types.h` include into the `#else` branch of the existing
  `_MSC_VER` guard
  - MSVC does not ship `sys/types.h` (POSIX header), and already gets
  `ssize_t` from `BaseTsd.h`
  
  ## Test plan
  
  - [x] `zig build -Dapp-runtime=none` -- clean build
  - [x] `zig build test -Dapp-runtime=none` on Windows (2606/2660 passed,
  54 skipped)
  - [x] `zig build test` on Linux (2658/2684 passed, 26 skipped)
  - [x] `zig build test` on macOS (2658/2668 passed, 10 skipped)
  - [x] `zig build test-lib-vt` on all 3 platforms
  - [x] Zig examples build on all 3 platforms
  - [x] CMake examples build on Windows (c-vt-cmake pass,
  c-vt-cmake-static pass)
  ```
- [`292bf13`](https://github.com/ghostty-org/ghostty/commit/292bf13d06a82065da2a9fb19cf18c2267578309) macOS: Make version in about dialog clickable ([#12007](https://github.com/ghostty-org/ghostty/issues/12007)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  - Fixes: https://github.com/ghostty-org/ghostty/issues/11964
  
  Made a private enum type `VersionConfig` to reference whether the
  release is a semver or tip, makes it easier for later in the view to
  `switch` between cases.
  
  I do think there could be a better place for this enum or we can get rid
  of it, open to opinions. Right now version parsing is kind of duplicated
  between `AboutView` and `UpdateModalView` so we can also extract to a
  common helper if wanted.
  
  Tested by manually setting `Marketing Version` in build settings to
  
  `1.3.1`
  <img width="412" height="532" alt="Screenshot 2026-03-30 at 18 31 15"
  src="https://github.com/user-attachments/assets/285bb94d-138b-4169-bb66-684eb04b6ca3"
  />
  
  `332b2aefc`
  <img width="412" height="532" alt="Screenshot 2026-03-30 at 18 32 48"
  src="https://github.com/user-attachments/assets/fea30d39-bea7-4885-8221-1696e148f45e"
  />
  
  ### AI Disclosure
  I used Sonnet 4.6 to understand where the version strings came from and
  in what format, it read release yml files to see what's going on. Then
  it proposed really bad code so I manually went in and cleaned up the
  view.
  ```
- [`30c9dec`](https://github.com/ghostty-org/ghostty/commit/30c9dec76b706c5b26cfad3fb0c25c4850ff1175) add all C struct layout metadata for WASM ([@elias8](https://github.com/elias8))
- [`1d0a247`](https://github.com/ghostty-org/ghostty/commit/1d0a247c20aa009124a0ba75cf9e460b7fa4aa1d) sort map alphabetically ([@elias8](https://github.com/elias8))
- [`f827530`](https://github.com/ghostty-org/ghostty/commit/f82753010300668d67c884fd75f618e7493978b8) libghostty: add all C struct layout metadata for WASM ([#12017](https://github.com/ghostty-org/ghostty/issues/12017)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Added all C structs and sorted the entries for readability.
  ```
- [`a06350d`](https://github.com/ghostty-org/ghostty/commit/a06350df9b077a0aa82657ecff22e7fb0d620faf) macOS: close search bar if needed when it loses focus ([@bo2themax](https://github.com/bo2themax))
  ```text
  This adds features like:
  1. Clicking outside of SearchBar works like typing `escape`
  2. Typing `tab` while search bar is focused also works like typing `escape`
  ```
- [`20cfaae`](https://github.com/ghostty-org/ghostty/commit/20cfaae2e5ec84cca2c5a55843b399b32fb9c810) macOS: close search bar if needed when it loses focus ([#11980](https://github.com/ghostty-org/ghostty/issues/11980)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds features like:
  
  1. Clicking outside of search bar works like typing `escape`
  2. Typing `tab` while search bar is focused also works like typing
  `escape`
  
  
  https://github.com/user-attachments/assets/a51f1560-ed14-4002-81b4-96eb927b17ca
  ```

## March 30, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23772709377), [2](https://github.com/ghostty-org/ghostty/actions/runs/23771282085), [3](https://github.com/ghostty-org/ghostty/actions/runs/23770358156), [4](https://github.com/ghostty-org/ghostty/actions/runs/23768910243), [5](https://github.com/ghostty-org/ghostty/actions/runs/23767138351), [6](https://github.com/ghostty-org/ghostty/actions/runs/23760068061), [7](https://github.com/ghostty-org/ghostty/actions/runs/23758387957), [8](https://github.com/ghostty-org/ghostty/actions/runs/23755858760), [9](https://github.com/ghostty-org/ghostty/actions/runs/23753629101), [10](https://github.com/ghostty-org/ghostty/actions/runs/23752772466)  
Summary: 10 runs • 45 commits • 8 authors

### Changes

- [`3509ccf`](https://github.com/ghostty-org/ghostty/commit/3509ccf78ef087fec2f0209fbc297a321106d339) Update VOUCHED list ([#12005](https://github.com/ghostty-org/ghostty/issues/12005)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11981#issuecomment-4158783258)
  from @tristan957.
  
  Vouch: @yabbal
  ```
- [`ee19c8f`](https://github.com/ghostty-org/ghostty/commit/ee19c8ff7f5f4e20e6279bc81f0bc5ede0b172d9) wasm: binary patching wow ([@mitchellh](https://github.com/mitchellh))
- [`624b488`](https://github.com/ghostty-org/ghostty/commit/624b4884c343a53fd256ca8da1628a4690a7b6f2) Add build_table ([@mitchellh](https://github.com/mitchellh))
- [`6c085e5`](https://github.com/ghostty-org/ghostty/commit/6c085e54426b83a8059273dc4b2a6ed159a76f15) build: binary patch to add growable tables ([@mitchellh](https://github.com/mitchellh))
- [`01a8ea7`](https://github.com/ghostty-org/ghostty/commit/01a8ea72125c4de72101637805a4c920eb54d34b) build: binary patching with Zig ([@mitchellh](https://github.com/mitchellh))
- [`f89195a`](https://github.com/ghostty-org/ghostty/commit/f89195ace9d5157e7a265acf807fbeb9b839b7c2) revert example/wasm-vt ([@mitchellh](https://github.com/mitchellh))
- [`50f3b1d`](https://github.com/ghostty-org/ghostty/commit/50f3b1d60dcbc7813aabb4170acfb8fc524b3ec6) libghostty: export function table and make it growable for wasm ([#12003](https://github.com/ghostty-org/ghostty/issues/12003)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Replaces #11958
  
  This exports the function table and makes it growable so that the
  effects API can be used. It's still very not ergonomic to use the
  effects API so I'm going to work on that next, but this at least makes
  it _possible_. Zig 0.15.x is missing the ability to pass
  `--growable-table` to the linker so we use binary patching to add it
  (yay!) lol.
  ```
- [`8fc0c85`](https://github.com/ghostty-org/ghostty/commit/8fc0c85e0c83d5eac3ba09720a5cc3024d2aa676) Update VOUCHED list ([#12002](https://github.com/ghostty-org/ghostty/issues/12002)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12001#discussioncomment-16386924)
  from @jcollie.
  
  Vouch: @louisunlimited
  ```
- [`a83a82b`](https://github.com/ghostty-org/ghostty/commit/a83a82b3f87b6efeb4384cbc9350056be70ecde0) build: normalize input archives before Darwin libtool merge (Barut)
  ```text
  Apple's recent libtool can warn about misaligned 64-bit archive members
  and silently drop them when merging static libraries. In Ghostty this
  showed up in the Darwin libtool step that builds libghostty-fat.a.
  
  Normalize each input archive by copying it and running ranlib on the
  copy
  before handing it to libtool. That rewrites the archive into a layout
  Apple's linker tools accept without flattening members through the
  filesystem or changing Ghostty's archive format.
  ```
- [`c75081b`](https://github.com/ghostty-org/ghostty/commit/c75081b89c5c5e6a337b926bb5abdbd81f2eaf1e) build: normalize input archives before Darwin libtool merge ([#11999](https://github.com/ghostty-org/ghostty/issues/11999)) ([@jcollie](https://github.com/jcollie))
  ```text
  ## Root cause
  
  Zig 0.15.2 can produce macOS `.a` archives where some 64-bit Mach-O
  members are only 4-byte aligned inside the archive. Recent Apple
  `libtool -static` does not handle that layout correctly: it emits `not
  8-byte aligned` warnings and, in the failing case, silently drops those
  members when creating the combined static library.
  
  In Ghostty, this happened in the Darwin `libtool` merge step that builds
  `libghostty-fat.a`. The x86_64 input `libghostty.a` still contained the
  expected `libghostty_zcu.o` and about 97 exported `_ghostty_` symbols,
  but after `libtool -static` the output archive contained only 4 SIMD
  symbols because `libghostty_zcu.o` had been discarded. The same warning
  pattern also appeared in third-party input archives such as
  `libfreetype.a` and `libz.a`, so this was not only a `libghostty.a`
  problem.
  
  ## What needed to be done
  
  The inputs to Apple `libtool` needed to be normalized before they were
  merged.
  
  The safest fix is to copy each input archive and run `ranlib -D` on the
  copy before passing it to `libtool`. `ranlib` rewrites the archive into
  a form that Apple’s linker tools accept, fixing the alignment/layout
  issue without changing the archive’s semantic contents.
  
  ## Why this approach
  
  An `ar x` -> `ar rcs` workaround can also make the warnings go away, but
  it is a broader and riskier transformation. Extracting archive members
  into a flat directory is not semantics-preserving:
  
  - duplicate member basenames can collide
  - non-`.o` members can be lost
  - member order can change
  
  That means an `ar`-based rearchive can silently change valid archives
  while fixing alignment. `ranlib -D` avoids those hazards because it
  rewrites the archive in place instead of flattening it through the
  filesystem.
  
  `-D` is also important because plain `ranlib` is not deterministic. In
  local testing, `ranlib -D` still fixed the alignment issue, preserved
  all 97 `_ghostty_` symbols, produced no `libtool` warnings, and was
  byte-stable across repeated runs.
  
  ## Validation
  
  This was reproduced directly:
  
  - before normalization, running `libtool -static` on the affected x86_64
  `libghostty.a` produced a `libghostty_zcu.o not 8-byte aligned` warning
  and the output archive dropped from 97 `_ghostty_` symbols to 4
  - after `ranlib -D`, the same `libtool -static` command preserved all 97
  `_ghostty_` symbols and emitted no alignment warnings
  
  After applying the normalization step, a clean `zig build` succeeded,
  and the final macOS xcframework archive contained 97 `_ghostty_` symbols
  in both the `x86_64` and `arm64` slices.
  
  ## Summary
  
  This was not a Metal issue, not an Xcode project issue, and not a
  stale-cache issue. The actual root cause was an Apple `libtool`
  interoperability problem with Zig-produced macOS archives. The required
  fix was to normalize each archive before the Darwin `libtool` merge
  step, and `ranlib -D` is the least invasive way to do that while
  preserving archive semantics.
  ```
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

