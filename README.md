> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: September 19, 2026 at 19:56 UTC.

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

## September 14, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/34895432872), [2](https://github.com/ghostty-org/ghostty/actions/runs/34891901089), [3](https://github.com/ghostty-org/ghostty/actions/runs/34849215429), [4](https://github.com/ghostty-org/ghostty/actions/runs/34791379020)  
Summary: 4 runs • 83 commits • 13 authors

### Changes

- [`4c7496c`](https://github.com/ghostty-org/ghostty/commit/4c7496c03541a62b9721da772e786bfe99e02849) i18n: update Lithuanian translation for v1.4 ([@tdslot](https://github.com/tdslot))
  ```text
  Translate all 181 missing strings, including the command palette entries.
  
  AI-assisted with Pi using OpenAI Codex (gpt-5.6-sol) to draft the translations and run gettext checks. I manually reviewed all translations. msgfmt and msgcmp checks pass.
  
  Related to #13766
  ```
- [`3e08654`](https://github.com/ghostty-org/ghostty/commit/3e08654225115eabd693d16f2f70135257a6a872) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`167ed57`](https://github.com/ghostty-org/ghostty/commit/167ed5788f804160c1a9c282b838a08639a50ec7) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`bd42267`](https://github.com/ghostty-org/ghostty/commit/bd4226741b7351a88303db269fb23610b663bef4) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`f8304c0`](https://github.com/ghostty-org/ghostty/commit/f8304c01f7c50a27b7047fce988826fca151cb51) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`e9693a4`](https://github.com/ghostty-org/ghostty/commit/e9693a4a2f5fe9083815eee117d8ace67be3ad5d) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`0f03d15`](https://github.com/ghostty-org/ghostty/commit/0f03d156c0e146c0645b501dd1aa0aed31681932) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`b3f4dbb`](https://github.com/ghostty-org/ghostty/commit/b3f4dbb37fb92170d7c31352704a7d0d1239cd2e) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`57b3122`](https://github.com/ghostty-org/ghostty/commit/57b312293d32d9d707a95759908468e5638f324b) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`dc2d6f1`](https://github.com/ghostty-org/ghostty/commit/dc2d6f1b3ad796ee511d7e69ceababfe5efe9941) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`eba2ec9`](https://github.com/ghostty-org/ghostty/commit/eba2ec988dbd4063f1072d310f87706dec5d2ca5) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`1779cab`](https://github.com/ghostty-org/ghostty/commit/1779cabf425421e3ec30c0e1463163107d85e1c4) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`58dd6d7`](https://github.com/ghostty-org/ghostty/commit/58dd6d777a77e5f49398a085610ee9c80cbb714a) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`a44c474`](https://github.com/ghostty-org/ghostty/commit/a44c47477ea49d5719d9eee488670fff8444ca4f) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`4df91b3`](https://github.com/ghostty-org/ghostty/commit/4df91b3fc7292c5929f7d834e90dfc29c5eb00e2) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`ab26bb4`](https://github.com/ghostty-org/ghostty/commit/ab26bb4b2ae5a2139fd41740c5fe531f088ade9e) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`7d355b8`](https://github.com/ghostty-org/ghostty/commit/7d355b8a0b09f9175ead9c61083e646ff23c19cf) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`d405da4`](https://github.com/ghostty-org/ghostty/commit/d405da4452dd5377232e44a1156ae46f7f89c4e0) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`6633869`](https://github.com/ghostty-org/ghostty/commit/6633869d8b44f527f3a9920963f263147840d52e) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`18d323d`](https://github.com/ghostty-org/ghostty/commit/18d323d24c19780fb041c1ba70dde4a439faa536) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`7a82211`](https://github.com/ghostty-org/ghostty/commit/7a8221113f761cc38e96e15e0da48eb687a3d3e6) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`7d6c090`](https://github.com/ghostty-org/ghostty/commit/7d6c090a7d3c1238fa5397bfafe0a4ca37caaddf) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`56b739c`](https://github.com/ghostty-org/ghostty/commit/56b739cc3188f53aa5ebd4e0021691831c2084bc) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`85508ca`](https://github.com/ghostty-org/ghostty/commit/85508ca2c9568b8204f37e1cb78344f0673ec9ad) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`05dd3c5`](https://github.com/ghostty-org/ghostty/commit/05dd3c53a7ed47d387d22db4a1e36fc172d6f06b) Update po/lt.po ([@tdslot](https://github.com/tdslot))
- [`159be4d`](https://github.com/ghostty-org/ghostty/commit/159be4d3c2186377884f77794a8d0aa874954d0b) Update po/lt.po ([@tdslot](https://github.com/tdslot))
  ```text
  Here translate correction isn't exact, but probably depend of context. In English version there is no word "exact".
  ```
- [`6f6da70`](https://github.com/ghostty-org/ghostty/commit/6f6da700ede0289ecb534a726b0b13c584a23f8e) Merge branch 'ghostty-org:main' into i18n-update-translation-lt-for-v1.4 ([@tdslot](https://github.com/tdslot))
- [`ff5b87e`](https://github.com/ghostty-org/ghostty/commit/ff5b87e4dbef56cd6b54174520ed151b88c47368) i18n: re-apply remaining lt.po review suggestions ([@tdslot](https://github.com/tdslot))
  ```text
  Eleven review suggestions from the PR were accepted but never made it
  into the pushed commit. Re-apply them and rewrap the affected entries to
  the canonical 79-column gettext width.
  
  Claude-Session: https://claude.ai/code/session_019aW9GqQj7USLWhmzNhuE34
  ```
- [`607d59b`](https://github.com/ghostty-org/ghostty/commit/607d59b0e8ef46da6e6e6e490ef8e82f961ffb25) i18n: fix Lithuanian grammar and terminology consistency in lt.po ([@tdslot](https://github.com/tdslot))
  ```text
  The wording follows the consultation bank of the VLKK (State Commission
  of the Lithuanian Language) rather than personal preference; the
  relevant entries are cited per change.
  
  - "padalinti" -> "padalyti" (9 strings). VLKK treats "dalyti" and
    "dalinti" as equal variants of the norm, prefixed derivatives
    explicitly included ("padalyti ir padalinti"), but advises picking one
    per text: "Viename tekste patartina pasirinkti vieną kurį variantą ir
    nuosekliai jį vartoti. Nereikėtų kaitalioti ir iš veiksmažodžio dalyti
    ir jo formų padarytų įsigalėjusių terminų."
    https://vlkk.lt/konsultacijos/4607-dalyti-dalinti
    The file was mixing them: the verb was "padalinti" while the noun
    everywhere was "padalijimas", which is formed from "dalyti". Unified
    on the "dalyti" line, since the established noun already commits the
    file to it, and it is also the primary variant in "Kalbos patarimai"
    (Vilnius, 2002, p. 69).
  
  - "atstatyti" -> "atkurti" / "nustatyti iš naujo" (7 strings). VLKK:
    "Veiksmažodis atstatyti reikšme 'grąžinti kokį dalyką į buvusią
    (nesusijusią su stovėjimu) padėtį' [...] vertinamas kaip verstinis ir
    vengtinas vartoti. Vartotini junginiai su veiksmažodžiais grąžinti,
    atkurti ar pan."
    https://vlkk.lt/konsultacijos/12800-atstatyti
    https://vlkk.lt/konsultacijos/235-atstatyti
    Restoring a default font or window size is exactly that sense, so
    "Reset Font Size" / "Reset Window Size" are now "Atkurti...". The file
    already used "atkurti" in "Išdidinti arba atkurti langą". Plain
    "Reset" and "Reset Terminal" re-initialise rather than restore a
    previous value, so those became "Nustatyti (terminalą) iš naujo".
  
  - "selection" is now consistently "pažymėtas tekstas" / "pažymėjimas"
    (26 strings). It had been split between that and "pasirinkimas",
    which means "a choice" -- the sense the file already uses it in for
    "Remember choice for this split".
  
  - "Toggle Fullscreen" now uses the same "Įjungti arba išjungti" pattern
    as the other on/off toggles.
  
  - "Equalize Splits" is plural, agreeing with its own description.
  
  - Unify the HTML "paste path" description with its plain/ANSI siblings,
    and minor wording fixes to the tagline and the $EDITOR description.
  
  Claude-Session: https://claude.ai/code/session_019aW9GqQj7USLWhmzNhuE34
  ```
- [`661e1e7`](https://github.com/ghostty-org/ghostty/commit/661e1e77f445057312666a74d9f5002e82f81764) i18n: update Lithuanian translation for v1.4 ([#13777](https://github.com/ghostty-org/ghostty/issues/13777)) ([@trag1c](https://github.com/trag1c))
  ```text
  Updates the Lithuanian translation for v1.4 and fills all 181 missing
  strings, including the command palette entries.
  
  Related to #13766.
  
  Validation:
  - Manually reviewed all translated strings
  - `msgfmt --check --check-compatibility --check-accelerators` passes
  - `msgcmp` against the translation template passes
  
  AI usage: I used Pi with OpenAI Codex (gpt-5.6-sol) to draft the
  translations and run gettext checks. I manually reviewed all
  translations before submitting.
  ```
- [`6542288`](https://github.com/ghostty-org/ghostty/commit/65422886645f0df601894b9571cb23f583f68caf) Start Italian translation for 1.4 ([@Misairuzame](https://github.com/Misairuzame))
- [`c488a41`](https://github.com/ghostty-org/ghostty/commit/c488a41b0673ec45e2dab28d0c8b6072b7da709f) nix: add libglvnd to devShell for EGL ([@pluiedev](https://github.com/pluiedev))
- [`fa2ec3a`](https://github.com/ghostty-org/ghostty/commit/fa2ec3a6a890c0d4e4d550564a8e37dc83d047ef) pkg/opengl: add EGL headers and bindings ([@pluiedev](https://github.com/pluiedev))
  ```text
  We need this for exporting DMABUFs and creating our own GL context
  independent of GTK.
  ```
- [`7581009`](https://github.com/ghostty-org/ghostty/commit/75810091686f5ee28d37550c4a7bb07eedaa51da) build: link against libEGL ([@pluiedev](https://github.com/pluiedev))
- [`2f0b653`](https://github.com/ghostty-org/ghostty/commit/2f0b65346918047518e7b32f9bbfa1240c15b62e) gtk,opengl: free us from the clutches of GtkGLArea ([@pluiedev](https://github.com/pluiedev))
  ```text
  GtkGLArea had numerous downsides that forced us to invent unsightly hacks
  in our renderer to work around them, most chiefly the fact that it holds
  its own GdkGLContext on the main thread (GL contexts are not at all
  thread-safe), forcing us to keep our GL calls on the main thread.
  It also does not interact well with triple-buffering and initialization
  is forced to be this sort of deferred song-and-dance since we need to
  wait for the GLArea to initialize its GL context before we can initialize
  the renderer, the core surface, and then most things in the GTK surface.
  
  We instead invent our own custom widget named RenderSurface that takes
  simple DMABUFs and displays them. The task of obtaining a GL context
  falls to manual EGL bindings, since we also need EGL to export OpenGL
  textures into DMABUFs. We keep the EGL context solely on the render
  thread meaning that the main thread never concerns itself with rendering
  except when being notified that the renderer has pushed a new frame.
  
  What makes this extra significant is that now the entire GTK apprt no
  longer depends on OpenGL in any way, shape or form. As long as it is
  being fed DMABUFs, it can render from whichever graphics API you want.
  This means we can add more backends based on OpenGL ES or more likely
  Vulkan rather painlessly in the future.
  
  **AI disclosure**: I came up with the idea and let Pi implement most of
  the nitty-gritty details around EGL, as well as replumbing the renderer
  and cleaning up all the GTK-specific workarounds there. I then carefully
  vetted every line of code and spent roughly as much time reviewing as
  coding. Most of the documentation and all commit messages are in my
  own words.
  ```
- [`380778e`](https://github.com/ghostty-org/ghostty/commit/380778e3ca8bd4083c76ce721f28417e0eacf396) ci: drop libghostty-internal builds on Windows ([@pluiedev](https://github.com/pluiedev))
  ```text
  libghostty-internal isn't really supposed to be used in Windows anyway,
  so why bother testing it?
  ```
- [`a5f604d`](https://github.com/ghostty-org/ghostty/commit/a5f604da718f600088504a37083ae1d160121af0) renderer: make LatestFrame methods no-ops when ExportedFrame is void ([@pluiedev](https://github.com/pluiedev))
- [`4c89835`](https://github.com/ghostty-org/ghostty/commit/4c8983586c4fcdeb0a13bc36a1820e5617c3877f) gtk: initialize core surface on first resize ([@pluiedev](https://github.com/pluiedev))
  ```text
  Now that our core surface does not depend on any GTK-sided OpenGL
  initialization, we can initialize it a lot earlier than before, during
  the first resize event right after GTK allocates the size for the widget.
  ```
- [`b87af86`](https://github.com/ghostty-org/ghostty/commit/b87af8646f71de1398e665c361fe659b0707a72e) pkg/opengl: replace cImport with translate-c ([@pluiedev](https://github.com/pluiedev))
  ```text
  General Zig 0.16+ futureproofing
  ```
- [`adf1614`](https://github.com/ghostty-org/ghostty/commit/adf161473d983986f48c9650152f707bd285d931) pkg/opengl: polish API ([@pluiedev](https://github.com/pluiedev))
- [`45aa963`](https://github.com/ghostty-org/ghostty/commit/45aa963d6b634f8d3e4e9a9ecdd272bf8ad751dd) opengl: delay opengl flush ([@pluiedev](https://github.com/pluiedev))
  ```text
  See https://github.com/ghostty-org/ghostty/pull/14052#issuecomment-5521325497
  ```
- [`ce5d51f`](https://github.com/ghostty-org/ghostty/commit/ce5d51f46f97e5321267abab488ff5d0fdabb2f6) gtk/render_surface: report dmabuf build errors ([@pluiedev](https://github.com/pluiedev))
- [`202fa8e`](https://github.com/ghostty-org/ghostty/commit/202fa8e39007ccbcc267173f1217422d1ac72736) gtk: do not disable OpenGL ES and Vulkan ([@pluiedev](https://github.com/pluiedev))
  ```text
  Apparently either OpenGL ES or Vulkan is required to present our DMABUFs
  for jcollie
  ```
- [`5728672`](https://github.com/ghostty-org/ghostty/commit/57286723d0529dbe10890b84e05baa682f7e9d56) nix: update zon2nix to 0.7.0 ([@jcollie](https://github.com/jcollie))
  ```text
  1. Speeds up runs by ~3x for projects with a large number of
  dependencies by downloading in parallel (~55s → 16s on my workstation).
  
  2. Adds some workarounds for Zig 0.16's package management. The changes
  don't affect Ghostty itself, but do affect downstream projects that
  embed libghostty-vt and want to create Nix packages of their own.
  ```
- [`f5efbae`](https://github.com/ghostty-org/ghostty/commit/f5efbaee5f3bec4de688ba188b51f5bd5b5059a3) nix: use hardlinks ([@jcollie](https://github.com/jcollie))
  ```text
  Zig doesn't like symlinks in some situations.
  ```
- [`13a21fc`](https://github.com/ghostty-org/ghostty/commit/13a21fc047d26827ee324268de427f0862289ab6) nix: use --reflink=auto instead of --link ([@jcollie](https://github.com/jcollie))
  ```text
  Another Zig build system quirk worked around.
  ```
- [`d08ebcc`](https://github.com/ghostty-org/ghostty/commit/d08ebcc867285a3c320144a6d10517b4c40d0790) Keep working on italian translation on 1.4 ([@Misairuzame](https://github.com/Misairuzame))
- [`69f42c1`](https://github.com/ghostty-org/ghostty/commit/69f42c1a30593bdeb7588c8e66586f8bb9e2ca06) Use 'riquadro' instead of 'divisione' for 'Split' ([@Misairuzame](https://github.com/Misairuzame))
- [`d00a498`](https://github.com/ghostty-org/ghostty/commit/d00a498274f321b8808ba89d63c4e23d93a7d8e0) opengl: flip Y axis during framebuffer blit ([@pluiedev](https://github.com/pluiedev))
- [`4dac203`](https://github.com/ghostty-org/ghostty/commit/4dac203c3f6da1c3ec884e71b1cdc6a428b7a8e5) Finish italian translation for 1.4 ([@Misairuzame](https://github.com/Misairuzame))
- [`74e47a7`](https://github.com/ghostty-org/ghostty/commit/74e47a706f95f7fabaa4ea7c7a0cf25ffae21bd2) macOS: fix title bar clipping custom font ([@bo2themax](https://github.com/bo2themax))
  ```text
  The #9168 fix is no longer needed, since the frame is now higher than the actual glyph.
  ```
- [`ef7edc4`](https://github.com/ghostty-org/ghostty/commit/ef7edc4a24cf3ef0d6862276602e09f7b4b11b40) gtk/build: speed up repeated builds by letting the Zig build cache work ([@jcollie](https://github.com/jcollie))
  ```text
  Repeated builds were penalized for three reasons:
  
  1. The gresource XML embedded the absolute cache paths of the compiled
  .ui files. It now uses relative paths, resolved against a `--sourcedir`
  passed to glib-compile-resources.
  
  2. Blueprints were compiled through a small Zig wrapper, and a Run step
  hashes the bytes of the executable it runs. A Zig binary does not relink
  to the same bytes, so after a branch switch that touched the wrapper
  every .ui moved, the gresource compiler re-ran and the whole app
  recompiled for identical output. blueprint-compiler is now run directly
  and the wrapper is reduced to a single version check whose output
  nothing reads.
  
  3. The gresource pipeline was built once per artifact. It is now
  memoized on the *std.Build.
  
  Cold builds and builds after real blueprint changes are unaffected. A
  build after the wrapper relinks goes from ~43s to ~7s on my system.
  
  AI disclosure: Claude Opus 5 was used to pinpoint the source of the
  cache poisoning and to prepare a patch. Claude Fable 5.1 measured it,
  traced the remaining churn to the wrapper's relinks, and replaced a
  custom build step with stock ones. The commit message is human-written
  based on the author's understanding of the changes.
  
  Claude-Session: https://claude.ai/code/session_01RsfB3eoSTLfnKa6zi25teN
  ```
- [`55c3e8c`](https://github.com/ghostty-org/ghostty/commit/55c3e8cc0da32921aded5bda5f4de70e69bc0888) First review feedback ([@Misairuzame](https://github.com/Misairuzame))
- [`5beb94c`](https://github.com/ghostty-org/ghostty/commit/5beb94c1620e5f9e880db002d84b95f84cbf25de) renderer: apply font-thicken to IME preedit text ([@helium777](https://github.com/helium777))
  ```text
  IME preedit text was rendered with unthickened glyphs because
  addPreeditCell omitted font_thicken options when calling
  renderCodepoint, leaving them at their default false values.
  
  Fixes #13758
  ```
- [`45058d7`](https://github.com/ghostty-org/ghostty/commit/45058d768991e49d74dd699e012fb0610bc8ae6f) Review feedback ([@Misairuzame](https://github.com/Misairuzame))
- [`962a060`](https://github.com/ghostty-org/ghostty/commit/962a060c86ec518baaf3f54ea51337e8259803ff) macOS: fix title bar clipping custom font ([#14217](https://github.com/ghostty-org/ghostty/issues/14217)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes https://github.com/ghostty-org/ghostty/issues/14135.
  
  <img width="1398" height="652" alt="image"
  src="https://github.com/user-attachments/assets/6901a05e-9d23-4e25-89a7-c16c1694a0f9"
  />
  
  
  > The #9168 fix is no longer needed, since the frame is now higher than
  the actual glyph.
  
  The frame change observation only affects those who have a custom window
  title font set in their config. I asked Claude to run some main thread
  benchmarking compared to `main`; it will gain some delays for rapid
  title changes and window resizing. The additional cost is brought by the
  frequent frame updates which are done by AppKit. But that's necessary
  for updating the title to the correct style.
  
  > I tried to do some diffing and removing duplicates, but it will add
  too many changes too, and I didn't think it's worth doing so.
  
  The amount looks ok to me.
  
  ### `window-title-font-family = PT Mono`
  
  | Phase | Metric | base | branch | Δ | ratio |
  |---|---|---:|---:|---:|---:|
  | Idle, 3 s | main-thread CPU | 2.8 ms | 2.8 ms | -0.0 | 1.00 |
  |  | process CPU | 11.3 ms | 11.2 ms | -0.1 | 0.99 |
  | Paced title updates, 150 × 100 ms | main-thread CPU | 878.5 ms |
  **946.7 ms** | **+68.3** | **1.08** |
  |  | process CPU | 1219.9 ms | 1335.0 ms | +115.1 | 1.09 |
  |  | wall | 17.24 s | 17.34 s | +0.1 | 1.01 |
  | Title burst, 5000 back-to-back | main-thread CPU | 180.7 ms | 181.4 ms
  | +0.7 | 1.00 |
  |  | process CPU | 254.2 ms | 254.8 ms | +0.6 | 1.00 |
  |  | wall | 2.31 s | 2.32 s | +0.0 | 1.00 |
  | `toggle_maximize` × 16 (animated resize) | main-thread CPU | 1947.8 ms
  | **2178.0 ms** | **+230.2** | **1.12** |
  |  | process CPU | 4166.8 ms | 4403.2 ms | +236.4 | 1.06 |
  |  | wall | 16.68 s | 16.72 s | +0.0 | 1.00 |
  | Native fullscreen enter/exit × 2 | main-thread CPU | 196.8 ms | 195.9
  ms | -0.9 | 1.00 |
  |  | process CPU | 360.8 ms | 361.5 ms | +0.7 | 1.00 |
  |  | wall | 8.47 s | 8.47 s | +0.0 | 1.00 |
  
  ### AI Disclosure
  
  Asked Claude to generate the harness to run the benchmark and review my
  changes. I did the changes myself.
  ```
- [`1ab2501`](https://github.com/ghostty-org/ghostty/commit/1ab2501e79b7f1b204896a1009cd6566c93f4e46) gtk/build: speed up repeated builds by letting the Zig build cache work ([#14212](https://github.com/ghostty-org/ghostty/issues/14212)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Repeated builds were penalized for three reasons:
  
  1. The gresource XML embedded the absolute cache paths of the compiled
  .ui files. It now uses relative paths, resolved against a `--sourcedir`
  passed to glib-compile-resources.
  
  2. Blueprints were compiled through a small Zig wrapper, and a Run step
  hashes the bytes of the executable it runs. A Zig binary does not relink
  to the same bytes, so after a branch switch that touched the wrapper
  every .ui moved, the gresource compiler re-ran and the whole app
  recompiled for identical output. blueprint-compiler is now run directly
  and the wrapper is reduced to a single version check whose output
  nothing reads.
  
  3. The gresource pipeline was built once per artifact. It is now
  memoized on the *std.Build.
  
  Cold builds and builds after real blueprint changes are unaffected. A
  build after the wrapper relinks goes from ~43s to ~7s on my system.
  
  AI disclosure: Claude Opus 5 was used to pinpoint the source of the
  cache poisoning and to prepare a patch. Claude Fable 5.1 measured it,
  traced the remaining churn to the wrapper's relinks, and replaced a
  custom build step with stock ones. The commit message is human-written
  based on the author's understanding of the changes.
  ```
- [`d30379c`](https://github.com/ghostty-org/ghostty/commit/d30379c5b9e3dad0963a0c6881896b9b38963801) nix: update zon2nix to 0.7.0 ([#14192](https://github.com/ghostty-org/ghostty/issues/14192)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  1. Speeds up runs by ~3x for projects with a large number of
  dependencies by downloading in parallel (~55s → 16s on my workstation).
  
  2. Adds some workarounds for Zig 0.16's package management. The changes
  don't affect Ghostty itself, but do affect downstream projects that
  embed libghostty-vt and want to create Nix packages of their own.
  
  AI disclosure: Claude was used to diagnose CI failures and suggest
  fixes.
  ```
- [`49b95d8`](https://github.com/ghostty-org/ghostty/commit/49b95d846621469ebc5950fd005fa57bcc160d85) gtk,opengl: free us from the clutches of GtkGLArea ([#14052](https://github.com/ghostty-org/ghostty/issues/14052)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  GtkGLArea had numerous downsides that forced us to invent unsightly
  hacks in our renderer to work around them, most chiefly the fact that it
  holds its own GdkGLContext on the main thread (GL contexts are not at
  all thread-safe), forcing us to keep our GL calls on the main thread. It
  also does not interact well with triple-buffering and initialization is
  forced to be this sort of deferred song-and-dance since we need to wait
  for the GLArea to initialize its GL context before we can initialize the
  renderer, the core surface, and then most things in the GTK surface.
  
  We instead invent our own custom widget named RenderSurface that takes
  simple DMABUFs and displays them. The task of obtaining a GL context
  falls to manual EGL bindings, since we also need EGL to export OpenGL
  textures into DMABUFs. We keep the EGL context solely on the render
  thread meaning that the main thread never concerns itself with rendering
  except when being notified that the renderer has pushed a new frame.
  
  What makes this extra significant is that now the entire GTK apprt no
  longer depends on OpenGL in any way, shape or form. As long as it is
  being fed DMABUFs, it can render from whichever graphics API you want.
  This means we can add more backends based on OpenGL ES or more likely
  Vulkan rather painlessly in the future.
  
  **AI disclosure**: I came up with the idea and let Pi implement most of
  the nitty-gritty details around EGL, as well as replumbing the renderer
  and cleaning up all the GTK-specific workarounds there. I then carefully
  vetted every line of code and spent roughly as much time reviewing as
  coding. Most of the documentation and all commit messages are in my own
  words.
  ```
- [`b38394a`](https://github.com/ghostty-org/ghostty/commit/b38394ae3407a4c4c27102517c03384bec89a560) i18n: it_IT translations for 1.4 ([#13996](https://github.com/ghostty-org/ghostty/issues/13996)) ([@00-kat](https://github.com/00-kat))
- [`6ab34ca`](https://github.com/ghostty-org/ghostty/commit/6ab34cad2d1a91a6282c088e448256248aadda0c) gtk: remove unused blueprint using statement ([@tristan957](https://github.com/tristan957))
- [`9dc0d97`](https://github.com/ghostty-org/ghostty/commit/9dc0d974e62d4a98f55680a58fa574949f4bf134) terminal: answer ANSI DECRQM queries ([@mitchellh](https://github.com/mitchellh))
  ```text
  #14225
  
  Handle the ANSI form of DECRQM (`CSI Ps $ p`), as specified by the
  VT510 reference [1] and xterm [2]. Previously, only the DEC private
  form reached the mode query handler.
  
  [1] https://vt100.net/docs/vt510-rm/DECRQM.html
  [2] https://invisible-island.net/xterm/ctlseqs/ctlseqs.txt
  ```
- [`ec98864`](https://github.com/ghostty-org/ghostty/commit/ec98864737dbf1ccbb6c44b7f72096479b847565) gtk: remove unused blueprint using statement ([#14235](https://github.com/ghostty-org/ghostty/issues/14235)) ([@mitchellh](https://github.com/mitchellh))
- [`3beb6d7`](https://github.com/ghostty-org/ghostty/commit/3beb6d717ac305e6a3c7b152103a6f7e81d8e3cf) terminal: decrqm don't truncate 16-bit mode requests ([@mitchellh](https://github.com/mitchellh))
  ```text
  DECRQM requests can use a full 16-bit number but we truncated to 15-bits
  for the reply (cause thats all we know about). Preserve, the full
  16-bits for requests so we give the proper response.
  ```
- [`88abb77`](https://github.com/ghostty-org/ghostty/commit/88abb77b17ba0028d41d6731a1521f318d31f777) renderer: apply font-thicken to IME preedit text ([#14230](https://github.com/ghostty-org/ghostty/issues/14230)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Fixes #13758
  
  ### Problem
  
  With `font-thicken = true` on macOS, IME preedit (composing) text
  renders noticeably thinner than committed text.
  
  ### Cause & Fix
  Committed and preedit text diverge in `src/renderer/generic.zig`:
  
  ```text
  Committed: Shaper -> addGlyph -> renderGlyph(..., { .thicken = config.font_thicken, ... })
  Preedit: State -> addPreeditCell -> renderCodepoint(..., { .grid_metrics })
  ```
  
  Fix: Pass `self.config.font_thicken` and
  `self.config.font_thicken_strength` in `addPreeditCell`.
  
  ### Testing
  
  - Verified on macOS with `font-thicken = true`.
  - Verified with `zig fmt --check`.
  
  ### AI Disclosure
  
  AI (gemini-3.8-flash) assisted in tracing the call path; manually
  verified and tested.
  ````
- [`1f225eb`](https://github.com/ghostty-org/ghostty/commit/1f225ebb5894189aa9e12cf3a371f787e574c5f4) terminal: answer ANSI DECRQM queries ([#14236](https://github.com/ghostty-org/ghostty/issues/14236)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  #14225
  
  Handle the ANSI form of DECRQM (`CSI Ps $ p`), as specified by the VT510
  reference [1] and xterm [2]. Previously, only the DEC private form
  reached the mode query handler.
  
  [1] https://vt100.net/docs/vt510-rm/DECRQM.html
  [2] https://invisible-island.net/xterm/ctlseqs/ctlseqs.txt
  ```
- [`148681e`](https://github.com/ghostty-org/ghostty/commit/148681e0aab45ea84386a7839a26db3e5015cfcd) terminal: decrqm don't truncate 16-bit mode requests ([#14237](https://github.com/ghostty-org/ghostty/issues/14237)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  DECRQM requests can use a full 16-bit number but we truncated to 15-bits
  for the reply (cause thats all we know about). Preserve, the full
  16-bits for requests so we give the proper response.
  ```
- [`ba8690c`](https://github.com/ghostty-org/ghostty/commit/ba8690c42088c4dbaaf51e983a31f424a1610b01) i18n(de): Typo fix ([@derVedro](https://github.com/derVedro))
- [`8b5678b`](https://github.com/ghostty-org/ghostty/commit/8b5678bd16df3f3ff0b58d533812c2e04e9dfb5a) i18n(de): German translation improvements ([@derVedro](https://github.com/derVedro))
- [`1266c0a`](https://github.com/ghostty-org/ghostty/commit/1266c0a32aca8faff43881f30176f56dd498c0d0) i18n: update `de_DE` translations ([@rpfaeffle](https://github.com/rpfaeffle))
- [`b32b2f8`](https://github.com/ghostty-org/ghostty/commit/b32b2f87ae478fa195a1e44737648f46ba95d51f) i18n(de): Typo fix ([@derVedro](https://github.com/derVedro))
- [`fee8cb5`](https://github.com/ghostty-org/ghostty/commit/fee8cb523709d89c986421cee844ee53137c2793) i18n(de): Wording plain text ([@derVedro](https://github.com/derVedro))
- [`4cc8fa3`](https://github.com/ghostty-org/ghostty/commit/4cc8fa3359fe3368859b7e226cc28ba93d78d3d1) i18n(de): Fix accidental deletion ([@derVedro](https://github.com/derVedro))
- [`9c4a5a8`](https://github.com/ghostty-org/ghostty/commit/9c4a5a8998bd5fb5f139dce35b7da84b287ca0ae) i18n(de): German translation improvements ([@derVedro](https://github.com/derVedro))
- [`3879bff`](https://github.com/ghostty-org/ghostty/commit/3879bff33d279990539e563d5e40e0368f515665) i18n(de): Wording plain text ([@derVedro](https://github.com/derVedro))
- [`1aaca23`](https://github.com/ghostty-org/ghostty/commit/1aaca23e35f0fac52120d9c4be7a8300b7b5734d) i18n(de): Fix accidental deletion ([@derVedro](https://github.com/derVedro))
- [`5e61670`](https://github.com/ghostty-org/ghostty/commit/5e6167072624f672ac21c3cfc0eef83bb95bec88) i18n(de): update German translation ([@derVedro](https://github.com/derVedro))
- [`e3849b7`](https://github.com/ghostty-org/ghostty/commit/e3849b7a674f5c681ec7d22050f5c4aa26bf83a7) i18n(de): update German translation ([@derVedro](https://github.com/derVedro))
- [`05fcdcc`](https://github.com/ghostty-org/ghostty/commit/05fcdccfedae9d7d3fd5c640ac448fa72f58e696) Merge branch 'i18n/de_DE' into german-supplements ([@derVedro](https://github.com/derVedro))
- [`5833977`](https://github.com/ghostty-org/ghostty/commit/583397756d56b0e2bf8050cd67371389c695a53b) i18n(de): additional improvements ([@rpfaeffle](https://github.com/rpfaeffle))
- [`50f757d`](https://github.com/ghostty-org/ghostty/commit/50f757dc84c1179fe55ee396fb00268ae8dab0b9) i18n(de): adjust floating state description ([@rpfaeffle](https://github.com/rpfaeffle))
- [`d5eba8d`](https://github.com/ghostty-org/ghostty/commit/d5eba8d169545cc29d5ee9796ba37ff29759f4db) i18n: update `de_DE` translations ([#13846](https://github.com/ghostty-org/ghostty/issues/13846)) ([@00-kat](https://github.com/00-kat))
  ```text
  Part of #13766.
  ```
- [`0c2a290`](https://github.com/ghostty-org/ghostty/commit/0c2a290d3a3e2a599be3a43435d778a5896667ee) Sync CODEOWNERS vouch list ([#14229](https://github.com/ghostty-org/ghostty/issues/14229)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Sync CODEOWNERS owners with vouch list.
  
  ## Added Users
  
  - @ibaios
  ```

## September 13, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/34768241847), [2](https://github.com/ghostty-org/ghostty/actions/runs/34754840764), [3](https://github.com/ghostty-org/ghostty/actions/runs/34737770142)  
Summary: 3 runs • 5 commits • 4 authors

### Changes

- [`1a8f331`](https://github.com/ghostty-org/ghostty/commit/1a8f331f16b36717f457306753352f260c2ccdb5) macOS: implement move_tab_to_new_window ([@pedronaugusto](https://github.com/pedronaugusto))
  ```text
  The action and its keybind exist, and GTK implements them, but macOS had no
  handler so the binding did nothing there. AppKit already has the command for
  window tabs, so this forwards to it.
  
  A window that isn't in a tab group, or is alone in one, is already a window of
  its own, so there is nothing to move and the action reports it did nothing.
  
  Implements the remaining macOS half of #2630.
  ```
- [`7aab0a0`](https://github.com/ghostty-org/ghostty/commit/7aab0a0392369613472bd5dcfd66bef58e78c3ec) macOS: implement move_tab_to_new_window ([#14216](https://github.com/ghostty-org/ghostty/issues/14216)) ([@bo2themax](https://github.com/bo2themax))
  ```text
  Closes #2630 for macOS. #13621 added the `move_tab_to_new_window` action
  and the GTK side; this does the same on macOS with AppKit.
  
  With native tabs a tab is already a window, so the action forwards to
  AppKit's own `moveTabToNewWindow:`. It's a no-op when the window is
  alone in its tab group, same as the Window menu item. The "only
  implemented on Linux" note comes off the doc comment in `Binding.zig`.
  Tested on macOS 26, from a keybind and from the command palette. I have
  no macOS 13-15 machine.
  
  Full disclosure, written with Claude Code, I directed it, read every
  line, and tested the result.
  ```
- [`09a2724`](https://github.com/ghostty-org/ghostty/commit/09a2724c23fd13f7cd24c093c568a4b6792a66a2) Update VOUCHED list ([#14223](https://github.com/ghostty-org/ghostty/issues/14223)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/14221#discussioncomment-18420862)
  from @jcollie.
  
  Vouch: @helium777
  ```
- [`6a64b1c`](https://github.com/ghostty-org/ghostty/commit/6a64b1c86a969bfd6e3a51f1a5c757f980657a3b) po/zh_CN: add missing translations ([@bo2themax](https://github.com/bo2themax))
- [`5252b19`](https://github.com/ghostty-org/ghostty/commit/5252b193cfd52b4bcd868135e21e4563f2f326ec) po/zh_CN: add missing translations ([#14218](https://github.com/ghostty-org/ghostty/issues/14218)) ([@pluiedev](https://github.com/pluiedev))

