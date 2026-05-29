> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: May 29, 2026 at 16:18 UTC.

## May 29, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26641829987)  
Summary: 1 runs • 2 commits • 2 authors

### Changes

- [`b771a3d`](https://github.com/ghostty-org/ghostty/commit/b771a3d4f1a2087ec5938e4a653c6926775caf5b) libghostty-vt: preserve shell prompts on resize by default ([@noib3](https://github.com/noib3))
  ```text
  This PR makes libghostty-vt preserve shell prompts across resize unless
  the shell explicitly opts into prompt clearing/redraw with `redraw=1`.
  ```
- [`9017595`](https://github.com/ghostty-org/ghostty/commit/90175950d5004382abd3b0b9528e7be81b0b52ec) libghostty-vt: preserve shell prompts on resize by default ([#12653](https://github.com/ghostty-org/ghostty/issues/12653)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This PR makes libghostty-vt preserve shell prompts across resize unless
  the shell explicitly opts into prompt clearing/redraw with `redraw=1`.
  ```

## May 28, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26600341544), [2](https://github.com/ghostty-org/ghostty/actions/runs/26554769180)  
Summary: 2 runs • 5 commits • 1 authors

### Changes

- [`3cf01e8`](https://github.com/ghostty-org/ghostty/commit/3cf01e84453c73e196cd3900d1b30757f4358e84) libghostty: add utf-8 grapheme cell getter to C API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a render-state row-cells getter that encodes the current cell's
  full grapheme cluster directly as UTF-8 into a caller-provided
  GhosttyBuffer. The getter writes the base codepoint first, followed by
  any extra grapheme codepoints, and follows the existing buffer-writer
  convention where len is bytes written on success or required capacity
  on GHOSTTY_OUT_OF_SPACE.
  
  Previously C consumers could query grapheme codepoints, but bindings
  that needed UTF-8 text had to reconstruct and encode the cluster
  themselves. That duplicated terminal internals in downstream bindings
  and made users pay for awkward cross-language struct handling. By
  owning the UTF-8/grapheme behavior in libghostty, bindings can use one
  stable C API and optionally wrap it with small binding-local helpers.
  ```
- [`519a612`](https://github.com/ghostty-org/ghostty/commit/519a612bebf25887973bab4ae22bba85f48a5e6b) libghostty: fix wasm build for selection gesture ([@mitchellh](https://github.com/mitchellh))
- [`cb36966`](https://github.com/ghostty-org/ghostty/commit/cb36966a752982014827a9cabcf630ec3788b3d9) libghostty: add utf-8 grapheme cell getter to C API ([#12847](https://github.com/ghostty-org/ghostty/issues/12847)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a render-state row-cells getter that encodes the current cell's full
  grapheme cluster directly as UTF-8 into a caller-provided GhosttyBuffer.
  The getter writes the base codepoint first, followed by any extra
  grapheme codepoints, and follows the existing buffer-writer convention
  where len is bytes written on success or required capacity on
  GHOSTTY_OUT_OF_SPACE.
  
  Previously C consumers could query grapheme codepoints, but bindings
  that needed UTF-8 text had to reconstruct and encode the cluster
  themselves. That duplicated terminal internals in downstream bindings
  and made users pay for awkward cross-language struct handling. By owning
  the UTF-8/grapheme behavior in libghostty, bindings can use one stable C
  API and optionally wrap it with small binding-local helpers.
  ```
- [`8beea5f`](https://github.com/ghostty-org/ghostty/commit/8beea5f92dcfb229b9434eed6ea5548e32ed5df8) libghostty: expose row cell styling bit ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a render row-cells data key for querying whether the current cell has
  explicit styling. This lets consumers avoid fetching a raw cell or full style
  snapshot when all they need is the cell's HasStyling bit.
  
  The new key is appended to the existing enum for ABI safety and is served by
  the existing row-cells getter path. Existing data keys and function exports are
  unchanged.
  ```
- [`54ac5fd`](https://github.com/ghostty-org/ghostty/commit/54ac5fd21e5eeef5e910f7f646934dc58fd373f8) libghostty: expose row cell styling bit ([#12837](https://github.com/ghostty-org/ghostty/issues/12837)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a render row-cells data key for querying whether the current cell
  has explicit styling. This lets consumers avoid fetching a raw cell or
  full style snapshot when all they need is the cell's HasStyling bit.
  
  The new key is appended to the existing enum for ABI safety and is
  served by the existing row-cells getter path. Existing data keys and
  function exports are unchanged.
  
  This was identified as an allocation hot-spot in Go renderers.
  ```

## May 27, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26543370661), [2](https://github.com/ghostty-org/ghostty/actions/runs/26530789804), [3](https://github.com/ghostty-org/ghostty/actions/runs/26519976482)  
Summary: 3 runs • 32 commits • 5 authors

### Changes

- [`f730ee0`](https://github.com/ghostty-org/ghostty/commit/f730ee0557917258024e18a45489918de2ce9fa7) libghostty: expose viewport active state ([@mitchellh](https://github.com/mitchellh))
  ```text
  Expose whether the terminal viewport is currently pinned to the active
  area through the libghostty-vt terminal data API. Previously embedders
  could only infer this from scrollbar geometry, which was indirect and
  could require the more expensive scrollbar calculation.
  
  The new GHOSTTY_TERMINAL_DATA_VIEWPORT_ACTIVE value returns the exact
  PageList viewport state as a bool. The scroll viewport test now verifies
  the value while moving between the active area and scrollback.
  ```
- [`1526485`](https://github.com/ghostty-org/ghostty/commit/15264856f61b112c8beb14fbe3f403f6266c8bdf) libghostty: expose viewport active state ([#12836](https://github.com/ghostty-org/ghostty/issues/12836)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Expose whether the terminal viewport is currently pinned to the active
  area through the libghostty-vt terminal data API. Previously embedders
  could only infer this from scrollbar geometry, which was indirect and
  could require the more expensive scrollbar calculation.
  
  The new GHOSTTY_TERMINAL_DATA_VIEWPORT_ACTIVE value returns the exact
  PageList viewport state as a bool. The scroll viewport test now verifies
  the value while moving between the active area and scrollback.
  ```
- [`2f61ba0`](https://github.com/ghostty-org/ghostty/commit/2f61ba036ed4d0013f34414728938bf7825219c8) libghostty: starting the SelectionGesture API, just init/get ([@mitchellh](https://github.com/mitchellh))
- [`bbfa984`](https://github.com/ghostty-org/ghostty/commit/bbfa984aec99c8d3e2e7dde1a10c7520f4f873cb) libghostty: GhosttySelectionGestureEvent ([@mitchellh](https://github.com/mitchellh))
- [`5ac8e65`](https://github.com/ghostty-org/ghostty/commit/5ac8e6569a8d1d73f1bff9b4fc82ea703b9ca97e) libghostty: add ghostty_selection_gesture_event ([@mitchellh](https://github.com/mitchellh))
- [`3fd2c66`](https://github.com/ghostty-org/ghostty/commit/3fd2c66a048ad12901ea30ef30da1a4dfc7395a4) libghostty: selection gesture release event ([@mitchellh](https://github.com/mitchellh))
- [`90fd1ec`](https://github.com/ghostty-org/ghostty/commit/90fd1ec2e78d1c0b3f640c9eb1e73a6e7dd7232b) libghostty: selection gesture drag events ([@mitchellh](https://github.com/mitchellh))
- [`603684b`](https://github.com/ghostty-org/ghostty/commit/603684ba11092b9430c336b3378ba22ef9615cc0) libghostty: selection gesture autotick ([@mitchellh](https://github.com/mitchellh))
- [`f0fcb10`](https://github.com/ghostty-org/ghostty/commit/f0fcb104069647051b2e612c23c90e2414a0db58) libghostty: selection gesture deep press ([@mitchellh](https://github.com/mitchellh))
- [`3e0477a`](https://github.com/ghostty-org/ghostty/commit/3e0477a14a1a6a0a8f4a5256b95528aa8145351a) example/c-vt-selection-gesture ([@mitchellh](https://github.com/mitchellh))
- [`4e2d7c3`](https://github.com/ghostty-org/ghostty/commit/4e2d7c314b2e3645924c50eba309a431d28c4bb2) libghostty: optimize bits for selection gesture validation fields ([@mitchellh](https://github.com/mitchellh))
- [`6d089a5`](https://github.com/ghostty-org/ghostty/commit/6d089a544db53f3457374c2c406bccee80722cdf) libghostty: C API for SelectionGesture ([#12833](https://github.com/ghostty-org/ghostty/issues/12833)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  C API side of https://github.com/ghostty-org/ghostty/pull/12830
  ```
- [`ac69942`](https://github.com/ghostty-org/ghostty/commit/ac69942cdcc2d7c26bc5fe7ed1d5d505c3461e0c) cli: rework +ssh-cache internals and user interface ([@jparise](https://github.com/jparise))
  ```text
  This change primarily focused on a revised +ssh-cache user interface,
  but it also reworks a bunch of the internals.
  
  The primary CLI improvement is support for positional arguments and a
  consistent list output format that includes both the ISO-formatted
  timestamp and relative age.
  
      ghostty +ssh-cache                           # List all cached destinations
      ghostty +ssh-cache user@example.com          # Show that destination
      ghostty +ssh-cache example.com               # Show all users on that host
      ghostty +ssh-cache --add=user@example.com    # Manually add a destination
      ghostty +ssh-cache --remove=user@example.com # Remove a destination
      ghostty +ssh-cache --prune=30d               # Remove entries older than 30 days
      ghostty +ssh-cache --clear                   # Clear entire cache
  
  Notable, we now support a --prune operation that replaces the previous
  --expire-days flag that was never actually hooked up to anything (!!).
  --prune also supports a wider range of Duration-based values.
  
  We're also much more consistent with error codes: 0=success, 1=failure,
  2=usage.
  
  While working on those changes, I also reworked the cache internals,
  particularly the code around timestamp handling and errors. For example,
  I dropped the explicit error sets because they were growing unwieldy,
  and in practice we only matched on a subset of those errors.
  
  Lastly, overall test coverage should be much improved, especially around
  the time- and allocation-related operations.
  ```
- [`d86ff37`](https://github.com/ghostty-org/ghostty/commit/d86ff37a58f77d87f1774a433bdcfabf9f99e246) terminal: SelectionGesture, but only with mouse press ([@mitchellh](https://github.com/mitchellh))
- [`14df684`](https://github.com/ghostty-org/ghostty/commit/14df684a70fed6085ec70b711f045f0261dbe4c2) core: adapt Surface to use SelectionGesture with press only ([@mitchellh](https://github.com/mitchellh))
- [`57d2020`](https://github.com/ghostty-org/ghostty/commit/57d202066d138e9078f89c9b27302a5aee6b9422) macOS: clear stale OSC 11 background cache on config change ([@b0uks](https://github.com/b0uks))
  ```text
  SurfaceView caches the background color set by OSC 11 in
  backgroundColor. TerminalWindow.preferredBackgroundColor consults
  that cache before falling back to derivedConfig.backgroundColor,
  so once OSC 11 has fired the cached value masks any later config
  change. After a light/dark theme auto-switch this leaves the
  window chrome on the previous theme's color until the application
  next emits OSC 11.
  
  In ghosttyConfigDidChange, after updating derivedConfig, drop the
  cache when it no longer matches the new config-derived background.
  A subsequent ghosttyColorDidChange repopulates it as before, so
  within-config OSC 11 behavior is unchanged.
  ```
- [`33f1558`](https://github.com/ghostty-org/ghostty/commit/33f1558801d5282e9b2fb7b35194fed69d98f167) core: mouse left release renderer lock made more coarse ([@mitchellh](https://github.com/mitchellh))
  ```text
  This will make our selection gesture extraction a bit easier.
  ```
- [`c00cdd8`](https://github.com/ghostty-org/ghostty/commit/c00cdd886b933cd7db175ddcf031c2e703ea1409) SelectionGesture: drag events ([@mitchellh](https://github.com/mitchellh))
- [`229f4c1`](https://github.com/ghostty-org/ghostty/commit/229f4c1f4fdd2a24ff1e2634d6450de158fd987c) terminal: SelectionGesture handles word/line drag ([@mitchellh](https://github.com/mitchellh))
- [`141c7d4`](https://github.com/ghostty-org/ghostty/commit/141c7d44d2d10621d6b8f014c6a1ec3e416f14ea) SelectionGesture: release event ([@mitchellh](https://github.com/mitchellh))
- [`df98b6d`](https://github.com/ghostty-org/ghostty/commit/df98b6d9833dbc80babee58b8a02d102d14bfd83) terminal: SelectionGesture autoscrollTick ([@mitchellh](https://github.com/mitchellh))
- [`f5f9d32`](https://github.com/ghostty-org/ghostty/commit/f5f9d32d0a42b55bb80599a000e63c33a25d549e) terminal: SelectionGesture deep press ([@mitchellh](https://github.com/mitchellh))
- [`5368adc`](https://github.com/ghostty-org/ghostty/commit/5368adcd29754939e6c283198ef6b1c122293815) macos: avoid duplicate appearance sync on tab focus ([@Tunglies](https://github.com/Tunglies))
  ```text
  Close #12825
  
  Skip the initial emissions from the focused surface appearance publishers after a tab focus change. The focused surface is already synced immediately, so the initial Combine values only repeat the same titlebar and background updates. Subsequent derived config and OSC background changes still resync the window appearance.
  ```
- [`ce4128a`](https://github.com/ghostty-org/ghostty/commit/ce4128afc494d192edcc0f3a28e2d63fbb059eda) Update VOUCHED list ([#12829](https://github.com/ghostty-org/ghostty/issues/12829)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12827#discussioncomment-17075382)
  from @trag1c.
  
  Denounce: @Cznorth
  ```
- [`9b00bb4`](https://github.com/ghostty-org/ghostty/commit/9b00bb436a99ece1b78bea90b403f38636cbff15) terminal: better SelectionGesture docs ([@mitchellh](https://github.com/mitchellh))
- [`82a73f2`](https://github.com/ghostty-org/ghostty/commit/82a73f2bf185ee2836378e3aeea8fc528e757921) terminal: SelectionGesture press returns standard behaviors ([@mitchellh](https://github.com/mitchellh))
- [`7d4d1e5`](https://github.com/ghostty-org/ghostty/commit/7d4d1e5819b635004b17e28bc302a036e4461c04) terminal: add configurable behaviors based on click count ([@mitchellh](https://github.com/mitchellh))
- [`68959c5`](https://github.com/ghostty-org/ghostty/commit/68959c5c6388fad9f7c169ad8229a6bfd17d8ff0) terminal: fix selection gesture edge cases ([@mitchellh](https://github.com/mitchellh))
  ```text
  Selection gestures now treat releases with invalidated anchors as dragged,
  so a press that crosses screen boundaries cannot also activate links or
  prompt clicks on release. Cell drags that create a same-cell selection also
  mark the gesture as dragged, which keeps click-only actions from firing
  after a threshold-crossing drag.
  
  Autoscroll now resolves the drag pin after moving the viewport instead of
  reusing the pin from before the scroll. This keeps the selection aligned
  with the row currently under the pointer. The inspector also validates the
  tracked click pin before displaying it so stale pins from inactive screens
  are ignored.
  ```
- [`c343c5a`](https://github.com/ghostty-org/ghostty/commit/c343c5a67a041833eb9c716319f2df3ca8388144) Extract click/drag selection handling into SelectionGesture ([#12830](https://github.com/ghostty-org/ghostty/issues/12830)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Refactor terminal text selection into a reusable `SelectionGesture`
  state machine. Most importantly, this means our click+drag logic around
  selection is now fully unit tested! And we found bugs! And fixed them!
  
  The large line increase in this diff is mainly comments + tests.
  
  I've wanted to do this forever so we can unit test this, but I was
  kicked in the butt to do it recently because reimplementing selection
  logic in libghostty consumers turns out to be complex and error prone
  and we have a perfectly battle tested logic machine here so why not
  extract it?
  
  Behavioral changes from main surfaced via unit testing:
  
  - Dragging now drags by output across semantic output blocks when the
  initial press was an output selection. This matches the behavior of
  dragging continuing whatever the initial selection logic was.
  - Selection autoscroll now stops when the click anchor is invalidated by
  a screen change (e.g. primary to alt)
  - Deep press (macOS force touch) now selects the word at the original
  press location and consumes the active drag gesture, preventing later
  movement from dragging or autoscrolling that selection. This matches
  built-in macOS apps.
  - Mouse release records whether the gesture moved away from the pressed
  cell, so link and prompt clicks are skipped after a drag while normal
  clicks still activate them.
  
  Example usage:
  
  ```zig
  var gesture: terminal.SelectionGesture = .init;
  defer gesture.deinit(t);
  
  const press_selection = try gesture.press(t, .{
      .time = try std.time.Instant.now(),
      .pin = press_pin,
      .xpos = mouse_x,
      .ypos = mouse_y,
      .max_distance = cell_width,
      .repeat_interval = mouse_interval,
      .word_boundary_codepoints = selection_word_chars,
      .behaviors = &.{ .cell, .word, .output },
  });
  try t.screens.active.select(press_selection);
  
  if (gesture.drag(t, drag_event)) |drag_selection| {
      try t.screens.active.select(drag_selection);
  }
  
  gesture.release(t, .{ .pin = release_pin });
  ```
  ````
- [`8518986`](https://github.com/ghostty-org/ghostty/commit/8518986b1e84998e8141eacce462afd213b38073) macOS: clear stale OSC 11 background cache on config change ([#12822](https://github.com/ghostty-org/ghostty/issues/12822)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Summary
  
  `SurfaceView` caches the background color set by OSC 11 in
  `backgroundColor`. `TerminalWindow.preferredBackgroundColor` consults
  that cache before falling back to `derivedConfig.backgroundColor`, so
  once OSC 11 has fired the cached value masks any later config change.
  
  After a light/dark theme auto-switch (e.g. `theme =
  light:my-light,dark:my-dark`) this leaves the window chrome on the
  previous theme's color until the application next emits OSC 11.
  
  In `ghosttyConfigDidChange`, after updating `derivedConfig`, drop the
  cache when it no longer matches the new config-derived background. A
  subsequent `ghosttyColorDidChange` repopulates it as before, so
  within-config OSC 11 behavior is unchanged.
  
  ## Reproduction
  
  1. Configure `theme = light:SomeLight,dark:SomeDark` where the two
  themes have visibly different background colors.
  2. Open a terminal session where any application (e.g. a shell startup
  script) has sent OSC 11 to set a custom background color.
  3. Switch macOS appearance (System Settings → Appearance).
  4. **Before**: window chrome stays the previous theme's color until the
  terminal next emits OSC 11.
  5. **After**: window chrome immediately updates to the new theme's
  background color.
  
  ## Changes
  
  - `SurfaceView_AppKit.swift` — one guard: if the cached
  `backgroundColor` disagrees with the new
  `derivedConfig.backgroundColor`, set it to `nil`.
  ```
- [`756fda7`](https://github.com/ghostty-org/ghostty/commit/756fda776b1f8516bcf925ad9901cb0139b64271) cli: rework +ssh-cache internals and user interface ([#12814](https://github.com/ghostty-org/ghostty/issues/12814)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This change primarily focused on a revised +ssh-cache user interface,
  but it also reworks a bunch of the internals.
  
  The primary CLI improvement is support for positional arguments and a
  consistent list output format that includes both the ISO-formatted
  timestamp and relative age.
  
  ghostty +ssh-cache # List all cached destinations
      ghostty +ssh-cache user@example.com          # Show that destination
  ghostty +ssh-cache example.com # Show all users on that host
  ghostty +ssh-cache --add=user@example.com # Manually add a destination
      ghostty +ssh-cache --remove=user@example.com # Remove a destination
  ghostty +ssh-cache --prune=30d # Remove entries older than 30 days
      ghostty +ssh-cache --clear                   # Clear entire cache
  
  Notable, we now support a --prune operation that replaces the previous
  --expire-days flag that was never actually hooked up to anything (!!).
  --prune also supports a wider range of Duration-based values.
  
  We're also much more consistent with error codes: 0=success, 1=failure,
  2=usage.
  
  While working on those changes, I also reworked the cache internals,
  particularly the code around timestamp handling and errors. For example,
  I dropped the explicit error sets because they were growing unwieldy,
  and in practice we only matched on a subset of those errors.
  
  Lastly, overall test coverage should be much improved, especially around
  the time- and allocation-related operations.
  
  ---
  
  *AI Disclosure:* I made a lot of iterative, AI-assisted (Claude Opus
  4.7) correctness passes over this work. It was particularly helpful in
  tracing through the various failure modes, and it wrote those unit tests
  in the process.
  ```
- [`3103ae8`](https://github.com/ghostty-org/ghostty/commit/3103ae883880fe6cccdc17ea923e3ccd3587a83e) macos: avoid duplicate appearance sync on tab focus ([#12828](https://github.com/ghostty-org/ghostty/issues/12828)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Close #12825
  
  Skip the initial emissions from the focused surface appearance
  publishers after a tab focus change. The focused surface is already
  synced immediately, so the initial Combine values only repeat the same
  titlebar and background updates. Subsequent derived config and OSC
  background changes still resync the window appearance.
  
  
  
  https://github.com/user-attachments/assets/f229fb95-4b4c-4040-85ac-0acfcc54ca82
  
  
  
  Assigned to Codex GPT 5.5(medium)
  PS: Sry for I don't write zig and let AI write this.
  ```

## May 26, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26461870831)  
Summary: 1 runs • 5 commits • 3 authors

### Changes

- [`a746d0f`](https://github.com/ghostty-org/ghostty/commit/a746d0f7281954eb251915f4cd9fcea4924ad999) Update VOUCHED list ([#12816](https://github.com/ghostty-org/ghostty/issues/12816)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12815#issuecomment-4537093020)
  from @jcollie.
  
  Vouch: @nikicat
  ```
- [`0b6d91e`](https://github.com/ghostty-org/ghostty/commit/0b6d91e531a14c70f25bb1c8cd4a376a89bad7a4) apprt/gtk: reuse one audio-bell MediaFile per surface to fix thread leak ([@nikicat](https://github.com/nikicat))
  ```text
  Each audio bell called gtk.MediaFile.newForFilename, which spins up a
  full GStreamer pipeline. The GTK4 GStreamer backend's GL sink starts
  gstglcontext/gldisplay-event threads that are never joined on teardown,
  so allocating a MediaFile per ring leaked a pipeline and ~4 threads on
  every bell. A long-running instance accumulated 705 threads over ~4h of
  normal use.
  
  Cache one MediaFile per surface (priv.bell_media), rebuilt only when
  bell-audio-path changes and unref'd on dispose. Each bell now replays
  the same pipeline via seek(0)+play() instead of creating a new one. The
  notify::ended -> unref handler is removed: it was what discarded (and
  leaked) a pipeline per ring. seek(0) is required so an ended stream
  plays again (#8957).
  
  Verified on a real instance: GStreamer's global element counter reached
  only oggdemux4 over an hour of use (one pipeline per bell-ringing
  surface, reused) and thread count stayed flat, versus per-bell growth
  before.
  ```
- [`0708f93`](https://github.com/ghostty-org/ghostty/commit/0708f932a51d7e4a0d1022a01f73d0267d42660d) apprt/gtk: add regression test for audio-bell MediaFile reuse ([@nikicat](https://github.com/nikicat))
  ```text
  Guards the contract that prevents the bell thread leak: bellMediaFile
  must return the same cached MediaFile for an unchanged path and only
  rebuild when the path changes. A revert to per-bell allocation (the
  leak) would fail this. Runs in the existing test-gtk CI job; needs no
  display or playback since the path bookkeeping is all that's asserted.
  ```
- [`9910a1a`](https://github.com/ghostty-org/ghostty/commit/9910a1a4753c9e135cd1add4119624f86d8167aa) test: add audio-bell thread-leak NixOS check (GNOME/Wayland) ([@nikicat](https://github.com/nikicat))
  ```text
  Adds a bell-leak-check-gnome NixOS test (nix/tests.nix) that launches
  Ghostty under GNOME on Wayland, rings 100 bells in the window, and fails
  if the GUI process thread count grows per-bell — the end-to-end
  signature of the GStreamer pipeline leak fixed in this branch. Verified
  locally: growth of ~1 thread over 100 bells, vs ~+400 pre-fix.
  
  Replaces the earlier Xvfb shell script + workflow job: per review, X11
  support in GNOME is going away, and this belongs as a Nix check
  alongside the other *-gnome tests rather than a standalone script.
  
  The VM has no GPU, so it renders via llvmpipe; the test gives the guest
  enough cores/RAM for software GL and tolerates the +new-window D-Bus
  activation exceeding its client-side timeout (the window still comes up)
  by waiting for the window rather than hard-failing on the call.
  ```
- [`2e5ad91`](https://github.com/ghostty-org/ghostty/commit/2e5ad917eb4e325a3dbb161c3f41208a8cd35e44) apprt/gtk: fix audio-bell GStreamer thread leak (reuse one MediaFile per surface) ([#12815](https://github.com/ghostty-org/ghostty/issues/12815)) ([@jcollie](https://github.com/jcollie))
  ```text
  ## Problem
  
  Every audio bell calls `gtk.MediaFile.newForFilename`, which spins up a
  full GStreamer pipeline. The GTK4 GStreamer backend's GL sink starts
  `gstglcontext`/`gldisplay-event` threads that are **never joined on
  teardown**, so allocating a fresh `MediaFile` per ring leaks a pipeline
  and ~4 threads on every bell. The old `notify::ended -> unref` handler
  discarded the pipeline but did not (and could not) join those threads.
  
  A long-running instance accumulated **705 threads over ~4h** of normal
  use.
  
  ## Fix
  
  Cache one `MediaFile` per surface (`priv.bell_media`), rebuilt only when
  `bell-audio-path` changes and unref'd on `dispose`. Each bell now
  replays the same pipeline via `seek(0)` + `play()` instead of creating a
  new one. `seek(0)` is required so an ended stream plays again (cf.
  #8957).
  
  ## Verification
  
  Confirmed on a real running instance with the fix: GStreamer's global
  element counter only ever reached `oggdemux4` over an hour of use (one
  pipeline per bell-ringing surface, reused for every subsequent bell) and
  the process thread count stayed flat — versus the per-bell growth
  before.
  
  ## Commits
  
  1. **The fix** — reuse one MediaFile per surface.
  2. **Unit regression test** — guards the `bellMediaFile` reuse contract
  (same path → same object, changed path → rebuild). Runs in the existing
  `test-gtk` CI job; needs no display.
  3. **End-to-end CI job** *(kept separate so it can be dropped
  independently)* — `test/bell-leak.sh` + a `test-gtk-bell-leak` workflow
  job that runs ghostty headless (Xvfb + software GL), rings 120 bells,
  and fails if the thread count grows per-bell. It's heavier and more
  environment-sensitive (needs Xvfb/Mesa/GStreamer on the runner), so it's
  isolated for easy review/removal.
  
  🤖 Generated with [Claude Code](https://claude.com/claude-code)
  ```

## May 25, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26413295588), [2](https://github.com/ghostty-org/ghostty/actions/runs/26410170673), [3](https://github.com/ghostty-org/ghostty/actions/runs/26403112298), [4](https://github.com/ghostty-org/ghostty/actions/runs/26382148026), [5](https://github.com/ghostty-org/ghostty/actions/runs/26381111088)  
Summary: 5 runs • 10 commits • 4 authors

### Changes

- [`2d0fb81`](https://github.com/ghostty-org/ghostty/commit/2d0fb81751def478e2f8a5f7e2ee91fa9cbf9bff) Update VOUCHED list ([#12813](https://github.com/ghostty-org/ghostty/issues/12813)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12793#discussioncomment-17052752)
  from @bo2themax.
  
  Vouch: @LePips
  ```
- [`a5550a2`](https://github.com/ghostty-org/ghostty/commit/a5550a2dcb8c81d0e6a53391e68d7887c0078147) cli: fix readEntries leak and double-free ([@jparise](https://github.com/jparise))
  ```text
  readEntries had two memory bugs on the allocation failure path, both
  only reachable under OOM:
  
  - The map itself was never freed if we ran into an allocation failure
  - The unconditional `errdefer`s for the dupe'd hostname and terminfo
    values could double-free if there was a later allocation failure.
  
  This change restructures this function so that these values are dupe'd
  up-front, and then their ownership is tracked using optionals that can
  be null'ed out once their ownership is transferred into the map.
  
  Both of these cases are now covered by unit tests.
  ```
- [`16d7c8f`](https://github.com/ghostty-org/ghostty/commit/16d7c8f2b42890c09590e8c9a00ec34504d449b5) elvish: remove community maintenance note ([@jparise](https://github.com/jparise))
  ```text
  The Elvish integration is currently actively maintained by the Ghostty
  maintainers. Contributions are of course still welcome.
  ```
- [`53e400a`](https://github.com/ghostty-org/ghostty/commit/53e400ad85c021809bb9f05ceb3c9b38c1843fac) cli: fix readEntries leak and double-free ([#12811](https://github.com/ghostty-org/ghostty/issues/12811)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  readEntries had two memory bugs on the allocation failure path, both
  only reachable under OOM:
  
  - The map itself was never freed if we ran into an allocation failure
  - The unconditional `errdefer`s for the dupe'd hostname and terminfo
  values could double-free if there was a later allocation failure.
  
  This change restructures this function so that these values are dupe'd
  up-front, and then their ownership is tracked using optionals that can
  be null'ed out once their ownership is transferred into the map.
  
  Both of these cases are now covered by unit tests.
  ```
- [`cb28160`](https://github.com/ghostty-org/ghostty/commit/cb28160b5a2fd32d2e1cfeefb01d4297dbca8b18) elvish: remove community maintenance note ([#12812](https://github.com/ghostty-org/ghostty/issues/12812)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The Elvish integration is currently actively maintained by the Ghostty
  maintainers. Contributions are of course still welcome.
  ```
- [`ae52f97`](https://github.com/ghostty-org/ghostty/commit/ae52f97dcac558735cfa916ea3965f247e5c6e9e) Update VOUCHED list ([#12809](https://github.com/ghostty-org/ghostty/issues/12809)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12807#issuecomment-4534655288)
  from @pluiedev.
  
  Denounce: @eric-assetpass
  ```
- [`edf2da0`](https://github.com/ghostty-org/ghostty/commit/edf2da015705db22fffdcab62a0871c898fa064b) libghostty: expose per-cell selection state ([@mitchellh](https://github.com/mitchellh))
  ```text
  Render-state rows already expose their selected range, but
  cell-oriented C API consumers had to fetch that row range separately
  and duplicate the containment check while rendering.
  
  Add a SELECTED row-cells data kind that carries the row selection into
  the row-cells wrapper and returns whether the current cell column is in
  that inclusive range. The field remains separate from cell colors and
  style so selection stays an explicit render overlay policy.
  
  For performance reasons, the span-based row getter is recommended still
  but this is a convenient thing to do for cell-oriented folks.
  ```
- [`b869a6e`](https://github.com/ghostty-org/ghostty/commit/b869a6e5ab0a50ce01e8eb5aa408a02b3cbe4f3a) libghostty: expose per-cell selection state ([#12798](https://github.com/ghostty-org/ghostty/issues/12798)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Render-state rows already expose their selected range, but cell-oriented
  C API consumers had to fetch that row range separately and duplicate the
  containment check while rendering.
  
  Add a SELECTED row-cells data kind that carries the row selection into
  the row-cells wrapper and returns whether the current cell column is in
  that inclusive range. The field remains separate from cell colors and
  style so selection stays an explicit render overlay policy.
  
  For performance reasons, the span-based row getter is recommended still
  but this is a convenient thing to do for cell-oriented folks.
  ```
- [`bb375a2`](https://github.com/ghostty-org/ghostty/commit/bb375a2f7565b9d8c8b60c6cbc0bd4e6c4532023) deal with large outputs from xdg-open/rundll32/open ([@jcollie](https://github.com/jcollie))
  ```text
  Depending on your system config, `xdg-open` may stay open for extended
  periods, and potentially log more than the 50kb of output that we were
  previously able to deal with. This changes `open()` so that output on
  `stdout` is just directly ignored. Any output from `stderr` is immedialy
  logged rather than collected for later logging.
  
  Note that this will generally occur if your system is not configured
  with the DBus portals that `xdg-open` uses to open URLs rather than
  launching programs like your web browser directly. This could be seen as
  user misconfiguration but we should deal with it robustly anyway.
  ```
- [`cf9e85e`](https://github.com/ghostty-org/ghostty/commit/cf9e85ecd73cc3f044cab228a75145f63e88ca1d) deal with large outputs from xdg-open/rundll32/open ([#12797](https://github.com/ghostty-org/ghostty/issues/12797)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Depending on your system config, `xdg-open` may stay open for extended
  periods, and potentially log more than the 50kb of output that we were
  previously able to deal with. This changes `open()` so that output on
  `stdout` is just directly ignored. Any output from `stderr` is immedialy
  logged rather than collected for later logging.
  
  Note that this will generally occur if your system is not configured
  with the DBus portals that `xdg-open` uses to open URLs rather than
  launching programs like your web browser directly. This could be seen as
  user misconfiguration but we should deal with it robustly anyway.
  ```

## May 24, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26373400178)  
Summary: 1 runs • 17 commits • 1 authors

### Changes

- [`ae03d3c`](https://github.com/ghostty-org/ghostty/commit/ae03d3cae4d4af244a43d91a0d8040739899e4a3) libghostty: expose get/set active selection state ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add terminal set/get support for the active screen selection through the
  existing option and data APIs. Setting a selection copies the C snapshot
  into terminal-owned tracked state, while passing NULL clears the current
  selection.
  
  Getting the selection now returns an untracked GhosttySelection snapshot
  or GHOSTTY_NO_VALUE when there is no selection. The C header documents
  the different lifetimes for set and get so embedders know when input and
  returned grid references remain valid.
  ```
- [`24048ff`](https://github.com/ghostty-org/ghostty/commit/24048ffd471c5e88006bafc6ab3e5eb3c710a15d) libghostty: expose row-local render selections ([@mitchellh](https://github.com/mitchellh))
  ```text
  Render state already tracks the selected cell range for each viewport row,
  but C renderers could only get the full terminal selection. That required
  consumers to map global selection pins back into row-local spans themselves.
  
  Add row selection data to the render-state row API. Querying the new row
  data returns GHOSTTY_NO_VALUE for unselected rows and writes the inclusive
  start and end columns for selected rows. The render example now demonstrates
  setting a selection and reading the row-local range while iterating rows.
  ```
- [`545a5ae`](https://github.com/ghostty-org/ghostty/commit/545a5aef663ef551bd8b2b2b794f47d9a74d7586) libghostty: document selection snapshot lifetime ([@mitchellh](https://github.com/mitchellh))
  ```text
  Clarify that GhosttySelection is a snapshot type whose endpoints are
  untracked GhosttyGridRef values. The previous documentation described the
  range shape but did not repeat the grid reference lifetime caveat, which
  made it easy to keep selections across terminal mutations incorrectly.
  ```
- [`15d8963`](https://github.com/ghostty-org/ghostty/commit/15d89636814ac0d8d0beb783da0dee6ba63f8f7c) libghostty: add selection adjustment api ([@mitchellh](https://github.com/mitchellh))
- [`4a77e81`](https://github.com/ghostty-org/ghostty/commit/4a77e8196720088cbdce701c88412d3ba16089b5) libghostty: add selection ordering APIs ([@mitchellh](https://github.com/mitchellh))
  ```text
  Expose selection endpoint ordering through the libghostty-vt C API so
  embedders can safely normalize selections whose start and end refs may be
  reversed. The new APIs report the current order and return a fresh
  untracked selection with forward or reverse bounds.
  
  Selection.Order now uses lib.Enum, matching the existing adjustment enum
  pattern and keeping the C ABI enum generated from the same Zig source of
  truth. The new functions are wired through the C API re-export and lib-vt
  export paths, with coverage for mirrored rectangular selection ordering.
  ```
- [`671c12f`](https://github.com/ghostty-org/ghostty/commit/671c12fad9f85c8b384773c3ba936b07b4af45bf) libghostty: add selection contains API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Expose a C API for checking whether a GhosttyPoint is inside a
  GhosttySelection. The new terminal helper validates the selection snapshot
  against the active screen, resolves the point to a grid pin, and delegates
  to the internal Selection.contains implementation so C consumers get the
  same linear and rectangular selection semantics as Ghostty.
  
  Wire the symbol through the C API exports and public headers, and add a
  focused test covering linear containment and rectangular selection behavior.
  ```
- [`2512fad`](https://github.com/ghostty-org/ghostty/commit/2512fad9408bf0fee76dda2eae7a401e28d6b18f) libghostty: move selection functions to selection doxygen group ([@mitchellh](https://github.com/mitchellh))
- [`ae83939`](https://github.com/ghostty-org/ghostty/commit/ae839393d9b0a6d6776e816e8a9193c3d6875850) libghostty: add Selection equal and validate ([@mitchellh](https://github.com/mitchellh))
- [`7b49d1f`](https://github.com/ghostty-org/ghostty/commit/7b49d1f12928908de022c00ef5dbc099a66517fb) terminal: PageList.reset needs to reset page serial mins ([@mitchellh](https://github.com/mitchellh))
- [`847b8af`](https://github.com/ghostty-org/ghostty/commit/847b8afc872110f6cfd0c0f4690133904a06da16) libghostty: remove selection validation, way too expensive ([@mitchellh](https://github.com/mitchellh))
- [`cc48312`](https://github.com/ghostty-org/ghostty/commit/cc48312c08a0f0e08f77a8df74c15e9e367ce70e) libghostty: selection word/line/output/all helpers ([@mitchellh](https://github.com/mitchellh))
- [`e8f5353`](https://github.com/ghostty-org/ghostty/commit/e8f53539120e73e06c5bd82ab39dbf1499bf9311) example/c-vt-selection ([@mitchellh](https://github.com/mitchellh))
- [`eb777b8`](https://github.com/ghostty-org/ghostty/commit/eb777b8036d8c457ee181eab136858d1ca86aa88) libghostty: selectWordBetween in C ([@mitchellh](https://github.com/mitchellh))
- [`2ce5db2`](https://github.com/ghostty-org/ghostty/commit/2ce5db29ca162033e3cc570533184e13f3c01b53) libghostty: selection formatting ([@mitchellh](https://github.com/mitchellh))
- [`03df613`](https://github.com/ghostty-org/ghostty/commit/03df613e392b764d828941cb4f5864c5a75edb83) libghostty: detach tracked grid refs on free ([@mitchellh](https://github.com/mitchellh))
  ```text
  Tracked grid references previously held a raw terminal wrapper pointer and
  were required to be freed before the terminal. If callers kept one past
  terminal destruction, later tracked-ref calls could dereference freed
  terminal or page-list memory before detecting that the reference was no
  longer meaningful.
  
  Track live C tracked-grid-ref handles from the terminal wrapper and detach
  them before tearing down terminal storage. Detached refs now report no
  value through the tracked-ref APIs and can still be freed by the caller.
  Update the C API docs to describe this lifetime behavior and add a
  regression test for using a tracked ref after terminal free.
  
  This introduces some overhead but tracked pins shouldn't be numerous
  and this dramatically improves safety.
  ```
- [`5f08694`](https://github.com/ghostty-org/ghostty/commit/5f086947597dba0b5136d52c0b47db1d64fa5dfb) libghostty: selection APIs for C ([#12794](https://github.com/ghostty-org/ghostty/issues/12794)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Adds libghostty-vt selection APIs read/write, formatting, inspecting,
  and rendering selection state from C.
  
  | Introduced type/function | Purpose |
  | --- | --- |
  | `GhosttyRenderStateRowSelection` | Row-local inclusive selection range
  returned by render row queries. |
  | `GhosttyTerminalSelectWordOptions` | Options for deriving a word
  selection from a grid ref. |
  | `GhosttyTerminalSelectWordBetweenOptions` | Options for finding the
  nearest selectable word between two refs. |
  | `GhosttyTerminalSelectLineOptions` | Options for deriving line
  selections, including semantic prompt boundaries. |
  | `GhosttyTerminalSelectionFormatOptions` | Options for formatting the
  active or caller-provided selection. |
  | `GhosttySelectionOrder` | Describes endpoint ordering, including
  rectangular mirrored orders. |
  | `GhosttySelectionAdjust` | Operations for moving a selection endpoint.
  |
  | `ghostty_terminal_select_word` | Derive a word selection snapshot. |
  | `ghostty_terminal_select_word_between` | Derive the nearest word
  selection between two refs. |
  | `ghostty_terminal_select_line` | Derive a line selection snapshot. |
  | `ghostty_terminal_select_all` | Derive a selection covering all
  selectable content. |
  | `ghostty_terminal_select_output` | Derive a semantic command-output
  selection. |
  | `ghostty_terminal_selection_format_buf` | Format a selection into a
  caller-provided buffer. |
  | `ghostty_terminal_selection_format_alloc` | Format a selection into an
  allocated buffer. |
  | `ghostty_terminal_selection_adjust` | Mutate a selection snapshot
  endpoint. |
  | `ghostty_terminal_selection_order` | Query selection endpoint order. |
  | `ghostty_terminal_selection_ordered` | Return a selection with
  normalized endpoint order. |
  | `ghostty_terminal_selection_contains` | Test whether a point is inside
  a selection. |
  | `ghostty_terminal_selection_equal` | Compare two selection snapshots
  using terminal semantics. |
  ```
- [`c5946f4`](https://github.com/ghostty-org/ghostty/commit/c5946f4fefd9382ba00d21c1bed0b6ff33a1b687) libghostty: detach tracked grid refs on free ([#12795](https://github.com/ghostty-org/ghostty/issues/12795)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Tracked grid references previously held a raw terminal wrapper pointer
  and were required to be freed before the terminal. If callers kept one
  past terminal destruction, later tracked-ref calls could dereference
  freed terminal or page-list memory before detecting that the reference
  was no longer meaningful.
  
  Track live C tracked-grid-ref handles from the terminal wrapper and
  detach them before tearing down terminal storage. Detached refs now
  report no value through the tracked-ref APIs and can still be freed by
  the caller. Update the C API docs to describe this lifetime behavior and
  add a regression test for using a tracked ref after terminal free.
  
  This introduces some overhead but tracked pins shouldn't be numerous and
  this dramatically improves safety.
  
  No API changes due to this (just more safety).
  ```

## May 23, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26344833525), [2](https://github.com/ghostty-org/ghostty/actions/runs/26344470484), [3](https://github.com/ghostty-org/ghostty/actions/runs/26327527612)  
Summary: 3 runs • 9 commits • 4 authors

### Changes

- [`7a346dd`](https://github.com/ghostty-org/ghostty/commit/7a346dd8d40e21b14c96114c45f75eb0d347c236) macOS: fix search bar Enter key blocking IME composition ([@minorcell](https://github.com/minorcell))
  ```text
  Use onSubmit for the plain Enter → next-match behavior, which respects
  IME composition state. Keep onKeyPress only for Shift+Enter (previous
  match), returning .ignored for plain Enter so the IME can process it.
  ```
- [`da541be`](https://github.com/ghostty-org/ghostty/commit/da541bea6333458c5f4a987e734269e019a2103d) fix stray brace from conflict resolution ([@minorcell](https://github.com/minorcell))
- [`d5d8cef`](https://github.com/ghostty-org/ghostty/commit/d5d8cef4d3834cc8999eb9344066b0960b033f2d) macOS: fix search bar Enter key blocking IME composition ([#12781](https://github.com/ghostty-org/ghostty/issues/12781)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Closes https://github.com/ghostty-org/ghostty/discussions/12774
  
  `.onKeyPress(.return)` unconditionally returns `.handled`, so when IME
  is composing the return key never reaches the IME to confirm the
  candidate. The search bar gets stuck.
  
  The fix: use `.onSubmit` for the next-match navigation — it only fires
  when there is no composing text. In `.onKeyPress` only intercept
  shift+return (previous match), return `.ignored` otherwise.
  
  Tested on macOS 26.5, Ghostty 1.3.1, built from source. Chinese Pinyin
  input in the search bar works correctly after the fix.
  ```
- [`1b3c5b5`](https://github.com/ghostty-org/ghostty/commit/1b3c5b57ff50c4241c612337bc202c12823cc5d8) Update VOUCHED list ([@github-actions[bot]](https://github.com/apps/github-actions))
  ```text
  https://github.com/ghostty-org/ghostty/discussions/12775#discussioncomment-DC_kwDOHFhdAs4BA9x5
  ```
- [`2355550`](https://github.com/ghostty-org/ghostty/commit/2355550a9410f0f10bc1e88e677a9f9ed091bb71) libghostty: add tracked grid ref API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a C API for tracked pins, known as a tracked grid ref in C.
  
  The new API can create tracked refs from terminal points, snapshot them
  back to regular grid refs for cell access, convert them to coordinates,
  move them to a new point, report when their semantic location was lost,
  and free the tracked pin bookkeeping. This is backed by PageList tracked
  pins and exposed through the libghostty-vt export layer and headers.
  ```
- [`60f767d`](https://github.com/ghostty-org/ghostty/commit/60f767dd84cac94d5a6f4e827847361c42d1c078) core: guard surface left-click pins with screen generations ([@mitchellh](https://github.com/mitchellh))
  ```text
  Left-click mouse state stored a tracked pin with only the screen key that
  owned it. If the alternate screen was removed and later recreated, the key
  could match again even though the stored pin belonged to destroyed PageList
  storage.
  
  Store the screen generation alongside the left-click pin and resolve the
  pin through helpers that require both the key and generation to match. This
  keeps selection scrolling, link hover checks, pressure selection, and drag
  selection from dereferencing stale tracked pins after screen teardown.
  ```
- [`af94eac`](https://github.com/ghostty-org/ghostty/commit/af94eac1e1f26bee94b84f7d0076776dd3514d05) libghostty: add tracked grid ref API ([#12785](https://github.com/ghostty-org/ghostty/issues/12785)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a C API for tracked pins, known as a tracked grid ref in C.
  
  The new API can create tracked refs from terminal points, snapshot them
  back to regular grid refs for cell access, convert them to coordinates,
  move them to a new point, report when their semantic location was lost,
  and free the tracked pin bookkeeping. This is backed by PageList tracked
  pins and exposed through the libghostty-vt export layer and headers.
  ```
- [`7c3d950`](https://github.com/ghostty-org/ghostty/commit/7c3d9502dc6374d2563c30629f354fcd5251f141) Update VOUCHED list ([#12779](https://github.com/ghostty-org/ghostty/issues/12779)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12775#discussioncomment-17030265)
  from @bo2themax.
  
  Vouch: @minorcell
  ```
- [`a968e12`](https://github.com/ghostty-org/ghostty/commit/a968e120dd084bd886239d1cac938f0177f019d9) Update VOUCHED list ([#12780](https://github.com/ghostty-org/ghostty/issues/12780)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12775#discussioncomment-17030265)
  from @bo2themax.
  
  Vouch: @minorcell
  ```

