> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: April 5, 2026 at 00:25 UTC.

## April 4, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23987875945), [2](https://github.com/ghostty-org/ghostty/actions/runs/23980573913), [3](https://github.com/ghostty-org/ghostty/actions/runs/23970370985), [4](https://github.com/ghostty-org/ghostty/actions/runs/23968719391)  
Summary: 4 runs • 8 commits • 3 authors

### Changes

- [`1bd7c19`](https://github.com/ghostty-org/ghostty/commit/1bd7c19dac8cfa03b5c6b24bf6c7e6703c30c151) nix: add option to disable simd in libghostty-vt package ([@jcollie](https://github.com/jcollie))
- [`0a4cf58`](https://github.com/ghostty-org/ghostty/commit/0a4cf5877e4b325b1c3dba1833cbcafa2ed42ec7) nix: add option to disable simd in libghostty-vt package ([#12103](https://github.com/ghostty-org/ghostty/issues/12103)) ([@jcollie](https://github.com/jcollie))
- [`e157dd6`](https://github.com/ghostty-org/ghostty/commit/e157dd69c57a39f8d3a88b12e050e69830bfb1d5) build: add pkg-config static linking support and fat archives to libghostty ([@mitchellh](https://github.com/mitchellh))
  ```text
  The libghostty-vt pkg-config file was missing Libs.private, so
  pkg-config --libs --static returned the same flags as the shared
  case, omitting the C++ standard library needed by the SIMD code.
  
  Additionally, the static archive did not bundle the vendored SIMD
  dependencies (simdutf, highway, utfcpp), leaving consumers with
  unresolved symbols when linking. If we're choosing to vendor (no -fsys)
  then we should produce a fat static archive that includes them. If `-fsys`
  is used, then we should not bundle them and instead reference them via
  Requires.private, letting pkg-config chain to their own .pc files.
  
  Add Libs.private with the C++ runtime (-lc++ on Darwin, -lstdc++
  on Linux) and Requires.private for any SIMD deps provided via
  system integration. When SIMD deps are vendored (the default),
  produce a fat static archive that bundles them using libtool on
  Darwin and ar on Linux. When they come from the system (-fsys=),
  reference them via Requires.private instead, letting pkg-config
  chain to their own .pc files.
  ```
- [`0a492fd`](https://github.com/ghostty-org/ghostty/commit/0a492fdb331f1e0be29aedbcc78c3c852cb437f2) build: add pkg-config static linking support and fat archives to libghostty ([#12096](https://github.com/ghostty-org/ghostty/issues/12096)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The libghostty-vt pkg-config file was missing Libs.private, so
  pkg-config --libs --static returned the same flags as the shared case,
  omitting the C++ standard library needed by the SIMD code.
  
  Additionally, the static archive did not bundle the vendored SIMD
  dependencies (simdutf, highway, utfcpp), leaving consumers with
  unresolved symbols when linking. If we're choosing to vendor (no -fsys)
  then we should produce a fat static archive that includes them. If
  `-fsys` is used, then we should not bundle them and instead reference
  them via Requires.private, letting pkg-config chain to their own .pc
  files.
  
  Add Libs.private with the C++ runtime (-lc++ on Darwin, -lstdc++ on
  Linux) and Requires.private for any SIMD deps provided via system
  integration. When SIMD deps are vendored (the default), produce a fat
  static archive that bundles them using libtool on Darwin and ar on
  Linux. When they come from the system (-fsys=), reference them via
  Requires.private instead, letting pkg-config chain to their own .pc
  files.
  ```
- [`4f825e8`](https://github.com/ghostty-org/ghostty/commit/4f825e87f5f848347669e18e507aea91b1fb26ab) add a nix package (with CI tests) for libghostty-vt ([@jcollie](https://github.com/jcollie))
- [`326178a`](https://github.com/ghostty-org/ghostty/commit/326178adb80db39dc9e62a8c58740dc2cac3c061) nix: address review comments ([@jcollie](https://github.com/jcollie))
  ```text
  * split out dev subpackage
  * change version number to 0.1.0
  * supported on same platforms as Zig
  ```
- [`707cd57`](https://github.com/ghostty-org/ghostty/commit/707cd57acb8e79923a14ae39b1b582ed683c008b) add a nix package (with CI tests) for libghostty-vt ([#12090](https://github.com/ghostty-org/ghostty/issues/12090)) ([@mitchellh](https://github.com/mitchellh))
- [`e3bbd54`](https://github.com/ghostty-org/ghostty/commit/e3bbd54dd3bc63d00f536e086e28c33daf3f06d0) Update VOUCHED list ([#12094](https://github.com/ghostty-org/ghostty/issues/12094)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12093#discussioncomment-16444399)
  from @jcollie.
  
  Vouch: @jordandm
  ```

## April 2, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23919753798), [2](https://github.com/ghostty-org/ghostty/actions/runs/23913311718), [3](https://github.com/ghostty-org/ghostty/actions/runs/23903937555)  
Summary: 3 runs • 4 commits • 3 authors

### Changes

- [`18f2702`](https://github.com/ghostty-org/ghostty/commit/18f270222557fd46d8c3305da523212445066154) macOS: fix Find Next/Previous button in the menu bar is not working as expected ([@bo2themax](https://github.com/bo2themax))
- [`0790937`](https://github.com/ghostty-org/ghostty/commit/0790937d03df6e7a9420c61de91ce520a85fe4ef) macOS: fix Find Next/Previous button in the menu bar is not working as expected ([#12070](https://github.com/ghostty-org/ghostty/issues/12070)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  I don’t know why the search-related commands were added as performable
  keybinds in 240d5e0fc56d1b24fa9795335a3e38365190661a, but **I asked
  Claude to add some tests for that**
  
  > This won't fix cmd+g/G not working when the search bar is focused.
  ```
- [`7747c96`](https://github.com/ghostty-org/ghostty/commit/7747c96033dd435db9f7e00649178993a7791dc8) Update VOUCHED list ([#12069](https://github.com/ghostty-org/ghostty/issues/12069)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12068#issuecomment-4179350272)
  from @jcollie.
  
  Vouch: @Douglas-MacGregor
  ```
- [`63372f8`](https://github.com/ghostty-org/ghostty/commit/63372f8ddb26fa1514da2c40fc77c48076a9e4da) Update VOUCHED list ([#12066](https://github.com/ghostty-org/ghostty/issues/12066)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12038#discussioncomment-16423690)
  from @mitchellh.
  
  Vouch: @h3nock
  ```

## April 1, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23874449602), [2](https://github.com/ghostty-org/ghostty/actions/runs/23872415256), [3](https://github.com/ghostty-org/ghostty/actions/runs/23856480951), [4](https://github.com/ghostty-org/ghostty/actions/runs/23853671581), [5](https://github.com/ghostty-org/ghostty/actions/runs/23832732331)  
Summary: 5 runs • 10 commits • 5 authors

### Changes

- [`48d3e97`](https://github.com/ghostty-org/ghostty/commit/48d3e972d839999745368b156df396d9512fd17b) Update VOUCHED list ([#12052](https://github.com/ghostty-org/ghostty/issues/12052)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12050#issuecomment-4173393542)
  from @mitchellh.
  
  Vouch: @justonia
  ```
- [`9ec5672`](https://github.com/ghostty-org/ghostty/commit/9ec5672505cf9cb61006b23e799dfc154b3f7b22) Revert "macOS: close search bar if needed when it loses focus ([#11980](https://github.com/ghostty-org/ghostty/issues/11980))" ([@bo2themax](https://github.com/bo2themax))
  ```text
  This reverts commit 20cfaae2e5ec84cca2c5a55843b399b32fb9c810, reversing
  changes made to 3509ccf78ef087fec2f0209fbc297a321106d339.
  ```
- [`c16cf0e`](https://github.com/ghostty-org/ghostty/commit/c16cf0ef07edf60db1accaed1b8c6a3ba99d2dcd) fix: Ensure snap paths come first in gio module loading ([@kenvandine](https://github.com/kenvandine))
- [`92a4601`](https://github.com/ghostty-org/ghostty/commit/92a4601f39de1f9b566be45f6c02756e2145a0a7) Revert "macOS: close search bar if needed when it loses focus ([#11980](https://github.com/ghostty-org/ghostty/issues/11980))" ([#12046](https://github.com/ghostty-org/ghostty/issues/12046)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This reverts commit 20cfaae2e5ec84cca2c5a55843b399b32fb9c810, reversing
  changes made to 3509ccf78ef087fec2f0209fbc297a321106d339.
  
  This breaks some behaviours when there are multiple splits, which
  requires another click to focus to another split in the same window🫪
  ```
- [`b8251de`](https://github.com/ghostty-org/ghostty/commit/b8251de7e8656ae4a848856f00f1003347ad37d7) fix: Ensure snap paths come first in gio module loading ([#12045](https://github.com/ghostty-org/ghostty/issues/12045)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This fixes the issue reported in
  https://github.com/ghostty-org/ghostty/discussions/11311
  ```
- [`702a2b4`](https://github.com/ghostty-org/ghostty/commit/702a2b43c35b8960bdd2930b64e742a33c7ca1b9) macOS: fix upper cased letter is not correctly mapped to menu shortcut ([@bo2themax](https://github.com/bo2themax))
- [`f6e6bb0`](https://github.com/ghostty-org/ghostty/commit/f6e6bb0238cbf4ce8c154c07f5df8c5109dc9f03) macOS: fix upper cased letter is not correctly mapped to menu shortcut ([#12039](https://github.com/ghostty-org/ghostty/issues/12039)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This is known issues before key-related PRs, tested on
  fa9265636b6e14e012b9990868f60a6d2376fe59.
  
  The following config is mapped incorrectly to the menu shortcut:
  ```
  keybind=A=goto_split:left
  ```
  <img width="223" height="106" alt="image"
  src="https://github.com/user-attachments/assets/b80da251-9cff-4b29-b143-64854a5c4271"
  />
  
  Surfaces only accept `a` as a trigger to select left split, not
  `shift+a`
  ````
- [`c8702ec`](https://github.com/ghostty-org/ghostty/commit/c8702ece8f8db400df95b767fc03b401dce0d015) gtk(chore): fix typos ([@bo2themax](https://github.com/bo2themax))
  ```text
  ### AI Disclosure
  
  Claude wrote the regex to ignore base64-encoded sequences
  ```
- [`6d15b53`](https://github.com/ghostty-org/ghostty/commit/6d15b53fc753cb8087f230d1d922b2e95c526b20) gtk(chore): fix typos ([#12036](https://github.com/ghostty-org/ghostty/issues/12036)) ([@pluiedev](https://github.com/pluiedev))
- [`b7e5604`](https://github.com/ghostty-org/ghostty/commit/b7e56044dbe3265495f3578fa5764e3bb5a433f0) Update VOUCHED list ([#12031](https://github.com/ghostty-org/ghostty/issues/12031)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12030#issuecomment-4167464133)
  from @mitchellh.
  
  Vouch: @Jarred-Sumner
  ```

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

