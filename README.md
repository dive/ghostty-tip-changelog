> [!TIP]
> **Subscribe to Releases:** In GitHub, use `Watch -> Custom -> Releases` for this repository
> to get a daily notification with the previous day's Ghostty tip changes.

> [!NOTE]
> This changelog summarizes [Ghostty tip](https://tip.ghostty.org/) nightly builds.
> It is auto-updated every 3 hours by GitHub Actions and shows a rolling 7-day window by default.
>
> Entries are grouped by UTC day and combine commits across all successful runs for each day.
>
> Last updated: April 7, 2026 at 18:19 UTC.

## April 7, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/24088285274), [2](https://github.com/ghostty-org/ghostty/actions/runs/24082641330), [3](https://github.com/ghostty-org/ghostty/actions/runs/24065610222), [4](https://github.com/ghostty-org/ghostty/actions/runs/24062899731), [5](https://github.com/ghostty-org/ghostty/actions/runs/24061565576)  
Summary: 5 runs • 11 commits • 6 authors

### Changes

- [`853183e`](https://github.com/ghostty-org/ghostty/commit/853183e911b70ff7b61057f52fc7b47ea4934238) Update VOUCHED list ([#12165](https://github.com/ghostty-org/ghostty/issues/12165)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12164#discussioncomment-16477806)
  from @jcollie.
  
  Vouch: @MoonMao42
  ```
- [`355aecb`](https://github.com/ghostty-org/ghostty/commit/355aecb6ba26584c4430377dc0f6e9a0b0d59fe0) macos: cancel deferred tab presentation on close ([@jamylak](https://github.com/jamylak))
  ```text
  The 👻 Ghost Tab Issue
  
  Previous failure scenario (User perspective):
  
  1. Open a new tab
  2. Instantly trigger close other tabs
     (eg. through custom user keyboard shortcut)
  3. Now you will see an empty Ghost Tab
     (Only a window bar with empty content)
  
  The previous failure mode is:
  
  1. Create a tab or window now in `newTab(...)` / `newWindow(...)`.
  2. Queue its initial show/focus work with `DispatchQueue.main.async`.
  3. Close that tab or window with `closeTabImmediately()` /
   `closeWindowImmediately()` before the queued callback runs.
  4. The queued callback still runs anyway and calls `showWindow(...)` /
   `makeKeyAndOrderFront(...)` on stale state.
  5. The tab can be resurrected as a half-closed blank ghost tab.
  
  The fix:
  
  - Store deferred presentation work in a cancellable
    DispatchWorkItem and cancel it from the close paths
    before AppKit finishes tearing down the tab or window.
  - This prevents the stale show/focus callback from
    running after close.
  ```
- [`06340cd`](https://github.com/ghostty-org/ghostty/commit/06340cd3f05f7124c7757571a9fba77a30f78a53) libghostty-vt: add semver pre info to build info ([@jcollie](https://github.com/jcollie))
- [`5c45484`](https://github.com/ghostty-org/ghostty/commit/5c45484a717388395e8537dc35881c57940edf2d) build(deps): bump flatpak/flatpak-github-actions from 6.6 to 6.7 ([@dependabot[bot]](https://github.com/apps/dependabot))
  ```text
  Bumps [flatpak/flatpak-github-actions](https://github.com/flatpak/flatpak-github-actions) from 6.6 to 6.7.
  - [Release notes](https://github.com/flatpak/flatpak-github-actions/releases)
  - [Commits](https://github.com/flatpak/flatpak-github-actions/compare/92ae9851ad316786193b1fd3f40c4b51eb5cb101...401fe28a8384095fc1531b9d320b292f0ee45adb)
  
  ---
  updated-dependencies:
  - dependency-name: flatpak/flatpak-github-actions
    dependency-version: '6.7'
    dependency-type: direct:production
    update-type: version-update:semver-minor
  ...
  ```
- [`140ddd9`](https://github.com/ghostty-org/ghostty/commit/140ddd9770c1f139464a368359be6c370d609866) build(deps): bump flatpak/flatpak-github-actions from 6.6 to 6.7 ([#12154](https://github.com/ghostty-org/ghostty/issues/12154)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Bumps
  [flatpak/flatpak-github-actions](https://github.com/flatpak/flatpak-github-actions)
  from 6.6 to 6.7.
  <details>
  <summary>Release notes</summary>
  <p><em>Sourced from <a
  href="https://github.com/flatpak/flatpak-github-actions/releases">flatpak/flatpak-github-actions's
  releases</a>.</em></p>
  <blockquote>
  <h2>v6.7</h2>
  <ul>
  <li>Bump action to node 24</li>
  <li>Add the git commit as the ostree commit subject</li>
  <li>Allow configurable build/repo/state dirs</li>
  <li>Add keep-build-dirs flag</li>
  <li>Update action dependencies</li>
  <li>Improvements to contributing docs</li>
  </ul>
  </blockquote>
  </details>
  <details>
  <summary>Commits</summary>
  <ul>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/401fe28a8384095fc1531b9d320b292f0ee45adb"><code>401fe28</code></a>
  flatpak-builder: Add keepBuildDirs flag (<a
  href="https://redirect.github.com/flatpak/flatpak-github-actions/issues/229">#229</a>)</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/fc05c5ecc19c74ec586bd7a5bc32532ab3f0043f"><code>fc05c5e</code></a>
  action: Bump to node 24 (<a
  href="https://redirect.github.com/flatpak/flatpak-github-actions/issues/243">#243</a>)</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/ce5753fa4123107dee7bb03dd0d360c884baf222"><code>ce5753f</code></a>
  Some doc improvements (<a
  href="https://redirect.github.com/flatpak/flatpak-github-actions/issues/245">#245</a>)</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/fef33cbb5c2d1a311753adfa02239b91fb237077"><code>fef33cb</code></a>
  Update dependencies (<a
  href="https://redirect.github.com/flatpak/flatpak-github-actions/issues/244">#244</a>)</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/0a631396999e4243489a8a6ecf54fcb9f0575078"><code>0a63139</code></a>
  feat(flatpak-builder): Allow configurable build/repo/state dirs (<a
  href="https://redirect.github.com/flatpak/flatpak-github-actions/issues/237">#237</a>)</li>
  <li><a
  href="https://github.com/flatpak/flatpak-github-actions/commit/ad1b66ed726a37baa034681da3009761063ec360"><code>ad1b66e</code></a>
  flatpak-builder: Add the git commit as the ostree commit subject</li>
  <li>See full diff in <a
  href="https://github.com/flatpak/flatpak-github-actions/compare/92ae9851ad316786193b1fd3f40c4b51eb5cb101...401fe28a8384095fc1531b9d320b292f0ee45adb">compare
  view</a></li>
  </ul>
  </details>
  <br />
  
  
  [![Dependabot compatibility
  score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=flatpak/flatpak-github-actions&package-manager=github_actions&previous-version=6.6&new-version=6.7)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)
  
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
- [`2b62e3c`](https://github.com/ghostty-org/ghostty/commit/2b62e3c82a5541747a259b1dfe946ebd5993a471) libghostty-vt: add semver pre info to build info ([#12150](https://github.com/ghostty-org/ghostty/issues/12150)) ([@mitchellh](https://github.com/mitchellh))
- [`0043e66`](https://github.com/ghostty-org/ghostty/commit/0043e665f5a28a5eaa6bcb3090b56e8a5a7d0894) macos: cancel deferred tab presentation on close ([#12119](https://github.com/ghostty-org/ghostty/issues/12119)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The 👻 Ghost Tab Issue
  
  
  https://github.com/user-attachments/assets/cb91cd85-4a08-4c16-9efb-1a9ab30fc2bc
  
  Previous failure scenario (User perspective):
  
  1. Open a new tab
  2. Instantly trigger close other tabs (eg. through custom user keyboard
  shortcut)
  3. Now you will see an empty Ghost Tab (Only a window bar with empty
  content)
  
  The previous failure mode is:
  
  1. Create a tab or window now in `newTab(...)` / `newWindow(...)`.
  2. Queue its initial show/focus work with `DispatchQueue.main.async`.
  3. Close that tab or window with `closeTabImmediately()` /
  `closeWindowImmediately()` before the queued callback runs.
  4. The queued callback still runs anyway and calls `showWindow(...)` /
  `makeKeyAndOrderFront(...)` on stale state.
  5. The tab can be resurrected as a half-closed blank ghost tab.
  
  The fix:
  
  - Store deferred presentation work in a cancellable DispatchWorkItem and
  cancel it from the close paths before AppKit finishes tearing down the
  tab or window.
  - This prevents the stale show/focus callback from running after close.
  
  ## AI Usage
  
  I used GPT 5.4 to find the initial issue and fix it. I cleaned up and
  narrowed down the commit afterwards.
  
  -----
  
  Additional Notes:
  
  I use `cmd+o` to `close_tab:other`
  
  https://github.com/jamylak/dotfiles/blob/main/ghostty/config#L106C1-L106C34
  
  Try it for your self if you want to reproduce, just do a quick `cmd+t`
  `cmd+o` and you will see
  ```
- [`95fb39a`](https://github.com/ghostty-org/ghostty/commit/95fb39ae0cb8d0f8cfe2e4e50a5278d2b8983335) chore: removed superfluous word ([@tbrundige](https://github.com/tbrundige))
- [`ee236e9`](https://github.com/ghostty-org/ghostty/commit/ee236e9a73951689ee77af9c07f25c15cb64c52c) chore: removed superfluous word ([#12160](https://github.com/ghostty-org/ghostty/issues/12160)) ([@jcollie](https://github.com/jcollie))
  ```text
  I noticed a likely unintentional "actually" in the README. Nothing
  fancy, just updating the documentation.
  ```
- [`a1e75da`](https://github.com/ghostty-org/ghostty/commit/a1e75daef8b64426dbca551c6e41b1fbc2b7ae24) Update VOUCHED list ([#12158](https://github.com/ghostty-org/ghostty/issues/12158)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12157#discussioncomment-16470907)
  from @jcollie.
  
  Vouch: @tbrundige
  ```
- [`8f376d8`](https://github.com/ghostty-org/ghostty/commit/8f376d84b495a389c8859309df9b35c7355c9c97) Update VOUCHED list ([#12156](https://github.com/ghostty-org/ghostty/issues/12156)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12155#discussioncomment-16470483)
  from @jcollie.
  
  Vouch: @KieranCanter
  ```

## April 6, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/24053831175), [2](https://github.com/ghostty-org/ghostty/actions/runs/24051267343), [3](https://github.com/ghostty-org/ghostty/actions/runs/24049440104), [4](https://github.com/ghostty-org/ghostty/actions/runs/24047275570), [5](https://github.com/ghostty-org/ghostty/actions/runs/24039345933), [6](https://github.com/ghostty-org/ghostty/actions/runs/24036582590), [7](https://github.com/ghostty-org/ghostty/actions/runs/24035367670), [8](https://github.com/ghostty-org/ghostty/actions/runs/24018750527)  
Summary: 8 runs • 46 commits • 5 authors

### Changes

- [`05fb57d`](https://github.com/ghostty-org/ghostty/commit/05fb57dd4044dbd44f5b751afaa0beafea9df4bb) build: emit xcframework for libghostty-vt on macOS ([@mitchellh](https://github.com/mitchellh))
  ```text
  On Darwin targets, the build now automatically produces a universal
  (arm64 + x86_64) XCFramework at lib/ghostty-vt.xcframework under
  the install prefix. This bundles the fat static library with headers
  so consumers using Xcode or Swift PM can link libghostty-vt directly.
  ```
- [`f567f7f`](https://github.com/ghostty-org/ghostty/commit/f567f7f46d0b60da3fddb18070e74b1c0deb074f) build: add GhosttyVt module map to xcframework and Swift example ([@mitchellh](https://github.com/mitchellh))
  ```text
  The xcframework now generates its own headers directory with a
  GhosttyVt module map instead of reusing include/ directly, which
  contains the GhosttyKit module map for the macOS app. The generated
  directory copies the ghostty headers and adds a module.modulemap
  that exposes ghostty/vt.h as the umbrella header.
  
  A new swift-vt-xcframework example demonstrates consuming the
  xcframework from a Swift Package. It creates a terminal, writes
  VT sequences, and formats the output as plain text, verifying
  the full round-trip works with swift build and swift run.
  ```
- [`764ff18`](https://github.com/ghostty-org/ghostty/commit/764ff18b8edef150c7736d16a82a3f4e557fc374) ci: add Swift example builds on macOS ([@mitchellh](https://github.com/mitchellh))
  ```text
  Auto-discover Swift examples via example/*/Package.swift alongside
  the existing zig and cmake discovery. The new build-examples-swift
  job runs on macOS, builds the xcframework with zig build -Demit-lib-vt,
  then runs swift run in each example directory to verify the
  xcframework links and functions correctly end-to-end.
  ```
- [`90b706b`](https://github.com/ghostty-org/ghostty/commit/90b706b97703bcec3dab6c2285acf86685e5fdfb) ci: publish lib-vt xcframework in tip releases ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a build-lib-vt-xcframework job to the release-tip workflow that
  builds the universal xcframework with ReleaseFast, zips it, signs
  it with minisign, and uploads it to both the GitHub Release and R2
  blob storage. Consumers can pull the xcframework zip from the tip
  release or by commit hash from tip.files.ghostty.org.
  ```
- [`e1a0e40`](https://github.com/ghostty-org/ghostty/commit/e1a0e40ec4cfd7ae6ed7d99b92db733cea95a2c0) build: skip xcframework when cross-compiling ([@mitchellh](https://github.com/mitchellh))
  ```text
  Gate the xcframework build on the host being macOS in addition to
  the target, since xcodebuild is only available on macOS.
  ```
- [`9b281cd`](https://github.com/ghostty-org/ghostty/commit/9b281cde4324f9a4c993c6776829fb64ce601f77) build: add iOS slices to lib-vt xcframework ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add iOS device and simulator slices to the xcframework, gated on
  SDK availability via std.zig.LibCInstallation.findNative. Refactor
  AppleLibs from a struct with named fields to an EnumMap keyed by
  ApplePlatform so that adding new platforms only requires extending
  the enum and its sdk_platforms table.
  
  tvOS, watchOS, and visionOS are listed as not yet supported due to
  Zig stdlib limitations (missing PATH_MAX, mcontext fields).
  ```
- [`249aee7`](https://github.com/ghostty-org/ghostty/commit/249aee70105facdfdf0e627be4f0c0d342ce08a0) example/swift-vt-xcframework: fix buffer overflow ([@mitchellh](https://github.com/mitchellh))
- [`445e194`](https://github.com/ghostty-org/ghostty/commit/445e1945da573a5b63adb4e4e7294c135cb0e86a) ci: upload lib-vt source tarball to R2 ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add R2 upload steps to the source-tarball-lib-vt job in the tip
  release workflow, matching the pattern used by the xcframework
  job. The tarball is uploaded to the ghostty-tip R2 bucket keyed
  by commit hash, making it available at
  tip.files.ghostty.org/<commit>/libghostty-vt-source.tar.gz.
  ```
- [`c12a0e3`](https://github.com/ghostty-org/ghostty/commit/c12a0e395d75c19b0a2c841f021885f535e68cbc) libghostty: build universal xcframework and release it on tip ([#12149](https://github.com/ghostty-org/ghostty/issues/12149)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This produces a `ghostty-vt.xcframework` for `zig build -Demit-lib-vt`
  when the host is macOS and the target is Apple platforms. Our CI has
  been updated to release this via tip channels (GH releases and our blob
  storage), too.
  
  The xcframework contains binaries for macOS Universal (x86_64 +
  aarch64), iOS, and iOS simulator.
  
  I've added a Swift example we run in CI to verify this works. Users can
  also drag and drop the XCFramework directly into Xcode.
  
  ## Example
  
  ```swift
  // swift-tools-version: 5.9
  import PackageDescription
  
  let package = Package(
      name: "swift-vt-xcframework",
      platforms: [.macOS(.v13)],
      targets: [
          .executableTarget(
              name: "swift-vt-xcframework",
              dependencies: ["GhosttyVt"],
              path: "Sources",
              linkerSettings: [
                  .linkedLibrary("c++"),
              ]
          ),
          .binaryTarget(
              name: "GhosttyVt",
              path: "../../zig-out/lib/ghostty-vt.xcframework"
          ),
      ]
  )
  ```
  
  ```swift
  import GhosttyVt
  
  // Create a terminal with a small grid
  var terminal: GhosttyTerminal?
  var opts = GhosttyTerminalOptions(
      cols: 80,
      rows: 24,
      max_scrollback: 0
  )
  let result = ghostty_terminal_new(nil, &terminal, opts)
  guard result == GHOSTTY_SUCCESS, let terminal else {
      fatalError("Failed to create terminal")
  }
  
  // Write some VT-encoded content
  let text = "Hello from \u{1b}[1mSwift\u{1b}[0m via xcframework!\r\n"
  text.withCString { ptr in
      ghostty_terminal_vt_write(terminal, ptr, strlen(ptr))
  }
  
  // Format the terminal contents as plain text
  var fmtOpts = GhosttyFormatterTerminalOptions()
  fmtOpts.size = MemoryLayout<GhosttyFormatterTerminalOptions>.size
  fmtOpts.emit = GHOSTTY_FORMATTER_FORMAT_PLAIN
  fmtOpts.trim = true
  
  var formatter: GhosttyFormatter?
  let fmtResult = ghostty_formatter_terminal_new(nil, &formatter, terminal, fmtOpts)
  guard fmtResult == GHOSTTY_SUCCESS, let formatter else {
      fatalError("Failed to create formatter")
  }
  
  var buf: UnsafeMutablePointer<UInt8>?
  var len: Int = 0
  let allocResult = ghostty_formatter_format_alloc(formatter, nil, &buf, &len)
  guard allocResult == GHOSTTY_SUCCESS, let buf else {
      fatalError("Failed to format")
  }
  
  print("Plain text (\(len) bytes):")
  print(String(cString: buf))
  
  ghostty_free(nil, buf, len)
  ghostty_formatter_free(formatter)
  ghostty_terminal_free(terminal)
  ```
  ````
- [`da83575`](https://github.com/ghostty-org/ghostty/commit/da835757b0330474ec4050fa2b149a9b0c887d52) prettier: ignore swift outputs ([@mitchellh](https://github.com/mitchellh))
- [`06144d3`](https://github.com/ghostty-org/ghostty/commit/06144d30f2541508d1fe8f10083bd87ff422af72) libghostty-vt: allow version to be customized from the Zig build command ([@jcollie](https://github.com/jcollie))
- [`f7a9e31`](https://github.com/ghostty-org/ghostty/commit/f7a9e313cd39e8c08f3b306fa808ca97cbd55d27) libghostty-vt: allow version to be customized from the Zig build command ([#12104](https://github.com/ghostty-org/ghostty/issues/12104)) ([@mitchellh](https://github.com/mitchellh))
- [`66bfdf8`](https://github.com/ghostty-org/ghostty/commit/66bfdf8e7a2662d9a10c702edd69bc14cc0886a6) libghostty: add z-layer filtered placement iterator ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a placement_iterator_set function that configures iterator
  properties via an enum, following the same pattern as other set
  functions in the C API (e.g. render_state_set). The first settable
  option is a z-layer filter.
  
  The GhosttyKittyPlacementLayer enum classifies placements into three
  layers based on kitty protocol z-index conventions: below background
  (z < INT32_MIN/2), below text (INT32_MIN/2 <= z < 0), and above text
  (z >= 0). The default is ALL which preserves existing behavior.
  
  When a layer filter is set, placement_iterator_next automatically
  skips non-matching placements, so embedders no longer need to
  reimplement the z-index bucketing logic or iterate all placements
  three times per frame just to filter by layer.
  ```
- [`b43d35b`](https://github.com/ghostty-org/ghostty/commit/b43d35b4d3c147b637fed085fca4d4dad277fc80) libghostty: add viewport-relative placement positioning ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add ghostty_kitty_graphics_placement_viewport_pos which converts a
  placement's internal pin to viewport-relative grid coordinates.
  The returned row can be negative when the placement's origin has
  scrolled above the viewport, allowing embedders to compute the
  correct destination rectangle for partially visible images.
  
  Returns GHOSTTY_NO_VALUE only when the placement is completely
  outside the viewport (bottom edge above the viewport or top edge
  at or below the last row), so embedders do not need to perform
  their own visibility checks. Partially visible placements always
  return GHOSTTY_SUCCESS with their true signed coordinates.
  ```
- [`d712bef`](https://github.com/ghostty-org/ghostty/commit/d712beff5b616f1f886937c6de8e8105b9f3956e) libghostty: add resolved source rect for placements ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add ghostty_kitty_graphics_placement_source_rect which returns the
  fully resolved and clamped source rectangle for a placement. This
  applies kitty protocol semantics (width/height of 0 means full
  image dimension) and clamps the result to the actual image bounds,
  eliminating ~20 lines of protocol-aware logic from each embedder.
  ```
- [`65e3265`](https://github.com/ghostty-org/ghostty/commit/65e3265e3cd4df063a83fcabfa7fd2a4b61627b5) libghostty: fix kitty graphics test failures ([@mitchellh](https://github.com/mitchellh))
  ```text
  Fix three categories of test bugs in the kitty graphics C API tests:
  
  The placement iterator reset in getTyped was clobbering the
  layer_filter field when reinitializing the iterator struct,
  causing the layer filter test to see unfiltered placements.
  Preserve layer_filter across resets.
  
  The viewport position tests were not accounting for the default
  cursor_movement=after behavior of the kitty display command,
  which calls index() for each row of the placement before the
  test scroll sequence. Add C=1 to suppress cursor movement so
  the scroll math in the tests is correct.
  
  The source_rect tests used an 88-character all-A base64 payload
  which decodes to 66 bytes, but a 4x4 RGBA image requires exactly
  64 bytes. Fix the payload to use proper base64 padding (AA==).
  ```
- [`fdb6e3d`](https://github.com/ghostty-org/ghostty/commit/fdb6e3d2c8543e2e756b7e07f44372efbc0fba4b) libghostty: add z-layer filtering, viewport positioning, and source rects for kitty graphics placements ([#12147](https://github.com/ghostty-org/ghostty/issues/12147)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Based on the Ghostling implementation, these are APIs that will help
  other implementors:
  
  **Z-layer filtering.** The placement iterator now supports a
  configurable layer filter via a new
  `ghostty_kitty_graphics_placement_iterator_set()` option API. When a
  layer is set, `ghostty_kitty_graphics_placement_next()` skips placements
  whose z-index doesn't match the requested layer. The three layers follow
  the kitty protocol z-index conventions (below background, below text,
  above text) and map directly to distinct rendering passes. Default is
  `ALL` (no filtering, existing behavior).
  
  **Viewport-relative positioning.**
  `ghostty_kitty_graphics_placement_viewport_pos()` converts a placement's
  internal pin to viewport-relative grid coordinates. The row value can be
  negative for placements that have partially scrolled above the viewport.
  Returns `GHOSTTY_NO_VALUE` when the placement is entirely off-screen or
  is a virtual (unicode placeholder) placement, so the renderer can skip
  it without extra math.
  
  **Source rectangle resolution.**
  `ghostty_kitty_graphics_placement_source_rect()` applies kitty protocol
  semantics (0 = full image dimension) and clamps to image bounds,
  returning pixel coordinates ready for texture sampling.
  
  ## New APIs
  
  | Function | Description |
  |----------|-------------|
  | `ghostty_kitty_graphics_placement_iterator_set` | Set an option on a
  placement iterator (currently: z-layer filter) |
  | `ghostty_kitty_graphics_placement_viewport_pos` | Get
  viewport-relative grid position of the current placement |
  | `ghostty_kitty_graphics_placement_source_rect` | Get the resolved
  source rectangle in pixels for the current placement |
  
  ## New Types
  
  | Type | Description |
  |------|-------------|
  | `GhosttyKittyPlacementLayer` | Z-layer classification: `ALL`,
  `BELOW_BG`, `BELOW_TEXT`, `ABOVE_TEXT` |
  | `GhosttyKittyGraphicsPlacementIteratorOption` | Settable iterator
  options (currently: `LAYER`) |
  ```
- [`a977822`](https://github.com/ghostty-org/ghostty/commit/a977822b58634e0aa12aecc65fe316a56f9becab) update kitty graphics docs ([@mitchellh](https://github.com/mitchellh))
- [`e89b2c8`](https://github.com/ghostty-org/ghostty/commit/e89b2c88f3a07956bd02bbd8279ead3bcbdd03a4) libghostty: introduce the kitty graphics opaque type ([@mitchellh](https://github.com/mitchellh))
- [`9033f6f`](https://github.com/ghostty-org/ghostty/commit/9033f6f8ce2bc50fb2529616764fcb2325ae67b2) libghostty: add kitty graphics placement iterator API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a C API for iterating over Kitty graphics placements via the
  new GhosttyKittyGraphics opaque handle. The API follows the same
  pattern as the render state row iterator: allocate an iterator with
  ghostty_kitty_graphics_placement_iterator_new, populate it from a
  graphics handle via ghostty_kitty_graphics_get with the
  PLACEMENT_ITERATOR data kind, advance with
  ghostty_kitty_graphics_placement_next, and query per-placement
  fields with ghostty_kitty_graphics_placement_get.
  ```
- [`46a69ea`](https://github.com/ghostty-org/ghostty/commit/46a69ea63d2891eca2e404eddd1bfbd84c66de0c) libghostty: add kitty graphics image lookup API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a GhosttyKittyGraphicsImage opaque type and API for looking up
  images by ID and querying their properties. This complements the
  existing placement iterator by allowing direct image introspection.
  
  The new ghostty_kitty_graphics_image() function looks up an image by
  its ID from the storage, returning a borrowed opaque handle. Properties
  are queried via ghostty_kitty_image_get() using the new
  GhosttyKittyGraphicsImageData enum, which exposes id, number, width,
  height, format, compression, and a borrowed data pointer with length.
  
  Format and compression are exposed as their own C enum types
  (GhosttyKittyImageFormat and GhosttyKittyImageCompression) rather
  than raw integers.
  ```
- [`9ff4bb2`](https://github.com/ghostty-org/ghostty/commit/9ff4bb2df5d2542f7f4e189aebe309d907e3449e) terminal/kitty: convert Format, Medium, Compression to lib.Enum ([@mitchellh](https://github.com/mitchellh))
  ```text
  Convert the Transmission.Format, Transmission.Medium, and
  Transmission.Compression types from plain Zig enums to lib.Enum so
  they get a C-compatible backing type when building with c_abi. This
  lets the C API layer reuse the types directly instead of maintaining
  separate mirror enums.
  
  Move Format.bpp() to a standalone Transmission.formatBpp() function
  since lib.Enum types cannot have decls.
  
  In the C API layer, rename kitty_gfx to kitty_storage and command to
  kitty_cmd for clarity, and simplify the format/compression getters
  to direct assignment now that the types are shared.
  ```
- [`7144204`](https://github.com/ghostty-org/ghostty/commit/714420409be233bb0acacdc60f6d15f6822de8e1) libghostty: add placement_rect and centralize opaque typedefs ([@mitchellh](https://github.com/mitchellh))
  ```text
  Expose Placement.rect() from the Zig kitty graphics storage as a new
  C API function ghostty_kitty_graphics_placement_rect(). It takes the
  terminal, image handle, and a positioned placement iterator, and
  writes the bounding grid rectangle into a GhosttySelection out param.
  Virtual placements return GHOSTTY_NO_VALUE.
  
  Move all opaque handle typedefs (GhosttyTerminal, GhosttyKittyGraphics,
  GhosttyRenderState, GhosttySgrParser, GhosttyFormatter, GhosttyOsc*)
  into types.h so they are available everywhere without circular includes
  and Doxygen renders them in the correct @ingroup sections.
  ```
- [`03a6eed`](https://github.com/ghostty-org/ghostty/commit/03a6eeda1de9b00164c97960b176fe2b8457acb9) libghostty: add placement pixel_size and grid_size, rename calculatedSize ([@mitchellh](https://github.com/mitchellh))
  ```text
  Expose Placement.pixelSize() and Placement.gridSize() as new C API
  functions ghostty_kitty_graphics_placement_pixel_size() and
  ghostty_kitty_graphics_placement_grid_size(). Both take the placement
  iterator, image handle, and terminal, returning their results via
  out params.
  
  Rename the internal Zig method from calculatedSize to pixelSize to
  pair naturally with gridSize — one returns pixels, the other grid
  cells. Updated all callers including the renderer.
  ```
- [`426dc40`](https://github.com/ghostty-org/ghostty/commit/426dc40799407b3ec564324438b73cce03f79835) example: update c-vt-kitty-graphics to use new APIs ([@mitchellh](https://github.com/mitchellh))
- [`68a8cbb`](https://github.com/ghostty-org/ghostty/commit/68a8cbb065028b8de4f3b9e0d1676891e8018bbe) libghostty: fix expected format in image_get test ([@mitchellh](https://github.com/mitchellh))
  ```text
  The test transmits an image with f=24 (24-bit RGB) but was asserting
  that the format field equals .rgba (32-bit). Corrected the expectation
  to .rgb to match the transmitted pixel format.
  ```
- [`fc9299a`](https://github.com/ghostty-org/ghostty/commit/fc9299a41df3c2cb7c987350e9a5cb67433e2835) libghostty: rename ghostty_kitty_image_get to ghostty_kitty_graphics_image_get ([@mitchellh](https://github.com/mitchellh))
  ```text
  Rename the public API function to follow the consistent
  ghostty_kitty_graphics_* naming convention used by the other
  kitty graphics API symbols.
  ```
- [`20b7fe0`](https://github.com/ghostty-org/ghostty/commit/20b7fe0e1dd485af1f64ff5ce5d08135274896e9) libghostty: gate kitty graphics placement types on build option ([@mitchellh](https://github.com/mitchellh))
  ```text
  The PlacementIterator, PlacementMap, and PlacementIteratorWrapper
  types in the C API were unconditionally referencing
  kitty_storage.ImageStorage, which transitively pulled in
  Image.transmit_time (std.time.Instant). On wasm32-freestanding,
  std.time.Instant requires posix.timespec which does not exist,
  causing a compilation error.
  
  Gate these types behind build_options.kitty_graphics, matching the
  existing pattern used for KittyGraphics and ImageHandle. When
  kitty graphics is disabled, they fall back to opaque/void types.
  Add early-return guards to placement_iterator_new and
  placement_iterator_free which directly operate on the wrapper
  struct.
  ```
- [`6b94c2d`](https://github.com/ghostty-org/ghostty/commit/6b94c2da26653cc8feeaee3ef90166b3ad1e3aee) libghostty: add ghostty_terminal_point_from_grid_ref ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add the inverse of ghostty_terminal_grid_ref(), converting a grid
  reference back to coordinates in a requested coordinate system
  (active, viewport, screen, or history). This wraps the existing
  internal PageList.pointFromPin and is placed on the terminal API
  since it requires terminal-owned PageList state to resolve the
  top-left anchor for each coordinate system.
  
  Returns GHOSTTY_NO_VALUE when the ref falls outside the requested
  range, e.g. a scrollback ref cannot be expressed in active
  coordinates.
  ```
- [`800cc64`](https://github.com/ghostty-org/ghostty/commit/800cc64f1b7699c68d0db823b708388f04605e67) libghostty: C APIs for Kitty Graphics inspection ([#12145](https://github.com/ghostty-org/ghostty/issues/12145)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This adds a C API for inspecting Kitty graphics image storage, images,
  and placements from a terminal instance.
  
  I think this is enough of the API surface area for a renderer to draw
  images. But I'll have to add it to Ghostling to be sure.
  
  ## Example
  
  ```c
  #include <stdint.h>
  #include <stdio.h>
  #include <ghostty/vt.h>
  
  /* After creating a terminal and transmitting a Kitty graphics image... */
  
  /* Get the kitty graphics storage from the terminal. */
  GhosttyKittyGraphics graphics = NULL;
  ghostty_terminal_get(terminal, GHOSTTY_TERMINAL_DATA_KITTY_GRAPHICS, &graphics);
  
  /* Iterate over all placements. */
  GhosttyKittyGraphicsPlacementIterator iter = NULL;
  ghostty_kitty_graphics_placement_iterator_new(NULL, &iter);
  ghostty_kitty_graphics_get(graphics,
      GHOSTTY_KITTY_GRAPHICS_DATA_PLACEMENT_ITERATOR, &iter);
  
  while (ghostty_kitty_graphics_placement_next(iter)) {
    uint32_t image_id = 0;
    ghostty_kitty_graphics_placement_get(iter,
        GHOSTTY_KITTY_GRAPHICS_PLACEMENT_DATA_IMAGE_ID, &image_id);
  
    /* Look up the image and query its properties. */
    GhosttyKittyGraphicsImage image = ghostty_kitty_graphics_image(graphics, image_id);
    uint32_t width = 0, height = 0;
    GhosttyKittyImageFormat format = 0;
    ghostty_kitty_image_get(image, GHOSTTY_KITTY_IMAGE_DATA_WIDTH, &width);
    ghostty_kitty_image_get(image, GHOSTTY_KITTY_IMAGE_DATA_HEIGHT, &height);
    ghostty_kitty_image_get(image, GHOSTTY_KITTY_IMAGE_DATA_FORMAT, &format);
    printf("image %u: %ux%u format=%d\n", image_id, width, height, format);
  
    /* Compute rendered pixel size and grid size. */
    uint32_t px_w, px_h, cols, rows;
    ghostty_kitty_graphics_placement_pixel_size(iter, image, terminal, &px_w, &px_h);
    ghostty_kitty_graphics_placement_grid_size(iter, image, terminal, &cols, &rows);
    printf("  rendered: %ux%u px, %ux%u cells\n", px_w, px_h, cols, rows);
  }
  
  ghostty_kitty_graphics_placement_iterator_free(iter);
  ```
  
  ## API
  
  ### Functions
  
  | Function | Description |
  |----------|-------------|
  | `ghostty_kitty_graphics_get` | Query data from a kitty graphics
  storage (e.g. placement iterator) |
  | `ghostty_kitty_graphics_image` | Look up an image by its image ID |
  | `ghostty_kitty_graphics_image_get` | Query image properties (ID,
  dimensions, format, compression, pixel data) |
  | `ghostty_kitty_graphics_placement_iterator_new` | Create a new
  placement iterator |
  | `ghostty_kitty_graphics_placement_iterator_free` | Free a placement
  iterator |
  | `ghostty_kitty_graphics_placement_next` | Advance the iterator to the
  next placement |
  | `ghostty_kitty_graphics_placement_get` | Query placement properties
  (image ID, offsets, source rect, z-index, etc.) |
  | `ghostty_kitty_graphics_placement_rect` | Compute the bounding grid
  rectangle for a placement |
  | `ghostty_kitty_graphics_placement_pixel_size` | Compute the rendered
  pixel dimensions of a placement |
  | `ghostty_kitty_graphics_placement_grid_size` | Compute the grid cell
  dimensions of a placement |
  
  ### Types
  
  | Type | Description |
  |------|-------------|
  | `GhosttyKittyGraphics` | Opaque handle to image storage (borrowed from
  terminal) |
  | `GhosttyKittyGraphicsImage` | Opaque handle to a single image |
  | `GhosttyKittyGraphicsPlacementIterator` | Opaque handle to a placement
  iterator |
  | `GhosttyKittyGraphicsData` | Enum for `ghostty_kitty_graphics_get`
  data kinds |
  | `GhosttyKittyGraphicsImageData` | Enum for `ghostty_kitty_image_get`
  data kinds |
  | `GhosttyKittyGraphicsPlacementData` | Enum for
  `ghostty_kitty_graphics_placement_get` data kinds |
  | `GhosttyKittyImageFormat` | Image pixel format (RGB, RGBA, PNG, gray,
  gray+alpha) |
  | `GhosttyKittyImageCompression` | Image compression (none, zlib) |
  ````
- [`3a52e0e`](https://github.com/ghostty-org/ghostty/commit/3a52e0e3bdba98b5372cf0f2d5ca5f150b8c09d7) libghostty: expose kitty image options via terminal set/get ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add four new terminal options for configuring Kitty graphics at runtime
  through the C API: storage limit, and the three loading medium flags
  (file, temporary file, shared memory).
  
  The storage limit setter propagates to all initialized screens and
  uses setLimit which handles eviction when lowering the limit. The
  medium setters similarly propagate to all screens. Getters read from
  the active screen. All options compile to no-ops or return no_value
  when kitty graphics are disabled at build time.
  ```
- [`d7fa920`](https://github.com/ghostty-org/ghostty/commit/d7fa92088c0e50d02d97190973b91d49d0c39d6a) libghostty: expose sys interface to C API ([@mitchellh](https://github.com/mitchellh))
  ```text
  The terminal sys module provides runtime-swappable function pointers
  for operations that depend on external implementations (e.g. PNG
  decoding). This exposes that functionality through the C API via a
  ghostty_sys_set() function, modeled after the ghostty_terminal_set()
  enum-based option pattern.
  
  Embedders can install a PNG decode callback to enable Kitty Graphics
  Protocol PNG support. The callback receives a userdata pointer
  (set via GHOSTTY_SYS_OPT_USERDATA) and a GhosttyAllocator that must
  be used to allocate the returned pixel data, since the library takes
  ownership of the buffer. Passing NULL clears the callback and
  disables the feature.
  ```
- [`64340c6`](https://github.com/ghostty-org/ghostty/commit/64340c62bfab76147d6fa4aec4d4979d3c4d2e33) example: add c-vt-kitty-graphics ([@mitchellh](https://github.com/mitchellh))
  ```text
  Demonstrates the sys interface for Kitty Graphics Protocol PNG
  support. The example installs a PNG decode callback via
  ghostty_sys_set, creates a terminal with image storage enabled,
  and sends an inline 1x1 PNG image through vt_write. Snippet
  markers are wired up to the sys.h doxygen docs.
  ```
- [`f65fb3d`](https://github.com/ghostty-org/ghostty/commit/f65fb3d44265f9c199df0a78f4788dc62a20b018) libghostty: expose Kitty image configs, decode png callback from C API ([#12144](https://github.com/ghostty-org/ghostty/issues/12144)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This exposes the APIs necessary to enable Kitty image protocol parsing
  and state from the C API.
  
  * You can now set the PNG decoder via the `ghostty_sys_set` API.
  * You can set Kitty image configs via `ghostty_terminal_set` API.
  * An example showing this working has been added.
  * **You cannot yet query Kitty images for metadata or rendering.** I'm
  going to follow that up in a separate PR.
  ```
- [`e390937`](https://github.com/ghostty-org/ghostty/commit/e390937867b99efce6f8ac27a033088500fe6201) macos: fix badge permission ([@KayLeung](https://github.com/KayLeung))
  ```text
  The previous version requested general notification permissions but omitted the `.badge` option. Because the initial request was granted, `settings.authorizationStatus` returns `.authorized`, leading the app to believe it has full notification privileges when it actually lacks the authority to update the dock icon badge.
  ```
- [`13f7d23`](https://github.com/ghostty-org/ghostty/commit/13f7d23145891fbe3a99c268e7df388a3c9e52fc) macOS: force layout sync when frame size mismatches GeometryReader ([@fru1tworld](https://github.com/fru1tworld))
- [`fd884bc`](https://github.com/ghostty-org/ghostty/commit/fd884bc532ca8a667a3b8397037ef382d18efc68) macOS: force surface layout sync in updateOSView ([#12143](https://github.com/ghostty-org/ghostty/issues/12143)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  `updateOSView` assumed SwiftUI always propagates frame changes to the
  scroll view. Under system load, this can be deferred, leaving the
  surface rendering at stale dimensions. Check for size mismatch and mark
  layout as needed.
  
  
  <img width="1408" height="464" alt="ghostty_bug"
  src="https://github.com/user-attachments/assets/3a6f81ff-9d02-4ffa-aded-e2eddc9f40a5"
  />
  
  ---
  AI Disclosure: Used Claude Code for PR preparation.
  ```
- [`8ae8089`](https://github.com/ghostty-org/ghostty/commit/8ae80892baba44eb49faf0b33f142c120ac04412) macos: fix dock icon badge permission ([#12133](https://github.com/ghostty-org/ghostty/issues/12133)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The previous version requested general notification permissions but
  omitted the `.badge` option. Because the initial request was granted,
  `settings.authorizationStatus` returns `.authorized`, leading the app to
  believe it has full notification privileges when it actually lacks the
  authority to update the dock icon badge.
  
  Debug hint:
  You can reset the notification settings by right-clicking on the app
  name.
  <img width="307" height="85" alt=""
  src="https://github.com/user-attachments/assets/660cd332-eda6-45d6-8bfd-a6f9e28e21e8"
  />
  ```
- [`29e3de7`](https://github.com/ghostty-org/ghostty/commit/29e3de737e9cc4c4d6a3ac9624bbd26c87bf0eb2) terminal: make wuffs runtime-swappable, enable Kitty graphics for libvt ([@mitchellh](https://github.com/mitchellh))
  ```text
  Introduce terminal/sys.zig which provides runtime-swappable function
  pointers for operations that depend on external implementations. This
  allows embedders of the terminal package to swap out implementations
  at startup without hard dependencies on specific libraries.
  
  The first function exposed is decode_png, which defaults to a wuffs
  implementation. The kitty graphics image loader now calls through
  sys.decode_png instead of importing wuffs directly.
  
  This allows us to enable Kitty graphics support in libghostty-vt
  for all targets except wasm32-freestanding.
  ```
- [`6a99c24`](https://github.com/ghostty-org/ghostty/commit/6a99c248d0c2a952bf0ba1333247f3fa4e381184) terminal/kitty: add Limits to restrict capabilities of image transfer ([@mitchellh](https://github.com/mitchellh))
- [`64dcb91`](https://github.com/ghostty-org/ghostty/commit/64dcb91c1f3f1122706f70b888948d19fb1d7c42) terminal/kitty: add loading limits to kitty graphics protocol ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a Limits type to LoadingImage that controls which transmission
  mediums (file, temporary_file, shared_memory) are allowed when
  loading images. This defaults to "direct" (most restrictive) on
  ImageStorage and is set to "all" by Termio, allowing apprt
  embedders like libghostty to restrict medium types for resource or
  security reasons.
  
  The limits are stored on ImageStorage, plumbed through
  Screen.Options for screen initialization and inheritance, and
  enforced in graphics_exec during both query and transmit. Two new
  Terminal methods (setKittyGraphicsSizeLimit, setKittyGraphicsLoadingLimits)
  centralize updating all screens, replacing the manual iteration
  previously done in Termio.
  ```
- [`935d37f`](https://github.com/ghostty-org/ghostty/commit/935d37fbf1eea969245e144757116e8fbe93192a) terminal: add kitty image limits to Terminal.Options ([@mitchellh](https://github.com/mitchellh))
  ```text
  Move kitty_image_storage_limit and kitty_image_loading_limits into
  Terminal.Options so callers can set them at construction time
  rather than calling setter functions after init. The values flow
  through to Screen.Options during ScreenSet initialization. Termio
  now passes both at construction, keeping the setter functions for
  the updateConfig path.
  ```
- [`306acc4`](https://github.com/ghostty-org/ghostty/commit/306acc494128e54e1702e872d15cbf661b3c9e0a) terminal/kitty: use direct medium for tests if we're not using files ([@mitchellh](https://github.com/mitchellh))
- [`810ebae`](https://github.com/ghostty-org/ghostty/commit/810ebae8e8eca363b46553b62db7fc7bfe69e24b) terminal: lower default kitty image storage limit for libghostty ([@mitchellh](https://github.com/mitchellh))
  ```text
  The default kitty image storage limit was 320 MB for all build
  artifacts. For libghostty, this is overly generous since it is an
  embedded library where conservative memory usage is preferred.
  Lower the default to 10 MB when building as the lib artifact while
  keeping the 320 MB default for the full Ghostty application.
  ```
- [`c9c3c70`](https://github.com/ghostty-org/ghostty/commit/c9c3c701e23634fd13913cb8943962e267b00d3a) terminal: make wuffs runtime-swappable, enable Kitty graphics for libvt ([#12117](https://github.com/ghostty-org/ghostty/issues/12117)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This enables Kitty Graphics for `libghostty-vt` for the Zig API (C to
  come next).
  
  First, a note on security: by default, Kitty graphics will only allow
  images transferred via the _direct_ medium (directly via the pty) and
  will not allow file or shared memory based images. libghostty-vt
  consumers need to manually opt-in via terminal init options or
  `terminal.setKittyGraphicsLoadingLimits` to enable file-based things.
  **This is so we're as secure as possible by default.**
  
  Second, for PNG decoding, embedders must now set a global
  runtime-callback at `ghostty.sys.decode_png`. If this is not set, PNG
  formatted images are rejected. If this is set, then we'll use this to
  decode and embedders can use any decoder they want.
  
  There is no C API exposed yet to set this, so this is only for Zig to
  start.
  
  ## Examples (Zig)
  
  ### Configuring Allowed Formats
  
  ```zig
  var term = try Terminal.init(alloc, .{
      .cols = 80,
      .rows = 24,
      // Only allow direct (inline) image data, no file/shm access.
      // This is the default so you don't need to specify it.
      .kitty_image_loading_limits = .direct,
  });
  ```
  
  ```zig
  var term = try Terminal.init(alloc, .{
      .cols = 80,
      .rows = 24,
      // Allow all transmission mediums: direct, file, temporary file, shared memory.
      .kitty_image_loading_limits = .all,
  });
  ```
  
  ```zig
  var term = try Terminal.init(alloc, .{
      .cols = 80,
      .rows = 24,
      .kitty_image_loading_limits = .{
          .file = true,
          .temporary_file = true,
          .shared_memory = false,
      },
  });
  ```
  
  ### Iterate all images
  
  ```zig
  var it = term.screens.active.kitty_images.images.iterator();
  while (it.next()) |kv| {
      const img = kv.value_ptr;
      std.debug.print("id={} {}x{} format={} bytes={}\n", .{
          img.id, img.width, img.height, img.format, img.data.len,
      });
  }
  ```
  
  ### Delete all images
  
  ```zig
  term.screens.active.kitty_images.delete(alloc, &term, .{ .all = true });
  ```
  ````
- [`841a49a`](https://github.com/ghostty-org/ghostty/commit/841a49ae1a25cda91a50e4f8ebac4811503081fa) Update VOUCHED list ([#12138](https://github.com/ghostty-org/ghostty/issues/12138)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12137#discussioncomment-16460337)
  from @rhodes-b.
  
  Vouch: @neurosnap
  ```

## April 5, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/24011311343), [2](https://github.com/ghostty-org/ghostty/actions/runs/23999805792), [3](https://github.com/ghostty-org/ghostty/actions/runs/23994374178), [4](https://github.com/ghostty-org/ghostty/actions/runs/23993802101), [5](https://github.com/ghostty-org/ghostty/actions/runs/23993258076)  
Summary: 5 runs • 9 commits • 2 authors

### Changes

- [`4f543ff`](https://github.com/ghostty-org/ghostty/commit/4f543ff3d80fc33eaab2740b60356cf8ef96eed9) Update VOUCHED list ([#12135](https://github.com/ghostty-org/ghostty/issues/12135)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12133#issuecomment-4189589541)
  from @jcollie.
  
  Vouch: @KayLeung
  ```
- [`ba398df`](https://github.com/ghostty-org/ghostty/commit/ba398dfff3e30ff83da07140981ca138410cf608) Update VOUCHED list ([#12123](https://github.com/ghostty-org/ghostty/issues/12123)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12119#issuecomment-4188681042)
  from @bo2themax.
  
  Vouch: @jamylak
  ```
- [`a8e92c9`](https://github.com/ghostty-org/ghostty/commit/a8e92c9c53e5c6018507c6f1e06af4f3b3e4f49c) terminal: add APC handler to stream_terminal ([@mitchellh](https://github.com/mitchellh))
  ```text
  Wire up the APC handler to `terminal.TerminalStream` to process
  APC sequences, enabling support for kitty graphics commands in
  libghostty, in theory.
  
  The "in theory" is because we still don't export a way to actually
  enable Kitty graphics in libghostty because we have some other things in
  the way: PNG decoding and OS filesystem access that need to be more
  conditionally compiled before we can enable the feature. However, this
  is a step in the right direction, and we can at least verify that the
  APC handler works via a test in Ghostty GUI.
  ```
- [`c541ceb`](https://github.com/ghostty-org/ghostty/commit/c541ceb120ee48c3495fa9e115f1614cd2e13249) terminal: add APC handler to stream_terminal ([#12116](https://github.com/ghostty-org/ghostty/issues/12116)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Wire up the APC handler to `terminal.TerminalStream` to process APC
  sequences, enabling support for kitty graphics commands in libghostty,
  in theory.
  
  The "in theory" is because we still don't export a way to actually
  enable Kitty graphics in libghostty because we have some other things in
  the way: PNG decoding and OS filesystem access that need to be more
  conditionally compiled before we can enable the feature. However, this
  is a step in the right direction, and we can at least verify that the
  APC handler works via a test in Ghostty GUI.
  ```
- [`b9a241d`](https://github.com/ghostty-org/ghostty/commit/b9a241d1e237fa97bf8b3b161f253cc2313100f2) libghostty: add hyperlink URI accessor to grid_ref API ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add ghostty_grid_ref_hyperlink_uri to extract the OSC 8 hyperlink
  URI from a cell at a grid reference position. Follows the same
  buffer pattern as ghostty_grid_ref_graphemes: callers pass a buffer
  and get back the byte length, or GHOSTTY_OUT_OF_SPACE with the
  required size if the buffer is too small. Cells without a hyperlink
  return success with length 0.
  ```
- [`757eff5`](https://github.com/ghostty-org/ghostty/commit/757eff5881b9afb811a99497fb5c231cc3677a6b) libghostty: add GhosttySelection type and selection support to formatter ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a new GhosttySelection C API type (selection.h / c/selection.zig)
  that pairs two GhosttyGridRef endpoints with a rectangle flag. This
  maps directly to the internal Selection type using untracked pins.
  
  The formatter terminal options gain an optional selection pointer.
  When non-null the formatter restricts output to the specified range
  instead of emitting the entire screen. When null the existing
  behavior of formatting the full screen is preserved.
  ```
- [`86554de`](https://github.com/ghostty-org/ghostty/commit/86554de090cdd5e9322652146e202a468a5e4bb5) libghostty: add hyperlink URI accessor to grid_ref API ([#12114](https://github.com/ghostty-org/ghostty/issues/12114)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add ghostty_grid_ref_hyperlink_uri to extract the OSC 8 hyperlink URI
  from a cell at a grid reference position. Follows the same buffer
  pattern as ghostty_grid_ref_graphemes: callers pass a buffer and get
  back the byte length, or GHOSTTY_OUT_OF_SPACE with the required size if
  the buffer is too small. Cells without a hyperlink return success with
  length 0.
  ```
- [`10696b5`](https://github.com/ghostty-org/ghostty/commit/10696b5ed170090df09f06a9afeeefe643159f40) libghostty: add GhosttySelection type and selection support to formatter ([#12115](https://github.com/ghostty-org/ghostty/issues/12115)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  Add a new GhosttySelection C API type (selection.h / c/selection.zig)
  that pairs two GhosttyGridRef endpoints with a rectangle flag. This maps
  directly to the internal Selection type using untracked pins.
  
  The formatter terminal options gain an optional selection pointer. When
  non-null the formatter restricts output to the specified range instead
  of emitting the entire screen. When null the existing behavior of
  formatting the full screen is preserved.
  ```
- [`cf8a240`](https://github.com/ghostty-org/ghostty/commit/cf8a2407a042a2e407fe58ade93582af6073c49d) Update VOUCHED list ([#12113](https://github.com/ghostty-org/ghostty/issues/12113)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12098#discussioncomment-16452103)
  from @mitchellh.
  
  Vouch: @fru1tworld
  ```

## April 4, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23987875945), [2](https://github.com/ghostty-org/ghostty/actions/runs/23980573913), [3](https://github.com/ghostty-org/ghostty/actions/runs/23970370985), [4](https://github.com/ghostty-org/ghostty/actions/runs/23968719391)  
Summary: 4 runs • 8 commits • 3 authors

### Changes

- [`1bd7c19`](https://github.com/ghostty-org/ghostty/commit/1bd7c19dac8cfa03b5c6b24bf6c7e6703c30c151) nix: add option to disable simd in libghostty-vt package ([@jcollie](https://github.com/jcollie))
- [`0a4cf58`](https://github.com/ghostty-org/ghostty/commit/0a4cf5877e4b325b1c3dba1833cbcafa2ed42ec7) nix: add option to disable simd in libghostty-vt package ([#12103](https://github.com/ghostty-org/ghostty/issues/12103)) ([@jcollie](https://github.com/jcollie))
- [`e157dd6`](https://github.com/ghostty-org/ghostty/commit/e157dd69c57a39f8d3a88b12e050e69830bfb1d5) build: add pkg-config static linking support and fat archives to libghostty ([@mitchellh](https://github.com/mitchellh))
  ```text
  The libghostty-vt pkg-config file was missing Libs.private, so
  pkg-config --libs --static returned the same flags as the shared
  case, omitting the C++ standard library needed by the SIMD code.
  
  Additionally, the static archive did not bundle the vendored SIMD
  dependencies (simdutf, highway, utfcpp), leaving consumers with
  unresolved symbols when linking. If we're choosing to vendor (no -fsys)
  then we should produce a fat static archive that includes them. If `-fsys`
  is used, then we should not bundle them and instead reference them via
  Requires.private, letting pkg-config chain to their own .pc files.
  
  Add Libs.private with the C++ runtime (-lc++ on Darwin, -lstdc++
  on Linux) and Requires.private for any SIMD deps provided via
  system integration. When SIMD deps are vendored (the default),
  produce a fat static archive that bundles them using libtool on
  Darwin and ar on Linux. When they come from the system (-fsys=),
  reference them via Requires.private instead, letting pkg-config
  chain to their own .pc files.
  ```
- [`0a492fd`](https://github.com/ghostty-org/ghostty/commit/0a492fdb331f1e0be29aedbcc78c3c852cb437f2) build: add pkg-config static linking support and fat archives to libghostty ([#12096](https://github.com/ghostty-org/ghostty/issues/12096)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  The libghostty-vt pkg-config file was missing Libs.private, so
  pkg-config --libs --static returned the same flags as the shared case,
  omitting the C++ standard library needed by the SIMD code.
  
  Additionally, the static archive did not bundle the vendored SIMD
  dependencies (simdutf, highway, utfcpp), leaving consumers with
  unresolved symbols when linking. If we're choosing to vendor (no -fsys)
  then we should produce a fat static archive that includes them. If
  `-fsys` is used, then we should not bundle them and instead reference
  them via Requires.private, letting pkg-config chain to their own .pc
  files.
  
  Add Libs.private with the C++ runtime (-lc++ on Darwin, -lstdc++ on
  Linux) and Requires.private for any SIMD deps provided via system
  integration. When SIMD deps are vendored (the default), produce a fat
  static archive that bundles them using libtool on Darwin and ar on
  Linux. When they come from the system (-fsys=), reference them via
  Requires.private instead, letting pkg-config chain to their own .pc
  files.
  ```
- [`4f825e8`](https://github.com/ghostty-org/ghostty/commit/4f825e87f5f848347669e18e507aea91b1fb26ab) add a nix package (with CI tests) for libghostty-vt ([@jcollie](https://github.com/jcollie))
- [`326178a`](https://github.com/ghostty-org/ghostty/commit/326178adb80db39dc9e62a8c58740dc2cac3c061) nix: address review comments ([@jcollie](https://github.com/jcollie))
  ```text
  * split out dev subpackage
  * change version number to 0.1.0
  * supported on same platforms as Zig
  ```
- [`707cd57`](https://github.com/ghostty-org/ghostty/commit/707cd57acb8e79923a14ae39b1b582ed683c008b) add a nix package (with CI tests) for libghostty-vt ([#12090](https://github.com/ghostty-org/ghostty/issues/12090)) ([@mitchellh](https://github.com/mitchellh))
- [`e3bbd54`](https://github.com/ghostty-org/ghostty/commit/e3bbd54dd3bc63d00f536e086e28c33daf3f06d0) Update VOUCHED list ([#12094](https://github.com/ghostty-org/ghostty/issues/12094)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12093#discussioncomment-16444399)
  from @jcollie.
  
  Vouch: @jordandm
  ```

## April 2, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23919753798), [2](https://github.com/ghostty-org/ghostty/actions/runs/23913311718), [3](https://github.com/ghostty-org/ghostty/actions/runs/23903937555)  
Summary: 3 runs • 4 commits • 3 authors

### Changes

- [`18f2702`](https://github.com/ghostty-org/ghostty/commit/18f270222557fd46d8c3305da523212445066154) macOS: fix Find Next/Previous button in the menu bar is not working as expected ([@bo2themax](https://github.com/bo2themax))
- [`0790937`](https://github.com/ghostty-org/ghostty/commit/0790937d03df6e7a9420c61de91ce520a85fe4ef) macOS: fix Find Next/Previous button in the menu bar is not working as expected ([#12070](https://github.com/ghostty-org/ghostty/issues/12070)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  I don’t know why the search-related commands were added as performable
  keybinds in 240d5e0fc56d1b24fa9795335a3e38365190661a, but **I asked
  Claude to add some tests for that**
  
  > This won't fix cmd+g/G not working when the search bar is focused.
  ```
- [`7747c96`](https://github.com/ghostty-org/ghostty/commit/7747c96033dd435db9f7e00649178993a7791dc8) Update VOUCHED list ([#12069](https://github.com/ghostty-org/ghostty/issues/12069)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12068#issuecomment-4179350272)
  from @jcollie.
  
  Vouch: @Douglas-MacGregor
  ```
- [`63372f8`](https://github.com/ghostty-org/ghostty/commit/63372f8ddb26fa1514da2c40fc77c48076a9e4da) Update VOUCHED list ([#12066](https://github.com/ghostty-org/ghostty/issues/12066)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by [discussion
  comment](https://github.com/ghostty-org/ghostty/discussions/12038#discussioncomment-16423690)
  from @mitchellh.
  
  Vouch: @h3nock
  ```

## April 1, 2026

Runs: [1](https://github.com/ghostty-org/ghostty/actions/runs/23874449602), [2](https://github.com/ghostty-org/ghostty/actions/runs/23872415256), [3](https://github.com/ghostty-org/ghostty/actions/runs/23856480951), [4](https://github.com/ghostty-org/ghostty/actions/runs/23853671581), [5](https://github.com/ghostty-org/ghostty/actions/runs/23832732331)  
Summary: 5 runs • 10 commits • 5 authors

### Changes

- [`48d3e97`](https://github.com/ghostty-org/ghostty/commit/48d3e972d839999745368b156df396d9512fd17b) Update VOUCHED list ([#12052](https://github.com/ghostty-org/ghostty/issues/12052)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12050#issuecomment-4173393542)
  from @mitchellh.
  
  Vouch: @justonia
  ```
- [`9ec5672`](https://github.com/ghostty-org/ghostty/commit/9ec5672505cf9cb61006b23e799dfc154b3f7b22) Revert "macOS: close search bar if needed when it loses focus ([#11980](https://github.com/ghostty-org/ghostty/issues/11980))" ([@bo2themax](https://github.com/bo2themax))
  ```text
  This reverts commit 20cfaae2e5ec84cca2c5a55843b399b32fb9c810, reversing
  changes made to 3509ccf78ef087fec2f0209fbc297a321106d339.
  ```
- [`c16cf0e`](https://github.com/ghostty-org/ghostty/commit/c16cf0ef07edf60db1accaed1b8c6a3ba99d2dcd) fix: Ensure snap paths come first in gio module loading ([@kenvandine](https://github.com/kenvandine))
- [`92a4601`](https://github.com/ghostty-org/ghostty/commit/92a4601f39de1f9b566be45f6c02756e2145a0a7) Revert "macOS: close search bar if needed when it loses focus ([#11980](https://github.com/ghostty-org/ghostty/issues/11980))" ([#12046](https://github.com/ghostty-org/ghostty/issues/12046)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This reverts commit 20cfaae2e5ec84cca2c5a55843b399b32fb9c810, reversing
  changes made to 3509ccf78ef087fec2f0209fbc297a321106d339.
  
  This breaks some behaviours when there are multiple splits, which
  requires another click to focus to another split in the same window🫪
  ```
- [`b8251de`](https://github.com/ghostty-org/ghostty/commit/b8251de7e8656ae4a848856f00f1003347ad37d7) fix: Ensure snap paths come first in gio module loading ([#12045](https://github.com/ghostty-org/ghostty/issues/12045)) ([@mitchellh](https://github.com/mitchellh))
  ```text
  This fixes the issue reported in
  https://github.com/ghostty-org/ghostty/discussions/11311
  ```
- [`702a2b4`](https://github.com/ghostty-org/ghostty/commit/702a2b43c35b8960bdd2930b64e742a33c7ca1b9) macOS: fix upper cased letter is not correctly mapped to menu shortcut ([@bo2themax](https://github.com/bo2themax))
- [`f6e6bb0`](https://github.com/ghostty-org/ghostty/commit/f6e6bb0238cbf4ce8c154c07f5df8c5109dc9f03) macOS: fix upper cased letter is not correctly mapped to menu shortcut ([#12039](https://github.com/ghostty-org/ghostty/issues/12039)) ([@mitchellh](https://github.com/mitchellh))
  ````text
  This is known issues before key-related PRs, tested on
  fa9265636b6e14e012b9990868f60a6d2376fe59.
  
  The following config is mapped incorrectly to the menu shortcut:
  ```
  keybind=A=goto_split:left
  ```
  <img width="223" height="106" alt="image"
  src="https://github.com/user-attachments/assets/b80da251-9cff-4b29-b143-64854a5c4271"
  />
  
  Surfaces only accept `a` as a trigger to select left split, not
  `shift+a`
  ````
- [`c8702ec`](https://github.com/ghostty-org/ghostty/commit/c8702ece8f8db400df95b767fc03b401dce0d015) gtk(chore): fix typos ([@bo2themax](https://github.com/bo2themax))
  ```text
  ### AI Disclosure
  
  Claude wrote the regex to ignore base64-encoded sequences
  ```
- [`6d15b53`](https://github.com/ghostty-org/ghostty/commit/6d15b53fc753cb8087f230d1d922b2e95c526b20) gtk(chore): fix typos ([#12036](https://github.com/ghostty-org/ghostty/issues/12036)) ([@pluiedev](https://github.com/pluiedev))
- [`b7e5604`](https://github.com/ghostty-org/ghostty/commit/b7e56044dbe3265495f3578fa5764e3bb5a433f0) Update VOUCHED list ([#12031](https://github.com/ghostty-org/ghostty/issues/12031)) ([@ghostty-vouch[bot]](https://github.com/apps/ghostty-vouch))
  ```text
  Triggered by
  [comment](https://github.com/ghostty-org/ghostty/issues/12030#issuecomment-4167464133)
  from @mitchellh.
  
  Vouch: @Jarred-Sumner
  ```

