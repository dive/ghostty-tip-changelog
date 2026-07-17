> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: July 17, 2026 at 18:59 UTC.

## July 17, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/29602269436), [2](https://github.com/ghostty-org/ghostty/actions/runs/29600718239), [3](https://github.com/ghostty-org/ghostty/actions/runs/29586962822)  
Summary: 3 runs • 7 commits • 3 authors

### Changes

- [`89b103d`](https://github.com/ghostty-org/ghostty/commit/89b103dd5ec669318de53fa361195d155b9e7155) terminal: more full featured resize (cell geo, sync rendering, etc.) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This makes the Terminal.resize handle more of the common elements that
  a core terminal emulator should: cell geoemtry handling (if exists),
  updates synchronized output modes.
  
  This adds a new TerminalStream.resize that also handles the side effects
  for more easy integration into downstream libghostty-vt consumers, namely
  mode 2048 in-band signaling handling.
  ```
- [`dde3d4d`](https://github.com/ghostty-org/ghostty/commit/dde3d4d6b05338e1860a7c45fd17990a6d634e8b) terminal: screen resize failures are now safe ([@mitchellh](https://github.com/mitchellh))
- [`a3c1cab`](https://github.com/ghostty-org/ghostty/commit/a3c1caba545e7894b21fa359701d245b82b82083) terminal: resize failures are now almost fully safe ([@mitchellh](https://github.com/mitchellh))
  ```text
  Terminal resize could leave tab stops, pixel geometry, synchronized output,
  or screen dimensions partially updated when a later allocation failed. This
  is now safe. There is one exception, see the code comments.
  ```
- [`d7e9773`](https://github.com/ghostty-org/ghostty/commit/d7e9773329ae86e6117c9ab5b6531367ac8c530a) terminal: make resize handling error-safe, handle more logic ([#13367](https://github.com/ghostty-org/ghostty/issues/13367)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This makes error returns in `Screen.resize` and `Terminal.resize` safe:
  they leave the terminal/screen in its prior state (with one exception,
  noted below). Previously, both were documented as leaving the terminal
  in a garbage stage on error.
  
  Unit tests with tripwire added to verify errdefer behaviors.
  
  This also includes a refactor: the common behaviors that resize needs
  such as updating cell size in pixels, disabling synchronized output,
  handling mode 2048, are now pulled into libghostty-vt. This will make it
  easier for downstream libghostty users to make proper terminals.
  
  **The one perfect undo exception:** If the primary screen can resize but
  the alt screen cannot, then we try our best to do something reasonable,
  in order:
  
  1. If we're on the primary screen, we just deallocate the alt screen.
  It'll be reallocated lazily (and may fail) in the future. Worst case
  here is we lose screen data if the future TUI doesn't expect a clear on
  enter/exit.
  
  2. If we're on the alt screen, we deallocate to try recover memory, then
  reinitialize eagerly at the new size hoping to at least have a blank alt
  screen. Similar to 1, we lose screen data here, but its likely screen
  data that mattered since we were actively on the alt screen.
  
  3. If the eager reinit fails, we switch to the primary screen. This is
  the biggest issue, cause the TUI program won't know this happened and
  probably do some crazy stuff on the primary screen. But, its also a
  super exceptional situation.
  
  In every case though, the terminal is consistent and safe to use.
  
  **LLM notes:** Only used as a judge and to assist with test writing, not
  used at all for commit messages, PR, or non-test logic.
  ```
- [`f21d376`](https://github.com/ghostty-org/ghostty/commit/f21d37688368be95b0ee57674f30e9af9376f40b) Update VOUCHED list ([#13368](https://github.com/ghostty-org/ghostty/issues/13368)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13366#discussioncomment-17675218)
  from @jcollie.
  
  Vouch: @AprilNEA
  ```
- [`0f0ede8`](https://github.com/ghostty-org/ghostty/commit/0f0ede81d5950f7889dccde07a450d162ffd6e7c) build(deps): bump namespacelabs/nscloud-cache-action from 1.6.0 to 1.6.1 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [namespacelabs/nscloud-cache-action](https://github.com/namespacelabs/nscloud-cache-action) from 1.6.0 to 1.6.1.
  - [Release notes](https://github.com/namespacelabs/nscloud-cache-action/releases)
  - [Commits](https://github.com/namespacelabs/nscloud-cache-action/compare/58bf6e08898e88803c098e2b522668541cd3b2e3...c5f8dab7560444c4bf8dbc64f1b203431873c547)
  
  ---
  updated-dependencies:
  - dependency-name: namespacelabs/nscloud-cache-action
    dependency-version: 1.6.1
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`e9ffb25`](https://github.com/ghostty-org/ghostty/commit/e9ffb2579d71185ad25926fb6122e5f388454dcf) build(deps): bump namespacelabs/nscloud-cache-action from 1.6.0 to 1.6.1 ([#13361](https://github.com/ghostty-org/ghostty/issues/13361)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [namespacelabs/nscloud-cache-action](https://github.com/namespacelabs/nscloud-cache-action)
  from 1.6.0 to 1.6.1.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/namespacelabs/nscloud-cache-action/releases">namespacelabs/nscloud-cache-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v1.6.1</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>Bump the minor-actions-dependencies group across 1 directory with 6
  updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/154">namespacelabs/nscloud-cache-action#154</a></li>
  <li>Remove Tuist cache mode test by <a
  href="https://github.com/rcrowe"><code>@​rcrowe</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/156">namespacelabs/nscloud-cache-action#156</a></li>
  <li>Bump the minor-npm-dependencies group across 1 directory with 9
  updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/155">namespacelabs/nscloud-cache-action#155</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/namespacelabs/nscloud-cache-action/compare/v1...v1.6.1">https://github.com/namespacelabs/nscloud-cache-action/compare/v1...v1.6.1</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/c5f8dab7560444c4bf8dbc64f1b203431873c547"><code>c5f8dab</code></a>
  Bump the minor-npm-dependencies group across 1 directory with 9 updates
  (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/155">#155</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/0820eca039c654baff6026b49fe635a167913044"><code>0820eca</code></a>
  ci: remove tuist cache mode test (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/156">#156</a>)</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/fa75731ea70ffa2e55a1e66dd0cb4383c9b2b716"><code>fa75731</code></a>
  Bump the minor-actions-dependencies group across 1 directory with 6
  updates (...</li>
  <li>See full diff in <a
  href="https://github.com/namespacelabs/nscloud-cache-action/compare/58bf6e08898e88803c098e2b522668541cd3b2e3...c5f8dab7560444c4bf8dbc64f1b203431873c547">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=namespacelabs/nscloud-cache-action&package-manager=github_actions&previous-version=1.6.0&new-version=1.6.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## July 16, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/29461862065)  
Summary: 1 runs • 2 commits • 2 authors

### Changes

- [`68376f5`](https://github.com/ghostty-org/ghostty/commit/68376f5accba208498ef4a6333a5d097db4e3c20) build(deps): bump cachix/install-nix-action from 31.10.7 to 31.11.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [cachix/install-nix-action](https://github.com/cachix/install-nix-action) from 31.10.7 to 31.11.0.
  - [Release notes](https://github.com/cachix/install-nix-action/releases)
  - [Changelog](https://github.com/cachix/install-nix-action/blob/master/RELEASE.md)
  - [Commits](https://github.com/cachix/install-nix-action/compare/a49548c11d9846ad46ecc0115273879b045f001c...630ae543ea3a38a9a4166f03376c02c50f408342)
  
  ---
  updated-dependencies:
  - dependency-name: cachix/install-nix-action
    dependency-version: 31.11.0
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`73534c4`](https://github.com/ghostty-org/ghostty/commit/73534c4680a809398b396c94ac7f12fcccb7963d) build(deps): bump cachix/install-nix-action from 31.10.7 to 31.11.0 ([#13351](https://github.com/ghostty-org/ghostty/issues/13351)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [cachix/install-nix-action](https://github.com/cachix/install-nix-action)
  from 31.10.7 to 31.11.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/cachix/install-nix-action/releases">cachix/install-nix-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v31.11.0</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>nix: 2.34.8 -&gt; 2.35.1 by <a
  href="https://github.com/github-actions"><code>@​github-actions</code></a>[bot]
  in <a
  href="https://redirect.github.com/cachix/install-nix-action/pull/279">cachix/install-nix-action#279</a>
  Release notes: <a
  href="https://discourse.nixos.org/t/nix-2-35-0-released/78914">https://discourse.nixos.org/t/nix-2-35-0-released/78914</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/cachix/install-nix-action/compare/v31.10.7...v31.11.0">https://github.com/cachix/install-nix-action/compare/v31.10.7...v31.11.0</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/630ae543ea3a38a9a4166f03376c02c50f408342"><code>630ae54</code></a>
  Merge pull request <a
  href="https://redirect.github.com/cachix/install-nix-action/issues/279">#279</a>
  from cachix/create-pull-request/patch</li>
  <li><a
  href="https://github.com/cachix/install-nix-action/commit/0247906e3a81152580edf10a53a0f6c191922535"><code>0247906</code></a>
  nix: 2.34.8 -&gt; 2.35.1</li>
  <li>See full diff in <a
  href="https://github.com/cachix/install-nix-action/compare/a49548c11d9846ad46ecc0115273879b045f001c...630ae543ea3a38a9a4166f03376c02c50f408342">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=cachix/install-nix-action&package-manager=github_actions&previous-version=31.10.7&new-version=31.11.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## July 15, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/29451493235), [2](https://github.com/ghostty-org/ghostty/actions/runs/29386904038)  
Summary: 2 runs • 4 commits • 4 authors

### Changes

- [`42b4c59`](https://github.com/ghostty-org/ghostty/commit/42b4c5972d01eccfcd5e896ce5c7b63e8307ccb4) cleanup: remove dead code line ([@Secrus](https://github.com/Secrus))
- [`b094737`](https://github.com/ghostty-org/ghostty/commit/b0947378349eff70f7030dda0e6d022fae1e6fbd) cleanup: remove dead code line ([#13349](https://github.com/ghostty-org/ghostty/issues/13349)) ([@jcollie](https://github.com/jcollie))
  ```text
  Pointed out on Discord, this code is dead, `std.debug.assert` is
  imported, but never used.
  ```
- [`59c3a08`](https://github.com/ghostty-org/ghostty/commit/59c3a08366ce9464b21dcc2521890b2e033d6a18) build(deps): bump softprops/action-gh-release from 3.0.1 to 3.0.2 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [softprops/action-gh-release](https://github.com/softprops/action-gh-release) from 3.0.1 to 3.0.2.
  - [Release notes](https://github.com/softprops/action-gh-release/releases)
  - [Changelog](https://github.com/softprops/action-gh-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/softprops/action-gh-release/compare/718ea10b132b3b2eba29c1007bb80653f286566b...3d0d9888cb7fd7b750713d6e236d1fcb99157228)
  
  ---
  updated-dependencies:
  - dependency-name: softprops/action-gh-release
    dependency-version: 3.0.2
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`c5a21ed`](https://github.com/ghostty-org/ghostty/commit/c5a21edfcbc2d5b46540ad91b7980aca31f5f1f3) build(deps): bump softprops/action-gh-release from 3.0.1 to 3.0.2 ([#13336](https://github.com/ghostty-org/ghostty/issues/13336)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [softprops/action-gh-release](https://github.com/softprops/action-gh-release)
  from 3.0.1 to 3.0.2.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/softprops/action-gh-release/releases">softprops/action-gh-release's
  releases</a>.</em></p>
  <blockquote>
  <h2>v3.0.2</h2>
  <p><code>3.0.2</code> is a patch release focused on release reliability
  and compatibility. It
  reuses existing draft releases when publishing prereleases, supports
  replacing
  release assets on Gitea, hardens streamed asset uploads, and provides
  clearer
  release-creation diagnostics. It also includes TypeScript, coverage, and
  tooling
  maintenance merged since <code>3.0.1</code>.</p>
  <p>This release fixes <a
  href="https://redirect.github.com/softprops/action-gh-release/issues/795">#795</a>,
  <a
  href="https://redirect.github.com/softprops/action-gh-release/issues/438">#438</a>,
  and <a
  href="https://redirect.github.com/softprops/action-gh-release/issues/803">#803</a>.
  The upload transport hardening covers the
  historical failure reported in <a
  href="https://redirect.github.com/softprops/action-gh-release/issues/790">#790</a>,
  although current hosted Node 24 runners did
  not reproduce it naturally. The diagnostics work is related to <a
  href="https://redirect.github.com/softprops/action-gh-release/issues/786">#786</a>
  and does not
  claim a reproducible release-creation fix.</p>
  <h2>What's Changed</h2>
  <h3>Exciting New Features 🎉</h3>
  <ul>
  <li>feat: improve release error reporting and test coverage by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/813">softprops/action-gh-release#813</a></li>
  </ul>
  <h3>Bug fixes 🐛</h3>
  <ul>
  <li>fix: publish existing draft releases as prereleases by <a
  href="https://github.com/godfengliang"><code>@​godfengliang</code></a>
  in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/801">softprops/action-gh-release#801</a></li>
  <li>fix: upload small checksum assets reliably by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/815">softprops/action-gh-release#815</a></li>
  <li>fix: replace existing release assets on Gitea by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/816">softprops/action-gh-release#816</a></li>
  <li>fix: clarify release creation 404 errors by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/817">softprops/action-gh-release#817</a></li>
  </ul>
  <h3>Other Changes 🔄</h3>
  <ul>
  <li>chore(deps): upgrade TypeScript to 7 by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/812">softprops/action-gh-release#812</a></li>
  <li>chore(deps): remove unused TypeScript tooling by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/814">softprops/action-gh-release#814</a></li>
  <li>dependency, Node 24 pin, and CI maintenance merged since
  <code>3.0.1</code></li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/softprops/action-gh-release/blob/master/CHANGELOG.md">softprops/action-gh-release's
  changelog</a>.</em></p>
  <blockquote>
  <h2>3.0.2</h2>
  <p><code>3.0.2</code> is a patch release focused on release reliability
  and compatibility. It
  reuses existing draft releases when publishing prereleases, supports
  replacing
  release assets on Gitea, hardens streamed asset uploads, and provides
  clearer
  release-creation diagnostics. It also includes TypeScript, coverage, and
  tooling
  maintenance merged since <code>3.0.1</code>.</p>
  <p>This release fixes <a
  href="https://redirect.github.com/softprops/action-gh-release/issues/795">#795</a>,
  <a
  href="https://redirect.github.com/softprops/action-gh-release/issues/438">#438</a>,
  and <a
  href="https://redirect.github.com/softprops/action-gh-release/issues/803">#803</a>.
  The upload transport hardening covers the
  historical failure reported in <a
  href="https://redirect.github.com/softprops/action-gh-release/issues/790">#790</a>,
  although current hosted Node 24 runners did
  not reproduce it naturally. The diagnostics work is related to <a
  href="https://redirect.github.com/softprops/action-gh-release/issues/786">#786</a>
  and does not
  claim a reproducible release-creation fix.</p>
  <h2>What's Changed</h2>
  <h3>Exciting New Features 🎉</h3>
  <ul>
  <li>feat: improve release error reporting and test coverage by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/813">softprops/action-gh-release#813</a></li>
  </ul>
  <h3>Bug fixes 🐛</h3>
  <ul>
  <li>fix: publish existing draft releases as prereleases by <a
  href="https://github.com/godfengliang"><code>@​godfengliang</code></a>
  in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/801">softprops/action-gh-release#801</a></li>
  <li>fix: upload small checksum assets reliably by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/815">softprops/action-gh-release#815</a></li>
  <li>fix: replace existing release assets on Gitea by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/816">softprops/action-gh-release#816</a></li>
  <li>fix: clarify release creation 404 errors by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/817">softprops/action-gh-release#817</a></li>
  </ul>
  <h3>Other Changes 🔄</h3>
  <ul>
  <li>chore(deps): upgrade TypeScript to 7 by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/812">softprops/action-gh-release#812</a></li>
  <li>chore(deps): remove unused TypeScript tooling by <a
  href="https://github.com/chenrui333"><code>@​chenrui333</code></a> in <a
  href="https://redirect.github.com/softprops/action-gh-release/pull/814">softprops/action-gh-release#814</a></li>
  <li>dependency, Node 24 pin, and CI maintenance merged since
  <code>3.0.1</code></li>
  </ul>
  <h2>3.0.1</h2>
  <ul>
  <li>maintenance release with updated dependencies</li>
  </ul>
  <h2>3.0.0</h2>
  <p><code>3.0.0</code> is a major release that moves the action runtime
  from Node 20 to Node 24.
  Use <code>v3</code> on GitHub-hosted runners and self-hosted fleets that
  already support the
  Node 24 Actions runtime. <code>v2.6.2</code> was the final Node
  20-compatible release and is
  no longer maintained or supported.</p>
  <h2>What's Changed</h2>
  <h3>Other Changes 🔄</h3>
  <ul>
  <li>Move the action runtime and bundle target to Node 24</li>
  <li>Update <code>@types/node</code> to the Node 24 line and allow future
  Dependabot updates</li>
  <li>Keep the floating major tag on <code>v3</code>; freeze
  <code>v2</code> at the final <code>v2.6.2</code> release</li>
  </ul>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/3d0d9888cb7fd7b750713d6e236d1fcb99157228"><code>3d0d988</code></a>
  release 3.0.2 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/818">#818</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/7e13ed4ac596a4adf801d3812be5a089356949aa"><code>7e13ed4</code></a>
  fix: clarify release creation 404 errors (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/817">#817</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/e6c70a53cf67373fbff7eeebca7782b4fe8f106c"><code>e6c70a5</code></a>
  fix: replace existing release assets on Gitea (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/816">#816</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/f3453378888d5ef6208e2788af1c5ba50d8a898d"><code>f345337</code></a>
  fix: publish existing draft releases as prereleases (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/801">#801</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/d8a89a206684ded8435bf16d6f698bf04ab05164"><code>d8a89a2</code></a>
  fix: upload small checksum assets reliably (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/815">#815</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/45ece40c3178522904ac6c51c21d8a4e3565f3c8"><code>45ece40</code></a>
  chore(deps): remove unused TypeScript tooling (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/814">#814</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/f6b913c3f95302d88e8ef7cb2859c2e7656aa01e"><code>f6b913c</code></a>
  feat: improve release error reporting and test coverage (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/813">#813</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/15f193d7d8aa9623b5181913a31fafceb4e8cef9"><code>15f193d</code></a>
  chore(deps): upgrade TypeScript to 7 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/812">#812</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/cc8268d46a81d57ec9b061f27b0dd68ebd7fb17f"><code>cc8268d</code></a>
  chore(deps): bump actions/checkout in the github-actions group (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/810">#810</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/fd0ed1e85b6730f87f5c67d7355751c46ad513d6"><code>fd0ed1e</code></a>
  chore(deps): bump the npm group with 3 updates (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/811">#811</a>)</li>
  <li>Additional commits viewable in <a
  href="https://github.com/softprops/action-gh-release/compare/718ea10b132b3b2eba29c1007bb80653f286566b...3d0d9888cb7fd7b750713d6e236d1fcb99157228">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=softprops/action-gh-release&package-manager=github_actions&previous-version=3.0.1&new-version=3.0.2)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## July 14, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/29351501961), [2](https://github.com/ghostty-org/ghostty/actions/runs/29349604817)  
Summary: 2 runs • 11 commits • 3 authors

### Changes

- [`f8041e8`](https://github.com/ghostty-org/ghostty/commit/f8041e849b36efbbb9736b6ecf0ccfcb01d94e69) Update VOUCHED list ([#13330](https://github.com/ghostty-org/ghostty/issues/13330)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13329#discussioncomment-17638470)
  from @rockorager.
  
  Vouch: @aymanbagabas
  ```
- [`7622200`](https://github.com/ghostty-org/ghostty/commit/76222008ebf9d0a6bcb53d14116a4fbe445f70f0) build(deps): bump mitchellh/vouch/action/manage-by-issue ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [mitchellh/vouch/action/manage-by-issue](https://github.com/mitchellh/vouch) from 1.4.2 to 1.5.0.
  - [Release notes](https://github.com/mitchellh/vouch/releases)
  - [Commits](https://github.com/mitchellh/vouch/compare/c6d80ead49839655b61b422700b7a3bc9d0804a9...d66fa29a64600490892131ad87597c30c91fcac4)
  
  ---
  updated-dependencies:
  - dependency-name: mitchellh/vouch/action/manage-by-issue
    dependency-version: 1.5.0
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`8093d2d`](https://github.com/ghostty-org/ghostty/commit/8093d2d437bcbd7e55ab710dba524c81cc2189d3) build(deps): bump mitchellh/vouch/action/check-pr from 1.4.2 to 1.5.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [mitchellh/vouch/action/check-pr](https://github.com/mitchellh/vouch) from 1.4.2 to 1.5.0.
  - [Release notes](https://github.com/mitchellh/vouch/releases)
  - [Commits](https://github.com/mitchellh/vouch/compare/c6d80ead49839655b61b422700b7a3bc9d0804a9...d66fa29a64600490892131ad87597c30c91fcac4)
  
  ---
  updated-dependencies:
  - dependency-name: mitchellh/vouch/action/check-pr
    dependency-version: 1.5.0
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`3f6b9a1`](https://github.com/ghostty-org/ghostty/commit/3f6b9a16bca2b65139f9ae4ff1fe9d1760f4bf49) build(deps): bump mitchellh/vouch/action/check-issue ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [mitchellh/vouch/action/check-issue](https://github.com/mitchellh/vouch) from baeb3bf7c7e6c12d6e33bab3870b7e936580a934 to d66fa29a64600490892131ad87597c30c91fcac4.
  - [Release notes](https://github.com/mitchellh/vouch/releases)
  - [Commits](https://github.com/mitchellh/vouch/compare/baeb3bf7c7e6c12d6e33bab3870b7e936580a934...d66fa29a64600490892131ad87597c30c91fcac4)
  
  ---
  updated-dependencies:
  - dependency-name: mitchellh/vouch/action/check-issue
    dependency-version: d66fa29a64600490892131ad87597c30c91fcac4
    dependency-type: direct:production
  ...
  ```
- [`97f70cc`](https://github.com/ghostty-org/ghostty/commit/97f70cccfa004ead2d0485120eb2f7292a3d65c5) build(deps): bump mitchellh/vouch/action/manage-by-discussion ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [mitchellh/vouch/action/manage-by-discussion](https://github.com/mitchellh/vouch) from 1.4.2 to 1.5.0.
  - [Release notes](https://github.com/mitchellh/vouch/releases)
  - [Commits](https://github.com/mitchellh/vouch/compare/c6d80ead49839655b61b422700b7a3bc9d0804a9...d66fa29a64600490892131ad87597c30c91fcac4)
  
  ---
  updated-dependencies:
  - dependency-name: mitchellh/vouch/action/manage-by-discussion
    dependency-version: 1.5.0
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`0ac423d`](https://github.com/ghostty-org/ghostty/commit/0ac423d57b9d9a31bb4044e9ed669a4e3d9a671d) build(deps): bump mitchellh/vouch/action/sync-codeowners ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [mitchellh/vouch/action/sync-codeowners](https://github.com/mitchellh/vouch) from 1.4.2 to 1.5.0.
  - [Release notes](https://github.com/mitchellh/vouch/releases)
  - [Commits](https://github.com/mitchellh/vouch/compare/c6d80ead49839655b61b422700b7a3bc9d0804a9...d66fa29a64600490892131ad87597c30c91fcac4)
  
  ---
  updated-dependencies:
  - dependency-name: mitchellh/vouch/action/sync-codeowners
    dependency-version: 1.5.0
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`728134f`](https://github.com/ghostty-org/ghostty/commit/728134f3fbea4d097cc6da6041b5cc780a2a31ef) build(deps): bump mitchellh/vouch/action/sync-codeowners from 1.4.2 to 1.5.0 ([#13316](https://github.com/ghostty-org/ghostty/issues/13316)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [mitchellh/vouch/action/sync-codeowners](https://github.com/mitchellh/vouch)
  from 1.4.2 to 1.5.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/mitchellh/vouch/releases">mitchellh/vouch/action/sync-codeowners's
  releases</a>.</em></p>
  <blockquote>
  <h2>v1.5.0</h2>
  <h2>What's New</h2>
  <h3>Improvements</h3>
  <p>-<strong><code>action/check-issue</code></strong> has a new option
  <code>auto-lock</code> to automatically lock closed issues. (<a
  href="https://redirect.github.com/mitchellh/vouch/pull/90">#90</a>)</p>
  <ul>
  <li><strong><code>gh-manage-by-discussion</code></strong> supports
  numerical IDs. (<a
  href="https://redirect.github.com/mitchellh/vouch/pull/77">#77</a>)</li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/d66fa29a64600490892131ad87597c30c91fcac4"><code>d66fa29</code></a>
  Merge pull request <a
  href="https://redirect.github.com/mitchellh/vouch/issues/93">#93</a>
  from mitchellh/dependabot/github_actions/actions/check...</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/c22b93d0e8352a4323b9e24a1b313b349735657a"><code>c22b93d</code></a>
  Bump actions/checkout from 6.0.2 to 7.0.0</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/baeb3bf7c7e6c12d6e33bab3870b7e936580a934"><code>baeb3bf</code></a>
  Merge pull request <a
  href="https://redirect.github.com/mitchellh/vouch/issues/90">#90</a>
  from trag1c/lock-issues</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/52aec3d64655edf2fdb58f298e02da754a056daf"><code>52aec3d</code></a>
  add an option to lock closed issues</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/3dbc69c691b8832a0dbb3913f47563b7c16c99f7"><code>3dbc69c</code></a>
  Merge pull request <a
  href="https://redirect.github.com/mitchellh/vouch/issues/87">#87</a>
  from freepicheep/example-attribute</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/a6933466b4243576126c2fadc20d18d765ae11c6"><code>a693346</code></a>
  Update VOUCHED list</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/21177c0fec7b362251e27867e49b255906559fa6"><code>21177c0</code></a>
  Merge pull request <a
  href="https://redirect.github.com/mitchellh/vouch/issues/74">#74</a>
  from pavelzw/vouch-cli</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/527cdc34880f5579be51349c22e61506d439c04e"><code>527cdc3</code></a>
  Merge pull request <a
  href="https://redirect.github.com/mitchellh/vouch/issues/81">#81</a>
  from mitchellh/dependabot/github_actions/hustcer/setup...</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/1895e9c54f125df407f75cef7b409274a124f348"><code>1895e9c</code></a>
  feat: use <a
  href="https://github.com/example"><code>@​example</code></a> attribute
  for command examples</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/8c80ada45b47ed245457b8c7c50f860bcea6cf74"><code>8c80ada</code></a>
  Update README</li>
  <li>Additional commits viewable in <a
  href="https://github.com/mitchellh/vouch/compare/c6d80ead49839655b61b422700b7a3bc9d0804a9...d66fa29a64600490892131ad87597c30c91fcac4">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=mitchellh/vouch/action/sync-codeowners&package-manager=github_actions&previous-version=1.4.2&new-version=1.5.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`4862e73`](https://github.com/ghostty-org/ghostty/commit/4862e73419ca22ec7d1f095fe6c5bb789ad25681) build(deps): bump mitchellh/vouch/action/manage-by-discussion from 1.4.2 to 1.5.0 ([#13315](https://github.com/ghostty-org/ghostty/issues/13315)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [mitchellh/vouch/action/manage-by-discussion](https://github.com/mitchellh/vouch)
  from 1.4.2 to 1.5.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/mitchellh/vouch/releases">mitchellh/vouch/action/manage-by-discussion's
  releases</a>.</em></p>
  <blockquote>
  <h2>v1.5.0</h2>
  <h2>What's New</h2>
  <h3>Improvements</h3>
  <p>-<strong><code>action/check-issue</code></strong> has a new option
  <code>auto-lock</code> to automatically lock closed issues. (<a
  href="https://redirect.github.com/mitchellh/vouch/pull/90">#90</a>)</p>
  <ul>
  <li><strong><code>gh-manage-by-discussion</code></strong> supports
  numerical IDs. (<a
  href="https://redirect.github.com/mitchellh/vouch/pull/77">#77</a>)</li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/d66fa29a64600490892131ad87597c30c91fcac4"><code>d66fa29</code></a>
  Merge pull request <a
  href="https://redirect.github.com/mitchellh/vouch/issues/93">#93</a>
  from mitchellh/dependabot/github_actions/actions/check...</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/c22b93d0e8352a4323b9e24a1b313b349735657a"><code>c22b93d</code></a>
  Bump actions/checkout from 6.0.2 to 7.0.0</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/baeb3bf7c7e6c12d6e33bab3870b7e936580a934"><code>baeb3bf</code></a>
  Merge pull request <a
  href="https://redirect.github.com/mitchellh/vouch/issues/90">#90</a>
  from trag1c/lock-issues</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/52aec3d64655edf2fdb58f298e02da754a056daf"><code>52aec3d</code></a>
  add an option to lock closed issues</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/3dbc69c691b8832a0dbb3913f47563b7c16c99f7"><code>3dbc69c</code></a>
  Merge pull request <a
  href="https://redirect.github.com/mitchellh/vouch/issues/87">#87</a>
  from freepicheep/example-attribute</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/a6933466b4243576126c2fadc20d18d765ae11c6"><code>a693346</code></a>
  Update VOUCHED list</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/21177c0fec7b362251e27867e49b255906559fa6"><code>21177c0</code></a>
  Merge pull request <a
  href="https://redirect.github.com/mitchellh/vouch/issues/74">#74</a>
  from pavelzw/vouch-cli</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/527cdc34880f5579be51349c22e61506d439c04e"><code>527cdc3</code></a>
  Merge pull request <a
  href="https://redirect.github.com/mitchellh/vouch/issues/81">#81</a>
  from mitchellh/dependabot/github_actions/hustcer/setup...</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/1895e9c54f125df407f75cef7b409274a124f348"><code>1895e9c</code></a>
  feat: use <a
  href="https://github.com/example"><code>@​example</code></a> attribute
  for command examples</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/8c80ada45b47ed245457b8c7c50f860bcea6cf74"><code>8c80ada</code></a>
  Update README</li>
  <li>Additional commits viewable in <a
  href="https://github.com/mitchellh/vouch/compare/c6d80ead49839655b61b422700b7a3bc9d0804a9...d66fa29a64600490892131ad87597c30c91fcac4">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=mitchellh/vouch/action/manage-by-discussion&package-manager=github_actions&previous-version=1.4.2&new-version=1.5.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`07a8706`](https://github.com/ghostty-org/ghostty/commit/07a87067f5e28289fa5c6f22babfca334531c0cd) build(deps): bump mitchellh/vouch/action/check-issue from baeb3bf7c7e6c12d6e33bab3870b7e936580a934 to d66fa29a64600490892131ad87597c30c91fcac4 ([#13314](https://github.com/ghostty-org/ghostty/issues/13314)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [mitchellh/vouch/action/check-issue](https://github.com/mitchellh/vouch)
  from baeb3bf7c7e6c12d6e33bab3870b7e936580a934 to
  d66fa29a64600490892131ad87597c30c91fcac4.
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/d66fa29a64600490892131ad87597c30c91fcac4"><code>d66fa29</code></a>
  Merge pull request <a
  href="https://redirect.github.com/mitchellh/vouch/issues/93">#93</a>
  from mitchellh/dependabot/github_actions/actions/check...</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/c22b93d0e8352a4323b9e24a1b313b349735657a"><code>c22b93d</code></a>
  Bump actions/checkout from 6.0.2 to 7.0.0</li>
  <li>See full diff in <a
  href="https://github.com/mitchellh/vouch/compare/baeb3bf7c7e6c12d6e33bab3870b7e936580a934...d66fa29a64600490892131ad87597c30c91fcac4">compare
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
- [`e758e2b`](https://github.com/ghostty-org/ghostty/commit/e758e2b9ee5cf43ac744d546f17f19a1b5b2faae) build(deps): bump mitchellh/vouch/action/check-pr from 1.4.2 to 1.5.0 ([#13313](https://github.com/ghostty-org/ghostty/issues/13313)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [mitchellh/vouch/action/check-pr](https://github.com/mitchellh/vouch)
  from 1.4.2 to 1.5.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/mitchellh/vouch/releases">mitchellh/vouch/action/check-pr's
  releases</a>.</em></p>
  <blockquote>
  <h2>v1.5.0</h2>
  <h2>What's New</h2>
  <h3>Improvements</h3>
  <p>-<strong><code>action/check-issue</code></strong> has a new option
  <code>auto-lock</code> to automatically lock closed issues. (<a
  href="https://redirect.github.com/mitchellh/vouch/pull/90">#90</a>)</p>
  <ul>
  <li><strong><code>gh-manage-by-discussion</code></strong> supports
  numerical IDs. (<a
  href="https://redirect.github.com/mitchellh/vouch/pull/77">#77</a>)</li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/d66fa29a64600490892131ad87597c30c91fcac4"><code>d66fa29</code></a>
  Merge pull request <a
  href="https://redirect.github.com/mitchellh/vouch/issues/93">#93</a>
  from mitchellh/dependabot/github_actions/actions/check...</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/c22b93d0e8352a4323b9e24a1b313b349735657a"><code>c22b93d</code></a>
  Bump actions/checkout from 6.0.2 to 7.0.0</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/baeb3bf7c7e6c12d6e33bab3870b7e936580a934"><code>baeb3bf</code></a>
  Merge pull request <a
  href="https://redirect.github.com/mitchellh/vouch/issues/90">#90</a>
  from trag1c/lock-issues</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/52aec3d64655edf2fdb58f298e02da754a056daf"><code>52aec3d</code></a>
  add an option to lock closed issues</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/3dbc69c691b8832a0dbb3913f47563b7c16c99f7"><code>3dbc69c</code></a>
  Merge pull request <a
  href="https://redirect.github.com/mitchellh/vouch/issues/87">#87</a>
  from freepicheep/example-attribute</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/a6933466b4243576126c2fadc20d18d765ae11c6"><code>a693346</code></a>
  Update VOUCHED list</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/21177c0fec7b362251e27867e49b255906559fa6"><code>21177c0</code></a>
  Merge pull request <a
  href="https://redirect.github.com/mitchellh/vouch/issues/74">#74</a>
  from pavelzw/vouch-cli</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/527cdc34880f5579be51349c22e61506d439c04e"><code>527cdc3</code></a>
  Merge pull request <a
  href="https://redirect.github.com/mitchellh/vouch/issues/81">#81</a>
  from mitchellh/dependabot/github_actions/hustcer/setup...</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/1895e9c54f125df407f75cef7b409274a124f348"><code>1895e9c</code></a>
  feat: use <a
  href="https://github.com/example"><code>@​example</code></a> attribute
  for command examples</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/8c80ada45b47ed245457b8c7c50f860bcea6cf74"><code>8c80ada</code></a>
  Update README</li>
  <li>Additional commits viewable in <a
  href="https://github.com/mitchellh/vouch/compare/c6d80ead49839655b61b422700b7a3bc9d0804a9...d66fa29a64600490892131ad87597c30c91fcac4">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=mitchellh/vouch/action/check-pr&package-manager=github_actions&previous-version=1.4.2&new-version=1.5.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`cf60af2`](https://github.com/ghostty-org/ghostty/commit/cf60af281bd7559a819aa25372cef01d623b8c5a) build(deps): bump mitchellh/vouch/action/manage-by-issue from 1.4.2 to 1.5.0 ([#13312](https://github.com/ghostty-org/ghostty/issues/13312)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [mitchellh/vouch/action/manage-by-issue](https://github.com/mitchellh/vouch)
  from 1.4.2 to 1.5.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/mitchellh/vouch/releases">mitchellh/vouch/action/manage-by-issue's
  releases</a>.</em></p>
  <blockquote>
  <h2>v1.5.0</h2>
  <h2>What's New</h2>
  <h3>Improvements</h3>
  <p>-<strong><code>action/check-issue</code></strong> has a new option
  <code>auto-lock</code> to automatically lock closed issues. (<a
  href="https://redirect.github.com/mitchellh/vouch/pull/90">#90</a>)</p>
  <ul>
  <li><strong><code>gh-manage-by-discussion</code></strong> supports
  numerical IDs. (<a
  href="https://redirect.github.com/mitchellh/vouch/pull/77">#77</a>)</li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/d66fa29a64600490892131ad87597c30c91fcac4"><code>d66fa29</code></a>
  Merge pull request <a
  href="https://redirect.github.com/mitchellh/vouch/issues/93">#93</a>
  from mitchellh/dependabot/github_actions/actions/check...</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/c22b93d0e8352a4323b9e24a1b313b349735657a"><code>c22b93d</code></a>
  Bump actions/checkout from 6.0.2 to 7.0.0</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/baeb3bf7c7e6c12d6e33bab3870b7e936580a934"><code>baeb3bf</code></a>
  Merge pull request <a
  href="https://redirect.github.com/mitchellh/vouch/issues/90">#90</a>
  from trag1c/lock-issues</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/52aec3d64655edf2fdb58f298e02da754a056daf"><code>52aec3d</code></a>
  add an option to lock closed issues</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/3dbc69c691b8832a0dbb3913f47563b7c16c99f7"><code>3dbc69c</code></a>
  Merge pull request <a
  href="https://redirect.github.com/mitchellh/vouch/issues/87">#87</a>
  from freepicheep/example-attribute</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/a6933466b4243576126c2fadc20d18d765ae11c6"><code>a693346</code></a>
  Update VOUCHED list</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/21177c0fec7b362251e27867e49b255906559fa6"><code>21177c0</code></a>
  Merge pull request <a
  href="https://redirect.github.com/mitchellh/vouch/issues/74">#74</a>
  from pavelzw/vouch-cli</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/527cdc34880f5579be51349c22e61506d439c04e"><code>527cdc3</code></a>
  Merge pull request <a
  href="https://redirect.github.com/mitchellh/vouch/issues/81">#81</a>
  from mitchellh/dependabot/github_actions/hustcer/setup...</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/1895e9c54f125df407f75cef7b409274a124f348"><code>1895e9c</code></a>
  feat: use <a
  href="https://github.com/example"><code>@​example</code></a> attribute
  for command examples</li>
  <li><a
  href="https://github.com/mitchellh/vouch/commit/8c80ada45b47ed245457b8c7c50f860bcea6cf74"><code>8c80ada</code></a>
  Update README</li>
  <li>Additional commits viewable in <a
  href="https://github.com/mitchellh/vouch/compare/c6d80ead49839655b61b422700b7a3bc9d0804a9...d66fa29a64600490892131ad87597c30c91fcac4">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=mitchellh/vouch/action/manage-by-issue&package-manager=github_actions&previous-version=1.4.2&new-version=1.5.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## July 13, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/29217291958)  
Summary: 1 runs • 5 commits • 4 authors

### Changes

- [`7fa4376`](https://github.com/ghostty-org/ghostty/commit/7fa43764b0c612cc2fdc2a73b1d929e312996ce6) add nushell complete attribute ([@ruoyouz](https://github.com/ruoyouz))
- [`71522c3`](https://github.com/ghostty-org/ghostty/commit/71522c31143df15090cf55f2d9647d3ff3bdb5d7) remove unneeded comments ([@ruoyouz](https://github.com/ruoyouz))
- [`bc8bb6c`](https://github.com/ghostty-org/ghostty/commit/bc8bb6c0f0307ca3b48c01061bca63ce5643dc3d) terminal/search: don't clear storage when updating fingerprint ([@vancluever](https://github.com/vancluever))
  ```text
  Using `clearRetainingCapacity` as it was being used in
  Fingerprint.update produces undefined behavior; both the old "copy" and
  current version of the fingerprint would still be using the same
  storage.
  
  This commit changes the function so that the storage is more clearly
  re-used, and shrunk at the end if need be.
  ```
- [`89621a1`](https://github.com/ghostty-org/ghostty/commit/89621a194c4896f4d0f13e2e332efd123c519a7f) terminal/search: don't clear storage when updating fingerprint ([#13311](https://github.com/ghostty-org/ghostty/issues/13311)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Using `clearRetainingCapacity` as it was being used in
  Fingerprint.update produces undefined behavior; both the old "copy" and
  current version of the fingerprint would still be using the same
  storage.
  
  This commit changes the function so that the storage is more clearly
  re-used, and shrunk at the end if need be.
  ```
- [`55a3e33`](https://github.com/ghostty-org/ghostty/commit/55a3e33ab26a23d75b274b23c7f76d837db00578) nushell: add complete attribute ([#13310](https://github.com/ghostty-org/ghostty/issues/13310)) ([@jparise](https://github.com/jparise))
  ```text
  Added correct attribute so nushell can generate completions for ghostty
  redefined commands (i.e., `ssh` and `sudo`).
  
  Fixes #12008
  ```

## July 12, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/29207635351), [2](https://github.com/ghostty-org/ghostty/actions/runs/29206968818)  
Summary: 2 runs • 3 commits • 3 authors

### Changes

- [`a3ac713`](https://github.com/ghostty-org/ghostty/commit/a3ac713b777b7d85e260a2367c0d7e5498c8b5ea) Update VOUCHED list ([#13309](https://github.com/ghostty-org/ghostty/issues/13309)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/13308#discussioncomment-17614846)
  from @jcollie.
  
  Vouch: @ruoyouz
  ```
- [`9659167`](https://github.com/ghostty-org/ghostty/commit/9659167ecd177f2bea9d33532d30666f8b321cd4) terminal/search: reuse viewport fingerprint storage ([@jparise](https://github.com/jparise))
  ```text
  Retain the existing fingerprint's storage instead of allocating a fresh
  owned slice on every update. The previous approach built a replacement
  fingerprint before it knew whether the viewport changed, discarding it
  for unchanged viewports.
  
  The fingerprint now rebuilds in place after reserving viewport-sized
  capacity and reports whether its contents changed. Unchanged viewport
  updates skip the allocation, while changed viewports will usually reuse
  the existing buffer for the lifetime of the active search.
  ```
- [`c4c61c5`](https://github.com/ghostty-org/ghostty/commit/c4c61c5a80ec40b2488fb005f28241e5c01331ce) terminal/search: reuse viewport fingerprint storage ([#13307](https://github.com/ghostty-org/ghostty/issues/13307)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Retain the existing fingerprint's storage instead of allocating a fresh
  owned slice on every update. The previous approach built a replacement
  fingerprint before it knew whether the viewport changed, discarding it
  for unchanged viewports.
  
  The fingerprint now rebuilds in place after reserving viewport-sized
  capacity and reports whether its contents changed. Unchanged viewport
  updates skip the allocation, while changed viewports will usually reuse
  the existing buffer for the lifetime of the active search.
  ```

## July 11, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/29170016149), [2](https://github.com/ghostty-org/ghostty/actions/runs/29163919811), [3](https://github.com/ghostty-org/ghostty/actions/runs/29162364457)  
Summary: 3 runs • 7 commits • 5 authors

### Changes

- [`7e14347`](https://github.com/ghostty-org/ghostty/commit/7e14347c130c3296136a28fb4255e94e1ca672e7) terminal: bound page map probe lengths ([@mitchellh](https://github.com/mitchellh))
  ```text
  #13292
  
  Page maps previously allowed a 100% load factor. Once live entries
  and tombstones filled every slot, a missing-key lookup or insertion
  could scan the entire map.
  
  Reserve 20% of each offset hash map as insertion headroom and track
  that budget separately from the live count. Port the allocation-free
  in-place rehash from Zig HashMapUnmanaged so canonical insertion can
  rebuild fragmented probes and restore tombstone-exhausted headroom
  without growing the page. Assumed-capacity insertion now applies the
  same guard, preventing the headroom counter from wrapping.
  
  Pass the exact requested hyperlink count into map layout before
  load-factor scaling, avoiding a redundant power-of-two rounding step.
  Screen-level recovery now grows only when live hyperlinks actually fill
  usable capacity.
  
  ReleaseFast terminal benchmarks compare main with the combined map
  changes:
  
  | workload | before | after | speedup |
  |---|---:|---:|---:|
  | map churn | 1.253 s | 12.5 ms | 100x |
  | full OSC 8 stream | 3.576 s | 75.6 ms | 47x |
  | clear and redraw | 299.1 ms | 118.3 ms | 2.5x |
  ```
- [`65f953e`](https://github.com/ghostty-org/ghostty/commit/65f953e8e82f7dfd9e5eb4e04538ad88a71f2452) terminal: avoid duplicate probes when moving cell data ([@rockorager](https://github.com/rockorager))
  ```text
  Hyperlink and grapheme maps are keyed by cell offset. Moving their
  data removes the source entry and reinserts it at a destination known
  to be absent. Generic clobbering insertion still searches the probe
  sequence to rule out a duplicate.
  
  Use no-clobber insertion for these moves so the first available
  tombstone can be reused. If a destination reaches a free slot after
  tombstones exhaust insertion headroom, rebuild the map in place and
  retry before decrementing the budget. This keeps the known-absent fast
  path safe at every load state.
  
  The ReleaseFast movement benchmark improves from 133.7 ms to 126.4 ms,
  a 5.5% reduction. The linked-line control remains neutral at 395.4 ms
  before and 395.7 ms after.
  ```
- [`fedd42e`](https://github.com/ghostty-org/ghostty/commit/fedd42e8d66b2ba5665031000ce842ca0535a610) terminal: use backward-shift deletion in page maps ([@mitchellh](https://github.com/mitchellh))
  ```text
  Page maps handled removal with tombstones, which a fixed-capacity map
  can never outgrow. Keeping probe lengths bounded required an insertion
  headroom counter, an allocation-free rehash, and five separate recovery
  paths with subtle invariants: removal created a tombstone without
  restoring headroom, so the counter could reach zero while the map was
  half empty and every insertion path had to be prepared to rebuild.
  
  Replace tombstones with backward-shift deletion (Knuth vol. 3, 6.4
  algorithm R). Removal restores the table to the state it would be in
  had the key never been inserted, so probe chains stay canonical at all
  times and fragmentation cannot accumulate by construction. This deletes
  the headroom counter, the in-place rehash, and every recovery path.
  Insertion no longer invalidates pointers; removal may now move other
  entries instead, and no caller holds entry pointers across removals.
  
  Removal costs a cluster scan instead of a byte write, paying
  incrementally what tombstones deferred to later probes and periodic
  rebuilds. Free slots remain all-zero bytes so probe loops keep fusing
  the state and fingerprint checks into single-byte compares. A
  randomized oracle test against the stdlib map and a canonical-placement
  invariant check cover the new removal path, including full tables where
  no free slot terminates the shift.
  
  ReleaseFast benchmarks against the prior map commits:
  
  | workload | delta |
  |---|---:|
  | map churn, 50% load | 1.23x faster |
  | map churn, 75% load | 1.15x faster |
  | map churn, max load | 1.07x slower |
  | map lookup | neutral |
  | clear and redraw stream | 1.32x faster |
  | full OSC 8 stream | 1.06x faster |
  | linked-line movement | neutral |
  ```
- [`a887df4`](https://github.com/ghostty-org/ghostty/commit/a887df42c56f6de86c0fe6da9c4eeca37931e083) terminal: bound page map probe lengths without tombstones ([#13294](https://github.com/ghostty-org/ghostty/issues/13294)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Replaces #13292
  
  This optimizes page-local hyperlink and grapheme maps under full
  occupancy, repeated clear and redraw, and managed-cell movement.
  
  Hyperlink maps previously allowed 100% occupancy and retained tombstones
  after removals. This PR bounds probe lengths with a reserved load factor
  and removes tombstones from the design entirely: removal now restores
  the table to the exact state it would be in had the key never been
  inserted, so fragmentation cannot accumulate by construction.
  
  Clear and redraw improves by 2.4x, hyperlinked cell movement by 10.4x, a
  scrolling OSC 8 stream by 1.7x, and normal ASCII/unicode output does not
  regress.
  
  ## The changes
  
  1. **Reserve probe headroom in hyperlink cell maps.** Hash maps now
  support a maximum load config and hyperlink maps set it to 80%.
  **Result: known-absent cell movement improves from 1.550 s to 149 ms.**
  
  2. **Replace tombstone removal with backward-shift deletion.** Removing
  an entry now closes the hole by shifting later entries backward. This
  keeps probe chains short without tombstones, headroom bookkeeping, or
  periodic rehashing. Removal may move other entries, but no caller
  retains pointers across removals. **Result: clear and redraw improves
  from 672 ms to 512 ms over the tombstone revision, 2.4x over baseline,
  and the map shrinks by ~140 lines, improving maintenance.**
  
  3. **Avoid duplicate probes when moving managed cell data.** Hyperlink
  and grapheme movement already guarantees that the destination is absent,
  so these paths use no-clobber insertion and skip duplicate detection.
  With backward-shift deletion this fast path is safe at every load state
  without special cases, because removing the source genuinely frees a
  slot before the destination is inserted. **Result: movement stays at
  parity with the tombstone revision (149 ms vs 148 ms) while its
  rehash-retry guard is deleted.**
  
  Note a trade-off: the map-churn microbenchmark at maximum load is ~16%
  slower, because removal pays a cluster scan up front instead of
  deferring cost to later probes and periodic rebuilds. But its a
  synthetic case that isn't grounded in reality. Instead, the realistic
  counterpart (clear and redraw at high occupancy through the full VT
  stream) is 31% faster, and lookups are neutral.
  
  ## Benchmarks
  
  | workload | baseline | tombstones | this PR |
  |---|---:|---:|---:|
  | clear and redraw, 3,000 frames | 1.243 s | 671.9 ms | 511.6 ms |
  | scrolling OSC 8 stream, 39 MiB | 5.375 s | 3.484 s | 3.214 s |
  | known-absent cell movement | 1.550 s | 148.2 ms | 149.2 ms |
  | map churn, 50% load | n/a | 566.8 ms | 464.6 ms |
  | map churn, max load | n/a | 1.088 s | 1.259 s |
  | map lookup | n/a | 636.2 ms | 643.0 ms |
  
  ## LLM Notes
  
  Assisted by GPT 5.6 and Fable. Hand-reviewed, transition to backshift
  was my nudge, benchmark numbers are from an LLM benchmark run using
  committed benchmarks.
  ```
- [`ae76cfb`](https://github.com/ghostty-org/ghostty/commit/ae76cfbfcf7e531f89e8287b6e3e29c78fbdb305) i18n: fix untranslated Close Split string in zh_CN.po ([@Arvin7liu](https://github.com/Arvin7liu))
- [`d31ac2b`](https://github.com/ghostty-org/ghostty/commit/d31ac2be380de05dbcded8b35302fbb43281364a) i18n: Fix untranslated Close Split string in zh_CN.po ([#13296](https://github.com/ghostty-org/ghostty/issues/13296)) ([@00-kat](https://github.com/00-kat))
  ```text
  Fix one untranslated string in the Simplified Chinese localization
  (`zh_CN.po`).
  
  ## Changes
  
  - `msgid "Close Split"`: `""` → `"关闭分屏"`
  
  This achieves terminology consistency:
  - Split → 分屏 (already established)
  - Close Split? → 关闭分屏吗？ (already existed)
  - Close Split → 关闭分屏 (this fix)
  ```
- [`78a9731`](https://github.com/ghostty-org/ghostty/commit/78a9731c9da011207be5c92c40ce9dfe836fa0a9) Update VOUCHED list ([#13299](https://github.com/ghostty-org/ghostty/issues/13299)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/13296#issuecomment-4948155117)
  from @00-kat.
  
  Vouch: @Arvin7liu
  ```

