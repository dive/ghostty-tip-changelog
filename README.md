> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: April 16, 2026 at 04:03 UTC.

## April 15, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/24480459490), [2](https://github.com/ghostty-org/ghostty/actions/runs/24479115337), [3](https://github.com/ghostty-org/ghostty/actions/runs/24472495002)  
Summary: 3 runs • 11 commits • 4 authors

### Changes

- [`9e080c5`](https://github.com/ghostty-org/ghostty/commit/9e080c5a403475dcbee93c40eeb22cf6f92121f4) Update VOUCHED list ([#12302](https://github.com/ghostty-org/ghostty/issues/12302)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12301#issuecomment-4255856979)
  from @trag1c.
  
  Vouch: @bleikurr
  ```
- [`858e856`](https://github.com/ghostty-org/ghostty/commit/858e856e2e1c4572585f6e043876d7d2f0ef79b4) macOS: fix shortcuts not showing on menu item for `scroll_to_selection` and `search_selection` ([@bo2themax](https://github.com/bo2themax))
  ```text
  Incorrect link after 9b6a3be99339bcefcc49b7791b7b9761d24e6093 and 7d0157e69a7b8082b4c56baa466304768f68cbc6
  ```
- [`815ccb0`](https://github.com/ghostty-org/ghostty/commit/815ccb060b1f983272dab86af6bacb156dfcbfd9) terminal: fix viewport pin during resize reflow ([@mitchellh](https://github.com/mitchellh))
  ```text
  Maybe related to #12298?
  
  When Screen resize forwards the active cursor into PageList reflow, a
  history-pinned viewport can be remapped into the active area before the
  preserved-cursor grow step finishes. The old code kept treating that
  viewport as a history pin during the intermediate grow calls, which left
  too few rows beneath the pin and tripped the viewport integrity checks.
  
  Fix this by normalizing the viewport back to active as soon as reflow
  moves the pinned row into the active area. Add a Screen-level regression
  test that exercises the full resize path with bounded scrollback and
  wrapped rows, and document the setup so the unwrap and viewport
  transition are clear.
  ```
- [`551bf0a`](https://github.com/ghostty-org/ghostty/commit/551bf0af3fab6ff8b7567fc77b53698a944fce60) terminal: fix viewport pin during resize reflow ([#12300](https://github.com/ghostty-org/ghostty/issues/12300)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Maybe related to #12298?
  
  When Screen resize forwards the active cursor into PageList reflow, a
  history-pinned viewport can be remapped into the active area before the
  preserved-cursor grow step finishes. The old code kept treating that
  viewport as a history pin during the intermediate grow calls, which left
  too few rows beneath the pin and tripped the viewport integrity checks.
  
  Fix this by normalizing the viewport back to active as soon as reflow
  moves the pinned row into the active area. Add a Screen-level regression
  test that exercises the full resize path with bounded scrollback and
  wrapped rows, and document the setup so the unwrap and viewport
  transition are clear.
  ```
- [`d85051a`](https://github.com/ghostty-org/ghostty/commit/d85051a530690450148e558216d6f399ef978dfc) macOS: fix shortcuts not showing on menu item for `scroll_to_selection` and `search_selection` ([#12281](https://github.com/ghostty-org/ghostty/issues/12281)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  …
  
  Incorrect link after 9b6a3be99339bcefcc49b7791b7b9761d24e6093 and
  7d0157e69a7b8082b4c56baa466304768f68cbc6
  
  Reload following config and see the menu
  ```
  keybind = cmd+j=scroll_to_selection
  keybind = cmd+m=search_selection
  ```
  
  <img width="473" height="222" alt="image"
  src="https://github.com/user-attachments/assets/f92c6024-e7f4-496d-9aed-43103c21794d"
  />
  ````
- [`9c49c34`](https://github.com/ghostty-org/ghostty/commit/9c49c343569791071603d63138aa1a6f7d9dd2dc) benchmark: add AGENTS, improve UTF-8 synthetic data ([@mitchellh](https://github.com/mitchellh))
  ```text
  This updates our synthetic generator for UTF-8 to expose:
  
    - Flags to change 1/2/3/4-byte UTF-8 character distribution
    - Flags to have only printable characters so we can benchmark
      pure UTF-8 vs our control sequence finder.
    - Flags to have invalid characters so we can benchmark our error
      handling.
  
  This also adds an AGENTS.md to src/benchmark so agents can do the right
  thing more easily.
  ```
- [`29f92c0`](https://github.com/ghostty-org/ghostty/commit/29f92c0c8bb8428ccddb90efe095b114c3ff2950) benchmark: add AGENTS, improve UTF-8 synthetic data ([#12297](https://github.com/ghostty-org/ghostty/issues/12297)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This updates our synthetic generator for UTF-8 to expose:
  
    - Flags to change 1/2/3/4-byte UTF-8 character distribution
  - Flags to have only printable characters so we can benchmark pure UTF-8
  vs our control sequence finder.
  - Flags to have invalid characters so we can benchmark our error
  handling.
  
  This also adds an AGENTS.md to src/benchmark so agents can do the right
  thing more easily.
  
  These are necessary to robustly benchmark our libc++ removal PR.
  ```
- [`f53d3ab`](https://github.com/ghostty-org/ghostty/commit/f53d3ab8a35fe5a0cf077838e541bd450b09863a) nix: update to the latest zon2nix ([@jcollie](https://github.com/jcollie))
- [`efa8da6`](https://github.com/ghostty-org/ghostty/commit/efa8da6aea1e9cc099412c86405791bb0734ec0e) nix: update to the latest zon2nix ([#12299](https://github.com/ghostty-org/ghostty/issues/12299)) ([@mitchellh](https://github.com/mitchellh))
- [`e51de8b`](https://github.com/ghostty-org/ghostty/commit/e51de8b58faba2c851604b813e569f926910f522) libghostty: Remove all libc++ and libc++ ABI dependencies ([@mitchellh](https://github.com/mitchellh))
  ```text
  This updates simdutf to my fork which has a SIMDUTF_NO_LIBCXX option
  that removes all libc++ and libc++ ABI dependencies.
  
  From there, the hand-written simd code we have has been updated to also
  no longer use any libc++ features. Part of this required removing utfcpp
  since it depended on libc++ (`<iterator>`).
  
  libghostty-vt now only depends on libc.
  ```
- [`43a05dc`](https://github.com/ghostty-org/ghostty/commit/43a05dc968eda9bfa2196d66ba1819daf510b62a) libghostty: Remove all libc++ and libc++ ABI dependencies ([#12291](https://github.com/ghostty-org/ghostty/issues/12291)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This updates simdutf to my fork which has a SIMDUTF_NO_LIBCXX option
  that removes all libc++ and libc++ ABI dependencies. The plan is to open
  an upstream PR with this, but I want to verify it here first.
  
  From there, the hand-written simd code we have has been updated to also
  no longer use any libc++ features. Part of this required removing utfcpp
  since it depended on libc++ (`<iterator>`).
  
  libghostty-vt now only depends on libc.
  
  ## Benchmark Results
  
  | Corpus | Current `HEAD` median | `main` median | Delta vs `main` |
  Notes |
  | --- | ---: | ---: | ---: | --- |
  | `valid-mixed-1g-seed1.bin` | `9.245s` | `9.111s` | `1.5%` slower |
  Near tie; `main` remains slightly faster on fully valid input |
  | `malformed-mixed-1g-seed1-rate0.005.bin` | `9.251s` | `12.705s` |
  `37.3%` faster | Large improvement on malformed UTF-8 input |
  
  Approximate throughput from the medians:
  
  - Valid corpus: current `HEAD` `110.8 MiB/s`, `main` `112.4 MiB/s`
  - Malformed corpus: current `HEAD` `110.7 MiB/s`, `main` `80.6 MiB/s`
  ```

## April 14, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/24422513385), [2](https://github.com/ghostty-org/ghostty/actions/runs/24404590083)  
Summary: 2 runs • 4 commits • 3 authors

### Changes

- [`49a43bf`](https://github.com/ghostty-org/ghostty/commit/49a43bf560322eac0ba5d30c20a8b212106e3883) Update VOUCHED list ([#12285](https://github.com/ghostty-org/ghostty/issues/12285)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12284#issuecomment-4247088526)
  from @trag1c.
  
  Vouch: @illiakrauchanka
  ```
- [`fe8a646`](https://github.com/ghostty-org/ghostty/commit/fe8a6464b94e7f11a3514627b8344442ab9e63c4) macOS: update MenuShortcutKey ([@bo2themax](https://github.com/bo2themax))
- [`6033c12`](https://github.com/ghostty-org/ghostty/commit/6033c12790aaf0e9e7cee44118aa8745c4dfaadd) macOS: reset menu shortcuts when its not updated ([@bo2themax](https://github.com/bo2themax))
- [`79a470d`](https://github.com/ghostty-org/ghostty/commit/79a470d9a3b0a2b2cde3e939f0cb25968a162183) macOS: refactor MenuShortcutManager ([#12271](https://github.com/ghostty-org/ghostty/issues/12271)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Closes #11995
  
  Yet another small step to fix menu shortcut-related issues.
  
  1. Create `MenuShortcutKey` from `NSMenuItem` and `KeyboardShortcut`.
  2. Add `updateMenuShortcut` to update to Ghostty ones only.
  
  Doesn't contain any actual changes to pass previous test cases.
  ```

## April 13, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/24348683917), [2](https://github.com/ghostty-org/ghostty/actions/runs/24347722200), [3](https://github.com/ghostty-org/ghostty/actions/runs/24323184090)  
Summary: 3 runs • 26 commits • 5 authors

### Changes

- [`158b976`](https://github.com/ghostty-org/ghostty/commit/158b97607c8404e5f8a0d0589b56b83462aacdce) Update VOUCHED list ([#12268](https://github.com/ghostty-org/ghostty/issues/12268)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12267#issuecomment-4237110063)
  from @mitchellh.
  
  Vouch: @0xDVC
  ```
- [`aea70a5`](https://github.com/ghostty-org/ghostty/commit/aea70a5f7c48c40177077992fe6318fc643f86ca) core: implement backarrow key mode (DECBKM) - mode 67 ([@jcollie](https://github.com/jcollie))
  ```text
  This mode allows programs to modify the code that the `backspace`
  key (backarrow key in DEC parlance) sends. If this mode is
  `off`/`false`/`reset` (the default, the same as before this PR), we
  send the byte `0x7f`. If this mode is `on`/`true`/`set` we send the
  byte `0x08`.
  ```
- [`203895e`](https://github.com/ghostty-org/ghostty/commit/203895e3f76af0e3f9a8e16778a706d08f6718f1) decbkm: address review comments ([@jcollie](https://github.com/jcollie))
  ```text
  * Don't alter Kitty keyboard protocol responses. Kitty does not support
    DECBKM so KKP doesn't take DECBKM into consideration.
  * Make better use of the function key lookup to control what sequence is
    returned when backspace is pressed using the legacy encoding.
  ```
- [`de4992c`](https://github.com/ghostty-org/ghostty/commit/de4992c2b273ea701008c2fe4a7b39e9276f6818) decbkm: use if statements instead of named blocks ([@jcollie](https://github.com/jcollie))
- [`3a9ae7a`](https://github.com/ghostty-org/ghostty/commit/3a9ae7a0f28791e3ab451954c63d72142ad3ccf4) decbkm: expose DECBKM to libghostty-vt ([@jcollie](https://github.com/jcollie))
- [`f29d5d4`](https://github.com/ghostty-org/ghostty/commit/f29d5d415053e8cda87e23e8c9f8aa2b22dfc0c3) zon2nix: update to a version that is compatible with Zig 0.16 ([@jcollie](https://github.com/jcollie))
  ```text
  The `zon2nix` binary is now compiled with Zig 0.16, but it still produces
  Zig 0.15 compatible output (in fact the output is identical to previous
  versions).
  ```
- [`1443e7a`](https://github.com/ghostty-org/ghostty/commit/1443e7a9cd1a1d579f8fa54faa5f000ed6772f0c) zon2nix: use github mirror ([@jcollie](https://github.com/jcollie))
- [`c2a93db`](https://github.com/ghostty-org/ghostty/commit/c2a93db591a55988d78f1010219efdf7d3ed7880) macOS: move url hover to a separate file ([@bo2themax](https://github.com/bo2themax))
- [`38e64c3`](https://github.com/ghostty-org/ghostty/commit/38e64c3706b9bc12e9191f4deaf6f37a717afe95) macOS: add bottom bar when child exits ([@bo2themax](https://github.com/bo2themax))
- [`2bdc6bb`](https://github.com/ghostty-org/ghostty/commit/2bdc6bb1f7f2a6093d1e50484fba4aac9e7334a7) macOS: Highlight matching text in command palette search results ([@bo2themax](https://github.com/bo2themax))
  ```text
  Add String.matchedIndices(for:) to find substring matches and use
  it to bold and tint matched characters with the accent color in
  both titles and subtitles. Title matches take priority — subtitles
  are only highlighted when the title didn't match.
  ```
- [`2e169c4`](https://github.com/ghostty-org/ghostty/commit/2e169c42e8334bdd343b17cd3489281d32cd5044) macOS: Support initials matching in command palette search ([@bo2themax](https://github.com/bo2themax))
  ```text
  Extend String.matchedIndices(for:) to fall back to initials
  matching when no substring match is found. Typing the first letter
  of each word now matches commands, e.g. "tbo" matches "Toggle
  Background Opacity", with each matched initial highlighted.
  ```
- [`073dd8a`](https://github.com/ghostty-org/ghostty/commit/073dd8a39974d19e482a093c2f070d18deca3cc7) macOS: trim query before filtering commands ([@bo2themax](https://github.com/bo2themax))
- [`fab8777`](https://github.com/ghostty-org/ghostty/commit/fab8777931b55092ec4bcdd37fb99683bbf2c781) core: implement backarrow key mode (DECBKM) - mode 67 ([#12226](https://github.com/ghostty-org/ghostty/issues/12226)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This mode allows programs to modify the code that the `backspace` key
  (backarrow key in DEC parlance) sends. If this mode is
  `off`/`false`/`reset` (the default, the same as before this PR), we send
  the byte `0x7f`. If this mode is `on`/`true`/`set` we send the byte
  `0x08`.
  
  <img width="659" height="715" alt="Screenshot From 2026-04-09 11-00-25"
  src="https://github.com/user-attachments/assets/4f3e14ac-757d-4bb2-9fc5-b17019ad35d5"
  />
  ```
- [`ec434ec`](https://github.com/ghostty-org/ghostty/commit/ec434ec096265e39dcd31453ae3affc992013a58) zon2nix: update to a version that is compatible with Zig 0.16 ([#12259](https://github.com/ghostty-org/ghostty/issues/12259)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The `zon2nix` binary is now compiled with Zig 0.16, but it still
  produces Zig 0.15 compatible output (in fact the output is identical to
  previous versions).
  ```
- [`4699a3f`](https://github.com/ghostty-org/ghostty/commit/4699a3f7955543a6e027e0baeaf1b7c442bc8c8d) macOS: Command palette highlight matches ([#12264](https://github.com/ghostty-org/ghostty/issues/12264)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  - Highlight matching text in command palette search results
  - Support initials matching
  - Trim query before filtering commands
  
  ### AI Disclosure
  
  Claude wrote most of it. I tested and reviewed it myself.
  
  <img width="1544" height="297" alt="image"
  src="https://github.com/user-attachments/assets/6ed98538-d6d3-48a0-8bb0-ac705611d058"
  />
  ```
- [`4f36896`](https://github.com/ghostty-org/ghostty/commit/4f36896ddb6a1738d4b9d28b541b24bee89e2f30) macOS: add bottom bar when child exits ([#12251](https://github.com/ghostty-org/ghostty/issues/12251)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ### Closes #7649
  
  The bar lives alongside URL Hover in VStack at the bottom. The current
  body of SurfaceView is becoming rather long and complicated, so this pr
  also contains some refactors:
  
  - Move URL Hover to a separate file
  
  > The text is copied from previous input string to keep it consistent,
  also I’m confused with text on GTK so this is my first choice, but it
  can be changed as the same as GTK.
  
  Separate prs will be opened for:
  1. Set to Read-only after exits
  2. Hide cursor when in Read-only
  
  ### Preview
  
  
  https://github.com/user-attachments/assets/eb44e211-eac5-4f40-836c-4912b18dfb01
  ```
- [`ea2753b`](https://github.com/ghostty-org/ghostty/commit/ea2753b8191a9f6ca0c61e0043781e4877135989) build(deps): bump softprops/action-gh-release from 2.6.1 to 3.0.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [softprops/action-gh-release](https://github.com/softprops/action-gh-release) from 2.6.1 to 3.0.0.
  - [Release notes](https://github.com/softprops/action-gh-release/releases)
  - [Changelog](https://github.com/softprops/action-gh-release/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/softprops/action-gh-release/compare/153bb8e04406b158c6c84fc1615b65b24149a1fe...b4309332981a82ec1c5618f44dd2e27cc8bfbfda)
  
  ---
  updated-dependencies:
  - dependency-name: softprops/action-gh-release
    dependency-version: 3.0.0
    dependency-type: direct:production
    update-type: version-update:semver-major
  ...
  ```
- [`b0cfc59`](https://github.com/ghostty-org/ghostty/commit/b0cfc595f244233eb514ddeb006c1e00fe191382) build(deps): bump peter-evans/create-pull-request from 8.1.0 to 8.1.1 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [peter-evans/create-pull-request](https://github.com/peter-evans/create-pull-request) from 8.1.0 to 8.1.1.
  - [Release notes](https://github.com/peter-evans/create-pull-request/releases)
  - [Commits](https://github.com/peter-evans/create-pull-request/compare/c0f553fe549906ede9cf27b5156039d195d2ece0...5f6978faf089d4d20b00c7766989d076bb2fc7f1)
  
  ---
  updated-dependencies:
  - dependency-name: peter-evans/create-pull-request
    dependency-version: 8.1.1
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`470605f`](https://github.com/ghostty-org/ghostty/commit/470605f0abf9264d4ba5ce846e09d8a484153295) build(deps): bump docker/build-push-action from 7.0.0 to 7.1.0 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [docker/build-push-action](https://github.com/docker/build-push-action) from 7.0.0 to 7.1.0.
  - [Release notes](https://github.com/docker/build-push-action/releases)
  - [Commits](https://github.com/docker/build-push-action/compare/d08e5c354a6adb9ed34480a06d141179aa583294...bcafcacb16a39f128d818304e6c9c0c18556b85f)
  
  ---
  updated-dependencies:
  - dependency-name: docker/build-push-action
    dependency-version: 7.1.0
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`c2a1ac5`](https://github.com/ghostty-org/ghostty/commit/c2a1ac5866b1ea1a77692c7890522cf6d27b2779) build(deps): bump actions/create-github-app-token from 3.0.0 to 3.1.1 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [actions/create-github-app-token](https://github.com/actions/create-github-app-token) from 3.0.0 to 3.1.1.
  - [Release notes](https://github.com/actions/create-github-app-token/releases)
  - [Commits](https://github.com/actions/create-github-app-token/compare/f8d387b68d61c58ab83c6c016672934102569859...1b10c78c7865c340bc4f6099eb2f838309f1e8c3)
  
  ---
  updated-dependencies:
  - dependency-name: actions/create-github-app-token
    dependency-version: 3.1.1
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`e30c2bd`](https://github.com/ghostty-org/ghostty/commit/e30c2bd86b7758840292c8dce4fc11c2261bd9fd) build(deps): bump actions/upload-artifact from 7.0.0 to 7.0.1 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [actions/upload-artifact](https://github.com/actions/upload-artifact) from 7.0.0 to 7.0.1.
  - [Release notes](https://github.com/actions/upload-artifact/releases)
  - [Commits](https://github.com/actions/upload-artifact/compare/bbbca2ddaa5d8feaa63e36b76fdaad77386f024f...043fb46d1a93c77aae656e7c1c64a875d1fc6a0a)
  
  ---
  updated-dependencies:
  - dependency-name: actions/upload-artifact
    dependency-version: 7.0.1
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`3ef500b`](https://github.com/ghostty-org/ghostty/commit/3ef500b3c8551019956f9875c17f3c9c59de2e2a) build(deps): bump softprops/action-gh-release from 2.6.1 to 3.0.0 ([#12254](https://github.com/ghostty-org/ghostty/issues/12254)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [softprops/action-gh-release](https://github.com/softprops/action-gh-release)
  from 2.6.1 to 3.0.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/softprops/action-gh-release/releases">softprops/action-gh-release's
  releases</a>.</em></p>
  <blockquote>
  <h2>v3.0.0</h2>
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
  <h2>v2.6.2</h2>
  <!-- raw HTML omitted -->
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
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/softprops/action-gh-release/compare/v2...v2.6.2">https://github.com/softprops/action-gh-release/compare/v2...v2.6.2</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Changelog</summary>
  <p><em>Sourced from <a
  href="https://github.com/softprops/action-gh-release/blob/master/CHANGELOG.md">softprops/action-gh-release's
  changelog</a>.</em></p>
  <blockquote>
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
  <p>If you still hit an issue after upgrading, please open a report with
  the bug template and include a minimal repro or sanitized workflow
  snippet where possible.</p>
  <h2>What's Changed</h2>
  <!-- raw HTML omitted -->
  </blockquote>
  <p>... (truncated)</p>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/b4309332981a82ec1c5618f44dd2e27cc8bfbfda"><code>b430933</code></a>
  release: cut v3.0.0 for Node 24 upgrade (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/670">#670</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/c2e35e05a74208bafbfcbdae5ebc9da7236e980f"><code>c2e35e0</code></a>
  chore(deps): bump the npm group across 1 directory with 7 updates (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/783">#783</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/3bb12739c298aeb8a4eeaf626c5b8d85266b0e65"><code>3bb1273</code></a>
  release 2.6.2</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/c34030fec99b0db0f2f22ce7806c445dddb6e224"><code>c34030f</code></a>
  chore: bump node to 24.14.1</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/8975bd05c0630603edb0dca2fc7544bf1c77f600"><code>8975bd0</code></a>
  chore(deps): bump vite from 8.0.0 to 8.0.5 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/781">#781</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/f71937f44d5662ac6eb861431746174a7b46a7b6"><code>f71937f</code></a>
  chore(deps): bump brace-expansion from 5.0.4 to 5.0.5 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/777">#777</a>)</li>
  <li><a
  href="https://github.com/softprops/action-gh-release/commit/3f0d239d58d5c226738ec0a08d0465b548dc026f"><code>3f0d239</code></a>
  chore(deps): bump picomatch from 4.0.3 to 4.0.4 (<a
  href="https://redirect.github.com/softprops/action-gh-release/issues/775">#775</a>)</li>
  <li>See full diff in <a
  href="https://github.com/softprops/action-gh-release/compare/153bb8e04406b158c6c84fc1615b65b24149a1fe...b4309332981a82ec1c5618f44dd2e27cc8bfbfda">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=softprops/action-gh-release&package-manager=github_actions&previous-version=2.6.1&new-version=3.0.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`922b610`](https://github.com/ghostty-org/ghostty/commit/922b61063292595133b2943c76027cfa9ca7855f) build(deps): bump peter-evans/create-pull-request from 8.1.0 to 8.1.1 ([#12255](https://github.com/ghostty-org/ghostty/issues/12255)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [peter-evans/create-pull-request](https://github.com/peter-evans/create-pull-request)
  from 8.1.0 to 8.1.1.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/peter-evans/create-pull-request/releases">peter-evans/create-pull-request's
  releases</a>.</em></p>
  <blockquote>
  <h2>Create Pull Request v8.1.1</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>build(deps-dev): bump the npm group with 2 updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4305">peter-evans/create-pull-request#4305</a></li>
  <li>build(deps): bump minimatch by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4311">peter-evans/create-pull-request#4311</a></li>
  <li>build(deps): bump the github-actions group with 2 updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4316">peter-evans/create-pull-request#4316</a></li>
  <li>build(deps): bump <code>@​tootallnate/once</code> and
  jest-environment-jsdom by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4323">peter-evans/create-pull-request#4323</a></li>
  <li>build(deps-dev): bump undici from 6.23.0 to 6.24.0 by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4328">peter-evans/create-pull-request#4328</a></li>
  <li>build(deps-dev): bump flatted from 3.3.1 to 3.4.2 by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4334">peter-evans/create-pull-request#4334</a></li>
  <li>build(deps): bump picomatch by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4339">peter-evans/create-pull-request#4339</a></li>
  <li>build(deps-dev): bump handlebars from 4.7.8 to 4.7.9 by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4344">peter-evans/create-pull-request#4344</a></li>
  <li>build(deps-dev): bump the npm group with 3 updates by <a
  href="https://github.com/dependabot"><code>@​dependabot</code></a>[bot]
  in <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4349">peter-evans/create-pull-request#4349</a></li>
  <li>fix: retry post-creation API calls on 422 eventual consistency
  errors by <a
  href="https://github.com/peter-evans"><code>@​peter-evans</code></a> in
  <a
  href="https://redirect.github.com/peter-evans/create-pull-request/pull/4356">peter-evans/create-pull-request#4356</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/peter-evans/create-pull-request/compare/v8.1.0...v8.1.1">https://github.com/peter-evans/create-pull-request/compare/v8.1.0...v8.1.1</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/peter-evans/create-pull-request/commit/5f6978faf089d4d20b00c7766989d076bb2fc7f1"><code>5f6978f</code></a>
  fix: retry post-creation API calls on 422 eventual consistency errors
  (<a
  href="https://redirect.github.com/peter-evans/create-pull-request/issues/4356">#4356</a>)</li>
  <li><a
  href="https://github.com/peter-evans/create-pull-request/commit/d32e88dac789dcc7906e7d26f69f24116fa9c97d"><code>d32e88d</code></a>
  build(deps-dev): bump the npm group with 3 updates (<a
  href="https://redirect.github.com/peter-evans/create-pull-request/issues/4349">#4349</a>)</li>
  <li><a
  href="https://github.com/peter-evans/create-pull-request/commit/8170bccad11c0df62542c04dcaefe36d342dfd39"><code>8170bcc</code></a>
  build(deps-dev): bump handlebars from 4.7.8 to 4.7.9 (<a
  href="https://redirect.github.com/peter-evans/create-pull-request/issues/4344">#4344</a>)</li>
  <li><a
  href="https://github.com/peter-evans/create-pull-request/commit/00418193b417f888dbf1d993c5c0d31d27fdc7de"><code>0041819</code></a>
  build(deps): bump picomatch (<a
  href="https://redirect.github.com/peter-evans/create-pull-request/issues/4339">#4339</a>)</li>
  <li><a
  href="https://github.com/peter-evans/create-pull-request/commit/b993918c8536b6d44706130734d5456879762b27"><code>b993918</code></a>
  build(deps-dev): bump flatted from 3.3.1 to 3.4.2 (<a
  href="https://redirect.github.com/peter-evans/create-pull-request/issues/4334">#4334</a>)</li>
  <li><a
  href="https://github.com/peter-evans/create-pull-request/commit/36d7c8468b48f9c2f8f29e260e82f10d4b90d2bd"><code>36d7c84</code></a>
  build(deps-dev): bump undici from 6.23.0 to 6.24.0 (<a
  href="https://redirect.github.com/peter-evans/create-pull-request/issues/4328">#4328</a>)</li>
  <li><a
  href="https://github.com/peter-evans/create-pull-request/commit/a45d1fb447fcaf601166e405fd4f335cde1a8aa8"><code>a45d1fb</code></a>
  build(deps): bump <code>@​tootallnate/once</code> and
  jest-environment-jsdom (<a
  href="https://redirect.github.com/peter-evans/create-pull-request/issues/4323">#4323</a>)</li>
  <li><a
  href="https://github.com/peter-evans/create-pull-request/commit/3499eb61835cc0015c0b786e203d74b1e8f55e43"><code>3499eb6</code></a>
  build(deps): bump the github-actions group with 2 updates (<a
  href="https://redirect.github.com/peter-evans/create-pull-request/issues/4316">#4316</a>)</li>
  <li><a
  href="https://github.com/peter-evans/create-pull-request/commit/3f3b473b8c148f5a7520efb4d1f9a70eea3d9d1f"><code>3f3b473</code></a>
  build(deps): bump minimatch (<a
  href="https://redirect.github.com/peter-evans/create-pull-request/issues/4311">#4311</a>)</li>
  <li><a
  href="https://github.com/peter-evans/create-pull-request/commit/6699836a213cf8b28c4f0408a404a6ac79d4458a"><code>6699836</code></a>
  build(deps-dev): bump the npm group with 2 updates (<a
  href="https://redirect.github.com/peter-evans/create-pull-request/issues/4305">#4305</a>)</li>
  <li>See full diff in <a
  href="https://github.com/peter-evans/create-pull-request/compare/c0f553fe549906ede9cf27b5156039d195d2ece0...5f6978faf089d4d20b00c7766989d076bb2fc7f1">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=peter-evans/create-pull-request&package-manager=github_actions&previous-version=8.1.0&new-version=8.1.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`2c9f57f`](https://github.com/ghostty-org/ghostty/commit/2c9f57f8b0de77a2296da82472db1b3ae99ed646) build(deps): bump docker/build-push-action from 7.0.0 to 7.1.0 ([#12256](https://github.com/ghostty-org/ghostty/issues/12256)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [docker/build-push-action](https://github.com/docker/build-push-action)
  from 7.0.0 to 7.1.0.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/docker/build-push-action/releases">docker/build-push-action's
  releases</a>.</em></p>
  <blockquote>
  <h2>v7.1.0</h2>
  <ul>
  <li>Git context <a
  href="https://docs.docker.com/build/concepts/context/#url-queries">query
  format</a> support by <a
  href="https://github.com/crazy-max"><code>@​crazy-max</code></a> in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1505">docker/build-push-action#1505</a></li>
  <li>Bump <code>@​docker/actions-toolkit</code> from 0.79.0 to 0.87.0 by
  <a href="https://github.com/crazy-max"><code>@​crazy-max</code></a> in
  <a
  href="https://redirect.github.com/docker/build-push-action/pull/1505">docker/build-push-action#1505</a></li>
  <li>Bump brace-expansion from 1.1.12 to 1.1.13 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1500">docker/build-push-action#1500</a></li>
  <li>Bump fast-xml-parser from 5.4.2 to 5.5.7 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1489">docker/build-push-action#1489</a></li>
  <li>Bump flatted from 3.3.3 to 3.4.2 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1491">docker/build-push-action#1491</a></li>
  <li>Bump glob from 10.3.12 to 10.5.0 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1490">docker/build-push-action#1490</a></li>
  <li>Bump handlebars from 4.7.8 to 4.7.9 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1497">docker/build-push-action#1497</a></li>
  <li>Bump lodash from 4.17.23 to 4.18.1 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1510">docker/build-push-action#1510</a></li>
  <li>Bump picomatch from 4.0.3 to 4.0.4 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1496">docker/build-push-action#1496</a></li>
  <li>Bump undici from 6.23.0 to 6.24.1 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1486">docker/build-push-action#1486</a></li>
  <li>Bump vite from 7.3.1 to 7.3.2 in <a
  href="https://redirect.github.com/docker/build-push-action/pull/1509">docker/build-push-action#1509</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/docker/build-push-action/compare/v7.0.0...v7.1.0">https://github.com/docker/build-push-action/compare/v7.0.0...v7.1.0</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/docker/build-push-action/commit/bcafcacb16a39f128d818304e6c9c0c18556b85f"><code>bcafcac</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1509">#1509</a>
  from docker/dependabot/npm_and_yarn/vite-7.3.2</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/18e62f1158d9c45a4a84a58a6828d21f8ed3644b"><code>18e62f1</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1510">#1510</a>
  from docker/dependabot/npm_and_yarn/lodash-4.18.1</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/46580d2c9d43b0888270cb6fa90956e483de56fc"><code>46580d2</code></a>
  chore: update generated content</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/3f80b252ca2331f6ec3e890f4346b5506ee1dc81"><code>3f80b25</code></a>
  chore(deps): Bump lodash from 4.17.23 to 4.18.1</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/efeec9557c40a646afe433e39a1e94ca689103f0"><code>efeec95</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1505">#1505</a>
  from crazy-max/refactor-git-context</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/ddf04b08eb12882258ed936fea4a2806754ff349"><code>ddf04b0</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1511">#1511</a>
  from docker/dependabot/github_actions/crazy-max-dot-...</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/db08d97a08e4a0d15f85d1c4e64dfd5f88cbe1a9"><code>db08d97</code></a>
  chore(deps): Bump the crazy-max-dot-github group with 2 updates</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/ef1fb9688fc3626d0fd5e462f502cbbdc6456feb"><code>ef1fb96</code></a>
  Merge pull request <a
  href="https://redirect.github.com/docker/build-push-action/issues/1508">#1508</a>
  from docker/dependabot/github_actions/docker/login-a...</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/2d8f2a1a378a5c302dcd7b2b4326cefa24180bb1"><code>2d8f2a1</code></a>
  chore: update generated content</li>
  <li><a
  href="https://github.com/docker/build-push-action/commit/919ac7bd7d1aa8cb13fe4de76545abea8d8b5ed2"><code>919ac7b</code></a>
  fix test since secrets are not written to temp path anymore</li>
  <li>Additional commits viewable in <a
  href="https://github.com/docker/build-push-action/compare/d08e5c354a6adb9ed34480a06d141179aa583294...bcafcacb16a39f128d818304e6c9c0c18556b85f">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=docker/build-push-action&package-manager=github_actions&previous-version=7.0.0&new-version=7.1.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`6b97d91`](https://github.com/ghostty-org/ghostty/commit/6b97d911dfb8f68b76d36ee4df8d1e1170db9754) build(deps): bump actions/create-github-app-token from 3.0.0 to 3.1.1 ([#12257](https://github.com/ghostty-org/ghostty/issues/12257)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [actions/create-github-app-token](https://github.com/actions/create-github-app-token)
  from 3.0.0 to 3.1.1.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/actions/create-github-app-token/releases">actions/create-github-app-token's
  releases</a>.</em></p>
  <blockquote>
  <h2>v3.1.1</h2>
  <h2><a
  href="https://github.com/actions/create-github-app-token/compare/v3.1.0...v3.1.1">3.1.1</a>
  (2026-04-11)</h2>
  <h3>Bug Fixes</h3>
  <ul>
  <li>improve error message when app identifier is empty (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/362">#362</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/07e2b760664f080c40eec4eacf7477256582db36">07e2b76</a>),
  closes <a
  href="https://redirect.github.com/actions/create-github-app-token/issues/249">#249</a></li>
  </ul>
  <h2>v3.1.0</h2>
  <h1><a
  href="https://github.com/actions/create-github-app-token/compare/v3.0.0...v3.1.0">3.1.0</a>
  (2026-04-11)</h1>
  <h3>Bug Fixes</h3>
  <ul>
  <li><strong>deps:</strong> bump p-retry from 7.1.1 to 8.0.0 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/357">#357</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/3bbe07d928e2d6c30bf3e37c6b89edbc4045facf">3bbe07d</a>)</li>
  </ul>
  <h3>Features</h3>
  <ul>
  <li>add <code>client-id</code> input and deprecate <code>app-id</code>
  (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/353">#353</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/e6bd4e6970172bed9fe138b2eaf4cbffa4cca8f9">e6bd4e6</a>)</li>
  <li>update permission inputs (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/358">#358</a>)
  (<a
  href="https://github.com/actions/create-github-app-token/commit/076e9480ca6e9633bff412d05eff0fc2f1e7d2be">076e948</a>)</li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/1b10c78c7865c340bc4f6099eb2f838309f1e8c3"><code>1b10c78</code></a>
  build(release): 3.1.1 [skip ci]</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/07e2b760664f080c40eec4eacf7477256582db36"><code>07e2b76</code></a>
  fix: improve error message when app identifier is empty (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/362">#362</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/ea0121618bb39abc1cff180c258978a02d4e04fd"><code>ea01216</code></a>
  ci: remove publish-immutable-action workflow (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/361">#361</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/7bd03711494f032dfa3be3558f7dc8787b0be333"><code>7bd0371</code></a>
  build(release): 3.1.0 [skip ci]</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/e6bd4e6970172bed9fe138b2eaf4cbffa4cca8f9"><code>e6bd4e6</code></a>
  feat: add <code>client-id</code> input and deprecate <code>app-id</code>
  (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/353">#353</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/076e9480ca6e9633bff412d05eff0fc2f1e7d2be"><code>076e948</code></a>
  feat: update permission inputs (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/358">#358</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/3bbe07d928e2d6c30bf3e37c6b89edbc4045facf"><code>3bbe07d</code></a>
  fix(deps): bump p-retry from 7.1.1 to 8.0.0 (<a
  href="https://redirect.github.com/actions/create-github-app-token/issues/357">#357</a>)</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/28a99e369c23d11dbaf8e9ff29e577c7129aaa6c"><code>28a99e3</code></a>
  build(deps-dev): bump c8 from 10.1.3 to 11.0.0</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/4df50600ef5eaf70cb3514fbb1716e183ec4b25d"><code>4df5060</code></a>
  build(deps-dev): bump open-cli from 8.0.0 to 9.0.0</li>
  <li><a
  href="https://github.com/actions/create-github-app-token/commit/4843c538d99b70fef283d0c8a7e12a8f4c9a7b70"><code>4843c53</code></a>
  build(deps-dev): bump the development-dependencies group with 3
  updates</li>
  <li>See full diff in <a
  href="https://github.com/actions/create-github-app-token/compare/f8d387b68d61c58ab83c6c016672934102569859...1b10c78c7865c340bc4f6099eb2f838309f1e8c3">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=actions/create-github-app-token&package-manager=github_actions&previous-version=3.0.0&new-version=3.1.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`0182541`](https://github.com/ghostty-org/ghostty/commit/01825411ab2720e47e6902e9464e805bc6a062a1) build(deps): bump actions/upload-artifact from 7.0.0 to 7.0.1 ([#12258](https://github.com/ghostty-org/ghostty/issues/12258)) ([@jcollie](https://github.com/jcollie))
  ```text
  Bumps
  [actions/upload-artifact](https://github.com/actions/upload-artifact)
  from 7.0.0 to 7.0.1.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/actions/upload-artifact/releases">actions/upload-artifact's
  releases</a>.</em></p>
  <blockquote>
  <h2>v7.0.1</h2>
  <h2>What's Changed</h2>
  <ul>
  <li>Update the readme with direct upload details by <a
  href="https://github.com/danwkennedy"><code>@​danwkennedy</code></a> in
  <a
  href="https://redirect.github.com/actions/upload-artifact/pull/795">actions/upload-artifact#795</a></li>
  <li>Readme: bump all the example versions to v7 by <a
  href="https://github.com/danwkennedy"><code>@​danwkennedy</code></a> in
  <a
  href="https://redirect.github.com/actions/upload-artifact/pull/796">actions/upload-artifact#796</a></li>
  <li>Include changes in typespec/ts-http-runtime 0.3.5 by <a
  href="https://github.com/yacaovsnc"><code>@​yacaovsnc</code></a> in <a
  href="https://redirect.github.com/actions/upload-artifact/pull/797">actions/upload-artifact#797</a></li>
  </ul>
  <p><strong>Full Changelog</strong>: <a
  href="https://github.com/actions/upload-artifact/compare/v7...v7.0.1">https://github.com/actions/upload-artifact/compare/v7...v7.0.1</a></p>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/actions/upload-artifact/commit/043fb46d1a93c77aae656e7c1c64a875d1fc6a0a"><code>043fb46</code></a>
  Merge pull request <a
  href="https://redirect.github.com/actions/upload-artifact/issues/797">#797</a>
  from actions/yacaovsnc/update-dependency</li>
  <li><a
  href="https://github.com/actions/upload-artifact/commit/634250c1388765ea7ed0f053e636f1f399000b94"><code>634250c</code></a>
  Include changes in typespec/ts-http-runtime 0.3.5</li>
  <li><a
  href="https://github.com/actions/upload-artifact/commit/e454baaac2be505c9450e11b8f3215c6fc023ce8"><code>e454baa</code></a>
  Readme: bump all the example versions to v7 (<a
  href="https://redirect.github.com/actions/upload-artifact/issues/796">#796</a>)</li>
  <li><a
  href="https://github.com/actions/upload-artifact/commit/74fad66b98a6d799dc004d3353ccd0e6f6b2530e"><code>74fad66</code></a>
  Update the readme with direct upload details (<a
  href="https://redirect.github.com/actions/upload-artifact/issues/795">#795</a>)</li>
  <li>See full diff in <a
  href="https://github.com/actions/upload-artifact/compare/bbbca2ddaa5d8feaa63e36b76fdaad77386f024f...043fb46d1a93c77aae656e7c1c64a875d1fc6a0a">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=actions/upload-artifact&package-manager=github_actions&previous-version=7.0.0&new-version=7.0.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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

## April 12, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/24315826889)  
Summary: 1 runs • 26 commits • 4 authors

### Changes

- [`30fdc8f`](https://github.com/ghostty-org/ghostty/commit/30fdc8f4c881c309199bd75086b52962e3ed344c) macOS: fix cannot rebind super+up and super+down ([@otomn](https://github.com/otomn))
- [`dd04856`](https://github.com/ghostty-org/ghostty/commit/dd04856482d3c38746da989901b1cdeeb8580c7c) build: add ghostty-internal pkg-config modules (shared + static) ([@deblasis](https://github.com/deblasis))
- [`4fd16ef`](https://github.com/ghostty-org/ghostty/commit/4fd16ef9bcb73e19c2fdb406107803f819dc7d92) build: install ghostty-internal dll/static with new names ([@deblasis](https://github.com/deblasis))
  ```text
  Rename the internal library's install names to match the new
  ghostty-internal pkg-config module convention:
  
    ghostty.dll          -> ghostty-internal.dll
    ghostty-static.lib   -> ghostty-internal-static.lib
    libghostty.so        -> ghostty-internal.so
    libghostty.a         -> ghostty-internal.a
  
  This is the glue library between Ghostty's app shells and the GUI
  core, historically (mis)named "libghostty". It is not the public
  libghostty-vt API.
  ```
- [`1988ac9`](https://github.com/ghostty-org/ghostty/commit/1988ac94d4815b878e34258a543d17707024f209) build: point ghostty-internal pkg-config files at direct paths ([@deblasis](https://github.com/deblasis))
  ```text
  Switch the shared ghostty-internal.pc Libs: line from -lghostty to a
  direct ${libdir}/<file> path, matching what the -static module already
  does. The name-per-OS helpers now emit:
  
    shared:  ghostty-internal.dll (Windows) / ghostty-internal.so (other)
    static:  ghostty-internal-static.lib (Windows) / ghostty-internal.a
  
  Direct paths sidestep the GNU-ld -l<name> search template, which
  expects libghostty-internal.so/.a on Unix - we drop the lib prefix to
  match the ghostty-internal pkg-config module name.
  
  Also update the LipoStep out_name for the macOS universal static
  archive to ghostty-internal.a for consistency.
  ```
- [`935b08a`](https://github.com/ghostty-org/ghostty/commit/935b08acea92e4c9a6772d0518022e6659a9be68) test/windows: load ghostty-internal.dll in CRT init reproducer ([@deblasis](https://github.com/deblasis))
  ```text
  The internal glue DLL was renamed from ghostty.dll to
  ghostty-internal.dll. Update the LoadLibraryA call and the comment
  block so this regression test still exercises the right artifact.
  ```
- [`19bf63a`](https://github.com/ghostty-org/ghostty/commit/19bf63ab714ddd5807df5ec2df0572c7fd9ac94a) test/windows: update README for ghostty-internal.dll rename ([@deblasis](https://github.com/deblasis))
  ```text
  Match the dll filename rename so the copy/run instructions stay
  accurate.
  ```
- [`8bd1aba`](https://github.com/ghostty-org/ghostty/commit/8bd1aba40a75601a7c9c934d9b3551f3d9bb67da) macOS: add shared OSSurfaceView ([@bo2themax](https://github.com/bo2themax))
- [`46fef77`](https://github.com/ghostty-org/ghostty/commit/46fef7718cb5c53dc983aa301599887ec398c624) macOS: move `pwd` to `OSSurfaceView` ([@bo2themax](https://github.com/bo2themax))
- [`d38301b`](https://github.com/ghostty-org/ghostty/commit/d38301bb9ff4a3bf52dca046f0dc75d50a43d244) macOS: move `cellSize` to `OSSurfaceView` ([@bo2themax](https://github.com/bo2themax))
- [`3936069`](https://github.com/ghostty-org/ghostty/commit/3936069297ac2e7a2f4e2508bdbe6da735425f7d) macOS: move `healthy` and `error` to `OSSurfaceView` ([@bo2themax](https://github.com/bo2themax))
- [`619e12d`](https://github.com/ghostty-org/ghostty/commit/619e12dc75a2c3ec4f32929b9b59ddf2b2355180) macOS: move `hoverUrl` to `OSSurfaceView` ([@bo2themax](https://github.com/bo2themax))
- [`8b99c77`](https://github.com/ghostty-org/ghostty/commit/8b99c77bf76810ba9a0cd7a05a8215c81948f26e) macOS: update title comments ([@bo2themax](https://github.com/bo2themax))
- [`19af8e9`](https://github.com/ghostty-org/ghostty/commit/19af8e9ce2727477373a556d576792b943e1d78a) macOS: move `progressReport` to `OSSurfaceView` ([@bo2themax](https://github.com/bo2themax))
- [`56b505c`](https://github.com/ghostty-org/ghostty/commit/56b505cbb07485dc75e0907eec1c5432d03b515b) macOS: move `keyTables` to `OSSurfaceView` ([@bo2themax](https://github.com/bo2themax))
- [`7c83561`](https://github.com/ghostty-org/ghostty/commit/7c83561f9e3a3581bc94c1c4a47b8810f8591625) macOS: move `focusInstant` to `OSSurfaceView` ([@bo2themax](https://github.com/bo2themax))
- [`3834751`](https://github.com/ghostty-org/ghostty/commit/3834751aef32c9b18c7d584776813ae0c1c38cbb) macOS: move `surfaceSize` to `OSSurfaceView` ([@bo2themax](https://github.com/bo2themax))
- [`2efe851`](https://github.com/ghostty-org/ghostty/commit/2efe851cda266c38f3a2022db6738df72ce72140) macOS: move `readonly` to `OSSurfaceView` ([@bo2themax](https://github.com/bo2themax))
- [`1665755`](https://github.com/ghostty-org/ghostty/commit/1665755a93502485f8970c0a012359759bdb8bf9) macOS: move `highlighted` to `OSSurfaceView` ([@bo2themax](https://github.com/bo2themax))
- [`a541e23`](https://github.com/ghostty-org/ghostty/commit/a541e2312082a80e054d0482ef672efe4c97f06e) macOS: move `surface` to `OSSurfaceView` ([@bo2themax](https://github.com/bo2themax))
- [`90ea604`](https://github.com/ghostty-org/ghostty/commit/90ea604a7cf16145e3cb05beb8028ccf242e552a) macOS: move `searchState` to `OSSurfaceView` ([@bo2themax](https://github.com/bo2themax))
- [`bf6fd4a`](https://github.com/ghostty-org/ghostty/commit/bf6fd4abe583b7a0f2f339c7b9e762d4399e4991) macOS: add `focusDidChange` & `sizeDidChange` placeholders to `OSSurfaceView` ([@bo2themax](https://github.com/bo2themax))
- [`5301999`](https://github.com/ghostty-org/ghostty/commit/53019991f7291edb74abffe03ad85256933d733a) macOS: fix the arrow alignment of the secure input popover ([@bo2themax](https://github.com/bo2themax))
- [`0325964`](https://github.com/ghostty-org/ghostty/commit/032596442fb16983ed15e492dddc8267a163a1f1) macOS: clean up duplicated declarations in SurfaceView_AppKit/UIKit ([#12250](https://github.com/ghostty-org/ghostty/issues/12250)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Added a shared `OSSurfaceView` as the base class to share common
  variables and functions across platforms.
  
  Each commit contains a small change to move one or two variables or
  functions to `OSSurfaceView`.
  ```
- [`7f6d2a4`](https://github.com/ghostty-org/ghostty/commit/7f6d2a44b8f2d207f76cc4ecc8d60b6b48610fd7) macOS: fix cannot rebind super+up and super+down ([#12245](https://github.com/ghostty-org/ghostty/issues/12245)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fix: #11989
  Cause identified to: ab352b5af9694a7cba8e237d0b1b5a507a6e4226
  Original PR: #10003
  Problem: I don't think it is OK to hard code the keybind like this at
  all. Ghostty's config is flexible enough to achieve this.
  Proposal: Revert the above commit via this PR.
  
  @yasuf @bo2themax
  ```
- [`d2b79be`](https://github.com/ghostty-org/ghostty/commit/d2b79bea771a1633ffedf3ac7b9c73c194d4e83f) macOS: fix the arrow alignment of the secure input popover ([#12249](https://github.com/ghostty-org/ghostty/issues/12249)) ([@mitchellh](https://github.com/mitchellh))
- [`94cd3da`](https://github.com/ghostty-org/ghostty/commit/94cd3da8bc66af3968752e83b24858b90455b165) build: add ghostty-internal pkg-config modules (shared + static) ([#12214](https://github.com/ghostty-org/ghostty/issues/12214)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  ## Summary
  Mirror the `libghostty-vt-static` pkg-config pattern from #12210 for the
  internal library.
  
  - Add `ghostty-internal.pc` (shared, `-lghostty`) and
  `ghostty-internal-static.pc` (static, direct archive reference) so
  consumers can discover either variant via pkg-config
  - Named `ghostty-internal` to distinguish from the public
  `libghostty-vt` API
  - Static module points at the platform-correct archive name
  (`ghostty-static.lib` on Windows, `libghostty.a` elsewhere)
  - pkg-config files are generated during shared builds and installed via
  `GhosttyLib.install()`
  
  ## Test plan
  
  - [x] `zig build` succeeds (default target)
  - [x] `ghostty-internal.pc` and `ghostty-internal-static.pc` appear in
  `zig-out/share/pkgconfig/`
  - [x] Static `.pc` points at `ghostty-static.lib` (Windows) /
  `libghostty.a` (Unix)
  - [x] Shared `.pc` uses standard `-L -l` flags
  - [x] Existing `libghostty-vt` pkg-config files are unaffected
  ```

## April 11, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/24292563886), [2](https://github.com/ghostty-org/ghostty/actions/runs/24290621387)  
Summary: 2 runs • 8 commits • 2 authors

### Changes

- [`3e6a65f`](https://github.com/ghostty-org/ghostty/commit/3e6a65f73f5b1b0adb8a7af30d90d6238c1ac517) pkg/highway: drop libc++ from vendored hwy ([@mitchellh](https://github.com/mitchellh))
  ```text
  The vendored Highway package was being built with libc++ even though
  Ghostty only uses its runtime target selection and dispatch support.
  That pulled in extra C++ runtime baggage from upstream support files
  such as abort, timer, print, and benchmark helpers.
  
  Build Highway in HWY_NO_LIBCXX mode, only compile the target dispatch
  sources we actually need, and compile Ghostty's SIMD translation units
  with the same define so the header ABI stays consistent. Replace the
  upstream abort implementation with a small local bridge that provides
  Highway's Warn/Abort hooks and the target-query shim without depending
  on libc++.
  
  This keeps the Highway archive down to the dispatch pieces Ghostty
  uses while preserving the existing dynamic dispatch behavior. The
  bridge is documented so it is clear why Ghostty carries this small
  local replacement.
  ```
- [`fa2c3a1`](https://github.com/ghostty-org/ghostty/commit/fa2c3a1e60a9f8d40c0799d5d55e2fe4c8050f11) pkg/highway: drop libc++ dependency from vendored hwy ([#12238](https://github.com/ghostty-org/ghostty/issues/12238)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The vendored Highway package was being built with libc++ even though
  Ghostty only uses its runtime target selection and dispatch support.
  That pulled in extra C++ runtime baggage from upstream support files
  such as abort, timer, print, and benchmark helpers.
  
  Build Highway in HWY_NO_LIBCXX mode, only compile the target dispatch
  sources we actually need, and compile Ghostty's SIMD translation units
  with the same define so the header ABI stays consistent. Replace the
  upstream abort implementation with a small local bridge that provides
  Highway's Warn/Abort hooks and the target-query shim without depending
  on libc++.
  
  This keeps the Highway archive down to the dispatch pieces Ghostty uses
  while preserving the existing dynamic dispatch behavior. The bridge is
  documented so it is clear why Ghostty carries this small local
  replacement.
  
  We still depend on libc++ for other reasons, but I figure we should just
  trim it down as needed. 😄
  ```
- [`5e102c9`](https://github.com/ghostty-org/ghostty/commit/5e102c9dc78d3a9bf3c400b5bcb24252a8995da2) build: stop linking libc++ for utfcpp ([@mitchellh](https://github.com/mitchellh))
  ```text
  utfcpp is a header-only dependency, so its package wrapper does not
  need to link the C++ standard library. Keep the empty static archive
  for build integration, but stop adding an unnecessary libc++
  dependency.
  ```
- [`557de7c`](https://github.com/ghostty-org/ghostty/commit/557de7c92556ab0eb9725b5693d396a68b242dc3) build: stop linking libc++ for utfcpp ([#12239](https://github.com/ghostty-org/ghostty/issues/12239)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  utfcpp is a header-only dependency, so its package wrapper does not need
  to link the C++ standard library. Keep the empty static archive for
  build integration, but stop adding an unnecessary libc++ dependency.
  ```
- [`650cd96`](https://github.com/ghostty-org/ghostty/commit/650cd966461ed38bb2ab347203af71e78c7b336b) macOS: fix memory leak of TerminalController ([@bo2themax](https://github.com/bo2themax))
  ```text
  Regression of #12119, this memory leak affects new tabs, since the terminal controller is not deallocated correctly. Hitting `cmd+t` will create a new window with two tabs, but only one actually contains usable surface.
  
  You can reproduce by:
  1. Quit and Reopen Ghostty
  2. Open a new window if no window is created (initial-window = false)
  3. Close the window
  4. Hit `cmd+t`
  ```
- [`2c1dad7`](https://github.com/ghostty-org/ghostty/commit/2c1dad790b750b64adf0f2c4128604c2eba91dab) libghostty: add _get_multi to all _get APIs ([@mitchellh](https://github.com/mitchellh))
  ```text
  Replace the ImageInfo and PlacementInfo sized structs and their
  associated .info enum variants with a new _get_multi pattern that
  batches multiple enum+pointer pairs into a single call. This avoids
  struct ABI concerns (field order, padding, alignment, GHOSTTY_INIT_SIZED)
  while preserving the single-call-crossing performance benefit for FFI
  and Cgo callers.
  
  Each _get_multi function takes an array of enum keys, an array of
  output pointers, and an optional out_written parameter that reports
  how many values were successfully written before any error. This
  applies uniformly to all _get APIs: terminal_get, cell_get, row_get,
  render_state_get, render_state_row_get, render_state_row_cells_get,
  kitty_graphics_image_get, and kitty_graphics_placement_get.
  
  The C example is updated to use compound-literal _get_multi calls,
  and tests cover both success and error paths for every new function.
  ```
- [`abf1332`](https://github.com/ghostty-org/ghostty/commit/abf1332737813259f738e89dc3f76afcfec74e3a) macOS: fix memory leak of TerminalController ([#12237](https://github.com/ghostty-org/ghostty/issues/12237)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Regression of #12119, this memory leak affects new tabs, since the
  terminal controller is not deallocated correctly, hitting `cmd+t` will
  create a new window with two tabs, but only one actually contains usable
  surface.
  
  You can reproduce by:
  1. Quit and Reopen Ghostty
  2. Open a new window if no window is created (initial-window = false)
  3. Close the window
  4. Hit `cmd+t`
  ```
- [`c36b458`](https://github.com/ghostty-org/ghostty/commit/c36b458ad57a95869745e405c9d8d45104a97773) libghostty: add _get_multi to all _get APIs ([#12236](https://github.com/ghostty-org/ghostty/issues/12236)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Replace the ImageInfo and PlacementInfo sized structs and their
  associated .info enum variants with a new _get_multi pattern that
  batches multiple enum+pointer pairs into a single call. This avoids
  struct ABI concerns (field order, padding, alignment,
  GHOSTTY_INIT_SIZED) while preserving the single-call-crossing
  performance benefit for FFI and Cgo callers.
  
  Each _get_multi function takes an array of enum keys, an array of output
  pointers, and an optional out_written parameter that reports how many
  values were successfully written before any error. This applies
  uniformly to all _get APIs: terminal_get, cell_get, row_get,
  render_state_get, render_state_row_get, render_state_row_cells_get,
  kitty_graphics_image_get, and kitty_graphics_placement_get.
  
  The C example is updated to use compound-literal _get_multi calls, and
  tests cover both success and error paths for every new function.
  ```

## April 10, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/24265668827), [2](https://github.com/ghostty-org/ghostty/actions/runs/24259333144), [3](https://github.com/ghostty-org/ghostty/actions/runs/24257789901), [4](https://github.com/ghostty-org/ghostty/actions/runs/24248204427), [5](https://github.com/ghostty-org/ghostty/actions/runs/24245766423), [6](https://github.com/ghostty-org/ghostty/actions/runs/24230549966), [7](https://github.com/ghostty-org/ghostty/actions/runs/24225583592)  
Summary: 7 runs • 16 commits • 5 authors

### Changes

- [`3295bf4`](https://github.com/ghostty-org/ghostty/commit/3295bf40a725b3c67b9aed8d3f7851f8442ffb41) libghostty: add convenience accessors for kitty graphics ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add three sized structs that let callers fetch all image, placement,
  or rendering metadata in a single call instead of many individual
  queries. This is an optimization for environments with high per-call
  overhead such as FFI or Cgo.
  
  GhosttyKittyGraphicsImageInfo is returned via image_get() with the
  new GHOSTTY_KITTY_IMAGE_DATA_INFO data kind. It bundles id, number,
  width, height, format, compression, data pointer, and data length.
  
  GhosttyKittyGraphicsPlacementInfo is returned via placement_get()
  with the new GHOSTTY_KITTY_GRAPHICS_PLACEMENT_DATA_INFO data kind.
  It bundles image id, placement id, virtual flag, offsets, source
  rect, columns, rows, and z-index.
  
  GhosttyKittyGraphicsPlacementRenderInfo is returned by the new
  ghostty_kitty_graphics_placement_render_info() function, which
  combines pixel size, grid size, viewport position, and resolved
  source rectangle. This one requires image and terminal handles so
  it does not fit the existing _get() pattern and is a dedicated
  function.
  
  All three use the sized-struct ABI pattern with GHOSTTY_INIT_SIZED
  for forward compatibility.
  ```
- [`7421b4b`](https://github.com/ghostty-org/ghostty/commit/7421b4b13f87e101d4bbcedd4da84886ceae4e7b) libghostty: add convenience accessors for kitty graphics ([#12229](https://github.com/ghostty-org/ghostty/issues/12229)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add three sized structs that let callers fetch all image, placement, or
  rendering metadata in a single call instead of many individual queries.
  This is an optimization for environments with high per-call overhead
  such as FFI or Cgo.
  
  GhosttyKittyGraphicsImageInfo is returned via image_get() with the new
  GHOSTTY_KITTY_IMAGE_DATA_INFO data kind. It bundles id, number, width,
  height, format, compression, data pointer, and data length.
  
  GhosttyKittyGraphicsPlacementInfo is returned via placement_get() with
  the new GHOSTTY_KITTY_GRAPHICS_PLACEMENT_DATA_INFO data kind. It bundles
  image id, placement id, virtual flag, offsets, source rect, columns,
  rows, and z-index.
  
  GhosttyKittyGraphicsPlacementRenderInfo is returned by the new
  ghostty_kitty_graphics_placement_render_info() function, which combines
  pixel size, grid size, viewport position, and resolved source rectangle.
  This one requires image and terminal handles so it does not fit the
  existing _get() pattern and is a dedicated function.
  
  All three use the sized-struct ABI pattern with GHOSTTY_INIT_SIZED for
  forward compatibility.
  ```
- [`85be3ca`](https://github.com/ghostty-org/ghostty/commit/85be3ca2c17ca606753fa623ab0f4e3abb164287) build: skip ghostty-test graph when building libghostty-vt ([@kataokatsuki](https://github.com/kataokatsuki))
  ```text
  Fixes #12151
  ```
- [`d3ce892`](https://github.com/ghostty-org/ghostty/commit/d3ce8926b9deeccda6d7a6b228150d876e125c74) build: skip ghostty-test graph when building libghostty-vt ([#12224](https://github.com/ghostty-org/ghostty/issues/12224)) ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes #12151
  
  When `emit_lib_vt` is true, the `// Tests` block was still
  evaluated, pulling in the full ghostty-test dependency graph
  (freetype, zlib, dcimgui, etc.). This causes the Nix
  `libghostty-vt` package to fail when `doCheck` is enabled,
  since those system libraries aren't available in the sandbox.
  
  Guard the block with `if (!config.emit_lib_vt)`, following
  the existing pattern at line 179.
  ```
- [`f2e299f`](https://github.com/ghostty-org/ghostty/commit/f2e299fb46fee50a348a76165f18e5433fdb9945) cmake: add ghostty_vt_add_target() for cross-compilation ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a ghostty_vt_add_target() CMake function that lets downstream
  projects build libghostty-vt for a specific Zig target triple. The
  function encapsulates zig discovery, build-type-to-optimize mapping,
  the zig build invocation, and output path conventions so consumers
  do not need to duplicate any of that logic. It creates named IMPORTED
  targets (e.g. ghostty-vt-static-linux-amd64) that work alongside the
  existing native ghostty-vt and ghostty-vt-static targets.
  
  The build-type mapping is factored into a shared _GHOSTTY_ZIG_OPT_FLAG
  variable used by both the native build and the new function.
  
  The static library targets now propagate c++ as a link dependency on
  non-Windows platforms, fixing link failures when consumers use static
  linking with the default SIMD-enabled build.
  
  A new example/c-vt-cmake-cross/ demonstrates end-to-end cross-
  compilation using zig cc as the C compiler, auto-detecting a cross
  target based on the host OS.
  ```
- [`7127abf`](https://github.com/ghostty-org/ghostty/commit/7127abfe285014c62bc1f9b24d4e038af7f94afa) cmake: add ghostty_vt_add_target() for cross-compilation ([#12212](https://github.com/ghostty-org/ghostty/issues/12212)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a ghostty_vt_add_target() CMake function that lets downstream
  projects build libghostty-vt for a specific Zig target triple. The
  function encapsulates zig discovery, build-type-to-optimize mapping, the
  zig build invocation, and output path conventions so consumers do not
  need to duplicate any of that logic. It creates named IMPORTED targets
  (e.g. ghostty-vt-static-linux-amd64) that work alongside the existing
  native ghostty-vt and ghostty-vt-static targets.
  
  The build-type mapping is factored into a shared _GHOSTTY_ZIG_OPT_FLAG
  variable used by both the native build and the new function.
  
  A new example/c-vt-cmake-cross/ demonstrates end-to-end cross-
  compilation using zig cc as the C compiler, auto-detecting a cross
  target based on the host OS.
  ```
- [`aa6943d`](https://github.com/ghostty-org/ghostty/commit/aa6943da378a9b5b985d14449baa284a738e51f5) libghostty: add log callback configuration ([@mitchellh](https://github.com/mitchellh))
  ```text
  In C ABI builds, the Zig std.log default writes to stderr which is
  not appropriate for a library. Override std_options.logFn with a
  custom sink that dispatches to an embedder-provided callback, or
  silently discards when none is registered.
  
  Add GHOSTTY_SYS_OPT_LOG to ghostty_sys_set() following the existing
  decode_png pattern. The callback receives the log level as a
  GhosttySysLogLevel enum, scope and message as separate byte slices,
  giving embedders full control over formatting and routing.
  
  Export ghostty_sys_log_stderr as a built-in convenience callback that
  writes to stderr using std.debug.lockStderrWriter for thread-safe
  output. Embedders who want the old behavior can install it at startup
  with a single ghostty_sys_set call.
  ```
- [`c34901d`](https://github.com/ghostty-org/ghostty/commit/c34901dddbc36b63f33bbb1a47d62f6911584d65) libghostty: add log callback configuration ([#12227](https://github.com/ghostty-org/ghostty/issues/12227)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  In C ABI builds, the Zig std.log default writes to stderr which is not
  appropriate for a library. Override std_options.logFn with a custom sink
  that dispatches to an embedder-provided callback, or silently discards
  when none is registered.
  
  Add GHOSTTY_SYS_OPT_LOG to ghostty_sys_set() following the existing
  decode_png pattern. The callback receives the log level as a
  GhosttySysLogLevel enum, scope and message as separate byte slices,
  giving embedders full control over formatting and routing.
  
  Export ghostty_sys_log_stderr as a built-in convenience callback that
  writes to stderr using std.debug.lockStderrWriter for thread-safe
  output. Embedders who want the old behavior can install it at startup
  with a single ghostty_sys_set call.
  ```
- [`b5d54d8`](https://github.com/ghostty-org/ghostty/commit/b5d54d8f51727ac8af5ad793e87d0a6d03bc9fd6) Update VOUCHED list ([#12225](https://github.com/ghostty-org/ghostty/issues/12225)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12223#discussioncomment-16518906)
  from @jcollie.
  
  Vouch: @kataokatsuki
  ```
- [`e7f58ad`](https://github.com/ghostty-org/ghostty/commit/e7f58ad72e8fd32b59e60660cb8430fdc59d0ddd) macOS: double click title to enlarge window ([@bo2themax](https://github.com/bo2themax))
  ```text
  Previously with `macos-titlebar-style	= tabs`, double clicking title will do nothing
  ```
- [`41c872c`](https://github.com/ghostty-org/ghostty/commit/41c872c1f4116b344e20985f1c41f604acc0cdd6) macOS: fix tab title editor frame update during winding resizing ([@bo2themax](https://github.com/bo2themax))
- [`d51e94f`](https://github.com/ghostty-org/ghostty/commit/d51e94f7ebb71d095572af7dde30d34c81b6cae3) macOS: fix tab title editor frame update during winding resizing ([#12220](https://github.com/ghostty-org/ghostty/issues/12220)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  https://github.com/user-attachments/assets/69bee4f9-e3e1-4dc7-8e9c-c395572d2dbf
  ```
- [`19b0ed2`](https://github.com/ghostty-org/ghostty/commit/19b0ed2bdfed5f9913b89e69523e666bb020ed9e) macOS: double click title to enlarge window ([#12219](https://github.com/ghostty-org/ghostty/issues/12219)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Previously with `macos-titlebar-style = tabs`, double clicking title
  would do nothing
  ```
- [`1348e04`](https://github.com/ghostty-org/ghostty/commit/1348e046268402320253b1435b1559c754176c76) Update VOUCHED list ([#12216](https://github.com/ghostty-org/ghostty/issues/12216)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12213#discussioncomment-16512677)
  from @pluiedev.
  
  Vouch: @otomn
  ```
- [`a82e156`](https://github.com/ghostty-org/ghostty/commit/a82e1569252352bf3875f33a87f5935ddd6fd4a7) build: add libghostty-vt-static pkg-config module ([@mitchellh](https://github.com/mitchellh))
  ```text
  Keep libghostty-vt.pc as the shared/default pkg-config module so
  `pkg-config --static libghostty-vt` continues to emit the historical
  `-lghostty-vt` flags. This preserves the old behavior for consumers
  that still want it, even though that form remains ambiguous on macOS
  when both the dylib and archive are installed in the same directory.
  
  Add a separate libghostty-vt-static.pc module for consumers that need
  an unambiguous static link. Its `Libs:` entry points directly at the
  installed archive so macOS does not resolve the request to the dylib.
  
  Update the Nix packaging to rewrite the new static module into the `dev`
  output, use it in the static-link smoke test, and add a compatibility
  check that covers both pkg-config entry points.
  ```
- [`48a01b8`](https://github.com/ghostty-org/ghostty/commit/48a01b8bd51b0cf4ba3ed281a6662ae131ee8239) build: add libghostty-vt-static pkg-config module ([#12210](https://github.com/ghostty-org/ghostty/issues/12210)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Keep libghostty-vt.pc as the shared/default pkg-config module so
  `pkg-config --static libghostty-vt` continues to emit the historical
  `-lghostty-vt` flags. This preserves the old behavior for consumers that
  still want it, even though that form remains ambiguous on macOS when
  both the dylib and archive are installed in the same directory.
  
  Add a separate libghostty-vt-static.pc module for consumers that need an
  unambiguous static link. Its `Libs:` entry points directly at the
  installed archive so macOS does not resolve the request to the dylib.
  
  Update the Nix packaging to rewrite the new static module into the `dev`
  output, use it in the static-link smoke test, and add a compatibility
  check that covers both pkg-config entry points.
  ```

