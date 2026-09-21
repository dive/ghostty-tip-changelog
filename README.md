> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: September 21, 2026 at 08:45 UTC.

## September 21, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/35546322398)  
Summary: 1 runs • 1 commits • 1 authors

### Changes

- [`3c47ca1`](https://github.com/ghostty-org/ghostty/commit/3c47ca159368eb4a860ffe5333abdf4a85b2767b) Sync CODEOWNERS vouch list ([#14327](https://github.com/ghostty-org/ghostty/issues/14327)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Sync CODEOWNERS owners with vouch list.
  
  ## Added Users
  
  - @dungdm93
  ```

## September 20, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/35492892512), [2](https://github.com/ghostty-org/ghostty/actions/runs/35490141243), [3](https://github.com/ghostty-org/ghostty/actions/runs/35487007432)  
Summary: 3 runs • 8 commits • 3 authors

### Changes

- [`27e8b3f`](https://github.com/ghostty-org/ghostty/commit/27e8b3fa85d9cf8c7cd5ae2ced348bcb0a4fba9c) Update VOUCHED list ([#14320](https://github.com/ghostty-org/ghostty/issues/14320)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14319#issuecomment-5747979152)
  from @pluiedev.
  
  Vouch: @RadicalTray
  ```
- [`e507794`](https://github.com/ghostty-org/ghostty/commit/e5077949834c3291a9434f88b38a381d8f5fedfc) libghostty-vt: add render hold effect for synchronized output (mode 2026) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds a new callback `render_hold` to the libghostty-vt API (Zig and
  C). This callback is called whenever the embedder should snapshot the
  last rendered frame at the current terminal state (currently only for mode
  2026). The name is generic so other sources in the future might reuse it.
  
  Before this, libghostty-vt did nothing for mode 2026 beyond setting
  the mode bit, so an embedder could only check the mode before each
  draw and skip the render state update when it was set.
  
  That has two problems:
  
    1. The frame left on screen is whatever was drawn last, which
       can be older than what the program intended or even a half-drawn
       frame.
    2. If the program resets and sets the mode again between two
       draws (or within a single write), the mode never appears to turn off
       and the finished frame in between is lost, so a program that draws
       continuously can appear frozen.
  
  With the callback, an embedder updates its render state when a hold begins,
  which captures exactly the frame the program wants left on screen,
  and then skips updates until the hold ends.
  
  This actually is a more robust implementation than Ghostty GUI has so I
  plan to follow up to fix that!
  ```
- [`56a3437`](https://github.com/ghostty-org/ghostty/commit/56a3437a7f51796d7946584043229c2f15c70583) libghostty-vt: add render hold effect for synchronized output ([#14317](https://github.com/ghostty-org/ghostty/issues/14317)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds a new callback `render_hold` to the libghostty-vt API (Zig and
  C). This callback is called whenever the embedder should snapshot the
  last rendered frame at the current terminal state (currently only for
  mode 2026). The name is generic so other sources in the future might
  reuse it.
  
  Before this, libghostty-vt did nothing for mode 2026 beyond setting the
  mode bit, so an embedder could only check the mode before each draw and
  skip the render state update when it was set.
  
  That has two problems:
  
  1. The frame left on screen is whatever was drawn last, which can be
  older than what the program intended or even a half-drawn frame.
  2. If the program resets and sets the mode again between two draws (or
  within a single write), the mode never appears to turn off and the
  finished frame in between is lost, so a program that draws continuously
  can appear frozen.
  
  With the callback, an embedder updates its render state when a hold
  begins, which captures exactly the frame the program wants left on
  screen, and then skips updates until the hold ends.
  
  This actually is a more robust implementation than Ghostty GUI has so I
  plan to follow up to fix that!
  ```
- [`12542b3`](https://github.com/ghostty-org/ghostty/commit/12542b3923106fd13e4f5d0f9b7c8b65843a1836) deps: Update uucode for Unicode 18 ([@jacobsandlund](https://github.com/jacobsandlund))
- [`aef7aae`](https://github.com/ghostty-org/ghostty/commit/aef7aaeb88423d7b483e857042a4135d8d5143f1) check-zig-hash --update ([@jacobsandlund](https://github.com/jacobsandlund))
- [`9cdbf79`](https://github.com/ghostty-org/ghostty/commit/9cdbf798d904769d0b3514658f3684b24850487d) deps: Update uucode for Unicode 18 ([#14293](https://github.com/ghostty-org/ghostty/issues/14293)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This updates `uucode` for the new (as of 9/16) Unicode 18 release. See
  the [PR on uucode](https://github.com/jacobsandlund/uucode/pull/58) for
  details.
  
  In short, mostly Unicode 18 is the typical Emoji, Scripts, Blocks
  additions, but it also simplifies Grapheme Breaking for Indic Conjunct
  Break, somewhat. Also in the `uucode` PR is the results of the
  `+grapheme-break` benchmark showing this has no performance impact.
  
  Note a new `.table_len` and `.fromTableIndex` help us precompute the
  lookup table, though the slightly more complicated index calculation
  needs a bump in @setEvalBranchQuota.
  
  Testing note, I've been running this on my mac, but my linux machine has
  been collecting dust :(
  
  **AI disclaimer**: I used Astra and Fable to develop this, but closely
  reviewed and steered the code such that there is a cleaner split with
  `indic_conjunct_break_linker_extend` and
  `indic_conjunct_break_linker_other`, and arranged the new `BreakState`
  for easier manipulation while still keeping the same precomputed table
  size (the naive switch from 5 enum values to 3 enum values plus a
  boolean was going to raise the size a bit).
  ```
- [`079502e`](https://github.com/ghostty-org/ghostty/commit/079502e23e2c296d200776e03058aab81703c93d) terminal: look up modes by number with a comptime sorted set ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds `datastruct.ComptimeIntSet`, a set of comptime-known integer
  keys with a fast runtime lookup, and uses it in `modes.modeFromInt` to
  map a mode number to its mode.
  
  Previously `modesFromInt` did an inline for comparing every entry.
  In disassembly this showed up as hundreds of branches and instructions.
  
  This is admittedly a micro-optimization but it has a really practical
  reason: checking some of these modes is critical on the render path
  (e.g. synchronized rendering) and every nanosecond is something we want
  to save. Plus, the complexity of this change is pretty low.
  
    C API get mode 2026:          10.5 ns ->  3.2 ns
    C API get unknown mode:       10.5 ns ->  1.8 ns
    C API get KAM (first entry):   3.8 ns ->  3.2 ns
    stream CSI ? 2026 h/l:        20.6 ns -> 12.7 ns per sequence
    stream set/reset 3 modes:     46.0 ns -> 28.0 ns per sequence
    stream DECRQM:                57.0 ns -> 41.0 ns per sequence
  ```
- [`01a8d3a`](https://github.com/ghostty-org/ghostty/commit/01a8d3af223dbb5ba3ddbf0a8f3d7820e304880a) terminal: look up modes by number with a comptime sorted set ([#14316](https://github.com/ghostty-org/ghostty/issues/14316)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds `datastruct.ComptimeIntSet`, a set of comptime-known integer
  keys with a fast runtime lookup, and uses it in `modes.modeFromInt` to
  map a mode number to its mode.
  
  Previously `modesFromInt` did an inline for comparing every entry. In
  disassembly this showed up as hundreds of branches and instructions.
  
  This is admittedly a micro-optimization but it has a really practical
  reason: checking some of these modes is critical on the render path
  (e.g. synchronized rendering) and every nanosecond is something we want
  to save. Plus, the complexity of this change is pretty low.
  
  >   C API get mode 2026:          10.5 ns ->  3.2 ns
  >   C API get unknown mode:       10.5 ns ->  1.8 ns
  >   C API get KAM (first entry):   3.8 ns ->  3.2 ns
  >   stream CSI ? 2026 h/l:        20.6 ns -> 12.7 ns per sequence
  >   stream set/reset 3 modes:     46.0 ns -> 28.0 ns per sequence
  >   stream DECRQM:                57.0 ns -> 41.0 ns per sequence
  ```

## September 19, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/35468004060), [2](https://github.com/ghostty-org/ghostty/actions/runs/35466266073)  
Summary: 2 runs • 3 commits • 3 authors

### Changes

- [`790c6b6`](https://github.com/ghostty-org/ghostty/commit/790c6b60f730a17fef267ffde0817c55fa7d62d3) Update VOUCHED list ([@github-actions[bot]](https://github.com/apps/github-actions))
  ```text
  https://github.com/ghostty-org/ghostty/discussions/14305#discussioncomment-DC_kwDOHFhdAs4BGpVY
  ```
- [`a301054`](https://github.com/ghostty-org/ghostty/commit/a3010543b0c39b98a81ace9f50b1910ae641c8c1) Update VOUCHED list ([#14307](https://github.com/ghostty-org/ghostty/issues/14307)) ([@jcollie](https://github.com/jcollie))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14305#discussioncomment-18519384)
  from @jcollie.
  
  Vouch: @thomasfedb
  ```
- [`ca9b038`](https://github.com/ghostty-org/ghostty/commit/ca9b0384f22fc018d81b9f69cada01677f565126) Update VOUCHED list ([#14308](https://github.com/ghostty-org/ghostty/issues/14308)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14305#discussioncomment-18519384)
  from @jcollie.
  
  Vouch: @thomasfedb
  ```

## September 18, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/35375414566), [2](https://github.com/ghostty-org/ghostty/actions/runs/35354192495), [3](https://github.com/ghostty-org/ghostty/actions/runs/35346319697), [4](https://github.com/ghostty-org/ghostty/actions/runs/35340649466), [5](https://github.com/ghostty-org/ghostty/actions/runs/35332773941)  
Summary: 5 runs • 25 commits • 11 authors

### Changes

- [`c55f213`](https://github.com/ghostty-org/ghostty/commit/c55f213aa2a3aa1d852f9f91cb4bd95d55982f48) terminal: add option to disable scrollback pull on resize ([@mitchellh](https://github.com/mitchellh))
  ```text
  #14294
  
  This adds a boolean flag throughout the Zig API and C API to control
  whether resizing can pull scrollback back into the active area. The
  default is true, which is the existing behavior.
  
  Ptys that keep their own screen buffer without scrollback (namely
  Windows ConPTY) can't pull rows back, so after a resize that pulls we
  disagree with the pty about what is on screen and subsequent output
  lands in the wrong place.
  
  Row growth always appends blank rows at the bottom when pulling is
  disabled.
  
  Refs:
  https://github.com/microsoft/terminal/blob/7c92ecd037476f957809d0813b14d8bc44bb071a/src/cascadia/TerminalCore/Terminal.cpp#L380-L406
  https://github.com/xtermjs/xterm.js/blob/c58ea3637f3968e0e6e79cd92cf9aace7ef89ee2/src/common/buffer/Buffer.ts#L194-L197
  https://github.com/wezterm/wezterm/blob/b09b56c29c1e367e598b60ca266e2cc9038751e0/term/src/screen.rs#L268-L288
  ```
- [`b32f20f`](https://github.com/ghostty-org/ghostty/commit/b32f20f3e8d25bb925ec545c54498e93518e7ced) terminal: add option to disable scrollback pull on resize ([#14296](https://github.com/ghostty-org/ghostty/issues/14296)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  #14294
  
  This adds a boolean flag throughout the Zig API and C API to control
  whether resizing can pull scrollback back into the active area. The
  default is true, which is the existing behavior.
  
  Ptys that keep their own screen buffer without scrollback (namely
  Windows ConPTY) can't pull rows back, so after a resize that pulls we
  disagree with the pty about what is on screen and subsequent output
  lands in the wrong place.
  
  Row growth always appends blank rows at the bottom when pulling is
  disabled.
  
  Refs:
  
  https://github.com/microsoft/terminal/blob/7c92ecd037476f957809d0813b14d8bc44bb071a/src/cascadia/TerminalCore/Terminal.cpp#L380-L406
  https://github.com/xtermjs/xterm.js/blob/c58ea3637f3968e0e6e79cd92cf9aace7ef89ee2/src/common/buffer/Buffer.ts#L194-L197
  https://github.com/wezterm/wezterm/blob/b09b56c29c1e367e598b60ca266e2cc9038751e0/term/src/screen.rs#L268-L288
  ```
- [`a4031c8`](https://github.com/ghostty-org/ghostty/commit/a4031c8e3f94f40df712de7cdf6fd4f6c17980c6) bash: detect hooks in prompt command arrays ([@jparise](https://github.com/jparise))
  ```text
  The delimiter-based guard treats PROMPT_COMMAND as a semicolon-separated
  command list. Indexed array expansion joins elements with spaces instead,
  so a hook appended after an existing element is not detected when the
  integration is sourced again.
  
  Match the full internal hook command as a substring so the guard works
  for both scalar and array values. This intentionally gives up command
  boundary matching; the private function name and redirection keep an
  incidental match unlikely.
  ```
- [`a1bf5b5`](https://github.com/ghostty-org/ghostty/commit/a1bf5b5e113b1b0c4e30c87ecbe746bd07eda3e4) embedded: route split and close C APIs through performBindingAction ([@MisterTea](https://github.com/MisterTea))
  ```text
  macOS menus call ghostty_surface_split, split_focus, and request_close
  directly, while keybinds go through Surface.performBindingAction. GTK
  already uses that path for splits and close. Route the embedded C APIs
  the same way so menus and keybinds share one hook.
  ```
- [`ab34b8b`](https://github.com/ghostty-org/ghostty/commit/ab34b8b131eb2d60e7d22838dd6d77b98fec04b3) opengl: explicitly set EGL_SURFACE_TYPE ([@pluiedev](https://github.com/pluiedev))
- [`c15e2f7`](https://github.com/ghostty-org/ghostty/commit/c15e2f79922620f8651b92bb55662b19ce9505bb) opengl: EGLattrib arrays need no explicit sentinel ([@pluiedev](https://github.com/pluiedev))
  ```text
  Array literals automagically gain the sentinel when assigned the correct
  type. Neat, huh?
  
  See https://ziglang.org/documentation/0.16.0/#Sentinel-Terminated-Arrays
  ```
- [`851cd4d`](https://github.com/ghostty-org/ghostty/commit/851cd4dc13adbd17886ab1baf46280d27a6c9fa6) gtk: disable Vulkan again, remove old version gates ([@pluiedev](https://github.com/pluiedev))
  ```text
  Vulkan is causing problems again...
  
  Also our minimum GTK version requirement is 4.18 now, so we can nuke all
  the old checks
  ```
- [`0fca3d3`](https://github.com/ghostty-org/ghostty/commit/0fca3d34a56a420da92a7cb20109e71d523f7bf6) gtk/imgui_widget: remove direct call to glClearColor ([@pluiedev](https://github.com/pluiedev))
  ```text
  Since the refactor to move our OpenGL context off-thread there is no more
  GLAD context loaded on the main thread for this widget, so calling ANY
  OpenGL function will crash the entire app.
  
  I don't think the call even worked as intended? I at least can't seem to
  tell any difference when the clear commands are simply removed.
  Maybe they were useful before.
  ```
- [`590ab15`](https://github.com/ghostty-org/ghostty/commit/590ab157f4f05286888f5838f4167fe4fcc07be2) opengl/Sampler: handle enum parameters correctly ([@pluiedev](https://github.com/pluiedev))
  ```text
  I'm so dumb like honestly, always double check if your unreachables
  are *comptime*. Whether the value being switched on is comptime or not
  does not matter
  ```
- [`f5c056d`](https://github.com/ghostty-org/ghostty/commit/f5c056d3045b4b9baf86400a95e598044a0573b5) font: import Constraint from Glyph.zig in nerd-font codegen ([@j-c-m](https://github.com/j-c-m))
  ```text
  1c0aac54b moved RenderOptions.Constraint from face.zig to Glyph.zig
  and updated nerd_font_attributes.zig. This does the matching change to
  the generator.
  ```
- [`cd8daf9`](https://github.com/ghostty-org/ghostty/commit/cd8daf9eb6fe85ed6ec1c4450b34fff84abf9bea) build(deps): bump docker/build-push-action from 7.3.0 to 7.4.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [docker/build-push-action](https://github.com/docker/build-push-action) from 7.3.0 to 7.4.0.
  - [Release notes](https://github.com/docker/build-push-action/releases)
  - [Commits](https://github.com/docker/build-push-action/compare/53b7df96c91f9c12dcc8a07bcb9ccacbed38856a...c3c9e263c25d99ce0380d002d59b67737d91b0dc)
  
  ---
  updated-dependencies:
  - dependency-name: docker/build-push-action
    dependency-version: 7.4.0
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`98f2e3e`](https://github.com/ghostty-org/ghostty/commit/98f2e3e6dce6f4198254c9d8ccf5de50c94b17ca) build(deps): bump namespacelabs/nscloud-cache-action from 1.6.1 to 1.7.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [namespacelabs/nscloud-cache-action](https://github.com/namespacelabs/nscloud-cache-action) from 1.6.1 to 1.7.0.
  - [Release notes](https://github.com/namespacelabs/nscloud-cache-action/releases)
  - [Commits](https://github.com/namespacelabs/nscloud-cache-action/compare/c5f8dab7560444c4bf8dbc64f1b203431873c547...1124a6f3ce44e5cf84cc22111530961f4d2a15f9)
  
  ---
  updated-dependencies:
  - dependency-name: namespacelabs/nscloud-cache-action
    dependency-version: 1.7.0
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`1bd494c`](https://github.com/ghostty-org/ghostty/commit/1bd494cf956e1c57267b7836eceb77e872b17f6e) build(deps): bump namespacelabs/nscloud-cache-action from 1.6.1 to 1.7.0 ([#14285](https://github.com/ghostty-org/ghostty/issues/14285)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [namespacelabs/nscloud-cache-action](https://github.com/namespacelabs/nscloud-cache-action)
  from 1.6.1 to 1.7.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/namespacelabs/nscloud-cache-action/releases">namespacelabs/nscloud-cache-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v1.7.0</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>fix: Stabilize Brew and Maven cache mode tests by <a
  href="https://github.com/sebawita"><code>@​sebawita</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/170">namespacelabs/nscloud-cache-action#170</a></li>
  <li>fix: update actions toolkit to 0.5.0 by <a
  href="https://github.com/rcrowe"><code>@​rcrowe</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/175">namespacelabs/nscloud-cache-action#175</a></li>
  <li>Add cache miss documentation hint by <a
  href="https://github.com/sebawita"><code>@​sebawita</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/169">namespacelabs/nscloud-cache-action#169</a></li>
  <li>fix: update vulnerable transitive dependencies by <a
  href="https://github.com/rcrowe"><code>@​rcrowe</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/176">namespacelabs/nscloud-cache-action#176</a></li>
  <li>test: move Vitest mocks to module scope by <a
  href="https://github.com/rcrowe"><code>@​rcrowe</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/177">namespacelabs/nscloud-cache-action#177</a></li>
  </ul>
  <h2>New Contributors</h2>
  <ul>
  <li><a href="https://github.com/sebawita"><code>@​sebawita</code></a>
  made their first contribution in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/170">namespacelabs/nscloud-cache-action#170</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/namespacelabs/nscloud-cache-action/compare/v1.6.1...v1.7.0">https://github.com/namespacelabs/nscloud-cache-action/compare/v1.6.1...v1.7.0</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/1124a6f3ce44e5cf84cc22111530961f4d2a15f9"><code>1124a6f</code></a>
  test: move Vitest mocks to module scope (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/177">#177</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/e40c60c47e26a5b911d6a0683a7294401e5f2dbe"><code>e40c60c</code></a>
  fix: update vulnerable transitive dependencies (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/176">#176</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/7db012f73e34bd0e002c17e6ada243fc8b89008f"><code>7db012f</code></a>
  Add cache miss documentation hint (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/169">#169</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/3199dcd520c302741adae1d82317e99e3db7bf94"><code>3199dcd</code></a>
  fix: update actions toolkit to 0.5.0 (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/175">#175</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/ac29750009f671e320b31cb40043262d8679ed61"><code>ac29750</code></a>
  Stabilize Brew and Maven cache mode tests (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/170">#170</a>)</li>
  <li>See full diff in <a
  href="https://github.com/namespacelabs/nscloud-cache-action/compare/c5f8dab7560444c4bf8dbc64f1b203431873c547...1124a6f3ce44e5cf84cc22111530961f4d2a15f9">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=namespacelabs/nscloud-cache-action&package-manager=github_actions&previous-version=1.6.1&new-version=1.7.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`89efb12`](https://github.com/ghostty-org/ghostty/commit/89efb129b8cc5ed6249a7afaa4ea3900396f87c0) build(deps): bump docker/build-push-action from 7.3.0 to 7.4.0 ([#14284](https://github.com/ghostty-org/ghostty/issues/14284)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [docker/build-push-action](https://github.com/docker/build-push-action)
  from 7.3.0 to 7.4.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/docker/build-push-action/releases">docker/build-push-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v7.4.0</h2>
  <ul>
  <li>Use the shared error helper for Buildx commands by <a
  href="https://github.com/crazy-max"><code>@​crazy-max</code></a> in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1620">docker/build-push-action#1620</a></li>
  <li>Prevent workflow command injection in metadata logs by <a
  href="https://github.com/crazy-max"><code>@​crazy-max</code></a> in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1617">docker/build-push-action#1617</a></li>
  <li>Bump <code>@​docker/actions-toolkit</code> from 0.92.0 to 0.100.0 in
  <a
  href="https://redirect.github.com/docker/build-push-action/pull/1614">docker/build-push-action#1614</a>
  <a
  href="https://redirect.github.com/docker/build-push-action/pull/1618">docker/build-push-action#1618</a>
  <a
  href="https://redirect.github.com/docker/build-push-action/pull/1621">docker/build-push-action#1621</a></li>
  <li>Bump <code>@​humanfs/node</code> from 0.16.7 to 0.16.8 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1609">docker/build-push-action#1609</a></li>
  <li>Bump brace-expansion from 1.1.13 to 1.1.18 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1592">docker/build-push-action#1592</a></li>
  <li>Bump csv-parse from 7.0.0 to 7.0.2 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1613">docker/build-push-action#1613</a></li>
  <li>Bump js-yaml from 4.3.0 to 4.3.2 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1605">docker/build-push-action#1605</a>
  <a
  href="https://redirect.github.com/docker/build-push-action/pull/1615">docker/build-push-action#1615</a></li>
  <li>Bump nanoid from 3.3.16 to 3.3.18 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1611">docker/build-push-action#1611</a></li>
  <li>Bump postcss from 8.5.10 to 8.5.25 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1590">docker/build-push-action#1590</a></li>
  <li>Bump postcss-selector-parser from 7.1.1 to 7.1.5 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1606">docker/build-push-action#1606</a></li>
  <li>Bump sigstore from 4.1.0 to 4.1.1 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1577">docker/build-push-action#1577</a></li>
  <li>Bump undici from 6.27.0 to 6.28.0 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1594">docker/build-push-action#1594</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/docker/build-push-action/compare/v7.3.0...v7.4.0">https://github.com/docker/build-push-action/compare/v7.3.0...v7.4.0</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/docker/build-push-action/commit/c3c9e263c25d99ce0380d002d59b67737d91b0dc"><code>c3c9e26</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1621">#1621</a>
  from docker/dependabot/npm_and_yarn/docker/actions-t...</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/459b6741834dcd35f946352017e7675bd2089d42"><code>459b674</code></a>
  [dependabot skip] chore: update generated content</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/4dedcb23c91d79c1629bf53ec2c3bcfffef5b34e"><code>4dedcb2</code></a>
  chore(deps): Bump <code>@​docker/actions-toolkit</code> from 0.99.0 to
  0.100.0</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/379bf63a979bd70751945601fa04c50674509952"><code>379bf63</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1620">#1620</a>
  from crazy-max/buildx-error-message</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/9877975c9e0b0b661592ff61049069507f9bc2f6"><code>9877975</code></a>
  chore: update generated content</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/7ed0556ffafb8eb312463411ef0a84a1dfe24d94"><code>7ed0556</code></a>
  use the shared Buildx error summary helper</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/91670ba5a4df99a24efff8637a78c83fd1b0f6b1"><code>91670ba</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1618">#1618</a>
  from docker/dependabot/npm_and_yarn/docker/actions-t...</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/80dbc8614a5c0ce4356740f69179cf829ecdc79a"><code>80dbc86</code></a>
  [dependabot skip] chore: update generated content</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/50cac3a3b6f55e6015d6483d1dd72a3ecb90d20d"><code>50cac3a</code></a>
  chore(deps): Bump <code>@​docker/actions-toolkit</code> from 0.98.0 to
  0.99.0</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/03b4d6cac0163b44733e1fa60adfd6da560ee4d1"><code>03b4d6c</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1617">#1617</a>
  from crazy-max/fix-metadata-workflow-commands</li>
  <li>Additional commits viewable in <a
  href="https://github.com/docker/build-push-action/compare/53b7df96c91f9c12dcc8a07bcb9ccacbed38856a...c3c9e263c25d99ce0380d002d59b67737d91b0dc">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=docker/build-push-action&package-manager=github_actions&previous-version=7.3.0&new-version=7.4.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`d3f5910`](https://github.com/ghostty-org/ghostty/commit/d3f5910cc45e53c5341b3e2dacde839b30434a6e) font: import Constraint from Glyph.zig in nerd-font codegen ([#14282](https://github.com/ghostty-org/ghostty/issues/14282)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  1c0aac54b moved RenderOptions.Constraint from face.zig to Glyph.zig and
  updated nerd_font_attributes.zig. This does the matching change to the
  generator.
  ```
- [`85bfc98`](https://github.com/ghostty-org/ghostty/commit/85bfc983a519890cf5bf2ee7f5b9542817043a1f) gtk,opengl: cleanup & fixes for [#14052](https://github.com/ghostty-org/ghostty/issues/14052) ([#14279](https://github.com/ghostty-org/ghostty/issues/14279)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes most issues mentioned in #14243, #14254 and elsewhere e.g. on
  Discord. Will add more fixes if they can be solidly reproduced.
  
  Please review each commit individually.
  ```
- [`0a08614`](https://github.com/ghostty-org/ghostty/commit/0a08614aaafe8aafd1891750b1644c631896c703) bash: detect hooks in prompt command arrays ([#14266](https://github.com/ghostty-org/ghostty/issues/14266)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The delimiter-based guard treats PROMPT_COMMAND as a semicolon-separated
  command list. Indexed array expansion joins elements with spaces
  instead, so a hook appended after an existing element is not detected
  when the integration is sourced again.
  
  Match the full internal hook command as a substring so the guard works
  for both scalar and array values. This intentionally gives up command
  boundary matching; the private function name and redirection keep an
  incidental match unlikely.
  ```
- [`1e3cd1a`](https://github.com/ghostty-org/ghostty/commit/1e3cd1a24673be7e352c1d1f716d262798d37f7f) embedded: route split and close C APIs through performBindingAction ([#14261](https://github.com/ghostty-org/ghostty/issues/14261)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Summary
  
  macOS menus call `ghostty_surface_split`, `split_focus`, and
  `request_close` directly, while keybinds go through
  `Surface.performBindingAction`. GTK already uses that path for splits
  and close. Route the embedded C APIs the same way so menus and keybinds
  share one hook.
  
  Behavior without any extra Surface hook is unchanged:
  `performBindingAction` still forwards splits to the app and
  `close_surface` still closes.
  
  ## Test plan
  
  - [x] `zig build test -Demit-macos-app=false` (compiles; these C exports
  have no unit test)
  
  ## AI disclosure
  
  This change was prepared with Cursor. I reviewed the C API routing and
  how it compares to GTK's existing `performBindingAction` path.
  
  
  Made with [Cursor](https://cursor.com)
  ```
- [`86f4490`](https://github.com/ghostty-org/ghostty/commit/86f449013ed4ca4096395de5b9798a962cce0944) Update VOUCHED list ([#14292](https://github.com/ghostty-org/ghostty/issues/14292)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14291#discussioncomment-18500537)
  from @pluiedev.
  
  Vouch: @KonstantinHudyakov
  ```
- [`87b6065`](https://github.com/ghostty-org/ghostty/commit/87b60655bffa8632bf06740291d68fb87440dfa7) Update the Norwegian translation ([@cristeahub](https://github.com/cristeahub))
  ```text
  These are mostly nitpicky changes that focuses on the following:
  
  - Consistent langauge (marker, last inn, tøm)
  - Grammatical fixes
  - Language flow improvements
  
  There are still a few things that could be changed, but I felt these
  changes are the most impactful and makes the language better.
  ```
- [`cb7db24`](https://github.com/ghostty-org/ghostty/commit/cb7db2490bb7ff3bad14a1a375c8dfb34d902e62) Update the Norwegian translation ([#14289](https://github.com/ghostty-org/ghostty/issues/14289)) ([@trag1c](https://github.com/trag1c))
  ```text
  These are mostly nitpicky changes that focuses on the following:
  
  - Consistent langauge (marker, last inn, tøm)
  - Grammatical fixes
  - Language flow improvements
  
  There are still a few things that could be changed, but I felt these
  changes are the most impactful and makes the language better.
  ```
- [`494e413`](https://github.com/ghostty-org/ghostty/commit/494e41374e536f80fafa9cb30c6d1d8cb1e77110) i18n(ru): refine Russian translation ([@derVedro](https://github.com/derVedro))
- [`57bdb8c`](https://github.com/ghostty-org/ghostty/commit/57bdb8c443e39c523d543f6c3f50a9370c35c314) i18n(ru): small fixes ([@derVedro](https://github.com/derVedro))
  ```text
  хорошо!
  ```
- [`5de703a`](https://github.com/ghostty-org/ghostty/commit/5de703a1b6ca0b91fcebe932b44be1df2de0a683) i18n: refine Russian translation ([#14257](https://github.com/ghostty-org/ghostty/issues/14257)) ([@00-kat](https://github.com/00-kat))
  ```text
  We had a small conversation in the last Russian translation PR #13809,
  and @korikhin made a good point about how the translation could be
  improved, something everyone had overlooked until then.
  ```
- [`e842d76`](https://github.com/ghostty-org/ghostty/commit/e842d763ce2f4d7739a9b405d302dafb3ce96a25) Update VOUCHED list ([#14290](https://github.com/ghostty-org/ghostty/issues/14290)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/14289#issuecomment-5728440286)
  from @trag1c.
  
  Vouch: @cristeahub
  ```

## September 16, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/35115987294)  
Summary: 1 runs • 7 commits • 4 authors

### Changes

- [`fe9cf6a`](https://github.com/ghostty-org/ghostty/commit/fe9cf6a26691fb7dbfc260eb169a801ca4b9790f) build: fully transition away from cImport/addTranslateC ([@vancluever](https://github.com/vancluever))
  ```text
  This migrates all remaining uses of cImport (and addTranslateC for good
  measure) to using translate-c for C translation, ensuring that we are
  ready for when cImport is removed from the language, and also that all
  sources of C translation are using the same snapshot of the external
  package (when can then be updated when we need to fix something).
  
  A couple of notes:
  
  * A few options have been added to support the new translations, namely
    the ability to link libraries (passed through to linkLibrary on the
    Translator side) and whether or not to initialize default values
    (looks like cImport did this without a way to control it, but
    translate-c does not do it by default).
  
  * Using the new library linking option actually simplifies the process
    of translating a number of the C packages as we have been shipping the
    necessary headers for these packages already with the applicable
    libraries. For some of the more complex translation processes though,
    we still include the appropriate directories directly.
  ```
- [`4dfa44e`](https://github.com/ghostty-org/ghostty/commit/4dfa44ecd95a9e6c72188484c2a2871298800e8a) bash: use passed exit status in precmd ([@jparise](https://github.com/jparise))
  ```text
  The Bash 4.4+ prompt hook saves the command status before doing its own
  work and passes it to __ghostty_precmd. The function ignored that
  argument and instead read the hook invocation status, causing command
  end markers to report zero.
  
  Use the explicit argument when present while retaining the current
  status fallback required by the older bash-preexec path.
  
  See #14247
  ```
- [`ed7f046`](https://github.com/ghostty-org/ghostty/commit/ed7f046ee4dee89e5e8bbbecbc67ee14ac1f10d1) bash: recognize attributed prompt command arrays ([@jparise](https://github.com/jparise))
  ```text
  Bash includes additional variable attributes in declare output, so an
  exported indexed array is reported with an -ax prefix instead of -a.
  Match the indexed-array prefix without requiring a following space so
  these values continue through the array-preserving path.
  ```
- [`591ccac`](https://github.com/ghostty-org/ghostty/commit/591ccacbdfa59945cb4f5b015390d0b8d416a7f0) bash: preserve exit status across prompt commands ([@jparise](https://github.com/jparise))
  ```text
  Existing scalar PROMPT_COMMAND entries can overwrite the last command's
  status before Ghostty's appended hook runs. Capture and restore the
  status before those commands, then consume the saved value in the final
  hook.
  
  Keep array hooks as independent entries because Bash 5.1 and newer
  restore the original status for each entry. Preserve the existing
  PROMPT_COMMAND type and safely handle inherited prompt commands where
  Ghostty's function definitions are absent.
  
  This retains the fast Bash 4.4+ PS0 integration rather than using
  bash-preexec's DEBUG trap.
  
  See #14247
  ```
- [`8482d54`](https://github.com/ghostty-org/ghostty/commit/8482d5454e0eee8329cadf2711be78c40298b6ec) bash: fix OSC 133;D status always zero ([#14250](https://github.com/ghostty-org/ghostty/issues/14250)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The Bash 4.4+ prompt hook saves the command status before doing its own
  work and passes it to __ghostty_precmd. The function ignored that
  argument and instead read the hook invocation status, causing command
  end markers to report zero.
  
  Also, existing scalar PROMPT_COMMAND entries can overwrite the last
  command's status before Ghostty's appended hook runs. Capture and
  restore the status before those commands, then consume the saved value
  in the final hook.
  
  Fixes #14247
  ```
- [`8fff9d6`](https://github.com/ghostty-org/ghostty/commit/8fff9d6e98ccb37930629429dafdb02ff97faaea) build: fully transition away from cImport/addTranslateC ([#14246](https://github.com/ghostty-org/ghostty/issues/14246)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This migrates all remaining uses of `cImport` (and `addTranslateC` for
  good measure) to using translate-c for C translation, ensuring that we
  are ready for when `cImport` is removed from the language, and also that
  all sources of C translation are using the same snapshot of the external
  package (when can then be updated when we need to fix something).
  
  A couple of notes:
  
  * A few options have been added to support the new translations, namely
  the ability to link libraries (passed through to `linkLibrary` on the
  Translator side) and whether or not to initialize default values (looks
  like `cImport` did this without a way to control it, but translate-c
  does not do it by default).
  
  * Using the new library linking option actually simplifies the process
  of translating a number of the C packages as we have been shipping the
  necessary headers for these packages already with the applicable
  libraries. For some of the more complex translation processes though, we
  still include the appropriate directories directly.
  ```
- [`f9a3f24`](https://github.com/ghostty-org/ghostty/commit/f9a3f24a56bf05f70894e1a084809d4fffadf420) Update VOUCHED list ([#14256](https://github.com/ghostty-org/ghostty/issues/14256)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14249#discussioncomment-18467661)
  from @mitchellh.
  
  Vouch: @MisterTea
  ```

## September 15, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/34933551563)  
Summary: 1 runs • 1 commits • 1 authors

### Changes

- [`d4c88d8`](https://github.com/ghostty-org/ghostty/commit/d4c88d8069912b653d707191388ca98e24751f12) Update VOUCHED list ([#14241](https://github.com/ghostty-org/ghostty/issues/14241)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14240#discussioncomment-18444371)
  from @jcollie.
  
  Vouch: @JuaniRaggio
  ```

