> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: July 2, 2026 at 06:36 UTC.

## July 2, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/28563110896)  
Summary: 1 runs • 2 commits • 1 authors

### Changes

- [`aea63d7`](https://github.com/ghostty-org/ghostty/commit/aea63d71fe6630ae940b8ecf07d35851c0c11fba) libghostty: fix utf-8 grapheme length overflow ([@mitchellh](https://github.com/mitchellh))
  ```text
  The GRAPHEMES_UTF8 row-cells getter inferred its required byte
  accumulator from utf8CodepointSequenceLength, which stores the
  value in u3. Multi-scalar clusters longer than seven UTF-8 bytes
  could overflow that accumulator before the capacity check, causing
  wrong probe sizes and allowing optimized builds to write past a
  caller-provided buffer.
  
  Use usize for the required byte count so probing and capacity
  checks match the later encode loop. Extend the render C API test
  to cover the short combining cluster, an eight-byte flag cluster,
  a longer family emoji, exact-size success, and the
  cap == needed - 1 no-write boundary.
  ```
- [`c22df09`](https://github.com/ghostty-org/ghostty/commit/c22df09da10b27dd248b21b7be8b26dcbddeb8ef) libghostty: fix utf-8 grapheme length overflow ([#13145](https://github.com/ghostty-org/ghostty/issues/13145)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The GRAPHEMES_UTF8 row-cells getter inferred its required byte
  accumulator from utf8CodepointSequenceLength, which stores the value in
  u3. Multi-scalar clusters longer than seven UTF-8 bytes could overflow
  that accumulator before the capacity check, causing wrong probe sizes
  and allowing optimized builds to write past a caller-provided buffer.
  
  Use usize for the required byte count so probing and capacity checks
  match the later encode loop. Extend the render C API test to cover the
  short combining cluster, an eight-byte flag cluster, a longer family
  emoji, exact-size success, and the cap == needed - 1 no-write boundary.
  ```

## July 1, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/28551941025), [2](https://github.com/ghostty-org/ghostty/actions/runs/28537629892), [3](https://github.com/ghostty-org/ghostty/actions/runs/28485879059)  
Summary: 3 runs • 5 commits • 4 authors

### Changes

- [`df5cee2`](https://github.com/ghostty-org/ghostty/commit/df5cee23829e14074d546c63baca839c47326d6f) Update VOUCHED list ([#13141](https://github.com/ghostty-org/ghostty/issues/13141)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13121#discussioncomment-17502740)
  from @jcollie.
  
  Vouch: @yak3d
  ```
- [`480edb4`](https://github.com/ghostty-org/ghostty/commit/480edb45e323daf21993c32d386a457ee8c23e96) ci: skip tip release when only non-artifact files change ([@claude](https://github.com/claude))
  ```text
  Detect changes since the last tip with dorny/paths-filter (base: tip)
  and skip the build when a push touches only files that never reach the
  built artifact: all of .github (except release-tip.yml, which defines the
  build/tag/publish jobs) plus docs and repo/lint/editor metadata.
  ```
- [`8b71d7a`](https://github.com/ghostty-org/ghostty/commit/8b71d7a03cf345b6430171e480fa6e5135953095) ci: skip tip release when only non-artifact files change ([#13130](https://github.com/ghostty-org/ghostty/issues/13130)) ([@jcollie](https://github.com/jcollie))
  ```text
  Ignore more files when releasing tip. Moved release-tip run to a
  separate script so we can test against it.
  
  ### AI Disclosure
  
  Claude did this, I reviewed the changes and asked it run the tests
  locally before creating the pr.
  ```
- [`c6b0c0d`](https://github.com/ghostty-org/ghostty/commit/c6b0c0dcb45f4fa8dfb1d74604568ced30f8c48d) build(deps): bump namespacelabs/nscloud-cache-action from 1.5.0 to 1.6.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [namespacelabs/nscloud-cache-action](https://github.com/namespacelabs/nscloud-cache-action) from 1.5.0 to 1.6.0.
  - [Release notes](https://github.com/namespacelabs/nscloud-cache-action/releases)
  - [Commits](https://github.com/namespacelabs/nscloud-cache-action/compare/d6b68aa38adace8976c09629021052d57bb1ce9c...58bf6e08898e88803c098e2b522668541cd3b2e3)
  
  ---
  updated-dependencies:
  - dependency-name: namespacelabs/nscloud-cache-action
    dependency-version: 1.6.0
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`e1d31de`](https://github.com/ghostty-org/ghostty/commit/e1d31deaaed21aa9225afca78d778fb373c95852) build(deps): bump namespacelabs/nscloud-cache-action from 1.5.0 to 1.6.0 ([#13126](https://github.com/ghostty-org/ghostty/issues/13126)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [namespacelabs/nscloud-cache-action](https://github.com/namespacelabs/nscloud-cache-action)
  from 1.5.0 to 1.6.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/namespacelabs/nscloud-cache-action/releases">namespacelabs/nscloud-cache-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v1.6.0</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>Remove unused Unix-only helpers from utils by <a
  href="https://github.com/rcrowe"><code>@​rcrowe</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/148">namespacelabs/nscloud-cache-action#148</a></li>
  <li>Validate cache links on Windows runners by <a
  href="https://github.com/rcrowe"><code>@​rcrowe</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/149">namespacelabs/nscloud-cache-action#149</a></li>
  <li>Early Windows support -&gt; Bump actions-toolkit to v0.4.0, fix
  Dependabot &amp; patch security advisories by <a
  href="https://github.com/rcrowe"><code>@​rcrowe</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/150">namespacelabs/nscloud-cache-action#150</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/namespacelabs/nscloud-cache-action/compare/v1...v1.6.0">https://github.com/namespacelabs/nscloud-cache-action/compare/v1...v1.6.0</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/58bf6e08898e88803c098e2b522668541cd3b2e3"><code>58bf6e0</code></a>
  Bump actions-toolkit to v0.4.0; fix Dependabot and patch security
  advisories ...</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/07c62f87b6a9734917f8944b3afce3181492e327"><code>07c62f8</code></a>
  Validate cache links on Windows runners (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/149">#149</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/148be15ff18531cb436517206569f053ce7bf8d1"><code>148be15</code></a>
  Remove unused Unix-only helpers from utils (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/148">#148</a>)</li>
  <li>See full diff in <a
  href="https://github.com/namespacelabs/nscloud-cache-action/compare/d6b68aa38adace8976c09629021052d57bb1ce9c...58bf6e08898e88803c098e2b522668541cd3b2e3">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=namespacelabs/nscloud-cache-action&package-manager=github_actions&previous-version=1.5.0&new-version=1.6.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## June 30, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/28454269522)  
Summary: 1 runs • 2 commits • 2 authors

### Changes

- [`5d47602`](https://github.com/ghostty-org/ghostty/commit/5d476024b4e9960802dd5772aa5f77bab5df2a76) build(deps): bump namespacelabs/nscloud-cache-action from 1.4.3 to 1.5.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [namespacelabs/nscloud-cache-action](https://github.com/namespacelabs/nscloud-cache-action) from 1.4.3 to 1.5.0.
  - [Release notes](https://github.com/namespacelabs/nscloud-cache-action/releases)
  - [Commits](https://github.com/namespacelabs/nscloud-cache-action/compare/15799a6b54e5765f85b2aac25b3f0df43ed571c0...d6b68aa38adace8976c09629021052d57bb1ce9c)
  
  ---
  updated-dependencies:
  - dependency-name: namespacelabs/nscloud-cache-action
    dependency-version: 1.5.0
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`0a50617`](https://github.com/ghostty-org/ghostty/commit/0a5061743d608a1b0349a3305a4136ff67600921) build(deps): bump namespacelabs/nscloud-cache-action from 1.4.3 to 1.5.0 ([#13120](https://github.com/ghostty-org/ghostty/issues/13120)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [namespacelabs/nscloud-cache-action](https://github.com/namespacelabs/nscloud-cache-action)
  from 1.4.3 to 1.5.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/namespacelabs/nscloud-cache-action/releases">namespacelabs/nscloud-cache-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v1.5.0</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>Bump pnpm/action-setup from 5.0.0 to 6.0.3 in the
  major-actions-dependencies group across 1 directory by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/127">namespacelabs/nscloud-cache-action#127</a></li>
  <li>Bump the minor-npm-dependencies group across 1 directory with 8
  updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/130">namespacelabs/nscloud-cache-action#130</a></li>
  <li>ci: add --verbose to cargo invocations by <a
  href="https://github.com/annervisser"><code>@​annervisser</code></a> in
  <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/117">namespacelabs/nscloud-cache-action#117</a></li>
  <li>Bump the minor-actions-dependencies group with 5 updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/133">namespacelabs/nscloud-cache-action#133</a></li>
  <li>Bump eslint-plugin-n from 17.24.0 to 18.0.1 by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/132">namespacelabs/nscloud-cache-action#132</a></li>
  <li>fix(ci): pin astral-sh/setup-uv to a valid v7 SHA by <a
  href="https://github.com/rcrowe"><code>@​rcrowe</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/134">namespacelabs/nscloud-cache-action#134</a></li>
  <li>ci: matrix pnpm versions to cover v11 by <a
  href="https://github.com/rcrowe"><code>@​rcrowe</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/131">namespacelabs/nscloud-cache-action#131</a></li>
  <li>Bump the major-actions-dependencies group across 1 directory with 2
  updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/142">namespacelabs/nscloud-cache-action#142</a></li>
  <li>Bump the minor-actions-dependencies group across 1 directory with 7
  updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/145">namespacelabs/nscloud-cache-action#145</a></li>
  <li>Bump the minor-npm-dependencies group across 1 directory with 9
  updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/144">namespacelabs/nscloud-cache-action#144</a></li>
  <li>Pass spacectl binPath explicitly instead of relying on PATH by <a
  href="https://github.com/rcrowe"><code>@​rcrowe</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/146">namespacelabs/nscloud-cache-action#146</a></li>
  <li>ci: add tuist cache mode test by <a
  href="https://github.com/rcrowe"><code>@​rcrowe</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/147">namespacelabs/nscloud-cache-action#147</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/namespacelabs/nscloud-cache-action/compare/v1...v1.5.0">https://github.com/namespacelabs/nscloud-cache-action/compare/v1...v1.5.0</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/d6b68aa38adace8976c09629021052d57bb1ce9c"><code>d6b68aa</code></a>
  ci: add tuist cache mode test (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/147">#147</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/aee11c4fe2689420e2ba4128c27a6e297217997c"><code>aee11c4</code></a>
  Pass spacectl binPath explicitly instead of relying on PATH (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/146">#146</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/4cfea58f960c4e6cbab9f11ce754c4933274642d"><code>4cfea58</code></a>
  Bump the minor-npm-dependencies group across 1 directory with 9 updates
  (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/144">#144</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/2d59ae229313b90908155bbad0758681ad61a0d8"><code>2d59ae2</code></a>
  Bump the minor-actions-dependencies group across 1 directory with 7
  updates (...</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/18c2caf2ae15a55cd922b6430072bf4dcb42653c"><code>18c2caf</code></a>
  Bump the major-actions-dependencies group across 1 directory with 2
  updates (...</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/709f7233c082f4e6834932395fe47810bc3bbc52"><code>709f723</code></a>
  ci: matrix pnpm versions to cover v11 (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/131">#131</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/34b9206dd6befcd25156541c21ecae4dd706db56"><code>34b9206</code></a>
  Bump eslint-plugin-n from 17.24.0 to 18.0.1 (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/132">#132</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/8004c8e3d292e880d4d2dd8b79e96a531b6466be"><code>8004c8e</code></a>
  fix(ci): pin astral-sh/setup-uv to valid v7.6.0 SHA (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/134">#134</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/0a5f069ee9873caaecdd04aa15a9b358c16b35bc"><code>0a5f069</code></a>
  Bump the minor-actions-dependencies group with 5 updates (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/133">#133</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/064bb70e4ad00eaf0b1384a443a76315612db876"><code>064bb70</code></a>
  ci: add --verbose to cargo invocations (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/117">#117</a>)</li>
  <li>Additional commits viewable in <a
  href="https://github.com/namespacelabs/nscloud-cache-action/compare/15799a6b54e5765f85b2aac25b3f0df43ed571c0...d6b68aa38adace8976c09629021052d57bb1ce9c">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=namespacelabs/nscloud-cache-action&package-manager=github_actions&previous-version=1.4.3&new-version=1.5.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## June 29, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/28395795571)  
Summary: 1 runs • 1 commits • 1 authors

### Changes

- [`28f9367`](https://github.com/ghostty-org/ghostty/commit/28f9367bee11ad42f40f8aa589eb8c6db62d34be) Update VOUCHED list ([#13119](https://github.com/ghostty-org/ghostty/issues/13119)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13118#discussioncomment-17475451)
  from @mitchellh.
  
  Vouch: @quinnypig
  ```

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

