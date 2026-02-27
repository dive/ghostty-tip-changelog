> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: February 27, 2026 at 12:10 UTC.

## February 27, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22472504190), [2](https://github.com/ghostty-org/ghostty/actions/runs/22471926489), [3](https://github.com/ghostty-org/ghostty/actions/runs/22467433202)  
Summary: 3 runs • 10 commits • 4 authors

### Changes

- [`3ee6303`](https://github.com/ghostty-org/ghostty/commit/3ee63035d310c1290e631b51ec84bc5507f5d36e) macos: DockTilePlugin finds app bundle via `.app` suffix ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11029 (probably)
  
  If you renamed the app bundle, the prior check would infinite loop due
  to the combination of two bugs: invalid termination checks and
  hardcoding "Ghostty.app"
  ```
- [`32a9d35`](https://github.com/ghostty-org/ghostty/commit/32a9d35c8110a5f528e8c86eaa8128b92ae4d976) macos: DockTilePlugin finds app bundle via `.app` suffix ([#11049](https://github.com/ghostty-org/ghostty/issues/11049)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #11029 (probably)
  
  If you renamed the app bundle, the prior check would infinite loop due
  to the combination of two bugs: invalid termination checks and
  hardcoding "Ghostty.app"
  ```
- [`3b4e2bb`](https://github.com/ghostty-org/ghostty/commit/3b4e2bbcbef7f5f786818457f8ef88f7ea08ea93) core: parse cmdline and cmdline_url semantic prompt options ([@jcollie](https://github.com/jcollie))
- [`f19d847`](https://github.com/ghostty-org/ghostty/commit/f19d847f95d3f775b26a5f4bc0fc2ea944bf946d) core: parse cmdline and cmdline_url semantic prompt options ([#11046](https://github.com/ghostty-org/ghostty/issues/11046)) ([@mitchellh](https://github.com/mitchellh))
- [`d5f6210`](https://github.com/ghostty-org/ghostty/commit/d5f621044deb8cc37612e2a5a890f8adb71107f0) Update `language` config option's documentation. ([@00-kat](https://github.com/00-kat))
  ```text
  Follow-up to #10976.
  ```
- [`64fd8d7`](https://github.com/ghostty-org/ghostty/commit/64fd8d794c20e33b1e02e22957ce1665d0350aea) build(deps): bump actions/upload-artifact from 6.0.0 to 7.0.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [actions/upload-artifact](https://github.com/actions/upload-artifact) from 6.0.0 to 7.0.0.
  - [Release notes](https://github.com/actions/upload-artifact/releases)
  - [Commits](https://github.com/actions/upload-artifact/compare/v6...bbbca2ddaa5d8feaa63e36b76fdaad77386f024f)
  
  ---
  updated-dependencies:
  - dependency-name: actions/upload-artifact
    dependency-version: 7.0.0
    dependency-type: direct:production
    update-type: version-update:semver-major
  ...
  ```
- [`5319d8d`](https://github.com/ghostty-org/ghostty/commit/5319d8d41c86e1be96f36b967e4be1006782a1da) build(deps): bump actions/download-artifact from 7.0.0 to 8.0.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [actions/download-artifact](https://github.com/actions/download-artifact) from 7.0.0 to 8.0.0.
  - [Release notes](https://github.com/actions/download-artifact/releases)
  - [Commits](https://github.com/actions/download-artifact/compare/37930b1c2abaa49bbe596cd826c3c89aef350131...70fc10c6e5e1ce46ad2ea6f2b72d43f7d47b13c3)
  
  ---
  updated-dependencies:
  - dependency-name: actions/download-artifact
    dependency-version: 8.0.0
    dependency-type: direct:production
    update-type: version-update:semver-major
  ...
  ```
- [`48e4f12`](https://github.com/ghostty-org/ghostty/commit/48e4f126d28c8b0ec7c0e33f63d52f077e52b817) build(deps): bump actions/download-artifact from 7.0.0 to 8.0.0 ([#11045](https://github.com/ghostty-org/ghostty/issues/11045)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [actions/download-artifact](https://github.com/actions/download-artifact)
  from 7.0.0 to 8.0.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/actions/download-artifact/releases">actions/download-artifact's
  releases</a>.</em></p>
  <blockquote>
  <h2>v8.0.0</h2>
  <h2>v8 - What's new</h2>
  <h3>Direct downloads</h3>
  <p>To support direct uploads in <code>actions/upload-artifact</code>,
  the action will no longer attempt to unzip all downloaded files.
  Instead, the action checks the <code>Content-Type</code> header ahead of
  unzipping and skips non-zipped files. Callers wishing to download a
  zipped file as-is can also set the new <code>skip-decompress</code>
  parameter to <code>false</code>.</p>
  <h3>Enforced checks (breaking)</h3>
  <p>A previous release introduced digest checks on the download. If a
  download hash didn't match the expected hash from the server, the action
  would log a warning. Callers can now configure the behavior on mismatch
  with the <code>digest-mismatch</code> parameter. To be secure by
  default, we are now defaulting the behavior to <code>error</code> which
  will fail the workflow run.</p>
  <h3>ESM</h3>
  <p>To support new versions of the @actions/* packages, we've upgraded
  the package to ESM.</p>
  <h2>What's Changed</h2>
  <ul>
  <li>Don't attempt to un-zip non-zipped downloads by <a
  href="https://github.com/danwkennedy"><code>@​danwkennedy</code></a> in
  <a
  href="https://redirect.github.com/actions/download-artifact/pull/460">actions/download-artifact#460</a></li>
  <li>Add a setting to specify what to do on hash mismatch and default it
  to <code>error</code> by <a
  href="https://github.com/danwkennedy"><code>@​danwkennedy</code></a> in
  <a
  href="https://redirect.github.com/actions/download-artifact/pull/461">actions/download-artifact#461</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/actions/download-artifact/compare/v7...v8.0.0">https://github.com/actions/download-artifact/compare/v7...v8.0.0</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/actions/download-artifact/commit/70fc10c6e5e1ce46ad2ea6f2b72d43f7d47b13c3"><code>70fc10c</code></a>
  Merge pull request <a
  href="https://redirect.github.com/actions/download-artifact/issues/461">#461</a>
  from actions/danwkennedy/digest-mismatch-behavior</li>
  <li><a
  href="https://github.com/actions/download-artifact/commit/f258da9a506b755b84a09a531814700b86ccfc62"><code>f258da9</code></a>
  Add change docs</li>
  <li><a
  href="https://github.com/actions/download-artifact/commit/ccc058e5fbb0bb2352213eaec3491e117cbc4a5c"><code>ccc058e</code></a>
  Fix linting issues</li>
  <li><a
  href="https://github.com/actions/download-artifact/commit/bd7976ba57ecea96e6f3df575eb922d11a12a9fd"><code>bd7976b</code></a>
  Add a setting to specify what to do on hash mismatch and default it to
  <code>error</code></li>
  <li><a
  href="https://github.com/actions/download-artifact/commit/ac21fcf45e0aaee541c0f7030558bdad38d77d6c"><code>ac21fcf</code></a>
  Merge pull request <a
  href="https://redirect.github.com/actions/download-artifact/issues/460">#460</a>
  from actions/danwkennedy/download-no-unzip</li>
  <li><a
  href="https://github.com/actions/download-artifact/commit/15999bff51058bc7c19b50ebbba518eaef7c26c0"><code>15999bf</code></a>
  Add note about package bumps</li>
  <li><a
  href="https://github.com/actions/download-artifact/commit/974686ed5098c7f9c9289ec946b9058e496a2561"><code>974686e</code></a>
  Bump the version to <code>v8</code> and add release notes</li>
  <li><a
  href="https://github.com/actions/download-artifact/commit/fbe48b1d2756394be4cd4358ed3bc1343b330e75"><code>fbe48b1</code></a>
  Update test names to make it clearer what they do</li>
  <li><a
  href="https://github.com/actions/download-artifact/commit/96bf374a614d4360e225874c3efd6893a3f285e7"><code>96bf374</code></a>
  One more test fix</li>
  <li><a
  href="https://github.com/actions/download-artifact/commit/b8c4819ef592cbe04fd93534534b38f853864332"><code>b8c4819</code></a>
  Fix skip decompress test</li>
  <li>Additional commits viewable in <a
  href="https://github.com/actions/download-artifact/compare/37930b1c2abaa49bbe596cd826c3c89aef350131...70fc10c6e5e1ce46ad2ea6f2b72d43f7d47b13c3">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=actions/download-artifact&package-manager=github_actions&previous-version=7.0.0&new-version=8.0.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`f9c57f0`](https://github.com/ghostty-org/ghostty/commit/f9c57f0bf6a705e4a3755f24dd591878607b5ca7) build(deps): bump actions/upload-artifact from 6.0.0 to 7.0.0 ([#11044](https://github.com/ghostty-org/ghostty/issues/11044)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [actions/upload-artifact](https://github.com/actions/upload-artifact)
  from 6.0.0 to 7.0.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/actions/upload-artifact/releases">actions/upload-artifact's
  releases</a>.</em></p>
  <blockquote>
  <h2>v7.0.0</h2>
  <h2>v7 What's new</h2>
  <h3>Direct Uploads</h3>
  <p>Adds support for uploading single files directly (unzipped). Callers
  can set the new <code>archive</code> parameter to <code>false</code> to
  skip zipping the file during upload. Right now, we only support single
  files. The action will fail if the glob passed resolves to multiple
  files. The <code>name</code> parameter is also ignored with this
  setting. Instead, the name of the artifact will be the name of the
  uploaded file.</p>
  <h3>ESM</h3>
  <p>To support new versions of the <code>@actions/*</code> packages,
  we've upgraded the package to ESM.</p>
  <h2>What's Changed</h2>
  <ul>
  <li>Add proxy integration test by <a
  href="https://github.com/Link"><code>@​Link</code></a>- in <a
  href="https://redirect.github.com/actions/upload-artifact/pull/754">actions/upload-artifact#754</a></li>
  <li>Upgrade the module to ESM and bump dependencies by <a
  href="https://github.com/danwkennedy"><code>@​danwkennedy</code></a> in
  <a
  href="https://redirect.github.com/actions/upload-artifact/pull/762">actions/upload-artifact#762</a></li>
  <li>Support direct file uploads by <a
  href="https://github.com/danwkennedy"><code>@​danwkennedy</code></a> in
  <a
  href="https://redirect.github.com/actions/upload-artifact/pull/764">actions/upload-artifact#764</a></li>
  </ul>
  <h2>New Contributors</h2>
  <ul>
  <li><a href="https://github.com/Link"><code>@​Link</code></a>- made
  their first contribution in <a
  href="https://redirect.github.com/actions/upload-artifact/pull/754">actions/upload-artifact#754</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/actions/upload-artifact/compare/v6...v7.0.0">https://github.com/actions/upload-artifact/compare/v6...v7.0.0</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/actions/upload-artifact/commit/bbbca2ddaa5d8feaa63e36b76fdaad77386f024f"><code>bbbca2d</code></a>
  Support direct file uploads (<a
  href="https://redirect.github.com/actions/upload-artifact/issues/764">#764</a>)</li>
  <li><a
  href="https://github.com/actions/upload-artifact/commit/589182c5a4cec8920b8c1bce3e2fab1c97a02296"><code>589182c</code></a>
  Upgrade the module to ESM and bump dependencies (<a
  href="https://redirect.github.com/actions/upload-artifact/issues/762">#762</a>)</li>
  <li><a
  href="https://github.com/actions/upload-artifact/commit/47309c993abb98030a35d55ef7ff34b7fa1074b5"><code>47309c9</code></a>
  Merge pull request <a
  href="https://redirect.github.com/actions/upload-artifact/issues/754">#754</a>
  from actions/Link-/add-proxy-integration-tests</li>
  <li><a
  href="https://github.com/actions/upload-artifact/commit/02a8460834e70dab0ce194c64360c59dc1475ef0"><code>02a8460</code></a>
  Add proxy integration test</li>
  <li>See full diff in <a
  href="https://github.com/actions/upload-artifact/compare/v6...bbbca2ddaa5d8feaa63e36b76fdaad77386f024f">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=actions/upload-artifact&package-manager=github_actions&previous-version=6.0.0&new-version=7.0.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`336ca18`](https://github.com/ghostty-org/ghostty/commit/336ca188457f08df89f5682cdb39288f7b40c946) Update `language` config option's documentation ([#11043](https://github.com/ghostty-org/ghostty/issues/11043)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Follow-up to #10976.
  ```

## February 26, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22463045986), [2](https://github.com/ghostty-org/ghostty/actions/runs/22462019157), [3](https://github.com/ghostty-org/ghostty/actions/runs/22458670934), [4](https://github.com/ghostty-org/ghostty/actions/runs/22452954838), [5](https://github.com/ghostty-org/ghostty/actions/runs/22448005878), [6](https://github.com/ghostty-org/ghostty/actions/runs/22447594199), [7](https://github.com/ghostty-org/ghostty/actions/runs/22424533999), [8](https://github.com/ghostty-org/ghostty/actions/runs/22421985597)  
Summary: 8 runs • 37 commits • 10 authors

### Changes

- [`3b5a7b7`](https://github.com/ghostty-org/ghostty/commit/3b5a7b77d3feedbee460f70a644b64edc5d8a6a4) macos: implement notify on command finish ([@JosephMart](https://github.com/JosephMart))
- [`f4ddddc`](https://github.com/ghostty-org/ghostty/commit/f4ddddc4b797e5bc185bbfb486f74231a331dfff) macos: refactor command finish notification duration handling ([@JosephMart](https://github.com/JosephMart))
- [`a5909df`](https://github.com/ghostty-org/ghostty/commit/a5909dfa1dabd005073ccab9d5c57ce8496addc6) macos: command finished notifications always show up ([@mitchellh](https://github.com/mitchellh))
- [`ca09c0e`](https://github.com/ghostty-org/ghostty/commit/ca09c0ef2e806479eebd6edf7fa69e4ea3bcbefe) macOS: add "command finished" notifications ([#10934](https://github.com/ghostty-org/ghostty/issues/10934)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  fixes https://github.com/ghostty-org/ghostty/issues/10840
  
  Implement command finished notifications for MacOS. Building on the work
  of #8992
  
  ### AI Tools Used
  * Cursor
  * Models
      * Opus 4.6
      * Composer 1.5
  ```
- [`875985d`](https://github.com/ghostty-org/ghostty/commit/875985dbd708023abea882520ce567e1473fe02a) zsh: fix ssh-terminfo shell integration to not interpret escape characters ([@mihi314](https://github.com/mihi314))
- [`45d1787`](https://github.com/ghostty-org/ghostty/commit/45d1787effd01bd7f21d1e621e149bfbb2f27130) i18n: rename `.po` files ([@jcollie](https://github.com/jcollie))
  ```text
  This seems to be the defacto standard for naming `.po` files. See the
  GTK source code [1] as an example. I was unable to find any definitive
  documentation on the naming.
  
  Replaces: #10905
  
  [1] https://gitlab.gnome.org/GNOME/gtk/-/tree/main/po?ref_type=heads
  ```
- [`39d163f`](https://github.com/ghostty-org/ghostty/commit/39d163fee270963570b0d6b3d09d775f7d91f708) zsh: fix ssh-terminfo shell integration to not interpret escape characters ([#11038](https://github.com/ghostty-org/ghostty/issues/11038)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  With zsh, when installing the ghostty terminfo on a server via the
  ssh-terminfo shell integration, parts of the terminfo get mangled. In
  particular, the newline escape sequence in
  ```
  > infocmp -0 -x xterm-ghostty | grep ind=
   ...,ind=\n,indn=...
   ```
  gets interpreted by `print` as a literal newline, which then just gets ignored / does not have the intended effect.
  
  Documentation for the `-r` flag of `print` used in the fix is [here](https://zsh.sourceforge.io/Doc/Release/Shell-Builtin-Commands.html#:~:text=Ignore%20the%20escape%20conventions%20of%20echo.).
  
  ### Testing locally
  You can directly demonstrate this locally. This outputs a host of warning messages:
  ```
  ssh_terminfo=$(infocmp -0 -x xterm-ghostty 2>/dev/null)
  print "$ssh_terminfo" | tic -x -
  ```
  Whereas
  ```print -r "$ssh_terminfo" | tic -x -```
  or
  ```infocmp -0 -x xterm-ghostty | tic -x -```
  work without issue.
  
  ### Testing remotely
  The most visible way is to observe the output of `htop` before and after the change.
  
  More directly, the output of `infocmp -x xterm-ghostty | grep " ind="` should be
  ```ich=\E[%p1%d@, ich1=\E[@, il=\E[%p1%dL, il1=\E[L, ind=\n,```
  instead of
  ```ich=\E[%p1%d@, ich1=\E[@, il=\E[%p1%dL, il1=\E[L, ind=,```
  
  ---
  
  Discussed in #11031.
  
  ---
  AI disclosure: I used Claude for parts of figuring out what was going on. The fix itself and the rest was written and tested by myself.
  ````
- [`62873f6`](https://github.com/ghostty-org/ghostty/commit/62873f60c53d726e9f94e768a1300ee9e72dc1f7) i18n: rename `.po` files ([#10976](https://github.com/ghostty-org/ghostty/issues/10976)) ([@jcollie](https://github.com/jcollie))
  ```text
  This seems to be the defacto standard for naming `.po` files. See the
  GTK source code [1] as an example. I was unable to find any definitive
  documentation on the naming.
  
  Replaces: #10905
  
  [1] https://gitlab.gnome.org/GNOME/gtk/-/tree/main/po?ref_type=heads
  ```
- [`d05fb65`](https://github.com/ghostty-org/ghostty/commit/d05fb652ed51727300f701e5c2f71f5624c64cdb) macos: update AGENTS.md ([@mitchellh](https://github.com/mitchellh))
- [`ea8bf17`](https://github.com/ghostty-org/ghostty/commit/ea8bf17df8b86b055f4fcc209cfe31e603928d3a) macos: use combine to coalesce bell values ([@mitchellh](https://github.com/mitchellh))
- [`79ca4da`](https://github.com/ghostty-org/ghostty/commit/79ca4daea6565545cf6bce230bf73ff8c94f90ca) macos: try to clean up Appdelegate combine mess ([@mitchellh](https://github.com/mitchellh))
- [`3aca722`](https://github.com/ghostty-org/ghostty/commit/3aca7224159c3b06d5d1b120b47cab4cd89e33b2) macos: further simplication of AppDelegate bell state ([@mitchellh](https://github.com/mitchellh))
- [`454a89e`](https://github.com/ghostty-org/ghostty/commit/454a89e011c51c1943400aec2788e1aa544b4ad1) macos: clean up badge request state ([@mitchellh](https://github.com/mitchellh))
- [`5389fdf`](https://github.com/ghostty-org/ghostty/commit/5389fdfbafea8f45f1a291703d57693d52c31c07) macos: lint ([@mitchellh](https://github.com/mitchellh))
- [`dcb7c9a`](https://github.com/ghostty-org/ghostty/commit/dcb7c9a4b8eace183b1da65eac4c78a1c073f61e) macos: show the notification count number in the badge ([@mitchellh](https://github.com/mitchellh))
- [`dc514c9`](https://github.com/ghostty-org/ghostty/commit/dc514c9e116ba32641365702e52760c6365d797f) build: don't build OpenGL support into imgui on iOS ([@mitchellh](https://github.com/mitchellh))
- [`4b7a55a`](https://github.com/ghostty-org/ghostty/commit/4b7a55a50e6eb5922517336618c6423fddf77f06) macOS: Clear badge icon when no surfaces have an active bell ([#11035](https://github.com/ghostty-org/ghostty/issues/11035)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #8487
  
  I did this by setting up a publisher on `BaseTerminalController` for any
  bell state change on any surfaces in the tree (including removing
  surfaces). By listening to this event at AppDelegate and reinspecting
  all our windows, we can reliably set the badge.
  
  **This also includes a change to show the number of terminals with an
  active bell!** We can now determine the number, so we show it!
  ```
- [`eb4aa11`](https://github.com/ghostty-org/ghostty/commit/eb4aa113d7bf2e2634021b822c9bc61c459472ce) i18n: add missing nb_NO strings ([@Uzaaft](https://github.com/Uzaaft))
- [`9d6a8d0`](https://github.com/ghostty-org/ghostty/commit/9d6a8d0fc15a42ae9815484c9830a63e21b97413) i18n: add missing nb_NO strings ([#11036](https://github.com/ghostty-org/ghostty/issues/11036)) ([@trag1c](https://github.com/trag1c))
- [`f38234b`](https://github.com/ghostty-org/ghostty/commit/f38234bc5bf7c3c6e9688c6129718b04d1fd9366) apprt: show title override in command palette jump commands ([@bernsno](https://github.com/bernsno))
- [`62c1d50`](https://github.com/ghostty-org/ghostty/commit/62c1d50757218db6e9458a91364bea2e7886d316) Update macos/Sources/Features/Command Palette/TerminalCommandPalette.swift ([@bernsno](https://github.com/bernsno))
- [`c4766df`](https://github.com/ghostty-org/ghostty/commit/c4766dff77d5c11c9279d83b5b3c75fc526279e5) fix: restore terminalTitle variable removed in previous edit ([@bernsno](https://github.com/bernsno))
- [`9fe3cc1`](https://github.com/ghostty-org/ghostty/commit/9fe3cc125d76530d095c78510fa5e6fb1f6be5ac) apprt/gtk: use new get effective title ([@mitchellh](https://github.com/mitchellh))
- [`e3d68e2`](https://github.com/ghostty-org/ghostty/commit/e3d68e28c91e83e03ed6d9ddeb038d08dcc4c916) apprt: show title override in command palette jump commands ([#10458](https://github.com/ghostty-org/ghostty/issues/10458)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Relates to https://github.com/ghostty-org/ghostty/discussions/3709
  
  When a surface has a title override set (via `prompt_surface_title`),
  the command palette's "Focus:" jump commands now display the override
  instead of the terminal title.
  
  **No title override:**
  <img width="515" height="265" alt="Screenshot 2026-01-26 at 6 11 56 PM"
  src="https://github.com/user-attachments/assets/55f49878-87fd-498d-be4e-098ea42b7aaf"
  />
  
  **With title override**
  <img width="519" height="270" alt="Screenshot 2026-01-26 at 6 11 30 PM"
  src="https://github.com/user-attachments/assets/e2a293ef-0c29-4fab-94ff-b6b357193321"
  />
  
  **AI DISCLAIMER**
  
  I leveraged Claude Code to understand the codebase, make a plan and
  write the first draft of the code. I reviewed and edited the code
  written by claude and manually tested the change on iOS.
  ```
- [`c60e24d`](https://github.com/ghostty-org/ghostty/commit/c60e24d2001e178c478df757385d286955761a29) macos: update to Sparkle 2.9 ([@mitchellh](https://github.com/mitchellh))
- [`aa5ef9c`](https://github.com/ghostty-org/ghostty/commit/aa5ef9c64cfbb7080d58ee1e6585aaf2e3422cc8) macos: update to Sparkle 2.9 ([#11034](https://github.com/ghostty-org/ghostty/issues/11034)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Nothing critical, though we may make use of some of the new features
  like Markdown and signed feeds in a follow up PR.
  ```
- [`20351a7`](https://github.com/ghostty-org/ghostty/commit/20351a71d0a1e44357a78e7a5f761823a533151f) Fix Palette.C array size typo: [265] → [256] ([@markhuot](https://github.com/markhuot))
  ```text
  The C struct Palette.C declared colors as [265]Color.C, but the
  terminal palette is 256 colors (terminal.color.Palette = [256]RGB)
  and the C header ghostty_config_palette_s correctly uses colors[256].
  
  The mismatch causes ghostty_config_get to write 265×3 = 795 bytes
  through a pointer sized for 256×3 = 768 bytes, producing a 27-byte
  buffer overflow. On macOS Release builds with stack protector enabled,
  this triggers __stack_chk_fail → SIGABRT on launch.
  ```
- [`05a1255`](https://github.com/ghostty-org/ghostty/commit/05a125533be72460c2e596bb44dd5c906a4e93b0) macos: fix glass tinting when theme changes ([@bo2themax](https://github.com/bo2themax))
- [`6ebc796`](https://github.com/ghostty-org/ghostty/commit/6ebc796c4cca7d8c9053cfd81deba56f1997e98b) Fix Palette.C array size typo: [265] → [256] ([#11027](https://github.com/ghostty-org/ghostty/issues/11027)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The C struct Palette.C declared colors as [265]Color.C, but the terminal
  palette is 256 colors (terminal.color.Palette = [256]RGB) and the C
  header ghostty_config_palette_s correctly uses colors[256].
  
  The mismatch causes ghostty_config_get to write 265×3 = 795 bytes
  through a pointer sized for 256×3 = 768 bytes, producing a 27-byte
  buffer overflow. On macOS Release builds with stack protector enabled,
  this triggers __stack_chk_fail → SIGABRT on launch.
  
  Discovered this while working on https://github.com/markhuot/watchtower.
  Builds were succeeding but the app was crashing on launch because we use
  the new C bindings to get the foreground/background colors to set window
  theming like "selection" color.
  ```
- [`87428bd`](https://github.com/ghostty-org/ghostty/commit/87428bd1ebde2635bd9e726c90dc3fc054bb2012) macos: fix glass tinting when theme changes ([#11030](https://github.com/ghostty-org/ghostty/issues/11030)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This is a minimal and temporary workaround for #11017
  ```
- [`e6da439`](https://github.com/ghostty-org/ghostty/commit/e6da439e431e8c8a978c0abf82645a14f52e673f) macos: style changes ([@mitchellh](https://github.com/mitchellh))
- [`de4ee28`](https://github.com/ghostty-org/ghostty/commit/de4ee288f54ba7878040efbd146257507758910d) pkg/dcimgui: only add the OpenGL3 shutdown helper if backend enabled ([@mitchellh](https://github.com/mitchellh))
- [`3dcc8e6`](https://github.com/ghostty-org/ghostty/commit/3dcc8e6235d5207cca23397a9dc7b72fed48dba5) Update VOUCHED list ([#11032](https://github.com/ghostty-org/ghostty/issues/11032)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11031#discussioncomment-15935875)
  from @mitchellh.
  
  Vouch: @mihi314
  ```
- [`74ba971`](https://github.com/ghostty-org/ghostty/commit/74ba971ebaca7e5ce20b1e30ee916a8f0704bd8d) Update VOUCHED list ([#11028](https://github.com/ghostty-org/ghostty/issues/11028)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11027#issuecomment-3963449775)
  from @jcollie.
  
  Vouch: @markhuot
  ```
- [`7db8346`](https://github.com/ghostty-org/ghostty/commit/7db8346fcafe945f0bc752a9341d7042c1f2fd4b) apprt/gtk: fix SIGSEGV on ImGui GLArea re-realize ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #10406
  
  ImGui_ImplOpenGL3_Shutdown() calls imgl3wShutdown() which dlcloses the
  GL library handles but does not zero out the imgl3w function pointer
  table (imgl3wProcs). When a GLArea is re-realized (e.g. during
  reparenting), ImGui_ImplOpenGL3_Init() calls ImGui_ImplOpenGL3_InitLoader()
  which checks "if (glGetIntegerv == nullptr)". Since the stale pointers
  are non-null, it skips re-initialization. The next GL call through a
  dangling function pointer causes a SIGSEGV.
  
  Fix this by introducing ImGui_ImplOpenGL3_ShutdownWithLoaderCleanup()
  which calls the normal shutdown and then zeroes the imgl3wProcs table,
  forcing the next Init to reload GL function pointers via imgl3wInit().
  
  Also properly destroy the ImGui context and reset widget state in
  glAreaUnrealize so re-realize starts clean. This was extra but was
  probably leaking memory.
  ```
- [`610e1f5`](https://github.com/ghostty-org/ghostty/commit/610e1f5f471a6b073d8be21f8c798096e645c59d) macos: add Weak to iOS build ([@mitchellh](https://github.com/mitchellh))
- [`eb531ca`](https://github.com/ghostty-org/ghostty/commit/eb531caa31d54f683f3a6a3b3d1282900c53d2c0) apprt/gtk: fix SIGSEGV on ImGui GLArea re-realize ([#11025](https://github.com/ghostty-org/ghostty/issues/11025)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #10406
  
  ImGui_ImplOpenGL3_Shutdown() calls imgl3wShutdown() which dlcloses the
  GL library handles but does not zero out the imgl3w function pointer
  table (imgl3wProcs). When a GLArea is re-realized (e.g. during
  reparenting), ImGui_ImplOpenGL3_Init() calls
  ImGui_ImplOpenGL3_InitLoader() which checks "if (glGetIntegerv ==
  nullptr)". Since the stale pointers are non-null, it skips
  re-initialization. The next GL call through a dangling function pointer
  causes a SIGSEGV.
  
  Fix this by introducing ImGui_ImplOpenGL3_ShutdownWithLoaderCleanup()
  which calls the normal shutdown and then zeroes the imgl3wProcs table,
  forcing the next Init to reload GL function pointers via imgl3wInit().
  
  Also properly destroy the ImGui context and reset widget state in
  glAreaUnrealize so re-realize starts clean. This was extra but was
  probably leaking memory.
  ```

## February 25, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22418517986), [2](https://github.com/ghostty-org/ghostty/actions/runs/22408105877), [3](https://github.com/ghostty-org/ghostty/actions/runs/22381369347), [4](https://github.com/ghostty-org/ghostty/actions/runs/22378200332)  
Summary: 4 runs • 11 commits • 3 authors

### Changes

- [`36cbbeb`](https://github.com/ghostty-org/ghostty/commit/36cbbebc01f6bc24e4e6b27c9660b56525c72566) Update VOUCHED list ([#11021](https://github.com/ghostty-org/ghostty/issues/11021)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11014#discussioncomment-15925945)
  from @mitchellh.
  
  Vouch: @amadeus
  ```
- [`1c3f760`](https://github.com/ghostty-org/ghostty/commit/1c3f7601a7bff2bde89bed482e0994109603f265) macos: pass last focused surface as env, use for focus detection ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #10935
  
  This is a more robust way to detect "is my surface focused" because that
  question usually means "is my surface the last focused surface" if a
  _different_ surface is not focused. We already have used this pattern
  all over but we should extend it to SwiftUI too.
  ```
- [`7935ae6`](https://github.com/ghostty-org/ghostty/commit/7935ae6649805aa29aa12edb23731d300db76de1) macos: pass last focused surface as env, use for focus detection ([#11024](https://github.com/ghostty-org/ghostty/issues/11024)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #10935
  
  This is a more robust way to detect "is my surface focused" because that
  question usually means "is my surface the last focused surface" if a
  _different_ surface is not focused. We already have used this pattern
  all over but we should extend it to SwiftUI too.
  ```
- [`dd4e36f`](https://github.com/ghostty-org/ghostty/commit/dd4e36f921e479386a44a12c931bc21528ce683c) macOS: fix crash when adding tab from tab overview ([@nmggithub](https://github.com/nmggithub))
- [`58acab6`](https://github.com/ghostty-org/ghostty/commit/58acab6c7d51d53b131d173f24b2bbcb35cc3c11) Merge branch 'ghostty-org:main' into fix-tabbing-from-tab-overview ([@nmggithub](https://github.com/nmggithub))
- [`304823d`](https://github.com/ghostty-org/ghostty/commit/304823d560450ccde4e0f582a68fc88241eb76bd) macos: just some textual cleanup ([@mitchellh](https://github.com/mitchellh))
- [`da045d2`](https://github.com/ghostty-org/ghostty/commit/da045d2fb3d7d7139a927d7f41f9db44ad7b8fd1) Remove ObjCExceptionCatcher from iOS target ([@mitchellh](https://github.com/mitchellh))
- [`26146f5`](https://github.com/ghostty-org/ghostty/commit/26146f54c5c739c72ad11c774caff2826cfd7eb5) update comments ([@mitchellh](https://github.com/mitchellh))
- [`8b1e4c6`](https://github.com/ghostty-org/ghostty/commit/8b1e4c66d7eedbc9455e5e06c15b531945b1ccc3) macOS: fix crash when adding tab from tab overview ([#11009](https://github.com/ghostty-org/ghostty/issues/11009)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  (moved from #11008)
  
  I have this branch up to fix #10252. It was written with AI (in Cursor),
  but only after I made sure I thoroughly understood what was happening
  (almost to an excessive extent). I had already determined that an
  Objective-C helper was necessary, I just asked GPT 5.3 Codex in Cursor
  to write it for me.
  
  **TL;DR: deep within AppKit, there is an Objective-C exception that is
  _always_ thrown when opening a new tab from the visual tab picker ("tab
  overview"). [Objective-C exceptions *cannot* be safely recovered from in
  Swift.](http://developer.apple.com/documentation/swift/handling-cocoa-errors-in-swift#Handle-Exceptions-in-Objective-C-Only)
  As Ghostty is primarily Swift, we must introduce some Objective-C
  wrapper around tab creation to safely swallow this exception.**
  
  There is a lot more I know about this than the above, and can discuss it
  at length if desired. Interestingly, it seems debug builds of Ghostty
  (`zig build run`) *do* gracefully recover and don't crash. Release
  builds (`zig build run -Doptimize=ReleaseFast`), however, *do* crash.
  The crashing seems to be expected behavior and **_I don't think there's
  any feasible way to get release builds to recover as debug builds do._**
  The debug builds do, arguably, have better animation behavior. Not sure
  how I can approach that part.
  
  Release build off of my commit:
  
  
  https://github.com/user-attachments/assets/c81927be-b2d2-48b3-a18f-30b389a90f04
  
  
  Debug build off `db1e31c7a69924913e8faafcedb290de3cb4a8b6` (current
  `main`, as of writing):
  
  
  https://github.com/user-attachments/assets/76367154-b039-4453-8d39-8a0465973deb
  ```
- [`4c8f2bc`](https://github.com/ghostty-org/ghostty/commit/4c8f2bc77b218349839b8e929a981a2bdf4734a8) Update VOUCHED list ([#11012](https://github.com/ghostty-org/ghostty/issues/11012)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/11010#issuecomment-3956559518)
  from @jcollie.
  
  Vouch: @douglance
  ```
- [`d1a32d3`](https://github.com/ghostty-org/ghostty/commit/d1a32d382bfa261065ba6b2481cd39513f08d7f9) Update VOUCHED list ([#11007](https://github.com/ghostty-org/ghostty/issues/11007)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/11006#discussioncomment-15917730)
  from @jcollie.
  
  Vouch: @nmggithub
  ```

## February 24, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22368804680), [2](https://github.com/ghostty-org/ghostty/actions/runs/22365398434), [3](https://github.com/ghostty-org/ghostty/actions/runs/22363144492), [4](https://github.com/ghostty-org/ghostty/actions/runs/22348279554), [5](https://github.com/ghostty-org/ghostty/actions/runs/22346359578), [6](https://github.com/ghostty-org/ghostty/actions/runs/22343590519), [7](https://github.com/ghostty-org/ghostty/actions/runs/22336124748), [8](https://github.com/ghostty-org/ghostty/actions/runs/22334890136)  
Summary: 8 runs • 28 commits • 9 authors

### Changes

- [`45525a0`](https://github.com/ghostty-org/ghostty/commit/45525a0a85a7ef318ca0962941aa5afc00f50e1a) macOS: use `NSDockTilePlugIn` to update app icons ([@bo2themax](https://github.com/bo2themax))
- [`a79557f`](https://github.com/ghostty-org/ghostty/commit/a79557f5214bda88de13a9de2c109ad9020ee7d6) macOS: stop cycling icons when AboutWindow is closed ([@bo2themax](https://github.com/bo2themax))
  ```text
  and start cycling with current icon
  ```
- [`2c28c27`](https://github.com/ghostty-org/ghostty/commit/2c28c27ca52f130fa743ae3314cdbb0cd5ebd710) moving lots of files, removing unused stuff ([@mitchellh](https://github.com/mitchellh))
- [`4b1178e`](https://github.com/ghostty-org/ghostty/commit/4b1178e4f647119b93b004e86f95f2d99485468f) macos: rename a bunch of files ([@mitchellh](https://github.com/mitchellh))
- [`f831f68`](https://github.com/ghostty-org/ghostty/commit/f831f68f1aab3148e8d46362cb9991425e62f395) macOS: update AppIcon encoding ([@bo2themax](https://github.com/bo2themax))
  ```text
  - make `ColorizedGhosttyIcon` codable
  - remove deprecated string encoding introduced in tip
  ```
- [`c727888`](https://github.com/ghostty-org/ghostty/commit/c72788894e11c0d60368ba138f3f346b8c1eb145) ci: fix linting and delete non-useful tests ([@bo2themax](https://github.com/bo2themax))
- [`f451ea8`](https://github.com/ghostty-org/ghostty/commit/f451ea8e4603a63058a9f019623a8d18b103b98f) macos: move icon codable/equatable to extension ([@mitchellh](https://github.com/mitchellh))
- [`eaf7d8a`](https://github.com/ghostty-org/ghostty/commit/eaf7d8a012636d51aa304d59147ea656e1edd615) macos: icon tests ([@mitchellh](https://github.com/mitchellh))
- [`06084cd`](https://github.com/ghostty-org/ghostty/commit/06084cd840daa053d80e56c78b03490b36dd67cd) macos: various dock tile cleanups ([@mitchellh](https://github.com/mitchellh))
- [`99a4723`](https://github.com/ghostty-org/ghostty/commit/99a47233afcdb8274d60d0b7d9bf6cfb6c52f63b) macOS: use `NSDockTilePlugIn` to update app icons ([#9983](https://github.com/ghostty-org/ghostty/issues/9983)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  * Using MAP prohibited `NSDockTilePlugIn` to update custom icons more
  reliably. And it also fixes the corner radius issue on older os: #8870
  * Changes in AboutWindow cc @jparise
    * Start cycling with current icon
    * Stop cycling icons when AboutWindow is closed
    * Add menu to copy icon config
  
  <img width="166" height="63" alt="Xnip2025-12-20_18-40-58"
  src="https://github.com/user-attachments/assets/52fc1215-909e-49c7-a37a-b7c73eef61f1"
  />
  
  > [!WARNING]
  > Upgrading from `macOS-custom-icon` needs to manually open the app once
  to update the icon, since this plugin is running under
  `com.apple.dock.external.extra.arm64`, which has sandbox enabled.
  >
  > When first upgraded to this commit, a notification about the dock
  plugin will pop up. The user has to enable this to change the icon
  smoothly.
  > <img width="389" height="159" alt="image"
  src="https://github.com/user-attachments/assets/a883ac6b-0b4d-4794-8c61-50b60707f6a2"
  />
  
  
  
  Here are the testing results on
  [Tahoe](https://github.com/user-attachments/assets/e5fc8354-5f5c-4280-805f-88f043ceadca)
  and
  [Sequoia](https://github.com/user-attachments/assets/633d9a07-7d9d-4806-8496-82ddaffb8833):
  
  > When you see some pause in the recording, that's when I rebuild or
  replace the older version with the latest.
  
  This also fixes some issues when changing between different styles,
  consistency issues, and resetting from others to `official`.
  
  
  ### Developer's Note
  
  This shouldn't affect current CI flow, since this new target is just a
  bundle not runnable, and I tested with archiving, exporting and signing
  in Xcode, nothing big changed.
  
  
  > [!NOTE]
  > AI helped me to write the typo ignore-re and proofread my comments
  ```
- [`6132597`](https://github.com/ghostty-org/ghostty/commit/6132597563596a12ced386f3760786b62e2dd216) ci: codesign DockTilePlugin ([@mitchellh](https://github.com/mitchellh))
- [`57d5705`](https://github.com/ghostty-org/ghostty/commit/57d570525b3ee4e365ec7bde237230d429760e41) gtk: clean up title renaming and fix a small leak ([@jcollie](https://github.com/jcollie))
- [`0cf93a3`](https://github.com/ghostty-org/ghostty/commit/0cf93a3e2f4d5ec473699394805a7314e46ae1be) gtk: clean up title renaming and fix a small leak ([#10997](https://github.com/ghostty-org/ghostty/issues/10997)) ([@jcollie](https://github.com/jcollie))
  ```text
  Also enables the "Change Title…" item in the main menu.
  ```
- [`245ea56`](https://github.com/ghostty-org/ghostty/commit/245ea565975a1199e048699759a839c790c76d79) update vouch to 1.4.2 ([@mitchellh](https://github.com/mitchellh))
- [`1087751`](https://github.com/ghostty-org/ghostty/commit/1087751d265364e2b52eb4069505852edd48b8b7) Update VOUCHED list ([#10996](https://github.com/ghostty-org/ghostty/issues/10996)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/10981#discussioncomment-15913757)
  from @mitchellh.
  
  Vouch: @Koranir
  ```
- [`9f3f97b`](https://github.com/ghostty-org/ghostty/commit/9f3f97b231ac738eb4413bb0d948525510025531) i18n: Updated mk translations with new strings (Andrej Daskalov)
- [`d0e308f`](https://github.com/ghostty-org/ghostty/commit/d0e308f32b0024d2203232626e605b2fd4417d21) i18n: Updated mk translations with new strings ([#10985](https://github.com/ghostty-org/ghostty/issues/10985)) ([@00-kat](https://github.com/00-kat))
  ```text
  Issue #10632
  ```
- [`3fde784`](https://github.com/ghostty-org/ghostty/commit/3fde7842935deff7cf4328d4ce0e066f2e82cb67) i18n: update zh_TW translation ([@pan93412](https://github.com/pan93412))
- [`8e135c4`](https://github.com/ghostty-org/ghostty/commit/8e135c4f9b94593ffe0e9d56ca3ee8ddb1ba640b) i18n: update zh_TW translation ([#10819](https://github.com/ghostty-org/ghostty/issues/10819)) ([@00-kat](https://github.com/00-kat))
  ```text
  Update to 2860dd29bb117b3d9dbe4a94736484b410614d02
  
  Related to #10814
  ```
- [`4989f1c`](https://github.com/ghostty-org/ghostty/commit/4989f1c0121e42324e4ee9b7c85e31a2a0b02a80) i18n: Add new translations for nl_NL ([@nwehg](https://github.com/nwehg))
- [`d816e83`](https://github.com/ghostty-org/ghostty/commit/d816e835a82f3050cae9de6d52ad9b45205f67fd) Update translations to imperative form ([@nwehg](https://github.com/nwehg))
- [`2a9d963`](https://github.com/ghostty-org/ghostty/commit/2a9d963631152bafe0f540551b5ed423fcb66635) i18n: Add new translations for nl_NL ([#10838](https://github.com/ghostty-org/ghostty/issues/10838)) ([@00-kat](https://github.com/00-kat))
  ```text
  Addding 3 new translations mentioned in #10632
  ```
- [`c3a900d`](https://github.com/ghostty-org/ghostty/commit/c3a900d1f4b67dd59d9fab89faf4b69026464390) ci: update vouch to 1.4.1 ([@mitchellh](https://github.com/mitchellh))
- [`956b427`](https://github.com/ghostty-org/ghostty/commit/956b427d7a84d92401f14151b8f580cedfe2314e) ci: update vouch to 1.4.1 ([#10977](https://github.com/ghostty-org/ghostty/issues/10977)) ([@mitchellh](https://github.com/mitchellh))
- [`e3a6ade`](https://github.com/ghostty-org/ghostty/commit/e3a6adeff5918fbbaecf98b738f9fb55c715370b) ci: point xcode to the mounted cache path by Namespace ([@mitchellh](https://github.com/mitchellh))
- [`c51f0d7`](https://github.com/ghostty-org/ghostty/commit/c51f0d745d3f8048d9f1262c9f54c34a6e4ef422) ci: point xcode to the mounted cache path by Namespace ([#10978](https://github.com/ghostty-org/ghostty/issues/10978)) ([@mitchellh](https://github.com/mitchellh))
- [`123438a`](https://github.com/ghostty-org/ghostty/commit/123438a4ebf249f4391b58af068bd5e7d0dbf80d) build(deps): bump namespacelabs/nscloud-setup from 0.0.10 to 0.0.11 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [namespacelabs/nscloud-setup](https://github.com/namespacelabs/nscloud-setup) from 0.0.10 to 0.0.11.
  - [Release notes](https://github.com/namespacelabs/nscloud-setup/releases)
  - [Commits](https://github.com/namespacelabs/nscloud-setup/compare/d1c625762f7c926a54bd39252efff0705fd11c64...f378676225212387f1283f4da878712af2c4cd60)
  
  ---
  updated-dependencies:
  - dependency-name: namespacelabs/nscloud-setup
    dependency-version: 0.0.11
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`d3bac33`](https://github.com/ghostty-org/ghostty/commit/d3bac33d2be44ce97187b644ddd245b84dfd7c83) build(deps): bump namespacelabs/nscloud-setup from 0.0.10 to 0.0.11 ([#10975](https://github.com/ghostty-org/ghostty/issues/10975)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [namespacelabs/nscloud-setup](https://github.com/namespacelabs/nscloud-setup)
  from 0.0.10 to 0.0.11.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/namespacelabs/nscloud-setup/releases">namespacelabs/nscloud-setup's
  releases</a>.</em></p>
  <blockquote>
  <h2>v0.0.11</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>Add exponential backoff retry for flaky network operations by <a
  href="https://github.com/GabrielBianconi"><code>@​GabrielBianconi</code></a>
  in <a
  href="https://redirect.github.com/namespacelabs/nscloud-setup/pull/9">namespacelabs/nscloud-setup#9</a></li>
  </ul>
  <h2>New Contributors</h2>
  <ul>
  <li><a
  href="https://github.com/GabrielBianconi"><code>@​GabrielBianconi</code></a>
  made their first contribution in <a
  href="https://redirect.github.com/namespacelabs/nscloud-setup/pull/9">namespacelabs/nscloud-setup#9</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/namespacelabs/nscloud-setup/compare/v0...v0.0.11">https://github.com/namespacelabs/nscloud-setup/compare/v0...v0.0.11</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/namespacelabs/nscloud-setup/commit/f378676225212387f1283f4da878712af2c4cd60"><code>f378676</code></a>
  Change input from retries to max-attempts to match checkout action</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-setup/commit/57f47752a56c01ba3272917656ea6a0d75574664"><code>57f4775</code></a>
  Add additional safety checks for unparsable number or thrown
  non-error</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-setup/commit/7fca3e5502e36494541012a1cb9f5daf09c75e49"><code>7fca3e5</code></a>
  Add exponential backoff retry for flaky network operations</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-setup/commit/d61c0c48a4247de5102d76b9a7281f985b2cfcb9"><code>d61c0c4</code></a>
  Update README</li>
  <li>See full diff in <a
  href="https://github.com/namespacelabs/nscloud-setup/compare/d1c625762f7c926a54bd39252efff0705fd11c64...f378676225212387f1283f4da878712af2c4cd60">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=namespacelabs/nscloud-setup&package-manager=github_actions&previous-version=0.0.10&new-version=0.0.11)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## February 23, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22327612320), [2](https://github.com/ghostty-org/ghostty/actions/runs/22327402698), [3](https://github.com/ghostty-org/ghostty/actions/runs/22323944108), [4](https://github.com/ghostty-org/ghostty/actions/runs/22319585055), [5](https://github.com/ghostty-org/ghostty/actions/runs/22316769133), [6](https://github.com/ghostty-org/ghostty/actions/runs/22315574597), [7](https://github.com/ghostty-org/ghostty/actions/runs/22314803568), [8](https://github.com/ghostty-org/ghostty/actions/runs/22311275840), [9](https://github.com/ghostty-org/ghostty/actions/runs/22288273568)  
Summary: 9 runs • 50 commits • 9 authors

### Changes

- [`b2a7f71`](https://github.com/ghostty-org/ghostty/commit/b2a7f71b586b83d3b2bb6a17b8c2d79b123dc33f) Update VOUCHED list ([#10972](https://github.com/ghostty-org/ghostty/issues/10972)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/10801) from
  @mitchellh.
  
  Vouch: @curtismoncoq
  ```
- [`7a4bddd`](https://github.com/ghostty-org/ghostty/commit/7a4bddd37bfb1f758a2302c04ec8e77ecae3e49b) renderer: added cursor style and visibility uniforms ([@ClearAspect](https://github.com/ClearAspect))
  ```text
  Specifically:
  iCurrentCursorStyle
  iPreviousCursorStyle
  iCurrentCursorVisible
  iPreviousCursorVisible
  
  Visibility calculated and updated independently from the typical cursor
  unifrom updates to preserve cursor style even when not in the viewport
  or set to be hidden
  ```
- [`81f21a0`](https://github.com/ghostty-org/ghostty/commit/81f21a04de4d9f9cb12597ec887646ae01a850d9) custom shader: added cursor style and visibility uniforms ([#9572](https://github.com/ghostty-org/ghostty/issues/9572)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes: #9416
  
  Specifically:
    iCurrentCursorStyle
    iPreviousCursorStyle
    iCurrentCursorVisible
    iPreviousCursorVisible
  
  Visibility calculated and updated independently from the typical cursor
  uniform updates to preserve cursor style even when not in the viewport
  or set to be hidden
  
  I used Claude-Code to initially navigate and gauge an understanding of
  the rendering system. Otherwise I authored the rest of the PR
  ```
- [`375a631`](https://github.com/ghostty-org/ghostty/commit/375a6313c94d913c456c33c5d033a3fa910739ac) Update VOUCHED list ([#10971](https://github.com/ghostty-org/ghostty/issues/10971)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/10942) from
  @mitchellh.
  
  Vouch: @aalhendi
  ```
- [`47577c7`](https://github.com/ghostty-org/ghostty/commit/47577c7623efc859c7f7a9c7da3f712807487f29) Make top visual space for surface drag handles ([@martinemde](https://github.com/martinemde))
- [`2842b18`](https://github.com/ghostty-org/ghostty/commit/2842b18a3fc6de1b5ad6f15832a4f28419cd5051) Only show drag handle on hovered surface ([@martinemde](https://github.com/martinemde))
- [`40e6a6d`](https://github.com/ghostty-org/ghostty/commit/40e6a6dd58b7fe5422c9811a81c236ecb14b26b3) Refine spacing and header usage ([@martinemde](https://github.com/martinemde))
  ```text
  This is 4pt header space, 12pt clickable frame height
  ```
- [`0316154`](https://github.com/ghostty-org/ghostty/commit/03161547f6847e43f6b3fd308c0387ddb714f5ad) Remove the top padding for macOS grab bar ([@mitchellh](https://github.com/mitchellh))
- [`ba593d8`](https://github.com/ghostty-org/ghostty/commit/ba593d823cbf69f733a5d7ca84c6a908581134a3) feat(macos): Refine MacOS surface drag handle UI ([#10280](https://github.com/ghostty-org/ghostty/issues/10280)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  <img width="638" height="476" alt="Screenshot 2026-01-11 at 1 41 52 PM"
  src="https://github.com/user-attachments/assets/bf3457e8-1b1c-4b2d-b6d1-312d48739108"
  />
  
  This PR makes 3 small changes:
  
  1. Makes the surface move grab handle present when the surface is
  hovered and the mouse cursor is not hidden.
  2. Makes the grab handle partial width, allowing space to more easily
  grab the divider for resize (anywhere but the center) and increasing the
  grabbable area for the grab handle.
  3. Adds appropriate padding to the top of the surface (in the metal
  stack so shaders can apply) to give space for the header so that text is
  not occluded by the grab handle.
  
  I think it looks good and works well, but I suggest trying it out since
  the interaction is the most important part.
  
  Problems I was trying to solve:
  1. The old grab bar overlays actual clickable area on TUIs and can make
  them hard to use
  2. The old bar makes the entire divider also a grab area, making divider
  resizing more difficult.
  3. The old bar is not always present, making it hard to discover until
  you're going to resize something, which then is confusing
  4. The old bar is not colored with the style.
  
  
  https://github.com/user-attachments/assets/588a35b5-ba2f-4074-8edb-e090e0006224
  
  
  AI Disclosure: I originally did this with Claude, but at this point I've
  gone over this code manually enough to feel somewhat familiar. I think
  the video and design speak for themselves and the code change is
  minimal, but I'm not a Swift programmer, so I can't evaluate whether
  this is the best possible solution.
  
  Human Disclosure: I don't have a linux machine to check that the padding
  doesn't apply outside of MacOS. I find it hard to believe that it
  wouldn't work, but worth calling out.
  ```
- [`0830ecf`](https://github.com/ghostty-org/ghostty/commit/0830ecfb65dbd44cbb61fcefe65a932928e12b76) ci: enable macOS caching (Zig, Xcode) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Namespace now supports cache volumes on macOS.
  
  This enables caching for Zig and Xcode artifacts. We can't do Nix yet because
  we can't create `/nix` and there's a chicken/egg with how Nix installation
  works on macOS. I'm emailing Namespace support about it... But still, a big
  win for Zig and Xcode!
  ```
- [`7dad801`](https://github.com/ghostty-org/ghostty/commit/7dad801abc86204a123f2395842965f41d4bfcc3) ci: enable macOS caching (Zig, Xcode) ([#10969](https://github.com/ghostty-org/ghostty/issues/10969)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Namespace now supports cache volumes on macOS.
  
  This enables caching for Zig and Xcode artifacts. We can't do Nix yet
  because we can't create `/nix` and there's a chicken/egg with how Nix
  installation works on macOS. I'm emailing Namespace support about it...
  But still, a big win for Zig and Xcode!
  ```
- [`dcbc765`](https://github.com/ghostty-org/ghostty/commit/dcbc765dc0cd84f190013b5085b08bd6e2f800c4) Update VOUCHED list ([#10970](https://github.com/ghostty-org/ghostty/issues/10970)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/10767#issuecomment-3946557197)
  from @mitchellh.
  
  Unvouch: @prsweet
  ```
- [`81c9c81`](https://github.com/ghostty-org/ghostty/commit/81c9c81ae3df165d239c73d739b71245ddc8b32d) Refactor glass effect into TerminalGlassView and add inactive window tint overlay ([@sunshine-syz](https://github.com/sunshine-syz))
- [`daa2a9d`](https://github.com/ghostty-org/ghostty/commit/daa2a9d0d506378b18ec246f3b7a5b90005966b4) macos: allow renaming tab title on double-click ([@MiUPa](https://github.com/MiUPa))
- [`feee444`](https://github.com/ghostty-org/ghostty/commit/feee4443da680e8f9077e9e11909b0172d72dbfa) macOS: add inline tab title editing ([@MiUPa](https://github.com/MiUPa))
- [`f6e9b19`](https://github.com/ghostty-org/ghostty/commit/f6e9b19fd501b6354ffd471fa3bd626148635504) macOS: widen inline tab title editor ([@MiUPa](https://github.com/MiUPa))
- [`368e190`](https://github.com/ghostty-org/ghostty/commit/368e190a4165f3446364b5b91168d18e99bfacd4) macOS: defer inline tab rename start to reduce flicker ([@MiUPa](https://github.com/MiUPa))
- [`879d7cf`](https://github.com/ghostty-org/ghostty/commit/879d7cf337fa8a31703fe0bf417d5beb10295076) macOS: remove dead tab title edit helper ([@MiUPa](https://github.com/MiUPa))
- [`b6a9d54`](https://github.com/ghostty-org/ghostty/commit/b6a9d54e98d1c65c4d941ee53f389b03c67c8caf) macos: extract inline title editing to standalone file ([@mitchellh](https://github.com/mitchellh))
- [`f5e2561`](https://github.com/ghostty-org/ghostty/commit/f5e2561eb75e8dcfd018fd726ed06671dc6233e3) macos: rename to TabTitleEditor ([@mitchellh](https://github.com/mitchellh))
- [`51f304e`](https://github.com/ghostty-org/ghostty/commit/51f304e9a08f66ff35419bfd33cb58024ee42a8c) macos: add AGENTS.md ([@mitchellh](https://github.com/mitchellh))
- [`1c715de`](https://github.com/ghostty-org/ghostty/commit/1c715def07d81024a20223998785c305c6880329) macOS: add inline tab title editing ([#10963](https://github.com/ghostty-org/ghostty/issues/10963)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Double-clicking a tab allows you to edit the tab name inline.
  - Implemented an inline editor that allows you to edit the tab title
  directly.
  - Press Enter to confirm, Esc to cancel.
  ```
- [`6a9a21a`](https://github.com/ghostty-org/ghostty/commit/6a9a21afb6123729b2f3964a0d19770f8a21f8c6) macOS: Add inactive window tint overlay for liquid glass ([#10943](https://github.com/ghostty-org/ghostty/issues/10943)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  **Summary:**
  - Add tint overlay to dim terminal windows when inactive, fixes
  https://github.com/ghostty-org/ghostty/discussions/10040
  - Refactor the liquid glass effect into a dedicated `TerminalGlassView`
  class
  
  Note: The tint overlay color and opacity values may not be ideal —
  feedback is welcome.
  
  **AI Disclosure:** I used Claude Code to read the macos repo and
  understand the liquid glass implementation. Implemented basic tint
  overlay mainly by hand. Refactor the code and review changes with Claude
  Code.
  ```
- [`335f0bf`](https://github.com/ghostty-org/ghostty/commit/335f0bff310f8de934431fc040d3684dec4e4799) Update VOUCHED list ([#10968](https://github.com/ghostty-org/ghostty/issues/10968)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/9932#issuecomment-3945908641)
  from @mitchellh.
  
  Vouch: @MrMage
  ```
- [`6afdf34`](https://github.com/ghostty-org/ghostty/commit/6afdf3400e52d4eb83a058c9e43e8e1de755eb64) unicode: change cell to wide when grapheme width changes ([@jacobsandlund](https://github.com/jacobsandlund))
- [`556504a`](https://github.com/ghostty-org/ghostty/commit/556504a2d4239a0ff3c5df028fdfbbb2afabff71) Merge branch 'grapheme-break' into grapheme-width-changes ([@jacobsandlund](https://github.com/jacobsandlund))
- [`a67cfb4`](https://github.com/ghostty-org/ghostty/commit/a67cfb4232f4bd41bb6d21b273ef4dd39549930d) Merge branch 'grapheme-break' into grapheme-width-changes ([@jacobsandlund](https://github.com/jacobsandlund))
- [`96c69c9`](https://github.com/ghostty-org/ghostty/commit/96c69c9f9b92651d024107f311967dd2dd88dae0) Add comment for desired_wide = .wide when !width_zero_in_grapheme ([@jacobsandlund](https://github.com/jacobsandlund))
- [`d240a19`](https://github.com/ghostty-org/ghostty/commit/d240a194e1b3728b7819e21fc9a5f98dcccb618a) Merge branch 'grapheme-break' into grapheme-width-changes ([@jacobsandlund](https://github.com/jacobsandlund))
- [`755c5b3`](https://github.com/ghostty-org/ghostty/commit/755c5b30965271805624fca593de1f39505081d9) Merge branch 'grapheme-break' into grapheme-width-changes ([@jacobsandlund](https://github.com/jacobsandlund))
- [`a1c1d66`](https://github.com/ghostty-org/ghostty/commit/a1c1d66ec8f3c6d051973d60d6e0a42e148fa970) Merge branch 'grapheme-break' into grapheme-width-changes ([@jacobsandlund](https://github.com/jacobsandlund))
- [`8020a88`](https://github.com/ghostty-org/ghostty/commit/8020a88205dbacba7e724d94cdc657d97d868f65) Merge branch 'grapheme-break' into grapheme-width-changes ([@jacobsandlund](https://github.com/jacobsandlund))
- [`8d47081`](https://github.com/ghostty-org/ghostty/commit/8d470816cf45b4bdc570045cf90674dd13347d45) Merge branch 'grapheme-break' into grapheme-width-changes ([@jacobsandlund](https://github.com/jacobsandlund))
- [`6b2caf6`](https://github.com/ghostty-org/ghostty/commit/6b2caf69db7c80aab9ec5b4c15982993d6517569) Merge remote-tracking branch 'upstream/main' into grapheme-width-changes ([@jacobsandlund](https://github.com/jacobsandlund))
- [`a7080b6`](https://github.com/ghostty-org/ghostty/commit/a7080b6fab66d1586fe4e0b30e340f62282dbdd6) Make VS15 test check that previous grapheme is not affected ([@jacobsandlund](https://github.com/jacobsandlund))
- [`5beeec0`](https://github.com/ghostty-org/ghostty/commit/5beeec0b8a818b4ead7102093bf1c0e5e824a51c) Merge remote-tracking branch 'upstream/main' into grapheme-width-changes ([@jacobsandlund](https://github.com/jacobsandlund))
- [`d5098f5`](https://github.com/ghostty-org/ghostty/commit/d5098f5896265bfcc13c95a86ff0f6ffde106fdb) Merge remote-tracking branch 'upstream/main' into grapheme-width-changes ([@jacobsandlund](https://github.com/jacobsandlund))
- [`77957aa`](https://github.com/ghostty-org/ghostty/commit/77957aa319e99a3ecfedb2300bf83bd382c7740d) Fix Bengali test due to wider grapheme ([@jacobsandlund](https://github.com/jacobsandlund))
- [`1c3fc06`](https://github.com/ghostty-org/ghostty/commit/1c3fc062e1efcf9d8c28e11c5cc6c48421264f2f) clarify comments ([@jacobsandlund](https://github.com/jacobsandlund))
- [`96c623e`](https://github.com/ghostty-org/ghostty/commit/96c623ee33189729b93c0a118be83795d0c4995c) Merge remote-tracking branch 'upstream/main' into grapheme-width-changes ([@jacobsandlund](https://github.com/jacobsandlund))
- [`bc7bbb2`](https://github.com/ghostty-org/ghostty/commit/bc7bbb27afd3077ec87771cc668262fe41a10520) Merge remote-tracking branch 'upstream/main' into grapheme-width-changes ([@jacobsandlund](https://github.com/jacobsandlund))
- [`bb9d37c`](https://github.com/ghostty-org/ghostty/commit/bb9d37c09c19b58e827c2bbd670505707a00645e) Merge remote-tracking branch 'upstream/main' into grapheme-width-changes ([@jacobsandlund](https://github.com/jacobsandlund))
- [`4f6fc32`](https://github.com/ghostty-org/ghostty/commit/4f6fc324f1043bca4e7123e45d660c3600107ccd) build(deps): bump namespacelabs/nscloud-cache-action from 1.4.1 to 1.4.2 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [namespacelabs/nscloud-cache-action](https://github.com/namespacelabs/nscloud-cache-action) from 1.4.1 to 1.4.2.
  - [Release notes](https://github.com/namespacelabs/nscloud-cache-action/releases)
  - [Commits](https://github.com/namespacelabs/nscloud-cache-action/compare/v1.4.1...a90bb5d4b27522ce881c6e98eebd7d7e6d1653f9)
  
  ---
  updated-dependencies:
  - dependency-name: namespacelabs/nscloud-cache-action
    dependency-version: 1.4.2
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`f53e4b4`](https://github.com/ghostty-org/ghostty/commit/f53e4b43c4d2a30a6d98a902a124c5fa55acc893) Merge remote-tracking branch 'upstream/main' into grapheme-width-changes ([@jacobsandlund](https://github.com/jacobsandlund))
- [`327cdbe`](https://github.com/ghostty-org/ghostty/commit/327cdbefadefbbfbdc177a13f42e3d4d8bc97eef) Merge remote-tracking branch 'upstream/main' into grapheme-width-changes ([@jacobsandlund](https://github.com/jacobsandlund))
- [`35a5ea0`](https://github.com/ghostty-org/ghostty/commit/35a5ea0e83c44e95d228d1ae1ca4d4c130ba3a68) build(deps): bump namespacelabs/nscloud-cache-action from 1.4.1 to 1.4.2 ([#10960](https://github.com/ghostty-org/ghostty/issues/10960)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [namespacelabs/nscloud-cache-action](https://github.com/namespacelabs/nscloud-cache-action)
  from 1.4.1 to 1.4.2.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/namespacelabs/nscloud-cache-action/releases">namespacelabs/nscloud-cache-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v1.4.2</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>Append error cause to failure message by <a
  href="https://github.com/rcrowe"><code>@​rcrowe</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/104">namespacelabs/nscloud-cache-action#104</a></li>
  <li>Update <code>@​namespacelabs/actions-toolkit</code> to 0.2.6 by <a
  href="https://github.com/rcrowe"><code>@​rcrowe</code></a> in <a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/pull/107">namespacelabs/nscloud-cache-action#107</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/namespacelabs/nscloud-cache-action/compare/v1.4.1...v1.4.2">https://github.com/namespacelabs/nscloud-cache-action/compare/v1.4.1...v1.4.2</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/a90bb5d4b27522ce881c6e98eebd7d7e6d1653f9"><code>a90bb5d</code></a>
  Update <code>@​namespacelabs/actions-toolkit</code> to 0.2.6</li>
  <li><a
  href="https://github.com/namespacelabs/nscloud-cache-action/commit/60628686a062537fb52c6fdeacedb198d1379023"><code>6062868</code></a>
  Append error cause to failure message (<a
  href="https://redirect.github.com/namespacelabs/nscloud-cache-action/issues/104">#104</a>)</li>
  <li>See full diff in <a
  href="https://github.com/namespacelabs/nscloud-cache-action/compare/v1.4.1...a90bb5d4b27522ce881c6e98eebd7d7e6d1653f9">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=namespacelabs/nscloud-cache-action&package-manager=github_actions&previous-version=1.4.1&new-version=1.4.2)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`d186613`](https://github.com/ghostty-org/ghostty/commit/d186613ca4a31389e1b624efcd981ebfe5354393) terminal: change cell width when wider grapheme detected ([#10465](https://github.com/ghostty-org/ghostty/issues/10465)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This PR updates the logic in Terminal `print` to include more cases of
  changing a cell to be wide due to a grapheme cluster that needs to be
  wide but starts off narrow. The existing case of this is a
  text-presentation code point followed by VS16 to make it emoji
  presentation. This PR handles more cases that are found in scripts such
  as Devanagari where the correct grapheme width calculation sums up
  multiple code points of non-zero widths. An example, as seen from
  [uucode's issue #1](https://github.com/jacobsandlund/uucode/issues/1) is
  `क्‍ष`, which now with https://github.com/ghostty-org/ghostty/pull/9680
  merged is one grapheme cluster instead of two, but the U+0915 (first
  code point) is width one and U+0937 (final code point) is also width
  one, and the whole cluster should be width 1 + 1 = 2. This is important
  to address with the grapheme break change otherwise these scripts would
  show with narrow cells, incorrectly.
  
  Before:
  
  <img width="680" height="124" alt="CleanShot 2026-01-27 at 10 31 24@2x"
  src="https://github.com/user-attachments/assets/4ff5959d-9c14-4062-8280-83004af38495"
  />
  
  After:
  
  <img width="646" height="118" alt="CleanShot 2026-01-27 at 10 29 10@2x"
  src="https://github.com/user-attachments/assets/3ad11afd-2141-46fb-b22b-9fa7b2546366"
  />
  
  ---
  
  Note that the logic here just takes `width_zero_in_grapheme` and if it's
  not zero width, makes the cell wide. This is actually wrong for
  graphemes with `prepend` (usually/always? zero width) followed by a
  character that should be narrow width, but that's affecting a much
  smaller number of graphemes. To address that, we would need to run the
  full `wcwidth` from `uucode` on the grapheme, and compare the width
  output with the current cell's `Wide`. I figured it'd be better to
  incrementally just handle the bulk of the cases with the
  `width_zero_in_grapheme` check.
  
  This also adds tests to make sure moving the cell is handled correctly,
  which was not the case for the existing VS16 logic.
  
  There's a lot of code here to handle transferring the graphemes when the
  narrow cell should wrap to the next line to become wide. I'd like
  feedback on the approach here before attempting to clean anything up, if
  desired (pull it out into a separate method?).
  
  AI was used in some of the uucode changes in
  https://github.com/ghostty-org/ghostty/pull/9678 (Amp--primarily for
  tests), but everything was carefully vetted and much of it done by hand.
  This PR was made without AI.
  ```
- [`79f0bfe`](https://github.com/ghostty-org/ghostty/commit/79f0bfe374c0a324cf3158f351ecce5aeb36770f) nix: update ucs-detect to latest master ([@jacobsandlund](https://github.com/jacobsandlund))
- [`05b4db5`](https://github.com/ghostty-org/ghostty/commit/05b4db574b4c3a36670172024ffc1998048f397f) nix: update ucs-detect to latest master ([#10965](https://github.com/ghostty-org/ghostty/issues/10965)) ([@jcollie](https://github.com/jcollie))
  ```text
  This updates [ucs-detect](https://github.com/jquast/ucs-detect) to the
  latest `master` version from 2/7/2026.
  
  AI disclaimer: this was done almost entirely with the help of AI, with
  this thread here:
  https://ampcode.com/threads/T-019c8ac5-e8ab-738d-93a6-06ec5b20f5e2
  ```
- [`c61f184`](https://github.com/ghostty-org/ghostty/commit/c61f184069336c61f7840e2268c6f4dc183b60af) Sync CODEOWNERS vouch list ([#10959](https://github.com/ghostty-org/ghostty/issues/10959)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Sync CODEOWNERS owners with vouch list.
  
  ## Added Users
  
  - @Atomk
  ```

## February 22, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22287450777), [2](https://github.com/ghostty-org/ghostty/actions/runs/22286556611), [3](https://github.com/ghostty-org/ghostty/actions/runs/22278639787), [4](https://github.com/ghostty-org/ghostty/actions/runs/22271139862), [5](https://github.com/ghostty-org/ghostty/actions/runs/22270853637), [6](https://github.com/ghostty-org/ghostty/actions/runs/22270626299)  
Summary: 6 runs • 16 commits • 4 authors

### Changes

- [`2a02b8f`](https://github.com/ghostty-org/ghostty/commit/2a02b8f0efb6a73eef2faba070283ea3752cd245) android: build improvements ([@jcollie](https://github.com/jcollie))
  ```text
  * Use a GitHub action to download the Android NDK
  * Use helper functions available on `std.Build` to simplify
    the build script.
  * Use various Zig-isms to simplify the code.
  
  FYI, using Nix to seems to be a non-starter as getting any Android
  development kits from nixpkgs requires accepting the Android license
  agreement and allowing many packages to use unfree licenses. And since
  the packages are unfree they are not cached by NixOS so the build
  triggers massive memory-hungry builds.
  ```
- [`20fe661`](https://github.com/ghostty-org/ghostty/commit/20fe661c0681c9b7835233055d7f93a4178f631b) android: build improvements ([#10956](https://github.com/ghostty-org/ghostty/issues/10956)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  * Use a GitHub action to download the Android NDK
  * Use helper functions available on `std.Build` to simplify the build
  script.
  * Use various Zig-isms to simplify the code.
  
  FYI, using Nix to seems to be a non-starter as getting any Android
  development kits from nixpkgs requires accepting the Android license
  agreement and allowing many packages to use unfree licenses. And since
  the packages are unfree they are not cached by NixOS so the build
  triggers massive memory-hungry builds.
  ```
- [`c6e7a7b`](https://github.com/ghostty-org/ghostty/commit/c6e7a7b85ad8cc721e8986ca4033313714f5c3f7) input: Disallow table/chain= and make chain apply to the most recent table ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #10039
  
  (Context is all there)
  ```
- [`f0f80d4`](https://github.com/ghostty-org/ghostty/commit/f0f80d4902f7d0e17df48b28f7208ea18e28e093) input: Disallow table/chain= and make chain apply to the most recent table ([#10954](https://github.com/ghostty-org/ghostty/issues/10954)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #10039
  
  (Context is all there)
  ```
- [`504a361`](https://github.com/ghostty-org/ghostty/commit/504a3611f6f2d9a1cb1a4eb419b41aea3c8049ca) Update VOUCHED list ([#10947](https://github.com/ghostty-org/ghostty/issues/10947)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/10946) from
  @00-kat.
  
  Vouch: @Laxystem
  ```
- [`bd96116`](https://github.com/ghostty-org/ghostty/commit/bd9611650fd1c8e72367cf781270ddf3494ff451) build: add support for Android NDK path configuration ([@elias8](https://github.com/elias8))
- [`e7cfb17`](https://github.com/ghostty-org/ghostty/commit/e7cfb17d5a28c5eebe33c0f733de1d80a51773f2) build: support 16kb page sizes for Android 15+ ([@elias8](https://github.com/elias8))
- [`b728e41`](https://github.com/ghostty-org/ghostty/commit/b728e41d77617188f38a20b10dfc5698b2ffe297) build: clarify ANDROID_NDK_HOME variable description ([@elias8](https://github.com/elias8))
- [`88a6e8a`](https://github.com/ghostty-org/ghostty/commit/88a6e8ae4b4030cacf41c25a8790e0dbf0f02698) build: add Android build target for libghostty-vt ([@elias8](https://github.com/elias8))
- [`12c2f5c`](https://github.com/ghostty-org/ghostty/commit/12c2f5c3590631cbfa37597d9ec3ca785592f3d4) prettier ([@mitchellh](https://github.com/mitchellh))
- [`79e530a`](https://github.com/ghostty-org/ghostty/commit/79e530a0f3e2aa86062a6b15da6984cfa4abba6b) ci: fix CI for NDK ([@mitchellh](https://github.com/mitchellh))
- [`861a9cf`](https://github.com/ghostty-org/ghostty/commit/861a9cf537a58a380bc6a0784573b3de3a70415e) ci: Add `lib-vt` Android support ([#10925](https://github.com/ghostty-org/ghostty/issues/10925)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The PR introduces `lib-vt` Android support as discussed in #10902.
  
  A few more notes:
  
  - Introduces new CI for Android builds as a change requires NDK to be
  configured.
  - To build locally, it is required to have the NDK installed in the
  system and either have the path exported via `ANDROID_NDK_HOME` pointing
  to the exact NDK path or `ANDROID_HOME` or `ANDROID_SDK_ROOT` pointing
  at the Android SDK path from which the build system will infer the NDK
  path and version.
  - 16kb page size alignment is configured for Android 15+. Builds are
  backward compatible with 4kb page size devices.
  ```
- [`c4c58a9`](https://github.com/ghostty-org/ghostty/commit/c4c58a9f584d269c2e991292c209e708a0ec2f60) update deps to mirror ([@mitchellh](https://github.com/mitchellh))
- [`3fca5bd`](https://github.com/ghostty-org/ghostty/commit/3fca5bd18ba7c03121da9f7bfd845d18f4185995) update deps to mirror ([#10939](https://github.com/ghostty-org/ghostty/issues/10939)) ([@mitchellh](https://github.com/mitchellh))
- [`fad5599`](https://github.com/ghostty-org/ghostty/commit/fad5599c32581d4bdfdf1fc3230b906e18c90500) deps: Update iTerm2 color schemes ([@mitchellh](https://github.com/mitchellh))
- [`84b7d14`](https://github.com/ghostty-org/ghostty/commit/84b7d14aa069a15d248f7166a92a95dec5da6efc) Update iTerm2 colorschemes ([#10938](https://github.com/ghostty-org/ghostty/issues/10938)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Upstream release:
  https://github.com/mbadolato/iTerm2-Color-Schemes/releases/tag/release-20260216-151611-fc73ce3
  ```

## February 21, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22266631328), [2](https://github.com/ghostty-org/ghostty/actions/runs/22266137820), [3](https://github.com/ghostty-org/ghostty/actions/runs/22265821791), [4](https://github.com/ghostty-org/ghostty/actions/runs/22265014052), [5](https://github.com/ghostty-org/ghostty/actions/runs/22260952552), [6](https://github.com/ghostty-org/ghostty/actions/runs/22259478775), [7](https://github.com/ghostty-org/ghostty/actions/runs/22253414227), [8](https://github.com/ghostty-org/ghostty/actions/runs/22250871348), [9](https://github.com/ghostty-org/ghostty/actions/runs/22250367020), [10](https://github.com/ghostty-org/ghostty/actions/runs/22250298660)  
Summary: 10 runs • 33 commits • 9 authors

### Changes

- [`27180d5`](https://github.com/ghostty-org/ghostty/commit/27180d560c6fa2094f54677246adaac760acf6d7) i18n: add 1.3 it_IT translations ([@Misairuzame](https://github.com/Misairuzame))
- [`b28b0b0`](https://github.com/ghostty-org/ghostty/commit/b28b0b02376a2a361d5ebcd22a3d6d7a47964685) Apply suggestions ([@Misairuzame](https://github.com/Misairuzame))
- [`5c7cf6d`](https://github.com/ghostty-org/ghostty/commit/5c7cf6dd70ddac7816787b88a53b7595da13580a) Merge branch 'ghostty-org:main' into i18n-it_IT-1.3-translation ([@Misairuzame](https://github.com/Misairuzame))
- [`a73c5b2`](https://github.com/ghostty-org/ghostty/commit/a73c5b2835396abe5cafc1bee6718c5b86275c85) Translate 3 additional strings ([@Misairuzame](https://github.com/Misairuzame))
- [`d991372`](https://github.com/ghostty-org/ghostty/commit/d991372bc8958f30114eee47a5a083fd9f9e31e4) translation update for lt_LT - filled in missing strings ([@tdslot](https://github.com/tdslot))
  ```text
  added translations for:
  - Open in Ghostty (Nautilus)
  - Change Tab Title menu/dialog
  
  all 74 messages done now
  ```
- [`850e9b5`](https://github.com/ghostty-org/ghostty/commit/850e9b58fced90947506a46ba0dda95aab0cbf8e) Merge branch 'main' into i18n-update-translation-lt-LT-for-v1.3 ([@tdslot](https://github.com/tdslot))
- [`266e910`](https://github.com/ghostty-org/ghostty/commit/266e910cd148d41e339a9a4c132b89698b924fd3) translation update for lt_LT - filled in missing strings ([#10886](https://github.com/ghostty-org/ghostty/issues/10886)) ([@00-kat](https://github.com/00-kat))
  ```text
  added translations for:
  - Open in Ghostty (Nautilus)
  - Change Tab Title menu/dialog
  
  all 74 messages done now
  ```
- [`1e380e8`](https://github.com/ghostty-org/ghostty/commit/1e380e8bf132b1993275e8e365aa6d46adb9cd8c) i18n: add 1.3 it_IT translations ([#10708](https://github.com/ghostty-org/ghostty/issues/10708)) ([@00-kat](https://github.com/00-kat))
  ```text
  Added the new Italian translations for 1.3.0. Any feedback is
  appreciated, as always!
  ```
- [`cdfa73b`](https://github.com/ghostty-org/ghostty/commit/cdfa73b403d2c7c26201311c9a7706da4ef11129) config: selection-word-chars parses escape sequences ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #10548
  
  Escaped characters in selection-word-chars are now correctly parsed,
  allowing for characters like `\t` to be included in the set of word
  characters.
  ```
- [`4f3e897`](https://github.com/ghostty-org/ghostty/commit/4f3e8971a0fcb75c39664081a381dffc36fde264) config: selection-word-chars parses escape sequences ([#10933](https://github.com/ghostty-org/ghostty/issues/10933)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #10548
  
  Escaped characters in selection-word-chars are now correctly parsed,
  allowing for characters like `\t` to be included in the set of word
  characters.
  ```
- [`3de6922`](https://github.com/ghostty-org/ghostty/commit/3de6922295782cec35e155cfb43635c1da8704ab) Update VOUCHED list ([#10936](https://github.com/ghostty-org/ghostty/issues/10936)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/10824) from
  @mitchellh.
  
  Vouch: @rgehan
  ```
- [`caec9e0`](https://github.com/ghostty-org/ghostty/commit/caec9e04d21db3bb1dabe2186529b6e5e9baa1f0) renderer: kitty image update requires draw_mutex ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #10680
  
  The image state is used for drawing, so when we update it, we need to
  acquire the draw mutex. All our other state updates already acquire the
  draw mutex but Kitty images are odd in that they happen in the critical
  area (due to their size).
  ```
- [`548930a`](https://github.com/ghostty-org/ghostty/commit/548930a7424b87beecfa9f6b5e7407e5f530a4de) renderer: kitty image update requires draw_mutex ([#10932](https://github.com/ghostty-org/ghostty/issues/10932)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fixes #10680
  
  The image state is used for drawing, so when we update it, we need to
  acquire the draw mutex. All our other state updates already acquire the
  draw mutex but Kitty images are odd in that they happen in the critical
  area (due to their size).
  ```
- [`dd29617`](https://github.com/ghostty-org/ghostty/commit/dd29617cd33225b865a3ba0e1a865f0c98142f23) macos: swiftlint 'multiple_closures_with_trailing_closure' rule ([@jparise](https://github.com/jparise))
  ```text
  Also, re-enable the 'force_cast' rule, which was addressed earlier.
  ```
- [`255b0c9`](https://github.com/ghostty-org/ghostty/commit/255b0c9964ad8c622be81c2f3f5a9f3a82c7e573) macos: swiftlint 'multiple_closures_with_trailing_closure' rule ([#10929](https://github.com/ghostty-org/ghostty/issues/10929)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Also, re-enable the 'force_cast' rule, which was addressed earlier.
  ```
- [`2e102b0`](https://github.com/ghostty-org/ghostty/commit/2e102b015facfa82432d09bd5d8151d239552800) Update VOUCHED list ([#10931](https://github.com/ghostty-org/ghostty/issues/10931)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/10840#issuecomment-3939561550)
  from @trag1c.
  
  Vouch: @JosephMart
  ```
- [`2e172ee`](https://github.com/ghostty-org/ghostty/commit/2e172eeb60b0096f2946eb631b2e8bc294e45c62) Update VOUCHED list ([#10927](https://github.com/ghostty-org/ghostty/issues/10927)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/10920) from
  @mitchellh.
  
  Vouch: @sunshine-syz
  ```
- [`407b3c0`](https://github.com/ghostty-org/ghostty/commit/407b3c082fb700be57ebf5c114b5d4f686c72c30) macos: fix new tab crash ([@tristan957](https://github.com/tristan957))
  ```text
  It was introduced in 2a81d8cd2910b12fe007f0bc5fb5d6be57f0f0fe[0]. We
  lost the subview. prefix of from the contains() call.
  
  Fixes: https://github.com/ghostty-org/ghostty/issues/10923
  Link: https://github.com/ghostty-org/ghostty/commit/2a81d8cd2910b12fe007f0bc5fb5d6be57f0f0fe [0]
  ```
- [`4581392`](https://github.com/ghostty-org/ghostty/commit/4581392625c09524ba330bba0b9fd37f4494d2de) macos: fix new tab crash ([#10924](https://github.com/ghostty-org/ghostty/issues/10924)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  It was introduced in 2a81d8cd2910b12fe007f0bc5fb5d6be57f0f0fe[0]. We
  lost the subview. prefix of from the contains() call.
  
  
  Fixes: https://github.com/ghostty-org/ghostty/issues/10923
  Link:
  https://github.com/ghostty-org/ghostty/commit/2a81d8cd2910b12fe007f0bc5fb5d6be57f0f0fe
  [0]
  ```
- [`791c949`](https://github.com/ghostty-org/ghostty/commit/791c94919059d73aa1df69eb034c9e105e85cbae) i18n/zh: update strings ([@pluiedev](https://github.com/pluiedev))
- [`02ca33d`](https://github.com/ghostty-org/ghostty/commit/02ca33d119eb46bb6eb07632caed98e989e21334) i18n/zh: update strings ([#10844](https://github.com/ghostty-org/ghostty/issues/10844)) ([@00-kat](https://github.com/00-kat))
  ```text
  See #10632
  ```
- [`f7e6639`](https://github.com/ghostty-org/ghostty/commit/f7e6639c43b9537f0fb4ebfa1544652c24a715ff) macos: swiftlint 'switch_case_alignment' rule ([@jparise](https://github.com/jparise))
- [`2d6fa92`](https://github.com/ghostty-org/ghostty/commit/2d6fa92d7837f3e19db495da9c159138380188a0) macos: swiftlint 'for_where' rule ([@jparise](https://github.com/jparise))
- [`b65261e`](https://github.com/ghostty-org/ghostty/commit/b65261eb6643ace961e5ea548c329b3cbd646c40) macOS: expand tilde in file paths before opening ([@AlexFeijoo44](https://github.com/AlexFeijoo44))
  ```text
  `URL(filePath:)` treats `~` as a literal directory name, so
  cmd-clicking a path like `~/Documents/file.txt` would fail to
  open because the resulting file URL doesn't point to a real file.
  
  Use `NSString.expandingTildeInPath` to resolve `~` to the user's
  home directory before constructing the file URL.
  ```
- [`6ec8744`](https://github.com/ghostty-org/ghostty/commit/6ec8744b16cbb2a35a86b89e4dbc7ca8ad43788c) macOS: expand tilde in file paths before opening ([#10863](https://github.com/ghostty-org/ghostty/issues/10863)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  ## Summary
  
  Cmd-clicking a file path containing `~` (e.g. `~/Documents/file.txt`)
  fails to open the file on macOS because `URL(filePath:)` treats `~` as a
  literal directory name rather than the user's home directory.
  
  This uses `NSString.expandingTildeInPath` to resolve `~` before
  constructing the file URL.
  
  ## Root Cause
  
  In `openURL()`, when the URL string has no scheme it falls through to:
  
  ```swift
  url = URL(filePath: action.url)
  ```
  
  Swift's `URL(filePath:)` does not perform tilde expansion. A path like
  `~/Documents/file.txt` produces a URL pointing to a non-existent file,
  and `NSWorkspace.open` silently fails.
  
  ## Fix
  
  ```swift
  let expandedPath = NSString(string: action.url).expandingTildeInPath
  url = URL(filePath: expandedPath)
  ```
  
  ## Reproduction
  
  1. Have a terminal application (e.g. Claude Code) that outputs file
  paths with `~` prefixes
  2. Cmd-click the path in Ghostty on macOS
  3. The file does not open (fails silently)
  
  With this fix, the path resolves correctly and opens in the default
  editor.
  ````
- [`ce46cae`](https://github.com/ghostty-org/ghostty/commit/ce46caeacb76f7056c2e82e86b7ffdc2099746e0) macos: swiftlint 'switch_case_alignment' rule ([#10908](https://github.com/ghostty-org/ghostty/issues/10908)) ([@mitchellh](https://github.com/mitchellh))
- [`7c50464`](https://github.com/ghostty-org/ghostty/commit/7c504649fd0b2b6d12a9a60a3e9c073315d09d64) ci: use explicit PAT with path-filter for higher rate limits ([@mitchellh](https://github.com/mitchellh))
- [`c17844c`](https://github.com/ghostty-org/ghostty/commit/c17844c2dbeba6c7186c8662191e4f5e3456a297) ci: use explicit PAT with path-filter for higher rate limits ([#10915](https://github.com/ghostty-org/ghostty/issues/10915)) ([@mitchellh](https://github.com/mitchellh))
- [`2a81d8c`](https://github.com/ghostty-org/ghostty/commit/2a81d8cd2910b12fe007f0bc5fb5d6be57f0f0fe) macos: swiftlint 'for_where' rule ([#10909](https://github.com/ghostty-org/ghostty/issues/10909)) ([@mitchellh](https://github.com/mitchellh))
- [`07a68b3`](https://github.com/ghostty-org/ghostty/commit/07a68b3e6521e74922fcc099ffb9e34d8f6a44ad) ci: use `every` to filter vouch paths ([@mitchellh](https://github.com/mitchellh))
  ```text
  The prior filter wasn't working because the default quantifier is
  `any`.
  ```
- [`1e7f470`](https://github.com/ghostty-org/ghostty/commit/1e7f470eb852ca8be509cdb77426a5b1c3bd1933) ci: use `every` to filter vouch paths ([#10913](https://github.com/ghostty-org/ghostty/issues/10913)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The prior filter wasn't working because the default quantifier is `any`.
  ```
- [`e7b8e73`](https://github.com/ghostty-org/ghostty/commit/e7b8e731eb60733cc09a04d9ddec383244f97d0e) Update VOUCHED list ([#10914](https://github.com/ghostty-org/ghostty/issues/10914)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/10581) from
  @mitchellh.
  
  Vouch: @neo773
  ```
- [`3404595`](https://github.com/ghostty-org/ghostty/commit/3404595c72d755d34c01fdb252a4b7fe8917c179) Update VOUCHED list ([#10912](https://github.com/ghostty-org/ghostty/issues/10912)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/10906) from
  @mitchellh.
  
  Vouch: @NateSmyth
  ```

