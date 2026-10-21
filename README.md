> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: October 21, 2026 at 21:08 UTC.

## October 21, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/39620313939), [2](https://github.com/ghostty-org/ghostty/actions/runs/39562349268), [3](https://github.com/ghostty-org/ghostty/actions/runs/39536529900), [4](https://github.com/ghostty-org/ghostty/actions/runs/39533979636)  
Summary: 4 runs • 25 commits • 6 authors

### Changes

- [`521cf2c`](https://github.com/ghostty-org/ghostty/commit/521cf2c5d30bd48028ca61546c64e7913764073d) Update VOUCHED list ([#14798](https://github.com/ghostty-org/ghostty/issues/14798)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14774#discussioncomment-19100005)
  from @jcollie.
  
  Vouch: @olrtg
  ```
- [`9603143`](https://github.com/ghostty-org/ghostty/commit/9603143989e302937878c1b43f4083d2ca0f04fd) gtk: fix focus and drop result when moving a split between split trees ([@thomasfedb](https://github.com/thomasfedb))
  ```text
  Moving a split out of a split tree now moves focus in that tree to
  another split, as closing it does. Previously the old window kept the
  moved split's title and didn't receive keyboard input.
  
  The split drop handler now returns whether the split was moved, since
  GTK expects a result from it.
  ```
- [`67edd20`](https://github.com/ghostty-org/ghostty/commit/67edd20a0292629da7e01b64973de19d356df487) gtk: fix focus and drop result when moving a split between split trees ([#14475](https://github.com/ghostty-org/ghostty/issues/14475)) ([@jcollie](https://github.com/jcollie))
  ```text
  **Issue**
  Dragging a split onto a split in another window removed it from its
  split tree without moving focus to another split, as closing a split
  does. The old window kept showing the moved split's title.
  
  To reproduce: split a window (A | B), open a second window, and drag B's
  handle onto the second window's split. The first window's title still
  reads B's title, and typing does nothing.
  
  **Fix**
  This reuses the close path's "remove and focus a neighbour" logic for
  moves.
  Tested on Fedora 44 against current `main`, before and after the change.
  
  First pass written with Claude Code (Claude Opus 5.5), reviewed and
  reprompted by me.
  ```
- [`1152bc9`](https://github.com/ghostty-org/ghostty/commit/1152bc991ce9ff95323c25566dc7fe6b3d2d4648) termio: free the exec env once when Surface.init fails ([@Pyre909](https://github.com/Pyre909))
- [`d7ea628`](https://github.com/ghostty-org/ghostty/commit/d7ea6284a620e94ea8c2725d9ce967f806dfdea3) core: free the termio derived config when Termio.init fails ([@Pyre909](https://github.com/Pyre909))
- [`05b4692`](https://github.com/ghostty-org/ghostty/commit/05b46924ea4de8bda3b14f60e1accea9b98e20b4) termio: fail every allocation in the exec env test ([@Pyre909](https://github.com/Pyre909))
- [`1e9b06f`](https://github.com/ghostty-org/ghostty/commit/1e9b06f601d6956d3ea80a57bcde03370d51e48e) core: free the renderer config when Renderer.init fails ([@Pyre909](https://github.com/Pyre909))
- [`0bda7c3`](https://github.com/ghostty-org/ghostty/commit/0bda7c34c54b5bee0e5d7d44ded5f94e873f00fd) core: release the font grid when Surface.init fails ([@Pyre909](https://github.com/Pyre909))
- [`88fb0f8`](https://github.com/ghostty-org/ghostty/commit/88fb0f8f677676e8563f66db547eacbb72d9e438) terminal: make Kitty image storage dirty a change counter ([@mitchellh](https://github.com/mitchellh))
- [`4501fe7`](https://github.com/ghostty-org/ghostty/commit/4501fe72ecf98f325d68a34815ff1a631de0a5f9) terminal: add a fixed Kitty placement kind to the render state ([@mitchellh](https://github.com/mitchellh))
- [`b1260a0`](https://github.com/ghostty-org/ghostty/commit/b1260a050cc7ccae43dd503984cd98d6ee9996e1) terminal: report fixed Kitty placements from the render state ([@mitchellh](https://github.com/mitchellh))
- [`59a68e1`](https://github.com/ghostty-org/ghostty/commit/59a68e16628485057303eff98ee9d91d844d666b) terminal: tell render state consumers when the image list changed ([@mitchellh](https://github.com/mitchellh))
- [`d22c3aa`](https://github.com/ghostty-org/ghostty/commit/d22c3aa030b9e38fc6a0d60eccb2918d5aeda4df) terminal: expose the image placements generation to C embedders ([@mitchellh](https://github.com/mitchellh))
- [`7bd9798`](https://github.com/ghostty-org/ghostty/commit/7bd979836f96976632e9bfa4534229d73cecf0eb) renderer: draw every Kitty placement from the render state ([@mitchellh](https://github.com/mitchellh))
- [`9fc5ec6`](https://github.com/ghostty-org/ghostty/commit/9fc5ec6bbc1fdde5c0aa2b6853f057c37f144729) docs: describe drawing Kitty images from the render state ([@mitchellh](https://github.com/mitchellh))
- [`606012e`](https://github.com/ghostty-org/ghostty/commit/606012ecb9686d8eb36c041bca69d648cdc87410) terminal: fix render state compile on 32-bit targets ([@mitchellh](https://github.com/mitchellh))
- [`dcaf698`](https://github.com/ghostty-org/ghostty/commit/dcaf6984ed542ddb297be6acc9d757504dfa8e0b) terminal: reject OSC 7501 reports with malformed ids ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #14790
  
  OSC 7501 validation iterated id values with a ValueIterator that
  filtered by the value alphabet, which silently skips any value
  containing a disallowed byte.
  
  Validation now iterates the raw values so invalid ids discard the
  whole report as documented. The app, title, and msg length checks
  had the same filtering, so an over-limit value with a disallowed
  byte also escaped its limit. Those now check raw values too.
  ```
- [`8c425a7`](https://github.com/ghostty-org/ghostty/commit/8c425a7bd57de848aa83cb9b003b1ecd6037c56a) terminal: reject OSC 7501 reports with malformed ids ([#14793](https://github.com/ghostty-org/ghostty/issues/14793)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #14790
  
  OSC 7501 validation iterated id values with a ValueIterator that
  filtered by the value alphabet, which silently skips any value
  containing a disallowed byte.
  
  Validation now iterates the raw values so invalid ids discard the whole
  report as documented. The app, title, and msg length checks had the same
  filtering, so an over-limit value with a disallowed byte also escaped
  its limit. Those now check raw values too.
  ```
- [`5799392`](https://github.com/ghostty-org/ghostty/commit/5799392844848cab33b2be217b0963e44fec5026) termio: free the exec env once when Surface.init fails ([#14715](https://github.com/ghostty-org/ghostty/issues/14715)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fix for the double free described in #14708.
  
  `Surface.init` passes the termio env map to `termio.Exec.init` by value,
  and the subprocess frees it in `Exec.deinit`. Though the surface's
  `errdefer env.deinit()` stays armed after that handoff, so if a later
  step fails (the mailbox, `Termio.DerivedConfig.init`, or `Termio.init`),
  the env is freed twice: once by `io_exec.deinit()` and again by
  `env.deinit()`. If `Exec.init` itself fails after adding entries, the
  surface frees its stale copy of the map instead.
  
  The fix:
  - `Exec.init` owns the env from the call on and frees it if it fails.
  Only its copy is current once it has modified the map, so the caller
  can't free it safely.
  - `Surface.init` builds the env in its own block, so its errdefer ends
  before the handoff.
  - A test fails an allocation inside `Exec.init` and relies on the
  testing allocator to catch a leaked env. Without the fix it reports 317
  bytes allocated and 0 freed.
  - Fixes the term config leak, renderer config leak, and the font grid
  reference. For which all are on the same failure path.
  
  **Testing**
  - Was able to Reproduce on macOS(Upstream), Linux (GTK) (Upstream), and
  Windows (ran under my forked build) by forcing an allocation failure
  just before `Termio.init`. Each crashed in `Environ.Map.deinit` at
  `0xaaaaaaaaaaaaaaaa` (freed memory) without the fix and reported a clean
  `error.OutOfMemory` with it.
  - `zig build test` on macOS: all tests pass.
  
  **AI disclosure:** I used Claude Code to help find the bug, write the
  fix and test, and run the reproductions. I reviewed the changes and
  understand all the code being submitted for implementation.
  ```
- [`48dde97`](https://github.com/ghostty-org/ghostty/commit/48dde97e0413a27064e4c6182db3df6ee999db7d) Move all Kitty placements to RenderState, update renderer ([#14789](https://github.com/ghostty-org/ghostty/issues/14789)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This finishes moving Kitty image placements into `RenderState`, which
  #14780 started with virtual placements.
  
  The render state now reports every Kitty placement on screen: virtual,
  fixed (placed at a cell), and relative placements, including ones
  chained to a fixed placement. Ghostty's renderer now draws only from the
  render state's image placement iterator, so Ghostty and libghostty-vt
  embedders share one source of truth for what images are on screen and
  where.
  
  Benchmark highlights (image work per frame, main => this PR):
  
  - Scrolling with images and 100k lines of scrollback: 3.3µs to 70ns.
  Main's cost grew with scrollback because `pointFromPin` walks the page
  list, but the new render state doesn't do that.
  - New output lines with images on screen: 672–919ns to ~115ns.
  - A dirty row with placeholder images elsewhere on screen: 281ns to
  14ns. Main rebuilt every frame, but the render state is smarter.
  
  **AI usage:** I drove the overall Zig code changes and wrote most of it,
  AI helped with the C API changes since they're mostly mechanical, plus
  testing, validation. I wrote all the comment/docs and this PR message.
  ```
- [`57ad578`](https://github.com/ghostty-org/ghostty/commit/57ad5787a34f38c8bf505d3defa576c551c8620d) gtk: pass an activation token to the OpenURI portal (Dylan Kenney)
  ```text
  Opening a link through the portal sent no activation_token, so the app
  the portal launched had no proof the user asked for it and couldn't
  raise its window on compositors that check. Ask GDK for a token tied to
  the input that opened the link, as GTK's own URI launcher does, and
  pass it in the OpenURI options.
  ```
- [`ab77366`](https://github.com/ghostty-org/ghostty/commit/ab773665b99f35d0877f02c5438ff36423d82207) nix: update zon2nix ([@jcollie](https://github.com/jcollie))
  ```text
  Eliminates extraneous flake inputs.
  Better caching behavior.
  ```
- [`df246d0`](https://github.com/ghostty-org/ghostty/commit/df246d0105e13dfd4a6a54754a9c6555325644ec) nix: update zon2nix ([#14788](https://github.com/ghostty-org/ghostty/issues/14788)) ([@jcollie](https://github.com/jcollie))
  ```text
  Eliminates extraneous flake inputs.
  Better caching behavior.
  ```
- [`47bd203`](https://github.com/ghostty-org/ghostty/commit/47bd2033cd01a84fe45f1256606224a6891da5cb) gtk: pass an activation token to the OpenURI portal ([#14787](https://github.com/ghostty-org/ghostty/issues/14787)) ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes #14785
  
  Opening a link through the portal sent no activation_token, so the app
  the portal launched had no proof the user asked for it and couldn't
  raise its window on compositors that check. Ask GDK for a token tied to
  the input that opened the link, as GTK's own URI launcher does, and pass
  it in the OpenURI options.
  
  Rebased on main (Zig 0.17), 3994 tests passed, 0 failed, and a
  Ctrl+click's token showed up in the OpenURI call and Brave used it.
  
  Claude Code wrote the change and ran the build and test suite. I
  reviewed the code and did the real-click tests myself.
  ```
- [`90dcd00`](https://github.com/ghostty-org/ghostty/commit/90dcd00b508c86e79402e8d06a5afd16af6b6059) Update VOUCHED list ([#14794](https://github.com/ghostty-org/ghostty/issues/14794)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14792#discussioncomment-19086968)
  from @jcollie.
  
  Vouch: @binaryfire
  ```

## October 20, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/39489141420), [2](https://github.com/ghostty-org/ghostty/actions/runs/39488892378), [3](https://github.com/ghostty-org/ghostty/actions/runs/39477553764), [4](https://github.com/ghostty-org/ghostty/actions/runs/39352155221)  
Summary: 4 runs • 64 commits • 5 authors

### Changes

- [`96a5131`](https://github.com/ghostty-org/ghostty/commit/96a5131a15281765aff5835dbd9e1c714cddcd3f) Update VOUCHED list ([#14783](https://github.com/ghostty-org/ghostty/issues/14783)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14782#discussioncomment-19080745)
  from @jcollie.
  
  Vouch: @dmkenney
  ```
- [`17bc3e9`](https://github.com/ghostty-org/ghostty/commit/17bc3e94a77edc650913d7627c92e3253e15d177) resolve Kitty graphics placeholders in the render state ([@mitchellh](https://github.com/mitchellh))
  ````text
  This adds image placements in `RenderState`, unifying all our image
  placement logic into one location for both Ghostty GUI and libghostty-vt.
  
  Note this only does Kitty virtual placements right now but the plan is
  to move ALL images into this so all renderers (Ghostty and libghostty)
  have one source of truth for all possible rendered images.
  
  I purposely made all the APIs as generic as possible so we can support
  other graphics protocols that might exist in the future. None planned,
  just doing this now for ABI reasons since this touches the C ABI.
  
  Benchmark highlights:
  
  - Ghostty per frame with a screen full of placeholders and one dirty
    row: 207us to 3.4us. Main rescanned the whole viewport every frame
    while any virtual placement existed.
  - Render state with a screen full of placeholders: full redraw 127us
    to 172us (about 4.5ns per placeholder cell), one dirty row 2.2us to
    3.1us.
  - Render state without images: +3ns per clean update (noise) and
    +6.5ns per update with one dirty row (noise).
  
  Example:
  
  ```c
  ghostty_render_state_get(
      state, GHOSTTY_RENDER_STATE_DATA_IMAGE_ITERATOR, &images);
  while (ghostty_render_state_image_iterator_next(images)) {
    GhosttyImageProtocol protocol;
    uint32_t image_id;
    uint64_t generation;
    ghostty_render_state_image_get(
        images, GHOSTTY_RENDER_STATE_IMAGE_DATA_PROTOCOL, &protocol);
    ghostty_render_state_image_get(
        images, GHOSTTY_RENDER_STATE_IMAGE_DATA_IMAGE_ID, &image_id);
    ghostty_render_state_image_get(
        images, GHOSTTY_RENDER_STATE_IMAGE_DATA_IMAGE_GENERATION,
        &generation);
  
    // Read the position, size, source rectangle, layer, and z the same
    // way, then draw the texture for (protocol, image_id, generation).
  }
  ```
  ````
- [`0643224`](https://github.com/ghostty-org/ghostty/commit/0643224a73c2387ebc038f72ab535943cfbf5c6f) resolve Kitty graphics placeholders in the render state ([#14780](https://github.com/ghostty-org/ghostty/issues/14780)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This adds image placements in `RenderState`, unifying all our image
  placement logic into one location for both Ghostty GUI and
  libghostty-vt.
  
  Note this only does Kitty virtual placements right now but the plan is
  to move ALL images into this so all renderers (Ghostty and libghostty)
  have one source of truth for all possible rendered images.
  
  I purposely made all the APIs as generic as possible so we can support
  other graphics protocols that might exist in the future. None planned,
  just doing this now for ABI reasons since this touches the C ABI.
  
  Benchmark highlights:
  
  - Ghostty per frame with a screen full of placeholders and one dirty
  row: 207us to 3.4us. Main rescanned the whole viewport every frame while
  any virtual placement existed.
  - Render state with a screen full of placeholders: full redraw 127us to
  172us (about 4.5ns per placeholder cell), one dirty row 2.2us to 3.1us.
  - Render state without images: +3ns per clean update (noise) and +6.5ns
  per update with one dirty row (noise).
  
  Example:
  
  ```c
  ghostty_render_state_get(
      state, GHOSTTY_RENDER_STATE_DATA_IMAGE_ITERATOR, &images);
  while (ghostty_render_state_image_iterator_next(images)) {
    GhosttyImageProtocol protocol;
    uint32_t image_id;
    uint64_t generation;
    ghostty_render_state_image_get(
        images, GHOSTTY_RENDER_STATE_IMAGE_DATA_PROTOCOL, &protocol);
    ghostty_render_state_image_get(
        images, GHOSTTY_RENDER_STATE_IMAGE_DATA_IMAGE_ID, &image_id);
    ghostty_render_state_image_get(
        images, GHOSTTY_RENDER_STATE_IMAGE_DATA_IMAGE_GENERATION,
        &generation);
  
    // Read the position, size, source rectangle, layer, and z the same
    // way, then draw the texture for (protocol, image_id, generation).
  }
  ```
  
  **AI usage:** I designed the whole thing and wrote all the
  docs/comments, had Fable/Opus come in to add validation and benchmarks.
  ````
- [`16956fb`](https://github.com/ghostty-org/ghostty/commit/16956fb43b2a4a42576d7e712e9725c0b4817810) Update VOUCHED list ([#14781](https://github.com/ghostty-org/ghostty/issues/14781)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14779#discussioncomment-19080718)
  from @jcollie.
  
  Vouch: @thapakrish
  ```
- [`3110fb3`](https://github.com/ghostty-org/ghostty/commit/3110fb358948cfef6e4f03d6b270a882168d17cf) nix: update to Zig 0.17 ([@pluiedev](https://github.com/pluiedev))
- [`8b94338`](https://github.com/ghostty-org/ghostty/commit/8b9433839c23bec54f5907c86ea089192ac0f0af) nix: update zon2nix ([@pluiedev](https://github.com/pluiedev))
- [`a557f01`](https://github.com/ghostty-org/ghostty/commit/a557f010cb73cf73363963a0e37b24d14292e820) nix: patch pkg-config files to comply with Zig 0.17 ([@pluiedev](https://github.com/pluiedev))
  ```text
  Zig 0.17 has a really strict C flags parser for some reason, and the
  entire build fails if one dependency has an unrecognized C flag. Why?
  ```
- [`160093d`](https://github.com/ghostty-org/ghostty/commit/160093daa68972e69bf1a0e636a91118b7dde31b) build: update Zig dependencies ([@pluiedev](https://github.com/pluiedev))
- [`aa57f1f`](https://github.com/ghostty-org/ghostty/commit/aa57f1f41503139fd1cc388fb923de19977e7e91) build: port build script to Zig 0.17 ([@pluiedev](https://github.com/pluiedev))
  ```text
  https://ziglang.org/download/0.17.0/release-notes.html#Build-System
  
  https://ziglang.org/download/0.17.0/release-notes.html#Run-Step-Passthru-Args
  ```
- [`f987028`](https://github.com/ghostty-org/ghostty/commit/f987028f3fe414324da1597a25757d4c21d10c2d) treewide: `@intFromEnum` -> `@backingInt`, `@enumFromInt` -> `@fromBackingInt` ([@pluiedev](https://github.com/pluiedev))
  ```text
  https://ziglang.org/download/0.17.0/release-notes.html#toc-Added-codebackingIntcode-and-codefromBackingIntcode
  ```
- [`578d119`](https://github.com/ghostty-org/ghostty/commit/578d11956247c1a7dc7e46ef2439096a024f7b5d) treewide: `std.fmt.bufPrint{,Z,Sentinel}` -> `std.mem.print{,Sentinel}` ([@pluiedev](https://github.com/pluiedev))
- [`4f0d109`](https://github.com/ghostty-org/ghostty/commit/4f0d109f06ab373b00546a0b6b3953075ae2195e) treewide: nuke all uses of `**` ([@pluiedev](https://github.com/pluiedev))
- [`42c92b6`](https://github.com/ghostty-org/ghostty/commit/42c92b620e6acec5bf6953c4e1c9aa489b5cb918) treewide: Debug -> debug, ReleaseFast -> fast, etc. ([@pluiedev](https://github.com/pluiedev))
  ```text
  https://ziglang.org/download/0.17.0/release-notes.html#toc-Rename-codelangOptimizeModecode-to-codelangOptimizecode
  ```
- [`99d2583`](https://github.com/ghostty-org/ghostty/commit/99d258323d4a7f675a46aa7a45593df9dcdc393c) treewide: std.builtin -> std.lang ([@pluiedev](https://github.com/pluiedev))
- [`5158c4f`](https://github.com/ghostty-org/ghostty/commit/5158c4f6f2b2b24e5e99a5a0024abd4e3029ffba) treewide: .init(Empty|Full) -> .(empty|full) ([@pluiedev](https://github.com/pluiedev))
- [`1147e51`](https://github.com/ghostty-org/ghostty/commit/1147e516588e19205afd260b2b97dddba1899174) treewide: std.meta.field(Types|Names|Info) -> `@typeInfo` ([@pluiedev](https://github.com/pluiedev))
- [`95aad22`](https://github.com/ghostty-org/ghostty/commit/95aad22869ecd6c7329250b06e30e20476ac8dbb) treewide: migrate `@typeInfo` to Struct-Of-Arrays style ([@pluiedev](https://github.com/pluiedev))
  ```text
  https://ziglang.org/download/0.17.0/release-notes.html#toc-Struct-Of-Arrays-Style-for-codestdlangTypecode
  ```
- [`4892f50`](https://github.com/ghostty-org/ghostty/commit/4892f5013b374ef167ed06787c9fdae3b0febaf6) treewide: builtin.{cpu,os,abi} -> builtin.target.{cpu,os,abi} ([@pluiedev](https://github.com/pluiedev))
  ```text
  https://ziglang.org/download/0.17.0/release-notes.html#importbuiltin-Deprecations
  ```
- [`50a2c21`](https://github.com/ghostty-org/ghostty/commit/50a2c21de59d4e22d39f4ce3925cbf73193a1b9d) treewide: `std.fmt.allocPrint{,Sentinel}` -> `Allocator.print{,Sentinel}` ([@pluiedev](https://github.com/pluiedev))
  ```text
  https://ziglang.org/download/0.17.0/release-notes.html#toc-codefmtallocPrintcode-moved-to-codememAllocatorcode
  ```
- [`30d30aa`](https://github.com/ghostty-org/ghostty/commit/30d30aab066b234db07d7a4ee930e0c079101b69) treewide: `std.heap.stackFallback` -> `BufferFirstAllocator` ([@pluiedev](https://github.com/pluiedev))
  ```text
  https://ziglang.org/download/0.17.0/release-notes.html#StackFallbackAllocator-Reworked
  ```
- [`bb2a0fa`](https://github.com/ghostty-org/ghostty/commit/bb2a0fae2cb1b6755de12c9b615872a4b16cae90) treewide: std.{Static,Dynamic}BitSet -> std.bit_set.{Static,Dynamic} ([@pluiedev](https://github.com/pluiedev))
  ```text
  https://ziglang.org/download/0.17.0/release-notes.html#toc-Rename-codebit_setcode-Variants-and-Deprecate-the-Managed-One
  ```
- [`643898e`](https://github.com/ghostty-org/ghostty/commit/643898e687bd98b1358d0d7478ac00906fab577a) treewide: `DebugAllocator` -> `SafeAllocator` ([@pluiedev](https://github.com/pluiedev))
  ```text
  https://ziglang.org/download/0.17.0/release-notes.html#SafeAllocator-Introduced
  ```
- [`7ad29db`](https://github.com/ghostty-org/ghostty/commit/7ad29db6b0213bfc797c3eaaa0e961b4cd60f5d0) lib/TinyIo: sync with Zig 0.17 IO VTable ([@pluiedev](https://github.com/pluiedev))
  ```text
  A bunch of functions got removed. This is a good thing!
  ```
- [`57732c9`](https://github.com/ghostty-org/ghostty/commit/57732c93d219fa301de4b7860d1fd86997ffad60) treewide: `std.meta.Int` -> `@Int` ([@pluiedev](https://github.com/pluiedev))
- [`bef1bfb`](https://github.com/ghostty-org/ghostty/commit/bef1bfbb32485edcc67f562ef255a43191cfaac0) treewide: `Allocator.dupeZ` -> `Allocator.dupeSentinel` ([@pluiedev](https://github.com/pluiedev))
- [`e432c0a`](https://github.com/ghostty-org/ghostty/commit/e432c0a5bcfd45fbaf2bed3b02d310a6816809b4) renderer: SIMD vectors cannot appear in extern structs ([@pluiedev](https://github.com/pluiedev))
- [`ef349f7`](https://github.com/ghostty-org/ghostty/commit/ef349f7f6b81b0143068bcef89b34f497a40770c) renderer: atomics cannot be `@bitCast` into raw value ([@pluiedev](https://github.com/pluiedev))
  ```text
  Part of https://ziglang.org/download/0.17.0/release-notes.html#codebitCastcode-changes
  ```
- [`db2760d`](https://github.com/ghostty-org/ghostty/commit/db2760db041306185eb8b2db70e01722d200f5f6) crc32c: update to Zig 0.17 ([@pluiedev](https://github.com/pluiedev))
- [`bfbc895`](https://github.com/ghostty-org/ghostty/commit/bfbc8951cac853b61159c6d7cccfa4d7270691f3) treewide: miscellaneous Zig 0.17 changes ([@pluiedev](https://github.com/pluiedev))
  ```text
  https://ziglang.org/download/0.17.0/release-notes.html#codehasDeclcode-Returns-codetruecode-Only-for-Public-Declarations
  
  https://ziglang.org/download/0.17.0/release-notes.html#toc-Decouple-codeUricode-and-codenetHostNamecode
  ```
- [`3313085`](https://github.com/ghostty-org/ghostty/commit/331308587f23f5dee81125a03066209a86ad24f2) terminal: FailingAllocator behavioral changes ([@pluiedev](https://github.com/pluiedev))
  ```text
  Analysis by GLM 5.3 Flash:
  
  "In Zig 0.17, ArrayList growth goes through Allocator.remap, and
  FailingAllocator's remap/resize paths only honor resize_fail_index
  (default maxInt), never fail_index. So the growth succeeds in-place
  via remap, the induced alloc failure is never hit, and the code
  returns success (void) instead of OutOfMemory. The fix is to also
  arm resize_fail_index in these tests."
  ```
- [`8f78fe4`](https://github.com/ghostty-org/ghostty/commit/8f78fe4c179e3c5708b969e20a257f73487111da) snapshot/grid: fix corrupt metadata panic ([@pluiedev](https://github.com/pluiedev))
  ````text
  To be entirely honest I don't know how a human can debug this.
  From GLM 5.3 Flash:
  
  > `encodeNarrowStep` stores a `@Vector(size*4, u8)` shuffle result
  > through a pointer cast; Zig/LLVM compiled that 4-byte store as a full
  > 16-byte `vmovdqu`, overrunning the writer buffer by up to 12 bytes
  > whenever the last vector step landed at the buffer's end — clobbering
  > the SafeAllocator's footer and panicking on the next remap. Fixed by
  > materializing the shuffle result into a `[size*4]u8` array and copying
  > with an explicit-length `@memcpy` (verified by watchpoint that the
  > store is now exact). I also replaced the tail's overlapping vector
  > step (`encodeNarrowStep(words, count - 4, ...)`) with scalar writes,
  > which is simpler and avoids overlapping stores entirely.
  ```
  ````
- [`58f5a03`](https://github.com/ghostty-org/ghostty/commit/58f5a031fde9f6d2ede2895b146cb6f3068ddd73) build/GhosttyResources: explicitly list substituted variables ([@pluiedev](https://github.com/pluiedev))
  ```text
  Zig 0.17 made `Step.ConfigHeader` much stricter, as in compilation will
  fail when a variable gets unused.
  ```
- [`bdba842`](https://github.com/ghostty-org/ghostty/commit/bdba8422bc76c25d00c9fd5e5e542c0541609788) example: use addPassthruArgs ([@pluiedev](https://github.com/pluiedev))
- [`bd5f421`](https://github.com/ghostty-org/ghostty/commit/bd5f4216eff22807b8d3660afc4e083ac3198278) apple-sdk: remove Zig 0.16-specific workaround ([@pluiedev](https://github.com/pluiedev))
- [`bb440db`](https://github.com/ghostty-org/ghostty/commit/bb440db4c9d39df91e2aba2e42eea1df42d9cc3c) apple-sdk: fix header discovery in cross-compilation ([@pluiedev](https://github.com/pluiedev))
- [`cddba9a`](https://github.com/ghostty-org/ghostty/commit/cddba9a68a19ad097b65819f466e1a3fea83ecdb) build/XCFramework: explicitly install in prefix or in source tree ([@pluiedev](https://github.com/pluiedev))
  ```text
  The previous use of a simple string as the target path is bad for all
  sorts of reasons incl. caching and the fact that the install prefix
  is unknowable at configure time, so that has to go. This also has the
  added benefit of not requiring a manual delete step for the source_tree
  case since USF replaces the generated file.
  ```
- [`fab348f`](https://github.com/ghostty-org/ghostty/commit/fab348fd442484cb53a37fc9c3dc6d52a7c9d894) ci,flake: update names of Optimize modes ([@pluiedev](https://github.com/pluiedev))
  ```text
  Tests were failing because they can't find ReleaseFast anymore, which was
  admittedly very amusing
  ```
- [`b68ed39`](https://github.com/ghostty-org/ghostty/commit/b68ed392bfa2d36c05cea84a6c8cd9f1b090b470) highway: disable Zig-side stack protection on MSVC ([@pluiedev](https://github.com/pluiedev))
  ```text
  This somehow never triggered a CI failure with Zig 0.16. Odd!
  ```
- [`c0e8589`](https://github.com/ghostty-org/ghostty/commit/c0e8589c123e6af5f70645a9a7313909d6d6f12b) android-ndk: make libc.txt contain all fields ([@pluiedev](https://github.com/pluiedev))
  ```text
  Zig 0.17 is rather picky I see
  ```
- [`63153f7`](https://github.com/ghostty-org/ghostty/commit/63153f7ab5441b34ef22ac64a583e7b0700d7ba2) macos: replace extern struct bitcasts ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  Zig 0.17 no longer permits `@bitCast` involving extern structs. Convert
  CoreFoundation and CoreGraphics wrapper values by copying their fields
  explicitly.
  
  Avoid pointer-cast type punning so these conversions do not silently
  depend on wrapper and SDK types retaining identical padding, alignment,
  and layout.
  ```
- [`89cb6b7`](https://github.com/ghostty-org/ghostty/commit/89cb6b725738bb710f43b3eba406eff4fbc5684d) renderer/metal: use ABI-safe projection matrix ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  Zig 0.17 no longer permits vector fields in extern structs because
  vectors have no guaranteed memory representation. Store the Metal
  projection matrix as a scalar array, matching its MSL layout and the
  existing OpenGL representation.
  ```
- [`e4d7422`](https://github.com/ghostty-org/ghostty/commit/e4d7422ad32b8382b581a828b6e866837342fd57) build: resolve relative libsystem archive paths ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  Zig 0.17 supplies generated archive paths relative to the build root.
  Resolve them before entering the temporary directory so the override
  script continues to address the intended input and output archives.
  ```
- [`db5de6e`](https://github.com/ghostty-org/ghostty/commit/db5de6e5e86026ea03bec1cb53192a0809b1c6b0) build: update xcframework directory handling ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  Zig 0.17 requires directory inputs and outputs to be declared as such.
  Give the generated bundle its required extension, install it as a
  directory, and explicitly replace source-tree bundle outputs.
  ```
- [`e4c4567`](https://github.com/ghostty-org/ghostty/commit/e4c4567eb906d7686a2172972089bd0c46da17cf) apple-sdk: update stdout writer creation ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  The Zig 0.17 writer constructor returns a value directly and requires a
  mutable binding for writes. Remove the obsolete try and make the writer
  mutable so SDK-less Apple cross-compilation works again.
  ```
- [`06d22d5`](https://github.com/ghostty-org/ghostty/commit/06d22d5672b50ec3ea920b75f0061638f0c6a5a7) build: keep retargeted modules private ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  Retargeted modules are implementation details of universal library builds.
  Create them as private modules instead of registering architecture-based
  names that collide when multiple Apple platforms share an architecture.
  ```
- [`aa0e4c2`](https://github.com/ghostty-org/ghostty/commit/aa0e4c2f2ee4d7837c5922d9d55b116554bd21dc) build: fix pkg-config library selection ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  Select the shared and static library arguments in the correct modes and
  join argument lists with spaces. Shared consumers no longer attempt to
  link the relocated static archive.
  ```
- [`84c100f`](https://github.com/ghostty-org/ghostty/commit/84c100fe15d96f22dd4278e9c1456421939c898d) nix: patch Zig process replacement for iOS ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  Backport the upstream Zig fix that avoids instantiating unsupported Darwin
  process spawning code for iOS targets. This allows XCFramework C and C++
  sources to cross-compile with the pinned Zig 0.17 toolchain.
  ```
- [`f588912`](https://github.com/ghostty-org/ghostty/commit/f5889127938b2618a729fc575662f34447ce9f6e) ci: isolate LLVM-compatible AFL++ ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  Build AFL++ against LLVM 22 so it can consume bitcode emitted by Zig
  0.17. Keep this custom package in a dedicated fuzz development shell so
  unrelated CI jobs do not build it and exhaust smaller runners.
  ```
- [`ee8d209`](https://github.com/ghostty-org/ghostty/commit/ee8d209596a26cdf2384da026f2b14cf22277327) ci: ignore truncated patch context typo ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  The imported Zig patch has a truncated hunk header ending in "proces".
  Ignore that exact header so typos can continue checking the rest of the
  patch.
  ```
- [`4f2af6b`](https://github.com/ghostty-org/ghostty/commit/4f2af6b7b7b96959899dc4ae83e6f0809673956a) nix: limit GTK dev dependencies to Linux ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  The development shell previously included GTK, libadwaita, and the
  Blueprint compiler on macOS solely to support source tarball creation.
  Those tarballs are produced by Linux CI jobs.
  
  Keep the tooling in the Linux shell while avoiding its large dependency
  closure for macOS builds and tests.
  
  Amp-Thread-ID: T-01a10d3c-97d3-722f-a89c-71d962238f4d
  ```
- [`6dc48fc`](https://github.com/ghostty-org/ghostty/commit/6dc48fc18de8663ae0b02f4867173ebd799d15fb) nix: remove obsolete WABT dependency ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  Commit 01a8ea721 (build: binary patching with Zig) replaced the
  wasm2wat and wat2wasm pipeline with a native Zig binary patcher. No
  callers remain, so remove WABT from the development shell.
  ```
- [`99d593d`](https://github.com/ghostty-org/ghostty/commit/99d593da2feb14e709326edb5dba2dfe8006692c) nix: remove unused Wasmtime CLI ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  Commit 8bf5c4ed7 (the build.zig refactor) removed the broken WASM build
  and its test-wasm step, the last caller of the standalone Wasmtime CLI.
  ABI manifest verification uses the Python wasmtime module instead,
  which remains in the development shell.
  ```
- [`bf94988`](https://github.com/ghostty-org/ghostty/commit/bf949882d291539c89c5fb726cc554818bf7a568) nix: remove unused scdoc dependency ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  scdoc was added with the initial Nix shell in commit f8b000044, but
  that tree contained no scdoc input or invocation and no caller has been
  added since. Ghostty now generates its documentation with Pandoc, so
  remove the stale development dependency.
  ```
- [`923d863`](https://github.com/ghostty-org/ghostty/commit/923d8633b4ca6e425d1b07768c8c3768fac59d78) build: always delete and rebuild xcframework ([@bo2themax](https://github.com/bo2themax))
- [`4280d32`](https://github.com/ghostty-org/ghostty/commit/4280d32d230ce2d0f844c6dc6bd96cc04dc43482) nix: remove obsolete LLVM dependency ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  Commit 2d3126ffb added LLVM to provide llvm-lipo for combining the two
  cross-compiled macOS binaries. Commit d0f82f96a switched releases to
  native Xcode builds and removed that final caller, leaving the latest
  LLVM package unused. The LLVM 22 package for Linux AFL++ remains.
  ```
- [`3a875d9`](https://github.com/ghostty-org/ghostty/commit/3a875d95e241f38c21649b0389a97795b5d25aa0) build: cache xcframework ([#14646](https://github.com/ghostty-org/ghostty/issues/14646)) ([@bo2themax](https://github.com/bo2themax))
- [`0ecfea7`](https://github.com/ghostty-org/ghostty/commit/0ecfea767e789aee774b018d6cb31af4d4069232) simd: construct decoder test fixtures at comptime ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  Runtime codegen for `std.simd.repeat` in the decoder tests hangs
  LLVM's AArch64 Debug legalizer with Zig 0.17.
  
  Evaluate the repeated strings at comptime to avoid generating the
  problematic vector shuffles. Production SIMD code, runtime safety,
  and optimization settings remain unchanged.
  ```
- [`39b07b2`](https://github.com/ghostty-org/ghostty/commit/39b07b2b9319a322d81247dacc66ee447401c92b) mirror our deps ([@mitchellh](https://github.com/mitchellh))
- [`8b8aa5d`](https://github.com/ghostty-org/ghostty/commit/8b8aa5d88e0a8d97a49058a0590d7204bb281adc) fix cache hashes ([@mitchellh](https://github.com/mitchellh))
- [`f8d4724`](https://github.com/ghostty-org/ghostty/commit/f8d472466f76e728be7a24858a214ddfe970bf93) core: fix stray zig 0.17 syntax change ([@mitchellh](https://github.com/mitchellh))
- [`3d07ef9`](https://github.com/ghostty-org/ghostty/commit/3d07ef9e28c4af05065b9e2e546b8ac8f9b62df0) Update to Zig 0.17 ([#14519](https://github.com/ghostty-org/ghostty/issues/14519)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Closes #14518
  
  Most of the diff is just extremely boring mechanical manipulation.
  
  **AI notice**: Some mechanical changes implemented by Deepseek v4.1
  Flash
  ```
- [`8904e32`](https://github.com/ghostty-org/ghostty/commit/8904e328411082c3549fc263cf11d9a74a87ddee) libghostty-vt: add a Kitty graphics animation tick to the C API ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds `ghostty_kitty_graphics_animation_tick`, which advances every
  playing Kitty graphics animation to the frame due at the given time and
  returns the absolute time the next frame is due. It returns
  `GHOSTTY_NO_VALUE` when nothing is playing, so embedders schedule a
  single redraw for the returned time instead of polling.
  ```
- [`a84a070`](https://github.com/ghostty-org/ghostty/commit/a84a0703082dfc6dcef7b985266aa2f0827fdd67) libghostty-vt: add a Kitty graphics animation tick to the C API ([#14776](https://github.com/ghostty-org/ghostty/issues/14776)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds `ghostty_kitty_graphics_animation_tick`, which advances every
  playing Kitty graphics animation to the frame due at the given time and
  returns the absolute time the next frame is due. It returns
  `GHOSTTY_NO_VALUE` when nothing is playing, so embedders schedule a
  single redraw for the returned time instead of polling.
  ```
- [`b58ef1d`](https://github.com/ghostty-org/ghostty/commit/b58ef1d678be2747c830bc1b1e6c0a086afecf9a) Update VOUCHED list ([#14772](https://github.com/ghostty-org/ghostty/issues/14772)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14418#discussioncomment-19055528)
  from @jcollie.
  
  Vouch: @neobrain
  ```

## October 19, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/39261955893), [2](https://github.com/ghostty-org/ghostty/actions/runs/39185729191), [3](https://github.com/ghostty-org/ghostty/actions/runs/39178943848)  
Summary: 3 runs • 17 commits • 6 authors

### Changes

- [`152bdbc`](https://github.com/ghostty-org/ghostty/commit/152bdbc68075ee4bc5b4745fb908598a16fc628c) formatter: restore blank cells and erased backgrounds in VT output ([@robmorgan](https://github.com/robmorgan))
  ```text
  VT output wrote the empty cells of a gap between text as spaces, in the
  pen of the text before the gap, so replaying it turned them into text
  and painted that text's background into the gap. Cells that only carry
  a background (erased while a background color was set) were written as
  spaces too, and rows of only those were dropped as blank, losing the
  color.
  
  VT output now steps over the empty cells of a gap with CUF. Cells that
  only carry a background are recreated as they were made: a run of the
  same background is erased with ECH under that background, then stepped
  over. Rows of them are no longer treated as blank. Blanks carried over
  from a wrapped row when unwrapping can't be stepped over, since CUF
  stops at the end of the row, so they are still spaces, but no longer in
  the pen of the text before them.
  
  An open hyperlink is no longer closed and reopened around a gap: stepping
  over the cells doesn't write them, so the link doesn't reach them.
  ```
- [`bd1c9cc`](https://github.com/ghostty-org/ghostty/commit/bd1c9cc8cb2cad3cd949fcc566872174f306821b) formatter: keep trailing blank rows in VT output without trimming ([@robmorgan](https://github.com/robmorgan))
  ```text
  VT output left out the blank rows at the end of the formatted range,
  even with trimming off. They are part of the screen's layout: a replay
  without them scrolls less, so whenever there is scrollback the rows
  above them end up too low. After clearing below a prompt, say, the
  prompt comes back on the bottom row with older output above it.
  
  VT output without trimming now ends with a newline for each of those
  rows, mapped in the pin map to the row it ends, as between rows. Trimmed
  output and the other formats still drop them.
  ```
- [`1cd6d0b`](https://github.com/ghostty-org/ghostty/commit/1cd6d0b74ec515fc690450732fa3a9f6df8fa758) terminal/kitty: accept shared memory names without a leading slash ([@davidhodge](https://github.com/davidhodge))
  ```text
  Since 090fca451d, `t=s` names must start with a slash and contain no
  other slash. Sandboxed macOS apps can't create such names: the App
  Sandbox only allows POSIX shared memory named `<app group id>/<name>`,
  with no leading slash. So every sandboxed client was refused.
  
  kitty hit the same thing and relaxed it in kovidgoyal/kitty@2efa09d.
  The protocol spec now says terminals must accept names without a
  leading slash and pass them unmodified to shm_open and shm_unlink.
  
  Only reject clearly malformed names: empty, containing NUL, or longer
  than NAME_MAX. Slashes are left to shm_open, since the valid forms are
  platform specific (Darwin's namespace is flat, glibc and musl reject
  any slash after the leading ones).
  
  Fixes #14744
  ```
- [`0bb2c91`](https://github.com/ghostty-org/ghostty/commit/0bb2c910df7308bb1dab743a49c535458783cc67) terminal/kitty: reject a bare slash shm name, document unlink behavior ([@davidhodge](https://github.com/davidhodge))
  ```text
  Reject "/" as a shared memory name again, as before. Also note where
  we unlink the object that Ghostty unlinks whatever name the client
  sends, so a client can remove any shared memory object Ghostty can
  open, including another app group's if it can guess the name. This
  isn't new, but it's worth writing down.
  ```
- [`33111db`](https://github.com/ghostty-org/ghostty/commit/33111db3175e2261bd6ff087836b8532975eae29) core: size click_state to hold every mouse button ([@jcollie](https://github.com/jcollie))
  ```text
  MouseButton.max is the largest enum value (11), not a count, so an
  array of that length has no slot for .eleven. Recording a press or
  release of button 11 indexed past the end, which panics in safe builds.
  
  Size the array max + 1 and correct the doc comment on max that
  suggested using it directly as an array length.
  ```
- [`53fb05c`](https://github.com/ghostty-org/ghostty/commit/53fb05c6eba4e678c9a70f76bd828b74625c32d3) terminal: stop CUB and BS at the left margin ([@jcollie](https://github.com/jcollie))
  ```text
  With reverse wrap off, cursorLeft took a fast path that clamped only at
  column zero and ignored DECSLRM's left margin, so CUB and BS moved the
  cursor past it. Clamp to the left margin there as the reverse-wrap path
  and cursorRight already do, unless the cursor is already left of it.
  
  Fixes esctest's test_BS_StopsAtLeftMargin and
  test_CUB_StopsAtLeftMarginInScrollRegion.
  ```
- [`82df0be`](https://github.com/ghostty-org/ghostty/commit/82df0be2c7522d2285187db863d62e9366fd9c4c) terminal: keep CHA, VPA, HPR and VPR origin-relative ([@jcollie](https://github.com/jcollie))
  ```text
  In origin mode setCursorPos takes coordinates relative to the scrolling
  region, but the stream handlers for CHA/HPA, VPA, HPR and VPR built them
  from the cursor's absolute screen position. The coordinate each meant to
  keep, or move relative to, then had the margin offset added a second
  time.
  
  Add setCursorRow, setCursorCol, cursorRowRelative and cursorColRelative
  to Terminal, which convert the cursor position into origin-relative
  coordinates first, as xterm's CursorRow and CursorCol do, and use them
  from both stream handlers.
  
  Fixes esctest's test_CHA_RespectsOriginMode, test_HPR_IgnoresOriginMode
  and test_VPR_IgnoresOriginMode.
  ```
- [`71c1e67`](https://github.com/ghostty-org/ghostty/commit/71c1e67a00f6919640084e9896b49354a9c9582a) terminal/kitty: address review feedback on the shm round-trip test ([@davidhodge](https://github.com/davidhodge))
  ```text
  Use bufPrintSentinel since bufPrintZ is removed in Zig 0.17. Always
  unlink the test object with a plain defer, and drop an unneeded @as.
  
  Check that the terminal unlinked the object by trying to reopen it
  rather than by unlinking it again, so the check has no side effects.
  fstat can't be used for this because macOS always reports st_nlink 0
  for shared memory objects.
  ```
- [`d7a0bd9`](https://github.com/ghostty-org/ghostty/commit/d7a0bd96fe7dfa09701bb0e768dd8bf418e1dcaa) terminal/kitty: accept shared memory names without a leading slash ([#14750](https://github.com/ghostty-org/ghostty/issues/14750)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #14744
  
  Since 090fca451d, `t=s` names must start with `/` and contain no other
  `/`. A sandboxed macOS app can only create POSIX shared memory named
  `<app group id>/<name>`, with no leading slash, so every sandboxed
  client is refused with `EINVAL: invalid data`.
  
  kitty relaxed the same check in kovidgoyal/kitty@2efa09d, and the
  protocol spec now says terminals must accept names without a leading
  slash and pass them unmodified to `shm_open()`/`shm_unlink()`.
  
  `validSharedMemoryName` now only rejects empty names, names containing
  NUL, and names longer than `NAME_MAX`. Slashes are left to `shm_open`,
  because what's valid depends on the platform: Darwin's namespace is
  flat, and glibc and musl reject any slash after the leading ones. This
  matches kitty, which never checked for inner slashes. It also means
  `/a/b` is accepted again, as it was before 090fca451d. On Linux it still
  fails in `shm_open`.
  
  Tests:
  - Updated the name unit test.
  - The NUL case still goes through `LoadingImage.init` and is rejected.
  - New round-trip test: it creates a real shm object
  (`ghostty.test/shm-<pid>` on macOS, `ghostty-test-shm-<pid>` elsewhere),
  loads it with `t=s`, and checks the bytes and that the terminal unlinked
  it. It fails on main with `InvalidData`.
  
  Tested on macOS (M5, Zig 0.16.0) with `zig build test
  -Dtest-filter="shared memory"`, `-Dtest-filter=kitty` and `zig build
  test-lib-vt -Dtest-filter="shared memory"`, plus a full `zig build`. A
  small C program against libghostty-vt sends `a=t,t=s` for
  `F2RRU25WBT.sr/e2e<pid>`. With this change the image is stored with OK;
  on main it gets `EINVAL: invalid data`.
  
  AI disclosure: written with Claude Code. It wrote the fix and tests, ran
  the tests and the libghostty-vt check above, and drafted this
  description; a second Claude Code pass reviewed the diff. I reviewed and
  understand the change.
  ```
- [`7c9b7da`](https://github.com/ghostty-org/ghostty/commit/7c9b7da47f82b97c6b540d72703f7b05534dfec4) core: size click_state to hold every mouse button ([#14759](https://github.com/ghostty-org/ghostty/issues/14759)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  MouseButton.max is the largest enum value (11), not a count, so an array
  of that length has no slot for .eleven. Recording a press or release of
  button 11 indexed past the end, which panics in safe builds.
  
  Size the array max + 1 and correct the doc comment on max that suggested
  using it directly as an array length.
  
  AI disclosure: Claude Code was used in the preparation of this PR
  ```
- [`63fd4ea`](https://github.com/ghostty-org/ghostty/commit/63fd4eab8267b4f307289bbf0a9d1a4b3e35a5b8) terminal: stop CUB and BS at the left margin ([#14761](https://github.com/ghostty-org/ghostty/issues/14761)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  With reverse wrap off, cursorLeft took a fast path that clamped only at
  column zero and ignored DECSLRM's left margin, so CUB and BS moved the
  cursor past it. Clamp to the left margin there as the reverse-wrap path
  and cursorRight already do, unless the cursor is already left of it.
  
  Fixes esctest's test_BS_StopsAtLeftMargin and
  test_CUB_StopsAtLeftMarginInScrollRegion.
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`746c895`](https://github.com/ghostty-org/ghostty/commit/746c895c6f77a76309783fc1f05c69665219c733) terminal: keep CHA, VPA, HPR and VPR origin-relative ([#14762](https://github.com/ghostty-org/ghostty/issues/14762)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  In origin mode setCursorPos takes coordinates relative to the scrolling
  region, but the stream handlers for CHA/HPA, VPA, HPR and VPR built them
  from the cursor's absolute screen position. The coordinate each meant to
  keep, or move relative to, then had the margin offset added a second
  time.
  
  Add setCursorRow, setCursorCol, cursorRowRelative and cursorColRelative
  to Terminal, which convert the cursor position into origin-relative
  coordinates first, as xterm's CursorRow and CursorCol do, and use them
  from both stream handlers.
  
  Fixes esctest's test_CHA_RespectsOriginMode, test_HPR_IgnoresOriginMode
  and test_VPR_IgnoresOriginMode.
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`891a4db`](https://github.com/ghostty-org/ghostty/commit/891a4dba5757f7bd4db0e927d0d68032320783ff) formatter: restore blank cells and erased backgrounds in VT output ([#14725](https://github.com/ghostty-org/ghostty/issues/14725)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  VT output loses two kinds of blank cells, so replaying it doesn't
  recreate the original screen properly:
  
  1. **Gaps between text.** Empty cells between two pieces of text on a
  row (left by a cursor movement, for example) are written as spaces, in
  the pen of the text before them. Replaying the output turns them into
  text and paints that text's background into the gap. For example,
  `\x1b[41mred\x1b[0m\x1b[10Gplain` comes back with a red bar between the
  two words.
  2. **Cells that only have a background.** Erasing while a background
  color is set (`EL`, `ED`, `ECH`) leaves cells with no text, only a
  background color. These are written as spaces, and a row made only of
  them is treated as blank and dropped, so a full-width colored status bar
  or a cleared colored screen loses its color.
  
  TUIs are doing this all the time - think status lines, panes,
  highlighted rows in vim/nvim, Claude Code, Codex etc. They are mostly
  colored erases and gaps.
  
  ### Changes
  
  Here's what I've done:
  
  - Gaps are stepped over with CUF (`\x1b[nC`), which moves the cursor
  without writing anything, so the cells stay empty.
  - A run of cells that share one background is recreated the way it was
  made: `ECH` under that background, then CUF over the run. HTML output is
  unchanged and still writes a space in the background's style.
  - Rows of background-only cells are no longer treated as blank in VT
  output.
  - When unwrapping, blanks carried over from the end of a wrapped row
  can't be stepped over, because CUF stops at the end of the row. They are
  still written as spaces, but with the style closed first, so they no
  longer take the pen of the text before them. The same goes for an open
  hyperlink.
  
  Side effect: An open hyperlink is no longer closed and reopened around a
  gap. Why? stepping over the cells doesn't write them, so the link
  doesn't reach them. This changes the expected output of a test I added
  in #14711.
  
  ### Benchmarks
  
  The first two rows use a generated TUI-like corpus with gaps, colored
  `EL` and colored full-row clears. The last two use the output of
  `ghostty-gen +styled`, which has no gaps.
  
  | Corpus | main | this PR | Change |
  |---|---|---|---|
  | TUI-like | 3.91 ms | 3.53 ms | −9.6% |
  | TUI-like, pin map | 5.12 ms | 4.45 ms | −13% |
  | styled | 2.52 ms | 2.50 ms | about the same |
  | styled, pin map | 3.85 ms | 3.79 ms | about the same |
  
  On the TUI-like corpus the output is 21% smaller (962,370 → 762,173
  bytes), since a CUF is shorter than a run of spaces. On corpora without
  gaps or erased backgrounds the output is byte-identical to `main`.
  
  AI disclosure: Created with help from Claude Code using Opus 5.5,
  Iterated on, manually tested and reviewed by me.
  ```
- [`c7cbc9b`](https://github.com/ghostty-org/ghostty/commit/c7cbc9bfd44cb11a9c7eae00f1166624671e363b) formatter: keep trailing blank rows in VT output without trimming ([#14766](https://github.com/ghostty-org/ghostty/issues/14766)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  VT output currently leaves out the blank rows at the end of the
  formatted range, even with trimming off. Because VT is the only output
  that gets replayed into the terminal, it means a replay without them
  scrolls less, so whenever there is scrollback the rows above them end up
  too low.
  
  For example, on a 5-row screen with three lines in scrollback,
  `\x1b[3;1H\x1b[J` (clear below the second row) leaves `4`, `5` and three
  blank rows. Replaying the VT output shows `1 2 3 4 5` instead: the three
  blank rows are missing, so `1` to `3` never scroll off. The same happens
  to a shell prompt after clearing below it and it comes back on the
  bottom row with older output above it.
  
  **Note:** this changes output for existing callers that ask for vT with
  trim off. They will now get line breaks, they didn't before. Personally,
  I think that's the right behavior, since asking for exact layout is the
  point of turning trim off and the description says so.
  
  ### Reproduce
  
  I have a small Go program using Mitchell's SDK. I can also remove the
  middle-man if desired, but I've tested and the bug occurs in `main`:
  
  ```go
  // rowsdemo shows the trailing blank rows bug in the real terminal it runs in.
  //
  //    rowsdemo           # writes the input straight to this terminal (the original)
  //    rowsdemo -replay   # feeds it to libghostty and replays the VT snapshot instead
  //
  // Both clear the screen and scrollback first, then wait for Enter.
  package main
  
  import (
        "bufio"
        "flag"
        "fmt"
        "os"
  
        "go.mitchellh.com/libghostty"
        "golang.org/x/term"
  )
  
  func main() {
        replay := flag.Bool("replay", false, "replay the VT snapshot instead of the input")
        flag.Parse()
  
        cols, rows, err := term.GetSize(int(os.Stdout.Fd()))
        check(err)
  
        // Enough output to fill the screen and push some into scrollback, then
        // clear below the second row and print a prompt, as a shell does after
        // clearing below the cursor.
        var input []byte
        for i := 1; i <= rows+10; i++ {
                input = fmt.Appendf(input, "output line %d\r\n", i)
        }
        input = append(input, "\x1b[3;1H\x1b[J$ the prompt is here"...)
  
        out := input
        if *replay {
                t, err := libghostty.NewTerminal(libghostty.WithSize(uint16(cols), uint16(row
                check(err)
                t.VTWrite(input)
                f, err := libghostty.NewFormatter(t,
                        libghostty.WithFormatterFormat(libghostty.FormatterFormatVT),
                        libghostty.WithFormatterTrim(false),
                        libghostty.WithFormatterUnwrap(false),
                        libghostty.WithFormatterExtraCursor(true),
                        libghostty.WithFormatterExtraStyle(true),
                )
                check(err)
                out, err = f.Format()
                check(err)
        }
  
        os.Stdout.WriteString("\x1b[H\x1b[2J\x1b[3J")
        os.Stdout.Write(out)
        bufio.NewReader(os.Stdin).ReadString('\n')
        os.Stdout.WriteString("\x1b[H\x1b[2J\x1b[3J")
  }
  
  func check(err error) {
        if err != nil {
                fmt.Fprintln(os.Stderr, "rowsdemo:", err)
                os.Exit(2)
        }
  }
  ```
  
  ### Benchmarks
  
  I didn't benchmark this one as the only cost is a few `\r\n` written
  once at the end of the output.
  
  AI disclosure: Created with help from Claude Code using Opus 5.5,
  Iterated on, manually tested and reviewed by me.
  ````
- [`9860397`](https://github.com/ghostty-org/ghostty/commit/98603976e9cfd643ab5dec78be5fd06ea8dbec74) build(deps): bump cachix/install-nix-action from 31.11.1 to 31.11.2 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [cachix/install-nix-action](https://github.com/cachix/install-nix-action) from 31.11.1 to 31.11.2.
  - [Release notes](https://github.com/cachix/install-nix-action/releases)
  - [Changelog](https://github.com/cachix/install-nix-action/blob/master/RELEASE.md)
  - [Commits](https://github.com/cachix/install-nix-action/compare/13d8dd58da0234aa297dedd986986ccb8e7f3e24...448cde739abec1eaf0646249e3d25bb8d9bc7702)
  
  ---
  updated-dependencies:
  - dependency-name: cachix/install-nix-action
    dependency-version: 31.11.2
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`765ea37`](https://github.com/ghostty-org/ghostty/commit/765ea37ad64f7e3a48f6ac27a70ad7fb6f31b9bb) build(deps): bump cachix/install-nix-action from 31.11.1 to 31.11.2 ([#14765](https://github.com/ghostty-org/ghostty/issues/14765)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [cachix/install-nix-action](https://github.com/cachix/install-nix-action)
  from 31.11.1 to 31.11.2.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/cachix/install-nix-action/releases">cachix/install-nix-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v31.11.2</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>nix: 2.35.2 -&gt; 2.35.3 by <a
  href="https://github.com/github-actions"><code>@​github-actions</code></a>[bot]
  in <a
  href="https://redirect.github.com/cachix/install-nix-action/pull/282">cachix/install-nix-action#282</a>
  <strong>Security</strong>: Fixes a number of vulnerabilities that could
  be combined to achieve root priviledge escalation.
  See <a
  href="https://discourse.nixos.org/t/security-advisory-for-nix-and-lix-october-2026/80547">https://discourse.nixos.org/t/security-advisory-for-nix-and-lix-october-2026/80547</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/cachix/install-nix-action/compare/v31.11.1...v31.11.2">https://github.com/cachix/install-nix-action/compare/v31.11.1...v31.11.2</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/448cde739abec1eaf0646249e3d25bb8d9bc7702"><code>448cde7</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/install-nix-action/issues/282">#282</a>
  from cachix/create-pull-request/patch</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/280a41184aaf35a185e673c5fb4412df02ee80e8"><code>280a411</code></a>
  nix: 2.35.2 -&gt; 2.35.3</li>
  <li>See full diff in <a
  href="https://github.com/cachix/install-nix-action/compare/13d8dd58da0234aa297dedd986986ccb8e7f3e24...448cde739abec1eaf0646249e3d25bb8d9bc7702">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=cachix/install-nix-action&package-manager=github_actions&previous-version=31.11.1&new-version=31.11.2)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`06d872f`](https://github.com/ghostty-org/ghostty/commit/06d872fa663ba1edab65126ddbb2705c0d565468) Sync CODEOWNERS vouch list ([#14764](https://github.com/ghostty-org/ghostty/issues/14764)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Sync CODEOWNERS owners with vouch list.
  
  ## Added Users
  
  - @complexsplit
  - @Pugma
  ```

## October 18, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/39163290389), [2](https://github.com/ghostty-org/ghostty/actions/runs/39155084891), [3](https://github.com/ghostty-org/ghostty/actions/runs/39146825669), [4](https://github.com/ghostty-org/ghostty/actions/runs/39104821716), [5](https://github.com/ghostty-org/ghostty/actions/runs/39100383906), [6](https://github.com/ghostty-org/ghostty/actions/runs/39100309164), [7](https://github.com/ghostty-org/ghostty/actions/runs/39098494353), [8](https://github.com/ghostty-org/ghostty/actions/runs/39084774558)  
Summary: 8 runs • 15 commits • 6 authors

### Changes

- [`72e5434`](https://github.com/ghostty-org/ghostty/commit/72e543435103cdedafb115ec690b8661fb4b6123) gtk: keep IME cursor location updated during preedit ([@moonward](https://github.com/moonward))
  ```text
  Add updateImePosition(), the only place that reports the cursor
  location to GTK.
  
  - Call updateImePosition() on preedit start/change and focus-in, in
    addition to key events.
  - Report a rectangle that spans the full cell height.
  - Correct the position from imePoint() for the gtk-xft-dpi scale.
  
  Details: https://github.com/ghostty-org/ghostty/discussions/14066
  ```
- [`6417d30`](https://github.com/ghostty-org/ghostty/commit/6417d3023e57151a2e5ec01d150b8145c9454aae) gtk: use imePointScaled to get widget coordinates ([@moonward](https://github.com/moonward))
  ```text
  Add imePointScaled(), which divides our sizes by the given scale
  instead of the content scale. imePoint() calls it with the content
  scale, so its result does not change.
  
  Make updateImePosition() call imePointScaled() with the surface scale,
  so it no longer has to undo the font DPI scale.
  ```
- [`d8619f1`](https://github.com/ghostty-org/ghostty/commit/d8619f1bce383090260221dab5f62fc953d1280b) gtk: keep IME cursor location updated during preedit on Wayland ([#14729](https://github.com/ghostty-org/ghostty/issues/14729)) ([@jcollie](https://github.com/jcollie))
  ```text
  This PR is to fix the issues of IME candidate window placement on
  Wayland as discussed in:
  
  https://github.com/ghostty-org/ghostty/discussions/14066#discussioncomment-18851489
  
  ### Fix
  Add updateImePosition() as the single place that reports the correct
  cursor location to GTK.
  Changes are:
  - Call updateImePosition() on preedit start/change and focus-in, in
  addition to key events.
  - Report a rectangle that spans full cell height so a candidate window
  flipped above the cursor does not cover the line being edited.
  - Correct the position from imePoint() for gtk-xft-dpi scale.
  
  ### Verification
  Unpatched builds reproduce the issues, and with the patch the candidate
  window appears next to the preedit without covering it, on Hyprland
  (fcitx5: mozc, hazkey, Rime), KWin (fcitx5, ibus) and GNOME (ibus), all
  on CachyOS. (refer to Examples section in the above link.)
  
  ### Related
  #13396, #13395, #5645 (X11, i3), #13015 (Xft.dpi=120). #5645 looks like
  the bottom-row case and #13015 like the text-scaling case, but I have
  not tested on a native X11 session. tomocrafter independently proposed
  the same full-cell-height change in #14267.
  
  ### AI Disclosure
  I used Claude Code (Fable 5 / Sonnet 5.5) to help with investigation,
  implementation and testing, Opus 5.5 for code review, and GPT5.6/6 sol
  for some automated tests. I reviewed the code, tested on real devices,
  and edited this text myself.
  ```
- [`189af86`](https://github.com/ghostty-org/ghostty/commit/189af86eac5e91e1b282bdaf371f369c3863591f) Update VOUCHED list ([#14760](https://github.com/ghostty-org/ghostty/issues/14760)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14755#discussioncomment-19022050)
  from @jcollie.
  
  Vouch: @aredmondd
  ```
- [`431126c`](https://github.com/ghostty-org/ghostty/commit/431126c215dc324a53ef6f054264e951a4b21604) Update VOUCHED list ([#14756](https://github.com/ghostty-org/ghostty/issues/14756)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14723#discussioncomment-19020874)
  from @pluiedev.
  
  Denounce: @gotar
  ```
- [`c8c481c`](https://github.com/ghostty-org/ghostty/commit/c8c481c1750033ad21f4f34718f5d0b1906ec251) fix(nix): prioritize pinned Zig in the macOS dev shell ([@ekusiadadus](https://github.com/ekusiadadus))
- [`d2865b8`](https://github.com/ghostty-org/ghostty/commit/d2865b8f578fa4e85e2f2b85ef97f5ef69de951f) nix: prioritize pinned Zig in the macOS dev shell ([#14692](https://github.com/ghostty-org/ghostty/issues/14692)) ([@jcollie](https://github.com/jcollie))
  ```text
  The macOS shell hook prepends Homebrew directories to PATH ahead of
  the Nix-provided tools. When Zig is also installed through Homebrew,
  the dev shell uses that version instead of the version pinned by the
  flake, which can cause builds to fail.
  
  Prepend `${zig}/bin` to PATH so the dev shell uses the project's pinned
  Zig while preserving the existing precedence for LLVM and Apple tools.
  
  Verified on macOS with Homebrew Zig 0.17.0 installed:
  - Before: `direnv exec . zig version` returned `0.17.0`.
  - After: the same command returned the pinned `0.16.0`.
  ```
- [`f44c678`](https://github.com/ghostty-org/ghostty/commit/f44c67817d1869cd1ff3cbd648552e4c7ac9ba23) Update VOUCHED list ([#14748](https://github.com/ghostty-org/ghostty/issues/14748)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14734#discussioncomment-19012178)
  from @jcollie.
  
  Vouch: @locriani
  ```
- [`0e6afb2`](https://github.com/ghostty-org/ghostty/commit/0e6afb2600d4f8be736ec94b44a21ba8d608921e) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`5c93856`](https://github.com/ghostty-org/ghostty/commit/5c93856710d09f313aae515aaac207981f64a528) Update iTerm2 colorschemes ([#14740](https://github.com/ghostty-org/ghostty/issues/14740)) ([@jcollie](https://github.com/jcollie))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20261012-151317-d3e95e4
  ```
- [`fb3373c`](https://github.com/ghostty-org/ghostty/commit/fb3373c8b52ffdd0669ae2d585ed0f9f7f1107fa) Update VOUCHED list ([#14747](https://github.com/ghostty-org/ghostty/issues/14747)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14690#discussioncomment-19012170)
  from @jcollie.
  
  Vouch: @Davey-Hughes
  ```
- [`8f77be7`](https://github.com/ghostty-org/ghostty/commit/8f77be73d2b525dff30f1d1a50c3523a27a3d095) Update VOUCHED list ([#14745](https://github.com/ghostty-org/ghostty/issues/14745)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14743#discussioncomment-19011080)
  from @jcollie.
  
  Vouch: @zzznu
  ```
- [`71970ee`](https://github.com/ghostty-org/ghostty/commit/71970eee87936dfe16ccc7cddceee07fcc7aa64b) Update VOUCHED list ([#14746](https://github.com/ghostty-org/ghostty/issues/14746)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14742#discussioncomment-19011082)
  from @jcollie.
  
  Vouch: @davidhodge
  ```
- [`23dd1b7`](https://github.com/ghostty-org/ghostty/commit/23dd1b723e8314e34f56042e2af1e7653f47b2e5) gtk: stop progress bar pulse animation ([@dkinzler](https://github.com/dkinzler))
  ```text
  Fixes #14704.
  
  Explicitly stop the pulse animation when the progress bar of a Surface
  widget is removed. Previously its tick callback kept running and
  continuously queued redraws. This kept the GTK main loop busy even when
  the progress bar was not visible and the window not focused.
  ```
- [`73e4ff1`](https://github.com/ghostty-org/ghostty/commit/73e4ff10fb2b30d1ab6e6f7f52ef33f3a0593dcc) gtk: stop progress bar pulse animation ([#14738](https://github.com/ghostty-org/ghostty/issues/14738)) ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes #14704.
  
  Explicitly stop the pulse animation when the progress bar of a Surface
  widget is removed. Previously its tick callback kept running and
  continuously queued redraws. This kept the GTK main loop busy even when
  the progress bar was not visible and the window not focused.
  
  The issue can be reproduced by sending ConEmu OSC 9;4 progress reports.
  First one with state "undetermined" (`printf '\e]9;4;3\e\x5c'`) to show
  the progress bar and start the pulse animation, then one with "inactive"
  (`printf '\e]9;4;0\e\x5c'`) to remove it. Unfocus the window and observe
  the amount of main loop iterations e.g. with debug logs in the `run`
  function in `apprt/gtk/class/application.zig`. With the fix there is ~1
  iteration per second, without it there are lots.
  
  AI Disclosure: no AI used on this one.
  ```

## October 16, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/38951024014), [2](https://github.com/ghostty-org/ghostty/actions/runs/38943108606), [3](https://github.com/ghostty-org/ghostty/actions/runs/38936269574)  
Summary: 3 runs • 3 commits • 3 authors

### Changes

- [`e3ebb1d`](https://github.com/ghostty-org/ghostty/commit/e3ebb1d1bf772cf5d1bc70b5ae19e6943e33a110) Catalan translation of command palette ([#13776](https://github.com/ghostty-org/ghostty/issues/13776)) ([@francescarpi](https://github.com/francescarpi))
- [`22d623f`](https://github.com/ghostty-org/ghostty/commit/22d623f38aeea55deb6191ca64c7b9d02922980e) I18n: update `id_ID` translations for v1.4 ([#13905](https://github.com/ghostty-org/ghostty/issues/13905)) ([@halosatrio](https://github.com/halosatrio))
- [`949149d`](https://github.com/ghostty-org/ghostty/commit/949149d5791a0eb08412ad05cd8fd484ad134481) i18n: complete missing Japanese translations ([#14575](https://github.com/ghostty-org/ghostty/issues/14575)) ([@ekusiadadus](https://github.com/ekusiadadus))
  ```text
  Fill 181 untranslated entries while preserving existing translations.
  Validate the catalog against the current template with gettext.
  ```

## October 15, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/38812465411), [2](https://github.com/ghostty-org/ghostty/actions/runs/38705285984), [3](https://github.com/ghostty-org/ghostty/actions/runs/38683778451), [4](https://github.com/ghostty-org/ghostty/actions/runs/38680434974)  
Summary: 4 runs • 9 commits • 6 authors

### Changes

- [`508cfad`](https://github.com/ghostty-org/ghostty/commit/508cfade5e5f62a3ee35b65938c7080de19f4441) benchmark: convert prints to log ([@jcollie](https://github.com/jcollie))
  ```text
  Zig really doesn't like tests to print anything to stderr while
  running tests. Convert some stray std.debug.print statements into log
  statements. Log statements below `warn` will be suppressed when running
  tests, keeping Zig happy.
  ```
- [`b3dc3d7`](https://github.com/ghostty-org/ghostty/commit/b3dc3d794513c11633e7c3347935693957744e83) benchmark: convert prints to log ([#14718](https://github.com/ghostty-org/ghostty/issues/14718)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Zig really doesn't like tests to print anything to stderr while running
  tests. Convert some stray std.debug.print statements into log
  statements. Log statements below `warn` will be suppressed when running
  tests, keeping Zig happy.
  ```
- [`22fa134`](https://github.com/ghostty-org/ghostty/commit/22fa134a07f5749edd9e92c6bc17d8aaf61843be) Update VOUCHED list ([#14722](https://github.com/ghostty-org/ghostty/issues/14722)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14721#discussioncomment-18944491)
  from @trag1c.
  
  Denounce: @KooshaPari
  ```
- [`510b253`](https://github.com/ghostty-org/ghostty/commit/510b253dbc52d77b9f842ab6b8cba9ef046cea11) formatter: emit the hyperlinks of cells in VT output ([@robmorgan](https://github.com/robmorgan))
  ```text
  VT output only emitted the cursor's hyperlink (with the hyperlink extra),
  not the hyperlinks of text on the screen, so replaying it lost them. HTML
  output already wraps linked cells in anchors.
  
  Emit OSC 8 around linked cells in VT output, with the explicit id when
  there is one, using the same transition tracking as HTML. Opening a
  hyperlink replaces the open one, so the close is only written when no
  hyperlink follows. Blank cells have no hyperlink, so an open hyperlink is
  closed before the spaces written for them. Pages without hyperlinks, the
  common case, take a copy of the cell run loop that never checks for them.
  ```
- [`a2e4403`](https://github.com/ghostty-org/ghostty/commit/a2e440396403385680008e456a741a7776091412) formatter: emit the hyperlinks of cells in VT output ([#14711](https://github.com/ghostty-org/ghostty/issues/14711)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  VT output drops the hyperlinks of text on the screen, so replaying it
  loses them and the hyperlink extra only restores the cursor's open
  hyperlink. The HTML output already wraps linked cells in anchors and
  I've found a comment in the formatter notes that VT should do the same
  with OSC 8.
  
  This PR emits OSC 8 around linked cells in VT output, using the same
  transition tracking as HTML:
  
  - The explicit id is kept when there is one (`OSC 8 ; id=… ; URI ST`).
  - A hyperlink stays open across line breaks, so a link that continues on
  the next row is written once.
  - Blank cells have no hyperlink, so an open one is closed before the
  spaces written for them. Otherwise, the spaces would come back linked.
  - Opening a hyperlink replaces the open one, so switching between two
  links writes no close.
  - Pages without hyperlinks use a copy of the cell run loop that never
  checks for them.
  
  Cell hyperlinks are emitted like cell styles (always in VT, like HTML).
  I've left it so the `hyperlink` extra still covers only the cursor's
  hyperlink, the same way `style` only covers the cursor's style. This
  means "copy as VT" and `write_screen_file` with VT now include links. If
  you'd rather they be opt-in, then I can put them behind an option.
  
  ### Reproduction
  
  Small C program:
  
  ```c
  // libghostty-vt's VT formatter drops the hyperlinks (OSC 8) of text.
  #include <stdio.h>
  #include <ghostty/vt.h>
  
  int main(void) {
    GhosttyTerminal t;
    ghostty_terminal_new(NULL, &t, 20, 2);
  
    const char in[] = "\x1b]8;;https://example.com\x1b\\link\x1b]8;;\x1b\\ text";
    ghostty_terminal_vt_write(t, (const uint8_t *)in, sizeof(in) - 1);
  
    GhosttyFormatterTerminalOptions opts = {
        .size = sizeof(opts),
        .emit = GHOSTTY_FORMATTER_FORMAT_VT,
        .trim = true,
        .extra = {.size = sizeof(opts.extra),
                  .screen = {.size = sizeof(opts.extra.screen)}},
    };
    GhosttyFormatter f;
    ghostty_formatter_terminal_new(NULL, &f, t, opts);
    uint8_t buf[256];
    size_t len;
    ghostty_formatter_format_buf(f, buf, sizeof(buf), &len);
  
    // Print the output with ESC visible.
    for (size_t i = 0; i < len; i++) {
      if (buf[i] == 0x1b) fputs("\\e", stdout);
      else putchar(buf[i]);
    }
    putchar('\n');
    return 0;
  }
  ```
  
  ```sh
  zig build -Demit-lib-vt -Demit-xcframework=false --prefix out
  cc -o repro repro.c -Iout/include out/lib/libghostty-vt.a && ./repro
  ```
  
  Before: `link text`
  After: `\e]8;;https://example.com\e\link\e]8;;\e\ text`
  
  ### Benchmarks
  
  Note: Things get slower, but the cost only applies to linked text. On
  the `0.5` corpus, a third of it is one hyperlink lookup per linked cell,
  a tenth is the OSC 8 output, and the rest is leaving the fast cell loop
  at each link's start and end. Handling link changes inside the fast loop
  is measured as slower. Removing the lookups would take a per-page array
  of hyperlink ids, which seemed like too much for this PR.
  `--mode=roundtrip` gives `equal=true` for every corpus.
  
  I ran `ghostty-bench +terminal-formatter --formatter=terminal`, on 640
  KB `ghostty-gen +styled` corpora, with `--osc8-rate` setting how many
  cells are linked. Time per format, from `hyperfine` (main run twice
  agreed within 0.5%):
  
  | Corpus | VT output | main | this PR | Change |
  |---|---|---|---|---|
  | No hyperlinks | unchanged | 2.50 ms | 2.54 ms | +1.5% |
  | `--osc8-rate=0.1` | +19% bytes | 2.06 ms | 3.17 ms | +54% |
  | `--osc8-rate=0.5` | +69% bytes | 1.39 ms | 3.03 ms | +118% |
  | `--osc8-rate=0.5`, `--pin-map=true` | +68% bytes | 2.12 ms | 4.02 ms |
  +89% |
  
  One known limit: an implicit hyperlink that is closed and reopened,
  around a gap or at a page boundary, comes back as two implicit
  hyperlinks with the same URI.
  
  AI disclosure: Created with help from Claude Code using Opus 5.5,
  Iterated on, manually tested and reviewed by me.
  ````
- [`9689532`](https://github.com/ghostty-org/ghostty/commit/9689532cfff16b486eeab69c2194c7b3e3797c3a) core: report the release of a tracked click on a prompt ([@fornwall](https://github.com/fornwall))
  ```text
  When the cursor is at a prompt that declared click_events=1 or cl=,
  a left release ran the prompt click before the mouse report. Under
  mouse tracking the press had already been reported, so the release
  was replaced by a synthetic SGR press or arrow keys. Ghostty's own
  shell integration hits this whenever a widget runs a mouse-tracking
  program from the prompt, such as fzf's Ctrl-R binding.
  
  The selection gesture is reset when a press is reported, so a zero
  click count on release means the press reached the program. Skip the
  prompt click then and report the release too. Shift+click under
  tracking still records a gesture and moves the cursor.
  ```
- [`5dd2ee1`](https://github.com/ghostty-org/ghostty/commit/5dd2ee119db9d65aefc65fce830bbc69f55b17b2) build(deps): bump actions/create-github-app-token from 3.2.0 to 3.3.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [actions/create-github-app-token](https://github.com/actions/create-github-app-token) from 3.2.0 to 3.3.0.
  - [Release notes](https://github.com/actions/create-github-app-token/releases)
  - [Changelog](https://github.com/actions/create-github-app-token/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/actions/create-github-app-token/compare/bcd2ba49218906704ab6c1aa796996da409d3eb1...64ab729a6294000f5aa4a4bc0b73d1f32bc45510)
  
  ---
  updated-dependencies:
  - dependency-name: actions/create-github-app-token
    dependency-version: 3.3.0
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`9d1b234`](https://github.com/ghostty-org/ghostty/commit/9d1b234d97469b821dc6223bb9bcfdff7d625611) build(deps): bump actions/create-github-app-token from 3.2.0 to 3.3.0 ([#14713](https://github.com/ghostty-org/ghostty/issues/14713)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [actions/create-github-app-token](https://github.com/actions/create-github-app-token)
  from 3.2.0 to 3.3.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/actions/create-github-app-token/releases">actions/create-github-app-token's
  releases</a>.</em></p>
  <blockquote>
  <h2>v3.3.0</h2>
  <h2><a
  href="https://github.com/actions/create-github-app-token/compare/v3.2.0...v3.3.0">3.3.0</a>
  (2026-10-12)</h2>
  <h3>Features</h3>
  <ul>
  <li>update permission inputs (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/399">#399</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/a47236f79f79fcbc3532af49fe3a5ded89529b6e">a47236f</a>)</li>
  </ul>
  <h3>Bug Fixes</h3>
  <ul>
  <li><strong>deps:</strong> bump nested undici from 6.24.0 to 6.29.0 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/403">#403</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/12461a3a794e67c032f1eff5bb95ece9427eb4fb">12461a3</a>)</li>
  <li><strong>deps:</strong> bump the production-dependencies group across
  1 directory with 3 updates (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/395">#395</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/a69c19ddfdf8e1ab093900e0064524ce9309c807">a69c19d</a>)</li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/actions/create-github-app-token/blob/main/CHANGELOG.md">actions/create-github-app-token's
  changelog</a>.</em></p>
  <blockquote>
  <h1>Changelog</h1>
  <h2><a
  href="https://github.com/actions/create-github-app-token/compare/v3.2.0...v3.3.0">3.3.0</a>
  (2026-10-12)</h2>
  <h3>Features</h3>
  <ul>
  <li>update permission inputs (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/399">#399</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/a47236f79f79fcbc3532af49fe3a5ded89529b6e">a47236f</a>)</li>
  </ul>
  <h3>Bug Fixes</h3>
  <ul>
  <li><strong>deps:</strong> bump nested undici from 6.24.0 to 6.29.0 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/403">#403</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/12461a3a794e67c032f1eff5bb95ece9427eb4fb">12461a3</a>)</li>
  <li><strong>deps:</strong> bump the production-dependencies group across
  1 directory with 3 updates (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/395">#395</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/a69c19ddfdf8e1ab093900e0064524ce9309c807">a69c19d</a>)</li>
  </ul>
  <h2><a
  href="https://github.com/actions/create-github-app-token/compare/v3.1.1...v3.2.0">3.2.0</a>
  (2026-05-12)</h2>
  <h3>Features</h3>
  <ul>
  <li>add support for enterprise-level GitHub Apps (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/263">#263</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/952a2a7073df6bfa5f49bc469ec895b6ec1acea4">952a2a7</a>)</li>
  <li>support full repository names in <code>repositories</code> input (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/372">#372</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/85eb8dd41472213aed25d1a126460e0069138ab6">85eb8dd</a>)</li>
  </ul>
  <h3>Bug Fixes</h3>
  <ul>
  <li><strong>deps:</strong> bump <code>@​actions/core</code> from 3.0.0
  to 3.0.1 in the production-dependencies group (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/364">#364</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/43e5c345bfd4d4f3ecea019ad0042001a09dd857">43e5c34</a>)</li>
  <li>validate private-key input (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/376">#376</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/f24bbd89643991c0de27ae823c01791b2c6bafdd">f24bbd8</a>)</li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/64ab729a6294000f5aa4a4bc0b73d1f32bc45510"><code>64ab729</code></a>
  chore(main): release 3.3.0 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/402">#402</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/f3a828e4b91180d3a46ac1f4b43fa8384b0dea07"><code>f3a828e</code></a>
  ci: create signed dist commits in release workflow (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/404">#404</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/655017ffa7c6b0c6e4210729fa6bce35cacd8ca0"><code>655017f</code></a>
  docs: clarify when owner grants access to all repositories (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/378">#378</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/12461a3a794e67c032f1eff5bb95ece9427eb4fb"><code>12461a3</code></a>
  fix(deps): bump nested undici from 6.24.0 to 6.29.0 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/403">#403</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/a47236f79f79fcbc3532af49fe3a5ded89529b6e"><code>a47236f</code></a>
  feat: update permission inputs (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/399">#399</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/a69c19ddfdf8e1ab093900e0064524ce9309c807"><code>a69c19d</code></a>
  fix(deps): bump the production-dependencies group across 1 directory
  with 3 u...</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/d5cb7ae41d64331820d88810a4878e0942ec992a"><code>d5cb7ae</code></a>
  build(deps): bump actions/checkout from 6 to 7 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/384">#384</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/575da866bd0a42d7f234a8645831d55573252b09"><code>575da86</code></a>
  build(deps): bump stefanzweifel/git-auto-commit-action from 7.1.0 to
  7.2.0 in...</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/e85f677b44da0d1f08115ce52cdfd8fd2c69874a"><code>e85f677</code></a>
  test: omit stack traces from snapshots (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/401">#401</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/9419396df4d5672241cfb593dadc19758e54a204"><code>9419396</code></a>
  build(deps-dev): bump c8 from 11.0.0 to 12.0.0 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/400">#400</a>)</li>
  <li>Additional commits viewable in <a
  href="https://github.com/actions/create-github-app-token/compare/bcd2ba49218906704ab6c1aa796996da409d3eb1...64ab729a6294000f5aa4a4bc0b73d1f32bc45510">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=actions/create-github-app-token&package-manager=github_actions&previous-version=3.2.0&new-version=3.3.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`a9139e5`](https://github.com/ghostty-org/ghostty/commit/a9139e56c3e99209648d25063c60c4c9f61b3645) core: report the release of a tracked click on a prompt ([#14710](https://github.com/ghostty-org/ghostty/issues/14710)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  When the cursor is at a prompt with click-to-move (OSC 133
  [click_events](https://sw.kovidgoyal.net/kitty/shell-integration/#notes-for-shell-developers)
  or
  [cl=](https://gitlab.freedesktop.org/Per_Bothner/specifications/blob/master/proposals/semantic-prompts.md))
  and a program started from that prompt tracks the mouse, a left click
  reaches the program as a press without a release (the release is instead
  replaced by the prompt click).
  
  A release whose press went to the program now goes to the program too,
  instead of becoming a prompt click.
  
  Steps to reproduce:
  1. Use [ghostty shell
  integration](https://ghostty.org/docs/features/shell-integration).
  2. Use [fzf shell
  integration](https://junegunn.github.io/fzf/shell-integration/#setting-up-shell-integration),
  for example `source <(fzf --zsh)` under zsh. Tested with zsh; bash uses
  the same `cl=line` mark and fish uses `click_events=1`, so both should
  take the same path.
  3. Press `Ctrl-R` to open the fzf history search.
  4. Double click on a history item to select it.
  
  Results:
  - Before: The history item is not inserted into the shell prompt, since
  fzf only completes a double click on the release event it never
  receives.
  - After: The history item is inserted into the shell prompt.
  
  AI disclosure: Created with opus 5.5 through claude code. Reviewed and
  tested by me.
  ```

