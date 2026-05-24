> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: May 24, 2026 at 21:19 UTC.

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

## May 22, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26299049671), [2](https://github.com/ghostty-org/ghostty/actions/runs/26262927116)  
Summary: 2 runs • 33 commits • 9 authors

### Changes

- [`3c2c596`](https://github.com/ghostty-org/ghostty/commit/3c2c596dc77679385e18039052e2b7556049e07f) fix global keybinds from not repsonding anymore ([@adrum](https://github.com/adrum))
- [`3828660`](https://github.com/ghostty-org/ghostty/commit/3828660382483a9eae10c0a4e4c3d0ae826d3aed) Merge branch 'main' into fix/keybind ([@adrum](https://github.com/adrum))
- [`484d6ec`](https://github.com/ghostty-org/ghostty/commit/484d6ec66b0c27808341c05eb71416a39517ad03) cli: add an ssh-wrapping +ssh action ([@jparise](https://github.com/jparise))
  ```text
  Add a drop-in `ssh` wrapper that sets up the remote environment for
  Ghostty. Anything not consumed as one of our own flags is forwarded to
  the real, wrapped `ssh` binary. It can be used directly (`ghostty +ssh
  user@host`), aliased (`alias ssh='ghostty +ssh --'`), or invoked through
  Ghostty's shell integration.
  
  Before exec'ing ssh, `+ssh`:
  
  - Forwards Ghostty environment to the remote (`--forward-env`): sets
    TERM=xterm-256color and requests SendEnv forwarding of COLORTERM,
    TERM_PROGRAM, and TERM_PROGRAM_VERSION.
  - Installs Ghostty's terminfo on the remote (`--terminfo`), informed by
    our existing `ssh-cache` system and using our internal xterm-ghostty
    terminfo representation.
  
  A third flag, `--cache`, controls cache use; `--cache=false` bypasses
  both read and write, which is useful for scripting and for debugging
  install failures without polluting the cache.
  
  For shell integration, this replaces the per-shell logic (which made up
  roughly a third of our shell integration scripts) with a simple wrapper
  function that translates GHOSTTY_SHELL_FEATURES into a `ghostty +ssh`
  command line. This commit only migrates the bash integration; the other
  shells will follow separately.
  ```
- [`2d11205`](https://github.com/ghostty-org/ghostty/commit/2d112059a7e87104a483866ff472638e3ebd81b1) zsh: replace ssh wrapper with ghostty +ssh ([@jparise](https://github.com/jparise))
  ```text
  Replace the inline ssh integration with a thin wrapper that translates
  GHOSTTY_SHELL_FEATURES into a `ghostty +ssh` command line. The shell
  wrapper no longer carries terminfo install, ControlMaster wiring, or
  cache bookkeeping; it just maps the feature flags to flags on `+ssh`
  and forwards everything else.
  ```
- [`283dca1`](https://github.com/ghostty-org/ghostty/commit/283dca130e02945aed1d3f2eae43676d37782717) fish: replace ssh wrapper with ghostty +ssh ([@jparise](https://github.com/jparise))
  ```text
  Replace the inline ssh integration with a thin wrapper that translates
  GHOSTTY_SHELL_FEATURES into a `ghostty +ssh` command line.
  ```
- [`e537810`](https://github.com/ghostty-org/ghostty/commit/e5378107eb8ffff72ba98eab45092b569f56bcf0) elvish: replace ssh wrapper with ghostty +ssh ([@jparise](https://github.com/jparise))
  ```text
  Replace the inline ssh integration with a thin wrapper that translates
  GHOSTTY_SHELL_FEATURES into a `ghostty +ssh` command line.
  ```
- [`ac103b8`](https://github.com/ghostty-org/ghostty/commit/ac103b8f75f5206af3cc98deecc2b7d0f9705683) nushell: replace ssh wrapper with ghostty +ssh ([@jparise](https://github.com/jparise))
  ```text
  Replace the inline ssh integration with a thin wrapper that translates
  GHOSTTY_SHELL_FEATURES into a `ghostty +ssh` command line. When no
  ssh-* feature is enabled, the wrapper falls through to the real `ssh`
  binary unchanged so nushell users without ssh integration get plain
  ssh behavior.
  ```
- [`3f11e69`](https://github.com/ghostty-org/ghostty/commit/3f11e695d0fd8f3cabc2c46c7a091c0509884b41) fix: apply variation selectors to preceding codepoint ([@noib3](https://github.com/noib3))
  ```text
  This fixes a bug where the variation selectors (VS15 & VS16) were
  checked against the first codepoint in a cell instead of the previous
  codepoint in the cell's grapheme cluster, causing them to be dropped if
  the first codepoint was not a valid base.
  ```
- [`c44afa6`](https://github.com/ghostty-org/ghostty/commit/c44afa62506dd94b9dcc680da412ddb650931b3b) fix: preserve active cursor position during reflow ([@noib3](https://github.com/noib3))
  ```text
  This PR fixes an issue where reflowing could leave the active cursor
  attached to a clipped trailing blank cell instead of following the
  current write position.
  ```
- [`366c348`](https://github.com/ghostty-org/ghostty/commit/366c34831a39651b196f216f1e9fd651568b60b8) macOS: fix first responder after dragging a non-focused surface ([@bo2themax](https://github.com/bo2themax))
  ```text
  This fixes a bug: after dragging a non-focused surface from window A to window B **quickly without making B the key window**, the focused surface in window A is not receiving `keyDown` events.
  ```
- [`2c6dd59`](https://github.com/ghostty-org/ghostty/commit/2c6dd5940688643604f82cd50fd426a463e78d56) macOS: fix render_thread "stuck" after dragging surface to another tab within the same window ([@bo2themax](https://github.com/bo2themax))
  ```text
  The reason the thread is stuck is because the surface's occlusion state is set to invisible after target tab's activate while dragging, since the dragged surface is still in previous tree before dropping, and after dropping the occlusion state of this surface is not updated to visible, which causing the surface is accepting input but not rendering.
  ```
- [`0226bcf`](https://github.com/ghostty-org/ghostty/commit/0226bcf034a0ba040ae4178336144f9df80e4c6e) macOS: update window appearance for About and ConfigurationErrors ([@bo2themax](https://github.com/bo2themax))
- [`59eece9`](https://github.com/ghostty-org/ghostty/commit/59eece9a8edebf29f59d7d1b627cbc97c1363924) feat: use find pasteboard to store search needle ([@nolinmcfarland](https://github.com/nolinmcfarland))
- [`8fa42c6`](https://github.com/ghostty-org/ghostty/commit/8fa42c6ec0b2be97148ec7e90c00e3cc58d5c589) feat: add search state unit tests ([@nolinmcfarland](https://github.com/nolinmcfarland))
- [`69cab3d`](https://github.com/ghostty-org/ghostty/commit/69cab3d8085d0731574f4498864ced901e55c8b0) feat: select needle when reading from pasteboard ([@nolinmcfarland](https://github.com/nolinmcfarland))
- [`ed52160`](https://github.com/ghostty-org/ghostty/commit/ed521606122cde73f0072abc6a7caa5da7dc4829) feat: support BackportSelectionTextField on iOS 18 ([@nolinmcfarland](https://github.com/nolinmcfarland))
- [`bf716a0`](https://github.com/ghostty-org/ghostty/commit/bf716a0c3940ef9a77a4a5d38581e83c0ad44411) feat: add extension to normalize OSPasteboard string interface ([@nolinmcfarland](https://github.com/nolinmcfarland))
- [`7f5c233`](https://github.com/ghostty-org/ghostty/commit/7f5c233492c40e26d6e58e25b4ad07617e728ea4) macOS: add `windowCanBeClosedWithoutConfirmation` without any side effects ([@bo2themax](https://github.com/bo2themax))
- [`8f9b86a`](https://github.com/ghostty-org/ghostty/commit/8f9b86afa8d48afe94e2b895c8442f670c4a0b9b) macOS: add confirmCloseAsync to return the actual response ([@bo2themax](https://github.com/bo2themax))
- [`00a9897`](https://github.com/ghostty-org/ghostty/commit/00a989774e23d4c6035f5565a167be63e22c788d) macOS: add review windows when quitting ([@bo2themax](https://github.com/bo2themax))
  ```text
  Inspired by Terminal.app
  ```
- [`88d30bb`](https://github.com/ghostty-org/ghostty/commit/88d30bb30a02459a97e49fbb0817748422d6f65a) gtk: wire occlusionCallback to GLArea map/unmap ([@mjbommar](https://github.com/mjbommar))
  ```text
  Calls core_surface.occlusionCallback(visible) from the existing
  glareaMap/glareaUnmap handlers (added in #12698) so the renderer
  thread learns when a surface is off-screen.
  ```
- [`14d9e60`](https://github.com/ghostty-org/ghostty/commit/14d9e600acf274f9b04da0dd2695d092aa93c3b6) renderer: skip updateFrame when surface is not visible ([@mjbommar](https://github.com/mjbommar))
  ```text
  renderCallback early-returns while !flags.visible to avoid the
  cell rebuild for hidden surfaces (tab switch, minimize, etc.).
  The .visible → true mailbox handler now runs updateFrame before
  drawFrame so the first frame after re-show isn't stale.
  ```
- [`ec15d0e`](https://github.com/ghostty-org/ghostty/commit/ec15d0e7db3d8079f0e109d0abc9323b750646ba) gtk: wire up occlusionCallback for non-focused tabs ([#12760](https://github.com/ghostty-org/ghostty/issues/12760)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  As discussed in #12745, there has been an outstanding plan to make
  rendering behavior for non-focused surfaces consistent across platforms.
  This PR does that for Linux/GTK using the same patterns as OSX.
  
  The change in `src/apprt/gtk/class/surface.zig` piggybacks on the
  existing `glareaMap` / `glareaUnmap` callbacks (added by `e59e27f8b`) by
  also calling a new `updateOcclusion(bool)` helper. If you don't like the
  helper, or want the helper lifted up further and used on other paths,
  let me know and I can revise.
  
  The changes in `src/renderer/Thread.zig` bail on `renderCallback` when
  not visible and then block on `drainMailbox` to complete the "catch up"
  before trying to draw again.
  
  I want to note that this is more granular than the original #1512, which
  was just focused on the top level window state. I can look at that as
  well if you want, but given the complexity around how
  `XDG_TOPLEVEL_STATE_SUSPENDED` event is fired, I would want to make sure
  we discussed things like transparency and single-instance properly first
  (e.g., do we render when behind another transparent window).
  
  ## Testing
  
  Here's a summary of what I tested:
  
  Tested on Linux/GTK (Ubuntu 26.04, GTK 4.22.2, libadwaita 1.9.0,
  Wayland), built `ReleaseFast`. The patched binary has been daily-driven
  for ~24 hours as my primary terminal.
  
  | Test | Workload | Result |
  |---|---|---|
  | Daily drive | byobu × multiple SSH sessions, Claude Code and Codex
  producing sustained streaming output, `top` / `btop` redrawing on 1 s
  intervals, frequent tab switching | No observed issues over ~24 hours of
  mixed use |
  | Bell on hidden tab | `sleep 5 && printf '\a'` in background tab | Bell
  + needs-attention indicator both fire; confirms IO-thread → GTK-signal
  path is untouched |
  | Search highlight survives hide/show | Open search w/ matches
  highlighted in tab B → switch to tab A for ~10 s → switch back |
  Highlights restored instantly with no stale state; confirms
  deferred-replay path (`updateFrame` on `.visible → true`) works
  correctly |
  | Selection persistence | Select text in tab B → switch tabs → switch
  back | Selection preserved exactly |
  | Lifecycle (close-all) | Opened 8 surfaces, closed them one at a time,
  then process exit + systemd restart | Zero `glib-CRITICAL`, zero `error
  in occlusion callback ...` warnings, clean teardown per `journalctl
  --user -u app-com.mitchellh.ghostty` |
  | Per-thread CPU during workload | `pidstat -t -p <pid>` 30 s with 1
  byobu surface focused, 1 background | Hidden surface's renderer thread
  sits at 0.00 % every sample; focused surface's renderer shows ~1 % blips
  on byobu status ticks |
  
  
  
  ## AI usage
  
  Claude Code (Opus 4.7) helped review my patch and monitor / summarize
  the jorunald log and pidstat entries.
  ```
- [`52f23fb`](https://github.com/ghostty-org/ghostty/commit/52f23fb4190d7f1830635c4171e33f3f394d3919) macOS: review windows when quitting ([#12742](https://github.com/ghostty-org/ghostty/issues/12742)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Inspired by `Terminal.app` which I think is a nice feature.
  
  First two commits contains some changes in `BaseTerminalController` so
  that I can use swift concurrency to review those windows in chain more
  easily.
  
  
  
  https://github.com/user-attachments/assets/41d92432-4ae0-499e-961a-fc247602f3d7
  
  
  Works with tabs as well, i forgot to record that.
  ```
- [`afe4819`](https://github.com/ghostty-org/ghostty/commit/afe4819920036d2d85edc75ccf757404f45632f0) macOS: Re-enable global keybinds after event tap disable events ([#12714](https://github.com/ghostty-org/ghostty/issues/12714)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  While testing https://github.com/ghostty-org/ghostty/pull/9857, I
  encountered the behavior mentioned below. It's pretty frustrating to
  encounter, so I've been actually compiling this fix into my test builds
  for last month or so, and the issue has not come back. I exclusively use
  the QuickTerminal, so my workflow depends on global keybinds working
  reliably.
  
  Issue: https://github.com/ghostty-org/ghostty/issues/12294
  
  The solution includes listening to two events that are fired when a tap
  is disabled:
  - tapDisabledByTimeout
  - tapDisabledByUserInput
  
  When these are fired, we re-enable the tap.
  
  Apple's Docs:
  https://developer.apple.com/documentation/coregraphics/cgeventtype?language=swift
  
  Related Discussions:
  - https://github.com/ghostty-org/ghostty/discussions/11819
  - https://github.com/ghostty-org/ghostty/discussions/12091
  ```
- [`7e24f0e`](https://github.com/ghostty-org/ghostty/commit/7e24f0e0bc771d48c8a3db49bc18425318c0794e) macOS: use find pasteboard for search needle ([#12712](https://github.com/ghostty-org/ghostty/issues/12712)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes the issue described in #12516.
  
  ### What
  - Inject an `OSPasteboard` into `SearchState`
  - Add `OSPasteboard` extension to normalize working with strings between
  UIPasteboard/NSPasteboard
  - Add `BackportSelectionTextField` which supports text selection for
  MacOS 15/iOS 18 and up.
  - Read from the pasteboard when the overlay opens and when the app
  becomes active
  - Write to the pasteboard when the search needle changes
  - Annotate `SearchState` as MainActor. `NSPasteboard` isn't thread safe,
  and since `SearchState` is already accessed from the main thread,
  MainActor enforces our writes be thread safe
  - Add SearchState unit tests
  
  ### Why
  Consistent with other macOS apps, the Find bar's search needle should
  persist when re-opened and should sync to the Find bar in other apps.
  For example, see Xcode, Notes, Terminal, and Safari.
  
  
  https://github.com/user-attachments/assets/b6a55a4a-a52c-45bc-ac38-c9df452c11cb
  ```
- [`b78174a`](https://github.com/ghostty-org/ghostty/commit/b78174a68f6a97c487fe5ee4e0c155433f4a03d9) macOS: update window appearance for About and ConfigurationErrors ([#12601](https://github.com/ghostty-org/ghostty/issues/12601)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  <img width="1224" height="696" alt="Xnip2026-05-06_19-13-31"
  src="https://github.com/user-attachments/assets/ab090dc0-7c06-4a01-8e7c-5d48ca6ccca3"
  />
  ```
- [`24d664f`](https://github.com/ghostty-org/ghostty/commit/24d664f0ba1074c4c1047da7a239bd1cf6bdf7af) fix: apply variation selectors to preceding codepoint ([#12596](https://github.com/ghostty-org/ghostty/issues/12596)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This fixes a bug where the variation selectors (VS15 & VS16) were
  checked against the first codepoint in a cell instead of the previous
  codepoint in the cell's grapheme cluster, causing them to be dropped if
  that first codepoint was not a valid base.
  ```
- [`a03b52e`](https://github.com/ghostty-org/ghostty/commit/a03b52e18b26048dbd71c08764cb011044edfd3a) fix: preserve active cursor position during reflow ([#12598](https://github.com/ghostty-org/ghostty/issues/12598)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This PR fixes an issue where reflowing could leave the active cursor
  attached to a clipped trailing blank cell instead of following the
  current write position.
  ```
- [`f5aa271`](https://github.com/ghostty-org/ghostty/commit/f5aa271d07f97f68886153f2d741f50ec060ba9b) cli: add an ssh-wrapping +ssh action ([#12582](https://github.com/ghostty-org/ghostty/issues/12582)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a drop-in `ssh` wrapper that sets up the remote environment for
  Ghostty. Anything not consumed as one of our own flags is forwarded to
  the real, wrapped `ssh` binary. It can be used directly (`ghostty +ssh
  user@host`), aliased (`alias ssh='ghostty +ssh --'`), or invoked through
  Ghostty's shell integration.
  
  Before exec'ing ssh, `+ssh`:
  
  - Forwards Ghostty environment to the remote (`--forward-env`): sets
  TERM=xterm-256color and requests SendEnv forwarding of COLORTERM,
  TERM_PROGRAM, and TERM_PROGRAM_VERSION.
  - Installs Ghostty's terminfo on the remote (`--terminfo`), informed by
  our existing `ssh-cache` system and using our internal xterm-ghostty
  terminfo representation.
  
  A third flag, `--cache`, controls cache use; `--cache=false` bypasses
  both read and write, which is useful for scripting and for debugging
  install failures without polluting the cache.
  
  For shell integration, this replaces the per-shell logic (which made up
  roughly a third of our shell integration scripts) with a simple wrapper
  function that translates GHOSTTY_SHELL_FEATURES into a `ghostty +ssh`
  command line.
  ```
- [`3e3705b`](https://github.com/ghostty-org/ghostty/commit/3e3705b93233480f18274620f5e57c1c7021bf85) macOS: fix surface focus/render state after dragging in to to another window/tab ([#12338](https://github.com/ghostty-org/ghostty/issues/12338)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes 2 bugs
  
  1. After dragging a non-focused surface from window A to window B
  **quickly without making B the key window**, the focused surface in
  window A is not receiving `keyDown` events.
  
  
  https://github.com/user-attachments/assets/a8861c0a-9300-470d-bf7e-0f32a9ab2cd1
  
  2. #12343 After dragging a surface from tab A to tab B within the same
  window, the dragged surface is not rendering input correctly.
  > The reason the thread is stuck is because the surface's occlusion
  state is set to invisible after target tab's activate while dragging,
  since the dragged surface is still in previous tree before dropping, and
  after dropping the occlusion state of this surface is not updated to
  visible, which causing the surface is accepting input but not rendering.
  
  
  
  https://github.com/user-attachments/assets/d67f5dba-8609-4f67-a956-921982faf796
  ```
- [`cb79efa`](https://github.com/ghostty-org/ghostty/commit/cb79efa779ce05535797ff191bd0b7ce06b2ea77) build(deps): bump docker/build-push-action from 7.1.0 to 7.2.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [docker/build-push-action](https://github.com/docker/build-push-action) from 7.1.0 to 7.2.0.
  - [Release notes](https://github.com/docker/build-push-action/releases)
  - [Commits](https://github.com/docker/build-push-action/compare/bcafcacb16a39f128d818304e6c9c0c18556b85f...f9f3042f7e2789586610d6e8b85c8f03e5195baf)
  
  ---
  updated-dependencies:
  - dependency-name: docker/build-push-action
    dependency-version: 7.2.0
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`10c6121`](https://github.com/ghostty-org/ghostty/commit/10c6121458c8a03e7b7804c00291292d7a811ecf) build(deps): bump docker/build-push-action from 7.1.0 to 7.2.0 ([#12765](https://github.com/ghostty-org/ghostty/issues/12765)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [docker/build-push-action](https://github.com/docker/build-push-action)
  from 7.1.0 to 7.2.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/docker/build-push-action/releases">docker/build-push-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v7.2.0</h2>
  <ul>
  <li>Bump <code>@​actions/core</code> from 3.0.0 to 3.0.1 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1525">docker/build-push-action#1525</a></li>
  <li>Bump <code>@​docker/actions-toolkit</code> from 0.87.0 to 0.90.0 in
  <a
  href="https://redirect.github.com/docker/build-push-action/pull/1517">docker/build-push-action#1517</a></li>
  <li>Bump brace-expansion from 2.0.2 to 5.0.6 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1534">docker/build-push-action#1534</a></li>
  <li>Bump fast-xml-builder from 1.1.4 to 1.2.0 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1529">docker/build-push-action#1529</a></li>
  <li>Bump fast-xml-parser from 5.5.7 to 5.8.0 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1521">docker/build-push-action#1521</a></li>
  <li>Bump postcss from 8.5.6 to 8.5.10 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1526">docker/build-push-action#1526</a></li>
  <li>Bump tar from 6.2.1 to 7.5.15 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1533">docker/build-push-action#1533</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/docker/build-push-action/compare/v7.1.0...v7.2.0">https://github.com/docker/build-push-action/compare/v7.1.0...v7.2.0</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/docker/build-push-action/commit/f9f3042f7e2789586610d6e8b85c8f03e5195baf"><code>f9f3042</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1517">#1517</a>
  from docker/dependabot/npm_and_yarn/docker/actions-t...</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/812d5fd9212a4c5d419e5be02fd8e9bb435c5d76"><code>812d5fd</code></a>
  chore: update generated content</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/b6f66930769f2917a3275dc4d81f15583ac7e105"><code>b6f6693</code></a>
  chore(deps): Bump <code>@​docker/actions-toolkit</code> from 0.87.0 to
  0.90.0</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/c1c626eced73a500ec65c4256c620b3b9e8278c0"><code>c1c626e</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1525">#1525</a>
  from docker/dependabot/npm_and_yarn/actions/core-3.0.1</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/51bb284cd4d05650aa6f5e4e22cb96d2cbfe62b7"><code>51bb284</code></a>
  chore: update generated content</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/5f7884def8f133e8ef40c53d003d1471c05621c6"><code>5f7884d</code></a>
  chore(deps): Bump <code>@​actions/core</code> from 3.0.0 to 3.0.1</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/e01deff7d956c756a20f3e19ff7ddc0e4a50fc1d"><code>e01deff</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1521">#1521</a>
  from docker/dependabot/npm_and_yarn/fast-xml-parser-...</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/3804d497934b39bd591ee9d1c6c9e593b4488a67"><code>3804d49</code></a>
  chore: update generated content</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/71e8947aac5dad23ce83a43e9c98f750e02de2f3"><code>71e8947</code></a>
  chore(deps): Bump fast-xml-parser from 5.5.7 to 5.8.0</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/4925ad24cdbc42ff492d76cf9fe7a30b79976b60"><code>4925ad2</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1526">#1526</a>
  from docker/dependabot/npm_and_yarn/postcss-8.5.10</li>
  <li>Additional commits viewable in <a
  href="https://github.com/docker/build-push-action/compare/bcafcacb16a39f128d818304e6c9c0c18556b85f...f9f3042f7e2789586610d6e8b85c8f03e5195baf">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=docker/build-push-action&package-manager=github_actions&previous-version=7.1.0&new-version=7.2.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## May 20, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26177391439), [2](https://github.com/ghostty-org/ghostty/actions/runs/26172134530), [3](https://github.com/ghostty-org/ghostty/actions/runs/26165647879), [4](https://github.com/ghostty-org/ghostty/actions/runs/26139523610)  
Summary: 4 runs • 7 commits • 6 authors

### Changes

- [`4f94afd`](https://github.com/ghostty-org/ghostty/commit/4f94afdb4b25b52583eef6c03217b8bb561c9ad6) vouch: enable auto-locking closed issues ([@trag1c](https://github.com/trag1c))
- [`46d54ed`](https://github.com/ghostty-org/ghostty/commit/46d54ed673a004df09078bee56e809421a82370e) vouch: enable auto-locking closed issues ([#12752](https://github.com/ghostty-org/ghostty/issues/12752)) ([@mitchellh](https://github.com/mitchellh))
- [`41878d6`](https://github.com/ghostty-org/ghostty/commit/41878d6f7977d4758ea15b6599ee7d025be40ecc) snap: export TERMINFO_DIRS so child shells find xterm-ghostty ([@aaron-ang](https://github.com/aaron-ang))
  ```text
  Without this, shells spawned by ghostty cannot find the xterm-ghostty
  terminfo entry because ncurses only searches standard system paths.
  The snap's terminfo lives inside the snap sandbox and is inaccessible
  unless TERMINFO_DIRS is set explicitly.
  ```
- [`2559654`](https://github.com/ghostty-org/ghostty/commit/25596541ec42f08d2a98ac54337b81a6244a5328) snap: export TERMINFO_DIRS so child shells find xterm-ghostty ([#12662](https://github.com/ghostty-org/ghostty/issues/12662)) ([@kenvandine](https://github.com/kenvandine))
  ````text
  ## Summary
  
  When Ghostty is installed via snap on Ubuntu, programs running inside
  Ghostty (e.g. `clear`) fail with:
  
  ```
  terminals database is inaccessible
  ```
  
  The snap ships terminfo at `${SNAP}/share/terminfo` but the launcher
  never exports `TERMINFO_DIRS`, so ncurses in child shells falls back to
  the host's system database. On Ubuntu 24.04 (ncurses 6.4) the system
  database predates the `xterm-ghostty` entry, so the lookup fails.
  
  This is the same fix as the auto-closed #12303 and resolves #12304.
  
  ## Fix
  
  Export `TERMINFO_DIRS` in `snap/local/launcher` so all child processes
  can resolve the bundled entry without manual setup.
  
  ## Local build (how this PR was verified)
  
  Remix the installed store snap by swapping `app/launcher` with the
  patched one:
  
  ```sh
  sudo unsquashfs -d /tmp/g \
    /var/lib/snapd/snaps/ghostty_$(readlink /snap/ghostty/current).snap
  sudo cp snap/local/launcher /tmp/g/app/launcher
  sudo mksquashfs /tmp/g /tmp/ghostty-test.snap -comp xz -noappend
  sudo snap install --dangerous --classic /tmp/ghostty-test.snap
  ```
  
  Then launch `/snap/bin/ghostty` and run `clear`.
  
  ## Test plan
  
  Verified locally on Ubuntu 24.04 / arm64.
  
  - [x] In default `zsh` / `bash` inside Ghostty, `clear` succeeds.
  - [x] `infocmp xterm-ghostty` resolves to
  `/snap/ghostty/current/share/terminfo/x/xterm-ghostty`.
  - [x] No manual copying of terminfo entries into `~/.terminfo/`
  required.
  
  ## AI Disclosure
  
  Claude Code was used to investigate the root cause and to draft this
  single-line launcher change. The fix is identical to the proposal in the
  linked discussion (#12304). I manually verified by remixing the
  installed snap with the patched launcher and confirming `clear` and
  `infocmp xterm-ghostty` work without manually copying terminfo entries
  into `~/.terminfo/` (original workaround shared in the discussion).
  ````
- [`7c2b29a`](https://github.com/ghostty-org/ghostty/commit/7c2b29a9f3047b2f73d632546c51cfbe52fd6a7b) build(highway): require `apple_sdk` for darwin builds ([@elias8](https://github.com/elias8))
- [`8644415`](https://github.com/ghostty-org/ghostty/commit/86444156b403e7dd79ea7f0b2854be76927875b1) build(highway): require `apple_sdk` for darwin builds ([#12725](https://github.com/ghostty-org/ghostty/issues/12725)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Noticed this was removed in another PR, but `apple_sdk` is required to
  build libghsotty for the iOS simulator, specifically for the x86 version
  (see the error log
  [here](https://github.com/elias8/libghostty/actions/runs/26075576793/job/76666498246)).
  Figured it'd be better to include the SDK in all darwin builds for
  consistency.
  ```
- [`19e20f7`](https://github.com/ghostty-org/ghostty/commit/19e20f7664dc7a755d2d7a16ab545b2503f26caf) Update VOUCHED list ([#12746](https://github.com/ghostty-org/ghostty/issues/12746)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12745#discussioncomment-16984203)
  from @jcollie.
  
  Vouch: @mjbommar
  ```

## May 19, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26123808733), [2](https://github.com/ghostty-org/ghostty/actions/runs/26110763000)  
Summary: 2 runs • 6 commits • 3 authors

### Changes

- [`9bcb30a`](https://github.com/ghostty-org/ghostty/commit/9bcb30aa119b20833d74d4e32104dafe20bd8203) Update VOUCHED list ([#12744](https://github.com/ghostty-org/ghostty/issues/12744)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12743#discussioncomment-16981434)
  from @bo2themax.
  
  Vouch: @b0uks
  ```
- [`aed6461`](https://github.com/ghostty-org/ghostty/commit/aed646139d2a8571c4d4048158e6a6f0c8b353e0) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`fdf84ef`](https://github.com/ghostty-org/ghostty/commit/fdf84ef7ce611b4374d5cef3e213f155fae26914) macOS: check the resource the URL refers to. ([@bo2themax](https://github.com/bo2themax))
  ```text
  Fixes #12727. [`NSURL.hasDirectoryPath` doesn't do this](https://developer.apple.com/documentation/foundation/nsurl/hasdirectorypath).
  
  We don't need to check this in NewTerminalIntent since AppIntent already appends `/` to the directory.
  ```
- [`3ac7562`](https://github.com/ghostty-org/ghostty/commit/3ac75627910232ac761e8e932a2850123243d5a3) macOS: set error when there is no directory to open with ([@bo2themax](https://github.com/bo2themax))
- [`5f2f08e`](https://github.com/ghostty-org/ghostty/commit/5f2f08ebda33bf7e1f9f0b80c2c5845b39357f76) macOS: check the resource the URL refers to ([#12731](https://github.com/ghostty-org/ghostty/issues/12731)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  - Fixes https://github.com/ghostty-org/ghostty/issues/12727.
  [`NSURL.hasDirectoryPath` doesn't do
  this](https://developer.apple.com/documentation/foundation/nsurl/hasdirectorypath).
  
  <img width="977" height="177" alt="image"
  src="https://github.com/user-attachments/assets/94f77277-8ef0-4573-8ae1-0e54f810463f"
  />
  
  > We don't need to check this in NewTerminalIntent since AppIntent
  already appends `/` to the directory.
  
  - Set error when there is no directory to open with
  ```
- [`8150b5b`](https://github.com/ghostty-org/ghostty/commit/8150b5b772343887c76d1a50e79cd844d9d4d5c0) Update iTerm2 colorschemes ([#12711](https://github.com/ghostty-org/ghostty/issues/12711)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260511-160054-2671288
  ```

## May 18, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26055045190), [2](https://github.com/ghostty-org/ghostty/actions/runs/26010120405), [3](https://github.com/ghostty-org/ghostty/actions/runs/26009059850)  
Summary: 3 runs • 11 commits • 4 authors

### Changes

- [`3706aba`](https://github.com/ghostty-org/ghostty/commit/3706abab0c962d9c93c4c4af853149f9d55f4deb) Update VOUCHED list ([#12733](https://github.com/ghostty-org/ghostty/issues/12733)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12732#discussioncomment-16966426)
  from @jcollie.
  
  Vouch: @rewdy
  ```
- [`81af657`](https://github.com/ghostty-org/ghostty/commit/81af65766f319a954a26196b4812d159496d4f00) feat: add +toggle-quick-terminal IPC command ([@huajiang-tubi](https://github.com/huajiang-tubi))
  ```text
  Expose toggle-quick-terminal as a proper IPC action so it can be
  triggered via 'ghostty +toggle-quick-terminal' from the command line,
  instead of calling the raw D-Bus org.gtk.Actions.Activate interface.
  
  This follows the same pattern as the existing +new-window IPC command:
  
    - Add toggle_quick_terminal to apprt.ipc.Action enum (Zig + C ABI)
    - Create apprt/gtk/ipc/toggle_quick_terminal.zig (GTK D-Bus handler)
    - Route .toggle_quick_terminal in apprt/gtk/App.zig performIpc
    - Register toggle-quick-terminal GAction in application.zig
    - Add +toggle-quick-terminal CLI handler in cli/
    - Register in cli/ghostty.zig Action enum, runMain, and options
    - Add stub in apprt/embedded.zig
    - Update include/ghostty.h C header enum
  
  Usage:
    ghostty +toggle-quick-terminal
  
  Closes: #12618
  ```
- [`22b9df2`](https://github.com/ghostty-org/ghostty/commit/22b9df25e65a37292e2cf91750947d73fc669b64) Fix "Available since" ([@jcollie](https://github.com/jcollie))
- [`4b7bf0b`](https://github.com/ghostty-org/ghostty/commit/4b7bf0b20e3baf9c1ba10c63f2ad1fd853faea8f) IPC: add +toggle-quick-terminal command ([#12661](https://github.com/ghostty-org/ghostty/issues/12661)) ([@jcollie](https://github.com/jcollie))
  ```text
  Add `+toggle-quick-terminal` as a first-class IPC action, following the
  same pattern as `+new-window`. This provides a proper CLI command
  (`ghostty +toggle-quick-terminal`) to toggle the quick terminal on a
  running Ghostty instance.
  
  Closes discussion #12618
  ```
- [`57a9adc`](https://github.com/ghostty-org/ghostty/commit/57a9adce7164b7491bf333be2ee7b336c2b8f045) fix datastruct/SplitTree not calculating the correct new split ratio when resizing a split ([@dkinzler](https://github.com/dkinzler))
- [`e59e27f`](https://github.com/ghostty-org/ghostty/commit/e59e27f8bd7610f82ca66c3f0971e6e88713e06c) Fix nested splits disappearing and focus being lost. ([@dkinzler](https://github.com/dkinzler))
  ```text
  The cause of these bugs is that GTK can initially allocate
  a split/surface a width/height of 0 which causes it to
  get unmapped and lose focus. Additionally the split ratio is
  only set once but not accurately for tiny splits, which can keep
  a surface invisible even when the split gets resized later.
  
  To fix these problems the split ratio is always checked and
  possibly corrected when a split gets resized. Changes in a split
  ratio caused by the user dragging the divider are detected
  separately using an event controller. If a surface loses focus
  we restore it once the surface becomes mapped again.
  ```
- [`54a38e8`](https://github.com/ghostty-org/ghostty/commit/54a38e8134b8418d1d8d5293c2881b48a7274689) Distinguish resize and manual update using a combination of ([@dkinzler](https://github.com/dkinzler))
  ```text
  max-position and position properties. Listening to drag events directly
  did not work that well.
  ```
- [`93d1142`](https://github.com/ghostty-org/ghostty/commit/93d1142ada9336c3e33e23bd6343aa1366265bbd) small formatting changes ([@dkinzler](https://github.com/dkinzler))
- [`9f72eb9`](https://github.com/ghostty-org/ghostty/commit/9f72eb9d7ca05fb1e7dfd1f9eb0395ed77205d13) added back accidentally deleted empty line ([@dkinzler](https://github.com/dkinzler))
- [`4814aee`](https://github.com/ghostty-org/ghostty/commit/4814aee44e40ab6e1cb0a06c4cd5f650b6fac209) gtk: fix invisible splits and focus being lost ([#12698](https://github.com/ghostty-org/ghostty/issues/12698)) ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes #11193 where terminal surfaces might not appear and focus might be
  lost when creating multiple nested splits.
  
  These bugs are caused by GTK initially allocating a tiny width/height to
  deeply nested splits. For a split with a tiny size, the split ratio will
  be set inaccurately e.g. to 1 which means that the right/bottom child of
  the split is invisible. If that child is the terminal surface that
  should have the focus, it will lose it. In the current implementation
  the split ratio can be set at most once, which means the inaccurate
  ratio never gets corrected and a surface (or an entire sub-tree of the
  layout) will stay invisible.
  
  The following explains the current implementation and bug in more
  detail, it is a bit long, but I hope it will make it easier to review
  this PR.
  
  ### Current Implementation
  
  A split layout is a tree, in code represented by `datastruct/SplitTree`,
  where inner nodes are splits and leafs are terminal surface. A split can
  be either horizontal or vertical, and has a ratio that defines how its
  space should be divided among the 2 children.
  The counterpart in the GTK UI is the `apprt/gtk/class/SplitTree` widget
  whose `onRebuild/buildTree` functions build a widget tree that has the
  same structure as the `datastruct/SplitTree`. The widget tree consists
  of a `SplitTreeSplit` widget for every split and a `Surface` widget for
  every terminal surface.
  
  A `SplitTreeSplit` widget wraps a `gtk.Paned` widget, which displays its
  two children with a divider in between, either horizontally or
  vertically. How much space each child gets is determined by 3
  properties. `min_position` is always 0 in our case, `max_position`
  corresponds to the width/height (for horizontal/vertical splits) of the
  widget and `position` is where the divider should be. So `position` is
  equivalent to the width/height of the left/top child and thereby also
  determines the width/height of the right/bottom child. `SplitTreeSplit`
  listens for changes in the 3 properties. If there is one, the
  `propPosition`, `propMinPosition` or `propMaxPosition` function gets
  triggered and an idle callback for the `onIdle` function is added.
  
  We need to make sure that the widget tree and the `datastruct/SplitTree`
  stay in sync.
  
  If we e.g. create a new split or close a surface, the structure of the
  split tree changes. In that case `gtk/class/SplitTree.onRebuild` will
  completely rebuild the widget tree (the `Surface` widgets are actually
  reused) to match the new tree structure. If we resize a split (i.e.
  change the split ratio) via action/keybind, we also completely rebuild
  the widget tree.
  
  Additionally we need to make sure that for every
  `SplitTreeSplit/gtk.Paned` the `position` divided by `max_position`
  matches the ratio of the corresponding split node in our
  `datastruct/SplitTree`. There are two ways the current implementation
  keeps these ratios in sync, both are handled by the
  `SplitTreeSplit.onIdle` function.
  1. Initially when the widget tree is built, GTK allocates each widget a
  size. Specifically it also sets the `position` and `max_position`
  properties of each `gtk.Paned` widget, which will trigger the
  `SplitTreeSplit.onIdle` function to run. GTK will not necessarily set
  position correctly, it is the task of `onIdle` to make sure that the UI
  matches the layout defined by the `datastruct/SplitTree`. `onIdle`
  checks if `position/max_position` matches the ratio that the split
  should have and if not calls `gtk.Paned.setPosition` to update it. This
  can only happen once for each split since `onIdle` checks if the
  position was set previously. The idea is that we should only ever need
  to set the position once, because `gtk.Paned` will automatically keep
  its current ratio whenever its size/`max-position` changes (if the
  `setPosition` function has been called before). A size change can happen
  e.g. because the entire window was resized or because an ancestor split
  changed its split ratio.
  2. The user can manually change the ratio between the two children of a
  split by dragging the divider between them in the UI. When that happens
  the `position` property in `gtk.Paned` changes and eventually the
  `SplitTreeSplit.onIdle` function gets called. Since `setPosition` should
  have already been called when the widget was initially sized, we should
  fall through to the second case and write the current ratio back to the
  `datastructure/SplitTree`.
  
  The problem with `SplitTreeSplit.onIdle` is that sometimes the split
  ratio cannot be set accurately given the current size of the `gtk.Paned`
  widget. Because `onIdle` can only set the position/ratio once, any
  previous inaccuracy can never get corrected.
  
  For example with many nested vertical splits, GTK might initially
  allocate a `gtk.Paned` widget a height of 1. It will have
  `max_position=1` and `position=1`. When `onIdle` runs the current ratio
  of `position/max_position = 1` is different from the desired ratio of
  e.g. 0.5. But a ratio of 0.5 cannot be set, the position can only be 0
  or 1 corresponding to a ratio of 0 or 1. The position will then get set
  as 1 and can't be changed later. Even when the split later gets a larger
  height, it will keep the ratio of 1 and the bottom child will stay
  invisible. When the surface that should be focused initially becomes
  invisible it loses focus and the focus will never be restored. That is
  exactly what happens in the first screencast in the issue description
  (#11193).
  
  Another problem with `onIdle` is that the `setPosition` call in `onIdle`
  will trigger another idle callback where the position change is
  sometimes wrongly interpreted as a manual update and written back to the
  tree. Also sometimes the initial ratio in a `gtk.Paned` can already be
  correct, in which case position will not get set. The next manual
  position update is then not detected as a manual update.
  
  ### Changes
  
  `SplitTreeSplit.onIdle` is now able to set the split position every time
  the widget is resized, an inaccurate initial ratio will be corrected. To
  be able to distinguish a widget resize from a manual position update by
  the user, we keep track of whether `max-position`, `position` or both
  properties changed. If only `max-position` or both properties changed,
  then the widget was resized. If just `position` changed it is a manual
  update. This is kind of hacky but works. To verify I checked the source
  code for `gtk.Paned`, see the comment in the code on `onIdle`.
  
  `SplitTreeSplit` no longer listens to changes in `min-position`, that
  should always be 0 (because we use the default resize/shrink properties
  for `gtk.Paned`) and there is already an assert in `onIdle` that checks
  that.
  
  It can still happen that a surface initially gets allocated width/height
  0 and loses focus. The only reliable way to detect when we can restore
  focus, is to listen to the `map/unmap` signals exposed by `gtk.Widget`.
  The `Surface` widget now listens to these signals on its `GlArea` child
  (because that is where we want to put focus) and stores the current
  state in the new `mapped` property. The `SplitTree` widget listens to
  changes in that property: when surfaces become mapped, an idle callback
  for the new `onRestoreFocus` function is added, which will check whether
  the last focused surface is mapped and if so restore focus to it.
  
  ### Other possible solutions
  
  Alternatively we could try to only set the split ratio once the split
  has its correct final size, but I think it's hard to detect that
  reliably. Or we could try to prevent the splits/surfaces from becoming
  invisible in the first place by e.g. setting a minimal widget size. But
  then you won't get the exactly correct layout and sometimes you do want
  a surface to be tiny or invisible e.g. you can drag the divider in a
  split all the way to one side.
  
  The ideal solution would probably be to write a custom version of
  `gtk.Paned` where you can provide the desired ratio on widget creation.
  Then everything will be sized correctly from the start, focus will not
  be lost. In terms of performance it would probably be better as well,
  because right now there can be multiple rounds of resizes until every
  split/surface has its correct size. I have played around with this a
  bit, it is definitely possible. But you would have to implement the
  divider widget, logic for layouting, handling gestures and co. That is a
  bigger undertaking.
  
  ### Testing
  
  Tested by creating/modifying deeply nested layouts, dragging split
  dividers and resizing splits via keybind. Checked that ratios are
  maintained when the window is resized and tested that it works with
  zoom. Tested locally with hyprland and in a VM with KDE.
  
  All the bugs described in the issue should be fixed.
  
  ### AI Disclosure
  
  Discovered the bug and wrote all code/comments by myself. Used AI in
  researching various internals of GTK.
  ```
- [`cfac861`](https://github.com/ghostty-org/ghostty/commit/cfac86179436a42747812ae8e9075dea4df8f062) split_tree: rescale split ratio when resizing ([#12699](https://github.com/ghostty-org/ghostty/issues/12699)) ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes `SplitTree.resize` not rescaling the split ratio to be relative to
  the size of the split. Added a unit test for resizing a nested split.
  
  Previously the new ratio was incorrectly calculated relative to the
  entire grid. As a consequence resizing a nested split in the GTK app
  would cause unexpected size changes like large jumps. E.g. in the
  following recording the window has height ~1000px and the resize was
  done using a keybind for `resize_split:up,10`. The change is much larger
  than 10 pixels.
  
  
  
  https://github.com/user-attachments/assets/ba375ddf-5b2f-45e4-8b12-69021ef2f8a8
  
  
  
  Note that even with this fix, resizing by a small amount like 10 pixels
  might not work at all (depending on window size and layout), because of
  the same bug causing #11193 (see my PR #12698). Initially an inaccurate
  split ratio will be set and eventually written back to the split tree
  datastructure. That incorrect split ratio will be the same before and
  after the small resize, so nothing actually changes in the UI.
  
  The split tree implementation for the macOS app already calculates the
  ratios correctly.
  
  AI Disclosure
  No AI was used, the bug was discovered and all code written by myself.
  ```

