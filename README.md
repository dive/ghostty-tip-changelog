> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: April 30, 2026 at 09:42 UTC.

## April 30, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/25150964925)  
Summary: 1 runs • 1 commits • 1 authors

### Changes

- [`f5664cd`](https://github.com/ghostty-org/ghostty/commit/f5664cd7b0c0c23f35782c9ec5bdb485e0b9510f) Update VOUCHED list ([#12533](https://github.com/ghostty-org/ghostty/issues/12533)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12530#discussioncomment-16765566)
  from @jcollie.
  
  Vouch: @Samasaur1
  ```

## April 27, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/25018134977), [2](https://github.com/ghostty-org/ghostty/actions/runs/25007723053)  
Summary: 2 runs • 24 commits • 9 authors

### Changes

- [`1df7a5d`](https://github.com/ghostty-org/ghostty/commit/1df7a5d3f3a5b77e1a779260c9823c0ec7311f08) macOS: update keybind for end_search ([@bo2themax](https://github.com/bo2themax))
- [`97c5a21`](https://github.com/ghostty-org/ghostty/commit/97c5a21abae800c7cb3e0af3610aa4eb73da47ed) macOS: fix ending search in menu bar does focus on surface ([@bo2themax](https://github.com/bo2themax))
- [`8f3d9b4`](https://github.com/ghostty-org/ghostty/commit/8f3d9b4690979f9d16d1982fa805aadb5c41abb6) update zon2nix to 0.5.0 ([@jcollie](https://github.com/jcollie))
  ```text
  fix hash outputs for flatpak
  build with Zig 0.16 from nixpkgs
  (which required fixing prettier reference in devShell.nix)
  ```
- [`acbaa47`](https://github.com/ghostty-org/ghostty/commit/acbaa47de58fae5f136c9d5e07f92d478ee8b57e) switch back to older nixpkgs ([@jcollie](https://github.com/jcollie))
- [`8925a91`](https://github.com/ghostty-org/ghostty/commit/8925a91c5c0ed75707ad4a1a3a99b6f70933eebc) update zon2nix to 0.5.0 ([#12488](https://github.com/ghostty-org/ghostty/issues/12488)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  fix hash outputs for flatpak
  ```
- [`2cbe706`](https://github.com/ghostty-org/ghostty/commit/2cbe7062768b544a0e32df9cdfb2272f238bc161) macOS: fix keybindings for end_search not working correctly ([#12492](https://github.com/ghostty-org/ghostty/issues/12492)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This now fixes #11410 completely, `navigate_search:next` and
  `navigate_search:previous` are already fixed in
  18f270222557fd46d8c3305da523212445066154.
  
  Also fixes: surface is not focused after ending search via menu bar
  ```
- [`154169b`](https://github.com/ghostty-org/ghostty/commit/154169b054a4bec21127a963d9164b364c518d9c) Fix speedy high-resolution scrolling on Linux ([@rightaditya](https://github.com/rightaditya))
  ```text
  Enforcing an absolute minimum of 1 for scroll events causes differing
  scroll speeds between high-resolution and standard scroll wheels on
  Linux. Since this was added to handle MacOS's precision scrolling
  emulation, this patch alters the behaviour so that the absolute minimum
  is only enforced on MacOS.
  
  Fixes #11648.
  ```
- [`5871a2d`](https://github.com/ghostty-org/ghostty/commit/5871a2d4f079c13c07997ac5b2938aabe053ea55) zig-fmt cleanup ([@rightaditya](https://github.com/rightaditya))
- [`6590196`](https://github.com/ghostty-org/ghostty/commit/6590196661f769dd8f2b3e85d6c98262c4ec5b3b) Fix speedy high-resolution scrolling on Linux ([#12483](https://github.com/ghostty-org/ghostty/issues/12483)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Enforcing an absolute minimum of 1 for scroll events causes differing
  scroll speeds between high-resolution and standard scroll wheels on
  Linux. Since this was added to handle MacOS's precision scrolling
  emulation, this patch alters the behaviour so that the absolute minimum
  is only enforced on MacOS.
  
  NB: This can't just be fixed by adjusting `mouse-scroll-multiplier`
  since that affects *all* scroll events whether they're high-resolution
  or not. Reducing `mouse-scroll-multiplier` to handle high-res scroll
  events better makes scrolling unusably slow for regular scroll wheels
  connected to the same machine.
  
  Fixes #11648.
  ```
- [`2648668`](https://github.com/ghostty-org/ghostty/commit/2648668da9104829ce88451c510e691df25fbf65) fix quick-terminal breaking when it is manually toggled while autohide is enabled ([@dkinzler](https://github.com/dkinzler))
- [`b662588`](https://github.com/ghostty-org/ghostty/commit/b66258806e1a6f9204c322d7bb2dbdb3fc464a17) test: only change themes in theme tests ([@bo2themax](https://github.com/bo2themax))
- [`a7eaecf`](https://github.com/ghostty-org/ghostty/commit/a7eaecf929b9a060962d3491d926f7d6b8fd0c63) test: always use temporary config when running ui tests ([@bo2themax](https://github.com/bo2themax))
- [`df365ba`](https://github.com/ghostty-org/ghostty/commit/df365baf18180577e099c66c23858dab3fd3eeb2) test: add test plan and override default config when running tests ([@bo2themax](https://github.com/bo2themax))
- [`12ac199`](https://github.com/ghostty-org/ghostty/commit/12ac19939c365b3f29660b252ed36028f9a4a7a9) feat: add middle-click action configuration ([@lebdron](https://github.com/lebdron))
- [`ac67a61`](https://github.com/ghostty-org/ghostty/commit/ac67a6160c8169ac3f0d7fddae796338999d113c) renderer: fix preedit range width ([@dobbylee](https://github.com/dobbylee))
- [`8769d32`](https://github.com/ghostty-org/ghostty/commit/8769d322022f135886d4d26d2974fb2dcea40c43) Update VOUCHED list ([#12485](https://github.com/ghostty-org/ghostty/issues/12485)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12484#discussioncomment-16723661)
  from @jcollie.
  
  Vouch: @kylesower
  ```
- [`6c68650`](https://github.com/ghostty-org/ghostty/commit/6c68650920804a202a3208d7d355368c9dd28a46) fix: update Se terminfo entry to reset cursor to configured default ([@kylesower](https://github.com/kylesower))
- [`9717530`](https://github.com/ghostty-org/ghostty/commit/971753074bd3bd79ff208232f3165e74e1e6f5fb) input: remove translated in capi ([@bo2themax](https://github.com/bo2themax))
  ```text
  Follow up for a3462dd2bd541af6372855917c6ccb5643aeda93
  ```
- [`5031973`](https://github.com/ghostty-org/ghostty/commit/503197362366f5ab52a557a08670974b53c1e499) input: remove translated in capi ([#12490](https://github.com/ghostty-org/ghostty/issues/12490)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Follow up for a3462dd2bd541af6372855917c6ccb5643aeda93
  
  <img width="884" height="255" alt="image"
  src="https://github.com/user-attachments/assets/da4e4dd5-e645-40ed-8e9c-0ed8c9aee1c4"
  />
  ```
- [`c19ce03`](https://github.com/ghostty-org/ghostty/commit/c19ce03b3e9b9522a1e98dd992f34a6f4f9e6ff0) fix: update Se terminfo entry to reset cursor to configured default ([#12487](https://github.com/ghostty-org/ghostty/issues/12487)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Problem
  
  Current `Se` sequence (reset cursor style) is `\E[2 q`, which always
  sets steady block, regardless of user config.
  
  ## Solution
  
  Update sequence to `\E[0 q`, which sets the cursor style to the user
  configured default cursor.
  
  fix https://github.com/ghostty-org/ghostty/issues/12482
  Helps with neovim issue: https://github.com/neovim/neovim/issues/38987
  
  ## AI Disclosure
  
  I didn't use AI for this, haha. Unless you count random questions to
  learn about terminfo beforehand, but I relied on [legit
  resources](https://invisible-island.net/xterm/terminfo.html) for real
  info. It says:
  
  >  Se resets the cursor style to the terminal power-on default.
  
  I think the useful interpretation is to set the user configured default.
  ```
- [`1ed22a5`](https://github.com/ghostty-org/ghostty/commit/1ed22a5210f4a7a3dc48088cdf33fac9d95bb278) renderer: fix preedit range width ([#12479](https://github.com/ghostty-org/ghostty/issues/12479)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Related to #12466
  
  `Preedit.range()` returns an inclusive range, but the end position was
  calculated as `start + w`. For wide preedit text, this covers one extra
  cell.
  
  In Debug builds, Korean IME composition between existing Hangul
  characters can panic with:
  `index out of bounds: index 2, len 2`
  
  I reproduced this reliably when there are two Hangul characters to the
  right of the cursor. For example, type `가나다`, move the cursor between
  `가` and `나`, then start a new Korean IME composition. With the old range
  calculation, the renderer skips the first wide character plus the head
  cell of the next wide character, then resumes on that character's spacer
  tail.
  
  This changes the inclusive end to `start + (w - 1)` and adds focused
  tests for narrow, wide, and right-edge preedit ranges.
  
  This does not fully fix the visual behavior reported in #12466. The
  adjacent character can still disappear during composition, so this PR
  only fixes the crash side of the problem.
  ```
- [`576d07f`](https://github.com/ghostty-org/ghostty/commit/576d07ffc13c1b0e257f6650484757f31ed5bf39) macOS: update tests and add test plan ([#12473](https://github.com/ghostty-org/ghostty/issues/12473)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This updates UI tests and adds a test plan on disk, so we can change the
  configuration to different ones with the host app.
  
  If you changed the icon in regular ghostty config file, the tests can
  only be run once, since the signature is changed after changing the
  icon. Adding an on-disk test plan helps us to better control the
  environment for the tests.
  ```
- [`0b56ae2`](https://github.com/ghostty-org/ghostty/commit/0b56ae2cc737656280ed646888ce276468ca8c73) gtk: fix quick terminal breaking when manually toggled off while auto-hide is enabled ([#12471](https://github.com/ghostty-org/ghostty/issues/12471)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes quick terminal breaking when auto-hide is enabled and quick
  terminal is manually toggled off (#11679).
  
  `quick-terminal-autohide` is implemented by the `Window.propIsActive`
  function in `apprt/gtk/class/window.zig` which calls
  `Window.toggleVisibility` when the quick terminal window becomes
  inactive (loses focus). However `Window.propIsActive` is also triggered
  when you manually hide the quick terminal because hiding it causes the
  window to become inactive. Normally that should just toggle the quick
  terminal off and immediately back on, but there is also a re-entrancy
  issue. Manually toggling off the terminal causes the
  `Application.toggleQuickTerminal` (in `apprt/gtk/class/application.zig`)
  to run which sets off the call chain `Window.toggleVisibility ->
  gtk_widget_set_visible -> ... GTK signal/event handling ... ->
  Window.propIsActive -> Window.toggleVisibility ->
  gtk_widget_set_visible`.
  The nested calls to `gtk_widget_set_visible` cause the GTK window state
  to become corrupted. The window is marked visible, but is not actually
  visible or just shows a placeholder. What exactly happens depends on the
  compositor and how it handles moving window focus.
  
  Reproduced the bug on KDE and hyprland and verified the fix on both.
  
  ### Changes
  
  `apprt/gtk/class/window.zig`: added check to `Window.propIsActive` to
  only toggle quick-terminal if it is inactive **and** visible.
  
  ### AI Disclosure
  
  Found the bug without AI using "printf debugging" then traced it through
  GTK with valgrind. Used GPT5.4 in setting up valgrind and researching
  how signals/events move through GTK internally.
  ```
- [`34cbb5f`](https://github.com/ghostty-org/ghostty/commit/34cbb5fa8180c1f5f7cb874377af23904cd4c36a) feat: add middle-click action configuration ([#12478](https://github.com/ghostty-org/ghostty/issues/12478)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This PR addresses
  https://github.com/ghostty-org/ghostty/discussions/12108 implemented
  similarly to https://github.com/ghostty-org/ghostty/pull/8254 to allow
  middle click + TrackPoint scrolling on MacOS. `primary-paste` naming
  comes from `gtk_enable_primary_paste`.
  
  The following configuration values for `middle-click-action` are
  provided:
  - `primary-paste` - Paste from the selection (or system) clipboard per
  `copy-on-select`.
  - `ignore` - Do nothing, ignore the middle click.
  
  Tested locally on macOS with Zig 0.15.2 using `zig build
  -Doptimize=ReleaseFast`.
  
  Thank you!
  ```

## April 26, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/24947896288)  
Summary: 1 runs • 5 commits • 3 authors

### Changes

- [`7cc9cc8`](https://github.com/ghostty-org/ghostty/commit/7cc9cc8ba8ba19965b9752ea55c171b5fba97874) flatpak: terminate session if Ghostty disconnects from bus ([@alaviss](https://github.com/alaviss))
  ```text
  This makes sure that if Ghostty crashes, commands spawned are also
  terminated automatically by the Flatpak Session Helper.
  ```
- [`8b8f713`](https://github.com/ghostty-org/ghostty/commit/8b8f7136d041d324867f977e8980cba4e1aeb675) flatpak: don't assume c_uint to be u32 ([@alaviss](https://github.com/alaviss))
  ```text
  Thanks pluie for the pointer.
  ```
- [`8b90efd`](https://github.com/ghostty-org/ghostty/commit/8b90efd913ceb51ec49034dfb08736a39c07cf2d) os: use GetTempPathW for allocTmpDir on Windows ([@jparise](https://github.com/jparise))
  ```text
  `allocTmpDir` previously read `%TMP%` via `getenvW` and returned `null`
  if the variable wasn't set, requiring each caller to to deal with the
  nullable. Unfortunately, there isn't a platform-neutral default value
  that makes sense for those cases (i.e. `/tmp` is POSIX-y).
  
  We now use `GetTempPathW` on Windows, which is the official way to get
  this directory: `TMP` → `TEMP` → `USERPROFILE` → `GetWindowsDirectoryW`.
  
  With a real system call behind it, the function no longer needs to be
  nullable: the only remaining failure modes are OOM (propagated) and the
  syscall itself failing or returning data we can't decode. In those later
  cases, we use `C:\Windows\Temp` as a fallback, similar to how we use
  `/tmp` in the POSIX case.
  
  The Windows path always allocates so it still must be paired with
  `freeTmpDir`, which matches the existing contract.
  ```
- [`278041c`](https://github.com/ghostty-org/ghostty/commit/278041c4bc0e47aebfda9c695760476838f2da4a) flatpak: terminate session if Ghostty disconnects from bus ([#12427](https://github.com/ghostty-org/ghostty/issues/12427)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This makes sure that if Ghostty crashes, commands spawned are also
  terminated automatically by the Flatpak Session Helper.
  
  The few crashes I got left a lot of background processes, some of them
  pretty heavy and took awhile to be figured out.
  ```
- [`c74f6d5`](https://github.com/ghostty-org/ghostty/commit/c74f6d56d1feef473033057bc0ff7e3f00cf6421) os: use GetTempPathW for allocTmpDir on Windows ([#12469](https://github.com/ghostty-org/ghostty/issues/12469)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `allocTmpDir` previously read `%TMP%` via `getenvW` and returned `null`
  if the variable wasn't set, requiring each caller to to deal with the
  nullable. Unfortunately, there isn't a platform-neutral default value
  that makes sense for those cases (i.e. `/tmp` is POSIX-y).
  
  We now use `GetTempPathW` on Windows, which is the official way to get
  this directory: `TMP` → `TEMP` → `USERPROFILE` → `GetWindowsDirectoryW`.
  
  With a real system call behind it, the function no longer needs to be
  nullable: the only remaining failure modes are OOM (propagated) and the
  syscall itself failing or returning data we can't decode. In those later
  cases, we use `C:\Windows\Temp` as a fallback, similar to how we use
  `/tmp` in the POSIX case.
  
  The Windows path always allocates so it still must be paired with
  `freeTmpDir`, which matches the existing contract.
  
  ---
  
  *AI Disclosure:* I verified the Windows path using Claude and Zig's
  cross-compilation capabilities because I don't have a Windows
  environment in which to test this. I do fully understand the code based
  on my prior life as a Windows game developer though.
  ```

## April 25, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/24940217324), [2](https://github.com/ghostty-org/ghostty/actions/runs/24940064595), [3](https://github.com/ghostty-org/ghostty/actions/runs/24936929621), [4](https://github.com/ghostty-org/ghostty/actions/runs/24936454850), [5](https://github.com/ghostty-org/ghostty/actions/runs/24935930871), [6](https://github.com/ghostty-org/ghostty/actions/runs/24935717312), [7](https://github.com/ghostty-org/ghostty/actions/runs/24935635947), [8](https://github.com/ghostty-org/ghostty/actions/runs/24935490306), [9](https://github.com/ghostty-org/ghostty/actions/runs/24935332327), [10](https://github.com/ghostty-org/ghostty/actions/runs/24935218124), [11](https://github.com/ghostty-org/ghostty/actions/runs/24933524535), [12](https://github.com/ghostty-org/ghostty/actions/runs/24923989307)  
Summary: 12 runs • 49 commits • 11 authors

### Changes

- [`13ada38`](https://github.com/ghostty-org/ghostty/commit/13ada38ac45c5fb2a78c9b57cf86b5d22c9cf739) os: RANDOM_BASENAME_LEN -> random_basename_len ([@jparise](https://github.com/jparise))
- [`67b5783`](https://github.com/ghostty-org/ghostty/commit/67b5783bdd718796a9e2a5d5f9de505f8e047ea5) os: RANDOM_BASENAME_LEN -> random_basename_len ([#12467](https://github.com/ghostty-org/ghostty/issues/12467)) ([@mitchellh](https://github.com/mitchellh))
- [`28f4676`](https://github.com/ghostty-org/ghostty/commit/28f4676b5d8964189ac3f6974cfbb212ef322bb4) core: Acquire renderer state mutex before calling processLinks ([@jmr](https://github.com/jmr))
  ```text
  Holding the renderer state mutex is a documented precondition of
  `processLinks`, but `mouseButtonCallback` previously called
  the function without the mutex.
  
  This creates a race with the I/O thread's `processOutput`, which can
  prune scrollback pages while `processLinks` is reading them, resulting
  in a use-after-free segfault.  See
  https://github.com/ghostty-org/ghostty/discussions/12409 (Linux: crash
  while selecting text).
  
  https://github.com/ghostty-org/ghostty/blob/57b5e1e2507cd65ab8197d39baa4ce2505185510/src/Surface.zig#L4354-L4355
  
  https://github.com/ghostty-org/ghostty/blob/57b5e1e2507cd65ab8197d39baa4ce2505185510/src/Surface.zig#L3822-L3824
  
  995e4e375 (os: open) changed the body of `processLinks` to be
  non-trivial and documented the precondition, but the lock was not held
  at the call site.
  ```
- [`8ebf4f7`](https://github.com/ghostty-org/ghostty/commit/8ebf4f70e5e8d0e2bf80a2b9c53ca85ca8d396e7) macOS: make tab color optional ([@bo2themax](https://github.com/bo2themax))
- [`5b89671`](https://github.com/ghostty-org/ghostty/commit/5b89671d513fc128ae7e9a2cfe43262e443c1a13) macOS: make terminal restorable state compatible with 1.2.3(v5) ([@bo2themax](https://github.com/bo2themax))
- [`bfe07bb`](https://github.com/ghostty-org/ghostty/commit/bfe07bb99ed796e7f9248d06cf21b9c3e640dcc7) macOS: add InternalState to cover migrations ([@bo2themax](https://github.com/bo2themax))
- [`72c03e7`](https://github.com/ghostty-org/ghostty/commit/72c03e7fb87e97bbbb6973919d55adb2c671ec43) macOS: add window restoration tests ([@bo2themax](https://github.com/bo2themax))
- [`231f6f4`](https://github.com/ghostty-org/ghostty/commit/231f6f4c75f02531ae385c22c2b8ad81f53d1555) macOS: move the restoration logs ([@bo2themax](https://github.com/bo2themax))
- [`3853761`](https://github.com/ghostty-org/ghostty/commit/385376185cf8d9f9545aec04cf643d7601300c81) macOS: remove manual invalidateRestorableState() ([@bo2themax](https://github.com/bo2themax))
- [`c9d2285`](https://github.com/ghostty-org/ghostty/commit/c9d2285f63fc3f34c466087f4828741fd43e2538) os: add randomTmpPath for allocating temp paths ([@jparise](https://github.com/jparise))
  ```text
  Factor TempDir's name generation into a reusable `randomBasename` (16
  random bytes, url-safe base64) and add `randomTmpPath` on top, which
  composes `allocTmpDir` + `randomBasename` into a single allocated path
  in the form `{TMPDIR}/{prefix}{random}` (mktemp(1)-ish).
  
  This is convenient for callers who want a unique path under TMPDIR (for
  a temporary file, socket, etc.) without having to think about basename
  buffer sizing or path joining.
  
  Also, use `std.base64.url_safe_no_pad.Encoder` instead of the custom
  base64 alphabet, which is exactly equivalent.
  ```
- [`8e1dfbc`](https://github.com/ghostty-org/ghostty/commit/8e1dfbcf3ebd546ef22086857859c9e22764282c) os: add randomTmpPath for allocating temp paths ([#12465](https://github.com/ghostty-org/ghostty/issues/12465)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Factor TempDir's name generation into a reusable `randomBasename` (16
  random bytes, url-safe base64) and add `randomTmpPath` on top, which
  composes `allocTmpDir` + `randomBasename` into a single allocated path
  in the form `{TMPDIR}/{prefix}{random}` (`mktemp(1)`-ish).
  
  This is convenient for callers who want a unique path under TMPDIR (for
  a temporary file, socket, etc.) without having to think about basename
  buffer sizing or path joining.
  
  Also, use `std.base64.url_safe_no_pad.Encoder` instead of the custom
  base64 alphabet, which is exactly equivalent.
  ```
- [`aedf39f`](https://github.com/ghostty-org/ghostty/commit/aedf39f3bdce14101a823003aeadcfcbe085b54a) macOS: support migrations when restoring window state ([#12461](https://github.com/ghostty-org/ghostty/issues/12461)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  First two commits fix the issue when upgrading from 1.2.x to 1.3.x.
  (#11304)
  
  > To double check if this pr really fixes the issue, you can either
  archive a release build, sign with the same profile, and override
  manually.
  >
  > Or you can find the `savedState` files (located in `~/Library/Daemon\
  Containers/<uuid>`), can copy them the local build dir (which is what I
  did), and run the debug build.
  
  Following commits add tests for migrations and some logs.
  
  **Currently the minimum version is set to 1.2.x**, since there's a lot
  changes comparing to 1.1.x. It will be difficult to restore
  `Ghostty.SplitNode` -> `SplitTree<Ghostty.SurfaceView>` without
  introducing a lot of checks.
  ```
- [`0e0bcaf`](https://github.com/ghostty-org/ghostty/commit/0e0bcafed5b648e07b3f9f4259254b3864fb69b7) macOS: remove manual invalidateRestorableState() ([#12464](https://github.com/ghostty-org/ghostty/issues/12464)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This should be safe to delete now after #12461.
  
  I tested saving 27 tabs, 4 with 2 splits,
  `TerminalRestorable.encode(with:` finished successfully.
  
  And I check the breakpoints when the Sparkle sends
  `-[NSRunningApplication treminate]`. The call stack at `-[NSResponder
  invalidateRestorableState]` is pretty much the same as quitting via
  `cmd+q`.
  ```
- [`e9ca0f8`](https://github.com/ghostty-org/ghostty/commit/e9ca0f8c9a403938e90d1481c7b72459cee78457) core: Acquire renderer state mutex before calling processLinks ([#12463](https://github.com/ghostty-org/ghostty/issues/12463)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Holding the renderer state mutex is a documented precondition of
  `processLinks`, but `mouseButtonCallback` previously called the function
  without the mutex.
  
  This creates a race with the I/O thread's `processOutput`, which can
  prune scrollback pages while `processLinks` is reading them, resulting
  in a use-after-free segfault. See
  https://github.com/ghostty-org/ghostty/discussions/12409 (Linux: crash
  while selecting text).
  
  
  https://github.com/ghostty-org/ghostty/blob/57b5e1e2507cd65ab8197d39baa4ce2505185510/src/Surface.zig#L4354-L4355
  
  
  https://github.com/ghostty-org/ghostty/blob/57b5e1e2507cd65ab8197d39baa4ce2505185510/src/Surface.zig#L3822-L3824
  
  995e4e375 (os: open) changed the body of `processLinks` to be
  non-trivial and documented the precondition, but the lock was not held
  at the call site.
  ```
- [`85dc4b1`](https://github.com/ghostty-org/ghostty/commit/85dc4b1842799d23db4abc5c2a671e4975c9d49d) surface: respect semantic prompt boundaries for links (Vasyl Zuziak)
  ```text
  Link detection currently expands the clicked location to a full line
  before running the configured regexes. When semantic prompt markers
  are present, this can cause prompt text and neighboring content to be
  matched together even though they are distinct semantic regions.
  
  Use semantic prompt boundaries when selecting the text to inspect for
  link matching. This keeps prompt text separate from the content beside
  it and avoids folding prompt text into double-click link/path
  selection.
  
  Add a regression test that models a prompt and command on the same
  line and verifies the prompt region and input region remain separate.
  ```
- [`c4a671b`](https://github.com/ghostty-org/ghostty/commit/c4a671ba5a5c3a896b90b066f2a22abe2eaad17b) fix: remove test as has been suggested in comment (Vasyl Zuziak)
- [`b613ffc`](https://github.com/ghostty-org/ghostty/commit/b613ffcfd8c323d2d97f723f6f998b21ceba5a54) surface: respect semantic prompt boundaries for links ([#12435](https://github.com/ghostty-org/ghostty/issues/12435)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Link detection currently expands the clicked location to a full line
  before running the configured regexes. When semantic prompt markers are
  present, this can cause prompt text and neighboring content to be
  matched together even though they are distinct semantic regions.
  
  Use semantic prompt boundaries when selecting the text to inspect for
  link matching. This keeps prompt text separate from the content beside
  it and avoids folding prompt text into double-click link/path selection.
  
  Add a regression test that models a prompt and command on the same line
  and verifies the prompt region and input region remain separate.
  
  ----
  
  this is a fix for the issue users reported in
  https://github.com/ghostty-org/ghostty/discussions/11415
  
  **disclaimer**: I used codex addon within Cursor to research this
  bug/regression and find a proper fix for it.
  ```
- [`14c0631`](https://github.com/ghostty-org/ghostty/commit/14c06312d541c7f655cfa134062422bd8dc3551e) feat: add default GTK keybinds for move_tab ([@enzowilliam](https://github.com/enzowilliam))
  ```text
  Reassign jump_to_prompt from Ctrl+Shift+PageUp/PageDown to
  Ctrl+Shift+Arrow Up/Down on GTK, freeing the idiomatic Linux
  keybinds (Ctrl+Shift+PageUp/PageDown) for move_tab.
  
  This matches the tab-moving keybinds used by Firefox, GNOME Terminal,
  and VSCode. The new jump_to_prompt binding mirrors the macOS pattern
  (Cmd+Shift+Arrow Up/Down).
  
  Closes #4998
  ```
- [`c5c3cf1`](https://github.com/ghostty-org/ghostty/commit/c5c3cf16ba96ec67b20423e43a3a1aedeff0b726) feat: add GTK keybinds (matching the idiomatic Linux convention used by Firefox, GNOME Terminal, and VSCode) for move_tab ([#12458](https://github.com/ghostty-org/ghostty/issues/12458)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  > Re-submitting #11857, which was auto-closed pre-vouch. I'm now in the
  vouched list.
  
  ## Summary
  
  Adds default keybinds for `move_tab` on GTK/Linux, matching the
  idiomatic Linux convention used by Firefox, GNOME Terminal, and VSCode:
  
  - **`Ctrl+Shift+PageUp`** → `move_tab:-1` (move tab left)
  - **`Ctrl+Shift+PageDown`** → `move_tab:1` (move tab right)
  
  To free these keys, `jump_to_prompt` is reassigned to `Ctrl+Shift+Arrow
  Up/Down`, which:
  - Mirrors the macOS default (`Cmd+Shift+Arrow Up/Down`)
  - Is currently unbound on GTK
  - Maintains directional consistency (up = previous, down = next)
  
  The new `move_tab` bindings use `putFlags` with `performable: true` to
  match the pattern used by other tab actions (`previous_tab`,
  `next_tab`).
  
  Closes #4998
  
  ## Changes
  - `src/config/Config.zig`: Reassign `jump_to_prompt` from
  `Ctrl+Shift+PageUp/PageDown` to `Ctrl+Shift+Arrow Up/Down` (GTK only)
  - `src/config/Config.zig`: Add `move_tab` default keybinds as
  `Ctrl+Shift+PageUp/PageDown` (GTK only)
  
  ## Test plan
  - [ ] Build on Linux/GTK: `zig build`
  - [ ] Verify `Ctrl+Shift+PageUp` moves current tab left
  - [ ] Verify `Ctrl+Shift+PageDown` moves current tab right
  - [ ] Verify `Ctrl+Shift+Arrow Up` jumps to previous prompt
  - [ ] Verify `Ctrl+Shift+Arrow Down` jumps to next prompt
  - [ ] Verify `Ctrl+PageUp/PageDown` still switches tabs (unchanged)
  - [ ] Verify macOS keybinds are unaffected
  ```
- [`fa141a7`](https://github.com/ghostty-org/ghostty/commit/fa141a726203224c12b831e0513530fa2406ef26) Fix Korean IME committed text handling for arrow keys ([@dobbylee](https://github.com/dobbylee))
- [`df4f981`](https://github.com/ghostty-org/ghostty/commit/df4f981592e9145334ada57271858a98728607eb) Fix Korean IME committed text handling for arrow keys ([#12447](https://github.com/ghostty-org/ghostty/issues/12447)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11461
  
  - Send Korean IME committed text as a separate text-only key event when
  arrow-key handling commits preedit text.
  - Replay arrow navigation after the committed text is sent. Do not
  replay plain Left Arrow to match Terminal.app behavior.
  - Manually tested Arrow keys and Opt/Cmd+Arrow during Korean preedit on
  macOS.
  ```
- [`4d1bb9e`](https://github.com/ghostty-org/ghostty/commit/4d1bb9efe47cd0d1d2057cc08bf361229618e7c7) Update VOUCHED list ([#12456](https://github.com/ghostty-org/ghostty/issues/12456)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11685#discussioncomment-16712917)
  from @mitchellh.
  
  Denounce: @enkr1
  ```
- [`c9ba2b2`](https://github.com/ghostty-org/ghostty/commit/c9ba2b2afaf133c42bc1baeef683d8e6af19818b) Update VOUCHED list ([#12457](https://github.com/ghostty-org/ghostty/issues/12457)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11628#discussioncomment-16712930)
  from @mitchellh.
  
  Denounce: @4RH1T3CT0R7
  ```
- [`0e707ba`](https://github.com/ghostty-org/ghostty/commit/0e707ba3f661705e61e58715a335cb064d168928) Update VOUCHED list ([#12452](https://github.com/ghostty-org/ghostty/issues/12452)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11975#discussioncomment-16712831)
  from @mitchellh.
  
  Vouch: @rightaditya
  ```
- [`e0c71dd`](https://github.com/ghostty-org/ghostty/commit/e0c71dd41bf771c591b01dd32f7d0cbddc0c525f) Update VOUCHED list ([#12453](https://github.com/ghostty-org/ghostty/issues/12453)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11882#discussioncomment-16712859)
  from @mitchellh.
  
  Vouch: @mpatankar6
  ```
- [`5a3b0c9`](https://github.com/ghostty-org/ghostty/commit/5a3b0c9c493c540a38f9c26ec3479f1472e7533e) Update VOUCHED list ([#12454](https://github.com/ghostty-org/ghostty/issues/12454)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11858#discussioncomment-16712861)
  from @mitchellh.
  
  Vouch: @enzowilliam
  ```
- [`03e08f0`](https://github.com/ghostty-org/ghostty/commit/03e08f0c89765c7d2029abc1b956d4606d454c1b) Update VOUCHED list ([#12455](https://github.com/ghostty-org/ghostty/issues/12455)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11795#discussioncomment-16712869)
  from @mitchellh.
  
  Vouch: @bch
  ```
- [`50e8eba`](https://github.com/ghostty-org/ghostty/commit/50e8ebaf6025c4b35ef57f0e82418e4beb3e3db3) surface: sync middle-click paste source with copy-on-select ([@007hacky007](https://github.com/007hacky007))
  ```text
  Middle-click paste previously always read from the selection clipboard
  (falling back to the standard clipboard on platforms without one).
  
  Now the paste source follows copy-on-select:
  - copy-on-select = true: paste from selection clipboard (unchanged)
  - copy-on-select = clipboard: paste from system clipboard
  - copy-on-select = false: paste from selection clipboard (unchanged)
  
  Fixes ghostty-org/ghostty#9788.
  ```
- [`e72774f`](https://github.com/ghostty-org/ghostty/commit/e72774f2aba03f5db6426dfc0748e6f71c9429e8) Update VOUCHED list ([@github-actions[bot]](https://github.com/apps/github-actions))
  ```text
  https://github.com/ghostty-org/ghostty/discussions/12263#discussioncomment-DC_kwDOHFhdAs4A_wQ_
  ```
- [`4c046ef`](https://github.com/ghostty-org/ghostty/commit/4c046efbb10562400e76e690d3c327c0e3a806b1) Update VOUCHED list ([#12449](https://github.com/ghostty-org/ghostty/issues/12449)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12141#discussioncomment-16712795)
  from @mitchellh.
  
  Vouch: @AkimioJR
  ```
- [`ee81a6e`](https://github.com/ghostty-org/ghostty/commit/ee81a6e1c62bdec461bec670fbad3b1cd3351bf3) Update VOUCHED list ([#12450](https://github.com/ghostty-org/ghostty/issues/12450)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12108#discussioncomment-16712799)
  from @mitchellh.
  
  Vouch: @lebdron
  ```
- [`2dee1f1`](https://github.com/ghostty-org/ghostty/commit/2dee1f1a3f66ccf903fdd9d23783bdb88411bd56) Update VOUCHED list ([#12445](https://github.com/ghostty-org/ghostty/issues/12445)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12263#discussioncomment-16712767)
  from @mitchellh.
  
  Vouch: @thoutbeckers
  ```
- [`69452b5`](https://github.com/ghostty-org/ghostty/commit/69452b5c6f54b794664a7593e9a665bdd1caf1b2) Sync middle-click paste with copy-on-select ([#12443](https://github.com/ghostty-org/ghostty/issues/12443)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Implements the behavior from #9788.
  
  Today, middle-click paste always reads from the selection clipboard (or
  the
  system clipboard on platforms without a selection clipboard). With this
  change
  it follows `copy-on-select`:
  
  - `true`: selection clipboard (unchanged)
  - `clipboard`: system clipboard
  - `false`: selection clipboard (also unchanged, preserves traditional
  X11
    middle-click behavior)
  
  The idea is symmetry: if `copy-on-select = clipboard` writes selections
  to the
  system clipboard, middle-click should come back from there too.
  
  Also updated the config doc comment, which previously claimed
  middle-click
  "will always use the selection clipboard".
  
  ### Testing
  
  `zig build test` passes locally (macOS, Zig 0.15.2).
  
  Built and runtime-tested via the fork's CI:
  https://github.com/007hacky007/ghostty/actions/runs/24707475544 - I'm
  running the resulting binary daily and the three `copy-on-select` modes
  behave as described above.
  ```
- [`51590ad`](https://github.com/ghostty-org/ghostty/commit/51590ad7f1b80e60a1aa200f887f5a24f44d4006) Update VOUCHED list ([#12451](https://github.com/ghostty-org/ghostty/issues/12451)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11993#discussioncomment-16712826)
  from @mitchellh.
  
  Vouch: @VoidNV
  ```
- [`fc7a064`](https://github.com/ghostty-org/ghostty/commit/fc7a064e80870f5c67e288668045c9ad80aec9b9) Update VOUCHED list ([#12444](https://github.com/ghostty-org/ghostty/issues/12444)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12305#discussioncomment-16712760)
  from @mitchellh.
  
  Vouch: @aaron-ang
  ```
- [`8c3db43`](https://github.com/ghostty-org/ghostty/commit/8c3db43c8602d7d148083a7cca2b63e533115719) Update VOUCHED list ([#12446](https://github.com/ghostty-org/ghostty/issues/12446)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12272#discussioncomment-16712769)
  from @mitchellh.
  
  Vouch: @dkinzler
  ```
- [`e0d0fbe`](https://github.com/ghostty-org/ghostty/commit/e0d0fbe0ad0a39c42fb3a7fa3885de829c3e5cdb) Update VOUCHED list ([#12448](https://github.com/ghostty-org/ghostty/issues/12448)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12169#discussioncomment-16712790)
  from @mitchellh.
  
  Vouch: @knu
  ```
- [`560b7ba`](https://github.com/ghostty-org/ghostty/commit/560b7ba8e853d1744a04915b9c62062f992310a0) gtk/SurfaceScrolledWindow: wrap root child with another Adw.Bin ([@alaviss](https://github.com/alaviss))
  ```text
  Due to a known Gtk issue, the scrolled_window at the root of the
  template is free-ed twice on dispose. This causes crashes when used with
  GNOME 49 platform (Gtk 4.20, libadwaita 1.8.5).
  
  Workaround this issue by wrapping the root child in another Adw.Bin,
  similar to widgets like ResizeOverlay.
  
  LLM was used to perform discovery against a manually recorded Valgrind
  trace, and helped tracking down known fixes for this problem.
  
  Fixes https://github.com/ghostty-org/ghostty/discussions/12306
  
  Assisted-by: OpenAI GPT-5.4
  ```
- [`74045cc`](https://github.com/ghostty-org/ghostty/commit/74045cc5d8368e03ea3b4b8896b6e0a1dcf4089b) Update VOUCHED list ([#12438](https://github.com/ghostty-org/ghostty/issues/12438)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12354#discussioncomment-16712711)
  from @mitchellh.
  
  Vouch: @007hacky007
  ```
- [`b3d4f51`](https://github.com/ghostty-org/ghostty/commit/b3d4f51ca78788eeda1fe784ce3c6056c8d3aa1d) Update VOUCHED list ([#12439](https://github.com/ghostty-org/ghostty/issues/12439)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12347#discussioncomment-16712718)
  from @mitchellh.
  
  Vouch: @rjwittams
  ```
- [`8e2a13c`](https://github.com/ghostty-org/ghostty/commit/8e2a13cb6094561a693e47e587e23abdcbb791d6) gtk/SurfaceScrolledWindow: wrap root child with another Adw.Bin ([#12426](https://github.com/ghostty-org/ghostty/issues/12426)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Due to a known Gtk issue, the scrolled_window at the root of the
  template is free-ed twice on dispose. This causes crashes when used with
  GNOME 49 platform (Gtk 4.20, libadwaita 1.8.5).
  
  Workaround this issue by wrapping the root child in another Adw.Bin,
  similar to widgets like ResizeOverlay.
  
  LLM was used to perform discovery against a manually recorded Valgrind
  trace, and helped tracking down known fixes for this problem. The
  comment in code was taken from another instance in the repository.
  
  Fixes https://github.com/ghostty-org/ghostty/discussions/12306
  
  Assisted-by: OpenAI GPT-5.4
  ```
- [`c21ba8d`](https://github.com/ghostty-org/ghostty/commit/c21ba8d8268cfaf8c5967f65d140be38e86fd159) Update VOUCHED list ([#12440](https://github.com/ghostty-org/ghostty/issues/12440)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11632#discussioncomment-16712730)
  from @mitchellh.
  
  Vouch: @ajiblock
  ```
- [`667d467`](https://github.com/ghostty-org/ghostty/commit/667d467e24b77dff439a5ab02bed6771931debcd) Update VOUCHED list ([#12441](https://github.com/ghostty-org/ghostty/issues/12441)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11987#discussioncomment-16712733)
  from @mitchellh.
  
  Vouch: @nouritsu
  ```
- [`119f387`](https://github.com/ghostty-org/ghostty/commit/119f3875d46f7fd142ce8aa3cb65e05c0e007482) Update VOUCHED list ([#12442](https://github.com/ghostty-org/ghostty/issues/12442)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12435#issuecomment-4320055303)
  from @mitchellh.
  
  Vouch: @ZuBB
  ```
- [`6fb86a8`](https://github.com/ghostty-org/ghostty/commit/6fb86a819e6691a63fdf669e9a066de795cad533) flatpak: update runtime to GNOME 50 ([@alaviss](https://github.com/alaviss))
- [`98d14aa`](https://github.com/ghostty-org/ghostty/commit/98d14aa66bf9e29c1d05c1b62705173653d3a5b5) flatpak: update runtime to GNOME 50 ([#12428](https://github.com/ghostty-org/ghostty/issues/12428)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Notable dependency changes:
  
  - GTK: `4.20.4` -> `4.22.2`
  - libadwaita: `1.8.5` -> `1.9.0`
  ```
- [`98fb58b`](https://github.com/ghostty-org/ghostty/commit/98fb58b3265d10cde89a6fb1f76676fe2e61ff44) Update VOUCHED list ([#12437](https://github.com/ghostty-org/ghostty/issues/12437)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12295#discussioncomment-16712704)
  from @mitchellh.
  
  Vouch: @dobbylee
  ```
- [`c47a809`](https://github.com/ghostty-org/ghostty/commit/c47a8091f18200af980f7943d646ff0abc031a4b) Update VOUCHED list ([#12436](https://github.com/ghostty-org/ghostty/issues/12436)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12409#discussioncomment-16712208)
  from @00-kat.
  
  Vouch: @jmr
  ```
- [`57b5e1e`](https://github.com/ghostty-org/ghostty/commit/57b5e1e2507cd65ab8197d39baa4ce2505185510) Update VOUCHED list ([#12425](https://github.com/ghostty-org/ghostty/issues/12425)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12308#discussioncomment-16709130)
  from @jcollie.
  
  Vouch: @alaviss
  ```

## April 24, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/24914171209), [2](https://github.com/ghostty-org/ghostty/actions/runs/24911997879), [3](https://github.com/ghostty-org/ghostty/actions/runs/24907048466), [4](https://github.com/ghostty-org/ghostty/actions/runs/24889534540), [5](https://github.com/ghostty-org/ghostty/actions/runs/24873393693)  
Summary: 5 runs • 24 commits • 7 authors

### Changes

- [`7c91cef`](https://github.com/ghostty-org/ghostty/commit/7c91cef28de31a9b2238d83b0f63b03a9841bd49) config: use Config to check key binding instead of App ([@bo2themax](https://github.com/bo2themax))
  ```text
  Previously `ghostty_app_key_is_binding` (unlike Surface) is just using `config.keybind` to check whether a KeyEvent is in the set or not.
  
  After this, I can add unit tests for keybinding more easily, with dummy configs.
  ```
- [`4ceeba4`](https://github.com/ghostty-org/ghostty/commit/4ceeba4851030e75398cf1e5d3f7d8c7ed645e87) config: use Config to check key binding instead of App ([#12415](https://github.com/ghostty-org/ghostty/issues/12415)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously `ghostty_app_key_is_binding` (unlike Surface) is just using
  `config.keybind` to check whether a KeyEvent is in the set or not.
  
  After this, I can add unit tests for keybinding more easily with dummy
  configs.
  
  I didn't find any usages of this in GTK, so it shouldn't affect
  anything. ci will see if this is the case:)
  ```
- [`6b69ea0`](https://github.com/ghostty-org/ghostty/commit/6b69ea05170435ee6abd79b9a3da7a2609d5aaa3) libghostty: enable cross-compiling macOS from Linux/Windows ([@mitchellh](https://github.com/mitchellh))
  ```text
  This allows libghostty-vt to be cross-compiled for macOS from non-macOS
  platforms. I've updated pkg/apple-sdk to fallback to Zig's embedded
  macOS headers if the macOS SDK is not found.
  
  Additionally, CombineArchivesStep has been updated to use Linux
  tooling on Linux.
  ```
- [`2ed382a`](https://github.com/ghostty-org/ghostty/commit/2ed382a15566b267c32fae440b065f7844b15bfb) libghostty: enable cross-compiling macOS from Linux/Windows ([#12417](https://github.com/ghostty-org/ghostty/issues/12417)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This allows libghostty-vt to be cross-compiled for macOS from non-macOS
  platforms. I've updated pkg/apple-sdk to fallback to Zig's embedded
  macOS headers if the macOS SDK is not found. Additionally,
  CombineArchivesStep has been updated to use Linux tooling on Linux. CI
  updated to test this.
  ```
- [`4204dec`](https://github.com/ghostty-org/ghostty/commit/4204dec94a45ee7ce3990af33b301053191232c5) build: respect config.emit_xcframework for building libghostty-vt.xcframework on Darwin (0xDVC)
  ```text
  This fixes a hardcoded build issue on macOS where Zig unconditionally forces xcodebuild -create-xcframework to run during compilation, even when the caller explicitly specifies that they only want the raw standard C objects/headers (-Demit-lib-vt).
  
  The Bug:
  Around line 155 in build.zig, the libghostty-vt xcframework was being packaged unconditionally for Darwin builds. This caused developers (and wrappers like go-libghostty) attempting to natively build the vt library locally using only the minimal macOS Command Line Tools to experience an immediate crash, as xcodebuild -create-xcframework strictly demands a full Xcode application installation.
  
  The Fix:
  Guarded the GhosttyLibVt xcframework creation step with config.emit_xcframework. Because src/build/Config.zig intuitively forces emit_xcframework to default to false whenever emit_lib_vt is invoked, this structurally allows lightweight macOS builds to safely skip the xcodebuild invocation while still correctly compiling the standard .a object library files.
  ```
- [`38e8e54`](https://github.com/ghostty-org/ghostty/commit/38e8e54f98a8d5574962cfd34649d0740643a6ff) build: make libghostty-vt xcframework emission explicit via -Demit-lib-vt-xcframework (0xDVC)
- [`4e2e765`](https://github.com/ghostty-org/ghostty/commit/4e2e765fd4e70d94a0d7fca36fd742e5b77d8842) Merge branch 'main' into fix/xcframework-macos-dependency ([@0xDVC](https://github.com/0xDVC))
- [`caad13e`](https://github.com/ghostty-org/ghostty/commit/caad13e2323ff74f2ca9c7eecab4db0963842498) chore(fmt): zig fmt build.zig to pass test (0xDVC)
- [`44a2d87`](https://github.com/ghostty-org/ghostty/commit/44a2d8740a4a701d3eeded5261035db8e85ff8d7) build: gate lib-vt xcframework on emit-xcframework with xcodebuild detection (0xDVC)
- [`33fc2aa`](https://github.com/ghostty-org/ghostty/commit/33fc2aac97420466137a9b34fe7630f677f1a2e3) cleanups ([@mitchellh](https://github.com/mitchellh))
- [`5f892b6`](https://github.com/ghostty-org/ghostty/commit/5f892b691b8ef887525df16c85fc0cc799e24ec7) ci: fix ([@mitchellh](https://github.com/mitchellh))
- [`d35f02d`](https://github.com/ghostty-org/ghostty/commit/d35f02d83c195f02bf0c333f8af0e7913e0ee673) build: respect config.emit_xcframework for building libghostty-vt.xcframework on Darwin ([#12267](https://github.com/ghostty-org/ghostty/issues/12267)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This fixes a hardcoded build issue on macOS where Zig unconditionally
  forces xcodebuild -create-xcframework to run during compilation, even
  when the caller explicitly specifies that they only want the raw
  standard C objects/headers (-Demit-lib-vt).
  ```
- [`eee1018`](https://github.com/ghostty-org/ghostty/commit/eee10189885c7b730ca1c87d0ef7a8c8d29b4c27) Update VOUCHED list ([#12418](https://github.com/ghostty-org/ghostty/issues/12418)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11461#issuecomment-4315618982)
  from @jcollie.
  
  Vouch: @seyoungjeong
  ```
- [`2f067e1`](https://github.com/ghostty-org/ghostty/commit/2f067e14f15582fe7e13c366f18e952b70f3fd4e) ci: fix vouch-check-issue to checkout the template file ([@trag1c](https://github.com/trag1c))
- [`48ccec1`](https://github.com/ghostty-org/ghostty/commit/48ccec182a932c2ec04c344d45a5fc553861cb13) ci: fix vouch-check-issue to checkout the template file ([#12412](https://github.com/ghostty-org/ghostty/issues/12412)) ([@trag1c](https://github.com/trag1c))
- [`c642e31`](https://github.com/ghostty-org/ghostty/commit/c642e3104bb8b22ab29e2fd700132ed5d62203cf) pkg/highway: Darwin builds don't rely on Apple headers ([@mitchellh](https://github.com/mitchellh))
  ```text
  This uses a custom fork of `hwy/targtes.cpp` that uses an extern
  function written in Zig to use Zig's standard CPU detection to avoid
  a dependency on Apple SDK headers.
  
  This is on the path to removing Apple SDK requirements to build
  libghostty-vt, but will require a lot more work outside of this. The goal
  is to get this out of our external dependencies first and then we can
  work on removing the internal side.
  ```
- [`bdb164a`](https://github.com/ghostty-org/ghostty/commit/bdb164a6e561daa767e3e81f892f221548d5a1da) pkg/highway: expand detection to all platforms not just darwin ([@mitchellh](https://github.com/mitchellh))
- [`f3f9af6`](https://github.com/ghostty-org/ghostty/commit/f3f9af612967154c419b63976bc5b0e718d57ab6) pkg/highway: vendor and modify to remain all libc usage ([@mitchellh](https://github.com/mitchellh))
- [`055922f`](https://github.com/ghostty-org/ghostty/commit/055922faaa6e1e164b3c5306dc25b0e42c49c5c0) more zon2nix update for improved 0.16 compatibility ([@jcollie](https://github.com/jcollie))
- [`3c0b976`](https://github.com/ghostty-org/ghostty/commit/3c0b976d071dab71df687f371c1de0a1eca60b3c) pkg/highway: requires libc headers ([@mitchellh](https://github.com/mitchellh))
- [`00dfd67`](https://github.com/ghostty-org/ghostty/commit/00dfd67beea63148d7779613756200952b0b9ab0) pkg/highway: replace resolveTargetQuery with direct CPU detection ([@mitchellh](https://github.com/mitchellh))
  ```text
  The previous runtime_detect.zig called std.zig.system.resolveTargetQuery
  which pulled in the entire Zig target/CPU model table infrastructure for
  every architecture (~4,000 symbols, ~175 KB of data tables, ~130 KB of
  code). This bloated the binary by ~500 KB and shifted code layout enough
  to cause a measurable icache/branch-predictor regression in unrelated
  hot paths like the terminal parser (~20% more cycles for identical
  instruction counts).
  
  Replace with minimal, direct CPU feature detection per architecture:
  CPUID + XGETBV inline assembly on x86, sysctlbyname on Darwin AArch64,
  and getauxval/prctl via std.os.linux (direct syscalls, no libc) on
  Linux for AArch64, PPC, S390x, RISC-V, and LoongArch.
  
  Split into per-architecture files under src/detect/ for
  maintainability.
  ```
- [`bf3047b`](https://github.com/ghostty-org/ghostty/commit/bf3047b9b21972acc1f017a930e9b3ed6048e037) benchmark: isolate parser hot loop from code-layout shifts ([@mitchellh](https://github.com/mitchellh))
  ```text
  Extract the tight per-byte parsing loop from TerminalParser.step into
  a separate noinline function (parseAll). This eliminates a ~20%
  benchmark regression that appeared after the highway vendor changes
  despite zero changes to the parser source code.
  
  The root cause: the parser benchmark processes 50 MB of input through
  a byte-at-a-time DFA loop that is highly sensitive to instruction
  cache-line placement on Apple Silicon. The M-series cores fetch
  aligned 16-byte blocks; when the loop head lands near the end of a
  64-byte cache line (offset 60), only one instruction fits in the
  first fetch versus four when aligned to offset 48. This causes ~29%
  more cycles for identical instruction counts.
  
  Previously the loop was inlined into the large step() function, so
  any code change anywhere in the binary (like the highway vendor
  restructuring) could shift the loop across a cache-line boundary.
  By making parseAll noinline, the loop gets its own function placement
  that is stable regardless of surrounding code changes.
  ```
- [`5f43437`](https://github.com/ghostty-org/ghostty/commit/5f43437576ce1bf88a9a8236d6df0753ec13ce15) pkg/highway: no libc requirement ([#12402](https://github.com/ghostty-org/ghostty/issues/12402)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This uses a custom fork Google Highway that removes all libc usage. For
  most, it was logging and we can just remove it. For detection, we moved
  this to an extern func implemented in Zig built using the Zig standard
  library so we can avoid libc.
  
  # Benchmark Results
  
  All benchmarks use 50 MB pre-generated inputs (`ghostty-gen +utf8
  --seed=42`)
  built and run with `-Doptimize=ReleaseFast` on Apple Silicon
  (aarch64-macos).
  
  ## Input Descriptions
  
  | Input | Description |
  |:------|:------------|
  | ascii-only | 1-byte sequences only, printable ASCII |
  | 2byte-only | 2-byte sequences only (Latin/Cyrillic/etc.) |
  | 3byte-only | 3-byte sequences only (CJK/BMP) |
  | 4byte-only | 4-byte sequences only (emoji/supplementary planes) |
  | mixed-equal | Equal weight across all 4 lengths |
  | mostly-ascii | ~80% ASCII, ~20% multibyte |
  | cjk-heavy | ~80% 3-byte, ~20% other |
  | 10pct-invalid | Equal-weight mix with 10% malformed sequences |
  
  ## Terminal Parser (byte-by-byte DFA, no SIMD)
  
  | Input | Mean [ms] | Min [ms] | Max [ms] | Relative |
  |:------|----------:|---------:|---------:|---------:|
  | ascii-only | 46.3 ± 0.8 | 45.4 | 48.1 | 1.00 |
  | 2byte-only | 59.1 ± 1.2 | 57.8 | 62.7 | 1.28 ± 0.03 |
  | 3byte-only | 65.4 ± 2.1 | 64.1 | 78.6 | 1.41 ± 0.05 |
  | 4byte-only | 59.3 ± 1.3 | 57.2 | 63.5 | 1.28 ± 0.04 |
  | mixed-equal | 180.7 ± 0.7 | 179.5 | 182.3 | 3.90 ± 0.07 |
  | mostly-ascii | 59.3 ± 1.0 | 57.3 | 61.1 | 1.28 ± 0.03 |
  | cjk-heavy | 142.4 ± 2.0 | 140.4 | 149.9 | 3.08 ± 0.07 |
  | 10pct-invalid | 180.2 ± 1.5 | 178.4 | 184.9 | 3.89 ± 0.08 |
  
  ## Terminal Stream (SIMD UTF-8 decode + terminal handling)
  
  | Input | Mean [ms] | Min [ms] | Max [ms] | Relative |
  |:------|----------:|---------:|---------:|---------:|
  | ascii-only | 377.0 ± 8.7 | 357.1 | 386.4 | 2.42 ± 0.08 |
  | 2byte-only | 664.5 ± 4.0 | 656.9 | 672.6 | 4.27 ± 0.11 |
  | 3byte-only | 233.5 ± 0.9 | 231.1 | 234.8 | 1.50 ± 0.04 |
  | 4byte-only | 155.5 ± 4.0 | 149.6 | 161.3 | 1.00 |
  | mixed-equal | 467.0 ± 3.4 | 461.8 | 473.9 | 3.00 ± 0.08 |
  | mostly-ascii | 470.8 ± 7.2 | 459.6 | 482.8 | 3.03 ± 0.09 |
  | cjk-heavy | 338.4 ± 2.4 | 334.3 | 341.7 | 2.18 ± 0.06 |
  | 10pct-invalid | 635.1 ± 3.5 | 630.5 | 640.8 | 4.08 ± 0.11 |
  
  ## Branch Comparison: `main` vs `fixed`
  
  ### Terminal Parser
  
  | Input | main [ms] | fixed [ms] | Δ |
  |:------|----------:|-----------:|:--|
  | ascii-only | 46.9 ± 0.7 | 47.3 ± 0.9 | ~same |
  | 2byte-only | 59.0 ± 0.5 | 59.1 ± 1.2 | ~same |
  | 3byte-only | 65.9 ± 2.1 | 65.4 ± 2.1 | ~same |
  | 4byte-only | 58.8 ± 0.5 | 59.3 ± 1.3 | ~same |
  | mixed-equal | 182.5 ± 0.9 | 180.7 ± 0.7 | fixed 1% faster |
  | mostly-ascii | 59.0 ± 0.5 | 59.3 ± 1.0 | ~same |
  | cjk-heavy | 144.1 ± 1.7 | 142.4 ± 2.0 | ~same |
  | 10pct-invalid | 181.7 ± 1.0 | 180.2 ± 1.5 | ~same |
  
  ### Terminal Stream
  
  | Input | main [ms] | fixed [ms] | Δ |
  |:------|----------:|-----------:|:--|
  | ascii-only | 388.4 ± 8.8 | 383.1 ± 7.6 | ~same |
  | 2byte-only | 687.7 ± 4.8 | 672.9 ± 2.6 | fixed 2% faster |
  | 3byte-only | 235.5 ± 1.2 | 236.3 ± 2.5 | ~same |
  | 4byte-only | 166.2 ± 2.9 | 159.9 ± 3.1 | fixed 4% faster |
  | mixed-equal | 481.8 ± 3.3 | 480.7 ± 6.3 | ~same |
  | mostly-ascii | 483.8 ± 6.7 | 475.9 ± 4.3 | ~same |
  | cjk-heavy | 341.7 ± 3.1 | 341.6 ± 2.0 | ~same |
  | 10pct-invalid | 647.6 ± 3.3 | 640.4 ± 3.4 | ~same |
  
  No regressions in either benchmark. Fixed branch is equal or slightly
  faster
  across all inputs.
  
  ## Reproduction
  
  ```bash
  # Generate inputs (do NOT regenerate when comparing branches)
  for profile in \
    "--weight-one=1 --weight-two=0 --weight-three=0 --weight-four=0 --ascii-printable-only=true" \
    "--weight-one=0 --weight-two=1 --weight-three=0 --weight-four=0" \
    "--weight-one=0 --weight-two=0 --weight-three=1 --weight-four=0" \
    "--weight-one=0 --weight-two=0 --weight-three=0 --weight-four=1" \
    "--weight-one=1 --weight-two=1 --weight-three=1 --weight-four=1" \
    "--weight-one=10 --weight-two=1 --weight-three=1 --weight-four=0.5 --ascii-printable-only=true" \
    "--weight-one=1 --weight-two=0.5 --weight-three=10 --weight-four=0.5" \
    "--weight-one=1 --weight-two=1 --weight-three=1 --weight-four=1 --invalid-rate=0.1"; do
    ghostty-gen +utf8 --seed=42 $profile | head -c 50000000 > /tmp/ghostty-bench-data/<name>.dat
  done
  
  # Build
  zig build -Demit-bench -Doptimize=ReleaseFast -Demit-macos-app=false
  
  # Run
  hyperfine --warmup 3 --min-runs 10 \
    './zig-out/bin/ghostty-bench +terminal-stream --data=<path>'
  ```
  ````
- [`b0d359c`](https://github.com/ghostty-org/ghostty/commit/b0d359cbbd945f9f3807327526ef79fcaf0477df) more zon2nix update for improved 0.16 compatibility ([#12405](https://github.com/ghostty-org/ghostty/issues/12405)) ([@mitchellh](https://github.com/mitchellh))

