> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: June 26, 2026 at 10:05 UTC.

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

## June 22, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/27981920319), [2](https://github.com/ghostty-org/ghostty/actions/runs/27962325305)  
Summary: 2 runs • 11 commits • 5 authors

### Changes

- [`b3cc500`](https://github.com/ghostty-org/ghostty/commit/b3cc5000e07b00ed3c3d345ede3c14b83b1ec9c7) build(deps): bump actions/checkout from 6.0.3 to 7.0.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [actions/checkout](https://github.com/actions/checkout) from 6.0.3 to 7.0.0.
  - [Release notes](https://github.com/actions/checkout/releases)
  - [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/actions/checkout/compare/df4cb1c069e1874edd31b4311f1884172cec0e10...9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0)
  
  ---
  updated-dependencies:
  - dependency-name: actions/checkout
    dependency-version: 7.0.0
    dependency-type: direct:production
    update-type: version-update:semver-major
  ...
  ```
- [`5fa37f2`](https://github.com/ghostty-org/ghostty/commit/5fa37f2b7e2c38a2837632d4dbc1b0b72401bd05) Use correct type for number of remaining rows so that PageList.scroll works with long scrollback history. ([@dkinzler](https://github.com/dkinzler))
- [`dc8d385`](https://github.com/ghostty-org/ghostty/commit/dc8d38503d4127f0897fe9a516dfb4349f6f501f) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`1fcc622`](https://github.com/ghostty-org/ghostty/commit/1fcc622d639ee3aba8bd914ec532631eba9d73dd) build(deps): bump softprops/action-gh-release from 3.0.0 to 3.0.1 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [softprops/action-gh-release](https://github.com/softprops/action-gh-release) from 3.0.0 to 3.0.1.
  - [Release notes](https://github.com/softprops/action-gh-release/releases)
  - [Changelog](https://github.com/softprops/action-gh-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/softprops/action-gh-release/compare/b4309332981a82ec1c5618f44dd2e27cc8bfbfda...718ea10b132b3b2eba29c1007bb80653f286566b)
  
  ---
  updated-dependencies:
  - dependency-name: softprops/action-gh-release
    dependency-version: 3.0.1
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`632aa67`](https://github.com/ghostty-org/ghostty/commit/632aa6756073e4584b05d0c3b7493b118f42f2af) macOS: fix tabs frame on macOS 27 beta 2 ([@bo2themax](https://github.com/bo2themax))
- [`6f27429`](https://github.com/ghostty-org/ghostty/commit/6f274295db837779e6ac4c6747a692f08a7ea8dd) macOS: fix tabs frame on macOS 27 beta 2 ([#13069](https://github.com/ghostty-org/ghostty/issues/13069)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Also created a follow-up task to check whether this will survive the
  final release: #13070
  ```
- [`06aee71`](https://github.com/ghostty-org/ghostty/commit/06aee71b720e04fc73669a338194414413f2837a) build(deps): bump softprops/action-gh-release from 3.0.0 to 3.0.1 ([#13059](https://github.com/ghostty-org/ghostty/issues/13059)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [softprops/action-gh-release](https://github.com/softprops/action-gh-release)
  from 3.0.0 to 3.0.1.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/softprops/action-gh-release/releases">softprops/action-gh-release's
  releases</a>.</em></p>
  <blockquote>
  <h2>v3.0.1</h2>
  <h2>3.0.1</h2>
  <ul>
  <li>maintenance release with updated dependencies</li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/softprops/action-gh-release/blob/master/CHANGELOG.md">softprops/action-gh-release's
  changelog</a>.</em></p>
  <blockquote>
  <h2>3.0.1</h2>
  <ul>
  <li>maintenance release with updated dependencies</li>
  </ul>
  <h2>3.0.0</h2>
  <p><code>3.0.0</code> is a major release that moves the action runtime
  from Node 20 to Node 24.
  Use <code>v3</code> on GitHub-hosted runners and self-hosted fleets that
  already support the
  Node 24 Actions runtime. If you still need the last Node 20-compatible
  line, stay on
  <code>v2.6.2</code>.</p>
  <h2>What's Changed</h2>
  <h3>Other Changes 🔄</h3>
  <ul>
  <li>Move the action runtime and bundle target to Node 24</li>
  <li>Update <code>@types/node</code> to the Node 24 line and allow future
  Dependabot updates</li>
  <li>Keep the floating major tag on <code>v3</code>; <code>v2</code>
  remains pinned to the latest <code>2.x</code> release</li>
  </ul>
  <h2>2.6.2</h2>
  <h2>What's Changed</h2>
  <h3>Other Changes 🔄</h3>
  <ul>
  <li>chore(deps): bump picomatch from 4.0.3 to 4.0.4 by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/775">softprops/action-gh-release#775</a></li>
  <li>chore(deps): bump brace-expansion from 5.0.4 to 5.0.5 by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/777">softprops/action-gh-release#777</a></li>
  <li>chore(deps): bump vite from 8.0.0 to 8.0.5 by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/781">softprops/action-gh-release#781</a></li>
  </ul>
  <h2>2.6.1</h2>
  <p><code>2.6.1</code> is a patch release focused on restoring linked
  discussion thread creation when
  <code>discussion_category_name</code> is set. It fixes
  <code>[#764](https://github.com/softprops/action-gh-release/issues/764)</code>,
  where the draft-first publish flow
  stopped carrying the discussion category through the final publish
  step.</p>
  <p>If you still hit an issue after upgrading, please open a report with
  the bug template and include a minimal repro or sanitized workflow
  snippet where possible.</p>
  <h2>What's Changed</h2>
  <h3>Bug fixes 🐛</h3>
  <ul>
  <li>fix: preserve discussion category on publish by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/765">softprops/action-gh-release#765</a></li>
  </ul>
  <h2>2.6.0</h2>
  <p><code>2.6.0</code> is a minor release centered on
  <code>previous_tag</code> support for
  <code>generate_release_notes</code>,
  which lets workflows pin GitHub's comparison base explicitly instead of
  relying on the default range.
  It also includes the recent concurrent asset upload recovery fix, a
  <code>working_directory</code> docs sync,
  a checked-bundle freshness guard for maintainers, and clearer
  immutable-prerelease guidance where
  GitHub platform behavior imposes constraints on how prerelease asset
  uploads can be published.</p>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/718ea10b132b3b2eba29c1007bb80653f286566b"><code>718ea10</code></a>
  release 3.0.1</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/f1a938b9d84ca9b770d0d8dfeb3e7285fe261e63"><code>f1a938b</code></a>
  chore(deps): bump esbuild from 0.28.0 to 0.28.1 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/802">#802</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/0066ead0de7252b4876b36b5357fc3974619d36a"><code>0066ead</code></a>
  chore(deps): bump vite from 8.0.14 to 8.0.16 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/806">#806</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/dc643cac6252aaa00c9b0b6c940d489cd7bf6b23"><code>dc643ca</code></a>
  chore(deps): bump the npm group with 3 updates (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/805">#805</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/85ee99b6b20742a3823a8a289ee5e6ceab44e8aa"><code>85ee99b</code></a>
  chore(deps): bump actions/checkout in the github-actions group (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/804">#804</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/9ed3cf9a6863b31f005d951c8d19de20628cf4eb"><code>9ed3cf9</code></a>
  chore(deps): bump the npm group with 2 updates (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/800">#800</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/3efcac8951299998593f871640ea8059d6818655"><code>3efcac8</code></a>
  chore(deps): bump the npm group with 3 updates (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/798">#798</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/05d6b9164aa74958de40b0179d6a773112fcdc7f"><code>05d6b91</code></a>
  chore(deps): bump brace-expansion from 5.0.5 to 5.0.6 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/797">#797</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/403a5240f3837fa857f642062e05aad6bb3391ca"><code>403a524</code></a>
  chore(deps): bump <code>@​types/node</code> from 24.12.2 to 24.12.3 in
  the npm group (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/796">#796</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/437e073e786973c6b6af97d9e445c41ae43b1d29"><code>437e073</code></a>
  chore(deps): bump the npm group with 4 updates (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/792">#792</a>)</li>
  <li>Additional commits viewable in <a
  href="https://github.com/softprops/action-gh-release/compare/b4309332981a82ec1c5618f44dd2e27cc8bfbfda...718ea10b132b3b2eba29c1007bb80653f286566b">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=softprops/action-gh-release&package-manager=github_actions&previous-version=3.0.0&new-version=3.0.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`af0c835`](https://github.com/ghostty-org/ghostty/commit/af0c8352439d08c0b1aaeee0af230a4b8a33893b) Update iTerm2 colorschemes ([#13055](https://github.com/ghostty-org/ghostty/issues/13055)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260615-163819-6e33c6b
  ```
- [`b831ef6`](https://github.com/ghostty-org/ghostty/commit/b831ef6bb01a822dd2513416fef7f94587269c13) build(deps): bump actions/checkout from 6.0.3 to 7.0.0 ([#13044](https://github.com/ghostty-org/ghostty/issues/13044)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps [actions/checkout](https://github.com/actions/checkout) from 6.0.3
  to 7.0.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/actions/checkout/releases">actions/checkout's
  releases</a>.</em></p>
  <blockquote>
  <h2>v7.0.0</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>block checking out fork pr for pull_request_target and workflow_run
  by <a href="https://github.com/aiqiaoy"><code>@​aiqiaoy</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2454">actions/checkout#2454</a></li>
  <li>Bump actions/publish-immutable-action from 0.0.3 to 0.0.4 in the
  minor-actions-dependencies group across 1 directory by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/actions/checkout/pull/2458">actions/checkout#2458</a></li>
  <li>Bump flatted from 3.3.1 to 3.4.2 by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/actions/checkout/pull/2460">actions/checkout#2460</a></li>
  <li>Bump js-yaml from 4.1.0 to 4.2.0 by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/actions/checkout/pull/2461">actions/checkout#2461</a></li>
  <li>Bump <code>@​actions/core</code> and
  <code>@​actions/tool-cache</code> and Remove uuid by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/actions/checkout/pull/2459">actions/checkout#2459</a></li>
  <li>upgrade module to esm and update dependencies by <a
  href="https://github.com/aiqiaoy"><code>@​aiqiaoy</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2463">actions/checkout#2463</a></li>
  <li>Bump the minor-npm-dependencies group across 1 directory with 3
  updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/actions/checkout/pull/2462">actions/checkout#2462</a></li>
  <li>getting ready for checkout v7 release by <a
  href="https://github.com/aiqiaoy"><code>@​aiqiaoy</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2464">actions/checkout#2464</a></li>
  <li>update error wording by <a
  href="https://github.com/aiqiaoy"><code>@​aiqiaoy</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2467">actions/checkout#2467</a></li>
  </ul>
  <h2>New Contributors</h2>
  <ul>
  <li><a href="https://github.com/aiqiaoy"><code>@​aiqiaoy</code></a> made
  their first contribution in <a
  href="https://redirect.github.com/actions/checkout/pull/2454">actions/checkout#2454</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/actions/checkout/compare/v6.0.3...v7.0.0">https://github.com/actions/checkout/compare/v6.0.3...v7.0.0</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/actions/checkout/blob/main/CHANGELOG.md">actions/checkout's
  changelog</a>.</em></p>
  <blockquote>
  <h1>Changelog</h1>
  <h2>v7.0.0</h2>
  <ul>
  <li>Block checking out fork PR for pull_request_target and workflow_run
  by <a href="https://github.com/aiqiaoy"><code>@​aiqiaoy</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2454">actions/checkout#2454</a></li>
  <li>Bump actions/publish-immutable-action from 0.0.3 to 0.0.4 in the
  minor-actions-dependencies group across 1 directory by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/actions/checkout/pull/2458">actions/checkout#2458</a></li>
  <li>Bump flatted from 3.3.1 to 3.4.2 by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/actions/checkout/pull/2460">actions/checkout#2460</a></li>
  <li>Bump js-yaml from 4.1.0 to 4.2.0 by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/actions/checkout/pull/2461">actions/checkout#2461</a></li>
  <li>Bump <code>@​actions/core</code> and
  <code>@​actions/tool-cache</code> and Remove uuid by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/actions/checkout/pull/2459">actions/checkout#2459</a></li>
  <li>upgrade module to esm and update dependencies by <a
  href="https://github.com/aiqiaoy"><code>@​aiqiaoy</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2463">actions/checkout#2463</a></li>
  <li>Bump the minor-npm-dependencies group across 1 directory with 3
  updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/actions/checkout/pull/2462">actions/checkout#2462</a></li>
  </ul>
  <h2>v6.0.3</h2>
  <ul>
  <li>Fix checkout init for SHA-256 repositories by <a
  href="https://github.com/yaananth"><code>@​yaananth</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2439">actions/checkout#2439</a></li>
  <li>fix: expand merge commit SHA regex and add SHA-256 test cases by <a
  href="https://github.com/yaananth"><code>@​yaananth</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2414">actions/checkout#2414</a></li>
  </ul>
  <h2>v6.0.2</h2>
  <ul>
  <li>Fix tag handling: preserve annotations and explicit fetch-tags by <a
  href="https://github.com/ericsciple"><code>@​ericsciple</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2356">actions/checkout#2356</a></li>
  </ul>
  <h2>v6.0.1</h2>
  <ul>
  <li>Add worktree support for persist-credentials includeIf by <a
  href="https://github.com/ericsciple"><code>@​ericsciple</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2327">actions/checkout#2327</a></li>
  </ul>
  <h2>v6.0.0</h2>
  <ul>
  <li>Persist creds to a separate file by <a
  href="https://github.com/ericsciple"><code>@​ericsciple</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2286">actions/checkout#2286</a></li>
  <li>Update README to include Node.js 24 support details and requirements
  by <a href="https://github.com/salmanmkc"><code>@​salmanmkc</code></a>
  in <a
  href="https://redirect.github.com/actions/checkout/pull/2248">actions/checkout#2248</a></li>
  </ul>
  <h2>v5.0.1</h2>
  <ul>
  <li>Port v6 cleanup to v5 by <a
  href="https://github.com/ericsciple"><code>@​ericsciple</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2301">actions/checkout#2301</a></li>
  </ul>
  <h2>v5.0.0</h2>
  <ul>
  <li>Update actions checkout to use node 24 by <a
  href="https://github.com/salmanmkc"><code>@​salmanmkc</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2226">actions/checkout#2226</a></li>
  </ul>
  <h2>v4.3.1</h2>
  <ul>
  <li>Port v6 cleanup to v4 by <a
  href="https://github.com/ericsciple"><code>@​ericsciple</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2305">actions/checkout#2305</a></li>
  </ul>
  <h2>v4.3.0</h2>
  <ul>
  <li>docs: update README.md by <a
  href="https://github.com/motss"><code>@​motss</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/1971">actions/checkout#1971</a></li>
  <li>Add internal repos for checking out multiple repositories by <a
  href="https://github.com/mouismail"><code>@​mouismail</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/1977">actions/checkout#1977</a></li>
  <li>Documentation update - add recommended permissions to Readme by <a
  href="https://github.com/benwells"><code>@​benwells</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2043">actions/checkout#2043</a></li>
  <li>Adjust positioning of user email note and permissions heading by <a
  href="https://github.com/joshmgross"><code>@​joshmgross</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2044">actions/checkout#2044</a></li>
  <li>Update README.md by <a
  href="https://github.com/nebuk89"><code>@​nebuk89</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2194">actions/checkout#2194</a></li>
  <li>Update CODEOWNERS for actions by <a
  href="https://github.com/TingluoHuang"><code>@​TingluoHuang</code></a>
  in <a
  href="https://redirect.github.com/actions/checkout/pull/2224">actions/checkout#2224</a></li>
  <li>Update package dependencies by <a
  href="https://github.com/salmanmkc"><code>@​salmanmkc</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2236">actions/checkout#2236</a></li>
  </ul>
  <h2>v4.2.2</h2>
  <ul>
  <li><code>url-helper.ts</code> now leverages well-known environment
  variables by <a href="https://github.com/jww3"><code>@​jww3</code></a>
  in <a
  href="https://redirect.github.com/actions/checkout/pull/1941">actions/checkout#1941</a></li>
  <li>Expand unit test coverage for <code>isGhes</code> by <a
  href="https://github.com/jww3"><code>@​jww3</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/1946">actions/checkout#1946</a></li>
  </ul>
  <h2>v4.2.1</h2>
  <ul>
  <li>Check out other refs/* by commit if provided, fall back to ref by <a
  href="https://github.com/orhantoy"><code>@​orhantoy</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/1924">actions/checkout#1924</a></li>
  </ul>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/actions/checkout/commit/9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0"><code>9c091bb</code></a>
  update error wording (<a
  href="https://redirect.github.com/actions/checkout/issues/2467">#2467</a>)</li>
  <li><a
  href="https://github.com/actions/checkout/commit/1044a6dea927916f2c38ba5aeffbc0a847b1221a"><code>1044a6d</code></a>
  getting ready for checkout v7 release (<a
  href="https://redirect.github.com/actions/checkout/issues/2464">#2464</a>)</li>
  <li><a
  href="https://github.com/actions/checkout/commit/f0282184c7ce73ab54c7e4ab5a617122602e575f"><code>f028218</code></a>
  Bump the minor-npm-dependencies group across 1 directory with 3 updates
  (<a
  href="https://redirect.github.com/actions/checkout/issues/2462">#2462</a>)</li>
  <li><a
  href="https://github.com/actions/checkout/commit/d914b262ffc244530a203ab40decab34c3abf34d"><code>d914b26</code></a>
  upgrade module to esm and update dependencies (<a
  href="https://redirect.github.com/actions/checkout/issues/2463">#2463</a>)</li>
  <li><a
  href="https://github.com/actions/checkout/commit/537c7ef99cef6e5ddb5e7ff5d16d14510503801d"><code>537c7ef</code></a>
  Bump <code>@​actions/core</code> and <code>@​actions/tool-cache</code>
  and Remove uuid (<a
  href="https://redirect.github.com/actions/checkout/issues/2459">#2459</a>)</li>
  <li><a
  href="https://github.com/actions/checkout/commit/130a169078a413d3a5246a393625e8e742f387f6"><code>130a169</code></a>
  Bump js-yaml from 4.1.0 to 4.2.0 (<a
  href="https://redirect.github.com/actions/checkout/issues/2461">#2461</a>)</li>
  <li><a
  href="https://github.com/actions/checkout/commit/7d09575332117a40b46e5e020664df234cd416f3"><code>7d09575</code></a>
  Bump flatted from 3.3.1 to 3.4.2 (<a
  href="https://redirect.github.com/actions/checkout/issues/2460">#2460</a>)</li>
  <li><a
  href="https://github.com/actions/checkout/commit/0f9f3aa320cb53abeb534aeb54048075d9697a0e"><code>0f9f3aa</code></a>
  Bump actions/publish-immutable-action (<a
  href="https://redirect.github.com/actions/checkout/issues/2458">#2458</a>)</li>
  <li><a
  href="https://github.com/actions/checkout/commit/f9e715a95fcd1f9253f77dd28f11e88d2d6460c7"><code>f9e715a</code></a>
  block checking out fork pr for pull_request_target and workflow_run (<a
  href="https://redirect.github.com/actions/checkout/issues/2454">#2454</a>)</li>
  <li>See full diff in <a
  href="https://github.com/actions/checkout/compare/df4cb1c069e1874edd31b4311f1884172cec0e10...9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=actions/checkout&package-manager=github_actions&previous-version=6.0.3&new-version=7.0.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`65744ff`](https://github.com/ghostty-org/ghostty/commit/65744ffe358d883ae74aa67389dcbfa35f91a551) core: fix PageList.scroll using wrong type for row offset ([#13048](https://github.com/ghostty-org/ghostty/issues/13048)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Changes `PageList.scroll` to use `usize` as the type for the number of
  remaining rows when trying to find a specific row in the list of pages.
  Previously `CellCountInt=u16` was used, but the row offset can be larger
  than `maxInt(u16)=65535`, in which case the scroll operation would fail.
  
  Fixes #13000 where scrolling does not work correctly in the GTK app with
  a large scrollback history. E.g. nothing happens when you click in the
  middle of the scrollbar. Note that this problem only manifests at
  millions of lines of history instead of already when the row offset
  overflows `u16`. The reason for that is that GTK often emits multiple
  scroll adjustments, the first of which is usually close enough to the
  current position to not overflow `u16`. The other scroll adjustments are
  then handled by the fast path in `PageList.scroll` that works correctly.
  
  #### AI Disclosure
  No AI was used.
  ```
- [`45db2c2`](https://github.com/ghostty-org/ghostty/commit/45db2c2551ecc016f9746e8e2855f4f8a3871e7b) Update VOUCHED list ([#13065](https://github.com/ghostty-org/ghostty/issues/13065)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13063#discussioncomment-17394374)
  from @pluiedev.
  
  Denounce: @schickling-assistant
  ```

## June 20, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/27871780495)  
Summary: 1 runs • 2 commits • 2 authors

### Changes

- [`e2e6153`](https://github.com/ghostty-org/ghostty/commit/e2e61531123187d922408c3795be48d8df25c321) i18n(kk): translate missing "Close Split" string ([@AnmiTaliDev](https://github.com/AnmiTaliDev))
- [`4749c4e`](https://github.com/ghostty-org/ghostty/commit/4749c4e93731067049bfbf2e4572061cef2bdd17) i18n(kk): translate missing "Close Split" string ([#13052](https://github.com/ghostty-org/ghostty/issues/13052)) ([@00-kat](https://github.com/00-kat))

