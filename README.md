> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: November 18, 2026 at 10:59 UTC.

## November 18, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/44247634968)  
Summary: 1 runs • 2 commits • 2 authors

### Changes

- [`d9d56b6`](https://github.com/ghostty-org/ghostty/commit/d9d56b6c26d778e360257f119885eee24000505d) build(deps): bump hustcer/milestone-action from 3.2 to 3.3 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [hustcer/milestone-action](https://github.com/hustcer/milestone-action) from 3.2 to 3.3.
  - [Release notes](https://github.com/hustcer/milestone-action/releases)
  - [Changelog](https://github.com/hustcer/milestone-action/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/hustcer/milestone-action/compare/2f38355153344ccaaa44b5b5fcff9f604dff1b45...815f8224db33f809c5063c66e2e4f530208f401e)
  
  ---
  updated-dependencies:
  - dependency-name: hustcer/milestone-action
    dependency-version: '3.3'
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`7a8ff4d`](https://github.com/ghostty-org/ghostty/commit/7a8ff4d992edd2aad7537e5bef73ec911aa126bf) build(deps): bump hustcer/milestone-action from 3.2 to 3.3 ([#15271](https://github.com/ghostty-org/ghostty/issues/15271)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [hustcer/milestone-action](https://github.com/hustcer/milestone-action)
  from 3.2 to 3.3.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/hustcer/milestone-action/releases">hustcer/milestone-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v3.3</h2>
  <h2>[3.3] - 2026-11-15</h2>
  <h3>Deps</h3>
  <ul>
  <li>Upgrade nushell from 0.115.1 to 0.117.0</li>
  <li>Upgrade hustcer/setup-nu from v3.27 to v3.30</li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/hustcer/milestone-action/blob/main/CHANGELOG.md">hustcer/milestone-action's
  changelog</a>.</em></p>
  <blockquote>
  <h1>Changelog</h1>
  <p>All notable changes to this project will be documented in this
  file.</p>
  <h2>[3.3] - 2026-11-15</h2>
  <h3>Deps</h3>
  <ul>
  <li>Upgrade nushell from 0.115.1 to 0.117.0</li>
  <li>Upgrade hustcer/setup-nu from v3.27 to v3.30</li>
  </ul>
  <h2>[3.2] - 2026-08-25</h2>
  <h3>Bug Fixes</h3>
  <ul>
  <li>Harden action inputs and make GraphQL file lookup path-independent
  (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/168">#168</a>)</li>
  <li>Look up milestones by title across all states with pagination (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/170">#170</a>)</li>
  <li>Guard GITHUB_OUTPUT, surface GraphQL errors and tighten is-int (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/172">#172</a>)</li>
  <li>Require title for create action and sync stale docs (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/174">#174</a>)</li>
  <li>Send milestone fields as raw strings and harden action inputs (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/176">#176</a>)</li>
  </ul>
  <h3>Deps</h3>
  <ul>
  <li>Upgrade hustcer/setup-nu to v3.25 &amp; Nu to 0.113.1</li>
  <li>Upgrade hustcer/setup-nu to v3.27 and Nu to 0.115</li>
  <li>Upgrade Nu to 0.115.1</li>
  </ul>
  <h2>[3.1] - 2026-01-23</h2>
  <h3>Documentation</h3>
  <ul>
  <li>Update milestone-action version in README (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/162">#162</a>)</li>
  </ul>
  <h3>Features</h3>
  <ul>
  <li>Break before sleep when milestone found</li>
  </ul>
  <h3>Miscellaneous Tasks</h3>
  <ul>
  <li>Update README.md (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/166">#166</a>)</li>
  </ul>
  <h3>Deps</h3>
  <ul>
  <li>Update Nu to 0.109.1</li>
  <li>Update Nushell to 0.110.0 (<a
  href="https://redirect.github.com/hustcer/milestone-action/issues/167">#167</a>)</li>
  <li>Upgrade hustcer/setup-nu to v3.22</li>
  </ul>
  <h1>Changelog</h1>
  <p>All notable changes to this project will be documented in this
  file.</p>
  <h2>[3.0] - 2025-10-26</h2>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/815f8224db33f809c5063c66e2e4f530208f401e"><code>815f822</code></a>
  chore: update CHANGELOG.md</li>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/13801ea24afcdea4b80608b936582475ba55bdd3"><code>13801ea</code></a>
  Bump to v3.3</li>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/916b5dc899cb31ea0c72f86d09288bf76c9a9a5e"><code>916b5dc</code></a>
  deps: Upgrade hustcer/setup-nu &amp; Nu to latest version</li>
  <li><a
  href="https://github.com/hustcer/milestone-action/commit/93633102e028c297578c8e156312d16ba7dc2998"><code>9363310</code></a>
  deps: Upgrade hustcer/setup-nu &amp; Nu to latest version</li>
  <li>See full diff in <a
  href="https://github.com/hustcer/milestone-action/compare/2f38355153344ccaaa44b5b5fcff9f604dff1b45...815f8224db33f809c5063c66e2e4f530208f401e">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=hustcer/milestone-action&package-manager=github_actions&previous-version=3.2&new-version=3.3)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## November 17, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/44197412683), [2](https://github.com/ghostty-org/ghostty/actions/runs/44177280756), [3](https://github.com/ghostty-org/ghostty/actions/runs/44140849876), [4](https://github.com/ghostty-org/ghostty/actions/runs/44116065599)  
Summary: 4 runs • 6 commits • 4 authors

### Changes

- [`c688263`](https://github.com/ghostty-org/ghostty/commit/c68826391717a5f12e3408000e6623f3df926d6c) benchmark: add scrollback-search benchmark ([@teddytennant](https://github.com/teddytennant))
- [`f3e1f65`](https://github.com/ghostty-org/ghostty/commit/f3e1f65bb602ac3d441ffdd5f9645bef66a39648) benchmark: add scrollback-search benchmark ([#15267](https://github.com/ghostty-org/ghostty/issues/15267)) ([@jcollie](https://github.com/jcollie))
  ```text
  Adds `ghostty-bench +scrollback-search` (#15262). It loads `--data` into
  the primary screen, then searches all of it with `ScreenSearch`.
  
  - `typing` searches each prefix of `--needle` from scratch, like the
  search thread does while you type.
  - `report` prints per-prefix timings, including time in `feed`, which
  runs under the terminal lock.
  - `--compress` compresses history first.
  
  On a full default scrollback of Ghostty's source (47,560 rows,
  i7-11700K), each keystroke takes about 18 ms, 15.5 of it in `feed`.
  Compressed, 27 ms and 24 ms.
  
  AI disclosure: I had fable 5.2 help me explore the codebase and review
  my code
  ```
- [`9ba17be`](https://github.com/ghostty-org/ghostty/commit/9ba17be7b95dab894f259329b4a568a6667f276c) gtk: preserve IME commits triggered by key release ([@aohanhongzhi](https://github.com/aohanhongzhi))
- [`47b5c20`](https://github.com/ghostty-org/ghostty/commit/47b5c2026927b0d8a38d224c5d34008589fd6d19) gtk: preserve IME commits triggered by key release ([#15246](https://github.com/ghostty-org/ghostty/issues/15246)) ([@jcollie](https://github.com/jcollie))
  ```text
  When client preedit is disabled in Fcitx5, tapping Shift to commit
  pending Latin input can lose the text in Ghostty. For example, typing
  `abc` in WowType and tapping Shift produces no terminal input, even
  though the IME commits `abc`.
  
  Without client preedit, `im_composing` remains false. A commit emitted
  synchronously during `filterKeypress` is therefore buffered as ordinary
  key text. When the triggering event is a key release, legacy key
  encoding discards that text.
  
  Track key releases separately in `IMKeyEvent` and send their IME commits
  through the existing independent-text path. Press/repeat commits retain
  their existing handling.
  
  Validation:
  - Reproduced with Ghostty 1.3.1, Fcitx5/WowType, GTK 4.14.5 and
  libadwaita 1.5.0 under an isolated Xvfb/D-Bus session: client preedit
  off loses `abc`; client preedit on commits it.
  - Backported the fix to 1.3.1 and built with Zig 0.15.2. With client
  preedit off, left Shift, right Shift and Return each commit `abc`;
  typing `XYZ` after the left-Shift switch produces `abcXYZ`.
  - The installed backport was also confirmed working by the affected
  user.
  - On this PR's main-based change, `zig fmt --check` and `git diff
  --check` pass. Main's build/tests could not complete locally because
  they require libadwaita >= 1.7, while this system has 1.5.0. Runtime
  results above are for the backport, not main.
  
  AI disclosure: OpenAI Codex assisted with investigation, implementation,
  building, automated reproduction, and this PR description. The user
  reproduced the original problem and confirmed the installed fix.
  ```
- [`356b3b3`](https://github.com/ghostty-org/ghostty/commit/356b3b399290c12a2723a613ebee0c49eeee4b72) Update VOUCHED list ([#15269](https://github.com/ghostty-org/ghostty/issues/15269)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/15268#issuecomment-6956126500)
  from @mitchellh.
  
  Vouch: @davidbrochart
  ```
- [`b634352`](https://github.com/ghostty-org/ghostty/commit/b634352b739dbe4a0389ae7c6ae4585462cfa96e) Update VOUCHED list ([#15263](https://github.com/ghostty-org/ghostty/issues/15263)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/15262#discussioncomment-19683634)
  from @jcollie.
  
  Vouch: @teddytennant
  ```

## November 16, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/43897023330), [2](https://github.com/ghostty-org/ghostty/actions/runs/43800593590), [3](https://github.com/ghostty-org/ghostty/actions/runs/43782996616)  
Summary: 3 runs • 4 commits • 3 authors

### Changes

- [`5ebe501`](https://github.com/ghostty-org/ghostty/commit/5ebe501a63425b13d9952e8c54682c046386e5af) Update VOUCHED list ([#15249](https://github.com/ghostty-org/ghostty/issues/15249)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/15247#discussioncomment-19657452)
  from @jcollie.
  
  Vouch: @aohanhongzhi
  ```
- [`d4cf6ec`](https://github.com/ghostty-org/ghostty/commit/d4cf6ec225dc0398f3d46024b1437a7f5b0f8777) Update VOUCHED list ([#15244](https://github.com/ghostty-org/ghostty/issues/15244)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/15235#discussioncomment-19645399)
  from @mitchellh.
  
  Vouch: @craig-b
  ```
- [`32abdc3`](https://github.com/ghostty-org/ghostty/commit/32abdc39251f398a14a0448e21430f74555a603c) build(deps): bump cachix/install-nix-action from 31.11.3 to 31.11.5 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [cachix/install-nix-action](https://github.com/cachix/install-nix-action) from 31.11.3 to 31.11.5.
  - [Release notes](https://github.com/cachix/install-nix-action/releases)
  - [Changelog](https://github.com/cachix/install-nix-action/blob/master/RELEASE.md)
  - [Commits](https://github.com/cachix/install-nix-action/compare/75c75c31ebece974e48ebc36b4ad125bd97bd97b...3dc140bfc76c49fbd4dd958429132e3746bcb086)
  
  ---
  updated-dependencies:
  - dependency-name: cachix/install-nix-action
    dependency-version: 31.11.5
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`542611b`](https://github.com/ghostty-org/ghostty/commit/542611b3db75d320907ed09fac9a61b572ca86d9) build(deps): bump cachix/install-nix-action from 31.11.3 to 31.11.5 ([#15243](https://github.com/ghostty-org/ghostty/issues/15243)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [cachix/install-nix-action](https://github.com/cachix/install-nix-action)
  from 31.11.3 to 31.11.5.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/cachix/install-nix-action/releases">cachix/install-nix-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v31.11.5</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>nix: 2.35.5 -&gt; 2.35.6 by <a
  href="https://github.com/github-actions"><code>@​github-actions</code></a>[bot]
  in <a
  href="https://redirect.github.com/cachix/install-nix-action/pull/286">cachix/install-nix-action#286</a>
  <a
  href="https://github.com/NixOS/nix/compare/2.35.5...2.35.6">https://github.com/NixOS/nix/compare/2.35.5...2.35.6</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/cachix/install-nix-action/compare/v31.11.4...v31.11.5">https://github.com/cachix/install-nix-action/compare/v31.11.4...v31.11.5</a></p>
  <h2>v31.11.4</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>nix: 2.35.4 -&gt; 2.35.5 by <a
  href="https://github.com/github-actions"><code>@​github-actions</code></a>[bot]
  in <a
  href="https://redirect.github.com/cachix/install-nix-action/pull/285">cachix/install-nix-action#285</a>
  <a
  href="https://github.com/NixOS/nix/compare/2.35.4...2.35.5">https://github.com/NixOS/nix/compare/2.35.4...2.35.5</a></li>
  <li>fix: prevent <code>extra-experimental-flags</code> from overriding
  the default <code>experimental-flags</code> <a
  href="https://redirect.github.com/cachix/install-nix-action/issues/280">cachix/install-nix-action#280</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/cachix/install-nix-action/compare/31.11.3...v31.11.4">https://github.com/cachix/install-nix-action/compare/31.11.3...v31.11.4</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/3dc140bfc76c49fbd4dd958429132e3746bcb086"><code>3dc140b</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/install-nix-action/issues/286">#286</a>
  from cachix/create-pull-request/patch</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/4a2975a2dca3cbb2d8ab548cce58c031b4d34427"><code>4a2975a</code></a>
  nix: 2.35.5 -&gt; 2.35.6</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/91f6a0f59e94dfb2cfed0f4000f36a68ead1d20c"><code>91f6a0f</code></a>
  fix: set defaults early and prevent extra-experimental-features from
  breaking...</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/00c5b1cd086ebe268a49bcad4dbf28b743ec2f9e"><code>00c5b1c</code></a>
  fix(ci): drop unsupported macos-14 runner</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/42a481b9609c29a582a42766228db91ae970eed3"><code>42a481b</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/install-nix-action/issues/285">#285</a>
  from cachix/create-pull-request/patch</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/4b19a0032d58a4215d3a8d41ad5107d7901f39b5"><code>4b19a00</code></a>
  nix: 2.35.4 -&gt; 2.35.5</li>
  <li>See full diff in <a
  href="https://github.com/cachix/install-nix-action/compare/75c75c31ebece974e48ebc36b4ad125bd97bd97b...3dc140bfc76c49fbd4dd958429132e3746bcb086">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=cachix/install-nix-action&package-manager=github_actions&previous-version=31.11.3&new-version=31.11.5)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## November 15, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/43676333954), [2](https://github.com/ghostty-org/ghostty/actions/runs/43661574384), [3](https://github.com/ghostty-org/ghostty/actions/runs/43658848165)  
Summary: 3 runs • 10 commits • 3 authors

### Changes

- [`285af45`](https://github.com/ghostty-org/ghostty/commit/285af456014219bf8c86bac75c930179ecae452f) nix: update nixpkgs to get Zig 0.17.1 ([@jcollie](https://github.com/jcollie))
- [`931544b`](https://github.com/ghostty-org/ghostty/commit/931544b1078f855b9db152008b582b75b8e0c360) nix: update zig-overlay to Zig 0.17.1 ([@jcollie](https://github.com/jcollie))
- [`1d84459`](https://github.com/ghostty-org/ghostty/commit/1d84459682a983a7b91979e14214ffec7f239cad) build: require Zig 0.17.1 ([@jcollie](https://github.com/jcollie))
- [`f4830b2`](https://github.com/ghostty-org/ghostty/commit/f4830b2f18785aba11af9d92239f35c6e211abca) terminal: don't check PageList integrity mid-way through growing rows ([@jcollie](https://github.com/jcollie))
  ```text
  Growing the row count sets self.rows to the new size before calling
  grow(), so that grow() doesn't prune pages the active area needs. Until
  the last grow() the list therefore holds fewer rows than the active
  area claims, and a viewport pinned in history appears to have too few
  rows below it. Each grow() asserts integrity on the way out, so a Debug
  build panicked with ViewportPinInsufficientRows whenever the terminal
  was resized taller while scrolled up. Both the pull-scrollback and the
  no-pull paths were affected.
  
  Pause integrity checks across the row growth; resize() still verifies
  the final state.
  
  Reported in discussion #15234.
  
  Fixes #15236
  ```
- [`2521ab9`](https://github.com/ghostty-org/ghostty/commit/2521ab9f64d052db84f86a6779709e587d558a80) nix: update to Zig 0.17.1 ([#15230](https://github.com/ghostty-org/ghostty/issues/15230)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Update nixpkgs and the Zig overlay to get Zig 0.17.1.
  ```
- [`7fa26e8`](https://github.com/ghostty-org/ghostty/commit/7fa26e8b675f3248975479d88274c937d7e63905) terminal: don't check PageList integrity mid-way through growing rows ([#15237](https://github.com/ghostty-org/ghostty/issues/15237)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Growing the row count sets self.rows to the new size before calling
  grow(), so that grow() doesn't prune pages the active area needs. Until
  the last grow() the list therefore holds fewer rows than the active area
  claims, and a viewport pinned in history appears to have too few rows
  below it. Each grow() asserts integrity on the way out, so a Debug build
  panicked with ViewportPinInsufficientRows whenever the terminal was
  resized taller while scrolled up. Both the pull-scrollback and the
  no-pull paths were affected.
  
  Pause integrity checks across the row growth; resize() still verifies
  the final state.
  
  Reported in discussion #15234.
  
  Fixes #15236
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`18adc65`](https://github.com/ghostty-org/ghostty/commit/18adc65d0285ec4757ee1ab06300ddcd0cad7cee) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`35188fe`](https://github.com/ghostty-org/ghostty/commit/35188fe06a655d04c6ffcaf277a966aef80e3cf5) Update iTerm2 colorschemes ([#15239](https://github.com/ghostty-org/ghostty/issues/15239)) ([@jcollie](https://github.com/jcollie))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20261109-150625-5fad1bd
  ```
- [`226070d`](https://github.com/ghostty-org/ghostty/commit/226070de59daeb0e472f8122d0389198f4707e02) i18n: correctly collect translation context comments ([@trag1c](https://github.com/trag1c))
- [`a757b70`](https://github.com/ghostty-org/ghostty/commit/a757b703fed1da2ed633e2bd1782d439d9bd4e58) build: correctly collect translation context comments ([#15238](https://github.com/ghostty-org/ghostty/issues/15238)) ([@jcollie](https://github.com/jcollie))
  ```text
  I think this is a regression from #9976 (haven't verified though) and
  that we never noticed because we don't use this functionality at all.
  Before this change, all comments would get dropped since the flag was
  present when merging `.pot` files and not when creating them.
  
  **AI disclosure:** Claude Haiku 5.5 found this. I reproduced and fixed
  the issue and wrote everything here myself.
  ```

## November 14, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/43542056669)  
Summary: 1 runs • 5 commits • 1 authors

### Changes

- [`eeac3a4`](https://github.com/ghostty-org/ghostty/commit/eeac3a4422b82b53d1e00ff43742504a12419e3a) pkg/fontconfig: set the package version to 2.18.3 ([@jcollie](https://github.com/jcollie))
  ```text
  The bundled source was updated to 2.18.3 but the package version was
  left at 2.14.2. build.zig derives -DFC_VERSION_{MAJOR,MINOR,MICRO} from
  it, and fontconfig stamps its cache files with that version and compares
  caches against it, so the library has been building as if it were
  2.14.2.
  ```
- [`ba283a6`](https://github.com/ghostty-org/ghostty/commit/ba283a6f90e77bbe92e49f7c25233d6c58a526c7) font/discovery: skip fontconfig matches that have no file ([@jcollie](https://github.com/jcollie))
  ```text
  Fontconfig has been seen to return a match, from what is in a user's
  font cache, that carries a charset and a lang but no file, family or
  index. If its charset claims the codepoint being searched for, fallback
  discovery accepts it and the codepoint is assigned a face that can never
  be loaded, even though good fonts for it come later in the sorted list.
  
  Skip a match unless it has the file and index DeferredFace needs to
  load it, so the next candidate is used instead.
  ```
- [`efd4a82`](https://github.com/ghostty-org/ghostty/commit/efd4a82bda0b6c36ec3165386e8165002c6fc215) font: treat a fallback face that fails to load as no font ([@jcollie](https://github.com/jcollie))
  ```text
  SharedGrid.getIndex preloads the face it resolves a codepoint to, and
  returned the error if the load failed. The run iterator passes that
  error up and the renderer, on any error building a row, clears the
  whole row. So one codepoint whose face cannot be loaded blanked every
  row it appeared on, and because the failed lookup was not cached, the
  load was retried on every frame.
  
  Seen with U+1F17C on a system where fontconfig returned a match with
  no file: every row containing it was blank, while the text was still
  there to copy.
  
  Log the failure and cache the codepoint as having no font instead, so
  the run iterator falls back to U+FFFD for that cell. OutOfMemory is
  still returned, since it may pass.
  ```
- [`ef21f06`](https://github.com/ghostty-org/ghostty/commit/ef21f065f899575cb58616ebb9c03b2c9da611fb) font: list the face load errors that mean no font ([@jcollie](https://github.com/jcollie))
  ```text
  Name the errors that mean the face has nothing we can open or read:
  fontconfig's lookup errors (a match with no file or index), CoreText's
  FontHasNoFile and FontPathCantDecode, and FreeType's CannotOpenResource,
  UnknownFileFormat and InvalidFileFormat. Every other error is returned.
  
  The switch is over anyerror because getFace's error set depends on the
  font backend, and a prong naming an error outside the set does not
  compile.
  ```
- [`6d95777`](https://github.com/ghostty-org/ghostty/commit/6d9577708a211b0e6c5e6c6886f3cfb7efc47555) font: don't blank a row when a fallback face can't be loaded ([#15216](https://github.com/ghostty-org/ghostty/issues/15216)) ([@jcollie](https://github.com/jcollie))
  ````text
  A user on 1.4.0 (Snap) reported that any row containing U+1F17C (🅼) was
  drawn completely blank, though the text was still there to copy.
  Starship's
  default Maven symbol is 🅼, so the first line of their prompt vanished.
  
  `ghostty +show-face --cp=0x1F17C` on their machine printed:
  
  ```
  info(font_codepoint_resolver): found codepoint 0x1F17C in fallback face=<error>
  Unable to get face: error.FontconfigNoMatch
  ```
  
  Fontconfig returned a fallback match whose charset claims U+1F17C but
  which
  has no `file`, `index` or family.
  
  Two things in Ghostty turned that into a blank row:
  
  - Fallback discovery accepted the match, so the codepoint was given a
  face
    that can never load.
  - `SharedGrid.getIndex` preloads the face and returned the error. The
  run
  iterator passes it up, `rebuildRow` fails, and the renderer clears the
  whole
    row. The failed lookup wasn't cached, so it was retried every frame.
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ````

## November 13, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/43515100328), [2](https://github.com/ghostty-org/ghostty/actions/runs/43472953670), [3](https://github.com/ghostty-org/ghostty/actions/runs/43468038557)  
Summary: 3 runs • 12 commits • 4 authors

### Changes

- [`a0fe573`](https://github.com/ghostty-org/ghostty/commit/a0fe573fe3e147ee9a3d86201d5b323cd07935cc) config: copy-on-select defaults to the selection clipboard on macOS ([@jcollie](https://github.com/jcollie))
  ```text
  Ghostty 1.4 changed the macOS default for copy-on-select from `true`
  to `none`, so selecting text no longer fills the private selection
  pasteboard that Paste Selection (`paste_from_selection`) reads, and
  Paste Selection keeps pasting whatever was copied there before the
  upgrade. The compatibility mapping made `true` mean `clipboard` on
  macOS, so setting `copy-on-select = true` didn't bring it back either.
  
  The macOS app does have a selection clipboard: it reports
  `supports_selection_clipboard` and serves it with its own pasteboard,
  which is what `true` copied to before 1.4. So default to `primary` on
  macOS as on Linux, map `true` to `primary` there as well, and fix the
  docs that said `primary` has no effect on macOS. Also note that
  `clipboard` no longer copies to the selection clipboard, which it did
  before 1.4, and that `both` is the value for that.
  
  See: https://github.com/ghostty-org/ghostty/discussions/14895
  ```
- [`f08437b`](https://github.com/ghostty-org/ghostty/commit/f08437b7956abdefa0d6e0431c495303a7009069) config: copy-on-select defaults to the selection clipboard on macOS ([#15147](https://github.com/ghostty-org/ghostty/issues/15147)) ([@jcollie](https://github.com/jcollie))
  ```text
  Ghostty 1.4 changed the macOS default for copy-on-select from `true` to
  `none`, so selecting text no longer fills the private selection
  pasteboard that Paste Selection (`paste_from_selection`) reads, and
  Paste Selection keeps pasting whatever was copied there before the
  upgrade. The compatibility mapping made `true` mean `clipboard` on
  macOS, so setting `copy-on-select = true` didn't bring it back either.
  
  The macOS app does have a selection clipboard: it reports
  `supports_selection_clipboard` and serves it with its own pasteboard,
  which is what `true` copied to before 1.4. So default to `primary` on
  macOS as on Linux, map `true` to `primary` there as well, and fix the
  docs that said `primary` has no effect on macOS. Also note that
  `clipboard` no longer copies to the selection clipboard, which it did
  before 1.4, and that `both` is the value for that.
  
  See: https://github.com/ghostty-org/ghostty/discussions/14895
  
  AI disclosure: Claude Code was used in the preparation of this PR.
  ```
- [`6e0c818`](https://github.com/ghostty-org/ghostty/commit/6e0c8186f28902c3b902028945435f652dd035a8) terminal/kitty: skip the temp-dir rejection test under /tmp ([@jcollie](https://github.com/jcollie))
  ```text
  The test that a temporary file outside the configured directory is
  rejected puts the file in std.testing.tmpDir, which is under the
  working directory. When the tests run from under /tmp, as some
  package builds do, that file is inside /tmp and is always accepted,
  so the test failed.
  
  Move the directories that are always accepted into one list, used by
  isPathInTempDir and by the test, and skip the test when its file is
  in one of them.
  ```
- [`46f1cea`](https://github.com/ghostty-org/ghostty/commit/46f1cea1a10a19bef97a8a0f5948e660d0b74fe2) terminal/kitty: skip the temp-dir rejection test under /tmp ([#15225](https://github.com/ghostty-org/ghostty/issues/15225)) ([@jcollie](https://github.com/jcollie))
  ```text
  The test that a temporary file outside the configured directory is
  rejected puts the file in std.testing.tmpDir, which is under the working
  directory. When the tests run from under /tmp, as some package builds
  do, that file is inside /tmp and is always accepted, so the test failed.
  
  Move the directories that are always accepted into one list, used by
  isPathInTempDir and by the test, and skip the test when its file is in
  one of them.
  
  AI disclosure: Claude Code was used in the development of this PR.
  ```
- [`52cd6c9`](https://github.com/ghostty-org/ghostty/commit/52cd6c9f15a313c3b668be37017a5932a7d2364b) build(deps): bump peter-evans/create-pull-request from 8.1.2 to 8.1.3 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [peter-evans/create-pull-request](https://github.com/peter-evans/create-pull-request) from 8.1.2 to 8.1.3.
  - [Release notes](https://github.com/peter-evans/create-pull-request/releases)
  - [Commits](https://github.com/peter-evans/create-pull-request/compare/15733dbdfeedb4f7fdb73d13c6f5ac83b710fab8...3ffccacd46053766916f087ce41d627c0b8cf2d1)
  
  ---
  updated-dependencies:
  - dependency-name: peter-evans/create-pull-request
    dependency-version: 8.1.3
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`dcdb167`](https://github.com/ghostty-org/ghostty/commit/dcdb1674cf846030da6cc2e2ff356baa1cbecc91) terminal: clear a clone's padding rows to their page's width ([@arc-source-coder](https://github.com/arc-source-coder))
  ```text
  `PageList.clone` pads a cloned region with blank rows when it is shorter
  than the active area, but clears them to the list's width. A page can be
  narrower than its list, so the clear can write past the end of the row.
  
  Clear to the page's width, and assert the range in `Page.clearCells`.
  ```
- [`8434d09`](https://github.com/ghostty-org/ghostty/commit/8434d0900e86a63907d0da4b0892cbb89533be0d) terminal: avoid the pin lookup on a carriage return ([@arc-source-coder](https://github.com/arc-source-coder))
  ```text
  Every carriage return goes through `cursorHorizontalAbsolute`, which
  looks the row and cell up again through the page pin even though the
  cursor stays on its row.
  
  Move the cached cell pointer by the column difference instead, like
  `cursorLeft` and `cursorRight` do.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream` at 120x80, on Windows x86-64:
  
  | Input                         | Before (ms)   | After (ms)    | Speedup |
  | ----------------------------- | ------------- | ------------- | ------- |
  | scrolling (20MB scrollback)   | 1022.2 ± 26.3 | 997.6 ± 21.2  | 1.02x   |
  | scrolling_bottom_region       | 540.5 ± 8.0   | 516.5 ± 8.6   | 1.05x   |
  | scrolling_bottom_small_region | 527.0 ± 17.8  | 497.8 ± 13.7  | 1.06x   |
  | scrolling_fullscreen          | 47.0 ± 3.6    | 45.6 ± 1.5    | 1.03x   |
  | scrolling_top_region          | 528.2 ± 11.8  | 507.6 ± 10.9  | 1.04x   |
  | scrolling_top_small_region    | 522.3 ± 12.9  | 512.3 ± 17.3  | 1.02x   |
  ```
- [`a5cd02e`](https://github.com/ghostty-org/ghostty/commit/a5cd02e8afed4289fab5a2dad50c695b81d46d7a) terminal: clear a clone's padding rows to their page's width ([#15222](https://github.com/ghostty-org/ghostty/issues/15222)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `PageList.clone` pads a cloned region with blank rows when it is shorter
  than the active area, but clears them to the list's width. A page can be
  narrower than its list, so the clear can write past the end of the row.
  
  This clears to the page's width instead, and asserts the range in
  `Page.clearCells`.
  
  AI disclosure: Developed with Claude Code (Opus 5.5).
  ```
- [`9fff234`](https://github.com/ghostty-org/ghostty/commit/9fff23493f87a2a9a9b56b29dca45e27d5adf27e) terminal: avoid the pin lookup on a carriage return ([#15221](https://github.com/ghostty-org/ghostty/issues/15221)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Every carriage return goes through `cursorHorizontalAbsolute`, which
  looks the row and cell up again through the page pin even though the
  cursor stays on its row.
  
  This moves the cached cell pointer by the column difference instead,
  like `cursorLeft` and `cursorRight` do.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream` at 120x80, on Windows x86-64:
  
  | Input | Before (ms) | After (ms) | Speedup |
  | ----------------------------- | ------------- | ------------- |
  ------- |
  | scrolling (20MB scrollback) | 1022.2 ± 26.3 | 997.6 ± 21.2 | 1.02x |
  | scrolling_bottom_region | 540.5 ± 8.0 | 516.5 ± 8.6 | 1.05x |
  | scrolling_bottom_small_region | 527.0 ± 17.8 | 497.8 ± 13.7 | 1.06x |
  | scrolling_fullscreen | 47.0 ± 3.6 | 45.6 ± 1.5 | 1.03x |
  | scrolling_top_region | 528.2 ± 11.8 | 507.6 ± 10.9 | 1.04x |
  | scrolling_top_small_region | 522.3 ± 12.9 | 512.3 ± 17.3 | 1.02x |
  
  AI disclosure: Developed with Claude Code (Opus 5.5).
  ```
- [`a09d940`](https://github.com/ghostty-org/ghostty/commit/a09d94003cf29d5b7f9cf20ecfa81b1e0a36abb9) terminal: unify Page and Screen clearCells ([@arc-source-coder](https://github.com/arc-source-coder))
  ```text
  `Screen.clearCells` keeps its own copy of `Page.clearCells` that fills
  cells with the cursor's blank cell. Only the screen's copy skips rows
  that are already blank and releases styles a run at a time.
  
  Move the implementation into `Page.clearCells`, which now takes the
  blank cell, and use it for `Screen.clearCells` and the background fill
  after scrolling.
  
  Release resources out of line in `releaseCells`, and use `Mask.eqlEnd`
  both to find style runs and to check whether a row still has styled
  cells.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream` on Windows x86-64, with 32 MB
  of `ghostty-gen +erase --seed=1` output:
  
  | Size    | Before (ms)  | After (ms)   | Speedup |
  | ------- | ------------ | ------------ | ------- |
  | 120x80  | 240.0 ± 8.2  | 228.1 ± 2.8  | 1.05x   |
  | 120x12  | 217.3 ± 3.5  | 210.0 ± 6.4  | 1.03x   |
  | 160x50  | 252.5 ± 10.6 | 238.3 ± 5.8  | 1.06x   |
  | 300x100 | 330.1 ± 7.3  | 310.1 ± 13.1 | 1.06x   |
  ```
- [`06ad376`](https://github.com/ghostty-org/ghostty/commit/06ad376742a0c8b04af33fc401d1f445e53560c2) build(deps): bump peter-evans/create-pull-request from 8.1.2 to 8.1.3 ([#15217](https://github.com/ghostty-org/ghostty/issues/15217)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [peter-evans/create-pull-request](https://github.com/peter-evans/create-pull-request)
  from 8.1.2 to 8.1.3.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/peter-evans/create-pull-request/releases">peter-evans/create-pull-request's
  releases</a>.</em></p>
  <blockquote>
  <h2>Create Pull Request v8.1.3</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>fix: check git ref directly when pushing signed commits by <a
  href="https://github.com/peter-evans"><code>@​peter-evans</code></a> in
  <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4521">peter-evans/create-pull-request#4521</a></li>
  <li>Update distribution by <a
  href="https://github.com/actions-bot"><code>@​actions-bot</code></a> in
  <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4526">peter-evans/create-pull-request#4526</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/peter-evans/create-pull-request/compare/v8.1.2...v8.1.3">https://github.com/peter-evans/create-pull-request/compare/v8.1.2...v8.1.3</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/peter-evans/create-pull-request/commit/3ffccacd46053766916f087ce41d627c0b8cf2d1"><code>3ffccac</code></a>
  build: update distribution (<a
  href="https://redirect.github.com/peter-evans/create-pull-request/issues/4526">#4526</a>)</li>
  <li><a
  href="https://github.com/peter-evans/create-pull-request/commit/77d56500d90859d7079a6d0dae948d3c1d197278"><code>77d5650</code></a>
  fix: check git ref directly when pushing signed commits (<a
  href="https://redirect.github.com/peter-evans/create-pull-request/issues/4521">#4521</a>)</li>
  <li>See full diff in <a
  href="https://github.com/peter-evans/create-pull-request/compare/15733dbdfeedb4f7fdb73d13c6f5ac83b710fab8...3ffccacd46053766916f087ce41d627c0b8cf2d1">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=peter-evans/create-pull-request&package-manager=github_actions&previous-version=8.1.2&new-version=8.1.3)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`8046a23`](https://github.com/ghostty-org/ghostty/commit/8046a2360340ec9788e0089da5a9ed0378adf0ea) terminal: unify Page and Screen clearCells ([#15224](https://github.com/ghostty-org/ghostty/issues/15224)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `Screen.clearCells` currently keeps its own copy of `Page.clearCells`
  that fills cells with the cursor's blank cell. Only the screen's copy
  skips rows that are already blank and releases styles a run at a time.
  
  This moves the implementation into `Page.clearCells`, which now takes
  the blank cell, and uses it for `Screen.clearCells` and the background
  fill after scrolling.
  
  Resources are now released out of line in `releaseCells`, and
  `Mask.eqlEnd` is used to find style runs and check whether a row still
  has styled cells.
  
  ## Benchmarks
  
  `ghostty-bench +terminal-stream` on Windows x86-64, with 32 MB of
  `ghostty-gen +erase --seed=1` output:
  
  | Size    | main (ms)  | This PR (ms)   | Speedup |
  | ------- | ------------ | ------------ | ------- |
  | 120x80  | 240.0 ± 8.2  | 228.1 ± 2.8  | 1.05x   |
  | 120x12  | 217.3 ± 3.5  | 210.0 ± 6.4  | 1.03x   |
  | 160x50  | 252.5 ± 10.6 | 238.3 ± 5.8  | 1.06x   |
  | 300x100 | 330.1 ± 7.3  | 310.1 ± 13.1 | 1.06x   |
  
  AI disclosure: Developed with Claude Code (Opus 5.5).
  ```

## November 12, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/43236342398), [2](https://github.com/ghostty-org/ghostty/actions/runs/43156147800)  
Summary: 2 runs • 3 commits • 3 authors

### Changes

- [`cf3a8a6`](https://github.com/ghostty-org/ghostty/commit/cf3a8a6594eec899fe6335465668c60f2281ce9c) Update VOUCHED list ([#15213](https://github.com/ghostty-org/ghostty/issues/15213)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/15212#discussioncomment-19566389)
  from @trag1c.
  
  Denounce: @MisterWanted
  ```
- [`73b201e`](https://github.com/ghostty-org/ghostty/commit/73b201ed3355622eb4e6ff8c3fb703fb1fed702c) docs: fix prettier error in vt release notes ([@jcollie](https://github.com/jcollie))
- [`72ac7dc`](https://github.com/ghostty-org/ghostty/commit/72ac7dced84e96a5d5214d005d59eadd10da27bb) docs: fix prettier error in vt release notes ([#15211](https://github.com/ghostty-org/ghostty/issues/15211)) ([@mitchellh](https://github.com/mitchellh))

