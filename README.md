> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: August 11, 2026 at 09:55 UTC.

## August 11, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/31453674000), [2](https://github.com/ghostty-org/ghostty/actions/runs/31450087990)  
Summary: 2 runs • 4 commits • 3 authors

### Changes

- [`94d775f`](https://github.com/ghostty-org/ghostty/commit/94d775fefc21f74d9cc85a46b34c4e1d85318fd0) Update VOUCHED list ([#13743](https://github.com/ghostty-org/ghostty/issues/13743)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13742#discussioncomment-17970277)
  from @jcollie.
  
  Vouch: @dave92082
  ```
- [`49e4df7`](https://github.com/ghostty-org/ghostty/commit/49e4df78333ccdeb262e59d0f3c4de9d4b0bc7fd) macOS: rework for [#12712](https://github.com/ghostty-org/ghostty/issues/12712) and [#13645](https://github.com/ghostty-org/ghostty/issues/13645) ([@bo2themax](https://github.com/bo2themax))
- [`4b9d589`](https://github.com/ghostty-org/ghostty/commit/4b9d589bcb234b3fdd2160a3abf02cf9b647f328) macOS: disable text selection on macOS 15 ([@bo2themax](https://github.com/bo2themax))
- [`44f06d4`](https://github.com/ghostty-org/ghostty/commit/44f06d4e4fd098aa4b5627e0c2b2d6e704834117) macOS: rework for [#12712](https://github.com/ghostty-org/ghostty/issues/12712) and [#13645](https://github.com/ghostty-org/ghostty/issues/13645) ([#13717](https://github.com/ghostty-org/ghostty/issues/13717)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  `needleSelection` was introduced in #12712 to select all texts when
  syncing pasteboard, the crash happens most on macOS 15 in
  `readPasteboardNeedle`. It seems that `objectWillChange` fires
  differently there, and it's hard to reproduce on macOS 26/27. I think
  guaranteeing from ourside is enough, I believe SwiftUI already as its
  own when updating the binding.
  
  **Confirmed with a simple example on macOS 15, it seems a SwiftUI
  issue🫪. So I changed the minimal macOS version for text selection to
  macOS 26. I don't see an elegant way to fix it.**
  
  <img width="1352" height="849" alt="image"
  src="https://github.com/user-attachments/assets/1dfef3f5-ceaa-41dd-bb91-c23dbc5e4ad3"
  />
  
  
  ```swift
  struct ContentView: View {
      @State private var text = ""
      @State private var selection: TextSelection?
      var body: some View {
          TextField("Search", text: $text, selection: $selection)
      }
  }
  ```
  ````

## August 10, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/31439881201), [2](https://github.com/ghostty-org/ghostty/actions/runs/31436717873), [3](https://github.com/ghostty-org/ghostty/actions/runs/31414618806), [4](https://github.com/ghostty-org/ghostty/actions/runs/31400623896), [5](https://github.com/ghostty-org/ghostty/actions/runs/31367606708), [6](https://github.com/ghostty-org/ghostty/actions/runs/31354005195), [7](https://github.com/ghostty-org/ghostty/actions/runs/31347193596)  
Summary: 7 runs • 26 commits • 9 authors

### Changes

- [`09557e9`](https://github.com/ghostty-org/ghostty/commit/09557e91dc33907fb151b2791414d2c6153fd2e0) Update VOUCHED list ([#13739](https://github.com/ghostty-org/ghostty/issues/13739)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13738#discussioncomment-17968662)
  from @jcollie.
  
  Vouch: @PRIHLOP
  ```
- [`b68eb67`](https://github.com/ghostty-org/ghostty/commit/b68eb67e956b051372910cfe6b453e43121b76e3) config/edit: better handling of existing paths ([@vancluever](https://github.com/vancluever))
  ```text
  This adds some better handling of existing paths when editing
  configuration files:
  
  * If we've found an existing file we just skip any attempts to create
    files/dirs, and just return the path.
  
  * If the path (including file) does not exist, we check to see if the
    directory exists first (possibly following symlinks). Directory
    creation happens normally after this (note that any intermediary
    symlinks in this process will still cause the process to fail, this is
    to prevent infinite loops, as per the comments in
    std.Io.Threaded.dirCreateDirPath).
  ```
- [`d929e6a`](https://github.com/ghostty-org/ghostty/commit/d929e6a34a091dcfd69d45011b96cc70b5575dac) config/edit: better handling of existing paths ([#13736](https://github.com/ghostty-org/ghostty/issues/13736)) ([@jcollie](https://github.com/jcollie))
  ```text
  This adds some better handling of existing paths when editing
  configuration files:
  
  * If we've found an existing file we just skip any attempts to create
  files/dirs, and just return the path.
  
  * If the path (including file) does not exist, we check to see if the
  directory exists first (possibly following symlinks). Directory creation
  happens normally after this (note that any intermediary symlinks in this
  process will still cause the process to fail, this is to prevent
  infinite loops, as per the comments in
  std.Io.Threaded.dirCreateDirPath).
  ```
- [`1dbc8ca`](https://github.com/ghostty-org/ghostty/commit/1dbc8ca30c8ce929019c8a4d971113fc79cd4d58) apprt/gtk: add WeakRef.deinit and use it at teardown sites ([@hakonhagland](https://github.com/hakonhagland))
  ```text
  A GWeakRef must be released before the memory holding it is freed: the
  target keeps a pointer to the GWeakRef so it can clear it at finalize,
  and if that memory is gone by then the target walks into whatever now
  occupies it. inspector_window.zig already carries this warning, and
  every call site follows it — but the rule lives in a comment in one
  file, while the type itself offers only set and get, so releasing one
  looks like an ordinary assignment.
  
  Give it a name. deinit forwards to g_weak_ref_clear, which is the call
  GLib documents for a GWeakRef that is going away, and the dispose-time
  clears now use it. set(null) still works and is unchanged; the clear in
  handleReloadConfig stays a set(null) because the object is still alive
  there and the reference is reused.
  
  Zig has no destructors so this enforces nothing. It puts the
  requirement on the type someone is already looking at.
  ```
- [`951a03b`](https://github.com/ghostty-org/ghostty/commit/951a03b58bf60e73d2d361ac8848cb9423c8be26) apprt/gtk: add WeakRef.deinit and use it at teardown sites ([#13732](https://github.com/ghostty-org/ghostty/issues/13732)) ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes #13713.
  
  `WeakRef(T)` offers `set` and `get`, so releasing one is spelled
  `set(null)` — indistinguishable from an ordinary assignment. The
  requirement that it *must* happen before the owning memory is freed
  lives in a comment in `class/inspector_window.zig`, which is not where
  somebody using the type is looking.
  
  This adds `deinit`, forwarding to `g_weak_ref_clear` — the call GLib
  documents for a `GWeakRef` that is going away — and switches the
  dispose-time clears to it.
  
  ### What changed
  
  - `weak_ref.zig`: new `deinit`, with the reasoning in its doc comment.
  - `window.zig`, `split_tree.zig`, `application.zig`,
  `command_palette.zig`: the four dispose-time clears now call `deinit`.
  
  `set(null)` is unchanged and still valid. The clear in
  `Application.handleReloadConfig` deliberately stays a `set(null)`: the
  object is alive there and the reference is reused, so it is a logical
  clear rather than teardown — which is the distinction the new name is
  meant to make visible.
  
  ### Why it is worth a method
  
  Zig has no destructors, so this enforces nothing; it is documentation
  that happens to be executable. The concrete case is in #13713: I added a
  `WeakRef(Window)` in a downstream branch, did not clear it, and closing
  a window that had shown that dialog deadlocked the GTK main loop inside
  `weak_ref_data_clear_list` locking freed memory. Every upstream call
  site already gets this right — the point is only to put the rule where
  the next person will see it.
  
  ### Testing
  
  `zig build test` passes. `zig fmt --check` clean. Built and used on
  Linux/GTK; the change is behaviourally identical to what was there,
  since `g_weak_ref_clear` and `g_weak_ref_set(NULL)` both unregister.
  
  ---
  
  **AI disclosure per `AI_POLICY.md`:** I investigated the underlying
  incident with Claude Code and it drafted this change; I reviewed it.
  ```
- [`fd47b15`](https://github.com/ghostty-org/ghostty/commit/fd47b15cd4dad1152e17d13b8f79a0f1183c61f2) gtk: free hotkeys memory on app teardown ([@dkinzler](https://github.com/dkinzler))
  ```text
  Free array list memory in Hotkeys.deinit to avoid DebugAllocator
  throwing an error about leaked memory.
  ```
- [`0a183c9`](https://github.com/ghostty-org/ghostty/commit/0a183c923bfc6150e710121f481e3d03464f1b60) core/gtk: allow editing Ghostty config in a Ghostty window ([@jcollie](https://github.com/jcollie))
  ```text
  This PR extends the `open_config` keybind action to allow editing the
  Ghostty config in a new Ghostty window using the editor configured in
  `$EDITOR` or `$VISUAL`.
  ```
- [`e53b18a`](https://github.com/ghostty-org/ghostty/commit/e53b18a64726ad0ef0860d1dd77065defca8223f) gtk: free hotkeys memory on app teardown ([#13727](https://github.com/ghostty-org/ghostty/issues/13727)) ([@pluiedev](https://github.com/pluiedev))
  ```text
  In debug builds the DebugAllocator throws an error about leaked memory
  when you close Ghostty, if you have global keybinds in your config with
  a Wayland compositor that supports the vicinae-hotkey protocol. The
  cause is the `Hotkeys.entries` array list never actually being freed.
  Not really a problem because the list should be kept around until app
  teardown anyway, but not getting an error every time would be nice (even
  if you need a somewhat specific setup for this to even happen right
  now).
  
  To fix this free the array list memory in Hotkeys.deinit with
  `ArrayList.clearAndFree`. As the existing comment on `deinit` already
  mentions, we can't use `ArrayList.deinit` because it leaves the list in
  an invalid state and `Hotkeys.clear` might still get called and use it.
  ```
- [`0914c5c`](https://github.com/ghostty-org/ghostty/commit/0914c5c2f1b96cefb2277a2cb871db181fd559da) core/gtk: allow editing Ghostty config in a Ghostty window ([#11905](https://github.com/ghostty-org/ghostty/issues/11905)) ([@jcollie](https://github.com/jcollie))
  ```text
  This PR extends the `open_config` keybind action to allow editing the
  Ghostty config in a new Ghostty window using the editor configured in
  `$EDITOR` or `$VISUAL`.
  ```
- [`d6248a3`](https://github.com/ghostty-org/ghostty/commit/d6248a32dd724e1cd9c7f9b68c9360f3ad630d47) ghostty.h: mark as internal ([@pluiedev](https://github.com/pluiedev))
  ```text
  Its moniker has been `libghostty-internal` for *quite* a while now among
  maintainers but that has never really been clarified for the public aside
  from a couple comments on discussions. Judging by how many people still
  try to vibe their way into making this work for their purposes, I think
  we should clear this up once and for all.
  ```
- [`7e463bc`](https://github.com/ghostty-org/ghostty/commit/7e463bc65d430e8a8f0aa786abf83601cf2b9598) ghostty.h: mark as internal ([#13724](https://github.com/ghostty-org/ghostty/issues/13724)) ([@bo2themax](https://github.com/bo2themax))
- [`a82637b`](https://github.com/ghostty-org/ghostty/commit/a82637b53aa434fa5c8bc8360c58561d7d48a8e1) crash: resolve sentry directories on the init thread ([@mitchellh](https://github.com/mitchellh))
  ```text
  Sentry initialization already ran on a separate thread, but the cache
  and state directory resolution happened on the main thread before
  spawning it. On macOS the cache dir resolution calls NSFileManager
  URLForDirectory:inDomain:appropriateForURL:create:error: which takes
  multiple milliseconds and was the single largest cost in global.init.
  
  All directory resolution now happens on the init thread.
  
    before: 2967us-4018us
    after:    30us-70us (env map snapshot + thread spawn)
  
  global.init total drops from ~3.4-5.0ms to ~0.4-1.0ms.
  ```
- [`3225e9e`](https://github.com/ghostty-org/ghostty/commit/3225e9ebb195b1cc237c7b8d9de3d51c6863cb5e) macos: cache unified logging loggers per scope ([@mitchellh](https://github.com/mitchellh))
  ```text
  The logFn for macOS unified logging created and released an os_log_t
  logger on every single log call. Loggers are now cached per log scope for
  the process lifetime via an atomic pointer (a creation race wastes at most
  one create).
  
  Measured on macOS (Apple Silicon) with local timing instrumentation
  during app launch, the version-info logging block in global.init:
  
    before: 1070us-2629us
    after:   858us-1319us
  ```
- [`afc79b8`](https://github.com/ghostty-org/ghostty/commit/afc79b8ccf4098ba15659578d0fc666c74fb61bd) font: look up Apple Color Emoji by exact name on macOS ([@mitchellh](https://github.com/mitchellh))
  ```text
  The Apple Color Emoji fallback font was discovered with the generic
  discovery path, which builds a CTFontCollection and runs system-wide
  font matching. Since we know the exact font we want, we can look it
  up directly with CTFontCreateWithName instead.
  ```
- [`c454a3b`](https://github.com/ghostty-org/ghostty/commit/c454a3bf47cd72945b7f4db3b53f8af332e167c9) font: support warmup threads ([@mitchellh](https://github.com/mitchellh))
  ```text
  The first CoreText font query in a process initializes the system
  font database, which takes multiple milliseconds (~7ms measured in an
  isolated process; 2-4ms observed inside Ghostty startup). This cost
  was previously paid during the first surface's font grid
  initialization, on the critical path to the first window.
  
  App.create can now spawn a background thread that performs the warmup.
  ```
- [`131b293`](https://github.com/ghostty-org/ghostty/commit/131b293dbbf426acf57618bc43bef0a4fe260d12) renderer/metal: warm up the Metal device machinery at app creation ([@mitchellh](https://github.com/mitchellh))
  ```text
  The first Metal device query in a process (MTLCopyAllDevices) takes
  multiple milliseconds; once the framework is warm, subsequent queries
  are effectively free (measured ~15ms cold, ~1us warm in isolation).
  This cost was paid during the first surface's renderer
  initialization, on the critical path to the first window.
  
  Measured on macOS (Apple Silicon) with local timing instrumentation
  during app launch, first surface renderer initialization:
  
    GraphicsAPI.init before: 4227us (device query ~3.5ms)
    GraphicsAPI.init after:  ~900us (device query 20-25us)
  ```
- [`de1336f`](https://github.com/ghostty-org/ghostty/commit/de1336faddbdffc8fb4f58af3597d3f031e2b2d9) renderer/metal: warm up command queue and shader pipelines ([@mitchellh](https://github.com/mitchellh))
  ```text
  Extend the Metal portion of the startup warmup thread to also create
  (and discard) a command queue and build (and discard) the shader
  pipelines for both pixel formats we may use (which one is used
  depends on the blending config). The first command queue for a device
  and the first render pipeline state creations pay one-time driver
  setup and shader compilation costs; once warm, the real creations
  during surface initialization hit driver and OS caches.
  
  Measured on macOS (Apple Silicon) with local timing instrumentation
  during app launch, first surface renderer initialization:
  
    queue creation:  717us -> 93us
    pipeline builds: 1023us -> 347us
    renderer init total: 2777us -> 1466us
  ```
- [`db6d20d`](https://github.com/ghostty-org/ghostty/commit/db6d20dce1df0614b4903a4c5c5489a384ab8eeb) apprt/embedded: initialize the TIS keymap lazily ([@mitchellh](https://github.com/mitchellh))
  ```text
  The embedded apprt App init created the keyboard layout keymap
  eagerly, which requires talking to the text input system (TIS). The
  first TIS call in a process is slow: 6.6ms measured inside
  ghostty_app_new during app launch (up to ~30ms in a cold process).
  
  The keymap is only used for keyboard layout queries (option-as-alt
  detection, layout change reload), which happen once keyboard events
  are flowing. By then AppKit has already warmed TIS and the call is
  effectively free (~0.2us measured warm). So initialize the keymap
  lazily on first use. If the layout changes before the keymap was ever
  created, reload is a no-op since lazy init picks up the current
  layout.
  
  Measured on macOS (Apple Silicon) with local timing instrumentation
  during app launch:
  
    embedded app init before: ~6.7ms (keymap 6614us)
    embedded app init after:  ~60us (config clone only)
  ```
- [`4b1e02c`](https://github.com/ghostty-org/ghostty/commit/4b1e02c7c3cf6d6a3548a67d88d08d4962ff67ed) macos: do not load the config errors window when there are no errors ([@mitchellh](https://github.com/mitchellh))
  ```text
  Measured on macOS (Apple Silicon) during app launch, via a startup
  timeline instrumented across the Swift app and libghostty:
  
    config apply, errors step:      35.5ms -> 0.1ms
    main() -> first frame rendered: ~126ms -> ~93ms
    main() -> window visible:       ~193ms -> ~173ms
  ```
- [`da74563`](https://github.com/ghostty-org/ghostty/commit/da745630bed8689365be0ec9a0cfe283a2ed965d) macos: only check for auto-tabbing when tabbing preference is always ([@mitchellh](https://github.com/mitchellh))
  ```text
  windowDidLoad undoes macOS automatic window tabbing by inspecting
  window.tabGroup. Accessing tabGroup on a fresh window materializes
  AppKit's tab group machinery, which takes ~15-20ms and is on the
  critical path of every window creation, including the first window at
  app launch.
  
  AppKit only auto-tabs a fresh window when the system tabbing
  preference is "always": the tab bar "+" button goes through
  newWindowForTab which we intercept and route through our own tab
  logic, so it never auto-tabs. Guard the check on
  NSWindow.userTabbingPreference == .always so everyone else skips the
  tab group materialization entirely.
  
  Measured on macOS (Apple Silicon) during app launch via the startup
  timeline instrumentation:
  
    windowDidLoad tab group check: 17.8ms -> ~0ms
    main() -> window visible: median ~173ms -> ~165ms (n=7)
  ```
- [`931a538`](https://github.com/ghostty-org/ghostty/commit/931a538a3992c0f33c6647360bd15ff54f0f7a87) comments ([@mitchellh](https://github.com/mitchellh))
- [`ad08f3b`](https://github.com/ghostty-org/ghostty/commit/ad08f3b0378b119c584aa54980fc5f7fb18b45bb) macos: reduce app launch time ~15%, time to first frame ~27% ([#13722](https://github.com/ghostty-org/ghostty/issues/13722)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Startup optimizations for macOS! Highlights:
  
   * Process exec to visible window: **15% reduction, ~193ms to ~165ms.**
   * Time to first rendered frame: **27% reduction, ~126ms to ~92ms.**
  * Zig startup time goes from **20ms to ~5ms**, the remainder is
  AppKit/Swift stuff.
  
  > [!NOTE]
  >
  > "Time to first rendered frame?" I measured the time between global
  init start to the first Metal callback saying that a frame was
  completed/drawn. This is faster than when it is _presented_ because we
  can create an IOSurfaceLayer and draw to it before AppKit finishes its
  startup and shows the window. But, the good news is this means that when
  the window is shown, the frame is already drawn!
  
  See individual commits for speeds, but a summary below:
  
  1. **Resolve Sentry directories on the init thread, not startup thread
  (~3-4ms).** Sentry init already ran on a thread, but directory
  resolution happened on the main thread first, and on macOS that calls
  `NSFileManager URLForDirectory:` which is slow as shit.
  
  2. **Initialize the TIS keymap lazily (~7ms).** The keymap is only
  needed once keyboard events flow. If AppKit isn't warmed up, this is
  SLOW. Defer setup until its needed.
  
  3. **Warm up the font registry and Metal on background threads (~7ms+
  off the first surface).** The first CoreText query initializes the
  system font database (~7ms) and the first Metal device/queue/pipeline
  use pays framework init and shader compilation costs. `App.create` now
  spawns a detached warmup thread per subsystem so this overlaps config
  load, AppKit launch, and window creation. First font grid init went from
  ~4.5ms to ~1.1ms, renderer init from ~6.8ms to ~1.5ms.
  
  4. **Look up Apple Color Emoji by exact name.** We know exactly which
  font we want, so skip the system-wide `CTFontCollection` matching
  (~312us to ~13us).
  
  5. **Cache unified logging loggers per scope.** We created and released
  an `os_log_t` on every log call. I actually had a comment saying this is
  slow but probably won't matter. Well, we log a lot on startup, and this
  actually mattered.
  
  ## Warmup Threads
  
  As a note, some of the biggest speedups are by using "warmup" threads.
  These are one-time launched threads on system start that basically just
  "touch" the relevant frameworks (CoreText/Metal). The initial touching
  of these frameworks has a ton of cost associated with them (and they're
  thread-safe), so we can shave off a bunch of time by just touching them
  in the background.
  
  This sets up a race between our own startup needing it and these warmup
  threads, but in every case I measured, the warmup threads win.
  
  ## Linux
  
  All the optimizations here focused really on slow macOS APIs. I plan on
  measuring on Linux, but nothing here should slow it down.
  
  **AI usage:** Fable was used for this one to find the issues, help
  perform the measurements, and draft commit messages by splitting up my
  work. I wrote the code, then edited the commit messages. This PR message
  is fully hand-written.
  ```
- [`b8222f4`](https://github.com/ghostty-org/ghostty/commit/b8222f4a8403765050cca52c537ddd7638725457) terminal/kitty: clear placements on image retransmit ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13719
  
  The Kitty graphics protocol requires retransmitting data for a
  specific image ID to delete the previous image and all of its
  placements.
  
  Ghostty instead preserved the placement count and map when replacing image
  data. Repeated `a=T` commands therefore added one anonymous placement per
  frame and retained its tracked pin.
  
  Spec: https://sw.kovidgoyal.net/kitty/graphics-protocol/#display-images-on-screen
  ```
- [`156bc8c`](https://github.com/ghostty-org/ghostty/commit/156bc8c814292349981f3adbfb1120c3d4f02020) terminal/kitty: clear placements on image retransmit ([#13723](https://github.com/ghostty-org/ghostty/issues/13723)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #13719
  
  The Kitty graphics protocol requires retransmitting data for a specific
  image ID to delete the previous image and all of its placements.
  
  Ghostty instead preserved the placement count and map when replacing
  image data. Repeated `a=T` commands therefore added one anonymous
  placement per frame and retained its tracked pin.
  
  Spec:
  https://sw.kovidgoyal.net/kitty/graphics-protocol/#display-images-on-screen
  ```
- [`c285d3c`](https://github.com/ghostty-org/ghostty/commit/c285d3c2442f314b9b9221bc95d02108c61d8d0f) build(deps): bump dorny/paths-filter from 4.0.2 to 4.0.3 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [dorny/paths-filter](https://github.com/dorny/paths-filter) from 4.0.2 to 4.0.3.
  - [Release notes](https://github.com/dorny/paths-filter/releases)
  - [Changelog](https://github.com/dorny/paths-filter/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/dorny/paths-filter/compare/7b450fff21473bca461d4b92ce414b9d0420d706...ceb8a2b8f2d89434be7ff52d3de7ec3738c5cc9d)
  
  ---
  updated-dependencies:
  - dependency-name: dorny/paths-filter
    dependency-version: 4.0.3
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`bb876a0`](https://github.com/ghostty-org/ghostty/commit/bb876a0d286b661089b7f40dd3a6488d629beffe) build(deps): bump dorny/paths-filter from 4.0.2 to 4.0.3 ([#13718](https://github.com/ghostty-org/ghostty/issues/13718)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps [dorny/paths-filter](https://github.com/dorny/paths-filter) from
  4.0.2 to 4.0.3.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/dorny/paths-filter/releases">dorny/paths-filter's
  releases</a>.</em></p>
  <blockquote>
  <h2>v4.0.3</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>Update Outputs in readme to account for the 'every'
  predicate-quantifier by <a
  href="https://github.com/hintron"><code>@​hintron</code></a> in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/247">dorny/paths-filter#247</a></li>
  <li>fix: scope base-ignored warning to API path by <a
  href="https://github.com/saschabratton"><code>@​saschabratton</code></a>
  in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/319">dorny/paths-filter#319</a></li>
  <li>docs: add contents permission to PR example by <a
  href="https://github.com/134130"><code>@​134130</code></a> in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/248">dorny/paths-filter#248</a></li>
  <li>feat: add 'some-with-excludes' predicate quantifier by <a
  href="https://github.com/arxeiss"><code>@​arxeiss</code></a> in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/322">dorny/paths-filter#322</a></li>
  <li>Document safe handling of file list outputs in workflows by <a
  href="https://github.com/dorny"><code>@​dorny</code></a> in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/326">dorny/paths-filter#326</a></li>
  </ul>
  <h2>Security</h2>
  <ul>
  <li>Escape multi-line filenames in list-files shell and csv output] by
  <a href="https://github.com/ken-matsui"><code>@​ken-matsui</code></a>
  and <a href="https://github.com/tjswlsgg"><code>@​tjswlsgg</code></a> in
  <a
  href="https://github.com/advisories/GHSA-7hc6-8hq5-9q2m">https://github.com/advisories/GHSA-7hc6-8hq5-9q2m</a></li>
  </ul>
  <h2>New Contributors</h2>
  <ul>
  <li><a href="https://github.com/hintron"><code>@​hintron</code></a> made
  their first contribution in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/247">dorny/paths-filter#247</a></li>
  <li><a href="https://github.com/134130"><code>@​134130</code></a> made
  their first contribution in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/248">dorny/paths-filter#248</a></li>
  <li><a href="https://github.com/arxeiss"><code>@​arxeiss</code></a> made
  their first contribution in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/322">dorny/paths-filter#322</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/dorny/paths-filter/compare/v4...v4.0.3">https://github.com/dorny/paths-filter/compare/v4...v4.0.3</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/dorny/paths-filter/blob/master/CHANGELOG.md">dorny/paths-filter's
  changelog</a>.</em></p>
  <blockquote>
  <h1>Changelog</h1>
  <h2>v4.0.3</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/326">Document
  safe handling of file list outputs in workflows</a></li>
  <li><a href="https://github.com/advisories/GHSA-7hc6-8hq5-9q2m">Escape
  multi-line filenames in list-files shell and csv output</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/322">Add
  'some-with-excludes' predicate quantifier</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/248">Add
  contents permission to PR example</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/319">Scope
  base-ignored warning to API path</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/247">Update
  outputs in readme to account for the 'every'
  predicate-quantifier</a></li>
  </ul>
  <h2>v4.0.2</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/317">Work
  around git dubious ownership errors in container jobs</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/303">Use
  rev-parse instead of branch --show-current for older git compat</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/282">Fix
  warning message</a></li>
  </ul>
  <h2>v4.0.1</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/255">Support
  merge queue</a></li>
  </ul>
  <h2>v4.0.0</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/294">Update
  action runtime to node24</a></li>
  </ul>
  <h2>v3.0.4</h2>
  <ul>
  <li><a href="https://github.com/advisories/GHSA-7hc6-8hq5-9q2m">Escape
  multi-line filenames in list-files shell and csv output</a></li>
  </ul>
  <h2>v3.0.3</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/279">Add
  missing predicate-quantifier</a></li>
  </ul>
  <h2>v3.0.2</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/224">Add
  config parameter for predicate quantifier</a></li>
  </ul>
  <h2>v3.0.1</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/133">Compare
  base and ref when token is empty</a></li>
  </ul>
  <h2>v3.0.0</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/210">Update to
  Node.js 20</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/215">Update
  all dependencies</a></li>
  </ul>
  <h2>v2.11.1</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/167">Update
  @​actions/core to v1.10.0 - Fixes warning about deprecated
  set-output</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/168">Document
  need for pull-requests: read permission</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/164">Updating
  to actions/checkout@v3</a></li>
  </ul>
  <h2>v2.11.0</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/157">Set
  list-files input parameter as not required</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/161">Update
  Node.js</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/162">Fix
  incorrect handling of Unicode characters in exec()</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/163">Use
  Octokit pagination</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/160">Updates
  real world links</a></li>
  </ul>
  <h2>v2.10.2</h2>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/ceb8a2b8f2d89434be7ff52d3de7ec3738c5cc9d"><code>ceb8a2b</code></a>
  Update CHANGELOG.md for v4.0.3 and v3.0.4 (<a
  href="https://redirect.github.com/dorny/paths-filter/issues/327">#327</a>)</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/ef09b88f3eacdbec6ce135a7c9a193a6849545c1"><code>ef09b88</code></a>
  Document safe handling of file list outputs in workflows (<a
  href="https://redirect.github.com/dorny/paths-filter/issues/326">#326</a>)</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/44adc5b06dc135dba334efce9bf3cf0624512d2d"><code>44adc5b</code></a>
  Merge commit from fork</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/4711b7a31b4aa89103d8c6ffab2e3b8e7b6381c7"><code>4711b7a</code></a>
  feat: add 'some-with-excludes' predicate quantifier (<a
  href="https://redirect.github.com/dorny/paths-filter/issues/322">#322</a>)</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/93c889f9e58fca66f35a0c83d8673ac7e88bb70a"><code>93c889f</code></a>
  fix: escape multi-line filenames in list-files shell and csv output</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/b41dfa943b1939b9b646f67753bfe35cf6e4de03"><code>b41dfa9</code></a>
  docs: add contents permission to PR example (<a
  href="https://redirect.github.com/dorny/paths-filter/issues/248">#248</a>)</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/9af6e5a9d010d1ae8ec570390b3d793e2b70a402"><code>9af6e5a</code></a>
  fix: scope base-ignored warning to API path (<a
  href="https://redirect.github.com/dorny/paths-filter/issues/319">#319</a>)</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/cae9006b65a1a53044b518c68e13e835c54948a7"><code>cae9006</code></a>
  docs: update outputs in readme to account for the 'every'
  predicate-quantifie...</li>
  <li>See full diff in <a
  href="https://github.com/dorny/paths-filter/compare/7b450fff21473bca461d4b92ce414b9d0420d706...ceb8a2b8f2d89434be7ff52d3de7ec3738c5cc9d">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=dorny/paths-filter&package-manager=github_actions&previous-version=4.0.2&new-version=4.0.3)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## August 9, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/31337999494), [2](https://github.com/ghostty-org/ghostty/actions/runs/31325264351), [3](https://github.com/ghostty-org/ghostty/actions/runs/31320152152), [4](https://github.com/ghostty-org/ghostty/actions/runs/31313857575), [5](https://github.com/ghostty-org/ghostty/actions/runs/31293445585), [6](https://github.com/ghostty-org/ghostty/actions/runs/31292361837)  
Summary: 6 runs • 27 commits • 6 authors

### Changes

- [`0aa71d0`](https://github.com/ghostty-org/ghostty/commit/0aa71d02ed068a3a036721ab9e480cbdf82ac329) terminal: reduce Parser.Action log formatting code size ([@mitchellh](https://github.com/mitchellh))
  ```text
  Shrinks libghostty-vt dylib by ~2%.
  ```
- [`f368543`](https://github.com/ghostty-org/ghostty/commit/f36854345e50fe382f37a6ef5859f9013787a23b) libghostty: skip stack traces in release panic handlers ([@mitchellh](https://github.com/mitchellh))
  ```text
  The default Zig panic handler unwinds the stack and symbolicates it,
  which drags in ~160KB worth of helper machinery. For an embedded library
  this isn't great because the embedder's environment should be providing
  this as long as libghostty is compiled with symbols or has a way to
  symbolize.
  
  Change ReleaseFast/ReleaseSmall libghostty-vt builds to use a custom
  panic handler. Debug/ReleaseSafe keep the full Zig handlers.
  
  This shrinks libghostty-vt on macOS by ~160KB (~9%).
  ```
- [`579db41`](https://github.com/ghostty-org/ghostty/commit/579db418934a5990296b7fd65d1b6b586b46dfc6) libghostty: log to stderr with raw writes, not lockStderr ([@mitchellh](https://github.com/mitchellh))
  ```text
  see the prior commit, but most importantly this makes it so we can
  replace our IO impl from Threaded.
  ```
- [`82df79e`](https://github.com/ghostty-org/ghostty/commit/82df79ec8d2c61f3beb3ecfc543ed32cb4aba450) libghostty: replace Io.Threaded with custom Io impl (TinyIo) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a new Io implementation `TinyIo` that only supports the operations
  we need and doesn't support concurrency. This shrinks the binary size
  of libghostty by anywhere from ~100KB (macOS) to ~200KB (Linux) and
  runtime memory requirements by over 256KB (the thread-local storage
  `std.Io.Threaded` creates plus the 18KB threaded structure is gone).
  
  `TinyIo` is POSIX-only: Windows keeps std.Io.Threaded, and on
  freestanding targets (wasm) TinyIo degrades to std.Io.failing
  behavior just like before.
  
  It is also exported from the Zig module as `ghostty.TinyIo` so
  Zig embedders can opt into the same size win when constructing
  terminals.
  ```
- [`d524a0f`](https://github.com/ghostty-org/ghostty/commit/d524a0fe645cfd4d9ae27bd8451b934dcf2ebaef) libghostty: guard release builds against std debug Io ([@mitchellh](https://github.com/mitchellh))
  ```text
  Release libghostty-vt builds carefully avoid referencing
  std.Options.debug_io because its default implementation is
  std.Io.Threaded, and referencing that vtable keeps every operation
  Threaded supports linked into the binary: roughly 110KB of unreachable
  code. Nothing references it today, but any std.debug.print,
  std.debug.lockStderr, or std.log default-handler call added to
  release-reachable code would silently reintroduce all of it.
  
  Declare std_options_debug_io in the root module so std uses our value
  instead of constructing the Threaded default. Development builds
  (Debug, ReleaseSafe, tests) forward the std default so std.debug.print
  and friends work normally. ReleaseFast and ReleaseSmall builds declare
  it as a @compileError: since std only analyzes the declaration lazily,
  at the moment something references a debug Io code path, the error
  fires exactly at the offending reference, turning a silent size
  regression into a build failure with a message explaining the
  alternatives.
  
  Release binaries are byte-identical when the guard is not tripped.
  ```
- [`a15ddda`](https://github.com/ghostty-org/ghostty/commit/a15dddae2a497e6540feca5c6adc7e86edd59adb) TinyIo: fix failing tests in CI ([@mitchellh](https://github.com/mitchellh))
- [`fea378e`](https://github.com/ghostty-org/ghostty/commit/fea378e565c8ddb7f49808c4f2e36a4a932e35ff) libghostty: reduce binary size ~16% (macOS), ~22% (Linux) ([#13715](https://github.com/ghostty-org/ghostty/issues/13715)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This shrinks the binary size of libghostty-vt by **16% on aarch64 macOS
  and 22% on x86_64 Linux**. It also shrinks the in-memory footprint by
  ~256KB per thread + ~20KB per app. All benchmarks remain the same, no
  speedups or slowdowns.
  
  Each commit message explains an individual tactic used, but to
  summarize:
  
  1. **No stack traces in release panic handlers (~160KB).** This requires
  the Zig stack unwind and symbolication logic. I don't think this makes
  sense in an embedded library because the embedder should handle this.
  
  2. **An alternate `std.Io` implementation called `TinyIo` (~100KB to
  200KB).** See later... since this is the big one.
  
  3. **Disable recursive Parser.Action logging (~35KB).** We now only log
  the top-level fields of a Parser.Action, which lowers the amount of
  `std.fmt` codegen significantly.
  
  All sizes above are aarch64 macOS and x86_64 Linux ReleaseFast
  libghostty builds.
  
  ## TinyIo
  
  I think the main complexity introduction here is our alternate `std.Io`
  implementation `TinyIo`. This is an IO implementation that implements IO
  operations we need through direct syscalls and does not support
  concurrency or any other options like network, progress, etc.
  
  Why? Because of the way `std.Io` works through vtable dispatch, the
  linker and dead code removal can't prune ANY of the function pointers.
  So our binary has full implementations of all the networking,
  concurrency, etc. related code even though we don't use it.
  
  This has a runtime effect too: even though we put `std.Io.Threaded` in
  single-threaded mode, it still allocates ~256KB of TLS _per thread_, and
  its raw struct state is ~18KB (versus 80 _bytes_ for `TinyIo`).
  
  For future maintenance: I exhaustively implemented the vtable rather
  than use the failing vtable from Zig stdlib so any Zig changes to add
  new fields to this error so we can determine if we want to support it or
  not.
  ```
- [`034506f`](https://github.com/ghostty-org/ghostty/commit/034506f14562242c70618aaf5775366766653ffd) gtk: add +new-tab cli action ([@jcollie](https://github.com/jcollie))
- [`9d8fbd1`](https://github.com/ghostty-org/ghostty/commit/9d8fbd15b3b4e385b82c1a9e31cdbb99a74dabd6) gtk: add +new-tab action ([#11762](https://github.com/ghostty-org/ghostty/issues/11762)) ([@jcollie](https://github.com/jcollie))
  ```text
  This PR adds a `+new-tab` CLI action, useful for automation on GTK. This
  mainly re-uses machinery added for the `+new-window`, but adds in a
  unique surface ID for identifying surfaces for IPC purposes (and
  eliminates use of raw pointers for callbacks from notifications).
  ```
- [`16e13a5`](https://github.com/ghostty-org/ghostty/commit/16e13a59aeda57ccb1b9998ab989615960dbcafb) build: fix Linux Android SDK fallback path ([@fornwall](https://github.com/fornwall))
  ```text
  Use the standard ~/Android/Sdk capitalization for the Linux SDK fallback.
  
  This lets NDK discovery work when neither ANDROID_NDK_HOME nor an SDK
  environment variable is set.
  ```
- [`74f91d1`](https://github.com/ghostty-org/ghostty/commit/74f91d1b439e7b906f003e60a65bd8994c3c77a5) macOS: support `drag-handle` config ([@bo2themax](https://github.com/bo2themax))
- [`fde9e28`](https://github.com/ghostty-org/ghostty/commit/fde9e281c4a6bd9e62d87eedc66e3c3dc48e40cc) agents: remove double negative ([@jparise](https://github.com/jparise))
- [`349664f`](https://github.com/ghostty-org/ghostty/commit/349664f031852bc6cca44c96dda7bf2b779d0402) agents: remove double negative ([#13710](https://github.com/ghostty-org/ghostty/issues/13710)) ([@mitchellh](https://github.com/mitchellh))
- [`da59a2e`](https://github.com/ghostty-org/ghostty/commit/da59a2ec42744e81c4cdafbd2a3507f257c455be) macOS: support `drag-handle` config ([#13709](https://github.com/ghostty-org/ghostty/issues/13709)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Closes https://github.com/ghostty-org/ghostty/discussions/12332
  
  Also a tiny rephrasing for the documentation.
  ```
- [`2dc0883`](https://github.com/ghostty-org/ghostty/commit/2dc08839b1a1a331d9ba71ca097c5f8db2965182) build: fix Linux Android SDK fallback path ([#13705](https://github.com/ghostty-org/ghostty/issues/13705)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Use the standard `~/Android/Sdk` capitalization for the Linux SDK
  fallback.
  
  This lets NDK discovery work when neither `ANDROID_NDK_HOME` nor an
  `SDK` environment variable is set.
  ```
- [`c6e7e9e`](https://github.com/ghostty-org/ghostty/commit/c6e7e9e4e2fa27e1a5dea57e878eb1146faaf62b) config: add `drag-handle` ([@pluiedev](https://github.com/pluiedev))
- [`65a3e66`](https://github.com/ghostty-org/ghostty/commit/65a3e666efdda5191051f94a5414eb2cf516245c) gtk: drag overlay toggle ([@pluiedev](https://github.com/pluiedev))
- [`850ca8c`](https://github.com/ghostty-org/ghostty/commit/850ca8c7b1c69078621aea638bb6564d7b3d53b5) gtk: rebind is-split after moving split cross-tree ([@pluiedev](https://github.com/pluiedev))
  ```text
  It turns out we never unbound the split from its original tree after
  moving, which means `is-split` in particular is desynced and leads to
  hilarious artifacts like how `unfocused-split-*` options just stop
  working properly. I only realized this is a thing after the naïve
  drag handle config option didn't work properly. Fun!
  ```
- [`05221c1`](https://github.com/ghostty-org/ghostty/commit/05221c11c9db0715666fc6e038915128fc6a563e) core,gtk: add `drag-handle` config ([#13706](https://github.com/ghostty-org/ghostty/issues/13706)) ([@pluiedev](https://github.com/pluiedev))
  ```text
  Fixes hundreds of complaints about the fact that drag handles cannot be
  hidden, on GTK at least.
  
  I'm not sure if we ever made an issue for this? If you come across any
  discussions asking for this, please link them here :)
  ```
- [`74efadb`](https://github.com/ghostty-org/ghostty/commit/74efadb446205eb052ce10d202300b2dc8970947) lib-vt: answer XTGETTCAP queries ([@fornwall](https://github.com/fornwall))
  ```text
  Ghostty's full termio path answers XTGETTCAP from the static terminfo
  map, but terminal/stream_terminal.zig, which backs libghostty-vt,
  parses the same DCS request and then discards it. There is no XTGETTCAP
  effect either, so an embedder cannot restore the replies through the
  C API.
  
  Programs query these over SSH instead of assuming the remote host has
  the client's terminfo entry. This matters more for an embedder than for
  the desktop app, which can install its entry on the remote through
  shell integration.
  
  Answer the queries in stream_terminal the same way termio does: look
  up each requested key in the static terminfo map and write the reply
  to the pty, skipping the lookups entirely when no write_pty effect is
  set. The map now stores null-terminated responses so they can be
  handed straight to write_pty without copying. terminal/dcs.zig and the
  termio path are unchanged.
  
  "TN" is handled separately. It names the terminfo entry the terminal
  runs as, so it has to agree with TERM -- which is set in
  termio/Exec.zig, a layer libghostty-vt does not contain. The library
  never sees TERM and cannot answer on the embedder's behalf, and
  answering with Ghostty's own entry from the static map would misreport
  every embedder, so "TN" is intercepted before the map lookup. The name
  is instead configured through a new option,
  GHOSTTY_TERMINAL_OPT_TERMINFO_NAME: the string is copied into the
  terminal, names longer than 128 bytes are rejected, and while unset
  the query goes unanswered.
  
  This is the first dependency from src/terminal on src/terminfo, so
  libghostty-vt now carries Ghostty's terminfo table: +16,023 bytes
  (+1.9%) on a wasm32-freestanding ReleaseSmall build.
  ```
- [`f64f4ac`](https://github.com/ghostty-org/ghostty/commit/f64f4aca2c29b554d111b36c3d946a9bddd159ff) lib-vt: answer XTGETTCAP queries ([#13530](https://github.com/ghostty-org/ghostty/issues/13530)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Ghostty's full termio path answers XTGETTCAP from the static terminfo
  map, but `terminal/stream_terminal.zig`, which backs libghostty-vt,
  parses the same DCS request and then discards it. There is no XTGETTCAP
  effect either, so an embedder cannot restore the replies through the C
  API.
  
  Programs query these over SSH instead of assuming the remote host has
  the client's terminfo entry. This matters more for an embedder than for
  the desktop app, which can install its entry on the remote through shell
  integration.
  
  Answer the queries in `stream_terminal` the same way termio does: look
  up each requested key in the static terminfo map and write the reply to
  the pty, skipping the lookups entirely when no `write_pty` effect is
  set. The map now stores null-terminated responses so they can be handed
  straight to `write_pty` without copying. `terminal/dcs.zig` and the
  termio path are unchanged.
  
  `TN` is handled separately. It names the terminfo entry the terminal
  runs as, so it has to agree with `TERM` — which is set in
  `termio/Exec.zig`, a layer libghostty-vt does not contain. The library
  never sees `TERM` and cannot answer on the embedder's behalf, and
  answering with Ghostty's own entry from the static map would misreport
  every embedder, so `TN` is intercepted before the map lookup. The name
  is instead configured through a new option,
  `GHOSTTY_TERMINAL_OPT_TERMINFO_NAME`: the string is copied into the
  terminal, names longer than 128 bytes are rejected, and while unset the
  query goes unanswered.
  
  This is the first dependency from `src/terminal` on `src/terminfo`, so
  libghostty-vt now carries Ghostty's terminfo table: +16,023 bytes
  (+1.9%) on a `wasm32-freestanding` `ReleaseSmall` build.
  
  ---
  
  AI usage: Created with claude code and opus 5. I have reviewed the code
  and made modifications where it made sense. I have also tested this end
  to end in an application.
  ```
- [`afb351f`](https://github.com/ghostty-org/ghostty/commit/afb351f8385d8b895671cb398d13fb39e06611f4) terminal/stream: fast-path APC termination ([@mitchellh](https://github.com/mitchellh))
  ```text
  APC payload bytes are bulk consumed, but the terminating byte still passed
  through the generic parser action loop. Handle ESC and C1 ST directly after
  bulk consumption while leaving other transitions on the scalar path.
  ```
- [`b537282`](https://github.com/ghostty-org/ghostty/commit/b537282411ae731f3d49705be391320ff5f51e9e) terminal/apc: support reporting unknown APC sequences ([@mitchellh](https://github.com/mitchellh))
- [`6b990de`](https://github.com/ghostty-org/ghostty/commit/6b990de5be7fcce9ffc7bed1a713f64c8503fbff) terminal: C API for unknown sequences ([@mitchellh](https://github.com/mitchellh))
- [`7e8b4f3`](https://github.com/ghostty-org/ghostty/commit/7e8b4f360be6f9aea0bced4641e25dd564d60abc) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`94beef8`](https://github.com/ghostty-org/ghostty/commit/94beef81efad44514c328564d2e6c2fefc243712) libghostty: effect for unknown sequence (APC only this PR) ([#13702](https://github.com/ghostty-org/ghostty/issues/13702)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This introduces a new effect for Zig/C callers to detect unknown
  sequences.
  
  This PR starts only with APC, but the API shape is such that we can add
  other types (OSC next) in future PRs. The goal of this is to have zero
  overhead in the disabled/undetected (both) case, and minimal overhead in
  the detected case.
  
  This is important in particular for libghostty consumers because it
  allows them to implement their own custom protocols and/or support
  features libghostty doesn't support. It isn't possible to support them
  at the same performance libghostty does but supporting them in general
  is usually valuable.
  
  From a Zig API to enable this, users must set `unknown_max_bytes` for
  the APC handler AND update their stream handler to recognize unknown
  sequences. The built-in `stream_terminal` stream type has an exposed
  callback for this, so both must be set.
  ```
- [`163e229`](https://github.com/ghostty-org/ghostty/commit/163e229756e632e39838a9f6e26402269dda213a) Update iTerm2 colorschemes ([#13704](https://github.com/ghostty-org/ghostty/issues/13704)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260803-155300-875a82f
  ```

## August 8, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/31271139905), [2](https://github.com/ghostty-org/ghostty/actions/runs/31267536850), [3](https://github.com/ghostty-org/ghostty/actions/runs/31240383705)  
Summary: 3 runs • 4 commits • 3 authors

### Changes

- [`a6fc3e0`](https://github.com/ghostty-org/ghostty/commit/a6fc3e0e2e78aeb4219ce4ef6b866cc06b1b0e09) gtk/wayland: clean up blur regions ([@gotenksIN](https://github.com/gotenksIN))
  ```text
  Destroy temporary Wayland regions after each blur update and release
  the previous cached blur region before replacing it. This prevents
  resources from leaking while the blur region changes.
  ```
- [`136f436`](https://github.com/ghostty-org/ghostty/commit/136f436a3bbb14fd48d18e927a83fc6585d5a63c) gtk/wayland: clean up blur regions ([#13699](https://github.com/ghostty-org/ghostty/issues/13699)) ([@pluiedev](https://github.com/pluiedev))
  ```text
  Fix two resource leaks when the Wayland background blur region changes.
  
  Temporary `wl_region` objects were destroyed only after an error. They
  are now always destroyed after the blur request. The previous cached
  blur region is also released before its replacement.
  
  This change does not alter protocol selection or add new Wayland
  protocols.
  
  Testing:
  
  - Verified blur on KDE Plasma 6.7.4 with GTK 4.22.4.
  - Verified with `zig build -Doptimize=ReleaseFast`.
  
  This code was written with assistance from GPT 5.6 Sol and manually
  reviewed.
  ```
- [`6e647a1`](https://github.com/ghostty-org/ghostty/commit/6e647a1cbd96175fee710a34c7116c06f0bf14b3) Update VOUCHED list ([#13697](https://github.com/ghostty-org/ghostty/issues/13697)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/13693#issuecomment-5227046478)
  from @tristan957.
  
  Vouch: @gotenksIN
  ```
- [`4714732`](https://github.com/ghostty-org/ghostty/commit/47147324cee9d12b537f0ea204bf16449d706b3a) Update VOUCHED list ([#13691](https://github.com/ghostty-org/ghostty/issues/13691)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/13690#issuecomment-5224579870)
  from @00-kat.
  
  Vouch: @a-lang
  ```

## August 7, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/31217902577), [2](https://github.com/ghostty-org/ghostty/actions/runs/31191840813), [3](https://github.com/ghostty-org/ghostty/actions/runs/31189543209), [4](https://github.com/ghostty-org/ghostty/actions/runs/31187359620), [5](https://github.com/ghostty-org/ghostty/actions/runs/31146859128)  
Summary: 5 runs • 28 commits • 9 authors

### Changes

- [`e83cf0b`](https://github.com/ghostty-org/ghostty/commit/e83cf0b06f504be8917292b180ac65b0de685ac0) macOS: fix quit alert missing when hidden ([@bo2themax](https://github.com/bo2themax))
- [`2602886`](https://github.com/ghostty-org/ghostty/commit/2602886144c7e95099c9e2ba07f181c69e7276f3) macOS: fix quit alert missing when hidden ([#13686](https://github.com/ghostty-org/ghostty/issues/13686)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes https://github.com/ghostty-org/ghostty/discussions/13685.
  
  Removed presumably deprecated check introduced in
  8f1a014afd9c6724b767b2fbf65d27d26b3c01e5 for update pill
  > I checked for auto update as well, it works as before this, and for
  manual updates we're not confirming anyway, so I think its safe to
  remove it now.
  
  Each BaseTerminalController already has quit check and confirming code
  added in that review windows pr. It didn't cover QT before, overriding
  it to animate in for showing alert.
  
  [#5450](https://github.com/ghostty-org/ghostty/issues/5450) stays fixed.
  
  
  
  
  https://github.com/user-attachments/assets/dbf36f16-e3ce-4f6a-bc25-367fe48739b9
  ```
- [`e11bfb5`](https://github.com/ghostty-org/ghostty/commit/e11bfb513919c51d3f842a367c787ab026d8d868) macos: sync appearance when new windows are created ([#13324](https://github.com/ghostty-org/ghostty/issues/13324)) ([@zenangst](https://github.com/zenangst))
  ```text
  call `syncAppearance` after `super.showWindow` has been called to
  ensure that the window is visible.
  ```
- [`b9113d2`](https://github.com/ghostty-org/ghostty/commit/b9113d2e7f0a978003a82b9a2deb8b27e2f1bb80) build: fix flatpak/snap, restore rpath opt, fix local gtk4-layer-shell ([@vancluever](https://github.com/vancluever))
  ```text
  This fixes regressions in the flatpak/snap builds, and knock-on stuff
  that was discovered as as a result:
  
  * Update the Zig versions in the flatpak/snap build configuration files.
  * Restore the classic -Dpatch-rpath option, and add a new -Dpatch-interp
    option. This ensures that the snap can still use -Dpatch-rpath
    correctly.
  * There seems to be an issue in Zig when parsing IPv6 addresses that
    leads to issues loading resolv.conf files; when trying to load a
    nameserver that has an IPv6 address with a numeric interface index as
    the scoped zone ID, Zig will try to resolve the interface as a name
    rather than just use the index. This is coming up in snap builds
    because the build process seems to, by default, use the exhaustive
    /run/systemd/resolve/resolv.conf file, versus the simpler stub
    (stub-resolv.conf) file. We work around this for the time being by
    linking the stub at the end of the Zig part, overwriting the link to
    the non-stub file.
  * Fixed gtk4-layer-shell packaging - the migration to external
    translate-c meant that non-system builds of the dependency were not
    handing the local gtk4-layer-shell headers over for translation. Now,
    instead, we've extracted the management of the gtk4-layer-shell source
    and wayland-protocols generation to a locally-cached object so that
    the source can be shared by both C translation and the library build
    in a way that is not coupled to any particular step.
  ```
- [`219173a`](https://github.com/ghostty-org/ghostty/commit/219173ab370839889a191d3fd6855e53cb82e95d) terminal/snapshot: remove BLAKE3 digests ([@mitchellh](https://github.com/mitchellh))
  ```text
  Remove BLAKE3 prefix digests. Keep READY/FINISH as empty records since
  they're semantically important markers.
  
  Our existing format (CRC32 per-record, declared counts, strict tag ordering
  requirements, etc.) already detect: accidental corruption, truncation,
  data omission, and duplication.
  
  BLAKE3 only protects against valid records being swapped or removed entirely.
  It is heavy for just that, and callers can solve that anyways via their
  own transport (like, just use TCP). For more adversarial protection,
  callers can also add layers like TLS or their own alternate signing
  methods depending on their own threat models.
  
  Removing the hash improves encode times by ~1.4x, decode times by ~1.3x.
  Time-to-READY decoding is effectively unchanged because it was such a
  small package to begin with.
  ```
- [`fd98370`](https://github.com/ghostty-org/ghostty/commit/fd98370211d5e1657a3430dde5ca1c59cb5f92ab) macOS: fix swiftlint ([@bo2themax](https://github.com/bo2themax))
- [`0a78672`](https://github.com/ghostty-org/ghostty/commit/0a78672e7cd4303588aada1d7bf2a6a28129cb65) build: fix flatpak/snap, restore rpath opt, fix local gtk4-layer-shell ([#13677](https://github.com/ghostty-org/ghostty/issues/13677)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This fixes regressions in the flatpak/snap builds, and knock-on stuff
  that was discovered as as a result:
  
  * Update the Zig versions in the flatpak/snap build configuration files.
  * Restore the classic `-Dpatch-rpath` option, and add a new
  `-Dpatch-interp` option. This ensures that the snap can still use
  `-Dpatch-rpath` correctly.
  * There seems to be an issue in Zig when parsing IPv6 addresses that
  leads to issues loading `resolv.conf` files; when trying to load a
  nameserver that has an IPv6 address with a numeric interface index as
  the scoped zone ID, Zig will try to resolve the interface as a name
  rather than just use the index. This is coming up in snap builds because
  the build process seems to, by default, use the exhaustive
  `/run/systemd/resolve/resolv.conf` file, versus the simpler stub
  (`stub-resolv.conf`) file. We work around this for the time being by
  linking the stub at the end of the Zig part, overwriting the link to the
  non-stub file.
  * Fixed `gtk4-layer-shell` packaging - the migration to external
  translate-c meant that non-system builds of the dependency were not
  handing the local `gtk4-layer-shell` headers over for translation. Now,
  instead, we've extracted the management of the `gtk4-layer-shell` source
  and `wayland-protocols` generation to a locally-cached object so that
  the source can be shared by both C translation and the library build in
  a way that is not coupled to any particular step.
  ```
- [`204989a`](https://github.com/ghostty-org/ghostty/commit/204989ad90e3ca104eb76e55a77afb185f2ed074) terminal/snapshot: remove BLAKE3 digests ([#13680](https://github.com/ghostty-org/ghostty/issues/13680)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Remove BLAKE3 prefix digests. Keep READY/FINISH as empty records since
  they're semantically important markers.
  
  Our existing format (CRC32 per-record, declared counts, strict tag
  ordering requirements, etc.) already detect: accidental corruption,
  truncation, data omission, and duplication.
  
  BLAKE3 only protects against valid records being swapped or removed
  entirely. It is heavy for just that, and callers can solve that anyways
  via their own transport (like, just use TCP). For more adversarial
  protection, callers can also add layers like TLS or their own alternate
  signing methods depending on their own threat models.
  
  Removing the hash improves encode times by ~1.4x, decode times by ~1.3x.
  Time-to-READY decoding is effectively unchanged because it was such a
  small package to begin with.
  
  **AI usage:** I had it clean up the comments and the tests, but I did
  the blake3 removal and marker changes, and wrote the commit message
  myself. All reviewed.
  ```
- [`34282fc`](https://github.com/ghostty-org/ghostty/commit/34282fc7b3ba3e7f42281db73647a83768710f89) macOS: fix swiftlint ([#13684](https://github.com/ghostty-org/ghostty/issues/13684)) ([@mitchellh](https://github.com/mitchellh))
- [`4693e1b`](https://github.com/ghostty-org/ghostty/commit/4693e1b546dfc00128d5fe83533def5a92c69ab0) macos: sync appearance when new windows are created ([#13675](https://github.com/ghostty-org/ghostty/issues/13675)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  For new windows to get their appearance synced, we need to call
  `syncAppearance` after `super.showWindow(sender)`. All previous calls to
  `syncAppearance` on `TerminalWindow` will be ignored because the window
  needs to have `isVisible` set to `true`.
  
  This regression was introduced by:
  5368adcd29754939e6c283198ef6b1c122293815
  
  It added `.dropFirst()` to the `focusedSurface` appearance publishers in
  `TerminalController.swift` which removes the initial call of the
  subscription.
  
  Fixes https://github.com/ghostty-org/ghostty/issues/13324
  
  (landed on the same fix as @rasitakyol found here:
  https://github.com/ghostty-org/ghostty/pull/13341)
  ```
- [`daeed25`](https://github.com/ghostty-org/ghostty/commit/daeed25b378d219268ad023e9a18b933a74b3250) font/coretext: creation functions can return null, handle OOM ([@mitchellh](https://github.com/mitchellh))
  ```text
  Catch NULL results from CoreFoundation/CoreText creation functions and
  return error.OOM rather than null derefs later. I verified that this is
  possible but didn't verify the behavior when it happens, this is just
  defensive based on the report here: #13671 because it costs us nothing
  really.
  ```
- [`9682685`](https://github.com/ghostty-org/ghostty/commit/96826853bde13bad0825cd0afe35584a0760d17a) macOS: fix window sizing after dragging a split into a window ([@bo2themax](https://github.com/bo2themax))
- [`571c62d`](https://github.com/ghostty-org/ghostty/commit/571c62dada5da79f68d12d376957cc1d02d846b1) font/coretext: creation functions can return null, handle OOM ([#13679](https://github.com/ghostty-org/ghostty/issues/13679)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Catch NULL results from CoreFoundation/CoreText creation functions and
  return error.OOM rather than null derefs later. I verified that this is
  possible but didn't verify the behavior when it happens, this is just
  defensive based on the report here: #13671 because it costs us nothing
  really.
  ```
- [`faeac91`](https://github.com/ghostty-org/ghostty/commit/faeac91fa5ea91d855d623c551c18036dbaa0209) macOS: fix window sizing after dragging a split into a window ([#13682](https://github.com/ghostty-org/ghostty/issues/13682)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Regression from
  [#13601](https://github.com/ghostty-org/ghostty/issues/13601), but I
  don't see why it matters. But the surface's bounds changes after
  window's created.
  ```
- [`44a05a8`](https://github.com/ghostty-org/ghostty/commit/44a05a88aad347916fd2447bf29b637d553238b7) macos: discard debounced selection notification ([@mitchellh](https://github.com/mitchellh))
  ```text
  Discard the selection notification payload before debouncing
  accessibility changes.
  
  The debouncer previously retained the notification and its surface
  object, keeping a closed tab's view and PTY alive after the undo
  timeout.
  ```
- [`fcee198`](https://github.com/ghostty-org/ghostty/commit/fcee19819e0a0fa6656ca8f3a946d193edf63cc9) macos: discard debounced selection notification ([#13676](https://github.com/ghostty-org/ghostty/issues/13676)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Discard the selection notification payload before debouncing
  accessibility changes.
  
  The debouncer previously retained the notification and its surface
  object, keeping a closed tab's view and PTY alive after the undo
  timeout.
  ```
- [`7f96e0b`](https://github.com/ghostty-org/ghostty/commit/7f96e0bdab175deb7205ec54e0c8a084283bf015) Update VOUCHED list ([#13683](https://github.com/ghostty-org/ghostty/issues/13683)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/13675#issuecomment-5218250080)
  from @jcollie.
  
  Vouch: @zenangst
  ```
- [`25b2d8a`](https://github.com/ghostty-org/ghostty/commit/25b2d8a38568eab31283786f6a1f1501411863b5) input,apprt: add new_tab_to_new_window action ([@pluiedev](https://github.com/pluiedev))
- [`f6fca9a`](https://github.com/ghostty-org/ghostty/commit/f6fca9aabffc4f0576f9c427672b1972ed813dec) gtk: implement `move_tab_to_new_window` ([@pluiedev](https://github.com/pluiedev))
- [`f03d71d`](https://github.com/ghostty-org/ghostty/commit/f03d71d970a65aa6f58b6a836469258fbf2d52f4) po: update template ([@pluiedev](https://github.com/pluiedev))
- [`18f06ef`](https://github.com/ghostty-org/ghostty/commit/18f06ef03c8827cb2f794741c469b7091a2da112) macOS: fix unsupported action falls through wrong handling ([@bo2themax](https://github.com/bo2themax))
- [`1118773`](https://github.com/ghostty-org/ghostty/commit/111877354edd2c29a78f35c2023492d699454026) core,gtk: add move_tab_to_new_window action ([#13621](https://github.com/ghostty-org/ghostty/issues/13621)) ([@pluiedev](https://github.com/pluiedev))
  ```text
  Implements most of #2630
  
  This is in reality a really simple change and ideally we can get this
  out before the 1.4 string freeze
  ```
- [`22d1317`](https://github.com/ghostty-org/ghostty/commit/22d13172cde98a0a4dda05d3d6a3fcb0dd8ed018) macOS: fix unsupported action falls through wrong handling ([#13668](https://github.com/ghostty-org/ghostty/issues/13668)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  There're won't be any visible errors, but
  `keybind=cmd+r=toggle_tab_overview/toggle_window_decorations/size_limit/quit_time`
  shouldn't go to `showChildExited`
  
  ## AI Disclosure
  
  Found by Claude during another quest, but I changed on myself.
  ```
- [`a14eba7`](https://github.com/ghostty-org/ghostty/commit/a14eba7478fc1af4e6e0cf4a793728d308f3278f) input: update toggle_maximize documentation ([@claude](https://github.com/claude))
- [`c011ad8`](https://github.com/ghostty-org/ghostty/commit/c011ad87070a742b39eaffee800a006f3c977988) Update wording ([@bo2themax](https://github.com/bo2themax))
- [`f9b2ad8`](https://github.com/ghostty-org/ghostty/commit/f9b2ad8dbed93e0b8cdd6320d8f5a46ba15c5bc8) input: update toggle_maximize documentation ([#13673](https://github.com/ghostty-org/ghostty/issues/13673)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## AI Closure
  
  Claude found and changed it
  ```
- [`987f442`](https://github.com/ghostty-org/ghostty/commit/987f44260d10a9f685d06f0ff638457aee64f2f2) cli: add g/G as vi-style aliases for Home/End in list-themes ([@bousii](https://github.com/bousii))
- [`7e567c3`](https://github.com/ghostty-org/ghostty/commit/7e567c3f03e914140f0b6beb8b03c20efcc03188) cli: add g/G as vi-style aliases for Home/End in list-themes ([#13681](https://github.com/ghostty-org/ghostty/issues/13681)) ([@jcollie](https://github.com/jcollie))
  ```text
  I was messing around with this tool the other day on a 60% keyboard so I
  thought this would be a nice addition for situations like that. Keeps in
  line with the vi/less j and k inputs that this tool has as well.
  ```

## August 6, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/31109909886), [2](https://github.com/ghostty-org/ghostty/actions/runs/31075330039), [3](https://github.com/ghostty-org/ghostty/actions/runs/31070313370)  
Summary: 3 runs • 14 commits • 4 authors

### Changes

- [`cfc19e8`](https://github.com/ghostty-org/ghostty/commit/cfc19e8053b96dbc9a7d7994b84ec6eef7eb17de) libghostty: add configurable mode defaults, remove mode_set/get ([@mitchellh](https://github.com/mitchellh))
  ```text
  ABI BREAKING: This removes `ghostty_terminal_mode_get` and `_mode_set`.
  We can now represent these operations completely with standard
  `ghostty_terminal_get` and `ghostty_terminal_set`, which makes it much
  more flexible to preserve ABI in the future.
  
  This is all centered around a new `GhosttyTerminalModeConfig` structure
  that is an in or out parameter depending on use case.
  
  This also adds a new `GHOSTTY_TERMINAL_OPT_MODE_DEFAULT` option that
  can be used to set the _default_ value of mode that happens when a RIS
  event (full reset) is sent.
  ```
- [`301bd6f`](https://github.com/ghostty-org/ghostty/commit/301bd6f8b0251301f25f0943f85264fd8f6845e3) macOS: hide settings menu icon on macOS 27 ([@bo2themax](https://github.com/bo2themax))
  ```text
  Settings appears to be somehow special and it's not hidden previously.
  ```
- [`76907d8`](https://github.com/ghostty-org/ghostty/commit/76907d8de8c78f51d3c44a941772759da24cbc5f) macOS: remove flaky color match tests ([@bo2themax](https://github.com/bo2themax))
- [`33bdeed`](https://github.com/ghostty-org/ghostty/commit/33bdeed1cbc69196c10466d0c9d881c0a7a7ac9c) macOS: remove flaky color match tests ([#13667](https://github.com/ghostty-org/ghostty/issues/13667)) ([@mitchellh](https://github.com/mitchellh))
- [`99c483f`](https://github.com/ghostty-org/ghostty/commit/99c483f477dcf3d6523a976772dcac71ab9466d3) macOS: hide settings menu icon on macOS 27 ([#13664](https://github.com/ghostty-org/ghostty/issues/13664)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Settings appears to be somehow special and it's not hidden previously.
  
  This would require building with Xcode 27 tho.
  
  <img width="704" height="364" alt="image"
  src="https://github.com/user-attachments/assets/2cb23a01-6840-40a2-b794-6a8e914aaa7d"
  />
  ```
- [`afa9e4f`](https://github.com/ghostty-org/ghostty/commit/afa9e4fad065653a87e89e9ea75c54ee7fb3f94a) libghostty: add configurable mode defaults, remove mode_set/get ([#13661](https://github.com/ghostty-org/ghostty/issues/13661)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ABI BREAKING: This removes `ghostty_terminal_mode_get` and `_mode_set`.
  We can now represent these operations completely with standard
  `ghostty_terminal_get` and `ghostty_terminal_set`, which makes it much
  more flexible to preserve ABI in the future.
  
  This is all centered around a new `GhosttyTerminalModeConfig` structure
  that is an in or out parameter depending on use case.
  
  This also adds a new `GHOSTTY_TERMINAL_OPT_MODE_DEFAULT` option that can
  be used to set the _default_ value of mode that happens when a RIS event
  (full reset) is sent. Note that not all modes are configurable because
  some are set based on live terminal state and aren't modes in and of
  themselves.
  
  ## Why Delete Functions? Why Not Add?
  
  Once tagged, the goal of `libghostty-vt` is to remain HIGHLY ABI
  compatible. We are striving for top tier ABI compatibility similar to
  legendary C libraries. That means we need to be highly confident in our
  API shapes: functions, structs, etc. and using shapes that we can retain
  ABI compatibility even as we add features. Every function is a risk. By
  pushing stuff into our `_get/_set` patterns, its easier to maintain ABI
  compatibility.
  ```
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

