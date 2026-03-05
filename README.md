> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: March 5, 2026 at 15:17 UTC.

## March 5, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22723550848), [2](https://github.com/ghostty-org/ghostty/actions/runs/22723016503), [3](https://github.com/ghostty-org/ghostty/actions/runs/22722387895), [4](https://github.com/ghostty-org/ghostty/actions/runs/22707501732), [5](https://github.com/ghostty-org/ghostty/actions/runs/22704188724), [6](https://github.com/ghostty-org/ghostty/actions/runs/22703620859), [7](https://github.com/ghostty-org/ghostty/actions/runs/22703142519), [8](https://github.com/ghostty-org/ghostty/actions/runs/22702479466)  
Summary: 8 runs • 16 commits • 8 authors

### Changes

- [`e1f4ee7`](https://github.com/ghostty-org/ghostty/commit/e1f4ee7fdd4d5fc4b6b86dd70986be75a0bacabd) Update VOUCHED list ([#11192](https://github.com/ghostty-org/ghostty/issues/11192)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11184#discussioncomment-16011801)
  from @mitchellh.
  
  Vouch: @mac0ne
  ```
- [`f36b903`](https://github.com/ghostty-org/ghostty/commit/f36b903479f54fc7202a95ca10509f3eac06e007) Update VOUCHED list ([#11191](https://github.com/ghostty-org/ghostty/issues/11191)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11190#issuecomment-4005537826)
  from @00-kat.
  
  Vouch: @AnthonyZhOon
  ```
- [`e07aefa`](https://github.com/ghostty-org/ghostty/commit/e07aefa6010716ccc51c745b8e0dde9598b58812) fix: zsh shell integration when `sudo` and `ssh` aliases are defined ([@Michielvk](https://github.com/Michielvk))
- [`42540f4`](https://github.com/ghostty-org/ghostty/commit/42540f44cd717a0e1169fb5008443c6ebb9a073d) fix: zsh shell integration when `sudo` and `ssh` aliases are defined ([#11185](https://github.com/ghostty-org/ghostty/issues/11185)) ([@jparise](https://github.com/jparise))
  ````text
  I encountered an issue related to
  https://github.com/ghostty-org/ghostty/discussions/8641 and
  https://github.com/ghostty-org/ghostty/pull/8647, but in `zsh` instead
  of `bash`.
  
  One of my aliases is:
  
  ```bash
  alias sudo='sudo '
  ```
  
  Which causes following error when sourcing the zsh shell integrations:
  
  ```shell
  source /usr/share/ghostty/shell-integration/zsh/ghostty-integration
  /usr/share/ghostty/shell-integration/zsh/ghostty-integration:149: defining function based on alias `sudo'
  /usr/share/ghostty/shell-integration/zsh/ghostty-integration:233: parse error near `()'
  ```
  ````
- [`c920a88`](https://github.com/ghostty-org/ghostty/commit/c920a88cdcc19ed42ab013c1ba2bb9ad41592ada) GTK: add 'move' to the drop target actions ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes #11175
  ```
- [`dd575c7`](https://github.com/ghostty-org/ghostty/commit/dd575c716077e0e2d12881fe0c5f65b067978176) GTK: add 'move' to the drop target actions ([#11182](https://github.com/ghostty-org/ghostty/issues/11182)) ([@pluiedev](https://github.com/pluiedev))
  ```text
  Fixes #11175
  ```
- [`2fe5515`](https://github.com/ghostty-org/ghostty/commit/2fe55152ca6fe74219f129ee6339b265a41d0252) i18n: add Vietnamese translation ([@anhthang](https://github.com/anhthang))
- [`4d30d88`](https://github.com/ghostty-org/ghostty/commit/4d30d886c636305875748b84ec06d489af669921) update translation ([@anhthang](https://github.com/anhthang))
- [`e2a01be`](https://github.com/ghostty-org/ghostty/commit/e2a01beca7bed7974f1e700cef1ad0eecea2d13d) Merge branch 'main' into vi_VN ([@anhthang](https://github.com/anhthang))
- [`0b802e7`](https://github.com/ghostty-org/ghostty/commit/0b802e7c2e228b246bb0daee925ab87f66c6ec5c) i18n: add Vietnamese translation ([#8912](https://github.com/ghostty-org/ghostty/issues/8912)) ([@00-kat](https://github.com/00-kat))
  ```text
  Adds support for the Vietnamese language
  ```
- [`3dde6e2`](https://github.com/ghostty-org/ghostty/commit/3dde6e2559e0aa67e04a6001485d87b80ed4c1dd) terminal: bound link regex search work with Oniguruma retry limits ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11177
  
  Use per-search Oniguruma match params (retry_limit_in_search) in
  StringMap-backed link detection to avoid pathological backtracking hangs
  on very long lines.
  
  The units are ticks in the internal loop so its kind of opaque but
  this seems to still match some very long URLs. The test case in question
  was a 169K character line (which is now rejected).
  ```
- [`fe1e25f`](https://github.com/ghostty-org/ghostty/commit/fe1e25f7a6cec06c45f3c11ef8cc259a617697d4) terminal: bound link regex search work with Oniguruma retry limits ([#11181](https://github.com/ghostty-org/ghostty/issues/11181)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11177
  
  Use per-search Oniguruma match params (retry_limit_in_search) in
  StringMap-backed link detection to avoid pathological backtracking hangs
  on very long lines.
  
  The units are ticks in the internal loop so its kind of opaque but this
  seems to still match some very long URLs. The test case in question was
  a 169K character line (which is now rejected).
  ```
- [`961bf46`](https://github.com/ghostty-org/ghostty/commit/961bf46884dc7f75a4bfd8640bf7f57baed6b540) Fix Windows test in src/Command.zig ([@jcollie](https://github.com/jcollie))
  ```text
  This was introduced in #10611. This doesn't fix all of the current
  Windows build problems, but at least fixes one that I introduced.
  ```
- [`320d9c2`](https://github.com/ghostty-org/ghostty/commit/320d9c2f1cba79a8a9ab32c4d8c337571e435c20) Fix Windows test in src/Command.zig ([#11180](https://github.com/ghostty-org/ghostty/issues/11180)) ([@jcollie](https://github.com/jcollie))
  ```text
  This was introduced in #10611. This doesn't fix all of the current
  Windows build problems, but at least fixes one that I introduced.
  ```
- [`dfa968d`](https://github.com/ghostty-org/ghostty/commit/dfa968d932ecb6928ebab9a9d460ae0ac629f985) Update VOUCHED list ([#11176](https://github.com/ghostty-org/ghostty/issues/11176)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11175#issuecomment-4001807388)
  from @jcollie.
  
  Vouch: @douglas
  ```
- [`a5327a5`](https://github.com/ghostty-org/ghostty/commit/a5327a51f3fedea890f59ad75e7666a57bb743c4) Update VOUCHED list ([#11179](https://github.com/ghostty-org/ghostty/issues/11179)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11164#discussioncomment-16005149)
  from @mitchellh.
  
  Vouch: @Michielvk
  ```

## March 4, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22694000891), [2](https://github.com/ghostty-org/ghostty/actions/runs/22691416275), [3](https://github.com/ghostty-org/ghostty/actions/runs/22685396526), [4](https://github.com/ghostty-org/ghostty/actions/runs/22684084893), [5](https://github.com/ghostty-org/ghostty/actions/runs/22678614686), [6](https://github.com/ghostty-org/ghostty/actions/runs/22654900798)  
Summary: 6 runs • 30 commits • 9 authors

### Changes

- [`6961c22`](https://github.com/ghostty-org/ghostty/commit/6961c2265e3b760dda9146aa285f11eee1e16abe) gtk: `+new-window` now respects `--working-directory` and `-e` ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes: #8862
  Fixes: #10716
  
  This adds the machinery to pass configuration settings received over
  DBus down to the GObject Surface so that that configuration information
  can be used to override some settings from the current "live" config
  when creating a new window. Currently it's only possible to override
  `--working-directory` and `--command`. `-e` on the `ghostty +new-window`
  CLI works as well.
  
  Adding more overridable settings is possible, but being able to fully
  override any possible setting would better be served with a major
  revamp of how Ghostty handles configs, which I is way out of scope at
  the moment.
  ```
- [`ec0f9ef`](https://github.com/ghostty-org/ghostty/commit/ec0f9ef4163ee8262a31c779a9062c21b7486d5c) gtk: `+new-window` now respects `--title` ([@jcollie](https://github.com/jcollie))
- [`f2ce7c3`](https://github.com/ghostty-org/ghostty/commit/f2ce7c348edbd635dd74cae9b3b330825768ba76) gtk: `+new-window` document `--title` ([@jcollie](https://github.com/jcollie))
- [`002a6cc`](https://github.com/ghostty-org/ghostty/commit/002a6cc76526240b19cee9792a79de05077bb09a) gtk: use simpler method for passing overrides around ([@jcollie](https://github.com/jcollie))
  ```text
  As discussed in Discord, this commit drops the `ConfigOverride` object
  in favor of a simpler method of passing the overrides around. Completely
  avoiding changes to the core wasn't possible but it's very minimal now.
  ```
- [`e27956f`](https://github.com/ghostty-org/ghostty/commit/e27956fdde1b3964d689f8f0c038b29f6e7d5157) gtk: remove modifications to the core for overrides ([@jcollie](https://github.com/jcollie))
- [`5bc5820`](https://github.com/ghostty-org/ghostty/commit/5bc5820f3255cc8dfbf6c30e3f7edb4a947add3d) gtk: simplify new-window action memory management with an arena ([@jcollie](https://github.com/jcollie))
- [`58d6021`](https://github.com/ghostty-org/ghostty/commit/58d6021ec44c2383344f2c08214ebe3dd754ea4d) apprt/gtk: reduce split-tree flicker by reusing leaf widgets ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #8208
  
  Split-tree updates currently clear `tree_bin` and then wait for every surface
  to become parentless before rebuilding. That leaves the split area blank for
  one or more frames, which is the visible flicker during split create/close/
  resize/equalize actions.
  
  Keep the previous widget tree attached until the idle rebuild runs, then
  swap in the rebuilt tree in one step. During rebuild, reuse existing
  leaf widgets by detaching and reparenting them into the new `GtkPaned`
  hierarchy instead of recreating wrappers for every leaf.
  
  This removes the parent-settling rebuild path and avoids transient blank
  frames while preserving debounced rebuild behavior.
  ```
- [`436a11d`](https://github.com/ghostty-org/ghostty/commit/436a11dd59598ddfcc74434cd6283017753eed0f) apprt/gtk: reduce split-tree flicker by reusing leaf widgets ([#11170](https://github.com/ghostty-org/ghostty/issues/11170)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #8208
  
  Split-tree updates currently clear `tree_bin` and then wait for every
  surface to become parentless before rebuilding. That leaves the split
  area blank for one or more frames, which is the visible flicker during
  split create/close/ resize/equalize actions.
  
  Keep the previous widget tree attached until the idle rebuild runs, then
  swap in the rebuilt tree in one step. During rebuild, reuse existing
  leaf widgets by detaching and reparenting them into the new `GtkPaned`
  hierarchy instead of recreating wrappers for every leaf.
  
  This removes the parent-settling rebuild path and avoids transient blank
  frames while preserving debounced rebuild behavior.
  ```
- [`46522a8`](https://github.com/ghostty-org/ghostty/commit/46522a8779ba44e47d4f68ab633ace5382971624) gtk: `+new-window` now respects `--working-directory` and `-e` ([#10809](https://github.com/ghostty-org/ghostty/issues/10809)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes: #8862
  Fixes: #10716
  
  This adds the machinery to pass configuration settings received over
  DBus down to the GObject Surface so that that configuration information
  can be used to override some settings from the current "live" config
  when creating a new window. Currently it's only possible to override
  `--working-directory`, `--command`, and `--title`. `-e` on the `ghostty
  +new-window` CLI works as well.
  
  Adding more overridable settings is possible, but being able to fully
  override any possible setting would better be served with a major revamp
  of how Ghostty handles configs, which is way out of scope at the moment.
  ```
- [`05807f0`](https://github.com/ghostty-org/ghostty/commit/05807f0d72d44ba24048cce56bf716d2c629ff30) Revert "build: link to the system FontConfig by default on non-macOS systems ([#11152](https://github.com/ghostty-org/ghostty/issues/11152))" ([@mitchellh](https://github.com/mitchellh))
  ```text
  This reverts commit ee4c6f88c5517d242b73427f66da4d54d41e35a8.
  ```
- [`57d877a`](https://github.com/ghostty-org/ghostty/commit/57d877a0d622a01381688cbafd8d227612640fc7) Revert "build: link to the system FontConfig by default on non-macOS systems" ([@mitchellh](https://github.com/mitchellh))
  ```text
  This reverts commit 89f9dd7848111b28287a70388d610d66227a53f4.
  ```
- [`2cfc9d3`](https://github.com/ghostty-org/ghostty/commit/2cfc9d36d8ea81722d9ecfad027ba8558879b780) Revert "build: link to the system FontConfig by default ([#11169](https://github.com/ghostty-org/ghostty/issues/11169)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This reverts commit ee4c6f88c5517d242b73427f66da4d54d41e35a8.
  
  This breaks standard `zig build run` from a dev shell in Nix/NixOS. I
  think we need to rethink some of the protections here, possibly only to
  apply to packaging/release modes or something.
  
  cc @jcollie
  ```
- [`9a3dbe1`](https://github.com/ghostty-org/ghostty/commit/9a3dbe10b05912ee30061dae6d730d8d9db0bc46) zsh: fix extra newlines with leading-newline prompts ([@jparise](https://github.com/jparise))
  ```text
  In our multiline prompt logic, skip the newline immediately after the
  first mark to avoid introducing a double newline due to OSC 133;A's
  fresh-line behavior.
  
  Fixes: #11003
  ```
- [`9386fa6`](https://github.com/ghostty-org/ghostty/commit/9386fa64997db6124f1cdbd4730938edb49f2a85) zsh: emit missing prompt markers in line-init ([@jparise](https://github.com/jparise))
  ```text
  Emit semantic prompt markers at line-init if PS1 doesn't contain our
  marks. This ensures the terminal sees prompt markers even if another
  plugin (like zinit or oh-my-posh) regenerated PS1 after our precmd ran.
  We use 133;P instead of 133;A to avoid fresh-line behavior which would
  disrupt the display since the prompt has already been drawn. We also
  emit 133;B to mark the input area, which is needed for click-to-move.
  
  Fixes: #10555
  ```
- [`3ee8ef4`](https://github.com/ghostty-org/ghostty/commit/3ee8ef4f650f550698ee1e8e81e591511e195bf4) macos: suppress split-focus click mouse reports ([@rockorager](https://github.com/rockorager))
  ```text
  Amp-Thread-ID: https://ampcode.com/threads/T-019cb9fe-b11b-753f-99e7-8ecc52b73ec4
  ```
- [`0fa12f8`](https://github.com/ghostty-org/ghostty/commit/0fa12f89151d5332233c97308bdda8925f6627b9) gtk: suppress mouse reports on focus-transfer clicks ([@rockorager](https://github.com/rockorager))
  ```text
  Amp-Thread-ID: https://ampcode.com/threads/T-019cb9fe-b11b-753f-99e7-8ecc52b73ec4
  ```
- [`d146808`](https://github.com/ghostty-org/ghostty/commit/d1468086efcb7ae83498c4660ecfa5c3aebd8b6a) macos: defer key-window focus sync to reduce churn ([@rockorager](https://github.com/rockorager))
  ```text
  Amp-Thread-ID: https://ampcode.com/threads/T-019cb9fe-b11b-753f-99e7-8ecc52b73ec4
  ```
- [`3bcf329`](https://github.com/ghostty-org/ghostty/commit/3bcf329c2b5894e64e129542742db305a51d463e) zsh: emit missing prompt markers in line-init ([#11165](https://github.com/ghostty-org/ghostty/issues/11165)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Emit semantic prompt markers at line-init if PS1 doesn't contain our
  marks. This ensures the terminal sees prompt markers even if another
  plugin (like zinit or oh-my-posh) regenerated PS1 after our precmd ran.
  We use 133;P instead of 133;A to avoid fresh-line behavior which would
  disrupt the display since the prompt has already been drawn. We also
  emit 133;B to mark the input area, which is needed for click-to-move.
  
  Fixes: #10572, #10555
  ```
- [`226d0b9`](https://github.com/ghostty-org/ghostty/commit/226d0b9918b6c6149d21f79a05a432d4c10da0bf) zsh: fix extra newlines with leading-newline prompts ([#11166](https://github.com/ghostty-org/ghostty/issues/11166)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  In our multiline prompt logic, skip the newline immediately after the
  first mark to avoid introducing a double newline due to OSC 133;A's
  fresh-line behavior.
  
  Fixes: #11003
  ```
- [`c3febab`](https://github.com/ghostty-org/ghostty/commit/c3febabd286dfaa47c3d7d251ede22e8e382b6f3) apprt: unify split-click focus behavior across macOS and GTK; suppress focus-transfer mouse events ([#11167](https://github.com/ghostty-org/ghostty/issues/11167)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Summary
  
  This PR aligns split-pane click behavior across macOS and GTK when focus
  changes due to click.
  
  When a left-click is used to transfer focus (window activation or
  switching to another split), Ghostty now treats that click as focus-only
  and suppresses forwarding mouse press/release events for that
  focus-transfer click.
  
  ## Changes
  
  1. macOS: suppress focus-transfer left mouse-down and matching mouse-up
  in `SurfaceView_AppKit.swift`.
  1. GTK: suppress focus-transfer left mouse-down and matching mouse-up in
  `src/apprt/gtk/class/surface.zig`.
  1. macOS: defer key-window focus sync to next runloop tick to reduce
  transient focus churn in `BaseTerminalController.swift`.
  1. macOS build/lint: exclude generated/dependency paths from SwiftLint
  during build in `.swiftlint.yml` and
  `Ghostty.xcodeproj/project.pbxproj`.
  
  ## Behavior
  
  1. Focus-transfer split clicks are now focus-only on both macOS and GTK.
  1. Matching release is also suppressed for those clicks, avoiding
  release-without-press sequences.
  1. Platform behavior is consistent for split focus transitions.
  
  ## Validation
  
  1. Built macOS target with `xcodebuild -target Ghostty -configuration
  Debug -arch arm64`.
  1. Ran targeted Zig test command `zig build test
  -Dtest-filter=computeFraction`.
  1. Ran format/lint for touched files (`swiftlint lint --fix`, `zig
  fmt`).
  4. Build and (human) tested click scenarios on macOS
  
  ## AI Disclosure
  
  AI-assisted.
  
  Thread:
  https://ampcode.com/threads/T-019cb9fe-b11b-753f-99e7-8ecc52b73ec4
  ```
- [`2772c90`](https://github.com/ghostty-org/ghostty/commit/2772c90885d2ffc27fdf5e7e758c5ecca2af6f8c) i18n: add Kazakh translation (kk) ([@crayxt](https://github.com/crayxt))
- [`0797b28`](https://github.com/ghostty-org/ghostty/commit/0797b281ec0268f2df65399b1aede85eaea0d31a) Add Kazakh translation ([#10670](https://github.com/ghostty-org/ghostty/issues/10670)) ([@00-kat](https://github.com/00-kat))
  ```text
  Dear maintainers,
  
  This PR adds Kazakh language translation file and necessary edits to
  CODEOWNERS and i18n file with the list of locales.
  
  Please review (and squash when committing)
  
  Thank you!
  ```
- [`a716b9c`](https://github.com/ghostty-org/ghostty/commit/a716b9c4d421a3ab94f93fe301ddc28a5a086361) macos: Ghostty.Shell.escape unit tests ([@jparise](https://github.com/jparise))
- [`53ef422`](https://github.com/ghostty-org/ghostty/commit/53ef42266a422c23b1523a3347caf7433fb63983) macos: Ghostty.Shell.escape unit tests ([#11162](https://github.com/ghostty-org/ghostty/issues/11162)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  *AI Disclosure:* These were written using the Claude Agent in Xcode
  26.3, partly as an excuse to try out that latest integration.
  ```
- [`b215291`](https://github.com/ghostty-org/ghostty/commit/b2152919141de84a71052dd6f298d24dc1b08d63) macos: implement audio bell support with bell-audio-path ([@alaasdk](https://github.com/alaasdk))
  ```text
  Extends the macOS bell implementation to support the `audio` bell
  feature by playing a user-specified audio file via NSSound.
  
  Previously, macOS only supported the `system` feature (NSSound.beep()).
  This change adds support for:
  - `audio` bell feature: plays the file at `bell-audio-path` using
    NSSound, respecting the `bell-audio-volume` setting
  - Adds `cval()` to the `Path` type so it can be returned via the C API
  
  Also removes the "(GTK only)" restriction from `bell-audio-path` and
  `bell-audio-volume` documentation, as these options now work on macOS.
  
  Example config:
    bell-features = audio
    bell-audio-path = /System/Library/Sounds/Glass.aiff
    bell-audio-volume = 0.8
  ```
- [`c93cf52`](https://github.com/ghostty-org/ghostty/commit/c93cf521088594649a6c2d54e1c916c3906c0a0f) Update VOUCHED list ([#11156](https://github.com/ghostty-org/ghostty/issues/11156)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/10982#discussioncomment-15990906)
  from @jcollie.
  
  Vouch: @cmwetherell
  ```
- [`69df92b`](https://github.com/ghostty-org/ghostty/commit/69df92b56a85d1ae883dc8f034fb19665161c498) build(deps): bump cachix/install-nix-action from 31.9.1 to 31.10.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [cachix/install-nix-action](https://github.com/cachix/install-nix-action) from 31.9.1 to 31.10.0.
  - [Release notes](https://github.com/cachix/install-nix-action/releases)
  - [Changelog](https://github.com/cachix/install-nix-action/blob/master/RELEASE.md)
  - [Commits](https://github.com/cachix/install-nix-action/compare/2126ae7fc54c9df00dd18f7f18754393182c73cd...19effe9fe722874e6d46dd7182e4b8b7a43c4a99)
  
  ---
  updated-dependencies:
  - dependency-name: cachix/install-nix-action
    dependency-version: 31.10.0
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`73ce40c`](https://github.com/ghostty-org/ghostty/commit/73ce40c6235af6028dac5dfd4502b50c779b7bf5) build(deps): bump cachix/install-nix-action from 31.9.1 to 31.10.0 ([#11157](https://github.com/ghostty-org/ghostty/issues/11157)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [cachix/install-nix-action](https://github.com/cachix/install-nix-action)
  from 31.9.1 to 31.10.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/cachix/install-nix-action/releases">cachix/install-nix-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v31.10.0</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>nix: 2.33.3 -&gt; 2.34.0 by <a
  href="https://github.com/github-actions"><code>@​github-actions</code></a>[bot]
  in <a
  href="https://redirect.github.com/cachix/install-nix-action/pull/267">cachix/install-nix-action#267</a>
  Release notes: <a
  href="https://discourse.nixos.org/t/nix-2-34-0-released/75818">https://discourse.nixos.org/t/nix-2-34-0-released/75818</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/cachix/install-nix-action/compare/v31.9.1...v31.10.0">https://github.com/cachix/install-nix-action/compare/v31.9.1...v31.10.0</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/19effe9fe722874e6d46dd7182e4b8b7a43c4a99"><code>19effe9</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/install-nix-action/issues/267">#267</a>
  from cachix/create-pull-request/patch</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/d3f3b99dd19236cb244609944767f2864ec646ee"><code>d3f3b99</code></a>
  nix: 2.33.3 -&gt; 2.34.0</li>
  <li>See full diff in <a
  href="https://github.com/cachix/install-nix-action/compare/2126ae7fc54c9df00dd18f7f18754393182c73cd...19effe9fe722874e6d46dd7182e4b8b7a43c4a99">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=cachix/install-nix-action&package-manager=github_actions&previous-version=31.9.1&new-version=31.10.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`98ad1d9`](https://github.com/ghostty-org/ghostty/commit/98ad1d955cf8d66cf5548f581a6502cf10f2f852) use proper type for optional path ([@mitchellh](https://github.com/mitchellh))
- [`619e33a`](https://github.com/ghostty-org/ghostty/commit/619e33a4febec871c0d655f51d85e7f5f21ba289) macos: implement audio bell support with bell-audio-path ([#11154](https://github.com/ghostty-org/ghostty/issues/11154)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  ## Summary
  
  This extends the macOS bell implementation to support the `audio` bell
  feature, bringing it to parity with GTK/Linux.
  
  Previously, macOS only had the `system` feature (`NSSound.beep()`). This
  PR adds:
  
  - **`audio` bell feature on macOS**: plays the file at `bell-audio-path`
  using `NSSound(contentsOfFile:)`, respecting `bell-audio-volume`
  - **`cval()` on the `Path` type**: allows `Path` values (a union type)
  to be returned through the C API, which is needed for Swift to read
  `bell-audio-path`
  - **Removes `(GTK only)` restriction** from `bell-audio-path` and
  `bell-audio-volume` documentation
  
  ## How it works
  
  In `AppDelegate.swift`, when the bell rings and the `audio` feature is
  enabled, Ghostty now:
  1. Reads `bell-audio-path` from config
  2. Loads it as an `NSSound`
  3. Applies `bell-audio-volume` and plays it
  
  Falls back gracefully if the path is not set or the file cannot be
  loaded.
  
  ## Example config
  
  ```
  bell-features = audio
  bell-audio-path = /System/Library/Sounds/Glass.aiff
  bell-audio-volume = 0.8
  ```
  
  ## Testing
  
  - Set `bell-features = audio` and `bell-audio-path` to any valid audio
  file
  - Trigger a bell with `echo -e '\a'`
  - Audio should play at the configured volume
  ````

## March 3, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22645694880), [2](https://github.com/ghostty-org/ghostty/actions/runs/22644801904), [3](https://github.com/ghostty-org/ghostty/actions/runs/22643251900), [4](https://github.com/ghostty-org/ghostty/actions/runs/22634551065), [5](https://github.com/ghostty-org/ghostty/actions/runs/22633830469), [6](https://github.com/ghostty-org/ghostty/actions/runs/22632962784), [7](https://github.com/ghostty-org/ghostty/actions/runs/22630103557), [8](https://github.com/ghostty-org/ghostty/actions/runs/22608444462), [9](https://github.com/ghostty-org/ghostty/actions/runs/22607408000), [10](https://github.com/ghostty-org/ghostty/actions/runs/22603105482)  
Summary: 10 runs • 26 commits • 8 authors

### Changes

- [`205c05d`](https://github.com/ghostty-org/ghostty/commit/205c05d59d016222b350b63dd10f8745b1a5d831) macos: passthrough mouse down event to TabTitleEditor if needed ([@bo2themax](https://github.com/bo2themax))
- [`6614708`](https://github.com/ghostty-org/ghostty/commit/661470897e878b766254e59f30531192d7ae2771) macos: passthrough right mouse down event to TabTitleEditor if needed ([@bo2themax](https://github.com/bo2themax))
- [`78fdff3`](https://github.com/ghostty-org/ghostty/commit/78fdff34a969d3864ae5a471f673a19ab5e064cf) macos: hide close button when editing tab title ([@bo2themax](https://github.com/bo2themax))
- [`4437707`](https://github.com/ghostty-org/ghostty/commit/44377071323b629480a367abf80862a1d7b084b0) macos: use a separated struct to hide and restore tab states ([@bo2themax](https://github.com/bo2themax))
- [`4c83872`](https://github.com/ghostty-org/ghostty/commit/4c838723173da757a16a2f3afd4c94f16732ef6a) macOS: Refine tab title editing ([#11150](https://github.com/ghostty-org/ghostty/issues/11150)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  - Pass through mouse down event to `TabTitleEditor` if needed
  - Pass through right mouse down event to `TabTitleEditor` if needed
  - Hide close button when editing tab title
  
  Refactor:
  - Use a separated struct to hide and restore tab states
  
  
  https://github.com/user-attachments/assets/e69838f5-e199-437c-b53b-a491e9d5b752
  ```
- [`0149fd7`](https://github.com/ghostty-org/ghostty/commit/0149fd7139ce76f89357d9ab9bbfba439d1d8445) Update VOUCHED list ([#11155](https://github.com/ghostty-org/ghostty/issues/11155)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11154#issuecomment-3993830083)
  from @mitchellh.
  
  Vouch: @alaasdk
  ```
- [`89f9dd7`](https://github.com/ghostty-org/ghostty/commit/89f9dd7848111b28287a70388d610d66227a53f4) build: link to the system FontConfig by default on non-macOS systems ([@jcollie](https://github.com/jcollie))
  ```text
  Because of the global shared state that FontConfig maintains, FontConfig
  must be linked dynamically to the same system FontConfig shared library
  that GTK uses. Ghostty's default has been changed to always link to the
  system FontConfig library on non-macOS systems. If that is overridden
  (by specifying `-fno-sys=fontconfig` during the build) Ghostty may crash
  when trying to locate glyphs that are not available in the default font.
  
  Fixes #10432
  ```
- [`ee4c6f8`](https://github.com/ghostty-org/ghostty/commit/ee4c6f88c5517d242b73427f66da4d54d41e35a8) build: link to the system FontConfig by default on non-macOS systems ([#11152](https://github.com/ghostty-org/ghostty/issues/11152)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Because of the global shared state that FontConfig maintains, FontConfig
  must be linked dynamically to the same system FontConfig shared library
  that GTK uses. Ghostty's default has been changed to always link to the
  system FontConfig library on non-macOS systems. If that is overridden
  (by specifying `-fno-sys=fontconfig` during the build) Ghostty may crash
  when trying to locate glyphs that are not available in the default font.
  
  Fixes #10432
  ```
- [`fdfc9fe`](https://github.com/ghostty-org/ghostty/commit/fdfc9fea2ff291436685e7ff6158ffbccbc8a36e) input: send composed text in kitty keyboard protocol ([@mitchellh](https://github.com/mitchellh))
  ```text
  When the kitty keyboard protocol "report all keys as escape codes" mode
  was active, composed/IME text (e.g. from dead keys or compose sequences)
  was silently dropped.
  
  This happened because the composed text is sent within our GTK apprt
  with key=unidentified and no unshifted_codepoint, so no kitty entry was
  found and the encoder returned without producing any output. The
  plain-text fallback was also skipped because report_all bypasses it.
  
  Send composed text as raw UTF-8 when no kitty entry is found, matching
  the behavior of Kitty on Linux for me.
  
  Fixes #10049
  ```
- [`2d5bb18`](https://github.com/ghostty-org/ghostty/commit/2d5bb18e29bc9f50eb2783973f5ed4599285ac1b) input: send composed text in kitty keyboard protocol ([#11149](https://github.com/ghostty-org/ghostty/issues/11149)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  When the kitty keyboard protocol "report all keys as escape codes" mode
  was active, composed/IME text (e.g. from dead keys or compose sequences)
  was silently dropped.
  
  This happened because the composed text is sent within our GTK apprt
  with key=unidentified and no unshifted_codepoint, so no kitty entry was
  found and the encoder returned without producing any output. The
  plain-text fallback was also skipped because report_all bypasses it.
  
  Send composed text as raw UTF-8 when no kitty entry is found, matching
  the behavior of Kitty on Linux for me.
  
  Fixes #10049
  ```
- [`d2175d1`](https://github.com/ghostty-org/ghostty/commit/d2175d1b56e2f821745ee5ef08056bc918a43ea2) fuzz: add OSC parser fuzzer ([@mitchellh](https://github.com/mitchellh))
- [`562721e`](https://github.com/ghostty-org/ghostty/commit/562721e6d18a64f267ce1da132df2b236152434c) fuzz: add OSC parser fuzzer ([#11148](https://github.com/ghostty-org/ghostty/issues/11148)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  I'm running this now, 10 minutes with nothing but I figure this is a big
  enough target we should also add this.
  ```
- [`d9d65fd`](https://github.com/ghostty-org/ghostty/commit/d9d65fdb9f20c7190609009717a680c18b977425) fix: calculate cell size before presenting gtk window ([@ajbucci](https://github.com/ajbucci))
- [`0af3477`](https://github.com/ghostty-org/ghostty/commit/0af3477e3540c5ad6748d67d7519a3092e219838) fix: remove max() and magic numbers ([@ajbucci](https://github.com/ajbucci))
- [`733d307`](https://github.com/ghostty-org/ghostty/commit/733d307bf4138fe66b8eff01f1d923941c9fe7f0) gtk: update some comments/function names, take min sizes into account ([@jcollie](https://github.com/jcollie))
- [`e6e5f3f`](https://github.com/ghostty-org/ghostty/commit/e6e5f3ffe18871359a812bdba68fd325e8ecb359) macos: finish editing tab title when the window resigns as key window ([@bo2themax](https://github.com/bo2themax))
- [`c8a0092`](https://github.com/ghostty-org/ghostty/commit/c8a0092301a3274dac0ccb982d4b05fca98d0468) fix: calculate cell size before presenting gtk window ([#10459](https://github.com/ghostty-org/ghostty/issues/10459)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #7937
  
  Added `computeInitialSize` to GTK `Surface` and call it in GTK
  `Application` before the first `present()`, so the window manager
  centers the correct size on initial show.
  
  The issue occurs because the core `Surface.recomputeInitialSize()` runs
  only after the renderer is initialized. In GTK, the `GLArea` isn’t
  realized until after `present()`, so the initial size arrives too late
  for WM centering.
  
  **Limitations**: when we precompute size before `present()` we do not
  have access to padding, so the sizing will be very slightly off... but
  since it is only off a few pixels I was unable to tell visually that it
  wasn't perfectly centered.
  
  **Other thoughts**: I was hesitant to make changes to core `Surface`
  because the issue is Linux-specific, but it may make sense to extract a
  helper from `recomputeInitialSize` to avoid duplicating the sizing math.
  
  **AI Disclosure:** I used AI to explore the project, help with any
  language / API questions (I've never used zig before and rarely use
  gtk), and make implementation suggestions.
  ```
- [`2f0039d`](https://github.com/ghostty-org/ghostty/commit/2f0039d419022cd827d3c7023947c48a478e3137) macos: finish editing tab title when the window resigns as key window ([#11147](https://github.com/ghostty-org/ghostty/issues/11147)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This fixes #11146 and also #10993. Updated the comments added in #11052.
  
  > After finishing editing when the window resigns as the key window,
  using `labelFrame.minY` is fine with the same usage as #10993, but when
  double-clicking with text selected it will move up again 🤷🏻‍♂️.
  
  This makes focus state more accurate with cursor shape on the surface,
  when editing the title for a tab in another window group.
  
  [Incorrect
  example](https://github.com/user-attachments/assets/c3c4e774-a683-44e7-9bb6-3be79ac72ec2)
  ```
- [`4ce782b`](https://github.com/ghostty-org/ghostty/commit/4ce782b63f7348867cb6fd00695740b3970ec77a) terminfo: add support for SGR dim ([@noib3](https://github.com/noib3))
  ```text
  This PR implements the fix discussed in
  https://github.com/ghostty-org/ghostty/discussions/11128
  ```
- [`cb06b9b`](https://github.com/ghostty-org/ghostty/commit/cb06b9b0018508b04702e9a4580963eed8d00cdd) terminfo: add support for SGR dim ([#11144](https://github.com/ghostty-org/ghostty/issues/11144)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This PR implements the fix discussed in
  https://github.com/ghostty-org/ghostty/discussions/11128.
  
  Before:
  
  <img width="818" height="96" alt="before"
  src="https://github.com/user-attachments/assets/788f981f-3d1b-4c60-bf85-0c297641cae7"
  />
  
  After:
  
  <img width="813" height="93" alt="after"
  src="https://github.com/user-attachments/assets/a530015a-053a-4680-9a85-812aa8df3d91"
  />
  ```
- [`bb64692`](https://github.com/ghostty-org/ghostty/commit/bb646926f8c4c242365cd2e915140760f95c1c75) config: respect cursor-click-to-move for OSC133 click to move ([@mitchellh](https://github.com/mitchellh))
  ```text
  When cursor-click-to-move is set to false, disable all prompt
  click-to-move mechanisms including shell-native methods such as OSC 133
  cl= (arrow key synthesis) and click_events.
  
  I forgot to port this config over when we did the OSC133 stuff.
  
  Also update the config documentation to accurately describe the current
  behavior.
  
  Fixes #11138
  ```
- [`2502ca2`](https://github.com/ghostty-org/ghostty/commit/2502ca294efe5aa9722c36e25b2252b0150054e9) config: respect cursor-click-to-move for OSC133 click to move ([#11141](https://github.com/ghostty-org/ghostty/issues/11141)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  When cursor-click-to-move is set to false, disable all prompt
  click-to-move mechanisms including shell-native methods such as OSC 133
  cl= (arrow key synthesis) and click_events.
  
  I forgot to port this config over when we did the OSC133 stuff.
  
  Also update the config documentation to accurately describe the current
  behavior.
  
  Fixes #11138
  ```
- [`391c904`](https://github.com/ghostty-org/ghostty/commit/391c9044bc62bd001ab842e52bde0bd398837823) pkg/afl++: remove @@ from run target since we use in-memory targets ([@mitchellh](https://github.com/mitchellh))
- [`5e7a5cc`](https://github.com/ghostty-org/ghostty/commit/5e7a5cc9c1b4b198e226e2b88df5b3eb66299dcf) pin python depds to latest tag ([@rhodes-b](https://github.com/rhodes-b))
- [`eaa83b8`](https://github.com/ghostty-org/ghostty/commit/eaa83b82b3f637ab1c07ac78ea8e69e3f620cc4d) address comments ([@rhodes-b](https://github.com/rhodes-b))
- [`d3c3770`](https://github.com/ghostty-org/ghostty/commit/d3c37704359cdc863a85a0d67baa8a9cd09f88af) Nix pkgs pin dependencies ([#11121](https://github.com/ghostty-org/ghostty/issues/11121)) ([@pluiedev](https://github.com/pluiedev))

## March 2, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22592783895), [2](https://github.com/ghostty-org/ghostty/actions/runs/22591766134), [3](https://github.com/ghostty-org/ghostty/actions/runs/22583700515), [4](https://github.com/ghostty-org/ghostty/actions/runs/22581513590), [5](https://github.com/ghostty-org/ghostty/actions/runs/22562974731), [6](https://github.com/ghostty-org/ghostty/actions/runs/22562509161), [7](https://github.com/ghostty-org/ghostty/actions/runs/22561514943), [8](https://github.com/ghostty-org/ghostty/actions/runs/22558361524), [9](https://github.com/ghostty-org/ghostty/actions/runs/22558023945), [10](https://github.com/ghostty-org/ghostty/actions/runs/22556024652)  
Summary: 10 runs • 20 commits • 3 authors

### Changes

- [`177612a`](https://github.com/ghostty-org/ghostty/commit/177612a4cf239b2c3d8c36a45c9fa5e9d4a22ba0) terminal: fix insertBlanks orphaned spacer_tail beyond right margin ([@mitchellh](https://github.com/mitchellh))
  ```text
  When insertBlanks clears the entire region from cursor to the right
  margin (scroll_amount == 0), a wide character whose head is at the right
  margin gets cleared but its spacer_tail just beyond the margin is left
  behind, causing a "spacer tail not following wide" page integrity
  violation.
  
  Move the right-margin wide-char cleanup from inside the scroll_amount >
  0 block to before it, so it runs unconditionally — matching the
  rowWillBeShifted pattern of cleaning up boundary-straddling wide chars
  up front.
  
  Found via AFL++ fuzzing. #11109
  ```
- [`5fa42dd`](https://github.com/ghostty-org/ghostty/commit/5fa42dd80235bf3493d4e8d7d6817597d8f3e1c8) Update VOUCHED list ([#11139](https://github.com/ghostty-org/ghostty/issues/11139)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11128#discussioncomment-15976454)
  from @mitchellh.
  
  Vouch: @noib3
  ```
- [`aa157c0`](https://github.com/ghostty-org/ghostty/commit/aa157c09abf6384e38cd4d9c19c35bfab8f7a3b8) terminal: fix insertBlanks orphaned spacer_tail beyond right margin ([#11137](https://github.com/ghostty-org/ghostty/issues/11137)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  When insertBlanks clears the entire region from cursor to the right
  margin (scroll_amount == 0), a wide character whose head is at the right
  margin gets cleared but its spacer_tail just beyond the margin is left
  behind, causing a "spacer tail not following wide" page integrity
  violation.
  
  Move the right-margin wide-char cleanup from inside the scroll_amount >
  0 block to before it, so it runs unconditionally — matching the
  rowWillBeShifted pattern of cleaning up boundary-straddling wide chars
  up front.
  
  Found via AFL++ fuzzing. #11109
  ```
- [`1ba9f91`](https://github.com/ghostty-org/ghostty/commit/1ba9f9187ef09a507cf58a3c38de493aacb090c4) terminal: fix no-reflow resize leaving stale spacer heads ([@mitchellh](https://github.com/mitchellh))
  ```text
  resizeWithoutReflowGrowCols has a fast path that reuses existing page
  capacity when growing columns: it simply bumps page.size.cols without
  touching cell data. If any row has a spacer_head at the old last column
  (from a wide char that did not fit), that cell is no longer at the end
  of the now-wider row, causing a page integrity violation.
  
  Fix by checking for spacer_head cells at the old last column before
  taking the fast path. If any are found, fall through to the slow path
  which handles spacer heads correctly via cloneRowFrom.
  
  Found by AFL++ stream fuzzer. #11109
  ```
- [`b39a00d`](https://github.com/ghostty-org/ghostty/commit/b39a00ddfa9003572e058d6ba1e87c449e575967) terminal: fix insertLines/deleteLines orphaned cells on full clear ([@mitchellh](https://github.com/mitchellh))
  ```text
  When deleteLines or insertLines count >= scroll region height, all rows
  go through the clear-only path (no shifting). This path did not call
  rowWillBeShifted, leaving orphaned spacer_tail cells when wide characters
  straddled the right margin boundary, causing a "spacer tail not following
  wide" page integrity violation.
  
  Add rowWillBeShifted before clearCells in the else branch of both
  functions.
  
  Found via AFL++ fuzzing. #11109
  ```
- [`678601d`](https://github.com/ghostty-org/ghostty/commit/678601d94a4d7fe0828b6f67b1a2b0d690c73aa9) terminal: fix no-reflow resize leaving stale spacer heads ([#11135](https://github.com/ghostty-org/ghostty/issues/11135)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  resizeWithoutReflowGrowCols has a fast path that reuses existing page
  capacity when growing columns: it simply bumps page.size.cols without
  touching cell data. If any row has a spacer_head at the old last column
  (from a wide char that did not fit), that cell is no longer at the end
  of the now-wider row, causing a page integrity violation.
  
  Fix by checking for spacer_head cells at the old last column before
  taking the fast path. If any are found, fall through to the slow path
  which handles spacer heads correctly via cloneRowFrom.
  
  Found by AFL++ stream fuzzer. #11109
  ```
- [`4768fff`](https://github.com/ghostty-org/ghostty/commit/4768ffff7396fb78578a61a6e488f16e1e961bf7) terminal: fix insertLines/deleteLines orphaned cells on full clear ([#11136](https://github.com/ghostty-org/ghostty/issues/11136)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  When deleteLines or insertLines count >= scroll region height, all rows
  go through the clear-only path (no shifting). This path did not call
  rowWillBeShifted, leaving orphaned spacer_tail cells when wide
  characters straddled the right margin boundary, causing a "spacer tail
  not following wide" page integrity violation.
  
  Add rowWillBeShifted before clearCells in the else branch of both
  functions.
  
  Found via AFL++ fuzzing. #11109
  ```
- [`e7030e7`](https://github.com/ghostty-org/ghostty/commit/e7030e73dbafd3f986c57b1a015d16cd53e7435b) terminal: fix printCell corrupting previous row when overwriting wide char ([@mitchellh](https://github.com/mitchellh))
  ```text
  printCell, when overwriting a wide cell with a narrow cell at x<=1 and
  y>0, unconditionally sets the last cell of the previous row to .narrow.
  This is intended to clear a spacer_head left by a wrapped wide char, but
  the cell could be a spacer_tail if a wide char fit entirely on the
  previous row. Setting a spacer_tail to .narrow orphans the preceding
  .wide cell, which later causes an integrity violation in insertBlanks
  (assert that the cell after a .wide is .spacer_tail).
  
  Fix by guarding the assignment so it only fires when the previous row's
  last cell is actually a .spacer_head. The same fix is applied in both
  the .wide and .spacer_tail branches of printCell.
  
  Found by AFL++ stream fuzzer.
  ```
- [`8cddd38`](https://github.com/ghostty-org/ghostty/commit/8cddd384c6ef614a373cf52b2a0e835c7e85134a) terminal: fix printCell corrupting previous row when overwriting wide char ([#11134](https://github.com/ghostty-org/ghostty/issues/11134)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  printCell, when overwriting a wide cell with a narrow cell at x<=1 and
  y>0, unconditionally sets the last cell of the previous row to .narrow.
  This is intended to clear a spacer_head left by a wrapped wide char, but
  the cell could be a spacer_tail if a wide char fit entirely on the
  previous row. Setting a spacer_tail to .narrow orphans the preceding
  .wide cell, which later causes an integrity violation in insertBlanks
  (assert that the cell after a .wide is .spacer_tail).
  
  Fix by guarding the assignment so it only fires when the previous row's
  last cell is actually a .spacer_head. The same fix is applied in both
  the .wide and .spacer_tail branches of printCell.
  
  Found by AFL++ stream fuzzer. #11109
  ```
- [`90e96a3`](https://github.com/ghostty-org/ghostty/commit/90e96a3891b7718ff98819ee51ecbd7c133d422f) terminal: fix insertBlanks integrity violation with wide char at right margin ([@mitchellh](https://github.com/mitchellh))
  ```text
  insertBlanks checks whether the last source cell being shifted is wide
  and clears it to avoid splitting, but it did not check the destination
  cells at the right edge of the scroll region. When a wide character
  straddles the right scroll margin (head at the margin, spacer_tail just
  beyond it), the swap loop displaced the wide head without clearing the
  orphaned spacer_tail, causing a page integrity violation
  (InvalidSpacerTailLocation).
  
  Fix by checking the cell at the right margin (last destination cell)
  before the swap loop and clearing it along with its spacer_tail when it
  is wide.
  
  Found by AFL++ stream fuzzer. #11109
  ```
- [`9d3c46c`](https://github.com/ghostty-org/ghostty/commit/9d3c46c4bc2348594148f809c01433ce768173ce) terminal: fix insertBlanks integrity violation with wide char at right margin ([#11132](https://github.com/ghostty-org/ghostty/issues/11132)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  insertBlanks checks whether the last source cell being shifted is wide
  and clears it to avoid splitting, but it did not check the destination
  cells at the right edge of the scroll region. When a wide character
  straddles the right scroll margin (head at the margin, spacer_tail just
  beyond it), the swap loop displaced the wide head without clearing the
  orphaned spacer_tail, causing a page integrity violation
  (InvalidSpacerTailLocation).
  
  Fix by checking the cell at the right margin (last destination cell)
  before the swap loop and clearing it along with its spacer_tail when it
  is wide.
  
  Found by AFL++ stream fuzzer. #11109
  ```
- [`913c120`](https://github.com/ghostty-org/ghostty/commit/913c12097bad2feb8977853cf1a60c137a968b50) Update VOUCHED list ([#11123](https://github.com/ghostty-org/ghostty/issues/11123)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11118#discussioncomment-15967576)
  from @pluiedev.
  
  Vouch: @jguthmiller
  ```
- [`22e29bb`](https://github.com/ghostty-org/ghostty/commit/22e29bb1f00b11c4ca1caf6d1302f67b2e9fa970) Update VOUCHED list ([#11122](https://github.com/ghostty-org/ghostty/issues/11122)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11121#issuecomment-3982187512)
  from @jcollie.
  
  Vouch: @rhodes-b
  ```
- [`97c11af`](https://github.com/ghostty-org/ghostty/commit/97c11af347be4ab8fd66ff0048048ee4209a03e9) terminal: fix integrity violation printing wide char with hyperlink at right edge ([@mitchellh](https://github.com/mitchellh))
  ```text
  Printing a wide character at the right edge of the screen with an active
  hyperlink triggered a page integrity violation (UnwrappedSpacerHead).
  printCell wrote the spacer_head to the cell and then called
  cursorSetHyperlink, whose internal integrity check observed the
  spacer_head before printWrap had a chance to set the row wrap flag.
  
  Fix by setting row.wrap = true before calling printCell for the
  spacer_head case, so all integrity checks see a consistent state.
  printWrap sets wrap again afterward, which is harmless. Found by AFL++
  stream fuzzer.
  ```
- [`43ec4ac`](https://github.com/ghostty-org/ghostty/commit/43ec4ace47ec47d7dea66826e0ebdfb3cae51a02) fuzz: add replay-crashes.nu to help find crash repros ([@mitchellh](https://github.com/mitchellh))
- [`f3da60a`](https://github.com/ghostty-org/ghostty/commit/f3da60aef59e3c9c645dc016e0377eb0af748a05) terminal: fix integrity violation printing wide char with hyperlink at right edge ([#11119](https://github.com/ghostty-org/ghostty/issues/11119)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Printing a wide character at the right edge of the screen with an active
  hyperlink triggered a page integrity violation (UnwrappedSpacerHead).
  printCell wrote the spacer_head to the cell and then called
  cursorSetHyperlink, whose internal integrity check observed the
  spacer_head before printWrap had a chance to set the row wrap flag.
  
  Fix by setting row.wrap = true before calling printCell for the
  spacer_head case, so all integrity checks see a consistent state.
  printWrap sets wrap again afterward, which is harmless. Found by AFL++
  stream fuzzer.
  
  #11109
  ```
- [`7665efc`](https://github.com/ghostty-org/ghostty/commit/7665efc3a161e3424267846216e913ba324aeb1c) fuzz: new stream corpus from 2 hour run ([@mitchellh](https://github.com/mitchellh))
- [`ca31828`](https://github.com/ghostty-org/ghostty/commit/ca31828c9387e2743f2b41d0405e2ed80590cd7f) Update VOUCHED list ([#11116](https://github.com/ghostty-org/ghostty/issues/11116)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11115#issuecomment-3981600125)
  from @mitchellh.
  
  Vouch: @markdorison
  ```
- [`533ad9e`](https://github.com/ghostty-org/ghostty/commit/533ad9e3fadf4eb1e5d28cb2d4b40ef4a8b311e3) i18n: update pt_BR translations ([#10635](https://github.com/ghostty-org/ghostty/issues/10635)) ([@guilhermetk](https://github.com/guilhermetk))
  ```text
  Add missing pt_BR translations reported in
  https://github.com/ghostty-org/ghostty/issues/10632 for version 1.3
  ```
- [`2454642`](https://github.com/ghostty-org/ghostty/commit/24546426c8de75d11c8448464fb4cd614663da46) Sync CODEOWNERS vouch list ([#11114](https://github.com/ghostty-org/ghostty/issues/11114)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Sync CODEOWNERS owners with vouch list.
  
  ## Added Users
  
  - @derVedro
  ```

## March 1, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22555802707), [2](https://github.com/ghostty-org/ghostty/actions/runs/22555273087), [3](https://github.com/ghostty-org/ghostty/actions/runs/22554564893), [4](https://github.com/ghostty-org/ghostty/actions/runs/22553094056), [5](https://github.com/ghostty-org/ghostty/actions/runs/22545810012), [6](https://github.com/ghostty-org/ghostty/actions/runs/22545426741), [7](https://github.com/ghostty-org/ghostty/actions/runs/22545388100), [8](https://github.com/ghostty-org/ghostty/actions/runs/22540291186), [9](https://github.com/ghostty-org/ghostty/actions/runs/22536791173)  
Summary: 9 runs • 55 commits • 5 authors

### Changes

- [`a595c00`](https://github.com/ghostty-org/ghostty/commit/a595c00f3c9e61bbd6ea9430a5444e5f026c1a0a) terminal: fix panic on CSI g (TBC) with overflowing param ([@mitchellh](https://github.com/mitchellh))
  ```text
  A fuzz crash found that CSI g with a parameter that saturates to
  u16 max (65535) causes @enumFromInt to panic when narrowing to
  TabClear (enum(u8)). Use std.meta.intToEnum instead, which safely
  returns an error for out-of-range values.
  ```
- [`f253c54`](https://github.com/ghostty-org/ghostty/commit/f253c54facb6fc00a4f408e1ab641f616b7d9f91) terminal: handle trailing colon in SGR underline parsing ([@mitchellh](https://github.com/mitchellh))
  ```text
  A trailing colon with no following sub-parameter (e.g. "ESC[58:4:m")
  leaves the colon separator bit set on the last param without adding
  another entry to the params array. When the SGR parser later iterates
  to that param (4 = underline) and sees the colon bit, it entered the
  colon path which asserted slice.len >= 2, but the slice only had one
  element.
  
  Replace the assert with a bounds check that treats the malformed
  sequence as a default single underline.
  
  Add a regression test reproducing the crash from AFL++ fuzzing
  (afl-out/stream/default/crashes/id:000021).
  ```
- [`ec4c5f9`](https://github.com/ghostty-org/ghostty/commit/ec4c5f90a8a825f06881307cf0b8d1735ac2c249) terminal: fix panic on CSI g (TBC) with overflowing param ([#11112](https://github.com/ghostty-org/ghostty/issues/11112)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A fuzz crash found that CSI g with a parameter that saturates to u16 max
  (65535) causes @enumFromInt to panic when narrowing to TabClear
  (enum(u8)). Use std.meta.intToEnum instead, which safely returns an
  error for out-of-range values.
  
  #11109
  ```
- [`2d69568`](https://github.com/ghostty-org/ghostty/commit/2d69568a67b5662000d0ccc3e7e70d3217e77034) terminal: handle trailing colon in SGR underline parsing ([#11113](https://github.com/ghostty-org/ghostty/issues/11113)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  A trailing colon with no following sub-parameter (e.g. "ESC[58:4:m")
  leaves the colon separator bit set on the last param without adding
  another entry to the params array. When the SGR parser later iterates to
  that param (4 = underline) and sees the colon bit, it entered the colon
  path which asserted slice.len >= 2, but the slice only had one element.
  
  Replace the assert with a bounds check that treats the malformed
  sequence as a default single underline.
  
  Add a regression test reproducing the crash from AFL++ fuzzing
  (afl-out/stream/default/crashes/id:000021).
  
  #11109
  ```
- [`9157eb4`](https://github.com/ghostty-org/ghostty/commit/9157eb439a3dfe34579e5030fcd03a6bb32585c7) terminal: insertBlanks should not crash with count 0 and CSI @ clamps [1,) ([@mitchellh](https://github.com/mitchellh))
  ```text
  CSI @ (ICH) with an explicit parameter of 0 should be clamped to 1,
  matching xterm behavior. Previously, a zero count reached
  Terminal.insertBlanks which called clearCells with an empty slice,
  triggering an out-of-bounds panic.
  
  Fix the stream dispatch to clamp 0 to 1 via @max, and add a defensive
  guard in insertBlanks for count == 0. Found by AFL++ stream fuzzer.
  ```
- [`1e027c9`](https://github.com/ghostty-org/ghostty/commit/1e027c9f206b220b61bccb930202f59b00a38407) terminal: insertBlanks should not crash with count 0 and CSI @ clamps to 1 min ([#11111](https://github.com/ghostty-org/ghostty/issues/11111)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  CSI @ (ICH) with an explicit parameter of 0 should be clamped to 1,
  matching xterm behavior. Previously, a zero count reached
  Terminal.insertBlanks which called clearCells with an empty slice,
  triggering an out-of-bounds panic.
  
  Fix the stream dispatch to clamp 0 to 1 via @max, and add a defensive
  guard in insertBlanks for count == 0. Found by AFL++ stream fuzzer.
  #11109
  ```
- [`e081a4a`](https://github.com/ghostty-org/ghostty/commit/e081a4abb4a9212ca99a797fa4497c08b1a3e5f3) fuzz/vt-stream ([@mitchellh](https://github.com/mitchellh))
- [`4f44879`](https://github.com/ghostty-org/ghostty/commit/4f44879c3b044264be558b1bf79e80c8f8bb1fd7) Clean up how fuzzers are laid out ([@mitchellh](https://github.com/mitchellh))
- [`33fbd73`](https://github.com/ghostty-org/ghostty/commit/33fbd73247de1024c2be2224447fd01bf6012529) fuzz/stream: clean up ([@mitchellh](https://github.com/mitchellh))
- [`1c65611`](https://github.com/ghostty-org/ghostty/commit/1c6561144603c94a38c4bfcf69c8f3a0119ca435) prettier should ignore various fuzz files ([@mitchellh](https://github.com/mitchellh))
- [`dce2326`](https://github.com/ghostty-org/ghostty/commit/dce2326c4ce4e1be34563aa6f65f26aa18251ed0) fix up gitattributes ([@mitchellh](https://github.com/mitchellh))
- [`8cebcaa`](https://github.com/ghostty-org/ghostty/commit/8cebcaa468589500e40e376d1c17586fc87d66e0) fuzz: stream cmin ([@mitchellh](https://github.com/mitchellh))
- [`1ead8f4`](https://github.com/ghostty-org/ghostty/commit/1ead8f4275edda26ca2981e664406bd8bce2c6e9) fuzz: `terminal.vtStream` fuzzer ([#11109](https://github.com/ghostty-org/ghostty/issues/11109)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This augments our libghostty fuzzing to add fuzzing for
  `terminal.vtStream` which exercises a LOT more codepaths than the pure
  parser (thousands of tuples compared to hundreds with `afl-showmap` on
  the two binaries). I also fixed up a few more minor things: prettier
  ignores AFL related files, lib-vt exports the readonly streams, etc.
  ```
- [`dcaa8f3`](https://github.com/ghostty-org/ghostty/commit/dcaa8f3979ea53a27fcd7b297fb5beab6f338709) terminal: fix out-of-bounds access in CSI W handler with no params ([@mitchellh](https://github.com/mitchellh))
  ```text
  CSI ? W (cursor tabulation control) accessed input.params[0] without
  first checking that params.len > 0, causing an index out-of-bounds
  panic when the sequence had an intermediate but no parameters.
  
  Add a params.len == 1 guard before accessing params[0].
  
  Found by AFL++ fuzzing.
  ```
- [`8c22cb0`](https://github.com/ghostty-org/ghostty/commit/8c22cb060138aa6f1d26be7ced2fa30da15af7c5) terminal: fix out-of-bounds access in CSI W handler with no params ([#11110](https://github.com/ghostty-org/ghostty/issues/11110)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  CSI ? W (cursor tabulation control) accessed input.params[0] without
  first checking that params.len > 0, causing an index out-of-bounds panic
  when the sequence had an intermediate but no parameters.
  
  Add a params.len == 1 guard before accessing params[0].
  
  Found by AFL++ fuzzing #11109
  ```
- [`adbb432`](https://github.com/ghostty-org/ghostty/commit/adbb432930ad66bc7f8d700a8701560efd038439) test/fuzz-libghostty: basic afl++-based fuzzer for libghostty ([@mitchellh](https://github.com/mitchellh))
- [`4e47c22`](https://github.com/ghostty-org/ghostty/commit/4e47c225b1541339600d24fd0d8d8689292ce848) pkg/afl++ ([@mitchellh](https://github.com/mitchellh))
- [`3294621`](https://github.com/ghostty-org/ghostty/commit/3294621430504ea776c094a33ccfa3e99945b117) switch to pkg/afl++ for fuzz ([@mitchellh](https://github.com/mitchellh))
- [`673dd47`](https://github.com/ghostty-org/ghostty/commit/673dd474f80fc0c99569a401f7f3863046634ddd) test/fuzz-libghostty: gitignore and initial corpus ([@mitchellh](https://github.com/mitchellh))
- [`2a34053`](https://github.com/ghostty-org/ghostty/commit/2a340536a6588c0a1f6aabde64cb03248a674d6d) test/fuzz-libghostty: add zig build run ([@mitchellh](https://github.com/mitchellh))
- [`54bdbdf`](https://github.com/ghostty-org/ghostty/commit/54bdbdf87d789ac1cc33c397d4573e8ce8f81a14) pkg/afl++: clean up, comments ([@mitchellh](https://github.com/mitchellh))
- [`afabbaf`](https://github.com/ghostty-org/ghostty/commit/afabbaf012a7f3b208ff42aeaf3366446418510a) pkg/afl++: extract runner ([@mitchellh](https://github.com/mitchellh))
- [`1d9f080`](https://github.com/ghostty-org/ghostty/commit/1d9f080309cc403200e22171b03703271cad8716) test/fuzz-libghostty: add README ([@mitchellh](https://github.com/mitchellh))
- [`eb7d28d`](https://github.com/ghostty-org/ghostty/commit/eb7d28d1800e9f5f2f82dac3ba4743aa830ce1e2) Corpus management update ([@mitchellh](https://github.com/mitchellh))
- [`2bd0952`](https://github.com/ghostty-org/ghostty/commit/2bd09523c80454ad994f2d653d60d79a08453487) pkg/afl++: use usize for len ([@mitchellh](https://github.com/mitchellh))
- [`23f6b1a`](https://github.com/ghostty-org/ghostty/commit/23f6b1af650aa9a0ca6feea72d2b2c4f305d9d4f) pkg/afl++: fuzzer takes a file argument ([@mitchellh](https://github.com/mitchellh))
- [`3462482`](https://github.com/ghostty-org/ghostty/commit/346248251e1697e8d7e154c8d18430c446c1e503) typos ([@mitchellh](https://github.com/mitchellh))
- [`2685efc`](https://github.com/ghostty-org/ghostty/commit/2685efca7a1667e6205f26bce98b80e1b9a70ff0) pkg/afl++: remove file arg ([@mitchellh](https://github.com/mitchellh))
- [`0ccaf3d`](https://github.com/ghostty-org/ghostty/commit/0ccaf3d5d61697672664601e0d87e681f0c97ef3) Clear key state overlay on "ignore" action ([@cespare](https://github.com/cespare))
- [`7cf8e0c`](https://github.com/ghostty-org/ghostty/commit/7cf8e0ccc000649e0b556a0bc781b9c97ba915a0) docs: clarify if pre-vouching contributors are also required to apply to get vouched before contributing to Ghostty ([@AlexJuca](https://github.com/AlexJuca))
- [`fc4d5a4`](https://github.com/ghostty-org/ghostty/commit/fc4d5a40dd10c1f69ee038e3bd4dee73659c60f8) chore: add improvements ([@AlexJuca](https://github.com/AlexJuca))
- [`2ed0e3b`](https://github.com/ghostty-org/ghostty/commit/2ed0e3b82b92de149bd4d58aca01a1d9269c1780) fix: format with prettier ([@AlexJuca](https://github.com/AlexJuca))
- [`4f34a0b`](https://github.com/ghostty-org/ghostty/commit/4f34a0b7d298dc202d4e48e18bd00fb280bb88b1) ci: fix windows CI checkouts with afl-min filenames ([@mitchellh](https://github.com/mitchellh))
- [`e8f861f`](https://github.com/ghostty-org/ghostty/commit/e8f861f561ee81a29cd06ad727a353a08a548eac) fuzz: replace : with _ for Windows ([@mitchellh](https://github.com/mitchellh))
- [`41870c1`](https://github.com/ghostty-org/ghostty/commit/41870c14aded310907dab03b28df8e63f9561765) ci: test libghostty fuzzer build ([@mitchellh](https://github.com/mitchellh))
- [`7bc44e7`](https://github.com/ghostty-org/ghostty/commit/7bc44e77d08ec2b3e3f209b2d6d1941b4d1f6e2d) shellcheck ([@mitchellh](https://github.com/mitchellh))
- [`f43874a`](https://github.com/ghostty-org/ghostty/commit/f43874a168dc8bd560ca1d7819d9a34c2ff318bf) fuzz: update corpus ([@mitchellh](https://github.com/mitchellh))
- [`683de81`](https://github.com/ghostty-org/ghostty/commit/683de81ee9546b52f7b8720dbe2b67f8ede914a8) typos: ignore fuzz corpus ([@mitchellh](https://github.com/mitchellh))
- [`a0b7714`](https://github.com/ghostty-org/ghostty/commit/a0b771489892aff695b8b1d834bc27adbc6011d9) Update CONTRIBUTING.md ([@AlexJuca](https://github.com/AlexJuca))
- [`059b02e`](https://github.com/ghostty-org/ghostty/commit/059b02eacb2145c9fe8a1c14e5a8fcbce9efc9a3) Update CONTRIBUTING.md ([@AlexJuca](https://github.com/AlexJuca))
- [`56f3b3d`](https://github.com/ghostty-org/ghostty/commit/56f3b3d0604428cfc2612d2aee450c2dd2a397f5) Update CONTRIBUTING.md ([@AlexJuca](https://github.com/AlexJuca))
- [`fa2a74d`](https://github.com/ghostty-org/ghostty/commit/fa2a74d7654b645afbc0da7742fd85a158c11f06) Update CONTRIBUTING.md ([@AlexJuca](https://github.com/AlexJuca))
- [`3972426`](https://github.com/ghostty-org/ghostty/commit/39724268527e9120ae24fdf0e73f6b085e72bb76) chore: improve grammer ([@AlexJuca](https://github.com/AlexJuca))
- [`c735fd8`](https://github.com/ghostty-org/ghostty/commit/c735fd8c4724a275fef9d8263c1986694649b62b) Update CONTRIBUTING.md ([@AlexJuca](https://github.com/AlexJuca))
- [`125b6e9`](https://github.com/ghostty-org/ghostty/commit/125b6e9f6ca90f3683716ac0cfb9e41d7787b58c) Clear key state overlay on "ignore" action ([#11103](https://github.com/ghostty-org/ghostty/issues/11103)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This fixes a bug in the key state sequence overlay.
  
  ## Demo
  
  In my ghostty config, I have
  
      keybind = ctrl+space>escape=ignore
      keybind = ctrl+space>p=toggle_command_palette
      ...
  
  because I use `ctrl+space>` sequences for most things and so hitting
  `esc` is my way to bail out of the sequence if I change my mind.
  
  I just switched to tip and got the new GTK key sequence overlay. Here's
  what I saw. In these screen recordings, the sequence of keys I press is
  
  ctrl+space, escape, ctrl+space, escape, ctrl+space, escape, ctrl+space,
  p
  
  
  https://github.com/user-attachments/assets/4a37bc7e-b75c-4bd1-99de-f21f4211b5b5
  
  after the fix:
  
  
  https://github.com/user-attachments/assets/023be88e-1299-4219-920c-1b1134b2888c
  
  ## Notes
  
  I believe this was also a leak, since the queued keys wouldn't be
  deinited.
  
  **AI usage:** Claude Code suggested the fix, then I read enough code to
  convince myself that it makes sense.
  ```
- [`a48cb63`](https://github.com/ghostty-org/ghostty/commit/a48cb630a8bcfda9ab0f3a6a05939482754fe839) libghostty-vt parser fuzzing, generic fuzz harness, using AFL++ ([#11089](https://github.com/ghostty-org/ghostty/issues/11089)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds a `test/fuzz-libghostty` which is a standalone `zig build`
  target for building an AFL++ instrumented executable for fuzzing the
  libghostty-vt parser. I also added a `pkg/afl++` (based on zig-afl-kit)
  so instrumenting objects and using AFL++ is a bit easier.
  
  Fuzzing `libghostty-vt`'s parser is as easy as `zig build run`, but see
  the README for a lot more details. I ran the fuzzer for ~14 hours total
  and only found one crash #11088. I'm pretty confident at this point our
  Parser layer isn't obviously crash-able, but need to instrument more
  places to fuzz.
  
  We don't use Zig's built-in fuzzing yet because as of 0.15 (our current
  stable), it isn't ready and AFL++ is an industry proven tool to do this.
  ```
- [`db7c140`](https://github.com/ghostty-org/ghostty/commit/db7c140100371305f1fa755e478282871908d672) Update VOUCHED list ([#11107](https://github.com/ghostty-org/ghostty/issues/11107)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11102#discussioncomment-15964699)
  from @mitchellh.
  
  Vouch: @mischief
  ```
- [`72df30f`](https://github.com/ghostty-org/ghostty/commit/72df30f14bd61f49d52341950ccac7db22d3c21a) docs: add clarification for pre-vouching contributors  ([#11096](https://github.com/ghostty-org/ghostty/issues/11096)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  If this PR is accepted, it will add a clarification to the contribution
  guidelines to inform pre-vouching contributors that they are still
  required to apply for vouching as would a first-time contributor.
  ```
- [`851b62d`](https://github.com/ghostty-org/ghostty/commit/851b62d73860a7cc09d3803bbfaeda1f0eb9b990) 🐛 Prevent git log output with signature information ([@drepper](https://github.com/drepper))
  ```text
  When users have something like
  
  [log]
          showSignature = true
  
  in their .gitconfig files, invocations of the log or show git sub-command
  emit additional information about signatures.  This additional output
  disturbs the generation of short_hash in GitVersion.zig, the additional text
  is copied verbatim into the string and then shown in the CSI >q output.
  
  To fix it always suppress the output of the signature information.  This
  has no effects when the setting is disabled anyway.
  ```
- [`9771aaa`](https://github.com/ghostty-org/ghostty/commit/9771aaaebb7dfe681744a58084cecd8d8017ce16) 🐛 Prevent git log output with signature information ([#11094](https://github.com/ghostty-org/ghostty/issues/11094)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  When users have something like
  
  [log]
          showSignature = true
  
  in their .gitconfig files, invocations of the log or show git
  sub-command emit additional information about signatures. This
  additional output disturbs the generation of short_hash in
  GitVersion.zig, the additional text is copied verbatim into the string
  and then shown in the CSI >q output.
  
  To fix it always suppress the output of the signature information. This
  has no effects when the setting is disabled anyway.
  ```
- [`4bef13a`](https://github.com/ghostty-org/ghostty/commit/4bef13a4d033f22fd392d51df415e047d3ffb6f1) Update VOUCHED list ([#11099](https://github.com/ghostty-org/ghostty/issues/11099)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11090#discussioncomment-15962101)
  from @jcollie.
  
  Vouch: @cespare
  ```
- [`6cf8f13`](https://github.com/ghostty-org/ghostty/commit/6cf8f13189c6793579a78cd2aa3c444e90a28980) Update VOUCHED list ([#11098](https://github.com/ghostty-org/ghostty/issues/11098)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11094#issuecomment-3980080445)
  from @jcollie.
  
  Vouch: @drepper
  ```
- [`33c855e`](https://github.com/ghostty-org/ghostty/commit/33c855e0478809c1c944f55cc2b86172e445b891) Update VOUCHED list ([#11093](https://github.com/ghostty-org/ghostty/issues/11093)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/5036#issuecomment-3979553300)
  from @jcollie.
  
  Vouch: @AlexJuca
  ```
- [`12f43df`](https://github.com/ghostty-org/ghostty/commit/12f43dfb7df9d04352616e29bfe0b2be9120bd96) fix(terminal): bounds check params in DCS passthrough entry ([@mitchellh](https://github.com/mitchellh))
  ```text
  When a DCS sequence has more than MAX_PARAMS parameters, entering
  dcs_passthrough would write to params[params_idx] without a bounds
  check, causing an out-of-bounds access. Drop the entire DCS hook
  when params overflow, consistent with how csi_dispatch handles it.
  
  Found by AFL fuzzing.
  ```
- [`25f1208`](https://github.com/ghostty-org/ghostty/commit/25f12080cb567a1a78980effbfe8692dbdcbba44) terminal: bounds check params in DCS passthrough entry ([#11088](https://github.com/ghostty-org/ghostty/issues/11088)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  When a DCS sequence has more than MAX_PARAMS parameters, entering
  dcs_passthrough would write to params[params_idx] without a bounds
  check, causing an out-of-bounds access. Add the same guard that
  csi_dispatch already has.
  
  Found by AFL fuzzing, test and fix produced by Codex.
  ```

## February 28, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22530851345), [2](https://github.com/ghostty-org/ghostty/actions/runs/22530301190), [3](https://github.com/ghostty-org/ghostty/actions/runs/22523375318), [4](https://github.com/ghostty-org/ghostty/actions/runs/22517662185), [5](https://github.com/ghostty-org/ghostty/actions/runs/22516696749), [6](https://github.com/ghostty-org/ghostty/actions/runs/22512782769)  
Summary: 6 runs • 12 commits • 5 authors

### Changes

- [`981901a`](https://github.com/ghostty-org/ghostty/commit/981901a01172311f5bfb7123242d9949347137e4) Remove old "acceptance tests" ([@mitchellh](https://github.com/mitchellh))
  ```text
  We haven't used or run these in forever (literally like 3+ years).
  They're just wasting cognitive space and confuse some users as to what
  they're for. Remove them.
  ```
- [`1499491`](https://github.com/ghostty-org/ghostty/commit/149949190ee5cf1e013dd2c70c84dc12f745369f) Remove old "acceptance tests" ([#11086](https://github.com/ghostty-org/ghostty/issues/11086)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  We haven't used or run these in forever (literally like 3+ years).
  They're just wasting cognitive space and confuse some users as to what
  they're for. Remove them.
  ```
- [`0db32ab`](https://github.com/ghostty-org/ghostty/commit/0db32ab9a8ff72d0c1eaf9c9e0cc94c3b27b2dd1) macos: fix window size/position restoration on Cmd+W close ([@abdurrahmanski](https://github.com/abdurrahmanski))
  ```text
  This fixes two overlapping issues regarding window positioning and Cmd+W window closures on macOS:
  
  1. `window-position-x` and `window-position-y` coordinates were being ignored on initial launch because `TerminalWindow.setInitialWindowPosition` depended on the `TerminalController`, which isn't fully attached during `awakeFromNib`. This logic was moved so explicit coordinates are correctly enforced.
  2. When closing a window via Cmd+W (leaving the app active), reopening the window would continuously cascade down and to the right rather than restoring to the previous position. It now checks if there are other windows open before cascading.
  3. `LastWindowPosition` was updated to save both the frame origin and size (width/height), ensuring that restoring a closed window correctly mimics native AppKit State Restoration size behaviors while honoring explicit configurations.
  ```
- [`6e622f8`](https://github.com/ghostty-org/ghostty/commit/6e622f8c75d6a80b17e1ba5e40d3f9efca410855) fix(macos): extract window cascade logic into helper function ([@abdurrahmanski](https://github.com/abdurrahmanski))
- [`0d5b9d5`](https://github.com/ghostty-org/ghostty/commit/0d5b9d554c14bc1b574267fa63dd95eee84edff3) Update macos/Sources/Features/Terminal/TerminalController.swift ([@abdurrahmanski](https://github.com/abdurrahmanski))
  ```text
  apply reviewer suggestion for cascading
  ```
- [`b40404b`](https://github.com/ghostty-org/ghostty/commit/b40404b0d97353f427f1378464624cf951f55edc) macOS: fix for Cmd+W window position/size restoration ([#11070](https://github.com/ghostty-org/ghostty/issues/11070)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  I'd like to contribute a fix for an issue I found regarding how macOS
  window restoration works when a window is closed via Cmd+W (leaving the
  app active).
  
  Currently, the position cascades down and to the right on every reopen,
  and size explicitly resets. Also, explicit `window-position-x/y` configs
  get ignored on first launch.
  
  I've diagnosed the issues:
  1. In `TerminalWindow.swift`, `setInitialWindowPosition` relies on the
  `TerminalController` which isn't present during `awakeFromNib`. I moved
  the `screen.origin` calculation directly into the window class to ensure
  fixed coordinates are respected immediately.
  2. In `TerminalController.swift`, I consolidated the window spawning
  cascade logic into a new `applyCascade(to:hasFixedPos:)` helper. It now
  only calls `cascadeTopLeft` if `TerminalController.all.count > 1`
  (meaning another window is active) and fixed coords aren't set. If it's
  the only window, it anchors exactly where `LastWindowPosition` placed
  it.
  3. In `LastWindowPosition.swift`, I updated the `save` and `restore`
  logic to persist the full `window.frame` (origin + size) instead of just
  the origin.
  
  *Disclosure: I used Cursor (Tab) to assist in navigating the codebase
  and formatting the Swift code, but I fully understand the AppKit
  lifecycle changes and edge cases I'm proposing.*
  
  I have the commit locally formatted with `swiftlint` and ready to push!
  ```
- [`889a945`](https://github.com/ghostty-org/ghostty/commit/889a945f74014b411ed4bf96d09dfc982d0f77e0) Update VOUCHED list ([#11078](https://github.com/ghostty-org/ghostty/issues/11078)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11076#discussioncomment-15955432)
  from @jcollie.
  
  Vouch: @DiaaEddin
  ```
- [`de62821`](https://github.com/ghostty-org/ghostty/commit/de62821973b0369f8e3586f7e8fd35d0aa1c838b) Rename ko.po back to ko_KR.po. ([@00-kat](https://github.com/00-kat))
  ```text
  While it was renamed from ko_KR.UTF-8.po to ko.po in #10976, @uhojin,
  a Korean locale maintainer, notes [1] that “ko_KR [*South* Korean] makes
  more sense in locale context just to avoid any potential confusion
  between 한국어 vs 조선어”.
  
  Despite ko_KP (North Korean) not being present in glibc (as of version
  2.43), and the ISO639 maintainers expressing disapproval of ko_KP [2],
  it is possible opinions may change in the future, and individual
  opinions may be contested—disambiguating doesn't hurt.
  
  [1]: https://github.com/ghostty-org/ghostty/pull/10976#discussion_r2861424171
  [2]: https://github.com/ghostty-org/ghostty/pull/10976#discussion_r2861359240
  ```
- [`14166bc`](https://github.com/ghostty-org/ghostty/commit/14166bc84c49eef8dee1c82add03ba9b672275fc) Rename `ko.po` back to `ko_KR.po` ([#11074](https://github.com/ghostty-org/ghostty/issues/11074)) ([@jcollie](https://github.com/jcollie))
  ```text
  While it was renamed from `ko_KR.UTF-8.po` to `ko.po` in #10976,
  @uhojin, a Korean locale maintainer, [notes] that “ko_KR [*South*
  Korean] makes more sense in locale context just to avoid any potential
  confusion between 한국어 vs 조선어”.
  
  Despite `ko_KP` (North Korean) not being present in glibc (as of version
  2.43), and the ISO639 maintainers [expressing disapproval of `ko_KP`],
  it is possible opinions may change in the future, and individual
  opinions may be contested—disambiguating doesn't hurt.
  
  Requesting a review from all involved parties; I wish you ***all* opine
  before merging**.
  
  [notes]:
  https://github.com/ghostty-org/ghostty/pull/10976#discussion_r2861424171
  [expressing disapproval of `ko_KP`]:
  https://github.com/ghostty-org/ghostty/pull/10976#discussion_r2861359240
  ```
- [`9192276`](https://github.com/ghostty-org/ghostty/commit/9192276d3e4795deccc04760359b371400540d16) Rename pt.po back to pt_BR.po. ([@00-kat](https://github.com/00-kat))
  ```text
  Portugal exists! Wikipedia notes [1] it to be the main other dialect.
  There's already a PR for pt_PT support too:
  https://github.com/ghostty-org/ghostty/pull/9078.
  
  It was renamed from pt_BR.UTF-8.po to pt.po in #10976.
  
  [1]: https://en.wikipedia.org/wiki/Portuguese_dialects
  ```
- [`ee0e0ae`](https://github.com/ghostty-org/ghostty/commit/ee0e0ae3dd3d5462728f40c3b9f80575bd195d1a) Rename `pt.po` back to `pt_BR.po` ([#11073](https://github.com/ghostty-org/ghostty/issues/11073)) ([@jcollie](https://github.com/jcollie))
  ```text
  Follow-up to #10976.
  
  Portugal exists! [Wikipedia notes it] to be the main other dialect.
  There's already a PR for `pt_PT` support too: #9078.
  
  [Wikipedia notes it]: https://en.wikipedia.org/wiki/Portuguese_dialects
  ```
- [`6d6dc9a`](https://github.com/ghostty-org/ghostty/commit/6d6dc9a114aaff7a35ecbaf2de0057dcb7630dc0) Update VOUCHED list ([#11071](https://github.com/ghostty-org/ghostty/issues/11071)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11070#issuecomment-3976278687)
  from @mitchellh.
  
  Vouch: @abdurrahmanski
  ```

## February 27, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22504821858), [2](https://github.com/ghostty-org/ghostty/actions/runs/22501525531), [3](https://github.com/ghostty-org/ghostty/actions/runs/22500996171), [4](https://github.com/ghostty-org/ghostty/actions/runs/22499732917), [5](https://github.com/ghostty-org/ghostty/actions/runs/22495419202), [6](https://github.com/ghostty-org/ghostty/actions/runs/22492229290), [7](https://github.com/ghostty-org/ghostty/actions/runs/22488004135), [8](https://github.com/ghostty-org/ghostty/actions/runs/22472504190), [9](https://github.com/ghostty-org/ghostty/actions/runs/22471926489), [10](https://github.com/ghostty-org/ghostty/actions/runs/22467433202)  
Summary: 10 runs • 40 commits • 9 authors

### Changes

- [`d75725b`](https://github.com/ghostty-org/ghostty/commit/d75725bd4dcfe493a7a5a8360a4548a2324c66bd) Remove duplicate word in README_TRANSLATORS § CODEOWNERS. ([@00-kat](https://github.com/00-kat))
- [`414c80c`](https://github.com/ghostty-org/ghostty/commit/414c80ce35ea061fc2be2e6621c45deef9381dfb) Improve word grouping w.r.t. localization team names. ([@00-kat](https://github.com/00-kat))
  ```text
  “always include a language and a country code” reads as “always include
  a language, and also always include a country code”, while the intended
  meaning was that it includes both a language *code* and a country code.
  ```
- [`608da64`](https://github.com/ghostty-org/ghostty/commit/608da647cb984df3f909a5b32bb8318ed87a39d0) Elaborate on X-Generator removal. ([@00-kat](https://github.com/00-kat))
  ```text
  That line was intended to guide those who do not normally edit po files
  with a plain text editor, but ended up sounding like it states the
  obvious (“to do X, do X”) before this change.
  ```
- [`71cb9de`](https://github.com/ghostty-org/ghostty/commit/71cb9debb9e47077a9b8d67fde35908db7ae7d85) Fix a few typos ([#11068](https://github.com/ghostty-org/ghostty/issues/11068)) ([@trag1c](https://github.com/trag1c))
- [`c78d9cb`](https://github.com/ghostty-org/ghostty/commit/c78d9cba9e3e82aacaeec0b827b56b66e85866bc) config: disable palette-generate by default ([@mitchellh](https://github.com/mitchellh))
  ```text
  Following the discussion at #10852, I believe this is the right default.
  I'm willing to continue to revisit this decisions, but Ghostty 1.3 is
  around the corner and I don't think such a change like this should be
  pushed into it.
  
  I think palette generation is best left as a _theme author_ tool. A
  Ghostty color theme could include `palette-generate=true` if it wants
  to customize the 256-color palette more easily. Of course, end users can
  as well anytime.
  
  Another part of my reasoning is that TUI programs who want this behavior
  can already achieve it themselves by mixing dark/light theme detection
  via CSI 996 (https://contour-terminal.org/vt-extensions/color-palette-update-notifications/)
  with OSC 4/10/11 color query and change sequences, both of which are
  decently supported in the terminal ecosystem and fully supported in
  Ghostty.
  
  I'm also open to considering some kind of new sequence to make this
  easier for TUIs (probably a mode) where they can opt-in to palette
  generation plus "harmonius" palettes (see `palette-harmonius`) and
  Ghostty does it on demand then. I think that'd solve the legacy vs new
  TUI argument where legacy programs can continue to make assumptions
  about the palette and new programs can opt-in to a more dynamic palette
  without having to do a lot of work themselves.
  ```
- [`705d8c6`](https://github.com/ghostty-org/ghostty/commit/705d8c61ce045ddc588176e155f04eebafdb39e7) config: disable palette-generate by default ([#11067](https://github.com/ghostty-org/ghostty/issues/11067)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Following the discussion at #10852, I believe this is the right default.
  I'm willing to continue to revisit this decisions, but Ghostty 1.3 is
  around the corner and I don't think such a change like this should be
  pushed into it.
  
  This was proposed before but I wanted to wait to iron out any bugs here
  and I think we have. Namely we identified one bug where we were
  accidentally overriding our _default_ palette which shouldn't happen.
  But now that it has sat awhile and we've gathered enough feedback, I'm
  willing to commit to it.
  
  In general, we got **very little negative feedback.** The linked
  discussion shows very little activity relative to other more
  controversial changes we've made. It has basically 1 upvote with around
  5 participants whereas our most popular or breaking features/bugs have
  had at least dozens if not over a hundred. I think this shows that this
  change isn't that disruptive, either because the colors work fine or
  because not that many things use the 256-color palette (probably the
  latter moreso but a mix for sure). For that reason, I do think
  revisiting this at some point is warranted.
  
  I think palette generation is best left as a _theme author_ tool. A
  Ghostty color theme could include `palette-generate=true` if it wants to
  customize the 256-color palette more easily. Of course, end users can as
  well anytime.
  
  Another part of my reasoning is that TUI programs who want this behavior
  can already achieve it themselves by mixing dark/light theme detection
  via CSI 996
  (https://contour-terminal.org/vt-extensions/color-palette-update-notifications/)
  with OSC 4/10/11 color query and change sequences, both of which are
  decently supported in the terminal ecosystem and fully supported in
  Ghostty.
  
  I'm also open to considering some kind of new sequence to make this
  easier for TUIs (probably a mode) where they can opt-in to palette
  generation plus "harmonius" palettes (see `palette-harmonius`) and
  Ghostty does it on demand then. I think that'd solve the legacy vs new
  TUI argument where legacy programs can continue to make assumptions
  about the palette and new programs can opt-in to a more dynamic palette
  without having to do a lot of work themselves.
  
  cc @jake-stewart
  ```
- [`2a41401`](https://github.com/ghostty-org/ghostty/commit/2a41401463c36a73a6d9c1ce9f250d628cd4153c) fix(macOS): filter phantom mouse events that defeat mouse-hide-while-typing ([@linustalacko](https://github.com/linustalacko))
  ```text
  On macOS, TUI apps like Zellij that frequently update the window title
  cause phantom mouse-move events to be generated at the same coordinates.
  These phantom events reach cursorPosCallback in the core, which calls
  showMouse() and explicitly unhides the cursor via
  NSCursor.setHiddenUntilMouseMoves(false), defeating the
  mouse-hide-while-typing feature.
  
  This ports the same position-equality check already present in the GTK
  runtime (added in PR #4973 for issue #3345) to the embedded runtime used
  by macOS. If the cursor position hasn't changed by more than 1px, the
  event is discarded.
  ```
- [`3a21305`](https://github.com/ghostty-org/ghostty/commit/3a21305d09bd73c99fad5977cff83c55b0421a1d) fix(macOS): filter phantom mouse events that defeat mouse-hide-while-typing ([#11066](https://github.com/ghostty-org/ghostty/issues/11066)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  ## Summary
  
  Ports the phantom mouse-motion position-equality check from the GTK
  runtime to the embedded runtime (used by macOS).
  
  On macOS, TUI apps like Zellij that frequently update the window title
  cause phantom `mouseMoved` events at the same coordinates. These flow
  through `embedded.zig` → `Surface.zig` `cursorPosCallback` →
  `showMouse()`, which explicitly calls
  `NSCursor.setHiddenUntilMouseMoves(false)` and unhides the cursor,
  defeating `mouse-hide-while-typing`.
  
  The GTK runtime already filters these in PR #4973 (for #3345):
  
  ```zig
  const is_cursor_still = @abs(priv.cursor_pos.x - pos.x) < 1 and
      @abs(priv.cursor_pos.y - pos.y) < 1;
  if (is_cursor_still) return;
  ```
  
  This PR adds the same check to `embedded.zig`'s `cursorPosCallback`,
  using the already-stored `self.cursor_pos` field.
  
  ## Test plan
  
  - [x] Enable `mouse-hide-while-typing = true` in Ghostty config
  - [ ] Run a TUI app that updates the window title frequently (e.g.
  Zellij)
  - [ ] Type — cursor should hide and stay hidden despite title updates
  - [ ] Move the mouse — cursor should reappear normally
  - [ ] Verify no regressions with normal mouse movement,
  focus-follows-mouse, or link hovering
  ````
- [`9da6588`](https://github.com/ghostty-org/ghostty/commit/9da6588c168c785e01c59d89ec9d99a149c8c9fd) feat(vt): Parse UAPI OSC 3008 hierarchical context signalling ([@Prakhar54-byte](https://github.com/Prakhar54-byte))
  ```text
  Implements parsing for OSC 3008, which allows terminal emulators to keep track of the stack of processes that have current control over the tty. The implementation mirrors existing `semantic_prompt.zig` architecture and natively maps UAPI definitions to Zig structures with lazy evaluation for optional metadata.
  
  Fixes #10900
  ```
- [`3e10047`](https://github.com/ghostty-org/ghostty/commit/3e1004717b7af345dd73629153cbccb458b457fc) refactor: apply PR feedback ([@Prakhar54-byte](https://github.com/Prakhar54-byte))
  ```text
  - Use `std.meta.stringToEnum` in ContextType and ExitStatus
  - Ensure `parseInt` only accepts digits for pids
  - Use `@tagName` for string representation in Field
  - Rename `fields_raw` to `metadata`
  - Rename `readField` to `readOption`
  ```
- [`99311e8`](https://github.com/ghostty-org/ghostty/commit/99311e8c2702d3541d14096c1c140d1808246673) Update VOUCHED list ([#11062](https://github.com/ghostty-org/ghostty/issues/11062)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11061#discussioncomment-15949027)
  from @mitchellh.
  
  Vouch: @adrum
  ```
- [`eafdbaa`](https://github.com/ghostty-org/ghostty/commit/eafdbaaadad375f62e2a8e825ca9fe931fb2708e) refactor: simplify Enum parse call and loop parsing logic ([@Prakhar54-byte](https://github.com/Prakhar54-byte))
- [`0bdd3bb`](https://github.com/ghostty-org/ghostty/commit/0bdd3bb6b5cefa58cb1d6dd3fb1b9bd6f909db12) feat(vt): Parse UAPI OSC 3008 hierarchical context signalling ([#11057](https://github.com/ghostty-org/ghostty/issues/11057)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Implements parsing for OSC 3008, which allows terminal emulators to keep
  track of the stack of processes that have current control over the tty.
  The implementation mirrors existing `semantic_prompt.zig` architecture
  and natively maps UAPI definitions to Zig structures with lazy
  evaluation for optional metadata.
  
  Fixes #10900
  ```
- [`b065703`](https://github.com/ghostty-org/ghostty/commit/b0657036a08179b092a1080798064846bc9d7f58) Update VOUCHED list ([#11065](https://github.com/ghostty-org/ghostty/issues/11065)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11064#issuecomment-3974502615)
  from @mitchellh.
  
  Vouch: @linustalacko
  ```
- [`df53f75`](https://github.com/ghostty-org/ghostty/commit/df53f75ad1b1e469d04afd035f941fbd2605903f) macOS: refine window tint for liquid glass ([#11018](https://github.com/ghostty-org/ghostty/issues/11018)) ([@bo2themax](https://github.com/bo2themax))
  ```text
  Depends on #11030
  
  - Update constraints of `TerminalGlassView`
  - Use `TerminalViewContainer.DerivedConfig` to map styling properties
  - Add TerminalViewContainerTests
  - Instead of using delay, now the view updates are explicitly called by
  window controllers
  ```
- [`b30db91`](https://github.com/ghostty-org/ghostty/commit/b30db91e69c68b724cc0410b5d703dd6ba66c2aa) build: test that `ghostty.h` compiles during a normal `zig build test` ([@jcollie](https://github.com/jcollie))
- [`ea5b07d`](https://github.com/ghostty-org/ghostty/commit/ea5b07d20f6ee76b54db67984b3e7926bc8c62e2) core: add tests for `ghostty.h` ([@jcollie](https://github.com/jcollie))
  ```text
  * ensure that `ghostty.h` compiles during basic Zig tests
  * ensure that non-exhaustive enums are kept synchronized between
    `ghostty.h` and their respective Zig counterpart.
  * adjust some enums that varied from established conventions
  ```
- [`537a2bc`](https://github.com/ghostty-org/ghostty/commit/537a2bccefef4c7bd371b18de3f2f6616657c140) Update VOUCHED list ([#11058](https://github.com/ghostty-org/ghostty/issues/11058)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11057#issuecomment-3973652560)
  from @mitchellh.
  
  Vouch: @Prakhar54-byte
  ```
- [`cdf0dd1`](https://github.com/ghostty-org/ghostty/commit/cdf0dd15e90996db24f88a2104fc9c798b8d4cbf) testing: use std.Build.TranslateC instead of @cImport ([@jcollie](https://github.com/jcollie))
- [`c61c8f9`](https://github.com/ghostty-org/ghostty/commit/c61c8f9e300d67de3f983fcb0296972ef1472b38) minor moving stuff ([@mitchellh](https://github.com/mitchellh))
- [`b6d26f2`](https://github.com/ghostty-org/ghostty/commit/b6d26f258be01b849fd629583235be60aa87f493) core: add tests for `ghostty.h` ([#11051](https://github.com/ghostty-org/ghostty/issues/11051)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  * ensure that `ghostty.h` compiles during basic Zig tests
  * ensure that non-exhaustive enums are kept synchronized between
  `ghostty.h` and their respective Zig counterpart.
  * adjust some enums that varied from established conventions
  ```
- [`dea263a`](https://github.com/ghostty-org/ghostty/commit/dea263a8ae42ae0281e571ff511001cfa1124846) Correct “i.e. de, es, and fr” to use “e.g”. ([@00-kat](https://github.com/00-kat))
  ```text
  That isn't a rephrasing of “language codes”, but rather lists examples.
  ```
- [`848d8af`](https://github.com/ghostty-org/ghostty/commit/848d8afecc71f63cf81a3698cdf655fc7be32480) Document common mistakes in translations. ([@00-kat](https://github.com/00-kat))
  ```text
  trag1c or I point these out manually whenever we see them, but they're
  extremely common and probably deserve being explicitly documented.
  
  “Style Guide” was made sentence case because no other title is in title
  case.
  
  Before anyone comments: I use “full stop” instead of “period” because
  the Unicode Character Database uses “full stop” instead of “period”, and
  I avoid “dot” because Unicode has a plethora of dots.
  ```
- [`d503681`](https://github.com/ghostty-org/ghostty/commit/d50368137f9885cd9fc19f188b5ad3b42bcbdf82) Elaborate on viewing translations. ([@00-kat](https://github.com/00-kat))
  ```text
  Documenting `--language` was suggested by @Filip7 in
  https://github.com/ghostty-org/ghostty/pull/10976#issuecomment-3969285334
  ```
- [`d68f516`](https://github.com/ghostty-org/ghostty/commit/d68f51672e48a3c27ce2e0a2ffda6132d5acbe7d) Prefer present over future tense in translators' guide. ([@00-kat](https://github.com/00-kat))
- [`f833928`](https://github.com/ghostty-org/ghostty/commit/f833928fcdc2e47c356d4a4aacfaad1b5d8baf94) Document localization teams. ([@00-kat](https://github.com/00-kat))
- [`e55ebf0`](https://github.com/ghostty-org/ghostty/commit/e55ebf0008da55f10ce379fe0f7025fd18c51a84) macos: workaround for TabTitleEditor alignment issue ([@bo2themax](https://github.com/bo2themax))
- [`6074e8b`](https://github.com/ghostty-org/ghostty/commit/6074e8b1fa626bb8a36f574e3218fd6b213b4cda) macos: workaround for `TabTitleEditor` alignment issue ([#11052](https://github.com/ghostty-org/ghostty/issues/11052)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #10993
  
  
  
  https://github.com/user-attachments/assets/666803f9-05aa-4c86-ab4a-7a183d471e33
  ```
- [`a476bef`](https://github.com/ghostty-org/ghostty/commit/a476bef11810dead6e61c996a3549a2a8c0bbcac) Assorted additions to `README_TRANSLATORS` ([#11047](https://github.com/ghostty-org/ghostty/issues/11047)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Optionally see individual commit descriptions.
  
  Re review requests:
  - I'm requesting a review from @pluiedev because she wrote the document.
  Feel free to ignore or remove your request.
  - @jcollie's text about CODEOWNERS from #10976 was rewritten, so I felt
  it would be appropriate to ask jcollie to check the new text.
  ```
- [`eb5b736`](https://github.com/ghostty-org/ghostty/commit/eb5b73639bf2127fc8f604d1f7156f11e7376076) Update VOUCHED list ([#11055](https://github.com/ghostty-org/ghostty/issues/11055)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11053#discussioncomment-15946894)
  from @jcollie.
  
  Vouch: @icodesign
  ```
- [`3ee6303`](https://github.com/ghostty-org/ghostty/commit/3ee63035d310c1290e631b51ec84bc5507f5d36e) macos: DockTilePlugin finds app bundle via `.app` suffix ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11029 (probably)
  
  If you renamed the app bundle, the prior check would infinite loop due
  to the combination of two bugs: invalid termination checks and
  hardcoding "Ghostty.app"
  ```
- [`32a9d35`](https://github.com/ghostty-org/ghostty/commit/32a9d35c8110a5f528e8c86eaa8128b92ae4d976) macos: DockTilePlugin finds app bundle via `.app` suffix ([#11049](https://github.com/ghostty-org/ghostty/issues/11049)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11029 (probably)
  
  If you renamed the app bundle, the prior check would infinite loop due
  to the combination of two bugs: invalid termination checks and
  hardcoding "Ghostty.app"
  ```
- [`3b4e2bb`](https://github.com/ghostty-org/ghostty/commit/3b4e2bbcbef7f5f786818457f8ef88f7ea08ea93) core: parse cmdline and cmdline_url semantic prompt options ([@jcollie](https://github.com/jcollie))
- [`f19d847`](https://github.com/ghostty-org/ghostty/commit/f19d847f95d3f775b26a5f4bc0fc2ea944bf946d) core: parse cmdline and cmdline_url semantic prompt options ([#11046](https://github.com/ghostty-org/ghostty/issues/11046)) ([@mitchellh](https://github.com/mitchellh))
- [`d5f6210`](https://github.com/ghostty-org/ghostty/commit/d5f621044deb8cc37612e2a5a890f8adb71107f0) Update `language` config option's documentation. ([@00-kat](https://github.com/00-kat))
  ```text
  Follow-up to #10976.
  ```
- [`64fd8d7`](https://github.com/ghostty-org/ghostty/commit/64fd8d794c20e33b1e02e22957ce1665d0350aea) build(deps): bump actions/upload-artifact from 6.0.0 to 7.0.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [actions/upload-artifact](https://github.com/actions/upload-artifact) from 6.0.0 to 7.0.0.
  - [Release notes](https://github.com/actions/upload-artifact/releases)
  - [Commits](https://github.com/actions/upload-artifact/compare/v6...bbbca2ddaa5d8feaa63e36b76fdaad77386f024f)
  
  ---
  updated-dependencies:
  - dependency-name: actions/upload-artifact
    dependency-version: 7.0.0
    dependency-type: direct:production
    update-type: version-update:semver-major
  ...
  ```
- [`5319d8d`](https://github.com/ghostty-org/ghostty/commit/5319d8d41c86e1be96f36b967e4be1006782a1da) build(deps): bump actions/download-artifact from 7.0.0 to 8.0.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [actions/download-artifact](https://github.com/actions/download-artifact) from 7.0.0 to 8.0.0.
  - [Release notes](https://github.com/actions/download-artifact/releases)
  - [Commits](https://github.com/actions/download-artifact/compare/37930b1c2abaa49bbe596cd826c3c89aef350131...70fc10c6e5e1ce46ad2ea6f2b72d43f7d47b13c3)
  
  ---
  updated-dependencies:
  - dependency-name: actions/download-artifact
    dependency-version: 8.0.0
    dependency-type: direct:production
    update-type: version-update:semver-major
  ...
  ```
- [`48e4f12`](https://github.com/ghostty-org/ghostty/commit/48e4f126d28c8b0ec7c0e33f63d52f077e52b817) build(deps): bump actions/download-artifact from 7.0.0 to 8.0.0 ([#11045](https://github.com/ghostty-org/ghostty/issues/11045)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [actions/download-artifact](https://github.com/actions/download-artifact)
  from 7.0.0 to 8.0.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/actions/download-artifact/releases">actions/download-artifact's
  releases</a>.</em></p>
  <blockquote>
  <h2>v8.0.0</h2>
  <h2>v8 - What's new</h2>
  <h3>Direct downloads</h3>
  <p>To support direct uploads in <code>actions/upload-artifact</code>,
  the action will no longer attempt to unzip all downloaded files.
  Instead, the action checks the <code>Content-Type</code> header ahead of
  unzipping and skips non-zipped files. Callers wishing to download a
  zipped file as-is can also set the new <code>skip-decompress</code>
  parameter to <code>false</code>.</p>
  <h3>Enforced checks (breaking)</h3>
  <p>A previous release introduced digest checks on the download. If a
  download hash didn't match the expected hash from the server, the action
  would log a warning. Callers can now configure the behavior on mismatch
  with the <code>digest-mismatch</code> parameter. To be secure by
  default, we are now defaulting the behavior to <code>error</code> which
  will fail the workflow run.</p>
  <h3>ESM</h3>
  <p>To support new versions of the @actions/* packages, we've upgraded
  the package to ESM.</p>
  <h2>What's Changed</h2>
  <ul>
  <li>Don't attempt to un-zip non-zipped downloads by <a
  href="https://github.com/danwkennedy"><code>@​danwkennedy</code></a> in
  <a
  href="https://redirect.github.com/actions/download-artifact/pull/460">actions/download-artifact#460</a></li>
  <li>Add a setting to specify what to do on hash mismatch and default it
  to <code>error</code> by <a
  href="https://github.com/danwkennedy"><code>@​danwkennedy</code></a> in
  <a
  href="https://redirect.github.com/actions/download-artifact/pull/461">actions/download-artifact#461</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/actions/download-artifact/compare/v7...v8.0.0">https://github.com/actions/download-artifact/compare/v7...v8.0.0</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/actions/download-artifact/commit/70fc10c6e5e1ce46ad2ea6f2b72d43f7d47b13c3"><code>70fc10c</code></a>
  Merge pull request <a
  href="https://redirect.github.com/actions/download-artifact/issues/461">#461</a>
  from actions/danwkennedy/digest-mismatch-behavior</li>
  <li><a
  href="https://github.com/actions/download-artifact/commit/f258da9a506b755b84a09a531814700b86ccfc62"><code>f258da9</code></a>
  Add change docs</li>
  <li><a
  href="https://github.com/actions/download-artifact/commit/ccc058e5fbb0bb2352213eaec3491e117cbc4a5c"><code>ccc058e</code></a>
  Fix linting issues</li>
  <li><a
  href="https://github.com/actions/download-artifact/commit/bd7976ba57ecea96e6f3df575eb922d11a12a9fd"><code>bd7976b</code></a>
  Add a setting to specify what to do on hash mismatch and default it to
  <code>error</code></li>
  <li><a
  href="https://github.com/actions/download-artifact/commit/ac21fcf45e0aaee541c0f7030558bdad38d77d6c"><code>ac21fcf</code></a>
  Merge pull request <a
  href="https://redirect.github.com/actions/download-artifact/issues/460">#460</a>
  from actions/danwkennedy/download-no-unzip</li>
  <li><a
  href="https://github.com/actions/download-artifact/commit/15999bff51058bc7c19b50ebbba518eaef7c26c0"><code>15999bf</code></a>
  Add note about package bumps</li>
  <li><a
  href="https://github.com/actions/download-artifact/commit/974686ed5098c7f9c9289ec946b9058e496a2561"><code>974686e</code></a>
  Bump the version to <code>v8</code> and add release notes</li>
  <li><a
  href="https://github.com/actions/download-artifact/commit/fbe48b1d2756394be4cd4358ed3bc1343b330e75"><code>fbe48b1</code></a>
  Update test names to make it clearer what they do</li>
  <li><a
  href="https://github.com/actions/download-artifact/commit/96bf374a614d4360e225874c3efd6893a3f285e7"><code>96bf374</code></a>
  One more test fix</li>
  <li><a
  href="https://github.com/actions/download-artifact/commit/b8c4819ef592cbe04fd93534534b38f853864332"><code>b8c4819</code></a>
  Fix skip decompress test</li>
  <li>Additional commits viewable in <a
  href="https://github.com/actions/download-artifact/compare/37930b1c2abaa49bbe596cd826c3c89aef350131...70fc10c6e5e1ce46ad2ea6f2b72d43f7d47b13c3">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=actions/download-artifact&package-manager=github_actions&previous-version=7.0.0&new-version=8.0.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`f9c57f0`](https://github.com/ghostty-org/ghostty/commit/f9c57f0bf6a705e4a3755f24dd591878607b5ca7) build(deps): bump actions/upload-artifact from 6.0.0 to 7.0.0 ([#11044](https://github.com/ghostty-org/ghostty/issues/11044)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [actions/upload-artifact](https://github.com/actions/upload-artifact)
  from 6.0.0 to 7.0.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/actions/upload-artifact/releases">actions/upload-artifact's
  releases</a>.</em></p>
  <blockquote>
  <h2>v7.0.0</h2>
  <h2>v7 What's new</h2>
  <h3>Direct Uploads</h3>
  <p>Adds support for uploading single files directly (unzipped). Callers
  can set the new <code>archive</code> parameter to <code>false</code> to
  skip zipping the file during upload. Right now, we only support single
  files. The action will fail if the glob passed resolves to multiple
  files. The <code>name</code> parameter is also ignored with this
  setting. Instead, the name of the artifact will be the name of the
  uploaded file.</p>
  <h3>ESM</h3>
  <p>To support new versions of the <code>@actions/*</code> packages,
  we've upgraded the package to ESM.</p>
  <h2>What's Changed</h2>
  <ul>
  <li>Add proxy integration test by <a
  href="https://github.com/Link"><code>@​Link</code></a>- in <a
  href="https://redirect.github.com/actions/upload-artifact/pull/754">actions/upload-artifact#754</a></li>
  <li>Upgrade the module to ESM and bump dependencies by <a
  href="https://github.com/danwkennedy"><code>@​danwkennedy</code></a> in
  <a
  href="https://redirect.github.com/actions/upload-artifact/pull/762">actions/upload-artifact#762</a></li>
  <li>Support direct file uploads by <a
  href="https://github.com/danwkennedy"><code>@​danwkennedy</code></a> in
  <a
  href="https://redirect.github.com/actions/upload-artifact/pull/764">actions/upload-artifact#764</a></li>
  </ul>
  <h2>New Contributors</h2>
  <ul>
  <li><a href="https://github.com/Link"><code>@​Link</code></a>- made
  their first contribution in <a
  href="https://redirect.github.com/actions/upload-artifact/pull/754">actions/upload-artifact#754</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/actions/upload-artifact/compare/v6...v7.0.0">https://github.com/actions/upload-artifact/compare/v6...v7.0.0</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/actions/upload-artifact/commit/bbbca2ddaa5d8feaa63e36b76fdaad77386f024f"><code>bbbca2d</code></a>
  Support direct file uploads (<a
  href="https://redirect.github.com/actions/upload-artifact/issues/764">#764</a>)</li>
  <li><a
  href="https://github.com/actions/upload-artifact/commit/589182c5a4cec8920b8c1bce3e2fab1c97a02296"><code>589182c</code></a>
  Upgrade the module to ESM and bump dependencies (<a
  href="https://redirect.github.com/actions/upload-artifact/issues/762">#762</a>)</li>
  <li><a
  href="https://github.com/actions/upload-artifact/commit/47309c993abb98030a35d55ef7ff34b7fa1074b5"><code>47309c9</code></a>
  Merge pull request <a
  href="https://redirect.github.com/actions/upload-artifact/issues/754">#754</a>
  from actions/Link-/add-proxy-integration-tests</li>
  <li><a
  href="https://github.com/actions/upload-artifact/commit/02a8460834e70dab0ce194c64360c59dc1475ef0"><code>02a8460</code></a>
  Add proxy integration test</li>
  <li>See full diff in <a
  href="https://github.com/actions/upload-artifact/compare/v6...bbbca2ddaa5d8feaa63e36b76fdaad77386f024f">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=actions/upload-artifact&package-manager=github_actions&previous-version=6.0.0&new-version=7.0.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`336ca18`](https://github.com/ghostty-org/ghostty/commit/336ca188457f08df89f5682cdb39288f7b40c946) Update `language` config option's documentation ([#11043](https://github.com/ghostty-org/ghostty/issues/11043)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Follow-up to #10976.
  ```

