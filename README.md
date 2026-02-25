> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: February 25, 2026 at 12:13 UTC.

## February 25, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22381369347), [2](https://github.com/ghostty-org/ghostty/actions/runs/22378200332)  
Summary: 2 runs • 2 commits • 1 authors

### Changes

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

## February 20, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22242592203), [2](https://github.com/ghostty-org/ghostty/actions/runs/22237663080), [3](https://github.com/ghostty-org/ghostty/actions/runs/22235836482), [4](https://github.com/ghostty-org/ghostty/actions/runs/22235046074), [5](https://github.com/ghostty-org/ghostty/actions/runs/22234176983), [6](https://github.com/ghostty-org/ghostty/actions/runs/22232199017), [7](https://github.com/ghostty-org/ghostty/actions/runs/22219871214), [8](https://github.com/ghostty-org/ghostty/actions/runs/22211628446), [9](https://github.com/ghostty-org/ghostty/actions/runs/22210903027), [10](https://github.com/ghostty-org/ghostty/actions/runs/22206371589)  
Summary: 10 runs • 59 commits • 13 authors

### Changes

- [`7e90e26`](https://github.com/ghostty-org/ghostty/commit/7e90e26ae1a422d3e4b62fac5eb2928be3cc74b4) macos: optimize secure input overlay animation ([@brentschroeter](https://github.com/brentschroeter))
  ```text
  Rendering the Secure Keyboard Input overlay using
  innerShadow() can strain the resources of the main
  thread, leading to elevated CPU load and in some
  cases extended disruptions to the main thread's
  DispatchQueue that result in lag or frozen frames.
  
  This change achieves the same animated visual
  effect with ~35% lower CPU usage and resolves most
  or all of the terminal rendering issues associated
  with the overlay.
  ```
- [`3d3ea3f`](https://github.com/ghostty-org/ghostty/commit/3d3ea3fa596a27075a1cef601217a0780edca20c) macos: swiftlint 'no_fallthrough_only' rule ([@jparise](https://github.com/jparise))
  ```text
  This rule is generally trying to be helpful, but it doesn't like a few
  places in our code base where we're intentionally listing out all of the
  well-known cases. Given that, just disable it.
  
  https://realm.github.io/SwiftLint/no_fallthrough_only.html
  ```
- [`2ed3414`](https://github.com/ghostty-org/ghostty/commit/2ed341495f2de5c9254b17511378d38c7960ac3f) macos: optimize secure input overlay animation ([#10903](https://github.com/ghostty-org/ghostty/issues/10903)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Addresses discussion in #3729 and issues relating to #7333, #9590, and
  #9617.
  
  Rendering the Secure Keyboard Input overlay using innerShadow() can
  strain the resources of the main thread, leading to elevated CPU load
  and in some cases extended disruptions to the main thread's
  DispatchQueue that result in lag or frozen frames. This change achieves
  the same animated visual effect with ~35% lower CPU usage and resolves
  most or all of the terminal rendering issues associated with the
  overlay.
  ```
- [`5db9f03`](https://github.com/ghostty-org/ghostty/commit/5db9f03f6282141f084a8a4c8c9cb3d752b0ae9e) macos: swiftlint 'no_fallthrough_only' rule ([#10899](https://github.com/ghostty-org/ghostty/issues/10899)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This rule is generally trying to be helpful, but it doesn't like a few
  places in our code base where we're intentionally listing out all of the
  well-known cases. Given that, just disable it.
  
  https://realm.github.io/SwiftLint/no_fallthrough_only.html
  ```
- [`8699a67`](https://github.com/ghostty-org/ghostty/commit/8699a67ecf94e65f7b9037df22353e475546b661) ci: Add a `skips` job where we can accumulate skip conditions ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds a new job that we can use to set outputs to accumulate skip
  conditions for other tests. The major change here is skipping all tests
  if we're only updating vouches, to save our CI.
  
  I also included a number of minor skips based on filepaths.
  ```
- [`db1e31c`](https://github.com/ghostty-org/ghostty/commit/db1e31c7a69924913e8faafcedb290de3cb4a8b6) ci: Add a `skips` job where we can accumulate skip conditions ([#10901](https://github.com/ghostty-org/ghostty/issues/10901)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This adds a new job that we can use to set outputs to accumulate skip
  conditions for other tests. The major change here is skipping all tests
  if we're only updating vouches, to save our CI.
  
  I also included a number of minor skips based on filepaths.
  ```
- [`89e06a8`](https://github.com/ghostty-org/ghostty/commit/89e06a8402288d3d40568db2da6540ae3fbf82a1) Update VOUCHED list ([#10898](https://github.com/ghostty-org/ghostty/issues/10898)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/10863#issuecomment-3936322278)
  from @mitchellh.
  
  Vouch: @AlexFeijoo44
  ```
- [`727446f`](https://github.com/ghostty-org/ghostty/commit/727446fa8bdb7322b954022476c046a4f094b427) gtk: for a new window's first tab, inherit the parent's initial size hints ([@EriksRemess](https://github.com/EriksRemess))
- [`8e862e6`](https://github.com/ghostty-org/ghostty/commit/8e862e611b3ac8b390b6879a9c265edce64a26de) GTK: Pass parent's computed default/min sizes to the new window ([#10805](https://github.com/ghostty-org/ghostty/issues/10805)) ([@jcollie](https://github.com/jcollie))
  ```text
  Fixes for #10532
  ```
- [`d2098d8`](https://github.com/ghostty-org/ghostty/commit/d2098d830c804c528d772f9f3352ec334f547f17) deps: Update uucode to 0.2.0 (with unicode 17) ([@jacobsandlund](https://github.com/jacobsandlund))
- [`e887527`](https://github.com/ghostty-org/ghostty/commit/e887527e59a67f869b1fef1f6bcd61302b24e01c) macos: swiftlint 'unused_enumerated' rule ([@jparise](https://github.com/jparise))
- [`c2eab3b`](https://github.com/ghostty-org/ghostty/commit/c2eab3b43d142cc54d02aee3af9e9f80a51090dd) macos: add root-level .swiftlint.yml ([@jparise](https://github.com/jparise))
  ```text
  In order to support running from both the repository root and from
  within Xcode project, and to keep things generally organized, our
  primary .swiftlint.yml configuration file lives under macos/.
  
  This change introduces a root-level .swiftlint.yml which limits the file
  scope to macos/ and then includes macos/.swiftlint.yml for the rest of
  the directives.
  
  This unlocks a few benefits:
  
  - We no longer need to pass an explicit `macos` path argument in any of
    our invocations. SwiftLint will do the right thing when run either
    from the repository root or from within the macos/ directory.
  - It lets us easily exclude the macos/build/ directory (and re-enable
    the 'deployment_target' rule). In the previous setup, this was more
    challenging than you'd expect due to SwiftLint's path resolution rules
    and required passing even more arguments like `--working-directory`.
  
  The only downside is adding a new file to the repository root, but that
  feels like the right trade-off given the benefits and conveniences.
  ```
- [`454d53e`](https://github.com/ghostty-org/ghostty/commit/454d53e26441b0d3603745a6e7bfef631bad1d54) macos: ignore swiftlint 'line_length' rule ([@jparise](https://github.com/jparise))
  ```text
  Also, there are no more outstanding 'mark' issues.
  ```
- [`add991b`](https://github.com/ghostty-org/ghostty/commit/add991b66abd46225309816685110d067c8d1eea) Merge remote-tracking branch 'upstream/main' into uucode-unicode-17 ([@jacobsandlund](https://github.com/jacobsandlund))
- [`e06ac6d`](https://github.com/ghostty-org/ghostty/commit/e06ac6d33e6adb7dbd98d782723ec58e8e4eeff0) Force prepend to use wcwidth_standalone ([@jacobsandlund](https://github.com/jacobsandlund))
- [`0ac8104`](https://github.com/ghostty-org/ghostty/commit/0ac810461a2af268d6700e55bf3c9991e7cbe221) deps: Update uucode to v0.2.0 (with unicode 17) ([#10895](https://github.com/ghostty-org/ghostty/issues/10895)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This PR updates `uucode` to v0.2.0, with several new Unicode files being
  parsed, various fixes (not affecting Ghostty), `wcwidth` grapheme
  support, code point iteration, and finally an upgrade to Unicode 17. As
  far as this impacting Ghostty, the Unicode 17 upgrade is the biggest
  change, and even that is relatively minor.
  
  
  https://github.com/jacobsandlund/uucode/compare/31655fba3c638229989cc524363ef5e3c7b580c1...v0.2.0
  
  The only needed change to the configuration is to revert `prepend`
  characters to being non-zero width for Ghostty. See the comment.
  
  No AI was used except to check the grammar of the comment. AI was used a
  bit in the `uucode` changes, but mostly done by hand and closely
  reviewed when used.
  ```
- [`d4e5ba8`](https://github.com/ghostty-org/ghostty/commit/d4e5ba8c166d40719544678858629b1d65e7f5f9) macos: ignore swiftlint 'line_length' rule ([#10893](https://github.com/ghostty-org/ghostty/issues/10893)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Also, there are no more outstanding 'mark' issues.
  ```
- [`6ca8009`](https://github.com/ghostty-org/ghostty/commit/6ca80091c5126e7539254b0215e17728adbc8a56) macos: add root-level .swiftlint.yml ([#10890](https://github.com/ghostty-org/ghostty/issues/10890)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  In order to support running from both the repository root and from
  within Xcode project, and to keep things generally organized, our
  primary .swiftlint.yml configuration file lives under macos/.
  
  This change introduces a root-level .swiftlint.yml which limits the file
  scope to macos/ and then includes macos/.swiftlint.yml for the rest of
  the directives.
  
  This unlocks a few benefits:
  
  - We no longer need to pass an explicit `macos` path argument in any of
  our invocations. SwiftLint will do the right thing when run either from
  the repository root or from within the macos/ directory.
  - It lets us easily exclude the macos/build/ directory (and re-enable
  the 'deployment_target' rule). In the previous setup, this was more
  challenging than you'd expect due to SwiftLint's path resolution rules
  and required passing even more arguments like `--working-directory`.
  
  The only downside is adding a new file to the repository root, but that
  feels like the right trade-off given the benefits and conveniences.
  ```
- [`3ba6d81`](https://github.com/ghostty-org/ghostty/commit/3ba6d8174dd93e85ad53a39664346edaf84c2ad2) macos: swiftlint 'unused_enumerated' rule ([#10888](https://github.com/ghostty-org/ghostty/issues/10888)) ([@mitchellh](https://github.com/mitchellh))
- [`125e96f`](https://github.com/ghostty-org/ghostty/commit/125e96ff9ea0db8d4f59711c3e50fe2e63f1647b) Update VOUCHED list ([#10896](https://github.com/ghostty-org/ghostty/issues/10896)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/10895#issuecomment-3936131923)
  from @trag1c.
  
  Vouch: @jacobsandlund
  ```
- [`b0f00a6`](https://github.com/ghostty-org/ghostty/commit/b0f00a65edcd029a0670a669506de778edc39cfd) Add ghostty_config_get tests ([@nicosuave](https://github.com/nicosuave))
  ```text
  I mostly did this to familiarize myself with the codebase and figured it
  doesn't hurt to cover this with tests if I add more in this area,
  despite receiving indirect coverage elsewhere.
  ```
- [`b6c1a26`](https://github.com/ghostty-org/ghostty/commit/b6c1a264378ea8616d9e71d941731ded400ca83e) Update VOUCHED list ([#10887](https://github.com/ghostty-org/ghostty/issues/10887)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/10882) from
  @jcollie.
  
  Vouch: @brentschroeter
  ```
- [`5008d7e`](https://github.com/ghostty-org/ghostty/commit/5008d7eb9323e642510426bef9887e7d32dff402) Add ghostty_config_get tests ([#10891](https://github.com/ghostty-org/ghostty/issues/10891)) ([@jcollie](https://github.com/jcollie))
  ```text
  I mostly did this to familiarize myself with the codebase and figured it
  doesn't hurt to cover this with tests if more added logic in this area,
  despite this logic receiving indirect coverage elsewhere. [Here's my
  related
  proposal](https://github.com/ghostty-org/ghostty/discussions/10807).
  
  I gave more thought around how to expose some of these config values and
  their metadata in the C api to eventually drive a settings UI and was
  hoping for feedback before I proceed.
  
  The cleanest path forward feels like annotating config values with
  formal metadata around things like: supported platforms, whether or not
  a restart is required, presentation metadata like grouping + ordering,
  tolerated ranges for values, possible enum values, etc. My intent is
  that Swift & other consumers can enumerate potential settings values
  with metadata such as to drive the UI from the metadata.
  
  ---
  
  AI Disclosure: I used Codex 5.3 to help me understand how the config
  subsystem in zig is exposed to Swift via the C API. Codex wrote these
  tests; but we brainstormed on a pragmatic coverage balance and I
  understand how the tests work.
  ```
- [`585bf3f`](https://github.com/ghostty-org/ghostty/commit/585bf3fcd25be3d1d70383a0f1b55e0f6744d639) Update es_AR translations with additional strings for 1.3 ([#10861](https://github.com/ghostty-org/ghostty/issues/10861)) ([@alanmoyano](https://github.com/alanmoyano))
  ```text
  - Adds the three new string
  - Changes one string for better wording
  ```
- [`c4c87f8`](https://github.com/ghostty-org/ghostty/commit/c4c87f8c85fb7339c093538196847fc3d0eed3c8) make palette inversion opt-in ([@jake-stewart](https://github.com/jake-stewart))
- [`f66a84b`](https://github.com/ghostty-org/ghostty/commit/f66a84b18a44838831af5819cdad1ba85d9592e4) improve light theme detection ([@jake-stewart](https://github.com/jake-stewart))
- [`acf8cc7`](https://github.com/ghostty-org/ghostty/commit/acf8cc74195f8f778e933a3e8c218891d79a36e4) i18n: Update and slightly clean up Russian translation ([#10633](https://github.com/ghostty-org/ghostty/issues/10633)) ([@TicClick](https://github.com/TicClick))
  ```text
  as per #10632
  ```
- [`0eaf77d`](https://github.com/ghostty-org/ghostty/commit/0eaf77da5fe0cbfe24ac5e0585a04d80d51fb952) WIP: Make palette inversion opt-in ([#10877](https://github.com/ghostty-org/ghostty/issues/10877)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  From #10554
  
  > I can see there being space for some kind of new sequence that tells
  the terminal that "hey, I want a semantic palette" or something, that is
  better adjusted to themes automatically. But, I don't think we should
  this by default.
  
  > So my concrete proposal is to eliminate the inversion and bg => fg
  ramp and do a more typical dark => light ramp (still taking into account
  bg/fg, but keeping 16 black and 231 white). I think this is the only way
  we can really make this a default on feature. I think this would address
  all the negative reactions we've gotten to it.
  
  This adds a new `palette-harmonious`, disabled by default, which allows
  generated light themes to be inverted.
  ```
- [`2863849`](https://github.com/ghostty-org/ghostty/commit/2863849fcae7ef46342e14af30fc3d850cd2109a) ci: milestone workflow should use our vouch app token ([@mitchellh](https://github.com/mitchellh))
  ```text
  This increases our rate limits and the vouch app already has the
  permissions required for the milestone workflow.
  ```
- [`c316472`](https://github.com/ghostty-org/ghostty/commit/c316472362dc9d6ced051b2d07c4ea5ee542822e) ci: milestone workflow should use our vouch app token ([#10879](https://github.com/ghostty-org/ghostty/issues/10879)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This increases our rate limits and the vouch app already has the
  permissions required for the milestone workflow.
  
  cc @trag1c
  ```
- [`df47dc1`](https://github.com/ghostty-org/ghostty/commit/df47dc1a98b9df29152ee1b24daea5f50883c99a) ci: milestone workflow should use our vouch app token ([@mitchellh](https://github.com/mitchellh))
  ```text
  This increases our rate limits and the vouch app already has the
  permissions required for the milestone workflow.
  ```
- [`a6b6033`](https://github.com/ghostty-org/ghostty/commit/a6b603385236bad5a592eb078d3e72a39c8215c1) ci: pass milestone token via github-token parameter ([@mitchellh](https://github.com/mitchellh))
  ```text
  If I am reading the upstream action right, even if you set GITHUB_TOKEN
  env var its defaulting to `github.token`, so we need to specify as a
  param.
  ```
- [`1fa4e78`](https://github.com/ghostty-org/ghostty/commit/1fa4e787eb1f50729153d09b7f455ebb9fc4ccc9) ci: pass milestone token via github-token parameter ([#10881](https://github.com/ghostty-org/ghostty/issues/10881)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  If I am reading the upstream action right, even if you set GITHUB_TOKEN
  env var its defaulting to `github.token`, so we need to specify as a
  param.
  ```
- [`786bad9`](https://github.com/ghostty-org/ghostty/commit/786bad9774cfa4753a11f8bb46b47aedc974bf3e) macos: swiftlint 'colon' rule ([@jparise](https://github.com/jparise))
- [`6ade5df`](https://github.com/ghostty-org/ghostty/commit/6ade5df7990d8f2fbd7dce5c05f43ba43bd510e5) macos: swiftlint 'comma' rule ([@jparise](https://github.com/jparise))
- [`a8903c1`](https://github.com/ghostty-org/ghostty/commit/a8903c1bb199aa52b63d20593361672f27a4d4ba) macos: swiftlint 'comment_spacing' rule ([@jparise](https://github.com/jparise))
- [`56d67ce`](https://github.com/ghostty-org/ghostty/commit/56d67ce88f05f9cf499ae483f34212722475ebf4) macos: swiftlint 'control_statement' rule ([@jparise](https://github.com/jparise))
- [`1b827e3`](https://github.com/ghostty-org/ghostty/commit/1b827e3e45f93b30767bfc4aa5e2131594dc60d0) macos: swiftlint 'empty_enum_arguments' rule ([@jparise](https://github.com/jparise))
- [`a83c8f8`](https://github.com/ghostty-org/ghostty/commit/a83c8f8a9d2b82956a02c24f82f5ab0ddaf9998c) macos: swiftlint 'empty_parentheses_with_trailing_closure' rule ([@jparise](https://github.com/jparise))
- [`9287a61`](https://github.com/ghostty-org/ghostty/commit/9287a61920da4262cd6c544dbd51c3e918d50174) macos: swiftlint 'implicit_optional_initialization' rule ([@jparise](https://github.com/jparise))
- [`32e540c`](https://github.com/ghostty-org/ghostty/commit/32e540c248815bed6a09bcf76ea1df536e25bf4f) macos: swiftlint 'legacy_constant' rule ([@jparise](https://github.com/jparise))
- [`b10dcc9`](https://github.com/ghostty-org/ghostty/commit/b10dcc96299aea9e4c276896a7331a3a2ded837f) macos: swiftlint 'legacy_constructor' rule ([@jparise](https://github.com/jparise))
- [`6052f66`](https://github.com/ghostty-org/ghostty/commit/6052f664cf83921114d05c6db19bb3ff1fb23063) macos: swiftlint 'opening_brace' rule ([@jparise](https://github.com/jparise))
- [`25b38b2`](https://github.com/ghostty-org/ghostty/commit/25b38b291e8128df96258b342fff914f71f80cac) macos: swiftlint 'private_over_fileprivate' rule ([@jparise](https://github.com/jparise))
- [`6af9599`](https://github.com/ghostty-org/ghostty/commit/6af959920e9815750998ea8e3dcb11a1264fee86) macos: swiftlint 'syntactic_sugar' rule ([@jparise](https://github.com/jparise))
- [`33dce85`](https://github.com/ghostty-org/ghostty/commit/33dce8511efa5432059e7593e20f0c53d7da080d) macos: swiftlint 'trailing_semicolon' rule ([@jparise](https://github.com/jparise))
- [`b532cd5`](https://github.com/ghostty-org/ghostty/commit/b532cd55d626fd1e472c288ce42151f8e6945634) macos: swiftlint 'trailing_whitespace' rule ([@jparise](https://github.com/jparise))
- [`540adb0`](https://github.com/ghostty-org/ghostty/commit/540adb0da3494cfdae9264782e9e38281ca0997f) macos: swiftlint 'unneeded_synthesized_initializer' rule ([@jparise](https://github.com/jparise))
- [`a36d2f5`](https://github.com/ghostty-org/ghostty/commit/a36d2f5420dee5b0ac1d0c55e83e1ea6dea3b879) macos: swiftlint 'unused_closure_parameter' rule ([@jparise](https://github.com/jparise))
- [`629a656`](https://github.com/ghostty-org/ghostty/commit/629a656e5329b35c970fdba3ee10fc5b366d2ba0) macos: swiftlint 'vertical_whitespace' rule ([@jparise](https://github.com/jparise))
- [`f4d70df`](https://github.com/ghostty-org/ghostty/commit/f4d70df34c8d564a7824144433d9bf30dfcef3e0) macos: swiftlint 'implicit_getter' rule ([@jparise](https://github.com/jparise))
- [`9bae26a`](https://github.com/ghostty-org/ghostty/commit/9bae26ab455110a7b28872c65dc82efb9d352027) macos: swiftlint 'orphaned_doc_comment' rule ([@jparise](https://github.com/jparise))
- [`a7719a8`](https://github.com/ghostty-org/ghostty/commit/a7719a8db6bae10c57bad6a73b94def4826fff5b) macos: swiftlint 'shorthand_operator' rule ([@jparise](https://github.com/jparise))
- [`c418e4b`](https://github.com/ghostty-org/ghostty/commit/c418e4b581d61969d3f02c2adae4e2e862f07b58) macos: swiftlint 'unused_optional_binding' rule ([@jparise](https://github.com/jparise))
- [`dbf2e0e`](https://github.com/ghostty-org/ghostty/commit/dbf2e0e087ced90a8f844fc028d73d9b2e40e668) macos: swiftlint 'vertical_parameter_alignment' rule ([@jparise](https://github.com/jparise))
- [`a6fcb46`](https://github.com/ghostty-org/ghostty/commit/a6fcb46e18b14a9199446dd0f053ebe08ef33bc9) macos: autofixable swiftlint rules ([#10878](https://github.com/ghostty-org/ghostty/issues/10878)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Apply fixes for all of the SwiftLint rules that can be automatically
  fixed (`--fix`) or addressed via some minor reformatting.
  
  Each rule is in its own commit for easier review.
  ```
- [`ca700b2`](https://github.com/ghostty-org/ghostty/commit/ca700b2d7b8d9e9e9ed46df2e1bb49a13b2fe606) additional strings for 3.0 ([@phush0](https://github.com/phush0))
- [`d1cb225`](https://github.com/ghostty-org/ghostty/commit/d1cb225895f6f3b195a5477d41d89b69216d5fc6) Fix translation for 'Open in Ghostty' ([@phush0](https://github.com/phush0))
- [`42c81db`](https://github.com/ghostty-org/ghostty/commit/42c81dbccc7c62ccc1eaef7fd724af9e308814ef) bg_BG additional strings for 1.3 ([#10836](https://github.com/ghostty-org/ghostty/issues/10836)) ([@trag1c](https://github.com/trag1c))

## February 19, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/22203301071), [2](https://github.com/ghostty-org/ghostty/actions/runs/22203050588), [3](https://github.com/ghostty-org/ghostty/actions/runs/22201254557), [4](https://github.com/ghostty-org/ghostty/actions/runs/22191269216), [5](https://github.com/ghostty-org/ghostty/actions/runs/22187435492), [6](https://github.com/ghostty-org/ghostty/actions/runs/22173999761), [7](https://github.com/ghostty-org/ghostty/actions/runs/22170147524), [8](https://github.com/ghostty-org/ghostty/actions/runs/22163738596), [9](https://github.com/ghostty-org/ghostty/actions/runs/22162963278)  
Summary: 9 runs • 31 commits • 11 authors

### Changes

- [`3d0da44`](https://github.com/ghostty-org/ghostty/commit/3d0da44e15cc8f4506acd17ad599229bc493f1c6) feat(config): allow fullscreen config to specify non-native mode directly ([@benodiwal](https://github.com/benodiwal))
- [`0ad8db8`](https://github.com/ghostty-org/ghostty/commit/0ad8db85824a240fade7e3626da5455eb1f821d5) Merge branch 'main' into feat/fullscreen-non-native-config ([@benodiwal](https://github.com/benodiwal))
- [`4289c1d`](https://github.com/ghostty-org/ghostty/commit/4289c1d63796afaf0c7ee665d12fe73564147ef9) feat(config): allow fullscreen config to specify non-native mode directly ([#9876](https://github.com/ghostty-org/ghostty/issues/9876)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Closes #8388
  ```
- [`81f537e`](https://github.com/ghostty-org/ghostty/commit/81f537e9927c94c84c5356424d6baabfabaee1b6) feat: implement scroll-to-bottom on output option ([@benodiwal](https://github.com/benodiwal))
  ```text
  Implements the `output` option for the `scroll-to-bottom` configuration,
  which scrolls the viewport to the bottom when new lines are printed.
  ```
- [`e197b95`](https://github.com/ghostty-org/ghostty/commit/e197b95c32f12abe97fbc1b0ca1f0514367ef702) feat: scroll-to-bottom on output via renderer pin tracking ([@benodiwal](https://github.com/benodiwal))
- [`2634697`](https://github.com/ghostty-org/ghostty/commit/263469755c56fa79474be2a56f2c85478cb1e25e) refactor: remove unused stream handler scroll-to-bottom code ([@benodiwal](https://github.com/benodiwal))
  ```text
  The renderer approach doesn't need termio changes.
  ```
- [`eb335fb`](https://github.com/ghostty-org/ghostty/commit/eb335fb8ddc8cc088c2c96924aaec979e1fea39f) cleanup by just scrolling in the renderer ([@mitchellh](https://github.com/mitchellh))
- [`2a62f21`](https://github.com/ghostty-org/ghostty/commit/2a62f21bf079f253245e0b9f752dbcdbb49eb95a) fix tests ([@mitchellh](https://github.com/mitchellh))
- [`410ee0d`](https://github.com/ghostty-org/ghostty/commit/410ee0d5c707f33437389c77252e2186468dc8dd) feat: implement scroll-to-bottom on output option ([#9938](https://github.com/ghostty-org/ghostty/issues/9938)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Closes #8408
  ```
- [`70cc121`](https://github.com/ghostty-org/ghostty/commit/70cc121736c55415c4f97f75294f6f29b1b65698) Update VOUCHED list ([#10873](https://github.com/ghostty-org/ghostty/issues/10873)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/10789) from
  @mitchellh.
  
  Vouch: @MiUPa
  ```
- [`faead2d`](https://github.com/ghostty-org/ghostty/commit/faead2d559b3cc90760bd17fdf902c69b2f40814) Update VOUCHED list ([#10874](https://github.com/ghostty-org/ghostty/issues/10874)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/10807) from
  @mitchellh.
  
  Vouch: @nicosuave
  ```
- [`cc17e96`](https://github.com/ghostty-org/ghostty/commit/cc17e968955b57d770f7bf01891b520c35ed41ce) Update VOUCHED list ([#10875](https://github.com/ghostty-org/ghostty/issues/10875)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/9876#issuecomment-3930522015)
  from @mitchellh.
  
  Vouch: @benodiwal
  ```
- [`21ea946`](https://github.com/ghostty-org/ghostty/commit/21ea94610abedabb37bbcbbd82429e5d2a274847) macos: lint Swift files using SwiftLint ([@jparise](https://github.com/jparise))
  ```text
  SwiftLint <https://realm.github.io/SwiftLint/> is both a linter and
  formatting. It's a popular way to spot issues and enforce a consistent
  style.
  
  Our SwiftLint configuration lives in macos/.swiftlint.yml, where is is
  automatically discovered. It's very configurable, and I made an initial
  pass as some basic, weakly-opinionated rules. The "TODO" section lists
  rules that currently have violations but can be easily (auto)fixed in
  follow-up commits.
  
  Our integration is CLI-based. Similar to our other support tools, we
  expect developers to install `swiftlint` via nix or e.g. Homebrew.
  This is documented in HACKING.md.
  
  We also have an optional Xcode integration, for in-editor feedback. When
  `swiftlint` is available, it's run as a script-based Build Phase.
  
  SwiftLint supports an auto-fix mode (--fix). Agents are aware of this
  via AGENTS.md.
  
  The rules are enforced using a (nix-based) CI job.
  ```
- [`a5dd7a7`](https://github.com/ghostty-org/ghostty/commit/a5dd7a750b2986da303f60fa4a4e4d24516b884d) ci: only run 'swiftlint' when macos/ changes ([@jparise](https://github.com/jparise))
  ```text
  This saves us some work on the majority of our commits. I think we'd
  only miss commits to .github/ and the nix environment with this filter,
  but we can expand the filter's scope as needed.
  ```
- [`c5488af`](https://github.com/ghostty-org/ghostty/commit/c5488afc75a9f9bd2e4c6b718e7828925b276f4a) url: improve space in path handling ([@bkircher](https://github.com/bkircher))
  ```text
  The space-segment patterns in the path regex (dotted_path_space_segments
  and any_path_space_segments) greedily consume text after a space even
  when we know that the text is the start of a new independent path (e.g.,
  `/tmp/bar` in `/tmp/foo /tmp/bar`).
  
  Fix: Add two negative lookaheads after the space in both patterns:
  - `(?!\.{0,2}\/)` →  don't match if the next segment starts with `/`,
    `./`, or `../`
  - `(?!~\/)` →  don't match if the next segment starts with `~/`
  ```
- [`f66064b`](https://github.com/ghostty-org/ghostty/commit/f66064b0b09e99d8877f9201f8c90f9b2edbbf25) url: fix regression with unified diff lines ([@bkircher](https://github.com/bkircher))
  ```text
  Bare relative paths don't need space-continuation semantics.
  
  Fixes #10773
  ```
- [`7928883`](https://github.com/ghostty-org/ghostty/commit/7928883f73dfc432ce3723305774f594ca75a80e) ci: add sync-codeowners action so that codeowners auto-vouch ([@mitchellh](https://github.com/mitchellh))
- [`57a16f7`](https://github.com/ghostty-org/ghostty/commit/57a16f7f60eb359de9208cc68ab64e124f984587) ci: add sync-codeowners action so that codeowners auto-vouch ([#10869](https://github.com/ghostty-org/ghostty/issues/10869)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This isn't attached to a tag yet because I have to test it.
  ```
- [`df7cd0f`](https://github.com/ghostty-org/ghostty/commit/df7cd0fb37714f8bd13310635c39c829ff983079) Sync CODEOWNERS vouch list ([#10872](https://github.com/ghostty-org/ghostty/issues/10872)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Sync CODEOWNERS owners with vouch list.
  
  ## Added Users
  
  - @00-kat
  - @abudvytis
  - @aindriu80
  - @andrejdaskalov
  - @balazs-szucs
  - @Beryesa
  - @bo2themax
  - @charliie-dev
  - @CraziestOwl
  - @d-Dudas
  - @damyanbogoev
  - @danulqua
  - @flou
  - @francescarpi
  - @gagbo
  - @ghokun
  - @gmile
  - @gordonbondon
  - @gpanders
  - @guilhermetk
  - @halosatrio
  - @johnslavik
  - @jparise
  - @kenvandine
  - @Kirwiisp
  - @kjvdven
  - @kloneets
  - @kristina8888
  - @liby
  - @lonsagisawa
  - @marijagjorgjieva
  - @MatkoTiric
  - @Misairuzame
  - @mtak
  - @OshDubh
  - @piedrahitac
  - @reo101
  - @RMEngelbrecht
  - @rockorager
  - @rpfaeffle
  - @silveirapf
  - @tdslot
  - @TicClick
  - @tnagatomi
  - @trag1c
  - @tristan957
  - @uhojin
  - @zenyr
  - @zeshi09
  ```
- [`35e2645`](https://github.com/ghostty-org/ghostty/commit/35e2645ab30f8525749b9bb6a15749bdc4cea90c) clickable file path fixes ([#10867](https://github.com/ghostty-org/ghostty/issues/10867)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  - **url: improve space in path handling**
  The space-segment patterns in the path regex (dotted_path_space_segments
    and any_path_space_segments) greedily consume text after a space even
  when we know that the text is the start of a new independent path (e.g.,
    `/tmp/bar` in `/tmp/foo /tmp/bar`).
  
    Fix: Add two negative lookaheads after the space in both patterns:
    - `(?!\.{0,2}\/)` →  don't match if the next segment starts with `/`,
      `./`, or `../`
    - `(?!~\/)` →  don't match if the next segment starts with `~/`
  
  
  - **url: fix regression with unified diff lines**
    Bare relative paths don't need space-continuation semantics.
  
    Fixes #10773
  ```
- [`f2a5f36`](https://github.com/ghostty-org/ghostty/commit/f2a5f36f26559d882078972052ebd63dafa54f96) macos: lint Swift files using SwiftLint ([#10860](https://github.com/ghostty-org/ghostty/issues/10860)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  SwiftLint <https://realm.github.io/SwiftLint/> is both a linter and
  formatting. It's a popular way to spot issues and enforce a consistent
  style.
  
  Our SwiftLint configuration lives in `macos/.swiftlint.yml`, where is is
  automatically discovered. It's very configurable, and I made an initial
  pass as some basic, weakly-opinionated rules. The "TODO" section lists
  rules that currently have violations but can be easily (auto)fixed in
  follow-up commits.
  
  Our integration is CLI-based. Similar to our other support tools, we
  expect developers to install `swiftlint` via nix or e.g. Homebrew. This
  is documented in HACKING.md.
  
  We also have an optional Xcode integration, for in-editor feedback. When
  `swiftlint` is available, it's run as a script-based Build Phase.
  
  SwiftLint supports an auto-fix mode (`--fix`). Agents are aware of this
  via AGENTS.md.
  
  The rules are enforced using a (nix-based) CI job.
  ```
- [`2ac3c1f`](https://github.com/ghostty-org/ghostty/commit/2ac3c1f1da69a7b3474fb1adcc8c2280001cf23d) Update VOUCHED list ([#10862](https://github.com/ghostty-org/ghostty/issues/10862)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/10861#issuecomment-3928416623)
  from @trag1c.
  ```
- [`16b320c`](https://github.com/ghostty-org/ghostty/commit/16b320ca8aafc81bd977a2c74d2cffa46340e637) build(deps): bump namespacelabs/nscloud-cache-action from 1.4.1 to 1.4.2 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [namespacelabs/nscloud-cache-action](https://github.com/namespacelabs/nscloud-cache-action) from 1.4.1 to 1.4.2.
  - [Release notes](https://github.com/namespacelabs/nscloud-cache-action/releases)
  - [Commits](https://github.com/namespacelabs/nscloud-cache-action/compare/4d61c33d0b4333a518e975a0c4de7633d28713bb...a90bb5d4b27522ce881c6e98eebd7d7e6d1653f9)
  
  ---
  updated-dependencies:
  - dependency-name: namespacelabs/nscloud-cache-action
    dependency-version: 1.4.2
    dependency-type: direct:production
    update-type: version-update:semver-patch
  ...
  ```
- [`9f2d66c`](https://github.com/ghostty-org/ghostty/commit/9f2d66c9c9a90d15b6d7ad01af5eef25d4cfd539) toggle command palette works on gtk ([@jcollie](https://github.com/jcollie))
- [`74c1555`](https://github.com/ghostty-org/ghostty/commit/74c15555917179943b51cb447fcb043b1327e897) build(deps): bump namespacelabs/nscloud-cache-action from 1.4.1 to 1.4.2 ([#10854](https://github.com/ghostty-org/ghostty/issues/10854)) ([@jcollie](https://github.com/jcollie))
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
  href="https://github.com/namespacelabs/nscloud-cache-action/compare/4d61c33d0b4333a518e975a0c4de7633d28713bb...a90bb5d4b27522ce881c6e98eebd7d7e6d1653f9">compare
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
- [`c11db66`](https://github.com/ghostty-org/ghostty/commit/c11db662e6f514350cbd8fcef06f81dc95260d00) toggle command palette works on gtk ([#10856](https://github.com/ghostty-org/ghostty/issues/10856)) ([@mitchellh](https://github.com/mitchellh))
- [`6692be4`](https://github.com/ghostty-org/ghostty/commit/6692be477d40f9eba49b861aa63ac67640b4bb4e) i18n: update hr locale with new strings ([#10792](https://github.com/ghostty-org/ghostty/issues/10792)) ([@Filip7](https://github.com/Filip7))
  ```text
  Translated freshly added tab and nautilus strings
  ```
- [`09c5d36`](https://github.com/ghostty-org/ghostty/commit/09c5d36d3fe3f246e4d6231a18af8db83c1b34a3) i18n: Update Hebrew (he_IL) translations for 1.3 (3 new strings) ([#10841](https://github.com/ghostty-org/ghostty/issues/10841)) ([@slsrepo](https://github.com/slsrepo))
  ```text
  Addressing the three newer strings [requested by Kat] in #10632.
  
  [requested by Kat]: https://github.com/ghostty-org/ghostty/issues/10632#issuecomment-3919649650
  ```
- [`2982bfa`](https://github.com/ghostty-org/ghostty/commit/2982bfa21a0172ca8918619b2bb3cf49172b1728) i18n: update ja_JP translation ([@kawarimidoll](https://github.com/kawarimidoll))
- [`3288a6e`](https://github.com/ghostty-org/ghostty/commit/3288a6e0a41c508bef5333fb2f4c7d2491f6cbad) i18n: update ja_JP translation ([#10829](https://github.com/ghostty-org/ghostty/issues/10829)) ([@00-kat](https://github.com/00-kat))
  ````text
  as requested in
  https://github.com/ghostty-org/ghostty/issues/10632#issuecomment-3919649650
  
  for Japanese reviewers:
  
  既存の以下に合わせ、
  
  ```
  msgid "Change Title…"
  msgstr "タイトルを変更…"
  
  msgid "Change Terminal Title"
  msgstr "ターミナルのタイトルを変更する"
  ```
  
  以下の2つでは末尾の表現を変えました。
  
  ```
  msgid "Change Tab Title…"
  msgstr "タブのタイトルを変更…"
  
  msgid "Change Tab Title"
  msgstr "タブのタイトルを変更する"
  ```
  ````
- [`7e19135`](https://github.com/ghostty-org/ghostty/commit/7e1913527a0ceab1a1958c96947e2593e07b9eba) Update VOUCHED list ([#10853](https://github.com/ghostty-org/ghostty/issues/10853)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/10702#issuecomment-3923898649)
  from @trag1c.
  ```

