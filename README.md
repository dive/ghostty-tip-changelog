> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: May 18, 2026 at 07:23 UTC.

## May 18, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26010120405), [2](https://github.com/ghostty-org/ghostty/actions/runs/26009059850)  
Summary: 2 runs • 10 commits • 3 authors

### Changes

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

## May 17, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/25977502466)  
Summary: 1 runs • 2 commits • 2 authors

### Changes

- [`ee316e4`](https://github.com/ghostty-org/ghostty/commit/ee316e43c140568729487a95fc7dfd7ee87a4176) build(deps): bump actions/create-github-app-token from 3.1.1 to 3.2.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [actions/create-github-app-token](https://github.com/actions/create-github-app-token) from 3.1.1 to 3.2.0.
  - [Release notes](https://github.com/actions/create-github-app-token/releases)
  - [Changelog](https://github.com/actions/create-github-app-token/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/actions/create-github-app-token/compare/1b10c78c7865c340bc4f6099eb2f838309f1e8c3...bcd2ba49218906704ab6c1aa796996da409d3eb1)
  
  ---
  updated-dependencies:
  - dependency-name: actions/create-github-app-token
    dependency-version: 3.2.0
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`e90b7c9`](https://github.com/ghostty-org/ghostty/commit/e90b7c9fadadb5b7f936506dfd4f995729093108) build(deps): bump actions/create-github-app-token from 3.1.1 to 3.2.0 ([#12670](https://github.com/ghostty-org/ghostty/issues/12670)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [actions/create-github-app-token](https://github.com/actions/create-github-app-token)
  from 3.1.1 to 3.2.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/actions/create-github-app-token/releases">actions/create-github-app-token's
  releases</a>.</em></p>
  <blockquote>
  <h2>v3.2.0</h2>
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
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/actions/create-github-app-token/blob/main/CHANGELOG.md">actions/create-github-app-token's
  changelog</a>.</em></p>
  <blockquote>
  <h1>Changelog</h1>
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
  href="https://github.com/actions/create-github-app-token/commit/bcd2ba49218906704ab6c1aa796996da409d3eb1"><code>bcd2ba4</code></a>
  chore(main): release 3.2.0 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/370">#370</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/f24bbd89643991c0de27ae823c01791b2c6bafdd"><code>f24bbd8</code></a>
  fix: validate private-key input (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/376">#376</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/363531b6d972a60a00b3f1e6bb139e5e6c764cd9"><code>363531b</code></a>
  docs: capitalize Git as a proper noun in README (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/374">#374</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/fd2801133e469d2950f2c5af5e591d6b2ad833c8"><code>fd28011</code></a>
  docs: update procedure to configure Git (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/287">#287</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/85eb8dd41472213aed25d1a126460e0069138ab6"><code>85eb8dd</code></a>
  feat: support full repository names in <code>repositories</code> input
  (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/372">#372</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/c9aabb83728c3bd519212fa657ebc07e1f2a5dec"><code>c9aabb8</code></a>
  build(deps-dev): bump yaml from 2.8.3 to 2.8.4 in the
  development-dependencie...</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/e02e816e5591415258a53bf735aff57977dcd5e2"><code>e02e816</code></a>
  build(deps-dev): bump undici from 7.24.6 to 8.2.0 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/366">#366</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/8d835bfd37aa48fcb8e709925115857568d98bc4"><code>8d835bf</code></a>
  build(deps-dev): bump esbuild from 0.27.4 to 0.28.0 in the
  development-depend...</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/952a2a7073df6bfa5f49bc469ec895b6ec1acea4"><code>952a2a7</code></a>
  feat: add support for enterprise-level GitHub Apps (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/263">#263</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/43e5c345bfd4d4f3ecea019ad0042001a09dd857"><code>43e5c34</code></a>
  fix(deps): bump <code>@​actions/core</code> from 3.0.0 to 3.0.1 in the
  production-dependenc...</li>
  <li>Additional commits viewable in <a
  href="https://github.com/actions/create-github-app-token/compare/1b10c78c7865c340bc4f6099eb2f838309f1e8c3...bcd2ba49218906704ab6c1aa796996da409d3eb1">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=actions/create-github-app-token&package-manager=github_actions&previous-version=3.1.1&new-version=3.2.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## May 16, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/25975314998), [2](https://github.com/ghostty-org/ghostty/actions/runs/25962520206), [3](https://github.com/ghostty-org/ghostty/actions/runs/25962442981)  
Summary: 3 runs • 6 commits • 3 authors

### Changes

- [`e5c31e8`](https://github.com/ghostty-org/ghostty/commit/e5c31e8b379f6f850caadc2f11c74ea9e6644f34) macos: opacity-toggle setting persists between tabs in a window and to a newly created window ([@davidsanchez222](https://github.com/davidsanchez222))
- [`0e49204`](https://github.com/ghostty-org/ghostty/commit/0e49204b95fca41b1342ad56c9a0092f0872d737) refactor(macos): centralize background opacity toggling across controllers ([@davidsanchez222](https://github.com/davidsanchez222))
- [`b6c6f76`](https://github.com/ghostty-org/ghostty/commit/b6c6f7630abf6aff8ac98a16b378b0f0e6931142) macos: opacity-toggle setting persists between tabs in a window and to a newly created window ([#11583](https://github.com/ghostty-org/ghostty/issues/11583)) ([@bo2themax](https://github.com/bo2themax))
- [`42ed74b`](https://github.com/ghostty-org/ghostty/commit/42ed74bf8cda529553a655439788e6c36d2a8549) Update VOUCHED list ([#12706](https://github.com/ghostty-org/ghostty/issues/12706)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12686#discussioncomment-16940039)
  from @bo2themax.
  
  Vouch: @nolinmcfarland
  ```
- [`cf24a48`](https://github.com/ghostty-org/ghostty/commit/cf24a4856b24f7b381c13f1491421e84b3bf802a) Update VOUCHED list ([#12707](https://github.com/ghostty-org/ghostty/issues/12707)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12625#discussioncomment-16940042)
  from @bo2themax.
  
  Unvouch: @backnotprop
  ```
- [`0a3598d`](https://github.com/ghostty-org/ghostty/commit/0a3598d7a1e794214b2887f3f2acf79f67222fac) Update VOUCHED list ([#12705](https://github.com/ghostty-org/ghostty/issues/12705)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12625#discussioncomment-16940011)
  from @bo2themax.
  
  Vouch: @backnotprop
  ```

## May 15, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/25899767544), [2](https://github.com/ghostty-org/ghostty/actions/runs/25898620299)  
Summary: 2 runs • 3 commits • 3 authors

### Changes

- [`e9213bb`](https://github.com/ghostty-org/ghostty/commit/e9213bb1e7d1eaf5bce486d6b03bc102d6dee507) Delete test_align ([@vancluever](https://github.com/vancluever))
  ```text
  Checked in to make sure that this wasn't added intentionally :slightly_smiling_face:
  
  Looks like it snuck in in #11868.
  ```
- [`0071971`](https://github.com/ghostty-org/ghostty/commit/0071971b577c6ef6396cfe99684b466757bf0ef9) Delete test_align ([#12688](https://github.com/ghostty-org/ghostty/issues/12688)) ([@jcollie](https://github.com/jcollie))
  ```text
  Checked in to make sure that this wasn't added intentionally
  :slightly_smiling_face:
  
  Looks like it snuck in in #11868.
  ```
- [`84ad649`](https://github.com/ghostty-org/ghostty/commit/84ad649128be60fb7e449d03a8d1369fed51a84b) Update VOUCHED list ([#12689](https://github.com/ghostty-org/ghostty/issues/12689)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12688#issuecomment-4456633108)
  from @rhodes-b.
  
  Vouch: @vancluever
  ```

## May 14, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/25878980199), [2](https://github.com/ghostty-org/ghostty/actions/runs/25871337194)  
Summary: 2 runs • 3 commits • 3 authors

### Changes

- [`13ca032`](https://github.com/ghostty-org/ghostty/commit/13ca032b1de461146f8e9c416901d2414df19189) config: clear `command-palette-entry` like `keybind` ([@bo2themax](https://github.com/bo2themax))
  ```text
  After #1368, `command-palette-entry=` will no longer clear the entries like the documentation says. Since i couldn't find an existing issue or discussion about this, I assume no one is actually using it. So I put 1.4.0 here, lemme know if you want to change it to 1.3.2.
  
  > I basically copied the `keybind` parsing code and doc.
  ```
- [`96848d7`](https://github.com/ghostty-org/ghostty/commit/96848d792e0ea2ed87125ee286f50399cac1aa5b) config: clear `command-palette-entry` like `keybind` ([#12682](https://github.com/ghostty-org/ghostty/issues/12682)) ([@pluiedev](https://github.com/pluiedev))
  ```text
  After #1368, `command-palette-entry=` will no longer clear the entries
  like the documentation says. Since i couldn't find an existing issue or
  discussion about this, I assume no one is actually using it. So I put
  1.4.0 here, lemme know if you want to change it to 1.3.2.
  
  > I basically copied the `keybind` parsing code and doc.
  ```
- [`47382f8`](https://github.com/ghostty-org/ghostty/commit/47382f8dcbf9fe1dc448f0dfcbc6b4230d17cb06) Update VOUCHED list ([#12680](https://github.com/ghostty-org/ghostty/issues/12680)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12678#issuecomment-4452472142)
  from @trag1c.
  
  Denounce: @zaviro
  ```

## May 13, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/25825350217)  
Summary: 1 runs • 3 commits • 3 authors

### Changes

- [`b3c1f75`](https://github.com/ghostty-org/ghostty/commit/b3c1f754adf228631b7665751b322aa5652b6296) build(deps): bump cachix/cachix-action ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [cachix/cachix-action](https://github.com/cachix/cachix-action) from 1eb2ef646ac0255473d23a5907ad7b04ce94065c to 5f2d7c5294214f71b873db4b969586b980625e71.
  - [Release notes](https://github.com/cachix/cachix-action/releases)
  - [Changelog](https://github.com/cachix/cachix-action/blob/master/RELEASE.md)
  - [Commits](https://github.com/cachix/cachix-action/compare/1eb2ef646ac0255473d23a5907ad7b04ce94065c...5f2d7c5294214f71b873db4b969586b980625e71)
  
  ---
  updated-dependencies:
  - dependency-name: cachix/cachix-action
    dependency-version: 5f2d7c5294214f71b873db4b969586b980625e71
    dependency-type: direct:production
  ...
  ```
- [`b0f8276`](https://github.com/ghostty-org/ghostty/commit/b0f8276658fbcc75318d2125d40146074a3fc505) build(deps): bump cachix/cachix-action from 1eb2ef646ac0255473d23a5907ad7b04ce94065c to 5f2d7c5294214f71b873db4b969586b980625e71 ([#12651](https://github.com/ghostty-org/ghostty/issues/12651)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps [cachix/cachix-action](https://github.com/cachix/cachix-action)
  from 1eb2ef646ac0255473d23a5907ad7b04ce94065c to
  5f2d7c5294214f71b873db4b969586b980625e71.
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/cachix/cachix-action/blob/master/RELEASE.md">cachix/cachix-action's
  changelog</a>.</em></p>
  <blockquote>
  <h1>Release</h1>
  <ol>
  <li>
  <p>Create and push a new tag:</p>
  <pre lang="console"><code>git tag v17
  git push origin v17
  </code></pre>
  </li>
  <li>
  <p>Wait for CI to pass.</p>
  </li>
  <li>
  <p><a href="https://github.com/cachix/cachix-action/releases/new">Create
  a release</a> for the new tag.</p>
  </li>
  <li>
  <p>Move the major version tag to the latest release:</p>
  <pre lang="console"><code>git tag -fa v17
  git push origin v17 --force
  </code></pre>
  </li>
  </ol>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/5f2d7c5294214f71b873db4b969586b980625e71"><code>5f2d7c5</code></a>
  fix: await main functions</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/4ee54539d70638c5ce6c547ec6765bea7af27c00"><code>4ee5453</code></a>
  rebuilt dist</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/9f82c7e3322d9b4c3a65cb2cef2eea15c41ba3e6"><code>9f82c7e</code></a>
  fix: ensure that the post-build hook never fails</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/a593539ec5b1ba1eb95f89a396efd45ca2cdaf5d"><code>a593539</code></a>
  ci: add a workflow to auto-bump version in README</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/8d6d4b9006df1043eb58997a65c1eb7ae12056fb"><code>8d6d4b9</code></a>
  docs: add release and contributing docs</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/6505427c13f0fc890ba714848703523a78ac3ce2"><code>6505427</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/cachix-action/issues/213">#213</a>
  from jleroux98/update-readme</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/5941c261999ff0868bced8a2261b624a5f839338"><code>5941c26</code></a>
  use regular tags</li>
  <li><a
  href="https://github.com/cachix/cachix-action/commit/80a630b9fcc17e3d3afad8ff9a4f4c7b155f9957"><code>80a630b</code></a>
  update tags</li>
  <li>See full diff in <a
  href="https://github.com/cachix/cachix-action/compare/1eb2ef646ac0255473d23a5907ad7b04ce94065c...5f2d7c5294214f71b873db4b969586b980625e71">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
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
- [`b23d567`](https://github.com/ghostty-org/ghostty/commit/b23d567cd89874ffe218036536a2aec52851f34f) Update VOUCHED list ([#12675](https://github.com/ghostty-org/ghostty/issues/12675)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12674#issuecomment-4445057781)
  from @trag1c.
  
  Vouch: @B1NAR10
  ```

