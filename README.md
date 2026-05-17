> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: May 17, 2026 at 09:34 UTC.

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

## May 11, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/25658156161), [2](https://github.com/ghostty-org/ghostty/actions/runs/25657875662)  
Summary: 2 runs • 3 commits • 1 authors

### Changes

- [`611525a`](https://github.com/ghostty-org/ghostty/commit/611525ac3f6cc3e2c63988ad8111d7ace093950e) Update VOUCHED list ([#12655](https://github.com/ghostty-org/ghostty/issues/12655)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12618#discussioncomment-16876561)
  from @pluiedev.
  
  Vouch: @thirstycrow
  ```
- [`64131dc`](https://github.com/ghostty-org/ghostty/commit/64131dcd413ef27147378e2139efe1d2d81e092a) Update VOUCHED list ([#12656](https://github.com/ghostty-org/ghostty/issues/12656)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12616#discussioncomment-16876564)
  from @pluiedev.
  
  Vouch: @00JCIV00
  ```
- [`4c68594`](https://github.com/ghostty-org/ghostty/commit/4c6859447cd794a96b79ae549d1e8e48a5c9874e) Update VOUCHED list ([#12654](https://github.com/ghostty-org/ghostty/issues/12654)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12650#discussioncomment-16876487)
  from @pluiedev.
  
  Vouch: @athaapa
  ```

