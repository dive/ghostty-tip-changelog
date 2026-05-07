> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: May 7, 2026 at 18:34 UTC.

## May 7, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/25486122457)  
Summary: 1 runs • 1 commits • 1 authors

### Changes

- [`063ac3e`](https://github.com/ghostty-org/ghostty/commit/063ac3ecc5adae6360ae2044dc54e7a68c64f3a1) Update VOUCHED list ([#12613](https://github.com/ghostty-org/ghostty/issues/12613)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12612#issuecomment-4395645191)
  from @trag1c.
  
  Vouch: @raphamorim
  ```

## May 6, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/25466794168)  
Summary: 1 runs • 1 commits • 1 authors

### Changes

- [`0deaac0`](https://github.com/ghostty-org/ghostty/commit/0deaac08ed1a95330346afabbad03da701708331) Update VOUCHED list ([#12606](https://github.com/ghostty-org/ghostty/issues/12606)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12604#issuecomment-4392933026)
  from @jcollie.
  
  Vouch: @mohshami
  ```

## May 5, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/25368075621), [2](https://github.com/ghostty-org/ghostty/actions/runs/25357894222)  
Summary: 2 runs • 7 commits • 5 authors

### Changes

- [`248df8e`](https://github.com/ghostty-org/ghostty/commit/248df8e7aadeca395007857dd7f82d4505ace6a6) docs(input): document copy_to_clipboard arguments ([@claude](https://github.com/claude))
- [`b1b0174`](https://github.com/ghostty-org/ghostty/commit/b1b01741f6c0d694bb9e19daa1a77874676a84ea) docs(input): document navigate_search arguments ([@claude](https://github.com/claude))
- [`df44c6d`](https://github.com/ghostty-org/ghostty/commit/df44c6dd8344544d614e4dbf121b60e7149244db) docs(input): document close_tab arguments ([@claude](https://github.com/claude))
- [`5874ce6`](https://github.com/ghostty-org/ghostty/commit/5874ce633c8e49a4b1bf38c336e1196c735f83cb) Apply suggestions from code review ([@bo2themax](https://github.com/bo2themax))
- [`f9a9d33`](https://github.com/ghostty-org/ghostty/commit/f9a9d33b3a40a95ba01cfbc0f89586567932a22b) docs(input): add documentation for missing action parameters ([#12579](https://github.com/ghostty-org/ghostty/issues/12579)) ([@00-kat](https://github.com/00-kat))
  ```text
  ### AI Disclosure
  
  Claude generated all the commits, I reviewed it and created this PR
  ```
- [`81e399c`](https://github.com/ghostty-org/ghostty/commit/81e399c4124ba8647e547eb3638af0220fdf6bdb) build(deps): bump cachix/install-nix-action from 31.10.5 to 31.10.6 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [cachix/install-nix-action](https://github.com/cachix/install-nix-action) from 31.10.5 to 31.10.6.
  - [Release notes](https://github.com/cachix/install-nix-action/releases)
  - [Changelog](https://github.com/cachix/install-nix-action/blob/master/RELEASE.md)
  - [Commits](https://github.com/cachix/install-nix-action/compare/ab739621df7a23f52766f9ccc97f38da6b7af14f...8aa03977d8d733052d78f4e008a241fd1dbf36b3)
  
  ---
  updated-dependencies:
  - dependency-name: cachix/install-nix-action
    dependency-version: 31.10.6
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`ac48a9b`](https://github.com/ghostty-org/ghostty/commit/ac48a9b15bd533a676f6ea9549ac122feb955249) build(deps): bump cachix/install-nix-action from 31.10.5 to 31.10.6 ([#12584](https://github.com/ghostty-org/ghostty/issues/12584)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [cachix/install-nix-action](https://github.com/cachix/install-nix-action)
  from 31.10.5 to 31.10.6.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/cachix/install-nix-action/releases">cachix/install-nix-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v31.10.6</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>nix: 2.34.6 -&gt; 2.34.7 by <a
  href="https://github.com/github-actions"><code>@​github-actions</code></a>[bot]
  in <a
  href="https://redirect.github.com/cachix/install-nix-action/pull/275">cachix/install-nix-action#275</a>
  <strong><a
  href="https://github.com/NixOS/nix/security/advisories/GHSA-vh5x-56v6-4368">GHSA-vh5x-56v6-4368</a></strong>:
  Fixes a coroutine stack-to-heap overflow via unbounded recursion in the
  NAR directory parser. <strong>Severity: High.</strong>
  <strong><a
  href="https://github.com/NixOS/nix/security/advisories/GHSA-gr92-w2r5-qw5p">GHSA-gr92-w2r5-qw5p</a></strong>:
  Fixes an absolute path traversal vulnerability when unpacking archives
  to disk. Severity: Moderate.</li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/cachix/install-nix-action/compare/v31...v31.10.6">https://github.com/cachix/install-nix-action/compare/v31...v31.10.6</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/8aa03977d8d733052d78f4e008a241fd1dbf36b3"><code>8aa0397</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/install-nix-action/issues/275">#275</a>
  from cachix/create-pull-request/patch</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/21d0b780f08a47ae2baf9814c722ef3884db92aa"><code>21d0b78</code></a>
  nix: 2.34.6 -&gt; 2.34.7</li>
  <li>See full diff in <a
  href="https://github.com/cachix/install-nix-action/compare/ab739621df7a23f52766f9ccc97f38da6b7af14f...8aa03977d8d733052d78f4e008a241fd1dbf36b3">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=cachix/install-nix-action&package-manager=github_actions&previous-version=31.10.5&new-version=31.10.6)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## May 4, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/25344940935)  
Summary: 1 runs • 4 commits • 2 authors

### Changes

- [`28767f6`](https://github.com/ghostty-org/ghostty/commit/28767f62b18fa553ed681efd4acf2780e8c2196e) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`c20fcfa`](https://github.com/ghostty-org/ghostty/commit/c20fcfa1b487ab8a8402b773c19faa3d84a8beac) Fix zero-width grapheme attachment during pending wrap ([@noib3](https://github.com/noib3))
  ```text
  This PR fixes an issue where a zero-width combining mark could attach to
  the wrong cell when the preceding character was written in the final
  column and the cursor had a pending wrap.
  ```
- [`c2c0901`](https://github.com/ghostty-org/ghostty/commit/c2c0901ed063e695f35f84232f5333d83db2ab8d) Update iTerm2 colorschemes ([#12562](https://github.com/ghostty-org/ghostty/issues/12562)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260427-153600-5e4d1de
  ```
- [`563b085`](https://github.com/ghostty-org/ghostty/commit/563b085a4d623995663b320818b6088ba0f2588f) Fix zero-width grapheme attachment during pending wrap ([#12581](https://github.com/ghostty-org/ghostty/issues/12581)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This PR fixes an issue where a zero-width combining mark could attach to
  the wrong cell when the preceding character was written in the final
  column and the cursor had a pending wrap.
  
  The test I added used to fail before the fix, but it passes now.
  ```

## May 3, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/25267280551)  
Summary: 1 runs • 1 commits • 1 authors

### Changes

- [`1547dd6`](https://github.com/ghostty-org/ghostty/commit/1547dd667ab6d1f4ebcdc7282adc54c95752ee67) Update VOUCHED list ([#12564](https://github.com/ghostty-org/ghostty/issues/12564)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12563#discussioncomment-16793038)
  from @jcollie.
  
  Vouch: @agoodkind
  ```

## May 2, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/25255420939), [2](https://github.com/ghostty-org/ghostty/actions/runs/25240925859)  
Summary: 2 runs • 8 commits • 4 authors

### Changes

- [`d60a16c`](https://github.com/ghostty-org/ghostty/commit/d60a16c1465415cedf7154d1fd4ad44ca66c3ebe) macos: avoid replaying keys that commit preedit ([@knu](https://github.com/knu))
  ```text
  Refs #10460
  Related: #12518
  
  When an input method commits all or part of marked text during keyDown,
  AppKit returns the committed text through insertText. Treat that as
  text committed by the input method instead of replaying the original key
  event to the terminal.
  
  Previously this path only handled arrow-key commits specially. A
  control-key shortcut that commits preedit text could still be encoded as
  the original control input after composition, such as ctrl+j becoming LF.
  
  Send committed preedit text as a text-only event for any key that causes
  the commit. Only replay arrow navigation keys that the existing Korean
  IME handling expects, and keep plain left-arrow suppressed because AppKit
  already leaves the caret in place.
  
  AI usage: OpenAI Codex helped investigate, implement, test, and refine
  this change. I reviewed and tested the resulting code.
  ```
- [`a971bf1`](https://github.com/ghostty-org/ghostty/commit/a971bf16a0152c31f20001864a196f24e117a731) libghostty-vt: support building nix derivation on darwin ([@sandydoo](https://github.com/sandydoo))
- [`9df670c`](https://github.com/ghostty-org/ghostty/commit/9df670cb557e4dde7870fe551a472ddf2feb2bcc) build: skip unnecessary steps for libghostty-vt ([@sandydoo](https://github.com/sandydoo))
- [`d17e551`](https://github.com/ghostty-org/ghostty/commit/d17e5517c7d1b38d78811801285a38ced8c6fe5a) libghostty-vt: fix dependency path resolution errors ([@sandydoo](https://github.com/sandydoo))
  ```text
  Zigs build infra computes relatives paths to build-time executables that use `setCwd.`
  The logic is purely lexical and doesn't take into account symlinks, unlike `chdir` that follows symlinks.
  
  If the `cwd` resolves to a different depth, then the relative path becomes incorrect.
  ```
- [`7123bdd`](https://github.com/ghostty-org/ghostty/commit/7123bddc184e4c96caa7705b319609f07534359d) libghostty-vt: fix linker tests for darwin ([@sandydoo](https://github.com/sandydoo))
- [`058d054`](https://github.com/ghostty-org/ghostty/commit/058d054fa24478a19a6b71fb2e1977f084d0ff12) libghostty-vt: support building on macOS with Nix ([#12548](https://github.com/ghostty-org/ghostty/issues/12548)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Adds support for building libghostty-vt on macOS with Nix.
  
  Tested on aarch64-darwin. Tests pass as well.
  
  _Claude used to speed up debugging process. All comments, commit
  messages, and final code authored by me._
  ```
- [`f0bb6ed`](https://github.com/ghostty-org/ghostty/commit/f0bb6ed9eee5271cbbcee7b87d252830b90fb719) macos: avoid replaying keys that commit preedit ([#12547](https://github.com/ghostty-org/ghostty/issues/12547)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Refs #10460
  Related: #12518
  
  When an input method commits all or part of marked text during keyDown,
  AppKit returns the committed text through insertText. Treat that as text
  committed by the input method instead of replaying the original key
  event to the terminal.
  
  Previously this path only handled arrow-key commits specially. A
  control-key shortcut that commits preedit text could still be encoded as
  the original control input after composition, such as ctrl+j becoming
  LF.
  
  Send committed preedit text as a text-only event for any key that causes
  the commit. Only replay arrow navigation keys that the existing Korean
  IME handling expects, and keep plain left-arrow suppressed because
  AppKit already leaves the caret in place.
  
  Before:
  <img width="375" height="375" alt="before"
  src="https://github.com/user-attachments/assets/1073b93f-625a-4881-8f95-67adefe9d3da"
  />
  
  After:
  <img width="375" height="375" alt="after"
  src="https://github.com/user-attachments/assets/3e4be2a5-4df9-4cdd-bc95-e178ca44c7e7"
  />
  
  AI usage: OpenAI Codex helped investigate, implement, test, and refine
  this change. I reviewed and tested the resulting code.
  ```
- [`f27aa86`](https://github.com/ghostty-org/ghostty/commit/f27aa865af5a8f33178d68ef9d9f30b05ba74036) Update VOUCHED list ([#12552](https://github.com/ghostty-org/ghostty/issues/12552)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12542#discussioncomment-16785276)
  from @00-kat.
  
  Denounce: @MorgenGeluk
  ```

## May 1, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/25212984448)  
Summary: 1 runs • 1 commits • 1 authors

### Changes

- [`35c0e25`](https://github.com/ghostty-org/ghostty/commit/35c0e2572fe6f3ca142d2af92f3a22c411e1e16b) Update VOUCHED list ([#12545](https://github.com/ghostty-org/ghostty/issues/12545)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12544#issuecomment-4359105411)
  from @trag1c.
  
  Vouch: @erral
  ```

