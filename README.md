> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: August 6, 2026 at 11:16 UTC.

## August 6, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/31075330039), [2](https://github.com/ghostty-org/ghostty/actions/runs/31070313370)  
Summary: 2 runs • 8 commits • 3 authors

### Changes

- [`49fd1ae`](https://github.com/ghostty-org/ghostty/commit/49fd1ae654c97fbc4e6f7ba94b3ee8b563378e2c) build: default dependencies to lib-vt mode ([@mitchellh](https://github.com/mitchellh))
  ```text
  Related to #10651
  
  Default Ghostty dependency builds to libghostty-vt-only mode and
  avoid initializing anything that would trigger broader dependency
  requirements.
  
  The impact of this is that Zig consumers can import ghostty-vt without
  requiring Xcode on macOS.
  ```
- [`ec58fbc`](https://github.com/ghostty-org/ghostty/commit/ec58fbc6a2da89f6d17381d56ef316f29dbf789b) build: default dependencies to lib-vt mode to avoid Xcode requirements ([#13660](https://github.com/ghostty-org/ghostty/issues/13660)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Related to #10651
  
  Default Ghostty dependency builds to libghostty-vt-only mode and avoid
  initializing anything that would trigger broader dependency
  requirements.
  
  The impact of this is that Zig consumers can import ghostty-vt without
  requiring Xcode on macOS.
  ```
- [`f0f3f4d`](https://github.com/ghostty-org/ghostty/commit/f0f3f4d8d816836e8e527dc1938841462913a1fa) GTK: move audio bell processing to the application ([@jcollie](https://github.com/jcollie))
  ```text
  This fixes #13647 by using at most one GStreamer thread per application.
  This was previously addressed in #12815 which used at most one GStreamer
  thread per surface. Originally discussed in #12808.
  ```
- [`1d6bc68`](https://github.com/ghostty-org/ghostty/commit/1d6bc6829812a448ac6148e7e86e36dff30d19fb) lib: remove cutPrefix implementation ([@jparise](https://github.com/jparise))
  ```text
  We can use std.mem.cutPrefix directly now that we're on Zig 0.16.
  ```
- [`e1fc390`](https://github.com/ghostty-org/ghostty/commit/e1fc390c192ca2ebba6b61403bb335f0d03b4d2b) GTK: move audio bell processing to the application ([#13657](https://github.com/ghostty-org/ghostty/issues/13657)) ([@jcollie](https://github.com/jcollie))
  ```text
  This fixes #13647 by using at most one GStreamer thread per application.
  This was previously addressed in #12815 which used at most one GStreamer
  thread per surface. Originally discussed in #12808.
  ```
- [`63da4e8`](https://github.com/ghostty-org/ghostty/commit/63da4e84d49d34a026ff7771699db237de65c044) lib: remove backported cutPrefix implementation ([#13658](https://github.com/ghostty-org/ghostty/issues/13658)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  We can use std.mem.cutPrefix directly now that we're on Zig 0.16.
  ```
- [`e0ef934`](https://github.com/ghostty-org/ghostty/commit/e0ef934f736089efc60288caff1061a2ba82c2fc) termio: replace SegmentedPool with std.MemoryPool ([@mitchellh](https://github.com/mitchellh))
  ```text
  The purpose of SegmentedPool was pointer-stable values for the pty write
  path, and the std.MemoryPool provides that.
  
  SegmentedPool is actually so old it predates a stdlib memory pool!
  Just noting why I did it in the first place. I also wrote it when I was
  pretty fucking bad at Zig, so I'm shocked its lasted this long.
  
  The write path is hot , so the replacement was benchmarked against the old
  SegmentedPool plus a rewrite simple Pool I did before realizing...
  wait... why not just a MemoryPool. Benchmarked using the real 240-byte xev
  write request.
  
    workload                    old                     std.MemoryPool
    depth-1 (keystroke echo)    3.93 ns/op              0.96 ns/op
    burst (1MiB paste, d=256)   4.27 ns/op              1.00 ns/op
    cold growth (32 -> 16k)     4.54 ns/op              6.48 ns/op
    malloc create/destroy       15.9 ns/op              (baseline)
  
  Cold growth is slower but this is only a cost when the pool grows.
  
  Note this also gets rid of the preallocation, which didn't show any
  measurable performance benefit at all. This has the benefit of shrinking
  our ThreadData by ~10KB.
  ```
- [`f948d42`](https://github.com/ghostty-org/ghostty/commit/f948d4207655f31ae9b95fa039e73524df43cd13) termio: replace SegmentedPool with std.MemoryPool ([#13659](https://github.com/ghostty-org/ghostty/issues/13659)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  The purpose of SegmentedPool was pointer-stable values for the pty write
  path, and the std.MemoryPool provides that.
  
  SegmentedPool is actually so old it predates a stdlib memory pool! Just
  noting why I did it in the first place. I also wrote it when I was
  pretty fucking bad at Zig, so I'm shocked its lasted this long.
  
  The write path is hot , so the replacement was benchmarked against the
  old SegmentedPool plus a rewrite simple Pool I did before realizing...
  wait... why not just a MemoryPool. Benchmarked using the real 240-byte
  xev write request.
  
  ```
    workload                    old                     std.MemoryPool
    depth-1 (keystroke echo)    3.93 ns/op              0.96 ns/op
    burst (1MiB paste, d=256)   4.27 ns/op              1.00 ns/op
    cold growth (32 -> 16k)     4.54 ns/op              6.48 ns/op
    malloc create/destroy       15.9 ns/op              (baseline)
  ```
  
  Cold growth is slower but this is only a cost when the pool grows.
  
  Note this also gets rid of the preallocation, which didn't show any
  measurable performance benefit at all. This has the benefit of shrinking
  our ThreadData by ~10KB.
  
  This was motivated by #13655
  ````

## August 5, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/31056985659), [2](https://github.com/ghostty-org/ghostty/actions/runs/31055889251), [3](https://github.com/ghostty-org/ghostty/actions/runs/31051671572), [4](https://github.com/ghostty-org/ghostty/actions/runs/31042413734), [5](https://github.com/ghostty-org/ghostty/actions/runs/31038815123), [6](https://github.com/ghostty-org/ghostty/actions/runs/31034042138), [7](https://github.com/ghostty-org/ghostty/actions/runs/31028395613), [8](https://github.com/ghostty-org/ghostty/actions/runs/31025899355), [9](https://github.com/ghostty-org/ghostty/actions/runs/31024376852), [10](https://github.com/ghostty-org/ghostty/actions/runs/31015249528), [11](https://github.com/ghostty-org/ghostty/actions/runs/30982669077), [12](https://github.com/ghostty-org/ghostty/actions/runs/30973436116), [13](https://github.com/ghostty-org/ghostty/actions/runs/30970856835)  
Summary: 13 runs • 84 commits • 11 authors

### Changes

- [`f1d2250`](https://github.com/ghostty-org/ghostty/commit/f1d225020ae68b789b663b7b0637ac52c0a38a05) core: avoid allocating for small pwd change actions ([@jparise](https://github.com/jparise))
  ```text
  Surface.handleMessage allocated a null-terminated copy for every working
  directory update.
  
  Use a small 256-byte stack-fallback buffer for common working directory
  lengths without adding significant pressure to this deep call stack. Longer
  paths retain the existing heap behavior, and performAction continues to borrow
  the value only for the duration of the call.
  ```
- [`b5e86a4`](https://github.com/ghostty-org/ghostty/commit/b5e86a42844e8be67af67c7d612a058ed8cd340c) terminal/kitty: release evicted placement pins ([@ampagent](https://github.com/ampagent))
  ```text
  Image eviction removed associated placements from storage without
  deinitializing them. Pin-backed placements therefore remained registered
  with the screen after eviction, allowing graphics-heavy output to
  accumulate stale tracked pins.
  
  Pass the owning screen through image insertion and eviction, and
  deinitialize each placement before removing it. Cover both the released
  pin and a retained image's live pin in the eviction regression test.
  ```
- [`ea21a2f`](https://github.com/ghostty-org/ghostty/commit/ea21a2f141e309fffc549d8639479622d504051b) core: avoid allocating for pwd change actions ([#13654](https://github.com/ghostty-org/ghostty/issues/13654)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Surface.handleMessage allocated a null-terminated copy for every working
  directory update. OSC 7 values fit within the parser's 2 KiB fixed
  buffer, so use stack-fallback storage sized for that bound and its
  terminator.
  
  The message type does not enforce the OSC bound, so an oversized future
  producer still falls back to the heap. performAction already borrows the
  value only for the duration of the call, preserving its existing
  lifetime.
  ```
- [`8eecb8f`](https://github.com/ghostty-org/ghostty/commit/8eecb8fdbfcc21bfda31ee759ff3ef23216d80fb) terminal: release Kitty placement pins on eviction ([#13656](https://github.com/ghostty-org/ghostty/issues/13656)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Image eviction removed associated placements from storage without
  deinitializing them. Pin-backed placements therefore remained registered
  with the screen after eviction, allowing graphics-heavy output to
  accumulate stale tracked pins.
  
  Pass the owning screen through image insertion and eviction, and
  deinitialize each placement before removing it. Cover both the released
  pin and a retained image's live pin in the eviction regression test.
  ```
- [`d02ad96`](https://github.com/ghostty-org/ghostty/commit/d02ad967b62af94d7ffaca3bbac9029966ff8824) macOS: update command options match order ([@claude](https://github.com/claude))
  ```text
  Matches are sorted in the following order:
  leadingColor > title > subtitle > description.
  
  Ranking is lexicographic on (colorScore, textScore)
  ```
- [`4371871`](https://github.com/ghostty-org/ghostty/commit/4371871bc2074c8b615583bd4a7ebc1957480d58) terminal/kitty: evict without scratch allocation ([@jparise](https://github.com/jparise))
  ```text
  Track each image's placement count in its existing metadata. This lets
  us use constant-time usage checks (rather than scans) during eviction.
  
  Select the best candidate directly from storage on each eviction, preserving
  the existing priority order: unused status, transient hint, generation, then
  ID.
  
  Since eviction no longer allocates, it can't fail, so callers no longer
  need to handle out-of-memory conditions.
  ```
- [`d28bc12`](https://github.com/ghostty-org/ghostty/commit/d28bc121a88def99cbc5ec8be1e18bc40f789325) macos: synchronize cached value access ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13276
  
  Make CachedValue safe for concurrent terminal content reads and expiry.
  
  The expiry task could previously release cached Swift String storage
  while another thread retained it, aborting the process during otherwise
  normal terminal use.
  
  Protect cached values and task handles with an NSLock, and exercise
  concurrent reads across repeated expiration in a regression test.
  ```
- [`57c1baf`](https://github.com/ghostty-org/ghostty/commit/57c1baf43ae5b576644879212ec6e9cc46284ff3) macos: defer overlapping clipboard completion ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #/13074
  
  Overlapping clipboard confirmations now defer denial until the next
  main queue turn rather than completing inside the confirmation callback.
  
  This prevents the native request state from being invalidated while its
  callback is still active, avoiding the OSC 52 crash reported in #13074.
  
  The deferred closure retains the originating surface view and completes
  the ignored request with empty data, preserving the existing deny
  behavior.
  ```
- [`8524cb5`](https://github.com/ghostty-org/ghostty/commit/8524cb593c5fa542f017744c7879c22c66a5e377) terminal/kitty: fix point deletion calculations (d=p, d=c) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fix d=p and d=c point deletion so only placements intersecting the
  target cell are removed.
  
  Previously, placements spanning multiple rows could be deleted from
  columns outside the target because the page-order comparison flattened
  row and column coordinates.
  
  Check the rectangle's column independently and use page order only for
  its row span, matching Kitty's implementation:
  https://github.com/kovidgoyal/kitty/blob/master/kitty/graphics.c
  
  NOTE: I did not look at Kitty's source prior to fixing this. I only
  referenced it after the fix to verify that the behavior matches.
  
  Spec:
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#deleting-images
  ```
- [`f973bd5`](https://github.com/ghostty-org/ghostty/commit/f973bd53ba90f161c7629d01b195b0a7f2ed88a5) terminal: report overline in DECRQSS SGR response ([@mitchellh](https://github.com/mitchellh))
  ```text
  #11638
  
  Report SGR 53 when the active cursor style has overline enabled.
  ```
- [`c9ef382`](https://github.com/ghostty-org/ghostty/commit/c9ef382fc97d8256b9c5af3e8f13841896b0db15) macos: synchronize cached value access ([#13646](https://github.com/ghostty-org/ghostty/issues/13646)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13276
  
  Make CachedValue safe for concurrent terminal content reads and expiry.
  
  The expiry task could previously release cached Swift String storage
  while another thread retained it, aborting the process during otherwise
  normal terminal use.
  
  Protect cached values and task handles with an NSLock, and exercise
  concurrent reads across repeated expiration in a regression test.
  ```
- [`ae0ff51`](https://github.com/ghostty-org/ghostty/commit/ae0ff51c42f859b483b4a5a073b7fb4941f78273) macos: defer overlapping clipboard completion ([#13648](https://github.com/ghostty-org/ghostty/issues/13648)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13074
  
  Overlapping clipboard confirmations now defer denial until the next main
  queue turn rather than completing inside the confirmation callback.
  
  This prevents the native request state from being invalidated while its
  callback is still active, avoiding the OSC 52 crash reported in #13074.
  
  The deferred closure retains the originating surface view and completes
  the ignored request with empty data, preserving the existing deny
  behavior.
  ```
- [`a61e15e`](https://github.com/ghostty-org/ghostty/commit/a61e15efd563f7b21098561e8d282999b5634985) terminal/kitty: fix point deletion calculations (d=p, d=c) ([#13652](https://github.com/ghostty-org/ghostty/issues/13652)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes https://github.com/ghostty-org/ghostty/discussions/12346
  
  Fix d=p and d=c point deletion so only placements intersecting the
  target cell are removed.
  
  Previously, placements spanning multiple rows could be deleted from
  columns outside the target because the page-order comparison flattened
  row and column coordinates.
  
  Check the rectangle's column independently and use page order only for
  its row span, matching Kitty's implementation:
  https://github.com/kovidgoyal/kitty/blob/master/kitty/graphics.c
  
  NOTE: I did not look at Kitty's source prior to fixing this. I only
  referenced it after the fix to verify that the behavior matches.
  
  Spec:
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#deleting-images
  ```
- [`090d161`](https://github.com/ghostty-org/ghostty/commit/090d161b2855a0235771954c88059399dae6e058) terminal: report overline in DECRQSS SGR response ([#13653](https://github.com/ghostty-org/ghostty/issues/13653)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  #11638
  
  Report SGR 53 when the active cursor style has overline enabled.
  ```
- [`9cb2147`](https://github.com/ghostty-org/ghostty/commit/9cb21476411cba36844d3dd67373b11a9328f5e8) terminal/kitty: evict without scratch allocation ([#13627](https://github.com/ghostty-org/ghostty/issues/13627)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Track each image's placement count in its existing metadata. This lets
  us use constant-time usage checks (rather than scans) during eviction.
  
  Select the best candidate directly from storage on each eviction,
  preserving the existing priority order: unused status, transient hint,
  generation, then ID.
  
  Since eviction no longer allocates, it can't fail, so callers no longer
  need to handle out-of-memory conditions.
  ```
- [`e886012`](https://github.com/ghostty-org/ghostty/commit/e88601239d9ea8c4f93ad123e031f789c64eca3f) macOS: update command options match order ([#13624](https://github.com/ghostty-org/ghostty/issues/13624)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Matches are sorted in the following order:
  leadingColor > title > subtitle > description.
  
  Ranking is lexicographic on (colorScore, textScore)
  
  <img height="300" alt="image"
  src="https://github.com/user-attachments/assets/1ec99e67-537e-4fc6-b595-d7eec8cbf31d"
  />
  
  
  ### AI Disclosure
  
  Claude reviewed and added unit tests, also did some refactoring of my
  original implementation.
  ```
- [`1d053bd`](https://github.com/ghostty-org/ghostty/commit/1d053bd6ea28d9109fa352862588e421c2f2767f) gtk: implement drag-to-move for splits ([@pluiedev](https://github.com/pluiedev))
  ```text
  One major todo is moving splits across different split trees (i.e.
  moving across tabs and windows), but that would involve a lot more logic.
  This MVP version works for now.
  
  GTK version of #10090
  
  Closes #10224
  ```
- [`98fae16`](https://github.com/ghostty-org/ghostty/commit/98fae16a0503548b894e4bbed84f645a79ab5210) gtk: support cross-tree surface drag and drop ([@pluiedev](https://github.com/pluiedev))
- [`261848c`](https://github.com/ghostty-org/ghostty/commit/261848c2fbd34ddb5fb74dcc8327c5ded980d691) gtk: reformat blueprints ([@pluiedev](https://github.com/pluiedev))
- [`7a04755`](https://github.com/ghostty-org/ghostty/commit/7a047553c7ab35863a0bc10ea4bc029c9a4f1993) macos: avoid IOSurface leak on automated surface creation ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13444
  
  A close while AppKit temporarily cleared/changed a surface's window would
  leak the surface in the controller's pslit tree. This retained surface kept
  a bunch of resources around, particularly large IOSurfaces.
  
  This seems to only be reproducible under scripted load: rapid terminal
  creation/destruction so that destruction happens just while there is a nil
  window on a surface view.
  
  Track surface ownership in a weak controller map updated alongside the split
  tree, with validated fallbacks for existing attachment state. Resolve
  scripted and App Intent operations through that ownership, and route
  non-confirming root closes directly through the immediate tab or window close
  path so teardown always reaches the renderer.
  ```
- [`4b4a5b2`](https://github.com/ghostty-org/ghostty/commit/4b4a5b2411091ccda2cd6373631ec7ccd184c577) renderer/metal: clear callback before layer release ([@mitchellh](https://github.com/mitchellh))
  ```text
  Clear the IOSurfaceLayer display callback when releasing the wrapper.
  The host view can retain the backing layer beyond renderer teardown.
  This prevents a later Core Animation display pass from invoking the
  callback with a freed renderer context.
  ```
- [`a177ba9`](https://github.com/ghostty-org/ghostty/commit/a177ba90af18d5df91b2b5cb8dddc0a55905c37f) macos: tolerate display link creation failures ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13293
  
  Treat Core Video display link creation as optional when macOS has no
  active displays. The previous error path reported every creation
  failure as out of memory and aborted renderer initialization.
  
  This also resyncs the display link on any display change so when
  a display becomes available it re-adds itself.
  
  Tabs created while the session is locked now initialize normally and
  fall back to event-driven rendering without vsync.
  ```
- [`15ac61d`](https://github.com/ghostty-org/ghostty/commit/15ac61db164fd6b6fdef0163ebddf3e07db4842a) gtk: implement drag-to-move for splits ([#10423](https://github.com/ghostty-org/ghostty/issues/10423)) ([@jcollie](https://github.com/jcollie))
  ```text
  One major todo is moving splits across different split trees (i.e.
  moving across tabs and windows), but that would involve a lot more
  logic. This MVP version works for now.
  
  Video demo (somehow the encode quality is terrible - I'll fix this
  later):
  
  
  https://github.com/user-attachments/assets/a5029451-9641-4680-bff6-38f52ebded4b
  
  
  GTK version of #10090
  
  Closes #10224
  ```
- [`d166c05`](https://github.com/ghostty-org/ghostty/commit/d166c05edd5732b4eb2db907d18f14a2faff77a2) font: handle missing CoreText display names ([@mitchellh](https://github.com/mitchellh))
  ```text
  CTFontCopyDisplayName can return null.
  ```
- [`74f01cf`](https://github.com/ghostty-org/ghostty/commit/74f01cf5df5c3426c37951015500c92a20afdfa9) macos: prevent stale search selection crash ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13266
  
  Keep search text and its selection range synchronized as a single
  state transition.
  
  Deleting or replacing a search term could leave a String.Index range
  from the old value attached to the text field. Applying that range
  could crash the app.
  
  Clear selection before publishing new text.
  ```
- [`7a9c369`](https://github.com/ghostty-org/ghostty/commit/7a9c369cf5da72d41946f683c48b0466a210cb7e) terminal: preserve cursor when formatting tabstops ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13269
  
  Move VT tabstop serialization ahead of screen formatting so cursor-moving
  CHA and HTS sequences run before screen state is restored.
  
  Tabstop-enabled snapshots previously finished at the final configured
  tabstop instead of the serialized cursor position. Replaying a snapshot
  could resume input in the wrong column.
  
  Keep tabstop bytes in their original pin-map accounting and extend the
  round-trip test to verify tabstops, cursor position, and map length.
  ```
- [`2b32b5b`](https://github.com/ghostty-org/ghostty/commit/2b32b5b75cfe7a31a6043a82d111065b0279b875) core: close retained temp directory handles ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13219
  
  Screen file actions intentionally retain their temporary directory so
  the generated path remains valid after dispatch. The directory and
  parent handles were retained with it, while TempDir.deinit also left the
  parent handle open.
  
  Each successful action leaked two descriptors. Repeated screen,
  scrollback, or selection writes could exhaust the process descriptor
  limit and prevent new PTYs, tabs, and windows from opening.
  
  Give TempDir an exhaustive close mode that either deletes or retains its
  contents while always releasing both handles. Defer screen-file cleanup,
  retaining only after successful dispatch, and cover both lifecycle paths
  with descriptor tests.
  ```
- [`880eded`](https://github.com/ghostty-org/ghostty/commit/880eded1586d7414874025863bbd9ebede1027e5) macos: avoid IOSurface leak on automated surface creation ([#13640](https://github.com/ghostty-org/ghostty/issues/13640)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13444
  
  A close while AppKit temporarily cleared/changed a surface's window
  would leak the surface in the controller's pslit tree. This retained
  surface kept a bunch of resources around, particularly large IOSurfaces.
  
  This seems to only be reproducible under scripted load: rapid terminal
  creation/destruction so that destruction happens just while there is a
  nil window on a surface view.
  
  Track surface ownership in a weak controller map updated alongside the
  split tree, with validated fallbacks for existing attachment state.
  Resolve scripted and App Intent operations through that ownership, and
  route non-confirming root closes directly through the immediate tab or
  window close path so teardown always reaches the renderer.
  ```
- [`bb1f590`](https://github.com/ghostty-org/ghostty/commit/bb1f5908f8ba737d0bccdc777b99aec2099f7d5f) terminfo: advertise overline support ([@mitchellh](https://github.com/mitchellh))
  ```text
  #12885
  
  Ghostty already implements SGR 53 and 55, but its terminfo description
  does not expose the corresponding Smol and Rmol capabilities. Add both
  entries so the advertised capabilities match the renderer.
  ```
- [`7cd2f65`](https://github.com/ghostty-org/ghostty/commit/7cd2f65f5cb3578d2751ae31bcbcf44189879430) terminal: color reset should set override to null, not default ([@mitchellh](https://github.com/mitchellh))
  ```text
  #12755
  
  Reset previously copied the active default into the override. This is
  wrong, a reset should unset the override and defer back to the default.
  
  Reset foreground, background, and cursor colors now resolve through the
  current default while explicit OSC overrides remain unchanged across
  configuration updates.
  
  Set a configured background in the OSC 11 regression, assert OSC 111
  clears its override, then change the default to verify the reset color
  follows it.
  ```
- [`e205647`](https://github.com/ghostty-org/ghostty/commit/e20564791e538249c99b65bf8457d3a29df9c981) libghostty-vt: spacer-tail handling needs to respect slow runtime safety ([@mitchellh](https://github.com/mitchellh))
  ```text
  Debug libghostty-vt dependencies embedded in ReleaseFast or ReleaseSmall
  binaries no longer panic when narrow text overwrites the tail of a wide
  glyph.
  
  Replace the root module's std.debug.runtime_safety gate with
  build_options.slow_runtime_safety so mixed optimization modes use the
  dependency's safety configuration consistently.
  ```
- [`b30387a`](https://github.com/ghostty-org/ghostty/commit/b30387a80f6a0aede4986251583fe1569c9819da) renderer/metal: clear callback before layer release ([#13641](https://github.com/ghostty-org/ghostty/issues/13641)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes https://github.com/ghostty-org/ghostty/discussions/13242
  
  Clear the IOSurfaceLayer display callback when releasing the wrapper.
  The host view can retain the backing layer beyond renderer teardown.
  This prevents a later Core Animation display pass from invoking the
  callback with a freed renderer context.
  
  This doesn't happen the way Ghostty GUI uses our renderer, but it is
  possible for folks using ghostty-internal and its straightforward and
  easy for us to fix it.
  ```
- [`71c2d68`](https://github.com/ghostty-org/ghostty/commit/71c2d68eb40d4e51d30d94e46e7b0c305aa4407f) macos: tolerate display link creation failures ([#13639](https://github.com/ghostty-org/ghostty/issues/13639)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13293
  
  Treat Core Video display link creation as optional when macOS has no
  active displays. The previous error path reported every creation failure
  as out of memory and aborted renderer initialization.
  
  Tabs created while the session is locked now initialize normally and
  fall back to event-driven rendering without vsync.
  ```
- [`b60970c`](https://github.com/ghostty-org/ghostty/commit/b60970ce250e9000f48e013ba9d1f9efb0316f49) macos: handle missing CoreText display names ([#13642](https://github.com/ghostty-org/ghostty/issues/13642)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes https://github.com/ghostty-org/ghostty/discussions/13262
  
  CTFontCopyDisplayName can return null.
  ```
- [`5033ea8`](https://github.com/ghostty-org/ghostty/commit/5033ea83d83c243b2eddc8a38745a791a52ee177) terminal: preserve cursor when formatting tabstops ([#13643](https://github.com/ghostty-org/ghostty/issues/13643)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13269
  
  Move VT tabstop serialization ahead of screen formatting so
  cursor-moving CHA and HTS sequences run before screen state is restored.
  
  Tabstop-enabled snapshots previously finished at the final configured
  tabstop instead of the serialized cursor position. Replaying a snapshot
  could resume input in the wrong column.
  
  Keep tabstop bytes in their original pin-map accounting and extend the
  round-trip test to verify tabstops, cursor position, and map length.
  ```
- [`0dcb411`](https://github.com/ghostty-org/ghostty/commit/0dcb41168123068d7f9a7e49b561789dcba870df) fix screen action fd leak from tempdir ([#13644](https://github.com/ghostty-org/ghostty/issues/13644)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13219
  
  Screen file actions intentionally retain their temporary directory so
  the generated path remains valid after dispatch. The directory and
  parent handles were retained with it, while TempDir.deinit also left the
  parent handle open.
  
  Each successful action leaked two descriptors. Repeated screen,
  scrollback, or selection writes could exhaust the process descriptor
  limit and prevent new PTYs, tabs, and windows from opening.
  
  Give TempDir an exhaustive close mode that either deletes or retains its
  contents while always releasing both handles. Defer screen-file cleanup,
  retaining only after successful dispatch, and cover both lifecycle paths
  with descriptor tests.
  ```
- [`78dec34`](https://github.com/ghostty-org/ghostty/commit/78dec345b25dfd9e4dbbcc4ba1d5ac040aae2204) terminfo: advertise overline support ([#13649](https://github.com/ghostty-org/ghostty/issues/13649)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  #12885
  
  Ghostty already implements SGR 53 and 55, but its terminfo description
  does not expose the corresponding Smol and Rmol capabilities. Add both
  entries so the advertised capabilities match the renderer. Tmux uses
  this to gate overline.
  ```
- [`1aeca67`](https://github.com/ghostty-org/ghostty/commit/1aeca6705eab280e12352e3866e3162002b242a0) terminal: color reset should set override to null, not default ([#13650](https://github.com/ghostty-org/ghostty/issues/13650)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  #12755
  
  Reset previously copied the active default into the override. This is
  wrong, a reset should unset the override and defer back to the default.
  
  Reset foreground, background, and cursor colors now resolve through the
  current default while explicit OSC overrides remain unchanged across
  configuration updates.
  
  Set a configured background in the OSC 11 regression, assert OSC 111
  clears its override, then change the default to verify the reset color
  follows it.
  ```
- [`9ed6142`](https://github.com/ghostty-org/ghostty/commit/9ed61428daa9f15b2dc89e73f9fe0d16d3a6bb71) libghostty-vt: spacer-tail handling needs to respect slow runtime safety ([#13651](https://github.com/ghostty-org/ghostty/issues/13651)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Debug libghostty-vt dependencies embedded in ReleaseFast or ReleaseSmall
  binaries no longer panic when narrow text overwrites the tail of a wide
  glyph.
  
  Replace the root module's std.debug.runtime_safety gate with
  build_options.slow_runtime_safety so mixed optimization modes use the
  dependency's safety configuration consistently.
  ```
- [`947e839`](https://github.com/ghostty-org/ghostty/commit/947e839930718fb1d4903f75aba5b314bb5fc1e4) macos: prevent stale search selection crash ([#13645](https://github.com/ghostty-org/ghostty/issues/13645)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13266
  
  Keep search text and its selection range synchronized as a single state
  transition.
  
  Deleting or replacing a search term could leave a String.Index range
  from the old value attached to the text field. Applying that range could
  crash the app.
  
  Clear selection before publishing new text.
  ```
- [`0060d89`](https://github.com/ghostty-org/ghostty/commit/0060d89b5be3a8b07d43599ea88fc7c5893bf36e) core: fix encoded key request cleanup ([@jparise](https://github.com/jparise))
  ```text
  Encoded key requests are owned by the caller until they are added to a
  key sequence or queued for IO. The child_exited path and failed queue
  append returned without freeing the allocated request.
  
  The existing errdefer was also too broad: after queueIo took ownership, a
  later setSelection or queueRender error could free the queued request.
  
  We now free requests in the return paths that still own them, and the
  errdefer has been removed.
  
  Also, activate a sequence only after encoding and queue append succeed
  so failure preserves the previous sequence state.
  ```
- [`168c7b9`](https://github.com/ghostty-org/ghostty/commit/168c7b94672d91cded4b506143cb0ebebc5d1ceb) core: fix encoded key request cleanup ([#13635](https://github.com/ghostty-org/ghostty/issues/13635)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Encoded key requests are owned by the caller until they are added to a
  key sequence or queued for IO. The child_exited path and failed queue
  append returned without freeing the allocated request.
  
  The existing errdefer was also too broad: after queueIo took ownership,
  a later setSelection or queueRender error could free the queued request.
  
  We now free requests in the return paths that still own them, and the
  errdefer has been removed.
  
  Also, activate a sequence only after encoding and queue append succeed
  so failure preserves the previous sequence state.
  ```
- [`8696bef`](https://github.com/ghostty-org/ghostty/commit/8696bef64486a51bb3b637c74d93a6f6079a900b) macos: guard fullscreen tab presentation ([@mitchellh](https://github.com/mitchellh))
  ```text
  #13611
  
  Route new-tab window presentation through an Objective-C exception catcher.
  
  AppKit can raise an NSInternalInconsistencyException while selecting a
  new tab in native fullscreen.
  
  Catch the presentation exception, report it through the existing error
  logging path, and leave Ghostty running when AppKit’s fullscreen window
  stack is inconsistent.
  
  This was pretty hard to reproduce but I was able to reproduce it about
  1/3rd of the time via AppleScript automation...
  ```
- [`bfd40c8`](https://github.com/ghostty-org/ghostty/commit/bfd40c84bd56965ab1a0e5112a4f3e380a31b18a) terminal: reset wrap state for CSI 2 K ([@mitchellh](https://github.com/mitchellh))
  ```text
  #13616
  
  Reset the soft-wrap state when CSI 2 K erases the complete cursor
  row. Previously, erase-to-end reset the flag while complete-line erase
  left it set.
  
  WezTerm, kitty, Alacritty, VTE, and xterm.js clear the wrap state for
  complete-line erase. xterm preserves it, but xterm copies physical rows
  during resize instead of reflowing them. Diverge from xterm so reflow in
  Ghostty does not treat erased rows as one logical line, and cover the
  behavior with a resize regression test.
  ```
- [`c247e45`](https://github.com/ghostty-org/ghostty/commit/c247e455c2b5f742ba837602ac31e85908dd1292) config: refill after ignored line boundaries ([@mitchellh](https://github.com/mitchellh))
  ```text
  Refill the line iterator when an ignored comment or blank line
  consumes the remaining buffered data.
  
  Configuration parsing previously stopped silently at these boundaries
  and left every subsequent setting unapplied.
  
  Request more data before continuing the loop and cover both comment
  and blank line boundaries with buffered-reader regression tests.
  ```
- [`713ad0e`](https://github.com/ghostty-org/ghostty/commit/713ad0eb18dc28c735c1c24f2d9a628fe5fd461f) config: refill after ignored line boundaries ([#13638](https://github.com/ghostty-org/ghostty/issues/13638)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes https://github.com/ghostty-org/ghostty/discussions/13441
  
  Refill the line iterator when an ignored comment or blank line consumes
  the remaining buffered data.
  
  Configuration parsing previously stopped silently at these boundaries
  and left every subsequent setting unapplied.
  
  Request more data before continuing the loop and cover both comment and
  blank line boundaries with buffered-reader regression tests.
  ```
- [`b1887bd`](https://github.com/ghostty-org/ghostty/commit/b1887bd71601b699a9678c92000969cac16874f6) terminal: reset wrap state for CSI 2 K ([#13637](https://github.com/ghostty-org/ghostty/issues/13637)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  #13616
  
  Reset the soft-wrap state when CSI 2 K erases the complete cursor row.
  Previously, erase-to-end reset the flag while complete-line erase left
  it set.
  
  WezTerm, kitty, Alacritty, VTE, and xterm.js clear the wrap state for
  complete-line erase. xterm preserves it, but xterm copies physical rows
  during resize instead of reflowing them. Diverge from xterm so reflow in
  Ghostty does not treat erased rows as one logical line, and cover the
  behavior with a resize regression test.
  ```
- [`d0659ba`](https://github.com/ghostty-org/ghostty/commit/d0659ba52192b1dc40c3cc671ba71aeb7780568f) macos: guard fullscreen tab presentation with objc catcher ([#13636](https://github.com/ghostty-org/ghostty/issues/13636)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  #13611
  
  Route new-tab window presentation through an Objective-C exception
  catcher.
  
  AppKit can raise an NSInternalInconsistencyException while selecting a
  new tab in native fullscreen.
  
  Catch the presentation exception, report it through the existing error
  logging path, and leave Ghostty running when AppKit’s fullscreen window
  stack is inconsistent.
  
  This was pretty hard to reproduce but I was able to reproduce it about
  1/3rd of the time via AppleScript automation...
  ```
- [`77537c8`](https://github.com/ghostty-org/ghostty/commit/77537c8065f3055d214144caab7d137543a6e133) macos: handled untrusted OSC8 hyperlinks more carefully ([@mitchellh](https://github.com/mitchellh))
  ```text
  OSC8 hyperlinks previously executed directly via the NSWorkspace opener
  so a malicious application can just do whatever it wanted and trick the
  user into opening something through Launch Services.
  
  This PR notifies apprt of OSC8 hyperlinks so they can be handled
  specially. In this PR, I added macOS-specific handling of OSC8 through a
  variety of improvements:
  
    - Preview text is sanitized, so invisible Unicode characters now show.
    - Questionable-looking URLs require confirmation to open, but a user
      can confirm to open.
    - Very questionable or definitely unsafe URLs are blocked with an
      alert that only allows the user to copy the link. The alert also
      notifies the user why.
  ```
- [`54fe8e1`](https://github.com/ghostty-org/ghostty/commit/54fe8e188552977249a084db687e75aee6bf12e9) macos: handled untrusted OSC8 hyperlinks more carefully ([#13634](https://github.com/ghostty-org/ghostty/issues/13634)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  OSC8 hyperlinks previously executed directly via the NSWorkspace opener
  so a malicious application can just do whatever it wanted and trick the
  user into opening something through Launch Services.
  
  This PR notifies apprt of OSC8 hyperlinks so they can be handled
  specially. In this PR, I added macOS-specific handling of OSC8 through a
  variety of improvements:
  
    - Preview text is sanitized, so invisible Unicode characters now show.
  - Questionable-looking URLs require confirmation to open, but a user can
  confirm to open.
  - Very questionable or definitely unsafe URLs are blocked with an alert
  that only allows the user to copy the link. The alert also notifies the
  user why.
  
  This PR also adds an explicit `link-osc8` config (default true) that
  users can use to disable osc8 completely.
  
  ## Demos
  
  ### Custom URL Schemes (Confirm)
  
  <img width="1432" height="1110" alt="CleanShot 2026-08-05 at 10 25
  57@2x"
  src="https://github.com/user-attachments/assets/f7773ca2-3389-4749-a5c9-393ae097c044"
  />
  
  ### Invisible Characters (Block)
  
  <img width="1432" height="1110" alt="CleanShot 2026-08-05 at 10 26
  44@2x"
  src="https://github.com/user-attachments/assets/bd2d0f33-f128-46e8-9bdb-227afecbb942"
  />
  
  ### Executable Target (Block)
  
  <img width="1432" height="1110" alt="CleanShot 2026-08-05 at 10 27
  31@2x"
  src="https://github.com/user-attachments/assets/080c0524-2c8e-4931-892f-d2643a5d0d4e"
  />
  ```
- [`727b8a0`](https://github.com/ghostty-org/ghostty/commit/727b8a02f8734840de664c060678dd66f01931f6) terminal: bound OSC and grapheme allocations ([@mitchellh](https://github.com/mitchellh))
  ```text
  Cap allocating OSC payloads at 8 MiB and retain at most 64 grapheme
  suffix codepoints per cell. Our limits are generous compared to other
  terminals and this prevents an easy DoS.
  
  When the grapheme codepoint max is hit we just ignore any remainders.
  This can result in real broken graphemes because Unicode spec is really
  unbounded on them but for all practical use cases its reasonable.
  
  Compared to other terminals:
  
  | Terminal | OSC capture limit | Cell codepoints |
  | --- | ---: | ---: |
  | Ghostty | 8 MiB | 65 |
  | kitty | ~256 KiB ordinary | 24 |
  | VTE | 4,096 scalars | 11 |
  | xterm | 20 or 600 KB | 3 default, 6 max |
  | Alacritty | unbounded | unbounded |
  | WezTerm | unbounded | no explicit limit |
  ```
- [`46767b5`](https://github.com/ghostty-org/ghostty/commit/46767b521358200bfe3f268f365ccd2f218db558) terminal: bound OSC and grapheme allocations ([#13633](https://github.com/ghostty-org/ghostty/issues/13633)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Cap allocating OSC payloads at 8 MiB and retain at most 64 grapheme
  suffix codepoints per cell. Our limits are generous compared to other
  terminals and this prevents an easy DoS.
  
  When the grapheme codepoint max is hit we just ignore any remainders.
  This can result in real broken graphemes because Unicode spec is really
  unbounded on them but for all practical use cases its reasonable.
  
  Compared to other terminals:
  
  | Terminal | OSC capture limit | Cell codepoints |
  | --- | ---: | ---: |
  | Ghostty | 8 MiB | 65 |
  | kitty | ~256 KiB ordinary | 24 |
  | VTE | 4,096 scalars | 11 |
  | xterm | 20 or 600 KB | 3 default, 6 max |
  | Alacritty | unbounded | unbounded |
  | WezTerm | unbounded | no explicit limit |
  ```
- [`38e891e`](https://github.com/ghostty-org/ghostty/commit/38e891e6c0bbaa50661b529424fc9fdd866ae252) terminal: require opt-in for title reports ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add an explicit libghostty-vt title-report option and keep CSI 21 t
  disabled unless an embedder enables it.
  
  Previously, registering the general PTY write callback also caused the
  terminal to echo attacker-controlled window titles. This exposed
  embedders to command injection after user interaction.
  
  Gate the response in the shared terminal stream, append the C API
  option without renumbering existing values, and cover the default,
  opt-in, and reset behavior in Zig and C API tests.
  ```
- [`ad27c98`](https://github.com/ghostty-org/ghostty/commit/ad27c989a4cc59b9e9f906cd4e07cdc8c30b332b) libghostty-vt: require opt-in for title reports ([#13632](https://github.com/ghostty-org/ghostty/issues/13632)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add an explicit libghostty-vt title-report option and keep CSI 21 t
  disabled unless an embedder enables it.
  
  Previously, registering the general PTY write callback also caused the
  terminal to echo attacker-controlled window titles. This exposed
  embedders to command injection after user interaction. Ghostty fixed
  this a long time ago by making CSI 21 t an opt-in in the config. Do the
  same but with our C/Zig API.
  ```
- [`c092b2b`](https://github.com/ghostty-org/ghostty/commit/c092b2bcf51415a83ff9a1f2fddf67caa58b1283) terminal: report DECECM as permanently reset ([@athaapa](https://github.com/athaapa))
- [`f1ca88d`](https://github.com/ghostty-org/ghostty/commit/f1ca88da37315b0ab96be66e7697cec6a5c1da45) terminal: clarify DECECM report handling ([@athaapa](https://github.com/athaapa))
- [`7bb3758`](https://github.com/ghostty-org/ghostty/commit/7bb37580084b990029f04dca366f2d7d1ca1d089) terminal: document DECECM report behavior ([@athaapa](https://github.com/athaapa))
- [`d866fa4`](https://github.com/ghostty-org/ghostty/commit/d866fa4553850050ec54eefa9daf2c63a9f4f4e5) terminal/kitty: fix graphics range deletion ([@mitchellh](https://github.com/mitchellh))
  ```text
  Use inclusive image ID bounds for the Kitty graphics protocol range
  delete operation.
  
  Range deletion previously joined the lower and upper bound checks with or,
  which matched every placement for any valid range. A targeted delete could
  therefore remove every graphics placement.
  
  Join the bounds with and and update the lowercase and uppercase range tests
  to keep placements below and above the selected interval.
  ```
- [`af2faa3`](https://github.com/ghostty-org/ghostty/commit/af2faa311a5a16b40afff8410a28da077b8ced57) terminal/kitty: restrict temporary image file paths ([@mitchellh](https://github.com/mitchellh))
  ```text
  Require temporary image file paths to match complete directory
  components when checking /tmp, /dev/shm, the configured temporary
  directory, and its resolved path.
  
  The previous byte-prefix checks accepted similarly named sibling
  directories such as /tmpX. A temporary-file transmission could read
  and unlink a file outside the permitted temporary directories.
  
  Add a component-boundary helper and regression coverage for built-in
  and configured directory prefixes. An integration test also verifies
  that a rejected file remains on disk.
  ```
- [`e5840bb`](https://github.com/ghostty-org/ghostty/commit/e5840bb9bacdaae78c42baa4b276f52eaa91fdbe) terminal/kitty: harden placement geometry ([@mitchellh](https://github.com/mitchellh))
  ```text
  Treat Kitty placement dimensions and offsets as untrusted values when
  calculating pixel, grid, and rectangle geometry. Saturate results that
  do not fit and return no rectangle when missing pixel metrics produces
  an empty grid.
  
  Unchecked u32 arithmetic previously panicked in safe builds and wrapped
  in fast builds. A zero row count could underflow into a maximum-size
  page traversal, while maximum dimensions could spin cursor movement or
  overflow render visibility calculations.
  
  Use checked integer scaling instead of floating-point casts, saturating
  arithmetic for extents and cursor columns, and bound off-screen cursor
  work to the terminal row count. Compute C API visibility in i64 and
  cover maximum protocol values in storage, execution, and render-info
  tests.
  ```
- [`fb4c561`](https://github.com/ghostty-org/ghostty/commit/fb4c56159fe8c6c19fa84c2a6691a44098c65e78) core: transfer long key encoding buffer ([@jparise](https://github.com/jparise))
  ```text
  The long-preedit fallback introduced in e95b1707c intentionally allocated
  twice. The encoder wrote into an oversized caller-owned buffer and returned
  only the written subslice, so transferring it required manually shrinking
  the allocation or tracking its original capacity. The copy kept that rare
  path simple.
  
  The key encoder moved to std.Io.Writer.Allocating in 44496df899. Its
  toOwnedSlice method handles shrinking and ownership transfer, remapping when
  the allocator supports it and falling back to an allocation and copy when it
  does not. Use it directly for WriteReq.alloc to remove the guaranteed second
  allocation while preserving cleanup on failure.
  ```
- [`ec04900`](https://github.com/ghostty-org/ghostty/commit/ec04900ab957c7637584e2002aeb6f24c985bd70) terminal/kitty: validate opened image file paths ([@mitchellh](https://github.com/mitchellh))
  ```text
  Validate Kitty file transmissions against a canonical path derived from
  the open file handle. Keep temporary file policy and cleanup keyed to
  that handle path.
  
  Path validation previously ran before opening, so a local cooperating
  process could replace a symlink or directory entry and make Ghostty
  read a blocklisted file.
  
  Open the submitted path once, derive its canonical path from the handle,
  and use the same handle for stat and reads. Add a regression test that
  replaces a blocked symlink after open and verifies the pinned target is
  still rejected.
  ```
- [`f766f30`](https://github.com/ghostty-org/ghostty/commit/f766f303a7d39b9f41fdda1b6d71b329f410d45f) terminal/kitty: validate shared memory ranges ([@mitchellh](https://github.com/mitchellh))
  ```text
  Validate Kitty shared memory byte ranges before mapping and copying
  image data. Interpret S as a byte count from O and preserve default
  raw-image sizing.
  
  Shared memory transmissions previously multiplied untrusted u32
  dimensions before the limit check and sliced mappings with an unchecked
  offset. Malformed commands could panic in safe builds or request a
  wrapped allocation in fast builds.
  
  Reject oversized dimensions before widening size arithmetic, derive
  bounded ranges from the stat size, and enforce max_size before
  constructing a slice. Add regression tests for explicit and implicit
  offsets, out-of-bounds offsets, and maximum dimensions.
  ```
- [`590d669`](https://github.com/ghostty-org/ghostty/commit/590d669c4a72eb9cb990bf0162071c2b9eb0f7ad) terminal/kitty: limit png decoder allocations ([@mitchellh](https://github.com/mitchellh))
  ```text
  Limit individual allocator requests made by PNG decoders to the Kitty
  graphics protocol's 400 MiB image ceiling. Add a reusable allocator
  wrapper for callers that need per-request bounds.
  
  PNG decoding previously used Wuffs' 4 GiB package limit and checked
  the result only after allocation. A tiny PNG with oversized dimensions
  could cause a multi-gigabyte RSS spike before being rejected.
  
  Wrap decoder allocators with LimitedAllocator and translate limit
  rejections to invalid image data while preserving genuine out-of-memory
  errors. Add allocator boundary tests and regression coverage for a
  crafted PNG below Wuffs' limit.
  ```
- [`d0c516f`](https://github.com/ghostty-org/ghostty/commit/d0c516f8f384ee4cc3304c4eef3dabc07c432de4) terminal/kitty: release replaced placement pins ([@mitchellh](https://github.com/mitchellh))
  ```text
  Release a Kitty graphics placement's tracked pin before replacement.
  
  Repeated updates to an external placement previously leaked tracked pins.
  
  Pass the owning screen to storage and deinitialize the old placement.
  ```
- [`402b922`](https://github.com/ghostty-org/ghostty/commit/402b9227de1efab24de981ce0d71b4d378417490) terminal/kitty: reclaim pruned placements ([@mitchellh](https://github.com/mitchellh))
  ```text
  Reclaim pin-backed Kitty graphics placements after their tracked screen
  content is pruned. Treat garbage pins as non-renderable until the next
  placement command sweeps them.
  
  Placements that scrolled beyond retained history previously remained in
  the placement map and tracked-pin set. Long-running graphics output could
  accumulate stale state, and remapped garbage pins could appear at an
  unrelated fallback location.
  
  Sweep garbage placements before growing the placement map, releasing each
  tracked pin while preserving virtual placements. Return no geometry or
  visible render position for garbage pins and cover both storage and C API
  behavior with regression tests.
  ```
- [`e206558`](https://github.com/ghostty-org/ghostty/commit/e2065583a41e576cd94927832d8e8b72f0cae1f1) core: transfer long key encoding buffer ([#13628](https://github.com/ghostty-org/ghostty/issues/13628)) ([@jcollie](https://github.com/jcollie))
  ```text
  The long-preedit fallback introduced in e95b1707c intentionally
  allocated twice. The encoder wrote into an oversized caller-owned buffer
  and returned only the written subslice, so transferring it required
  manually shrinking the allocation or tracking its original capacity. The
  copy kept that rare path simple.
  
  The key encoder moved to std.Io.Writer.Allocating in 44496df899. Its
  toOwnedSlice method handles shrinking and ownership transfer, remapping
  when the allocator supports it and falling back to an allocation and
  copy when it does not. Use it directly for WriteReq.alloc to remove the
  guaranteed second allocation while preserving cleanup on failure.
  ```
- [`dd03528`](https://github.com/ghostty-org/ghostty/commit/dd035284c2c548c139e4b312751f7b9ef628d251) Kitty graphics protocol bugs ([#13630](https://github.com/ghostty-org/ghostty/issues/13630)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Specifics in each commit message. This will be part of a security
  advisory in 1.4.0 since these patches issues related to overflows, DoS,
  unbounded memory allocation, etc.
  ```
- [`33d34cf`](https://github.com/ghostty-org/ghostty/commit/33d34cf5ce7bece9e108aaab069584c0628300be) terminal: avoid VS15 cursor underflow ([@mitchellh](https://github.com/mitchellh))
  ```text
  Handle VS15 width changes when the wide grapheme base is directly under
  the cursor. Cover both disabled wraparound and restored pending-wrap
  cursor states.
  
  A zero cursor distance previously underflowed while locating the spacer
  tail. Debug builds panicked and ReleaseFast computed an out-of-bounds
  cell pointer before updating it.
  
  Find the spacer from the wide base instead of subtracting from the
  cursor distance. Reposition the cursor from the base column and clamp it
  to the active right margin.
  ```
- [`fe98aef`](https://github.com/ghostty-org/ghostty/commit/fe98aef21cf29e06555a3c76527923eb0256af2b) terminal: report DECECM as permanently reset ([#12660](https://github.com/ghostty-org/ghostty/issues/12660)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Closes #12505
  
  This PR allows Ghostty to respond to DECRQM queries for DECECM with the
  "permanently reset".
  
  AI disclosure: I used Codex to help inspect the relevant code path and
  explain the issue, but I reviewed and made the code changes myself.
  ```
- [`bd21ff1`](https://github.com/ghostty-org/ghostty/commit/bd21ff153e047f2480086aa4eb88c88fa8368823) terminal: avoid VS15 cursor underflow ([#13631](https://github.com/ghostty-org/ghostty/issues/13631)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Handle VS15 width changes when the wide grapheme base is directly under
  the cursor.
  
  A zero cursor distance previously underflowed while locating the spacer
  tail. Debug builds panicked and ReleaseFast computed an out-of-bounds
  cell pointer before updating it.
  ```
- [`f17b425`](https://github.com/ghostty-org/ghostty/commit/f17b425aac518acd7cb7cbc500b862656631a4a8) surface: use id instead of intFromPtr ([@pluiedev](https://github.com/pluiedev))
  ```text
  intFromPtr was always a hack that we had to use before we had stable
  surface IDs, and it was always slightly unsafe. Let's do it properly
  this time.
  ```
- [`c93752a`](https://github.com/ghostty-org/ghostty/commit/c93752a008b5a9a9a717c9e2bea4742d7efb4c00) macOS: suppress restart tips for auto update ([@bo2themax](https://github.com/bo2themax))
- [`5b70f20`](https://github.com/ghostty-org/ghostty/commit/5b70f208bc6870bb32f13720376840edc3c5ed31) terminal: print repeated characters through printSlice ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  While doing some work on my tmux fork I noticed multiple parts of
  libghostty-vt was slower than tmux equivalents(isolated). Turns out they
  do some smart stuff there.
  
  printRepeat called print() once per repeat, so something like \x1b[2000b
  ran grapheme checks, width lookups, wrap handling, etc etc 2000 times.
  
  printSlice is already documented as semantically identical to
  calling print per codepoint, so this just feeds the repeated
  codepoint through it in 4096-entry stack chunks. Simple runs take
  the batched fast path, and anything that needs care falls back to the
  previous behaviour.
  ```
- [`19e9f49`](https://github.com/ghostty-org/ghostty/commit/19e9f49089606310bb717a6a8e49174ffdd0e90a) surface: use id instead of intFromPtr ([#13620](https://github.com/ghostty-org/ghostty/issues/13620)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  intFromPtr was always a hack that we had to use before we had stable
  surface IDs, and it was always slightly unsafe. Let's do it properly
  this time.
  ```
- [`3f8b99b`](https://github.com/ghostty-org/ghostty/commit/3f8b99bb68cb46381924f33496b7e6a25d3859a8) terminal: print repeated characters through printSlice ([#13625](https://github.com/ghostty-org/ghostty/issues/13625)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  `printRepeat` (CSI `b`, repeat the previous character N times) calls
  `print()` once per repeat, so something like `\x1b[2000b` ran grapheme
  checks, width lookups, wrap handling, and the integrity assert 2000
  times for what is usually the same character on the same row.
  
  `Terminal.print` was 24% of samples on a REP-heavy micro benchmark.
  
  This PR just aims to add a fast path by introducing a chunking
  mechanism. anything that needs care (insert mode, grapheme clustering,
  hyperlinks) still falls back to per-codepoint print() inside printSlice,
  so behavior *should* stay unchanged.
  
  Some profiling data:
  
  Generated with some plain stupid logic:
  
  ```py
  D = "benchdata"
  parts, total = [], 0
  while total < 40_000_000:
      line = "x" + "\x1b[80b" + "y" + "\x1b[35b" + "\r\n"
      parts.append(line); total += len(line)
  open(f"{D}/rep.bin", "wb").write("".join(parts).encode())
  ```
  **macOS (hyperfine, 15 runs, warmup 3):**
  
  | | mean |
  |---|---|
  | before | 2.360 s |
  | after | 1.166 s |
  
  
  And now the really interesting and promising stuff
  
  **Linux, 24-core NixOS x86_64 (poop, 6s sampling):**
  
  | | wall_time | instructions | branch_misses | peak_rss |
  |---|---|---|---|---|
  | before | 1.51 s | 50.9 G | 9.41 M | 6.82 MB |
  | after | 562 ms | 9.07 G | 114 K | 6.74 MB |
  ````
- [`5944ab2`](https://github.com/ghostty-org/ghostty/commit/5944ab286d825b48b68d0e99088273cf435d6870) macOS: suppress restart tips for auto update ([#13623](https://github.com/ghostty-org/ghostty/issues/13623)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  With this, users will not be prompted to restart the app when an
  automatic update is ready. Relaunching with this state will have no
  visible difference to users.
  
  If the user checks for updates manually, either by menu, command
  palette, or keybind, a restart alert will be prompted.
  
  Closes #13478
  
  Auto updates:
  
  
  https://github.com/user-attachments/assets/f77f65a1-6e2f-4002-961c-fee4b73d447e
  
  Manual Updates:
  
  
  https://github.com/user-attachments/assets/8a52a5a0-2022-413f-97c5-6f9a2eb26e7a
  ```
- [`f5419b9`](https://github.com/ghostty-org/ghostty/commit/f5419b9b151e85c027f481f045f586e10ddf1d01) gtk: do not set bell ringing if already focused ([@lotheac](https://github.com/lotheac))
- [`9e30f70`](https://github.com/ghostty-org/ghostty/commit/9e30f70f23418fecbdca1088673000417527c4e4) gtk: do not set bell ringing if already focused ([#13597](https://github.com/ghostty-org/ghostty/issues/13597)) ([@pluiedev](https://github.com/pluiedev))
- [`2346c4f`](https://github.com/ghostty-org/ghostty/commit/2346c4fe4767373cda50b5977d95191f714b1cca) Update VOUCHED list ([#13617](https://github.com/ghostty-org/ghostty/issues/13617)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12984#issuecomment-5187316604)
  from @mitchellh.
  
  Denounce: @jamesarch
  ```
- [`a86c49d`](https://github.com/ghostty-org/ghostty/commit/a86c49d7af2a92e945487f52e821ee478e276fad) macOS: rename UpdateState.isIdle to isHidden ([@bo2themax](https://github.com/bo2themax))
- [`a00d155`](https://github.com/ghostty-org/ghostty/commit/a00d155e9cb31829a27c3342653e30c6220e93ca) config: limit command translations to GTK ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13614
  
  Only translate the shared default commands when building the GTK runtime.
  macOS now use the source strings until we do broader localization.
  ```
- [`d2f08f1`](https://github.com/ghostty-org/ghostty/commit/d2f08f1589cbe73e1f7cbedc2db9c5e1ae5a1ca6) config: limit command translations to GTK ([#13615](https://github.com/ghostty-org/ghostty/issues/13615)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13614
  
  Only translate the shared default commands when building the GTK
  runtime. macOS now use the source strings until we do broader
  localization.
  ```
- [`d7f7a4e`](https://github.com/ghostty-org/ghostty/commit/d7f7a4e736d47bb3501d22cc9118b23dd398a764) macOS: rename UpdateState.isIdle to isHidden ([#13613](https://github.com/ghostty-org/ghostty/issues/13613)) ([@mitchellh](https://github.com/mitchellh))

## August 4, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/30953205060), [2](https://github.com/ghostty-org/ghostty/actions/runs/30941010176), [3](https://github.com/ghostty-org/ghostty/actions/runs/30930443397), [4](https://github.com/ghostty-org/ghostty/actions/runs/30927144840), [5](https://github.com/ghostty-org/ghostty/actions/runs/30924765500), [6](https://github.com/ghostty-org/ghostty/actions/runs/30918428683), [7](https://github.com/ghostty-org/ghostty/actions/runs/30913840647), [8](https://github.com/ghostty-org/ghostty/actions/runs/30907032744), [9](https://github.com/ghostty-org/ghostty/actions/runs/30877679965)  
Summary: 9 runs • 36 commits • 10 authors

### Changes

- [`63d08c0`](https://github.com/ghostty-org/ghostty/commit/63d08c0342ba4b5132de7b3098797a80eba8b757) macOS: show cancel update option when its actually cancellable ([@bo2themax](https://github.com/bo2themax))
  ```text
  `extracting` and `installing` state aren't cancellable by us
  ```
- [`ccb08f3`](https://github.com/ghostty-org/ghostty/commit/ccb08f35f683d6087786dda8e793e911ef1a2f8a) macOS: show cancel update option when its actually cancellable ([#13612](https://github.com/ghostty-org/ghostty/issues/13612)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `extracting` and `installing` state aren't cancellable by us.
  
  > Recommend reviewing with whitespace hidden
  ```
- [`02f3483`](https://github.com/ghostty-org/ghostty/commit/02f34835ea48b9daee0abdcc09fca02702def688) datastruct: remove unused LRU implementation ([@Uzaaft](https://github.com/Uzaaft))
- [`8cfbaf5`](https://github.com/ghostty-org/ghostty/commit/8cfbaf545ab4215ccc9820ba905f502387d1de1f) config: formatted action should be parsable into the original ([@bo2themax](https://github.com/bo2themax))
- [`b67f8ef`](https://github.com/ghostty-org/ghostty/commit/b67f8ef51d8092ff3aaf52574a89c98f9f46b0ca) config: don't escape Binding.Action.String ([@bo2themax](https://github.com/bo2themax))
- [`066a0b7`](https://github.com/ghostty-org/ghostty/commit/066a0b7c45e50694df0c3c3892961523162a55ad) macOS: show description when subtitle missing in CommandPalette ([@bo2themax](https://github.com/bo2themax))
- [`51cf099`](https://github.com/ghostty-org/ghostty/commit/51cf099678d90775b3c587e5e34427531396d75e) datastruct: remove unused LRU implementation ([#13607](https://github.com/ghostty-org/ghostty/issues/13607)) ([@jcollie](https://github.com/jcollie))
- [`760a250`](https://github.com/ghostty-org/ghostty/commit/760a2500291df56c42cccd4d34efeeceaf8bd6ae) config: formatted action should be parsable into the original  ([#13609](https://github.com/ghostty-org/ghostty/issues/13609)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This fixes the issue where an action with string as it's parameter is
  not working correctly in CommandPalette, found in #9671. For example:
  
  ```
  command-palette-entry = title:"Set Ghostty Title",description:test sending text.,action:set_tab_title:👻
  keybind=cmd+r=set_tab_title:👻
  ```
  
  Keybind works perfectly, but the title is escaped when triggering in
  CommandPalette.
  
  > Introduced in
  [#8873](https://github.com/ghostty-org/ghostty/pull/8873/changes#diff-9e7936787320bcf70e332c868125039d8c0a7f96c4a88f2af0af21d952c6830dR1216),
  I tested the fixed issue as well, the following config still parses
  correctly, mentioned in
  https://github.com/ghostty-org/ghostty/issues/8849#issuecomment-3322018212.
  
  ```
  command-palette-entry = title:Focus Split: Next,description:"Focus the next split, if any.",action:goto_split:next
  ```
  
  Also `ghostty +show-config` now will also output the readable strings as
  well.
  <img width="1078" height="428" alt="image"
  src="https://github.com/user-attachments/assets/f9dc1447-7b4e-44f4-8362-b54f4d805c7a"
  />
  ````
- [`b8ab2ff`](https://github.com/ghostty-org/ghostty/commit/b8ab2ff16847b73afd2ea99498e44ab6694e930f) macOS: show/search description when subtitle missing in CommandPalette ([#13610](https://github.com/ghostty-org/ghostty/issues/13610)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  <img width="1125" height="552" alt="image"
  src="https://github.com/user-attachments/assets/09866c9b-d5c4-422f-860b-de4de4cca055"
  />
  ```
- [`48d85ea`](https://github.com/ghostty-org/ghostty/commit/48d85eaeb06ac9fc49073815bda5bac97de655ca) core: fix mouse reporting mutex lock ([@mitchellh](https://github.com/mitchellh))
- [`488b710`](https://github.com/ghostty-org/ghostty/commit/488b7109bb4df41589846e1e872db114d3d6c9bb) gtk: forward middle click to TUIs with mouse reporting ([@ajr-khll](https://github.com/ajr-khll))
- [`ca56412`](https://github.com/ghostty-org/ghostty/commit/ca56412bf28ae4de7e323d4b30b39844501be05b) gtk: forward middle click to TUIs with mouse reporting ([#13108](https://github.com/ghostty-org/ghostty/issues/13108)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fix for Issue #12940
  I actually do not know if this has already been resolved and the issue
  is just still open. Either way, here's a fix. Now we run a check to see
  if the current program is accepting mouse events before discarding the
  middle click.
  ```
- [`08342c9`](https://github.com/ghostty-org/ghostty/commit/08342c92446ceda22b49f42ce39e8c4714054a6e) Update VOUCHED list ([#13603](https://github.com/ghostty-org/ghostty/issues/13603)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13602#discussioncomment-17895866)
  from @jcollie.
  
  Vouch: @UnsaltedScholar
  ```
- [`df23bef`](https://github.com/ghostty-org/ghostty/commit/df23bef0e91d602ab4b95e33ef9a4c213a1058da) i18n: translation support for command palete and Latvian translation for it ([@EriksRemess](https://github.com/EriksRemess))
- [`1125fa2`](https://github.com/ghostty-org/ghostty/commit/1125fa26df6387131295fb4433ffcab411f0bcfc) i18n: note about i18n.N_ usage and @inComptime() return msgid for i18n._ ([@EriksRemess](https://github.com/EriksRemess))
- [`e0744dd`](https://github.com/ghostty-org/ghostty/commit/e0744dde62c53555aa6b9457e2bb9fd8c74a1dc2) i18n - command palette - empty translations ([@EriksRemess](https://github.com/EriksRemess))
- [`cfa0ca7`](https://github.com/ghostty-org/ghostty/commit/cfa0ca710659175d3ae21b2c136dcf1024fd5d91) macos: defer transparent titlebar KVO rebinding ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13386
  
  Defer transparent-titlebar KVO rebinding to the next main-queue turn.
  Track the observed tab group so unchanged bindings are preserved.
  
  Previously, a tab-group callback could invalidate and recreate its own
  observation before returning, leaving closed terminal windows registered
  with AppKit after the undo timeout. These windows accumulated titlebar and
  layer state, increasing memory use and WindowServer CPU with tab churn.
  
  Validated with an AppDelegate change that sat and created/closed tabs
  in a loop, then counted weak controllers/windows/nsapp window.
  ```
- [`363e6e6`](https://github.com/ghostty-org/ghostty/commit/363e6e6b427c1f3a6647b14692f1953746d83045) i18n: translation support for command palete ([#11641](https://github.com/ghostty-org/ghostty/issues/11641)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Most obvious next step in translating Ghostty is the command palette.
  Added support for i18n.N_ (https://docs.gtk.org/glib/i18n.html#macros).
  Made a Latvian translation for the command palette to test. Codex did
  bulk of the translations but I verified them.
  ```
- [`594ee21`](https://github.com/ghostty-org/ghostty/commit/594ee212bc3c048ffa06ba90623eaf207a4d145c) macos: defer transparent titlebar KVO rebinding ([#13601](https://github.com/ghostty-org/ghostty/issues/13601)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13386, based on
  https://github.com/mustafa0x/ghostty/commit/a8c090
  
  Defer transparent-titlebar KVO rebinding to the next main-queue turn.
  Track the observed tab group so unchanged bindings are preserved.
  
  Previously, a tab-group callback could invalidate and recreate its own
  observation before returning, leaving closed terminal windows registered
  with AppKit after the undo timeout. These windows accumulated titlebar
  and layer state, increasing memory use and WindowServer CPU with tab
  churn.
  
  Validated with an AppDelegate change that sat and created/closed tabs in
  a loop, then counted weak controllers/windows/nsapp window.
  ```
- [`85083d2`](https://github.com/ghostty-org/ghostty/commit/85083d23cd12e2959f11dd247916c43a51f5f10e) config: clarify cursor-click-to-move's relation to shell-integration ([@lotheac](https://github.com/lotheac))
  ```text
  the original wording is a bit confusing; I thought cursor-click-to-move
  required shell-integration to be enabled, and was confused when the
  mouse was still moving my cursor in fish even with
  shell-integration=none.
  ```
- [`1f6e266`](https://github.com/ghostty-org/ghostty/commit/1f6e26642e540ddf01803858772909c4fab33428) config: clarify cursor-click-to-move's relation to shell-integration ([#13589](https://github.com/ghostty-org/ghostty/issues/13589)) ([@jparise](https://github.com/jparise))
- [`bdd849f`](https://github.com/ghostty-org/ghostty/commit/bdd849fc2feff762612c2d057db7e013c118e390) Update VOUCHED list ([#13596](https://github.com/ghostty-org/ghostty/issues/13596)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/13589#issuecomment-5178660481)
  from @jparise.
  
  Vouch: @lotheac
  ```
- [`9e6e2ea`](https://github.com/ghostty-org/ghostty/commit/9e6e2ea964587757b0e26178950c624c955ee6ed) renderer: reset terminal state cleanup counter ([@jparise](https://github.com/jparise))
  ```text
  Reset the frame counter whenever retained render state is cleared.
  Otherwise, every subsequent frame will be deinitialized and rebuilt.
  ```
- [`04f1bc0`](https://github.com/ghostty-org/ghostty/commit/04f1bc0960908ede6976f4030408454481605fc0) winproto/wayland: disable custom blur on GTK >=4.23.3 ([@pluiedev](https://github.com/pluiedev))
  ```text
  GTK 4.23.3 added its own (much smarter) implementation of background blur,
  which means our implementation is not only redundant, it also crashes the
  program because a surface cannot have multiple associated blur objects.
  Ergo, don't do custom blur on newer GTK versions.
  
  See #13578
  ```
- [`3263fc6`](https://github.com/ghostty-org/ghostty/commit/3263fc6c4b6e3e85155797d85086480aba6b7375) gtk: use native blur on GTK 4.23.3+ ([@pluiedev](https://github.com/pluiedev))
  ```text
  Finally, what was previously thought impossible, is now possible.
  The blur region itself is far more accurate than what we can conjure up
  on our own, and in a much more finetuned and detailed way too.
  Thank you, GTK devs!
  ```
- [`b11d608`](https://github.com/ghostty-org/ghostty/commit/b11d60818a8b311db39c3b8cb0a10f6d51bdec44) synthetic: styled output generator ([@mitchellh](https://github.com/mitchellh))
- [`85b1dd0`](https://github.com/ghostty-org/ghostty/commit/85b1dd0dd9a3b3216eed939a5b8274209a1f4587) benchmark: formatter benchmark ([@mitchellh](https://github.com/mitchellh))
- [`8838c37`](https://github.com/ghostty-org/ghostty/commit/8838c37f4c60f9fc0bcaf796ae43dd5ed958c040) terminal: fast print styles ([@mitchellh](https://github.com/mitchellh))
- [`79aa256`](https://github.com/ghostty-org/ghostty/commit/79aa256fa26c06f4cf89a9962ab8faf40a210642) terminal: speed up formatter mostly by avoiding std.fmt ([@mitchellh](https://github.com/mitchellh))
- [`d4391ff`](https://github.com/ghostty-org/ghostty/commit/d4391ff835fba87d3f6616b94299ab358c4cef1a) fastprint: fix compile errors ([@mitchellh](https://github.com/mitchellh))
- [`2b6a1e4`](https://github.com/ghostty-org/ghostty/commit/2b6a1e41fcedd93d620e4462372606371bde8a56) macos: avoid leaking ports while awaiting accessibility ([@mitchellh](https://github.com/mitchellh))
  ```text
  #11799
  
  Creating a CGEventTap without Accessibility permission leaks a Mach
  port inside CoreGraphics on every failed attempt. The global keybind
  listener retried this once per second while waiting for permission, so
  Ghostty eventually exhausted the process port limit.
  
  Request Accessibility access once, poll AXIsProcessTrusted while
  access is denied, and create the event tap only after access is
  granted. Stop polling before creation so an unrelated tap failure
  cannot restart the leaking retry loop.
  ```
- [`2ed67ca`](https://github.com/ghostty-org/ghostty/commit/2ed67cadd1c5f52d2eaedf2f99968eed0c6eac15) terminal: redesign pin map for formatter ([@mitchellh](https://github.com/mitchellh))
- [`74b4264`](https://github.com/ghostty-org/ghostty/commit/74b426458b7b4a53c15a7e19a55c50e605ba7690) gtk: use native blur on GTK 4.23.3+ ([#13586](https://github.com/ghostty-org/ghostty/issues/13586)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Finally, what was previously thought impossible, is now possible.
  The blur region itself is far more accurate than what we can conjure up
  on our own, and in a much more finetuned and detailed way too.
  Thank you, GTK devs!
  
  Closes #13581
  ```
- [`e69dc2b`](https://github.com/ghostty-org/ghostty/commit/e69dc2bee8ac57f853ee07590548590a35aab89b) renderer: reset terminal state cleanup counter ([#13585](https://github.com/ghostty-org/ghostty/issues/13585)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Reset the frame counter whenever retained render state is cleared.
  Otherwise, every subsequent frame will be deinitialized and rebuilt.
  ```
- [`b9d8829`](https://github.com/ghostty-org/ghostty/commit/b9d88292be587388a336a2e59c08c4e993c04109) terminal: speed up formatting anywhere from ~1.5x to ~8x ([#13587](https://github.com/ghostty-org/ghostty/issues/13587)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This PR speeds up our formatting (plain text, html, and VT) by anywhere
  from ~1.5x to ~8x.
  
  The formatter is the hot path behind multiple features in Ghostty GUI:
  clipboard copy (plain/VT/HTML), `write_screen_file`, `selectionString`,
  and terminal search sliding window. It's also the hot path for
  libghostty users, namely people like
  [zmx](https://github.com/neurosnap/zmx) which utilize the VT formatter
  to restore a terminal.
  
  This PR also adds the benchmarking infrastructure for the formatter.
  
  ## How
  
  - **Fast cell-run optimization.** For simple cells (single codepoint, no
  style/hyperlink) we encode them as a single run rather than one at a
  time.
  - **Make some arguments comptime.** Generates more code but benchmarks
  show it improves things, specifically for per-format switches that we do
  a LOT.
  - **Interned style id fast path.** Styles are interned per page, so id
  equality implies style equality. We track the id of the active style and
  skip the per-cell `Style` copy + `eql` when it matches.
  - **Fast printing.** Avoid `std.fmt` where possible and assemble
  integers, RGB colors, codepoints in fixed-width buffers with a single
  memcpy. This was extracted partially to `fastprint.zig` so we can reuse
  it.
  - **Avoid double-formatting for tracked pins.** Previously we formatted
  twice (once through a `Discarding` writer to count bytes) for pin maps.
  Now I'm smarter about it and do a single pass.
  
  ## Performance
  
  All on my machine, 80x24 terminal, 10K lines of scrollback.
  
  | workload              | main     | this PR  | speedup | throughput |
  | --------------------- | -------- | -------- | ------- | ---------- |
  | plain / plain         | 5.74 ms  | 1.67 ms  | 3.4x    | 364 MB/s   |
  | plain / vt            | 6.46 ms  | 1.04 ms  | 6.2x    | 596 MB/s   |
  | plain / html          | 7.39 ms  | 2.32 ms  | 3.2x    | 308 MB/s   |
  | unicode / plain       | 9.74 ms  | 5.42 ms  | 1.8x    | 276 MB/s   |
  | unicode / vt          | 10.42 ms | 5.53 ms  | 1.9x    | 275 MB/s   |
  | unicode / html        | 12.53 ms | 7.35 ms  | 1.7x    | 509 MB/s   |
  | styled / plain        | 5.65 ms  | 1.69 ms  | 3.4x    | 360 MB/s   |
  | styled / vt           | 9.07 ms  | 4.20 ms  | 2.2x    | 409 MB/s   |
  | styled / html         | 10.78 ms | 6.64 ms  | 1.6x    | 740 MB/s   |
  | mixed / plain         | 8.59 ms  | 4.81 ms  | 1.8x    | 226 MB/s   |
  | mixed / vt            | 11.25 ms | 6.65 ms  | 1.7x    | 250 MB/s   |
  | mixed / html          | 14.47 ms | 10.52 ms | 1.4x    | 414 MB/s   |
  | wrapped / plain       | 7.30 ms  | 1.11 ms  | 6.6x    | 733 MB/s   |
  | wrapped / vt          | 8.14 ms  | 1.04 ms  | 7.8x    | 789 MB/s   |
  | wrapped / html        | 9.00 ms  | 2.12 ms  | 4.2x    | 465 MB/s   |
  | pin-map / plain       | 12.51 ms | 3.80 ms  | 3.3x    |            |
  | pin-map / vt          | 13.12 ms | 2.99 ms  | 4.4x    |            |
  | active screen / plain | 12.5 µs  | 2.7 µs   | 4.6x    |            |
  | active screen / vt    | 18.4 µs  | 6.8 µs   | 2.7x    |            |
  
  Workloads:
  - `plain` is ASCII lines
  - `unicode` is 2/3/4-byte codepoints with 10% grapheme clusters
  - `styled` is heavy SGR churn
  - `mixed` is styles + Unicode + hyperlinks
  -  `wrapped` is a continuous soft-wrapped stream
  - `pin-map`/`active screen` are the selectionString/search-style and
  visible-screen-only cases respectively.
  ```
- [`6687d60`](https://github.com/ghostty-org/ghostty/commit/6687d6089dc254b14b1cdb22ca310f8394c3290f) macos: avoid leaking ports while awaiting accessibility ([#13590](https://github.com/ghostty-org/ghostty/issues/13590)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  #11799
  
  Creating a CGEventTap without Accessibility permission leaks a Mach port
  inside CoreGraphics on every failed attempt. The global keybind listener
  retried this once per second while waiting for permission, so Ghostty
  eventually exhausted the process port limit.
  
  Request Accessibility access once, poll AXIsProcessTrusted while access
  is denied, and create the event tap only after access is granted. Stop
  polling before creation so an unrelated tap failure cannot restart the
  leaking retry loop.
  
  Tested this with various settings and global keys working fine.
  ```

## August 3, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/30862297316), [2](https://github.com/ghostty-org/ghostty/actions/runs/30855802273), [3](https://github.com/ghostty-org/ghostty/actions/runs/30840279326), [4](https://github.com/ghostty-org/ghostty/actions/runs/30834015563), [5](https://github.com/ghostty-org/ghostty/actions/runs/30829026722), [6](https://github.com/ghostty-org/ghostty/actions/runs/30823354937), [7](https://github.com/ghostty-org/ghostty/actions/runs/30782256667)  
Summary: 7 runs • 29 commits • 5 authors

### Changes

- [`ca8868a`](https://github.com/ghostty-org/ghostty/commit/ca8868a2956de2ffd8113d7279ecbdd699c23772) font/shaper: eliminate grapheme candidate allocations ([@jparise](https://github.com/jparise))
  ```text
  RunIterator allocated a list of font candidates for every multi-codepoint
  grapheme, then scanned it for the first font covering the entire cluster.
  
  Instead, check the primary and additional font candidates as they're
  discovered. This preserves their order while removing the temporary
  array and avoids additional lookups when the primary font supports the
  full grapheme.
  ```
- [`f124c42`](https://github.com/ghostty-org/ghostty/commit/f124c42ab97e729fd9b14a8cfe8f919b4054aa34) font/shaper: eliminate grapheme candidate allocations ([#13584](https://github.com/ghostty-org/ghostty/issues/13584)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  RunIterator allocated a list of font candidates for every
  multi-codepoint grapheme, then scanned it for the first font covering
  the entire cluster.
  
  Instead, check the primary and additional font candidates as they're
  discovered. This preserves their order while removing the temporary
  array and avoids additional lookups when the primary font supports the
  full grapheme.
  ```
- [`2f7fbad`](https://github.com/ghostty-org/ghostty/commit/2f7fbadb0b9cda181282c836771610358543a032) termio: free resources for discarded messages ([@jparise](https://github.com/jparise))
  ```text
  Messages can own allocated data or a derived config. Some paths (writer
  thread draining, mailbox shutdown with unread messages, and queue push
  failures) discarded messages without releasing those resources.
  
  This change adds Message.deinit and uses it whenever a message is
  discarded.
  ```
- [`d7bb4b8`](https://github.com/ghostty-org/ghostty/commit/d7bb4b8639614c7d6eeac403bf92d64066b2c73f) libghostty-vt: add C API for snapshotting functions ([@mitchellh](https://github.com/mitchellh))
  ````text
  Expose terminal snapshot through the libghostty-vt C API and add
  a new C example that runs in CI to verify this stuff works!
  
  ## Example
  
  ```c
  size_t continuation_limit = 1024;
  assert(ghostty_terminal_set(
      terminal,
      GHOSTTY_TERMINAL_OPT_CONTINUATION_MAX_BYTES,
      &continuation_limit) == GHOSTTY_SUCCESS);
  
  uint8_t *bytes = NULL;
  size_t len = 0;
  assert(ghostty_snapshot_encode_alloc(
      terminal, NULL, &bytes, &len) == GHOSTTY_SUCCESS);
  
  GhosttySnapshotDecoder decoder = NULL;
  assert(ghostty_snapshot_decoder_new_buf(
      NULL, &decoder, bytes, len) == GHOSTTY_SUCCESS);
  
  GhosttyTerminal restored = NULL;
  assert(ghostty_snapshot_decoder_decode(
      decoder, &restored) == GHOSTTY_SUCCESS);
  
  ghostty_snapshot_decoder_free(decoder);
  ghostty_free(NULL, bytes, len);
  ```
  
  Streaming decode:
  
  ```c
  GhosttyReader reader = {
      .read = read_snapshot,
      .userdata = source,
  };
  GhosttySnapshotDecoder decoder = NULL;
  assert(ghostty_snapshot_decoder_new(
      NULL, &decoder, reader) == GHOSTTY_SUCCESS);
  
  GhosttyTerminal terminal = NULL;
  assert(ghostty_snapshot_decoder_ready(
      decoder, &terminal) == GHOSTTY_SUCCESS);
  
  GhosttyResult result;
  while ((result = ghostty_snapshot_decoder_next(decoder)) ==
         GHOSTTY_SUCCESS) {
    size_t rows = 0;
    assert(ghostty_snapshot_decoder_get(
        decoder,
        GHOSTTY_SNAPSHOT_DECODER_DATA_PROGRESS_ROWS,
        &rows) == GHOSTTY_SUCCESS);
    render(terminal);
  }
  assert(result == GHOSTTY_NO_VALUE);
  ```
  ````
- [`6760c64`](https://github.com/ghostty-org/ghostty/commit/6760c6482be2df6da273239d684086394ccac29a) terminal: support pending image payloads for kitty graphics ([@mitchellh](https://github.com/mitchellh))
  ```text
  Represent Kitty image data as a complete/pending tagged union.
  Kitty images can now be completed _later_ if we have all their other
  metadata up front.
  
  This will be used by the snapshot API to transmit lightweight
  information up front so that renderers of the snapshot can show
  placeholders and accept mutating pty data, while the real image data
  streams in later.
  ```
- [`a011043`](https://github.com/ghostty-org/ghostty/commit/a011043784101325d747030b41067b65d15d164a) termio: free resources for discarded messages ([#13579](https://github.com/ghostty-org/ghostty/issues/13579)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Messages can own allocated data or a derived config. Some paths (writer
  thread draining, mailbox shutdown with unread messages, and queue push
  failures) discarded messages without releasing those resources.
  
  This change adds Message.deinit and uses it whenever a message is
  discarded.
  ```
- [`5700414`](https://github.com/ghostty-org/ghostty/commit/5700414f14428dd83af58670a5a42a7de3706109) libghostty-vt: add C API for snapshotting functions ([#13580](https://github.com/ghostty-org/ghostty/issues/13580)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Expose terminal snapshot through the libghostty-vt C API and add a new C
  example that runs in CI to verify this stuff works!
  
  ## Example
  
  ```c
  // Enable PTY continuation tracking
  size_t continuation_limit = 1024;
  assert(ghostty_terminal_set(
      terminal,
      GHOSTTY_TERMINAL_OPT_CONTINUATION_MAX_BYTES,
      &continuation_limit) == GHOSTTY_SUCCESS);
  
  // Encode a terminal with heap allocation
  uint8_t *bytes = NULL;
  size_t len = 0;
  assert(ghostty_snapshot_encode_alloc(
      terminal, NULL, &bytes, &len) == GHOSTTY_SUCCESS);
  
  // Full blocking decode from an owned buffer.
  GhosttySnapshotDecoder decoder = NULL;
  assert(ghostty_snapshot_decoder_new_buf(
      NULL, &decoder, bytes, len) == GHOSTTY_SUCCESS);
  
  GhosttyTerminal restored = NULL;
  assert(ghostty_snapshot_decoder_decode(
      decoder, &restored) == GHOSTTY_SUCCESS);
  
  ghostty_snapshot_decoder_free(decoder);
  ghostty_free(NULL, bytes, len);
  ```
  
  Streaming decode:
  
  ```c
  // Streaming decoder from a custom reader IO function.
  GhosttyReader reader = {
      .read = read_snapshot,
      .userdata = source,
  };
  GhosttySnapshotDecoder decoder = NULL;
  assert(ghostty_snapshot_decoder_new(
      NULL, &decoder, reader) == GHOSTTY_SUCCESS);
  
  // Read up to the ready state (when we can render and start processing pty bytes)
  GhosttyTerminal terminal = NULL;
  assert(ghostty_snapshot_decoder_ready(
      decoder, &terminal) == GHOSTTY_SUCCESS);
  
  // Sometime later or async process remaining frames.
  GhosttyResult result;
  while ((result = ghostty_snapshot_decoder_next(decoder)) ==
         GHOSTTY_SUCCESS) {
    size_t rows = 0;
    assert(ghostty_snapshot_decoder_get(
        decoder,
        GHOSTTY_SNAPSHOT_DECODER_DATA_PROGRESS_ROWS,
        &rows) == GHOSTTY_SUCCESS);
    render(terminal);
  }
  assert(result == GHOSTTY_NO_VALUE);
  ```
  ````
- [`7e50356`](https://github.com/ghostty-org/ghostty/commit/7e50356642afead216a35c8968f4c33cb38d7f04) terminal: support pending image payloads for kitty graphics ([#13582](https://github.com/ghostty-org/ghostty/issues/13582)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Represent Kitty image data as a complete/pending tagged union. Kitty
  images can now be completed _later_ if we have all their other metadata
  up front.
  
  This will be used by the snapshot API to transmit lightweight
  information up front so that renderers of the snapshot can show
  placeholders and accept mutating pty data, while the real image data
  streams in later.
  
  No user-visible behavior changes today.
  ```
- [`c11fe54`](https://github.com/ghostty-org/ghostty/commit/c11fe5486f7c1f0aa346b8f0a23ea0fcedf79433) core: avoid copying OSC 52 clipboard responses ([@jparise](https://github.com/jparise))
  ```text
  OSC 52 clipboard reads built their response in an allocated buffer and
  then passed it through Message.writeReq, which allocated a second copy
  for large responses.
  
  Instead, transfer the allocated response directly using .write_alloc.
  
  Small responses now retain their initial allocation until the IO thread
  consumes them instead of being copied inline and freed immediately.
  Their allocation count is unchanged, while large responses improve from
  two allocations to one. Both cases avoid the additional copy.
  ```
- [`ac04fc2`](https://github.com/ghostty-org/ghostty/commit/ac04fc276169c70d31aa6fcfc5b43fc160d6fe6e) core: avoid copying OSC 52 clipboard responses ([#13577](https://github.com/ghostty-org/ghostty/issues/13577)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  OSC 52 clipboard reads built their response in an allocated buffer and
  then passed it through Message.writeReq, which allocated a second copy
  for large responses.
  
  Instead, transfer the allocated response directly using .write_alloc.
  
  Small responses now retain their initial allocation until the IO thread
  consumes them instead of being copied inline and freed immediately.
  Their allocation count is unchanged, while large responses improve from
  two allocations to one. Both cases avoid the additional copy.
  ```
- [`90da3ab`](https://github.com/ghostty-org/ghostty/commit/90da3aba58a8c5f44d97bd9ec54eaa1696591256) gtk: fix split sizing to eliminate flickering ([@dkinzler](https://github.com/dkinzler))
  ```text
  For widget resizes the split ratio is now synced directly from the
  propMaxPosition callback in the SplitTreeSplit widget, instead of an
  idle callback. With this change all surfaces will be sized correctly
  from the start, in a single round of size allocation in GTK. Previously,
  surfaces would initially be shown with the wrong size for a few frames
  until the idle callback ran, resulting in visible flickering. This was
  especially visible when resizing a split quickly by holding down the
  resize keybind.
  
  Moved logic to sync split ratio between gtk.Paned widget and split tree
  into new syncSplitRatio function in the SplitTreeSplit widget. Added
  debug assertions and log warnings to syncSplitRatio where we look up
  the split tree.
  ```
- [`957ed21`](https://github.com/ghostty-org/ghostty/commit/957ed21d5c6241f81526581db78520d3c3196421) core: free allocated writes in read-only mode ([@jparise](https://github.com/jparise))
  ```text
  Read-only filtering happens in Surface.queueIo after callers construct
  the message. This early return leaked write_alloc payloads because the
  IO thread never receives them and therefore does not perform its normal
  cleanup.
  ```
- [`7d74809`](https://github.com/ghostty-org/ghostty/commit/7d748097a069768e12fa9bf63d598215a3e8f7a3) core: free allocated writes in read-only mode ([#13574](https://github.com/ghostty-org/ghostty/issues/13574)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Read-only filtering happens in Surface.queueIo after callers construct
  the message. This early return leaked write_alloc payloads because the
  IO thread never receives them and therefore does not perform its normal
  cleanup.
  ```
- [`da581e0`](https://github.com/ghostty-org/ghostty/commit/da581e0fb7a49af38b59a91ef59e1677ff06435a) gtk: improve split sizing ([#13414](https://github.com/ghostty-org/ghostty/issues/13414)) ([@jcollie](https://github.com/jcollie))
  ```text
  This PR improves the way splits/surfaces are sized in the GTK app, which
  eliminates flickering and slightly improves performance.
  
  Fixes #13328, #12709, #11187.
  Related #8208 (closed) but some later comments mention flickering issues
  persisting.
  Builds on top of the changes in #12698.
  
  Previously an idle callback was used to sync the split ratio between the
  GTK widget tree and the split tree data structure that represents the
  split layout. The widget tree contains a `SplitTreeSplit` widget, which
  wraps a `GtkPaned` widget, for every split. During size allocation a
  `GtkPaned` widget first computes the initial position of the divider and
  thereby the size for its two children. We get notified of that position
  (and the max possible position) via the `propPosition/propMaxPosition`
  callbacks in `SplitTreeSplit` and set up an idle callback (the `onIdle`
  function) to update the position if it does not match the desired split
  ratio. Since the initial position is often not correct, especially in
  nested layouts or if the ratio is not 0.5, a surface will first be shown
  with the wrong size for a few frames until the idle callback runs and
  corrects the sizing. In nested layouts it might take multiple rounds of
  size allocation and idle callbacks until every surface gets the correct
  size. This causes flickering as widgets eventually snap to another size,
  which is especially noticeable if the layout changes quickly e.g. when
  resizing a split using keybinds.
  
  To fix this, the divider position will now be corrected directly from
  the `propMaxPosition` callback, which runs during GTK size allocation,
  right after a `GtkPaned` computes the initial position and right before
  it uses the position to allocate sizes for its two children. With this
  change every surface will be sized correctly during the first round of
  size allocation.
  The idle callback is still used to update the ratio in the split tree
  when a split is resized by manually dragging the divider in the UI. The
  logic to sync the split ratio was moved to the new `syncSplitRatio`
  function which is called from both `propMaxPosition` and `onIdle`.
  
  This is kind of hacky, but I reviewed the GTK source code in detail to
  verify that this is safe (see the various code comments for more
  details). I also tested extensively on both Hyprland and KDE Plasma:
  creating deeply nested layouts, resizing with both keybinds and dragging
  dividers by hand, with multiple tabs, resizing the entire window,
  resizing entire subtrees to 0 and back. Everything seems to work fine.
  
  For performance testing I used sysprof which can also collect GTK stats.
  When creating/deleting/resizing splits I can measure a slight but
  consistent increase in GTK FPS (+5 to 10) on my system. Other than that
  CPU usage and FPS seem to be the same before and after. I guess this
  makes sense, while we added a bit of work to the GTK loop during size
  allocation, we avoid surfaces being resized.
  
  For the flickering, here's a side-by-side comparison. Left is before the
  changes, right is after.
  
  
  https://github.com/user-attachments/assets/2a4f0b4b-e113-49b5-b0d7-d9e507a5a4ff
  
  AI Disclosure: no AI was used.
  ```
- [`15c50c1`](https://github.com/ghostty-org/ghostty/commit/15c50c1db1983961c9aa37a2fc0f51327ad26608) crash: do not use global state ([@vancluever](https://github.com/vancluever))
  ```text
  This removes use of global state from the crash reporting functionality
  (everything in src/crash).
  
  This particularly ensures that there are no races on the system
  environment during the execution of the initialization thread that would
  possibly cause crashes, particularly in any (albeit unsupported) 3rd
  party integrations of libghostty-internal.
  
  Ultimately, this pushes any coupling of I/O and environment to places
  that would more correctly interface with global state, such as the
  same-thread global.init, and the crash report CLI.
  
  Note that similar de-coupling actions have been taken on XDG and home
  directory functionality, pushing their coupling points up the stack in a
  similar way.
  ```
- [`b5290e7`](https://github.com/ghostty-org/ghostty/commit/b5290e74c42c2fc5f891eb20f08d0ac0c7c634f8) terminal/snapshot: release decoded hyperlink table refs ([@mitchellh](https://github.com/mitchellh))
  ```text
  Decoded hyperlink table entries retained their insertion reference after
  the grid added its per-cell references. Overwriting all linked cells could
  therefore leave unused entries alive indefinitely.
  
  Release each accepted wire table entry after grid decoding, including
  duplicate values that map to one native ID. Regression coverage verifies
  exact cell ownership and reaping after overwrite.
  ```
- [`f99896b`](https://github.com/ghostty-org/ghostty/commit/f99896bf8c2438e2edbc2a5779a1f2fafa9bcc6d) terminal/snapshot: preserve style reader errors ([@mitchellh](https://github.com/mitchellh))
  ```text
  Lenient style decoding previously caught every error, so PAGE and SCREEN
  could treat truncation or an I/O failure as an invalid semantic style and
  continue from a corrupted stream position.
  
  Add a nullable decoder that discards only invalid style contents while
  propagating reader failures. Update snapshot callers and cover both semantic
  fallback and structural failure behavior.
  ```
- [`cafe7d5`](https://github.com/ghostty-org/ghostty/commit/cafe7d5da43fb19020117e1ab5cca06751f8d0c7) terminal/snapshot: clamp decoded saved cursors ([@mitchellh](https://github.com/mitchellh))
  ```text
  SCREEN decoding restored saved cursor coordinates directly from the wire
  even when they exceeded the current terminal dimensions, unlike the live
  cursor restoration path.
  ```
- [`7d9aaa2`](https://github.com/ghostty-org/ghostty/commit/7d9aaa29703750c4f129790314a54c9a6cd5c7c5) terminal/snapshot: clarify incremental history errors ([@mitchellh](https://github.com/mitchellh))
  ```text
  Document why incremental history decoding exposes native page finalization
  errors and intentionally bypasses the one-shot ExistingHistory guard after READY.
  ```
- [`5c65304`](https://github.com/ghostty-org/ghostty/commit/5c65304a27402f64a7d7356a92b08973e99bc911) crash: do not use global state ([#13567](https://github.com/ghostty-org/ghostty/issues/13567)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This removes use of global state from the crash reporting functionality
  (everything in `src/crash`).
  
  This particularly ensures that there are no races on the system
  environment during the execution of the initialization thread that would
  possibly cause crashes, particularly in any (albeit unsupported) 3rd
  party integrations of libghostty-internal.
  
  Ultimately, this pushes any coupling of I/O and environment to places
  that would more correctly interface with global state, such as the
  same-thread `global.init`, and the crash report CLI.
  
  Note that similar de-coupling actions have been taken on XDG and home
  directory functionality, pushing their coupling points up the stack in a
  similar way.
  ```
- [`863fc95`](https://github.com/ghostty-org/ghostty/commit/863fc9531ae0b8e09b7103a9089dfc00319a7d9c) terminal/snapshot: more misc bugs ([#13573](https://github.com/ghostty-org/ghostty/issues/13573)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Again nothing critical, just some polish around the edges.
  ```
- [`d148471`](https://github.com/ghostty-org/ghostty/commit/d14847183844e84fb8282ebe5a6c9061f40530e3) terminal/snapshot: preserve mixed-width pending wrap ([@mitchellh](https://github.com/mitchellh))
  ```text
  SCREEN decode clamped the cursor x coordinate to the physical page
  width, but validated pending wrap against the terminal-wide column
  count. A lazily reflowed page narrower than the current terminal could
  therefore lose a valid pending-wrap state at its last physical column.
  The next write would continue on the same row instead of wrapping.
  
  Validate pending wrap against the cursor page width, matching the clamp
  and the page-local cursor pin. Add a mixed-width decode regression that
  places the cursor at the narrow page boundary.
  ```
- [`cbc9f36`](https://github.com/ghostty-org/ghostty/commit/cbc9f360b1d6be9305f25cd6e68c49884fa24187) terminal/snapshot: report invalid decoder states ([@mitchellh](https://github.com/mitchellh))
  ```text
  Decoder.next treated calls before READY and calls after any prior decode
  error as unreachable. Network or mux glue that retried after a truncated
  history record, or invoked next before setup completed, could therefore
  turn a recoverable protocol misuse into a process panic.
  
  Add DecoderNotReady and DecoderFailed to NextError and return them for
  the start and failed states. Keep finished calls idempotent, and cover
  both an early call and a retry after FINISH truncation.
  ```
- [`e89ff37`](https://github.com/ghostty-org/ghostty/commit/e89ff37aa8a551369a8f5ae9022cc43410b6d59e) terminal/snapshot: encode screen pages safely ([@mitchellh](https://github.com/mitchellh))
  ```text
  SCREEN encoding assumed every page from the active boundary onward was
  resident. A debug assertion guarded that PageList policy invariant, but
  release builds immediately used pageAssumeResident. If compression policy
  ever allowed a SCREEN suffix page to remain compressed, the encoder would
  read an inactive union field, causing undefined behavior and potentially
  a crash or corrupt snapshot.
  
  Use pagePreservingState for every SCREEN suffix page, as HISTORY already
  does, and include allocation failure in EncodeError. Resident pages remain
  a zero-allocation borrow while compressed pages decode into temporary
  read-only storage without changing the source representation. Exercise the
  path with an explicitly compressed active suffix page.
  ```
- [`9a5279d`](https://github.com/ghostty-org/ghostty/commit/9a5279db682832274442ba2471d277b2ca9b4fa4) terminal/snapshot: release decoded style table refs ([@mitchellh](https://github.com/mitchellh))
  ```text
  PAGE decoding inserted every valid style table entry into the native
  ref-counted set before decoding cells. That insertion contributed one
  reference in addition to every cell reference, unlike organically built
  pages where the initial add belongs to the first cell. An unused encoded
  style therefore remained live with refcount one and was emitted again on
  every re-encode; used styles were also permanently over-counted.
  
  After the grid has installed all cell references, release the temporary
  table-owned reference once per distinct live style. Unused styles become
  dead immediately and used styles retain exactly their cell count. Cover
  used reference counts, unordered sparse IDs, and canonical first
  re-encoding of an unused entry.
  ```
- [`418b5d1`](https://github.com/ghostty-org/ghostty/commit/418b5d18054a015f25efc30592a412a0ac5c6c68) terminal/snapshot: harden grapheme suffix decode ([@mitchellh](https://github.com/mitchellh))
  ```text
  Grapheme suffix decoding accepted U+0000 even though zero is the native
  empty-cell sentinel. It also appended codepoints one at a time and, when
  page capacity failed after a prefix had been stored, left that truncated
  prefix attached to the cell. Hostile snapshots could therefore introduce
  invalid cluster data or render a partial cluster depending on allocator
  capacity.
  
  Ignore NUL alongside invalid scalar values. If any append runs out of
  native capacity, remove the prefix already attached and consume the rest
  of the declared suffix without applying it, making delivery atomic at the
  cluster level. Cover NUL input and a failure after 128 accepted suffix
  codepoints.
  ```
- [`0b940ed`](https://github.com/ghostty-org/ghostty/commit/0b940ed58925cdf5b27e9c10855694f0f83c0d57) terminal/snapshot: misc bugs ([#13572](https://github.com/ghostty-org/ghostty/issues/13572)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Misc bugs related to snapshotting. Nothing critical. Each backed by a
  failed test w/o the change that passes with it.
  ```
- [`e37865b`](https://github.com/ghostty-org/ghostty/commit/e37865bedc2e1b4884f728f41f0d4a179418387f) terminal/snapshot: add incremental decoder ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds a new `terminal.snapshot.Decoder` that allows for incremental
  decoding of a snapshot stream. There are two methods: `ready` builds up
  the entire terminal up to READY. Then `next` acts like a Zig iterator
  and applies incremental history as it becomes available. In between
  calls to `ready` and `next` the caller can do whatever.
  ```
- [`b4592ee`](https://github.com/ghostty-org/ghostty/commit/b4592eefd27290457852ad7d4f16799ecc00b983) terminal/snapshot: add incremental decoder ([#13569](https://github.com/ghostty-org/ghostty/issues/13569)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds a new `terminal.snapshot.Decoder` that allows for incremental
  decoding of a snapshot stream. There are two methods: `ready` builds up
  the entire terminal up to READY. Then `next` acts like a Zig iterator
  and applies incremental history as it becomes available. In between
  calls to `ready` and `next` the caller can do whatever.
  
  The use case for this: with a 1MB ascii stream, the time to decode to
  READY is ~40us on my machine, versus 1.5ms for the entire history. This
  means that a terminal could be rendered and visible after 40us rather
  than waiting for the full terminal. This isn't a large terminal, but
  that READY time should be pretty standard since screens don't get that
  big, but history is unbounded.
  ```

## August 2, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/30770277131), [2](https://github.com/ghostty-org/ghostty/actions/runs/30769052845), [3](https://github.com/ghostty-org/ghostty/actions/runs/30765748163), [4](https://github.com/ghostty-org/ghostty/actions/runs/30752310032), [5](https://github.com/ghostty-org/ghostty/actions/runs/30743972710)  
Summary: 5 runs • 25 commits • 7 authors

### Changes

- [`7031c89`](https://github.com/ghostty-org/ghostty/commit/7031c892b2d1309d4463a56654b90bd0501f3970) synthetic: line length options for the ascii generator ([@mitchellh](https://github.com/mitchellh))
  ```text
  The ascii generator emits an unbroken stream of printable bytes, which
  exercises terminal wrapping but produces only full-width rows. Add
  line-min and line-max options that emit CR LF-terminated lines with a
  uniformly distributed printable length so generated corpora can also
  model shell-like output where most rows end well before the last
  column. The default behavior is unchanged.
  ```
- [`0b5e124`](https://github.com/ghostty-org/ghostty/commit/0b5e12453b639af3f904ad57123cb075a97a82f8) benchmark: add terminal-snapshot benchmark ([@mitchellh](https://github.com/mitchellh))
  ```text
  Measures the terminal binary snapshot codecs in both directions
  against the same terminal state. Setup feeds a pre-generated VT
  stream (for example from ghostty-gen ascii) to a terminal outside
  the timed region.
  
  Baseline measurements at this commit (M-series, ReleaseFast, 80x24,
  unlimited scrollback, 1 MB corpora, per-loop time with setup
  subtracted):
  
    ascii lines 1-70:  34.16 MB  encode  92.8 ms  decode 119.8 ms
    ascii full-wrap:   16.01 MB  encode  43.6 ms  decode  56.2 ms
    utf8:               4.33 MB  encode  12.4 ms  decode  19.0 ms
  ```
- [`ed0f54f`](https://github.com/ghostty-org/ghostty/commit/ed0f54fb8ccf45fc502de25f2c0f1e60967fc2a4) terminal/snapshot: 8-byte grid cells with blank elision ([@mitchellh](https://github.com/mitchellh))
  ```text
  Rework the PAGE grid encoding for codec speed and size. This is a
  breaking change to the work-in-progress version 1 wire format.
  
  Cells were previously a fixed 16-byte header plus inline grapheme
  suffixes: one byte each for content kind, width, and flags, a
  reserved byte, 16-bit style and hyperlink IDs, a 32-bit value, and an
  always-present 32-bit suffix count that was almost always zero. Cells
  are now one 64-bit little-endian word with a documented bit registry
  that carries the hyperlink ID in its high bits. The layout
  deliberately coincides with the native cell so clean rows encode as a
  straight copy of page memory and decode as one bulk read plus an
  in-place normalization pass; a comptime check falls back to a
  portable field-by-field codec if the native layout ever diverges.
  
  Each row header also gains an encoded cell count so trailing default
  cells are elided instead of spending 16 bytes apiece encoding
  nothing: on typical shell output most of every row is blank, and
  measurement showed 97% of encoded snapshot bytes were zero. Grapheme
  suffixes move out of the cell stream into a per-grid section of
  (row, column, codepoints) entries, which keeps row decoding
  fixed-stride and bulk-copyable.
  
  Decode ID remapping switches from hash maps to direct-indexed tables
  sized by the 16-bit encoded ID space, removing per-styled-cell hash
  lookups.
  
  Benchmark deltas at this commit (terminal-snapshot, M-series,
  ReleaseFast, 1 MB corpora):
  
    ascii lines 1-70:  34.16 MB -> 7.66 MB (4.5x)
                       encode 92.8 -> 18.2 ms, decode 119.8 -> 28.0 ms
    ascii full-wrap:   16.01 MB -> 8.04 MB (2.0x)
                       encode 43.6 -> 18.4 ms, decode  56.2 -> 25.6 ms
    utf8:               4.33 MB -> 1.90 MB (2.3x)
                       encode 12.4 ->  4.9 ms, decode  19.0 ->  9.6 ms
  ```
- [`9cc061c`](https://github.com/ghostty-org/ghostty/commit/9cc061c28cc79f5c11eae1299fe06fe486ada157) terminal/snapshot: hardware-accelerated CRC32C ([@mitchellh](https://github.com/mitchellh))
- [`9f66563`](https://github.com/ghostty-org/ghostty/commit/9f66563479df3b12e08d28fca2bb7bbe4ce65e16) terminal/snapshot: gate page verification on slow runtime safety ([@mitchellh](https://github.com/mitchellh))
  ```text
  PAGE decoding verified the complete native integrity of every decoded
  page unconditionally, building per-cell reference maps that accounted
  for roughly a fifth of decode time. The decoder normalizes every
  semantic value while decoding, so a completed decode upholds page
  invariants by construction and the verification only defends against
  decoder bugs. Follow the native page policy instead: assertIntegrity
  and friends run full verification only when slow runtime safety is
  enabled, which keeps the check in debug and test builds where those
  bugs are caught.
  
  Benchmark deltas at this commit (terminal-snapshot, 1 MB corpora):
  
    ascii lines 1-70:  decode 15.5 -> 12.2 ms (encode unchanged)
  ```
- [`3e5d128`](https://github.com/ghostty-org/ghostty/commit/3e5d128353171df595a9535e595f18a4406db0c2) terminal/snapshot: stage PAGE payloads while decoding ([@mitchellh](https://github.com/mitchellh))
  ```text
  PAGE payloads were decoded through a stack of stream adapters:
  a CRC32C-hashing reader over a length-limited reader over the
  BLAKE3-hashing snapshot reader. Every row paid several adapter
  crossings and both hashes were fed row-sized chunks, which kept
  BLAKE3 out of its efficient many-block path and made adapter
  overhead about a quarter of decode time.
  
  Decode now reads the remaining payload into a scratch buffer with
  one bulk read, so each hash sees the payload as a single update, and
  then parses the tables and grid from a flat in-memory reader. Row
  headers are also read as one three-byte read instead of two calls.
  Staging is capped at 8 MiB, far above any standard-capacity page
  payload, so a hostile declared length cannot force a large
  allocation; larger payloads fall back to the streaming path. CRC
  validation and exact-exhaustion checks are unchanged, with the
  staged reader checked for leftover bytes to preserve
  PayloadNotExhausted semantics.
  
  Benchmark deltas at this commit (terminal-snapshot, 1 MB corpora):
  
    ascii lines 1-70:  decode 12.2 -> 8.1 ms (encode unchanged)
    ascii full-wrap:   decode 11.1 -> 7.2 ms
    utf8:              decode  3.1 -> 2.1 ms
  
  Relative to the previous wire format and codecs, the series is a
  16.0x encode and 14.8x decode improvement on line-shaped scrollback
  at 4.5x smaller wire size.
  ```
- [`9e3019f`](https://github.com/ghostty-org/ghostty/commit/9e3019f1905496970e90eb9169fac4ebc0804321) terminal/snapshot: variable-width grid cell encoding ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a per-row encoded cell width to the PAGE grid format. Rows
  previously always spent eight bytes per cell, but a plain text cell
  carries only a codepoint: on line-shaped scrollback most encoded
  bytes were predictable zeros that still had to pass through CRC32C,
  BLAKE3, both codecs, and any transport compression the caller
  applies.
  
  Each row now declares one of four widths in previously reserved row
  flag bits, chosen canonically as the smallest width admitted by the
  bitwise OR of the row cell words: one or two bytes transport a bare
  codepoint, four bytes transport the low word half (any content kind,
  style IDs up to sixty-three, no wide or flag or hyperlink bits), and
  eight bytes remain the full word. Every width is a truncation on
  encode and a zero-extension on decode, so narrow rows encode and
  decode as vectorizable integer loops, one and two byte rows need at
  most surrogate replacement and skip cell normalization entirely, and
  full-width rows keep the existing bulk copy. Decoders use the
  declared width for framing and accept rows encoded wider than
  necessary. Rows containing wide characters, hyperlinks, semantic
  content, or large style IDs still use the full width, which leaves
  CJK-heavy content unchanged.
  
  Benchmark deltas at this commit (terminal-snapshot, M-series,
  ReleaseFast, 1 MB corpora):
  
    ascii lines 1-70:  7.66 MB -> 1.03 MB (7.4x)
                       encode 5.8 -> 2.0 ms, decode 8.1 -> 2.7 ms
    ascii full-wrap:   8.04 MB -> 1.04 MB (7.7x)
                       encode 5.4 -> 1.3 ms, decode 7.2 -> 1.8 ms
    utf8:              unchanged (wide cells keep rows at full width)
  
  For a caller compressing the stream, the lines snapshot end to end
  with zstd -1: encode plus compress 18.5 -> 2.8 ms, decompress plus
  decode 15.8 -> 3.6 ms, and the compressed size itself drops from
  1.35 MB to 0.86 MB because the packed stream is denser for the
  entropy coder.
  ```
- [`d351d9c`](https://github.com/ghostty-org/ghostty/commit/d351d9ce07d53c9bee9db4bf28a95c17c0a9d448) terminal/snapshot: more efficient binary form, optimize wire size + encode/decode speeds ([#13566](https://github.com/ghostty-org/ghostty/issues/13566)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Reworks the terminal PAGE grid wire format and optimize both
  encode/decode. Example improvements for 1MB of VT input w/ full
  scrollback: ~30x smaller wire size, ~45x faster encoding and decoding.
  
  > [!IMPORTANT]
  >
  > **Snapshot version 1 is still explicitly a work-in-progress format, so
  this breaks wire compatibility**.
  
  The original snapshot version I merged favored simplicity over
  optimization. This was the format used a proof-of-concept in my own
  projects, but I knew it wasn't what I wanted to ship. This PR looks at
  the record formats and trades simplicity for performance, a fair trade
  for a performance-sensitive binary format.
  
  Overview of changes:
  
  - **8-byte grid cells.** Cells are now one 64-bit word whose layout
  deliberately coincides with the native cell. Previously, cells were 16
  bytes each and in our 1MB corpus 97% of the data was `0`. Lol.
  - **Blank trailing cells are not written.** Rows declare an encoded cell
  count so trailing blank cells cost nothing.
  - **Hardware CRC32C.** Added `src/crc32c.zig` that uses inline-asm on
  aarch64/x86_64 to get hardware speeds for CRC32. Zig's stdlib is 0.56
  GB/s, aarch64 hardware is 10 GB/s on my computer.
  - **Variable-width cells.** Each row declares how many bytes transport
  each cell word: 1, 2, 4, or 8 depending on the widest row cell.
  
  ## Format
  
  Grid layout, per PAGE record:
  
  ```
     old                                new
     +--------------------------+      +--------------------------+
     | row 0                    |      | row 0                    |
     |   flags (1)              |      |   flags + width (1)      |
     |   cols * 16B cells with  |      |   encoded cell count (2) |
     |   inline suffixes        |      |   count * width cells    |
     +--------------------------+      +--------------------------+
     | ...                      |      | ...                      |
     +--------------------------+      +--------------------------+
     | row (rows - 1)           |      | row (rows - 1)           |
     +--------------------------+      +--------------------------+
                                       | grapheme suffix section  |
                                       +--------------------------+
  ```
  
  Every row previously carried exactly `cols` cells; now it carries cells
  only through its last non-default cell, and the cells past the count are
  implicitly zero. The row flag byte gains the encoded cell width in its
  previously reserved bits:
  
  ```
     bit 0 wrap                 bit 2-3 semantic prompt
     bit 1 wrap continuation    bit 4-5 encoded cell width (log2 bytes)
  ```
  
  The cell itself, old fixed 16-byte header versus the new single word:
  
  ```
     old (16 bytes + inline suffixes)     new (one u64 word)
     +--------+---------+--------+        bit  0 +------------------+
     | kind 1 | width 1 | flags 1|               | content kind  2b |
     +--------+---------+--------+        bit  2 +------------------+
     | zero 1 | style id 2       |               | content      24b |
     +--------+------------------+        bit 26 +------------------+
     | hyperlink id 2            |               | style ID     16b |
     +---------------------------+        bit 42 +------------------+
     | value 4                   |               | width kind    2b |
     +---------------------------+        bit 44 +------------------+
     | grapheme count 4          |               | protected     1b |
     +---------------------------+        bit 45 +------------------+
     | grapheme cps 4 * count    |               | hyperlink     1b |
     +---------------------------+        bit 46 +------------------+
                                                 | semantic      2b |
                                          bit 48 +------------------+
                                                 | hyperlink ID 16b |
                                          bit 64 +------------------+
  ```
  
  The word's bit layout intentionally matches the native cell (with the
  wire hyperlink ID in the native padding), so full-width rows are a
  straight copy of page memory. The row's encoded width then transports
  each word truncated, and decode is the matching zero-extension:
  
  ```
     width | bytes | admitted cells
     ------+-------+------------------------------------------------
       0   |   1   | codepoint <= U+00FF, nothing else set
       1   |   2   | codepoint <= U+FFFF, nothing else set
       2   |   4   | any content kind/codepoint, style IDs 1-63,
           |       | narrow, no flags, no hyperlink
       3   |   8   | everything
  ```
  
  Grapheme suffixes were inline after each cell, which forced per-cell
  framing decisions; they are now one section after the rows, so a
  grapheme-free page (the overwhelming case) pays 4 bytes total:
  
  ```
     old: ... | cell | cp cp | cell | ...      (inline, per cell)
  
     new: +----------------+----------------------------------+
          | entry count 4  | entries: row 2, col 2, count 2,  |
          |                |          count * codepoint 4     |
          +----------------+----------------------------------+
  ```
  
  ## Performance
  
  Setup: `ghostty-bench +terminal-snapshot`, 80x24 terminal with unlimited
  scrollback fed 1 MB of VT input.
  
  Per-commit improvements:
  
  | change                        | wire size | encode  | decode   |
  |-------------------------------|-----------|---------|----------|
  | baseline (v1 before this PR)  | 34.16 MB  | 92.8 ms | 119.8 ms |
  | 8-byte cells + blank elision  | 7.66 MB   | 18.2 ms | 28.0 ms  |
  | hardware CRC32C               | 7.66 MB   | 5.8 ms  | 15.5 ms  |
  | gate page verification        | 7.66 MB   | 5.8 ms  | 12.2 ms  |
  | staged PAGE payload decoding  | 7.66 MB   | 5.8 ms  | 8.1 ms   |
  | variable-width cells          | 1.03 MB   | 2.0 ms  | 2.7 ms   |
  
  Final result across various inputs:
  
  | corpus | wire size | encode | decode |
  
  |----------------------------|------------------------|----------------------|-----------------------|
  | ascii lines 1-70 | 34.16 -> 1.03 MB (33x) | 92.8 -> 2.0 ms (46x) |
  119.8 -> 2.7 ms (44x) |
  | ascii full-width wrap | 16.01 -> 1.04 MB (15x) | 43.6 -> 1.3 ms (34x)
  | 56.2 -> 1.8 ms (31x) |
  | utf8 (wide/grapheme heavy) | 4.33 -> 1.89 MB (2.3x) | 12.4 -> 1.7 ms
  (7x) | 19.0 -> 2.2 ms (9x) |
  
  ### Relationship with Compression
  
  I expect that users of this will wrap everything in compression, so I
  also benchmarked all my changes against a caller-owned zstd compressor
  to ensure we're making the write tradeoffs. Less bytes means less time
  in a compressor, even if a ton of 0s compresses really well.
  
  My results: `zstd -1` over the `lines` snapshot drops from 12.7 ms to
  0.8 ms, and the compressed artifact shrinks from 1.35 MB to 0.86 MB. So
  the end state is a win-win.
  ````
- [`3a606c6`](https://github.com/ghostty-org/ghostty/commit/3a606c6c41b83996d5f23860062548a63a08546c) macOS: install update with same code path ([@bo2themax](https://github.com/bo2themax))
- [`c992658`](https://github.com/ghostty-org/ghostty/commit/c992658b2994a560b052f79b241e4cd02df843c5) terminal/osc: decode OSC 52 base64 with the SIMD decoder ([@Uzaaft](https://github.com/Uzaaft))
  ```text
  OSC 52 clipboard writes decoded their base64 payload with the scalar
  std implementation while Kitty graphics payloads already used the SIMD
  decoder in src/simd.
  
  Move clipboard path to use the same SIMD decoder. The encode side
  of the read reply stays scalar since the codebase has no SIMD
  encoder. 3.3x faster on a 4KB-payload decode micro-benchmark.
  ```
- [`39799a6`](https://github.com/ghostty-org/ghostty/commit/39799a61ce116a4f85e5f98582017383bd73ebc8) terminal/osc: decode OSC 52 base64 with the SIMD decoder ([#13565](https://github.com/ghostty-org/ghostty/issues/13565)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  use simd decoder for OSC 52 clipboard instead of the scalar impl.
  ```
- [`f424b20`](https://github.com/ghostty-org/ghostty/commit/f424b20589e3cd286a7ec3c49836849150c1bcf5) macOS: install update with same code path ([#13562](https://github.com/ghostty-org/ghostty/issues/13562)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously if you select "**Install and Relaunch**" in the update pill,
  there's still a confirmation alert about killing active process, but it
  will just relaunch regardlessly(which is the intended behaviour) when
  you do it in the command palette.
  
  Using UpdateState to check so Ghostty will relaunch immediately when
  user chooses "Install and Relaunch".
  
  > For the auto update case, this will be handled a bit differently in
  the future. If an update is already installed and waiting for relaunch
  (that the user is not aware of), quitting Ghostty will still remind them
  if there's active processes.
  ```
- [`a4f9b9c`](https://github.com/ghostty-org/ghostty/commit/a4f9b9cea23e84873f785c77eaa3475689354e43) Update VOUCHED list ([#13564](https://github.com/ghostty-org/ghostty/issues/13564)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/13563#issuecomment-5160200376)
  from @trag1c.
  
  Denounce: @guysoft
  ```
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

