> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: April 6, 2026 at 18:18 UTC.

## April 6, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/24039345933), [2](https://github.com/ghostty-org/ghostty/actions/runs/24036582590), [3](https://github.com/ghostty-org/ghostty/actions/runs/24035367670), [4](https://github.com/ghostty-org/ghostty/actions/runs/24018750527)  
Summary: 4 runs • 16 commits • 4 authors

### Changes

- [`3a52e0e`](https://github.com/ghostty-org/ghostty/commit/3a52e0e3bdba98b5372cf0f2d5ca5f150b8c09d7) libghostty: expose kitty image options via terminal set/get ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add four new terminal options for configuring Kitty graphics at runtime
  through the C API: storage limit, and the three loading medium flags
  (file, temporary file, shared memory).
  
  The storage limit setter propagates to all initialized screens and
  uses setLimit which handles eviction when lowering the limit. The
  medium setters similarly propagate to all screens. Getters read from
  the active screen. All options compile to no-ops or return no_value
  when kitty graphics are disabled at build time.
  ```
- [`d7fa920`](https://github.com/ghostty-org/ghostty/commit/d7fa92088c0e50d02d97190973b91d49d0c39d6a) libghostty: expose sys interface to C API ([@mitchellh](https://github.com/mitchellh))
  ```text
  The terminal sys module provides runtime-swappable function pointers
  for operations that depend on external implementations (e.g. PNG
  decoding). This exposes that functionality through the C API via a
  ghostty_sys_set() function, modeled after the ghostty_terminal_set()
  enum-based option pattern.
  
  Embedders can install a PNG decode callback to enable Kitty Graphics
  Protocol PNG support. The callback receives a userdata pointer
  (set via GHOSTTY_SYS_OPT_USERDATA) and a GhosttyAllocator that must
  be used to allocate the returned pixel data, since the library takes
  ownership of the buffer. Passing NULL clears the callback and
  disables the feature.
  ```
- [`64340c6`](https://github.com/ghostty-org/ghostty/commit/64340c62bfab76147d6fa4aec4d4979d3c4d2e33) example: add c-vt-kitty-graphics ([@mitchellh](https://github.com/mitchellh))
  ```text
  Demonstrates the sys interface for Kitty Graphics Protocol PNG
  support. The example installs a PNG decode callback via
  ghostty_sys_set, creates a terminal with image storage enabled,
  and sends an inline 1x1 PNG image through vt_write. Snippet
  markers are wired up to the sys.h doxygen docs.
  ```
- [`f65fb3d`](https://github.com/ghostty-org/ghostty/commit/f65fb3d44265f9c199df0a78f4788dc62a20b018) libghostty: expose Kitty image configs, decode png callback from C API ([#12144](https://github.com/ghostty-org/ghostty/issues/12144)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This exposes the APIs necessary to enable Kitty image protocol parsing
  and state from the C API.
  
  * You can now set the PNG decoder via the `ghostty_sys_set` API.
  * You can set Kitty image configs via `ghostty_terminal_set` API.
  * An example showing this working has been added.
  * **You cannot yet query Kitty images for metadata or rendering.** I'm
  going to follow that up in a separate PR.
  ```
- [`e390937`](https://github.com/ghostty-org/ghostty/commit/e390937867b99efce6f8ac27a033088500fe6201) macos: fix badge permission ([@KayLeung](https://github.com/KayLeung))
  ```text
  The previous version requested general notification permissions but omitted the `.badge` option. Because the initial request was granted, `settings.authorizationStatus` returns `.authorized`, leading the app to believe it has full notification privileges when it actually lacks the authority to update the dock icon badge.
  ```
- [`13f7d23`](https://github.com/ghostty-org/ghostty/commit/13f7d23145891fbe3a99c268e7df388a3c9e52fc) macOS: force layout sync when frame size mismatches GeometryReader ([@fru1tworld](https://github.com/fru1tworld))
- [`fd884bc`](https://github.com/ghostty-org/ghostty/commit/fd884bc532ca8a667a3b8397037ef382d18efc68) macOS: force surface layout sync in updateOSView ([#12143](https://github.com/ghostty-org/ghostty/issues/12143)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `updateOSView` assumed SwiftUI always propagates frame changes to the
  scroll view. Under system load, this can be deferred, leaving the
  surface rendering at stale dimensions. Check for size mismatch and mark
  layout as needed.
  
  
  <img width="1408" height="464" alt="ghostty_bug"
  src="https://github.com/user-attachments/assets/3a6f81ff-9d02-4ffa-aded-e2eddc9f40a5"
  />
  
  ---
  AI Disclosure: Used Claude Code for PR preparation.
  ```
- [`8ae8089`](https://github.com/ghostty-org/ghostty/commit/8ae80892baba44eb49faf0b33f142c120ac04412) macos: fix dock icon badge permission ([#12133](https://github.com/ghostty-org/ghostty/issues/12133)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The previous version requested general notification permissions but
  omitted the `.badge` option. Because the initial request was granted,
  `settings.authorizationStatus` returns `.authorized`, leading the app to
  believe it has full notification privileges when it actually lacks the
  authority to update the dock icon badge.
  
  Debug hint:
  You can reset the notification settings by right-clicking on the app
  name.
  <img width="307" height="85" alt=""
  src="https://github.com/user-attachments/assets/660cd332-eda6-45d6-8bfd-a6f9e28e21e8"
  />
  ```
- [`29e3de7`](https://github.com/ghostty-org/ghostty/commit/29e3de737e9cc4c4d6a3ac9624bbd26c87bf0eb2) terminal: make wuffs runtime-swappable, enable Kitty graphics for libvt ([@mitchellh](https://github.com/mitchellh))
  ```text
  Introduce terminal/sys.zig which provides runtime-swappable function
  pointers for operations that depend on external implementations. This
  allows embedders of the terminal package to swap out implementations
  at startup without hard dependencies on specific libraries.
  
  The first function exposed is decode_png, which defaults to a wuffs
  implementation. The kitty graphics image loader now calls through
  sys.decode_png instead of importing wuffs directly.
  
  This allows us to enable Kitty graphics support in libghostty-vt
  for all targets except wasm32-freestanding.
  ```
- [`6a99c24`](https://github.com/ghostty-org/ghostty/commit/6a99c248d0c2a952bf0ba1333247f3fa4e381184) terminal/kitty: add Limits to restrict capabilities of image transfer ([@mitchellh](https://github.com/mitchellh))
- [`64dcb91`](https://github.com/ghostty-org/ghostty/commit/64dcb91c1f3f1122706f70b888948d19fb1d7c42) terminal/kitty: add loading limits to kitty graphics protocol ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a Limits type to LoadingImage that controls which transmission
  mediums (file, temporary_file, shared_memory) are allowed when
  loading images. This defaults to "direct" (most restrictive) on
  ImageStorage and is set to "all" by Termio, allowing apprt
  embedders like libghostty to restrict medium types for resource or
  security reasons.
  
  The limits are stored on ImageStorage, plumbed through
  Screen.Options for screen initialization and inheritance, and
  enforced in graphics_exec during both query and transmit. Two new
  Terminal methods (setKittyGraphicsSizeLimit, setKittyGraphicsLoadingLimits)
  centralize updating all screens, replacing the manual iteration
  previously done in Termio.
  ```
- [`935d37f`](https://github.com/ghostty-org/ghostty/commit/935d37fbf1eea969245e144757116e8fbe93192a) terminal: add kitty image limits to Terminal.Options ([@mitchellh](https://github.com/mitchellh))
  ```text
  Move kitty_image_storage_limit and kitty_image_loading_limits into
  Terminal.Options so callers can set them at construction time
  rather than calling setter functions after init. The values flow
  through to Screen.Options during ScreenSet initialization. Termio
  now passes both at construction, keeping the setter functions for
  the updateConfig path.
  ```
- [`306acc4`](https://github.com/ghostty-org/ghostty/commit/306acc494128e54e1702e872d15cbf661b3c9e0a) terminal/kitty: use direct medium for tests if we're not using files ([@mitchellh](https://github.com/mitchellh))
- [`810ebae`](https://github.com/ghostty-org/ghostty/commit/810ebae8e8eca363b46553b62db7fc7bfe69e24b) terminal: lower default kitty image storage limit for libghostty ([@mitchellh](https://github.com/mitchellh))
  ```text
  The default kitty image storage limit was 320 MB for all build
  artifacts. For libghostty, this is overly generous since it is an
  embedded library where conservative memory usage is preferred.
  Lower the default to 10 MB when building as the lib artifact while
  keeping the 320 MB default for the full Ghostty application.
  ```
- [`c9c3c70`](https://github.com/ghostty-org/ghostty/commit/c9c3c701e23634fd13913cb8943962e267b00d3a) terminal: make wuffs runtime-swappable, enable Kitty graphics for libvt ([#12117](https://github.com/ghostty-org/ghostty/issues/12117)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This enables Kitty Graphics for `libghostty-vt` for the Zig API (C to
  come next).
  
  First, a note on security: by default, Kitty graphics will only allow
  images transferred via the _direct_ medium (directly via the pty) and
  will not allow file or shared memory based images. libghostty-vt
  consumers need to manually opt-in via terminal init options or
  `terminal.setKittyGraphicsLoadingLimits` to enable file-based things.
  **This is so we're as secure as possible by default.**
  
  Second, for PNG decoding, embedders must now set a global
  runtime-callback at `ghostty.sys.decode_png`. If this is not set, PNG
  formatted images are rejected. If this is set, then we'll use this to
  decode and embedders can use any decoder they want.
  
  There is no C API exposed yet to set this, so this is only for Zig to
  start.
  
  ## Examples (Zig)
  
  ### Configuring Allowed Formats
  
  ```zig
  var term = try Terminal.init(alloc, .{
      .cols = 80,
      .rows = 24,
      // Only allow direct (inline) image data, no file/shm access.
      // This is the default so you don't need to specify it.
      .kitty_image_loading_limits = .direct,
  });
  ```
  
  ```zig
  var term = try Terminal.init(alloc, .{
      .cols = 80,
      .rows = 24,
      // Allow all transmission mediums: direct, file, temporary file, shared memory.
      .kitty_image_loading_limits = .all,
  });
  ```
  
  ```zig
  var term = try Terminal.init(alloc, .{
      .cols = 80,
      .rows = 24,
      .kitty_image_loading_limits = .{
          .file = true,
          .temporary_file = true,
          .shared_memory = false,
      },
  });
  ```
  
  ### Iterate all images
  
  ```zig
  var it = term.screens.active.kitty_images.images.iterator();
  while (it.next()) |kv| {
      const img = kv.value_ptr;
      std.debug.print("id={} {}x{} format={} bytes={}\n", .{
          img.id, img.width, img.height, img.format, img.data.len,
      });
  }
  ```
  
  ### Delete all images
  
  ```zig
  term.screens.active.kitty_images.delete(alloc, &term, .{ .all = true });
  ```
  ````
- [`841a49a`](https://github.com/ghostty-org/ghostty/commit/841a49ae1a25cda91a50e4f8ebac4811503081fa) Update VOUCHED list ([#12138](https://github.com/ghostty-org/ghostty/issues/12138)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12137#discussioncomment-16460337)
  from @rhodes-b.
  
  Vouch: @neurosnap
  ```

## April 5, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/24011311343), [2](https://github.com/ghostty-org/ghostty/actions/runs/23999805792), [3](https://github.com/ghostty-org/ghostty/actions/runs/23994374178), [4](https://github.com/ghostty-org/ghostty/actions/runs/23993802101), [5](https://github.com/ghostty-org/ghostty/actions/runs/23993258076)  
Summary: 5 runs • 9 commits • 2 authors

### Changes

- [`4f543ff`](https://github.com/ghostty-org/ghostty/commit/4f543ff3d80fc33eaab2740b60356cf8ef96eed9) Update VOUCHED list ([#12135](https://github.com/ghostty-org/ghostty/issues/12135)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12133#issuecomment-4189589541)
  from @jcollie.
  
  Vouch: @KayLeung
  ```
- [`ba398df`](https://github.com/ghostty-org/ghostty/commit/ba398dfff3e30ff83da07140981ca138410cf608) Update VOUCHED list ([#12123](https://github.com/ghostty-org/ghostty/issues/12123)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12119#issuecomment-4188681042)
  from @bo2themax.
  
  Vouch: @jamylak
  ```
- [`a8e92c9`](https://github.com/ghostty-org/ghostty/commit/a8e92c9c53e5c6018507c6f1e06af4f3b3e4f49c) terminal: add APC handler to stream_terminal ([@mitchellh](https://github.com/mitchellh))
  ```text
  Wire up the APC handler to `terminal.TerminalStream` to process
  APC sequences, enabling support for kitty graphics commands in
  libghostty, in theory.
  
  The "in theory" is because we still don't export a way to actually
  enable Kitty graphics in libghostty because we have some other things in
  the way: PNG decoding and OS filesystem access that need to be more
  conditionally compiled before we can enable the feature. However, this
  is a step in the right direction, and we can at least verify that the
  APC handler works via a test in Ghostty GUI.
  ```
- [`c541ceb`](https://github.com/ghostty-org/ghostty/commit/c541ceb120ee48c3495fa9e115f1614cd2e13249) terminal: add APC handler to stream_terminal ([#12116](https://github.com/ghostty-org/ghostty/issues/12116)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Wire up the APC handler to `terminal.TerminalStream` to process APC
  sequences, enabling support for kitty graphics commands in libghostty,
  in theory.
  
  The "in theory" is because we still don't export a way to actually
  enable Kitty graphics in libghostty because we have some other things in
  the way: PNG decoding and OS filesystem access that need to be more
  conditionally compiled before we can enable the feature. However, this
  is a step in the right direction, and we can at least verify that the
  APC handler works via a test in Ghostty GUI.
  ```
- [`b9a241d`](https://github.com/ghostty-org/ghostty/commit/b9a241d1e237fa97bf8b3b161f253cc2313100f2) libghostty: add hyperlink URI accessor to grid_ref API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add ghostty_grid_ref_hyperlink_uri to extract the OSC 8 hyperlink
  URI from a cell at a grid reference position. Follows the same
  buffer pattern as ghostty_grid_ref_graphemes: callers pass a buffer
  and get back the byte length, or GHOSTTY_OUT_OF_SPACE with the
  required size if the buffer is too small. Cells without a hyperlink
  return success with length 0.
  ```
- [`757eff5`](https://github.com/ghostty-org/ghostty/commit/757eff5881b9afb811a99497fb5c231cc3677a6b) libghostty: add GhosttySelection type and selection support to formatter ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a new GhosttySelection C API type (selection.h / c/selection.zig)
  that pairs two GhosttyGridRef endpoints with a rectangle flag. This
  maps directly to the internal Selection type using untracked pins.
  
  The formatter terminal options gain an optional selection pointer.
  When non-null the formatter restricts output to the specified range
  instead of emitting the entire screen. When null the existing
  behavior of formatting the full screen is preserved.
  ```
- [`86554de`](https://github.com/ghostty-org/ghostty/commit/86554de090cdd5e9322652146e202a468a5e4bb5) libghostty: add hyperlink URI accessor to grid_ref API ([#12114](https://github.com/ghostty-org/ghostty/issues/12114)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add ghostty_grid_ref_hyperlink_uri to extract the OSC 8 hyperlink URI
  from a cell at a grid reference position. Follows the same buffer
  pattern as ghostty_grid_ref_graphemes: callers pass a buffer and get
  back the byte length, or GHOSTTY_OUT_OF_SPACE with the required size if
  the buffer is too small. Cells without a hyperlink return success with
  length 0.
  ```
- [`10696b5`](https://github.com/ghostty-org/ghostty/commit/10696b5ed170090df09f06a9afeeefe643159f40) libghostty: add GhosttySelection type and selection support to formatter ([#12115](https://github.com/ghostty-org/ghostty/issues/12115)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a new GhosttySelection C API type (selection.h / c/selection.zig)
  that pairs two GhosttyGridRef endpoints with a rectangle flag. This maps
  directly to the internal Selection type using untracked pins.
  
  The formatter terminal options gain an optional selection pointer. When
  non-null the formatter restricts output to the specified range instead
  of emitting the entire screen. When null the existing behavior of
  formatting the full screen is preserved.
  ```
- [`cf8a240`](https://github.com/ghostty-org/ghostty/commit/cf8a2407a042a2e407fe58ade93582af6073c49d) Update VOUCHED list ([#12113](https://github.com/ghostty-org/ghostty/issues/12113)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12098#discussioncomment-16452103)
  from @mitchellh.
  
  Vouch: @fru1tworld
  ```

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

