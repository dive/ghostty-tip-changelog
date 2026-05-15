> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: May 15, 2026 at 18:33 UTC.

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

## May 10, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/25630689955)  
Summary: 1 runs • 1 commits • 1 authors

### Changes

- [`ce6a00b`](https://github.com/ghostty-org/ghostty/commit/ce6a00bfbfc7f0fed25e9385ac9100f7b4b0e098) Update VOUCHED list ([#12647](https://github.com/ghostty-org/ghostty/issues/12647)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12644#issuecomment-4415471290)
  from @jcollie.
  
  Denounce: @f1813483-netizen
  ```

## May 9, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/25609668241), [2](https://github.com/ghostty-org/ghostty/actions/runs/25606064691), [3](https://github.com/ghostty-org/ghostty/actions/runs/25604916760)  
Summary: 3 runs • 8 commits • 5 authors

### Changes

- [`2b48045`](https://github.com/ghostty-org/ghostty/commit/2b480457316b3b21739d3ed26b301e456f5856c7) macos: simplify workingDirectory setter ([@jparise](https://github.com/jparise))
  ```text
  This is a minor improvement to the computed property's `set` logic: we
  can just use `.map {}` to unify the two optional paths.
  ```
- [`e3e9b51`](https://github.com/ghostty-org/ghostty/commit/e3e9b51b79c538c3f70a49e4dbda02ccb3cab731) macos: simplify workingDirectory setter ([#12639](https://github.com/ghostty-org/ghostty/issues/12639)) ([@jparise](https://github.com/jparise))
  ```text
  This is a minor improvement to the computed property's `set` logic: we
  can just use `.map {}` to unify the two optional paths.
  ```
- [`cbd43fd`](https://github.com/ghostty-org/ghostty/commit/cbd43fd4834a7969480866c037f8650ca0912a25) feature: add basque translation ([@erral](https://github.com/erral))
- [`afb8fc7`](https://github.com/ghostty-org/ghostty/commit/afb8fc7eb3042196b7e1d0fb5ec0eb0601efaf85) Update po/eu.po ([@erral](https://github.com/erral))
- [`ec145bc`](https://github.com/ghostty-org/ghostty/commit/ec145bca9f1b24df3c6c8321892e60fb68f05c3d) Fix translation errors in eu ([@erral](https://github.com/erral))
- [`a330ee9`](https://github.com/ghostty-org/ghostty/commit/a330ee93e8cb01844a4442eb692ac1769ab1d35d) i18n: add Basque (eu) translation ([#12544](https://github.com/ghostty-org/ghostty/issues/12544)) ([@00-kat](https://github.com/00-kat))
  ```text
  Same as with icelandic (#12301) we may be even fewer than them but let's
  have this translated into Basque.
  
  I also volunteer for the basque translation team.
  ```
- [`607152e`](https://github.com/ghostty-org/ghostty/commit/607152ec6d2487ab10fb1cf5de6e0519baf8a21b) macOS: normalize working directory paths with FilePath ([@bo2themax](https://github.com/bo2themax))
  ```text
  This fixes for nuShell when opening Ghostty via Finder service and Shortcuts, also makes path parsing more robust in AppleScript.
  ```
- [`4bd8fa1`](https://github.com/ghostty-org/ghostty/commit/4bd8fa1e3e7a9538ad0b2433c2ddabeaa051eedc) macOS: normalize working directory paths with FilePath ([#12614](https://github.com/ghostty-org/ghostty/issues/12614)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This fixes for
  [Nushell](https://github.com/nushell/nushell/blob/f342d8acfa81bd9543bb38e3e08b1a93ecafe5d1/crates/nu-protocol/src/engine/engine_state.rs#L1012)
  when opening Ghostty via Finder service and Shortcuts, also makes path
  parsing more robust in AppleScript.
  
  <img width="976" height="690" alt="image"
  src="https://github.com/user-attachments/assets/d3c19481-39ce-4797-ba31-d431af16651d"
  />
  ```

