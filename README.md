> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: June 29, 2026 at 00:44 UTC.

## June 28, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/28307553086), [2](https://github.com/ghostty-org/ghostty/actions/runs/28307122528)  
Summary: 2 runs • 4 commits • 3 authors

### Changes

- [`07a56d0`](https://github.com/ghostty-org/ghostty/commit/07a56d08bd8c8fd326f7f499cfe3f07098c8e46e) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`07d3166`](https://github.com/ghostty-org/ghostty/commit/07d31666e73bce337b9cece60a884c67fe8906f4) Update iTerm2 colorschemes ([#13107](https://github.com/ghostty-org/ghostty/issues/13107)) ([@jcollie](https://github.com/jcollie))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260622-163450-75bc706
  ```
- [`e1e2e5f`](https://github.com/ghostty-org/ghostty/commit/e1e2e5f34ee6cd075383c6b0375e4c167abaa8d1) build(deps): bump mitchellh/vouch/action/check-issue ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [mitchellh/vouch/action/check-issue](https://github.com/mitchellh/vouch) from 52aec3d64655edf2fdb58f298e02da754a056daf to baeb3bf7c7e6c12d6e33bab3870b7e936580a934.
  - [Release notes](https://github.com/mitchellh/vouch/releases)
  - [Commits](https://github.com/mitchellh/vouch/compare/52aec3d64655edf2fdb58f298e02da754a056daf...baeb3bf7c7e6c12d6e33bab3870b7e936580a934)
  
  ---
  updated-dependencies:
  - dependency-name: mitchellh/vouch/action/check-issue
    dependency-version: baeb3bf7c7e6c12d6e33bab3870b7e936580a934
    dependency-type: direct:production
  ...
  ```
- [`18a44bf`](https://github.com/ghostty-org/ghostty/commit/18a44bfdd95d3bbe778c05770524506d98b0e84c) build(deps): bump mitchellh/vouch/action/check-issue from 52aec3d64655edf2fdb58f298e02da754a056daf to baeb3bf7c7e6c12d6e33bab3870b7e936580a934 ([#13099](https://github.com/ghostty-org/ghostty/issues/13099)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [mitchellh/vouch/action/check-issue](https://github.com/mitchellh/vouch)
  from 52aec3d64655edf2fdb58f298e02da754a056daf to
  baeb3bf7c7e6c12d6e33bab3870b7e936580a934.
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/baeb3bf7c7e6c12d6e33bab3870b7e936580a934"><code>baeb3bf</code></a>
  Merge pull request <a
  href="https://redirect.github.com/mitchellh/vouch/issues/90">#90</a>
  from trag1c/lock-issues</li>
  <li>See full diff in <a
  href="https://github.com/mitchellh/vouch/compare/52aec3d64655edf2fdb58f298e02da754a056daf...baeb3bf7c7e6c12d6e33bab3870b7e936580a934">compare
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

## June 27, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/28282306177)  
Summary: 1 runs • 3 commits • 2 authors

### Changes

- [`5ea4591`](https://github.com/ghostty-org/ghostty/commit/5ea45919d7090a1fd3f77fe75eaddd97fd54f3bd) config: add gtk-horizontal-tab-scroll option ([@00JCIV00](https://github.com/00JCIV00))
  ```text
  Add a boolean config option to enable/disable two-finger horizontal
  touchpad scrolling for switching tabs. Defaults to true to preserve
  existing behavior.
  
  When tab scrolling is disabled or the scroll source is not a touchpad,
  forward horizontal scroll events to the terminal so applications like
  neovim can handle them.
  ```
- [`b5f5ca0`](https://github.com/ghostty-org/ghostty/commit/b5f5ca07892f4df799bcc4645f80e441640b5946) Add "available since" ([@jcollie](https://github.com/jcollie))
- [`e5b65a2`](https://github.com/ghostty-org/ghostty/commit/e5b65a2ce31665ea517145fa7788c48fd1583c50) config: add gtk-horizontal-tab-scroll option ([#12659](https://github.com/ghostty-org/ghostty/issues/12659)) ([@jcollie](https://github.com/jcollie))
  ```text
  I've implemented a GTK toggle (gtk-horizontal-tab-scroll) for the
  2-finger tab swiping introduced in #10575.
  
  This resolves the issue presented in #11566. Simply put, this allows
  users to decide whether or not they want to use horizontal tab scrolling
  or just have the events passed through. Passing through the horizontal
  scroll events allows programs like Neovim to use them for horizontal
  scrolling.
  
  This PR was largely generated by Claude Code and fully reviewed/refined
  by me.
  ```

## June 26, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/28241095905)  
Summary: 1 runs • 2 commits • 2 authors

### Changes

- [`0a117e0`](https://github.com/ghostty-org/ghostty/commit/0a117e0797741d0efc70d2f99fcb27b9dd1832b6) gtk: fix missing dbus connection causing crash ([@dkinzler](https://github.com/dkinzler))
  ```text
  Changes GlobalShortcuts.refresh to do nothing when there is no dbus connection and GlobalShortcuts.close to always clean up arena memory.
  ```
- [`9f62873`](https://github.com/ghostty-org/ghostty/commit/9f62873bf195e4d8a762d768a1405a5f2f7b1697) gtk: fix crash caused by missing dbus connection ([#13101](https://github.com/ghostty-org/ghostty/issues/13101)) ([@pluiedev](https://github.com/pluiedev))
  ```text
  Fixes #13075 where GTK app will crash if a D-Bus connection can't be
  opened. If you have global keybinds set in your config, Ghostty will
  crash immediately in both debug and release builds. With no global
  keybinds it still crashes when you reload the config, but only in builds
  with safety checks enabled, due to a failed assertion.
  
  This problem is rooted in `GlobalShortcuts`, which implements the XDG
  global shortcuts protocol. The `refresh` function is triggered every
  time the config changes and once on startup. If there are global
  keybinds in the config but no D-Bus connection, `refresh` will still try
  to setup the global keybinds by calling the `request` method, which will
  use `priv.dbus_connection.?` while the field is null. Depending on the
  build mode this either fails the Zig runtime safety check immediately or
  eventually causes a segmentation fault somewhere in `gio/glib` when the
  null pointer is used.
  Additionally, even if there are no global keybinds set, Ghostty will
  still crash when the config is reloaded, because the `close` function
  exits early if `dbus_connection` is null and doesn't clean up the arena
  that was created in the first call to `refresh` on startup. The next
  call to `refresh` will then fail the `priv.arena == null` assertion.
  This only happens if built with safety checks enabled.
  
  As a fix `close` will now always clean up the arena and `refresh` will
  exit early if there is no D-Bus connection.
  
  To easily reproduce the crash, change
  `Application.startupGlobalShortcuts` (in
  `src/apprt/gtk/class/application.zig`) to set the D-Bus connection to
  null with `priv.global_shortcuts.setDbusConnection(null)`. Then run with
  a global keybind e.g. `ghostty
  --keybind="global:ctrl+o=toggle_quick_terminal"`.
  
  #### AI Disclosure
  No AI was used.
  ```

## June 25, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/28205137125), [2](https://github.com/ghostty-org/ghostty/actions/runs/28192883748), [3](https://github.com/ghostty-org/ghostty/actions/runs/28190387006)  
Summary: 3 runs • 4 commits • 2 authors

### Changes

- [`f9194f9`](https://github.com/ghostty-org/ghostty/commit/f9194f93deeec82670771fc3909132b37356b155) Update VOUCHED list ([#13098](https://github.com/ghostty-org/ghostty/issues/13098)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13096#discussioncomment-17439268)
  from @jcollie.
  
  Vouch: @WilliamHCarter
  ```
- [`f52f8aa`](https://github.com/ghostty-org/ghostty/commit/f52f8aab95b268d6b0f3a483d6620246dd143779) macos: avoid notification publisher retain cycle ([@mitchellh](https://github.com/mitchellh))
  ````text
  Turns out combine's `publisher(for:,object:)` retains the object!
  We verified this with a test script shown below. Fix this with a
  manual filter. Found by @mustafa0x.
  
  ```
  import Combine
  import Foundation
  
  final class Token {
      deinit { print("Token deinitialized") }
  }
  
  weak var weakToken: Token?
  var publisher: NotificationCenter.Publisher?
  
  // Create scope that will free token.
  do {
      let token = Token()
      weakToken = token
      publisher = NotificationCenter.default.publisher(
          for: Notification.Name("TestNotification"),
          object: token
      )
  }
  
  print("Retained:", weakToken != nil)
  publisher = nil
  print("Released:", weakToken == nil)
  ```
  ````
- [`2415028`](https://github.com/ghostty-org/ghostty/commit/2415028fb256579c6c0f9e4ab7a15c0d59484fd0) macos: avoid notification publisher retain cycle ([#13094](https://github.com/ghostty-org/ghostty/issues/13094)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  Turns out combine's `publisher(for:,object:)` retains the object! We
  verified this with a test script shown below. Fix this with a manual
  filter. Found by @mustafa0x.
  
  ```
  import Combine
  import Foundation
  
  final class Token {
      deinit { print("Token deinitialized") }
  }
  
  weak var weakToken: Token?
  var publisher: NotificationCenter.Publisher?
  
  // Create scope that will free token.
  do {
      let token = Token()
      weakToken = token
      publisher = NotificationCenter.default.publisher(
          for: Notification.Name("TestNotification"),
          object: token
      )
  }
  
  print("Retained:", weakToken != nil)
  publisher = nil
  print("Released:", weakToken == nil)
  ```
  ````
- [`5e872a6`](https://github.com/ghostty-org/ghostty/commit/5e872a6a681488b2ed1e87a23e12065c89948206) Update VOUCHED list ([#13093](https://github.com/ghostty-org/ghostty/issues/13093)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/13092#issuecomment-4802701425)
  from @bo2themax.
  
  Vouch: @mustafa0x
  ```

## June 23, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/28008191370)  
Summary: 1 runs • 1 commits • 1 authors

### Changes

- [`4789bbd`](https://github.com/ghostty-org/ghostty/commit/4789bbdb9ef9e2a878b92d85ee89faeba1f48a87) Update VOUCHED list ([#13072](https://github.com/ghostty-org/ghostty/issues/13072)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13071#discussioncomment-17403343)
  from @pluiedev.
  
  Vouch: @nilsherzig
  ```

