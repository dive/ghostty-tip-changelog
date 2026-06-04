> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: June 4, 2026 at 04:31 UTC.

## June 3, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26908961402), [2](https://github.com/ghostty-org/ghostty/actions/runs/26869468488), [3](https://github.com/ghostty-org/ghostty/actions/runs/26864366652)  
Summary: 3 runs • 5 commits • 5 authors

### Changes

- [`5f7738a`](https://github.com/ghostty-org/ghostty/commit/5f7738a0e9fc192c2b8ccbb0da22084bde5dd191) build(deps): bump actions/checkout from 6.0.2 to 6.0.3 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [actions/checkout](https://github.com/actions/checkout) from 6.0.2 to 6.0.3.
  - [Release notes](https://github.com/actions/checkout/releases)
  - [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
  - [Commits](https://github.com/actions/checkout/compare/de0fac2e4500dabe0009e67214ff5f5447ce83dd...df4cb1c069e1874edd31b4311f1884172cec0e10)
  
  ---
  updated-dependencies:
  - dependency-name: actions/checkout
    dependency-version: 6.0.3
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`bfe633a`](https://github.com/ghostty-org/ghostty/commit/bfe633a9487892ff3d27ed727db540267f22ef90) build(deps): bump actions/checkout from 6.0.2 to 6.0.3 ([#12911](https://github.com/ghostty-org/ghostty/issues/12911)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps [actions/checkout](https://github.com/actions/checkout) from 6.0.2
  to 6.0.3.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/actions/checkout/releases">actions/checkout's
  releases</a>.</em></p>
  <blockquote>
  <h2>v6.0.3</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>Update changelog by <a
  href="https://github.com/ericsciple"><code>@​ericsciple</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2357">actions/checkout#2357</a></li>
  <li>fix: expand merge commit SHA regex and add SHA-256 test cases by <a
  href="https://github.com/yaananth"><code>@​yaananth</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2414">actions/checkout#2414</a></li>
  <li>Fix checkout init for SHA-256 repositories by <a
  href="https://github.com/yaananth"><code>@​yaananth</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2439">actions/checkout#2439</a></li>
  <li>Update changelog for v6.0.3 by <a
  href="https://github.com/yaananth"><code>@​yaananth</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/2446">actions/checkout#2446</a></li>
  </ul>
  <h2>New Contributors</h2>
  <ul>
  <li><a href="https://github.com/yaananth"><code>@​yaananth</code></a>
  made their first contribution in <a
  href="https://redirect.github.com/actions/checkout/pull/2414">actions/checkout#2414</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/actions/checkout/compare/v6...v6.0.3">https://github.com/actions/checkout/compare/v6...v6.0.3</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/actions/checkout/blob/main/CHANGELOG.md">actions/checkout's
  changelog</a>.</em></p>
  <blockquote>
  <h1>Changelog</h1>
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
  <h2>v4.2.0</h2>
  <ul>
  <li>Add Ref and Commit outputs by <a
  href="https://github.com/lucacome"><code>@​lucacome</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/1180">actions/checkout#1180</a></li>
  <li>Dependency updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>- <a
  href="https://redirect.github.com/actions/checkout/pull/1777">actions/checkout#1777</a>,
  <a
  href="https://redirect.github.com/actions/checkout/pull/1872">actions/checkout#1872</a></li>
  </ul>
  <h2>v4.1.7</h2>
  <ul>
  <li>Bump the minor-npm-dependencies group across 1 directory with 4
  updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/1739">actions/checkout#1739</a></li>
  <li>Bump actions/checkout from 3 to 4 by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/1697">actions/checkout#1697</a></li>
  <li>Check out other refs/* by commit by <a
  href="https://github.com/orhantoy"><code>@​orhantoy</code></a> in <a
  href="https://redirect.github.com/actions/checkout/pull/1774">actions/checkout#1774</a></li>
  </ul>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/actions/checkout/commit/df4cb1c069e1874edd31b4311f1884172cec0e10"><code>df4cb1c</code></a>
  Update changelog for v6.0.3 (<a
  href="https://redirect.github.com/actions/checkout/issues/2446">#2446</a>)</li>
  <li><a
  href="https://github.com/actions/checkout/commit/1cce3390c2bfda521930d01229c073c7ff920824"><code>1cce339</code></a>
  Fix checkout init for SHA-256 repositories (<a
  href="https://redirect.github.com/actions/checkout/issues/2439">#2439</a>)</li>
  <li><a
  href="https://github.com/actions/checkout/commit/900f2210b1d28bbbd0bd22d17926b9e224e8f231"><code>900f221</code></a>
  fix: expand merge commit SHA regex and add SHA-256 test cases (<a
  href="https://redirect.github.com/actions/checkout/issues/2414">#2414</a>)</li>
  <li><a
  href="https://github.com/actions/checkout/commit/0c366fd6a839edf440554fa01a7085ccba70ac98"><code>0c366fd</code></a>
  Update changelog (<a
  href="https://redirect.github.com/actions/checkout/issues/2357">#2357</a>)</li>
  <li>See full diff in <a
  href="https://github.com/actions/checkout/compare/de0fac2e4500dabe0009e67214ff5f5447ce83dd...df4cb1c069e1874edd31b4311f1884172cec0e10">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=actions/checkout&package-manager=github_actions&previous-version=6.0.2&new-version=6.0.3)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`ef68e96`](https://github.com/ghostty-org/ghostty/commit/ef68e96400fd8811b786c2b0e9ab49692eae8bab) macos: fix GHOSTTY_QUICK_TERMINAL not set for quick terminal splits (YuWiz)
- [`4df593b`](https://github.com/ghostty-org/ghostty/commit/4df593bd24675b0f0e14add31825dc8b184cf724) macos: fix GHOSTTY_QUICK_TERMINAL not set for quick terminal splits ([#12896](https://github.com/ghostty-org/ghostty/issues/12896)) ([@bo2themax](https://github.com/bo2themax))
- [`629838b`](https://github.com/ghostty-org/ghostty/commit/629838b9bd050b4708bdd162c115b58874646b34) Update VOUCHED list ([#12906](https://github.com/ghostty-org/ghostty/issues/12906)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12905#discussioncomment-17160340)
  from @jcollie.
  
  Vouch: @c0x0o
  ```

## June 2, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26822901695)  
Summary: 1 runs • 3 commits • 2 authors

### Changes

- [`ab82b8a`](https://github.com/ghostty-org/ghostty/commit/ab82b8ab720ce46183a58a55554e4a4a7423e3f5) core: fix use-after-free in Surface.setSelection ([@jparise](https://github.com/jparise))
  ```text
  setSelection captured the previous selection, then called Screen.select
  (which deinits the previous selection's tracked pins), then compared the
  new selection against the now-freed previous pin via `sel.eql(prev)`.
  That read freed pin memory (use-after-free).
  
  The comparison was a copy-on-select optimization ("only re-copy if the
  selection changed"). Remove it rather than repair it because:
  
  - It never fired correctly. It compared against freed memory, so the
    shipped behavior was already "always copy".
  
  - It can't be repaired by copying `prev`'s pin before Screen.select.
    That fixes the use-after-free but not the logic: the call sites (e.g.
    mouse drag release) pass a selection equal to the one already set, so
    a working `eql` skip would suppress the very copy those sites exist to
    perform. A correct optimization would have to compare against the
    last-copied selection (before the mouse event mutated the live one),
    which would require extra state.
  
  - It isn't worth tracking that additional state. The copy runs once per
    selection gesture (mouse up, double-click), which isn't in a hot path,
    so skipping a redundant re-copy only saves a single clipboard write.
  
  Removing the skip eliminates the use-after-free and keeps the behavior
  consistent with what we've already been doing.
  ```
- [`76b9bdb`](https://github.com/ghostty-org/ghostty/commit/76b9bdb1999398fa1b64d000f9a77088af232b62) terminal: test Screen.select frees existing pins ([@jparise](https://github.com/jparise))
- [`6246c28`](https://github.com/ghostty-org/ghostty/commit/6246c288ae1087c8d67f75432a59da004b30bf25) core: fix use-after-free in Surface.setSelection ([#12894](https://github.com/ghostty-org/ghostty/issues/12894)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `setSelection` captured the previous selection, then called
  `Screen.select` (which deinits the previous selection's tracked pins),
  then compared the new selection against the now-freed previous pin via
  `sel.eql(prev)`. That read freed pin memory (use-after-free).
  
  The comparison was a copy-on-select optimization ("only re-copy if the
  selection changed"). Remove it rather than repair it because:
  
  - It never fired correctly. It compared against freed memory, so the
  shipped behavior was already "always copy".
  
  - It can't be repaired by copying `prev`'s pin before `Screen.select`.
  That fixes the use-after-free but not the logic: the call sites (e.g.
  mouse drag release) pass a selection equal to the one already set, so a
  working `eql` skip would suppress the very copy those sites exist to
  perform. A correct optimization would have to compare against the
  last-copied selection (before the mouse event mutated the live one),
  which would require extra state.
  
  - It isn't worth tracking that additional state. The copy runs once per
  selection gesture (mouse up, double-click), which isn't in a hot path,
  so skipping a redundant re-copy only saves a single clipboard write.
  
  Removing the skip eliminates the use-after-free and keeps the behavior
  consistent with what we've already been doing.
  
  ---
  
  _AI Disclosure_: Claude Opus 4.8 found this in a review while I was
  working on adjacent code.
  ```

## June 1, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26773386588), [2](https://github.com/ghostty-org/ghostty/actions/runs/26770642732)  
Summary: 2 runs • 13 commits • 7 authors

### Changes

- [`d3775d1`](https://github.com/ghostty-org/ghostty/commit/d3775d1ed0a2e41ee8f2ecdb325f6c016b2b3e93) terminal: glyph protocol parser and response encoder ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds the core parse/encode for the still in-development and experimental
  terminal glyph protocol: https://github.com/raphamorim/rio/pull/1542
  Up to version 1.9.
  
  The only cross-cutting change necessary was changing the APC
  identification logic which previously only looked at a single byte to
  support multi-byte identifiers since the glyph protocol uses `25a1`.
  ```
- [`5758e14`](https://github.com/ghostty-org/ghostty/commit/5758e149319d244cbf2d21d1ae8d1376adaf1f91) terminal: glyph protocol parser and response encoder ([#12352](https://github.com/ghostty-org/ghostty/issues/12352)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  **Important: this DOES NOT hook up the glyph protocol to Ghostty or
  libghostty. Its just the parser.**
  
  This adds the core parse/encode for the still in-development and
  experimental terminal glyph protocol:
  https://github.com/raphamorim/rio/pull/1542
  
  The only cross-cutting change necessary was changing the APC
  identification logic which previously only looked at a single byte to
  support multi-byte identifiers since the glyph protocol uses `25a1`.
  
  For DoS protection, the default limits any glyph-related APC command
  size to 1 megabyte.
  
  > [!WARNING]
  >
  > Since this protocol is still in development and discussion, there is
  no promise the implementation will stay within Ghostty or that any of
  the APIs exposed by this will remain stable. We're just getting ahead of
  it.
  ```
- [`024880b`](https://github.com/ghostty-org/ghostty/commit/024880b9ca40ecf8a399deff14e422dd32746f68) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`33adb58`](https://github.com/ghostty-org/ghostty/commit/33adb58bee9eeca906e29ee957140275d4903257) macos: remove unneeded initializers ([@jparise](https://github.com/jparise))
  ```text
  These will be automatically synthesized (they only do memberwise
  initialization) and do not need to be manually defined.
  ```
- [`e32d7ab`](https://github.com/ghostty-org/ghostty/commit/e32d7abe6eeae9c3aa557fef2bcfe97a212688c5) macos: fix swiftlint opening_brace issue ([@jparise](https://github.com/jparise))
- [`3e83a54`](https://github.com/ghostty-org/ghostty/commit/3e83a54d08ef4f4820b8a401910c838f4f0636e0) macos: remove unneeded initializers ([#12875](https://github.com/ghostty-org/ghostty/issues/12875)) ([@bo2themax](https://github.com/bo2themax))
  ```text
  These will be automatically synthesized (they only do memberwise
  initialization) and do not need to be manually defined.
  ```
- [`eb5c1c7`](https://github.com/ghostty-org/ghostty/commit/eb5c1c7220121c8616160e10cb1aa664166a06f3) fix(macos): mark Swift os.Logger interpolations as public ([@claude](https://github.com/claude))
- [`a181c38`](https://github.com/ghostty-org/ghostty/commit/a181c386ca938f730c6e802b7931b37ec65f3047) config: fix missing space in docs ([@masterflitzer](https://github.com/masterflitzer))
  ```text
  fixes #12873
  
  comment/docs only change:
  switched space and tab in default value of `selection-word-chars`
  so there is no space at the value boundary
  needed because markdown trims spaces at the beginning & end
  of a code snippet
  ```
- [`c4c9e94`](https://github.com/ghostty-org/ghostty/commit/c4c9e945aefbd0afbfc21a05f76d06e36e10a625) Update VOUCHED list ([#12880](https://github.com/ghostty-org/ghostty/issues/12880)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12879#issuecomment-4587359428)
  from @00-kat.
  
  Vouch: @masterflitzer
  ```
- [`16f2fdc`](https://github.com/ghostty-org/ghostty/commit/16f2fdc90c2ca59ed870c7b3355a337b1fd650b2) config: fix missing space in docs ([#12879](https://github.com/ghostty-org/ghostty/issues/12879)) ([@jcollie](https://github.com/jcollie))
  ```text
  fixes #12873
  
  comment/docs only change:
  switched space and tab in default value of `selection-word-chars` so
  there is no space at the value boundary
  needed because markdown trims spaces at the beginning & end of a code
  snippet
  ```
- [`0f7cd84`](https://github.com/ghostty-org/ghostty/commit/0f7cd84b880b203c98683e520e84b9db0c5938d8) Update VOUCHED list ([#12889](https://github.com/ghostty-org/ghostty/issues/12889)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12840#discussioncomment-17132417)
  from @bo2themax.
  
  Vouch: @52dyd
  ```
- [`b81670f`](https://github.com/ghostty-org/ghostty/commit/b81670f3f439eff8df615257ff70d9ef39e60065) macOS: mark Swift os.Logger interpolations as public ([#12877](https://github.com/ghostty-org/ghostty/issues/12877)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ### AI Disclosure
  
  Claude implemented it. I'm fully aware of and confident about the
  change; it's just chore work actually.
  ```
- [`43e0340`](https://github.com/ghostty-org/ghostty/commit/43e03401758e8e1e0d23afb3a8e2a00b43e8e8ee) Update iTerm2 colorschemes ([#12867](https://github.com/ghostty-org/ghostty/issues/12867)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260525-155808-7335c0a
  ```

## May 30, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26674005784)  
Summary: 1 runs • 6 commits • 3 authors

### Changes

- [`37997f8`](https://github.com/ghostty-org/ghostty/commit/37997f8dbe1221f19343e6b9fa907ce2b944f1a2) Use a timeout callback to wait for changes in window active state to settle. Depending on the backend a window might temporarily become inactive. ([@dkinzler](https://github.com/dkinzler))
  ```text
  Fixes an issue where quick-terminal would disappear when opening the surface context menu.
  ```
- [`1753d57`](https://github.com/ghostty-org/ghostty/commit/1753d57bfdf0ac694ac624e7d63ec9fecd220bc6) remove timeout source when window is disposed ([@dkinzler](https://github.com/dkinzler))
- [`ff963f3`](https://github.com/ghostty-org/ghostty/commit/ff963f3119bffbd9366a5b7d98fbcaba06fc9f05) Renamed timeout source and callback function. Added comment explaining timeout delay. ([@dkinzler](https://github.com/dkinzler))
- [`c09ade2`](https://github.com/ghostty-org/ghostty/commit/c09ade225acb0abfea2f845197b227086a76922f) agents: symlink CLAUDE.md to AGENTS.md ([@Uzaaft](https://github.com/Uzaaft))
- [`c4eba3d`](https://github.com/ghostty-org/ghostty/commit/c4eba3da38c629dbd4b8f770da3e0c605f2a7f53) agents: symlink CLAUDE.md to AGENTS.md ([#12861](https://github.com/ghostty-org/ghostty/issues/12861)) ([@jcollie](https://github.com/jcollie))
  ```text
  Claude code [doesn't support AGENTS.md
  files](https://github.com/anthropics/claude-code/issues/6235) so I've
  seen lots of repos symlinking
  ```
- [`2c62d18`](https://github.com/ghostty-org/ghostty/commit/2c62d182cec246764ff725096a70b9ef44996f7f) gtk: fix context menu hiding quick-terminal ([#12843](https://github.com/ghostty-org/ghostty/issues/12843)) ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes #12783 where opening the context menu (with right click) inside
  the quick-terminal will hide the quick-terminal if autohide is enabled.
  
  The cause of this issue is the quick-terminal window becoming inactive
  and immediately active again when you open the context-menu. When the
  window becomes inactive, the autohide feature hides the quick-terminal.
  The temporary focus loss in GTK is triggered by GDK focus change events,
  which probably originate from the windowing backend treating the context
  menu as its own window. Whereas in GTK the context menu is not a
  separate window but instead part of the widget tree of the window it was
  opened from, so even when the context menu has focus that window is
  still the active one in GTK.
  
  As a fix `Window.propIsActive`, which implements the autohide logic,
  will now do its work from a timeout callback, since there is probably no
  reliable way to distinguish a temporary focus loss from a real one from
  inside GTK and I'm not sure we can make any assumptions about the timing
  of things happening in the windowing backend. A 100ms delay should be
  long enough for the focus state to settle while still hiding the
  quick-terminal quickly.
  
  I reproduced the bug and verified the fix on Wayland with both Hyprland
  and KDE. Temporary focus loss happens on X11+KDE as well, although it
  doesn't matter there because there is no quick-terminal.
  
  ### AI Disclosure
  
  No AI was used, code and comments were written by myself.
  ```

## May 29, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/26641829987)  
Summary: 1 runs • 2 commits • 2 authors

### Changes

- [`b771a3d`](https://github.com/ghostty-org/ghostty/commit/b771a3d4f1a2087ec5938e4a653c6926775caf5b) libghostty-vt: preserve shell prompts on resize by default ([@noib3](https://github.com/noib3))
  ```text
  This PR makes libghostty-vt preserve shell prompts across resize unless
  the shell explicitly opts into prompt clearing/redraw with `redraw=1`.
  ```
- [`9017595`](https://github.com/ghostty-org/ghostty/commit/90175950d5004382abd3b0b9528e7be81b0b52ec) libghostty-vt: preserve shell prompts on resize by default ([#12653](https://github.com/ghostty-org/ghostty/issues/12653)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This PR makes libghostty-vt preserve shell prompts across resize unless
  the shell explicitly opts into prompt clearing/redraw with `redraw=1`.
  ```

