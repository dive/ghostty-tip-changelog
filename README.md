> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: March 13, 2026 at 15:15 UTC.

## March 13, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23030892705)  
Summary: 1 runs • 2 commits • 2 authors

### Changes

- [`eccf960`](https://github.com/ghostty-org/ghostty/commit/eccf960def6f15dc33abaeff6f9b7ad3894db5dd) build(deps): bump dorny/paths-filter from 3.0.2 to 4.0.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [dorny/paths-filter](https://github.com/dorny/paths-filter) from 3.0.2 to 4.0.0.
  - [Release notes](https://github.com/dorny/paths-filter/releases)
  - [Changelog](https://github.com/dorny/paths-filter/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/dorny/paths-filter/compare/de90cc6fb38fc0963ad72b210f1f284cd68cea36...9d7afb8d214ad99e78fbd4247752c4caed2b6e4c)
  
  ---
  updated-dependencies:
  - dependency-name: dorny/paths-filter
    dependency-version: 4.0.0
    dependency-type: direct:production
    update-type: version-update:semver-major
  ...
  ```
- [`d4019fa`](https://github.com/ghostty-org/ghostty/commit/d4019fa484c821b8d3a1ef73d42357ae8d86f2b7) build(deps): bump dorny/paths-filter from 3.0.2 to 4.0.0 ([#11436](https://github.com/ghostty-org/ghostty/issues/11436)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps [dorny/paths-filter](https://github.com/dorny/paths-filter) from
  3.0.2 to 4.0.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/dorny/paths-filter/releases">dorny/paths-filter's
  releases</a>.</em></p>
  <blockquote>
  <h2>v4.0.0</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>feat: update action runtime to node24 by <a
  href="https://github.com/saschabratton"><code>@​saschabratton</code></a>
  in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/294">dorny/paths-filter#294</a></li>
  </ul>
  <h2>New Contributors</h2>
  <ul>
  <li><a
  href="https://github.com/saschabratton"><code>@​saschabratton</code></a>
  made their first contribution in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/294">dorny/paths-filter#294</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/dorny/paths-filter/compare/v3.0.3...v4.0.0">https://github.com/dorny/paths-filter/compare/v3.0.3...v4.0.0</a></p>
  <h2>v3.0.3</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>Add missing predicate-quantifier by <a
  href="https://github.com/wardpeet"><code>@​wardpeet</code></a> in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/279">dorny/paths-filter#279</a></li>
  </ul>
  <h2>New Contributors</h2>
  <ul>
  <li><a href="https://github.com/wardpeet"><code>@​wardpeet</code></a>
  made their first contribution in <a
  href="https://redirect.github.com/dorny/paths-filter/pull/279">dorny/paths-filter#279</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/dorny/paths-filter/compare/v3...v3.0.3">https://github.com/dorny/paths-filter/compare/v3...v3.0.3</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/dorny/paths-filter/blob/master/CHANGELOG.md">dorny/paths-filter's
  changelog</a>.</em></p>
  <blockquote>
  <h1>Changelog</h1>
  <h2>v4.0.0</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/294">Update
  action runtime to node24</a></li>
  </ul>
  <h2>v3.0.3</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/279">Add
  missing predicate-quantifier</a></li>
  </ul>
  <h2>v3.0.2</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/224">Add
  config parameter for predicate quantifier</a></li>
  </ul>
  <h2>v3.0.1</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/133">Compare
  base and ref when token is empty</a></li>
  </ul>
  <h2>v3.0.0</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/210">Update to
  Node.js 20</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/215">Update
  all dependencies</a></li>
  </ul>
  <h2>v2.11.1</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/167">Update
  <code>@​actions/core</code> to v1.10.0 - Fixes warning about deprecated
  set-output</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/168">Document
  need for pull-requests: read permission</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/164">Updating
  to actions/checkout@v3</a></li>
  </ul>
  <h2>v2.11.0</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/157">Set
  list-files input parameter as not required</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/161">Update
  Node.js</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/162">Fix
  incorrect handling of Unicode characters in exec()</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/163">Use
  Octokit pagination</a></li>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/160">Updates
  real world links</a></li>
  </ul>
  <h2>v2.10.2</h2>
  <ul>
  <li><a href="https://redirect.github.com/dorny/paths-filter/pull/91">Fix
  getLocalRef() returns wrong ref</a></li>
  </ul>
  <h2>v2.10.1</h2>
  <ul>
  <li><a
  href="https://redirect.github.com/dorny/paths-filter/pull/85">Improve
  robustness of change detection</a></li>
  </ul>
  <h2>v2.10.0</h2>
  <ul>
  <li><a href="https://redirect.github.com/dorny/paths-filter/pull/82">Add
  ref input parameter</a></li>
  <li><a href="https://redirect.github.com/dorny/paths-filter/pull/83">Fix
  change detection in PR when pullRequest.changed_files is
  incorrect</a></li>
  </ul>
  <h2>v2.9.3</h2>
  <ul>
  <li><a href="https://redirect.github.com/dorny/paths-filter/pull/78">Fix
  change detection when base is a tag</a></li>
  </ul>
  <h2>v2.9.2</h2>
  <ul>
  <li><a href="https://redirect.github.com/dorny/paths-filter/pull/75">Fix
  fetching git history</a></li>
  </ul>
  <h2>v2.9.1</h2>
  <ul>
  <li><a href="https://redirect.github.com/dorny/paths-filter/pull/74">Fix
  fetching git history + fallback to unshallow repo</a></li>
  </ul>
  <h2>v2.9.0</h2>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/9d7afb8d214ad99e78fbd4247752c4caed2b6e4c"><code>9d7afb8</code></a>
  Update CHANGELOG for v4.0.0</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/782470c5d953cae2693d643172b14e01bacb71f3"><code>782470c</code></a>
  Merge branch 'releases/v3'</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/d1c1ffe0248fe513906c8e24db8ea791d46f8590"><code>d1c1ffe</code></a>
  Update CHANGELOG for v3.0.3</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/ce10459c8b92cd8901166c0a222fbb033ef39365"><code>ce10459</code></a>
  Merge pull request <a
  href="https://redirect.github.com/dorny/paths-filter/issues/294">#294</a>
  from saschabratton/master</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/5f40380c5482e806c81cec080f5192e7234d8fe9"><code>5f40380</code></a>
  feat: update action runtime to node24</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/668c092af3649c4b664c54e4b704aa46782f6f7c"><code>668c092</code></a>
  Merge pull request <a
  href="https://redirect.github.com/dorny/paths-filter/issues/279">#279</a>
  from wardpeet/patch-1</li>
  <li><a
  href="https://github.com/dorny/paths-filter/commit/209e61402dbca8aa44f967535da6666b284025ed"><code>209e614</code></a>
  Add missing predicate-quantifier</li>
  <li>See full diff in <a
  href="https://github.com/dorny/paths-filter/compare/de90cc6fb38fc0963ad72b210f1f284cd68cea36...9d7afb8d214ad99e78fbd4247752c4caed2b6e4c">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=dorny/paths-filter&package-manager=github_actions&previous-version=3.0.2&new-version=4.0.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## March 12, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23023692641), [2](https://github.com/ghostty-org/ghostty/actions/runs/23020014641), [3](https://github.com/ghostty-org/ghostty/actions/runs/23016405050), [4](https://github.com/ghostty-org/ghostty/actions/runs/23012255263), [5](https://github.com/ghostty-org/ghostty/actions/runs/23006959585), [6](https://github.com/ghostty-org/ghostty/actions/runs/22985944795), [7](https://github.com/ghostty-org/ghostty/actions/runs/22984951308)  
Summary: 7 runs • 23 commits • 5 authors

### Changes

- [`64331b8`](https://github.com/ghostty-org/ghostty/commit/64331b8c35e2a39a9296594f9e6b096c54a8b49f) snap: Don't leak LD_LIBRARY_PATH set by the snap launcher ([@kenvandine](https://github.com/kenvandine))
- [`174aae3`](https://github.com/ghostty-org/ghostty/commit/174aae359d86c71be7bbe75f6c93166214fc4b1f) snap: Don't leak LD_LIBRARY_PATH set by the snap launcher ([#11431](https://github.com/ghostty-org/ghostty/issues/11431)) ([@kenvandine](https://github.com/kenvandine))
  ```text
  LD_LIBRARY_PATH was being leaked which could break some apps launched
  from ghostty, such as opening configuration in a text editor.
  ```
- [`d6d6fe4`](https://github.com/ghostty-org/ghostty/commit/d6d6fe4e5800f48846815a6cb2401c495e9ca57c) macOS: update window cascading ([@bo2themax](https://github.com/bo2themax))
  ```text
  Make it smaller and add comparisons between y values
  ```
- [`3022aa0`](https://github.com/ghostty-org/ghostty/commit/3022aa05ea82296adb598d340735f8339f5bf753) macOS: add test cases for drag-split ([@bo2themax](https://github.com/bo2themax))
- [`07bc888`](https://github.com/ghostty-org/ghostty/commit/07bc8886822bdc19932efea54e6d01bd230078cc) macOS: fix window position when dragging split into a new window ([@bo2themax](https://github.com/bo2themax))
- [`5c51603`](https://github.com/ghostty-org/ghostty/commit/5c51603b0b82a33c7461384e27ee67edbf3818fd) chore: make ci happy ([@bo2themax](https://github.com/bo2themax))
- [`597e8cf`](https://github.com/ghostty-org/ghostty/commit/597e8cf1c592d23fa8e69f64d1f43a20c44726ef) macOS: fix window position when dragging split into a new window ([#11429](https://github.com/ghostty-org/ghostty/issues/11429)) ([@mitchellh](https://github.com/mitchellh))
- [`77c2acf`](https://github.com/ghostty-org/ghostty/commit/77c2acf843e49c9566128fd2381a667077e4f2f8) macOS: add test case for window cascading without moving the window ([@bo2themax](https://github.com/bo2themax))
- [`ea262cd`](https://github.com/ghostty-org/ghostty/commit/ea262cdd34c36ac848ddd417cdf29a4dc93d7fb6) macOS: fix window cascading for 3rd+ window ([@bo2themax](https://github.com/bo2themax))
- [`5e38663`](https://github.com/ghostty-org/ghostty/commit/5e3866381b321bbc936f5de18e9f2b9622e0af4c) macOS: fix window cascading for the second window ([@bo2themax](https://github.com/bo2themax))
- [`a91e747`](https://github.com/ghostty-org/ghostty/commit/a91e747cb187dc143054b5c17ed2451d19422ef1) macOS: fix window cascading ([#11426](https://github.com/ghostty-org/ghostty/issues/11426)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Added test case for cascading **without moving previous window**, #11161
  will follow up for more accurate cascading after this.
  
  Fixed window cascading after last pr, now we should perform cascading
  **after** showing the window.
  ```
- [`c399812`](https://github.com/ghostty-org/ghostty/commit/c399812036a3161a7c2cf3b7dc63f4240949c607) macOS: add test case for positioning the very first window ([@bo2themax](https://github.com/bo2themax))
- [`4f849a1`](https://github.com/ghostty-org/ghostty/commit/4f849a15124b64dab955a489b77a80388b595523) macOS: fix window position for the very first window ([@bo2themax](https://github.com/bo2themax))
- [`08107d3`](https://github.com/ghostty-org/ghostty/commit/08107d342a1404ea095e48b0ee7fcc5299c2024f) macOS: we don't need initialFrame anymore ([@bo2themax](https://github.com/bo2themax))
- [`7068573`](https://github.com/ghostty-org/ghostty/commit/70685733c5947bdef9c8c7074419d0b15be86812) macOS: fix window position for the very first window ([#11421](https://github.com/ghostty-org/ghostty/issues/11421)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Depends on https://github.com/ghostty-org/ghostty/pull/11417
  
  Moved positioning part from `windowDidLoad` to `showWindow` to make new
  users happy. Also deleted `initialFrame`, since we don't need it
  anymore.
  ```
- [`d6dfaf2`](https://github.com/ghostty-org/ghostty/commit/d6dfaf28feb8e30834f18f987d1b909a3452e9fc) macOS: support injecting temporary defaults when testing ([@bo2themax](https://github.com/bo2themax))
- [`8dde340`](https://github.com/ghostty-org/ghostty/commit/8dde340f88d87bf1fa83cbbd312cf7962eaf284b) macOS: support injecting temporary defaults when testing ([#11417](https://github.com/ghostty-org/ghostty/issues/11417)) ([@mitchellh](https://github.com/mitchellh))
- [`84d48d1`](https://github.com/ghostty-org/ghostty/commit/84d48d1c6a9d4fb93eccd31cf0a731adbe174d02) config: add progress-style option ([@MOlechowski](https://github.com/MOlechowski))
  ```text
  Add option to disable OSC 9;4 ConEmu progress bars via config.
  
  Fixes #11241
  ```
- [`ab269e2`](https://github.com/ghostty-org/ghostty/commit/ab269e2c79d1540cd6d5aea74562ea4634c0104a) config: add progress-style option ([#11289](https://github.com/ghostty-org/ghostty/issues/11289)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Adds progress-style config to control OSC 9;4 progress bar visibility.
  Defaults to true, set false to hide.
  
  Fixes #11241
  
  AI Disclosure: Claude Code (Opus 4.6) used for codebase exploration,
  code review, and testing assistance. All code written and reviewed by
  hand.
  ```
- [`16ca952`](https://github.com/ghostty-org/ghostty/commit/16ca9527e95ea857a5cc6a30685bfcf58705af08) build(deps): bump actions/download-artifact from 8.0.0 to 8.0.1 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [actions/download-artifact](https://github.com/actions/download-artifact) from 8.0.0 to 8.0.1.
  - [Release notes](https://github.com/actions/download-artifact/releases)
  - [Commits](https://github.com/actions/download-artifact/compare/70fc10c6e5e1ce46ad2ea6f2b72d43f7d47b13c3...3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c)
  
  ---
  updated-dependencies:
  - dependency-name: actions/download-artifact
    dependency-version: 8.0.1
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`8093695`](https://github.com/ghostty-org/ghostty/commit/809369505534b40c83560f9cd0cbee8e7ecb7516) macos: only run key equivalents for Ghostty-owned menu items ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11396
  
  Track menu items populated from Ghostty keybind actions and only trigger
  those from SurfaceView performKeyEquivalent. This avoids app-default
  shortcuts such as Hide from pre-empting explicit keybinds.
  ```
- [`8392255`](https://github.com/ghostty-org/ghostty/commit/8392255fd6ed12dd5aad87eae0357ab6e69ec4a0) build(deps): bump actions/download-artifact from 8.0.0 to 8.0.1 ([#11399](https://github.com/ghostty-org/ghostty/issues/11399)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [actions/download-artifact](https://github.com/actions/download-artifact)
  from 8.0.0 to 8.0.1.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/actions/download-artifact/releases">actions/download-artifact's
  releases</a>.</em></p>
  <blockquote>
  <h2>v8.0.1</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>Support for CJK characters in the artifact name by <a
  href="https://github.com/danwkennedy"><code>@​danwkennedy</code></a> in
  <a
  href="https://redirect.github.com/actions/download-artifact/pull/471">actions/download-artifact#471</a></li>
  <li>Add a regression test for artifact name + content-type mismatches by
  <a href="https://github.com/danwkennedy"><code>@​danwkennedy</code></a>
  in <a
  href="https://redirect.github.com/actions/download-artifact/pull/472">actions/download-artifact#472</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/actions/download-artifact/compare/v8...v8.0.1">https://github.com/actions/download-artifact/compare/v8...v8.0.1</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/actions/download-artifact/commit/3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c"><code>3e5f45b</code></a>
  Add regression tests for CJK characters (<a
  href="https://redirect.github.com/actions/download-artifact/issues/471">#471</a>)</li>
  <li><a
  href="https://github.com/actions/download-artifact/commit/e6d03f67377d4412c7aa56a8e2e4988e6ec479dd"><code>e6d03f6</code></a>
  Add a regression test for artifact name + content-type mismatches (<a
  href="https://redirect.github.com/actions/download-artifact/issues/472">#472</a>)</li>
  <li>See full diff in <a
  href="https://github.com/actions/download-artifact/compare/70fc10c6e5e1ce46ad2ea6f2b72d43f7d47b13c3...3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=actions/download-artifact&package-manager=github_actions&previous-version=8.0.0&new-version=8.0.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`35f4d18`](https://github.com/ghostty-org/ghostty/commit/35f4d1880290d7f882f6f00fbafb46a49196e014) macos: only run key equivalents for Ghostty-owned menu items ([#11403](https://github.com/ghostty-org/ghostty/issues/11403)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11396
  
  Track menu items populated from Ghostty keybind actions and only trigger
  those from SurfaceView performKeyEquivalent. This avoids app-default
  shortcuts such as Hide from pre-empting explicit keybinds.
  ```

## March 11, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22970467471), [2](https://github.com/ghostty-org/ghostty/actions/runs/22967683770), [3](https://github.com/ghostty-org/ghostty/actions/runs/22964898207), [4](https://github.com/ghostty-org/ghostty/actions/runs/22964025677), [5](https://github.com/ghostty-org/ghostty/actions/runs/22963156248), [6](https://github.com/ghostty-org/ghostty/actions/runs/22961429369), [7](https://github.com/ghostty-org/ghostty/actions/runs/22957941413), [8](https://github.com/ghostty-org/ghostty/actions/runs/22945785511), [9](https://github.com/ghostty-org/ghostty/actions/runs/22945215801), [10](https://github.com/ghostty-org/ghostty/actions/runs/22942691693), [11](https://github.com/ghostty-org/ghostty/actions/runs/22934741901), [12](https://github.com/ghostty-org/ghostty/actions/runs/22934034203)  
Summary: 12 runs • 38 commits • 10 authors

### Changes

- [`0f745b5`](https://github.com/ghostty-org/ghostty/commit/0f745b56730ae0eff4de2e40e959d432cbdcb004) Update VOUCHED list ([#11389](https://github.com/ghostty-org/ghostty/issues/11389)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11388#discussioncomment-16087905)
  from @jcollie.
  
  Vouch: @wyounas
  ```
- [`fe98f38`](https://github.com/ghostty-org/ghostty/commit/fe98f3884d7dd72f0988949ab661beb018a191b4) macos: only show split grab handle when the mouse is near it ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11379
  
  For this pass, I made it a very simple "within 20%" (height-wise) of the
  split handle. There is no horizontal component. I want to find the right
  balance between always visible (today mostly) to only visible on direct
  hover, because I think it'll be too hard to discover on that far right
  side.
  ```
- [`a0d3566`](https://github.com/ghostty-org/ghostty/commit/a0d3566872c3bca4a139be3a49aaa9944040f95c) macos: only show split grab handle when the mouse is near it ([#11383](https://github.com/ghostty-org/ghostty/issues/11383)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11379
  
  For this pass, I made it a very simple "within 20%" (height-wise) of the
  split handle down. There is no horizontal component. I want to find the
  right balance between always visible (today mostly) to only visible on
  direct hover, because I think it'll be too hard to discover on that far
  right side.
  ```
- [`9503fa0`](https://github.com/ghostty-org/ghostty/commit/9503fa0786d3e79a5862361ae59db6d5972b4eae) nix: bump zig-overlay version ([@faukah](https://github.com/faukah))
- [`0af9938`](https://github.com/ghostty-org/ghostty/commit/0af9938ad2f2fb84d8e00501716933029bc0ba65) macos: add UI test for window position restore across titlebar styles ([@bo2themax](https://github.com/bo2themax))
  ```text
  Tests that window position and size are correctly restored after
  reopen for all four macos-titlebar-style variants.
  ```
- [`e8c82ca`](https://github.com/ghostty-org/ghostty/commit/e8c82ca1af29a8e911f328abe89bcc2650ec1705) macOS: save frame only if the window is visible ([@bo2themax](https://github.com/bo2themax))
- [`45d360d`](https://github.com/ghostty-org/ghostty/commit/45d360dc6879a80ca55f6f01ea36d9161732e099) macOS: set the initial window position after window is loaded ([@bo2themax](https://github.com/bo2themax))
- [`596d502`](https://github.com/ghostty-org/ghostty/commit/596d502a756ce6454093b5d0782bc17d700804ab) macOS: restore window frame under certain conditions ([@bo2themax](https://github.com/bo2themax))
- [`e31615d`](https://github.com/ghostty-org/ghostty/commit/e31615d00bf3811bdba4ae697c80fcb1ede3817a) bash: fix extra newlines with readline vi mode indicator ([@jparise](https://github.com/jparise))
  ```text
  Use OSC 133;P (prompt mark) instead of 133;A (fresh line + prompt mark)
  inside PS1 and PS2. Readline redraws the prompt on vi mode switches,
  Ctrl-L, and other events, and 133;A's fresh-line behavior would emit a
  CR+LF whenever the cursor wasn't at column 0, causing visible extra
  newlines.
  
  The one-time 133;A is now emitted via printf in __ghostty_precmd, which
  only runs once per prompt cycle via PROMPT_COMMAND. On SIGWINCH, bash
  redraws PS1 (firing the 133;P marks) but doesn't re-run PROMPT_COMMAND,
  so there's no unwanted fresh-line on resize either. The redraw=last flag
  persists from the initial printf.
  
  This is a little less optimal than our previous approach, in terms of
  number of prompt marks we emit, but it produces an overall more correct
  result, which is the important thing.
  
  Because readline prints its output outside the scope of PS1, those
  characters "inherit" the surrounded prompt scope. This is usually fine,
  but it can sometimes get out of sync (especially during redraws). This
  is inherently a limitation of the fact that it's a separate output
  channel, so we just have to accept that can happen.
  
  See: #11267
  ```
- [`7aff470`](https://github.com/ghostty-org/ghostty/commit/7aff470ceb220fbf58fd7e76cc7e342c7011d629) bash: fix extra newlines with readline vi mode indicator ([#11377](https://github.com/ghostty-org/ghostty/issues/11377)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Use OSC 133;P (prompt mark) instead of 133;A (fresh line + prompt mark)
  inside PS1 and PS2. Readline redraws the prompt on vi mode switches,
  Ctrl-L, and other events, and 133;A's fresh-line behavior would emit a
  CR+LF whenever the cursor wasn't at column 0, causing visible extra
  newlines.
  
  The one-time 133;A is now emitted via printf in __ghostty_precmd, which
  only runs once per prompt cycle via PROMPT_COMMAND. On SIGWINCH, bash
  redraws PS1 (firing the 133;P marks) but doesn't re-run PROMPT_COMMAND,
  so there's no unwanted fresh-line on resize either. The redraw=last flag
  persists from the initial printf.
  
  This is a little less optimal than our previous approach, in terms of
  number of prompt marks we emit, but it produces an overall more correct
  result, which is the important thing.
  
  Because readline prints its output outside the scope of PS1, those
  characters "inherit" the surrounded prompt scope. This is usually fine,
  but it can sometimes get out of sync (especially during redraws). This
  is inherently a limitation of the fact that it's a separate output
  channel, so we just have to accept that can happen.
  
  Fixes: #10953
  See: #11267
  ```
- [`12bc1e7`](https://github.com/ghostty-org/ghostty/commit/12bc1e786052a31d6f50cdbb0a703b45371a182d) macos: only show the grab handle in fullscreen if there are splits ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11376
  ```
- [`2296a82`](https://github.com/ghostty-org/ghostty/commit/2296a82c13f3621f25c2a5bb78280a80ac6c56b8) macOS: fix window frame when (re)opening new window ([#11380](https://github.com/ghostty-org/ghostty/issues/11380)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Claude wrote the fail path in the UI tests, or you can easily reproduce
  this manually. This is kinda a regression after #11322, since we are not
  delaying the frame update anymore, which exposes some of the "flaws" of
  the previous implementation.
  
  The following three commits fix this step by step:
  - We shouldn't save intermediate frames when the window is loading,
  which is triggered by `windowDidResize` and `windowDidMove` during the
  process.
  - We should set the initial position (from the config) after the window
  is loaded.
  - A small refactor on `LastWindowPosition` to support restoring the
  window frame under certain conditions.
  
  
  https://github.com/user-attachments/assets/6f90f9a5-653d-4146-95c6-8e5c69bda656
  
  
  
  ### AI Disclosure
  
  Claude helped me write the UI tests.
  ```
- [`19e5053`](https://github.com/ghostty-org/ghostty/commit/19e5053b28c524317c77d482a65b68f56fe372a4) macos: only show the grab handle in fullscreen if there are splits ([#11381](https://github.com/ghostty-org/ghostty/issues/11381)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11376
  ```
- [`36c1450`](https://github.com/ghostty-org/ghostty/commit/36c1450dc950c67e9acb008dd778d4ad813835df) nix: bump zig-overlay version ([#11375](https://github.com/ghostty-org/ghostty/issues/11375)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bump of `zig-overlay`, allowing us to drop flake-utils from the flake
  inputs. :)
  ```
- [`86c2a2e`](https://github.com/ghostty-org/ghostty/commit/86c2a2e87faa5996ac856c65718c0765be3fa3d0) input: add direct set_surface_title and set_tab_title actions ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11316
  
  This mirrors the `prompt` actions (hence why there is no window action
  here) and enables setting titles via keybind actions which importantly
  lets this work via command palettes, App Intents, AppleScript, etc.
  ```
- [`8ad9ec8`](https://github.com/ghostty-org/ghostty/commit/8ad9ec8e8806af12534080a38decc73322c877fe) add direct set_surface_title and set_tab_title actions ([#11373](https://github.com/ghostty-org/ghostty/issues/11373)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11316
  
  This mirrors the `prompt` actions (hence why there is no window action
  here) and enables setting titles via keybind actions which importantly
  lets this work via command palettes, App Intents, AppleScript, etc.
  ```
- [`f571c80`](https://github.com/ghostty-org/ghostty/commit/f571c806fec71a7de5b5ca0afc35eed92fa3cf9f) ci: skip vouched PRs for milestone attachment ([@mitchellh](https://github.com/mitchellh))
- [`d48b6ba`](https://github.com/ghostty-org/ghostty/commit/d48b6ba085eb96d2253e8a7f00c12e942a362a54) ci: skip vouched PRs for milestone attachment ([#11371](https://github.com/ghostty-org/ghostty/issues/11371)) ([@mitchellh](https://github.com/mitchellh))
- [`a8d38fe`](https://github.com/ghostty-org/ghostty/commit/a8d38fe5d807e8cf18f99dcef117355d02048d7c) Update VOUCHED list ([#11374](https://github.com/ghostty-org/ghostty/issues/11374)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11372#discussioncomment-16086042)
  from @mitchellh.
  
  Vouch: @faukah
  ```
- [`26d8bd9`](https://github.com/ghostty-org/ghostty/commit/26d8bd9e71c27f1f7f31a1079bee3ca79e79b205) bash: fix multiline PS1 with command substitutions ([@jparise](https://github.com/jparise))
  ```text
  Only replace the \n prompt escape when inserting secondary prompt marks,
  not literal newlines ($'\n'). Literal newlines may appear inside $(...)
  or `...` command substitutions, and inserting escape sequences there
  breaks the shell syntax. For example:
  
        PS1='$(if [ $? -eq 0 ]; then echo -e "P";
                      else echo -e "F";
                      fi) $ '
  
  The literal newlines between the if/else/fi are part of the shell syntax
  inside the command substitution. The previous code replaced all literal
  newlines in PS1 with newline + OSC 133 escape sequences, which injected
  terminal escapes into the middle of the command substitution and caused
  bash to report a syntax error when evaluating it.
  
  The \n prompt escape is PS1-specific and safe to replace globally. This
  means prompts using literal newlines for line breaks (rather than \n)
  won't get per-line secondary marks, but this is the conventional form
  and avoids the need for complex shell parsing.
  
  Fixes: #11267
  ```
- [`660767c`](https://github.com/ghostty-org/ghostty/commit/660767c77d077c1b7cef441fc2fa44f7dd666b08) bash: fix multiline PS1 with command substitutions ([#11369](https://github.com/ghostty-org/ghostty/issues/11369)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Only replace the \n prompt escape when inserting secondary prompt marks,
  not literal newlines `($'\n')`. Literal newlines may appear inside
  `$(...)` or `...` command substitutions, and inserting escape sequences
  there breaks the shell syntax. For example:
  
        PS1='$(if [ $? -eq 0 ]; then echo -e "P";
                      else echo -e "F";
                      fi) $ '
  
  The literal newlines between the if/else/fi are part of the shell syntax
  inside the command substitution. The previous code replaced all literal
  newlines in PS1 with newline + OSC 133 escape sequences, which injected
  terminal escapes into the middle of the command substitution and caused
  bash to report a syntax error when evaluating it.
  
  The \n prompt escape is PS1-specific and safe to replace globally. This
  means prompts using literal newlines for line breaks (rather than \n)
  won't get per-line secondary marks, but this is the conventional form
  and avoids the need for complex shell parsing.
  
  Fixes: #11267
  ```
- [`23f3cd5`](https://github.com/ghostty-org/ghostty/commit/23f3cd5f101fedcff6350648f8ba3993e6c55d90) zsh: improve prompt marking with dynamic themes ([@jparise](https://github.com/jparise))
  ```text
  Replace the strip-in-preexec / re-add-in-precmd pattern for OSC 133
  marks with a save/restore approach. Instead of pattern-matching marks
  out of PS1 (which exposes PS1 in intermediate states to other hooks), we
  save the original PS1/PS2 before adding marks and then restore them.
  
  This also adds dynamic theme detection: if PS1 changed between cycles
  (e.g., a theme rebuilt it), we skip injecting continuation marks into
  newlines. This prevents breaking plugins like Pure that use pattern
  matching to strip/rebuild the prompt.
  
  Additionally, move _ghostty_precmd to the end of precmd_functions in
  _ghostty_deferred_init (instead of substituting in-place) so that the
  first prompt is properly marked even when other hooks were appended
  after our auto-injection.
  
  There's one scenario that we still don't complete cover:
  
      precmd_functions+=(_test_overwrite_ps1)
      _test_overwrite_ps1() {
          PS1="test> "
      }
  
  ... which results in the first prompt not printing its prompt marks
  because _test_overwrite_ps1 becomes the last thing to run, overwriting
  our marks, but this will be fixed for subsequent prompts when we move
  our handler back to the last index.
  
  Fixes: #11282
  ```
- [`87e496b`](https://github.com/ghostty-org/ghostty/commit/87e496b30ff62a08e6dbdea651d86ea18b50493a) Update VOUCHED list ([#11368](https://github.com/ghostty-org/ghostty/issues/11368)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11365#issuecomment-4039534706)
  from @mitchellh.
  
  Vouch: @ydah
  ```
- [`c220654`](https://github.com/ghostty-org/ghostty/commit/c2206542d3bcb1b88eb4196620e553dad0717ca4) macos: fix tab title rename hit testing and focus handling in fullscreen mode ([@ydah](https://github.com/ydah))
- [`048a2d0`](https://github.com/ghostty-org/ghostty/commit/048a2d043a84eca4e67345eab2cdacb1a6390a70) Merge fix-fullscreen-tab-title-rename-hit into main ([@mitchellh](https://github.com/mitchellh))
- [`61865bc`](https://github.com/ghostty-org/ghostty/commit/61865bc37facf68056c4d0545a1dc4829550a8c1) zsh: improve prompt marking with dynamic themes ([#11367](https://github.com/ghostty-org/ghostty/issues/11367)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Replace the strip-in-preexec / re-add-in-precmd pattern for OSC 133
  marks with a save/restore approach. Instead of pattern-matching marks
  out of PS1 (which exposes PS1 in intermediate states to other hooks), we
  save the original PS1/PS2 before adding marks and then restore them.
  
  This also adds dynamic theme detection: if PS1 changed between cycles
  (e.g., a theme rebuilt it), we skip injecting continuation marks into
  newlines. This prevents breaking plugins like Pure that use pattern
  matching to strip/rebuild the prompt.
  
  Additionally, move _ghostty_precmd to the end of precmd_functions in
  _ghostty_deferred_init (instead of substituting in-place) so that the
  first prompt is properly marked even when other hooks were appended
  after our auto-injection.
  
  There's one scenario that we still don't complete cover:
  
      precmd_functions+=(_test_overwrite_ps1)
      _test_overwrite_ps1() {
          PS1="test> "
      }
  
  ... which results in the first prompt not printing its prompt marks
  because _test_overwrite_ps1 becomes the last thing to run, overwriting
  our marks, but this will be fixed for subsequent prompts when we move
  our handler back to the last index.
  
  Fixes: #11282
  ```
- [`ad6d366`](https://github.com/ghostty-org/ghostty/commit/ad6d3665c29b7e2db4da7e2a5fe67239d0f3df32) gtk: fix +new-window `--working-directory` inferrence. ([@jcollie](https://github.com/jcollie))
  ```text
  If the CLI argument `--working-directory` is not used with
  `+new-window`, the current working directory that `ghostty +new-window`
  is run from will be appended to the list of configuration data sent
  to the main Ghostty process. If `-e` _was_ used on the CLI, the
  `--working-directory` that was appended will be interpreted as part of
  the command to be executed, likely causing it to fail.
  
  Instead, insert `--working-directory` at the beginning of the list of
  configuration that it sent to the main Ghostty process.
  
  Fixes #11356
  ```
- [`76e9ee7`](https://github.com/ghostty-org/ghostty/commit/76e9ee7d376445a04421a7a78f5cc3e4787bcad4) gtk: fix +new-window `--working-directory` inferrence. ([#11357](https://github.com/ghostty-org/ghostty/issues/11357)) ([@pluiedev](https://github.com/pluiedev))
- [`82a8052`](https://github.com/ghostty-org/ghostty/commit/82a805296c3b45235571ecfa3b75821d9ca264b5) docs: fix backtick rendering in selection-word-chars default value ([@puzza007](https://github.com/puzza007))
  ```text
  The default value contains a literal backtick which broke inline code
  rendering on the website. Use double backtick delimiters to properly
  contain it.
  ```
- [`b992b66`](https://github.com/ghostty-org/ghostty/commit/b992b6605033d888c1c1afcf8015a6bf8cb9e7a5) docs: fix backtick rendering in selection-word-chars default value ([#11361](https://github.com/ghostty-org/ghostty/issues/11361)) ([@pluiedev](https://github.com/pluiedev))
- [`a644fca`](https://github.com/ghostty-org/ghostty/commit/a644fca5c5e74850312f13ed69f9677556abcd27) Update VOUCHED list ([#11360](https://github.com/ghostty-org/ghostty/issues/11360)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11358#discussioncomment-16080010)
  from @jcollie.
  
  Vouch: @puzza007
  ```
- [`6dd5b85`](https://github.com/ghostty-org/ghostty/commit/6dd5b856b05fbcb76f415ad18fbdfac600c3abde) macos: disable Tahoe one-time codes ([@mitchellh](https://github.com/mitchellh))
  ```text
  This disables all the automatic one-time code inputs in Ghostty.
  It'd be really neat to actually dynamically change this (not sure if its
  possible with NSTextContext or how often thats cached) but for now we
  should just fully disable it.
  ```
- [`dc18b25`](https://github.com/ghostty-org/ghostty/commit/dc18b25f86f59c79055ece87e158a5b27f625b05) macos: disable Tahoe one-time codes ([#11351](https://github.com/ghostty-org/ghostty/issues/11351)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This disables all the automatic one-time code inputs in Ghostty. It'd be
  really neat to actually dynamically change this (not sure if it's
  possible with NSTextContext or how often thats cached) but for now we
  should just fully disable it.
  
  Thanks to Ricky Mondello for the heads up on this.
  ```
- [`3293444`](https://github.com/ghostty-org/ghostty/commit/32934445cfb60e387013f4a7c4293352ac3aae44) macos: add TemporaryConfig for AI to write test cases ([@bo2themax](https://github.com/bo2themax))
- [`90dc431`](https://github.com/ghostty-org/ghostty/commit/90dc4315e2632faeb9771536cf526c46d33fc539) macos: add test cases for Ghostty.Config properties ([@bo2themax](https://github.com/bo2themax))
  ```text
  Test boolean, string, enum, and numeric config properties using
  TemporaryConfig to verify defaults and parsed values.
  ```
- [`85bec80`](https://github.com/ghostty-org/ghostty/commit/85bec8033474438182fbb33ded8dfcdcb009ea6a) build(deps): bump cachix/install-nix-action from 31.10.0 to 31.10.1 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [cachix/install-nix-action](https://github.com/cachix/install-nix-action) from 31.10.0 to 31.10.1.
  - [Release notes](https://github.com/cachix/install-nix-action/releases)
  - [Changelog](https://github.com/cachix/install-nix-action/blob/master/RELEASE.md)
  - [Commits](https://github.com/cachix/install-nix-action/compare/19effe9fe722874e6d46dd7182e4b8b7a43c4a99...1ca7d21a94afc7c957383a2d217460d980de4934)
  
  ---
  updated-dependencies:
  - dependency-name: cachix/install-nix-action
    dependency-version: 31.10.1
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`d5dab55`](https://github.com/ghostty-org/ghostty/commit/d5dab554aae398cc4b83c24d93bec20eaccbc5d9) build(deps): bump cachix/install-nix-action from 31.10.0 to 31.10.1 ([#11347](https://github.com/ghostty-org/ghostty/issues/11347)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [cachix/install-nix-action](https://github.com/cachix/install-nix-action)
  from 31.10.0 to 31.10.1.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/cachix/install-nix-action/releases">cachix/install-nix-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v31.10.1</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>nix: 2.34.0 -&gt; 2.34.1 by <a
  href="https://github.com/github-actions"><code>@​github-actions</code></a>[bot]
  in <a
  href="https://redirect.github.com/cachix/install-nix-action/pull/269">cachix/install-nix-action#269</a>
  Fixes a bug introduced in 2.34.0 that made the Nix daemon fail to load
  authentication keys configured by <code>cachix-action</code>.</li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/cachix/install-nix-action/compare/v31.10.0...v31.10.1">https://github.com/cachix/install-nix-action/compare/v31.10.0...v31.10.1</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/1ca7d21a94afc7c957383a2d217460d980de4934"><code>1ca7d21</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/install-nix-action/issues/269">#269</a>
  from cachix/create-pull-request/patch</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/b6137343272cafad497671822066f2a10ded6fef"><code>b613734</code></a>
  nix: 2.34.0 -&gt; 2.34.1</li>
  <li>See full diff in <a
  href="https://github.com/cachix/install-nix-action/compare/19effe9fe722874e6d46dd7182e4b8b7a43c4a99...1ca7d21a94afc7c957383a2d217460d980de4934">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=cachix/install-nix-action&package-manager=github_actions&previous-version=31.10.0&new-version=31.10.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`2a170b5`](https://github.com/ghostty-org/ghostty/commit/2a170b50c3ec088910645894f2d2e958ec381b42) macos: add test cases for Ghostty.Config properties ([#11263](https://github.com/ghostty-org/ghostty/issues/11263)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ### AI Disclosure
  
  Test cases is written using the Claude Agent in Xcode
  ```

## March 10, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22929804807), [2](https://github.com/ghostty-org/ghostty/actions/runs/22928895181), [3](https://github.com/ghostty-org/ghostty/actions/runs/22926107536), [4](https://github.com/ghostty-org/ghostty/actions/runs/22919665780), [5](https://github.com/ghostty-org/ghostty/actions/runs/22918391292), [6](https://github.com/ghostty-org/ghostty/actions/runs/22917096976), [7](https://github.com/ghostty-org/ghostty/actions/runs/22916232794), [8](https://github.com/ghostty-org/ghostty/actions/runs/22914796222), [9](https://github.com/ghostty-org/ghostty/actions/runs/22913587645), [10](https://github.com/ghostty-org/ghostty/actions/runs/22911767766), [11](https://github.com/ghostty-org/ghostty/actions/runs/22906920447), [12](https://github.com/ghostty-org/ghostty/actions/runs/22906644160), [13](https://github.com/ghostty-org/ghostty/actions/runs/22906186474)  
Summary: 13 runs • 33 commits • 7 authors

### Changes

- [`f9862cd`](https://github.com/ghostty-org/ghostty/commit/f9862cd4e27daf72e8e983646451a0954a47258b) GTK does support scrollbars ([@hulet](https://github.com/hulet))
- [`818e170`](https://github.com/ghostty-org/ghostty/commit/818e170ec0a16b501a78adc5ea9e197e142e877b) GTK does support scrollbars ([#11345](https://github.com/ghostty-org/ghostty/issues/11345)) ([@jcollie](https://github.com/jcollie))
  ```text
  Native GTK scrollbars are supported in 1.3.0:
  https://ghostty.org/docs/install/release-notes/1-3-0#scrollbars
  ```
- [`615af97`](https://github.com/ghostty-org/ghostty/commit/615af975f3365ea85594be7ebbc6ae90cac9558c) Update VOUCHED list ([#11344](https://github.com/ghostty-org/ghostty/issues/11344)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11343#discussioncomment-16075282)
  from @jcollie.
  
  Vouch: @hulet
  ```
- [`04d5efc`](https://github.com/ghostty-org/ghostty/commit/04d5efc8eb7b5f660bf44c0b63b9366c881e9635) config: working-directory expands ~/ prefix ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11336
  
  Introduce a proper WorkingDirectory tagged union type with home, inherit,
  and path variants. The field is now an optional (?WorkingDirectory) where
  null represents "use platform default" which is resolved during Config.finalize
  to .inherit (CLI) or .home (desktop launcher).
  ```
- [`0cb189b`](https://github.com/ghostty-org/ghostty/commit/0cb189bfbba4515797dee666e107d9b73b861ab0) config: working-directory expands ~/ prefix ([#11337](https://github.com/ghostty-org/ghostty/issues/11337)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11336
  
  Introduce a proper WorkingDirectory tagged union type with home,
  inherit, and path variants. The field is now an optional
  (?WorkingDirectory) where null represents "use platform default" which
  is resolved during Config.finalize to .inherit (CLI) or .home (desktop
  launcher).
  ```
- [`96f9772`](https://github.com/ghostty-org/ghostty/commit/96f9772cd838fa9d562ed369ea6fa8e657f870e3) tests: disable tests that fail if you have locally installed fonts ([@jcollie](https://github.com/jcollie))
  ```text
  If you have "Noto Sans Tai Tham" and/or "Noto Sans Javanese" installed
  locally on Linux, three tests fail. This PR disables those tests until a
  more permanent solution can be found.
  ```
- [`c131329`](https://github.com/ghostty-org/ghostty/commit/c1313294cd765e41c02e0b8e048fbad1beb5f740) add comments about why tests are disabled ([@jcollie](https://github.com/jcollie))
- [`a4cc37d`](https://github.com/ghostty-org/ghostty/commit/a4cc37db72bd345a7cdd90855e80339ed1caddd1) tests: disable tests that fail if you have locally installed fonts ([#11285](https://github.com/ghostty-org/ghostty/issues/11285)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  If you have "Noto Sans Tai Tham" and/or "Noto Sans Javanese" installed
  locally on Linux, three tests fail. This PR disables those tests until a
  more permanent solution can be found.
  ```
- [`71f8152`](https://github.com/ghostty-org/ghostty/commit/71f81527ad8d3393609d1e9134987653249473d4) macos: remove IntrinsicSizeTimingTests temporarily ([@mitchellh](https://github.com/mitchellh))
  ```text
  These were too flaky.
  ```
- [`8784636`](https://github.com/ghostty-org/ghostty/commit/8784636547520dc94d1b6ed2d58db00ed80eadfb) macos: remove IntrinsicSizeTimingTests temporarily ([#11332](https://github.com/ghostty-org/ghostty/issues/11332)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  These were too flaky.
  
  cc @bo2themax
  ```
- [`de0f2ab`](https://github.com/ghostty-org/ghostty/commit/de0f2ab22d941e270a4ba259ef2522f71bb84247) macos:  add enum type for macos-titlebar-style ([@bo2themax](https://github.com/bo2themax))
- [`53637ec`](https://github.com/ghostty-org/ghostty/commit/53637ec7b2b91da8e19b79cd755874b3fc2cf0db) fix jump_to_prompt forward behavior for multiline prompts ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11330.
  
  When jumping forward from prompt content, skip prompt continuation rows so a
  multiline prompt is treated as a single prompt block.
  ```
- [`7fb8e0a`](https://github.com/ghostty-org/ghostty/commit/7fb8e0ac90eeba0413736dee5b5b451d1a79ae20) fix jump_to_prompt forward behavior for multiline prompts ([#11331](https://github.com/ghostty-org/ghostty/issues/11331)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11330.
  
  When jumping forward from prompt content, skip prompt continuation rows
  so a multiline prompt is treated as a single prompt block.
  ```
- [`f88b42a`](https://github.com/ghostty-org/ghostty/commit/f88b42ad3968779168666eb03866f70e9a7568e4) macos: add enum type for macos-titlebar-style ([#11262](https://github.com/ghostty-org/ghostty/issues/11262)) ([@mitchellh](https://github.com/mitchellh))
- [`aaad43c`](https://github.com/ghostty-org/ghostty/commit/aaad43c23569e75929d611a13483e96cec6b1060) macos: make paste_from_clipboard performable on macos ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #10751
  ```
- [`c06ede5`](https://github.com/ghostty-org/ghostty/commit/c06ede584939979947336094c35b5a4c9a5ba267) macos: make paste_from_clipboard performable on macos ([#11328](https://github.com/ghostty-org/ghostty/issues/11328)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #10751
  ```
- [`f8d7876`](https://github.com/ghostty-org/ghostty/commit/f8d7876203ad65572cd085ff89afb758252217cb) Update VOUCHED list ([#11329](https://github.com/ghostty-org/ghostty/issues/11329)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11313#issuecomment-4033213188)
  from @mitchellh.
  
  Vouch: @VaughanAndrews
  ```
- [`6092c29`](https://github.com/ghostty-org/ghostty/commit/6092c299d55cd24ec72d3d5d2365279645c30ff3) macos: reset mouse state on focus loss to prevent phantom drag ([@seruman](https://github.com/seruman))
  ```text
  Fixes phantom mouse drag/selection when switching splits or apps.
  The suppressNextLeftMouseUp flag and core mouse click_state were not
  being reset on focus transitions, causing stale state that led to
  unexpected drag behavior.
  
  - Reset suppressNextLeftMouseUp in focusDidChange when losing focus
  - Defensively reset the flag when processing normal clicks
  - Reset core mouse.click_state and left_click_count on focus loss
  ```
- [`119ce0b`](https://github.com/ghostty-org/ghostty/commit/119ce0bc1df37be42cd65c57b4a3e8c39013b6c5) macos: reset mouse state on focus loss to prevent phantom drag ([#11276](https://github.com/ghostty-org/ghostty/issues/11276)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes https://github.com/ghostty-org/ghostty/discussions/11203
  
  The `suppressNextLeftMouseUp` flag from #11167 wasn't being reset on
  focus loss, causing stale state that led to phantom drags/selections and
  scrolls if you're lucky enough.
  
  I've followed the #11167 's path and made it reset on focus loss.
  
  As I stated in the [vouch
  request](https://github.com/ghostty-org/ghostty/discussions/11274); I'm
  not experienced in Swift, just following the prior PR's steps to reset
  the state. I've been using this patch for couple days and the change
  looks trivial to me tho not 100% sure if I'm missing anything.
  
  > [!NOTE]
  > Used Claude Code -Opus 4.6- for navigating the codebase and reviewing
  the change.
  ```
- [`d9039eb`](https://github.com/ghostty-org/ghostty/commit/d9039eb85a6f12ff7de205c116d978482c80bdab) config: don't double load app support path on macOS ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11323
  ```
- [`9759787`](https://github.com/ghostty-org/ghostty/commit/9759787847a0c6ed6983d1a8fe2b9c1d615b6010) config: don't double load app support path on macOS ([#11326](https://github.com/ghostty-org/ghostty/issues/11326)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11323
  ```
- [`4e24adf`](https://github.com/ghostty-org/ghostty/commit/4e24adf7177946af7f3d0e367d94fc8e2dead133) ci: skip xcode tests for freetype build ([@mitchellh](https://github.com/mitchellh))
- [`cfedda1`](https://github.com/ghostty-org/ghostty/commit/cfedda1a0e9197dfa7463a3a3aeb90ad980ab86f) macOS: add regression tests for intrinsicContentSize race ([#11256](https://github.com/ghostty-org/ghostty/issues/11256)) ([@bo2themax](https://github.com/bo2themax))
  ```text
  Tests that validate intrinsicContentSize returns a correct value when
  TerminalController.windowDidLoad() reads it. Currently fail, proving
  the race condition where @FocusedValue hasn't propagated
  lastFocusedSurface before the 40ms timer fires.
  ```
- [`a6cd1b0`](https://github.com/ghostty-org/ghostty/commit/a6cd1b08af240e7be0b07163d78dac5efa6b1752) macOS: fix intrinsicContentSize race in windowDidLoad ([#11256](https://github.com/ghostty-org/ghostty/issues/11256)) ([@bo2themax](https://github.com/bo2themax))
  ```text
  Add initialContentSize fallback on TerminalViewContainer so
  intrinsicContentSize returns the correct value immediately,
  without waiting for @FocusedValue to propagate. This removes
  the need for the DispatchQueue.main.asyncAfter 40ms delay.
  ```
- [`1592caf`](https://github.com/ghostty-org/ghostty/commit/1592cafa32e99119cee0b074fde3f50070ac3dac) Update AGENTS.md ([@mitchellh](https://github.com/mitchellh))
- [`7629130`](https://github.com/ghostty-org/ghostty/commit/7629130fb4f66262684d4b75d549b522d5943f59) macOS: restore keyboard focus after inline tab title edit ([@chronologos](https://github.com/chronologos))
  ```text
  After finishing an inline tab title edit (via keybind or double-click),
  `TabTitleEditor.finishEditing()` calls `makeFirstResponder(nil)` to
  clear focus from the text field, leaving the window itself as first
  responder. No code path restores focus to the terminal surface, so all
  keyboard input is lost until the user clicks into a pane.
  
  Add a `tabTitleEditorDidFinishEditing` delegate callback that fires
  after every edit (commit or cancel). TerminalWindow implements it by
  calling `makeFirstResponder(focusedSurface)` to hand focus back to the
  terminal.
  
  Fixes https://github.com/ghostty-org/ghostty/discussions/11315
  ```
- [`85f0972`](https://github.com/ghostty-org/ghostty/commit/85f0972b395c045fb91488399aeb6597c6be94ec) macOS: fix intrinsicContentSize race in windowDidLoad ([#11322](https://github.com/ghostty-org/ghostty/issues/11322)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This should fix #11256 and #11271.
  
  Tested manually with various combination of `window-width/height` and
  `macos-titlebar-style`.
  
  
  https://github.com/user-attachments/assets/90c12728-b195-47bf-abfd-8a4034b1e7a2
  
  
  ### AI Disclosure
  
  All the commits are generated by Claude, but orchestrated and manually
  tested by myself.
  ```
- [`3782d11`](https://github.com/ghostty-org/ghostty/commit/3782d118e1123c839eaff139bceb268ba5892bc7) macOS: restore keyboard focus after inline tab title edit ([#11320](https://github.com/ghostty-org/ghostty/issues/11320)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Summary
  
  - After finishing an inline tab title edit (via keybind or
  double-click), all keyboard input is lost because
  `TabTitleEditor.finishEditing()` sets `makeFirstResponder(nil)`, leaving
  the window itself as first responder with no path back to the terminal
  surface.
  - Adds a `tabTitleEditorDidFinishEditing` delegate callback to
  `TabTitleEditorDelegate` that fires after every edit (commit or cancel).
  - `TerminalWindow` implements it by calling
  `makeFirstResponder(focusedSurface)` to restore keyboard focus to the
  terminal.
  
  Fixes https://github.com/ghostty-org/ghostty/discussions/11315
  
  ## Testing
  
  - [x] Bind `prompt_tab_title` to a keybind (e.g. `keybind =
  cmd+shift+i=prompt_tab_title`)
  - [x] Trigger inline tab title edit via keybind, press Enter — verify
  keyboard input works immediately
  - [x] Trigger inline tab title edit via keybind, press Escape — verify
  keyboard input works immediately
  - [x] Double-click a tab title, press Enter — verify keyboard input
  works immediately
  - [x] Double-click a tab title, press Escape — verify keyboard input
  works immediately
  - [x] Verify Cmd+number tab switching works after all of the above
  - [x] Verify split pane focus is correct after editing tab title with
  splits open
  
  AI disclosure: Codebase exploration and review via [Claude
  Code](https://claude.com/claude-code)
  ```
- [`f8f431b`](https://github.com/ghostty-org/ghostty/commit/f8f431ba67e32b7fa0d63c54bc736d55cf27532f) docs: update bell-features docs for macOS ([@jcollie](https://github.com/jcollie))
  ```text
  PR #11154 didn't fully update the docs regarding `bell-features=audio`
  on macOS.
  ```
- [`e11f350`](https://github.com/ghostty-org/ghostty/commit/e11f350e8eb81ceda33a8267b6181c50e5be2789) docs: update bell-features docs for macOS ([#11279](https://github.com/ghostty-org/ghostty/issues/11279)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  PR #11154 didn't fully update the docs regarding `bell-features=audio`
  on macOS.
  ```
- [`6c73091`](https://github.com/ghostty-org/ghostty/commit/6c7309196fef805e1d0fbb0ce82944aab8edda7d) Update VOUCHED list ([#11321](https://github.com/ghostty-org/ghostty/issues/11321)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11320#issuecomment-4031703556)
  from @mitchellh.
  
  Vouch: @chronologos
  ```
- [`c83dea4`](https://github.com/ghostty-org/ghostty/commit/c83dea49fd1c4b89eee2956f8638b80122596bdc) Update VOUCHED list ([#11318](https://github.com/ghostty-org/ghostty/issues/11318)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11309#discussioncomment-16069391)
  from @mitchellh.
  
  Vouch: @dzhlobo
  ```
- [`327783f`](https://github.com/ghostty-org/ghostty/commit/327783ff6c86c5843eedaab20c7f394e4396daa4) Update VOUCHED list ([#11314](https://github.com/ghostty-org/ghostty/issues/11314)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11287#discussioncomment-16069141)
  from @mitchellh.
  
  Vouch: @ocean6954
  ```

## March 9, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22870694331), [2](https://github.com/ghostty-org/ghostty/actions/runs/22862195455), [3](https://github.com/ghostty-org/ghostty/actions/runs/22861709161), [4](https://github.com/ghostty-org/ghostty/actions/runs/22861225605), [5](https://github.com/ghostty-org/ghostty/actions/runs/22860218660), [6](https://github.com/ghostty-org/ghostty/actions/runs/22856309252), [7](https://github.com/ghostty-org/ghostty/actions/runs/22839029556), [8](https://github.com/ghostty-org/ghostty/actions/runs/22837001539), [9](https://github.com/ghostty-org/ghostty/actions/runs/22833175636)  
Summary: 9 runs • 21 commits • 6 authors

### Changes

- [`f8a0a45`](https://github.com/ghostty-org/ghostty/commit/f8a0a45963010e5cb3baa8069dbcc07a60c5d26d) Update VOUCHED list ([#11275](https://github.com/ghostty-org/ghostty/issues/11275)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11274#discussioncomment-16057271)
  from @jcollie.
  
  Vouch: @seruman
  ```
- [`703d11c`](https://github.com/ghostty-org/ghostty/commit/703d11c642a96af9e54b55b04f131bf3888948a9) Bump version to 1.3.0 ([@mitchellh](https://github.com/mitchellh))
- [`a6ee1fb`](https://github.com/ghostty-org/ghostty/commit/a6ee1fb292d2361bd3fca7998d1d86f6509b3272) macos: increase window-width/height apply delay from 10ms to 40ms ([@mitchellh](https://github.com/mitchellh))
  ```text
  Band-aid for #10304
  
  We don't have a robust fix yet but this should help mitigate more
  scenarios.
  ```
- [`8dde269`](https://github.com/ghostty-org/ghostty/commit/8dde2693bcd55e72a48c1b771f3e685e9bdfcfb6) macos: increase window-width/height apply delay from 10ms to 40ms ([#11265](https://github.com/ghostty-org/ghostty/issues/11265)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Band-aid for #10304
  
  We don't have a robust fix yet but this should help mitigate more
  scenarios.
  ```
- [`3c93c35`](https://github.com/ghostty-org/ghostty/commit/3c93c35869f40bd95db3e729549f05f48a371089) macOS: filter proper intrinsicContentSize when opening new window ([@bo2themax](https://github.com/bo2themax))
  ```text
  Fixes #11256
  ```
- [`3445c9a`](https://github.com/ghostty-org/ghostty/commit/3445c9afdad7d459ba42e0c66e25e0c09dda7eff) macOS: filter proper intrinsicContentSize when opening new window ([#11257](https://github.com/ghostty-org/ghostty/issues/11257)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11256, which is rather hard to reproduce on macOS 26, but after
  adding breaking points on size update, we can see that it happens when
  the `intrinsicContentSize` is not properly updated.
  
  <img width="998" height="556" alt="Xnip2026-03-09_11-38-40"
  src="https://github.com/user-attachments/assets/8ac1de91-5895-45fc-a443-002eb016a1ce"
  />
  ```
- [`dd3d72c`](https://github.com/ghostty-org/ghostty/commit/dd3d72c3de474c10da7e1576e39c7e2e7ad7617f) Revert "macOS: filter proper intrinsicContentSize when opening new window ([#11257](https://github.com/ghostty-org/ghostty/issues/11257))" ([@mitchellh](https://github.com/mitchellh))
  ```text
  This reverts commit 3445c9afdad7d459ba42e0c66e25e0c09dda7eff, reversing
  changes made to 1e981f858a4833ae63e7e53f9f0c84c516b4241e.
  ```
- [`3ba49a7`](https://github.com/ghostty-org/ghostty/commit/3ba49a784f4313e301efb68362158e8e338662da) terminal: fix grapheme edge-wrap hyperlink integrity panic ([@mitchellh](https://github.com/mitchellh))
  ```text
  When a grapheme expands to width 2 at the screen edge, this path can write
  spacer_head before printWrap() sets row.wrap. With an active hyperlink,
  printCell triggers hyperlink bookkeeping and page integrity checks in that
  intermediate state, causing UnwrappedSpacerHead.
  
  Mark row.wrap before writing spacer_head in this grapheme-wrap path to keep
  the intermediate state valid.
  ```
- [`1e981f8`](https://github.com/ghostty-org/ghostty/commit/1e981f858a4833ae63e7e53f9f0c84c516b4241e) terminal: fix grapheme edge-wrap hyperlink integrity panic ([#11264](https://github.com/ghostty-org/ghostty/issues/11264)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  When a grapheme expands to width 2 at the screen edge, this path can
  write spacer_head before printWrap() sets row.wrap. With an active
  hyperlink, printCell triggers hyperlink bookkeeping and page integrity
  checks in that intermediate state, causing UnwrappedSpacerHead.
  
  Mark row.wrap before writing spacer_head in this grapheme-wrap path to
  keep the intermediate state valid.
  ```
- [`fd557e8`](https://github.com/ghostty-org/ghostty/commit/fd557e83474e23b42d0f5133df319a79eda66653) bash: only define $__ghostty_ps0 when unset ([@jparise](https://github.com/jparise))
  ```text
  This fixes an error if the script was sourced a second time:
  
      bash: __ghostty_ps0: readonly variable
  
  Because this is a non-exported variable, this would only happen if the
  script was sourced multiple times in the same bash session.
  ```
- [`0a659af`](https://github.com/ghostty-org/ghostty/commit/0a659af55ff214c781347def6f41d7aaed63b84a) bash: handle existing ; in PROMPT_COMMAND ([@jparise](https://github.com/jparise))
  ```text
  If an existing PROMPT_COMMAND was a string ending in ; (and maybe some
  spaces), we'd add a redundant ;, resulting in a syntax error. Now we
  strip any trailing `;[[:space:]]*` characters from the original string
  before add ours.
  ```
- [`308b713`](https://github.com/ghostty-org/ghostty/commit/308b713e5828a3e1b07238f3ab56d75914389e3b) bash: handle existing ; in PROMPT_COMMAND ([#11260](https://github.com/ghostty-org/ghostty/issues/11260)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  If an existing PROMPT_COMMAND was a string ending in ; (and maybe some
  spaces), we'd add a redundant ;, resulting in a syntax error. Now we
  strip any trailing `;[[:space:]]*` characters from the original string
  before add ours.
  
  Fixes #11259
  ```
- [`f4c40c7`](https://github.com/ghostty-org/ghostty/commit/f4c40c7d53c1de1fcc97413fd6d543a561924e89) bash: only define $__ghostty_ps0 when unset ([#11258](https://github.com/ghostty-org/ghostty/issues/11258)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This fixes an error if the script was sourced a second time:
  
      bash: __ghostty_ps0: readonly variable
  
  Because this is a non-exported variable, this would only happen if the
  script was sourced multiple times in the same bash session.
  ```
- [`aee9361`](https://github.com/ghostty-org/ghostty/commit/aee9361fa3fdd95177823fe1ffa2b8ff19e7e413) Update es_AR.po ([@dariogriffo](https://github.com/dariogriffo))
  ```text
  Minor updates
  ```
- [`2cb8f61`](https://github.com/ghostty-org/ghostty/commit/2cb8f61bcfafeae1382edd23a1c105ab25c7a8c8) Update es_AR.po ([@dariogriffo](https://github.com/dariogriffo))
- [`c570d53`](https://github.com/ghostty-org/ghostty/commit/c570d53d45218aae294c52fa81d48220755fe692) Update es_AR.po ([@dariogriffo](https://github.com/dariogriffo))
- [`4969b0c`](https://github.com/ghostty-org/ghostty/commit/4969b0c56ecf65e0639e978a6bb9e7f076273afe) Update es_AR.po ([@dariogriffo](https://github.com/dariogriffo))
- [`9dc6f67`](https://github.com/ghostty-org/ghostty/commit/9dc6f6763f12d056e286ca62e02f960b19a8fb9e) Update es_AR.po translation for "Unable to acquire an OpenGL context for rendering." ([#11227](https://github.com/ghostty-org/ghostty/issues/11227)) ([@00-kat](https://github.com/00-kat))
  ```text
  - "Unable to acquire an OpenGL context for rendering."
  This could be translated to "No se puede" or "No se pudo", depends on
  the context of the message.
  If the message is showing a current intent the translation should be "No
  se puede", if the message is communicating that Ghostty failed to
  acquire the OpenGL then the translation should be "No se pudo", here I
  need more context.
  Either case the wording "No se puedo" is incorrect.
  ```
- [`233fb12`](https://github.com/ghostty-org/ghostty/commit/233fb12081009fee649295d323c93716655fc671) macos: add AppleScript front window and focused terminal properties ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds two new propeties to make it easy to get the frontmost (main)
  window and the focused terminal within a tab. We already had a property
  to get the selected tab of a tab group.
  ```
- [`b82d452`](https://github.com/ghostty-org/ghostty/commit/b82d452f486bbff6977ee4e5472e3cf9163e9b7a) macos: add AppleScript front window and focused terminal properties ([#11251](https://github.com/ghostty-org/ghostty/issues/11251)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This adds two new propeties to make it easy to get the frontmost (main)
  window and the focused terminal within a tab. We already had a property
  to get the selected tab of a tab group.
  
  ## Examples
  
  ### Send Input to Focused Terminal
  
  ```AppleScript
  tell application "Ghostty"
    set term to focused terminal of selected tab of front window
    input text "pwd\n" to term
  end tell
  ```
  
  ### Split the Focused Terminal
  
  ```applescript
  tell application "Ghostty"
    set currentTerm to focused terminal of selected tab of front window
    set newTerm to split currentTerm direction right
    input text "echo split-ready\n" to newTerm
  end tell
  ```
  ````
- [`ec1ca4c`](https://github.com/ghostty-org/ghostty/commit/ec1ca4c0c903d13a15452c18b1df11b3cabddaf7) Update VOUCHED list ([#11247](https://github.com/ghostty-org/ghostty/issues/11247)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11246#discussioncomment-16045992)
  from @jcollie.
  
  Vouch: @jmcgover
  ```

## March 8, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22830044719), [2](https://github.com/ghostty-org/ghostty/actions/runs/22828977678), [3](https://github.com/ghostty-org/ghostty/actions/runs/22823777958), [4](https://github.com/ghostty-org/ghostty/actions/runs/22823564404), [5](https://github.com/ghostty-org/ghostty/actions/runs/22823301773), [6](https://github.com/ghostty-org/ghostty/actions/runs/22823118931), [7](https://github.com/ghostty-org/ghostty/actions/runs/22822697530), [8](https://github.com/ghostty-org/ghostty/actions/runs/22819402525), [9](https://github.com/ghostty-org/ghostty/actions/runs/22816478930)  
Summary: 9 runs • 21 commits • 10 authors

### Changes

- [`8635fef`](https://github.com/ghostty-org/ghostty/commit/8635fef7a5dc6185b67982dc94892d6ddb3b9ac0) if search is active dont apply unfocused options ([@rhodes-b](https://github.com/rhodes-b))
- [`1d59f5d`](https://github.com/ghostty-org/ghostty/commit/1d59f5dbcdbe0fc7065a6ed9c46c42d22584add4) pass search active state through blueprint ([@rhodes-b](https://github.com/rhodes-b))
- [`2d347ca`](https://github.com/ghostty-org/ghostty/commit/2d347cad336b6d4bd461f33fe87d90e6aa269843) GTK: Don't apply unfocused options when searching ([#11224](https://github.com/ghostty-org/ghostty/issues/11224)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  If you have multiple splits and start searching naturally the focus
  transfers over to the search widget which would apply the unfocused
  options. This could make it difficult to view your matches from
  searching without re-focusing the surface.
  
  This was discovered when I tested
  https://github.com/ghostty-org/ghostty/discussions/11218 (which is a
  different issue)
  ```
- [`a384af5`](https://github.com/ghostty-org/ghostty/commit/a384af5e25228b5b342c717abb5387bd4c3b0b58) vt: align SGR C enum tags with parser output ([@mitchellh](https://github.com/mitchellh))
  ```text
  Remove the stale GHOSTTY_SGR_ATTR_RESET_UNDERLINE entry from the C header
  and renumber subsequent GhosttySgrAttributeTag values to match
  src/terminal/sgr.zig Attribute.Tag ordering.
  
  This fixes misclassified attributes from ghostty_sgr_next for C consumers
  that switch on the enum tags from include/ghostty/vt/sgr.h.
  ```
- [`a2ea5b5`](https://github.com/ghostty-org/ghostty/commit/a2ea5b5d7940c97205fba9452517f75213328e03) Update VOUCHED list ([#11240](https://github.com/ghostty-org/ghostty/issues/11240)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11207#discussioncomment-16043795)
  from @mitchellh.
  
  Vouch: @MOlechowski
  ```
- [`43f3d2c`](https://github.com/ghostty-org/ghostty/commit/43f3d2ca9206220040b66d9b8b7bd281d32b1795) vt: align SGR C enum tags with parser output ([#11239](https://github.com/ghostty-org/ghostty/issues/11239)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Remove the stale GHOSTTY_SGR_ATTR_RESET_UNDERLINE entry from the C
  header and renumber subsequent GhosttySgrAttributeTag values to match
  src/terminal/sgr.zig Attribute.Tag ordering.
  
  This fixes misclassified attributes from ghostty_sgr_next for C
  consumers that switch on the enum tags from include/ghostty/vt/sgr.h.
  ```
- [`235dde6`](https://github.com/ghostty-org/ghostty/commit/235dde6844d697e73e974c2311c69abf3a57b0f8) fix: list-actions outputs without `--docs` ([@dmehala](https://github.com/dmehala))
  ```text
  Explicitly flush the buffer once the generation is complete.
  
  Resolves #11221
  ```
- [`2d9dc5c`](https://github.com/ghostty-org/ghostty/commit/2d9dc5cfd1aa8bb9a7dda5a273197535b0e6fbee) fix: list-actions outputs without `--docs` ([#11231](https://github.com/ghostty-org/ghostty/issues/11231)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Explicitly flush the buffer once the generation is complete.
  
  Resolves #11221
  ```
- [`686fd34`](https://github.com/ghostty-org/ghostty/commit/686fd34e96409dcf9ab095294f3d073a7ea04b7d) Update VOUCHED list ([#11232](https://github.com/ghostty-org/ghostty/issues/11232)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11231#issuecomment-4019204219)
  from @mitchellh.
  
  Vouch: @dmehala
  ```
- [`059bd54`](https://github.com/ghostty-org/ghostty/commit/059bd54a5d9188d2f7c6fc3a56afc35b934f4ff1) elvish: improve OSC 133 semantic prompt support ([@jparise](https://github.com/jparise))
  ```text
  Add `aid=$pid` to 133;A and 133;D for nested shell tracking, and fix the
  state comparison which was incorrectly using `constantly` (comparing a
  string to a function, which always evaluated to true).
  
  OSC 133;B (input start) and 133;P;k=r (right prompt) cannot be reliably
  implemented at the script level because Elvish escapes control
  characters in prompt function output, and writing directly to /dev/tty
  has timing issues because Elvish renders its prompts on a background
  thread. Full semantic prompt support requires a native implementation:
  https://github.com/elves/elvish/pull/1917
  
  See: #10523
  ```
- [`df4d9bc`](https://github.com/ghostty-org/ghostty/commit/df4d9bc0d00a3fc309dc68bdc81254e32816c298) macos: fix quick terminal glassy background ([@bo2themax](https://github.com/bo2themax))
- [`1d76820`](https://github.com/ghostty-org/ghostty/commit/1d76820937c6d4c8008a74a80e5c0c03cac1f8fd) elvish: improve OSC 133 semantic prompt support ([#11222](https://github.com/ghostty-org/ghostty/issues/11222)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add `aid=$pid` to 133;A and 133;D for nested shell tracking, and fix the
  state comparison which was incorrectly using `constantly` (comparing a
  string to a function, which always evaluated to true).
  
  OSC 133;B (input start) and 133;P;k=r (right prompt) cannot be reliably
  implemented at the script level because Elvish escapes control
  characters in prompt function output, and writing directly to /dev/tty
  has timing issues because Elvish renders its prompts on a background
  thread. Full semantic prompt support requires a native implementation:
  https://github.com/elves/elvish/pull/1917
  
  See: #10523
  ```
- [`602db55`](https://github.com/ghostty-org/ghostty/commit/602db55a283adeabfbd082c678eddf1a6ee1ae43) macos: fix quick terminal glassy background ([#11229](https://github.com/ghostty-org/ghostty/issues/11229)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes a regression from
  [#9032096](https://github.com/ghostty-org/ghostty/commit/9032096) 🥲 and
  clean some dead code
  
  On first launch of the quick terminal window, the container style is not
  properly updated; you'll have to reload the config to show the
  background.
  
  <img width="571" height="312" alt="IMG_4783"
  src="https://github.com/user-attachments/assets/c5d920ea-9ad8-494d-98c0-c560e36c4a31"
  />
  ```
- [`360c369`](https://github.com/ghostty-org/ghostty/commit/360c369d235e36092ba0ac4319de0e7a8be1eaa7) Update VOUCHED list ([#11230](https://github.com/ghostty-org/ghostty/issues/11230)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11125#discussioncomment-16041168)
  from @mitchellh.
  
  Vouch: @pauley-unsaturated
  ```
- [`1a15fc0`](https://github.com/ghostty-org/ghostty/commit/1a15fc0adba90bddce5c95a04c9ea30254186925) i18n: update Indonesian translation (id_ID) ([@halosatrio](https://github.com/halosatrio))
- [`97c479a`](https://github.com/ghostty-org/ghostty/commit/97c479a3476d1a1ebb278b86b883cf7715beeab0) i18n: update Indonesian translation (id_ID) ([#11226](https://github.com/ghostty-org/ghostty/issues/11226)) ([@00-kat](https://github.com/00-kat))
  ```text
  Updated translation for Indonesian (id_ID). This is a duplicate of PR
  #10794, as the original PR has not been updated since last week. I think
  it would be better to merge this updated translation before the 1.3
  release.
  ```
- [`eaef109`](https://github.com/ghostty-org/ghostty/commit/eaef1094d92c579fbfc0ce204cc1fc09c41059cf) Update VOUCHED list ([#11228](https://github.com/ghostty-org/ghostty/issues/11228)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11227#issuecomment-4019112158)
  from @00-kat.
  
  Vouch: @dariogriffo
  ```
- [`e9dc03b`](https://github.com/ghostty-org/ghostty/commit/e9dc03b0b4fd5b23d0791987a517851656831ddb) i18n: update Hungarian translations ([@balazs-szucs](https://github.com/balazs-szucs))
- [`42d3635`](https://github.com/ghostty-org/ghostty/commit/42d36359dbe3cb13adacf8e40ddf3c37c8a2e564) i18n: update Hungarian translations ([#11039](https://github.com/ghostty-org/ghostty/issues/11039)) ([@00-kat](https://github.com/00-kat))
  ```text
  New string translated with this!
  
  Part of: #10632
  ```
- [`adc6794`](https://github.com/ghostty-org/ghostty/commit/adc6794f3b1a1f46048f86e61397bc4736567589) Add es_ES.UTF-8 translation ([@alosarjos](https://github.com/alosarjos))
- [`4d89f1b`](https://github.com/ghostty-org/ghostty/commit/4d89f1bcaeacd64ced18dc20504362b759f22e65) Add es_ES.UTF-8 translation ([#10722](https://github.com/ghostty-org/ghostty/issues/10722)) ([@00-kat](https://github.com/00-kat))

## March 7, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22803119380), [2](https://github.com/ghostty-org/ghostty/actions/runs/22802362890), [3](https://github.com/ghostty-org/ghostty/actions/runs/22800843484)  
Summary: 3 runs • 30 commits • 4 authors

### Changes

- [`4bb602b`](https://github.com/ghostty-org/ghostty/commit/4bb602b0e1a251f401e49d490400e4a2b51d0b5a) Fix snap EGL vendor dirs to include host NVIDIA ICD paths ([@04cb](https://github.com/04cb))
- [`472b926`](https://github.com/ghostty-org/ghostty/commit/472b926a4d7abbacad4deea17aa0a0c69ffc12d3) Fix snap EGL vendor dirs to include host NVIDIA ICD paths ([#11209](https://github.com/ghostty-org/ghostty/issues/11209)) ([@kenvandine](https://github.com/kenvandine))
  ```text
  Fixes #10760. The snap launcher script was overriding the default system
  EGL vendor directories, preventing NVIDIA's proprietary EGL driver from
  being discovered. This caused crashes for users with NVIDIA GPUs on snap
  systems.
  
  The fix adds the standard host system paths (/etc/glvnd/egl_vendor.d and
  /usr/share/glvnd/egl_vendor.d) to __EGL_VENDOR_LIBRARY_DIRS before the
  snap-internal path. This is safe for classic confinement snaps since the
  host filesystem is fully accessible.
  ```
- [`291fbf5`](https://github.com/ghostty-org/ghostty/commit/291fbf55cb9c6946d7c080c90d8163d0b720dfe0) macos: AppleScript starting ([@mitchellh](https://github.com/mitchellh))
- [`c90a782`](https://github.com/ghostty-org/ghostty/commit/c90a782e592aa90e3a1479b80d5b9a3acdc63dff) macos: implement basic read-only applescript stuff ([@mitchellh](https://github.com/mitchellh))
- [`52c0709`](https://github.com/ghostty-org/ghostty/commit/52c0709d88c20f05edc1450d5e7105377f03206d) macos: add ability for agents to run debug app ([@mitchellh](https://github.com/mitchellh))
- [`40c7481`](https://github.com/ghostty-org/ghostty/commit/40c74811f16236df9afeb522dcbd9a98ebcb4a3f) macos: fix perform action ([@mitchellh](https://github.com/mitchellh))
- [`ef669ee`](https://github.com/ghostty-org/ghostty/commit/ef669eeae7574335631d6897c07f60ce4015727c) macos: add AppleScript `split` command ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a new `split` command to the AppleScript scripting dictionary that
  splits a terminal in a given direction (right, left, down, up) and
  returns the newly created terminal.
  
  The command is exposed as:
    split terminal <terminal> direction <direction>
  
  Also adds a `fourCharCode` String extension for converting four-character
  ASCII strings to their FourCharCode (UInt32) representation.
  ```
- [`1742aed`](https://github.com/ghostty-org/ghostty/commit/1742aeda503c57979b7faa54c9ecffa9a176abde) macos: add focus and close AppleScript commands for terminals ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add two new AppleScript commands to the scripting dictionary:
  
  - `focus terminal <terminal>` — focuses the given terminal and brings
    its window to the front.
  - `close terminal <terminal>` — closes the given terminal without a
    confirmation prompt.
  
  Each command is implemented as an NSScriptCommand subclass following
  the same pattern as the existing split command.
  ```
- [`fd5ad1f`](https://github.com/ghostty-org/ghostty/commit/fd5ad1f574e3ad084db0e2a9b2161edaf53e85e5) macos: add AppleScript commands for text input, key, and mouse events ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add five new AppleScript commands to Ghostty.sdef mirroring the existing
  App Intents for terminal input:
  
  - `input text`: send text to a terminal as if pasted
  - `send key`: simulate a keyboard event with optional action and modifiers
  - `send mouse button`: send a mouse button press/release event
  - `send mouse position`: send a mouse cursor position event
  - `send mouse scroll`: send a scroll event with precision and momentum
  
  A shared `input action` enumeration (press/release) is used by both key
  and mouse button commands. Modifier keys are passed as a comma-separated
  string parameter (shift, control, option, command).
  ```
- [`ffe622e`](https://github.com/ghostty-org/ghostty/commit/ffe622ed30c60eb2a0ed2fdd644b2b4f606b0ba0) macos: add standard application properties and commands ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add standard Cocoa scripting definitions to the AppleScript dictionary:
  
  - Application properties: name, frontmost, version
  - Standard Suite commands: exists, quit
  
  These are backed by built-in Cocoa scripting classes (NSExistsCommand,
  NSQuitCommand) and standard NSApplication KVC keys, so no Swift code
  changes are needed.
  ```
- [`547fd6f`](https://github.com/ghostty-org/ghostty/commit/547fd6f748e9c504019513b3ec95fdf5a1ec4efb) typos: ignore apple four char codes ([@mitchellh](https://github.com/mitchellh))
- [`d03338c`](https://github.com/ghostty-org/ghostty/commit/d03338c1b53e1f0bc1e5f711f91c5d474d27ceee) macos: fix iOS build ([@mitchellh](https://github.com/mitchellh))
- [`341d8bd`](https://github.com/ghostty-org/ghostty/commit/341d8bdf754b85fe0dfaa57ceabe598e7eea0c59) macos: AppleScript windows/tabs ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add ScriptWindow and ScriptTab classes to expose window/tab hierarchy
  to AppleScript, along with the corresponding sdef definitions.
  ```
- [`f72d416`](https://github.com/ghostty-org/ghostty/commit/f72d41675bfd1d912f71a00c1e8716ddd6ae9654) macos: fix AppleScript quit command being silently ignored ([@mitchellh](https://github.com/mitchellh))
  ```text
  The application class in Ghostty.sdef was missing a responds-to
  declaration for the quit command. Apple's Cocoa Scripting requires
  the application class to explicitly declare it responds to quit via
  handleQuitScriptCommand: for the aevtquit event to be dispatched.
  ```
- [`e514035`](https://github.com/ghostty-org/ghostty/commit/e514035519a88fa593dd1047fa22bcb39a9022c0) macos: add terminals element to window and tab AppleScript classes ([@mitchellh](https://github.com/mitchellh))
  ```text
  Expose terminal surfaces as elements on both ScriptWindow and ScriptTab,
  allowing AppleScript to enumerate terminals scoped to a specific window
  or tab (e.g. `terminals of window 1`, `terminals of tab 1 of window 1`).
  
  Changes:
  - Add `<element type="terminal">` to window and tab classes in Ghostty.sdef
  - Add `terminals` computed property and `valueInTerminalsWithUniqueID:`
    lookup to ScriptWindow (returns all surfaces across all tabs)
  - Add `terminals` computed property and `valueInTerminalsWithUniqueID:`
    lookup to ScriptTab (returns surfaces within that tab)
  ```
- [`122d0ec`](https://github.com/ghostty-org/ghostty/commit/122d0ecdfd9947d0c8c34953d0babc39502556e5) macos: expose name (title) on window, tab, and terminal via AppleScript ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a `name` property (code `pnam`, cocoa key `title`) to the window, tab,
  and terminal classes in the scripting definition. This follows the standard
  Cocoa scripting convention where `name`/`pnam` maps to the `title` KVC key,
  matching what Apple does in CocoaStandard.sdef for NSWindow.
  
  Also fixes the pre-existing terminal `title` property which used a custom
  four-char code (`Gttl`) that AppleScript could not resolve directly — only
  via `properties of terminal`. All three classes now use the standard `pnam`
  code so `name of window 1`, `name of tab 1 of window 1`, and
  `name of terminal 1` all work correctly.
  ```
- [`959c2f5`](https://github.com/ghostty-org/ghostty/commit/959c2f51ac524e6556fe0e8d8b2db9ff090e0dd0) macos: add AppleScript new window command ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a `new window` command to the scripting dictionary and wire it to
  `NSApplication` so AppleScript can create Ghostty windows.
  
  The command returns a scripting `window` object for the created window,
  with a fallback to a direct wrapper when AppKit window ordering has not
  yet refreshed in the current run loop.
  ```
- [`a3adeb0`](https://github.com/ghostty-org/ghostty/commit/a3adeb0166b2dc896045b71f8656b2605648e9c2) macos: use value-style AppleScript surface configuration records ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a `surface configuration` record type to the scripting dictionary,
  implement `new surface configuration` (with optional copy-from), and allow
  `new window` to accept `with configuration`.
  ```
- [`459eaa2`](https://github.com/ghostty-org/ghostty/commit/459eaa2640444b1b434f5508b807afd8f273e151) macos: order AppleScript dictionary definitions ([@mitchellh](https://github.com/mitchellh))
  ```text
  Document the preferred Ghostty.sdef top-level order in AGENTS.md and reorder
  Ghostty Suite definitions to classes, records, enums, then commands.
  ```
- [`4d5de70`](https://github.com/ghostty-org/ghostty/commit/4d5de702f2613ea0130ec83eb7af867e51a9d8a0) macos: allow split command surface configuration ([@mitchellh](https://github.com/mitchellh))
- [`d271c8c`](https://github.com/ghostty-org/ghostty/commit/d271c8ccaab0f08ab0092b2f0893c8e0d0e5283d) macos: add new tab command ([@mitchellh](https://github.com/mitchellh))
- [`28b4e24`](https://github.com/ghostty-org/ghostty/commit/28b4e2495db53c707d4e6616af136eadd1eba393) macos: Add AppleScript commands for window and tab control ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add scripting dictionary commands for activating windows, selecting tabs,
  closing tabs, and closing windows.
  
  Implement the corresponding Cocoa AppleScript command handlers and expose
  minimal ScriptWindow/ScriptTab helpers needed to resolve live targets.
  
  Verified by building Ghostty and running osascript commands against the
  absolute Debug app path to exercise all four new commands.
  ```
- [`25fa581`](https://github.com/ghostty-org/ghostty/commit/25fa58143ec6d8e6eb200b459838f16376423fdf) macos: add macos-applescript config ([@mitchellh](https://github.com/mitchellh))
- [`221a163`](https://github.com/ghostty-org/ghostty/commit/221a1639af6060b485fd2ef214fa260b7aa7ddb1) swiftlint ([@mitchellh](https://github.com/mitchellh))
- [`259a41d`](https://github.com/ghostty-org/ghostty/commit/259a41d503ad24eb9af83dd7f50566cf312ef87a) macos: rename surface config working directory to not be ambiguous ([@mitchellh](https://github.com/mitchellh))
- [`038ebef`](https://github.com/ghostty-org/ghostty/commit/038ebef16cc8cea570f87a95771eb76528935210) address some PR feedback ([@mitchellh](https://github.com/mitchellh))
- [`210b01a`](https://github.com/ghostty-org/ghostty/commit/210b01ad600f0dceff9ff2be1a16bbf6c9fa7f57) macos: use direct parameters for object-targeting commands ([@mitchellh](https://github.com/mitchellh))
  ```text
  Change split, focus, close, activate window, select tab, close tab, and
  close window commands to accept their target object as a direct parameter
  instead of a named parameter. This produces natural AppleScript syntax:
  
    activate window (window 1)
    close tab (tab 1 of window 1)
    split (terminal 1) direction right
  
  instead of the awkward redundant form:
  
    activate window window (window 1)
    close tab tab (tab 1 of window 1)
    split terminal (terminal 1) direction right
  
  The implementation moves command logic from NSScriptCommand subclasses
  into responds-to handler methods on ScriptTerminal, ScriptWindow, and
  ScriptTab, which is the standard Cocoa Scripting pattern for commands
  whose direct parameter is an application class.
  ```
- [`ed9a6cb`](https://github.com/ghostty-org/ghostty/commit/ed9a6cb6488ff282a5061bbd016d9082d7c3e773) macos: implement the quit command ([@mitchellh](https://github.com/mitchellh))
- [`fd3a62b`](https://github.com/ghostty-org/ghostty/commit/fd3a62b9c1712508516bdd18fdaf652929bff4ed) AppleScript ([#11208](https://github.com/ghostty-org/ghostty/issues/11208)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This adds AppleScript support to the macOS app.
  
  AppleScript is still one of the best ways to script macOS apps. It is
  more CLI friendly and share-able than Apple Shortcuts and can be used by
  other CLI programs like editors (Neovim plugins), launchers
  (Raycast/Alfred), etc. It has been heavily requested to introduce more
  scriptability into Ghostty and this is a really good, powerful option on
  macOS.
  
  > [!NOTE]
  >
  > I definitely still want to do something cross-platform and more
  official as a plugin/scripting API for Ghostty. But native integrations
  like this are a goal of Ghostty as well and this implementation is just
  some thin logic over already existing internals to expose it.
  
  I plan on merging this ahead of 1.3. Normally I wouldn't ship a feature
  so late in the game but this is fairly hermetic (doesn't impact other
  systems) and I plan on documenting it as a "preview" feature since the
  API and stability are in question.
  
  ## Security
  
  Apple secures AppleScript via TCC by asking for permission when a script
  is run whether an app is allowed to be controlled. Because this is
  always asked, we do default AppleScript to being enabled. This is
  typical of macOS native applications already.
  
  AppleScript can be wholesale disabled via `macos-applescript = false`.
  
  ## Future
  
  There is a big question of what else to expose to this to make it
  useful. I'm going to make a call to action for the 1.3 cycle to gather
  feedback on this, since we can expose mostly anything!
  
  ## Capabilities
  
  ### Objects
  
  | Object | Key Properties | Key Elements |
  | --- | --- | --- |
  | `application` | `name`, `frontmost`, `version` | `windows`,
  `terminals` |
  | `window` | `id`, `name`, `selected tab` | `tabs`, `terminals` |
  | `tab` | `id`, `name`, `index`, `selected` | `terminals` |
  | `terminal` | `id`, `name`, `working directory` | None |
  
  ### Commands
  
  | Category | Command | Purpose |
  | --- | --- | --- |
  | Application | `perform action` | Execute a Ghostty action string on a
  terminal. |
  | Configuration | `new surface configuration` | Create/copy a reusable
  surface configuration record. |
  | Creation | `new window` | Open a new Ghostty window (optional
  configuration). |
  | Creation | `new tab` | Open a new tab (optional target
  window/configuration). |
  | Layout | `split` | Split a terminal and return the new terminal. |
  | Focus/Selection | `focus` | Focus a terminal. |
  | Focus/Selection | `activate window` | Bring a window to front and
  activate app. |
  | Focus/Selection | `select tab` | Select and foreground a tab. |
  | Lifecycle | `close` | Close a terminal. |
  | Lifecycle | `close tab` | Close a tab. |
  | Lifecycle | `close window` | Close a window. |
  | Input | `input text` | Paste-style text input into terminal. |
  | Input | `send key` | Send key press/release with optional modifiers. |
  | Input | `send mouse button` | Send mouse button press/release. |
  | Input | `send mouse position` | Send mouse position update. |
  | Input | `send mouse scroll` | Send scroll event with
  precision/momentum options. |
  | Standard Suite | `count`, `exists`, `quit` | Standard Cocoa scripting
  functionality. |
  
  ## Examples
  
  ### Layout
  
  ```AppleScript
  -- Tmux-like layout: 4 panes in one tab (2x2), each with a job.
  set projectDir to POSIX path of (path to home folder) & "src/ghostty"
  
  tell application "Ghostty"
      activate
  
      -- Reusable config for all panes.
      set cfg to new surface configuration
      set initial working directory of cfg to projectDir
  
      -- Create the first window/tab + split into 4 panes.
      set win to new window with configuration cfg
      set paneEditor to terminal 1 of selected tab of win
      set paneBuild to split paneEditor direction right with configuration cfg
      set paneGit to split paneEditor direction down with configuration cfg
      set paneLogs to split paneBuild direction down with configuration cfg
  
      -- Seed each pane with a command.
      input text "nvim ." to paneEditor
      send key "enter" to paneEditor
  
      input text "zig build -Demit-macos-app=false" to paneBuild
  
      input text "git status -sb" to paneGit
  
      input text "tail -f /tmp/dev.log" to paneLogs
      send key "enter" to paneLogs
  
      -- Put focus back where you want to type.
      focus paneEditor
  end tell
  ```
  
  ### Broadcast Commands
  
  ```AppleScript
  -- Run one command across every open terminal surface.
  set cmd to "echo sync && date"
  
  tell application "Ghostty"
      set allTerms to terminals
  
      repeat with t in allTerms
          input text cmd to t
          send key "enter" to t
      end repeat
  
      display dialog ("Broadcasted to " & (count of allTerms) & " terminal(s).")
  end tell
  ```
  
  ### Jump by Working Directory
  
  ```applescript
  -- Find the first terminal whose cwd contains this text.
  set needle to "ghostty"
  
  tell application "Ghostty"
      set matches to every terminal whose working directory contains needle
  
      -- Fallback: try title if cwd had no match.
      if (count of matches) = 0 then
          set matches to every terminal whose name contains needle
      end if
  
      if (count of matches) = 0 then
          display dialog ("No terminal matched: " & needle)
      else
          set t to item 1 of matches
          focus terminal t
          input text "echo '[focused by AppleScript]'" to t
          send key "enter" to t
      end if
  end tell
  ```
  ````
- [`af43af1`](https://github.com/ghostty-org/ghostty/commit/af43af13c363e2819763ede819e3279cf778e993) Update VOUCHED list ([#11211](https://github.com/ghostty-org/ghostty/issues/11211)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11209#issuecomment-4016613771)
  from @mitchellh.
  
  Vouch: @04cb
  ```

